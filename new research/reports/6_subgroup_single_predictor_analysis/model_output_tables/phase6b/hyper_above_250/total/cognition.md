# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Total analysis base - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 795; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **795**, R² = **0.0793**, Adj R² = **0.0676**, F-statistic = **6.75** (p = **3.88e-10**), Residual SE = **3.383** on **784** df, AIC = **4204.8**, BIC = **4256.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0899** | 0.9844 | ±1.9688 | **+27.520** | **1.02e-166** | *** |
| **Education: graduate level (vs college)** | **+0.7966** | 0.2549 | ±0.5097 | **+3.125** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.6132** | 0.4541 | ±0.9082 | **-3.552** | **3.82e-04** | *** |
| Site: UCSD (vs UAB) | -0.4737 | 0.3187 | ±0.6374 | -1.486 | 0.1372 |  |
| Site: UW (vs UAB) | +0.0409 | 0.2979 | ±0.5958 | +0.137 | 0.8907 |  |
| **Age (years)** | **-0.0383** | 0.0123 | ±0.0245 | **-3.126** | **0.0018** | ** |
| BMI (kg/m2) | +0.0219 | 0.0165 | ±0.0330 | +1.326 | 0.1848 |  |
| **Hypertension** | **-0.7680** | 0.2768 | ±0.5536 | **-2.774** | **0.0055** | ** |
| High cholesterol | +0.3390 | 0.2650 | ±0.5299 | +1.280 | 0.2007 |  |
| Kidney disease | +0.4213 | 0.3604 | ±0.7208 | +1.169 | 0.2424 |  |
| Circulatory disease | +0.1179 | 0.3020 | ±0.6041 | +0.390 | 0.6963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **795**, R² = **0.0858**, Adj R² = **0.0729**, F-statistic = **6.68** (p = **9.27e-11**), Residual SE = **3.373** on **783** df, AIC = **4201.1**, BIC = **4257.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4034** | 1.1633 | ±2.3266 | **+24.417** | **1.14e-131** | *** |
| **Education: graduate level (vs college)** | **+0.7522** | 0.2556 | ±0.5112 | **+2.943** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **-1.4957** | 0.4560 | ±0.9120 | **-3.280** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.5081 | 0.3201 | ±0.6402 | -1.587 | 0.1125 |  |
| Site: UW (vs UAB) | -0.0144 | 0.2995 | ±0.5991 | -0.048 | 0.9616 |  |
| **Age (years)** | **-0.0389** | 0.0122 | ±0.0245 | **-3.183** | **0.0015** | ** |
| BMI (kg/m2) | +0.0285 | 0.0168 | ±0.0337 | +1.693 | 0.0904 | . |
| **Hypertension** | **-0.7393** | 0.2760 | ±0.5519 | **-2.679** | **0.0074** | ** |
| High cholesterol | +0.3638 | 0.2648 | ±0.5297 | +1.374 | 0.1695 |  |
| Kidney disease | +0.4291 | 0.3600 | ±0.7200 | +1.192 | 0.2334 |  |
| Circulatory disease | +0.1604 | 0.3008 | ±0.6015 | +0.533 | 0.5938 |  |
| **HbA1c (%)** | **-0.2192** | 0.0921 | ±0.1842 | **-2.380** | **0.0173** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **795**, R² = **0.0892**, Adj R² = **0.0764**, F-statistic = **6.97** (p = **2.55e-11**), Residual SE = **3.367** on **783** df, AIC = **4198.2**, BIC = **4254.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.3890** | 1.1111 | ±2.2222 | **+25.551** | **5.38e-144** | *** |
| **Education: graduate level (vs college)** | **+0.7675** | 0.2545 | ±0.5090 | **+3.016** | **0.0026** | ** |
| **Education: high school or below (vs college)** | **-1.4781** | 0.4545 | ±0.9090 | **-3.252** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5381 | 0.3204 | ±0.6408 | -1.679 | 0.0931 | . |
| Site: UW (vs UAB) | -0.0233 | 0.2989 | ±0.5978 | -0.078 | 0.9380 |  |
| **Age (years)** | **-0.0394** | 0.0123 | ±0.0245 | **-3.212** | **0.0013** | ** |
| BMI (kg/m2) | +0.0289 | 0.0168 | ±0.0336 | +1.722 | 0.0851 | . |
| **Hypertension** | **-0.7426** | 0.2756 | ±0.5511 | **-2.695** | **0.0070** | ** |
| High cholesterol | +0.3541 | 0.2637 | ±0.5275 | +1.343 | 0.1794 |  |
| Kidney disease | +0.4744 | 0.3615 | ±0.7229 | +1.313 | 0.1893 |  |
| Circulatory disease | +0.1796 | 0.2950 | ±0.5899 | +0.609 | 0.5425 |  |
| **Mean glucose (mg/dL)** | **-0.0090** | 0.0032 | ±0.0064 | **-2.816** | **0.0049** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **795**, R² = **0.0892**, Adj R² = **0.0764**, F-statistic = **6.97** (p = **2.55e-11**), Residual SE = **3.367** on **783** df, AIC = **4198.2**, BIC = **4254.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6350** | 1.3725 | ±2.7451 | **+21.591** | **2.16e-103** | *** |
| **Education: graduate level (vs college)** | **+0.7675** | 0.2545 | ±0.5090 | **+3.016** | **0.0026** | ** |
| **Education: high school or below (vs college)** | **-1.4781** | 0.4545 | ±0.9090 | **-3.252** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5381 | 0.3204 | ±0.6408 | -1.679 | 0.0931 | . |
| Site: UW (vs UAB) | -0.0233 | 0.2989 | ±0.5978 | -0.078 | 0.9380 |  |
| **Age (years)** | **-0.0394** | 0.0123 | ±0.0245 | **-3.212** | **0.0013** | ** |
| BMI (kg/m2) | +0.0289 | 0.0168 | ±0.0336 | +1.722 | 0.0851 | . |
| **Hypertension** | **-0.7426** | 0.2756 | ±0.5511 | **-2.695** | **0.0070** | ** |
| High cholesterol | +0.3541 | 0.2637 | ±0.5275 | +1.343 | 0.1794 |  |
| Kidney disease | +0.4744 | 0.3615 | ±0.7229 | +1.313 | 0.1893 |  |
| Circulatory disease | +0.1796 | 0.2950 | ±0.5899 | +0.609 | 0.5425 |  |
| **GMI (%)** | **-0.3764** | 0.1337 | ±0.2673 | **-2.816** | **0.0049** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **795**, R² = **0.0881**, Adj R² = **0.0752**, F-statistic = **6.87** (p = **3.93e-11**), Residual SE = **3.369** on **783** df, AIC = **4199.2**, BIC = **4255.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.2111** | 1.0948 | ±2.1896 | **+25.769** | **1.99e-146** | *** |
| **Education: graduate level (vs college)** | **+0.7575** | 0.2541 | ±0.5082 | **+2.981** | **0.0029** | ** |
| **Education: high school or below (vs college)** | **-1.5013** | 0.4537 | ±0.9075 | **-3.309** | **9.37e-04** | *** |
| Site: UCSD (vs UAB) | -0.5317 | 0.3207 | ±0.6414 | -1.658 | 0.0973 | . |
| Site: UW (vs UAB) | +0.0003 | 0.2983 | ±0.5967 | +0.001 | 0.9991 |  |
| **Age (years)** | **-0.0405** | 0.0124 | ±0.0247 | **-3.275** | **0.0011** | ** |
| BMI (kg/m2) | +0.0303 | 0.0170 | ±0.0339 | +1.783 | 0.0746 | . |
| **Hypertension** | **-0.7518** | 0.2757 | ±0.5514 | **-2.727** | **0.0064** | ** |
| High cholesterol | +0.3499 | 0.2636 | ±0.5273 | +1.327 | 0.1844 |  |
| Kidney disease | +0.4405 | 0.3588 | ±0.7176 | +1.228 | 0.2196 |  |
| Circulatory disease | +0.1712 | 0.2962 | ±0.5924 | +0.578 | 0.5633 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0080** | 0.0030 | ±0.0060 | **-2.645** | **0.0082** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **795**, R² = **0.0886**, Adj R² = **0.0758**, F-statistic = **6.92** (p = **3.21e-11**), Residual SE = **3.368** on **783** df, AIC = **4198.7**, BIC = **4254.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.0116** | 1.0468 | ±2.0936 | **+26.760** | **9.52e-158** | *** |
| **Education: graduate level (vs college)** | **+0.7500** | 0.2548 | ±0.5097 | **+2.943** | **0.0032** | ** |
| **Education: high school or below (vs college)** | **-1.5104** | 0.4507 | ±0.9013 | **-3.351** | **8.04e-04** | *** |
| Site: UCSD (vs UAB) | -0.5319 | 0.3209 | ±0.6419 | -1.657 | 0.0975 | . |
| Site: UW (vs UAB) | -0.0624 | 0.3046 | ±0.6093 | -0.205 | 0.8378 |  |
| **Age (years)** | **-0.0380** | 0.0123 | ±0.0246 | **-3.096** | **0.0020** | ** |
| BMI (kg/m2) | +0.0279 | 0.0167 | ±0.0334 | +1.673 | 0.0942 | . |
| **Hypertension** | **-0.7265** | 0.2754 | ±0.5507 | **-2.638** | **0.0083** | ** |
| High cholesterol | +0.3279 | 0.2625 | ±0.5251 | +1.249 | 0.2118 |  |
| Kidney disease | +0.5997 | 0.3608 | ±0.7216 | +1.662 | 0.0965 | . |
| Circulatory disease | +0.1665 | 0.2982 | ±0.5964 | +0.558 | 0.5765 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0294** | 0.0102 | ±0.0204 | **-2.874** | **0.0040** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **795**, R² = **0.0878**, Adj R² = **0.0749**, F-statistic = **6.85** (p = **4.41e-11**), Residual SE = **3.369** on **783** df, AIC = **4199.4**, BIC = **4255.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.0001** | 1.0455 | ±2.0911 | **+26.781** | **5.41e-158** | *** |
| **Education: graduate level (vs college)** | **+0.7624** | 0.2551 | ±0.5101 | **+2.989** | **0.0028** | ** |
| **Education: high school or below (vs college)** | **-1.5058** | 0.4517 | ±0.9035 | **-3.333** | **8.58e-04** | *** |
| Site: UCSD (vs UAB) | -0.5294 | 0.3206 | ±0.6412 | -1.651 | 0.0987 | . |
| Site: UW (vs UAB) | -0.0486 | 0.3033 | ±0.6066 | -0.160 | 0.8726 |  |
| **Age (years)** | **-0.0377** | 0.0123 | ±0.0246 | **-3.063** | **0.0022** | ** |
| BMI (kg/m2) | +0.0262 | 0.0166 | ±0.0333 | +1.575 | 0.1153 |  |
| **Hypertension** | **-0.7342** | 0.2757 | ±0.5513 | **-2.663** | **0.0077** | ** |
| High cholesterol | +0.3300 | 0.2632 | ±0.5264 | +1.254 | 0.2099 |  |
| Kidney disease | +0.6028 | 0.3627 | ±0.7254 | +1.662 | 0.0965 | . |
| Circulatory disease | +0.1573 | 0.2998 | ±0.5996 | +0.525 | 0.5998 |  |
| **Avg. daily SD (mg/dL)** | **-0.0317** | 0.0117 | ±0.0234 | **-2.717** | **0.0066** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **795**, R² = **0.0795**, Adj R² = **0.0665**, F-statistic = **6.15** (p = **9.83e-10**), Residual SE = **3.385** on **783** df, AIC = **4206.6**, BIC = **4262.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2850** | 1.0765 | ±2.1530 | **+25.347** | **9.81e-142** | *** |
| **Education: graduate level (vs college)** | **+0.7912** | 0.2553 | ±0.5106 | **+3.099** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **-1.6115** | 0.4545 | ±0.9090 | **-3.546** | **3.92e-04** | *** |
| Site: UCSD (vs UAB) | -0.4783 | 0.3205 | ±0.6411 | -1.492 | 0.1356 |  |
| Site: UW (vs UAB) | +0.0291 | 0.3039 | ±0.6077 | +0.096 | 0.9237 |  |
| **Age (years)** | **-0.0381** | 0.0124 | ±0.0247 | **-3.083** | **0.0020** | ** |
| BMI (kg/m2) | +0.0221 | 0.0165 | ±0.0330 | +1.337 | 0.1811 |  |
| **Hypertension** | **-0.7629** | 0.2766 | ±0.5532 | **-2.758** | **0.0058** | ** |
| High cholesterol | +0.3335 | 0.2653 | ±0.5307 | +1.257 | 0.2089 |  |
| Kidney disease | +0.4471 | 0.3605 | ±0.7210 | +1.240 | 0.2149 |  |
| Circulatory disease | +0.1187 | 0.3026 | ±0.6052 | +0.392 | 0.6950 |  |
| CV (%) | -0.0089 | 0.0209 | ±0.0417 | -0.428 | 0.6688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **795**, R² = **0.0799**, Adj R² = **0.0670**, F-statistic = **6.18** (p = **8.38e-10**), Residual SE = **3.384** on **783** df, AIC = **4206.2**, BIC = **4262.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6696** | 1.1411 | ±2.2822 | **+23.372** | **8.17e-121** | *** |
| **Education: graduate level (vs college)** | **+0.7883** | 0.2552 | ±0.5105 | **+3.089** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **-1.6109** | 0.4545 | ±0.9089 | **-3.545** | **3.93e-04** | *** |
| Site: UCSD (vs UAB) | -0.4769 | 0.3191 | ±0.6383 | -1.494 | 0.1351 |  |
| Site: UW (vs UAB) | +0.0229 | 0.3021 | ±0.6042 | +0.076 | 0.9396 |  |
| **Age (years)** | **-0.0380** | 0.0123 | ±0.0247 | **-3.080** | **0.0021** | ** |
| BMI (kg/m2) | +0.0220 | 0.0165 | ±0.0330 | +1.334 | 0.1822 |  |
| **Hypertension** | **-0.7591** | 0.2763 | ±0.5526 | **-2.748** | **0.0060** | ** |
| High cholesterol | +0.3339 | 0.2651 | ±0.5302 | +1.260 | 0.2078 |  |
| Kidney disease | +0.4611 | 0.3588 | ±0.7176 | +1.285 | 0.1987 |  |
| Circulatory disease | +0.1230 | 0.3034 | ±0.6068 | +0.406 | 0.6851 |  |
| Mean / SD ratio | +0.0895 | 0.1167 | ±0.2335 | +0.766 | 0.4434 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **795**, R² = **0.0794**, Adj R² = **0.0665**, F-statistic = **6.14** (p = **1.01e-09**), Residual SE = **3.385** on **783** df, AIC = **4206.7**, BIC = **4262.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.9319** | 1.1502 | ±2.3004 | **+23.415** | **2.98e-121** | *** |
| **Education: graduate level (vs college)** | **+0.7940** | 0.2558 | ±0.5117 | **+3.104** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **-1.6119** | 0.4546 | ±0.9093 | **-3.546** | **3.92e-04** | *** |
| Site: UCSD (vs UAB) | -0.4743 | 0.3191 | ±0.6382 | -1.486 | 0.1372 |  |
| Site: UW (vs UAB) | +0.0347 | 0.3010 | ±0.6020 | +0.115 | 0.9082 |  |
| **Age (years)** | **-0.0381** | 0.0124 | ±0.0248 | **-3.081** | **0.0021** | ** |
| BMI (kg/m2) | +0.0218 | 0.0165 | ±0.0331 | +1.318 | 0.1876 |  |
| **Hypertension** | **-0.7648** | 0.2767 | ±0.5535 | **-2.764** | **0.0057** | ** |
| High cholesterol | +0.3364 | 0.2657 | ±0.5313 | +1.266 | 0.2055 |  |
| Kidney disease | +0.4364 | 0.3607 | ±0.7215 | +1.210 | 0.2264 |  |
| Circulatory disease | +0.1181 | 0.3031 | ±0.6063 | +0.390 | 0.6968 |  |
| Avg. daily mean/SD | +0.0288 | 0.1008 | ±0.2015 | +0.286 | 0.7750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **795**, R² = **0.0841**, Adj R² = **0.0713**, F-statistic = **6.54** (p = **1.74e-10**), Residual SE = **3.376** on **783** df, AIC = **4202.6**, BIC = **4258.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4342** | 1.1733 | ±2.3465 | **+24.235** | **9.52e-130** | *** |
| **Education: graduate level (vs college)** | **+0.7524** | 0.2579 | ±0.5159 | **+2.917** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **-1.5886** | 0.4490 | ±0.8980 | **-3.538** | **4.03e-04** | *** |
| Site: UCSD (vs UAB) | -0.5254 | 0.3207 | ±0.6415 | -1.638 | 0.1014 |  |
| Site: UW (vs UAB) | -0.0623 | 0.3060 | ±0.6121 | -0.204 | 0.8387 |  |
| **Age (years)** | **-0.0404** | 0.0122 | ±0.0245 | **-3.299** | **9.70e-04** | *** |
| BMI (kg/m2) | +0.0237 | 0.0165 | ±0.0331 | +1.432 | 0.1523 |  |
| **Hypertension** | **-0.7826** | 0.2778 | ±0.5556 | **-2.817** | **0.0048** | ** |
| High cholesterol | +0.3001 | 0.2647 | ±0.5294 | +1.134 | 0.2568 |  |
| Kidney disease | +0.4766 | 0.3681 | ±0.7363 | +1.295 | 0.1955 |  |
| Circulatory disease | +0.1307 | 0.3008 | ±0.6016 | +0.435 | 0.6639 |  |
| MAG (mg/dL/h) | -0.0261 | 0.0134 | ±0.0268 | -1.950 | 0.0512 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **795**, R² = **0.0849**, Adj R² = **0.0720**, F-statistic = **6.60** (p = **1.31e-10**), Residual SE = **3.375** on **783** df, AIC = **4201.9**, BIC = **4258.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.2233** | 1.1229 | ±2.2458 | **+25.134** | **2.13e-139** | *** |
| **Education: graduate level (vs college)** | **+0.7689** | 0.2556 | ±0.5113 | **+3.008** | **0.0026** | ** |
| **Education: high school or below (vs college)** | **-1.5287** | 0.4529 | ±0.9057 | **-3.375** | **7.37e-04** | *** |
| Site: UCSD (vs UAB) | -0.5295 | 0.3216 | ±0.6433 | -1.646 | 0.0997 | . |
| Site: UW (vs UAB) | -0.0383 | 0.3043 | ±0.6086 | -0.126 | 0.8998 |  |
| **Age (years)** | **-0.0388** | 0.0123 | ±0.0246 | **-3.155** | **0.0016** | ** |
| BMI (kg/m2) | +0.0243 | 0.0166 | ±0.0331 | +1.464 | 0.1431 |  |
| **Hypertension** | **-0.7587** | 0.2762 | ±0.5524 | **-2.747** | **0.0060** | ** |
| High cholesterol | +0.3260 | 0.2640 | ±0.5280 | +1.235 | 0.2169 |  |
| Kidney disease | +0.5658 | 0.3642 | ±0.7283 | +1.554 | 0.1202 |  |
| Circulatory disease | +0.1526 | 0.3011 | ±0.6021 | +0.507 | 0.6121 |  |
| **Avg. daily range (mg/dL)** | **-0.0076** | 0.0036 | ±0.0072 | **-2.117** | **0.0342** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **795**, R² = **0.0840**, Adj R² = **0.0711**, F-statistic = **6.53** (p = **1.83e-10**), Residual SE = **3.376** on **783** df, AIC = **4202.7**, BIC = **4258.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.4070** | 1.0115 | ±2.0229 | **+27.096** | **1.08e-161** | *** |
| **Education: graduate level (vs college)** | **+0.7438** | 0.2540 | ±0.5080 | **+2.928** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **-1.5831** | 0.4498 | ±0.8995 | **-3.520** | **4.32e-04** | *** |
| Site: UCSD (vs UAB) | -0.4995 | 0.3214 | ±0.6429 | -1.554 | 0.1202 |  |
| Site: UW (vs UAB) | -0.0167 | 0.3047 | ±0.6094 | -0.055 | 0.9564 |  |
| **Age (years)** | **-0.0395** | 0.0123 | ±0.0246 | **-3.210** | **0.0013** | ** |
| BMI (kg/m2) | +0.0271 | 0.0166 | ±0.0332 | +1.631 | 0.1029 |  |
| **Hypertension** | **-0.7323** | 0.2761 | ±0.5522 | **-2.652** | **0.0080** | ** |
| High cholesterol | +0.3370 | 0.2636 | ±0.5272 | +1.278 | 0.2011 |  |
| Kidney disease | +0.4752 | 0.3593 | ±0.7186 | +1.322 | 0.1860 |  |
| Circulatory disease | +0.1669 | 0.3000 | ±0.6001 | +0.556 | 0.5781 |  |
| **SD of daily means (mg/dL)** | **-0.0305** | 0.0155 | ±0.0311 | **-1.963** | **0.0496** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **795**, R² = **0.0888**, Adj R² = **0.0760**, F-statistic = **6.93** (p = **3.00e-11**), Residual SE = **3.368** on **783** df, AIC = **4198.6**, BIC = **4254.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.8632** | 1.0559 | ±2.1118 | **+24.494** | **1.70e-132** | *** |
| **Education: graduate level (vs college)** | **+0.7651** | 0.2547 | ±0.5093 | **+3.004** | **0.0027** | ** |
| **Education: high school or below (vs college)** | **-1.4856** | 0.4537 | ±0.9074 | **-3.275** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5487 | 0.3222 | ±0.6445 | -1.703 | 0.0886 | . |
| Site: UW (vs UAB) | -0.0343 | 0.3009 | ±0.6018 | -0.114 | 0.9094 |  |
| **Age (years)** | **-0.0387** | 0.0122 | ±0.0245 | **-3.160** | **0.0016** | ** |
| BMI (kg/m2) | +0.0302 | 0.0168 | ±0.0336 | +1.797 | 0.0724 | . |
| **Hypertension** | **-0.7515** | 0.2756 | ±0.5512 | **-2.727** | **0.0064** | ** |
| High cholesterol | +0.3378 | 0.2629 | ±0.5257 | +1.285 | 0.1987 |  |
| Kidney disease | +0.5008 | 0.3607 | ±0.7214 | +1.388 | 0.1650 |  |
| Circulatory disease | +0.1685 | 0.2957 | ±0.5915 | +0.570 | 0.5689 |  |
| **Time in range 70-180, pooled (%)** | **+0.0141** | 0.0051 | ±0.0102 | **+2.774** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **795**, R² = **0.0884**, Adj R² = **0.0756**, F-statistic = **6.90** (p = **3.50e-11**), Residual SE = **3.368** on **783** df, AIC = **4198.9**, BIC = **4255.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.8829** | 1.0579 | ±2.1158 | **+24.466** | **3.36e-132** | *** |
| **Education: graduate level (vs college)** | **+0.7689** | 0.2547 | ±0.5095 | **+3.018** | **0.0025** | ** |
| **Education: high school or below (vs college)** | **-1.4858** | 0.4541 | ±0.9082 | **-3.272** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5512 | 0.3226 | ±0.6453 | -1.709 | 0.0875 | . |
| Site: UW (vs UAB) | -0.0338 | 0.3011 | ±0.6022 | -0.112 | 0.9105 |  |
| **Age (years)** | **-0.0386** | 0.0122 | ±0.0245 | **-3.149** | **0.0016** | ** |
| BMI (kg/m2) | +0.0301 | 0.0168 | ±0.0336 | +1.792 | 0.0732 | . |
| **Hypertension** | **-0.7530** | 0.2756 | ±0.5513 | **-2.732** | **0.0063** | ** |
| High cholesterol | +0.3384 | 0.2630 | ±0.5260 | +1.287 | 0.1982 |  |
| Kidney disease | +0.5038 | 0.3608 | ±0.7216 | +1.396 | 0.1626 |  |
| Circulatory disease | +0.1667 | 0.2958 | ±0.5917 | +0.563 | 0.5732 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0137** | 0.0051 | ±0.0101 | **+2.705** | **0.0068** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **795**, R² = **0.0802**, Adj R² = **0.0673**, F-statistic = **6.21** (p = **7.46e-10**), Residual SE = **3.383** on **783** df, AIC = **4206.0**, BIC = **4262.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.9986** | 0.9902 | ±1.9804 | **+27.266** | **1.08e-163** | *** |
| **Education: graduate level (vs college)** | **+0.8033** | 0.2548 | ±0.5096 | **+3.153** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.6004** | 0.4582 | ±0.9164 | **-3.493** | **4.78e-04** | *** |
| Site: UCSD (vs UAB) | -0.4604 | 0.3214 | ±0.6428 | -1.432 | 0.1520 |  |
| Site: UW (vs UAB) | +0.0550 | 0.3012 | ±0.6024 | +0.182 | 0.8552 |  |
| **Age (years)** | **-0.0379** | 0.0122 | ±0.0245 | **-3.101** | **0.0019** | ** |
| BMI (kg/m2) | +0.0217 | 0.0165 | ±0.0331 | +1.313 | 0.1892 |  |
| **Hypertension** | **-0.7817** | 0.2776 | ±0.5552 | **-2.816** | **0.0049** | ** |
| High cholesterol | +0.3576 | 0.2673 | ±0.5346 | +1.338 | 0.1809 |  |
| Kidney disease | +0.4176 | 0.3610 | ±0.7220 | +1.157 | 0.2474 |  |
| Circulatory disease | +0.1042 | 0.3027 | ±0.6054 | +0.344 | 0.7306 |  |
| Any reading < 54 during wear (0/1) | +0.2545 | 0.2872 | ±0.5744 | +0.886 | 0.3755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **795**, R² = **0.0811**, Adj R² = **0.0682**, F-statistic = **6.29** (p = **5.30e-10**), Residual SE = **3.382** on **783** df, AIC = **4205.2**, BIC = **4261.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0159** | 0.9851 | ±1.9701 | **+27.425** | **1.37e-165** | *** |
| **Education: graduate level (vs college)** | **+0.8155** | 0.2549 | ±0.5098 | **+3.199** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.5904** | 0.4552 | ±0.9105 | **-3.494** | **4.76e-04** | *** |
| Site: UCSD (vs UAB) | -0.4457 | 0.3197 | ±0.6394 | -1.394 | 0.1632 |  |
| Site: UW (vs UAB) | +0.0750 | 0.2997 | ±0.5993 | +0.250 | 0.8023 |  |
| **Age (years)** | **-0.0388** | 0.0123 | ±0.0245 | **-3.165** | **0.0016** | ** |
| BMI (kg/m2) | +0.0230 | 0.0165 | ±0.0331 | +1.389 | 0.1647 |  |
| **Hypertension** | **-0.7682** | 0.2766 | ±0.5533 | **-2.777** | **0.0055** | ** |
| High cholesterol | +0.3646 | 0.2662 | ±0.5324 | +1.370 | 0.1708 |  |
| Kidney disease | +0.4251 | 0.3603 | ±0.7206 | +1.180 | 0.2380 |  |
| Circulatory disease | +0.1308 | 0.3022 | ±0.6044 | +0.433 | 0.6652 |  |
| **Time < 54 (%)** | **+0.2681** | 0.1296 | ±0.2592 | **+2.068** | **0.0386** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **795**, R² = **0.0803**, Adj R² = **0.0674**, F-statistic = **6.21** (p = **7.26e-10**), Residual SE = **3.383** on **783** df, AIC = **4205.9**, BIC = **4262.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0444** | 0.9855 | ±1.9709 | **+27.443** | **8.41e-166** | *** |
| **Education: graduate level (vs college)** | **+0.8086** | 0.2550 | ±0.5099 | **+3.171** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.5957** | 0.4552 | ±0.9103 | **-3.506** | **4.55e-04** | *** |
| Site: UCSD (vs UAB) | -0.4528 | 0.3197 | ±0.6393 | -1.416 | 0.1566 |  |
| Site: UW (vs UAB) | +0.0691 | 0.3002 | ±0.6005 | +0.230 | 0.8180 |  |
| **Age (years)** | **-0.0386** | 0.0123 | ±0.0246 | **-3.147** | **0.0016** | ** |
| BMI (kg/m2) | +0.0223 | 0.0165 | ±0.0331 | +1.350 | 0.1769 |  |
| **Hypertension** | **-0.7697** | 0.2769 | ±0.5539 | **-2.779** | **0.0054** | ** |
| High cholesterol | +0.3606 | 0.2665 | ±0.5331 | +1.353 | 0.1760 |  |
| Kidney disease | +0.4196 | 0.3604 | ±0.7208 | +1.164 | 0.2443 |  |
| Circulatory disease | +0.1268 | 0.3022 | ±0.6044 | +0.420 | 0.6748 |  |
| Avg. daily time < 54 (%) | +0.2270 | 0.2257 | ±0.4513 | +1.006 | 0.3145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **795**, R² = **0.0795**, Adj R² = **0.0666**, F-statistic = **6.15** (p = **9.76e-10**), Residual SE = **3.385** on **783** df, AIC = **4206.6**, BIC = **4262.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0696** | 0.9871 | ±1.9742 | **+27.423** | **1.45e-165** | *** |
| **Education: graduate level (vs college)** | **+0.8030** | 0.2555 | ±0.5111 | **+3.142** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.6075** | 0.4551 | ±0.9102 | **-3.532** | **4.12e-04** | *** |
| Site: UCSD (vs UAB) | -0.4624 | 0.3206 | ±0.6412 | -1.442 | 0.1492 |  |
| Site: UW (vs UAB) | +0.0535 | 0.3013 | ±0.6026 | +0.178 | 0.8590 |  |
| **Age (years)** | **-0.0385** | 0.0123 | ±0.0246 | **-3.137** | **0.0017** | ** |
| BMI (kg/m2) | +0.0218 | 0.0165 | ±0.0330 | +1.323 | 0.1858 |  |
| **Hypertension** | **-0.7718** | 0.2774 | ±0.5548 | **-2.782** | **0.0054** | ** |
| High cholesterol | +0.3510 | 0.2675 | ±0.5350 | +1.312 | 0.1895 |  |
| Kidney disease | +0.4169 | 0.3614 | ±0.7227 | +1.154 | 0.2486 |  |
| Circulatory disease | +0.1240 | 0.3024 | ±0.6049 | +0.410 | 0.6818 |  |
| Time 54-69, pooled (%) | +0.0488 | 0.0843 | ±0.1686 | +0.578 | 0.5631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **795**, R² = **0.0795**, Adj R² = **0.0665**, F-statistic = **6.14** (p = **9.87e-10**), Residual SE = **3.385** on **783** df, AIC = **4206.6**, BIC = **4262.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0757** | 0.9868 | ±1.9735 | **+27.439** | **9.33e-166** | *** |
| **Education: graduate level (vs college)** | **+0.8031** | 0.2558 | ±0.5116 | **+3.139** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.6073** | 0.4550 | ±0.9101 | **-3.532** | **4.12e-04** | *** |
| Site: UCSD (vs UAB) | -0.4632 | 0.3206 | ±0.6413 | -1.445 | 0.1485 |  |
| Site: UW (vs UAB) | +0.0538 | 0.3015 | ±0.6030 | +0.179 | 0.8583 |  |
| **Age (years)** | **-0.0385** | 0.0123 | ±0.0246 | **-3.138** | **0.0017** | ** |
| BMI (kg/m2) | +0.0218 | 0.0165 | ±0.0330 | +1.320 | 0.1867 |  |
| **Hypertension** | **-0.7715** | 0.2774 | ±0.5548 | **-2.781** | **0.0054** | ** |
| High cholesterol | +0.3506 | 0.2677 | ±0.5353 | +1.310 | 0.1903 |  |
| Kidney disease | +0.4177 | 0.3611 | ±0.7222 | +1.157 | 0.2474 |  |
| Circulatory disease | +0.1243 | 0.3028 | ±0.6055 | +0.411 | 0.6814 |  |
| Avg. daily time 54-69 (%) | +0.0428 | 0.0817 | ±0.1635 | +0.524 | 0.6001 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **795**, R² = **0.0801**, Adj R² = **0.0672**, F-statistic = **6.20** (p = **7.82e-10**), Residual SE = **3.383** on **783** df, AIC = **4206.1**, BIC = **4262.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0396** | 0.9870 | ±1.9740 | **+27.396** | **3.06e-165** | *** |
| **Education: graduate level (vs college)** | **+0.8113** | 0.2555 | ±0.5109 | **+3.176** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.5985** | 0.4555 | ±0.9111 | **-3.509** | **4.50e-04** | *** |
| Site: UCSD (vs UAB) | -0.4493 | 0.3207 | ±0.6414 | -1.401 | 0.1612 |  |
| Site: UW (vs UAB) | +0.0689 | 0.3017 | ±0.6034 | +0.228 | 0.8193 |  |
| **Age (years)** | **-0.0387** | 0.0123 | ±0.0246 | **-3.154** | **0.0016** | ** |
| BMI (kg/m2) | +0.0221 | 0.0165 | ±0.0331 | +1.339 | 0.1806 |  |
| **Hypertension** | **-0.7736** | 0.2773 | ±0.5545 | **-2.790** | **0.0053** | ** |
| High cholesterol | +0.3638 | 0.2678 | ±0.5357 | +1.359 | 0.1743 |  |
| Kidney disease | +0.4158 | 0.3611 | ±0.7222 | +1.152 | 0.2495 |  |
| Circulatory disease | +0.1305 | 0.3024 | ±0.6049 | +0.432 | 0.6661 |  |
| Time < 70 (%) | +0.0727 | 0.0685 | ±0.1370 | +1.061 | 0.2888 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **795**, R² = **0.0797**, Adj R² = **0.0668**, F-statistic = **6.17** (p = **8.95e-10**), Residual SE = **3.384** on **783** df, AIC = **4206.4**, BIC = **4262.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0624** | 0.9867 | ±1.9733 | **+27.428** | **1.27e-165** | *** |
| **Education: graduate level (vs college)** | **+0.8072** | 0.2556 | ±0.5113 | **+3.158** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.6020** | 0.4553 | ±0.9105 | **-3.519** | **4.33e-04** | *** |
| Site: UCSD (vs UAB) | -0.4563 | 0.3206 | ±0.6412 | -1.423 | 0.1547 |  |
| Site: UW (vs UAB) | +0.0629 | 0.3018 | ±0.6035 | +0.209 | 0.8348 |  |
| **Age (years)** | **-0.0386** | 0.0123 | ±0.0246 | **-3.147** | **0.0016** | ** |
| BMI (kg/m2) | +0.0219 | 0.0165 | ±0.0330 | +1.325 | 0.1852 |  |
| **Hypertension** | **-0.7726** | 0.2773 | ±0.5546 | **-2.786** | **0.0053** | ** |
| High cholesterol | +0.3579 | 0.2678 | ±0.5356 | +1.336 | 0.1814 |  |
| Kidney disease | +0.4166 | 0.3610 | ±0.7220 | +1.154 | 0.2485 |  |
| Circulatory disease | +0.1277 | 0.3026 | ±0.6053 | +0.422 | 0.6731 |  |
| Avg. daily time < 70 (%) | +0.0518 | 0.0687 | ±0.1375 | +0.753 | 0.4513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **795**, R² = **0.0869**, Adj R² = **0.0741**, F-statistic = **6.78** (p = **5.99e-11**), Residual SE = **3.371** on **783** df, AIC = **4200.1**, BIC = **4256.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.4158** | 1.1738 | ±2.3476 | **+21.653** | **5.74e-104** | *** |
| **Education: graduate level (vs college)** | **+0.7492** | 0.2551 | ±0.5102 | **+2.937** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **-1.5090** | 0.4540 | ±0.9080 | **-3.324** | **8.88e-04** | *** |
| Site: UCSD (vs UAB) | -0.5331 | 0.3195 | ±0.6390 | -1.668 | 0.0952 | . |
| Site: UW (vs UAB) | -0.0369 | 0.2997 | ±0.5994 | -0.123 | 0.9020 |  |
| **Age (years)** | **-0.0407** | 0.0124 | ±0.0247 | **-3.293** | **9.90e-04** | *** |
| BMI (kg/m2) | +0.0254 | 0.0167 | ±0.0334 | +1.518 | 0.1291 |  |
| **Hypertension** | **-0.7423** | 0.2763 | ±0.5526 | **-2.687** | **0.0072** | ** |
| High cholesterol | +0.3287 | 0.2629 | ±0.5259 | +1.250 | 0.2112 |  |
| Kidney disease | +0.4653 | 0.3622 | ±0.7245 | +1.285 | 0.1989 |  |
| Circulatory disease | +0.1637 | 0.2966 | ±0.5931 | +0.552 | 0.5809 |  |
| **Time 54-250, pooled (%)** | **+0.0189** | 0.0078 | ±0.0155 | **+2.439** | **0.0147** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **795**, R² = **0.0868**, Adj R² = **0.0740**, F-statistic = **6.77** (p = **6.24e-11**), Residual SE = **3.371** on **783** df, AIC = **4200.2**, BIC = **4256.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.3849** | 1.1907 | ±2.3813 | **+21.320** | **7.44e-101** | *** |
| **Education: graduate level (vs college)** | **+0.7504** | 0.2552 | ±0.5103 | **+2.941** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **-1.5097** | 0.4537 | ±0.9074 | **-3.327** | **8.77e-04** | *** |
| Site: UCSD (vs UAB) | -0.5335 | 0.3197 | ±0.6393 | -1.669 | 0.0951 | . |
| Site: UW (vs UAB) | -0.0339 | 0.2995 | ±0.5991 | -0.113 | 0.9098 |  |
| **Age (years)** | **-0.0404** | 0.0123 | ±0.0247 | **-3.274** | **0.0011** | ** |
| BMI (kg/m2) | +0.0255 | 0.0167 | ±0.0335 | +1.521 | 0.1282 |  |
| **Hypertension** | **-0.7442** | 0.2762 | ±0.5525 | **-2.694** | **0.0071** | ** |
| High cholesterol | +0.3287 | 0.2629 | ±0.5259 | +1.250 | 0.2113 |  |
| Kidney disease | +0.4697 | 0.3624 | ±0.7249 | +1.296 | 0.1950 |  |
| Circulatory disease | +0.1660 | 0.2965 | ±0.5931 | +0.560 | 0.5757 |  |
| **Avg. daily time 54-250 (%)** | **+0.0190** | 0.0080 | ±0.0159 | **+2.385** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **795**, R² = **0.0837**, Adj R² = **0.0708**, F-statistic = **6.50** (p = **2.03e-10**), Residual SE = **3.377** on **783** df, AIC = **4203.0**, BIC = **4259.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.1071** | 0.9831 | ±1.9663 | **+27.572** | **2.40e-167** | *** |
| **Education: graduate level (vs college)** | **+0.8031** | 0.2553 | ±0.5106 | **+3.145** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.5538** | 0.4550 | ±0.9100 | **-3.415** | **6.38e-04** | *** |
| Site: UCSD (vs UAB) | -0.5053 | 0.3217 | ±0.6433 | -1.571 | 0.1162 |  |
| Site: UW (vs UAB) | +0.0253 | 0.2988 | ±0.5975 | +0.085 | 0.9324 |  |
| **Age (years)** | **-0.0368** | 0.0122 | ±0.0245 | **-3.006** | **0.0026** | ** |
| BMI (kg/m2) | +0.0284 | 0.0167 | ±0.0334 | +1.700 | 0.0892 | . |
| **Hypertension** | **-0.7724** | 0.2764 | ±0.5529 | **-2.794** | **0.0052** | ** |
| High cholesterol | +0.3505 | 0.2648 | ±0.5296 | +1.324 | 0.1856 |  |
| Kidney disease | +0.4736 | 0.3586 | ±0.7172 | +1.321 | 0.1866 |  |
| Circulatory disease | +0.1389 | 0.3003 | ±0.6007 | +0.462 | 0.6438 |  |
| Time 181-250, pooled (%) | -0.0162 | 0.0085 | ±0.0170 | -1.912 | 0.0559 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **795**, R² = **0.0835**, Adj R² = **0.0706**, F-statistic = **6.48** (p = **2.23e-10**), Residual SE = **3.377** on **783** df, AIC = **4203.2**, BIC = **4259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.1104** | 0.9839 | ±1.9679 | **+27.553** | **4.07e-167** | *** |
| **Education: graduate level (vs college)** | **+0.8053** | 0.2554 | ±0.5109 | **+3.152** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.5515** | 0.4557 | ±0.9114 | **-3.405** | **6.62e-04** | *** |
| Site: UCSD (vs UAB) | -0.5087 | 0.3221 | ±0.6441 | -1.580 | 0.1142 |  |
| Site: UW (vs UAB) | +0.0221 | 0.2992 | ±0.5984 | +0.074 | 0.9410 |  |
| **Age (years)** | **-0.0370** | 0.0122 | ±0.0245 | **-3.022** | **0.0025** | ** |
| BMI (kg/m2) | +0.0282 | 0.0167 | ±0.0335 | +1.687 | 0.0915 | . |
| **Hypertension** | **-0.7717** | 0.2764 | ±0.5528 | **-2.792** | **0.0052** | ** |
| High cholesterol | +0.3509 | 0.2649 | ±0.5299 | +1.325 | 0.1853 |  |
| Kidney disease | +0.4738 | 0.3586 | ±0.7172 | +1.321 | 0.1865 |  |
| Circulatory disease | +0.1362 | 0.3004 | ±0.6008 | +0.453 | 0.6504 |  |
| Avg. daily time 181-250 (%) | -0.0155 | 0.0084 | ±0.0167 | -1.852 | 0.0641 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **795**, R² = **0.0889**, Adj R² = **0.0761**, F-statistic = **6.95** (p = **2.83e-11**), Residual SE = **3.367** on **783** df, AIC = **4198.4**, BIC = **4254.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2636** | 0.9890 | ±1.9781 | **+27.566** | **2.86e-167** | *** |
| **Education: graduate level (vs college)** | **+0.7679** | 0.2546 | ±0.5092 | **+3.016** | **0.0026** | ** |
| **Education: high school or below (vs college)** | **-1.4828** | 0.4540 | ±0.9080 | **-3.266** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5439 | 0.3217 | ±0.6434 | -1.691 | 0.0909 | . |
| Site: UW (vs UAB) | -0.0288 | 0.3003 | ±0.6007 | -0.096 | 0.9236 |  |
| **Age (years)** | **-0.0387** | 0.0122 | ±0.0245 | **-3.167** | **0.0015** | ** |
| BMI (kg/m2) | +0.0302 | 0.0168 | ±0.0336 | +1.799 | 0.0719 | . |
| **Hypertension** | **-0.7526** | 0.2755 | ±0.5511 | **-2.731** | **0.0063** | ** |
| High cholesterol | +0.3426 | 0.2631 | ±0.5262 | +1.302 | 0.1928 |  |
| Kidney disease | +0.4997 | 0.3606 | ±0.7213 | +1.386 | 0.1658 |  |
| Circulatory disease | +0.1709 | 0.2957 | ±0.5914 | +0.578 | 0.5633 |  |
| **Time > 180 (%)** | **-0.0141** | 0.0050 | ±0.0101 | **-2.800** | **0.0051** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **795**, R² = **0.0885**, Adj R² = **0.0757**, F-statistic = **6.91** (p = **3.37e-11**), Residual SE = **3.368** on **783** df, AIC = **4198.8**, BIC = **4255.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2456** | 0.9893 | ±1.9786 | **+27.540** | **5.78e-167** | *** |
| **Education: graduate level (vs college)** | **+0.7717** | 0.2547 | ±0.5094 | **+3.030** | **0.0024** | ** |
| **Education: high school or below (vs college)** | **-1.4831** | 0.4544 | ±0.9088 | **-3.264** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5465 | 0.3221 | ±0.6442 | -1.697 | 0.0898 | . |
| Site: UW (vs UAB) | -0.0279 | 0.3005 | ±0.6010 | -0.093 | 0.9260 |  |
| **Age (years)** | **-0.0386** | 0.0122 | ±0.0245 | **-3.156** | **0.0016** | ** |
| BMI (kg/m2) | +0.0301 | 0.0168 | ±0.0336 | +1.791 | 0.0733 | . |
| **Hypertension** | **-0.7542** | 0.2756 | ±0.5512 | **-2.737** | **0.0062** | ** |
| High cholesterol | +0.3434 | 0.2633 | ±0.5266 | +1.304 | 0.1921 |  |
| Kidney disease | +0.5025 | 0.3607 | ±0.7214 | +1.393 | 0.1636 |  |
| Circulatory disease | +0.1692 | 0.2958 | ±0.5917 | +0.572 | 0.5674 |  |
| **Avg. daily time > 180 (%)** | **-0.0137** | 0.0050 | ±0.0100 | **-2.724** | **0.0065** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **795**, R² = **0.0882**, Adj R² = **0.0754**, F-statistic = **6.89** (p = **3.72e-11**), Residual SE = **3.369** on **783** df, AIC = **4199.0**, BIC = **4255.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.1927** | 0.9866 | ±1.9731 | **+27.563** | **3.09e-167** | *** |
| **Education: graduate level (vs college)** | **+0.7450** | 0.2537 | ±0.5075 | **+2.936** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **-1.5111** | 0.4530 | ±0.9061 | **-3.335** | **8.52e-04** | *** |
| Site: UCSD (vs UAB) | -0.5471 | 0.3222 | ±0.6444 | -1.698 | 0.0895 | . |
| Site: UW (vs UAB) | -0.0094 | 0.2993 | ±0.5986 | -0.031 | 0.9751 |  |
| **Age (years)** | **-0.0400** | 0.0123 | ±0.0247 | **-3.241** | **0.0012** | ** |
| BMI (kg/m2) | +0.0316 | 0.0170 | ±0.0339 | +1.864 | 0.0623 | . |
| **Hypertension** | **-0.7621** | 0.2753 | ±0.5506 | **-2.768** | **0.0056** | ** |
| High cholesterol | +0.3336 | 0.2630 | ±0.5260 | +1.268 | 0.2046 |  |
| Kidney disease | +0.4726 | 0.3581 | ±0.7163 | +1.320 | 0.1869 |  |
| Circulatory disease | +0.1640 | 0.2965 | ±0.5929 | +0.553 | 0.5802 |  |
| **Nocturnal time > 180 (%)** | **-0.0123** | 0.0046 | ±0.0092 | **-2.672** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **795**, R² = **0.0872**, Adj R² = **0.0744**, F-statistic = **6.80** (p = **5.44e-11**), Residual SE = **3.370** on **783** df, AIC = **4199.9**, BIC = **4256.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3065** | 0.9958 | ±1.9916 | **+27.422** | **1.51e-165** | *** |
| **Education: graduate level (vs college)** | **+0.7498** | 0.2550 | ±0.5101 | **+2.940** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **-1.5057** | 0.4541 | ±0.9083 | **-3.315** | **9.15e-04** | *** |
| Site: UCSD (vs UAB) | -0.5321 | 0.3193 | ±0.6387 | -1.666 | 0.0957 | . |
| Site: UW (vs UAB) | -0.0357 | 0.2994 | ±0.5989 | -0.119 | 0.9050 |  |
| **Age (years)** | **-0.0408** | 0.0124 | ±0.0247 | **-3.299** | **9.71e-04** | *** |
| BMI (kg/m2) | +0.0255 | 0.0167 | ±0.0334 | +1.526 | 0.1270 |  |
| **Hypertension** | **-0.7419** | 0.2762 | ±0.5525 | **-2.686** | **0.0072** | ** |
| High cholesterol | +0.3304 | 0.2630 | ±0.5260 | +1.256 | 0.2090 |  |
| Kidney disease | +0.4663 | 0.3623 | ±0.7245 | +1.287 | 0.1980 |  |
| Circulatory disease | +0.1654 | 0.2965 | ±0.5930 | +0.558 | 0.5770 |  |
| **Time > 250 (%)** | **-0.0192** | 0.0078 | ±0.0155 | **-2.474** | **0.0134** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 795)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **795**, R² = **0.0870**, Adj R² = **0.0742**, F-statistic = **6.78** (p = **5.86e-11**), Residual SE = **3.371** on **783** df, AIC = **4200.1**, BIC = **4256.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2830** | 0.9952 | ±1.9904 | **+27.414** | **1.86e-165** | *** |
| **Education: graduate level (vs college)** | **+0.7509** | 0.2551 | ±0.5102 | **+2.944** | **0.0032** | ** |
| **Education: high school or below (vs college)** | **-1.5071** | 0.4539 | ±0.9077 | **-3.321** | **8.98e-04** | *** |
| Site: UCSD (vs UAB) | -0.5324 | 0.3195 | ±0.6390 | -1.666 | 0.0956 | . |
| Site: UW (vs UAB) | -0.0323 | 0.2993 | ±0.5987 | -0.108 | 0.9140 |  |
| **Age (years)** | **-0.0405** | 0.0123 | ±0.0247 | **-3.278** | **0.0010** | ** |
| BMI (kg/m2) | +0.0255 | 0.0167 | ±0.0335 | +1.526 | 0.1271 |  |
| **Hypertension** | **-0.7441** | 0.2762 | ±0.5524 | **-2.694** | **0.0071** | ** |
| High cholesterol | +0.3304 | 0.2630 | ±0.5260 | +1.256 | 0.2090 |  |
| Kidney disease | +0.4701 | 0.3624 | ±0.7248 | +1.297 | 0.1946 |  |
| Circulatory disease | +0.1672 | 0.2965 | ±0.5930 | +0.564 | 0.5728 |  |
| **Avg. daily time > 250 (%)** | **-0.0192** | 0.0080 | ±0.0160 | **-2.407** | **0.0161** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 795; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0514**, LLR χ² = **56.47** (p = **1.67e-08**), AUC = **0.6518**, AIC = **1064.1**, BIC = **1115.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7003** | 0.6384 | ±1.2767 | **-2.664** | **0.0077** | 0.1826 | ** |
| **Education: graduate level (vs college)** | **-0.5422** | 0.1664 | ±0.3327 | **-3.259** | **0.0011** | 0.5815 | ** |
| **Education: high school or below (vs college)** | **+0.6826** | 0.2259 | ±0.4517 | **+3.022** | **0.0025** | 1.9791 | ** |
| **Site: UCSD (vs UAB)** | **+0.3839** | 0.1890 | ±0.3779 | **+2.032** | **0.0422** | 1.4680 | * |
| Site: UW (vs UAB) | -0.1325 | 0.1801 | ±0.3602 | -0.735 | 0.4621 | 0.8759 |  |
| **Age (years)** | **+0.0260** | 0.0075 | ±0.0149 | **+3.478** | **5.06e-04** | 1.0263 | *** |
| BMI (kg/m2) | -0.0040 | 0.0109 | ±0.0217 | -0.364 | 0.7156 | 0.9961 |  |
| Hypertension | +0.2933 | 0.1688 | ±0.3376 | +1.738 | 0.0823 | 1.3408 | . |
| High cholesterol | -0.0376 | 0.1594 | ±0.3189 | -0.236 | 0.8135 | 0.9631 |  |
| Kidney disease | -0.3354 | 0.2086 | ±0.4173 | -1.608 | 0.1079 | 0.7150 |  |
| Circulatory disease | -0.0750 | 0.1968 | ±0.3936 | -0.381 | 0.7031 | 0.9277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0558**, LLR χ² = **61.34** (p = **5.23e-09**), AUC = **0.6547**, AIC = **1061.2**, BIC = **1117.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4677** | 0.7326 | ±1.4653 | **-3.368** | **7.57e-04** | 0.0848 | *** |
| **Education: graduate level (vs college)** | **-0.5203** | 0.1673 | ±0.3346 | **-3.110** | **0.0019** | 0.5943 | ** |
| **Education: high school or below (vs college)** | **+0.6168** | 0.2281 | ±0.4561 | **+2.704** | **0.0068** | 1.8530 | ** |
| **Site: UCSD (vs UAB)** | **+0.4034** | 0.1897 | ±0.3793 | **+2.127** | **0.0334** | 1.4969 | * |
| Site: UW (vs UAB) | -0.1021 | 0.1811 | ±0.3623 | -0.563 | 0.5732 | 0.9030 |  |
| **Age (years)** | **+0.0264** | 0.0075 | ±0.0150 | **+3.521** | **4.30e-04** | 1.0268 | *** |
| BMI (kg/m2) | -0.0078 | 0.0111 | ±0.0221 | -0.708 | 0.4789 | 0.9922 |  |
| Hypertension | +0.2772 | 0.1694 | ±0.3387 | +1.636 | 0.1017 | 1.3194 |  |
| High cholesterol | -0.0512 | 0.1601 | ±0.3202 | -0.320 | 0.7490 | 0.9501 |  |
| Kidney disease | -0.3418 | 0.2096 | ±0.4191 | -1.631 | 0.1029 | 0.7105 |  |
| Circulatory disease | -0.1009 | 0.1978 | ±0.3955 | -0.510 | 0.6098 | 0.9040 |  |
| **HbA1c (%)** | **+0.1273** | 0.0586 | ±0.1173 | **+2.171** | **0.0299** | 1.1358 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0581**, LLR χ² = **63.77** (p = **1.83e-09**), AUC = **0.6549**, AIC = **1058.8**, BIC = **1114.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4569** | 0.7024 | ±1.4048 | **-3.498** | **4.69e-04** | 0.0857 | *** |
| **Education: graduate level (vs college)** | **-0.5310** | 0.1672 | ±0.3345 | **-3.175** | **0.0015** | 0.5880 | ** |
| **Education: high school or below (vs college)** | **+0.6088** | 0.2281 | ±0.4563 | **+2.668** | **0.0076** | 1.8381 | ** |
| **Site: UCSD (vs UAB)** | **+0.4208** | 0.1902 | ±0.3803 | **+2.213** | **0.0269** | 1.5232 | * |
| Site: UW (vs UAB) | -0.0986 | 0.1813 | ±0.3626 | -0.544 | 0.5865 | 0.9061 |  |
| **Age (years)** | **+0.0267** | 0.0075 | ±0.0150 | **+3.561** | **3.70e-04** | 1.0271 | *** |
| BMI (kg/m2) | -0.0080 | 0.0110 | ±0.0220 | -0.727 | 0.4669 | 0.9920 |  |
| Hypertension | +0.2803 | 0.1696 | ±0.3391 | +1.653 | 0.0983 | 1.3236 | . |
| High cholesterol | -0.0457 | 0.1602 | ±0.3205 | -0.285 | 0.7753 | 0.9553 |  |
| Kidney disease | -0.3697 | 0.2104 | ±0.4208 | -1.757 | 0.0789 | 0.6910 | . |
| Circulatory disease | -0.1134 | 0.1984 | ±0.3968 | -0.572 | 0.5675 | 0.8928 |  |
| **Mean glucose (mg/dL)** | **+0.0052** | 0.0019 | ±0.0039 | **+2.666** | **0.0077** | 1.0052 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0581**, LLR χ² = **63.77** (p = **1.83e-09**), AUC = **0.6549**, AIC = **1058.8**, BIC = **1114.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1751** | 0.8483 | ±1.6967 | **-3.743** | **1.82e-04** | 0.0418 | *** |
| **Education: graduate level (vs college)** | **-0.5310** | 0.1672 | ±0.3345 | **-3.175** | **0.0015** | 0.5880 | ** |
| **Education: high school or below (vs college)** | **+0.6088** | 0.2281 | ±0.4563 | **+2.668** | **0.0076** | 1.8381 | ** |
| **Site: UCSD (vs UAB)** | **+0.4208** | 0.1902 | ±0.3803 | **+2.213** | **0.0269** | 1.5232 | * |
| Site: UW (vs UAB) | -0.0986 | 0.1813 | ±0.3626 | -0.544 | 0.5865 | 0.9061 |  |
| **Age (years)** | **+0.0267** | 0.0075 | ±0.0150 | **+3.561** | **3.70e-04** | 1.0271 | *** |
| BMI (kg/m2) | -0.0080 | 0.0110 | ±0.0220 | -0.727 | 0.4669 | 0.9920 |  |
| Hypertension | +0.2803 | 0.1696 | ±0.3391 | +1.653 | 0.0983 | 1.3236 | . |
| High cholesterol | -0.0457 | 0.1602 | ±0.3205 | -0.285 | 0.7753 | 0.9553 |  |
| Kidney disease | -0.3697 | 0.2104 | ±0.4208 | -1.757 | 0.0789 | 0.6910 | . |
| Circulatory disease | -0.1134 | 0.1984 | ±0.3968 | -0.572 | 0.5675 | 0.8928 |  |
| **GMI (%)** | **+0.2170** | 0.0814 | ±0.1628 | **+2.666** | **0.0077** | 1.2423 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0562**, LLR χ² = **61.75** (p = **4.38e-09**), AUC = **0.6552**, AIC = **1060.8**, BIC = **1117.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2895** | 0.6920 | ±1.3840 | **-3.309** | **9.38e-04** | 0.1013 | *** |
| **Education: graduate level (vs college)** | **-0.5264** | 0.1671 | ±0.3342 | **-3.150** | **0.0016** | 0.5907 | ** |
| **Education: high school or below (vs college)** | **+0.6266** | 0.2276 | ±0.4551 | **+2.754** | **0.0059** | 1.8712 | ** |
| **Site: UCSD (vs UAB)** | **+0.4134** | 0.1899 | ±0.3798 | **+2.177** | **0.0295** | 1.5119 | * |
| Site: UW (vs UAB) | -0.1138 | 0.1808 | ±0.3616 | -0.630 | 0.5289 | 0.8924 |  |
| **Age (years)** | **+0.0272** | 0.0075 | ±0.0150 | **+3.621** | **2.94e-04** | 1.0276 | *** |
| BMI (kg/m2) | -0.0082 | 0.0111 | ±0.0221 | -0.745 | 0.4565 | 0.9918 |  |
| Hypertension | +0.2852 | 0.1694 | ±0.3388 | +1.684 | 0.0922 | 1.3300 | . |
| High cholesterol | -0.0431 | 0.1600 | ±0.3201 | -0.270 | 0.7875 | 0.9578 |  |
| Kidney disease | -0.3496 | 0.2097 | ±0.4194 | -1.667 | 0.0955 | 0.7050 | . |
| Circulatory disease | -0.1050 | 0.1981 | ±0.3963 | -0.530 | 0.5960 | 0.9003 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0042** | 0.0018 | ±0.0037 | **+2.273** | **0.0230** | 1.0042 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0579**, LLR χ² = **63.65** (p = **1.93e-09**), AUC = **0.6573**, AIC = **1058.9**, BIC = **1115.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2614** | 0.6781 | ±1.3562 | **-3.335** | **8.54e-04** | 0.1042 | *** |
| **Education: graduate level (vs college)** | **-0.5216** | 0.1674 | ±0.3349 | **-3.115** | **0.0018** | 0.5936 | ** |
| **Education: high school or below (vs college)** | **+0.6227** | 0.2272 | ±0.4544 | **+2.741** | **0.0061** | 1.8639 | ** |
| **Site: UCSD (vs UAB)** | **+0.4212** | 0.1904 | ±0.3808 | **+2.213** | **0.0269** | 1.5239 | * |
| Site: UW (vs UAB) | -0.0717 | 0.1824 | ±0.3648 | -0.393 | 0.6942 | 0.9308 |  |
| **Age (years)** | **+0.0260** | 0.0075 | ±0.0150 | **+3.465** | **5.30e-04** | 1.0264 | *** |
| BMI (kg/m2) | -0.0074 | 0.0110 | ±0.0220 | -0.676 | 0.4987 | 0.9926 |  |
| Hypertension | +0.2708 | 0.1696 | ±0.3392 | +1.597 | 0.1103 | 1.3110 |  |
| High cholesterol | -0.0295 | 0.1603 | ±0.3205 | -0.184 | 0.8542 | 0.9710 |  |
| **Kidney disease** | **-0.4429** | 0.2138 | ±0.4275 | **-2.072** | **0.0383** | 0.6422 | * |
| Circulatory disease | -0.1071 | 0.1980 | ±0.3961 | -0.541 | 0.5887 | 0.8985 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0173** | 0.0065 | ±0.0131 | **+2.647** | **0.0081** | 1.0175 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0573**, LLR χ² = **62.96** (p = **2.60e-09**), AUC = **0.6570**, AIC = **1059.6**, BIC = **1115.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2513** | 0.6796 | ±1.3592 | **-3.313** | **9.24e-04** | 0.1053 | *** |
| **Education: graduate level (vs college)** | **-0.5290** | 0.1673 | ±0.3346 | **-3.162** | **0.0016** | 0.5892 | ** |
| **Education: high school or below (vs college)** | **+0.6200** | 0.2272 | ±0.4545 | **+2.728** | **0.0064** | 1.8589 | ** |
| **Site: UCSD (vs UAB)** | **+0.4200** | 0.1903 | ±0.3806 | **+2.207** | **0.0273** | 1.5219 | * |
| Site: UW (vs UAB) | -0.0805 | 0.1820 | ±0.3641 | -0.442 | 0.6583 | 0.9226 |  |
| **Age (years)** | **+0.0258** | 0.0075 | ±0.0150 | **+3.435** | **5.92e-04** | 1.0261 | *** |
| BMI (kg/m2) | -0.0064 | 0.0109 | ±0.0219 | -0.586 | 0.5578 | 0.9936 |  |
| Hypertension | +0.2751 | 0.1695 | ±0.3389 | +1.624 | 0.1045 | 1.3167 |  |
| High cholesterol | -0.0298 | 0.1601 | ±0.3202 | -0.186 | 0.8524 | 0.9707 |  |
| **Kidney disease** | **-0.4435** | 0.2141 | ±0.4282 | **-2.072** | **0.0383** | 0.6418 | * |
| Circulatory disease | -0.1012 | 0.1978 | ±0.3955 | -0.512 | 0.6088 | 0.9038 |  |
| **Avg. daily SD (mg/dL)** | **+0.0186** | 0.0074 | ±0.0148 | **+2.517** | **0.0118** | 1.0188 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0517**, LLR χ² = **56.83** (p = **3.58e-08**), AUC = **0.6520**, AIC = **1065.7**, BIC = **1121.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8836** | 0.7095 | ±1.4190 | **-2.655** | **0.0079** | 0.1520 | ** |
| **Education: graduate level (vs college)** | **-0.5376** | 0.1666 | ±0.3332 | **-3.227** | **0.0013** | 0.5841 | ** |
| **Education: high school or below (vs college)** | **+0.6811** | 0.2258 | ±0.4517 | **+3.016** | **0.0026** | 1.9761 | ** |
| **Site: UCSD (vs UAB)** | **+0.3886** | 0.1892 | ±0.3783 | **+2.054** | **0.0400** | 1.4749 | * |
| Site: UW (vs UAB) | -0.1209 | 0.1812 | ±0.3624 | -0.667 | 0.5045 | 0.8861 |  |
| **Age (years)** | **+0.0258** | 0.0075 | ±0.0150 | **+3.448** | **5.65e-04** | 1.0261 | *** |
| BMI (kg/m2) | -0.0042 | 0.0109 | ±0.0217 | -0.382 | 0.7026 | 0.9959 |  |
| Hypertension | +0.2886 | 0.1690 | ±0.3379 | +1.708 | 0.0876 | 1.3346 | . |
| High cholesterol | -0.0319 | 0.1597 | ±0.3195 | -0.200 | 0.8418 | 0.9686 |  |
| Kidney disease | -0.3591 | 0.2124 | ±0.4247 | -1.691 | 0.0909 | 0.6983 | . |
| Circulatory disease | -0.0760 | 0.1968 | ±0.3937 | -0.386 | 0.6996 | 0.9269 |  |
| CV (%) | +0.0083 | 0.0139 | ±0.0279 | +0.596 | 0.5510 | 1.0083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0517**, LLR χ² = **56.75** (p = **3.70e-08**), AUC = **0.6518**, AIC = **1065.8**, BIC = **1122.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.5147** | 0.7297 | ±1.4594 | **-2.076** | **0.0379** | 0.2199 | * |
| **Education: graduate level (vs college)** | **-0.5390** | 0.1665 | ±0.3330 | **-3.237** | **0.0012** | 0.5833 | ** |
| **Education: high school or below (vs college)** | **+0.6817** | 0.2258 | ±0.4517 | **+3.018** | **0.0025** | 1.9772 | ** |
| **Site: UCSD (vs UAB)** | **+0.3856** | 0.1890 | ±0.3780 | **+2.040** | **0.0413** | 1.4705 | * |
| Site: UW (vs UAB) | -0.1239 | 0.1809 | ±0.3618 | -0.685 | 0.4932 | 0.8834 |  |
| **Age (years)** | **+0.0259** | 0.0075 | ±0.0150 | **+3.458** | **5.44e-04** | 1.0262 | *** |
| BMI (kg/m2) | -0.0040 | 0.0109 | ±0.0217 | -0.370 | 0.7116 | 0.9960 |  |
| Hypertension | +0.2893 | 0.1690 | ±0.3379 | +1.712 | 0.0868 | 1.3355 | . |
| High cholesterol | -0.0350 | 0.1595 | ±0.3191 | -0.219 | 0.8264 | 0.9656 |  |
| Kidney disease | -0.3527 | 0.2112 | ±0.4223 | -1.670 | 0.0949 | 0.7028 | . |
| Circulatory disease | -0.0775 | 0.1969 | ±0.3938 | -0.394 | 0.6939 | 0.9254 |  |
| Mean / SD ratio | -0.0400 | 0.0763 | ±0.1525 | -0.524 | 0.6003 | 0.9608 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0514**, LLR χ² = **56.51** (p = **4.09e-08**), AUC = **0.6517**, AIC = **1066.1**, BIC = **1122.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.6351** | 0.7183 | ±1.4366 | **-2.276** | **0.0228** | 0.1949 | * |
| **Education: graduate level (vs college)** | **-0.5413** | 0.1664 | ±0.3329 | **-3.252** | **0.0011** | 0.5820 | ** |
| **Education: high school or below (vs college)** | **+0.6820** | 0.2259 | ±0.4517 | **+3.020** | **0.0025** | 1.9779 | ** |
| **Site: UCSD (vs UAB)** | **+0.3843** | 0.1890 | ±0.3779 | **+2.034** | **0.0420** | 1.4686 | * |
| Site: UW (vs UAB) | -0.1297 | 0.1806 | ±0.3613 | -0.718 | 0.4727 | 0.8783 |  |
| **Age (years)** | **+0.0259** | 0.0075 | ±0.0150 | **+3.463** | **5.34e-04** | 1.0262 | *** |
| BMI (kg/m2) | -0.0039 | 0.0109 | ±0.0217 | -0.360 | 0.7187 | 0.9961 |  |
| Hypertension | +0.2920 | 0.1689 | ±0.3378 | +1.729 | 0.0839 | 1.3390 | . |
| High cholesterol | -0.0364 | 0.1596 | ±0.3191 | -0.228 | 0.8198 | 0.9643 |  |
| Kidney disease | -0.3415 | 0.2109 | ±0.4218 | -1.620 | 0.1053 | 0.7107 |  |
| Circulatory disease | -0.0751 | 0.1968 | ±0.3936 | -0.382 | 0.7028 | 0.9277 |  |
| Avg. daily mean/SD | -0.0120 | 0.0609 | ±0.1217 | -0.198 | 0.8432 | 0.9880 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0551**, LLR χ² = **60.51** (p = **7.47e-09**), AUC = **0.6529**, AIC = **1062.1**, BIC = **1118.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.5434** | 0.7702 | ±1.5404 | **-3.302** | **9.59e-04** | 0.0786 | *** |
| **Education: graduate level (vs college)** | **-0.5182** | 0.1672 | ±0.3343 | **-3.100** | **0.0019** | 0.5956 | ** |
| **Education: high school or below (vs college)** | **+0.6668** | 0.2260 | ±0.4519 | **+2.951** | **0.0032** | 1.9481 | ** |
| **Site: UCSD (vs UAB)** | **+0.4182** | 0.1904 | ±0.3809 | **+2.196** | **0.0281** | 1.5192 | * |
| Site: UW (vs UAB) | -0.0688 | 0.1833 | ±0.3667 | -0.375 | 0.7075 | 0.9335 |  |
| **Age (years)** | **+0.0274** | 0.0075 | ±0.0151 | **+3.636** | **2.76e-04** | 1.0278 | *** |
| BMI (kg/m2) | -0.0050 | 0.0109 | ±0.0217 | -0.458 | 0.6470 | 0.9950 |  |
| Hypertension | +0.3040 | 0.1692 | ±0.3384 | +1.797 | 0.0724 | 1.3552 | . |
| High cholesterol | -0.0123 | 0.1603 | ±0.3207 | -0.077 | 0.9389 | 0.9878 |  |
| Kidney disease | -0.3694 | 0.2102 | ±0.4203 | -1.758 | 0.0788 | 0.6911 | . |
| Circulatory disease | -0.0853 | 0.1974 | ±0.3949 | -0.432 | 0.6657 | 0.9182 |  |
| **MAG (mg/dL/h)** | **+0.0161** | 0.0081 | ±0.0161 | **+1.992** | **0.0464** | 1.0162 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0558**, LLR χ² = **61.33** (p = **5.25e-09**), AUC = **0.6560**, AIC = **1061.2**, BIC = **1117.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4254** | 0.7239 | ±1.4478 | **-3.350** | **8.07e-04** | 0.0884 | *** |
| **Education: graduate level (vs college)** | **-0.5301** | 0.1671 | ±0.3342 | **-3.172** | **0.0015** | 0.5886 | ** |
| **Education: high school or below (vs college)** | **+0.6294** | 0.2270 | ±0.4539 | **+2.773** | **0.0055** | 1.8765 | ** |
| **Site: UCSD (vs UAB)** | **+0.4212** | 0.1903 | ±0.3806 | **+2.213** | **0.0269** | 1.5238 | * |
| Site: UW (vs UAB) | -0.0836 | 0.1821 | ±0.3641 | -0.459 | 0.6460 | 0.9198 |  |
| **Age (years)** | **+0.0265** | 0.0075 | ±0.0150 | **+3.530** | **4.16e-04** | 1.0268 | *** |
| BMI (kg/m2) | -0.0053 | 0.0109 | ±0.0218 | -0.488 | 0.6253 | 0.9947 |  |
| Hypertension | +0.2887 | 0.1692 | ±0.3383 | +1.707 | 0.0879 | 1.3347 | . |
| High cholesterol | -0.0273 | 0.1600 | ±0.3199 | -0.171 | 0.8646 | 0.9731 |  |
| **Kidney disease** | **-0.4267** | 0.2136 | ±0.4272 | **-1.998** | **0.0457** | 0.6526 | * |
| Circulatory disease | -0.0992 | 0.1977 | ±0.3953 | -0.502 | 0.6157 | 0.9055 |  |
| **Avg. daily range (mg/dL)** | **+0.0048** | 0.0022 | ±0.0043 | **+2.187** | **0.0287** | 1.0048 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0555**, LLR χ² = **61.00** (p = **6.03e-09**), AUC = **0.6557**, AIC = **1061.6**, BIC = **1117.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9192** | 0.6503 | ±1.3007 | **-2.951** | **0.0032** | 0.1467 | ** |
| **Education: graduate level (vs college)** | **-0.5113** | 0.1674 | ±0.3349 | **-3.054** | **0.0023** | 0.5997 | ** |
| **Education: high school or below (vs college)** | **+0.6622** | 0.2264 | ±0.4529 | **+2.924** | **0.0035** | 1.9390 | ** |
| **Site: UCSD (vs UAB)** | **+0.4022** | 0.1898 | ±0.3796 | **+2.119** | **0.0341** | 1.4951 | * |
| Site: UW (vs UAB) | -0.0939 | 0.1815 | ±0.3630 | -0.517 | 0.6050 | 0.9104 |  |
| **Age (years)** | **+0.0269** | 0.0075 | ±0.0150 | **+3.580** | **3.43e-04** | 1.0273 | *** |
| BMI (kg/m2) | -0.0074 | 0.0110 | ±0.0221 | -0.673 | 0.5009 | 0.9926 |  |
| Hypertension | +0.2718 | 0.1695 | ±0.3391 | +1.603 | 0.1089 | 1.3123 |  |
| High cholesterol | -0.0385 | 0.1601 | ±0.3202 | -0.240 | 0.8100 | 0.9622 |  |
| Kidney disease | -0.3733 | 0.2101 | ±0.4203 | -1.777 | 0.0756 | 0.6885 | . |
| Circulatory disease | -0.1085 | 0.1982 | ±0.3963 | -0.548 | 0.5839 | 0.8971 |  |
| **SD of daily means (mg/dL)** | **+0.0203** | 0.0097 | ±0.0193 | **+2.099** | **0.0359** | 1.0205 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0587**, LLR χ² = **64.44** (p = **1.37e-09**), AUC = **0.6554**, AIC = **1058.1**, BIC = **1114.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9655 | 0.6923 | ±1.3846 | -1.395 | 0.1632 | 0.3808 |  |
| **Education: graduate level (vs college)** | **-0.5302** | 0.1674 | ±0.3348 | **-3.167** | **0.0015** | 0.5885 | ** |
| **Education: high school or below (vs college)** | **+0.6080** | 0.2280 | ±0.4561 | **+2.666** | **0.0077** | 1.8367 | ** |
| **Site: UCSD (vs UAB)** | **+0.4313** | 0.1905 | ±0.3810 | **+2.264** | **0.0236** | 1.5393 | * |
| Site: UW (vs UAB) | -0.0886 | 0.1818 | ±0.3635 | -0.487 | 0.6260 | 0.9152 |  |
| **Age (years)** | **+0.0264** | 0.0075 | ±0.0150 | **+3.515** | **4.40e-04** | 1.0268 | *** |
| BMI (kg/m2) | -0.0090 | 0.0111 | ±0.0221 | -0.814 | 0.4155 | 0.9910 |  |
| Hypertension | +0.2850 | 0.1696 | ±0.3393 | +1.680 | 0.0930 | 1.3297 | . |
| High cholesterol | -0.0351 | 0.1603 | ±0.3205 | -0.219 | 0.8266 | 0.9655 |  |
| Kidney disease | -0.3880 | 0.2108 | ±0.4216 | -1.841 | 0.0657 | 0.6784 | . |
| Circulatory disease | -0.1095 | 0.1983 | ±0.3966 | -0.552 | 0.5809 | 0.8963 |  |
| **Time in range 70-180, pooled (%)** | **-0.0086** | 0.0031 | ±0.0061 | **-2.802** | **0.0051** | 0.9914 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0585**, LLR χ² = **64.28** (p = **1.47e-09**), AUC = **0.6549**, AIC = **1058.3**, BIC = **1114.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9683 | 0.6928 | ±1.3857 | -1.398 | 0.1622 | 0.3797 |  |
| **Education: graduate level (vs college)** | **-0.5325** | 0.1674 | ±0.3348 | **-3.181** | **0.0015** | 0.5872 | ** |
| **Education: high school or below (vs college)** | **+0.6070** | 0.2281 | ±0.4561 | **+2.661** | **0.0078** | 1.8348 | ** |
| **Site: UCSD (vs UAB)** | **+0.4334** | 0.1906 | ±0.3811 | **+2.274** | **0.0229** | 1.5425 | * |
| Site: UW (vs UAB) | -0.0885 | 0.1818 | ±0.3636 | -0.487 | 0.6264 | 0.9153 |  |
| **Age (years)** | **+0.0263** | 0.0075 | ±0.0150 | **+3.507** | **4.53e-04** | 1.0267 | *** |
| BMI (kg/m2) | -0.0090 | 0.0111 | ±0.0221 | -0.817 | 0.4141 | 0.9910 |  |
| Hypertension | +0.2856 | 0.1696 | ±0.3393 | +1.684 | 0.0922 | 1.3306 | . |
| High cholesterol | -0.0355 | 0.1602 | ±0.3205 | -0.222 | 0.8246 | 0.9651 |  |
| Kidney disease | -0.3909 | 0.2110 | ±0.4219 | -1.853 | 0.0639 | 0.6765 | . |
| Circulatory disease | -0.1086 | 0.1982 | ±0.3965 | -0.548 | 0.5837 | 0.8970 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0085** | 0.0031 | ±0.0061 | **-2.775** | **0.0055** | 0.9916 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0533**, LLR χ² = **58.59** (p = **1.69e-08**), AUC = **0.6563**, AIC = **1064.0**, BIC = **1120.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.6105** | 0.6423 | ±1.2846 | **-2.507** | **0.0122** | 0.1998 | * |
| **Education: graduate level (vs college)** | **-0.5517** | 0.1668 | ±0.3336 | **-3.308** | **9.41e-04** | 0.5760 | *** |
| **Education: high school or below (vs college)** | **+0.6707** | 0.2263 | ±0.4525 | **+2.964** | **0.0030** | 1.9556 | ** |
| Site: UCSD (vs UAB) | +0.3710 | 0.1893 | ±0.3787 | +1.959 | 0.0501 | 1.4492 | . |
| Site: UW (vs UAB) | -0.1481 | 0.1806 | ±0.3613 | -0.820 | 0.4122 | 0.8623 |  |
| **Age (years)** | **+0.0256** | 0.0075 | ±0.0150 | **+3.428** | **6.09e-04** | 1.0260 | *** |
| BMI (kg/m2) | -0.0038 | 0.0109 | ±0.0218 | -0.350 | 0.7265 | 0.9962 |  |
| Hypertension | +0.3078 | 0.1693 | ±0.3385 | +1.819 | 0.0690 | 1.3604 | . |
| High cholesterol | -0.0581 | 0.1602 | ±0.3204 | -0.362 | 0.7170 | 0.9436 |  |
| Kidney disease | -0.3339 | 0.2092 | ±0.4184 | -1.596 | 0.1104 | 0.7161 |  |
| Circulatory disease | -0.0613 | 0.1972 | ±0.3945 | -0.311 | 0.7561 | 0.9406 |  |
| Any reading < 54 during wear (0/1) | -0.2575 | 0.1776 | ±0.3552 | -1.450 | 0.1470 | 0.7729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0525**, LLR χ² = **57.70** (p = **2.47e-08**), AUC = **0.6539**, AIC = **1064.9**, BIC = **1121.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.6614** | 0.6394 | ±1.2787 | **-2.598** | **0.0094** | 0.1899 | ** |
| **Education: graduate level (vs college)** | **-0.5525** | 0.1667 | ±0.3333 | **-3.315** | **9.16e-04** | 0.5755 | *** |
| **Education: high school or below (vs college)** | **+0.6699** | 0.2262 | ±0.4525 | **+2.961** | **0.0031** | 1.9541 | ** |
| Site: UCSD (vs UAB) | +0.3692 | 0.1895 | ±0.3789 | +1.948 | 0.0514 | 1.4465 | . |
| Site: UW (vs UAB) | -0.1520 | 0.1810 | ±0.3619 | -0.840 | 0.4009 | 0.8590 |  |
| **Age (years)** | **+0.0263** | 0.0075 | ±0.0150 | **+3.513** | **4.43e-04** | 1.0266 | *** |
| BMI (kg/m2) | -0.0045 | 0.0109 | ±0.0218 | -0.411 | 0.6813 | 0.9955 |  |
| Hypertension | +0.2947 | 0.1689 | ±0.3378 | +1.744 | 0.0811 | 1.3427 | . |
| High cholesterol | -0.0528 | 0.1601 | ±0.3202 | -0.330 | 0.7413 | 0.9485 |  |
| Kidney disease | -0.3374 | 0.2088 | ±0.4175 | -1.616 | 0.1060 | 0.7136 |  |
| Circulatory disease | -0.0830 | 0.1970 | ±0.3940 | -0.422 | 0.6734 | 0.9203 |  |
| Time < 54 (%) | -0.1695 | 0.1821 | ±0.3642 | -0.930 | 0.3521 | 0.8441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0516**, LLR χ² = **56.66** (p = **3.84e-08**), AUC = **0.6523**, AIC = **1065.9**, BIC = **1122.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.6868** | 0.6390 | ±1.2781 | **-2.640** | **0.0083** | 0.1851 | ** |
| **Education: graduate level (vs college)** | **-0.5456** | 0.1666 | ±0.3331 | **-3.276** | **0.0011** | 0.5795 | ** |
| **Education: high school or below (vs college)** | **+0.6777** | 0.2262 | ±0.4523 | **+2.996** | **0.0027** | 1.9693 | ** |
| **Site: UCSD (vs UAB)** | **+0.3779** | 0.1895 | ±0.3789 | **+1.995** | **0.0461** | 1.4592 | * |
| Site: UW (vs UAB) | -0.1408 | 0.1811 | ±0.3622 | -0.777 | 0.4369 | 0.8687 |  |
| **Age (years)** | **+0.0261** | 0.0075 | ±0.0149 | **+3.488** | **4.86e-04** | 1.0264 | *** |
| BMI (kg/m2) | -0.0041 | 0.0109 | ±0.0217 | -0.376 | 0.7066 | 0.9959 |  |
| Hypertension | +0.2937 | 0.1688 | ±0.3376 | +1.740 | 0.0819 | 1.3414 | . |
| High cholesterol | -0.0441 | 0.1601 | ±0.3203 | -0.275 | 0.7831 | 0.9569 |  |
| Kidney disease | -0.3349 | 0.2087 | ±0.4173 | -1.605 | 0.1085 | 0.7154 |  |
| Circulatory disease | -0.0776 | 0.1969 | ±0.3938 | -0.394 | 0.6933 | 0.9253 |  |
| Avg. daily time < 54 (%) | -0.0646 | 0.1514 | ±0.3028 | -0.427 | 0.6697 | 0.9375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0516**, LLR χ² = **56.74** (p = **3.72e-08**), AUC = **0.6521**, AIC = **1065.8**, BIC = **1122.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7162** | 0.6393 | ±1.2787 | **-2.684** | **0.0073** | 0.1797 | ** |
| **Education: graduate level (vs college)** | **-0.5372** | 0.1666 | ±0.3333 | **-3.224** | **0.0013** | 0.5844 | ** |
| **Education: high school or below (vs college)** | **+0.6873** | 0.2261 | ±0.4522 | **+3.040** | **0.0024** | 1.9883 | ** |
| **Site: UCSD (vs UAB)** | **+0.3926** | 0.1898 | ±0.3796 | **+2.069** | **0.0386** | 1.4809 | * |
| Site: UW (vs UAB) | -0.1224 | 0.1812 | ±0.3624 | -0.676 | 0.4993 | 0.8848 |  |
| **Age (years)** | **+0.0258** | 0.0075 | ±0.0149 | **+3.457** | **5.46e-04** | 1.0262 | *** |
| BMI (kg/m2) | -0.0040 | 0.0109 | ±0.0217 | -0.369 | 0.7123 | 0.9960 |  |
| Hypertension | +0.2907 | 0.1689 | ±0.3378 | +1.721 | 0.0853 | 1.3373 | . |
| High cholesterol | -0.0281 | 0.1605 | ±0.3211 | -0.175 | 0.8611 | 0.9723 |  |
| Kidney disease | -0.3387 | 0.2087 | ±0.4174 | -1.623 | 0.1046 | 0.7127 |  |
| Circulatory disease | -0.0702 | 0.1970 | ±0.3940 | -0.356 | 0.7216 | 0.9322 |  |
| Time 54-69, pooled (%) | +0.0367 | 0.0715 | ±0.1429 | +0.514 | 0.6072 | 1.0374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0520**, LLR χ² = **57.11** (p = **3.18e-08**), AUC = **0.6527**, AIC = **1065.5**, BIC = **1121.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7198** | 0.6393 | ±1.2785 | **-2.690** | **0.0071** | 0.1791 | ** |
| **Education: graduate level (vs college)** | **-0.5340** | 0.1667 | ±0.3334 | **-3.203** | **0.0014** | 0.5863 | ** |
| **Education: high school or below (vs college)** | **+0.6907** | 0.2262 | ±0.4523 | **+3.054** | **0.0023** | 1.9950 | ** |
| **Site: UCSD (vs UAB)** | **+0.3975** | 0.1898 | ±0.3797 | **+2.094** | **0.0363** | 1.4881 | * |
| Site: UW (vs UAB) | -0.1153 | 0.1815 | ±0.3630 | -0.635 | 0.5253 | 0.8911 |  |
| **Age (years)** | **+0.0257** | 0.0075 | ±0.0150 | **+3.441** | **5.79e-04** | 1.0261 | *** |
| BMI (kg/m2) | -0.0041 | 0.0109 | ±0.0217 | -0.377 | 0.7060 | 0.9959 |  |
| Hypertension | +0.2891 | 0.1690 | ±0.3379 | +1.711 | 0.0870 | 1.3353 | . |
| High cholesterol | -0.0222 | 0.1607 | ±0.3213 | -0.138 | 0.8900 | 0.9780 |  |
| Kidney disease | -0.3402 | 0.2087 | ±0.4174 | -1.630 | 0.1031 | 0.7116 |  |
| Circulatory disease | -0.0666 | 0.1971 | ±0.3941 | -0.338 | 0.7353 | 0.9355 |  |
| Avg. daily time 54-69 (%) | +0.0543 | 0.0689 | ±0.1379 | +0.787 | 0.4311 | 1.0558 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0514**, LLR χ² = **56.48** (p = **4.15e-08**), AUC = **0.6520**, AIC = **1066.1**, BIC = **1122.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.6982** | 0.6395 | ±1.2790 | **-2.656** | **0.0079** | 0.1830 | ** |
| **Education: graduate level (vs college)** | **-0.5428** | 0.1667 | ±0.3335 | **-3.255** | **0.0011** | 0.5811 | ** |
| **Education: high school or below (vs college)** | **+0.6820** | 0.2261 | ±0.4523 | **+3.016** | **0.0026** | 1.9779 | ** |
| **Site: UCSD (vs UAB)** | **+0.3829** | 0.1898 | ±0.3797 | **+2.017** | **0.0437** | 1.4666 | * |
| Site: UW (vs UAB) | -0.1336 | 0.1814 | ±0.3628 | -0.737 | 0.4613 | 0.8749 |  |
| **Age (years)** | **+0.0260** | 0.0075 | ±0.0150 | **+3.477** | **5.07e-04** | 1.0263 | *** |
| BMI (kg/m2) | -0.0040 | 0.0109 | ±0.0217 | -0.365 | 0.7150 | 0.9960 |  |
| Hypertension | +0.2935 | 0.1688 | ±0.3377 | +1.738 | 0.0822 | 1.3411 | . |
| High cholesterol | -0.0387 | 0.1606 | ±0.3212 | -0.241 | 0.8097 | 0.9621 |  |
| Kidney disease | -0.3352 | 0.2087 | ±0.4174 | -1.606 | 0.1082 | 0.7152 |  |
| Circulatory disease | -0.0756 | 0.1970 | ±0.3941 | -0.383 | 0.7014 | 0.9272 |  |
| Time < 70 (%) | -0.0029 | 0.0532 | ±0.1064 | -0.055 | 0.9565 | 0.9971 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0516**, LLR χ² = **56.68** (p = **3.82e-08**), AUC = **0.6521**, AIC = **1065.9**, BIC = **1122.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7134** | 0.6392 | ±1.2785 | **-2.680** | **0.0074** | 0.1803 | ** |
| **Education: graduate level (vs college)** | **-0.5374** | 0.1667 | ±0.3334 | **-3.223** | **0.0013** | 0.5843 | ** |
| **Education: high school or below (vs college)** | **+0.6878** | 0.2262 | ±0.4524 | **+3.041** | **0.0024** | 1.9894 | ** |
| **Site: UCSD (vs UAB)** | **+0.3919** | 0.1899 | ±0.3797 | **+2.064** | **0.0390** | 1.4798 | * |
| Site: UW (vs UAB) | -0.1221 | 0.1816 | ±0.3632 | -0.672 | 0.5014 | 0.8851 |  |
| **Age (years)** | **+0.0258** | 0.0075 | ±0.0150 | **+3.456** | **5.48e-04** | 1.0262 | *** |
| BMI (kg/m2) | -0.0040 | 0.0109 | ±0.0217 | -0.365 | 0.7147 | 0.9960 |  |
| Hypertension | +0.2914 | 0.1689 | ±0.3377 | +1.725 | 0.0845 | 1.3382 | . |
| High cholesterol | -0.0287 | 0.1607 | ±0.3213 | -0.179 | 0.8581 | 0.9717 |  |
| Kidney disease | -0.3376 | 0.2087 | ±0.4174 | -1.618 | 0.1057 | 0.7135 |  |
| Circulatory disease | -0.0705 | 0.1970 | ±0.3941 | -0.358 | 0.7207 | 0.9320 |  |
| Avg. daily time < 70 (%) | +0.0230 | 0.0512 | ±0.1025 | +0.448 | 0.6539 | 1.0232 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0566**, LLR χ² = **62.21** (p = **3.59e-09**), AUC = **0.6538**, AIC = **1060.4**, BIC = **1116.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7207 | 0.7660 | ±1.5320 | -0.941 | 0.3468 | 0.4864 |  |
| **Education: graduate level (vs college)** | **-0.5178** | 0.1672 | ±0.3344 | **-3.096** | **0.0020** | 0.5959 | ** |
| **Education: high school or below (vs college)** | **+0.6266** | 0.2276 | ±0.4553 | **+2.753** | **0.0059** | 1.8713 | ** |
| **Site: UCSD (vs UAB)** | **+0.4168** | 0.1899 | ±0.3799 | **+2.195** | **0.0282** | 1.5171 | * |
| Site: UW (vs UAB) | -0.0905 | 0.1815 | ±0.3630 | -0.499 | 0.6179 | 0.9134 |  |
| **Age (years)** | **+0.0274** | 0.0075 | ±0.0150 | **+3.643** | **2.69e-04** | 1.0278 | *** |
| BMI (kg/m2) | -0.0060 | 0.0109 | ±0.0219 | -0.553 | 0.5804 | 0.9940 |  |
| Hypertension | +0.2795 | 0.1694 | ±0.3389 | +1.649 | 0.0990 | 1.3224 | . |
| High cholesterol | -0.0304 | 0.1601 | ±0.3202 | -0.190 | 0.8495 | 0.9701 |  |
| Kidney disease | -0.3621 | 0.2100 | ±0.4200 | -1.724 | 0.0846 | 0.6962 | . |
| Circulatory disease | -0.1038 | 0.1982 | ±0.3963 | -0.524 | 0.6004 | 0.9014 |  |
| **Time 54-250, pooled (%)** | **-0.0111** | 0.0047 | ±0.0095 | **-2.342** | **0.0192** | 0.9890 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0564**, LLR χ² = **61.98** (p = **3.97e-09**), AUC = **0.6537**, AIC = **1060.6**, BIC = **1116.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7171 | 0.7712 | ±1.5424 | -0.930 | 0.3524 | 0.4881 |  |
| **Education: graduate level (vs college)** | **-0.5188** | 0.1672 | ±0.3344 | **-3.103** | **0.0019** | 0.5952 | ** |
| **Education: high school or below (vs college)** | **+0.6274** | 0.2276 | ±0.4552 | **+2.757** | **0.0058** | 1.8727 | ** |
| **Site: UCSD (vs UAB)** | **+0.4166** | 0.1899 | ±0.3798 | **+2.194** | **0.0283** | 1.5169 | * |
| Site: UW (vs UAB) | -0.0928 | 0.1814 | ±0.3628 | -0.511 | 0.6091 | 0.9114 |  |
| **Age (years)** | **+0.0272** | 0.0075 | ±0.0150 | **+3.624** | **2.90e-04** | 1.0276 | *** |
| BMI (kg/m2) | -0.0061 | 0.0109 | ±0.0219 | -0.554 | 0.5794 | 0.9940 |  |
| Hypertension | +0.2808 | 0.1694 | ±0.3388 | +1.658 | 0.0973 | 1.3242 | . |
| High cholesterol | -0.0308 | 0.1600 | ±0.3201 | -0.192 | 0.8476 | 0.9697 |  |
| Kidney disease | -0.3644 | 0.2101 | ±0.4201 | -1.734 | 0.0828 | 0.6946 | . |
| Circulatory disease | -0.1046 | 0.1982 | ±0.3964 | -0.528 | 0.5977 | 0.9007 |  |
| **Avg. daily time 54-250 (%)** | **-0.0110** | 0.0048 | ±0.0096 | **-2.294** | **0.0218** | 0.9891 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0551**, LLR χ² = **60.58** (p = **7.23e-09**), AUC = **0.6536**, AIC = **1062.0**, BIC = **1118.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7242** | 0.6407 | ±1.2814 | **-2.691** | **0.0071** | 0.1783 | ** |
| **Education: graduate level (vs college)** | **-0.5512** | 0.1670 | ±0.3341 | **-3.300** | **9.68e-04** | 0.5763 | *** |
| **Education: high school or below (vs college)** | **+0.6464** | 0.2269 | ±0.4538 | **+2.849** | **0.0044** | 1.9086 | ** |
| **Site: UCSD (vs UAB)** | **+0.4059** | 0.1896 | ±0.3793 | **+2.140** | **0.0323** | 1.5007 | * |
| Site: UW (vs UAB) | -0.1231 | 0.1808 | ±0.3616 | -0.681 | 0.4961 | 0.8842 |  |
| **Age (years)** | **+0.0251** | 0.0075 | ±0.0150 | **+3.353** | **8.01e-04** | 1.0255 | *** |
| BMI (kg/m2) | -0.0081 | 0.0111 | ±0.0222 | -0.729 | 0.4658 | 0.9920 |  |
| Hypertension | +0.2970 | 0.1692 | ±0.3385 | +1.755 | 0.0793 | 1.3458 | . |
| High cholesterol | -0.0440 | 0.1599 | ±0.3197 | -0.275 | 0.7830 | 0.9569 |  |
| Kidney disease | -0.3728 | 0.2101 | ±0.4203 | -1.774 | 0.0761 | 0.6888 | . |
| Circulatory disease | -0.0909 | 0.1974 | ±0.3948 | -0.460 | 0.6453 | 0.9131 |  |
| **Time 181-250, pooled (%)** | **+0.0104** | 0.0051 | ±0.0103 | **+2.023** | **0.0431** | 1.0105 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0552**, LLR χ² = **60.61** (p = **7.14e-09**), AUC = **0.6536**, AIC = **1062.0**, BIC = **1118.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7265** | 0.6409 | ±1.2819 | **-2.694** | **0.0071** | 0.1779 | ** |
| **Education: graduate level (vs college)** | **-0.5530** | 0.1671 | ±0.3342 | **-3.310** | **9.34e-04** | 0.5752 | *** |
| **Education: high school or below (vs college)** | **+0.6433** | 0.2270 | ±0.4540 | **+2.834** | **0.0046** | 1.9028 | ** |
| **Site: UCSD (vs UAB)** | **+0.4089** | 0.1897 | ±0.3795 | **+2.155** | **0.0312** | 1.5051 | * |
| Site: UW (vs UAB) | -0.1208 | 0.1808 | ±0.3617 | -0.668 | 0.5042 | 0.8862 |  |
| **Age (years)** | **+0.0252** | 0.0075 | ±0.0150 | **+3.366** | **7.63e-04** | 1.0256 | *** |
| BMI (kg/m2) | -0.0081 | 0.0111 | ±0.0222 | -0.732 | 0.4644 | 0.9919 |  |
| Hypertension | +0.2965 | 0.1692 | ±0.3385 | +1.752 | 0.0798 | 1.3451 | . |
| High cholesterol | -0.0445 | 0.1599 | ±0.3197 | -0.278 | 0.7806 | 0.9565 |  |
| Kidney disease | -0.3742 | 0.2102 | ±0.4205 | -1.780 | 0.0751 | 0.6878 | . |
| Circulatory disease | -0.0893 | 0.1973 | ±0.3947 | -0.453 | 0.6508 | 0.9145 |  |
| **Avg. daily time 181-250 (%)** | **+0.0103** | 0.0051 | ±0.0101 | **+2.030** | **0.0423** | 1.0103 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0586**, LLR χ² = **64.32** (p = **1.44e-09**), AUC = **0.6554**, AIC = **1058.2**, BIC = **1114.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8190** | 0.6437 | ±1.2873 | **-2.826** | **0.0047** | 0.1622 | ** |
| **Education: graduate level (vs college)** | **-0.5322** | 0.1674 | ±0.3348 | **-3.179** | **0.0015** | 0.5873 | ** |
| **Education: high school or below (vs college)** | **+0.6074** | 0.2281 | ±0.4562 | **+2.663** | **0.0077** | 1.8356 | ** |
| **Site: UCSD (vs UAB)** | **+0.4276** | 0.1904 | ±0.3807 | **+2.246** | **0.0247** | 1.5336 | * |
| Site: UW (vs UAB) | -0.0928 | 0.1816 | ±0.3633 | -0.511 | 0.6096 | 0.9114 |  |
| **Age (years)** | **+0.0265** | 0.0075 | ±0.0150 | **+3.521** | **4.31e-04** | 1.0268 | *** |
| BMI (kg/m2) | -0.0089 | 0.0111 | ±0.0221 | -0.810 | 0.4182 | 0.9911 |  |
| Hypertension | +0.2857 | 0.1696 | ±0.3393 | +1.684 | 0.0921 | 1.3307 | . |
| High cholesterol | -0.0382 | 0.1602 | ±0.3205 | -0.239 | 0.8114 | 0.9625 |  |
| Kidney disease | -0.3867 | 0.2108 | ±0.4216 | -1.834 | 0.0666 | 0.6793 | . |
| Circulatory disease | -0.1105 | 0.1983 | ±0.3966 | -0.557 | 0.5773 | 0.8954 |  |
| **Time > 180 (%)** | **+0.0085** | 0.0030 | ±0.0061 | **+2.783** | **0.0054** | 1.0085 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0583**, LLR χ² = **64.02** (p = **1.64e-09**), AUC = **0.6546**, AIC = **1058.5**, BIC = **1114.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8079** | 0.6433 | ±1.2866 | **-2.810** | **0.0049** | 0.1640 | ** |
| **Education: graduate level (vs college)** | **-0.5344** | 0.1673 | ±0.3347 | **-3.193** | **0.0014** | 0.5860 | ** |
| **Education: high school or below (vs college)** | **+0.6068** | 0.2281 | ±0.4562 | **+2.660** | **0.0078** | 1.8346 | ** |
| **Site: UCSD (vs UAB)** | **+0.4293** | 0.1904 | ±0.3808 | **+2.255** | **0.0241** | 1.5362 | * |
| Site: UW (vs UAB) | -0.0933 | 0.1816 | ±0.3632 | -0.514 | 0.6076 | 0.9110 |  |
| **Age (years)** | **+0.0264** | 0.0075 | ±0.0150 | **+3.513** | **4.44e-04** | 1.0267 | *** |
| BMI (kg/m2) | -0.0089 | 0.0111 | ±0.0221 | -0.806 | 0.4204 | 0.9911 |  |
| Hypertension | +0.2865 | 0.1696 | ±0.3392 | +1.689 | 0.0911 | 1.3318 | . |
| High cholesterol | -0.0388 | 0.1602 | ±0.3204 | -0.242 | 0.8087 | 0.9620 |  |
| Kidney disease | -0.3888 | 0.2109 | ±0.4218 | -1.843 | 0.0653 | 0.6779 | . |
| Circulatory disease | -0.1095 | 0.1982 | ±0.3965 | -0.552 | 0.5807 | 0.8963 |  |
| **Avg. daily time > 180 (%)** | **+0.0083** | 0.0030 | ±0.0061 | **+2.730** | **0.0063** | 1.0083 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0570**, LLR χ² = **62.60** (p = **3.04e-09**), AUC = **0.6551**, AIC = **1060.0**, BIC = **1116.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7695** | 0.6422 | ±1.2843 | **-2.756** | **0.0059** | 0.1704 | ** |
| **Education: graduate level (vs college)** | **-0.5197** | 0.1673 | ±0.3347 | **-3.106** | **0.0019** | 0.5947 | ** |
| **Education: high school or below (vs college)** | **+0.6284** | 0.2275 | ±0.4549 | **+2.763** | **0.0057** | 1.8745 | ** |
| **Site: UCSD (vs UAB)** | **+0.4254** | 0.1903 | ±0.3807 | **+2.235** | **0.0254** | 1.5302 | * |
| Site: UW (vs UAB) | -0.1064 | 0.1811 | ±0.3623 | -0.587 | 0.5571 | 0.8991 |  |
| **Age (years)** | **+0.0271** | 0.0075 | ±0.0150 | **+3.599** | **3.19e-04** | 1.0274 | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0222 | -0.837 | 0.4026 | 0.9907 |  |
| Hypertension | +0.2905 | 0.1694 | ±0.3389 | +1.714 | 0.0865 | 1.3371 | . |
| High cholesterol | -0.0329 | 0.1601 | ±0.3201 | -0.205 | 0.8373 | 0.9677 |  |
| Kidney disease | -0.3679 | 0.2101 | ±0.4203 | -1.751 | 0.0800 | 0.6922 | . |
| Circulatory disease | -0.1038 | 0.1982 | ±0.3963 | -0.524 | 0.6006 | 0.9014 |  |
| **Nocturnal time > 180 (%)** | **+0.0068** | 0.0028 | ±0.0055 | **+2.461** | **0.0139** | 1.0068 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0568**, LLR χ² = **62.40** (p = **3.32e-09**), AUC = **0.6541**, AIC = **1060.2**, BIC = **1116.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8277** | 0.6433 | ±1.2867 | **-2.841** | **0.0045** | 0.1608 | ** |
| **Education: graduate level (vs college)** | **-0.5182** | 0.1672 | ±0.3344 | **-3.099** | **0.0019** | 0.5956 | ** |
| **Education: high school or below (vs college)** | **+0.6249** | 0.2277 | ±0.4554 | **+2.745** | **0.0061** | 1.8681 | ** |
| **Site: UCSD (vs UAB)** | **+0.4161** | 0.1899 | ±0.3798 | **+2.191** | **0.0284** | 1.5161 | * |
| Site: UW (vs UAB) | -0.0914 | 0.1814 | ±0.3629 | -0.504 | 0.6143 | 0.9126 |  |
| **Age (years)** | **+0.0275** | 0.0075 | ±0.0151 | **+3.649** | **2.64e-04** | 1.0278 | *** |
| BMI (kg/m2) | -0.0061 | 0.0109 | ±0.0219 | -0.560 | 0.5752 | 0.9939 |  |
| Hypertension | +0.2793 | 0.1694 | ±0.3389 | +1.648 | 0.0993 | 1.3222 | . |
| High cholesterol | -0.0314 | 0.1601 | ±0.3202 | -0.196 | 0.8444 | 0.9691 |  |
| Kidney disease | -0.3627 | 0.2100 | ±0.4200 | -1.727 | 0.0841 | 0.6958 | . |
| Circulatory disease | -0.1048 | 0.1982 | ±0.3964 | -0.529 | 0.5970 | 0.9005 |  |
| **Time > 250 (%)** | **+0.0113** | 0.0047 | ±0.0095 | **+2.376** | **0.0175** | 1.0113 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 795)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **795**, events = **371**, McFadden pseudo-R² = **0.0565**, LLR χ² = **62.04** (p = **3.87e-09**), AUC = **0.6538**, AIC = **1060.5**, BIC = **1116.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8121** | 0.6427 | ±1.2854 | **-2.819** | **0.0048** | 0.1633 | ** |
| **Education: graduate level (vs college)** | **-0.5193** | 0.1672 | ±0.3343 | **-3.106** | **0.0019** | 0.5949 | ** |
| **Education: high school or below (vs college)** | **+0.6263** | 0.2276 | ±0.4553 | **+2.751** | **0.0059** | 1.8706 | ** |
| **Site: UCSD (vs UAB)** | **+0.4158** | 0.1899 | ±0.3798 | **+2.189** | **0.0286** | 1.5155 | * |
| Site: UW (vs UAB) | -0.0940 | 0.1814 | ±0.3627 | -0.518 | 0.6042 | 0.9103 |  |
| **Age (years)** | **+0.0273** | 0.0075 | ±0.0150 | **+3.627** | **2.87e-04** | 1.0276 | *** |
| BMI (kg/m2) | -0.0061 | 0.0109 | ±0.0219 | -0.557 | 0.5773 | 0.9939 |  |
| Hypertension | +0.2809 | 0.1694 | ±0.3388 | +1.658 | 0.0973 | 1.3243 | . |
| High cholesterol | -0.0319 | 0.1600 | ±0.3201 | -0.199 | 0.8422 | 0.9686 |  |
| Kidney disease | -0.3645 | 0.2101 | ±0.4202 | -1.735 | 0.0828 | 0.6946 | . |
| Circulatory disease | -0.1052 | 0.1982 | ±0.3964 | -0.531 | 0.5956 | 0.9002 |  |
| **Avg. daily time > 250 (%)** | **+0.0110** | 0.0048 | ±0.0096 | **+2.306** | **0.0211** | 1.0111 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 795; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **795**, R² = **0.0722**, Adj R² = **0.0604**, F-statistic = **6.10** (p = **5.47e-09**), Residual SE = **2.810** on **784** df, AIC = **3909.7**, BIC = **3961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6320** | 0.8113 | ±1.6225 | **+19.269** | **9.86e-83** | *** |
| Education: graduate level (vs college) | +0.1153 | 0.2219 | ±0.4437 | +0.520 | 0.6032 |  |
| **Education: high school or below (vs college)** | **-1.1389** | 0.3495 | ±0.6990 | **-3.259** | **0.0011** | ** |
| Site: UCSD (vs UAB) | +0.2204 | 0.2714 | ±0.5427 | +0.812 | 0.4166 |  |
| Site: UW (vs UAB) | +0.1810 | 0.2542 | ±0.5083 | +0.712 | 0.4764 |  |
| **Age (years)** | **-0.0545** | 0.0102 | ±0.0204 | **-5.346** | **9.00e-08** | *** |
| BMI (kg/m2) | +0.0019 | 0.0144 | ±0.0287 | +0.133 | 0.8946 |  |
| **Hypertension** | **-0.4944** | 0.2242 | ±0.4483 | **-2.206** | **0.0274** | * |
| High cholesterol | +0.3099 | 0.2131 | ±0.4262 | +1.454 | 0.1459 |  |
| Kidney disease | +0.3719 | 0.2785 | ±0.5570 | +1.335 | 0.1818 |  |
| Circulatory disease | +0.1845 | 0.2651 | ±0.5302 | +0.696 | 0.4864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **795**, R² = **0.0761**, Adj R² = **0.0632**, F-statistic = **5.87** (p = **3.36e-09**), Residual SE = **2.806** on **783** df, AIC = **3908.3**, BIC = **3964.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4788** | 0.9394 | ±1.8789 | **+17.541** | **6.97e-69** | *** |
| Education: graduate level (vs college) | +0.0867 | 0.2215 | ±0.4429 | +0.392 | 0.6954 |  |
| **Education: high school or below (vs college)** | **-1.0631** | 0.3536 | ±0.7072 | **-3.007** | **0.0026** | ** |
| Site: UCSD (vs UAB) | +0.1983 | 0.2730 | ±0.5460 | +0.726 | 0.4677 |  |
| Site: UW (vs UAB) | +0.1453 | 0.2559 | ±0.5118 | +0.568 | 0.5702 |  |
| **Age (years)** | **-0.0549** | 0.0102 | ±0.0204 | **-5.395** | **6.87e-08** | *** |
| BMI (kg/m2) | +0.0062 | 0.0146 | ±0.0293 | +0.422 | 0.6733 |  |
| **Hypertension** | **-0.4759** | 0.2228 | ±0.4456 | **-2.136** | **0.0327** | * |
| High cholesterol | +0.3259 | 0.2125 | ±0.4249 | +1.534 | 0.1250 |  |
| Kidney disease | +0.3769 | 0.2789 | ±0.5578 | +1.351 | 0.1766 |  |
| Circulatory disease | +0.2119 | 0.2661 | ±0.5321 | +0.797 | 0.4257 |  |
| HbA1c (%) | -0.1413 | 0.0741 | ±0.1482 | -1.908 | 0.0564 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **795**, R² = **0.0762**, Adj R² = **0.0633**, F-statistic = **5.87** (p = **3.25e-09**), Residual SE = **2.805** on **783** df, AIC = **3908.2**, BIC = **3964.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3179** | 0.8924 | ±1.7848 | **+18.285** | **1.09e-74** | *** |
| Education: graduate level (vs college) | +0.1000 | 0.2217 | ±0.4434 | +0.451 | 0.6520 |  |
| **Education: high school or below (vs college)** | **-1.0676** | 0.3490 | ±0.6981 | **-3.059** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1864 | 0.2731 | ±0.5462 | +0.683 | 0.4948 |  |
| Site: UW (vs UAB) | +0.1471 | 0.2554 | ±0.5109 | +0.576 | 0.5647 |  |
| **Age (years)** | **-0.0551** | 0.0102 | ±0.0204 | **-5.399** | **6.69e-08** | *** |
| BMI (kg/m2) | +0.0056 | 0.0146 | ±0.0291 | +0.387 | 0.6991 |  |
| **Hypertension** | **-0.4810** | 0.2233 | ±0.4467 | **-2.154** | **0.0313** | * |
| High cholesterol | +0.3179 | 0.2126 | ±0.4252 | +1.495 | 0.1349 |  |
| Kidney disease | +0.3999 | 0.2791 | ±0.5582 | +1.433 | 0.1519 |  |
| Circulatory disease | +0.2171 | 0.2652 | ±0.5304 | +0.819 | 0.4130 |  |
| **Mean glucose (mg/dL)** | **-0.0048** | 0.0024 | ±0.0047 | **-2.022** | **0.0432** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **795**, R² = **0.0762**, Adj R² = **0.0633**, F-statistic = **5.87** (p = **3.25e-09**), Residual SE = **2.805** on **783** df, AIC = **3908.2**, BIC = **3964.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9756** | 1.0689 | ±2.1379 | **+15.881** | **8.59e-57** | *** |
| Education: graduate level (vs college) | +0.1000 | 0.2217 | ±0.4434 | +0.451 | 0.6520 |  |
| **Education: high school or below (vs college)** | **-1.0676** | 0.3490 | ±0.6981 | **-3.059** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1864 | 0.2731 | ±0.5462 | +0.683 | 0.4948 |  |
| Site: UW (vs UAB) | +0.1471 | 0.2554 | ±0.5109 | +0.576 | 0.5647 |  |
| **Age (years)** | **-0.0551** | 0.0102 | ±0.0204 | **-5.399** | **6.69e-08** | *** |
| BMI (kg/m2) | +0.0056 | 0.0146 | ±0.0291 | +0.387 | 0.6991 |  |
| **Hypertension** | **-0.4810** | 0.2233 | ±0.4467 | **-2.154** | **0.0313** | * |
| High cholesterol | +0.3179 | 0.2126 | ±0.4252 | +1.495 | 0.1349 |  |
| Kidney disease | +0.3999 | 0.2791 | ±0.5582 | +1.433 | 0.1519 |  |
| Circulatory disease | +0.2171 | 0.2652 | ±0.5304 | +0.819 | 0.4130 |  |
| **GMI (%)** | **-0.1987** | 0.0983 | ±0.1965 | **-2.022** | **0.0432** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **795**, R² = **0.0771**, Adj R² = **0.0642**, F-statistic = **5.95** (p = **2.34e-09**), Residual SE = **2.804** on **783** df, AIC = **3907.4**, BIC = **3963.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3274** | 0.8660 | ±1.7319 | **+18.855** | **2.68e-79** | *** |
| Education: graduate level (vs college) | +0.0911 | 0.2213 | ±0.4426 | +0.412 | 0.6806 |  |
| **Education: high school or below (vs college)** | **-1.0695** | 0.3490 | ±0.6979 | **-3.065** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1844 | 0.2727 | ±0.5454 | +0.676 | 0.4988 |  |
| Site: UW (vs UAB) | +0.1558 | 0.2547 | ±0.5095 | +0.612 | 0.5408 |  |
| **Age (years)** | **-0.0559** | 0.0102 | ±0.0205 | **-5.459** | **4.78e-08** | *** |
| BMI (kg/m2) | +0.0071 | 0.0148 | ±0.0295 | +0.480 | 0.6311 |  |
| **Hypertension** | **-0.4843** | 0.2230 | ±0.4460 | **-2.172** | **0.0299** | * |
| High cholesterol | +0.3167 | 0.2124 | ±0.4248 | +1.491 | 0.1360 |  |
| Kidney disease | +0.3838 | 0.2788 | ±0.5577 | +1.377 | 0.1687 |  |
| Circulatory disease | +0.2176 | 0.2643 | ±0.5286 | +0.823 | 0.4104 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0050** | 0.0022 | ±0.0044 | **-2.231** | **0.0257** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **795**, R² = **0.0785**, Adj R² = **0.0656**, F-statistic = **6.06** (p = **1.41e-09**), Residual SE = **2.802** on **783** df, AIC = **3906.2**, BIC = **3962.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2600** | 0.8724 | ±1.7449 | **+18.638** | **1.59e-77** | *** |
| Education: graduate level (vs college) | +0.0836 | 0.2218 | ±0.4435 | +0.377 | 0.7061 |  |
| **Education: high school or below (vs college)** | **-1.0689** | 0.3509 | ±0.7017 | **-3.046** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.1808 | 0.2726 | ±0.5453 | +0.663 | 0.5073 |  |
| Site: UW (vs UAB) | +0.1106 | 0.2573 | ±0.5146 | +0.430 | 0.6673 |  |
| **Age (years)** | **-0.0543** | 0.0102 | ±0.0204 | **-5.327** | **9.99e-08** | *** |
| BMI (kg/m2) | +0.0060 | 0.0144 | ±0.0287 | +0.419 | 0.6753 |  |
| **Hypertension** | **-0.4662** | 0.2233 | ±0.4465 | **-2.088** | **0.0368** | * |
| High cholesterol | +0.3023 | 0.2116 | ±0.4233 | +1.428 | 0.1532 |  |
| Kidney disease | +0.4935 | 0.2783 | ±0.5566 | +1.773 | 0.0762 | . |
| Circulatory disease | +0.2177 | 0.2642 | ±0.5284 | +0.824 | 0.4100 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0200** | 0.0084 | ±0.0168 | **-2.388** | **0.0170** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **795**, R² = **0.0781**, Adj R² = **0.0651**, F-statistic = **6.03** (p = **1.64e-09**), Residual SE = **2.803** on **783** df, AIC = **3906.6**, BIC = **3962.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2605** | 0.8787 | ±1.7573 | **+18.506** | **1.86e-76** | *** |
| Education: graduate level (vs college) | +0.0917 | 0.2220 | ±0.4440 | +0.413 | 0.6796 |  |
| **Education: high school or below (vs college)** | **-1.0647** | 0.3503 | ±0.7006 | **-3.040** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +0.1819 | 0.2719 | ±0.5438 | +0.669 | 0.5034 |  |
| Site: UW (vs UAB) | +0.1191 | 0.2564 | ±0.5127 | +0.465 | 0.6422 |  |
| **Age (years)** | **-0.0541** | 0.0102 | ±0.0204 | **-5.303** | **1.14e-07** | *** |
| BMI (kg/m2) | +0.0049 | 0.0143 | ±0.0287 | +0.340 | 0.7342 |  |
| **Hypertension** | **-0.4711** | 0.2237 | ±0.4474 | **-2.106** | **0.0352** | * |
| High cholesterol | +0.3037 | 0.2122 | ±0.4243 | +1.431 | 0.1523 |  |
| Kidney disease | +0.4972 | 0.2777 | ±0.5555 | +1.790 | 0.0734 | . |
| Circulatory disease | +0.2117 | 0.2649 | ±0.5299 | +0.799 | 0.4242 |  |
| **Avg. daily SD (mg/dL)** | **-0.0219** | 0.0093 | ±0.0186 | **-2.361** | **0.0182** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **795**, R² = **0.0738**, Adj R² = **0.0608**, F-statistic = **5.67** (p = **7.89e-09**), Residual SE = **2.809** on **783** df, AIC = **3910.3**, BIC = **3966.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1118** | 0.9300 | ±1.8600 | **+17.324** | **3.10e-67** | *** |
| Education: graduate level (vs college) | +0.1022 | 0.2222 | ±0.4444 | +0.460 | 0.6454 |  |
| **Education: high school or below (vs college)** | **-1.1346** | 0.3508 | ±0.7016 | **-3.234** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.2090 | 0.2719 | ±0.5437 | +0.769 | 0.4420 |  |
| Site: UW (vs UAB) | +0.1519 | 0.2569 | ±0.5137 | +0.591 | 0.5543 |  |
| **Age (years)** | **-0.0540** | 0.0102 | ±0.0204 | **-5.282** | **1.27e-07** | *** |
| BMI (kg/m2) | +0.0024 | 0.0143 | ±0.0286 | +0.167 | 0.8673 |  |
| **Hypertension** | **-0.4820** | 0.2240 | ±0.4481 | **-2.151** | **0.0315** | * |
| High cholesterol | +0.2962 | 0.2133 | ±0.4267 | +1.389 | 0.1650 |  |
| Kidney disease | +0.4354 | 0.2779 | ±0.5559 | +1.566 | 0.1173 |  |
| Circulatory disease | +0.1864 | 0.2651 | ±0.5301 | +0.703 | 0.4818 |  |
| CV (%) | -0.0219 | 0.0178 | ±0.0355 | -1.235 | 0.2168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **795**, R² = **0.0728**, Adj R² = **0.0598**, F-statistic = **5.59** (p = **1.13e-08**), Residual SE = **2.811** on **783** df, AIC = **3911.1**, BIC = **3967.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2869** | 0.8880 | ±1.7759 | **+17.216** | **2.03e-66** | *** |
| Education: graduate level (vs college) | +0.1086 | 0.2220 | ±0.4441 | +0.489 | 0.6249 |  |
| **Education: high school or below (vs college)** | **-1.1370** | 0.3505 | ±0.7010 | **-3.244** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.2178 | 0.2717 | ±0.5434 | +0.802 | 0.4228 |  |
| Site: UW (vs UAB) | +0.1662 | 0.2573 | ±0.5146 | +0.646 | 0.5184 |  |
| **Age (years)** | **-0.0543** | 0.0102 | ±0.0204 | **-5.322** | **1.03e-07** | *** |
| BMI (kg/m2) | +0.0020 | 0.0143 | ±0.0287 | +0.140 | 0.8886 |  |
| **Hypertension** | **-0.4871** | 0.2240 | ±0.4480 | **-2.175** | **0.0297** | * |
| High cholesterol | +0.3057 | 0.2134 | ±0.4267 | +1.433 | 0.1519 |  |
| Kidney disease | +0.4046 | 0.2781 | ±0.5562 | +1.455 | 0.1457 |  |
| Circulatory disease | +0.1888 | 0.2651 | ±0.5302 | +0.712 | 0.4765 |  |
| Mean / SD ratio | +0.0735 | 0.1002 | ±0.2004 | +0.733 | 0.4633 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **795**, R² = **0.0726**, Adj R² = **0.0596**, F-statistic = **5.57** (p = **1.23e-08**), Residual SE = **2.811** on **783** df, AIC = **3911.3**, BIC = **3967.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3777** | 0.8738 | ±1.7477 | **+17.598** | **2.56e-69** | *** |
| Education: graduate level (vs college) | +0.1112 | 0.2224 | ±0.4447 | +0.500 | 0.6169 |  |
| **Education: high school or below (vs college)** | **-1.1368** | 0.3503 | ±0.7007 | **-3.245** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.2194 | 0.2716 | ±0.5433 | +0.808 | 0.4193 |  |
| Site: UW (vs UAB) | +0.1710 | 0.2570 | ±0.5141 | +0.665 | 0.5060 |  |
| **Age (years)** | **-0.0542** | 0.0102 | ±0.0203 | **-5.330** | **9.84e-08** | *** |
| BMI (kg/m2) | +0.0017 | 0.0144 | ±0.0288 | +0.120 | 0.9042 |  |
| **Hypertension** | **-0.4892** | 0.2243 | ±0.4486 | **-2.181** | **0.0292** | * |
| High cholesterol | +0.3056 | 0.2137 | ±0.4275 | +1.430 | 0.1527 |  |
| Kidney disease | +0.3962 | 0.2784 | ±0.5568 | +1.423 | 0.1547 |  |
| Circulatory disease | +0.1849 | 0.2653 | ±0.5305 | +0.697 | 0.4857 |  |
| Avg. daily mean/SD | +0.0464 | 0.0850 | ±0.1701 | +0.545 | 0.5855 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **795**, R² = **0.0748**, Adj R² = **0.0618**, F-statistic = **5.75** (p = **5.51e-09**), Residual SE = **2.808** on **783** df, AIC = **3909.4**, BIC = **3965.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4466** | 1.0239 | ±2.0478 | **+16.062** | **4.68e-58** | *** |
| Education: graduate level (vs college) | +0.0885 | 0.2260 | ±0.4521 | +0.392 | 0.6953 |  |
| **Education: high school or below (vs college)** | **-1.1240** | 0.3477 | ±0.6954 | **-3.233** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.1891 | 0.2701 | ±0.5402 | +0.700 | 0.4838 |  |
| Site: UW (vs UAB) | +0.1184 | 0.2569 | ±0.5139 | +0.461 | 0.6449 |  |
| **Age (years)** | **-0.0558** | 0.0103 | ±0.0205 | **-5.435** | **5.48e-08** | *** |
| BMI (kg/m2) | +0.0030 | 0.0143 | ±0.0286 | +0.208 | 0.8349 |  |
| **Hypertension** | **-0.5033** | 0.2238 | ±0.4476 | **-2.249** | **0.0245** | * |
| High cholesterol | +0.2864 | 0.2141 | ±0.4282 | +1.338 | 0.1810 |  |
| Kidney disease | +0.4054 | 0.2814 | ±0.5628 | +1.440 | 0.1497 |  |
| Circulatory disease | +0.1923 | 0.2678 | ±0.5356 | +0.718 | 0.4727 |  |
| MAG (mg/dL/h) | -0.0158 | 0.0111 | ±0.0222 | -1.424 | 0.1545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **795**, R² = **0.0764**, Adj R² = **0.0634**, F-statistic = **5.89** (p = **3.07e-09**), Residual SE = **2.805** on **783** df, AIC = **3908.1**, BIC = **3964.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4444** | 0.9479 | ±1.8959 | **+17.347** | **2.06e-67** | *** |
| Education: graduate level (vs college) | +0.0955 | 0.2230 | ±0.4460 | +0.428 | 0.6686 |  |
| **Education: high school or below (vs college)** | **-1.0783** | 0.3502 | ±0.7004 | **-3.079** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1804 | 0.2717 | ±0.5433 | +0.664 | 0.5066 |  |
| Site: UW (vs UAB) | +0.1242 | 0.2561 | ±0.5122 | +0.485 | 0.6278 |  |
| **Age (years)** | **-0.0549** | 0.0102 | ±0.0205 | **-5.360** | **8.33e-08** | *** |
| BMI (kg/m2) | +0.0036 | 0.0143 | ±0.0286 | +0.251 | 0.8015 |  |
| **Hypertension** | **-0.4877** | 0.2239 | ±0.4478 | **-2.178** | **0.0294** | * |
| High cholesterol | +0.3006 | 0.2124 | ±0.4248 | +1.415 | 0.1571 |  |
| Kidney disease | +0.4755 | 0.2786 | ±0.5571 | +1.707 | 0.0878 | . |
| Circulatory disease | +0.2094 | 0.2660 | ±0.5319 | +0.787 | 0.4310 |  |
| Avg. daily range (mg/dL) | -0.0055 | 0.0029 | ±0.0058 | -1.881 | 0.0600 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **795**, R² = **0.0750**, Adj R² = **0.0620**, F-statistic = **5.77** (p = **5.16e-09**), Residual SE = **2.807** on **783** df, AIC = **3909.3**, BIC = **3965.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8337** | 0.8250 | ±1.6499 | **+19.193** | **4.24e-82** | *** |
| Education: graduate level (vs college) | +0.0817 | 0.2218 | ±0.4436 | +0.369 | 0.7125 |  |
| **Education: high school or below (vs college)** | **-1.1198** | 0.3508 | ±0.7016 | **-3.192** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.2040 | 0.2735 | ±0.5470 | +0.746 | 0.4556 |  |
| Site: UW (vs UAB) | +0.1444 | 0.2577 | ±0.5153 | +0.560 | 0.5753 |  |
| **Age (years)** | **-0.0553** | 0.0102 | ±0.0204 | **-5.421** | **5.94e-08** | *** |
| BMI (kg/m2) | +0.0052 | 0.0144 | ±0.0288 | +0.362 | 0.7171 |  |
| **Hypertension** | **-0.4717** | 0.2228 | ±0.4457 | **-2.117** | **0.0343** | * |
| High cholesterol | +0.3086 | 0.2121 | ±0.4242 | +1.455 | 0.1456 |  |
| Kidney disease | +0.4062 | 0.2796 | ±0.5592 | +1.453 | 0.1464 |  |
| Circulatory disease | +0.2157 | 0.2631 | ±0.5262 | +0.820 | 0.4124 |  |
| SD of daily means (mg/dL) | -0.0194 | 0.0141 | ±0.0282 | -1.376 | 0.1689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **795**, R² = **0.0762**, Adj R² = **0.0632**, F-statistic = **5.87** (p = **3.33e-09**), Residual SE = **2.806** on **783** df, AIC = **3908.3**, BIC = **3964.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.9752** | 0.8577 | ±1.7153 | **+17.461** | **2.86e-68** | *** |
| Education: graduate level (vs college) | +0.0985 | 0.2216 | ±0.4432 | +0.444 | 0.6568 |  |
| **Education: high school or below (vs college)** | **-1.0706** | 0.3486 | ±0.6972 | **-3.071** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1803 | 0.2743 | ±0.5485 | +0.657 | 0.5110 |  |
| Site: UW (vs UAB) | +0.1407 | 0.2565 | ±0.5130 | +0.549 | 0.5833 |  |
| **Age (years)** | **-0.0547** | 0.0102 | ±0.0204 | **-5.371** | **7.83e-08** | *** |
| BMI (kg/m2) | +0.0063 | 0.0146 | ±0.0291 | +0.435 | 0.6636 |  |
| **Hypertension** | **-0.4856** | 0.2233 | ±0.4465 | **-2.175** | **0.0296** | * |
| High cholesterol | +0.3093 | 0.2122 | ±0.4244 | +1.457 | 0.1450 |  |
| Kidney disease | +0.4145 | 0.2785 | ±0.5570 | +1.488 | 0.1367 |  |
| Circulatory disease | +0.2116 | 0.2650 | ±0.5299 | +0.799 | 0.4245 |  |
| Time in range 70-180, pooled (%) | +0.0076 | 0.0039 | ±0.0078 | +1.948 | 0.0514 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **795**, R² = **0.0761**, Adj R² = **0.0631**, F-statistic = **5.86** (p = **3.40e-09**), Residual SE = **2.806** on **783** df, AIC = **3908.3**, BIC = **3964.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.9768** | 0.8597 | ±1.7193 | **+17.422** | **5.63e-68** | *** |
| Education: graduate level (vs college) | +0.1003 | 0.2217 | ±0.4433 | +0.452 | 0.6510 |  |
| **Education: high school or below (vs college)** | **-1.0698** | 0.3487 | ±0.6974 | **-3.068** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1783 | 0.2745 | ±0.5489 | +0.650 | 0.5158 |  |
| Site: UW (vs UAB) | +0.1404 | 0.2566 | ±0.5132 | +0.547 | 0.5843 |  |
| **Age (years)** | **-0.0547** | 0.0102 | ±0.0204 | **-5.365** | **8.08e-08** | *** |
| BMI (kg/m2) | +0.0064 | 0.0146 | ±0.0292 | +0.436 | 0.6626 |  |
| **Hypertension** | **-0.4863** | 0.2233 | ±0.4465 | **-2.178** | **0.0294** | * |
| High cholesterol | +0.3096 | 0.2123 | ±0.4245 | +1.458 | 0.1447 |  |
| Kidney disease | +0.4167 | 0.2784 | ±0.5568 | +1.497 | 0.1345 |  |
| Circulatory disease | +0.2110 | 0.2649 | ±0.5299 | +0.796 | 0.4258 |  |
| Avg. daily time in range 70-180 (%) | +0.0074 | 0.0039 | ±0.0077 | +1.924 | 0.0544 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **795**, R² = **0.0723**, Adj R² = **0.0593**, F-statistic = **5.55** (p = **1.35e-08**), Residual SE = **2.811** on **783** df, AIC = **3911.6**, BIC = **3967.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6055** | 0.8181 | ±1.6362 | **+19.075** | **4.08e-81** | *** |
| Education: graduate level (vs college) | +0.1173 | 0.2221 | ±0.4443 | +0.528 | 0.5975 |  |
| **Education: high school or below (vs college)** | **-1.1352** | 0.3499 | ±0.6999 | **-3.244** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.2243 | 0.2724 | ±0.5448 | +0.823 | 0.4103 |  |
| Site: UW (vs UAB) | +0.1851 | 0.2556 | ±0.5112 | +0.724 | 0.4691 |  |
| **Age (years)** | **-0.0544** | 0.0102 | ±0.0204 | **-5.336** | **9.52e-08** | *** |
| BMI (kg/m2) | +0.0018 | 0.0144 | ±0.0288 | +0.128 | 0.8978 |  |
| **Hypertension** | **-0.4984** | 0.2250 | ±0.4500 | **-2.215** | **0.0268** | * |
| High cholesterol | +0.3153 | 0.2139 | ±0.4277 | +1.474 | 0.1404 |  |
| Kidney disease | +0.3708 | 0.2789 | ±0.5578 | +1.330 | 0.1837 |  |
| Circulatory disease | +0.1805 | 0.2652 | ±0.5304 | +0.681 | 0.4960 |  |
| Any reading < 54 during wear (0/1) | +0.0741 | 0.2329 | ±0.4659 | +0.318 | 0.7504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **795**, R² = **0.0722**, Adj R² = **0.0592**, F-statistic = **5.54** (p = **1.40e-08**), Residual SE = **2.812** on **783** df, AIC = **3911.7**, BIC = **3967.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6268** | 0.8150 | ±1.6301 | **+19.173** | **6.20e-82** | *** |
| Education: graduate level (vs college) | +0.1167 | 0.2222 | ±0.4444 | +0.525 | 0.5996 |  |
| **Education: high school or below (vs college)** | **-1.1373** | 0.3496 | ±0.6992 | **-3.253** | **0.0011** | ** |
| Site: UCSD (vs UAB) | +0.2224 | 0.2725 | ±0.5449 | +0.816 | 0.4144 |  |
| Site: UW (vs UAB) | +0.1834 | 0.2559 | ±0.5117 | +0.717 | 0.4736 |  |
| **Age (years)** | **-0.0546** | 0.0102 | ±0.0204 | **-5.339** | **9.37e-08** | *** |
| BMI (kg/m2) | +0.0020 | 0.0145 | ±0.0289 | +0.137 | 0.8912 |  |
| **Hypertension** | **-0.4944** | 0.2242 | ±0.4484 | **-2.205** | **0.0274** | * |
| High cholesterol | +0.3117 | 0.2142 | ±0.4285 | +1.455 | 0.1457 |  |
| Kidney disease | +0.3721 | 0.2785 | ±0.5570 | +1.336 | 0.1814 |  |
| Circulatory disease | +0.1854 | 0.2653 | ±0.5307 | +0.699 | 0.4847 |  |
| Time < 54 (%) | +0.0188 | 0.0882 | ±0.1764 | +0.214 | 0.8308 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **795**, R² = **0.0724**, Adj R² = **0.0593**, F-statistic = **5.55** (p = **1.33e-08**), Residual SE = **2.811** on **783** df, AIC = **3911.5**, BIC = **3967.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6477** | 0.8147 | ±1.6294 | **+19.206** | **3.29e-82** | *** |
| Education: graduate level (vs college) | +0.1112 | 0.2222 | ±0.4445 | +0.500 | 0.6169 |  |
| **Education: high school or below (vs college)** | **-1.1450** | 0.3496 | ±0.6993 | **-3.275** | **0.0011** | ** |
| Site: UCSD (vs UAB) | +0.2132 | 0.2726 | ±0.5451 | +0.782 | 0.4340 |  |
| Site: UW (vs UAB) | +0.1713 | 0.2565 | ±0.5129 | +0.668 | 0.5043 |  |
| **Age (years)** | **-0.0544** | 0.0102 | ±0.0204 | **-5.326** | **1.01e-07** | *** |
| BMI (kg/m2) | +0.0017 | 0.0144 | ±0.0288 | +0.121 | 0.9035 |  |
| **Hypertension** | **-0.4938** | 0.2243 | ±0.4486 | **-2.201** | **0.0277** | * |
| High cholesterol | +0.3024 | 0.2147 | ±0.4295 | +1.408 | 0.1590 |  |
| Kidney disease | +0.3724 | 0.2787 | ±0.5575 | +1.336 | 0.1815 |  |
| Circulatory disease | +0.1814 | 0.2653 | ±0.5307 | +0.684 | 0.4941 |  |
| Avg. daily time < 54 (%) | -0.0784 | 0.1891 | ±0.3782 | -0.415 | 0.6785 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **795**, R² = **0.0728**, Adj R² = **0.0598**, F-statistic = **5.59** (p = **1.14e-08**), Residual SE = **2.811** on **783** df, AIC = **3911.2**, BIC = **3967.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6606** | 0.8138 | ±1.6276 | **+19.244** | **1.60e-82** | *** |
| Education: graduate level (vs college) | +0.1062 | 0.2225 | ±0.4449 | +0.478 | 0.6329 |  |
| **Education: high school or below (vs college)** | **-1.1470** | 0.3493 | ±0.6986 | **-3.284** | **0.0010** | ** |
| Site: UCSD (vs UAB) | +0.2045 | 0.2723 | ±0.5447 | +0.751 | 0.4526 |  |
| Site: UW (vs UAB) | +0.1632 | 0.2559 | ±0.5119 | +0.638 | 0.5236 |  |
| **Age (years)** | **-0.0543** | 0.0102 | ±0.0204 | **-5.314** | **1.07e-07** | *** |
| BMI (kg/m2) | +0.0020 | 0.0143 | ±0.0287 | +0.137 | 0.8912 |  |
| **Hypertension** | **-0.4891** | 0.2248 | ±0.4495 | **-2.176** | **0.0295** | * |
| High cholesterol | +0.2930 | 0.2151 | ±0.4302 | +1.362 | 0.1732 |  |
| Kidney disease | +0.3780 | 0.2783 | ±0.5565 | +1.358 | 0.1743 |  |
| Circulatory disease | +0.1759 | 0.2661 | ±0.5322 | +0.661 | 0.5086 |  |
| Time 54-69, pooled (%) | -0.0688 | 0.1011 | ±0.2022 | -0.680 | 0.4963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **795**, R² = **0.0739**, Adj R² = **0.0608**, F-statistic = **5.68** (p = **7.74e-09**), Residual SE = **2.809** on **783** df, AIC = **3910.2**, BIC = **3966.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6685** | 0.8118 | ±1.6235 | **+19.302** | **5.15e-83** | *** |
| Education: graduate level (vs college) | +0.0984 | 0.2225 | ±0.4450 | +0.442 | 0.6582 |  |
| **Education: high school or below (vs college)** | **-1.1544** | 0.3491 | ±0.6981 | **-3.307** | **9.43e-04** | *** |
| Site: UCSD (vs UAB) | +0.1934 | 0.2726 | ±0.5451 | +0.710 | 0.4780 |  |
| Site: UW (vs UAB) | +0.1477 | 0.2566 | ±0.5131 | +0.576 | 0.5649 |  |
| **Age (years)** | **-0.0540** | 0.0102 | ±0.0204 | **-5.288** | **1.24e-07** | *** |
| BMI (kg/m2) | +0.0021 | 0.0143 | ±0.0286 | +0.150 | 0.8807 |  |
| **Hypertension** | **-0.4854** | 0.2249 | ±0.4499 | **-2.158** | **0.0309** | * |
| High cholesterol | +0.2801 | 0.2154 | ±0.4309 | +1.300 | 0.1935 |  |
| Kidney disease | +0.3811 | 0.2781 | ±0.5562 | +1.370 | 0.1706 |  |
| Circulatory disease | +0.1679 | 0.2662 | ±0.5324 | +0.631 | 0.5282 |  |
| Avg. daily time 54-69 (%) | -0.1107 | 0.1106 | ±0.2212 | -1.001 | 0.3171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **795**, R² = **0.0725**, Adj R² = **0.0594**, F-statistic = **5.56** (p = **1.28e-08**), Residual SE = **2.811** on **783** df, AIC = **3911.4**, BIC = **3967.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6564** | 0.8155 | ±1.6309 | **+19.199** | **3.75e-82** | *** |
| Education: graduate level (vs college) | +0.1082 | 0.2226 | ±0.4451 | +0.486 | 0.6269 |  |
| **Education: high school or below (vs college)** | **-1.1461** | 0.3493 | ±0.6987 | **-3.281** | **0.0010** | ** |
| Site: UCSD (vs UAB) | +0.2086 | 0.2728 | ±0.5456 | +0.765 | 0.4444 |  |
| Site: UW (vs UAB) | +0.1674 | 0.2565 | ±0.5131 | +0.653 | 0.5140 |  |
| **Age (years)** | **-0.0543** | 0.0102 | ±0.0204 | **-5.315** | **1.07e-07** | *** |
| BMI (kg/m2) | +0.0018 | 0.0144 | ±0.0288 | +0.124 | 0.9011 |  |
| **Hypertension** | **-0.4917** | 0.2244 | ±0.4489 | **-2.191** | **0.0285** | * |
| High cholesterol | +0.2979 | 0.2153 | ±0.4306 | +1.384 | 0.1665 |  |
| Kidney disease | +0.3745 | 0.2785 | ±0.5569 | +1.345 | 0.1787 |  |
| Circulatory disease | +0.1784 | 0.2659 | ±0.5318 | +0.671 | 0.5023 |  |
| Time < 70 (%) | -0.0352 | 0.0631 | ±0.1261 | -0.559 | 0.5765 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **795**, R² = **0.0735**, Adj R² = **0.0604**, F-statistic = **5.64** (p = **8.97e-09**), Residual SE = **2.810** on **783** df, AIC = **3910.6**, BIC = **3966.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6706** | 0.8131 | ±1.6262 | **+19.273** | **9.07e-83** | *** |
| Education: graduate level (vs college) | +0.1003 | 0.2226 | ±0.4451 | +0.451 | 0.6521 |  |
| **Education: high school or below (vs college)** | **-1.1547** | 0.3492 | ±0.6984 | **-3.307** | **9.43e-04** | *** |
| Site: UCSD (vs UAB) | +0.1959 | 0.2729 | ±0.5457 | +0.718 | 0.4727 |  |
| Site: UW (vs UAB) | +0.1500 | 0.2570 | ±0.5140 | +0.584 | 0.5594 |  |
| **Age (years)** | **-0.0541** | 0.0102 | ±0.0204 | **-5.295** | **1.19e-07** | *** |
| BMI (kg/m2) | +0.0019 | 0.0143 | ±0.0286 | +0.134 | 0.8933 |  |
| **Hypertension** | **-0.4880** | 0.2246 | ±0.4491 | **-2.173** | **0.0298** | * |
| High cholesterol | +0.2834 | 0.2156 | ±0.4311 | +1.314 | 0.1887 |  |
| Kidney disease | +0.3785 | 0.2784 | ±0.5568 | +1.360 | 0.1739 |  |
| Circulatory disease | +0.1707 | 0.2660 | ±0.5319 | +0.642 | 0.5209 |  |
| Avg. daily time < 70 (%) | -0.0728 | 0.0721 | ±0.1441 | -1.010 | 0.3124 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **795**, R² = **0.0753**, Adj R² = **0.0624**, F-statistic = **5.80** (p = **4.50e-09**), Residual SE = **2.807** on **783** df, AIC = **3909.0**, BIC = **3965.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.7447** | 0.9254 | ±1.8508 | **+15.933** | **3.73e-57** | *** |
| Education: graduate level (vs college) | +0.0902 | 0.2221 | ±0.4441 | +0.406 | 0.6845 |  |
| **Education: high school or below (vs college)** | **-1.0837** | 0.3495 | ±0.6991 | **-3.100** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1889 | 0.2727 | ±0.5455 | +0.693 | 0.4885 |  |
| Site: UW (vs UAB) | +0.1397 | 0.2559 | ±0.5119 | +0.546 | 0.5851 |  |
| **Age (years)** | **-0.0558** | 0.0102 | ±0.0205 | **-5.446** | **5.15e-08** | *** |
| BMI (kg/m2) | +0.0037 | 0.0145 | ±0.0290 | +0.259 | 0.7957 |  |
| **Hypertension** | **-0.4808** | 0.2236 | ±0.4473 | **-2.150** | **0.0316** | * |
| High cholesterol | +0.3045 | 0.2122 | ±0.4244 | +1.435 | 0.1513 |  |
| Kidney disease | +0.3952 | 0.2793 | ±0.5585 | +1.415 | 0.1570 |  |
| Circulatory disease | +0.2088 | 0.2655 | ±0.5310 | +0.786 | 0.4316 |  |
| Time 54-250, pooled (%) | +0.0100 | 0.0055 | ±0.0109 | +1.835 | 0.0664 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **795**, R² = **0.0751**, Adj R² = **0.0621**, F-statistic = **5.78** (p = **4.95e-09**), Residual SE = **2.807** on **783** df, AIC = **3909.2**, BIC = **3965.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.7601** | 0.9297 | ±1.8594 | **+15.876** | **9.30e-57** | *** |
| Education: graduate level (vs college) | +0.0917 | 0.2222 | ±0.4443 | +0.413 | 0.6797 |  |
| **Education: high school or below (vs college)** | **-1.0860** | 0.3494 | ±0.6989 | **-3.108** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1898 | 0.2728 | ±0.5455 | +0.696 | 0.4865 |  |
| Site: UW (vs UAB) | +0.1427 | 0.2558 | ±0.5116 | +0.558 | 0.5770 |  |
| **Age (years)** | **-0.0556** | 0.0102 | ±0.0205 | **-5.433** | **5.54e-08** | *** |
| BMI (kg/m2) | +0.0037 | 0.0145 | ±0.0290 | +0.257 | 0.7970 |  |
| **Hypertension** | **-0.4822** | 0.2237 | ±0.4473 | **-2.156** | **0.0311** | * |
| High cholesterol | +0.3046 | 0.2123 | ±0.4245 | +1.435 | 0.1513 |  |
| Kidney disease | +0.3966 | 0.2793 | ±0.5586 | +1.420 | 0.1556 |  |
| Circulatory disease | +0.2091 | 0.2656 | ±0.5313 | +0.787 | 0.4312 |  |
| Avg. daily time 54-250 (%) | +0.0097 | 0.0055 | ±0.0110 | +1.770 | 0.0767 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **795**, R² = **0.0739**, Adj R² = **0.0609**, F-statistic = **5.68** (p = **7.61e-09**), Residual SE = **2.809** on **783** df, AIC = **3910.2**, BIC = **3966.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6409** | 0.8125 | ±1.6251 | **+19.249** | **1.43e-82** | *** |
| Education: graduate level (vs college) | +0.1187 | 0.2222 | ±0.4444 | +0.534 | 0.5933 |  |
| **Education: high school or below (vs college)** | **-1.1084** | 0.3492 | ±0.6983 | **-3.174** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.2042 | 0.2734 | ±0.5469 | +0.747 | 0.4553 |  |
| Site: UW (vs UAB) | +0.1730 | 0.2550 | ±0.5101 | +0.678 | 0.4977 |  |
| **Age (years)** | **-0.0537** | 0.0102 | ±0.0204 | **-5.278** | **1.31e-07** | *** |
| BMI (kg/m2) | +0.0053 | 0.0146 | ±0.0291 | +0.361 | 0.7181 |  |
| **Hypertension** | **-0.4966** | 0.2242 | ±0.4484 | **-2.215** | **0.0267** | * |
| High cholesterol | +0.3158 | 0.2133 | ±0.4266 | +1.480 | 0.1388 |  |
| Kidney disease | +0.3988 | 0.2779 | ±0.5558 | +1.435 | 0.1513 |  |
| Circulatory disease | +0.1953 | 0.2649 | ±0.5298 | +0.737 | 0.4610 |  |
| Time 181-250, pooled (%) | -0.0083 | 0.0066 | ±0.0132 | -1.267 | 0.2053 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **795**, R² = **0.0740**, Adj R² = **0.0610**, F-statistic = **5.69** (p = **7.36e-09**), Residual SE = **2.809** on **783** df, AIC = **3910.1**, BIC = **3966.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6432** | 0.8131 | ±1.6262 | **+19.239** | **1.76e-82** | *** |
| Education: graduate level (vs college) | +0.1200 | 0.2223 | ±0.4445 | +0.540 | 0.5891 |  |
| **Education: high school or below (vs college)** | **-1.1054** | 0.3494 | ±0.6988 | **-3.164** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.2014 | 0.2737 | ±0.5474 | +0.736 | 0.4618 |  |
| Site: UW (vs UAB) | +0.1708 | 0.2553 | ±0.5105 | +0.669 | 0.5035 |  |
| **Age (years)** | **-0.0538** | 0.0102 | ±0.0204 | **-5.283** | **1.27e-07** | *** |
| BMI (kg/m2) | +0.0054 | 0.0146 | ±0.0292 | +0.367 | 0.7138 |  |
| **Hypertension** | **-0.4964** | 0.2241 | ±0.4482 | **-2.215** | **0.0267** | * |
| High cholesterol | +0.3164 | 0.2134 | ±0.4267 | +1.483 | 0.1381 |  |
| Kidney disease | +0.4004 | 0.2777 | ±0.5554 | +1.442 | 0.1493 |  |
| Circulatory disease | +0.1944 | 0.2648 | ±0.5296 | +0.734 | 0.4628 |  |
| Avg. daily time 181-250 (%) | -0.0084 | 0.0065 | ±0.0130 | -1.292 | 0.1965 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **795**, R² = **0.0760**, Adj R² = **0.0630**, F-statistic = **5.85** (p = **3.55e-09**), Residual SE = **2.806** on **783** df, AIC = **3908.4**, BIC = **3964.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7222** | 0.8166 | ±1.6333 | **+19.253** | **1.34e-82** | *** |
| Education: graduate level (vs college) | +0.1005 | 0.2216 | ±0.4432 | +0.453 | 0.6503 |  |
| **Education: high school or below (vs college)** | **-1.0712** | 0.3486 | ±0.6973 | **-3.073** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1840 | 0.2740 | ±0.5480 | +0.671 | 0.5019 |  |
| Site: UW (vs UAB) | +0.1448 | 0.2562 | ±0.5124 | +0.565 | 0.5720 |  |
| **Age (years)** | **-0.0548** | 0.0102 | ±0.0204 | **-5.373** | **7.75e-08** | *** |
| BMI (kg/m2) | +0.0062 | 0.0146 | ±0.0292 | +0.427 | 0.6697 |  |
| **Hypertension** | **-0.4864** | 0.2233 | ±0.4466 | **-2.178** | **0.0294** | * |
| High cholesterol | +0.3118 | 0.2124 | ±0.4247 | +1.468 | 0.1421 |  |
| Kidney disease | +0.4126 | 0.2786 | ±0.5572 | +1.481 | 0.1386 |  |
| Circulatory disease | +0.2120 | 0.2650 | ±0.5300 | +0.800 | 0.4237 |  |
| Time > 180 (%) | -0.0073 | 0.0038 | ±0.0077 | -1.907 | 0.0565 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **795**, R² = **0.0758**, Adj R² = **0.0628**, F-statistic = **5.84** (p = **3.80e-09**), Residual SE = **2.806** on **783** df, AIC = **3908.6**, BIC = **3964.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7128** | 0.8165 | ±1.6330 | **+19.244** | **1.57e-82** | *** |
| Education: graduate level (vs college) | +0.1024 | 0.2217 | ±0.4434 | +0.462 | 0.6440 |  |
| **Education: high school or below (vs college)** | **-1.0714** | 0.3488 | ±0.6976 | **-3.072** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1827 | 0.2742 | ±0.5484 | +0.666 | 0.5052 |  |
| Site: UW (vs UAB) | +0.1453 | 0.2563 | ±0.5126 | +0.567 | 0.5708 |  |
| **Age (years)** | **-0.0547** | 0.0102 | ±0.0204 | **-5.367** | **7.99e-08** | *** |
| BMI (kg/m2) | +0.0062 | 0.0146 | ±0.0292 | +0.421 | 0.6734 |  |
| **Hypertension** | **-0.4873** | 0.2233 | ±0.4467 | **-2.182** | **0.0291** | * |
| High cholesterol | +0.3122 | 0.2125 | ±0.4249 | +1.469 | 0.1417 |  |
| Kidney disease | +0.4140 | 0.2785 | ±0.5569 | +1.487 | 0.1371 |  |
| Circulatory disease | +0.2111 | 0.2650 | ±0.5301 | +0.797 | 0.4257 |  |
| Avg. daily time > 180 (%) | -0.0071 | 0.0038 | ±0.0077 | -1.852 | 0.0641 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **795**, R² = **0.0762**, Adj R² = **0.0632**, F-statistic = **5.87** (p = **3.33e-09**), Residual SE = **2.806** on **783** df, AIC = **3908.3**, BIC = **3964.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6888** | 0.8142 | ±1.6283 | **+19.270** | **9.64e-83** | *** |
| Education: graduate level (vs college) | +0.0869 | 0.2209 | ±0.4418 | +0.393 | 0.6941 |  |
| **Education: high school or below (vs college)** | **-1.0825** | 0.3487 | ±0.6973 | **-3.105** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1799 | 0.2740 | ±0.5479 | +0.657 | 0.5113 |  |
| Site: UW (vs UAB) | +0.1532 | 0.2553 | ±0.5106 | +0.600 | 0.5484 |  |
| **Age (years)** | **-0.0554** | 0.0102 | ±0.0205 | **-5.411** | **6.26e-08** | *** |
| BMI (kg/m2) | +0.0073 | 0.0148 | ±0.0297 | +0.490 | 0.6239 |  |
| **Hypertension** | **-0.4911** | 0.2232 | ±0.4463 | **-2.201** | **0.0278** | * |
| High cholesterol | +0.3069 | 0.2122 | ±0.4245 | +1.446 | 0.1481 |  |
| Kidney disease | +0.4002 | 0.2784 | ±0.5569 | +1.437 | 0.1506 |  |
| Circulatory disease | +0.2099 | 0.2643 | ±0.5286 | +0.794 | 0.4270 |  |
| Nocturnal time > 180 (%) | -0.0068 | 0.0035 | ±0.0070 | -1.944 | 0.0518 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **795**, R² = **0.0754**, Adj R² = **0.0624**, F-statistic = **5.80** (p = **4.48e-09**), Residual SE = **2.807** on **783** df, AIC = **3909.0**, BIC = **3965.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7452** | 0.8178 | ±1.6357 | **+19.252** | **1.35e-82** | *** |
| Education: graduate level (vs college) | +0.0909 | 0.2220 | ±0.4440 | +0.409 | 0.6822 |  |
| **Education: high school or below (vs college)** | **-1.0827** | 0.3496 | ±0.6992 | **-3.097** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.1899 | 0.2726 | ±0.5453 | +0.697 | 0.4860 |  |
| Site: UW (vs UAB) | +0.1409 | 0.2558 | ±0.5116 | +0.551 | 0.5816 |  |
| **Age (years)** | **-0.0558** | 0.0102 | ±0.0205 | **-5.447** | **5.12e-08** | *** |
| BMI (kg/m2) | +0.0038 | 0.0145 | ±0.0290 | +0.262 | 0.7934 |  |
| **Hypertension** | **-0.4808** | 0.2236 | ±0.4473 | **-2.150** | **0.0316** | * |
| High cholesterol | +0.3054 | 0.2122 | ±0.4244 | +1.439 | 0.1501 |  |
| Kidney disease | +0.3954 | 0.2792 | ±0.5585 | +1.416 | 0.1568 |  |
| Circulatory disease | +0.2093 | 0.2655 | ±0.5311 | +0.788 | 0.4305 |  |
| Time > 250 (%) | -0.0100 | 0.0055 | ±0.0109 | -1.840 | 0.0658 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 795)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **795**, R² = **0.0750**, Adj R² = **0.0620**, F-statistic = **5.77** (p = **5.03e-09**), Residual SE = **2.807** on **783** df, AIC = **3909.2**, BIC = **3965.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7290** | 0.8171 | ±1.6342 | **+19.250** | **1.42e-82** | *** |
| Education: graduate level (vs college) | +0.0924 | 0.2221 | ±0.4443 | +0.416 | 0.6774 |  |
| **Education: high school or below (vs college)** | **-1.0857** | 0.3495 | ±0.6990 | **-3.106** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1910 | 0.2727 | ±0.5453 | +0.700 | 0.4837 |  |
| Site: UW (vs UAB) | +0.1442 | 0.2557 | ±0.5114 | +0.564 | 0.5728 |  |
| **Age (years)** | **-0.0556** | 0.0102 | ±0.0205 | **-5.432** | **5.56e-08** | *** |
| BMI (kg/m2) | +0.0037 | 0.0145 | ±0.0290 | +0.257 | 0.7969 |  |
| **Hypertension** | **-0.4824** | 0.2237 | ±0.4473 | **-2.157** | **0.0310** | * |
| High cholesterol | +0.3056 | 0.2123 | ±0.4246 | +1.439 | 0.1501 |  |
| Kidney disease | +0.3964 | 0.2793 | ±0.5585 | +1.419 | 0.1558 |  |
| Circulatory disease | +0.2093 | 0.2657 | ±0.5313 | +0.788 | 0.4308 |  |
| Avg. daily time > 250 (%) | -0.0096 | 0.0055 | ±0.0110 | -1.758 | 0.0788 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 90 single-predictor tests; 43 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 90 tests (samples with n >= 500), of which **8** are significant at BH q < 0.05 in the all-tests family and 29 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 795): best single predictor out of sample is **SD (pooled)** (CV R² 0.055 vs 0.047 for covariates alone, gain +0.007; -0.36 per SD, p = 0.004, q = 0.041). FDR-robust associations (5): SD (pooled) (lower outcome, -0.36 per SD, q = 0.041); GMI (lower outcome, -0.365 per SD, q = 0.045); Mean glucose (lower outcome, -0.365 per SD, q = 0.045); %>180 (pooled) (lower outcome, -0.362 per SD, q = 0.046); TIR 70-180 (pooled) (higher outcome, +0.36 per SD, q = 0.046).
- **Cognitive impairment (MoCA < 26)** (n = 795): best single predictor out of sample is **SD (pooled)** (CV AUC 0.626 vs 0.621 for covariates alone, gain +0.005; OR 1.24 per SD, p = 0.008, q = 0.056). FDR-robust associations (3): TIR 70-180 (pooled) (lower outcome, OR 0.80 per SD, q = 0.046); %>180 (pooled) (higher outcome, OR 1.24 per SD, q = 0.046); TIR 70-180 (daily avg) (lower outcome, OR 0.80 per SD, q = 0.046).
- **MoCA memory index score (0-15)** (n = 795): best single predictor out of sample is **Nocturnal mean** (CV R² 0.040 vs 0.035 for covariates alone, gain +0.005; -0.214 per SD, p = 0.026, q = 0.115). No association survives FDR; nominal only: SD (pooled) (p = 0.017), SD (daily avg) (p = 0.018), Nocturnal mean (p = 0.026), GMI (p = 0.043).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA total score (0-30) (+0.007, via SD (pooled)); Cognitive impairment (MoCA < 26) (+0.005, via SD (pooled)); MoCA memory index score (0-15) (+0.005, via Nocturnal mean). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Range 70-180 (3 FDR-significant / 4 raw-significant of 6); CGM level (2 FDR-significant / 9 raw-significant of 9); Band > 180 (2 FDR-significant / 6 raw-significant of 9).
Level metrics: 2 FDR-significant (9 raw); variability metrics: 1 FDR-significant (11 raw); HbA1c alone: 0 FDR-significant (2 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (Mean glucose, ΔAIC -3.0); Cognitive impairment (TIR 70-180 (pooled), ΔAIC -3.1); MoCA memory index score (SD (pooled), ΔAIC -2.0).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
