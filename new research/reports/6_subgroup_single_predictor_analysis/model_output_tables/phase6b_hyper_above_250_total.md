# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Total analysis base

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 793; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **793**, R² = **0.1469**, Adj R² = **0.1360**, F-statistic = **13.47** (p = **5.13e-22**), Residual SE = **4.800** on **782** df, AIC = **4749.2**, BIC = **4800.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5398** | 1.4612 | ±2.9224 | **+7.213** | **5.47e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0567** | 0.3573 | ±0.7145 | **-2.958** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+1.4950** | 0.6077 | ±1.2153 | **+2.460** | **0.0139** | * |
| Site: UCSD (vs UAB) | -0.2142 | 0.4675 | ±0.9349 | -0.458 | 0.6468 |  |
| Site: UW (vs UAB) | -0.7134 | 0.4037 | ±0.8075 | -1.767 | 0.0772 | . |
| **Age (years)** | **-0.1135** | 0.0162 | ±0.0325 | **-6.990** | **2.74e-12** | *** |
| **BMI (kg/m2)** | **+0.0645** | 0.0274 | ±0.0548 | **+2.351** | **0.0187** | * |
| Hypertension | +0.3963 | 0.3727 | ±0.7454 | +1.063 | 0.2876 |  |
| High cholesterol | +0.4108 | 0.3621 | ±0.7242 | +1.135 | 0.2565 |  |
| Kidney disease | +0.9556 | 0.5192 | ±1.0384 | +1.841 | 0.0657 | . |
| **Circulatory disease** | **+1.6761** | 0.5081 | ±1.0163 | **+3.299** | **9.72e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **793**, R² = **0.1491**, Adj R² = **0.1371**, F-statistic = **12.44** (p = **7.71e-22**), Residual SE = **4.797** on **781** df, AIC = **4749.2**, BIC = **4805.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4280** | 1.7288 | ±3.4576 | **+5.453** | **4.94e-08** | *** |
| **Education: graduate level (vs college)** | **-1.0187** | 0.3576 | ±0.7151 | **-2.849** | **0.0044** | ** |
| **Education: high school or below (vs college)** | **+1.3926** | 0.6047 | ±1.2094 | **+2.303** | **0.0213** | * |
| Site: UCSD (vs UAB) | -0.1852 | 0.4681 | ±0.9361 | -0.396 | 0.6923 |  |
| Site: UW (vs UAB) | -0.6679 | 0.4083 | ±0.8167 | -1.636 | 0.1019 |  |
| **Age (years)** | **-0.1130** | 0.0163 | ±0.0325 | **-6.954** | **3.56e-12** | *** |
| **BMI (kg/m2)** | **+0.0588** | 0.0279 | ±0.0558 | **+2.107** | **0.0351** | * |
| Hypertension | +0.3715 | 0.3749 | ±0.7498 | +0.991 | 0.3217 |  |
| High cholesterol | +0.3900 | 0.3605 | ±0.7210 | +1.082 | 0.2793 |  |
| Kidney disease | +0.9497 | 0.5208 | ±1.0416 | +1.823 | 0.0682 | . |
| **Circulatory disease** | **+1.6391** | 0.5088 | ±1.0177 | **+3.221** | **0.0013** | ** |
| HbA1c (%) | +0.1862 | 0.1536 | ±0.3071 | +1.213 | 0.2252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1358**, F-statistic = **12.32** (p = **1.31e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.3**, BIC = **4806.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9602** | 1.6263 | ±3.2526 | **+6.124** | **9.10e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0436** | 0.3576 | ±0.7153 | **-2.918** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4335** | 0.6109 | ±1.2218 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | -0.1854 | 0.4697 | ±0.9393 | -0.395 | 0.6930 |  |
| Site: UW (vs UAB) | -0.6853 | 0.4090 | ±0.8181 | -1.675 | 0.0939 | . |
| **Age (years)** | **-0.1130** | 0.0163 | ±0.0325 | **-6.948** | **3.70e-12** | *** |
| **BMI (kg/m2)** | **+0.0613** | 0.0277 | ±0.0553 | **+2.215** | **0.0267** | * |
| Hypertension | +0.3852 | 0.3734 | ±0.7468 | +1.032 | 0.3022 |  |
| High cholesterol | +0.4035 | 0.3617 | ±0.7235 | +1.115 | 0.2646 |  |
| Kidney disease | +0.9322 | 0.5252 | ±1.0504 | +1.775 | 0.0759 | . |
| **Circulatory disease** | **+1.6471** | 0.5094 | ±1.0189 | **+3.233** | **0.0012** | ** |
| Mean glucose (mg/dL) | +0.0040 | 0.0049 | ±0.0099 | +0.819 | 0.4125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1358**, F-statistic = **12.32** (p = **1.31e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.3**, BIC = **4806.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4010** | 2.0180 | ±4.0360 | **+4.659** | **3.18e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0436** | 0.3576 | ±0.7153 | **-2.918** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4335** | 0.6109 | ±1.2218 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | -0.1854 | 0.4697 | ±0.9393 | -0.395 | 0.6930 |  |
| Site: UW (vs UAB) | -0.6853 | 0.4090 | ±0.8181 | -1.675 | 0.0939 | . |
| **Age (years)** | **-0.1130** | 0.0163 | ±0.0325 | **-6.948** | **3.70e-12** | *** |
| **BMI (kg/m2)** | **+0.0613** | 0.0277 | ±0.0553 | **+2.215** | **0.0267** | * |
| Hypertension | +0.3852 | 0.3734 | ±0.7468 | +1.032 | 0.3022 |  |
| High cholesterol | +0.4035 | 0.3617 | ±0.7235 | +1.115 | 0.2646 |  |
| Kidney disease | +0.9322 | 0.5252 | ±1.0504 | +1.775 | 0.0759 | . |
| **Circulatory disease** | **+1.6471** | 0.5094 | ±1.0189 | **+3.233** | **0.0012** | ** |
| GMI (%) | +0.1690 | 0.2062 | ±0.4124 | +0.819 | 0.4125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **793**, R² = **0.1488**, Adj R² = **0.1368**, F-statistic = **12.41** (p = **8.74e-22**), Residual SE = **4.798** on **781** df, AIC = **4749.4**, BIC = **4805.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7817** | 1.6025 | ±3.2051 | **+6.104** | **1.04e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0300** | 0.3581 | ±0.7162 | **-2.876** | **0.0040** | ** |
| **Education: high school or below (vs college)** | **+1.4172** | 0.6083 | ±1.2166 | **+2.330** | **0.0198** | * |
| Site: UCSD (vs UAB) | -0.1749 | 0.4684 | ±0.9368 | -0.373 | 0.7088 |  |
| Site: UW (vs UAB) | -0.6869 | 0.4069 | ±0.8138 | -1.688 | 0.0914 | . |
| **Age (years)** | **-0.1120** | 0.0163 | ±0.0326 | **-6.875** | **6.21e-12** | *** |
| **BMI (kg/m2)** | **+0.0587** | 0.0277 | ±0.0555 | **+2.118** | **0.0342** | * |
| Hypertension | +0.3853 | 0.3732 | ±0.7464 | +1.033 | 0.3018 |  |
| High cholesterol | +0.4031 | 0.3614 | ±0.7227 | +1.116 | 0.2646 |  |
| Kidney disease | +0.9432 | 0.5239 | ±1.0477 | +1.800 | 0.0718 | . |
| **Circulatory disease** | **+1.6385** | 0.5092 | ±1.0183 | **+3.218** | **0.0013** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0054 | 0.0046 | ±0.0092 | +1.180 | 0.2382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **793**, R² = **0.1494**, Adj R² = **0.1374**, F-statistic = **12.47** (p = **6.82e-22**), Residual SE = **4.796** on **781** df, AIC = **4748.9**, BIC = **4805.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.8444** | 1.5486 | ±3.0972 | **+6.357** | **2.06e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0215** | 0.3571 | ±0.7141 | **-2.861** | **0.0042** | ** |
| **Education: high school or below (vs college)** | **+1.4176** | 0.6092 | ±1.2185 | **+2.327** | **0.0200** | * |
| Site: UCSD (vs UAB) | -0.1702 | 0.4687 | ±0.9373 | -0.363 | 0.7164 |  |
| Site: UW (vs UAB) | -0.6353 | 0.4116 | ±0.8231 | -1.544 | 0.1227 |  |
| **Age (years)** | **-0.1137** | 0.0163 | ±0.0325 | **-6.988** | **2.78e-12** | *** |
| **BMI (kg/m2)** | **+0.0599** | 0.0278 | ±0.0556 | **+2.153** | **0.0313** | * |
| Hypertension | +0.3653 | 0.3750 | ±0.7499 | +0.974 | 0.3299 |  |
| High cholesterol | +0.4189 | 0.3610 | ±0.7219 | +1.161 | 0.2458 |  |
| Kidney disease | +0.8209 | 0.5353 | ±1.0707 | +1.533 | 0.1252 |  |
| **Circulatory disease** | **+1.6389** | 0.5098 | ±1.0196 | **+3.215** | **0.0013** | ** |
| Glucose SD, pooled (mg/dL) | +0.0222 | 0.0158 | ±0.0315 | +1.408 | 0.1592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1357**, F-statistic = **12.31** (p = **1.37e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.4**, BIC = **4806.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.1214** | 1.5381 | ±3.0763 | **+6.580** | **4.70e-11** | *** |
| **Education: graduate level (vs college)** | **-1.0410** | 0.3569 | ±0.7137 | **-2.917** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4464** | 0.6123 | ±1.2246 | **+2.362** | **0.0182** | * |
| Site: UCSD (vs UAB) | -0.1885 | 0.4699 | ±0.9397 | -0.401 | 0.6882 |  |
| Site: UW (vs UAB) | -0.6719 | 0.4102 | ±0.8203 | -1.638 | 0.1014 |  |
| **Age (years)** | **-0.1138** | 0.0163 | ±0.0325 | **-6.993** | **2.69e-12** | *** |
| **BMI (kg/m2)** | **+0.0625** | 0.0277 | ±0.0553 | **+2.258** | **0.0239** | * |
| Hypertension | +0.3811 | 0.3754 | ±0.7507 | +1.015 | 0.3099 |  |
| High cholesterol | +0.4146 | 0.3620 | ±0.7241 | +1.145 | 0.2522 |  |
| Kidney disease | +0.8722 | 0.5364 | ±1.0728 | +1.626 | 0.1039 |  |
| **Circulatory disease** | **+1.6578** | 0.5097 | ±1.0194 | **+3.252** | **0.0011** | ** |
| Avg. daily SD (mg/dL) | +0.0146 | 0.0178 | ±0.0357 | +0.817 | 0.4137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.26** (p = **1.68e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4807.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.1464** | 1.6337 | ±3.2673 | **+6.211** | **5.27e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0461** | 0.3568 | ±0.7136 | **-2.932** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.4923** | 0.6085 | ±1.2171 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | -0.2048 | 0.4684 | ±0.9367 | -0.437 | 0.6620 |  |
| Site: UW (vs UAB) | -0.6892 | 0.4064 | ±0.8128 | -1.696 | 0.0899 | . |
| **Age (years)** | **-0.1139** | 0.0162 | ±0.0324 | **-7.022** | **2.19e-12** | *** |
| **BMI (kg/m2)** | **+0.0641** | 0.0275 | ±0.0551 | **+2.326** | **0.0200** | * |
| Hypertension | +0.3861 | 0.3748 | ±0.7495 | +1.030 | 0.3029 |  |
| High cholesterol | +0.4222 | 0.3637 | ±0.7274 | +1.161 | 0.2457 |  |
| Kidney disease | +0.9036 | 0.5252 | ±1.0505 | +1.720 | 0.0854 | . |
| **Circulatory disease** | **+1.6753** | 0.5092 | ±1.0184 | **+3.290** | **0.0010** | ** |
| CV (%) | +0.0179 | 0.0326 | ±0.0652 | +0.549 | 0.5831 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **793**, R² = **0.1476**, Adj R² = **0.1356**, F-statistic = **12.29** (p = **1.47e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1791** | 1.6856 | ±3.3713 | **+6.632** | **3.31e-11** | *** |
| **Education: graduate level (vs college)** | **-1.0442** | 0.3570 | ±0.7140 | **-2.925** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.4927** | 0.6083 | ±1.2166 | **+2.454** | **0.0141** | * |
| Site: UCSD (vs UAB) | -0.2091 | 0.4678 | ±0.9355 | -0.447 | 0.6549 |  |
| Site: UW (vs UAB) | -0.6850 | 0.4052 | ±0.8105 | -1.690 | 0.0910 | . |
| **Age (years)** | **-0.1140** | 0.0162 | ±0.0324 | **-7.027** | **2.11e-12** | *** |
| **BMI (kg/m2)** | **+0.0643** | 0.0275 | ±0.0551 | **+2.334** | **0.0196** | * |
| Hypertension | +0.3828 | 0.3750 | ±0.7499 | +1.021 | 0.3073 |  |
| High cholesterol | +0.4187 | 0.3626 | ±0.7253 | +1.155 | 0.2482 |  |
| Kidney disease | +0.8944 | 0.5224 | ±1.0449 | +1.712 | 0.0869 | . |
| **Circulatory disease** | **+1.6691** | 0.5090 | ±1.0179 | **+3.280** | **0.0010** | ** |
| Mean / SD ratio | -0.1367 | 0.1799 | ±0.3597 | -0.760 | 0.4471 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **793**, R² = **0.1469**, Adj R² = **0.1349**, F-statistic = **12.23** (p = **1.94e-21**), Residual SE = **4.803** on **781** df, AIC = **4751.2**, BIC = **4807.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5731** | 1.6885 | ±3.3769 | **+6.262** | **3.80e-10** | *** |
| **Education: graduate level (vs college)** | **-1.0561** | 0.3570 | ±0.7141 | **-2.958** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+1.4948** | 0.6086 | ±1.2172 | **+2.456** | **0.0140** | * |
| Site: UCSD (vs UAB) | -0.2140 | 0.4680 | ±0.9361 | -0.457 | 0.6475 |  |
| Site: UW (vs UAB) | -0.7120 | 0.4037 | ±0.8075 | -1.764 | 0.0778 | . |
| **Age (years)** | **-0.1135** | 0.0163 | ±0.0325 | **-6.977** | **3.01e-12** | *** |
| **BMI (kg/m2)** | **+0.0645** | 0.0274 | ±0.0549 | **+2.350** | **0.0188** | * |
| Hypertension | +0.3957 | 0.3751 | ±0.7501 | +1.055 | 0.2915 |  |
| High cholesterol | +0.4114 | 0.3633 | ±0.7265 | +1.133 | 0.2574 |  |
| Kidney disease | +0.9524 | 0.5218 | ±1.0436 | +1.825 | 0.0680 | . |
| **Circulatory disease** | **+1.6761** | 0.5088 | ±1.0176 | **+3.294** | **9.86e-04** | *** |
| Avg. daily mean/SD | -0.0061 | 0.1446 | ±0.2893 | -0.042 | 0.9663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **793**, R² = **0.1513**, Adj R² = **0.1394**, F-statistic = **12.66** (p = **2.91e-22**), Residual SE = **4.791** on **781** df, AIC = **4747.0**, BIC = **4803.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6502** | 1.7843 | ±3.5686 | **+4.848** | **1.25e-06** | *** |
| **Education: graduate level (vs college)** | **-0.9941** | 0.3573 | ±0.7146 | **-2.782** | **0.0054** | ** |
| **Education: high school or below (vs college)** | **+1.4580** | 0.6028 | ±1.2057 | **+2.418** | **0.0156** | * |
| Site: UCSD (vs UAB) | -0.1416 | 0.4681 | ±0.9361 | -0.302 | 0.7623 |  |
| Site: UW (vs UAB) | -0.5694 | 0.4140 | ±0.8279 | -1.376 | 0.1690 |  |
| **Age (years)** | **-0.1107** | 0.0162 | ±0.0324 | **-6.825** | **8.77e-12** | *** |
| **BMI (kg/m2)** | **+0.0619** | 0.0274 | ±0.0548 | **+2.260** | **0.0238** | * |
| Hypertension | +0.4172 | 0.3726 | ±0.7452 | +1.120 | 0.2629 |  |
| High cholesterol | +0.4651 | 0.3617 | ±0.7234 | +1.286 | 0.1985 |  |
| Kidney disease | +0.8785 | 0.5254 | ±1.0509 | +1.672 | 0.0945 | . |
| **Circulatory disease** | **+1.6558** | 0.5121 | ±1.0242 | **+3.233** | **0.0012** | ** |
| MAG (mg/dL/h) | +0.0369 | 0.0198 | ±0.0397 | +1.859 | 0.0631 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **793**, R² = **0.1474**, Adj R² = **0.1354**, F-statistic = **12.28** (p = **1.56e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.7**, BIC = **4806.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0293** | 1.6536 | ±3.3073 | **+6.065** | **1.32e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0442** | 0.3567 | ±0.7135 | **-2.927** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.4574** | 0.6130 | ±1.2260 | **+2.378** | **0.0174** | * |
| Site: UCSD (vs UAB) | -0.1890 | 0.4709 | ±0.9418 | -0.401 | 0.6881 |  |
| Site: UW (vs UAB) | -0.6775 | 0.4107 | ±0.8214 | -1.650 | 0.0990 | . |
| **Age (years)** | **-0.1133** | 0.0163 | ±0.0325 | **-6.966** | **3.25e-12** | *** |
| **BMI (kg/m2)** | **+0.0634** | 0.0275 | ±0.0551 | **+2.302** | **0.0213** | * |
| Hypertension | +0.3925 | 0.3739 | ±0.7477 | +1.050 | 0.2938 |  |
| High cholesterol | +0.4163 | 0.3626 | ±0.7252 | +1.148 | 0.2509 |  |
| Kidney disease | +0.8905 | 0.5357 | ±1.0714 | +1.662 | 0.0964 | . |
| **Circulatory disease** | **+1.6601** | 0.5100 | ±1.0199 | **+3.255** | **0.0011** | ** |
| Avg. daily range (mg/dL) | +0.0034 | 0.0052 | ±0.0105 | +0.656 | 0.5120 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **793**, R² = **0.1572**, Adj R² = **0.1453**, F-statistic = **13.24** (p = **2.34e-23**), Residual SE = **4.774** on **781** df, AIC = **4741.6**, BIC = **4797.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.8582** | 1.4738 | ±2.9476 | **+6.689** | **2.25e-11** | *** |
| **Education: graduate level (vs college)** | **-0.9410** | 0.3577 | ±0.7154 | **-2.631** | **0.0085** | ** |
| **Education: high school or below (vs college)** | **+1.4228** | 0.6000 | ±1.2000 | **+2.371** | **0.0177** | * |
| Site: UCSD (vs UAB) | -0.1586 | 0.4645 | ±0.9290 | -0.342 | 0.7327 |  |
| Site: UW (vs UAB) | -0.5919 | 0.4059 | ±0.8118 | -1.458 | 0.1448 |  |
| **Age (years)** | **-0.1110** | 0.0164 | ±0.0328 | **-6.768** | **1.31e-11** | *** |
| BMI (kg/m2) | +0.0531 | 0.0277 | ±0.0555 | +1.915 | 0.0555 | . |
| Hypertension | +0.3172 | 0.3735 | ±0.7470 | +0.849 | 0.3957 |  |
| High cholesterol | +0.4164 | 0.3578 | ±0.7156 | +1.164 | 0.2445 |  |
| Kidney disease | +0.8397 | 0.5256 | ±1.0512 | +1.598 | 0.1102 |  |
| **Circulatory disease** | **+1.5678** | 0.5051 | ±1.0103 | **+3.104** | **0.0019** | ** |
| **SD of daily means (mg/dL)** | **+0.0664** | 0.0226 | ±0.0451 | **+2.943** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **793**, R² = **0.1483**, Adj R² = **0.1363**, F-statistic = **12.37** (p = **1.06e-21**), Residual SE = **4.799** on **781** df, AIC = **4749.9**, BIC = **4806.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.2404** | 1.6145 | ±3.2291 | **+6.962** | **3.36e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0387** | 0.3575 | ±0.7150 | **-2.906** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+1.4219** | 0.6124 | ±1.2248 | **+2.322** | **0.0202** | * |
| Site: UCSD (vs UAB) | -0.1717 | 0.4707 | ±0.9413 | -0.365 | 0.7153 |  |
| Site: UW (vs UAB) | -0.6712 | 0.4108 | ±0.8215 | -1.634 | 0.1022 |  |
| **Age (years)** | **-0.1133** | 0.0163 | ±0.0326 | **-6.953** | **3.59e-12** | *** |
| **BMI (kg/m2)** | **+0.0597** | 0.0278 | ±0.0556 | **+2.148** | **0.0317** | * |
| Hypertension | +0.3874 | 0.3730 | ±0.7459 | +1.039 | 0.2990 |  |
| High cholesterol | +0.4108 | 0.3614 | ±0.7229 | +1.137 | 0.2557 |  |
| Kidney disease | +0.9109 | 0.5288 | ±1.0576 | +1.722 | 0.0850 | . |
| **Circulatory disease** | **+1.6460** | 0.5083 | ±1.0167 | **+3.238** | **0.0012** | ** |
| Time in range 70-180, pooled (%) | -0.0080 | 0.0078 | ±0.0156 | -1.025 | 0.3056 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **793**, R² = **0.1482**, Adj R² = **0.1362**, F-statistic = **12.35** (p = **1.15e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.0**, BIC = **4806.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1996** | 1.6208 | ±3.2416 | **+6.910** | **4.85e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0416** | 0.3575 | ±0.7149 | **-2.914** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.4251** | 0.6130 | ±1.2259 | **+2.325** | **0.0201** | * |
| Site: UCSD (vs UAB) | -0.1722 | 0.4708 | ±0.9416 | -0.366 | 0.7146 |  |
| Site: UW (vs UAB) | -0.6733 | 0.4106 | ±0.8212 | -1.640 | 0.1010 |  |
| **Age (years)** | **-0.1134** | 0.0163 | ±0.0326 | **-6.957** | **3.47e-12** | *** |
| **BMI (kg/m2)** | **+0.0599** | 0.0278 | ±0.0557 | **+2.154** | **0.0313** | * |
| Hypertension | +0.3886 | 0.3730 | ±0.7459 | +1.042 | 0.2975 |  |
| High cholesterol | +0.4105 | 0.3615 | ±0.7231 | +1.135 | 0.2562 |  |
| Kidney disease | +0.9112 | 0.5289 | ±1.0577 | +1.723 | 0.0849 | . |
| **Circulatory disease** | **+1.6482** | 0.5086 | ±1.0172 | **+3.241** | **0.0012** | ** |
| Avg. daily time in range 70-180 (%) | -0.0075 | 0.0078 | ±0.0156 | -0.957 | 0.3388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **793**, R² = **0.1498**, Adj R² = **0.1378**, F-statistic = **12.51** (p = **5.65e-22**), Residual SE = **4.795** on **781** df, AIC = **4748.5**, BIC = **4804.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.2916** | 1.4637 | ±2.9274 | **+7.031** | **2.05e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0394** | 0.3569 | ±0.7138 | **-2.912** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.5321** | 0.6061 | ±1.2121 | **+2.528** | **0.0115** | * |
| Site: UCSD (vs UAB) | -0.1791 | 0.4657 | ±0.9315 | -0.385 | 0.7006 |  |
| Site: UW (vs UAB) | -0.6744 | 0.4028 | ±0.8055 | -1.675 | 0.0940 | . |
| **Age (years)** | **-0.1123** | 0.0163 | ±0.0327 | **-6.875** | **6.20e-12** | *** |
| **BMI (kg/m2)** | **+0.0640** | 0.0272 | ±0.0545 | **+2.350** | **0.0188** | * |
| Hypertension | +0.3602 | 0.3740 | ±0.7480 | +0.963 | 0.3355 |  |
| High cholesterol | +0.4604 | 0.3607 | ±0.7213 | +1.276 | 0.2018 |  |
| Kidney disease | +0.9446 | 0.5182 | ±1.0365 | +1.823 | 0.0684 | . |
| **Circulatory disease** | **+1.6441** | 0.5125 | ±1.0251 | **+3.208** | **0.0013** | ** |
| Any reading < 54 during wear (0/1) | +0.6632 | 0.4129 | ±0.8258 | +1.606 | 0.1082 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **793**, R² = **0.1469**, Adj R² = **0.1349**, F-statistic = **12.23** (p = **1.94e-21**), Residual SE = **4.803** on **781** df, AIC = **4751.2**, BIC = **4807.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5440** | 1.4660 | ±2.9320 | **+7.192** | **6.37e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0577** | 0.3576 | ±0.7152 | **-2.958** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+1.4937** | 0.6079 | ±1.2158 | **+2.457** | **0.0140** | * |
| Site: UCSD (vs UAB) | -0.2158 | 0.4685 | ±0.9369 | -0.461 | 0.6451 |  |
| Site: UW (vs UAB) | -0.7153 | 0.4056 | ±0.8113 | -1.764 | 0.0778 | . |
| **Age (years)** | **-0.1135** | 0.0162 | ±0.0325 | **-6.988** | **2.78e-12** | *** |
| **BMI (kg/m2)** | **+0.0644** | 0.0275 | ±0.0550 | **+2.342** | **0.0192** | * |
| Hypertension | +0.3964 | 0.3728 | ±0.7457 | +1.063 | 0.2877 |  |
| High cholesterol | +0.4094 | 0.3627 | ±0.7254 | +1.129 | 0.2590 |  |
| Kidney disease | +0.9554 | 0.5192 | ±1.0385 | +1.840 | 0.0658 | . |
| **Circulatory disease** | **+1.6754** | 0.5083 | ±1.0166 | **+3.296** | **9.81e-04** | *** |
| Time < 54 (%) | -0.0151 | 0.1685 | ±0.3371 | -0.090 | 0.9285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **793**, R² = **0.1470**, Adj R² = **0.1350**, F-statistic = **12.24** (p = **1.87e-21**), Residual SE = **4.803** on **781** df, AIC = **4751.1**, BIC = **4807.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5198** | 1.4658 | ±2.9315 | **+7.177** | **7.13e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0514** | 0.3577 | ±0.7154 | **-2.940** | **0.0033** | ** |
| **Education: high school or below (vs college)** | **+1.5027** | 0.6080 | ±1.2161 | **+2.471** | **0.0135** | * |
| Site: UCSD (vs UAB) | -0.2051 | 0.4686 | ±0.9372 | -0.438 | 0.6616 |  |
| Site: UW (vs UAB) | -0.7011 | 0.4062 | ±0.8123 | -1.726 | 0.0843 | . |
| **Age (years)** | **-0.1136** | 0.0163 | ±0.0325 | **-6.987** | **2.80e-12** | *** |
| **BMI (kg/m2)** | **+0.0646** | 0.0275 | ±0.0551 | **+2.349** | **0.0188** | * |
| Hypertension | +0.3956 | 0.3729 | ±0.7459 | +1.061 | 0.2888 |  |
| High cholesterol | +0.4203 | 0.3630 | ±0.7260 | +1.158 | 0.2470 |  |
| Kidney disease | +0.9549 | 0.5195 | ±1.0390 | +1.838 | 0.0661 | . |
| **Circulatory disease** | **+1.6801** | 0.5084 | ±1.0169 | **+3.304** | **9.52e-04** | *** |
| Avg. daily time < 54 (%) | +0.0988 | 0.3648 | ±0.7296 | +0.271 | 0.7866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.27** (p = **1.62e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4806.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4930** | 1.4621 | ±2.9243 | **+7.176** | **7.15e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0430** | 0.3574 | ±0.7147 | **-2.919** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.5085** | 0.6075 | ±1.2149 | **+2.483** | **0.0130** | * |
| Site: UCSD (vs UAB) | -0.1900 | 0.4675 | ±0.9350 | -0.406 | 0.6845 |  |
| Site: UW (vs UAB) | -0.6857 | 0.4047 | ±0.8094 | -1.694 | 0.0902 | . |
| **Age (years)** | **-0.1138** | 0.0162 | ±0.0325 | **-7.014** | **2.31e-12** | *** |
| **BMI (kg/m2)** | **+0.0644** | 0.0275 | ±0.0549 | **+2.345** | **0.0190** | * |
| Hypertension | +0.3883 | 0.3728 | ±0.7457 | +1.041 | 0.2977 |  |
| High cholesterol | +0.4368 | 0.3653 | ±0.7306 | +1.196 | 0.2318 |  |
| Kidney disease | +0.9459 | 0.5207 | ±1.0415 | +1.816 | 0.0693 | . |
| **Circulatory disease** | **+1.6904** | 0.5092 | ±1.0185 | **+3.320** | **9.02e-04** | *** |
| Time 54-69, pooled (%) | +0.1041 | 0.1688 | ±0.3377 | +0.616 | 0.5376 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **793**, R² = **0.1478**, Adj R² = **0.1358**, F-statistic = **12.31** (p = **1.35e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.4**, BIC = **4806.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4876** | 1.4617 | ±2.9233 | **+7.175** | **7.23e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0353** | 0.3574 | ±0.7148 | **-2.897** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+1.5168** | 0.6077 | ±1.2154 | **+2.496** | **0.0126** | * |
| Site: UCSD (vs UAB) | -0.1794 | 0.4679 | ±0.9357 | -0.383 | 0.7014 |  |
| Site: UW (vs UAB) | -0.6695 | 0.4055 | ±0.8111 | -1.651 | 0.0987 | . |
| **Age (years)** | **-0.1141** | 0.0162 | ±0.0325 | **-7.025** | **2.14e-12** | *** |
| **BMI (kg/m2)** | **+0.0642** | 0.0275 | ±0.0550 | **+2.336** | **0.0195** | * |
| Hypertension | +0.3848 | 0.3728 | ±0.7456 | +1.032 | 0.3020 |  |
| High cholesterol | +0.4494 | 0.3648 | ±0.7296 | +1.232 | 0.2180 |  |
| Kidney disease | +0.9431 | 0.5202 | ±1.0404 | +1.813 | 0.0698 | . |
| **Circulatory disease** | **+1.6992** | 0.5096 | ±1.0193 | **+3.334** | **8.56e-04** | *** |
| Avg. daily time 54-69 (%) | +0.1411 | 0.1722 | ±0.3443 | +0.820 | 0.4123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **793**, R² = **0.1471**, Adj R² = **0.1351**, F-statistic = **12.25** (p = **1.77e-21**), Residual SE = **4.802** on **781** df, AIC = **4751.0**, BIC = **4807.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4995** | 1.4646 | ±2.9293 | **+7.169** | **7.57e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0455** | 0.3574 | ±0.7148 | **-2.925** | **0.0034** | ** |
| **Education: high school or below (vs college)** | **+1.5069** | 0.6076 | ±1.2151 | **+2.480** | **0.0131** | * |
| Site: UCSD (vs UAB) | -0.1955 | 0.4680 | ±0.9360 | -0.418 | 0.6762 |  |
| Site: UW (vs UAB) | -0.6916 | 0.4053 | ±0.8107 | -1.706 | 0.0880 | . |
| **Age (years)** | **-0.1138** | 0.0162 | ±0.0325 | **-7.012** | **2.35e-12** | *** |
| **BMI (kg/m2)** | **+0.0646** | 0.0274 | ±0.0549 | **+2.355** | **0.0185** | * |
| Hypertension | +0.3920 | 0.3727 | ±0.7454 | +1.052 | 0.2929 |  |
| High cholesterol | +0.4300 | 0.3648 | ±0.7296 | +1.179 | 0.2385 |  |
| Kidney disease | +0.9512 | 0.5201 | ±1.0402 | +1.829 | 0.0674 | . |
| **Circulatory disease** | **+1.6865** | 0.5088 | ±1.0175 | **+3.315** | **9.17e-04** | *** |
| Time < 70 (%) | +0.0555 | 0.1075 | ±0.2149 | +0.516 | 0.6057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **793**, R² = **0.1476**, Adj R² = **0.1356**, F-statistic = **12.29** (p = **1.48e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4868** | 1.4636 | ±2.9272 | **+7.165** | **7.77e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0377** | 0.3575 | ±0.7150 | **-2.903** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+1.5165** | 0.6078 | ±1.2156 | **+2.495** | **0.0126** | * |
| Site: UCSD (vs UAB) | -0.1828 | 0.4683 | ±0.9365 | -0.390 | 0.6962 |  |
| Site: UW (vs UAB) | -0.6731 | 0.4060 | ±0.8121 | -1.658 | 0.0974 | . |
| **Age (years)** | **-0.1140** | 0.0162 | ±0.0325 | **-7.018** | **2.25e-12** | *** |
| **BMI (kg/m2)** | **+0.0645** | 0.0275 | ±0.0550 | **+2.346** | **0.0190** | * |
| Hypertension | +0.3880 | 0.3726 | ±0.7451 | +1.042 | 0.2976 |  |
| High cholesterol | +0.4450 | 0.3646 | ±0.7292 | +1.220 | 0.2223 |  |
| Kidney disease | +0.9467 | 0.5200 | ±1.0400 | +1.821 | 0.0687 | . |
| **Circulatory disease** | **+1.6950** | 0.5093 | ±1.0185 | **+3.328** | **8.74e-04** | *** |
| Avg. daily time < 70 (%) | +0.0926 | 0.1205 | ±0.2411 | +0.768 | 0.4422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **793**, R² = **0.1475**, Adj R² = **0.1355**, F-statistic = **12.29** (p = **1.50e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.2393** | 1.8438 | ±3.6876 | **+6.096** | **1.09e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0369** | 0.3582 | ±0.7163 | **-2.895** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+1.4508** | 0.6096 | ±1.2191 | **+2.380** | **0.0173** | * |
| Site: UCSD (vs UAB) | -0.1895 | 0.4697 | ±0.9395 | -0.403 | 0.6866 |  |
| Site: UW (vs UAB) | -0.6815 | 0.4113 | ±0.8226 | -1.657 | 0.0975 | . |
| **Age (years)** | **-0.1125** | 0.0163 | ±0.0326 | **-6.901** | **5.16e-12** | *** |
| **BMI (kg/m2)** | **+0.0630** | 0.0276 | ±0.0552 | **+2.281** | **0.0225** | * |
| Hypertension | +0.3856 | 0.3731 | ±0.7462 | +1.034 | 0.3013 |  |
| High cholesterol | +0.4150 | 0.3623 | ±0.7246 | +1.146 | 0.2520 |  |
| Kidney disease | +0.9375 | 0.5232 | ±1.0464 | +1.792 | 0.0731 | . |
| **Circulatory disease** | **+1.6565** | 0.5107 | ±1.0214 | **+3.244** | **0.0012** | ** |
| Time 54-250, pooled (%) | -0.0079 | 0.0127 | ±0.0255 | -0.619 | 0.5358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.27** (p = **1.63e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4806.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1302** | 1.8717 | ±3.7433 | **+5.947** | **2.74e-09** | *** |
| **Education: graduate level (vs college)** | **-1.0407** | 0.3580 | ±0.7160 | **-2.907** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+1.4587** | 0.6098 | ±1.2196 | **+2.392** | **0.0168** | * |
| Site: UCSD (vs UAB) | -0.1936 | 0.4700 | ±0.9400 | -0.412 | 0.6804 |  |
| Site: UW (vs UAB) | -0.6880 | 0.4108 | ±0.8215 | -1.675 | 0.0940 | . |
| **Age (years)** | **-0.1128** | 0.0163 | ±0.0326 | **-6.924** | **4.40e-12** | *** |
| **BMI (kg/m2)** | **+0.0632** | 0.0276 | ±0.0552 | **+2.288** | **0.0221** | * |
| Hypertension | +0.3881 | 0.3731 | ±0.7462 | +1.040 | 0.2982 |  |
| High cholesterol | +0.4143 | 0.3625 | ±0.7249 | +1.143 | 0.2530 |  |
| Kidney disease | +0.9391 | 0.5232 | ±1.0464 | +1.795 | 0.0727 | . |
| **Circulatory disease** | **+1.6590** | 0.5108 | ±1.0216 | **+3.248** | **0.0012** | ** |
| Avg. daily time 54-250 (%) | -0.0066 | 0.0130 | ±0.0259 | -0.507 | 0.6124 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **793**, R² = **0.1481**, Adj R² = **0.1361**, F-statistic = **12.34** (p = **1.19e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.1**, BIC = **4806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5297** | 1.4658 | ±2.9315 | **+7.184** | **6.78e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0616** | 0.3578 | ±0.7156 | **-2.967** | **0.0030** | ** |
| **Education: high school or below (vs college)** | **+1.4504** | 0.6133 | ±1.2266 | **+2.365** | **0.0180** | * |
| Site: UCSD (vs UAB) | -0.1905 | 0.4697 | ±0.9395 | -0.405 | 0.6852 |  |
| Site: UW (vs UAB) | -0.7018 | 0.4054 | ±0.8109 | -1.731 | 0.0835 | . |
| **Age (years)** | **-0.1147** | 0.0163 | ±0.0327 | **-7.018** | **2.26e-12** | *** |
| **BMI (kg/m2)** | **+0.0595** | 0.0278 | ±0.0556 | **+2.139** | **0.0324** | * |
| Hypertension | +0.4002 | 0.3729 | ±0.7458 | +1.073 | 0.2831 |  |
| High cholesterol | +0.4013 | 0.3620 | ±0.7239 | +1.109 | 0.2676 |  |
| Kidney disease | +0.9165 | 0.5286 | ±1.0572 | +1.734 | 0.0829 | . |
| **Circulatory disease** | **+1.6589** | 0.5065 | ±1.0131 | **+3.275** | **0.0011** | ** |
| Time 181-250, pooled (%) | +0.0122 | 0.0126 | ±0.0252 | +0.969 | 0.3327 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **793**, R² = **0.1481**, Adj R² = **0.1361**, F-statistic = **12.34** (p = **1.18e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.1**, BIC = **4806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5270** | 1.4664 | ±2.9328 | **+7.179** | **7.04e-13** | *** |
| **Education: graduate level (vs college)** | **-1.0635** | 0.3579 | ±0.7159 | **-2.971** | **0.0030** | ** |
| **Education: high school or below (vs college)** | **+1.4467** | 0.6140 | ±1.2280 | **+2.356** | **0.0185** | * |
| Site: UCSD (vs UAB) | -0.1869 | 0.4698 | ±0.9395 | -0.398 | 0.6907 |  |
| Site: UW (vs UAB) | -0.6990 | 0.4057 | ±0.8114 | -1.723 | 0.0849 | . |
| **Age (years)** | **-0.1146** | 0.0163 | ±0.0327 | **-7.016** | **2.29e-12** | *** |
| **BMI (kg/m2)** | **+0.0595** | 0.0278 | ±0.0557 | **+2.136** | **0.0327** | * |
| Hypertension | +0.3998 | 0.3728 | ±0.7455 | +1.073 | 0.2835 |  |
| High cholesterol | +0.4006 | 0.3620 | ±0.7239 | +1.107 | 0.2684 |  |
| Kidney disease | +0.9150 | 0.5287 | ±1.0574 | +1.731 | 0.0835 | . |
| **Circulatory disease** | **+1.6604** | 0.5069 | ±1.0137 | **+3.276** | **0.0011** | ** |
| Avg. daily time 181-250 (%) | +0.0121 | 0.0124 | ±0.0248 | +0.972 | 0.3309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **793**, R² = **0.1483**, Adj R² = **0.1363**, F-statistic = **12.36** (p = **1.10e-21**), Residual SE = **4.799** on **781** df, AIC = **4749.9**, BIC = **4806.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4483** | 1.4695 | ±2.9390 | **+7.110** | **1.16e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0409** | 0.3575 | ±0.7150 | **-2.912** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.4230** | 0.6125 | ±1.2249 | **+2.323** | **0.0202** | * |
| Site: UCSD (vs UAB) | -0.1759 | 0.4704 | ±0.9408 | -0.374 | 0.7084 |  |
| Site: UW (vs UAB) | -0.6758 | 0.4100 | ±0.8201 | -1.648 | 0.0993 | . |
| **Age (years)** | **-0.1133** | 0.0163 | ±0.0326 | **-6.952** | **3.61e-12** | *** |
| **BMI (kg/m2)** | **+0.0599** | 0.0278 | ±0.0556 | **+2.155** | **0.0312** | * |
| Hypertension | +0.3883 | 0.3730 | ±0.7460 | +1.041 | 0.2978 |  |
| High cholesterol | +0.4082 | 0.3615 | ±0.7229 | +1.129 | 0.2588 |  |
| Kidney disease | +0.9132 | 0.5284 | ±1.0568 | +1.728 | 0.0840 | . |
| **Circulatory disease** | **+1.6457** | 0.5083 | ±1.0166 | **+3.238** | **0.0012** | ** |
| Time > 180 (%) | +0.0077 | 0.0077 | ±0.0155 | +0.997 | 0.3186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **793**, R² = **0.1480**, Adj R² = **0.1360**, F-statistic = **12.34** (p = **1.20e-21**), Residual SE = **4.800** on **781** df, AIC = **4750.1**, BIC = **4806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4631** | 1.4690 | ±2.9379 | **+7.123** | **1.06e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0438** | 0.3575 | ±0.7150 | **-2.920** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+1.4273** | 0.6130 | ±1.2261 | **+2.328** | **0.0199** | * |
| Site: UCSD (vs UAB) | -0.1768 | 0.4705 | ±0.9411 | -0.376 | 0.7070 |  |
| Site: UW (vs UAB) | -0.6786 | 0.4099 | ±0.8197 | -1.656 | 0.0978 | . |
| **Age (years)** | **-0.1134** | 0.0163 | ±0.0326 | **-6.957** | **3.49e-12** | *** |
| **BMI (kg/m2)** | **+0.0602** | 0.0278 | ±0.0556 | **+2.164** | **0.0305** | * |
| Hypertension | +0.3896 | 0.3730 | ±0.7460 | +1.045 | 0.2962 |  |
| High cholesterol | +0.4079 | 0.3616 | ±0.7232 | +1.128 | 0.2592 |  |
| Kidney disease | +0.9143 | 0.5284 | ±1.0568 | +1.730 | 0.0836 | . |
| **Circulatory disease** | **+1.6483** | 0.5086 | ±1.0171 | **+3.241** | **0.0012** | ** |
| Avg. daily time > 180 (%) | +0.0070 | 0.0077 | ±0.0154 | +0.914 | 0.3609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **793**, R² = **0.1495**, Adj R² = **0.1376**, F-statistic = **12.48** (p = **6.36e-22**), Residual SE = **4.796** on **781** df, AIC = **4748.7**, BIC = **4804.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4629** | 1.4688 | ±2.9376 | **+7.123** | **1.05e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0152** | 0.3582 | ±0.7165 | **-2.834** | **0.0046** | ** |
| **Education: high school or below (vs college)** | **+1.4102** | 0.6094 | ±1.2187 | **+2.314** | **0.0207** | * |
| Site: UCSD (vs UAB) | -0.1560 | 0.4688 | ±0.9376 | -0.333 | 0.7393 |  |
| Site: UW (vs UAB) | -0.6754 | 0.4076 | ±0.8151 | -1.657 | 0.0975 | . |
| **Age (years)** | **-0.1123** | 0.0163 | ±0.0327 | **-6.867** | **6.55e-12** | *** |
| **BMI (kg/m2)** | **+0.0567** | 0.0280 | ±0.0560 | **+2.025** | **0.0429** | * |
| Hypertension | +0.3910 | 0.3726 | ±0.7451 | +1.049 | 0.2940 |  |
| High cholesterol | +0.4156 | 0.3611 | ±0.7222 | +1.151 | 0.2498 |  |
| Kidney disease | +0.9155 | 0.5274 | ±1.0547 | +1.736 | 0.0826 | . |
| **Circulatory disease** | **+1.6384** | 0.5086 | ±1.0172 | **+3.222** | **0.0013** | ** |
| Nocturnal time > 180 (%) | +0.0098 | 0.0070 | ±0.0140 | +1.400 | 0.1615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **793**, R² = **0.1475**, Adj R² = **0.1355**, F-statistic = **12.29** (p = **1.49e-21**), Residual SE = **4.801** on **781** df, AIC = **4750.6**, BIC = **4806.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4526** | 1.4734 | ±2.9468 | **+7.094** | **1.30e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0374** | 0.3581 | ±0.7162 | **-2.897** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+1.4501** | 0.6097 | ±1.2193 | **+2.379** | **0.0174** | * |
| Site: UCSD (vs UAB) | -0.1903 | 0.4696 | ±0.9391 | -0.405 | 0.6853 |  |
| Site: UW (vs UAB) | -0.6824 | 0.4109 | ±0.8218 | -1.661 | 0.0968 | . |
| **Age (years)** | **-0.1125** | 0.0163 | ±0.0326 | **-6.900** | **5.21e-12** | *** |
| **BMI (kg/m2)** | **+0.0630** | 0.0276 | ±0.0552 | **+2.280** | **0.0226** | * |
| Hypertension | +0.3856 | 0.3731 | ±0.7462 | +1.034 | 0.3013 |  |
| High cholesterol | +0.4143 | 0.3622 | ±0.7245 | +1.144 | 0.2528 |  |
| Kidney disease | +0.9374 | 0.5232 | ±1.0464 | +1.792 | 0.0732 | . |
| **Circulatory disease** | **+1.6560** | 0.5107 | ±1.0214 | **+3.243** | **0.0012** | ** |
| Time > 250 (%) | +0.0079 | 0.0127 | ±0.0255 | +0.621 | 0.5347 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **793**, R² = **0.1473**, Adj R² = **0.1353**, F-statistic = **12.27** (p = **1.64e-21**), Residual SE = **4.802** on **781** df, AIC = **4750.8**, BIC = **4806.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4763** | 1.4714 | ±2.9429 | **+7.120** | **1.08e-12** | *** |
| **Education: graduate level (vs college)** | **-1.0412** | 0.3580 | ±0.7160 | **-2.909** | **0.0036** | ** |
| **Education: high school or below (vs college)** | **+1.4587** | 0.6099 | ±1.2198 | **+2.392** | **0.0168** | * |
| Site: UCSD (vs UAB) | -0.1945 | 0.4699 | ±0.9398 | -0.414 | 0.6790 |  |
| Site: UW (vs UAB) | -0.6891 | 0.4104 | ±0.8209 | -1.679 | 0.0931 | . |
| **Age (years)** | **-0.1128** | 0.0163 | ±0.0326 | **-6.923** | **4.41e-12** | *** |
| **BMI (kg/m2)** | **+0.0632** | 0.0276 | ±0.0553 | **+2.288** | **0.0221** | * |
| Hypertension | +0.3883 | 0.3731 | ±0.7462 | +1.041 | 0.2980 |  |
| High cholesterol | +0.4136 | 0.3624 | ±0.7249 | +1.141 | 0.2537 |  |
| Kidney disease | +0.9394 | 0.5231 | ±1.0463 | +1.796 | 0.0725 | . |
| **Circulatory disease** | **+1.6590** | 0.5108 | ±1.0217 | **+3.248** | **0.0012** | ** |
| Avg. daily time > 250 (%) | +0.0065 | 0.0129 | ±0.0259 | +0.500 | 0.6172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 793; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0914**, LLR χ² = **74.14** (p = **7.00e-12**), AUC = **0.7072**, AIC = **758.9**, BIC = **810.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1259 | 0.7675 | ±1.5350 | -0.164 | 0.8697 | 0.8817 |  |
| Education: graduate level (vs college) | -0.3009 | 0.2195 | ±0.4390 | -1.371 | 0.1705 | 0.7402 |  |
| Education: high school or below (vs college) | +0.1936 | 0.2529 | ±0.5057 | +0.766 | 0.4439 | 1.2136 |  |
| Site: UCSD (vs UAB) | -0.2245 | 0.2356 | ±0.4712 | -0.953 | 0.3407 | 0.7989 |  |
| Site: UW (vs UAB) | -0.3745 | 0.2252 | ±0.4503 | -1.663 | 0.0963 | 0.6876 | . |
| **Age (years)** | **-0.0424** | 0.0097 | ±0.0194 | **-4.380** | **1.18e-05** | 0.9585 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.842** | **0.0045** | 1.0359 | ** |
| Hypertension | +0.2749 | 0.2185 | ±0.4369 | +1.258 | 0.2083 | 1.3164 |  |
| High cholesterol | +0.2062 | 0.2029 | ±0.4058 | +1.016 | 0.3094 | 1.2290 |  |
| Kidney disease | +0.3617 | 0.2411 | ±0.4823 | +1.500 | 0.1336 | 1.4358 |  |
| **Circulatory disease** | **+0.7652** | 0.2246 | ±0.4492 | **+3.407** | **6.56e-04** | 2.1495 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0949**, LLR χ² = **76.97** (p = **5.67e-12**), AUC = **0.7110**, AIC = **758.1**, BIC = **814.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8192 | 0.8730 | ±1.7459 | -0.938 | 0.3481 | 0.4408 |  |
| Education: graduate level (vs college) | -0.2688 | 0.2205 | ±0.4410 | -1.219 | 0.2229 | 0.7643 |  |
| Education: high school or below (vs college) | +0.1328 | 0.2569 | ±0.5139 | +0.517 | 0.6054 | 1.1420 |  |
| Site: UCSD (vs UAB) | -0.2001 | 0.2367 | ±0.4734 | -0.845 | 0.3979 | 0.8186 |  |
| Site: UW (vs UAB) | -0.3367 | 0.2271 | ±0.4542 | -1.483 | 0.1381 | 0.7141 |  |
| **Age (years)** | **-0.0417** | 0.0097 | ±0.0194 | **-4.289** | **1.79e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0126 | ±0.0252 | **+2.575** | **0.0100** | 1.0330 | * |
| Hypertension | +0.2590 | 0.2192 | ±0.4383 | +1.182 | 0.2374 | 1.2956 |  |
| High cholesterol | +0.1915 | 0.2032 | ±0.4064 | +0.942 | 0.3461 | 1.2110 |  |
| Kidney disease | +0.3705 | 0.2414 | ±0.4829 | +1.535 | 0.1249 | 1.4485 |  |
| **Circulatory disease** | **+0.7477** | 0.2247 | ±0.4494 | **+3.327** | **8.77e-04** | 2.1120 | *** |
| HbA1c (%) | +0.1070 | 0.0628 | ±0.1255 | +1.705 | 0.0882 | 1.1130 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0931**, LLR χ² = **75.54** (p = **1.07e-11**), AUC = **0.7101**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5363 | 0.8430 | ±1.6861 | -0.636 | 0.5247 | 0.5849 |  |
| Education: graduate level (vs college) | -0.2842 | 0.2201 | ±0.4402 | -1.291 | 0.1966 | 0.7526 |  |
| Education: high school or below (vs college) | +0.1569 | 0.2553 | ±0.5106 | +0.614 | 0.5390 | 1.1698 |  |
| Site: UCSD (vs UAB) | -0.2036 | 0.2365 | ±0.4731 | -0.861 | 0.3894 | 0.8158 |  |
| Site: UW (vs UAB) | -0.3501 | 0.2264 | ±0.4529 | -1.546 | 0.1221 | 0.7046 |  |
| **Age (years)** | **-0.0417** | 0.0097 | ±0.0194 | **-4.303** | **1.68e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0336** | 0.0125 | ±0.0251 | **+2.684** | **0.0073** | 1.0342 | ** |
| Hypertension | +0.2653 | 0.2187 | ±0.4374 | +1.213 | 0.2252 | 1.3038 |  |
| High cholesterol | +0.1992 | 0.2030 | ±0.4060 | +0.981 | 0.3264 | 1.2205 |  |
| Kidney disease | +0.3536 | 0.2414 | ±0.4827 | +1.465 | 0.1429 | 1.4242 |  |
| **Circulatory disease** | **+0.7490** | 0.2248 | ±0.4495 | **+3.332** | **8.61e-04** | 2.1148 | *** |
| Mean glucose (mg/dL) | +0.0026 | 0.0021 | ±0.0043 | +1.194 | 0.2324 | 1.0026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0931**, LLR χ² = **75.54** (p = **1.07e-11**), AUC = **0.7101**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8902 | 1.0018 | ±2.0036 | -0.889 | 0.3742 | 0.4106 |  |
| Education: graduate level (vs college) | -0.2842 | 0.2201 | ±0.4402 | -1.291 | 0.1966 | 0.7526 |  |
| Education: high school or below (vs college) | +0.1569 | 0.2553 | ±0.5106 | +0.614 | 0.5390 | 1.1698 |  |
| Site: UCSD (vs UAB) | -0.2036 | 0.2365 | ±0.4731 | -0.861 | 0.3894 | 0.8158 |  |
| Site: UW (vs UAB) | -0.3501 | 0.2264 | ±0.4529 | -1.546 | 0.1221 | 0.7046 |  |
| **Age (years)** | **-0.0417** | 0.0097 | ±0.0194 | **-4.303** | **1.68e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0336** | 0.0125 | ±0.0251 | **+2.684** | **0.0073** | 1.0342 | ** |
| Hypertension | +0.2653 | 0.2187 | ±0.4374 | +1.213 | 0.2252 | 1.3038 |  |
| High cholesterol | +0.1992 | 0.2030 | ±0.4060 | +0.981 | 0.3264 | 1.2205 |  |
| Kidney disease | +0.3536 | 0.2414 | ±0.4827 | +1.465 | 0.1429 | 1.4242 |  |
| **Circulatory disease** | **+0.7490** | 0.2248 | ±0.4495 | **+3.332** | **8.61e-04** | 2.1148 | *** |
| GMI (%) | +0.1069 | 0.0895 | ±0.1791 | +1.194 | 0.2324 | 1.1129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0961**, LLR χ² = **77.93** (p = **3.71e-12**), AUC = **0.7141**, AIC = **757.1**, BIC = **813.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7359 | 0.8313 | ±1.6627 | -0.885 | 0.3761 | 0.4791 |  |
| Education: graduate level (vs college) | -0.2650 | 0.2207 | ±0.4413 | -1.201 | 0.2298 | 0.7672 |  |
| Education: high school or below (vs college) | +0.1413 | 0.2557 | ±0.5114 | +0.552 | 0.5806 | 1.1517 |  |
| Site: UCSD (vs UAB) | -0.1912 | 0.2369 | ±0.4738 | -0.807 | 0.4195 | 0.8259 |  |
| Site: UW (vs UAB) | -0.3485 | 0.2264 | ±0.4527 | -1.539 | 0.1237 | 0.7058 |  |
| **Age (years)** | **-0.0410** | 0.0097 | ±0.0194 | **-4.220** | **2.44e-05** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0319** | 0.0126 | ±0.0252 | **+2.532** | **0.0113** | 1.0324 | * |
| Hypertension | +0.2649 | 0.2190 | ±0.4381 | +1.209 | 0.2266 | 1.3032 |  |
| High cholesterol | +0.1996 | 0.2034 | ±0.4068 | +0.981 | 0.3264 | 1.2209 |  |
| Kidney disease | +0.3657 | 0.2415 | ±0.4830 | +1.514 | 0.1299 | 1.4416 |  |
| **Circulatory disease** | **+0.7431** | 0.2248 | ±0.4495 | **+3.306** | **9.46e-04** | 2.1024 | *** |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0039** | 0.0020 | ±0.0040 | **+1.965** | **0.0494** | 1.0039 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0958**, LLR χ² = **77.71** (p = **4.09e-12**), AUC = **0.7131**, AIC = **757.4**, BIC = **813.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6183 | 0.8124 | ±1.6247 | -0.761 | 0.4466 | 0.5389 |  |
| Education: graduate level (vs college) | -0.2664 | 0.2208 | ±0.4416 | -1.206 | 0.2277 | 0.7662 |  |
| Education: high school or below (vs college) | +0.1458 | 0.2552 | ±0.5103 | +0.572 | 0.5676 | 1.1570 |  |
| Site: UCSD (vs UAB) | -0.2083 | 0.2365 | ±0.4730 | -0.881 | 0.3784 | 0.8119 |  |
| Site: UW (vs UAB) | -0.3214 | 0.2275 | ±0.4550 | -1.413 | 0.1577 | 0.7251 |  |
| **Age (years)** | **-0.0421** | 0.0097 | ±0.0193 | **-4.349** | **1.37e-05** | 0.9588 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0126 | ±0.0251 | **+2.593** | **0.0095** | 1.0331 | ** |
| Hypertension | +0.2568 | 0.2193 | ±0.4386 | +1.171 | 0.2415 | 1.2928 |  |
| High cholesterol | +0.2088 | 0.2032 | ±0.4063 | +1.028 | 0.3040 | 1.2322 |  |
| Kidney disease | +0.2731 | 0.2465 | ±0.4930 | +1.108 | 0.2678 | 1.3141 |  |
| **Circulatory disease** | **+0.7512** | 0.2250 | ±0.4501 | **+3.338** | **8.43e-04** | 2.1195 | *** |
| Glucose SD, pooled (mg/dL) | +0.0143 | 0.0075 | ±0.0150 | +1.898 | 0.0577 | 1.0144 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0930**, LLR χ² = **75.40** (p = **1.14e-11**), AUC = **0.7096**, AIC = **759.7**, BIC = **815.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4310 | 0.8153 | ±1.6306 | -0.529 | 0.5970 | 0.6498 |  |
| Education: graduate level (vs college) | -0.2836 | 0.2202 | ±0.4405 | -1.288 | 0.1978 | 0.7531 |  |
| Education: high school or below (vs college) | +0.1619 | 0.2548 | ±0.5096 | +0.635 | 0.5252 | 1.1757 |  |
| Site: UCSD (vs UAB) | -0.2143 | 0.2360 | ±0.4720 | -0.908 | 0.3639 | 0.8071 |  |
| Site: UW (vs UAB) | -0.3458 | 0.2268 | ±0.4536 | -1.525 | 0.1273 | 0.7076 |  |
| **Age (years)** | **-0.0423** | 0.0097 | ±0.0194 | **-4.373** | **1.23e-05** | 0.9586 | *** |
| **BMI (kg/m2)** | **+0.0341** | 0.0125 | ±0.0250 | **+2.731** | **0.0063** | 1.0347 | ** |
| Hypertension | +0.2672 | 0.2187 | ±0.4374 | +1.222 | 0.2219 | 1.3063 |  |
| High cholesterol | +0.2077 | 0.2029 | ±0.4058 | +1.024 | 0.3060 | 1.2308 |  |
| Kidney disease | +0.3044 | 0.2468 | ±0.4936 | +1.233 | 0.2175 | 1.3558 |  |
| **Circulatory disease** | **+0.7588** | 0.2247 | ±0.4493 | **+3.377** | **7.32e-04** | 2.1357 | *** |
| Avg. daily SD (mg/dL) | +0.0097 | 0.0086 | ±0.0172 | +1.128 | 0.2592 | 1.0098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0918**, LLR χ² = **74.48** (p = **1.70e-11**), AUC = **0.7080**, AIC = **760.6**, BIC = **816.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3433 | 0.8512 | ±1.7025 | -0.403 | 0.6867 | 0.7094 |  |
| Education: graduate level (vs college) | -0.2943 | 0.2199 | ±0.4398 | -1.338 | 0.1807 | 0.7450 |  |
| Education: high school or below (vs college) | +0.1914 | 0.2530 | ±0.5059 | +0.757 | 0.4492 | 1.2110 |  |
| Site: UCSD (vs UAB) | -0.2247 | 0.2357 | ±0.4713 | -0.954 | 0.3403 | 0.7987 |  |
| Site: UW (vs UAB) | -0.3632 | 0.2260 | ±0.4521 | -1.607 | 0.1081 | 0.6955 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0194 | **-4.400** | **1.08e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0350** | 0.0124 | ±0.0249 | **+2.813** | **0.0049** | 1.0356 | ** |
| Hypertension | +0.2707 | 0.2187 | ±0.4374 | +1.238 | 0.2159 | 1.3108 |  |
| High cholesterol | +0.2127 | 0.2032 | ±0.4065 | +1.047 | 0.2952 | 1.2371 |  |
| Kidney disease | +0.3286 | 0.2479 | ±0.4957 | +1.326 | 0.1850 | 1.3890 |  |
| **Circulatory disease** | **+0.7671** | 0.2248 | ±0.4496 | **+3.412** | **6.44e-04** | 2.1536 | *** |
| CV (%) | +0.0101 | 0.0171 | ±0.0341 | +0.589 | 0.5557 | 1.0101 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.27** (p = **1.87e-11**), AUC = **0.7073**, AIC = **760.8**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0371 | 0.8878 | ±1.7755 | +0.042 | 0.9666 | 1.0378 |  |
| Education: graduate level (vs college) | -0.2970 | 0.2198 | ±0.4396 | -1.351 | 0.1767 | 0.7430 |  |
| Education: high school or below (vs college) | +0.1933 | 0.2529 | ±0.5058 | +0.764 | 0.4446 | 1.2132 |  |
| Site: UCSD (vs UAB) | -0.2260 | 0.2357 | ±0.4713 | -0.959 | 0.3377 | 0.7977 |  |
| Site: UW (vs UAB) | -0.3682 | 0.2259 | ±0.4517 | -1.630 | 0.1031 | 0.6920 |  |
| **Age (years)** | **-0.0425** | 0.0097 | ±0.0194 | **-4.389** | **1.14e-05** | 0.9584 | *** |
| **BMI (kg/m2)** | **+0.0352** | 0.0124 | ±0.0249 | **+2.830** | **0.0047** | 1.0358 | ** |
| Hypertension | +0.2733 | 0.2186 | ±0.4371 | +1.251 | 0.2111 | 1.3144 |  |
| High cholesterol | +0.2076 | 0.2029 | ±0.4059 | +1.023 | 0.3063 | 1.2307 |  |
| Kidney disease | +0.3445 | 0.2457 | ±0.4915 | +1.402 | 0.1609 | 1.4113 |  |
| **Circulatory disease** | **+0.7641** | 0.2248 | ±0.4495 | **+3.400** | **6.74e-04** | 2.1471 | *** |
| Mean / SD ratio | -0.0346 | 0.0945 | ±0.1891 | -0.366 | 0.7147 | 0.9660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0918**, LLR χ² = **74.45** (p = **1.73e-11**), AUC = **0.7074**, AIC = **760.6**, BIC = **816.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3541 | 0.8683 | ±1.7367 | -0.408 | 0.6834 | 0.7018 |  |
| Education: graduate level (vs college) | -0.3056 | 0.2196 | ±0.4393 | -1.391 | 0.1641 | 0.7367 |  |
| Education: high school or below (vs college) | +0.1948 | 0.2530 | ±0.5060 | +0.770 | 0.4413 | 1.2151 |  |
| Site: UCSD (vs UAB) | -0.2212 | 0.2357 | ±0.4714 | -0.939 | 0.3479 | 0.8015 |  |
| Site: UW (vs UAB) | -0.3822 | 0.2256 | ±0.4513 | -1.694 | 0.0903 | 0.6824 | . |
| **Age (years)** | **-0.0422** | 0.0097 | ±0.0194 | **-4.355** | **1.33e-05** | 0.9587 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0249 | **+2.838** | **0.0045** | 1.0359 | ** |
| Hypertension | +0.2763 | 0.2186 | ±0.4371 | +1.264 | 0.2061 | 1.3183 |  |
| High cholesterol | +0.2030 | 0.2030 | ±0.4061 | +1.000 | 0.3175 | 1.2251 |  |
| Kidney disease | +0.3869 | 0.2453 | ±0.4906 | +1.577 | 0.1147 | 1.4724 |  |
| **Circulatory disease** | **+0.7649** | 0.2245 | ±0.4489 | **+3.408** | **6.54e-04** | 2.1489 | *** |
| Avg. daily mean/SD | +0.0417 | 0.0740 | ±0.1480 | +0.563 | 0.5734 | 1.0425 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0951**, LLR χ² = **77.14** (p = **5.25e-12**), AUC = **0.7093**, AIC = **757.9**, BIC = **814.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9733 | 0.9117 | ±1.8234 | -1.068 | 0.2857 | 0.3778 |  |
| Education: graduate level (vs college) | -0.2684 | 0.2208 | ±0.4415 | -1.216 | 0.2240 | 0.7646 |  |
| Education: high school or below (vs college) | +0.1657 | 0.2548 | ±0.5097 | +0.650 | 0.5155 | 1.1802 |  |
| Site: UCSD (vs UAB) | -0.1999 | 0.2365 | ±0.4730 | -0.846 | 0.3978 | 0.8188 |  |
| Site: UW (vs UAB) | -0.3058 | 0.2291 | ±0.4582 | -1.335 | 0.1820 | 0.7366 |  |
| **Age (years)** | **-0.0410** | 0.0097 | ±0.0195 | **-4.212** | **2.53e-05** | 0.9598 | *** |
| **BMI (kg/m2)** | **+0.0342** | 0.0125 | ±0.0250 | **+2.739** | **0.0062** | 1.0348 | ** |
| Hypertension | +0.2867 | 0.2194 | ±0.4389 | +1.307 | 0.1914 | 1.3320 |  |
| High cholesterol | +0.2280 | 0.2039 | ±0.4078 | +1.118 | 0.2635 | 1.2561 |  |
| Kidney disease | +0.3358 | 0.2422 | ±0.4845 | +1.386 | 0.1657 | 1.3990 |  |
| **Circulatory disease** | **+0.7585** | 0.2252 | ±0.4504 | **+3.368** | **7.57e-04** | 2.1351 | *** |
| MAG (mg/dL/h) | +0.0162 | 0.0093 | ±0.0185 | +1.742 | 0.0815 | 1.0163 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0927**, LLR χ² = **75.19** (p = **1.25e-11**), AUC = **0.7094**, AIC = **759.9**, BIC = **816.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5368 | 0.8667 | ±1.7334 | -0.619 | 0.5357 | 0.5846 |  |
| Education: graduate level (vs college) | -0.2843 | 0.2202 | ±0.4405 | -1.291 | 0.1968 | 0.7525 |  |
| Education: high school or below (vs college) | +0.1636 | 0.2549 | ±0.5098 | +0.642 | 0.5208 | 1.1778 |  |
| Site: UCSD (vs UAB) | -0.2110 | 0.2362 | ±0.4723 | -0.893 | 0.3716 | 0.8098 |  |
| Site: UW (vs UAB) | -0.3472 | 0.2269 | ±0.4538 | -1.530 | 0.1260 | 0.7067 |  |
| **Age (years)** | **-0.0420** | 0.0097 | ±0.0194 | **-4.338** | **1.44e-05** | 0.9588 | *** |
| **BMI (kg/m2)** | **+0.0345** | 0.0125 | ±0.0249 | **+2.768** | **0.0056** | 1.0351 | ** |
| Hypertension | +0.2758 | 0.2186 | ±0.4372 | +1.262 | 0.2070 | 1.3176 |  |
| High cholesterol | +0.2088 | 0.2030 | ±0.4059 | +1.029 | 0.3036 | 1.2322 |  |
| Kidney disease | +0.3092 | 0.2469 | ±0.4938 | +1.252 | 0.2104 | 1.3623 |  |
| **Circulatory disease** | **+0.7569** | 0.2249 | ±0.4497 | **+3.366** | **7.62e-04** | 2.1317 | *** |
| Avg. daily range (mg/dL) | +0.0026 | 0.0026 | ±0.0051 | +1.031 | 0.3028 | 1.0026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.1064**, LLR χ² = **86.32** (p = **8.74e-14**), AUC = **0.7259**, AIC = **748.7**, BIC = **804.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5956 | 0.7790 | ±1.5580 | -0.765 | 0.4445 | 0.5512 |  |
| Education: graduate level (vs college) | -0.2203 | 0.2226 | ±0.4453 | -0.990 | 0.3223 | 0.8022 |  |
| Education: high school or below (vs college) | +0.1616 | 0.2564 | ±0.5128 | +0.630 | 0.5286 | 1.1754 |  |
| Site: UCSD (vs UAB) | -0.2058 | 0.2386 | ±0.4771 | -0.863 | 0.3883 | 0.8140 |  |
| Site: UW (vs UAB) | -0.2921 | 0.2283 | ±0.4566 | -1.279 | 0.2008 | 0.7467 |  |
| **Age (years)** | **-0.0405** | 0.0097 | ±0.0193 | **-4.197** | **2.71e-05** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0301** | 0.0126 | ±0.0253 | **+2.381** | **0.0172** | 1.0306 | * |
| Hypertension | +0.2259 | 0.2214 | ±0.4429 | +1.020 | 0.3076 | 1.2535 |  |
| High cholesterol | +0.2066 | 0.2048 | ±0.4095 | +1.009 | 0.3130 | 1.2295 |  |
| Kidney disease | +0.3032 | 0.2447 | ±0.4893 | +1.239 | 0.2153 | 1.3542 |  |
| **Circulatory disease** | **+0.7178** | 0.2276 | ±0.4551 | **+3.154** | **0.0016** | 2.0499 | ** |
| **SD of daily means (mg/dL)** | **+0.0371** | 0.0106 | ±0.0212 | **+3.499** | **4.67e-04** | 1.0378 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0932**, LLR χ² = **75.60** (p = **1.04e-11**), AUC = **0.7096**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2048 | 0.8145 | ±1.6289 | +0.251 | 0.8015 | 1.2273 |  |
| Education: graduate level (vs college) | -0.2822 | 0.2202 | ±0.4405 | -1.281 | 0.2000 | 0.7541 |  |
| Education: high school or below (vs college) | +0.1592 | 0.2549 | ±0.5097 | +0.625 | 0.5321 | 1.1726 |  |
| Site: UCSD (vs UAB) | -0.1997 | 0.2368 | ±0.4735 | -0.843 | 0.3990 | 0.8190 |  |
| Site: UW (vs UAB) | -0.3458 | 0.2267 | ±0.4534 | -1.525 | 0.1272 | 0.7077 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.323** | **1.54e-05** | 0.9590 | *** |
| **BMI (kg/m2)** | **+0.0331** | 0.0126 | ±0.0252 | **+2.626** | **0.0086** | 1.0336 | ** |
| Hypertension | +0.2678 | 0.2187 | ±0.4375 | +1.224 | 0.2208 | 1.3071 |  |
| High cholesterol | +0.2027 | 0.2030 | ±0.4060 | +0.999 | 0.3179 | 1.2248 |  |
| Kidney disease | +0.3440 | 0.2417 | ±0.4835 | +1.423 | 0.1548 | 1.4105 |  |
| **Circulatory disease** | **+0.7506** | 0.2248 | ±0.4495 | **+3.340** | **8.39e-04** | 2.1183 | *** |
| Time in range 70-180, pooled (%) | -0.0043 | 0.0035 | ±0.0071 | -1.220 | 0.2226 | 0.9957 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0929**, LLR χ² = **75.39** (p = **1.14e-11**), AUC = **0.7093**, AIC = **759.7**, BIC = **815.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1842 | 0.8159 | ±1.6318 | +0.226 | 0.8214 | 1.2023 |  |
| Education: graduate level (vs college) | -0.2848 | 0.2201 | ±0.4402 | -1.294 | 0.1957 | 0.7522 |  |
| Education: high school or below (vs college) | +0.1608 | 0.2549 | ±0.5099 | +0.631 | 0.5283 | 1.1744 |  |
| Site: UCSD (vs UAB) | -0.2002 | 0.2368 | ±0.4736 | -0.846 | 0.3978 | 0.8185 |  |
| Site: UW (vs UAB) | -0.3476 | 0.2267 | ±0.4534 | -1.533 | 0.1253 | 0.7064 |  |
| **Age (years)** | **-0.0419** | 0.0097 | ±0.0194 | **-4.333** | **1.47e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0332** | 0.0126 | ±0.0252 | **+2.634** | **0.0084** | 1.0337 | ** |
| Hypertension | +0.2689 | 0.2187 | ±0.4374 | +1.230 | 0.2188 | 1.3085 |  |
| High cholesterol | +0.2029 | 0.2030 | ±0.4060 | +1.000 | 0.3174 | 1.2250 |  |
| Kidney disease | +0.3439 | 0.2418 | ±0.4836 | +1.422 | 0.1549 | 1.4105 |  |
| **Circulatory disease** | **+0.7519** | 0.2247 | ±0.4495 | **+3.346** | **8.20e-04** | 2.1211 | *** |
| Avg. daily time in range 70-180 (%) | -0.0040 | 0.0035 | ±0.0070 | -1.126 | 0.2601 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0993**, LLR χ² = **80.52** (p = **1.17e-12**), AUC = **0.7115**, AIC = **754.5**, BIC = **810.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3244 | 0.7729 | ±1.5457 | -0.420 | 0.6747 | 0.7230 |  |
| Education: graduate level (vs college) | -0.2965 | 0.2208 | ±0.4416 | -1.343 | 0.1794 | 0.7434 |  |
| Education: high school or below (vs college) | +0.2206 | 0.2543 | ±0.5085 | +0.868 | 0.3856 | 1.2468 |  |
| Site: UCSD (vs UAB) | -0.1985 | 0.2369 | ±0.4739 | -0.838 | 0.4021 | 0.8199 |  |
| Site: UW (vs UAB) | -0.3463 | 0.2266 | ±0.4532 | -1.528 | 0.1265 | 0.7073 |  |
| **Age (years)** | **-0.0416** | 0.0097 | ±0.0194 | **-4.287** | **1.81e-05** | 0.9592 | *** |
| **BMI (kg/m2)** | **+0.0351** | 0.0125 | ±0.0250 | **+2.812** | **0.0049** | 1.0357 | ** |
| Hypertension | +0.2391 | 0.2207 | ±0.4414 | +1.084 | 0.2786 | 1.2701 |  |
| High cholesterol | +0.2504 | 0.2049 | ±0.4098 | +1.222 | 0.2217 | 1.2846 |  |
| Kidney disease | +0.3462 | 0.2433 | ±0.4866 | +1.423 | 0.1547 | 1.4137 |  |
| **Circulatory disease** | **+0.7422** | 0.2263 | ±0.4525 | **+3.280** | **0.0010** | 2.1005 | ** |
| **Any reading < 54 during wear (0/1)** | **+0.5266** | 0.2056 | ±0.4112 | **+2.561** | **0.0104** | 1.6931 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0914**, LLR χ² = **74.17** (p = **1.96e-11**), AUC = **0.7070**, AIC = **760.9**, BIC = **817.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1313 | 0.7682 | ±1.5364 | -0.171 | 0.8642 | 0.8769 |  |
| Education: graduate level (vs college) | -0.2990 | 0.2198 | ±0.4396 | -1.360 | 0.1737 | 0.7416 |  |
| Education: high school or below (vs college) | +0.1961 | 0.2533 | ±0.5066 | +0.774 | 0.4388 | 1.2166 |  |
| Site: UCSD (vs UAB) | -0.2219 | 0.2361 | ±0.4721 | -0.940 | 0.3471 | 0.8010 |  |
| Site: UW (vs UAB) | -0.3713 | 0.2259 | ±0.4519 | -1.643 | 0.1003 | 0.6899 |  |
| **Age (years)** | **-0.0425** | 0.0097 | ±0.0194 | **-4.383** | **1.17e-05** | 0.9584 | *** |
| **BMI (kg/m2)** | **+0.0354** | 0.0124 | ±0.0249 | **+2.846** | **0.0044** | 1.0360 | ** |
| Hypertension | +0.2742 | 0.2185 | ±0.4370 | +1.255 | 0.2095 | 1.3155 |  |
| High cholesterol | +0.2093 | 0.2036 | ±0.4073 | +1.028 | 0.3041 | 1.2328 |  |
| Kidney disease | +0.3620 | 0.2412 | ±0.4824 | +1.501 | 0.1334 | 1.4361 |  |
| **Circulatory disease** | **+0.7672** | 0.2249 | ±0.4498 | **+3.412** | **6.46e-04** | 2.1538 | *** |
| Time < 54 (%) | +0.0345 | 0.1860 | ±0.3721 | +0.186 | 0.8527 | 1.0352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.28** (p = **1.87e-11**), AUC = **0.7066**, AIC = **760.8**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1355 | 0.7682 | ±1.5364 | -0.176 | 0.8600 | 0.8733 |  |
| Education: graduate level (vs college) | -0.2974 | 0.2198 | ±0.4395 | -1.353 | 0.1761 | 0.7428 |  |
| Education: high school or below (vs college) | +0.1992 | 0.2534 | ±0.5067 | +0.786 | 0.4316 | 1.2205 |  |
| Site: UCSD (vs UAB) | -0.2189 | 0.2361 | ±0.4723 | -0.927 | 0.3539 | 0.8034 |  |
| Site: UW (vs UAB) | -0.3670 | 0.2262 | ±0.4523 | -1.623 | 0.1047 | 0.6928 |  |
| **Age (years)** | **-0.0425** | 0.0097 | ±0.0194 | **-4.388** | **1.15e-05** | 0.9584 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.844** | **0.0045** | 1.0360 | ** |
| Hypertension | +0.2729 | 0.2186 | ±0.4372 | +1.249 | 0.2118 | 1.3138 |  |
| High cholesterol | +0.2135 | 0.2039 | ±0.4079 | +1.047 | 0.2952 | 1.2380 |  |
| Kidney disease | +0.3610 | 0.2412 | ±0.4824 | +1.497 | 0.1344 | 1.4348 |  |
| **Circulatory disease** | **+0.7688** | 0.2248 | ±0.4496 | **+3.419** | **6.28e-04** | 2.1571 | *** |
| Avg. daily time < 54 (%) | +0.0712 | 0.1834 | ±0.3667 | +0.388 | 0.6979 | 1.0738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.32** (p = **1.83e-11**), AUC = **0.7075**, AIC = **760.7**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1384 | 0.7683 | ±1.5366 | -0.180 | 0.8571 | 0.8708 |  |
| Education: graduate level (vs college) | -0.2967 | 0.2198 | ±0.4396 | -1.350 | 0.1771 | 0.7433 |  |
| Education: high school or below (vs college) | +0.1973 | 0.2531 | ±0.5062 | +0.779 | 0.4357 | 1.2181 |  |
| Site: UCSD (vs UAB) | -0.2174 | 0.2362 | ±0.4724 | -0.920 | 0.3574 | 0.8046 |  |
| Site: UW (vs UAB) | -0.3670 | 0.2260 | ±0.4520 | -1.624 | 0.1044 | 0.6928 |  |
| **Age (years)** | **-0.0426** | 0.0097 | ±0.0194 | **-4.392** | **1.12e-05** | 0.9583 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.839** | **0.0045** | 1.0359 | ** |
| Hypertension | +0.2715 | 0.2187 | ±0.4373 | +1.242 | 0.2143 | 1.3119 |  |
| High cholesterol | +0.2158 | 0.2042 | ±0.4084 | +1.057 | 0.2906 | 1.2409 |  |
| Kidney disease | +0.3572 | 0.2414 | ±0.4829 | +1.479 | 0.1390 | 1.4293 |  |
| **Circulatory disease** | **+0.7710** | 0.2250 | ±0.4501 | **+3.426** | **6.12e-04** | 2.1620 | *** |
| Time 54-69, pooled (%) | +0.0357 | 0.0824 | ±0.1648 | +0.434 | 0.6646 | 1.0364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0919**, LLR χ² = **74.54** (p = **1.66e-11**), AUC = **0.7080**, AIC = **760.5**, BIC = **816.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1406 | 0.7683 | ±1.5365 | -0.183 | 0.8548 | 0.8688 |  |
| Education: graduate level (vs college) | -0.2932 | 0.2200 | ±0.4400 | -1.333 | 0.1826 | 0.7459 |  |
| Education: high school or below (vs college) | +0.2007 | 0.2533 | ±0.5066 | +0.793 | 0.4281 | 1.2223 |  |
| Site: UCSD (vs UAB) | -0.2136 | 0.2363 | ±0.4726 | -0.904 | 0.3661 | 0.8077 |  |
| Site: UW (vs UAB) | -0.3610 | 0.2264 | ±0.4528 | -1.595 | 0.1108 | 0.6970 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0194 | **-4.402** | **1.07e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0352** | 0.0124 | ±0.0249 | **+2.831** | **0.0046** | 1.0358 | ** |
| Hypertension | +0.2697 | 0.2187 | ±0.4374 | +1.233 | 0.2175 | 1.3096 |  |
| High cholesterol | +0.2217 | 0.2045 | ±0.4090 | +1.084 | 0.2783 | 1.2482 |  |
| Kidney disease | +0.3558 | 0.2414 | ±0.4828 | +1.474 | 0.1406 | 1.4273 |  |
| **Circulatory disease** | **+0.7749** | 0.2251 | ±0.4503 | **+3.442** | **5.78e-04** | 2.1703 | *** |
| Avg. daily time 54-69 (%) | +0.0500 | 0.0766 | ±0.1531 | +0.653 | 0.5137 | 1.0513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0916**, LLR χ² = **74.29** (p = **1.85e-11**), AUC = **0.7073**, AIC = **760.8**, BIC = **816.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1392 | 0.7685 | ±1.5369 | -0.181 | 0.8563 | 0.8701 |  |
| Education: graduate level (vs college) | -0.2964 | 0.2199 | ±0.4398 | -1.348 | 0.1777 | 0.7435 |  |
| Education: high school or below (vs college) | +0.1982 | 0.2532 | ±0.5065 | +0.783 | 0.4338 | 1.2192 |  |
| Site: UCSD (vs UAB) | -0.2174 | 0.2363 | ±0.4727 | -0.920 | 0.3577 | 0.8046 |  |
| Site: UW (vs UAB) | -0.3665 | 0.2262 | ±0.4524 | -1.620 | 0.1052 | 0.6932 |  |
| **Age (years)** | **-0.0426** | 0.0097 | ±0.0194 | **-4.392** | **1.12e-05** | 0.9583 | *** |
| **BMI (kg/m2)** | **+0.0353** | 0.0124 | ±0.0248 | **+2.844** | **0.0045** | 1.0360 | ** |
| Hypertension | +0.2719 | 0.2186 | ±0.4373 | +1.244 | 0.2136 | 1.3125 |  |
| High cholesterol | +0.2156 | 0.2044 | ±0.4087 | +1.055 | 0.2914 | 1.2406 |  |
| Kidney disease | +0.3586 | 0.2413 | ±0.4827 | +1.486 | 0.1373 | 1.4313 |  |
| **Circulatory disease** | **+0.7710** | 0.2251 | ±0.4502 | **+3.425** | **6.15e-04** | 2.1619 | *** |
| Time < 70 (%) | +0.0262 | 0.0649 | ±0.1297 | +0.404 | 0.6862 | 1.0266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0919**, LLR χ² = **74.51** (p = **1.69e-11**), AUC = **0.7074**, AIC = **760.6**, BIC = **816.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1416 | 0.7684 | ±1.5367 | -0.184 | 0.8538 | 0.8680 |  |
| Education: graduate level (vs college) | -0.2935 | 0.2200 | ±0.4400 | -1.334 | 0.1822 | 0.7457 |  |
| Education: high school or below (vs college) | +0.2018 | 0.2534 | ±0.5068 | +0.796 | 0.4259 | 1.2236 |  |
| Site: UCSD (vs UAB) | -0.2136 | 0.2364 | ±0.4728 | -0.904 | 0.3661 | 0.8077 |  |
| Site: UW (vs UAB) | -0.3607 | 0.2265 | ±0.4531 | -1.592 | 0.1113 | 0.6972 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0194 | **-4.400** | **1.08e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0352** | 0.0124 | ±0.0248 | **+2.835** | **0.0046** | 1.0358 | ** |
| Hypertension | +0.2700 | 0.2187 | ±0.4374 | +1.235 | 0.2169 | 1.3100 |  |
| High cholesterol | +0.2214 | 0.2046 | ±0.4092 | +1.082 | 0.2793 | 1.2478 |  |
| Kidney disease | +0.3570 | 0.2414 | ±0.4827 | +1.479 | 0.1391 | 1.4290 |  |
| **Circulatory disease** | **+0.7741** | 0.2251 | ±0.4502 | **+3.439** | **5.84e-04** | 2.1687 | *** |
| Avg. daily time < 70 (%) | +0.0368 | 0.0591 | ±0.1182 | +0.623 | 0.5332 | 1.0375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0920**, LLR χ² = **74.64** (p = **1.59e-11**), AUC = **0.7086**, AIC = **760.4**, BIC = **816.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1660 | 0.8700 | ±1.7400 | +0.191 | 0.8487 | 1.1806 |  |
| Education: graduate level (vs college) | -0.2883 | 0.2203 | ±0.4405 | -1.309 | 0.1906 | 0.7495 |  |
| Education: high school or below (vs college) | +0.1734 | 0.2548 | ±0.5097 | +0.680 | 0.4962 | 1.1894 |  |
| Site: UCSD (vs UAB) | -0.2109 | 0.2365 | ±0.4729 | -0.892 | 0.3725 | 0.8099 |  |
| Site: UW (vs UAB) | -0.3574 | 0.2266 | ±0.4533 | -1.577 | 0.1148 | 0.6995 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.302** | **1.70e-05** | 0.9591 | *** |
| **BMI (kg/m2)** | **+0.0347** | 0.0125 | ±0.0249 | **+2.788** | **0.0053** | 1.0354 | ** |
| Hypertension | +0.2676 | 0.2187 | ±0.4374 | +1.224 | 0.2210 | 1.3069 |  |
| High cholesterol | +0.2066 | 0.2028 | ±0.4057 | +1.019 | 0.3084 | 1.2295 |  |
| Kidney disease | +0.3568 | 0.2413 | ±0.4826 | +1.479 | 0.1392 | 1.4288 |  |
| **Circulatory disease** | **+0.7584** | 0.2245 | ±0.4491 | **+3.377** | **7.32e-04** | 2.1348 | *** |
| Time 54-250, pooled (%) | -0.0035 | 0.0049 | ±0.0098 | -0.712 | 0.4766 | 0.9965 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0917**, LLR χ² = **74.40** (p = **1.76e-11**), AUC = **0.7080**, AIC = **760.7**, BIC = **816.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0955 | 0.8779 | ±1.7559 | +0.109 | 0.9133 | 1.1002 |  |
| Education: graduate level (vs college) | -0.2919 | 0.2202 | ±0.4404 | -1.326 | 0.1850 | 0.7468 |  |
| Education: high school or below (vs college) | +0.1787 | 0.2548 | ±0.5095 | +0.701 | 0.4830 | 1.1957 |  |
| Site: UCSD (vs UAB) | -0.2143 | 0.2365 | ±0.4729 | -0.906 | 0.3648 | 0.8071 |  |
| Site: UW (vs UAB) | -0.3623 | 0.2265 | ±0.4530 | -1.600 | 0.1097 | 0.6961 |  |
| **Age (years)** | **-0.0420** | 0.0097 | ±0.0194 | **-4.326** | **1.52e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0349** | 0.0125 | ±0.0249 | **+2.799** | **0.0051** | 1.0355 | ** |
| Hypertension | +0.2700 | 0.2187 | ±0.4373 | +1.235 | 0.2169 | 1.3100 |  |
| High cholesterol | +0.2066 | 0.2028 | ±0.4057 | +1.018 | 0.3085 | 1.2295 |  |
| Kidney disease | +0.3574 | 0.2413 | ±0.4827 | +1.481 | 0.1386 | 1.4296 |  |
| **Circulatory disease** | **+0.7599** | 0.2246 | ±0.4492 | **+3.383** | **7.17e-04** | 2.1381 | *** |
| Avg. daily time 54-250 (%) | -0.0026 | 0.0050 | ±0.0100 | -0.519 | 0.6038 | 0.9974 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0932**, LLR χ² = **75.61** (p = **1.03e-11**), AUC = **0.7094**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1767 | 0.7685 | ±1.5370 | -0.230 | 0.8182 | 0.8381 |  |
| Education: graduate level (vs college) | -0.2963 | 0.2198 | ±0.4396 | -1.348 | 0.1776 | 0.7435 |  |
| Education: high school or below (vs college) | +0.1756 | 0.2532 | ±0.5065 | +0.693 | 0.4881 | 1.1919 |  |
| Site: UCSD (vs UAB) | -0.2113 | 0.2362 | ±0.4723 | -0.895 | 0.3709 | 0.8095 |  |
| Site: UW (vs UAB) | -0.3628 | 0.2256 | ±0.4511 | -1.609 | 0.1077 | 0.6957 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0193 | **-4.417** | **9.99e-06** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0127 | ±0.0253 | **+2.570** | **0.0102** | 1.0331 | * |
| Hypertension | +0.2793 | 0.2189 | ±0.4377 | +1.276 | 0.2019 | 1.3223 |  |
| High cholesterol | +0.1968 | 0.2033 | ±0.4066 | +0.968 | 0.3330 | 1.2175 |  |
| Kidney disease | +0.3418 | 0.2418 | ±0.4836 | +1.414 | 0.1575 | 1.4075 |  |
| **Circulatory disease** | **+0.7533** | 0.2251 | ±0.4502 | **+3.347** | **8.18e-04** | 2.1240 | *** |
| Time 181-250, pooled (%) | +0.0077 | 0.0063 | ±0.0126 | +1.222 | 0.2217 | 1.0077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0934**, LLR χ² = **75.75** (p = **9.74e-12**), AUC = **0.7097**, AIC = **759.3**, BIC = **815.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1798 | 0.7687 | ±1.5374 | -0.234 | 0.8150 | 0.8354 |  |
| Education: graduate level (vs college) | -0.2977 | 0.2198 | ±0.4396 | -1.354 | 0.1756 | 0.7425 |  |
| Education: high school or below (vs college) | +0.1723 | 0.2534 | ±0.5068 | +0.680 | 0.4965 | 1.1881 |  |
| Site: UCSD (vs UAB) | -0.2086 | 0.2363 | ±0.4725 | -0.883 | 0.3772 | 0.8117 |  |
| Site: UW (vs UAB) | -0.3605 | 0.2257 | ±0.4513 | -1.598 | 0.1101 | 0.6973 |  |
| **Age (years)** | **-0.0427** | 0.0097 | ±0.0193 | **-4.413** | **1.02e-05** | 0.9582 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0127 | ±0.0253 | **+2.556** | **0.0106** | 1.0329 | * |
| Hypertension | +0.2792 | 0.2189 | ±0.4377 | +1.276 | 0.2020 | 1.3221 |  |
| High cholesterol | +0.1961 | 0.2033 | ±0.4067 | +0.964 | 0.3349 | 1.2166 |  |
| Kidney disease | +0.3404 | 0.2419 | ±0.4837 | +1.408 | 0.1592 | 1.4056 |  |
| **Circulatory disease** | **+0.7540** | 0.2250 | ±0.4501 | **+3.350** | **8.07e-04** | 2.1254 | *** |
| Avg. daily time 181-250 (%) | +0.0079 | 0.0062 | ±0.0123 | +1.278 | 0.2014 | 1.0079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0931**, LLR χ² = **75.53** (p = **1.07e-11**), AUC = **0.7095**, AIC = **759.5**, BIC = **815.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2203 | 0.7724 | ±1.5447 | -0.285 | 0.7754 | 0.8023 |  |
| Education: graduate level (vs college) | -0.2835 | 0.2202 | ±0.4403 | -1.288 | 0.1979 | 0.7532 |  |
| Education: high school or below (vs college) | +0.1597 | 0.2549 | ±0.5097 | +0.627 | 0.5310 | 1.1731 |  |
| Site: UCSD (vs UAB) | -0.2015 | 0.2367 | ±0.4733 | -0.851 | 0.3945 | 0.8175 |  |
| Site: UW (vs UAB) | -0.3479 | 0.2266 | ±0.4532 | -1.535 | 0.1247 | 0.7062 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.322** | **1.54e-05** | 0.9590 | *** |
| **BMI (kg/m2)** | **+0.0331** | 0.0126 | ±0.0252 | **+2.632** | **0.0085** | 1.0337 | ** |
| Hypertension | +0.2685 | 0.2187 | ±0.4374 | +1.228 | 0.2195 | 1.3080 |  |
| High cholesterol | +0.2015 | 0.2030 | ±0.4060 | +0.992 | 0.3210 | 1.2232 |  |
| Kidney disease | +0.3450 | 0.2417 | ±0.4834 | +1.428 | 0.1534 | 1.4120 |  |
| **Circulatory disease** | **+0.7502** | 0.2248 | ±0.4496 | **+3.337** | **8.46e-04** | 2.1174 | *** |
| Time > 180 (%) | +0.0042 | 0.0035 | ±0.0070 | +1.189 | 0.2343 | 1.0042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0928**, LLR χ² = **75.30** (p = **1.19e-11**), AUC = **0.7091**, AIC = **759.8**, BIC = **815.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2063 | 0.7717 | ±1.5435 | -0.267 | 0.7892 | 0.8136 |  |
| Education: graduate level (vs college) | -0.2862 | 0.2201 | ±0.4401 | -1.301 | 0.1934 | 0.7511 |  |
| Education: high school or below (vs college) | +0.1615 | 0.2550 | ±0.5099 | +0.633 | 0.5265 | 1.1752 |  |
| Site: UCSD (vs UAB) | -0.2023 | 0.2367 | ±0.4734 | -0.855 | 0.3928 | 0.8168 |  |
| Site: UW (vs UAB) | -0.3500 | 0.2266 | ±0.4531 | -1.545 | 0.1224 | 0.7047 |  |
| **Age (years)** | **-0.0419** | 0.0097 | ±0.0194 | **-4.333** | **1.47e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0333** | 0.0126 | ±0.0252 | **+2.643** | **0.0082** | 1.0338 | ** |
| Hypertension | +0.2697 | 0.2187 | ±0.4373 | +1.233 | 0.2174 | 1.3096 |  |
| High cholesterol | +0.2017 | 0.2030 | ±0.4060 | +0.993 | 0.3205 | 1.2234 |  |
| Kidney disease | +0.3452 | 0.2417 | ±0.4835 | +1.428 | 0.1533 | 1.4123 |  |
| **Circulatory disease** | **+0.7516** | 0.2248 | ±0.4496 | **+3.344** | **8.26e-04** | 2.1205 | *** |
| Avg. daily time > 180 (%) | +0.0038 | 0.0035 | ±0.0070 | +1.084 | 0.2786 | 1.0038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0962**, LLR χ² = **78.00** (p = **3.59e-12**), AUC = **0.7141**, AIC = **757.1**, BIC = **813.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2333 | 0.7709 | ±1.5418 | -0.303 | 0.7621 | 0.7919 |  |
| Education: graduate level (vs college) | -0.2579 | 0.2211 | ±0.4422 | -1.166 | 0.2435 | 0.7727 |  |
| Education: high school or below (vs college) | +0.1502 | 0.2549 | ±0.5098 | +0.589 | 0.5557 | 1.1621 |  |
| Site: UCSD (vs UAB) | -0.1808 | 0.2374 | ±0.4748 | -0.762 | 0.4462 | 0.8346 |  |
| Site: UW (vs UAB) | -0.3417 | 0.2266 | ±0.4533 | -1.508 | 0.1316 | 0.7105 |  |
| **Age (years)** | **-0.0412** | 0.0097 | ±0.0194 | **-4.258** | **2.06e-05** | 0.9596 | *** |
| **BMI (kg/m2)** | **+0.0309** | 0.0127 | ±0.0254 | **+2.440** | **0.0147** | 1.0314 | * |
| Hypertension | +0.2690 | 0.2192 | ±0.4383 | +1.227 | 0.2197 | 1.3087 |  |
| High cholesterol | +0.2070 | 0.2034 | ±0.4069 | +1.017 | 0.3090 | 1.2300 |  |
| Kidney disease | +0.3496 | 0.2417 | ±0.4833 | +1.447 | 0.1480 | 1.4185 |  |
| **Circulatory disease** | **+0.7446** | 0.2249 | ±0.4499 | **+3.311** | **9.31e-04** | 2.1057 | *** |
| **Nocturnal time > 180 (%)** | **+0.0062** | 0.0031 | ±0.0062 | **+1.988** | **0.0468** | 1.0062 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0920**, LLR χ² = **74.63** (p = **1.60e-11**), AUC = **0.7087**, AIC = **760.4**, BIC = **816.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1808 | 0.7723 | ±1.5445 | -0.234 | 0.8149 | 0.8346 |  |
| Education: graduate level (vs college) | -0.2886 | 0.2202 | ±0.4405 | -1.310 | 0.1901 | 0.7493 |  |
| Education: high school or below (vs college) | +0.1733 | 0.2549 | ±0.5098 | +0.680 | 0.4965 | 1.1892 |  |
| Site: UCSD (vs UAB) | -0.2112 | 0.2364 | ±0.4728 | -0.893 | 0.3717 | 0.8096 |  |
| Site: UW (vs UAB) | -0.3579 | 0.2266 | ±0.4532 | -1.579 | 0.1143 | 0.6992 |  |
| **Age (years)** | **-0.0418** | 0.0097 | ±0.0194 | **-4.301** | **1.70e-05** | 0.9591 | *** |
| **BMI (kg/m2)** | **+0.0347** | 0.0125 | ±0.0249 | **+2.788** | **0.0053** | 1.0354 | ** |
| Hypertension | +0.2678 | 0.2187 | ±0.4374 | +1.224 | 0.2208 | 1.3070 |  |
| High cholesterol | +0.2063 | 0.2028 | ±0.4057 | +1.017 | 0.3090 | 1.2292 |  |
| Kidney disease | +0.3568 | 0.2413 | ±0.4826 | +1.479 | 0.1392 | 1.4288 |  |
| **Circulatory disease** | **+0.7582** | 0.2246 | ±0.4491 | **+3.376** | **7.34e-04** | 2.1345 | *** |
| Time > 250 (%) | +0.0035 | 0.0049 | ±0.0098 | +0.707 | 0.4795 | 1.0035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 793)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **793**, events = **165**, McFadden pseudo-R² = **0.0917**, LLR χ² = **74.39** (p = **1.77e-11**), AUC = **0.7081**, AIC = **760.7**, BIC = **816.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1617 | 0.7712 | ±1.5425 | -0.210 | 0.8339 | 0.8507 |  |
| Education: graduate level (vs college) | -0.2922 | 0.2202 | ±0.4404 | -1.327 | 0.1845 | 0.7466 |  |
| Education: high school or below (vs college) | +0.1788 | 0.2548 | ±0.5096 | +0.702 | 0.4829 | 1.1958 |  |
| Site: UCSD (vs UAB) | -0.2147 | 0.2364 | ±0.4728 | -0.908 | 0.3639 | 0.8068 |  |
| Site: UW (vs UAB) | -0.3628 | 0.2265 | ±0.4529 | -1.602 | 0.1091 | 0.6957 |  |
| **Age (years)** | **-0.0420** | 0.0097 | ±0.0194 | **-4.327** | **1.51e-05** | 0.9589 | *** |
| **BMI (kg/m2)** | **+0.0349** | 0.0125 | ±0.0249 | **+2.800** | **0.0051** | 1.0355 | ** |
| Hypertension | +0.2702 | 0.2186 | ±0.4373 | +1.236 | 0.2166 | 1.3102 |  |
| High cholesterol | +0.2063 | 0.2028 | ±0.4057 | +1.017 | 0.3090 | 1.2292 |  |
| Kidney disease | +0.3575 | 0.2413 | ±0.4827 | +1.481 | 0.1385 | 1.4297 |  |
| **Circulatory disease** | **+0.7599** | 0.2246 | ±0.4493 | **+3.383** | **7.17e-04** | 2.1381 | *** |
| Avg. daily time > 250 (%) | +0.0025 | 0.0050 | ±0.0100 | +0.509 | 0.6106 | 1.0025 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.1867**, Adj R² = **0.1729**, F-statistic = **13.58** (p = **1.96e-27**), Residual SE = **0.896** on **769** df, AIC = **2063.8**, BIC = **2129.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0481** | 0.3027 | ±0.6055 | **+10.069** | **7.61e-24** | *** |
| Education: graduate level (vs college) | -0.1230 | 0.0666 | ±0.1331 | -1.848 | 0.0646 | . |
| **Education: high school or below (vs college)** | **+0.4850** | 0.1163 | ±0.2326 | **+4.170** | **3.05e-05** | *** |
| Site: UCSD (vs UAB) | +0.0036 | 0.0775 | ±0.1550 | +0.046 | 0.9634 |  |
| **Site: UW (vs UAB)** | **-0.4477** | 0.0796 | ±0.1593 | **-5.621** | **1.90e-08** | *** |
| Season: spring (vs autumn) | -0.0969 | 0.0881 | ±0.1762 | -1.099 | 0.2717 |  |
| Season: summer (vs autumn) | +0.0955 | 0.0890 | ±0.1780 | +1.073 | 0.2834 |  |
| Season: winter (vs autumn) | +0.0567 | 0.0965 | ±0.1929 | +0.587 | 0.5569 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.878** | **6.07e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0054 | ±0.0107 | +1.843 | 0.0654 | . |
| Hypertension | +0.0327 | 0.0685 | ±0.1371 | +0.477 | 0.6334 |  |
| High cholesterol | +0.0420 | 0.0655 | ±0.1311 | +0.641 | 0.5214 |  |
| Kidney disease | -0.0324 | 0.0879 | ±0.1758 | -0.369 | 0.7125 |  |
| Circulatory disease | +0.0262 | 0.0827 | ±0.1654 | +0.317 | 0.7515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.2002**, Adj R² = **0.1856**, F-statistic = **13.73** (p = **1.82e-29**), Residual SE = **0.889** on **768** df, AIC = **2052.7**, BIC = **2122.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5134** | 0.3413 | ±0.6826 | **+7.364** | **1.79e-13** | *** |
| Education: graduate level (vs college) | -0.1057 | 0.0670 | ±0.1339 | -1.578 | 0.1145 |  |
| **Education: high school or below (vs college)** | **+0.4359** | 0.1124 | ±0.2247 | **+3.879** | **1.05e-04** | *** |
| Site: UCSD (vs UAB) | +0.0205 | 0.0775 | ±0.1550 | +0.264 | 0.7915 |  |
| **Site: UW (vs UAB)** | **-0.4243** | 0.0789 | ±0.1579 | **-5.375** | **7.64e-08** | *** |
| Season: spring (vs autumn) | -0.0875 | 0.0879 | ±0.1759 | -0.995 | 0.3195 |  |
| Season: summer (vs autumn) | +0.1079 | 0.0884 | ±0.1769 | +1.220 | 0.2225 |  |
| Season: winter (vs autumn) | +0.0578 | 0.0955 | ±0.1910 | +0.605 | 0.5449 |  |
| **Age (years)** | **-0.0214** | 0.0031 | ±0.0062 | **-6.879** | **6.02e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0055 | ±0.0111 | +1.280 | 0.2004 |  |
| Hypertension | +0.0204 | 0.0680 | ±0.1360 | +0.300 | 0.7641 |  |
| High cholesterol | +0.0320 | 0.0654 | ±0.1308 | +0.490 | 0.6242 |  |
| Kidney disease | -0.0358 | 0.0873 | ±0.1746 | -0.411 | 0.6813 |  |
| Circulatory disease | +0.0071 | 0.0829 | ±0.1657 | +0.085 | 0.9320 |  |
| **HbA1c (%)** | **+0.0891** | 0.0314 | ±0.0627 | **+2.842** | **0.0045** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.1934**, Adj R² = **0.1786**, F-statistic = **13.15** (p = **3.85e-28**), Residual SE = **0.893** on **768** df, AIC = **2059.3**, BIC = **2129.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7491** | 0.3231 | ±0.6462 | **+8.508** | **1.77e-17** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0667 | ±0.1334 | -1.729 | 0.0837 | . |
| **Education: high school or below (vs college)** | **+0.4533** | 0.1132 | ±0.2263 | **+4.006** | **6.18e-05** | *** |
| Site: UCSD (vs UAB) | +0.0194 | 0.0774 | ±0.1548 | +0.251 | 0.8020 |  |
| **Site: UW (vs UAB)** | **-0.4320** | 0.0796 | ±0.1592 | **-5.428** | **5.71e-08** | *** |
| Season: spring (vs autumn) | -0.1041 | 0.0885 | ±0.1771 | -1.176 | 0.2397 |  |
| Season: summer (vs autumn) | +0.1062 | 0.0889 | ±0.1778 | +1.195 | 0.2320 |  |
| Season: winter (vs autumn) | +0.0548 | 0.0959 | ±0.1917 | +0.572 | 0.5676 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0062 | **-6.845** | **7.64e-12** | *** |
| BMI (kg/m2) | +0.0081 | 0.0055 | ±0.0110 | +1.479 | 0.1391 |  |
| Hypertension | +0.0265 | 0.0686 | ±0.1373 | +0.387 | 0.6990 |  |
| High cholesterol | +0.0390 | 0.0656 | ±0.1312 | +0.595 | 0.5517 |  |
| Kidney disease | -0.0453 | 0.0876 | ±0.1752 | -0.517 | 0.6050 |  |
| Circulatory disease | +0.0117 | 0.0831 | ±0.1663 | +0.141 | 0.8881 |  |
| **Mean glucose (mg/dL)** | **+0.0021** | 0.0010 | ±0.0019 | **+2.166** | **0.0303** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.1934**, Adj R² = **0.1786**, F-statistic = **13.15** (p = **3.85e-28**), Residual SE = **0.893** on **768** df, AIC = **2059.3**, BIC = **2129.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4597** | 0.3917 | ±0.7834 | **+6.280** | **3.40e-10** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0667 | ±0.1334 | -1.729 | 0.0837 | . |
| **Education: high school or below (vs college)** | **+0.4533** | 0.1132 | ±0.2263 | **+4.006** | **6.18e-05** | *** |
| Site: UCSD (vs UAB) | +0.0194 | 0.0774 | ±0.1548 | +0.251 | 0.8020 |  |
| **Site: UW (vs UAB)** | **-0.4320** | 0.0796 | ±0.1592 | **-5.428** | **5.71e-08** | *** |
| Season: spring (vs autumn) | -0.1041 | 0.0885 | ±0.1771 | -1.176 | 0.2397 |  |
| Season: summer (vs autumn) | +0.1062 | 0.0889 | ±0.1778 | +1.195 | 0.2320 |  |
| Season: winter (vs autumn) | +0.0548 | 0.0959 | ±0.1917 | +0.572 | 0.5676 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0062 | **-6.845** | **7.64e-12** | *** |
| BMI (kg/m2) | +0.0081 | 0.0055 | ±0.0110 | +1.479 | 0.1391 |  |
| Hypertension | +0.0265 | 0.0686 | ±0.1373 | +0.387 | 0.6990 |  |
| High cholesterol | +0.0390 | 0.0656 | ±0.1312 | +0.595 | 0.5517 |  |
| Kidney disease | -0.0453 | 0.0876 | ±0.1752 | -0.517 | 0.6050 |  |
| Circulatory disease | +0.0117 | 0.0831 | ±0.1663 | +0.141 | 0.8881 |  |
| **GMI (%)** | **+0.0874** | 0.0404 | ±0.0807 | **+2.166** | **0.0303** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.1962**, Adj R² = **0.1816**, F-statistic = **13.39** (p = **1.06e-28**), Residual SE = **0.891** on **768** df, AIC = **2056.5**, BIC = **2126.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7205** | 0.3149 | ±0.6297 | **+8.640** | **5.61e-18** | *** |
| Education: graduate level (vs college) | -0.1100 | 0.0667 | ±0.1334 | -1.648 | 0.0994 | . |
| **Education: high school or below (vs college)** | **+0.4513** | 0.1129 | ±0.2258 | **+3.996** | **6.43e-05** | *** |
| Site: UCSD (vs UAB) | +0.0213 | 0.0771 | ±0.1543 | +0.276 | 0.7824 |  |
| **Site: UW (vs UAB)** | **-0.4352** | 0.0793 | ±0.1586 | **-5.488** | **4.06e-08** | *** |
| Season: spring (vs autumn) | -0.1099 | 0.0884 | ±0.1767 | -1.243 | 0.2137 |  |
| Season: summer (vs autumn) | +0.1089 | 0.0885 | ±0.1771 | +1.230 | 0.2185 |  |
| Season: winter (vs autumn) | +0.0518 | 0.0956 | ±0.1913 | +0.541 | 0.5882 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0062 | **-6.727** | **1.73e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0055 | ±0.0111 | +1.311 | 0.1898 |  |
| Hypertension | +0.0277 | 0.0687 | ±0.1373 | +0.403 | 0.6867 |  |
| High cholesterol | +0.0392 | 0.0656 | ±0.1311 | +0.598 | 0.5500 |  |
| Kidney disease | -0.0378 | 0.0867 | ±0.1734 | -0.436 | 0.6629 |  |
| Circulatory disease | +0.0104 | 0.0828 | ±0.1657 | +0.126 | 0.9001 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0024** | 0.0009 | ±0.0018 | **+2.615** | **0.0089** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.1920**, Adj R² = **0.1772**, F-statistic = **13.03** (p = **7.11e-28**), Residual SE = **0.894** on **768** df, AIC = **2060.7**, BIC = **2130.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8543** | 0.3092 | ±0.6183 | **+9.232** | **2.65e-20** | *** |
| Education: graduate level (vs college) | -0.1122 | 0.0668 | ±0.1337 | -1.679 | 0.0932 | . |
| **Education: high school or below (vs college)** | **+0.4627** | 0.1154 | ±0.2308 | **+4.009** | **6.11e-05** | *** |
| Site: UCSD (vs UAB) | +0.0177 | 0.0774 | ±0.1549 | +0.228 | 0.8195 |  |
| **Site: UW (vs UAB)** | **-0.4245** | 0.0798 | ±0.1595 | **-5.323** | **1.02e-07** | *** |
| Season: spring (vs autumn) | -0.1040 | 0.0885 | ±0.1769 | -1.176 | 0.2396 |  |
| Season: summer (vs autumn) | +0.1028 | 0.0889 | ±0.1778 | +1.156 | 0.2477 |  |
| Season: winter (vs autumn) | +0.0545 | 0.0960 | ±0.1919 | +0.568 | 0.5700 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.906** | **4.99e-12** | *** |
| BMI (kg/m2) | +0.0085 | 0.0054 | ±0.0107 | +1.582 | 0.1136 |  |
| Hypertension | +0.0232 | 0.0684 | ±0.1368 | +0.339 | 0.7345 |  |
| High cholesterol | +0.0457 | 0.0657 | ±0.1315 | +0.695 | 0.4871 |  |
| Kidney disease | -0.0715 | 0.0866 | ±0.1732 | -0.826 | 0.4089 |  |
| Circulatory disease | +0.0154 | 0.0831 | ±0.1662 | +0.185 | 0.8532 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0063** | 0.0028 | ±0.0056 | **+2.240** | **0.0251** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.1897**, Adj R² = **0.1749**, F-statistic = **12.84** (p = **1.95e-27**), Residual SE = **0.895** on **768** df, AIC = **2062.9**, BIC = **2132.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8955** | 0.3111 | ±0.6222 | **+9.308** | **1.31e-20** | *** |
| Education: graduate level (vs college) | -0.1166 | 0.0668 | ±0.1335 | -1.747 | 0.0807 | . |
| **Education: high school or below (vs college)** | **+0.4664** | 0.1162 | ±0.2323 | **+4.015** | **5.95e-05** | *** |
| Site: UCSD (vs UAB) | +0.0144 | 0.0777 | ±0.1554 | +0.186 | 0.8528 |  |
| **Site: UW (vs UAB)** | **-0.4316** | 0.0799 | ±0.1599 | **-5.399** | **6.72e-08** | *** |
| Season: spring (vs autumn) | -0.1020 | 0.0883 | ±0.1767 | -1.155 | 0.2480 |  |
| Season: summer (vs autumn) | +0.1016 | 0.0892 | ±0.1784 | +1.139 | 0.2547 |  |
| Season: winter (vs autumn) | +0.0572 | 0.0963 | ±0.1926 | +0.594 | 0.5525 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.908** | **4.92e-12** | *** |
| BMI (kg/m2) | +0.0091 | 0.0054 | ±0.0108 | +1.685 | 0.0920 | . |
| Hypertension | +0.0264 | 0.0684 | ±0.1369 | +0.386 | 0.6992 |  |
| High cholesterol | +0.0445 | 0.0658 | ±0.1315 | +0.676 | 0.4990 |  |
| Kidney disease | -0.0638 | 0.0869 | ±0.1739 | -0.734 | 0.4630 |  |
| Circulatory disease | +0.0193 | 0.0832 | ±0.1664 | +0.232 | 0.8163 |  |
| Avg. daily SD (mg/dL) | +0.0054 | 0.0031 | ±0.0062 | +1.734 | 0.0830 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.1871**, Adj R² = **0.1723**, F-statistic = **12.62** (p = **6.19e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.4**, BIC = **2135.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9665** | 0.3355 | ±0.6711 | **+8.841** | **9.50e-19** | *** |
| Education: graduate level (vs college) | -0.1207 | 0.0668 | ±0.1336 | -1.807 | 0.0708 | . |
| **Education: high school or below (vs college)** | **+0.4842** | 0.1167 | ±0.2334 | **+4.149** | **3.34e-05** | *** |
| Site: UCSD (vs UAB) | +0.0059 | 0.0777 | ±0.1553 | +0.076 | 0.9397 |  |
| **Site: UW (vs UAB)** | **-0.4425** | 0.0798 | ±0.1597 | **-5.542** | **2.99e-08** | *** |
| Season: spring (vs autumn) | -0.0970 | 0.0883 | ±0.1766 | -1.098 | 0.2721 |  |
| Season: summer (vs autumn) | +0.0957 | 0.0890 | ±0.1781 | +1.075 | 0.2823 |  |
| Season: winter (vs autumn) | +0.0566 | 0.0966 | ±0.1932 | +0.586 | 0.5580 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.882** | **5.91e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.831 | 0.0671 | . |
| Hypertension | +0.0304 | 0.0685 | ±0.1370 | +0.444 | 0.6568 |  |
| High cholesterol | +0.0446 | 0.0658 | ±0.1317 | +0.678 | 0.4978 |  |
| Kidney disease | -0.0434 | 0.0871 | ±0.1741 | -0.498 | 0.6183 |  |
| Circulatory disease | +0.0257 | 0.0829 | ±0.1657 | +0.310 | 0.7562 |  |
| CV (%) | +0.0038 | 0.0063 | ±0.0126 | +0.597 | 0.5507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.1871**, Adj R² = **0.1723**, F-statistic = **12.63** (p = **6.13e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.4**, BIC = **2135.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1478** | 0.3489 | ±0.6977 | **+9.023** | **1.83e-19** | *** |
| Education: graduate level (vs college) | -0.1212 | 0.0667 | ±0.1334 | -1.816 | 0.0694 | . |
| **Education: high school or below (vs college)** | **+0.4844** | 0.1168 | ±0.2336 | **+4.148** | **3.36e-05** | *** |
| Site: UCSD (vs UAB) | +0.0047 | 0.0776 | ±0.1551 | +0.061 | 0.9517 |  |
| **Site: UW (vs UAB)** | **-0.4433** | 0.0799 | ±0.1599 | **-5.545** | **2.94e-08** | *** |
| Season: spring (vs autumn) | -0.0978 | 0.0882 | ±0.1764 | -1.109 | 0.2676 |  |
| Season: summer (vs autumn) | +0.0935 | 0.0890 | ±0.1779 | +1.051 | 0.2935 |  |
| Season: winter (vs autumn) | +0.0553 | 0.0967 | ±0.1933 | +0.573 | 0.5670 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.879** | **6.03e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.839 | 0.0659 | . |
| Hypertension | +0.0305 | 0.0685 | ±0.1369 | +0.445 | 0.6564 |  |
| High cholesterol | +0.0434 | 0.0656 | ±0.1312 | +0.662 | 0.5081 |  |
| Kidney disease | -0.0417 | 0.0874 | ±0.1748 | -0.478 | 0.6330 |  |
| Circulatory disease | +0.0248 | 0.0828 | ±0.1656 | +0.300 | 0.7642 |  |
| Mean / SD ratio | -0.0210 | 0.0346 | ±0.0692 | -0.607 | 0.5439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.1868**, Adj R² = **0.1720**, F-statistic = **12.60** (p = **6.97e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.7**, BIC = **2135.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1007** | 0.3402 | ±0.6803 | **+9.115** | **7.85e-20** | *** |
| Education: graduate level (vs college) | -0.1223 | 0.0667 | ±0.1335 | -1.832 | 0.0670 | . |
| **Education: high school or below (vs college)** | **+0.4845** | 0.1169 | ±0.2339 | **+4.143** | **3.43e-05** | *** |
| Site: UCSD (vs UAB) | +0.0041 | 0.0776 | ±0.1553 | +0.052 | 0.9583 |  |
| **Site: UW (vs UAB)** | **-0.4455** | 0.0800 | ±0.1600 | **-5.567** | **2.58e-08** | *** |
| Season: spring (vs autumn) | -0.0966 | 0.0884 | ±0.1768 | -1.093 | 0.2746 |  |
| Season: summer (vs autumn) | +0.0948 | 0.0889 | ±0.1778 | +1.066 | 0.2863 |  |
| Season: winter (vs autumn) | +0.0566 | 0.0966 | ±0.1933 | +0.585 | 0.5583 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.879** | **6.04e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0053 | ±0.0107 | +1.850 | 0.0643 | . |
| Hypertension | +0.0315 | 0.0685 | ±0.1371 | +0.460 | 0.6455 |  |
| High cholesterol | +0.0430 | 0.0656 | ±0.1312 | +0.655 | 0.5123 |  |
| Kidney disease | -0.0374 | 0.0879 | ±0.1758 | -0.426 | 0.6704 |  |
| Circulatory disease | +0.0260 | 0.0828 | ±0.1656 | +0.314 | 0.7537 |  |
| Avg. daily mean/SD | -0.0096 | 0.0289 | ±0.0578 | -0.331 | 0.7410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.1883**, Adj R² = **0.1736**, F-statistic = **12.73** (p = **3.55e-27**), Residual SE = **0.896** on **768** df, AIC = **2064.2**, BIC = **2134.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8236** | 0.3403 | ±0.6806 | **+8.297** | **1.07e-16** | *** |
| Education: graduate level (vs college) | -0.1151 | 0.0671 | ±0.1342 | -1.715 | 0.0864 | . |
| **Education: high school or below (vs college)** | **+0.4808** | 0.1151 | ±0.2302 | **+4.178** | **2.94e-05** | *** |
| Site: UCSD (vs UAB) | +0.0123 | 0.0775 | ±0.1549 | +0.158 | 0.8743 |  |
| **Site: UW (vs UAB)** | **-0.4302** | 0.0804 | ±0.1608 | **-5.352** | **8.72e-08** | *** |
| Season: spring (vs autumn) | -0.0982 | 0.0885 | ±0.1770 | -1.109 | 0.2673 |  |
| Season: summer (vs autumn) | +0.1049 | 0.0888 | ±0.1777 | +1.181 | 0.2374 |  |
| Season: winter (vs autumn) | +0.0601 | 0.0962 | ±0.1923 | +0.625 | 0.5322 |  |
| **Age (years)** | **-0.0212** | 0.0031 | ±0.0063 | **-6.787** | **1.14e-11** | *** |
| BMI (kg/m2) | +0.0095 | 0.0054 | ±0.0108 | +1.770 | 0.0767 | . |
| Hypertension | +0.0353 | 0.0685 | ±0.1370 | +0.515 | 0.6062 |  |
| High cholesterol | +0.0485 | 0.0662 | ±0.1324 | +0.733 | 0.4634 |  |
| Kidney disease | -0.0419 | 0.0890 | ±0.1781 | -0.470 | 0.6381 |  |
| Circulatory disease | +0.0240 | 0.0829 | ±0.1658 | +0.289 | 0.7725 |  |
| MAG (mg/dL/h) | +0.0043 | 0.0034 | ±0.0068 | +1.271 | 0.2036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.1890**, Adj R² = **0.1742**, F-statistic = **12.78** (p = **2.66e-27**), Residual SE = **0.895** on **768** df, AIC = **2063.6**, BIC = **2133.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8440** | 0.3258 | ±0.6517 | **+8.728** | **2.59e-18** | *** |
| Education: graduate level (vs college) | -0.1175 | 0.0668 | ±0.1336 | -1.758 | 0.0787 | . |
| **Education: high school or below (vs college)** | **+0.4692** | 0.1161 | ±0.2322 | **+4.042** | **5.31e-05** | *** |
| Site: UCSD (vs UAB) | +0.0148 | 0.0776 | ±0.1552 | +0.190 | 0.8492 |  |
| **Site: UW (vs UAB)** | **-0.4326** | 0.0800 | ±0.1599 | **-5.410** | **6.32e-08** | *** |
| Season: spring (vs autumn) | -0.1033 | 0.0884 | ±0.1767 | -1.169 | 0.2425 |  |
| Season: summer (vs autumn) | +0.0978 | 0.0890 | ±0.1779 | +1.099 | 0.2718 |  |
| Season: winter (vs autumn) | +0.0558 | 0.0962 | ±0.1925 | +0.580 | 0.5619 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.854** | **7.16e-12** | *** |
| BMI (kg/m2) | +0.0094 | 0.0054 | ±0.0107 | +1.746 | 0.0808 | . |
| Hypertension | +0.0306 | 0.0686 | ±0.1371 | +0.446 | 0.6555 |  |
| High cholesterol | +0.0450 | 0.0658 | ±0.1316 | +0.684 | 0.4939 |  |
| Kidney disease | -0.0592 | 0.0870 | ±0.1741 | -0.680 | 0.4964 |  |
| Circulatory disease | +0.0197 | 0.0833 | ±0.1665 | +0.237 | 0.8129 |  |
| Avg. daily range (mg/dL) | +0.0014 | 0.0009 | ±0.0018 | +1.537 | 0.1243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.1996**, Adj R² = **0.1851**, F-statistic = **13.68** (p = **2.30e-29**), Residual SE = **0.889** on **768** df, AIC = **2053.2**, BIC = **2123.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9082** | 0.2967 | ±0.5934 | **+9.801** | **1.11e-22** | *** |
| Education: graduate level (vs college) | -0.0971 | 0.0670 | ±0.1340 | -1.449 | 0.1473 |  |
| **Education: high school or below (vs college)** | **+0.4708** | 0.1136 | ±0.2272 | **+4.144** | **3.42e-05** | *** |
| Site: UCSD (vs UAB) | +0.0177 | 0.0768 | ±0.1536 | +0.230 | 0.8181 |  |
| **Site: UW (vs UAB)** | **-0.4199** | 0.0788 | ±0.1575 | **-5.333** | **9.68e-08** | *** |
| Season: spring (vs autumn) | -0.1056 | 0.0881 | ±0.1763 | -1.198 | 0.2310 |  |
| Season: summer (vs autumn) | +0.0964 | 0.0886 | ±0.1773 | +1.088 | 0.2766 |  |
| Season: winter (vs autumn) | +0.0423 | 0.0954 | ±0.1909 | +0.444 | 0.6574 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0062 | **-6.789** | **1.13e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0053 | ±0.0106 | +1.383 | 0.1668 |  |
| Hypertension | +0.0154 | 0.0685 | ±0.1371 | +0.225 | 0.8220 |  |
| High cholesterol | +0.0445 | 0.0653 | ±0.1306 | +0.682 | 0.4952 |  |
| Kidney disease | -0.0583 | 0.0852 | ±0.1703 | -0.685 | 0.4935 |  |
| Circulatory disease | +0.0018 | 0.0821 | ±0.1643 | +0.022 | 0.9825 |  |
| **SD of daily means (mg/dL)** | **+0.0143** | 0.0045 | ±0.0089 | **+3.219** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.1942**, Adj R² = **0.1795**, F-statistic = **13.22** (p = **2.62e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.5**, BIC = **2128.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3612** | 0.3392 | ±0.6785 | **+9.908** | **3.83e-23** | *** |
| Education: graduate level (vs college) | -0.1146 | 0.0667 | ±0.1335 | -1.716 | 0.0861 | . |
| **Education: high school or below (vs college)** | **+0.4524** | 0.1133 | ±0.2265 | **+3.994** | **6.49e-05** | *** |
| Site: UCSD (vs UAB) | +0.0236 | 0.0774 | ±0.1547 | +0.305 | 0.7602 |  |
| **Site: UW (vs UAB)** | **-0.4277** | 0.0796 | ±0.1592 | **-5.374** | **7.68e-08** | *** |
| Season: spring (vs autumn) | -0.1044 | 0.0884 | ±0.1769 | -1.181 | 0.2376 |  |
| Season: summer (vs autumn) | +0.1040 | 0.0886 | ±0.1773 | +1.174 | 0.2406 |  |
| Season: winter (vs autumn) | +0.0516 | 0.0958 | ±0.1916 | +0.538 | 0.5902 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.894** | **5.44e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.396 | 0.1627 |  |
| Hypertension | +0.0281 | 0.0686 | ±0.1372 | +0.410 | 0.6818 |  |
| High cholesterol | +0.0428 | 0.0656 | ±0.1312 | +0.653 | 0.5135 |  |
| Kidney disease | -0.0529 | 0.0873 | ±0.1746 | -0.606 | 0.5443 |  |
| Circulatory disease | +0.0131 | 0.0825 | ±0.1651 | +0.159 | 0.8737 |  |
| **Time in range 70-180, pooled (%)** | **-0.0036** | 0.0015 | ±0.0030 | **-2.381** | **0.0173** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.1942**, Adj R² = **0.1795**, F-statistic = **13.22** (p = **2.63e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.5**, BIC = **2128.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3633** | 0.3399 | ±0.6798 | **+9.895** | **4.39e-23** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0667 | ±0.1335 | -1.729 | 0.0837 | . |
| **Education: high school or below (vs college)** | **+0.4518** | 0.1132 | ±0.2265 | **+3.990** | **6.62e-05** | *** |
| Site: UCSD (vs UAB) | +0.0247 | 0.0773 | ±0.1547 | +0.319 | 0.7498 |  |
| **Site: UW (vs UAB)** | **-0.4274** | 0.0796 | ±0.1591 | **-5.371** | **7.84e-08** | *** |
| Season: spring (vs autumn) | -0.1052 | 0.0885 | ±0.1769 | -1.190 | 0.2342 |  |
| Season: summer (vs autumn) | +0.1030 | 0.0886 | ±0.1772 | +1.162 | 0.2451 |  |
| Season: winter (vs autumn) | +0.0505 | 0.0958 | ±0.1916 | +0.527 | 0.5983 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.898** | **5.26e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.388 | 0.1651 |  |
| Hypertension | +0.0284 | 0.0686 | ±0.1372 | +0.414 | 0.6789 |  |
| High cholesterol | +0.0427 | 0.0656 | ±0.1312 | +0.651 | 0.5152 |  |
| Kidney disease | -0.0541 | 0.0872 | ±0.1744 | -0.620 | 0.5352 |  |
| Circulatory disease | +0.0133 | 0.0826 | ±0.1651 | +0.161 | 0.8717 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0035** | 0.0015 | ±0.0030 | **-2.384** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.1869**, Adj R² = **0.1721**, F-statistic = **12.61** (p = **6.60e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.5**, BIC = **2135.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0332** | 0.3007 | ±0.6015 | **+10.086** | **6.38e-24** | *** |
| Education: graduate level (vs college) | -0.1219 | 0.0666 | ±0.1332 | -1.830 | 0.0672 | . |
| **Education: high school or below (vs college)** | **+0.4871** | 0.1164 | ±0.2328 | **+4.184** | **2.86e-05** | *** |
| Site: UCSD (vs UAB) | +0.0056 | 0.0774 | ±0.1548 | +0.072 | 0.9427 |  |
| **Site: UW (vs UAB)** | **-0.4456** | 0.0793 | ±0.1586 | **-5.618** | **1.93e-08** | *** |
| Season: spring (vs autumn) | -0.0965 | 0.0883 | ±0.1767 | -1.092 | 0.2749 |  |
| Season: summer (vs autumn) | +0.0971 | 0.0893 | ±0.1786 | +1.087 | 0.2769 |  |
| Season: winter (vs autumn) | +0.0594 | 0.0969 | ±0.1937 | +0.613 | 0.5399 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.880** | **5.98e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.838 | 0.0660 | . |
| Hypertension | +0.0307 | 0.0689 | ±0.1377 | +0.446 | 0.6557 |  |
| High cholesterol | +0.0450 | 0.0664 | ±0.1328 | +0.677 | 0.4982 |  |
| Kidney disease | -0.0333 | 0.0876 | ±0.1752 | -0.380 | 0.7036 |  |
| Circulatory disease | +0.0244 | 0.0834 | ±0.1667 | +0.293 | 0.7698 |  |
| Any reading < 54 during wear (0/1) | +0.0383 | 0.0802 | ±0.1603 | +0.478 | 0.6330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.1868**, Adj R² = **0.1720**, F-statistic = **12.60** (p = **6.92e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.6**, BIC = **2135.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0418** | 0.3042 | ±0.6084 | **+10.000** | **1.53e-23** | *** |
| Education: graduate level (vs college) | -0.1215 | 0.0666 | ±0.1332 | -1.824 | 0.0682 | . |
| **Education: high school or below (vs college)** | **+0.4869** | 0.1162 | ±0.2323 | **+4.192** | **2.77e-05** | *** |
| Site: UCSD (vs UAB) | +0.0058 | 0.0777 | ±0.1554 | +0.074 | 0.9408 |  |
| **Site: UW (vs UAB)** | **-0.4449** | 0.0797 | ±0.1594 | **-5.581** | **2.39e-08** | *** |
| Season: spring (vs autumn) | -0.0960 | 0.0883 | ±0.1765 | -1.088 | 0.2765 |  |
| Season: summer (vs autumn) | +0.0966 | 0.0891 | ±0.1781 | +1.084 | 0.2782 |  |
| Season: winter (vs autumn) | +0.0558 | 0.0967 | ±0.1935 | +0.577 | 0.5640 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.881** | **5.93e-12** | *** |
| BMI (kg/m2) | +0.0100 | 0.0054 | ±0.0108 | +1.844 | 0.0652 | . |
| Hypertension | +0.0326 | 0.0687 | ±0.1373 | +0.475 | 0.6350 |  |
| High cholesterol | +0.0442 | 0.0664 | ±0.1328 | +0.665 | 0.5059 |  |
| Kidney disease | -0.0322 | 0.0879 | ±0.1758 | -0.366 | 0.7143 |  |
| Circulatory disease | +0.0272 | 0.0826 | ±0.1653 | +0.329 | 0.7425 |  |
| Time < 54 (%) | +0.0218 | 0.1091 | ±0.2182 | +0.199 | 0.8419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.1874**, Adj R² = **0.1726**, F-statistic = **12.65** (p = **5.45e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.1**, BIC = **2135.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0361** | 0.3036 | ±0.6073 | **+9.999** | **1.53e-23** | *** |
| Education: graduate level (vs college) | -0.1202 | 0.0665 | ±0.1331 | -1.806 | 0.0709 | . |
| **Education: high school or below (vs college)** | **+0.4893** | 0.1160 | ±0.2320 | **+4.218** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | +0.0083 | 0.0776 | ±0.1551 | +0.108 | 0.9143 |  |
| **Site: UW (vs UAB)** | **-0.4411** | 0.0795 | ±0.1590 | **-5.547** | **2.90e-08** | *** |
| Season: spring (vs autumn) | -0.0932 | 0.0883 | ±0.1767 | -1.055 | 0.2912 |  |
| Season: summer (vs autumn) | +0.0997 | 0.0891 | ±0.1781 | +1.119 | 0.2631 |  |
| Season: winter (vs autumn) | +0.0559 | 0.0967 | ±0.1934 | +0.578 | 0.5633 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.895** | **5.38e-12** | *** |
| BMI (kg/m2) | +0.0100 | 0.0054 | ±0.0108 | +1.856 | 0.0635 | . |
| Hypertension | +0.0321 | 0.0687 | ±0.1373 | +0.468 | 0.6397 |  |
| High cholesterol | +0.0472 | 0.0666 | ±0.1332 | +0.709 | 0.4783 |  |
| Kidney disease | -0.0331 | 0.0877 | ±0.1754 | -0.377 | 0.7060 |  |
| Circulatory disease | +0.0280 | 0.0825 | ±0.1651 | +0.340 | 0.7341 |  |
| Avg. daily time < 54 (%) | +0.0531 | 0.0930 | ±0.1860 | +0.571 | 0.5682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.1869**, Adj R² = **0.1721**, F-statistic = **12.61** (p = **6.72e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.6**, BIC = **2135.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0408** | 0.3027 | ±0.6054 | **+10.046** | **9.60e-24** | *** |
| Education: graduate level (vs college) | -0.1210 | 0.0665 | ±0.1330 | -1.820 | 0.0687 | . |
| **Education: high school or below (vs college)** | **+0.4869** | 0.1163 | ±0.2327 | **+4.185** | **2.85e-05** | *** |
| Site: UCSD (vs UAB) | +0.0069 | 0.0774 | ±0.1548 | +0.089 | 0.9293 |  |
| **Site: UW (vs UAB)** | **-0.4440** | 0.0792 | ±0.1583 | **-5.608** | **2.05e-08** | *** |
| Season: spring (vs autumn) | -0.0947 | 0.0889 | ±0.1778 | -1.065 | 0.2867 |  |
| Season: summer (vs autumn) | +0.0982 | 0.0895 | ±0.1790 | +1.097 | 0.2726 |  |
| Season: winter (vs autumn) | +0.0577 | 0.0973 | ±0.1946 | +0.593 | 0.5530 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0063 | **-6.849** | **7.46e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0053 | ±0.0107 | +1.843 | 0.0654 | . |
| Hypertension | +0.0315 | 0.0691 | ±0.1382 | +0.456 | 0.6480 |  |
| High cholesterol | +0.0457 | 0.0670 | ±0.1339 | +0.682 | 0.4952 |  |
| Kidney disease | -0.0338 | 0.0875 | ±0.1751 | -0.386 | 0.6995 |  |
| Circulatory disease | +0.0280 | 0.0826 | ±0.1651 | +0.339 | 0.7344 |  |
| Time 54-69, pooled (%) | +0.0143 | 0.0526 | ±0.1051 | +0.273 | 0.7849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.1871**, Adj R² = **0.1723**, F-statistic = **12.63** (p = **6.14e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.4**, BIC = **2135.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0403** | 0.3024 | ±0.6049 | **+10.052** | **8.97e-24** | *** |
| Education: graduate level (vs college) | -0.1200 | 0.0665 | ±0.1330 | -1.804 | 0.0713 | . |
| **Education: high school or below (vs college)** | **+0.4878** | 0.1163 | ±0.2327 | **+4.193** | **2.75e-05** | *** |
| Site: UCSD (vs UAB) | +0.0082 | 0.0774 | ±0.1548 | +0.106 | 0.9156 |  |
| **Site: UW (vs UAB)** | **-0.4419** | 0.0792 | ±0.1585 | **-5.577** | **2.45e-08** | *** |
| Season: spring (vs autumn) | -0.0940 | 0.0889 | ±0.1777 | -1.058 | 0.2900 |  |
| Season: summer (vs autumn) | +0.0991 | 0.0894 | ±0.1788 | +1.109 | 0.2675 |  |
| Season: winter (vs autumn) | +0.0576 | 0.0972 | ±0.1944 | +0.592 | 0.5538 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0063 | **-6.850** | **7.37e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.841 | 0.0657 | . |
| Hypertension | +0.0311 | 0.0692 | ±0.1384 | +0.449 | 0.6536 |  |
| High cholesterol | +0.0473 | 0.0672 | ±0.1344 | +0.704 | 0.4814 |  |
| Kidney disease | -0.0341 | 0.0874 | ±0.1749 | -0.390 | 0.6964 |  |
| Circulatory disease | +0.0290 | 0.0826 | ±0.1651 | +0.351 | 0.7256 |  |
| Avg. daily time 54-69 (%) | +0.0190 | 0.0526 | ±0.1051 | +0.362 | 0.7171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.1869**, Adj R² = **0.1721**, F-statistic = **12.61** (p = **6.59e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.5**, BIC = **2135.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0388** | 0.3034 | ±0.6068 | **+10.015** | **1.31e-23** | *** |
| Education: graduate level (vs college) | -0.1205 | 0.0665 | ±0.1331 | -1.812 | 0.0700 | . |
| **Education: high school or below (vs college)** | **+0.4876** | 0.1162 | ±0.2324 | **+4.195** | **2.73e-05** | *** |
| Site: UCSD (vs UAB) | +0.0074 | 0.0775 | ±0.1550 | +0.096 | 0.9235 |  |
| **Site: UW (vs UAB)** | **-0.4431** | 0.0793 | ±0.1585 | **-5.591** | **2.26e-08** | *** |
| Season: spring (vs autumn) | -0.0947 | 0.0887 | ±0.1773 | -1.068 | 0.2856 |  |
| Season: summer (vs autumn) | +0.0983 | 0.0893 | ±0.1786 | +1.101 | 0.2709 |  |
| Season: winter (vs autumn) | +0.0571 | 0.0969 | ±0.1938 | +0.589 | 0.5558 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0063 | **-6.857** | **7.06e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0054 | ±0.0107 | +1.847 | 0.0647 | . |
| Hypertension | +0.0317 | 0.0688 | ±0.1377 | +0.460 | 0.6452 |  |
| High cholesterol | +0.0462 | 0.0671 | ±0.1341 | +0.689 | 0.4911 |  |
| Kidney disease | -0.0334 | 0.0876 | ±0.1752 | -0.382 | 0.7028 |  |
| Circulatory disease | +0.0282 | 0.0825 | ±0.1650 | +0.342 | 0.7325 |  |
| Time < 70 (%) | +0.0117 | 0.0341 | ±0.0681 | +0.344 | 0.7309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.1873**, Adj R² = **0.1725**, F-statistic = **12.64** (p = **5.65e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.2**, BIC = **2135.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0371** | 0.3028 | ±0.6056 | **+10.030** | **1.13e-23** | *** |
| Education: graduate level (vs college) | -0.1193 | 0.0665 | ±0.1330 | -1.794 | 0.0728 | . |
| **Education: high school or below (vs college)** | **+0.4890** | 0.1162 | ±0.2324 | **+4.208** | **2.58e-05** | *** |
| Site: UCSD (vs UAB) | +0.0093 | 0.0775 | ±0.1549 | +0.121 | 0.9041 |  |
| **Site: UW (vs UAB)** | **-0.4403** | 0.0793 | ±0.1585 | **-5.554** | **2.79e-08** | *** |
| Season: spring (vs autumn) | -0.0931 | 0.0888 | ±0.1775 | -1.049 | 0.2942 |  |
| Season: summer (vs autumn) | +0.1002 | 0.0893 | ±0.1786 | +1.122 | 0.2620 |  |
| Season: winter (vs autumn) | +0.0572 | 0.0970 | ±0.1940 | +0.590 | 0.5551 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0063 | **-6.867** | **6.55e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0053 | ±0.0107 | +1.847 | 0.0647 | . |
| Hypertension | +0.0310 | 0.0690 | ±0.1380 | +0.450 | 0.6529 |  |
| High cholesterol | +0.0485 | 0.0673 | ±0.1346 | +0.721 | 0.4706 |  |
| Kidney disease | -0.0342 | 0.0874 | ±0.1748 | -0.391 | 0.6957 |  |
| Circulatory disease | +0.0293 | 0.0825 | ±0.1650 | +0.356 | 0.7221 |  |
| Avg. daily time < 70 (%) | +0.0173 | 0.0359 | ±0.0717 | +0.482 | 0.6295 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.1916**, Adj R² = **0.1769**, F-statistic = **13.00** (p = **8.33e-28**), Residual SE = **0.894** on **768** df, AIC = **2061.0**, BIC = **2131.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4286** | 0.3772 | ±0.7543 | **+9.091** | **9.84e-20** | *** |
| Education: graduate level (vs college) | -0.1115 | 0.0674 | ±0.1347 | -1.655 | 0.0980 | . |
| **Education: high school or below (vs college)** | **+0.4613** | 0.1132 | ±0.2264 | **+4.076** | **4.59e-05** | *** |
| Site: UCSD (vs UAB) | +0.0177 | 0.0775 | ±0.1550 | +0.228 | 0.8198 |  |
| **Site: UW (vs UAB)** | **-0.4297** | 0.0796 | ±0.1592 | **-5.399** | **6.69e-08** | *** |
| Season: spring (vs autumn) | -0.0980 | 0.0886 | ±0.1771 | -1.106 | 0.2687 |  |
| Season: summer (vs autumn) | +0.1102 | 0.0891 | ±0.1783 | +1.236 | 0.2165 |  |
| Season: winter (vs autumn) | +0.0566 | 0.0961 | ±0.1923 | +0.589 | 0.5559 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.715** | **1.88e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.659 | 0.0970 | . |
| Hypertension | +0.0263 | 0.0685 | ±0.1370 | +0.384 | 0.7006 |  |
| High cholesterol | +0.0451 | 0.0659 | ±0.1317 | +0.685 | 0.4934 |  |
| Kidney disease | -0.0428 | 0.0881 | ±0.1763 | -0.486 | 0.6268 |  |
| Circulatory disease | +0.0153 | 0.0836 | ±0.1671 | +0.183 | 0.8545 |  |
| Time 54-250, pooled (%) | -0.0043 | 0.0025 | ±0.0050 | -1.724 | 0.0847 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.1917**, Adj R² = **0.1770**, F-statistic = **13.01** (p = **7.98e-28**), Residual SE = **0.894** on **768** df, AIC = **2060.9**, BIC = **2130.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4425** | 0.3797 | ±0.7595 | **+9.066** | **1.24e-19** | *** |
| Education: graduate level (vs college) | -0.1116 | 0.0673 | ±0.1346 | -1.657 | 0.0975 | . |
| **Education: high school or below (vs college)** | **+0.4610** | 0.1132 | ±0.2264 | **+4.073** | **4.64e-05** | *** |
| Site: UCSD (vs UAB) | +0.0180 | 0.0774 | ±0.1549 | +0.233 | 0.8160 |  |
| **Site: UW (vs UAB)** | **-0.4301** | 0.0795 | ±0.1591 | **-5.408** | **6.37e-08** | *** |
| Season: spring (vs autumn) | -0.0984 | 0.0886 | ±0.1771 | -1.112 | 0.2663 |  |
| Season: summer (vs autumn) | +0.1095 | 0.0891 | ±0.1781 | +1.229 | 0.2189 |  |
| Season: winter (vs autumn) | +0.0563 | 0.0961 | ±0.1923 | +0.585 | 0.5583 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.735** | **1.64e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.652 | 0.0986 | . |
| Hypertension | +0.0267 | 0.0685 | ±0.1370 | +0.390 | 0.6969 |  |
| High cholesterol | +0.0452 | 0.0658 | ±0.1317 | +0.686 | 0.4925 |  |
| Kidney disease | -0.0440 | 0.0881 | ±0.1761 | -0.500 | 0.6171 |  |
| Circulatory disease | +0.0146 | 0.0837 | ±0.1673 | +0.175 | 0.8613 |  |
| Avg. daily time 54-250 (%) | -0.0044 | 0.0025 | ±0.0050 | -1.749 | 0.0803 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.1910**, Adj R² = **0.1762**, F-statistic = **12.95** (p = **1.10e-27**), Residual SE = **0.894** on **768** df, AIC = **2061.6**, BIC = **2131.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0478** | 0.3001 | ±0.6002 | **+10.156** | **3.11e-24** | *** |
| Education: graduate level (vs college) | -0.1251 | 0.0666 | ±0.1333 | -1.877 | 0.0605 | . |
| **Education: high school or below (vs college)** | **+0.4679** | 0.1161 | ±0.2321 | **+4.031** | **5.55e-05** | *** |
| Site: UCSD (vs UAB) | +0.0132 | 0.0775 | ±0.1550 | +0.170 | 0.8650 |  |
| **Site: UW (vs UAB)** | **-0.4424** | 0.0797 | ±0.1594 | **-5.552** | **2.82e-08** | *** |
| Season: spring (vs autumn) | -0.1060 | 0.0882 | ±0.1764 | -1.202 | 0.2294 |  |
| Season: summer (vs autumn) | +0.0901 | 0.0889 | ±0.1778 | +1.013 | 0.3112 |  |
| Season: winter (vs autumn) | +0.0499 | 0.0965 | ±0.1929 | +0.518 | 0.6048 |  |
| **Age (years)** | **-0.0220** | 0.0032 | ±0.0063 | **-6.975** | **3.06e-12** | *** |
| BMI (kg/m2) | +0.0080 | 0.0055 | ±0.0111 | +1.446 | 0.1481 |  |
| Hypertension | +0.0339 | 0.0686 | ±0.1371 | +0.495 | 0.6208 |  |
| High cholesterol | +0.0387 | 0.0656 | ±0.1311 | +0.590 | 0.5552 |  |
| Kidney disease | -0.0471 | 0.0871 | ±0.1741 | -0.540 | 0.5889 |  |
| Circulatory disease | +0.0204 | 0.0819 | ±0.1638 | +0.249 | 0.8030 |  |
| Time 181-250, pooled (%) | +0.0045 | 0.0023 | ±0.0047 | +1.940 | 0.0523 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.1909**, Adj R² = **0.1761**, F-statistic = **12.94** (p = **1.15e-27**), Residual SE = **0.894** on **768** df, AIC = **2061.7**, BIC = **2131.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0468** | 0.3001 | ±0.6002 | **+10.152** | **3.23e-24** | *** |
| Education: graduate level (vs college) | -0.1257 | 0.0667 | ±0.1333 | -1.886 | 0.0593 | . |
| **Education: high school or below (vs college)** | **+0.4670** | 0.1160 | ±0.2320 | **+4.026** | **5.67e-05** | *** |
| Site: UCSD (vs UAB) | +0.0143 | 0.0775 | ±0.1550 | +0.184 | 0.8541 |  |
| **Site: UW (vs UAB)** | **-0.4414** | 0.0797 | ±0.1595 | **-5.536** | **3.09e-08** | *** |
| Season: spring (vs autumn) | -0.1063 | 0.0883 | ±0.1765 | -1.205 | 0.2283 |  |
| Season: summer (vs autumn) | +0.0899 | 0.0890 | ±0.1779 | +1.011 | 0.3120 |  |
| Season: winter (vs autumn) | +0.0492 | 0.0965 | ±0.1929 | +0.510 | 0.6102 |  |
| **Age (years)** | **-0.0219** | 0.0031 | ±0.0063 | **-6.965** | **3.29e-12** | *** |
| BMI (kg/m2) | +0.0080 | 0.0055 | ±0.0111 | +1.447 | 0.1479 |  |
| Hypertension | +0.0337 | 0.0686 | ±0.1372 | +0.492 | 0.6228 |  |
| High cholesterol | +0.0384 | 0.0656 | ±0.1312 | +0.586 | 0.5577 |  |
| Kidney disease | -0.0473 | 0.0871 | ±0.1741 | -0.543 | 0.5869 |  |
| Circulatory disease | +0.0211 | 0.0819 | ±0.1639 | +0.258 | 0.7965 |  |
| Avg. daily time 181-250 (%) | +0.0044 | 0.0023 | ±0.0045 | +1.935 | 0.0530 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.1939**, Adj R² = **0.1792**, F-statistic = **13.20** (p = **2.98e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.8**, BIC = **2128.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0092** | 0.3001 | ±0.6001 | **+10.029** | **1.14e-23** | *** |
| Education: graduate level (vs college) | -0.1155 | 0.0667 | ±0.1335 | -1.731 | 0.0834 | . |
| **Education: high school or below (vs college)** | **+0.4525** | 0.1133 | ±0.2265 | **+3.996** | **6.45e-05** | *** |
| Site: UCSD (vs UAB) | +0.0219 | 0.0774 | ±0.1548 | +0.283 | 0.7770 |  |
| **Site: UW (vs UAB)** | **-0.4296** | 0.0796 | ±0.1592 | **-5.398** | **6.76e-08** | *** |
| Season: spring (vs autumn) | -0.1049 | 0.0885 | ±0.1769 | -1.186 | 0.2358 |  |
| Season: summer (vs autumn) | +0.1030 | 0.0887 | ±0.1773 | +1.161 | 0.2455 |  |
| Season: winter (vs autumn) | +0.0516 | 0.0958 | ±0.1917 | +0.539 | 0.5902 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.888** | **5.66e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.402 | 0.1610 |  |
| Hypertension | +0.0285 | 0.0686 | ±0.1372 | +0.416 | 0.6774 |  |
| High cholesterol | +0.0416 | 0.0656 | ±0.1311 | +0.635 | 0.5257 |  |
| Kidney disease | -0.0521 | 0.0875 | ±0.1750 | -0.595 | 0.5516 |  |
| Circulatory disease | +0.0129 | 0.0825 | ±0.1651 | +0.156 | 0.8760 |  |
| **Time > 180 (%)** | **+0.0035** | 0.0015 | ±0.0030 | **+2.331** | **0.0198** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.1939**, Adj R² = **0.1792**, F-statistic = **13.19** (p = **3.08e-28**), Residual SE = **0.893** on **768** df, AIC = **2058.9**, BIC = **2128.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0133** | 0.3002 | ±0.6003 | **+10.039** | **1.02e-23** | *** |
| Education: graduate level (vs college) | -0.1164 | 0.0667 | ±0.1334 | -1.744 | 0.0811 | . |
| **Education: high school or below (vs college)** | **+0.4520** | 0.1132 | ±0.2264 | **+3.992** | **6.55e-05** | *** |
| Site: UCSD (vs UAB) | +0.0229 | 0.0774 | ±0.1547 | +0.296 | 0.7676 |  |
| **Site: UW (vs UAB)** | **-0.4295** | 0.0796 | ±0.1592 | **-5.396** | **6.81e-08** | *** |
| Season: spring (vs autumn) | -0.1057 | 0.0885 | ±0.1770 | -1.194 | 0.2323 |  |
| Season: summer (vs autumn) | +0.1018 | 0.0886 | ±0.1773 | +1.149 | 0.2506 |  |
| Season: winter (vs autumn) | +0.0506 | 0.0958 | ±0.1917 | +0.528 | 0.5978 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.892** | **5.49e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.398 | 0.1622 |  |
| Hypertension | +0.0289 | 0.0686 | ±0.1372 | +0.421 | 0.6739 |  |
| High cholesterol | +0.0414 | 0.0656 | ±0.1311 | +0.631 | 0.5280 |  |
| Kidney disease | -0.0531 | 0.0874 | ±0.1748 | -0.607 | 0.5438 |  |
| Circulatory disease | +0.0131 | 0.0826 | ±0.1651 | +0.159 | 0.8739 |  |
| **Avg. daily time > 180 (%)** | **+0.0034** | 0.0015 | ±0.0030 | **+2.321** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.1944**, Adj R² = **0.1798**, F-statistic = **13.24** (p = **2.37e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.3**, BIC = **2128.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0250** | 0.2999 | ±0.5997 | **+10.088** | **6.23e-24** | *** |
| Education: graduate level (vs college) | -0.1085 | 0.0670 | ±0.1340 | -1.619 | 0.1055 |  |
| **Education: high school or below (vs college)** | **+0.4574** | 0.1133 | ±0.2266 | **+4.038** | **5.39e-05** | *** |
| Site: UCSD (vs UAB) | +0.0235 | 0.0772 | ±0.1544 | +0.305 | 0.7607 |  |
| **Site: UW (vs UAB)** | **-0.4337** | 0.0793 | ±0.1587 | **-5.468** | **4.56e-08** | *** |
| Season: spring (vs autumn) | -0.1082 | 0.0884 | ±0.1769 | -1.223 | 0.2212 |  |
| Season: summer (vs autumn) | +0.1048 | 0.0883 | ±0.1766 | +1.187 | 0.2353 |  |
| Season: winter (vs autumn) | +0.0489 | 0.0959 | ±0.1918 | +0.510 | 0.6103 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0062 | **-6.792** | **1.11e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0056 | ±0.0111 | +1.292 | 0.1964 |  |
| Hypertension | +0.0310 | 0.0685 | ±0.1371 | +0.452 | 0.6513 |  |
| High cholesterol | +0.0434 | 0.0655 | ±0.1311 | +0.663 | 0.5075 |  |
| Kidney disease | -0.0454 | 0.0871 | ±0.1742 | -0.522 | 0.6019 |  |
| Circulatory disease | +0.0139 | 0.0826 | ±0.1651 | +0.168 | 0.8666 |  |
| **Nocturnal time > 180 (%)** | **+0.0033** | 0.0014 | ±0.0027 | **+2.416** | **0.0157** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.1916**, Adj R² = **0.1768**, F-statistic = **13.00** (p = **8.58e-28**), Residual SE = **0.894** on **768** df, AIC = **2061.1**, BIC = **2131.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0005** | 0.3047 | ±0.6095 | **+9.846** | **7.13e-23** | *** |
| Education: graduate level (vs college) | -0.1118 | 0.0673 | ±0.1347 | -1.661 | 0.0967 | . |
| **Education: high school or below (vs college)** | **+0.4611** | 0.1132 | ±0.2263 | **+4.075** | **4.60e-05** | *** |
| Site: UCSD (vs UAB) | +0.0171 | 0.0775 | ±0.1550 | +0.221 | 0.8251 |  |
| **Site: UW (vs UAB)** | **-0.4304** | 0.0796 | ±0.1591 | **-5.409** | **6.36e-08** | *** |
| Season: spring (vs autumn) | -0.0981 | 0.0886 | ±0.1771 | -1.108 | 0.2679 |  |
| Season: summer (vs autumn) | +0.1098 | 0.0891 | ±0.1783 | +1.232 | 0.2179 |  |
| Season: winter (vs autumn) | +0.0568 | 0.0962 | ±0.1923 | +0.591 | 0.5547 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.712** | **1.92e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.655 | 0.0978 | . |
| Hypertension | +0.0264 | 0.0685 | ±0.1370 | +0.385 | 0.7000 |  |
| High cholesterol | +0.0447 | 0.0658 | ±0.1316 | +0.678 | 0.4975 |  |
| Kidney disease | -0.0428 | 0.0882 | ±0.1763 | -0.486 | 0.6272 |  |
| Circulatory disease | +0.0152 | 0.0836 | ±0.1671 | +0.182 | 0.8556 |  |
| Time > 250 (%) | +0.0043 | 0.0025 | ±0.0050 | +1.710 | 0.0872 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.1916**, Adj R² = **0.1769**, F-statistic = **13.00** (p = **8.41e-28**), Residual SE = **0.894** on **768** df, AIC = **2061.0**, BIC = **2131.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0054** | 0.3046 | ±0.6093 | **+9.866** | **5.87e-23** | *** |
| Education: graduate level (vs college) | -0.1119 | 0.0673 | ±0.1346 | -1.663 | 0.0963 | . |
| **Education: high school or below (vs college)** | **+0.4610** | 0.1132 | ±0.2263 | **+4.074** | **4.62e-05** | *** |
| Site: UCSD (vs UAB) | +0.0174 | 0.0774 | ±0.1549 | +0.225 | 0.8217 |  |
| **Site: UW (vs UAB)** | **-0.4308** | 0.0795 | ±0.1590 | **-5.418** | **6.04e-08** | *** |
| Season: spring (vs autumn) | -0.0987 | 0.0886 | ±0.1771 | -1.115 | 0.2650 |  |
| Season: summer (vs autumn) | +0.1090 | 0.0891 | ±0.1781 | +1.224 | 0.2211 |  |
| Season: winter (vs autumn) | +0.0563 | 0.0961 | ±0.1923 | +0.586 | 0.5579 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.733** | **1.66e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.650 | 0.0988 | . |
| Hypertension | +0.0268 | 0.0685 | ±0.1370 | +0.391 | 0.6956 |  |
| High cholesterol | +0.0447 | 0.0658 | ±0.1316 | +0.680 | 0.4967 |  |
| Kidney disease | -0.0438 | 0.0881 | ±0.1762 | -0.498 | 0.6188 |  |
| Circulatory disease | +0.0146 | 0.0837 | ±0.1673 | +0.175 | 0.8614 |  |
| Avg. daily time > 250 (%) | +0.0043 | 0.0025 | ±0.0050 | +1.726 | 0.0843 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.3085**, Adj R² = **0.2968**, F-statistic = **26.39** (p = **2.38e-53**), Residual SE = **1.998** on **769** df, AIC = **3319.9**, BIC = **3385.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9596** | 0.6104 | ±1.2207 | **+37.617** | **1.14e-309** | *** |
| Education: graduate level (vs college) | -0.2588 | 0.1549 | ±0.3098 | -1.670 | 0.0948 | . |
| Education: high school or below (vs college) | +0.0893 | 0.2281 | ±0.4562 | +0.391 | 0.6955 |  |
| Site: UCSD (vs UAB) | +0.0038 | 0.1830 | ±0.3660 | +0.021 | 0.9836 |  |
| **Site: UW (vs UAB)** | **-1.2751** | 0.1744 | ±0.3488 | **-7.310** | **2.66e-13** | *** |
| Season: spring (vs autumn) | -0.2241 | 0.1949 | ±0.3897 | -1.150 | 0.2502 |  |
| **Season: summer (vs autumn)** | **+2.0187** | 0.2218 | ±0.4435 | **+9.103** | **8.79e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9676** | 0.1964 | ±0.3929 | **-4.926** | **8.41e-07** | *** |
| **Age (years)** | **+0.0205** | 0.0075 | ±0.0149 | **+2.752** | **0.0059** | ** |
| BMI (kg/m2) | +0.0193 | 0.0109 | ±0.0219 | +1.762 | 0.0781 | . |
| Hypertension | +0.1308 | 0.1553 | ±0.3106 | +0.842 | 0.3998 |  |
| High cholesterol | +0.0930 | 0.1541 | ±0.3081 | +0.604 | 0.5461 |  |
| Kidney disease | +0.1344 | 0.1965 | ±0.3930 | +0.684 | 0.4940 |  |
| Circulatory disease | +0.1289 | 0.1995 | ±0.3990 | +0.646 | 0.5181 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.3091**, Adj R² = **0.2965**, F-statistic = **24.55** (p = **8.99e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.2**, BIC = **3391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6830** | 0.7513 | ±1.5025 | **+30.193** | **2.92e-200** | *** |
| Education: graduate level (vs college) | -0.2498 | 0.1570 | ±0.3139 | -1.591 | 0.1115 |  |
| Education: high school or below (vs college) | +0.0639 | 0.2310 | ±0.4619 | +0.277 | 0.7821 |  |
| Site: UCSD (vs UAB) | +0.0125 | 0.1850 | ±0.3701 | +0.068 | 0.9460 |  |
| **Site: UW (vs UAB)** | **-1.2630** | 0.1755 | ±0.3510 | **-7.197** | **6.15e-13** | *** |
| Season: spring (vs autumn) | -0.2193 | 0.1966 | ±0.3932 | -1.115 | 0.2647 |  |
| **Season: summer (vs autumn)** | **+2.0251** | 0.2225 | ±0.4449 | **+9.103** | **8.77e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9670** | 0.1962 | ±0.3923 | **-4.930** | **8.24e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.768** | **0.0056** | ** |
| BMI (kg/m2) | +0.0178 | 0.0113 | ±0.0226 | +1.578 | 0.1145 |  |
| Hypertension | +0.1244 | 0.1550 | ±0.3100 | +0.803 | 0.4221 |  |
| High cholesterol | +0.0878 | 0.1556 | ±0.3112 | +0.564 | 0.5725 |  |
| Kidney disease | +0.1326 | 0.1983 | ±0.3966 | +0.669 | 0.5036 |  |
| Circulatory disease | +0.1191 | 0.2024 | ±0.4048 | +0.588 | 0.5564 |  |
| HbA1c (%) | +0.0461 | 0.0767 | ±0.1533 | +0.601 | 0.5477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.02e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7859** | 0.6645 | ±1.3291 | **+34.288** | **1.18e-257** | *** |
| Education: graduate level (vs college) | -0.2543 | 0.1552 | ±0.3104 | -1.639 | 0.1013 |  |
| Education: high school or below (vs college) | +0.0709 | 0.2316 | ±0.4632 | +0.306 | 0.7596 |  |
| Site: UCSD (vs UAB) | +0.0130 | 0.1842 | ±0.3685 | +0.070 | 0.9439 |  |
| **Site: UW (vs UAB)** | **-1.2660** | 0.1764 | ±0.3528 | **-7.176** | **7.17e-13** | *** |
| Season: spring (vs autumn) | -0.2283 | 0.1956 | ±0.3912 | -1.167 | 0.2432 |  |
| **Season: summer (vs autumn)** | **+2.0249** | 0.2223 | ±0.4446 | **+9.108** | **8.36e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9687** | 0.1966 | ±0.3931 | **-4.928** | **8.31e-07** | *** |
| **Age (years)** | **+0.0207** | 0.0075 | ±0.0149 | **+2.771** | **0.0056** | ** |
| BMI (kg/m2) | +0.0183 | 0.0111 | ±0.0222 | +1.645 | 0.0999 | . |
| Hypertension | +0.1272 | 0.1548 | ±0.3096 | +0.822 | 0.4112 |  |
| High cholesterol | +0.0912 | 0.1542 | ±0.3083 | +0.592 | 0.5540 |  |
| Kidney disease | +0.1269 | 0.1969 | ±0.3938 | +0.644 | 0.5193 |  |
| Circulatory disease | +0.1205 | 0.2011 | ±0.4021 | +0.599 | 0.5489 |  |
| Mean glucose (mg/dL) | +0.0012 | 0.0020 | ±0.0040 | +0.609 | 0.5423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.02e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6178** | 0.8139 | ±1.6278 | **+27.790** | **5.70e-170** | *** |
| Education: graduate level (vs college) | -0.2543 | 0.1552 | ±0.3104 | -1.639 | 0.1013 |  |
| Education: high school or below (vs college) | +0.0709 | 0.2316 | ±0.4632 | +0.306 | 0.7596 |  |
| Site: UCSD (vs UAB) | +0.0130 | 0.1842 | ±0.3685 | +0.070 | 0.9439 |  |
| **Site: UW (vs UAB)** | **-1.2660** | 0.1764 | ±0.3528 | **-7.176** | **7.17e-13** | *** |
| Season: spring (vs autumn) | -0.2283 | 0.1956 | ±0.3912 | -1.167 | 0.2432 |  |
| **Season: summer (vs autumn)** | **+2.0249** | 0.2223 | ±0.4446 | **+9.108** | **8.36e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9687** | 0.1966 | ±0.3931 | **-4.928** | **8.31e-07** | *** |
| **Age (years)** | **+0.0207** | 0.0075 | ±0.0149 | **+2.771** | **0.0056** | ** |
| BMI (kg/m2) | +0.0183 | 0.0111 | ±0.0222 | +1.645 | 0.0999 | . |
| Hypertension | +0.1272 | 0.1548 | ±0.3096 | +0.822 | 0.4112 |  |
| High cholesterol | +0.0912 | 0.1542 | ±0.3083 | +0.592 | 0.5540 |  |
| Kidney disease | +0.1269 | 0.1969 | ±0.3938 | +0.644 | 0.5193 |  |
| Circulatory disease | +0.1205 | 0.2011 | ±0.4021 | +0.599 | 0.5489 |  |
| GMI (%) | +0.0508 | 0.0833 | ±0.1667 | +0.609 | 0.5423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.03e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8044** | 0.6542 | ±1.3083 | **+34.861** | **2.90e-266** | *** |
| Education: graduate level (vs college) | -0.2526 | 0.1554 | ±0.3107 | -1.626 | 0.1040 |  |
| Education: high school or below (vs college) | +0.0733 | 0.2310 | ±0.4620 | +0.317 | 0.7509 |  |
| Site: UCSD (vs UAB) | +0.0122 | 0.1840 | ±0.3680 | +0.066 | 0.9473 |  |
| **Site: UW (vs UAB)** | **-1.2692** | 0.1759 | ±0.3519 | **-7.213** | **5.46e-13** | *** |
| Season: spring (vs autumn) | -0.2303 | 0.1960 | ±0.3920 | -1.175 | 0.2401 |  |
| **Season: summer (vs autumn)** | **+2.0251** | 0.2223 | ±0.4445 | **+9.111** | **8.16e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9699** | 0.1966 | ±0.3932 | **-4.933** | **8.10e-07** | *** |
| **Age (years)** | **+0.0208** | 0.0075 | ±0.0149 | **+2.792** | **0.0052** | ** |
| BMI (kg/m2) | +0.0180 | 0.0113 | ±0.0225 | +1.603 | 0.1089 |  |
| Hypertension | +0.1284 | 0.1550 | ±0.3099 | +0.829 | 0.4073 |  |
| High cholesterol | +0.0916 | 0.1542 | ±0.3083 | +0.594 | 0.5522 |  |
| Kidney disease | +0.1318 | 0.1970 | ±0.3939 | +0.669 | 0.5033 |  |
| Circulatory disease | +0.1215 | 0.2010 | ±0.4020 | +0.604 | 0.5457 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0011 | 0.0019 | ±0.0038 | +0.591 | 0.5545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.3093**, Adj R² = **0.2967**, F-statistic = **24.57** (p = **8.11e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7761** | 0.6376 | ±1.2753 | **+35.719** | **2.01e-279** | *** |
| Education: graduate level (vs college) | -0.2485 | 0.1550 | ±0.3100 | -1.603 | 0.1089 |  |
| Education: high school or below (vs college) | +0.0682 | 0.2313 | ±0.4626 | +0.295 | 0.7682 |  |
| Site: UCSD (vs UAB) | +0.0171 | 0.1839 | ±0.3678 | +0.093 | 0.9258 |  |
| **Site: UW (vs UAB)** | **-1.2531** | 0.1773 | ±0.3546 | **-7.067** | **1.58e-12** | *** |
| Season: spring (vs autumn) | -0.2309 | 0.1959 | ±0.3918 | -1.179 | 0.2386 |  |
| **Season: summer (vs autumn)** | **+2.0256** | 0.2220 | ±0.4440 | **+9.124** | **7.26e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9696** | 0.1967 | ±0.3933 | **-4.930** | **8.21e-07** | *** |
| **Age (years)** | **+0.0204** | 0.0075 | ±0.0149 | **+2.738** | **0.0062** | ** |
| BMI (kg/m2) | +0.0180 | 0.0110 | ±0.0220 | +1.631 | 0.1030 |  |
| Hypertension | +0.1218 | 0.1552 | ±0.3104 | +0.785 | 0.4326 |  |
| High cholesterol | +0.0965 | 0.1541 | ±0.3083 | +0.626 | 0.5315 |  |
| Kidney disease | +0.0973 | 0.2006 | ±0.4012 | +0.485 | 0.6275 |  |
| Circulatory disease | +0.1187 | 0.1998 | ±0.3997 | +0.594 | 0.5525 |  |
| Glucose SD, pooled (mg/dL) | +0.0060 | 0.0066 | ±0.0133 | +0.898 | 0.3689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.60e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.3**, BIC = **3391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8103** | 0.6405 | ±1.2810 | **+35.613** | **8.80e-278** | *** |
| Education: graduate level (vs college) | -0.2525 | 0.1550 | ±0.3100 | -1.629 | 0.1033 |  |
| Education: high school or below (vs college) | +0.0711 | 0.2317 | ±0.4634 | +0.307 | 0.7589 |  |
| Site: UCSD (vs UAB) | +0.0144 | 0.1836 | ±0.3672 | +0.078 | 0.9375 |  |
| **Site: UW (vs UAB)** | **-1.2593** | 0.1768 | ±0.3536 | **-7.123** | **1.05e-12** | *** |
| Season: spring (vs autumn) | -0.2292 | 0.1957 | ±0.3914 | -1.171 | 0.2416 |  |
| **Season: summer (vs autumn)** | **+2.0247** | 0.2219 | ±0.4437 | **+9.126** | **7.11e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9671** | 0.1968 | ±0.3936 | **-4.915** | **8.90e-07** | *** |
| **Age (years)** | **+0.0204** | 0.0075 | ±0.0149 | **+2.732** | **0.0063** | ** |
| BMI (kg/m2) | +0.0185 | 0.0110 | ±0.0219 | +1.686 | 0.0918 | . |
| Hypertension | +0.1247 | 0.1556 | ±0.3111 | +0.801 | 0.4229 |  |
| High cholesterol | +0.0954 | 0.1542 | ±0.3085 | +0.618 | 0.5364 |  |
| Kidney disease | +0.1037 | 0.2002 | ±0.4004 | +0.518 | 0.6046 |  |
| Circulatory disease | +0.1222 | 0.1999 | ±0.3997 | +0.612 | 0.5408 |  |
| Avg. daily SD (mg/dL) | +0.0053 | 0.0072 | ±0.0144 | +0.732 | 0.4643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.3094**, Adj R² = **0.2968**, F-statistic = **24.58** (p = **7.87e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6717** | 0.6754 | ±1.3508 | **+33.568** | **4.99e-247** | *** |
| Education: graduate level (vs college) | -0.2505 | 0.1547 | ±0.3094 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +0.0868 | 0.2290 | ±0.4579 | +0.379 | 0.7047 |  |
| Site: UCSD (vs UAB) | +0.0120 | 0.1830 | ±0.3659 | +0.065 | 0.9479 |  |
| **Site: UW (vs UAB)** | **-1.2568** | 0.1754 | ±0.3507 | **-7.167** | **7.69e-13** | *** |
| Season: spring (vs autumn) | -0.2245 | 0.1954 | ±0.3908 | -1.149 | 0.2504 |  |
| **Season: summer (vs autumn)** | **+2.0196** | 0.2217 | ±0.4434 | **+9.109** | **8.32e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9679** | 0.1969 | ±0.3937 | **-4.917** | **8.80e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0075 | ±0.0149 | **+2.703** | **0.0069** | ** |
| BMI (kg/m2) | +0.0189 | 0.0109 | ±0.0219 | +1.731 | 0.0834 | . |
| Hypertension | +0.1228 | 0.1562 | ±0.3124 | +0.786 | 0.4316 |  |
| High cholesterol | +0.1022 | 0.1545 | ±0.3089 | +0.662 | 0.5083 |  |
| Kidney disease | +0.0956 | 0.2021 | ±0.4043 | +0.473 | 0.6361 |  |
| Circulatory disease | +0.1273 | 0.1994 | ±0.3987 | +0.639 | 0.5230 |  |
| CV (%) | +0.0132 | 0.0133 | ±0.0266 | +0.993 | 0.3207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.3104**, Adj R² = **0.2978**, F-statistic = **24.69** (p = **4.65e-53**), Residual SE = **1.997** on **768** df, AIC = **3319.8**, BIC = **3389.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4599** | 0.6962 | ±1.3925 | **+33.695** | **6.89e-249** | *** |
| Education: graduate level (vs college) | -0.2494 | 0.1544 | ±0.3087 | -1.616 | 0.1062 |  |
| Education: high school or below (vs college) | +0.0863 | 0.2290 | ±0.4581 | +0.377 | 0.7063 |  |
| Site: UCSD (vs UAB) | +0.0095 | 0.1826 | ±0.3651 | +0.052 | 0.9585 |  |
| **Site: UW (vs UAB)** | **-1.2528** | 0.1750 | ±0.3500 | **-7.159** | **8.10e-13** | *** |
| Season: spring (vs autumn) | -0.2288 | 0.1952 | ±0.3905 | -1.172 | 0.2412 |  |
| **Season: summer (vs autumn)** | **+2.0085** | 0.2217 | ±0.4433 | **+9.061** | **1.29e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9743** | 0.1966 | ±0.3932 | **-4.956** | **7.21e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0074 | ±0.0149 | **+2.701** | **0.0069** | ** |
| BMI (kg/m2) | +0.0191 | 0.0109 | ±0.0219 | +1.745 | 0.0810 | . |
| Hypertension | +0.1196 | 0.1559 | ±0.3118 | +0.767 | 0.4431 |  |
| High cholesterol | +0.1000 | 0.1541 | ±0.3083 | +0.649 | 0.5165 |  |
| Kidney disease | +0.0875 | 0.2004 | ±0.4008 | +0.437 | 0.6623 |  |
| Circulatory disease | +0.1222 | 0.1990 | ±0.3980 | +0.614 | 0.5392 |  |
| Mean / SD ratio | -0.1054 | 0.0712 | ±0.1423 | -1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.3098**, Adj R² = **0.2972**, F-statistic = **24.62** (p = **6.41e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.4**, BIC = **3390.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3401** | 0.6895 | ±1.3791 | **+33.848** | **3.82e-251** | *** |
| Education: graduate level (vs college) | -0.2532 | 0.1547 | ±0.3093 | -1.637 | 0.1016 |  |
| Education: high school or below (vs college) | +0.0857 | 0.2293 | ±0.4586 | +0.374 | 0.7087 |  |
| Site: UCSD (vs UAB) | +0.0074 | 0.1828 | ±0.3656 | +0.040 | 0.9677 |  |
| **Site: UW (vs UAB)** | **-1.2594** | 0.1750 | ±0.3500 | **-7.196** | **6.21e-13** | *** |
| Season: spring (vs autumn) | -0.2221 | 0.1951 | ±0.3902 | -1.138 | 0.2550 |  |
| **Season: summer (vs autumn)** | **+2.0137** | 0.2215 | ±0.4431 | **+9.090** | **9.93e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9683** | 0.1970 | ±0.3941 | **-4.914** | **8.93e-07** | *** |
| **Age (years)** | **+0.0200** | 0.0075 | ±0.0149 | **+2.686** | **0.0072** | ** |
| BMI (kg/m2) | +0.0195 | 0.0110 | ±0.0219 | +1.781 | 0.0750 | . |
| Hypertension | +0.1224 | 0.1562 | ±0.3124 | +0.784 | 0.4333 |  |
| High cholesterol | +0.0999 | 0.1543 | ±0.3085 | +0.648 | 0.5171 |  |
| Kidney disease | +0.0981 | 0.1999 | ±0.3999 | +0.491 | 0.6237 |  |
| Circulatory disease | +0.1275 | 0.1994 | ±0.3987 | +0.639 | 0.5226 |  |
| Avg. daily mean/SD | -0.0691 | 0.0597 | ±0.1195 | -1.157 | 0.2473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.3086**, Adj R² = **0.2960**, F-statistic = **24.48** (p = **1.22e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.8**, BIC = **3391.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8706** | 0.7095 | ±1.4190 | **+32.235** | **5.72e-228** | *** |
| Education: graduate level (vs college) | -0.2556 | 0.1562 | ±0.3123 | -1.637 | 0.1017 |  |
| Education: high school or below (vs college) | +0.0876 | 0.2283 | ±0.4566 | +0.384 | 0.7011 |  |
| Site: UCSD (vs UAB) | +0.0072 | 0.1829 | ±0.3658 | +0.039 | 0.9685 |  |
| **Site: UW (vs UAB)** | **-1.2682** | 0.1755 | ±0.3509 | **-7.227** | **4.93e-13** | *** |
| Season: spring (vs autumn) | -0.2246 | 0.1952 | ±0.3903 | -1.151 | 0.2498 |  |
| **Season: summer (vs autumn)** | **+2.0225** | 0.2226 | ±0.4453 | **+9.084** | **1.05e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9662** | 0.1963 | ±0.3927 | **-4.921** | **8.61e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.766** | **0.0057** | ** |
| BMI (kg/m2) | +0.0191 | 0.0110 | ±0.0220 | +1.741 | 0.0816 | . |
| Hypertension | +0.1318 | 0.1557 | ±0.3113 | +0.847 | 0.3971 |  |
| High cholesterol | +0.0956 | 0.1548 | ±0.3096 | +0.617 | 0.5371 |  |
| Kidney disease | +0.1306 | 0.1978 | ±0.3957 | +0.660 | 0.5090 |  |
| Circulatory disease | +0.1281 | 0.1999 | ±0.3998 | +0.641 | 0.5218 |  |
| MAG (mg/dL/h) | +0.0017 | 0.0077 | ±0.0153 | +0.224 | 0.8230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.3094**, Adj R² = **0.2968**, F-statistic = **24.57** (p = **7.99e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6628** | 0.6744 | ±1.3488 | **+33.604** | **1.46e-247** | *** |
| Education: graduate level (vs college) | -0.2507 | 0.1548 | ±0.3095 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +0.0664 | 0.2311 | ±0.4622 | +0.287 | 0.7739 |  |
| Site: UCSD (vs UAB) | +0.0201 | 0.1834 | ±0.3668 | +0.109 | 0.9129 |  |
| **Site: UW (vs UAB)** | **-1.2531** | 0.1768 | ±0.3535 | **-7.089** | **1.35e-12** | *** |
| Season: spring (vs autumn) | -0.2334 | 0.1959 | ±0.3918 | -1.192 | 0.2334 |  |
| **Season: summer (vs autumn)** | **+2.0220** | 0.2216 | ±0.4433 | **+9.124** | **7.27e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9688** | 0.1968 | ±0.3935 | **-4.924** | **8.49e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0074 | ±0.0149 | **+2.770** | **0.0056** | ** |
| BMI (kg/m2) | +0.0186 | 0.0109 | ±0.0219 | +1.696 | 0.0900 | . |
| Hypertension | +0.1277 | 0.1553 | ±0.3107 | +0.822 | 0.4110 |  |
| High cholesterol | +0.0973 | 0.1544 | ±0.3088 | +0.630 | 0.5286 |  |
| Kidney disease | +0.0954 | 0.2004 | ±0.4008 | +0.476 | 0.6340 |  |
| Circulatory disease | +0.1195 | 0.1998 | ±0.3996 | +0.598 | 0.5497 |  |
| Avg. daily range (mg/dL) | +0.0020 | 0.0021 | ±0.0041 | +0.978 | 0.3280 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.3095**, Adj R² = **0.2969**, F-statistic = **24.59** (p = **7.32e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.7**, BIC = **3390.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8655** | 0.6145 | ±1.2291 | **+37.208** | **5.01e-303** | *** |
| Education: graduate level (vs college) | -0.2413 | 0.1558 | ±0.3117 | -1.549 | 0.1215 |  |
| Education: high school or below (vs college) | +0.0798 | 0.2292 | ±0.4585 | +0.348 | 0.7279 |  |
| Site: UCSD (vs UAB) | +0.0133 | 0.1842 | ±0.3684 | +0.072 | 0.9426 |  |
| **Site: UW (vs UAB)** | **-1.2564** | 0.1775 | ±0.3551 | **-7.077** | **1.47e-12** | *** |
| Season: spring (vs autumn) | -0.2299 | 0.1962 | ±0.3925 | -1.172 | 0.2413 |  |
| **Season: summer (vs autumn)** | **+2.0193** | 0.2223 | ±0.4445 | **+9.085** | **1.03e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9772** | 0.1963 | ±0.3926 | **-4.978** | **6.43e-07** | *** |
| **Age (years)** | **+0.0209** | 0.0075 | ±0.0149 | **+2.798** | **0.0051** | ** |
| BMI (kg/m2) | +0.0176 | 0.0112 | ±0.0224 | +1.572 | 0.1159 |  |
| Hypertension | +0.1192 | 0.1547 | ±0.3094 | +0.770 | 0.4412 |  |
| High cholesterol | +0.0947 | 0.1541 | ±0.3082 | +0.614 | 0.5390 |  |
| Kidney disease | +0.1170 | 0.1987 | ±0.3973 | +0.589 | 0.5560 |  |
| Circulatory disease | +0.1126 | 0.2001 | ±0.4003 | +0.562 | 0.5738 |  |
| SD of daily means (mg/dL) | +0.0096 | 0.0112 | ±0.0224 | +0.859 | 0.3901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.3094**, Adj R² = **0.2968**, F-statistic = **24.57** (p = **8.01e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2113** | 0.6837 | ±1.3674 | **+33.949** | **1.28e-252** | *** |
| Education: graduate level (vs college) | -0.2520 | 0.1551 | ±0.3103 | -1.624 | 0.1044 |  |
| Education: high school or below (vs college) | +0.0631 | 0.2315 | ±0.4631 | +0.273 | 0.7852 |  |
| Site: UCSD (vs UAB) | +0.0199 | 0.1841 | ±0.3682 | +0.108 | 0.9139 |  |
| **Site: UW (vs UAB)** | **-1.2590** | 0.1766 | ±0.3532 | **-7.128** | **1.02e-12** | *** |
| Season: spring (vs autumn) | -0.2302 | 0.1956 | ±0.3912 | -1.177 | 0.2393 |  |
| **Season: summer (vs autumn)** | **+2.0256** | 0.2223 | ±0.4447 | **+9.110** | **8.22e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9717** | 0.1963 | ±0.3926 | **-4.950** | **7.41e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.758** | **0.0058** | ** |
| BMI (kg/m2) | +0.0175 | 0.0111 | ±0.0222 | +1.574 | 0.1154 |  |
| Hypertension | +0.1271 | 0.1549 | ±0.3097 | +0.821 | 0.4118 |  |
| High cholesterol | +0.0936 | 0.1540 | ±0.3080 | +0.608 | 0.5431 |  |
| Kidney disease | +0.1179 | 0.1969 | ±0.3938 | +0.599 | 0.5494 |  |
| Circulatory disease | +0.1184 | 0.2006 | ±0.4012 | +0.590 | 0.5550 |  |
| Time in range 70-180, pooled (%) | -0.0029 | 0.0032 | ±0.0064 | -0.896 | 0.3704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.3092**, Adj R² = **0.2966**, F-statistic = **24.55** (p = **8.80e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.1**, BIC = **3391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.1850** | 0.6842 | ±1.3683 | **+33.889** | **9.78e-252** | *** |
| Education: graduate level (vs college) | -0.2533 | 0.1552 | ±0.3104 | -1.632 | 0.1026 |  |
| Education: high school or below (vs college) | +0.0655 | 0.2317 | ±0.4634 | +0.283 | 0.7773 |  |
| Site: UCSD (vs UAB) | +0.0189 | 0.1842 | ±0.3684 | +0.102 | 0.9184 |  |
| **Site: UW (vs UAB)** | **-1.2606** | 0.1767 | ±0.3535 | **-7.133** | **9.85e-13** | *** |
| Season: spring (vs autumn) | -0.2301 | 0.1956 | ±0.3912 | -1.176 | 0.2395 |  |
| **Season: summer (vs autumn)** | **+2.0241** | 0.2223 | ±0.4446 | **+9.105** | **8.65e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9720** | 0.1964 | ±0.3928 | **-4.949** | **7.46e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.754** | **0.0059** | ** |
| BMI (kg/m2) | +0.0177 | 0.0111 | ±0.0223 | +1.590 | 0.1119 |  |
| Hypertension | +0.1277 | 0.1549 | ±0.3098 | +0.824 | 0.4097 |  |
| High cholesterol | +0.0934 | 0.1540 | ±0.3081 | +0.607 | 0.5441 |  |
| Kidney disease | +0.1189 | 0.1968 | ±0.3935 | +0.604 | 0.5457 |  |
| Circulatory disease | +0.1197 | 0.2006 | ±0.4013 | +0.597 | 0.5506 |  |
| Avg. daily time in range 70-180 (%) | -0.0025 | 0.0032 | ±0.0064 | -0.793 | 0.4275 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.3086**, Adj R² = **0.2960**, F-statistic = **24.49** (p = **1.20e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.8**, BIC = **3391.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9791** | 0.6227 | ±1.2453 | **+36.904** | **4.00e-298** | *** |
| Education: graduate level (vs college) | -0.2602 | 0.1548 | ±0.3097 | -1.681 | 0.0928 | . |
| Education: high school or below (vs college) | +0.0864 | 0.2273 | ±0.4545 | +0.380 | 0.7037 |  |
| Site: UCSD (vs UAB) | +0.0012 | 0.1845 | ±0.3689 | +0.006 | 0.9950 |  |
| **Site: UW (vs UAB)** | **-1.2779** | 0.1752 | ±0.3505 | **-7.293** | **3.04e-13** | *** |
| Season: spring (vs autumn) | -0.2246 | 0.1950 | ±0.3900 | -1.152 | 0.2494 |  |
| **Season: summer (vs autumn)** | **+2.0166** | 0.2223 | ±0.4447 | **+9.071** | **1.18e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9711** | 0.1975 | ±0.3949 | **-4.918** | **8.74e-07** | *** |
| **Age (years)** | **+0.0204** | 0.0075 | ±0.0150 | **+2.724** | **0.0064** | ** |
| BMI (kg/m2) | +0.0193 | 0.0109 | ±0.0219 | +1.765 | 0.0776 | . |
| Hypertension | +0.1334 | 0.1563 | ±0.3126 | +0.853 | 0.3935 |  |
| High cholesterol | +0.0891 | 0.1532 | ±0.3064 | +0.582 | 0.5607 |  |
| Kidney disease | +0.1356 | 0.1970 | ±0.3940 | +0.688 | 0.4912 |  |
| Circulatory disease | +0.1313 | 0.1992 | ±0.3985 | +0.659 | 0.5100 |  |
| Any reading < 54 during wear (0/1) | -0.0499 | 0.1711 | ±0.3421 | -0.292 | 0.7704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.3113**, Adj R² = **0.2988**, F-statistic = **24.80** (p = **2.80e-53**), Residual SE = **1.995** on **768** df, AIC = **3318.7**, BIC = **3388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8945** | 0.6099 | ±1.2198 | **+37.537** | **2.30e-308** | *** |
| Education: graduate level (vs college) | -0.2428 | 0.1548 | ±0.3096 | -1.569 | 0.1168 |  |
| Education: high school or below (vs college) | +0.1096 | 0.2286 | ±0.4573 | +0.479 | 0.6318 |  |
| Site: UCSD (vs UAB) | +0.0265 | 0.1828 | ±0.3656 | +0.145 | 0.8849 |  |
| **Site: UW (vs UAB)** | **-1.2464** | 0.1748 | ±0.3495 | **-7.132** | **9.90e-13** | *** |
| Season: spring (vs autumn) | -0.2158 | 0.1954 | ±0.3908 | -1.104 | 0.2695 |  |
| **Season: summer (vs autumn)** | **+2.0299** | 0.2221 | ±0.4441 | **+9.141** | **6.18e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9765** | 0.1960 | ±0.3921 | **-4.981** | **6.31e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0075 | ±0.0149 | **+2.691** | **0.0071** | ** |
| BMI (kg/m2) | +0.0203 | 0.0109 | ±0.0218 | +1.862 | 0.0627 | . |
| Hypertension | +0.1299 | 0.1554 | ±0.3109 | +0.835 | 0.4034 |  |
| High cholesterol | +0.1151 | 0.1542 | ±0.3085 | +0.746 | 0.4556 |  |
| Kidney disease | +0.1365 | 0.1965 | ±0.3930 | +0.694 | 0.4874 |  |
| Circulatory disease | +0.1389 | 0.2001 | ±0.4001 | +0.694 | 0.4875 |  |
| Time < 54 (%) | +0.2230 | 0.1819 | ±0.3639 | +1.226 | 0.2204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.3098**, Adj R² = **0.2972**, F-statistic = **24.63** (p = **6.22e-53**), Residual SE = **1.997** on **768** df, AIC = **3320.4**, BIC = **3390.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9197** | 0.6098 | ±1.2196 | **+37.585** | **3.73e-309** | *** |
| Education: graduate level (vs college) | -0.2492 | 0.1549 | ±0.3098 | -1.609 | 0.1076 |  |
| Education: high school or below (vs college) | +0.1038 | 0.2286 | ±0.4572 | +0.454 | 0.6497 |  |
| Site: UCSD (vs UAB) | +0.0196 | 0.1829 | ±0.3658 | +0.107 | 0.9145 |  |
| **Site: UW (vs UAB)** | **-1.2533** | 0.1751 | ±0.3503 | **-7.156** | **8.30e-13** | *** |
| Season: spring (vs autumn) | -0.2121 | 0.1960 | ±0.3919 | -1.082 | 0.2791 |  |
| **Season: summer (vs autumn)** | **+2.0325** | 0.2228 | ±0.4455 | **+9.124** | **7.24e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9701** | 0.1973 | ±0.3946 | **-4.917** | **8.78e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0075 | ±0.0149 | **+2.708** | **0.0068** | ** |
| BMI (kg/m2) | +0.0197 | 0.0109 | ±0.0219 | +1.797 | 0.0723 | . |
| Hypertension | +0.1290 | 0.1558 | ±0.3117 | +0.828 | 0.4079 |  |
| High cholesterol | +0.1102 | 0.1545 | ±0.3090 | +0.714 | 0.4755 |  |
| Kidney disease | +0.1321 | 0.1967 | ±0.3935 | +0.671 | 0.5019 |  |
| Circulatory disease | +0.1351 | 0.1999 | ±0.3997 | +0.676 | 0.4991 |  |
| Avg. daily time < 54 (%) | +0.1760 | 0.2616 | ±0.5231 | +0.673 | 0.5011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.85e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9345** | 0.6130 | ±1.2260 | **+37.414** | **2.33e-306** | *** |
| Education: graduate level (vs college) | -0.2518 | 0.1555 | ±0.3110 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +0.0958 | 0.2283 | ±0.4565 | +0.420 | 0.6747 |  |
| Site: UCSD (vs UAB) | +0.0151 | 0.1838 | ±0.3675 | +0.082 | 0.9343 |  |
| **Site: UW (vs UAB)** | **-1.2622** | 0.1759 | ±0.3517 | **-7.178** | **7.09e-13** | *** |
| Season: spring (vs autumn) | -0.2168 | 0.1951 | ±0.3903 | -1.111 | 0.2666 |  |
| **Season: summer (vs autumn)** | **+2.0280** | 0.2216 | ±0.4432 | **+9.151** | **5.65e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9639** | 0.1970 | ±0.3940 | **-4.892** | **9.96e-07** | *** |
| **Age (years)** | **+0.0203** | 0.0074 | ±0.0149 | **+2.728** | **0.0064** | ** |
| BMI (kg/m2) | +0.0192 | 0.0110 | ±0.0219 | +1.757 | 0.0790 | . |
| Hypertension | +0.1268 | 0.1566 | ±0.3132 | +0.810 | 0.4181 |  |
| High cholesterol | +0.1056 | 0.1549 | ±0.3097 | +0.682 | 0.4955 |  |
| Kidney disease | +0.1296 | 0.1973 | ±0.3945 | +0.657 | 0.5113 |  |
| Circulatory disease | +0.1352 | 0.2008 | ±0.4017 | +0.673 | 0.5008 |  |
| Time 54-69, pooled (%) | +0.0493 | 0.0842 | ±0.1685 | +0.586 | 0.5580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.3092**, Adj R² = **0.2966**, F-statistic = **24.56** (p = **8.60e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.1**, BIC = **3391.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9353** | 0.6118 | ±1.2236 | **+37.487** | **1.50e-307** | *** |
| Education: graduate level (vs college) | -0.2493 | 0.1553 | ±0.3107 | -1.605 | 0.1085 |  |
| Education: high school or below (vs college) | +0.0982 | 0.2283 | ±0.4565 | +0.430 | 0.6672 |  |
| Site: UCSD (vs UAB) | +0.0182 | 0.1836 | ±0.3673 | +0.099 | 0.9213 |  |
| **Site: UW (vs UAB)** | **-1.2571** | 0.1756 | ±0.3513 | **-7.157** | **8.23e-13** | *** |
| Season: spring (vs autumn) | -0.2154 | 0.1951 | ±0.3902 | -1.104 | 0.2696 |  |
| **Season: summer (vs autumn)** | **+2.0300** | 0.2217 | ±0.4433 | **+9.158** | **5.29e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9648** | 0.1970 | ±0.3941 | **-4.897** | **9.75e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0074 | ±0.0149 | **+2.714** | **0.0067** | ** |
| BMI (kg/m2) | +0.0192 | 0.0110 | ±0.0219 | +1.749 | 0.0803 | . |
| Hypertension | +0.1257 | 0.1567 | ±0.3134 | +0.802 | 0.4224 |  |
| High cholesterol | +0.1094 | 0.1548 | ±0.3096 | +0.707 | 0.4798 |  |
| Kidney disease | +0.1290 | 0.1971 | ±0.3942 | +0.655 | 0.5128 |  |
| Circulatory disease | +0.1376 | 0.2005 | ±0.4011 | +0.686 | 0.4926 |  |
| Avg. daily time 54-69 (%) | +0.0589 | 0.0824 | ±0.1648 | +0.715 | 0.4743 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.3099**, Adj R² = **0.2974**, F-statistic = **24.64** (p = **5.87e-53**), Residual SE = **1.997** on **768** df, AIC = **3320.3**, BIC = **3390.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9072** | 0.6123 | ±1.2247 | **+37.409** | **2.76e-306** | *** |
| Education: graduate level (vs college) | -0.2449 | 0.1553 | ±0.3105 | -1.577 | 0.1147 |  |
| Education: high school or below (vs college) | +0.1039 | 0.2282 | ±0.4565 | +0.455 | 0.6489 |  |
| Site: UCSD (vs UAB) | +0.0255 | 0.1834 | ±0.3667 | +0.139 | 0.8893 |  |
| **Site: UW (vs UAB)** | **-1.2496** | 0.1757 | ±0.3513 | **-7.113** | **1.13e-12** | *** |
| Season: spring (vs autumn) | -0.2119 | 0.1954 | ±0.3909 | -1.084 | 0.2782 |  |
| **Season: summer (vs autumn)** | **+2.0343** | 0.2218 | ±0.4437 | **+9.170** | **4.72e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9653** | 0.1970 | ±0.3940 | **-4.901** | **9.55e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0074 | ±0.0149 | **+2.703** | **0.0069** | ** |
| BMI (kg/m2) | +0.0195 | 0.0110 | ±0.0219 | +1.784 | 0.0744 | . |
| Hypertension | +0.1253 | 0.1564 | ±0.3129 | +0.801 | 0.4233 |  |
| High cholesterol | +0.1162 | 0.1547 | ±0.3094 | +0.751 | 0.4526 |  |
| Kidney disease | +0.1286 | 0.1973 | ±0.3946 | +0.652 | 0.5144 |  |
| Circulatory disease | +0.1402 | 0.2010 | ±0.4020 | +0.698 | 0.4855 |  |
| Time < 70 (%) | +0.0655 | 0.0692 | ±0.1383 | +0.947 | 0.3436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.3096**, Adj R² = **0.2970**, F-statistic = **24.60** (p = **7.09e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.7**, BIC = **3390.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9245** | 0.6113 | ±1.2225 | **+37.504** | **8.08e-308** | *** |
| Education: graduate level (vs college) | -0.2470 | 0.1552 | ±0.3103 | -1.592 | 0.1114 |  |
| Education: high school or below (vs college) | +0.1021 | 0.2283 | ±0.4566 | +0.447 | 0.6547 |  |
| Site: UCSD (vs UAB) | +0.0221 | 0.1833 | ±0.3667 | +0.121 | 0.9039 |  |
| **Site: UW (vs UAB)** | **-1.2515** | 0.1755 | ±0.3510 | **-7.131** | **9.95e-13** | *** |
| Season: spring (vs autumn) | -0.2122 | 0.1953 | ±0.3906 | -1.087 | 0.2772 |  |
| **Season: summer (vs autumn)** | **+2.0335** | 0.2219 | ±0.4438 | **+9.165** | **4.98e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9658** | 0.1970 | ±0.3941 | **-4.902** | **9.50e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0074 | ±0.0149 | **+2.703** | **0.0069** | ** |
| BMI (kg/m2) | +0.0193 | 0.0110 | ±0.0219 | +1.762 | 0.0781 | . |
| Hypertension | +0.1255 | 0.1565 | ±0.3129 | +0.802 | 0.4225 |  |
| High cholesterol | +0.1137 | 0.1547 | ±0.3093 | +0.735 | 0.4624 |  |
| Kidney disease | +0.1287 | 0.1971 | ±0.3942 | +0.653 | 0.5138 |  |
| Circulatory disease | +0.1389 | 0.2004 | ±0.4009 | +0.693 | 0.4882 |  |
| Avg. daily time < 70 (%) | +0.0549 | 0.0657 | ±0.1315 | +0.836 | 0.4033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.3091**, Adj R² = **0.2965**, F-statistic = **24.54** (p = **9.14e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.2**, BIC = **3391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2769** | 0.7624 | ±1.5248 | **+30.530** | **1.04e-204** | *** |
| Education: graduate level (vs college) | -0.2491 | 0.1554 | ±0.3108 | -1.603 | 0.1090 |  |
| Education: high school or below (vs college) | +0.0696 | 0.2308 | ±0.4616 | +0.301 | 0.7631 |  |
| Site: UCSD (vs UAB) | +0.0155 | 0.1844 | ±0.3689 | +0.084 | 0.9329 |  |
| **Site: UW (vs UAB)** | **-1.2601** | 0.1769 | ±0.3538 | **-7.123** | **1.05e-12** | *** |
| Season: spring (vs autumn) | -0.2250 | 0.1956 | ±0.3913 | -1.150 | 0.2501 |  |
| **Season: summer (vs autumn)** | **+2.0309** | 0.2225 | ±0.4451 | **+9.126** | **7.11e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9676** | 0.1965 | ±0.3930 | **-4.924** | **8.47e-07** | *** |
| **Age (years)** | **+0.0209** | 0.0075 | ±0.0149 | **+2.803** | **0.0051** | ** |
| BMI (kg/m2) | +0.0186 | 0.0110 | ±0.0221 | +1.680 | 0.0930 | . |
| Hypertension | +0.1255 | 0.1548 | ±0.3095 | +0.811 | 0.4175 |  |
| High cholesterol | +0.0955 | 0.1542 | ±0.3083 | +0.620 | 0.5354 |  |
| Kidney disease | +0.1257 | 0.1974 | ±0.3948 | +0.637 | 0.5244 |  |
| Circulatory disease | +0.1199 | 0.2012 | ±0.4024 | +0.596 | 0.5512 |  |
| Time 54-250, pooled (%) | -0.0036 | 0.0049 | ±0.0098 | -0.729 | 0.4662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.82e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.3**, BIC = **3391.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2459** | 0.7725 | ±1.5450 | **+30.092** | **6.20e-199** | *** |
| Education: graduate level (vs college) | -0.2504 | 0.1555 | ±0.3110 | -1.611 | 0.1072 |  |
| Education: high school or below (vs college) | +0.0719 | 0.2308 | ±0.4615 | +0.312 | 0.7553 |  |
| Site: UCSD (vs UAB) | +0.0143 | 0.1845 | ±0.3691 | +0.077 | 0.9384 |  |
| **Site: UW (vs UAB)** | **-1.2623** | 0.1769 | ±0.3537 | **-7.137** | **9.51e-13** | *** |
| Season: spring (vs autumn) | -0.2252 | 0.1956 | ±0.3912 | -1.152 | 0.2495 |  |
| **Season: summer (vs autumn)** | **+2.0289** | 0.2226 | ±0.4452 | **+9.114** | **7.92e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9679** | 0.1965 | ±0.3931 | **-4.924** | **8.46e-07** | *** |
| **Age (years)** | **+0.0208** | 0.0075 | ±0.0149 | **+2.792** | **0.0052** | ** |
| BMI (kg/m2) | +0.0186 | 0.0111 | ±0.0221 | +1.684 | 0.0922 | . |
| Hypertension | +0.1264 | 0.1548 | ±0.3096 | +0.817 | 0.4141 |  |
| High cholesterol | +0.0953 | 0.1542 | ±0.3084 | +0.618 | 0.5367 |  |
| Kidney disease | +0.1259 | 0.1974 | ±0.3948 | +0.638 | 0.5235 |  |
| Circulatory disease | +0.1205 | 0.2013 | ±0.4026 | +0.599 | 0.5493 |  |
| Avg. daily time 54-250 (%) | -0.0032 | 0.0050 | ±0.0100 | -0.635 | 0.5252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.02e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9593** | 0.6110 | ±1.2220 | **+37.576** | **5.37e-309** | *** |
| Education: graduate level (vs college) | -0.2603 | 0.1551 | ±0.3102 | -1.678 | 0.0933 | . |
| Education: high school or below (vs college) | +0.0769 | 0.2302 | ±0.4605 | +0.334 | 0.7384 |  |
| Site: UCSD (vs UAB) | +0.0107 | 0.1831 | ±0.3661 | +0.059 | 0.9532 |  |
| **Site: UW (vs UAB)** | **-1.2713** | 0.1749 | ±0.3499 | **-7.267** | **3.69e-13** | *** |
| Season: spring (vs autumn) | -0.2307 | 0.1957 | ±0.3914 | -1.179 | 0.2385 |  |
| **Season: summer (vs autumn)** | **+2.0148** | 0.2218 | ±0.4436 | **+9.083** | **1.05e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9725** | 0.1969 | ±0.3938 | **-4.939** | **7.85e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0075 | ±0.0150 | **+2.689** | **0.0072** | ** |
| BMI (kg/m2) | +0.0179 | 0.0111 | ±0.0221 | +1.617 | 0.1058 |  |
| Hypertension | +0.1317 | 0.1553 | ±0.3107 | +0.848 | 0.3966 |  |
| High cholesterol | +0.0906 | 0.1540 | ±0.3080 | +0.588 | 0.5565 |  |
| Kidney disease | +0.1238 | 0.1961 | ±0.3922 | +0.631 | 0.5280 |  |
| Circulatory disease | +0.1248 | 0.1996 | ±0.3993 | +0.625 | 0.5320 |  |
| Time 181-250, pooled (%) | +0.0033 | 0.0051 | ±0.0102 | +0.643 | 0.5202 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.3088**, Adj R² = **0.2962**, F-statistic = **24.51** (p = **1.07e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.5**, BIC = **3391.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9587** | 0.6109 | ±1.2217 | **+37.583** | **4.02e-309** | *** |
| Education: graduate level (vs college) | -0.2605 | 0.1551 | ±0.3102 | -1.680 | 0.0930 | . |
| Education: high school or below (vs college) | +0.0776 | 0.2305 | ±0.4610 | +0.337 | 0.7363 |  |
| Site: UCSD (vs UAB) | +0.0107 | 0.1831 | ±0.3661 | +0.058 | 0.9535 |  |
| **Site: UW (vs UAB)** | **-1.2710** | 0.1751 | ±0.3502 | **-7.258** | **3.93e-13** | *** |
| Season: spring (vs autumn) | -0.2302 | 0.1958 | ±0.3915 | -1.176 | 0.2396 |  |
| **Season: summer (vs autumn)** | **+2.0151** | 0.2218 | ±0.4436 | **+9.085** | **1.03e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9724** | 0.1970 | ±0.3941 | **-4.935** | **8.01e-07** | *** |
| **Age (years)** | **+0.0203** | 0.0075 | ±0.0150 | **+2.701** | **0.0069** | ** |
| BMI (kg/m2) | +0.0181 | 0.0111 | ±0.0221 | +1.635 | 0.1021 |  |
| Hypertension | +0.1315 | 0.1554 | ±0.3107 | +0.846 | 0.3975 |  |
| High cholesterol | +0.0907 | 0.1541 | ±0.3081 | +0.589 | 0.5562 |  |
| Kidney disease | +0.1248 | 0.1959 | ±0.3919 | +0.637 | 0.5243 |  |
| Circulatory disease | +0.1257 | 0.1997 | ±0.3993 | +0.629 | 0.5291 |  |
| Avg. daily time 181-250 (%) | +0.0028 | 0.0050 | ±0.0100 | +0.566 | 0.5717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.3092**, Adj R² = **0.2966**, F-statistic = **24.56** (p = **8.59e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.1**, BIC = **3391.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9302** | 0.6104 | ±1.2208 | **+37.567** | **7.57e-309** | *** |
| Education: graduate level (vs college) | -0.2531 | 0.1551 | ±0.3103 | -1.631 | 0.1028 |  |
| Education: high school or below (vs college) | +0.0649 | 0.2316 | ±0.4633 | +0.280 | 0.7794 |  |
| Site: UCSD (vs UAB) | +0.0176 | 0.1840 | ±0.3681 | +0.096 | 0.9239 |  |
| **Site: UW (vs UAB)** | **-1.2615** | 0.1764 | ±0.3529 | **-7.149** | **8.72e-13** | *** |
| Season: spring (vs autumn) | -0.2301 | 0.1956 | ±0.3912 | -1.176 | 0.2394 |  |
| **Season: summer (vs autumn)** | **+2.0243** | 0.2223 | ±0.4446 | **+9.106** | **8.55e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9714** | 0.1964 | ±0.3927 | **-4.947** | **7.54e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.760** | **0.0058** | ** |
| BMI (kg/m2) | +0.0177 | 0.0111 | ±0.0222 | +1.588 | 0.1123 |  |
| Hypertension | +0.1276 | 0.1549 | ±0.3098 | +0.824 | 0.4099 |  |
| High cholesterol | +0.0927 | 0.1540 | ±0.3080 | +0.602 | 0.5474 |  |
| Kidney disease | +0.1196 | 0.1968 | ±0.3936 | +0.608 | 0.5435 |  |
| Circulatory disease | +0.1189 | 0.2007 | ±0.4014 | +0.593 | 0.5534 |  |
| Time > 180 (%) | +0.0026 | 0.0032 | ±0.0063 | +0.823 | 0.4105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.3091**, Adj R² = **0.2965**, F-statistic = **24.54** (p = **9.29e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.2**, BIC = **3391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9361** | 0.6105 | ±1.2210 | **+37.570** | **6.66e-309** | *** |
| Education: graduate level (vs college) | -0.2543 | 0.1552 | ±0.3103 | -1.639 | 0.1013 |  |
| Education: high school or below (vs college) | +0.0671 | 0.2318 | ±0.4636 | +0.289 | 0.7723 |  |
| Site: UCSD (vs UAB) | +0.0168 | 0.1841 | ±0.3682 | +0.091 | 0.9274 |  |
| **Site: UW (vs UAB)** | **-1.2628** | 0.1765 | ±0.3530 | **-7.154** | **8.43e-13** | *** |
| Season: spring (vs autumn) | -0.2300 | 0.1956 | ±0.3912 | -1.176 | 0.2396 |  |
| **Season: summer (vs autumn)** | **+2.0230** | 0.2223 | ±0.4445 | **+9.102** | **8.91e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9717** | 0.1965 | ±0.3929 | **-4.946** | **7.59e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.756** | **0.0058** | ** |
| BMI (kg/m2) | +0.0178 | 0.0111 | ±0.0222 | +1.603 | 0.1090 |  |
| Hypertension | +0.1282 | 0.1549 | ±0.3099 | +0.827 | 0.4080 |  |
| High cholesterol | +0.0925 | 0.1541 | ±0.3081 | +0.601 | 0.5481 |  |
| Kidney disease | +0.1205 | 0.1967 | ±0.3934 | +0.613 | 0.5402 |  |
| Circulatory disease | +0.1201 | 0.2007 | ±0.4014 | +0.599 | 0.5495 |  |
| Avg. daily time > 180 (%) | +0.0023 | 0.0032 | ±0.0063 | +0.730 | 0.4655 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.3088**, Adj R² = **0.2962**, F-statistic = **24.51** (p = **1.07e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.5**, BIC = **3391.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9487** | 0.6105 | ±1.2209 | **+37.592** | **2.86e-309** | *** |
| Education: graduate level (vs college) | -0.2519 | 0.1557 | ±0.3114 | -1.618 | 0.1056 |  |
| Education: high school or below (vs college) | +0.0764 | 0.2307 | ±0.4614 | +0.331 | 0.7406 |  |
| Site: UCSD (vs UAB) | +0.0131 | 0.1842 | ±0.3684 | +0.071 | 0.9432 |  |
| **Site: UW (vs UAB)** | **-1.2686** | 0.1763 | ±0.3526 | **-7.195** | **6.25e-13** | *** |
| Season: spring (vs autumn) | -0.2294 | 0.1960 | ±0.3920 | -1.171 | 0.2418 |  |
| **Season: summer (vs autumn)** | **+2.0231** | 0.2223 | ±0.4447 | **+9.099** | **9.08e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9712** | 0.1966 | ±0.3932 | **-4.940** | **7.82e-07** | *** |
| **Age (years)** | **+0.0207** | 0.0075 | ±0.0149 | **+2.779** | **0.0055** | ** |
| BMI (kg/m2) | +0.0180 | 0.0113 | ±0.0226 | +1.591 | 0.1116 |  |
| Hypertension | +0.1300 | 0.1552 | ±0.3104 | +0.837 | 0.4024 |  |
| High cholesterol | +0.0936 | 0.1542 | ±0.3083 | +0.607 | 0.5436 |  |
| Kidney disease | +0.1283 | 0.1964 | ±0.3929 | +0.653 | 0.5137 |  |
| Circulatory disease | +0.1232 | 0.2008 | ±0.4015 | +0.613 | 0.5396 |  |
| Nocturnal time > 180 (%) | +0.0015 | 0.0030 | ±0.0059 | +0.518 | 0.6045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.57e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.3**, BIC = **3391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9226** | 0.6119 | ±1.2239 | **+37.459** | **4.34e-307** | *** |
| Education: graduate level (vs college) | -0.2501 | 0.1554 | ±0.3109 | -1.609 | 0.1076 |  |
| Education: high school or below (vs college) | +0.0708 | 0.2308 | ±0.4617 | +0.307 | 0.7592 |  |
| Site: UCSD (vs UAB) | +0.0143 | 0.1845 | ±0.3689 | +0.077 | 0.9383 |  |
| **Site: UW (vs UAB)** | **-1.2616** | 0.1769 | ±0.3538 | **-7.133** | **9.83e-13** | *** |
| Season: spring (vs autumn) | -0.2251 | 0.1956 | ±0.3912 | -1.151 | 0.2498 |  |
| **Season: summer (vs autumn)** | **+2.0298** | 0.2225 | ±0.4451 | **+9.121** | **7.45e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9675** | 0.1965 | ±0.3931 | **-4.922** | **8.55e-07** | *** |
| **Age (years)** | **+0.0209** | 0.0075 | ±0.0149 | **+2.800** | **0.0051** | ** |
| BMI (kg/m2) | +0.0186 | 0.0110 | ±0.0221 | +1.683 | 0.0923 | . |
| Hypertension | +0.1259 | 0.1547 | ±0.3095 | +0.814 | 0.4159 |  |
| High cholesterol | +0.0950 | 0.1542 | ±0.3084 | +0.616 | 0.5377 |  |
| Kidney disease | +0.1263 | 0.1974 | ±0.3947 | +0.640 | 0.5221 |  |
| Circulatory disease | +0.1204 | 0.2012 | ±0.4024 | +0.599 | 0.5495 |  |
| Time > 250 (%) | +0.0033 | 0.0049 | ±0.0098 | +0.673 | 0.5008 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.01e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9298** | 0.6116 | ±1.2233 | **+37.489** | **1.40e-307** | *** |
| Education: graduate level (vs college) | -0.2510 | 0.1555 | ±0.3110 | -1.615 | 0.1064 |  |
| Education: high school or below (vs college) | +0.0726 | 0.2308 | ±0.4616 | +0.314 | 0.7532 |  |
| Site: UCSD (vs UAB) | +0.0134 | 0.1845 | ±0.3690 | +0.073 | 0.9419 |  |
| **Site: UW (vs UAB)** | **-1.2633** | 0.1768 | ±0.3536 | **-7.145** | **8.98e-13** | *** |
| Season: spring (vs autumn) | -0.2254 | 0.1956 | ±0.3911 | -1.153 | 0.2491 |  |
| **Season: summer (vs autumn)** | **+2.0281** | 0.2226 | ±0.4452 | **+9.112** | **8.10e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9678** | 0.1966 | ±0.3931 | **-4.924** | **8.50e-07** | *** |
| **Age (years)** | **+0.0208** | 0.0075 | ±0.0149 | **+2.791** | **0.0053** | ** |
| BMI (kg/m2) | +0.0187 | 0.0111 | ±0.0221 | +1.687 | 0.0917 | . |
| Hypertension | +0.1267 | 0.1548 | ±0.3096 | +0.818 | 0.4131 |  |
| High cholesterol | +0.0949 | 0.1542 | ±0.3084 | +0.615 | 0.5385 |  |
| Kidney disease | +0.1264 | 0.1974 | ±0.3947 | +0.641 | 0.5218 |  |
| Circulatory disease | +0.1209 | 0.2013 | ±0.4026 | +0.601 | 0.5482 |  |
| Avg. daily time > 250 (%) | +0.0030 | 0.0050 | ±0.0100 | +0.602 | 0.5471 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2301**, F-statistic = **18.98** (p = **8.92e-39**), Residual SE = **6.017** on **769** df, AIC = **5046.3**, BIC = **5111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4585** | 1.8993 | ±3.7986 | **+26.040** | **1.74e-149** | *** |
| Education: graduate level (vs college) | +0.0099 | 0.4910 | ±0.9820 | +0.020 | 0.9839 |  |
| Education: high school or below (vs college) | +0.4064 | 0.6358 | ±1.2716 | +0.639 | 0.5227 |  |
| **Site: UCSD (vs UAB)** | **+3.0471** | 0.5694 | ±1.1389 | **+5.351** | **8.75e-08** | *** |
| Site: UW (vs UAB) | -0.8284 | 0.5206 | ±1.0411 | -1.591 | 0.1115 |  |
| **Season: spring (vs autumn)** | **-2.1310** | 0.6165 | ±1.2330 | **-3.457** | **5.47e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8428** | 0.6165 | ±1.2330 | **+2.989** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6420** | 0.6626 | ±1.3252 | **-8.515** | **1.66e-17** | *** |
| **Age (years)** | **-0.0425** | 0.0216 | ±0.0433 | **-1.962** | **0.0497** | * |
| BMI (kg/m2) | -0.0262 | 0.0330 | ±0.0660 | -0.796 | 0.4262 |  |
| Hypertension | -0.7613 | 0.4995 | ±0.9989 | -1.524 | 0.1275 |  |
| High cholesterol | -0.5099 | 0.4593 | ±0.9186 | -1.110 | 0.2669 |  |
| Kidney disease | +1.1047 | 0.6056 | ±1.2113 | +1.824 | 0.0681 | . |
| Circulatory disease | +0.1813 | 0.5828 | ±1.1656 | +0.311 | 0.7557 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.2439**, Adj R² = **0.2301**, F-statistic = **17.69** (p = **2.51e-38**), Residual SE = **6.017** on **768** df, AIC = **5047.3**, BIC = **5117.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4693** | 2.1405 | ±4.2809 | **+22.644** | **1.59e-113** | *** |
| Education: graduate level (vs college) | +0.0420 | 0.4911 | ±0.9823 | +0.086 | 0.9318 |  |
| Education: high school or below (vs college) | +0.3156 | 0.6363 | ±1.2725 | +0.496 | 0.6199 |  |
| **Site: UCSD (vs UAB)** | **+3.0784** | 0.5725 | ±1.1450 | **+5.377** | **7.57e-08** | *** |
| Site: UW (vs UAB) | -0.7851 | 0.5241 | ±1.0481 | -1.498 | 0.1341 |  |
| **Season: spring (vs autumn)** | **-2.1137** | 0.6173 | ±1.2346 | **-3.424** | **6.17e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8657** | 0.6168 | ±1.2336 | **+3.025** | **0.0025** | ** |
| **Season: winter (vs autumn)** | **-5.6399** | 0.6632 | ±1.3264 | **-8.504** | **1.84e-17** | *** |
| Age (years) | -0.0421 | 0.0217 | ±0.0433 | -1.943 | 0.0520 | . |
| BMI (kg/m2) | -0.0314 | 0.0334 | ±0.0668 | -0.940 | 0.3472 |  |
| Hypertension | -0.7840 | 0.4984 | ±0.9969 | -1.573 | 0.1157 |  |
| High cholesterol | -0.5284 | 0.4611 | ±0.9223 | -1.146 | 0.2519 |  |
| Kidney disease | +1.0983 | 0.6044 | ±1.2087 | +1.817 | 0.0692 | . |
| Circulatory disease | +0.1459 | 0.5845 | ±1.1691 | +0.250 | 0.8029 |  |
| HbA1c (%) | +0.1649 | 0.1672 | ±0.3343 | +0.986 | 0.3241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.2449**, Adj R² = **0.2311**, F-statistic = **17.79** (p = **1.51e-38**), Residual SE = **6.013** on **768** df, AIC = **5046.2**, BIC = **5116.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3164** | 2.0322 | ±4.0643 | **+23.776** | **5.92e-125** | *** |
| Education: graduate level (vs college) | +0.0393 | 0.4908 | ±0.9817 | +0.080 | 0.9362 |  |
| Education: high school or below (vs college) | +0.2855 | 0.6371 | ±1.2742 | +0.448 | 0.6541 |  |
| **Site: UCSD (vs UAB)** | **+3.1076** | 0.5748 | ±1.1497 | **+5.406** | **6.45e-08** | *** |
| Site: UW (vs UAB) | -0.7686 | 0.5246 | ±1.0492 | -1.465 | 0.1429 |  |
| **Season: spring (vs autumn)** | **-2.1586** | 0.6159 | ±1.2318 | **-3.505** | **4.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8838** | 0.6161 | ±1.2322 | **+3.058** | **0.0022** | ** |
| **Season: winter (vs autumn)** | **-5.6491** | 0.6622 | ±1.3244 | **-8.531** | **1.45e-17** | *** |
| Age (years) | -0.0416 | 0.0216 | ±0.0433 | -1.922 | 0.0546 | . |
| BMI (kg/m2) | -0.0328 | 0.0335 | ±0.0669 | -0.982 | 0.3263 |  |
| Hypertension | -0.7847 | 0.4991 | ±0.9983 | -1.572 | 0.1159 |  |
| High cholesterol | -0.5213 | 0.4599 | ±0.9198 | -1.134 | 0.2570 |  |
| Kidney disease | +1.0553 | 0.6037 | ±1.2073 | +1.748 | 0.0804 | . |
| Circulatory disease | +0.1260 | 0.5861 | ±1.1723 | +0.215 | 0.8298 |  |
| Mean glucose (mg/dL) | +0.0080 | 0.0058 | ±0.0115 | +1.388 | 0.1651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.2449**, Adj R² = **0.2311**, F-statistic = **17.79** (p = **1.51e-38**), Residual SE = **6.013** on **768** df, AIC = **5046.2**, BIC = **5116.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2114** | 2.4356 | ±4.8711 | **+19.384** | **1.05e-83** | *** |
| Education: graduate level (vs college) | +0.0393 | 0.4908 | ±0.9817 | +0.080 | 0.9362 |  |
| Education: high school or below (vs college) | +0.2855 | 0.6371 | ±1.2742 | +0.448 | 0.6541 |  |
| **Site: UCSD (vs UAB)** | **+3.1076** | 0.5748 | ±1.1497 | **+5.406** | **6.45e-08** | *** |
| Site: UW (vs UAB) | -0.7686 | 0.5246 | ±1.0492 | -1.465 | 0.1429 |  |
| **Season: spring (vs autumn)** | **-2.1586** | 0.6159 | ±1.2318 | **-3.505** | **4.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8838** | 0.6161 | ±1.2322 | **+3.058** | **0.0022** | ** |
| **Season: winter (vs autumn)** | **-5.6491** | 0.6622 | ±1.3244 | **-8.531** | **1.45e-17** | *** |
| Age (years) | -0.0416 | 0.0216 | ±0.0433 | -1.922 | 0.0546 | . |
| BMI (kg/m2) | -0.0328 | 0.0335 | ±0.0669 | -0.982 | 0.3263 |  |
| Hypertension | -0.7847 | 0.4991 | ±0.9983 | -1.572 | 0.1159 |  |
| High cholesterol | -0.5213 | 0.4599 | ±0.9198 | -1.134 | 0.2570 |  |
| Kidney disease | +1.0553 | 0.6037 | ±1.2073 | +1.748 | 0.0804 | . |
| Circulatory disease | +0.1260 | 0.5861 | ±1.1723 | +0.215 | 0.8298 |  |
| GMI (%) | +0.3339 | 0.2405 | ±0.4810 | +1.388 | 0.1651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.2441**, Adj R² = **0.2303**, F-statistic = **17.72** (p = **2.21e-38**), Residual SE = **6.016** on **768** df, AIC = **5047.1**, BIC = **5117.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6438** | 2.0036 | ±4.0072 | **+24.278** | **3.35e-130** | *** |
| Education: graduate level (vs college) | +0.0424 | 0.4916 | ±0.9833 | +0.086 | 0.9312 |  |
| Education: high school or below (vs college) | +0.3227 | 0.6377 | ±1.2753 | +0.506 | 0.6129 |  |
| **Site: UCSD (vs UAB)** | **+3.0912** | 0.5744 | ±1.1488 | **+5.381** | **7.39e-08** | *** |
| Site: UW (vs UAB) | -0.7972 | 0.5230 | ±1.0460 | -1.524 | 0.1274 |  |
| **Season: spring (vs autumn)** | **-2.1634** | 0.6165 | ±1.2330 | **-3.509** | **4.50e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8762** | 0.6164 | ±1.2327 | **+3.044** | **0.0023** | ** |
| **Season: winter (vs autumn)** | **-5.6542** | 0.6630 | ±1.3261 | **-8.528** | **1.49e-17** | *** |
| Age (years) | -0.0409 | 0.0216 | ±0.0433 | -1.889 | 0.0589 | . |
| BMI (kg/m2) | -0.0327 | 0.0337 | ±0.0673 | -0.971 | 0.3317 |  |
| Hypertension | -0.7737 | 0.4992 | ±0.9984 | -1.550 | 0.1212 |  |
| High cholesterol | -0.5170 | 0.4600 | ±0.9200 | -1.124 | 0.2611 |  |
| Kidney disease | +1.0912 | 0.6046 | ±1.2092 | +1.805 | 0.0711 | . |
| Circulatory disease | +0.1420 | 0.5859 | ±1.1717 | +0.242 | 0.8084 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0059 | 0.0053 | ±0.0106 | +1.115 | 0.2648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.2431**, Adj R² = **0.2293**, F-statistic = **17.62** (p = **3.54e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.1**, BIC = **5118.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1710** | 2.0304 | ±4.0607 | **+24.218** | **1.44e-129** | *** |
| Education: graduate level (vs college) | +0.0260 | 0.4956 | ±0.9911 | +0.053 | 0.9581 |  |
| Education: high school or below (vs college) | +0.3734 | 0.6313 | ±1.2627 | +0.591 | 0.5543 |  |
| **Site: UCSD (vs UAB)** | **+3.0680** | 0.5750 | ±1.1500 | **+5.336** | **9.51e-08** | *** |
| Site: UW (vs UAB) | -0.7940 | 0.5300 | ±1.0601 | -1.498 | 0.1341 |  |
| **Season: spring (vs autumn)** | **-2.1416** | 0.6160 | ±1.2320 | **-3.477** | **5.08e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8536** | 0.6183 | ±1.2365 | **+2.998** | **0.0027** | ** |
| **Season: winter (vs autumn)** | **-5.6452** | 0.6623 | ±1.3246 | **-8.524** | **1.55e-17** | *** |
| **Age (years)** | **-0.0426** | 0.0217 | ±0.0434 | **-1.966** | **0.0493** | * |
| BMI (kg/m2) | -0.0283 | 0.0332 | ±0.0664 | -0.852 | 0.3944 |  |
| Hypertension | -0.7753 | 0.4984 | ±0.9969 | -1.556 | 0.1198 |  |
| High cholesterol | -0.5045 | 0.4594 | ±0.9189 | -1.098 | 0.2722 |  |
| Kidney disease | +1.0466 | 0.6141 | ±1.2282 | +1.704 | 0.0883 | . |
| Circulatory disease | +0.1653 | 0.5860 | ±1.1719 | +0.282 | 0.7779 |  |
| Glucose SD, pooled (mg/dL) | +0.0093 | 0.0186 | ±0.0372 | +0.502 | 0.6158 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **3.00e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9920** | 2.0270 | ±4.0541 | **+24.169** | **4.69e-129** | *** |
| Education: graduate level (vs college) | +0.0296 | 0.4949 | ±0.9897 | +0.060 | 0.9524 |  |
| Education: high school or below (vs college) | +0.3497 | 0.6321 | ±1.2641 | +0.553 | 0.5801 |  |
| **Site: UCSD (vs UAB)** | **+3.0803** | 0.5754 | ±1.1509 | **+5.353** | **8.66e-08** | *** |
| Site: UW (vs UAB) | -0.7792 | 0.5293 | ±1.0586 | -1.472 | 0.1410 |  |
| **Season: spring (vs autumn)** | **-2.1468** | 0.6162 | ±1.2324 | **-3.484** | **4.94e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8615** | 0.6187 | ±1.2375 | **+3.009** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6404** | 0.6623 | ±1.3246 | **-8.516** | **1.65e-17** | *** |
| **Age (years)** | **-0.0429** | 0.0217 | ±0.0434 | **-1.977** | **0.0480** | * |
| BMI (kg/m2) | -0.0287 | 0.0332 | ±0.0665 | -0.863 | 0.3884 |  |
| Hypertension | -0.7803 | 0.4981 | ±0.9961 | -1.567 | 0.1172 |  |
| High cholesterol | -0.5025 | 0.4594 | ±0.9188 | -1.094 | 0.2741 |  |
| Kidney disease | +1.0086 | 0.6147 | ±1.2294 | +1.641 | 0.1008 |  |
| Circulatory disease | +0.1603 | 0.5863 | ±1.1725 | +0.273 | 0.7845 |  |
| Avg. daily SD (mg/dL) | +0.0165 | 0.0211 | ±0.0423 | +0.780 | 0.4351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.2434**, Adj R² = **0.2296**, F-statistic = **17.64** (p = **3.18e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.8**, BIC = **5117.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0631** | 2.1811 | ±4.3623 | **+22.953** | **1.38e-116** | *** |
| Education: graduate level (vs college) | -0.0074 | 0.4955 | ±0.9910 | -0.015 | 0.9881 |  |
| Education: high school or below (vs college) | +0.4117 | 0.6348 | ±1.2695 | +0.649 | 0.5167 |  |
| **Site: UCSD (vs UAB)** | **+3.0299** | 0.5714 | ±1.1428 | **+5.302** | **1.14e-07** | *** |
| Site: UW (vs UAB) | -0.8669 | 0.5253 | ±1.0506 | -1.650 | 0.0989 | . |
| **Season: spring (vs autumn)** | **-2.1300** | 0.6171 | ±1.2342 | **-3.452** | **5.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8410** | 0.6165 | ±1.2330 | **+2.986** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6414** | 0.6641 | ±1.3283 | **-8.494** | **1.99e-17** | *** |
| Age (years) | -0.0417 | 0.0216 | ±0.0432 | -1.930 | 0.0537 | . |
| BMI (kg/m2) | -0.0256 | 0.0329 | ±0.0658 | -0.778 | 0.4365 |  |
| Hypertension | -0.7446 | 0.4984 | ±0.9968 | -1.494 | 0.1352 |  |
| High cholesterol | -0.5292 | 0.4592 | ±0.9184 | -1.153 | 0.2491 |  |
| Kidney disease | +1.1861 | 0.6167 | ±1.2333 | +1.923 | 0.0544 | . |
| Circulatory disease | +0.1846 | 0.5827 | ±1.1653 | +0.317 | 0.7513 |  |
| CV (%) | -0.0278 | 0.0410 | ±0.0819 | -0.678 | 0.4975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.2436**, Adj R² = **0.2298**, F-statistic = **17.67** (p = **2.81e-38**), Residual SE = **6.018** on **768** df, AIC = **5047.6**, BIC = **5117.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5594** | 2.0782 | ±4.1563 | **+23.367** | **9.36e-121** | *** |
| Education: graduate level (vs college) | -0.0069 | 0.4947 | ±0.9894 | -0.014 | 0.9889 |  |
| Education: high school or below (vs college) | +0.4117 | 0.6347 | ±1.2695 | +0.649 | 0.5166 |  |
| **Site: UCSD (vs UAB)** | **+3.0368** | 0.5703 | ±1.1406 | **+5.325** | **1.01e-07** | *** |
| Site: UW (vs UAB) | -0.8684 | 0.5238 | ±1.0476 | -1.658 | 0.0973 | . |
| **Season: spring (vs autumn)** | **-2.1224** | 0.6166 | ±1.2332 | **-3.442** | **5.77e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8611** | 0.6151 | ±1.2302 | **+3.026** | **0.0025** | ** |
| **Season: winter (vs autumn)** | **-5.6300** | 0.6633 | ±1.3266 | **-8.487** | **2.11e-17** | *** |
| Age (years) | -0.0418 | 0.0216 | ±0.0433 | -1.930 | 0.0536 | . |
| BMI (kg/m2) | -0.0259 | 0.0329 | ±0.0658 | -0.789 | 0.4302 |  |
| Hypertension | -0.7412 | 0.4984 | ±0.9967 | -1.487 | 0.1370 |  |
| High cholesterol | -0.5225 | 0.4589 | ±0.9177 | -1.139 | 0.2548 |  |
| Kidney disease | +1.1890 | 0.6107 | ±1.2215 | +1.947 | 0.0516 | . |
| Circulatory disease | +0.1934 | 0.5826 | ±1.1652 | +0.332 | 0.7399 |  |
| Mean / SD ratio | +0.1895 | 0.2212 | ±0.4424 | +0.857 | 0.3917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.2430**, Adj R² = **0.2292**, F-statistic = **17.61** (p = **3.82e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.2**, BIC = **5118.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1703** | 2.0741 | ±4.1482 | **+23.707** | **3.09e-124** | *** |
| Education: graduate level (vs college) | +0.0057 | 0.4943 | ±0.9886 | +0.011 | 0.9908 |  |
| Education: high school or below (vs college) | +0.4092 | 0.6357 | ±1.2714 | +0.644 | 0.5198 |  |
| **Site: UCSD (vs UAB)** | **+3.0443** | 0.5702 | ±1.1404 | **+5.339** | **9.35e-08** | *** |
| Site: UW (vs UAB) | -0.8404 | 0.5236 | ±1.0472 | -1.605 | 0.1085 |  |
| **Season: spring (vs autumn)** | **-2.1325** | 0.6177 | ±1.2354 | **-3.452** | **5.56e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8465** | 0.6160 | ±1.2321 | **+2.997** | **0.0027** | ** |
| **Season: winter (vs autumn)** | **-5.6415** | 0.6637 | ±1.3274 | **-8.500** | **1.90e-17** | *** |
| Age (years) | -0.0421 | 0.0217 | ±0.0434 | -1.941 | 0.0523 | . |
| BMI (kg/m2) | -0.0264 | 0.0330 | ±0.0660 | -0.801 | 0.4234 |  |
| Hypertension | -0.7549 | 0.4983 | ±0.9966 | -1.515 | 0.1298 |  |
| High cholesterol | -0.5152 | 0.4588 | ±0.9177 | -1.123 | 0.2615 |  |
| Kidney disease | +1.1322 | 0.6099 | ±1.2199 | +1.856 | 0.0634 | . |
| Circulatory disease | +0.1824 | 0.5832 | ±1.1664 | +0.313 | 0.7545 |  |
| Avg. daily mean/SD | +0.0523 | 0.1812 | ±0.3624 | +0.289 | 0.7727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.2432**, Adj R² = **0.2294**, F-statistic = **17.63** (p = **3.44e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.0**, BIC = **5118.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7950** | 2.2118 | ±4.4237 | **+22.061** | **7.50e-108** | *** |
| Education: graduate level (vs college) | +0.0334 | 0.4974 | ±0.9948 | +0.067 | 0.9464 |  |
| Education: high school or below (vs college) | +0.3943 | 0.6354 | ±1.2708 | +0.621 | 0.5349 |  |
| **Site: UCSD (vs UAB)** | **+3.0728** | 0.5763 | ±1.1525 | **+5.332** | **9.70e-08** | *** |
| Site: UW (vs UAB) | -0.7768 | 0.5330 | ±1.0660 | -1.457 | 0.1450 |  |
| **Season: spring (vs autumn)** | **-2.1349** | 0.6174 | ±1.2348 | **-3.458** | **5.44e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8707** | 0.6182 | ±1.2364 | **+3.026** | **0.0025** | ** |
| **Season: winter (vs autumn)** | **-5.6320** | 0.6639 | ±1.3279 | **-8.483** | **2.20e-17** | *** |
| Age (years) | -0.0415 | 0.0216 | ±0.0433 | -1.917 | 0.0552 | . |
| BMI (kg/m2) | -0.0273 | 0.0331 | ±0.0661 | -0.824 | 0.4098 |  |
| Hypertension | -0.7535 | 0.5007 | ±1.0014 | -1.505 | 0.1324 |  |
| High cholesterol | -0.4906 | 0.4601 | ±0.9202 | -1.066 | 0.2863 |  |
| Kidney disease | +1.0766 | 0.6076 | ±1.2152 | +1.772 | 0.0764 | . |
| Circulatory disease | +0.1747 | 0.5830 | ±1.1659 | +0.300 | 0.7644 |  |
| MAG (mg/dL/h) | +0.0128 | 0.0222 | ±0.0444 | +0.576 | 0.5645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.2434**, Adj R² = **0.2296**, F-statistic = **17.65** (p = **3.08e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.8**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7799** | 2.1539 | ±4.3078 | **+22.647** | **1.48e-113** | *** |
| Education: graduate level (vs college) | +0.0284 | 0.4955 | ±0.9909 | +0.057 | 0.9542 |  |
| Education: high school or below (vs college) | +0.3541 | 0.6326 | ±1.2653 | +0.560 | 0.5757 |  |
| **Site: UCSD (vs UAB)** | **+3.0843** | 0.5768 | ±1.1537 | **+5.347** | **8.94e-08** | *** |
| Site: UW (vs UAB) | -0.7781 | 0.5310 | ±1.0620 | -1.465 | 0.1428 |  |
| **Season: spring (vs autumn)** | **-2.1523** | 0.6153 | ±1.2306 | **-3.498** | **4.69e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8504** | 0.6172 | ±1.2345 | **+2.998** | **0.0027** | ** |
| **Season: winter (vs autumn)** | **-5.6448** | 0.6619 | ±1.3237 | **-8.529** | **1.48e-17** | *** |
| Age (years) | -0.0422 | 0.0217 | ±0.0434 | -1.946 | 0.0517 | . |
| BMI (kg/m2) | -0.0279 | 0.0331 | ±0.0663 | -0.840 | 0.4007 |  |
| Hypertension | -0.7682 | 0.4988 | ±0.9976 | -1.540 | 0.1235 |  |
| High cholesterol | -0.5000 | 0.4594 | ±0.9187 | -1.089 | 0.2764 |  |
| Kidney disease | +1.0155 | 0.6134 | ±1.2268 | +1.656 | 0.0978 | . |
| Circulatory disease | +0.1597 | 0.5852 | ±1.1704 | +0.273 | 0.7849 |  |
| Avg. daily range (mg/dL) | +0.0046 | 0.0061 | ±0.0122 | +0.760 | 0.4470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.97e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4749** | 1.9356 | ±3.8711 | **+25.561** | **4.13e-144** | *** |
| Education: graduate level (vs college) | +0.0069 | 0.4956 | ±0.9912 | +0.014 | 0.9889 |  |
| Education: high school or below (vs college) | +0.4081 | 0.6350 | ±1.2700 | +0.643 | 0.5204 |  |
| **Site: UCSD (vs UAB)** | **+3.0454** | 0.5722 | ±1.1443 | **+5.323** | **1.02e-07** | *** |
| Site: UW (vs UAB) | -0.8317 | 0.5249 | ±1.0498 | -1.585 | 0.1131 |  |
| **Season: spring (vs autumn)** | **-2.1300** | 0.6167 | ±1.2334 | **-3.454** | **5.53e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8427** | 0.6172 | ±1.2343 | **+2.986** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6403** | 0.6648 | ±1.3296 | **-8.484** | **2.18e-17** | *** |
| Age (years) | -0.0425 | 0.0217 | ±0.0434 | -1.960 | 0.0500 | . |
| BMI (kg/m2) | -0.0260 | 0.0330 | ±0.0661 | -0.785 | 0.4323 |  |
| Hypertension | -0.7592 | 0.5012 | ±1.0023 | -1.515 | 0.1298 |  |
| High cholesterol | -0.5102 | 0.4597 | ±0.9195 | -1.110 | 0.2671 |  |
| Kidney disease | +1.1077 | 0.6071 | ±1.2142 | +1.825 | 0.0681 | . |
| Circulatory disease | +0.1841 | 0.5873 | ±1.1745 | +0.314 | 0.7538 |  |
| SD of daily means (mg/dL) | -0.0017 | 0.0273 | ±0.0547 | -0.062 | 0.9509 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.99e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0676** | 2.1045 | ±4.2091 | **+23.790** | **4.20e-125** | *** |
| Education: graduate level (vs college) | +0.0264 | 0.4917 | ±0.9834 | +0.054 | 0.9571 |  |
| Education: high school or below (vs college) | +0.3431 | 0.6360 | ±1.2720 | +0.539 | 0.5895 |  |
| **Site: UCSD (vs UAB)** | **+3.0861** | 0.5761 | ±1.1522 | **+5.357** | **8.47e-08** | *** |
| Site: UW (vs UAB) | -0.7895 | 0.5258 | ±1.0517 | -1.501 | 0.1333 |  |
| **Season: spring (vs autumn)** | **-2.1458** | 0.6161 | ±1.2322 | **-3.483** | **4.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8594** | 0.6170 | ±1.2340 | **+3.014** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6519** | 0.6632 | ±1.3265 | **-8.522** | **1.57e-17** | *** |
| Age (years) | -0.0423 | 0.0217 | ±0.0433 | -1.955 | 0.0506 | . |
| BMI (kg/m2) | -0.0305 | 0.0337 | ±0.0675 | -0.903 | 0.3664 |  |
| Hypertension | -0.7701 | 0.4997 | ±0.9995 | -1.541 | 0.1233 |  |
| High cholesterol | -0.5083 | 0.4597 | ±0.9195 | -1.106 | 0.2689 |  |
| Kidney disease | +1.0647 | 0.6067 | ±1.2133 | +1.755 | 0.0793 | . |
| Circulatory disease | +0.1559 | 0.5855 | ±1.1710 | +0.266 | 0.7901 |  |
| Time in range 70-180, pooled (%) | -0.0069 | 0.0095 | ±0.0190 | -0.730 | 0.4652 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.2436**, Adj R² = **0.2298**, F-statistic = **17.66** (p = **2.89e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.6**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1100** | 2.1073 | ±4.2146 | **+23.779** | **5.44e-125** | *** |
| Education: graduate level (vs college) | +0.0257 | 0.4917 | ±0.9833 | +0.052 | 0.9583 |  |
| Education: high school or below (vs college) | +0.3378 | 0.6359 | ±1.2719 | +0.531 | 0.5953 |  |
| **Site: UCSD (vs UAB)** | **+3.0907** | 0.5766 | ±1.1532 | **+5.360** | **8.32e-08** | *** |
| Site: UW (vs UAB) | -0.7864 | 0.5260 | ±1.0519 | -1.495 | 0.1349 |  |
| **Season: spring (vs autumn)** | **-2.1483** | 0.6161 | ±1.2322 | **-3.487** | **4.88e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8583** | 0.6169 | ±1.2337 | **+3.013** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6548** | 0.6633 | ±1.3266 | **-8.525** | **1.53e-17** | *** |
| Age (years) | -0.0424 | 0.0217 | ±0.0433 | -1.957 | 0.0504 | . |
| BMI (kg/m2) | -0.0308 | 0.0337 | ±0.0675 | -0.913 | 0.3614 |  |
| Hypertension | -0.7701 | 0.4997 | ±0.9993 | -1.541 | 0.1233 |  |
| High cholesterol | -0.5086 | 0.4598 | ±0.9195 | -1.106 | 0.2687 |  |
| Kidney disease | +1.0598 | 0.6067 | ±1.2133 | +1.747 | 0.0806 | . |
| Circulatory disease | +0.1547 | 0.5857 | ±1.1713 | +0.264 | 0.7917 |  |
| Avg. daily time in range 70-180 (%) | -0.0073 | 0.0094 | ±0.0188 | -0.776 | 0.4378 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.97e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4472** | 1.9138 | ±3.8277 | **+25.837** | **3.44e-147** | *** |
| Education: graduate level (vs college) | +0.0108 | 0.4922 | ±0.9845 | +0.022 | 0.9826 |  |
| Education: high school or below (vs college) | +0.4081 | 0.6378 | ±1.2757 | +0.640 | 0.5223 |  |
| **Site: UCSD (vs UAB)** | **+3.0486** | 0.5708 | ±1.1417 | **+5.341** | **9.27e-08** | *** |
| Site: UW (vs UAB) | -0.8268 | 0.5205 | ±1.0411 | -1.588 | 0.1122 |  |
| **Season: spring (vs autumn)** | **-2.1307** | 0.6177 | ±1.2355 | **-3.449** | **5.62e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8440** | 0.6176 | ±1.2351 | **+2.986** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6400** | 0.6637 | ±1.3273 | **-8.498** | **1.92e-17** | *** |
| Age (years) | -0.0424 | 0.0217 | ±0.0433 | -1.959 | 0.0502 | . |
| BMI (kg/m2) | -0.0263 | 0.0330 | ±0.0660 | -0.796 | 0.4262 |  |
| Hypertension | -0.7628 | 0.5023 | ±1.0046 | -1.519 | 0.1289 |  |
| High cholesterol | -0.5077 | 0.4607 | ±0.9215 | -1.102 | 0.2705 |  |
| Kidney disease | +1.1040 | 0.6062 | ±1.2124 | +1.821 | 0.0686 | . |
| Circulatory disease | +0.1799 | 0.5841 | ±1.1683 | +0.308 | 0.7580 |  |
| Any reading < 54 during wear (0/1) | +0.0288 | 0.5209 | ±1.0418 | +0.055 | 0.9560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.2446**, Adj R² = **0.2309**, F-statistic = **17.77** (p = **1.73e-38**), Residual SE = **6.014** on **768** df, AIC = **5046.5**, BIC = **5116.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6056** | 1.8997 | ±3.7994 | **+26.112** | **2.66e-150** | *** |
| Education: graduate level (vs college) | -0.0262 | 0.4916 | ±0.9831 | -0.053 | 0.9576 |  |
| Education: high school or below (vs college) | +0.3606 | 0.6365 | ±1.2729 | +0.567 | 0.5710 |  |
| **Site: UCSD (vs UAB)** | **+2.9958** | 0.5698 | ±1.1396 | **+5.258** | **1.46e-07** | *** |
| Site: UW (vs UAB) | -0.8934 | 0.5211 | ±1.0423 | -1.714 | 0.0865 | . |
| **Season: spring (vs autumn)** | **-2.1498** | 0.6165 | ±1.2330 | **-3.487** | **4.88e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8174** | 0.6159 | ±1.2317 | **+2.951** | **0.0032** | ** |
| **Season: winter (vs autumn)** | **-5.6218** | 0.6629 | ±1.3258 | **-8.481** | **2.24e-17** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0433 | -1.916 | 0.0554 | . |
| BMI (kg/m2) | -0.0285 | 0.0330 | ±0.0659 | -0.866 | 0.3865 |  |
| Hypertension | -0.7592 | 0.4993 | ±0.9987 | -1.520 | 0.1284 |  |
| High cholesterol | -0.5599 | 0.4602 | ±0.9203 | -1.217 | 0.2237 |  |
| Kidney disease | +1.1000 | 0.6061 | ±1.2122 | +1.815 | 0.0695 | . |
| Circulatory disease | +0.1588 | 0.5825 | ±1.1650 | +0.273 | 0.7852 |  |
| **Time < 54 (%)** | **-0.5042** | 0.2501 | ±0.5003 | **-2.016** | **0.0439** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.2441**, Adj R² = **0.2303**, F-statistic = **17.72** (p = **2.23e-38**), Residual SE = **6.016** on **768** df, AIC = **5047.1**, BIC = **5117.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5684** | 1.9008 | ±3.8015 | **+26.078** | **6.46e-150** | *** |
| Education: graduate level (vs college) | -0.0165 | 0.4916 | ±0.9833 | -0.033 | 0.9733 |  |
| Education: high school or below (vs college) | +0.3663 | 0.6367 | ±1.2735 | +0.575 | 0.5651 |  |
| **Site: UCSD (vs UAB)** | **+3.0033** | 0.5697 | ±1.1393 | **+5.272** | **1.35e-07** | *** |
| Site: UW (vs UAB) | -0.8887 | 0.5219 | ±1.0438 | -1.703 | 0.0886 | . |
| **Season: spring (vs autumn)** | **-2.1640** | 0.6171 | ±1.2342 | **-3.507** | **4.54e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8046** | 0.6174 | ±1.2347 | **+2.923** | **0.0035** | ** |
| **Season: winter (vs autumn)** | **-5.6350** | 0.6638 | ±1.3276 | **-8.489** | **2.09e-17** | *** |
| Age (years) | -0.0417 | 0.0216 | ±0.0433 | -1.926 | 0.0541 | . |
| BMI (kg/m2) | -0.0274 | 0.0329 | ±0.0659 | -0.831 | 0.4061 |  |
| Hypertension | -0.7563 | 0.4998 | ±0.9995 | -1.513 | 0.1302 |  |
| High cholesterol | -0.5575 | 0.4609 | ±0.9217 | -1.210 | 0.2264 |  |
| Kidney disease | +1.1111 | 0.6063 | ±1.2126 | +1.833 | 0.0669 | . |
| Circulatory disease | +0.1643 | 0.5822 | ±1.1645 | +0.282 | 0.7778 |  |
| Avg. daily time < 54 (%) | -0.4854 | 0.4767 | ±0.9534 | -1.018 | 0.3085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.97e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4642** | 1.9045 | ±3.8089 | **+25.973** | **1.01e-148** | *** |
| Education: graduate level (vs college) | +0.0083 | 0.4920 | ±0.9840 | +0.017 | 0.9865 |  |
| Education: high school or below (vs college) | +0.4049 | 0.6362 | ±1.2725 | +0.636 | 0.5245 |  |
| **Site: UCSD (vs UAB)** | **+3.0445** | 0.5705 | ±1.1409 | **+5.337** | **9.46e-08** | *** |
| Site: UW (vs UAB) | -0.8314 | 0.5209 | ±1.0417 | -1.596 | 0.1105 |  |
| **Season: spring (vs autumn)** | **-2.1327** | 0.6190 | ±1.2381 | **-3.445** | **5.71e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8406** | 0.6182 | ±1.2363 | **+2.978** | **0.0029** | ** |
| **Season: winter (vs autumn)** | **-5.6428** | 0.6643 | ±1.3286 | **-8.495** | **1.98e-17** | *** |
| Age (years) | -0.0424 | 0.0217 | ±0.0434 | -1.957 | 0.0503 | . |
| BMI (kg/m2) | -0.0262 | 0.0330 | ±0.0661 | -0.794 | 0.4271 |  |
| Hypertension | -0.7604 | 0.4994 | ±0.9989 | -1.522 | 0.1279 |  |
| High cholesterol | -0.5128 | 0.4620 | ±0.9241 | -1.110 | 0.2671 |  |
| Kidney disease | +1.1058 | 0.6071 | ±1.2143 | +1.821 | 0.0686 | . |
| Circulatory disease | +0.1798 | 0.5837 | ±1.1674 | +0.308 | 0.7580 |  |
| Time 54-69, pooled (%) | -0.0113 | 0.2348 | ±0.4696 | -0.048 | 0.9616 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.98e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4566** | 1.9043 | ±3.8086 | **+25.971** | **1.06e-148** | *** |
| Education: graduate level (vs college) | +0.0107 | 0.4922 | ±0.9844 | +0.022 | 0.9827 |  |
| Education: high school or below (vs college) | +0.4071 | 0.6368 | ±1.2735 | +0.639 | 0.5226 |  |
| **Site: UCSD (vs UAB)** | **+3.0482** | 0.5700 | ±1.1400 | **+5.348** | **8.90e-08** | *** |
| Site: UW (vs UAB) | -0.8270 | 0.5214 | ±1.0428 | -1.586 | 0.1127 |  |
| **Season: spring (vs autumn)** | **-2.1303** | 0.6190 | ±1.2381 | **-3.441** | **5.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8436** | 0.6186 | ±1.2372 | **+2.980** | **0.0029** | ** |
| **Season: winter (vs autumn)** | **-5.6418** | 0.6641 | ±1.3282 | **-8.496** | **1.97e-17** | *** |
| **Age (years)** | **-0.0425** | 0.0217 | ±0.0434 | **-1.960** | **0.0499** | * |
| BMI (kg/m2) | -0.0263 | 0.0330 | ±0.0661 | -0.794 | 0.4270 |  |
| Hypertension | -0.7617 | 0.4994 | ±0.9988 | -1.525 | 0.1272 |  |
| High cholesterol | -0.5086 | 0.4624 | ±0.9247 | -1.100 | 0.2713 |  |
| Kidney disease | +1.1043 | 0.6066 | ±1.2131 | +1.821 | 0.0687 | . |
| Circulatory disease | +0.1820 | 0.5837 | ±1.1673 | +0.312 | 0.7552 |  |
| Avg. daily time 54-69 (%) | +0.0045 | 0.2189 | ±0.4378 | +0.021 | 0.9834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.2432**, Adj R² = **0.2294**, F-statistic = **17.63** (p = **3.38e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.0**, BIC = **5117.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5321** | 1.9039 | ±3.8078 | **+26.016** | **3.23e-149** | *** |
| Education: graduate level (vs college) | -0.0096 | 0.4921 | ±0.9842 | -0.020 | 0.9844 |  |
| Education: high school or below (vs college) | +0.3858 | 0.6358 | ±1.2717 | +0.607 | 0.5440 |  |
| **Site: UCSD (vs UAB)** | **+3.0165** | 0.5702 | ±1.1404 | **+5.290** | **1.22e-07** | *** |
| Site: UW (vs UAB) | -0.8643 | 0.5212 | ±1.0423 | -1.658 | 0.0972 | . |
| **Season: spring (vs autumn)** | **-2.1481** | 0.6187 | ±1.2373 | **-3.472** | **5.16e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8208** | 0.6171 | ±1.2342 | **+2.950** | **0.0032** | ** |
| **Season: winter (vs autumn)** | **-5.6451** | 0.6644 | ±1.3287 | **-8.497** | **1.94e-17** | *** |
| Age (years) | -0.0419 | 0.0217 | ±0.0433 | -1.935 | 0.0530 | . |
| BMI (kg/m2) | -0.0266 | 0.0330 | ±0.0660 | -0.807 | 0.4198 |  |
| Hypertension | -0.7535 | 0.4996 | ±0.9992 | -1.508 | 0.1315 |  |
| High cholesterol | -0.5425 | 0.4621 | ±0.9243 | -1.174 | 0.2404 |  |
| Kidney disease | +1.1128 | 0.6073 | ±1.2146 | +1.832 | 0.0669 | . |
| Circulatory disease | +0.1654 | 0.5836 | ±1.1672 | +0.283 | 0.7768 |  |
| Time < 70 (%) | -0.0921 | 0.1875 | ±0.3749 | -0.491 | 0.6232 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.2430**, Adj R² = **0.2292**, F-statistic = **17.61** (p = **3.74e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.2**, BIC = **5118.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4940** | 1.9041 | ±3.8081 | **+25.994** | **5.81e-149** | *** |
| Education: graduate level (vs college) | -0.0020 | 0.4922 | ±0.9844 | -0.004 | 0.9967 |  |
| Education: high school or below (vs college) | +0.3934 | 0.6363 | ±1.2727 | +0.618 | 0.5364 |  |
| **Site: UCSD (vs UAB)** | **+3.0285** | 0.5698 | ±1.1396 | **+5.315** | **1.07e-07** | *** |
| Site: UW (vs UAB) | -0.8523 | 0.5216 | ±1.0431 | -1.634 | 0.1022 |  |
| **Season: spring (vs autumn)** | **-2.1430** | 0.6190 | ±1.2380 | **-3.462** | **5.36e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8278** | 0.6182 | ±1.2364 | **+2.957** | **0.0031** | ** |
| **Season: winter (vs autumn)** | **-5.6438** | 0.6642 | ±1.3285 | **-8.497** | **1.95e-17** | *** |
| Age (years) | -0.0421 | 0.0217 | ±0.0433 | -1.943 | 0.0520 | . |
| BMI (kg/m2) | -0.0263 | 0.0330 | ±0.0660 | -0.796 | 0.4261 |  |
| Hypertension | -0.7559 | 0.4996 | ±0.9991 | -1.513 | 0.1302 |  |
| High cholesterol | -0.5309 | 0.4623 | ±0.9246 | -1.148 | 0.2509 |  |
| Kidney disease | +1.1105 | 0.6068 | ±1.2136 | +1.830 | 0.0672 | . |
| Circulatory disease | +0.1712 | 0.5834 | ±1.1667 | +0.293 | 0.7692 |  |
| Avg. daily time < 70 (%) | -0.0557 | 0.1729 | ±0.3457 | -0.322 | 0.7474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.65** (p = **3.04e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3472** | 2.3129 | ±4.6258 | **+21.768** | **4.68e-105** | *** |
| Education: graduate level (vs college) | +0.0370 | 0.4918 | ±0.9836 | +0.075 | 0.9401 |  |
| Education: high school or below (vs college) | +0.3512 | 0.6399 | ±1.2798 | +0.549 | 0.5831 |  |
| **Site: UCSD (vs UAB)** | **+3.0800** | 0.5747 | ±1.1493 | **+5.360** | **8.33e-08** | *** |
| Site: UW (vs UAB) | -0.7863 | 0.5262 | ±1.0525 | -1.494 | 0.1351 |  |
| **Season: spring (vs autumn)** | **-2.1336** | 0.6171 | ±1.2342 | **-3.457** | **5.46e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8770** | 0.6180 | ±1.2360 | **+3.037** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6421** | 0.6628 | ±1.3256 | **-8.512** | **1.70e-17** | *** |
| Age (years) | -0.0413 | 0.0217 | ±0.0433 | -1.907 | 0.0565 | . |
| BMI (kg/m2) | -0.0282 | 0.0332 | ±0.0665 | -0.849 | 0.3957 |  |
| Hypertension | -0.7761 | 0.4998 | ±0.9996 | -1.553 | 0.1205 |  |
| High cholesterol | -0.5027 | 0.4598 | ±0.9196 | -1.093 | 0.2742 |  |
| Kidney disease | +1.0802 | 0.6060 | ±1.2120 | +1.783 | 0.0747 | . |
| Circulatory disease | +0.1559 | 0.5836 | ±1.1671 | +0.267 | 0.7893 |  |
| Time 54-250, pooled (%) | -0.0100 | 0.0136 | ±0.0272 | -0.739 | 0.4600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **3.02e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3854** | 2.3495 | ±4.6989 | **+21.445** | **5.04e-102** | *** |
| Education: graduate level (vs college) | +0.0369 | 0.4919 | ±0.9837 | +0.075 | 0.9402 |  |
| Education: high school or below (vs college) | +0.3502 | 0.6403 | ±1.2805 | +0.547 | 0.5844 |  |
| **Site: UCSD (vs UAB)** | **+3.0811** | 0.5747 | ±1.1494 | **+5.361** | **8.27e-08** | *** |
| Site: UW (vs UAB) | -0.7870 | 0.5260 | ±1.0521 | -1.496 | 0.1346 |  |
| **Season: spring (vs autumn)** | **-2.1347** | 0.6171 | ±1.2342 | **-3.459** | **5.42e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8757** | 0.6177 | ±1.2354 | **+3.037** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6429** | 0.6629 | ±1.3258 | **-8.513** | **1.70e-17** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0433 | -1.914 | 0.0556 | . |
| BMI (kg/m2) | -0.0283 | 0.0332 | ±0.0665 | -0.852 | 0.3943 |  |
| Hypertension | -0.7754 | 0.4997 | ±0.9994 | -1.552 | 0.1207 |  |
| High cholesterol | -0.5025 | 0.4597 | ±0.9194 | -1.093 | 0.2744 |  |
| Kidney disease | +1.0773 | 0.6063 | ±1.2127 | +1.777 | 0.0756 | . |
| Circulatory disease | +0.1541 | 0.5835 | ±1.1670 | +0.264 | 0.7917 |  |
| Avg. daily time 54-250 (%) | -0.0103 | 0.0139 | ±0.0279 | -0.740 | 0.4592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.2431**, Adj R² = **0.2293**, F-statistic = **17.62** (p = **3.60e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.1**, BIC = **5118.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4579** | 1.9012 | ±3.8025 | **+26.013** | **3.49e-149** | *** |
| Education: graduate level (vs college) | +0.0068 | 0.4915 | ±0.9830 | +0.014 | 0.9890 |  |
| Education: high school or below (vs college) | +0.3805 | 0.6328 | ±1.2657 | +0.601 | 0.5477 |  |
| **Site: UCSD (vs UAB)** | **+3.0617** | 0.5726 | ±1.1452 | **+5.347** | **8.94e-08** | *** |
| Site: UW (vs UAB) | -0.8204 | 0.5222 | ±1.0444 | -1.571 | 0.1162 |  |
| **Season: spring (vs autumn)** | **-2.1449** | 0.6159 | ±1.2318 | **-3.483** | **4.97e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8345** | 0.6171 | ±1.2342 | **+2.973** | **0.0030** | ** |
| **Season: winter (vs autumn)** | **-5.6522** | 0.6632 | ±1.3264 | **-8.523** | **1.56e-17** | *** |
| **Age (years)** | **-0.0431** | 0.0217 | ±0.0434 | **-1.985** | **0.0471** | * |
| BMI (kg/m2) | -0.0291 | 0.0337 | ±0.0674 | -0.863 | 0.3881 |  |
| Hypertension | -0.7594 | 0.4997 | ±0.9995 | -1.520 | 0.1286 |  |
| High cholesterol | -0.5150 | 0.4603 | ±0.9205 | -1.119 | 0.2632 |  |
| Kidney disease | +1.0824 | 0.6066 | ±1.2132 | +1.784 | 0.0744 | . |
| Circulatory disease | +0.1725 | 0.5856 | ±1.1712 | +0.295 | 0.7683 |  |
| Time 181-250, pooled (%) | +0.0069 | 0.0157 | ±0.0314 | +0.438 | 0.6613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.2432**, Adj R² = **0.2294**, F-statistic = **17.63** (p = **3.49e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.0**, BIC = **5118.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4562** | 1.9016 | ±3.8032 | **+26.008** | **4.03e-149** | *** |
| Education: graduate level (vs college) | +0.0051 | 0.4914 | ±0.9828 | +0.010 | 0.9917 |  |
| Education: high school or below (vs college) | +0.3745 | 0.6324 | ±1.2648 | +0.592 | 0.5537 |  |
| **Site: UCSD (vs UAB)** | **+3.0660** | 0.5732 | ±1.1464 | **+5.349** | **8.85e-08** | *** |
| Site: UW (vs UAB) | -0.8173 | 0.5225 | ±1.0449 | -1.564 | 0.1178 |  |
| **Season: spring (vs autumn)** | **-2.1478** | 0.6159 | ±1.2319 | **-3.487** | **4.88e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8329** | 0.6170 | ±1.2340 | **+2.971** | **0.0030** | ** |
| **Season: winter (vs autumn)** | **-5.6553** | 0.6632 | ±1.3264 | **-8.527** | **1.50e-17** | *** |
| **Age (years)** | **-0.0431** | 0.0217 | ±0.0434 | **-1.988** | **0.0468** | * |
| BMI (kg/m2) | -0.0295 | 0.0337 | ±0.0674 | -0.877 | 0.3807 |  |
| Hypertension | -0.7594 | 0.4996 | ±0.9993 | -1.520 | 0.1286 |  |
| High cholesterol | -0.5162 | 0.4603 | ±0.9206 | -1.122 | 0.2621 |  |
| Kidney disease | +1.0783 | 0.6064 | ±1.2128 | +1.778 | 0.0754 | . |
| Circulatory disease | +0.1723 | 0.5857 | ±1.1714 | +0.294 | 0.7686 |  |
| Avg. daily time 181-250 (%) | +0.0078 | 0.0153 | ±0.0306 | +0.509 | 0.6111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.94e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3786** | 1.8997 | ±3.7994 | **+25.993** | **5.98e-149** | *** |
| Education: graduate level (vs college) | +0.0253 | 0.4916 | ±0.9833 | +0.052 | 0.9589 |  |
| Education: high school or below (vs college) | +0.3399 | 0.6360 | ±1.2719 | +0.534 | 0.5930 |  |
| **Site: UCSD (vs UAB)** | **+3.0847** | 0.5756 | ±1.1512 | **+5.359** | **8.37e-08** | *** |
| Site: UW (vs UAB) | -0.7913 | 0.5255 | ±1.0509 | -1.506 | 0.1321 |  |
| **Season: spring (vs autumn)** | **-2.1475** | 0.6161 | ±1.2322 | **-3.486** | **4.91e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8581** | 0.6169 | ±1.2338 | **+3.012** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6524** | 0.6632 | ±1.3265 | **-8.522** | **1.56e-17** | *** |
| Age (years) | -0.0423 | 0.0217 | ±0.0433 | -1.953 | 0.0508 | . |
| BMI (kg/m2) | -0.0306 | 0.0337 | ±0.0675 | -0.908 | 0.3641 |  |
| Hypertension | -0.7698 | 0.4997 | ±0.9994 | -1.540 | 0.1235 |  |
| High cholesterol | -0.5108 | 0.4598 | ±0.9197 | -1.111 | 0.2667 |  |
| Kidney disease | +1.0643 | 0.6066 | ±1.2132 | +1.755 | 0.0793 | . |
| Circulatory disease | +0.1540 | 0.5856 | ±1.1711 | +0.263 | 0.7926 |  |
| Time > 180 (%) | +0.0071 | 0.0094 | ±0.0188 | +0.754 | 0.4506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.2436**, Adj R² = **0.2298**, F-statistic = **17.67** (p = **2.85e-38**), Residual SE = **6.018** on **768** df, AIC = **5047.6**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3834** | 1.8993 | ±3.7986 | **+26.001** | **4.86e-149** | *** |
| Education: graduate level (vs college) | +0.0243 | 0.4916 | ±0.9832 | +0.049 | 0.9606 |  |
| Education: high school or below (vs college) | +0.3353 | 0.6360 | ±1.2720 | +0.527 | 0.5980 |  |
| **Site: UCSD (vs UAB)** | **+3.0887** | 0.5762 | ±1.1523 | **+5.361** | **8.28e-08** | *** |
| Site: UW (vs UAB) | -0.7891 | 0.5255 | ±1.0511 | -1.501 | 0.1332 |  |
| **Season: spring (vs autumn)** | **-2.1501** | 0.6161 | ±1.2322 | **-3.490** | **4.83e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8565** | 0.6168 | ±1.2335 | **+3.010** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6552** | 0.6633 | ±1.3267 | **-8.525** | **1.52e-17** | *** |
| Age (years) | -0.0423 | 0.0216 | ±0.0433 | -1.955 | 0.0506 | . |
| BMI (kg/m2) | -0.0309 | 0.0337 | ±0.0675 | -0.915 | 0.3604 |  |
| Hypertension | -0.7695 | 0.4997 | ±0.9993 | -1.540 | 0.1235 |  |
| High cholesterol | -0.5113 | 0.4599 | ±0.9198 | -1.112 | 0.2662 |  |
| Kidney disease | +1.0601 | 0.6067 | ±1.2133 | +1.747 | 0.0806 | . |
| Circulatory disease | +0.1531 | 0.5857 | ±1.1714 | +0.261 | 0.7938 |  |
| Avg. daily time > 180 (%) | +0.0074 | 0.0094 | ±0.0187 | +0.789 | 0.4302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.94e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4503** | 1.9009 | ±3.8018 | **+26.014** | **3.43e-149** | *** |
| Education: graduate level (vs college) | +0.0151 | 0.4927 | ±0.9854 | +0.031 | 0.9756 |  |
| Education: high school or below (vs college) | +0.3967 | 0.6376 | ±1.2752 | +0.622 | 0.5338 |  |
| **Site: UCSD (vs UAB)** | **+3.0541** | 0.5759 | ±1.1517 | **+5.304** | **1.14e-07** | *** |
| Site: UW (vs UAB) | -0.8235 | 0.5239 | ±1.0478 | -1.572 | 0.1160 |  |
| **Season: spring (vs autumn)** | **-2.1350** | 0.6164 | ±1.2328 | **-3.464** | **5.33e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8461** | 0.6171 | ±1.2342 | **+2.992** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6447** | 0.6643 | ±1.3286 | **-8.497** | **1.94e-17** | *** |
| Age (years) | -0.0423 | 0.0217 | ±0.0433 | -1.953 | 0.0508 | . |
| BMI (kg/m2) | -0.0272 | 0.0339 | ±0.0678 | -0.802 | 0.4228 |  |
| Hypertension | -0.7619 | 0.5001 | ±1.0002 | -1.523 | 0.1276 |  |
| High cholesterol | -0.5094 | 0.4597 | ±0.9194 | -1.108 | 0.2678 |  |
| Kidney disease | +1.1001 | 0.6070 | ±1.2140 | +1.812 | 0.0699 | . |
| Circulatory disease | +0.1769 | 0.5840 | ±1.1679 | +0.303 | 0.7619 |  |
| Nocturnal time > 180 (%) | +0.0012 | 0.0083 | ±0.0167 | +0.138 | 0.8902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.94e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3396** | 1.8983 | ±3.7966 | **+25.991** | **6.20e-149** | *** |
| Education: graduate level (vs college) | +0.0379 | 0.4918 | ±0.9835 | +0.077 | 0.9386 |  |
| Education: high school or below (vs college) | +0.3469 | 0.6399 | ±1.2798 | +0.542 | 0.5877 |  |
| **Site: UCSD (vs UAB)** | **+3.0809** | 0.5745 | ±1.1490 | **+5.363** | **8.19e-08** | *** |
| Site: UW (vs UAB) | -0.7851 | 0.5260 | ±1.0521 | -1.493 | 0.1355 |  |
| **Season: spring (vs autumn)** | **-2.1342** | 0.6171 | ±1.2342 | **-3.458** | **5.43e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8785** | 0.6180 | ±1.2359 | **+3.040** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6417** | 0.6627 | ±1.3254 | **-8.513** | **1.70e-17** | *** |
| Age (years) | -0.0412 | 0.0217 | ±0.0433 | -1.903 | 0.0570 | . |
| BMI (kg/m2) | -0.0284 | 0.0332 | ±0.0665 | -0.855 | 0.3928 |  |
| Hypertension | -0.7769 | 0.4998 | ±0.9996 | -1.555 | 0.1201 |  |
| High cholesterol | -0.5033 | 0.4598 | ±0.9196 | -1.095 | 0.2736 |  |
| Kidney disease | +1.0787 | 0.6059 | ±1.2118 | +1.780 | 0.0750 | . |
| Circulatory disease | +0.1539 | 0.5836 | ±1.1671 | +0.264 | 0.7920 |  |
| Time > 250 (%) | +0.0106 | 0.0136 | ±0.0272 | +0.784 | 0.4331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.94e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3523** | 1.8964 | ±3.7928 | **+26.024** | **2.63e-149** | *** |
| Education: graduate level (vs college) | +0.0375 | 0.4918 | ±0.9836 | +0.076 | 0.9392 |  |
| Education: high school or below (vs college) | +0.3469 | 0.6403 | ±1.2807 | +0.542 | 0.5880 |  |
| **Site: UCSD (vs UAB)** | **+3.0816** | 0.5745 | ±1.1491 | **+5.363** | **8.16e-08** | *** |
| Site: UW (vs UAB) | -0.7865 | 0.5258 | ±1.0517 | -1.496 | 0.1347 |  |
| **Season: spring (vs autumn)** | **-2.1356** | 0.6171 | ±1.2341 | **-3.461** | **5.38e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8763** | 0.6176 | ±1.2353 | **+3.038** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6428** | 0.6628 | ±1.3257 | **-8.513** | **1.69e-17** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0433 | -1.911 | 0.0560 | . |
| BMI (kg/m2) | -0.0284 | 0.0332 | ±0.0665 | -0.855 | 0.3923 |  |
| Hypertension | -0.7759 | 0.4997 | ±0.9994 | -1.553 | 0.1205 |  |
| High cholesterol | -0.5032 | 0.4597 | ±0.9195 | -1.095 | 0.2737 |  |
| Kidney disease | +1.0762 | 0.6063 | ±1.2125 | +1.775 | 0.0759 | . |
| Circulatory disease | +0.1525 | 0.5835 | ±1.1670 | +0.261 | 0.7938 |  |
| Avg. daily time > 250 (%) | +0.0108 | 0.0139 | ±0.0279 | +0.772 | 0.4400 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0555**, F-statistic = **4.53** (p = **1.67e-07**), Residual SE = **16.867** on **769** df, AIC = **6660.4**, BIC = **6725.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6351** | 6.6943 | ±13.3887 | **+18.917** | **8.30e-80** | *** |
| Education: graduate level (vs college) | -1.0720 | 1.2495 | ±2.4991 | -0.858 | 0.3909 |  |
| **Education: high school or below (vs college)** | **+6.2851** | 2.2654 | ±4.5307 | **+2.774** | **0.0055** | ** |
| Site: UCSD (vs UAB) | +3.1010 | 1.6964 | ±3.3928 | +1.828 | 0.0675 | . |
| Site: UW (vs UAB) | -2.8051 | 1.4313 | ±2.8627 | -1.960 | 0.0500 | . |
| **Season: spring (vs autumn)** | **+3.5501** | 1.4970 | ±2.9940 | **+2.371** | **0.0177** | * |
| Season: summer (vs autumn) | +3.1214 | 1.6511 | ±3.3022 | +1.891 | 0.0587 | . |
| **Season: winter (vs autumn)** | **+3.7614** | 1.8748 | ±3.7495 | **+2.006** | **0.0448** | * |
| **Age (years)** | **-0.1493** | 0.0690 | ±0.1379 | **-2.165** | **0.0304** | * |
| BMI (kg/m2) | +0.1956 | 0.1098 | ±0.2196 | +1.782 | 0.0748 | . |
| Hypertension | +0.5220 | 1.4770 | ±2.9539 | +0.353 | 0.7238 |  |
| High cholesterol | +1.9132 | 1.3427 | ±2.6854 | +1.425 | 0.1542 |  |
| Kidney disease | -2.0221 | 1.7254 | ±3.4507 | -1.172 | 0.2412 |  |
| Circulatory disease | +0.0338 | 1.7091 | ±3.4182 | +0.020 | 0.9842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.0808**, Adj R² = **0.0640**, F-statistic = **4.82** (p = **1.40e-08**), Residual SE = **16.790** on **768** df, AIC = **6654.3**, BIC = **6724.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.5959** | 7.1333 | ±14.2666 | **+18.869** | **2.06e-79** | *** |
| Education: graduate level (vs college) | -1.3302 | 1.2398 | ±2.4796 | -1.073 | 0.2833 |  |
| **Education: high school or below (vs college)** | **+7.0160** | 2.2657 | ±4.5315 | **+3.097** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +2.8489 | 1.6891 | ±3.3782 | +1.687 | 0.0917 | . |
| **Site: UW (vs UAB)** | **-3.1537** | 1.4258 | ±2.8516 | **-2.212** | **0.0270** | * |
| **Season: spring (vs autumn)** | **+3.4113** | 1.4957 | ±2.9914 | **+2.281** | **0.0226** | * |
| Season: summer (vs autumn) | +2.9369 | 1.6499 | ±3.2998 | +1.780 | 0.0751 | . |
| **Season: winter (vs autumn)** | **+3.7444** | 1.8659 | ±3.7317 | **+2.007** | **0.0448** | * |
| **Age (years)** | **-0.1524** | 0.0690 | ±0.1380 | **-2.209** | **0.0272** | * |
| **BMI (kg/m2)** | **+0.2371** | 0.1110 | ±0.2221 | **+2.135** | **0.0327** | * |
| Hypertension | +0.7048 | 1.4678 | ±2.9356 | +0.480 | 0.6311 |  |
| High cholesterol | +2.0618 | 1.3395 | ±2.6791 | +1.539 | 0.1238 |  |
| Kidney disease | -1.9705 | 1.7151 | ±3.4302 | -1.149 | 0.2506 |  |
| Circulatory disease | +0.3184 | 1.7059 | ±3.4117 | +0.187 | 0.8519 |  |
| **HbA1c (%)** | **-1.3267** | 0.5129 | ±1.0258 | **-2.587** | **0.0097** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.0763**, Adj R² = **0.0595**, F-statistic = **4.53** (p = **6.48e-08**), Residual SE = **16.831** on **768** df, AIC = **6658.1**, BIC = **6728.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.2762** | 7.3033 | ±14.6065 | **+17.975** | **3.06e-72** | *** |
| Education: graduate level (vs college) | -1.1912 | 1.2420 | ±2.4839 | -0.959 | 0.3375 |  |
| **Education: high school or below (vs college)** | **+6.7766** | 2.2785 | ±4.5571 | **+2.974** | **0.0029** | ** |
| Site: UCSD (vs UAB) | +2.8551 | 1.7109 | ±3.4218 | +1.669 | 0.0952 | . |
| **Site: UW (vs UAB)** | **-3.0484** | 1.4345 | ±2.8689 | **-2.125** | **0.0336** | * |
| **Season: spring (vs autumn)** | **+3.6622** | 1.4962 | ±2.9924 | **+2.448** | **0.0144** | * |
| Season: summer (vs autumn) | +2.9547 | 1.6603 | ±3.3205 | +1.780 | 0.0751 | . |
| **Season: winter (vs autumn)** | **+3.7904** | 1.8626 | ±3.7252 | **+2.035** | **0.0418** | * |
| **Age (years)** | **-0.1530** | 0.0695 | ±0.1390 | **-2.201** | **0.0277** | * |
| **BMI (kg/m2)** | **+0.2225** | 0.1091 | ±0.2182 | **+2.039** | **0.0415** | * |
| Hypertension | +0.6173 | 1.4769 | ±2.9538 | +0.418 | 0.6760 |  |
| High cholesterol | +1.9597 | 1.3444 | ±2.6888 | +1.458 | 0.1449 |  |
| Kidney disease | -1.8215 | 1.7330 | ±3.4659 | -1.051 | 0.2932 |  |
| Circulatory disease | +0.2587 | 1.7067 | ±3.4134 | +0.152 | 0.8795 |  |
| Mean glucose (mg/dL) | -0.0325 | 0.0169 | ±0.0337 | -1.923 | 0.0545 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.0763**, Adj R² = **0.0595**, F-statistic = **4.53** (p = **6.48e-08**), Residual SE = **16.831** on **768** df, AIC = **6658.1**, BIC = **6728.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.7669** | 8.5236 | ±17.0472 | **+15.928** | **4.03e-57** | *** |
| Education: graduate level (vs college) | -1.1912 | 1.2420 | ±2.4839 | -0.959 | 0.3375 |  |
| **Education: high school or below (vs college)** | **+6.7766** | 2.2785 | ±4.5571 | **+2.974** | **0.0029** | ** |
| Site: UCSD (vs UAB) | +2.8551 | 1.7109 | ±3.4218 | +1.669 | 0.0952 | . |
| **Site: UW (vs UAB)** | **-3.0484** | 1.4345 | ±2.8689 | **-2.125** | **0.0336** | * |
| **Season: spring (vs autumn)** | **+3.6622** | 1.4962 | ±2.9924 | **+2.448** | **0.0144** | * |
| Season: summer (vs autumn) | +2.9547 | 1.6603 | ±3.3205 | +1.780 | 0.0751 | . |
| **Season: winter (vs autumn)** | **+3.7904** | 1.8626 | ±3.7252 | **+2.035** | **0.0418** | * |
| **Age (years)** | **-0.1530** | 0.0695 | ±0.1390 | **-2.201** | **0.0277** | * |
| **BMI (kg/m2)** | **+0.2225** | 0.1091 | ±0.2182 | **+2.039** | **0.0415** | * |
| Hypertension | +0.6173 | 1.4769 | ±2.9538 | +0.418 | 0.6760 |  |
| High cholesterol | +1.9597 | 1.3444 | ±2.6888 | +1.458 | 0.1449 |  |
| Kidney disease | -1.8215 | 1.7330 | ±3.4659 | -1.051 | 0.2932 |  |
| Circulatory disease | +0.2587 | 1.7067 | ±3.4134 | +0.152 | 0.8795 |  |
| GMI (%) | -1.3567 | 0.7054 | ±1.4109 | -1.923 | 0.0545 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.0754**, Adj R² = **0.0585**, F-statistic = **4.47** (p = **9.07e-08**), Residual SE = **16.840** on **768** df, AIC = **6658.9**, BIC = **6728.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4578** | 7.4496 | ±14.8993 | **+17.512** | **1.16e-68** | *** |
| Education: graduate level (vs college) | -1.2246 | 1.2419 | ±2.4838 | -0.986 | 0.3241 |  |
| **Education: high school or below (vs college)** | **+6.6782** | 2.2526 | ±4.5053 | **+2.965** | **0.0030** | ** |
| Site: UCSD (vs UAB) | +2.8939 | 1.7127 | ±3.4254 | +1.690 | 0.0911 | . |
| **Site: UW (vs UAB)** | **-2.9516** | 1.4314 | ±2.8627 | **-2.062** | **0.0392** | * |
| **Season: spring (vs autumn)** | **+3.7021** | 1.4947 | ±2.9895 | **+2.477** | **0.0133** | * |
| Season: summer (vs autumn) | +2.9646 | 1.6638 | ±3.3276 | +1.782 | 0.0748 | . |
| **Season: winter (vs autumn)** | **+3.8185** | 1.8596 | ±3.7191 | **+2.053** | **0.0400** | * |
| **Age (years)** | **-0.1568** | 0.0702 | ±0.1403 | **-2.235** | **0.0254** | * |
| **BMI (kg/m2)** | **+0.2258** | 0.1086 | ±0.2172 | **+2.079** | **0.0376** | * |
| Hypertension | +0.5803 | 1.4795 | ±2.9590 | +0.392 | 0.6949 |  |
| High cholesterol | +1.9463 | 1.3459 | ±2.6919 | +1.446 | 0.1482 |  |
| Kidney disease | -1.9589 | 1.7311 | ±3.4622 | -1.132 | 0.2578 |  |
| Circulatory disease | +0.2180 | 1.7021 | ±3.4043 | +0.128 | 0.8981 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0276 | 0.0177 | ±0.0355 | -1.557 | 0.1194 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.0742**, Adj R² = **0.0573**, F-statistic = **4.39** (p = **1.36e-07**), Residual SE = **16.851** on **768** df, AIC = **6659.9**, BIC = **6729.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.2029** | 6.7374 | ±13.4749 | **+19.177** | **5.78e-82** | *** |
| Education: graduate level (vs college) | -1.2158 | 1.2462 | ±2.4924 | -0.976 | 0.3293 |  |
| **Education: high school or below (vs college)** | **+6.5804** | 2.2759 | ±4.5519 | **+2.891** | **0.0038** | ** |
| Site: UCSD (vs UAB) | +2.9141 | 1.7111 | ±3.4222 | +1.703 | 0.0886 | . |
| **Site: UW (vs UAB)** | **-3.1123** | 1.4411 | ±2.8823 | **-2.160** | **0.0308** | * |
| **Season: spring (vs autumn)** | **+3.6451** | 1.4990 | ±2.9980 | **+2.432** | **0.0150** | * |
| Season: summer (vs autumn) | +3.0251 | 1.6554 | ±3.3108 | +1.827 | 0.0676 | . |
| **Season: winter (vs autumn)** | **+3.7901** | 1.8686 | ±3.7372 | **+2.028** | **0.0425** | * |
| **Age (years)** | **-0.1481** | 0.0693 | ±0.1386 | **-2.137** | **0.0326** | * |
| BMI (kg/m2) | +0.2138 | 0.1116 | ±0.2232 | +1.916 | 0.0554 | . |
| Hypertension | +0.6476 | 1.4685 | ±2.9370 | +0.441 | 0.6592 |  |
| High cholesterol | +1.8647 | 1.3376 | ±2.6751 | +1.394 | 0.1633 |  |
| Kidney disease | -1.5034 | 1.7507 | ±3.5015 | -0.859 | 0.3905 |  |
| Circulatory disease | +0.1769 | 1.7029 | ±3.4058 | +0.104 | 0.9173 |  |
| Glucose SD, pooled (mg/dL) | -0.0834 | 0.0609 | ±0.1219 | -1.368 | 0.1713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.0722**, Adj R² = **0.0552**, F-statistic = **4.27** (p = **2.66e-07**), Residual SE = **16.869** on **768** df, AIC = **6661.6**, BIC = **6731.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.1765** | 6.8007 | ±13.6015 | **+18.847** | **3.08e-79** | *** |
| Education: graduate level (vs college) | -1.1368 | 1.2505 | ±2.5010 | -0.909 | 0.3633 |  |
| **Education: high school or below (vs college)** | **+6.4726** | 2.2755 | ±4.5509 | **+2.845** | **0.0044** | ** |
| Site: UCSD (vs UAB) | +2.9913 | 1.7056 | ±3.4111 | +1.754 | 0.0795 | . |
| **Site: UW (vs UAB)** | **-2.9678** | 1.4409 | ±2.8819 | **-2.060** | **0.0394** | * |
| **Season: spring (vs autumn)** | **+3.6024** | 1.4974 | ±2.9947 | **+2.406** | **0.0161** | * |
| Season: summer (vs autumn) | +3.0595 | 1.6582 | ±3.3164 | +1.845 | 0.0650 | . |
| **Season: winter (vs autumn)** | **+3.7561** | 1.8748 | ±3.7495 | **+2.004** | **0.0451** | * |
| **Age (years)** | **-0.1480** | 0.0692 | ±0.1384 | **-2.138** | **0.0325** | * |
| BMI (kg/m2) | +0.2036 | 0.1107 | ±0.2213 | +1.840 | 0.0657 | . |
| Hypertension | +0.5850 | 1.4745 | ±2.9490 | +0.397 | 0.6915 |  |
| High cholesterol | +1.8886 | 1.3415 | ±2.6830 | +1.408 | 0.1592 |  |
| Kidney disease | -1.7046 | 1.7511 | ±3.5021 | -0.973 | 0.3303 |  |
| Circulatory disease | +0.1031 | 1.7106 | ±3.4212 | +0.060 | 0.9520 |  |
| Avg. daily SD (mg/dL) | -0.0545 | 0.0587 | ±0.1174 | -0.928 | 0.3533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0543**, F-statistic = **4.21** (p = **3.61e-07**), Residual SE = **16.877** on **768** df, AIC = **6662.4**, BIC = **6732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2674** | 6.5137 | ±13.0275 | **+19.538** | **5.19e-85** | *** |
| Education: graduate level (vs college) | -1.0901 | 1.2575 | ±2.5150 | -0.867 | 0.3860 |  |
| **Education: high school or below (vs college)** | **+6.2906** | 2.2691 | ±4.5382 | **+2.772** | **0.0056** | ** |
| Site: UCSD (vs UAB) | +3.0830 | 1.6991 | ±3.3982 | +1.814 | 0.0696 | . |
| **Site: UW (vs UAB)** | **-2.8453** | 1.4348 | ±2.8697 | **-1.983** | **0.0474** | * |
| **Season: spring (vs autumn)** | **+3.5511** | 1.4992 | ±2.9984 | **+2.369** | **0.0179** | * |
| Season: summer (vs autumn) | +3.1195 | 1.6527 | ±3.3053 | +1.888 | 0.0591 | . |
| **Season: winter (vs autumn)** | **+3.7620** | 1.8774 | ±3.7549 | **+2.004** | **0.0451** | * |
| **Age (years)** | **-0.1485** | 0.0699 | ±0.1398 | **-2.125** | **0.0336** | * |
| BMI (kg/m2) | +0.1963 | 0.1106 | ±0.2211 | +1.776 | 0.0758 | . |
| Hypertension | +0.5394 | 1.4647 | ±2.9293 | +0.368 | 0.7127 |  |
| High cholesterol | +1.8930 | 1.3404 | ±2.6807 | +1.412 | 0.1579 |  |
| Kidney disease | -1.9369 | 1.7410 | ±3.4819 | -1.113 | 0.2659 |  |
| Circulatory disease | +0.0373 | 1.7108 | ±3.4215 | +0.022 | 0.9826 |  |
| CV (%) | -0.0291 | 0.1150 | ±0.2300 | -0.253 | 0.8005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0543**, F-statistic = **4.20** (p = **3.68e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2500** | 7.9794 | ±15.9589 | **+15.822** | **2.20e-56** | *** |
| Education: graduate level (vs college) | -1.0792 | 1.2566 | ±2.5132 | -0.859 | 0.3904 |  |
| **Education: high school or below (vs college)** | **+6.2874** | 2.2678 | ±4.5356 | **+2.772** | **0.0056** | ** |
| Site: UCSD (vs UAB) | +3.0966 | 1.6984 | ±3.3969 | +1.823 | 0.0683 | . |
| **Site: UW (vs UAB)** | **-2.8222** | 1.4330 | ±2.8661 | **-1.969** | **0.0489** | * |
| **Season: spring (vs autumn)** | **+3.5537** | 1.5004 | ±3.0007 | **+2.369** | **0.0179** | * |
| Season: summer (vs autumn) | +3.1293 | 1.6562 | ±3.3124 | +1.889 | 0.0588 | . |
| **Season: winter (vs autumn)** | **+3.7665** | 1.8832 | ±3.7663 | **+2.000** | **0.0455** | * |
| **Age (years)** | **-0.1490** | 0.0697 | ±0.1394 | **-2.138** | **0.0325** | * |
| BMI (kg/m2) | +0.1958 | 0.1101 | ±0.2202 | +1.778 | 0.0754 | . |
| Hypertension | +0.5306 | 1.4673 | ±2.9346 | +0.362 | 0.7176 |  |
| High cholesterol | +1.9078 | 1.3414 | ±2.6827 | +1.422 | 0.1549 |  |
| Kidney disease | -1.9860 | 1.7330 | ±3.4661 | -1.146 | 0.2518 |  |
| Circulatory disease | +0.0390 | 1.7092 | ±3.4183 | +0.023 | 0.9818 |  |
| Mean / SD ratio | +0.0812 | 0.6347 | ±1.2695 | +0.128 | 0.8983 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.0717**, Adj R² = **0.0548**, F-statistic = **4.24** (p = **3.06e-07**), Residual SE = **16.873** on **768** df, AIC = **6662.0**, BIC = **6731.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.5085** | 7.6080 | ±15.2159 | **+16.891** | **5.21e-64** | *** |
| Education: graduate level (vs college) | -1.0444 | 1.2567 | ±2.5134 | -0.831 | 0.4059 |  |
| **Education: high school or below (vs college)** | **+6.2673** | 2.2642 | ±4.5284 | **+2.768** | **0.0056** | ** |
| Site: UCSD (vs UAB) | +3.1189 | 1.6976 | ±3.3952 | +1.837 | 0.0662 | . |
| Site: UW (vs UAB) | -2.7276 | 1.4351 | ±2.8701 | -1.901 | 0.0573 | . |
| **Season: spring (vs autumn)** | **+3.5598** | 1.5017 | ±3.0033 | **+2.371** | **0.0178** | * |
| Season: summer (vs autumn) | +3.0970 | 1.6520 | ±3.3039 | +1.875 | 0.0608 | . |
| **Season: winter (vs autumn)** | **+3.7580** | 1.8769 | ±3.7538 | **+2.002** | **0.0453** | * |
| **Age (years)** | **-0.1518** | 0.0697 | ±0.1395 | **-2.176** | **0.0296** | * |
| BMI (kg/m2) | +0.1968 | 0.1096 | ±0.2192 | +1.796 | 0.0725 | . |
| Hypertension | +0.4809 | 1.4715 | ±2.9429 | +0.327 | 0.7438 |  |
| High cholesterol | +1.9474 | 1.3455 | ±2.6911 | +1.447 | 0.1478 |  |
| Kidney disease | -2.2008 | 1.7415 | ±3.4830 | -1.264 | 0.2063 |  |
| Circulatory disease | +0.0265 | 1.7101 | ±3.4202 | +0.016 | 0.9876 |  |
| Avg. daily mean/SD | -0.3402 | 0.4846 | ±0.9691 | -0.702 | 0.4826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0542**, F-statistic = **4.20** (p = **3.70e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8268** | 6.7159 | ±13.4319 | **+18.884** | **1.53e-79** | *** |
| Education: graduate level (vs college) | -1.0788 | 1.2509 | ±2.5017 | -0.862 | 0.3885 |  |
| **Education: high school or below (vs college)** | **+6.2886** | 2.2796 | ±4.5592 | **+2.759** | **0.0058** | ** |
| Site: UCSD (vs UAB) | +3.0936 | 1.6893 | ±3.3786 | +1.831 | 0.0671 | . |
| **Site: UW (vs UAB)** | **-2.8200** | 1.4228 | ±2.8455 | **-1.982** | **0.0475** | * |
| **Season: spring (vs autumn)** | **+3.5512** | 1.5005 | ±3.0011 | **+2.367** | **0.0180** | * |
| Season: summer (vs autumn) | +3.1134 | 1.6446 | ±3.2891 | +1.893 | 0.0583 | . |
| **Season: winter (vs autumn)** | **+3.7585** | 1.8728 | ±3.7455 | **+2.007** | **0.0448** | * |
| **Age (years)** | **-0.1496** | 0.0679 | ±0.1358 | **-2.204** | **0.0276** | * |
| BMI (kg/m2) | +0.1959 | 0.1111 | ±0.2222 | +1.763 | 0.0779 | . |
| Hypertension | +0.5198 | 1.4830 | ±2.9660 | +0.350 | 0.7260 |  |
| High cholesterol | +1.9077 | 1.3657 | ±2.7314 | +1.397 | 0.1625 |  |
| Kidney disease | -2.0140 | 1.7074 | ±3.4148 | -1.180 | 0.2382 |  |
| Circulatory disease | +0.0357 | 1.7186 | ±3.4371 | +0.021 | 0.9834 |  |
| MAG (mg/dL/h) | -0.0037 | 0.0717 | ±0.1434 | -0.052 | 0.9588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.0715**, Adj R² = **0.0546**, F-statistic = **4.23** (p = **3.28e-07**), Residual SE = **16.875** on **768** df, AIC = **6662.1**, BIC = **6732.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0686** | 6.9079 | ±13.8158 | **+18.539** | **9.91e-77** | *** |
| Education: graduate level (vs college) | -1.1111 | 1.2515 | ±2.5030 | -0.888 | 0.3746 |  |
| **Education: high school or below (vs college)** | **+6.3956** | 2.2732 | ±4.5464 | **+2.813** | **0.0049** | ** |
| Site: UCSD (vs UAB) | +3.0223 | 1.7020 | ±3.4039 | +1.776 | 0.0758 | . |
| **Site: UW (vs UAB)** | **-2.9114** | 1.4337 | ±2.8675 | **-2.031** | **0.0423** | * |
| **Season: spring (vs autumn)** | **+3.5952** | 1.4998 | ±2.9997 | **+2.397** | **0.0165** | * |
| Season: summer (vs autumn) | +3.1054 | 1.6546 | ±3.3092 | +1.877 | 0.0605 | . |
| **Season: winter (vs autumn)** | **+3.7673** | 1.8760 | ±3.7520 | **+2.008** | **0.0446** | * |
| **Age (years)** | **-0.1499** | 0.0690 | ±0.1380 | **-2.172** | **0.0299** | * |
| BMI (kg/m2) | +0.1990 | 0.1106 | ±0.2212 | +1.800 | 0.0719 | . |
| Hypertension | +0.5368 | 1.4764 | ±2.9528 | +0.364 | 0.7162 |  |
| High cholesterol | +1.8924 | 1.3422 | ±2.6845 | +1.410 | 0.1586 |  |
| Kidney disease | -1.8337 | 1.7391 | ±3.4782 | -1.054 | 0.2917 |  |
| Circulatory disease | +0.0793 | 1.7116 | ±3.4233 | +0.046 | 0.9630 |  |
| Avg. daily range (mg/dL) | -0.0098 | 0.0173 | ±0.0346 | -0.564 | 0.5725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.0799**, Adj R² = **0.0631**, F-statistic = **4.76** (p = **1.91e-08**), Residual SE = **16.798** on **768** df, AIC = **6655.0**, BIC = **6725.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.6592** | 6.6878 | ±13.3757 | **+19.238** | **1.79e-82** | *** |
| Education: graduate level (vs college) | -1.4472 | 1.2468 | ±2.4935 | -1.161 | 0.2457 |  |
| **Education: high school or below (vs college)** | **+6.4897** | 2.2454 | ±4.4907 | **+2.890** | **0.0038** | ** |
| Site: UCSD (vs UAB) | +2.8968 | 1.7088 | ±3.4176 | +1.695 | 0.0900 | . |
| **Site: UW (vs UAB)** | **-3.2067** | 1.4383 | ±2.8766 | **-2.230** | **0.0258** | * |
| **Season: spring (vs autumn)** | **+3.6763** | 1.4990 | ±2.9981 | **+2.452** | **0.0142** | * |
| Season: summer (vs autumn) | +3.1077 | 1.6424 | ±3.2848 | +1.892 | 0.0585 | . |
| **Season: winter (vs autumn)** | **+3.9688** | 1.8424 | ±3.6849 | **+2.154** | **0.0312** | * |
| **Age (years)** | **-0.1568** | 0.0690 | ±0.1380 | **-2.272** | **0.0231** | * |
| **BMI (kg/m2)** | **+0.2320** | 0.1148 | ±0.2297 | **+2.020** | **0.0434** | * |
| Hypertension | +0.7718 | 1.4735 | ±2.9470 | +0.524 | 0.6004 |  |
| High cholesterol | +1.8768 | 1.3392 | ±2.6785 | +1.401 | 0.1611 |  |
| Kidney disease | -1.6470 | 1.7400 | ±3.4799 | -0.947 | 0.3439 |  |
| Circulatory disease | +0.3865 | 1.6833 | ±3.3667 | +0.230 | 0.8184 |  |
| SD of daily means (mg/dL) | -0.2075 | 0.1298 | ±0.2595 | -1.599 | 0.1098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.0756**, Adj R² = **0.0587**, F-statistic = **4.48** (p = **8.43e-08**), Residual SE = **16.838** on **768** df, AIC = **6658.7**, BIC = **6728.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.4185** | 7.0550 | ±14.1099 | **+17.352** | **1.90e-67** | *** |
| Education: graduate level (vs college) | -1.1862 | 1.2385 | ±2.4770 | -0.958 | 0.3382 |  |
| **Education: high school or below (vs college)** | **+6.7233** | 2.2847 | ±4.5695 | **+2.943** | **0.0033** | ** |
| Site: UCSD (vs UAB) | +2.8308 | 1.7075 | ±3.4150 | +1.658 | 0.0973 | . |
| **Site: UW (vs UAB)** | **-3.0746** | 1.4276 | ±2.8553 | **-2.154** | **0.0313** | * |
| **Season: spring (vs autumn)** | **+3.6523** | 1.4917 | ±2.9835 | **+2.448** | **0.0143** | * |
| Season: summer (vs autumn) | +3.0065 | 1.6561 | ±3.3121 | +1.815 | 0.0695 | . |
| **Season: winter (vs autumn)** | **+3.8297** | 1.8569 | ±3.7138 | **+2.062** | **0.0392** | * |
| **Age (years)** | **-0.1504** | 0.0695 | ±0.1390 | **-2.164** | **0.0305** | * |
| **BMI (kg/m2)** | **+0.2249** | 0.1100 | ±0.2200 | **+2.044** | **0.0409** | * |
| Hypertension | +0.5835 | 1.4787 | ±2.9574 | +0.395 | 0.6931 |  |
| High cholesterol | +1.9021 | 1.3433 | ±2.6866 | +1.416 | 0.1568 |  |
| Kidney disease | -1.7452 | 1.7444 | ±3.4888 | -1.000 | 0.3171 |  |
| Circulatory disease | +0.2098 | 1.7086 | ±3.4171 | +0.123 | 0.9023 |  |
| Time in range 70-180, pooled (%) | +0.0479 | 0.0279 | ±0.0557 | +1.720 | 0.0854 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.0759**, Adj R² = **0.0590**, F-statistic = **4.50** (p = **7.58e-08**), Residual SE = **16.835** on **768** df, AIC = **6658.4**, BIC = **6728.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2385** | 7.0485 | ±14.0969 | **+17.343** | **2.24e-67** | *** |
| Education: graduate level (vs college) | -1.1784 | 1.2396 | ±2.4791 | -0.951 | 0.3418 |  |
| **Education: high school or below (vs college)** | **+6.7482** | 2.2816 | ±4.5632 | **+2.958** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +2.8065 | 1.7087 | ±3.4174 | +1.642 | 0.1005 |  |
| **Site: UW (vs UAB)** | **-3.0888** | 1.4278 | ±2.8555 | **-2.163** | **0.0305** | * |
| **Season: spring (vs autumn)** | **+3.6670** | 1.4911 | ±2.9822 | **+2.459** | **0.0139** | * |
| Season: summer (vs autumn) | +3.0168 | 1.6543 | ±3.3085 | +1.824 | 0.0682 | . |
| **Season: winter (vs autumn)** | **+3.8477** | 1.8537 | ±3.7074 | **+2.076** | **0.0379** | * |
| **Age (years)** | **-0.1500** | 0.0695 | ±0.1390 | **-2.159** | **0.0308** | * |
| **BMI (kg/m2)** | **+0.2264** | 0.1099 | ±0.2198 | **+2.060** | **0.0394** | * |
| Hypertension | +0.5817 | 1.4787 | ±2.9573 | +0.393 | 0.6940 |  |
| High cholesterol | +1.9041 | 1.3432 | ±2.6865 | +1.418 | 0.1563 |  |
| Kidney disease | -1.7193 | 1.7424 | ±3.4848 | -0.987 | 0.3238 |  |
| Circulatory disease | +0.2131 | 1.7089 | ±3.4178 | +0.125 | 0.9007 |  |
| Avg. daily time in range 70-180 (%) | +0.0493 | 0.0277 | ±0.0554 | +1.780 | 0.0751 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.0713**, Adj R² = **0.0543**, F-statistic = **4.21** (p = **3.59e-07**), Residual SE = **16.877** on **768** df, AIC = **6662.4**, BIC = **6732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4771** | 6.4697 | ±12.9393 | **+19.549** | **4.18e-85** | *** |
| Education: graduate level (vs college) | -1.0604 | 1.2495 | ±2.4990 | -0.849 | 0.3961 |  |
| **Education: high school or below (vs college)** | **+6.3080** | 2.2600 | ±4.5199 | **+2.791** | **0.0053** | ** |
| Site: UCSD (vs UAB) | +3.1222 | 1.6937 | ±3.3874 | +1.843 | 0.0653 | . |
| **Site: UW (vs UAB)** | **-2.7823** | 1.4132 | ±2.8264 | **-1.969** | **0.0490** | * |
| **Season: spring (vs autumn)** | **+3.5542** | 1.4989 | ±2.9979 | **+2.371** | **0.0177** | * |
| Season: summer (vs autumn) | +3.1384 | 1.6486 | ±3.2971 | +1.904 | 0.0569 | . |
| **Season: winter (vs autumn)** | **+3.7899** | 1.8903 | ±3.7806 | **+2.005** | **0.0450** | * |
| **Age (years)** | **-0.1487** | 0.0682 | ±0.1364 | **-2.180** | **0.0292** | * |
| BMI (kg/m2) | +0.1953 | 0.1102 | ±0.2204 | +1.773 | 0.0763 | . |
| Hypertension | +0.5011 | 1.4734 | ±2.9468 | +0.340 | 0.7338 |  |
| High cholesterol | +1.9445 | 1.3594 | ±2.7187 | +1.430 | 0.1526 |  |
| Kidney disease | -2.0320 | 1.7284 | ±3.4569 | -1.176 | 0.2397 |  |
| Circulatory disease | +0.0149 | 1.7088 | ±3.4175 | +0.009 | 0.9930 |  |
| Any reading < 54 during wear (0/1) | +0.4040 | 1.6179 | ±3.2357 | +0.250 | 0.8028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.0719**, Adj R² = **0.0550**, F-statistic = **4.25** (p = **2.85e-07**), Residual SE = **16.871** on **768** df, AIC = **6661.8**, BIC = **6731.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8861** | 6.6885 | ±13.3771 | **+18.971** | **2.98e-80** | *** |
| Education: graduate level (vs college) | -1.1336 | 1.2528 | ±2.5057 | -0.905 | 0.3656 |  |
| **Education: high school or below (vs college)** | **+6.2069** | 2.2668 | ±4.5336 | **+2.738** | **0.0062** | ** |
| Site: UCSD (vs UAB) | +3.0135 | 1.7001 | ±3.4001 | +1.773 | 0.0763 | . |
| **Site: UW (vs UAB)** | **-2.9159** | 1.4379 | ±2.8759 | **-2.028** | **0.0426** | * |
| **Season: spring (vs autumn)** | **+3.5180** | 1.4981 | ±2.9962 | **+2.348** | **0.0189** | * |
| Season: summer (vs autumn) | +3.0782 | 1.6528 | ±3.3057 | +1.862 | 0.0626 | . |
| **Season: winter (vs autumn)** | **+3.7958** | 1.8783 | ±3.7566 | **+2.021** | **0.0433** | * |
| **Age (years)** | **-0.1475** | 0.0691 | ±0.1381 | **-2.137** | **0.0326** | * |
| BMI (kg/m2) | +0.1917 | 0.1098 | ±0.2195 | +1.747 | 0.0807 | . |
| Hypertension | +0.5255 | 1.4773 | ±2.9546 | +0.356 | 0.7221 |  |
| High cholesterol | +1.8279 | 1.3464 | ±2.6929 | +1.358 | 0.1746 |  |
| Kidney disease | -2.0301 | 1.7271 | ±3.4542 | -1.175 | 0.2398 |  |
| Circulatory disease | -0.0046 | 1.7105 | ±3.4210 | -0.003 | 0.9979 |  |
| Time < 54 (%) | -0.8603 | 1.3012 | ±2.6024 | -0.661 | 0.5085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.0720**, Adj R² = **0.0551**, F-statistic = **4.26** (p = **2.81e-07**), Residual SE = **16.870** on **768** df, AIC = **6661.7**, BIC = **6731.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8660** | 6.6877 | ±13.3754 | **+18.970** | **3.02e-80** | *** |
| Education: graduate level (vs college) | -1.1274 | 1.2526 | ±2.5052 | -0.900 | 0.3681 |  |
| **Education: high school or below (vs college)** | **+6.2009** | 2.2674 | ±4.5347 | **+2.735** | **0.0062** | ** |
| Site: UCSD (vs UAB) | +3.0090 | 1.7001 | ±3.4003 | +1.770 | 0.0767 | . |
| **Site: UW (vs UAB)** | **-2.9316** | 1.4386 | ±2.8771 | **-2.038** | **0.0416** | * |
| **Season: spring (vs autumn)** | **+3.4808** | 1.4982 | ±2.9964 | **+2.323** | **0.0202** | * |
| Season: summer (vs autumn) | +3.0413 | 1.6550 | ±3.3100 | +1.838 | 0.0661 | . |
| **Season: winter (vs autumn)** | **+3.7761** | 1.8752 | ±3.7505 | **+2.014** | **0.0440** | * |
| **Age (years)** | **-0.1476** | 0.0690 | ±0.1381 | **-2.139** | **0.0325** | * |
| BMI (kg/m2) | +0.1933 | 0.1097 | ±0.2193 | +1.763 | 0.0780 | . |
| Hypertension | +0.5325 | 1.4767 | ±2.9533 | +0.361 | 0.7184 |  |
| High cholesterol | +1.8132 | 1.3492 | ±2.6983 | +1.344 | 0.1790 |  |
| Kidney disease | -2.0087 | 1.7280 | ±3.4560 | -1.162 | 0.2451 |  |
| Circulatory disease | -0.0019 | 1.7104 | ±3.4208 | -0.001 | 0.9991 |  |
| Avg. daily time < 54 (%) | -1.0196 | 0.6930 | ±1.3860 | -1.471 | 0.1412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.0720**, Adj R² = **0.0551**, F-statistic = **4.26** (p = **2.81e-07**), Residual SE = **16.870** on **768** df, AIC = **6661.7**, BIC = **6731.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8829** | 6.6597 | ±13.3195 | **+19.052** | **6.29e-81** | *** |
| Education: graduate level (vs college) | -1.1407 | 1.2591 | ±2.5183 | -0.906 | 0.3650 |  |
| **Education: high school or below (vs college)** | **+6.2203** | 2.2661 | ±4.5321 | **+2.745** | **0.0061** | ** |
| Site: UCSD (vs UAB) | +2.9884 | 1.6967 | ±3.3933 | +1.761 | 0.0782 | . |
| **Site: UW (vs UAB)** | **-2.9326** | 1.4368 | ±2.8736 | **-2.041** | **0.0412** | * |
| **Season: spring (vs autumn)** | **+3.4777** | 1.4955 | ±2.9910 | **+2.325** | **0.0200** | * |
| Season: summer (vs autumn) | +3.0294 | 1.6465 | ±3.2930 | +1.840 | 0.0658 | . |
| **Season: winter (vs autumn)** | **+3.7251** | 1.8728 | ±3.7457 | **+1.989** | **0.0467** | * |
| **Age (years)** | **-0.1472** | 0.0693 | ±0.1385 | **-2.126** | **0.0335** | * |
| BMI (kg/m2) | +0.1958 | 0.1099 | ±0.2199 | +1.781 | 0.0749 | . |
| Hypertension | +0.5612 | 1.4729 | ±2.9459 | +0.381 | 0.7032 |  |
| High cholesterol | +1.7886 | 1.3607 | ±2.7214 | +1.314 | 0.1887 |  |
| Kidney disease | -1.9743 | 1.7298 | ±3.4597 | -1.141 | 0.2537 |  |
| Circulatory disease | -0.0284 | 1.7146 | ±3.4293 | -0.017 | 0.9868 |  |
| Time 54-69, pooled (%) | -0.4886 | 0.6255 | ±1.2511 | -0.781 | 0.4348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.0728**, Adj R² = **0.0559**, F-statistic = **4.30** (p = **2.18e-07**), Residual SE = **16.863** on **768** df, AIC = **6661.1**, BIC = **6731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9015** | 6.6664 | ±13.3329 | **+19.036** | **8.60e-81** | *** |
| Education: graduate level (vs college) | -1.1758 | 1.2581 | ±2.5163 | -0.935 | 0.3500 |  |
| **Education: high school or below (vs college)** | **+6.1875** | 2.2678 | ±4.5357 | **+2.728** | **0.0064** | ** |
| Site: UCSD (vs UAB) | +2.9430 | 1.6961 | ±3.3922 | +1.735 | 0.0827 | . |
| **Site: UW (vs UAB)** | **-3.0028** | 1.4367 | ±2.8735 | **-2.090** | **0.0366** | * |
| **Season: spring (vs autumn)** | **+3.4545** | 1.4945 | ±2.9890 | **+2.311** | **0.0208** | * |
| Season: summer (vs autumn) | +2.9977 | 1.6455 | ±3.2910 | +1.822 | 0.0685 | . |
| **Season: winter (vs autumn)** | **+3.7313** | 1.8725 | ±3.7451 | **+1.993** | **0.0463** | * |
| **Age (years)** | **-0.1459** | 0.0693 | ±0.1386 | **-2.105** | **0.0353** | * |
| BMI (kg/m2) | +0.1967 | 0.1101 | ±0.2202 | +1.787 | 0.0739 | . |
| Hypertension | +0.5775 | 1.4723 | ±2.9445 | +0.392 | 0.6949 |  |
| High cholesterol | +1.7329 | 1.3611 | ±2.7222 | +1.273 | 0.2030 |  |
| Kidney disease | -1.9630 | 1.7274 | ±3.4547 | -1.136 | 0.2558 |  |
| Circulatory disease | -0.0613 | 1.7121 | ±3.4243 | -0.036 | 0.9714 |  |
| Avg. daily time 54-69 (%) | -0.6477 | 0.5197 | ±1.0394 | -1.246 | 0.2127 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.0723**, Adj R² = **0.0553**, F-statistic = **4.27** (p = **2.57e-07**), Residual SE = **16.868** on **768** df, AIC = **6661.5**, BIC = **6731.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9701** | 6.6609 | ±13.3218 | **+19.062** | **5.23e-81** | *** |
| Education: graduate level (vs college) | -1.1610 | 1.2590 | ±2.5181 | -0.922 | 0.3565 |  |
| **Education: high school or below (vs college)** | **+6.1914** | 2.2664 | ±4.5328 | **+2.732** | **0.0063** | ** |
| Site: UCSD (vs UAB) | +2.9617 | 1.6986 | ±3.3971 | +1.744 | 0.0812 | . |
| **Site: UW (vs UAB)** | **-2.9685** | 1.4387 | ±2.8773 | **-2.063** | **0.0391** | * |
| **Season: spring (vs autumn)** | **+3.4723** | 1.4959 | ±2.9917 | **+2.321** | **0.0203** | * |
| Season: summer (vs autumn) | +3.0214 | 1.6480 | ±3.2960 | +1.833 | 0.0668 | . |
| **Season: winter (vs autumn)** | **+3.7470** | 1.8740 | ±3.7479 | **+2.000** | **0.0456** | * |
| **Age (years)** | **-0.1467** | 0.0693 | ±0.1385 | **-2.118** | **0.0342** | * |
| BMI (kg/m2) | +0.1939 | 0.1096 | ±0.2193 | +1.768 | 0.0770 | . |
| Hypertension | +0.5573 | 1.4734 | ±2.9468 | +0.378 | 0.7053 |  |
| High cholesterol | +1.7647 | 1.3577 | ±2.7154 | +1.300 | 0.1937 |  |
| Kidney disease | -1.9850 | 1.7290 | ±3.4579 | -1.148 | 0.2509 |  |
| Circulatory disease | -0.0383 | 1.7133 | ±3.4266 | -0.022 | 0.9822 |  |
| Time < 70 (%) | -0.4193 | 0.3908 | ±0.7817 | -1.073 | 0.2834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.0728**, Adj R² = **0.0559**, F-statistic = **4.31** (p = **2.16e-07**), Residual SE = **16.863** on **768** df, AIC = **6661.1**, BIC = **6731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9502** | 6.6671 | ±13.3341 | **+19.041** | **7.75e-81** | *** |
| Education: graduate level (vs college) | -1.1781 | 1.2575 | ±2.5150 | -0.937 | 0.3488 |  |
| **Education: high school or below (vs college)** | **+6.1698** | 2.2682 | ±4.5363 | **+2.720** | **0.0065** | ** |
| Site: UCSD (vs UAB) | +2.9359 | 1.6976 | ±3.3953 | +1.729 | 0.0837 | . |
| **Site: UW (vs UAB)** | **-3.0172** | 1.4388 | ±2.8776 | **-2.097** | **0.0360** | * |
| **Season: spring (vs autumn)** | **+3.4436** | 1.4951 | ±2.9902 | **+2.303** | **0.0213** | * |
| Season: summer (vs autumn) | +2.9882 | 1.6480 | ±3.2960 | +1.813 | 0.0698 | . |
| **Season: winter (vs autumn)** | **+3.7456** | 1.8730 | ±3.7460 | **+2.000** | **0.0455** | * |
| **Age (years)** | **-0.1459** | 0.0692 | ±0.1385 | **-2.107** | **0.0351** | * |
| BMI (kg/m2) | +0.1953 | 0.1098 | ±0.2196 | +1.779 | 0.0753 | . |
| Hypertension | +0.5694 | 1.4734 | ±2.9468 | +0.386 | 0.6992 |  |
| High cholesterol | +1.7272 | 1.3593 | ±2.7187 | +1.271 | 0.2039 |  |
| Kidney disease | -1.9705 | 1.7278 | ±3.4557 | -1.140 | 0.2541 |  |
| Circulatory disease | -0.0560 | 1.7118 | ±3.4235 | -0.033 | 0.9739 |  |
| Avg. daily time < 70 (%) | -0.4940 | 0.3423 | ±0.6846 | -1.443 | 0.1490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.0802**, Adj R² = **0.0634**, F-statistic = **4.78** (p = **1.74e-08**), Residual SE = **16.796** on **768** df, AIC = **6654.8**, BIC = **6724.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+117.5779** | 7.2659 | ±14.5317 | **+16.182** | **6.73e-59** | *** |
| Education: graduate level (vs college) | -1.3477 | 1.2448 | ±2.4896 | -1.083 | 0.2790 |  |
| **Education: high school or below (vs college)** | **+6.8480** | 2.2694 | ±4.5388 | **+3.018** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +2.7653 | 1.7123 | ±3.4246 | +1.615 | 0.1063 |  |
| **Site: UW (vs UAB)** | **-3.2342** | 1.4451 | ±2.8903 | **-2.238** | **0.0252** | * |
| **Season: spring (vs autumn)** | **+3.5768** | 1.5052 | ±3.0104 | **+2.376** | **0.0175** | * |
| Season: summer (vs autumn) | +2.7724 | 1.6709 | ±3.3417 | +1.659 | 0.0971 | . |
| **Season: winter (vs autumn)** | **+3.7624** | 1.8583 | ±3.7166 | **+2.025** | **0.0429** | * |
| **Age (years)** | **-0.1612** | 0.0695 | ±0.1391 | **-2.319** | **0.0204** | * |
| **BMI (kg/m2)** | **+0.2158** | 0.1086 | ±0.2172 | **+1.988** | **0.0469** | * |
| Hypertension | +0.6731 | 1.4649 | ±2.9297 | +0.460 | 0.6459 |  |
| High cholesterol | +1.8400 | 1.3363 | ±2.6726 | +1.377 | 0.1685 |  |
| Kidney disease | -1.7729 | 1.7255 | ±3.4510 | -1.027 | 0.3042 |  |
| Circulatory disease | +0.2923 | 1.7072 | ±3.4144 | +0.171 | 0.8641 |  |
| **Time 54-250, pooled (%)** | **+0.1023** | 0.0401 | ±0.0802 | **+2.552** | **0.0107** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.0807**, Adj R² = **0.0640**, F-statistic = **4.82** (p = **1.44e-08**), Residual SE = **16.791** on **768** df, AIC = **6654.3**, BIC = **6724.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+117.0630** | 7.2933 | ±14.5866 | **+16.051** | **5.65e-58** | *** |
| Education: graduate level (vs college) | -1.3505 | 1.2450 | ±2.4900 | -1.085 | 0.2780 |  |
| **Education: high school or below (vs college)** | **+6.8656** | 2.2657 | ±4.5314 | **+3.030** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +2.7500 | 1.7120 | ±3.4240 | +1.606 | 0.1082 |  |
| **Site: UW (vs UAB)** | **-3.2329** | 1.4432 | ±2.8865 | **-2.240** | **0.0251** | * |
| **Season: spring (vs autumn)** | **+3.5888** | 1.5052 | ±3.0104 | **+2.384** | **0.0171** | * |
| Season: summer (vs autumn) | +2.7813 | 1.6693 | ±3.3387 | +1.666 | 0.0957 | . |
| **Season: winter (vs autumn)** | **+3.7712** | 1.8571 | ±3.7142 | **+2.031** | **0.0423** | * |
| **Age (years)** | **-0.1602** | 0.0695 | ±0.1390 | **-2.305** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.2170** | 0.1083 | ±0.2166 | **+2.004** | **0.0451** | * |
| Hypertension | +0.6676 | 1.4650 | ±2.9301 | +0.456 | 0.6486 |  |
| High cholesterol | +1.8365 | 1.3361 | ±2.6722 | +1.375 | 0.1693 |  |
| Kidney disease | -1.7392 | 1.7232 | ±3.4464 | -1.009 | 0.3128 |  |
| Circulatory disease | +0.3145 | 1.7100 | ±3.4200 | +0.184 | 0.8541 |  |
| **Avg. daily time 54-250 (%)** | **+0.1065** | 0.0413 | ±0.0825 | **+2.580** | **0.0099** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0542**, F-statistic = **4.20** (p = **3.70e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6353** | 6.7183 | ±13.4365 | **+18.849** | **2.97e-79** | *** |
| Education: graduate level (vs college) | -1.0707 | 1.2564 | ±2.5127 | -0.852 | 0.3941 |  |
| **Education: high school or below (vs college)** | **+6.2962** | 2.2830 | ±4.5660 | **+2.758** | **0.0058** | ** |
| Site: UCSD (vs UAB) | +3.0948 | 1.6981 | ±3.3962 | +1.823 | 0.0684 | . |
| **Site: UW (vs UAB)** | **-2.8085** | 1.4273 | ±2.8546 | **-1.968** | **0.0491** | * |
| **Season: spring (vs autumn)** | **+3.5560** | 1.4923 | ±2.9846 | **+2.383** | **0.0172** | * |
| Season: summer (vs autumn) | +3.1250 | 1.6504 | ±3.3008 | +1.893 | 0.0583 | . |
| **Season: winter (vs autumn)** | **+3.7657** | 1.8527 | ±3.7055 | **+2.033** | **0.0421** | * |
| **Age (years)** | **-0.1491** | 0.0693 | ±0.1387 | **-2.150** | **0.0316** | * |
| BMI (kg/m2) | +0.1968 | 0.1120 | ±0.2239 | +1.758 | 0.0787 | . |
| Hypertension | +0.5212 | 1.4763 | ±2.9527 | +0.353 | 0.7241 |  |
| High cholesterol | +1.9154 | 1.3420 | ±2.6841 | +1.427 | 0.1535 |  |
| Kidney disease | -2.0125 | 1.7605 | ±3.5211 | -1.143 | 0.2530 |  |
| Circulatory disease | +0.0376 | 1.7093 | ±3.4187 | +0.022 | 0.9825 |  |
| Time 181-250, pooled (%) | -0.0029 | 0.0542 | ±0.1084 | -0.054 | 0.9567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0543**, F-statistic = **4.20** (p = **3.68e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6366** | 6.7189 | ±13.4378 | **+18.848** | **3.06e-79** | *** |
| Education: graduate level (vs college) | -1.0689 | 1.2577 | ±2.5153 | -0.850 | 0.3954 |  |
| **Education: high school or below (vs college)** | **+6.3055** | 2.2829 | ±4.5658 | **+2.762** | **0.0057** | ** |
| Site: UCSD (vs UAB) | +3.0889 | 1.7000 | ±3.4000 | +1.817 | 0.0692 | . |
| **Site: UW (vs UAB)** | **-2.8122** | 1.4266 | ±2.8532 | **-1.971** | **0.0487** | * |
| **Season: spring (vs autumn)** | **+3.5608** | 1.4921 | ±2.9843 | **+2.386** | **0.0170** | * |
| Season: summer (vs autumn) | +3.1277 | 1.6505 | ±3.3010 | +1.895 | 0.0581 | . |
| **Season: winter (vs autumn)** | **+3.7699** | 1.8500 | ±3.7001 | **+2.038** | **0.0416** | * |
| **Age (years)** | **-0.1489** | 0.0693 | ±0.1386 | **-2.148** | **0.0317** | * |
| BMI (kg/m2) | +0.1977 | 0.1122 | ±0.2243 | +1.763 | 0.0779 | . |
| Hypertension | +0.5208 | 1.4770 | ±2.9539 | +0.353 | 0.7244 |  |
| High cholesterol | +1.9173 | 1.3424 | ±2.6847 | +1.428 | 0.1532 |  |
| Kidney disease | -2.0051 | 1.7613 | ±3.5225 | -1.138 | 0.2549 |  |
| Circulatory disease | +0.0395 | 1.7085 | ±3.4170 | +0.023 | 0.9815 |  |
| Avg. daily time 181-250 (%) | -0.0050 | 0.0522 | ±0.1045 | -0.095 | 0.9240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.0753**, Adj R² = **0.0584**, F-statistic = **4.46** (p = **9.39e-08**), Residual SE = **16.841** on **768** df, AIC = **6659.0**, BIC = **6728.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1502** | 6.7376 | ±13.4751 | **+18.872** | **1.94e-79** | *** |
| Education: graduate level (vs college) | -1.1714 | 1.2395 | ±2.4791 | -0.945 | 0.3447 |  |
| **Education: high school or below (vs college)** | **+6.7140** | 2.2851 | ±4.5702 | **+2.938** | **0.0033** | ** |
| Site: UCSD (vs UAB) | +2.8581 | 1.7069 | ±3.4137 | +1.674 | 0.0940 | . |
| **Site: UW (vs UAB)** | **-3.0447** | 1.4279 | ±2.8558 | **-2.132** | **0.0330** | * |
| **Season: spring (vs autumn)** | **+3.6563** | 1.4914 | ±2.9828 | **+2.452** | **0.0142** | * |
| Season: summer (vs autumn) | +3.0225 | 1.6554 | ±3.3108 | +1.826 | 0.0679 | . |
| **Season: winter (vs autumn)** | **+3.8283** | 1.8573 | ±3.7145 | **+2.061** | **0.0393** | * |
| **Age (years)** | **-0.1506** | 0.0695 | ±0.1390 | **-2.167** | **0.0302** | * |
| **BMI (kg/m2)** | **+0.2238** | 0.1100 | ±0.2199 | **+2.035** | **0.0418** | * |
| Hypertension | +0.5769 | 1.4787 | ±2.9575 | +0.390 | 0.6964 |  |
| High cholesterol | +1.9189 | 1.3434 | ±2.6869 | +1.428 | 0.1532 |  |
| Kidney disease | -1.7616 | 1.7434 | ±3.4869 | -1.010 | 0.3123 |  |
| Circulatory disease | +0.2098 | 1.7082 | ±3.4165 | +0.123 | 0.9022 |  |
| Time > 180 (%) | -0.0458 | 0.0277 | ±0.0554 | -1.654 | 0.0980 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.0755**, Adj R² = **0.0587**, F-statistic = **4.48** (p = **8.62e-08**), Residual SE = **16.838** on **768** df, AIC = **6658.8**, BIC = **6728.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1119** | 6.7362 | ±13.4724 | **+18.870** | **2.01e-79** | *** |
| Education: graduate level (vs college) | -1.1632 | 1.2406 | ±2.4812 | -0.938 | 0.3484 |  |
| **Education: high school or below (vs college)** | **+6.7368** | 2.2825 | ±4.5651 | **+2.951** | **0.0032** | ** |
| Site: UCSD (vs UAB) | +2.8364 | 1.7081 | ±3.4161 | +1.661 | 0.0968 | . |
| **Site: UW (vs UAB)** | **-3.0550** | 1.4279 | ±2.8559 | **-2.139** | **0.0324** | * |
| **Season: spring (vs autumn)** | **+3.6715** | 1.4909 | ±2.9818 | **+2.463** | **0.0138** | * |
| Season: summer (vs autumn) | +3.0345 | 1.6537 | ±3.3074 | +1.835 | 0.0665 | . |
| **Season: winter (vs autumn)** | **+3.8450** | 1.8542 | ±3.7084 | **+2.074** | **0.0381** | * |
| **Age (years)** | **-0.1503** | 0.0695 | ±0.1390 | **-2.163** | **0.0305** | * |
| **BMI (kg/m2)** | **+0.2249** | 0.1098 | ±0.2196 | **+2.048** | **0.0405** | * |
| Hypertension | +0.5743 | 1.4787 | ±2.9573 | +0.388 | 0.6977 |  |
| High cholesterol | +1.9222 | 1.3436 | ±2.6871 | +1.431 | 0.1525 |  |
| Kidney disease | -1.7388 | 1.7416 | ±3.4832 | -0.998 | 0.3181 |  |
| Circulatory disease | +0.2130 | 1.7086 | ±3.4171 | +0.125 | 0.9008 |  |
| Avg. daily time > 180 (%) | -0.0469 | 0.0275 | ±0.0551 | -1.703 | 0.0886 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.0731**, Adj R² = **0.0562**, F-statistic = **4.33** (p = **1.94e-07**), Residual SE = **16.860** on **768** df, AIC = **6660.8**, BIC = **6730.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8379** | 6.7435 | ±13.4869 | **+18.809** | **6.37e-79** | *** |
| Education: graduate level (vs college) | -1.2000 | 1.2336 | ±2.4673 | -0.973 | 0.3307 |  |
| **Education: high school or below (vs college)** | **+6.5269** | 2.2746 | ±4.5492 | **+2.869** | **0.0041** | ** |
| Site: UCSD (vs UAB) | +2.9257 | 1.7140 | ±3.4281 | +1.707 | 0.0878 | . |
| **Site: UW (vs UAB)** | **-2.9277** | 1.4247 | ±2.8494 | **-2.055** | **0.0399** | * |
| **Season: spring (vs autumn)** | **+3.6496** | 1.4896 | ±2.9791 | **+2.450** | **0.0143** | * |
| Season: summer (vs autumn) | +3.0396 | 1.6595 | ±3.3191 | +1.832 | 0.0670 | . |
| **Season: winter (vs autumn)** | **+3.8297** | 1.8529 | ±3.7057 | **+2.067** | **0.0387** | * |
| **Age (years)** | **-0.1532** | 0.0699 | ±0.1398 | **-2.193** | **0.0283** | * |
| **BMI (kg/m2)** | **+0.2190** | 0.1099 | ±0.2198 | **+1.992** | **0.0463** | * |
| Hypertension | +0.5370 | 1.4796 | ±2.9591 | +0.363 | 0.7166 |  |
| High cholesterol | +1.9009 | 1.3450 | ±2.6900 | +1.413 | 0.1576 |  |
| Kidney disease | -1.9075 | 1.7423 | ±3.4846 | -1.095 | 0.2736 |  |
| Circulatory disease | +0.1419 | 1.7048 | ±3.4097 | +0.083 | 0.9337 |  |
| Nocturnal time > 180 (%) | -0.0287 | 0.0281 | ±0.0561 | -1.022 | 0.3069 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.0800**, Adj R² = **0.0632**, F-statistic = **4.77** (p = **1.86e-08**), Residual SE = **16.798** on **768** df, AIC = **6655.0**, BIC = **6724.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7648** | 6.7096 | ±13.4192 | **+19.042** | **7.63e-81** | *** |
| Education: graduate level (vs college) | -1.3374 | 1.2449 | ±2.4897 | -1.074 | 0.2827 |  |
| **Education: high school or below (vs college)** | **+6.8508** | 2.2699 | ±4.5399 | **+3.018** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +2.7794 | 1.7117 | ±3.4234 | +1.624 | 0.1044 |  |
| **Site: UW (vs UAB)** | **-3.2163** | 1.4444 | ±2.8887 | **-2.227** | **0.0260** | * |
| **Season: spring (vs autumn)** | **+3.5802** | 1.5050 | ±3.0100 | **+2.379** | **0.0174** | * |
| Season: summer (vs autumn) | +2.7815 | 1.6704 | ±3.3408 | +1.665 | 0.0959 | . |
| **Season: winter (vs autumn)** | **+3.7583** | 1.8589 | ±3.7177 | **+2.022** | **0.0432** | * |
| **Age (years)** | **-0.1613** | 0.0695 | ±0.1391 | **-2.319** | **0.0204** | * |
| **BMI (kg/m2)** | **+0.2161** | 0.1086 | ±0.2173 | **+1.989** | **0.0467** | * |
| Hypertension | +0.6710 | 1.4651 | ±2.9302 | +0.458 | 0.6470 |  |
| High cholesterol | +1.8509 | 1.3368 | ±2.6737 | +1.385 | 0.1662 |  |
| Kidney disease | -1.7748 | 1.7252 | ±3.4504 | -1.029 | 0.3036 |  |
| Circulatory disease | +0.2939 | 1.7071 | ±3.4141 | +0.172 | 0.8633 |  |
| **Time > 250 (%)** | **-0.1011** | 0.0401 | ±0.0802 | **-2.522** | **0.0117** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.0805**, Adj R² = **0.0638**, F-statistic = **4.81** (p = **1.53e-08**), Residual SE = **16.792** on **768** df, AIC = **6654.5**, BIC = **6724.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.6751** | 6.7025 | ±13.4049 | **+19.049** | **6.70e-81** | *** |
| Education: graduate level (vs college) | -1.3420 | 1.2450 | ±2.4901 | -1.078 | 0.2811 |  |
| **Education: high school or below (vs college)** | **+6.8686** | 2.2663 | ±4.5327 | **+3.031** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +2.7630 | 1.7115 | ±3.4229 | +1.614 | 0.1064 |  |
| **Site: UW (vs UAB)** | **-3.2156** | 1.4425 | ±2.8851 | **-2.229** | **0.0258** | * |
| **Season: spring (vs autumn)** | **+3.5956** | 1.5049 | ±3.0099 | **+2.389** | **0.0169** | * |
| Season: summer (vs autumn) | +2.7930 | 1.6686 | ±3.3372 | +1.674 | 0.0942 | . |
| **Season: winter (vs autumn)** | **+3.7696** | 1.8576 | ±3.7152 | **+2.029** | **0.0424** | * |
| **Age (years)** | **-0.1603** | 0.0695 | ±0.1390 | **-2.306** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.2171** | 0.1083 | ±0.2166 | **+2.004** | **0.0451** | * |
| Hypertension | +0.6651 | 1.4652 | ±2.9305 | +0.454 | 0.6499 |  |
| High cholesterol | +1.8476 | 1.3367 | ±2.6733 | +1.382 | 0.1669 |  |
| Kidney disease | -1.7433 | 1.7229 | ±3.4458 | -1.012 | 0.3116 |  |
| Circulatory disease | +0.3155 | 1.7099 | ±3.4197 | +0.184 | 0.8536 |  |
| **Avg. daily time > 250 (%)** | **-0.1054** | 0.0413 | ±0.0826 | **-2.553** | **0.0107** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 690; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1535**, F-statistic = **13.49** (p = **8.56e-22**), Residual SE = **4604.077** on **679** df, AIC = **13608.9**, BIC = **13658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21543.0182** | 1500.7933 | ±3001.5866 | **+14.354** | **1.00e-46** | *** |
| Education: graduate level (vs college) | -47.3197 | 379.6187 | ±759.2373 | -0.125 | 0.9008 |  |
| Education: high school or below (vs college) | +1058.8636 | 632.8681 | ±1265.7361 | +1.673 | 0.0943 | . |
| Site: UCSD (vs UAB) | +664.8012 | 487.0980 | ±974.1960 | +1.365 | 0.1723 |  |
| Site: UW (vs UAB) | +15.2514 | 425.2723 | ±850.5446 | +0.036 | 0.9714 |  |
| **Age (years)** | **-160.2026** | 16.4631 | ±32.9261 | **-9.731** | **2.22e-22** | *** |
| BMI (kg/m2) | -48.4338 | 29.0686 | ±58.1372 | -1.666 | 0.0957 | . |
| Hypertension | -269.6488 | 389.9338 | ±779.8676 | -0.692 | 0.4892 |  |
| High cholesterol | +299.9184 | 379.0434 | ±758.0868 | +0.791 | 0.4288 |  |
| **Kidney disease** | **-1290.2472** | 467.0888 | ±934.1775 | **-2.762** | **0.0057** | ** |
| **Circulatory disease** | **-1425.6425** | 440.6012 | ±881.2023 | **-3.236** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **690**, R² = **0.1707**, Adj R² = **0.1573**, F-statistic = **12.69** (p = **4.98e-22**), Residual SE = **4593.856** on **678** df, AIC = **13606.8**, BIC = **13661.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20000.5328** | 1672.3985 | ±3344.7970 | **+11.959** | **5.81e-33** | *** |
| Education: graduate level (vs college) | +17.1653 | 384.1704 | ±768.3408 | +0.045 | 0.9644 |  |
| Education: high school or below (vs college) | +933.9534 | 631.2671 | ±1262.5342 | +1.479 | 0.1390 |  |
| Site: UCSD (vs UAB) | +694.0932 | 486.6987 | ±973.3975 | +1.426 | 0.1538 |  |
| Site: UW (vs UAB) | +83.8873 | 422.6922 | ±845.3843 | +0.198 | 0.8427 |  |
| **Age (years)** | **-159.9177** | 16.3840 | ±32.7680 | **-9.761** | **1.66e-22** | *** |
| **BMI (kg/m2)** | **-58.5668** | 29.6548 | ±59.3096 | **-1.975** | **0.0483** | * |
| Hypertension | -313.4526 | 391.6305 | ±783.2609 | -0.800 | 0.4235 |  |
| High cholesterol | +283.7085 | 379.0696 | ±758.1393 | +0.748 | 0.4542 |  |
| **Kidney disease** | **-1275.4091** | 466.6248 | ±933.2496 | **-2.733** | **0.0063** | ** |
| **Circulatory disease** | **-1457.7345** | 442.0612 | ±884.1224 | **-3.298** | **9.75e-04** | *** |
| HbA1c (%) | +270.4922 | 154.9667 | ±309.9334 | +1.745 | 0.0809 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **690**, R² = **0.1667**, Adj R² = **0.1532**, F-statistic = **12.33** (p = **2.29e-21**), Residual SE = **4604.936** on **678** df, AIC = **13610.2**, BIC = **13664.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21006.2131** | 1588.2194 | ±3176.4389 | **+13.226** | **6.19e-40** | *** |
| Education: graduate level (vs college) | -31.6708 | 383.0422 | ±766.0844 | -0.083 | 0.9341 |  |
| Education: high school or below (vs college) | +1007.9318 | 628.3307 | ±1256.6614 | +1.604 | 0.1087 |  |
| Site: UCSD (vs UAB) | +685.1824 | 485.4473 | ±970.8946 | +1.411 | 0.1581 |  |
| Site: UW (vs UAB) | +41.6325 | 423.5810 | ±847.1620 | +0.098 | 0.9217 |  |
| **Age (years)** | **-159.8568** | 16.4221 | ±32.8442 | **-9.734** | **2.15e-22** | *** |
| BMI (kg/m2) | -52.3256 | 29.4520 | ±58.9040 | -1.777 | 0.0756 | . |
| Hypertension | -282.3796 | 391.4612 | ±782.9224 | -0.721 | 0.4707 |  |
| High cholesterol | +301.8208 | 379.8386 | ±759.6771 | +0.795 | 0.4268 |  |
| **Kidney disease** | **-1309.3741** | 470.8464 | ±941.6928 | **-2.781** | **0.0054** | ** |
| **Circulatory disease** | **-1456.2670** | 443.8650 | ±887.7300 | **-3.281** | **0.0010** | ** |
| Mean glucose (mg/dL) | +3.9347 | 5.2623 | ±10.5246 | +0.748 | 0.4546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **690**, R² = **0.1667**, Adj R² = **0.1532**, F-statistic = **12.33** (p = **2.29e-21**), Residual SE = **4604.936** on **678** df, AIC = **13610.2**, BIC = **13664.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20461.7339** | 1960.4944 | ±3920.9888 | **+10.437** | **1.68e-25** | *** |
| Education: graduate level (vs college) | -31.6708 | 383.0422 | ±766.0844 | -0.083 | 0.9341 |  |
| Education: high school or below (vs college) | +1007.9318 | 628.3307 | ±1256.6614 | +1.604 | 0.1087 |  |
| Site: UCSD (vs UAB) | +685.1824 | 485.4473 | ±970.8946 | +1.411 | 0.1581 |  |
| Site: UW (vs UAB) | +41.6325 | 423.5810 | ±847.1620 | +0.098 | 0.9217 |  |
| **Age (years)** | **-159.8568** | 16.4221 | ±32.8442 | **-9.734** | **2.15e-22** | *** |
| BMI (kg/m2) | -52.3256 | 29.4520 | ±58.9040 | -1.777 | 0.0756 | . |
| Hypertension | -282.3796 | 391.4612 | ±782.9224 | -0.721 | 0.4707 |  |
| High cholesterol | +301.8208 | 379.8386 | ±759.6771 | +0.795 | 0.4268 |  |
| **Kidney disease** | **-1309.3741** | 470.8464 | ±941.6928 | **-2.781** | **0.0054** | ** |
| **Circulatory disease** | **-1456.2670** | 443.8650 | ±887.7300 | **-3.281** | **0.0010** | ** |
| GMI (%) | +164.4952 | 219.9950 | ±439.9900 | +0.748 | 0.4546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **690**, R² = **0.1684**, Adj R² = **0.1549**, F-statistic = **12.48** (p = **1.21e-21**), Residual SE = **4600.289** on **678** df, AIC = **13608.8**, BIC = **13663.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20721.6256** | 1582.4176 | ±3164.8353 | **+13.095** | **3.52e-39** | *** |
| Education: graduate level (vs college) | -13.7794 | 384.1674 | ±768.3347 | -0.036 | 0.9714 |  |
| Education: high school or below (vs college) | +978.9994 | 626.6794 | ±1253.3588 | +1.562 | 0.1182 |  |
| Site: UCSD (vs UAB) | +695.4477 | 484.7585 | ±969.5169 | +1.435 | 0.1514 |  |
| Site: UW (vs UAB) | +45.1378 | 423.1643 | ±846.3287 | +0.107 | 0.9151 |  |
| **Age (years)** | **-158.7886** | 16.3715 | ±32.7431 | **-9.699** | **3.04e-22** | *** |
| BMI (kg/m2) | -56.4472 | 29.5854 | ±59.1708 | -1.908 | 0.0564 | . |
| Hypertension | -287.1270 | 391.4074 | ±782.8148 | -0.734 | 0.4632 |  |
| High cholesterol | +309.3549 | 379.7470 | ±759.4940 | +0.815 | 0.4153 |  |
| **Kidney disease** | **-1293.0693** | 469.3785 | ±938.7569 | **-2.755** | **0.0059** | ** |
| **Circulatory disease** | **-1475.4615** | 443.6421 | ±887.2843 | **-3.326** | **8.82e-04** | *** |
| Nocturnal mean 00-06h (mg/dL) | +6.2791 | 5.1316 | ±10.2632 | +1.224 | 0.2211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1659**, Adj R² = **0.1524**, F-statistic = **12.26** (p = **3.10e-21**), Residual SE = **4607.124** on **678** df, AIC = **13610.8**, BIC = **13665.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21394.7271** | 1522.1778 | ±3044.3555 | **+14.055** | **7.14e-45** | *** |
| Education: graduate level (vs college) | -38.8706 | 385.5182 | ±771.0364 | -0.101 | 0.9197 |  |
| Education: high school or below (vs college) | +1042.2130 | 630.1985 | ±1260.3970 | +1.654 | 0.0982 | . |
| Site: UCSD (vs UAB) | +676.3856 | 482.6809 | ±965.3618 | +1.401 | 0.1611 |  |
| Site: UW (vs UAB) | +34.7989 | 421.7594 | ±843.5188 | +0.083 | 0.9342 |  |
| **Age (years)** | **-160.3468** | 16.5758 | ±33.1517 | **-9.674** | **3.91e-22** | *** |
| BMI (kg/m2) | -49.4899 | 29.4272 | ±58.8544 | -1.682 | 0.0926 | . |
| Hypertension | -277.3797 | 392.4702 | ±784.9405 | -0.707 | 0.4797 |  |
| High cholesterol | +304.2682 | 379.9137 | ±759.8274 | +0.801 | 0.4232 |  |
| **Kidney disease** | **-1318.6626** | 484.3868 | ±968.7736 | **-2.722** | **0.0065** | ** |
| **Circulatory disease** | **-1433.5466** | 443.5360 | ±887.0721 | **-3.232** | **0.0012** | ** |
| Glucose SD, pooled (mg/dL) | +4.9212 | 17.3196 | ±34.6393 | +0.284 | 0.7763 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.469** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21529.7268** | 1528.6432 | ±3057.2864 | **+14.084** | **4.75e-45** | *** |
| Education: graduate level (vs college) | -46.7309 | 383.2719 | ±766.5439 | -0.122 | 0.9030 |  |
| Education: high school or below (vs college) | +1057.2653 | 633.5457 | ±1267.0914 | +1.669 | 0.0952 | . |
| Site: UCSD (vs UAB) | +665.8026 | 482.1618 | ±964.3236 | +1.381 | 0.1673 |  |
| Site: UW (vs UAB) | +16.8037 | 421.6039 | ±843.2078 | +0.040 | 0.9682 |  |
| **Age (years)** | **-160.2211** | 16.5924 | ±33.1848 | **-9.656** | **4.62e-22** | *** |
| BMI (kg/m2) | -48.4991 | 29.2378 | ±58.4755 | -1.659 | 0.0972 | . |
| Hypertension | -270.2653 | 392.4272 | ±784.8545 | -0.689 | 0.4910 |  |
| High cholesterol | +300.2521 | 379.5500 | ±759.1001 | +0.791 | 0.4289 |  |
| **Kidney disease** | **-1292.8768** | 484.0962 | ±968.1924 | **-2.671** | **0.0076** | ** |
| **Circulatory disease** | **-1426.2473** | 442.5686 | ±885.1372 | **-3.223** | **0.0013** | ** |
| Avg. daily SD (mg/dL) | +0.4803 | 18.5898 | ±37.1796 | +0.026 | 0.9794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **690**, R² = **0.1666**, Adj R² = **0.1530**, F-statistic = **12.32** (p = **2.43e-21**), Residual SE = **4605.356** on **678** df, AIC = **13610.3**, BIC = **13664.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22128.8116** | 1624.3208 | ±3248.6416 | **+13.623** | **2.91e-42** | *** |
| Education: graduate level (vs college) | -63.2611 | 381.5556 | ±763.1111 | -0.166 | 0.8683 |  |
| Education: high school or below (vs college) | +1069.1705 | 632.7412 | ±1265.4824 | +1.690 | 0.0911 | . |
| Site: UCSD (vs UAB) | +639.7637 | 485.4058 | ±970.8117 | +1.318 | 0.1875 |  |
| Site: UW (vs UAB) | -27.0008 | 425.5256 | ±851.0513 | -0.063 | 0.9494 |  |
| **Age (years)** | **-159.3871** | 16.5263 | ±33.0525 | **-9.644** | **5.19e-22** | *** |
| BMI (kg/m2) | -48.5075 | 28.9821 | ±57.9642 | -1.674 | 0.0942 | . |
| Hypertension | -254.5364 | 391.1636 | ±782.3271 | -0.651 | 0.5152 |  |
| High cholesterol | +284.2147 | 379.3046 | ±758.6091 | +0.749 | 0.4537 |  |
| **Kidney disease** | **-1216.3418** | 477.0439 | ±954.0877 | **-2.550** | **0.0108** | * |
| **Circulatory disease** | **-1429.5475** | 440.6297 | ±881.2593 | **-3.244** | **0.0012** | ** |
| CV (%) | -26.2244 | 30.8152 | ±61.6304 | -0.851 | 0.3948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.21e-21**), Residual SE = **4607.367** on **678** df, AIC = **13610.9**, BIC = **13665.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21689.4298** | 1739.6366 | ±3479.2733 | **+12.468** | **1.12e-35** | *** |
| Education: graduate level (vs college) | -44.4389 | 380.9653 | ±761.9306 | -0.117 | 0.9071 |  |
| Education: high school or below (vs college) | +1056.9223 | 633.6817 | ±1267.3634 | +1.668 | 0.0953 | . |
| Site: UCSD (vs UAB) | +668.2296 | 485.7892 | ±971.5784 | +1.376 | 0.1690 |  |
| Site: UW (vs UAB) | +23.1571 | 423.8337 | ±847.6673 | +0.055 | 0.9564 |  |
| **Age (years)** | **-160.3455** | 16.5028 | ±33.0056 | **-9.716** | **2.57e-22** | *** |
| BMI (kg/m2) | -48.3512 | 29.1146 | ±58.2293 | -1.661 | 0.0968 | . |
| Hypertension | -273.0011 | 391.3782 | ±782.7564 | -0.698 | 0.4855 |  |
| High cholesterol | +301.4258 | 379.0118 | ±758.0236 | +0.795 | 0.4264 |  |
| **Kidney disease** | **-1304.5452** | 476.4126 | ±952.8252 | **-2.738** | **0.0062** | ** |
| **Circulatory disease** | **-1426.2471** | 441.1101 | ±882.2203 | **-3.233** | **0.0012** | ** |
| Mean / SD ratio | -31.6650 | 164.3227 | ±328.6455 | -0.193 | 0.8472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1660**, Adj R² = **0.1525**, F-statistic = **12.27** (p = **2.99e-21**), Residual SE = **4606.865** on **678** df, AIC = **13610.7**, BIC = **13665.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21872.4623** | 1695.4211 | ±3390.8422 | **+12.901** | **4.45e-38** | *** |
| Education: graduate level (vs college) | -42.2616 | 379.6514 | ±759.3028 | -0.111 | 0.9114 |  |
| Education: high school or below (vs college) | +1053.1010 | 635.2944 | ±1270.5888 | +1.658 | 0.0974 | . |
| Site: UCSD (vs UAB) | +671.1360 | 486.4048 | ±972.8096 | +1.380 | 0.1677 |  |
| Site: UW (vs UAB) | +32.1965 | 423.6089 | ±847.2178 | +0.076 | 0.9394 |  |
| **Age (years)** | **-160.6887** | 16.4909 | ±32.9818 | **-9.744** | **1.96e-22** | *** |
| BMI (kg/m2) | -47.8419 | 29.1118 | ±58.2236 | -1.643 | 0.1003 |  |
| Hypertension | -277.8491 | 390.8171 | ±781.6341 | -0.711 | 0.4771 |  |
| High cholesterol | +304.9979 | 378.9854 | ±757.9708 | +0.805 | 0.4209 |  |
| **Kidney disease** | **-1322.3025** | 473.1716 | ±946.3431 | **-2.795** | **0.0052** | ** |
| **Circulatory disease** | **-1423.9662** | 440.7785 | ±881.5570 | **-3.231** | **0.0012** | ** |
| Avg. daily mean/SD | -61.3099 | 129.6089 | ±259.2179 | -0.473 | 0.6362 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **690**, R² = **0.1703**, Adj R² = **0.1568**, F-statistic = **12.65** (p = **5.91e-22**), Residual SE = **4595.101** on **678** df, AIC = **13607.2**, BIC = **13661.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19696.3304** | 1799.5226 | ±3599.0452 | **+10.945** | **7.00e-28** | *** |
| Education: graduate level (vs college) | +7.1941 | 381.5395 | ±763.0790 | +0.019 | 0.9850 |  |
| Education: high school or below (vs college) | +1021.4258 | 629.1415 | ±1258.2830 | +1.624 | 0.1045 |  |
| Site: UCSD (vs UAB) | +751.5406 | 489.4807 | ±978.9613 | +1.535 | 0.1247 |  |
| Site: UW (vs UAB) | +153.2053 | 425.0915 | ±850.1829 | +0.360 | 0.7185 |  |
| **Age (years)** | **-157.7646** | 16.3034 | ±32.6067 | **-9.677** | **3.78e-22** | *** |
| BMI (kg/m2) | -49.7299 | 29.0299 | ±58.0598 | -1.713 | 0.0867 | . |
| Hypertension | -248.6170 | 390.1754 | ±780.3507 | -0.637 | 0.5240 |  |
| High cholesterol | +346.9125 | 382.5457 | ±765.0915 | +0.907 | 0.3645 |  |
| **Kidney disease** | **-1365.8487** | 468.7044 | ±937.4087 | **-2.914** | **0.0036** | ** |
| **Circulatory disease** | **-1434.7615** | 440.2083 | ±880.4165 | **-3.259** | **0.0011** | ** |
| MAG (mg/dL/h) | +35.8123 | 21.1825 | ±42.3649 | +1.691 | 0.0909 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.19e-21**), Residual SE = **4607.332** on **678** df, AIC = **13610.9**, BIC = **13665.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21390.3432** | 1638.2427 | ±3276.4854 | **+13.057** | **5.81e-39** | *** |
| Education: graduate level (vs college) | -43.3228 | 382.2617 | ±764.5235 | -0.113 | 0.9098 |  |
| Education: high school or below (vs college) | +1046.8805 | 633.9924 | ±1267.9848 | +1.651 | 0.0987 | . |
| Site: UCSD (vs UAB) | +673.7281 | 482.7165 | ±965.4330 | +1.396 | 0.1628 |  |
| Site: UW (vs UAB) | +27.3518 | 422.6918 | ±845.3836 | +0.065 | 0.9484 |  |
| **Age (years)** | **-160.2019** | 16.4929 | ±32.9858 | **-9.713** | **2.64e-22** | *** |
| BMI (kg/m2) | -48.7248 | 29.1512 | ±58.3024 | -1.671 | 0.0946 | . |
| Hypertension | -271.3801 | 391.5158 | ±783.0317 | -0.693 | 0.4882 |  |
| High cholesterol | +302.8575 | 379.5215 | ±759.0431 | +0.798 | 0.4249 |  |
| **Kidney disease** | **-1309.3552** | 480.0665 | ±960.1329 | **-2.727** | **0.0064** | ** |
| **Circulatory disease** | **-1429.6168** | 442.3751 | ±884.7503 | **-3.232** | **0.0012** | ** |
| Avg. daily range (mg/dL) | +1.0464 | 5.4457 | ±10.8914 | +0.192 | 0.8476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **690**, R² = **0.1686**, Adj R² = **0.1552**, F-statistic = **12.50** (p = **1.10e-21**), Residual SE = **4599.598** on **678** df, AIC = **13608.6**, BIC = **13663.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21216.5687** | 1494.5111 | ±2989.0223 | **+14.196** | **9.65e-46** | *** |
| Education: graduate level (vs college) | +8.3989 | 391.8855 | ±783.7711 | +0.021 | 0.9829 |  |
| Education: high school or below (vs college) | +1029.2665 | 628.5590 | ±1257.1179 | +1.638 | 0.1015 |  |
| Site: UCSD (vs UAB) | +694.0621 | 486.4465 | ±972.8931 | +1.427 | 0.1536 |  |
| Site: UW (vs UAB) | +83.4958 | 423.7099 | ±847.4198 | +0.197 | 0.8438 |  |
| **Age (years)** | **-159.1699** | 16.3509 | ±32.7018 | **-9.735** | **2.15e-22** | *** |
| BMI (kg/m2) | -54.7497 | 29.4681 | ±58.9363 | -1.858 | 0.0632 | . |
| Hypertension | -312.9617 | 391.1188 | ±782.2377 | -0.800 | 0.4236 |  |
| High cholesterol | +316.1738 | 378.8160 | ±757.6319 | +0.835 | 0.4039 |  |
| **Kidney disease** | **-1330.5716** | 471.6328 | ±943.2656 | **-2.821** | **0.0048** | ** |
| **Circulatory disease** | **-1481.2720** | 445.7988 | ±891.5976 | **-3.323** | **8.91e-04** | *** |
| SD of daily means (mg/dL) | +34.2837 | 26.7847 | ±53.5695 | +1.280 | 0.2006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **690**, R² = **0.1668**, Adj R² = **0.1533**, F-statistic = **12.34** (p = **2.20e-21**), Residual SE = **4604.641** on **678** df, AIC = **13610.1**, BIC = **13664.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22158.5494** | 1751.6401 | ±3503.2802 | **+12.650** | **1.12e-36** | *** |
| Education: graduate level (vs college) | -28.8198 | 383.9622 | ±767.9244 | -0.075 | 0.9402 |  |
| Education: high school or below (vs college) | +1005.6737 | 627.4300 | ±1254.8599 | +1.603 | 0.1090 |  |
| Site: UCSD (vs UAB) | +695.5087 | 484.6706 | ±969.3412 | +1.435 | 0.1513 |  |
| Site: UW (vs UAB) | +50.9305 | 424.5983 | ±849.1966 | +0.120 | 0.9045 |  |
| **Age (years)** | **-160.2004** | 16.4914 | ±32.9828 | **-9.714** | **2.62e-22** | *** |
| BMI (kg/m2) | -53.1762 | 29.4112 | ±58.8225 | -1.808 | 0.0706 | . |
| Hypertension | -280.4042 | 391.3927 | ±782.7854 | -0.716 | 0.4737 |  |
| High cholesterol | +309.8068 | 379.7726 | ±759.5451 | +0.816 | 0.4146 |  |
| **Kidney disease** | **-1320.1825** | 474.0132 | ±948.0265 | **-2.785** | **0.0054** | ** |
| **Circulatory disease** | **-1456.1877** | 441.8429 | ±883.6857 | **-3.296** | **9.82e-04** | *** |
| Time in range 70-180, pooled (%) | -6.7079 | 8.5178 | ±17.0356 | -0.788 | 0.4310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **690**, R² = **0.1667**, Adj R² = **0.1532**, F-statistic = **12.33** (p = **2.27e-21**), Residual SE = **4604.843** on **678** df, AIC = **13610.1**, BIC = **13664.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22140.4149** | 1754.5811 | ±3509.1621 | **+12.619** | **1.67e-36** | *** |
| Education: graduate level (vs college) | -31.2357 | 383.5740 | ±767.1481 | -0.081 | 0.9351 |  |
| Education: high school or below (vs college) | +1006.1430 | 627.1516 | ±1254.3033 | +1.604 | 0.1086 |  |
| Site: UCSD (vs UAB) | +696.6150 | 484.3411 | ±968.6823 | +1.438 | 0.1504 |  |
| Site: UW (vs UAB) | +50.0463 | 424.4287 | ±848.8574 | +0.118 | 0.9061 |  |
| **Age (years)** | **-160.2748** | 16.5027 | ±33.0053 | **-9.712** | **2.68e-22** | *** |
| BMI (kg/m2) | -53.0542 | 29.4467 | ±58.8933 | -1.802 | 0.0716 | . |
| Hypertension | -279.1870 | 391.3239 | ±782.6477 | -0.713 | 0.4756 |  |
| High cholesterol | +308.9738 | 379.8143 | ±759.6285 | +0.813 | 0.4159 |  |
| **Kidney disease** | **-1321.5841** | 474.4073 | ±948.8145 | **-2.786** | **0.0053** | ** |
| **Circulatory disease** | **-1454.4007** | 442.0209 | ±884.0417 | **-3.290** | **0.0010** | ** |
| Avg. daily time in range 70-180 (%) | -6.4165 | 8.4344 | ±16.8689 | -0.761 | 0.4468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1693**, Adj R² = **0.1558**, F-statistic = **12.56** (p = **8.59e-22**), Residual SE = **4597.811** on **678** df, AIC = **13608.0**, BIC = **13662.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21795.2489** | 1522.8846 | ±3045.7693 | **+14.312** | **1.85e-46** | *** |
| Education: graduate level (vs college) | -64.6144 | 380.0925 | ±760.1850 | -0.170 | 0.8650 |  |
| Education: high school or below (vs college) | +1015.6631 | 629.0069 | ±1258.0137 | +1.615 | 0.1064 |  |
| Site: UCSD (vs UAB) | +616.7296 | 490.0523 | ±980.1046 | +1.258 | 0.2082 |  |
| Site: UW (vs UAB) | -22.1632 | 428.1568 | ±856.3135 | -0.052 | 0.9587 |  |
| **Age (years)** | **-161.0584** | 16.5693 | ±33.1385 | **-9.720** | **2.47e-22** | *** |
| BMI (kg/m2) | -48.3383 | 29.2520 | ±58.5039 | -1.652 | 0.0984 | . |
| Hypertension | -242.7734 | 391.7915 | ±783.5829 | -0.620 | 0.5355 |  |
| High cholesterol | +264.0081 | 378.2895 | ±756.5790 | +0.698 | 0.4852 |  |
| **Kidney disease** | **-1293.1809** | 467.9560 | ±935.9121 | **-2.763** | **0.0057** | ** |
| **Circulatory disease** | **-1383.9087** | 441.8017 | ±883.6034 | **-3.132** | **0.0017** | ** |
| Any reading < 54 during wear (0/1) | -699.6394 | 413.0243 | ±826.0485 | -1.694 | 0.0903 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1677**, Adj R² = **0.1542**, F-statistic = **12.42** (p = **1.59e-21**), Residual SE = **4602.286** on **678** df, AIC = **13609.4**, BIC = **13663.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21651.9359** | 1506.2815 | ±3012.5629 | **+14.374** | **7.49e-47** | *** |
| Education: graduate level (vs college) | -75.5819 | 380.3965 | ±760.7929 | -0.199 | 0.8425 |  |
| Education: high school or below (vs college) | +1023.3439 | 633.6138 | ±1267.2275 | +1.615 | 0.1063 |  |
| Site: UCSD (vs UAB) | +625.0745 | 489.6438 | ±979.2876 | +1.277 | 0.2017 |  |
| Site: UW (vs UAB) | -34.5419 | 429.2829 | ±858.5658 | -0.080 | 0.9359 |  |
| **Age (years)** | **-159.3834** | 16.4631 | ±32.9262 | **-9.681** | **3.62e-22** | *** |
| BMI (kg/m2) | -50.1786 | 29.1368 | ±58.2737 | -1.722 | 0.0850 | . |
| Hypertension | -269.3140 | 390.3696 | ±780.7393 | -0.690 | 0.4903 |  |
| High cholesterol | +261.7239 | 380.2306 | ±760.4611 | +0.688 | 0.4912 |  |
| **Kidney disease** | **-1298.9427** | 466.4627 | ±932.9253 | **-2.785** | **0.0054** | ** |
| **Circulatory disease** | **-1445.9815** | 441.5811 | ±883.1622 | **-3.275** | **0.0011** | ** |
| Time < 54 (%) | -361.9507 | 619.8516 | ±1239.7032 | -0.584 | 0.5593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1687**, Adj R² = **0.1552**, F-statistic = **12.51** (p = **1.07e-21**), Residual SE = **4599.429** on **678** df, AIC = **13608.5**, BIC = **13663.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21651.9986** | 1504.5964 | ±3009.1928 | **+14.391** | **5.93e-47** | *** |
| Education: graduate level (vs college) | -77.6545 | 380.5882 | ±761.1764 | -0.204 | 0.8383 |  |
| Education: high school or below (vs college) | +1011.7310 | 633.3336 | ±1266.6671 | +1.597 | 0.1102 |  |
| Site: UCSD (vs UAB) | +613.5422 | 490.2941 | ±980.5882 | +1.251 | 0.2108 |  |
| Site: UW (vs UAB) | -55.0660 | 429.1751 | ±858.3502 | -0.128 | 0.8979 |  |
| **Age (years)** | **-159.3222** | 16.4646 | ±32.9292 | **-9.677** | **3.79e-22** | *** |
| BMI (kg/m2) | -49.5683 | 29.0549 | ±58.1098 | -1.706 | 0.0880 | . |
| Hypertension | -263.8081 | 389.4574 | ±778.9149 | -0.677 | 0.4982 |  |
| High cholesterol | +243.7600 | 379.7831 | ±759.5663 | +0.642 | 0.5210 |  |
| **Kidney disease** | **-1289.9052** | 466.2614 | ±932.5229 | **-2.766** | **0.0057** | ** |
| **Circulatory disease** | **-1451.5282** | 440.9031 | ±881.8061 | **-3.292** | **9.94e-04** | *** |
| Avg. daily time < 54 (%) | -519.2349 | 334.9115 | ±669.8230 | -1.550 | 0.1211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1701**, Adj R² = **0.1566**, F-statistic = **12.63** (p = **6.41e-22**), Residual SE = **4595.691** on **678** df, AIC = **13607.4**, BIC = **13661.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21700.2196** | 1498.3257 | ±2996.6514 | **+14.483** | **1.55e-47** | *** |
| Education: graduate level (vs college) | -101.6528 | 378.6451 | ±757.2902 | -0.268 | 0.7883 |  |
| Education: high school or below (vs college) | +1015.0026 | 632.1327 | ±1264.2654 | +1.606 | 0.1083 |  |
| Site: UCSD (vs UAB) | +585.3926 | 488.2029 | ±976.4058 | +1.199 | 0.2305 |  |
| Site: UW (vs UAB) | -79.1892 | 426.8884 | ±853.7767 | -0.186 | 0.8528 |  |
| **Age (years)** | **-158.7509** | 16.4387 | ±32.8775 | **-9.657** | **4.59e-22** | *** |
| BMI (kg/m2) | -48.8513 | 29.0341 | ±58.0682 | -1.683 | 0.0925 | . |
| Hypertension | -246.7868 | 388.4215 | ±776.8430 | -0.635 | 0.5252 |  |
| High cholesterol | +218.7556 | 377.3164 | ±754.6329 | +0.580 | 0.5621 |  |
| **Kidney disease** | **-1281.8352** | 465.8631 | ±931.7263 | **-2.752** | **0.0059** | ** |
| **Circulatory disease** | **-1483.1063** | 439.6566 | ±879.3131 | **-3.373** | **7.43e-04** | *** |
| **Time 54-69, pooled (%)** | **-318.0817** | 154.8236 | ±309.6471 | **-2.054** | **0.0399** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **690**, R² = **0.1705**, Adj R² = **0.1571**, F-statistic = **12.67** (p = **5.34e-22**), Residual SE = **4594.368** on **678** df, AIC = **13607.0**, BIC = **13661.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21670.7522** | 1498.5110 | ±2997.0220 | **+14.462** | **2.12e-47** | *** |
| Education: graduate level (vs college) | -103.3671 | 378.7894 | ±757.5787 | -0.273 | 0.7849 |  |
| Education: high school or below (vs college) | +1007.9186 | 631.0353 | ±1262.0706 | +1.597 | 0.1102 |  |
| Site: UCSD (vs UAB) | +580.2411 | 488.9846 | ±977.9692 | +1.187 | 0.2354 |  |
| Site: UW (vs UAB) | -90.9237 | 427.9157 | ±855.8313 | -0.212 | 0.8317 |  |
| **Age (years)** | **-158.4847** | 16.4279 | ±32.8557 | **-9.647** | **5.05e-22** | *** |
| BMI (kg/m2) | -48.4853 | 29.0455 | ±58.0910 | -1.669 | 0.0951 | . |
| Hypertension | -244.1403 | 388.4408 | ±776.8815 | -0.629 | 0.5297 |  |
| High cholesterol | +213.3498 | 376.3968 | ±752.7936 | +0.567 | 0.5708 |  |
| **Kidney disease** | **-1277.4327** | 465.8878 | ±931.7757 | **-2.742** | **0.0061** | ** |
| **Circulatory disease** | **-1484.8886** | 440.2841 | ±880.5682 | **-3.373** | **7.45e-04** | *** |
| **Avg. daily time 54-69 (%)** | **-312.0102** | 140.3172 | ±280.6343 | **-2.224** | **0.0262** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **690**, R² = **0.1702**, Adj R² = **0.1567**, F-statistic = **12.64** (p = **6.08e-22**), Residual SE = **4595.300** on **678** df, AIC = **13607.3**, BIC = **13661.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21731.3956** | 1501.4356 | ±3002.8711 | **+14.474** | **1.78e-47** | *** |
| Education: graduate level (vs college) | -106.2867 | 379.4261 | ±758.8522 | -0.280 | 0.7794 |  |
| Education: high school or below (vs college) | +1002.9461 | 632.2693 | ±1264.5387 | +1.586 | 0.1127 |  |
| Site: UCSD (vs UAB) | +579.6536 | 489.7163 | ±979.4326 | +1.184 | 0.2366 |  |
| Site: UW (vs UAB) | -87.6813 | 428.4359 | ±856.8718 | -0.205 | 0.8378 |  |
| **Age (years)** | **-158.5852** | 16.4402 | ±32.8805 | **-9.646** | **5.10e-22** | *** |
| BMI (kg/m2) | -49.8868 | 28.9789 | ±57.9577 | -1.721 | 0.0852 | . |
| Hypertension | -252.4016 | 388.6366 | ±777.2731 | -0.649 | 0.5160 |  |
| High cholesterol | +214.4672 | 377.9082 | ±755.8164 | +0.568 | 0.5704 |  |
| **Kidney disease** | **-1289.6734** | 465.6222 | ±931.2445 | **-2.770** | **0.0056** | ** |
| **Circulatory disease** | **-1481.7552** | 440.0057 | ±880.0115 | **-3.368** | **7.58e-04** | *** |
| **Time < 70 (%)** | **-236.9123** | 96.4272 | ±192.8545 | **-2.457** | **0.0140** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **690**, R² = **0.1708**, Adj R² = **0.1573**, F-statistic = **12.70** (p = **4.83e-22**), Residual SE = **4593.646** on **678** df, AIC = **13606.8**, BIC = **13661.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21691.9253** | 1500.2090 | ±3000.4179 | **+14.459** | **2.19e-47** | *** |
| Education: graduate level (vs college) | -104.5608 | 379.5770 | ±759.1540 | -0.275 | 0.7830 |  |
| Education: high school or below (vs college) | +997.7757 | 631.5354 | ±1263.0708 | +1.580 | 0.1141 |  |
| Site: UCSD (vs UAB) | +575.8967 | 490.2317 | ±980.4634 | +1.175 | 0.2401 |  |
| Site: UW (vs UAB) | -99.1367 | 429.0556 | ±858.1113 | -0.231 | 0.8173 |  |
| **Age (years)** | **-158.4710** | 16.4307 | ±32.8614 | **-9.645** | **5.17e-22** | *** |
| BMI (kg/m2) | -48.9988 | 28.9899 | ±57.9798 | -1.690 | 0.0910 | . |
| Hypertension | -247.2857 | 388.5594 | ±777.1188 | -0.636 | 0.5245 |  |
| High cholesterol | +207.1972 | 377.3641 | ±754.7283 | +0.549 | 0.5830 |  |
| **Kidney disease** | **-1280.2132** | 465.6437 | ±931.2874 | **-2.749** | **0.0060** | ** |
| **Circulatory disease** | **-1483.2884** | 440.4434 | ±880.8868 | **-3.368** | **7.58e-04** | *** |
| **Avg. daily time < 70 (%)** | **-240.4531** | 87.9352 | ±175.8705 | **-2.734** | **0.0062** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.471** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21554.8551** | 2007.2692 | ±4014.5385 | **+10.738** | **6.72e-27** | *** |
| Education: graduate level (vs college) | -46.9220 | 386.7841 | ±773.5682 | -0.121 | 0.9034 |  |
| Education: high school or below (vs college) | +1058.2743 | 625.1065 | ±1250.2131 | +1.693 | 0.0905 | . |
| Site: UCSD (vs UAB) | +665.0799 | 484.9763 | ±969.9526 | +1.371 | 0.1703 |  |
| Site: UW (vs UAB) | +15.7628 | 423.7599 | ±847.5197 | +0.037 | 0.9703 |  |
| **Age (years)** | **-160.1870** | 16.3254 | ±32.6508 | **-9.812** | **9.98e-23** | *** |
| BMI (kg/m2) | -48.4680 | 29.3401 | ±58.6802 | -1.652 | 0.0985 | . |
| Hypertension | -269.8022 | 390.6640 | ±781.3281 | -0.691 | 0.4898 |  |
| High cholesterol | +300.0535 | 381.0181 | ±762.0361 | +0.788 | 0.4310 |  |
| **Kidney disease** | **-1290.5128** | 470.4119 | ±940.8239 | **-2.743** | **0.0061** | ** |
| **Circulatory disease** | **-1425.9513** | 443.4871 | ±886.9742 | **-3.215** | **0.0013** | ** |
| Time 54-250, pooled (%) | -0.1303 | 12.8068 | ±25.6135 | -0.010 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.461** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21600.6451** | 1995.5832 | ±3991.1663 | **+10.824** | **2.64e-27** | *** |
| Education: graduate level (vs college) | -45.4858 | 386.7495 | ±773.4991 | -0.118 | 0.9064 |  |
| Education: high school or below (vs college) | +1056.1037 | 625.8216 | ±1251.6431 | +1.688 | 0.0915 | . |
| Site: UCSD (vs UAB) | +666.1525 | 484.9823 | ±969.9646 | +1.374 | 0.1696 |  |
| Site: UW (vs UAB) | +17.5868 | 423.7547 | ±847.5095 | +0.042 | 0.9669 |  |
| **Age (years)** | **-160.1382** | 16.3489 | ±32.6978 | **-9.795** | **1.18e-22** | *** |
| BMI (kg/m2) | -48.6006 | 29.3090 | ±58.6180 | -1.658 | 0.0973 | . |
| Hypertension | -270.3052 | 390.6822 | ±781.3644 | -0.692 | 0.4890 |  |
| High cholesterol | +300.5631 | 380.9142 | ±761.8285 | +0.789 | 0.4301 |  |
| **Kidney disease** | **-1291.6843** | 470.8081 | ±941.6161 | **-2.744** | **0.0061** | ** |
| **Circulatory disease** | **-1427.1833** | 443.4588 | ±886.9176 | **-3.218** | **0.0013** | ** |
| Avg. daily time 54-250 (%) | -0.6242 | 12.5594 | ±25.1187 | -0.050 | 0.9604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1691**, Adj R² = **0.1557**, F-statistic = **12.55** (p = **9.06e-22**), Residual SE = **4598.193** on **678** df, AIC = **13608.1**, BIC = **13662.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21571.5303** | 1502.5028 | ±3005.0055 | **+14.357** | **9.62e-47** | *** |
| Education: graduate level (vs college) | -56.8069 | 377.9325 | ±755.8650 | -0.150 | 0.8805 |  |
| Education: high school or below (vs college) | +986.6784 | 635.4438 | ±1270.8877 | +1.553 | 0.1205 |  |
| Site: UCSD (vs UAB) | +709.3825 | 486.4106 | ±972.8213 | +1.458 | 0.1447 |  |
| Site: UW (vs UAB) | +37.5975 | 425.6476 | ±851.2951 | +0.088 | 0.9296 |  |
| **Age (years)** | **-162.5340** | 16.6141 | ±33.2281 | **-9.783** | **1.33e-22** | *** |
| **BMI (kg/m2)** | **-57.5085** | 29.0374 | ±58.0748 | **-1.980** | **0.0476** | * |
| Hypertension | -276.8727 | 390.9561 | ±781.9123 | -0.708 | 0.4788 |  |
| High cholesterol | +303.6202 | 378.8492 | ±757.6984 | +0.801 | 0.4229 |  |
| **Kidney disease** | **-1339.0777** | 472.1696 | ±944.3392 | **-2.836** | **0.0046** | ** |
| **Circulatory disease** | **-1473.8015** | 439.8135 | ±879.6270 | **-3.351** | **8.05e-04** | *** |
| Time 181-250, pooled (%) | +20.3659 | 13.1264 | ±26.2527 | +1.552 | 0.1208 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **690**, R² = **0.1687**, Adj R² = **0.1552**, F-statistic = **12.51** (p = **1.07e-21**), Residual SE = **4599.366** on **678** df, AIC = **13608.5**, BIC = **13662.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21565.2621** | 1503.3746 | ±3006.7493 | **+14.345** | **1.15e-46** | *** |
| Education: graduate level (vs college) | -58.7188 | 378.0489 | ±756.0977 | -0.155 | 0.8766 |  |
| Education: high school or below (vs college) | +985.0105 | 633.5293 | ±1267.0585 | +1.555 | 0.1200 |  |
| Site: UCSD (vs UAB) | +711.8623 | 486.1087 | ±972.2174 | +1.464 | 0.1431 |  |
| Site: UW (vs UAB) | +40.2716 | 425.4875 | ±850.9750 | +0.095 | 0.9246 |  |
| **Age (years)** | **-162.2351** | 16.6278 | ±33.2557 | **-9.757** | **1.72e-22** | *** |
| BMI (kg/m2) | -56.8849 | 29.1712 | ±58.3424 | -1.950 | 0.0512 | . |
| Hypertension | -276.2384 | 391.1025 | ±782.2051 | -0.706 | 0.4800 |  |
| High cholesterol | +301.8022 | 379.1991 | ±758.3981 | +0.796 | 0.4261 |  |
| **Kidney disease** | **-1337.6450** | 472.4344 | ±944.8688 | **-2.831** | **0.0046** | ** |
| **Circulatory disease** | **-1466.7544** | 440.5612 | ±881.1224 | **-3.329** | **8.71e-04** | *** |
| Avg. daily time 181-250 (%) | +18.6582 | 12.8673 | ±25.7345 | +1.450 | 0.1470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **690**, R² = **0.1671**, Adj R² = **0.1535**, F-statistic = **12.36** (p = **2.01e-21**), Residual SE = **4603.968** on **678** df, AIC = **13609.9**, BIC = **13664.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21487.9319** | 1499.3420 | ±2998.6840 | **+14.332** | **1.39e-46** | *** |
| Education: graduate level (vs college) | -28.7478 | 383.3638 | ±766.7276 | -0.075 | 0.9402 |  |
| Education: high school or below (vs college) | +998.4226 | 627.3725 | ±1254.7451 | +1.591 | 0.1115 |  |
| Site: UCSD (vs UAB) | +696.0260 | 484.8899 | ±969.7797 | +1.435 | 0.1512 |  |
| Site: UW (vs UAB) | +51.4065 | 424.4319 | ±848.8638 | +0.121 | 0.9036 |  |
| **Age (years)** | **-160.1496** | 16.4827 | ±32.9654 | **-9.716** | **2.57e-22** | *** |
| BMI (kg/m2) | -53.7123 | 29.3942 | ±58.7885 | -1.827 | 0.0677 | . |
| Hypertension | -280.9783 | 391.3809 | ±782.7618 | -0.718 | 0.4728 |  |
| High cholesterol | +308.1603 | 379.6943 | ±759.3885 | +0.812 | 0.4170 |  |
| **Kidney disease** | **-1323.2623** | 473.9549 | ±947.9099 | **-2.792** | **0.0052** | ** |
| **Circulatory disease** | **-1461.1017** | 441.8986 | ±883.7972 | **-3.306** | **9.45e-04** | *** |
| Time > 180 (%) | +7.4020 | 8.4338 | ±16.8676 | +0.878 | 0.3801 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1670**, Adj R² = **0.1535**, F-statistic = **12.36** (p = **2.05e-21**), Residual SE = **4604.101** on **678** df, AIC = **13609.9**, BIC = **13664.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21497.7209** | 1499.9994 | ±2999.9987 | **+14.332** | **1.38e-46** | *** |
| Education: graduate level (vs college) | -30.9515 | 383.0216 | ±766.0432 | -0.081 | 0.9356 |  |
| Education: high school or below (vs college) | +997.7483 | 627.0307 | ±1254.0614 | +1.591 | 0.1116 |  |
| Site: UCSD (vs UAB) | +697.9068 | 484.5518 | ±969.1037 | +1.440 | 0.1498 |  |
| Site: UW (vs UAB) | +50.9445 | 424.2729 | ±848.5458 | +0.120 | 0.9044 |  |
| **Age (years)** | **-160.2319** | 16.4930 | ±32.9860 | **-9.715** | **2.60e-22** | *** |
| BMI (kg/m2) | -53.6462 | 29.4291 | ±58.8581 | -1.823 | 0.0683 | . |
| Hypertension | -279.7031 | 391.2938 | ±782.5875 | -0.715 | 0.4747 |  |
| High cholesterol | +307.3186 | 379.7251 | ±759.4501 | +0.809 | 0.4183 |  |
| **Kidney disease** | **-1325.1833** | 474.3249 | ±948.6498 | **-2.794** | **0.0052** | ** |
| **Circulatory disease** | **-1459.7097** | 442.1163 | ±884.2326 | **-3.302** | **9.61e-04** | *** |
| Avg. daily time > 180 (%) | +7.2152 | 8.3701 | ±16.7402 | +0.862 | 0.3887 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1679**, Adj R² = **0.1544**, F-statistic = **12.44** (p = **1.47e-21**), Residual SE = **4601.708** on **678** df, AIC = **13609.2**, BIC = **13663.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21516.0211** | 1503.8717 | ±3007.7433 | **+14.307** | **1.98e-46** | *** |
| Education: graduate level (vs college) | -8.2813 | 387.2526 | ±774.5052 | -0.021 | 0.9829 |  |
| Education: high school or below (vs college) | +994.9263 | 625.0727 | ±1250.1455 | +1.592 | 0.1115 |  |
| Site: UCSD (vs UAB) | +706.8489 | 483.6921 | ±967.3841 | +1.461 | 0.1439 |  |
| Site: UW (vs UAB) | +51.5872 | 423.8732 | ±847.7464 | +0.122 | 0.9031 |  |
| **Age (years)** | **-159.2472** | 16.4409 | ±32.8817 | **-9.686** | **3.46e-22** | *** |
| BMI (kg/m2) | -56.4983 | 29.4478 | ±58.8956 | -1.919 | 0.0550 | . |
| Hypertension | -280.9422 | 391.1611 | ±782.3222 | -0.718 | 0.4726 |  |
| High cholesterol | +320.5406 | 379.7265 | ±759.4529 | +0.844 | 0.3986 |  |
| **Kidney disease** | **-1311.6845** | 472.6284 | ±945.2568 | **-2.775** | **0.0055** | ** |
| **Circulatory disease** | **-1468.6883** | 441.2877 | ±882.5754 | **-3.328** | **8.74e-04** | *** |
| Nocturnal time > 180 (%) | +8.6654 | 7.7923 | ±15.5847 | +1.112 | 0.2661 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.25e-21**), Residual SE = **4607.460** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21537.4682** | 1495.3632 | ±2990.7264 | **+14.403** | **4.97e-47** | *** |
| Education: graduate level (vs college) | -45.4524 | 386.5076 | ±773.0152 | -0.118 | 0.9064 |  |
| Education: high school or below (vs college) | +1055.9630 | 624.9556 | ±1249.9113 | +1.690 | 0.0911 | . |
| Site: UCSD (vs UAB) | +666.0750 | 485.0727 | ±970.1453 | +1.373 | 0.1697 |  |
| Site: UW (vs UAB) | +17.6286 | 423.6545 | ±847.3091 | +0.042 | 0.9668 |  |
| **Age (years)** | **-160.1262** | 16.3228 | ±32.6457 | **-9.810** | **1.02e-22** | *** |
| BMI (kg/m2) | -48.6017 | 29.3516 | ±58.7032 | -1.656 | 0.0978 | . |
| Hypertension | -270.3869 | 390.6737 | ±781.3473 | -0.692 | 0.4889 |  |
| High cholesterol | +300.5032 | 380.8671 | ±761.7343 | +0.789 | 0.4301 |  |
| **Kidney disease** | **-1291.5418** | 470.5087 | ±941.0173 | **-2.745** | **0.0061** | ** |
| **Circulatory disease** | **-1427.1652** | 443.5493 | ±887.0987 | **-3.218** | **0.0013** | ** |
| Time > 250 (%) | +0.6277 | 12.8157 | ±25.6314 | +0.049 | 0.9609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 690)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **690**, R² = **0.1658**, Adj R² = **0.1523**, F-statistic = **12.25** (p = **3.23e-21**), Residual SE = **4607.433** on **678** df, AIC = **13610.9**, BIC = **13665.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21534.2204** | 1496.9509 | ±2993.9018 | **+14.385** | **6.39e-47** | *** |
| Education: graduate level (vs college) | -43.9284 | 386.5231 | ±773.0462 | -0.114 | 0.9095 |  |
| Education: high school or below (vs college) | +1053.5495 | 625.7043 | ±1251.4087 | +1.684 | 0.0922 | . |
| Site: UCSD (vs UAB) | +667.2344 | 485.0640 | ±970.1279 | +1.376 | 0.1690 |  |
| Site: UW (vs UAB) | +19.4982 | 423.6839 | ±847.3678 | +0.046 | 0.9633 |  |
| **Age (years)** | **-160.0791** | 16.3469 | ±32.6937 | **-9.793** | **1.21e-22** | *** |
| BMI (kg/m2) | -48.7512 | 29.3145 | ±58.6290 | -1.663 | 0.0963 | . |
| Hypertension | -270.8740 | 390.6768 | ±781.3536 | -0.693 | 0.4881 |  |
| High cholesterol | +301.0074 | 380.7639 | ±761.5278 | +0.791 | 0.4292 |  |
| **Kidney disease** | **-1292.9579** | 470.8643 | ±941.7286 | **-2.746** | **0.0060** | ** |
| **Circulatory disease** | **-1428.6083** | 443.5101 | ±887.0202 | **-3.221** | **0.0013** | ** |
| Avg. daily time > 250 (%) | +1.1777 | 12.5722 | ±25.1445 | +0.094 | 0.9254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 690; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **690**, R² = **0.1849**, Adj R² = **0.1729**, F-statistic = **15.40** (p = **5.12e-25**), Residual SE = **13.513** on **679** df, AIC = **5562.1**, BIC = **5612.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3722** | 4.3530 | ±8.7061 | **+13.410** | **5.32e-41** | *** |
| Education: graduate level (vs college) | -0.3768 | 1.1370 | ±2.2739 | -0.331 | 0.7403 |  |
| Education: high school or below (vs college) | +3.1159 | 1.7654 | ±3.5307 | +1.765 | 0.0776 | . |
| **Site: UCSD (vs UAB)** | **+2.9142** | 1.4586 | ±2.9172 | **+1.998** | **0.0457** | * |
| Site: UW (vs UAB) | +1.1397 | 1.2145 | ±2.4291 | +0.938 | 0.3480 |  |
| **Age (years)** | **-0.5229** | 0.0489 | ±0.0978 | **-10.699** | **1.03e-26** | *** |
| BMI (kg/m2) | -0.0486 | 0.0814 | ±0.1627 | -0.597 | 0.5505 |  |
| Hypertension | -1.0976 | 1.1607 | ±2.3213 | -0.946 | 0.3443 |  |
| High cholesterol | +0.9646 | 1.0857 | ±2.1713 | +0.889 | 0.3743 |  |
| Kidney disease | -2.3816 | 1.4240 | ±2.8480 | -1.672 | 0.0944 | . |
| **Circulatory disease** | **-3.7550** | 1.2733 | ±2.5465 | **-2.949** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **690**, R² = **0.1900**, Adj R² = **0.1769**, F-statistic = **14.46** (p = **2.71e-25**), Residual SE = **13.480** on **678** df, AIC = **5559.7**, BIC = **5614.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.6792** | 4.7444 | ±9.4888 | **+11.314** | **1.12e-29** | *** |
| Education: graduate level (vs college) | -0.1806 | 1.1447 | ±2.2894 | -0.158 | 0.8746 |  |
| Education: high school or below (vs college) | +2.7359 | 1.7610 | ±3.5220 | +1.554 | 0.1203 |  |
| **Site: UCSD (vs UAB)** | **+3.0034** | 1.4551 | ±2.9101 | **+2.064** | **0.0390** | * |
| Site: UW (vs UAB) | +1.3485 | 1.2050 | ±2.4100 | +1.119 | 0.2631 |  |
| **Age (years)** | **-0.5221** | 0.0487 | ±0.0974 | **-10.722** | **8.06e-27** | *** |
| BMI (kg/m2) | -0.0794 | 0.0838 | ±0.1677 | -0.947 | 0.3435 |  |
| Hypertension | -1.2309 | 1.1676 | ±2.3352 | -1.054 | 0.2918 |  |
| High cholesterol | +0.9153 | 1.0843 | ±2.1685 | +0.844 | 0.3986 |  |
| Kidney disease | -2.3364 | 1.4165 | ±2.8330 | -1.649 | 0.0991 | . |
| **Circulatory disease** | **-3.8526** | 1.2740 | ±2.5481 | **-3.024** | **0.0025** | ** |
| HbA1c (%) | +0.8230 | 0.4304 | ±0.8607 | +1.912 | 0.0558 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.08** (p = **1.36e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6485** | 4.4876 | ±8.9753 | **+12.623** | **1.57e-36** | *** |
| Education: graduate level (vs college) | -0.3266 | 1.1468 | ±2.2936 | -0.285 | 0.7758 |  |
| Education: high school or below (vs college) | +2.9524 | 1.7505 | ±3.5010 | +1.687 | 0.0917 | . |
| **Site: UCSD (vs UAB)** | **+2.9797** | 1.4486 | ±2.8973 | **+2.057** | **0.0397** | * |
| Site: UW (vs UAB) | +1.2244 | 1.2020 | ±2.4040 | +1.019 | 0.3084 |  |
| **Age (years)** | **-0.5218** | 0.0487 | ±0.0975 | **-10.705** | **9.63e-27** | *** |
| BMI (kg/m2) | -0.0611 | 0.0831 | ±0.1662 | -0.735 | 0.4624 |  |
| Hypertension | -1.1385 | 1.1676 | ±2.3352 | -0.975 | 0.3295 |  |
| High cholesterol | +0.9707 | 1.0884 | ±2.1768 | +0.892 | 0.3724 |  |
| Kidney disease | -2.4430 | 1.4309 | ±2.8619 | -1.707 | 0.0878 | . |
| **Circulatory disease** | **-3.8533** | 1.2793 | ±2.5586 | **-3.012** | **0.0026** | ** |
| Mean glucose (mg/dL) | +0.0126 | 0.0149 | ±0.0298 | +0.848 | 0.3962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.08** (p = **1.36e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9002** | 5.4508 | ±10.9016 | **+10.072** | **7.35e-24** | *** |
| Education: graduate level (vs college) | -0.3266 | 1.1468 | ±2.2936 | -0.285 | 0.7758 |  |
| Education: high school or below (vs college) | +2.9524 | 1.7505 | ±3.5010 | +1.687 | 0.0917 | . |
| **Site: UCSD (vs UAB)** | **+2.9797** | 1.4486 | ±2.8973 | **+2.057** | **0.0397** | * |
| Site: UW (vs UAB) | +1.2244 | 1.2020 | ±2.4040 | +1.019 | 0.3084 |  |
| **Age (years)** | **-0.5218** | 0.0487 | ±0.0975 | **-10.705** | **9.63e-27** | *** |
| BMI (kg/m2) | -0.0611 | 0.0831 | ±0.1662 | -0.735 | 0.4624 |  |
| Hypertension | -1.1385 | 1.1676 | ±2.3352 | -0.975 | 0.3295 |  |
| High cholesterol | +0.9707 | 1.0884 | ±2.1768 | +0.892 | 0.3724 |  |
| Kidney disease | -2.4430 | 1.4309 | ±2.8619 | -1.707 | 0.0878 | . |
| **Circulatory disease** | **-3.8533** | 1.2793 | ±2.5586 | **-3.012** | **0.0026** | ** |
| GMI (%) | +0.5282 | 0.6226 | ±1.2452 | +0.848 | 0.3962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **690**, R² = **0.1874**, Adj R² = **0.1742**, F-statistic = **14.21** (p = **7.68e-25**), Residual SE = **13.502** on **678** df, AIC = **5561.9**, BIC = **5616.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.9652** | 4.4923 | ±8.9846 | **+12.458** | **1.27e-35** | *** |
| Education: graduate level (vs college) | -0.2785 | 1.1502 | ±2.3004 | -0.242 | 0.8087 |  |
| Education: high school or below (vs college) | +2.8819 | 1.7494 | ±3.4988 | +1.647 | 0.0995 | . |
| **Site: UCSD (vs UAB)** | **+3.0040** | 1.4475 | ±2.8950 | **+2.075** | **0.0380** | * |
| Site: UW (vs UAB) | +1.2273 | 1.2035 | ±2.4070 | +1.020 | 0.3078 |  |
| **Age (years)** | **-0.5188** | 0.0485 | ±0.0971 | **-10.687** | **1.17e-26** | *** |
| BMI (kg/m2) | -0.0721 | 0.0835 | ±0.1670 | -0.863 | 0.3882 |  |
| Hypertension | -1.1488 | 1.1671 | ±2.3343 | -0.984 | 0.3250 |  |
| High cholesterol | +0.9923 | 1.0891 | ±2.1781 | +0.911 | 0.3622 |  |
| Kidney disease | -2.3898 | 1.4259 | ±2.8518 | -1.676 | 0.0937 | . |
| **Circulatory disease** | **-3.9010** | 1.2800 | ±2.5600 | **-3.048** | **0.0023** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0184 | 0.0147 | ±0.0294 | +1.253 | 0.2102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1857**, Adj R² = **0.1725**, F-statistic = **14.05** (p = **1.51e-24**), Residual SE = **13.516** on **678** df, AIC = **5563.4**, BIC = **5617.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2518** | 4.3852 | ±8.7704 | **+13.056** | **5.89e-39** | *** |
| Education: graduate level (vs college) | -0.3130 | 1.1531 | ±2.3061 | -0.271 | 0.7860 |  |
| Education: high school or below (vs college) | +2.9901 | 1.7530 | ±3.5060 | +1.706 | 0.0881 | . |
| **Site: UCSD (vs UAB)** | **+3.0018** | 1.4418 | ±2.8836 | **+2.082** | **0.0373** | * |
| Site: UW (vs UAB) | +1.2874 | 1.1934 | ±2.3868 | +1.079 | 0.2807 |  |
| **Age (years)** | **-0.5240** | 0.0492 | ±0.0984 | **-10.654** | **1.66e-26** | *** |
| BMI (kg/m2) | -0.0566 | 0.0825 | ±0.1649 | -0.686 | 0.4927 |  |
| Hypertension | -1.1560 | 1.1727 | ±2.3454 | -0.986 | 0.3243 |  |
| High cholesterol | +0.9975 | 1.0878 | ±2.1755 | +0.917 | 0.3591 |  |
| Kidney disease | -2.5962 | 1.4786 | ±2.9572 | -1.756 | 0.0791 | . |
| **Circulatory disease** | **-3.8147** | 1.2746 | ±2.5492 | **-2.993** | **0.0028** | ** |
| Glucose SD, pooled (mg/dL) | +0.0372 | 0.0500 | ±0.1000 | +0.744 | 0.4571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1851**, Adj R² = **0.1719**, F-statistic = **14.00** (p = **1.88e-24**), Residual SE = **13.521** on **678** df, AIC = **5563.9**, BIC = **5618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7287** | 4.4053 | ±8.8106 | **+13.104** | **3.11e-39** | *** |
| Education: graduate level (vs college) | -0.3483 | 1.1476 | ±2.2952 | -0.304 | 0.7615 |  |
| Education: high school or below (vs college) | +3.0385 | 1.7631 | ±3.5263 | +1.723 | 0.0848 | . |
| **Site: UCSD (vs UAB)** | **+2.9627** | 1.4427 | ±2.8855 | **+2.054** | **0.0400** | * |
| Site: UW (vs UAB) | +1.2149 | 1.1943 | ±2.3886 | +1.017 | 0.3090 |  |
| **Age (years)** | **-0.5238** | 0.0493 | ±0.0985 | **-10.633** | **2.10e-26** | *** |
| BMI (kg/m2) | -0.0517 | 0.0819 | ±0.1638 | -0.632 | 0.5274 |  |
| Hypertension | -1.1274 | 1.1727 | ±2.3454 | -0.961 | 0.3363 |  |
| High cholesterol | +0.9808 | 1.0877 | ±2.1754 | +0.902 | 0.3672 |  |
| Kidney disease | -2.5089 | 1.4764 | ±2.9529 | -1.699 | 0.0893 | . |
| **Circulatory disease** | **-3.7843** | 1.2745 | ±2.5490 | **-2.969** | **0.0030** | ** |
| Avg. daily SD (mg/dL) | +0.0233 | 0.0539 | ±0.1079 | +0.431 | 0.6664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1718**, F-statistic = **13.99** (p = **1.94e-24**), Residual SE = **13.522** on **678** df, AIC = **5563.9**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.2104** | 4.7785 | ±9.5570 | **+12.391** | **2.92e-35** | *** |
| Education: graduate level (vs college) | -0.3996 | 1.1414 | ±2.2828 | -0.350 | 0.7262 |  |
| Education: high school or below (vs college) | +3.1307 | 1.7669 | ±3.5339 | +1.772 | 0.0764 | . |
| **Site: UCSD (vs UAB)** | **+2.8784** | 1.4550 | ±2.9099 | **+1.978** | **0.0479** | * |
| Site: UW (vs UAB) | +1.0792 | 1.2171 | ±2.4342 | +0.887 | 0.3752 |  |
| **Age (years)** | **-0.5218** | 0.0490 | ±0.0980 | **-10.651** | **1.73e-26** | *** |
| BMI (kg/m2) | -0.0487 | 0.0813 | ±0.1627 | -0.599 | 0.5494 |  |
| Hypertension | -1.0760 | 1.1660 | ±2.3320 | -0.923 | 0.3561 |  |
| High cholesterol | +0.9421 | 1.0836 | ±2.1672 | +0.869 | 0.3846 |  |
| Kidney disease | -2.2758 | 1.4647 | ±2.9295 | -1.554 | 0.1202 |  |
| **Circulatory disease** | **-3.7606** | 1.2753 | ±2.5506 | **-2.949** | **0.0032** | ** |
| CV (%) | -0.0375 | 0.0906 | ±0.1812 | -0.414 | 0.6787 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **690**, R² = **0.1853**, Adj R² = **0.1721**, F-statistic = **14.02** (p = **1.73e-24**), Residual SE = **13.519** on **678** df, AIC = **5563.7**, BIC = **5618.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.9058** | 5.0036 | ±10.0071 | **+11.973** | **4.94e-33** | *** |
| Education: graduate level (vs college) | -0.3467 | 1.1408 | ±2.2816 | -0.304 | 0.7612 |  |
| Education: high school or below (vs college) | +3.0956 | 1.7667 | ±3.5333 | +1.752 | 0.0797 | . |
| **Site: UCSD (vs UAB)** | **+2.9501** | 1.4558 | ±2.9116 | **+2.026** | **0.0427** | * |
| Site: UW (vs UAB) | +1.2225 | 1.2102 | ±2.4205 | +1.010 | 0.3124 |  |
| **Age (years)** | **-0.5244** | 0.0490 | ±0.0980 | **-10.707** | **9.42e-27** | *** |
| BMI (kg/m2) | -0.0477 | 0.0817 | ±0.1634 | -0.584 | 0.5592 |  |
| Hypertension | -1.1327 | 1.1659 | ±2.3318 | -0.972 | 0.3313 |  |
| High cholesterol | +0.9804 | 1.0844 | ±2.1689 | +0.904 | 0.3660 |  |
| Kidney disease | -2.5313 | 1.4637 | ±2.9273 | -1.729 | 0.0837 | . |
| **Circulatory disease** | **-3.7613** | 1.2729 | ±2.5457 | **-2.955** | **0.0031** | ** |
| Mean / SD ratio | -0.3317 | 0.4784 | ±0.9568 | -0.693 | 0.4881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **690**, R² = **0.1855**, Adj R² = **0.1723**, F-statistic = **14.04** (p = **1.61e-24**), Residual SE = **13.518** on **678** df, AIC = **5563.5**, BIC = **5618.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.0587** | 4.8820 | ±9.7640 | **+12.302** | **8.82e-35** | *** |
| Education: graduate level (vs college) | -0.3509 | 1.1373 | ±2.2747 | -0.309 | 0.7577 |  |
| Education: high school or below (vs college) | +3.0864 | 1.7709 | ±3.5418 | +1.743 | 0.0814 | . |
| **Site: UCSD (vs UAB)** | **+2.9467** | 1.4580 | ±2.9160 | **+2.021** | **0.0433** | * |
| Site: UW (vs UAB) | +1.2264 | 1.2115 | ±2.4230 | +1.012 | 0.3114 |  |
| **Age (years)** | **-0.5254** | 0.0489 | ±0.0979 | **-10.735** | **6.97e-27** | *** |
| BMI (kg/m2) | -0.0456 | 0.0817 | ±0.1634 | -0.557 | 0.5772 |  |
| Hypertension | -1.1396 | 1.1646 | ±2.3293 | -0.978 | 0.3278 |  |
| High cholesterol | +0.9906 | 1.0849 | ±2.1698 | +0.913 | 0.3612 |  |
| Kidney disease | -2.5457 | 1.4471 | ±2.8941 | -1.759 | 0.0785 | . |
| **Circulatory disease** | **-3.7464** | 1.2726 | ±2.5453 | **-2.944** | **0.0032** | ** |
| Avg. daily mean/SD | -0.3139 | 0.3775 | ±0.7549 | -0.831 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **690**, R² = **0.1903**, Adj R² = **0.1771**, F-statistic = **14.48** (p = **2.48e-25**), Residual SE = **13.478** on **678** df, AIC = **5559.5**, BIC = **5613.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3472** | 5.2448 | ±10.4897 | **+9.981** | **1.85e-23** | *** |
| Education: graduate level (vs college) | -0.1990 | 1.1418 | ±2.2836 | -0.174 | 0.8617 |  |
| Education: high school or below (vs college) | +2.9938 | 1.7503 | ±3.5007 | +1.710 | 0.0872 | . |
| **Site: UCSD (vs UAB)** | **+3.1972** | 1.4646 | ±2.9292 | **+2.183** | **0.0290** | * |
| Site: UW (vs UAB) | +1.5898 | 1.2073 | ±2.4146 | +1.317 | 0.1879 |  |
| **Age (years)** | **-0.5150** | 0.0485 | ±0.0970 | **-10.618** | **2.46e-26** | *** |
| BMI (kg/m2) | -0.0528 | 0.0815 | ±0.1629 | -0.648 | 0.5168 |  |
| Hypertension | -1.0290 | 1.1610 | ±2.3221 | -0.886 | 0.3755 |  |
| High cholesterol | +1.1179 | 1.0971 | ±2.1942 | +1.019 | 0.3082 |  |
| Kidney disease | -2.6282 | 1.4249 | ±2.8497 | -1.845 | 0.0651 | . |
| **Circulatory disease** | **-3.7848** | 1.2688 | ±2.5377 | **-2.983** | **0.0029** | ** |
| MAG (mg/dL/h) | +0.1168 | 0.0611 | ±0.1223 | +1.911 | 0.0560 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **690**, R² = **0.1854**, Adj R² = **0.1722**, F-statistic = **14.03** (p = **1.70e-24**), Residual SE = **13.519** on **678** df, AIC = **5563.7**, BIC = **5618.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9321** | 4.7304 | ±9.4608 | **+12.035** | **2.32e-33** | *** |
| Education: graduate level (vs college) | -0.3391 | 1.1448 | ±2.2896 | -0.296 | 0.7671 |  |
| Education: high school or below (vs college) | +3.0029 | 1.7646 | ±3.5291 | +1.702 | 0.0888 | . |
| **Site: UCSD (vs UAB)** | **+2.9984** | 1.4446 | ±2.8893 | **+2.076** | **0.0379** | * |
| Site: UW (vs UAB) | +1.2538 | 1.1977 | ±2.3954 | +1.047 | 0.2952 |  |
| **Age (years)** | **-0.5229** | 0.0489 | ±0.0979 | **-10.683** | **1.22e-26** | *** |
| BMI (kg/m2) | -0.0513 | 0.0816 | ±0.1632 | -0.629 | 0.5294 |  |
| Hypertension | -1.1139 | 1.1670 | ±2.3340 | -0.955 | 0.3398 |  |
| High cholesterol | +0.9923 | 1.0880 | ±2.1759 | +0.912 | 0.3617 |  |
| Kidney disease | -2.5618 | 1.4682 | ±2.9364 | -1.745 | 0.0810 | . |
| **Circulatory disease** | **-3.7925** | 1.2742 | ±2.5484 | **-2.976** | **0.0029** | ** |
| Avg. daily range (mg/dL) | +0.0099 | 0.0159 | ±0.0319 | +0.619 | 0.5360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **690**, R² = **0.1884**, Adj R² = **0.1752**, F-statistic = **14.30** (p = **5.25e-25**), Residual SE = **13.494** on **678** df, AIC = **5561.1**, BIC = **5615.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2982** | 4.3285 | ±8.6571 | **+13.237** | **5.34e-40** | *** |
| Education: graduate level (vs college) | -0.1935 | 1.1669 | ±2.3339 | -0.166 | 0.8683 |  |
| Education: high school or below (vs college) | +3.0185 | 1.7500 | ±3.5001 | +1.725 | 0.0846 | . |
| **Site: UCSD (vs UAB)** | **+3.0105** | 1.4518 | ±2.9036 | **+2.074** | **0.0381** | * |
| Site: UW (vs UAB) | +1.3642 | 1.2037 | ±2.4075 | +1.133 | 0.2571 |  |
| **Age (years)** | **-0.5195** | 0.0486 | ±0.0971 | **-10.698** | **1.04e-26** | *** |
| BMI (kg/m2) | -0.0694 | 0.0825 | ±0.1650 | -0.841 | 0.4006 |  |
| Hypertension | -1.2401 | 1.1695 | ±2.3390 | -1.060 | 0.2890 |  |
| High cholesterol | +1.0181 | 1.0839 | ±2.1677 | +0.939 | 0.3476 |  |
| Kidney disease | -2.5142 | 1.4350 | ±2.8699 | -1.752 | 0.0798 | . |
| **Circulatory disease** | **-3.9380** | 1.2740 | ±2.5479 | **-3.091** | **0.0020** | ** |
| SD of daily means (mg/dL) | +0.1128 | 0.0741 | ±0.1481 | +1.523 | 0.1277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.08** (p = **1.36e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2483** | 5.1961 | ±10.3921 | **+11.595** | **4.37e-31** | *** |
| Education: graduate level (vs college) | -0.3204 | 1.1497 | ±2.2994 | -0.279 | 0.7805 |  |
| Education: high school or below (vs college) | +2.9538 | 1.7534 | ±3.5068 | +1.685 | 0.0921 | . |
| **Site: UCSD (vs UAB)** | **+3.0078** | 1.4432 | ±2.8864 | **+2.084** | **0.0371** | * |
| Site: UW (vs UAB) | +1.2484 | 1.1982 | ±2.3964 | +1.042 | 0.2974 |  |
| **Age (years)** | **-0.5229** | 0.0490 | ±0.0979 | **-10.678** | **1.28e-26** | *** |
| BMI (kg/m2) | -0.0630 | 0.0832 | ±0.1664 | -0.758 | 0.4487 |  |
| Hypertension | -1.1304 | 1.1677 | ±2.3354 | -0.968 | 0.3330 |  |
| High cholesterol | +0.9948 | 1.0896 | ±2.1792 | +0.913 | 0.3613 |  |
| Kidney disease | -2.4728 | 1.4389 | ±2.8777 | -1.719 | 0.0857 | . |
| **Circulatory disease** | **-3.8481** | 1.2756 | ±2.5512 | **-3.017** | **0.0026** | ** |
| Time in range 70-180, pooled (%) | -0.0204 | 0.0240 | ±0.0480 | -0.853 | 0.3939 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **690**, R² = **0.1859**, Adj R² = **0.1727**, F-statistic = **14.07** (p = **1.38e-24**), Residual SE = **13.514** on **678** df, AIC = **5563.2**, BIC = **5617.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2222** | 5.2062 | ±10.4124 | **+11.567** | **6.03e-31** | *** |
| Education: graduate level (vs college) | -0.3270 | 1.1486 | ±2.2973 | -0.285 | 0.7759 |  |
| Education: high school or below (vs college) | +2.9527 | 1.7526 | ±3.5052 | +1.685 | 0.0920 | . |
| **Site: UCSD (vs UAB)** | **+3.0128** | 1.4418 | ±2.8837 | **+2.090** | **0.0367** | * |
| Site: UW (vs UAB) | +1.2474 | 1.1976 | ±2.3952 | +1.042 | 0.2976 |  |
| **Age (years)** | **-0.5232** | 0.0490 | ±0.0980 | **-10.674** | **1.35e-26** | *** |
| BMI (kg/m2) | -0.0629 | 0.0833 | ±0.1666 | -0.755 | 0.4504 |  |
| Hypertension | -1.1271 | 1.1674 | ±2.3347 | -0.966 | 0.3343 |  |
| High cholesterol | +0.9927 | 1.0896 | ±2.1791 | +0.911 | 0.3623 |  |
| Kidney disease | -2.4786 | 1.4399 | ±2.8797 | -1.721 | 0.0852 | . |
| **Circulatory disease** | **-3.8441** | 1.2761 | ±2.5521 | **-3.012** | **0.0026** | ** |
| Avg. daily time in range 70-180 (%) | -0.0199 | 0.0238 | ±0.0476 | -0.835 | 0.4038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1866**, Adj R² = **0.1734**, F-statistic = **14.14** (p = **1.06e-24**), Residual SE = **13.509** on **678** df, AIC = **5562.6**, BIC = **5617.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8970** | 4.4412 | ±8.8825 | **+13.261** | **3.88e-40** | *** |
| Education: graduate level (vs college) | -0.4128 | 1.1374 | ±2.2748 | -0.363 | 0.7166 |  |
| Education: high school or below (vs college) | +3.0260 | 1.7614 | ±3.5228 | +1.718 | 0.0858 | . |
| Site: UCSD (vs UAB) | +2.8142 | 1.4707 | ±2.9414 | +1.914 | 0.0557 | . |
| Site: UW (vs UAB) | +1.0618 | 1.2238 | ±2.4476 | +0.868 | 0.3856 |  |
| **Age (years)** | **-0.5247** | 0.0493 | ±0.0985 | **-10.653** | **1.68e-26** | *** |
| BMI (kg/m2) | -0.0484 | 0.0818 | ±0.1636 | -0.591 | 0.5543 |  |
| Hypertension | -1.0417 | 1.1668 | ±2.3337 | -0.893 | 0.3720 |  |
| High cholesterol | +0.8899 | 1.0816 | ±2.1631 | +0.823 | 0.4106 |  |
| Kidney disease | -2.3877 | 1.4250 | ±2.8499 | -1.676 | 0.0938 | . |
| **Circulatory disease** | **-3.6682** | 1.2787 | ±2.5573 | **-2.869** | **0.0041** | ** |
| Any reading < 54 during wear (0/1) | -1.4558 | 1.2208 | ±2.4416 | -1.192 | 0.2331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1864**, Adj R² = **0.1732**, F-statistic = **14.12** (p = **1.13e-24**), Residual SE = **13.510** on **678** df, AIC = **5562.8**, BIC = **5617.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6657** | 4.3744 | ±8.7489 | **+13.411** | **5.21e-41** | *** |
| Education: graduate level (vs college) | -0.4530 | 1.1395 | ±2.2790 | -0.398 | 0.6910 |  |
| Education: high school or below (vs college) | +3.0202 | 1.7671 | ±3.5341 | +1.709 | 0.0874 | . |
| Site: UCSD (vs UAB) | +2.8072 | 1.4669 | ±2.9338 | +1.914 | 0.0557 | . |
| Site: UW (vs UAB) | +1.0055 | 1.2228 | ±2.4456 | +0.822 | 0.4109 |  |
| **Age (years)** | **-0.5207** | 0.0488 | ±0.0977 | **-10.663** | **1.51e-26** | *** |
| BMI (kg/m2) | -0.0533 | 0.0815 | ±0.1630 | -0.654 | 0.5133 |  |
| Hypertension | -1.0967 | 1.1604 | ±2.3207 | -0.945 | 0.3446 |  |
| High cholesterol | +0.8617 | 1.0864 | ±2.1727 | +0.793 | 0.4277 |  |
| Kidney disease | -2.4050 | 1.4221 | ±2.8443 | -1.691 | 0.0908 | . |
| **Circulatory disease** | **-3.8098** | 1.2737 | ±2.5474 | **-2.991** | **0.0028** | ** |
| Time < 54 (%) | -0.9754 | 1.1328 | ±2.2657 | -0.861 | 0.3892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **690**, R² = **0.1875**, Adj R² = **0.1743**, F-statistic = **14.23** (p = **7.31e-25**), Residual SE = **13.501** on **678** df, AIC = **5561.8**, BIC = **5616.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6815** | 4.3692 | ±8.7384 | **+13.431** | **3.99e-41** | *** |
| Education: graduate level (vs college) | -0.4629 | 1.1402 | ±2.2804 | -0.406 | 0.6848 |  |
| Education: high school or below (vs college) | +2.9822 | 1.7667 | ±3.5334 | +1.688 | 0.0914 | . |
| Site: UCSD (vs UAB) | +2.7688 | 1.4695 | ±2.9390 | +1.884 | 0.0595 | . |
| Site: UW (vs UAB) | +0.9402 | 1.2245 | ±2.4490 | +0.768 | 0.4426 |  |
| **Age (years)** | **-0.5204** | 0.0489 | ±0.0977 | **-10.651** | **1.73e-26** | *** |
| BMI (kg/m2) | -0.0518 | 0.0813 | ±0.1626 | -0.637 | 0.5240 |  |
| Hypertension | -1.0810 | 1.1592 | ±2.3183 | -0.933 | 0.3510 |  |
| High cholesterol | +0.8053 | 1.0862 | ±2.1724 | +0.741 | 0.4585 |  |
| Kidney disease | -2.3806 | 1.4212 | ±2.8423 | -1.675 | 0.0939 | . |
| **Circulatory disease** | **-3.8285** | 1.2730 | ±2.5461 | **-3.007** | **0.0026** | ** |
| Avg. daily time < 54 (%) | -1.4735 | 0.8642 | ±1.7283 | -1.705 | 0.0882 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **690**, R² = **0.1879**, Adj R² = **0.1748**, F-statistic = **14.26** (p = **6.19e-25**), Residual SE = **13.497** on **678** df, AIC = **5561.5**, BIC = **5615.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7691** | 4.3579 | ±8.7158 | **+13.486** | **1.90e-41** | *** |
| Education: graduate level (vs college) | -0.5140 | 1.1344 | ±2.2688 | -0.453 | 0.6505 |  |
| Education: high school or below (vs college) | +3.0052 | 1.7674 | ±3.5347 | +1.700 | 0.0891 | . |
| Site: UCSD (vs UAB) | +2.7137 | 1.4659 | ±2.9318 | +1.851 | 0.0641 | . |
| Site: UW (vs UAB) | +0.9012 | 1.2218 | ±2.4436 | +0.738 | 0.4607 |  |
| **Age (years)** | **-0.5193** | 0.0488 | ±0.0975 | **-10.647** | **1.80e-26** | *** |
| BMI (kg/m2) | -0.0496 | 0.0813 | ±0.1626 | -0.610 | 0.5416 |  |
| Hypertension | -1.0399 | 1.1570 | ±2.3139 | -0.899 | 0.3688 |  |
| High cholesterol | +0.7597 | 1.0801 | ±2.1602 | +0.703 | 0.4818 |  |
| Kidney disease | -2.3603 | 1.4196 | ±2.8391 | -1.663 | 0.0964 | . |
| **Circulatory disease** | **-3.9001** | 1.2707 | ±2.5414 | **-3.069** | **0.0021** | ** |
| Time 54-69, pooled (%) | -0.8032 | 0.4391 | ±0.8783 | -1.829 | 0.0674 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **690**, R² = **0.1887**, Adj R² = **0.1755**, F-statistic = **14.33** (p = **4.61e-25**), Residual SE = **13.491** on **678** df, AIC = **5560.8**, BIC = **5615.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7132** | 4.3546 | ±8.7092 | **+13.483** | **1.97e-41** | *** |
| Education: graduate level (vs college) | -0.5264 | 1.1345 | ±2.2689 | -0.464 | 0.6426 |  |
| Education: high school or below (vs college) | +2.9799 | 1.7630 | ±3.5261 | +1.690 | 0.0910 | . |
| Site: UCSD (vs UAB) | +2.6885 | 1.4680 | ±2.9360 | +1.831 | 0.0670 | . |
| Site: UW (vs UAB) | +0.8563 | 1.2247 | ±2.4494 | +0.699 | 0.4844 |  |
| **Age (years)** | **-0.5183** | 0.0487 | ±0.0975 | **-10.634** | **2.08e-26** | *** |
| BMI (kg/m2) | -0.0487 | 0.0813 | ±0.1627 | -0.599 | 0.5492 |  |
| Hypertension | -1.0295 | 1.1568 | ±2.3136 | -0.890 | 0.3735 |  |
| High cholesterol | +0.7335 | 1.0775 | ±2.1550 | +0.681 | 0.4960 |  |
| Kidney disease | -2.3473 | 1.4194 | ±2.8389 | -1.654 | 0.0982 | . |
| **Circulatory disease** | **-3.9132** | 1.2723 | ±2.5446 | **-3.076** | **0.0021** | ** |
| **Avg. daily time 54-69 (%)** | **-0.8328** | 0.4057 | ±0.8113 | **-2.053** | **0.0401** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **690**, R² = **0.1882**, Adj R² = **0.1750**, F-statistic = **14.29** (p = **5.67e-25**), Residual SE = **13.496** on **678** df, AIC = **5561.3**, BIC = **5615.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8568** | 4.3683 | ±8.7365 | **+13.474** | **2.23e-41** | *** |
| Education: graduate level (vs college) | -0.5285 | 1.1370 | ±2.2740 | -0.465 | 0.6420 |  |
| Education: high school or below (vs college) | +2.9721 | 1.7676 | ±3.5351 | +1.681 | 0.0927 | . |
| Site: UCSD (vs UAB) | +2.6952 | 1.4702 | ±2.9404 | +1.833 | 0.0668 | . |
| Site: UW (vs UAB) | +0.8749 | 1.2252 | ±2.4504 | +0.714 | 0.4752 |  |
| **Age (years)** | **-0.5188** | 0.0488 | ±0.0975 | **-10.639** | **1.95e-26** | *** |
| BMI (kg/m2) | -0.0523 | 0.0812 | ±0.1623 | -0.645 | 0.5192 |  |
| Hypertension | -1.0532 | 1.1576 | ±2.3153 | -0.910 | 0.3629 |  |
| High cholesterol | +0.7448 | 1.0816 | ±2.1632 | +0.689 | 0.4911 |  |
| Kidney disease | -2.3801 | 1.4189 | ±2.8379 | -1.677 | 0.0935 | . |
| **Circulatory disease** | **-3.8994** | 1.2711 | ±2.5422 | **-3.068** | **0.0022** | ** |
| **Time < 70 (%)** | **-0.6094** | 0.2834 | ±0.5668 | **-2.151** | **0.0315** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **690**, R² = **0.1890**, Adj R² = **0.1759**, F-statistic = **14.37** (p = **4.01e-25**), Residual SE = **13.488** on **678** df, AIC = **5560.5**, BIC = **5615.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7764** | 4.3604 | ±8.7207 | **+13.480** | **2.06e-41** | *** |
| Education: graduate level (vs college) | -0.5322 | 1.1371 | ±2.2742 | -0.468 | 0.6397 |  |
| Education: high school or below (vs college) | +2.9501 | 1.7640 | ±3.5280 | +1.672 | 0.0945 | . |
| Site: UCSD (vs UAB) | +2.6729 | 1.4717 | ±2.9434 | +1.816 | 0.0693 | . |
| Site: UW (vs UAB) | +0.8292 | 1.2274 | ±2.4548 | +0.676 | 0.4993 |  |
| **Age (years)** | **-0.5182** | 0.0488 | ±0.0975 | **-10.630** | **2.16e-26** | *** |
| BMI (kg/m2) | -0.0501 | 0.0812 | ±0.1624 | -0.617 | 0.5370 |  |
| Hypertension | -1.0369 | 1.1573 | ±2.3146 | -0.896 | 0.3703 |  |
| High cholesterol | +0.7129 | 1.0799 | ±2.1598 | +0.660 | 0.5091 |  |
| Kidney disease | -2.3543 | 1.4188 | ±2.8376 | -1.659 | 0.0970 | . |
| **Circulatory disease** | **-3.9115** | 1.2724 | ±2.5448 | **-3.074** | **0.0021** | ** |
| **Avg. daily time < 70 (%)** | **-0.6528** | 0.2729 | ±0.5459 | **-2.392** | **0.0168** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1849**, Adj R² = **0.1717**, F-statistic = **13.99** (p = **2.01e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.1027** | 5.8368 | ±11.6735 | **+10.126** | **4.24e-24** | *** |
| Education: graduate level (vs college) | -0.3523 | 1.1598 | ±2.3197 | -0.304 | 0.7613 |  |
| Education: high school or below (vs college) | +3.0795 | 1.7455 | ±3.4909 | +1.764 | 0.0777 | . |
| **Site: UCSD (vs UAB)** | **+2.9314** | 1.4482 | ±2.8964 | **+2.024** | **0.0429** | * |
| Site: UW (vs UAB) | +1.1713 | 1.1988 | ±2.3977 | +0.977 | 0.3286 |  |
| **Age (years)** | **-0.5220** | 0.0485 | ±0.0969 | **-10.769** | **4.80e-27** | *** |
| BMI (kg/m2) | -0.0507 | 0.0824 | ±0.1648 | -0.615 | 0.5384 |  |
| Hypertension | -1.1070 | 1.1649 | ±2.3298 | -0.950 | 0.3419 |  |
| High cholesterol | +0.9730 | 1.0918 | ±2.1837 | +0.891 | 0.3729 |  |
| Kidney disease | -2.3979 | 1.4340 | ±2.8679 | -1.672 | 0.0945 | . |
| **Circulatory disease** | **-3.7741** | 1.2800 | ±2.5601 | **-2.948** | **0.0032** | ** |
| Time 54-250, pooled (%) | -0.0080 | 0.0361 | ±0.0722 | -0.223 | 0.8239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1717**, F-statistic = **13.99** (p = **1.99e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.2591** | 5.8030 | ±11.6060 | **+10.212** | **1.76e-24** | *** |
| Education: graduate level (vs college) | -0.3486 | 1.1597 | ±2.3194 | -0.301 | 0.7637 |  |
| Education: high school or below (vs college) | +3.0734 | 1.7470 | ±3.4941 | +1.759 | 0.0785 | . |
| **Site: UCSD (vs UAB)** | **+2.9350** | 1.4480 | ±2.8961 | **+2.027** | **0.0427** | * |
| Site: UW (vs UAB) | +1.1756 | 1.1995 | ±2.3990 | +0.980 | 0.3270 |  |
| **Age (years)** | **-0.5219** | 0.0485 | ±0.0971 | **-10.753** | **5.72e-27** | *** |
| BMI (kg/m2) | -0.0512 | 0.0823 | ±0.1646 | -0.622 | 0.5342 |  |
| Hypertension | -1.1077 | 1.1648 | ±2.3295 | -0.951 | 0.3416 |  |
| High cholesterol | +0.9745 | 1.0914 | ±2.1829 | +0.893 | 0.3719 |  |
| Kidney disease | -2.4037 | 1.4351 | ±2.8702 | -1.675 | 0.0939 | . |
| **Circulatory disease** | **-3.7787** | 1.2795 | ±2.5590 | **-2.953** | **0.0031** | ** |
| Avg. daily time 54-250 (%) | -0.0096 | 0.0354 | ±0.0709 | -0.271 | 0.7864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1873**, Adj R² = **0.1741**, F-statistic = **14.20** (p = **8.02e-25**), Residual SE = **13.503** on **678** df, AIC = **5562.0**, BIC = **5616.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4441** | 4.3687 | ±8.7374 | **+13.378** | **8.15e-41** | *** |
| Education: graduate level (vs college) | -0.4008 | 1.1338 | ±2.2677 | -0.353 | 0.7237 |  |
| Education: high school or below (vs college) | +2.9338 | 1.7741 | ±3.5482 | +1.654 | 0.0982 | . |
| **Site: UCSD (vs UAB)** | **+3.0267** | 1.4518 | ±2.9035 | **+2.085** | **0.0371** | * |
| Site: UW (vs UAB) | +1.1961 | 1.2118 | ±2.4237 | +0.987 | 0.3236 |  |
| **Age (years)** | **-0.5288** | 0.0497 | ±0.0993 | **-10.650** | **1.75e-26** | *** |
| BMI (kg/m2) | -0.0715 | 0.0824 | ±0.1648 | -0.867 | 0.3858 |  |
| Hypertension | -1.1158 | 1.1648 | ±2.3297 | -0.958 | 0.3381 |  |
| High cholesterol | +0.9740 | 1.0869 | ±2.1738 | +0.896 | 0.3702 |  |
| Kidney disease | -2.5047 | 1.4312 | ±2.8623 | -1.750 | 0.0801 | . |
| **Circulatory disease** | **-3.8765** | 1.2709 | ±2.5418 | **-3.050** | **0.0023** | ** |
| Time 181-250, pooled (%) | +0.0514 | 0.0378 | ±0.0756 | +1.358 | 0.1745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **690**, R² = **0.1870**, Adj R² = **0.1739**, F-statistic = **14.18** (p = **8.81e-25**), Residual SE = **13.505** on **678** df, AIC = **5562.2**, BIC = **5616.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4292** | 4.3696 | ±8.7392 | **+13.372** | **8.84e-41** | *** |
| Education: graduate level (vs college) | -0.4060 | 1.1340 | ±2.2680 | -0.358 | 0.7203 |  |
| Education: high school or below (vs college) | +2.9268 | 1.7695 | ±3.5390 | +1.654 | 0.0981 | . |
| **Site: UCSD (vs UAB)** | **+3.0348** | 1.4501 | ±2.9003 | **+2.093** | **0.0364** | * |
| Site: UW (vs UAB) | +1.2038 | 1.2103 | ±2.4207 | +0.995 | 0.3199 |  |
| **Age (years)** | **-0.5281** | 0.0497 | ±0.0993 | **-10.636** | **2.02e-26** | *** |
| BMI (kg/m2) | -0.0702 | 0.0828 | ±0.1656 | -0.848 | 0.3964 |  |
| Hypertension | -1.1145 | 1.1651 | ±2.3302 | -0.957 | 0.3388 |  |
| High cholesterol | +0.9694 | 1.0875 | ±2.1751 | +0.891 | 0.3727 |  |
| Kidney disease | -2.5029 | 1.4318 | ±2.8636 | -1.748 | 0.0804 | . |
| **Circulatory disease** | **-3.8603** | 1.2731 | ±2.5463 | **-3.032** | **0.0024** | ** |
| Avg. daily time 181-250 (%) | +0.0478 | 0.0371 | ±0.0742 | +1.287 | 0.1980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **690**, R² = **0.1862**, Adj R² = **0.1729**, F-statistic = **14.10** (p = **1.25e-24**), Residual SE = **13.512** on **678** df, AIC = **5563.0**, BIC = **5617.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2071** | 4.3380 | ±8.6759 | **+13.418** | **4.74e-41** | *** |
| Education: graduate level (vs college) | -0.3212 | 1.1480 | ±2.2961 | -0.280 | 0.7797 |  |
| Education: high school or below (vs college) | +2.9348 | 1.7534 | ±3.5069 | +1.674 | 0.0942 | . |
| **Site: UCSD (vs UAB)** | **+3.0078** | 1.4443 | ±2.8887 | **+2.082** | **0.0373** | * |
| Site: UW (vs UAB) | +1.2480 | 1.1993 | ±2.3985 | +1.041 | 0.2980 |  |
| **Age (years)** | **-0.5228** | 0.0489 | ±0.0979 | **-10.682** | **1.24e-26** | *** |
| BMI (kg/m2) | -0.0644 | 0.0832 | ±0.1664 | -0.774 | 0.4388 |  |
| Hypertension | -1.1315 | 1.1674 | ±2.3349 | -0.969 | 0.3324 |  |
| High cholesterol | +0.9893 | 1.0891 | ±2.1782 | +0.908 | 0.3637 |  |
| Kidney disease | -2.4805 | 1.4383 | ±2.8766 | -1.725 | 0.0846 | . |
| **Circulatory disease** | **-3.8613** | 1.2756 | ±2.5512 | **-3.027** | **0.0025** | ** |
| Time > 180 (%) | +0.0222 | 0.0238 | ±0.0475 | +0.933 | 0.3507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1861**, Adj R² = **0.1729**, F-statistic = **14.10** (p = **1.25e-24**), Residual SE = **13.512** on **678** df, AIC = **5563.0**, BIC = **5617.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2340** | 4.3423 | ±8.6846 | **+13.411** | **5.23e-41** | *** |
| Education: graduate level (vs college) | -0.3269 | 1.1471 | ±2.2942 | -0.285 | 0.7756 |  |
| Education: high school or below (vs college) | +2.9295 | 1.7523 | ±3.5047 | +1.672 | 0.0946 | . |
| **Site: UCSD (vs UAB)** | **+3.0152** | 1.4429 | ±2.8858 | **+2.090** | **0.0366** | * |
| Site: UW (vs UAB) | +1.2486 | 1.1987 | ±2.3975 | +1.042 | 0.2976 |  |
| **Age (years)** | **-0.5230** | 0.0490 | ±0.0980 | **-10.677** | **1.30e-26** | *** |
| BMI (kg/m2) | -0.0645 | 0.0833 | ±0.1666 | -0.774 | 0.4388 |  |
| Hypertension | -1.1282 | 1.1670 | ±2.3341 | -0.967 | 0.3337 |  |
| High cholesterol | +0.9872 | 1.0890 | ±2.1780 | +0.906 | 0.3647 |  |
| Kidney disease | -2.4881 | 1.4392 | ±2.8784 | -1.729 | 0.0838 | . |
| **Circulatory disease** | **-3.8589** | 1.2762 | ±2.5523 | **-3.024** | **0.0025** | ** |
| Avg. daily time > 180 (%) | +0.0220 | 0.0236 | ±0.0473 | +0.931 | 0.3520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **690**, R² = **0.1866**, Adj R² = **0.1734**, F-statistic = **14.14** (p = **1.04e-24**), Residual SE = **13.508** on **678** df, AIC = **5562.6**, BIC = **5617.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2983** | 4.3610 | ±8.7219 | **+13.368** | **9.28e-41** | *** |
| Education: graduate level (vs college) | -0.2700 | 1.1594 | ±2.3187 | -0.233 | 0.8159 |  |
| Education: high school or below (vs college) | +2.9409 | 1.7508 | ±3.5016 | +1.680 | 0.0930 | . |
| **Site: UCSD (vs UAB)** | **+3.0293** | 1.4418 | ±2.8836 | **+2.101** | **0.0356** | * |
| Site: UW (vs UAB) | +1.2391 | 1.2007 | ±2.4013 | +1.032 | 0.3020 |  |
| **Age (years)** | **-0.5203** | 0.0487 | ±0.0974 | **-10.684** | **1.21e-26** | *** |
| BMI (kg/m2) | -0.0707 | 0.0832 | ±0.1663 | -0.850 | 0.3956 |  |
| Hypertension | -1.1285 | 1.1664 | ±2.3328 | -0.968 | 0.3333 |  |
| High cholesterol | +1.0211 | 1.0908 | ±2.1815 | +0.936 | 0.3492 |  |
| Kidney disease | -2.4402 | 1.4356 | ±2.8712 | -1.700 | 0.0892 | . |
| **Circulatory disease** | **-3.8728** | 1.2745 | ±2.5489 | **-3.039** | **0.0024** | ** |
| Nocturnal time > 180 (%) | +0.0237 | 0.0221 | ±0.0441 | +1.075 | 0.2822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1717**, F-statistic = **13.99** (p = **1.99e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2893** | 4.3268 | ±8.6536 | **+13.472** | **2.29e-41** | *** |
| Education: graduate level (vs college) | -0.3489 | 1.1590 | ±2.3180 | -0.301 | 0.7634 |  |
| Education: high school or below (vs college) | +3.0726 | 1.7451 | ±3.4902 | +1.761 | 0.0783 | . |
| **Site: UCSD (vs UAB)** | **+2.9333** | 1.4486 | ±2.8973 | **+2.025** | **0.0429** | * |
| Site: UW (vs UAB) | +1.1752 | 1.1991 | ±2.3981 | +0.980 | 0.3270 |  |
| **Age (years)** | **-0.5218** | 0.0485 | ±0.0969 | **-10.768** | **4.86e-27** | *** |
| BMI (kg/m2) | -0.0511 | 0.0824 | ±0.1649 | -0.620 | 0.5354 |  |
| Hypertension | -1.1086 | 1.1649 | ±2.3298 | -0.952 | 0.3413 |  |
| High cholesterol | +0.9734 | 1.0914 | ±2.1828 | +0.892 | 0.3725 |  |
| Kidney disease | -2.4009 | 1.4341 | ±2.8682 | -1.674 | 0.0941 | . |
| **Circulatory disease** | **-3.7778** | 1.2801 | ±2.5602 | **-2.951** | **0.0032** | ** |
| Time > 250 (%) | +0.0094 | 0.0361 | ±0.0723 | +0.259 | 0.7953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 690)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **690**, R² = **0.1850**, Adj R² = **0.1718**, F-statistic = **13.99** (p = **1.96e-24**), Residual SE = **13.522** on **678** df, AIC = **5564.0**, BIC = **5618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2887** | 4.3338 | ±8.6676 | **+13.450** | **3.09e-41** | *** |
| Education: graduate level (vs college) | -0.3446 | 1.1590 | ±2.3180 | -0.297 | 0.7662 |  |
| Education: high school or below (vs college) | +3.0655 | 1.7467 | ±3.4935 | +1.755 | 0.0793 | . |
| **Site: UCSD (vs UAB)** | **+2.9373** | 1.4484 | ±2.8968 | **+2.028** | **0.0426** | * |
| Site: UW (vs UAB) | +1.1800 | 1.1998 | ±2.3995 | +0.984 | 0.3253 |  |
| **Age (years)** | **-0.5218** | 0.0485 | ±0.0971 | **-10.752** | **5.83e-27** | *** |
| BMI (kg/m2) | -0.0516 | 0.0823 | ±0.1646 | -0.627 | 0.5307 |  |
| Hypertension | -1.1092 | 1.1647 | ±2.3294 | -0.952 | 0.3409 |  |
| High cholesterol | +0.9750 | 1.0910 | ±2.1820 | +0.894 | 0.3715 |  |
| Kidney disease | -2.4073 | 1.4351 | ±2.8702 | -1.677 | 0.0935 | . |
| **Circulatory disease** | **-3.7832** | 1.2796 | ±2.5591 | **-2.957** | **0.0031** | ** |
| Avg. daily time > 250 (%) | +0.0112 | 0.0355 | ±0.0710 | +0.315 | 0.7528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 692; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **692**, R² = **0.1495**, Adj R² = **0.1371**, F-statistic = **11.97** (p = **3.43e-19**), Residual SE = **8.427** on **681** df, AIC = **4924.7**, BIC = **4974.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.6611** | 2.7711 | ±5.5422 | **+25.499** | **2.00e-143** | *** |
| Education: graduate level (vs college) | -0.8187 | 0.7236 | ±1.4472 | -1.131 | 0.2579 |  |
| **Education: high school or below (vs college)** | **+2.4427** | 0.9751 | ±1.9501 | **+2.505** | **0.0122** | * |
| Site: UCSD (vs UAB) | -1.1672 | 0.8975 | ±1.7951 | -1.300 | 0.1935 |  |
| Site: UW (vs UAB) | -0.9820 | 0.7917 | ±1.5835 | -1.240 | 0.2148 |  |
| **Age (years)** | **-0.2068** | 0.0317 | ±0.0634 | **-6.518** | **7.14e-11** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0497 | ±0.0994 | **+4.337** | **1.45e-05** | *** |
| Hypertension | +0.5415 | 0.7341 | ±1.4682 | +0.738 | 0.4608 |  |
| High cholesterol | +0.6128 | 0.7107 | ±1.4214 | +0.862 | 0.3886 |  |
| Kidney disease | +0.1586 | 0.9577 | ±1.9154 | +0.166 | 0.8685 |  |
| Circulatory disease | -0.3380 | 0.8512 | ±1.7024 | -0.397 | 0.6913 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **692**, R² = **0.1814**, Adj R² = **0.1682**, F-statistic = **13.70** (p = **6.61e-24**), Residual SE = **8.274** on **680** df, AIC = **4900.2**, BIC = **4954.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.5088** | 3.1417 | ±6.2833 | **+20.215** | **7.22e-91** | *** |
| Education: graduate level (vs college) | -0.5201 | 0.7191 | ±1.4383 | -0.723 | 0.4695 |  |
| Education: high school or below (vs college) | +1.8275 | 0.9573 | ±1.9146 | +1.909 | 0.0563 | . |
| Site: UCSD (vs UAB) | -1.0529 | 0.8920 | ±1.7840 | -1.180 | 0.2379 |  |
| Site: UW (vs UAB) | -0.6675 | 0.7844 | ±1.5689 | -0.851 | 0.3948 |  |
| **Age (years)** | **-0.2051** | 0.0311 | ±0.0622 | **-6.593** | **4.31e-11** | *** |
| **BMI (kg/m2)** | **+0.1692** | 0.0510 | ±0.1019 | **+3.320** | **9.00e-04** | *** |
| Hypertension | +0.3259 | 0.7226 | ±1.4453 | +0.451 | 0.6520 |  |
| High cholesterol | +0.5543 | 0.7037 | ±1.4075 | +0.788 | 0.4309 |  |
| Kidney disease | +0.2162 | 0.9544 | ±1.9087 | +0.227 | 0.8208 |  |
| Circulatory disease | -0.4929 | 0.8418 | ±1.6836 | -0.586 | 0.5582 |  |
| **HbA1c (%)** | **+1.2497** | 0.2375 | ±0.4750 | **+5.262** | **1.43e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **692**, R² = **0.1856**, Adj R² = **0.1724**, F-statistic = **14.09** (p = **1.29e-24**), Residual SE = **8.253** on **680** df, AIC = **4896.7**, BIC = **4951.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.5039** | 3.0427 | ±6.0855 | **+21.199** | **9.71e-100** | *** |
| Education: graduate level (vs college) | -0.6400 | 0.7124 | ±1.4248 | -0.898 | 0.3690 |  |
| Education: high school or below (vs college) | +1.8142 | 0.9526 | ±1.9051 | +1.905 | 0.0568 | . |
| Site: UCSD (vs UAB) | -0.9541 | 0.8901 | ±1.7801 | -1.072 | 0.2837 |  |
| Site: UW (vs UAB) | -0.6778 | 0.7800 | ±1.5599 | -0.869 | 0.3848 |  |
| **Age (years)** | **-0.2024** | 0.0308 | ±0.0615 | **-6.580** | **4.72e-11** | *** |
| **BMI (kg/m2)** | **+0.1725** | 0.0506 | ±0.1011 | **+3.412** | **6.44e-04** | *** |
| Hypertension | +0.3775 | 0.7220 | ±1.4439 | +0.523 | 0.6011 |  |
| High cholesterol | +0.6541 | 0.7005 | ±1.4009 | +0.934 | 0.3504 |  |
| Kidney disease | -0.0628 | 0.9491 | ±1.8981 | -0.066 | 0.9472 |  |
| Circulatory disease | -0.6870 | 0.8398 | ±1.6796 | -0.818 | 0.4133 |  |
| **Mean glucose (mg/dL)** | **+0.0447** | 0.0087 | ±0.0174 | **+5.137** | **2.79e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **692**, R² = **0.1856**, Adj R² = **0.1724**, F-statistic = **14.09** (p = **1.29e-24**), Residual SE = **8.253** on **680** df, AIC = **4896.7**, BIC = **4951.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3157** | 3.7405 | ±7.4809 | **+15.590** | **8.45e-55** | *** |
| Education: graduate level (vs college) | -0.6400 | 0.7124 | ±1.4248 | -0.898 | 0.3690 |  |
| Education: high school or below (vs college) | +1.8142 | 0.9526 | ±1.9051 | +1.905 | 0.0568 | . |
| Site: UCSD (vs UAB) | -0.9541 | 0.8901 | ±1.7801 | -1.072 | 0.2837 |  |
| Site: UW (vs UAB) | -0.6778 | 0.7800 | ±1.5599 | -0.869 | 0.3848 |  |
| **Age (years)** | **-0.2024** | 0.0308 | ±0.0615 | **-6.580** | **4.72e-11** | *** |
| **BMI (kg/m2)** | **+0.1725** | 0.0506 | ±0.1011 | **+3.412** | **6.44e-04** | *** |
| Hypertension | +0.3775 | 0.7220 | ±1.4439 | +0.523 | 0.6011 |  |
| High cholesterol | +0.6541 | 0.7005 | ±1.4009 | +0.934 | 0.3504 |  |
| Kidney disease | -0.0628 | 0.9491 | ±1.8981 | -0.066 | 0.9472 |  |
| Circulatory disease | -0.6870 | 0.8398 | ±1.6796 | -0.818 | 0.4133 |  |
| **GMI (%)** | **+1.8695** | 0.3639 | ±0.7279 | **+5.137** | **2.79e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **692**, R² = **0.1803**, Adj R² = **0.1671**, F-statistic = **13.60** (p = **1.00e-23**), Residual SE = **8.279** on **680** df, AIC = **4901.1**, BIC = **4955.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.4858** | 3.0047 | ±6.0094 | **+21.795** | **2.61e-105** | *** |
| Education: graduate level (vs college) | -0.6094 | 0.7195 | ±1.4390 | -0.847 | 0.3970 |  |
| **Education: high school or below (vs college)** | **+1.9125** | 0.9441 | ±1.8882 | **+2.026** | **0.0428** | * |
| Site: UCSD (vs UAB) | -0.9858 | 0.8936 | ±1.7871 | -1.103 | 0.2699 |  |
| Site: UW (vs UAB) | -0.7904 | 0.7798 | ±1.5595 | -1.014 | 0.3107 |  |
| **Age (years)** | **-0.1976** | 0.0311 | ±0.0623 | **-6.346** | **2.21e-10** | *** |
| **BMI (kg/m2)** | **+0.1664** | 0.0509 | ±0.1017 | **+3.272** | **0.0011** | ** |
| Hypertension | +0.4208 | 0.7243 | ±1.4485 | +0.581 | 0.5613 |  |
| High cholesterol | +0.6844 | 0.7051 | ±1.4101 | +0.971 | 0.3317 |  |
| Kidney disease | +0.1381 | 0.9477 | ±1.8953 | +0.146 | 0.8841 |  |
| Circulatory disease | -0.6507 | 0.8405 | ±1.6810 | -0.774 | 0.4389 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0392** | 0.0082 | ±0.0164 | **+4.785** | **1.71e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1682**, Adj R² = **0.1548**, F-statistic = **12.50** (p = **1.09e-21**), Residual SE = **8.340** on **680** df, AIC = **4911.3**, BIC = **4965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.3490** | 2.8961 | ±5.7922 | **+23.255** | **1.26e-119** | *** |
| Education: graduate level (vs college) | -0.6301 | 0.7197 | ±1.4393 | -0.876 | 0.3812 |  |
| **Education: high school or below (vs college)** | **+2.0102** | 0.9766 | ±1.9533 | **+2.058** | **0.0396** | * |
| Site: UCSD (vs UAB) | -0.9465 | 0.8982 | ±1.7965 | -1.054 | 0.2920 |  |
| Site: UW (vs UAB) | -0.5554 | 0.7958 | ±1.5916 | -0.698 | 0.4853 |  |
| **Age (years)** | **-0.2094** | 0.0310 | ±0.0619 | **-6.761** | **1.37e-11** | *** |
| **BMI (kg/m2)** | **+0.1930** | 0.0507 | ±0.1014 | **+3.809** | **1.40e-04** | *** |
| Hypertension | +0.3464 | 0.7353 | ±1.4706 | +0.471 | 0.6376 |  |
| High cholesterol | +0.7355 | 0.7086 | ±1.4172 | +1.038 | 0.2993 |  |
| Kidney disease | -0.4803 | 0.9678 | ±1.9356 | -0.496 | 0.6197 |  |
| Circulatory disease | -0.5179 | 0.8485 | ±1.6970 | -0.610 | 0.5416 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1085** | 0.0308 | ±0.0616 | **+3.523** | **4.26e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1649**, Adj R² = **0.1514**, F-statistic = **12.20** (p = **3.92e-21**), Residual SE = **8.357** on **680** df, AIC = **4914.1**, BIC = **4968.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5402** | 2.9020 | ±5.8039 | **+23.274** | **8.14e-120** | *** |
| Education: graduate level (vs college) | -0.6781 | 0.7180 | ±1.4360 | -0.944 | 0.3449 |  |
| **Education: high school or below (vs college)** | **+2.0139** | 0.9839 | ±1.9678 | **+2.047** | **0.0407** | * |
| Site: UCSD (vs UAB) | -0.9644 | 0.8990 | ±1.7981 | -1.073 | 0.2834 |  |
| Site: UW (vs UAB) | -0.6273 | 0.7966 | ±1.5931 | -0.788 | 0.4310 |  |
| **Age (years)** | **-0.2106** | 0.0311 | ±0.0622 | **-6.773** | **1.26e-11** | *** |
| **BMI (kg/m2)** | **+0.2009** | 0.0503 | ±0.1007 | **+3.990** | **6.60e-05** | *** |
| Hypertension | +0.3761 | 0.7356 | ±1.4712 | +0.511 | 0.6092 |  |
| High cholesterol | +0.7132 | 0.7083 | ±1.4165 | +1.007 | 0.3139 |  |
| Kidney disease | -0.4679 | 0.9783 | ±1.9567 | -0.478 | 0.6325 |  |
| Circulatory disease | -0.4868 | 0.8465 | ±1.6930 | -0.575 | 0.5653 |  |
| **Avg. daily SD (mg/dL)** | **+0.1117** | 0.0346 | ±0.0693 | **+3.224** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **692**, R² = **0.1496**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.22e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.6**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8456** | 3.0576 | ±6.1152 | **+23.170** | **9.09e-119** | *** |
| Education: graduate level (vs college) | -0.8238 | 0.7245 | ±1.4490 | -1.137 | 0.2555 |  |
| **Education: high school or below (vs college)** | **+2.4475** | 0.9789 | ±1.9578 | **+2.500** | **0.0124** | * |
| Site: UCSD (vs UAB) | -1.1741 | 0.9025 | ±1.8050 | -1.301 | 0.1933 |  |
| Site: UW (vs UAB) | -0.9950 | 0.8039 | ±1.6079 | -1.238 | 0.2158 |  |
| **Age (years)** | **-0.2065** | 0.0319 | ±0.0638 | **-6.475** | **9.45e-11** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0498 | ±0.0995 | **+4.329** | **1.49e-05** | *** |
| Hypertension | +0.5467 | 0.7399 | ±1.4799 | +0.739 | 0.4600 |  |
| High cholesterol | +0.6072 | 0.7159 | ±1.4317 | +0.848 | 0.3963 |  |
| Kidney disease | +0.1825 | 0.9871 | ±1.9742 | +0.185 | 0.8534 |  |
| Circulatory disease | -0.3388 | 0.8519 | ±1.7037 | -0.398 | 0.6909 |  |
| CV (%) | -0.0082 | 0.0607 | ±0.1214 | -0.136 | 0.8921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **692**, R² = **0.1496**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.22e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.7**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8317** | 3.2219 | ±6.4439 | **+21.984** | **4.09e-107** | *** |
| Education: graduate level (vs college) | -0.8153 | 0.7239 | ±1.4478 | -1.126 | 0.2601 |  |
| **Education: high school or below (vs college)** | **+2.4393** | 0.9798 | ±1.9596 | **+2.490** | **0.0128** | * |
| Site: UCSD (vs UAB) | -1.1639 | 0.8998 | ±1.7995 | -1.294 | 0.1958 |  |
| Site: UW (vs UAB) | -0.9731 | 0.8017 | ±1.6034 | -1.214 | 0.2248 |  |
| **Age (years)** | **-0.2069** | 0.0318 | ±0.0636 | **-6.505** | **7.78e-11** | *** |
| **BMI (kg/m2)** | **+0.2156** | 0.0498 | ±0.0996 | **+4.331** | **1.48e-05** | *** |
| Hypertension | +0.5371 | 0.7395 | ±1.4789 | +0.726 | 0.4676 |  |
| High cholesterol | +0.6150 | 0.7126 | ±1.4252 | +0.863 | 0.3881 |  |
| Kidney disease | +0.1413 | 0.9747 | ±1.9493 | +0.145 | 0.8847 |  |
| Circulatory disease | -0.3391 | 0.8525 | ±1.7049 | -0.398 | 0.6908 |  |
| Mean / SD ratio | -0.0369 | 0.3363 | ±0.6725 | -0.110 | 0.9125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1496**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.22e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.6**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.4394** | 3.1779 | ±6.3559 | **+22.165** | **7.45e-109** | *** |
| Education: graduate level (vs college) | -0.8223 | 0.7234 | ±1.4467 | -1.137 | 0.2556 |  |
| **Education: high school or below (vs college)** | **+2.4479** | 0.9793 | ±1.9586 | **+2.500** | **0.0124** | * |
| Site: UCSD (vs UAB) | -1.1706 | 0.8999 | ±1.7997 | -1.301 | 0.1933 |  |
| Site: UW (vs UAB) | -0.9930 | 0.7994 | ±1.5989 | -1.242 | 0.2142 |  |
| **Age (years)** | **-0.2064** | 0.0319 | ±0.0638 | **-6.473** | **9.62e-11** | *** |
| **BMI (kg/m2)** | **+0.2151** | 0.0497 | ±0.0994 | **+4.327** | **1.51e-05** | *** |
| Hypertension | +0.5475 | 0.7392 | ±1.4784 | +0.741 | 0.4589 |  |
| High cholesterol | +0.6089 | 0.7128 | ±1.4257 | +0.854 | 0.3930 |  |
| Kidney disease | +0.1811 | 0.9767 | ±1.9534 | +0.185 | 0.8529 |  |
| Circulatory disease | -0.3384 | 0.8519 | ±1.7037 | -0.397 | 0.6912 |  |
| Avg. daily mean/SD | +0.0412 | 0.2632 | ±0.5264 | +0.157 | 0.8755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **692**, R² = **0.1566**, Adj R² = **0.1429**, F-statistic = **11.47** (p = **9.02e-20**), Residual SE = **8.399** on **680** df, AIC = **4920.9**, BIC = **4975.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.4568** | 3.4299 | ±6.8599 | **+19.375** | **1.24e-83** | *** |
| Education: graduate level (vs college) | -0.6935 | 0.7236 | ±1.4472 | -0.958 | 0.3379 |  |
| **Education: high school or below (vs college)** | **+2.3273** | 0.9693 | ±1.9386 | **+2.401** | **0.0164** | * |
| Site: UCSD (vs UAB) | -0.9844 | 0.9057 | ±1.8113 | -1.087 | 0.2771 |  |
| Site: UW (vs UAB) | -0.6703 | 0.8143 | ±1.6286 | -0.823 | 0.4104 |  |
| **Age (years)** | **-0.2010** | 0.0316 | ±0.0632 | **-6.363** | **1.98e-10** | *** |
| **BMI (kg/m2)** | **+0.2130** | 0.0500 | ±0.1000 | **+4.258** | **2.06e-05** | *** |
| Hypertension | +0.5763 | 0.7337 | ±1.4673 | +0.786 | 0.4321 |  |
| High cholesterol | +0.7308 | 0.7145 | ±1.4289 | +1.023 | 0.3064 |  |
| Kidney disease | -0.0151 | 0.9710 | ±1.9421 | -0.016 | 0.9876 |  |
| Circulatory disease | -0.3585 | 0.8477 | ±1.6953 | -0.423 | 0.6724 |  |
| **MAG (mg/dL/h)** | **+0.0811** | 0.0364 | ±0.0728 | **+2.228** | **0.0259** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **692**, R² = **0.1604**, Adj R² = **0.1468**, F-statistic = **11.81** (p = **2.14e-20**), Residual SE = **8.380** on **680** df, AIC = **4917.8**, BIC = **4972.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.5804** | 3.1023 | ±6.2045 | **+21.462** | **3.54e-102** | *** |
| Education: graduate level (vs college) | -0.7091 | 0.7204 | ±1.4408 | -0.984 | 0.3250 |  |
| **Education: high school or below (vs college)** | **+2.0805** | 0.9818 | ±1.9635 | **+2.119** | **0.0341** | * |
| Site: UCSD (vs UAB) | -0.9517 | 0.9003 | ±1.8007 | -1.057 | 0.2905 |  |
| Site: UW (vs UAB) | -0.6652 | 0.8015 | ±1.6030 | -0.830 | 0.4066 |  |
| **Age (years)** | **-0.2064** | 0.0313 | ±0.0626 | **-6.593** | **4.32e-11** | *** |
| **BMI (kg/m2)** | **+0.2083** | 0.0501 | ±0.1002 | **+4.157** | **3.23e-05** | *** |
| Hypertension | +0.4782 | 0.7331 | ±1.4663 | +0.652 | 0.5142 |  |
| High cholesterol | +0.7080 | 0.7106 | ±1.4212 | +0.996 | 0.3191 |  |
| Kidney disease | -0.3614 | 0.9826 | ±1.9652 | -0.368 | 0.7131 |  |
| Circulatory disease | -0.4505 | 0.8470 | ±1.6940 | -0.532 | 0.5948 |  |
| **Avg. daily range (mg/dL)** | **+0.0278** | 0.0098 | ±0.0195 | **+2.845** | **0.0044** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **692**, R² = **0.1767**, Adj R² = **0.1634**, F-statistic = **13.27** (p = **4.19e-23**), Residual SE = **8.298** on **680** df, AIC = **4904.2**, BIC = **4958.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.7937** | 2.7763 | ±5.5526 | **+24.779** | **1.51e-135** | *** |
| Education: graduate level (vs college) | -0.5093 | 0.7246 | ±1.4493 | -0.703 | 0.4822 |  |
| **Education: high school or below (vs college)** | **+2.2176** | 0.9520 | ±1.9041 | **+2.329** | **0.0198** | * |
| Site: UCSD (vs UAB) | -1.0390 | 0.8945 | ±1.7891 | -1.162 | 0.2454 |  |
| Site: UW (vs UAB) | -0.6018 | 0.7856 | ±1.5713 | -0.766 | 0.4437 |  |
| **Age (years)** | **-0.2004** | 0.0311 | ±0.0622 | **-6.446** | **1.15e-10** | *** |
| **BMI (kg/m2)** | **+0.1810** | 0.0500 | ±0.1000 | **+3.619** | **2.96e-04** | *** |
| Hypertension | +0.2772 | 0.7316 | ±1.4632 | +0.379 | 0.7047 |  |
| High cholesterol | +0.7285 | 0.7101 | ±1.4203 | +1.026 | 0.3049 |  |
| Kidney disease | -0.0624 | 0.9411 | ±1.8823 | -0.066 | 0.9471 |  |
| Circulatory disease | -0.6397 | 0.8496 | ±1.6992 | -0.753 | 0.4515 |  |
| **SD of daily means (mg/dL)** | **+0.1910** | 0.0439 | ±0.0878 | **+4.347** | **1.38e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **692**, R² = **0.1883**, Adj R² = **0.1751**, F-statistic = **14.34** (p = **4.49e-25**), Residual SE = **8.239** on **680** df, AIC = **4894.4**, BIC = **4948.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.4612** | 2.9896 | ±5.9792 | **+25.910** | **5.09e-148** | *** |
| Education: graduate level (vs college) | -0.6123 | 0.7131 | ±1.4262 | -0.859 | 0.3905 |  |
| Education: high school or below (vs college) | +1.7914 | 0.9515 | ±1.9030 | +1.883 | 0.0597 | . |
| Site: UCSD (vs UAB) | -0.8487 | 0.8912 | ±1.7825 | -0.952 | 0.3409 |  |
| Site: UW (vs UAB) | -0.5797 | 0.7806 | ±1.5613 | -0.743 | 0.4577 |  |
| **Age (years)** | **-0.2062** | 0.0308 | ±0.0616 | **-6.696** | **2.14e-11** | *** |
| **BMI (kg/m2)** | **+0.1640** | 0.0508 | ±0.1016 | **+3.230** | **0.0012** | ** |
| Hypertension | +0.3999 | 0.7245 | ±1.4489 | +0.552 | 0.5809 |  |
| High cholesterol | +0.7469 | 0.7027 | ±1.4054 | +1.063 | 0.2878 |  |
| Kidney disease | -0.1814 | 0.9478 | ±1.8955 | -0.191 | 0.8482 |  |
| Circulatory disease | -0.6809 | 0.8354 | ±1.6709 | -0.815 | 0.4150 |  |
| **Time in range 70-180, pooled (%)** | **-0.0748** | 0.0141 | ±0.0283 | **-5.287** | **1.24e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **692**, R² = **0.1871**, Adj R² = **0.1740**, F-statistic = **14.23** (p = **7.07e-25**), Residual SE = **8.245** on **680** df, AIC = **4895.4**, BIC = **4949.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.4083** | 2.9979 | ±5.9959 | **+25.820** | **5.22e-147** | *** |
| Education: graduate level (vs college) | -0.6352 | 0.7137 | ±1.4275 | -0.890 | 0.3735 |  |
| Education: high school or below (vs college) | +1.7846 | 0.9515 | ±1.9030 | +1.876 | 0.0607 | . |
| Site: UCSD (vs UAB) | -0.8284 | 0.8919 | ±1.7838 | -0.929 | 0.3530 |  |
| Site: UW (vs UAB) | -0.5813 | 0.7813 | ±1.5627 | -0.744 | 0.4569 |  |
| **Age (years)** | **-0.2071** | 0.0309 | ±0.0617 | **-6.710** | **1.94e-11** | *** |
| **BMI (kg/m2)** | **+0.1642** | 0.0510 | ±0.1019 | **+3.222** | **0.0013** | ** |
| Hypertension | +0.4114 | 0.7247 | ±1.4495 | +0.568 | 0.5702 |  |
| High cholesterol | +0.7394 | 0.7033 | ±1.4066 | +1.051 | 0.2931 |  |
| Kidney disease | -0.2046 | 0.9498 | ±1.8995 | -0.215 | 0.8294 |  |
| Circulatory disease | -0.6679 | 0.8367 | ±1.6734 | -0.798 | 0.4247 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0731** | 0.0140 | ±0.0281 | **-5.208** | **1.91e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1504**, Adj R² = **0.1367**, F-statistic = **10.95** (p = **8.87e-19**), Residual SE = **8.429** on **680** df, AIC = **4926.0**, BIC = **4980.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8958** | 2.7963 | ±5.5926 | **+25.353** | **8.25e-142** | *** |
| Education: graduate level (vs college) | -0.8345 | 0.7251 | ±1.4501 | -1.151 | 0.2498 |  |
| **Education: high school or below (vs college)** | **+2.4106** | 0.9775 | ±1.9551 | **+2.466** | **0.0137** | * |
| Site: UCSD (vs UAB) | -1.2071 | 0.9026 | ±1.8052 | -1.337 | 0.1811 |  |
| Site: UW (vs UAB) | -1.0160 | 0.7963 | ±1.5926 | -1.276 | 0.2020 |  |
| **Age (years)** | **-0.2076** | 0.0318 | ±0.0636 | **-6.524** | **6.83e-11** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0500 | ±0.1000 | **+4.312** | **1.62e-05** | *** |
| Hypertension | +0.5687 | 0.7360 | ±1.4720 | +0.773 | 0.4397 |  |
| High cholesterol | +0.5774 | 0.7171 | ±1.4343 | +0.805 | 0.4207 |  |
| Kidney disease | +0.1554 | 0.9600 | ±1.9200 | +0.162 | 0.8714 |  |
| Circulatory disease | -0.3011 | 0.8527 | ±1.7053 | -0.353 | 0.7240 |  |
| Any reading < 54 during wear (0/1) | -0.6350 | 0.7622 | ±1.5244 | -0.833 | 0.4048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1495**, Adj R² = **0.1358**, F-statistic = **10.87** (p = **1.23e-18**), Residual SE = **8.433** on **680** df, AIC = **4926.7**, BIC = **4981.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.6545** | 2.7792 | ±5.5585 | **+25.422** | **1.43e-142** | *** |
| Education: graduate level (vs college) | -0.8170 | 0.7250 | ±1.4500 | -1.127 | 0.2598 |  |
| **Education: high school or below (vs college)** | **+2.4449** | 0.9774 | ±1.9548 | **+2.501** | **0.0124** | * |
| Site: UCSD (vs UAB) | -1.1647 | 0.9021 | ±1.8043 | -1.291 | 0.1967 |  |
| Site: UW (vs UAB) | -0.9790 | 0.7979 | ±1.5959 | -1.227 | 0.2198 |  |
| **Age (years)** | **-0.2068** | 0.0318 | ±0.0636 | **-6.505** | **7.76e-11** | *** |
| **BMI (kg/m2)** | **+0.2156** | 0.0499 | ±0.0998 | **+4.320** | **1.56e-05** | *** |
| Hypertension | +0.5414 | 0.7344 | ±1.4687 | +0.737 | 0.4610 |  |
| High cholesterol | +0.6151 | 0.7143 | ±1.4286 | +0.861 | 0.3891 |  |
| Kidney disease | +0.1591 | 0.9577 | ±1.9154 | +0.166 | 0.8680 |  |
| Circulatory disease | -0.3367 | 0.8523 | ±1.7045 | -0.395 | 0.6928 |  |
| Time < 54 (%) | +0.0221 | 0.2663 | ±0.5326 | +0.083 | 0.9340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1499**, Adj R² = **0.1361**, F-statistic = **10.90** (p = **1.09e-18**), Residual SE = **8.432** on **680** df, AIC = **4926.4**, BIC = **4980.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7279** | 2.7799 | ±5.5599 | **+25.442** | **8.62e-143** | *** |
| Education: graduate level (vs college) | -0.8376 | 0.7246 | ±1.4491 | -1.156 | 0.2477 |  |
| **Education: high school or below (vs college)** | **+2.4137** | 0.9771 | ±1.9542 | **+2.470** | **0.0135** | * |
| Site: UCSD (vs UAB) | -1.1989 | 0.9029 | ±1.8057 | -1.328 | 0.1842 |  |
| Site: UW (vs UAB) | -1.0253 | 0.7997 | ±1.5995 | -1.282 | 0.1998 |  |
| **Age (years)** | **-0.2062** | 0.0318 | ±0.0636 | **-6.482** | **9.07e-11** | *** |
| **BMI (kg/m2)** | **+0.2148** | 0.0500 | ±0.0999 | **+4.299** | **1.72e-05** | *** |
| Hypertension | +0.5451 | 0.7343 | ±1.4686 | +0.742 | 0.4578 |  |
| High cholesterol | +0.5782 | 0.7150 | ±1.4300 | +0.809 | 0.4187 |  |
| Kidney disease | +0.1591 | 0.9582 | ±1.9164 | +0.166 | 0.8681 |  |
| Circulatory disease | -0.3537 | 0.8522 | ±1.7045 | -0.415 | 0.6781 |  |
| Avg. daily time < 54 (%) | -0.3203 | 0.6032 | ±1.2063 | -0.531 | 0.5954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1505**, Adj R² = **0.1367**, F-statistic = **10.95** (p = **8.77e-19**), Residual SE = **8.429** on **680** df, AIC = **4925.9**, BIC = **4980.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7902** | 2.7798 | ±5.5597 | **+25.465** | **4.76e-143** | *** |
| Education: graduate level (vs college) | -0.8648 | 0.7259 | ±1.4519 | -1.191 | 0.2336 |  |
| **Education: high school or below (vs college)** | **+2.4057** | 0.9756 | ±1.9512 | **+2.466** | **0.0137** | * |
| Site: UCSD (vs UAB) | -1.2338 | 0.9034 | ±1.8069 | -1.366 | 0.1720 |  |
| Site: UW (vs UAB) | -1.0604 | 0.8038 | ±1.6076 | -1.319 | 0.1871 |  |
| **Age (years)** | **-0.2055** | 0.0318 | ±0.0637 | **-6.454** | **1.09e-10** | *** |
| **BMI (kg/m2)** | **+0.2152** | 0.0499 | ±0.0998 | **+4.312** | **1.62e-05** | *** |
| Hypertension | +0.5605 | 0.7358 | ±1.4717 | +0.762 | 0.4462 |  |
| High cholesterol | +0.5448 | 0.7178 | ±1.4355 | +0.759 | 0.4478 |  |
| Kidney disease | +0.1676 | 0.9587 | ±1.9174 | +0.175 | 0.8613 |  |
| Circulatory disease | -0.3846 | 0.8531 | ±1.7061 | -0.451 | 0.6521 |  |
| Time 54-69, pooled (%) | -0.2670 | 0.3651 | ±0.7302 | -0.731 | 0.4647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **692**, R² = **0.1510**, Adj R² = **0.1373**, F-statistic = **11.00** (p = **7.07e-19**), Residual SE = **8.426** on **680** df, AIC = **4925.5**, BIC = **4979.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7873** | 2.7771 | ±5.5542 | **+25.489** | **2.58e-143** | *** |
| Education: graduate level (vs college) | -0.8763 | 0.7255 | ±1.4510 | -1.208 | 0.2271 |  |
| **Education: high school or below (vs college)** | **+2.3905** | 0.9749 | ±1.9497 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | -1.2531 | 0.9039 | ±1.8077 | -1.386 | 0.1656 |  |
| Site: UW (vs UAB) | -1.0889 | 0.8043 | ±1.6087 | -1.354 | 0.1758 |  |
| **Age (years)** | **-0.2050** | 0.0319 | ±0.0637 | **-6.432** | **1.26e-10** | *** |
| **BMI (kg/m2)** | **+0.2155** | 0.0499 | ±0.0999 | **+4.316** | **1.59e-05** | *** |
| Hypertension | +0.5673 | 0.7360 | ±1.4720 | +0.771 | 0.4409 |  |
| High cholesterol | +0.5249 | 0.7169 | ±1.4339 | +0.732 | 0.4641 |  |
| Kidney disease | +0.1740 | 0.9591 | ±1.9181 | +0.181 | 0.8560 |  |
| Circulatory disease | -0.3963 | 0.8539 | ±1.7078 | -0.464 | 0.6426 |  |
| Avg. daily time 54-69 (%) | -0.3176 | 0.3583 | ±0.7166 | -0.887 | 0.3753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **692**, R² = **0.1500**, Adj R² = **0.1363**, F-statistic = **10.91** (p = **1.04e-18**), Residual SE = **8.431** on **680** df, AIC = **4926.3**, BIC = **4980.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7701** | 2.7833 | ±5.5666 | **+25.427** | **1.28e-142** | *** |
| Education: graduate level (vs college) | -0.8537 | 0.7265 | ±1.4530 | -1.175 | 0.2399 |  |
| **Education: high school or below (vs college)** | **+2.4097** | 0.9769 | ±1.9539 | **+2.467** | **0.0136** | * |
| Site: UCSD (vs UAB) | -1.2173 | 0.9050 | ±1.8099 | -1.345 | 0.1786 |  |
| Site: UW (vs UAB) | -1.0420 | 0.8049 | ±1.6098 | -1.295 | 0.1955 |  |
| **Age (years)** | **-0.2058** | 0.0319 | ±0.0637 | **-6.460** | **1.05e-10** | *** |
| **BMI (kg/m2)** | **+0.2147** | 0.0500 | ±0.0999 | **+4.298** | **1.73e-05** | *** |
| Hypertension | +0.5516 | 0.7344 | ±1.4687 | +0.751 | 0.4526 |  |
| High cholesterol | +0.5627 | 0.7181 | ±1.4362 | +0.784 | 0.4333 |  |
| Kidney disease | +0.1601 | 0.9584 | ±1.9168 | +0.167 | 0.8673 |  |
| Circulatory disease | -0.3700 | 0.8529 | ±1.7058 | -0.434 | 0.6644 |  |
| Time < 70 (%) | -0.1393 | 0.2063 | ±0.4126 | -0.675 | 0.4994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **692**, R² = **0.1508**, Adj R² = **0.1371**, F-statistic = **10.98** (p = **7.71e-19**), Residual SE = **8.427** on **680** df, AIC = **4925.6**, BIC = **4980.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7937** | 2.7801 | ±5.5601 | **+25.465** | **4.83e-143** | *** |
| Education: graduate level (vs college) | -0.8713 | 0.7256 | ±1.4511 | -1.201 | 0.2298 |  |
| **Education: high school or below (vs college)** | **+2.3869** | 0.9758 | ±1.9516 | **+2.446** | **0.0144** | * |
| Site: UCSD (vs UAB) | -1.2480 | 0.9050 | ±1.8100 | -1.379 | 0.1679 |  |
| Site: UW (vs UAB) | -1.0851 | 0.8051 | ±1.6102 | -1.348 | 0.1777 |  |
| **Age (years)** | **-0.2052** | 0.0319 | ±0.0637 | **-6.439** | **1.21e-10** | *** |
| **BMI (kg/m2)** | **+0.2150** | 0.0500 | ±0.0999 | **+4.303** | **1.69e-05** | *** |
| Hypertension | +0.5618 | 0.7347 | ±1.4694 | +0.765 | 0.4445 |  |
| High cholesterol | +0.5286 | 0.7174 | ±1.4348 | +0.737 | 0.4612 |  |
| Kidney disease | +0.1696 | 0.9588 | ±1.9176 | +0.177 | 0.8596 |  |
| Circulatory disease | -0.3889 | 0.8534 | ±1.7069 | -0.456 | 0.6486 |  |
| Avg. daily time < 70 (%) | -0.2188 | 0.2304 | ±0.4608 | -0.950 | 0.3423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1634**, Adj R² = **0.1499**, F-statistic = **12.08** (p = **6.76e-21**), Residual SE = **8.364** on **680** df, AIC = **4915.3**, BIC = **4969.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.6501** | 3.2199 | ±6.4398 | **+23.805** | **2.96e-125** | *** |
| Education: graduate level (vs college) | -0.6176 | 0.7253 | ±1.4506 | -0.851 | 0.3945 |  |
| **Education: high school or below (vs college)** | **+2.1193** | 0.9577 | ±1.9155 | **+2.213** | **0.0269** | * |
| Site: UCSD (vs UAB) | -1.0369 | 0.8948 | ±1.7895 | -1.159 | 0.2465 |  |
| Site: UW (vs UAB) | -0.7196 | 0.7949 | ±1.5898 | -0.905 | 0.3653 |  |
| **Age (years)** | **-0.1986** | 0.0314 | ±0.0629 | **-6.319** | **2.63e-10** | *** |
| **BMI (kg/m2)** | **+0.1987** | 0.0504 | ±0.1009 | **+3.939** | **8.18e-05** | *** |
| Hypertension | +0.4552 | 0.7319 | ±1.4639 | +0.622 | 0.5340 |  |
| High cholesterol | +0.6918 | 0.7081 | ±1.4162 | +0.977 | 0.3285 |  |
| Kidney disease | +0.0229 | 0.9594 | ±1.9187 | +0.024 | 0.9810 |  |
| Circulatory disease | -0.4942 | 0.8416 | ±1.6832 | -0.587 | 0.5570 |  |
| **Time 54-250, pooled (%)** | **-0.0662** | 0.0210 | ±0.0420 | **-3.153** | **0.0016** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1636**, Adj R² = **0.1500**, F-statistic = **12.09** (p = **6.43e-21**), Residual SE = **8.364** on **680** df, AIC = **4915.2**, BIC = **4969.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.8630** | 3.2618 | ±6.5235 | **+23.565** | **8.82e-123** | *** |
| Education: graduate level (vs college) | -0.6215 | 0.7249 | ±1.4497 | -0.857 | 0.3912 |  |
| **Education: high school or below (vs college)** | **+2.1186** | 0.9584 | ±1.9167 | **+2.211** | **0.0271** | * |
| Site: UCSD (vs UAB) | -1.0336 | 0.8947 | ±1.7894 | -1.155 | 0.2480 |  |
| Site: UW (vs UAB) | -0.7271 | 0.7947 | ±1.5893 | -0.915 | 0.3602 |  |
| **Age (years)** | **-0.1995** | 0.0314 | ±0.0629 | **-6.349** | **2.17e-10** | *** |
| **BMI (kg/m2)** | **+0.1980** | 0.0506 | ±0.1011 | **+3.916** | **8.99e-05** | *** |
| Hypertension | +0.4614 | 0.7315 | ±1.4629 | +0.631 | 0.5282 |  |
| High cholesterol | +0.6936 | 0.7081 | ±1.4161 | +0.980 | 0.3273 |  |
| Kidney disease | +0.0029 | 0.9602 | ±1.9204 | +0.003 | 0.9976 |  |
| Circulatory disease | -0.5034 | 0.8423 | ±1.6847 | -0.598 | 0.5501 |  |
| **Avg. daily time 54-250 (%)** | **-0.0675** | 0.0216 | ±0.0432 | **-3.125** | **0.0018** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1890**, Adj R² = **0.1759**, F-statistic = **14.41** (p = **3.35e-25**), Residual SE = **8.235** on **680** df, AIC = **4893.8**, BIC = **4948.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7822** | 2.7138 | ±5.4275 | **+26.083** | **5.71e-150** | *** |
| Education: graduate level (vs college) | -0.8757 | 0.7067 | ±1.4134 | -1.239 | 0.2153 |  |
| **Education: high school or below (vs college)** | **+1.9407** | 0.9763 | ±1.9525 | **+1.988** | **0.0468** | * |
| Site: UCSD (vs UAB) | -0.9087 | 0.8892 | ±1.7785 | -1.022 | 0.3068 |  |
| Site: UW (vs UAB) | -0.8398 | 0.7719 | ±1.5439 | -1.088 | 0.2767 |  |
| **Age (years)** | **-0.2208** | 0.0313 | ±0.0625 | **-7.065** | **1.61e-12** | *** |
| **BMI (kg/m2)** | **+0.1604** | 0.0502 | ±0.1004 | **+3.195** | **0.0014** | ** |
| Hypertension | +0.4758 | 0.7224 | ±1.4449 | +0.659 | 0.5101 |  |
| High cholesterol | +0.6565 | 0.7015 | ±1.4030 | +0.936 | 0.3494 |  |
| Kidney disease | -0.1535 | 0.9369 | ±1.8738 | -0.164 | 0.8699 |  |
| Circulatory disease | -0.6420 | 0.8432 | ±1.6863 | -0.761 | 0.4464 |  |
| **Time 181-250, pooled (%)** | **+0.1267** | 0.0231 | ±0.0462 | **+5.484** | **4.17e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **692**, R² = **0.1873**, Adj R² = **0.1741**, F-statistic = **14.25** (p = **6.56e-25**), Residual SE = **8.244** on **680** df, AIC = **4895.2**, BIC = **4949.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7535** | 2.7164 | ±5.4328 | **+26.047** | **1.45e-149** | *** |
| Education: graduate level (vs college) | -0.8909 | 0.7086 | ±1.4172 | -1.257 | 0.2087 |  |
| **Education: high school or below (vs college)** | **+1.9129** | 0.9722 | ±1.9445 | **+1.967** | **0.0491** | * |
| Site: UCSD (vs UAB) | -0.8776 | 0.8904 | ±1.7808 | -0.986 | 0.3243 |  |
| Site: UW (vs UAB) | -0.8160 | 0.7735 | ±1.5470 | -1.055 | 0.2914 |  |
| **Age (years)** | **-0.2196** | 0.0313 | ±0.0625 | **-7.022** | **2.18e-12** | *** |
| **BMI (kg/m2)** | **+0.1617** | 0.0504 | ±0.1007 | **+3.211** | **0.0013** | ** |
| Hypertension | +0.4794 | 0.7235 | ±1.4471 | +0.663 | 0.5076 |  |
| High cholesterol | +0.6441 | 0.7025 | ±1.4050 | +0.917 | 0.3592 |  |
| Kidney disease | -0.1585 | 0.9395 | ±1.8790 | -0.169 | 0.8660 |  |
| Circulatory disease | -0.6106 | 0.8452 | ±1.6904 | -0.722 | 0.4700 |  |
| **Avg. daily time 181-250 (%)** | **+0.1215** | 0.0226 | ±0.0452 | **+5.372** | **7.81e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **692**, R² = **0.1881**, Adj R² = **0.1750**, F-statistic = **14.32** (p = **4.74e-25**), Residual SE = **8.240** on **680** df, AIC = **4894.5**, BIC = **4949.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.0454** | 2.7276 | ±5.4552 | **+25.680** | **1.94e-145** | *** |
| Education: graduate level (vs college) | -0.6329 | 0.7126 | ±1.4252 | -0.888 | 0.3744 |  |
| Education: high school or below (vs college) | +1.7804 | 0.9518 | ±1.9036 | +1.871 | 0.0614 | . |
| Site: UCSD (vs UAB) | -0.8786 | 0.8908 | ±1.7816 | -0.986 | 0.3240 |  |
| Site: UW (vs UAB) | -0.6156 | 0.7792 | ±1.5585 | -0.790 | 0.4295 |  |
| **Age (years)** | **-0.2057** | 0.0308 | ±0.0616 | **-6.677** | **2.43e-11** | *** |
| **BMI (kg/m2)** | **+0.1641** | 0.0509 | ±0.1017 | **+3.226** | **0.0013** | ** |
| Hypertension | +0.4067 | 0.7241 | ±1.4482 | +0.562 | 0.5743 |  |
| High cholesterol | +0.7189 | 0.7020 | ±1.4040 | +1.024 | 0.3058 |  |
| Kidney disease | -0.1772 | 0.9477 | ±1.8954 | -0.187 | 0.8516 |  |
| Circulatory disease | -0.6945 | 0.8354 | ±1.6709 | -0.831 | 0.4058 |  |
| **Time > 180 (%)** | **+0.0741** | 0.0140 | ±0.0280 | **+5.298** | **1.17e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1874**, Adj R² = **0.1743**, F-statistic = **14.26** (p = **6.26e-25**), Residual SE = **8.243** on **680** df, AIC = **4895.1**, BIC = **4949.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.1400** | 2.7324 | ±5.4648 | **+25.670** | **2.56e-145** | *** |
| Education: graduate level (vs college) | -0.6532 | 0.7132 | ±1.4264 | -0.916 | 0.3597 |  |
| Education: high school or below (vs college) | +1.7679 | 0.9515 | ±1.9030 | +1.858 | 0.0632 | . |
| Site: UCSD (vs UAB) | -0.8563 | 0.8914 | ±1.7828 | -0.961 | 0.3367 |  |
| Site: UW (vs UAB) | -0.6168 | 0.7797 | ±1.5595 | -0.791 | 0.4289 |  |
| **Age (years)** | **-0.2065** | 0.0309 | ±0.0617 | **-6.693** | **2.19e-11** | *** |
| **BMI (kg/m2)** | **+0.1642** | 0.0510 | ±0.1021 | **+3.217** | **0.0013** | ** |
| Hypertension | +0.4186 | 0.7242 | ±1.4484 | +0.578 | 0.5633 |  |
| High cholesterol | +0.7110 | 0.7023 | ±1.4046 | +1.012 | 0.3114 |  |
| Kidney disease | -0.1999 | 0.9495 | ±1.8990 | -0.211 | 0.8333 |  |
| Circulatory disease | -0.6839 | 0.8369 | ±1.6737 | -0.817 | 0.4138 |  |
| **Avg. daily time > 180 (%)** | **+0.0729** | 0.0139 | ±0.0278 | **+5.250** | **1.52e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1744**, Adj R² = **0.1611**, F-statistic = **13.06** (p = **1.00e-22**), Residual SE = **8.309** on **680** df, AIC = **4906.1**, BIC = **4960.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.4498** | 2.7561 | ±5.5121 | **+25.562** | **4.06e-144** | *** |
| Education: graduate level (vs college) | -0.5751 | 0.7258 | ±1.4516 | -0.792 | 0.4281 |  |
| **Education: high school or below (vs college)** | **+2.0122** | 0.9440 | ±1.8879 | **+2.132** | **0.0330** | * |
| Site: UCSD (vs UAB) | -0.9144 | 0.8965 | ±1.7931 | -1.020 | 0.3078 |  |
| Site: UW (vs UAB) | -0.7491 | 0.7829 | ±1.5658 | -0.957 | 0.3387 |  |
| **Age (years)** | **-0.2005** | 0.0314 | ±0.0628 | **-6.383** | **1.74e-10** | *** |
| **BMI (kg/m2)** | **+0.1659** | 0.0513 | ±0.1025 | **+3.236** | **0.0012** | ** |
| Hypertension | +0.4602 | 0.7306 | ±1.4613 | +0.630 | 0.5288 |  |
| High cholesterol | +0.7547 | 0.7091 | ±1.4181 | +1.064 | 0.2872 |  |
| Kidney disease | +0.0226 | 0.9484 | ±1.8968 | +0.024 | 0.9810 |  |
| Circulatory disease | -0.6082 | 0.8373 | ±1.6746 | -0.726 | 0.4676 |  |
| **Nocturnal time > 180 (%)** | **+0.0543** | 0.0127 | ±0.0254 | **+4.274** | **1.92e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1634**, Adj R² = **0.1499**, F-statistic = **12.07** (p = **6.80e-21**), Residual SE = **8.364** on **680** df, AIC = **4915.3**, BIC = **4969.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.0477** | 2.7894 | ±5.5788 | **+25.112** | **3.69e-139** | *** |
| Education: graduate level (vs college) | -0.6230 | 0.7251 | ±1.4501 | -0.859 | 0.3903 |  |
| **Education: high school or below (vs college)** | **+2.1131** | 0.9580 | ±1.9160 | **+2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | -1.0442 | 0.8946 | ±1.7893 | -1.167 | 0.2431 |  |
| Site: UW (vs UAB) | -0.7289 | 0.7943 | ±1.5885 | -0.918 | 0.3588 |  |
| **Age (years)** | **-0.1985** | 0.0314 | ±0.0629 | **-6.312** | **2.76e-10** | *** |
| **BMI (kg/m2)** | **+0.1984** | 0.0505 | ±0.1009 | **+3.931** | **8.47e-05** | *** |
| Hypertension | +0.4553 | 0.7319 | ±1.4638 | +0.622 | 0.5339 |  |
| High cholesterol | +0.6848 | 0.7080 | ±1.4159 | +0.967 | 0.3334 |  |
| Kidney disease | +0.0215 | 0.9594 | ±1.9188 | +0.022 | 0.9821 |  |
| Circulatory disease | -0.4978 | 0.8416 | ±1.6833 | -0.591 | 0.5542 |  |
| **Time > 250 (%)** | **+0.0662** | 0.0210 | ±0.0419 | **+3.157** | **0.0016** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 692)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **692**, R² = **0.1637**, Adj R² = **0.1502**, F-statistic = **12.10** (p = **6.10e-21**), Residual SE = **8.363** on **680** df, AIC = **4915.1**, BIC = **4969.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.1249** | 2.7925 | ±5.5850 | **+25.112** | **3.70e-139** | *** |
| Education: graduate level (vs college) | -0.6245 | 0.7247 | ±1.4494 | -0.862 | 0.3888 |  |
| **Education: high school or below (vs college)** | **+2.1109** | 0.9585 | ±1.9170 | **+2.202** | **0.0276** | * |
| Site: UCSD (vs UAB) | -1.0397 | 0.8946 | ±1.7891 | -1.162 | 0.2451 |  |
| Site: UW (vs UAB) | -0.7350 | 0.7940 | ±1.5881 | -0.926 | 0.3546 |  |
| **Age (years)** | **-0.1994** | 0.0314 | ±0.0629 | **-6.343** | **2.26e-10** | *** |
| **BMI (kg/m2)** | **+0.1978** | 0.0506 | ±0.1012 | **+3.909** | **9.27e-05** | *** |
| Hypertension | +0.4618 | 0.7314 | ±1.4627 | +0.631 | 0.5278 |  |
| High cholesterol | +0.6867 | 0.7078 | ±1.4157 | +0.970 | 0.3320 |  |
| Kidney disease | +0.0022 | 0.9602 | ±1.9204 | +0.002 | 0.9982 |  |
| Circulatory disease | -0.5075 | 0.8424 | ±1.6848 | -0.602 | 0.5469 |  |
| **Avg. daily time > 250 (%)** | **+0.0678** | 0.0216 | ±0.0432 | **+3.142** | **0.0017** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 694; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **694**, R² = **0.0405**, Adj R² = **0.0264**, F-statistic = **2.88** (p = **0.0016**), Residual SE = **66.292** on **683** df, AIC = **7801.8**, BIC = **7851.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.3068** | 22.0318 | ±44.0636 | **+17.353** | **1.89e-67** | *** |
| Education: graduate level (vs college) | -1.5602 | 5.6599 | ±11.3197 | -0.276 | 0.7828 |  |
| Education: high school or below (vs college) | -11.0140 | 7.7007 | ±15.4015 | -1.430 | 0.1526 |  |
| **Site: UCSD (vs UAB)** | **-19.1719** | 6.2197 | ±12.4394 | **-3.082** | **0.0021** | ** |
| Site: UW (vs UAB) | +0.3116 | 6.5446 | ±13.0892 | +0.048 | 0.9620 |  |
| Age (years) | +0.1968 | 0.2616 | ±0.5233 | +0.752 | 0.4520 |  |
| **BMI (kg/m2)** | **-0.9525** | 0.3584 | ±0.7168 | **-2.658** | **0.0079** | ** |
| Hypertension | -9.4587 | 5.4709 | ±10.9418 | -1.729 | 0.0838 | . |
| High cholesterol | +0.6950 | 5.1964 | ±10.3928 | +0.134 | 0.8936 |  |
| Kidney disease | -0.7362 | 7.8512 | ±15.7024 | -0.094 | 0.9253 |  |
| **Circulatory disease** | **+16.1730** | 7.5709 | ±15.1417 | **+2.136** | **0.0327** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **694**, R² = **0.0478**, Adj R² = **0.0325**, F-statistic = **3.11** (p = **4.15e-04**), Residual SE = **66.087** on **682** df, AIC = **7798.4**, BIC = **7853.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+408.2180** | 23.9973 | ±47.9946 | **+17.011** | **6.81e-65** | *** |
| Education: graduate level (vs college) | -2.6886 | 5.6984 | ±11.3968 | -0.472 | 0.6371 |  |
| Education: high school or below (vs college) | -8.8992 | 7.6512 | ±15.3023 | -1.163 | 0.2448 |  |
| **Site: UCSD (vs UAB)** | **-19.6161** | 6.2029 | ±12.4058 | **-3.162** | **0.0016** | ** |
| Site: UW (vs UAB) | -0.7953 | 6.5490 | ±13.0981 | -0.121 | 0.9033 |  |
| Age (years) | +0.1920 | 0.2601 | ±0.5202 | +0.738 | 0.4604 |  |
| **BMI (kg/m2)** | **-0.7920** | 0.3720 | ±0.7441 | **-2.129** | **0.0333** | * |
| Hypertension | -8.8530 | 5.4512 | ±10.9024 | -1.624 | 0.1044 |  |
| High cholesterol | +0.9483 | 5.1714 | ±10.3428 | +0.183 | 0.8545 |  |
| Kidney disease | -0.8813 | 7.8517 | ±15.7033 | -0.112 | 0.9106 |  |
| **Circulatory disease** | **+16.7905** | 7.5219 | ±15.0438 | **+2.232** | **0.0256** | * |
| **HbA1c (%)** | **-4.4957** | 1.7375 | ±3.4750 | **-2.587** | **0.0097** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **694**, R² = **0.0410**, Adj R² = **0.0255**, F-statistic = **2.65** (p = **0.0025**), Residual SE = **66.324** on **682** df, AIC = **7803.4**, BIC = **7857.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.6803** | 23.6082 | ±47.2164 | **+16.421** | **1.34e-60** | *** |
| Education: graduate level (vs college) | -1.7571 | 5.6849 | ±11.3697 | -0.309 | 0.7573 |  |
| Education: high school or below (vs college) | -10.5355 | 7.7340 | ±15.4680 | -1.362 | 0.1731 |  |
| **Site: UCSD (vs UAB)** | **-19.3769** | 6.2317 | ±12.4634 | **-3.109** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0549 | 6.5570 | ±13.1141 | +0.008 | 0.9933 |  |
| Age (years) | +0.1943 | 0.2620 | ±0.5240 | +0.742 | 0.4583 |  |
| **BMI (kg/m2)** | **-0.9167** | 0.3691 | ±0.7381 | **-2.484** | **0.0130** | * |
| Hypertension | -9.3648 | 5.4708 | ±10.9416 | -1.712 | 0.0869 | . |
| High cholesterol | +0.6898 | 5.2044 | ±10.4088 | +0.133 | 0.8946 |  |
| Kidney disease | -0.5065 | 7.9097 | ±15.8194 | -0.064 | 0.9489 |  |
| **Circulatory disease** | **+16.4977** | 7.6235 | ±15.2470 | **+2.164** | **0.0305** | * |
| Mean glucose (mg/dL) | -0.0391 | 0.0671 | ±0.1342 | -0.583 | 0.5598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **694**, R² = **0.0410**, Adj R² = **0.0255**, F-statistic = **2.65** (p = **0.0025**), Residual SE = **66.324** on **682** df, AIC = **7803.4**, BIC = **7857.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.0956** | 28.2877 | ±56.5753 | **+13.896** | **6.66e-44** | *** |
| Education: graduate level (vs college) | -1.7571 | 5.6849 | ±11.3697 | -0.309 | 0.7573 |  |
| Education: high school or below (vs college) | -10.5355 | 7.7340 | ±15.4680 | -1.362 | 0.1731 |  |
| **Site: UCSD (vs UAB)** | **-19.3769** | 6.2317 | ±12.4634 | **-3.109** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0549 | 6.5570 | ±13.1141 | +0.008 | 0.9933 |  |
| Age (years) | +0.1943 | 0.2620 | ±0.5240 | +0.742 | 0.4583 |  |
| **BMI (kg/m2)** | **-0.9167** | 0.3691 | ±0.7381 | **-2.484** | **0.0130** | * |
| Hypertension | -9.3648 | 5.4708 | ±10.9416 | -1.712 | 0.0869 | . |
| High cholesterol | +0.6898 | 5.2044 | ±10.4088 | +0.133 | 0.8946 |  |
| Kidney disease | -0.5065 | 7.9097 | ±15.8194 | -0.064 | 0.9489 |  |
| **Circulatory disease** | **+16.4977** | 7.6235 | ±15.2470 | **+2.164** | **0.0305** | * |
| GMI (%) | -1.6360 | 2.8058 | ±5.6117 | -0.583 | 0.5598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **694**, R² = **0.0405**, Adj R² = **0.0250**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.340** on **682** df, AIC = **7803.7**, BIC = **7858.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+383.4633** | 23.3668 | ±46.7336 | **+16.411** | **1.61e-60** | *** |
| Education: graduate level (vs college) | -1.6150 | 5.6923 | ±11.3846 | -0.284 | 0.7766 |  |
| Education: high school or below (vs college) | -10.9105 | 7.7388 | ±15.4776 | -1.410 | 0.1586 |  |
| **Site: UCSD (vs UAB)** | **-19.2221** | 6.2378 | ±12.4757 | **-3.082** | **0.0021** | ** |
| Site: UW (vs UAB) | +0.2702 | 6.5574 | ±13.1149 | +0.041 | 0.9671 |  |
| Age (years) | +0.1950 | 0.2625 | ±0.5249 | +0.743 | 0.4574 |  |
| **BMI (kg/m2)** | **-0.9422** | 0.3722 | ±0.7443 | **-2.532** | **0.0114** | * |
| Hypertension | -9.4456 | 5.4781 | ±10.9562 | -1.724 | 0.0847 | . |
| High cholesterol | +0.6884 | 5.2041 | ±10.4081 | +0.132 | 0.8948 |  |
| Kidney disease | -0.7175 | 7.8737 | ±15.7474 | -0.091 | 0.9274 |  |
| **Circulatory disease** | **+16.2487** | 7.6363 | ±15.2726 | **+2.128** | **0.0334** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0088 | 0.0638 | ±0.1276 | -0.137 | 0.8909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **694**, R² = **0.0461**, Adj R² = **0.0307**, F-statistic = **2.99** (p = **6.62e-04**), Residual SE = **66.147** on **682** df, AIC = **7799.7**, BIC = **7854.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.4000** | 22.8519 | ±45.7037 | **+17.303** | **4.48e-67** | *** |
| Education: graduate level (vs college) | -2.4186 | 5.6886 | ±11.3772 | -0.425 | 0.6707 |  |
| Education: high school or below (vs college) | -9.3165 | 7.6881 | ±15.3763 | -1.212 | 0.2256 |  |
| **Site: UCSD (vs UAB)** | **-20.0176** | 6.2240 | ±12.4480 | **-3.216** | **0.0013** | ** |
| Site: UW (vs UAB) | -1.3950 | 6.5931 | ±13.1862 | -0.212 | 0.8324 |  |
| Age (years) | +0.2113 | 0.2597 | ±0.5194 | +0.813 | 0.4160 |  |
| **BMI (kg/m2)** | **-0.8538** | 0.3685 | ±0.7370 | **-2.317** | **0.0205** | * |
| Hypertension | -8.7931 | 5.4646 | ±10.9292 | -1.609 | 0.1076 |  |
| High cholesterol | +0.2293 | 5.1819 | ±10.3639 | +0.044 | 0.9647 |  |
| Kidney disease | +1.8501 | 8.1919 | ±16.3838 | +0.226 | 0.8213 |  |
| **Circulatory disease** | **+16.8977** | 7.5068 | ±15.0136 | **+2.251** | **0.0244** | * |
| **Glucose SD, pooled (mg/dL)** | **-0.4407** | 0.2173 | ±0.4347 | **-2.028** | **0.0426** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **694**, R² = **0.0454**, Adj R² = **0.0300**, F-statistic = **2.95** (p = **7.91e-04**), Residual SE = **66.170** on **682** df, AIC = **7800.2**, BIC = **7854.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.1003** | 22.8697 | ±45.7394 | **+17.276** | **7.11e-67** | *** |
| Education: graduate level (vs college) | -2.2449 | 5.6688 | ±11.3376 | -0.396 | 0.6921 |  |
| Education: high school or below (vs college) | -9.2510 | 7.7220 | ±15.4440 | -1.198 | 0.2309 |  |
| **Site: UCSD (vs UAB)** | **-19.9623** | 6.2385 | ±12.4769 | **-3.200** | **0.0014** | ** |
| Site: UW (vs UAB) | -1.1487 | 6.5904 | ±13.1807 | -0.174 | 0.8616 |  |
| Age (years) | +0.2169 | 0.2598 | ±0.5196 | +0.835 | 0.4039 |  |
| **BMI (kg/m2)** | **-0.8840** | 0.3653 | ±0.7306 | **-2.420** | **0.0155** | * |
| Hypertension | -8.8898 | 5.4581 | ±10.9162 | -1.629 | 0.1034 |  |
| High cholesterol | +0.3144 | 5.1850 | ±10.3701 | +0.061 | 0.9516 |  |
| Kidney disease | +1.9042 | 8.2037 | ±16.4075 | +0.232 | 0.8165 |  |
| **Circulatory disease** | **+16.7879** | 7.5187 | ±15.0374 | **+2.233** | **0.0256** | * |
| Avg. daily SD (mg/dL) | -0.4709 | 0.2458 | ±0.4916 | -1.916 | 0.0554 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **694**, R² = **0.0442**, Adj R² = **0.0288**, F-statistic = **2.87** (p = **0.0011**), Residual SE = **66.211** on **682** df, AIC = **7801.1**, BIC = **7855.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.4438** | 24.1383 | ±48.2767 | **+16.548** | **1.65e-61** | *** |
| Education: graduate level (vs college) | -2.0574 | 5.6651 | ±11.3301 | -0.363 | 0.7165 |  |
| Education: high school or below (vs college) | -10.4820 | 7.6968 | ±15.3935 | -1.362 | 0.1732 |  |
| **Site: UCSD (vs UAB)** | **-19.7305** | 6.2368 | ±12.4736 | **-3.164** | **0.0016** | ** |
| Site: UW (vs UAB) | -0.8977 | 6.5837 | ±13.1673 | -0.136 | 0.8915 |  |
| Age (years) | +0.2205 | 0.2604 | ±0.5208 | +0.847 | 0.3971 |  |
| **BMI (kg/m2)** | **-0.9445** | 0.3599 | ±0.7198 | **-2.625** | **0.0087** | ** |
| Hypertension | -8.9812 | 5.4680 | ±10.9360 | -1.643 | 0.1005 |  |
| High cholesterol | +0.1198 | 5.1907 | ±10.3815 | +0.023 | 0.9816 |  |
| Kidney disease | +1.4109 | 8.1344 | ±16.2688 | +0.173 | 0.8623 |  |
| **Circulatory disease** | **+16.0629** | 7.5374 | ±15.0749 | **+2.131** | **0.0331** | * |
| CV (%) | -0.7781 | 0.4633 | ±0.9266 | -1.680 | 0.0931 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **694**, R² = **0.0466**, Adj R² = **0.0312**, F-statistic = **3.03** (p = **5.72e-04**), Residual SE = **66.128** on **682** df, AIC = **7799.3**, BIC = **7853.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.3916** | 25.1630 | ±50.3260 | **+14.163** | **1.55e-45** | *** |
| Education: graduate level (vs college) | -2.0962 | 5.6529 | ±11.3059 | -0.371 | 0.7108 |  |
| Education: high school or below (vs college) | -10.3305 | 7.6849 | ±15.3697 | -1.344 | 0.1789 |  |
| **Site: UCSD (vs UAB)** | **-19.5454** | 6.2109 | ±12.4218 | **-3.147** | **0.0016** | ** |
| Site: UW (vs UAB) | -0.9989 | 6.5704 | ±13.1409 | -0.152 | 0.8792 |  |
| Age (years) | +0.2232 | 0.2603 | ±0.5207 | +0.857 | 0.3913 |  |
| **BMI (kg/m2)** | **-0.9530** | 0.3599 | ±0.7198 | **-2.648** | **0.0081** | ** |
| Hypertension | -8.8384 | 5.4688 | ±10.9375 | -1.616 | 0.1061 |  |
| High cholesterol | +0.3284 | 5.1847 | ±10.3694 | +0.063 | 0.9495 |  |
| Kidney disease | +1.6716 | 8.0660 | ±16.1320 | +0.207 | 0.8358 |  |
| **Circulatory disease** | **+16.2729** | 7.5148 | ±15.0295 | **+2.165** | **0.0304** | * |
| **Mean / SD ratio** | **+5.5004** | 2.4726 | ±4.9452 | **+2.225** | **0.0261** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **694**, R² = **0.0491**, Adj R² = **0.0338**, F-statistic = **3.20** (p = **2.91e-04**), Residual SE = **66.041** on **682** df, AIC = **7797.5**, BIC = **7852.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+353.6626** | 24.6718 | ±49.3436 | **+14.335** | **1.33e-46** | *** |
| Education: graduate level (vs college) | -2.0518 | 5.6311 | ±11.2621 | -0.364 | 0.7156 |  |
| Education: high school or below (vs college) | -10.1453 | 7.6989 | ±15.3977 | -1.318 | 0.1876 |  |
| **Site: UCSD (vs UAB)** | **-19.4520** | 6.2148 | ±12.4295 | **-3.130** | **0.0017** | ** |
| Site: UW (vs UAB) | -1.0232 | 6.5582 | ±13.1164 | -0.156 | 0.8760 |  |
| Age (years) | +0.2407 | 0.2598 | ±0.5195 | +0.927 | 0.3541 |  |
| **BMI (kg/m2)** | **-0.9868** | 0.3583 | ±0.7165 | **-2.754** | **0.0059** | ** |
| Hypertension | -8.7570 | 5.4537 | ±10.9074 | -1.606 | 0.1083 |  |
| High cholesterol | +0.1984 | 5.1769 | ±10.3537 | +0.038 | 0.9694 |  |
| Kidney disease | +1.9466 | 8.0081 | ±16.0161 | +0.243 | 0.8079 |  |
| **Circulatory disease** | **+16.0113** | 7.5407 | ±15.0814 | **+2.123** | **0.0337** | * |
| **Avg. daily mean/SD** | **+5.2112** | 2.0181 | ±4.0362 | **+2.582** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **694**, R² = **0.0612**, Adj R² = **0.0460**, F-statistic = **4.04** (p = **9.52e-06**), Residual SE = **65.622** on **682** df, AIC = **7788.6**, BIC = **7843.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+435.0134** | 26.3327 | ±52.6655 | **+16.520** | **2.64e-61** | *** |
| Education: graduate level (vs college) | -3.2794 | 5.6426 | ±11.2853 | -0.581 | 0.5611 |  |
| Education: high school or below (vs college) | -9.5318 | 7.5646 | ±15.1293 | -1.260 | 0.2077 |  |
| **Site: UCSD (vs UAB)** | **-21.1549** | 6.1940 | ±12.3880 | **-3.415** | **6.37e-04** | *** |
| Site: UW (vs UAB) | -3.5503 | 6.5182 | ±13.0364 | -0.545 | 0.5860 |  |
| Age (years) | +0.1341 | 0.2600 | ±0.5200 | +0.516 | 0.6059 |  |
| **BMI (kg/m2)** | **-0.9158** | 0.3559 | ±0.7119 | **-2.573** | **0.0101** | * |
| Hypertension | -9.9424 | 5.4124 | ±10.8248 | -1.837 | 0.0662 | . |
| High cholesterol | -0.5826 | 5.1843 | ±10.3686 | -0.112 | 0.9105 |  |
| Kidney disease | +1.3947 | 7.9108 | ±15.8215 | +0.176 | 0.8601 |  |
| **Circulatory disease** | **+16.2829** | 7.4446 | ±14.8893 | **+2.187** | **0.0287** | * |
| **MAG (mg/dL/h)** | **-1.0357** | 0.2615 | ±0.5231 | **-3.960** | **7.50e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **694**, R² = **0.0460**, Adj R² = **0.0306**, F-statistic = **2.99** (p = **6.77e-04**), Residual SE = **66.150** on **682** df, AIC = **7799.8**, BIC = **7854.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.5657** | 24.4072 | ±48.8144 | **+16.535** | **2.06e-61** | *** |
| Education: graduate level (vs college) | -2.1925 | 5.6649 | ±11.3297 | -0.387 | 0.6987 |  |
| Education: high school or below (vs college) | -9.0941 | 7.7140 | ±15.4281 | -1.179 | 0.2384 |  |
| **Site: UCSD (vs UAB)** | **-20.1928** | 6.2474 | ±12.4948 | **-3.232** | **0.0012** | ** |
| Site: UW (vs UAB) | -1.3405 | 6.5909 | ±13.1818 | -0.203 | 0.8388 |  |
| Age (years) | +0.1989 | 0.2599 | ±0.5198 | +0.765 | 0.4441 |  |
| **BMI (kg/m2)** | **-0.9082** | 0.3618 | ±0.7235 | **-2.510** | **0.0121** | * |
| Hypertension | -9.2227 | 5.4541 | ±10.9082 | -1.691 | 0.0908 | . |
| High cholesterol | +0.2398 | 5.1890 | ±10.3780 | +0.046 | 0.9631 |  |
| Kidney disease | +1.9830 | 8.1611 | ±16.3222 | +0.243 | 0.8080 |  |
| **Circulatory disease** | **+16.7407** | 7.5074 | ±15.0148 | **+2.230** | **0.0258** | * |
| **Avg. daily range (mg/dL)** | **-0.1475** | 0.0724 | ±0.1449 | **-2.036** | **0.0418** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **694**, R² = **0.0459**, Adj R² = **0.0305**, F-statistic = **2.98** (p = **6.94e-04**), Residual SE = **66.153** on **682** df, AIC = **7799.8**, BIC = **7854.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.2703** | 22.3463 | ±44.6925 | **+17.375** | **1.27e-67** | *** |
| Education: graduate level (vs college) | -2.6093 | 5.7294 | ±11.4588 | -0.455 | 0.6488 |  |
| Education: high school or below (vs college) | -10.3166 | 7.6138 | ±15.2277 | -1.355 | 0.1754 |  |
| **Site: UCSD (vs UAB)** | **-19.6171** | 6.1787 | ±12.3575 | **-3.175** | **0.0015** | ** |
| Site: UW (vs UAB) | -0.9667 | 6.5845 | ±13.1690 | -0.147 | 0.8833 |  |
| Age (years) | +0.1777 | 0.2616 | ±0.5232 | +0.679 | 0.4969 |  |
| **BMI (kg/m2)** | **-0.8334** | 0.3644 | ±0.7288 | **-2.287** | **0.0222** | * |
| Hypertension | -8.6565 | 5.4936 | ±10.9871 | -1.576 | 0.1151 |  |
| High cholesterol | +0.3402 | 5.1830 | ±10.3661 | +0.066 | 0.9477 |  |
| Kidney disease | +0.0543 | 7.9736 | ±15.9471 | +0.007 | 0.9946 |  |
| **Circulatory disease** | **+17.1760** | 7.5122 | ±15.0244 | **+2.286** | **0.0222** | * |
| SD of daily means (mg/dL) | -0.6333 | 0.3282 | ±0.6565 | -1.930 | 0.0537 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.329** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+377.6139** | 24.6781 | ±49.3561 | **+15.302** | **7.46e-53** | *** |
| Education: graduate level (vs college) | -1.7415 | 5.6829 | ±11.3657 | -0.306 | 0.7593 |  |
| Education: high school or below (vs college) | -10.6159 | 7.7576 | ±15.5152 | -1.368 | 0.1712 |  |
| **Site: UCSD (vs UAB)** | **-19.4017** | 6.2526 | ±12.5052 | **-3.103** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0422 | 6.5849 | ±13.1698 | +0.006 | 0.9949 |  |
| Age (years) | +0.1976 | 0.2620 | ±0.5239 | +0.754 | 0.4507 |  |
| **BMI (kg/m2)** | **-0.9180** | 0.3726 | ±0.7451 | **-2.464** | **0.0137** | * |
| Hypertension | -9.4049 | 5.4713 | ±10.9426 | -1.719 | 0.0856 | . |
| High cholesterol | +0.6246 | 5.2038 | ±10.4076 | +0.120 | 0.9045 |  |
| Kidney disease | -0.4760 | 7.9373 | ±15.8747 | -0.060 | 0.9522 |  |
| **Circulatory disease** | **+16.4132** | 7.5953 | ±15.1906 | **+2.161** | **0.0307** | * |
| Time in range 70-180, pooled (%) | +0.0513 | 0.1089 | ±0.2179 | +0.471 | 0.6374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **694**, R² = **0.0407**, Adj R² = **0.0252**, F-statistic = **2.63** (p = **0.0027**), Residual SE = **66.332** on **682** df, AIC = **7803.6**, BIC = **7858.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+378.2660** | 24.7673 | ±49.5347 | **+15.273** | **1.16e-52** | *** |
| Education: graduate level (vs college) | -1.7035 | 5.6804 | ±11.3609 | -0.300 | 0.7643 |  |
| Education: high school or below (vs college) | -10.6614 | 7.7642 | ±15.5284 | -1.373 | 0.1697 |  |
| **Site: UCSD (vs UAB)** | **-19.3847** | 6.2613 | ±12.5225 | **-3.096** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.0777 | 6.5865 | ±13.1730 | +0.012 | 0.9906 |  |
| Age (years) | +0.1979 | 0.2621 | ±0.5241 | +0.755 | 0.4500 |  |
| **BMI (kg/m2)** | **-0.9227** | 0.3728 | ±0.7456 | **-2.475** | **0.0133** | * |
| Hypertension | -9.4179 | 5.4724 | ±10.9448 | -1.721 | 0.0853 | . |
| High cholesterol | +0.6378 | 5.2039 | ±10.4078 | +0.123 | 0.9025 |  |
| Kidney disease | -0.4966 | 7.9478 | ±15.8956 | -0.062 | 0.9502 |  |
| **Circulatory disease** | **+16.3743** | 7.5955 | ±15.1909 | **+2.156** | **0.0311** | * |
| Avg. daily time in range 70-180 (%) | +0.0436 | 0.1085 | ±0.2170 | +0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **694**, R² = **0.0412**, Adj R² = **0.0258**, F-statistic = **2.67** (p = **0.0023**), Residual SE = **66.314** on **682** df, AIC = **7803.2**, BIC = **7857.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.6705** | 22.3192 | ±44.6384 | **+17.056** | **3.17e-65** | *** |
| Education: graduate level (vs college) | -1.4057 | 5.6800 | ±11.3599 | -0.247 | 0.8045 |  |
| Education: high school or below (vs college) | -10.8334 | 7.7437 | ±15.4875 | -1.399 | 0.1618 |  |
| **Site: UCSD (vs UAB)** | **-18.9644** | 6.2361 | ±12.4722 | **-3.041** | **0.0024** | ** |
| Site: UW (vs UAB) | +0.5344 | 6.5460 | ±13.0920 | +0.082 | 0.9349 |  |
| Age (years) | +0.2025 | 0.2623 | ±0.5246 | +0.772 | 0.4401 |  |
| **BMI (kg/m2)** | **-0.9522** | 0.3601 | ±0.7202 | **-2.644** | **0.0082** | ** |
| Hypertension | -9.6538 | 5.4895 | ±10.9790 | -1.759 | 0.0786 | . |
| High cholesterol | +0.9586 | 5.2255 | ±10.4510 | +0.183 | 0.8545 |  |
| Kidney disease | -0.6799 | 7.8527 | ±15.7054 | -0.087 | 0.9310 |  |
| **Circulatory disease** | **+15.9608** | 7.5628 | ±15.1255 | **+2.110** | **0.0348** | * |
| Any reading < 54 during wear (0/1) | +4.3380 | 5.9799 | ±11.9597 | +0.725 | 0.4682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.331** on **682** df, AIC = **7803.6**, BIC = **7858.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.9117** | 22.0768 | ±44.1535 | **+17.345** | **2.17e-67** | *** |
| Education: graduate level (vs college) | -1.7186 | 5.6745 | ±11.3490 | -0.303 | 0.7620 |  |
| Education: high school or below (vs college) | -11.1924 | 7.7199 | ±15.4399 | -1.450 | 0.1471 |  |
| **Site: UCSD (vs UAB)** | **-19.3752** | 6.2502 | ±12.5005 | **-3.100** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0462 | 6.5908 | ±13.1816 | +0.007 | 0.9944 |  |
| Age (years) | +0.2009 | 0.2619 | ±0.5239 | +0.767 | 0.4432 |  |
| **BMI (kg/m2)** | **-0.9618** | 0.3590 | ±0.7179 | **-2.679** | **0.0074** | ** |
| Hypertension | -9.4667 | 5.4717 | ±10.9434 | -1.730 | 0.0836 | . |
| High cholesterol | +0.4907 | 5.2316 | ±10.4632 | +0.094 | 0.9253 |  |
| Kidney disease | -0.7888 | 7.8530 | ±15.7061 | -0.100 | 0.9200 |  |
| **Circulatory disease** | **+16.0752** | 7.5803 | ±15.1607 | **+2.121** | **0.0340** | * |
| Time < 54 (%) | -1.9106 | 1.6284 | ±3.2567 | -1.173 | 0.2407 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.337** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.5973** | 22.0708 | ±44.1416 | **+17.335** | **2.56e-67** | *** |
| Education: graduate level (vs college) | -1.6403 | 5.6726 | ±11.3451 | -0.289 | 0.7725 |  |
| Education: high school or below (vs college) | -11.1252 | 7.7232 | ±15.4464 | -1.440 | 0.1497 |  |
| **Site: UCSD (vs UAB)** | **-19.2904** | 6.2568 | ±12.5136 | **-3.083** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1381 | 6.6062 | ±13.2124 | +0.021 | 0.9833 |  |
| Age (years) | +0.1987 | 0.2618 | ±0.5235 | +0.759 | 0.4478 |  |
| **BMI (kg/m2)** | **-0.9554** | 0.3584 | ±0.7167 | **-2.666** | **0.0077** | ** |
| Hypertension | -9.4506 | 5.4717 | ±10.9435 | -1.727 | 0.0841 | . |
| High cholesterol | +0.5568 | 5.2437 | ±10.4875 | +0.106 | 0.9154 |  |
| Kidney disease | -0.7416 | 7.8524 | ±15.7048 | -0.094 | 0.9248 |  |
| **Circulatory disease** | **+16.1193** | 7.5812 | ±15.1624 | **+2.126** | **0.0335** | * |
| Avg. daily time < 54 (%) | -1.2663 | 2.4806 | ±4.9611 | -0.511 | 0.6097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **694**, R² = **0.0436**, Adj R² = **0.0282**, F-statistic = **2.82** (p = **0.0013**), Residual SE = **66.233** on **682** df, AIC = **7801.5**, BIC = **7856.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.5215** | 22.0616 | ±44.1232 | **+17.248** | **1.16e-66** | *** |
| Education: graduate level (vs college) | -0.9173 | 5.6629 | ±11.3258 | -0.162 | 0.8713 |  |
| Education: high school or below (vs college) | -10.5854 | 7.7035 | ±15.4070 | -1.374 | 0.1694 |  |
| **Site: UCSD (vs UAB)** | **-18.3371** | 6.2458 | ±12.4916 | **-2.936** | **0.0033** | ** |
| Site: UW (vs UAB) | +1.3776 | 6.5972 | ±13.1944 | +0.209 | 0.8346 |  |
| Age (years) | +0.1811 | 0.2624 | ±0.5249 | +0.690 | 0.4902 |  |
| **BMI (kg/m2)** | **-0.9513** | 0.3587 | ±0.7174 | **-2.652** | **0.0080** | ** |
| Hypertension | -9.7013 | 5.4891 | ±10.9783 | -1.767 | 0.0772 | . |
| High cholesterol | +1.6594 | 5.2607 | ±10.5214 | +0.315 | 0.7524 |  |
| Kidney disease | -0.8173 | 7.8342 | ±15.6685 | -0.104 | 0.9169 |  |
| **Circulatory disease** | **+16.8632** | 7.5911 | ±15.1822 | **+2.221** | **0.0263** | * |
| Time 54-69, pooled (%) | +3.6440 | 2.5760 | ±5.1520 | +1.415 | 0.1572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **694**, R² = **0.0427**, Adj R² = **0.0273**, F-statistic = **2.77** (p = **0.0016**), Residual SE = **66.262** on **682** df, AIC = **7802.1**, BIC = **7856.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.1431** | 22.0382 | ±44.0765 | **+17.295** | **5.16e-67** | *** |
| Education: graduate level (vs college) | -1.0239 | 5.6624 | ±11.3247 | -0.181 | 0.8565 |  |
| Education: high school or below (vs college) | -10.5916 | 7.7076 | ±15.4152 | -1.374 | 0.1694 |  |
| **Site: UCSD (vs UAB)** | **-18.4518** | 6.2545 | ±12.5090 | **-2.950** | **0.0032** | ** |
| Site: UW (vs UAB) | +1.2811 | 6.6053 | ±13.2106 | +0.194 | 0.8462 |  |
| Age (years) | +0.1817 | 0.2626 | ±0.5252 | +0.692 | 0.4889 |  |
| **BMI (kg/m2)** | **-0.9555** | 0.3591 | ±0.7182 | **-2.661** | **0.0078** | ** |
| Hypertension | -9.6769 | 5.4841 | ±10.9682 | -1.765 | 0.0776 | . |
| High cholesterol | +1.5214 | 5.2664 | ±10.5328 | +0.289 | 0.7727 |  |
| Kidney disease | -0.8439 | 7.8400 | ±15.6801 | -0.108 | 0.9143 |  |
| **Circulatory disease** | **+16.7467** | 7.5869 | ±15.1737 | **+2.207** | **0.0273** | * |
| Avg. daily time 54-69 (%) | +2.8936 | 2.2010 | ±4.4020 | +1.315 | 0.1886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **694**, R² = **0.0416**, Adj R² = **0.0261**, F-statistic = **2.69** (p = **0.0021**), Residual SE = **66.302** on **682** df, AIC = **7803.0**, BIC = **7857.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.0092** | 22.0853 | ±44.1707 | **+17.252** | **1.09e-66** | *** |
| Education: graduate level (vs college) | -1.1430 | 5.6705 | ±11.3409 | -0.202 | 0.8403 |  |
| Education: high school or below (vs college) | -10.6746 | 7.7239 | ±15.4478 | -1.382 | 0.1670 |  |
| **Site: UCSD (vs UAB)** | **-18.6321** | 6.2578 | ±12.5155 | **-2.977** | **0.0029** | ** |
| Site: UW (vs UAB) | +1.0057 | 6.6124 | ±13.2247 | +0.152 | 0.8791 |  |
| Age (years) | +0.1864 | 0.2623 | ±0.5246 | +0.711 | 0.4773 |  |
| **BMI (kg/m2)** | **-0.9442** | 0.3591 | ±0.7181 | **-2.629** | **0.0086** | ** |
| Hypertension | -9.5592 | 5.4787 | ±10.9573 | -1.745 | 0.0810 | . |
| High cholesterol | +1.2928 | 5.2700 | ±10.5401 | +0.245 | 0.8062 |  |
| Kidney disease | -0.7278 | 7.8446 | ±15.6892 | -0.093 | 0.9261 |  |
| **Circulatory disease** | **+16.5600** | 7.5911 | ±15.1821 | **+2.182** | **0.0291** | * |
| Time < 70 (%) | +1.6087 | 1.7147 | ±3.4294 | +0.938 | 0.3481 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **694**, R² = **0.0415**, Adj R² = **0.0261**, F-statistic = **2.69** (p = **0.0022**), Residual SE = **66.305** on **682** df, AIC = **7803.0**, BIC = **7857.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.3783** | 22.0589 | ±44.1179 | **+17.289** | **5.69e-67** | *** |
| Education: graduate level (vs college) | -1.1947 | 5.6674 | ±11.3348 | -0.211 | 0.8330 |  |
| Education: high school or below (vs college) | -10.6703 | 7.7193 | ±15.4386 | -1.382 | 0.1669 |  |
| **Site: UCSD (vs UAB)** | **-18.6685** | 6.2632 | ±12.5264 | **-2.981** | **0.0029** | ** |
| Site: UW (vs UAB) | +1.0055 | 6.6161 | ±13.2322 | +0.152 | 0.8792 |  |
| Age (years) | +0.1869 | 0.2623 | ±0.5247 | +0.712 | 0.4762 |  |
| **BMI (kg/m2)** | **-0.9507** | 0.3591 | ±0.7182 | **-2.647** | **0.0081** | ** |
| Hypertension | -9.5790 | 5.4764 | ±10.9529 | -1.749 | 0.0803 | . |
| High cholesterol | +1.2752 | 5.2716 | ±10.5432 | +0.242 | 0.8089 |  |
| Kidney disease | -0.7847 | 7.8467 | ±15.6933 | -0.100 | 0.9203 |  |
| **Circulatory disease** | **+16.5268** | 7.5849 | ±15.1698 | **+2.179** | **0.0293** | * |
| Avg. daily time < 70 (%) | +1.4700 | 1.4209 | ±2.8418 | +1.035 | 0.3009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.63** (p = **0.0027**), Residual SE = **66.336** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+377.6241** | 26.8053 | ±53.6106 | **+14.088** | **4.52e-45** | *** |
| Education: graduate level (vs college) | -1.7368 | 5.7360 | ±11.4719 | -0.303 | 0.7621 |  |
| Education: high school or below (vs college) | -10.8164 | 7.6893 | ±15.3786 | -1.407 | 0.1595 |  |
| **Site: UCSD (vs UAB)** | **-19.2909** | 6.2337 | ±12.4673 | **-3.095** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1165 | 6.5376 | ±13.0753 | +0.018 | 0.9858 |  |
| Age (years) | +0.1911 | 0.2620 | ±0.5241 | +0.729 | 0.4657 |  |
| **BMI (kg/m2)** | **-0.9404** | 0.3640 | ±0.7279 | **-2.584** | **0.0098** | ** |
| Hypertension | -9.4183 | 5.4725 | ±10.9451 | -1.721 | 0.0852 | . |
| High cholesterol | +0.6437 | 5.2039 | ±10.4077 | +0.124 | 0.9016 |  |
| Kidney disease | -0.6158 | 7.8947 | ±15.7895 | -0.078 | 0.9378 |  |
| **Circulatory disease** | **+16.3115** | 7.6181 | ±15.2362 | **+2.141** | **0.0323** | * |
| Time 54-250, pooled (%) | +0.0518 | 0.1553 | ±0.3106 | +0.333 | 0.7389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.337** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+378.2323** | 27.1214 | ±54.2429 | **+13.946** | **3.33e-44** | *** |
| Education: graduate level (vs college) | -1.7060 | 5.7344 | ±11.4687 | -0.298 | 0.7661 |  |
| Education: high school or below (vs college) | -10.8474 | 7.6896 | ±15.3793 | -1.411 | 0.1583 |  |
| **Site: UCSD (vs UAB)** | **-19.2743** | 6.2356 | ±12.4711 | **-3.091** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1525 | 6.5347 | ±13.0695 | +0.023 | 0.9814 |  |
| Age (years) | +0.1926 | 0.2619 | ±0.5239 | +0.735 | 0.4621 |  |
| **BMI (kg/m2)** | **-0.9420** | 0.3641 | ±0.7281 | **-2.587** | **0.0097** | ** |
| Hypertension | -9.4293 | 5.4729 | ±10.9458 | -1.723 | 0.0849 | . |
| High cholesterol | +0.6508 | 5.2039 | ±10.4077 | +0.125 | 0.9005 |  |
| Kidney disease | -0.6211 | 7.9054 | ±15.8107 | -0.079 | 0.9374 |  |
| **Circulatory disease** | **+16.2957** | 7.6222 | ±15.2444 | **+2.138** | **0.0325** | * |
| Avg. daily time 54-250 (%) | +0.0443 | 0.1585 | ±0.3170 | +0.280 | 0.7797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **694**, R² = **0.0409**, Adj R² = **0.0254**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.326** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.1694** | 22.0505 | ±44.1009 | **+17.332** | **2.72e-67** | *** |
| Education: graduate level (vs college) | -1.5546 | 5.6789 | ±11.3578 | -0.274 | 0.7843 |  |
| Education: high school or below (vs college) | -10.6172 | 7.8113 | ±15.6226 | -1.359 | 0.1741 |  |
| **Site: UCSD (vs UAB)** | **-19.3626** | 6.2465 | ±12.4931 | **-3.100** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.1957 | 6.5820 | ±13.1639 | +0.030 | 0.9763 |  |
| Age (years) | +0.2086 | 0.2630 | ±0.5260 | +0.793 | 0.4277 |  |
| **BMI (kg/m2)** | **-0.9095** | 0.3724 | ±0.7448 | **-2.442** | **0.0146** | * |
| Hypertension | -9.4391 | 5.4757 | ±10.9515 | -1.724 | 0.0847 | . |
| High cholesterol | +0.6837 | 5.2066 | ±10.4132 | +0.131 | 0.8955 |  |
| Kidney disease | -0.4699 | 7.9289 | ±15.8578 | -0.059 | 0.9527 |  |
| **Circulatory disease** | **+16.3877** | 7.5665 | ±15.1330 | **+2.166** | **0.0303** | * |
| Time 181-250, pooled (%) | -0.0979 | 0.1915 | ±0.3830 | -0.512 | 0.6090 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.329** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.2108** | 22.0545 | ±44.1090 | **+17.330** | **2.78e-67** | *** |
| Education: graduate level (vs college) | -1.5444 | 5.6807 | ±11.3615 | -0.272 | 0.7857 |  |
| Education: high school or below (vs college) | -10.6380 | 7.8241 | ±15.6482 | -1.360 | 0.1739 |  |
| **Site: UCSD (vs UAB)** | **-19.3671** | 6.2561 | ±12.5123 | **-3.096** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1906 | 6.5877 | ±13.1754 | +0.029 | 0.9769 |  |
| Age (years) | +0.2064 | 0.2631 | ±0.5261 | +0.785 | 0.4326 |  |
| **BMI (kg/m2)** | **-0.9151** | 0.3724 | ±0.7449 | **-2.457** | **0.0140** | * |
| Hypertension | -9.4422 | 5.4767 | ±10.9533 | -1.724 | 0.0847 | . |
| High cholesterol | +0.6925 | 5.2074 | ±10.4147 | +0.133 | 0.8942 |  |
| Kidney disease | -0.4957 | 7.9306 | ±15.8612 | -0.063 | 0.9502 |  |
| **Circulatory disease** | **+16.3452** | 7.5684 | ±15.1367 | **+2.160** | **0.0308** | * |
| Avg. daily time 181-250 (%) | -0.0841 | 0.1874 | ±0.3747 | -0.449 | 0.6535 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **694**, R² = **0.0409**, Adj R² = **0.0254**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.327** on **682** df, AIC = **7803.5**, BIC = **7858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.7440** | 22.0340 | ±44.0680 | **+17.371** | **1.38e-67** | *** |
| Education: graduate level (vs college) | -1.7437 | 5.6816 | ±11.3631 | -0.307 | 0.7589 |  |
| Education: high school or below (vs college) | -10.5673 | 7.7603 | ±15.5206 | -1.362 | 0.1733 |  |
| **Site: UCSD (vs UAB)** | **-19.4042** | 6.2474 | ±12.4948 | **-3.106** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0416 | 6.5789 | ±13.1577 | +0.006 | 0.9950 |  |
| Age (years) | +0.1973 | 0.2619 | ±0.5239 | +0.753 | 0.4513 |  |
| **BMI (kg/m2)** | **-0.9145** | 0.3725 | ±0.7449 | **-2.455** | **0.0141** | * |
| Hypertension | -9.4034 | 5.4714 | ±10.9429 | -1.719 | 0.0857 | . |
| High cholesterol | +0.6389 | 5.2033 | ±10.4066 | +0.123 | 0.9023 |  |
| Kidney disease | -0.4517 | 7.9370 | ±15.8740 | -0.057 | 0.9546 |  |
| **Circulatory disease** | **+16.4489** | 7.5971 | ±15.1942 | **+2.165** | **0.0304** | * |
| Time > 180 (%) | -0.0561 | 0.1082 | ±0.2164 | -0.518 | 0.6042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **694**, R² = **0.0408**, Adj R² = **0.0253**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **66.330** on **682** df, AIC = **7803.6**, BIC = **7858.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.6334** | 22.0355 | ±44.0709 | **+17.364** | **1.53e-67** | *** |
| Education: graduate level (vs college) | -1.7077 | 5.6795 | ±11.3589 | -0.301 | 0.7637 |  |
| Education: high school or below (vs college) | -10.6100 | 7.7665 | ±15.5330 | -1.366 | 0.1719 |  |
| **Site: UCSD (vs UAB)** | **-19.3923** | 6.2548 | ±12.5096 | **-3.100** | **0.0019** | ** |
| Site: UW (vs UAB) | +0.0741 | 6.5798 | ±13.1595 | +0.011 | 0.9910 |  |
| Age (years) | +0.1977 | 0.2620 | ±0.5240 | +0.755 | 0.4504 |  |
| **BMI (kg/m2)** | **-0.9192** | 0.3725 | ±0.7449 | **-2.468** | **0.0136** | * |
| Hypertension | -9.4173 | 5.4725 | ±10.9450 | -1.721 | 0.0853 | . |
| High cholesterol | +0.6505 | 5.2036 | ±10.4072 | +0.125 | 0.9005 |  |
| Kidney disease | -0.4710 | 7.9469 | ±15.8937 | -0.059 | 0.9527 |  |
| **Circulatory disease** | **+16.4089** | 7.5970 | ±15.1939 | **+2.160** | **0.0308** | * |
| Avg. daily time > 180 (%) | -0.0486 | 0.1078 | ±0.2156 | -0.451 | 0.6523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.338** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.2283** | 22.0445 | ±44.0891 | **+17.339** | **2.39e-67** | *** |
| Education: graduate level (vs college) | -1.4492 | 5.6973 | ±11.3946 | -0.254 | 0.7992 |  |
| Education: high school or below (vs college) | -11.1664 | 7.7598 | ±15.5195 | -1.439 | 0.1501 |  |
| **Site: UCSD (vs UAB)** | **-19.0541** | 6.2712 | ±12.5424 | **-3.038** | **0.0024** | ** |
| Site: UW (vs UAB) | +0.4043 | 6.5759 | ±13.1518 | +0.061 | 0.9510 |  |
| Age (years) | +0.1988 | 0.2620 | ±0.5239 | +0.759 | 0.4478 |  |
| **BMI (kg/m2)** | **-0.9721** | 0.3758 | ±0.7517 | **-2.586** | **0.0097** | ** |
| Hypertension | -9.4704 | 5.4802 | ±10.9605 | -1.728 | 0.0840 | . |
| High cholesterol | +0.7419 | 5.2089 | ±10.4177 | +0.142 | 0.8867 |  |
| Kidney disease | -0.8103 | 7.8961 | ±15.7923 | -0.103 | 0.9183 |  |
| **Circulatory disease** | **+16.0586** | 7.6053 | ±15.2107 | **+2.111** | **0.0347** | * |
| Nocturnal time > 180 (%) | +0.0221 | 0.0978 | ±0.1956 | +0.226 | 0.8215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.336** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.7568** | 22.0414 | ±44.0827 | **+17.365** | **1.51e-67** | *** |
| Education: graduate level (vs college) | -1.7231 | 5.7330 | ±11.4660 | -0.301 | 0.7638 |  |
| Education: high school or below (vs college) | -10.8226 | 7.6906 | ±15.3812 | -1.407 | 0.1594 |  |
| **Site: UCSD (vs UAB)** | **-19.2792** | 6.2323 | ±12.4646 | **-3.093** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1339 | 6.5358 | ±13.0717 | +0.020 | 0.9837 |  |
| Age (years) | +0.1913 | 0.2621 | ±0.5241 | +0.730 | 0.4653 |  |
| **BMI (kg/m2)** | **-0.9408** | 0.3641 | ±0.7283 | **-2.584** | **0.0098** | ** |
| Hypertension | -9.4203 | 5.4729 | ±10.9458 | -1.721 | 0.0852 | . |
| High cholesterol | +0.6517 | 5.2034 | ±10.4068 | +0.125 | 0.9003 |  |
| Kidney disease | -0.6210 | 7.8951 | ±15.7903 | -0.079 | 0.9373 |  |
| **Circulatory disease** | **+16.3064** | 7.6201 | ±15.2402 | **+2.140** | **0.0324** | * |
| Time > 250 (%) | -0.0489 | 0.1553 | ±0.3106 | -0.315 | 0.7527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 694)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **694**, R² = **0.0406**, Adj R² = **0.0251**, F-statistic = **2.62** (p = **0.0028**), Residual SE = **66.337** on **682** df, AIC = **7803.7**, BIC = **7858.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.6440** | 22.0386 | ±44.0771 | **+17.362** | **1.59e-67** | *** |
| Education: graduate level (vs college) | -1.6985 | 5.7320 | ±11.4640 | -0.296 | 0.7670 |  |
| Education: high school or below (vs college) | -10.8491 | 7.6907 | ±15.3814 | -1.411 | 0.1583 |  |
| **Site: UCSD (vs UAB)** | **-19.2669** | 6.2340 | ±12.4680 | **-3.091** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.1636 | 6.5329 | ±13.0659 | +0.025 | 0.9800 |  |
| Age (years) | +0.1927 | 0.2620 | ±0.5239 | +0.736 | 0.4619 |  |
| **BMI (kg/m2)** | **-0.9422** | 0.3641 | ±0.7282 | **-2.588** | **0.0097** | ** |
| Hypertension | -9.4306 | 5.4731 | ±10.9461 | -1.723 | 0.0849 | . |
| High cholesterol | +0.6569 | 5.2034 | ±10.4068 | +0.126 | 0.8995 |  |
| Kidney disease | -0.6247 | 7.9054 | ±15.8107 | -0.079 | 0.9370 |  |
| **Circulatory disease** | **+16.2934** | 7.6239 | ±15.2478 | **+2.137** | **0.0326** | * |
| Avg. daily time > 250 (%) | -0.0429 | 0.1585 | ±0.3170 | -0.271 | 0.7868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 692; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **692**, R² = **0.1118**, Adj R² = **0.0987**, F-statistic = **8.57** (p = **2.95e-13**), Residual SE = **17.463** on **681** df, AIC = **5933.1**, BIC = **5983.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.3603** | 5.7369 | ±11.4738 | **+11.393** | **4.53e-30** | *** |
| Education: graduate level (vs college) | -2.2336 | 1.5020 | ±3.0041 | -1.487 | 0.1370 |  |
| Education: high school or below (vs college) | +2.8033 | 1.9940 | ±3.9880 | +1.406 | 0.1598 |  |
| Site: UCSD (vs UAB) | +3.5406 | 1.8239 | ±3.6478 | +1.941 | 0.0522 | . |
| Site: UW (vs UAB) | +1.0064 | 1.6008 | ±3.2016 | +0.629 | 0.5295 |  |
| **Age (years)** | **-0.3799** | 0.0661 | ±0.1321 | **-5.751** | **8.86e-09** | *** |
| **BMI (kg/m2)** | **+0.4104** | 0.0987 | ±0.1973 | **+4.160** | **3.19e-05** | *** |
| Hypertension | -0.3276 | 1.5404 | ±3.0808 | -0.213 | 0.8316 |  |
| High cholesterol | +1.2435 | 1.4558 | ±2.9116 | +0.854 | 0.3930 |  |
| Kidney disease | -1.1705 | 1.9537 | ±3.9074 | -0.599 | 0.5491 |  |
| Circulatory disease | -2.4329 | 1.8320 | ±3.6641 | -1.328 | 0.1842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **692**, R² = **0.1530**, Adj R² = **0.1393**, F-statistic = **11.16** (p = **3.44e-19**), Residual SE = **17.065** on **680** df, AIC = **5902.2**, BIC = **5956.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9034** | 6.3705 | ±12.7411 | **+7.676** | **1.64e-14** | *** |
| Education: graduate level (vs college) | -1.5421 | 1.4881 | ±2.9762 | -1.036 | 0.3001 |  |
| Education: high school or below (vs college) | +1.3988 | 1.9350 | ±3.8699 | +0.723 | 0.4697 |  |
| **Site: UCSD (vs UAB)** | **+3.8141** | 1.7956 | ±3.5912 | **+2.124** | **0.0337** | * |
| Site: UW (vs UAB) | +1.7337 | 1.5839 | ±3.1679 | +1.095 | 0.2737 |  |
| **Age (years)** | **-0.3770** | 0.0642 | ±0.1284 | **-5.872** | **4.31e-09** | *** |
| **BMI (kg/m2)** | **+0.3046** | 0.0990 | ±0.1980 | **+3.077** | **0.0021** | ** |
| Hypertension | -0.8258 | 1.5082 | ±3.0165 | -0.547 | 0.5840 |  |
| High cholesterol | +1.0824 | 1.4302 | ±2.8603 | +0.757 | 0.4491 |  |
| Kidney disease | -0.9954 | 1.9051 | ±3.8102 | -0.523 | 0.6013 |  |
| Circulatory disease | -2.7526 | 1.7957 | ±3.5914 | -1.533 | 0.1253 |  |
| **HbA1c (%)** | **+2.8794** | 0.4818 | ±0.9635 | **+5.977** | **2.27e-09** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **692**, R² = **0.1462**, Adj R² = **0.1324**, F-statistic = **10.59** (p = **4.20e-18**), Residual SE = **17.133** on **680** df, AIC = **5907.7**, BIC = **5962.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.1816** | 6.3266 | ±12.6531 | **+8.406** | **4.24e-17** | *** |
| Education: graduate level (vs college) | -1.8713 | 1.4902 | ±2.9804 | -1.256 | 0.2092 |  |
| Education: high school or below (vs college) | +1.5696 | 1.9182 | ±3.8364 | +0.818 | 0.4132 |  |
| **Site: UCSD (vs UAB)** | **+3.9645** | 1.8113 | ±3.6226 | **+2.189** | **0.0286** | * |
| Site: UW (vs UAB) | +1.6115 | 1.5895 | ±3.1791 | +1.014 | 0.3107 |  |
| **Age (years)** | **-0.3721** | 0.0642 | ±0.1283 | **-5.799** | **6.68e-09** | *** |
| **BMI (kg/m2)** | **+0.3260** | 0.0989 | ±0.1979 | **+3.295** | **9.84e-04** | *** |
| Hypertension | -0.6532 | 1.5234 | ±3.0467 | -0.429 | 0.6681 |  |
| High cholesterol | +1.2992 | 1.4408 | ±2.8815 | +0.902 | 0.3672 |  |
| Kidney disease | -1.5618 | 1.9210 | ±3.8419 | -0.813 | 0.4162 |  |
| Circulatory disease | -3.0821 | 1.8051 | ±3.6102 | -1.707 | 0.0877 | . |
| **Mean glucose (mg/dL)** | **+0.0886** | 0.0191 | ±0.0382 | **+4.639** | **3.50e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **692**, R² = **0.1462**, Adj R² = **0.1324**, F-statistic = **10.59** (p = **4.20e-18**), Residual SE = **17.133** on **680** df, AIC = **5907.7**, BIC = **5962.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9148** | 7.9039 | ±15.8077 | **+5.177** | **2.26e-07** | *** |
| Education: graduate level (vs college) | -1.8713 | 1.4902 | ±2.9804 | -1.256 | 0.2092 |  |
| Education: high school or below (vs college) | +1.5696 | 1.9182 | ±3.8364 | +0.818 | 0.4132 |  |
| **Site: UCSD (vs UAB)** | **+3.9645** | 1.8113 | ±3.6226 | **+2.189** | **0.0286** | * |
| Site: UW (vs UAB) | +1.6115 | 1.5895 | ±3.1791 | +1.014 | 0.3107 |  |
| **Age (years)** | **-0.3721** | 0.0642 | ±0.1283 | **-5.799** | **6.68e-09** | *** |
| **BMI (kg/m2)** | **+0.3260** | 0.0989 | ±0.1979 | **+3.295** | **9.84e-04** | *** |
| Hypertension | -0.6532 | 1.5234 | ±3.0467 | -0.429 | 0.6681 |  |
| High cholesterol | +1.2992 | 1.4408 | ±2.8815 | +0.902 | 0.3672 |  |
| Kidney disease | -1.5618 | 1.9210 | ±3.8419 | -0.813 | 0.4162 |  |
| Circulatory disease | -3.0821 | 1.8051 | ±3.6102 | -1.707 | 0.0877 | . |
| **GMI (%)** | **+3.7060** | 0.7989 | ±1.5977 | **+4.639** | **3.50e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **692**, R² = **0.1381**, Adj R² = **0.1241**, F-statistic = **9.90** (p = **8.26e-17**), Residual SE = **17.215** on **680** df, AIC = **5914.3**, BIC = **5968.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.6797** | 6.2708 | ±12.5416 | **+8.879** | **6.73e-19** | *** |
| Education: graduate level (vs college) | -1.8378 | 1.5034 | ±3.0069 | -1.222 | 0.2216 |  |
| Education: high school or below (vs college) | +1.8135 | 1.9186 | ±3.8372 | +0.945 | 0.3445 |  |
| **Site: UCSD (vs UAB)** | **+3.8850** | 1.8204 | ±3.6408 | **+2.134** | **0.0328** | * |
| Site: UW (vs UAB) | +1.3668 | 1.5895 | ±3.1790 | +0.860 | 0.3898 |  |
| **Age (years)** | **-0.3636** | 0.0650 | ±0.1299 | **-5.597** | **2.18e-08** | *** |
| **BMI (kg/m2)** | **+0.3196** | 0.0998 | ±0.1996 | **+3.203** | **0.0014** | ** |
| Hypertension | -0.5615 | 1.5282 | ±3.0564 | -0.367 | 0.7133 |  |
| High cholesterol | +1.3592 | 1.4504 | ±2.9007 | +0.937 | 0.3487 |  |
| Kidney disease | -1.1757 | 1.9288 | ±3.8576 | -0.610 | 0.5422 |  |
| Circulatory disease | -2.9891 | 1.8114 | ±3.6229 | -1.650 | 0.0989 | . |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0735** | 0.0183 | ±0.0366 | **+4.012** | **6.03e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1307**, Adj R² = **0.1166**, F-statistic = **9.29** (p = **1.19e-15**), Residual SE = **17.289** on **680** df, AIC = **5920.2**, BIC = **5974.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6598** | 6.0344 | ±12.0689 | **+9.721** | **2.46e-22** | *** |
| Education: graduate level (vs college) | -1.8400 | 1.5021 | ±3.0042 | -1.225 | 0.2206 |  |
| Education: high school or below (vs college) | +1.9583 | 1.9786 | ±3.9573 | +0.990 | 0.3223 |  |
| **Site: UCSD (vs UAB)** | **+3.9935** | 1.8249 | ±3.6499 | **+2.188** | **0.0286** | * |
| Site: UW (vs UAB) | +1.8782 | 1.6280 | ±3.2560 | +1.154 | 0.2486 |  |
| **Age (years)** | **-0.3860** | 0.0645 | ±0.1290 | **-5.985** | **2.16e-09** | *** |
| **BMI (kg/m2)** | **+0.3642** | 0.0998 | ±0.1995 | **+3.650** | **2.62e-04** | *** |
| Hypertension | -0.7123 | 1.5469 | ±3.0938 | -0.460 | 0.6452 |  |
| High cholesterol | +1.4649 | 1.4575 | ±2.9150 | +1.005 | 0.3149 |  |
| Kidney disease | -2.4178 | 1.9612 | ±3.9225 | -1.233 | 0.2177 |  |
| Circulatory disease | -2.7522 | 1.8178 | ±3.6356 | -1.514 | 0.1300 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.2208** | 0.0631 | ±0.1262 | **+3.500** | **4.65e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1296**, Adj R² = **0.1155**, F-statistic = **9.21** (p = **1.72e-15**), Residual SE = **17.299** on **680** df, AIC = **5921.0**, BIC = **5975.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5798** | 6.0789 | ±12.1579 | **+9.637** | **5.61e-22** | *** |
| Education: graduate level (vs college) | -1.9114 | 1.4967 | ±2.9934 | -1.277 | 0.2016 |  |
| Education: high school or below (vs college) | +1.8953 | 1.9939 | ±3.9878 | +0.951 | 0.3418 |  |
| **Site: UCSD (vs UAB)** | **+3.9760** | 1.8235 | ±3.6469 | **+2.180** | **0.0292** | * |
| Site: UW (vs UAB) | +1.7846 | 1.6294 | ±3.2588 | +1.095 | 0.2734 |  |
| **Age (years)** | **-0.3892** | 0.0646 | ±0.1292 | **-6.023** | **1.71e-09** | *** |
| **BMI (kg/m2)** | **+0.3779** | 0.0994 | ±0.1987 | **+3.803** | **1.43e-04** | *** |
| Hypertension | -0.6693 | 1.5489 | ±3.0978 | -0.432 | 0.6657 |  |
| High cholesterol | +1.4337 | 1.4569 | ±2.9138 | +0.984 | 0.3251 |  |
| Kidney disease | -2.4856 | 1.9772 | ±3.9544 | -1.257 | 0.2087 |  |
| Circulatory disease | -2.7083 | 1.8168 | ±3.6336 | -1.491 | 0.1360 |  |
| **Avg. daily SD (mg/dL)** | **+0.2443** | 0.0739 | ±0.1477 | **+3.308** | **9.40e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **692**, R² = **0.1118**, Adj R² = **0.0974**, F-statistic = **7.78** (p = **8.90e-13**), Residual SE = **17.475** on **680** df, AIC = **5935.0**, BIC = **5989.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.7653** | 6.4391 | ±12.8782 | **+10.213** | **1.73e-24** | *** |
| Education: graduate level (vs college) | -2.2452 | 1.5065 | ±3.0130 | -1.490 | 0.1361 |  |
| Education: high school or below (vs college) | +2.8121 | 1.9984 | ±3.9967 | +1.407 | 0.1594 |  |
| Site: UCSD (vs UAB) | +3.5252 | 1.8298 | ±3.6597 | +1.927 | 0.0540 | . |
| Site: UW (vs UAB) | +0.9777 | 1.6206 | ±3.2413 | +0.603 | 0.5463 |  |
| **Age (years)** | **-0.3793** | 0.0663 | ±0.1326 | **-5.721** | **1.06e-08** | *** |
| **BMI (kg/m2)** | **+0.4104** | 0.0988 | ±0.1977 | **+4.152** | **3.29e-05** | *** |
| Hypertension | -0.3168 | 1.5452 | ±3.0904 | -0.205 | 0.8376 |  |
| High cholesterol | +1.2320 | 1.4589 | ±2.9179 | +0.844 | 0.3984 |  |
| Kidney disease | -1.1195 | 1.9920 | ±3.9840 | -0.562 | 0.5741 |  |
| Circulatory disease | -2.4360 | 1.8345 | ±3.6690 | -1.328 | 0.1842 |  |
| CV (%) | -0.0182 | 0.1284 | ±0.2569 | -0.141 | 0.8876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **692**, R² = **0.1118**, Adj R² = **0.0975**, F-statistic = **7.78** (p = **8.77e-13**), Residual SE = **17.475** on **680** df, AIC = **5935.0**, BIC = **5989.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0931** | 6.5416 | ±13.0832 | **+10.104** | **5.33e-24** | *** |
| Education: graduate level (vs college) | -2.2184 | 1.5049 | ±3.0097 | -1.474 | 0.1404 |  |
| Education: high school or below (vs college) | +2.7916 | 2.0024 | ±4.0049 | +1.394 | 0.1633 |  |
| Site: UCSD (vs UAB) | +3.5550 | 1.8281 | ±3.6562 | +1.945 | 0.0518 | . |
| Site: UW (vs UAB) | +1.0450 | 1.6207 | ±3.2413 | +0.645 | 0.5190 |  |
| **Age (years)** | **-0.3806** | 0.0661 | ±0.1322 | **-5.758** | **8.52e-09** | *** |
| **BMI (kg/m2)** | **+0.4107** | 0.0989 | ±0.1978 | **+4.153** | **3.29e-05** | *** |
| Hypertension | -0.3446 | 1.5457 | ±3.0914 | -0.223 | 0.8236 |  |
| High cholesterol | +1.2518 | 1.4584 | ±2.9167 | +0.858 | 0.3907 |  |
| Kidney disease | -1.2420 | 1.9810 | ±3.9620 | -0.627 | 0.5307 |  |
| Circulatory disease | -2.4355 | 1.8358 | ±3.6716 | -1.327 | 0.1846 |  |
| Mean / SD ratio | -0.1581 | 0.7058 | ±1.4117 | -0.224 | 0.8227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **692**, R² = **0.1119**, Adj R² = **0.0975**, F-statistic = **7.79** (p = **8.70e-13**), Residual SE = **17.475** on **680** df, AIC = **5935.0**, BIC = **5989.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1543** | 6.4244 | ±12.8489 | **+10.297** | **7.25e-25** | *** |
| Education: graduate level (vs college) | -2.2198 | 1.5031 | ±3.0063 | -1.477 | 0.1397 |  |
| Education: high school or below (vs college) | +2.7868 | 2.0037 | ±4.0073 | +1.391 | 0.1643 |  |
| Site: UCSD (vs UAB) | +3.5520 | 1.8280 | ±3.6560 | +1.943 | 0.0520 | . |
| Site: UW (vs UAB) | +1.0456 | 1.6172 | ±3.2344 | +0.647 | 0.5179 |  |
| **Age (years)** | **-0.3811** | 0.0662 | ±0.1324 | **-5.758** | **8.51e-09** | *** |
| **BMI (kg/m2)** | **+0.4117** | 0.0991 | ±0.1983 | **+4.152** | **3.29e-05** | *** |
| Hypertension | -0.3467 | 1.5461 | ±3.0921 | -0.224 | 0.8226 |  |
| High cholesterol | +1.2559 | 1.4591 | ±2.9182 | +0.861 | 0.3894 |  |
| Kidney disease | -1.2479 | 1.9870 | ±3.9739 | -0.628 | 0.5300 |  |
| Circulatory disease | -2.4286 | 1.8362 | ±3.6724 | -1.323 | 0.1860 |  |
| Avg. daily mean/SD | -0.1470 | 0.5600 | ±1.1200 | -0.263 | 0.7929 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **692**, R² = **0.1163**, Adj R² = **0.1020**, F-statistic = **8.13** (p = **1.90e-13**), Residual SE = **17.431** on **680** df, AIC = **5931.6**, BIC = **5986.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5723** | 6.9375 | ±13.8750 | **+8.443** | **3.10e-17** | *** |
| Education: graduate level (vs college) | -2.0193 | 1.5017 | ±3.0035 | -1.345 | 0.1787 |  |
| Education: high school or below (vs college) | +2.6325 | 1.9882 | ±3.9763 | +1.324 | 0.1855 |  |
| **Site: UCSD (vs UAB)** | **+3.8207** | 1.8386 | ±3.6773 | **+2.078** | **0.0377** | * |
| Site: UW (vs UAB) | +1.5113 | 1.6426 | ±3.2852 | +0.920 | 0.3575 |  |
| **Age (years)** | **-0.3708** | 0.0656 | ±0.1313 | **-5.648** | **1.62e-08** | *** |
| **BMI (kg/m2)** | **+0.4055** | 0.0993 | ±0.1987 | **+4.082** | **4.47e-05** | *** |
| Hypertension | -0.2571 | 1.5427 | ±3.0855 | -0.167 | 0.8676 |  |
| High cholesterol | +1.4286 | 1.4698 | ±2.9396 | +0.972 | 0.3311 |  |
| Kidney disease | -1.4311 | 1.9710 | ±3.9421 | -0.726 | 0.4678 |  |
| Circulatory disease | -2.4466 | 1.8267 | ±3.6534 | -1.339 | 0.1805 |  |
| MAG (mg/dL/h) | +0.1313 | 0.0731 | ±0.1462 | +1.796 | 0.0725 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **692**, R² = **0.1232**, Adj R² = **0.1091**, F-statistic = **8.69** (p = **1.66e-14**), Residual SE = **17.362** on **680** df, AIC = **5926.1**, BIC = **5980.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.8926** | 6.5268 | ±13.0536 | **+8.717** | **2.86e-18** | *** |
| Education: graduate level (vs college) | -1.9878 | 1.5014 | ±3.0027 | -1.324 | 0.1855 |  |
| Education: high school or below (vs college) | +2.0766 | 1.9964 | ±3.9927 | +1.040 | 0.2983 |  |
| **Site: UCSD (vs UAB)** | **+3.9718** | 1.8296 | ±3.6593 | **+2.171** | **0.0299** | * |
| Site: UW (vs UAB) | +1.6680 | 1.6375 | ±3.2750 | +1.019 | 0.3084 |  |
| **Age (years)** | **-0.3798** | 0.0651 | ±0.1302 | **-5.832** | **5.48e-09** | *** |
| **BMI (kg/m2)** | **+0.3944** | 0.0991 | ±0.1981 | **+3.981** | **6.86e-05** | *** |
| Hypertension | -0.4405 | 1.5470 | ±3.0939 | -0.285 | 0.7758 |  |
| High cholesterol | +1.4240 | 1.4620 | ±2.9240 | +0.974 | 0.3301 |  |
| Kidney disease | -2.2098 | 1.9838 | ±3.9677 | -1.114 | 0.2653 |  |
| Circulatory disease | -2.6264 | 1.8236 | ±3.6472 | -1.440 | 0.1498 |  |
| **Avg. daily range (mg/dL)** | **+0.0580** | 0.0212 | ±0.0423 | **+2.740** | **0.0061** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **692**, R² = **0.1271**, Adj R² = **0.1130**, F-statistic = **9.00** (p = **4.17e-15**), Residual SE = **17.324** on **680** df, AIC = **5923.0**, BIC = **5977.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5211** | 5.7876 | ±11.5753 | **+10.803** | **3.35e-27** | *** |
| Education: graduate level (vs college) | -1.7622 | 1.5193 | ±3.0386 | -1.160 | 0.2461 |  |
| Education: high school or below (vs college) | +2.4680 | 1.9422 | ±3.8845 | +1.271 | 0.2038 |  |
| **Site: UCSD (vs UAB)** | **+3.7463** | 1.8235 | ±3.6470 | **+2.054** | **0.0399** | * |
| Site: UW (vs UAB) | +1.5880 | 1.6074 | ±3.2149 | +0.988 | 0.3232 |  |
| **Age (years)** | **-0.3705** | 0.0652 | ±0.1304 | **-5.684** | **1.32e-08** | *** |
| **BMI (kg/m2)** | **+0.3583** | 0.0987 | ±0.1975 | **+3.628** | **2.85e-04** | *** |
| Hypertension | -0.7368 | 1.5444 | ±3.0888 | -0.477 | 0.6333 |  |
| High cholesterol | +1.4080 | 1.4605 | ±2.9210 | +0.964 | 0.3350 |  |
| Kidney disease | -1.4871 | 1.9410 | ±3.8820 | -0.766 | 0.4436 |  |
| Circulatory disease | -2.8757 | 1.8289 | ±3.6578 | -1.572 | 0.1159 |  |
| **SD of daily means (mg/dL)** | **+0.2912** | 0.0837 | ±0.1673 | **+3.481** | **5.00e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **692**, R² = **0.1498**, Adj R² = **0.1360**, F-statistic = **10.89** (p = **1.12e-18**), Residual SE = **17.097** on **680** df, AIC = **5904.8**, BIC = **5959.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0467** | 6.1317 | ±12.2634 | **+12.891** | **5.03e-38** | *** |
| Education: graduate level (vs college) | -1.8141 | 1.4893 | ±2.9787 | -1.218 | 0.2232 |  |
| Education: high school or below (vs college) | +1.5223 | 1.9194 | ±3.8387 | +0.793 | 0.4277 |  |
| **Site: UCSD (vs UAB)** | **+4.1926** | 1.8185 | ±3.6371 | **+2.305** | **0.0211** | * |
| Site: UW (vs UAB) | +1.8177 | 1.5903 | ±3.1806 | +1.143 | 0.2530 |  |
| **Age (years)** | **-0.3797** | 0.0642 | ±0.1285 | **-5.910** | **3.42e-09** | *** |
| **BMI (kg/m2)** | **+0.3074** | 0.0997 | ±0.1993 | **+3.085** | **0.0020** | ** |
| Hypertension | -0.6078 | 1.5275 | ±3.0550 | -0.398 | 0.6907 |  |
| High cholesterol | +1.4808 | 1.4454 | ±2.8908 | +1.024 | 0.3056 |  |
| Kidney disease | -1.7998 | 1.9195 | ±3.8390 | -0.938 | 0.3484 |  |
| Circulatory disease | -3.0750 | 1.7980 | ±3.5960 | -1.710 | 0.0872 | . |
| **Time in range 70-180, pooled (%)** | **-0.1502** | 0.0295 | ±0.0590 | **-5.087** | **3.65e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **692**, R² = **0.1485**, Adj R² = **0.1347**, F-statistic = **10.78** (p = **1.80e-18**), Residual SE = **17.110** on **680** df, AIC = **5905.8**, BIC = **5960.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.9119** | 6.1523 | ±12.3046 | **+12.826** | **1.17e-37** | *** |
| Education: graduate level (vs college) | -1.8604 | 1.4905 | ±2.9811 | -1.248 | 0.2120 |  |
| Education: high school or below (vs college) | +1.5099 | 1.9203 | ±3.8405 | +0.786 | 0.4317 |  |
| **Site: UCSD (vs UAB)** | **+4.2303** | 1.8210 | ±3.6419 | **+2.323** | **0.0202** | * |
| Site: UW (vs UAB) | +1.8127 | 1.5914 | ±3.1828 | +1.139 | 0.2547 |  |
| **Age (years)** | **-0.3814** | 0.0644 | ±0.1288 | **-5.923** | **3.15e-09** | *** |
| **BMI (kg/m2)** | **+0.3079** | 0.1000 | ±0.2000 | **+3.079** | **0.0021** | ** |
| Hypertension | -0.5834 | 1.5281 | ±3.0561 | -0.382 | 0.7026 |  |
| High cholesterol | +1.4661 | 1.4459 | ±2.8919 | +1.014 | 0.3106 |  |
| Kidney disease | -1.8462 | 1.9224 | ±3.8447 | -0.960 | 0.3369 |  |
| Circulatory disease | -3.0485 | 1.8003 | ±3.6007 | -1.693 | 0.0904 | . |
| **Avg. daily time in range 70-180 (%)** | **-0.1465** | 0.0293 | ±0.0586 | **-5.002** | **5.67e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1128**, Adj R² = **0.0984**, F-statistic = **7.86** (p = **6.34e-13**), Residual SE = **17.466** on **680** df, AIC = **5934.3**, BIC = **5988.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.8652** | 5.8029 | ±11.6058 | **+11.350** | **7.38e-30** | *** |
| Education: graduate level (vs college) | -2.2682 | 1.5064 | ±3.0128 | -1.506 | 0.1321 |  |
| Education: high school or below (vs college) | +2.7308 | 1.9989 | ±3.9978 | +1.366 | 0.1719 |  |
| Site: UCSD (vs UAB) | +3.4535 | 1.8292 | ±3.6584 | +1.888 | 0.0590 | . |
| Site: UW (vs UAB) | +0.9320 | 1.6086 | ±3.2171 | +0.579 | 0.5623 |  |
| **Age (years)** | **-0.3818** | 0.0663 | ±0.1326 | **-5.758** | **8.49e-09** | *** |
| **BMI (kg/m2)** | **+0.4108** | 0.0991 | ±0.1982 | **+4.146** | **3.39e-05** | *** |
| Hypertension | -0.2784 | 1.5416 | ±3.0832 | -0.181 | 0.8567 |  |
| High cholesterol | +1.1715 | 1.4603 | ±2.9207 | +0.802 | 0.4224 |  |
| Kidney disease | -1.1793 | 1.9571 | ±3.9142 | -0.603 | 0.5468 |  |
| Circulatory disease | -2.3546 | 1.8302 | ±3.6604 | -1.286 | 0.1983 |  |
| Any reading < 54 during wear (0/1) | -1.3828 | 1.5834 | ±3.1668 | -0.873 | 0.3825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1120**, Adj R² = **0.0977**, F-statistic = **7.80** (p = **8.17e-13**), Residual SE = **17.473** on **680** df, AIC = **5934.9**, BIC = **5989.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5129** | 5.7571 | ±11.5143 | **+11.379** | **5.30e-30** | *** |
| Education: graduate level (vs college) | -2.2740 | 1.5046 | ±3.0092 | -1.511 | 0.1307 |  |
| Education: high school or below (vs college) | +2.7532 | 1.9977 | ±3.9954 | +1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +3.4846 | 1.8286 | ±3.6573 | +1.906 | 0.0567 | . |
| Site: UW (vs UAB) | +0.9365 | 1.6102 | ±3.2204 | +0.582 | 0.5608 |  |
| **Age (years)** | **-0.3787** | 0.0662 | ±0.1323 | **-5.723** | **1.04e-08** | *** |
| **BMI (kg/m2)** | **+0.4079** | 0.0993 | ±0.1985 | **+4.109** | **3.97e-05** | *** |
| Hypertension | -0.3271 | 1.5413 | ±3.0827 | -0.212 | 0.8320 |  |
| High cholesterol | +1.1898 | 1.4601 | ±2.9202 | +0.815 | 0.4151 |  |
| Kidney disease | -1.1825 | 1.9542 | ±3.9085 | -0.605 | 0.5451 |  |
| Circulatory disease | -2.4614 | 1.8335 | ±3.6671 | -1.342 | 0.1795 |  |
| Time < 54 (%) | -0.5112 | 1.3113 | ±2.6227 | -0.390 | 0.6967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **692**, R² = **0.1126**, Adj R² = **0.0982**, F-statistic = **7.84** (p = **6.83e-13**), Residual SE = **17.468** on **680** df, AIC = **5934.4**, BIC = **5988.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5688** | 5.7546 | ±11.5092 | **+11.394** | **4.47e-30** | *** |
| Education: graduate level (vs college) | -2.2923 | 1.5033 | ±3.0066 | -1.525 | 0.1273 |  |
| Education: high school or below (vs college) | +2.7124 | 1.9955 | ±3.9910 | +1.359 | 0.1741 |  |
| Site: UCSD (vs UAB) | +3.4410 | 1.8298 | ±3.6596 | +1.881 | 0.0600 | . |
| Site: UW (vs UAB) | +0.8715 | 1.6111 | ±3.2223 | +0.541 | 0.5886 |  |
| **Age (years)** | **-0.3782** | 0.0662 | ±0.1323 | **-5.717** | **1.09e-08** | *** |
| **BMI (kg/m2)** | **+0.4082** | 0.0991 | ±0.1983 | **+4.117** | **3.83e-05** | *** |
| Hypertension | -0.3159 | 1.5401 | ±3.0801 | -0.205 | 0.8375 |  |
| High cholesterol | +1.1358 | 1.4588 | ±2.9175 | +0.779 | 0.4362 |  |
| Kidney disease | -1.1693 | 1.9541 | ±3.9082 | -0.598 | 0.5496 |  |
| Circulatory disease | -2.4822 | 1.8323 | ±3.6645 | -1.355 | 0.1755 |  |
| Avg. daily time < 54 (%) | -0.9999 | 1.0347 | ±2.0694 | -0.966 | 0.3338 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **692**, R² = **0.1123**, Adj R² = **0.0979**, F-statistic = **7.82** (p = **7.56e-13**), Residual SE = **17.471** on **680** df, AIC = **5934.7**, BIC = **5989.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5536** | 5.7651 | ±11.5301 | **+11.371** | **5.84e-30** | *** |
| Education: graduate level (vs college) | -2.3025 | 1.5069 | ±3.0138 | -1.528 | 0.1265 |  |
| Education: high school or below (vs college) | +2.7474 | 1.9931 | ±3.9862 | +1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +3.4392 | 1.8261 | ±3.6521 | +1.883 | 0.0596 | . |
| Site: UW (vs UAB) | +0.8885 | 1.6175 | ±3.2350 | +0.549 | 0.5828 |  |
| **Age (years)** | **-0.3780** | 0.0663 | ±0.1326 | **-5.703** | **1.18e-08** | *** |
| **BMI (kg/m2)** | **+0.4100** | 0.0991 | ±0.1982 | **+4.136** | **3.53e-05** | *** |
| Hypertension | -0.3006 | 1.5513 | ±3.1025 | -0.194 | 0.8464 |  |
| High cholesterol | +1.1430 | 1.4577 | ±2.9154 | +0.784 | 0.4330 |  |
| Kidney disease | -1.1577 | 1.9541 | ±3.9083 | -0.592 | 0.5536 |  |
| Circulatory disease | -2.5036 | 1.8399 | ±3.6798 | -1.361 | 0.1736 |  |
| Time 54-69, pooled (%) | -0.4015 | 1.1048 | ±2.2096 | -0.363 | 0.7163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **692**, R² = **0.1124**, Adj R² = **0.0981**, F-statistic = **7.83** (p = **7.17e-13**), Residual SE = **17.469** on **680** df, AIC = **5934.6**, BIC = **5989.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5291** | 5.7526 | ±11.5052 | **+11.391** | **4.63e-30** | *** |
| Education: graduate level (vs college) | -2.3103 | 1.5056 | ±3.0111 | -1.535 | 0.1249 |  |
| Education: high school or below (vs college) | +2.7329 | 1.9914 | ±3.9828 | +1.372 | 0.1699 |  |
| Site: UCSD (vs UAB) | +3.4233 | 1.8280 | ±3.6560 | +1.873 | 0.0611 | . |
| Site: UW (vs UAB) | +0.8626 | 1.6199 | ±3.2398 | +0.533 | 0.5944 |  |
| **Age (years)** | **-0.3775** | 0.0663 | ±0.1327 | **-5.691** | **1.27e-08** | *** |
| **BMI (kg/m2)** | **+0.4104** | 0.0990 | ±0.1980 | **+4.146** | **3.38e-05** | *** |
| Hypertension | -0.2946 | 1.5512 | ±3.1024 | -0.190 | 0.8494 |  |
| High cholesterol | +1.1272 | 1.4562 | ±2.9124 | +0.774 | 0.4389 |  |
| Kidney disease | -1.1502 | 1.9548 | ±3.9096 | -0.588 | 0.5563 |  |
| Circulatory disease | -2.5116 | 1.8393 | ±3.6787 | -1.366 | 0.1721 |  |
| Avg. daily time 54-69 (%) | -0.4269 | 1.0180 | ±2.0360 | -0.419 | 0.6749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **692**, R² = **0.1123**, Adj R² = **0.0979**, F-statistic = **7.82** (p = **7.43e-13**), Residual SE = **17.470** on **680** df, AIC = **5934.6**, BIC = **5989.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.6012** | 5.7715 | ±11.5431 | **+11.366** | **6.15e-30** | *** |
| Education: graduate level (vs college) | -2.3110 | 1.5074 | ±3.0148 | -1.533 | 0.1253 |  |
| Education: high school or below (vs college) | +2.7300 | 1.9948 | ±3.9897 | +1.369 | 0.1711 |  |
| Site: UCSD (vs UAB) | +3.4287 | 1.8284 | ±3.6569 | +1.875 | 0.0608 | . |
| Site: UW (vs UAB) | +0.8734 | 1.6189 | ±3.2377 | +0.540 | 0.5895 |  |
| **Age (years)** | **-0.3778** | 0.0663 | ±0.1326 | **-5.698** | **1.21e-08** | *** |
| **BMI (kg/m2)** | **+0.4086** | 0.0994 | ±0.1988 | **+4.111** | **3.95e-05** | *** |
| Hypertension | -0.3065 | 1.5456 | ±3.0913 | -0.198 | 0.8428 |  |
| High cholesterol | +1.1337 | 1.4588 | ±2.9175 | +0.777 | 0.4371 |  |
| Kidney disease | -1.1679 | 1.9533 | ±3.9067 | -0.598 | 0.5499 |  |
| Circulatory disease | -2.5045 | 1.8373 | ±3.6747 | -1.363 | 0.1728 |  |
| Time < 70 (%) | -0.3089 | 0.6625 | ±1.3250 | -0.466 | 0.6410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **692**, R² = **0.1126**, Adj R² = **0.0983**, F-statistic = **7.84** (p = **6.70e-13**), Residual SE = **17.467** on **680** df, AIC = **5934.4**, BIC = **5988.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5808** | 5.7570 | ±11.5139 | **+11.392** | **4.61e-30** | *** |
| Education: graduate level (vs college) | -2.3206 | 1.5050 | ±3.0101 | -1.542 | 0.1231 |  |
| Education: high school or below (vs college) | +2.7099 | 1.9924 | ±3.9847 | +1.360 | 0.1738 |  |
| Site: UCSD (vs UAB) | +3.4039 | 1.8298 | ±3.6596 | +1.860 | 0.0628 | . |
| Site: UW (vs UAB) | +0.8342 | 1.6205 | ±3.2411 | +0.515 | 0.6067 |  |
| **Age (years)** | **-0.3772** | 0.0663 | ±0.1326 | **-5.690** | **1.27e-08** | *** |
| **BMI (kg/m2)** | **+0.4096** | 0.0991 | ±0.1983 | **+4.132** | **3.59e-05** | *** |
| Hypertension | -0.2951 | 1.5470 | ±3.0939 | -0.191 | 0.8487 |  |
| High cholesterol | +1.1046 | 1.4576 | ±2.9152 | +0.758 | 0.4485 |  |
| Kidney disease | -1.1527 | 1.9539 | ±3.9078 | -0.590 | 0.5552 |  |
| Circulatory disease | -2.5182 | 1.8370 | ±3.6740 | -1.371 | 0.1704 |  |
| Avg. daily time < 70 (%) | -0.3651 | 0.6659 | ±1.3319 | -0.548 | 0.5835 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1281**, Adj R² = **0.1140**, F-statistic = **9.08** (p = **3.00e-15**), Residual SE = **17.315** on **680** df, AIC = **5922.3**, BIC = **5976.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.5253** | 7.0705 | ±14.1409 | **+11.106** | **1.17e-28** | *** |
| Education: graduate level (vs college) | -1.7916 | 1.5115 | ±3.0230 | -1.185 | 0.2359 |  |
| Education: high school or below (vs college) | +2.1065 | 1.9461 | ±3.8922 | +1.082 | 0.2791 |  |
| **Site: UCSD (vs UAB)** | **+3.8356** | 1.8224 | ±3.6448 | **+2.105** | **0.0353** | * |
| Site: UW (vs UAB) | +1.5844 | 1.6119 | ±3.2239 | +0.983 | 0.3257 |  |
| **Age (years)** | **-0.3623** | 0.0649 | ±0.1299 | **-5.579** | **2.41e-08** | *** |
| **BMI (kg/m2)** | **+0.3735** | 0.0989 | ±0.1979 | **+3.775** | **1.60e-04** | *** |
| Hypertension | -0.5163 | 1.5338 | ±3.0676 | -0.337 | 0.7364 |  |
| High cholesterol | +1.4046 | 1.4557 | ±2.9113 | +0.965 | 0.3346 |  |
| Kidney disease | -1.4483 | 1.9425 | ±3.8850 | -0.746 | 0.4559 |  |
| Circulatory disease | -2.7589 | 1.8091 | ±3.6183 | -1.525 | 0.1273 |  |
| **Time 54-250, pooled (%)** | **-0.1454** | 0.0487 | ±0.0974 | **-2.988** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **692**, R² = **0.1282**, Adj R² = **0.1141**, F-statistic = **9.09** (p = **2.82e-15**), Residual SE = **17.313** on **680** df, AIC = **5922.1**, BIC = **5976.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0038** | 7.1838 | ±14.3675 | **+10.998** | **3.93e-28** | *** |
| Education: graduate level (vs college) | -1.7997 | 1.5107 | ±3.0214 | -1.191 | 0.2335 |  |
| Education: high school or below (vs college) | +2.1041 | 1.9457 | ±3.8913 | +1.081 | 0.2795 |  |
| **Site: UCSD (vs UAB)** | **+3.8428** | 1.8221 | ±3.6443 | **+2.109** | **0.0349** | * |
| Site: UW (vs UAB) | +1.5684 | 1.6107 | ±3.2213 | +0.974 | 0.3302 |  |
| **Age (years)** | **-0.3643** | 0.0649 | ±0.1299 | **-5.610** | **2.03e-08** | *** |
| **BMI (kg/m2)** | **+0.3721** | 0.0992 | ±0.1984 | **+3.750** | **1.77e-04** | *** |
| Hypertension | -0.5023 | 1.5329 | ±3.0659 | -0.328 | 0.7432 |  |
| High cholesterol | +1.4083 | 1.4554 | ±2.9109 | +0.968 | 0.3333 |  |
| Kidney disease | -1.4923 | 1.9430 | ±3.8859 | -0.768 | 0.4424 |  |
| Circulatory disease | -2.7791 | 1.8099 | ±3.6198 | -1.535 | 0.1247 |  |
| **Avg. daily time 54-250 (%)** | **-0.1483** | 0.0499 | ±0.0998 | **-2.971** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1457**, Adj R² = **0.1319**, F-statistic = **10.54** (p = **5.12e-18**), Residual SE = **17.139** on **680** df, AIC = **5908.1**, BIC = **5962.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.6206** | 5.6793 | ±11.3587 | **+11.554** | **7.02e-31** | *** |
| Education: graduate level (vs college) | -2.3331 | 1.4807 | ±2.9614 | -1.576 | 0.1151 |  |
| Education: high school or below (vs college) | +1.8801 | 1.9665 | ±3.9330 | +0.956 | 0.3390 |  |
| **Site: UCSD (vs UAB)** | **+4.0311** | 1.8146 | ±3.6293 | **+2.221** | **0.0263** | * |
| Site: UW (vs UAB) | +1.2765 | 1.5749 | ±3.1497 | +0.811 | 0.4176 |  |
| **Age (years)** | **-0.4072** | 0.0650 | ±0.1301 | **-6.262** | **3.80e-10** | *** |
| **BMI (kg/m2)** | **+0.3073** | 0.1007 | ±0.2013 | **+3.052** | **0.0023** | ** |
| Hypertension | -0.4468 | 1.5323 | ±3.0646 | -0.292 | 0.7706 |  |
| High cholesterol | +1.2963 | 1.4426 | ±2.8852 | +0.899 | 0.3689 |  |
| Kidney disease | -1.7059 | 1.9146 | ±3.8292 | -0.891 | 0.3729 |  |
| Circulatory disease | -2.9590 | 1.8204 | ±3.6408 | -1.625 | 0.1041 |  |
| **Time 181-250, pooled (%)** | **+0.2381** | 0.0478 | ±0.0955 | **+4.985** | **6.21e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **692**, R² = **0.1438**, Adj R² = **0.1300**, F-statistic = **10.38** (p = **1.02e-17**), Residual SE = **17.158** on **680** df, AIC = **5909.6**, BIC = **5964.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.5646** | 5.6845 | ±11.3689 | **+11.534** | **8.89e-31** | *** |
| Education: graduate level (vs college) | -2.3602 | 1.4845 | ±2.9690 | -1.590 | 0.1119 |  |
| Education: high school or below (vs college) | +1.8328 | 1.9617 | ±3.9233 | +0.934 | 0.3501 |  |
| **Site: UCSD (vs UAB)** | **+4.0840** | 1.8182 | ±3.6364 | **+2.246** | **0.0247** | * |
| Site: UW (vs UAB) | +1.3189 | 1.5782 | ±3.1564 | +0.836 | 0.4033 |  |
| **Age (years)** | **-0.4047** | 0.0651 | ±0.1302 | **-6.217** | **5.06e-10** | *** |
| **BMI (kg/m2)** | **+0.3104** | 0.1009 | ±0.2018 | **+3.077** | **0.0021** | ** |
| Hypertension | -0.4390 | 1.5335 | ±3.0671 | -0.286 | 0.7747 |  |
| High cholesterol | +1.2744 | 1.4439 | ±2.8878 | +0.883 | 0.3775 |  |
| Kidney disease | -1.7137 | 1.9191 | ±3.8382 | -0.893 | 0.3719 |  |
| Circulatory disease | -2.8984 | 1.8248 | ±3.6496 | -1.588 | 0.1122 |  |
| **Avg. daily time 181-250 (%)** | **+0.2269** | 0.0468 | ±0.0936 | **+4.850** | **1.23e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **692**, R² = **0.1497**, Adj R² = **0.1360**, F-statistic = **10.88** (p = **1.15e-18**), Residual SE = **17.098** on **680** df, AIC = **5904.8**, BIC = **5959.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.1577** | 5.6461 | ±11.2922 | **+11.363** | **6.38e-30** | *** |
| Education: graduate level (vs college) | -1.8553 | 1.4885 | ±2.9771 | -1.246 | 0.2126 |  |
| Education: high school or below (vs college) | +1.4989 | 1.9187 | ±3.8374 | +0.781 | 0.4347 |  |
| **Site: UCSD (vs UAB)** | **+4.1327** | 1.8171 | ±3.6342 | **+2.274** | **0.0229** | * |
| Site: UW (vs UAB) | +1.7461 | 1.5875 | ±3.1751 | +1.100 | 0.2714 |  |
| **Age (years)** | **-0.3786** | 0.0643 | ±0.1285 | **-5.892** | **3.81e-09** | *** |
| **BMI (kg/m2)** | **+0.3075** | 0.0998 | ±0.1996 | **+3.080** | **0.0021** | ** |
| Hypertension | -0.5950 | 1.5269 | ±3.0538 | -0.390 | 0.6968 |  |
| High cholesterol | +1.4257 | 1.4434 | ±2.8868 | +0.988 | 0.3233 |  |
| Kidney disease | -1.7927 | 1.9186 | ±3.8373 | -0.934 | 0.3501 |  |
| Circulatory disease | -3.1035 | 1.7987 | ±3.5975 | -1.725 | 0.0845 | . |
| **Time > 180 (%)** | **+0.1488** | 0.0293 | ±0.0586 | **+5.075** | **3.87e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1487**, Adj R² = **0.1349**, F-statistic = **10.80** (p = **1.70e-18**), Residual SE = **17.109** on **680** df, AIC = **5905.7**, BIC = **5960.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.3522** | 5.6558 | ±11.3117 | **+11.378** | **5.38e-30** | *** |
| Education: graduate level (vs college) | -1.8969 | 1.4898 | ±2.9796 | -1.273 | 0.2029 |  |
| Education: high school or below (vs college) | +1.4787 | 1.9190 | ±3.8381 | +0.771 | 0.4410 |  |
| **Site: UCSD (vs UAB)** | **+4.1725** | 1.8194 | ±3.6389 | **+2.293** | **0.0218** | * |
| Site: UW (vs UAB) | +1.7401 | 1.5885 | ±3.1769 | +1.095 | 0.2733 |  |
| **Age (years)** | **-0.3803** | 0.0644 | ±0.1288 | **-5.906** | **3.50e-09** | *** |
| **BMI (kg/m2)** | **+0.3081** | 0.1002 | ±0.2003 | **+3.076** | **0.0021** | ** |
| Hypertension | -0.5692 | 1.5272 | ±3.0543 | -0.373 | 0.7094 |  |
| High cholesterol | +1.4096 | 1.4434 | ±2.8868 | +0.977 | 0.3288 |  |
| Kidney disease | -1.8359 | 1.9212 | ±3.8423 | -0.956 | 0.3393 |  |
| Circulatory disease | -3.0797 | 1.8012 | ±3.6025 | -1.710 | 0.0873 | . |
| **Avg. daily time > 180 (%)** | **+0.1458** | 0.0291 | ±0.0583 | **+5.007** | **5.53e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **692**, R² = **0.1342**, Adj R² = **0.1202**, F-statistic = **9.58** (p = **3.30e-16**), Residual SE = **17.253** on **680** df, AIC = **5917.3**, BIC = **5971.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.9687** | 5.7250 | ±11.4500 | **+11.348** | **7.57e-30** | *** |
| Education: graduate level (vs college) | -1.7654 | 1.5106 | ±3.0211 | -1.169 | 0.2425 |  |
| Education: high school or below (vs college) | +1.9905 | 1.9230 | ±3.8460 | +1.035 | 0.3006 |  |
| **Site: UCSD (vs UAB)** | **+4.0421** | 1.8295 | ±3.6590 | **+2.209** | **0.0271** | * |
| Site: UW (vs UAB) | +1.4573 | 1.5940 | ±3.1880 | +0.914 | 0.3606 |  |
| **Age (years)** | **-0.3683** | 0.0655 | ±0.1310 | **-5.624** | **1.87e-08** | *** |
| **BMI (kg/m2)** | **+0.3153** | 0.1013 | ±0.2025 | **+3.114** | **0.0018** | ** |
| Hypertension | -0.4885 | 1.5363 | ±3.0727 | -0.318 | 0.7505 |  |
| High cholesterol | +1.5001 | 1.4557 | ±2.9113 | +1.031 | 0.3028 |  |
| Kidney disease | -1.4048 | 1.9355 | ±3.8710 | -0.726 | 0.4680 |  |
| Circulatory disease | -2.9301 | 1.8066 | ±3.6132 | -1.622 | 0.1048 |  |
| **Nocturnal time > 180 (%)** | **+0.1046** | 0.0266 | ±0.0532 | **+3.935** | **8.33e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **692**, R² = **0.1282**, Adj R² = **0.1141**, F-statistic = **9.09** (p = **2.85e-15**), Residual SE = **17.313** on **680** df, AIC = **5922.1**, BIC = **5976.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0199** | 5.7147 | ±11.4293 | **+11.203** | **3.95e-29** | *** |
| Education: graduate level (vs college) | -1.8011 | 1.5109 | ±3.0217 | -1.192 | 0.2332 |  |
| Education: high school or below (vs college) | +2.0891 | 1.9460 | ±3.8920 | +1.074 | 0.2830 |  |
| **Site: UCSD (vs UAB)** | **+3.8209** | 1.8216 | ±3.6433 | **+2.098** | **0.0359** | * |
| Site: UW (vs UAB) | +1.5669 | 1.6104 | ±3.2208 | +0.973 | 0.3305 |  |
| **Age (years)** | **-0.3619** | 0.0649 | ±0.1299 | **-5.572** | **2.51e-08** | *** |
| **BMI (kg/m2)** | **+0.3726** | 0.0990 | ±0.1979 | **+3.765** | **1.66e-04** | *** |
| Hypertension | -0.5170 | 1.5336 | ±3.0672 | -0.337 | 0.7360 |  |
| High cholesterol | +1.3900 | 1.4550 | ±2.9099 | +0.955 | 0.3394 |  |
| Kidney disease | -1.4529 | 1.9425 | ±3.8851 | -0.748 | 0.4545 |  |
| Circulatory disease | -2.7685 | 1.8093 | ±3.6186 | -1.530 | 0.1260 |  |
| **Time > 250 (%)** | **+0.1461** | 0.0487 | ±0.0973 | **+3.002** | **0.0027** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 692)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **692**, R² = **0.1285**, Adj R² = **0.1144**, F-statistic = **9.11** (p = **2.59e-15**), Residual SE = **17.311** on **680** df, AIC = **5921.9**, BIC = **5976.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.1935** | 5.7204 | ±11.4409 | **+11.222** | **3.19e-29** | *** |
| Education: graduate level (vs college) | -1.8055 | 1.5102 | ±3.0205 | -1.195 | 0.2319 |  |
| Education: high school or below (vs college) | +2.0856 | 1.9453 | ±3.8906 | +1.072 | 0.2837 |  |
| **Site: UCSD (vs UAB)** | **+3.8300** | 1.8214 | ±3.6429 | **+2.103** | **0.0355** | * |
| Site: UW (vs UAB) | +1.5521 | 1.6092 | ±3.2184 | +0.965 | 0.3348 |  |
| **Age (years)** | **-0.3640** | 0.0649 | ±0.1299 | **-5.604** | **2.09e-08** | *** |
| **BMI (kg/m2)** | **+0.3715** | 0.0993 | ±0.1985 | **+3.743** | **1.82e-04** | *** |
| Hypertension | -0.5017 | 1.5326 | ±3.0651 | -0.327 | 0.7434 |  |
| High cholesterol | +1.3933 | 1.4545 | ±2.9090 | +0.958 | 0.3381 |  |
| Kidney disease | -1.4944 | 1.9429 | ±3.8858 | -0.769 | 0.4418 |  |
| Circulatory disease | -2.7889 | 1.8100 | ±3.6201 | -1.541 | 0.1234 |  |
| **Avg. daily time > 250 (%)** | **+0.1494** | 0.0500 | ±0.0999 | **+2.990** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
