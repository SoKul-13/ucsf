# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Total analysis base - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 637; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **637**, R² = **0.1291**, Adj R² = **0.1152**, F-statistic = **9.28** (p = **2.00e-14**), Residual SE = **4.764** on **626** df, AIC = **3807.6**, BIC = **3856.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9321** | 1.5439 | ±3.0878 | **+4.490** | **7.12e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0471** | 0.4155 | ±0.8310 | **-2.520** | **0.0117** | * |
| **Education: high school or below (vs college)** | **+1.9717** | 0.7852 | ±1.5704 | **+2.511** | **0.0120** | * |
| Site: UCSD (vs UAB) | +0.8842 | 0.5240 | ±1.0481 | +1.687 | 0.0915 | . |
| Site: UW (vs UAB) | +0.2743 | 0.4492 | ±0.8983 | +0.611 | 0.5414 |  |
| **Age (years)** | **-0.0833** | 0.0174 | ±0.0349 | **-4.776** | **1.78e-06** | *** |
| **BMI (kg/m2)** | **+0.1139** | 0.0307 | ±0.0614 | **+3.710** | **2.08e-04** | *** |
| Hypertension | -0.1794 | 0.4472 | ±0.8943 | -0.401 | 0.6883 |  |
| High cholesterol | +0.6767 | 0.4052 | ±0.8103 | +1.670 | 0.0949 | . |
| Kidney disease | +1.0988 | 0.7130 | ±1.4261 | +1.541 | 0.1233 |  |
| Circulatory disease | +0.5826 | 0.5308 | ±1.0616 | +1.098 | 0.2723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **637**, R² = **0.1335**, Adj R² = **0.1183**, F-statistic = **8.76** (p = **1.51e-14**), Residual SE = **4.756** on **625** df, AIC = **3806.3**, BIC = **3859.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.8402** | 1.9808 | ±3.9616 | **+2.444** | **0.0145** | * |
| **Education: graduate level (vs college)** | **-0.9937** | 0.4145 | ±0.8290 | **-2.397** | **0.0165** | * |
| **Education: high school or below (vs college)** | **+1.8454** | 0.7823 | ±1.5647 | **+2.359** | **0.0183** | * |
| Site: UCSD (vs UAB) | +0.8563 | 0.5198 | ±1.0396 | +1.647 | 0.0995 | . |
| Site: UW (vs UAB) | +0.3296 | 0.4507 | ±0.9015 | +0.731 | 0.4646 |  |
| **Age (years)** | **-0.0871** | 0.0178 | ±0.0356 | **-4.891** | **1.00e-06** | *** |
| **BMI (kg/m2)** | **+0.1098** | 0.0308 | ±0.0617 | **+3.561** | **3.70e-04** | *** |
| Hypertension | -0.2649 | 0.4498 | ±0.8996 | -0.589 | 0.5559 |  |
| High cholesterol | +0.6312 | 0.4038 | ±0.8075 | +1.563 | 0.1180 |  |
| Kidney disease | +1.0387 | 0.7158 | ±1.4316 | +1.451 | 0.1468 |  |
| Circulatory disease | +0.5925 | 0.5281 | ±1.0561 | +1.122 | 0.2619 |  |
| HbA1c (%) | +0.4211 | 0.2584 | ±0.5167 | +1.630 | 0.1031 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **637**, R² = **0.1342**, Adj R² = **0.1189**, F-statistic = **8.81** (p = **1.22e-14**), Residual SE = **4.754** on **625** df, AIC = **3805.9**, BIC = **3859.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.2726** | 1.7575 | ±3.5150 | **+3.000** | **0.0027** | ** |
| **Education: graduate level (vs college)** | **-1.0481** | 0.4150 | ±0.8301 | **-2.525** | **0.0116** | * |
| **Education: high school or below (vs college)** | **+1.8439** | 0.7856 | ±1.5711 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | +0.8758 | 0.5214 | ±1.0429 | +1.680 | 0.0930 | . |
| Site: UW (vs UAB) | +0.2947 | 0.4497 | ±0.8994 | +0.655 | 0.5123 |  |
| **Age (years)** | **-0.0841** | 0.0175 | ±0.0351 | **-4.795** | **1.63e-06** | *** |
| **BMI (kg/m2)** | **+0.1113** | 0.0308 | ±0.0616 | **+3.614** | **3.02e-04** | *** |
| Hypertension | -0.2894 | 0.4525 | ±0.9051 | -0.640 | 0.5225 |  |
| High cholesterol | +0.6280 | 0.4021 | ±0.8042 | +1.562 | 0.1183 |  |
| Kidney disease | +0.9594 | 0.7236 | ±1.4471 | +1.326 | 0.1849 |  |
| Circulatory disease | +0.5671 | 0.5297 | ±1.0595 | +1.071 | 0.2844 |  |
| Mean glucose (mg/dL) | +0.0154 | 0.0085 | ±0.0170 | +1.820 | 0.0687 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **637**, R² = **0.1342**, Adj R² = **0.1189**, F-statistic = **8.81** (p = **1.22e-14**), Residual SE = **4.754** on **625** df, AIC = **3805.9**, BIC = **3859.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.1359 | 2.5381 | ±5.0761 | +1.236 | 0.2166 |  |
| **Education: graduate level (vs college)** | **-1.0481** | 0.4150 | ±0.8301 | **-2.525** | **0.0116** | * |
| **Education: high school or below (vs college)** | **+1.8439** | 0.7856 | ±1.5711 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | +0.8758 | 0.5214 | ±1.0429 | +1.680 | 0.0930 | . |
| Site: UW (vs UAB) | +0.2947 | 0.4497 | ±0.8994 | +0.655 | 0.5123 |  |
| **Age (years)** | **-0.0841** | 0.0175 | ±0.0351 | **-4.795** | **1.63e-06** | *** |
| **BMI (kg/m2)** | **+0.1113** | 0.0308 | ±0.0616 | **+3.614** | **3.02e-04** | *** |
| Hypertension | -0.2894 | 0.4525 | ±0.9051 | -0.640 | 0.5225 |  |
| High cholesterol | +0.6280 | 0.4021 | ±0.8042 | +1.562 | 0.1183 |  |
| Kidney disease | +0.9594 | 0.7236 | ±1.4471 | +1.326 | 0.1849 |  |
| Circulatory disease | +0.5671 | 0.5297 | ±1.0595 | +1.071 | 0.2844 |  |
| GMI (%) | +0.6455 | 0.3547 | ±0.7093 | +1.820 | 0.0687 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **637**, R² = **0.1383**, Adj R² = **0.1231**, F-statistic = **9.12** (p = **3.15e-15**), Residual SE = **4.743** on **625** df, AIC = **3802.8**, BIC = **3856.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.6962** | 1.7548 | ±3.5096 | **+2.676** | **0.0074** | ** |
| **Education: graduate level (vs college)** | **-1.0610** | 0.4141 | ±0.8282 | **-2.562** | **0.0104** | * |
| **Education: high school or below (vs college)** | **+1.8088** | 0.7805 | ±1.5610 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +0.8648 | 0.5185 | ±1.0369 | +1.668 | 0.0953 | . |
| Site: UW (vs UAB) | +0.2913 | 0.4493 | ±0.8985 | +0.648 | 0.5167 |  |
| **Age (years)** | **-0.0818** | 0.0175 | ±0.0350 | **-4.672** | **2.98e-06** | *** |
| **BMI (kg/m2)** | **+0.1074** | 0.0309 | ±0.0617 | **+3.483** | **4.97e-04** | *** |
| Hypertension | -0.3168 | 0.4499 | ±0.8997 | -0.704 | 0.4814 |  |
| High cholesterol | +0.5869 | 0.3997 | ±0.7995 | +1.468 | 0.1421 |  |
| Kidney disease | +1.0420 | 0.7221 | ±1.4443 | +1.443 | 0.1490 |  |
| Circulatory disease | +0.5773 | 0.5280 | ±1.0560 | +1.093 | 0.2742 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0208** | 0.0082 | ±0.0164 | **+2.530** | **0.0114** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **637**, R² = **0.1393**, Adj R² = **0.1242**, F-statistic = **9.20** (p = **2.25e-15**), Residual SE = **4.740** on **625** df, AIC = **3802.1**, BIC = **3855.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.1946** | 1.5640 | ±3.1281 | **+3.961** | **7.48e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0126** | 0.4130 | ±0.8260 | **-2.452** | **0.0142** | * |
| **Education: high school or below (vs college)** | **+1.7273** | 0.7817 | ±1.5635 | **+2.210** | **0.0271** | * |
| Site: UCSD (vs UAB) | +0.8773 | 0.5197 | ±1.0394 | +1.688 | 0.0914 | . |
| Site: UW (vs UAB) | +0.3687 | 0.4473 | ±0.8947 | +0.824 | 0.4099 |  |
| **Age (years)** | **-0.0890** | 0.0176 | ±0.0352 | **-5.053** | **4.36e-07** | *** |
| **BMI (kg/m2)** | **+0.1132** | 0.0308 | ±0.0616 | **+3.675** | **2.38e-04** | *** |
| Hypertension | -0.3267 | 0.4496 | ±0.8992 | -0.727 | 0.4675 |  |
| High cholesterol | +0.6684 | 0.4010 | ±0.8020 | +1.667 | 0.0956 | . |
| Kidney disease | +0.7122 | 0.7329 | ±1.4658 | +0.972 | 0.3312 |  |
| Circulatory disease | +0.6036 | 0.5286 | ±1.0572 | +1.142 | 0.2535 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0453** | 0.0165 | ±0.0330 | **+2.746** | **0.0060** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **637**, R² = **0.1374**, Adj R² = **0.1222**, F-statistic = **9.05** (p = **4.29e-15**), Residual SE = **4.746** on **625** df, AIC = **3803.5**, BIC = **3857.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.2627** | 1.5636 | ±3.1272 | **+4.005** | **6.19e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0093** | 0.4136 | ±0.8272 | **-2.440** | **0.0147** | * |
| **Education: high school or below (vs college)** | **+1.7218** | 0.7855 | ±1.5709 | **+2.192** | **0.0284** | * |
| Site: UCSD (vs UAB) | +0.8685 | 0.5214 | ±1.0428 | +1.666 | 0.0958 | . |
| Site: UW (vs UAB) | +0.3469 | 0.4476 | ±0.8951 | +0.775 | 0.4383 |  |
| **Age (years)** | **-0.0890** | 0.0176 | ±0.0352 | **-5.054** | **4.32e-07** | *** |
| **BMI (kg/m2)** | **+0.1135** | 0.0307 | ±0.0615 | **+3.693** | **2.22e-04** | *** |
| Hypertension | -0.3010 | 0.4503 | ±0.9006 | -0.668 | 0.5038 |  |
| High cholesterol | +0.6607 | 0.4016 | ±0.8032 | +1.645 | 0.0999 | . |
| Kidney disease | +0.7365 | 0.7388 | ±1.4777 | +0.997 | 0.3188 |  |
| Circulatory disease | +0.6148 | 0.5294 | ±1.0588 | +1.161 | 0.2455 |  |
| **Avg. daily SD (mg/dL)** | **+0.0473** | 0.0189 | ±0.0378 | **+2.507** | **0.0122** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **637**, R² = **0.1355**, Adj R² = **0.1202**, F-statistic = **8.90** (p = **8.04e-15**), Residual SE = **4.751** on **625** df, AIC = **3804.9**, BIC = **3858.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.8575** | 1.6236 | ±3.2473 | **+3.608** | **3.09e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0153** | 0.4135 | ±0.8270 | **-2.455** | **0.0141** | * |
| **Education: high school or below (vs college)** | **+1.8049** | 0.7824 | ±1.5648 | **+2.307** | **0.0211** | * |
| Site: UCSD (vs UAB) | +0.8741 | 0.5222 | ±1.0444 | +1.674 | 0.0941 | . |
| Site: UW (vs UAB) | +0.3623 | 0.4455 | ±0.8911 | +0.813 | 0.4161 |  |
| **Age (years)** | **-0.0900** | 0.0177 | ±0.0353 | **-5.093** | **3.53e-07** | *** |
| **BMI (kg/m2)** | **+0.1146** | 0.0308 | ±0.0617 | **+3.715** | **2.03e-04** | *** |
| Hypertension | -0.2636 | 0.4483 | ±0.8965 | -0.588 | 0.5565 |  |
| High cholesterol | +0.7019 | 0.4036 | ±0.8072 | +1.739 | 0.0820 | . |
| Kidney disease | +0.7710 | 0.7333 | ±1.4667 | +1.051 | 0.2931 |  |
| Circulatory disease | +0.6087 | 0.5314 | ±1.0628 | +1.146 | 0.2520 |  |
| **CV (%)** | **+0.0708** | 0.0321 | ±0.0643 | **+2.201** | **0.0277** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **637**, R² = **0.1363**, Adj R² = **0.1211**, F-statistic = **8.97** (p = **6.11e-15**), Residual SE = **4.749** on **625** df, AIC = **3804.3**, BIC = **3857.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2467** | 1.7980 | ±3.5959 | **+5.143** | **2.71e-07** | *** |
| **Education: graduate level (vs college)** | **-1.0383** | 0.4130 | ±0.8260 | **-2.514** | **0.0119** | * |
| **Education: high school or below (vs college)** | **+1.7967** | 0.7801 | ±1.5602 | **+2.303** | **0.0213** | * |
| Site: UCSD (vs UAB) | +0.8464 | 0.5231 | ±1.0463 | +1.618 | 0.1057 |  |
| Site: UW (vs UAB) | +0.3290 | 0.4465 | ±0.8929 | +0.737 | 0.4612 |  |
| **Age (years)** | **-0.0908** | 0.0176 | ±0.0352 | **-5.167** | **2.38e-07** | *** |
| **BMI (kg/m2)** | **+0.1131** | 0.0306 | ±0.0613 | **+3.692** | **2.22e-04** | *** |
| Hypertension | -0.2555 | 0.4488 | ±0.8975 | -0.569 | 0.5691 |  |
| High cholesterol | +0.6994 | 0.4031 | ±0.8061 | +1.735 | 0.0827 | . |
| Kidney disease | +0.8362 | 0.7319 | ±1.4637 | +1.143 | 0.2532 |  |
| Circulatory disease | +0.5782 | 0.5314 | ±1.0629 | +1.088 | 0.2766 |  |
| **Mean / SD ratio** | **-0.3484** | 0.1484 | ±0.2967 | **-2.349** | **0.0188** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **637**, R² = **0.1325**, Adj R² = **0.1172**, F-statistic = **8.68** (p = **2.11e-14**), Residual SE = **4.759** on **625** df, AIC = **3807.1**, BIC = **3860.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5106** | 1.7960 | ±3.5921 | **+4.739** | **2.15e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0364** | 0.4146 | ±0.8292 | **-2.500** | **0.0124** | * |
| **Education: high school or below (vs college)** | **+1.8354** | 0.7838 | ±1.5677 | **+2.342** | **0.0192** | * |
| Site: UCSD (vs UAB) | +0.8390 | 0.5273 | ±1.0547 | +1.591 | 0.1116 |  |
| Site: UW (vs UAB) | +0.2995 | 0.4475 | ±0.8950 | +0.669 | 0.5034 |  |
| **Age (years)** | **-0.0889** | 0.0176 | ±0.0351 | **-5.059** | **4.21e-07** | *** |
| **BMI (kg/m2)** | **+0.1131** | 0.0306 | ±0.0612 | **+3.696** | **2.19e-04** | *** |
| Hypertension | -0.2142 | 0.4497 | ±0.8994 | -0.476 | 0.6339 |  |
| High cholesterol | +0.6825 | 0.4042 | ±0.8084 | +1.689 | 0.0913 | . |
| Kidney disease | +0.9313 | 0.7314 | ±1.4628 | +1.273 | 0.2029 |  |
| Circulatory disease | +0.5906 | 0.5311 | ±1.0622 | +1.112 | 0.2661 |  |
| Avg. daily mean/SD | -0.1960 | 0.1226 | ±0.2452 | -1.599 | 0.1098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **637**, R² = **0.1310**, Adj R² = **0.1157**, F-statistic = **8.56** (p = **3.49e-14**), Residual SE = **4.763** on **625** df, AIC = **3808.2**, BIC = **3861.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.0075** | 1.6905 | ±3.3810 | **+3.554** | **3.80e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0389** | 0.4149 | ±0.8299 | **-2.504** | **0.0123** | * |
| **Education: high school or below (vs college)** | **+1.8913** | 0.7873 | ±1.5746 | **+2.402** | **0.0163** | * |
| Site: UCSD (vs UAB) | +0.8589 | 0.5258 | ±1.0516 | +1.634 | 0.1023 |  |
| Site: UW (vs UAB) | +0.3324 | 0.4524 | ±0.9048 | +0.735 | 0.4625 |  |
| **Age (years)** | **-0.0834** | 0.0174 | ±0.0349 | **-4.780** | **1.75e-06** | *** |
| **BMI (kg/m2)** | **+0.1123** | 0.0311 | ±0.0622 | **+3.610** | **3.06e-04** | *** |
| Hypertension | -0.2032 | 0.4481 | ±0.8963 | -0.453 | 0.6503 |  |
| High cholesterol | +0.6914 | 0.4064 | ±0.8128 | +1.701 | 0.0889 | . |
| Kidney disease | +1.0716 | 0.7163 | ±1.4326 | +1.496 | 0.1347 |  |
| Circulatory disease | +0.5869 | 0.5310 | ±1.0620 | +1.105 | 0.2691 |  |
| MAG (mg/dL/h) | +0.0234 | 0.0217 | ±0.0434 | +1.080 | 0.2802 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **637**, R² = **0.1356**, Adj R² = **0.1204**, F-statistic = **8.91** (p = **7.71e-15**), Residual SE = **4.751** on **625** df, AIC = **3804.8**, BIC = **3858.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9710** | 1.5985 | ±3.1971 | **+3.735** | **1.88e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0103** | 0.4142 | ±0.8284 | **-2.439** | **0.0147** | * |
| **Education: high school or below (vs college)** | **+1.7492** | 0.7859 | ±1.5719 | **+2.226** | **0.0260** | * |
| Site: UCSD (vs UAB) | +0.8663 | 0.5224 | ±1.0448 | +1.658 | 0.0973 | . |
| Site: UW (vs UAB) | +0.3339 | 0.4476 | ±0.8952 | +0.746 | 0.4556 |  |
| **Age (years)** | **-0.0879** | 0.0175 | ±0.0351 | **-5.010** | **5.45e-07** | *** |
| **BMI (kg/m2)** | **+0.1155** | 0.0307 | ±0.0615 | **+3.759** | **1.70e-04** | *** |
| Hypertension | -0.2675 | 0.4500 | ±0.8999 | -0.594 | 0.5522 |  |
| High cholesterol | +0.6685 | 0.4026 | ±0.8053 | +1.660 | 0.0969 | . |
| Kidney disease | +0.8026 | 0.7373 | ±1.4747 | +1.089 | 0.2763 |  |
| Circulatory disease | +0.5881 | 0.5307 | ±1.0614 | +1.108 | 0.2678 |  |
| **Avg. daily range (mg/dL)** | **+0.0111** | 0.0051 | ±0.0103 | **+2.147** | **0.0318** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **637**, R² = **0.1421**, Adj R² = **0.1270**, F-statistic = **9.41** (p = **8.93e-16**), Residual SE = **4.733** on **625** df, AIC = **3800.0**, BIC = **3853.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4232** | 1.5516 | ±3.1033 | **+4.140** | **3.48e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0190** | 0.4128 | ±0.8256 | **-2.468** | **0.0136** | * |
| **Education: high school or below (vs college)** | **+1.8885** | 0.7702 | ±1.5403 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | +0.9083 | 0.5154 | ±1.0307 | +1.763 | 0.0780 | . |
| Site: UW (vs UAB) | +0.3680 | 0.4461 | ±0.8922 | +0.825 | 0.4095 |  |
| **Age (years)** | **-0.0857** | 0.0177 | ±0.0354 | **-4.851** | **1.23e-06** | *** |
| **BMI (kg/m2)** | **+0.1120** | 0.0308 | ±0.0617 | **+3.631** | **2.82e-04** | *** |
| Hypertension | -0.3284 | 0.4462 | ±0.8925 | -0.736 | 0.4618 |  |
| High cholesterol | +0.6704 | 0.4009 | ±0.8017 | +1.672 | 0.0944 | . |
| Kidney disease | +0.8390 | 0.7153 | ±1.4306 | +1.173 | 0.2408 |  |
| Circulatory disease | +0.5273 | 0.5281 | ±1.0563 | +0.998 | 0.3181 |  |
| **SD of daily means (mg/dL)** | **+0.0855** | 0.0286 | ±0.0572 | **+2.990** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **637**, R² = **0.1399**, Adj R² = **0.1247**, F-statistic = **9.24** (p = **1.86e-15**), Residual SE = **4.739** on **625** df, AIC = **3801.7**, BIC = **3855.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.0144** | 2.1280 | ±4.2561 | **+5.176** | **2.27e-07** | *** |
| **Education: graduate level (vs college)** | **-0.9937** | 0.4128 | ±0.8256 | **-2.407** | **0.0161** | * |
| **Education: high school or below (vs college)** | **+1.8086** | 0.7803 | ±1.5605 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +0.9220 | 0.5179 | ±1.0359 | +1.780 | 0.0751 | . |
| Site: UW (vs UAB) | +0.3930 | 0.4477 | ±0.8953 | +0.878 | 0.3800 |  |
| **Age (years)** | **-0.0855** | 0.0176 | ±0.0351 | **-4.868** | **1.13e-06** | *** |
| **BMI (kg/m2)** | **+0.1126** | 0.0308 | ±0.0616 | **+3.659** | **2.53e-04** | *** |
| Hypertension | -0.2897 | 0.4462 | ±0.8924 | -0.649 | 0.5162 |  |
| High cholesterol | +0.6334 | 0.3999 | ±0.7998 | +1.584 | 0.1132 |  |
| Kidney disease | +0.8017 | 0.7287 | ±1.4574 | +1.100 | 0.2713 |  |
| Circulatory disease | +0.5632 | 0.5285 | ±1.0570 | +1.066 | 0.2866 |  |
| **Time in range 70-180, pooled (%)** | **-0.0423** | 0.0144 | ±0.0289 | **-2.927** | **0.0034** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **637**, R² = **0.1407**, Adj R² = **0.1256**, F-statistic = **9.30** (p = **1.42e-15**), Residual SE = **4.736** on **625** df, AIC = **3801.1**, BIC = **3854.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1746** | 2.1409 | ±4.2818 | **+5.220** | **1.79e-07** | *** |
| **Education: graduate level (vs college)** | **-0.9898** | 0.4126 | ±0.8251 | **-2.399** | **0.0164** | * |
| **Education: high school or below (vs college)** | **+1.7956** | 0.7789 | ±1.5578 | **+2.305** | **0.0212** | * |
| Site: UCSD (vs UAB) | +0.9218 | 0.5175 | ±1.0350 | +1.781 | 0.0749 | . |
| Site: UW (vs UAB) | +0.3997 | 0.4474 | ±0.8947 | +0.894 | 0.3716 |  |
| **Age (years)** | **-0.0858** | 0.0176 | ±0.0351 | **-4.887** | **1.03e-06** | *** |
| **BMI (kg/m2)** | **+0.1126** | 0.0308 | ±0.0616 | **+3.657** | **2.55e-04** | *** |
| Hypertension | -0.2898 | 0.4459 | ±0.8919 | -0.650 | 0.5158 |  |
| High cholesterol | +0.6274 | 0.3997 | ±0.7994 | +1.570 | 0.1165 |  |
| Kidney disease | +0.7849 | 0.7285 | ±1.4571 | +1.077 | 0.2813 |  |
| Circulatory disease | +0.5631 | 0.5282 | ±1.0564 | +1.066 | 0.2864 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0436** | 0.0145 | ±0.0290 | **-3.007** | **0.0026** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **637**, R² = **0.1297**, Adj R² = **0.1144**, F-statistic = **8.47** (p = **5.30e-14**), Residual SE = **4.767** on **625** df, AIC = **3809.2**, BIC = **3862.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.0328** | 1.5613 | ±3.1226 | **+4.505** | **6.65e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0520** | 0.4161 | ±0.8321 | **-2.529** | **0.0115** | * |
| **Education: high school or below (vs college)** | **+1.9505** | 0.7880 | ±1.5759 | **+2.475** | **0.0133** | * |
| Site: UCSD (vs UAB) | +0.8396 | 0.5301 | ±1.0602 | +1.584 | 0.1132 |  |
| Site: UW (vs UAB) | +0.2376 | 0.4536 | ±0.9072 | +0.524 | 0.6003 |  |
| **Age (years)** | **-0.0831** | 0.0174 | ±0.0349 | **-4.765** | **1.89e-06** | *** |
| **BMI (kg/m2)** | **+0.1135** | 0.0307 | ±0.0615 | **+3.692** | **2.23e-04** | *** |
| Hypertension | -0.1904 | 0.4485 | ±0.8971 | -0.425 | 0.6711 |  |
| High cholesterol | +0.6594 | 0.4063 | ±0.8125 | +1.623 | 0.1046 |  |
| Kidney disease | +1.1022 | 0.7119 | ±1.4238 | +1.548 | 0.1216 |  |
| Circulatory disease | +0.5862 | 0.5308 | ±1.0615 | +1.105 | 0.2694 |  |
| Time < 54 (%) | -0.1378 | 0.1948 | ±0.3897 | -0.707 | 0.4795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **637**, R² = **0.1292**, Adj R² = **0.1139**, F-statistic = **8.43** (p = **6.23e-14**), Residual SE = **4.768** on **625** df, AIC = **3809.5**, BIC = **3863.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9475** | 1.5527 | ±3.1054 | **+4.474** | **7.66e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0503** | 0.4165 | ±0.8330 | **-2.522** | **0.0117** | * |
| **Education: high school or below (vs college)** | **+1.9657** | 0.7890 | ±1.5779 | **+2.492** | **0.0127** | * |
| Site: UCSD (vs UAB) | +0.8737 | 0.5265 | ±1.0531 | +1.659 | 0.0970 | . |
| Site: UW (vs UAB) | +0.2629 | 0.4524 | ±0.9047 | +0.581 | 0.5612 |  |
| **Age (years)** | **-0.0831** | 0.0175 | ±0.0350 | **-4.750** | **2.03e-06** | *** |
| **BMI (kg/m2)** | **+0.1138** | 0.0308 | ±0.0615 | **+3.698** | **2.17e-04** | *** |
| Hypertension | -0.1827 | 0.4495 | ±0.8990 | -0.406 | 0.6844 |  |
| High cholesterol | +0.6719 | 0.4055 | ±0.8109 | +1.657 | 0.0975 | . |
| Kidney disease | +1.1013 | 0.7137 | ±1.4274 | +1.543 | 0.1228 |  |
| Circulatory disease | +0.5843 | 0.5323 | ±1.0645 | +1.098 | 0.2723 |  |
| Avg. daily time < 54 (%) | -0.0446 | 0.2502 | ±0.5004 | -0.178 | 0.8585 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **637**, R² = **0.1298**, Adj R² = **0.1145**, F-statistic = **8.48** (p = **5.06e-14**), Residual SE = **4.766** on **625** df, AIC = **3809.1**, BIC = **3862.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8423** | 1.5523 | ±3.1046 | **+4.408** | **1.04e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0299** | 0.4161 | ±0.8322 | **-2.475** | **0.0133** | * |
| **Education: high school or below (vs college)** | **+1.9751** | 0.7858 | ±1.5717 | **+2.513** | **0.0120** | * |
| Site: UCSD (vs UAB) | +0.9097 | 0.5224 | ±1.0448 | +1.741 | 0.0816 | . |
| Site: UW (vs UAB) | +0.3050 | 0.4469 | ±0.8939 | +0.682 | 0.4950 |  |
| **Age (years)** | **-0.0838** | 0.0174 | ±0.0349 | **-4.805** | **1.54e-06** | *** |
| **BMI (kg/m2)** | **+0.1138** | 0.0308 | ±0.0616 | **+3.697** | **2.18e-04** | *** |
| Hypertension | -0.1623 | 0.4488 | ±0.8976 | -0.362 | 0.7176 |  |
| High cholesterol | +0.6838 | 0.4057 | ±0.8114 | +1.685 | 0.0919 | . |
| Kidney disease | +1.0850 | 0.7139 | ±1.4278 | +1.520 | 0.1286 |  |
| Circulatory disease | +0.5887 | 0.5316 | ±1.0632 | +1.108 | 0.2681 |  |
| Time 54-69, pooled (%) | +0.0590 | 0.0821 | ±0.1642 | +0.719 | 0.4720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **637**, R² = **0.1304**, Adj R² = **0.1151**, F-statistic = **8.52** (p = **4.15e-14**), Residual SE = **4.765** on **625** df, AIC = **3808.6**, BIC = **3862.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8476** | 1.5487 | ±3.0974 | **+4.422** | **9.80e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0207** | 0.4161 | ±0.8322 | **-2.453** | **0.0142** | * |
| **Education: high school or below (vs college)** | **+1.9758** | 0.7858 | ±1.5716 | **+2.514** | **0.0119** | * |
| Site: UCSD (vs UAB) | +0.9130 | 0.5219 | ±1.0438 | +1.749 | 0.0802 | . |
| Site: UW (vs UAB) | +0.3200 | 0.4465 | ±0.8930 | +0.717 | 0.4736 |  |
| **Age (years)** | **-0.0844** | 0.0175 | ±0.0349 | **-4.831** | **1.36e-06** | *** |
| **BMI (kg/m2)** | **+0.1136** | 0.0308 | ±0.0615 | **+3.693** | **2.21e-04** | *** |
| Hypertension | -0.1567 | 0.4486 | ±0.8973 | -0.349 | 0.7269 |  |
| High cholesterol | +0.6856 | 0.4054 | ±0.8108 | +1.691 | 0.0908 | . |
| Kidney disease | +1.0820 | 0.7126 | ±1.4251 | +1.518 | 0.1289 |  |
| Circulatory disease | +0.5915 | 0.5318 | ±1.0635 | +1.112 | 0.2660 |  |
| Avg. daily time 54-69 (%) | +0.0783 | 0.0804 | ±0.1607 | +0.974 | 0.3301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **637**, R² = **0.1293**, Adj R² = **0.1140**, F-statistic = **8.44** (p = **5.93e-14**), Residual SE = **4.768** on **625** df, AIC = **3809.4**, BIC = **3862.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8744** | 1.5572 | ±3.1144 | **+4.415** | **1.01e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0387** | 0.4165 | ±0.8330 | **-2.494** | **0.0126** | * |
| **Education: high school or below (vs college)** | **+1.9771** | 0.7860 | ±1.5719 | **+2.515** | **0.0119** | * |
| Site: UCSD (vs UAB) | +0.9036 | 0.5240 | ±1.0480 | +1.724 | 0.0846 | . |
| Site: UW (vs UAB) | +0.2945 | 0.4485 | ±0.8971 | +0.656 | 0.5115 |  |
| **Age (years)** | **-0.0835** | 0.0174 | ±0.0349 | **-4.791** | **1.66e-06** | *** |
| **BMI (kg/m2)** | **+0.1139** | 0.0308 | ±0.0615 | **+3.701** | **2.14e-04** | *** |
| Hypertension | -0.1699 | 0.4492 | ±0.8984 | -0.378 | 0.7053 |  |
| High cholesterol | +0.6830 | 0.4061 | ±0.8123 | +1.682 | 0.0926 | . |
| Kidney disease | +1.0921 | 0.7148 | ±1.4297 | +1.528 | 0.1266 |  |
| Circulatory disease | +0.5846 | 0.5316 | ±1.0631 | +1.100 | 0.2714 |  |
| Time < 70 (%) | +0.0256 | 0.0653 | ±0.1306 | +0.393 | 0.6946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **637**, R² = **0.1299**, Adj R² = **0.1146**, F-statistic = **8.49** (p = **4.89e-14**), Residual SE = **4.766** on **625** df, AIC = **3809.0**, BIC = **3862.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8603** | 1.5503 | ±3.1006 | **+4.425** | **9.64e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0264** | 0.4165 | ±0.8329 | **-2.465** | **0.0137** | * |
| **Education: high school or below (vs college)** | **+1.9811** | 0.7858 | ±1.5717 | **+2.521** | **0.0117** | * |
| Site: UCSD (vs UAB) | +0.9146 | 0.5224 | ±1.0449 | +1.751 | 0.0800 | . |
| Site: UW (vs UAB) | +0.3167 | 0.4474 | ±0.8948 | +0.708 | 0.4790 |  |
| **Age (years)** | **-0.0842** | 0.0175 | ±0.0349 | **-4.819** | **1.44e-06** | *** |
| **BMI (kg/m2)** | **+0.1138** | 0.0308 | ±0.0615 | **+3.698** | **2.17e-04** | *** |
| Hypertension | -0.1610 | 0.4491 | ±0.8982 | -0.358 | 0.7200 |  |
| High cholesterol | +0.6879 | 0.4055 | ±0.8111 | +1.696 | 0.0899 | . |
| Kidney disease | +1.0851 | 0.7136 | ±1.4273 | +1.521 | 0.1284 |  |
| Circulatory disease | +0.5865 | 0.5320 | ±1.0641 | +1.102 | 0.2703 |  |
| Avg. daily time < 70 (%) | +0.0504 | 0.0659 | ±0.1318 | +0.765 | 0.4445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **637**, R² = **0.1431**, Adj R² = **0.1280**, F-statistic = **9.49** (p = **6.43e-16**), Residual SE = **4.730** on **625** df, AIC = **3799.3**, BIC = **3852.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3366** | 2.7708 | ±5.5417 | **+6.257** | **3.93e-10** | *** |
| **Education: graduate level (vs college)** | **-0.9902** | 0.4146 | ±0.8292 | **-2.388** | **0.0169** | * |
| **Education: high school or below (vs college)** | **+1.7965** | 0.7678 | ±1.5357 | **+2.340** | **0.0193** | * |
| Site: UCSD (vs UAB) | +0.9491 | 0.5166 | ±1.0333 | +1.837 | 0.0662 | . |
| Site: UW (vs UAB) | +0.4095 | 0.4495 | ±0.8989 | +0.911 | 0.3623 |  |
| **Age (years)** | **-0.0829** | 0.0174 | ±0.0349 | **-4.758** | **1.95e-06** | *** |
| **BMI (kg/m2)** | **+0.1147** | 0.0308 | ±0.0615 | **+3.729** | **1.92e-04** | *** |
| Hypertension | -0.2673 | 0.4437 | ±0.8875 | -0.602 | 0.5469 |  |
| High cholesterol | +0.7153 | 0.4002 | ±0.8005 | +1.787 | 0.0739 | . |
| Kidney disease | +0.9354 | 0.7178 | ±1.4356 | +1.303 | 0.1925 |  |
| Circulatory disease | +0.5379 | 0.5264 | ±1.0527 | +1.022 | 0.3068 |  |
| **Time 54-250, pooled (%)** | **-0.1065** | 0.0239 | ±0.0478 | **-4.458** | **8.28e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **637**, R² = **0.1431**, Adj R² = **0.1280**, F-statistic = **9.49** (p = **6.37e-16**), Residual SE = **4.730** on **625** df, AIC = **3799.3**, BIC = **3852.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.5038** | 3.3915 | ±6.7830 | **+5.456** | **4.87e-08** | *** |
| **Education: graduate level (vs college)** | **-0.9832** | 0.4146 | ±0.8292 | **-2.371** | **0.0177** | * |
| **Education: high school or below (vs college)** | **+1.7667** | 0.7677 | ±1.5354 | **+2.301** | **0.0214** | * |
| Site: UCSD (vs UAB) | +0.9370 | 0.5158 | ±1.0317 | +1.816 | 0.0693 | . |
| Site: UW (vs UAB) | +0.4043 | 0.4486 | ±0.8973 | +0.901 | 0.3675 |  |
| **Age (years)** | **-0.0837** | 0.0174 | ±0.0349 | **-4.800** | **1.59e-06** | *** |
| **BMI (kg/m2)** | **+0.1152** | 0.0307 | ±0.0615 | **+3.747** | **1.79e-04** | *** |
| Hypertension | -0.2686 | 0.4440 | ±0.8880 | -0.605 | 0.5452 |  |
| High cholesterol | +0.7089 | 0.4002 | ±0.8003 | +1.772 | 0.0765 | . |
| Kidney disease | +0.9039 | 0.7163 | ±1.4325 | +1.262 | 0.2070 |  |
| Circulatory disease | +0.5265 | 0.5270 | ±1.0541 | +0.999 | 0.3178 |  |
| **Avg. daily time 54-250 (%)** | **-0.1177** | 0.0308 | ±0.0616 | **-3.818** | **1.35e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **637**, R² = **0.1334**, Adj R² = **0.1182**, F-statistic = **8.75** (p = **1.56e-14**), Residual SE = **4.756** on **625** df, AIC = **3806.4**, BIC = **3859.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9487** | 1.5459 | ±3.0917 | **+4.495** | **6.96e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0302** | 0.4137 | ±0.8274 | **-2.490** | **0.0128** | * |
| **Education: high school or below (vs college)** | **+1.8843** | 0.7882 | ±1.5764 | **+2.391** | **0.0168** | * |
| Site: UCSD (vs UAB) | +0.8786 | 0.5226 | ±1.0453 | +1.681 | 0.0928 | . |
| Site: UW (vs UAB) | +0.3135 | 0.4485 | ±0.8970 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.0850** | 0.0176 | ±0.0351 | **-4.840** | **1.30e-06** | *** |
| **BMI (kg/m2)** | **+0.1125** | 0.0308 | ±0.0615 | **+3.656** | **2.56e-04** | *** |
| Hypertension | -0.2592 | 0.4486 | ±0.8972 | -0.578 | 0.5635 |  |
| High cholesterol | +0.6188 | 0.4032 | ±0.8064 | +1.535 | 0.1248 |  |
| Kidney disease | +0.8962 | 0.7307 | ±1.4615 | +1.226 | 0.2200 |  |
| Circulatory disease | +0.5771 | 0.5306 | ±1.0613 | +1.088 | 0.2768 |  |
| Time 181-250, pooled (%) | +0.0385 | 0.0225 | ±0.0450 | +1.711 | 0.0871 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **637**, R² = **0.1346**, Adj R² = **0.1194**, F-statistic = **8.84** (p = **1.06e-14**), Residual SE = **4.753** on **625** df, AIC = **3805.5**, BIC = **3859.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9346** | 1.5456 | ±3.0911 | **+4.487** | **7.23e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0288** | 0.4134 | ±0.8269 | **-2.488** | **0.0128** | * |
| **Education: high school or below (vs college)** | **+1.8726** | 0.7869 | ±1.5738 | **+2.380** | **0.0173** | * |
| Site: UCSD (vs UAB) | +0.8862 | 0.5221 | ±1.0442 | +1.697 | 0.0896 | . |
| Site: UW (vs UAB) | +0.3245 | 0.4484 | ±0.8968 | +0.724 | 0.4693 |  |
| **Age (years)** | **-0.0850** | 0.0176 | ±0.0351 | **-4.840** | **1.30e-06** | *** |
| **BMI (kg/m2)** | **+0.1122** | 0.0308 | ±0.0616 | **+3.646** | **2.66e-04** | *** |
| Hypertension | -0.2664 | 0.4480 | ±0.8960 | -0.595 | 0.5521 |  |
| High cholesterol | +0.6127 | 0.4027 | ±0.8054 | +1.521 | 0.1281 |  |
| Kidney disease | +0.8741 | 0.7321 | ±1.4641 | +1.194 | 0.2325 |  |
| Circulatory disease | +0.5790 | 0.5302 | ±1.0605 | +1.092 | 0.2748 |  |
| Avg. daily time 181-250 (%) | +0.0422 | 0.0223 | ±0.0445 | +1.894 | 0.0582 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **637**, R² = **0.1392**, Adj R² = **0.1241**, F-statistic = **9.19** (p = **2.30e-15**), Residual SE = **4.740** on **625** df, AIC = **3802.1**, BIC = **3855.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8851** | 1.5425 | ±3.0851 | **+4.463** | **8.06e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0087** | 0.4132 | ±0.8264 | **-2.441** | **0.0146** | * |
| **Education: high school or below (vs college)** | **+1.8049** | 0.7812 | ±1.5625 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | +0.8899 | 0.5193 | ±1.0386 | +1.714 | 0.0866 | . |
| Site: UW (vs UAB) | +0.3572 | 0.4482 | ±0.8963 | +0.797 | 0.4255 |  |
| **Age (years)** | **-0.0850** | 0.0175 | ±0.0351 | **-4.844** | **1.27e-06** | *** |
| **BMI (kg/m2)** | **+0.1126** | 0.0307 | ±0.0615 | **+3.663** | **2.49e-04** | *** |
| Hypertension | -0.3015 | 0.4472 | ±0.8944 | -0.674 | 0.5002 |  |
| High cholesterol | +0.6247 | 0.4002 | ±0.8004 | +1.561 | 0.1185 |  |
| Kidney disease | +0.8212 | 0.7283 | ±1.4566 | +1.128 | 0.2595 |  |
| Circulatory disease | +0.5606 | 0.5280 | ±1.0559 | +1.062 | 0.2883 |  |
| **Time > 180 (%)** | **+0.0410** | 0.0148 | ±0.0295 | **+2.778** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **637**, R² = **0.1395**, Adj R² = **0.1244**, F-statistic = **9.21** (p = **2.11e-15**), Residual SE = **4.740** on **625** df, AIC = **3801.9**, BIC = **3855.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8802** | 1.5428 | ±3.0855 | **+4.460** | **8.21e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0095** | 0.4131 | ±0.8262 | **-2.444** | **0.0145** | * |
| **Education: high school or below (vs college)** | **+1.7961** | 0.7803 | ±1.5605 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +0.8950 | 0.5190 | ±1.0380 | +1.725 | 0.0846 | . |
| Site: UW (vs UAB) | +0.3589 | 0.4481 | ±0.8963 | +0.801 | 0.4232 |  |
| **Age (years)** | **-0.0849** | 0.0175 | ±0.0351 | **-4.844** | **1.27e-06** | *** |
| **BMI (kg/m2)** | **+0.1127** | 0.0307 | ±0.0615 | **+3.664** | **2.48e-04** | *** |
| Hypertension | -0.2998 | 0.4470 | ±0.8941 | -0.671 | 0.5025 |  |
| High cholesterol | +0.6205 | 0.4001 | ±0.8001 | +1.551 | 0.1209 |  |
| Kidney disease | +0.8109 | 0.7287 | ±1.4574 | +1.113 | 0.2658 |  |
| Circulatory disease | +0.5608 | 0.5278 | ±1.0557 | +1.062 | 0.2881 |  |
| **Avg. daily time > 180 (%)** | **+0.0415** | 0.0149 | ±0.0298 | **+2.784** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **637**, R² = **0.1495**, Adj R² = **0.1346**, F-statistic = **9.99** (p = **7.36e-17**), Residual SE = **4.712** on **625** df, AIC = **3794.5**, BIC = **3848.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8736** | 1.5394 | ±3.0787 | **+4.465** | **8.00e-06** | *** |
| **Education: graduate level (vs college)** | **-0.9813** | 0.4111 | ±0.8222 | **-2.387** | **0.0170** | * |
| **Education: high school or below (vs college)** | **+1.8064** | 0.7715 | ±1.5430 | **+2.341** | **0.0192** | * |
| Site: UCSD (vs UAB) | +0.9276 | 0.5138 | ±1.0276 | +1.805 | 0.0710 | . |
| Site: UW (vs UAB) | +0.3794 | 0.4460 | ±0.8920 | +0.851 | 0.3950 |  |
| **Age (years)** | **-0.0834** | 0.0175 | ±0.0350 | **-4.764** | **1.90e-06** | *** |
| **BMI (kg/m2)** | **+0.1099** | 0.0307 | ±0.0615 | **+3.575** | **3.50e-04** | *** |
| Hypertension | -0.3480 | 0.4440 | ±0.8879 | -0.784 | 0.4331 |  |
| High cholesterol | +0.6035 | 0.3970 | ±0.7940 | +1.520 | 0.1285 |  |
| Kidney disease | +0.9445 | 0.7250 | ±1.4501 | +1.303 | 0.1927 |  |
| Circulatory disease | +0.5375 | 0.5270 | ±1.0539 | +1.020 | 0.3077 |  |
| **Nocturnal time > 180 (%)** | **+0.0608** | 0.0148 | ±0.0297 | **+4.094** | **4.25e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **637**, R² = **0.1339**, Adj R² = **0.1187**, F-statistic = **8.79** (p = **1.33e-14**), Residual SE = **4.755** on **625** df, AIC = **3806.1**, BIC = **3859.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8694** | 1.5351 | ±3.0702 | **+4.475** | **7.64e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0025** | 0.4128 | ±0.8256 | **-2.429** | **0.0152** | * |
| **Education: high school or below (vs college)** | **+1.8976** | 0.7823 | ±1.5647 | **+2.425** | **0.0153** | * |
| Site: UCSD (vs UAB) | +0.8535 | 0.5250 | ±1.0499 | +1.626 | 0.1040 |  |
| Site: UW (vs UAB) | +0.3011 | 0.4482 | ±0.8965 | +0.672 | 0.5017 |  |
| **Age (years)** | **-0.0864** | 0.0174 | ±0.0347 | **-4.971** | **6.66e-07** | *** |
| **BMI (kg/m2)** | **+0.1162** | 0.0306 | ±0.0612 | **+3.796** | **1.47e-04** | *** |
| Hypertension | -0.2739 | 0.4504 | ±0.9007 | -0.608 | 0.5431 |  |
| High cholesterol | +0.6603 | 0.4041 | ±0.8081 | +1.634 | 0.1022 |  |
| Kidney disease | +0.9064 | 0.7084 | ±1.4169 | +1.279 | 0.2007 |  |
| Circulatory disease | +0.5933 | 0.5300 | ±1.0601 | +1.119 | 0.2630 |  |
| Any reading > 250 during wear (0/1) | +0.8037 | 0.4308 | ±0.8617 | +1.865 | 0.0621 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **637**, R² = **0.1444**, Adj R² = **0.1293**, F-statistic = **9.59** (p = **4.17e-16**), Residual SE = **4.726** on **625** df, AIC = **3798.3**, BIC = **3851.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7537** | 1.5399 | ±3.0798 | **+4.386** | **1.16e-05** | *** |
| **Education: graduate level (vs college)** | **-0.9908** | 0.4142 | ±0.8283 | **-2.392** | **0.0167** | * |
| **Education: high school or below (vs college)** | **+1.7685** | 0.7689 | ±1.5378 | **+2.300** | **0.0214** | * |
| Site: UCSD (vs UAB) | +0.9164 | 0.5164 | ±1.0329 | +1.775 | 0.0760 | . |
| Site: UW (vs UAB) | +0.3876 | 0.4482 | ±0.8965 | +0.865 | 0.3871 |  |
| **Age (years)** | **-0.0828** | 0.0174 | ±0.0349 | **-4.751** | **2.03e-06** | *** |
| **BMI (kg/m2)** | **+0.1145** | 0.0307 | ±0.0614 | **+3.727** | **1.94e-04** | *** |
| Hypertension | -0.2818 | 0.4437 | ±0.8874 | -0.635 | 0.5254 |  |
| High cholesterol | +0.7034 | 0.3997 | ±0.7993 | +1.760 | 0.0784 | . |
| Kidney disease | +0.9283 | 0.7162 | ±1.4323 | +1.296 | 0.1949 |  |
| Circulatory disease | +0.5382 | 0.5253 | ±1.0507 | +1.024 | 0.3056 |  |
| **Time > 250 (%)** | **+0.1130** | 0.0251 | ±0.0501 | **+4.509** | **6.50e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **637**, R² = **0.1439**, Adj R² = **0.1288**, F-statistic = **9.55** (p = **4.94e-16**), Residual SE = **4.728** on **625** df, AIC = **3798.7**, BIC = **3852.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7710** | 1.5396 | ±3.0792 | **+4.398** | **1.09e-05** | *** |
| **Education: graduate level (vs college)** | **-0.9892** | 0.4142 | ±0.8285 | **-2.388** | **0.0169** | * |
| **Education: high school or below (vs college)** | **+1.7408** | 0.7701 | ±1.5402 | **+2.261** | **0.0238** | * |
| Site: UCSD (vs UAB) | +0.9105 | 0.5160 | ±1.0321 | +1.765 | 0.0776 | . |
| Site: UW (vs UAB) | +0.3787 | 0.4479 | ±0.8957 | +0.846 | 0.3978 |  |
| **Age (years)** | **-0.0832** | 0.0174 | ±0.0349 | **-4.775** | **1.80e-06** | *** |
| **BMI (kg/m2)** | **+0.1150** | 0.0307 | ±0.0614 | **+3.748** | **1.78e-04** | *** |
| Hypertension | -0.2819 | 0.4441 | ±0.8882 | -0.635 | 0.5255 |  |
| High cholesterol | +0.6972 | 0.3998 | ±0.7996 | +1.744 | 0.0812 | . |
| Kidney disease | +0.9018 | 0.7157 | ±1.4314 | +1.260 | 0.2077 |  |
| Circulatory disease | +0.5284 | 0.5262 | ±1.0524 | +1.004 | 0.3153 |  |
| **Avg. daily time > 250 (%)** | **+0.1231** | 0.0332 | ±0.0664 | **+3.708** | **2.09e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 637; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0687**, LLR χ² = **45.59** (p = **1.70e-06**), AUC = **0.6867**, AIC = **639.6**, BIC = **688.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4437 | 0.7945 | ±1.5889 | -1.817 | 0.0692 | 0.2361 | . |
| Education: graduate level (vs college) | -0.3656 | 0.2334 | ±0.4668 | -1.567 | 0.1172 | 0.6938 |  |
| Education: high school or below (vs college) | +0.4017 | 0.3147 | ±0.6293 | +1.277 | 0.2017 | 1.4944 |  |
| Site: UCSD (vs UAB) | +0.2438 | 0.2671 | ±0.5341 | +0.913 | 0.3613 | 1.2761 |  |
| Site: UW (vs UAB) | +0.0406 | 0.2405 | ±0.4811 | +0.169 | 0.8661 | 1.0414 |  |
| **Age (years)** | **-0.0259** | 0.0103 | ±0.0206 | **-2.513** | **0.0120** | 0.9745 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.557** | **3.75e-04** | 1.0467 | *** |
| Hypertension | -0.0530 | 0.2262 | ±0.4523 | -0.234 | 0.8149 | 0.9484 |  |
| High cholesterol | +0.2159 | 0.2130 | ±0.4261 | +1.013 | 0.3109 | 1.2409 |  |
| **Kidney disease** | **+0.6401** | 0.3115 | ±0.6230 | **+2.055** | **0.0399** | 1.8966 | * |
| Circulatory disease | +0.3612 | 0.2509 | ±0.5017 | +1.440 | 0.1499 | 1.4351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0810**, LLR χ² = **53.74** (p = **1.32e-07**), AUC = **0.6962**, AIC = **633.5**, BIC = **687.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0875** | 0.9916 | ±1.9832 | **-3.114** | **0.0018** | 0.0456 | ** |
| Education: graduate level (vs college) | -0.3246 | 0.2358 | ±0.4716 | -1.377 | 0.1686 | 0.7228 |  |
| Education: high school or below (vs college) | +0.3094 | 0.3210 | ±0.6420 | +0.964 | 0.3351 | 1.3627 |  |
| Site: UCSD (vs UAB) | +0.2241 | 0.2702 | ±0.5404 | +0.829 | 0.4068 | 1.2512 |  |
| Site: UW (vs UAB) | +0.1041 | 0.2438 | ±0.4876 | +0.427 | 0.6695 | 1.1097 |  |
| **Age (years)** | **-0.0286** | 0.0104 | ±0.0208 | **-2.755** | **0.0059** | 0.9718 | ** |
| **BMI (kg/m2)** | **+0.0431** | 0.0130 | ±0.0259 | **+3.329** | **8.73e-04** | 1.0441 | *** |
| Hypertension | -0.1450 | 0.2312 | ±0.4624 | -0.627 | 0.5305 | 0.8650 |  |
| High cholesterol | +0.1888 | 0.2148 | ±0.4297 | +0.879 | 0.3795 | 1.2078 |  |
| Kidney disease | +0.6130 | 0.3153 | ±0.6307 | +1.944 | 0.0519 | 1.8459 | . |
| Circulatory disease | +0.3685 | 0.2534 | ±0.5067 | +1.454 | 0.1458 | 1.4456 |  |
| **HbA1c (%)** | **+0.3224** | 0.1132 | ±0.2263 | **+2.849** | **0.0044** | 1.3804 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0827**, LLR χ² = **54.84** (p = **8.30e-08**), AUC = **0.6936**, AIC = **632.4**, BIC = **685.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7706** | 0.9156 | ±1.8312 | **-3.026** | **0.0025** | 0.0626 | ** |
| Education: graduate level (vs college) | -0.3725 | 0.2353 | ±0.4705 | -1.583 | 0.1134 | 0.6890 |  |
| Education: high school or below (vs college) | +0.3110 | 0.3203 | ±0.6406 | +0.971 | 0.3316 | 1.3648 |  |
| Site: UCSD (vs UAB) | +0.2294 | 0.2707 | ±0.5415 | +0.847 | 0.3968 | 1.2579 |  |
| Site: UW (vs UAB) | +0.0721 | 0.2426 | ±0.4853 | +0.297 | 0.7664 | 1.0747 |  |
| **Age (years)** | **-0.0261** | 0.0103 | ±0.0207 | **-2.520** | **0.0117** | 0.9743 | * |
| **BMI (kg/m2)** | **+0.0445** | 0.0129 | ±0.0259 | **+3.438** | **5.87e-04** | 1.0455 | *** |
| Hypertension | -0.1570 | 0.2322 | ±0.4644 | -0.676 | 0.4988 | 0.8547 |  |
| High cholesterol | +0.1833 | 0.2153 | ±0.4306 | +0.851 | 0.3946 | 1.2012 |  |
| Kidney disease | +0.5485 | 0.3163 | ±0.6325 | +1.734 | 0.0828 | 1.7307 | . |
| Circulatory disease | +0.3446 | 0.2541 | ±0.5083 | +1.356 | 0.1752 | 1.4114 |  |
| **Mean glucose (mg/dL)** | **+0.0118** | 0.0039 | ±0.0078 | **+3.027** | **0.0025** | 1.0119 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0827**, LLR χ² = **54.84** (p = **8.30e-08**), AUC = **0.6936**, AIC = **632.4**, BIC = **685.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4020** | 1.2667 | ±2.5334 | **-3.475** | **5.11e-04** | 0.0123 | *** |
| Education: graduate level (vs college) | -0.3725 | 0.2353 | ±0.4705 | -1.583 | 0.1134 | 0.6890 |  |
| Education: high school or below (vs college) | +0.3110 | 0.3203 | ±0.6406 | +0.971 | 0.3316 | 1.3648 |  |
| Site: UCSD (vs UAB) | +0.2294 | 0.2707 | ±0.5415 | +0.847 | 0.3968 | 1.2579 |  |
| Site: UW (vs UAB) | +0.0721 | 0.2426 | ±0.4853 | +0.297 | 0.7664 | 1.0747 |  |
| **Age (years)** | **-0.0261** | 0.0103 | ±0.0207 | **-2.520** | **0.0117** | 0.9743 | * |
| **BMI (kg/m2)** | **+0.0445** | 0.0129 | ±0.0259 | **+3.438** | **5.87e-04** | 1.0455 | *** |
| Hypertension | -0.1570 | 0.2322 | ±0.4644 | -0.676 | 0.4988 | 0.8547 |  |
| High cholesterol | +0.1833 | 0.2153 | ±0.4306 | +0.851 | 0.3946 | 1.2012 |  |
| Kidney disease | +0.5485 | 0.3163 | ±0.6325 | +1.734 | 0.0828 | 1.7307 | . |
| Circulatory disease | +0.3446 | 0.2541 | ±0.5083 | +1.356 | 0.1752 | 1.4114 |  |
| **GMI (%)** | **+0.4929** | 0.1628 | ±0.3256 | **+3.027** | **0.0025** | 1.6370 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0910**, LLR χ² = **60.33** (p = **8.04e-09**), AUC = **0.7029**, AIC = **626.9**, BIC = **680.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1287** | 0.9217 | ±1.8435 | **-3.394** | **6.88e-04** | 0.0438 | *** |
| Education: graduate level (vs college) | -0.3785 | 0.2361 | ±0.4721 | -1.603 | 0.1089 | 0.6849 |  |
| Education: high school or below (vs college) | +0.3007 | 0.3212 | ±0.6423 | +0.936 | 0.3492 | 1.3507 |  |
| Site: UCSD (vs UAB) | +0.2294 | 0.2723 | ±0.5447 | +0.842 | 0.3995 | 1.2579 |  |
| Site: UW (vs UAB) | +0.0652 | 0.2435 | ±0.4870 | +0.268 | 0.7889 | 1.0674 |  |
| **Age (years)** | **-0.0248** | 0.0104 | ±0.0208 | **-2.384** | **0.0171** | 0.9755 | * |
| **BMI (kg/m2)** | **+0.0424** | 0.0130 | ±0.0260 | **+3.270** | **0.0011** | 1.0433 | ** |
| Hypertension | -0.1739 | 0.2329 | ±0.4658 | -0.747 | 0.4552 | 0.8404 |  |
| High cholesterol | +0.1562 | 0.2171 | ±0.4343 | +0.719 | 0.4718 | 1.1691 |  |
| Kidney disease | +0.6170 | 0.3164 | ±0.6328 | +1.950 | 0.0512 | 1.8534 | . |
| Circulatory disease | +0.3571 | 0.2562 | ±0.5123 | +1.394 | 0.1633 | 1.4292 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0150** | 0.0040 | ±0.0080 | **+3.753** | **1.75e-04** | 1.0151 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0857**, LLR χ² = **56.85** (p = **3.55e-08**), AUC = **0.7024**, AIC = **630.4**, BIC = **683.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9278** | 0.8177 | ±1.6353 | **-2.358** | **0.0184** | 0.1455 | * |
| Education: graduate level (vs college) | -0.3507 | 0.2359 | ±0.4719 | -1.487 | 0.1371 | 0.7042 |  |
| Education: high school or below (vs college) | +0.2472 | 0.3242 | ±0.6484 | +0.762 | 0.4458 | 1.2804 |  |
| Site: UCSD (vs UAB) | +0.2302 | 0.2708 | ±0.5416 | +0.850 | 0.3953 | 1.2589 |  |
| Site: UW (vs UAB) | +0.1153 | 0.2442 | ±0.4884 | +0.472 | 0.6368 | 1.1222 |  |
| **Age (years)** | **-0.0294** | 0.0104 | ±0.0209 | **-2.820** | **0.0048** | 0.9710 | ** |
| **BMI (kg/m2)** | **+0.0461** | 0.0130 | ±0.0259 | **+3.557** | **3.75e-04** | 1.0472 | *** |
| Hypertension | -0.1691 | 0.2331 | ±0.4662 | -0.726 | 0.4681 | 0.8444 |  |
| High cholesterol | +0.2206 | 0.2159 | ±0.4318 | +1.022 | 0.3068 | 1.2469 |  |
| Kidney disease | +0.4131 | 0.3247 | ±0.6494 | +1.272 | 0.2033 | 1.5115 |  |
| Circulatory disease | +0.3850 | 0.2535 | ±0.5070 | +1.519 | 0.1287 | 1.4697 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0274** | 0.0082 | ±0.0165 | **+3.330** | **8.69e-04** | 1.0278 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0816**, LLR χ² = **54.15** (p = **1.11e-07**), AUC = **0.6994**, AIC = **633.1**, BIC = **686.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8797** | 0.8171 | ±1.6342 | **-2.301** | **0.0214** | 0.1526 | * |
| Education: graduate level (vs college) | -0.3460 | 0.2353 | ±0.4706 | -1.470 | 0.1415 | 0.7075 |  |
| Education: high school or below (vs college) | +0.2459 | 0.3243 | ±0.6487 | +0.758 | 0.4483 | 1.2788 |  |
| Site: UCSD (vs UAB) | +0.2284 | 0.2699 | ±0.5399 | +0.846 | 0.3974 | 1.2566 |  |
| Site: UW (vs UAB) | +0.0988 | 0.2434 | ±0.4868 | +0.406 | 0.6849 | 1.1038 |  |
| **Age (years)** | **-0.0292** | 0.0104 | ±0.0209 | **-2.797** | **0.0052** | 0.9712 | ** |
| **BMI (kg/m2)** | **+0.0462** | 0.0129 | ±0.0259 | **+3.576** | **3.48e-04** | 1.0473 | *** |
| Hypertension | -0.1453 | 0.2318 | ±0.4636 | -0.627 | 0.5307 | 0.8647 |  |
| High cholesterol | +0.2164 | 0.2153 | ±0.4306 | +1.005 | 0.3147 | 1.2416 |  |
| Kidney disease | +0.4318 | 0.3240 | ±0.6480 | +1.333 | 0.1826 | 1.5401 |  |
| Circulatory disease | +0.3911 | 0.2526 | ±0.5053 | +1.548 | 0.1216 | 1.4787 |  |
| **Avg. daily SD (mg/dL)** | **+0.0279** | 0.0096 | ±0.0192 | **+2.905** | **0.0037** | 1.0283 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0763**, LLR χ² = **50.63** (p = **4.81e-07**), AUC = **0.7005**, AIC = **636.6**, BIC = **690.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0308** | 0.8424 | ±1.6848 | **-2.411** | **0.0159** | 0.1312 | * |
| Education: graduate level (vs college) | -0.3537 | 0.2349 | ±0.4698 | -1.506 | 0.1321 | 0.7021 |  |
| Education: high school or below (vs college) | +0.3032 | 0.3200 | ±0.6399 | +0.948 | 0.3433 | 1.3542 |  |
| Site: UCSD (vs UAB) | +0.2345 | 0.2683 | ±0.5366 | +0.874 | 0.3820 | 1.2643 |  |
| Site: UW (vs UAB) | +0.0958 | 0.2433 | ±0.4867 | +0.394 | 0.6938 | 1.1006 |  |
| **Age (years)** | **-0.0297** | 0.0105 | ±0.0210 | **-2.828** | **0.0047** | 0.9708 | ** |
| **BMI (kg/m2)** | **+0.0463** | 0.0129 | ±0.0258 | **+3.589** | **3.32e-04** | 1.0474 | *** |
| Hypertension | -0.1108 | 0.2297 | ±0.4594 | -0.482 | 0.6295 | 0.8951 |  |
| High cholesterol | +0.2346 | 0.2147 | ±0.4294 | +1.093 | 0.2745 | 1.2644 |  |
| Kidney disease | +0.4654 | 0.3237 | ±0.6474 | +1.438 | 0.1505 | 1.5927 |  |
| Circulatory disease | +0.3871 | 0.2519 | ±0.5039 | +1.536 | 0.1244 | 1.4727 |  |
| **CV (%)** | **+0.0383** | 0.0169 | ±0.0338 | **+2.262** | **0.0237** | 1.0390 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0765**, LLR χ² = **50.75** (p = **4.59e-07**), AUC = **0.6979**, AIC = **636.5**, BIC = **690.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2118 | 0.9624 | ±1.9249 | -0.220 | 0.8258 | 0.8092 |  |
| Education: graduate level (vs college) | -0.3691 | 0.2349 | ±0.4699 | -1.571 | 0.1162 | 0.6914 |  |
| Education: high school or below (vs college) | +0.3027 | 0.3194 | ±0.6389 | +0.948 | 0.3433 | 1.3536 |  |
| Site: UCSD (vs UAB) | +0.2250 | 0.2684 | ±0.5369 | +0.838 | 0.4019 | 1.2523 |  |
| Site: UW (vs UAB) | +0.0778 | 0.2426 | ±0.4851 | +0.321 | 0.7484 | 1.0809 |  |
| **Age (years)** | **-0.0301** | 0.0105 | ±0.0210 | **-2.857** | **0.0043** | 0.9704 | ** |
| **BMI (kg/m2)** | **+0.0455** | 0.0129 | ±0.0257 | **+3.539** | **4.02e-04** | 1.0466 | *** |
| Hypertension | -0.1029 | 0.2293 | ±0.4586 | -0.449 | 0.6535 | 0.9022 |  |
| High cholesterol | +0.2271 | 0.2146 | ±0.4293 | +1.058 | 0.2900 | 1.2549 |  |
| Kidney disease | +0.5085 | 0.3190 | ±0.6379 | +1.594 | 0.1109 | 1.6629 |  |
| Circulatory disease | +0.3711 | 0.2516 | ±0.5032 | +1.475 | 0.1402 | 1.4494 |  |
| **Mean / SD ratio** | **-0.1873** | 0.0835 | ±0.1671 | **-2.242** | **0.0249** | 0.8292 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0719**, LLR χ² = **47.67** (p = **1.63e-06**), AUC = **0.6928**, AIC = **639.6**, BIC = **693.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6763 | 0.9562 | ±1.9124 | -0.707 | 0.4794 | 0.5085 |  |
| Education: graduate level (vs college) | -0.3615 | 0.2341 | ±0.4683 | -1.544 | 0.1225 | 0.6966 |  |
| Education: high school or below (vs college) | +0.3323 | 0.3190 | ±0.6379 | +1.042 | 0.2976 | 1.3941 |  |
| Site: UCSD (vs UAB) | +0.2223 | 0.2679 | ±0.5358 | +0.830 | 0.4067 | 1.2490 |  |
| Site: UW (vs UAB) | +0.0583 | 0.2415 | ±0.4829 | +0.241 | 0.8093 | 1.0600 |  |
| **Age (years)** | **-0.0287** | 0.0105 | ±0.0210 | **-2.728** | **0.0064** | 0.9717 | ** |
| **BMI (kg/m2)** | **+0.0455** | 0.0129 | ±0.0257 | **+3.541** | **3.99e-04** | 1.0466 | *** |
| Hypertension | -0.0741 | 0.2278 | ±0.4556 | -0.325 | 0.7450 | 0.9286 |  |
| High cholesterol | +0.2198 | 0.2138 | ±0.4275 | +1.028 | 0.3038 | 1.2458 |  |
| Kidney disease | +0.5627 | 0.3167 | ±0.6334 | +1.777 | 0.0756 | 1.7554 | . |
| Circulatory disease | +0.3694 | 0.2511 | ±0.5021 | +1.471 | 0.1412 | 1.4468 |  |
| Avg. daily mean/SD | -0.0971 | 0.0679 | ±0.1358 | -1.429 | 0.1530 | 0.9075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0696**, LLR χ² = **46.17** (p = **3.01e-06**), AUC = **0.6888**, AIC = **641.1**, BIC = **694.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7616** | 0.8974 | ±1.7947 | **-1.963** | **0.0496** | 0.1718 | * |
| Education: graduate level (vs college) | -0.3651 | 0.2336 | ±0.4673 | -1.563 | 0.1182 | 0.6941 |  |
| Education: high school or below (vs college) | +0.3699 | 0.3178 | ±0.6357 | +1.164 | 0.2445 | 1.4476 |  |
| Site: UCSD (vs UAB) | +0.2347 | 0.2675 | ±0.5350 | +0.877 | 0.3803 | 1.2646 |  |
| Site: UW (vs UAB) | +0.0634 | 0.2427 | ±0.4853 | +0.261 | 0.7938 | 1.0655 |  |
| **Age (years)** | **-0.0259** | 0.0103 | ±0.0206 | **-2.514** | **0.0119** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0452** | 0.0129 | ±0.0257 | **+3.514** | **4.41e-04** | 1.0462 | *** |
| Hypertension | -0.0635 | 0.2271 | ±0.4542 | -0.279 | 0.7799 | 0.9385 |  |
| High cholesterol | +0.2237 | 0.2136 | ±0.4272 | +1.048 | 0.2948 | 1.2507 |  |
| **Kidney disease** | **+0.6318** | 0.3121 | ±0.6242 | **+2.024** | **0.0429** | 1.8810 | * |
| Circulatory disease | +0.3622 | 0.2510 | ±0.5020 | +1.443 | 0.1490 | 1.4365 |  |
| MAG (mg/dL/h) | +0.0080 | 0.0104 | ±0.0208 | +0.766 | 0.4439 | 1.0080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0775**, LLR χ² = **51.39** (p = **3.51e-07**), AUC = **0.6953**, AIC = **635.9**, BIC = **689.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0040** | 0.8347 | ±1.6695 | **-2.401** | **0.0164** | 0.1348 | * |
| Education: graduate level (vs college) | -0.3470 | 0.2349 | ±0.4699 | -1.477 | 0.1397 | 0.7068 |  |
| Education: high school or below (vs college) | +0.2675 | 0.3232 | ±0.6464 | +0.828 | 0.4078 | 1.3067 |  |
| Site: UCSD (vs UAB) | +0.2305 | 0.2690 | ±0.5381 | +0.857 | 0.3916 | 1.2592 |  |
| Site: UW (vs UAB) | +0.0856 | 0.2428 | ±0.4856 | +0.352 | 0.7246 | 1.0893 |  |
| **Age (years)** | **-0.0285** | 0.0104 | ±0.0209 | **-2.731** | **0.0063** | 0.9719 | ** |
| **BMI (kg/m2)** | **+0.0471** | 0.0129 | ±0.0258 | **+3.646** | **2.67e-04** | 1.0482 | *** |
| Hypertension | -0.1159 | 0.2305 | ±0.4610 | -0.503 | 0.6151 | 0.8906 |  |
| High cholesterol | +0.2194 | 0.2146 | ±0.4292 | +1.023 | 0.3065 | 1.2454 |  |
| Kidney disease | +0.4763 | 0.3222 | ±0.6444 | +1.479 | 0.1393 | 1.6102 |  |
| Circulatory disease | +0.3703 | 0.2522 | ±0.5044 | +1.468 | 0.1421 | 1.4482 |  |
| **Avg. daily range (mg/dL)** | **+0.0061** | 0.0025 | ±0.0051 | **+2.416** | **0.0157** | 1.0062 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0902**, LLR χ² = **59.82** (p = **1.00e-08**), AUC = **0.7045**, AIC = **627.4**, BIC = **680.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7353** | 0.8074 | ±1.6149 | **-2.149** | **0.0316** | 0.1764 | * |
| Education: graduate level (vs college) | -0.3599 | 0.2366 | ±0.4731 | -1.521 | 0.1282 | 0.6977 |  |
| Education: high school or below (vs college) | +0.3564 | 0.3214 | ±0.6428 | +1.109 | 0.2675 | 1.4282 |  |
| Site: UCSD (vs UAB) | +0.2446 | 0.2726 | ±0.5453 | +0.897 | 0.3696 | 1.2771 |  |
| Site: UW (vs UAB) | +0.1063 | 0.2441 | ±0.4881 | +0.435 | 0.6632 | 1.1121 |  |
| **Age (years)** | **-0.0280** | 0.0104 | ±0.0208 | **-2.692** | **0.0071** | 0.9724 | ** |
| **BMI (kg/m2)** | **+0.0449** | 0.0130 | ±0.0260 | **+3.458** | **5.44e-04** | 1.0459 | *** |
| Hypertension | -0.1741 | 0.2328 | ±0.4656 | -0.748 | 0.4546 | 0.8402 |  |
| High cholesterol | +0.2217 | 0.2168 | ±0.4337 | +1.022 | 0.3066 | 1.2482 |  |
| Kidney disease | +0.4980 | 0.3220 | ±0.6439 | +1.547 | 0.1219 | 1.6454 |  |
| Circulatory disease | +0.3417 | 0.2560 | ±0.5121 | +1.334 | 0.1820 | 1.4073 |  |
| **SD of daily means (mg/dL)** | **+0.0513** | 0.0140 | ±0.0279 | **+3.670** | **2.43e-04** | 1.0526 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0893**, LLR χ² = **59.23** (p = **1.29e-08**), AUC = **0.7047**, AIC = **628.0**, BIC = **681.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0427 | 1.0564 | ±2.1128 | +0.987 | 0.3236 | 2.8370 |  |
| Education: graduate level (vs college) | -0.3356 | 0.2369 | ±0.4738 | -1.417 | 0.1565 | 0.7149 |  |
| Education: high school or below (vs college) | +0.3063 | 0.3224 | ±0.6447 | +0.950 | 0.3420 | 1.3584 |  |
| Site: UCSD (vs UAB) | +0.2625 | 0.2727 | ±0.5453 | +0.963 | 0.3357 | 1.3001 |  |
| Site: UW (vs UAB) | +0.1380 | 0.2451 | ±0.4903 | +0.563 | 0.5735 | 1.1480 |  |
| **Age (years)** | **-0.0273** | 0.0104 | ±0.0208 | **-2.622** | **0.0087** | 0.9731 | ** |
| **BMI (kg/m2)** | **+0.0457** | 0.0130 | ±0.0260 | **+3.522** | **4.28e-04** | 1.0468 | *** |
| Hypertension | -0.1452 | 0.2320 | ±0.4640 | -0.626 | 0.5315 | 0.8649 |  |
| High cholesterol | +0.1927 | 0.2168 | ±0.4335 | +0.889 | 0.3741 | 1.2125 |  |
| Kidney disease | +0.4662 | 0.3214 | ±0.6428 | +1.451 | 0.1469 | 1.5939 |  |
| Circulatory disease | +0.3508 | 0.2555 | ±0.5110 | +1.373 | 0.1697 | 1.4202 |  |
| **Time in range 70-180, pooled (%)** | **-0.0262** | 0.0072 | ±0.0144 | **-3.648** | **2.65e-04** | 0.9742 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0894**, LLR χ² = **59.30** (p = **1.25e-08**), AUC = **0.7050**, AIC = **627.9**, BIC = **681.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0483 | 1.0545 | ±2.1090 | +0.994 | 0.3202 | 2.8528 |  |
| Education: graduate level (vs college) | -0.3338 | 0.2369 | ±0.4739 | -1.409 | 0.1589 | 0.7162 |  |
| Education: high school or below (vs college) | +0.3015 | 0.3226 | ±0.6453 | +0.934 | 0.3501 | 1.3518 |  |
| Site: UCSD (vs UAB) | +0.2614 | 0.2728 | ±0.5455 | +0.958 | 0.3379 | 1.2988 |  |
| Site: UW (vs UAB) | +0.1402 | 0.2452 | ±0.4904 | +0.572 | 0.5675 | 1.1505 |  |
| **Age (years)** | **-0.0274** | 0.0104 | ±0.0208 | **-2.636** | **0.0084** | 0.9730 | ** |
| **BMI (kg/m2)** | **+0.0457** | 0.0130 | ±0.0260 | **+3.525** | **4.23e-04** | 1.0468 | *** |
| Hypertension | -0.1425 | 0.2320 | ±0.4640 | -0.614 | 0.5391 | 0.8672 |  |
| High cholesterol | +0.1909 | 0.2168 | ±0.4336 | +0.880 | 0.3787 | 1.2103 |  |
| Kidney disease | +0.4607 | 0.3220 | ±0.6440 | +1.431 | 0.1524 | 1.5853 |  |
| Circulatory disease | +0.3524 | 0.2555 | ±0.5109 | +1.379 | 0.1678 | 1.4224 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0260** | 0.0071 | ±0.0142 | **-3.665** | **2.47e-04** | 0.9743 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0700**, LLR χ² = **46.41** (p = **2.74e-06**), AUC = **0.6867**, AIC = **640.8**, BIC = **694.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3734 | 0.7981 | ±1.5961 | -1.721 | 0.0853 | 0.2532 | . |
| Education: graduate level (vs college) | -0.3640 | 0.2333 | ±0.4665 | -1.560 | 0.1186 | 0.6949 |  |
| Education: high school or below (vs college) | +0.3855 | 0.3153 | ±0.6305 | +1.223 | 0.2215 | 1.4703 |  |
| Site: UCSD (vs UAB) | +0.2044 | 0.2703 | ±0.5406 | +0.756 | 0.4496 | 1.2268 |  |
| Site: UW (vs UAB) | +0.0096 | 0.2426 | ±0.4852 | +0.040 | 0.9683 | 1.0097 |  |
| **Age (years)** | **-0.0258** | 0.0103 | ±0.0206 | **-2.506** | **0.0122** | 0.9746 | * |
| **BMI (kg/m2)** | **+0.0460** | 0.0129 | ±0.0257 | **+3.574** | **3.51e-04** | 1.0471 | *** |
| Hypertension | -0.0618 | 0.2266 | ±0.4532 | -0.273 | 0.7850 | 0.9401 |  |
| High cholesterol | +0.2014 | 0.2136 | ±0.4273 | +0.943 | 0.3459 | 1.2231 |  |
| **Kidney disease** | **+0.6398** | 0.3122 | ±0.6244 | **+2.050** | **0.0404** | 1.8962 | * |
| Circulatory disease | +0.3626 | 0.2511 | ±0.5021 | +1.444 | 0.1487 | 1.4371 |  |
| Time < 54 (%) | -0.1386 | 0.1653 | ±0.3305 | -0.839 | 0.4016 | 0.8706 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0693**, LLR χ² = **45.98** (p = **3.26e-06**), AUC = **0.6863**, AIC = **641.3**, BIC = **694.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4238 | 0.7950 | ±1.5900 | -1.791 | 0.0733 | 0.2408 | . |
| Education: graduate level (vs college) | -0.3698 | 0.2334 | ±0.4667 | -1.585 | 0.1130 | 0.6908 |  |
| Education: high school or below (vs college) | +0.3911 | 0.3151 | ±0.6301 | +1.241 | 0.2144 | 1.4787 |  |
| Site: UCSD (vs UAB) | +0.2224 | 0.2691 | ±0.5382 | +0.826 | 0.4086 | 1.2490 |  |
| Site: UW (vs UAB) | +0.0183 | 0.2429 | ±0.4858 | +0.076 | 0.9398 | 1.0185 |  |
| **Age (years)** | **-0.0255** | 0.0103 | ±0.0206 | **-2.474** | **0.0134** | 0.9748 | * |
| **BMI (kg/m2)** | **+0.0458** | 0.0129 | ±0.0257 | **+3.563** | **3.66e-04** | 1.0469 | *** |
| Hypertension | -0.0592 | 0.2264 | ±0.4528 | -0.262 | 0.7936 | 0.9425 |  |
| High cholesterol | +0.2061 | 0.2135 | ±0.4271 | +0.965 | 0.3346 | 1.2288 |  |
| **Kidney disease** | **+0.6434** | 0.3119 | ±0.6238 | **+2.063** | **0.0391** | 1.9030 | * |
| Circulatory disease | +0.3628 | 0.2510 | ±0.5020 | +1.445 | 0.1483 | 1.4374 |  |
| Avg. daily time < 54 (%) | -0.0980 | 0.1665 | ±0.3330 | -0.589 | 0.5560 | 0.9066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0688**, LLR χ² = **45.62** (p = **3.77e-06**), AUC = **0.6870**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4527 | 0.7962 | ±1.5923 | -1.825 | 0.0681 | 0.2339 | . |
| Education: graduate level (vs college) | -0.3631 | 0.2339 | ±0.4678 | -1.552 | 0.1206 | 0.6955 |  |
| Education: high school or below (vs college) | +0.4020 | 0.3147 | ±0.6293 | +1.278 | 0.2014 | 1.4949 |  |
| Site: UCSD (vs UAB) | +0.2481 | 0.2682 | ±0.5364 | +0.925 | 0.3549 | 1.2816 |  |
| Site: UW (vs UAB) | +0.0444 | 0.2416 | ±0.4832 | +0.184 | 0.8541 | 1.0454 |  |
| **Age (years)** | **-0.0260** | 0.0103 | ±0.0206 | **-2.518** | **0.0118** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.555** | **3.78e-04** | 1.0467 | *** |
| Hypertension | -0.0503 | 0.2267 | ±0.4533 | -0.222 | 0.8244 | 0.9509 |  |
| High cholesterol | +0.2167 | 0.2131 | ±0.4262 | +1.017 | 0.3092 | 1.2420 |  |
| **Kidney disease** | **+0.6384** | 0.3116 | ±0.6232 | **+2.049** | **0.0405** | 1.8935 | * |
| Circulatory disease | +0.3629 | 0.2510 | ±0.5020 | +1.446 | 0.1482 | 1.4375 |  |
| Time 54-69, pooled (%) | +0.0077 | 0.0436 | ±0.0871 | +0.177 | 0.8594 | 1.0077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0688**, LLR χ² = **45.65** (p = **3.72e-06**), AUC = **0.6870**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4520 | 0.7952 | ±1.5904 | -1.826 | 0.0679 | 0.2341 | . |
| Education: graduate level (vs college) | -0.3616 | 0.2340 | ±0.4681 | -1.545 | 0.1223 | 0.6965 |  |
| Education: high school or below (vs college) | +0.4021 | 0.3147 | ±0.6294 | +1.278 | 0.2013 | 1.4949 |  |
| Site: UCSD (vs UAB) | +0.2488 | 0.2679 | ±0.5358 | +0.929 | 0.3529 | 1.2825 |  |
| Site: UW (vs UAB) | +0.0462 | 0.2418 | ±0.4835 | +0.191 | 0.8484 | 1.0473 |  |
| **Age (years)** | **-0.0261** | 0.0103 | ±0.0207 | **-2.524** | **0.0116** | 0.9743 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.553** | **3.80e-04** | 1.0466 | *** |
| Hypertension | -0.0496 | 0.2266 | ±0.4532 | -0.219 | 0.8266 | 0.9516 |  |
| High cholesterol | +0.2170 | 0.2131 | ±0.4263 | +1.018 | 0.3085 | 1.2424 |  |
| **Kidney disease** | **+0.6382** | 0.3116 | ±0.6231 | **+2.048** | **0.0405** | 1.8930 | * |
| Circulatory disease | +0.3637 | 0.2510 | ±0.5020 | +1.449 | 0.1474 | 1.4386 |  |
| Avg. daily time 54-69 (%) | +0.0103 | 0.0418 | ±0.0835 | +0.246 | 0.8057 | 1.0103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0688**, LLR χ² = **45.60** (p = **3.80e-06**), AUC = **0.6866**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4383 | 0.7969 | ±1.5938 | -1.805 | 0.0711 | 0.2373 | . |
| Education: graduate level (vs college) | -0.3666 | 0.2337 | ±0.4673 | -1.569 | 0.1166 | 0.6931 |  |
| Education: high school or below (vs college) | +0.4012 | 0.3147 | ±0.6294 | +1.275 | 0.2024 | 1.4936 |  |
| Site: UCSD (vs UAB) | +0.2411 | 0.2689 | ±0.5379 | +0.896 | 0.3700 | 1.2726 |  |
| Site: UW (vs UAB) | +0.0382 | 0.2421 | ±0.4841 | +0.158 | 0.8746 | 1.0389 |  |
| **Age (years)** | **-0.0258** | 0.0103 | ±0.0206 | **-2.503** | **0.0123** | 0.9745 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.557** | **3.74e-04** | 1.0467 | *** |
| Hypertension | -0.0543 | 0.2267 | ±0.4533 | -0.239 | 0.8108 | 0.9472 |  |
| High cholesterol | +0.2152 | 0.2132 | ±0.4264 | +1.009 | 0.3128 | 1.2401 |  |
| **Kidney disease** | **+0.6408** | 0.3116 | ±0.6232 | **+2.056** | **0.0398** | 1.8979 | * |
| Circulatory disease | +0.3606 | 0.2510 | ±0.5020 | +1.437 | 0.1508 | 1.4342 |  |
| Time < 70 (%) | -0.0031 | 0.0366 | ±0.0731 | -0.086 | 0.9316 | 0.9969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0687**, LLR χ² = **45.60** (p = **3.81e-06**), AUC = **0.6869**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4458 | 0.7953 | ±1.5906 | -1.818 | 0.0691 | 0.2356 | . |
| Education: graduate level (vs college) | -0.3647 | 0.2339 | ±0.4678 | -1.559 | 0.1189 | 0.6944 |  |
| Education: high school or below (vs college) | +0.4020 | 0.3147 | ±0.6294 | +1.278 | 0.2014 | 1.4949 |  |
| Site: UCSD (vs UAB) | +0.2453 | 0.2683 | ±0.5366 | +0.914 | 0.3606 | 1.2780 |  |
| Site: UW (vs UAB) | +0.0422 | 0.2422 | ±0.4844 | +0.174 | 0.8617 | 1.0431 |  |
| **Age (years)** | **-0.0259** | 0.0103 | ±0.0207 | **-2.509** | **0.0121** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.556** | **3.77e-04** | 1.0467 | *** |
| Hypertension | -0.0522 | 0.2266 | ±0.4531 | -0.230 | 0.8179 | 0.9492 |  |
| High cholesterol | +0.2163 | 0.2132 | ±0.4264 | +1.015 | 0.3103 | 1.2415 |  |
| **Kidney disease** | **+0.6396** | 0.3116 | ±0.6232 | **+2.053** | **0.0401** | 1.8958 | * |
| Circulatory disease | +0.3617 | 0.2509 | ±0.5019 | +1.441 | 0.1495 | 1.4357 |  |
| Avg. daily time < 70 (%) | +0.0020 | 0.0351 | ±0.0702 | +0.058 | 0.9538 | 1.0020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0915**, LLR χ² = **60.66** (p = **6.98e-09**), AUC = **0.6989**, AIC = **626.6**, BIC = **680.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.3229** | 2.4242 | ±4.8483 | **+2.196** | **0.0281** | 204.9791 | * |
| Education: graduate level (vs college) | -0.3362 | 0.2360 | ±0.4721 | -1.424 | 0.1544 | 0.7145 |  |
| Education: high school or below (vs college) | +0.2874 | 0.3281 | ±0.6563 | +0.876 | 0.3811 | 1.3329 |  |
| Site: UCSD (vs UAB) | +0.2774 | 0.2729 | ±0.5457 | +1.016 | 0.3094 | 1.3197 |  |
| Site: UW (vs UAB) | +0.1432 | 0.2450 | ±0.4900 | +0.584 | 0.5589 | 1.1540 |  |
| **Age (years)** | **-0.0259** | 0.0104 | ±0.0208 | **-2.486** | **0.0129** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0469** | 0.0130 | ±0.0259 | **+3.618** | **2.97e-04** | 1.0480 | *** |
| Hypertension | -0.1338 | 0.2316 | ±0.4632 | -0.578 | 0.5636 | 0.8748 |  |
| High cholesterol | +0.2499 | 0.2174 | ±0.4348 | +1.149 | 0.2504 | 1.2839 |  |
| Kidney disease | +0.5358 | 0.3198 | ±0.6395 | +1.676 | 0.0938 | 1.7088 | . |
| Circulatory disease | +0.3436 | 0.2565 | ±0.5129 | +1.340 | 0.1803 | 1.4101 |  |
| **Time 54-250, pooled (%)** | **-0.0694** | 0.0231 | ±0.0461 | **-3.008** | **0.0026** | 0.9330 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0918**, LLR χ² = **60.90** (p = **6.29e-09**), AUC = **0.6981**, AIC = **626.3**, BIC = **679.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9995** | 2.5497 | ±5.0995 | **+2.353** | **0.0186** | 403.2113 | * |
| Education: graduate level (vs college) | -0.3296 | 0.2360 | ±0.4720 | -1.397 | 0.1625 | 0.7192 |  |
| Education: high school or below (vs college) | +0.2677 | 0.3299 | ±0.6599 | +0.811 | 0.4171 | 1.3070 |  |
| Site: UCSD (vs UAB) | +0.2711 | 0.2734 | ±0.5468 | +0.992 | 0.3214 | 1.3114 |  |
| Site: UW (vs UAB) | +0.1411 | 0.2449 | ±0.4898 | +0.576 | 0.5645 | 1.1515 |  |
| **Age (years)** | **-0.0264** | 0.0104 | ±0.0208 | **-2.530** | **0.0114** | 0.9740 | * |
| **BMI (kg/m2)** | **+0.0471** | 0.0130 | ±0.0259 | **+3.635** | **2.78e-04** | 1.0483 | *** |
| Hypertension | -0.1353 | 0.2318 | ±0.4636 | -0.584 | 0.5594 | 0.8735 |  |
| High cholesterol | +0.2462 | 0.2175 | ±0.4351 | +1.132 | 0.2578 | 1.2791 |  |
| Kidney disease | +0.5173 | 0.3210 | ±0.6420 | +1.611 | 0.1071 | 1.6774 |  |
| Circulatory disease | +0.3430 | 0.2568 | ±0.5136 | +1.336 | 0.1816 | 1.4092 |  |
| **Avg. daily time 54-250 (%)** | **-0.0758** | 0.0243 | ±0.0486 | **-3.119** | **0.0018** | 0.9270 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0802**, LLR χ² = **53.20** (p = **1.65e-07**), AUC = **0.6993**, AIC = **634.0**, BIC = **687.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4633 | 0.7999 | ±1.5998 | -1.829 | 0.0673 | 0.2315 | . |
| Education: graduate level (vs college) | -0.3578 | 0.2353 | ±0.4707 | -1.520 | 0.1284 | 0.6992 |  |
| Education: high school or below (vs college) | +0.3423 | 0.3176 | ±0.6353 | +1.078 | 0.2811 | 1.4082 |  |
| Site: UCSD (vs UAB) | +0.2291 | 0.2704 | ±0.5409 | +0.847 | 0.3969 | 1.2575 |  |
| Site: UW (vs UAB) | +0.0827 | 0.2426 | ±0.4852 | +0.341 | 0.7330 | 1.0863 |  |
| **Age (years)** | **-0.0270** | 0.0103 | ±0.0207 | **-2.609** | **0.0091** | 0.9734 | ** |
| **BMI (kg/m2)** | **+0.0451** | 0.0129 | ±0.0258 | **+3.488** | **4.87e-04** | 1.0461 | *** |
| Hypertension | -0.1250 | 0.2303 | ±0.4605 | -0.543 | 0.5872 | 0.8825 |  |
| High cholesterol | +0.1682 | 0.2158 | ±0.4315 | +0.779 | 0.4357 | 1.1831 |  |
| Kidney disease | +0.4969 | 0.3197 | ±0.6394 | +1.554 | 0.1201 | 1.6436 |  |
| Circulatory disease | +0.3555 | 0.2537 | ±0.5074 | +1.401 | 0.1611 | 1.4269 |  |
| **Time 181-250, pooled (%)** | **+0.0286** | 0.0103 | ±0.0205 | **+2.787** | **0.0053** | 1.0290 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0815**, LLR χ² = **54.07** (p = **1.15e-07**), AUC = **0.7008**, AIC = **633.2**, BIC = **686.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4769 | 0.8009 | ±1.6018 | -1.844 | 0.0652 | 0.2284 | . |
| Education: graduate level (vs college) | -0.3584 | 0.2356 | ±0.4712 | -1.521 | 0.1282 | 0.6988 |  |
| Education: high school or below (vs college) | +0.3386 | 0.3179 | ±0.6359 | +1.065 | 0.2868 | 1.4031 |  |
| Site: UCSD (vs UAB) | +0.2355 | 0.2707 | ±0.5415 | +0.870 | 0.3843 | 1.2656 |  |
| Site: UW (vs UAB) | +0.0913 | 0.2430 | ±0.4859 | +0.376 | 0.7072 | 1.0955 |  |
| **Age (years)** | **-0.0268** | 0.0103 | ±0.0207 | **-2.596** | **0.0094** | 0.9735 | ** |
| **BMI (kg/m2)** | **+0.0450** | 0.0129 | ±0.0259 | **+3.483** | **4.95e-04** | 1.0461 | *** |
| Hypertension | -0.1262 | 0.2304 | ±0.4608 | -0.548 | 0.5838 | 0.8814 |  |
| High cholesterol | +0.1673 | 0.2159 | ±0.4318 | +0.775 | 0.4384 | 1.1821 |  |
| Kidney disease | +0.4904 | 0.3202 | ±0.6403 | +1.532 | 0.1256 | 1.6330 |  |
| Circulatory disease | +0.3584 | 0.2539 | ±0.5078 | +1.412 | 0.1580 | 1.4311 |  |
| **Avg. daily time 181-250 (%)** | **+0.0292** | 0.0099 | ±0.0198 | **+2.942** | **0.0033** | 1.0296 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0893**, LLR χ² = **59.22** (p = **1.29e-08**), AUC = **0.7019**, AIC = **628.0**, BIC = **681.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5262 | 0.8057 | ±1.6115 | -1.894 | 0.0582 | 0.2174 | . |
| Education: graduate level (vs college) | -0.3441 | 0.2365 | ±0.4731 | -1.455 | 0.1458 | 0.7089 |  |
| Education: high school or below (vs college) | +0.3021 | 0.3227 | ±0.6453 | +0.936 | 0.3491 | 1.3527 |  |
| Site: UCSD (vs UAB) | +0.2381 | 0.2727 | ±0.5454 | +0.873 | 0.3826 | 1.2688 |  |
| Site: UW (vs UAB) | +0.1168 | 0.2443 | ±0.4886 | +0.478 | 0.6326 | 1.1239 |  |
| **Age (years)** | **-0.0268** | 0.0104 | ±0.0208 | **-2.582** | **0.0098** | 0.9736 | ** |
| **BMI (kg/m2)** | **+0.0458** | 0.0130 | ±0.0260 | **+3.528** | **4.18e-04** | 1.0469 | *** |
| Hypertension | -0.1563 | 0.2325 | ±0.4649 | -0.672 | 0.5013 | 0.8553 |  |
| High cholesterol | +0.1864 | 0.2167 | ±0.4335 | +0.860 | 0.3899 | 1.2048 |  |
| Kidney disease | +0.4737 | 0.3213 | ±0.6426 | +1.474 | 0.1404 | 1.6059 |  |
| Circulatory disease | +0.3454 | 0.2558 | ±0.5115 | +1.350 | 0.1769 | 1.4125 |  |
| **Time > 180 (%)** | **+0.0260** | 0.0071 | ±0.0143 | **+3.646** | **2.66e-04** | 1.0264 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0894**, LLR χ² = **59.27** (p = **1.27e-08**), AUC = **0.7028**, AIC = **628.0**, BIC = **681.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5253 | 0.8058 | ±1.6117 | -1.893 | 0.0584 | 0.2175 | . |
| Education: graduate level (vs college) | -0.3455 | 0.2366 | ±0.4732 | -1.460 | 0.1442 | 0.7079 |  |
| Education: high school or below (vs college) | +0.2966 | 0.3230 | ±0.6459 | +0.918 | 0.3584 | 1.3453 |  |
| Site: UCSD (vs UAB) | +0.2410 | 0.2728 | ±0.5456 | +0.883 | 0.3770 | 1.2725 |  |
| Site: UW (vs UAB) | +0.1180 | 0.2443 | ±0.4886 | +0.483 | 0.6291 | 1.1252 |  |
| **Age (years)** | **-0.0268** | 0.0104 | ±0.0208 | **-2.583** | **0.0098** | 0.9735 | ** |
| **BMI (kg/m2)** | **+0.0459** | 0.0130 | ±0.0260 | **+3.534** | **4.10e-04** | 1.0469 | *** |
| Hypertension | -0.1529 | 0.2323 | ±0.4646 | -0.658 | 0.5104 | 0.8582 |  |
| High cholesterol | +0.1840 | 0.2168 | ±0.4335 | +0.849 | 0.3959 | 1.2020 |  |
| Kidney disease | +0.4666 | 0.3220 | ±0.6440 | +1.449 | 0.1473 | 1.5946 |  |
| Circulatory disease | +0.3464 | 0.2558 | ±0.5116 | +1.354 | 0.1757 | 1.4140 |  |
| **Avg. daily time > 180 (%)** | **+0.0261** | 0.0071 | ±0.0142 | **+3.661** | **2.51e-04** | 1.0264 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.1027**, LLR χ² = **68.09** (p = **2.81e-10**), AUC = **0.7167**, AIC = **619.2**, BIC = **672.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5435 | 0.8113 | ±1.6227 | -1.902 | 0.0571 | 0.2136 | . |
| Education: graduate level (vs college) | -0.3199 | 0.2381 | ±0.4762 | -1.344 | 0.1791 | 0.7262 |  |
| Education: high school or below (vs college) | +0.3213 | 0.3243 | ±0.6485 | +0.991 | 0.3218 | 1.3789 |  |
| Site: UCSD (vs UAB) | +0.2731 | 0.2759 | ±0.5518 | +0.990 | 0.3222 | 1.3141 |  |
| Site: UW (vs UAB) | +0.1294 | 0.2463 | ±0.4926 | +0.525 | 0.5995 | 1.1381 |  |
| **Age (years)** | **-0.0261** | 0.0105 | ±0.0209 | **-2.496** | **0.0126** | 0.9742 | * |
| **BMI (kg/m2)** | **+0.0450** | 0.0131 | ±0.0261 | **+3.444** | **5.74e-04** | 1.0460 | *** |
| Hypertension | -0.1856 | 0.2349 | ±0.4698 | -0.790 | 0.4295 | 0.8306 |  |
| High cholesterol | +0.1731 | 0.2196 | ±0.4391 | +0.788 | 0.4306 | 1.1889 |  |
| Kidney disease | +0.5676 | 0.3208 | ±0.6417 | +1.769 | 0.0769 | 1.7641 | . |
| Circulatory disease | +0.3449 | 0.2599 | ±0.5197 | +1.327 | 0.1845 | 1.4118 |  |
| **Nocturnal time > 180 (%)** | **+0.0352** | 0.0080 | ±0.0160 | **+4.414** | **1.02e-05** | 1.0359 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0810**, LLR χ² = **53.75** (p = **1.31e-07**), AUC = **0.6965**, AIC = **633.5**, BIC = **687.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4927 | 0.8030 | ±1.6060 | -1.859 | 0.0630 | 0.2248 | . |
| Education: graduate level (vs college) | -0.3364 | 0.2355 | ±0.4711 | -1.428 | 0.1533 | 0.7143 |  |
| Education: high school or below (vs college) | +0.3420 | 0.3178 | ±0.6357 | +1.076 | 0.2820 | 1.4077 |  |
| Site: UCSD (vs UAB) | +0.2142 | 0.2694 | ±0.5387 | +0.795 | 0.4264 | 1.2389 |  |
| Site: UW (vs UAB) | +0.0600 | 0.2424 | ±0.4848 | +0.248 | 0.8045 | 1.0619 |  |
| **Age (years)** | **-0.0288** | 0.0105 | ±0.0209 | **-2.753** | **0.0059** | 0.9716 | ** |
| **BMI (kg/m2)** | **+0.0480** | 0.0129 | ±0.0259 | **+3.706** | **2.10e-04** | 1.0491 | *** |
| Hypertension | -0.1379 | 0.2315 | ±0.4631 | -0.595 | 0.5516 | 0.8712 |  |
| High cholesterol | +0.2061 | 0.2154 | ±0.4307 | +0.957 | 0.3387 | 1.2288 |  |
| Kidney disease | +0.4892 | 0.3200 | ±0.6401 | +1.529 | 0.1263 | 1.6311 |  |
| Circulatory disease | +0.3716 | 0.2535 | ±0.5070 | +1.466 | 0.1427 | 1.4500 |  |
| **Any reading > 250 during wear (0/1)** | **+0.6383** | 0.2216 | ±0.4431 | **+2.881** | **0.0040** | 1.8932 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0935**, LLR χ² = **62.00** (p = **3.94e-09**), AUC = **0.7009**, AIC = **625.2**, BIC = **678.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5709 | 0.8078 | ±1.6155 | -1.945 | 0.0518 | 0.2079 | . |
| Education: graduate level (vs college) | -0.3346 | 0.2361 | ±0.4722 | -1.417 | 0.1565 | 0.7156 |  |
| Education: high school or below (vs college) | +0.2675 | 0.3300 | ±0.6601 | +0.810 | 0.4177 | 1.3067 |  |
| Site: UCSD (vs UAB) | +0.2531 | 0.2733 | ±0.5467 | +0.926 | 0.3544 | 1.2881 |  |
| Site: UW (vs UAB) | +0.1288 | 0.2445 | ±0.4891 | +0.527 | 0.5984 | 1.1375 |  |
| **Age (years)** | **-0.0258** | 0.0104 | ±0.0208 | **-2.482** | **0.0131** | 0.9745 | * |
| **BMI (kg/m2)** | **+0.0469** | 0.0130 | ±0.0260 | **+3.612** | **3.04e-04** | 1.0480 | *** |
| Hypertension | -0.1459 | 0.2322 | ±0.4645 | -0.628 | 0.5299 | 0.8643 |  |
| High cholesterol | +0.2409 | 0.2177 | ±0.4354 | +1.106 | 0.2686 | 1.2723 |  |
| Kidney disease | +0.5250 | 0.3212 | ±0.6424 | +1.634 | 0.1022 | 1.6904 |  |
| Circulatory disease | +0.3464 | 0.2571 | ±0.5142 | +1.347 | 0.1779 | 1.4139 |  |
| **Time > 250 (%)** | **+0.0759** | 0.0250 | ±0.0500 | **+3.039** | **0.0024** | 1.0789 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0939**, LLR χ² = **62.26** (p = **3.52e-09**), AUC = **0.7011**, AIC = **625.0**, BIC = **678.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5575 | 0.8079 | ±1.6159 | -1.928 | 0.0539 | 0.2107 | . |
| Education: graduate level (vs college) | -0.3322 | 0.2360 | ±0.4721 | -1.407 | 0.1593 | 0.7174 |  |
| Education: high school or below (vs college) | +0.2453 | 0.3321 | ±0.6642 | +0.739 | 0.4602 | 1.2779 |  |
| Site: UCSD (vs UAB) | +0.2525 | 0.2739 | ±0.5478 | +0.922 | 0.3566 | 1.2873 |  |
| Site: UW (vs UAB) | +0.1263 | 0.2445 | ±0.4890 | +0.517 | 0.6053 | 1.1347 |  |
| **Age (years)** | **-0.0262** | 0.0104 | ±0.0209 | **-2.510** | **0.0121** | 0.9742 | * |
| **BMI (kg/m2)** | **+0.0472** | 0.0130 | ±0.0260 | **+3.630** | **2.83e-04** | 1.0483 | *** |
| Hypertension | -0.1469 | 0.2323 | ±0.4646 | -0.633 | 0.5270 | 0.8634 |  |
| High cholesterol | +0.2369 | 0.2178 | ±0.4357 | +1.088 | 0.2768 | 1.2673 |  |
| Kidney disease | +0.5056 | 0.3225 | ±0.6451 | +1.568 | 0.1170 | 1.6580 |  |
| Circulatory disease | +0.3475 | 0.2575 | ±0.5151 | +1.349 | 0.1772 | 1.4156 |  |
| **Avg. daily time > 250 (%)** | **+0.0836** | 0.0263 | ±0.0527 | **+3.176** | **0.0015** | 1.0872 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
