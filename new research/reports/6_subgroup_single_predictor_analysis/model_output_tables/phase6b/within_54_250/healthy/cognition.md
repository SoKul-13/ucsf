# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 685; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, R² = **0.1195**, Adj R² = **0.1064**, F-statistic = **9.14** (p = **2.96e-14**), Residual SE = **2.668** on **674** df, AIC = **3299.4**, BIC = **3349.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2282** | 0.8665 | ±1.7329 | **+34.887** | **1.17e-266** | *** |
| **Education: graduate level (vs college)** | **+0.6539** | 0.2097 | ±0.4193 | **+3.119** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.6412** | 0.5058 | ±1.0116 | **-3.245** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5252 | 0.2965 | ±0.5931 | -1.771 | 0.0766 | . |
| Site: UW (vs UAB) | -0.2570 | 0.2889 | ±0.5778 | -0.889 | 0.3738 |  |
| **Age (years)** | **-0.0511** | 0.0101 | ±0.0202 | **-5.049** | **4.44e-07** | *** |
| **BMI (kg/m2)** | **-0.0299** | 0.0150 | ±0.0300 | **-1.993** | **0.0463** | * |
| Hypertension | -0.2567 | 0.2388 | ±0.4776 | -1.075 | 0.2825 |  |
| High cholesterol | +0.1468 | 0.2173 | ±0.4346 | +0.676 | 0.4993 |  |
| Kidney disease | -0.0369 | 0.4457 | ±0.8914 | -0.083 | 0.9341 |  |
| Circulatory disease | -0.5981 | 0.3752 | ±0.7504 | -1.594 | 0.1109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, R² = **0.1263**, Adj R² = **0.1120**, F-statistic = **8.84** (p = **8.74e-15**), Residual SE = **2.660** on **673** df, AIC = **3296.1**, BIC = **3350.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.9216** | 1.9578 | ±3.9156 | **+17.326** | **2.98e-67** | *** |
| **Education: graduate level (vs college)** | **+0.6635** | 0.2095 | ±0.4190 | **+3.167** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.6360** | 0.5009 | ±1.0019 | **-3.266** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5257 | 0.2957 | ±0.5914 | -1.778 | 0.0755 | . |
| Site: UW (vs UAB) | -0.2475 | 0.2893 | ±0.5786 | -0.856 | 0.3923 |  |
| **Age (years)** | **-0.0485** | 0.0101 | ±0.0201 | **-4.820** | **1.43e-06** | *** |
| BMI (kg/m2) | -0.0251 | 0.0152 | ±0.0303 | -1.653 | 0.0984 | . |
| Hypertension | -0.2121 | 0.2381 | ±0.4761 | -0.891 | 0.3729 |  |
| High cholesterol | +0.1933 | 0.2161 | ±0.4322 | +0.894 | 0.3711 |  |
| Kidney disease | -0.0403 | 0.4336 | ±0.8673 | -0.093 | 0.9260 |  |
| Circulatory disease | -0.6144 | 0.3744 | ±0.7488 | -1.641 | 0.1008 |  |
| **HbA1c (%)** | **-0.7219** | 0.3326 | ±0.6652 | **-2.170** | **0.0300** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, R² = **0.1295**, Adj R² = **0.1153**, F-statistic = **9.10** (p = **2.75e-15**), Residual SE = **2.655** on **673** df, AIC = **3293.5**, BIC = **3347.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.0384** | 1.4351 | ±2.8701 | **+23.022** | **2.79e-117** | *** |
| **Education: graduate level (vs college)** | **+0.6933** | 0.2086 | ±0.4172 | **+3.324** | **8.89e-04** | *** |
| **Education: high school or below (vs college)** | **-1.6095** | 0.4987 | ±0.9974 | **-3.227** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5543 | 0.2915 | ±0.5829 | -1.902 | 0.0572 | . |
| Site: UW (vs UAB) | -0.2060 | 0.2893 | ±0.5786 | -0.712 | 0.4765 |  |
| **Age (years)** | **-0.0497** | 0.0101 | ±0.0202 | **-4.929** | **8.26e-07** | *** |
| BMI (kg/m2) | -0.0253 | 0.0154 | ±0.0308 | -1.643 | 0.1005 |  |
| Hypertension | -0.2164 | 0.2392 | ±0.4784 | -0.905 | 0.3657 |  |
| High cholesterol | +0.1437 | 0.2174 | ±0.4348 | +0.661 | 0.5087 |  |
| Kidney disease | +0.0100 | 0.4341 | ±0.8681 | +0.023 | 0.9816 |  |
| Circulatory disease | -0.5402 | 0.3705 | ±0.7411 | -1.458 | 0.1449 |  |
| **Mean glucose (mg/dL)** | **-0.0259** | 0.0115 | ±0.0230 | **-2.247** | **0.0246** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, R² = **0.1295**, Adj R² = **0.1153**, F-statistic = **9.10** (p = **2.75e-15**), Residual SE = **2.655** on **673** df, AIC = **3293.5**, BIC = **3347.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+36.6167** | 2.8753 | ±5.7507 | **+12.735** | **3.79e-37** | *** |
| **Education: graduate level (vs college)** | **+0.6933** | 0.2086 | ±0.4172 | **+3.324** | **8.89e-04** | *** |
| **Education: high school or below (vs college)** | **-1.6095** | 0.4987 | ±0.9974 | **-3.227** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5543 | 0.2915 | ±0.5829 | -1.902 | 0.0572 | . |
| Site: UW (vs UAB) | -0.2060 | 0.2893 | ±0.5786 | -0.712 | 0.4765 |  |
| **Age (years)** | **-0.0497** | 0.0101 | ±0.0202 | **-4.929** | **8.26e-07** | *** |
| BMI (kg/m2) | -0.0253 | 0.0154 | ±0.0308 | -1.643 | 0.1005 |  |
| Hypertension | -0.2164 | 0.2392 | ±0.4784 | -0.905 | 0.3657 |  |
| High cholesterol | +0.1437 | 0.2174 | ±0.4348 | +0.661 | 0.5087 |  |
| Kidney disease | +0.0100 | 0.4341 | ±0.8681 | +0.023 | 0.9816 |  |
| Circulatory disease | -0.5402 | 0.3705 | ±0.7411 | -1.458 | 0.1449 |  |
| **GMI (%)** | **-1.0810** | 0.4811 | ±0.9622 | **-2.247** | **0.0246** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, R² = **0.1247**, Adj R² = **0.1104**, F-statistic = **8.71** (p = **1.52e-14**), Residual SE = **2.662** on **673** df, AIC = **3297.4**, BIC = **3351.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9936** | 1.2705 | ±2.5409 | **+25.183** | **6.23e-140** | *** |
| **Education: graduate level (vs college)** | **+0.6708** | 0.2094 | ±0.4188 | **+3.204** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.6249** | 0.5007 | ±1.0014 | **-3.245** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5244 | 0.2950 | ±0.5900 | -1.778 | 0.0755 | . |
| Site: UW (vs UAB) | -0.2199 | 0.2912 | ±0.5824 | -0.755 | 0.4501 |  |
| **Age (years)** | **-0.0518** | 0.0101 | ±0.0202 | **-5.132** | **2.87e-07** | *** |
| BMI (kg/m2) | -0.0229 | 0.0160 | ±0.0321 | -1.430 | 0.1527 |  |
| Hypertension | -0.2422 | 0.2390 | ±0.4780 | -1.013 | 0.3109 |  |
| High cholesterol | +0.1627 | 0.2190 | ±0.4380 | +0.743 | 0.4575 |  |
| Kidney disease | -0.0198 | 0.4408 | ±0.8816 | -0.045 | 0.9642 |  |
| Circulatory disease | -0.5672 | 0.3703 | ±0.7405 | -1.532 | 0.1256 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0165 | 0.0098 | ±0.0197 | -1.677 | 0.0935 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, R² = **0.1199**, Adj R² = **0.1056**, F-statistic = **8.34** (p = **7.87e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.1**, BIC = **3355.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.5002** | 0.9558 | ±1.9116 | **+31.910** | **1.92e-223** | *** |
| **Education: graduate level (vs college)** | **+0.6477** | 0.2100 | ±0.4201 | **+3.084** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **-1.6357** | 0.5056 | ±1.0113 | **-3.235** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5346 | 0.2962 | ±0.5925 | -1.805 | 0.0711 | . |
| Site: UW (vs UAB) | -0.2489 | 0.2892 | ±0.5783 | -0.861 | 0.3894 |  |
| **Age (years)** | **-0.0505** | 0.0102 | ±0.0204 | **-4.940** | **7.82e-07** | *** |
| BMI (kg/m2) | -0.0295 | 0.0152 | ±0.0304 | -1.942 | 0.0521 | . |
| Hypertension | -0.2487 | 0.2390 | ±0.4779 | -1.041 | 0.2981 |  |
| High cholesterol | +0.1480 | 0.2177 | ±0.4354 | +0.680 | 0.4966 |  |
| Kidney disease | -0.0292 | 0.4440 | ±0.8879 | -0.066 | 0.9475 |  |
| Circulatory disease | -0.6001 | 0.3747 | ±0.7495 | -1.601 | 0.1093 |  |
| Glucose SD, pooled (mg/dL) | -0.0167 | 0.0284 | ±0.0569 | -0.587 | 0.5570 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, R² = **0.1199**, Adj R² = **0.1056**, F-statistic = **8.34** (p = **7.86e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.1**, BIC = **3355.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4754** | 0.9443 | ±1.8885 | **+32.274** | **1.62e-228** | *** |
| **Education: graduate level (vs college)** | **+0.6503** | 0.2102 | ±0.4204 | **+3.094** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **-1.6350** | 0.5058 | ±1.0115 | **-3.233** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5362 | 0.2965 | ±0.5930 | -1.808 | 0.0706 | . |
| Site: UW (vs UAB) | -0.2491 | 0.2889 | ±0.5778 | -0.862 | 0.3885 |  |
| **Age (years)** | **-0.0505** | 0.0102 | ±0.0204 | **-4.951** | **7.37e-07** | *** |
| BMI (kg/m2) | -0.0294 | 0.0152 | ±0.0304 | -1.932 | 0.0533 | . |
| Hypertension | -0.2496 | 0.2392 | ±0.4783 | -1.044 | 0.2966 |  |
| High cholesterol | +0.1470 | 0.2177 | ±0.4354 | +0.675 | 0.4996 |  |
| Kidney disease | -0.0269 | 0.4435 | ±0.8869 | -0.061 | 0.9516 |  |
| Circulatory disease | -0.5989 | 0.3745 | ±0.7490 | -1.599 | 0.1098 |  |
| Avg. daily SD (mg/dL) | -0.0170 | 0.0284 | ±0.0569 | -0.597 | 0.5505 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, R² = **0.1201**, Adj R² = **0.1057**, F-statistic = **8.35** (p = **7.42e-14**), Residual SE = **2.669** on **673** df, AIC = **3300.9**, BIC = **3355.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8271** | 1.0502 | ±2.1004 | **+28.401** | **1.97e-177** | *** |
| **Education: graduate level (vs college)** | **+0.6683** | 0.2093 | ±0.4186 | **+3.193** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.6433** | 0.5070 | ±1.0140 | **-3.241** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5161 | 0.2973 | ±0.5946 | -1.736 | 0.0826 | . |
| Site: UW (vs UAB) | -0.2605 | 0.2883 | ±0.5767 | -0.903 | 0.3663 |  |
| **Age (years)** | **-0.0517** | 0.0102 | ±0.0204 | **-5.063** | **4.12e-07** | *** |
| **BMI (kg/m2)** | **-0.0298** | 0.0149 | ±0.0299 | **-1.995** | **0.0460** | * |
| Hypertension | -0.2627 | 0.2390 | ±0.4779 | -1.099 | 0.2717 |  |
| High cholesterol | +0.1459 | 0.2173 | ±0.4347 | +0.671 | 0.5020 |  |
| Kidney disease | -0.0414 | 0.4465 | ±0.8931 | -0.093 | 0.9262 |  |
| Circulatory disease | -0.5878 | 0.3764 | ±0.7527 | -1.562 | 0.1183 |  |
| CV (%) | +0.0264 | 0.0400 | ±0.0800 | +0.660 | 0.5095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, R² = **0.1211**, Adj R² = **0.1068**, F-statistic = **8.43** (p = **5.21e-14**), Residual SE = **2.668** on **673** df, AIC = **3300.1**, BIC = **3354.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.9220** | 1.0928 | ±2.1857 | **+28.295** | **3.93e-176** | *** |
| **Education: graduate level (vs college)** | **+0.6782** | 0.2084 | ±0.4168 | **+3.254** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **-1.6472** | 0.5077 | ±1.0154 | **-3.244** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5157 | 0.2969 | ±0.5937 | -1.737 | 0.0824 | . |
| Site: UW (vs UAB) | -0.2669 | 0.2873 | ±0.5746 | -0.929 | 0.3529 |  |
| **Age (years)** | **-0.0519** | 0.0102 | ±0.0203 | **-5.101** | **3.37e-07** | *** |
| **BMI (kg/m2)** | **-0.0297** | 0.0149 | ±0.0298 | **-1.997** | **0.0458** | * |
| Hypertension | -0.2672 | 0.2389 | ±0.4777 | -1.119 | 0.2633 |  |
| High cholesterol | +0.1472 | 0.2174 | ±0.4348 | +0.677 | 0.4984 |  |
| Kidney disease | -0.0449 | 0.4471 | ±0.8942 | -0.100 | 0.9201 |  |
| Circulatory disease | -0.5814 | 0.3767 | ±0.7533 | -1.544 | 0.1227 |  |
| Mean / SD ratio | -0.1032 | 0.1011 | ±0.2022 | -1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, R² = **0.1207**, Adj R² = **0.1063**, F-statistic = **8.40** (p = **6.00e-14**), Residual SE = **2.668** on **673** df, AIC = **3300.4**, BIC = **3354.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.8032** | 1.0572 | ±2.1143 | **+29.137** | **1.21e-186** | *** |
| **Education: graduate level (vs college)** | **+0.6702** | 0.2090 | ±0.4180 | **+3.207** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.6477** | 0.5074 | ±1.0148 | **-3.247** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5146 | 0.2972 | ±0.5945 | -1.731 | 0.0834 | . |
| Site: UW (vs UAB) | -0.2670 | 0.2875 | ±0.5750 | -0.929 | 0.3531 |  |
| **Age (years)** | **-0.0518** | 0.0102 | ±0.0203 | **-5.100** | **3.40e-07** | *** |
| **BMI (kg/m2)** | **-0.0303** | 0.0149 | ±0.0299 | **-2.026** | **0.0427** | * |
| Hypertension | -0.2606 | 0.2391 | ±0.4782 | -1.090 | 0.2758 |  |
| High cholesterol | +0.1497 | 0.2177 | ±0.4354 | +0.688 | 0.4917 |  |
| Kidney disease | -0.0471 | 0.4464 | ±0.8928 | -0.105 | 0.9160 |  |
| Circulatory disease | -0.5849 | 0.3774 | ±0.7547 | -1.550 | 0.1211 |  |
| Avg. daily mean/SD | -0.0727 | 0.0785 | ±0.1571 | -0.925 | 0.3548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, R² = **0.1195**, Adj R² = **0.1051**, F-statistic = **8.30** (p = **9.21e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.4**, BIC = **3355.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3056** | 0.9768 | ±1.9536 | **+31.026** | **2.43e-211** | *** |
| **Education: graduate level (vs college)** | **+0.6538** | 0.2099 | ±0.4198 | **+3.115** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.6375** | 0.5059 | ±1.0118 | **-3.237** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5260 | 0.2966 | ±0.5933 | -1.773 | 0.0762 | . |
| Site: UW (vs UAB) | -0.2573 | 0.2891 | ±0.5783 | -0.890 | 0.3734 |  |
| **Age (years)** | **-0.0511** | 0.0101 | ±0.0203 | **-5.046** | **4.50e-07** | *** |
| **BMI (kg/m2)** | **-0.0300** | 0.0150 | ±0.0301 | **-1.994** | **0.0462** | * |
| Hypertension | -0.2580 | 0.2390 | ±0.4780 | -1.079 | 0.2804 |  |
| High cholesterol | +0.1464 | 0.2176 | ±0.4351 | +0.673 | 0.5009 |  |
| Kidney disease | -0.0348 | 0.4469 | ±0.8938 | -0.078 | 0.9379 |  |
| Circulatory disease | -0.5989 | 0.3755 | ±0.7510 | -1.595 | 0.1107 |  |
| MAG (mg/dL/h) | -0.0021 | 0.0135 | ±0.0269 | -0.155 | 0.8768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, R² = **0.1197**, Adj R² = **0.1054**, F-statistic = **8.32** (p = **8.42e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.2**, BIC = **3355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4752** | 0.9959 | ±1.9917 | **+30.602** | **1.16e-205** | *** |
| **Education: graduate level (vs college)** | **+0.6543** | 0.2101 | ±0.4202 | **+3.114** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.6332** | 0.5050 | ±1.0100 | **-3.234** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5299 | 0.2968 | ±0.5935 | -1.786 | 0.0742 | . |
| Site: UW (vs UAB) | -0.2512 | 0.2885 | ±0.5771 | -0.871 | 0.3839 |  |
| **Age (years)** | **-0.0507** | 0.0102 | ±0.0203 | **-4.990** | **6.05e-07** | *** |
| **BMI (kg/m2)** | **-0.0302** | 0.0151 | ±0.0301 | **-2.008** | **0.0447** | * |
| Hypertension | -0.2547 | 0.2393 | ±0.4786 | -1.064 | 0.2872 |  |
| High cholesterol | +0.1452 | 0.2178 | ±0.4357 | +0.666 | 0.5052 |  |
| Kidney disease | -0.0289 | 0.4437 | ±0.8873 | -0.065 | 0.9480 |  |
| Circulatory disease | -0.5964 | 0.3752 | ±0.7504 | -1.589 | 0.1120 |  |
| Avg. daily range (mg/dL) | -0.0030 | 0.0062 | ±0.0124 | -0.477 | 0.6332 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, R² = **0.1208**, Adj R² = **0.1064**, F-statistic = **8.41** (p = **5.87e-14**), Residual SE = **2.668** on **673** df, AIC = **3300.4**, BIC = **3354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4443** | 0.8835 | ±1.7670 | **+34.459** | **3.33e-260** | *** |
| **Education: graduate level (vs college)** | **+0.6509** | 0.2095 | ±0.4190 | **+3.107** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **-1.6379** | 0.5041 | ±1.0081 | **-3.249** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5285 | 0.2962 | ±0.5923 | -1.785 | 0.0743 | . |
| Site: UW (vs UAB) | -0.2505 | 0.2896 | ±0.5793 | -0.865 | 0.3871 |  |
| **Age (years)** | **-0.0511** | 0.0101 | ±0.0202 | **-5.048** | **4.47e-07** | *** |
| BMI (kg/m2) | -0.0284 | 0.0153 | ±0.0306 | -1.852 | 0.0641 | . |
| Hypertension | -0.2597 | 0.2393 | ±0.4786 | -1.085 | 0.2778 |  |
| High cholesterol | +0.1625 | 0.2175 | ±0.4351 | +0.747 | 0.4551 |  |
| Kidney disease | -0.0502 | 0.4438 | ±0.8876 | -0.113 | 0.9100 |  |
| Circulatory disease | -0.5952 | 0.3759 | ±0.7518 | -1.583 | 0.1134 |  |
| SD of daily means (mg/dL) | -0.0462 | 0.0482 | ±0.0965 | -0.957 | 0.3383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, R² = **0.1242**, Adj R² = **0.1098**, F-statistic = **8.67** (p = **1.81e-14**), Residual SE = **2.663** on **673** df, AIC = **3297.8**, BIC = **3352.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9435** | 5.6580 | ±11.3160 | **+4.055** | **5.01e-05** | *** |
| **Education: graduate level (vs college)** | **+0.6570** | 0.2098 | ±0.4195 | **+3.132** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.6435** | 0.5028 | ±1.0055 | **-3.269** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5554 | 0.2922 | ±0.5844 | -1.901 | 0.0573 | . |
| Site: UW (vs UAB) | -0.2385 | 0.2895 | ±0.5790 | -0.824 | 0.4101 |  |
| **Age (years)** | **-0.0499** | 0.0102 | ±0.0204 | **-4.900** | **9.58e-07** | *** |
| BMI (kg/m2) | -0.0287 | 0.0153 | ±0.0306 | -1.876 | 0.0607 | . |
| Hypertension | -0.2497 | 0.2388 | ±0.4776 | -1.046 | 0.2957 |  |
| High cholesterol | +0.1685 | 0.2204 | ±0.4407 | +0.764 | 0.4446 |  |
| Kidney disease | -0.0156 | 0.4365 | ±0.8729 | -0.036 | 0.9715 |  |
| Circulatory disease | -0.5716 | 0.3757 | ±0.7515 | -1.521 | 0.1282 |  |
| Time in range 70-180, pooled (%) | +0.0730 | 0.0551 | ±0.1102 | +1.326 | 0.1849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, R² = **0.1247**, Adj R² = **0.1104**, F-statistic = **8.72** (p = **1.50e-14**), Residual SE = **2.662** on **673** df, AIC = **3297.3**, BIC = **3351.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.3538** | 5.7280 | ±11.4560 | **+3.903** | **9.52e-05** | *** |
| **Education: graduate level (vs college)** | **+0.6578** | 0.2097 | ±0.4193 | **+3.137** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.6471** | 0.5026 | ±1.0051 | **-3.277** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.5577 | 0.2921 | ±0.5842 | -1.909 | 0.0562 | . |
| Site: UW (vs UAB) | -0.2401 | 0.2890 | ±0.5780 | -0.831 | 0.4061 |  |
| **Age (years)** | **-0.0500** | 0.0102 | ±0.0203 | **-4.915** | **8.88e-07** | *** |
| BMI (kg/m2) | -0.0283 | 0.0154 | ±0.0308 | -1.837 | 0.0662 | . |
| Hypertension | -0.2522 | 0.2386 | ±0.4771 | -1.057 | 0.2904 |  |
| High cholesterol | +0.1703 | 0.2202 | ±0.4404 | +0.773 | 0.4393 |  |
| Kidney disease | -0.0111 | 0.4344 | ±0.8687 | -0.026 | 0.9796 |  |
| Circulatory disease | -0.5653 | 0.3767 | ±0.7535 | -1.500 | 0.1335 |  |
| Avg. daily time in range 70-180 (%) | +0.0789 | 0.0558 | ±0.1115 | +1.414 | 0.1572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, R² = **0.1200**, Adj R² = **0.1056**, F-statistic = **8.34** (p = **7.80e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.0**, BIC = **3355.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1860** | 0.8708 | ±1.7416 | **+34.664** | **2.75e-263** | *** |
| **Education: graduate level (vs college)** | **+0.6686** | 0.2110 | ±0.4221 | **+3.169** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.6235** | 0.5076 | ±1.0151 | **-3.199** | **0.0014** | ** |
| Site: UCSD (vs UAB) | -0.5304 | 0.2966 | ±0.5932 | -1.788 | 0.0737 | . |
| Site: UW (vs UAB) | -0.2531 | 0.2894 | ±0.5788 | -0.875 | 0.3818 |  |
| **Age (years)** | **-0.0510** | 0.0101 | ±0.0202 | **-5.040** | **4.65e-07** | *** |
| **BMI (kg/m2)** | **-0.0298** | 0.0150 | ±0.0300 | **-1.983** | **0.0473** | * |
| Hypertension | -0.2580 | 0.2392 | ±0.4785 | -1.078 | 0.2809 |  |
| High cholesterol | +0.1430 | 0.2174 | ±0.4348 | +0.658 | 0.5107 |  |
| Kidney disease | -0.0336 | 0.4460 | ±0.8920 | -0.075 | 0.9400 |  |
| Circulatory disease | -0.5896 | 0.3751 | ±0.7502 | -1.572 | 0.1160 |  |
| Time 54-69, pooled (%) | +0.1228 | 0.1606 | ±0.3213 | +0.765 | 0.4445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, R² = **0.1199**, Adj R² = **0.1055**, F-statistic = **8.33** (p = **8.10e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.1**, BIC = **3355.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1952** | 0.8692 | ±1.7385 | **+34.738** | **2.11e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6673** | 0.2110 | ±0.4220 | **+3.163** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.6246** | 0.5071 | ±1.0143 | **-3.203** | **0.0014** | ** |
| Site: UCSD (vs UAB) | -0.5321 | 0.2966 | ±0.5931 | -1.794 | 0.0728 | . |
| Site: UW (vs UAB) | -0.2543 | 0.2893 | ±0.5787 | -0.879 | 0.3795 |  |
| **Age (years)** | **-0.0511** | 0.0101 | ±0.0202 | **-5.046** | **4.52e-07** | *** |
| **BMI (kg/m2)** | **-0.0298** | 0.0150 | ±0.0300 | **-1.983** | **0.0473** | * |
| Hypertension | -0.2574 | 0.2392 | ±0.4785 | -1.076 | 0.2821 |  |
| High cholesterol | +0.1439 | 0.2174 | ±0.4348 | +0.662 | 0.5080 |  |
| Kidney disease | -0.0344 | 0.4461 | ±0.8922 | -0.077 | 0.9385 |  |
| Circulatory disease | -0.5889 | 0.3749 | ±0.7498 | -1.571 | 0.1162 |  |
| Avg. daily time 54-69 (%) | +0.1052 | 0.1568 | ±0.3135 | +0.671 | 0.5020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, R² = **0.1200**, Adj R² = **0.1056**, F-statistic = **8.34** (p = **7.80e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.0**, BIC = **3355.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1860** | 0.8708 | ±1.7416 | **+34.664** | **2.75e-263** | *** |
| **Education: graduate level (vs college)** | **+0.6686** | 0.2110 | ±0.4221 | **+3.169** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.6235** | 0.5076 | ±1.0151 | **-3.199** | **0.0014** | ** |
| Site: UCSD (vs UAB) | -0.5304 | 0.2966 | ±0.5932 | -1.788 | 0.0737 | . |
| Site: UW (vs UAB) | -0.2531 | 0.2894 | ±0.5788 | -0.875 | 0.3818 |  |
| **Age (years)** | **-0.0510** | 0.0101 | ±0.0202 | **-5.040** | **4.65e-07** | *** |
| **BMI (kg/m2)** | **-0.0298** | 0.0150 | ±0.0300 | **-1.983** | **0.0473** | * |
| Hypertension | -0.2580 | 0.2392 | ±0.4785 | -1.078 | 0.2809 |  |
| High cholesterol | +0.1430 | 0.2174 | ±0.4348 | +0.658 | 0.5107 |  |
| Kidney disease | -0.0336 | 0.4460 | ±0.8920 | -0.075 | 0.9400 |  |
| Circulatory disease | -0.5896 | 0.3751 | ±0.7502 | -1.572 | 0.1160 |  |
| Time < 70 (%) | +0.1228 | 0.1606 | ±0.3213 | +0.765 | 0.4445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, R² = **0.1199**, Adj R² = **0.1055**, F-statistic = **8.33** (p = **8.10e-14**), Residual SE = **2.670** on **673** df, AIC = **3301.1**, BIC = **3355.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1952** | 0.8692 | ±1.7385 | **+34.738** | **2.11e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6673** | 0.2110 | ±0.4220 | **+3.163** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.6246** | 0.5071 | ±1.0143 | **-3.203** | **0.0014** | ** |
| Site: UCSD (vs UAB) | -0.5321 | 0.2966 | ±0.5931 | -1.794 | 0.0728 | . |
| Site: UW (vs UAB) | -0.2543 | 0.2893 | ±0.5787 | -0.879 | 0.3795 |  |
| **Age (years)** | **-0.0511** | 0.0101 | ±0.0202 | **-5.046** | **4.52e-07** | *** |
| **BMI (kg/m2)** | **-0.0298** | 0.0150 | ±0.0300 | **-1.983** | **0.0473** | * |
| Hypertension | -0.2574 | 0.2392 | ±0.4785 | -1.076 | 0.2821 |  |
| High cholesterol | +0.1439 | 0.2174 | ±0.4348 | +0.662 | 0.5080 |  |
| Kidney disease | -0.0344 | 0.4461 | ±0.8922 | -0.077 | 0.9385 |  |
| Circulatory disease | -0.5889 | 0.3749 | ±0.7498 | -1.571 | 0.1162 |  |
| Avg. daily time < 70 (%) | +0.1052 | 0.1568 | ±0.3135 | +0.671 | 0.5020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, R² = **0.1247**, Adj R² = **0.1104**, F-statistic = **8.72** (p = **1.49e-14**), Residual SE = **2.662** on **673** df, AIC = **3297.3**, BIC = **3351.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2229** | 0.8699 | ±1.7398 | **+34.743** | **1.78e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6664** | 0.2093 | ±0.4185 | **+3.184** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.6326** | 0.5026 | ±1.0053 | **-3.248** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5603 | 0.2918 | ±0.5836 | -1.920 | 0.0549 | . |
| Site: UW (vs UAB) | -0.2351 | 0.2897 | ±0.5793 | -0.812 | 0.4170 |  |
| **Age (years)** | **-0.0498** | 0.0102 | ±0.0204 | **-4.889** | **1.01e-06** | *** |
| BMI (kg/m2) | -0.0285 | 0.0153 | ±0.0306 | -1.865 | 0.0622 | . |
| Hypertension | -0.2502 | 0.2389 | ±0.4777 | -1.048 | 0.2949 |  |
| High cholesterol | +0.1672 | 0.2201 | ±0.4402 | +0.760 | 0.4475 |  |
| Kidney disease | -0.0124 | 0.4361 | ±0.8722 | -0.028 | 0.9773 |  |
| Circulatory disease | -0.5650 | 0.3756 | ±0.7511 | -1.504 | 0.1325 |  |
| Time 181-250, pooled (%) | -0.0768 | 0.0550 | ±0.1099 | -1.398 | 0.1622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, R² = **0.1253**, Adj R² = **0.1110**, F-statistic = **8.76** (p = **1.24e-14**), Residual SE = **2.661** on **673** df, AIC = **3296.9**, BIC = **3351.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2172** | 0.8707 | ±1.7415 | **+34.703** | **7.16e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6685** | 0.2092 | ±0.4183 | **+3.196** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.6345** | 0.5024 | ±1.0049 | **-3.253** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5647 | 0.2916 | ±0.5832 | -1.937 | 0.0528 | . |
| Site: UW (vs UAB) | -0.2373 | 0.2892 | ±0.5784 | -0.820 | 0.4120 |  |
| **Age (years)** | **-0.0499** | 0.0102 | ±0.0203 | **-4.910** | **9.13e-07** | *** |
| BMI (kg/m2) | -0.0281 | 0.0154 | ±0.0308 | -1.824 | 0.0682 | . |
| Hypertension | -0.2526 | 0.2386 | ±0.4772 | -1.058 | 0.2899 |  |
| High cholesterol | +0.1691 | 0.2200 | ±0.4400 | +0.769 | 0.4422 |  |
| Kidney disease | -0.0080 | 0.4341 | ±0.8682 | -0.018 | 0.9853 |  |
| Circulatory disease | -0.5566 | 0.3767 | ±0.7533 | -1.478 | 0.1395 |  |
| Avg. daily time 181-250 (%) | -0.0825 | 0.0557 | ±0.1114 | -1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, R² = **0.1247**, Adj R² = **0.1104**, F-statistic = **8.72** (p = **1.49e-14**), Residual SE = **2.662** on **673** df, AIC = **3297.3**, BIC = **3351.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2229** | 0.8699 | ±1.7398 | **+34.743** | **1.78e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6664** | 0.2093 | ±0.4185 | **+3.184** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.6326** | 0.5026 | ±1.0053 | **-3.248** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5603 | 0.2918 | ±0.5836 | -1.920 | 0.0549 | . |
| Site: UW (vs UAB) | -0.2351 | 0.2897 | ±0.5793 | -0.812 | 0.4170 |  |
| **Age (years)** | **-0.0498** | 0.0102 | ±0.0204 | **-4.889** | **1.01e-06** | *** |
| BMI (kg/m2) | -0.0285 | 0.0153 | ±0.0306 | -1.865 | 0.0622 | . |
| Hypertension | -0.2502 | 0.2389 | ±0.4777 | -1.048 | 0.2949 |  |
| High cholesterol | +0.1672 | 0.2201 | ±0.4402 | +0.760 | 0.4475 |  |
| Kidney disease | -0.0124 | 0.4361 | ±0.8722 | -0.028 | 0.9773 |  |
| Circulatory disease | -0.5650 | 0.3756 | ±0.7511 | -1.504 | 0.1325 |  |
| Time > 180 (%) | -0.0768 | 0.0550 | ±0.1099 | -1.398 | 0.1622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, R² = **0.1253**, Adj R² = **0.1110**, F-statistic = **8.76** (p = **1.24e-14**), Residual SE = **2.661** on **673** df, AIC = **3296.9**, BIC = **3351.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2172** | 0.8707 | ±1.7415 | **+34.703** | **7.16e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6685** | 0.2092 | ±0.4183 | **+3.196** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.6345** | 0.5024 | ±1.0049 | **-3.253** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.5647 | 0.2916 | ±0.5832 | -1.937 | 0.0528 | . |
| Site: UW (vs UAB) | -0.2373 | 0.2892 | ±0.5784 | -0.820 | 0.4120 |  |
| **Age (years)** | **-0.0499** | 0.0102 | ±0.0203 | **-4.910** | **9.13e-07** | *** |
| BMI (kg/m2) | -0.0281 | 0.0154 | ±0.0308 | -1.824 | 0.0682 | . |
| Hypertension | -0.2526 | 0.2386 | ±0.4772 | -1.058 | 0.2899 |  |
| High cholesterol | +0.1691 | 0.2200 | ±0.4400 | +0.769 | 0.4422 |  |
| Kidney disease | -0.0080 | 0.4341 | ±0.8682 | -0.018 | 0.9853 |  |
| Circulatory disease | -0.5566 | 0.3767 | ±0.7533 | -1.478 | 0.1395 |  |
| Avg. daily time > 180 (%) | -0.0825 | 0.0557 | ±0.1114 | -1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, R² = **0.1213**, Adj R² = **0.1069**, F-statistic = **8.44** (p = **4.96e-14**), Residual SE = **2.668** on **673** df, AIC = **3300.0**, BIC = **3354.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2111** | 0.8704 | ±1.7408 | **+34.710** | **5.65e-264** | *** |
| **Education: graduate level (vs college)** | **+0.6511** | 0.2103 | ±0.4206 | **+3.096** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **-1.6277** | 0.5009 | ±1.0017 | **-3.250** | **0.0012** | ** |
| Site: UCSD (vs UAB) | -0.5358 | 0.2958 | ±0.5915 | -1.811 | 0.0701 | . |
| Site: UW (vs UAB) | -0.2469 | 0.2898 | ±0.5796 | -0.852 | 0.3943 |  |
| **Age (years)** | **-0.0514** | 0.0101 | ±0.0202 | **-5.090** | **3.58e-07** | *** |
| BMI (kg/m2) | -0.0276 | 0.0152 | ±0.0305 | -1.810 | 0.0703 | . |
| Hypertension | -0.2641 | 0.2386 | ±0.4772 | -1.107 | 0.2685 |  |
| High cholesterol | +0.1728 | 0.2213 | ±0.4426 | +0.781 | 0.4349 |  |
| Kidney disease | -0.0400 | 0.4443 | ±0.8886 | -0.090 | 0.9282 |  |
| Circulatory disease | -0.5986 | 0.3728 | ±0.7455 | -1.606 | 0.1083 |  |
| Nocturnal time > 180 (%) | -0.0399 | 0.0424 | ±0.0848 | -0.940 | 0.3471 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 685; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0675**, LLR χ² = **60.03** (p = **3.58e-09**), AUC = **0.6738**, AIC = **851.7**, BIC = **901.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4477** | 0.7027 | ±1.4054 | **-4.907** | **9.27e-07** | 0.0318 | *** |
| **Education: graduate level (vs college)** | **-0.5434** | 0.1807 | ±0.3614 | **-3.007** | **0.0026** | 0.5808 | ** |
| **Education: high school or below (vs college)** | **+0.9318** | 0.2970 | ±0.5941 | **+3.137** | **0.0017** | 2.5392 | ** |
| Site: UCSD (vs UAB) | +0.4027 | 0.2244 | ±0.4488 | +1.795 | 0.0727 | 1.4959 | . |
| Site: UW (vs UAB) | +0.2115 | 0.2230 | ±0.4461 | +0.948 | 0.3431 | 1.2355 |  |
| **Age (years)** | **+0.0306** | 0.0078 | ±0.0156 | **+3.910** | **9.23e-05** | 1.0311 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0133 | ±0.0266 | **+2.107** | **0.0351** | 1.0284 | * |
| Hypertension | +0.2286 | 0.1852 | ±0.3705 | +1.234 | 0.2170 | 1.2569 |  |
| High cholesterol | +0.0148 | 0.1748 | ±0.3495 | +0.085 | 0.9324 | 1.0149 |  |
| Kidney disease | -0.3314 | 0.3340 | ±0.6681 | -0.992 | 0.3212 | 0.7179 |  |
| Circulatory disease | +0.2714 | 0.2597 | ±0.5193 | +1.045 | 0.2959 | 1.3118 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0688**, LLR χ² = **61.20** (p = **5.55e-09**), AUC = **0.6749**, AIC = **852.6**, BIC = **906.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.8920** | 1.5154 | ±3.0307 | **-3.228** | **0.0012** | 0.0075 | ** |
| **Education: graduate level (vs college)** | **-0.5520** | 0.1811 | ±0.3621 | **-3.049** | **0.0023** | 0.5758 | ** |
| **Education: high school or below (vs college)** | **+0.9309** | 0.2976 | ±0.5951 | **+3.128** | **0.0018** | 2.5368 | ** |
| Site: UCSD (vs UAB) | +0.4049 | 0.2245 | ±0.4490 | +1.803 | 0.0714 | 1.4991 | . |
| Site: UW (vs UAB) | +0.2103 | 0.2235 | ±0.4470 | +0.941 | 0.3467 | 1.2341 |  |
| **Age (years)** | **+0.0297** | 0.0079 | ±0.0157 | **+3.776** | **1.59e-04** | 1.0302 | *** |
| BMI (kg/m2) | +0.0260 | 0.0133 | ±0.0267 | +1.952 | 0.0510 | 1.0264 | . |
| Hypertension | +0.2142 | 0.1857 | ±0.3714 | +1.153 | 0.2488 | 1.2389 |  |
| High cholesterol | -0.0030 | 0.1757 | ±0.3513 | -0.017 | 0.9862 | 0.9970 |  |
| Kidney disease | -0.3259 | 0.3335 | ±0.6671 | -0.977 | 0.3286 | 0.7219 |  |
| Circulatory disease | +0.2779 | 0.2600 | ±0.5201 | +1.069 | 0.2853 | 1.3203 |  |
| HbA1c (%) | +0.2810 | 0.2603 | ±0.5206 | +1.079 | 0.2804 | 1.3244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0729**, LLR χ² = **64.90** (p = **1.13e-09**), AUC = **0.6812**, AIC = **848.9**, BIC = **903.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.2928** | 1.1004 | ±2.2007 | **-4.810** | **1.51e-06** | 0.0050 | *** |
| **Education: graduate level (vs college)** | **-0.5754** | 0.1822 | ±0.3643 | **-3.159** | **0.0016** | 0.5625 | ** |
| **Education: high school or below (vs college)** | **+0.9176** | 0.2976 | ±0.5952 | **+3.083** | **0.0020** | 2.5033 | ** |
| Site: UCSD (vs UAB) | +0.4282 | 0.2254 | ±0.4509 | +1.899 | 0.0575 | 1.5345 | . |
| Site: UW (vs UAB) | +0.1784 | 0.2244 | ±0.4488 | +0.795 | 0.4267 | 1.1952 |  |
| **Age (years)** | **+0.0298** | 0.0078 | ±0.0157 | **+3.802** | **1.43e-04** | 1.0303 | *** |
| BMI (kg/m2) | +0.0249 | 0.0133 | ±0.0267 | +1.866 | 0.0620 | 1.0252 | . |
| Hypertension | +0.2065 | 0.1861 | ±0.3722 | +1.110 | 0.2671 | 1.2294 |  |
| High cholesterol | +0.0212 | 0.1752 | ±0.3504 | +0.121 | 0.9036 | 1.0215 |  |
| Kidney disease | -0.3651 | 0.3350 | ±0.6700 | -1.090 | 0.2758 | 0.6941 |  |
| Circulatory disease | +0.2358 | 0.2617 | ±0.5234 | +0.901 | 0.3676 | 1.2660 |  |
| **Mean glucose (mg/dL)** | **+0.0169** | 0.0076 | ±0.0153 | **+2.206** | **0.0274** | 1.0170 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0729**, LLR χ² = **64.90** (p = **1.13e-09**), AUC = **0.6812**, AIC = **848.9**, BIC = **903.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-7.6245** | 2.0298 | ±4.0596 | **-3.756** | **1.72e-04** | 0.0005 | *** |
| **Education: graduate level (vs college)** | **-0.5754** | 0.1822 | ±0.3643 | **-3.159** | **0.0016** | 0.5625 | ** |
| **Education: high school or below (vs college)** | **+0.9176** | 0.2976 | ±0.5952 | **+3.083** | **0.0020** | 2.5033 | ** |
| Site: UCSD (vs UAB) | +0.4282 | 0.2254 | ±0.4509 | +1.899 | 0.0575 | 1.5345 | . |
| Site: UW (vs UAB) | +0.1784 | 0.2244 | ±0.4488 | +0.795 | 0.4267 | 1.1952 |  |
| **Age (years)** | **+0.0298** | 0.0078 | ±0.0157 | **+3.802** | **1.43e-04** | 1.0303 | *** |
| BMI (kg/m2) | +0.0249 | 0.0133 | ±0.0267 | +1.866 | 0.0620 | 1.0252 | . |
| Hypertension | +0.2065 | 0.1861 | ±0.3722 | +1.110 | 0.2671 | 1.2294 |  |
| High cholesterol | +0.0212 | 0.1752 | ±0.3504 | +0.121 | 0.9036 | 1.0215 |  |
| Kidney disease | -0.3651 | 0.3350 | ±0.6700 | -1.090 | 0.2758 | 0.6941 |  |
| Circulatory disease | +0.2358 | 0.2617 | ±0.5234 | +0.901 | 0.3676 | 1.2660 |  |
| **GMI (%)** | **+0.7044** | 0.3193 | ±0.6386 | **+2.206** | **0.0274** | 2.0227 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0715**, LLR χ² = **63.62** (p = **1.96e-09**), AUC = **0.6813**, AIC = **850.1**, BIC = **904.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.8323** | 1.0187 | ±2.0374 | **-4.744** | **2.10e-06** | 0.0080 | *** |
| **Education: graduate level (vs college)** | **-0.5629** | 0.1815 | ±0.3630 | **-3.101** | **0.0019** | 0.5696 | ** |
| **Education: high school or below (vs college)** | **+0.9249** | 0.2977 | ±0.5954 | **+3.107** | **0.0019** | 2.5215 | ** |
| Site: UCSD (vs UAB) | +0.4078 | 0.2248 | ±0.4495 | +1.815 | 0.0696 | 1.5036 | . |
| Site: UW (vs UAB) | +0.1833 | 0.2241 | ±0.4481 | +0.818 | 0.4134 | 1.2011 |  |
| **Age (years)** | **+0.0313** | 0.0078 | ±0.0157 | **+3.987** | **6.68e-05** | 1.0318 | *** |
| BMI (kg/m2) | +0.0225 | 0.0135 | ±0.0269 | +1.673 | 0.0943 | 1.0228 | . |
| Hypertension | +0.2213 | 0.1856 | ±0.3713 | +1.192 | 0.2332 | 1.2477 |  |
| High cholesterol | +0.0053 | 0.1751 | ±0.3502 | +0.030 | 0.9757 | 1.0053 |  |
| Kidney disease | -0.3464 | 0.3346 | ±0.6692 | -1.035 | 0.3006 | 0.7072 |  |
| Circulatory disease | +0.2491 | 0.2610 | ±0.5220 | +0.954 | 0.3399 | 1.2829 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0128 | 0.0068 | ±0.0135 | +1.896 | 0.0580 | 1.0129 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0680**, LLR χ² = **60.51** (p = **7.44e-09**), AUC = **0.6736**, AIC = **853.2**, BIC = **907.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6995** | 0.7905 | ±1.5809 | **-4.680** | **2.87e-06** | 0.0247 | *** |
| **Education: graduate level (vs college)** | **-0.5386** | 0.1809 | ±0.3618 | **-2.978** | **0.0029** | 0.5835 | ** |
| **Education: high school or below (vs college)** | **+0.9270** | 0.2971 | ±0.5942 | **+3.120** | **0.0018** | 2.5269 | ** |
| Site: UCSD (vs UAB) | +0.4125 | 0.2249 | ±0.4499 | +1.834 | 0.0667 | 1.5106 | . |
| Site: UW (vs UAB) | +0.2039 | 0.2235 | ±0.4469 | +0.913 | 0.3615 | 1.2262 |  |
| **Age (years)** | **+0.0300** | 0.0079 | ±0.0157 | **+3.816** | **1.36e-04** | 1.0305 | *** |
| **BMI (kg/m2)** | **+0.0275** | 0.0133 | ±0.0266 | **+2.070** | **0.0385** | 1.0279 | * |
| Hypertension | +0.2217 | 0.1856 | ±0.3711 | +1.195 | 0.2322 | 1.2482 |  |
| High cholesterol | +0.0151 | 0.1748 | ±0.3496 | +0.086 | 0.9313 | 1.0152 |  |
| Kidney disease | -0.3395 | 0.3340 | ±0.6681 | -1.016 | 0.3095 | 0.7121 |  |
| Circulatory disease | +0.2728 | 0.2600 | ±0.5201 | +1.049 | 0.2941 | 1.3137 |  |
| Glucose SD, pooled (mg/dL) | +0.0157 | 0.0226 | ±0.0452 | +0.696 | 0.4865 | 1.0159 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0681**, LLR χ² = **60.55** (p = **7.32e-09**), AUC = **0.6736**, AIC = **853.2**, BIC = **907.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6821** | 0.7738 | ±1.5477 | **-4.758** | **1.95e-06** | 0.0252 | *** |
| **Education: graduate level (vs college)** | **-0.5410** | 0.1808 | ±0.3616 | **-2.992** | **0.0028** | 0.5822 | ** |
| **Education: high school or below (vs college)** | **+0.9262** | 0.2972 | ±0.5944 | **+3.117** | **0.0018** | 2.5250 | ** |
| Site: UCSD (vs UAB) | +0.4141 | 0.2251 | ±0.4501 | +1.840 | 0.0658 | 1.5130 | . |
| Site: UW (vs UAB) | +0.2037 | 0.2234 | ±0.4469 | +0.911 | 0.3621 | 1.2259 |  |
| **Age (years)** | **+0.0300** | 0.0079 | ±0.0157 | **+3.813** | **1.37e-04** | 1.0304 | *** |
| **BMI (kg/m2)** | **+0.0274** | 0.0133 | ±0.0266 | **+2.058** | **0.0396** | 1.0277 | * |
| Hypertension | +0.2225 | 0.1855 | ±0.3711 | +1.199 | 0.2304 | 1.2492 |  |
| High cholesterol | +0.0156 | 0.1748 | ±0.3496 | +0.089 | 0.9288 | 1.0157 |  |
| Kidney disease | -0.3413 | 0.3341 | ±0.6682 | -1.022 | 0.3070 | 0.7108 |  |
| Circulatory disease | +0.2718 | 0.2600 | ±0.5200 | +1.045 | 0.2959 | 1.3123 |  |
| Avg. daily SD (mg/dL) | +0.0165 | 0.0229 | ±0.0458 | +0.722 | 0.4702 | 1.0167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0676**, LLR χ² = **60.15** (p = **8.71e-09**), AUC = **0.6745**, AIC = **853.6**, BIC = **908.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2912** | 0.8378 | ±1.6756 | **-3.928** | **8.55e-05** | 0.0372 | *** |
| **Education: graduate level (vs college)** | **-0.5489** | 0.1814 | ±0.3629 | **-3.025** | **0.0025** | 0.5776 | ** |
| **Education: high school or below (vs college)** | **+0.9331** | 0.2971 | ±0.5942 | **+3.141** | **0.0017** | 2.5423 | ** |
| Site: UCSD (vs UAB) | +0.3993 | 0.2246 | ±0.4492 | +1.777 | 0.0755 | 1.4907 | . |
| Site: UW (vs UAB) | +0.2128 | 0.2231 | ±0.4461 | +0.954 | 0.3401 | 1.2372 |  |
| **Age (years)** | **+0.0308** | 0.0079 | ±0.0157 | **+3.923** | **8.74e-05** | 1.0313 | *** |
| **BMI (kg/m2)** | **+0.0281** | 0.0133 | ±0.0267 | **+2.106** | **0.0352** | 1.0285 | * |
| Hypertension | +0.2310 | 0.1854 | ±0.3707 | +1.246 | 0.2126 | 1.2599 |  |
| High cholesterol | +0.0148 | 0.1748 | ±0.3496 | +0.085 | 0.9325 | 1.0149 |  |
| Kidney disease | -0.3292 | 0.3342 | ±0.6685 | -0.985 | 0.3246 | 0.7195 |  |
| Circulatory disease | +0.2677 | 0.2598 | ±0.5196 | +1.030 | 0.3029 | 1.3069 |  |
| CV (%) | -0.0105 | 0.0307 | ±0.0614 | -0.343 | 0.7318 | 0.9895 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0679**, LLR χ² = **60.38** (p = **7.88e-09**), AUC = **0.6745**, AIC = **853.4**, BIC = **907.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.7526** | 0.8730 | ±1.7461 | **-4.298** | **1.72e-05** | 0.0235 | *** |
| **Education: graduate level (vs college)** | **-0.5536** | 0.1816 | ±0.3632 | **-3.048** | **0.0023** | 0.5749 | ** |
| **Education: high school or below (vs college)** | **+0.9353** | 0.2972 | ±0.5944 | **+3.147** | **0.0016** | 2.5480 | ** |
| Site: UCSD (vs UAB) | +0.3989 | 0.2245 | ±0.4490 | +1.777 | 0.0756 | 1.4901 | . |
| Site: UW (vs UAB) | +0.2156 | 0.2232 | ±0.4463 | +0.966 | 0.3341 | 1.2405 |  |
| **Age (years)** | **+0.0310** | 0.0079 | ±0.0157 | **+3.942** | **8.08e-05** | 1.0315 | *** |
| **BMI (kg/m2)** | **+0.0281** | 0.0133 | ±0.0267 | **+2.105** | **0.0353** | 1.0285 | * |
| Hypertension | +0.2331 | 0.1854 | ±0.3708 | +1.257 | 0.2086 | 1.2626 |  |
| High cholesterol | +0.0143 | 0.1748 | ±0.3496 | +0.082 | 0.9349 | 1.0144 |  |
| Kidney disease | -0.3277 | 0.3344 | ±0.6687 | -0.980 | 0.3270 | 0.7206 |  |
| Circulatory disease | +0.2650 | 0.2598 | ±0.5196 | +1.020 | 0.3077 | 1.3034 |  |
| Mean / SD ratio | +0.0445 | 0.0749 | ±0.1498 | +0.594 | 0.5527 | 1.0455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0676**, LLR χ² = **60.17** (p = **8.63e-09**), AUC = **0.6741**, AIC = **853.6**, BIC = **907.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6295** | 0.8586 | ±1.7171 | **-4.227** | **2.36e-05** | 0.0265 | *** |
| **Education: graduate level (vs college)** | **-0.5481** | 0.1812 | ±0.3624 | **-3.025** | **0.0025** | 0.5780 | ** |
| **Education: high school or below (vs college)** | **+0.9342** | 0.2971 | ±0.5942 | **+3.144** | **0.0017** | 2.5451 | ** |
| Site: UCSD (vs UAB) | +0.3996 | 0.2246 | ±0.4491 | +1.779 | 0.0752 | 1.4912 | . |
| Site: UW (vs UAB) | +0.2146 | 0.2232 | ±0.4464 | +0.961 | 0.3364 | 1.2393 |  |
| **Age (years)** | **+0.0308** | 0.0079 | ±0.0157 | **+3.926** | **8.64e-05** | 1.0313 | *** |
| **BMI (kg/m2)** | **+0.0282** | 0.0133 | ±0.0267 | **+2.116** | **0.0343** | 1.0286 | * |
| Hypertension | +0.2298 | 0.1852 | ±0.3705 | +1.240 | 0.2149 | 1.2583 |  |
| High cholesterol | +0.0140 | 0.1748 | ±0.3496 | +0.080 | 0.9363 | 1.0141 |  |
| Kidney disease | -0.3284 | 0.3343 | ±0.6685 | -0.982 | 0.3259 | 0.7201 |  |
| Circulatory disease | +0.2677 | 0.2598 | ±0.5196 | +1.030 | 0.3028 | 1.3070 |  |
| Avg. daily mean/SD | +0.0225 | 0.0606 | ±0.1213 | +0.371 | 0.7108 | 1.0227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0688**, LLR χ² = **61.23** (p = **5.49e-09**), AUC = **0.6743**, AIC = **852.5**, BIC = **906.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9562** | 0.8446 | ±1.6892 | **-4.684** | **2.81e-06** | 0.0191 | *** |
| **Education: graduate level (vs college)** | **-0.5449** | 0.1809 | ±0.3618 | **-3.013** | **0.0026** | 0.5799 | ** |
| **Education: high school or below (vs college)** | **+0.9086** | 0.2975 | ±0.5950 | **+3.054** | **0.0023** | 2.4807 | ** |
| Site: UCSD (vs UAB) | +0.4096 | 0.2246 | ±0.4491 | +1.824 | 0.0681 | 1.5063 | . |
| Site: UW (vs UAB) | +0.2118 | 0.2232 | ±0.4464 | +0.949 | 0.3426 | 1.2359 |  |
| **Age (years)** | **+0.0308** | 0.0078 | ±0.0157 | **+3.929** | **8.52e-05** | 1.0312 | *** |
| **BMI (kg/m2)** | **+0.0282** | 0.0133 | ±0.0265 | **+2.126** | **0.0335** | 1.0286 | * |
| Hypertension | +0.2386 | 0.1856 | ±0.3712 | +1.285 | 0.1987 | 1.2694 |  |
| High cholesterol | +0.0155 | 0.1750 | ±0.3499 | +0.089 | 0.9295 | 1.0156 |  |
| Kidney disease | -0.3417 | 0.3341 | ±0.6682 | -1.023 | 0.3065 | 0.7106 |  |
| Circulatory disease | +0.2767 | 0.2603 | ±0.5205 | +1.063 | 0.2878 | 1.3187 |  |
| MAG (mg/dL/h) | +0.0136 | 0.0125 | ±0.0249 | +1.093 | 0.2743 | 1.0137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0682**, LLR χ² = **60.65** (p = **7.02e-09**), AUC = **0.6735**, AIC = **853.1**, BIC = **907.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.7879** | 0.8264 | ±1.6528 | **-4.584** | **4.57e-06** | 0.0226 | *** |
| **Education: graduate level (vs college)** | **-0.5452** | 0.1809 | ±0.3617 | **-3.015** | **0.0026** | 0.5797 | ** |
| **Education: high school or below (vs college)** | **+0.9210** | 0.2973 | ±0.5946 | **+3.098** | **0.0019** | 2.5118 | ** |
| Site: UCSD (vs UAB) | +0.4103 | 0.2248 | ±0.4495 | +1.826 | 0.0679 | 1.5073 | . |
| Site: UW (vs UAB) | +0.2036 | 0.2235 | ±0.4469 | +0.911 | 0.3622 | 1.2258 |  |
| **Age (years)** | **+0.0301** | 0.0079 | ±0.0157 | **+3.832** | **1.27e-04** | 1.0305 | *** |
| **BMI (kg/m2)** | **+0.0284** | 0.0133 | ±0.0266 | **+2.130** | **0.0331** | 1.0288 | * |
| Hypertension | +0.2266 | 0.1854 | ±0.3708 | +1.222 | 0.2216 | 1.2543 |  |
| High cholesterol | +0.0175 | 0.1749 | ±0.3498 | +0.100 | 0.9201 | 1.0177 |  |
| Kidney disease | -0.3408 | 0.3340 | ±0.6679 | -1.020 | 0.3076 | 0.7112 |  |
| Circulatory disease | +0.2687 | 0.2600 | ±0.5201 | +1.033 | 0.3015 | 1.3083 |  |
| Avg. daily range (mg/dL) | +0.0041 | 0.0052 | ±0.0104 | +0.787 | 0.4314 | 1.0041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0690**, LLR χ² = **61.42** (p = **5.05e-09**), AUC = **0.6751**, AIC = **852.3**, BIC = **906.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6596** | 0.7255 | ±1.4511 | **-5.044** | **4.56e-07** | 0.0257 | *** |
| **Education: graduate level (vs college)** | **-0.5435** | 0.1810 | ±0.3620 | **-3.003** | **0.0027** | 0.5807 | ** |
| **Education: high school or below (vs college)** | **+0.9290** | 0.2970 | ±0.5939 | **+3.128** | **0.0018** | 2.5319 | ** |
| Site: UCSD (vs UAB) | +0.4085 | 0.2247 | ±0.4494 | +1.818 | 0.0690 | 1.5046 | . |
| Site: UW (vs UAB) | +0.2076 | 0.2234 | ±0.4469 | +0.929 | 0.3527 | 1.2308 |  |
| **Age (years)** | **+0.0307** | 0.0078 | ±0.0156 | **+3.919** | **8.88e-05** | 1.0311 | *** |
| **BMI (kg/m2)** | **+0.0266** | 0.0133 | ±0.0267 | **+1.991** | **0.0465** | 1.0269 | * |
| Hypertension | +0.2315 | 0.1853 | ±0.3707 | +1.249 | 0.2116 | 1.2605 |  |
| High cholesterol | +0.0026 | 0.1751 | ±0.3502 | +0.015 | 0.9879 | 1.0026 |  |
| Kidney disease | -0.3174 | 0.3336 | ±0.6673 | -0.951 | 0.3414 | 0.7280 |  |
| Circulatory disease | +0.2686 | 0.2602 | ±0.5204 | +1.032 | 0.3018 | 1.3082 |  |
| SD of daily means (mg/dL) | +0.0435 | 0.0369 | ±0.0738 | +1.179 | 0.2385 | 1.0445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0682**, LLR χ² = **60.65** (p = **7.03e-09**), AUC = **0.6738**, AIC = **853.1**, BIC = **907.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9746 | 3.1854 | ±6.3708 | -0.306 | 0.7596 | 0.3774 |  |
| **Education: graduate level (vs college)** | **-0.5441** | 0.1808 | ±0.3616 | **-3.009** | **0.0026** | 0.5803 | ** |
| **Education: high school or below (vs college)** | **+0.9336** | 0.2972 | ±0.5943 | **+3.142** | **0.0017** | 2.5437 | ** |
| Site: UCSD (vs UAB) | +0.4128 | 0.2248 | ±0.4497 | +1.836 | 0.0663 | 1.5111 | . |
| Site: UW (vs UAB) | +0.2044 | 0.2234 | ±0.4467 | +0.915 | 0.3601 | 1.2268 |  |
| **Age (years)** | **+0.0302** | 0.0078 | ±0.0157 | **+3.847** | **1.20e-04** | 1.0306 | *** |
| **BMI (kg/m2)** | **+0.0275** | 0.0133 | ±0.0266 | **+2.068** | **0.0387** | 1.0279 | * |
| Hypertension | +0.2266 | 0.1854 | ±0.3707 | +1.222 | 0.2216 | 1.2543 |  |
| High cholesterol | +0.0087 | 0.1750 | ±0.3500 | +0.050 | 0.9602 | 1.0088 |  |
| Kidney disease | -0.3382 | 0.3340 | ±0.6680 | -1.013 | 0.3112 | 0.7130 |  |
| Circulatory disease | +0.2629 | 0.2604 | ±0.5209 | +1.010 | 0.3127 | 1.3007 |  |
| Time in range 70-180, pooled (%) | -0.0248 | 0.0312 | ±0.0623 | -0.795 | 0.4266 | 0.9755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0686**, LLR χ² = **61.01** (p = **6.02e-09**), AUC = **0.6746**, AIC = **852.7**, BIC = **907.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2794 | 3.2370 | ±6.4739 | -0.086 | 0.9312 | 0.7563 |  |
| **Education: graduate level (vs college)** | **-0.5447** | 0.1809 | ±0.3618 | **-3.011** | **0.0026** | 0.5800 | ** |
| **Education: high school or below (vs college)** | **+0.9356** | 0.2973 | ±0.5945 | **+3.147** | **0.0016** | 2.5487 | ** |
| Site: UCSD (vs UAB) | +0.4157 | 0.2249 | ±0.4498 | +1.848 | 0.0646 | 1.5154 | . |
| Site: UW (vs UAB) | +0.2037 | 0.2234 | ±0.4468 | +0.912 | 0.3619 | 1.2259 |  |
| **Age (years)** | **+0.0301** | 0.0078 | ±0.0157 | **+3.840** | **1.23e-04** | 1.0306 | *** |
| **BMI (kg/m2)** | **+0.0272** | 0.0133 | ±0.0266 | **+2.046** | **0.0407** | 1.0276 | * |
| Hypertension | +0.2274 | 0.1854 | ±0.3708 | +1.226 | 0.2200 | 1.2554 |  |
| High cholesterol | +0.0067 | 0.1750 | ±0.3501 | +0.038 | 0.9694 | 1.0067 |  |
| Kidney disease | -0.3406 | 0.3339 | ±0.6678 | -1.020 | 0.3077 | 0.7113 |  |
| Circulatory disease | +0.2590 | 0.2607 | ±0.5213 | +0.994 | 0.3203 | 1.2957 |  |
| Avg. daily time in range 70-180 (%) | -0.0317 | 0.0317 | ±0.0633 | -1.001 | 0.3168 | 0.9688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0678**, LLR χ² = **60.36** (p = **7.93e-09**), AUC = **0.6752**, AIC = **853.4**, BIC = **907.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4181** | 0.7047 | ±1.4094 | **-4.851** | **1.23e-06** | 0.0328 | *** |
| **Education: graduate level (vs college)** | **-0.5550** | 0.1818 | ±0.3636 | **-3.053** | **0.0023** | 0.5741 | ** |
| **Education: high school or below (vs college)** | **+0.9188** | 0.2978 | ±0.5957 | **+3.085** | **0.0020** | 2.5062 | ** |
| Site: UCSD (vs UAB) | +0.4076 | 0.2246 | ±0.4492 | +1.815 | 0.0695 | 1.5032 | . |
| Site: UW (vs UAB) | +0.2080 | 0.2231 | ±0.4462 | +0.932 | 0.3513 | 1.2312 |  |
| **Age (years)** | **+0.0306** | 0.0078 | ±0.0157 | **+3.905** | **9.44e-05** | 1.0310 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0133 | ±0.0266 | **+2.100** | **0.0357** | 1.0283 | * |
| Hypertension | +0.2306 | 0.1852 | ±0.3705 | +1.245 | 0.2131 | 1.2594 |  |
| High cholesterol | +0.0184 | 0.1749 | ±0.3498 | +0.105 | 0.9163 | 1.0186 |  |
| Kidney disease | -0.3349 | 0.3342 | ±0.6684 | -1.002 | 0.3163 | 0.7154 |  |
| Circulatory disease | +0.2642 | 0.2601 | ±0.5203 | +1.015 | 0.3099 | 1.3023 |  |
| Time 54-69, pooled (%) | -0.0948 | 0.1680 | ±0.3360 | -0.564 | 0.5725 | 0.9095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0677**, LLR χ² = **60.22** (p = **8.45e-09**), AUC = **0.6748**, AIC = **853.5**, BIC = **907.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4278** | 0.7043 | ±1.4085 | **-4.867** | **1.13e-06** | 0.0325 | *** |
| **Education: graduate level (vs college)** | **-0.5523** | 0.1819 | ±0.3637 | **-3.037** | **0.0024** | 0.5756 | ** |
| **Education: high school or below (vs college)** | **+0.9215** | 0.2980 | ±0.5959 | **+3.093** | **0.0020** | 2.5131 | ** |
| Site: UCSD (vs UAB) | +0.4078 | 0.2247 | ±0.4494 | +1.815 | 0.0695 | 1.5035 | . |
| Site: UW (vs UAB) | +0.2095 | 0.2231 | ±0.4462 | +0.939 | 0.3478 | 1.2330 |  |
| **Age (years)** | **+0.0306** | 0.0078 | ±0.0156 | **+3.909** | **9.28e-05** | 1.0311 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0133 | ±0.0266 | **+2.100** | **0.0357** | 1.0284 | * |
| Hypertension | +0.2298 | 0.1852 | ±0.3704 | +1.241 | 0.2147 | 1.2583 |  |
| High cholesterol | +0.0171 | 0.1749 | ±0.3497 | +0.098 | 0.9221 | 1.0173 |  |
| Kidney disease | -0.3337 | 0.3342 | ±0.6683 | -0.999 | 0.3180 | 0.7163 |  |
| Circulatory disease | +0.2649 | 0.2603 | ±0.5205 | +1.018 | 0.3087 | 1.3033 |  |
| Avg. daily time 54-69 (%) | -0.0674 | 0.1590 | ±0.3179 | -0.424 | 0.6713 | 0.9348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0678**, LLR χ² = **60.36** (p = **7.93e-09**), AUC = **0.6752**, AIC = **853.4**, BIC = **907.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4181** | 0.7047 | ±1.4094 | **-4.851** | **1.23e-06** | 0.0328 | *** |
| **Education: graduate level (vs college)** | **-0.5550** | 0.1818 | ±0.3636 | **-3.053** | **0.0023** | 0.5741 | ** |
| **Education: high school or below (vs college)** | **+0.9188** | 0.2978 | ±0.5957 | **+3.085** | **0.0020** | 2.5062 | ** |
| Site: UCSD (vs UAB) | +0.4076 | 0.2246 | ±0.4492 | +1.815 | 0.0695 | 1.5032 | . |
| Site: UW (vs UAB) | +0.2080 | 0.2231 | ±0.4462 | +0.932 | 0.3513 | 1.2312 |  |
| **Age (years)** | **+0.0306** | 0.0078 | ±0.0157 | **+3.905** | **9.44e-05** | 1.0310 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0133 | ±0.0266 | **+2.100** | **0.0357** | 1.0283 | * |
| Hypertension | +0.2306 | 0.1852 | ±0.3705 | +1.245 | 0.2131 | 1.2594 |  |
| High cholesterol | +0.0184 | 0.1749 | ±0.3498 | +0.105 | 0.9163 | 1.0186 |  |
| Kidney disease | -0.3349 | 0.3342 | ±0.6684 | -1.002 | 0.3163 | 0.7154 |  |
| Circulatory disease | +0.2642 | 0.2601 | ±0.5203 | +1.015 | 0.3099 | 1.3023 |  |
| Time < 70 (%) | -0.0948 | 0.1680 | ±0.3360 | -0.564 | 0.5725 | 0.9095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0677**, LLR χ² = **60.22** (p = **8.45e-09**), AUC = **0.6748**, AIC = **853.5**, BIC = **907.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4278** | 0.7043 | ±1.4085 | **-4.867** | **1.13e-06** | 0.0325 | *** |
| **Education: graduate level (vs college)** | **-0.5523** | 0.1819 | ±0.3637 | **-3.037** | **0.0024** | 0.5756 | ** |
| **Education: high school or below (vs college)** | **+0.9215** | 0.2980 | ±0.5959 | **+3.093** | **0.0020** | 2.5131 | ** |
| Site: UCSD (vs UAB) | +0.4078 | 0.2247 | ±0.4494 | +1.815 | 0.0695 | 1.5035 | . |
| Site: UW (vs UAB) | +0.2095 | 0.2231 | ±0.4462 | +0.939 | 0.3478 | 1.2330 |  |
| **Age (years)** | **+0.0306** | 0.0078 | ±0.0156 | **+3.909** | **9.28e-05** | 1.0311 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0133 | ±0.0266 | **+2.100** | **0.0357** | 1.0284 | * |
| Hypertension | +0.2298 | 0.1852 | ±0.3704 | +1.241 | 0.2147 | 1.2583 |  |
| High cholesterol | +0.0171 | 0.1749 | ±0.3497 | +0.098 | 0.9221 | 1.0173 |  |
| Kidney disease | -0.3337 | 0.3342 | ±0.6683 | -0.999 | 0.3180 | 0.7163 |  |
| Circulatory disease | +0.2649 | 0.2603 | ±0.5205 | +1.018 | 0.3087 | 1.3033 |  |
| Avg. daily time < 70 (%) | -0.0674 | 0.1590 | ±0.3179 | -0.424 | 0.6713 | 0.9348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0684**, LLR χ² = **60.83** (p = **6.50e-09**), AUC = **0.6743**, AIC = **852.9**, BIC = **907.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4430** | 0.7020 | ±1.4040 | **-4.904** | **9.37e-07** | 0.0320 | *** |
| **Education: graduate level (vs college)** | **-0.5480** | 0.1809 | ±0.3619 | **-3.028** | **0.0025** | 0.5781 | ** |
| **Education: high school or below (vs college)** | **+0.9299** | 0.2972 | ±0.5943 | **+3.129** | **0.0018** | 2.5342 | ** |
| Site: UCSD (vs UAB) | +0.4158 | 0.2250 | ±0.4499 | +1.848 | 0.0646 | 1.5156 | . |
| Site: UW (vs UAB) | +0.2024 | 0.2234 | ±0.4469 | +0.906 | 0.3649 | 1.2244 |  |
| **Age (years)** | **+0.0301** | 0.0078 | ±0.0157 | **+3.838** | **1.24e-04** | 1.0306 | *** |
| **BMI (kg/m2)** | **+0.0274** | 0.0133 | ±0.0266 | **+2.060** | **0.0394** | 1.0278 | * |
| Hypertension | +0.2269 | 0.1854 | ±0.3707 | +1.224 | 0.2210 | 1.2547 |  |
| High cholesterol | +0.0088 | 0.1749 | ±0.3499 | +0.050 | 0.9598 | 1.0089 |  |
| Kidney disease | -0.3402 | 0.3341 | ±0.6681 | -1.018 | 0.3085 | 0.7116 |  |
| Circulatory disease | +0.2597 | 0.2607 | ±0.5213 | +0.996 | 0.3190 | 1.2966 |  |
| Time 181-250, pooled (%) | +0.0280 | 0.0309 | ±0.0617 | +0.906 | 0.3649 | 1.0284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0688**, LLR χ² = **61.19** (p = **5.58e-09**), AUC = **0.6751**, AIC = **852.6**, BIC = **906.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4389** | 0.7016 | ±1.4032 | **-4.901** | **9.52e-07** | 0.0321 | *** |
| **Education: graduate level (vs college)** | **-0.5496** | 0.1810 | ±0.3621 | **-3.036** | **0.0024** | 0.5772 | ** |
| **Education: high school or below (vs college)** | **+0.9306** | 0.2972 | ±0.5945 | **+3.131** | **0.0017** | 2.5359 | ** |
| Site: UCSD (vs UAB) | +0.4195 | 0.2251 | ±0.4502 | +1.864 | 0.0624 | 1.5212 | . |
| Site: UW (vs UAB) | +0.2020 | 0.2234 | ±0.4469 | +0.904 | 0.3659 | 1.2239 |  |
| **Age (years)** | **+0.0301** | 0.0078 | ±0.0157 | **+3.835** | **1.26e-04** | 1.0305 | *** |
| **BMI (kg/m2)** | **+0.0271** | 0.0133 | ±0.0266 | **+2.038** | **0.0416** | 1.0275 | * |
| Hypertension | +0.2279 | 0.1854 | ±0.3709 | +1.229 | 0.2190 | 1.2560 |  |
| High cholesterol | +0.0071 | 0.1750 | ±0.3500 | +0.040 | 0.9678 | 1.0071 |  |
| Kidney disease | -0.3426 | 0.3340 | ±0.6680 | -1.026 | 0.3050 | 0.7099 |  |
| Circulatory disease | +0.2548 | 0.2610 | ±0.5219 | +0.976 | 0.3289 | 1.2902 |  |
| Avg. daily time 181-250 (%) | +0.0342 | 0.0315 | ±0.0629 | +1.088 | 0.2765 | 1.0348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0684**, LLR χ² = **60.83** (p = **6.50e-09**), AUC = **0.6743**, AIC = **852.9**, BIC = **907.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4430** | 0.7020 | ±1.4040 | **-4.904** | **9.37e-07** | 0.0320 | *** |
| **Education: graduate level (vs college)** | **-0.5480** | 0.1809 | ±0.3619 | **-3.028** | **0.0025** | 0.5781 | ** |
| **Education: high school or below (vs college)** | **+0.9299** | 0.2972 | ±0.5943 | **+3.129** | **0.0018** | 2.5342 | ** |
| Site: UCSD (vs UAB) | +0.4158 | 0.2250 | ±0.4499 | +1.848 | 0.0646 | 1.5156 | . |
| Site: UW (vs UAB) | +0.2024 | 0.2234 | ±0.4469 | +0.906 | 0.3649 | 1.2244 |  |
| **Age (years)** | **+0.0301** | 0.0078 | ±0.0157 | **+3.838** | **1.24e-04** | 1.0306 | *** |
| **BMI (kg/m2)** | **+0.0274** | 0.0133 | ±0.0266 | **+2.060** | **0.0394** | 1.0278 | * |
| Hypertension | +0.2269 | 0.1854 | ±0.3707 | +1.224 | 0.2210 | 1.2547 |  |
| High cholesterol | +0.0088 | 0.1749 | ±0.3499 | +0.050 | 0.9598 | 1.0089 |  |
| Kidney disease | -0.3402 | 0.3341 | ±0.6681 | -1.018 | 0.3085 | 0.7116 |  |
| Circulatory disease | +0.2597 | 0.2607 | ±0.5213 | +0.996 | 0.3190 | 1.2966 |  |
| Time > 180 (%) | +0.0280 | 0.0309 | ±0.0617 | +0.906 | 0.3649 | 1.0284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0688**, LLR χ² = **61.19** (p = **5.58e-09**), AUC = **0.6751**, AIC = **852.6**, BIC = **906.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4389** | 0.7016 | ±1.4032 | **-4.901** | **9.52e-07** | 0.0321 | *** |
| **Education: graduate level (vs college)** | **-0.5496** | 0.1810 | ±0.3621 | **-3.036** | **0.0024** | 0.5772 | ** |
| **Education: high school or below (vs college)** | **+0.9306** | 0.2972 | ±0.5945 | **+3.131** | **0.0017** | 2.5359 | ** |
| Site: UCSD (vs UAB) | +0.4195 | 0.2251 | ±0.4502 | +1.864 | 0.0624 | 1.5212 | . |
| Site: UW (vs UAB) | +0.2020 | 0.2234 | ±0.4469 | +0.904 | 0.3659 | 1.2239 |  |
| **Age (years)** | **+0.0301** | 0.0078 | ±0.0157 | **+3.835** | **1.26e-04** | 1.0305 | *** |
| **BMI (kg/m2)** | **+0.0271** | 0.0133 | ±0.0266 | **+2.038** | **0.0416** | 1.0275 | * |
| Hypertension | +0.2279 | 0.1854 | ±0.3709 | +1.229 | 0.2190 | 1.2560 |  |
| High cholesterol | +0.0071 | 0.1750 | ±0.3500 | +0.040 | 0.9678 | 1.0071 |  |
| Kidney disease | -0.3426 | 0.3340 | ±0.6680 | -1.026 | 0.3050 | 0.7099 |  |
| Circulatory disease | +0.2548 | 0.2610 | ±0.5219 | +0.976 | 0.3289 | 1.2902 |  |
| Avg. daily time > 180 (%) | +0.0342 | 0.0315 | ±0.0629 | +1.088 | 0.2765 | 1.0348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, events = **242**, McFadden pseudo-R² = **0.0679**, LLR χ² = **60.42** (p = **7.76e-09**), AUC = **0.6733**, AIC = **853.3**, BIC = **907.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4405** | 0.7020 | ±1.4040 | **-4.901** | **9.53e-07** | 0.0320 | *** |
| **Education: graduate level (vs college)** | **-0.5426** | 0.1808 | ±0.3615 | **-3.002** | **0.0027** | 0.5812 | ** |
| **Education: high school or below (vs college)** | **+0.9270** | 0.2972 | ±0.5945 | **+3.119** | **0.0018** | 2.5270 | ** |
| Site: UCSD (vs UAB) | +0.4076 | 0.2246 | ±0.4491 | +1.815 | 0.0695 | 1.5032 | . |
| Site: UW (vs UAB) | +0.2071 | 0.2232 | ±0.4465 | +0.928 | 0.3536 | 1.2301 |  |
| **Age (years)** | **+0.0308** | 0.0078 | ±0.0157 | **+3.928** | **8.57e-05** | 1.0312 | *** |
| **BMI (kg/m2)** | **+0.0270** | 0.0134 | ±0.0268 | **+2.014** | **0.0440** | 1.0273 | * |
| Hypertension | +0.2318 | 0.1854 | ±0.3707 | +1.250 | 0.2112 | 1.2608 |  |
| High cholesterol | +0.0049 | 0.1755 | ±0.3511 | +0.028 | 0.9779 | 1.0049 |  |
| Kidney disease | -0.3292 | 0.3339 | ±0.6677 | -0.986 | 0.3242 | 0.7195 |  |
| Circulatory disease | +0.2722 | 0.2600 | ±0.5200 | +1.047 | 0.2952 | 1.3128 |  |
| Nocturnal time > 180 (%) | +0.0170 | 0.0270 | ±0.0539 | +0.631 | 0.5278 | 1.0172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 685; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, R² = **0.0885**, Adj R² = **0.0750**, F-statistic = **6.54** (p = **1.05e-09**), Residual SE = **2.551** on **674** df, AIC = **3237.6**, BIC = **3287.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4192** | 0.8080 | ±1.6160 | **+20.321** | **8.40e-92** | *** |
| Education: graduate level (vs college) | +0.2525 | 0.2044 | ±0.4089 | +1.235 | 0.2167 |  |
| **Education: high school or below (vs college)** | **-1.4239** | 0.4810 | ±0.9620 | **-2.960** | **0.0031** | ** |
| Site: UCSD (vs UAB) | -0.0806 | 0.2718 | ±0.5436 | -0.296 | 0.7669 |  |
| Site: UW (vs UAB) | -0.1437 | 0.2748 | ±0.5496 | -0.523 | 0.6010 |  |
| **Age (years)** | **-0.0455** | 0.0097 | ±0.0195 | **-4.670** | **3.01e-06** | *** |
| BMI (kg/m2) | -0.0243 | 0.0142 | ±0.0285 | -1.704 | 0.0883 | . |
| Hypertension | -0.4078 | 0.2254 | ±0.4508 | -1.809 | 0.0705 | . |
| High cholesterol | -0.0254 | 0.2117 | ±0.4233 | -0.120 | 0.9044 |  |
| Kidney disease | -0.3885 | 0.4796 | ±0.9591 | -0.810 | 0.4178 |  |
| Circulatory disease | -0.1066 | 0.3055 | ±0.6109 | -0.349 | 0.7272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, R² = **0.0885**, Adj R² = **0.0736**, F-statistic = **5.94** (p = **2.80e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.6**, BIC = **3293.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5193** | 1.7754 | ±3.5508 | **+9.305** | **1.34e-20** | *** |
| Education: graduate level (vs college) | +0.2528 | 0.2047 | ±0.4094 | +1.235 | 0.2169 |  |
| **Education: high school or below (vs college)** | **-1.4238** | 0.4819 | ±0.9639 | **-2.954** | **0.0031** | ** |
| Site: UCSD (vs UAB) | -0.0806 | 0.2722 | ±0.5444 | -0.296 | 0.7672 |  |
| Site: UW (vs UAB) | -0.1434 | 0.2751 | ±0.5502 | -0.521 | 0.6021 |  |
| **Age (years)** | **-0.0454** | 0.0099 | ±0.0197 | **-4.610** | **4.02e-06** | *** |
| BMI (kg/m2) | -0.0241 | 0.0143 | ±0.0287 | -1.685 | 0.0920 | . |
| Hypertension | -0.4065 | 0.2272 | ±0.4543 | -1.790 | 0.0735 | . |
| High cholesterol | -0.0242 | 0.2102 | ±0.4204 | -0.115 | 0.9085 |  |
| Kidney disease | -0.3886 | 0.4803 | ±0.9605 | -0.809 | 0.4184 |  |
| Circulatory disease | -0.1070 | 0.3062 | ±0.6125 | -0.349 | 0.7267 |  |
| HbA1c (%) | -0.0196 | 0.3071 | ±0.6142 | -0.064 | 0.9492 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, R² = **0.0991**, Adj R² = **0.0844**, F-statistic = **6.73** (p = **9.06e-11**), Residual SE = **2.538** on **673** df, AIC = **3231.6**, BIC = **3286.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19.1228** | 1.4255 | ±2.8510 | **+13.415** | **4.97e-41** | *** |
| Education: graduate level (vs college) | +0.2904 | 0.2024 | ±0.4049 | +1.434 | 0.1514 |  |
| **Education: high school or below (vs college)** | **-1.3935** | 0.4780 | ±0.9560 | **-2.915** | **0.0036** | ** |
| Site: UCSD (vs UAB) | -0.1086 | 0.2664 | ±0.5328 | -0.408 | 0.6835 |  |
| Site: UW (vs UAB) | -0.0946 | 0.2781 | ±0.5562 | -0.340 | 0.7336 |  |
| **Age (years)** | **-0.0442** | 0.0098 | ±0.0197 | **-4.496** | **6.92e-06** | *** |
| BMI (kg/m2) | -0.0198 | 0.0145 | ±0.0290 | -1.363 | 0.1728 |  |
| Hypertension | -0.3690 | 0.2280 | ±0.4560 | -1.619 | 0.1055 |  |
| High cholesterol | -0.0284 | 0.2121 | ±0.4241 | -0.134 | 0.8934 |  |
| Kidney disease | -0.3434 | 0.4681 | ±0.9363 | -0.734 | 0.4632 |  |
| Circulatory disease | -0.0508 | 0.3054 | ±0.6109 | -0.166 | 0.8678 |  |
| **Mean glucose (mg/dL)** | **-0.0249** | 0.0123 | ±0.0246 | **-2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, R² = **0.0991**, Adj R² = **0.0844**, F-statistic = **6.73** (p = **9.06e-11**), Residual SE = **2.538** on **673** df, AIC = **3231.6**, BIC = **3286.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.5653** | 2.9942 | ±5.9883 | **+7.536** | **4.83e-14** | *** |
| Education: graduate level (vs college) | +0.2904 | 0.2024 | ±0.4049 | +1.434 | 0.1514 |  |
| **Education: high school or below (vs college)** | **-1.3935** | 0.4780 | ±0.9560 | **-2.915** | **0.0036** | ** |
| Site: UCSD (vs UAB) | -0.1086 | 0.2664 | ±0.5328 | -0.408 | 0.6835 |  |
| Site: UW (vs UAB) | -0.0946 | 0.2781 | ±0.5562 | -0.340 | 0.7336 |  |
| **Age (years)** | **-0.0442** | 0.0098 | ±0.0197 | **-4.496** | **6.92e-06** | *** |
| BMI (kg/m2) | -0.0198 | 0.0145 | ±0.0290 | -1.363 | 0.1728 |  |
| Hypertension | -0.3690 | 0.2280 | ±0.4560 | -1.619 | 0.1055 |  |
| High cholesterol | -0.0284 | 0.2121 | ±0.4241 | -0.134 | 0.8934 |  |
| Kidney disease | -0.3434 | 0.4681 | ±0.9363 | -0.734 | 0.4632 |  |
| Circulatory disease | -0.0508 | 0.3054 | ±0.6109 | -0.166 | 0.8678 |  |
| **GMI (%)** | **-1.0400** | 0.5140 | ±1.0279 | **-2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, R² = **0.0977**, Adj R² = **0.0830**, F-statistic = **6.63** (p = **1.41e-10**), Residual SE = **2.539** on **673** df, AIC = **3232.6**, BIC = **3287.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.6262** | 1.2352 | ±2.4704 | **+15.079** | **2.21e-51** | *** |
| Education: graduate level (vs college) | +0.2736 | 0.2033 | ±0.4067 | +1.346 | 0.1784 |  |
| **Education: high school or below (vs college)** | **-1.4036** | 0.4791 | ±0.9582 | **-2.930** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.0796 | 0.2703 | ±0.5406 | -0.294 | 0.7684 |  |
| Site: UW (vs UAB) | -0.0974 | 0.2771 | ±0.5542 | -0.351 | 0.7252 |  |
| **Age (years)** | **-0.0464** | 0.0097 | ±0.0194 | **-4.776** | **1.79e-06** | *** |
| BMI (kg/m2) | -0.0155 | 0.0153 | ±0.0306 | -1.015 | 0.3099 |  |
| Hypertension | -0.3897 | 0.2266 | ±0.4531 | -1.720 | 0.0855 | . |
| High cholesterol | -0.0055 | 0.2125 | ±0.4251 | -0.026 | 0.9793 |  |
| Kidney disease | -0.3672 | 0.4749 | ±0.9498 | -0.773 | 0.4394 |  |
| Circulatory disease | -0.0679 | 0.3048 | ±0.6095 | -0.223 | 0.8237 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0206** | 0.0100 | ±0.0200 | **-2.062** | **0.0392** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0885**, Adj R² = **0.0736**, F-statistic = **5.94** (p = **2.78e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.6**, BIC = **3293.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4827** | 0.9032 | ±1.8065 | **+18.249** | **2.13e-74** | *** |
| Education: graduate level (vs college) | +0.2511 | 0.2049 | ±0.4099 | +1.225 | 0.2206 |  |
| **Education: high school or below (vs college)** | **-1.4226** | 0.4817 | ±0.9634 | **-2.953** | **0.0031** | ** |
| Site: UCSD (vs UAB) | -0.0828 | 0.2718 | ±0.5435 | -0.305 | 0.7607 |  |
| Site: UW (vs UAB) | -0.1418 | 0.2754 | ±0.5509 | -0.515 | 0.6067 |  |
| **Age (years)** | **-0.0454** | 0.0098 | ±0.0196 | **-4.621** | **3.82e-06** | *** |
| BMI (kg/m2) | -0.0242 | 0.0143 | ±0.0287 | -1.687 | 0.0917 | . |
| Hypertension | -0.4059 | 0.2261 | ±0.4522 | -1.795 | 0.0726 | . |
| High cholesterol | -0.0251 | 0.2117 | ±0.4234 | -0.119 | 0.9055 |  |
| Kidney disease | -0.3867 | 0.4808 | ±0.9617 | -0.804 | 0.4212 |  |
| Circulatory disease | -0.1070 | 0.3058 | ±0.6116 | -0.350 | 0.7263 |  |
| Glucose SD, pooled (mg/dL) | -0.0039 | 0.0264 | ±0.0529 | -0.147 | 0.8828 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0886**, Adj R² = **0.0737**, F-statistic = **5.95** (p = **2.74e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.5**, BIC = **3293.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5096** | 0.8854 | ±1.7708 | **+18.647** | **1.34e-77** | *** |
| Education: graduate level (vs college) | +0.2512 | 0.2048 | ±0.4096 | +1.226 | 0.2200 |  |
| **Education: high school or below (vs college)** | **-1.4217** | 0.4817 | ±0.9633 | **-2.952** | **0.0032** | ** |
| Site: UCSD (vs UAB) | -0.0846 | 0.2712 | ±0.5423 | -0.312 | 0.7551 |  |
| Site: UW (vs UAB) | -0.1408 | 0.2757 | ±0.5513 | -0.511 | 0.6094 |  |
| **Age (years)** | **-0.0453** | 0.0098 | ±0.0196 | **-4.621** | **3.82e-06** | *** |
| BMI (kg/m2) | -0.0241 | 0.0144 | ±0.0287 | -1.676 | 0.0937 | . |
| Hypertension | -0.4052 | 0.2261 | ±0.4522 | -1.792 | 0.0731 | . |
| High cholesterol | -0.0253 | 0.2120 | ±0.4239 | -0.120 | 0.9048 |  |
| Kidney disease | -0.3849 | 0.4807 | ±0.9614 | -0.801 | 0.4233 |  |
| Circulatory disease | -0.1069 | 0.3057 | ±0.6115 | -0.350 | 0.7267 |  |
| Avg. daily SD (mg/dL) | -0.0062 | 0.0267 | ±0.0534 | -0.233 | 0.8161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, R² = **0.0902**, Adj R² = **0.0754**, F-statistic = **6.07** (p = **1.61e-09**), Residual SE = **2.550** on **673** df, AIC = **3238.3**, BIC = **3292.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8018** | 1.0116 | ±2.0231 | **+15.621** | **5.22e-55** | *** |
| Education: graduate level (vs college) | +0.2747 | 0.2037 | ±0.4074 | +1.349 | 0.1775 |  |
| **Education: high school or below (vs college)** | **-1.4272** | 0.4812 | ±0.9624 | **-2.966** | **0.0030** | ** |
| Site: UCSD (vs UAB) | -0.0667 | 0.2730 | ±0.5459 | -0.244 | 0.8069 |  |
| Site: UW (vs UAB) | -0.1491 | 0.2743 | ±0.5485 | -0.544 | 0.5866 |  |
| **Age (years)** | **-0.0464** | 0.0098 | ±0.0196 | **-4.745** | **2.08e-06** | *** |
| BMI (kg/m2) | -0.0241 | 0.0141 | ±0.0282 | -1.706 | 0.0879 | . |
| Hypertension | -0.4170 | 0.2254 | ±0.4508 | -1.850 | 0.0643 | . |
| High cholesterol | -0.0268 | 0.2115 | ±0.4231 | -0.126 | 0.8993 |  |
| Kidney disease | -0.3955 | 0.4802 | ±0.9603 | -0.824 | 0.4102 |  |
| Circulatory disease | -0.0907 | 0.3074 | ±0.6147 | -0.295 | 0.7679 |  |
| CV (%) | +0.0406 | 0.0374 | ±0.0748 | +1.086 | 0.2777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, R² = **0.0917**, Adj R² = **0.0768**, F-statistic = **6.18** (p = **1.01e-09**), Residual SE = **2.548** on **673** df, AIC = **3237.2**, BIC = **3291.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3196** | 0.9961 | ±1.9921 | **+17.388** | **1.02e-67** | *** |
| Education: graduate level (vs college) | +0.2840 | 0.2028 | ±0.4056 | +1.400 | 0.1614 |  |
| **Education: high school or below (vs college)** | **-1.4317** | 0.4818 | ±0.9635 | **-2.972** | **0.0030** | ** |
| Site: UCSD (vs UAB) | -0.0683 | 0.2729 | ±0.5458 | -0.250 | 0.8024 |  |
| Site: UW (vs UAB) | -0.1566 | 0.2730 | ±0.5461 | -0.573 | 0.5664 |  |
| **Age (years)** | **-0.0465** | 0.0098 | ±0.0195 | **-4.770** | **1.84e-06** | *** |
| BMI (kg/m2) | -0.0240 | 0.0141 | ±0.0281 | -1.707 | 0.0878 | . |
| Hypertension | -0.4214 | 0.2252 | ±0.4505 | -1.871 | 0.0613 | . |
| High cholesterol | -0.0249 | 0.2117 | ±0.4235 | -0.118 | 0.9064 |  |
| Kidney disease | -0.3989 | 0.4799 | ±0.9598 | -0.831 | 0.4058 |  |
| Circulatory disease | -0.0850 | 0.3075 | ±0.6150 | -0.276 | 0.7823 |  |
| Mean / SD ratio | -0.1340 | 0.1008 | ±0.2015 | -1.330 | 0.1837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0906**, Adj R² = **0.0757**, F-statistic = **6.09** (p = **1.45e-09**), Residual SE = **2.550** on **673** df, AIC = **3238.0**, BIC = **3292.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1111** | 0.9602 | ±1.9204 | **+17.821** | **4.87e-71** | *** |
| Education: graduate level (vs college) | +0.2721 | 0.2032 | ±0.4064 | +1.339 | 0.1806 |  |
| **Education: high school or below (vs college)** | **-1.4318** | 0.4815 | ±0.9629 | **-2.974** | **0.0029** | ** |
| Site: UCSD (vs UAB) | -0.0678 | 0.2731 | ±0.5461 | -0.248 | 0.8038 |  |
| Site: UW (vs UAB) | -0.1557 | 0.2737 | ±0.5473 | -0.569 | 0.5693 |  |
| **Age (years)** | **-0.0464** | 0.0097 | ±0.0195 | **-4.766** | **1.88e-06** | *** |
| BMI (kg/m2) | -0.0247 | 0.0141 | ±0.0282 | -1.747 | 0.0806 | . |
| Hypertension | -0.4125 | 0.2255 | ±0.4511 | -1.829 | 0.0674 | . |
| High cholesterol | -0.0219 | 0.2123 | ±0.4246 | -0.103 | 0.9179 |  |
| Kidney disease | -0.4008 | 0.4803 | ±0.9606 | -0.835 | 0.4040 |  |
| Circulatory disease | -0.0907 | 0.3071 | ±0.6143 | -0.295 | 0.7678 |  |
| Avg. daily mean/SD | -0.0875 | 0.0762 | ±0.1524 | -1.148 | 0.2511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, R² = **0.0886**, Adj R² = **0.0737**, F-statistic = **5.95** (p = **2.72e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.5**, BIC = **3293.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2710** | 0.9243 | ±1.8486 | **+17.603** | **2.32e-69** | *** |
| Education: graduate level (vs college) | +0.2528 | 0.2046 | ±0.4092 | +1.235 | 0.2167 |  |
| **Education: high school or below (vs college)** | **-1.4309** | 0.4793 | ±0.9587 | **-2.985** | **0.0028** | ** |
| Site: UCSD (vs UAB) | -0.0790 | 0.2719 | ±0.5438 | -0.290 | 0.7715 |  |
| Site: UW (vs UAB) | -0.1430 | 0.2753 | ±0.5505 | -0.520 | 0.6034 |  |
| **Age (years)** | **-0.0455** | 0.0098 | ±0.0195 | **-4.663** | **3.12e-06** | *** |
| BMI (kg/m2) | -0.0242 | 0.0142 | ±0.0284 | -1.702 | 0.0887 | . |
| Hypertension | -0.4051 | 0.2258 | ±0.4517 | -1.794 | 0.0728 | . |
| High cholesterol | -0.0247 | 0.2120 | ±0.4240 | -0.117 | 0.9071 |  |
| Kidney disease | -0.3925 | 0.4812 | ±0.9625 | -0.816 | 0.4148 |  |
| Circulatory disease | -0.1050 | 0.3054 | ±0.6108 | -0.344 | 0.7310 |  |
| MAG (mg/dL/h) | +0.0040 | 0.0136 | ±0.0273 | +0.293 | 0.7697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, R² = **0.0886**, Adj R² = **0.0737**, F-statistic = **5.95** (p = **2.75e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.5**, BIC = **3293.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5285** | 0.9400 | ±1.8800 | **+17.583** | **3.32e-69** | *** |
| Education: graduate level (vs college) | +0.2527 | 0.2049 | ±0.4097 | +1.233 | 0.2174 |  |
| **Education: high school or below (vs college)** | **-1.4204** | 0.4811 | ±0.9622 | **-2.952** | **0.0032** | ** |
| Site: UCSD (vs UAB) | -0.0827 | 0.2715 | ±0.5431 | -0.304 | 0.7608 |  |
| Site: UW (vs UAB) | -0.1412 | 0.2752 | ±0.5504 | -0.513 | 0.6080 |  |
| **Age (years)** | **-0.0453** | 0.0098 | ±0.0196 | **-4.637** | **3.54e-06** | *** |
| BMI (kg/m2) | -0.0244 | 0.0143 | ±0.0285 | -1.713 | 0.0867 | . |
| Hypertension | -0.4069 | 0.2259 | ±0.4517 | -1.801 | 0.0716 | . |
| High cholesterol | -0.0261 | 0.2126 | ±0.4251 | -0.123 | 0.9022 |  |
| Kidney disease | -0.3850 | 0.4800 | ±0.9601 | -0.802 | 0.4225 |  |
| Circulatory disease | -0.1058 | 0.3056 | ±0.6113 | -0.346 | 0.7292 |  |
| Avg. daily range (mg/dL) | -0.0013 | 0.0059 | ±0.0118 | -0.222 | 0.8245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, R² = **0.0892**, Adj R² = **0.0743**, F-statistic = **5.99** (p = **2.22e-09**), Residual SE = **2.551** on **673** df, AIC = **3239.0**, BIC = **3293.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5694** | 0.8325 | ±1.6651 | **+19.902** | **3.89e-88** | *** |
| Education: graduate level (vs college) | +0.2504 | 0.2047 | ±0.4093 | +1.223 | 0.2212 |  |
| **Education: high school or below (vs college)** | **-1.4217** | 0.4792 | ±0.9584 | **-2.967** | **0.0030** | ** |
| Site: UCSD (vs UAB) | -0.0829 | 0.2725 | ±0.5450 | -0.304 | 0.7609 |  |
| Site: UW (vs UAB) | -0.1392 | 0.2744 | ±0.5489 | -0.507 | 0.6120 |  |
| **Age (years)** | **-0.0455** | 0.0097 | ±0.0195 | **-4.671** | **3.00e-06** | *** |
| BMI (kg/m2) | -0.0232 | 0.0144 | ±0.0288 | -1.608 | 0.1079 |  |
| Hypertension | -0.4099 | 0.2257 | ±0.4515 | -1.816 | 0.0694 | . |
| High cholesterol | -0.0145 | 0.2116 | ±0.4232 | -0.069 | 0.9453 |  |
| Kidney disease | -0.3978 | 0.4789 | ±0.9578 | -0.831 | 0.4062 |  |
| Circulatory disease | -0.1045 | 0.3062 | ±0.6124 | -0.341 | 0.7329 |  |
| SD of daily means (mg/dL) | -0.0321 | 0.0416 | ±0.0832 | -0.772 | 0.4401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, R² = **0.0972**, Adj R² = **0.0824**, F-statistic = **6.58** (p = **1.70e-10**), Residual SE = **2.540** on **673** df, AIC = **3233.1**, BIC = **3287.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.1322 | 6.4512 | ±12.9023 | +1.106 | 0.2689 |  |
| Education: graduate level (vs college) | +0.2565 | 0.2041 | ±0.4081 | +1.257 | 0.2087 |  |
| **Education: high school or below (vs college)** | **-1.4269** | 0.4819 | ±0.9637 | **-2.961** | **0.0031** | ** |
| Site: UCSD (vs UAB) | -0.1191 | 0.2631 | ±0.5261 | -0.453 | 0.6507 |  |
| Site: UW (vs UAB) | -0.1201 | 0.2776 | ±0.5553 | -0.433 | 0.6653 |  |
| **Age (years)** | **-0.0440** | 0.0099 | ±0.0198 | **-4.445** | **8.77e-06** | *** |
| BMI (kg/m2) | -0.0227 | 0.0145 | ±0.0289 | -1.570 | 0.1164 |  |
| Hypertension | -0.3989 | 0.2267 | ±0.4533 | -1.760 | 0.0784 | . |
| High cholesterol | +0.0022 | 0.2129 | ±0.4259 | +0.010 | 0.9918 |  |
| Kidney disease | -0.3614 | 0.4692 | ±0.9385 | -0.770 | 0.4412 |  |
| Circulatory disease | -0.0728 | 0.3095 | ±0.6190 | -0.235 | 0.8140 |  |
| Time in range 70-180, pooled (%) | +0.0931 | 0.0625 | ±0.1250 | +1.490 | 0.1363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, R² = **0.0975**, Adj R² = **0.0828**, F-statistic = **6.61** (p = **1.52e-10**), Residual SE = **2.540** on **673** df, AIC = **3232.8**, BIC = **3287.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +6.7291 | 6.5285 | ±13.0571 | +1.031 | 0.3027 |  |
| Education: graduate level (vs college) | +0.2573 | 0.2040 | ±0.4080 | +1.261 | 0.2072 |  |
| **Education: high school or below (vs college)** | **-1.4313** | 0.4812 | ±0.9624 | **-2.974** | **0.0029** | ** |
| Site: UCSD (vs UAB) | -0.1206 | 0.2631 | ±0.5262 | -0.459 | 0.6465 |  |
| Site: UW (vs UAB) | -0.1230 | 0.2770 | ±0.5539 | -0.444 | 0.6570 |  |
| **Age (years)** | **-0.0441** | 0.0099 | ±0.0198 | **-4.468** | **7.91e-06** | *** |
| BMI (kg/m2) | -0.0222 | 0.0146 | ±0.0291 | -1.527 | 0.1267 |  |
| Hypertension | -0.4023 | 0.2267 | ±0.4533 | -1.775 | 0.0759 | . |
| High cholesterol | +0.0035 | 0.2128 | ±0.4256 | +0.016 | 0.9869 |  |
| Kidney disease | -0.3568 | 0.4673 | ±0.9346 | -0.764 | 0.4451 |  |
| Circulatory disease | -0.0662 | 0.3099 | ±0.6197 | -0.214 | 0.8309 |  |
| Avg. daily time in range 70-180 (%) | +0.0971 | 0.0633 | ±0.1265 | +1.534 | 0.1249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, R² = **0.0887**, Adj R² = **0.0738**, F-statistic = **5.96** (p = **2.61e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.4**, BIC = **3293.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3926** | 0.8119 | ±1.6237 | **+20.191** | **1.17e-90** | *** |
| Education: graduate level (vs college) | +0.2618 | 0.2054 | ±0.4108 | +1.275 | 0.2024 |  |
| **Education: high school or below (vs college)** | **-1.4128** | 0.4824 | ±0.9647 | **-2.929** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.0839 | 0.2722 | ±0.5445 | -0.308 | 0.7579 |  |
| Site: UW (vs UAB) | -0.1413 | 0.2750 | ±0.5501 | -0.514 | 0.6075 |  |
| **Age (years)** | **-0.0455** | 0.0098 | ±0.0195 | **-4.662** | **3.13e-06** | *** |
| BMI (kg/m2) | -0.0242 | 0.0143 | ±0.0285 | -1.697 | 0.0898 | . |
| Hypertension | -0.4086 | 0.2256 | ±0.4512 | -1.811 | 0.0701 | . |
| High cholesterol | -0.0278 | 0.2117 | ±0.4233 | -0.131 | 0.8954 |  |
| Kidney disease | -0.3865 | 0.4795 | ±0.9591 | -0.806 | 0.4203 |  |
| Circulatory disease | -0.1012 | 0.3060 | ±0.6119 | -0.331 | 0.7407 |  |
| Time 54-69, pooled (%) | +0.0774 | 0.1256 | ±0.2513 | +0.616 | 0.5380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, R² = **0.0887**, Adj R² = **0.0738**, F-statistic = **5.96** (p = **2.62e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.4**, BIC = **3293.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3963** | 0.8104 | ±1.6208 | **+20.232** | **5.12e-91** | *** |
| Education: graduate level (vs college) | +0.2618 | 0.2057 | ±0.4113 | +1.273 | 0.2030 |  |
| **Education: high school or below (vs college)** | **-1.4125** | 0.4824 | ±0.9648 | **-2.928** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.0854 | 0.2725 | ±0.5450 | -0.313 | 0.7540 |  |
| Site: UW (vs UAB) | -0.1419 | 0.2750 | ±0.5500 | -0.516 | 0.6060 |  |
| **Age (years)** | **-0.0455** | 0.0097 | ±0.0195 | **-4.666** | **3.07e-06** | *** |
| BMI (kg/m2) | -0.0242 | 0.0143 | ±0.0285 | -1.697 | 0.0898 | . |
| Hypertension | -0.4082 | 0.2255 | ±0.4511 | -1.810 | 0.0703 | . |
| High cholesterol | -0.0274 | 0.2117 | ±0.4233 | -0.130 | 0.8969 |  |
| Kidney disease | -0.3868 | 0.4796 | ±0.9593 | -0.807 | 0.4199 |  |
| Circulatory disease | -0.1002 | 0.3064 | ±0.6127 | -0.327 | 0.7436 |  |
| Avg. daily time 54-69 (%) | +0.0728 | 0.1223 | ±0.2445 | +0.596 | 0.5513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, R² = **0.0887**, Adj R² = **0.0738**, F-statistic = **5.96** (p = **2.61e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.4**, BIC = **3293.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3926** | 0.8119 | ±1.6237 | **+20.191** | **1.17e-90** | *** |
| Education: graduate level (vs college) | +0.2618 | 0.2054 | ±0.4108 | +1.275 | 0.2024 |  |
| **Education: high school or below (vs college)** | **-1.4128** | 0.4824 | ±0.9647 | **-2.929** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.0839 | 0.2722 | ±0.5445 | -0.308 | 0.7579 |  |
| Site: UW (vs UAB) | -0.1413 | 0.2750 | ±0.5501 | -0.514 | 0.6075 |  |
| **Age (years)** | **-0.0455** | 0.0098 | ±0.0195 | **-4.662** | **3.13e-06** | *** |
| BMI (kg/m2) | -0.0242 | 0.0143 | ±0.0285 | -1.697 | 0.0898 | . |
| Hypertension | -0.4086 | 0.2256 | ±0.4512 | -1.811 | 0.0701 | . |
| High cholesterol | -0.0278 | 0.2117 | ±0.4233 | -0.131 | 0.8954 |  |
| Kidney disease | -0.3865 | 0.4795 | ±0.9591 | -0.806 | 0.4203 |  |
| Circulatory disease | -0.1012 | 0.3060 | ±0.6119 | -0.331 | 0.7407 |  |
| Time < 70 (%) | +0.0774 | 0.1256 | ±0.2513 | +0.616 | 0.5380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, R² = **0.0887**, Adj R² = **0.0738**, F-statistic = **5.96** (p = **2.62e-09**), Residual SE = **2.552** on **673** df, AIC = **3239.4**, BIC = **3293.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3963** | 0.8104 | ±1.6208 | **+20.232** | **5.12e-91** | *** |
| Education: graduate level (vs college) | +0.2618 | 0.2057 | ±0.4113 | +1.273 | 0.2030 |  |
| **Education: high school or below (vs college)** | **-1.4125** | 0.4824 | ±0.9648 | **-2.928** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.0854 | 0.2725 | ±0.5450 | -0.313 | 0.7540 |  |
| Site: UW (vs UAB) | -0.1419 | 0.2750 | ±0.5500 | -0.516 | 0.6060 |  |
| **Age (years)** | **-0.0455** | 0.0097 | ±0.0195 | **-4.666** | **3.07e-06** | *** |
| BMI (kg/m2) | -0.0242 | 0.0143 | ±0.0285 | -1.697 | 0.0898 | . |
| Hypertension | -0.4082 | 0.2255 | ±0.4511 | -1.810 | 0.0703 | . |
| High cholesterol | -0.0274 | 0.2117 | ±0.4233 | -0.130 | 0.8969 |  |
| Kidney disease | -0.3868 | 0.4796 | ±0.9593 | -0.807 | 0.4199 |  |
| Circulatory disease | -0.1002 | 0.3064 | ±0.6127 | -0.327 | 0.7436 |  |
| Avg. daily time < 70 (%) | +0.0728 | 0.1223 | ±0.2445 | +0.596 | 0.5513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, R² = **0.0976**, Adj R² = **0.0829**, F-statistic = **6.62** (p = **1.46e-10**), Residual SE = **2.540** on **673** df, AIC = **3232.7**, BIC = **3287.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4127** | 0.8099 | ±1.6199 | **+20.264** | **2.65e-91** | *** |
| Education: graduate level (vs college) | +0.2680 | 0.2031 | ±0.4061 | +1.320 | 0.1869 |  |
| **Education: high school or below (vs college)** | **-1.4133** | 0.4821 | ±0.9642 | **-2.931** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.1240 | 0.2627 | ±0.5254 | -0.472 | 0.6369 |  |
| Site: UW (vs UAB) | -0.1167 | 0.2782 | ±0.5565 | -0.419 | 0.6750 |  |
| **Age (years)** | **-0.0439** | 0.0099 | ±0.0198 | **-4.432** | **9.32e-06** | *** |
| BMI (kg/m2) | -0.0226 | 0.0145 | ±0.0289 | -1.559 | 0.1191 |  |
| Hypertension | -0.3998 | 0.2266 | ±0.4533 | -1.764 | 0.0777 | . |
| High cholesterol | -0.0002 | 0.2129 | ±0.4258 | -0.001 | 0.9993 |  |
| Kidney disease | -0.3583 | 0.4689 | ±0.9378 | -0.764 | 0.4448 |  |
| Circulatory disease | -0.0656 | 0.3098 | ±0.6197 | -0.212 | 0.8323 |  |
| Time 181-250, pooled (%) | -0.0950 | 0.0626 | ±0.1251 | -1.518 | 0.1290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, R² = **0.0980**, Adj R² = **0.0833**, F-statistic = **6.65** (p = **1.29e-10**), Residual SE = **2.539** on **673** df, AIC = **3232.4**, BIC = **3286.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4059** | 0.8115 | ±1.6230 | **+20.216** | **7.04e-91** | *** |
| Education: graduate level (vs college) | +0.2701 | 0.2030 | ±0.4060 | +1.331 | 0.1834 |  |
| **Education: high school or below (vs college)** | **-1.4159** | 0.4813 | ±0.9627 | **-2.941** | **0.0033** | ** |
| Site: UCSD (vs UAB) | -0.1281 | 0.2624 | ±0.5249 | -0.488 | 0.6255 |  |
| Site: UW (vs UAB) | -0.1200 | 0.2775 | ±0.5549 | -0.432 | 0.6654 |  |
| **Age (years)** | **-0.0441** | 0.0099 | ±0.0198 | **-4.461** | **8.17e-06** | *** |
| BMI (kg/m2) | -0.0220 | 0.0146 | ±0.0291 | -1.514 | 0.1301 |  |
| Hypertension | -0.4028 | 0.2266 | ±0.4533 | -1.778 | 0.0755 | . |
| High cholesterol | +0.0014 | 0.2128 | ±0.4256 | +0.006 | 0.9949 |  |
| Kidney disease | -0.3538 | 0.4670 | ±0.9340 | -0.758 | 0.4486 |  |
| Circulatory disease | -0.0567 | 0.3106 | ±0.6211 | -0.182 | 0.8552 |  |
| Avg. daily time 181-250 (%) | -0.0992 | 0.0634 | ±0.1267 | -1.566 | 0.1175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, R² = **0.0976**, Adj R² = **0.0829**, F-statistic = **6.62** (p = **1.46e-10**), Residual SE = **2.540** on **673** df, AIC = **3232.7**, BIC = **3287.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4127** | 0.8099 | ±1.6199 | **+20.264** | **2.65e-91** | *** |
| Education: graduate level (vs college) | +0.2680 | 0.2031 | ±0.4061 | +1.320 | 0.1869 |  |
| **Education: high school or below (vs college)** | **-1.4133** | 0.4821 | ±0.9642 | **-2.931** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.1240 | 0.2627 | ±0.5254 | -0.472 | 0.6369 |  |
| Site: UW (vs UAB) | -0.1167 | 0.2782 | ±0.5565 | -0.419 | 0.6750 |  |
| **Age (years)** | **-0.0439** | 0.0099 | ±0.0198 | **-4.432** | **9.32e-06** | *** |
| BMI (kg/m2) | -0.0226 | 0.0145 | ±0.0289 | -1.559 | 0.1191 |  |
| Hypertension | -0.3998 | 0.2266 | ±0.4533 | -1.764 | 0.0777 | . |
| High cholesterol | -0.0002 | 0.2129 | ±0.4258 | -0.001 | 0.9993 |  |
| Kidney disease | -0.3583 | 0.4689 | ±0.9378 | -0.764 | 0.4448 |  |
| Circulatory disease | -0.0656 | 0.3098 | ±0.6197 | -0.212 | 0.8323 |  |
| Time > 180 (%) | -0.0950 | 0.0626 | ±0.1251 | -1.518 | 0.1290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, R² = **0.0980**, Adj R² = **0.0833**, F-statistic = **6.65** (p = **1.29e-10**), Residual SE = **2.539** on **673** df, AIC = **3232.4**, BIC = **3286.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4059** | 0.8115 | ±1.6230 | **+20.216** | **7.04e-91** | *** |
| Education: graduate level (vs college) | +0.2701 | 0.2030 | ±0.4060 | +1.331 | 0.1834 |  |
| **Education: high school or below (vs college)** | **-1.4159** | 0.4813 | ±0.9627 | **-2.941** | **0.0033** | ** |
| Site: UCSD (vs UAB) | -0.1281 | 0.2624 | ±0.5249 | -0.488 | 0.6255 |  |
| Site: UW (vs UAB) | -0.1200 | 0.2775 | ±0.5549 | -0.432 | 0.6654 |  |
| **Age (years)** | **-0.0441** | 0.0099 | ±0.0198 | **-4.461** | **8.17e-06** | *** |
| BMI (kg/m2) | -0.0220 | 0.0146 | ±0.0291 | -1.514 | 0.1301 |  |
| Hypertension | -0.4028 | 0.2266 | ±0.4533 | -1.778 | 0.0755 | . |
| High cholesterol | +0.0014 | 0.2128 | ±0.4256 | +0.006 | 0.9949 |  |
| Kidney disease | -0.3538 | 0.4670 | ±0.9340 | -0.758 | 0.4486 |  |
| Circulatory disease | -0.0567 | 0.3106 | ±0.6211 | -0.182 | 0.8552 |  |
| Avg. daily time > 180 (%) | -0.0992 | 0.0634 | ±0.1267 | -1.566 | 0.1175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, R² = **0.0892**, Adj R² = **0.0743**, F-statistic = **5.99** (p = **2.26e-09**), Residual SE = **2.551** on **673** df, AIC = **3239.1**, BIC = **3293.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4094** | 0.8104 | ±1.6208 | **+20.248** | **3.67e-91** | *** |
| Education: graduate level (vs college) | +0.2509 | 0.2050 | ±0.4100 | +1.224 | 0.2209 |  |
| **Education: high school or below (vs college)** | **-1.4162** | 0.4815 | ±0.9630 | **-2.941** | **0.0033** | ** |
| Site: UCSD (vs UAB) | -0.0867 | 0.2721 | ±0.5441 | -0.319 | 0.7501 |  |
| Site: UW (vs UAB) | -0.1379 | 0.2753 | ±0.5506 | -0.501 | 0.6165 |  |
| **Age (years)** | **-0.0457** | 0.0097 | ±0.0195 | **-4.693** | **2.69e-06** | *** |
| BMI (kg/m2) | -0.0229 | 0.0145 | ±0.0290 | -1.583 | 0.1135 |  |
| Hypertension | -0.4120 | 0.2258 | ±0.4516 | -1.825 | 0.0681 | . |
| High cholesterol | -0.0105 | 0.2106 | ±0.4212 | -0.050 | 0.9603 |  |
| Kidney disease | -0.3904 | 0.4793 | ±0.9586 | -0.814 | 0.4154 |  |
| Circulatory disease | -0.1068 | 0.3055 | ±0.6110 | -0.350 | 0.7266 |  |
| Nocturnal time > 180 (%) | -0.0229 | 0.0399 | ±0.0799 | -0.574 | 0.5660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
