# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Non-healthy group (T2D non-insulin + T2D insulin)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 229; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **229**, R² = **0.1608**, Adj R² = **0.1223**, F-statistic = **4.18** (p = **2.64e-05**), Residual SE = **4.486** on **218** df, AIC = **1348.1**, BIC = **1385.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5522** | 2.5509 | ±5.1018 | **+3.353** | **8.01e-04** | *** |
| Education: graduate level (vs college) | -0.8676 | 0.6531 | ±1.3061 | -1.329 | 0.1840 |  |
| Education: high school or below (vs college) | +1.9976 | 1.0742 | ±2.1484 | +1.860 | 0.0629 | . |
| Site: UCSD (vs UAB) | +1.5738 | 0.8626 | ±1.7253 | +1.824 | 0.0681 | . |
| Site: UW (vs UAB) | -1.3343 | 0.6873 | ±1.3747 | -1.941 | 0.0522 | . |
| **Age (years)** | **-0.0841** | 0.0278 | ±0.0556 | **-3.025** | **0.0025** | ** |
| BMI (kg/m2) | +0.0675 | 0.0399 | ±0.0798 | +1.692 | 0.0906 | . |
| Hypertension | -0.3056 | 0.7533 | ±1.5065 | -0.406 | 0.6850 |  |
| High cholesterol | +1.0335 | 0.6424 | ±1.2847 | +1.609 | 0.1076 |  |
| Kidney disease | +1.8051 | 0.9734 | ±1.9467 | +1.855 | 0.0637 | . |
| Circulatory disease | +0.3732 | 0.7063 | ±1.4126 | +0.528 | 0.5972 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **229**, R² = **0.1749**, Adj R² = **0.1330**, F-statistic = **4.18** (p = **1.30e-05**), Residual SE = **4.459** on **217** df, AIC = **1346.2**, BIC = **1387.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.7464 | 2.9367 | ±5.8734 | +1.957 | 0.0504 | . |
| Education: graduate level (vs college) | -0.7091 | 0.6628 | ±1.3255 | -1.070 | 0.2846 |  |
| Education: high school or below (vs college) | +1.8303 | 1.0515 | ±2.1030 | +1.741 | 0.0817 | . |
| Site: UCSD (vs UAB) | +1.6018 | 0.8496 | ±1.6992 | +1.885 | 0.0594 | . |
| Site: UW (vs UAB) | -1.2711 | 0.6927 | ±1.3853 | -1.835 | 0.0665 | . |
| **Age (years)** | **-0.0925** | 0.0291 | ±0.0582 | **-3.179** | **0.0015** | ** |
| BMI (kg/m2) | +0.0650 | 0.0402 | ±0.0804 | +1.617 | 0.1059 |  |
| Hypertension | -0.3687 | 0.7489 | ±1.4979 | -0.492 | 0.6225 |  |
| High cholesterol | +1.0854 | 0.6377 | ±1.2755 | +1.702 | 0.0888 | . |
| Kidney disease | +1.7622 | 0.9897 | ±1.9793 | +1.781 | 0.0750 | . |
| Circulatory disease | +0.3653 | 0.7012 | ±1.4023 | +0.521 | 0.6023 |  |
| HbA1c (%) | +0.5242 | 0.3200 | ±0.6400 | +1.638 | 0.1013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **229**, R² = **0.1765**, Adj R² = **0.1348**, F-statistic = **4.23** (p = **1.09e-05**), Residual SE = **4.454** on **217** df, AIC = **1345.7**, BIC = **1386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9832** | 2.7438 | ±5.4876 | **+2.181** | **0.0292** | * |
| Education: graduate level (vs college) | -0.8216 | 0.6583 | ±1.3167 | -1.248 | 0.2120 |  |
| Education: high school or below (vs college) | +1.8407 | 1.0535 | ±2.1070 | +1.747 | 0.0806 | . |
| Site: UCSD (vs UAB) | +1.5767 | 0.8504 | ±1.7009 | +1.854 | 0.0637 | . |
| Site: UW (vs UAB) | -1.2718 | 0.6966 | ±1.3932 | -1.826 | 0.0679 | . |
| **Age (years)** | **-0.0845** | 0.0281 | ±0.0561 | **-3.010** | **0.0026** | ** |
| BMI (kg/m2) | +0.0679 | 0.0396 | ±0.0793 | +1.712 | 0.0870 | . |
| Hypertension | -0.3486 | 0.7444 | ±1.4888 | -0.468 | 0.6395 |  |
| High cholesterol | +1.0576 | 0.6347 | ±1.2695 | +1.666 | 0.0957 | . |
| Kidney disease | +1.6497 | 1.0058 | ±2.0117 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.3197 | 0.6942 | ±1.3884 | +0.460 | 0.6452 |  |
| **Mean glucose (mg/dL)** | **+0.0193** | 0.0097 | ±0.0194 | **+1.989** | **0.0467** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **229**, R² = **0.1765**, Adj R² = **0.1348**, F-statistic = **4.23** (p = **1.09e-05**), Residual SE = **4.454** on **217** df, AIC = **1345.7**, BIC = **1386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3109 | 3.4847 | ±6.9694 | +0.950 | 0.3420 |  |
| Education: graduate level (vs college) | -0.8216 | 0.6583 | ±1.3167 | -1.248 | 0.2120 |  |
| Education: high school or below (vs college) | +1.8407 | 1.0535 | ±2.1070 | +1.747 | 0.0806 | . |
| Site: UCSD (vs UAB) | +1.5767 | 0.8504 | ±1.7009 | +1.854 | 0.0637 | . |
| Site: UW (vs UAB) | -1.2718 | 0.6966 | ±1.3932 | -1.826 | 0.0679 | . |
| **Age (years)** | **-0.0845** | 0.0281 | ±0.0561 | **-3.010** | **0.0026** | ** |
| BMI (kg/m2) | +0.0679 | 0.0396 | ±0.0793 | +1.712 | 0.0870 | . |
| Hypertension | -0.3486 | 0.7444 | ±1.4888 | -0.468 | 0.6395 |  |
| High cholesterol | +1.0576 | 0.6347 | ±1.2695 | +1.666 | 0.0957 | . |
| Kidney disease | +1.6497 | 1.0058 | ±2.0117 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.3197 | 0.6942 | ±1.3884 | +0.460 | 0.6452 |  |
| **GMI (%)** | **+0.8073** | 0.4060 | ±0.8119 | **+1.989** | **0.0467** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **229**, R² = **0.1972**, Adj R² = **0.1565**, F-statistic = **4.85** (p = **1.10e-06**), Residual SE = **4.398** on **217** df, AIC = **1339.9**, BIC = **1381.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7106 | 2.7313 | ±5.4626 | +1.725 | 0.0846 | . |
| Education: graduate level (vs college) | -0.8917 | 0.6483 | ±1.2966 | -1.376 | 0.1690 |  |
| Education: high school or below (vs college) | +1.7787 | 1.0329 | ±2.0658 | +1.722 | 0.0851 | . |
| Site: UCSD (vs UAB) | +1.5764 | 0.8276 | ±1.6552 | +1.905 | 0.0568 | . |
| Site: UW (vs UAB) | -1.2638 | 0.6986 | ±1.3973 | -1.809 | 0.0705 | . |
| **Age (years)** | **-0.0797** | 0.0281 | ±0.0562 | **-2.838** | **0.0045** | ** |
| BMI (kg/m2) | +0.0661 | 0.0394 | ±0.0789 | +1.676 | 0.0938 | . |
| Hypertension | -0.4214 | 0.7352 | ±1.4705 | -0.573 | 0.5665 |  |
| High cholesterol | +0.9933 | 0.6225 | ±1.2449 | +1.596 | 0.1105 |  |
| Kidney disease | +1.7786 | 0.9924 | ±1.9848 | +1.792 | 0.0731 | . |
| Circulatory disease | +0.2916 | 0.6869 | ±1.3738 | +0.424 | 0.6712 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0289** | 0.0088 | ±0.0177 | **+3.271** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **229**, R² = **0.1831**, Adj R² = **0.1417**, F-statistic = **4.42** (p = **5.32e-06**), Residual SE = **4.436** on **217** df, AIC = **1343.9**, BIC = **1385.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3904** | 2.6034 | ±5.2067 | **+2.839** | **0.0045** | ** |
| Education: graduate level (vs college) | -0.6924 | 0.6585 | ±1.3170 | -1.051 | 0.2931 |  |
| Education: high school or below (vs college) | +1.6329 | 1.0683 | ±2.1366 | +1.529 | 0.1264 |  |
| Site: UCSD (vs UAB) | +1.6189 | 0.8499 | ±1.6999 | +1.905 | 0.0568 | . |
| Site: UW (vs UAB) | -1.2113 | 0.6876 | ±1.3752 | -1.762 | 0.0781 | . |
| **Age (years)** | **-0.0947** | 0.0286 | ±0.0572 | **-3.314** | **9.20e-04** | *** |
| BMI (kg/m2) | +0.0725 | 0.0408 | ±0.0816 | +1.778 | 0.0754 | . |
| Hypertension | -0.3425 | 0.7365 | ±1.4729 | -0.465 | 0.6419 |  |
| High cholesterol | +1.0969 | 0.6362 | ±1.2724 | +1.724 | 0.0847 | . |
| Kidney disease | +1.3303 | 1.0426 | ±2.0852 | +1.276 | 0.2020 |  |
| Circulatory disease | +0.3845 | 0.6948 | ±1.3896 | +0.553 | 0.5800 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0488** | 0.0218 | ±0.0436 | **+2.238** | **0.0252** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **229**, R² = **0.1760**, Adj R² = **0.1342**, F-statistic = **4.21** (p = **1.15e-05**), Residual SE = **4.456** on **217** df, AIC = **1345.9**, BIC = **1387.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5069** | 2.5984 | ±5.1969 | **+2.889** | **0.0039** | ** |
| Education: graduate level (vs college) | -0.7168 | 0.6602 | ±1.3204 | -1.086 | 0.2776 |  |
| Education: high school or below (vs college) | +1.6486 | 1.0874 | ±2.1747 | +1.516 | 0.1295 |  |
| Site: UCSD (vs UAB) | +1.6090 | 0.8560 | ±1.7119 | +1.880 | 0.0601 | . |
| Site: UW (vs UAB) | -1.2487 | 0.6895 | ±1.3789 | -1.811 | 0.0701 | . |
| **Age (years)** | **-0.0930** | 0.0285 | ±0.0569 | **-3.266** | **0.0011** | ** |
| BMI (kg/m2) | +0.0728 | 0.0406 | ±0.0812 | +1.792 | 0.0732 | . |
| Hypertension | -0.3115 | 0.7406 | ±1.4812 | -0.421 | 0.6740 |  |
| High cholesterol | +1.0741 | 0.6401 | ±1.2803 | +1.678 | 0.0933 | . |
| Kidney disease | +1.3989 | 1.0600 | ±2.1200 | +1.320 | 0.1869 |  |
| Circulatory disease | +0.4032 | 0.6986 | ±1.3972 | +0.577 | 0.5638 |  |
| Avg. daily SD (mg/dL) | +0.0476 | 0.0257 | ±0.0514 | +1.851 | 0.0642 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **229**, R² = **0.1713**, Adj R² = **0.1293**, F-statistic = **4.08** (p = **1.90e-05**), Residual SE = **4.468** on **217** df, AIC = **1347.2**, BIC = **1388.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2919** | 2.7322 | ±5.4645 | **+2.669** | **0.0076** | ** |
| Education: graduate level (vs college) | -0.7118 | 0.6563 | ±1.3127 | -1.085 | 0.2781 |  |
| Education: high school or below (vs college) | +1.7066 | 1.1043 | ±2.2085 | +1.545 | 0.1222 |  |
| Site: UCSD (vs UAB) | +1.6094 | 0.8597 | ±1.7194 | +1.872 | 0.0612 | . |
| Site: UW (vs UAB) | -1.2495 | 0.6831 | ±1.3662 | -1.829 | 0.0674 | . |
| **Age (years)** | **-0.0969** | 0.0290 | ±0.0580 | **-3.345** | **8.24e-04** | *** |
| BMI (kg/m2) | +0.0724 | 0.0414 | ±0.0828 | +1.749 | 0.0803 | . |
| Hypertension | -0.3106 | 0.7449 | ±1.4898 | -0.417 | 0.6767 |  |
| High cholesterol | +1.0726 | 0.6443 | ±1.2887 | +1.665 | 0.0960 | . |
| Kidney disease | +1.3982 | 1.0691 | ±2.1381 | +1.308 | 0.1909 |  |
| Circulatory disease | +0.3972 | 0.7074 | ±1.4149 | +0.561 | 0.5745 |  |
| CV (%) | +0.0775 | 0.0530 | ±0.1061 | +1.461 | 0.1439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **229**, R² = **0.1685**, Adj R² = **0.1264**, F-statistic = **4.00** (p = **2.55e-05**), Residual SE = **4.476** on **217** df, AIC = **1348.0**, BIC = **1389.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.7116** | 3.0177 | ±6.0354 | **+3.550** | **3.86e-04** | *** |
| Education: graduate level (vs college) | -0.7338 | 0.6613 | ±1.3226 | -1.110 | 0.2672 |  |
| Education: high school or below (vs college) | +1.7409 | 1.0989 | ±2.1977 | +1.584 | 0.1131 |  |
| Site: UCSD (vs UAB) | +1.5655 | 0.8604 | ±1.7208 | +1.820 | 0.0688 | . |
| Site: UW (vs UAB) | -1.2900 | 0.6876 | ±1.3752 | -1.876 | 0.0606 | . |
| **Age (years)** | **-0.0961** | 0.0287 | ±0.0574 | **-3.347** | **8.18e-04** | *** |
| BMI (kg/m2) | +0.0699 | 0.0404 | ±0.0808 | +1.730 | 0.0836 | . |
| Hypertension | -0.2859 | 0.7466 | ±1.4932 | -0.383 | 0.7018 |  |
| High cholesterol | +1.0690 | 0.6454 | ±1.2908 | +1.656 | 0.0976 | . |
| Kidney disease | +1.5581 | 1.0542 | ±2.1084 | +1.478 | 0.1394 |  |
| Circulatory disease | +0.3452 | 0.7128 | ±1.4256 | +0.484 | 0.6282 |  |
| Mean / SD ratio | -0.3374 | 0.2608 | ±0.5215 | -1.294 | 0.1957 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **229**, R² = **0.1622**, Adj R² = **0.1197**, F-statistic = **3.82** (p = **4.93e-05**), Residual SE = **4.493** on **217** df, AIC = **1349.7**, BIC = **1390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4421** | 2.9707 | ±5.9414 | **+3.178** | **0.0015** | ** |
| Education: graduate level (vs college) | -0.8041 | 0.6625 | ±1.3251 | -1.214 | 0.2248 |  |
| Education: high school or below (vs college) | +1.8880 | 1.1064 | ±2.2128 | +1.706 | 0.0879 | . |
| Site: UCSD (vs UAB) | +1.5608 | 0.8665 | ±1.7331 | +1.801 | 0.0717 | . |
| Site: UW (vs UAB) | -1.3259 | 0.6895 | ±1.3791 | -1.923 | 0.0545 | . |
| **Age (years)** | **-0.0893** | 0.0286 | ±0.0573 | **-3.120** | **0.0018** | ** |
| BMI (kg/m2) | +0.0688 | 0.0404 | ±0.0807 | +1.705 | 0.0883 | . |
| Hypertension | -0.2838 | 0.7513 | ±1.5026 | -0.378 | 0.7056 |  |
| High cholesterol | +1.0387 | 0.6466 | ±1.2933 | +1.606 | 0.1082 |  |
| Kidney disease | +1.7246 | 1.0271 | ±2.0542 | +1.679 | 0.0931 | . |
| Circulatory disease | +0.3705 | 0.7117 | ±1.4233 | +0.521 | 0.6026 |  |
| Avg. daily mean/SD | -0.1173 | 0.2071 | ±0.4143 | -0.566 | 0.5711 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **229**, R² = **0.1721**, Adj R² = **0.1301**, F-statistic = **4.10** (p = **1.75e-05**), Residual SE = **4.466** on **217** df, AIC = **1347.0**, BIC = **1388.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7872** | 2.7437 | ±5.4874 | **+2.474** | **0.0134** | * |
| Education: graduate level (vs college) | -0.7709 | 0.6612 | ±1.3224 | -1.166 | 0.2436 |  |
| Education: high school or below (vs college) | +1.6935 | 1.0645 | ±2.1290 | +1.591 | 0.1116 |  |
| Site: UCSD (vs UAB) | +1.5123 | 0.8601 | ±1.7202 | +1.758 | 0.0787 | . |
| Site: UW (vs UAB) | -1.2472 | 0.6951 | ±1.3902 | -1.794 | 0.0728 | . |
| **Age (years)** | **-0.0879** | 0.0276 | ±0.0553 | **-3.178** | **0.0015** | ** |
| BMI (kg/m2) | +0.0621 | 0.0403 | ±0.0807 | +1.540 | 0.1236 |  |
| Hypertension | -0.2604 | 0.7498 | ±1.4997 | -0.347 | 0.7284 |  |
| High cholesterol | +1.0082 | 0.6381 | ±1.2762 | +1.580 | 0.1141 |  |
| Kidney disease | +1.7942 | 0.9792 | ±1.9583 | +1.832 | 0.0669 | . |
| Circulatory disease | +0.3656 | 0.7052 | ±1.4103 | +0.519 | 0.6041 |  |
| MAG (mg/dL/h) | +0.0483 | 0.0300 | ±0.0601 | +1.607 | 0.1081 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **229**, R² = **0.1767**, Adj R² = **0.1350**, F-statistic = **4.23** (p = **1.06e-05**), Residual SE = **4.454** on **217** df, AIC = **1345.7**, BIC = **1386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.0140** | 2.6560 | ±5.3120 | **+2.641** | **0.0083** | ** |
| Education: graduate level (vs college) | -0.6994 | 0.6620 | ±1.3241 | -1.056 | 0.2907 |  |
| Education: high school or below (vs college) | +1.5964 | 1.0912 | ±2.1824 | +1.463 | 0.1435 |  |
| Site: UCSD (vs UAB) | +1.6051 | 0.8554 | ±1.7108 | +1.876 | 0.0606 | . |
| Site: UW (vs UAB) | -1.2778 | 0.6894 | ±1.3789 | -1.853 | 0.0638 | . |
| **Age (years)** | **-0.0928** | 0.0282 | ±0.0563 | **-3.296** | **9.80e-04** | *** |
| BMI (kg/m2) | +0.0739 | 0.0404 | ±0.0809 | +1.827 | 0.0678 | . |
| Hypertension | -0.2755 | 0.7407 | ±1.4814 | -0.372 | 0.7099 |  |
| High cholesterol | +1.0499 | 0.6394 | ±1.2789 | +1.642 | 0.1006 |  |
| Kidney disease | +1.4018 | 1.0651 | ±2.1302 | +1.316 | 0.1881 |  |
| Circulatory disease | +0.3516 | 0.7008 | ±1.4017 | +0.502 | 0.6159 |  |
| Avg. daily range (mg/dL) | +0.0138 | 0.0074 | ±0.0148 | +1.870 | 0.0615 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **229**, R² = **0.1948**, Adj R² = **0.1540**, F-statistic = **4.77** (p = **1.44e-06**), Residual SE = **4.404** on **217** df, AIC = **1340.6**, BIC = **1381.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7645** | 2.5995 | ±5.1991 | **+2.987** | **0.0028** | ** |
| Education: graduate level (vs college) | -0.6573 | 0.6464 | ±1.2927 | -1.017 | 0.3092 |  |
| Education: high school or below (vs college) | +1.8647 | 1.0319 | ±2.0638 | +1.807 | 0.0708 | . |
| Site: UCSD (vs UAB) | +1.5842 | 0.8391 | ±1.6782 | +1.888 | 0.0590 | . |
| Site: UW (vs UAB) | -1.1858 | 0.6816 | ±1.3633 | -1.740 | 0.0819 | . |
| **Age (years)** | **-0.0913** | 0.0290 | ±0.0580 | **-3.147** | **0.0017** | ** |
| BMI (kg/m2) | +0.0719 | 0.0409 | ±0.0817 | +1.761 | 0.0783 | . |
| Hypertension | -0.5047 | 0.7419 | ±1.4838 | -0.680 | 0.4963 |  |
| High cholesterol | +1.1001 | 0.6274 | ±1.2548 | +1.753 | 0.0795 | . |
| Kidney disease | +1.4192 | 0.9679 | ±1.9358 | +1.466 | 0.1426 |  |
| Circulatory disease | +0.2239 | 0.7027 | ±1.4055 | +0.319 | 0.7500 |  |
| **SD of daily means (mg/dL)** | **+0.0952** | 0.0358 | ±0.0716 | **+2.658** | **0.0079** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **229**, R² = **0.1793**, Adj R² = **0.1377**, F-statistic = **4.31** (p = **8.03e-06**), Residual SE = **4.447** on **217** df, AIC = **1345.0**, BIC = **1386.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8239** | 3.0680 | ±6.1359 | **+3.854** | **1.16e-04** | *** |
| Education: graduate level (vs college) | -0.7104 | 0.6563 | ±1.3126 | -1.082 | 0.2791 |  |
| Education: high school or below (vs college) | +1.8109 | 1.0612 | ±2.1223 | +1.707 | 0.0879 | . |
| Site: UCSD (vs UAB) | +1.6129 | 0.8472 | ±1.6943 | +1.904 | 0.0569 | . |
| Site: UW (vs UAB) | -1.2288 | 0.6918 | ±1.3836 | -1.776 | 0.0757 | . |
| **Age (years)** | **-0.0882** | 0.0281 | ±0.0563 | **-3.134** | **0.0017** | ** |
| BMI (kg/m2) | +0.0703 | 0.0398 | ±0.0795 | +1.768 | 0.0770 | . |
| Hypertension | -0.3049 | 0.7422 | ±1.4844 | -0.411 | 0.6812 |  |
| High cholesterol | +1.0077 | 0.6328 | ±1.2656 | +1.592 | 0.1113 |  |
| Kidney disease | +1.5286 | 1.0109 | ±2.0219 | +1.512 | 0.1305 |  |
| Circulatory disease | +0.2871 | 0.6979 | ±1.3958 | +0.411 | 0.6808 |  |
| **Time in range 70-180, pooled (%)** | **-0.0370** | 0.0172 | ±0.0343 | **-2.157** | **0.0310** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **229**, R² = **0.1793**, Adj R² = **0.1377**, F-statistic = **4.31** (p = **8.03e-06**), Residual SE = **4.447** on **217** df, AIC = **1345.0**, BIC = **1386.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8151** | 3.0789 | ±6.1577 | **+3.838** | **1.24e-04** | *** |
| Education: graduate level (vs college) | -0.7111 | 0.6554 | ±1.3107 | -1.085 | 0.2779 |  |
| Education: high school or below (vs college) | +1.7924 | 1.0606 | ±2.1212 | +1.690 | 0.0910 | . |
| Site: UCSD (vs UAB) | +1.6175 | 0.8466 | ±1.6933 | +1.910 | 0.0561 | . |
| Site: UW (vs UAB) | -1.2214 | 0.6921 | ±1.3842 | -1.765 | 0.0776 | . |
| **Age (years)** | **-0.0882** | 0.0281 | ±0.0562 | **-3.138** | **0.0017** | ** |
| BMI (kg/m2) | +0.0708 | 0.0399 | ±0.0797 | +1.775 | 0.0758 | . |
| Hypertension | -0.2970 | 0.7423 | ±1.4846 | -0.400 | 0.6890 |  |
| High cholesterol | +1.0052 | 0.6325 | ±1.2650 | +1.589 | 0.1120 |  |
| Kidney disease | +1.5203 | 1.0078 | ±2.0156 | +1.508 | 0.1314 |  |
| Circulatory disease | +0.2861 | 0.6980 | ±1.3959 | +0.410 | 0.6819 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0370** | 0.0172 | ±0.0344 | **-2.149** | **0.0316** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **229**, R² = **0.1624**, Adj R² = **0.1199**, F-statistic = **3.82** (p = **4.84e-05**), Residual SE = **4.492** on **217** df, AIC = **1349.6**, BIC = **1390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6334** | 2.5531 | ±5.1061 | **+3.382** | **7.21e-04** | *** |
| Education: graduate level (vs college) | -0.8906 | 0.6580 | ±1.3160 | -1.354 | 0.1759 |  |
| Education: high school or below (vs college) | +1.9636 | 1.0695 | ±2.1390 | +1.836 | 0.0664 | . |
| Site: UCSD (vs UAB) | +1.5105 | 0.8727 | ±1.7453 | +1.731 | 0.0835 | . |
| **Site: UW (vs UAB)** | **-1.4089** | 0.7030 | ±1.4060 | **-2.004** | **0.0451** | * |
| **Age (years)** | **-0.0835** | 0.0278 | ±0.0556 | **-3.003** | **0.0027** | ** |
| BMI (kg/m2) | +0.0679 | 0.0398 | ±0.0796 | +1.707 | 0.0878 | . |
| Hypertension | -0.2938 | 0.7517 | ±1.5034 | -0.391 | 0.6959 |  |
| High cholesterol | +1.0418 | 0.6450 | ±1.2900 | +1.615 | 0.1063 |  |
| Kidney disease | +1.7913 | 0.9720 | ±1.9440 | +1.843 | 0.0653 | . |
| Circulatory disease | +0.4170 | 0.7183 | ±1.4367 | +0.581 | 0.5616 |  |
| Time < 54 (%) | -0.2639 | 0.4016 | ±0.8032 | -0.657 | 0.5111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **229**, R² = **0.1610**, Adj R² = **0.1185**, F-statistic = **3.79** (p = **5.57e-05**), Residual SE = **4.496** on **217** df, AIC = **1350.0**, BIC = **1391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5579** | 2.5529 | ±5.1058 | **+3.352** | **8.02e-04** | *** |
| Education: graduate level (vs college) | -0.8796 | 0.6556 | ±1.3113 | -1.342 | 0.1797 |  |
| Education: high school or below (vs college) | +1.9863 | 1.0715 | ±2.1430 | +1.854 | 0.0638 | . |
| Site: UCSD (vs UAB) | +1.5555 | 0.8649 | ±1.7297 | +1.799 | 0.0721 | . |
| Site: UW (vs UAB) | -1.3542 | 0.6965 | ±1.3930 | -1.944 | 0.0519 | . |
| **Age (years)** | **-0.0836** | 0.0282 | ±0.0564 | **-2.965** | **0.0030** | ** |
| BMI (kg/m2) | +0.0675 | 0.0401 | ±0.0802 | +1.685 | 0.0920 | . |
| Hypertension | -0.3038 | 0.7547 | ±1.5093 | -0.403 | 0.6872 |  |
| High cholesterol | +1.0299 | 0.6472 | ±1.2945 | +1.591 | 0.1116 |  |
| Kidney disease | +1.8062 | 0.9747 | ±1.9494 | +1.853 | 0.0639 | . |
| Circulatory disease | +0.3877 | 0.7319 | ±1.4639 | +0.530 | 0.5963 |  |
| Avg. daily time < 54 (%) | -0.0876 | 0.6516 | ±1.3031 | -0.134 | 0.8930 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **229**, R² = **0.1625**, Adj R² = **0.1201**, F-statistic = **3.83** (p = **4.77e-05**), Residual SE = **4.492** on **217** df, AIC = **1349.6**, BIC = **1390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5492** | 2.5599 | ±5.1197 | **+3.340** | **8.39e-04** | *** |
| Education: graduate level (vs college) | -0.8016 | 0.6608 | ±1.3217 | -1.213 | 0.2251 |  |
| Education: high school or below (vs college) | +1.9760 | 1.0855 | ±2.1710 | +1.820 | 0.0687 | . |
| Site: UCSD (vs UAB) | +1.6034 | 0.8625 | ±1.7251 | +1.859 | 0.0630 | . |
| Site: UW (vs UAB) | -1.3184 | 0.6866 | ±1.3731 | -1.920 | 0.0548 | . |
| **Age (years)** | **-0.0869** | 0.0277 | ±0.0554 | **-3.138** | **0.0017** | ** |
| BMI (kg/m2) | +0.0680 | 0.0401 | ±0.0801 | +1.696 | 0.0899 | . |
| Hypertension | -0.2870 | 0.7591 | ±1.5181 | -0.378 | 0.7053 |  |
| High cholesterol | +1.0104 | 0.6463 | ±1.2926 | +1.563 | 0.1180 |  |
| Kidney disease | +1.7856 | 0.9743 | ±1.9485 | +1.833 | 0.0668 | . |
| Circulatory disease | +0.3640 | 0.7169 | ±1.4337 | +0.508 | 0.6116 |  |
| Time 54-69, pooled (%) | +0.0813 | 0.1244 | ±0.2489 | +0.654 | 0.5133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **229**, R² = **0.1633**, Adj R² = **0.1209**, F-statistic = **3.85** (p = **4.39e-05**), Residual SE = **4.490** on **217** df, AIC = **1349.4**, BIC = **1390.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5922** | 2.5600 | ±5.1201 | **+3.356** | **7.90e-04** | *** |
| Education: graduate level (vs college) | -0.7872 | 0.6604 | ±1.3209 | -1.192 | 0.2333 |  |
| Education: high school or below (vs college) | +1.9630 | 1.0881 | ±2.1762 | +1.804 | 0.0712 | . |
| Site: UCSD (vs UAB) | +1.6065 | 0.8615 | ±1.7231 | +1.865 | 0.0622 | . |
| Site: UW (vs UAB) | -1.3124 | 0.6853 | ±1.3705 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.0880** | 0.0278 | ±0.0556 | **-3.166** | **0.0015** | ** |
| BMI (kg/m2) | +0.0679 | 0.0401 | ±0.0802 | +1.693 | 0.0905 | . |
| Hypertension | -0.2830 | 0.7593 | ±1.5186 | -0.373 | 0.7093 |  |
| High cholesterol | +1.0101 | 0.6478 | ±1.2956 | +1.559 | 0.1189 |  |
| Kidney disease | +1.7863 | 0.9721 | ±1.9442 | +1.838 | 0.0661 | . |
| Circulatory disease | +0.3688 | 0.7157 | ±1.4314 | +0.515 | 0.6063 |  |
| Avg. daily time 54-69 (%) | +0.0941 | 0.1224 | ±0.2448 | +0.769 | 0.4420 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **229**, R² = **0.1614**, Adj R² = **0.1189**, F-statistic = **3.80** (p = **5.35e-05**), Residual SE = **4.495** on **217** df, AIC = **1349.9**, BIC = **1391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5383** | 2.5607 | ±5.1213 | **+3.334** | **8.55e-04** | *** |
| Education: graduate level (vs college) | -0.8314 | 0.6600 | ±1.3200 | -1.260 | 0.2078 |  |
| Education: high school or below (vs college) | +1.9921 | 1.0813 | ±2.1626 | +1.842 | 0.0654 | . |
| Site: UCSD (vs UAB) | +1.5981 | 0.8638 | ±1.7276 | +1.850 | 0.0643 | . |
| Site: UW (vs UAB) | -1.3151 | 0.6883 | ±1.3765 | -1.911 | 0.0560 | . |
| **Age (years)** | **-0.0856** | 0.0278 | ±0.0555 | **-3.085** | **0.0020** | ** |
| BMI (kg/m2) | +0.0677 | 0.0401 | ±0.0802 | +1.687 | 0.0915 | . |
| Hypertension | -0.2982 | 0.7578 | ±1.5155 | -0.394 | 0.6939 |  |
| High cholesterol | +1.0208 | 0.6458 | ±1.2916 | +1.581 | 0.1140 |  |
| Kidney disease | +1.7976 | 0.9763 | ±1.9526 | +1.841 | 0.0656 | . |
| Circulatory disease | +0.3620 | 0.7192 | ±1.4385 | +0.503 | 0.6148 |  |
| Time < 70 (%) | +0.0402 | 0.1096 | ±0.2193 | +0.367 | 0.7137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **229**, R² = **0.1622**, Adj R² = **0.1197**, F-statistic = **3.82** (p = **4.93e-05**), Residual SE = **4.493** on **217** df, AIC = **1349.7**, BIC = **1390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5728** | 2.5605 | ±5.1209 | **+3.348** | **8.13e-04** | *** |
| Education: graduate level (vs college) | -0.8107 | 0.6592 | ±1.3185 | -1.230 | 0.2188 |  |
| Education: high school or below (vs college) | +1.9839 | 1.0837 | ±2.1674 | +1.831 | 0.0671 | . |
| Site: UCSD (vs UAB) | +1.6057 | 0.8615 | ±1.7231 | +1.864 | 0.0623 | . |
| Site: UW (vs UAB) | -1.3079 | 0.6862 | ±1.3723 | -1.906 | 0.0566 | . |
| **Age (years)** | **-0.0868** | 0.0279 | ±0.0558 | **-3.110** | **0.0019** | ** |
| BMI (kg/m2) | +0.0677 | 0.0402 | ±0.0803 | +1.686 | 0.0918 | . |
| Hypertension | -0.2930 | 0.7584 | ±1.5168 | -0.386 | 0.6993 |  |
| High cholesterol | +1.0216 | 0.6472 | ±1.2944 | +1.578 | 0.1145 |  |
| Kidney disease | +1.7929 | 0.9747 | ±1.9493 | +1.840 | 0.0658 | . |
| Circulatory disease | +0.3610 | 0.7187 | ±1.4374 | +0.502 | 0.6154 |  |
| Avg. daily time < 70 (%) | +0.0574 | 0.1101 | ±0.2202 | +0.521 | 0.6021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **229**, R² = **0.2007**, Adj R² = **0.1601**, F-statistic = **4.95** (p = **7.42e-07**), Residual SE = **4.388** on **217** df, AIC = **1338.9**, BIC = **1380.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.6472** | 3.3273 | ±6.6545 | **+5.604** | **2.09e-08** | *** |
| Education: graduate level (vs college) | -0.7154 | 0.6531 | ±1.3062 | -1.095 | 0.2734 |  |
| Education: high school or below (vs college) | +1.7042 | 1.0275 | ±2.0549 | +1.659 | 0.0972 | . |
| **Site: UCSD (vs UAB)** | **+1.6658** | 0.8345 | ±1.6690 | **+1.996** | **0.0459** | * |
| Site: UW (vs UAB) | -1.0983 | 0.6870 | ±1.3739 | -1.599 | 0.1099 |  |
| **Age (years)** | **-0.0828** | 0.0274 | ±0.0547 | **-3.027** | **0.0025** | ** |
| BMI (kg/m2) | +0.0722 | 0.0398 | ±0.0795 | +1.815 | 0.0696 | . |
| Hypertension | -0.3801 | 0.7291 | ±1.4581 | -0.521 | 0.6022 |  |
| High cholesterol | +1.1457 | 0.6212 | ±1.2424 | +1.844 | 0.0651 | . |
| Kidney disease | +1.6182 | 0.9855 | ±1.9710 | +1.642 | 0.1006 |  |
| Circulatory disease | +0.2323 | 0.6886 | ±1.3772 | +0.337 | 0.7358 |  |
| **Time 54-250, pooled (%)** | **-0.1076** | 0.0250 | ±0.0500 | **-4.309** | **1.64e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **229**, R² = **0.1981**, Adj R² = **0.1575**, F-statistic = **4.87** (p = **9.92e-07**), Residual SE = **4.395** on **217** df, AIC = **1339.6**, BIC = **1380.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19.4982** | 3.8473 | ±7.6946 | **+5.068** | **4.02e-07** | *** |
| Education: graduate level (vs college) | -0.7061 | 0.6540 | ±1.3081 | -1.080 | 0.2803 |  |
| Education: high school or below (vs college) | +1.6579 | 1.0295 | ±2.0589 | +1.610 | 0.1073 |  |
| **Site: UCSD (vs UAB)** | **+1.6432** | 0.8341 | ±1.6681 | **+1.970** | **0.0488** | * |
| Site: UW (vs UAB) | -1.1277 | 0.6862 | ±1.3725 | -1.643 | 0.1003 |  |
| **Age (years)** | **-0.0842** | 0.0273 | ±0.0547 | **-3.079** | **0.0021** | ** |
| BMI (kg/m2) | +0.0737 | 0.0399 | ±0.0797 | +1.849 | 0.0645 | . |
| Hypertension | -0.3818 | 0.7315 | ±1.4629 | -0.522 | 0.6017 |  |
| High cholesterol | +1.1373 | 0.6220 | ±1.2441 | +1.828 | 0.0675 | . |
| Kidney disease | +1.5831 | 0.9815 | ±1.9630 | +1.613 | 0.1068 |  |
| Circulatory disease | +0.2017 | 0.6927 | ±1.3854 | +0.291 | 0.7709 |  |
| **Avg. daily time 54-250 (%)** | **-0.1154** | 0.0317 | ±0.0635 | **-3.635** | **2.78e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **229**, R² = **0.1627**, Adj R² = **0.1203**, F-statistic = **3.83** (p = **4.67e-05**), Residual SE = **4.491** on **217** df, AIC = **1349.5**, BIC = **1390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4570** | 2.5522 | ±5.1044 | **+3.314** | **9.21e-04** | *** |
| Education: graduate level (vs college) | -0.8321 | 0.6552 | ±1.3105 | -1.270 | 0.2041 |  |
| Education: high school or below (vs college) | +1.9616 | 1.0774 | ±2.1549 | +1.821 | 0.0687 | . |
| Site: UCSD (vs UAB) | +1.5709 | 0.8639 | ±1.7278 | +1.818 | 0.0690 | . |
| Site: UW (vs UAB) | -1.3262 | 0.6916 | ±1.3831 | -1.918 | 0.0551 | . |
| **Age (years)** | **-0.0857** | 0.0283 | ±0.0566 | **-3.030** | **0.0024** | ** |
| BMI (kg/m2) | +0.0680 | 0.0399 | ±0.0799 | +1.703 | 0.0887 | . |
| Hypertension | -0.2971 | 0.7531 | ±1.5063 | -0.394 | 0.6933 |  |
| High cholesterol | +1.0079 | 0.6430 | ±1.2859 | +1.568 | 0.1170 |  |
| Kidney disease | +1.7086 | 0.9995 | ±1.9990 | +1.709 | 0.0874 | . |
| Circulatory disease | +0.3574 | 0.7060 | ±1.4120 | +0.506 | 0.6127 |  |
| Time 181-250, pooled (%) | +0.0176 | 0.0252 | ±0.0505 | +0.697 | 0.4859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **229**, R² = **0.1642**, Adj R² = **0.1219**, F-statistic = **3.88** (p = **3.99e-05**), Residual SE = **4.487** on **217** df, AIC = **1349.1**, BIC = **1390.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3909** | 2.5497 | ±5.0994 | **+3.291** | **9.99e-04** | *** |
| Education: graduate level (vs college) | -0.8223 | 0.6549 | ±1.3098 | -1.256 | 0.2092 |  |
| Education: high school or below (vs college) | +1.9464 | 1.0756 | ±2.1512 | +1.810 | 0.0704 | . |
| Site: UCSD (vs UAB) | +1.5791 | 0.8617 | ±1.7234 | +1.833 | 0.0669 | . |
| Site: UW (vs UAB) | -1.3107 | 0.6918 | ±1.3836 | -1.895 | 0.0582 | . |
| **Age (years)** | **-0.0857** | 0.0282 | ±0.0565 | **-3.037** | **0.0024** | ** |
| BMI (kg/m2) | +0.0682 | 0.0399 | ±0.0799 | +1.708 | 0.0876 | . |
| Hypertension | -0.2906 | 0.7518 | ±1.5036 | -0.387 | 0.6991 |  |
| High cholesterol | +1.0011 | 0.6420 | ±1.2839 | +1.559 | 0.1189 |  |
| Kidney disease | +1.6774 | 1.0022 | ±2.0045 | +1.674 | 0.0942 | . |
| Circulatory disease | +0.3544 | 0.7049 | ±1.4099 | +0.503 | 0.6152 |  |
| Avg. daily time 181-250 (%) | +0.0229 | 0.0251 | ±0.0501 | +0.914 | 0.3609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **229**, R² = **0.1775**, Adj R² = **0.1358**, F-statistic = **4.26** (p = **9.73e-06**), Residual SE = **4.452** on **217** df, AIC = **1345.5**, BIC = **1386.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1620** | 2.5367 | ±5.0734 | **+3.218** | **0.0013** | ** |
| Education: graduate level (vs college) | -0.7521 | 0.6567 | ±1.3135 | -1.145 | 0.2521 |  |
| Education: high school or below (vs college) | +1.8283 | 1.0591 | ±2.1183 | +1.726 | 0.0843 | . |
| Site: UCSD (vs UAB) | +1.5894 | 0.8500 | ±1.7000 | +1.870 | 0.0615 | . |
| Site: UW (vs UAB) | -1.2525 | 0.6932 | ±1.3863 | -1.807 | 0.0708 | . |
| **Age (years)** | **-0.0867** | 0.0281 | ±0.0561 | **-3.087** | **0.0020** | ** |
| BMI (kg/m2) | +0.0700 | 0.0397 | ±0.0794 | +1.763 | 0.0779 | . |
| Hypertension | -0.3113 | 0.7430 | ±1.4861 | -0.419 | 0.6753 |  |
| High cholesterol | +1.0203 | 0.6335 | ±1.2669 | +1.611 | 0.1072 |  |
| Kidney disease | +1.5538 | 1.0108 | ±2.0216 | +1.537 | 0.1242 |  |
| Circulatory disease | +0.3026 | 0.6947 | ±1.3894 | +0.436 | 0.6631 |  |
| **Time > 180 (%)** | **+0.0345** | 0.0169 | ±0.0337 | **+2.048** | **0.0406** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **229**, R² = **0.1771**, Adj R² = **0.1354**, F-statistic = **4.25** (p = **1.02e-05**), Residual SE = **4.453** on **217** df, AIC = **1345.6**, BIC = **1386.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1383** | 2.5369 | ±5.0737 | **+3.208** | **0.0013** | ** |
| Education: graduate level (vs college) | -0.7567 | 0.6559 | ±1.3118 | -1.154 | 0.2487 |  |
| Education: high school or below (vs college) | +1.8158 | 1.0584 | ±2.1168 | +1.716 | 0.0862 | . |
| Site: UCSD (vs UAB) | +1.5952 | 0.8495 | ±1.6991 | +1.878 | 0.0604 | . |
| Site: UW (vs UAB) | -1.2455 | 0.6938 | ±1.3877 | -1.795 | 0.0726 | . |
| **Age (years)** | **-0.0863** | 0.0280 | ±0.0560 | **-3.082** | **0.0021** | ** |
| BMI (kg/m2) | +0.0704 | 0.0398 | ±0.0796 | +1.770 | 0.0767 | . |
| Hypertension | -0.3052 | 0.7432 | ±1.4864 | -0.411 | 0.6814 |  |
| High cholesterol | +1.0145 | 0.6333 | ±1.2665 | +1.602 | 0.1092 |  |
| Kidney disease | +1.5487 | 1.0078 | ±2.0157 | +1.537 | 0.1244 |  |
| Circulatory disease | +0.2998 | 0.6953 | ±1.3906 | +0.431 | 0.6663 |  |
| **Avg. daily time > 180 (%)** | **+0.0342** | 0.0169 | ±0.0338 | **+2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **229**, R² = **0.1978**, Adj R² = **0.1571**, F-statistic = **4.86** (p = **1.03e-06**), Residual SE = **4.396** on **217** df, AIC = **1339.8**, BIC = **1381.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0492** | 2.5434 | ±5.0869 | **+3.165** | **0.0016** | ** |
| Education: graduate level (vs college) | -0.7306 | 0.6481 | ±1.2963 | -1.127 | 0.2596 |  |
| Education: high school or below (vs college) | +1.8377 | 1.0384 | ±2.0768 | +1.770 | 0.0768 | . |
| **Site: UCSD (vs UAB)** | **+1.6320** | 0.8271 | ±1.6543 | **+1.973** | **0.0485** | * |
| Site: UW (vs UAB) | -1.2073 | 0.6881 | ±1.3762 | -1.755 | 0.0793 | . |
| **Age (years)** | **-0.0835** | 0.0279 | ±0.0558 | **-2.992** | **0.0028** | ** |
| BMI (kg/m2) | +0.0688 | 0.0397 | ±0.0793 | +1.735 | 0.0827 | . |
| Hypertension | -0.3931 | 0.7368 | ±1.4737 | -0.534 | 0.5937 |  |
| High cholesterol | +0.9560 | 0.6223 | ±1.2446 | +1.536 | 0.1245 |  |
| Kidney disease | +1.6711 | 0.9933 | ±1.9867 | +1.682 | 0.0925 | . |
| Circulatory disease | +0.2162 | 0.6913 | ±1.3825 | +0.313 | 0.7545 |  |
| **Nocturnal time > 180 (%)** | **+0.0515** | 0.0151 | ±0.0303 | **+3.402** | **6.69e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **229**, R² = **0.1757**, Adj R² = **0.1339**, F-statistic = **4.21** (p = **1.18e-05**), Residual SE = **4.456** on **217** df, AIC = **1346.0**, BIC = **1387.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1806** | 2.5366 | ±5.0733 | **+3.225** | **0.0013** | ** |
| Education: graduate level (vs college) | -0.7202 | 0.6482 | ±1.2964 | -1.111 | 0.2665 |  |
| Education: high school or below (vs college) | +1.8679 | 1.0641 | ±2.1282 | +1.755 | 0.0792 | . |
| Site: UCSD (vs UAB) | +1.5718 | 0.8630 | ±1.7259 | +1.821 | 0.0685 | . |
| **Site: UW (vs UAB)** | **-1.4349** | 0.6918 | ±1.3836 | **-2.074** | **0.0381** | * |
| **Age (years)** | **-0.0928** | 0.0280 | ±0.0561 | **-3.310** | **9.34e-04** | *** |
| BMI (kg/m2) | +0.0769 | 0.0398 | ±0.0796 | +1.932 | 0.0533 | . |
| Hypertension | -0.3357 | 0.7433 | ±1.4867 | -0.452 | 0.6515 |  |
| High cholesterol | +1.0632 | 0.6378 | ±1.2757 | +1.667 | 0.0955 | . |
| Kidney disease | +1.4865 | 1.0102 | ±2.0205 | +1.471 | 0.1412 |  |
| Circulatory disease | +0.3458 | 0.6960 | ±1.3919 | +0.497 | 0.6193 |  |
| Any reading > 250 during wear (0/1) | +1.2309 | 0.6483 | ±1.2967 | +1.899 | 0.0576 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **229**, R² = **0.2024**, Adj R² = **0.1620**, F-statistic = **5.01** (p = **6.08e-07**), Residual SE = **4.384** on **217** df, AIC = **1338.4**, BIC = **1379.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9008** | 2.5006 | ±5.0012 | **+3.160** | **0.0016** | ** |
| Education: graduate level (vs college) | -0.7209 | 0.6532 | ±1.3064 | -1.104 | 0.2697 |  |
| Education: high school or below (vs college) | +1.6819 | 1.0254 | ±2.0509 | +1.640 | 0.1010 |  |
| **Site: UCSD (vs UAB)** | **+1.6418** | 0.8345 | ±1.6690 | **+1.967** | **0.0491** | * |
| Site: UW (vs UAB) | -1.1232 | 0.6859 | ±1.3719 | -1.637 | 0.1015 |  |
| **Age (years)** | **-0.0825** | 0.0273 | ±0.0547 | **-3.018** | **0.0025** | ** |
| BMI (kg/m2) | +0.0725 | 0.0396 | ±0.0792 | +1.829 | 0.0675 | . |
| Hypertension | -0.3772 | 0.7284 | ±1.4567 | -0.518 | 0.6046 |  |
| High cholesterol | +1.1522 | 0.6202 | ±1.2405 | +1.858 | 0.0632 | . |
| Kidney disease | +1.6073 | 0.9846 | ±1.9692 | +1.632 | 0.1026 |  |
| Circulatory disease | +0.2469 | 0.6849 | ±1.3698 | +0.360 | 0.7185 |  |
| **Time > 250 (%)** | **+0.1105** | 0.0254 | ±0.0509 | **+4.346** | **1.38e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **229**, R² = **0.1995**, Adj R² = **0.1590**, F-statistic = **4.92** (p = **8.44e-07**), Residual SE = **4.392** on **217** df, AIC = **1339.2**, BIC = **1380.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9521** | 2.4986 | ±4.9972 | **+3.183** | **0.0015** | ** |
| Education: graduate level (vs college) | -0.7175 | 0.6536 | ±1.3072 | -1.098 | 0.2723 |  |
| Education: high school or below (vs college) | +1.6323 | 1.0284 | ±2.0568 | +1.587 | 0.1125 |  |
| Site: UCSD (vs UAB) | +1.6204 | 0.8343 | ±1.6687 | +1.942 | 0.0521 | . |
| Site: UW (vs UAB) | -1.1484 | 0.6858 | ±1.3716 | -1.675 | 0.0940 | . |
| **Age (years)** | **-0.0835** | 0.0273 | ±0.0546 | **-3.057** | **0.0022** | ** |
| BMI (kg/m2) | +0.0739 | 0.0397 | ±0.0794 | +1.862 | 0.0626 | . |
| Hypertension | -0.3818 | 0.7306 | ±1.4612 | -0.523 | 0.6013 |  |
| High cholesterol | +1.1356 | 0.6211 | ±1.2422 | +1.828 | 0.0675 | . |
| Kidney disease | +1.5779 | 0.9806 | ±1.9612 | +1.609 | 0.1076 |  |
| Circulatory disease | +0.2162 | 0.6893 | ±1.3785 | +0.314 | 0.7538 |  |
| **Avg. daily time > 250 (%)** | **+0.1189** | 0.0328 | ±0.0657 | **+3.618** | **2.97e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 229; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.95** (p = **0.0038**), AUC = **0.7113**, AIC = **250.8**, BIC = **288.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0527 | 1.3876 | ±2.7753 | -0.759 | 0.4481 | 0.3490 |  |
| Education: graduate level (vs college) | -0.3714 | 0.4181 | ±0.8361 | -0.888 | 0.3744 | 0.6898 |  |
| Education: high school or below (vs college) | +0.6189 | 0.4473 | ±0.8947 | +1.383 | 0.1665 | 1.8568 |  |
| Site: UCSD (vs UAB) | +0.7697 | 0.3940 | ±0.7880 | +1.953 | 0.0508 | 2.1590 | . |
| Site: UW (vs UAB) | -0.6204 | 0.4810 | ±0.9620 | -1.290 | 0.1971 | 0.5377 |  |
| Age (years) | -0.0288 | 0.0177 | ±0.0354 | -1.629 | 0.1033 | 0.9716 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.383 | 0.1666 | 1.0291 |  |
| Hypertension | +0.0053 | 0.4048 | ±0.8096 | +0.013 | 0.9895 | 1.0053 |  |
| High cholesterol | +0.4538 | 0.3579 | ±0.7159 | +1.268 | 0.2049 | 1.5743 |  |
| **Kidney disease** | **+1.0962** | 0.4280 | ±0.8560 | **+2.561** | **0.0104** | 2.9929 | * |
| Circulatory disease | +0.3929 | 0.3698 | ±0.7396 | +1.062 | 0.2881 | 1.4813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1304**, LLR χ² = **33.23** (p = **4.82e-04**), AUC = **0.7395**, AIC = **245.5**, BIC = **286.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2440** | 1.6445 | ±3.2890 | **-1.973** | **0.0485** | 0.0390 | * |
| Education: graduate level (vs college) | -0.2963 | 0.4286 | ±0.8572 | -0.691 | 0.4894 | 0.7436 |  |
| Education: high school or below (vs college) | +0.4953 | 0.4660 | ±0.9321 | +1.063 | 0.2879 | 1.6410 |  |
| **Site: UCSD (vs UAB)** | **+0.8043** | 0.4025 | ±0.8051 | **+1.998** | **0.0457** | 2.2350 | * |
| Site: UW (vs UAB) | -0.5178 | 0.4851 | ±0.9703 | -1.067 | 0.2858 | 0.5958 |  |
| Age (years) | -0.0329 | 0.0178 | ±0.0357 | -1.844 | 0.0652 | 0.9676 | . |
| BMI (kg/m2) | +0.0280 | 0.0211 | ±0.0421 | +1.329 | 0.1837 | 1.0284 |  |
| Hypertension | -0.1194 | 0.4126 | ±0.8252 | -0.289 | 0.7723 | 0.8874 |  |
| High cholesterol | +0.5180 | 0.3686 | ±0.7372 | +1.405 | 0.1599 | 1.6787 |  |
| **Kidney disease** | **+1.1214** | 0.4402 | ±0.8804 | **+2.547** | **0.0109** | 3.0693 | * |
| Circulatory disease | +0.3772 | 0.3774 | ±0.7549 | +0.999 | 0.3176 | 1.4582 |  |
| **HbA1c (%)** | **+0.3802** | 0.1426 | ±0.2851 | **+2.667** | **0.0076** | 1.4626 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1390**, LLR χ² = **35.41** (p = **2.12e-04**), AUC = **0.7382**, AIC = **243.4**, BIC = **284.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2165** | 1.5976 | ±3.1953 | **-2.013** | **0.0441** | 0.0401 | * |
| Education: graduate level (vs college) | -0.3721 | 0.4286 | ±0.8572 | -0.868 | 0.3853 | 0.6893 |  |
| Education: high school or below (vs college) | +0.5114 | 0.4674 | ±0.9347 | +1.094 | 0.2739 | 1.6676 |  |
| Site: UCSD (vs UAB) | +0.7849 | 0.4058 | ±0.8117 | +1.934 | 0.0531 | 2.1922 | . |
| Site: UW (vs UAB) | -0.5805 | 0.4907 | ±0.9814 | -1.183 | 0.2368 | 0.5596 |  |
| Age (years) | -0.0282 | 0.0180 | ±0.0359 | -1.569 | 0.1165 | 0.9722 |  |
| BMI (kg/m2) | +0.0306 | 0.0212 | ±0.0423 | +1.446 | 0.1481 | 1.0311 |  |
| Hypertension | -0.0819 | 0.4168 | ±0.8337 | -0.196 | 0.8442 | 0.9214 |  |
| High cholesterol | +0.5461 | 0.3745 | ±0.7490 | +1.458 | 0.1448 | 1.7264 |  |
| **Kidney disease** | **+1.0328** | 0.4374 | ±0.8747 | **+2.362** | **0.0182** | 2.8090 | * |
| Circulatory disease | +0.3150 | 0.3838 | ±0.7676 | +0.821 | 0.4118 | 1.3703 |  |
| **Mean glucose (mg/dL)** | **+0.0151** | 0.0050 | ±0.0101 | **+2.998** | **0.0027** | 1.0152 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1390**, LLR χ² = **35.41** (p = **2.12e-04**), AUC = **0.7382**, AIC = **243.4**, BIC = **284.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.3088** | 2.0129 | ±4.0258 | **-2.637** | **0.0084** | 0.0049 | ** |
| Education: graduate level (vs college) | -0.3721 | 0.4286 | ±0.8572 | -0.868 | 0.3853 | 0.6893 |  |
| Education: high school or below (vs college) | +0.5114 | 0.4674 | ±0.9347 | +1.094 | 0.2739 | 1.6676 |  |
| Site: UCSD (vs UAB) | +0.7849 | 0.4058 | ±0.8117 | +1.934 | 0.0531 | 2.1922 | . |
| Site: UW (vs UAB) | -0.5805 | 0.4907 | ±0.9814 | -1.183 | 0.2368 | 0.5596 |  |
| Age (years) | -0.0282 | 0.0180 | ±0.0359 | -1.569 | 0.1165 | 0.9722 |  |
| BMI (kg/m2) | +0.0306 | 0.0212 | ±0.0423 | +1.446 | 0.1481 | 1.0311 |  |
| Hypertension | -0.0819 | 0.4168 | ±0.8337 | -0.196 | 0.8442 | 0.9214 |  |
| High cholesterol | +0.5461 | 0.3745 | ±0.7490 | +1.458 | 0.1448 | 1.7264 |  |
| **Kidney disease** | **+1.0328** | 0.4374 | ±0.8747 | **+2.362** | **0.0182** | 2.8090 | * |
| Circulatory disease | +0.3150 | 0.3838 | ±0.7676 | +0.821 | 0.4118 | 1.3703 |  |
| **GMI (%)** | **+0.6321** | 0.2108 | ±0.4216 | **+2.998** | **0.0027** | 1.8816 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1629**, LLR χ² = **41.49** (p = **1.98e-05**), AUC = **0.7615**, AIC = **237.3**, BIC = **278.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8587** | 1.6330 | ±3.2661 | **-2.363** | **0.0181** | 0.0211 | * |
| Education: graduate level (vs college) | -0.4085 | 0.4337 | ±0.8674 | -0.942 | 0.3462 | 0.6646 |  |
| Education: high school or below (vs college) | +0.5132 | 0.4734 | ±0.9469 | +1.084 | 0.2784 | 1.6706 |  |
| **Site: UCSD (vs UAB)** | **+0.8302** | 0.4145 | ±0.8291 | **+2.003** | **0.0452** | 2.2937 | * |
| Site: UW (vs UAB) | -0.5962 | 0.4980 | ±0.9959 | -1.197 | 0.2312 | 0.5509 |  |
| Age (years) | -0.0259 | 0.0183 | ±0.0366 | -1.414 | 0.1574 | 0.9744 |  |
| BMI (kg/m2) | +0.0308 | 0.0215 | ±0.0429 | +1.436 | 0.1511 | 1.0313 |  |
| Hypertension | -0.1182 | 0.4232 | ±0.8465 | -0.279 | 0.7801 | 0.8886 |  |
| High cholesterol | +0.5167 | 0.3812 | ±0.7624 | +1.355 | 0.1753 | 1.6764 |  |
| **Kidney disease** | **+1.1547** | 0.4445 | ±0.8889 | **+2.598** | **0.0094** | 3.1732 | ** |
| Circulatory disease | +0.3020 | 0.3923 | ±0.7846 | +0.770 | 0.4414 | 1.3526 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0195** | 0.0053 | ±0.0106 | **+3.690** | **2.25e-04** | 1.0197 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1391**, LLR χ² = **35.43** (p = **2.11e-04**), AUC = **0.7462**, AIC = **243.3**, BIC = **284.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9769 | 1.4589 | ±2.9178 | -1.355 | 0.1754 | 0.1385 |  |
| Education: graduate level (vs college) | -0.2938 | 0.4300 | ±0.8600 | -0.683 | 0.4944 | 0.7454 |  |
| Education: high school or below (vs college) | +0.3775 | 0.4719 | ±0.9437 | +0.800 | 0.4237 | 1.4587 |  |
| **Site: UCSD (vs UAB)** | **+0.8080** | 0.4031 | ±0.8061 | **+2.004** | **0.0450** | 2.2433 | * |
| Site: UW (vs UAB) | -0.5440 | 0.4929 | ±0.9859 | -1.104 | 0.2697 | 0.5804 |  |
| Age (years) | -0.0345 | 0.0180 | ±0.0361 | -1.912 | 0.0558 | 0.9661 | . |
| BMI (kg/m2) | +0.0329 | 0.0213 | ±0.0425 | +1.550 | 0.1212 | 1.0335 |  |
| Hypertension | -0.1004 | 0.4146 | ±0.8291 | -0.242 | 0.8087 | 0.9045 |  |
| High cholesterol | +0.5697 | 0.3755 | ±0.7509 | +1.517 | 0.1292 | 1.7677 |  |
| Kidney disease | +0.8246 | 0.4465 | ±0.8931 | +1.847 | 0.0648 | 2.2809 | . |
| Circulatory disease | +0.4153 | 0.3788 | ±0.7575 | +1.096 | 0.2729 | 1.5148 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0327** | 0.0109 | ±0.0217 | **+3.005** | **0.0027** | 1.0332 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1263**, LLR χ² = **32.19** (p = **7.12e-04**), AUC = **0.7347**, AIC = **246.6**, BIC = **287.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.8262 | 1.4517 | ±2.9034 | -1.258 | 0.2084 | 0.1610 |  |
| Education: graduate level (vs college) | -0.3008 | 0.4263 | ±0.8526 | -0.706 | 0.4804 | 0.7402 |  |
| Education: high school or below (vs college) | +0.3857 | 0.4695 | ±0.9390 | +0.821 | 0.4114 | 1.4706 |  |
| **Site: UCSD (vs UAB)** | **+0.7975** | 0.4001 | ±0.8002 | **+1.993** | **0.0462** | 2.2200 | * |
| Site: UW (vs UAB) | -0.5679 | 0.4889 | ±0.9777 | -1.162 | 0.2453 | 0.5667 |  |
| Age (years) | -0.0337 | 0.0180 | ±0.0361 | -1.869 | 0.0616 | 0.9668 | . |
| BMI (kg/m2) | +0.0325 | 0.0211 | ±0.0422 | +1.542 | 0.1232 | 1.0330 |  |
| Hypertension | -0.0539 | 0.4109 | ±0.8218 | -0.131 | 0.8957 | 0.9475 |  |
| High cholesterol | +0.5397 | 0.3704 | ±0.7408 | +1.457 | 0.1451 | 1.7155 |  |
| Kidney disease | +0.8615 | 0.4442 | ±0.8885 | +1.939 | 0.0525 | 2.3668 | . |
| Circulatory disease | +0.4330 | 0.3751 | ±0.7501 | +1.155 | 0.2483 | 1.5419 |  |
| **Avg. daily SD (mg/dL)** | **+0.0310** | 0.0126 | ±0.0252 | **+2.465** | **0.0137** | 1.0315 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1162**, LLR χ² = **29.61** (p = **0.0018**), AUC = **0.7335**, AIC = **249.2**, BIC = **290.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9075 | 1.4788 | ±2.9576 | -1.290 | 0.1971 | 0.1485 |  |
| Education: graduate level (vs college) | -0.3012 | 0.4254 | ±0.8508 | -0.708 | 0.4790 | 0.7400 |  |
| Education: high school or below (vs college) | +0.4291 | 0.4628 | ±0.9255 | +0.927 | 0.3537 | 1.5359 |  |
| **Site: UCSD (vs UAB)** | **+0.7899** | 0.3959 | ±0.7918 | **+1.995** | **0.0460** | 2.2031 | * |
| Site: UW (vs UAB) | -0.5721 | 0.4875 | ±0.9750 | -1.174 | 0.2406 | 0.5644 |  |
| **Age (years)** | **-0.0358** | 0.0182 | ±0.0363 | **-1.971** | **0.0487** | 0.9648 | * |
| BMI (kg/m2) | +0.0317 | 0.0210 | ±0.0420 | +1.509 | 0.1312 | 1.0322 |  |
| Hypertension | -0.0452 | 0.4068 | ±0.8135 | -0.111 | 0.9115 | 0.9558 |  |
| High cholesterol | +0.5065 | 0.3653 | ±0.7306 | +1.387 | 0.1656 | 1.6594 |  |
| Kidney disease | +0.8584 | 0.4489 | ±0.8979 | +1.912 | 0.0559 | 2.3594 | . |
| Circulatory disease | +0.4294 | 0.3732 | ±0.7463 | +1.151 | 0.2498 | 1.5364 |  |
| CV (%) | +0.0486 | 0.0254 | ±0.0508 | +1.912 | 0.0558 | 1.0498 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1143**, LLR χ² = **29.12** (p = **0.0022**), AUC = **0.7286**, AIC = **249.6**, BIC = **290.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4393 | 1.6299 | ±3.2597 | +0.270 | 0.7875 | 1.5516 |  |
| Education: graduate level (vs college) | -0.3197 | 0.4252 | ±0.8505 | -0.752 | 0.4522 | 0.7264 |  |
| Education: high school or below (vs college) | +0.4325 | 0.4613 | ±0.9227 | +0.937 | 0.3485 | 1.5411 |  |
| Site: UCSD (vs UAB) | +0.7706 | 0.3957 | ±0.7915 | +1.947 | 0.0515 | 2.1612 | . |
| Site: UW (vs UAB) | -0.5951 | 0.4851 | ±0.9702 | -1.227 | 0.2199 | 0.5515 |  |
| **Age (years)** | **-0.0364** | 0.0183 | ±0.0366 | **-1.989** | **0.0467** | 0.9642 | * |
| BMI (kg/m2) | +0.0304 | 0.0209 | ±0.0418 | +1.453 | 0.1461 | 1.0308 |  |
| Hypertension | -0.0231 | 0.4058 | ±0.8116 | -0.057 | 0.9546 | 0.9772 |  |
| High cholesterol | +0.5063 | 0.3650 | ±0.7299 | +1.387 | 0.1654 | 1.6592 |  |
| **Kidney disease** | **+0.9393** | 0.4423 | ±0.8847 | **+2.123** | **0.0337** | 2.5582 | * |
| Circulatory disease | +0.3892 | 0.3724 | ±0.7449 | +1.045 | 0.2960 | 1.4759 |  |
| Mean / SD ratio | -0.2424 | 0.1405 | ±0.2810 | -1.725 | 0.0845 | 0.7848 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1039**, LLR χ² = **26.47** (p = **0.0055**), AUC = **0.7158**, AIC = **252.3**, BIC = **293.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4735 | 1.6044 | ±3.2088 | -0.295 | 0.7679 | 0.6228 |  |
| Education: graduate level (vs college) | -0.3438 | 0.4213 | ±0.8425 | -0.816 | 0.4145 | 0.7091 |  |
| Education: high school or below (vs college) | +0.5423 | 0.4598 | ±0.9197 | +1.179 | 0.2383 | 1.7199 |  |
| Site: UCSD (vs UAB) | +0.7620 | 0.3942 | ±0.7885 | +1.933 | 0.0533 | 2.1425 | . |
| Site: UW (vs UAB) | -0.6163 | 0.4815 | ±0.9630 | -1.280 | 0.2005 | 0.5399 |  |
| Age (years) | -0.0321 | 0.0183 | ±0.0366 | -1.754 | 0.0795 | 0.9684 | . |
| BMI (kg/m2) | +0.0294 | 0.0208 | ±0.0415 | +1.414 | 0.1575 | 1.0298 |  |
| Hypertension | +0.0109 | 0.4048 | ±0.8097 | +0.027 | 0.9786 | 1.0109 |  |
| High cholesterol | +0.4681 | 0.3601 | ±0.7201 | +1.300 | 0.1936 | 1.5969 |  |
| **Kidney disease** | **+1.0475** | 0.4340 | ±0.8679 | **+2.414** | **0.0158** | 2.8506 | * |
| Circulatory disease | +0.3964 | 0.3702 | ±0.7404 | +1.071 | 0.2842 | 1.4865 |  |
| Avg. daily mean/SD | -0.0773 | 0.1085 | ±0.2170 | -0.712 | 0.4763 | 0.9256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1077**, LLR χ² = **27.44** (p = **0.0039**), AUC = **0.7159**, AIC = **251.3**, BIC = **292.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.7253 | 1.5019 | ±3.0038 | -1.149 | 0.2507 | 0.1781 |  |
| Education: graduate level (vs college) | -0.3449 | 0.4217 | ±0.8433 | -0.818 | 0.4133 | 0.7083 |  |
| Education: high school or below (vs college) | +0.4852 | 0.4637 | ±0.9274 | +1.046 | 0.2954 | 1.6246 |  |
| Site: UCSD (vs UAB) | +0.7440 | 0.3959 | ±0.7918 | +1.879 | 0.0602 | 2.1044 | . |
| Site: UW (vs UAB) | -0.5773 | 0.4833 | ±0.9667 | -1.194 | 0.2323 | 0.5614 |  |
| Age (years) | -0.0301 | 0.0178 | ±0.0357 | -1.688 | 0.0915 | 0.9703 | . |
| BMI (kg/m2) | +0.0264 | 0.0209 | ±0.0418 | +1.263 | 0.2065 | 1.0267 |  |
| Hypertension | +0.0284 | 0.4075 | ±0.8151 | +0.070 | 0.9444 | 1.0288 |  |
| High cholesterol | +0.4611 | 0.3605 | ±0.7209 | +1.279 | 0.2008 | 1.5858 |  |
| **Kidney disease** | **+1.0989** | 0.4314 | ±0.8629 | **+2.547** | **0.0109** | 3.0007 | * |
| Circulatory disease | +0.3839 | 0.3727 | ±0.7455 | +1.030 | 0.3030 | 1.4681 |  |
| MAG (mg/dL/h) | +0.0181 | 0.0147 | ±0.0295 | +1.225 | 0.2207 | 1.0182 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1229**, LLR χ² = **31.32** (p = **9.80e-04**), AUC = **0.7365**, AIC = **247.4**, BIC = **288.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.0340 | 1.4812 | ±2.9624 | -1.373 | 0.1697 | 0.1308 |  |
| Education: graduate level (vs college) | -0.2901 | 0.4260 | ±0.8520 | -0.681 | 0.4959 | 0.7482 |  |
| Education: high school or below (vs college) | +0.3647 | 0.4717 | ±0.9434 | +0.773 | 0.4394 | 1.4401 |  |
| **Site: UCSD (vs UAB)** | **+0.7942** | 0.3992 | ±0.7984 | **+1.990** | **0.0466** | 2.2127 | * |
| Site: UW (vs UAB) | -0.5886 | 0.4881 | ±0.9762 | -1.206 | 0.2278 | 0.5551 |  |
| Age (years) | -0.0335 | 0.0181 | ±0.0362 | -1.851 | 0.0641 | 0.9670 | . |
| BMI (kg/m2) | +0.0326 | 0.0210 | ±0.0421 | +1.550 | 0.1210 | 1.0332 |  |
| Hypertension | -0.0160 | 0.4105 | ±0.8209 | -0.039 | 0.9689 | 0.9841 |  |
| High cholesterol | +0.5198 | 0.3687 | ±0.7373 | +1.410 | 0.1585 | 1.6817 |  |
| **Kidney disease** | **+0.8738** | 0.4454 | ±0.8908 | **+1.962** | **0.0498** | 2.3960 | * |
| Circulatory disease | +0.3927 | 0.3753 | ±0.7506 | +1.046 | 0.2954 | 1.4810 |  |
| **Avg. daily range (mg/dL)** | **+0.0082** | 0.0036 | ±0.0072 | **+2.299** | **0.0215** | 1.0083 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1586**, LLR χ² = **40.41** (p = **3.05e-05**), AUC = **0.7689**, AIC = **238.4**, BIC = **279.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6953 | 1.4428 | ±2.8857 | -1.175 | 0.2400 | 0.1835 |  |
| Education: graduate level (vs college) | -0.2694 | 0.4345 | ±0.8690 | -0.620 | 0.5352 | 0.7638 |  |
| Education: high school or below (vs college) | +0.5561 | 0.4721 | ±0.9441 | +1.178 | 0.2388 | 1.7438 |  |
| Site: UCSD (vs UAB) | +0.8017 | 0.4104 | ±0.8209 | +1.953 | 0.0508 | 2.2294 | . |
| Site: UW (vs UAB) | -0.5437 | 0.4974 | ±0.9947 | -1.093 | 0.2743 | 0.5806 |  |
| Age (years) | -0.0329 | 0.0180 | ±0.0359 | -1.829 | 0.0674 | 0.9677 | . |
| BMI (kg/m2) | +0.0324 | 0.0216 | ±0.0432 | +1.500 | 0.1336 | 1.0329 |  |
| Hypertension | -0.2233 | 0.4204 | ±0.8407 | -0.531 | 0.5952 | 0.7999 |  |
| High cholesterol | +0.5579 | 0.3787 | ±0.7575 | +1.473 | 0.1407 | 1.7471 |  |
| **Kidney disease** | **+0.9024** | 0.4505 | ±0.9010 | **+2.003** | **0.0452** | 2.4654 | * |
| Circulatory disease | +0.2966 | 0.3899 | ±0.7797 | +0.761 | 0.4468 | 1.3453 |  |
| **SD of daily means (mg/dL)** | **+0.0653** | 0.0183 | ±0.0365 | **+3.576** | **3.49e-04** | 1.0675 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1425**, LLR χ² = **36.31** (p = **1.50e-04**), AUC = **0.7467**, AIC = **242.5**, BIC = **283.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1832 | 1.5965 | ±3.1929 | +0.741 | 0.4586 | 3.2648 |  |
| Education: graduate level (vs college) | -0.2844 | 0.4319 | ±0.8637 | -0.659 | 0.5102 | 0.7525 |  |
| Education: high school or below (vs college) | +0.5080 | 0.4671 | ±0.9342 | +1.088 | 0.2768 | 1.6620 |  |
| **Site: UCSD (vs UAB)** | **+0.8182** | 0.4077 | ±0.8153 | **+2.007** | **0.0447** | 2.2665 | * |
| Site: UW (vs UAB) | -0.5359 | 0.4908 | ±0.9816 | -1.092 | 0.2749 | 0.5851 |  |
| Age (years) | -0.0303 | 0.0180 | ±0.0359 | -1.689 | 0.0911 | 0.9701 | . |
| BMI (kg/m2) | +0.0319 | 0.0214 | ±0.0427 | +1.494 | 0.1353 | 1.0324 |  |
| Hypertension | -0.0509 | 0.4161 | ±0.8323 | -0.122 | 0.9026 | 0.9504 |  |
| High cholesterol | +0.4982 | 0.3731 | ±0.7463 | +1.335 | 0.1818 | 1.6458 |  |
| **Kidney disease** | **+0.9482** | 0.4402 | ±0.8805 | **+2.154** | **0.0313** | 2.5811 | * |
| Circulatory disease | +0.3264 | 0.3824 | ±0.7648 | +0.854 | 0.3933 | 1.3860 |  |
| **Time in range 70-180, pooled (%)** | **-0.0273** | 0.0086 | ±0.0173 | **-3.162** | **0.0016** | 0.9730 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1419**, LLR χ² = **36.16** (p = **1.59e-04**), AUC = **0.7469**, AIC = **242.6**, BIC = **283.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1630 | 1.5938 | ±3.1876 | +0.730 | 0.4656 | 3.1994 |  |
| Education: graduate level (vs college) | -0.2858 | 0.4318 | ±0.8637 | -0.662 | 0.5080 | 0.7514 |  |
| Education: high school or below (vs college) | +0.4930 | 0.4674 | ±0.9348 | +1.055 | 0.2915 | 1.6372 |  |
| **Site: UCSD (vs UAB)** | **+0.8191** | 0.4076 | ±0.8152 | **+2.010** | **0.0445** | 2.2685 | * |
| Site: UW (vs UAB) | -0.5280 | 0.4904 | ±0.9808 | -1.077 | 0.2816 | 0.5898 |  |
| Age (years) | -0.0304 | 0.0180 | ±0.0359 | -1.692 | 0.0906 | 0.9700 | . |
| BMI (kg/m2) | +0.0322 | 0.0214 | ±0.0427 | +1.508 | 0.1316 | 1.0327 |  |
| Hypertension | -0.0397 | 0.4159 | ±0.8319 | -0.096 | 0.9239 | 0.9611 |  |
| High cholesterol | +0.4966 | 0.3728 | ±0.7456 | +1.332 | 0.1828 | 1.6432 |  |
| **Kidney disease** | **+0.9381** | 0.4411 | ±0.8822 | **+2.127** | **0.0334** | 2.5552 | * |
| Circulatory disease | +0.3252 | 0.3823 | ±0.7646 | +0.851 | 0.3950 | 1.3843 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0271** | 0.0086 | ±0.0172 | **-3.144** | **0.0017** | 0.9733 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1042**, LLR χ² = **26.54** (p = **0.0054**), AUC = **0.7121**, AIC = **252.2**, BIC = **293.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9872 | 1.3903 | ±2.7807 | -0.710 | 0.4777 | 0.3726 |  |
| Education: graduate level (vs college) | -0.3816 | 0.4175 | ±0.8349 | -0.914 | 0.3606 | 0.6827 |  |
| Education: high school or below (vs college) | +0.5946 | 0.4492 | ±0.8983 | +1.324 | 0.1856 | 1.8123 |  |
| Site: UCSD (vs UAB) | +0.7212 | 0.3984 | ±0.7968 | +1.810 | 0.0702 | 2.0570 | . |
| Site: UW (vs UAB) | -0.6735 | 0.4856 | ±0.9713 | -1.387 | 0.1655 | 0.5099 |  |
| Age (years) | -0.0286 | 0.0177 | ±0.0355 | -1.615 | 0.1063 | 0.9718 |  |
| BMI (kg/m2) | +0.0294 | 0.0208 | ±0.0416 | +1.412 | 0.1581 | 1.0298 |  |
| Hypertension | +0.0072 | 0.4046 | ±0.8092 | +0.018 | 0.9859 | 1.0072 |  |
| High cholesterol | +0.4605 | 0.3585 | ±0.7169 | +1.285 | 0.1989 | 1.5848 |  |
| **Kidney disease** | **+1.0870** | 0.4289 | ±0.8578 | **+2.534** | **0.0113** | 2.9652 | * |
| Circulatory disease | +0.4065 | 0.3716 | ±0.7431 | +1.094 | 0.2739 | 1.5016 |  |
| Time < 54 (%) | -0.2021 | 0.2875 | ±0.5751 | -0.703 | 0.4821 | 0.8170 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.95** (p = **0.0066**), AUC = **0.7115**, AIC = **252.8**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0539 | 1.3880 | ±2.7760 | -0.759 | 0.4477 | 0.3486 |  |
| Education: graduate level (vs college) | -0.3700 | 0.4192 | ±0.8384 | -0.883 | 0.3775 | 0.6908 |  |
| Education: high school or below (vs college) | +0.6203 | 0.4484 | ±0.8968 | +1.383 | 0.1666 | 1.8595 |  |
| Site: UCSD (vs UAB) | +0.7720 | 0.3971 | ±0.7943 | +1.944 | 0.0519 | 2.1640 | . |
| Site: UW (vs UAB) | -0.6183 | 0.4831 | ±0.9662 | -1.280 | 0.2006 | 0.5389 |  |
| Age (years) | -0.0289 | 0.0178 | ±0.0355 | -1.628 | 0.1035 | 0.9715 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.383 | 0.1665 | 1.0291 |  |
| Hypertension | +0.0052 | 0.4049 | ±0.8097 | +0.013 | 0.9897 | 1.0052 |  |
| High cholesterol | +0.4544 | 0.3582 | ±0.7163 | +1.269 | 0.2046 | 1.5752 |  |
| **Kidney disease** | **+1.0964** | 0.4280 | ±0.8560 | **+2.562** | **0.0104** | 2.9933 | * |
| Circulatory disease | +0.3917 | 0.3707 | ±0.7414 | +1.057 | 0.2907 | 1.4794 |  |
| Avg. daily time < 54 (%) | +0.0094 | 0.1999 | ±0.3997 | +0.047 | 0.9624 | 1.0095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.96** (p = **0.0066**), AUC = **0.7100**, AIC = **252.8**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0526 | 1.3881 | ±2.7761 | -0.758 | 0.4482 | 0.3490 |  |
| Education: graduate level (vs college) | -0.3647 | 0.4225 | ±0.8450 | -0.863 | 0.3880 | 0.6944 |  |
| Education: high school or below (vs college) | +0.6179 | 0.4473 | ±0.8946 | +1.381 | 0.1672 | 1.8550 |  |
| Site: UCSD (vs UAB) | +0.7733 | 0.3954 | ±0.7908 | +1.956 | 0.0505 | 2.1670 | . |
| Site: UW (vs UAB) | -0.6201 | 0.4811 | ±0.9623 | -1.289 | 0.1974 | 0.5379 |  |
| Age (years) | -0.0291 | 0.0179 | ±0.0357 | -1.629 | 0.1032 | 0.9713 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.384 | 0.1665 | 1.0291 |  |
| Hypertension | +0.0065 | 0.4049 | ±0.8099 | +0.016 | 0.9872 | 1.0065 |  |
| High cholesterol | +0.4507 | 0.3590 | ±0.7180 | +1.255 | 0.2093 | 1.5694 |  |
| **Kidney disease** | **+1.0952** | 0.4281 | ±0.8561 | **+2.558** | **0.0105** | 2.9896 | * |
| Circulatory disease | +0.3936 | 0.3697 | ±0.7394 | +1.065 | 0.2871 | 1.4822 |  |
| Time 54-69, pooled (%) | +0.0073 | 0.0661 | ±0.1322 | +0.111 | 0.9119 | 1.0073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1022**, LLR χ² = **26.04** (p = **0.0064**), AUC = **0.7112**, AIC = **252.7**, BIC = **293.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0449 | 1.3890 | ±2.7780 | -0.752 | 0.4519 | 0.3517 |  |
| Education: graduate level (vs college) | -0.3520 | 0.4232 | ±0.8465 | -0.832 | 0.4056 | 0.7033 |  |
| Education: high school or below (vs college) | +0.6144 | 0.4474 | ±0.8949 | +1.373 | 0.1697 | 1.8486 |  |
| **Site: UCSD (vs UAB)** | **+0.7793** | 0.3953 | ±0.7907 | **+1.971** | **0.0487** | 2.1799 | * |
| Site: UW (vs UAB) | -0.6193 | 0.4814 | ±0.9628 | -1.286 | 0.1983 | 0.5383 |  |
| Age (years) | -0.0296 | 0.0179 | ±0.0358 | -1.655 | 0.0979 | 0.9708 | . |
| BMI (kg/m2) | +0.0288 | 0.0208 | ±0.0415 | +1.385 | 0.1661 | 1.0292 |  |
| Hypertension | +0.0088 | 0.4051 | ±0.8101 | +0.022 | 0.9827 | 1.0088 |  |
| High cholesterol | +0.4467 | 0.3586 | ±0.7172 | +1.246 | 0.2129 | 1.5632 |  |
| **Kidney disease** | **+1.0939** | 0.4280 | ±0.8561 | **+2.556** | **0.0106** | 2.9859 | * |
| Circulatory disease | +0.3958 | 0.3696 | ±0.7391 | +1.071 | 0.2842 | 1.4855 |  |
| Avg. daily time 54-69 (%) | +0.0193 | 0.0628 | ±0.1256 | +0.308 | 0.7582 | 1.0195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.96** (p = **0.0066**), AUC = **0.7120**, AIC = **252.8**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0510 | 1.3875 | ±2.7750 | -0.757 | 0.4488 | 0.3496 |  |
| Education: graduate level (vs college) | -0.3759 | 0.4214 | ±0.8428 | -0.892 | 0.3724 | 0.6867 |  |
| Education: high school or below (vs college) | +0.6188 | 0.4474 | ±0.8948 | +1.383 | 0.1667 | 1.8567 |  |
| Site: UCSD (vs UAB) | +0.7660 | 0.3963 | ±0.7926 | +1.933 | 0.0532 | 2.1512 | . |
| Site: UW (vs UAB) | -0.6220 | 0.4813 | ±0.9626 | -1.292 | 0.1962 | 0.5369 |  |
| Age (years) | -0.0287 | 0.0178 | ±0.0356 | -1.610 | 0.1073 | 0.9717 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.384 | 0.1665 | 1.0291 |  |
| Hypertension | +0.0047 | 0.4049 | ±0.8098 | +0.012 | 0.9908 | 1.0047 |  |
| High cholesterol | +0.4560 | 0.3589 | ±0.7178 | +1.271 | 0.2039 | 1.5777 |  |
| **Kidney disease** | **+1.0967** | 0.4281 | ±0.8561 | **+2.562** | **0.0104** | 2.9942 | * |
| Circulatory disease | +0.3929 | 0.3700 | ±0.7399 | +1.062 | 0.2882 | 1.4813 |  |
| Time < 70 (%) | -0.0047 | 0.0558 | ±0.1117 | -0.085 | 0.9326 | 0.9953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1021**, LLR χ² = **26.02** (p = **0.0064**), AUC = **0.7111**, AIC = **252.7**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0493 | 1.3886 | ±2.7772 | -0.756 | 0.4499 | 0.3502 |  |
| Education: graduate level (vs college) | -0.3559 | 0.4226 | ±0.8453 | -0.842 | 0.3997 | 0.7005 |  |
| Education: high school or below (vs college) | +0.6180 | 0.4473 | ±0.8945 | +1.382 | 0.1671 | 1.8551 |  |
| **Site: UCSD (vs UAB)** | **+0.7797** | 0.3960 | ±0.7921 | **+1.969** | **0.0490** | 2.1809 | * |
| Site: UW (vs UAB) | -0.6165 | 0.4815 | ±0.9631 | -1.280 | 0.2005 | 0.5398 |  |
| Age (years) | -0.0295 | 0.0179 | ±0.0358 | -1.648 | 0.0993 | 0.9709 | . |
| BMI (kg/m2) | +0.0287 | 0.0208 | ±0.0415 | +1.385 | 0.1662 | 1.0292 |  |
| Hypertension | +0.0075 | 0.4050 | ±0.8100 | +0.019 | 0.9852 | 1.0075 |  |
| High cholesterol | +0.4497 | 0.3583 | ±0.7165 | +1.255 | 0.2094 | 1.5678 |  |
| **Kidney disease** | **+1.0948** | 0.4280 | ±0.8559 | **+2.558** | **0.0105** | 2.9886 | * |
| Circulatory disease | +0.3930 | 0.3695 | ±0.7390 | +1.064 | 0.2875 | 1.4815 |  |
| Avg. daily time < 70 (%) | +0.0134 | 0.0510 | ±0.1019 | +0.263 | 0.7929 | 1.0135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1586**, LLR χ² = **40.41** (p = **3.05e-05**), AUC = **0.7494**, AIC = **238.4**, BIC = **279.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.5345** | 2.7642 | ±5.5285 | **+2.002** | **0.0453** | 253.2712 | * |
| Education: graduate level (vs college) | -0.3021 | 0.4299 | ±0.8599 | -0.703 | 0.4822 | 0.7392 |  |
| Education: high school or below (vs college) | +0.4536 | 0.4833 | ±0.9666 | +0.938 | 0.3480 | 1.5739 |  |
| **Site: UCSD (vs UAB)** | **+0.8573** | 0.4105 | ±0.8209 | **+2.089** | **0.0367** | 2.3569 | * |
| Site: UW (vs UAB) | -0.4645 | 0.4947 | ±0.9895 | -0.939 | 0.3478 | 0.6284 |  |
| Age (years) | -0.0278 | 0.0182 | ±0.0363 | -1.530 | 0.1261 | 0.9726 |  |
| BMI (kg/m2) | +0.0329 | 0.0214 | ±0.0427 | +1.538 | 0.1240 | 1.0334 |  |
| Hypertension | -0.1086 | 0.4225 | ±0.8450 | -0.257 | 0.7971 | 0.8971 |  |
| High cholesterol | +0.5932 | 0.3826 | ±0.7653 | +1.550 | 0.1211 | 1.8097 |  |
| **Kidney disease** | **+1.0111** | 0.4405 | ±0.8809 | **+2.296** | **0.0217** | 2.7487 | * |
| Circulatory disease | +0.3218 | 0.3875 | ±0.7749 | +0.830 | 0.4063 | 1.3796 |  |
| **Time 54-250, pooled (%)** | **-0.0710** | 0.0243 | ±0.0486 | **-2.921** | **0.0035** | 0.9314 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1585**, LLR χ² = **40.37** (p = **3.09e-05**), AUC = **0.7481**, AIC = **238.4**, BIC = **279.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.3151** | 2.9231 | ±5.8463 | **+2.160** | **0.0307** | 552.8610 | * |
| Education: graduate level (vs college) | -0.2858 | 0.4293 | ±0.8585 | -0.666 | 0.5055 | 0.7514 |  |
| Education: high school or below (vs college) | +0.4123 | 0.4878 | ±0.9755 | +0.845 | 0.3980 | 1.5103 |  |
| **Site: UCSD (vs UAB)** | **+0.8486** | 0.4115 | ±0.8230 | **+2.062** | **0.0392** | 2.3364 | * |
| Site: UW (vs UAB) | -0.4782 | 0.4939 | ±0.9878 | -0.968 | 0.3329 | 0.6199 |  |
| Age (years) | -0.0287 | 0.0182 | ±0.0364 | -1.580 | 0.1141 | 0.9717 |  |
| BMI (kg/m2) | +0.0337 | 0.0214 | ±0.0427 | +1.578 | 0.1145 | 1.0343 |  |
| Hypertension | -0.1072 | 0.4221 | ±0.8441 | -0.254 | 0.7994 | 0.8983 |  |
| High cholesterol | +0.5878 | 0.3825 | ±0.7649 | +1.537 | 0.1243 | 1.8001 |  |
| **Kidney disease** | **+0.9844** | 0.4424 | ±0.8848 | **+2.225** | **0.0261** | 2.6763 | * |
| Circulatory disease | +0.3109 | 0.3883 | ±0.7766 | +0.801 | 0.4234 | 1.3646 |  |
| **Avg. daily time 54-250 (%)** | **-0.0784** | 0.0261 | ±0.0522 | **-3.005** | **0.0027** | 0.9246 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1157**, LLR χ² = **29.48** (p = **0.0019**), AUC = **0.7296**, AIC = **249.3**, BIC = **290.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2650 | 1.4050 | ±2.8101 | -0.900 | 0.3680 | 0.2823 |  |
| Education: graduate level (vs college) | -0.3425 | 0.4232 | ±0.8465 | -0.809 | 0.4183 | 0.7100 |  |
| Education: high school or below (vs college) | +0.5763 | 0.4528 | ±0.9057 | +1.273 | 0.2032 | 1.7794 |  |
| Site: UCSD (vs UAB) | +0.7609 | 0.3990 | ±0.7980 | +1.907 | 0.0565 | 2.1402 | . |
| Site: UW (vs UAB) | -0.6068 | 0.4831 | ±0.9663 | -1.256 | 0.2091 | 0.5451 |  |
| Age (years) | -0.0299 | 0.0177 | ±0.0354 | -1.686 | 0.0919 | 0.9706 | . |
| BMI (kg/m2) | +0.0296 | 0.0210 | ±0.0419 | +1.413 | 0.1577 | 1.0301 |  |
| Hypertension | -0.0117 | 0.4072 | ±0.8144 | -0.029 | 0.9770 | 0.9883 |  |
| High cholesterol | +0.4463 | 0.3632 | ±0.7264 | +1.229 | 0.2191 | 1.5625 |  |
| **Kidney disease** | **+0.9901** | 0.4350 | ±0.8700 | **+2.276** | **0.0228** | 2.6915 | * |
| Circulatory disease | +0.3592 | 0.3756 | ±0.7512 | +0.956 | 0.3390 | 1.4321 |  |
| Time 181-250, pooled (%) | +0.0240 | 0.0127 | ±0.0255 | +1.888 | 0.0590 | 1.0243 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1182**, LLR χ² = **30.12** (p = **0.0015**), AUC = **0.7323**, AIC = **248.6**, BIC = **289.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3223 | 1.4106 | ±2.8213 | -0.937 | 0.3486 | 0.2665 |  |
| Education: graduate level (vs college) | -0.3463 | 0.4243 | ±0.8486 | -0.816 | 0.4144 | 0.7073 |  |
| Education: high school or below (vs college) | +0.5696 | 0.4536 | ±0.9071 | +1.256 | 0.2092 | 1.7676 |  |
| Site: UCSD (vs UAB) | +0.7727 | 0.3998 | ±0.7996 | +1.933 | 0.0533 | 2.1656 | . |
| Site: UW (vs UAB) | -0.5886 | 0.4838 | ±0.9676 | -1.217 | 0.2237 | 0.5551 |  |
| Age (years) | -0.0295 | 0.0177 | ±0.0355 | -1.661 | 0.0968 | 0.9710 | . |
| BMI (kg/m2) | +0.0298 | 0.0210 | ±0.0420 | +1.418 | 0.1561 | 1.0302 |  |
| Hypertension | -0.0046 | 0.4080 | ±0.8160 | -0.011 | 0.9911 | 0.9954 |  |
| High cholesterol | +0.4487 | 0.3639 | ±0.7277 | +1.233 | 0.2175 | 1.5663 |  |
| **Kidney disease** | **+0.9818** | 0.4358 | ±0.8717 | **+2.253** | **0.0243** | 2.6693 | * |
| Circulatory disease | +0.3596 | 0.3762 | ±0.7524 | +0.956 | 0.3392 | 1.4327 |  |
| **Avg. daily time 181-250 (%)** | **+0.0253** | 0.0123 | ±0.0246 | **+2.052** | **0.0402** | 1.0256 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1413**, LLR χ² = **35.99** (p = **1.70e-04**), AUC = **0.7446**, AIC = **242.8**, BIC = **284.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5223 | 1.4370 | ±2.8739 | -1.059 | 0.2894 | 0.2182 |  |
| Education: graduate level (vs college) | -0.3126 | 0.4305 | ±0.8610 | -0.726 | 0.4677 | 0.7315 |  |
| Education: high school or below (vs college) | +0.5096 | 0.4673 | ±0.9346 | +1.091 | 0.2755 | 1.6646 |  |
| Site: UCSD (vs UAB) | +0.7951 | 0.4069 | ±0.8137 | +1.954 | 0.0507 | 2.2147 | . |
| Site: UW (vs UAB) | -0.5517 | 0.4900 | ±0.9801 | -1.126 | 0.2602 | 0.5760 |  |
| Age (years) | -0.0294 | 0.0180 | ±0.0359 | -1.637 | 0.1016 | 0.9710 |  |
| BMI (kg/m2) | +0.0319 | 0.0213 | ±0.0426 | +1.497 | 0.1344 | 1.0324 |  |
| Hypertension | -0.0514 | 0.4159 | ±0.8318 | -0.124 | 0.9016 | 0.9499 |  |
| High cholesterol | +0.5071 | 0.3729 | ±0.7458 | +1.360 | 0.1739 | 1.6605 |  |
| **Kidney disease** | **+0.9577** | 0.4399 | ±0.8798 | **+2.177** | **0.0295** | 2.6058 | * |
| Circulatory disease | +0.3255 | 0.3831 | ±0.7662 | +0.850 | 0.3955 | 1.3847 |  |
| **Time > 180 (%)** | **+0.0264** | 0.0085 | ±0.0169 | **+3.119** | **0.0018** | 1.0267 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1398**, LLR χ² = **35.62** (p = **1.96e-04**), AUC = **0.7432**, AIC = **243.1**, BIC = **284.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5269 | 1.4366 | ±2.8733 | -1.063 | 0.2879 | 0.2172 |  |
| Education: graduate level (vs college) | -0.3186 | 0.4302 | ±0.8603 | -0.741 | 0.4589 | 0.7272 |  |
| Education: high school or below (vs college) | +0.4962 | 0.4673 | ±0.9347 | +1.062 | 0.2884 | 1.6424 |  |
| Site: UCSD (vs UAB) | +0.7964 | 0.4065 | ±0.8131 | +1.959 | 0.0501 | 2.2175 | . |
| Site: UW (vs UAB) | -0.5445 | 0.4895 | ±0.9790 | -1.112 | 0.2660 | 0.5802 |  |
| Age (years) | -0.0292 | 0.0180 | ±0.0359 | -1.627 | 0.1036 | 0.9712 |  |
| BMI (kg/m2) | +0.0321 | 0.0213 | ±0.0426 | +1.508 | 0.1315 | 1.0326 |  |
| Hypertension | -0.0398 | 0.4154 | ±0.8307 | -0.096 | 0.9238 | 0.9610 |  |
| High cholesterol | +0.4989 | 0.3720 | ±0.7440 | +1.341 | 0.1799 | 1.6469 |  |
| **Kidney disease** | **+0.9498** | 0.4405 | ±0.8810 | **+2.156** | **0.0311** | 2.5851 | * |
| Circulatory disease | +0.3223 | 0.3828 | ±0.7657 | +0.842 | 0.3998 | 1.3804 |  |
| **Avg. daily time > 180 (%)** | **+0.0260** | 0.0085 | ±0.0170 | **+3.064** | **0.0022** | 1.0263 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1668**, LLR χ² = **42.50** (p = **1.33e-05**), AUC = **0.7698**, AIC = **236.3**, BIC = **277.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6000 | 1.4644 | ±2.9287 | -1.093 | 0.2746 | 0.2019 |  |
| Education: graduate level (vs college) | -0.2798 | 0.4366 | ±0.8731 | -0.641 | 0.5215 | 0.7559 |  |
| Education: high school or below (vs college) | +0.5590 | 0.4721 | ±0.9441 | +1.184 | 0.2364 | 1.7489 |  |
| **Site: UCSD (vs UAB)** | **+0.8723** | 0.4170 | ±0.8340 | **+2.092** | **0.0365** | 2.3924 | * |
| Site: UW (vs UAB) | -0.5423 | 0.5000 | ±1.0000 | -1.085 | 0.2781 | 0.5814 |  |
| Age (years) | -0.0282 | 0.0184 | ±0.0367 | -1.533 | 0.1254 | 0.9722 |  |
| BMI (kg/m2) | +0.0321 | 0.0217 | ±0.0434 | +1.479 | 0.1392 | 1.0326 |  |
| Hypertension | -0.0917 | 0.4240 | ±0.8480 | -0.216 | 0.8288 | 0.9124 |  |
| High cholesterol | +0.4802 | 0.3811 | ±0.7622 | +1.260 | 0.2076 | 1.6165 |  |
| **Kidney disease** | **+1.0770** | 0.4428 | ±0.8856 | **+2.432** | **0.0150** | 2.9359 | * |
| Circulatory disease | +0.2916 | 0.3930 | ±0.7859 | +0.742 | 0.4580 | 1.3386 |  |
| **Nocturnal time > 180 (%)** | **+0.0341** | 0.0089 | ±0.0178 | **+3.832** | **1.27e-04** | 1.0347 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1307**, LLR χ² = **33.30** (p = **4.71e-04**), AUC = **0.7382**, AIC = **245.5**, BIC = **286.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3336 | 1.4360 | ±2.8720 | -0.929 | 0.3530 | 0.2635 |  |
| Education: graduate level (vs college) | -0.2999 | 0.4287 | ±0.8575 | -0.699 | 0.4843 | 0.7409 |  |
| Education: high school or below (vs college) | +0.5187 | 0.4579 | ±0.9158 | +1.133 | 0.2574 | 1.6798 |  |
| Site: UCSD (vs UAB) | +0.7802 | 0.4016 | ±0.8032 | +1.943 | 0.0521 | 2.1818 | . |
| Site: UW (vs UAB) | -0.7327 | 0.4886 | ±0.9771 | -1.500 | 0.1337 | 0.4806 |  |
| **Age (years)** | **-0.0365** | 0.0186 | ±0.0372 | **-1.962** | **0.0498** | 0.9641 | * |
| BMI (kg/m2) | +0.0359 | 0.0214 | ±0.0428 | +1.677 | 0.0936 | 1.0365 | . |
| Hypertension | -0.0682 | 0.4128 | ±0.8255 | -0.165 | 0.8688 | 0.9341 |  |
| High cholesterol | +0.5486 | 0.3718 | ±0.7437 | +1.475 | 0.1401 | 1.7309 |  |
| **Kidney disease** | **+0.8944** | 0.4408 | ±0.8817 | **+2.029** | **0.0425** | 2.4458 | * |
| Circulatory disease | +0.3663 | 0.3800 | ±0.7600 | +0.964 | 0.3351 | 1.4424 |  |
| **Any reading > 250 during wear (0/1)** | **+0.9626** | 0.3637 | ±0.7274 | **+2.647** | **0.0081** | 2.6185 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1612**, LLR χ² = **41.06** (p = **2.35e-05**), AUC = **0.7513**, AIC = **237.7**, BIC = **278.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5520 | 1.4450 | ±2.8900 | -1.074 | 0.2828 | 0.2118 |  |
| Education: graduate level (vs college) | -0.3050 | 0.4300 | ±0.8601 | -0.709 | 0.4781 | 0.7371 |  |
| Education: high school or below (vs college) | +0.4375 | 0.4856 | ±0.9711 | +0.901 | 0.3675 | 1.5489 |  |
| **Site: UCSD (vs UAB)** | **+0.8399** | 0.4109 | ±0.8217 | **+2.044** | **0.0409** | 2.3162 | * |
| Site: UW (vs UAB) | -0.4833 | 0.4946 | ±0.9893 | -0.977 | 0.3285 | 0.6167 |  |
| Age (years) | -0.0277 | 0.0182 | ±0.0364 | -1.524 | 0.1274 | 0.9727 |  |
| BMI (kg/m2) | +0.0331 | 0.0214 | ±0.0427 | +1.547 | 0.1219 | 1.0336 |  |
| Hypertension | -0.1103 | 0.4230 | ±0.8461 | -0.261 | 0.7943 | 0.8955 |  |
| High cholesterol | +0.5999 | 0.3836 | ±0.7672 | +1.564 | 0.1178 | 1.8220 |  |
| **Kidney disease** | **+1.0009** | 0.4416 | ±0.8833 | **+2.266** | **0.0234** | 2.7208 | * |
| Circulatory disease | +0.3303 | 0.3890 | ±0.7781 | +0.849 | 0.3959 | 1.3913 |  |
| **Time > 250 (%)** | **+0.0742** | 0.0252 | ±0.0504 | **+2.946** | **0.0032** | 1.0770 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1602**, LLR χ² = **40.81** (p = **2.60e-05**), AUC = **0.7504**, AIC = **238.0**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5205 | 1.4446 | ±2.8892 | -1.053 | 0.2925 | 0.2186 |  |
| Education: graduate level (vs college) | -0.2951 | 0.4291 | ±0.8581 | -0.688 | 0.4916 | 0.7444 |  |
| Education: high school or below (vs college) | +0.3886 | 0.4906 | ±0.9811 | +0.792 | 0.4283 | 1.4749 |  |
| **Site: UCSD (vs UAB)** | **+0.8318** | 0.4118 | ±0.8236 | **+2.020** | **0.0434** | 2.2975 | * |
| Site: UW (vs UAB) | -0.4949 | 0.4938 | ±0.9876 | -1.002 | 0.3162 | 0.6096 |  |
| Age (years) | -0.0284 | 0.0182 | ±0.0364 | -1.560 | 0.1189 | 0.9720 |  |
| BMI (kg/m2) | +0.0338 | 0.0214 | ±0.0428 | +1.580 | 0.1141 | 1.0344 |  |
| Hypertension | -0.1073 | 0.4223 | ±0.8445 | -0.254 | 0.7994 | 0.8983 |  |
| High cholesterol | +0.5827 | 0.3825 | ±0.7650 | +1.523 | 0.1276 | 1.7909 |  |
| **Kidney disease** | **+0.9764** | 0.4435 | ±0.8871 | **+2.201** | **0.0277** | 2.6548 | * |
| Circulatory disease | +0.3210 | 0.3899 | ±0.7798 | +0.823 | 0.4103 | 1.3786 |  |
| **Avg. daily time > 250 (%)** | **+0.0826** | 0.0275 | ±0.0550 | **+3.004** | **0.0027** | 1.0861 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1252**, F-statistic = **3.50** (p = **5.88e-05**), Residual SE = **1.038** on **214** df, AIC = **677.7**, BIC = **725.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1714** | 0.7188 | ±1.4377 | **+4.412** | **1.03e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4525** | 0.1497 | ±0.2994 | **-3.022** | **0.0025** | ** |
| Education: high school or below (vs college) | +0.3675 | 0.2414 | ±0.4829 | +1.522 | 0.1279 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1630 | ±0.3260 | +1.165 | 0.2441 |  |
| Site: UW (vs UAB) | -0.3509 | 0.1966 | ±0.3932 | -1.785 | 0.0743 | . |
| **Season: spring (vs autumn)** | **-0.4284** | 0.1937 | ±0.3875 | **-2.211** | **0.0270** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2153 | ±0.4305 | +0.159 | 0.8737 |  |
| Season: winter (vs autumn) | -0.0137 | 0.2386 | ±0.4772 | -0.057 | 0.9543 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0136 | **-2.427** | **0.0152** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0239 | +0.368 | 0.7129 |  |
| Hypertension | +0.1587 | 0.1563 | ±0.3127 | +1.015 | 0.3102 |  |
| High cholesterol | +0.0412 | 0.1550 | ±0.3101 | +0.266 | 0.7905 |  |
| Kidney disease | -0.0180 | 0.2294 | ±0.4588 | -0.078 | 0.9375 |  |
| Circulatory disease | -0.1277 | 0.1744 | ±0.3487 | -0.732 | 0.4641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.1918**, Adj R² = **0.1387**, F-statistic = **3.61** (p = **2.24e-05**), Residual SE = **1.030** on **213** df, AIC = **675.1**, BIC = **726.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4538** | 0.7657 | ±1.5314 | **+3.205** | **0.0014** | ** |
| **Education: graduate level (vs college)** | **-0.4093** | 0.1486 | ±0.2971 | **-2.755** | **0.0059** | ** |
| Education: high school or below (vs college) | +0.3306 | 0.2347 | ±0.4694 | +1.409 | 0.1590 |  |
| Site: UCSD (vs UAB) | +0.1945 | 0.1643 | ±0.3286 | +1.184 | 0.2363 |  |
| Site: UW (vs UAB) | -0.3368 | 0.1957 | ±0.3913 | -1.721 | 0.0852 | . |
| **Season: spring (vs autumn)** | **-0.4552** | 0.1950 | ±0.3901 | **-2.334** | **0.0196** | * |
| Season: summer (vs autumn) | +0.0469 | 0.2156 | ±0.4311 | +0.218 | 0.8278 |  |
| Season: winter (vs autumn) | -0.0343 | 0.2365 | ±0.4730 | -0.145 | 0.8847 |  |
| **Age (years)** | **-0.0185** | 0.0069 | ±0.0138 | **-2.674** | **0.0075** | ** |
| BMI (kg/m2) | +0.0041 | 0.0117 | ±0.0234 | +0.346 | 0.7296 |  |
| Hypertension | +0.1390 | 0.1564 | ±0.3128 | +0.889 | 0.3741 |  |
| High cholesterol | +0.0604 | 0.1559 | ±0.3119 | +0.387 | 0.6987 |  |
| Kidney disease | -0.0311 | 0.2186 | ±0.4372 | -0.142 | 0.8870 |  |
| Circulatory disease | -0.1304 | 0.1738 | ±0.3476 | -0.751 | 0.4529 |  |
| HbA1c (%) | +0.1321 | 0.0733 | ±0.1466 | +1.803 | 0.0715 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1211**, F-statistic = **3.23** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1601** | 0.7509 | ±1.5018 | **+4.209** | **2.57e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4522** | 0.1507 | ±0.3013 | **-3.002** | **0.0027** | ** |
| Education: high school or below (vs college) | +0.3670 | 0.2434 | ±0.4868 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1635 | ±0.3270 | +1.161 | 0.2456 |  |
| Site: UW (vs UAB) | -0.3507 | 0.1966 | ±0.3933 | -1.783 | 0.0745 | . |
| **Season: spring (vs autumn)** | **-0.4294** | 0.1969 | ±0.3937 | **-2.181** | **0.0292** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2160 | ±0.4319 | +0.158 | 0.8743 |  |
| Season: winter (vs autumn) | -0.0145 | 0.2412 | ±0.4824 | -0.060 | 0.9522 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.415** | **0.0157** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0240 | +0.367 | 0.7134 |  |
| Hypertension | +0.1585 | 0.1584 | ±0.3167 | +1.001 | 0.3170 |  |
| High cholesterol | +0.0415 | 0.1563 | ±0.3125 | +0.265 | 0.7907 |  |
| Kidney disease | -0.0188 | 0.2264 | ±0.4529 | -0.083 | 0.9339 |  |
| Circulatory disease | -0.1279 | 0.1762 | ±0.3523 | -0.726 | 0.4677 |  |
| Mean glucose (mg/dL) | +0.0001 | 0.0021 | ±0.0043 | +0.040 | 0.9680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1211**, F-statistic = **3.23** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1483** | 0.8824 | ±1.7648 | **+3.568** | **3.60e-04** | *** |
| **Education: graduate level (vs college)** | **-0.4522** | 0.1507 | ±0.3013 | **-3.002** | **0.0027** | ** |
| Education: high school or below (vs college) | +0.3670 | 0.2434 | ±0.4868 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1635 | ±0.3270 | +1.161 | 0.2456 |  |
| Site: UW (vs UAB) | -0.3507 | 0.1966 | ±0.3933 | -1.783 | 0.0745 | . |
| **Season: spring (vs autumn)** | **-0.4294** | 0.1969 | ±0.3937 | **-2.181** | **0.0292** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2160 | ±0.4319 | +0.158 | 0.8743 |  |
| Season: winter (vs autumn) | -0.0145 | 0.2412 | ±0.4824 | -0.060 | 0.9522 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.415** | **0.0157** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0240 | +0.367 | 0.7134 |  |
| Hypertension | +0.1585 | 0.1584 | ±0.3167 | +1.001 | 0.3170 |  |
| High cholesterol | +0.0415 | 0.1563 | ±0.3125 | +0.265 | 0.7907 |  |
| Kidney disease | -0.0188 | 0.2264 | ±0.4529 | -0.083 | 0.9339 |  |
| Circulatory disease | -0.1279 | 0.1762 | ±0.3523 | -0.726 | 0.4677 |  |
| GMI (%) | +0.0036 | 0.0891 | ±0.1781 | +0.040 | 0.9680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.1755**, Adj R² = **0.1213**, F-statistic = **3.24** (p = **1.14e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1139** | 0.7343 | ±1.4685 | **+4.241** | **2.23e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4523** | 0.1503 | ±0.3006 | **-3.010** | **0.0026** | ** |
| Education: high school or below (vs college) | +0.3648 | 0.2424 | ±0.4848 | +1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | +0.1897 | 0.1637 | ±0.3274 | +1.159 | 0.2465 |  |
| Site: UW (vs UAB) | -0.3504 | 0.1973 | ±0.3946 | -1.776 | 0.0757 | . |
| **Season: spring (vs autumn)** | **-0.4337** | 0.1989 | ±0.3978 | **-2.181** | **0.0292** | * |
| Season: summer (vs autumn) | +0.0348 | 0.2161 | ±0.4323 | +0.161 | 0.8722 |  |
| Season: winter (vs autumn) | -0.0177 | 0.2426 | ±0.4853 | -0.073 | 0.9419 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0136 | **-2.425** | **0.0153** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0240 | +0.368 | 0.7127 |  |
| Hypertension | +0.1567 | 0.1594 | ±0.3188 | +0.983 | 0.3255 |  |
| High cholesterol | +0.0415 | 0.1560 | ±0.3121 | +0.266 | 0.7901 |  |
| Kidney disease | -0.0189 | 0.2286 | ±0.4572 | -0.082 | 0.9343 |  |
| Circulatory disease | -0.1292 | 0.1770 | ±0.3540 | -0.730 | 0.4655 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0004 | 0.0023 | ±0.0047 | +0.186 | 0.8521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1763**, Adj R² = **0.1221**, F-statistic = **3.26** (p = **1.05e-04**), Residual SE = **1.040** on **213** df, AIC = **679.5**, BIC = **730.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1136** | 0.7436 | ±1.4872 | **+4.187** | **2.82e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4428** | 0.1491 | ±0.2983 | **-2.969** | **0.0030** | ** |
| Education: high school or below (vs college) | +0.3514 | 0.2485 | ±0.4970 | +1.414 | 0.1574 |  |
| Site: UCSD (vs UAB) | +0.1921 | 0.1630 | ±0.3261 | +1.178 | 0.2387 |  |
| Site: UW (vs UAB) | -0.3454 | 0.1968 | ±0.3935 | -1.755 | 0.0792 | . |
| **Season: spring (vs autumn)** | **-0.4335** | 0.1949 | ±0.3897 | **-2.225** | **0.0261** | * |
| Season: summer (vs autumn) | +0.0374 | 0.2164 | ±0.4328 | +0.173 | 0.8630 |  |
| Season: winter (vs autumn) | -0.0189 | 0.2395 | ±0.4790 | -0.079 | 0.9370 |  |
| **Age (years)** | **-0.0170** | 0.0069 | ±0.0137 | **-2.481** | **0.0131** | * |
| BMI (kg/m2) | +0.0047 | 0.0122 | ±0.0243 | +0.386 | 0.6995 |  |
| Hypertension | +0.1568 | 0.1578 | ±0.3157 | +0.993 | 0.3205 |  |
| High cholesterol | +0.0458 | 0.1572 | ±0.3144 | +0.291 | 0.7707 |  |
| Kidney disease | -0.0413 | 0.2241 | ±0.4482 | -0.184 | 0.8539 |  |
| Circulatory disease | -0.1271 | 0.1750 | ±0.3500 | -0.726 | 0.4676 |  |
| Glucose SD, pooled (mg/dL) | +0.0023 | 0.0047 | ±0.0094 | +0.497 | 0.6189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1756**, Adj R² = **0.1214**, F-statistic = **3.24** (p = **1.12e-04**), Residual SE = **1.041** on **213** df, AIC = **679.6**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1357** | 0.7439 | ±1.4878 | **+4.215** | **2.50e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4468** | 0.1493 | ±0.2986 | **-2.993** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.3565 | 0.2515 | ±0.5031 | +1.417 | 0.1564 |  |
| Site: UCSD (vs UAB) | +0.1910 | 0.1630 | ±0.3259 | +1.172 | 0.2413 |  |
| Site: UW (vs UAB) | -0.3483 | 0.1969 | ±0.3937 | -1.769 | 0.0769 | . |
| **Season: spring (vs autumn)** | **-0.4330** | 0.1948 | ±0.3895 | **-2.223** | **0.0262** | * |
| Season: summer (vs autumn) | +0.0357 | 0.2164 | ±0.4328 | +0.165 | 0.8690 |  |
| Season: winter (vs autumn) | -0.0160 | 0.2395 | ±0.4790 | -0.067 | 0.9466 |  |
| **Age (years)** | **-0.0168** | 0.0069 | ±0.0137 | **-2.452** | **0.0142** | * |
| BMI (kg/m2) | +0.0046 | 0.0122 | ±0.0244 | +0.378 | 0.7057 |  |
| Hypertension | +0.1584 | 0.1571 | ±0.3142 | +1.008 | 0.3133 |  |
| High cholesterol | +0.0437 | 0.1567 | ±0.3133 | +0.279 | 0.7801 |  |
| Kidney disease | -0.0317 | 0.2231 | ±0.4462 | -0.142 | 0.8868 |  |
| Circulatory disease | -0.1268 | 0.1747 | ±0.3494 | -0.726 | 0.4680 |  |
| Avg. daily SD (mg/dL) | +0.0016 | 0.0053 | ±0.0106 | +0.299 | 0.7647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.1785**, Adj R² = **0.1245**, F-statistic = **3.31** (p = **8.49e-05**), Residual SE = **1.039** on **213** df, AIC = **678.8**, BIC = **730.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0075** | 0.7850 | ±1.5700 | **+3.831** | **1.27e-04** | *** |
| **Education: graduate level (vs college)** | **-0.4309** | 0.1472 | ±0.2945 | **-2.926** | **0.0034** | ** |
| Education: high school or below (vs college) | +0.3319 | 0.2537 | ±0.5075 | +1.308 | 0.1908 |  |
| Site: UCSD (vs UAB) | +0.1961 | 0.1631 | ±0.3261 | +1.202 | 0.2292 |  |
| Site: UW (vs UAB) | -0.3395 | 0.1979 | ±0.3957 | -1.716 | 0.0862 | . |
| **Season: spring (vs autumn)** | **-0.4281** | 0.1955 | ±0.3910 | **-2.190** | **0.0285** | * |
| Season: summer (vs autumn) | +0.0362 | 0.2165 | ±0.4330 | +0.167 | 0.8673 |  |
| Season: winter (vs autumn) | -0.0162 | 0.2393 | ±0.4787 | -0.068 | 0.9459 |  |
| **Age (years)** | **-0.0182** | 0.0069 | ±0.0139 | **-2.619** | **0.0088** | ** |
| BMI (kg/m2) | +0.0050 | 0.0122 | ±0.0244 | +0.412 | 0.6803 |  |
| Hypertension | +0.1589 | 0.1570 | ±0.3140 | +1.012 | 0.3114 |  |
| High cholesterol | +0.0478 | 0.1577 | ±0.3155 | +0.303 | 0.7617 |  |
| Kidney disease | -0.0700 | 0.2296 | ±0.4592 | -0.305 | 0.7604 |  |
| Circulatory disease | -0.1237 | 0.1750 | ±0.3500 | -0.707 | 0.4794 |  |
| CV (%) | +0.0099 | 0.0124 | ±0.0248 | +0.798 | 0.4246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.1782**, Adj R² = **0.1242**, F-statistic = **3.30** (p = **8.69e-05**), Residual SE = **1.039** on **213** df, AIC = **678.9**, BIC = **730.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4817** | 0.7621 | ±1.5242 | **+4.569** | **4.91e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4321** | 0.1469 | ±0.2937 | **-2.942** | **0.0033** | ** |
| Education: high school or below (vs college) | +0.3326 | 0.2499 | ±0.4999 | +1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | +0.1908 | 0.1640 | ±0.3280 | +1.163 | 0.2447 |  |
| Site: UW (vs UAB) | -0.3437 | 0.1975 | ±0.3950 | -1.740 | 0.0818 | . |
| **Season: spring (vs autumn)** | **-0.4334** | 0.1946 | ±0.3891 | **-2.227** | **0.0259** | * |
| Season: summer (vs autumn) | +0.0307 | 0.2161 | ±0.4322 | +0.142 | 0.8872 |  |
| Season: winter (vs autumn) | -0.0176 | 0.2387 | ±0.4775 | -0.074 | 0.9414 |  |
| **Age (years)** | **-0.0183** | 0.0071 | ±0.0141 | **-2.593** | **0.0095** | ** |
| BMI (kg/m2) | +0.0047 | 0.0120 | ±0.0240 | +0.395 | 0.6928 |  |
| Hypertension | +0.1627 | 0.1555 | ±0.3111 | +1.046 | 0.2954 |  |
| High cholesterol | +0.0486 | 0.1575 | ±0.3150 | +0.309 | 0.7574 |  |
| Kidney disease | -0.0541 | 0.2258 | ±0.4517 | -0.239 | 0.8108 |  |
| Circulatory disease | -0.1309 | 0.1754 | ±0.3508 | -0.746 | 0.4555 |  |
| Mean / SD ratio | -0.0484 | 0.0544 | ±0.1087 | -0.891 | 0.3728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1780**, Adj R² = **0.1240**, F-statistic = **3.29** (p = **8.88e-05**), Residual SE = **1.039** on **213** df, AIC = **679.0**, BIC = **730.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4589** | 0.7584 | ±1.5169 | **+4.560** | **5.10e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4308** | 0.1478 | ±0.2955 | **-2.916** | **0.0035** | ** |
| Education: high school or below (vs college) | +0.3330 | 0.2505 | ±0.5010 | +1.329 | 0.1837 |  |
| Site: UCSD (vs UAB) | +0.1872 | 0.1654 | ±0.3309 | +1.132 | 0.2578 |  |
| Site: UW (vs UAB) | -0.3468 | 0.1974 | ±0.3948 | -1.757 | 0.0790 | . |
| **Season: spring (vs autumn)** | **-0.4314** | 0.1943 | ±0.3886 | **-2.220** | **0.0264** | * |
| Season: summer (vs autumn) | +0.0338 | 0.2161 | ±0.4322 | +0.156 | 0.8757 |  |
| Season: winter (vs autumn) | -0.0115 | 0.2392 | ±0.4785 | -0.048 | 0.9618 |  |
| **Age (years)** | **-0.0183** | 0.0070 | ±0.0140 | **-2.610** | **0.0091** | ** |
| BMI (kg/m2) | +0.0048 | 0.0120 | ±0.0241 | +0.400 | 0.6893 |  |
| Hypertension | +0.1669 | 0.1548 | ±0.3097 | +1.078 | 0.2810 |  |
| High cholesterol | +0.0452 | 0.1563 | ±0.3126 | +0.289 | 0.7726 |  |
| Kidney disease | -0.0438 | 0.2258 | ±0.4515 | -0.194 | 0.8463 |  |
| Circulatory disease | -0.1277 | 0.1755 | ±0.3511 | -0.727 | 0.4670 |  |
| Avg. daily mean/SD | -0.0382 | 0.0436 | ±0.0872 | -0.876 | 0.3813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.1786**, Adj R² = **0.1246**, F-statistic = **3.31** (p = **8.38e-05**), Residual SE = **1.039** on **213** df, AIC = **678.8**, BIC = **730.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4075** | 0.7407 | ±1.4815 | **+4.600** | **4.22e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4653** | 0.1509 | ±0.3018 | **-3.084** | **0.0020** | ** |
| Education: high school or below (vs college) | +0.4019 | 0.2482 | ±0.4964 | +1.619 | 0.1053 |  |
| Site: UCSD (vs UAB) | +0.1979 | 0.1641 | ±0.3281 | +1.206 | 0.2277 |  |
| Site: UW (vs UAB) | -0.3652 | 0.1969 | ±0.3939 | -1.855 | 0.0636 | . |
| **Season: spring (vs autumn)** | **-0.4199** | 0.1941 | ±0.3882 | **-2.164** | **0.0305** | * |
| Season: summer (vs autumn) | +0.0279 | 0.2158 | ±0.4315 | +0.129 | 0.8971 |  |
| Season: winter (vs autumn) | -0.0173 | 0.2389 | ±0.4778 | -0.072 | 0.9423 |  |
| **Age (years)** | **-0.0162** | 0.0069 | ±0.0137 | **-2.357** | **0.0184** | * |
| BMI (kg/m2) | +0.0050 | 0.0119 | ±0.0239 | +0.418 | 0.6761 |  |
| Hypertension | +0.1539 | 0.1561 | ±0.3123 | +0.986 | 0.3243 |  |
| High cholesterol | +0.0403 | 0.1555 | ±0.3110 | +0.259 | 0.7953 |  |
| Kidney disease | -0.0166 | 0.2286 | ±0.4571 | -0.073 | 0.9421 |  |
| Circulatory disease | -0.1284 | 0.1737 | ±0.3474 | -0.739 | 0.4599 |  |
| MAG (mg/dL/h) | -0.0061 | 0.0056 | ±0.0112 | -1.086 | 0.2776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1211**, F-statistic = **3.23** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1683** | 0.7657 | ±1.5315 | **+4.138** | **3.51e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4521** | 0.1501 | ±0.3001 | **-3.013** | **0.0026** | ** |
| Education: high school or below (vs college) | +0.3668 | 0.2526 | ±0.5052 | +1.452 | 0.1465 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1628 | ±0.3257 | +1.166 | 0.2435 |  |
| Site: UW (vs UAB) | -0.3507 | 0.1970 | ±0.3941 | -1.780 | 0.0751 | . |
| **Season: spring (vs autumn)** | **-0.4287** | 0.1942 | ±0.3884 | **-2.208** | **0.0273** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2159 | ±0.4318 | +0.158 | 0.8742 |  |
| Season: winter (vs autumn) | -0.0138 | 0.2392 | ±0.4785 | -0.058 | 0.9540 |  |
| **Age (years)** | **-0.0166** | 0.0068 | ±0.0137 | **-2.423** | **0.0154** | * |
| BMI (kg/m2) | +0.0044 | 0.0123 | ±0.0245 | +0.360 | 0.7192 |  |
| Hypertension | +0.1587 | 0.1556 | ±0.3113 | +1.020 | 0.3078 |  |
| High cholesterol | +0.0413 | 0.1559 | ±0.3118 | +0.265 | 0.7911 |  |
| Kidney disease | -0.0188 | 0.2240 | ±0.4480 | -0.084 | 0.9330 |  |
| Circulatory disease | -0.1277 | 0.1752 | ±0.3504 | -0.729 | 0.4661 |  |
| Avg. daily range (mg/dL) | +0.0000 | 0.0015 | ±0.0029 | +0.019 | 0.9850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.1795**, Adj R² = **0.1256**, F-statistic = **3.33** (p = **7.66e-05**), Residual SE = **1.038** on **213** df, AIC = **678.6**, BIC = **730.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1029** | 0.7197 | ±1.4393 | **+4.312** | **1.62e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4330** | 0.1488 | ±0.2976 | **-2.910** | **0.0036** | ** |
| Education: high school or below (vs college) | +0.3610 | 0.2415 | ±0.4829 | +1.495 | 0.1349 |  |
| Site: UCSD (vs UAB) | +0.1925 | 0.1644 | ±0.3288 | +1.171 | 0.2418 |  |
| Site: UW (vs UAB) | -0.3397 | 0.1958 | ±0.3917 | -1.735 | 0.0828 | . |
| **Season: spring (vs autumn)** | **-0.4234** | 0.1939 | ±0.3877 | **-2.184** | **0.0289** | * |
| Season: summer (vs autumn) | +0.0366 | 0.2149 | ±0.4299 | +0.170 | 0.8647 |  |
| Season: winter (vs autumn) | -0.0341 | 0.2403 | ±0.4806 | -0.142 | 0.8870 |  |
| **Age (years)** | **-0.0171** | 0.0069 | ±0.0137 | **-2.490** | **0.0128** | * |
| BMI (kg/m2) | +0.0049 | 0.0120 | ±0.0239 | +0.407 | 0.6840 |  |
| Hypertension | +0.1424 | 0.1599 | ±0.3198 | +0.890 | 0.3733 |  |
| High cholesterol | +0.0463 | 0.1563 | ±0.3126 | +0.296 | 0.7671 |  |
| Kidney disease | -0.0527 | 0.2248 | ±0.4495 | -0.234 | 0.8148 |  |
| Circulatory disease | -0.1388 | 0.1779 | ±0.3558 | -0.780 | 0.4351 |  |
| SD of daily means (mg/dL) | +0.0078 | 0.0082 | ±0.0164 | +0.952 | 0.3412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.1802**, Adj R² = **0.1264**, F-statistic = **3.35** (p = **7.13e-05**), Residual SE = **1.038** on **213** df, AIC = **678.4**, BIC = **729.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5647** | 0.7946 | ±1.5892 | **+4.486** | **7.26e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4301** | 0.1482 | ±0.2963 | **-2.903** | **0.0037** | ** |
| Education: high school or below (vs college) | +0.3498 | 0.2418 | ±0.4835 | +1.447 | 0.1480 |  |
| Site: UCSD (vs UAB) | +0.1946 | 0.1637 | ±0.3275 | +1.188 | 0.2347 |  |
| Site: UW (vs UAB) | -0.3409 | 0.1962 | ±0.3925 | -1.737 | 0.0824 | . |
| **Season: spring (vs autumn)** | **-0.4461** | 0.1963 | ±0.3925 | **-2.273** | **0.0230** | * |
| Season: summer (vs autumn) | +0.0398 | 0.2149 | ±0.4298 | +0.185 | 0.8531 |  |
| Season: winter (vs autumn) | -0.0394 | 0.2391 | ±0.4781 | -0.165 | 0.8691 |  |
| **Age (years)** | **-0.0170** | 0.0068 | ±0.0136 | **-2.496** | **0.0125** | * |
| BMI (kg/m2) | +0.0049 | 0.0119 | ±0.0238 | +0.416 | 0.6776 |  |
| Hypertension | +0.1577 | 0.1566 | ±0.3132 | +1.007 | 0.3139 |  |
| High cholesterol | +0.0419 | 0.1558 | ±0.3116 | +0.269 | 0.7880 |  |
| Kidney disease | -0.0546 | 0.2230 | ±0.4461 | -0.245 | 0.8066 |  |
| Circulatory disease | -0.1386 | 0.1764 | ±0.3527 | -0.786 | 0.4320 |  |
| Time in range 70-180, pooled (%) | -0.0045 | 0.0037 | ±0.0074 | -1.210 | 0.2262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.1809**, Adj R² = **0.1271**, F-statistic = **3.36** (p = **6.68e-05**), Residual SE = **1.037** on **213** df, AIC = **678.2**, BIC = **729.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5909** | 0.7980 | ±1.5959 | **+4.500** | **6.79e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4287** | 0.1478 | ±0.2956 | **-2.900** | **0.0037** | ** |
| Education: high school or below (vs college) | +0.3466 | 0.2417 | ±0.4834 | +1.434 | 0.1516 |  |
| Site: UCSD (vs UAB) | +0.1958 | 0.1636 | ±0.3272 | +1.196 | 0.2315 |  |
| Site: UW (vs UAB) | -0.3394 | 0.1962 | ±0.3923 | -1.730 | 0.0836 | . |
| **Season: spring (vs autumn)** | **-0.4487** | 0.1964 | ±0.3929 | **-2.284** | **0.0224** | * |
| Season: summer (vs autumn) | +0.0381 | 0.2147 | ±0.4294 | +0.178 | 0.8590 |  |
| Season: winter (vs autumn) | -0.0439 | 0.2391 | ±0.4783 | -0.183 | 0.8545 |  |
| **Age (years)** | **-0.0170** | 0.0068 | ±0.0136 | **-2.503** | **0.0123** | * |
| BMI (kg/m2) | +0.0051 | 0.0119 | ±0.0238 | +0.425 | 0.6708 |  |
| Hypertension | +0.1588 | 0.1565 | ±0.3130 | +1.015 | 0.3101 |  |
| High cholesterol | +0.0417 | 0.1557 | ±0.3114 | +0.268 | 0.7888 |  |
| Kidney disease | -0.0587 | 0.2214 | ±0.4429 | -0.265 | 0.7911 |  |
| Circulatory disease | -0.1394 | 0.1765 | ±0.3529 | -0.790 | 0.4294 |  |
| Avg. daily time in range 70-180 (%) | -0.0048 | 0.0037 | ±0.0074 | -1.290 | 0.1969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.2000**, Adj R² = **0.1474**, F-statistic = **3.80** (p = **9.58e-06**), Residual SE = **1.025** on **213** df, AIC = **672.8**, BIC = **724.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0786** | 0.7186 | ±1.4371 | **+4.284** | **1.83e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4303** | 0.1477 | ±0.2954 | **-2.914** | **0.0036** | ** |
| Education: high school or below (vs college) | +0.4018 | 0.2467 | ±0.4933 | +1.629 | 0.1033 |  |
| Site: UCSD (vs UAB) | +0.2516 | 0.1631 | ±0.3263 | +1.542 | 0.1231 |  |
| Site: UW (vs UAB) | -0.2768 | 0.1995 | ±0.3990 | -1.387 | 0.1653 |  |
| **Season: spring (vs autumn)** | **-0.3957** | 0.1971 | ±0.3941 | **-2.008** | **0.0447** | * |
| Season: summer (vs autumn) | +0.0421 | 0.2097 | ±0.4194 | +0.201 | 0.8410 |  |
| Season: winter (vs autumn) | -0.0023 | 0.2368 | ±0.4735 | -0.010 | 0.9922 |  |
| **Age (years)** | **-0.0170** | 0.0068 | ±0.0135 | **-2.513** | **0.0120** | * |
| BMI (kg/m2) | +0.0039 | 0.0115 | ±0.0230 | +0.340 | 0.7340 |  |
| Hypertension | +0.1502 | 0.1600 | ±0.3200 | +0.939 | 0.3479 |  |
| High cholesterol | +0.0312 | 0.1537 | ±0.3074 | +0.203 | 0.8390 |  |
| Kidney disease | -0.0043 | 0.2258 | ±0.4516 | -0.019 | 0.9847 |  |
| Circulatory disease | -0.1636 | 0.1713 | ±0.3426 | -0.955 | 0.3396 |  |
| **Time < 54 (%)** | **+0.2428** | 0.1102 | ±0.2205 | **+2.202** | **0.0276** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.2038**, Adj R² = **0.1514**, F-statistic = **3.89** (p = **6.42e-06**), Residual SE = **1.023** on **213** df, AIC = **671.7**, BIC = **723.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1381** | 0.7051 | ±1.4101 | **+4.451** | **8.55e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4182** | 0.1448 | ±0.2895 | **-2.889** | **0.0039** | ** |
| Education: high school or below (vs college) | +0.4019 | 0.2451 | ±0.4902 | +1.639 | 0.1011 |  |
| Site: UCSD (vs UAB) | +0.2448 | 0.1611 | ±0.3222 | +1.520 | 0.1286 |  |
| Site: UW (vs UAB) | -0.2920 | 0.1958 | ±0.3917 | -1.491 | 0.1360 |  |
| Season: spring (vs autumn) | -0.3828 | 0.1964 | ±0.3928 | -1.949 | 0.0513 | . |
| Season: summer (vs autumn) | +0.0411 | 0.2133 | ±0.4265 | +0.193 | 0.8471 |  |
| Season: winter (vs autumn) | -0.0089 | 0.2401 | ±0.4802 | -0.037 | 0.9705 |  |
| **Age (years)** | **-0.0179** | 0.0068 | ±0.0136 | **-2.634** | **0.0084** | ** |
| BMI (kg/m2) | +0.0042 | 0.0116 | ±0.0232 | +0.366 | 0.7143 |  |
| Hypertension | +0.1572 | 0.1585 | ±0.3169 | +0.992 | 0.3213 |  |
| High cholesterol | +0.0465 | 0.1541 | ±0.3083 | +0.302 | 0.7629 |  |
| Kidney disease | -0.0208 | 0.2241 | ±0.4482 | -0.093 | 0.9259 |  |
| Circulatory disease | -0.1616 | 0.1746 | ±0.3492 | -0.925 | 0.3548 |  |
| Avg. daily time < 54 (%) | +0.2365 | 0.1576 | ±0.3153 | +1.500 | 0.1336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.2098**, Adj R² = **0.1579**, F-statistic = **4.04** (p = **3.36e-06**), Residual SE = **1.019** on **213** df, AIC = **670.0**, BIC = **721.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1365** | 0.7103 | ±1.4206 | **+4.416** | **1.01e-05** | *** |
| **Education: graduate level (vs college)** | **-0.3824** | 0.1449 | ±0.2899 | **-2.639** | **0.0083** | ** |
| Education: high school or below (vs college) | +0.3471 | 0.2498 | ±0.4996 | +1.390 | 0.1646 |  |
| Site: UCSD (vs UAB) | +0.2233 | 0.1632 | ±0.3263 | +1.369 | 0.1710 |  |
| Site: UW (vs UAB) | -0.3269 | 0.1925 | ±0.3849 | -1.699 | 0.0894 | . |
| Season: spring (vs autumn) | -0.3706 | 0.1957 | ±0.3914 | -1.894 | 0.0583 | . |
| Season: summer (vs autumn) | +0.0556 | 0.2069 | ±0.4139 | +0.269 | 0.7883 |  |
| Season: winter (vs autumn) | +0.0096 | 0.2344 | ±0.4689 | +0.041 | 0.9674 |  |
| **Age (years)** | **-0.0194** | 0.0067 | ±0.0133 | **-2.907** | **0.0037** | ** |
| BMI (kg/m2) | +0.0048 | 0.0117 | ±0.0233 | +0.408 | 0.6835 |  |
| Hypertension | +0.1789 | 0.1608 | ±0.3216 | +1.112 | 0.2659 |  |
| High cholesterol | +0.0112 | 0.1518 | ±0.3037 | +0.074 | 0.9411 |  |
| Kidney disease | -0.0353 | 0.2281 | ±0.4563 | -0.155 | 0.8769 |  |
| Circulatory disease | -0.1316 | 0.1704 | ±0.3408 | -0.772 | 0.4399 |  |
| **Time 54-69, pooled (%)** | **+0.0849** | 0.0380 | ±0.0761 | **+2.233** | **0.0255** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.2122**, Adj R² = **0.1604**, F-statistic = **4.10** (p = **2.60e-06**), Residual SE = **1.017** on **213** df, AIC = **669.3**, BIC = **720.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1809** | 0.7055 | ±1.4110 | **+4.509** | **6.52e-06** | *** |
| **Education: graduate level (vs college)** | **-0.3797** | 0.1439 | ±0.2877 | **-2.640** | **0.0083** | ** |
| Education: high school or below (vs college) | +0.3391 | 0.2501 | ±0.5001 | +1.356 | 0.1750 |  |
| Site: UCSD (vs UAB) | +0.2231 | 0.1630 | ±0.3261 | +1.369 | 0.1711 |  |
| Site: UW (vs UAB) | -0.3244 | 0.1917 | ±0.3834 | -1.692 | 0.0906 | . |
| Season: spring (vs autumn) | -0.3725 | 0.1954 | ±0.3908 | -1.906 | 0.0566 | . |
| Season: summer (vs autumn) | +0.0488 | 0.2073 | ±0.4146 | +0.235 | 0.8140 |  |
| Season: winter (vs autumn) | +0.0054 | 0.2342 | ±0.4684 | +0.023 | 0.9817 |  |
| **Age (years)** | **-0.0199** | 0.0067 | ±0.0133 | **-2.991** | **0.0028** | ** |
| BMI (kg/m2) | +0.0046 | 0.0116 | ±0.0233 | +0.394 | 0.6933 |  |
| Hypertension | +0.1809 | 0.1607 | ±0.3214 | +1.126 | 0.2602 |  |
| High cholesterol | +0.0148 | 0.1519 | ±0.3038 | +0.097 | 0.9226 |  |
| Kidney disease | -0.0325 | 0.2258 | ±0.4515 | -0.144 | 0.8856 |  |
| Circulatory disease | -0.1258 | 0.1703 | ±0.3407 | -0.738 | 0.4603 |  |
| **Avg. daily time 54-69 (%)** | **+0.0838** | 0.0369 | ±0.0739 | **+2.269** | **0.0233** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.2125**, Adj R² = **0.1607**, F-statistic = **4.10** (p = **2.53e-06**), Residual SE = **1.017** on **213** df, AIC = **669.2**, BIC = **720.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1134** | 0.7096 | ±1.4192 | **+4.387** | **1.15e-05** | *** |
| **Education: graduate level (vs college)** | **-0.3855** | 0.1445 | ±0.2891 | **-2.667** | **0.0077** | ** |
| Education: high school or below (vs college) | +0.3603 | 0.2503 | ±0.5005 | +1.440 | 0.1500 |  |
| Site: UCSD (vs UAB) | +0.2373 | 0.1629 | ±0.3258 | +1.456 | 0.1453 |  |
| Site: UW (vs UAB) | -0.3079 | 0.1937 | ±0.3874 | -1.590 | 0.1119 |  |
| Season: spring (vs autumn) | -0.3688 | 0.1963 | ±0.3925 | -1.879 | 0.0603 | . |
| Season: summer (vs autumn) | +0.0550 | 0.2060 | ±0.4120 | +0.267 | 0.7895 |  |
| Season: winter (vs autumn) | +0.0098 | 0.2342 | ±0.4683 | +0.042 | 0.9667 |  |
| **Age (years)** | **-0.0191** | 0.0066 | ±0.0133 | **-2.875** | **0.0040** | ** |
| BMI (kg/m2) | +0.0046 | 0.0116 | ±0.0231 | +0.394 | 0.6937 |  |
| Hypertension | +0.1735 | 0.1608 | ±0.3216 | +1.079 | 0.2805 |  |
| High cholesterol | +0.0124 | 0.1518 | ±0.3036 | +0.082 | 0.9350 |  |
| Kidney disease | -0.0288 | 0.2265 | ±0.4530 | -0.127 | 0.8988 |  |
| Circulatory disease | -0.1419 | 0.1694 | ±0.3387 | -0.838 | 0.4023 |  |
| **Time < 70 (%)** | **+0.0731** | 0.0297 | ±0.0595 | **+2.459** | **0.0139** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.2155**, Adj R² = **0.1640**, F-statistic = **4.18** (p = **1.81e-06**), Residual SE = **1.015** on **213** df, AIC = **668.3**, BIC = **719.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1694** | 0.7022 | ±1.4044 | **+4.514** | **6.37e-06** | *** |
| **Education: graduate level (vs college)** | **-0.3799** | 0.1427 | ±0.2855 | **-2.661** | **0.0078** | ** |
| Education: high school or below (vs college) | +0.3537 | 0.2503 | ±0.5006 | +1.413 | 0.1577 |  |
| Site: UCSD (vs UAB) | +0.2350 | 0.1621 | ±0.3243 | +1.449 | 0.1473 |  |
| Site: UW (vs UAB) | -0.3104 | 0.1920 | ±0.3840 | -1.617 | 0.1060 |  |
| Season: spring (vs autumn) | -0.3667 | 0.1957 | ±0.3913 | -1.874 | 0.0609 | . |
| Season: summer (vs autumn) | +0.0488 | 0.2068 | ±0.4136 | +0.236 | 0.8135 |  |
| Season: winter (vs autumn) | +0.0041 | 0.2343 | ±0.4686 | +0.017 | 0.9861 |  |
| **Age (years)** | **-0.0199** | 0.0067 | ±0.0133 | **-2.977** | **0.0029** | ** |
| BMI (kg/m2) | +0.0045 | 0.0116 | ±0.0231 | +0.391 | 0.6961 |  |
| Hypertension | +0.1773 | 0.1604 | ±0.3207 | +1.105 | 0.2690 |  |
| High cholesterol | +0.0202 | 0.1521 | ±0.3042 | +0.133 | 0.8944 |  |
| Kidney disease | -0.0313 | 0.2241 | ±0.4482 | -0.139 | 0.8891 |  |
| Circulatory disease | -0.1363 | 0.1695 | ±0.3390 | -0.804 | 0.4212 |  |
| **Avg. daily time < 70 (%)** | **+0.0717** | 0.0298 | ±0.0597 | **+2.403** | **0.0162** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1757**, Adj R² = **0.1216**, F-statistic = **3.24** (p = **1.11e-04**), Residual SE = **1.040** on **213** df, AIC = **679.6**, BIC = **731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4073** | 0.8003 | ±1.6006 | **+4.257** | **2.07e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4479** | 0.1497 | ±0.2994 | **-2.993** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.3614 | 0.2443 | ±0.4885 | +1.480 | 0.1390 |  |
| Site: UCSD (vs UAB) | +0.1911 | 0.1630 | ±0.3261 | +1.172 | 0.2410 |  |
| Site: UW (vs UAB) | -0.3456 | 0.1973 | ±0.3946 | -1.752 | 0.0799 | . |
| **Season: spring (vs autumn)** | **-0.4319** | 0.1949 | ±0.3898 | **-2.216** | **0.0267** | * |
| Season: summer (vs autumn) | +0.0403 | 0.2178 | ±0.4355 | +0.185 | 0.8533 |  |
| Season: winter (vs autumn) | -0.0160 | 0.2390 | ±0.4780 | -0.067 | 0.9468 |  |
| **Age (years)** | **-0.0165** | 0.0069 | ±0.0137 | **-2.404** | **0.0162** | * |
| BMI (kg/m2) | +0.0046 | 0.0121 | ±0.0241 | +0.378 | 0.7052 |  |
| Hypertension | +0.1561 | 0.1579 | ±0.3158 | +0.989 | 0.3228 |  |
| High cholesterol | +0.0449 | 0.1557 | ±0.3114 | +0.288 | 0.7730 |  |
| Kidney disease | -0.0225 | 0.2279 | ±0.4558 | -0.099 | 0.9215 |  |
| Circulatory disease | -0.1311 | 0.1772 | ±0.3545 | -0.740 | 0.4594 |  |
| Time 54-250, pooled (%) | -0.0026 | 0.0058 | ±0.0116 | -0.442 | 0.6583 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1765**, Adj R² = **0.1224**, F-statistic = **3.26** (p = **1.03e-04**), Residual SE = **1.040** on **213** df, AIC = **679.4**, BIC = **730.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6285** | 0.8764 | ±1.7529 | **+4.140** | **3.47e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4440** | 0.1495 | ±0.2990 | **-2.970** | **0.0030** | ** |
| Education: high school or below (vs college) | +0.3550 | 0.2452 | ±0.4903 | +1.448 | 0.1475 |  |
| Site: UCSD (vs UAB) | +0.1913 | 0.1632 | ±0.3265 | +1.172 | 0.2411 |  |
| Site: UW (vs UAB) | -0.3430 | 0.1971 | ±0.3943 | -1.740 | 0.0819 | . |
| **Season: spring (vs autumn)** | **-0.4370** | 0.1953 | ±0.3906 | **-2.237** | **0.0253** | * |
| Season: summer (vs autumn) | +0.0430 | 0.2172 | ±0.4344 | +0.198 | 0.8431 |  |
| Season: winter (vs autumn) | -0.0206 | 0.2388 | ±0.4777 | -0.086 | 0.9312 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.411** | **0.0159** | * |
| BMI (kg/m2) | +0.0048 | 0.0121 | ±0.0242 | +0.395 | 0.6929 |  |
| Hypertension | +0.1541 | 0.1581 | ±0.3162 | +0.975 | 0.3297 |  |
| High cholesterol | +0.0477 | 0.1557 | ±0.3115 | +0.306 | 0.7596 |  |
| Kidney disease | -0.0280 | 0.2264 | ±0.4528 | -0.123 | 0.9017 |  |
| Circulatory disease | -0.1353 | 0.1783 | ±0.3567 | -0.758 | 0.4482 |  |
| Avg. daily time 54-250 (%) | -0.0049 | 0.0069 | ±0.0138 | -0.709 | 0.4781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1778**, Adj R² = **0.1238**, F-statistic = **3.29** (p = **9.03e-05**), Residual SE = **1.039** on **213** df, AIC = **679.0**, BIC = **730.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1528** | 0.7089 | ±1.4178 | **+4.447** | **8.69e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4411** | 0.1498 | ±0.2995 | **-2.945** | **0.0032** | ** |
| Education: high school or below (vs college) | +0.3612 | 0.2409 | ±0.4818 | +1.499 | 0.1338 |  |
| Site: UCSD (vs UAB) | +0.1906 | 0.1644 | ±0.3288 | +1.159 | 0.2463 |  |
| Site: UW (vs UAB) | -0.3514 | 0.1983 | ±0.3966 | -1.772 | 0.0764 | . |
| **Season: spring (vs autumn)** | **-0.4441** | 0.1971 | ±0.3942 | **-2.253** | **0.0243** | * |
| Season: summer (vs autumn) | +0.0277 | 0.2167 | ±0.4333 | +0.128 | 0.8983 |  |
| Season: winter (vs autumn) | -0.0380 | 0.2426 | ±0.4852 | -0.157 | 0.8754 |  |
| **Age (years)** | **-0.0170** | 0.0070 | ±0.0139 | **-2.444** | **0.0145** | * |
| BMI (kg/m2) | +0.0046 | 0.0119 | ±0.0238 | +0.390 | 0.6963 |  |
| Hypertension | +0.1613 | 0.1556 | ±0.3112 | +1.036 | 0.3000 |  |
| High cholesterol | +0.0367 | 0.1553 | ±0.3106 | +0.236 | 0.8132 |  |
| Kidney disease | -0.0476 | 0.2242 | ±0.4483 | -0.212 | 0.8319 |  |
| Circulatory disease | -0.1326 | 0.1759 | ±0.3517 | -0.754 | 0.4509 |  |
| Time 181-250, pooled (%) | +0.0047 | 0.0065 | ±0.0130 | +0.732 | 0.4641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.1773**, Adj R² = **0.1232**, F-statistic = **3.28** (p = **9.55e-05**), Residual SE = **1.039** on **213** df, AIC = **679.2**, BIC = **730.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1481** | 0.7089 | ±1.4177 | **+4.441** | **8.95e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4429** | 0.1496 | ±0.2992 | **-2.961** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.3615 | 0.2412 | ±0.4823 | +1.499 | 0.1339 |  |
| Site: UCSD (vs UAB) | +0.1920 | 0.1638 | ±0.3276 | +1.172 | 0.2411 |  |
| Site: UW (vs UAB) | -0.3490 | 0.1974 | ±0.3949 | -1.768 | 0.0771 | . |
| **Season: spring (vs autumn)** | **-0.4412** | 0.1970 | ±0.3939 | **-2.240** | **0.0251** | * |
| Season: summer (vs autumn) | +0.0296 | 0.2166 | ±0.4332 | +0.137 | 0.8913 |  |
| Season: winter (vs autumn) | -0.0344 | 0.2425 | ±0.4850 | -0.142 | 0.8871 |  |
| **Age (years)** | **-0.0168** | 0.0069 | ±0.0138 | **-2.436** | **0.0149** | * |
| BMI (kg/m2) | +0.0046 | 0.0119 | ±0.0238 | +0.389 | 0.6975 |  |
| Hypertension | +0.1615 | 0.1557 | ±0.3114 | +1.037 | 0.2996 |  |
| High cholesterol | +0.0375 | 0.1554 | ±0.3107 | +0.242 | 0.8091 |  |
| Kidney disease | -0.0435 | 0.2238 | ±0.4476 | -0.194 | 0.8459 |  |
| Circulatory disease | -0.1314 | 0.1757 | ±0.3514 | -0.748 | 0.4544 |  |
| Avg. daily time 181-250 (%) | +0.0040 | 0.0061 | ±0.0122 | +0.660 | 0.5094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.1767**, Adj R² = **0.1226**, F-statistic = **3.27** (p = **1.01e-04**), Residual SE = **1.040** on **213** df, AIC = **679.3**, BIC = **730.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1451** | 0.7138 | ±1.4276 | **+4.406** | **1.05e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4430** | 0.1497 | ±0.2994 | **-2.959** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.3586 | 0.2424 | ±0.4847 | +1.479 | 0.1390 |  |
| Site: UCSD (vs UAB) | +0.1908 | 0.1638 | ±0.3276 | +1.165 | 0.2441 |  |
| Site: UW (vs UAB) | -0.3471 | 0.1966 | ±0.3933 | -1.765 | 0.0776 | . |
| **Season: spring (vs autumn)** | **-0.4395** | 0.1965 | ±0.3930 | **-2.237** | **0.0253** | * |
| Season: summer (vs autumn) | +0.0364 | 0.2157 | ±0.4314 | +0.169 | 0.8659 |  |
| Season: winter (vs autumn) | -0.0277 | 0.2407 | ±0.4815 | -0.115 | 0.9083 |  |
| **Age (years)** | **-0.0167** | 0.0068 | ±0.0137 | **-2.438** | **0.0148** | * |
| BMI (kg/m2) | +0.0047 | 0.0120 | ±0.0239 | +0.391 | 0.6960 |  |
| Hypertension | +0.1577 | 0.1570 | ±0.3139 | +1.005 | 0.3150 |  |
| High cholesterol | +0.0425 | 0.1561 | ±0.3121 | +0.272 | 0.7856 |  |
| Kidney disease | -0.0366 | 0.2244 | ±0.4487 | -0.163 | 0.8704 |  |
| Circulatory disease | -0.1329 | 0.1768 | ±0.3537 | -0.751 | 0.4525 |  |
| Time > 180 (%) | +0.0023 | 0.0037 | ±0.0073 | +0.631 | 0.5278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1768**, Adj R² = **0.1227**, F-statistic = **3.27** (p = **1.00e-04**), Residual SE = **1.040** on **213** df, AIC = **679.3**, BIC = **730.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1425** | 0.7130 | ±1.4259 | **+4.408** | **1.04e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4429** | 0.1496 | ±0.2992 | **-2.960** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.3574 | 0.2425 | ±0.4850 | +1.474 | 0.1405 |  |
| Site: UCSD (vs UAB) | +0.1913 | 0.1637 | ±0.3273 | +1.169 | 0.2424 |  |
| Site: UW (vs UAB) | -0.3464 | 0.1966 | ±0.3931 | -1.762 | 0.0780 | . |
| **Season: spring (vs autumn)** | **-0.4408** | 0.1969 | ±0.3938 | **-2.239** | **0.0252** | * |
| Season: summer (vs autumn) | +0.0357 | 0.2157 | ±0.4313 | +0.166 | 0.8684 |  |
| Season: winter (vs autumn) | -0.0296 | 0.2412 | ±0.4825 | -0.123 | 0.9023 |  |
| **Age (years)** | **-0.0167** | 0.0068 | ±0.0137 | **-2.437** | **0.0148** | * |
| BMI (kg/m2) | +0.0047 | 0.0120 | ±0.0239 | +0.395 | 0.6928 |  |
| Hypertension | +0.1581 | 0.1568 | ±0.3137 | +1.008 | 0.3133 |  |
| High cholesterol | +0.0422 | 0.1560 | ±0.3119 | +0.270 | 0.7869 |  |
| Kidney disease | -0.0382 | 0.2233 | ±0.4466 | -0.171 | 0.8642 |  |
| Circulatory disease | -0.1333 | 0.1770 | ±0.3540 | -0.753 | 0.4512 |  |
| Avg. daily time > 180 (%) | +0.0024 | 0.0037 | ±0.0074 | +0.655 | 0.5122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1806**, Adj R² = **0.1268**, F-statistic = **3.35** (p = **6.85e-05**), Residual SE = **1.037** on **213** df, AIC = **678.2**, BIC = **729.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1209** | 0.7049 | ±1.4098 | **+4.428** | **9.53e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4360** | 0.1491 | ±0.2982 | **-2.924** | **0.0035** | ** |
| Education: high school or below (vs college) | +0.3575 | 0.2400 | ±0.4800 | +1.490 | 0.1363 |  |
| Site: UCSD (vs UAB) | +0.1933 | 0.1638 | ±0.3276 | +1.180 | 0.2380 |  |
| Site: UW (vs UAB) | -0.3435 | 0.1969 | ±0.3938 | -1.745 | 0.0810 | . |
| **Season: spring (vs autumn)** | **-0.4463** | 0.1965 | ±0.3930 | **-2.271** | **0.0231** | * |
| Season: summer (vs autumn) | +0.0486 | 0.2148 | ±0.4297 | +0.226 | 0.8210 |  |
| Season: winter (vs autumn) | -0.0400 | 0.2396 | ±0.4792 | -0.167 | 0.8674 |  |
| **Age (years)** | **-0.0164** | 0.0068 | ±0.0135 | **-2.427** | **0.0152** | * |
| BMI (kg/m2) | +0.0048 | 0.0119 | ±0.0237 | +0.403 | 0.6871 |  |
| Hypertension | +0.1485 | 0.1576 | ±0.3152 | +0.942 | 0.3461 |  |
| High cholesterol | +0.0380 | 0.1555 | ±0.3110 | +0.244 | 0.8069 |  |
| Kidney disease | -0.0326 | 0.2236 | ±0.4471 | -0.146 | 0.8842 |  |
| Circulatory disease | -0.1429 | 0.1785 | ±0.3571 | -0.800 | 0.4235 |  |
| Nocturnal time > 180 (%) | +0.0046 | 0.0041 | ±0.0082 | +1.125 | 0.2607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1760**, Adj R² = **0.1218**, F-statistic = **3.25** (p = **1.08e-04**), Residual SE = **1.040** on **213** df, AIC = **679.5**, BIC = **731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1864** | 0.7297 | ±1.4595 | **+4.367** | **1.26e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4597** | 0.1508 | ±0.3016 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | +0.3737 | 0.2446 | ±0.4892 | +1.528 | 0.1265 |  |
| Site: UCSD (vs UAB) | +0.1892 | 0.1633 | ±0.3266 | +1.159 | 0.2466 |  |
| Site: UW (vs UAB) | -0.3459 | 0.1982 | ±0.3964 | -1.745 | 0.0809 | . |
| **Season: spring (vs autumn)** | **-0.4231** | 0.1936 | ±0.3872 | **-2.185** | **0.0289** | * |
| Season: summer (vs autumn) | +0.0384 | 0.2156 | ±0.4311 | +0.178 | 0.8586 |  |
| Season: winter (vs autumn) | -0.0126 | 0.2399 | ±0.4798 | -0.052 | 0.9583 |  |
| **Age (years)** | **-0.0161** | 0.0070 | ±0.0140 | **-2.296** | **0.0217** | * |
| BMI (kg/m2) | +0.0039 | 0.0123 | ±0.0247 | +0.320 | 0.7491 |  |
| Hypertension | +0.1596 | 0.1587 | ±0.3173 | +1.006 | 0.3144 |  |
| High cholesterol | +0.0386 | 0.1563 | ±0.3127 | +0.247 | 0.8052 |  |
| Kidney disease | -0.0022 | 0.2281 | ±0.4562 | -0.010 | 0.9922 |  |
| Circulatory disease | -0.1262 | 0.1752 | ±0.3505 | -0.720 | 0.4713 |  |
| Any reading > 250 during wear (0/1) | -0.0602 | 0.1569 | ±0.3138 | -0.384 | 0.7012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1754**, Adj R² = **0.1212**, F-statistic = **3.24** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1643** | 0.7289 | ±1.4579 | **+4.341** | **1.42e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4509** | 0.1501 | ±0.3001 | **-3.004** | **0.0027** | ** |
| Education: high school or below (vs college) | +0.3651 | 0.2440 | ±0.4881 | +1.496 | 0.1346 |  |
| Site: UCSD (vs UAB) | +0.1901 | 0.1631 | ±0.3263 | +1.165 | 0.2439 |  |
| Site: UW (vs UAB) | -0.3492 | 0.1972 | ±0.3945 | -1.770 | 0.0767 | . |
| **Season: spring (vs autumn)** | **-0.4298** | 0.1946 | ±0.3893 | **-2.208** | **0.0272** | * |
| Season: summer (vs autumn) | +0.0364 | 0.2173 | ±0.4346 | +0.168 | 0.8668 |  |
| Season: winter (vs autumn) | -0.0146 | 0.2391 | ±0.4783 | -0.061 | 0.9514 |  |
| **Age (years)** | **-0.0165** | 0.0069 | ±0.0137 | **-2.410** | **0.0160** | * |
| BMI (kg/m2) | +0.0045 | 0.0121 | ±0.0242 | +0.370 | 0.7117 |  |
| Hypertension | +0.1577 | 0.1578 | ±0.3156 | +0.999 | 0.3176 |  |
| High cholesterol | +0.0426 | 0.1554 | ±0.3109 | +0.274 | 0.7840 |  |
| Kidney disease | -0.0197 | 0.2280 | ±0.4561 | -0.086 | 0.9311 |  |
| Circulatory disease | -0.1288 | 0.1771 | ±0.3542 | -0.727 | 0.4670 |  |
| Time > 250 (%) | +0.0010 | 0.0053 | ±0.0106 | +0.179 | 0.8577 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1756**, Adj R² = **0.1215**, F-statistic = **3.24** (p = **1.12e-04**), Residual SE = **1.041** on **213** df, AIC = **679.6**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1555** | 0.7269 | ±1.4538 | **+4.341** | **1.42e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4484** | 0.1500 | ±0.3001 | **-2.989** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.3606 | 0.2449 | ±0.4897 | +1.473 | 0.1409 |  |
| Site: UCSD (vs UAB) | +0.1900 | 0.1633 | ±0.3266 | +1.164 | 0.2446 |  |
| Site: UW (vs UAB) | -0.3473 | 0.1971 | ±0.3942 | -1.762 | 0.0780 | . |
| **Season: spring (vs autumn)** | **-0.4334** | 0.1952 | ±0.3905 | **-2.220** | **0.0264** | * |
| Season: summer (vs autumn) | +0.0388 | 0.2169 | ±0.4338 | +0.179 | 0.8581 |  |
| Season: winter (vs autumn) | -0.0174 | 0.2393 | ±0.4786 | -0.073 | 0.9420 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.411** | **0.0159** | * |
| BMI (kg/m2) | +0.0046 | 0.0121 | ±0.0242 | +0.380 | 0.7038 |  |
| Hypertension | +0.1563 | 0.1580 | ±0.3161 | +0.989 | 0.3228 |  |
| High cholesterol | +0.0446 | 0.1554 | ±0.3109 | +0.287 | 0.7744 |  |
| Kidney disease | -0.0232 | 0.2268 | ±0.4536 | -0.102 | 0.9184 |  |
| Circulatory disease | -0.1313 | 0.1783 | ±0.3565 | -0.737 | 0.4614 |  |
| Avg. daily time > 250 (%) | +0.0026 | 0.0063 | ±0.0127 | +0.408 | 0.6833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.3144**, Adj R² = **0.2728**, F-statistic = **7.55** (p = **3.30e-12**), Residual SE = **2.120** on **214** df, AIC = **1003.2**, BIC = **1051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6380** | 1.1535 | ±2.3069 | **+20.493** | **2.49e-93** | *** |
| Education: graduate level (vs college) | +0.3810 | 0.3248 | ±0.6496 | +1.173 | 0.2408 |  |
| Education: high school or below (vs college) | -0.0532 | 0.4537 | ±0.9073 | -0.117 | 0.9066 |  |
| Site: UCSD (vs UAB) | -0.2180 | 0.3695 | ±0.7389 | -0.590 | 0.5552 |  |
| **Site: UW (vs UAB)** | **-1.5972** | 0.3454 | ±0.6908 | **-4.624** | **3.76e-06** | *** |
| Season: spring (vs autumn) | +0.1233 | 0.3765 | ±0.7531 | +0.327 | 0.7433 |  |
| **Season: summer (vs autumn)** | **+2.5673** | 0.4004 | ±0.8009 | **+6.411** | **1.44e-10** | *** |
| Season: winter (vs autumn) | -0.8393 | 0.4631 | ±0.9262 | -1.812 | 0.0699 | . |
| Age (years) | +0.0093 | 0.0141 | ±0.0281 | +0.660 | 0.5091 |  |
| BMI (kg/m2) | +0.0194 | 0.0201 | ±0.0402 | +0.966 | 0.3343 |  |
| Hypertension | +0.5178 | 0.3586 | ±0.7172 | +1.444 | 0.1488 |  |
| High cholesterol | -0.5689 | 0.3154 | ±0.6309 | -1.804 | 0.0713 | . |
| Kidney disease | -0.3449 | 0.3841 | ±0.7682 | -0.898 | 0.3692 |  |
| Circulatory disease | +0.0920 | 0.3648 | ±0.7297 | +0.252 | 0.8009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.3180**, Adj R² = **0.2732**, F-statistic = **7.09** (p = **5.71e-12**), Residual SE = **2.119** on **213** df, AIC = **1004.0**, BIC = **1055.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3903** | 1.3777 | ±2.7553 | **+17.704** | **3.90e-70** | *** |
| Education: graduate level (vs college) | +0.3358 | 0.3291 | ±0.6581 | +1.020 | 0.3075 |  |
| Education: high school or below (vs college) | -0.0145 | 0.4555 | ±0.9110 | -0.032 | 0.9746 |  |
| Site: UCSD (vs UAB) | -0.2229 | 0.3757 | ±0.7515 | -0.593 | 0.5530 |  |
| **Site: UW (vs UAB)** | **-1.6120** | 0.3455 | ±0.6909 | **-4.666** | **3.07e-06** | *** |
| Season: spring (vs autumn) | +0.1514 | 0.3742 | ±0.7484 | +0.405 | 0.6858 |  |
| **Season: summer (vs autumn)** | **+2.5540** | 0.3991 | ±0.7982 | **+6.400** | **1.56e-10** | *** |
| Season: winter (vs autumn) | -0.8176 | 0.4676 | ±0.9352 | -1.749 | 0.0803 | . |
| Age (years) | +0.0113 | 0.0142 | ±0.0284 | +0.798 | 0.4247 |  |
| BMI (kg/m2) | +0.0198 | 0.0204 | ±0.0408 | +0.971 | 0.3316 |  |
| Hypertension | +0.5384 | 0.3598 | ±0.7197 | +1.496 | 0.1346 |  |
| High cholesterol | -0.5890 | 0.3166 | ±0.6333 | -1.860 | 0.0629 | . |
| Kidney disease | -0.3312 | 0.3869 | ±0.7738 | -0.856 | 0.3920 |  |
| Circulatory disease | +0.0949 | 0.3672 | ±0.7344 | +0.258 | 0.7961 |  |
| HbA1c (%) | -0.1385 | 0.1310 | ±0.2620 | -1.058 | 0.2902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.3207**, Adj R² = **0.2760**, F-statistic = **7.18** (p = **3.95e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4802** | 1.3818 | ±2.7637 | **+17.716** | **3.18e-70** | *** |
| Education: graduate level (vs college) | +0.3600 | 0.3252 | ±0.6504 | +1.107 | 0.2682 |  |
| Education: high school or below (vs college) | -0.0104 | 0.4511 | ±0.9023 | -0.023 | 0.9816 |  |
| Site: UCSD (vs UAB) | -0.2180 | 0.3776 | ±0.7551 | -0.577 | 0.5636 |  |
| **Site: UW (vs UAB)** | **-1.6105** | 0.3443 | ±0.6886 | **-4.678** | **2.90e-06** | *** |
| Season: spring (vs autumn) | +0.1971 | 0.3770 | ±0.7539 | +0.523 | 0.6010 |  |
| **Season: summer (vs autumn)** | **+2.5709** | 0.3965 | ±0.7931 | **+6.483** | **8.98e-11** | *** |
| Season: winter (vs autumn) | -0.7811 | 0.4725 | ±0.9449 | -1.653 | 0.0983 | . |
| Age (years) | +0.0094 | 0.0141 | ±0.0281 | +0.668 | 0.5038 |  |
| BMI (kg/m2) | +0.0189 | 0.0207 | ±0.0413 | +0.912 | 0.3616 |  |
| Hypertension | +0.5330 | 0.3605 | ±0.7210 | +1.478 | 0.1393 |  |
| High cholesterol | -0.5898 | 0.3178 | ±0.6355 | -1.856 | 0.0634 | . |
| Kidney disease | -0.2854 | 0.3890 | ±0.7779 | -0.734 | 0.4632 |  |
| Circulatory disease | +0.1132 | 0.3682 | ±0.7364 | +0.307 | 0.7585 |  |
| Mean glucose (mg/dL) | -0.0064 | 0.0054 | ±0.0108 | -1.188 | 0.2350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.3207**, Adj R² = **0.2760**, F-statistic = **7.18** (p = **3.95e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.3687** | 1.8945 | ±3.7890 | **+13.391** | **6.85e-41** | *** |
| Education: graduate level (vs college) | +0.3600 | 0.3252 | ±0.6504 | +1.107 | 0.2682 |  |
| Education: high school or below (vs college) | -0.0104 | 0.4511 | ±0.9023 | -0.023 | 0.9816 |  |
| Site: UCSD (vs UAB) | -0.2180 | 0.3776 | ±0.7551 | -0.577 | 0.5636 |  |
| **Site: UW (vs UAB)** | **-1.6105** | 0.3443 | ±0.6886 | **-4.678** | **2.90e-06** | *** |
| Season: spring (vs autumn) | +0.1971 | 0.3770 | ±0.7539 | +0.523 | 0.6010 |  |
| **Season: summer (vs autumn)** | **+2.5709** | 0.3965 | ±0.7931 | **+6.483** | **8.98e-11** | *** |
| Season: winter (vs autumn) | -0.7811 | 0.4725 | ±0.9449 | -1.653 | 0.0983 | . |
| Age (years) | +0.0094 | 0.0141 | ±0.0281 | +0.668 | 0.5038 |  |
| BMI (kg/m2) | +0.0189 | 0.0207 | ±0.0413 | +0.912 | 0.3616 |  |
| Hypertension | +0.5330 | 0.3605 | ±0.7210 | +1.478 | 0.1393 |  |
| High cholesterol | -0.5898 | 0.3178 | ±0.6355 | -1.856 | 0.0634 | . |
| Kidney disease | -0.2854 | 0.3890 | ±0.7779 | -0.734 | 0.4632 |  |
| Circulatory disease | +0.1132 | 0.3682 | ±0.7364 | +0.307 | 0.7585 |  |
| GMI (%) | -0.2684 | 0.2260 | ±0.4520 | -1.188 | 0.2350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.3179**, Adj R² = **0.2731**, F-statistic = **7.09** (p = **5.78e-12**), Residual SE = **2.119** on **213** df, AIC = **1004.0**, BIC = **1055.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2622** | 1.3757 | ±2.7515 | **+17.636** | **1.31e-69** | *** |
| Education: graduate level (vs college) | +0.3795 | 0.3257 | ±0.6515 | +1.165 | 0.2440 |  |
| Education: high school or below (vs college) | -0.0238 | 0.4544 | ±0.9088 | -0.052 | 0.9583 |  |
| Site: UCSD (vs UAB) | -0.2163 | 0.3791 | ±0.7582 | -0.571 | 0.5682 |  |
| **Site: UW (vs UAB)** | **-1.6020** | 0.3445 | ±0.6890 | **-4.650** | **3.31e-06** | *** |
| Season: spring (vs autumn) | +0.1808 | 0.3769 | ±0.7539 | +0.480 | 0.6315 |  |
| **Season: summer (vs autumn)** | **+2.5615** | 0.3984 | ±0.7967 | **+6.430** | **1.28e-10** | *** |
| Season: winter (vs autumn) | -0.7957 | 0.4698 | ±0.9395 | -1.694 | 0.0903 | . |
| Age (years) | +0.0085 | 0.0140 | ±0.0280 | +0.609 | 0.5425 |  |
| BMI (kg/m2) | +0.0193 | 0.0207 | ±0.0414 | +0.930 | 0.3522 |  |
| Hypertension | +0.5389 | 0.3576 | ±0.7152 | +1.507 | 0.1318 |  |
| High cholesterol | -0.5728 | 0.3181 | ±0.6362 | -1.801 | 0.0718 | . |
| Kidney disease | -0.3356 | 0.3846 | ±0.7692 | -0.873 | 0.3829 |  |
| Circulatory disease | +0.1087 | 0.3704 | ±0.7407 | +0.293 | 0.7692 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0047 | 0.0060 | ±0.0119 | -0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.3183**, Adj R² = **0.2735**, F-statistic = **7.10** (p = **5.47e-12**), Residual SE = **2.119** on **213** df, AIC = **1003.9**, BIC = **1055.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9014** | 1.2189 | ±2.4378 | **+19.609** | **1.29e-85** | *** |
| Education: graduate level (vs college) | +0.3368 | 0.3257 | ±0.6514 | +1.034 | 0.3012 |  |
| Education: high school or below (vs college) | +0.0205 | 0.4646 | ±0.9292 | +0.044 | 0.9648 |  |
| Site: UCSD (vs UAB) | -0.2283 | 0.3767 | ±0.7534 | -0.606 | 0.5444 |  |
| **Site: UW (vs UAB)** | **-1.6221** | 0.3467 | ±0.6933 | **-4.679** | **2.88e-06** | *** |
| Season: spring (vs autumn) | +0.1465 | 0.3772 | ±0.7545 | +0.388 | 0.6977 |  |
| **Season: summer (vs autumn)** | **+2.5530** | 0.4000 | ±0.8000 | **+6.382** | **1.74e-10** | *** |
| Season: winter (vs autumn) | -0.8153 | 0.4697 | ±0.9395 | -1.736 | 0.0826 | . |
| Age (years) | +0.0116 | 0.0142 | ±0.0285 | +0.814 | 0.4158 |  |
| BMI (kg/m2) | +0.0181 | 0.0203 | ±0.0406 | +0.890 | 0.3733 |  |
| Hypertension | +0.5262 | 0.3631 | ±0.7262 | +1.449 | 0.1473 |  |
| High cholesterol | -0.5901 | 0.3192 | ±0.6384 | -1.849 | 0.0645 | . |
| Kidney disease | -0.2387 | 0.4089 | ±0.8177 | -0.584 | 0.5594 |  |
| Circulatory disease | +0.0895 | 0.3692 | ±0.7384 | +0.242 | 0.8085 |  |
| Glucose SD, pooled (mg/dL) | -0.0107 | 0.0110 | ±0.0219 | -0.976 | 0.3289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.3214**, Adj R² = **0.2768**, F-statistic = **7.20** (p = **3.59e-12**), Residual SE = **2.114** on **213** df, AIC = **1002.9**, BIC = **1054.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0162** | 1.2411 | ±2.4822 | **+19.350** | **2.02e-83** | *** |
| Education: graduate level (vs college) | +0.3205 | 0.3256 | ±0.6512 | +0.984 | 0.3249 |  |
| Education: high school or below (vs college) | +0.0640 | 0.4604 | ±0.9208 | +0.139 | 0.8894 |  |
| Site: UCSD (vs UAB) | -0.2297 | 0.3732 | ±0.7464 | -0.616 | 0.5382 |  |
| **Site: UW (vs UAB)** | **-1.6248** | 0.3442 | ±0.6884 | **-4.721** | **2.35e-06** | *** |
| Season: spring (vs autumn) | +0.1720 | 0.3802 | ±0.7605 | +0.452 | 0.6510 |  |
| **Season: summer (vs autumn)** | **+2.5515** | 0.3994 | ±0.7988 | **+6.388** | **1.68e-10** | *** |
| Season: winter (vs autumn) | -0.8142 | 0.4677 | ±0.9353 | -1.741 | 0.0817 | . |
| Age (years) | +0.0124 | 0.0141 | ±0.0282 | +0.879 | 0.3793 |  |
| BMI (kg/m2) | +0.0172 | 0.0204 | ±0.0409 | +0.843 | 0.3991 |  |
| Hypertension | +0.5206 | 0.3624 | ±0.7248 | +1.437 | 0.1508 |  |
| High cholesterol | -0.5960 | 0.3197 | ±0.6394 | -1.864 | 0.0623 | . |
| Kidney disease | -0.1989 | 0.4097 | ±0.8194 | -0.485 | 0.6273 |  |
| Circulatory disease | +0.0825 | 0.3661 | ±0.7321 | +0.225 | 0.8216 |  |
| Avg. daily SD (mg/dL) | -0.0169 | 0.0117 | ±0.0235 | -1.440 | 0.1498 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.3147**, Adj R² = **0.2697**, F-statistic = **6.99** (p = **8.97e-12**), Residual SE = **2.124** on **213** df, AIC = **1005.1**, BIC = **1056.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7546** | 1.2682 | ±2.5364 | **+18.731** | **2.75e-78** | *** |
| Education: graduate level (vs college) | +0.3656 | 0.3268 | ±0.6536 | +1.119 | 0.2632 |  |
| Education: high school or below (vs college) | -0.0278 | 0.4699 | ±0.9399 | -0.059 | 0.9528 |  |
| Site: UCSD (vs UAB) | -0.2224 | 0.3733 | ±0.7467 | -0.596 | 0.5513 |  |
| **Site: UW (vs UAB)** | **-1.6053** | 0.3473 | ±0.6946 | **-4.622** | **3.80e-06** | *** |
| Season: spring (vs autumn) | +0.1231 | 0.3786 | ±0.7572 | +0.325 | 0.7451 |  |
| **Season: summer (vs autumn)** | **+2.5659** | 0.4026 | ±0.8052 | **+6.373** | **1.85e-10** | *** |
| Season: winter (vs autumn) | -0.8374 | 0.4672 | ±0.9345 | -1.792 | 0.0731 | . |
| Age (years) | +0.0105 | 0.0145 | ±0.0291 | +0.721 | 0.4711 |  |
| BMI (kg/m2) | +0.0190 | 0.0204 | ±0.0408 | +0.930 | 0.3526 |  |
| Hypertension | +0.5176 | 0.3613 | ±0.7226 | +1.433 | 0.1520 |  |
| High cholesterol | -0.5736 | 0.3196 | ±0.6392 | -1.795 | 0.0727 | . |
| Kidney disease | -0.3079 | 0.4235 | ±0.8470 | -0.727 | 0.4672 |  |
| Circulatory disease | +0.0892 | 0.3679 | ±0.7358 | +0.242 | 0.8084 |  |
| CV (%) | -0.0071 | 0.0252 | ±0.0505 | -0.280 | 0.7798 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.3150**, Adj R² = **0.2700**, F-statistic = **7.00** (p = **8.65e-12**), Residual SE = **2.124** on **213** df, AIC = **1005.0**, BIC = **1056.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3265** | 1.3609 | ±2.7219 | **+17.140** | **7.46e-66** | *** |
| Education: graduate level (vs college) | +0.3606 | 0.3276 | ±0.6552 | +1.101 | 0.2710 |  |
| Education: high school or below (vs college) | -0.0181 | 0.4667 | ±0.9333 | -0.039 | 0.9690 |  |
| Site: UCSD (vs UAB) | -0.2190 | 0.3719 | ±0.7439 | -0.589 | 0.5561 |  |
| **Site: UW (vs UAB)** | **-1.6044** | 0.3460 | ±0.6920 | **-4.637** | **3.53e-06** | *** |
| Season: spring (vs autumn) | +0.1283 | 0.3799 | ±0.7597 | +0.338 | 0.7356 |  |
| **Season: summer (vs autumn)** | **+2.5709** | 0.4017 | ±0.8035 | **+6.400** | **1.56e-10** | *** |
| Season: winter (vs autumn) | -0.8354 | 0.4682 | ±0.9364 | -1.784 | 0.0744 | . |
| Age (years) | +0.0110 | 0.0145 | ±0.0290 | +0.761 | 0.4469 |  |
| BMI (kg/m2) | +0.0191 | 0.0203 | ±0.0405 | +0.941 | 0.3465 |  |
| Hypertension | +0.5137 | 0.3588 | ±0.7177 | +1.432 | 0.1523 |  |
| High cholesterol | -0.5764 | 0.3216 | ±0.6432 | -1.792 | 0.0731 | . |
| Kidney disease | -0.3088 | 0.4147 | ±0.8295 | -0.744 | 0.4566 |  |
| Circulatory disease | +0.0952 | 0.3657 | ±0.7314 | +0.260 | 0.7946 |  |
| Mean / SD ratio | +0.0486 | 0.1362 | ±0.2724 | +0.357 | 0.7212 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.3168**, Adj R² = **0.2719**, F-statistic = **7.06** (p = **6.72e-12**), Residual SE = **2.121** on **213** df, AIC = **1004.4**, BIC = **1055.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.0260** | 1.3204 | ±2.6409 | **+17.438** | **4.24e-68** | *** |
| Education: graduate level (vs college) | +0.3349 | 0.3282 | ±0.6564 | +1.021 | 0.3075 |  |
| Education: high school or below (vs college) | +0.0203 | 0.4611 | ±0.9222 | +0.044 | 0.9649 |  |
| Site: UCSD (vs UAB) | -0.2124 | 0.3710 | ±0.7421 | -0.572 | 0.5671 |  |
| **Site: UW (vs UAB)** | **-1.6059** | 0.3452 | ±0.6903 | **-4.653** | **3.27e-06** | *** |
| Season: spring (vs autumn) | +0.1297 | 0.3801 | ±0.7603 | +0.341 | 0.7330 |  |
| **Season: summer (vs autumn)** | **+2.5682** | 0.4020 | ±0.8039 | **+6.389** | **1.67e-10** | *** |
| Season: winter (vs autumn) | -0.8440 | 0.4632 | ±0.9264 | -1.822 | 0.0685 | . |
| Age (years) | +0.0129 | 0.0144 | ±0.0288 | +0.899 | 0.3687 |  |
| BMI (kg/m2) | +0.0185 | 0.0203 | ±0.0405 | +0.915 | 0.3601 |  |
| Hypertension | +0.5002 | 0.3560 | ±0.7120 | +1.405 | 0.1600 |  |
| High cholesterol | -0.5774 | 0.3203 | ±0.6407 | -1.803 | 0.0715 | . |
| Kidney disease | -0.2901 | 0.4113 | ±0.8225 | -0.705 | 0.4806 |  |
| Circulatory disease | +0.0921 | 0.3657 | ±0.7314 | +0.252 | 0.8012 |  |
| Avg. daily mean/SD | +0.0812 | 0.1111 | ±0.2221 | +0.731 | 0.4645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.3177**, Adj R² = **0.2728**, F-statistic = **7.08** (p = **5.97e-12**), Residual SE = **2.120** on **213** df, AIC = **1004.1**, BIC = **1055.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1661** | 1.3220 | ±2.6441 | **+18.280** | **1.20e-74** | *** |
| Education: graduate level (vs college) | +0.3523 | 0.3316 | ±0.6632 | +1.062 | 0.2880 |  |
| Education: high school or below (vs college) | +0.0237 | 0.4501 | ±0.9001 | +0.053 | 0.9580 |  |
| Site: UCSD (vs UAB) | -0.2000 | 0.3723 | ±0.7445 | -0.537 | 0.5911 |  |
| **Site: UW (vs UAB)** | **-1.6294** | 0.3433 | ±0.6867 | **-4.746** | **2.08e-06** | *** |
| Season: spring (vs autumn) | +0.1423 | 0.3808 | ±0.7615 | +0.374 | 0.7086 |  |
| **Season: summer (vs autumn)** | **+2.5532** | 0.4026 | ±0.8051 | **+6.342** | **2.26e-10** | *** |
| Season: winter (vs autumn) | -0.8473 | 0.4648 | ±0.9296 | -1.823 | 0.0683 | . |
| Age (years) | +0.0100 | 0.0141 | ±0.0282 | +0.712 | 0.4764 |  |
| BMI (kg/m2) | +0.0207 | 0.0200 | ±0.0400 | +1.036 | 0.3000 |  |
| Hypertension | +0.5071 | 0.3588 | ±0.7176 | +1.413 | 0.1575 |  |
| High cholesterol | -0.5708 | 0.3161 | ±0.6321 | -1.806 | 0.0709 | . |
| Kidney disease | -0.3418 | 0.3888 | ±0.7777 | -0.879 | 0.3794 |  |
| Circulatory disease | +0.0904 | 0.3668 | ±0.7336 | +0.246 | 0.8053 |  |
| MAG (mg/dL/h) | -0.0136 | 0.0131 | ±0.0262 | -1.037 | 0.2999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.3210**, Adj R² = **0.2764**, F-statistic = **7.19** (p = **3.76e-12**), Residual SE = **2.114** on **213** df, AIC = **1003.0**, BIC = **1054.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1618** | 1.2833 | ±2.5666 | **+18.828** | **4.45e-79** | *** |
| Education: graduate level (vs college) | +0.3199 | 0.3273 | ±0.6545 | +0.978 | 0.3283 |  |
| Education: high school or below (vs college) | +0.0743 | 0.4593 | ±0.9186 | +0.162 | 0.8715 |  |
| Site: UCSD (vs UAB) | -0.2304 | 0.3721 | ±0.7442 | -0.619 | 0.5358 |  |
| **Site: UW (vs UAB)** | **-1.6173** | 0.3437 | ±0.6874 | **-4.705** | **2.53e-06** | *** |
| Season: spring (vs autumn) | +0.1775 | 0.3828 | ±0.7657 | +0.464 | 0.6430 |  |
| **Season: summer (vs autumn)** | **+2.5702** | 0.3988 | ±0.7976 | **+6.445** | **1.16e-10** | *** |
| Season: winter (vs autumn) | -0.8192 | 0.4684 | ±0.9367 | -1.749 | 0.0803 | . |
| Age (years) | +0.0122 | 0.0141 | ±0.0282 | +0.864 | 0.3876 |  |
| BMI (kg/m2) | +0.0170 | 0.0206 | ±0.0411 | +0.828 | 0.4076 |  |
| Hypertension | +0.5062 | 0.3605 | ±0.7211 | +1.404 | 0.1603 |  |
| High cholesterol | -0.5882 | 0.3194 | ±0.6388 | -1.841 | 0.0656 | . |
| Kidney disease | -0.2053 | 0.4124 | ±0.8247 | -0.498 | 0.6185 |  |
| Circulatory disease | +0.0989 | 0.3653 | ±0.7307 | +0.271 | 0.7866 |  |
| Avg. daily range (mg/dL) | -0.0047 | 0.0033 | ±0.0067 | -1.404 | 0.1603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.3145**, Adj R² = **0.2695**, F-statistic = **6.98** (p = **9.22e-12**), Residual SE = **2.125** on **213** df, AIC = **1005.2**, BIC = **1056.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6632** | 1.1666 | ±2.3331 | **+20.284** | **1.76e-91** | *** |
| Education: graduate level (vs college) | +0.3739 | 0.3260 | ±0.6520 | +1.147 | 0.2515 |  |
| Education: high school or below (vs college) | -0.0508 | 0.4607 | ±0.9213 | -0.110 | 0.9122 |  |
| Site: UCSD (vs UAB) | -0.2190 | 0.3810 | ±0.7620 | -0.575 | 0.5655 |  |
| **Site: UW (vs UAB)** | **-1.6013** | 0.3521 | ±0.7042 | **-4.548** | **5.42e-06** | *** |
| Season: spring (vs autumn) | +0.1215 | 0.3782 | ±0.7564 | +0.321 | 0.7481 |  |
| **Season: summer (vs autumn)** | **+2.5664** | 0.4017 | ±0.8034 | **+6.389** | **1.67e-10** | *** |
| Season: winter (vs autumn) | -0.8317 | 0.4689 | ±0.9377 | -1.774 | 0.0761 | . |
| Age (years) | +0.0095 | 0.0143 | ±0.0287 | +0.662 | 0.5077 |  |
| BMI (kg/m2) | +0.0192 | 0.0202 | ±0.0403 | +0.954 | 0.3399 |  |
| Hypertension | +0.5238 | 0.3592 | ±0.7183 | +1.458 | 0.1447 |  |
| High cholesterol | -0.5708 | 0.3177 | ±0.6354 | -1.797 | 0.0724 | . |
| Kidney disease | -0.3321 | 0.4035 | ±0.8070 | -0.823 | 0.4104 |  |
| Circulatory disease | +0.0961 | 0.3656 | ±0.7312 | +0.263 | 0.7926 |  |
| SD of daily means (mg/dL) | -0.0029 | 0.0232 | ±0.0464 | -0.124 | 0.9014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.3180**, Adj R² = **0.2732**, F-statistic = **7.09** (p = **5.74e-12**), Residual SE = **2.119** on **213** df, AIC = **1004.0**, BIC = **1055.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8875** | 1.3863 | ±2.7727 | **+16.509** | **3.14e-61** | *** |
| Education: graduate level (vs college) | +0.3383 | 0.3249 | ±0.6498 | +1.041 | 0.2977 |  |
| Education: high school or below (vs college) | -0.0193 | 0.4573 | ±0.9146 | -0.042 | 0.9664 |  |
| Site: UCSD (vs UAB) | -0.2270 | 0.3779 | ±0.7558 | -0.601 | 0.5481 |  |
| **Site: UW (vs UAB)** | **-1.6162** | 0.3462 | ±0.6923 | **-4.669** | **3.03e-06** | *** |
| Season: spring (vs autumn) | +0.1571 | 0.3784 | ±0.7567 | +0.415 | 0.6781 |  |
| **Season: summer (vs autumn)** | **+2.5567** | 0.4000 | ±0.8000 | **+6.392** | **1.64e-10** | *** |
| Season: winter (vs autumn) | -0.7902 | 0.4725 | ±0.9451 | -1.672 | 0.0945 | . |
| Age (years) | +0.0102 | 0.0142 | ±0.0284 | +0.716 | 0.4739 |  |
| BMI (kg/m2) | +0.0184 | 0.0204 | ±0.0407 | +0.902 | 0.3669 |  |
| Hypertension | +0.5195 | 0.3615 | ±0.7230 | +1.437 | 0.1507 |  |
| High cholesterol | -0.5702 | 0.3176 | ±0.6351 | -1.796 | 0.0725 | . |
| Kidney disease | -0.2751 | 0.3938 | ±0.7877 | -0.698 | 0.4849 |  |
| Circulatory disease | +0.1129 | 0.3655 | ±0.7311 | +0.309 | 0.7575 |  |
| Time in range 70-180, pooled (%) | +0.0085 | 0.0090 | ±0.0181 | +0.946 | 0.3441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.3175**, Adj R² = **0.2726**, F-statistic = **7.08** (p = **6.13e-12**), Residual SE = **2.120** on **213** df, AIC = **1004.2**, BIC = **1055.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9388** | 1.3843 | ±2.7686 | **+16.570** | **1.14e-61** | *** |
| Education: graduate level (vs college) | +0.3415 | 0.3248 | ±0.6495 | +1.051 | 0.2931 |  |
| Education: high school or below (vs college) | -0.0183 | 0.4588 | ±0.9175 | -0.040 | 0.9682 |  |
| Site: UCSD (vs UAB) | -0.2278 | 0.3781 | ±0.7562 | -0.603 | 0.5468 |  |
| **Site: UW (vs UAB)** | **-1.6162** | 0.3466 | ±0.6933 | **-4.662** | **3.12e-06** | *** |
| Season: spring (vs autumn) | +0.1571 | 0.3791 | ±0.7583 | +0.414 | 0.6786 |  |
| **Season: summer (vs autumn)** | **+2.5608** | 0.4001 | ±0.8002 | **+6.400** | **1.55e-10** | *** |
| Season: winter (vs autumn) | -0.7890 | 0.4735 | ±0.9469 | -1.666 | 0.0956 | . |
| Age (years) | +0.0101 | 0.0142 | ±0.0284 | +0.713 | 0.4758 |  |
| BMI (kg/m2) | +0.0183 | 0.0204 | ±0.0407 | +0.900 | 0.3679 |  |
| Hypertension | +0.5175 | 0.3617 | ±0.7233 | +1.431 | 0.1525 |  |
| High cholesterol | -0.5698 | 0.3176 | ±0.6351 | -1.794 | 0.0728 | . |
| Kidney disease | -0.2772 | 0.3946 | ±0.7893 | -0.702 | 0.4825 |  |
| Circulatory disease | +0.1116 | 0.3654 | ±0.7308 | +0.306 | 0.7600 |  |
| Avg. daily time in range 70-180 (%) | +0.0079 | 0.0090 | ±0.0181 | +0.878 | 0.3799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.3154**, Adj R² = **0.2704**, F-statistic = **7.01** (p = **8.22e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.9**, BIC = **1056.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5972** | 1.1440 | ±2.2881 | **+20.626** | **1.59e-94** | *** |
| Education: graduate level (vs college) | +0.3908 | 0.3261 | ±0.6521 | +1.198 | 0.2307 |  |
| Education: high school or below (vs college) | -0.0381 | 0.4515 | ±0.9031 | -0.084 | 0.9327 |  |
| Site: UCSD (vs UAB) | -0.1909 | 0.3691 | ±0.7383 | -0.517 | 0.6051 |  |
| **Site: UW (vs UAB)** | **-1.5647** | 0.3469 | ±0.6938 | **-4.510** | **6.48e-06** | *** |
| Season: spring (vs autumn) | +0.1377 | 0.3784 | ±0.7568 | +0.364 | 0.7160 |  |
| **Season: summer (vs autumn)** | **+2.5708** | 0.4008 | ±0.8016 | **+6.414** | **1.41e-10** | *** |
| Season: winter (vs autumn) | -0.8343 | 0.4675 | ±0.9351 | -1.784 | 0.0744 | . |
| Age (years) | +0.0091 | 0.0141 | ±0.0283 | +0.642 | 0.5212 |  |
| BMI (kg/m2) | +0.0192 | 0.0204 | ±0.0408 | +0.943 | 0.3459 |  |
| Hypertension | +0.5141 | 0.3607 | ±0.7215 | +1.425 | 0.1541 |  |
| High cholesterol | -0.5733 | 0.3170 | ±0.6341 | -1.808 | 0.0706 | . |
| Kidney disease | -0.3389 | 0.3857 | ±0.7713 | -0.879 | 0.3795 |  |
| Circulatory disease | +0.0762 | 0.3644 | ±0.7288 | +0.209 | 0.8343 |  |
| Time < 54 (%) | +0.1067 | 0.1800 | ±0.3599 | +0.593 | 0.5533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.3155**, Adj R² = **0.2705**, F-statistic = **7.01** (p = **8.08e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.8**, BIC = **1056.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6235** | 1.1507 | ±2.3014 | **+20.529** | **1.18e-93** | *** |
| Education: graduate level (vs college) | +0.3959 | 0.3239 | ±0.6478 | +1.222 | 0.2216 |  |
| Education: high school or below (vs college) | -0.0383 | 0.4506 | ±0.9012 | -0.085 | 0.9323 |  |
| Site: UCSD (vs UAB) | -0.1941 | 0.3707 | ±0.7413 | -0.524 | 0.6005 |  |
| **Site: UW (vs UAB)** | **-1.5716** | 0.3483 | ±0.6966 | **-4.512** | **6.42e-06** | *** |
| Season: spring (vs autumn) | +0.1431 | 0.3793 | ±0.7587 | +0.377 | 0.7059 |  |
| **Season: summer (vs autumn)** | **+2.5703** | 0.4034 | ±0.8067 | **+6.372** | **1.86e-10** | *** |
| Season: winter (vs autumn) | -0.8372 | 0.4690 | ±0.9381 | -1.785 | 0.0743 | . |
| Age (years) | +0.0087 | 0.0143 | ±0.0285 | +0.608 | 0.5432 |  |
| BMI (kg/m2) | +0.0193 | 0.0202 | ±0.0404 | +0.958 | 0.3382 |  |
| Hypertension | +0.5171 | 0.3599 | ±0.7198 | +1.437 | 0.1507 |  |
| High cholesterol | -0.5666 | 0.3167 | ±0.6334 | -1.789 | 0.0736 | . |
| Kidney disease | -0.3462 | 0.3847 | ±0.7694 | -0.900 | 0.3682 |  |
| Circulatory disease | +0.0773 | 0.3664 | ±0.7329 | +0.211 | 0.8330 |  |
| Avg. daily time < 54 (%) | +0.1028 | 0.2290 | ±0.4579 | +0.449 | 0.6534 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.3238**, Adj R² = **0.2794**, F-statistic = **7.29** (p = **2.55e-12**), Residual SE = **2.110** on **213** df, AIC = **1002.0**, BIC = **1053.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5972** | 1.1315 | ±2.2630 | **+20.855** | **1.38e-96** | *** |
| Education: graduate level (vs college) | +0.4630 | 0.3237 | ±0.6475 | +1.430 | 0.1527 |  |
| Education: high school or below (vs college) | -0.0771 | 0.4488 | ±0.8976 | -0.172 | 0.8636 |  |
| Site: UCSD (vs UAB) | -0.1788 | 0.3695 | ±0.7390 | -0.484 | 0.6284 |  |
| **Site: UW (vs UAB)** | **-1.5692** | 0.3426 | ±0.6851 | **-4.581** | **4.64e-06** | *** |
| Season: spring (vs autumn) | +0.1910 | 0.3696 | ±0.7392 | +0.517 | 0.6054 |  |
| **Season: summer (vs autumn)** | **+2.5923** | 0.3938 | ±0.7876 | **+6.583** | **4.62e-11** | *** |
| Season: winter (vs autumn) | -0.8120 | 0.4666 | ±0.9332 | -1.740 | 0.0818 | . |
| Age (years) | +0.0060 | 0.0139 | ±0.0278 | +0.430 | 0.6672 |  |
| BMI (kg/m2) | +0.0198 | 0.0209 | ±0.0418 | +0.948 | 0.3431 |  |
| Hypertension | +0.5414 | 0.3534 | ±0.7069 | +1.532 | 0.1256 |  |
| High cholesterol | -0.6040 | 0.3145 | ±0.6289 | -1.921 | 0.0548 | . |
| Kidney disease | -0.3652 | 0.3867 | ±0.7733 | -0.945 | 0.3449 |  |
| Circulatory disease | +0.0874 | 0.3647 | ±0.7294 | +0.240 | 0.8107 |  |
| Time 54-69, pooled (%) | +0.0994 | 0.0574 | ±0.1148 | +1.731 | 0.0835 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.3255**, Adj R² = **0.2812**, F-statistic = **7.34** (p = **2.02e-12**), Residual SE = **2.108** on **213** df, AIC = **1001.5**, BIC = **1052.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6497** | 1.1300 | ±2.2600 | **+20.929** | **2.90e-97** | *** |
| Education: graduate level (vs college) | +0.4703 | 0.3214 | ±0.6428 | +1.463 | 0.1434 |  |
| Education: high school or below (vs college) | -0.0881 | 0.4507 | ±0.9015 | -0.195 | 0.8451 |  |
| Site: UCSD (vs UAB) | -0.1772 | 0.3693 | ±0.7385 | -0.480 | 0.6314 |  |
| **Site: UW (vs UAB)** | **-1.5647** | 0.3415 | ±0.6829 | **-4.582** | **4.59e-06** | *** |
| Season: spring (vs autumn) | +0.1920 | 0.3691 | ±0.7381 | +0.520 | 0.6029 |  |
| **Season: summer (vs autumn)** | **+2.5852** | 0.3937 | ±0.7875 | **+6.566** | **5.17e-11** | *** |
| Season: winter (vs autumn) | -0.8159 | 0.4660 | ±0.9319 | -1.751 | 0.0800 | . |
| Age (years) | +0.0051 | 0.0139 | ±0.0277 | +0.370 | 0.7112 |  |
| BMI (kg/m2) | +0.0197 | 0.0207 | ±0.0414 | +0.949 | 0.3427 |  |
| Hypertension | +0.5451 | 0.3518 | ±0.7037 | +1.549 | 0.1213 |  |
| High cholesterol | -0.6014 | 0.3146 | ±0.6292 | -1.911 | 0.0560 | . |
| Kidney disease | -0.3627 | 0.3841 | ±0.7683 | -0.944 | 0.3450 |  |
| Circulatory disease | +0.0943 | 0.3635 | ±0.7270 | +0.259 | 0.7953 |  |
| Avg. daily time 54-69 (%) | +0.1029 | 0.0539 | ±0.1078 | +1.908 | 0.0563 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.3222**, Adj R² = **0.2776**, F-statistic = **7.23** (p = **3.21e-12**), Residual SE = **2.113** on **213** df, AIC = **1002.6**, BIC = **1054.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5786** | 1.1343 | ±2.2687 | **+20.786** | **5.74e-96** | *** |
| Education: graduate level (vs college) | +0.4496 | 0.3245 | ±0.6490 | +1.386 | 0.1658 |  |
| Education: high school or below (vs college) | -0.0606 | 0.4482 | ±0.8964 | -0.135 | 0.8924 |  |
| Site: UCSD (vs UAB) | -0.1694 | 0.3687 | ±0.7374 | -0.460 | 0.6459 |  |
| **Site: UW (vs UAB)** | **-1.5533** | 0.3430 | ±0.6860 | **-4.529** | **5.94e-06** | *** |
| Season: spring (vs autumn) | +0.1844 | 0.3720 | ±0.7440 | +0.496 | 0.6201 |  |
| **Season: summer (vs autumn)** | **+2.5886** | 0.3959 | ±0.7917 | **+6.539** | **6.19e-11** | *** |
| Season: winter (vs autumn) | -0.8152 | 0.4669 | ±0.9339 | -1.746 | 0.0808 | . |
| Age (years) | +0.0066 | 0.0140 | ±0.0280 | +0.475 | 0.6349 |  |
| BMI (kg/m2) | +0.0196 | 0.0209 | ±0.0418 | +0.937 | 0.3486 |  |
| Hypertension | +0.5330 | 0.3544 | ±0.7088 | +1.504 | 0.1326 |  |
| High cholesterol | -0.5984 | 0.3153 | ±0.6306 | -1.898 | 0.0577 | . |
| Kidney disease | -0.3560 | 0.3869 | ±0.7738 | -0.920 | 0.3575 |  |
| Circulatory disease | +0.0774 | 0.3643 | ±0.7286 | +0.213 | 0.8317 |  |
| Time < 70 (%) | +0.0749 | 0.0487 | ±0.0974 | +1.537 | 0.1243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.3234**, Adj R² = **0.2789**, F-statistic = **7.27** (p = **2.71e-12**), Residual SE = **2.111** on **213** df, AIC = **1002.2**, BIC = **1053.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6359** | 1.1341 | ±2.2682 | **+20.842** | **1.82e-96** | *** |
| Education: graduate level (vs college) | +0.4578 | 0.3219 | ±0.6438 | +1.422 | 0.1550 |  |
| Education: high school or below (vs college) | -0.0679 | 0.4500 | ±0.9001 | -0.151 | 0.8801 |  |
| Site: UCSD (vs UAB) | -0.1703 | 0.3690 | ±0.7381 | -0.461 | 0.6445 |  |
| **Site: UW (vs UAB)** | **-1.5544** | 0.3422 | ±0.6844 | **-4.542** | **5.56e-06** | *** |
| Season: spring (vs autumn) | +0.1885 | 0.3715 | ±0.7430 | +0.507 | 0.6118 |  |
| **Season: summer (vs autumn)** | **+2.5827** | 0.3963 | ±0.7926 | **+6.517** | **7.18e-11** | *** |
| Season: winter (vs autumn) | -0.8205 | 0.4664 | ±0.9327 | -1.759 | 0.0785 | . |
| Age (years) | +0.0058 | 0.0140 | ±0.0280 | +0.413 | 0.6798 |  |
| BMI (kg/m2) | +0.0195 | 0.0206 | ±0.0412 | +0.949 | 0.3428 |  |
| Hypertension | +0.5375 | 0.3530 | ±0.7059 | +1.523 | 0.1278 |  |
| High cholesterol | -0.5911 | 0.3159 | ±0.6317 | -1.871 | 0.0613 | . |
| Kidney disease | -0.3590 | 0.3841 | ±0.7681 | -0.935 | 0.3500 |  |
| Circulatory disease | +0.0828 | 0.3638 | ±0.7276 | +0.228 | 0.8199 |  |
| Avg. daily time < 70 (%) | +0.0758 | 0.0481 | ±0.0963 | +1.575 | 0.1153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.3159**, Adj R² = **0.2709**, F-statistic = **7.02** (p = **7.68e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.7**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6465** | 2.4059 | ±4.8118 | **+9.413** | **4.82e-21** | *** |
| Education: graduate level (vs college) | +0.3619 | 0.3246 | ±0.6493 | +1.115 | 0.2649 |  |
| Education: high school or below (vs college) | -0.0275 | 0.4656 | ±0.9312 | -0.059 | 0.9529 |  |
| Site: UCSD (vs UAB) | -0.2234 | 0.3819 | ±0.7638 | -0.585 | 0.5586 |  |
| **Site: UW (vs UAB)** | **-1.6194** | 0.3531 | ±0.7063 | **-4.586** | **4.53e-06** | *** |
| Season: spring (vs autumn) | +0.1377 | 0.3769 | ±0.7539 | +0.365 | 0.7149 |  |
| **Season: summer (vs autumn)** | **+2.5418** | 0.4024 | ±0.8048 | **+6.317** | **2.68e-10** | *** |
| Season: winter (vs autumn) | -0.8297 | 0.4692 | ±0.9383 | -1.769 | 0.0770 | . |
| Age (years) | +0.0090 | 0.0141 | ±0.0282 | +0.638 | 0.5235 |  |
| BMI (kg/m2) | +0.0187 | 0.0202 | ±0.0403 | +0.928 | 0.3535 |  |
| Hypertension | +0.5285 | 0.3603 | ±0.7206 | +1.467 | 0.1425 |  |
| High cholesterol | -0.5845 | 0.3159 | ±0.6317 | -1.851 | 0.0642 | . |
| Kidney disease | -0.3262 | 0.3854 | ±0.7709 | -0.846 | 0.3974 |  |
| Circulatory disease | +0.1066 | 0.3684 | ±0.7368 | +0.289 | 0.7722 |  |
| Time 54-250, pooled (%) | +0.0108 | 0.0219 | ±0.0438 | +0.491 | 0.6235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.3156**, Adj R² = **0.2706**, F-statistic = **7.02** (p = **7.98e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.8**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6340** | 2.7360 | ±5.4720 | **+8.273** | **1.31e-16** | *** |
| Education: graduate level (vs college) | +0.3625 | 0.3246 | ±0.6492 | +1.117 | 0.2641 |  |
| Education: high school or below (vs college) | -0.0258 | 0.4701 | ±0.9402 | -0.055 | 0.9563 |  |
| Site: UCSD (vs UAB) | -0.2213 | 0.3816 | ±0.7632 | -0.580 | 0.5620 |  |
| **Site: UW (vs UAB)** | **-1.6145** | 0.3524 | ±0.7049 | **-4.581** | **4.63e-06** | *** |
| Season: spring (vs autumn) | +0.1421 | 0.3786 | ±0.7573 | +0.375 | 0.7075 |  |
| **Season: summer (vs autumn)** | **+2.5481** | 0.4020 | ±0.8041 | **+6.338** | **2.33e-10** | *** |
| Season: winter (vs autumn) | -0.8240 | 0.4674 | ±0.9348 | -1.763 | 0.0779 | . |
| Age (years) | +0.0092 | 0.0141 | ±0.0282 | +0.649 | 0.5163 |  |
| BMI (kg/m2) | +0.0186 | 0.0201 | ±0.0402 | +0.924 | 0.3556 |  |
| Hypertension | +0.5278 | 0.3602 | ±0.7205 | +1.465 | 0.1429 |  |
| High cholesterol | -0.5831 | 0.3159 | ±0.6318 | -1.846 | 0.0649 | . |
| Kidney disease | -0.3231 | 0.3873 | ±0.7747 | -0.834 | 0.4042 |  |
| Circulatory disease | +0.1087 | 0.3667 | ±0.7335 | +0.296 | 0.7670 |  |
| Avg. daily time 54-250 (%) | +0.0107 | 0.0254 | ±0.0508 | +0.422 | 0.6732 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.3208**, Adj R² = **0.2762**, F-statistic = **7.19** (p = **3.87e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7043** | 1.1771 | ±2.3542 | **+20.138** | **3.44e-90** | *** |
| Education: graduate level (vs college) | +0.3404 | 0.3246 | ±0.6492 | +1.049 | 0.2943 |  |
| Education: high school or below (vs college) | -0.0305 | 0.4487 | ±0.8974 | -0.068 | 0.9458 |  |
| Site: UCSD (vs UAB) | -0.2206 | 0.3733 | ±0.7466 | -0.591 | 0.5544 |  |
| **Site: UW (vs UAB)** | **-1.5953** | 0.3414 | ±0.6828 | **-4.673** | **2.97e-06** | *** |
| Season: spring (vs autumn) | +0.1791 | 0.3782 | ±0.7565 | +0.474 | 0.6358 |  |
| **Season: summer (vs autumn)** | **+2.5907** | 0.3959 | ±0.7918 | **+6.543** | **6.01e-11** | *** |
| Season: winter (vs autumn) | -0.7523 | 0.4807 | ±0.9613 | -1.565 | 0.1175 |  |
| Age (years) | +0.0109 | 0.0141 | ±0.0283 | +0.772 | 0.4403 |  |
| BMI (kg/m2) | +0.0185 | 0.0206 | ±0.0412 | +0.900 | 0.3682 |  |
| Hypertension | +0.5085 | 0.3597 | ±0.7193 | +1.414 | 0.1574 |  |
| High cholesterol | -0.5529 | 0.3179 | ±0.6358 | -1.739 | 0.0820 | . |
| Kidney disease | -0.2394 | 0.3972 | ±0.7945 | -0.603 | 0.5468 |  |
| Circulatory disease | +0.1095 | 0.3634 | ±0.7268 | +0.301 | 0.7631 |  |
| Time 181-250, pooled (%) | -0.0169 | 0.0118 | ±0.0237 | -1.432 | 0.1521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.3207**, Adj R² = **0.2761**, F-statistic = **7.18** (p = **3.92e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7319** | 1.1813 | ±2.3626 | **+20.090** | **9.11e-90** | *** |
| Education: graduate level (vs college) | +0.3421 | 0.3243 | ±0.6487 | +1.055 | 0.2915 |  |
| Education: high school or below (vs college) | -0.0288 | 0.4491 | ±0.8982 | -0.064 | 0.9489 |  |
| Site: UCSD (vs UAB) | -0.2268 | 0.3741 | ±0.7482 | -0.606 | 0.5444 |  |
| **Site: UW (vs UAB)** | **-1.6049** | 0.3417 | ±0.6834 | **-4.697** | **2.64e-06** | *** |
| Season: spring (vs autumn) | +0.1751 | 0.3778 | ±0.7556 | +0.463 | 0.6431 |  |
| **Season: summer (vs autumn)** | **+2.5860** | 0.3962 | ±0.7924 | **+6.527** | **6.71e-11** | *** |
| Season: winter (vs autumn) | -0.7555 | 0.4799 | ±0.9597 | -1.574 | 0.1154 |  |
| Age (years) | +0.0105 | 0.0141 | ±0.0283 | +0.744 | 0.4566 |  |
| BMI (kg/m2) | +0.0185 | 0.0206 | ±0.0411 | +0.899 | 0.3687 |  |
| Hypertension | +0.5063 | 0.3601 | ±0.7202 | +1.406 | 0.1597 |  |
| High cholesterol | -0.5542 | 0.3178 | ±0.6356 | -1.744 | 0.0812 | . |
| Kidney disease | -0.2419 | 0.3966 | ±0.7931 | -0.610 | 0.5418 |  |
| Circulatory disease | +0.1073 | 0.3636 | ±0.7273 | +0.295 | 0.7680 |  |
| Avg. daily time 181-250 (%) | -0.0163 | 0.0114 | ±0.0229 | -1.425 | 0.1543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.3198**, Adj R² = **0.2751**, F-statistic = **7.15** (p = **4.48e-12**), Residual SE = **2.116** on **213** df, AIC = **1003.4**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7542** | 1.1764 | ±2.3528 | **+20.193** | **1.14e-90** | *** |
| Education: graduate level (vs college) | +0.3391 | 0.3244 | ±0.6488 | +1.045 | 0.2958 |  |
| Education: high school or below (vs college) | -0.0134 | 0.4542 | ±0.9084 | -0.030 | 0.9764 |  |
| Site: UCSD (vs UAB) | -0.2221 | 0.3769 | ±0.7538 | -0.589 | 0.5556 |  |
| **Site: UW (vs UAB)** | **-1.6140** | 0.3444 | ±0.6888 | **-4.687** | **2.78e-06** | *** |
| Season: spring (vs autumn) | +0.1723 | 0.3775 | ±0.7550 | +0.456 | 0.6482 |  |
| **Season: summer (vs autumn)** | **+2.5575** | 0.3984 | ±0.7969 | **+6.419** | **1.38e-10** | *** |
| Season: winter (vs autumn) | -0.7770 | 0.4728 | ±0.9455 | -1.644 | 0.1003 |  |
| Age (years) | +0.0100 | 0.0142 | ±0.0283 | +0.705 | 0.4805 |  |
| BMI (kg/m2) | +0.0182 | 0.0205 | ±0.0409 | +0.889 | 0.3742 |  |
| Hypertension | +0.5220 | 0.3610 | ±0.7220 | +1.446 | 0.1482 |  |
| High cholesterol | -0.5746 | 0.3174 | ±0.6348 | -1.810 | 0.0703 | . |
| Kidney disease | -0.2625 | 0.3934 | ±0.7869 | -0.667 | 0.5046 |  |
| Circulatory disease | +0.1151 | 0.3662 | ±0.7325 | +0.314 | 0.7534 |  |
| Time > 180 (%) | -0.0103 | 0.0089 | ±0.0178 | -1.150 | 0.2501 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.3195**, Adj R² = **0.2748**, F-statistic = **7.14** (p = **4.63e-12**), Residual SE = **2.117** on **213** df, AIC = **1003.5**, BIC = **1054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7582** | 1.1781 | ±2.3562 | **+20.167** | **1.92e-90** | *** |
| Education: graduate level (vs college) | +0.3410 | 0.3242 | ±0.6483 | +1.052 | 0.2929 |  |
| Education: high school or below (vs college) | -0.0108 | 0.4551 | ±0.9101 | -0.024 | 0.9811 |  |
| Site: UCSD (vs UAB) | -0.2242 | 0.3774 | ±0.7547 | -0.594 | 0.5525 |  |
| **Site: UW (vs UAB)** | **-1.6157** | 0.3444 | ±0.6888 | **-4.691** | **2.72e-06** | *** |
| Season: spring (vs autumn) | +0.1750 | 0.3784 | ±0.7568 | +0.462 | 0.6438 |  |
| **Season: summer (vs autumn)** | **+2.5611** | 0.3983 | ±0.7966 | **+6.430** | **1.28e-10** | *** |
| Season: winter (vs autumn) | -0.7728 | 0.4738 | ±0.9476 | -1.631 | 0.1029 |  |
| Age (years) | +0.0099 | 0.0142 | ±0.0283 | +0.698 | 0.4854 |  |
| BMI (kg/m2) | +0.0181 | 0.0204 | ±0.0409 | +0.883 | 0.3773 |  |
| Hypertension | +0.5200 | 0.3612 | ±0.7223 | +1.440 | 0.1499 |  |
| High cholesterol | -0.5730 | 0.3174 | ±0.6349 | -1.805 | 0.0711 | . |
| Kidney disease | -0.2607 | 0.3942 | ±0.7885 | -0.661 | 0.5085 |  |
| Circulatory disease | +0.1157 | 0.3661 | ±0.7321 | +0.316 | 0.7519 |  |
| Avg. daily time > 180 (%) | -0.0101 | 0.0090 | ±0.0180 | -1.121 | 0.2623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.3171**, Adj R² = **0.2722**, F-statistic = **7.07** (p = **6.46e-12**), Residual SE = **2.121** on **213** df, AIC = **1004.3**, BIC = **1055.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7185** | 1.1657 | ±2.3314 | **+20.347** | **4.96e-92** | *** |
| Education: graduate level (vs college) | +0.3548 | 0.3244 | ±0.6489 | +1.093 | 0.2742 |  |
| Education: high school or below (vs college) | -0.0372 | 0.4551 | ±0.9103 | -0.082 | 0.9348 |  |
| Site: UCSD (vs UAB) | -0.2234 | 0.3805 | ±0.7609 | -0.587 | 0.5570 |  |
| **Site: UW (vs UAB)** | **-1.6090** | 0.3461 | ±0.6921 | **-4.649** | **3.33e-06** | *** |
| Season: spring (vs autumn) | +0.1519 | 0.3765 | ±0.7531 | +0.403 | 0.6867 |  |
| **Season: summer (vs autumn)** | **+2.5444** | 0.4013 | ±0.8026 | **+6.340** | **2.30e-10** | *** |
| Season: winter (vs autumn) | -0.7972 | 0.4702 | ±0.9403 | -1.696 | 0.0900 | . |
| Age (years) | +0.0091 | 0.0141 | ±0.0282 | +0.646 | 0.5182 |  |
| BMI (kg/m2) | +0.0188 | 0.0204 | ±0.0409 | +0.920 | 0.3573 |  |
| Hypertension | +0.5340 | 0.3575 | ±0.7150 | +1.494 | 0.1353 |  |
| High cholesterol | -0.5638 | 0.3186 | ±0.6373 | -1.769 | 0.0768 | . |
| Kidney disease | -0.3217 | 0.3845 | ±0.7690 | -0.837 | 0.4028 |  |
| Circulatory disease | +0.1164 | 0.3660 | ±0.7321 | +0.318 | 0.7506 |  |
| Nocturnal time > 180 (%) | -0.0073 | 0.0102 | ±0.0204 | -0.722 | 0.4705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.3161**, Adj R² = **0.2711**, F-statistic = **7.03** (p = **7.43e-12**), Residual SE = **2.122** on **213** df, AIC = **1004.6**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6920** | 1.1823 | ±2.3646 | **+20.039** | **2.54e-89** | *** |
| Education: graduate level (vs college) | +0.3550 | 0.3282 | ±0.6563 | +1.082 | 0.2794 |  |
| Education: high school or below (vs college) | -0.0310 | 0.4529 | ±0.9057 | -0.068 | 0.9455 |  |
| Site: UCSD (vs UAB) | -0.2204 | 0.3720 | ±0.7440 | -0.593 | 0.5534 |  |
| **Site: UW (vs UAB)** | **-1.5796** | 0.3456 | ±0.6912 | **-4.571** | **4.86e-06** | *** |
| Season: spring (vs autumn) | +0.1424 | 0.3819 | ±0.7638 | +0.373 | 0.7092 |  |
| **Season: summer (vs autumn)** | **+2.5823** | 0.3984 | ±0.7968 | **+6.482** | **9.08e-11** | *** |
| Season: winter (vs autumn) | -0.8352 | 0.4669 | ±0.9339 | -1.789 | 0.0737 | . |
| Age (years) | +0.0109 | 0.0141 | ±0.0283 | +0.771 | 0.4406 |  |
| BMI (kg/m2) | +0.0178 | 0.0207 | ±0.0414 | +0.859 | 0.3903 |  |
| Hypertension | +0.5212 | 0.3600 | ±0.7199 | +1.448 | 0.1476 |  |
| High cholesterol | -0.5783 | 0.3179 | ±0.6358 | -1.819 | 0.0689 | . |
| Kidney disease | -0.2883 | 0.3968 | ±0.7937 | -0.727 | 0.4675 |  |
| Circulatory disease | +0.0971 | 0.3651 | ±0.7303 | +0.266 | 0.7903 |  |
| Any reading > 250 during wear (0/1) | -0.2161 | 0.3054 | ±0.6108 | -0.708 | 0.4792 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.3161**, Adj R² = **0.2711**, F-statistic = **7.03** (p = **7.45e-12**), Residual SE = **2.122** on **213** df, AIC = **1004.6**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7240** | 1.1626 | ±2.3252 | **+20.406** | **1.49e-92** | *** |
| Education: graduate level (vs college) | +0.3615 | 0.3246 | ±0.6492 | +1.114 | 0.2655 |  |
| Education: high school or below (vs college) | -0.0238 | 0.4664 | ±0.9328 | -0.051 | 0.9593 |  |
| Site: UCSD (vs UAB) | -0.2209 | 0.3805 | ±0.7610 | -0.580 | 0.5616 |  |
| **Site: UW (vs UAB)** | **-1.6176** | 0.3519 | ±0.7037 | **-4.597** | **4.28e-06** | *** |
| Season: spring (vs autumn) | +0.1404 | 0.3770 | ±0.7541 | +0.372 | 0.7096 |  |
| **Season: summer (vs autumn)** | **+2.5402** | 0.4027 | ±0.8054 | **+6.308** | **2.83e-10** | *** |
| Season: winter (vs autumn) | -0.8284 | 0.4694 | ±0.9388 | -1.765 | 0.0776 | . |
| Age (years) | +0.0090 | 0.0141 | ±0.0282 | +0.635 | 0.5257 |  |
| BMI (kg/m2) | +0.0186 | 0.0202 | ±0.0404 | +0.923 | 0.3558 |  |
| Hypertension | +0.5289 | 0.3602 | ±0.7204 | +1.468 | 0.1420 |  |
| High cholesterol | -0.5862 | 0.3159 | ±0.6318 | -1.856 | 0.0635 | . |
| Kidney disease | -0.3240 | 0.3856 | ±0.7712 | -0.840 | 0.4007 |  |
| Circulatory disease | +0.1061 | 0.3694 | ±0.7388 | +0.287 | 0.7740 |  |
| Time > 250 (%) | -0.0116 | 0.0224 | ±0.0448 | -0.518 | 0.6047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.3158**, Adj R² = **0.2709**, F-statistic = **7.02** (p = **7.69e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.7**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7120** | 1.1614 | ±2.3227 | **+20.417** | **1.17e-92** | *** |
| Education: graduate level (vs college) | +0.3620 | 0.3246 | ±0.6492 | +1.115 | 0.2648 |  |
| Education: high school or below (vs college) | -0.0206 | 0.4715 | ±0.9430 | -0.044 | 0.9651 |  |
| Site: UCSD (vs UAB) | -0.2189 | 0.3804 | ±0.7607 | -0.575 | 0.5650 |  |
| **Site: UW (vs UAB)** | **-1.6136** | 0.3511 | ±0.7023 | **-4.595** | **4.32e-06** | *** |
| Season: spring (vs autumn) | +0.1467 | 0.3793 | ±0.7586 | +0.387 | 0.6989 |  |
| **Season: summer (vs autumn)** | **+2.5461** | 0.4019 | ±0.8037 | **+6.336** | **2.36e-10** | *** |
| Season: winter (vs autumn) | -0.8219 | 0.4679 | ±0.9357 | -1.757 | 0.0790 | . |
| Age (years) | +0.0091 | 0.0141 | ±0.0282 | +0.643 | 0.5202 |  |
| BMI (kg/m2) | +0.0185 | 0.0201 | ±0.0403 | +0.918 | 0.3586 |  |
| Hypertension | +0.5290 | 0.3599 | ±0.7199 | +1.470 | 0.1417 |  |
| High cholesterol | -0.5846 | 0.3159 | ±0.6319 | -1.850 | 0.0642 | . |
| Kidney disease | -0.3205 | 0.3874 | ±0.7748 | -0.827 | 0.4080 |  |
| Circulatory disease | +0.1090 | 0.3681 | ±0.7361 | +0.296 | 0.7671 |  |
| Avg. daily time > 250 (%) | -0.0120 | 0.0265 | ±0.0530 | -0.455 | 0.6495 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.1865**, Adj R² = **0.1371**, F-statistic = **3.77** (p = **1.87e-05**), Residual SE = **6.678** on **214** df, AIC = **1526.5**, BIC = **1574.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5096** | 3.8285 | ±7.6570 | **+12.671** | **8.60e-37** | *** |
| Education: graduate level (vs college) | -0.6613 | 1.0542 | ±2.1083 | -0.627 | 0.5304 |  |
| Education: high school or below (vs college) | -0.3239 | 1.4081 | ±2.8162 | -0.230 | 0.8181 |  |
| **Site: UCSD (vs UAB)** | **+3.7523** | 1.1584 | ±2.3168 | **+3.239** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8900 | 1.0155 | ±2.0310 | -0.876 | 0.3808 |  |
| Season: spring (vs autumn) | -1.2987 | 1.2064 | ±2.4127 | -1.077 | 0.2817 |  |
| Season: summer (vs autumn) | +1.5588 | 1.1603 | ±2.3206 | +1.343 | 0.1791 |  |
| **Season: winter (vs autumn)** | **-5.8431** | 1.5066 | ±3.0132 | **-3.878** | **1.05e-04** | *** |
| Age (years) | -0.0646 | 0.0411 | ±0.0823 | -1.569 | 0.1166 |  |
| BMI (kg/m2) | +0.0198 | 0.0726 | ±0.1451 | +0.272 | 0.7853 |  |
| Hypertension | +0.5231 | 1.1662 | ±2.3323 | +0.449 | 0.6538 |  |
| High cholesterol | -0.2123 | 0.9893 | ±1.9787 | -0.215 | 0.8301 |  |
| Kidney disease | +0.8095 | 1.2537 | ±2.5073 | +0.646 | 0.5185 |  |
| Circulatory disease | +0.2229 | 1.0598 | ±2.1195 | +0.210 | 0.8334 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.1904**, Adj R² = **0.1372**, F-statistic = **3.58** (p = **2.57e-05**), Residual SE = **6.678** on **213** df, AIC = **1527.4**, BIC = **1578.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2534** | 4.7920 | ±9.5840 | **+9.652** | **4.81e-22** | *** |
| Education: graduate level (vs college) | -0.5257 | 1.0815 | ±2.1631 | -0.486 | 0.6269 |  |
| Education: high school or below (vs college) | -0.4399 | 1.4099 | ±2.8199 | -0.312 | 0.7550 |  |
| **Site: UCSD (vs UAB)** | **+3.7670** | 1.1649 | ±2.3297 | **+3.234** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8457 | 1.0090 | ±2.0180 | -0.838 | 0.4019 |  |
| Season: spring (vs autumn) | -1.3830 | 1.2078 | ±2.4155 | -1.145 | 0.2522 |  |
| Season: summer (vs autumn) | +1.5987 | 1.1649 | ±2.3297 | +1.372 | 0.1699 |  |
| **Season: winter (vs autumn)** | **-5.9079** | 1.5245 | ±3.0489 | **-3.875** | **1.06e-04** | *** |
| Age (years) | -0.0707 | 0.0411 | ±0.0822 | -1.720 | 0.0854 | . |
| BMI (kg/m2) | +0.0187 | 0.0732 | ±0.1463 | +0.255 | 0.7986 |  |
| Hypertension | +0.4613 | 1.1611 | ±2.3223 | +0.397 | 0.6912 |  |
| High cholesterol | -0.1520 | 1.0030 | ±2.0060 | -0.152 | 0.8796 |  |
| Kidney disease | +0.7684 | 1.2485 | ±2.4970 | +0.615 | 0.5382 |  |
| Circulatory disease | +0.2142 | 1.0642 | ±2.1285 | +0.201 | 0.8405 |  |
| HbA1c (%) | +0.4154 | 0.4366 | ±0.8732 | +0.952 | 0.3413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.1924**, Adj R² = **0.1394**, F-statistic = **3.63** (p = **2.09e-05**), Residual SE = **6.670** on **213** df, AIC = **1526.8**, BIC = **1578.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.1463** | 4.3777 | ±8.7554 | **+10.541** | **5.58e-26** | *** |
| Education: graduate level (vs college) | -0.6024 | 1.0552 | ±2.1103 | -0.571 | 0.5681 |  |
| Education: high school or below (vs college) | -0.4440 | 1.4069 | ±2.8138 | -0.316 | 0.7523 |  |
| **Site: UCSD (vs UAB)** | **+3.7524** | 1.1581 | ±2.3161 | **+3.240** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8528 | 1.0146 | ±2.0292 | -0.840 | 0.4006 |  |
| Season: spring (vs autumn) | -1.5059 | 1.2089 | ±2.4178 | -1.246 | 0.2129 |  |
| Season: summer (vs autumn) | +1.5488 | 1.1621 | ±2.3241 | +1.333 | 0.1826 |  |
| **Season: winter (vs autumn)** | **-6.0063** | 1.5329 | ±3.0657 | **-3.918** | **8.91e-05** | *** |
| Age (years) | -0.0649 | 0.0408 | ±0.0816 | -1.590 | 0.1119 |  |
| BMI (kg/m2) | +0.0214 | 0.0736 | ±0.1472 | +0.290 | 0.7717 |  |
| Hypertension | +0.4804 | 1.1600 | ±2.3200 | +0.414 | 0.6788 |  |
| High cholesterol | -0.1536 | 0.9984 | ±1.9969 | -0.154 | 0.8778 |  |
| Kidney disease | +0.6424 | 1.2418 | ±2.4836 | +0.517 | 0.6050 |  |
| Circulatory disease | +0.1634 | 1.0663 | ±2.1326 | +0.153 | 0.8782 |  |
| Mean glucose (mg/dL) | +0.0180 | 0.0141 | ±0.0282 | +1.279 | 0.2009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.1924**, Adj R² = **0.1394**, F-statistic = **3.63** (p = **2.09e-05**), Residual SE = **6.670** on **213** df, AIC = **1526.8**, BIC = **1578.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6534** | 5.5906 | ±11.1813 | **+7.808** | **5.80e-15** | *** |
| Education: graduate level (vs college) | -0.6024 | 1.0552 | ±2.1103 | -0.571 | 0.5681 |  |
| Education: high school or below (vs college) | -0.4440 | 1.4069 | ±2.8138 | -0.316 | 0.7523 |  |
| **Site: UCSD (vs UAB)** | **+3.7524** | 1.1581 | ±2.3161 | **+3.240** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8528 | 1.0146 | ±2.0292 | -0.840 | 0.4006 |  |
| Season: spring (vs autumn) | -1.5059 | 1.2089 | ±2.4178 | -1.246 | 0.2129 |  |
| Season: summer (vs autumn) | +1.5488 | 1.1621 | ±2.3241 | +1.333 | 0.1826 |  |
| **Season: winter (vs autumn)** | **-6.0063** | 1.5329 | ±3.0657 | **-3.918** | **8.91e-05** | *** |
| Age (years) | -0.0649 | 0.0408 | ±0.0816 | -1.590 | 0.1119 |  |
| BMI (kg/m2) | +0.0214 | 0.0736 | ±0.1472 | +0.290 | 0.7717 |  |
| Hypertension | +0.4804 | 1.1600 | ±2.3200 | +0.414 | 0.6788 |  |
| High cholesterol | -0.1536 | 0.9984 | ±1.9969 | -0.154 | 0.8778 |  |
| Kidney disease | +0.6424 | 1.2418 | ±2.4836 | +0.517 | 0.6050 |  |
| Circulatory disease | +0.1634 | 1.0663 | ±2.1326 | +0.153 | 0.8782 |  |
| GMI (%) | +0.7531 | 0.5889 | ±1.1778 | +1.279 | 0.2009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.1872**, Adj R² = **0.1338**, F-statistic = **3.50** (p = **3.56e-05**), Residual SE = **6.691** on **213** df, AIC = **1528.3**, BIC = **1579.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7173** | 4.3362 | ±8.6724 | **+11.004** | **3.64e-28** | *** |
| Education: graduate level (vs college) | -0.6594 | 1.0563 | ±2.1126 | -0.624 | 0.5324 |  |
| Education: high school or below (vs college) | -0.3613 | 1.4084 | ±2.8167 | -0.257 | 0.7976 |  |
| **Site: UCSD (vs UAB)** | **+3.7502** | 1.1623 | ±2.3247 | **+3.226** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8839 | 1.0184 | ±2.0369 | -0.868 | 0.3854 |  |
| Season: spring (vs autumn) | -1.3717 | 1.2148 | ±2.4295 | -1.129 | 0.2588 |  |
| Season: summer (vs autumn) | +1.5663 | 1.1644 | ±2.3288 | +1.345 | 0.1786 |  |
| **Season: winter (vs autumn)** | **-5.8984** | 1.5379 | ±3.0758 | **-3.835** | **1.25e-04** | *** |
| Age (years) | -0.0636 | 0.0412 | ±0.0823 | -1.545 | 0.1223 |  |
| BMI (kg/m2) | +0.0200 | 0.0731 | ±0.1462 | +0.273 | 0.7848 |  |
| Hypertension | +0.4963 | 1.1607 | ±2.3213 | +0.428 | 0.6689 |  |
| High cholesterol | -0.2074 | 0.9941 | ±1.9882 | -0.209 | 0.8348 |  |
| Kidney disease | +0.7977 | 1.2585 | ±2.5170 | +0.634 | 0.5262 |  |
| Circulatory disease | +0.2018 | 1.0723 | ±2.1446 | +0.188 | 0.8507 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0060 | 0.0137 | ±0.0275 | +0.438 | 0.6617 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1891**, Adj R² = **0.1358**, F-statistic = **3.55** (p = **2.93e-05**), Residual SE = **6.683** on **213** df, AIC = **1527.7**, BIC = **1579.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8914** | 4.1056 | ±8.2113 | **+11.665** | **1.93e-31** | *** |
| Education: graduate level (vs college) | -0.5574 | 1.0589 | ±2.1178 | -0.526 | 0.5986 |  |
| Education: high school or below (vs college) | -0.4969 | 1.4291 | ±2.8581 | -0.348 | 0.7281 |  |
| **Site: UCSD (vs UAB)** | **+3.7765** | 1.1604 | ±2.3208 | **+3.255** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8317 | 1.0242 | ±2.0485 | -0.812 | 0.4168 |  |
| Season: spring (vs autumn) | -1.3532 | 1.2126 | ±2.4252 | -1.116 | 0.2645 |  |
| Season: summer (vs autumn) | +1.5924 | 1.1596 | ±2.3193 | +1.373 | 0.1697 |  |
| **Season: winter (vs autumn)** | **-5.8992** | 1.5185 | ±3.0370 | **-3.885** | **1.02e-04** | *** |
| Age (years) | -0.0700 | 0.0410 | ±0.0821 | -1.705 | 0.0882 | . |
| BMI (kg/m2) | +0.0229 | 0.0745 | ±0.1491 | +0.308 | 0.7583 |  |
| Hypertension | +0.5032 | 1.1665 | ±2.3330 | +0.431 | 0.6662 |  |
| High cholesterol | -0.1626 | 1.0041 | ±2.0082 | -0.162 | 0.8714 |  |
| Kidney disease | +0.5602 | 1.2450 | ±2.4899 | +0.450 | 0.6527 |  |
| Circulatory disease | +0.2289 | 1.0616 | ±2.1233 | +0.216 | 0.8293 |  |
| Glucose SD, pooled (mg/dL) | +0.0251 | 0.0296 | ±0.0592 | +0.849 | 0.3962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1913**, Adj R² = **0.1382**, F-statistic = **3.60** (p = **2.35e-05**), Residual SE = **6.674** on **213** df, AIC = **1527.1**, BIC = **1578.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6030** | 4.0903 | ±8.1807 | **+11.638** | **2.64e-31** | *** |
| Education: graduate level (vs college) | -0.5163 | 1.0571 | ±2.1141 | -0.488 | 0.6252 |  |
| Education: high school or below (vs college) | -0.6049 | 1.4268 | ±2.8535 | -0.424 | 0.6716 |  |
| **Site: UCSD (vs UAB)** | **+3.7804** | 1.1558 | ±2.3115 | **+3.271** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8240 | 1.0229 | ±2.0459 | -0.806 | 0.4205 |  |
| Season: spring (vs autumn) | -1.4155 | 1.2172 | ±2.4344 | -1.163 | 0.2449 |  |
| Season: summer (vs autumn) | +1.5967 | 1.1583 | ±2.3165 | +1.378 | 0.1681 |  |
| **Season: winter (vs autumn)** | **-5.9032** | 1.5109 | ±3.0218 | **-3.907** | **9.34e-05** | *** |
| Age (years) | -0.0720 | 0.0411 | ±0.0822 | -1.752 | 0.0798 | . |
| BMI (kg/m2) | +0.0250 | 0.0746 | ±0.1491 | +0.335 | 0.7372 |  |
| Hypertension | +0.5163 | 1.1658 | ±2.3315 | +0.443 | 0.6579 |  |
| High cholesterol | -0.1474 | 1.0027 | ±2.0054 | -0.147 | 0.8831 |  |
| Kidney disease | +0.4595 | 1.2376 | ±2.4752 | +0.371 | 0.7104 |  |
| Circulatory disease | +0.2456 | 1.0577 | ±2.1153 | +0.232 | 0.8163 |  |
| Avg. daily SD (mg/dL) | +0.0405 | 0.0335 | ±0.0669 | +1.212 | 0.2257 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.1869**, Adj R² = **0.1334**, F-statistic = **3.50** (p = **3.68e-05**), Residual SE = **6.692** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1583** | 4.3860 | ±8.7720 | **+10.980** | **4.77e-28** | *** |
| Education: graduate level (vs college) | -0.6150 | 1.0595 | ±2.1189 | -0.581 | 0.5616 |  |
| Education: high school or below (vs college) | -0.4002 | 1.4563 | ±2.9126 | -0.275 | 0.7834 |  |
| **Site: UCSD (vs UAB)** | **+3.7656** | 1.1637 | ±2.3274 | **+3.236** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8656 | 1.0278 | ±2.0555 | -0.842 | 0.3997 |  |
| Season: spring (vs autumn) | -1.2981 | 1.2103 | ±2.4205 | -1.073 | 0.2835 |  |
| Season: summer (vs autumn) | +1.5630 | 1.1626 | ±2.3253 | +1.344 | 0.1788 |  |
| **Season: winter (vs autumn)** | **-5.8486** | 1.5167 | ±3.0335 | **-3.856** | **1.15e-04** | *** |
| Age (years) | -0.0681 | 0.0418 | ±0.0836 | -1.630 | 0.1031 |  |
| BMI (kg/m2) | +0.0211 | 0.0751 | ±0.1503 | +0.281 | 0.7785 |  |
| Hypertension | +0.5237 | 1.1706 | ±2.3412 | +0.447 | 0.6546 |  |
| High cholesterol | -0.1980 | 1.0016 | ±2.0031 | -0.198 | 0.8433 |  |
| Kidney disease | +0.6980 | 1.2968 | ±2.5936 | +0.538 | 0.5904 |  |
| Circulatory disease | +0.2313 | 1.0647 | ±2.1294 | +0.217 | 0.8280 |  |
| CV (%) | +0.0212 | 0.0757 | ±0.1515 | +0.280 | 0.7791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.1869**, Adj R² = **0.1335**, F-statistic = **3.50** (p = **3.65e-05**), Residual SE = **6.692** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2629** | 3.9733 | ±7.9467 | **+12.398** | **2.67e-35** | *** |
| Education: graduate level (vs college) | -0.6120 | 1.0722 | ±2.1443 | -0.571 | 0.5681 |  |
| Education: high school or below (vs college) | -0.4087 | 1.4406 | ±2.8812 | -0.284 | 0.7766 |  |
| **Site: UCSD (vs UAB)** | **+3.7546** | 1.1624 | ±2.3247 | **+3.230** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8727 | 1.0238 | ±2.0475 | -0.852 | 0.3940 |  |
| Season: spring (vs autumn) | -1.3107 | 1.2142 | ±2.4284 | -1.079 | 0.2804 |  |
| Season: summer (vs autumn) | +1.5502 | 1.1642 | ±2.3285 | +1.331 | 0.1830 |  |
| **Season: winter (vs autumn)** | **-5.8524** | 1.5171 | ±3.0343 | **-3.858** | **1.15e-04** | *** |
| Age (years) | -0.0688 | 0.0417 | ±0.0833 | -1.652 | 0.0986 | . |
| BMI (kg/m2) | +0.0206 | 0.0738 | ±0.1475 | +0.279 | 0.7799 |  |
| Hypertension | +0.5330 | 1.1709 | ±2.3418 | +0.455 | 0.6490 |  |
| High cholesterol | -0.1942 | 1.0012 | ±2.0025 | -0.194 | 0.8462 |  |
| Kidney disease | +0.7220 | 1.2751 | ±2.5502 | +0.566 | 0.5712 |  |
| Circulatory disease | +0.2151 | 1.0684 | ±2.1368 | +0.201 | 0.8404 |  |
| Mean / SD ratio | -0.1176 | 0.3774 | ±0.7547 | -0.312 | 0.7553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1881**, Adj R² = **0.1347**, F-statistic = **3.52** (p = **3.26e-05**), Residual SE = **6.688** on **213** df, AIC = **1528.0**, BIC = **1579.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9220** | 3.9776 | ±7.9552 | **+12.551** | **3.94e-36** | *** |
| Education: graduate level (vs college) | -0.5550 | 1.0714 | ±2.1429 | -0.518 | 0.6045 |  |
| Education: high school or below (vs college) | -0.4935 | 1.4276 | ±2.8553 | -0.346 | 0.7296 |  |
| **Site: UCSD (vs UAB)** | **+3.7393** | 1.1584 | ±2.3168 | **+3.228** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8700 | 1.0217 | ±2.0434 | -0.852 | 0.3945 |  |
| Season: spring (vs autumn) | -1.3135 | 1.2138 | ±2.4276 | -1.082 | 0.2792 |  |
| Season: summer (vs autumn) | +1.5568 | 1.1599 | ±2.3199 | +1.342 | 0.1795 |  |
| **Season: winter (vs autumn)** | **-5.8322** | 1.5065 | ±3.0130 | **-3.871** | **1.08e-04** | *** |
| Age (years) | -0.0730 | 0.0420 | ±0.0841 | -1.737 | 0.0824 | . |
| BMI (kg/m2) | +0.0218 | 0.0739 | ±0.1477 | +0.295 | 0.7680 |  |
| Hypertension | +0.5637 | 1.1674 | ±2.3348 | +0.483 | 0.6292 |  |
| High cholesterol | -0.1927 | 0.9972 | ±1.9944 | -0.193 | 0.8468 |  |
| Kidney disease | +0.6829 | 1.2493 | ±2.4986 | +0.547 | 0.5846 |  |
| Circulatory disease | +0.2228 | 1.0668 | ±2.1336 | +0.209 | 0.8346 |  |
| Avg. daily mean/SD | -0.1875 | 0.2819 | ±0.5638 | -0.665 | 0.5059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.1867**, Adj R² = **0.1333**, F-statistic = **3.49** (p = **3.73e-05**), Residual SE = **6.693** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1315** | 4.1725 | ±8.3451 | **+11.535** | **8.76e-31** | *** |
| Education: graduate level (vs college) | -0.6408 | 1.0769 | ±2.1538 | -0.595 | 0.5518 |  |
| Education: high school or below (vs college) | -0.3789 | 1.3931 | ±2.7862 | -0.272 | 0.7856 |  |
| **Site: UCSD (vs UAB)** | **+3.7394** | 1.1564 | ±2.3129 | **+3.234** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8670 | 1.0286 | ±2.0571 | -0.843 | 0.3993 |  |
| Season: spring (vs autumn) | -1.3123 | 1.2156 | ±2.4312 | -1.080 | 0.2803 |  |
| Season: summer (vs autumn) | +1.5689 | 1.1644 | ±2.3289 | +1.347 | 0.1779 |  |
| **Season: winter (vs autumn)** | **-5.8373** | 1.5090 | ±3.0179 | **-3.868** | **1.10e-04** | *** |
| Age (years) | -0.0651 | 0.0416 | ±0.0831 | -1.566 | 0.1173 |  |
| BMI (kg/m2) | +0.0188 | 0.0724 | ±0.1448 | +0.260 | 0.7949 |  |
| Hypertension | +0.5307 | 1.1682 | ±2.3364 | +0.454 | 0.6496 |  |
| High cholesterol | -0.2109 | 0.9928 | ±1.9856 | -0.212 | 0.8318 |  |
| Kidney disease | +0.8073 | 1.2601 | ±2.5203 | +0.641 | 0.5218 |  |
| Circulatory disease | +0.2241 | 1.0651 | ±2.1301 | +0.210 | 0.8334 |  |
| MAG (mg/dL/h) | +0.0097 | 0.0380 | ±0.0760 | +0.256 | 0.7983 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.1899**, Adj R² = **0.1367**, F-statistic = **3.57** (p = **2.71e-05**), Residual SE = **6.680** on **213** df, AIC = **1527.5**, BIC = **1579.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4313** | 4.1514 | ±8.3028 | **+11.425** | **3.12e-30** | *** |
| Education: graduate level (vs college) | -0.5355 | 1.0638 | ±2.1276 | -0.503 | 0.6147 |  |
| Education: high school or below (vs college) | -0.5863 | 1.4318 | ±2.8635 | -0.410 | 0.6822 |  |
| **Site: UCSD (vs UAB)** | **+3.7778** | 1.1584 | ±2.3169 | **+3.261** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8488 | 1.0245 | ±2.0491 | -0.828 | 0.4074 |  |
| Season: spring (vs autumn) | -1.4102 | 1.2223 | ±2.4447 | -1.154 | 0.2486 |  |
| Season: summer (vs autumn) | +1.5528 | 1.1593 | ±2.3185 | +1.339 | 0.1804 |  |
| **Season: winter (vs autumn)** | **-5.8844** | 1.5126 | ±3.0252 | **-3.890** | **1.00e-04** | *** |
| Age (years) | -0.0706 | 0.0415 | ±0.0830 | -1.699 | 0.0893 | . |
| BMI (kg/m2) | +0.0247 | 0.0744 | ±0.1488 | +0.332 | 0.7401 |  |
| Hypertension | +0.5469 | 1.1675 | ±2.3351 | +0.468 | 0.6395 |  |
| High cholesterol | -0.1726 | 1.0002 | ±2.0004 | -0.173 | 0.8630 |  |
| Kidney disease | +0.5221 | 1.2389 | ±2.4778 | +0.421 | 0.6734 |  |
| Circulatory disease | +0.2087 | 1.0616 | ±2.1233 | +0.197 | 0.8442 |  |
| Avg. daily range (mg/dL) | +0.0096 | 0.0094 | ±0.0189 | +1.019 | 0.3080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1332**, F-statistic = **3.49** (p = **3.78e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.4**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4503** | 3.9771 | ±7.9541 | **+12.182** | **3.86e-34** | *** |
| Education: graduate level (vs college) | -0.6445 | 1.0625 | ±2.1250 | -0.607 | 0.5441 |  |
| Education: high school or below (vs college) | -0.3296 | 1.4212 | ±2.8424 | -0.232 | 0.8166 |  |
| **Site: UCSD (vs UAB)** | **+3.7545** | 1.1635 | ±2.3270 | **+3.227** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8804 | 1.0217 | ±2.0435 | -0.862 | 0.3889 |  |
| Season: spring (vs autumn) | -1.2944 | 1.2097 | ±2.4194 | -1.070 | 0.2846 |  |
| Season: summer (vs autumn) | +1.5609 | 1.1644 | ±2.3288 | +1.341 | 0.1801 |  |
| **Season: winter (vs autumn)** | **-5.8608** | 1.5354 | ±3.0708 | **-3.817** | **1.35e-04** | *** |
| Age (years) | -0.0650 | 0.0411 | ±0.0821 | -1.584 | 0.1131 |  |
| BMI (kg/m2) | +0.0202 | 0.0739 | ±0.1478 | +0.273 | 0.7848 |  |
| Hypertension | +0.5090 | 1.1695 | ±2.3390 | +0.435 | 0.6634 |  |
| High cholesterol | -0.2078 | 0.9978 | ±1.9955 | -0.208 | 0.8350 |  |
| Kidney disease | +0.7795 | 1.2539 | ±2.5078 | +0.622 | 0.5342 |  |
| Circulatory disease | +0.2133 | 1.0795 | ±2.1589 | +0.198 | 0.8434 |  |
| SD of daily means (mg/dL) | +0.0067 | 0.0498 | ±0.0996 | +0.136 | 0.8922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.1928**, Adj R² = **0.1398**, F-statistic = **3.63** (p = **2.01e-05**), Residual SE = **6.668** on **213** df, AIC = **1526.7**, BIC = **1578.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3873** | 4.2360 | ±8.4720 | **+12.131** | **7.23e-34** | *** |
| Education: graduate level (vs college) | -0.4976 | 1.0618 | ±2.1237 | -0.469 | 0.6393 |  |
| Education: high school or below (vs college) | -0.4540 | 1.4117 | ±2.8234 | -0.322 | 0.7478 |  |
| **Site: UCSD (vs UAB)** | **+3.7867** | 1.1604 | ±2.3207 | **+3.263** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8172 | 1.0106 | ±2.0211 | -0.809 | 0.4187 |  |
| Season: spring (vs autumn) | -1.4282 | 1.2112 | ±2.4225 | -1.179 | 0.2383 |  |
| Season: summer (vs autumn) | +1.5996 | 1.1584 | ±2.3168 | +1.381 | 0.1673 |  |
| **Season: winter (vs autumn)** | **-6.0311** | 1.5294 | ±3.0589 | **-3.943** | **8.03e-05** | *** |
| Age (years) | -0.0679 | 0.0410 | ±0.0820 | -1.658 | 0.0973 | . |
| BMI (kg/m2) | +0.0238 | 0.0738 | ±0.1475 | +0.322 | 0.7473 |  |
| Hypertension | +0.5164 | 1.1614 | ±2.3228 | +0.445 | 0.6566 |  |
| High cholesterol | -0.2072 | 0.9961 | ±1.9922 | -0.208 | 0.8353 |  |
| Kidney disease | +0.5416 | 1.2414 | ±2.4829 | +0.436 | 0.6626 |  |
| Circulatory disease | +0.1429 | 1.0705 | ±2.1410 | +0.134 | 0.8938 |  |
| Time in range 70-180, pooled (%) | -0.0327 | 0.0256 | ±0.0512 | -1.279 | 0.2010 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.1926**, Adj R² = **0.1396**, F-statistic = **3.63** (p = **2.05e-05**), Residual SE = **6.669** on **213** df, AIC = **1526.7**, BIC = **1578.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3523** | 4.2898 | ±8.5797 | **+11.971** | **5.06e-33** | *** |
| Education: graduate level (vs college) | -0.5005 | 1.0622 | ±2.1244 | -0.471 | 0.6375 |  |
| Education: high school or below (vs college) | -0.4658 | 1.4137 | ±2.8275 | -0.329 | 0.7418 |  |
| **Site: UCSD (vs UAB)** | **+3.7923** | 1.1622 | ±2.3244 | **+3.263** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8128 | 1.0099 | ±2.0197 | -0.805 | 0.4209 |  |
| Season: spring (vs autumn) | -1.4362 | 1.2133 | ±2.4266 | -1.184 | 0.2365 |  |
| Season: summer (vs autumn) | +1.5854 | 1.1595 | ±2.3189 | +1.367 | 0.1715 |  |
| **Season: winter (vs autumn)** | **-6.0475** | 1.5363 | ±3.0725 | **-3.936** | **8.27e-05** | *** |
| Age (years) | -0.0680 | 0.0410 | ±0.0821 | -1.656 | 0.0977 | . |
| BMI (kg/m2) | +0.0242 | 0.0739 | ±0.1477 | +0.328 | 0.7432 |  |
| Hypertension | +0.5243 | 1.1614 | ±2.3227 | +0.451 | 0.6517 |  |
| High cholesterol | -0.2087 | 0.9964 | ±1.9929 | -0.209 | 0.8341 |  |
| Kidney disease | +0.5340 | 1.2400 | ±2.4800 | +0.431 | 0.6667 |  |
| Circulatory disease | +0.1431 | 1.0717 | ±2.1433 | +0.134 | 0.8938 |  |
| Avg. daily time in range 70-180 (%) | -0.0323 | 0.0262 | ±0.0525 | -1.231 | 0.2185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1884**, Adj R² = **0.1351**, F-statistic = **3.53** (p = **3.15e-05**), Residual SE = **6.686** on **213** df, AIC = **1527.9**, BIC = **1579.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6749** | 3.8569 | ±7.7138 | **+12.620** | **1.63e-36** | *** |
| Education: graduate level (vs college) | -0.7009 | 1.0563 | ±2.1126 | -0.664 | 0.5070 |  |
| Education: high school or below (vs college) | -0.3850 | 1.4065 | ±2.8130 | -0.274 | 0.7843 |  |
| **Site: UCSD (vs UAB)** | **+3.6423** | 1.1728 | ±2.3457 | **+3.106** | **0.0019** | ** |
| Site: UW (vs UAB) | -1.0220 | 1.0337 | ±2.0673 | -0.989 | 0.3228 |  |
| Season: spring (vs autumn) | -1.3571 | 1.2191 | ±2.4382 | -1.113 | 0.2656 |  |
| Season: summer (vs autumn) | +1.5448 | 1.1974 | ±2.3947 | +1.290 | 0.1970 |  |
| **Season: winter (vs autumn)** | **-5.8633** | 1.5195 | ±3.0391 | **-3.859** | **1.14e-04** | *** |
| Age (years) | -0.0637 | 0.0412 | ±0.0824 | -1.547 | 0.1219 |  |
| BMI (kg/m2) | +0.0206 | 0.0734 | ±0.1469 | +0.281 | 0.7787 |  |
| Hypertension | +0.5382 | 1.1643 | ±2.3285 | +0.462 | 0.6439 |  |
| High cholesterol | -0.1945 | 0.9919 | ±1.9838 | -0.196 | 0.8445 |  |
| Kidney disease | +0.7852 | 1.2602 | ±2.5204 | +0.623 | 0.5332 |  |
| Circulatory disease | +0.2870 | 1.0657 | ±2.1313 | +0.269 | 0.7877 |  |
| Time < 54 (%) | -0.4329 | 1.0072 | ±2.0144 | -0.430 | 0.6674 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.1889**, Adj R² = **0.1356**, F-statistic = **3.54** (p = **3.00e-05**), Residual SE = **6.684** on **213** df, AIC = **1527.8**, BIC = **1579.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5717** | 3.8185 | ±7.6370 | **+12.720** | **4.57e-37** | *** |
| Education: graduate level (vs college) | -0.7253 | 1.0575 | ±2.1150 | -0.686 | 0.4928 |  |
| Education: high school or below (vs college) | -0.3880 | 1.4037 | ±2.8075 | -0.276 | 0.7822 |  |
| **Site: UCSD (vs UAB)** | **+3.6496** | 1.1610 | ±2.3221 | **+3.143** | **0.0017** | ** |
| Site: UW (vs UAB) | -1.0000 | 1.0237 | ±2.0475 | -0.977 | 0.3287 |  |
| Season: spring (vs autumn) | -1.3839 | 1.2177 | ±2.4354 | -1.137 | 0.2557 |  |
| Season: summer (vs autumn) | +1.5459 | 1.1847 | ±2.3695 | +1.305 | 0.1919 |  |
| **Season: winter (vs autumn)** | **-5.8520** | 1.5136 | ±3.0273 | **-3.866** | **1.11e-04** | *** |
| Age (years) | -0.0620 | 0.0412 | ±0.0825 | -1.502 | 0.1330 |  |
| BMI (kg/m2) | +0.0201 | 0.0725 | ±0.1449 | +0.277 | 0.7818 |  |
| Hypertension | +0.5258 | 1.1648 | ±2.3296 | +0.451 | 0.6517 |  |
| High cholesterol | -0.2222 | 0.9948 | ±1.9896 | -0.223 | 0.8233 |  |
| Kidney disease | +0.8149 | 1.2614 | ±2.5229 | +0.646 | 0.5183 |  |
| Circulatory disease | +0.2863 | 1.0629 | ±2.1258 | +0.269 | 0.7877 |  |
| Avg. daily time < 54 (%) | -0.4418 | 0.7535 | ±1.5069 | -0.586 | 0.5577 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1331**, F-statistic = **3.49** (p = **3.79e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.5**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5169** | 3.8530 | ±7.7060 | **+12.592** | **2.34e-36** | *** |
| Education: graduate level (vs college) | -0.6761 | 1.0612 | ±2.1224 | -0.637 | 0.5241 |  |
| Education: high school or below (vs college) | -0.3196 | 1.4211 | ±2.8422 | -0.225 | 0.8221 |  |
| **Site: UCSD (vs UAB)** | **+3.7452** | 1.1685 | ±2.3370 | **+3.205** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8951 | 1.0149 | ±2.0299 | -0.882 | 0.3778 |  |
| Season: spring (vs autumn) | -1.3109 | 1.2071 | ±2.4142 | -1.086 | 0.2775 |  |
| Season: summer (vs autumn) | +1.5543 | 1.1710 | ±2.3420 | +1.327 | 0.1844 |  |
| **Season: winter (vs autumn)** | **-5.8480** | 1.5208 | ±3.0417 | **-3.845** | **1.20e-04** | *** |
| Age (years) | -0.0640 | 0.0417 | ±0.0835 | -1.533 | 0.1253 |  |
| BMI (kg/m2) | +0.0197 | 0.0732 | ±0.1463 | +0.269 | 0.7878 |  |
| Hypertension | +0.5188 | 1.1691 | ±2.3382 | +0.444 | 0.6572 |  |
| High cholesterol | -0.2059 | 0.9950 | ±1.9900 | -0.207 | 0.8360 |  |
| Kidney disease | +0.8132 | 1.2633 | ±2.5265 | +0.644 | 0.5198 |  |
| Circulatory disease | +0.2238 | 1.0672 | ±2.1343 | +0.210 | 0.8339 |  |
| Time 54-69, pooled (%) | -0.0179 | 0.2101 | ±0.4202 | -0.085 | 0.9321 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.1868**, Adj R² = **0.1334**, F-statistic = **3.50** (p = **3.69e-05**), Residual SE = **6.693** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5039** | 3.8415 | ±7.6831 | **+12.626** | **1.52e-36** | *** |
| Education: graduate level (vs college) | -0.7045 | 1.0626 | ±2.1253 | -0.663 | 0.5073 |  |
| Education: high school or below (vs college) | -0.3070 | 1.4226 | ±2.8451 | -0.216 | 0.8291 |  |
| **Site: UCSD (vs UAB)** | **+3.7325** | 1.1677 | ±2.3354 | **+3.197** | **0.0014** | ** |
| Site: UW (vs UAB) | -0.9058 | 1.0158 | ±2.0316 | -0.892 | 0.3726 |  |
| Season: spring (vs autumn) | -1.3319 | 1.2095 | ±2.4190 | -1.101 | 0.2708 |  |
| Season: summer (vs autumn) | +1.5502 | 1.1702 | ±2.3405 | +1.325 | 0.1853 |  |
| **Season: winter (vs autumn)** | **-5.8544** | 1.5218 | ±3.0436 | **-3.847** | **1.20e-04** | *** |
| Age (years) | -0.0626 | 0.0418 | ±0.0835 | -1.498 | 0.1342 |  |
| BMI (kg/m2) | +0.0197 | 0.0730 | ±0.1460 | +0.269 | 0.7878 |  |
| Hypertension | +0.5099 | 1.1669 | ±2.3338 | +0.437 | 0.6622 |  |
| High cholesterol | -0.1966 | 0.9945 | ±1.9890 | -0.198 | 0.8433 |  |
| Kidney disease | +0.8181 | 1.2604 | ±2.5208 | +0.649 | 0.5163 |  |
| Circulatory disease | +0.2218 | 1.0675 | ±2.1350 | +0.208 | 0.8354 |  |
| Avg. daily time 54-69 (%) | -0.0498 | 0.1964 | ±0.3928 | -0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.1868**, Adj R² = **0.1333**, F-statistic = **3.49** (p = **3.71e-05**), Residual SE = **6.693** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5400** | 3.8518 | ±7.7035 | **+12.602** | **2.06e-36** | *** |
| Education: graduate level (vs college) | -0.6965 | 1.0604 | ±2.1207 | -0.657 | 0.5113 |  |
| Education: high school or below (vs college) | -0.3201 | 1.4138 | ±2.8276 | -0.226 | 0.8209 |  |
| **Site: UCSD (vs UAB)** | **+3.7274** | 1.1704 | ±2.3408 | **+3.185** | **0.0014** | ** |
| Site: UW (vs UAB) | -0.9126 | 1.0144 | ±2.0288 | -0.900 | 0.3683 |  |
| Season: spring (vs autumn) | -1.3300 | 1.2090 | ±2.4180 | -1.100 | 0.2713 |  |
| Season: summer (vs autumn) | +1.5479 | 1.1697 | ±2.3393 | +1.323 | 0.1857 |  |
| **Season: winter (vs autumn)** | **-5.8554** | 1.5226 | ±3.0452 | **-3.846** | **1.20e-04** | *** |
| Age (years) | -0.0632 | 0.0416 | ±0.0832 | -1.519 | 0.1288 |  |
| BMI (kg/m2) | +0.0197 | 0.0733 | ±0.1466 | +0.269 | 0.7882 |  |
| Hypertension | +0.5153 | 1.1685 | ±2.3370 | +0.441 | 0.6592 |  |
| High cholesterol | -0.1971 | 0.9931 | ±1.9863 | -0.199 | 0.8427 |  |
| Kidney disease | +0.8152 | 1.2622 | ±2.5243 | +0.646 | 0.5183 |  |
| Circulatory disease | +0.2304 | 1.0663 | ±2.1326 | +0.216 | 0.8289 |  |
| Time < 70 (%) | -0.0384 | 0.1703 | ±0.3407 | -0.225 | 0.8217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.1873**, Adj R² = **0.1338**, F-statistic = **3.51** (p = **3.54e-05**), Residual SE = **6.691** on **213** df, AIC = **1528.3**, BIC = **1579.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5113** | 3.8350 | ±7.6700 | **+12.650** | **1.12e-36** | *** |
| Education: graduate level (vs college) | -0.7243 | 1.0605 | ±2.1210 | -0.683 | 0.4946 |  |
| Education: high school or below (vs college) | -0.3118 | 1.4142 | ±2.8285 | -0.220 | 0.8255 |  |
| **Site: UCSD (vs UAB)** | **+3.7131** | 1.1674 | ±2.3347 | **+3.181** | **0.0015** | ** |
| Site: UW (vs UAB) | -0.9252 | 1.0162 | ±2.0324 | -0.910 | 0.3626 |  |
| Season: spring (vs autumn) | -1.3522 | 1.2111 | ±2.4221 | -1.117 | 0.2642 |  |
| Season: summer (vs autumn) | +1.5462 | 1.1694 | ±2.3387 | +1.322 | 0.1861 |  |
| **Season: winter (vs autumn)** | **-5.8585** | 1.5218 | ±3.0436 | **-3.850** | **1.18e-04** | *** |
| Age (years) | -0.0617 | 0.0416 | ±0.0832 | -1.483 | 0.1381 |  |
| BMI (kg/m2) | +0.0197 | 0.0729 | ±0.1459 | +0.270 | 0.7874 |  |
| Hypertension | +0.5069 | 1.1652 | ±2.3304 | +0.435 | 0.6635 |  |
| High cholesterol | -0.1940 | 0.9930 | ±1.9860 | -0.195 | 0.8451 |  |
| Kidney disease | +0.8210 | 1.2597 | ±2.5194 | +0.652 | 0.5146 |  |
| Circulatory disease | +0.2305 | 1.0653 | ±2.1306 | +0.216 | 0.8287 |  |
| Avg. daily time < 70 (%) | -0.0622 | 0.1547 | ±0.3095 | -0.402 | 0.6877 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1887**, Adj R² = **0.1354**, F-statistic = **3.54** (p = **3.05e-05**), Residual SE = **6.685** on **213** df, AIC = **1527.9**, BIC = **1579.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0298** | 5.1471 | ±10.2942 | **+10.109** | **5.06e-24** | *** |
| Education: graduate level (vs college) | -0.5935 | 1.0565 | ±2.1130 | -0.562 | 0.5743 |  |
| Education: high school or below (vs college) | -0.4152 | 1.4138 | ±2.8275 | -0.294 | 0.7690 |  |
| **Site: UCSD (vs UAB)** | **+3.7714** | 1.1570 | ±2.3141 | **+3.260** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8115 | 1.0240 | ±2.0481 | -0.792 | 0.4281 |  |
| Season: spring (vs autumn) | -1.3498 | 1.2107 | ±2.4215 | -1.115 | 0.2649 |  |
| Season: summer (vs autumn) | +1.6493 | 1.1662 | ±2.3324 | +1.414 | 0.1573 |  |
| **Season: winter (vs autumn)** | **-5.8769** | 1.5111 | ±3.0222 | **-3.889** | **1.01e-04** | *** |
| Age (years) | -0.0636 | 0.0413 | ±0.0826 | -1.539 | 0.1237 |  |
| BMI (kg/m2) | +0.0223 | 0.0733 | ±0.1467 | +0.304 | 0.7613 |  |
| Hypertension | +0.4852 | 1.1683 | ±2.3366 | +0.415 | 0.6779 |  |
| High cholesterol | -0.1568 | 1.0069 | ±2.0137 | -0.156 | 0.8762 |  |
| Kidney disease | +0.7429 | 1.2482 | ±2.4965 | +0.595 | 0.5517 |  |
| Circulatory disease | +0.1710 | 1.0750 | ±2.1501 | +0.159 | 0.8736 |  |
| Time 54-250, pooled (%) | -0.0382 | 0.0420 | ±0.0841 | -0.908 | 0.3638 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1894**, Adj R² = **0.1361**, F-statistic = **3.55** (p = **2.86e-05**), Residual SE = **6.682** on **213** df, AIC = **1527.7**, BIC = **1579.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0256** | 6.0110 | ±12.0220 | **+8.821** | **1.13e-18** | *** |
| Education: graduate level (vs college) | -0.5780 | 1.0566 | ±2.1132 | -0.547 | 0.5844 |  |
| Education: high school or below (vs college) | -0.4472 | 1.4166 | ±2.8332 | -0.316 | 0.7522 |  |
| **Site: UCSD (vs UAB)** | **+3.7670** | 1.1562 | ±2.3124 | **+3.258** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8125 | 1.0218 | ±2.0435 | -0.795 | 0.4265 |  |
| Season: spring (vs autumn) | -1.3831 | 1.2158 | ±2.4316 | -1.138 | 0.2553 |  |
| Season: summer (vs autumn) | +1.6454 | 1.1640 | ±2.3279 | +1.414 | 0.1575 |  |
| **Season: winter (vs autumn)** | **-5.9116** | 1.5179 | ±3.0359 | **-3.894** | **9.84e-05** | *** |
| Age (years) | -0.0640 | 0.0413 | ±0.0825 | -1.551 | 0.1209 |  |
| BMI (kg/m2) | +0.0235 | 0.0736 | ±0.1472 | +0.319 | 0.7496 |  |
| Hypertension | +0.4781 | 1.1683 | ±2.3365 | +0.409 | 0.6824 |  |
| High cholesterol | -0.1483 | 1.0070 | ±2.0141 | -0.147 | 0.8829 |  |
| Kidney disease | +0.7111 | 1.2478 | ±2.4956 | +0.570 | 0.5687 |  |
| Circulatory disease | +0.1479 | 1.0818 | ±2.1635 | +0.137 | 0.8913 |  |
| Avg. daily time 54-250 (%) | -0.0482 | 0.0526 | ±0.1053 | -0.915 | 0.3600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1935**, Adj R² = **0.1405**, F-statistic = **3.65** (p = **1.87e-05**), Residual SE = **6.665** on **213** df, AIC = **1526.5**, BIC = **1577.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3093** | 3.8628 | ±7.7256 | **+12.506** | **6.90e-36** | *** |
| Education: graduate level (vs college) | -0.5387 | 1.0588 | ±2.1176 | -0.509 | 0.6109 |  |
| Education: high school or below (vs college) | -0.3924 | 1.4014 | ±2.8028 | -0.280 | 0.7794 |  |
| **Site: UCSD (vs UAB)** | **+3.7603** | 1.1626 | ±2.3252 | **+3.234** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8960 | 1.0041 | ±2.0081 | -0.892 | 0.3722 |  |
| Season: spring (vs autumn) | -1.4673 | 1.2095 | ±2.4191 | -1.213 | 0.2251 |  |
| Season: summer (vs autumn) | +1.4884 | 1.1638 | ±2.3277 | +1.279 | 0.2009 |  |
| **Season: winter (vs autumn)** | **-6.1055** | 1.5484 | ±3.0968 | **-3.943** | **8.04e-05** | *** |
| Age (years) | -0.0695 | 0.0408 | ±0.0817 | -1.701 | 0.0890 | . |
| BMI (kg/m2) | +0.0224 | 0.0737 | ±0.1475 | +0.304 | 0.7609 |  |
| Hypertension | +0.5512 | 1.1617 | ±2.3234 | +0.474 | 0.6352 |  |
| High cholesterol | -0.2605 | 0.9970 | ±1.9940 | -0.261 | 0.7939 |  |
| Kidney disease | +0.4908 | 1.2478 | ±2.4957 | +0.393 | 0.6941 |  |
| Circulatory disease | +0.1700 | 1.0638 | ±2.1276 | +0.160 | 0.8731 |  |
| Time 181-250, pooled (%) | +0.0511 | 0.0410 | ±0.0820 | +1.248 | 0.2119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.1931**, Adj R² = **0.1401**, F-statistic = **3.64** (p = **1.95e-05**), Residual SE = **6.667** on **213** df, AIC = **1526.6**, BIC = **1578.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2326** | 3.8718 | ±7.7436 | **+12.457** | **1.28e-35** | *** |
| Education: graduate level (vs college) | -0.5467 | 1.0586 | ±2.1171 | -0.516 | 0.6056 |  |
| Education: high school or below (vs college) | -0.3958 | 1.4037 | ±2.8075 | -0.282 | 0.7780 |  |
| **Site: UCSD (vs UAB)** | **+3.7781** | 1.1658 | ±2.3316 | **+3.241** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8675 | 1.0042 | ±2.0083 | -0.864 | 0.3877 |  |
| Season: spring (vs autumn) | -1.4514 | 1.2094 | ±2.4187 | -1.200 | 0.2301 |  |
| Season: summer (vs autumn) | +1.5037 | 1.1631 | ±2.3263 | +1.293 | 0.1961 |  |
| **Season: winter (vs autumn)** | **-6.0901** | 1.5474 | ±3.0948 | **-3.936** | **8.30e-05** | *** |
| Age (years) | -0.0682 | 0.0408 | ±0.0816 | -1.672 | 0.0946 | . |
| BMI (kg/m2) | +0.0225 | 0.0737 | ±0.1474 | +0.306 | 0.7597 |  |
| Hypertension | +0.5570 | 1.1627 | ±2.3254 | +0.479 | 0.6319 |  |
| High cholesterol | -0.2557 | 0.9968 | ±1.9936 | -0.256 | 0.7976 |  |
| Kidney disease | +0.5057 | 1.2457 | ±2.4915 | +0.406 | 0.6848 |  |
| Circulatory disease | +0.1778 | 1.0633 | ±2.1267 | +0.167 | 0.8672 |  |
| Avg. daily time 181-250 (%) | +0.0481 | 0.0397 | ±0.0794 | +1.211 | 0.2260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.1930**, Adj R² = **0.1399**, F-statistic = **3.64** (p = **1.98e-05**), Residual SE = **6.667** on **213** df, AIC = **1526.7**, BIC = **1578.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1406** | 3.8884 | ±7.7769 | **+12.380** | **3.33e-35** | *** |
| Education: graduate level (vs college) | -0.5283 | 1.0585 | ±2.1170 | -0.499 | 0.6177 |  |
| Education: high school or below (vs college) | -0.4501 | 1.4074 | ±2.8147 | -0.320 | 0.7491 |  |
| **Site: UCSD (vs UAB)** | **+3.7654** | 1.1573 | ±2.3147 | **+3.254** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8367 | 1.0106 | ±2.0213 | -0.828 | 0.4077 |  |
| Season: spring (vs autumn) | -1.4541 | 1.2118 | ±2.4236 | -1.200 | 0.2302 |  |
| Season: summer (vs autumn) | +1.5901 | 1.1581 | ±2.3162 | +1.373 | 0.1697 |  |
| **Season: winter (vs autumn)** | **-6.0406** | 1.5337 | ±3.0675 | **-3.938** | **8.20e-05** | *** |
| Age (years) | -0.0668 | 0.0409 | ±0.0818 | -1.633 | 0.1024 |  |
| BMI (kg/m2) | +0.0237 | 0.0738 | ±0.1476 | +0.321 | 0.7483 |  |
| Hypertension | +0.5098 | 1.1597 | ±2.3195 | +0.440 | 0.6603 |  |
| High cholesterol | -0.1943 | 0.9970 | ±1.9940 | -0.195 | 0.8454 |  |
| Kidney disease | +0.5479 | 1.2410 | ±2.4820 | +0.441 | 0.6589 |  |
| Circulatory disease | +0.1497 | 1.0703 | ±2.1406 | +0.140 | 0.8888 |  |
| Time > 180 (%) | +0.0326 | 0.0252 | ±0.0505 | +1.290 | 0.1969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1932**, Adj R² = **0.1402**, F-statistic = **3.64** (p = **1.93e-05**), Residual SE = **6.666** on **213** df, AIC = **1526.6**, BIC = **1578.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1118** | 3.8899 | ±7.7798 | **+12.368** | **3.87e-35** | *** |
| Education: graduate level (vs college) | -0.5288 | 1.0580 | ±2.1161 | -0.500 | 0.6173 |  |
| Education: high school or below (vs college) | -0.4642 | 1.4086 | ±2.8173 | -0.330 | 0.7417 |  |
| **Site: UCSD (vs UAB)** | **+3.7727** | 1.1592 | ±2.3184 | **+3.255** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8289 | 1.0093 | ±2.0185 | -0.821 | 0.4115 |  |
| Season: spring (vs autumn) | -1.4697 | 1.2143 | ±2.4286 | -1.210 | 0.2261 |  |
| Season: summer (vs autumn) | +1.5796 | 1.1585 | ±2.3170 | +1.363 | 0.1727 |  |
| **Season: winter (vs autumn)** | **-6.0628** | 1.5406 | ±3.0812 | **-3.935** | **8.31e-05** | *** |
| Age (years) | -0.0665 | 0.0409 | ±0.0818 | -1.626 | 0.1039 |  |
| BMI (kg/m2) | +0.0243 | 0.0738 | ±0.1476 | +0.329 | 0.7421 |  |
| Hypertension | +0.5157 | 1.1592 | ±2.3183 | +0.445 | 0.6564 |  |
| High cholesterol | -0.1988 | 0.9971 | ±1.9941 | -0.199 | 0.8419 |  |
| Kidney disease | +0.5307 | 1.2406 | ±2.4813 | +0.428 | 0.6688 |  |
| Circulatory disease | +0.1443 | 1.0712 | ±2.1423 | +0.135 | 0.8928 |  |
| Avg. daily time > 180 (%) | +0.0334 | 0.0261 | ±0.0522 | +1.281 | 0.2003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1331**, F-statistic = **3.49** (p = **3.79e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.5**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4811** | 3.8838 | ±7.7677 | **+12.483** | **9.27e-36** | *** |
| Education: graduate level (vs college) | -0.6520 | 1.0621 | ±2.1243 | -0.614 | 0.5393 |  |
| Education: high school or below (vs college) | -0.3295 | 1.4137 | ±2.8275 | -0.233 | 0.8157 |  |
| **Site: UCSD (vs UAB)** | **+3.7542** | 1.1653 | ±2.3306 | **+3.222** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8859 | 1.0222 | ±2.0445 | -0.867 | 0.3862 |  |
| Season: spring (vs autumn) | -1.3088 | 1.2150 | ±2.4300 | -1.077 | 0.2814 |  |
| Season: summer (vs autumn) | +1.5670 | 1.1615 | ±2.3230 | +1.349 | 0.1773 |  |
| **Season: winter (vs autumn)** | **-5.8580** | 1.5419 | ±3.0839 | **-3.799** | **1.45e-04** | *** |
| Age (years) | -0.0645 | 0.0413 | ±0.0826 | -1.562 | 0.1182 |  |
| BMI (kg/m2) | +0.0200 | 0.0732 | ±0.1463 | +0.273 | 0.7848 |  |
| Hypertension | +0.5173 | 1.1663 | ±2.3326 | +0.444 | 0.6574 |  |
| High cholesterol | -0.2141 | 0.9934 | ±1.9867 | -0.215 | 0.8294 |  |
| Kidney disease | +0.8013 | 1.2534 | ±2.5069 | +0.639 | 0.5226 |  |
| Circulatory disease | +0.2143 | 1.0817 | ±2.1633 | +0.198 | 0.8429 |  |
| Nocturnal time > 180 (%) | +0.0026 | 0.0254 | ±0.0508 | +0.102 | 0.9184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1332**, F-statistic = **3.49** (p = **3.77e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.4**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4731** | 3.8990 | ±7.7979 | **+12.432** | **1.75e-35** | *** |
| Education: graduate level (vs college) | -0.6437 | 1.0608 | ±2.1217 | -0.607 | 0.5440 |  |
| Education: high school or below (vs college) | -0.3389 | 1.4222 | ±2.8444 | -0.238 | 0.8117 |  |
| **Site: UCSD (vs UAB)** | **+3.7539** | 1.1648 | ±2.3296 | **+3.223** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.9019 | 1.0163 | ±2.0327 | -0.887 | 0.3748 |  |
| Season: spring (vs autumn) | -1.3116 | 1.2174 | ±2.4347 | -1.077 | 0.2813 |  |
| Season: summer (vs autumn) | +1.5487 | 1.1729 | ±2.3458 | +1.320 | 0.1867 |  |
| **Season: winter (vs autumn)** | **-5.8458** | 1.5138 | ±3.0276 | **-3.862** | **1.13e-04** | *** |
| Age (years) | -0.0657 | 0.0410 | ±0.0820 | -1.602 | 0.1092 |  |
| BMI (kg/m2) | +0.0209 | 0.0742 | ±0.1483 | +0.281 | 0.7784 |  |
| Hypertension | +0.5207 | 1.1686 | ±2.3373 | +0.446 | 0.6559 |  |
| High cholesterol | -0.2059 | 0.9953 | ±1.9906 | -0.207 | 0.8361 |  |
| Kidney disease | +0.7713 | 1.2592 | ±2.5184 | +0.613 | 0.5402 |  |
| Circulatory disease | +0.2195 | 1.0673 | ±2.1346 | +0.206 | 0.8371 |  |
| Any reading > 250 during wear (0/1) | +0.1460 | 0.9490 | ±1.8980 | +0.154 | 0.8777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1891**, Adj R² = **0.1358**, F-statistic = **3.55** (p = **2.94e-05**), Residual SE = **6.683** on **213** df, AIC = **1527.7**, BIC = **1579.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2016** | 3.8912 | ±7.7823 | **+12.387** | **3.06e-35** | *** |
| Education: graduate level (vs college) | -0.5912 | 1.0553 | ±2.1107 | -0.560 | 0.5753 |  |
| Education: high school or below (vs college) | -0.4292 | 1.4136 | ±2.8272 | -0.304 | 0.7614 |  |
| **Site: UCSD (vs UAB)** | **+3.7625** | 1.1553 | ±2.3106 | **+3.257** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8172 | 1.0225 | ±2.0451 | -0.799 | 0.4242 |  |
| Season: spring (vs autumn) | -1.3600 | 1.2114 | ±2.4229 | -1.123 | 0.2616 |  |
| Season: summer (vs autumn) | +1.6560 | 1.1670 | ±2.3340 | +1.419 | 0.1559 |  |
| **Season: winter (vs autumn)** | **-5.8818** | 1.5118 | ±3.0236 | **-3.891** | **1.00e-04** | *** |
| Age (years) | -0.0634 | 0.0413 | ±0.0826 | -1.535 | 0.1247 |  |
| BMI (kg/m2) | +0.0226 | 0.0733 | ±0.1467 | +0.308 | 0.7581 |  |
| Hypertension | +0.4833 | 1.1677 | ±2.3355 | +0.414 | 0.6790 |  |
| High cholesterol | -0.1502 | 1.0073 | ±2.0147 | -0.149 | 0.8815 |  |
| Kidney disease | +0.7347 | 1.2481 | ±2.4961 | +0.589 | 0.5561 |  |
| Circulatory disease | +0.1725 | 1.0743 | ±2.1485 | +0.161 | 0.8724 |  |
| Time > 250 (%) | +0.0416 | 0.0433 | ±0.0865 | +0.961 | 0.3367 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1900**, Adj R² = **0.1367**, F-statistic = **3.57** (p = **2.69e-05**), Residual SE = **6.680** on **213** df, AIC = **1527.5**, BIC = **1578.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1781** | 3.8850 | ±7.7700 | **+12.401** | **2.58e-35** | *** |
| Education: graduate level (vs college) | -0.5759 | 1.0552 | ±2.1105 | -0.546 | 0.5852 |  |
| Education: high school or below (vs college) | -0.4697 | 1.4171 | ±2.8342 | -0.331 | 0.7403 |  |
| **Site: UCSD (vs UAB)** | **+3.7562** | 1.1547 | ±2.3094 | **+3.253** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8167 | 1.0200 | ±2.0400 | -0.801 | 0.4233 |  |
| Season: spring (vs autumn) | -1.4036 | 1.2175 | ±2.4350 | -1.153 | 0.2490 |  |
| Season: summer (vs autumn) | +1.6542 | 1.1634 | ±2.3267 | +1.422 | 0.1551 |  |
| **Season: winter (vs autumn)** | **-5.9208** | 1.5191 | ±3.0381 | **-3.898** | **9.71e-05** | *** |
| Age (years) | -0.0636 | 0.0413 | ±0.0825 | -1.542 | 0.1231 |  |
| BMI (kg/m2) | +0.0240 | 0.0735 | ±0.1470 | +0.326 | 0.7444 |  |
| Hypertension | +0.4730 | 1.1669 | ±2.3338 | +0.405 | 0.6852 |  |
| High cholesterol | -0.1419 | 1.0071 | ±2.0143 | -0.141 | 0.8880 |  |
| Kidney disease | +0.7001 | 1.2487 | ±2.4973 | +0.561 | 0.5750 |  |
| Circulatory disease | +0.1467 | 1.0807 | ±2.1613 | +0.136 | 0.8921 |  |
| Avg. daily time > 250 (%) | +0.0539 | 0.0553 | ±0.1105 | +0.976 | 0.3293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.1054**, Adj R² = **0.0511**, F-statistic = **1.94** (p = **0.0273**), Residual SE = **19.089** on **214** df, AIC = **2005.4**, BIC = **2053.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9682** | 13.2243 | ±26.4486 | **+9.450** | **3.39e-21** | *** |
| **Education: graduate level (vs college)** | **-9.4747** | 2.9636 | ±5.9272 | **-3.197** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.3253 | 3.8884 | ±7.7768 | +0.341 | 0.7332 |  |
| Site: UCSD (vs UAB) | +1.7175 | 3.5086 | ±7.0171 | +0.490 | 0.6245 |  |
| Site: UW (vs UAB) | +0.4106 | 2.9515 | ±5.9029 | +0.139 | 0.8894 |  |
| Season: spring (vs autumn) | +3.0557 | 3.4063 | ±6.8126 | +0.897 | 0.3697 |  |
| Season: summer (vs autumn) | +1.8966 | 3.4814 | ±6.9629 | +0.545 | 0.5859 |  |
| **Season: winter (vs autumn)** | **+10.0481** | 4.7962 | ±9.5924 | **+2.095** | **0.0362** | * |
| Age (years) | -0.0502 | 0.1244 | ±0.2487 | -0.404 | 0.6862 |  |
| BMI (kg/m2) | +0.1719 | 0.1842 | ±0.3683 | +0.933 | 0.3507 |  |
| Hypertension | -2.5776 | 3.2962 | ±6.5925 | -0.782 | 0.4342 |  |
| High cholesterol | +2.4388 | 3.1116 | ±6.2232 | +0.784 | 0.4332 |  |
| Kidney disease | +1.5802 | 3.8039 | ±7.6078 | +0.415 | 0.6778 |  |
| Circulatory disease | -4.1215 | 3.5007 | ±7.0015 | -1.177 | 0.2391 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.1167**, Adj R² = **0.0587**, F-statistic = **2.01** (p = **0.0183**), Residual SE = **19.012** on **213** df, AIC = **2004.5**, BIC = **2055.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4781** | 11.7793 | ±23.5585 | **+11.501** | **1.30e-30** | *** |
| **Education: graduate level (vs college)** | **-10.1066** | 2.8675 | ±5.7351 | **-3.524** | **4.24e-04** | *** |
| Education: high school or below (vs college) | +1.8658 | 3.9142 | ±7.8284 | +0.477 | 0.6336 |  |
| Site: UCSD (vs UAB) | +1.6489 | 3.4836 | ±6.9672 | +0.473 | 0.6360 |  |
| Site: UW (vs UAB) | +0.2041 | 2.9938 | ±5.9876 | +0.068 | 0.9456 |  |
| Season: spring (vs autumn) | +3.4482 | 3.4198 | ±6.8396 | +1.008 | 0.3133 |  |
| Season: summer (vs autumn) | +1.7109 | 3.4664 | ±6.9329 | +0.494 | 0.6216 |  |
| **Season: winter (vs autumn)** | **+10.3500** | 4.6956 | ±9.3911 | **+2.204** | **0.0275** | * |
| Age (years) | -0.0215 | 0.1460 | ±0.2920 | -0.147 | 0.8828 |  |
| BMI (kg/m2) | +0.1770 | 0.1870 | ±0.3741 | +0.946 | 0.3440 |  |
| Hypertension | -2.2897 | 3.3986 | ±6.7972 | -0.674 | 0.5005 |  |
| High cholesterol | +2.1579 | 3.1495 | ±6.2990 | +0.685 | 0.4932 |  |
| Kidney disease | +1.7718 | 3.7054 | ±7.4107 | +0.478 | 0.6325 |  |
| Circulatory disease | -4.0807 | 3.4409 | ±6.8819 | -1.186 | 0.2356 |  |
| HbA1c (%) | -1.9352 | 1.9902 | ±3.9804 | -0.972 | 0.3309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.1107**, Adj R² = **0.0522**, F-statistic = **1.89** (p = **0.0285**), Residual SE = **19.077** on **213** df, AIC = **2006.0**, BIC = **2057.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.0482** | 11.9762 | ±23.9524 | **+10.942** | **7.23e-28** | *** |
| **Education: graduate level (vs college)** | **-9.6263** | 2.9324 | ±5.8648 | **-3.283** | **0.0010** | ** |
| Education: high school or below (vs college) | +1.6342 | 4.0412 | ±8.0824 | +0.404 | 0.6859 |  |
| Site: UCSD (vs UAB) | +1.7172 | 3.5463 | ±7.0927 | +0.484 | 0.6282 |  |
| Site: UW (vs UAB) | +0.3147 | 2.9743 | ±5.9486 | +0.106 | 0.9157 |  |
| Season: spring (vs autumn) | +3.5887 | 3.4924 | ±6.9848 | +1.028 | 0.3041 |  |
| Season: summer (vs autumn) | +1.9224 | 3.5125 | ±7.0249 | +0.547 | 0.5842 |  |
| **Season: winter (vs autumn)** | **+10.4681** | 4.5953 | ±9.1906 | **+2.278** | **0.0227** | * |
| Age (years) | -0.0494 | 0.1278 | ±0.2556 | -0.386 | 0.6991 |  |
| BMI (kg/m2) | +0.1678 | 0.1840 | ±0.3679 | +0.912 | 0.3618 |  |
| Hypertension | -2.4678 | 3.3716 | ±6.7433 | -0.732 | 0.4642 |  |
| High cholesterol | +2.2878 | 3.1482 | ±6.2965 | +0.727 | 0.4674 |  |
| Kidney disease | +2.0103 | 3.7746 | ±7.5492 | +0.533 | 0.5943 |  |
| Circulatory disease | -3.9683 | 3.4646 | ±6.9292 | -1.145 | 0.2520 |  |
| Mean glucose (mg/dL) | -0.0463 | 0.0680 | ±0.1359 | -0.682 | 0.4953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.1107**, Adj R² = **0.0522**, F-statistic = **1.89** (p = **0.0285**), Residual SE = **19.077** on **213** df, AIC = **2006.0**, BIC = **2057.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.4616** | 16.5062 | ±33.0124 | **+8.328** | **8.23e-17** | *** |
| **Education: graduate level (vs college)** | **-9.6263** | 2.9324 | ±5.8648 | **-3.283** | **0.0010** | ** |
| Education: high school or below (vs college) | +1.6342 | 4.0412 | ±8.0824 | +0.404 | 0.6859 |  |
| Site: UCSD (vs UAB) | +1.7172 | 3.5463 | ±7.0927 | +0.484 | 0.6282 |  |
| Site: UW (vs UAB) | +0.3147 | 2.9743 | ±5.9486 | +0.106 | 0.9157 |  |
| Season: spring (vs autumn) | +3.5887 | 3.4924 | ±6.9848 | +1.028 | 0.3041 |  |
| Season: summer (vs autumn) | +1.9224 | 3.5125 | ±7.0249 | +0.547 | 0.5842 |  |
| **Season: winter (vs autumn)** | **+10.4681** | 4.5953 | ±9.1906 | **+2.278** | **0.0227** | * |
| Age (years) | -0.0494 | 0.1278 | ±0.2556 | -0.386 | 0.6991 |  |
| BMI (kg/m2) | +0.1678 | 0.1840 | ±0.3679 | +0.912 | 0.3618 |  |
| Hypertension | -2.4678 | 3.3716 | ±6.7433 | -0.732 | 0.4642 |  |
| High cholesterol | +2.2878 | 3.1482 | ±6.2965 | +0.727 | 0.4674 |  |
| Kidney disease | +2.0103 | 3.7746 | ±7.5492 | +0.533 | 0.5943 |  |
| Circulatory disease | -3.9683 | 3.4646 | ±6.9292 | -1.145 | 0.2520 |  |
| GMI (%) | -1.9376 | 2.8415 | ±5.6831 | -0.682 | 0.4953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.1209**, Adj R² = **0.0631**, F-statistic = **2.09** (p = **0.0133**), Residual SE = **18.967** on **213** df, AIC = **2003.4**, BIC = **2054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.3072** | 12.4336 | ±24.8672 | **+10.882** | **1.40e-27** | *** |
| **Education: graduate level (vs college)** | **-9.4998** | 2.9934 | ±5.9869 | **-3.174** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.8130 | 3.9855 | ±7.9711 | +0.455 | 0.6492 |  |
| Site: UCSD (vs UAB) | +1.7447 | 3.5397 | ±7.0794 | +0.493 | 0.6221 |  |
| Site: UW (vs UAB) | +0.3310 | 2.9734 | ±5.9469 | +0.111 | 0.9114 |  |
| Season: spring (vs autumn) | +4.0081 | 3.5396 | ±7.0792 | +1.132 | 0.2575 |  |
| Season: summer (vs autumn) | +1.7993 | 3.4911 | ±6.9822 | +0.515 | 0.6063 |  |
| **Season: winter (vs autumn)** | **+10.7703** | 4.5836 | ±9.1672 | **+2.350** | **0.0188** | * |
| Age (years) | -0.0626 | 0.1238 | ±0.2476 | -0.505 | 0.6132 |  |
| BMI (kg/m2) | +0.1692 | 0.1866 | ±0.3732 | +0.907 | 0.3644 |  |
| Hypertension | -2.2282 | 3.3968 | ±6.7937 | -0.656 | 0.5118 |  |
| High cholesterol | +2.3749 | 3.1342 | ±6.2684 | +0.758 | 0.4486 |  |
| Kidney disease | +1.7346 | 3.7023 | ±7.4045 | +0.469 | 0.6394 |  |
| Circulatory disease | -3.8455 | 3.3964 | ±6.7928 | -1.132 | 0.2575 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0784 | 0.0759 | ±0.1519 | -1.033 | 0.3017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1103**, Adj R² = **0.0519**, F-statistic = **1.89** (p = **0.0291**), Residual SE = **19.080** on **213** df, AIC = **2006.1**, BIC = **2057.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.3001** | 12.5658 | ±25.1317 | **+10.131** | **4.04e-24** | *** |
| **Education: graduate level (vs college)** | **-9.8666** | 2.9115 | ±5.8230 | **-3.389** | **7.02e-04** | *** |
| Education: high school or below (vs college) | +1.9780 | 4.0720 | ±8.1440 | +0.486 | 0.6271 |  |
| Site: UCSD (vs UAB) | +1.6259 | 3.5724 | ±7.1448 | +0.455 | 0.6490 |  |
| Site: UW (vs UAB) | +0.1904 | 2.9699 | ±5.9399 | +0.064 | 0.9489 |  |
| Season: spring (vs autumn) | +3.2612 | 3.4068 | ±6.8136 | +0.957 | 0.3384 |  |
| Season: summer (vs autumn) | +1.7698 | 3.4863 | ±6.9726 | +0.508 | 0.6117 |  |
| **Season: winter (vs autumn)** | **+10.2599** | 4.7301 | ±9.4602 | **+2.169** | **0.0301** | * |
| Age (years) | -0.0298 | 0.1360 | ±0.2720 | -0.219 | 0.8263 |  |
| BMI (kg/m2) | +0.1599 | 0.1780 | ±0.3560 | +0.898 | 0.3689 |  |
| Hypertension | -2.5028 | 3.3198 | ±6.6396 | -0.754 | 0.4509 |  |
| High cholesterol | +2.2513 | 3.1042 | ±6.2084 | +0.725 | 0.4683 |  |
| Kidney disease | +2.5209 | 3.8693 | ±7.7385 | +0.652 | 0.5147 |  |
| Circulatory disease | -4.1439 | 3.5092 | ±7.0185 | -1.181 | 0.2377 |  |
| Glucose SD, pooled (mg/dL) | -0.0948 | 0.1157 | ±0.2314 | -0.819 | 0.4126 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1059**, Adj R² = **0.0471**, F-statistic = **1.80** (p = **0.0398**), Residual SE = **19.128** on **213** df, AIC = **2007.2**, BIC = **2058.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7724** | 12.8114 | ±25.6229 | **+9.817** | **9.50e-23** | *** |
| **Education: graduate level (vs college)** | **-9.6033** | 2.9343 | ±5.8687 | **-3.273** | **0.0011** | ** |
| Education: high school or below (vs college) | +1.5745 | 4.0304 | ±8.0609 | +0.391 | 0.6960 |  |
| Site: UCSD (vs UAB) | +1.6925 | 3.5459 | ±7.0919 | +0.477 | 0.6331 |  |
| Site: UW (vs UAB) | +0.3520 | 2.9598 | ±5.9195 | +0.119 | 0.9053 |  |
| Season: spring (vs autumn) | +3.1593 | 3.4256 | ±6.8512 | +0.922 | 0.3564 |  |
| Season: summer (vs autumn) | +1.8631 | 3.4895 | ±6.9789 | +0.534 | 0.5934 |  |
| **Season: winter (vs autumn)** | **+10.1014** | 4.7738 | ±9.5476 | **+2.116** | **0.0343** | * |
| Age (years) | -0.0436 | 0.1310 | ±0.2620 | -0.333 | 0.7392 |  |
| BMI (kg/m2) | +0.1672 | 0.1807 | ±0.3614 | +0.925 | 0.3547 |  |
| Hypertension | -2.5716 | 3.3126 | ±6.6252 | -0.776 | 0.4376 |  |
| High cholesterol | +2.3813 | 3.1211 | ±6.2422 | +0.763 | 0.4455 |  |
| Kidney disease | +1.8908 | 3.8864 | ±7.7728 | +0.487 | 0.6266 |  |
| Circulatory disease | -4.1416 | 3.5209 | ±7.0418 | -1.176 | 0.2395 |  |
| Avg. daily SD (mg/dL) | -0.0360 | 0.1034 | ±0.2068 | -0.348 | 0.7281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.1055**, Adj R² = **0.0467**, F-statistic = **1.79** (p = **0.0410**), Residual SE = **19.133** on **213** df, AIC = **2007.4**, BIC = **2058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3267** | 13.0921 | ±26.1842 | **+9.573** | **1.04e-21** | *** |
| **Education: graduate level (vs college)** | **-9.5219** | 2.9759 | ±5.9517 | **-3.200** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.4032 | 4.0041 | ±8.0082 | +0.350 | 0.7260 |  |
| Site: UCSD (vs UAB) | +1.7039 | 3.5574 | ±7.1148 | +0.479 | 0.6320 |  |
| Site: UW (vs UAB) | +0.3856 | 2.9596 | ±5.9191 | +0.130 | 0.8963 |  |
| Season: spring (vs autumn) | +3.0551 | 3.4207 | ±6.8414 | +0.893 | 0.3718 |  |
| Season: summer (vs autumn) | +1.8924 | 3.4912 | ±6.9825 | +0.542 | 0.5878 |  |
| **Season: winter (vs autumn)** | **+10.0537** | 4.8107 | ±9.6213 | **+2.090** | **0.0366** | * |
| Age (years) | -0.0466 | 0.1339 | ±0.2679 | -0.348 | 0.7279 |  |
| BMI (kg/m2) | +0.1705 | 0.1828 | ±0.3656 | +0.933 | 0.3510 |  |
| Hypertension | -2.5783 | 3.3086 | ±6.6172 | -0.779 | 0.4358 |  |
| High cholesterol | +2.4243 | 3.1130 | ±6.2260 | +0.779 | 0.4361 |  |
| Kidney disease | +1.6941 | 3.9037 | ±7.8074 | +0.434 | 0.6643 |  |
| Circulatory disease | -4.1300 | 3.5257 | ±7.0513 | -1.171 | 0.2414 |  |
| CV (%) | -0.0217 | 0.2029 | ±0.4057 | -0.107 | 0.9149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.1056**, Adj R² = **0.0468**, F-statistic = **1.80** (p = **0.0407**), Residual SE = **19.131** on **213** df, AIC = **2007.3**, BIC = **2058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3209** | 16.2357 | ±32.4714 | **+7.780** | **7.23e-15** | *** |
| **Education: graduate level (vs college)** | **-9.3860** | 2.9803 | ±5.9607 | **-3.149** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.1729 | 4.0236 | ±8.0473 | +0.291 | 0.7707 |  |
| Site: UCSD (vs UAB) | +1.7216 | 3.5235 | ±7.0470 | +0.489 | 0.6251 |  |
| Site: UW (vs UAB) | +0.4417 | 2.9503 | ±5.9006 | +0.150 | 0.8810 |  |
| Season: spring (vs autumn) | +3.0341 | 3.4462 | ±6.8923 | +0.880 | 0.3786 |  |
| Season: summer (vs autumn) | +1.8811 | 3.5043 | ±7.0085 | +0.537 | 0.5914 |  |
| **Season: winter (vs autumn)** | **+10.0312** | 4.8118 | ±9.6236 | **+2.085** | **0.0371** | * |
| Age (years) | -0.0579 | 0.1375 | ±0.2749 | -0.421 | 0.6738 |  |
| BMI (kg/m2) | +0.1734 | 0.1836 | ±0.3671 | +0.945 | 0.3449 |  |
| Hypertension | -2.5598 | 3.3144 | ±6.6289 | -0.772 | 0.4399 |  |
| High cholesterol | +2.4713 | 3.1255 | ±6.2510 | +0.791 | 0.4291 |  |
| Kidney disease | +1.4231 | 3.9154 | ±7.8307 | +0.363 | 0.7163 |  |
| Circulatory disease | -4.1355 | 3.5094 | ±7.0188 | -1.178 | 0.2386 |  |
| Mean / SD ratio | -0.2112 | 1.0134 | ±2.0269 | -0.208 | 0.8350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1083**, Adj R² = **0.0497**, F-statistic = **1.85** (p = **0.0338**), Residual SE = **19.103** on **213** df, AIC = **2006.6**, BIC = **2058.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.2075** | 14.5490 | ±29.0981 | **+8.950** | **3.57e-19** | *** |
| **Education: graduate level (vs college)** | **-9.0801** | 3.0432 | ±6.0863 | **-2.984** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.6960 | 3.9248 | ±7.8497 | +0.177 | 0.8592 |  |
| Site: UCSD (vs UAB) | +1.6693 | 3.5030 | ±7.0060 | +0.477 | 0.6337 |  |
| Site: UW (vs UAB) | +0.4850 | 2.9577 | ±5.9154 | +0.164 | 0.8698 |  |
| Season: spring (vs autumn) | +3.0007 | 3.4415 | ±6.8830 | +0.872 | 0.3832 |  |
| Season: summer (vs autumn) | +1.8892 | 3.4740 | ±6.9479 | +0.544 | 0.5866 |  |
| **Season: winter (vs autumn)** | **+10.0884** | 4.8220 | ±9.6441 | **+2.092** | **0.0364** | * |
| Age (years) | -0.0816 | 0.1294 | ±0.2588 | -0.631 | 0.5283 |  |
| BMI (kg/m2) | +0.1794 | 0.1858 | ±0.3717 | +0.965 | 0.3345 |  |
| Hypertension | -2.4268 | 3.3003 | ±6.6007 | -0.735 | 0.4621 |  |
| High cholesterol | +2.5115 | 3.1184 | ±6.2369 | +0.805 | 0.4206 |  |
| Kidney disease | +1.1107 | 3.8919 | ±7.7838 | +0.285 | 0.7754 |  |
| Circulatory disease | -4.1220 | 3.4961 | ±6.9922 | -1.179 | 0.2384 |  |
| Avg. daily mean/SD | -0.6956 | 0.7804 | ±1.5607 | -0.891 | 0.3727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.1119**, Adj R² = **0.0535**, F-statistic = **1.92** (p = **0.0261**), Residual SE = **19.064** on **213** df, AIC = **2005.7**, BIC = **2057.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.1075** | 12.0520 | ±24.1040 | **+9.883** | **4.94e-23** | *** |
| **Education: graduate level (vs college)** | **-9.1561** | 2.9104 | ±5.8208 | **-3.146** | **0.0017** | ** |
| Education: high school or below (vs college) | +0.4721 | 3.9050 | ±7.8100 | +0.121 | 0.9038 |  |
| Site: UCSD (vs UAB) | +1.5174 | 3.5274 | ±7.0548 | +0.430 | 0.6671 |  |
| Site: UW (vs UAB) | +0.7677 | 2.8723 | ±5.7446 | +0.267 | 0.7893 |  |
| Season: spring (vs autumn) | +2.8445 | 3.4810 | ±6.9620 | +0.817 | 0.4138 |  |
| Season: summer (vs autumn) | +2.0534 | 3.4992 | ±6.9984 | +0.587 | 0.5573 |  |
| **Season: winter (vs autumn)** | **+10.1375** | 4.7979 | ±9.5959 | **+2.113** | **0.0346** | * |
| Age (years) | -0.0586 | 0.1272 | ±0.2545 | -0.461 | 0.6449 |  |
| BMI (kg/m2) | +0.1571 | 0.1862 | ±0.3724 | +0.844 | 0.3987 |  |
| Hypertension | -2.4595 | 3.2406 | ±6.4812 | -0.759 | 0.4479 |  |
| High cholesterol | +2.4597 | 3.1271 | ±6.2542 | +0.787 | 0.4315 |  |
| Kidney disease | +1.5455 | 3.8207 | ±7.6415 | +0.405 | 0.6858 |  |
| Circulatory disease | -4.1038 | 3.4875 | ±6.9750 | -1.177 | 0.2393 |  |
| MAG (mg/dL/h) | +0.1506 | 0.1331 | ±0.2661 | +1.132 | 0.2578 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.1061**, Adj R² = **0.0474**, F-statistic = **1.81** (p = **0.0392**), Residual SE = **19.126** on **213** df, AIC = **2007.2**, BIC = **2058.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.6003** | 12.6285 | ±25.2570 | **+9.787** | **1.28e-22** | *** |
| **Education: graduate level (vs college)** | **-9.3150** | 2.9211 | ±5.8421 | **-3.189** | **0.0014** | ** |
| Education: high school or below (vs college) | +0.9923 | 4.0281 | ±8.0562 | +0.246 | 0.8054 |  |
| Site: UCSD (vs UAB) | +1.7499 | 3.5331 | ±7.0662 | +0.495 | 0.6204 |  |
| Site: UW (vs UAB) | +0.4629 | 2.9468 | ±5.8936 | +0.157 | 0.8752 |  |
| Season: spring (vs autumn) | +2.9142 | 3.4732 | ±6.9464 | +0.839 | 0.4014 |  |
| Season: summer (vs autumn) | +1.8890 | 3.4883 | ±6.9766 | +0.542 | 0.5881 |  |
| **Season: winter (vs autumn)** | **+9.9956** | 4.8016 | ±9.6031 | **+2.082** | **0.0374** | * |
| Age (years) | -0.0579 | 0.1303 | ±0.2607 | -0.444 | 0.6571 |  |
| BMI (kg/m2) | +0.1781 | 0.1813 | ±0.3625 | +0.982 | 0.3259 |  |
| Hypertension | -2.5474 | 3.3064 | ±6.6129 | -0.770 | 0.4410 |  |
| High cholesterol | +2.4891 | 3.1247 | ±6.2495 | +0.797 | 0.4257 |  |
| Kidney disease | +1.2156 | 3.8283 | ±7.6566 | +0.318 | 0.7508 |  |
| Circulatory disease | -4.1395 | 3.5207 | ±7.0415 | -1.176 | 0.2397 |  |
| Avg. daily range (mg/dL) | +0.0122 | 0.0300 | ±0.0600 | +0.407 | 0.6838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.1394**, Adj R² = **0.0828**, F-statistic = **2.46** (p = **0.0030**), Residual SE = **18.766** on **213** df, AIC = **1998.5**, BIC = **2050.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.4080** | 12.7918 | ±25.5836 | **+10.038** | **1.03e-23** | *** |
| **Education: graduate level (vs college)** | **-10.4510** | 2.9274 | ±5.8547 | **-3.570** | **3.57e-04** | *** |
| Education: high school or below (vs college) | +1.6555 | 3.8308 | ±7.6615 | +0.432 | 0.6656 |  |
| Site: UCSD (vs UAB) | +1.5866 | 3.5161 | ±7.0322 | +0.451 | 0.6518 |  |
| Site: UW (vs UAB) | -0.1472 | 2.9772 | ±5.9544 | -0.049 | 0.9606 |  |
| Season: spring (vs autumn) | +2.8054 | 3.2845 | ±6.5690 | +0.854 | 0.3930 |  |
| Season: summer (vs autumn) | +1.7751 | 3.4704 | ±6.9408 | +0.511 | 0.6090 |  |
| **Season: winter (vs autumn)** | **+11.0759** | 4.5820 | ±9.1640 | **+2.417** | **0.0156** | * |
| Age (years) | -0.0220 | 0.1394 | ±0.2788 | -0.158 | 0.8747 |  |
| BMI (kg/m2) | +0.1480 | 0.1734 | ±0.3468 | +0.854 | 0.3933 |  |
| Hypertension | -1.7592 | 3.3522 | ±6.7044 | -0.525 | 0.5997 |  |
| High cholesterol | +2.1820 | 3.1001 | ±6.2003 | +0.704 | 0.4815 |  |
| Kidney disease | +3.3214 | 3.7143 | ±7.4286 | +0.894 | 0.3712 |  |
| Circulatory disease | -3.5594 | 3.3226 | ±6.6453 | -1.071 | 0.2840 |  |
| SD of daily means (mg/dL) | -0.3916 | 0.2876 | ±0.5751 | -1.362 | 0.1733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.1069**, Adj R² = **0.0482**, F-statistic = **1.82** (p = **0.0371**), Residual SE = **19.117** on **213** df, AIC = **2007.0**, BIC = **2058.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.1196** | 22.0632 | ±44.1265 | **+5.490** | **4.03e-08** | *** |
| **Education: graduate level (vs college)** | **-9.6936** | 2.8254 | ±5.6508 | **-3.431** | **6.02e-04** | *** |
| Education: high school or below (vs college) | +1.4993 | 4.0725 | ±8.1451 | +0.368 | 0.7128 |  |
| Site: UCSD (vs UAB) | +1.6714 | 3.5854 | ±7.1707 | +0.466 | 0.6411 |  |
| Site: UW (vs UAB) | +0.3132 | 2.9508 | ±5.9017 | +0.106 | 0.9155 |  |
| Season: spring (vs autumn) | +3.2289 | 3.4506 | ±6.9013 | +0.936 | 0.3494 |  |
| Season: summer (vs autumn) | +1.8421 | 3.4819 | ±6.9638 | +0.529 | 0.5968 |  |
| **Season: winter (vs autumn)** | **+10.2995** | 4.5619 | ±9.1237 | **+2.258** | **0.0240** | * |
| Age (years) | -0.0457 | 0.1351 | ±0.2702 | -0.338 | 0.7351 |  |
| BMI (kg/m2) | +0.1665 | 0.1791 | ±0.3582 | +0.930 | 0.3525 |  |
| Hypertension | -2.5687 | 3.3781 | ±6.7562 | -0.760 | 0.4470 |  |
| High cholesterol | +2.4320 | 3.1670 | ±6.3340 | +0.768 | 0.4425 |  |
| Kidney disease | +1.9385 | 3.8584 | ±7.7168 | +0.502 | 0.6154 |  |
| Circulatory disease | -4.0145 | 3.4919 | ±6.9839 | -1.150 | 0.2503 |  |
| Time in range 70-180, pooled (%) | +0.0438 | 0.1278 | ±0.2556 | +0.343 | 0.7319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.1076**, Adj R² = **0.0489**, F-statistic = **1.83** (p = **0.0354**), Residual SE = **19.110** on **213** df, AIC = **2006.8**, BIC = **2058.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120.3501** | 22.0898 | ±44.1795 | **+5.448** | **5.09e-08** | *** |
| **Education: graduate level (vs college)** | **-9.7359** | 2.8318 | ±5.6637 | **-3.438** | **5.86e-04** | *** |
| Education: high school or below (vs college) | +1.5557 | 4.0762 | ±8.1524 | +0.382 | 0.7027 |  |
| Site: UCSD (vs UAB) | +1.6524 | 3.5860 | ±7.1719 | +0.461 | 0.6449 |  |
| Site: UW (vs UAB) | +0.2851 | 2.9470 | ±5.8940 | +0.097 | 0.9229 |  |
| Season: spring (vs autumn) | +3.2791 | 3.4616 | ±6.9231 | +0.947 | 0.3435 |  |
| Season: summer (vs autumn) | +1.8534 | 3.4890 | ±6.9780 | +0.531 | 0.5953 |  |
| **Season: winter (vs autumn)** | **+10.3801** | 4.5486 | ±9.0972 | **+2.282** | **0.0225** | * |
| Age (years) | -0.0447 | 0.1355 | ±0.2709 | -0.330 | 0.7413 |  |
| BMI (kg/m2) | +0.1647 | 0.1784 | ±0.3569 | +0.923 | 0.3561 |  |
| Hypertension | -2.5796 | 3.3782 | ±6.7565 | -0.764 | 0.4451 |  |
| High cholesterol | +2.4331 | 3.1665 | ±6.3330 | +0.768 | 0.4423 |  |
| Kidney disease | +2.0277 | 3.8424 | ±7.6849 | +0.528 | 0.5977 |  |
| Circulatory disease | -3.9917 | 3.4900 | ±6.9799 | -1.144 | 0.2527 |  |
| Avg. daily time in range 70-180 (%) | +0.0524 | 0.1282 | ±0.2564 | +0.409 | 0.6825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1072**, Adj R² = **0.0486**, F-statistic = **1.83** (p = **0.0363**), Residual SE = **19.114** on **213** df, AIC = **2006.9**, BIC = **2058.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.5212** | 13.4157 | ±26.8315 | **+9.282** | **1.67e-20** | *** |
| **Education: graduate level (vs college)** | **-9.3677** | 2.9891 | ±5.9783 | **-3.134** | **0.0017** | ** |
| Education: high school or below (vs college) | +1.4906 | 3.8928 | ±7.7855 | +0.383 | 0.7018 |  |
| Site: UCSD (vs UAB) | +2.0149 | 3.5497 | ±7.0994 | +0.568 | 0.5703 |  |
| Site: UW (vs UAB) | +0.7676 | 3.0625 | ±6.1249 | +0.251 | 0.8021 |  |
| Season: spring (vs autumn) | +3.2135 | 3.4455 | ±6.8910 | +0.933 | 0.3510 |  |
| Season: summer (vs autumn) | +1.9345 | 3.4862 | ±6.9723 | +0.555 | 0.5789 |  |
| **Season: winter (vs autumn)** | **+10.1028** | 4.7977 | ±9.5954 | **+2.106** | **0.0352** | * |
| Age (years) | -0.0526 | 0.1243 | ±0.2485 | -0.423 | 0.6722 |  |
| BMI (kg/m2) | +0.1695 | 0.1854 | ±0.3709 | +0.914 | 0.3606 |  |
| Hypertension | -2.6184 | 3.2919 | ±6.5839 | -0.795 | 0.4264 |  |
| High cholesterol | +2.3908 | 3.1190 | ±6.2381 | +0.767 | 0.4434 |  |
| Kidney disease | +1.6460 | 3.8001 | ±7.6002 | +0.433 | 0.6649 |  |
| Circulatory disease | -4.2947 | 3.5248 | ±7.0496 | -1.218 | 0.2231 |  |
| Time < 54 (%) | +1.1706 | 1.1956 | ±2.3912 | +0.979 | 0.3275 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.1087**, Adj R² = **0.0501**, F-statistic = **1.86** (p = **0.0327**), Residual SE = **19.098** on **213** df, AIC = **2006.5**, BIC = **2058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7685** | 13.2818 | ±26.5637 | **+9.394** | **5.78e-21** | *** |
| **Education: graduate level (vs college)** | **-9.2689** | 2.9799 | ±5.9599 | **-3.110** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.5314 | 3.8956 | ±7.7911 | +0.393 | 0.6942 |  |
| Site: UCSD (vs UAB) | +2.0474 | 3.5266 | ±7.0532 | +0.581 | 0.5615 |  |
| Site: UW (vs UAB) | +0.7640 | 3.0221 | ±6.0443 | +0.253 | 0.8004 |  |
| Season: spring (vs autumn) | +3.3297 | 3.4417 | ±6.8835 | +0.967 | 0.3333 |  |
| Season: summer (vs autumn) | +1.9382 | 3.4923 | ±6.9845 | +0.555 | 0.5789 |  |
| **Season: winter (vs autumn)** | **+10.0769** | 4.7974 | ±9.5948 | **+2.100** | **0.0357** | * |
| Age (years) | -0.0586 | 0.1235 | ±0.2470 | -0.475 | 0.6350 |  |
| BMI (kg/m2) | +0.1709 | 0.1850 | ±0.3699 | +0.924 | 0.3555 |  |
| Hypertension | -2.5865 | 3.2859 | ±6.5718 | -0.787 | 0.4312 |  |
| High cholesterol | +2.4708 | 3.1101 | ±6.2202 | +0.794 | 0.4269 |  |
| Kidney disease | +1.5631 | 3.7987 | ±7.5974 | +0.411 | 0.6807 |  |
| Circulatory disease | -4.3251 | 3.5285 | ±7.0571 | -1.226 | 0.2203 |  |
| Avg. daily time < 54 (%) | +1.4200 | 1.2212 | ±2.4423 | +1.163 | 0.2449 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1092**, Adj R² = **0.0506**, F-statistic = **1.86** (p = **0.0317**), Residual SE = **19.093** on **213** df, AIC = **2006.4**, BIC = **2057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7648** | 13.3278 | ±26.6557 | **+9.361** | **7.88e-21** | *** |
| **Education: graduate level (vs college)** | **-9.0660** | 3.0320 | ±6.0640 | **-2.990** | **0.0028** | ** |
| Education: high school or below (vs college) | +1.2061 | 3.9239 | ±7.8479 | +0.307 | 0.7586 |  |
| Site: UCSD (vs UAB) | +1.9128 | 3.5154 | ±7.0309 | +0.544 | 0.5864 |  |
| Site: UW (vs UAB) | +0.5502 | 3.0108 | ±6.0215 | +0.183 | 0.8550 |  |
| Season: spring (vs autumn) | +3.3930 | 3.4561 | ±6.9123 | +0.982 | 0.3262 |  |
| Season: summer (vs autumn) | +2.0213 | 3.4768 | ±6.9535 | +0.581 | 0.5610 |  |
| **Season: winter (vs autumn)** | **+10.1838** | 4.7747 | ±9.5494 | **+2.133** | **0.0329** | * |
| Age (years) | -0.0667 | 0.1223 | ±0.2447 | -0.545 | 0.5854 |  |
| BMI (kg/m2) | +0.1739 | 0.1870 | ±0.3739 | +0.930 | 0.3522 |  |
| Hypertension | -2.4597 | 3.3091 | ±6.6183 | -0.743 | 0.4573 |  |
| High cholesterol | +2.2640 | 3.1161 | ±6.2323 | +0.727 | 0.4675 |  |
| Kidney disease | +1.4791 | 3.8028 | ±7.6056 | +0.389 | 0.6973 |  |
| Circulatory disease | -4.1445 | 3.4963 | ±6.9927 | -1.185 | 0.2359 |  |
| Time 54-69, pooled (%) | +0.4954 | 0.4425 | ±0.8849 | +1.120 | 0.2629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.1081**, Adj R² = **0.0495**, F-statistic = **1.84** (p = **0.0342**), Residual SE = **19.105** on **213** df, AIC = **2006.7**, BIC = **2058.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0135** | 13.2464 | ±26.4928 | **+9.438** | **3.82e-21** | *** |
| **Education: graduate level (vs college)** | **-9.1282** | 3.0181 | ±6.0362 | **-3.024** | **0.0025** | ** |
| Education: high school or below (vs college) | +1.1900 | 3.9224 | ±7.8448 | +0.303 | 0.7616 |  |
| Site: UCSD (vs UAB) | +1.8759 | 3.5155 | ±7.0310 | +0.534 | 0.5936 |  |
| Site: UW (vs UAB) | +0.5367 | 3.0149 | ±6.0297 | +0.178 | 0.8587 |  |
| Season: spring (vs autumn) | +3.3222 | 3.4517 | ±6.9034 | +0.962 | 0.3358 |  |
| Season: summer (vs autumn) | +1.9660 | 3.4827 | ±6.9654 | +0.565 | 0.5724 |  |
| **Season: winter (vs autumn)** | **+10.1389** | 4.7800 | ±9.5600 | **+2.121** | **0.0339** | * |
| Age (years) | -0.0664 | 0.1224 | ±0.2448 | -0.542 | 0.5877 |  |
| BMI (kg/m2) | +0.1728 | 0.1859 | ±0.3717 | +0.930 | 0.3525 |  |
| Hypertension | -2.4716 | 3.3050 | ±6.6100 | -0.748 | 0.4546 |  |
| High cholesterol | +2.3129 | 3.1126 | ±6.2253 | +0.743 | 0.4574 |  |
| Kidney disease | +1.5112 | 3.8054 | ±7.6109 | +0.397 | 0.6913 |  |
| Circulatory disease | -4.1125 | 3.4983 | ±6.9966 | -1.176 | 0.2398 |  |
| Avg. daily time 54-69 (%) | +0.3992 | 0.4093 | ±0.8186 | +0.975 | 0.3294 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.1092**, Adj R² = **0.0506**, F-statistic = **1.86** (p = **0.0316**), Residual SE = **19.093** on **213** df, AIC = **2006.4**, BIC = **2057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6419** | 13.3647 | ±26.7294 | **+9.326** | **1.10e-20** | *** |
| **Education: graduate level (vs college)** | **-9.0974** | 3.0281 | ±6.0562 | **-3.004** | **0.0027** | ** |
| Education: high school or below (vs college) | +1.2844 | 3.9179 | ±7.8357 | +0.328 | 0.7430 |  |
| Site: UCSD (vs UAB) | +1.9845 | 3.5231 | ±7.0462 | +0.563 | 0.5732 |  |
| Site: UW (vs UAB) | +0.6523 | 3.0320 | ±6.0640 | +0.215 | 0.8297 |  |
| Season: spring (vs autumn) | +3.3916 | 3.4569 | ±6.9138 | +0.981 | 0.3265 |  |
| Season: summer (vs autumn) | +2.0136 | 3.4780 | ±6.9560 | +0.579 | 0.5626 |  |
| **Season: winter (vs autumn)** | **+10.1801** | 4.7771 | ±9.5542 | **+2.131** | **0.0331** | * |
| Age (years) | -0.0648 | 0.1225 | ±0.2449 | -0.529 | 0.5969 |  |
| BMI (kg/m2) | +0.1728 | 0.1869 | ±0.3739 | +0.924 | 0.3554 |  |
| Hypertension | -2.4940 | 3.3029 | ±6.6057 | -0.755 | 0.4502 |  |
| High cholesterol | +2.2766 | 3.1178 | ±6.2356 | +0.730 | 0.4653 |  |
| Kidney disease | +1.5193 | 3.7990 | ±7.5980 | +0.400 | 0.6892 |  |
| Circulatory disease | -4.2015 | 3.4987 | ±6.9973 | -1.201 | 0.2298 |  |
| Time < 70 (%) | +0.4118 | 0.3478 | ±0.6955 | +1.184 | 0.2364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.1087**, Adj R² = **0.0501**, F-statistic = **1.85** (p = **0.0328**), Residual SE = **19.098** on **213** df, AIC = **2006.5**, BIC = **2058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9584** | 13.2575 | ±26.5150 | **+9.425** | **4.28e-21** | *** |
| **Education: graduate level (vs college)** | **-9.1094** | 3.0124 | ±6.0249 | **-3.024** | **0.0025** | ** |
| Education: high school or below (vs college) | +1.2554 | 3.9198 | ±7.8395 | +0.320 | 0.7488 |  |
| Site: UCSD (vs UAB) | +1.9443 | 3.5182 | ±7.0364 | +0.553 | 0.5805 |  |
| Site: UW (vs UAB) | +0.6143 | 3.0267 | ±6.0535 | +0.203 | 0.8392 |  |
| Season: spring (vs autumn) | +3.3661 | 3.4528 | ±6.9057 | +0.975 | 0.3296 |  |
| Season: summer (vs autumn) | +1.9699 | 3.4826 | ±6.9652 | +0.566 | 0.5716 |  |
| **Season: winter (vs autumn)** | **+10.1374** | 4.7816 | ±9.5632 | **+2.120** | **0.0340** | * |
| Age (years) | -0.0669 | 0.1222 | ±0.2444 | -0.548 | 0.5840 |  |
| BMI (kg/m2) | +0.1725 | 0.1858 | ±0.3715 | +0.928 | 0.3532 |  |
| Hypertension | -2.4841 | 3.2976 | ±6.5952 | -0.753 | 0.4513 |  |
| High cholesterol | +2.3332 | 3.1118 | ±6.2237 | +0.750 | 0.4534 |  |
| Kidney disease | +1.5135 | 3.8006 | ±7.6013 | +0.398 | 0.6905 |  |
| Circulatory disease | -4.1651 | 3.4980 | ±6.9961 | -1.191 | 0.2338 |  |
| Avg. daily time < 70 (%) | +0.3606 | 0.3130 | ±0.6261 | +1.152 | 0.2493 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1263**, Adj R² = **0.0688**, F-statistic = **2.20** (p = **0.0088**), Residual SE = **18.909** on **213** df, AIC = **2002.0**, BIC = **2053.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+95.3096** | 32.6024 | ±65.2048 | **+2.923** | **0.0035** | ** |
| **Education: graduate level (vs college)** | **-10.0465** | 2.9335 | ±5.8669 | **-3.425** | **6.15e-04** | *** |
| Education: high school or below (vs college) | +2.0948 | 4.0905 | ±8.1809 | +0.512 | 0.6086 |  |
| Site: UCSD (vs UAB) | +1.5564 | 3.5525 | ±7.1050 | +0.438 | 0.6613 |  |
| Site: UW (vs UAB) | -0.2513 | 3.0458 | ±6.0917 | -0.083 | 0.9342 |  |
| Season: spring (vs autumn) | +3.4866 | 3.3822 | ±6.7644 | +1.031 | 0.3026 |  |
| Season: summer (vs autumn) | +1.1342 | 3.4454 | ±6.8909 | +0.329 | 0.7420 |  |
| **Season: winter (vs autumn)** | **+10.3328** | 4.7188 | ±9.4377 | **+2.190** | **0.0285** | * |
| Age (years) | -0.0586 | 0.1257 | ±0.2514 | -0.466 | 0.6412 |  |
| BMI (kg/m2) | +0.1507 | 0.1777 | ±0.3554 | +0.848 | 0.3963 |  |
| Hypertension | -2.2585 | 3.3432 | ±6.6863 | -0.676 | 0.4993 |  |
| High cholesterol | +1.9715 | 3.0741 | ±6.1482 | +0.641 | 0.5213 |  |
| Kidney disease | +2.1416 | 3.7730 | ±7.5461 | +0.568 | 0.5703 |  |
| Circulatory disease | -3.6836 | 3.3509 | ±6.7017 | -1.099 | 0.2716 |  |
| Time 54-250, pooled (%) | +0.3217 | 0.2829 | ±0.5658 | +1.137 | 0.2556 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1296**, Adj R² = **0.0724**, F-statistic = **2.27** (p = **0.0067**), Residual SE = **18.872** on **213** df, AIC = **2001.1**, BIC = **2052.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+88.9074** | 36.3101 | ±72.6202 | **+2.449** | **0.0143** | * |
| **Education: graduate level (vs college)** | **-10.1401** | 2.9366 | ±5.8733 | **-3.453** | **5.54e-04** | *** |
| Education: high school or below (vs college) | +2.3103 | 4.0953 | ±8.1905 | +0.564 | 0.5727 |  |
| Site: UCSD (vs UAB) | +1.5999 | 3.5357 | ±7.0715 | +0.453 | 0.6509 |  |
| Site: UW (vs UAB) | -0.2083 | 3.0342 | ±6.0683 | -0.069 | 0.9453 |  |
| Season: spring (vs autumn) | +3.7300 | 3.3891 | ±6.7782 | +1.101 | 0.2711 |  |
| Season: summer (vs autumn) | +1.2050 | 3.4285 | ±6.8569 | +0.351 | 0.7252 |  |
| **Season: winter (vs autumn)** | **+10.5950** | 4.6622 | ±9.3244 | **+2.273** | **0.0231** | * |
| Age (years) | -0.0547 | 0.1270 | ±0.2541 | -0.431 | 0.6666 |  |
| BMI (kg/m2) | +0.1422 | 0.1762 | ±0.3525 | +0.807 | 0.4198 |  |
| Hypertension | -2.2182 | 3.3426 | ±6.6852 | -0.664 | 0.5069 |  |
| High cholesterol | +1.9280 | 3.0690 | ±6.1380 | +0.628 | 0.5299 |  |
| Kidney disease | +2.3660 | 3.7552 | ±7.5104 | +0.630 | 0.5287 |  |
| Circulatory disease | -3.5219 | 3.3262 | ±6.6524 | -1.059 | 0.2897 |  |
| Avg. daily time 54-250 (%) | +0.3848 | 0.3200 | ±0.6400 | +1.203 | 0.2291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1068**, Adj R² = **0.0481**, F-statistic = **1.82** (p = **0.0373**), Residual SE = **19.118** on **213** df, AIC = **2007.0**, BIC = **2058.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7205** | 13.0508 | ±26.1016 | **+9.557** | **1.22e-21** | *** |
| **Education: graduate level (vs college)** | **-9.3231** | 2.8462 | ±5.6924 | **-3.276** | **0.0011** | ** |
| Education: high school or below (vs college) | +1.2405 | 3.9743 | ±7.9486 | +0.312 | 0.7549 |  |
| Site: UCSD (vs UAB) | +1.7274 | 3.5415 | ±7.0830 | +0.488 | 0.6257 |  |
| Site: UW (vs UAB) | +0.4032 | 2.9787 | ±5.9574 | +0.135 | 0.8923 |  |
| Season: spring (vs autumn) | +2.8472 | 3.5516 | ±7.1033 | +0.802 | 0.4228 |  |
| Season: summer (vs autumn) | +1.8096 | 3.5175 | ±7.0349 | +0.514 | 0.6069 |  |
| **Season: winter (vs autumn)** | **+9.7236** | 4.5163 | ±9.0326 | **+2.153** | **0.0313** | * |
| Age (years) | -0.0563 | 0.1385 | ±0.2769 | -0.407 | 0.6842 |  |
| BMI (kg/m2) | +0.1752 | 0.1826 | ±0.3652 | +0.959 | 0.3374 |  |
| Hypertension | -2.5429 | 3.3151 | ±6.6303 | -0.767 | 0.4430 |  |
| High cholesterol | +2.3791 | 3.1086 | ±6.2172 | +0.765 | 0.4441 |  |
| Kidney disease | +1.1862 | 3.9400 | ±7.8800 | +0.301 | 0.7634 |  |
| Circulatory disease | -4.1870 | 3.5457 | ±7.0914 | -1.181 | 0.2377 |  |
| Time 181-250, pooled (%) | +0.0632 | 0.1898 | ±0.3797 | +0.333 | 0.7391 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.1060**, Adj R² = **0.0472**, F-statistic = **1.80** (p = **0.0396**), Residual SE = **19.127** on **213** df, AIC = **2007.2**, BIC = **2058.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7445** | 12.9026 | ±25.8052 | **+9.668** | **4.12e-22** | *** |
| **Education: graduate level (vs college)** | **-9.3821** | 2.8553 | ±5.7106 | **-3.286** | **0.0010** | ** |
| Education: high school or below (vs college) | +1.2672 | 3.9768 | ±7.9537 | +0.319 | 0.7500 |  |
| Site: UCSD (vs UAB) | +1.7383 | 3.5356 | ±7.0712 | +0.492 | 0.6230 |  |
| Site: UW (vs UAB) | +0.4288 | 2.9528 | ±5.9055 | +0.145 | 0.8845 |  |
| Season: spring (vs autumn) | +2.9324 | 3.5315 | ±7.0630 | +0.830 | 0.4063 |  |
| Season: summer (vs autumn) | +1.8522 | 3.5146 | ±7.0292 | +0.527 | 0.5982 |  |
| **Season: winter (vs autumn)** | **+9.8486** | 4.5350 | ±9.0701 | **+2.172** | **0.0299** | * |
| Age (years) | -0.0532 | 0.1354 | ±0.2708 | -0.393 | 0.6943 |  |
| BMI (kg/m2) | +0.1741 | 0.1823 | ±0.3647 | +0.955 | 0.3396 |  |
| Hypertension | -2.5503 | 3.3135 | ±6.6270 | -0.770 | 0.4415 |  |
| High cholesterol | +2.4038 | 3.1185 | ±6.2371 | +0.771 | 0.4408 |  |
| Kidney disease | +1.3350 | 3.9089 | ±7.8178 | +0.342 | 0.7327 |  |
| Circulatory disease | -4.1579 | 3.5394 | ±7.0787 | -1.175 | 0.2401 |  |
| Avg. daily time 181-250 (%) | +0.0388 | 0.1777 | ±0.3553 | +0.218 | 0.8271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.1077**, Adj R² = **0.0491**, F-statistic = **1.84** (p = **0.0350**), Residual SE = **19.108** on **213** df, AIC = **2006.8**, BIC = **2058.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5730** | 12.8826 | ±25.7652 | **+9.747** | **1.89e-22** | *** |
| **Education: graduate level (vs college)** | **-9.6926** | 2.8505 | ±5.7010 | **-3.400** | **6.73e-04** | *** |
| Education: high school or below (vs college) | +1.5321 | 4.0718 | ±8.1437 | +0.376 | 0.7067 |  |
| Site: UCSD (vs UAB) | +1.6959 | 3.5697 | ±7.1394 | +0.475 | 0.6347 |  |
| Site: UW (vs UAB) | +0.3232 | 2.9550 | ±5.9100 | +0.109 | 0.9129 |  |
| Season: spring (vs autumn) | +3.3104 | 3.4686 | ±6.9372 | +0.954 | 0.3399 |  |
| Season: summer (vs autumn) | +1.8453 | 3.4849 | ±6.9698 | +0.530 | 0.5965 |  |
| **Season: winter (vs autumn)** | **+10.3717** | 4.5457 | ±9.0915 | **+2.282** | **0.0225** | * |
| Age (years) | -0.0466 | 0.1328 | ±0.2656 | -0.351 | 0.7256 |  |
| BMI (kg/m2) | +0.1655 | 0.1794 | ±0.3587 | +0.922 | 0.3563 |  |
| Hypertension | -2.5558 | 3.3857 | ±6.7715 | -0.755 | 0.4503 |  |
| High cholesterol | +2.4095 | 3.1740 | ±6.3479 | +0.759 | 0.4478 |  |
| Kidney disease | +2.0091 | 3.8421 | ±7.6842 | +0.523 | 0.6010 |  |
| Circulatory disease | -4.0014 | 3.4868 | ±6.9737 | -1.148 | 0.2511 |  |
| Time > 180 (%) | -0.0534 | 0.1268 | ±0.2536 | -0.421 | 0.6737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1085**, Adj R² = **0.0500**, F-statistic = **1.85** (p = **0.0331**), Residual SE = **19.100** on **213** df, AIC = **2006.6**, BIC = **2058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7103** | 12.8646 | ±25.7292 | **+9.772** | **1.49e-22** | *** |
| **Education: graduate level (vs college)** | **-9.7220** | 2.8582 | ±5.7164 | **-3.401** | **6.70e-04** | *** |
| Education: high school or below (vs college) | +1.5871 | 4.0765 | ±8.1531 | +0.389 | 0.6970 |  |
| Site: UCSD (vs UAB) | +1.6794 | 3.5709 | ±7.1418 | +0.470 | 0.6381 |  |
| Site: UW (vs UAB) | +0.2966 | 2.9507 | ±5.9015 | +0.101 | 0.9199 |  |
| Season: spring (vs autumn) | +3.3747 | 3.4847 | ±6.9694 | +0.968 | 0.3328 |  |
| Season: summer (vs autumn) | +1.8579 | 3.4912 | ±6.9825 | +0.532 | 0.5946 |  |
| **Season: winter (vs autumn)** | **+10.4581** | 4.5337 | ±9.0674 | **+2.307** | **0.0211** | * |
| Age (years) | -0.0466 | 0.1324 | ±0.2648 | -0.352 | 0.7250 |  |
| BMI (kg/m2) | +0.1634 | 0.1786 | ±0.3571 | +0.915 | 0.3601 |  |
| Hypertension | -2.5638 | 3.3852 | ±6.7703 | -0.757 | 0.4488 |  |
| High cholesterol | +2.4137 | 3.1711 | ±6.3422 | +0.761 | 0.4466 |  |
| Kidney disease | +2.1005 | 3.8270 | ±7.6541 | +0.549 | 0.5831 |  |
| Circulatory disease | -3.9749 | 3.4825 | ±6.9650 | -1.141 | 0.2537 |  |
| Avg. daily time > 180 (%) | -0.0623 | 0.1284 | ±0.2567 | -0.485 | 0.6274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1116**, Adj R² = **0.0532**, F-statistic = **1.91** (p = **0.0267**), Residual SE = **19.067** on **213** df, AIC = **2005.8**, BIC = **2057.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.9274** | 13.0102 | ±26.0204 | **+9.679** | **3.70e-22** | *** |
| **Education: graduate level (vs college)** | **-9.7875** | 2.8427 | ±5.6855 | **-3.443** | **5.75e-04** | *** |
| Education: high school or below (vs college) | +1.5154 | 4.0173 | ±8.0345 | +0.377 | 0.7060 |  |
| Site: UCSD (vs UAB) | +1.6526 | 3.6178 | ±7.2356 | +0.457 | 0.6478 |  |
| Site: UW (vs UAB) | +0.2710 | 2.9609 | ±5.9219 | +0.092 | 0.9271 |  |
| Season: spring (vs autumn) | +3.3962 | 3.4614 | ±6.9227 | +0.981 | 0.3265 |  |
| Season: summer (vs autumn) | +1.6230 | 3.4555 | ±6.9111 | +0.470 | 0.6386 |  |
| **Season: winter (vs autumn)** | **+10.5489** | 4.5404 | ±9.0808 | **+2.323** | **0.0202** | * |
| Age (years) | -0.0524 | 0.1283 | ±0.2565 | -0.409 | 0.6827 |  |
| BMI (kg/m2) | +0.1646 | 0.1820 | ±0.3641 | +0.904 | 0.3658 |  |
| Hypertension | -2.3843 | 3.4703 | ±6.9406 | -0.687 | 0.4920 |  |
| High cholesterol | +2.4992 | 3.1787 | ±6.3574 | +0.786 | 0.4317 |  |
| Kidney disease | +1.8574 | 3.7453 | ±7.4907 | +0.496 | 0.6199 |  |
| Circulatory disease | -3.8314 | 3.4371 | ±6.8742 | -1.115 | 0.2650 |  |
| Nocturnal time > 180 (%) | -0.0875 | 0.1545 | ±0.3090 | -0.566 | 0.5713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1094**, Adj R² = **0.0509**, F-statistic = **1.87** (p = **0.0312**), Residual SE = **19.091** on **213** df, AIC = **2006.4**, BIC = **2057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.3128** | 12.8941 | ±25.7883 | **+9.641** | **5.36e-22** | *** |
| **Education: graduate level (vs college)** | **-9.1590** | 2.9271 | ±5.8542 | **-3.129** | **0.0018** | ** |
| Education: high school or below (vs college) | +1.0558 | 3.9112 | ±7.8224 | +0.270 | 0.7872 |  |
| Site: UCSD (vs UAB) | +1.7470 | 3.5158 | ±7.0317 | +0.497 | 0.6193 |  |
| Site: UW (vs UAB) | +0.1968 | 3.0257 | ±6.0513 | +0.065 | 0.9481 |  |
| Season: spring (vs autumn) | +2.8239 | 3.4864 | ±6.9728 | +0.810 | 0.4179 |  |
| Season: summer (vs autumn) | +1.7148 | 3.4991 | ±6.9983 | +0.490 | 0.6241 |  |
| **Season: winter (vs autumn)** | **+9.9989** | 4.8063 | ±9.6126 | **+2.080** | **0.0375** | * |
| Age (years) | -0.0700 | 0.1348 | ±0.2696 | -0.519 | 0.6037 |  |
| BMI (kg/m2) | +0.1915 | 0.1780 | ±0.3559 | +1.076 | 0.2818 |  |
| Hypertension | -2.6195 | 3.3040 | ±6.6080 | -0.793 | 0.4279 |  |
| High cholesterol | +2.5529 | 3.1452 | ±6.2904 | +0.812 | 0.4170 |  |
| Kidney disease | +0.8939 | 3.8302 | ±7.6604 | +0.233 | 0.8155 |  |
| Circulatory disease | -4.1835 | 3.5225 | ±7.0451 | -1.188 | 0.2350 |  |
| Any reading > 250 during wear (0/1) | +2.6199 | 2.9014 | ±5.8027 | +0.903 | 0.3665 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1275**, Adj R² = **0.0702**, F-statistic = **2.22** (p = **0.0080**), Residual SE = **18.895** on **213** df, AIC = **2001.7**, BIC = **2053.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4395** | 13.0547 | ±26.1093 | **+9.762** | **1.64e-22** | *** |
| **Education: graduate level (vs college)** | **-10.0370** | 2.9333 | ±5.8666 | **-3.422** | **6.22e-04** | *** |
| Education: high school or below (vs college) | +2.1700 | 4.0975 | ±8.1950 | +0.530 | 0.5964 |  |
| Site: UCSD (vs UAB) | +1.6352 | 3.5244 | ±7.0487 | +0.464 | 0.6427 |  |
| Site: UW (vs UAB) | -0.1738 | 3.0296 | ±6.0592 | -0.057 | 0.9542 |  |
| Season: spring (vs autumn) | +3.5473 | 3.3864 | ±6.7727 | +1.048 | 0.2949 |  |
| Season: summer (vs autumn) | +1.1171 | 3.4391 | ±6.8782 | +0.325 | 0.7453 |  |
| **Season: winter (vs autumn)** | **+10.3588** | 4.7100 | ±9.4199 | **+2.199** | **0.0279** | * |
| Age (years) | -0.0595 | 0.1257 | ±0.2514 | -0.474 | 0.6357 |  |
| BMI (kg/m2) | +0.1493 | 0.1776 | ±0.3552 | +0.841 | 0.4006 |  |
| Hypertension | -2.2584 | 3.3487 | ±6.6973 | -0.674 | 0.5000 |  |
| High cholesterol | +1.9408 | 3.0778 | ±6.1556 | +0.631 | 0.5283 |  |
| Kidney disease | +2.1809 | 3.7721 | ±7.5442 | +0.578 | 0.5631 |  |
| Circulatory disease | -3.7169 | 3.3515 | ±6.7030 | -1.109 | 0.2674 |  |
| Time > 250 (%) | -0.3334 | 0.2874 | ±0.5749 | -1.160 | 0.2461 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1321**, Adj R² = **0.0751**, F-statistic = **2.32** (p = **0.0055**), Residual SE = **18.846** on **213** df, AIC = **2000.5**, BIC = **2051.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4828** | 13.0901 | ±26.1802 | **+9.739** | **2.06e-22** | *** |
| **Education: graduate level (vs college)** | **-10.1228** | 2.9369 | ±5.8738 | **-3.447** | **5.67e-04** | *** |
| Education: high school or below (vs college) | +2.4316 | 4.1102 | ±8.2204 | +0.592 | 0.5541 |  |
| Site: UCSD (vs UAB) | +1.6876 | 3.5049 | ±7.0099 | +0.481 | 0.6302 |  |
| Site: UW (vs UAB) | -0.1454 | 3.0216 | ±6.0432 | -0.048 | 0.9616 |  |
| Season: spring (vs autumn) | +3.8513 | 3.3975 | ±6.7950 | +1.134 | 0.2570 |  |
| Season: summer (vs autumn) | +1.1734 | 3.4181 | ±6.8362 | +0.343 | 0.7314 |  |
| **Season: winter (vs autumn)** | **+10.6377** | 4.6488 | ±9.2976 | **+2.288** | **0.0221** | * |
| Age (years) | -0.0574 | 0.1267 | ±0.2535 | -0.453 | 0.6505 |  |
| BMI (kg/m2) | +0.1400 | 0.1759 | ±0.3518 | +0.796 | 0.4259 |  |
| Hypertension | -2.1981 | 3.3473 | ±6.6946 | -0.657 | 0.5114 |  |
| High cholesterol | +1.9051 | 3.0718 | ±6.1436 | +0.620 | 0.5351 |  |
| Kidney disease | +2.4105 | 3.7505 | ±7.5010 | +0.643 | 0.5204 |  |
| Circulatory disease | -3.5428 | 3.3208 | ±6.6417 | -1.067 | 0.2860 |  |
| Avg. daily time > 250 (%) | -0.4090 | 0.3297 | ±0.6595 | -1.240 | 0.2148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 201; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1626**, F-statistic = **4.88** (p = **2.84e-06**), Residual SE = **4756.056** on **190** df, AIC = **3984.9**, BIC = **4021.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20913.1172** | 2797.8902 | ±5595.7803 | **+7.475** | **7.74e-14** | *** |
| Education: graduate level (vs college) | -1113.8693 | 736.7843 | ±1473.5687 | -1.512 | 0.1306 |  |
| Education: high school or below (vs college) | +666.7229 | 1129.7943 | ±2259.5887 | +0.590 | 0.5551 |  |
| Site: UCSD (vs UAB) | +290.4919 | 886.1215 | ±1772.2431 | +0.328 | 0.7430 |  |
| Site: UW (vs UAB) | +1042.5665 | 847.1455 | ±1694.2910 | +1.231 | 0.2184 |  |
| **Age (years)** | **-164.2027** | 31.3096 | ±62.6193 | **-5.244** | **1.57e-07** | *** |
| BMI (kg/m2) | -22.6211 | 47.3429 | ±94.6858 | -0.478 | 0.6328 |  |
| Hypertension | -449.9293 | 838.8805 | ±1677.7611 | -0.536 | 0.5917 |  |
| High cholesterol | +7.2580 | 794.7577 | ±1589.5154 | +0.009 | 0.9927 |  |
| Kidney disease | -1466.4636 | 919.1859 | ±1838.3718 | -1.595 | 0.1106 |  |
| **Circulatory disease** | **-1513.4648** | 671.8725 | ±1343.7450 | **-2.253** | **0.0243** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **201**, R² = **0.2123**, Adj R² = **0.1664**, F-statistic = **4.63** (p = **3.05e-06**), Residual SE = **4745.194** on **189** df, AIC = **3984.9**, BIC = **4024.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18750.9526** | 3597.4392 | ±7194.8783 | **+5.212** | **1.87e-07** | *** |
| Education: graduate level (vs college) | -976.6086 | 777.5427 | ±1555.0855 | -1.256 | 0.2091 |  |
| Education: high school or below (vs college) | +572.7467 | 1113.9227 | ±2227.8455 | +0.514 | 0.6071 |  |
| Site: UCSD (vs UAB) | +354.3065 | 881.5196 | ±1763.0391 | +0.402 | 0.6877 |  |
| Site: UW (vs UAB) | +1086.5417 | 855.8674 | ±1711.7348 | +1.270 | 0.2043 |  |
| **Age (years)** | **-171.9589** | 31.7109 | ±63.4217 | **-5.423** | **5.87e-08** | *** |
| BMI (kg/m2) | -25.2924 | 47.0925 | ±94.1850 | -0.537 | 0.5912 |  |
| Hypertension | -454.8998 | 840.8210 | ±1681.6420 | -0.541 | 0.5885 |  |
| High cholesterol | +35.2516 | 785.7152 | ±1571.4303 | +0.045 | 0.9642 |  |
| Kidney disease | -1473.1461 | 878.7037 | ±1757.4074 | -1.676 | 0.0936 | . |
| **Circulatory disease** | **-1499.7883** | 670.6228 | ±1341.2457 | **-2.236** | **0.0253** | * |
| HbA1c (%) | +413.2523 | 405.2215 | ±810.4430 | +1.020 | 0.3078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **201**, R² = **0.2053**, Adj R² = **0.1590**, F-statistic = **4.44** (p = **6.09e-06**), Residual SE = **4766.149** on **189** df, AIC = **3986.7**, BIC = **4026.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21530.9975** | 3451.6966 | ±6903.3931 | **+6.238** | **4.44e-10** | *** |
| Education: graduate level (vs college) | -1132.5031 | 745.9701 | ±1491.9401 | -1.518 | 0.1290 |  |
| Education: high school or below (vs college) | +690.6101 | 1132.2873 | ±2264.5746 | +0.610 | 0.5419 |  |
| Site: UCSD (vs UAB) | +288.5004 | 898.3152 | ±1796.6304 | +0.321 | 0.7481 |  |
| Site: UW (vs UAB) | +1031.4840 | 853.1697 | ±1706.3394 | +1.209 | 0.2267 |  |
| **Age (years)** | **-163.7911** | 31.2783 | ±62.5566 | **-5.237** | **1.64e-07** | *** |
| BMI (kg/m2) | -22.7728 | 47.4378 | ±94.8757 | -0.480 | 0.6312 |  |
| Hypertension | -454.2907 | 841.3928 | ±1682.7856 | -0.540 | 0.5892 |  |
| High cholesterol | +8.6508 | 799.2567 | ±1598.5134 | +0.011 | 0.9914 |  |
| Kidney disease | -1427.2896 | 927.2261 | ±1854.4522 | -1.539 | 0.1237 |  |
| **Circulatory disease** | **-1502.3347** | 680.2028 | ±1360.4055 | **-2.209** | **0.0272** | * |
| Mean glucose (mg/dL) | -4.6827 | 10.9951 | ±21.9901 | -0.426 | 0.6702 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **201**, R² = **0.2053**, Adj R² = **0.1590**, F-statistic = **4.44** (p = **6.09e-06**), Residual SE = **4766.149** on **189** df, AIC = **3986.7**, BIC = **4026.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22178.9733** | 4548.5593 | ±9097.1185 | **+4.876** | **1.08e-06** | *** |
| Education: graduate level (vs college) | -1132.5031 | 745.9701 | ±1491.9401 | -1.518 | 0.1290 |  |
| Education: high school or below (vs college) | +690.6101 | 1132.2873 | ±2264.5746 | +0.610 | 0.5419 |  |
| Site: UCSD (vs UAB) | +288.5004 | 898.3152 | ±1796.6304 | +0.321 | 0.7481 |  |
| Site: UW (vs UAB) | +1031.4840 | 853.1697 | ±1706.3394 | +1.209 | 0.2267 |  |
| **Age (years)** | **-163.7911** | 31.2783 | ±62.5566 | **-5.237** | **1.64e-07** | *** |
| BMI (kg/m2) | -22.7728 | 47.4378 | ±94.8757 | -0.480 | 0.6312 |  |
| Hypertension | -454.2907 | 841.3928 | ±1682.7856 | -0.540 | 0.5892 |  |
| High cholesterol | +8.6508 | 799.2567 | ±1598.5134 | +0.011 | 0.9914 |  |
| Kidney disease | -1427.2896 | 927.2261 | ±1854.4522 | -1.539 | 0.1237 |  |
| **Circulatory disease** | **-1502.3347** | 680.2028 | ±1360.4055 | **-2.209** | **0.0272** | * |
| GMI (%) | -195.7631 | 459.6596 | ±919.3192 | -0.426 | 0.6702 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.60e-06**), Residual SE = **4768.616** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20884.7376** | 3391.1451 | ±6782.2901 | **+6.159** | **7.34e-10** | *** |
| Education: graduate level (vs college) | -1113.7216 | 739.9618 | ±1479.9237 | -1.505 | 0.1323 |  |
| Education: high school or below (vs college) | +665.6103 | 1133.8174 | ±2267.6349 | +0.587 | 0.5572 |  |
| Site: UCSD (vs UAB) | +290.2894 | 889.8858 | ±1779.7716 | +0.326 | 0.7443 |  |
| Site: UW (vs UAB) | +1042.7546 | 850.4843 | ±1700.9687 | +1.226 | 0.2202 |  |
| **Age (years)** | **-164.1744** | 31.7120 | ±63.4239 | **-5.177** | **2.25e-07** | *** |
| BMI (kg/m2) | -22.6357 | 47.4391 | ±94.8783 | -0.477 | 0.6333 |  |
| Hypertension | -450.4046 | 844.5558 | ±1689.1116 | -0.533 | 0.5938 |  |
| High cholesterol | +6.9313 | 800.2624 | ±1600.5248 | +0.009 | 0.9931 |  |
| Kidney disease | -1466.9155 | 923.8434 | ±1847.6868 | -1.588 | 0.1123 |  |
| **Circulatory disease** | **-1514.1243** | 680.1977 | ±1360.3953 | **-2.226** | **0.0260** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.2134 | 10.5165 | ±21.0330 | +0.020 | 0.9838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2086**, Adj R² = **0.1626**, F-statistic = **4.53** (p = **4.39e-06**), Residual SE = **4756.192** on **189** df, AIC = **3985.9**, BIC = **4025.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21410.6696** | 2906.6588 | ±5813.3176 | **+7.366** | **1.76e-13** | *** |
| Education: graduate level (vs college) | -1218.6975 | 749.8228 | ±1499.6455 | -1.625 | 0.1041 |  |
| Education: high school or below (vs college) | +807.6093 | 1121.5160 | ±2243.0321 | +0.720 | 0.4715 |  |
| Site: UCSD (vs UAB) | +266.2295 | 901.3911 | ±1802.7822 | +0.295 | 0.7677 |  |
| Site: UW (vs UAB) | +996.2267 | 853.8541 | ±1707.7083 | +1.167 | 0.2433 |  |
| **Age (years)** | **-158.2332** | 31.5096 | ±63.0191 | **-5.022** | **5.12e-07** | *** |
| BMI (kg/m2) | -24.7991 | 47.6630 | ±95.3260 | -0.520 | 0.6029 |  |
| Hypertension | -470.7782 | 836.4406 | ±1672.8811 | -0.563 | 0.5735 |  |
| High cholesterol | +3.5531 | 797.6601 | ±1595.3202 | +0.004 | 0.9964 |  |
| Kidney disease | -1257.1407 | 927.8631 | ±1855.7262 | -1.355 | 0.1755 |  |
| **Circulatory disease** | **-1529.3293** | 679.4907 | ±1358.9814 | **-2.251** | **0.0244** | * |
| Glucose SD, pooled (mg/dL) | -22.6556 | 21.6716 | ±43.3433 | -1.045 | 0.2958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2110**, Adj R² = **0.1650**, F-statistic = **4.59** (p = **3.48e-06**), Residual SE = **4749.131** on **189** df, AIC = **3985.3**, BIC = **4024.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21612.3684** | 2916.1222 | ±5832.2444 | **+7.411** | **1.25e-13** | *** |
| Education: graduate level (vs college) | -1248.8566 | 750.0801 | ±1500.1602 | -1.665 | 0.0959 | . |
| Education: high school or below (vs college) | +878.5664 | 1114.8620 | ±2229.7239 | +0.788 | 0.4307 |  |
| Site: UCSD (vs UAB) | +252.8481 | 901.6362 | ±1803.2723 | +0.280 | 0.7791 |  |
| Site: UW (vs UAB) | +995.2793 | 850.2763 | ±1700.5526 | +1.171 | 0.2418 |  |
| **Age (years)** | **-156.8010** | 31.0894 | ±62.1787 | **-5.044** | **4.57e-07** | *** |
| BMI (kg/m2) | -26.5422 | 47.6605 | ±95.3209 | -0.557 | 0.5776 |  |
| Hypertension | -489.6443 | 835.2279 | ±1670.4559 | -0.586 | 0.5577 |  |
| High cholesterol | +18.2285 | 794.9810 | ±1589.9621 | +0.023 | 0.9817 |  |
| Kidney disease | -1201.5965 | 932.8987 | ±1865.7974 | -1.288 | 0.1977 |  |
| **Circulatory disease** | **-1543.1541** | 678.1181 | ±1356.2362 | **-2.276** | **0.0229** | * |
| Avg. daily SD (mg/dL) | -33.5755 | 24.0278 | ±48.0556 | -1.397 | 0.1623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **201**, R² = **0.2082**, Adj R² = **0.1622**, F-statistic = **4.52** (p = **4.55e-06**), Residual SE = **4757.290** on **189** df, AIC = **3985.9**, BIC = **4025.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21674.6713** | 2905.6951 | ±5811.3901 | **+7.459** | **8.69e-14** | *** |
| Education: graduate level (vs college) | -1239.9993 | 746.2879 | ±1492.5758 | -1.662 | 0.0966 | . |
| Education: high school or below (vs college) | +846.5928 | 1124.1222 | ±2248.2444 | +0.753 | 0.4514 |  |
| Site: UCSD (vs UAB) | +274.4087 | 890.1384 | ±1780.2768 | +0.308 | 0.7579 |  |
| Site: UW (vs UAB) | +994.6782 | 855.4078 | ±1710.8156 | +1.163 | 0.2449 |  |
| **Age (years)** | **-154.6823** | 33.2210 | ±66.4420 | **-4.656** | **3.22e-06** | *** |
| BMI (kg/m2) | -25.3099 | 48.0422 | ±96.0844 | -0.527 | 0.5983 |  |
| Hypertension | -477.6368 | 836.9363 | ±1673.8727 | -0.571 | 0.5682 |  |
| High cholesterol | +9.7671 | 797.2985 | ±1594.5970 | +0.012 | 0.9902 |  |
| Kidney disease | -1225.2981 | 935.8356 | ±1871.6711 | -1.309 | 0.1904 |  |
| **Circulatory disease** | **-1547.6238** | 679.5725 | ±1359.1450 | **-2.277** | **0.0228** | * |
| CV (%) | -50.8979 | 46.6975 | ±93.3950 | -1.090 | 0.2757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.59e-06**), Residual SE = **4768.568** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20795.5306** | 3237.7793 | ±6475.5585 | **+6.423** | **1.34e-10** | *** |
| Education: graduate level (vs college) | -1121.9369 | 751.0894 | ±1502.1787 | -1.494 | 0.1352 |  |
| Education: high school or below (vs college) | +679.3662 | 1131.3028 | ±2262.6056 | +0.601 | 0.5482 |  |
| Site: UCSD (vs UAB) | +291.8479 | 888.9467 | ±1777.8933 | +0.328 | 0.7427 |  |
| Site: UW (vs UAB) | +1041.0050 | 853.0599 | ±1706.1197 | +1.220 | 0.2223 |  |
| **Age (years)** | **-163.5184** | 33.4444 | ±66.8889 | **-4.889** | **1.01e-06** | *** |
| BMI (kg/m2) | -22.6934 | 47.6989 | ±95.3979 | -0.476 | 0.6342 |  |
| Hypertension | -452.4183 | 839.6556 | ±1679.3112 | -0.539 | 0.5900 |  |
| High cholesterol | +7.3216 | 797.8162 | ±1595.6325 | +0.009 | 0.9927 |  |
| Kidney disease | -1455.3805 | 941.7194 | ±1883.4389 | -1.545 | 0.1222 |  |
| **Circulatory disease** | **-1512.8772** | 674.5596 | ±1349.1192 | **-2.243** | **0.0249** | * |
| Mean / SD ratio | +17.5600 | 233.7308 | ±467.4616 | +0.075 | 0.9401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.59e-06**), Residual SE = **4768.566** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20797.3123** | 3202.9577 | ±6405.9153 | **+6.493** | **8.41e-11** | *** |
| Education: graduate level (vs college) | -1122.5515 | 747.6938 | ±1495.3877 | -1.501 | 0.1333 |  |
| Education: high school or below (vs college) | +679.7184 | 1120.4898 | ±2240.9796 | +0.607 | 0.5441 |  |
| Site: UCSD (vs UAB) | +292.6101 | 889.0494 | ±1778.0988 | +0.329 | 0.7421 |  |
| Site: UW (vs UAB) | +1042.3019 | 849.8156 | ±1699.6311 | +1.227 | 0.2200 |  |
| **Age (years)** | **-163.5096** | 33.2880 | ±66.5760 | **-4.912** | **9.02e-07** | *** |
| BMI (kg/m2) | -22.7474 | 47.6783 | ±95.3566 | -0.477 | 0.6333 |  |
| Hypertension | -453.6397 | 839.9143 | ±1679.8287 | -0.540 | 0.5891 |  |
| High cholesterol | +9.1265 | 799.8298 | ±1599.6596 | +0.011 | 0.9909 |  |
| Kidney disease | -1458.9358 | 934.3760 | ±1868.7520 | -1.561 | 0.1184 |  |
| **Circulatory disease** | **-1513.5460** | 674.1695 | ±1348.3390 | **-2.245** | **0.0248** | * |
| Avg. daily mean/SD | +14.7017 | 179.4812 | ±358.9625 | +0.082 | 0.9347 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **201**, R² = **0.2050**, Adj R² = **0.1587**, F-statistic = **4.43** (p = **6.27e-06**), Residual SE = **4767.063** on **189** df, AIC = **3986.8**, BIC = **4026.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20530.7174** | 3184.5984 | ±6369.1967 | **+6.447** | **1.14e-10** | *** |
| Education: graduate level (vs college) | -1085.8953 | 748.5260 | ±1497.0520 | -1.451 | 0.1469 |  |
| Education: high school or below (vs college) | +613.1487 | 1130.5464 | ±2261.0929 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | +278.7103 | 885.3691 | ±1770.7382 | +0.315 | 0.7529 |  |
| Site: UW (vs UAB) | +1070.6188 | 858.0461 | ±1716.0922 | +1.248 | 0.2121 |  |
| **Age (years)** | **-165.3058** | 31.4475 | ±62.8950 | **-5.257** | **1.47e-07** | *** |
| BMI (kg/m2) | -24.0653 | 47.3402 | ±94.6803 | -0.508 | 0.6112 |  |
| Hypertension | -433.9506 | 846.5063 | ±1693.0127 | -0.513 | 0.6082 |  |
| High cholesterol | -5.3608 | 803.7705 | ±1607.5409 | -0.007 | 0.9947 |  |
| Kidney disease | -1474.8780 | 925.5948 | ±1851.1896 | -1.593 | 0.1111 |  |
| **Circulatory disease** | **-1511.8332** | 675.9824 | ±1351.9648 | **-2.236** | **0.0253** | * |
| MAG (mg/dL/h) | +10.9812 | 35.1384 | ±70.2767 | +0.313 | 0.7547 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **201**, R² = **0.2077**, Adj R² = **0.1616**, F-statistic = **4.50** (p = **4.80e-06**), Residual SE = **4758.885** on **189** df, AIC = **3986.1**, BIC = **4025.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21621.3742** | 3036.8808 | ±6073.7616 | **+7.120** | **1.08e-12** | *** |
| Education: graduate level (vs college) | -1213.4720 | 752.6429 | ±1505.2857 | -1.612 | 0.1069 |  |
| Education: high school or below (vs college) | +833.0049 | 1121.0632 | ±2242.1263 | +0.743 | 0.4575 |  |
| Site: UCSD (vs UAB) | +280.0490 | 900.3161 | ±1800.6322 | +0.311 | 0.7558 |  |
| Site: UW (vs UAB) | +1019.9341 | 852.1492 | ±1704.2983 | +1.197 | 0.2313 |  |
| **Age (years)** | **-159.2985** | 31.2337 | ±62.4675 | **-5.100** | **3.39e-07** | *** |
| BMI (kg/m2) | -25.4830 | 47.9695 | ±95.9390 | -0.531 | 0.5953 |  |
| Hypertension | -492.7041 | 838.3883 | ±1676.7766 | -0.588 | 0.5567 |  |
| High cholesterol | +30.3793 | 798.5465 | ±1597.0929 | +0.038 | 0.9697 |  |
| Kidney disease | -1280.8065 | 932.0497 | ±1864.0993 | -1.374 | 0.1694 |  |
| **Circulatory disease** | **-1513.2314** | 675.8136 | ±1351.6272 | **-2.239** | **0.0251** | * |
| Avg. daily range (mg/dL) | -6.7043 | 7.3827 | ±14.7654 | -0.908 | 0.3638 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.58e-06**), Residual SE = **4768.520** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20889.2901** | 2853.2323 | ±5706.4645 | **+7.321** | **2.46e-13** | *** |
| Education: graduate level (vs college) | -1104.2799 | 761.0679 | ±1522.1358 | -1.451 | 0.1468 |  |
| Education: high school or below (vs college) | +666.1455 | 1141.4003 | ±2282.8006 | +0.584 | 0.5595 |  |
| Site: UCSD (vs UAB) | +290.5192 | 890.5152 | ±1781.0305 | +0.326 | 0.7442 |  |
| Site: UW (vs UAB) | +1047.0358 | 859.2254 | ±1718.4507 | +1.219 | 0.2230 |  |
| **Age (years)** | **-164.5160** | 31.6596 | ±63.3191 | **-5.196** | **2.03e-07** | *** |
| BMI (kg/m2) | -22.5227 | 47.8007 | ±95.6014 | -0.471 | 0.6375 |  |
| Hypertension | -453.8495 | 847.5509 | ±1695.1018 | -0.535 | 0.5923 |  |
| High cholesterol | +9.0747 | 796.8351 | ±1593.6702 | +0.011 | 0.9909 |  |
| Kidney disease | -1479.1445 | 913.5150 | ±1827.0300 | -1.619 | 0.1054 |  |
| **Circulatory disease** | **-1517.3404** | 680.8192 | ±1361.6383 | **-2.229** | **0.0258** | * |
| SD of daily means (mg/dL) | +3.2154 | 38.8064 | ±77.6128 | +0.083 | 0.9340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **201**, R² = **0.2084**, Adj R² = **0.1623**, F-statistic = **4.52** (p = **4.48e-06**), Residual SE = **4756.832** on **189** df, AIC = **3985.9**, BIC = **4025.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19298.6638** | 2868.8442 | ±5737.6885 | **+6.727** | **1.73e-11** | *** |
| Education: graduate level (vs college) | -1219.1405 | 751.7105 | ±1503.4210 | -1.622 | 0.1048 |  |
| Education: high school or below (vs college) | +714.6270 | 1134.0984 | ±2268.1968 | +0.630 | 0.5286 |  |
| Site: UCSD (vs UAB) | +257.9336 | 916.8806 | ±1833.7612 | +0.281 | 0.7785 |  |
| Site: UW (vs UAB) | +1001.4285 | 850.4539 | ±1700.9079 | +1.178 | 0.2390 |  |
| **Age (years)** | **-161.5154** | 31.1029 | ±62.2058 | **-5.193** | **2.07e-07** | *** |
| BMI (kg/m2) | -24.2342 | 47.8066 | ±95.6133 | -0.507 | 0.6122 |  |
| Hypertension | -486.1864 | 835.7017 | ±1671.4035 | -0.582 | 0.5607 |  |
| High cholesterol | +43.9041 | 801.2378 | ±1602.4756 | +0.055 | 0.9563 |  |
| Kidney disease | -1329.0129 | 930.7488 | ±1861.4977 | -1.428 | 0.1533 |  |
| **Circulatory disease** | **-1468.3155** | 680.9181 | ±1361.8363 | **-2.156** | **0.0311** | * |
| Time in range 70-180, pooled (%) | +18.2531 | 18.7856 | ±37.5712 | +0.972 | 0.3312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **201**, R² = **0.2083**, Adj R² = **0.1622**, F-statistic = **4.52** (p = **4.54e-06**), Residual SE = **4757.201** on **189** df, AIC = **3985.9**, BIC = **4025.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19335.0557** | 2891.8769 | ±5783.7539 | **+6.686** | **2.29e-11** | *** |
| Education: graduate level (vs college) | -1216.8282 | 750.6604 | ±1501.3209 | -1.621 | 0.1050 |  |
| Education: high school or below (vs college) | +722.8742 | 1134.9669 | ±2269.9338 | +0.637 | 0.5242 |  |
| Site: UCSD (vs UAB) | +253.7790 | 916.5398 | ±1833.0795 | +0.277 | 0.7819 |  |
| Site: UW (vs UAB) | +998.7071 | 850.6861 | ±1701.3722 | +1.174 | 0.2404 |  |
| **Age (years)** | **-161.6069** | 31.1292 | ±62.2583 | **-5.191** | **2.09e-07** | *** |
| BMI (kg/m2) | -24.5908 | 47.8197 | ±95.6394 | -0.514 | 0.6071 |  |
| Hypertension | -489.9613 | 836.0872 | ±1672.1743 | -0.586 | 0.5579 |  |
| High cholesterol | +44.8226 | 802.6378 | ±1605.2756 | +0.056 | 0.9555 |  |
| Kidney disease | -1327.8548 | 929.1313 | ±1858.2626 | -1.429 | 0.1530 |  |
| **Circulatory disease** | **-1465.9887** | 681.1666 | ±1362.3332 | **-2.152** | **0.0314** | * |
| Avg. daily time in range 70-180 (%) | +17.9517 | 18.7947 | ±37.5895 | +0.955 | 0.3395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2097**, Adj R² = **0.1637**, F-statistic = **4.56** (p = **3.94e-06**), Residual SE = **4752.917** on **189** df, AIC = **3985.6**, BIC = **4025.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21072.0777** | 2813.7074 | ±5627.4149 | **+7.489** | **6.94e-14** | *** |
| Education: graduate level (vs college) | -1167.1468 | 736.1824 | ±1472.3648 | -1.585 | 0.1129 |  |
| Education: high school or below (vs college) | +582.8858 | 1130.3447 | ±2260.6893 | +0.516 | 0.6061 |  |
| Site: UCSD (vs UAB) | +181.9764 | 886.8020 | ±1773.6040 | +0.205 | 0.8374 |  |
| Site: UW (vs UAB) | +896.8272 | 862.0341 | ±1724.0683 | +1.040 | 0.2982 |  |
| **Age (years)** | **-163.2924** | 31.2244 | ±62.4488 | **-5.230** | **1.70e-07** | *** |
| BMI (kg/m2) | -21.8903 | 47.7541 | ±95.5082 | -0.458 | 0.6467 |  |
| Hypertension | -403.5120 | 836.9935 | ±1673.9871 | -0.482 | 0.6297 |  |
| High cholesterol | +21.1273 | 793.0751 | ±1586.1502 | +0.027 | 0.9787 |  |
| Kidney disease | -1482.6712 | 914.9155 | ±1829.8310 | -1.621 | 0.1051 |  |
| **Circulatory disease** | **-1430.0111** | 673.9990 | ±1347.9980 | **-2.122** | **0.0339** | * |
| Time < 54 (%) | -495.0009 | 380.5457 | ±761.0914 | -1.301 | 0.1933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **201**, R² = **0.2122**, Adj R² = **0.1664**, F-statistic = **4.63** (p = **3.07e-06**), Residual SE = **4745.369** on **189** df, AIC = **3984.9**, BIC = **4024.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20961.6241** | 2789.6655 | ±5579.3309 | **+7.514** | **5.73e-14** | *** |
| Education: graduate level (vs college) | -1202.0702 | 742.2988 | ±1484.5976 | -1.619 | 0.1054 |  |
| Education: high school or below (vs college) | +570.2015 | 1131.3633 | ±2262.7266 | +0.504 | 0.6143 |  |
| Site: UCSD (vs UAB) | +178.3029 | 887.9828 | ±1775.9657 | +0.201 | 0.8409 |  |
| Site: UW (vs UAB) | +909.7437 | 859.2001 | ±1718.4001 | +1.059 | 0.2897 |  |
| **Age (years)** | **-161.1019** | 31.3736 | ±62.7471 | **-5.135** | **2.82e-07** | *** |
| BMI (kg/m2) | -22.7107 | 47.1150 | ±94.2301 | -0.482 | 0.6298 |  |
| Hypertension | -418.8048 | 837.7426 | ±1675.4852 | -0.500 | 0.6171 |  |
| High cholesterol | -16.7332 | 791.6705 | ±1583.3410 | -0.021 | 0.9831 |  |
| Kidney disease | -1452.0102 | 916.3045 | ±1832.6091 | -1.585 | 0.1130 |  |
| **Circulatory disease** | **-1417.1558** | 672.4138 | ±1344.8276 | **-2.108** | **0.0351** | * |
| Avg. daily time < 54 (%) | -542.1604 | 293.4102 | ±586.8205 | -1.848 | 0.0646 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2081**, Adj R² = **0.1620**, F-statistic = **4.51** (p = **4.64e-06**), Residual SE = **4757.867** on **189** df, AIC = **3986.0**, BIC = **4025.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20958.4643** | 2814.8929 | ±5629.7858 | **+7.446** | **9.65e-14** | *** |
| Education: graduate level (vs college) | -1230.2639 | 729.9056 | ±1459.8113 | -1.686 | 0.0919 | . |
| Education: high school or below (vs college) | +697.1774 | 1142.3198 | ±2284.6395 | +0.610 | 0.5417 |  |
| Site: UCSD (vs UAB) | +233.9471 | 874.6947 | ±1749.3894 | +0.267 | 0.7891 |  |
| Site: UW (vs UAB) | +1005.9507 | 847.9321 | ±1695.8642 | +1.186 | 0.2355 |  |
| **Age (years)** | **-160.3295** | 32.0908 | ±64.1815 | **-4.996** | **5.85e-07** | *** |
| BMI (kg/m2) | -23.3538 | 48.3477 | ±96.6953 | -0.483 | 0.6291 |  |
| Hypertension | -463.4314 | 837.2533 | ±1674.5066 | -0.554 | 0.5799 |  |
| High cholesterol | +27.9959 | 797.0722 | ±1594.1444 | +0.035 | 0.9720 |  |
| Kidney disease | -1449.6931 | 912.9796 | ±1825.9593 | -1.588 | 0.1123 |  |
| **Circulatory disease** | **-1501.2902** | 675.0257 | ±1350.0515 | **-2.224** | **0.0261** | * |
| Time 54-69, pooled (%) | -125.0139 | 106.3625 | ±212.7249 | -1.175 | 0.2399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **201**, R² = **0.2088**, Adj R² = **0.1628**, F-statistic = **4.53** (p = **4.30e-06**), Residual SE = **4755.587** on **189** df, AIC = **3985.8**, BIC = **4025.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20898.8758** | 2818.3867 | ±5636.7734 | **+7.415** | **1.21e-13** | *** |
| Education: graduate level (vs college) | -1233.3778 | 731.2641 | ±1462.5282 | -1.687 | 0.0917 | . |
| Education: high school or below (vs college) | +712.1018 | 1143.1213 | ±2286.2426 | +0.623 | 0.5333 |  |
| Site: UCSD (vs UAB) | +234.3829 | 875.0327 | ±1750.0653 | +0.268 | 0.7888 |  |
| Site: UW (vs UAB) | +1002.9322 | 849.6336 | ±1699.2671 | +1.180 | 0.2378 |  |
| **Age (years)** | **-159.3316** | 32.3003 | ±64.6007 | **-4.933** | **8.11e-07** | *** |
| BMI (kg/m2) | -23.3884 | 48.0643 | ±96.1285 | -0.487 | 0.6265 |  |
| Hypertension | -462.2409 | 837.4006 | ±1674.8013 | -0.552 | 0.5810 |  |
| High cholesterol | +24.8911 | 796.6637 | ±1593.3274 | +0.031 | 0.9751 |  |
| Kidney disease | -1447.4164 | 913.1651 | ±1826.3303 | -1.585 | 0.1130 |  |
| **Circulatory disease** | **-1503.2535** | 674.6342 | ±1349.2683 | **-2.228** | **0.0259** | * |
| Avg. daily time 54-69 (%) | -129.5705 | 96.6432 | ±193.2864 | -1.341 | 0.1800 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **201**, R² = **0.2090**, Adj R² = **0.1630**, F-statistic = **4.54** (p = **4.22e-06**), Residual SE = **4755.016** on **189** df, AIC = **3985.8**, BIC = **4025.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20992.1193** | 2813.4674 | ±5626.9349 | **+7.461** | **8.57e-14** | *** |
| Education: graduate level (vs college) | -1233.8606 | 730.8425 | ±1461.6849 | -1.688 | 0.0914 | . |
| Education: high school or below (vs college) | +675.2994 | 1137.7617 | ±2275.5234 | +0.594 | 0.5528 |  |
| Site: UCSD (vs UAB) | +212.9151 | 874.7887 | ±1749.5775 | +0.243 | 0.8077 |  |
| Site: UW (vs UAB) | +974.7183 | 848.3431 | ±1696.6862 | +1.149 | 0.2506 |  |
| **Age (years)** | **-160.4111** | 31.8668 | ±63.7336 | **-5.034** | **4.81e-07** | *** |
| BMI (kg/m2) | -23.1276 | 48.3778 | ±96.7555 | -0.478 | 0.6326 |  |
| Hypertension | -451.5735 | 834.2618 | ±1668.5236 | -0.541 | 0.5883 |  |
| High cholesterol | +29.6582 | 795.8794 | ±1591.7587 | +0.037 | 0.9703 |  |
| Kidney disease | -1454.7489 | 911.3598 | ±1822.7196 | -1.596 | 0.1104 |  |
| **Circulatory disease** | **-1482.7382** | 674.1763 | ±1348.3527 | **-2.199** | **0.0279** | * |
| Time < 70 (%) | -115.5224 | 84.0622 | ±168.1244 | -1.374 | 0.1694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **201**, R² = **0.2103**, Adj R² = **0.1644**, F-statistic = **4.58** (p = **3.71e-06**), Residual SE = **4751.073** on **189** df, AIC = **3985.4**, BIC = **4025.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20910.6174** | 2811.9806 | ±5623.9611 | **+7.436** | **1.04e-13** | *** |
| Education: graduate level (vs college) | -1246.5506 | 733.8767 | ±1467.7534 | -1.699 | 0.0894 | . |
| Education: high school or below (vs college) | +687.7795 | 1137.2446 | ±2274.4893 | +0.605 | 0.5453 |  |
| Site: UCSD (vs UAB) | +212.2341 | 875.4896 | ±1750.9792 | +0.242 | 0.8085 |  |
| Site: UW (vs UAB) | +975.2031 | 850.6327 | ±1701.2654 | +1.146 | 0.2516 |  |
| **Age (years)** | **-158.9062** | 32.0945 | ±64.1890 | **-4.951** | **7.38e-07** | *** |
| BMI (kg/m2) | -23.3655 | 47.9197 | ±95.8393 | -0.488 | 0.6258 |  |
| Hypertension | -454.5284 | 835.2902 | ±1670.5803 | -0.544 | 0.5863 |  |
| High cholesterol | +18.4883 | 794.7409 | ±1589.4818 | +0.023 | 0.9814 |  |
| Kidney disease | -1445.2276 | 911.9552 | ±1823.9103 | -1.585 | 0.1130 |  |
| **Circulatory disease** | **-1482.1053** | 673.2370 | ±1346.4740 | **-2.201** | **0.0277** | * |
| Avg. daily time < 70 (%) | -122.2838 | 73.0572 | ±146.1144 | -1.674 | 0.0942 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2092**, Adj R² = **0.1631**, F-statistic = **4.54** (p = **4.16e-06**), Residual SE = **4754.526** on **189** df, AIC = **3985.7**, BIC = **4025.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17321.8300** | 3988.4848 | ±7976.9697 | **+4.343** | **1.41e-05** | *** |
| Education: graduate level (vs college) | -1183.5604 | 739.4034 | ±1478.8067 | -1.601 | 0.1094 |  |
| Education: high school or below (vs college) | +738.1375 | 1131.0068 | ±2262.0135 | +0.653 | 0.5140 |  |
| Site: UCSD (vs UAB) | +251.0995 | 904.2885 | ±1808.5770 | +0.278 | 0.7813 |  |
| Site: UW (vs UAB) | +958.1388 | 850.9489 | ±1701.8979 | +1.126 | 0.2602 |  |
| **Age (years)** | **-164.5887** | 31.3700 | ±62.7399 | **-5.247** | **1.55e-07** | *** |
| BMI (kg/m2) | -24.4740 | 47.3291 | ±94.6582 | -0.517 | 0.6051 |  |
| Hypertension | -443.8624 | 835.9005 | ±1671.8010 | -0.531 | 0.5954 |  |
| High cholesterol | -23.4701 | 796.1858 | ±1592.3716 | -0.029 | 0.9765 |  |
| Kidney disease | -1388.3180 | 925.7504 | ±1851.5008 | -1.500 | 0.1337 |  |
| **Circulatory disease** | **-1453.2222** | 684.1817 | ±1368.3635 | **-2.124** | **0.0337** | * |
| Time 54-250, pooled (%) | +38.5253 | 34.5333 | ±69.0666 | +1.116 | 0.2646 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2072**, Adj R² = **0.1610**, F-statistic = **4.49** (p = **5.07e-06**), Residual SE = **4760.556** on **189** df, AIC = **3986.2**, BIC = **4025.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17841.7264** | 4391.0669 | ±8782.1339 | **+4.063** | **4.84e-05** | *** |
| Education: graduate level (vs college) | -1172.7108 | 740.6671 | ±1481.3343 | -1.583 | 0.1133 |  |
| Education: high school or below (vs college) | +730.3472 | 1131.5741 | ±2263.1483 | +0.645 | 0.5187 |  |
| Site: UCSD (vs UAB) | +263.5997 | 901.7193 | ±1803.4387 | +0.292 | 0.7700 |  |
| Site: UW (vs UAB) | +983.3526 | 851.1621 | ±1702.3242 | +1.155 | 0.2480 |  |
| **Age (years)** | **-164.1233** | 31.3504 | ±62.7008 | **-5.235** | **1.65e-07** | *** |
| BMI (kg/m2) | -24.5300 | 47.5075 | ±95.0149 | -0.516 | 0.6056 |  |
| Hypertension | -446.0872 | 837.6181 | ±1675.2362 | -0.533 | 0.5943 |  |
| High cholesterol | -13.9583 | 797.3742 | ±1594.7484 | -0.018 | 0.9860 |  |
| Kidney disease | -1394.0909 | 922.2625 | ±1844.5251 | -1.512 | 0.1306 |  |
| **Circulatory disease** | **-1457.0558** | 686.6513 | ±1373.3025 | **-2.122** | **0.0338** | * |
| Avg. daily time 54-250 (%) | +32.5766 | 39.3599 | ±78.7198 | +0.828 | 0.4079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2053**, Adj R² = **0.1590**, F-statistic = **4.44** (p = **6.11e-06**), Residual SE = **4766.231** on **189** df, AIC = **3986.7**, BIC = **4026.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20967.4784** | 2847.9273 | ±5695.8546 | **+7.362** | **1.81e-13** | *** |
| Education: graduate level (vs college) | -1151.2012 | 754.1686 | ±1508.3371 | -1.526 | 0.1269 |  |
| Education: high school or below (vs college) | +673.2232 | 1134.8300 | ±2269.6601 | +0.593 | 0.5530 |  |
| Site: UCSD (vs UAB) | +286.6826 | 906.1292 | ±1812.2583 | +0.316 | 0.7517 |  |
| Site: UW (vs UAB) | +1045.4107 | 846.9928 | ±1693.9856 | +1.234 | 0.2171 |  |
| **Age (years)** | **-162.6457** | 30.8728 | ±61.7456 | **-5.268** | **1.38e-07** | *** |
| BMI (kg/m2) | -23.0456 | 47.8486 | ±95.6973 | -0.482 | 0.6301 |  |
| Hypertension | -475.0348 | 834.2968 | ±1668.5935 | -0.569 | 0.5691 |  |
| High cholesterol | +39.8065 | 806.3288 | ±1612.6576 | +0.049 | 0.9606 |  |
| Kidney disease | -1400.2701 | 937.3835 | ±1874.7671 | -1.494 | 0.1352 |  |
| **Circulatory disease** | **-1503.4462** | 677.8223 | ±1355.6445 | **-2.218** | **0.0266** | * |
| Time 181-250, pooled (%) | -12.3319 | 29.4247 | ±58.8495 | -0.419 | 0.6751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **201**, R² = **0.2061**, Adj R² = **0.1599**, F-statistic = **4.46** (p = **5.62e-06**), Residual SE = **4763.707** on **189** df, AIC = **3986.5**, BIC = **4026.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21023.9132** | 2861.7038 | ±5723.4075 | **+7.347** | **2.03e-13** | *** |
| Education: graduate level (vs college) | -1165.2319 | 750.8604 | ±1501.7207 | -1.552 | 0.1207 |  |
| Education: high school or below (vs college) | +680.8094 | 1135.1720 | ±2270.3439 | +0.600 | 0.5487 |  |
| Site: UCSD (vs UAB) | +277.0557 | 911.7997 | ±1823.5994 | +0.304 | 0.7612 |  |
| Site: UW (vs UAB) | +1037.1066 | 847.8776 | ±1695.7551 | +1.223 | 0.2213 |  |
| **Age (years)** | **-162.4164** | 30.9751 | ±61.9502 | **-5.243** | **1.58e-07** | *** |
| BMI (kg/m2) | -23.3932 | 47.8104 | ±95.6207 | -0.489 | 0.6246 |  |
| Hypertension | -488.4146 | 835.1071 | ±1670.2143 | -0.585 | 0.5586 |  |
| High cholesterol | +51.8044 | 805.8674 | ±1611.7348 | +0.064 | 0.9487 |  |
| Kidney disease | -1375.0279 | 935.9892 | ±1871.9785 | -1.469 | 0.1418 |  |
| **Circulatory disease** | **-1499.2133** | 678.0585 | ±1356.1169 | **-2.211** | **0.0270** | * |
| Avg. daily time 181-250 (%) | -17.0825 | 27.8256 | ±55.6512 | -0.614 | 0.5393 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **201**, R² = **0.2070**, Adj R² = **0.1608**, F-statistic = **4.48** (p = **5.15e-06**), Residual SE = **4761.063** on **189** df, AIC = **3986.3**, BIC = **4025.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21068.7417** | 2860.4944 | ±5720.9888 | **+7.365** | **1.77e-13** | *** |
| Education: graduate level (vs college) | -1181.5795 | 749.6790 | ±1499.3581 | -1.576 | 0.1150 |  |
| Education: high school or below (vs college) | +703.2398 | 1132.7838 | ±2265.5676 | +0.621 | 0.5347 |  |
| Site: UCSD (vs UAB) | +274.5663 | 910.7929 | ±1821.5858 | +0.301 | 0.7631 |  |
| Site: UW (vs UAB) | +1018.7044 | 849.8201 | ±1699.6402 | +1.199 | 0.2306 |  |
| **Age (years)** | **-162.5646** | 31.1436 | ±62.2872 | **-5.220** | **1.79e-07** | *** |
| BMI (kg/m2) | -23.8238 | 47.7354 | ±95.4709 | -0.499 | 0.6177 |  |
| Hypertension | -478.1686 | 836.8710 | ±1673.7420 | -0.571 | 0.5677 |  |
| High cholesterol | +33.2297 | 800.8504 | ±1601.7008 | +0.041 | 0.9669 |  |
| Kidney disease | -1360.0881 | 931.0235 | ±1862.0469 | -1.461 | 0.1441 |  |
| **Circulatory disease** | **-1481.8546** | 681.0385 | ±1362.0770 | **-2.176** | **0.0296** | * |
| Time > 180 (%) | -14.3193 | 18.6761 | ±37.3523 | -0.767 | 0.4433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2067**, Adj R² = **0.1605**, F-statistic = **4.48** (p = **5.31e-06**), Residual SE = **4761.962** on **189** df, AIC = **3986.3**, BIC = **4026.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21076.9392** | 2866.3337 | ±5732.6673 | **+7.353** | **1.93e-13** | *** |
| Education: graduate level (vs college) | -1176.7545 | 748.5730 | ±1497.1460 | -1.572 | 0.1160 |  |
| Education: high school or below (vs college) | +706.6925 | 1133.4924 | ±2266.9847 | +0.623 | 0.5330 |  |
| Site: UCSD (vs UAB) | +271.4906 | 910.7353 | ±1821.4707 | +0.298 | 0.7656 |  |
| Site: UW (vs UAB) | +1016.9771 | 850.1641 | ±1700.3281 | +1.196 | 0.2316 |  |
| **Age (years)** | **-162.8330** | 31.1682 | ±62.3363 | **-5.224** | **1.75e-07** | *** |
| BMI (kg/m2) | -24.0225 | 47.8018 | ±95.6037 | -0.503 | 0.6153 |  |
| Hypertension | -479.5764 | 837.0598 | ±1674.1197 | -0.573 | 0.5667 |  |
| High cholesterol | +34.3131 | 802.0112 | ±1604.0224 | +0.043 | 0.9659 |  |
| Kidney disease | -1364.3994 | 928.6853 | ±1857.3706 | -1.469 | 0.1418 |  |
| **Circulatory disease** | **-1481.1694** | 681.1695 | ±1362.3391 | **-2.174** | **0.0297** | * |
| Avg. daily time > 180 (%) | -13.5228 | 18.7363 | ±37.4726 | -0.722 | 0.4705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2073**, Adj R² = **0.1612**, F-statistic = **4.49** (p = **4.99e-06**), Residual SE = **4760.072** on **189** df, AIC = **3986.2**, BIC = **4025.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21055.0947** | 2848.4118 | ±5696.8237 | **+7.392** | **1.45e-13** | *** |
| Education: graduate level (vs college) | -1168.7324 | 742.3009 | ±1484.6018 | -1.574 | 0.1154 |  |
| Education: high school or below (vs college) | +681.3817 | 1138.6277 | ±2277.2554 | +0.598 | 0.5496 |  |
| Site: UCSD (vs UAB) | +283.6155 | 912.5654 | ±1825.1308 | +0.311 | 0.7560 |  |
| Site: UW (vs UAB) | +1015.2296 | 847.3582 | ±1694.7164 | +1.198 | 0.2309 |  |
| **Age (years)** | **-164.2115** | 31.4037 | ±62.8074 | **-5.229** | **1.70e-07** | *** |
| BMI (kg/m2) | -22.8338 | 47.3065 | ±94.6130 | -0.483 | 0.6293 |  |
| Hypertension | -438.1124 | 838.5314 | ±1677.0629 | -0.522 | 0.6013 |  |
| High cholesterol | +39.8841 | 802.7117 | ±1605.4234 | +0.050 | 0.9604 |  |
| Kidney disease | -1408.8518 | 930.4915 | ±1860.9831 | -1.514 | 0.1300 |  |
| **Circulatory disease** | **-1461.3619** | 682.9314 | ±1365.8627 | **-2.140** | **0.0324** | * |
| Nocturnal time > 180 (%) | -14.9065 | 19.2261 | ±38.4522 | -0.775 | 0.4381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2065**, Adj R² = **0.1603**, F-statistic = **4.47** (p = **5.39e-06**), Residual SE = **4762.447** on **189** df, AIC = **3986.4**, BIC = **4026.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20807.0460** | 2838.2566 | ±5676.5132 | **+7.331** | **2.29e-13** | *** |
| Education: graduate level (vs college) | -1042.2967 | 758.7238 | ±1517.4476 | -1.374 | 0.1695 |  |
| Education: high school or below (vs college) | +630.6617 | 1142.1127 | ±2284.2254 | +0.552 | 0.5808 |  |
| Site: UCSD (vs UAB) | +276.8165 | 883.3546 | ±1766.7091 | +0.313 | 0.7540 |  |
| Site: UW (vs UAB) | +987.1419 | 818.4685 | ±1636.9370 | +1.206 | 0.2278 |  |
| **Age (years)** | **-168.4986** | 31.2630 | ±62.5260 | **-5.390** | **7.06e-08** | *** |
| BMI (kg/m2) | -18.8432 | 49.1256 | ±98.2512 | -0.384 | 0.7013 |  |
| Hypertension | -445.4620 | 839.2093 | ±1678.4187 | -0.531 | 0.5955 |  |
| High cholesterol | -9.1527 | 802.8200 | ±1605.6400 | -0.011 | 0.9909 |  |
| Kidney disease | -1585.8557 | 922.8880 | ±1845.7760 | -1.718 | 0.0857 | . |
| **Circulatory disease** | **-1511.4282** | 674.5802 | ±1349.1604 | **-2.241** | **0.0251** | * |
| Any reading > 250 during wear (0/1) | +501.1215 | 753.8858 | ±1507.7716 | +0.665 | 0.5062 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2084**, Adj R² = **0.1624**, F-statistic = **4.52** (p = **4.47e-06**), Residual SE = **4756.733** on **189** df, AIC = **3985.9**, BIC = **4025.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21143.0069** | 2830.5218 | ±5661.0437 | **+7.470** | **8.04e-14** | *** |
| Education: graduate level (vs college) | -1174.4142 | 739.3902 | ±1478.7804 | -1.588 | 0.1122 |  |
| Education: high school or below (vs college) | +738.7173 | 1130.7209 | ±2261.4418 | +0.653 | 0.5136 |  |
| Site: UCSD (vs UAB) | +261.9058 | 902.4817 | ±1804.9634 | +0.290 | 0.7717 |  |
| Site: UW (vs UAB) | +975.0563 | 849.7371 | ±1699.4743 | +1.147 | 0.2512 |  |
| **Age (years)** | **-164.6247** | 31.3891 | ±62.7782 | **-5.245** | **1.57e-07** | *** |
| BMI (kg/m2) | -24.3852 | 47.3383 | ±94.6767 | -0.515 | 0.6065 |  |
| Hypertension | -447.6622 | 836.9064 | ±1673.8128 | -0.535 | 0.5927 |  |
| High cholesterol | -22.1233 | 796.5720 | ±1593.1441 | -0.028 | 0.9778 |  |
| Kidney disease | -1393.1137 | 925.3790 | ±1850.7581 | -1.505 | 0.1322 |  |
| **Circulatory disease** | **-1463.8171** | 684.3174 | ±1368.6349 | **-2.139** | **0.0324** | * |
| Time > 250 (%) | -35.5867 | 34.8488 | ±69.6976 | -1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2064**, Adj R² = **0.1602**, F-statistic = **4.47** (p = **5.49e-06**), Residual SE = **4762.974** on **189** df, AIC = **3986.4**, BIC = **4026.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21068.3865** | 2832.2355 | ±5664.4710 | **+7.439** | **1.02e-13** | *** |
| Education: graduate level (vs college) | -1159.2087 | 739.9636 | ±1479.9272 | -1.567 | 0.1172 |  |
| Education: high school or below (vs college) | +725.5115 | 1130.7506 | ±2261.5013 | +0.642 | 0.5211 |  |
| Site: UCSD (vs UAB) | +273.4279 | 899.2896 | ±1798.5792 | +0.304 | 0.7611 |  |
| Site: UW (vs UAB) | +999.1821 | 849.9874 | ±1699.9747 | +1.176 | 0.2398 |  |
| **Age (years)** | **-164.2932** | 31.3702 | ±62.7404 | **-5.237** | **1.63e-07** | *** |
| BMI (kg/m2) | -24.2330 | 47.5602 | ±95.1204 | -0.510 | 0.6104 |  |
| Hypertension | -448.2594 | 838.5808 | ±1677.1616 | -0.535 | 0.5930 |  |
| High cholesterol | -9.4874 | 797.8774 | ±1595.7547 | -0.012 | 0.9905 |  |
| Kidney disease | -1405.9134 | 920.9515 | ±1841.9031 | -1.527 | 0.1269 |  |
| **Circulatory disease** | **-1470.5978** | 686.1013 | ±1372.2025 | **-2.143** | **0.0321** | * |
| Avg. daily time > 250 (%) | -27.5861 | 39.1825 | ±78.3651 | -0.704 | 0.4814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 201; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **201**, R² = **0.2272**, Adj R² = **0.1865**, F-statistic = **5.59** (p = **2.70e-07**), Residual SE = **13.517** on **190** df, AIC = **1627.9**, BIC = **1664.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3720** | 8.2431 | ±16.4862 | **+6.596** | **4.22e-11** | *** |
| Education: graduate level (vs college) | -2.9585 | 2.0743 | ±4.1485 | -1.426 | 0.1538 |  |
| Education: high school or below (vs college) | +4.2385 | 3.3740 | ±6.7480 | +1.256 | 0.2090 |  |
| Site: UCSD (vs UAB) | -0.3659 | 2.6696 | ±5.3392 | -0.137 | 0.8910 |  |
| Site: UW (vs UAB) | +2.6003 | 2.3469 | ±4.6939 | +1.108 | 0.2679 |  |
| **Age (years)** | **-0.4882** | 0.0881 | ±0.1763 | **-5.539** | **3.04e-08** | *** |
| BMI (kg/m2) | +0.0393 | 0.1327 | ±0.2655 | +0.296 | 0.7672 |  |
| Hypertension | -1.3215 | 2.4658 | ±4.9315 | -0.536 | 0.5920 |  |
| High cholesterol | -0.1246 | 2.2450 | ±4.4900 | -0.056 | 0.9557 |  |
| Kidney disease | -4.0670 | 2.5958 | ±5.1916 | -1.567 | 0.1172 |  |
| Circulatory disease | -3.5393 | 2.0091 | ±4.0181 | -1.762 | 0.0781 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **201**, R² = **0.2403**, Adj R² = **0.1961**, F-statistic = **5.43** (p = **1.69e-07**), Residual SE = **13.437** on **189** df, AIC = **1626.5**, BIC = **1666.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2971** | 10.4016 | ±20.8032 | **+4.451** | **8.55e-06** | *** |
| Education: graduate level (vs college) | -2.4459 | 2.1586 | ±4.3172 | -1.133 | 0.2572 |  |
| Education: high school or below (vs college) | +3.8875 | 3.3146 | ±6.6291 | +1.173 | 0.2409 |  |
| Site: UCSD (vs UAB) | -0.1276 | 2.6404 | ±5.2808 | -0.048 | 0.9615 |  |
| Site: UW (vs UAB) | +2.7645 | 2.3535 | ±4.7071 | +1.175 | 0.2401 |  |
| **Age (years)** | **-0.5171** | 0.0898 | ±0.1796 | **-5.759** | **8.46e-09** | *** |
| BMI (kg/m2) | +0.0293 | 0.1311 | ±0.2622 | +0.224 | 0.8230 |  |
| Hypertension | -1.3401 | 2.4652 | ±4.9304 | -0.544 | 0.5867 |  |
| High cholesterol | -0.0201 | 2.2124 | ±4.4248 | -0.009 | 0.9928 |  |
| Kidney disease | -4.0920 | 2.4355 | ±4.8709 | -1.680 | 0.0929 | . |
| Circulatory disease | -3.4882 | 1.9792 | ±3.9584 | -1.762 | 0.0780 | . |
| HbA1c (%) | +1.5433 | 1.1801 | ±2.3603 | +1.308 | 0.1910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **201**, R² = **0.2274**, Adj R² = **0.1825**, F-statistic = **5.06** (p = **6.52e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.3528** | 10.2726 | ±20.5452 | **+5.388** | **7.11e-08** | *** |
| Education: graduate level (vs college) | -2.9881 | 2.0921 | ±4.1842 | -1.428 | 0.1532 |  |
| Education: high school or below (vs college) | +4.2764 | 3.3956 | ±6.7913 | +1.259 | 0.2079 |  |
| Site: UCSD (vs UAB) | -0.3691 | 2.7092 | ±5.4183 | -0.136 | 0.8916 |  |
| Site: UW (vs UAB) | +2.5827 | 2.3666 | ±4.7331 | +1.091 | 0.2751 |  |
| **Age (years)** | **-0.4875** | 0.0882 | ±0.1764 | **-5.528** | **3.23e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.1335 | ±0.2670 | +0.293 | 0.7698 |  |
| Hypertension | -1.3285 | 2.4801 | ±4.9603 | -0.536 | 0.5922 |  |
| High cholesterol | -0.1224 | 2.2601 | ±4.5202 | -0.054 | 0.9568 |  |
| Kidney disease | -4.0048 | 2.6105 | ±5.2211 | -1.534 | 0.1250 |  |
| Circulatory disease | -3.5216 | 2.0356 | ±4.0712 | -1.730 | 0.0836 | . |
| Mean glucose (mg/dL) | -0.0074 | 0.0348 | ±0.0696 | -0.214 | 0.8309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **201**, R² = **0.2274**, Adj R² = **0.1825**, F-statistic = **5.06** (p = **6.52e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.3813** | 13.7699 | ±27.5397 | **+4.095** | **4.23e-05** | *** |
| Education: graduate level (vs college) | -2.9881 | 2.0921 | ±4.1842 | -1.428 | 0.1532 |  |
| Education: high school or below (vs college) | +4.2764 | 3.3956 | ±6.7913 | +1.259 | 0.2079 |  |
| Site: UCSD (vs UAB) | -0.3691 | 2.7092 | ±5.4183 | -0.136 | 0.8916 |  |
| Site: UW (vs UAB) | +2.5827 | 2.3666 | ±4.7331 | +1.091 | 0.2751 |  |
| **Age (years)** | **-0.4875** | 0.0882 | ±0.1764 | **-5.528** | **3.23e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.1335 | ±0.2670 | +0.293 | 0.7698 |  |
| Hypertension | -1.3285 | 2.4801 | ±4.9603 | -0.536 | 0.5922 |  |
| High cholesterol | -0.1224 | 2.2601 | ±4.5202 | -0.054 | 0.9568 |  |
| Kidney disease | -4.0048 | 2.6105 | ±5.2211 | -1.534 | 0.1250 |  |
| Circulatory disease | -3.5216 | 2.0356 | ±4.0712 | -1.730 | 0.0836 | . |
| GMI (%) | -0.3107 | 1.4550 | ±2.9101 | -0.214 | 0.8309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **201**, R² = **0.2276**, Adj R² = **0.1826**, F-statistic = **5.06** (p = **6.43e-07**), Residual SE = **13.549** on **189** df, AIC = **1629.8**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.1845** | 10.1213 | ±20.2427 | **+5.255** | **1.48e-07** | *** |
| Education: graduate level (vs college) | -2.9524 | 2.0829 | ±4.1658 | -1.417 | 0.1564 |  |
| Education: high school or below (vs college) | +4.1919 | 3.3966 | ±6.7933 | +1.234 | 0.2172 |  |
| Site: UCSD (vs UAB) | -0.3744 | 2.6740 | ±5.3481 | -0.140 | 0.8887 |  |
| Site: UW (vs UAB) | +2.6081 | 2.3586 | ±4.7172 | +1.106 | 0.2688 |  |
| **Age (years)** | **-0.4870** | 0.0892 | ±0.1784 | **-5.458** | **4.81e-08** | *** |
| BMI (kg/m2) | +0.0387 | 0.1333 | ±0.2665 | +0.290 | 0.7716 |  |
| Hypertension | -1.3414 | 2.4805 | ±4.9610 | -0.541 | 0.5887 |  |
| High cholesterol | -0.1383 | 2.2631 | ±4.5263 | -0.061 | 0.9513 |  |
| Kidney disease | -4.0859 | 2.5941 | ±5.1883 | -1.575 | 0.1152 |  |
| Circulatory disease | -3.5669 | 2.0233 | ±4.0465 | -1.763 | 0.0779 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0089 | 0.0337 | ±0.0673 | +0.265 | 0.7908 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2303**, Adj R² = **0.1855**, F-statistic = **5.14** (p = **4.86e-07**), Residual SE = **13.526** on **189** df, AIC = **1629.1**, BIC = **1668.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.6072** | 8.5579 | ±17.1159 | **+6.498** | **8.15e-11** | *** |
| Education: graduate level (vs college) | -3.2188 | 2.0979 | ±4.1957 | -1.534 | 0.1250 |  |
| Education: high school or below (vs college) | +4.5882 | 3.3785 | ±6.7571 | +1.358 | 0.1744 |  |
| Site: UCSD (vs UAB) | -0.4262 | 2.7277 | ±5.4554 | -0.156 | 0.8758 |  |
| Site: UW (vs UAB) | +2.4852 | 2.3649 | ±4.7299 | +1.051 | 0.2933 |  |
| **Age (years)** | **-0.4734** | 0.0895 | ±0.1790 | **-5.289** | **1.23e-07** | *** |
| BMI (kg/m2) | +0.0339 | 0.1340 | ±0.2681 | +0.253 | 0.8003 |  |
| Hypertension | -1.3733 | 2.4675 | ±4.9350 | -0.557 | 0.5778 |  |
| High cholesterol | -0.1338 | 2.2545 | ±4.5091 | -0.059 | 0.9527 |  |
| Kidney disease | -3.5474 | 2.5968 | ±5.1936 | -1.366 | 0.1719 |  |
| Circulatory disease | -3.5786 | 2.0515 | ±4.1029 | -1.744 | 0.0811 | . |
| Glucose SD, pooled (mg/dL) | -0.0562 | 0.0690 | ±0.1381 | -0.815 | 0.4152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2339**, Adj R² = **0.1893**, F-statistic = **5.24** (p = **3.34e-07**), Residual SE = **13.494** on **189** df, AIC = **1628.1**, BIC = **1667.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.4173** | 8.5777 | ±17.1555 | **+6.577** | **4.79e-11** | *** |
| Education: graduate level (vs college) | -3.3534 | 2.0997 | ±4.1995 | -1.597 | 0.1103 |  |
| Education: high school or below (vs college) | +4.8581 | 3.3519 | ±6.7039 | +1.449 | 0.1472 |  |
| Site: UCSD (vs UAB) | -0.4760 | 2.7206 | ±5.4412 | -0.175 | 0.8611 |  |
| Site: UW (vs UAB) | +2.4620 | 2.3533 | ±4.7066 | +1.046 | 0.2955 |  |
| **Age (years)** | **-0.4665** | 0.0879 | ±0.1758 | **-5.308** | **1.11e-07** | *** |
| BMI (kg/m2) | +0.0278 | 0.1341 | ±0.2681 | +0.208 | 0.8355 |  |
| Hypertension | -1.4377 | 2.4588 | ±4.9175 | -0.585 | 0.5587 |  |
| High cholesterol | -0.0925 | 2.2456 | ±4.4913 | -0.041 | 0.9671 |  |
| Kidney disease | -3.2923 | 2.5938 | ±5.1876 | -1.269 | 0.2043 |  |
| Circulatory disease | -3.6261 | 2.0456 | ±4.0912 | -1.773 | 0.0763 | . |
| Avg. daily SD (mg/dL) | -0.0982 | 0.0734 | ±0.1467 | -1.338 | 0.1807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **201**, R² = **0.2311**, Adj R² = **0.1864**, F-statistic = **5.16** (p = **4.45e-07**), Residual SE = **13.518** on **189** df, AIC = **1628.9**, BIC = **1668.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6127** | 8.4889 | ±16.9778 | **+6.669** | **2.58e-11** | *** |
| Education: graduate level (vs college) | -3.3297 | 2.0930 | ±4.1861 | -1.591 | 0.1117 |  |
| Education: high school or below (vs college) | +4.7677 | 3.3652 | ±6.7304 | +1.417 | 0.1566 |  |
| Site: UCSD (vs UAB) | -0.4132 | 2.6829 | ±5.3658 | -0.154 | 0.8776 |  |
| Site: UW (vs UAB) | +2.4594 | 2.3618 | ±4.7237 | +1.041 | 0.2977 |  |
| **Age (years)** | **-0.4602** | 0.0934 | ±0.1869 | **-4.925** | **8.42e-07** | *** |
| BMI (kg/m2) | +0.0314 | 0.1343 | ±0.2687 | +0.234 | 0.8152 |  |
| Hypertension | -1.4031 | 2.4603 | ±4.9206 | -0.570 | 0.5685 |  |
| High cholesterol | -0.1172 | 2.2517 | ±4.5034 | -0.052 | 0.9585 |  |
| Kidney disease | -3.3574 | 2.5648 | ±5.1295 | -1.309 | 0.1905 |  |
| Circulatory disease | -3.6398 | 2.0379 | ±4.0758 | -1.786 | 0.0741 | . |
| CV (%) | -0.1498 | 0.1340 | ±0.2681 | -1.117 | 0.2639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **201**, R² = **0.2275**, Adj R² = **0.1825**, F-statistic = **5.06** (p = **6.51e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0602** | 9.4996 | ±18.9991 | **+5.586** | **2.33e-08** | *** |
| Education: graduate level (vs college) | -3.0485 | 2.1105 | ±4.2211 | -1.444 | 0.1486 |  |
| Education: high school or below (vs college) | +4.3795 | 3.3758 | ±6.7516 | +1.297 | 0.1945 |  |
| Site: UCSD (vs UAB) | -0.3508 | 2.6789 | ±5.3578 | -0.131 | 0.8958 |  |
| Site: UW (vs UAB) | +2.5828 | 2.3602 | ±4.7204 | +1.094 | 0.2738 |  |
| **Age (years)** | **-0.4805** | 0.0938 | ±0.1876 | **-5.123** | **3.01e-07** | *** |
| BMI (kg/m2) | +0.0385 | 0.1337 | ±0.2675 | +0.288 | 0.7735 |  |
| Hypertension | -1.3493 | 2.4675 | ±4.9351 | -0.547 | 0.5845 |  |
| High cholesterol | -0.1239 | 2.2536 | ±4.5071 | -0.055 | 0.9561 |  |
| Kidney disease | -3.9434 | 2.6042 | ±5.2085 | -1.514 | 0.1300 |  |
| Circulatory disease | -3.5327 | 2.0200 | ±4.0400 | -1.749 | 0.0803 | . |
| Mean / SD ratio | +0.1959 | 0.6449 | ±1.2899 | +0.304 | 0.7613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2278**, Adj R² = **0.1828**, F-statistic = **5.07** (p = **6.29e-07**), Residual SE = **13.547** on **189** df, AIC = **1629.7**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4769** | 9.3960 | ±18.7919 | **+5.585** | **2.34e-08** | *** |
| Education: graduate level (vs college) | -3.1006 | 2.1122 | ±4.2243 | -1.468 | 0.1421 |  |
| Education: high school or below (vs college) | +4.4511 | 3.3389 | ±6.6778 | +1.333 | 0.1825 |  |
| Site: UCSD (vs UAB) | -0.3313 | 2.6784 | ±5.3569 | -0.124 | 0.9016 |  |
| Site: UW (vs UAB) | +2.5959 | 2.3563 | ±4.7125 | +1.102 | 0.2706 |  |
| **Age (years)** | **-0.4768** | 0.0934 | ±0.1867 | **-5.107** | **3.27e-07** | *** |
| BMI (kg/m2) | +0.0372 | 0.1337 | ±0.2674 | +0.279 | 0.7806 |  |
| Hypertension | -1.3823 | 2.4649 | ±4.9297 | -0.561 | 0.5749 |  |
| High cholesterol | -0.0940 | 2.2621 | ±4.5243 | -0.042 | 0.9668 |  |
| Kidney disease | -3.9438 | 2.6042 | ±5.2084 | -1.514 | 0.1299 |  |
| Circulatory disease | -3.5406 | 2.0167 | ±4.0334 | -1.756 | 0.0792 | . |
| Avg. daily mean/SD | +0.2406 | 0.5022 | ±1.0045 | +0.479 | 0.6319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **201**, R² = **0.2272**, Adj R² = **0.1823**, F-statistic = **5.05** (p = **6.66e-07**), Residual SE = **13.552** on **189** df, AIC = **1629.9**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.0366** | 9.5287 | ±19.0573 | **+5.671** | **1.42e-08** | *** |
| Education: graduate level (vs college) | -2.9340 | 2.1127 | ±4.2254 | -1.389 | 0.1649 |  |
| Education: high school or below (vs college) | +4.1915 | 3.3864 | ±6.7728 | +1.238 | 0.2158 |  |
| Site: UCSD (vs UAB) | -0.3763 | 2.6784 | ±5.3569 | -0.140 | 0.8883 |  |
| Site: UW (vs UAB) | +2.6249 | 2.3750 | ±4.7500 | +1.105 | 0.2691 |  |
| **Age (years)** | **-0.4891** | 0.0881 | ±0.1762 | **-5.551** | **2.83e-08** | *** |
| BMI (kg/m2) | +0.0380 | 0.1326 | ±0.2651 | +0.287 | 0.7742 |  |
| Hypertension | -1.3075 | 2.4894 | ±4.9788 | -0.525 | 0.5994 |  |
| High cholesterol | -0.1357 | 2.2766 | ±4.5531 | -0.060 | 0.9525 |  |
| Kidney disease | -4.0744 | 2.6142 | ±5.2284 | -1.559 | 0.1191 |  |
| Circulatory disease | -3.5378 | 2.0279 | ±4.0559 | -1.745 | 0.0811 | . |
| MAG (mg/dL/h) | +0.0096 | 0.1063 | ±0.2126 | +0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **201**, R² = **0.2309**, Adj R² = **0.1861**, F-statistic = **5.16** (p = **4.55e-07**), Residual SE = **13.520** on **189** df, AIC = **1628.9**, BIC = **1668.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.5532** | 8.9259 | ±17.8517 | **+6.336** | **2.36e-10** | *** |
| Education: graduate level (vs college) | -3.2653 | 2.1091 | ±4.2183 | -1.548 | 0.1216 |  |
| Education: high school or below (vs college) | +4.7506 | 3.3692 | ±6.7385 | +1.410 | 0.1585 |  |
| Site: UCSD (vs UAB) | -0.3981 | 2.7157 | ±5.4314 | -0.147 | 0.8835 |  |
| Site: UW (vs UAB) | +2.5306 | 2.3588 | ±4.7175 | +1.073 | 0.2833 |  |
| **Age (years)** | **-0.4731** | 0.0880 | ±0.1761 | **-5.374** | **7.70e-08** | *** |
| BMI (kg/m2) | +0.0305 | 0.1348 | ±0.2696 | +0.226 | 0.8210 |  |
| Hypertension | -1.4533 | 2.4685 | ±4.9369 | -0.589 | 0.5560 |  |
| High cholesterol | -0.0534 | 2.2569 | ±4.5138 | -0.024 | 0.9811 |  |
| Kidney disease | -3.4952 | 2.5835 | ±5.1670 | -1.353 | 0.1761 |  |
| Circulatory disease | -3.5385 | 2.0319 | ±4.0638 | -1.742 | 0.0816 | . |
| Avg. daily range (mg/dL) | -0.0206 | 0.0220 | ±0.0441 | -0.936 | 0.3490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **201**, R² = **0.2283**, Adj R² = **0.1834**, F-statistic = **5.08** (p = **5.94e-07**), Residual SE = **13.543** on **189** df, AIC = **1629.6**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.9723** | 8.3857 | ±16.7714 | **+6.436** | **1.22e-10** | *** |
| Education: graduate level (vs college) | -2.7977 | 2.1350 | ±4.2701 | -1.310 | 0.1901 |  |
| Education: high school or below (vs college) | +4.2288 | 3.3961 | ±6.7922 | +1.245 | 0.2131 |  |
| Site: UCSD (vs UAB) | -0.3655 | 2.6817 | ±5.3633 | -0.136 | 0.8916 |  |
| Site: UW (vs UAB) | +2.6752 | 2.3812 | ±4.7623 | +1.124 | 0.2612 |  |
| **Age (years)** | **-0.4934** | 0.0893 | ±0.1786 | **-5.525** | **3.29e-08** | *** |
| BMI (kg/m2) | +0.0410 | 0.1339 | ±0.2679 | +0.306 | 0.7598 |  |
| Hypertension | -1.3873 | 2.4884 | ±4.9769 | -0.558 | 0.5772 |  |
| High cholesterol | -0.0941 | 2.2457 | ±4.4913 | -0.042 | 0.9666 |  |
| Kidney disease | -4.2798 | 2.5704 | ±5.1408 | -1.665 | 0.0959 | . |
| Circulatory disease | -3.6043 | 2.0125 | ±4.0251 | -1.791 | 0.0733 | . |
| SD of daily means (mg/dL) | +0.0539 | 0.1256 | ±0.2512 | +0.430 | 0.6675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **201**, R² = **0.2288**, Adj R² = **0.1839**, F-statistic = **5.10** (p = **5.65e-07**), Residual SE = **13.538** on **189** df, AIC = **1629.5**, BIC = **1669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3736** | 8.9530 | ±17.9061 | **+5.738** | **9.57e-09** | *** |
| Education: graduate level (vs college) | -3.1541 | 2.1085 | ±4.2169 | -1.496 | 0.1347 |  |
| Education: high school or below (vs college) | +4.3274 | 3.3968 | ±6.7937 | +1.274 | 0.2027 |  |
| Site: UCSD (vs UAB) | -0.4264 | 2.7677 | ±5.5354 | -0.154 | 0.8776 |  |
| Site: UW (vs UAB) | +2.5239 | 2.3628 | ±4.7256 | +1.068 | 0.2854 |  |
| **Age (years)** | **-0.4832** | 0.0880 | ±0.1761 | **-5.489** | **4.05e-08** | *** |
| BMI (kg/m2) | +0.0363 | 0.1346 | ±0.2693 | +0.270 | 0.7874 |  |
| Hypertension | -1.3889 | 2.4747 | ±4.9494 | -0.561 | 0.5746 |  |
| High cholesterol | -0.0566 | 2.2713 | ±4.5425 | -0.025 | 0.9801 |  |
| Kidney disease | -3.8117 | 2.6343 | ±5.2686 | -1.447 | 0.1479 |  |
| Circulatory disease | -3.4554 | 2.0376 | ±4.0751 | -1.696 | 0.0899 | . |
| Time in range 70-180, pooled (%) | +0.0339 | 0.0614 | ±0.1228 | +0.552 | 0.5807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **201**, R² = **0.2288**, Adj R² = **0.1839**, F-statistic = **5.10** (p = **5.68e-07**), Residual SE = **13.539** on **189** df, AIC = **1629.5**, BIC = **1669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4333** | 8.9759 | ±17.9518 | **+5.730** | **1.00e-08** | *** |
| Education: graduate level (vs college) | -3.1503 | 2.1070 | ±4.2140 | -1.495 | 0.1349 |  |
| Education: high school or below (vs college) | +4.3430 | 3.3991 | ±6.7983 | +1.278 | 0.2014 |  |
| Site: UCSD (vs UAB) | -0.4343 | 2.7698 | ±5.5396 | -0.157 | 0.8754 |  |
| Site: UW (vs UAB) | +2.5186 | 2.3632 | ±4.7265 | +1.066 | 0.2865 |  |
| **Age (years)** | **-0.4833** | 0.0881 | ±0.1761 | **-5.488** | **4.07e-08** | *** |
| BMI (kg/m2) | +0.0356 | 0.1347 | ±0.2695 | +0.264 | 0.7914 |  |
| Hypertension | -1.3961 | 2.4768 | ±4.9536 | -0.564 | 0.5730 |  |
| High cholesterol | -0.0547 | 2.2742 | ±4.5483 | -0.024 | 0.9808 |  |
| Kidney disease | -3.8089 | 2.6290 | ±5.2579 | -1.449 | 0.1474 |  |
| Circulatory disease | -3.4508 | 2.0370 | ±4.0740 | -1.694 | 0.0903 | . |
| Avg. daily time in range 70-180 (%) | +0.0334 | 0.0612 | ±0.1223 | +0.546 | 0.5847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2307**, Adj R² = **0.1859**, F-statistic = **5.15** (p = **4.64e-07**), Residual SE = **13.522** on **189** df, AIC = **1629.0**, BIC = **1668.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.7477** | 8.2676 | ±16.5351 | **+6.622** | **3.54e-11** | *** |
| Education: graduate level (vs college) | -3.0844 | 2.0757 | ±4.1515 | -1.486 | 0.1373 |  |
| Education: high school or below (vs college) | +4.0403 | 3.3794 | ±6.7588 | +1.196 | 0.2319 |  |
| Site: UCSD (vs UAB) | -0.6224 | 2.6692 | ±5.3383 | -0.233 | 0.8156 |  |
| Site: UW (vs UAB) | +2.2559 | 2.3996 | ±4.7992 | +0.940 | 0.3472 |  |
| **Age (years)** | **-0.4860** | 0.0879 | ±0.1757 | **-5.531** | **3.19e-08** | *** |
| BMI (kg/m2) | +0.0410 | 0.1339 | ±0.2678 | +0.306 | 0.7593 |  |
| Hypertension | -1.2118 | 2.4635 | ±4.9270 | -0.492 | 0.6228 |  |
| High cholesterol | -0.0919 | 2.2452 | ±4.4903 | -0.041 | 0.9674 |  |
| Kidney disease | -4.1053 | 2.5882 | ±5.1764 | -1.586 | 0.1127 |  |
| Circulatory disease | -3.3420 | 2.0327 | ±4.0653 | -1.644 | 0.1001 |  |
| Time < 54 (%) | -1.1698 | 1.5336 | ±3.0672 | -0.763 | 0.4456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **201**, R² = **0.2331**, Adj R² = **0.1885**, F-statistic = **5.22** (p = **3.61e-07**), Residual SE = **13.501** on **189** df, AIC = **1628.3**, BIC = **1668.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4944** | 8.2209 | ±16.4418 | **+6.629** | **3.39e-11** | *** |
| Education: graduate level (vs college) | -3.1811 | 2.0882 | ±4.1764 | -1.523 | 0.1277 |  |
| Education: high school or below (vs college) | +3.9949 | 3.3776 | ±6.7552 | +1.183 | 0.2369 |  |
| Site: UCSD (vs UAB) | -0.6490 | 2.6710 | ±5.3420 | -0.243 | 0.8080 |  |
| Site: UW (vs UAB) | +2.2651 | 2.3848 | ±4.7697 | +0.950 | 0.3422 |  |
| **Age (years)** | **-0.4804** | 0.0885 | ±0.1770 | **-5.429** | **5.66e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.1326 | ±0.2652 | +0.295 | 0.7682 |  |
| Hypertension | -1.2430 | 2.4625 | ±4.9251 | -0.505 | 0.6137 |  |
| High cholesterol | -0.1852 | 2.2451 | ±4.4902 | -0.082 | 0.9343 |  |
| Kidney disease | -4.0305 | 2.5896 | ±5.1793 | -1.556 | 0.1196 |  |
| Circulatory disease | -3.2962 | 2.0273 | ±4.0545 | -1.626 | 0.1040 |  |
| Avg. daily time < 54 (%) | -1.3682 | 1.2412 | ±2.4824 | -1.102 | 0.2703 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2286**, Adj R² = **0.1837**, F-statistic = **5.09** (p = **5.79e-07**), Residual SE = **13.540** on **189** df, AIC = **1629.5**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4538** | 8.2628 | ±16.5256 | **+6.590** | **4.39e-11** | *** |
| Education: graduate level (vs college) | -3.1684 | 2.0718 | ±4.1435 | -1.529 | 0.1262 |  |
| Education: high school or below (vs college) | +4.2934 | 3.4016 | ±6.8033 | +1.262 | 0.2069 |  |
| Site: UCSD (vs UAB) | -0.4679 | 2.6436 | ±5.2872 | -0.177 | 0.8595 |  |
| Site: UW (vs UAB) | +2.5342 | 2.3521 | ±4.7043 | +1.077 | 0.2813 |  |
| **Age (years)** | **-0.4812** | 0.0900 | ±0.1801 | **-5.344** | **9.10e-08** | *** |
| BMI (kg/m2) | +0.0380 | 0.1341 | ±0.2683 | +0.283 | 0.7771 |  |
| Hypertension | -1.3459 | 2.4656 | ±4.9312 | -0.546 | 0.5852 |  |
| High cholesterol | -0.0872 | 2.2519 | ±4.5038 | -0.039 | 0.9691 |  |
| Kidney disease | -4.0368 | 2.5951 | ±5.1902 | -1.556 | 0.1198 |  |
| Circulatory disease | -3.5173 | 2.0180 | ±4.0361 | -1.743 | 0.0813 | . |
| Time 54-69, pooled (%) | -0.2254 | 0.2761 | ±0.5523 | -0.816 | 0.4144 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **201**, R² = **0.2291**, Adj R² = **0.1843**, F-statistic = **5.11** (p = **5.47e-07**), Residual SE = **13.535** on **189** df, AIC = **1629.4**, BIC = **1669.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3445** | 8.2822 | ±16.5644 | **+6.562** | **5.32e-11** | *** |
| Education: graduate level (vs college) | -3.1895 | 2.0721 | ±4.1442 | -1.539 | 0.1237 |  |
| Education: high school or below (vs college) | +4.3262 | 3.4061 | ±6.8122 | +1.270 | 0.2040 |  |
| Site: UCSD (vs UAB) | -0.4744 | 2.6444 | ±5.2889 | -0.179 | 0.8576 |  |
| Site: UW (vs UAB) | +2.5237 | 2.3564 | ±4.7128 | +1.071 | 0.2842 |  |
| **Age (years)** | **-0.4788** | 0.0907 | ±0.1815 | **-5.276** | **1.32e-07** | *** |
| BMI (kg/m2) | +0.0378 | 0.1338 | ±0.2676 | +0.283 | 0.7775 |  |
| Hypertension | -1.3453 | 2.4656 | ±4.9312 | -0.546 | 0.5853 |  |
| High cholesterol | -0.0905 | 2.2519 | ±4.5038 | -0.040 | 0.9679 |  |
| Kidney disease | -4.0302 | 2.5949 | ±5.1898 | -1.553 | 0.1204 |  |
| Circulatory disease | -3.5195 | 2.0182 | ±4.0365 | -1.744 | 0.0812 | . |
| Avg. daily time 54-69 (%) | -0.2504 | 0.2673 | ±0.5346 | -0.937 | 0.3489 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **201**, R² = **0.2293**, Adj R² = **0.1844**, F-statistic = **5.11** (p = **5.39e-07**), Residual SE = **13.534** on **189** df, AIC = **1629.3**, BIC = **1669.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.5264** | 8.2582 | ±16.5165 | **+6.603** | **4.04e-11** | *** |
| Education: graduate level (vs college) | -3.1930 | 2.0736 | ±4.1473 | -1.540 | 0.1236 |  |
| Education: high school or below (vs college) | +4.2552 | 3.3918 | ±6.7836 | +1.255 | 0.2096 |  |
| Site: UCSD (vs UAB) | -0.5175 | 2.6420 | ±5.2841 | -0.196 | 0.8447 |  |
| Site: UW (vs UAB) | +2.4677 | 2.3549 | ±4.7099 | +1.048 | 0.2947 |  |
| **Age (years)** | **-0.4808** | 0.0895 | ±0.1790 | **-5.371** | **7.83e-08** | *** |
| BMI (kg/m2) | +0.0383 | 0.1343 | ±0.2687 | +0.285 | 0.7755 |  |
| Hypertension | -1.3248 | 2.4583 | ±4.9167 | -0.539 | 0.5900 |  |
| High cholesterol | -0.0809 | 2.2497 | ±4.4995 | -0.036 | 0.9713 |  |
| Kidney disease | -4.0441 | 2.5908 | ±5.1816 | -1.561 | 0.1185 |  |
| Circulatory disease | -3.4792 | 2.0201 | ±4.0402 | -1.722 | 0.0850 | . |
| Time < 70 (%) | -0.2257 | 0.2325 | ±0.4651 | -0.971 | 0.3317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **201**, R² = **0.2303**, Adj R² = **0.1855**, F-statistic = **5.14** (p = **4.84e-07**), Residual SE = **13.525** on **189** df, AIC = **1629.1**, BIC = **1668.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3667** | 8.2693 | ±16.5386 | **+6.575** | **4.88e-11** | *** |
| Education: graduate level (vs college) | -3.2384 | 2.0774 | ±4.1548 | -1.559 | 0.1190 |  |
| Education: high school or below (vs college) | +4.2829 | 3.3925 | ±6.7850 | +1.262 | 0.2068 |  |
| Site: UCSD (vs UAB) | -0.5310 | 2.6438 | ±5.2875 | -0.201 | 0.8408 |  |
| Site: UW (vs UAB) | +2.4582 | 2.3606 | ±4.7212 | +1.041 | 0.2977 |  |
| **Age (years)** | **-0.4770** | 0.0903 | ±0.1807 | **-5.281** | **1.29e-07** | *** |
| BMI (kg/m2) | +0.0377 | 0.1337 | ±0.2674 | +0.282 | 0.7778 |  |
| Hypertension | -1.3312 | 2.4599 | ±4.9199 | -0.541 | 0.5884 |  |
| High cholesterol | -0.1009 | 2.2483 | ±4.4966 | -0.045 | 0.9642 |  |
| Kidney disease | -4.0222 | 2.5914 | ±5.1828 | -1.552 | 0.1206 |  |
| Circulatory disease | -3.4731 | 2.0196 | ±4.0392 | -1.720 | 0.0855 | . |
| Avg. daily time < 70 (%) | -0.2579 | 0.2233 | ±0.4466 | -1.155 | 0.2481 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2287**, Adj R² = **0.1838**, F-statistic = **5.09** (p = **5.72e-07**), Residual SE = **13.539** on **189** df, AIC = **1629.5**, BIC = **1669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5044** | 14.4216 | ±28.8432 | **+3.363** | **7.70e-04** | *** |
| Education: graduate level (vs college) | -3.0724 | 2.0799 | ±4.1599 | -1.477 | 0.1396 |  |
| Education: high school or below (vs college) | +4.3551 | 3.3992 | ±6.7984 | +1.281 | 0.2001 |  |
| Site: UCSD (vs UAB) | -0.4303 | 2.7516 | ±5.5032 | -0.156 | 0.8757 |  |
| Site: UW (vs UAB) | +2.4623 | 2.3665 | ±4.7329 | +1.041 | 0.2981 |  |
| **Age (years)** | **-0.4888** | 0.0885 | ±0.1770 | **-5.522** | **3.36e-08** | *** |
| BMI (kg/m2) | +0.0363 | 0.1334 | ±0.2667 | +0.272 | 0.7856 |  |
| Hypertension | -1.3116 | 2.4732 | ±4.9463 | -0.530 | 0.5959 |  |
| High cholesterol | -0.1748 | 2.2541 | ±4.5082 | -0.078 | 0.9382 |  |
| Kidney disease | -3.9393 | 2.6128 | ±5.2256 | -1.508 | 0.1316 |  |
| Circulatory disease | -3.4408 | 2.0515 | ±4.1029 | -1.677 | 0.0935 | . |
| Time 54-250, pooled (%) | +0.0629 | 0.1302 | ±0.2605 | +0.483 | 0.6289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2275**, Adj R² = **0.1826**, F-statistic = **5.06** (p = **6.46e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2215** | 15.4750 | ±30.9500 | **+3.310** | **9.33e-04** | *** |
| Education: graduate level (vs college) | -3.0189 | 2.0844 | ±4.1689 | -1.448 | 0.1475 |  |
| Education: high school or below (vs college) | +4.3037 | 3.3986 | ±6.7972 | +1.266 | 0.2054 |  |
| Site: UCSD (vs UAB) | -0.3935 | 2.7390 | ±5.4779 | -0.144 | 0.8858 |  |
| Site: UW (vs UAB) | +2.5395 | 2.3660 | ±4.7320 | +1.073 | 0.2831 |  |
| **Age (years)** | **-0.4881** | 0.0885 | ±0.1771 | **-5.512** | **3.54e-08** | *** |
| BMI (kg/m2) | +0.0373 | 0.1338 | ±0.2676 | +0.279 | 0.7802 |  |
| Hypertension | -1.3176 | 2.4788 | ±4.9577 | -0.532 | 0.5950 |  |
| High cholesterol | -0.1464 | 2.2566 | ±4.5133 | -0.065 | 0.9483 |  |
| Kidney disease | -3.9928 | 2.5994 | ±5.1988 | -1.536 | 0.1245 |  |
| Circulatory disease | -3.4814 | 2.0464 | ±4.0928 | -1.701 | 0.0889 | . |
| Avg. daily time 54-250 (%) | +0.0334 | 0.1417 | ±0.2834 | +0.236 | 0.8136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2277**, Adj R² = **0.1828**, F-statistic = **5.07** (p = **6.35e-07**), Residual SE = **13.548** on **189** df, AIC = **1629.8**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4972** | 8.3973 | ±16.7945 | **+6.490** | **8.59e-11** | *** |
| Education: graduate level (vs college) | -3.0445 | 2.1111 | ±4.2222 | -1.442 | 0.1493 |  |
| Education: high school or below (vs college) | +4.2534 | 3.3917 | ±6.7835 | +1.254 | 0.2098 |  |
| Site: UCSD (vs UAB) | -0.3747 | 2.7298 | ±5.4596 | -0.137 | 0.8908 |  |
| Site: UW (vs UAB) | +2.6068 | 2.3480 | ±4.6961 | +1.110 | 0.2669 |  |
| **Age (years)** | **-0.4846** | 0.0872 | ±0.1744 | **-5.558** | **2.72e-08** | *** |
| BMI (kg/m2) | +0.0383 | 0.1347 | ±0.2693 | +0.285 | 0.7760 |  |
| Hypertension | -1.3793 | 2.4656 | ±4.9313 | -0.559 | 0.5759 |  |
| High cholesterol | -0.0497 | 2.2842 | ±4.5684 | -0.022 | 0.9826 |  |
| Kidney disease | -3.9146 | 2.6467 | ±5.2935 | -1.479 | 0.1391 |  |
| Circulatory disease | -3.5162 | 2.0268 | ±4.0536 | -1.735 | 0.0828 | . |
| Time 181-250, pooled (%) | -0.0284 | 0.0886 | ±0.1773 | -0.320 | 0.7487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **201**, R² = **0.2285**, Adj R² = **0.1836**, F-statistic = **5.09** (p = **5.85e-07**), Residual SE = **13.541** on **189** df, AIC = **1629.5**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6553** | 8.4414 | ±16.8828 | **+6.475** | **9.50e-11** | *** |
| Education: graduate level (vs college) | -3.0899 | 2.1027 | ±4.2055 | -1.469 | 0.1417 |  |
| Education: high school or below (vs college) | +4.2745 | 3.3936 | ±6.7872 | +1.260 | 0.2078 |  |
| Site: UCSD (vs UAB) | -0.4003 | 2.7498 | ±5.4996 | -0.146 | 0.8843 |  |
| Site: UW (vs UAB) | +2.5863 | 2.3507 | ±4.7014 | +1.100 | 0.2712 |  |
| **Age (years)** | **-0.4836** | 0.0874 | ±0.1747 | **-5.536** | **3.10e-08** | *** |
| BMI (kg/m2) | +0.0373 | 0.1347 | ±0.2693 | +0.277 | 0.7816 |  |
| Hypertension | -1.4200 | 2.4684 | ±4.9367 | -0.575 | 0.5651 |  |
| High cholesterol | -0.0107 | 2.2817 | ±4.5633 | -0.005 | 0.9963 |  |
| Kidney disease | -3.8332 | 2.6443 | ±5.2886 | -1.450 | 0.1472 |  |
| Circulatory disease | -3.5028 | 2.0299 | ±4.0599 | -1.726 | 0.0844 | . |
| Avg. daily time 181-250 (%) | -0.0437 | 0.0845 | ±0.1690 | -0.517 | 0.6051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **201**, R² = **0.2282**, Adj R² = **0.1833**, F-statistic = **5.08** (p = **6.02e-07**), Residual SE = **13.544** on **189** df, AIC = **1629.6**, BIC = **1669.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6577** | 8.4334 | ±16.8667 | **+6.481** | **9.10e-11** | *** |
| Education: graduate level (vs college) | -3.0828 | 2.1009 | ±4.2019 | -1.467 | 0.1423 |  |
| Education: high school or below (vs college) | +4.3055 | 3.3936 | ±6.7873 | +1.269 | 0.2046 |  |
| Site: UCSD (vs UAB) | -0.3952 | 2.7476 | ±5.4953 | -0.144 | 0.8856 |  |
| Site: UW (vs UAB) | +2.5565 | 2.3589 | ±4.7178 | +1.084 | 0.2785 |  |
| **Age (years)** | **-0.4852** | 0.0880 | ±0.1760 | **-5.513** | **3.53e-08** | *** |
| BMI (kg/m2) | +0.0371 | 0.1345 | ±0.2690 | +0.276 | 0.7827 |  |
| Hypertension | -1.3734 | 2.4763 | ±4.9526 | -0.555 | 0.5792 |  |
| High cholesterol | -0.0769 | 2.2690 | ±4.5379 | -0.034 | 0.9729 |  |
| Kidney disease | -3.8717 | 2.6308 | ±5.2617 | -1.472 | 0.1411 |  |
| Circulatory disease | -3.4812 | 2.0363 | ±4.0726 | -1.710 | 0.0873 | . |
| Time > 180 (%) | -0.0263 | 0.0603 | ±0.1207 | -0.436 | 0.6631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2281**, Adj R² = **0.1831**, F-statistic = **5.08** (p = **6.12e-07**), Residual SE = **13.545** on **189** df, AIC = **1629.7**, BIC = **1669.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6653** | 8.4524 | ±16.9048 | **+6.467** | **9.97e-11** | *** |
| Education: graduate level (vs college) | -3.0711 | 2.1002 | ±4.2003 | -1.462 | 0.1436 |  |
| Education: high school or below (vs college) | +4.3100 | 3.3952 | ±6.7904 | +1.269 | 0.2043 |  |
| Site: UCSD (vs UAB) | -0.3999 | 2.7501 | ±5.5003 | -0.145 | 0.8844 |  |
| Site: UW (vs UAB) | +2.5545 | 2.3599 | ±4.7198 | +1.082 | 0.2791 |  |
| **Age (years)** | **-0.4857** | 0.0880 | ±0.1760 | **-5.518** | **3.42e-08** | *** |
| BMI (kg/m2) | +0.0368 | 0.1347 | ±0.2693 | +0.273 | 0.7847 |  |
| Hypertension | -1.3746 | 2.4778 | ±4.9556 | -0.555 | 0.5791 |  |
| High cholesterol | -0.0762 | 2.2716 | ±4.5432 | -0.034 | 0.9732 |  |
| Kidney disease | -3.8843 | 2.6241 | ±5.2482 | -1.480 | 0.1388 |  |
| Circulatory disease | -3.4814 | 2.0349 | ±4.0698 | -1.711 | 0.0871 | . |
| Avg. daily time > 180 (%) | -0.0242 | 0.0604 | ±0.1208 | -0.401 | 0.6886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2280**, Adj R² = **0.1830**, F-statistic = **5.07** (p = **6.18e-07**), Residual SE = **13.546** on **189** df, AIC = **1629.7**, BIC = **1669.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.5834** | 8.4011 | ±16.8021 | **+6.497** | **8.18e-11** | *** |
| Education: graduate level (vs college) | -3.0402 | 2.0854 | ±4.1707 | -1.458 | 0.1449 |  |
| Education: high school or below (vs college) | +4.2603 | 3.3989 | ±6.7978 | +1.253 | 0.2100 |  |
| Site: UCSD (vs UAB) | -0.3762 | 2.7475 | ±5.4949 | -0.137 | 0.8911 |  |
| Site: UW (vs UAB) | +2.5596 | 2.3544 | ±4.7088 | +1.087 | 0.2770 |  |
| **Age (years)** | **-0.4882** | 0.0885 | ±0.1770 | **-5.516** | **3.47e-08** | *** |
| BMI (kg/m2) | +0.0390 | 0.1334 | ±0.2668 | +0.292 | 0.7701 |  |
| Hypertension | -1.3039 | 2.4715 | ±4.9431 | -0.528 | 0.5978 |  |
| High cholesterol | -0.0761 | 2.2770 | ±4.5540 | -0.033 | 0.9734 |  |
| Kidney disease | -3.9812 | 2.6238 | ±5.2477 | -1.517 | 0.1292 |  |
| Circulatory disease | -3.4617 | 2.0337 | ±4.0675 | -1.702 | 0.0887 | . |
| Nocturnal time > 180 (%) | -0.0222 | 0.0638 | ±0.1275 | -0.348 | 0.7278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2284**, Adj R² = **0.1835**, F-statistic = **5.09** (p = **5.89e-07**), Residual SE = **13.542** on **189** df, AIC = **1629.6**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.1356** | 8.3542 | ±16.7083 | **+6.480** | **9.17e-11** | *** |
| Education: graduate level (vs college) | -2.7990 | 2.1293 | ±4.2587 | -1.314 | 0.1887 |  |
| Education: high school or below (vs college) | +4.1581 | 3.4085 | ±6.8170 | +1.220 | 0.2225 |  |
| Site: UCSD (vs UAB) | -0.3964 | 2.6643 | ±5.3287 | -0.149 | 0.8817 |  |
| Site: UW (vs UAB) | +2.4767 | 2.2927 | ±4.5853 | +1.080 | 0.2800 |  |
| **Age (years)** | **-0.4978** | 0.0883 | ±0.1765 | **-5.639** | **1.71e-08** | *** |
| BMI (kg/m2) | +0.0477 | 0.1381 | ±0.2762 | +0.346 | 0.7297 |  |
| Hypertension | -1.3116 | 2.4684 | ±4.9368 | -0.531 | 0.5952 |  |
| High cholesterol | -0.1612 | 2.2722 | ±4.5444 | -0.071 | 0.9434 |  |
| Kidney disease | -4.3331 | 2.5894 | ±5.1787 | -1.673 | 0.0942 | . |
| Circulatory disease | -3.5347 | 2.0166 | ±4.0331 | -1.753 | 0.0796 | . |
| Any reading > 250 during wear (0/1) | +1.1171 | 2.1523 | ±4.3046 | +0.519 | 0.6038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2284**, Adj R² = **0.1835**, F-statistic = **5.08** (p = **5.93e-07**), Residual SE = **13.542** on **189** df, AIC = **1629.6**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.7317** | 8.3446 | ±16.6891 | **+6.559** | **5.42e-11** | *** |
| Education: graduate level (vs college) | -3.0533 | 2.0791 | ±4.1582 | -1.469 | 0.1420 |  |
| Education: high school or below (vs college) | +4.3511 | 3.4003 | ±6.8006 | +1.280 | 0.2007 |  |
| Site: UCSD (vs UAB) | -0.4107 | 2.7427 | ±5.4853 | -0.150 | 0.8810 |  |
| Site: UW (vs UAB) | +2.4946 | 2.3613 | ±4.7225 | +1.056 | 0.2907 |  |
| **Age (years)** | **-0.4888** | 0.0886 | ±0.1771 | **-5.520** | **3.39e-08** | *** |
| BMI (kg/m2) | +0.0365 | 0.1334 | ±0.2668 | +0.274 | 0.7841 |  |
| Hypertension | -1.3180 | 2.4763 | ±4.9527 | -0.532 | 0.5946 |  |
| High cholesterol | -0.1706 | 2.2549 | ±4.5099 | -0.076 | 0.9397 |  |
| Kidney disease | -3.9522 | 2.6121 | ±5.2242 | -1.513 | 0.1303 |  |
| Circulatory disease | -3.4616 | 2.0502 | ±4.1003 | -1.688 | 0.0913 | . |
| Time > 250 (%) | -0.0557 | 0.1309 | ±0.2617 | -0.426 | 0.6705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2273**, Adj R² = **0.1823**, F-statistic = **5.05** (p = **6.61e-07**), Residual SE = **13.552** on **189** df, AIC = **1629.9**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4826** | 8.3513 | ±16.7026 | **+6.524** | **6.85e-11** | *** |
| Education: graduate level (vs college) | -2.9908 | 2.0825 | ±4.1649 | -1.436 | 0.1509 |  |
| Education: high school or below (vs college) | +4.2803 | 3.3981 | ±6.7962 | +1.260 | 0.2078 |  |
| Site: UCSD (vs UAB) | -0.3781 | 2.7273 | ±5.4547 | -0.139 | 0.8897 |  |
| Site: UW (vs UAB) | +2.5694 | 2.3616 | ±4.7231 | +1.088 | 0.2766 |  |
| **Age (years)** | **-0.4882** | 0.0886 | ±0.1771 | **-5.513** | **3.52e-08** | *** |
| BMI (kg/m2) | +0.0382 | 0.1338 | ±0.2677 | +0.285 | 0.7756 |  |
| Hypertension | -1.3203 | 2.4818 | ±4.9637 | -0.532 | 0.5947 |  |
| High cholesterol | -0.1366 | 2.2579 | ±4.5159 | -0.060 | 0.9518 |  |
| Kidney disease | -4.0239 | 2.5957 | ±5.1913 | -1.550 | 0.1211 |  |
| Circulatory disease | -3.5087 | 2.0425 | ±4.0850 | -1.718 | 0.0858 | . |
| Avg. daily time > 250 (%) | -0.0197 | 0.1417 | ±0.2835 | -0.139 | 0.8897 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 203; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1632**, F-statistic = **4.94** (p = **2.30e-06**), Residual SE = **7.894** on **192** df, AIC = **1425.6**, BIC = **1462.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8645** | 4.6906 | ±9.3813 | **+15.747** | **7.18e-56** | *** |
| **Education: graduate level (vs college)** | **-3.4724** | 1.3207 | ±2.6414 | **-2.629** | **0.0086** | ** |
| Education: high school or below (vs college) | -1.0447 | 1.5160 | ±3.0320 | -0.689 | 0.4908 |  |
| Site: UCSD (vs UAB) | -2.3582 | 1.4896 | ±2.9793 | -1.583 | 0.1134 |  |
| Site: UW (vs UAB) | +0.4190 | 1.5193 | ±3.0386 | +0.276 | 0.7827 |  |
| **Age (years)** | **-0.1835** | 0.0527 | ±0.1054 | **-3.481** | **4.99e-04** | *** |
| **BMI (kg/m2)** | **+0.1677** | 0.0727 | ±0.1455 | **+2.305** | **0.0211** | * |
| Hypertension | +0.5910 | 1.4383 | ±2.8766 | +0.411 | 0.6811 |  |
| High cholesterol | -0.2098 | 1.1606 | ±2.3212 | -0.181 | 0.8566 |  |
| Kidney disease | +0.7400 | 1.6563 | ±3.3125 | +0.447 | 0.6550 |  |
| Circulatory disease | -2.0248 | 1.3627 | ±2.7255 | -1.486 | 0.1373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **203**, R² = **0.2066**, Adj R² = **0.1609**, F-statistic = **4.52** (p = **4.46e-06**), Residual SE = **7.905** on **191** df, AIC = **1427.1**, BIC = **1466.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.0934** | 5.7682 | ±11.5364 | **+12.498** | **7.61e-36** | *** |
| **Education: graduate level (vs college)** | **-3.3602** | 1.3534 | ±2.7068 | **-2.483** | **0.0130** | * |
| Education: high school or below (vs college) | -1.1488 | 1.4884 | ±2.9768 | -0.772 | 0.4402 |  |
| Site: UCSD (vs UAB) | -2.3245 | 1.4879 | ±2.9758 | -1.562 | 0.1182 |  |
| Site: UW (vs UAB) | +0.4546 | 1.5225 | ±3.0449 | +0.299 | 0.7652 |  |
| **Age (years)** | **-0.1894** | 0.0530 | ±0.1060 | **-3.573** | **3.52e-04** | *** |
| **BMI (kg/m2)** | **+0.1655** | 0.0724 | ±0.1447 | **+2.287** | **0.0222** | * |
| Hypertension | +0.5803 | 1.4439 | ±2.8878 | +0.402 | 0.6878 |  |
| High cholesterol | -0.1817 | 1.1632 | ±2.3264 | -0.156 | 0.8758 |  |
| Kidney disease | +0.7362 | 1.6394 | ±3.2788 | +0.449 | 0.6534 |  |
| Circulatory disease | -2.0073 | 1.3715 | ±2.7429 | -1.464 | 0.1433 |  |
| HbA1c (%) | +0.3358 | 0.5894 | ±1.1789 | +0.570 | 0.5689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **203**, R² = **0.2052**, Adj R² = **0.1594**, F-statistic = **4.48** (p = **5.11e-06**), Residual SE = **7.912** on **191** df, AIC = **1427.5**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.0511** | 5.5213 | ±11.0426 | **+13.231** | **5.82e-40** | *** |
| **Education: graduate level (vs college)** | **-3.4467** | 1.3385 | ±2.6770 | **-2.575** | **0.0100** | * |
| Education: high school or below (vs college) | -1.0935 | 1.5139 | ±3.0279 | -0.722 | 0.4701 |  |
| Site: UCSD (vs UAB) | -2.3659 | 1.4945 | ±2.9891 | -1.583 | 0.1134 |  |
| Site: UW (vs UAB) | +0.4332 | 1.5241 | ±3.0481 | +0.284 | 0.7762 |  |
| **Age (years)** | **-0.1838** | 0.0528 | ±0.1056 | **-3.480** | **5.02e-04** | *** |
| **BMI (kg/m2)** | **+0.1679** | 0.0731 | ±0.1462 | **+2.297** | **0.0216** | * |
| Hypertension | +0.5932 | 1.4492 | ±2.8984 | +0.409 | 0.6823 |  |
| High cholesterol | -0.2090 | 1.1694 | ±2.3388 | -0.179 | 0.8581 |  |
| Kidney disease | +0.6898 | 1.6503 | ±3.3007 | +0.418 | 0.6760 |  |
| Circulatory disease | -2.0356 | 1.3799 | ±2.7598 | -1.475 | 0.1402 |  |
| Mean glucose (mg/dL) | +0.0061 | 0.0194 | ±0.0387 | +0.314 | 0.7537 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **203**, R² = **0.2052**, Adj R² = **0.1594**, F-statistic = **4.48** (p = **5.11e-06**), Residual SE = **7.912** on **191** df, AIC = **1427.5**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.2102** | 7.2940 | ±14.5881 | **+9.900** | **4.17e-23** | *** |
| **Education: graduate level (vs college)** | **-3.4467** | 1.3385 | ±2.6770 | **-2.575** | **0.0100** | * |
| Education: high school or below (vs college) | -1.0935 | 1.5139 | ±3.0279 | -0.722 | 0.4701 |  |
| Site: UCSD (vs UAB) | -2.3659 | 1.4945 | ±2.9891 | -1.583 | 0.1134 |  |
| Site: UW (vs UAB) | +0.4332 | 1.5241 | ±3.0481 | +0.284 | 0.7762 |  |
| **Age (years)** | **-0.1838** | 0.0528 | ±0.1056 | **-3.480** | **5.02e-04** | *** |
| **BMI (kg/m2)** | **+0.1679** | 0.0731 | ±0.1462 | **+2.297** | **0.0216** | * |
| Hypertension | +0.5932 | 1.4492 | ±2.8984 | +0.409 | 0.6823 |  |
| High cholesterol | -0.2090 | 1.1694 | ±2.3388 | -0.179 | 0.8581 |  |
| Kidney disease | +0.6898 | 1.6503 | ±3.3007 | +0.418 | 0.6760 |  |
| Circulatory disease | -2.0356 | 1.3799 | ±2.7598 | -1.475 | 0.1402 |  |
| GMI (%) | +0.2541 | 0.8097 | ±1.6195 | +0.314 | 0.7537 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **203**, R² = **0.2055**, Adj R² = **0.1597**, F-statistic = **4.49** (p = **4.96e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.8571** | 5.3942 | ±10.7883 | **+13.507** | **1.43e-41** | *** |
| **Education: graduate level (vs college)** | **-3.4651** | 1.3276 | ±2.6553 | **-2.610** | **0.0091** | ** |
| Education: high school or below (vs college) | -1.0996 | 1.5051 | ±3.0101 | -0.731 | 0.4650 |  |
| Site: UCSD (vs UAB) | -2.3736 | 1.4947 | ±2.9894 | -1.588 | 0.1123 |  |
| Site: UW (vs UAB) | +0.4254 | 1.5201 | ±3.0402 | +0.280 | 0.7796 |  |
| **Age (years)** | **-0.1823** | 0.0531 | ±0.1063 | **-3.431** | **6.02e-04** | *** |
| **BMI (kg/m2)** | **+0.1672** | 0.0729 | ±0.1458 | **+2.294** | **0.0218** | * |
| Hypertension | +0.5718 | 1.4538 | ±2.9076 | +0.393 | 0.6941 |  |
| High cholesterol | -0.2195 | 1.1674 | ±2.3348 | -0.188 | 0.8508 |  |
| Kidney disease | +0.7245 | 1.6385 | ±3.2770 | +0.442 | 0.6584 |  |
| Circulatory disease | -2.0450 | 1.3810 | ±2.7620 | -1.481 | 0.1387 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0075 | 0.0170 | ±0.0339 | +0.441 | 0.6591 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.01e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.2172** | 4.8309 | ±9.6619 | **+15.363** | **2.90e-53** | *** |
| **Education: graduate level (vs college)** | **-3.5459** | 1.3650 | ±2.7299 | **-2.598** | **0.0094** | ** |
| Education: high school or below (vs college) | -0.9284 | 1.5591 | ±3.1181 | -0.595 | 0.5515 |  |
| Site: UCSD (vs UAB) | -2.3633 | 1.4998 | ±2.9995 | -1.576 | 0.1151 |  |
| Site: UW (vs UAB) | +0.3876 | 1.5296 | ±3.0592 | +0.253 | 0.7999 |  |
| **Age (years)** | **-0.1797** | 0.0544 | ±0.1088 | **-3.303** | **9.58e-04** | *** |
| **BMI (kg/m2)** | **+0.1662** | 0.0740 | ±0.1480 | **+2.246** | **0.0247** | * |
| Hypertension | +0.5805 | 1.4408 | ±2.8817 | +0.403 | 0.6871 |  |
| High cholesterol | -0.2149 | 1.1676 | ±2.3351 | -0.184 | 0.8540 |  |
| Kidney disease | +0.8817 | 1.7250 | ±3.4500 | +0.511 | 0.6093 |  |
| Circulatory disease | -2.0396 | 1.3652 | ±2.7304 | -1.494 | 0.1352 |  |
| Glucose SD, pooled (mg/dL) | -0.0154 | 0.0447 | ±0.0895 | -0.345 | 0.7304 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **203**, R² = **0.2065**, Adj R² = **0.1608**, F-statistic = **4.52** (p = **4.50e-06**), Residual SE = **7.906** on **191** df, AIC = **1427.2**, BIC = **1466.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.4912** | 4.8591 | ±9.7183 | **+15.330** | **4.81e-53** | *** |
| **Education: graduate level (vs college)** | **-3.5920** | 1.3622 | ±2.7244 | **-2.637** | **0.0084** | ** |
| Education: high school or below (vs college) | -0.8284 | 1.5762 | ±3.1525 | -0.526 | 0.5992 |  |
| Site: UCSD (vs UAB) | -2.3715 | 1.5010 | ±3.0020 | -1.580 | 0.1141 |  |
| Site: UW (vs UAB) | +0.3782 | 1.5289 | ±3.0578 | +0.247 | 0.8046 |  |
| **Age (years)** | **-0.1775** | 0.0542 | ±0.1084 | **-3.277** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1643** | 0.0742 | ±0.1485 | **+2.214** | **0.0269** | * |
| Hypertension | +0.5631 | 1.4378 | ±2.8756 | +0.392 | 0.6953 |  |
| High cholesterol | -0.2051 | 1.1671 | ±2.3342 | -0.176 | 0.8605 |  |
| Kidney disease | +0.9681 | 1.7292 | ±3.4584 | +0.560 | 0.5756 |  |
| Circulatory disease | -2.0573 | 1.3619 | ±2.7238 | -1.511 | 0.1309 |  |
| Avg. daily SD (mg/dL) | -0.0291 | 0.0534 | ±0.1068 | -0.545 | 0.5858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **203**, R² = **0.2072**, Adj R² = **0.1616**, F-statistic = **4.54** (p = **4.18e-06**), Residual SE = **7.902** on **191** df, AIC = **1427.0**, BIC = **1466.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9233** | 4.9573 | ±9.9146 | **+15.114** | **1.31e-51** | *** |
| **Education: graduate level (vs college)** | **-3.6510** | 1.3812 | ±2.7624 | **-2.643** | **0.0082** | ** |
| Education: high school or below (vs college) | -0.7816 | 1.5583 | ±3.1165 | -0.502 | 0.6160 |  |
| Site: UCSD (vs UAB) | -2.3759 | 1.4976 | ±2.9953 | -1.586 | 0.1126 |  |
| Site: UW (vs UAB) | +0.3545 | 1.5278 | ±3.0557 | +0.232 | 0.8165 |  |
| **Age (years)** | **-0.1709** | 0.0567 | ±0.1134 | **-3.013** | **0.0026** | ** |
| **BMI (kg/m2)** | **+0.1640** | 0.0750 | ±0.1499 | **+2.187** | **0.0287** | * |
| Hypertension | +0.5527 | 1.4332 | ±2.8664 | +0.386 | 0.6998 |  |
| High cholesterol | -0.2047 | 1.1663 | ±2.3326 | -0.176 | 0.8607 |  |
| Kidney disease | +1.0687 | 1.7563 | ±3.5126 | +0.608 | 0.5429 |  |
| Circulatory disease | -2.0726 | 1.3772 | ±2.7543 | -1.505 | 0.1323 |  |
| CV (%) | -0.0692 | 0.1015 | ±0.2030 | -0.681 | 0.4956 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1589**, F-statistic = **4.47** (p = **5.37e-06**), Residual SE = **7.915** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6603** | 5.7887 | ±11.5774 | **+12.725** | **4.31e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4874** | 1.3954 | ±2.7908 | **-2.499** | **0.0124** | * |
| Education: high school or below (vs college) | -1.0213 | 1.5366 | ±3.0732 | -0.665 | 0.5063 |  |
| Site: UCSD (vs UAB) | -2.3559 | 1.4953 | ±2.9906 | -1.576 | 0.1151 |  |
| Site: UW (vs UAB) | +0.4163 | 1.5275 | ±3.0551 | +0.273 | 0.7852 |  |
| **Age (years)** | **-0.1823** | 0.0567 | ±0.1133 | **-3.218** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.1676** | 0.0734 | ±0.1468 | **+2.284** | **0.0224** | * |
| Hypertension | +0.5863 | 1.4337 | ±2.8674 | +0.409 | 0.6826 |  |
| High cholesterol | -0.2093 | 1.1685 | ±2.3370 | -0.179 | 0.8579 |  |
| Kidney disease | +0.7596 | 1.6966 | ±3.3933 | +0.448 | 0.6544 |  |
| Circulatory disease | -2.0237 | 1.3675 | ±2.7349 | -1.480 | 0.1389 |  |
| Mean / SD ratio | +0.0308 | 0.4953 | ±0.9906 | +0.062 | 0.9504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **203**, R² = **0.2049**, Adj R² = **0.1591**, F-statistic = **4.48** (p = **5.25e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.1637** | 5.7933 | ±11.5865 | **+12.629** | **1.46e-36** | *** |
| **Education: graduate level (vs college)** | **-3.5270** | 1.3955 | ±2.7910 | **-2.527** | **0.0115** | * |
| Education: high school or below (vs college) | -0.9616 | 1.5391 | ±3.0782 | -0.625 | 0.5321 |  |
| Site: UCSD (vs UAB) | -2.3447 | 1.4939 | ±2.9878 | -1.570 | 0.1165 |  |
| Site: UW (vs UAB) | +0.4175 | 1.5326 | ±3.0652 | +0.272 | 0.7853 |  |
| **Age (years)** | **-0.1793** | 0.0569 | ±0.1138 | **-3.151** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1669** | 0.0734 | ±0.1468 | **+2.274** | **0.0230** | * |
| Hypertension | +0.5681 | 1.4350 | ±2.8700 | +0.396 | 0.6922 |  |
| High cholesterol | -0.1978 | 1.1769 | ±2.3537 | -0.168 | 0.8665 |  |
| Kidney disease | +0.7861 | 1.6808 | ±3.3617 | +0.468 | 0.6400 |  |
| Circulatory disease | -2.0255 | 1.3683 | ±2.7366 | -1.480 | 0.1388 |  |
| Avg. daily mean/SD | +0.0896 | 0.4086 | ±0.8171 | +0.219 | 0.8263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **203**, R² = **0.2071**, Adj R² = **0.1614**, F-statistic = **4.53** (p = **4.24e-06**), Residual SE = **7.903** on **191** df, AIC = **1427.0**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.2351** | 4.8056 | ±9.6111 | **+15.656** | **3.03e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5718** | 1.3285 | ±2.6571 | **-2.688** | **0.0072** | ** |
| Education: high school or below (vs college) | -0.8275 | 1.5776 | ±3.1553 | -0.525 | 0.5999 |  |
| Site: UCSD (vs UAB) | -2.2979 | 1.4995 | ±2.9990 | -1.532 | 0.1254 |  |
| Site: UW (vs UAB) | +0.3194 | 1.5151 | ±3.0303 | +0.211 | 0.8331 |  |
| **Age (years)** | **-0.1799** | 0.0536 | ±0.1073 | **-3.353** | **7.98e-04** | *** |
| **BMI (kg/m2)** | **+0.1729** | 0.0730 | ±0.1460 | **+2.369** | **0.0178** | * |
| Hypertension | +0.5413 | 1.4454 | ±2.8909 | +0.374 | 0.7081 |  |
| High cholesterol | -0.1705 | 1.1709 | ±2.3419 | -0.146 | 0.8842 |  |
| Kidney disease | +0.7681 | 1.6534 | ±3.3068 | +0.465 | 0.6423 |  |
| Circulatory disease | -2.0371 | 1.3638 | ±2.7276 | -1.494 | 0.1353 |  |
| MAG (mg/dL/h) | -0.0390 | 0.0553 | ±0.1106 | -0.705 | 0.4809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **203**, R² = **0.2061**, Adj R² = **0.1604**, F-statistic = **4.51** (p = **4.66e-06**), Residual SE = **7.908** on **191** df, AIC = **1427.3**, BIC = **1467.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.6604** | 4.9277 | ±9.8553 | **+15.151** | **7.43e-52** | *** |
| **Education: graduate level (vs college)** | **-3.5844** | 1.3640 | ±2.7280 | **-2.628** | **0.0086** | ** |
| Education: high school or below (vs college) | -0.8371 | 1.5816 | ±3.1632 | -0.529 | 0.5966 |  |
| Site: UCSD (vs UAB) | -2.3556 | 1.5010 | ±3.0020 | -1.569 | 0.1166 |  |
| Site: UW (vs UAB) | +0.3943 | 1.5268 | ±3.0536 | +0.258 | 0.7962 |  |
| **Age (years)** | **-0.1784** | 0.0541 | ±0.1082 | **-3.298** | **9.75e-04** | *** |
| **BMI (kg/m2)** | **+0.1646** | 0.0740 | ±0.1479 | **+2.225** | **0.0261** | * |
| Hypertension | +0.5485 | 1.4361 | ±2.8723 | +0.382 | 0.7025 |  |
| High cholesterol | -0.1876 | 1.1699 | ±2.3398 | -0.160 | 0.8726 |  |
| Kidney disease | +0.9434 | 1.7180 | ±3.4359 | +0.549 | 0.5829 |  |
| Circulatory disease | -2.0295 | 1.3628 | ±2.7256 | -1.489 | 0.1364 |  |
| Avg. daily range (mg/dL) | -0.0074 | 0.0147 | ±0.0293 | -0.503 | 0.6147 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1597**, F-statistic = **4.49** (p = **5.00e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6678** | 4.7319 | ±9.4639 | **+15.568** | **1.20e-54** | *** |
| **Education: graduate level (vs college)** | **-3.3971** | 1.3579 | ±2.7157 | **-2.502** | **0.0124** | * |
| Education: high school or below (vs college) | -1.0710 | 1.5095 | ±3.0191 | -0.709 | 0.4780 |  |
| Site: UCSD (vs UAB) | -2.3711 | 1.4923 | ±2.9847 | -1.589 | 0.1121 |  |
| Site: UW (vs UAB) | +0.4532 | 1.5290 | ±3.0580 | +0.296 | 0.7669 |  |
| **Age (years)** | **-0.1856** | 0.0532 | ±0.1065 | **-3.487** | **4.88e-04** | *** |
| **BMI (kg/m2)** | **+0.1684** | 0.0728 | ±0.1457 | **+2.313** | **0.0207** | * |
| Hypertension | +0.5563 | 1.4591 | ±2.9183 | +0.381 | 0.7030 |  |
| High cholesterol | -0.1924 | 1.1657 | ±2.3314 | -0.165 | 0.8689 |  |
| Kidney disease | +0.6434 | 1.6565 | ±3.3129 | +0.388 | 0.6977 |  |
| Circulatory disease | -2.0500 | 1.3707 | ±2.7415 | -1.496 | 0.1348 |  |
| SD of daily means (mg/dL) | +0.0247 | 0.0538 | ±0.1075 | +0.460 | 0.6455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **203**, R² = **0.2053**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.03e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.5**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9445** | 5.3652 | ±10.7305 | **+13.969** | **2.43e-44** | *** |
| **Education: graduate level (vs college)** | **-3.4015** | 1.3654 | ±2.7307 | **-2.491** | **0.0127** | * |
| Education: high school or below (vs college) | -1.1008 | 1.5094 | ±3.0187 | -0.729 | 0.4658 |  |
| Site: UCSD (vs UAB) | -2.3526 | 1.4917 | ±2.9834 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4467 | 1.5313 | ±3.0626 | +0.292 | 0.7705 |  |
| **Age (years)** | **-0.1850** | 0.0527 | ±0.1054 | **-3.510** | **4.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1687** | 0.0733 | ±0.1466 | **+2.301** | **0.0214** | * |
| Hypertension | +0.6092 | 1.4423 | ±2.8846 | +0.422 | 0.6728 |  |
| High cholesterol | -0.2294 | 1.1703 | ±2.3405 | -0.196 | 0.8446 |  |
| Kidney disease | +0.6487 | 1.6676 | ±3.3351 | +0.389 | 0.6973 |  |
| Circulatory disease | -2.0495 | 1.3781 | ±2.7562 | -1.487 | 0.1370 |  |
| Time in range 70-180, pooled (%) | -0.0123 | 0.0349 | ±0.0699 | -0.353 | 0.7240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.02e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9578** | 5.2905 | ±10.5810 | **+14.168** | **1.44e-45** | *** |
| **Education: graduate level (vs college)** | **-3.4007** | 1.3658 | ±2.7315 | **-2.490** | **0.0128** | * |
| Education: high school or below (vs college) | -1.1085 | 1.5083 | ±3.0167 | -0.735 | 0.4624 |  |
| Site: UCSD (vs UAB) | -2.3496 | 1.4915 | ±2.9830 | -1.575 | 0.1152 |  |
| Site: UW (vs UAB) | +0.4496 | 1.5331 | ±3.0663 | +0.293 | 0.7693 |  |
| **Age (years)** | **-0.1850** | 0.0527 | ±0.1053 | **-3.513** | **4.43e-04** | *** |
| **BMI (kg/m2)** | **+0.1690** | 0.0735 | ±0.1469 | **+2.301** | **0.0214** | * |
| Hypertension | +0.6124 | 1.4412 | ±2.8824 | +0.425 | 0.6709 |  |
| High cholesterol | -0.2307 | 1.1684 | ±2.3368 | -0.197 | 0.8435 |  |
| Kidney disease | +0.6447 | 1.6668 | ±3.3337 | +0.387 | 0.6989 |  |
| Circulatory disease | -2.0520 | 1.3785 | ±2.7570 | -1.489 | 0.1366 |  |
| Avg. daily time in range 70-180 (%) | -0.0126 | 0.0338 | ±0.0677 | -0.371 | 0.7105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.2069**, Adj R² = **0.1612**, F-statistic = **4.53** (p = **4.33e-06**), Residual SE = **7.904** on **191** df, AIC = **1427.1**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6934** | 4.6881 | ±9.3761 | **+15.719** | **1.11e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4145** | 1.3205 | ±2.6409 | **-2.586** | **0.0097** | ** |
| Education: high school or below (vs college) | -0.9517 | 1.5316 | ±3.0632 | -0.621 | 0.5344 |  |
| Site: UCSD (vs UAB) | -2.2388 | 1.4919 | ±2.9838 | -1.501 | 0.1334 |  |
| Site: UW (vs UAB) | +0.5761 | 1.5402 | ±3.0804 | +0.374 | 0.7084 |  |
| **Age (years)** | **-0.1845** | 0.0529 | ±0.1057 | **-3.489** | **4.84e-04** | *** |
| **BMI (kg/m2)** | **+0.1669** | 0.0723 | ±0.1447 | **+2.308** | **0.0210** | * |
| Hypertension | +0.5420 | 1.4440 | ±2.8880 | +0.375 | 0.7074 |  |
| High cholesterol | -0.2256 | 1.1694 | ±2.3388 | -0.193 | 0.8470 |  |
| Kidney disease | +0.7571 | 1.6618 | ±3.3237 | +0.456 | 0.6487 |  |
| Circulatory disease | -2.1156 | 1.3597 | ±2.7195 | -1.556 | 0.1197 |  |
| Time < 54 (%) | +0.5339 | 0.6939 | ±1.3878 | +0.769 | 0.4417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **203**, R² = **0.2048**, Adj R² = **0.1590**, F-statistic = **4.47** (p = **5.32e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8754** | 4.7065 | ±9.4130 | **+15.696** | **1.60e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4916** | 1.3262 | ±2.6525 | **-2.633** | **0.0085** | ** |
| Education: high school or below (vs college) | -1.0655 | 1.5182 | ±3.0364 | -0.702 | 0.4828 |  |
| Site: UCSD (vs UAB) | -2.3826 | 1.4982 | ±2.9964 | -1.590 | 0.1118 |  |
| Site: UW (vs UAB) | +0.3904 | 1.5358 | ±3.0717 | +0.254 | 0.7993 |  |
| **Age (years)** | **-0.1828** | 0.0536 | ±0.1073 | **-3.409** | **6.52e-04** | *** |
| **BMI (kg/m2)** | **+0.1677** | 0.0735 | ±0.1469 | **+2.282** | **0.0225** | * |
| Hypertension | +0.5975 | 1.4495 | ±2.8989 | +0.412 | 0.6802 |  |
| High cholesterol | -0.2147 | 1.1706 | ±2.3412 | -0.183 | 0.8545 |  |
| Kidney disease | +0.7431 | 1.6616 | ±3.3232 | +0.447 | 0.6547 |  |
| Circulatory disease | -2.0040 | 1.3995 | ±2.7989 | -1.432 | 0.1522 |  |
| Avg. daily time < 54 (%) | -0.1165 | 1.1633 | ±2.3265 | -0.100 | 0.9202 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.01e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8978** | 4.7193 | ±9.4386 | **+15.659** | **2.90e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5601** | 1.3518 | ±2.7035 | **-2.634** | **0.0084** | ** |
| Education: high school or below (vs college) | -1.0263 | 1.5110 | ±3.0221 | -0.679 | 0.4970 |  |
| Site: UCSD (vs UAB) | -2.4043 | 1.5104 | ±3.0208 | -1.592 | 0.1114 |  |
| Site: UW (vs UAB) | +0.3916 | 1.5225 | ±3.0450 | +0.257 | 0.7970 |  |
| **Age (years)** | **-0.1806** | 0.0533 | ±0.1065 | **-3.390** | **6.99e-04** | *** |
| **BMI (kg/m2)** | **+0.1671** | 0.0735 | ±0.1471 | **+2.273** | **0.0230** | * |
| Hypertension | +0.5792 | 1.4456 | ±2.8913 | +0.401 | 0.6887 |  |
| High cholesterol | -0.1928 | 1.1737 | ±2.3474 | -0.164 | 0.8695 |  |
| Kidney disease | +0.7530 | 1.6589 | ±3.3179 | +0.454 | 0.6499 |  |
| Circulatory disease | -2.0143 | 1.3813 | ±2.7626 | -1.458 | 0.1448 |  |
| Time 54-69, pooled (%) | -0.0935 | 0.2338 | ±0.4677 | -0.400 | 0.6894 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **203**, R² = **0.2069**, Adj R² = **0.1612**, F-statistic = **4.53** (p = **4.31e-06**), Residual SE = **7.904** on **191** df, AIC = **1427.1**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8483** | 4.7199 | ±9.4399 | **+15.646** | **3.54e-55** | *** |
| **Education: graduate level (vs college)** | **-3.6178** | 1.3530 | ±2.7060 | **-2.674** | **0.0075** | ** |
| Education: high school or below (vs college) | -0.9977 | 1.5034 | ±3.0068 | -0.664 | 0.5069 |  |
| Site: UCSD (vs UAB) | -2.4330 | 1.5114 | ±3.0229 | -1.610 | 0.1075 |  |
| Site: UW (vs UAB) | +0.3716 | 1.5163 | ±3.0326 | +0.245 | 0.8064 |  |
| **Age (years)** | **-0.1776** | 0.0536 | ±0.1073 | **-3.311** | **9.28e-04** | *** |
| **BMI (kg/m2)** | **+0.1667** | 0.0737 | ±0.1474 | **+2.262** | **0.0237** | * |
| Hypertension | +0.5727 | 1.4487 | ±2.8974 | +0.395 | 0.6926 |  |
| High cholesterol | -0.1855 | 1.1751 | ±2.3502 | -0.158 | 0.8746 |  |
| Kidney disease | +0.7639 | 1.6544 | ±3.3088 | +0.462 | 0.6443 |  |
| Circulatory disease | -2.0099 | 1.3879 | ±2.7759 | -1.448 | 0.1476 |  |
| Avg. daily time 54-69 (%) | -0.1553 | 0.2389 | ±0.4777 | -0.650 | 0.5155 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **203**, R² = **0.2048**, Adj R² = **0.1590**, F-statistic = **4.47** (p = **5.33e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8846** | 4.7163 | ±9.4327 | **+15.666** | **2.60e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5034** | 1.3423 | ±2.6846 | **-2.610** | **0.0091** | ** |
| Education: high school or below (vs college) | -1.0440 | 1.5188 | ±3.0376 | -0.687 | 0.4918 |  |
| Site: UCSD (vs UAB) | -2.3794 | 1.5090 | ±3.0180 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4016 | 1.5294 | ±3.0589 | +0.263 | 0.7929 |  |
| **Age (years)** | **-0.1825** | 0.0533 | ±0.1066 | **-3.425** | **6.14e-04** | *** |
| **BMI (kg/m2)** | **+0.1676** | 0.0733 | ±0.1466 | **+2.286** | **0.0223** | * |
| Hypertension | +0.5900 | 1.4453 | ±2.8905 | +0.408 | 0.6831 |  |
| High cholesterol | -0.2035 | 1.1727 | ±2.3454 | -0.174 | 0.8622 |  |
| Kidney disease | +0.7431 | 1.6615 | ±3.3230 | +0.447 | 0.6547 |  |
| Circulatory disease | -2.0165 | 1.3780 | ±2.7560 | -1.463 | 0.1434 |  |
| Time < 70 (%) | -0.0296 | 0.1988 | ±0.3975 | -0.149 | 0.8817 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **203**, R² = **0.2064**, Adj R² = **0.1607**, F-statistic = **4.52** (p = **4.54e-06**), Residual SE = **7.906** on **191** df, AIC = **1427.2**, BIC = **1466.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8632** | 4.7201 | ±9.4402 | **+15.649** | **3.40e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5942** | 1.3459 | ±2.6919 | **-2.670** | **0.0076** | ** |
| Education: high school or below (vs college) | -1.0310 | 1.5071 | ±3.0141 | -0.684 | 0.4939 |  |
| Site: UCSD (vs UAB) | -2.4347 | 1.5091 | ±3.0181 | -1.613 | 0.1067 |  |
| Site: UW (vs UAB) | +0.3581 | 1.5200 | ±3.0401 | +0.236 | 0.8137 |  |
| **Age (years)** | **-0.1787** | 0.0539 | ±0.1077 | **-3.317** | **9.10e-04** | *** |
| **BMI (kg/m2)** | **+0.1670** | 0.0737 | ±0.1473 | **+2.267** | **0.0234** | * |
| Hypertension | +0.5841 | 1.4498 | ±2.8997 | +0.403 | 0.6870 |  |
| High cholesterol | -0.1972 | 1.1723 | ±2.3446 | -0.168 | 0.8664 |  |
| Kidney disease | +0.7601 | 1.6564 | ±3.3128 | +0.459 | 0.6463 |  |
| Circulatory disease | -1.9944 | 1.3902 | ±2.7804 | -1.435 | 0.1514 |  |
| Avg. daily time < 70 (%) | -0.1107 | 0.2121 | ±0.4241 | -0.522 | 0.6017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1589**, F-statistic = **4.47** (p = **5.36e-06**), Residual SE = **7.915** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.3349** | 8.4695 | ±16.9389 | **+8.659** | **4.77e-18** | *** |
| **Education: graduate level (vs college)** | **-3.4824** | 1.3367 | ±2.6734 | **-2.605** | **0.0092** | ** |
| Education: high school or below (vs college) | -1.0288 | 1.5423 | ±3.0847 | -0.667 | 0.5048 |  |
| Site: UCSD (vs UAB) | -2.3600 | 1.4947 | ±2.9894 | -1.579 | 0.1144 |  |
| Site: UW (vs UAB) | +0.4064 | 1.5320 | ±3.0639 | +0.265 | 0.7908 |  |
| **Age (years)** | **-0.1836** | 0.0530 | ±0.1060 | **-3.463** | **5.35e-04** | *** |
| **BMI (kg/m2)** | **+0.1675** | 0.0734 | ±0.1469 | **+2.280** | **0.0226** | * |
| Hypertension | +0.5935 | 1.4516 | ±2.9032 | +0.409 | 0.6826 |  |
| High cholesterol | -0.2156 | 1.1723 | ±2.3445 | -0.184 | 0.8540 |  |
| Kidney disease | +0.7511 | 1.6699 | ±3.3397 | +0.450 | 0.6529 |  |
| Circulatory disease | -2.0173 | 1.3863 | ±2.7726 | -1.455 | 0.1456 |  |
| Time 54-250, pooled (%) | +0.0057 | 0.0756 | ±0.1512 | +0.075 | 0.9399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.2049**, Adj R² = **0.1591**, F-statistic = **4.47** (p = **5.26e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.3354** | 7.8908 | ±15.7816 | **+9.547** | **1.33e-21** | *** |
| **Education: graduate level (vs college)** | **-3.4451** | 1.3375 | ±2.6751 | **-2.576** | **0.0100** | * |
| Education: high school or below (vs college) | -1.0911 | 1.5204 | ±3.0408 | -0.718 | 0.4730 |  |
| Site: UCSD (vs UAB) | -2.3572 | 1.4938 | ±2.9877 | -1.578 | 0.1146 |  |
| Site: UW (vs UAB) | +0.4475 | 1.5309 | ±3.0618 | +0.292 | 0.7701 |  |
| **Age (years)** | **-0.1834** | 0.0528 | ±0.1057 | **-3.471** | **5.19e-04** | *** |
| **BMI (kg/m2)** | **+0.1686** | 0.0734 | ±0.1468 | **+2.297** | **0.0216** | * |
| Hypertension | +0.5843 | 1.4480 | ±2.8960 | +0.404 | 0.6866 |  |
| High cholesterol | -0.1955 | 1.1700 | ±2.3399 | -0.167 | 0.8673 |  |
| Kidney disease | +0.7065 | 1.6587 | ±3.3174 | +0.426 | 0.6701 |  |
| Circulatory disease | -2.0477 | 1.3875 | ±2.7750 | -1.476 | 0.1400 |  |
| Avg. daily time 54-250 (%) | -0.0157 | 0.0692 | ±0.1384 | -0.226 | 0.8210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.2071**, Adj R² = **0.1615**, F-statistic = **4.54** (p = **4.22e-06**), Residual SE = **7.903** on **191** df, AIC = **1427.0**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6882** | 4.7534 | ±9.5068 | **+15.502** | **3.35e-54** | *** |
| **Education: graduate level (vs college)** | **-3.3637** | 1.3610 | ±2.7221 | **-2.471** | **0.0135** | * |
| Education: high school or below (vs college) | -1.1002 | 1.4934 | ±2.9869 | -0.737 | 0.4613 |  |
| Site: UCSD (vs UAB) | -2.3710 | 1.4855 | ±2.9711 | -1.596 | 0.1105 |  |
| Site: UW (vs UAB) | +0.4106 | 1.5217 | ±3.0433 | +0.270 | 0.7873 |  |
| **Age (years)** | **-0.1875** | 0.0525 | ±0.1051 | **-3.570** | **3.58e-04** | *** |
| **BMI (kg/m2)** | **+0.1689** | 0.0729 | ±0.1458 | **+2.316** | **0.0206** | * |
| Hypertension | +0.6547 | 1.4391 | ±2.8782 | +0.455 | 0.6492 |  |
| High cholesterol | -0.2968 | 1.1653 | ±2.3306 | -0.255 | 0.7990 |  |
| Kidney disease | +0.5511 | 1.6522 | ±3.3044 | +0.334 | 0.7387 |  |
| Circulatory disease | -2.0453 | 1.3758 | ±2.7516 | -1.487 | 0.1371 |  |
| Time 181-250, pooled (%) | +0.0356 | 0.0507 | ±0.1013 | +0.702 | 0.4826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **203**, R² = **0.2061**, Adj R² = **0.1604**, F-statistic = **4.51** (p = **4.65e-06**), Residual SE = **7.907** on **191** df, AIC = **1427.2**, BIC = **1467.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6779** | 4.7669 | ±9.5339 | **+15.456** | **6.87e-54** | *** |
| **Education: graduate level (vs college)** | **-3.3916** | 1.3607 | ±2.7214 | **-2.493** | **0.0127** | * |
| Education: high school or below (vs college) | -1.0930 | 1.4995 | ±2.9991 | -0.729 | 0.4661 |  |
| Site: UCSD (vs UAB) | -2.3544 | 1.4890 | ±2.9780 | -1.581 | 0.1138 |  |
| Site: UW (vs UAB) | +0.4274 | 1.5259 | ±3.0518 | +0.280 | 0.7794 |  |
| **Age (years)** | **-0.1859** | 0.0526 | ±0.1051 | **-3.537** | **4.04e-04** | *** |
| **BMI (kg/m2)** | **+0.1689** | 0.0731 | ±0.1463 | **+2.309** | **0.0210** | * |
| Hypertension | +0.6447 | 1.4380 | ±2.8760 | +0.448 | 0.6539 |  |
| High cholesterol | -0.2743 | 1.1655 | ±2.3309 | -0.235 | 0.8139 |  |
| Kidney disease | +0.5989 | 1.6592 | ±3.3183 | +0.361 | 0.7181 |  |
| Circulatory disease | -2.0410 | 1.3770 | ±2.7541 | -1.482 | 0.1383 |  |
| Avg. daily time 181-250 (%) | +0.0267 | 0.0499 | ±0.0999 | +0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.00e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7164** | 4.7551 | ±9.5103 | **+15.502** | **3.34e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4131** | 1.3550 | ±2.7099 | **-2.519** | **0.0118** | * |
| Education: high school or below (vs college) | -1.1018 | 1.5070 | ±3.0140 | -0.731 | 0.4647 |  |
| Site: UCSD (vs UAB) | -2.3615 | 1.4921 | ±2.9841 | -1.583 | 0.1135 |  |
| Site: UW (vs UAB) | +0.4400 | 1.5277 | ±3.0555 | +0.288 | 0.7734 |  |
| **Age (years)** | **-0.1846** | 0.0527 | ±0.1054 | **-3.505** | **4.57e-04** | *** |
| **BMI (kg/m2)** | **+0.1687** | 0.0733 | ±0.1465 | **+2.303** | **0.0213** | * |
| Hypertension | +0.6092 | 1.4435 | ±2.8869 | +0.422 | 0.6730 |  |
| High cholesterol | -0.2272 | 1.1682 | ±2.3364 | -0.194 | 0.8458 |  |
| Kidney disease | +0.6480 | 1.6610 | ±3.3221 | +0.390 | 0.6964 |  |
| Circulatory disease | -2.0465 | 1.3788 | ±2.7577 | -1.484 | 0.1378 |  |
| Time > 180 (%) | +0.0126 | 0.0333 | ±0.0667 | +0.378 | 0.7052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **203**, R² = **0.2058**, Adj R² = **0.1600**, F-statistic = **4.50** (p = **4.82e-06**), Residual SE = **7.909** on **191** df, AIC = **1427.3**, BIC = **1467.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6620** | 4.7659 | ±9.5318 | **+15.456** | **6.86e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4004** | 1.3566 | ±2.7132 | **-2.507** | **0.0122** | * |
| Education: high school or below (vs college) | -1.1220 | 1.5006 | ±3.0012 | -0.748 | 0.4546 |  |
| Site: UCSD (vs UAB) | -2.3583 | 1.4906 | ±2.9812 | -1.582 | 0.1136 |  |
| Site: UW (vs UAB) | +0.4485 | 1.5289 | ±3.0578 | +0.293 | 0.7692 |  |
| **Age (years)** | **-0.1847** | 0.0526 | ±0.1052 | **-3.510** | **4.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1692** | 0.0733 | ±0.1466 | **+2.308** | **0.0210** | * |
| Hypertension | +0.6166 | 1.4428 | ±2.8856 | +0.427 | 0.6691 |  |
| High cholesterol | -0.2340 | 1.1657 | ±2.3314 | -0.201 | 0.8409 |  |
| Kidney disease | +0.6244 | 1.6558 | ±3.3117 | +0.377 | 0.7061 |  |
| Circulatory disease | -2.0543 | 1.3799 | ±2.7598 | -1.489 | 0.1366 |  |
| Avg. daily time > 180 (%) | +0.0156 | 0.0322 | ±0.0644 | +0.485 | 0.6277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **203**, R² = **0.2052**, Adj R² = **0.1594**, F-statistic = **4.48** (p = **5.10e-06**), Residual SE = **7.912** on **191** df, AIC = **1427.5**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7557** | 4.7435 | ±9.4870 | **+15.549** | **1.62e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4332** | 1.3463 | ±2.6926 | **-2.550** | **0.0108** | * |
| Education: high school or below (vs college) | -1.0706 | 1.5042 | ±3.0084 | -0.712 | 0.4766 |  |
| Site: UCSD (vs UAB) | -2.3640 | 1.4922 | ±2.9844 | -1.584 | 0.1131 |  |
| Site: UW (vs UAB) | +0.4386 | 1.5251 | ±3.0502 | +0.288 | 0.7737 |  |
| **Age (years)** | **-0.1833** | 0.0528 | ±0.1057 | **-3.469** | **5.22e-04** | *** |
| **BMI (kg/m2)** | **+0.1678** | 0.0729 | ±0.1458 | **+2.302** | **0.0213** | * |
| Hypertension | +0.5783 | 1.4547 | ±2.9093 | +0.398 | 0.6910 |  |
| High cholesterol | -0.2298 | 1.1672 | ±2.3345 | -0.197 | 0.8439 |  |
| Kidney disease | +0.6996 | 1.6511 | ±3.3022 | +0.424 | 0.6718 |  |
| Circulatory disease | -2.0585 | 1.3815 | ±2.7629 | -1.490 | 0.1362 |  |
| Nocturnal time > 180 (%) | +0.0107 | 0.0302 | ±0.0603 | +0.355 | 0.7224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1589**, F-statistic = **4.47** (p = **5.36e-06**), Residual SE = **7.915** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8387** | 4.7602 | ±9.5205 | **+15.512** | **2.90e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4559** | 1.3642 | ±2.7284 | **-2.533** | **0.0113** | * |
| Education: high school or below (vs college) | -1.0546 | 1.5169 | ±3.0339 | -0.695 | 0.4869 |  |
| Site: UCSD (vs UAB) | -2.3616 | 1.4977 | ±2.9954 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4067 | 1.5301 | ±3.0602 | +0.266 | 0.7904 |  |
| **Age (years)** | **-0.1844** | 0.0533 | ±0.1067 | **-3.457** | **5.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1685** | 0.0754 | ±0.1507 | **+2.236** | **0.0253** | * |
| Hypertension | +0.5920 | 1.4446 | ±2.8891 | +0.410 | 0.6819 |  |
| High cholesterol | -0.2135 | 1.1686 | ±2.3372 | -0.183 | 0.8550 |  |
| Kidney disease | +0.7135 | 1.6918 | ±3.3837 | +0.422 | 0.6732 |  |
| Circulatory disease | -2.0242 | 1.3713 | ±2.7425 | -1.476 | 0.1399 |  |
| Any reading > 250 during wear (0/1) | +0.1106 | 1.2631 | ±2.5262 | +0.088 | 0.9302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.2048**, Adj R² = **0.1590**, F-statistic = **4.47** (p = **5.33e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.9274** | 4.7420 | ±9.4840 | **+15.590** | **8.52e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4877** | 1.3356 | ±2.6711 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | -1.0172 | 1.5431 | ±3.0862 | -0.659 | 0.5098 |  |
| Site: UCSD (vs UAB) | -2.3590 | 1.4960 | ±2.9920 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4013 | 1.5299 | ±3.0598 | +0.262 | 0.7931 |  |
| **Age (years)** | **-0.1837** | 0.0531 | ±0.1061 | **-3.462** | **5.36e-04** | *** |
| **BMI (kg/m2)** | **+0.1673** | 0.0734 | ±0.1468 | **+2.279** | **0.0227** | * |
| Hypertension | +0.5943 | 1.4514 | ±2.9029 | +0.409 | 0.6822 |  |
| High cholesterol | -0.2196 | 1.1732 | ±2.3465 | -0.187 | 0.8515 |  |
| Kidney disease | +0.7583 | 1.6707 | ±3.3414 | +0.454 | 0.6499 |  |
| Circulatory disease | -2.0142 | 1.3829 | ±2.7658 | -1.457 | 0.1452 |  |
| Time > 250 (%) | -0.0093 | 0.0733 | ±0.1467 | -0.126 | 0.8995 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.2049**, Adj R² = **0.1592**, F-statistic = **4.48** (p = **5.24e-06**), Residual SE = **7.913** on **191** df, AIC = **1427.6**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7619** | 4.7332 | ±9.4664 | **+15.584** | **9.36e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4453** | 1.3363 | ±2.6727 | **-2.578** | **0.0099** | ** |
| Education: high school or below (vs college) | -1.0987 | 1.5172 | ±3.0345 | -0.724 | 0.4690 |  |
| Site: UCSD (vs UAB) | -2.3607 | 1.4948 | ±2.9896 | -1.579 | 0.1143 |  |
| Site: UW (vs UAB) | +0.4461 | 1.5289 | ±3.0579 | +0.292 | 0.7705 |  |
| **Age (years)** | **-0.1832** | 0.0528 | ±0.1057 | **-3.468** | **5.25e-04** | *** |
| **BMI (kg/m2)** | **+0.1686** | 0.0733 | ±0.1466 | **+2.301** | **0.0214** | * |
| Hypertension | +0.5846 | 1.4476 | ±2.8953 | +0.404 | 0.6863 |  |
| High cholesterol | -0.1949 | 1.1704 | ±2.3409 | -0.166 | 0.8678 |  |
| Kidney disease | +0.7037 | 1.6565 | ±3.3130 | +0.425 | 0.6710 |  |
| Circulatory disease | -2.0468 | 1.3855 | ±2.7710 | -1.477 | 0.1396 |  |
| Avg. daily time > 250 (%) | +0.0172 | 0.0670 | ±0.1339 | +0.257 | 0.7975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 205; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **205**, R² = **0.0659**, Adj R² = **0.0177**, F-statistic = **1.37** (p = **0.1975**), Residual SE = **68.888** on **194** df, AIC = **2327.8**, BIC = **2364.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8528** | 40.7069 | ±81.4138 | **+9.675** | **3.84e-22** | *** |
| Education: graduate level (vs college) | +10.2617 | 12.7112 | ±25.4224 | +0.807 | 0.4195 |  |
| Education: high school or below (vs college) | -21.2336 | 13.7302 | ±27.4604 | -1.546 | 0.1220 |  |
| Site: UCSD (vs UAB) | -10.2666 | 12.8259 | ±25.6517 | -0.800 | 0.4234 |  |
| Site: UW (vs UAB) | -12.6536 | 12.7582 | ±25.5163 | -0.992 | 0.3213 |  |
| Age (years) | -0.0595 | 0.5377 | ±1.0754 | -0.111 | 0.9119 |  |
| BMI (kg/m2) | -0.3694 | 0.6533 | ±1.3066 | -0.565 | 0.5718 |  |
| **Hypertension** | **-27.1461** | 12.1421 | ±24.2842 | **-2.236** | **0.0254** | * |
| High cholesterol | +7.8438 | 10.2966 | ±20.5931 | +0.762 | 0.4462 |  |
| Kidney disease | +3.4725 | 17.3785 | ±34.7571 | +0.200 | 0.8416 |  |
| Circulatory disease | +1.7522 | 11.6420 | ±23.2841 | +0.151 | 0.8804 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **205**, R² = **0.1089**, Adj R² = **0.0581**, F-statistic = **2.14** (p = **0.0190**), Residual SE = **67.456** on **193** df, AIC = **2320.1**, BIC = **2360.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+461.9602** | 42.7001 | ±85.4002 | **+10.819** | **2.81e-27** | *** |
| Education: graduate level (vs college) | +5.8523 | 12.6761 | ±25.3522 | +0.462 | 0.6443 |  |
| Education: high school or below (vs college) | -16.7549 | 12.4925 | ±24.9850 | -1.341 | 0.1799 |  |
| Site: UCSD (vs UAB) | -11.2141 | 12.4538 | ±24.9075 | -0.900 | 0.3679 |  |
| Site: UW (vs UAB) | -13.9739 | 12.6603 | ±25.3205 | -1.104 | 0.2697 |  |
| Age (years) | +0.1696 | 0.5345 | ±1.0689 | +0.317 | 0.7510 |  |
| BMI (kg/m2) | -0.2797 | 0.6239 | ±1.2479 | -0.448 | 0.6539 |  |
| **Hypertension** | **-26.5696** | 11.7743 | ±23.5486 | **-2.257** | **0.0240** | * |
| High cholesterol | +6.6134 | 10.0139 | ±20.0278 | +0.660 | 0.5090 |  |
| Kidney disease | +3.6253 | 16.8248 | ±33.6496 | +0.215 | 0.8294 |  |
| Circulatory disease | +0.6999 | 11.2778 | ±22.5556 | +0.062 | 0.9505 |  |
| **HbA1c (%)** | **-12.9355** | 3.7701 | ±7.5402 | **-3.431** | **6.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **205**, R² = **0.0865**, Adj R² = **0.0344**, F-statistic = **1.66** (p = **0.0849**), Residual SE = **68.301** on **193** df, AIC = **2325.2**, BIC = **2365.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+434.6785** | 44.5592 | ±89.1183 | **+9.755** | **1.75e-22** | *** |
| Education: graduate level (vs college) | +8.7778 | 12.7798 | ±25.5597 | +0.687 | 0.4922 |  |
| Education: high school or below (vs college) | -18.6017 | 13.1882 | ±26.3765 | -1.410 | 0.1584 |  |
| Site: UCSD (vs UAB) | -10.0326 | 12.4157 | ±24.8313 | -0.808 | 0.4191 |  |
| Site: UW (vs UAB) | -13.2241 | 13.0593 | ±26.1187 | -1.013 | 0.3112 |  |
| Age (years) | -0.0347 | 0.5359 | ±1.0718 | -0.065 | 0.9484 |  |
| BMI (kg/m2) | -0.3796 | 0.6487 | ±1.2974 | -0.585 | 0.5584 |  |
| **Hypertension** | **-26.8413** | 11.9950 | ±23.9900 | **-2.238** | **0.0252** | * |
| High cholesterol | +7.6941 | 10.1512 | ±20.3024 | +0.758 | 0.4485 |  |
| Kidney disease | +6.1194 | 17.6388 | ±35.2776 | +0.347 | 0.7286 |  |
| Circulatory disease | +2.1811 | 11.4786 | ±22.9572 | +0.190 | 0.8493 |  |
| **Mean glucose (mg/dL)** | **-0.3115** | 0.1399 | ±0.2799 | **-2.226** | **0.0260** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **205**, R² = **0.0865**, Adj R² = **0.0344**, F-statistic = **1.66** (p = **0.0849**), Residual SE = **68.301** on **193** df, AIC = **2325.2**, BIC = **2365.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+477.7828** | 55.3233 | ±110.6467 | **+8.636** | **5.81e-18** | *** |
| Education: graduate level (vs college) | +8.7778 | 12.7798 | ±25.5597 | +0.687 | 0.4922 |  |
| Education: high school or below (vs college) | -18.6017 | 13.1882 | ±26.3765 | -1.410 | 0.1584 |  |
| Site: UCSD (vs UAB) | -10.0326 | 12.4157 | ±24.8313 | -0.808 | 0.4191 |  |
| Site: UW (vs UAB) | -13.2241 | 13.0593 | ±26.1187 | -1.013 | 0.3112 |  |
| Age (years) | -0.0347 | 0.5359 | ±1.0718 | -0.065 | 0.9484 |  |
| BMI (kg/m2) | -0.3796 | 0.6487 | ±1.2974 | -0.585 | 0.5584 |  |
| **Hypertension** | **-26.8413** | 11.9950 | ±23.9900 | **-2.238** | **0.0252** | * |
| High cholesterol | +7.6941 | 10.1512 | ±20.3024 | +0.758 | 0.4485 |  |
| Kidney disease | +6.1194 | 17.6388 | ±35.2776 | +0.347 | 0.7286 |  |
| Circulatory disease | +2.1811 | 11.4786 | ±22.9572 | +0.190 | 0.8493 |  |
| **GMI (%)** | **-13.0224** | 5.8503 | ±11.7006 | **-2.226** | **0.0260** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **205**, R² = **0.0800**, Adj R² = **0.0276**, F-statistic = **1.53** (p = **0.1246**), Residual SE = **68.542** on **193** df, AIC = **2326.6**, BIC = **2366.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+427.2895** | 44.7493 | ±89.4985 | **+9.549** | **1.32e-21** | *** |
| Education: graduate level (vs college) | +9.9144 | 12.8383 | ±25.6767 | +0.772 | 0.4400 |  |
| Education: high school or below (vs college) | -19.2807 | 13.2158 | ±26.4316 | -1.459 | 0.1446 |  |
| Site: UCSD (vs UAB) | -10.1747 | 12.5167 | ±25.0334 | -0.813 | 0.4163 |  |
| Site: UW (vs UAB) | -12.7833 | 13.1054 | ±26.2109 | -0.975 | 0.3294 |  |
| Age (years) | -0.0897 | 0.5390 | ±1.0780 | -0.166 | 0.8678 |  |
| BMI (kg/m2) | -0.3640 | 0.6480 | ±1.2960 | -0.562 | 0.5742 |  |
| **Hypertension** | **-26.3089** | 12.1611 | ±24.3222 | **-2.163** | **0.0305** | * |
| High cholesterol | +8.2622 | 10.1466 | ±20.2932 | +0.814 | 0.4155 |  |
| Kidney disease | +4.0661 | 17.5202 | ±35.0404 | +0.232 | 0.8165 |  |
| Circulatory disease | +2.4197 | 11.4745 | ±22.9490 | +0.211 | 0.8330 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.2522 | 0.1446 | ±0.2892 | -1.744 | 0.0811 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0803**, Adj R² = **0.0279**, F-statistic = **1.53** (p = **0.1227**), Residual SE = **68.532** on **193** df, AIC = **2326.6**, BIC = **2366.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.1054** | 40.7028 | ±81.4056 | **+9.977** | **1.92e-23** | *** |
| Education: graduate level (vs college) | +7.4579 | 12.8772 | ±25.7543 | +0.579 | 0.5625 |  |
| Education: high school or below (vs college) | -17.0254 | 13.5636 | ±27.1272 | -1.255 | 0.2094 |  |
| Site: UCSD (vs UAB) | -10.2274 | 12.4993 | ±24.9986 | -0.818 | 0.4132 |  |
| Site: UW (vs UAB) | -13.7174 | 12.9357 | ±25.8715 | -1.060 | 0.2890 |  |
| Age (years) | +0.0777 | 0.5427 | ±1.0854 | +0.143 | 0.8862 |  |
| BMI (kg/m2) | -0.4128 | 0.6498 | ±1.2996 | -0.635 | 0.5253 |  |
| **Hypertension** | **-27.1377** | 11.8882 | ±23.7764 | **-2.283** | **0.0224** | * |
| High cholesterol | +7.4864 | 10.2114 | ±20.4228 | +0.733 | 0.4635 |  |
| Kidney disease | +8.5738 | 18.2937 | ±36.5873 | +0.469 | 0.6393 |  |
| Circulatory disease | +0.9891 | 11.6212 | ±23.2424 | +0.085 | 0.9322 |  |
| Glucose SD, pooled (mg/dL) | -0.5567 | 0.3092 | ±0.6185 | -1.800 | 0.0718 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0765**, Adj R² = **0.0239**, F-statistic = **1.45** (p = **0.1521**), Residual SE = **68.673** on **193** df, AIC = **2327.4**, BIC = **2367.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.6342** | 41.1405 | ±82.2810 | **+9.860** | **6.22e-23** | *** |
| Education: graduate level (vs college) | +7.7983 | 12.7808 | ±25.5616 | +0.610 | 0.5418 |  |
| Education: high school or below (vs college) | -17.0176 | 13.7098 | ±27.4197 | -1.241 | 0.2145 |  |
| Site: UCSD (vs UAB) | -10.2537 | 12.5788 | ±25.1575 | -0.815 | 0.4150 |  |
| Site: UW (vs UAB) | -13.3797 | 12.9495 | ±25.8991 | -1.033 | 0.3015 |  |
| Age (years) | +0.0560 | 0.5416 | ±1.0831 | +0.103 | 0.9177 |  |
| BMI (kg/m2) | -0.4246 | 0.6551 | ±1.3102 | -0.648 | 0.5169 |  |
| **Hypertension** | **-27.3728** | 11.9196 | ±23.8393 | **-2.296** | **0.0217** | * |
| High cholesterol | +7.7704 | 10.2277 | ±20.4555 | +0.760 | 0.4474 |  |
| Kidney disease | +7.8821 | 18.1894 | ±36.3788 | +0.433 | 0.6648 |  |
| Circulatory disease | +0.9204 | 11.7071 | ±23.4142 | +0.079 | 0.9373 |  |
| Avg. daily SD (mg/dL) | -0.5645 | 0.3467 | ±0.6934 | -1.628 | 0.1035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **205**, R² = **0.0670**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2499**), Residual SE = **69.024** on **193** df, AIC = **2329.5**, BIC = **2369.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.4986** | 41.5301 | ±83.0603 | **+9.619** | **6.62e-22** | *** |
| Education: graduate level (vs college) | +9.2557 | 12.9988 | ±25.9975 | +0.712 | 0.4764 |  |
| Education: high school or below (vs college) | -19.8238 | 13.8968 | ±27.7935 | -1.427 | 0.1537 |  |
| Site: UCSD (vs UAB) | -10.2293 | 12.7987 | ±25.5974 | -0.799 | 0.4241 |  |
| Site: UW (vs UAB) | -12.9964 | 12.8026 | ±25.6051 | -1.015 | 0.3100 |  |
| Age (years) | +0.0070 | 0.5621 | ±1.1243 | +0.012 | 0.9901 |  |
| BMI (kg/m2) | -0.3851 | 0.6541 | ±1.3083 | -0.589 | 0.5561 |  |
| **Hypertension** | **-27.2497** | 12.0934 | ±24.1867 | **-2.253** | **0.0242** | * |
| High cholesterol | +7.8104 | 10.3234 | ±20.6468 | +0.757 | 0.4493 |  |
| Kidney disease | +5.2257 | 18.8483 | ±37.6965 | +0.277 | 0.7816 |  |
| Circulatory disease | +1.4120 | 11.7855 | ±23.5711 | +0.120 | 0.9046 |  |
| CV (%) | -0.3731 | 0.7619 | ±1.5238 | -0.490 | 0.6243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **205**, R² = **0.0664**, Adj R² = **0.0132**, F-statistic = **1.25** (p = **0.2575**), Residual SE = **69.046** on **193** df, AIC = **2329.7**, BIC = **2369.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.2335** | 48.7990 | ±97.5980 | **+7.894** | **2.92e-15** | *** |
| Education: graduate level (vs college) | +9.5965 | 12.9575 | ±25.9149 | +0.741 | 0.4589 |  |
| Education: high school or below (vs college) | -20.2467 | 13.9886 | ±27.9771 | -1.447 | 0.1478 |  |
| Site: UCSD (vs UAB) | -10.1136 | 12.8331 | ±25.6661 | -0.788 | 0.4306 |  |
| Site: UW (vs UAB) | -12.7673 | 12.8077 | ±25.6154 | -0.997 | 0.3188 |  |
| Age (years) | -0.0109 | 0.5580 | ±1.1161 | -0.019 | 0.9845 |  |
| BMI (kg/m2) | -0.3736 | 0.6546 | ±1.3092 | -0.571 | 0.5681 |  |
| **Hypertension** | **-27.2902** | 12.1159 | ±24.2318 | **-2.252** | **0.0243** | * |
| High cholesterol | +7.8416 | 10.3243 | ±20.6487 | +0.760 | 0.4475 |  |
| Kidney disease | +4.2883 | 18.2919 | ±36.5838 | +0.234 | 0.8146 |  |
| Circulatory disease | +1.7594 | 11.6890 | ±23.3781 | +0.151 | 0.8804 |  |
| Mean / SD ratio | +1.3006 | 3.9983 | ±7.9965 | +0.325 | 0.7450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0661**, Adj R² = **0.0128**, F-statistic = **1.24** (p = **0.2622**), Residual SE = **69.060** on **193** df, AIC = **2329.7**, BIC = **2369.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.0173** | 46.2554 | ±92.5108 | **+8.410** | **4.09e-17** | *** |
| Education: graduate level (vs college) | +9.8643 | 12.8744 | ±25.7487 | +0.766 | 0.4436 |  |
| Education: high school or below (vs college) | -20.6591 | 14.0068 | ±28.0137 | -1.475 | 0.1402 |  |
| Site: UCSD (vs UAB) | -10.1318 | 12.9143 | ±25.8286 | -0.785 | 0.4327 |  |
| Site: UW (vs UAB) | -12.6638 | 12.8103 | ±25.6206 | -0.989 | 0.3229 |  |
| Age (years) | -0.0315 | 0.5464 | ±1.0928 | -0.058 | 0.9541 |  |
| BMI (kg/m2) | -0.3738 | 0.6569 | ±1.3137 | -0.569 | 0.5693 |  |
| **Hypertension** | **-27.2832** | 12.1142 | ±24.2284 | **-2.252** | **0.0243** | * |
| High cholesterol | +7.9122 | 10.3087 | ±20.6174 | +0.768 | 0.4428 |  |
| Kidney disease | +3.7852 | 17.8639 | ±35.7277 | +0.212 | 0.8322 |  |
| Circulatory disease | +1.7316 | 11.7018 | ±23.4037 | +0.148 | 0.8824 |  |
| Avg. daily mean/SD | +0.6199 | 3.0975 | ±6.1949 | +0.200 | 0.8414 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **205**, R² = **0.1046**, Adj R² = **0.0536**, F-statistic = **2.05** (p = **0.0259**), Residual SE = **67.620** on **193** df, AIC = **2321.1**, BIC = **2361.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+439.0283** | 43.5885 | ±87.1770 | **+10.072** | **7.34e-24** | *** |
| Education: graduate level (vs college) | +6.9205 | 12.5316 | ±25.0632 | +0.552 | 0.5808 |  |
| Education: high school or below (vs college) | -13.9455 | 13.5960 | ±27.1920 | -1.026 | 0.3050 |  |
| Site: UCSD (vs UAB) | -8.4020 | 12.5196 | ±25.0391 | -0.671 | 0.5021 |  |
| Site: UW (vs UAB) | -15.9144 | 12.6269 | ±25.2539 | -1.260 | 0.2075 |  |
| Age (years) | +0.0497 | 0.5339 | ±1.0677 | +0.093 | 0.9259 |  |
| BMI (kg/m2) | -0.2072 | 0.6514 | ±1.3028 | -0.318 | 0.7504 |  |
| **Hypertension** | **-28.7958** | 11.6899 | ±23.3799 | **-2.463** | **0.0138** | * |
| High cholesterol | +9.0167 | 10.1056 | ±20.2112 | +0.892 | 0.3723 |  |
| Kidney disease | +4.3983 | 17.2424 | ±34.4849 | +0.255 | 0.7987 |  |
| Circulatory disease | +1.6602 | 11.6183 | ±23.2366 | +0.143 | 0.8864 |  |
| **MAG (mg/dL/h)** | **-1.2652** | 0.4792 | ±0.9585 | **-2.640** | **0.0083** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **205**, R² = **0.0787**, Adj R² = **0.0262**, F-statistic = **1.50** (p = **0.1341**), Residual SE = **68.589** on **193** df, AIC = **2326.9**, BIC = **2366.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.7207** | 42.0786 | ±84.1572 | **+9.808** | **1.04e-22** | *** |
| Education: graduate level (vs college) | +7.4674 | 12.8377 | ±25.6755 | +0.582 | 0.5608 |  |
| Education: high school or below (vs college) | -16.0895 | 13.8284 | ±27.6569 | -1.164 | 0.2446 |  |
| Site: UCSD (vs UAB) | -10.0492 | 12.5425 | ±25.0851 | -0.801 | 0.4230 |  |
| Site: UW (vs UAB) | -13.1998 | 12.9477 | ±25.8955 | -1.019 | 0.3080 |  |
| Age (years) | +0.0609 | 0.5426 | ±1.0852 | +0.112 | 0.9107 |  |
| BMI (kg/m2) | -0.4391 | 0.6594 | ±1.3188 | -0.666 | 0.5055 |  |
| **Hypertension** | **-27.8680** | 11.8729 | ±23.7457 | **-2.347** | **0.0189** | * |
| High cholesterol | +8.1866 | 10.1994 | ±20.3988 | +0.803 | 0.4222 |  |
| Kidney disease | +8.3452 | 18.2464 | ±36.4928 | +0.457 | 0.6474 |  |
| Circulatory disease | +1.4946 | 11.7150 | ±23.4299 | +0.128 | 0.8985 |  |
| Avg. daily range (mg/dL) | -0.1768 | 0.1030 | ±0.2060 | -1.716 | 0.0861 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **205**, R² = **0.0847**, Adj R² = **0.0325**, F-statistic = **1.62** (p = **0.0946**), Residual SE = **68.367** on **193** df, AIC = **2325.6**, BIC = **2365.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.3204** | 39.8019 | ±79.6038 | **+10.083** | **6.57e-24** | *** |
| Education: graduate level (vs college) | +7.0555 | 13.1066 | ±26.2131 | +0.538 | 0.5904 |  |
| Education: high school or below (vs college) | -20.0945 | 13.2515 | ±26.5030 | -1.516 | 0.1294 |  |
| Site: UCSD (vs UAB) | -9.9577 | 12.4468 | ±24.8936 | -0.800 | 0.4237 |  |
| Site: UW (vs UAB) | -13.9970 | 12.8768 | ±25.7535 | -1.087 | 0.2770 |  |
| Age (years) | +0.0334 | 0.5424 | ±1.0847 | +0.062 | 0.9508 |  |
| BMI (kg/m2) | -0.4023 | 0.6415 | ±1.2830 | -0.627 | 0.5306 |  |
| **Hypertension** | **-25.2742** | 12.0396 | ±24.0791 | **-2.099** | **0.0358** | * |
| High cholesterol | +7.0653 | 10.2369 | ±20.4737 | +0.690 | 0.4901 |  |
| Kidney disease | +7.4136 | 18.0438 | ±36.0875 | +0.411 | 0.6812 |  |
| Circulatory disease | +2.6125 | 11.3704 | ±22.7407 | +0.230 | 0.8183 |  |
| SD of daily means (mg/dL) | -1.0069 | 0.5231 | ±1.0461 | -1.925 | 0.0542 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **205**, R² = **0.0920**, Adj R² = **0.0403**, F-statistic = **1.78** (p = **0.0599**), Residual SE = **68.092** on **193** df, AIC = **2324.0**, BIC = **2363.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+338.1655** | 47.3798 | ±94.7596 | **+7.137** | **9.52e-13** | *** |
| Education: graduate level (vs college) | +6.3525 | 12.8598 | ±25.7196 | +0.494 | 0.6213 |  |
| Education: high school or below (vs college) | -18.2529 | 13.1255 | ±26.2511 | -1.391 | 0.1643 |  |
| Site: UCSD (vs UAB) | -10.7537 | 12.2875 | ±24.5751 | -0.875 | 0.3815 |  |
| Site: UW (vs UAB) | -13.9103 | 12.9611 | ±25.9221 | -1.073 | 0.2832 |  |
| Age (years) | +0.0288 | 0.5334 | ±1.0669 | +0.054 | 0.9570 |  |
| BMI (kg/m2) | -0.4231 | 0.6525 | ±1.3050 | -0.648 | 0.5168 |  |
| **Hypertension** | **-27.3557** | 11.8674 | ±23.7348 | **-2.305** | **0.0212** | * |
| High cholesterol | +8.6894 | 10.0794 | ±20.1587 | +0.862 | 0.3886 |  |
| Kidney disease | +8.1416 | 17.7240 | ±35.4481 | +0.459 | 0.6460 |  |
| Circulatory disease | +2.7740 | 11.4869 | ±22.9737 | +0.241 | 0.8092 |  |
| **Time in range 70-180, pooled (%)** | **+0.6249** | 0.2602 | ±0.5205 | **+2.401** | **0.0163** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **205**, R² = **0.0925**, Adj R² = **0.0407**, F-statistic = **1.79** (p = **0.0584**), Residual SE = **68.077** on **193** df, AIC = **2323.9**, BIC = **2363.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+337.9719** | 47.6355 | ±95.2710 | **+7.095** | **1.29e-12** | *** |
| Education: graduate level (vs college) | +6.3132 | 12.9134 | ±25.8267 | +0.489 | 0.6249 |  |
| Education: high school or below (vs college) | -17.8891 | 13.1238 | ±26.2475 | -1.363 | 0.1728 |  |
| Site: UCSD (vs UAB) | -10.9388 | 12.2940 | ±24.5880 | -0.890 | 0.3736 |  |
| Site: UW (vs UAB) | -14.0260 | 12.9764 | ±25.9527 | -1.081 | 0.2797 |  |
| Age (years) | +0.0288 | 0.5336 | ±1.0672 | +0.054 | 0.9569 |  |
| BMI (kg/m2) | -0.4377 | 0.6547 | ±1.3094 | -0.669 | 0.5037 |  |
| **Hypertension** | **-27.4672** | 11.8932 | ±23.7864 | **-2.309** | **0.0209** | * |
| High cholesterol | +8.7482 | 10.0664 | ±20.1329 | +0.869 | 0.3848 |  |
| Kidney disease | +8.3059 | 17.7765 | ±35.5530 | +0.467 | 0.6403 |  |
| Circulatory disease | +2.8849 | 11.4983 | ±22.9966 | +0.251 | 0.8019 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.6302** | 0.2667 | ±0.5334 | **+2.363** | **0.0181** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **205**, R² = **0.0742**, Adj R² = **0.0215**, F-statistic = **1.41** (p = **0.1723**), Residual SE = **68.757** on **193** df, AIC = **2327.9**, BIC = **2367.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.5639** | 40.6494 | ±81.2989 | **+9.608** | **7.39e-22** | *** |
| Education: graduate level (vs college) | +11.2051 | 12.8272 | ±25.6544 | +0.874 | 0.3824 |  |
| Education: high school or below (vs college) | -19.8533 | 13.7641 | ±27.5283 | -1.442 | 0.1492 |  |
| Site: UCSD (vs UAB) | -8.3356 | 12.9055 | ±25.8111 | -0.646 | 0.5184 |  |
| Site: UW (vs UAB) | -10.0850 | 13.0527 | ±26.1054 | -0.773 | 0.4397 |  |
| Age (years) | -0.0702 | 0.5420 | ±1.0841 | -0.130 | 0.8969 |  |
| BMI (kg/m2) | -0.3760 | 0.6470 | ±1.2940 | -0.581 | 0.5611 |  |
| **Hypertension** | **-27.8316** | 12.1856 | ±24.3713 | **-2.284** | **0.0224** | * |
| High cholesterol | +7.5486 | 10.2911 | ±20.5822 | +0.734 | 0.4633 |  |
| Kidney disease | +3.7796 | 17.4883 | ±34.9767 | +0.216 | 0.8289 |  |
| Circulatory disease | +0.2356 | 11.5197 | ±23.0395 | +0.020 | 0.9837 |  |
| Time < 54 (%) | +8.4301 | 4.5816 | ±9.1632 | +1.840 | 0.0658 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **205**, R² = **0.0708**, Adj R² = **0.0178**, F-statistic = **1.34** (p = **0.2067**), Residual SE = **68.885** on **193** df, AIC = **2328.7**, BIC = **2368.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.0664** | 40.8460 | ±81.6919 | **+9.623** | **6.39e-22** | *** |
| Education: graduate level (vs college) | +11.2428 | 12.8448 | ±25.6896 | +0.875 | 0.3814 |  |
| Education: high school or below (vs college) | -20.2772 | 13.7311 | ±27.4621 | -1.477 | 0.1397 |  |
| Site: UCSD (vs UAB) | -9.0843 | 12.9029 | ±25.8058 | -0.704 | 0.4814 |  |
| Site: UW (vs UAB) | -11.1930 | 12.9207 | ±25.8414 | -0.866 | 0.3863 |  |
| Age (years) | -0.0902 | 0.5435 | ±1.0869 | -0.166 | 0.8682 |  |
| BMI (kg/m2) | -0.3668 | 0.6533 | ±1.3067 | -0.561 | 0.5745 |  |
| **Hypertension** | **-27.4430** | 12.1760 | ±24.3520 | **-2.254** | **0.0242** | * |
| High cholesterol | +8.0886 | 10.2791 | ±20.5583 | +0.787 | 0.4313 |  |
| Kidney disease | +3.3306 | 17.5245 | ±35.0490 | +0.190 | 0.8493 |  |
| Circulatory disease | +0.7262 | 11.5293 | ±23.0585 | +0.063 | 0.9498 |  |
| Avg. daily time < 54 (%) | +5.8324 | 4.6481 | ±9.2962 | +1.255 | 0.2096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **205**, R² = **0.0671**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2493**), Residual SE = **69.022** on **193** df, AIC = **2329.5**, BIC = **2369.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.5258** | 40.9201 | ±81.8401 | **+9.617** | **6.78e-22** | *** |
| Education: graduate level (vs college) | +11.1794 | 12.9121 | ±25.8242 | +0.866 | 0.3866 |  |
| Education: high school or below (vs college) | -21.4370 | 13.8023 | ±27.6047 | -1.553 | 0.1204 |  |
| Site: UCSD (vs UAB) | -9.7867 | 12.8853 | ±25.7707 | -0.760 | 0.4475 |  |
| Site: UW (vs UAB) | -12.3584 | 12.8608 | ±25.7216 | -0.961 | 0.3366 |  |
| Age (years) | -0.0902 | 0.5482 | ±1.0964 | -0.165 | 0.8692 |  |
| BMI (kg/m2) | -0.3639 | 0.6522 | ±1.3044 | -0.558 | 0.5769 |  |
| **Hypertension** | **-27.0724** | 12.2528 | ±24.5056 | **-2.209** | **0.0271** | * |
| High cholesterol | +7.6854 | 10.3447 | ±20.6893 | +0.743 | 0.4575 |  |
| Kidney disease | +3.3437 | 17.5552 | ±35.1103 | +0.190 | 0.8489 |  |
| Circulatory disease | +1.6800 | 11.6975 | ±23.3950 | +0.144 | 0.8858 |  |
| Time 54-69, pooled (%) | +0.9819 | 2.2122 | ±4.4243 | +0.444 | 0.6571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **205**, R² = **0.0663**, Adj R² = **0.0131**, F-statistic = **1.25** (p = **0.2592**), Residual SE = **69.051** on **193** df, AIC = **2329.7**, BIC = **2369.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.9304** | 40.9270 | ±81.8540 | **+9.625** | **6.26e-22** | *** |
| Education: graduate level (vs college) | +10.7718 | 12.9269 | ±25.8537 | +0.833 | 0.4047 |  |
| Education: high school or below (vs college) | -21.4016 | 13.8414 | ±27.6829 | -1.546 | 0.1221 |  |
| Site: UCSD (vs UAB) | -10.0121 | 12.9038 | ±25.8077 | -0.776 | 0.4378 |  |
| Site: UW (vs UAB) | -12.4843 | 12.8307 | ±25.6614 | -0.973 | 0.3306 |  |
| Age (years) | -0.0801 | 0.5485 | ±1.0970 | -0.146 | 0.8838 |  |
| BMI (kg/m2) | -0.3665 | 0.6537 | ±1.3074 | -0.561 | 0.5750 |  |
| **Hypertension** | **-27.1109** | 12.2384 | ±24.4768 | **-2.215** | **0.0267** | * |
| High cholesterol | +7.7705 | 10.3408 | ±20.6817 | +0.751 | 0.4524 |  |
| Kidney disease | +3.3929 | 17.4922 | ±34.9844 | +0.194 | 0.8462 |  |
| Circulatory disease | +1.7227 | 11.7011 | ±23.4023 | +0.147 | 0.8830 |  |
| Avg. daily time 54-69 (%) | +0.5458 | 1.9810 | ±3.9621 | +0.276 | 0.7829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **205**, R² = **0.0685**, Adj R² = **0.0155**, F-statistic = **1.29** (p = **0.2319**), Residual SE = **68.968** on **193** df, AIC = **2329.2**, BIC = **2369.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.9884** | 40.9045 | ±81.8090 | **+9.607** | **7.44e-22** | *** |
| Education: graduate level (vs college) | +11.5127 | 12.9020 | ±25.8040 | +0.892 | 0.3722 |  |
| Education: high school or below (vs college) | -21.2855 | 13.7404 | ±27.4809 | -1.549 | 0.1214 |  |
| Site: UCSD (vs UAB) | -9.4085 | 12.8942 | ±25.7883 | -0.730 | 0.4656 |  |
| Site: UW (vs UAB) | -11.9301 | 12.9111 | ±25.8222 | -0.924 | 0.3555 |  |
| Age (years) | -0.0985 | 0.5481 | ±1.0962 | -0.180 | 0.8574 |  |
| BMI (kg/m2) | -0.3637 | 0.6504 | ±1.3007 | -0.559 | 0.5761 |  |
| **Hypertension** | **-27.1536** | 12.2588 | ±24.5175 | **-2.215** | **0.0268** | * |
| High cholesterol | +7.6091 | 10.3410 | ±20.6820 | +0.736 | 0.4618 |  |
| Kidney disease | +3.3592 | 17.5655 | ±35.1311 | +0.191 | 0.8483 |  |
| Circulatory disease | +1.4492 | 11.6710 | ±23.3421 | +0.124 | 0.9012 |  |
| Time < 70 (%) | +1.1954 | 1.7028 | ±3.4055 | +0.702 | 0.4827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **205**, R² = **0.0671**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2492**), Residual SE = **69.021** on **193** df, AIC = **2329.5**, BIC = **2369.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8583** | 40.9361 | ±81.8721 | **+9.621** | **6.50e-22** | *** |
| Education: graduate level (vs college) | +11.0941 | 12.9302 | ±25.8604 | +0.858 | 0.3909 |  |
| Education: high school or below (vs college) | -21.3421 | 13.7742 | ±27.5484 | -1.549 | 0.1213 |  |
| Site: UCSD (vs UAB) | -9.7617 | 12.9114 | ±25.8229 | -0.756 | 0.4496 |  |
| Site: UW (vs UAB) | -12.2305 | 12.8650 | ±25.7300 | -0.951 | 0.3418 |  |
| Age (years) | -0.0920 | 0.5486 | ±1.0972 | -0.168 | 0.8668 |  |
| BMI (kg/m2) | -0.3650 | 0.6528 | ±1.3057 | -0.559 | 0.5761 |  |
| **Hypertension** | **-27.1359** | 12.2446 | ±24.4891 | **-2.216** | **0.0267** | * |
| High cholesterol | +7.7740 | 10.3385 | ±20.6770 | +0.752 | 0.4521 |  |
| Kidney disease | +3.3440 | 17.5087 | ±35.0174 | +0.191 | 0.8485 |  |
| Circulatory disease | +1.5786 | 11.6747 | ±23.3494 | +0.135 | 0.8924 |  |
| Avg. daily time < 70 (%) | +0.7548 | 1.5239 | ±3.0479 | +0.495 | 0.6204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **205**, R² = **0.0900**, Adj R² = **0.0382**, F-statistic = **1.74** (p = **0.0681**), Residual SE = **68.168** on **193** df, AIC = **2324.4**, BIC = **2364.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+285.8052** | 60.0897 | ±120.1795 | **+4.756** | **1.97e-06** | *** |
| Education: graduate level (vs college) | +8.1879 | 12.7153 | ±25.4307 | +0.644 | 0.5196 |  |
| Education: high school or below (vs college) | -18.2000 | 13.1185 | ±26.2370 | -1.387 | 0.1653 |  |
| Site: UCSD (vs UAB) | -10.8490 | 12.4401 | ±24.8802 | -0.872 | 0.3832 |  |
| Site: UW (vs UAB) | -15.1612 | 12.7348 | ±25.4695 | -1.191 | 0.2338 |  |
| Age (years) | -0.0765 | 0.5242 | ±1.0484 | -0.146 | 0.8839 |  |
| BMI (kg/m2) | -0.4207 | 0.6534 | ±1.3067 | -0.644 | 0.5196 |  |
| **Hypertension** | **-26.2930** | 11.8747 | ±23.7494 | **-2.214** | **0.0268** | * |
| High cholesterol | +6.6256 | 10.1985 | ±20.3970 | +0.650 | 0.5159 |  |
| Kidney disease | +5.7265 | 17.2771 | ±34.5543 | +0.331 | 0.7403 |  |
| Circulatory disease | +3.1999 | 11.5213 | ±23.0426 | +0.278 | 0.7812 |  |
| **Time 54-250, pooled (%)** | **+1.1569** | 0.4708 | ±0.9415 | **+2.457** | **0.0140** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **205**, R² = **0.0932**, Adj R² = **0.0415**, F-statistic = **1.80** (p = **0.0558**), Residual SE = **68.050** on **193** df, AIC = **2323.7**, BIC = **2363.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+265.1368** | 62.3703 | ±124.7407 | **+4.251** | **2.13e-05** | *** |
| Education: graduate level (vs college) | +7.8150 | 12.7251 | ±25.4503 | +0.614 | 0.5391 |  |
| Education: high school or below (vs college) | -17.3868 | 13.0896 | ±26.1793 | -1.328 | 0.1841 |  |
| Site: UCSD (vs UAB) | -10.6384 | 12.3885 | ±24.7769 | -0.859 | 0.3905 |  |
| Site: UW (vs UAB) | -15.0953 | 12.7344 | ±25.4688 | -1.185 | 0.2359 |  |
| Age (years) | -0.0630 | 0.5243 | ±1.0486 | -0.120 | 0.9043 |  |
| BMI (kg/m2) | -0.4458 | 0.6547 | ±1.3094 | -0.681 | 0.4959 |  |
| **Hypertension** | **-26.1771** | 11.8651 | ±23.7303 | **-2.206** | **0.0274** | * |
| High cholesterol | +6.5994 | 10.1890 | ±20.3780 | +0.648 | 0.5172 |  |
| Kidney disease | +6.3897 | 17.3009 | ±34.6018 | +0.369 | 0.7119 |  |
| Circulatory disease | +3.6723 | 11.5332 | ±23.0664 | +0.318 | 0.7502 |  |
| **Avg. daily time 54-250 (%)** | **+1.3632** | 0.5023 | ±1.0045 | **+2.714** | **0.0066** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **205**, R² = **0.0828**, Adj R² = **0.0306**, F-statistic = **1.58** (p = **0.1057**), Residual SE = **68.436** on **193** df, AIC = **2326.0**, BIC = **2365.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.8669** | 40.9260 | ±81.8520 | **+9.697** | **3.10e-22** | *** |
| Education: graduate level (vs college) | +7.5687 | 12.8477 | ±25.6955 | +0.589 | 0.5558 |  |
| Education: high school or below (vs college) | -19.7527 | 13.3827 | ±26.7654 | -1.476 | 0.1399 |  |
| Site: UCSD (vs UAB) | -10.1042 | 12.4207 | ±24.8413 | -0.813 | 0.4159 |  |
| Site: UW (vs UAB) | -12.3047 | 13.1032 | ±26.2063 | -0.939 | 0.3477 |  |
| Age (years) | +0.0356 | 0.5433 | ±1.0867 | +0.066 | 0.9477 |  |
| BMI (kg/m2) | -0.3968 | 0.6501 | ±1.3002 | -0.610 | 0.5416 |  |
| **Hypertension** | **-27.9077** | 12.0328 | ±24.0656 | **-2.319** | **0.0204** | * |
| High cholesterol | +9.5571 | 10.1487 | ±20.2974 | +0.942 | 0.3463 |  |
| Kidney disease | +7.5878 | 17.9694 | ±35.9389 | +0.422 | 0.6728 |  |
| Circulatory disease | +1.9889 | 11.5836 | ±23.1673 | +0.172 | 0.8637 |  |
| Time 181-250, pooled (%) | -0.7632 | 0.4076 | ±0.8153 | -1.872 | 0.0612 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **205**, R² = **0.0829**, Adj R² = **0.0306**, F-statistic = **1.59** (p = **0.1055**), Residual SE = **68.435** on **193** df, AIC = **2326.0**, BIC = **2365.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.2124** | 40.9332 | ±81.8665 | **+9.728** | **2.28e-22** | *** |
| Education: graduate level (vs college) | +7.6416 | 12.9054 | ±25.8107 | +0.592 | 0.5538 |  |
| Education: high school or below (vs college) | -19.6202 | 13.3491 | ±26.6982 | -1.470 | 0.1416 |  |
| Site: UCSD (vs UAB) | -10.5094 | 12.4350 | ±24.8700 | -0.845 | 0.3980 |  |
| Site: UW (vs UAB) | -12.7104 | 13.1144 | ±26.2288 | -0.969 | 0.3324 |  |
| Age (years) | +0.0182 | 0.5414 | ±1.0829 | +0.034 | 0.9732 |  |
| BMI (kg/m2) | -0.4042 | 0.6524 | ±1.3047 | -0.620 | 0.5355 |  |
| **Hypertension** | **-28.0024** | 12.0560 | ±24.1120 | **-2.323** | **0.0202** | * |
| High cholesterol | +9.4837 | 10.1458 | ±20.2916 | +0.935 | 0.3499 |  |
| Kidney disease | +7.4615 | 17.9842 | ±35.9685 | +0.415 | 0.6782 |  |
| Circulatory disease | +2.0003 | 11.6076 | ±23.2152 | +0.172 | 0.8632 |  |
| Avg. daily time 181-250 (%) | -0.7408 | 0.4088 | ±0.8175 | -1.812 | 0.0699 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **205**, R² = **0.0937**, Adj R² = **0.0421**, F-statistic = **1.81** (p = **0.0538**), Residual SE = **68.029** on **193** df, AIC = **2323.6**, BIC = **2363.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.2707** | 40.4826 | ±80.9652 | **+9.887** | **4.72e-23** | *** |
| Education: graduate level (vs college) | +6.9721 | 12.8442 | ±25.6884 | +0.543 | 0.5873 |  |
| Education: high school or below (vs college) | -18.2489 | 13.0875 | ±26.1750 | -1.394 | 0.1632 |  |
| Site: UCSD (vs UAB) | -10.3055 | 12.2610 | ±24.5221 | -0.841 | 0.4006 |  |
| Site: UW (vs UAB) | -13.5413 | 13.0271 | ±26.0542 | -1.039 | 0.2986 |  |
| Age (years) | +0.0091 | 0.5329 | ±1.0659 | +0.017 | 0.9864 |  |
| BMI (kg/m2) | -0.4206 | 0.6494 | ±1.2987 | -0.648 | 0.5172 |  |
| **Hypertension** | **-27.3619** | 11.9021 | ±23.8042 | **-2.299** | **0.0215** | * |
| High cholesterol | +8.5743 | 10.0752 | ±20.1504 | +0.851 | 0.3947 |  |
| Kidney disease | +8.1311 | 17.7460 | ±35.4921 | +0.458 | 0.6468 |  |
| Circulatory disease | +2.6247 | 11.4598 | ±22.9196 | +0.229 | 0.8188 |  |
| **Time > 180 (%)** | **-0.6315** | 0.2563 | ±0.5126 | **-2.464** | **0.0137** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **205**, R² = **0.0938**, Adj R² = **0.0421**, F-statistic = **1.82** (p = **0.0537**), Residual SE = **68.028** on **193** df, AIC = **2323.6**, BIC = **2363.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.0644** | 40.5731 | ±81.1461 | **+9.885** | **4.84e-23** | *** |
| Education: graduate level (vs college) | +6.9752 | 12.8863 | ±25.7725 | +0.541 | 0.5883 |  |
| Education: high school or below (vs college) | -17.9468 | 13.0853 | ±26.1707 | -1.372 | 0.1702 |  |
| Site: UCSD (vs UAB) | -10.5198 | 12.2626 | ±24.5252 | -0.858 | 0.3910 |  |
| Site: UW (vs UAB) | -13.6831 | 13.0585 | ±26.1170 | -1.048 | 0.2947 |  |
| Age (years) | +0.0023 | 0.5330 | ±1.0660 | +0.004 | 0.9966 |  |
| BMI (kg/m2) | -0.4347 | 0.6527 | ±1.3054 | -0.666 | 0.5054 |  |
| **Hypertension** | **-27.4618** | 11.9379 | ±23.8758 | **-2.300** | **0.0214** | * |
| High cholesterol | +8.6985 | 10.0651 | ±20.1301 | +0.864 | 0.3875 |  |
| Kidney disease | +8.2465 | 17.7969 | ±35.5939 | +0.463 | 0.6431 |  |
| Circulatory disease | +2.7500 | 11.4794 | ±22.9588 | +0.240 | 0.8107 |  |
| **Avg. daily time > 180 (%)** | **-0.6365** | 0.2667 | ±0.5334 | **-2.387** | **0.0170** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **205**, R² = **0.0831**, Adj R² = **0.0309**, F-statistic = **1.59** (p = **0.1039**), Residual SE = **68.426** on **193** df, AIC = **2326.0**, BIC = **2365.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.4226** | 40.5053 | ±81.0107 | **+9.836** | **7.85e-23** | *** |
| Education: graduate level (vs college) | +8.3124 | 12.9115 | ±25.8230 | +0.644 | 0.5197 |  |
| Education: high school or below (vs college) | -19.9602 | 13.1835 | ±26.3669 | -1.514 | 0.1300 |  |
| Site: UCSD (vs UAB) | -10.4809 | 12.3977 | ±24.7954 | -0.845 | 0.3979 |  |
| Site: UW (vs UAB) | -13.5152 | 13.0681 | ±26.1361 | -1.034 | 0.3010 |  |
| Age (years) | -0.0583 | 0.5348 | ±1.0696 | -0.109 | 0.9132 |  |
| BMI (kg/m2) | -0.3874 | 0.6496 | ±1.2992 | -0.596 | 0.5509 |  |
| **Hypertension** | **-26.2139** | 12.0933 | ±24.1866 | **-2.168** | **0.0302** | * |
| High cholesterol | +8.8318 | 10.0998 | ±20.1997 | +0.874 | 0.3819 |  |
| Kidney disease | +5.3596 | 17.5896 | ±35.1792 | +0.305 | 0.7606 |  |
| Circulatory disease | +3.2454 | 11.4773 | ±22.9547 | +0.283 | 0.7774 |  |
| Nocturnal time > 180 (%) | -0.4919 | 0.2650 | ±0.5300 | -1.856 | 0.0634 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **205**, R² = **0.0921**, Adj R² = **0.0403**, F-statistic = **1.78** (p = **0.0598**), Residual SE = **68.091** on **193** df, AIC = **2323.9**, BIC = **2363.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.9023** | 40.5000 | ±81.0001 | **+9.849** | **6.89e-23** | *** |
| Education: graduate level (vs college) | +6.4104 | 12.7633 | ±25.5266 | +0.502 | 0.6155 |  |
| Education: high school or below (vs college) | -18.7538 | 13.8310 | ±27.6620 | -1.356 | 0.1751 |  |
| Site: UCSD (vs UAB) | -9.4791 | 12.3029 | ±24.6057 | -0.770 | 0.4410 |  |
| Site: UW (vs UAB) | -9.9111 | 13.1498 | ±26.2997 | -0.754 | 0.4510 |  |
| Age (years) | +0.1416 | 0.5592 | ±1.1184 | +0.253 | 0.8001 |  |
| BMI (kg/m2) | -0.5503 | 0.6399 | ±1.2797 | -0.860 | 0.3898 |  |
| **Hypertension** | **-26.6842** | 11.7820 | ±23.5640 | **-2.265** | **0.0235** | * |
| High cholesterol | +8.4182 | 10.1931 | ±20.3862 | +0.826 | 0.4089 |  |
| Kidney disease | +9.1991 | 17.8918 | ±35.7835 | +0.514 | 0.6071 |  |
| Circulatory disease | +1.2695 | 11.6406 | ±23.2812 | +0.109 | 0.9132 |  |
| **Any reading > 250 during wear (0/1)** | **-23.9643** | 11.3237 | ±22.6475 | **-2.116** | **0.0343** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **205**, R² = **0.0926**, Adj R² = **0.0409**, F-statistic = **1.79** (p = **0.0577**), Residual SE = **68.070** on **193** df, AIC = **2323.8**, BIC = **2363.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.4570** | 39.9793 | ±79.9586 | **+10.042** | **1.00e-23** | *** |
| Education: graduate level (vs college) | +8.2049 | 12.7136 | ±25.4273 | +0.645 | 0.5187 |  |
| Education: high school or below (vs college) | -17.8241 | 13.0996 | ±26.1993 | -1.361 | 0.1736 |  |
| Site: UCSD (vs UAB) | -10.6024 | 12.4094 | ±24.8188 | -0.854 | 0.3929 |  |
| Site: UW (vs UAB) | -14.9334 | 12.7361 | ±25.4723 | -1.173 | 0.2410 |  |
| Age (years) | -0.0791 | 0.5239 | ±1.0478 | -0.151 | 0.8800 |  |
| BMI (kg/m2) | -0.4246 | 0.6517 | ±1.3033 | -0.652 | 0.5147 |  |
| **Hypertension** | **-26.3431** | 11.8706 | ±23.7413 | **-2.219** | **0.0265** | * |
| High cholesterol | +6.5122 | 10.1896 | ±20.3791 | +0.639 | 0.5228 |  |
| Kidney disease | +5.9015 | 17.2679 | ±34.5358 | +0.342 | 0.7325 |  |
| Circulatory disease | +3.0635 | 11.4824 | ±22.9647 | +0.267 | 0.7896 |  |
| **Time > 250 (%)** | **-1.2238** | 0.4704 | ±0.9409 | **-2.601** | **0.0093** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **205**, R² = **0.0962**, Adj R² = **0.0446**, F-statistic = **1.87** (p = **0.0459**), Residual SE = **67.938** on **193** df, AIC = **2323.0**, BIC = **2362.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.7580** | 39.9952 | ±79.9903 | **+10.045** | **9.65e-24** | *** |
| Education: graduate level (vs college) | +7.9002 | 12.7175 | ±25.4350 | +0.621 | 0.5345 |  |
| Education: high school or below (vs college) | -16.8987 | 13.0883 | ±26.1766 | -1.291 | 0.1967 |  |
| Site: UCSD (vs UAB) | -10.3682 | 12.3535 | ±24.7070 | -0.839 | 0.4013 |  |
| Site: UW (vs UAB) | -14.8904 | 12.7462 | ±25.4924 | -1.168 | 0.2427 |  |
| Age (years) | -0.0709 | 0.5238 | ±1.0475 | -0.135 | 0.8923 |  |
| BMI (kg/m2) | -0.4501 | 0.6540 | ±1.3080 | -0.688 | 0.4913 |  |
| **Hypertension** | **-26.1880** | 11.8644 | ±23.7287 | **-2.207** | **0.0273** | * |
| High cholesterol | +6.5794 | 10.1717 | ±20.3433 | +0.647 | 0.5177 |  |
| Kidney disease | +6.5440 | 17.2989 | ±34.5979 | +0.378 | 0.7052 |  |
| Circulatory disease | +3.5417 | 11.5035 | ±23.0071 | +0.308 | 0.7582 |  |
| **Avg. daily time > 250 (%)** | **-1.4518** | 0.5262 | ±1.0525 | **-2.759** | **0.0058** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 203; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0902**, F-statistic = **3.00** (p = **0.0015**), Residual SE = **17.191** on **192** df, AIC = **1741.6**, BIC = **1778.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6324** | 11.0727 | ±22.1454 | **+6.108** | **1.01e-09** | *** |
| Education: graduate level (vs college) | -4.2421 | 2.8759 | ±5.7519 | -1.475 | 0.1402 |  |
| Education: high school or below (vs college) | -2.1048 | 3.5617 | ±7.1233 | -0.591 | 0.5546 |  |
| Site: UCSD (vs UAB) | +3.7145 | 3.3753 | ±6.7507 | +1.100 | 0.2711 |  |
| Site: UW (vs UAB) | +2.3003 | 3.3203 | ±6.6406 | +0.693 | 0.4884 |  |
| **Age (years)** | **-0.3506** | 0.1247 | ±0.2494 | **-2.811** | **0.0049** | ** |
| BMI (kg/m2) | +0.3236 | 0.1784 | ±0.3569 | +1.813 | 0.0698 | . |
| Hypertension | +1.6360 | 3.0762 | ±6.1523 | +0.532 | 0.5949 |  |
| High cholesterol | +1.1081 | 2.5558 | ±5.1117 | +0.434 | 0.6646 |  |
| Kidney disease | -1.3941 | 4.2140 | ±8.4280 | -0.331 | 0.7408 |  |
| **Circulatory disease** | **-6.4010** | 3.1006 | ±6.2012 | **-2.064** | **0.0390** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **203**, R² = **0.1429**, Adj R² = **0.0936**, F-statistic = **2.90** (p = **0.0015**), Residual SE = **17.159** on **191** df, AIC = **1741.8**, BIC = **1781.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1462** | 13.3881 | ±26.7763 | **+4.492** | **7.04e-06** | *** |
| Education: graduate level (vs college) | -3.7695 | 2.9377 | ±5.8753 | -1.283 | 0.1994 |  |
| Education: high school or below (vs college) | -2.5414 | 3.4876 | ±6.9751 | -0.729 | 0.4662 |  |
| Site: UCSD (vs UAB) | +3.8491 | 3.3698 | ±6.7395 | +1.142 | 0.2534 |  |
| Site: UW (vs UAB) | +2.4517 | 3.2934 | ±6.5868 | +0.744 | 0.4566 |  |
| **Age (years)** | **-0.3759** | 0.1253 | ±0.2506 | **-3.000** | **0.0027** | ** |
| BMI (kg/m2) | +0.3152 | 0.1763 | ±0.3526 | +1.788 | 0.0739 | . |
| Hypertension | +1.5542 | 3.0803 | ±6.1606 | +0.505 | 0.6139 |  |
| High cholesterol | +1.2333 | 2.5726 | ±5.1452 | +0.479 | 0.6316 |  |
| Kidney disease | -1.4062 | 4.1097 | ±8.2194 | -0.342 | 0.7322 |  |
| **Circulatory disease** | **-6.3256** | 3.1465 | ±6.2929 | **-2.010** | **0.0444** | * |
| HbA1c (%) | +1.4186 | 1.3551 | ±2.7101 | +1.047 | 0.2952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **203**, R² = **0.1394**, Adj R² = **0.0899**, F-statistic = **2.81** (p = **0.0020**), Residual SE = **17.194** on **191** df, AIC = **1742.6**, BIC = **1782.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7831** | 12.7656 | ±25.5312 | **+4.918** | **8.74e-07** | *** |
| Education: graduate level (vs college) | -4.0864 | 2.9015 | ±5.8030 | -1.408 | 0.1590 |  |
| Education: high school or below (vs college) | -2.3913 | 3.4901 | ±6.9802 | -0.685 | 0.4932 |  |
| Site: UCSD (vs UAB) | +3.6563 | 3.3925 | ±6.7851 | +1.078 | 0.2811 |  |
| Site: UW (vs UAB) | +2.3845 | 3.3070 | ±6.6139 | +0.721 | 0.4709 |  |
| **Age (years)** | **-0.3525** | 0.1243 | ±0.2487 | **-2.835** | **0.0046** | ** |
| BMI (kg/m2) | +0.3252 | 0.1792 | ±0.3584 | +1.815 | 0.0696 | . |
| Hypertension | +1.6274 | 3.1051 | ±6.2102 | +0.524 | 0.6002 |  |
| High cholesterol | +1.1191 | 2.5819 | ±5.1639 | +0.433 | 0.6647 |  |
| Kidney disease | -1.6906 | 4.1425 | ±8.2849 | -0.408 | 0.6832 |  |
| **Circulatory disease** | **-6.4622** | 3.1481 | ±6.2961 | **-2.053** | **0.0401** | * |
| Mean glucose (mg/dL) | +0.0362 | 0.0434 | ±0.0868 | +0.835 | 0.4040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **203**, R² = **0.1394**, Adj R² = **0.0899**, F-statistic = **2.81** (p = **0.0020**), Residual SE = **17.194** on **191** df, AIC = **1742.6**, BIC = **1782.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7697** | 16.6052 | ±33.2105 | **+3.479** | **5.03e-04** | *** |
| Education: graduate level (vs college) | -4.0864 | 2.9015 | ±5.8030 | -1.408 | 0.1590 |  |
| Education: high school or below (vs college) | -2.3913 | 3.4901 | ±6.9802 | -0.685 | 0.4932 |  |
| Site: UCSD (vs UAB) | +3.6563 | 3.3925 | ±6.7851 | +1.078 | 0.2811 |  |
| Site: UW (vs UAB) | +2.3845 | 3.3070 | ±6.6139 | +0.721 | 0.4709 |  |
| **Age (years)** | **-0.3525** | 0.1243 | ±0.2487 | **-2.835** | **0.0046** | ** |
| BMI (kg/m2) | +0.3252 | 0.1792 | ±0.3584 | +1.815 | 0.0696 | . |
| Hypertension | +1.6274 | 3.1051 | ±6.2102 | +0.524 | 0.6002 |  |
| High cholesterol | +1.1191 | 2.5819 | ±5.1639 | +0.433 | 0.6647 |  |
| Kidney disease | -1.6906 | 4.1425 | ±8.2849 | -0.408 | 0.6832 |  |
| **Circulatory disease** | **-6.4622** | 3.1481 | ±6.2961 | **-2.053** | **0.0401** | * |
| GMI (%) | +1.5146 | 1.8150 | ±3.6300 | +0.835 | 0.4040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **203**, R² = **0.1385**, Adj R² = **0.0889**, F-statistic = **2.79** (p = **0.0022**), Residual SE = **17.204** on **191** df, AIC = **1742.8**, BIC = **1782.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.4252** | 12.7015 | ±25.4031 | **+4.994** | **5.93e-07** | *** |
| Education: graduate level (vs college) | -4.2124 | 2.8847 | ±5.7694 | -1.460 | 0.1442 |  |
| Education: high school or below (vs college) | -2.3316 | 3.5011 | ±7.0023 | -0.666 | 0.5054 |  |
| Site: UCSD (vs UAB) | +3.6445 | 3.3988 | ±6.7975 | +1.072 | 0.2836 |  |
| Site: UW (vs UAB) | +2.3275 | 3.3009 | ±6.6018 | +0.705 | 0.4807 |  |
| **Age (years)** | **-0.3456** | 0.1253 | ±0.2506 | **-2.758** | **0.0058** | ** |
| BMI (kg/m2) | +0.3221 | 0.1789 | ±0.3579 | +1.800 | 0.0718 | . |
| Hypertension | +1.5316 | 3.1129 | ±6.2257 | +0.492 | 0.6227 |  |
| High cholesterol | +1.0721 | 2.5813 | ±5.1627 | +0.415 | 0.6779 |  |
| Kidney disease | -1.4560 | 4.1379 | ±8.2758 | -0.352 | 0.7249 |  |
| **Circulatory disease** | **-6.4844** | 3.1452 | ±6.2903 | **-2.062** | **0.0392** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0312 | 0.0394 | ±0.0789 | +0.793 | 0.4281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **203**, R² = **0.1355**, Adj R² = **0.0857**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.233** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1687** | 11.2682 | ±22.5363 | **+5.961** | **2.51e-09** | *** |
| Education: graduate level (vs college) | -4.1434 | 2.9772 | ±5.9545 | -1.392 | 0.1640 |  |
| Education: high school or below (vs college) | -2.2563 | 3.5308 | ±7.0617 | -0.639 | 0.5228 |  |
| Site: UCSD (vs UAB) | +3.7160 | 3.3895 | ±6.7789 | +1.096 | 0.2729 |  |
| Site: UW (vs UAB) | +2.3409 | 3.3349 | ±6.6699 | +0.702 | 0.4827 |  |
| **Age (years)** | **-0.3556** | 0.1285 | ±0.2569 | **-2.768** | **0.0056** | ** |
| BMI (kg/m2) | +0.3256 | 0.1793 | ±0.3586 | +1.816 | 0.0694 | . |
| Hypertension | +1.6471 | 3.0911 | ±6.1822 | +0.533 | 0.5941 |  |
| High cholesterol | +1.1169 | 2.5744 | ±5.1487 | +0.434 | 0.6644 |  |
| Kidney disease | -1.5805 | 4.2790 | ±8.5580 | -0.369 | 0.7118 |  |
| **Circulatory disease** | **-6.3799** | 3.1161 | ±6.2322 | **-2.047** | **0.0406** | * |
| Glucose SD, pooled (mg/dL) | +0.0203 | 0.0923 | ±0.1846 | +0.220 | 0.8259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5091** | 11.3261 | ±22.6523 | **+5.960** | **2.52e-09** | *** |
| Education: graduate level (vs college) | -4.2178 | 2.9735 | ±5.9469 | -1.418 | 0.1561 |  |
| Education: high school or below (vs college) | -2.1469 | 3.5458 | ±7.0916 | -0.605 | 0.5449 |  |
| Site: UCSD (vs UAB) | +3.7153 | 3.3925 | ±6.7849 | +1.095 | 0.2734 |  |
| Site: UW (vs UAB) | +2.3081 | 3.3385 | ±6.6771 | +0.691 | 0.4893 |  |
| **Age (years)** | **-0.3518** | 0.1286 | ±0.2572 | **-2.735** | **0.0062** | ** |
| BMI (kg/m2) | +0.3242 | 0.1799 | ±0.3598 | +1.802 | 0.0715 | . |
| Hypertension | +1.6413 | 3.0910 | ±6.1819 | +0.531 | 0.5954 |  |
| High cholesterol | +1.1078 | 2.5780 | ±5.1561 | +0.430 | 0.6674 |  |
| Kidney disease | -1.4391 | 4.2813 | ±8.5626 | -0.336 | 0.7368 |  |
| **Circulatory disease** | **-6.3940** | 3.1190 | ±6.2379 | **-2.050** | **0.0404** | * |
| Avg. daily SD (mg/dL) | +0.0057 | 0.1133 | ±0.2267 | +0.051 | 0.9596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **203**, R² = **0.1353**, Adj R² = **0.0855**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.235** on **191** df, AIC = **1743.6**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0742** | 11.4012 | ±22.8023 | **+5.971** | **2.36e-09** | *** |
| Education: graduate level (vs college) | -4.3187 | 3.0363 | ±6.0726 | -1.422 | 0.1549 |  |
| Education: high school or below (vs college) | -1.9960 | 3.5004 | ±7.0008 | -0.570 | 0.5685 |  |
| Site: UCSD (vs UAB) | +3.7113 | 3.3911 | ±6.7823 | +1.094 | 0.2738 |  |
| Site: UW (vs UAB) | +2.2740 | 3.3337 | ±6.6675 | +0.682 | 0.4952 |  |
| **Age (years)** | **-0.3453** | 0.1343 | ±0.2686 | **-2.571** | **0.0101** | * |
| BMI (kg/m2) | +0.3221 | 0.1800 | ±0.3601 | +1.789 | 0.0736 | . |
| Hypertension | +1.6190 | 3.0900 | ±6.1799 | +0.524 | 0.6003 |  |
| High cholesterol | +1.1089 | 2.5687 | ±5.1374 | +0.432 | 0.6660 |  |
| Kidney disease | -1.2565 | 4.3435 | ±8.6870 | -0.289 | 0.7724 |  |
| **Circulatory disease** | **-6.4225** | 3.1128 | ±6.2257 | **-2.063** | **0.0391** | * |
| CV (%) | -0.0289 | 0.2053 | ±0.4105 | -0.141 | 0.8879 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **203**, R² = **0.1366**, Adj R² = **0.0869**, F-statistic = **2.75** (p = **0.0025**), Residual SE = **17.223** on **191** df, AIC = **1743.3**, BIC = **1783.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.1670** | 13.2307 | ±26.4615 | **+5.379** | **7.49e-08** | *** |
| Education: graduate level (vs college) | -3.9774 | 3.0485 | ±6.0969 | -1.305 | 0.1920 |  |
| Education: high school or below (vs college) | -2.5054 | 3.5131 | ±7.0262 | -0.713 | 0.4758 |  |
| Site: UCSD (vs UAB) | +3.6633 | 3.3821 | ±6.7642 | +1.083 | 0.2787 |  |
| Site: UW (vs UAB) | +2.3443 | 3.3224 | ±6.6449 | +0.706 | 0.4804 |  |
| **Age (years)** | **-0.3709** | 0.1334 | ±0.2668 | **-2.781** | **0.0054** | ** |
| BMI (kg/m2) | +0.3257 | 0.1784 | ±0.3567 | +1.826 | 0.0679 | . |
| Hypertension | +1.7238 | 3.0808 | ±6.1616 | +0.560 | 0.5758 |  |
| High cholesterol | +1.1033 | 2.5736 | ±5.1472 | +0.429 | 0.6681 |  |
| Kidney disease | -1.7339 | 4.2404 | ±8.4808 | -0.409 | 0.6826 |  |
| **Circulatory disease** | **-6.4155** | 3.1214 | ±6.2429 | **-2.055** | **0.0398** | * |
| Mean / SD ratio | -0.5329 | 1.0094 | ±2.0188 | -0.528 | 0.5975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **203**, R² = **0.1355**, Adj R² = **0.0857**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.234** on **191** df, AIC = **1743.6**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.0754** | 13.2760 | ±26.5521 | **+5.203** | **1.96e-07** | *** |
| Education: graduate level (vs college) | -4.1262 | 3.0583 | ±6.1166 | -1.349 | 0.1773 |  |
| Education: high school or below (vs college) | -2.2733 | 3.5298 | ±7.0596 | -0.644 | 0.5196 |  |
| Site: UCSD (vs UAB) | +3.6797 | 3.3837 | ±6.7675 | +1.087 | 0.2768 |  |
| Site: UW (vs UAB) | +2.3020 | 3.3408 | ±6.6817 | +0.689 | 0.4908 |  |
| **Age (years)** | **-0.3592** | 0.1344 | ±0.2687 | **-2.673** | **0.0075** | ** |
| BMI (kg/m2) | +0.3250 | 0.1792 | ±0.3584 | +1.814 | 0.0697 | . |
| Hypertension | +1.6879 | 3.0909 | ±6.1818 | +0.546 | 0.5850 |  |
| High cholesterol | +1.0855 | 2.5873 | ±5.1745 | +0.420 | 0.6748 |  |
| Kidney disease | -1.4895 | 4.2304 | ±8.4608 | -0.352 | 0.7248 |  |
| **Circulatory disease** | **-6.3971** | 3.1221 | ±6.2441 | **-2.049** | **0.0405** | * |
| Avg. daily mean/SD | -0.1843 | 0.8672 | ±1.7344 | -0.212 | 0.8317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **203**, R² = **0.1381**, Adj R² = **0.0885**, F-statistic = **2.78** (p = **0.0022**), Residual SE = **17.207** on **191** df, AIC = **1742.9**, BIC = **1782.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7550** | 11.1191 | ±22.2382 | **+6.363** | **1.97e-10** | *** |
| Education: graduate level (vs college) | -4.4921 | 2.9380 | ±5.8760 | -1.529 | 0.1263 |  |
| Education: high school or below (vs college) | -1.6228 | 3.6273 | ±7.2547 | -0.447 | 0.6546 |  |
| Site: UCSD (vs UAB) | +3.9018 | 3.3816 | ±6.7632 | +1.154 | 0.2486 |  |
| Site: UW (vs UAB) | +2.0805 | 3.3291 | ±6.6582 | +0.625 | 0.5320 |  |
| **Age (years)** | **-0.3421** | 0.1269 | ±0.2539 | **-2.695** | **0.0070** | ** |
| BMI (kg/m2) | +0.3364 | 0.1785 | ±0.3570 | +1.885 | 0.0595 | . |
| Hypertension | +1.5075 | 3.0879 | ±6.1759 | +0.488 | 0.6254 |  |
| High cholesterol | +1.1826 | 2.5716 | ±5.1431 | +0.460 | 0.6456 |  |
| Kidney disease | -1.3288 | 4.2012 | ±8.4025 | -0.316 | 0.7518 |  |
| **Circulatory disease** | **-6.4459** | 3.0940 | ±6.1881 | **-2.083** | **0.0372** | * |
| MAG (mg/dL/h) | -0.0893 | 0.1178 | ±0.2355 | -0.758 | 0.4484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6909** | 11.4365 | ±22.8730 | **+5.919** | **3.24e-09** | *** |
| Education: graduate level (vs college) | -4.2508 | 2.9868 | ±5.9737 | -1.423 | 0.1547 |  |
| Education: high school or below (vs college) | -2.0897 | 3.5515 | ±7.1031 | -0.588 | 0.5563 |  |
| Site: UCSD (vs UAB) | +3.7157 | 3.3899 | ±6.7797 | +1.096 | 0.2730 |  |
| Site: UW (vs UAB) | +2.2987 | 3.3394 | ±6.6787 | +0.688 | 0.4912 |  |
| **Age (years)** | **-0.3502** | 0.1290 | ±0.2580 | **-2.715** | **0.0066** | ** |
| BMI (kg/m2) | +0.3234 | 0.1797 | ±0.3595 | +1.799 | 0.0720 | . |
| Hypertension | +1.6326 | 3.0886 | ±6.1771 | +0.529 | 0.5971 |  |
| High cholesterol | +1.1094 | 2.5852 | ±5.1704 | +0.429 | 0.6678 |  |
| Kidney disease | -1.3791 | 4.2658 | ±8.5316 | -0.323 | 0.7465 |  |
| **Circulatory disease** | **-6.4017** | 3.1167 | ±6.2334 | **-2.054** | **0.0400** | * |
| Avg. daily range (mg/dL) | -0.0005 | 0.0312 | ±0.0624 | -0.017 | 0.9860 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **203**, R² = **0.1392**, Adj R² = **0.0896**, F-statistic = **2.81** (p = **0.0020**), Residual SE = **17.197** on **191** df, AIC = **1742.7**, BIC = **1782.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.6814** | 11.1378 | ±22.2756 | **+5.987** | **2.14e-09** | *** |
| Education: graduate level (vs college) | -3.8812 | 2.9587 | ±5.9173 | -1.312 | 0.1896 |  |
| Education: high school or below (vs college) | -2.2300 | 3.5394 | ±7.0788 | -0.630 | 0.5287 |  |
| Site: UCSD (vs UAB) | +3.6491 | 3.3789 | ±6.7577 | +1.080 | 0.2801 |  |
| Site: UW (vs UAB) | +2.4662 | 3.3209 | ±6.6418 | +0.743 | 0.4577 |  |
| **Age (years)** | **-0.3609** | 0.1254 | ±0.2508 | **-2.878** | **0.0040** | ** |
| BMI (kg/m2) | +0.3278 | 0.1769 | ±0.3539 | +1.853 | 0.0639 | . |
| Hypertension | +1.4426 | 3.1121 | ±6.2243 | +0.464 | 0.6430 |  |
| High cholesterol | +1.1959 | 2.5765 | ±5.1529 | +0.464 | 0.6425 |  |
| Kidney disease | -1.8568 | 4.1926 | ±8.3852 | -0.443 | 0.6579 |  |
| **Circulatory disease** | **-6.5223** | 3.1205 | ±6.2411 | **-2.090** | **0.0366** | * |
| SD of daily means (mg/dL) | +0.1192 | 0.1185 | ±0.2369 | +1.006 | 0.3142 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **203**, R² = **0.1401**, Adj R² = **0.0906**, F-statistic = **2.83** (p = **0.0019**), Residual SE = **17.188** on **191** df, AIC = **1742.5**, BIC = **1782.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7003** | 12.6643 | ±25.3286 | **+5.820** | **5.90e-09** | *** |
| Education: graduate level (vs college) | -3.8422 | 2.9489 | ±5.8977 | -1.303 | 0.1926 |  |
| Education: high school or below (vs college) | -2.4164 | 3.4918 | ±6.9836 | -0.692 | 0.4889 |  |
| Site: UCSD (vs UAB) | +3.7361 | 3.3746 | ±6.7492 | +1.107 | 0.2682 |  |
| Site: UW (vs UAB) | +2.4561 | 3.3305 | ±6.6609 | +0.737 | 0.4608 |  |
| **Age (years)** | **-0.3593** | 0.1243 | ±0.2487 | **-2.890** | **0.0039** | ** |
| BMI (kg/m2) | +0.3299 | 0.1781 | ±0.3562 | +1.852 | 0.0640 | . |
| Hypertension | +1.7168 | 3.0861 | ±6.1722 | +0.556 | 0.5780 |  |
| High cholesterol | +1.0033 | 2.5875 | ±5.1749 | +0.388 | 0.6982 |  |
| Kidney disease | -1.9044 | 4.1679 | ±8.3359 | -0.457 | 0.6477 |  |
| **Circulatory disease** | **-6.5374** | 3.1314 | ±6.2627 | **-2.088** | **0.0368** | * |
| Time in range 70-180, pooled (%) | -0.0693 | 0.0738 | ±0.1476 | -0.939 | 0.3477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **203**, R² = **0.1402**, Adj R² = **0.0907**, F-statistic = **2.83** (p = **0.0019**), Residual SE = **17.186** on **191** df, AIC = **1742.4**, BIC = **1782.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7442** | 12.5534 | ±25.1067 | **+5.874** | **4.24e-09** | *** |
| Education: graduate level (vs college) | -3.8390 | 2.9492 | ±5.8984 | -1.302 | 0.1930 |  |
| Education: high school or below (vs college) | -2.4573 | 3.4923 | ±6.9846 | -0.704 | 0.4817 |  |
| Site: UCSD (vs UAB) | +3.7512 | 3.3738 | ±6.7476 | +1.112 | 0.2662 |  |
| Site: UW (vs UAB) | +2.4712 | 3.3364 | ±6.6729 | +0.741 | 0.4589 |  |
| **Age (years)** | **-0.3593** | 0.1243 | ±0.2486 | **-2.890** | **0.0039** | ** |
| BMI (kg/m2) | +0.3314 | 0.1784 | ±0.3569 | +1.857 | 0.0633 | . |
| Hypertension | +1.7354 | 3.0853 | ±6.1706 | +0.562 | 0.5738 |  |
| High cholesterol | +0.9972 | 2.5849 | ±5.1698 | +0.386 | 0.6997 |  |
| Kidney disease | -1.9244 | 4.1675 | ±8.3349 | -0.462 | 0.6442 |  |
| **Circulatory disease** | **-6.5499** | 3.1335 | ±6.2670 | **-2.090** | **0.0366** | * |
| Avg. daily time in range 70-180 (%) | -0.0702 | 0.0722 | ±0.1444 | -0.973 | 0.3307 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.1412**, Adj R² = **0.0917**, F-statistic = **2.85** (p = **0.0017**), Residual SE = **17.177** on **191** df, AIC = **1742.2**, BIC = **1782.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.0415** | 11.0255 | ±22.0509 | **+6.081** | **1.20e-09** | *** |
| Education: graduate level (vs college) | -4.0421 | 2.8698 | ±5.7397 | -1.408 | 0.1590 |  |
| Education: high school or below (vs college) | -1.7825 | 3.6388 | ±7.2777 | -0.490 | 0.6242 |  |
| Site: UCSD (vs UAB) | +4.1228 | 3.3749 | ±6.7497 | +1.222 | 0.2219 |  |
| Site: UW (vs UAB) | +2.8425 | 3.3526 | ±6.7052 | +0.848 | 0.3965 |  |
| **Age (years)** | **-0.3541** | 0.1251 | ±0.2502 | **-2.831** | **0.0046** | ** |
| BMI (kg/m2) | +0.3212 | 0.1767 | ±0.3535 | +1.817 | 0.0692 | . |
| Hypertension | +1.4572 | 3.0727 | ±6.1453 | +0.474 | 0.6353 |  |
| High cholesterol | +1.0558 | 2.5580 | ±5.1160 | +0.413 | 0.6798 |  |
| Kidney disease | -1.3338 | 4.2262 | ±8.4525 | -0.316 | 0.7523 |  |
| **Circulatory disease** | **-6.7135** | 3.0802 | ±6.1603 | **-2.180** | **0.0293** | * |
| Time < 54 (%) | +1.8419 | 1.2267 | ±2.4534 | +1.502 | 0.1332 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **203**, R² = **0.1360**, Adj R² = **0.0863**, F-statistic = **2.73** (p = **0.0026**), Residual SE = **17.228** on **191** df, AIC = **1743.4**, BIC = **1783.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5754** | 11.0797 | ±22.1593 | **+6.099** | **1.07e-09** | *** |
| Education: graduate level (vs college) | -4.1422 | 2.8861 | ±5.7722 | -1.435 | 0.1512 |  |
| Education: high school or below (vs college) | -1.9959 | 3.6032 | ±7.2065 | -0.554 | 0.5796 |  |
| Site: UCSD (vs UAB) | +3.8420 | 3.3957 | ±6.7914 | +1.131 | 0.2579 |  |
| Site: UW (vs UAB) | +2.4494 | 3.3526 | ±6.7051 | +0.731 | 0.4650 |  |
| **Age (years)** | **-0.3541** | 0.1263 | ±0.2526 | **-2.804** | **0.0050** | ** |
| BMI (kg/m2) | +0.3238 | 0.1788 | ±0.3576 | +1.811 | 0.0701 | . |
| Hypertension | +1.5993 | 3.0842 | ±6.1685 | +0.519 | 0.6041 |  |
| High cholesterol | +1.1344 | 2.5782 | ±5.1565 | +0.440 | 0.6599 |  |
| Kidney disease | -1.4105 | 4.2266 | ±8.4531 | -0.334 | 0.7386 |  |
| **Circulatory disease** | **-6.5098** | 3.1536 | ±6.3072 | **-2.064** | **0.0390** | * |
| Avg. daily time < 54 (%) | +0.6086 | 2.1114 | ±4.2227 | +0.288 | 0.7732 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.1356**, Adj R² = **0.0858**, F-statistic = **2.72** (p = **0.0027**), Residual SE = **17.233** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6826** | 11.1164 | ±22.2329 | **+6.089** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -4.3722 | 2.9633 | ±5.9266 | -1.475 | 0.1401 |  |
| Education: high school or below (vs college) | -2.0773 | 3.5552 | ±7.1103 | -0.584 | 0.5590 |  |
| Site: UCSD (vs UAB) | +3.6451 | 3.4156 | ±6.8311 | +1.067 | 0.2859 |  |
| Site: UW (vs UAB) | +2.2594 | 3.3236 | ±6.6472 | +0.680 | 0.4966 |  |
| **Age (years)** | **-0.3462** | 0.1262 | ±0.2523 | **-2.745** | **0.0061** | ** |
| BMI (kg/m2) | +0.3227 | 0.1793 | ±0.3587 | +1.799 | 0.0720 | . |
| Hypertension | +1.6213 | 3.0951 | ±6.1902 | +0.524 | 0.6004 |  |
| High cholesterol | +1.1333 | 2.5746 | ±5.1493 | +0.440 | 0.6598 |  |
| Kidney disease | -1.3750 | 4.2282 | ±8.4564 | -0.325 | 0.7450 |  |
| **Circulatory disease** | **-6.3851** | 3.1324 | ±6.2648 | **-2.038** | **0.0415** | * |
| Time 54-69, pooled (%) | -0.1393 | 0.5385 | ±1.0771 | -0.259 | 0.7960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **203**, R² = **0.1363**, Adj R² = **0.0866**, F-statistic = **2.74** (p = **0.0026**), Residual SE = **17.225** on **191** df, AIC = **1743.3**, BIC = **1783.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6097** | 11.1117 | ±22.2235 | **+6.085** | **1.17e-09** | *** |
| Education: graduate level (vs college) | -4.4534 | 2.9619 | ±5.9239 | -1.504 | 0.1327 |  |
| Education: high school or below (vs college) | -2.0356 | 3.5372 | ±7.0745 | -0.575 | 0.5650 |  |
| Site: UCSD (vs UAB) | +3.6034 | 3.4237 | ±6.8473 | +1.053 | 0.2926 |  |
| Site: UW (vs UAB) | +2.2306 | 3.3141 | ±6.6282 | +0.673 | 0.5009 |  |
| **Age (years)** | **-0.3420** | 0.1267 | ±0.2533 | **-2.700** | **0.0069** | ** |
| BMI (kg/m2) | +0.3220 | 0.1795 | ±0.3590 | +1.794 | 0.0728 | . |
| Hypertension | +1.6136 | 3.1026 | ±6.2052 | +0.520 | 0.6030 |  |
| High cholesterol | +1.1436 | 2.5769 | ±5.1538 | +0.444 | 0.6572 |  |
| Kidney disease | -1.3596 | 4.2219 | ±8.4439 | -0.322 | 0.7474 |  |
| **Circulatory disease** | **-6.3785** | 3.1373 | ±6.2746 | **-2.033** | **0.0420** | * |
| Avg. daily time 54-69 (%) | -0.2271 | 0.5265 | ±1.0530 | -0.431 | 0.6662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6177** | 11.1101 | ±22.2202 | **+6.086** | **1.16e-09** | *** |
| Education: graduate level (vs college) | -4.2196 | 2.9360 | ±5.8720 | -1.437 | 0.1507 |  |
| Education: high school or below (vs college) | -2.1053 | 3.5853 | ±7.1707 | -0.587 | 0.5571 |  |
| Site: UCSD (vs UAB) | +3.7301 | 3.4081 | ±6.8163 | +1.094 | 0.2738 |  |
| Site: UW (vs UAB) | +2.3130 | 3.3399 | ±6.6798 | +0.693 | 0.4886 |  |
| **Age (years)** | **-0.3513** | 0.1261 | ±0.2523 | **-2.785** | **0.0054** | ** |
| BMI (kg/m2) | +0.3237 | 0.1789 | ±0.3578 | +1.809 | 0.0704 | . |
| Hypertension | +1.6361 | 3.0874 | ±6.1747 | +0.530 | 0.5961 |  |
| High cholesterol | +1.1035 | 2.5697 | ±5.1395 | +0.429 | 0.6676 |  |
| Kidney disease | -1.3964 | 4.2340 | ±8.4681 | -0.330 | 0.7415 |  |
| **Circulatory disease** | **-6.4072** | 3.1271 | ±6.2543 | **-2.049** | **0.0405** | * |
| Time < 70 (%) | +0.0216 | 0.4453 | ±0.8905 | +0.048 | 0.9614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **203**, R² = **0.1356**, Adj R² = **0.0858**, F-statistic = **2.72** (p = **0.0027**), Residual SE = **17.232** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6317** | 11.1111 | ±22.2222 | **+6.087** | **1.15e-09** | *** |
| Education: graduate level (vs college) | -4.3619 | 2.9408 | ±5.8815 | -1.483 | 0.1380 |  |
| Education: high school or below (vs college) | -2.0910 | 3.5568 | ±7.1136 | -0.588 | 0.5566 |  |
| Site: UCSD (vs UAB) | +3.6381 | 3.4169 | ±6.8339 | +1.065 | 0.2870 |  |
| Site: UW (vs UAB) | +2.2399 | 3.3249 | ±6.6497 | +0.674 | 0.5005 |  |
| **Age (years)** | **-0.3458** | 0.1269 | ±0.2539 | **-2.724** | **0.0064** | ** |
| BMI (kg/m2) | +0.3228 | 0.1794 | ±0.3588 | +1.799 | 0.0720 | . |
| Hypertension | +1.6317 | 3.0977 | ±6.1953 | +0.527 | 0.5984 |  |
| High cholesterol | +1.1205 | 2.5727 | ±5.1454 | +0.436 | 0.6632 |  |
| Kidney disease | -1.3745 | 4.2267 | ±8.4534 | -0.325 | 0.7450 |  |
| **Circulatory disease** | **-6.3706** | 3.1408 | ±6.2817 | **-2.028** | **0.0425** | * |
| Avg. daily time < 70 (%) | -0.1095 | 0.4427 | ±0.8854 | -0.247 | 0.8047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.1353**, Adj R² = **0.0855**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.235** on **191** df, AIC = **1743.6**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.2618** | 19.6976 | ±39.3952 | **+3.516** | **4.38e-04** | *** |
| Education: graduate level (vs college) | -4.2113 | 2.9018 | ±5.8037 | -1.451 | 0.1467 |  |
| Education: high school or below (vs college) | -2.1535 | 3.5995 | ±7.1991 | -0.598 | 0.5497 |  |
| Site: UCSD (vs UAB) | +3.7196 | 3.3883 | ±6.7765 | +1.098 | 0.2723 |  |
| Site: UW (vs UAB) | +2.3389 | 3.3457 | ±6.6914 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.3503** | 0.1250 | ±0.2500 | **-2.802** | **0.0051** | ** |
| BMI (kg/m2) | +0.3244 | 0.1789 | ±0.3577 | +1.814 | 0.0697 | . |
| Hypertension | +1.6262 | 3.0977 | ±6.1954 | +0.525 | 0.5996 |  |
| High cholesterol | +1.1266 | 2.5805 | ±5.1609 | +0.437 | 0.6624 |  |
| Kidney disease | -1.4281 | 4.2295 | ±8.4591 | -0.338 | 0.7356 |  |
| **Circulatory disease** | **-6.4240** | 3.1455 | ±6.2910 | **-2.042** | **0.0411** | * |
| Time 54-250, pooled (%) | -0.0175 | 0.1680 | ±0.3360 | -0.104 | 0.9168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.1358**, Adj R² = **0.0860**, F-statistic = **2.73** (p = **0.0027**), Residual SE = **17.231** on **191** df, AIC = **1743.5**, BIC = **1783.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.3799** | 21.5038 | ±43.0075 | **+3.366** | **7.63e-04** | *** |
| Education: graduate level (vs college) | -4.1539 | 2.9036 | ±5.8071 | -1.431 | 0.1525 |  |
| Education: high school or below (vs college) | -2.2540 | 3.6030 | ±7.2059 | -0.626 | 0.5316 |  |
| Site: UCSD (vs UAB) | +3.7158 | 3.3930 | ±6.7859 | +1.095 | 0.2735 |  |
| Site: UW (vs UAB) | +2.3924 | 3.3433 | ±6.6866 | +0.716 | 0.4742 |  |
| **Age (years)** | **-0.3502** | 0.1248 | ±0.2497 | **-2.805** | **0.0050** | ** |
| BMI (kg/m2) | +0.3265 | 0.1787 | ±0.3573 | +1.828 | 0.0676 | . |
| Hypertension | +1.6093 | 3.0927 | ±6.1855 | +0.520 | 0.6028 |  |
| High cholesterol | +1.1552 | 2.5801 | ±5.1602 | +0.448 | 0.6543 |  |
| Kidney disease | -1.5015 | 4.2275 | ±8.4550 | -0.355 | 0.7225 |  |
| **Circulatory disease** | **-6.4745** | 3.1515 | ±6.3029 | **-2.054** | **0.0399** | * |
| Avg. daily time 54-250 (%) | -0.0505 | 0.1901 | ±0.3802 | -0.266 | 0.7903 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.1457**, Adj R² = **0.0965**, F-statistic = **2.96** (p = **0.0012**), Residual SE = **17.132** on **191** df, AIC = **1741.1**, BIC = **1780.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8734** | 11.1651 | ±22.3301 | **+5.990** | **2.10e-09** | *** |
| Education: graduate level (vs college) | -3.7694 | 2.9396 | ±5.8792 | -1.282 | 0.1997 |  |
| Education: high school or below (vs college) | -2.3379 | 3.4470 | ±6.8939 | -0.678 | 0.4976 |  |
| Site: UCSD (vs UAB) | +3.6417 | 3.3706 | ±6.7412 | +1.080 | 0.2800 |  |
| Site: UW (vs UAB) | +2.2632 | 3.2944 | ±6.5887 | +0.687 | 0.4921 |  |
| **Age (years)** | **-0.3681** | 0.1245 | ±0.2490 | **-2.957** | **0.0031** | ** |
| BMI (kg/m2) | +0.3292 | 0.1779 | ±0.3558 | +1.850 | 0.0643 | . |
| Hypertension | +1.8836 | 3.0940 | ±6.1880 | +0.609 | 0.5427 |  |
| High cholesterol | +0.7419 | 2.5751 | ±5.1501 | +0.288 | 0.7733 |  |
| Kidney disease | -2.2051 | 4.1118 | ±8.2236 | -0.536 | 0.5918 |  |
| **Circulatory disease** | **-6.4845** | 3.1138 | ±6.2276 | **-2.083** | **0.0373** | * |
| Time 181-250, pooled (%) | +0.1533 | 0.1068 | ±0.2136 | +1.436 | 0.1510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **203**, R² = **0.1442**, Adj R² = **0.0949**, F-statistic = **2.92** (p = **0.0014**), Residual SE = **17.147** on **191** df, AIC = **1741.5**, BIC = **1781.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.6725** | 11.1784 | ±22.3569 | **+5.964** | **2.46e-09** | *** |
| Education: graduate level (vs college) | -3.8210 | 2.9420 | ±5.8841 | -1.299 | 0.1940 |  |
| Education: high school or below (vs college) | -2.3472 | 3.4535 | ±6.9070 | -0.680 | 0.4967 |  |
| Site: UCSD (vs UAB) | +3.7157 | 3.3720 | ±6.7439 | +1.102 | 0.2705 |  |
| Site: UW (vs UAB) | +2.3423 | 3.3078 | ±6.6157 | +0.708 | 0.4789 |  |
| **Age (years)** | **-0.3634** | 0.1244 | ±0.2488 | **-2.921** | **0.0035** | ** |
| BMI (kg/m2) | +0.3300 | 0.1783 | ±0.3565 | +1.851 | 0.0641 | . |
| Hypertension | +1.8894 | 3.0939 | ±6.1877 | +0.611 | 0.5414 |  |
| High cholesterol | +0.7845 | 2.5744 | ±5.1488 | +0.305 | 0.7606 |  |
| Kidney disease | -2.1188 | 4.1242 | ±8.2485 | -0.514 | 0.6074 |  |
| **Circulatory disease** | **-6.4791** | 3.1187 | ±6.2373 | **-2.078** | **0.0378** | * |
| Avg. daily time 181-250 (%) | +0.1374 | 0.1034 | ±0.2068 | +1.329 | 0.1840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **203**, R² = **0.1398**, Adj R² = **0.0903**, F-statistic = **2.82** (p = **0.0019**), Residual SE = **17.190** on **191** df, AIC = **1742.5**, BIC = **1782.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8585** | 11.1293 | ±22.2586 | **+6.007** | **1.88e-09** | *** |
| Education: graduate level (vs college) | -3.9306 | 2.9297 | ±5.8594 | -1.342 | 0.1797 |  |
| Education: high school or below (vs college) | -2.3996 | 3.4848 | ±6.9697 | -0.689 | 0.4911 |  |
| Site: UCSD (vs UAB) | +3.6876 | 3.3808 | ±6.7615 | +1.091 | 0.2754 |  |
| Site: UW (vs UAB) | +2.4097 | 3.3217 | ±6.6433 | +0.725 | 0.4682 |  |
| **Age (years)** | **-0.3567** | 0.1243 | ±0.2486 | **-2.870** | **0.0041** | ** |
| BMI (kg/m2) | +0.3292 | 0.1783 | ±0.3566 | +1.846 | 0.0649 | . |
| Hypertension | +1.7123 | 3.0908 | ±6.1815 | +0.554 | 0.5796 |  |
| High cholesterol | +1.0223 | 2.5848 | ±5.1696 | +0.395 | 0.6925 |  |
| Kidney disease | -1.8723 | 4.1608 | ±8.3215 | -0.450 | 0.6527 |  |
| **Circulatory disease** | **-6.5119** | 3.1360 | ±6.2719 | **-2.077** | **0.0378** | * |
| Time > 180 (%) | +0.0659 | 0.0713 | ±0.1425 | +0.924 | 0.3554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **203**, R² = **0.1406**, Adj R² = **0.0911**, F-statistic = **2.84** (p = **0.0018**), Residual SE = **17.183** on **191** df, AIC = **1742.3**, BIC = **1782.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.7042** | 11.1470 | ±22.2941 | **+5.984** | **2.18e-09** | *** |
| Education: graduate level (vs college) | -3.9094 | 2.9313 | ±5.8627 | -1.334 | 0.1823 |  |
| Education: high school or below (vs college) | -2.4553 | 3.4768 | ±6.9537 | -0.706 | 0.4801 |  |
| Site: UCSD (vs UAB) | +3.7019 | 3.3795 | ±6.7590 | +1.095 | 0.2733 |  |
| Site: UW (vs UAB) | +2.4351 | 3.3249 | ±6.6497 | +0.732 | 0.4639 |  |
| **Age (years)** | **-0.3563** | 0.1242 | ±0.2484 | **-2.868** | **0.0041** | ** |
| BMI (kg/m2) | +0.3310 | 0.1785 | ±0.3569 | +1.855 | 0.0636 | . |
| Hypertension | +1.7346 | 3.0915 | ±6.1830 | +0.561 | 0.5747 |  |
| High cholesterol | +1.0031 | 2.5823 | ±5.1647 | +0.388 | 0.6977 |  |
| Kidney disease | -1.9221 | 4.1547 | ±8.3094 | -0.463 | 0.6436 |  |
| **Circulatory disease** | **-6.5330** | 3.1382 | ±6.2763 | **-2.082** | **0.0374** | * |
| Avg. daily time > 180 (%) | +0.0716 | 0.0701 | ±0.1403 | +1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **203**, R² = **0.1376**, Adj R² = **0.0880**, F-statistic = **2.77** (p = **0.0023**), Residual SE = **17.212** on **191** df, AIC = **1743.0**, BIC = **1782.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1519** | 11.1491 | ±22.2983 | **+6.023** | **1.71e-09** | *** |
| Education: graduate level (vs college) | -4.0704 | 2.9136 | ±5.8273 | -1.397 | 0.1624 |  |
| Education: high school or below (vs college) | -2.2180 | 3.5108 | ±7.0217 | -0.632 | 0.5276 |  |
| Site: UCSD (vs UAB) | +3.6867 | 3.3873 | ±6.7746 | +1.088 | 0.2764 |  |
| Site: UW (vs UAB) | +2.3873 | 3.3197 | ±6.6395 | +0.719 | 0.4721 |  |
| **Age (years)** | **-0.3498** | 0.1247 | ±0.2493 | **-2.806** | **0.0050** | ** |
| BMI (kg/m2) | +0.3245 | 0.1785 | ±0.3569 | +1.818 | 0.0691 | . |
| Hypertension | +1.5665 | 3.1018 | ±6.2037 | +0.505 | 0.6135 |  |
| High cholesterol | +1.0220 | 2.5807 | ±5.1614 | +0.396 | 0.6921 |  |
| Kidney disease | -1.5703 | 4.1710 | ±8.3420 | -0.376 | 0.7066 |  |
| **Circulatory disease** | **-6.5490** | 3.1402 | ±6.2804 | **-2.086** | **0.0370** | * |
| Nocturnal time > 180 (%) | +0.0472 | 0.0656 | ±0.1312 | +0.720 | 0.4716 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.1381**, Adj R² = **0.0884**, F-statistic = **2.78** (p = **0.0022**), Residual SE = **17.208** on **191** df, AIC = **1742.9**, BIC = **1782.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1631** | 11.1244 | ±22.2488 | **+6.037** | **1.57e-09** | *** |
| Education: graduate level (vs college) | -3.9317 | 2.9628 | ±5.9256 | -1.327 | 0.1845 |  |
| Education: high school or below (vs college) | -2.2860 | 3.5171 | ±7.0342 | -0.650 | 0.5157 |  |
| Site: UCSD (vs UAB) | +3.6441 | 3.3858 | ±6.7717 | +1.076 | 0.2818 |  |
| Site: UW (vs UAB) | +2.0716 | 3.3162 | ±6.6325 | +0.625 | 0.5322 |  |
| **Age (years)** | **-0.3673** | 0.1267 | ±0.2533 | **-2.900** | **0.0037** | ** |
| BMI (kg/m2) | +0.3381 | 0.1797 | ±0.3595 | +1.881 | 0.0599 | . |
| Hypertension | +1.6858 | 3.0939 | ±6.1879 | +0.545 | 0.5858 |  |
| High cholesterol | +1.0372 | 2.5789 | ±5.1579 | +0.402 | 0.6875 |  |
| Kidney disease | -1.8838 | 4.2710 | ±8.5420 | -0.441 | 0.6592 |  |
| **Circulatory disease** | **-6.3869** | 3.1290 | ±6.2581 | **-2.041** | **0.0412** | * |
| Any reading > 250 during wear (0/1) | +2.0349 | 2.6747 | ±5.3495 | +0.761 | 0.4468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5940** | 11.1018 | ±22.2036 | **+6.089** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -4.2328 | 2.9006 | ±5.8012 | -1.459 | 0.1445 |  |
| Education: high school or below (vs college) | -2.1214 | 3.6049 | ±7.2099 | -0.588 | 0.5562 |  |
| Site: UCSD (vs UAB) | +3.7149 | 3.3920 | ±6.7839 | +1.095 | 0.2734 |  |
| Site: UW (vs UAB) | +2.3111 | 3.3428 | ±6.6856 | +0.691 | 0.4893 |  |
| **Age (years)** | **-0.3505** | 0.1251 | ±0.2503 | **-2.801** | **0.0051** | ** |
| BMI (kg/m2) | +0.3239 | 0.1789 | ±0.3578 | +1.810 | 0.0702 | . |
| Hypertension | +1.6334 | 3.0994 | ±6.1989 | +0.527 | 0.5982 |  |
| High cholesterol | +1.1142 | 2.5813 | ±5.1626 | +0.432 | 0.6660 |  |
| Kidney disease | -1.4053 | 4.2321 | ±8.4642 | -0.332 | 0.7399 |  |
| **Circulatory disease** | **-6.4075** | 3.1426 | ±6.2853 | **-2.039** | **0.0415** | * |
| Time > 250 (%) | +0.0056 | 0.1658 | ±0.3317 | +0.034 | 0.9729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.1357**, Adj R² = **0.0859**, F-statistic = **2.73** (p = **0.0027**), Residual SE = **17.232** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.3602** | 11.0966 | ±22.1931 | **+6.070** | **1.28e-09** | *** |
| Education: graduate level (vs college) | -4.1701 | 2.9012 | ±5.8024 | -1.437 | 0.1506 |  |
| Education: high school or below (vs college) | -2.2474 | 3.6107 | ±7.2214 | -0.622 | 0.5337 |  |
| Site: UCSD (vs UAB) | +3.7061 | 3.3985 | ±6.7971 | +1.091 | 0.2755 |  |
| Site: UW (vs UAB) | +2.3722 | 3.3397 | ±6.6794 | +0.710 | 0.4775 |  |
| **Age (years)** | **-0.3500** | 0.1249 | ±0.2498 | **-2.802** | **0.0051** | ** |
| BMI (kg/m2) | +0.3262 | 0.1786 | ±0.3573 | +1.826 | 0.0678 | . |
| Hypertension | +1.6146 | 3.0936 | ±6.1871 | +0.522 | 0.6017 |  |
| High cholesterol | +1.1486 | 2.5803 | ±5.1606 | +0.445 | 0.6562 |  |
| Kidney disease | -1.4897 | 4.2277 | ±8.4554 | -0.352 | 0.7246 |  |
| **Circulatory disease** | **-6.4591** | 3.1518 | ±6.3036 | **-2.049** | **0.0404** | * |
| Avg. daily time > 250 (%) | +0.0456 | 0.1926 | ±0.3852 | +0.237 | 0.8130 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
