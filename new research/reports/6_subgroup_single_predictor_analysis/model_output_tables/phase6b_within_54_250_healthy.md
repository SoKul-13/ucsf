# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 685; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0571**, F-statistic = **5.14** (p = **2.88e-07**), Residual SE = **4.445** on **674** df, AIC = **3998.7**, BIC = **4048.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4667** | 1.3977 | ±2.7953 | **+6.058** | **1.38e-09** | *** |
| Education: graduate level (vs college) | -0.3027 | 0.3685 | ±0.7371 | -0.821 | 0.4115 |  |
| Education: high school or below (vs college) | +0.4970 | 0.7603 | ±1.5206 | +0.654 | 0.5133 |  |
| Site: UCSD (vs UAB) | -0.5737 | 0.4671 | ±0.9343 | -1.228 | 0.2194 |  |
| Site: UW (vs UAB) | -0.2200 | 0.4629 | ±0.9257 | -0.475 | 0.6346 |  |
| **Age (years)** | **-0.0841** | 0.0166 | ±0.0332 | **-5.059** | **4.21e-07** | *** |
| **BMI (kg/m2)** | **+0.0608** | 0.0282 | ±0.0563 | **+2.160** | **0.0308** | * |
| Hypertension | +0.4795 | 0.3992 | ±0.7983 | +1.201 | 0.2296 |  |
| High cholesterol | +0.6697 | 0.3550 | ±0.7099 | +1.887 | 0.0592 | . |
| Kidney disease | +1.0134 | 0.8449 | ±1.6898 | +1.199 | 0.2303 |  |
| Circulatory disease | +0.7221 | 0.6050 | ±1.2100 | +1.194 | 0.2326 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.79e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.8277** | 3.0899 | ±6.1798 | **+2.857** | **0.0043** | ** |
| Education: graduate level (vs college) | -0.3017 | 0.3710 | ±0.7419 | -0.813 | 0.4160 |  |
| Education: high school or below (vs college) | +0.4975 | 0.7621 | ±1.5242 | +0.653 | 0.5139 |  |
| Site: UCSD (vs UAB) | -0.5737 | 0.4679 | ±0.9359 | -1.226 | 0.2202 |  |
| Site: UW (vs UAB) | -0.2191 | 0.4636 | ±0.9272 | -0.473 | 0.6365 |  |
| **Age (years)** | **-0.0839** | 0.0169 | ±0.0338 | **-4.959** | **7.09e-07** | *** |
| **BMI (kg/m2)** | **+0.0613** | 0.0286 | ±0.0572 | **+2.145** | **0.0320** | * |
| Hypertension | +0.4839 | 0.4001 | ±0.8002 | +1.209 | 0.2265 |  |
| High cholesterol | +0.6743 | 0.3584 | ±0.7169 | +1.881 | 0.0599 | . |
| Kidney disease | +1.0131 | 0.8486 | ±1.6972 | +1.194 | 0.2325 |  |
| Circulatory disease | +0.7206 | 0.6054 | ±1.2107 | +1.190 | 0.2339 |  |
| HbA1c (%) | -0.0706 | 0.5632 | ±1.1265 | -0.125 | 0.9003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0561**, F-statistic = **4.69** (p = **6.08e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.3659** | 2.2468 | ±4.4936 | **+4.168** | **3.07e-05** | *** |
| Education: graduate level (vs college) | -0.2901 | 0.3701 | ±0.7402 | -0.784 | 0.4332 |  |
| Education: high school or below (vs college) | +0.5071 | 0.7618 | ±1.5236 | +0.666 | 0.5056 |  |
| Site: UCSD (vs UAB) | -0.5830 | 0.4671 | ±0.9342 | -1.248 | 0.2120 |  |
| Site: UW (vs UAB) | -0.2037 | 0.4665 | ±0.9330 | -0.437 | 0.6624 |  |
| **Age (years)** | **-0.0837** | 0.0167 | ±0.0334 | **-5.010** | **5.45e-07** | *** |
| **BMI (kg/m2)** | **+0.0623** | 0.0281 | ±0.0563 | **+2.215** | **0.0267** | * |
| Hypertension | +0.4924 | 0.4005 | ±0.8009 | +1.230 | 0.2189 |  |
| High cholesterol | +0.6687 | 0.3555 | ±0.7110 | +1.881 | 0.0599 | . |
| Kidney disease | +1.0284 | 0.8432 | ±1.6864 | +1.220 | 0.2226 |  |
| Circulatory disease | +0.7407 | 0.6053 | ±1.2107 | +1.224 | 0.2211 |  |
| Mean glucose (mg/dL) | -0.0083 | 0.0162 | ±0.0325 | -0.510 | 0.6103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0561**, F-statistic = **4.69** (p = **6.08e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.5107** | 4.2419 | ±8.4837 | **+2.478** | **0.0132** | * |
| Education: graduate level (vs college) | -0.2901 | 0.3701 | ±0.7402 | -0.784 | 0.4332 |  |
| Education: high school or below (vs college) | +0.5071 | 0.7618 | ±1.5236 | +0.666 | 0.5056 |  |
| Site: UCSD (vs UAB) | -0.5830 | 0.4671 | ±0.9342 | -1.248 | 0.2120 |  |
| Site: UW (vs UAB) | -0.2037 | 0.4665 | ±0.9330 | -0.437 | 0.6624 |  |
| **Age (years)** | **-0.0837** | 0.0167 | ±0.0334 | **-5.010** | **5.45e-07** | *** |
| **BMI (kg/m2)** | **+0.0623** | 0.0281 | ±0.0563 | **+2.215** | **0.0267** | * |
| Hypertension | +0.4924 | 0.4005 | ±0.8009 | +1.230 | 0.2189 |  |
| High cholesterol | +0.6687 | 0.3555 | ±0.7110 | +1.881 | 0.0599 | . |
| Kidney disease | +1.0284 | 0.8432 | ±1.6864 | +1.220 | 0.2226 |  |
| Circulatory disease | +0.7407 | 0.6053 | ±1.2107 | +1.224 | 0.2211 |  |
| GMI (%) | -0.3459 | 0.6787 | ±1.3574 | -0.510 | 0.6103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.75e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7343** | 2.1023 | ±4.2045 | **+4.155** | **3.26e-05** | *** |
| Education: graduate level (vs college) | -0.3001 | 0.3702 | ±0.7404 | -0.811 | 0.4175 |  |
| Education: high school or below (vs college) | +0.4995 | 0.7628 | ±1.5256 | +0.655 | 0.5126 |  |
| Site: UCSD (vs UAB) | -0.5736 | 0.4681 | ±0.9362 | -1.225 | 0.2204 |  |
| Site: UW (vs UAB) | -0.2144 | 0.4657 | ±0.9314 | -0.460 | 0.6453 |  |
| **Age (years)** | **-0.0842** | 0.0166 | ±0.0332 | **-5.071** | **3.95e-07** | *** |
| **BMI (kg/m2)** | **+0.0619** | 0.0285 | ±0.0569 | **+2.174** | **0.0297** | * |
| Hypertension | +0.4817 | 0.3993 | ±0.7986 | +1.206 | 0.2277 |  |
| High cholesterol | +0.6721 | 0.3561 | ±0.7122 | +1.887 | 0.0591 | . |
| Kidney disease | +1.0160 | 0.8445 | ±1.6889 | +1.203 | 0.2289 |  |
| Circulatory disease | +0.7268 | 0.6062 | ±1.2123 | +1.199 | 0.2305 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0025 | 0.0149 | ±0.0298 | -0.168 | 0.8669 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.83e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5132** | 1.5724 | ±3.1449 | **+5.414** | **6.16e-08** | *** |
| Education: graduate level (vs college) | -0.3037 | 0.3687 | ±0.7374 | -0.824 | 0.4100 |  |
| Education: high school or below (vs college) | +0.4979 | 0.7612 | ±1.5225 | +0.654 | 0.5130 |  |
| Site: UCSD (vs UAB) | -0.5753 | 0.4684 | ±0.9368 | -1.228 | 0.2194 |  |
| Site: UW (vs UAB) | -0.2186 | 0.4650 | ±0.9299 | -0.470 | 0.6382 |  |
| **Age (years)** | **-0.0840** | 0.0168 | ±0.0336 | **-5.000** | **5.73e-07** | *** |
| **BMI (kg/m2)** | **+0.0609** | 0.0282 | ±0.0565 | **+2.158** | **0.0309** | * |
| Hypertension | +0.4809 | 0.4005 | ±0.8009 | +1.201 | 0.2298 |  |
| High cholesterol | +0.6699 | 0.3558 | ±0.7115 | +1.883 | 0.0597 | . |
| Kidney disease | +1.0147 | 0.8439 | ±1.6878 | +1.202 | 0.2292 |  |
| Circulatory disease | +0.7218 | 0.6054 | ±1.2107 | +1.192 | 0.2331 |  |
| Glucose SD, pooled (mg/dL) | -0.0029 | 0.0473 | ±0.0946 | -0.060 | 0.9519 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0710**, Adj R² = **0.0558**, F-statistic = **4.68** (p = **6.49e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7090** | 1.5467 | ±3.0934 | **+5.631** | **1.80e-08** | *** |
| Education: graduate level (vs college) | -0.3062 | 0.3686 | ±0.7372 | -0.831 | 0.4061 |  |
| Education: high school or below (vs college) | +0.5030 | 0.7611 | ±1.5222 | +0.661 | 0.5087 |  |
| Site: UCSD (vs UAB) | -0.5845 | 0.4678 | ±0.9357 | -1.249 | 0.2116 |  |
| Site: UW (vs UAB) | -0.2123 | 0.4652 | ±0.9304 | -0.456 | 0.6481 |  |
| **Age (years)** | **-0.0835** | 0.0168 | ±0.0335 | **-4.983** | **6.25e-07** | *** |
| **BMI (kg/m2)** | **+0.0614** | 0.0283 | ±0.0565 | **+2.172** | **0.0299** | * |
| Hypertension | +0.4864 | 0.4005 | ±0.8009 | +1.215 | 0.2245 |  |
| High cholesterol | +0.6699 | 0.3555 | ±0.7110 | +1.885 | 0.0595 | . |
| Kidney disease | +1.0232 | 0.8450 | ±1.6900 | +1.211 | 0.2259 |  |
| Circulatory disease | +0.7214 | 0.6051 | ±1.2102 | +1.192 | 0.2332 |  |
| Avg. daily SD (mg/dL) | -0.0166 | 0.0483 | ±0.0966 | -0.344 | 0.7306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.72e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2706** | 1.6603 | ±3.3207 | **+4.981** | **6.31e-07** | *** |
| Education: graduate level (vs college) | -0.2956 | 0.3692 | ±0.7385 | -0.801 | 0.4233 |  |
| Education: high school or below (vs college) | +0.4960 | 0.7607 | ±1.5214 | +0.652 | 0.5144 |  |
| Site: UCSD (vs UAB) | -0.5693 | 0.4689 | ±0.9378 | -1.214 | 0.2247 |  |
| Site: UW (vs UAB) | -0.2217 | 0.4639 | ±0.9277 | -0.478 | 0.6326 |  |
| **Age (years)** | **-0.0844** | 0.0167 | ±0.0335 | **-5.043** | **4.59e-07** | *** |
| **BMI (kg/m2)** | **+0.0609** | 0.0282 | ±0.0564 | **+2.160** | **0.0308** | * |
| Hypertension | +0.4766 | 0.3998 | ±0.7997 | +1.192 | 0.2333 |  |
| High cholesterol | +0.6693 | 0.3556 | ±0.7112 | +1.882 | 0.0598 | . |
| Kidney disease | +1.0112 | 0.8439 | ±1.6878 | +1.198 | 0.2308 |  |
| Circulatory disease | +0.7272 | 0.6046 | ±1.2092 | +1.203 | 0.2291 |  |
| CV (%) | +0.0129 | 0.0621 | ±0.1242 | +0.208 | 0.8356 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.76e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6388** | 1.7552 | ±3.5103 | **+4.922** | **8.57e-07** | *** |
| Education: graduate level (vs college) | -0.2967 | 0.3698 | ±0.7396 | -0.802 | 0.4224 |  |
| Education: high school or below (vs college) | +0.4955 | 0.7605 | ±1.5210 | +0.652 | 0.5147 |  |
| Site: UCSD (vs UAB) | -0.5713 | 0.4683 | ±0.9366 | -1.220 | 0.2225 |  |
| Site: UW (vs UAB) | -0.2225 | 0.4641 | ±0.9282 | -0.479 | 0.6317 |  |
| **Age (years)** | **-0.0843** | 0.0167 | ±0.0335 | **-5.036** | **4.76e-07** | *** |
| **BMI (kg/m2)** | **+0.0609** | 0.0282 | ±0.0564 | **+2.160** | **0.0308** | * |
| Hypertension | +0.4769 | 0.3996 | ±0.7991 | +1.194 | 0.2327 |  |
| High cholesterol | +0.6698 | 0.3554 | ±0.7108 | +1.885 | 0.0595 | . |
| Kidney disease | +1.0115 | 0.8439 | ±1.6878 | +1.199 | 0.2307 |  |
| Circulatory disease | +0.7263 | 0.6047 | ±1.2094 | +1.201 | 0.2297 |  |
| Mean / SD ratio | -0.0256 | 0.1467 | ±0.2934 | -0.175 | 0.8615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.17e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9804** | 1.7540 | ±3.5079 | **+4.550** | **5.37e-06** | *** |
| Education: graduate level (vs college) | -0.3164 | 0.3690 | ±0.7381 | -0.857 | 0.3912 |  |
| Education: high school or below (vs college) | +0.5025 | 0.7608 | ±1.5216 | +0.660 | 0.5089 |  |
| Site: UCSD (vs UAB) | -0.5826 | 0.4678 | ±0.9356 | -1.246 | 0.2129 |  |
| Site: UW (vs UAB) | -0.2115 | 0.4645 | ±0.9290 | -0.455 | 0.6488 |  |
| **Age (years)** | **-0.0835** | 0.0167 | ±0.0334 | **-4.993** | **5.93e-07** | *** |
| **BMI (kg/m2)** | **+0.0611** | 0.0283 | ±0.0565 | **+2.163** | **0.0305** | * |
| Hypertension | +0.4828 | 0.3998 | ±0.7996 | +1.208 | 0.2272 |  |
| High cholesterol | +0.6673 | 0.3551 | ±0.7102 | +1.879 | 0.0603 | . |
| Kidney disease | +1.0221 | 0.8470 | ±1.6939 | +1.207 | 0.2275 |  |
| Circulatory disease | +0.7110 | 0.6033 | ±1.2066 | +1.178 | 0.2386 |  |
| Avg. daily mean/SD | +0.0615 | 0.1242 | ±0.2484 | +0.495 | 0.6206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.41e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0936** | 1.5453 | ±3.0906 | **+5.237** | **1.63e-07** | *** |
| Education: graduate level (vs college) | -0.3021 | 0.3689 | ±0.7378 | -0.819 | 0.4129 |  |
| Education: high school or below (vs college) | +0.4795 | 0.7676 | ±1.5352 | +0.625 | 0.5322 |  |
| Site: UCSD (vs UAB) | -0.5696 | 0.4677 | ±0.9354 | -1.218 | 0.2233 |  |
| Site: UW (vs UAB) | -0.2183 | 0.4633 | ±0.9267 | -0.471 | 0.6376 |  |
| **Age (years)** | **-0.0840** | 0.0166 | ±0.0333 | **-5.051** | **4.39e-07** | *** |
| **BMI (kg/m2)** | **+0.0610** | 0.0281 | ±0.0562 | **+2.171** | **0.0299** | * |
| Hypertension | +0.4861 | 0.3992 | ±0.7985 | +1.218 | 0.2234 |  |
| High cholesterol | +0.6715 | 0.3554 | ±0.7109 | +1.889 | 0.0589 | . |
| Kidney disease | +1.0035 | 0.8420 | ±1.6841 | +1.192 | 0.2333 |  |
| Circulatory disease | +0.7261 | 0.6068 | ±1.2135 | +1.197 | 0.2315 |  |
| MAG (mg/dL/h) | +0.0101 | 0.0244 | ±0.0487 | +0.413 | 0.6796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, R² = **0.0710**, Adj R² = **0.0558**, F-statistic = **4.68** (p = **6.56e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7471** | 1.6081 | ±3.2163 | **+5.439** | **5.35e-08** | *** |
| Education: graduate level (vs college) | -0.3022 | 0.3691 | ±0.7382 | -0.819 | 0.4129 |  |
| Education: high school or below (vs college) | +0.5061 | 0.7605 | ±1.5209 | +0.666 | 0.5057 |  |
| Site: UCSD (vs UAB) | -0.5791 | 0.4677 | ±0.9355 | -1.238 | 0.2157 |  |
| Site: UW (vs UAB) | -0.2135 | 0.4648 | ±0.9296 | -0.459 | 0.6460 |  |
| **Age (years)** | **-0.0837** | 0.0168 | ±0.0335 | **-4.995** | **5.89e-07** | *** |
| **BMI (kg/m2)** | **+0.0605** | 0.0283 | ±0.0565 | **+2.141** | **0.0323** | * |
| Hypertension | +0.4817 | 0.3998 | ±0.7996 | +1.205 | 0.2282 |  |
| High cholesterol | +0.6679 | 0.3549 | ±0.7099 | +1.882 | 0.0599 | . |
| Kidney disease | +1.0225 | 0.8441 | ±1.6881 | +1.211 | 0.2257 |  |
| Circulatory disease | +0.7241 | 0.6051 | ±1.2102 | +1.197 | 0.2314 |  |
| Avg. daily range (mg/dL) | -0.0034 | 0.0103 | ±0.0206 | -0.325 | 0.7452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, R² = **0.0712**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.12e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.4**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2819** | 1.4109 | ±2.8218 | **+5.870** | **4.36e-09** | *** |
| Education: graduate level (vs college) | -0.3001 | 0.3688 | ±0.7376 | -0.814 | 0.4158 |  |
| Education: high school or below (vs college) | +0.4942 | 0.7625 | ±1.5250 | +0.648 | 0.5169 |  |
| Site: UCSD (vs UAB) | -0.5708 | 0.4684 | ±0.9369 | -1.218 | 0.2230 |  |
| Site: UW (vs UAB) | -0.2256 | 0.4639 | ±0.9277 | -0.486 | 0.6268 |  |
| **Age (years)** | **-0.0841** | 0.0167 | ±0.0333 | **-5.050** | **4.43e-07** | *** |
| **BMI (kg/m2)** | **+0.0595** | 0.0284 | ±0.0567 | **+2.098** | **0.0359** | * |
| Hypertension | +0.4821 | 0.3996 | ±0.7991 | +1.207 | 0.2276 |  |
| High cholesterol | +0.6563 | 0.3591 | ±0.7181 | +1.828 | 0.0676 | . |
| Kidney disease | +1.0248 | 0.8493 | ±1.6987 | +1.207 | 0.2276 |  |
| Circulatory disease | +0.7196 | 0.6056 | ±1.2112 | +1.188 | 0.2347 |  |
| SD of daily means (mg/dL) | +0.0395 | 0.0743 | ±0.1486 | +0.532 | 0.5950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, R² = **0.0710**, Adj R² = **0.0558**, F-statistic = **4.68** (p = **6.50e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.6**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.7302 | 6.9089 | ±13.8177 | +1.553 | 0.1204 |  |
| Education: graduate level (vs college) | -0.3037 | 0.3691 | ±0.7382 | -0.823 | 0.4107 |  |
| Education: high school or below (vs college) | +0.4977 | 0.7611 | ±1.5223 | +0.654 | 0.5132 |  |
| Site: UCSD (vs UAB) | -0.5643 | 0.4690 | ±0.9379 | -1.203 | 0.2289 |  |
| Site: UW (vs UAB) | -0.2258 | 0.4637 | ±0.9273 | -0.487 | 0.6263 |  |
| **Age (years)** | **-0.0845** | 0.0167 | ±0.0334 | **-5.060** | **4.19e-07** | *** |
| **BMI (kg/m2)** | **+0.0605** | 0.0282 | ±0.0564 | **+2.146** | **0.0319** | * |
| Hypertension | +0.4774 | 0.4000 | ±0.7999 | +1.194 | 0.2327 |  |
| High cholesterol | +0.6630 | 0.3562 | ±0.7123 | +1.862 | 0.0627 | . |
| Kidney disease | +1.0068 | 0.8458 | ±1.6916 | +1.190 | 0.2339 |  |
| Circulatory disease | +0.7139 | 0.6066 | ±1.2131 | +1.177 | 0.2392 |  |
| Time in range 70-180, pooled (%) | -0.0227 | 0.0681 | ±0.1362 | -0.333 | 0.7389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.81e-07**), Residual SE = **4.449** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +9.2087 | 7.1295 | ±14.2590 | +1.292 | 0.1965 |  |
| Education: graduate level (vs college) | -0.3030 | 0.3690 | ±0.7381 | -0.821 | 0.4116 |  |
| Education: high school or below (vs college) | +0.4976 | 0.7612 | ±1.5224 | +0.654 | 0.5133 |  |
| Site: UCSD (vs UAB) | -0.5706 | 0.4688 | ±0.9376 | -1.217 | 0.2235 |  |
| Site: UW (vs UAB) | -0.2216 | 0.4635 | ±0.9270 | -0.478 | 0.6326 |  |
| **Age (years)** | **-0.0842** | 0.0167 | ±0.0334 | **-5.049** | **4.44e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.154** | **0.0312** | * |
| Hypertension | +0.4791 | 0.3999 | ±0.7997 | +1.198 | 0.2309 |  |
| High cholesterol | +0.6675 | 0.3562 | ±0.7124 | +1.874 | 0.0609 | . |
| Kidney disease | +1.0110 | 0.8454 | ±1.6909 | +1.196 | 0.2318 |  |
| Circulatory disease | +0.7191 | 0.6066 | ±1.2133 | +1.185 | 0.2359 |  |
| Avg. daily time in range 70-180 (%) | -0.0074 | 0.0703 | ±0.1406 | -0.106 | 0.9158 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.28e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5181** | 1.4025 | ±2.8051 | **+6.073** | **1.25e-09** | *** |
| Education: graduate level (vs college) | -0.3207 | 0.3727 | ±0.7454 | -0.860 | 0.3895 |  |
| Education: high school or below (vs college) | +0.4754 | 0.7628 | ±1.5256 | +0.623 | 0.5331 |  |
| Site: UCSD (vs UAB) | -0.5672 | 0.4667 | ±0.9335 | -1.215 | 0.2242 |  |
| Site: UW (vs UAB) | -0.2247 | 0.4630 | ±0.9260 | -0.485 | 0.6274 |  |
| **Age (years)** | **-0.0842** | 0.0166 | ±0.0333 | **-5.062** | **4.15e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4812 | 0.3999 | ±0.7997 | +1.203 | 0.2288 |  |
| High cholesterol | +0.6744 | 0.3553 | ±0.7106 | +1.898 | 0.0577 | . |
| Kidney disease | +1.0094 | 0.8476 | ±1.6952 | +1.191 | 0.2337 |  |
| Circulatory disease | +0.7118 | 0.6042 | ±1.2085 | +1.178 | 0.2388 |  |
| Time 54-69, pooled (%) | -0.1499 | 0.3294 | ±0.6588 | -0.455 | 0.6490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.37e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5082** | 1.4013 | ±2.8025 | **+6.072** | **1.26e-09** | *** |
| Education: graduate level (vs college) | -0.3196 | 0.3724 | ±0.7448 | -0.858 | 0.3907 |  |
| Education: high school or below (vs college) | +0.4762 | 0.7631 | ±1.5261 | +0.624 | 0.5326 |  |
| Site: UCSD (vs UAB) | -0.5649 | 0.4663 | ±0.9325 | -1.212 | 0.2257 |  |
| Site: UW (vs UAB) | -0.2234 | 0.4631 | ±0.9261 | -0.482 | 0.6295 |  |
| **Age (years)** | **-0.0841** | 0.0166 | ±0.0333 | **-5.057** | **4.25e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4804 | 0.3998 | ±0.7996 | +1.202 | 0.2296 |  |
| High cholesterol | +0.6734 | 0.3555 | ±0.7109 | +1.894 | 0.0582 | . |
| Kidney disease | +1.0104 | 0.8471 | ±1.6942 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7106 | 0.6046 | ±1.2092 | +1.175 | 0.2399 |  |
| Avg. daily time 54-69 (%) | -0.1325 | 0.3334 | ±0.6667 | -0.398 | 0.6910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0560**, F-statistic = **4.69** (p = **6.28e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5181** | 1.4025 | ±2.8051 | **+6.073** | **1.25e-09** | *** |
| Education: graduate level (vs college) | -0.3207 | 0.3727 | ±0.7454 | -0.860 | 0.3895 |  |
| Education: high school or below (vs college) | +0.4754 | 0.7628 | ±1.5256 | +0.623 | 0.5331 |  |
| Site: UCSD (vs UAB) | -0.5672 | 0.4667 | ±0.9335 | -1.215 | 0.2242 |  |
| Site: UW (vs UAB) | -0.2247 | 0.4630 | ±0.9260 | -0.485 | 0.6274 |  |
| **Age (years)** | **-0.0842** | 0.0166 | ±0.0333 | **-5.062** | **4.15e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4812 | 0.3999 | ±0.7997 | +1.203 | 0.2288 |  |
| High cholesterol | +0.6744 | 0.3553 | ±0.7106 | +1.898 | 0.0577 | . |
| Kidney disease | +1.0094 | 0.8476 | ±1.6952 | +1.191 | 0.2337 |  |
| Circulatory disease | +0.7118 | 0.6042 | ±1.2085 | +1.178 | 0.2388 |  |
| Time < 70 (%) | -0.1499 | 0.3294 | ±0.6588 | -0.455 | 0.6490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.37e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5082** | 1.4013 | ±2.8025 | **+6.072** | **1.26e-09** | *** |
| Education: graduate level (vs college) | -0.3196 | 0.3724 | ±0.7448 | -0.858 | 0.3907 |  |
| Education: high school or below (vs college) | +0.4762 | 0.7631 | ±1.5261 | +0.624 | 0.5326 |  |
| Site: UCSD (vs UAB) | -0.5649 | 0.4663 | ±0.9325 | -1.212 | 0.2257 |  |
| Site: UW (vs UAB) | -0.2234 | 0.4631 | ±0.9261 | -0.482 | 0.6295 |  |
| **Age (years)** | **-0.0841** | 0.0166 | ±0.0333 | **-5.057** | **4.25e-07** | *** |
| **BMI (kg/m2)** | **+0.0607** | 0.0282 | ±0.0564 | **+2.152** | **0.0314** | * |
| Hypertension | +0.4804 | 0.3998 | ±0.7996 | +1.202 | 0.2296 |  |
| High cholesterol | +0.6734 | 0.3555 | ±0.7109 | +1.894 | 0.0582 | . |
| Kidney disease | +1.0104 | 0.8471 | ±1.6942 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7106 | 0.6046 | ±1.2092 | +1.175 | 0.2399 |  |
| Avg. daily time < 70 (%) | -0.1325 | 0.3334 | ±0.6667 | -0.398 | 0.6910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.32e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4686** | 1.4000 | ±2.7999 | **+6.049** | **1.46e-09** | *** |
| Education: graduate level (vs college) | -0.3073 | 0.3695 | ±0.7390 | -0.832 | 0.4057 |  |
| Education: high school or below (vs college) | +0.4939 | 0.7613 | ±1.5226 | +0.649 | 0.5165 |  |
| Site: UCSD (vs UAB) | -0.5608 | 0.4688 | ±0.9377 | -1.196 | 0.2316 |  |
| Site: UW (vs UAB) | -0.2280 | 0.4638 | ±0.9276 | -0.492 | 0.6230 |  |
| **Age (years)** | **-0.0846** | 0.0167 | ±0.0334 | **-5.066** | **4.06e-07** | *** |
| **BMI (kg/m2)** | **+0.0603** | 0.0282 | ±0.0564 | **+2.141** | **0.0322** | * |
| Hypertension | +0.4772 | 0.3999 | ±0.7998 | +1.193 | 0.2328 |  |
| High cholesterol | +0.6623 | 0.3561 | ±0.7122 | +1.860 | 0.0629 | . |
| Kidney disease | +1.0045 | 0.8464 | ±1.6928 | +1.187 | 0.2353 |  |
| Circulatory disease | +0.7100 | 0.6065 | ±1.2130 | +1.171 | 0.2417 |  |
| Time 181-250, pooled (%) | +0.0281 | 0.0674 | ±0.1349 | +0.416 | 0.6773 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.73e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4684** | 1.3992 | ±2.7985 | **+6.052** | **1.43e-09** | *** |
| Education: graduate level (vs college) | -0.3050 | 0.3695 | ±0.7389 | -0.825 | 0.4091 |  |
| Education: high school or below (vs college) | +0.4960 | 0.7612 | ±1.5224 | +0.652 | 0.5147 |  |
| Site: UCSD (vs UAB) | -0.5675 | 0.4687 | ±0.9374 | -1.211 | 0.2260 |  |
| Site: UW (vs UAB) | -0.2231 | 0.4637 | ±0.9274 | -0.481 | 0.6304 |  |
| **Age (years)** | **-0.0843** | 0.0167 | ±0.0334 | **-5.054** | **4.32e-07** | *** |
| **BMI (kg/m2)** | **+0.0606** | 0.0282 | ±0.0564 | **+2.149** | **0.0316** | * |
| Hypertension | +0.4789 | 0.3999 | ±0.7997 | +1.198 | 0.2311 |  |
| High cholesterol | +0.6662 | 0.3561 | ±0.7123 | +1.871 | 0.0614 | . |
| Kidney disease | +1.0089 | 0.8459 | ±1.6918 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7157 | 0.6068 | ±1.2135 | +1.179 | 0.2382 |  |
| Avg. daily time 181-250 (%) | +0.0129 | 0.0698 | ±0.1396 | +0.185 | 0.8532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, R² = **0.0711**, Adj R² = **0.0559**, F-statistic = **4.68** (p = **6.32e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.5**, BIC = **4054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4686** | 1.4000 | ±2.7999 | **+6.049** | **1.46e-09** | *** |
| Education: graduate level (vs college) | -0.3073 | 0.3695 | ±0.7390 | -0.832 | 0.4057 |  |
| Education: high school or below (vs college) | +0.4939 | 0.7613 | ±1.5226 | +0.649 | 0.5165 |  |
| Site: UCSD (vs UAB) | -0.5608 | 0.4688 | ±0.9377 | -1.196 | 0.2316 |  |
| Site: UW (vs UAB) | -0.2280 | 0.4638 | ±0.9276 | -0.492 | 0.6230 |  |
| **Age (years)** | **-0.0846** | 0.0167 | ±0.0334 | **-5.066** | **4.06e-07** | *** |
| **BMI (kg/m2)** | **+0.0603** | 0.0282 | ±0.0564 | **+2.141** | **0.0322** | * |
| Hypertension | +0.4772 | 0.3999 | ±0.7998 | +1.193 | 0.2328 |  |
| High cholesterol | +0.6623 | 0.3561 | ±0.7122 | +1.860 | 0.0629 | . |
| Kidney disease | +1.0045 | 0.8464 | ±1.6928 | +1.187 | 0.2353 |  |
| Circulatory disease | +0.7100 | 0.6065 | ±1.2130 | +1.171 | 0.2417 |  |
| Time > 180 (%) | +0.0281 | 0.0674 | ±0.1349 | +0.416 | 0.6773 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, R² = **0.0709**, Adj R² = **0.0557**, F-statistic = **4.67** (p = **6.73e-07**), Residual SE = **4.448** on **673** df, AIC = **4000.7**, BIC = **4055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4684** | 1.3992 | ±2.7985 | **+6.052** | **1.43e-09** | *** |
| Education: graduate level (vs college) | -0.3050 | 0.3695 | ±0.7389 | -0.825 | 0.4091 |  |
| Education: high school or below (vs college) | +0.4960 | 0.7612 | ±1.5224 | +0.652 | 0.5147 |  |
| Site: UCSD (vs UAB) | -0.5675 | 0.4687 | ±0.9374 | -1.211 | 0.2260 |  |
| Site: UW (vs UAB) | -0.2231 | 0.4637 | ±0.9274 | -0.481 | 0.6304 |  |
| **Age (years)** | **-0.0843** | 0.0167 | ±0.0334 | **-5.054** | **4.32e-07** | *** |
| **BMI (kg/m2)** | **+0.0606** | 0.0282 | ±0.0564 | **+2.149** | **0.0316** | * |
| Hypertension | +0.4789 | 0.3999 | ±0.7997 | +1.198 | 0.2311 |  |
| High cholesterol | +0.6662 | 0.3561 | ±0.7123 | +1.871 | 0.0614 | . |
| Kidney disease | +1.0089 | 0.8459 | ±1.6918 | +1.193 | 0.2330 |  |
| Circulatory disease | +0.7157 | 0.6068 | ±1.2135 | +1.179 | 0.2382 |  |
| Avg. daily time > 180 (%) | +0.0129 | 0.0698 | ±0.1396 | +0.185 | 0.8532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, R² = **0.0776**, Adj R² = **0.0626**, F-statistic = **5.15** (p = **8.59e-08**), Residual SE = **4.432** on **673** df, AIC = **3995.7**, BIC = **4050.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5202** | 1.3918 | ±2.7836 | **+6.122** | **9.25e-10** | *** |
| Education: graduate level (vs college) | -0.2940 | 0.3678 | ±0.7356 | -0.799 | 0.4240 |  |
| Education: high school or below (vs college) | +0.4547 | 0.7618 | ±1.5236 | +0.597 | 0.5506 |  |
| Site: UCSD (vs UAB) | -0.5404 | 0.4681 | ±0.9362 | -1.154 | 0.2484 |  |
| Site: UW (vs UAB) | -0.2518 | 0.4624 | ±0.9247 | -0.545 | 0.5861 |  |
| **Age (years)** | **-0.0830** | 0.0167 | ±0.0334 | **-4.971** | **6.67e-07** | *** |
| BMI (kg/m2) | +0.0535 | 0.0279 | ±0.0557 | +1.920 | 0.0548 | . |
| Hypertension | +0.5028 | 0.3993 | ±0.7986 | +1.259 | 0.2080 |  |
| High cholesterol | +0.5881 | 0.3585 | ±0.7170 | +1.641 | 0.1009 |  |
| Kidney disease | +1.0234 | 0.8509 | ±1.7017 | +1.203 | 0.2291 |  |
| Circulatory disease | +0.7236 | 0.6008 | ±1.2015 | +1.204 | 0.2284 |  |
| **Nocturnal time > 180 (%)** | **+0.1253** | 0.0581 | ±0.1162 | **+2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 685; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **2.24e-06**), AUC = **0.6867**, AIC = **563.9**, BIC = **613.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0301 | 0.8467 | ±1.6934 | -0.036 | 0.9717 | 0.9704 |  |
| Education: graduate level (vs college) | -0.0419 | 0.2445 | ±0.4890 | -0.171 | 0.8639 | 0.9590 |  |
| Education: high school or below (vs college) | +0.3546 | 0.3670 | ±0.7339 | +0.966 | 0.3339 | 1.4256 |  |
| Site: UCSD (vs UAB) | -0.1112 | 0.3035 | ±0.6070 | -0.366 | 0.7141 | 0.8948 |  |
| Site: UW (vs UAB) | +0.1099 | 0.2842 | ±0.5683 | +0.387 | 0.6989 | 1.1162 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.873** | **1.10e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0153 | ±0.0306 | **+2.124** | **0.0337** | 1.0330 | * |
| Hypertension | +0.2834 | 0.2488 | ±0.4975 | +1.139 | 0.2546 | 1.3277 |  |
| **High cholesterol** | **+0.5988** | 0.2327 | ±0.4654 | **+2.573** | **0.0101** | 1.8199 | * |
| Kidney disease | +0.6240 | 0.3920 | ±0.7841 | +1.592 | 0.1114 | 1.8664 |  |
| Circulatory disease | +0.4209 | 0.3481 | ±0.6961 | +1.209 | 0.2265 | 1.5234 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **4.98e-06**), AUC = **0.6864**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1923 | 1.9544 | ±3.9088 | -0.098 | 0.9216 | 0.8250 |  |
| Education: graduate level (vs college) | -0.0415 | 0.2445 | ±0.4891 | -0.170 | 0.8653 | 0.9594 |  |
| Education: high school or below (vs college) | +0.3554 | 0.3670 | ±0.7341 | +0.968 | 0.3329 | 1.4268 |  |
| Site: UCSD (vs UAB) | -0.1104 | 0.3037 | ±0.6074 | -0.364 | 0.7162 | 0.8955 |  |
| Site: UW (vs UAB) | +0.1094 | 0.2843 | ±0.5685 | +0.385 | 0.7003 | 1.1156 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0222 | **-4.860** | **1.17e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0323** | 0.0155 | ±0.0310 | **+2.085** | **0.0370** | 1.0328 | * |
| Hypertension | +0.2808 | 0.2504 | ±0.5007 | +1.122 | 0.2621 | 1.3242 |  |
| **High cholesterol** | **+0.5967** | 0.2338 | ±0.4676 | **+2.552** | **0.0107** | 1.8161 | * |
| Kidney disease | +0.6231 | 0.3921 | ±0.7843 | +1.589 | 0.1120 | 1.8648 |  |
| Circulatory disease | +0.4226 | 0.3485 | ±0.6969 | +1.213 | 0.2253 | 1.5259 |  |
| HbA1c (%) | +0.0314 | 0.3412 | ±0.6825 | +0.092 | 0.9266 | 1.0319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0770**, LLR χ² = **45.20** (p = **4.48e-06**), AUC = **0.6873**, AIC = **565.7**, BIC = **620.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5885 | 1.3637 | ±2.7274 | -0.432 | 0.6660 | 0.5551 |  |
| Education: graduate level (vs college) | -0.0485 | 0.2450 | ±0.4901 | -0.198 | 0.8432 | 0.9527 |  |
| Education: high school or below (vs college) | +0.3499 | 0.3668 | ±0.7335 | +0.954 | 0.3401 | 1.4189 |  |
| Site: UCSD (vs UAB) | -0.1045 | 0.3039 | ±0.6077 | -0.344 | 0.7310 | 0.9008 |  |
| Site: UW (vs UAB) | +0.0990 | 0.2849 | ±0.5697 | +0.348 | 0.7281 | 1.1041 |  |
| **Age (years)** | **-0.0541** | 0.0111 | ±0.0221 | **-4.891** | **1.01e-06** | 0.9473 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0154 | ±0.0309 | **+2.047** | **0.0407** | 1.0321 | * |
| Hypertension | +0.2785 | 0.2490 | ±0.4979 | +1.119 | 0.2632 | 1.3212 |  |
| **High cholesterol** | **+0.5952** | 0.2328 | ±0.4656 | **+2.557** | **0.0106** | 1.8134 | * |
| Kidney disease | +0.6094 | 0.3933 | ±0.7866 | +1.550 | 0.1213 | 1.8394 |  |
| Circulatory disease | +0.4113 | 0.3486 | ±0.6971 | +1.180 | 0.2380 | 1.5087 |  |
| Mean glucose (mg/dL) | +0.0051 | 0.0098 | ±0.0195 | +0.523 | 0.6009 | 1.0051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0770**, LLR χ² = **45.20** (p = **4.48e-06**), AUC = **0.6873**, AIC = **565.7**, BIC = **620.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2960 | 2.5648 | ±5.1297 | -0.505 | 0.6133 | 0.2736 |  |
| Education: graduate level (vs college) | -0.0485 | 0.2450 | ±0.4901 | -0.198 | 0.8432 | 0.9527 |  |
| Education: high school or below (vs college) | +0.3499 | 0.3668 | ±0.7335 | +0.954 | 0.3401 | 1.4189 |  |
| Site: UCSD (vs UAB) | -0.1045 | 0.3039 | ±0.6077 | -0.344 | 0.7310 | 0.9008 |  |
| Site: UW (vs UAB) | +0.0990 | 0.2849 | ±0.5697 | +0.348 | 0.7281 | 1.1041 |  |
| **Age (years)** | **-0.0541** | 0.0111 | ±0.0221 | **-4.891** | **1.01e-06** | 0.9473 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0154 | ±0.0309 | **+2.047** | **0.0407** | 1.0321 | * |
| Hypertension | +0.2785 | 0.2490 | ±0.4979 | +1.119 | 0.2632 | 1.3212 |  |
| **High cholesterol** | **+0.5952** | 0.2328 | ±0.4656 | **+2.557** | **0.0106** | 1.8134 | * |
| Kidney disease | +0.6094 | 0.3933 | ±0.7866 | +1.550 | 0.1213 | 1.8394 |  |
| Circulatory disease | +0.4113 | 0.3486 | ±0.6971 | +1.180 | 0.2380 | 1.5087 |  |
| GMI (%) | +0.2137 | 0.4086 | ±0.8172 | +0.523 | 0.6009 | 1.2383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0809**, LLR χ² = **47.48** (p = **1.77e-06**), AUC = **0.6930**, AIC = **563.4**, BIC = **617.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5266 | 1.2633 | ±2.5267 | -1.208 | 0.2269 | 0.2173 |  |
| Education: graduate level (vs college) | -0.0516 | 0.2455 | ±0.4910 | -0.210 | 0.8336 | 0.9497 |  |
| Education: high school or below (vs college) | +0.3460 | 0.3672 | ±0.7344 | +0.942 | 0.3460 | 1.4134 |  |
| Site: UCSD (vs UAB) | -0.1136 | 0.3040 | ±0.6081 | -0.374 | 0.7087 | 0.8926 |  |
| Site: UW (vs UAB) | +0.0733 | 0.2852 | ±0.5704 | +0.257 | 0.7971 | 1.0761 |  |
| **Age (years)** | **-0.0533** | 0.0111 | ±0.0221 | **-4.816** | **1.47e-06** | 0.9481 | *** |
| BMI (kg/m2) | +0.0276 | 0.0160 | ±0.0319 | +1.731 | 0.0835 | 1.0280 | . |
| Hypertension | +0.2728 | 0.2489 | ±0.4979 | +1.096 | 0.2732 | 1.3136 |  |
| **High cholesterol** | **+0.5788** | 0.2334 | ±0.4668 | **+2.480** | **0.0131** | 1.7839 | * |
| Kidney disease | +0.6062 | 0.3934 | ±0.7867 | +1.541 | 0.1233 | 1.8335 |  |
| Circulatory disease | +0.4030 | 0.3484 | ±0.6969 | +1.157 | 0.2474 | 1.4964 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0137 | 0.0085 | ±0.0170 | +1.609 | 0.1076 | 1.0138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **4.99e-06**), AUC = **0.6868**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0691 | 0.9846 | ±1.9692 | -0.070 | 0.9440 | 0.9332 |  |
| Education: graduate level (vs college) | -0.0411 | 0.2447 | ±0.4895 | -0.168 | 0.8667 | 0.9597 |  |
| Education: high school or below (vs college) | +0.3539 | 0.3671 | ±0.7341 | +0.964 | 0.3350 | 1.4246 |  |
| Site: UCSD (vs UAB) | -0.1090 | 0.3049 | ±0.6097 | -0.358 | 0.7207 | 0.8967 |  |
| Site: UW (vs UAB) | +0.1097 | 0.2842 | ±0.5684 | +0.386 | 0.6994 | 1.1160 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0222 | **-4.859** | **1.18e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0153 | ±0.0306 | **+2.120** | **0.0340** | 1.0330 | * |
| Hypertension | +0.2822 | 0.2493 | ±0.4986 | +1.132 | 0.2576 | 1.3260 |  |
| **High cholesterol** | **+0.5986** | 0.2327 | ±0.4655 | **+2.572** | **0.0101** | 1.8195 | * |
| Kidney disease | +0.6230 | 0.3922 | ±0.7845 | +1.588 | 0.1122 | 1.8645 |  |
| Circulatory disease | +0.4219 | 0.3482 | ±0.6965 | +1.211 | 0.2257 | 1.5248 |  |
| Glucose SD, pooled (mg/dL) | +0.0023 | 0.0297 | ±0.0594 | +0.078 | 0.9380 | 1.0023 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.93** (p = **5.00e-06**), AUC = **0.6867**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0271 | 0.9616 | ±1.9233 | -0.028 | 0.9775 | 0.9732 |  |
| Education: graduate level (vs college) | -0.0419 | 0.2446 | ±0.4892 | -0.171 | 0.8639 | 0.9589 |  |
| Education: high school or below (vs college) | +0.3547 | 0.3671 | ±0.7342 | +0.966 | 0.3339 | 1.4257 |  |
| Site: UCSD (vs UAB) | -0.1114 | 0.3049 | ±0.6097 | -0.365 | 0.7148 | 0.8946 |  |
| Site: UW (vs UAB) | +0.1100 | 0.2842 | ±0.5684 | +0.387 | 0.6988 | 1.1162 |  |
| **Age (years)** | **-0.0538** | 0.0111 | ±0.0222 | **-4.849** | **1.24e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0153 | ±0.0306 | **+2.122** | **0.0338** | 1.0330 | * |
| Hypertension | +0.2835 | 0.2492 | ±0.4984 | +1.138 | 0.2552 | 1.3278 |  |
| **High cholesterol** | **+0.5988** | 0.2327 | ±0.4654 | **+2.573** | **0.0101** | 1.8199 | * |
| Kidney disease | +0.6241 | 0.3926 | ±0.7851 | +1.590 | 0.1118 | 1.8666 |  |
| Circulatory disease | +0.4209 | 0.3482 | ±0.6964 | +1.209 | 0.2268 | 1.5233 |  |
| Avg. daily SD (mg/dL) | -0.0002 | 0.0303 | ±0.0606 | -0.006 | 0.9949 | 0.9998 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.92e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0962 | 1.0594 | ±2.1188 | +0.091 | 0.9276 | 1.1010 |  |
| Education: graduate level (vs college) | -0.0459 | 0.2453 | ±0.4906 | -0.187 | 0.8516 | 0.9551 |  |
| Education: high school or below (vs college) | +0.3556 | 0.3670 | ±0.7341 | +0.969 | 0.3326 | 1.4271 |  |
| Site: UCSD (vs UAB) | -0.1164 | 0.3045 | ±0.6090 | -0.382 | 0.7023 | 0.8901 |  |
| Site: UW (vs UAB) | +0.1081 | 0.2842 | ±0.5684 | +0.380 | 0.7037 | 1.1142 |  |
| **Age (years)** | **-0.0537** | 0.0111 | ±0.0222 | **-4.843** | **1.28e-06** | 0.9477 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0153 | ±0.0306 | **+2.118** | **0.0342** | 1.0330 | * |
| Hypertension | +0.2863 | 0.2492 | ±0.4983 | +1.149 | 0.2506 | 1.3314 |  |
| **High cholesterol** | **+0.5983** | 0.2327 | ±0.4655 | **+2.571** | **0.0101** | 1.8191 | * |
| Kidney disease | +0.6243 | 0.3921 | ±0.7843 | +1.592 | 0.1114 | 1.8669 |  |
| Circulatory disease | +0.4164 | 0.3488 | ±0.6977 | +1.194 | 0.2326 | 1.5165 |  |
| CV (%) | -0.0081 | 0.0407 | ±0.0815 | -0.198 | 0.8427 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.93e-06**), AUC = **0.6864**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1577 | 1.0692 | ±2.1383 | -0.147 | 0.8827 | 0.8541 |  |
| Education: graduate level (vs college) | -0.0461 | 0.2454 | ±0.4909 | -0.188 | 0.8509 | 0.9549 |  |
| Education: high school or below (vs college) | +0.3562 | 0.3671 | ±0.7341 | +0.971 | 0.3318 | 1.4280 |  |
| Site: UCSD (vs UAB) | -0.1147 | 0.3039 | ±0.6079 | -0.377 | 0.7059 | 0.8916 |  |
| Site: UW (vs UAB) | +0.1093 | 0.2841 | ±0.5682 | +0.385 | 0.7006 | 1.1154 |  |
| **Age (years)** | **-0.0537** | 0.0111 | ±0.0222 | **-4.848** | **1.25e-06** | 0.9477 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0153 | ±0.0306 | **+2.118** | **0.0342** | 1.0330 | * |
| Hypertension | +0.2863 | 0.2492 | ±0.4984 | +1.149 | 0.2506 | 1.3315 |  |
| **High cholesterol** | **+0.5980** | 0.2328 | ±0.4655 | **+2.569** | **0.0102** | 1.8184 | * |
| Kidney disease | +0.6245 | 0.3921 | ±0.7842 | +1.593 | 0.1112 | 1.8673 |  |
| Circulatory disease | +0.4166 | 0.3488 | ±0.6976 | +1.194 | 0.2324 | 1.5167 |  |
| Mean / SD ratio | +0.0194 | 0.0993 | ±0.1986 | +0.196 | 0.8449 | 1.0196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0769**, LLR χ² = **45.10** (p = **4.65e-06**), AUC = **0.6866**, AIC = **565.8**, BIC = **620.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2953 | 1.0541 | ±2.1083 | -0.280 | 0.7794 | 0.7443 |  |
| Education: graduate level (vs college) | -0.0495 | 0.2452 | ±0.4904 | -0.202 | 0.8400 | 0.9517 |  |
| Education: high school or below (vs college) | +0.3580 | 0.3671 | ±0.7342 | +0.975 | 0.3294 | 1.4305 |  |
| Site: UCSD (vs UAB) | -0.1181 | 0.3038 | ±0.6076 | -0.389 | 0.6975 | 0.8886 |  |
| Site: UW (vs UAB) | +0.1102 | 0.2841 | ±0.5682 | +0.388 | 0.6981 | 1.1165 |  |
| **Age (years)** | **-0.0535** | 0.0111 | ±0.0222 | **-4.820** | **1.44e-06** | 0.9480 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0306 | **+2.130** | **0.0331** | 1.0331 | * |
| Hypertension | +0.2865 | 0.2489 | ±0.4977 | +1.151 | 0.2497 | 1.3317 |  |
| **High cholesterol** | **+0.5948** | 0.2329 | ±0.4657 | **+2.554** | **0.0106** | 1.8127 | * |
| Kidney disease | +0.6276 | 0.3922 | ±0.7843 | +1.600 | 0.1095 | 1.8732 |  |
| Circulatory disease | +0.4116 | 0.3489 | ±0.6979 | +1.180 | 0.2381 | 1.5093 |  |
| Avg. daily mean/SD | +0.0338 | 0.0800 | ±0.1601 | +0.423 | 0.6725 | 1.0344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0767**, LLR χ² = **45.04** (p = **4.78e-06**), AUC = **0.6872**, AIC = **565.8**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2313 | 1.0375 | ±2.0750 | -0.223 | 0.8236 | 0.7935 |  |
| Education: graduate level (vs college) | -0.0395 | 0.2446 | ±0.4893 | -0.161 | 0.8718 | 0.9613 |  |
| Education: high school or below (vs college) | +0.3458 | 0.3681 | ±0.7361 | +0.939 | 0.3475 | 1.4131 |  |
| Site: UCSD (vs UAB) | -0.1091 | 0.3037 | ±0.6073 | -0.359 | 0.7195 | 0.8967 |  |
| Site: UW (vs UAB) | +0.1103 | 0.2841 | ±0.5682 | +0.388 | 0.6979 | 1.1166 |  |
| **Age (years)** | **-0.0538** | 0.0111 | ±0.0221 | **-4.872** | **1.11e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0307 | **+2.126** | **0.0335** | 1.0331 | * |
| Hypertension | +0.2868 | 0.2490 | ±0.4979 | +1.152 | 0.2494 | 1.3321 |  |
| **High cholesterol** | **+0.6012** | 0.2330 | ±0.4660 | **+2.581** | **0.0099** | 1.8244 | ** |
| Kidney disease | +0.6189 | 0.3924 | ±0.7848 | +1.577 | 0.1147 | 1.8569 |  |
| Circulatory disease | +0.4246 | 0.3482 | ±0.6964 | +1.219 | 0.2227 | 1.5290 |  |
| MAG (mg/dL/h) | +0.0054 | 0.0160 | ±0.0321 | +0.337 | 0.7363 | 1.0054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.95** (p = **4.95e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0630 | 1.0259 | ±2.0518 | +0.061 | 0.9511 | 1.0650 |  |
| Education: graduate level (vs college) | -0.0418 | 0.2445 | ±0.4889 | -0.171 | 0.8643 | 0.9591 |  |
| Education: high school or below (vs college) | +0.3577 | 0.3676 | ±0.7351 | +0.973 | 0.3304 | 1.4301 |  |
| Site: UCSD (vs UAB) | -0.1144 | 0.3041 | ±0.6082 | -0.376 | 0.7068 | 0.8919 |  |
| Site: UW (vs UAB) | +0.1107 | 0.2842 | ±0.5684 | +0.390 | 0.6968 | 1.1171 |  |
| **Age (years)** | **-0.0537** | 0.0111 | ±0.0222 | **-4.839** | **1.31e-06** | 0.9477 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0153 | ±0.0306 | **+2.115** | **0.0344** | 1.0329 | * |
| Hypertension | +0.2843 | 0.2488 | ±0.4976 | +1.143 | 0.2532 | 1.3288 |  |
| **High cholesterol** | **+0.5979** | 0.2328 | ±0.4655 | **+2.569** | **0.0102** | 1.8183 | * |
| Kidney disease | +0.6282 | 0.3929 | ±0.7858 | +1.599 | 0.1098 | 1.8742 |  |
| Circulatory disease | +0.4208 | 0.3481 | ±0.6962 | +1.209 | 0.2267 | 1.5231 |  |
| Avg. daily range (mg/dL) | -0.0011 | 0.0070 | ±0.0140 | -0.161 | 0.8723 | 0.9989 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0775**, LLR χ² = **45.51** (p = **3.95e-06**), AUC = **0.6886**, AIC = **565.4**, BIC = **619.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2354 | 0.8886 | ±1.7773 | -0.265 | 0.7911 | 0.7903 |  |
| Education: graduate level (vs college) | -0.0329 | 0.2452 | ±0.4905 | -0.134 | 0.8931 | 0.9676 |  |
| Education: high school or below (vs college) | +0.3550 | 0.3670 | ±0.7340 | +0.967 | 0.3334 | 1.4262 |  |
| Site: UCSD (vs UAB) | -0.1031 | 0.3043 | ±0.6086 | -0.339 | 0.7347 | 0.9020 |  |
| Site: UW (vs UAB) | +0.1116 | 0.2849 | ±0.5697 | +0.392 | 0.6951 | 1.1181 |  |
| **Age (years)** | **-0.0536** | 0.0110 | ±0.0221 | **-4.856** | **1.20e-06** | 0.9478 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0154 | ±0.0309 | **+2.043** | **0.0410** | 1.0320 | * |
| Hypertension | +0.2848 | 0.2487 | ±0.4975 | +1.145 | 0.2522 | 1.3295 |  |
| **High cholesterol** | **+0.5805** | 0.2337 | ±0.4675 | **+2.484** | **0.0130** | 1.7870 | * |
| Kidney disease | +0.6407 | 0.3920 | ±0.7840 | +1.635 | 0.1021 | 1.8979 |  |
| Circulatory disease | +0.4275 | 0.3480 | ±0.6960 | +1.229 | 0.2192 | 1.5334 |  |
| SD of daily means (mg/dL) | +0.0366 | 0.0475 | ±0.0950 | +0.770 | 0.4415 | 1.0372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0812**, LLR χ² = **47.64** (p = **1.65e-06**), AUC = **0.6881**, AIC = **563.2**, BIC = **617.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.9246 | 3.6450 | ±7.2900 | +1.625 | 0.1041 | 374.1250 |  |
| Education: graduate level (vs college) | -0.0589 | 0.2460 | ±0.4919 | -0.239 | 0.8107 | 0.9428 |  |
| Education: high school or below (vs college) | +0.3499 | 0.3669 | ±0.7337 | +0.954 | 0.3402 | 1.4190 |  |
| Site: UCSD (vs UAB) | -0.0719 | 0.3051 | ±0.6102 | -0.236 | 0.8137 | 0.9306 |  |
| Site: UW (vs UAB) | +0.0981 | 0.2850 | ±0.5700 | +0.344 | 0.7307 | 1.1031 |  |
| **Age (years)** | **-0.0553** | 0.0111 | ±0.0223 | **-4.967** | **6.80e-07** | 0.9462 | *** |
| **BMI (kg/m2)** | **+0.0314** | 0.0154 | ±0.0309 | **+2.037** | **0.0417** | 1.0319 | * |
| Hypertension | +0.2910 | 0.2495 | ±0.4991 | +1.166 | 0.2435 | 1.3377 |  |
| **High cholesterol** | **+0.5715** | 0.2337 | ±0.4673 | **+2.446** | **0.0145** | 1.7708 | * |
| Kidney disease | +0.6032 | 0.3930 | ±0.7859 | +1.535 | 0.1248 | 1.8280 |  |
| Circulatory disease | +0.4015 | 0.3494 | ±0.6988 | +1.149 | 0.2505 | 1.4941 |  |
| Time in range 70-180, pooled (%) | -0.0595 | 0.0354 | ±0.0707 | -1.682 | 0.0926 | 0.9423 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0808**, LLR χ² = **47.40** (p = **1.82e-06**), AUC = **0.6886**, AIC = **563.5**, BIC = **617.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.8341 | 3.7453 | ±7.4905 | +1.558 | 0.1193 | 341.7658 |  |
| Education: graduate level (vs college) | -0.0582 | 0.2459 | ±0.4919 | -0.237 | 0.8129 | 0.9435 |  |
| Education: high school or below (vs college) | +0.3549 | 0.3666 | ±0.7332 | +0.968 | 0.3331 | 1.4260 |  |
| Site: UCSD (vs UAB) | -0.0733 | 0.3050 | ±0.6100 | -0.240 | 0.8102 | 0.9294 |  |
| Site: UW (vs UAB) | +0.1002 | 0.2849 | ±0.5699 | +0.352 | 0.7251 | 1.1054 |  |
| **Age (years)** | **-0.0551** | 0.0111 | ±0.0222 | **-4.956** | **7.18e-07** | 0.9464 | *** |
| **BMI (kg/m2)** | **+0.0312** | 0.0155 | ±0.0309 | **+2.019** | **0.0435** | 1.0317 | * |
| Hypertension | +0.2910 | 0.2495 | ±0.4989 | +1.166 | 0.2434 | 1.3377 |  |
| **High cholesterol** | **+0.5719** | 0.2336 | ±0.4673 | **+2.448** | **0.0144** | 1.7716 | * |
| Kidney disease | +0.5987 | 0.3932 | ±0.7864 | +1.523 | 0.1279 | 1.8198 |  |
| Circulatory disease | +0.4000 | 0.3493 | ±0.6986 | +1.145 | 0.2522 | 1.4918 |  |
| Avg. daily time in range 70-180 (%) | -0.0585 | 0.0363 | ±0.0727 | -1.610 | 0.1074 | 0.9432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.94** (p = **4.98e-06**), AUC = **0.6867**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0380 | 0.8498 | ±1.6997 | -0.045 | 0.9643 | 0.9627 |  |
| Education: graduate level (vs college) | -0.0396 | 0.2454 | ±0.4909 | -0.161 | 0.8719 | 0.9612 |  |
| Education: high school or below (vs college) | +0.3578 | 0.3681 | ±0.7363 | +0.972 | 0.3311 | 1.4302 |  |
| Site: UCSD (vs UAB) | -0.1120 | 0.3036 | ±0.6072 | -0.369 | 0.7123 | 0.8941 |  |
| Site: UW (vs UAB) | +0.1111 | 0.2844 | ±0.5688 | +0.391 | 0.6961 | 1.1175 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.873** | **1.10e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0306 | **+2.126** | **0.0335** | 1.0331 | * |
| Hypertension | +0.2833 | 0.2488 | ±0.4976 | +1.139 | 0.2548 | 1.3275 |  |
| **High cholesterol** | **+0.5983** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8191 | * |
| Kidney disease | +0.6255 | 0.3923 | ±0.7845 | +1.594 | 0.1108 | 1.8691 |  |
| Circulatory disease | +0.4222 | 0.3482 | ±0.6965 | +1.212 | 0.2254 | 1.5253 |  |
| Time 54-69, pooled (%) | +0.0249 | 0.2235 | ±0.4470 | +0.112 | 0.9112 | 1.0252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.93e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0423 | 0.8493 | ±1.6986 | -0.050 | 0.9603 | 0.9586 |  |
| Education: graduate level (vs college) | -0.0377 | 0.2455 | ±0.4911 | -0.153 | 0.8780 | 0.9630 |  |
| Education: high school or below (vs college) | +0.3605 | 0.3683 | ±0.7366 | +0.979 | 0.3277 | 1.4340 |  |
| Site: UCSD (vs UAB) | -0.1136 | 0.3038 | ±0.6076 | -0.374 | 0.7084 | 0.8926 |  |
| Site: UW (vs UAB) | +0.1117 | 0.2844 | ±0.5688 | +0.393 | 0.6946 | 1.1181 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.874** | **1.10e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0307 | **+2.128** | **0.0333** | 1.0332 | * |
| Hypertension | +0.2834 | 0.2489 | ±0.4977 | +1.139 | 0.2547 | 1.3277 |  |
| **High cholesterol** | **+0.5982** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8189 | * |
| Kidney disease | +0.6265 | 0.3923 | ±0.7845 | +1.597 | 0.1102 | 1.8711 |  |
| Circulatory disease | +0.4240 | 0.3484 | ±0.6969 | +1.217 | 0.2236 | 1.5281 |  |
| Avg. daily time 54-69 (%) | +0.0423 | 0.2141 | ±0.4283 | +0.198 | 0.8432 | 1.0433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.94** (p = **4.98e-06**), AUC = **0.6867**, AIC = **565.9**, BIC = **620.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0380 | 0.8498 | ±1.6997 | -0.045 | 0.9643 | 0.9627 |  |
| Education: graduate level (vs college) | -0.0396 | 0.2454 | ±0.4909 | -0.161 | 0.8719 | 0.9612 |  |
| Education: high school or below (vs college) | +0.3578 | 0.3681 | ±0.7363 | +0.972 | 0.3311 | 1.4302 |  |
| Site: UCSD (vs UAB) | -0.1120 | 0.3036 | ±0.6072 | -0.369 | 0.7123 | 0.8941 |  |
| Site: UW (vs UAB) | +0.1111 | 0.2844 | ±0.5688 | +0.391 | 0.6961 | 1.1175 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.873** | **1.10e-06** | 0.9476 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0306 | **+2.126** | **0.0335** | 1.0331 | * |
| Hypertension | +0.2833 | 0.2488 | ±0.4976 | +1.139 | 0.2548 | 1.3275 |  |
| **High cholesterol** | **+0.5983** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8191 | * |
| Kidney disease | +0.6255 | 0.3923 | ±0.7845 | +1.594 | 0.1108 | 1.8691 |  |
| Circulatory disease | +0.4222 | 0.3482 | ±0.6965 | +1.212 | 0.2254 | 1.5253 |  |
| Time < 70 (%) | +0.0249 | 0.2235 | ±0.4470 | +0.112 | 0.9112 | 1.0252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0766**, LLR χ² = **44.96** (p = **4.93e-06**), AUC = **0.6865**, AIC = **565.9**, BIC = **620.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0423 | 0.8493 | ±1.6986 | -0.050 | 0.9603 | 0.9586 |  |
| Education: graduate level (vs college) | -0.0377 | 0.2455 | ±0.4911 | -0.153 | 0.8780 | 0.9630 |  |
| Education: high school or below (vs college) | +0.3605 | 0.3683 | ±0.7366 | +0.979 | 0.3277 | 1.4340 |  |
| Site: UCSD (vs UAB) | -0.1136 | 0.3038 | ±0.6076 | -0.374 | 0.7084 | 0.8926 |  |
| Site: UW (vs UAB) | +0.1117 | 0.2844 | ±0.5688 | +0.393 | 0.6946 | 1.1181 |  |
| **Age (years)** | **-0.0539** | 0.0111 | ±0.0221 | **-4.874** | **1.10e-06** | 0.9475 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0153 | ±0.0307 | **+2.128** | **0.0333** | 1.0332 | * |
| Hypertension | +0.2834 | 0.2489 | ±0.4977 | +1.139 | 0.2547 | 1.3277 |  |
| **High cholesterol** | **+0.5982** | 0.2328 | ±0.4656 | **+2.570** | **0.0102** | 1.8189 | * |
| Kidney disease | +0.6265 | 0.3923 | ±0.7845 | +1.597 | 0.1102 | 1.8711 |  |
| Circulatory disease | +0.4240 | 0.3484 | ±0.6969 | +1.217 | 0.2236 | 1.5281 |  |
| Avg. daily time < 70 (%) | +0.0423 | 0.2141 | ±0.4283 | +0.198 | 0.8432 | 1.0433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0810**, LLR χ² = **47.54** (p = **1.72e-06**), AUC = **0.6875**, AIC = **563.3**, BIC = **617.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0048 | 0.8506 | ±1.7012 | -0.006 | 0.9955 | 0.9953 |  |
| Education: graduate level (vs college) | -0.0639 | 0.2461 | ±0.4922 | -0.259 | 0.7953 | 0.9381 |  |
| Education: high school or below (vs college) | +0.3428 | 0.3668 | ±0.7337 | +0.934 | 0.3501 | 1.4088 |  |
| Site: UCSD (vs UAB) | -0.0710 | 0.3052 | ±0.6104 | -0.233 | 0.8161 | 0.9315 |  |
| Site: UW (vs UAB) | +0.0957 | 0.2849 | ±0.5699 | +0.336 | 0.7368 | 1.1005 |  |
| **Age (years)** | **-0.0552** | 0.0111 | ±0.0223 | **-4.965** | **6.88e-07** | 0.9463 | *** |
| **BMI (kg/m2)** | **+0.0313** | 0.0154 | ±0.0309 | **+2.031** | **0.0423** | 1.0318 | * |
| Hypertension | +0.2910 | 0.2494 | ±0.4988 | +1.167 | 0.2433 | 1.3378 |  |
| **High cholesterol** | **+0.5730** | 0.2335 | ±0.4671 | **+2.454** | **0.0141** | 1.7737 | * |
| Kidney disease | +0.6003 | 0.3930 | ±0.7860 | +1.527 | 0.1266 | 1.8227 |  |
| Circulatory disease | +0.3990 | 0.3494 | ±0.6989 | +1.142 | 0.2535 | 1.4904 |  |
| Time 181-250, pooled (%) | +0.0580 | 0.0351 | ±0.0701 | +1.653 | 0.0983 | 1.0597 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0805**, LLR χ² = **47.27** (p = **1.93e-06**), AUC = **0.6881**, AIC = **563.6**, BIC = **617.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0031 | 0.8511 | ±1.7023 | -0.004 | 0.9971 | 0.9969 |  |
| Education: graduate level (vs college) | -0.0631 | 0.2461 | ±0.4921 | -0.256 | 0.7976 | 0.9388 |  |
| Education: high school or below (vs college) | +0.3472 | 0.3666 | ±0.7332 | +0.947 | 0.3436 | 1.4151 |  |
| Site: UCSD (vs UAB) | -0.0714 | 0.3052 | ±0.6104 | -0.234 | 0.8150 | 0.9311 |  |
| Site: UW (vs UAB) | +0.0982 | 0.2849 | ±0.5697 | +0.345 | 0.7302 | 1.1032 |  |
| **Age (years)** | **-0.0550** | 0.0111 | ±0.0222 | **-4.952** | **7.34e-07** | 0.9464 | *** |
| **BMI (kg/m2)** | **+0.0311** | 0.0154 | ±0.0309 | **+2.014** | **0.0440** | 1.0316 | * |
| Hypertension | +0.2907 | 0.2493 | ±0.4986 | +1.166 | 0.2436 | 1.3374 |  |
| **High cholesterol** | **+0.5735** | 0.2335 | ±0.4670 | **+2.456** | **0.0141** | 1.7744 | * |
| Kidney disease | +0.5963 | 0.3933 | ±0.7866 | +1.516 | 0.1294 | 1.8155 |  |
| Circulatory disease | +0.3966 | 0.3494 | ±0.6988 | +1.135 | 0.2563 | 1.4868 |  |
| Avg. daily time 181-250 (%) | +0.0565 | 0.0361 | ±0.0721 | +1.566 | 0.1173 | 1.0581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0810**, LLR χ² = **47.54** (p = **1.72e-06**), AUC = **0.6875**, AIC = **563.3**, BIC = **617.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0048 | 0.8506 | ±1.7012 | -0.006 | 0.9955 | 0.9953 |  |
| Education: graduate level (vs college) | -0.0639 | 0.2461 | ±0.4922 | -0.259 | 0.7953 | 0.9381 |  |
| Education: high school or below (vs college) | +0.3428 | 0.3668 | ±0.7337 | +0.934 | 0.3501 | 1.4088 |  |
| Site: UCSD (vs UAB) | -0.0710 | 0.3052 | ±0.6104 | -0.233 | 0.8161 | 0.9315 |  |
| Site: UW (vs UAB) | +0.0957 | 0.2849 | ±0.5699 | +0.336 | 0.7368 | 1.1005 |  |
| **Age (years)** | **-0.0552** | 0.0111 | ±0.0223 | **-4.965** | **6.88e-07** | 0.9463 | *** |
| **BMI (kg/m2)** | **+0.0313** | 0.0154 | ±0.0309 | **+2.031** | **0.0423** | 1.0318 | * |
| Hypertension | +0.2910 | 0.2494 | ±0.4988 | +1.167 | 0.2433 | 1.3378 |  |
| **High cholesterol** | **+0.5730** | 0.2335 | ±0.4671 | **+2.454** | **0.0141** | 1.7737 | * |
| Kidney disease | +0.6003 | 0.3930 | ±0.7860 | +1.527 | 0.1266 | 1.8227 |  |
| Circulatory disease | +0.3990 | 0.3494 | ±0.6989 | +1.142 | 0.2535 | 1.4904 |  |
| Time > 180 (%) | +0.0580 | 0.0351 | ±0.0701 | +1.653 | 0.0983 | 1.0597 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0805**, LLR χ² = **47.27** (p = **1.93e-06**), AUC = **0.6881**, AIC = **563.6**, BIC = **617.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0031 | 0.8511 | ±1.7023 | -0.004 | 0.9971 | 0.9969 |  |
| Education: graduate level (vs college) | -0.0631 | 0.2461 | ±0.4921 | -0.256 | 0.7976 | 0.9388 |  |
| Education: high school or below (vs college) | +0.3472 | 0.3666 | ±0.7332 | +0.947 | 0.3436 | 1.4151 |  |
| Site: UCSD (vs UAB) | -0.0714 | 0.3052 | ±0.6104 | -0.234 | 0.8150 | 0.9311 |  |
| Site: UW (vs UAB) | +0.0982 | 0.2849 | ±0.5697 | +0.345 | 0.7302 | 1.1032 |  |
| **Age (years)** | **-0.0550** | 0.0111 | ±0.0222 | **-4.952** | **7.34e-07** | 0.9464 | *** |
| **BMI (kg/m2)** | **+0.0311** | 0.0154 | ±0.0309 | **+2.014** | **0.0440** | 1.0316 | * |
| Hypertension | +0.2907 | 0.2493 | ±0.4986 | +1.166 | 0.2436 | 1.3374 |  |
| **High cholesterol** | **+0.5735** | 0.2335 | ±0.4670 | **+2.456** | **0.0141** | 1.7744 | * |
| Kidney disease | +0.5963 | 0.3933 | ±0.7866 | +1.516 | 0.1294 | 1.8155 |  |
| Circulatory disease | +0.3966 | 0.3494 | ±0.6988 | +1.135 | 0.2563 | 1.4868 |  |
| Avg. daily time > 180 (%) | +0.0565 | 0.0361 | ±0.0721 | +1.566 | 0.1173 | 1.0581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 685)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **685**, events = **105**, McFadden pseudo-R² = **0.0939**, LLR χ² = **55.11** (p = **7.40e-08**), AUC = **0.6966**, AIC = **555.7**, BIC = **610.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0428 | 0.8658 | ±1.7316 | +0.049 | 0.9606 | 1.0437 |  |
| Education: graduate level (vs college) | -0.0364 | 0.2477 | ±0.4954 | -0.147 | 0.8832 | 0.9642 |  |
| Education: high school or below (vs college) | +0.3092 | 0.3712 | ±0.7424 | +0.833 | 0.4049 | 1.3623 |  |
| Site: UCSD (vs UAB) | -0.0861 | 0.3048 | ±0.6096 | -0.283 | 0.7774 | 0.9175 |  |
| Site: UW (vs UAB) | +0.0662 | 0.2871 | ±0.5741 | +0.231 | 0.8175 | 1.0685 |  |
| **Age (years)** | **-0.0536** | 0.0112 | ±0.0223 | **-4.803** | **1.56e-06** | 0.9478 | *** |
| BMI (kg/m2) | +0.0267 | 0.0159 | ±0.0318 | +1.684 | 0.0922 | 1.0271 | . |
| Hypertension | +0.3199 | 0.2510 | ±0.5021 | +1.274 | 0.2025 | 1.3771 |  |
| **High cholesterol** | **+0.5234** | 0.2360 | ±0.4720 | **+2.218** | **0.0266** | 1.6878 | * |
| Kidney disease | +0.6481 | 0.3926 | ±0.7853 | +1.651 | 0.0988 | 1.9119 | . |
| Circulatory disease | +0.4333 | 0.3512 | ±0.7025 | +1.234 | 0.2173 | 1.5424 |  |
| **Nocturnal time > 180 (%)** | **+0.0961** | 0.0338 | ±0.0676 | **+2.845** | **0.0044** | 1.1009 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1307**, F-statistic = **8.78** (p = **1.04e-16**), Residual SE = **0.824** on **660** df, AIC = **1665.0**, BIC = **1728.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9414** | 0.2293 | ±0.4585 | **+8.468** | **2.50e-17** | *** |
| Education: graduate level (vs college) | +0.0307 | 0.0685 | ±0.1370 | +0.448 | 0.6538 |  |
| **Education: high school or below (vs college)** | **+0.5081** | 0.1407 | ±0.2813 | **+3.612** | **3.04e-04** | *** |
| Site: UCSD (vs UAB) | -0.0224 | 0.0825 | ±0.1651 | -0.271 | 0.7865 |  |
| **Site: UW (vs UAB)** | **-0.3590** | 0.0901 | ±0.1803 | **-3.982** | **6.84e-05** | *** |
| Season: spring (vs autumn) | -0.0462 | 0.0924 | ±0.1849 | -0.500 | 0.6173 |  |
| Season: summer (vs autumn) | +0.0741 | 0.0955 | ±0.1910 | +0.776 | 0.4378 |  |
| Season: winter (vs autumn) | -0.0054 | 0.0894 | ±0.1787 | -0.060 | 0.9521 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.045** | **5.23e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.401** | **1.08e-05** | *** |
| Hypertension | +0.0918 | 0.0751 | ±0.1503 | +1.222 | 0.2219 |  |
| High cholesterol | -0.0930 | 0.0627 | ±0.1255 | -1.482 | 0.1383 |  |
| Kidney disease | -0.0247 | 0.1074 | ±0.2147 | -0.230 | 0.8182 |  |
| **Circulatory disease** | **+0.3125** | 0.1232 | ±0.2464 | **+2.536** | **0.0112** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.1484**, Adj R² = **0.1303**, F-statistic = **8.20** (p = **2.31e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.2**, BIC = **1733.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.5076** | 0.5972 | ±1.1945 | **+2.524** | **0.0116** | * |
| Education: graduate level (vs college) | +0.0297 | 0.0686 | ±0.1372 | +0.433 | 0.6651 |  |
| **Education: high school or below (vs college)** | **+0.5066** | 0.1405 | ±0.2810 | **+3.606** | **3.11e-04** | *** |
| Site: UCSD (vs UAB) | -0.0225 | 0.0829 | ±0.1658 | -0.271 | 0.7863 |  |
| **Site: UW (vs UAB)** | **-0.3605** | 0.0901 | ±0.1802 | **-4.000** | **6.32e-05** | *** |
| Season: spring (vs autumn) | -0.0340 | 0.0929 | ±0.1859 | -0.366 | 0.7142 |  |
| Season: summer (vs autumn) | +0.0761 | 0.0958 | ±0.1916 | +0.794 | 0.4270 |  |
| Season: winter (vs autumn) | +0.0017 | 0.0900 | ±0.1801 | +0.018 | 0.9853 |  |
| **Age (years)** | **-0.0122** | 0.0030 | ±0.0059 | **-4.113** | **3.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0225** | 0.0052 | ±0.0104 | **+4.329** | **1.50e-05** | *** |
| Hypertension | +0.0872 | 0.0759 | ±0.1518 | +1.148 | 0.2509 |  |
| High cholesterol | -0.0993 | 0.0634 | ±0.1267 | -1.568 | 0.1170 |  |
| Kidney disease | -0.0258 | 0.1082 | ±0.2164 | -0.238 | 0.8117 |  |
| **Circulatory disease** | **+0.3165** | 0.1233 | ±0.2465 | **+2.567** | **0.0103** | * |
| HbA1c (%) | +0.0840 | 0.1026 | ±0.2052 | +0.818 | 0.4133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.1490**, Adj R² = **0.1309**, F-statistic = **8.24** (p = **1.88e-16**), Residual SE = **0.823** on **659** df, AIC = **1665.8**, BIC = **1733.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2834** | 0.3851 | ±0.7703 | **+5.929** | **3.05e-09** | *** |
| Education: graduate level (vs college) | +0.0357 | 0.0687 | ±0.1374 | +0.519 | 0.6037 |  |
| **Education: high school or below (vs college)** | **+0.5133** | 0.1407 | ±0.2813 | **+3.649** | **2.63e-04** | *** |
| Site: UCSD (vs UAB) | -0.0271 | 0.0827 | ±0.1654 | -0.328 | 0.7430 |  |
| **Site: UW (vs UAB)** | **-0.3534** | 0.0899 | ±0.1798 | **-3.932** | **8.43e-05** | *** |
| Season: spring (vs autumn) | -0.0479 | 0.0927 | ±0.1853 | -0.517 | 0.6049 |  |
| Season: summer (vs autumn) | +0.0749 | 0.0953 | ±0.1907 | +0.786 | 0.4322 |  |
| Season: winter (vs autumn) | -0.0088 | 0.0889 | ±0.1779 | -0.099 | 0.9208 |  |
| **Age (years)** | **-0.0117** | 0.0030 | ±0.0059 | **-3.981** | **6.85e-05** | *** |
| **BMI (kg/m2)** | **+0.0237** | 0.0053 | ±0.0105 | **+4.494** | **6.99e-06** | *** |
| Hypertension | +0.0968 | 0.0756 | ±0.1512 | +1.280 | 0.2005 |  |
| High cholesterol | -0.0930 | 0.0628 | ±0.1256 | -1.481 | 0.1386 |  |
| Kidney disease | -0.0183 | 0.1069 | ±0.2137 | -0.171 | 0.8642 |  |
| **Circulatory disease** | **+0.3188** | 0.1233 | ±0.2467 | **+2.584** | **0.0098** | ** |
| Mean glucose (mg/dL) | -0.0031 | 0.0029 | ±0.0057 | -1.096 | 0.2730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.1490**, Adj R² = **0.1309**, F-statistic = **8.24** (p = **1.88e-16**), Residual SE = **0.823** on **659** df, AIC = **1665.8**, BIC = **1733.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7166** | 0.7410 | ±1.4819 | **+3.666** | **2.46e-04** | *** |
| Education: graduate level (vs college) | +0.0357 | 0.0687 | ±0.1374 | +0.519 | 0.6037 |  |
| **Education: high school or below (vs college)** | **+0.5133** | 0.1407 | ±0.2813 | **+3.649** | **2.63e-04** | *** |
| Site: UCSD (vs UAB) | -0.0271 | 0.0827 | ±0.1654 | -0.328 | 0.7430 |  |
| **Site: UW (vs UAB)** | **-0.3534** | 0.0899 | ±0.1798 | **-3.932** | **8.43e-05** | *** |
| Season: spring (vs autumn) | -0.0479 | 0.0927 | ±0.1853 | -0.517 | 0.6049 |  |
| Season: summer (vs autumn) | +0.0749 | 0.0953 | ±0.1907 | +0.786 | 0.4322 |  |
| Season: winter (vs autumn) | -0.0088 | 0.0889 | ±0.1779 | -0.099 | 0.9208 |  |
| **Age (years)** | **-0.0117** | 0.0030 | ±0.0059 | **-3.981** | **6.85e-05** | *** |
| **BMI (kg/m2)** | **+0.0237** | 0.0053 | ±0.0105 | **+4.494** | **6.99e-06** | *** |
| Hypertension | +0.0968 | 0.0756 | ±0.1512 | +1.280 | 0.2005 |  |
| High cholesterol | -0.0930 | 0.0628 | ±0.1256 | -1.481 | 0.1386 |  |
| Kidney disease | -0.0183 | 0.1069 | ±0.2137 | -0.171 | 0.8642 |  |
| **Circulatory disease** | **+0.3188** | 0.1233 | ±0.2467 | **+2.584** | **0.0098** | ** |
| GMI (%) | -0.1309 | 0.1194 | ±0.2388 | -1.096 | 0.2730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.1487**, Adj R² = **0.1306**, F-statistic = **8.22** (p = **2.08e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.0**, BIC = **1733.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2075** | 0.3543 | ±0.7086 | **+6.231** | **4.64e-10** | *** |
| Education: graduate level (vs college) | +0.0333 | 0.0686 | ±0.1372 | +0.486 | 0.6272 |  |
| **Education: high school or below (vs college)** | **+0.5117** | 0.1408 | ±0.2815 | **+3.635** | **2.78e-04** | *** |
| Site: UCSD (vs UAB) | -0.0230 | 0.0825 | ±0.1649 | -0.279 | 0.7802 |  |
| **Site: UW (vs UAB)** | **-0.3540** | 0.0899 | ±0.1798 | **-3.938** | **8.21e-05** | *** |
| Season: spring (vs autumn) | -0.0446 | 0.0926 | ±0.1851 | -0.482 | 0.6296 |  |
| Season: summer (vs autumn) | +0.0766 | 0.0956 | ±0.1912 | +0.802 | 0.4228 |  |
| Season: winter (vs autumn) | -0.0050 | 0.0894 | ±0.1788 | -0.055 | 0.9558 |  |
| **Age (years)** | **-0.0120** | 0.0029 | ±0.0059 | **-4.079** | **4.52e-05** | *** |
| **BMI (kg/m2)** | **+0.0241** | 0.0054 | ±0.0108 | **+4.478** | **7.52e-06** | *** |
| Hypertension | +0.0944 | 0.0753 | ±0.1506 | +1.254 | 0.2100 |  |
| High cholesterol | -0.0907 | 0.0627 | ±0.1254 | -1.448 | 0.1477 |  |
| Kidney disease | -0.0221 | 0.1071 | ±0.2142 | -0.207 | 0.8362 |  |
| **Circulatory disease** | **+0.3165** | 0.1234 | ±0.2468 | **+2.565** | **0.0103** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0025 | 0.0026 | ±0.0052 | -0.968 | 0.3333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1294**, F-statistic = **8.14** (p = **3.16e-16**), Residual SE = **0.824** on **659** df, AIC = **1667.0**, BIC = **1734.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9352** | 0.2755 | ±0.5511 | **+7.023** | **2.17e-12** | *** |
| Education: graduate level (vs college) | +0.0308 | 0.0689 | ±0.1378 | +0.448 | 0.6545 |  |
| **Education: high school or below (vs college)** | **+0.5080** | 0.1405 | ±0.2810 | **+3.616** | **2.99e-04** | *** |
| Site: UCSD (vs UAB) | -0.0221 | 0.0832 | ±0.1665 | -0.266 | 0.7905 |  |
| **Site: UW (vs UAB)** | **-0.3591** | 0.0903 | ±0.1805 | **-3.979** | **6.93e-05** | *** |
| Season: spring (vs autumn) | -0.0462 | 0.0925 | ±0.1851 | -0.499 | 0.6176 |  |
| Season: summer (vs autumn) | +0.0741 | 0.0957 | ±0.1915 | +0.774 | 0.4392 |  |
| Season: winter (vs autumn) | -0.0055 | 0.0895 | ±0.1790 | -0.061 | 0.9514 |  |
| **Age (years)** | **-0.0119** | 0.0030 | ±0.0059 | **-4.037** | **5.41e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.396** | **1.10e-05** | *** |
| Hypertension | +0.0916 | 0.0755 | ±0.1510 | +1.213 | 0.2252 |  |
| High cholesterol | -0.0930 | 0.0628 | ±0.1257 | -1.481 | 0.1387 |  |
| Kidney disease | -0.0249 | 0.1075 | ±0.2149 | -0.231 | 0.8171 |  |
| **Circulatory disease** | **+0.3125** | 0.1233 | ±0.2467 | **+2.534** | **0.0113** | * |
| Glucose SD, pooled (mg/dL) | +0.0004 | 0.0083 | ±0.0166 | +0.046 | 0.9630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.12e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9643** | 0.2704 | ±0.5407 | **+7.265** | **3.72e-13** | *** |
| Education: graduate level (vs college) | +0.0305 | 0.0687 | ±0.1374 | +0.443 | 0.6576 |  |
| **Education: high school or below (vs college)** | **+0.5087** | 0.1405 | ±0.2810 | **+3.620** | **2.94e-04** | *** |
| Site: UCSD (vs UAB) | -0.0235 | 0.0833 | ±0.1666 | -0.282 | 0.7777 |  |
| **Site: UW (vs UAB)** | **-0.3583** | 0.0902 | ±0.1804 | **-3.972** | **7.12e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.501 | 0.6163 |  |
| Season: summer (vs autumn) | +0.0740 | 0.0955 | ±0.1911 | +0.774 | 0.4387 |  |
| Season: winter (vs autumn) | -0.0055 | 0.0895 | ±0.1790 | -0.062 | 0.9509 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-4.026** | **5.68e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.413** | **1.02e-05** | *** |
| Hypertension | +0.0924 | 0.0755 | ±0.1510 | +1.224 | 0.2210 |  |
| High cholesterol | -0.0929 | 0.0628 | ±0.1257 | -1.478 | 0.1394 |  |
| Kidney disease | -0.0237 | 0.1076 | ±0.2152 | -0.220 | 0.8255 |  |
| **Circulatory disease** | **+0.3124** | 0.1233 | ±0.2467 | **+2.533** | **0.0113** | * |
| Avg. daily SD (mg/dL) | -0.0016 | 0.0084 | ±0.0168 | -0.186 | 0.8524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.1479**, Adj R² = **0.1298**, F-statistic = **8.17** (p = **2.73e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.6**, BIC = **1734.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8407** | 0.3031 | ±0.6061 | **+6.074** | **1.25e-09** | *** |
| Education: graduate level (vs college) | +0.0340 | 0.0696 | ±0.1391 | +0.489 | 0.6246 |  |
| **Education: high school or below (vs college)** | **+0.5081** | 0.1405 | ±0.2811 | **+3.616** | **3.00e-04** | *** |
| Site: UCSD (vs UAB) | -0.0200 | 0.0831 | ±0.1662 | -0.240 | 0.8102 |  |
| **Site: UW (vs UAB)** | **-0.3599** | 0.0904 | ±0.1808 | **-3.982** | **6.83e-05** | *** |
| Season: spring (vs autumn) | -0.0469 | 0.0925 | ±0.1851 | -0.507 | 0.6123 |  |
| Season: summer (vs autumn) | +0.0734 | 0.0957 | ±0.1914 | +0.767 | 0.4430 |  |
| Season: winter (vs autumn) | -0.0080 | 0.0893 | ±0.1786 | -0.090 | 0.9284 |  |
| **Age (years)** | **-0.0120** | 0.0029 | ±0.0059 | **-4.087** | **4.37e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0053 | ±0.0105 | **+4.393** | **1.12e-05** | *** |
| Hypertension | +0.0903 | 0.0753 | ±0.1506 | +1.200 | 0.2302 |  |
| High cholesterol | -0.0935 | 0.0629 | ±0.1258 | -1.486 | 0.1373 |  |
| Kidney disease | -0.0256 | 0.1074 | ±0.2149 | -0.238 | 0.8119 |  |
| **Circulatory disease** | **+0.3146** | 0.1233 | ±0.2466 | **+2.551** | **0.0107** | * |
| CV (%) | +0.0067 | 0.0116 | ±0.0232 | +0.577 | 0.5640 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.1477**, Adj R² = **0.1296**, F-statistic = **8.16** (p = **2.97e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.8**, BIC = **1734.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0142** | 0.2854 | ±0.5708 | **+7.057** | **1.70e-12** | *** |
| Education: graduate level (vs college) | +0.0330 | 0.0696 | ±0.1392 | +0.474 | 0.6357 |  |
| **Education: high school or below (vs college)** | **+0.5078** | 0.1405 | ±0.2810 | **+3.614** | **3.02e-04** | *** |
| Site: UCSD (vs UAB) | -0.0212 | 0.0830 | ±0.1660 | -0.255 | 0.7985 |  |
| **Site: UW (vs UAB)** | **-0.3599** | 0.0904 | ±0.1809 | **-3.980** | **6.89e-05** | *** |
| Season: spring (vs autumn) | -0.0472 | 0.0925 | ±0.1851 | -0.511 | 0.6097 |  |
| Season: summer (vs autumn) | +0.0739 | 0.0956 | ±0.1913 | +0.772 | 0.4399 |  |
| Season: winter (vs autumn) | -0.0072 | 0.0894 | ±0.1788 | -0.080 | 0.9359 |  |
| **Age (years)** | **-0.0120** | 0.0029 | ±0.0059 | **-4.062** | **4.86e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0053 | ±0.0105 | **+4.392** | **1.12e-05** | *** |
| Hypertension | +0.0907 | 0.0753 | ±0.1505 | +1.205 | 0.2280 |  |
| High cholesterol | -0.0931 | 0.0629 | ±0.1257 | -1.481 | 0.1386 |  |
| Kidney disease | -0.0253 | 0.1074 | ±0.2149 | -0.235 | 0.8140 |  |
| **Circulatory disease** | **+0.3139** | 0.1233 | ±0.2467 | **+2.545** | **0.0109** | * |
| Mean / SD ratio | -0.0107 | 0.0280 | ±0.0560 | -0.382 | 0.7026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.13e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9699** | 0.2788 | ±0.5576 | **+7.066** | **1.60e-12** | *** |
| Education: graduate level (vs college) | +0.0315 | 0.0693 | ±0.1385 | +0.454 | 0.6498 |  |
| **Education: high school or below (vs college)** | **+0.5079** | 0.1406 | ±0.2813 | **+3.612** | **3.04e-04** | *** |
| Site: UCSD (vs UAB) | -0.0218 | 0.0831 | ±0.1662 | -0.262 | 0.7932 |  |
| **Site: UW (vs UAB)** | **-0.3594** | 0.0904 | ±0.1807 | **-3.977** | **6.98e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.502 | 0.6159 |  |
| Season: summer (vs autumn) | +0.0743 | 0.0956 | ±0.1912 | +0.777 | 0.4374 |  |
| Season: winter (vs autumn) | -0.0057 | 0.0894 | ±0.1788 | -0.064 | 0.9493 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.047** | **5.18e-05** | *** |
| **BMI (kg/m2)** | **+0.0230** | 0.0052 | ±0.0105 | **+4.395** | **1.11e-05** | *** |
| Hypertension | +0.0916 | 0.0753 | ±0.1505 | +1.217 | 0.2236 |  |
| High cholesterol | -0.0929 | 0.0628 | ±0.1257 | -1.479 | 0.1392 |  |
| Kidney disease | -0.0251 | 0.1078 | ±0.2155 | -0.233 | 0.8157 |  |
| **Circulatory disease** | **+0.3131** | 0.1233 | ±0.2466 | **+2.539** | **0.0111** | * |
| Avg. daily mean/SD | -0.0036 | 0.0227 | ±0.0454 | -0.157 | 0.8751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.20** (p = **2.40e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.3**, BIC = **1734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8015** | 0.2953 | ±0.5906 | **+6.101** | **1.05e-09** | *** |
| Education: graduate level (vs college) | +0.0306 | 0.0685 | ±0.1370 | +0.447 | 0.6551 |  |
| **Education: high school or below (vs college)** | **+0.5017** | 0.1428 | ±0.2857 | **+3.512** | **4.45e-04** | *** |
| Site: UCSD (vs UAB) | -0.0200 | 0.0832 | ±0.1663 | -0.240 | 0.8103 |  |
| **Site: UW (vs UAB)** | **-0.3580** | 0.0907 | ±0.1813 | **-3.948** | **7.87e-05** | *** |
| Season: spring (vs autumn) | -0.0470 | 0.0923 | ±0.1845 | -0.510 | 0.6102 |  |
| Season: summer (vs autumn) | +0.0765 | 0.0957 | ±0.1914 | +0.799 | 0.4241 |  |
| Season: winter (vs autumn) | -0.0043 | 0.0893 | ±0.1786 | -0.048 | 0.9614 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.033** | **5.50e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0053 | ±0.0105 | **+4.399** | **1.09e-05** | *** |
| Hypertension | +0.0941 | 0.0759 | ±0.1519 | +1.239 | 0.2154 |  |
| High cholesterol | -0.0924 | 0.0629 | ±0.1258 | -1.469 | 0.1419 |  |
| Kidney disease | -0.0286 | 0.1072 | ±0.2145 | -0.266 | 0.7900 |  |
| **Circulatory disease** | **+0.3138** | 0.1232 | ±0.2464 | **+2.547** | **0.0109** | * |
| MAG (mg/dL/h) | +0.0037 | 0.0050 | ±0.0100 | +0.750 | 0.4533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.1479**, Adj R² = **0.1298**, F-statistic = **8.17** (p = **2.77e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.7**, BIC = **1734.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0323** | 0.2897 | ±0.5794 | **+7.015** | **2.29e-12** | *** |
| Education: graduate level (vs college) | +0.0312 | 0.0685 | ±0.1370 | +0.455 | 0.6491 |  |
| **Education: high school or below (vs college)** | **+0.5109** | 0.1404 | ±0.2808 | **+3.639** | **2.73e-04** | *** |
| Site: UCSD (vs UAB) | -0.0247 | 0.0828 | ±0.1656 | -0.298 | 0.7658 |  |
| **Site: UW (vs UAB)** | **-0.3570** | 0.0902 | ±0.1804 | **-3.959** | **7.52e-05** | *** |
| Season: spring (vs autumn) | -0.0458 | 0.0926 | ±0.1851 | -0.494 | 0.6210 |  |
| Season: summer (vs autumn) | +0.0731 | 0.0953 | ±0.1907 | +0.766 | 0.4435 |  |
| Season: winter (vs autumn) | -0.0057 | 0.0896 | ±0.1791 | -0.063 | 0.9496 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-4.013** | **6.00e-05** | *** |
| **BMI (kg/m2)** | **+0.0230** | 0.0052 | ±0.0105 | **+4.387** | **1.15e-05** | *** |
| Hypertension | +0.0925 | 0.0753 | ±0.1505 | +1.229 | 0.2190 |  |
| High cholesterol | -0.0933 | 0.0628 | ±0.1256 | -1.487 | 0.1371 |  |
| Kidney disease | -0.0215 | 0.1075 | ±0.2150 | -0.200 | 0.8411 |  |
| **Circulatory disease** | **+0.3133** | 0.1233 | ±0.2466 | **+2.541** | **0.0111** | * |
| Avg. daily range (mg/dL) | -0.0011 | 0.0019 | ±0.0037 | -0.582 | 0.5607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.1480**, Adj R² = **0.1299**, F-statistic = **8.18** (p = **2.66e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.6**, BIC = **1734.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9031** | 0.2345 | ±0.4691 | **+8.114** | **4.89e-16** | *** |
| Education: graduate level (vs college) | +0.0311 | 0.0686 | ±0.1371 | +0.454 | 0.6497 |  |
| **Education: high school or below (vs college)** | **+0.5072** | 0.1405 | ±0.2809 | **+3.611** | **3.05e-04** | *** |
| Site: UCSD (vs UAB) | -0.0216 | 0.0826 | ±0.1653 | -0.261 | 0.7941 |  |
| **Site: UW (vs UAB)** | **-0.3602** | 0.0903 | ±0.1807 | **-3.987** | **6.68e-05** | *** |
| Season: spring (vs autumn) | -0.0495 | 0.0922 | ±0.1844 | -0.537 | 0.5914 |  |
| Season: summer (vs autumn) | +0.0687 | 0.0967 | ±0.1934 | +0.710 | 0.4775 |  |
| Season: winter (vs autumn) | -0.0092 | 0.0905 | ±0.1810 | -0.102 | 0.9188 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.043** | **5.28e-05** | *** |
| **BMI (kg/m2)** | **+0.0228** | 0.0053 | ±0.0106 | **+4.278** | **1.89e-05** | *** |
| Hypertension | +0.0921 | 0.0753 | ±0.1505 | +1.224 | 0.2210 |  |
| High cholesterol | -0.0958 | 0.0627 | ±0.1254 | -1.528 | 0.1265 |  |
| Kidney disease | -0.0215 | 0.1072 | ±0.2143 | -0.200 | 0.8413 |  |
| **Circulatory disease** | **+0.3113** | 0.1230 | ±0.2461 | **+2.530** | **0.0114** | * |
| SD of daily means (mg/dL) | +0.0088 | 0.0148 | ±0.0296 | +0.597 | 0.5508 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.19** (p = **2.44e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.4**, BIC = **1734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0311 | 1.1315 | ±2.2630 | +0.911 | 0.3622 |  |
| Education: graduate level (vs college) | +0.0313 | 0.0685 | ±0.1370 | +0.457 | 0.6479 |  |
| **Education: high school or below (vs college)** | **+0.5081** | 0.1408 | ±0.2816 | **+3.608** | **3.09e-04** | *** |
| Site: UCSD (vs UAB) | -0.0266 | 0.0830 | ±0.1659 | -0.321 | 0.7481 |  |
| **Site: UW (vs UAB)** | **-0.3567** | 0.0900 | ±0.1800 | **-3.964** | **7.37e-05** | *** |
| Season: spring (vs autumn) | -0.0480 | 0.0924 | ±0.1848 | -0.520 | 0.6032 |  |
| Season: summer (vs autumn) | +0.0733 | 0.0955 | ±0.1909 | +0.767 | 0.4428 |  |
| Season: winter (vs autumn) | -0.0073 | 0.0893 | ±0.1786 | -0.082 | 0.9350 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-3.999** | **6.37e-05** | *** |
| **BMI (kg/m2)** | **+0.0232** | 0.0052 | ±0.0105 | **+4.431** | **9.38e-06** | *** |
| Hypertension | +0.0926 | 0.0752 | ±0.1504 | +1.232 | 0.2181 |  |
| High cholesterol | -0.0899 | 0.0625 | ±0.1249 | -1.439 | 0.1501 |  |
| Kidney disease | -0.0214 | 0.1069 | ±0.2138 | -0.200 | 0.8414 |  |
| **Circulatory disease** | **+0.3158** | 0.1235 | ±0.2469 | **+2.558** | **0.0105** | * |
| Time in range 70-180, pooled (%) | +0.0091 | 0.0112 | ±0.0224 | +0.815 | 0.4150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.1488**, Adj R² = **0.1307**, F-statistic = **8.23** (p = **2.04e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.0**, BIC = **1733.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7361 | 1.1437 | ±2.2874 | +0.644 | 0.5198 |  |
| Education: graduate level (vs college) | +0.0315 | 0.0685 | ±0.1370 | +0.460 | 0.6452 |  |
| **Education: high school or below (vs college)** | **+0.5077** | 0.1407 | ±0.2815 | **+3.607** | **3.09e-04** | *** |
| Site: UCSD (vs UAB) | -0.0281 | 0.0829 | ±0.1658 | -0.338 | 0.7351 |  |
| **Site: UW (vs UAB)** | **-0.3565** | 0.0900 | ±0.1799 | **-3.963** | **7.41e-05** | *** |
| Season: spring (vs autumn) | -0.0485 | 0.0924 | ±0.1848 | -0.525 | 0.5992 |  |
| Season: summer (vs autumn) | +0.0731 | 0.0953 | ±0.1907 | +0.767 | 0.4433 |  |
| Season: winter (vs autumn) | -0.0083 | 0.0892 | ±0.1784 | -0.093 | 0.9262 |  |
| **Age (years)** | **-0.0117** | 0.0029 | ±0.0059 | **-3.994** | **6.49e-05** | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0052 | ±0.0105 | **+4.451** | **8.56e-06** | *** |
| Hypertension | +0.0925 | 0.0752 | ±0.1503 | +1.231 | 0.2185 |  |
| High cholesterol | -0.0889 | 0.0624 | ±0.1249 | -1.424 | 0.1545 |  |
| Kidney disease | -0.0199 | 0.1066 | ±0.2133 | -0.187 | 0.8520 |  |
| **Circulatory disease** | **+0.3175** | 0.1234 | ±0.2468 | **+2.572** | **0.0101** | * |
| Avg. daily time in range 70-180 (%) | +0.0121 | 0.0113 | ±0.0227 | +1.068 | 0.2856 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9379** | 0.2319 | ±0.4638 | **+8.356** | **6.48e-17** | *** |
| Education: graduate level (vs college) | +0.0320 | 0.0694 | ±0.1389 | +0.461 | 0.6445 |  |
| **Education: high school or below (vs college)** | **+0.5098** | 0.1412 | ±0.2824 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0229 | 0.0825 | ±0.1649 | -0.277 | 0.7815 |  |
| **Site: UW (vs UAB)** | **-0.3586** | 0.0902 | ±0.1805 | **-3.974** | **7.08e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.502 | 0.6159 |  |
| Season: summer (vs autumn) | +0.0735 | 0.0956 | ±0.1913 | +0.768 | 0.4423 |  |
| Season: winter (vs autumn) | -0.0063 | 0.0896 | ±0.1791 | -0.070 | 0.9439 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.037** | **5.41e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.401** | **1.08e-05** | *** |
| Hypertension | +0.0916 | 0.0753 | ±0.1505 | +1.217 | 0.2237 |  |
| High cholesterol | -0.0933 | 0.0626 | ±0.1252 | -1.490 | 0.1363 |  |
| Kidney disease | -0.0242 | 0.1073 | ±0.2147 | -0.226 | 0.8216 |  |
| **Circulatory disease** | **+0.3132** | 0.1235 | ±0.2471 | **+2.535** | **0.0112** | * |
| Time 54-69, pooled (%) | +0.0114 | 0.0531 | ±0.1062 | +0.214 | 0.8306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9381** | 0.2315 | ±0.4629 | **+8.374** | **5.59e-17** | *** |
| Education: graduate level (vs college) | +0.0322 | 0.0695 | ±0.1390 | +0.463 | 0.6436 |  |
| **Education: high school or below (vs college)** | **+0.5099** | 0.1413 | ±0.2825 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0232 | 0.0824 | ±0.1649 | -0.281 | 0.7788 |  |
| **Site: UW (vs UAB)** | **-0.3587** | 0.0902 | ±0.1805 | **-3.975** | **7.04e-05** | *** |
| Season: spring (vs autumn) | -0.0463 | 0.0925 | ±0.1850 | -0.500 | 0.6169 |  |
| Season: summer (vs autumn) | +0.0736 | 0.0956 | ±0.1913 | +0.770 | 0.4415 |  |
| Season: winter (vs autumn) | -0.0064 | 0.0896 | ±0.1791 | -0.072 | 0.9427 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.041** | **5.32e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.402** | **1.07e-05** | *** |
| Hypertension | +0.0916 | 0.0752 | ±0.1505 | +1.218 | 0.2233 |  |
| High cholesterol | -0.0932 | 0.0626 | ±0.1253 | -1.489 | 0.1366 |  |
| Kidney disease | -0.0243 | 0.1074 | ±0.2147 | -0.226 | 0.8209 |  |
| **Circulatory disease** | **+0.3134** | 0.1236 | ±0.2471 | **+2.536** | **0.0112** | * |
| Avg. daily time 54-69 (%) | +0.0115 | 0.0520 | ±0.1039 | +0.222 | 0.8245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9379** | 0.2319 | ±0.4638 | **+8.356** | **6.48e-17** | *** |
| Education: graduate level (vs college) | +0.0320 | 0.0694 | ±0.1389 | +0.461 | 0.6445 |  |
| **Education: high school or below (vs college)** | **+0.5098** | 0.1412 | ±0.2824 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0229 | 0.0825 | ±0.1649 | -0.277 | 0.7815 |  |
| **Site: UW (vs UAB)** | **-0.3586** | 0.0902 | ±0.1805 | **-3.974** | **7.08e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.502 | 0.6159 |  |
| Season: summer (vs autumn) | +0.0735 | 0.0956 | ±0.1913 | +0.768 | 0.4423 |  |
| Season: winter (vs autumn) | -0.0063 | 0.0896 | ±0.1791 | -0.070 | 0.9439 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.037** | **5.41e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.401** | **1.08e-05** | *** |
| Hypertension | +0.0916 | 0.0753 | ±0.1505 | +1.217 | 0.2237 |  |
| High cholesterol | -0.0933 | 0.0626 | ±0.1252 | -1.490 | 0.1363 |  |
| Kidney disease | -0.0242 | 0.1073 | ±0.2147 | -0.226 | 0.8216 |  |
| **Circulatory disease** | **+0.3132** | 0.1235 | ±0.2471 | **+2.535** | **0.0112** | * |
| Time < 70 (%) | +0.0114 | 0.0531 | ±0.1062 | +0.214 | 0.8306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9381** | 0.2315 | ±0.4629 | **+8.374** | **5.59e-17** | *** |
| Education: graduate level (vs college) | +0.0322 | 0.0695 | ±0.1390 | +0.463 | 0.6436 |  |
| **Education: high school or below (vs college)** | **+0.5099** | 0.1413 | ±0.2825 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0232 | 0.0824 | ±0.1649 | -0.281 | 0.7788 |  |
| **Site: UW (vs UAB)** | **-0.3587** | 0.0902 | ±0.1805 | **-3.975** | **7.04e-05** | *** |
| Season: spring (vs autumn) | -0.0463 | 0.0925 | ±0.1850 | -0.500 | 0.6169 |  |
| Season: summer (vs autumn) | +0.0736 | 0.0956 | ±0.1913 | +0.770 | 0.4415 |  |
| Season: winter (vs autumn) | -0.0064 | 0.0896 | ±0.1791 | -0.072 | 0.9427 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.041** | **5.32e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.402** | **1.07e-05** | *** |
| Hypertension | +0.0916 | 0.0752 | ±0.1505 | +1.218 | 0.2233 |  |
| High cholesterol | -0.0932 | 0.0626 | ±0.1253 | -1.489 | 0.1366 |  |
| Kidney disease | -0.0243 | 0.1074 | ±0.2147 | -0.226 | 0.8209 |  |
| **Circulatory disease** | **+0.3134** | 0.1236 | ±0.2471 | **+2.536** | **0.0112** | * |
| Avg. daily time < 70 (%) | +0.0115 | 0.0520 | ±0.1039 | +0.222 | 0.8245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.20** (p = **2.38e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.3**, BIC = **1734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9428** | 0.2293 | ±0.4587 | **+8.471** | **2.43e-17** | *** |
| Education: graduate level (vs college) | +0.0324 | 0.0685 | ±0.1371 | +0.473 | 0.6361 |  |
| **Education: high school or below (vs college)** | **+0.5094** | 0.1408 | ±0.2816 | **+3.619** | **2.96e-04** | *** |
| Site: UCSD (vs UAB) | -0.0272 | 0.0829 | ±0.1659 | -0.328 | 0.7427 |  |
| **Site: UW (vs UAB)** | **-0.3563** | 0.0900 | ±0.1800 | **-3.960** | **7.49e-05** | *** |
| Season: spring (vs autumn) | -0.0483 | 0.0924 | ±0.1849 | -0.523 | 0.6013 |  |
| Season: summer (vs autumn) | +0.0727 | 0.0954 | ±0.1909 | +0.762 | 0.4461 |  |
| Season: winter (vs autumn) | -0.0081 | 0.0893 | ±0.1786 | -0.091 | 0.9274 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-3.991** | **6.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0052 | ±0.0105 | **+4.434** | **9.27e-06** | *** |
| Hypertension | +0.0925 | 0.0752 | ±0.1503 | +1.230 | 0.2186 |  |
| High cholesterol | -0.0900 | 0.0626 | ±0.1252 | -1.438 | 0.1504 |  |
| Kidney disease | -0.0209 | 0.1069 | ±0.2137 | -0.195 | 0.8450 |  |
| **Circulatory disease** | **+0.3165** | 0.1235 | ±0.2471 | **+2.562** | **0.0104** | * |
| Time 181-250, pooled (%) | -0.0095 | 0.0112 | ±0.0224 | -0.846 | 0.3976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.1489**, Adj R² = **0.1308**, F-statistic = **8.23** (p = **1.98e-16**), Residual SE = **0.824** on **659** df, AIC = **1665.9**, BIC = **1733.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9425** | 0.2292 | ±0.4584 | **+8.475** | **2.36e-17** | *** |
| Education: graduate level (vs college) | +0.0331 | 0.0685 | ±0.1371 | +0.484 | 0.6287 |  |
| **Education: high school or below (vs college)** | **+0.5096** | 0.1407 | ±0.2813 | **+3.623** | **2.91e-04** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0829 | ±0.1659 | -0.351 | 0.7257 |  |
| **Site: UW (vs UAB)** | **-0.3561** | 0.0900 | ±0.1799 | **-3.959** | **7.52e-05** | *** |
| Season: spring (vs autumn) | -0.0487 | 0.0924 | ±0.1848 | -0.527 | 0.5981 |  |
| Season: summer (vs autumn) | +0.0725 | 0.0953 | ±0.1907 | +0.761 | 0.4467 |  |
| Season: winter (vs autumn) | -0.0095 | 0.0892 | ±0.1784 | -0.107 | 0.9151 |  |
| **Age (years)** | **-0.0117** | 0.0029 | ±0.0059 | **-3.989** | **6.62e-05** | *** |
| **BMI (kg/m2)** | **+0.0234** | 0.0052 | ±0.0105 | **+4.455** | **8.40e-06** | *** |
| Hypertension | +0.0923 | 0.0751 | ±0.1502 | +1.229 | 0.2191 |  |
| High cholesterol | -0.0890 | 0.0626 | ±0.1251 | -1.423 | 0.1548 |  |
| Kidney disease | -0.0193 | 0.1066 | ±0.2132 | -0.181 | 0.8560 |  |
| **Circulatory disease** | **+0.3187** | 0.1235 | ±0.2471 | **+2.580** | **0.0099** | ** |
| Avg. daily time 181-250 (%) | -0.0125 | 0.0114 | ±0.0227 | -1.098 | 0.2723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.20** (p = **2.38e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.3**, BIC = **1734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9428** | 0.2293 | ±0.4587 | **+8.471** | **2.43e-17** | *** |
| Education: graduate level (vs college) | +0.0324 | 0.0685 | ±0.1371 | +0.473 | 0.6361 |  |
| **Education: high school or below (vs college)** | **+0.5094** | 0.1408 | ±0.2816 | **+3.619** | **2.96e-04** | *** |
| Site: UCSD (vs UAB) | -0.0272 | 0.0829 | ±0.1659 | -0.328 | 0.7427 |  |
| **Site: UW (vs UAB)** | **-0.3563** | 0.0900 | ±0.1800 | **-3.960** | **7.49e-05** | *** |
| Season: spring (vs autumn) | -0.0483 | 0.0924 | ±0.1849 | -0.523 | 0.6013 |  |
| Season: summer (vs autumn) | +0.0727 | 0.0954 | ±0.1909 | +0.762 | 0.4461 |  |
| Season: winter (vs autumn) | -0.0081 | 0.0893 | ±0.1786 | -0.091 | 0.9274 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-3.991** | **6.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0052 | ±0.0105 | **+4.434** | **9.27e-06** | *** |
| Hypertension | +0.0925 | 0.0752 | ±0.1503 | +1.230 | 0.2186 |  |
| High cholesterol | -0.0900 | 0.0626 | ±0.1252 | -1.438 | 0.1504 |  |
| Kidney disease | -0.0209 | 0.1069 | ±0.2137 | -0.195 | 0.8450 |  |
| **Circulatory disease** | **+0.3165** | 0.1235 | ±0.2471 | **+2.562** | **0.0104** | * |
| Time > 180 (%) | -0.0095 | 0.0112 | ±0.0224 | -0.846 | 0.3976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.1489**, Adj R² = **0.1308**, F-statistic = **8.23** (p = **1.98e-16**), Residual SE = **0.824** on **659** df, AIC = **1665.9**, BIC = **1733.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9425** | 0.2292 | ±0.4584 | **+8.475** | **2.36e-17** | *** |
| Education: graduate level (vs college) | +0.0331 | 0.0685 | ±0.1371 | +0.484 | 0.6287 |  |
| **Education: high school or below (vs college)** | **+0.5096** | 0.1407 | ±0.2813 | **+3.623** | **2.91e-04** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0829 | ±0.1659 | -0.351 | 0.7257 |  |
| **Site: UW (vs UAB)** | **-0.3561** | 0.0900 | ±0.1799 | **-3.959** | **7.52e-05** | *** |
| Season: spring (vs autumn) | -0.0487 | 0.0924 | ±0.1848 | -0.527 | 0.5981 |  |
| Season: summer (vs autumn) | +0.0725 | 0.0953 | ±0.1907 | +0.761 | 0.4467 |  |
| Season: winter (vs autumn) | -0.0095 | 0.0892 | ±0.1784 | -0.107 | 0.9151 |  |
| **Age (years)** | **-0.0117** | 0.0029 | ±0.0059 | **-3.989** | **6.62e-05** | *** |
| **BMI (kg/m2)** | **+0.0234** | 0.0052 | ±0.0105 | **+4.455** | **8.40e-06** | *** |
| Hypertension | +0.0923 | 0.0751 | ±0.1502 | +1.229 | 0.2191 |  |
| High cholesterol | -0.0890 | 0.0626 | ±0.1251 | -1.423 | 0.1548 |  |
| Kidney disease | -0.0193 | 0.1066 | ±0.2132 | -0.181 | 0.8560 |  |
| **Circulatory disease** | **+0.3187** | 0.1235 | ±0.2471 | **+2.580** | **0.0099** | ** |
| Avg. daily time > 180 (%) | -0.0125 | 0.0114 | ±0.0227 | -1.098 | 0.2723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.1479**, Adj R² = **0.1298**, F-statistic = **8.17** (p = **2.71e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.6**, BIC = **1734.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9439** | 0.2298 | ±0.4595 | **+8.461** | **2.66e-17** | *** |
| Education: graduate level (vs college) | +0.0311 | 0.0686 | ±0.1371 | +0.454 | 0.6496 |  |
| **Education: high school or below (vs college)** | **+0.5059** | 0.1409 | ±0.2819 | **+3.590** | **3.31e-04** | *** |
| Site: UCSD (vs UAB) | -0.0206 | 0.0828 | ±0.1656 | -0.249 | 0.8037 |  |
| **Site: UW (vs UAB)** | **-0.3604** | 0.0902 | ±0.1804 | **-3.996** | **6.44e-05** | *** |
| Season: spring (vs autumn) | -0.0458 | 0.0927 | ±0.1854 | -0.494 | 0.6210 |  |
| Season: summer (vs autumn) | +0.0741 | 0.0958 | ±0.1915 | +0.774 | 0.4388 |  |
| Season: winter (vs autumn) | -0.0058 | 0.0898 | ±0.1795 | -0.064 | 0.9488 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-4.018** | **5.87e-05** | *** |
| **BMI (kg/m2)** | **+0.0227** | 0.0053 | ±0.0107 | **+4.250** | **2.14e-05** | *** |
| Hypertension | +0.0929 | 0.0751 | ±0.1503 | +1.236 | 0.2166 |  |
| High cholesterol | -0.0970 | 0.0626 | ±0.1251 | -1.550 | 0.1211 |  |
| Kidney disease | -0.0243 | 0.1075 | ±0.2151 | -0.226 | 0.8212 |  |
| **Circulatory disease** | **+0.3125** | 0.1232 | ±0.2465 | **+2.536** | **0.0112** | * |
| Nocturnal time > 180 (%) | +0.0061 | 0.0119 | ±0.0239 | +0.514 | 0.6076 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3382**, F-statistic = **27.45** (p = **9.60e-54**), Residual SE = **1.850** on **660** df, AIC = **2755.5**, BIC = **2818.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3033** | 0.6310 | ±1.2621 | **+38.513** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2021 | 0.1536 | ±0.3072 | -1.316 | 0.1883 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2981 | ±0.5962 | +0.473 | 0.6360 |  |
| Site: UCSD (vs UAB) | +0.0242 | 0.1975 | ±0.3950 | +0.123 | 0.9024 |  |
| **Site: UW (vs UAB)** | **-0.8980** | 0.1945 | ±0.3890 | **-4.617** | **3.89e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6942** | 0.2087 | ±0.4173 | **-3.327** | **8.78e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8638** | 0.2379 | ±0.4758 | **+7.835** | **4.71e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6257** | 0.2150 | ±0.4299 | **-7.563** | **3.95e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.966 | 0.3343 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.841 | 0.4005 |  |
| Hypertension | +0.2214 | 0.1753 | ±0.3506 | +1.263 | 0.2065 |  |
| High cholesterol | -0.1049 | 0.1548 | ±0.3096 | -0.678 | 0.4980 |  |
| Kidney disease | +0.1088 | 0.2670 | ±0.5339 | +0.407 | 0.6837 |  |
| **Circulatory disease** | **+0.5063** | 0.2527 | ±0.5054 | **+2.004** | **0.0451** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.3513**, Adj R² = **0.3375**, F-statistic = **25.49** (p = **4.33e-53**), Residual SE = **1.850** on **659** df, AIC = **2757.2**, BIC = **2824.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6101** | 1.2933 | ±2.5866 | **+18.256** | **1.86e-74** | *** |
| Education: graduate level (vs college) | -0.2037 | 0.1539 | ±0.3078 | -1.324 | 0.1856 |  |
| Education: high school or below (vs college) | +0.1387 | 0.2998 | ±0.5996 | +0.463 | 0.6436 |  |
| Site: UCSD (vs UAB) | +0.0240 | 0.1976 | ±0.3953 | +0.122 | 0.9032 |  |
| **Site: UW (vs UAB)** | **-0.9005** | 0.1947 | ±0.3893 | **-4.626** | **3.73e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6748** | 0.2109 | ±0.4218 | **-3.200** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.8670** | 0.2384 | ±0.4769 | **+7.830** | **4.88e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6144** | 0.2163 | ±0.4326 | **-7.463** | **8.43e-14** | *** |
| Age (years) | +0.0061 | 0.0070 | ±0.0139 | +0.881 | 0.3781 |  |
| BMI (kg/m2) | +0.0091 | 0.0119 | ±0.0238 | +0.768 | 0.4427 |  |
| Hypertension | +0.2140 | 0.1756 | ±0.3512 | +1.219 | 0.2229 |  |
| High cholesterol | -0.1150 | 0.1587 | ±0.3175 | -0.725 | 0.4687 |  |
| Kidney disease | +0.1070 | 0.2682 | ±0.5364 | +0.399 | 0.6899 |  |
| **Circulatory disease** | **+0.5127** | 0.2531 | ±0.5062 | **+2.025** | **0.0428** | * |
| HbA1c (%) | +0.1341 | 0.2197 | ±0.4394 | +0.610 | 0.5416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.3512**, Adj R² = **0.3374**, F-statistic = **25.48** (p = **4.57e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.3**, BIC = **2825.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9512** | 0.9503 | ±1.9005 | **+25.205** | **3.53e-140** | *** |
| Education: graduate level (vs college) | -0.2072 | 0.1535 | ±0.3070 | -1.349 | 0.1772 |  |
| Education: high school or below (vs college) | +0.1358 | 0.2984 | ±0.5968 | +0.455 | 0.6491 |  |
| Site: UCSD (vs UAB) | +0.0291 | 0.1987 | ±0.3974 | +0.147 | 0.8835 |  |
| **Site: UW (vs UAB)** | **-0.9037** | 0.1942 | ±0.3884 | **-4.654** | **3.25e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6924** | 0.2088 | ±0.4176 | **-3.316** | **9.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8630** | 0.2381 | ±0.4761 | **+7.826** | **5.05e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6221** | 0.2151 | ±0.4303 | **-7.540** | **4.72e-14** | *** |
| Age (years) | +0.0065 | 0.0069 | ±0.0139 | +0.939 | 0.3478 |  |
| BMI (kg/m2) | +0.0094 | 0.0119 | ±0.0239 | +0.788 | 0.4306 |  |
| Hypertension | +0.2162 | 0.1747 | ±0.3494 | +1.238 | 0.2158 |  |
| High cholesterol | -0.1049 | 0.1550 | ±0.3099 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1022 | 0.2662 | ±0.5324 | +0.384 | 0.7012 |  |
| **Circulatory disease** | **+0.4999** | 0.2530 | ±0.5059 | **+1.976** | **0.0482** | * |
| Mean glucose (mg/dL) | +0.0032 | 0.0064 | ±0.0128 | +0.502 | 0.6156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.3512**, Adj R² = **0.3374**, F-statistic = **25.48** (p = **4.57e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.3**, BIC = **2825.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5052** | 1.7193 | ±3.4387 | **+13.671** | **1.51e-42** | *** |
| Education: graduate level (vs college) | -0.2072 | 0.1535 | ±0.3070 | -1.349 | 0.1772 |  |
| Education: high school or below (vs college) | +0.1358 | 0.2984 | ±0.5968 | +0.455 | 0.6491 |  |
| Site: UCSD (vs UAB) | +0.0291 | 0.1987 | ±0.3974 | +0.147 | 0.8835 |  |
| **Site: UW (vs UAB)** | **-0.9037** | 0.1942 | ±0.3884 | **-4.654** | **3.25e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6924** | 0.2088 | ±0.4176 | **-3.316** | **9.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8630** | 0.2381 | ±0.4761 | **+7.826** | **5.05e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6221** | 0.2151 | ±0.4303 | **-7.540** | **4.72e-14** | *** |
| Age (years) | +0.0065 | 0.0069 | ±0.0139 | +0.939 | 0.3478 |  |
| BMI (kg/m2) | +0.0094 | 0.0119 | ±0.0239 | +0.788 | 0.4306 |  |
| Hypertension | +0.2162 | 0.1747 | ±0.3494 | +1.238 | 0.2158 |  |
| High cholesterol | -0.1049 | 0.1550 | ±0.3099 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1022 | 0.2662 | ±0.5324 | +0.384 | 0.7012 |  |
| **Circulatory disease** | **+0.4999** | 0.2530 | ±0.5059 | **+1.976** | **0.0482** | * |
| GMI (%) | +0.1347 | 0.2683 | ±0.5367 | +0.502 | 0.6156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.07e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1967** | 0.8661 | ±1.7322 | **+27.938** | **9.25e-172** | *** |
| Education: graduate level (vs college) | -0.2031 | 0.1535 | ±0.3069 | -1.324 | 0.1857 |  |
| Education: high school or below (vs college) | +0.1396 | 0.2985 | ±0.5970 | +0.468 | 0.6399 |  |
| Site: UCSD (vs UAB) | +0.0245 | 0.1978 | ±0.3957 | +0.124 | 0.9015 |  |
| **Site: UW (vs UAB)** | **-0.9000** | 0.1939 | ±0.3878 | **-4.642** | **3.45e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6949** | 0.2088 | ±0.4175 | **-3.328** | **8.73e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8628** | 0.2385 | ±0.4770 | **+7.811** | **5.68e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6258** | 0.2152 | ±0.4304 | **-7.556** | **4.17e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.972 | 0.3308 |  |
| BMI (kg/m2) | +0.0096 | 0.0121 | ±0.0243 | +0.791 | 0.4290 |  |
| Hypertension | +0.2204 | 0.1749 | ±0.3498 | +1.260 | 0.2077 |  |
| High cholesterol | -0.1058 | 0.1556 | ±0.3113 | -0.680 | 0.4967 |  |
| Kidney disease | +0.1077 | 0.2669 | ±0.5339 | +0.404 | 0.6865 |  |
| **Circulatory disease** | **+0.5047** | 0.2531 | ±0.5062 | **+1.994** | **0.0462** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0010 | 0.0054 | ±0.0109 | +0.184 | 0.8541 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.3518**, Adj R² = **0.3380**, F-statistic = **25.54** (p = **3.44e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.7**, BIC = **2824.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5911** | 0.7186 | ±1.4371 | **+34.222** | **1.14e-256** | *** |
| Education: graduate level (vs college) | -0.2075 | 0.1542 | ±0.3085 | -1.346 | 0.1785 |  |
| Education: high school or below (vs college) | +0.1466 | 0.2962 | ±0.5924 | +0.495 | 0.6206 |  |
| Site: UCSD (vs UAB) | +0.0126 | 0.1977 | ±0.3954 | +0.064 | 0.9492 |  |
| **Site: UW (vs UAB)** | **-0.8897** | 0.1940 | ±0.3879 | **-4.586** | **4.51e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6938** | 0.2089 | ±0.4177 | **-3.322** | **8.95e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8658** | 0.2387 | ±0.4774 | **+7.816** | **5.44e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6217** | 0.2150 | ±0.4301 | **-7.541** | **4.65e-14** | *** |
| Age (years) | +0.0073 | 0.0069 | ±0.0138 | +1.052 | 0.2930 |  |
| BMI (kg/m2) | +0.0105 | 0.0120 | ±0.0239 | +0.877 | 0.3807 |  |
| Hypertension | +0.2299 | 0.1754 | ±0.3508 | +1.311 | 0.1899 |  |
| High cholesterol | -0.1025 | 0.1554 | ±0.3108 | -0.660 | 0.5095 |  |
| Kidney disease | +0.1169 | 0.2660 | ±0.5319 | +0.440 | 0.6603 |  |
| **Circulatory disease** | **+0.5051** | 0.2540 | ±0.5080 | **+1.989** | **0.0467** | * |
| Glucose SD, pooled (mg/dL) | -0.0177 | 0.0194 | ±0.0387 | -0.917 | 0.3594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.3518**, Adj R² = **0.3380**, F-statistic = **25.54** (p = **3.43e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.7**, BIC = **2824.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5668** | 0.7130 | ±1.4261 | **+34.454** | **3.90e-260** | *** |
| Education: graduate level (vs college) | -0.2050 | 0.1542 | ±0.3083 | -1.330 | 0.1835 |  |
| Education: high school or below (vs college) | +0.1474 | 0.2963 | ±0.5925 | +0.497 | 0.6189 |  |
| Site: UCSD (vs UAB) | +0.0108 | 0.1977 | ±0.3954 | +0.055 | 0.9562 |  |
| **Site: UW (vs UAB)** | **-0.8901** | 0.1941 | ±0.3883 | **-4.585** | **4.54e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6963** | 0.2089 | ±0.4177 | **-3.334** | **8.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8626** | 0.2383 | ±0.4766 | **+7.817** | **5.43e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6272** | 0.2147 | ±0.4293 | **-7.580** | **3.44e-14** | *** |
| Age (years) | +0.0072 | 0.0069 | ±0.0138 | +1.053 | 0.2922 |  |
| BMI (kg/m2) | +0.0106 | 0.0120 | ±0.0240 | +0.887 | 0.3751 |  |
| Hypertension | +0.2288 | 0.1757 | ±0.3515 | +1.302 | 0.1929 |  |
| High cholesterol | -0.1034 | 0.1552 | ±0.3104 | -0.666 | 0.5052 |  |
| Kidney disease | +0.1198 | 0.2657 | ±0.5315 | +0.451 | 0.6522 |  |
| **Circulatory disease** | **+0.5055** | 0.2540 | ±0.5080 | **+1.990** | **0.0466** | * |
| Avg. daily SD (mg/dL) | -0.0180 | 0.0195 | ±0.0389 | -0.925 | 0.3549 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.3525**, Adj R² = **0.3387**, F-statistic = **25.63** (p = **2.39e-53**), Residual SE = **1.849** on **659** df, AIC = **2755.9**, BIC = **2823.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.8018** | 0.7513 | ±1.5026 | **+33.011** | **5.60e-239** | *** |
| Education: graduate level (vs college) | -0.2185 | 0.1546 | ±0.3092 | -1.413 | 0.1575 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2952 | ±0.5904 | +0.478 | 0.6328 |  |
| Site: UCSD (vs UAB) | +0.0123 | 0.1969 | ±0.3939 | +0.063 | 0.9502 |  |
| **Site: UW (vs UAB)** | **-0.8931** | 0.1938 | ±0.3876 | **-4.608** | **4.07e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6907** | 0.2086 | ±0.4173 | **-3.310** | **9.31e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8672** | 0.2381 | ±0.4763 | **+7.841** | **4.47e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6125** | 0.2151 | ±0.4303 | **-7.495** | **6.63e-14** | *** |
| Age (years) | +0.0074 | 0.0069 | ±0.0137 | +1.072 | 0.2836 |  |
| BMI (kg/m2) | +0.0099 | 0.0120 | ±0.0239 | +0.824 | 0.4098 |  |
| Hypertension | +0.2286 | 0.1756 | ±0.3511 | +1.302 | 0.1928 |  |
| High cholesterol | -0.1026 | 0.1552 | ±0.3104 | -0.661 | 0.5085 |  |
| Kidney disease | +0.1132 | 0.2668 | ±0.5336 | +0.424 | 0.6714 |  |
| Circulatory disease | +0.4957 | 0.2533 | ±0.5067 | +1.957 | 0.0504 | . |
| CV (%) | -0.0332 | 0.0251 | ±0.0502 | -1.322 | 0.1861 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.3521**, Adj R² = **0.3383**, F-statistic = **25.58** (p = **2.98e-53**), Residual SE = **1.849** on **659** df, AIC = **2756.4**, BIC = **2824.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8388** | 0.7435 | ±1.4871 | **+32.062** | **1.51e-225** | *** |
| Education: graduate level (vs college) | -0.2165 | 0.1545 | ±0.3091 | -1.401 | 0.1612 |  |
| Education: high school or below (vs college) | +0.1433 | 0.2958 | ±0.5916 | +0.484 | 0.6280 |  |
| Site: UCSD (vs UAB) | +0.0168 | 0.1971 | ±0.3942 | +0.085 | 0.9323 |  |
| **Site: UW (vs UAB)** | **-0.8920** | 0.1940 | ±0.3881 | **-4.597** | **4.29e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6875** | 0.2091 | ±0.4182 | **-3.287** | **0.0010** | ** |
| **Season: summer (vs autumn)** | **+1.8652** | 0.2381 | ±0.4763 | **+7.832** | **4.80e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6141** | 0.2154 | ±0.4309 | **-7.492** | **6.79e-14** | *** |
| Age (years) | +0.0072 | 0.0069 | ±0.0137 | +1.044 | 0.2965 |  |
| BMI (kg/m2) | +0.0099 | 0.0119 | ±0.0239 | +0.829 | 0.4072 |  |
| Hypertension | +0.2281 | 0.1756 | ±0.3512 | +1.299 | 0.1940 |  |
| High cholesterol | -0.1043 | 0.1551 | ±0.3103 | -0.672 | 0.5015 |  |
| Kidney disease | +0.1126 | 0.2669 | ±0.5338 | +0.422 | 0.6731 |  |
| **Circulatory disease** | **+0.4974** | 0.2534 | ±0.5068 | **+1.963** | **0.0497** | * |
| Mean / SD ratio | +0.0683 | 0.0610 | ±0.1220 | +1.119 | 0.2631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.3517**, Adj R² = **0.3379**, F-statistic = **25.53** (p = **3.56e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.8**, BIC = **2824.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9427** | 0.7183 | ±1.4366 | **+33.331** | **1.35e-243** | *** |
| Education: graduate level (vs college) | -0.2114 | 0.1547 | ±0.3095 | -1.366 | 0.1718 |  |
| Education: high school or below (vs college) | +0.1435 | 0.2965 | ±0.5930 | +0.484 | 0.6284 |  |
| Site: UCSD (vs UAB) | +0.0168 | 0.1972 | ±0.3943 | +0.085 | 0.9320 |  |
| **Site: UW (vs UAB)** | **-0.8922** | 0.1942 | ±0.3885 | **-4.593** | **4.36e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6912** | 0.2091 | ±0.4183 | **-3.305** | **9.51e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8617** | 0.2379 | ±0.4758 | **+7.825** | **5.07e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6217** | 0.2149 | ±0.4298 | **-7.546** | **4.47e-14** | *** |
| Age (years) | +0.0071 | 0.0069 | ±0.0137 | +1.038 | 0.2992 |  |
| BMI (kg/m2) | +0.0103 | 0.0120 | ±0.0239 | +0.858 | 0.3911 |  |
| Hypertension | +0.2237 | 0.1756 | ±0.3512 | +1.274 | 0.2028 |  |
| High cholesterol | -0.1060 | 0.1551 | ±0.3101 | -0.683 | 0.4943 |  |
| Kidney disease | +0.1143 | 0.2670 | ±0.5339 | +0.428 | 0.6685 |  |
| **Circulatory disease** | **+0.4988** | 0.2530 | ±0.5060 | **+1.972** | **0.0486** | * |
| Avg. daily mean/SD | +0.0453 | 0.0480 | ±0.0959 | +0.944 | 0.3450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.3514**, Adj R² = **0.3376**, F-statistic = **25.50** (p = **4.15e-53**), Residual SE = **1.850** on **659** df, AIC = **2757.1**, BIC = **2824.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0364** | 0.7480 | ±1.4960 | **+32.135** | **1.43e-226** | *** |
| Education: graduate level (vs college) | -0.2023 | 0.1538 | ±0.3076 | -1.315 | 0.1885 |  |
| Education: high school or below (vs college) | +0.1287 | 0.2993 | ±0.5986 | +0.430 | 0.6671 |  |
| Site: UCSD (vs UAB) | +0.0288 | 0.1984 | ±0.3967 | +0.145 | 0.8846 |  |
| **Site: UW (vs UAB)** | **-0.8961** | 0.1949 | ±0.3898 | **-4.598** | **4.27e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6958** | 0.2093 | ±0.4187 | **-3.324** | **8.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8684** | 0.2380 | ±0.4760 | **+7.851** | **4.13e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6237** | 0.2154 | ±0.4307 | **-7.539** | **4.74e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.976 | 0.3289 |  |
| BMI (kg/m2) | +0.0101 | 0.0119 | ±0.0238 | +0.849 | 0.3958 |  |
| Hypertension | +0.2258 | 0.1763 | ±0.3525 | +1.281 | 0.2001 |  |
| High cholesterol | -0.1037 | 0.1547 | ±0.3094 | -0.670 | 0.5027 |  |
| Kidney disease | +0.1013 | 0.2674 | ±0.5348 | +0.379 | 0.7047 |  |
| **Circulatory disease** | **+0.5089** | 0.2527 | ±0.5054 | **+2.014** | **0.0440** | * |
| MAG (mg/dL/h) | +0.0071 | 0.0114 | ±0.0228 | +0.623 | 0.5330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.3514**, Adj R² = **0.3377**, F-statistic = **25.51** (p = **4.05e-53**), Residual SE = **1.850** on **659** df, AIC = **2757.0**, BIC = **2824.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5682** | 0.7466 | ±1.4933 | **+32.906** | **1.82e-237** | *** |
| Education: graduate level (vs college) | -0.2008 | 0.1538 | ±0.3076 | -1.305 | 0.1918 |  |
| Education: high school or below (vs college) | +0.1492 | 0.2969 | ±0.5937 | +0.502 | 0.6153 |  |
| Site: UCSD (vs UAB) | +0.0175 | 0.1976 | ±0.3951 | +0.089 | 0.9293 |  |
| **Site: UW (vs UAB)** | **-0.8923** | 0.1944 | ±0.3889 | **-4.589** | **4.45e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6930** | 0.2092 | ±0.4184 | **-3.313** | **9.23e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8608** | 0.2378 | ±0.4756 | **+7.825** | **5.09e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6265** | 0.2150 | ±0.4299 | **-7.567** | **3.83e-14** | *** |
| Age (years) | +0.0070 | 0.0069 | ±0.0138 | +1.016 | 0.3094 |  |
| BMI (kg/m2) | +0.0097 | 0.0120 | ±0.0239 | +0.814 | 0.4154 |  |
| Hypertension | +0.2236 | 0.1759 | ±0.3517 | +1.271 | 0.2036 |  |
| High cholesterol | -0.1059 | 0.1551 | ±0.3102 | -0.683 | 0.4948 |  |
| Kidney disease | +0.1179 | 0.2670 | ±0.5339 | +0.441 | 0.6589 |  |
| **Circulatory disease** | **+0.5088** | 0.2539 | ±0.5078 | **+2.004** | **0.0451** | * |
| Avg. daily range (mg/dL) | -0.0031 | 0.0044 | ±0.0089 | -0.709 | 0.4782 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.46** (p = **4.96e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3413** | 0.6545 | ±1.3091 | **+37.188** | **1.06e-302** | *** |
| Education: graduate level (vs college) | -0.2025 | 0.1539 | ±0.3078 | -1.316 | 0.1882 |  |
| Education: high school or below (vs college) | +0.1420 | 0.2983 | ±0.5965 | +0.476 | 0.6340 |  |
| Site: UCSD (vs UAB) | +0.0234 | 0.1976 | ±0.3952 | +0.119 | 0.9055 |  |
| **Site: UW (vs UAB)** | **-0.8968** | 0.1948 | ±0.3896 | **-4.604** | **4.15e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6910** | 0.2085 | ±0.4169 | **-3.315** | **9.18e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8692** | 0.2399 | ±0.4797 | **+7.793** | **6.56e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6218** | 0.2150 | ±0.4300 | **-7.544** | **4.55e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.964 | 0.3350 |  |
| BMI (kg/m2) | +0.0103 | 0.0120 | ±0.0239 | +0.863 | 0.3882 |  |
| Hypertension | +0.2211 | 0.1758 | ±0.3516 | +1.258 | 0.2085 |  |
| High cholesterol | -0.1021 | 0.1561 | ±0.3122 | -0.654 | 0.5130 |  |
| Kidney disease | +0.1056 | 0.2678 | ±0.5356 | +0.394 | 0.6935 |  |
| **Circulatory disease** | **+0.5075** | 0.2533 | ±0.5066 | **+2.003** | **0.0451** | * |
| SD of daily means (mg/dL) | -0.0087 | 0.0351 | ±0.0702 | -0.249 | 0.8034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.12e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5753** | 2.3499 | ±4.6998 | **+10.458** | **1.35e-25** | *** |
| Education: graduate level (vs college) | -0.2022 | 0.1537 | ±0.3074 | -1.316 | 0.1882 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2985 | ±0.5969 | +0.473 | 0.6364 |  |
| Site: UCSD (vs UAB) | +0.0255 | 0.1976 | ±0.3952 | +0.129 | 0.8973 |  |
| **Site: UW (vs UAB)** | **-0.8987** | 0.1947 | ±0.3893 | **-4.616** | **3.90e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6937** | 0.2090 | ±0.4181 | **-3.318** | **9.06e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8641** | 0.2380 | ±0.4760 | **+7.832** | **4.82e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6251** | 0.2152 | ±0.4304 | **-7.552** | **4.28e-14** | *** |
| Age (years) | +0.0066 | 0.0069 | ±0.0138 | +0.957 | 0.3383 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.837 | 0.4028 |  |
| Hypertension | +0.2212 | 0.1753 | ±0.3507 | +1.261 | 0.2071 |  |
| High cholesterol | -0.1058 | 0.1551 | ±0.3102 | -0.682 | 0.4950 |  |
| Kidney disease | +0.1078 | 0.2666 | ±0.5331 | +0.404 | 0.6860 |  |
| **Circulatory disease** | **+0.5053** | 0.2536 | ±0.5071 | **+1.993** | **0.0463** | * |
| Time in range 70-180, pooled (%) | -0.0027 | 0.0230 | ±0.0460 | -0.119 | 0.9054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.14e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3820** | 2.4572 | ±4.9144 | **+9.923** | **3.32e-23** | *** |
| Education: graduate level (vs college) | -0.2021 | 0.1537 | ±0.3074 | -1.315 | 0.1885 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2984 | ±0.5968 | +0.473 | 0.6363 |  |
| Site: UCSD (vs UAB) | +0.0246 | 0.1975 | ±0.3949 | +0.125 | 0.9009 |  |
| **Site: UW (vs UAB)** | **-0.8981** | 0.1947 | ±0.3895 | **-4.612** | **3.98e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6941** | 0.2091 | ±0.4182 | **-3.319** | **9.02e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2381 | ±0.4761 | **+7.829** | **4.90e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6255** | 0.2153 | ±0.4305 | **-7.551** | **4.31e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.963 | 0.3357 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.839 | 0.4012 |  |
| Hypertension | +0.2214 | 0.1754 | ±0.3509 | +1.262 | 0.2070 |  |
| High cholesterol | -0.1052 | 0.1550 | ±0.3100 | -0.678 | 0.4975 |  |
| Kidney disease | +0.1084 | 0.2664 | ±0.5328 | +0.407 | 0.6839 |  |
| **Circulatory disease** | **+0.5060** | 0.2539 | ±0.5078 | **+1.993** | **0.0463** | * |
| Avg. daily time in range 70-180 (%) | -0.0008 | 0.0242 | ±0.0483 | -0.033 | 0.9739 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.10e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3089** | 0.6325 | ±1.2650 | **+38.432** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2042 | 0.1540 | ±0.3080 | -1.326 | 0.1849 |  |
| Education: high school or below (vs college) | +0.1385 | 0.2977 | ±0.5954 | +0.465 | 0.6418 |  |
| Site: UCSD (vs UAB) | +0.0250 | 0.1993 | ±0.3985 | +0.126 | 0.9000 |  |
| **Site: UW (vs UAB)** | **-0.8986** | 0.1944 | ±0.3887 | **-4.623** | **3.78e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6939** | 0.2088 | ±0.4177 | **-3.323** | **8.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8648** | 0.2379 | ±0.4758 | **+7.839** | **4.55e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6242** | 0.2156 | ±0.4313 | **-7.532** | **4.98e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.963 | 0.3356 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0239 | +0.837 | 0.4023 |  |
| Hypertension | +0.2217 | 0.1756 | ±0.3511 | +1.263 | 0.2065 |  |
| High cholesterol | -0.1045 | 0.1544 | ±0.3088 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1080 | 0.2669 | ±0.5339 | +0.405 | 0.6857 |  |
| **Circulatory disease** | **+0.5052** | 0.2528 | ±0.5056 | **+1.998** | **0.0457** | * |
| Time 54-69, pooled (%) | -0.0179 | 0.1520 | ±0.3039 | -0.118 | 0.9061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.15e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3030** | 0.6324 | ±1.2648 | **+38.429** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2019 | 0.1540 | ±0.3080 | -1.311 | 0.1899 |  |
| Education: high school or below (vs college) | +0.1413 | 0.2980 | ±0.5960 | +0.474 | 0.6355 |  |
| Site: UCSD (vs UAB) | +0.0241 | 0.1999 | ±0.3998 | +0.121 | 0.9039 |  |
| **Site: UW (vs UAB)** | **-0.8980** | 0.1944 | ±0.3889 | **-4.618** | **3.87e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6942** | 0.2088 | ±0.4177 | **-3.324** | **8.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8638** | 0.2379 | ±0.4758 | **+7.834** | **4.74e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6258** | 0.2157 | ±0.4313 | **-7.538** | **4.77e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.964 | 0.3348 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.841 | 0.4005 |  |
| Hypertension | +0.2214 | 0.1756 | ±0.3511 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1049 | 0.1544 | ±0.3089 | -0.679 | 0.4969 |  |
| Kidney disease | +0.1088 | 0.2670 | ±0.5340 | +0.407 | 0.6837 |  |
| **Circulatory disease** | **+0.5064** | 0.2529 | ±0.5057 | **+2.003** | **0.0452** | * |
| Avg. daily time 54-69 (%) | +0.0012 | 0.1403 | ±0.2806 | +0.009 | 0.9931 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.10e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3089** | 0.6325 | ±1.2650 | **+38.432** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2042 | 0.1540 | ±0.3080 | -1.326 | 0.1849 |  |
| Education: high school or below (vs college) | +0.1385 | 0.2977 | ±0.5954 | +0.465 | 0.6418 |  |
| Site: UCSD (vs UAB) | +0.0250 | 0.1993 | ±0.3985 | +0.126 | 0.9000 |  |
| **Site: UW (vs UAB)** | **-0.8986** | 0.1944 | ±0.3887 | **-4.623** | **3.78e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6939** | 0.2088 | ±0.4177 | **-3.323** | **8.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8648** | 0.2379 | ±0.4758 | **+7.839** | **4.55e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6242** | 0.2156 | ±0.4313 | **-7.532** | **4.98e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.963 | 0.3356 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0239 | +0.837 | 0.4023 |  |
| Hypertension | +0.2217 | 0.1756 | ±0.3511 | +1.263 | 0.2065 |  |
| High cholesterol | -0.1045 | 0.1544 | ±0.3088 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1080 | 0.2669 | ±0.5339 | +0.405 | 0.6857 |  |
| **Circulatory disease** | **+0.5052** | 0.2528 | ±0.5056 | **+1.998** | **0.0457** | * |
| Time < 70 (%) | -0.0179 | 0.1520 | ±0.3039 | -0.118 | 0.9061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.15e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3030** | 0.6324 | ±1.2648 | **+38.429** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2019 | 0.1540 | ±0.3080 | -1.311 | 0.1899 |  |
| Education: high school or below (vs college) | +0.1413 | 0.2980 | ±0.5960 | +0.474 | 0.6355 |  |
| Site: UCSD (vs UAB) | +0.0241 | 0.1999 | ±0.3998 | +0.121 | 0.9039 |  |
| **Site: UW (vs UAB)** | **-0.8980** | 0.1944 | ±0.3889 | **-4.618** | **3.87e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6942** | 0.2088 | ±0.4177 | **-3.324** | **8.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8638** | 0.2379 | ±0.4758 | **+7.834** | **4.74e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6258** | 0.2157 | ±0.4313 | **-7.538** | **4.77e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.964 | 0.3348 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.841 | 0.4005 |  |
| Hypertension | +0.2214 | 0.1756 | ±0.3511 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1049 | 0.1544 | ±0.3089 | -0.679 | 0.4969 |  |
| Kidney disease | +0.1088 | 0.2670 | ±0.5340 | +0.407 | 0.6837 |  |
| **Circulatory disease** | **+0.5064** | 0.2529 | ±0.5057 | **+2.003** | **0.0452** | * |
| Avg. daily time < 70 (%) | +0.0012 | 0.1403 | ±0.2806 | +0.009 | 0.9931 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.11e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3028** | 0.6315 | ±1.2629 | **+38.487** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2027 | 0.1537 | ±0.3074 | -1.319 | 0.1873 |  |
| Education: high school or below (vs college) | +0.1406 | 0.2984 | ±0.5968 | +0.471 | 0.6375 |  |
| Site: UCSD (vs UAB) | +0.0260 | 0.1981 | ±0.3962 | +0.131 | 0.8957 |  |
| **Site: UW (vs UAB)** | **-0.8989** | 0.1945 | ±0.3890 | **-4.621** | **3.81e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6935** | 0.2091 | ±0.4181 | **-3.317** | **9.10e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8643** | 0.2379 | ±0.4759 | **+7.836** | **4.67e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6247** | 0.2152 | ±0.4305 | **-7.548** | **4.41e-14** | *** |
| Age (years) | +0.0066 | 0.0069 | ±0.0138 | +0.955 | 0.3394 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.835 | 0.4036 |  |
| Hypertension | +0.2212 | 0.1754 | ±0.3507 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1060 | 0.1554 | ±0.3108 | -0.682 | 0.4954 |  |
| Kidney disease | +0.1074 | 0.2664 | ±0.5328 | +0.403 | 0.6869 |  |
| **Circulatory disease** | **+0.5049** | 0.2536 | ±0.5072 | **+1.991** | **0.0465** | * |
| Time 181-250, pooled (%) | +0.0034 | 0.0233 | ±0.0466 | +0.145 | 0.8846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.14e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3032** | 0.6317 | ±1.2635 | **+38.471** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2022 | 0.1537 | ±0.3074 | -1.315 | 0.1883 |  |
| Education: high school or below (vs college) | +0.1410 | 0.2983 | ±0.5966 | +0.473 | 0.6365 |  |
| Site: UCSD (vs UAB) | +0.0246 | 0.1981 | ±0.3961 | +0.124 | 0.9011 |  |
| **Site: UW (vs UAB)** | **-0.8982** | 0.1946 | ±0.3892 | **-4.615** | **3.93e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6941** | 0.2091 | ±0.4182 | **-3.319** | **9.03e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2380 | ±0.4760 | **+7.832** | **4.80e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6254** | 0.2154 | ±0.4307 | **-7.548** | **4.43e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.962 | 0.3359 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.840 | 0.4011 |  |
| Hypertension | +0.2214 | 0.1755 | ±0.3509 | +1.262 | 0.2070 |  |
| High cholesterol | -0.1051 | 0.1554 | ±0.3108 | -0.677 | 0.4987 |  |
| Kidney disease | +0.1084 | 0.2662 | ±0.5325 | +0.407 | 0.6838 |  |
| **Circulatory disease** | **+0.5060** | 0.2540 | ±0.5080 | **+1.992** | **0.0464** | * |
| Avg. daily time 181-250 (%) | +0.0007 | 0.0245 | ±0.0489 | +0.030 | 0.9761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.11e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3028** | 0.6315 | ±1.2629 | **+38.487** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2027 | 0.1537 | ±0.3074 | -1.319 | 0.1873 |  |
| Education: high school or below (vs college) | +0.1406 | 0.2984 | ±0.5968 | +0.471 | 0.6375 |  |
| Site: UCSD (vs UAB) | +0.0260 | 0.1981 | ±0.3962 | +0.131 | 0.8957 |  |
| **Site: UW (vs UAB)** | **-0.8989** | 0.1945 | ±0.3890 | **-4.621** | **3.81e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6935** | 0.2091 | ±0.4181 | **-3.317** | **9.10e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8643** | 0.2379 | ±0.4759 | **+7.836** | **4.67e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6247** | 0.2152 | ±0.4305 | **-7.548** | **4.41e-14** | *** |
| Age (years) | +0.0066 | 0.0069 | ±0.0138 | +0.955 | 0.3394 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.835 | 0.4036 |  |
| Hypertension | +0.2212 | 0.1754 | ±0.3507 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1060 | 0.1554 | ±0.3108 | -0.682 | 0.4954 |  |
| Kidney disease | +0.1074 | 0.2664 | ±0.5328 | +0.403 | 0.6869 |  |
| **Circulatory disease** | **+0.5049** | 0.2536 | ±0.5072 | **+1.991** | **0.0465** | * |
| Time > 180 (%) | +0.0034 | 0.0233 | ±0.0466 | +0.145 | 0.8846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.14e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3032** | 0.6317 | ±1.2635 | **+38.471** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2022 | 0.1537 | ±0.3074 | -1.315 | 0.1883 |  |
| Education: high school or below (vs college) | +0.1410 | 0.2983 | ±0.5966 | +0.473 | 0.6365 |  |
| Site: UCSD (vs UAB) | +0.0246 | 0.1981 | ±0.3961 | +0.124 | 0.9011 |  |
| **Site: UW (vs UAB)** | **-0.8982** | 0.1946 | ±0.3892 | **-4.615** | **3.93e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6941** | 0.2091 | ±0.4182 | **-3.319** | **9.03e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2380 | ±0.4760 | **+7.832** | **4.80e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6254** | 0.2154 | ±0.4307 | **-7.548** | **4.43e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.962 | 0.3359 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.840 | 0.4011 |  |
| Hypertension | +0.2214 | 0.1755 | ±0.3509 | +1.262 | 0.2070 |  |
| High cholesterol | -0.1051 | 0.1554 | ±0.3108 | -0.677 | 0.4987 |  |
| Kidney disease | +0.1084 | 0.2662 | ±0.5325 | +0.407 | 0.6838 |  |
| **Circulatory disease** | **+0.5060** | 0.2540 | ±0.5080 | **+1.992** | **0.0464** | * |
| Avg. daily time > 180 (%) | +0.0007 | 0.0245 | ±0.0489 | +0.030 | 0.9761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.3517**, Adj R² = **0.3379**, F-statistic = **25.53** (p = **3.56e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.8**, BIC = **2824.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3114** | 0.6290 | ±1.2580 | **+38.652** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2006 | 0.1536 | ±0.3073 | -1.306 | 0.1916 |  |
| Education: high school or below (vs college) | +0.1337 | 0.2987 | ±0.5975 | +0.448 | 0.6544 |  |
| Site: UCSD (vs UAB) | +0.0302 | 0.1978 | ±0.3956 | +0.153 | 0.8787 |  |
| **Site: UW (vs UAB)** | **-0.9028** | 0.1944 | ±0.3888 | **-4.644** | **3.42e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6930** | 0.2084 | ±0.4169 | **-3.325** | **8.85e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2377 | ±0.4755 | **+7.841** | **4.49e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6270** | 0.2150 | ±0.4300 | **-7.567** | **3.81e-14** | *** |
| Age (years) | +0.0069 | 0.0069 | ±0.0138 | +0.993 | 0.3205 |  |
| BMI (kg/m2) | +0.0088 | 0.0120 | ±0.0239 | +0.738 | 0.4608 |  |
| Hypertension | +0.2250 | 0.1755 | ±0.3511 | +1.282 | 0.1999 |  |
| High cholesterol | -0.1183 | 0.1570 | ±0.3141 | -0.753 | 0.4514 |  |
| Kidney disease | +0.1100 | 0.2665 | ±0.5330 | +0.413 | 0.6798 |  |
| **Circulatory disease** | **+0.5065** | 0.2526 | ±0.5053 | **+2.005** | **0.0450** | * |
| Nocturnal time > 180 (%) | +0.0205 | 0.0215 | ±0.0430 | +0.953 | 0.3405 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.2904**, Adj R² = **0.2764**, F-statistic = **20.77** (p = **2.09e-41**), Residual SE = **5.696** on **660** df, AIC = **4271.9**, BIC = **4335.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1962** | 1.6957 | ±3.3915 | **+29.602** | **1.43e-192** | *** |
| **Education: graduate level (vs college)** | **+1.3181** | 0.4746 | ±0.9493 | **+2.777** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.1824 | 0.9085 | ±1.8170 | +0.201 | 0.8409 |  |
| **Site: UCSD (vs UAB)** | **+3.1257** | 0.6106 | ±1.2211 | **+5.119** | **3.06e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9015** | 0.5738 | ±1.1476 | **-3.314** | **9.20e-04** | *** |
| Season: spring (vs autumn) | -0.9288 | 0.6414 | ±1.2828 | -1.448 | 0.1476 |  |
| **Season: summer (vs autumn)** | **+2.4749** | 0.6646 | ±1.3291 | **+3.724** | **1.96e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9883** | 0.6541 | ±1.3082 | **-7.626** | **2.42e-14** | *** |
| **Age (years)** | **-0.0477** | 0.0208 | ±0.0415 | **-2.297** | **0.0216** | * |
| BMI (kg/m2) | -0.0548 | 0.0340 | ±0.0680 | -1.611 | 0.1072 |  |
| Hypertension | +0.1131 | 0.5185 | ±1.0370 | +0.218 | 0.8274 |  |
| High cholesterol | -0.9252 | 0.4809 | ±0.9617 | -1.924 | 0.0543 | . |
| Kidney disease | -0.4924 | 0.8778 | ±1.7556 | -0.561 | 0.5748 |  |
| Circulatory disease | -0.8169 | 0.7057 | ±1.4113 | -1.158 | 0.2470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.2908**, Adj R² = **0.2758**, F-statistic = **19.30** (p = **8.01e-41**), Residual SE = **5.699** on **659** df, AIC = **4273.5**, BIC = **4341.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8821** | 3.9030 | ±7.8060 | **+12.268** | **1.35e-34** | *** |
| **Education: graduate level (vs college)** | **+1.3126** | 0.4758 | ±0.9516 | **+2.759** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1745 | 0.9052 | ±1.8104 | +0.193 | 0.8471 |  |
| **Site: UCSD (vs UAB)** | **+3.1251** | 0.6113 | ±1.2225 | **+5.112** | **3.18e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9099** | 0.5746 | ±1.1491 | **-3.324** | **8.87e-04** | *** |
| Season: spring (vs autumn) | -0.8639 | 0.6493 | ±1.2986 | -1.331 | 0.1833 |  |
| **Season: summer (vs autumn)** | **+2.4856** | 0.6652 | ±1.3305 | **+3.736** | **1.87e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9508** | 0.6531 | ±1.3063 | **-7.580** | **3.45e-14** | *** |
| **Age (years)** | **-0.0494** | 0.0212 | ±0.0425 | **-2.327** | **0.0200** | * |
| BMI (kg/m2) | -0.0578 | 0.0345 | ±0.0690 | -1.676 | 0.0937 | . |
| Hypertension | +0.0884 | 0.5231 | ±1.0462 | +0.169 | 0.8658 |  |
| **High cholesterol** | **-0.9590** | 0.4803 | ±0.9606 | **-1.997** | **0.0459** | * |
| Kidney disease | -0.4983 | 0.8759 | ±1.7517 | -0.569 | 0.5694 |  |
| Circulatory disease | -0.7958 | 0.7036 | ±1.4073 | -1.131 | 0.2581 |  |
| HbA1c (%) | +0.4478 | 0.7000 | ±1.4001 | +0.640 | 0.5224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.2907**, Adj R² = **0.2756**, F-statistic = **19.29** (p = **8.53e-41**), Residual SE = **5.699** on **659** df, AIC = **4273.6**, BIC = **4341.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0218** | 2.7763 | ±5.5526 | **+17.657** | **8.96e-70** | *** |
| **Education: graduate level (vs college)** | **+1.3011** | 0.4751 | ±0.9503 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1647 | 0.9098 | ±1.8195 | +0.181 | 0.8563 |  |
| **Site: UCSD (vs UAB)** | **+3.1420** | 0.6125 | ±1.2251 | **+5.129** | **2.91e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9207** | 0.5739 | ±1.1478 | **-3.347** | **8.18e-04** | *** |
| Season: spring (vs autumn) | -0.9228 | 0.6434 | ±1.2868 | -1.434 | 0.1515 |  |
| **Season: summer (vs autumn)** | **+2.4721** | 0.6669 | ±1.3338 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9764** | 0.6549 | ±1.3098 | **-7.599** | **2.99e-14** | *** |
| **Age (years)** | **-0.0482** | 0.0208 | ±0.0416 | **-2.315** | **0.0206** | * |
| BMI (kg/m2) | -0.0568 | 0.0341 | ±0.0682 | -1.668 | 0.0954 | . |
| Hypertension | +0.0958 | 0.5204 | ±1.0408 | +0.184 | 0.8539 |  |
| High cholesterol | -0.9252 | 0.4811 | ±0.9623 | -1.923 | 0.0545 | . |
| Kidney disease | -0.5144 | 0.8779 | ±1.7557 | -0.586 | 0.5579 |  |
| Circulatory disease | -0.8384 | 0.7090 | ±1.4180 | -1.183 | 0.2370 |  |
| Mean glucose (mg/dL) | +0.0108 | 0.0195 | ±0.0390 | +0.552 | 0.5809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.2907**, Adj R² = **0.2756**, F-statistic = **19.29** (p = **8.53e-41**), Residual SE = **5.699** on **659** df, AIC = **4273.6**, BIC = **4341.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5340** | 5.1773 | ±10.3547 | **+9.181** | **4.26e-20** | *** |
| **Education: graduate level (vs college)** | **+1.3011** | 0.4751 | ±0.9503 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1647 | 0.9098 | ±1.8195 | +0.181 | 0.8563 |  |
| **Site: UCSD (vs UAB)** | **+3.1420** | 0.6125 | ±1.2251 | **+5.129** | **2.91e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9207** | 0.5739 | ±1.1478 | **-3.347** | **8.18e-04** | *** |
| Season: spring (vs autumn) | -0.9228 | 0.6434 | ±1.2868 | -1.434 | 0.1515 |  |
| **Season: summer (vs autumn)** | **+2.4721** | 0.6669 | ±1.3338 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9764** | 0.6549 | ±1.3098 | **-7.599** | **2.99e-14** | *** |
| **Age (years)** | **-0.0482** | 0.0208 | ±0.0416 | **-2.315** | **0.0206** | * |
| BMI (kg/m2) | -0.0568 | 0.0341 | ±0.0682 | -1.668 | 0.0954 | . |
| Hypertension | +0.0958 | 0.5204 | ±1.0408 | +0.184 | 0.8539 |  |
| High cholesterol | -0.9252 | 0.4811 | ±0.9623 | -1.923 | 0.0545 | . |
| Kidney disease | -0.5144 | 0.8779 | ±1.7557 | -0.586 | 0.5579 |  |
| Circulatory disease | -0.8384 | 0.7090 | ±1.4180 | -1.183 | 0.2370 |  |
| GMI (%) | +0.4495 | 0.8142 | ±1.6283 | +0.552 | 0.5809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.2910**, Adj R² = **0.2760**, F-statistic = **19.32** (p = **7.25e-41**), Residual SE = **5.698** on **659** df, AIC = **4273.2**, BIC = **4340.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6935** | 2.6130 | ±5.2260 | **+18.635** | **1.67e-77** | *** |
| **Education: graduate level (vs college)** | **+1.3033** | 0.4750 | ±0.9501 | **+2.744** | **0.0061** | ** |
| Education: high school or below (vs college) | +0.1621 | 0.9110 | ±1.8219 | +0.178 | 0.8588 |  |
| **Site: UCSD (vs UAB)** | **+3.1294** | 0.6120 | ±1.2241 | **+5.113** | **3.17e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9297** | 0.5738 | ±1.1477 | **-3.363** | **7.72e-04** | *** |
| Season: spring (vs autumn) | -0.9375 | 0.6418 | ±1.2835 | -1.461 | 0.1441 |  |
| **Season: summer (vs autumn)** | **+2.4605** | 0.6678 | ±1.3356 | **+3.685** | **2.29e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9907** | 0.6561 | ±1.3121 | **-7.607** | **2.80e-14** | *** |
| **Age (years)** | **-0.0470** | 0.0208 | ±0.0416 | **-2.261** | **0.0238** | * |
| BMI (kg/m2) | -0.0608 | 0.0349 | ±0.0697 | -1.744 | 0.0811 | . |
| Hypertension | +0.0982 | 0.5190 | ±1.0380 | +0.189 | 0.8499 |  |
| High cholesterol | -0.9380 | 0.4808 | ±0.9616 | -1.951 | 0.0510 | . |
| Kidney disease | -0.5068 | 0.8819 | ±1.7637 | -0.575 | 0.5655 |  |
| Circulatory disease | -0.8398 | 0.7089 | ±1.4178 | -1.185 | 0.2362 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0141 | 0.0177 | ±0.0354 | +0.795 | 0.4268 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.2939**, Adj R² = **0.2789**, F-statistic = **19.60** (p = **2.00e-41**), Residual SE = **5.686** on **659** df, AIC = **4270.5**, BIC = **4338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4321** | 1.9837 | ±3.9674 | **+24.415** | **1.19e-131** | *** |
| **Education: graduate level (vs college)** | **+1.3516** | 0.4744 | ±0.9488 | **+2.849** | **0.0044** | ** |
| Education: high school or below (vs college) | +0.1483 | 0.9039 | ±1.8078 | +0.164 | 0.8697 |  |
| **Site: UCSD (vs UAB)** | **+3.1971** | 0.6077 | ±1.2153 | **+5.261** | **1.43e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9526** | 0.5702 | ±1.1405 | **-3.424** | **6.16e-04** | *** |
| Season: spring (vs autumn) | -0.9317 | 0.6398 | ±1.2797 | -1.456 | 0.1454 |  |
| **Season: summer (vs autumn)** | **+2.4626** | 0.6643 | ±1.3286 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0124** | 0.6570 | ±1.3139 | **-7.630** | **2.35e-14** | *** |
| **Age (years)** | **-0.0513** | 0.0207 | ±0.0414 | **-2.478** | **0.0132** | * |
| BMI (kg/m2) | -0.0577 | 0.0343 | ±0.0686 | -1.681 | 0.0927 | . |
| Hypertension | +0.0608 | 0.5186 | ±1.0372 | +0.117 | 0.9067 |  |
| High cholesterol | -0.9399 | 0.4809 | ±0.9619 | -1.954 | 0.0507 | . |
| Kidney disease | -0.5424 | 0.8717 | ±1.7435 | -0.622 | 0.5338 |  |
| Circulatory disease | -0.8091 | 0.7003 | ±1.4006 | -1.155 | 0.2479 |  |
| Glucose SD, pooled (mg/dL) | +0.1088 | 0.0593 | ±0.1186 | +1.834 | 0.0666 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.2942**, Adj R² = **0.2792**, F-statistic = **19.62** (p = **1.76e-41**), Residual SE = **5.685** on **659** df, AIC = **4270.2**, BIC = **4337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5183** | 1.9620 | ±3.9240 | **+24.729** | **5.20e-135** | *** |
| **Education: graduate level (vs college)** | **+1.3370** | 0.4741 | ±0.9482 | **+2.820** | **0.0048** | ** |
| Education: high school or below (vs college) | +0.1425 | 0.9050 | ±1.8099 | +0.157 | 0.8749 |  |
| **Site: UCSD (vs UAB)** | **+3.2109** | 0.6065 | ±1.2130 | **+5.294** | **1.20e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9518** | 0.5706 | ±1.1412 | **-3.421** | **6.25e-04** | *** |
| Season: spring (vs autumn) | -0.9159 | 0.6399 | ±1.2799 | -1.431 | 0.1524 |  |
| **Season: summer (vs autumn)** | **+2.4828** | 0.6637 | ±1.3275 | **+3.741** | **1.84e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9783** | 0.6558 | ±1.3116 | **-7.591** | **3.18e-14** | *** |
| **Age (years)** | **-0.0514** | 0.0206 | ±0.0412 | **-2.493** | **0.0127** | * |
| BMI (kg/m2) | -0.0587 | 0.0345 | ±0.0690 | -1.700 | 0.0891 | . |
| Hypertension | +0.0661 | 0.5185 | ±1.0370 | +0.127 | 0.8986 |  |
| High cholesterol | -0.9346 | 0.4815 | ±0.9630 | -1.941 | 0.0523 | . |
| Kidney disease | -0.5625 | 0.8690 | ±1.7380 | -0.647 | 0.5175 |  |
| Circulatory disease | -0.8118 | 0.7001 | ±1.4002 | -1.160 | 0.2462 |  |
| Avg. daily SD (mg/dL) | +0.1146 | 0.0602 | ±0.1204 | +1.903 | 0.0570 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.2938**, Adj R² = **0.2788**, F-statistic = **19.58** (p = **2.13e-41**), Residual SE = **5.687** on **659** df, AIC = **4270.6**, BIC = **4338.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.0217** | 2.1218 | ±4.2436 | **+22.633** | **2.06e-113** | *** |
| **Education: graduate level (vs college)** | **+1.3898** | 0.4737 | ±0.9474 | **+2.934** | **0.0033** | ** |
| Education: high school or below (vs college) | +0.1825 | 0.9022 | ±1.8044 | +0.202 | 0.8397 |  |
| **Site: UCSD (vs UAB)** | **+3.1777** | 0.6066 | ±1.2131 | **+5.239** | **1.62e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9228** | 0.5699 | ±1.1399 | **-3.374** | **7.42e-04** | *** |
| Season: spring (vs autumn) | -0.9441 | 0.6390 | ±1.2780 | -1.478 | 0.1395 |  |
| **Season: summer (vs autumn)** | **+2.4602** | 0.6617 | ±1.3235 | **+3.718** | **2.01e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0456** | 0.6559 | ±1.3118 | **-7.693** | **1.44e-14** | *** |
| **Age (years)** | **-0.0507** | 0.0207 | ±0.0414 | **-2.452** | **0.0142** | * |
| BMI (kg/m2) | -0.0541 | 0.0341 | ±0.0682 | -1.586 | 0.1128 |  |
| Hypertension | +0.0815 | 0.5173 | ±1.0346 | +0.158 | 0.8748 |  |
| High cholesterol | -0.9352 | 0.4817 | ±0.9633 | -1.942 | 0.0522 | . |
| Kidney disease | -0.5118 | 0.8729 | ±1.7458 | -0.586 | 0.5577 |  |
| Circulatory disease | -0.7708 | 0.6987 | ±1.3973 | -1.103 | 0.2699 |  |
| CV (%) | +0.1447 | 0.0824 | ±0.1648 | +1.756 | 0.0792 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.2923**, Adj R² = **0.2772**, F-statistic = **19.44** (p = **4.19e-41**), Residual SE = **5.693** on **659** df, AIC = **4272.1**, BIC = **4339.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.9864** | 2.2146 | ±4.4292 | **+23.474** | **7.44e-122** | *** |
| **Education: graduate level (vs college)** | **+1.3737** | 0.4741 | ±0.9482 | **+2.898** | **0.0038** | ** |
| Education: high school or below (vs college) | +0.1739 | 0.9053 | ±1.8106 | +0.192 | 0.8477 |  |
| **Site: UCSD (vs UAB)** | **+3.1545** | 0.6079 | ±1.2158 | **+5.189** | **2.11e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9248** | 0.5721 | ±1.1441 | **-3.365** | **7.67e-04** | *** |
| Season: spring (vs autumn) | -0.9549 | 0.6394 | ±1.2788 | -1.493 | 0.1353 |  |
| **Season: summer (vs autumn)** | **+2.4695** | 0.6639 | ±1.3278 | **+3.720** | **1.99e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0330** | 0.6567 | ±1.3134 | **-7.664** | **1.80e-14** | *** |
| **Age (years)** | **-0.0496** | 0.0208 | ±0.0415 | **-2.392** | **0.0168** | * |
| BMI (kg/m2) | -0.0543 | 0.0341 | ±0.0681 | -1.594 | 0.1110 |  |
| Hypertension | +0.0875 | 0.5182 | ±1.0364 | +0.169 | 0.8660 |  |
| High cholesterol | -0.9277 | 0.4818 | ±0.9636 | -1.925 | 0.0542 | . |
| Kidney disease | -0.5074 | 0.8749 | ±1.7498 | -0.580 | 0.5620 |  |
| Circulatory disease | -0.7825 | 0.7013 | ±1.4027 | -1.116 | 0.2645 |  |
| Mean / SD ratio | -0.2631 | 0.2062 | ±0.4125 | -1.276 | 0.2021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.2938**, Adj R² = **0.2788**, F-statistic = **19.58** (p = **2.15e-41**), Residual SE = **5.687** on **659** df, AIC = **4270.6**, BIC = **4338.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4589** | 2.1891 | ±4.3782 | **+23.964** | **6.68e-127** | *** |
| **Education: graduate level (vs college)** | **+1.3768** | 0.4722 | ±0.9444 | **+2.916** | **0.0036** | ** |
| Education: high school or below (vs college) | +0.1673 | 0.9051 | ±1.8103 | +0.185 | 0.8534 |  |
| **Site: UCSD (vs UAB)** | **+3.1722** | 0.6051 | ±1.2103 | **+5.242** | **1.59e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9381** | 0.5718 | ±1.1436 | **-3.390** | **7.00e-04** | *** |
| Season: spring (vs autumn) | -0.9481 | 0.6375 | ±1.2750 | -1.487 | 0.1370 |  |
| **Season: summer (vs autumn)** | **+2.4879** | 0.6620 | ±1.3241 | **+3.758** | **1.71e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0132** | 0.6542 | ±1.3084 | **-7.663** | **1.82e-14** | *** |
| **Age (years)** | **-0.0506** | 0.0207 | ±0.0413 | **-2.448** | **0.0144** | * |
| BMI (kg/m2) | -0.0563 | 0.0343 | ±0.0687 | -1.638 | 0.1015 |  |
| Hypertension | +0.0989 | 0.5163 | ±1.0325 | +0.192 | 0.8481 |  |
| High cholesterol | -0.9185 | 0.4825 | ±0.9650 | -1.903 | 0.0570 | . |
| Kidney disease | -0.5273 | 0.8710 | ±1.7420 | -0.605 | 0.5449 |  |
| Circulatory disease | -0.7698 | 0.6977 | ±1.3954 | -1.103 | 0.2699 |  |
| Avg. daily mean/SD | -0.2842 | 0.1728 | ±0.3457 | -1.644 | 0.1001 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.2906**, Adj R² = **0.2755**, F-statistic = **19.28** (p = **8.92e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.7**, BIC = **4341.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7365** | 2.1037 | ±4.2074 | **+24.118** | **1.62e-128** | *** |
| **Education: graduate level (vs college)** | **+1.3185** | 0.4751 | ±0.9502 | **+2.775** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.2074 | 0.9184 | ±1.8368 | +0.226 | 0.8213 |  |
| **Site: UCSD (vs UAB)** | **+3.1164** | 0.6123 | ±1.2247 | **+5.089** | **3.59e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9054** | 0.5740 | ±1.1480 | **-3.319** | **9.02e-04** | *** |
| Season: spring (vs autumn) | -0.9255 | 0.6431 | ±1.2861 | -1.439 | 0.1501 |  |
| **Season: summer (vs autumn)** | **+2.4656** | 0.6668 | ±1.3336 | **+3.698** | **2.17e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9924** | 0.6545 | ±1.3090 | **-7.628** | **2.38e-14** | *** |
| **Age (years)** | **-0.0478** | 0.0208 | ±0.0415 | **-2.303** | **0.0213** | * |
| BMI (kg/m2) | -0.0550 | 0.0341 | ±0.0681 | -1.614 | 0.1066 |  |
| Hypertension | +0.1042 | 0.5181 | ±1.0362 | +0.201 | 0.8406 |  |
| High cholesterol | -0.9277 | 0.4814 | ±0.9629 | -1.927 | 0.0540 | . |
| Kidney disease | -0.4774 | 0.8831 | ±1.7662 | -0.541 | 0.5888 |  |
| Circulatory disease | -0.8220 | 0.7070 | ±1.4140 | -1.163 | 0.2449 |  |
| MAG (mg/dL/h) | -0.0144 | 0.0340 | ±0.0680 | -0.424 | 0.6714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.2917**, Adj R² = **0.2767**, F-statistic = **19.39** (p = **5.34e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8951** | 2.0939 | ±4.1878 | **+23.351** | **1.34e-120** | *** |
| **Education: graduate level (vs college)** | **+1.3116** | 0.4759 | ±0.9517 | **+2.756** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1427 | 0.9063 | ±1.8126 | +0.157 | 0.8749 |  |
| **Site: UCSD (vs UAB)** | **+3.1586** | 0.6082 | ±1.2165 | **+5.193** | **2.07e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9293** | 0.5747 | ±1.1495 | **-3.357** | **7.89e-04** | *** |
| Season: spring (vs autumn) | -0.9348 | 0.6388 | ±1.2776 | -1.463 | 0.1434 |  |
| **Season: summer (vs autumn)** | **+2.4897** | 0.6639 | ±1.3277 | **+3.750** | **1.77e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9843** | 0.6559 | ±1.3119 | **-7.599** | **2.99e-14** | *** |
| **Age (years)** | **-0.0494** | 0.0207 | ±0.0414 | **-2.385** | **0.0171** | * |
| BMI (kg/m2) | -0.0534 | 0.0341 | ±0.0681 | -1.569 | 0.1168 |  |
| Hypertension | +0.1025 | 0.5194 | ±1.0388 | +0.197 | 0.8436 |  |
| High cholesterol | -0.9204 | 0.4828 | ±0.9656 | -1.906 | 0.0566 | . |
| Kidney disease | -0.5372 | 0.8736 | ±1.7472 | -0.615 | 0.5386 |  |
| Circulatory disease | -0.8290 | 0.7052 | ±1.4104 | -1.176 | 0.2397 |  |
| Avg. daily range (mg/dL) | +0.0155 | 0.0141 | ±0.0281 | +1.099 | 0.2717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.2917**, Adj R² = **0.2766**, F-statistic = **19.38** (p = **5.46e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7234** | 1.7437 | ±3.4874 | **+28.516** | **7.47e-179** | *** |
| **Education: graduate level (vs college)** | **+1.3233** | 0.4758 | ±0.9517 | **+2.781** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.1709 | 0.9093 | ±1.8186 | +0.188 | 0.8509 |  |
| **Site: UCSD (vs UAB)** | **+3.1354** | 0.6119 | ±1.2239 | **+5.124** | **3.00e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9168** | 0.5721 | ±1.1441 | **-3.351** | **8.06e-04** | *** |
| Season: spring (vs autumn) | -0.9696 | 0.6454 | ±1.2908 | -1.502 | 0.1330 |  |
| **Season: summer (vs autumn)** | **+2.4082** | 0.6692 | ±1.3385 | **+3.598** | **3.20e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0358** | 0.6586 | ±1.3172 | **-7.646** | **2.07e-14** | *** |
| **Age (years)** | **-0.0477** | 0.0208 | ±0.0415 | **-2.298** | **0.0216** | * |
| BMI (kg/m2) | -0.0585 | 0.0344 | ±0.0687 | -1.703 | 0.0886 | . |
| Hypertension | +0.1171 | 0.5196 | ±1.0391 | +0.225 | 0.8217 |  |
| **High cholesterol** | **-0.9599** | 0.4814 | ±0.9628 | **-1.994** | **0.0462** | * |
| Kidney disease | -0.4527 | 0.8799 | ±1.7598 | -0.514 | 0.6069 |  |
| Circulatory disease | -0.8317 | 0.7000 | ±1.3999 | -1.188 | 0.2348 |  |
| SD of daily means (mg/dL) | +0.1088 | 0.1053 | ±0.2105 | +1.034 | 0.3012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.2915**, Adj R² = **0.2765**, F-statistic = **19.37** (p = **5.85e-41**), Residual SE = **5.696** on **659** df, AIC = **4272.8**, BIC = **4340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7430** | 7.7202 | ±15.4404 | **+7.609** | **2.76e-14** | *** |
| **Education: graduate level (vs college)** | **+1.3126** | 0.4756 | ±0.9511 | **+2.760** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1830 | 0.9078 | ±1.8156 | +0.202 | 0.8402 |  |
| **Site: UCSD (vs UAB)** | **+3.1658** | 0.6141 | ±1.2282 | **+5.155** | **2.53e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9227** | 0.5727 | ±1.1454 | **-3.357** | **7.87e-04** | *** |
| Season: spring (vs autumn) | -0.9114 | 0.6430 | ±1.2861 | -1.417 | 0.1564 |  |
| **Season: summer (vs autumn)** | **+2.4828** | 0.6663 | ±1.3326 | **+3.726** | **1.94e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9704** | 0.6552 | ±1.3105 | **-7.586** | **3.31e-14** | *** |
| **Age (years)** | **-0.0489** | 0.0207 | ±0.0415 | **-2.359** | **0.0183** | * |
| BMI (kg/m2) | -0.0564 | 0.0342 | ±0.0685 | -1.647 | 0.0995 | . |
| Hypertension | +0.1051 | 0.5181 | ±1.0361 | +0.203 | 0.8392 |  |
| **High cholesterol** | **-0.9545** | 0.4811 | ±0.9623 | **-1.984** | **0.0473** | * |
| Kidney disease | -0.5232 | 0.8740 | ±1.7481 | -0.599 | 0.5494 |  |
| Circulatory disease | -0.8481 | 0.7063 | ±1.4126 | -1.201 | 0.2298 |  |
| Time in range 70-180, pooled (%) | -0.0859 | 0.0765 | ±0.1530 | -1.122 | 0.2617 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.2917**, Adj R² = **0.2767**, F-statistic = **19.39** (p = **5.36e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6582** | 7.8600 | ±15.7200 | **+7.590** | **3.20e-14** | *** |
| **Education: graduate level (vs college)** | **+1.3115** | 0.4755 | ±0.9510 | **+2.758** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1858 | 0.9083 | ±1.8166 | +0.205 | 0.8379 |  |
| **Site: UCSD (vs UAB)** | **+3.1704** | 0.6143 | ±1.2287 | **+5.161** | **2.46e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9205** | 0.5726 | ±1.1451 | **-3.354** | **7.96e-04** | *** |
| Season: spring (vs autumn) | -0.9103 | 0.6429 | ±1.2858 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4827** | 0.6661 | ±1.3321 | **+3.727** | **1.93e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9657** | 0.6553 | ±1.3106 | **-7.578** | **3.52e-14** | *** |
| **Age (years)** | **-0.0488** | 0.0207 | ±0.0414 | **-2.359** | **0.0183** | * |
| BMI (kg/m2) | -0.0570 | 0.0343 | ±0.0687 | -1.660 | 0.0969 | . |
| Hypertension | +0.1075 | 0.5180 | ±1.0360 | +0.207 | 0.8356 |  |
| **High cholesterol** | **-0.9575** | 0.4812 | ±0.9625 | **-1.990** | **0.0466** | * |
| Kidney disease | -0.5300 | 0.8727 | ±1.7455 | -0.607 | 0.5437 |  |
| Circulatory disease | -0.8561 | 0.7065 | ±1.4129 | -1.212 | 0.2256 |  |
| Avg. daily time in range 70-180 (%) | -0.0950 | 0.0783 | ±0.1566 | -1.213 | 0.2252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.2905**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.14e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.7**, BIC = **4341.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1462** | 1.7060 | ±3.4120 | **+29.394** | **6.60e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3367** | 0.4762 | ±0.9524 | **+2.807** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.2055 | 0.9083 | ±1.8165 | +0.226 | 0.8210 |  |
| **Site: UCSD (vs UAB)** | **+3.1185** | 0.6108 | ±1.2217 | **+5.105** | **3.30e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8966** | 0.5746 | ±1.1491 | **-3.301** | **9.64e-04** | *** |
| Season: spring (vs autumn) | -0.9321 | 0.6414 | ±1.2828 | -1.453 | 0.1461 |  |
| **Season: summer (vs autumn)** | **+2.4662** | 0.6638 | ±1.3277 | **+3.715** | **2.03e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0014** | 0.6556 | ±1.3112 | **-7.629** | **2.37e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.291** | **0.0220** | * |
| BMI (kg/m2) | -0.0545 | 0.0340 | ±0.0681 | -1.601 | 0.1093 |  |
| Hypertension | +0.1102 | 0.5189 | ±1.0379 | +0.212 | 0.8319 |  |
| High cholesterol | -0.9291 | 0.4816 | ±0.9632 | -1.929 | 0.0537 | . |
| Kidney disease | -0.4859 | 0.8778 | ±1.7557 | -0.554 | 0.5799 |  |
| Circulatory disease | -0.8070 | 0.7064 | ±1.4128 | -1.142 | 0.2533 |  |
| Time 54-69, pooled (%) | +0.1591 | 0.4473 | ±0.8946 | +0.356 | 0.7220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.2904**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.47e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.8**, BIC = **4341.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1654** | 1.7044 | ±3.4088 | **+29.433** | **2.09e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3313** | 0.4761 | ±0.9522 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.1989 | 0.9085 | ±1.8170 | +0.219 | 0.8267 |  |
| **Site: UCSD (vs UAB)** | **+3.1184** | 0.6108 | ±1.2217 | **+5.105** | **3.31e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8987** | 0.5744 | ±1.1488 | **-3.306** | **9.48e-04** | *** |
| Season: spring (vs autumn) | -0.9294 | 0.6415 | ±1.2830 | -1.449 | 0.1474 |  |
| **Season: summer (vs autumn)** | **+2.4703** | 0.6642 | ±1.3284 | **+3.719** | **2.00e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9982** | 0.6558 | ±1.3116 | **-7.622** | **2.51e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.294** | **0.0218** | * |
| BMI (kg/m2) | -0.0546 | 0.0340 | ±0.0681 | -1.603 | 0.1089 |  |
| Hypertension | +0.1115 | 0.5190 | ±1.0381 | +0.215 | 0.8299 |  |
| High cholesterol | -0.9275 | 0.4815 | ±0.9631 | -1.926 | 0.0541 | . |
| Kidney disease | -0.4890 | 0.8782 | ±1.7563 | -0.557 | 0.5776 |  |
| Circulatory disease | -0.8081 | 0.7074 | ±1.4147 | -1.142 | 0.2533 |  |
| Avg. daily time 54-69 (%) | +0.1059 | 0.4315 | ±0.8631 | +0.245 | 0.8061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.2905**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.14e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.7**, BIC = **4341.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1462** | 1.7060 | ±3.4120 | **+29.394** | **6.60e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3367** | 0.4762 | ±0.9524 | **+2.807** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.2055 | 0.9083 | ±1.8165 | +0.226 | 0.8210 |  |
| **Site: UCSD (vs UAB)** | **+3.1185** | 0.6108 | ±1.2217 | **+5.105** | **3.30e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8966** | 0.5746 | ±1.1491 | **-3.301** | **9.64e-04** | *** |
| Season: spring (vs autumn) | -0.9321 | 0.6414 | ±1.2828 | -1.453 | 0.1461 |  |
| **Season: summer (vs autumn)** | **+2.4662** | 0.6638 | ±1.3277 | **+3.715** | **2.03e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0014** | 0.6556 | ±1.3112 | **-7.629** | **2.37e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.291** | **0.0220** | * |
| BMI (kg/m2) | -0.0545 | 0.0340 | ±0.0681 | -1.601 | 0.1093 |  |
| Hypertension | +0.1102 | 0.5189 | ±1.0379 | +0.212 | 0.8319 |  |
| High cholesterol | -0.9291 | 0.4816 | ±0.9632 | -1.929 | 0.0537 | . |
| Kidney disease | -0.4859 | 0.8778 | ±1.7557 | -0.554 | 0.5799 |  |
| Circulatory disease | -0.8070 | 0.7064 | ±1.4128 | -1.142 | 0.2533 |  |
| Time < 70 (%) | +0.1591 | 0.4473 | ±0.8946 | +0.356 | 0.7220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.2904**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.47e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.8**, BIC = **4341.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1654** | 1.7044 | ±3.4088 | **+29.433** | **2.09e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3313** | 0.4761 | ±0.9522 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.1989 | 0.9085 | ±1.8170 | +0.219 | 0.8267 |  |
| **Site: UCSD (vs UAB)** | **+3.1184** | 0.6108 | ±1.2217 | **+5.105** | **3.31e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8987** | 0.5744 | ±1.1488 | **-3.306** | **9.48e-04** | *** |
| Season: spring (vs autumn) | -0.9294 | 0.6415 | ±1.2830 | -1.449 | 0.1474 |  |
| **Season: summer (vs autumn)** | **+2.4703** | 0.6642 | ±1.3284 | **+3.719** | **2.00e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9982** | 0.6558 | ±1.3116 | **-7.622** | **2.51e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.294** | **0.0218** | * |
| BMI (kg/m2) | -0.0546 | 0.0340 | ±0.0681 | -1.603 | 0.1089 |  |
| Hypertension | +0.1115 | 0.5190 | ±1.0381 | +0.215 | 0.8299 |  |
| High cholesterol | -0.9275 | 0.4815 | ±0.9631 | -1.926 | 0.0541 | . |
| Kidney disease | -0.4890 | 0.8782 | ±1.7563 | -0.557 | 0.5776 |  |
| Circulatory disease | -0.8081 | 0.7074 | ±1.4147 | -1.142 | 0.2533 |  |
| Avg. daily time < 70 (%) | +0.1059 | 0.4315 | ±0.8631 | +0.245 | 0.8061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.2914**, Adj R² = **0.2763**, F-statistic = **19.35** (p = **6.31e-41**), Residual SE = **5.697** on **659** df, AIC = **4272.9**, BIC = **4340.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1853** | 1.7029 | ±3.4058 | **+29.471** | **6.81e-191** | *** |
| **Education: graduate level (vs college)** | **+1.3038** | 0.4762 | ±0.9523 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1715 | 0.9082 | ±1.8164 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1662** | 0.6143 | ±1.2285 | **+5.154** | **2.54e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9235** | 0.5729 | ±1.1457 | **-3.358** | **7.86e-04** | *** |
| Season: spring (vs autumn) | -0.9111 | 0.6435 | ±1.2870 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4864** | 0.6668 | ±1.3335 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9654** | 0.6556 | ±1.3111 | **-7.574** | **3.61e-14** | *** |
| **Age (years)** | **-0.0489** | 0.0207 | ±0.0415 | **-2.355** | **0.0185** | * |
| BMI (kg/m2) | -0.0564 | 0.0342 | ±0.0685 | -1.648 | 0.0994 | . |
| Hypertension | +0.1072 | 0.5183 | ±1.0366 | +0.207 | 0.8362 |  |
| **High cholesterol** | **-0.9503** | 0.4812 | ±0.9624 | **-1.975** | **0.0483** | * |
| Kidney disease | -0.5240 | 0.8746 | ±1.7492 | -0.599 | 0.5491 |  |
| Circulatory disease | -0.8506 | 0.7069 | ±1.4137 | -1.203 | 0.2289 |  |
| Time 181-250, pooled (%) | +0.0789 | 0.0767 | ±0.1533 | +1.030 | 0.3032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.2916**, Adj R² = **0.2765**, F-statistic = **19.37** (p = **5.70e-41**), Residual SE = **5.696** on **659** df, AIC = **4272.7**, BIC = **4340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1886** | 1.7055 | ±3.4109 | **+29.428** | **2.39e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3006** | 0.4761 | ±0.9522 | **+2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | +0.1716 | 0.9086 | ±1.8173 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1740** | 0.6148 | ±1.2296 | **+5.163** | **2.43e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9218** | 0.5727 | ±1.1454 | **-3.356** | **7.92e-04** | *** |
| Season: spring (vs autumn) | -0.9108 | 0.6432 | ±1.2864 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4861** | 0.6666 | ±1.3332 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9586** | 0.6559 | ±1.3117 | **-7.561** | **4.01e-14** | *** |
| **Age (years)** | **-0.0488** | 0.0207 | ±0.0414 | **-2.356** | **0.0185** | * |
| BMI (kg/m2) | -0.0570 | 0.0343 | ±0.0686 | -1.662 | 0.0966 | . |
| Hypertension | +0.1091 | 0.5183 | ±1.0366 | +0.211 | 0.8332 |  |
| **High cholesterol** | **-0.9538** | 0.4813 | ±0.9626 | **-1.982** | **0.0475** | * |
| Kidney disease | -0.5307 | 0.8734 | ±1.7468 | -0.608 | 0.5434 |  |
| Circulatory disease | -0.8613 | 0.7073 | ±1.4147 | -1.218 | 0.2233 |  |
| Avg. daily time 181-250 (%) | +0.0897 | 0.0785 | ±0.1571 | +1.142 | 0.2535 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.2914**, Adj R² = **0.2763**, F-statistic = **19.35** (p = **6.31e-41**), Residual SE = **5.697** on **659** df, AIC = **4272.9**, BIC = **4340.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1853** | 1.7029 | ±3.4058 | **+29.471** | **6.81e-191** | *** |
| **Education: graduate level (vs college)** | **+1.3038** | 0.4762 | ±0.9523 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1715 | 0.9082 | ±1.8164 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1662** | 0.6143 | ±1.2285 | **+5.154** | **2.54e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9235** | 0.5729 | ±1.1457 | **-3.358** | **7.86e-04** | *** |
| Season: spring (vs autumn) | -0.9111 | 0.6435 | ±1.2870 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4864** | 0.6668 | ±1.3335 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9654** | 0.6556 | ±1.3111 | **-7.574** | **3.61e-14** | *** |
| **Age (years)** | **-0.0489** | 0.0207 | ±0.0415 | **-2.355** | **0.0185** | * |
| BMI (kg/m2) | -0.0564 | 0.0342 | ±0.0685 | -1.648 | 0.0994 | . |
| Hypertension | +0.1072 | 0.5183 | ±1.0366 | +0.207 | 0.8362 |  |
| **High cholesterol** | **-0.9503** | 0.4812 | ±0.9624 | **-1.975** | **0.0483** | * |
| Kidney disease | -0.5240 | 0.8746 | ±1.7492 | -0.599 | 0.5491 |  |
| Circulatory disease | -0.8506 | 0.7069 | ±1.4137 | -1.203 | 0.2289 |  |
| Time > 180 (%) | +0.0789 | 0.0767 | ±0.1533 | +1.030 | 0.3032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.2916**, Adj R² = **0.2765**, F-statistic = **19.37** (p = **5.70e-41**), Residual SE = **5.696** on **659** df, AIC = **4272.7**, BIC = **4340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1886** | 1.7055 | ±3.4109 | **+29.428** | **2.39e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3006** | 0.4761 | ±0.9522 | **+2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | +0.1716 | 0.9086 | ±1.8173 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1740** | 0.6148 | ±1.2296 | **+5.163** | **2.43e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9218** | 0.5727 | ±1.1454 | **-3.356** | **7.92e-04** | *** |
| Season: spring (vs autumn) | -0.9108 | 0.6432 | ±1.2864 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4861** | 0.6666 | ±1.3332 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9586** | 0.6559 | ±1.3117 | **-7.561** | **4.01e-14** | *** |
| **Age (years)** | **-0.0488** | 0.0207 | ±0.0414 | **-2.356** | **0.0185** | * |
| BMI (kg/m2) | -0.0570 | 0.0343 | ±0.0686 | -1.662 | 0.0966 | . |
| Hypertension | +0.1091 | 0.5183 | ±1.0366 | +0.211 | 0.8332 |  |
| **High cholesterol** | **-0.9538** | 0.4813 | ±0.9626 | **-1.982** | **0.0475** | * |
| Kidney disease | -0.5307 | 0.8734 | ±1.7468 | -0.608 | 0.5434 |  |
| Circulatory disease | -0.8613 | 0.7073 | ±1.4147 | -1.218 | 0.2233 |  |
| Avg. daily time > 180 (%) | +0.0897 | 0.0785 | ±0.1571 | +1.142 | 0.2535 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.2918**, Adj R² = **0.2767**, F-statistic = **19.39** (p = **5.28e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2288** | 1.7014 | ±3.4028 | **+29.522** | **1.52e-191** | *** |
| **Education: graduate level (vs college)** | **+1.3238** | 0.4746 | ±0.9493 | **+2.789** | **0.0053** | ** |
| Education: high school or below (vs college) | +0.1529 | 0.9096 | ±1.8191 | +0.168 | 0.8665 |  |
| **Site: UCSD (vs UAB)** | **+3.1496** | 0.6117 | ±1.2235 | **+5.148** | **2.63e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9206** | 0.5735 | ±1.1470 | **-3.349** | **8.11e-04** | *** |
| Season: spring (vs autumn) | -0.9239 | 0.6416 | ±1.2831 | -1.440 | 0.1498 |  |
| **Season: summer (vs autumn)** | **+2.4754** | 0.6652 | ±1.3304 | **+3.721** | **1.98e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9936** | 0.6538 | ±1.3075 | **-7.638** | **2.20e-14** | *** |
| **Age (years)** | **-0.0469** | 0.0208 | ±0.0415 | **-2.259** | **0.0239** | * |
| BMI (kg/m2) | -0.0596 | 0.0344 | ±0.0687 | -1.735 | 0.0828 | . |
| Hypertension | +0.1275 | 0.5197 | ±1.0394 | +0.245 | 0.8062 |  |
| **High cholesterol** | **-0.9788** | 0.4831 | ±0.9662 | **-2.026** | **0.0428** | * |
| Kidney disease | -0.4874 | 0.8802 | ±1.7604 | -0.554 | 0.5797 |  |
| Circulatory disease | -0.8162 | 0.7074 | ±1.4149 | -1.154 | 0.2486 |  |
| Nocturnal time > 180 (%) | +0.0822 | 0.0517 | ±0.1035 | +1.588 | 0.1122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.0365**, Adj R² = **0.0175**, F-statistic = **1.92** (p = **0.0249**), Residual SE = **15.454** on **660** df, AIC = **5617.3**, BIC = **5680.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2048** | 5.0857 | ±10.1714 | **+24.816** | **6.07e-136** | *** |
| Education: graduate level (vs college) | -2.0995 | 1.2822 | ±2.5645 | -1.637 | 0.1016 |  |
| Education: high school or below (vs college) | +3.6796 | 2.4478 | ±4.8956 | +1.503 | 0.1328 |  |
| Site: UCSD (vs UAB) | +0.7597 | 1.6229 | ±3.2458 | +0.468 | 0.6397 |  |
| Site: UW (vs UAB) | +0.0850 | 1.5766 | ±3.1532 | +0.054 | 0.9570 |  |
| Season: spring (vs autumn) | +3.0633 | 1.7026 | ±3.4052 | +1.799 | 0.0720 | . |
| Season: summer (vs autumn) | +2.4448 | 1.8092 | ±3.6185 | +1.351 | 0.1766 |  |
| **Season: winter (vs autumn)** | **+4.0573** | 1.7581 | ±3.5163 | **+2.308** | **0.0210** | * |
| Age (years) | -0.1135 | 0.0617 | ±0.1234 | -1.840 | 0.0657 | . |
| BMI (kg/m2) | +0.1643 | 0.0840 | ±0.1679 | +1.957 | 0.0504 | . |
| Hypertension | +0.7416 | 1.4143 | ±2.8285 | +0.524 | 0.6000 |  |
| High cholesterol | -0.1060 | 1.2796 | ±2.5591 | -0.083 | 0.9340 |  |
| Kidney disease | -1.0472 | 2.0363 | ±4.0726 | -0.514 | 0.6071 |  |
| Circulatory disease | +1.0222 | 2.0455 | ±4.0909 | +0.500 | 0.6172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.0372**, Adj R² = **0.0168**, F-statistic = **1.82** (p = **0.0323**), Residual SE = **15.460** on **659** df, AIC = **5618.7**, BIC = **5686.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.1489** | 11.7826 | ±23.5652 | **+11.300** | **1.31e-29** | *** |
| Education: graduate level (vs college) | -2.0831 | 1.2822 | ±2.5644 | -1.625 | 0.1042 |  |
| Education: high school or below (vs college) | +3.7033 | 2.4434 | ±4.8867 | +1.516 | 0.1296 |  |
| Site: UCSD (vs UAB) | +0.7616 | 1.6250 | ±3.2501 | +0.469 | 0.6393 |  |
| Site: UW (vs UAB) | +0.1100 | 1.5838 | ±3.1676 | +0.069 | 0.9446 |  |
| Season: spring (vs autumn) | +2.8686 | 1.7478 | ±3.4955 | +1.641 | 0.1007 |  |
| Season: summer (vs autumn) | +2.4126 | 1.8262 | ±3.6524 | +1.321 | 0.1865 |  |
| **Season: winter (vs autumn)** | **+3.9447** | 1.7824 | ±3.5649 | **+2.213** | **0.0269** | * |
| Age (years) | -0.1083 | 0.0623 | ±0.1247 | -1.738 | 0.0822 | . |
| **BMI (kg/m2)** | **+0.1733** | 0.0844 | ±0.1688 | **+2.054** | **0.0400** | * |
| Hypertension | +0.8156 | 1.4244 | ±2.8488 | +0.573 | 0.5669 |  |
| High cholesterol | -0.0047 | 1.3166 | ±2.6332 | -0.004 | 0.9972 |  |
| Kidney disease | -1.0296 | 2.0484 | ±4.0967 | -0.503 | 0.6152 |  |
| Circulatory disease | +0.9588 | 2.0694 | ±4.1388 | +0.463 | 0.6431 |  |
| HbA1c (%) | -1.3437 | 2.0567 | ±4.1135 | -0.653 | 0.5136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.0443**, Adj R² = **0.0240**, F-statistic = **2.18** (p = **0.0074**), Residual SE = **15.404** on **659** df, AIC = **5613.8**, BIC = **5681.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+139.9520** | 7.8225 | ±15.6450 | **+17.891** | **1.39e-71** | *** |
| Education: graduate level (vs college) | -1.9004 | 1.2841 | ±2.5683 | -1.480 | 0.1389 |  |
| Education: high school or below (vs college) | +3.8865 | 2.4469 | ±4.8938 | +1.588 | 0.1122 |  |
| Site: UCSD (vs UAB) | +0.5684 | 1.6178 | ±3.2357 | +0.351 | 0.7253 |  |
| Site: UW (vs UAB) | +0.3090 | 1.5727 | ±3.1453 | +0.196 | 0.8443 |  |
| Season: spring (vs autumn) | +2.9927 | 1.6927 | ±3.3854 | +1.768 | 0.0771 | . |
| Season: summer (vs autumn) | +2.4769 | 1.8139 | ±3.6278 | +1.366 | 0.1721 |  |
| **Season: winter (vs autumn)** | **+3.9177** | 1.7543 | ±3.5087 | **+2.233** | **0.0255** | * |
| Age (years) | -0.1074 | 0.0619 | ±0.1237 | -1.737 | 0.0824 | . |
| **BMI (kg/m2)** | **+0.1884** | 0.0831 | ±0.1662 | **+2.266** | **0.0234** | * |
| Hypertension | +0.9438 | 1.4098 | ±2.8197 | +0.669 | 0.5032 |  |
| High cholesterol | -0.1070 | 1.2796 | ±2.5593 | -0.084 | 0.9334 |  |
| Kidney disease | -0.7899 | 2.0680 | ±4.1359 | -0.382 | 0.7025 |  |
| Circulatory disease | +1.2740 | 2.0515 | ±4.1031 | +0.621 | 0.5346 |  |
| **Mean glucose (mg/dL)** | **-0.1258** | 0.0559 | ±0.1119 | **-2.250** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.0443**, Adj R² = **0.0240**, F-statistic = **2.18** (p = **0.0074**), Residual SE = **15.404** on **659** df, AIC = **5613.8**, BIC = **5681.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+157.3660** | 14.6173 | ±29.2347 | **+10.766** | **5.00e-27** | *** |
| Education: graduate level (vs college) | -1.9004 | 1.2841 | ±2.5683 | -1.480 | 0.1389 |  |
| Education: high school or below (vs college) | +3.8865 | 2.4469 | ±4.8938 | +1.588 | 0.1122 |  |
| Site: UCSD (vs UAB) | +0.5684 | 1.6178 | ±3.2357 | +0.351 | 0.7253 |  |
| Site: UW (vs UAB) | +0.3090 | 1.5727 | ±3.1453 | +0.196 | 0.8443 |  |
| Season: spring (vs autumn) | +2.9927 | 1.6927 | ±3.3854 | +1.768 | 0.0771 | . |
| Season: summer (vs autumn) | +2.4769 | 1.8139 | ±3.6278 | +1.366 | 0.1721 |  |
| **Season: winter (vs autumn)** | **+3.9177** | 1.7543 | ±3.5087 | **+2.233** | **0.0255** | * |
| Age (years) | -0.1074 | 0.0619 | ±0.1237 | -1.737 | 0.0824 | . |
| **BMI (kg/m2)** | **+0.1884** | 0.0831 | ±0.1662 | **+2.266** | **0.0234** | * |
| Hypertension | +0.9438 | 1.4098 | ±2.8197 | +0.669 | 0.5032 |  |
| High cholesterol | -0.1070 | 1.2796 | ±2.5593 | -0.084 | 0.9334 |  |
| Kidney disease | -0.7899 | 2.0680 | ±4.1359 | -0.382 | 0.7025 |  |
| Circulatory disease | +1.2740 | 2.0515 | ±4.1031 | +0.621 | 0.5346 |  |
| **GMI (%)** | **-5.2610** | 2.3384 | ±4.6768 | **-2.250** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.0410**, Adj R² = **0.0206**, F-statistic = **2.01** (p = **0.0149**), Residual SE = **15.430** on **659** df, AIC = **5616.1**, BIC = **5683.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.2821** | 7.1072 | ±14.2144 | **+19.035** | **8.83e-81** | *** |
| Education: graduate level (vs college) | -2.0102 | 1.2821 | ±2.5641 | -1.568 | 0.1169 |  |
| Education: high school or below (vs college) | +3.8025 | 2.4532 | ±4.9064 | +1.550 | 0.1211 |  |
| Site: UCSD (vs UAB) | +0.7374 | 1.6203 | ±3.2406 | +0.455 | 0.6490 |  |
| Site: UW (vs UAB) | +0.2551 | 1.5707 | ±3.1413 | +0.162 | 0.8710 |  |
| Season: spring (vs autumn) | +3.1160 | 1.7039 | ±3.4078 | +1.829 | 0.0674 | . |
| Season: summer (vs autumn) | +2.5316 | 1.8177 | ±3.6355 | +1.393 | 0.1637 |  |
| **Season: winter (vs autumn)** | **+4.0717** | 1.7621 | ±3.5241 | **+2.311** | **0.0208** | * |
| Age (years) | -0.1175 | 0.0618 | ±0.1236 | -1.902 | 0.0572 | . |
| **BMI (kg/m2)** | **+0.2007** | 0.0823 | ±0.1645 | **+2.440** | **0.0147** | * |
| Hypertension | +0.8313 | 1.4151 | ±2.8302 | +0.587 | 0.5569 |  |
| High cholesterol | -0.0286 | 1.2831 | ±2.5662 | -0.022 | 0.9822 |  |
| Kidney disease | -0.9605 | 2.0766 | ±4.1532 | -0.463 | 0.6437 |  |
| Circulatory disease | +1.1604 | 2.0523 | ±4.1045 | +0.565 | 0.5718 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0850 | 0.0465 | ±0.0930 | -1.828 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.0455**, Adj R² = **0.0253**, F-statistic = **2.25** (p = **0.0056**), Residual SE = **15.393** on **659** df, AIC = **5612.9**, BIC = **5680.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.7448** | 5.7141 | ±11.4282 | **+23.231** | **2.21e-119** | *** |
| Education: graduate level (vs college) | -2.2238 | 1.2767 | ±2.5534 | -1.742 | 0.0815 | . |
| Education: high school or below (vs college) | +3.8061 | 2.4556 | ±4.9112 | +1.550 | 0.1211 |  |
| Site: UCSD (vs UAB) | +0.4951 | 1.6141 | ±3.2283 | +0.307 | 0.7591 |  |
| Site: UW (vs UAB) | +0.2745 | 1.5530 | ±3.1059 | +0.177 | 0.8597 |  |
| Season: spring (vs autumn) | +3.0740 | 1.6948 | ±3.3895 | +1.814 | 0.0697 | . |
| Season: summer (vs autumn) | +2.4905 | 1.8171 | ±3.6341 | +1.371 | 0.1705 |  |
| **Season: winter (vs autumn)** | **+4.1465** | 1.7534 | ±3.5067 | **+2.365** | **0.0180** | * |
| Age (years) | -0.0999 | 0.0625 | ±0.1251 | -1.598 | 0.1101 |  |
| **BMI (kg/m2)** | **+0.1750** | 0.0820 | ±0.1641 | **+2.133** | **0.0329** | * |
| Hypertension | +0.9354 | 1.4165 | ±2.8331 | +0.660 | 0.5090 |  |
| High cholesterol | -0.0517 | 1.2767 | ±2.5533 | -0.041 | 0.9677 |  |
| Kidney disease | -0.8621 | 2.0233 | ±4.0467 | -0.426 | 0.6700 |  |
| Circulatory disease | +0.9933 | 2.0521 | ±4.1043 | +0.484 | 0.6284 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.4033** | 0.1672 | ±0.3343 | **-2.413** | **0.0158** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.0459**, Adj R² = **0.0256**, F-statistic = **2.26** (p = **0.0052**), Residual SE = **15.391** on **659** df, AIC = **5612.7**, BIC = **5680.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.2926** | 5.5046 | ±11.0092 | **+24.033** | **1.26e-127** | *** |
| Education: graduate level (vs college) | -2.1683 | 1.2752 | ±2.5505 | -1.700 | 0.0891 | . |
| Education: high school or below (vs college) | +3.8244 | 2.4528 | ±4.9055 | +1.559 | 0.1189 |  |
| Site: UCSD (vs UAB) | +0.4506 | 1.6124 | ±3.2248 | +0.279 | 0.7799 |  |
| Site: UW (vs UAB) | +0.2676 | 1.5525 | ±3.1050 | +0.172 | 0.8632 |  |
| Season: spring (vs autumn) | +3.0167 | 1.6943 | ±3.3887 | +1.780 | 0.0750 | . |
| Season: summer (vs autumn) | +2.4161 | 1.8190 | ±3.6380 | +1.328 | 0.1841 |  |
| **Season: winter (vs autumn)** | **+4.0207** | 1.7498 | ±3.4995 | **+2.298** | **0.0216** | * |
| Age (years) | -0.0999 | 0.0628 | ±0.1255 | -1.592 | 0.1113 |  |
| **BMI (kg/m2)** | **+0.1784** | 0.0818 | ±0.1637 | **+2.180** | **0.0292** | * |
| Hypertension | +0.9121 | 1.4145 | ±2.8289 | +0.645 | 0.5190 |  |
| High cholesterol | -0.0721 | 1.2763 | ±2.5526 | -0.057 | 0.9549 |  |
| Kidney disease | -0.7931 | 2.0161 | ±4.0321 | -0.393 | 0.6940 |  |
| Circulatory disease | +1.0037 | 2.0444 | ±4.0889 | +0.491 | 0.6235 |  |
| **Avg. daily SD (mg/dL)** | **-0.4158** | 0.1682 | ±0.3364 | **-2.472** | **0.0134** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.0397**, Adj R² = **0.0193**, F-statistic = **1.95** (p = **0.0197**), Residual SE = **15.441** on **659** df, AIC = **5617.0**, BIC = **5684.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.0877** | 6.0705 | ±12.1410 | **+21.594** | **2.04e-103** | *** |
| Education: graduate level (vs college) | -2.2607 | 1.2853 | ±2.5705 | -1.759 | 0.0786 | . |
| Education: high school or below (vs college) | +3.6793 | 2.4567 | ±4.9135 | +1.498 | 0.1342 |  |
| Site: UCSD (vs UAB) | +0.6430 | 1.6215 | ±3.2430 | +0.397 | 0.6917 |  |
| Site: UW (vs UAB) | +0.1328 | 1.5679 | ±3.1358 | +0.085 | 0.9325 |  |
| Season: spring (vs autumn) | +3.0978 | 1.7021 | ±3.4042 | +1.820 | 0.0688 | . |
| Season: summer (vs autumn) | +2.4778 | 1.8147 | ±3.6293 | +1.365 | 0.1721 |  |
| **Season: winter (vs autumn)** | **+4.1858** | 1.7616 | ±3.5232 | **+2.376** | **0.0175** | * |
| Age (years) | -0.1067 | 0.0624 | ±0.1247 | -1.711 | 0.0872 | . |
| BMI (kg/m2) | +0.1627 | 0.0835 | ±0.1669 | +1.949 | 0.0513 | . |
| Hypertension | +0.8124 | 1.4183 | ±2.8367 | +0.573 | 0.5668 |  |
| High cholesterol | -0.0836 | 1.2790 | ±2.5579 | -0.065 | 0.9479 |  |
| Kidney disease | -1.0038 | 2.0187 | ±4.0374 | -0.497 | 0.6190 |  |
| Circulatory disease | +0.9186 | 2.0503 | ±4.1005 | +0.448 | 0.6541 |  |
| CV (%) | -0.3249 | 0.2242 | ±0.4484 | -1.449 | 0.1473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.0408**, Adj R² = **0.0204**, F-statistic = **2.00** (p = **0.0156**), Residual SE = **15.432** on **659** df, AIC = **5616.3**, BIC = **5684.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.9430** | 6.3260 | ±12.6519 | **+18.960** | **3.62e-80** | *** |
| Education: graduate level (vs college) | -2.2942 | 1.2827 | ±2.5655 | -1.789 | 0.0737 | . |
| Education: high school or below (vs college) | +3.7095 | 2.4566 | ±4.9133 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.6589 | 1.6171 | ±3.2342 | +0.407 | 0.6837 |  |
| Site: UW (vs UAB) | +0.1663 | 1.5644 | ±3.1288 | +0.106 | 0.9154 |  |
| Season: spring (vs autumn) | +3.1545 | 1.7055 | ±3.4109 | +1.850 | 0.0644 | . |
| Season: summer (vs autumn) | +2.4635 | 1.8126 | ±3.6251 | +1.359 | 0.1741 |  |
| **Season: winter (vs autumn)** | **+4.2136** | 1.7609 | ±3.5218 | **+2.393** | **0.0167** | * |
| Age (years) | -0.1067 | 0.0623 | ±0.1245 | -1.713 | 0.0868 | . |
| BMI (kg/m2) | +0.1626 | 0.0834 | ±0.1668 | +1.950 | 0.0512 | . |
| Hypertension | +0.8312 | 1.4185 | ±2.8370 | +0.586 | 0.5579 |  |
| High cholesterol | -0.0976 | 1.2771 | ±2.5543 | -0.076 | 0.9391 |  |
| Kidney disease | -0.9950 | 2.0219 | ±4.0438 | -0.492 | 0.6226 |  |
| Circulatory disease | +0.9019 | 2.0477 | ±4.0953 | +0.440 | 0.6596 |  |
| Mean / SD ratio | +0.9203 | 0.5527 | ±1.1054 | +1.665 | 0.0959 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.0407**, Adj R² = **0.0203**, F-statistic = **1.99** (p = **0.0161**), Residual SE = **15.433** on **659** df, AIC = **5616.3**, BIC = **5684.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120.3793** | 6.3438 | ±12.6877 | **+18.976** | **2.70e-80** | *** |
| Education: graduate level (vs college) | -2.2508 | 1.2790 | ±2.5581 | -1.760 | 0.0785 | . |
| Education: high school or below (vs college) | +3.7185 | 2.4520 | ±4.9041 | +1.517 | 0.1294 |  |
| Site: UCSD (vs UAB) | +0.6399 | 1.6161 | ±3.2323 | +0.396 | 0.6921 |  |
| Site: UW (vs UAB) | +0.1791 | 1.5654 | ±3.1309 | +0.114 | 0.9089 |  |
| Season: spring (vs autumn) | +3.1130 | 1.7057 | ±3.4114 | +1.825 | 0.0680 | . |
| Season: summer (vs autumn) | +2.4113 | 1.8148 | ±3.6295 | +1.329 | 0.1839 |  |
| **Season: winter (vs autumn)** | **+4.1214** | 1.7587 | ±3.5174 | **+2.343** | **0.0191** | * |
| Age (years) | -0.1060 | 0.0625 | ±0.1250 | -1.696 | 0.0899 | . |
| **BMI (kg/m2)** | **+0.1680** | 0.0830 | ±0.1660 | **+2.024** | **0.0429** | * |
| Hypertension | +0.7781 | 1.4168 | ±2.8337 | +0.549 | 0.5829 |  |
| High cholesterol | -0.1235 | 1.2766 | ±2.5532 | -0.097 | 0.9229 |  |
| Kidney disease | -0.9574 | 2.0209 | ±4.0419 | -0.474 | 0.6357 |  |
| Circulatory disease | +0.9010 | 2.0464 | ±4.0929 | +0.440 | 0.6597 |  |
| Avg. daily mean/SD | +0.7318 | 0.4515 | ±0.9030 | +1.621 | 0.1051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.0365**, Adj R² = **0.0161**, F-statistic = **1.78** (p = **0.0372**), Residual SE = **15.466** on **659** df, AIC = **5619.2**, BIC = **5686.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7981** | 6.0627 | ±12.1254 | **+20.750** | **1.24e-95** | *** |
| Education: graduate level (vs college) | -2.0998 | 1.2840 | ±2.5680 | -1.635 | 0.1020 |  |
| Education: high school or below (vs college) | +3.6608 | 2.4659 | ±4.9317 | +1.485 | 0.1377 |  |
| Site: UCSD (vs UAB) | +0.7667 | 1.6261 | ±3.2521 | +0.471 | 0.6373 |  |
| Site: UW (vs UAB) | +0.0879 | 1.5792 | ±3.1585 | +0.056 | 0.9556 |  |
| Season: spring (vs autumn) | +3.0608 | 1.7058 | ±3.4115 | +1.794 | 0.0728 | . |
| Season: summer (vs autumn) | +2.4518 | 1.8146 | ±3.6293 | +1.351 | 0.1767 |  |
| **Season: winter (vs autumn)** | **+4.0604** | 1.7621 | ±3.5241 | **+2.304** | **0.0212** | * |
| Age (years) | -0.1134 | 0.0618 | ±0.1235 | -1.836 | 0.0664 | . |
| BMI (kg/m2) | +0.1644 | 0.0841 | ±0.1682 | +1.955 | 0.0506 | . |
| Hypertension | +0.7483 | 1.4222 | ±2.8444 | +0.526 | 0.5988 |  |
| High cholesterol | -0.1042 | 1.2814 | ±2.5628 | -0.081 | 0.9352 |  |
| Kidney disease | -1.0585 | 2.0485 | ±4.0969 | -0.517 | 0.6053 |  |
| Circulatory disease | +1.0261 | 2.0495 | ±4.0990 | +0.501 | 0.6166 |  |
| MAG (mg/dL/h) | +0.0109 | 0.0888 | ±0.1777 | +0.122 | 0.9028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.96** (p = **0.0187**), Residual SE = **15.438** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.0228** | 5.8374 | ±11.6748 | **+22.445** | **1.42e-111** | *** |
| Education: graduate level (vs college) | -2.0756 | 1.2802 | ±2.5605 | -1.621 | 0.1050 |  |
| Education: high school or below (vs college) | +3.8266 | 2.4591 | ±4.9182 | +1.556 | 0.1197 |  |
| Site: UCSD (vs UAB) | +0.6377 | 1.6215 | ±3.2430 | +0.393 | 0.6941 |  |
| Site: UW (vs UAB) | +0.1878 | 1.5624 | ±3.1248 | +0.120 | 0.9043 |  |
| Season: spring (vs autumn) | +3.0854 | 1.7053 | ±3.4106 | +1.809 | 0.0704 | . |
| Season: summer (vs autumn) | +2.3899 | 1.8184 | ±3.6368 | +1.314 | 0.1887 |  |
| **Season: winter (vs autumn)** | **+4.0421** | 1.7593 | ±3.5185 | **+2.298** | **0.0216** | * |
| Age (years) | -0.1072 | 0.0625 | ±0.1250 | -1.714 | 0.0865 | . |
| BMI (kg/m2) | +0.1592 | 0.0838 | ±0.1677 | +1.899 | 0.0575 | . |
| Hypertension | +0.7808 | 1.4168 | ±2.8335 | +0.551 | 0.5815 |  |
| High cholesterol | -0.1240 | 1.2794 | ±2.5588 | -0.097 | 0.9228 |  |
| Kidney disease | -0.8815 | 2.0289 | ±4.0577 | -0.434 | 0.6639 |  |
| Circulatory disease | +1.0672 | 2.0485 | ±4.0971 | +0.521 | 0.6024 |  |
| Avg. daily range (mg/dL) | -0.0573 | 0.0374 | ±0.0748 | -1.531 | 0.1258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.0373**, Adj R² = **0.0169**, F-statistic = **1.82** (p = **0.0319**), Residual SE = **15.460** on **659** df, AIC = **5618.7**, BIC = **5686.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0716** | 5.2882 | ±10.5763 | **+24.029** | **1.37e-127** | *** |
| Education: graduate level (vs college) | -2.1091 | 1.2840 | ±2.5681 | -1.643 | 0.1005 |  |
| Education: high school or below (vs college) | +3.7008 | 2.4510 | ±4.9020 | +1.510 | 0.1311 |  |
| Site: UCSD (vs UAB) | +0.7418 | 1.6246 | ±3.2492 | +0.457 | 0.6479 |  |
| Site: UW (vs UAB) | +0.1131 | 1.5784 | ±3.1568 | +0.072 | 0.9429 |  |
| Season: spring (vs autumn) | +3.1381 | 1.7192 | ±3.4383 | +1.825 | 0.0679 | . |
| Season: summer (vs autumn) | +2.5670 | 1.8163 | ±3.6326 | +1.413 | 0.1576 |  |
| **Season: winter (vs autumn)** | **+4.1444** | 1.7637 | ±3.5274 | **+2.350** | **0.0188** | * |
| Age (years) | -0.1135 | 0.0617 | ±0.1234 | -1.839 | 0.0659 | . |
| **BMI (kg/m2)** | **+0.1711** | 0.0835 | ±0.1669 | **+2.050** | **0.0404** | * |
| Hypertension | +0.7343 | 1.4153 | ±2.8306 | +0.519 | 0.6039 |  |
| High cholesterol | -0.0425 | 1.2805 | ±2.5609 | -0.033 | 0.9735 |  |
| Kidney disease | -1.1201 | 2.0434 | ±4.0868 | -0.548 | 0.5836 |  |
| Circulatory disease | +1.0493 | 2.0504 | ±4.1008 | +0.512 | 0.6088 |  |
| SD of daily means (mg/dL) | -0.1995 | 0.2907 | ±0.5814 | -0.686 | 0.4925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.0395**, Adj R² = **0.0191**, F-statistic = **1.94** (p = **0.0204**), Residual SE = **15.442** on **659** df, AIC = **5617.2**, BIC = **5684.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+94.0809** | 24.8602 | ±49.7204 | **+3.784** | **1.54e-04** | *** |
| Education: graduate level (vs college) | -2.0791 | 1.2837 | ±2.5673 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +3.6773 | 2.4687 | ±4.9374 | +1.490 | 0.1363 |  |
| Site: UCSD (vs UAB) | +0.6087 | 1.6251 | ±3.2502 | +0.375 | 0.7080 |  |
| Site: UW (vs UAB) | +0.1647 | 1.5845 | ±3.1689 | +0.104 | 0.9172 |  |
| Season: spring (vs autumn) | +2.9979 | 1.6956 | ±3.3911 | +1.768 | 0.0770 | . |
| Season: summer (vs autumn) | +2.4151 | 1.8223 | ±3.6446 | +1.325 | 0.1851 |  |
| **Season: winter (vs autumn)** | **+3.9898** | 1.7567 | ±3.5133 | **+2.271** | **0.0231** | * |
| Age (years) | -0.1089 | 0.0623 | ±0.1246 | -1.748 | 0.0805 | . |
| **BMI (kg/m2)** | **+0.1703** | 0.0840 | ±0.1680 | **+2.028** | **0.0426** | * |
| Hypertension | +0.7716 | 1.4141 | ±2.8282 | +0.546 | 0.5853 |  |
| High cholesterol | +0.0041 | 1.2895 | ±2.5790 | +0.003 | 0.9975 |  |
| Kidney disease | -0.9315 | 2.0317 | ±4.0634 | -0.458 | 0.6466 |  |
| Circulatory disease | +1.1397 | 2.0503 | ±4.1007 | +0.556 | 0.5783 |  |
| Time in range 70-180, pooled (%) | +0.3227 | 0.2379 | ±0.4757 | +1.357 | 0.1749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.96** (p = **0.0188**), Residual SE = **15.439** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+91.1455** | 25.3227 | ±50.6454 | **+3.599** | **3.19e-04** | *** |
| Education: graduate level (vs college) | -2.0752 | 1.2839 | ±2.5677 | -1.616 | 0.1060 |  |
| Education: high school or below (vs college) | +3.6671 | 2.4652 | ±4.9305 | +1.488 | 0.1369 |  |
| Site: UCSD (vs UAB) | +0.5940 | 1.6245 | ±3.2489 | +0.366 | 0.7146 |  |
| Site: UW (vs UAB) | +0.1553 | 1.5837 | ±3.1675 | +0.098 | 0.9219 |  |
| Season: spring (vs autumn) | +2.9947 | 1.6958 | ±3.3917 | +1.766 | 0.0774 | . |
| Season: summer (vs autumn) | +2.4160 | 1.8227 | ±3.6454 | +1.326 | 0.1850 |  |
| **Season: winter (vs autumn)** | **+3.9733** | 1.7561 | ±3.5123 | **+2.263** | **0.0237** | * |
| Age (years) | -0.1092 | 0.0622 | ±0.1244 | -1.756 | 0.0791 | . |
| **BMI (kg/m2)** | **+0.1724** | 0.0839 | ±0.1679 | **+2.054** | **0.0400** | * |
| Hypertension | +0.7623 | 1.4142 | ±2.8284 | +0.539 | 0.5898 |  |
| High cholesterol | +0.0136 | 1.2888 | ±2.5776 | +0.011 | 0.9916 |  |
| Kidney disease | -0.9082 | 2.0298 | ±4.0597 | -0.447 | 0.6546 |  |
| Circulatory disease | +1.1673 | 2.0479 | ±4.0958 | +0.570 | 0.5687 |  |
| Avg. daily time in range 70-180 (%) | +0.3519 | 0.2420 | ±0.4839 | +1.454 | 0.1458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.0368**, Adj R² = **0.0164**, F-statistic = **1.80** (p = **0.0352**), Residual SE = **15.464** on **659** df, AIC = **5619.0**, BIC = **5686.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0371** | 5.0804 | ±10.1609 | **+24.808** | **7.29e-136** | *** |
| Education: graduate level (vs college) | -2.0370 | 1.2898 | ±2.5797 | -1.579 | 0.1143 |  |
| Education: high school or below (vs college) | +3.7569 | 2.4530 | ±4.9061 | +1.532 | 0.1256 |  |
| Site: UCSD (vs UAB) | +0.7356 | 1.6264 | ±3.2527 | +0.452 | 0.6511 |  |
| Site: UW (vs UAB) | +0.1017 | 1.5720 | ±3.1440 | +0.065 | 0.9484 |  |
| Season: spring (vs autumn) | +3.0522 | 1.7027 | ±3.4053 | +1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +2.4157 | 1.8110 | ±3.6221 | +1.334 | 0.1822 |  |
| **Season: winter (vs autumn)** | **+4.0136** | 1.7486 | ±3.4972 | **+2.295** | **0.0217** | * |
| Age (years) | -0.1132 | 0.0617 | ±0.1234 | -1.834 | 0.0666 | . |
| **BMI (kg/m2)** | **+0.1652** | 0.0840 | ±0.1679 | **+1.967** | **0.0491** | * |
| Hypertension | +0.7319 | 1.4176 | ±2.8352 | +0.516 | 0.6057 |  |
| High cholesterol | -0.1189 | 1.2835 | ±2.5669 | -0.093 | 0.9262 |  |
| Kidney disease | -1.0254 | 2.0390 | ±4.0780 | -0.503 | 0.6150 |  |
| Circulatory disease | +1.0556 | 2.0432 | ±4.0864 | +0.517 | 0.6054 |  |
| Time 54-69, pooled (%) | +0.5334 | 1.5831 | ±3.1661 | +0.337 | 0.7361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.0366**, Adj R² = **0.0161**, F-statistic = **1.79** (p = **0.0369**), Residual SE = **15.466** on **659** df, AIC = **5619.2**, BIC = **5686.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1326** | 5.0854 | ±10.1709 | **+24.803** | **8.38e-136** | *** |
| Education: graduate level (vs college) | -2.0685 | 1.2915 | ±2.5830 | -1.602 | 0.1093 |  |
| Education: high school or below (vs college) | +3.7182 | 2.4531 | ±4.9062 | +1.516 | 0.1296 |  |
| Site: UCSD (vs UAB) | +0.7427 | 1.6273 | ±3.2546 | +0.456 | 0.6481 |  |
| Site: UW (vs UAB) | +0.0915 | 1.5739 | ±3.1479 | +0.058 | 0.9536 |  |
| Season: spring (vs autumn) | +3.0618 | 1.7034 | ±3.4067 | +1.797 | 0.0723 | . |
| Season: summer (vs autumn) | +2.4340 | 1.8111 | ±3.6222 | +1.344 | 0.1790 |  |
| **Season: winter (vs autumn)** | **+4.0344** | 1.7491 | ±3.4982 | **+2.307** | **0.0211** | * |
| Age (years) | -0.1134 | 0.0617 | ±0.1234 | -1.838 | 0.0661 | . |
| **BMI (kg/m2)** | **+0.1648** | 0.0840 | ±0.1679 | **+1.962** | **0.0497** | * |
| Hypertension | +0.7379 | 1.4173 | ±2.8345 | +0.521 | 0.6026 |  |
| High cholesterol | -0.1113 | 1.2826 | ±2.5652 | -0.087 | 0.9308 |  |
| Kidney disease | -1.0393 | 2.0373 | ±4.0747 | -0.510 | 0.6100 |  |
| Circulatory disease | +1.0427 | 2.0439 | ±4.0878 | +0.510 | 0.6099 |  |
| Avg. daily time 54-69 (%) | +0.2475 | 1.5088 | ±3.0176 | +0.164 | 0.8697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.0368**, Adj R² = **0.0164**, F-statistic = **1.80** (p = **0.0352**), Residual SE = **15.464** on **659** df, AIC = **5619.0**, BIC = **5686.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0371** | 5.0804 | ±10.1609 | **+24.808** | **7.29e-136** | *** |
| Education: graduate level (vs college) | -2.0370 | 1.2898 | ±2.5797 | -1.579 | 0.1143 |  |
| Education: high school or below (vs college) | +3.7569 | 2.4530 | ±4.9061 | +1.532 | 0.1256 |  |
| Site: UCSD (vs UAB) | +0.7356 | 1.6264 | ±3.2527 | +0.452 | 0.6511 |  |
| Site: UW (vs UAB) | +0.1017 | 1.5720 | ±3.1440 | +0.065 | 0.9484 |  |
| Season: spring (vs autumn) | +3.0522 | 1.7027 | ±3.4053 | +1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +2.4157 | 1.8110 | ±3.6221 | +1.334 | 0.1822 |  |
| **Season: winter (vs autumn)** | **+4.0136** | 1.7486 | ±3.4972 | **+2.295** | **0.0217** | * |
| Age (years) | -0.1132 | 0.0617 | ±0.1234 | -1.834 | 0.0666 | . |
| **BMI (kg/m2)** | **+0.1652** | 0.0840 | ±0.1679 | **+1.967** | **0.0491** | * |
| Hypertension | +0.7319 | 1.4176 | ±2.8352 | +0.516 | 0.6057 |  |
| High cholesterol | -0.1189 | 1.2835 | ±2.5669 | -0.093 | 0.9262 |  |
| Kidney disease | -1.0254 | 2.0390 | ±4.0780 | -0.503 | 0.6150 |  |
| Circulatory disease | +1.0556 | 2.0432 | ±4.0864 | +0.517 | 0.6054 |  |
| Time < 70 (%) | +0.5334 | 1.5831 | ±3.1661 | +0.337 | 0.7361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.0366**, Adj R² = **0.0161**, F-statistic = **1.79** (p = **0.0369**), Residual SE = **15.466** on **659** df, AIC = **5619.2**, BIC = **5686.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1326** | 5.0854 | ±10.1709 | **+24.803** | **8.38e-136** | *** |
| Education: graduate level (vs college) | -2.0685 | 1.2915 | ±2.5830 | -1.602 | 0.1093 |  |
| Education: high school or below (vs college) | +3.7182 | 2.4531 | ±4.9062 | +1.516 | 0.1296 |  |
| Site: UCSD (vs UAB) | +0.7427 | 1.6273 | ±3.2546 | +0.456 | 0.6481 |  |
| Site: UW (vs UAB) | +0.0915 | 1.5739 | ±3.1479 | +0.058 | 0.9536 |  |
| Season: spring (vs autumn) | +3.0618 | 1.7034 | ±3.4067 | +1.797 | 0.0723 | . |
| Season: summer (vs autumn) | +2.4340 | 1.8111 | ±3.6222 | +1.344 | 0.1790 |  |
| **Season: winter (vs autumn)** | **+4.0344** | 1.7491 | ±3.4982 | **+2.307** | **0.0211** | * |
| Age (years) | -0.1134 | 0.0617 | ±0.1234 | -1.838 | 0.0661 | . |
| **BMI (kg/m2)** | **+0.1648** | 0.0840 | ±0.1679 | **+1.962** | **0.0497** | * |
| Hypertension | +0.7379 | 1.4173 | ±2.8345 | +0.521 | 0.6026 |  |
| High cholesterol | -0.1113 | 1.2826 | ±2.5652 | -0.087 | 0.9308 |  |
| Kidney disease | -1.0393 | 2.0373 | ±4.0747 | -0.510 | 0.6100 |  |
| Circulatory disease | +1.0427 | 2.0439 | ±4.0878 | +0.510 | 0.6099 |  |
| Avg. daily time < 70 (%) | +0.2475 | 1.5088 | ±3.0176 | +0.164 | 0.8697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.95** (p = **0.0190**), Residual SE = **15.439** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2520** | 5.0852 | ±10.1705 | **+24.827** | **4.57e-136** | *** |
| Education: graduate level (vs college) | -2.0382 | 1.2855 | ±2.5710 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +3.7264 | 2.4674 | ±4.9348 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5855 | 1.6252 | ±3.2504 | +0.360 | 0.7187 |  |
| Site: UW (vs UAB) | +0.1795 | 1.5822 | ±3.1643 | +0.113 | 0.9097 |  |
| Season: spring (vs autumn) | +2.9874 | 1.6945 | ±3.3890 | +1.763 | 0.0779 | . |
| Season: summer (vs autumn) | +2.3951 | 1.8233 | ±3.6467 | +1.314 | 0.1890 |  |
| **Season: winter (vs autumn)** | **+3.9584** | 1.7551 | ±3.5102 | **+2.255** | **0.0241** | * |
| Age (years) | -0.1084 | 0.0623 | ±0.1246 | -1.741 | 0.0817 | . |
| **BMI (kg/m2)** | **+0.1712** | 0.0840 | ±0.1680 | **+2.039** | **0.0415** | * |
| Hypertension | +0.7669 | 1.4136 | ±2.8271 | +0.543 | 0.5874 |  |
| High cholesterol | +0.0016 | 1.2891 | ±2.5782 | +0.001 | 0.9990 |  |
| Kidney disease | -0.9116 | 2.0330 | ±4.0661 | -0.448 | 0.6539 |  |
| Circulatory disease | +1.1670 | 2.0469 | ±4.0937 | +0.570 | 0.5686 |  |
| Time 181-250, pooled (%) | -0.3396 | 0.2377 | ±0.4753 | -1.429 | 0.1531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.0401**, Adj R² = **0.0197**, F-statistic = **1.97** (p = **0.0181**), Residual SE = **15.437** on **659** df, AIC = **5616.7**, BIC = **5684.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2354** | 5.0790 | ±10.1580 | **+24.854** | **2.33e-136** | *** |
| Education: graduate level (vs college) | -2.0297 | 1.2865 | ±2.5730 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +3.7229 | 2.4650 | ±4.9300 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5659 | 1.6249 | ±3.2498 | +0.348 | 0.7276 |  |
| Site: UW (vs UAB) | +0.1663 | 1.5816 | ±3.1631 | +0.105 | 0.9163 |  |
| Season: spring (vs autumn) | +2.9911 | 1.6950 | ±3.3901 | +1.765 | 0.0776 | . |
| Season: summer (vs autumn) | +2.3998 | 1.8234 | ±3.6468 | +1.316 | 0.1881 |  |
| **Season: winter (vs autumn)** | **+3.9383** | 1.7546 | ±3.5092 | **+2.245** | **0.0248** | * |
| Age (years) | -0.1090 | 0.0622 | ±0.1244 | -1.753 | 0.0796 | . |
| **BMI (kg/m2)** | **+0.1733** | 0.0840 | ±0.1679 | **+2.064** | **0.0390** | * |
| Hypertension | +0.7574 | 1.4139 | ±2.8277 | +0.536 | 0.5922 |  |
| High cholesterol | +0.0084 | 1.2888 | ±2.5776 | +0.006 | 0.9948 |  |
| Kidney disease | -0.8937 | 2.0313 | ±4.0627 | -0.440 | 0.6600 |  |
| Circulatory disease | +1.2001 | 2.0438 | ±4.0876 | +0.587 | 0.5571 |  |
| Avg. daily time 181-250 (%) | -0.3593 | 0.2425 | ±0.4851 | -1.481 | 0.1385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.95** (p = **0.0190**), Residual SE = **15.439** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2520** | 5.0852 | ±10.1705 | **+24.827** | **4.57e-136** | *** |
| Education: graduate level (vs college) | -2.0382 | 1.2855 | ±2.5710 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +3.7264 | 2.4674 | ±4.9348 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5855 | 1.6252 | ±3.2504 | +0.360 | 0.7187 |  |
| Site: UW (vs UAB) | +0.1795 | 1.5822 | ±3.1643 | +0.113 | 0.9097 |  |
| Season: spring (vs autumn) | +2.9874 | 1.6945 | ±3.3890 | +1.763 | 0.0779 | . |
| Season: summer (vs autumn) | +2.3951 | 1.8233 | ±3.6467 | +1.314 | 0.1890 |  |
| **Season: winter (vs autumn)** | **+3.9584** | 1.7551 | ±3.5102 | **+2.255** | **0.0241** | * |
| Age (years) | -0.1084 | 0.0623 | ±0.1246 | -1.741 | 0.0817 | . |
| **BMI (kg/m2)** | **+0.1712** | 0.0840 | ±0.1680 | **+2.039** | **0.0415** | * |
| Hypertension | +0.7669 | 1.4136 | ±2.8271 | +0.543 | 0.5874 |  |
| High cholesterol | +0.0016 | 1.2891 | ±2.5782 | +0.001 | 0.9990 |  |
| Kidney disease | -0.9116 | 2.0330 | ±4.0661 | -0.448 | 0.6539 |  |
| Circulatory disease | +1.1670 | 2.0469 | ±4.0937 | +0.570 | 0.5686 |  |
| Time > 180 (%) | -0.3396 | 0.2377 | ±0.4753 | -1.429 | 0.1531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.0401**, Adj R² = **0.0197**, F-statistic = **1.97** (p = **0.0181**), Residual SE = **15.437** on **659** df, AIC = **5616.7**, BIC = **5684.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2354** | 5.0790 | ±10.1580 | **+24.854** | **2.33e-136** | *** |
| Education: graduate level (vs college) | -2.0297 | 1.2865 | ±2.5730 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +3.7229 | 2.4650 | ±4.9300 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5659 | 1.6249 | ±3.2498 | +0.348 | 0.7276 |  |
| Site: UW (vs UAB) | +0.1663 | 1.5816 | ±3.1631 | +0.105 | 0.9163 |  |
| Season: spring (vs autumn) | +2.9911 | 1.6950 | ±3.3901 | +1.765 | 0.0776 | . |
| Season: summer (vs autumn) | +2.3998 | 1.8234 | ±3.6468 | +1.316 | 0.1881 |  |
| **Season: winter (vs autumn)** | **+3.9383** | 1.7546 | ±3.5092 | **+2.245** | **0.0248** | * |
| Age (years) | -0.1090 | 0.0622 | ±0.1244 | -1.753 | 0.0796 | . |
| **BMI (kg/m2)** | **+0.1733** | 0.0840 | ±0.1679 | **+2.064** | **0.0390** | * |
| Hypertension | +0.7574 | 1.4139 | ±2.8277 | +0.536 | 0.5922 |  |
| High cholesterol | +0.0084 | 1.2888 | ±2.5776 | +0.006 | 0.9948 |  |
| Kidney disease | -0.8937 | 2.0313 | ±4.0627 | -0.440 | 0.6600 |  |
| Circulatory disease | +1.2001 | 2.0438 | ±4.0876 | +0.587 | 0.5571 |  |
| Avg. daily time > 180 (%) | -0.3593 | 0.2425 | ±0.4851 | -1.481 | 0.1385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.0392**, Adj R² = **0.0187**, F-statistic = **1.92** (p = **0.0219**), Residual SE = **15.445** on **659** df, AIC = **5617.4**, BIC = **5685.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0998** | 5.0657 | ±10.1315 | **+24.893** | **8.94e-137** | *** |
| Education: graduate level (vs college) | -2.1181 | 1.2790 | ±2.5580 | -1.656 | 0.0977 | . |
| Education: high school or below (vs college) | +3.7748 | 2.4872 | ±4.9744 | +1.518 | 0.1291 |  |
| Site: UCSD (vs UAB) | +0.6826 | 1.6235 | ±3.2470 | +0.420 | 0.6742 |  |
| Site: UW (vs UAB) | +0.1467 | 1.5716 | ±3.1432 | +0.093 | 0.9257 |  |
| Season: spring (vs autumn) | +3.0475 | 1.6978 | ±3.3955 | +1.795 | 0.0727 | . |
| Season: summer (vs autumn) | +2.4431 | 1.8236 | ±3.6473 | +1.340 | 0.1803 |  |
| **Season: winter (vs autumn)** | **+4.0741** | 1.7527 | ±3.5054 | **+2.324** | **0.0201** | * |
| Age (years) | -0.1160 | 0.0614 | ±0.1229 | -1.888 | 0.0591 | . |
| **BMI (kg/m2)** | **+0.1799** | 0.0832 | ±0.1665 | **+2.161** | **0.0307** | * |
| Hypertension | +0.6951 | 1.4144 | ±2.8288 | +0.491 | 0.6231 |  |
| High cholesterol | +0.0668 | 1.2951 | ±2.5901 | +0.052 | 0.9589 |  |
| Kidney disease | -1.0634 | 2.0465 | ±4.0930 | -0.520 | 0.6033 |  |
| Circulatory disease | +1.0200 | 2.0772 | ±4.1544 | +0.491 | 0.6234 |  |
| Nocturnal time > 180 (%) | -0.2651 | 0.1892 | ±0.3784 | -1.401 | 0.1611 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 593; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1195**, F-statistic = **9.04** (p = **6.37e-14**), Residual SE = **3709.413** on **582** df, AIC = **11441.1**, BIC = **11489.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17270.8292** | 1250.4427 | ±2500.8853 | **+13.812** | **2.16e-43** | *** |
| Education: graduate level (vs college) | -578.8517 | 310.6041 | ±621.2082 | -1.864 | 0.0624 | . |
| Education: high school or below (vs college) | +1371.0371 | 776.6242 | ±1553.2485 | +1.765 | 0.0775 | . |
| Site: UCSD (vs UAB) | -158.5977 | 416.8466 | ±833.6931 | -0.380 | 0.7036 |  |
| Site: UW (vs UAB) | -476.6411 | 402.3052 | ±804.6103 | -1.185 | 0.2361 |  |
| **Age (years)** | **-106.4262** | 15.0854 | ±30.1708 | **-7.055** | **1.73e-12** | *** |
| BMI (kg/m2) | -18.0475 | 25.1397 | ±50.2793 | -0.718 | 0.4728 |  |
| Hypertension | +267.9617 | 384.8497 | ±769.6995 | +0.696 | 0.4863 |  |
| High cholesterol | -234.4279 | 306.4427 | ±612.8854 | -0.765 | 0.4443 |  |
| Kidney disease | -605.4053 | 565.4140 | ±1130.8280 | -1.071 | 0.2843 |  |
| **Circulatory disease** | **-1008.2603** | 493.1095 | ±986.2191 | **-2.045** | **0.0409** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **593**, R² = **0.1421**, Adj R² = **0.1258**, F-statistic = **8.75** (p = **1.90e-14**), Residual SE = **3696.097** on **581** df, AIC = **11437.8**, BIC = **11490.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11824.8308** | 2781.3840 | ±5562.7679 | **+4.251** | **2.12e-05** | *** |
| Education: graduate level (vs college) | -591.4675 | 308.2507 | ±616.5014 | -1.919 | 0.0550 | . |
| Education: high school or below (vs college) | +1377.4586 | 777.6321 | ±1555.2643 | +1.771 | 0.0765 | . |
| Site: UCSD (vs UAB) | -136.9874 | 414.4365 | ±828.8729 | -0.331 | 0.7410 |  |
| Site: UW (vs UAB) | -480.1261 | 401.3306 | ±802.6612 | -1.196 | 0.2316 |  |
| **Age (years)** | **-110.8054** | 14.9913 | ±29.9825 | **-7.391** | **1.45e-13** | *** |
| BMI (kg/m2) | -25.6574 | 24.3460 | ±48.6921 | -1.054 | 0.2919 |  |
| Hypertension | +209.3878 | 385.3062 | ±770.6124 | +0.543 | 0.5868 |  |
| High cholesterol | -332.9329 | 314.1540 | ±628.3081 | -1.060 | 0.2892 |  |
| Kidney disease | -598.4686 | 560.9389 | ±1121.8778 | -1.067 | 0.2860 |  |
| **Circulatory disease** | **-993.2849** | 486.7873 | ±973.5746 | **-2.040** | **0.0413** | * |
| **HbA1c (%)** | **+1073.7239** | 486.6861 | ±973.3722 | **+2.206** | **0.0274** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.99e-13**), Residual SE = **3712.601** on **581** df, AIC = **11443.1**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17318.0174** | 1982.0237 | ±3964.0475 | **+8.738** | **2.38e-18** | *** |
| Education: graduate level (vs college) | -578.4736 | 310.7475 | ±621.4950 | -1.862 | 0.0627 | . |
| Education: high school or below (vs college) | +1371.0560 | 778.0507 | ±1556.1014 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -159.4493 | 415.8973 | ±831.7946 | -0.383 | 0.7014 |  |
| Site: UW (vs UAB) | -475.9900 | 402.6115 | ±805.2230 | -1.182 | 0.2371 |  |
| **Age (years)** | **-106.4017** | 15.0873 | ±30.1746 | **-7.052** | **1.76e-12** | *** |
| BMI (kg/m2) | -17.9628 | 25.2687 | ±50.5373 | -0.711 | 0.4772 |  |
| Hypertension | +268.5502 | 387.1221 | ±774.2442 | +0.694 | 0.4879 |  |
| High cholesterol | -234.1851 | 307.2667 | ±614.5334 | -0.762 | 0.4460 |  |
| Kidney disease | -604.5071 | 567.1880 | ±1134.3760 | -1.066 | 0.2865 |  |
| **Circulatory disease** | **-1007.6178** | 494.0832 | ±988.1663 | **-2.039** | **0.0414** | * |
| Mean glucose (mg/dL) | -0.4346 | 13.7189 | ±27.4379 | -0.032 | 0.9747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.99e-13**), Residual SE = **3712.601** on **581** df, AIC = **11443.1**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17378.1581** | 3656.1750 | ±7312.3501 | **+4.753** | **2.00e-06** | *** |
| Education: graduate level (vs college) | -578.4736 | 310.7475 | ±621.4950 | -1.862 | 0.0627 | . |
| Education: high school or below (vs college) | +1371.0560 | 778.0507 | ±1556.1014 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -159.4493 | 415.8973 | ±831.7946 | -0.383 | 0.7014 |  |
| Site: UW (vs UAB) | -475.9900 | 402.6115 | ±805.2230 | -1.182 | 0.2371 |  |
| **Age (years)** | **-106.4017** | 15.0873 | ±30.1746 | **-7.052** | **1.76e-12** | *** |
| BMI (kg/m2) | -17.9628 | 25.2687 | ±50.5373 | -0.711 | 0.4772 |  |
| Hypertension | +268.5502 | 387.1221 | ±774.2442 | +0.694 | 0.4879 |  |
| High cholesterol | -234.1851 | 307.2667 | ±614.5334 | -0.762 | 0.4460 |  |
| Kidney disease | -604.5071 | 567.1880 | ±1134.3760 | -1.066 | 0.2865 |  |
| **Circulatory disease** | **-1007.6178** | 494.0832 | ±988.1663 | **-2.039** | **0.0414** | * |
| GMI (%) | -18.1694 | 573.5343 | ±1147.0686 | -0.032 | 0.9747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.594** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17196.9910** | 1836.2690 | ±3672.5380 | **+9.365** | **7.59e-21** | *** |
| Education: graduate level (vs college) | -579.1488 | 310.9962 | ±621.9925 | -1.862 | 0.0626 | . |
| Education: high school or below (vs college) | +1370.4543 | 777.4472 | ±1554.8944 | +1.763 | 0.0779 | . |
| Site: UCSD (vs UAB) | -158.1655 | 417.3283 | ±834.6565 | -0.379 | 0.7047 |  |
| Site: UW (vs UAB) | -478.0631 | 401.4486 | ±802.8971 | -1.191 | 0.2337 |  |
| **Age (years)** | **-106.3949** | 15.1037 | ±30.2075 | **-7.044** | **1.86e-12** | *** |
| BMI (kg/m2) | -18.3354 | 25.7223 | ±51.4446 | -0.713 | 0.4760 |  |
| Hypertension | +267.4091 | 385.9117 | ±771.8235 | +0.693 | 0.4884 |  |
| High cholesterol | -235.5700 | 309.2971 | ±618.5942 | -0.762 | 0.4463 |  |
| Kidney disease | -606.1232 | 566.3759 | ±1132.7519 | -1.070 | 0.2845 |  |
| **Circulatory disease** | **-1008.9203** | 494.1593 | ±988.3187 | **-2.042** | **0.0412** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.6873 | 12.6735 | ±25.3471 | +0.054 | 0.9568 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1347**, Adj R² = **0.1183**, F-statistic = **8.22** (p = **1.82e-13**), Residual SE = **3711.978** on **581** df, AIC = **11442.9**, BIC = **11495.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16970.7182** | 1379.8840 | ±2759.7680 | **+12.299** | **9.21e-35** | *** |
| Education: graduate level (vs college) | -569.2457 | 310.2932 | ±620.5864 | -1.835 | 0.0666 | . |
| Education: high school or below (vs college) | +1372.8445 | 776.4057 | ±1552.8113 | +1.768 | 0.0770 | . |
| Site: UCSD (vs UAB) | -142.1482 | 417.7264 | ±835.4529 | -0.340 | 0.7336 |  |
| Site: UW (vs UAB) | -484.6003 | 400.8034 | ±801.6068 | -1.209 | 0.2266 |  |
| **Age (years)** | **-107.1279** | 15.2627 | ±30.5254 | **-7.019** | **2.24e-12** | *** |
| BMI (kg/m2) | -18.4897 | 25.1697 | ±50.3395 | -0.735 | 0.4626 |  |
| Hypertension | +258.8673 | 384.1161 | ±768.2323 | +0.674 | 0.5004 |  |
| High cholesterol | -237.6574 | 307.3980 | ±614.7959 | -0.773 | 0.4394 |  |
| Kidney disease | -612.9529 | 568.8319 | ±1137.6638 | -1.078 | 0.2812 |  |
| **Circulatory disease** | **-1006.9504** | 494.3676 | ±988.7351 | **-2.037** | **0.0417** | * |
| Glucose SD, pooled (mg/dL) | +18.3482 | 41.2610 | ±82.5220 | +0.445 | 0.6565 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1345**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.95e-13**), Residual SE = **3712.467** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17143.3768** | 1368.5698 | ±2737.1396 | **+12.526** | **5.35e-36** | *** |
| Education: graduate level (vs college) | -575.4764 | 310.9087 | ±621.8174 | -1.851 | 0.0642 | . |
| Education: high school or below (vs college) | +1371.3479 | 777.2740 | ±1554.5479 | +1.764 | 0.0777 | . |
| Site: UCSD (vs UAB) | -149.7948 | 416.7296 | ±833.4592 | -0.359 | 0.7193 |  |
| Site: UW (vs UAB) | -480.2423 | 401.9390 | ±803.8781 | -1.195 | 0.2322 |  |
| **Age (years)** | **-106.7666** | 15.2369 | ±30.4737 | **-7.007** | **2.43e-12** | *** |
| BMI (kg/m2) | -18.3090 | 25.2034 | ±50.4068 | -0.726 | 0.4676 |  |
| Hypertension | +264.4228 | 384.8881 | ±769.7763 | +0.687 | 0.4921 |  |
| High cholesterol | -235.7332 | 307.2173 | ±614.4346 | -0.767 | 0.4429 |  |
| Kidney disease | -609.3386 | 567.5705 | ±1135.1410 | -1.074 | 0.2830 |  |
| **Circulatory disease** | **-1007.9536** | 494.3975 | ±988.7949 | **-2.039** | **0.0415** | * |
| Avg. daily SD (mg/dL) | +8.7525 | 41.6286 | ±83.2571 | +0.210 | 0.8335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **593**, R² = **0.1345**, Adj R² = **0.1181**, F-statistic = **8.21** (p = **1.94e-13**), Residual SE = **3712.425** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17068.7996** | 1426.3352 | ±2852.6705 | **+11.967** | **5.30e-33** | *** |
| Education: graduate level (vs college) | -571.0787 | 309.4186 | ±618.8372 | -1.846 | 0.0649 | . |
| Education: high school or below (vs college) | +1372.6077 | 776.9810 | ±1553.9621 | +1.767 | 0.0773 | . |
| Site: UCSD (vs UAB) | -151.9570 | 418.6475 | ±837.2949 | -0.363 | 0.7166 |  |
| Site: UW (vs UAB) | -478.5918 | 401.8645 | ±803.7290 | -1.191 | 0.2337 |  |
| **Age (years)** | **-106.7306** | 15.2641 | ±30.5283 | **-6.992** | **2.71e-12** | *** |
| BMI (kg/m2) | -17.9515 | 25.1465 | ±50.2929 | -0.714 | 0.4753 |  |
| Hypertension | +264.3268 | 383.5737 | ±767.1473 | +0.689 | 0.4908 |  |
| High cholesterol | -234.7521 | 307.0385 | ±614.0770 | -0.765 | 0.4445 |  |
| Kidney disease | -606.6295 | 567.7556 | ±1135.5112 | -1.068 | 0.2853 |  |
| **Circulatory disease** | **-1004.7199** | 493.6984 | ±987.3968 | **-2.035** | **0.0418** | * |
| CV (%) | +13.1953 | 53.3964 | ±106.7928 | +0.247 | 0.8048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.95e-13**), Residual SE = **3712.478** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17453.7439** | 1606.6735 | ±3213.3471 | **+10.863** | **1.72e-27** | *** |
| Education: graduate level (vs college) | -572.0337 | 309.1143 | ±618.2286 | -1.851 | 0.0642 | . |
| Education: high school or below (vs college) | +1371.6913 | 777.0411 | ±1554.0822 | +1.765 | 0.0775 | . |
| Site: UCSD (vs UAB) | -153.5738 | 418.0013 | ±836.0026 | -0.367 | 0.7133 |  |
| Site: UW (vs UAB) | -478.8689 | 401.5890 | ±803.1780 | -1.192 | 0.2331 |  |
| **Age (years)** | **-106.6565** | 15.2477 | ±30.4954 | **-6.995** | **2.65e-12** | *** |
| BMI (kg/m2) | -17.9705 | 25.1580 | ±50.3159 | -0.714 | 0.4750 |  |
| Hypertension | +265.0034 | 383.4396 | ±766.8792 | +0.691 | 0.4895 |  |
| High cholesterol | -234.4712 | 307.0252 | ±614.0503 | -0.764 | 0.4451 |  |
| Kidney disease | -606.6047 | 567.3671 | ±1134.7342 | -1.069 | 0.2850 |  |
| **Circulatory disease** | **-1004.9895** | 493.7249 | ±987.4498 | **-2.036** | **0.0418** | * |
| Mean / SD ratio | -27.4057 | 133.5297 | ±267.0595 | -0.205 | 0.8374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.97e-13**), Residual SE = **3712.552** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17384.1088** | 1578.3248 | ±3156.6495 | **+11.014** | **3.26e-28** | *** |
| Education: graduate level (vs college) | -575.3383 | 310.0980 | ±620.1960 | -1.855 | 0.0635 | . |
| Education: high school or below (vs college) | +1370.9144 | 777.2976 | ±1554.5953 | +1.764 | 0.0778 | . |
| Site: UCSD (vs UAB) | -154.6045 | 417.0325 | ±834.0650 | -0.371 | 0.7108 |  |
| Site: UW (vs UAB) | -478.2784 | 402.0413 | ±804.0825 | -1.190 | 0.2342 |  |
| **Age (years)** | **-106.5931** | 15.2686 | ±30.5371 | **-6.981** | **2.93e-12** | *** |
| BMI (kg/m2) | -18.0800 | 25.1802 | ±50.3603 | -0.718 | 0.4727 |  |
| Hypertension | +267.2443 | 384.7144 | ±769.4288 | +0.695 | 0.4873 |  |
| High cholesterol | -234.3819 | 306.9951 | ±613.9901 | -0.763 | 0.4452 |  |
| Kidney disease | -606.5828 | 566.8410 | ±1133.6819 | -1.070 | 0.2846 |  |
| **Circulatory disease** | **-1006.3671** | 493.5028 | ±987.0056 | **-2.039** | **0.0414** | * |
| Avg. daily mean/SD | -14.4739 | 109.6830 | ±219.3660 | -0.132 | 0.8950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **593**, R² = **0.1577**, Adj R² = **0.1418**, F-statistic = **9.89** (p = **1.43e-16**), Residual SE = **3662.222** on **581** df, AIC = **11426.8**, BIC = **11479.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13951.1236** | 1384.9433 | ±2769.8867 | **+10.073** | **7.24e-24** | *** |
| Education: graduate level (vs college) | -554.3693 | 304.0557 | ±608.1114 | -1.823 | 0.0683 | . |
| Education: high school or below (vs college) | +1193.7531 | 779.2668 | ±1558.5335 | +1.532 | 0.1255 |  |
| Site: UCSD (vs UAB) | -90.6408 | 410.7545 | ±821.5091 | -0.221 | 0.8254 |  |
| Site: UW (vs UAB) | -456.9627 | 397.3790 | ±794.7581 | -1.150 | 0.2502 |  |
| **Age (years)** | **-106.4514** | 14.8268 | ±29.6535 | **-7.180** | **6.99e-13** | *** |
| BMI (kg/m2) | -17.7222 | 24.1081 | ±48.2161 | -0.735 | 0.4623 |  |
| Hypertension | +348.8348 | 383.3914 | ±766.7827 | +0.910 | 0.3629 |  |
| High cholesterol | -232.6933 | 301.6073 | ±603.2146 | -0.772 | 0.4404 |  |
| Kidney disease | -725.2339 | 571.5479 | ±1143.0959 | -1.269 | 0.2045 |  |
| Circulatory disease | -893.0417 | 497.0552 | ±994.1104 | -1.797 | 0.0724 | . |
| **MAG (mg/dL/h)** | **+90.8297** | 25.7177 | ±51.4355 | **+3.532** | **4.13e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **593**, R² = **0.1356**, Adj R² = **0.1192**, F-statistic = **8.29** (p = **1.37e-13**), Residual SE = **3709.994** on **581** df, AIC = **11442.2**, BIC = **11494.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16544.6304** | 1453.8668 | ±2907.7337 | **+11.380** | **5.28e-30** | *** |
| Education: graduate level (vs college) | -572.9932 | 311.1507 | ±622.3013 | -1.842 | 0.0655 | . |
| Education: high school or below (vs college) | +1356.1676 | 776.8371 | ±1553.6741 | +1.746 | 0.0809 | . |
| Site: UCSD (vs UAB) | -135.1396 | 416.0419 | ±832.0838 | -0.325 | 0.7453 |  |
| Site: UW (vs UAB) | -492.5178 | 401.8603 | ±803.7205 | -1.226 | 0.2204 |  |
| **Age (years)** | **-107.6523** | 15.1872 | ±30.3744 | **-7.088** | **1.36e-12** | *** |
| BMI (kg/m2) | -17.1775 | 25.1938 | ±50.3875 | -0.682 | 0.4954 |  |
| Hypertension | +264.0079 | 385.4670 | ±770.9340 | +0.685 | 0.4934 |  |
| High cholesterol | -233.5913 | 306.6018 | ±613.2037 | -0.762 | 0.4461 |  |
| Kidney disease | -626.4669 | 568.2137 | ±1136.4274 | -1.103 | 0.2702 |  |
| **Circulatory disease** | **-1010.5797** | 494.0420 | ±988.0840 | **-2.046** | **0.0408** | * |
| Avg. daily range (mg/dL) | +8.6931 | 9.3253 | ±18.6505 | +0.932 | 0.3512 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **593**, R² = **0.1438**, Adj R² = **0.1276**, F-statistic = **8.87** (p = **1.10e-14**), Residual SE = **3692.279** on **581** df, AIC = **11436.5**, BIC = **11489.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16433.4853** | 1238.9385 | ±2477.8771 | **+13.264** | **3.74e-40** | *** |
| Education: graduate level (vs college) | -573.8199 | 308.1882 | ±616.3764 | -1.862 | 0.0626 | . |
| Education: high school or below (vs college) | +1385.6472 | 766.5799 | ±1533.1597 | +1.808 | 0.0707 | . |
| Site: UCSD (vs UAB) | -125.8880 | 415.5236 | ±831.0472 | -0.303 | 0.7619 |  |
| Site: UW (vs UAB) | -488.5381 | 397.3297 | ±794.6594 | -1.230 | 0.2189 |  |
| **Age (years)** | **-106.1058** | 15.0601 | ±30.1203 | **-7.045** | **1.85e-12** | *** |
| BMI (kg/m2) | -24.4950 | 25.0147 | ±50.0293 | -0.979 | 0.3275 |  |
| Hypertension | +267.2084 | 380.1556 | ±760.3112 | +0.703 | 0.4821 |  |
| High cholesterol | -284.0465 | 307.9535 | ±615.9070 | -0.922 | 0.3563 |  |
| Kidney disease | -590.6265 | 561.1517 | ±1122.3033 | -1.053 | 0.2926 |  |
| **Circulatory disease** | **-1006.8727** | 493.0741 | ±986.1482 | **-2.042** | **0.0411** | * |
| **SD of daily means (mg/dL)** | **+175.1072** | 77.0978 | ±154.1957 | **+2.271** | **0.0231** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.99e-13**), Residual SE = **3712.602** on **581** df, AIC = **11443.1**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17431.5894** | 5952.4245 | ±11904.8490 | **+2.928** | **0.0034** | ** |
| Education: graduate level (vs college) | -578.7877 | 311.1963 | ±622.3926 | -1.860 | 0.0629 | . |
| Education: high school or below (vs college) | +1371.4197 | 780.4041 | ±1560.8081 | +1.757 | 0.0789 | . |
| Site: UCSD (vs UAB) | -157.7589 | 419.3374 | ±838.6749 | -0.376 | 0.7068 |  |
| Site: UW (vs UAB) | -477.0293 | 401.7645 | ±803.5290 | -1.187 | 0.2351 |  |
| **Age (years)** | **-106.4573** | 15.0786 | ±30.1573 | **-7.060** | **1.66e-12** | *** |
| BMI (kg/m2) | -18.0768 | 25.2158 | ±50.4317 | -0.717 | 0.4734 |  |
| Hypertension | +267.9819 | 385.2821 | ±770.5641 | +0.696 | 0.4867 |  |
| High cholesterol | -235.0346 | 308.1483 | ±616.2966 | -0.763 | 0.4456 |  |
| Kidney disease | -605.8635 | 566.3937 | ±1132.7875 | -1.070 | 0.2848 |  |
| **Circulatory disease** | **-1009.0474** | 493.7708 | ±987.5415 | **-2.044** | **0.0410** | * |
| Time in range 70-180, pooled (%) | -1.6095 | 58.8774 | ±117.7548 | -0.027 | 0.9782 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.583** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17738.6654** | 6007.4487 | ±12014.8975 | **+2.953** | **0.0031** | ** |
| Education: graduate level (vs college) | -578.7190 | 311.1141 | ±622.2282 | -1.860 | 0.0629 | . |
| Education: high school or below (vs college) | +1372.4222 | 780.2959 | ±1560.5919 | +1.759 | 0.0786 | . |
| Site: UCSD (vs UAB) | -156.0382 | 419.3391 | ±838.6782 | -0.372 | 0.7098 |  |
| Site: UW (vs UAB) | -477.5417 | 402.0067 | ±804.0135 | -1.188 | 0.2349 |  |
| **Age (years)** | **-106.5098** | 15.0776 | ±30.1551 | **-7.064** | **1.62e-12** | *** |
| BMI (kg/m2) | -18.1550 | 25.2354 | ±50.4708 | -0.719 | 0.4719 |  |
| Hypertension | +268.1563 | 385.2156 | ±770.4311 | +0.696 | 0.4864 |  |
| High cholesterol | -236.2019 | 308.0162 | ±616.0324 | -0.767 | 0.4432 |  |
| Kidney disease | -606.8048 | 566.3888 | ±1132.7777 | -1.071 | 0.2840 |  |
| **Circulatory disease** | **-1010.7979** | 494.0180 | ±988.0361 | **-2.046** | **0.0407** | * |
| Avg. daily time in range 70-180 (%) | -4.6772 | 59.2992 | ±118.5984 | -0.079 | 0.9371 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **593**, R² = **0.1346**, Adj R² = **0.1182**, F-statistic = **8.22** (p = **1.86e-13**), Residual SE = **3712.126** on **581** df, AIC = **11442.9**, BIC = **11495.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17310.8127** | 1260.8379 | ±2521.6759 | **+13.730** | **6.75e-43** | *** |
| Education: graduate level (vs college) | -593.2115 | 313.1815 | ±626.3630 | -1.894 | 0.0582 | . |
| Education: high school or below (vs college) | +1355.1262 | 776.1060 | ±1552.2119 | +1.746 | 0.0808 | . |
| Site: UCSD (vs UAB) | -150.8911 | 419.4364 | ±838.8728 | -0.360 | 0.7190 |  |
| Site: UW (vs UAB) | -478.4559 | 402.3708 | ±804.7416 | -1.189 | 0.2344 |  |
| **Age (years)** | **-106.5054** | 15.1299 | ±30.2597 | **-7.039** | **1.93e-12** | *** |
| BMI (kg/m2) | -18.2068 | 25.1447 | ±50.2893 | -0.724 | 0.4690 |  |
| Hypertension | +268.7329 | 385.1777 | ±770.3555 | +0.698 | 0.4854 |  |
| High cholesterol | -232.7983 | 306.6463 | ±613.2926 | -0.759 | 0.4477 |  |
| Kidney disease | -610.8263 | 564.5797 | ±1129.1594 | -1.082 | 0.2793 |  |
| **Circulatory disease** | **-1013.4199** | 493.4754 | ±986.9508 | **-2.054** | **0.0400** | * |
| Time 54-69, pooled (%) | -110.8416 | 370.7164 | ±741.4328 | -0.299 | 0.7649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **593**, R² = **0.1348**, Adj R² = **0.1184**, F-statistic = **8.23** (p = **1.76e-13**), Residual SE = **3711.768** on **581** df, AIC = **11442.8**, BIC = **11495.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17316.7396** | 1258.9383 | ±2517.8766 | **+13.755** | **4.75e-43** | *** |
| Education: graduate level (vs college) | -598.6666 | 312.8213 | ±625.6426 | -1.914 | 0.0557 | . |
| Education: high school or below (vs college) | +1348.2542 | 776.0834 | ±1552.1668 | +1.737 | 0.0823 | . |
| Site: UCSD (vs UAB) | -145.2398 | 420.6501 | ±841.3002 | -0.345 | 0.7299 |  |
| Site: UW (vs UAB) | -478.1780 | 402.5600 | ±805.1199 | -1.188 | 0.2349 |  |
| **Age (years)** | **-106.4717** | 15.1188 | ±30.2376 | **-7.042** | **1.89e-12** | *** |
| BMI (kg/m2) | -18.2344 | 25.1544 | ±50.3087 | -0.725 | 0.4685 |  |
| Hypertension | +268.0523 | 385.2641 | ±770.5281 | +0.696 | 0.4866 |  |
| High cholesterol | -232.9887 | 306.7647 | ±613.5294 | -0.760 | 0.4476 |  |
| Kidney disease | -612.3782 | 564.3677 | ±1128.7353 | -1.085 | 0.2779 |  |
| **Circulatory disease** | **-1017.4472** | 493.3926 | ±986.7852 | **-2.062** | **0.0392** | * |
| Avg. daily time 54-69 (%) | -142.2810 | 368.4577 | ±736.9155 | -0.386 | 0.6994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **593**, R² = **0.1346**, Adj R² = **0.1182**, F-statistic = **8.22** (p = **1.86e-13**), Residual SE = **3712.126** on **581** df, AIC = **11442.9**, BIC = **11495.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17310.8127** | 1260.8379 | ±2521.6759 | **+13.730** | **6.75e-43** | *** |
| Education: graduate level (vs college) | -593.2115 | 313.1815 | ±626.3630 | -1.894 | 0.0582 | . |
| Education: high school or below (vs college) | +1355.1262 | 776.1060 | ±1552.2119 | +1.746 | 0.0808 | . |
| Site: UCSD (vs UAB) | -150.8911 | 419.4364 | ±838.8728 | -0.360 | 0.7190 |  |
| Site: UW (vs UAB) | -478.4559 | 402.3708 | ±804.7416 | -1.189 | 0.2344 |  |
| **Age (years)** | **-106.5054** | 15.1299 | ±30.2597 | **-7.039** | **1.93e-12** | *** |
| BMI (kg/m2) | -18.2068 | 25.1447 | ±50.2893 | -0.724 | 0.4690 |  |
| Hypertension | +268.7329 | 385.1777 | ±770.3555 | +0.698 | 0.4854 |  |
| High cholesterol | -232.7983 | 306.6463 | ±613.2926 | -0.759 | 0.4477 |  |
| Kidney disease | -610.8263 | 564.5797 | ±1129.1594 | -1.082 | 0.2793 |  |
| **Circulatory disease** | **-1013.4199** | 493.4754 | ±986.9508 | **-2.054** | **0.0400** | * |
| Time < 70 (%) | -110.8416 | 370.7164 | ±741.4328 | -0.299 | 0.7649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **593**, R² = **0.1348**, Adj R² = **0.1184**, F-statistic = **8.23** (p = **1.76e-13**), Residual SE = **3711.768** on **581** df, AIC = **11442.8**, BIC = **11495.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17316.7396** | 1258.9383 | ±2517.8766 | **+13.755** | **4.75e-43** | *** |
| Education: graduate level (vs college) | -598.6666 | 312.8213 | ±625.6426 | -1.914 | 0.0557 | . |
| Education: high school or below (vs college) | +1348.2542 | 776.0834 | ±1552.1668 | +1.737 | 0.0823 | . |
| Site: UCSD (vs UAB) | -145.2398 | 420.6501 | ±841.3002 | -0.345 | 0.7299 |  |
| Site: UW (vs UAB) | -478.1780 | 402.5600 | ±805.1199 | -1.188 | 0.2349 |  |
| **Age (years)** | **-106.4717** | 15.1188 | ±30.2376 | **-7.042** | **1.89e-12** | *** |
| BMI (kg/m2) | -18.2344 | 25.1544 | ±50.3087 | -0.725 | 0.4685 |  |
| Hypertension | +268.0523 | 385.2641 | ±770.5281 | +0.696 | 0.4866 |  |
| High cholesterol | -232.9887 | 306.7647 | ±613.5294 | -0.760 | 0.4476 |  |
| Kidney disease | -612.3782 | 564.3677 | ±1128.7353 | -1.085 | 0.2779 |  |
| **Circulatory disease** | **-1017.4472** | 493.3926 | ±986.7852 | **-2.062** | **0.0392** | * |
| Avg. daily time < 70 (%) | -142.2810 | 368.4577 | ±736.9155 | -0.386 | 0.6994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.570** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17272.2210** | 1250.7640 | ±2501.5280 | **+13.809** | **2.24e-43** | *** |
| Education: graduate level (vs college) | -579.3718 | 310.5592 | ±621.1185 | -1.866 | 0.0621 | . |
| Education: high school or below (vs college) | +1371.5824 | 779.0508 | ±1558.1016 | +1.761 | 0.0783 | . |
| Site: UCSD (vs UAB) | -155.1773 | 419.8789 | ±839.7577 | -0.370 | 0.7117 |  |
| Site: UW (vs UAB) | -478.1327 | 401.4145 | ±802.8290 | -1.191 | 0.2336 |  |
| **Age (years)** | **-106.5422** | 15.1010 | ±30.2021 | **-7.055** | **1.72e-12** | *** |
| BMI (kg/m2) | -18.1611 | 25.1980 | ±50.3961 | -0.721 | 0.4711 |  |
| Hypertension | +268.0746 | 385.2573 | ±770.5145 | +0.696 | 0.4865 |  |
| High cholesterol | -236.5256 | 308.5074 | ±617.0149 | -0.767 | 0.4433 |  |
| Kidney disease | -607.3370 | 566.1693 | ±1132.3387 | -1.073 | 0.2834 |  |
| **Circulatory disease** | **-1011.3613** | 493.2596 | ±986.5192 | **-2.050** | **0.0403** | * |
| Time 181-250, pooled (%) | +5.7904 | 58.1144 | ±116.2287 | +0.100 | 0.9206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.96e-13**), Residual SE = **3712.493** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17274.5278** | 1250.3118 | ±2500.6237 | **+13.816** | **2.04e-43** | *** |
| Education: graduate level (vs college) | -580.0356 | 310.5496 | ±621.0991 | -1.868 | 0.0618 | . |
| Education: high school or below (vs college) | +1372.4891 | 778.7394 | ±1557.4787 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -151.7535 | 420.1025 | ±840.2050 | -0.361 | 0.7179 |  |
| Site: UW (vs UAB) | -478.8121 | 401.7026 | ±803.4053 | -1.192 | 0.2333 |  |
| **Age (years)** | **-106.6204** | 15.0999 | ±30.1998 | **-7.061** | **1.65e-12** | *** |
| BMI (kg/m2) | -18.3068 | 25.2044 | ±50.4088 | -0.726 | 0.4676 |  |
| Hypertension | +268.4126 | 385.1995 | ±770.3990 | +0.697 | 0.4859 |  |
| High cholesterol | -238.3689 | 308.4745 | ±616.9490 | -0.773 | 0.4397 |  |
| Kidney disease | -609.1227 | 565.9292 | ±1131.8585 | -1.076 | 0.2818 |  |
| **Circulatory disease** | **-1014.7416** | 493.4852 | ±986.9704 | **-2.056** | **0.0398** | * |
| Avg. daily time 181-250 (%) | +10.6755 | 58.7609 | ±117.5217 | +0.182 | 0.8558 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.570** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17272.2210** | 1250.7640 | ±2501.5280 | **+13.809** | **2.24e-43** | *** |
| Education: graduate level (vs college) | -579.3718 | 310.5592 | ±621.1185 | -1.866 | 0.0621 | . |
| Education: high school or below (vs college) | +1371.5824 | 779.0508 | ±1558.1016 | +1.761 | 0.0783 | . |
| Site: UCSD (vs UAB) | -155.1773 | 419.8789 | ±839.7577 | -0.370 | 0.7117 |  |
| Site: UW (vs UAB) | -478.1327 | 401.4145 | ±802.8290 | -1.191 | 0.2336 |  |
| **Age (years)** | **-106.5422** | 15.1010 | ±30.2021 | **-7.055** | **1.72e-12** | *** |
| BMI (kg/m2) | -18.1611 | 25.1980 | ±50.3961 | -0.721 | 0.4711 |  |
| Hypertension | +268.0746 | 385.2573 | ±770.5145 | +0.696 | 0.4865 |  |
| High cholesterol | -236.5256 | 308.5074 | ±617.0149 | -0.767 | 0.4433 |  |
| Kidney disease | -607.3370 | 566.1693 | ±1132.3387 | -1.073 | 0.2834 |  |
| **Circulatory disease** | **-1011.3613** | 493.2596 | ±986.5192 | **-2.050** | **0.0403** | * |
| Time > 180 (%) | +5.7904 | 58.1144 | ±116.2287 | +0.100 | 0.9206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.96e-13**), Residual SE = **3712.493** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17274.5278** | 1250.3118 | ±2500.6237 | **+13.816** | **2.04e-43** | *** |
| Education: graduate level (vs college) | -580.0356 | 310.5496 | ±621.0991 | -1.868 | 0.0618 | . |
| Education: high school or below (vs college) | +1372.4891 | 778.7394 | ±1557.4787 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -151.7535 | 420.1025 | ±840.2050 | -0.361 | 0.7179 |  |
| Site: UW (vs UAB) | -478.8121 | 401.7026 | ±803.4053 | -1.192 | 0.2333 |  |
| **Age (years)** | **-106.6204** | 15.0999 | ±30.1998 | **-7.061** | **1.65e-12** | *** |
| BMI (kg/m2) | -18.3068 | 25.2044 | ±50.4088 | -0.726 | 0.4676 |  |
| Hypertension | +268.4126 | 385.1995 | ±770.3990 | +0.697 | 0.4859 |  |
| High cholesterol | -238.3689 | 308.4745 | ±616.9490 | -0.773 | 0.4397 |  |
| Kidney disease | -609.1227 | 565.9292 | ±1131.8585 | -1.076 | 0.2818 |  |
| **Circulatory disease** | **-1014.7416** | 493.4852 | ±986.9704 | **-2.056** | **0.0398** | * |
| Avg. daily time > 180 (%) | +10.6755 | 58.7609 | ±117.5217 | +0.182 | 0.8558 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.95e-13**), Residual SE = **3712.486** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17268.7687** | 1253.3686 | ±2506.7372 | **+13.778** | **3.46e-43** | *** |
| Education: graduate level (vs college) | -579.6555 | 311.0459 | ±622.0917 | -1.864 | 0.0624 | . |
| Education: high school or below (vs college) | +1375.3347 | 780.4009 | ±1560.8017 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -162.6604 | 418.6330 | ±837.2660 | -0.389 | 0.6976 |  |
| Site: UW (vs UAB) | -474.1198 | 401.7627 | ±803.5253 | -1.180 | 0.2380 |  |
| **Age (years)** | **-106.5137** | 15.0772 | ±30.1543 | **-7.065** | **1.61e-12** | *** |
| BMI (kg/m2) | -17.5626 | 25.3574 | ±50.7149 | -0.693 | 0.4886 |  |
| Hypertension | +265.7215 | 385.5192 | ±771.0385 | +0.689 | 0.4907 |  |
| High cholesterol | -227.0618 | 313.6168 | ±627.2336 | -0.724 | 0.4691 |  |
| Kidney disease | -605.9547 | 566.2521 | ±1132.5041 | -1.070 | 0.2846 |  |
| **Circulatory disease** | **-1007.5507** | 498.0312 | ±996.0624 | **-2.023** | **0.0431** | * |
| Nocturnal time > 180 (%) | -9.3573 | 62.4517 | ±124.9034 | -0.150 | 0.8809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 593; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **593**, R² = **0.1461**, Adj R² = **0.1315**, F-statistic = **9.96** (p = **1.66e-15**), Residual SE = **11.523** on **582** df, AIC = **4592.7**, BIC = **4640.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7177** | 4.1331 | ±8.2662 | **+10.577** | **3.79e-26** | *** |
| Education: graduate level (vs college) | -1.5582 | 0.9653 | ±1.9306 | -1.614 | 0.1065 |  |
| Education: high school or below (vs college) | +3.0935 | 2.3519 | ±4.7038 | +1.315 | 0.1884 |  |
| Site: UCSD (vs UAB) | -0.4355 | 1.3278 | ±2.6555 | -0.328 | 0.7429 |  |
| Site: UW (vs UAB) | -1.0831 | 1.2291 | ±2.4583 | -0.881 | 0.3782 |  |
| **Age (years)** | **-0.3515** | 0.0455 | ±0.0910 | **-7.725** | **1.11e-14** | *** |
| BMI (kg/m2) | +0.0909 | 0.0839 | ±0.1678 | +1.083 | 0.2787 |  |
| Hypertension | +0.4547 | 1.1391 | ±2.2783 | +0.399 | 0.6898 |  |
| High cholesterol | -0.5058 | 0.9706 | ±1.9412 | -0.521 | 0.6023 |  |
| Kidney disease | -1.3642 | 1.8727 | ±3.7453 | -0.728 | 0.4663 |  |
| **Circulatory disease** | **-3.0418** | 1.4901 | ±2.9803 | **-2.041** | **0.0412** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **593**, R² = **0.1514**, Adj R² = **0.1353**, F-statistic = **9.42** (p = **1.06e-15**), Residual SE = **11.497** on **581** df, AIC = **4591.1**, BIC = **4643.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6503** | 8.8068 | ±17.6136 | **+3.367** | **7.61e-04** | *** |
| Education: graduate level (vs college) | -1.5907 | 0.9592 | ±1.9183 | -1.658 | 0.0972 | . |
| Education: high school or below (vs college) | +3.1101 | 2.3679 | ±4.7358 | +1.313 | 0.1890 |  |
| Site: UCSD (vs UAB) | -0.3797 | 1.3167 | ±2.6334 | -0.288 | 0.7731 |  |
| Site: UW (vs UAB) | -1.0921 | 1.2261 | ±2.4523 | -0.891 | 0.3731 |  |
| **Age (years)** | **-0.3629** | 0.0453 | ±0.0906 | **-8.012** | **1.12e-15** | *** |
| BMI (kg/m2) | +0.0712 | 0.0821 | ±0.1643 | +0.867 | 0.3860 |  |
| Hypertension | +0.3034 | 1.1361 | ±2.2722 | +0.267 | 0.7894 |  |
| High cholesterol | -0.7602 | 0.9979 | ±1.9958 | -0.762 | 0.4462 |  |
| Kidney disease | -1.3463 | 1.8517 | ±3.7033 | -0.727 | 0.4672 |  |
| **Circulatory disease** | **-3.0031** | 1.4772 | ±2.9544 | **-2.033** | **0.0421** | * |
| HbA1c (%) | +2.7735 | 1.5711 | ±3.1422 | +1.765 | 0.0775 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **593**, R² = **0.1463**, Adj R² = **0.1301**, F-statistic = **9.05** (p = **5.19e-15**), Residual SE = **11.531** on **581** df, AIC = **4594.6**, BIC = **4647.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2485** | 6.2202 | ±12.4404 | **+6.792** | **1.10e-11** | *** |
| Education: graduate level (vs college) | -1.5699 | 0.9663 | ±1.9327 | -1.625 | 0.1042 |  |
| Education: high school or below (vs college) | +3.0929 | 2.3526 | ±4.7052 | +1.315 | 0.1886 |  |
| Site: UCSD (vs UAB) | -0.4090 | 1.3252 | ±2.6503 | -0.309 | 0.7576 |  |
| Site: UW (vs UAB) | -1.1034 | 1.2322 | ±2.4643 | -0.896 | 0.3705 |  |
| **Age (years)** | **-0.3523** | 0.0454 | ±0.0909 | **-7.754** | **8.93e-15** | *** |
| BMI (kg/m2) | +0.0882 | 0.0842 | ±0.1683 | +1.048 | 0.2945 |  |
| Hypertension | +0.4364 | 1.1418 | ±2.2835 | +0.382 | 0.7023 |  |
| High cholesterol | -0.5133 | 0.9724 | ±1.9448 | -0.528 | 0.5976 |  |
| Kidney disease | -1.3922 | 1.8701 | ±3.7403 | -0.744 | 0.4566 |  |
| **Circulatory disease** | **-3.0618** | 1.5027 | ±3.0055 | **-2.037** | **0.0416** | * |
| Mean glucose (mg/dL) | +0.0135 | 0.0419 | ±0.0838 | +0.323 | 0.7466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **593**, R² = **0.1463**, Adj R² = **0.1301**, F-statistic = **9.05** (p = **5.19e-15**), Residual SE = **11.531** on **581** df, AIC = **4594.6**, BIC = **4647.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.3761** | 11.2351 | ±22.4701 | **+3.594** | **3.26e-04** | *** |
| Education: graduate level (vs college) | -1.5699 | 0.9663 | ±1.9327 | -1.625 | 0.1042 |  |
| Education: high school or below (vs college) | +3.0929 | 2.3526 | ±4.7052 | +1.315 | 0.1886 |  |
| Site: UCSD (vs UAB) | -0.4090 | 1.3252 | ±2.6503 | -0.309 | 0.7576 |  |
| Site: UW (vs UAB) | -1.1034 | 1.2322 | ±2.4643 | -0.896 | 0.3705 |  |
| **Age (years)** | **-0.3523** | 0.0454 | ±0.0909 | **-7.754** | **8.93e-15** | *** |
| BMI (kg/m2) | +0.0882 | 0.0842 | ±0.1683 | +1.048 | 0.2945 |  |
| Hypertension | +0.4364 | 1.1418 | ±2.2835 | +0.382 | 0.7023 |  |
| High cholesterol | -0.5133 | 0.9724 | ±1.9448 | -0.528 | 0.5976 |  |
| Kidney disease | -1.3922 | 1.8701 | ±3.7403 | -0.744 | 0.4566 |  |
| **Circulatory disease** | **-3.0618** | 1.5027 | ±3.0055 | **-2.037** | **0.0416** | * |
| GMI (%) | +0.5657 | 1.7507 | ±3.5014 | +0.323 | 0.7466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **593**, R² = **0.1461**, Adj R² = **0.1300**, F-statistic = **9.04** (p = **5.43e-15**), Residual SE = **11.532** on **581** df, AIC = **4594.7**, BIC = **4647.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6840** | 5.6141 | ±11.2281 | **+7.781** | **7.19e-15** | *** |
| Education: graduate level (vs college) | -1.5583 | 0.9667 | ±1.9333 | -1.612 | 0.1070 |  |
| Education: high school or below (vs college) | +3.0932 | 2.3552 | ±4.7103 | +1.313 | 0.1891 |  |
| Site: UCSD (vs UAB) | -0.4353 | 1.3287 | ±2.6573 | -0.328 | 0.7432 |  |
| Site: UW (vs UAB) | -1.0838 | 1.2324 | ±2.4649 | -0.879 | 0.3792 |  |
| **Age (years)** | **-0.3515** | 0.0456 | ±0.0912 | **-7.706** | **1.30e-14** | *** |
| BMI (kg/m2) | +0.0907 | 0.0868 | ±0.1737 | +1.045 | 0.2961 |  |
| Hypertension | +0.4545 | 1.1395 | ±2.2790 | +0.399 | 0.6900 |  |
| High cholesterol | -0.5063 | 0.9754 | ±1.9507 | -0.519 | 0.6037 |  |
| Kidney disease | -1.3645 | 1.8748 | ±3.7496 | -0.728 | 0.4667 |  |
| **Circulatory disease** | **-3.0421** | 1.4964 | ±2.9928 | **-2.033** | **0.0421** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0003 | 0.0370 | ±0.0740 | +0.008 | 0.9932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1486**, Adj R² = **0.1325**, F-statistic = **9.22** (p = **2.54e-15**), Residual SE = **11.516** on **581** df, AIC = **4593.0**, BIC = **4645.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.0011** | 4.5486 | ±9.0971 | **+9.014** | **1.99e-19** | *** |
| Education: graduate level (vs college) | -1.4712 | 0.9636 | ±1.9273 | -1.527 | 0.1268 |  |
| Education: high school or below (vs college) | +3.1099 | 2.3404 | ±4.6808 | +1.329 | 0.1839 |  |
| Site: UCSD (vs UAB) | -0.2866 | 1.3211 | ±2.6423 | -0.217 | 0.8282 |  |
| Site: UW (vs UAB) | -1.1552 | 1.2262 | ±2.4524 | -0.942 | 0.3461 |  |
| **Age (years)** | **-0.3579** | 0.0457 | ±0.0915 | **-7.826** | **5.05e-15** | *** |
| BMI (kg/m2) | +0.0869 | 0.0832 | ±0.1665 | +1.043 | 0.2968 |  |
| Hypertension | +0.3724 | 1.1371 | ±2.2741 | +0.328 | 0.7433 |  |
| High cholesterol | -0.5350 | 0.9708 | ±1.9416 | -0.551 | 0.5816 |  |
| Kidney disease | -1.4325 | 1.8778 | ±3.7555 | -0.763 | 0.4455 |  |
| **Circulatory disease** | **-3.0299** | 1.4921 | ±2.9841 | **-2.031** | **0.0423** | * |
| Glucose SD, pooled (mg/dL) | +0.1661 | 0.1274 | ±0.2547 | +1.304 | 0.1922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1481**, Adj R² = **0.1320**, F-statistic = **9.18** (p = **2.92e-15**), Residual SE = **11.519** on **581** df, AIC = **4593.3**, BIC = **4645.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.4922** | 4.5186 | ±9.0372 | **+9.182** | **4.21e-20** | *** |
| Education: graduate level (vs college) | -1.4992 | 0.9652 | ±1.9304 | -1.553 | 0.1204 |  |
| Education: high school or below (vs college) | +3.0989 | 2.3430 | ±4.6861 | +1.323 | 0.1860 |  |
| Site: UCSD (vs UAB) | -0.2818 | 1.3196 | ±2.6392 | -0.214 | 0.8309 |  |
| Site: UW (vs UAB) | -1.1460 | 1.2283 | ±2.4565 | -0.933 | 0.3508 |  |
| **Age (years)** | **-0.3575** | 0.0457 | ±0.0914 | **-7.820** | **5.29e-15** | *** |
| BMI (kg/m2) | +0.0863 | 0.0831 | ±0.1662 | +1.038 | 0.2992 |  |
| Hypertension | +0.3929 | 1.1392 | ±2.2784 | +0.345 | 0.7302 |  |
| High cholesterol | -0.5285 | 0.9712 | ±1.9425 | -0.544 | 0.5863 |  |
| Kidney disease | -1.4329 | 1.8728 | ±3.7457 | -0.765 | 0.4442 |  |
| **Circulatory disease** | **-3.0364** | 1.4926 | ±2.9851 | **-2.034** | **0.0419** | * |
| Avg. daily SD (mg/dL) | +0.1528 | 0.1310 | ±0.2619 | +1.167 | 0.2432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **593**, R² = **0.1477**, Adj R² = **0.1315**, F-statistic = **9.15** (p = **3.36e-15**), Residual SE = **11.522** on **581** df, AIC = **4593.6**, BIC = **4646.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.0011** | 4.7690 | ±9.5380 | **+8.597** | **8.15e-18** | *** |
| Education: graduate level (vs college) | -1.4536 | 0.9625 | ±1.9249 | -1.510 | 0.1310 |  |
| Education: high school or below (vs college) | +3.1146 | 2.3459 | ±4.6918 | +1.328 | 0.1843 |  |
| Site: UCSD (vs UAB) | -0.3462 | 1.3263 | ±2.6527 | -0.261 | 0.7941 |  |
| Site: UW (vs UAB) | -1.1094 | 1.2276 | ±2.4552 | -0.904 | 0.3662 |  |
| **Age (years)** | **-0.3556** | 0.0459 | ±0.0917 | **-7.754** | **8.90e-15** | *** |
| BMI (kg/m2) | +0.0922 | 0.0838 | ±0.1675 | +1.100 | 0.2712 |  |
| Hypertension | +0.4058 | 1.1377 | ±2.2755 | +0.357 | 0.7213 |  |
| High cholesterol | -0.5101 | 0.9718 | ±1.9436 | -0.525 | 0.5997 |  |
| Kidney disease | -1.3807 | 1.8834 | ±3.7669 | -0.733 | 0.4635 |  |
| **Circulatory disease** | **-2.9942** | 1.4875 | ±2.9750 | **-2.013** | **0.0441** | * |
| CV (%) | +0.1774 | 0.1694 | ±0.3388 | +1.047 | 0.2949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **593**, R² = **0.1475**, Adj R² = **0.1314**, F-statistic = **9.14** (p = **3.52e-15**), Residual SE = **11.523** on **581** df, AIC = **4593.7**, BIC = **4646.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5024** | 5.1409 | ±10.2818 | **+9.046** | **1.49e-19** | *** |
| Education: graduate level (vs college) | -1.4544 | 0.9621 | ±1.9243 | -1.512 | 0.1306 |  |
| Education: high school or below (vs college) | +3.1035 | 2.3445 | ±4.6890 | +1.324 | 0.1856 |  |
| Site: UCSD (vs UAB) | -0.3590 | 1.3253 | ±2.6506 | -0.271 | 0.7865 |  |
| Site: UW (vs UAB) | -1.1171 | 1.2270 | ±2.4541 | -0.910 | 0.3626 |  |
| **Age (years)** | **-0.3551** | 0.0459 | ±0.0917 | **-7.743** | **9.75e-15** | *** |
| BMI (kg/m2) | +0.0920 | 0.0838 | ±0.1677 | +1.098 | 0.2724 |  |
| Hypertension | +0.4097 | 1.1368 | ±2.2736 | +0.360 | 0.7186 |  |
| High cholesterol | -0.5064 | 0.9721 | ±1.9442 | -0.521 | 0.6024 |  |
| Kidney disease | -1.3825 | 1.8815 | ±3.7630 | -0.735 | 0.4625 |  |
| **Circulatory disease** | **-2.9920** | 1.4888 | ±2.9775 | **-2.010** | **0.0445** | * |
| Mean / SD ratio | -0.4172 | 0.4259 | ±0.8517 | -0.980 | 0.3272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1472**, Adj R² = **0.1310**, F-statistic = **9.12** (p = **3.90e-15**), Residual SE = **11.525** on **581** df, AIC = **4594.0**, BIC = **4646.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.0591** | 5.0506 | ±10.1012 | **+9.120** | **7.54e-20** | *** |
| Education: graduate level (vs college) | -1.4855 | 0.9646 | ±1.9292 | -1.540 | 0.1235 |  |
| Education: high school or below (vs college) | +3.0910 | 2.3466 | ±4.6933 | +1.317 | 0.1878 |  |
| Site: UCSD (vs UAB) | -0.3530 | 1.3229 | ±2.6457 | -0.267 | 0.7896 |  |
| Site: UW (vs UAB) | -1.1170 | 1.2288 | ±2.4576 | -0.909 | 0.3633 |  |
| **Age (years)** | **-0.3550** | 0.0459 | ±0.0919 | **-7.729** | **1.08e-14** | *** |
| BMI (kg/m2) | +0.0902 | 0.0838 | ±0.1675 | +1.077 | 0.2816 |  |
| Hypertension | +0.4399 | 1.1397 | ±2.2794 | +0.386 | 0.6995 |  |
| High cholesterol | -0.5048 | 0.9723 | ±1.9447 | -0.519 | 0.6036 |  |
| Kidney disease | -1.3885 | 1.8766 | ±3.7532 | -0.740 | 0.4593 |  |
| **Circulatory disease** | **-3.0026** | 1.4881 | ±2.9762 | **-2.018** | **0.0436** | * |
| Avg. daily mean/SD | -0.2992 | 0.3497 | ±0.6993 | -0.856 | 0.3922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **593**, R² = **0.1758**, Adj R² = **0.1602**, F-statistic = **11.27** (p = **4.22e-19**), Residual SE = **11.330** on **581** df, AIC = **4573.7**, BIC = **4626.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.0089** | 4.4636 | ±8.9272 | **+7.171** | **7.44e-13** | *** |
| Education: graduate level (vs college) | -1.4718 | 0.9443 | ±1.8886 | -1.559 | 0.1191 |  |
| Education: high school or below (vs college) | +2.4682 | 2.3244 | ±4.6487 | +1.062 | 0.2883 |  |
| Site: UCSD (vs UAB) | -0.1958 | 1.2995 | ±2.5989 | -0.151 | 0.8802 |  |
| Site: UW (vs UAB) | -1.0137 | 1.2034 | ±2.4068 | -0.842 | 0.3996 |  |
| **Age (years)** | **-0.3516** | 0.0448 | ±0.0897 | **-7.842** | **4.44e-15** | *** |
| BMI (kg/m2) | +0.0920 | 0.0787 | ±0.1574 | +1.169 | 0.2424 |  |
| Hypertension | +0.7400 | 1.1237 | ±2.2474 | +0.659 | 0.5102 |  |
| High cholesterol | -0.4996 | 0.9520 | ±1.9039 | -0.525 | 0.5997 |  |
| Kidney disease | -1.7868 | 1.8738 | ±3.7477 | -0.954 | 0.3403 |  |
| Circulatory disease | -2.6354 | 1.4796 | ±2.9593 | -1.781 | 0.0749 | . |
| **MAG (mg/dL/h)** | **+0.3204** | 0.0757 | ±0.1514 | **+4.232** | **2.31e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **593**, R² = **0.1524**, Adj R² = **0.1363**, F-statistic = **9.49** (p = **7.77e-16**), Residual SE = **11.490** on **581** df, AIC = **4590.4**, BIC = **4643.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.5776** | 4.8435 | ±9.6871 | **+7.965** | **1.66e-15** | *** |
| Education: graduate level (vs college) | -1.5167 | 0.9637 | ±1.9274 | -1.574 | 0.1155 |  |
| Education: high school or below (vs college) | +2.9882 | 2.3426 | ±4.6852 | +1.276 | 0.2021 |  |
| Site: UCSD (vs UAB) | -0.2695 | 1.3143 | ±2.6287 | -0.205 | 0.8375 |  |
| Site: UW (vs UAB) | -1.1955 | 1.2261 | ±2.4522 | -0.975 | 0.3295 |  |
| **Age (years)** | **-0.3602** | 0.0455 | ±0.0910 | **-7.918** | **2.41e-15** | *** |
| BMI (kg/m2) | +0.0970 | 0.0839 | ±0.1678 | +1.156 | 0.2476 |  |
| Hypertension | +0.4267 | 1.1402 | ±2.2804 | +0.374 | 0.7082 |  |
| High cholesterol | -0.4998 | 0.9683 | ±1.9366 | -0.516 | 0.6057 |  |
| Kidney disease | -1.5133 | 1.8597 | ±3.7194 | -0.814 | 0.4158 |  |
| **Circulatory disease** | **-3.0582** | 1.4872 | ±2.9744 | **-2.056** | **0.0398** | * |
| **Avg. daily range (mg/dL)** | **+0.0615** | 0.0304 | ±0.0608 | **+2.023** | **0.0431** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **593**, R² = **0.1533**, Adj R² = **0.1372**, F-statistic = **9.56** (p = **5.83e-16**), Residual SE = **11.484** on **581** df, AIC = **4589.7**, BIC = **4642.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.4404** | 4.0741 | ±8.1482 | **+10.172** | **2.65e-24** | *** |
| Education: graduate level (vs college) | -1.5445 | 0.9602 | ±1.9203 | -1.609 | 0.1077 |  |
| Education: high school or below (vs college) | +3.1332 | 2.3170 | ±4.6340 | +1.352 | 0.1763 |  |
| Site: UCSD (vs UAB) | -0.3466 | 1.3215 | ±2.6431 | -0.262 | 0.7931 |  |
| Site: UW (vs UAB) | -1.1155 | 1.2189 | ±2.4378 | -0.915 | 0.3601 |  |
| **Age (years)** | **-0.3507** | 0.0454 | ±0.0908 | **-7.724** | **1.13e-14** | *** |
| BMI (kg/m2) | +0.0733 | 0.0834 | ±0.1668 | +0.879 | 0.3794 |  |
| Hypertension | +0.4527 | 1.1287 | ±2.2575 | +0.401 | 0.6884 |  |
| High cholesterol | -0.6407 | 0.9669 | ±1.9338 | -0.663 | 0.5076 |  |
| Kidney disease | -1.3240 | 1.8573 | ±3.7145 | -0.713 | 0.4759 |  |
| **Circulatory disease** | **-3.0380** | 1.4915 | ±2.9831 | **-2.037** | **0.0417** | * |
| **SD of daily means (mg/dL)** | **+0.4762** | 0.2245 | ±0.4490 | **+2.121** | **0.0339** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **593**, R² = **0.1464**, Adj R² = **0.1303**, F-statistic = **9.06** (p = **4.93e-15**), Residual SE = **11.530** on **581** df, AIC = **4594.5**, BIC = **4647.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7413** | 15.9517 | ±31.9034 | **+3.244** | **0.0012** | ** |
| Education: graduate level (vs college) | -1.5550 | 0.9666 | ±1.9331 | -1.609 | 0.1077 |  |
| Education: high school or below (vs college) | +3.1126 | 2.3520 | ±4.7040 | +1.323 | 0.1857 |  |
| Site: UCSD (vs UAB) | -0.3937 | 1.3309 | ±2.6618 | -0.296 | 0.7674 |  |
| Site: UW (vs UAB) | -1.1025 | 1.2296 | ±2.4592 | -0.897 | 0.3699 |  |
| **Age (years)** | **-0.3531** | 0.0453 | ±0.0906 | **-7.792** | **6.58e-15** | *** |
| BMI (kg/m2) | +0.0894 | 0.0838 | ±0.1677 | +1.066 | 0.2862 |  |
| Hypertension | +0.4557 | 1.1407 | ±2.2815 | +0.400 | 0.6895 |  |
| High cholesterol | -0.5360 | 0.9730 | ±1.9460 | -0.551 | 0.5817 |  |
| Kidney disease | -1.3871 | 1.8667 | ±3.7334 | -0.743 | 0.4574 |  |
| **Circulatory disease** | **-3.0811** | 1.5027 | ±3.0054 | **-2.050** | **0.0403** | * |
| Time in range 70-180, pooled (%) | -0.0803 | 0.1569 | ±0.3138 | -0.512 | 0.6087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **593**, R² = **0.1467**, Adj R² = **0.1305**, F-statistic = **9.08** (p = **4.59e-15**), Residual SE = **11.529** on **581** df, AIC = **4594.3**, BIC = **4646.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6006** | 16.6998 | ±33.3996 | **+3.270** | **0.0011** | ** |
| Education: graduate level (vs college) | -1.5551 | 0.9662 | ±1.9324 | -1.609 | 0.1075 |  |
| Education: high school or below (vs college) | +3.1257 | 2.3518 | ±4.7035 | +1.329 | 0.1838 |  |
| Site: UCSD (vs UAB) | -0.3760 | 1.3309 | ±2.6618 | -0.283 | 0.7776 |  |
| Site: UW (vs UAB) | -1.1041 | 1.2294 | ±2.4587 | -0.898 | 0.3691 |  |
| **Age (years)** | **-0.3535** | 0.0453 | ±0.0907 | **-7.798** | **6.29e-15** | *** |
| BMI (kg/m2) | +0.0884 | 0.0837 | ±0.1674 | +1.056 | 0.2912 |  |
| Hypertension | +0.4593 | 1.1408 | ±2.2816 | +0.403 | 0.6873 |  |
| High cholesterol | -0.5470 | 0.9727 | ±1.9454 | -0.562 | 0.5739 |  |
| Kidney disease | -1.3968 | 1.8624 | ±3.7248 | -0.750 | 0.4533 |  |
| **Circulatory disease** | **-3.1008** | 1.5049 | ±3.0098 | **-2.060** | **0.0394** | * |
| Avg. daily time in range 70-180 (%) | -0.1088 | 0.1644 | ±0.3287 | -0.662 | 0.5080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **593**, R² = **0.1469**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.26e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.2**, BIC = **4646.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9517** | 4.1482 | ±8.2965 | **+10.595** | **3.13e-26** | *** |
| Education: graduate level (vs college) | -1.6422 | 0.9786 | ±1.9571 | -1.678 | 0.0933 | . |
| Education: high school or below (vs college) | +3.0004 | 2.3498 | ±4.6997 | +1.277 | 0.2017 |  |
| Site: UCSD (vs UAB) | -0.3904 | 1.3296 | ±2.6593 | -0.294 | 0.7690 |  |
| Site: UW (vs UAB) | -1.0938 | 1.2294 | ±2.4588 | -0.890 | 0.3737 |  |
| **Age (years)** | **-0.3520** | 0.0455 | ±0.0911 | **-7.729** | **1.09e-14** | *** |
| BMI (kg/m2) | +0.0899 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4592 | 1.1396 | ±2.2791 | +0.403 | 0.6870 |  |
| High cholesterol | -0.4962 | 0.9710 | ±1.9420 | -0.511 | 0.6093 |  |
| Kidney disease | -1.3959 | 1.8725 | ±3.7450 | -0.745 | 0.4560 |  |
| **Circulatory disease** | **-3.0720** | 1.4917 | ±2.9833 | **-2.059** | **0.0395** | * |
| Time 54-69, pooled (%) | -0.6485 | 0.8699 | ±1.7399 | -0.745 | 0.4560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1309**, F-statistic = **9.10** (p = **4.13e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9337** | 4.1444 | ±8.2887 | **+10.601** | **2.95e-26** | *** |
| Education: graduate level (vs college) | -1.6514 | 0.9783 | ±1.9567 | -1.688 | 0.0914 | . |
| Education: high school or below (vs college) | +2.9863 | 2.3521 | ±4.7043 | +1.270 | 0.2042 |  |
| Site: UCSD (vs UAB) | -0.3727 | 1.3304 | ±2.6608 | -0.280 | 0.7794 |  |
| Site: UW (vs UAB) | -1.0904 | 1.2296 | ±2.4592 | -0.887 | 0.3752 |  |
| **Age (years)** | **-0.3518** | 0.0455 | ±0.0911 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | +0.0900 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4552 | 1.1397 | ±2.2794 | +0.399 | 0.6896 |  |
| High cholesterol | -0.4990 | 0.9712 | ±1.9424 | -0.514 | 0.6074 |  |
| Kidney disease | -1.3970 | 1.8716 | ±3.7432 | -0.746 | 0.4554 |  |
| **Circulatory disease** | **-3.0850** | 1.4942 | ±2.9884 | **-2.065** | **0.0390** | * |
| Avg. daily time 54-69 (%) | -0.6693 | 0.8640 | ±1.7280 | -0.775 | 0.4385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **593**, R² = **0.1469**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.26e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.2**, BIC = **4646.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9517** | 4.1482 | ±8.2965 | **+10.595** | **3.13e-26** | *** |
| Education: graduate level (vs college) | -1.6422 | 0.9786 | ±1.9571 | -1.678 | 0.0933 | . |
| Education: high school or below (vs college) | +3.0004 | 2.3498 | ±4.6997 | +1.277 | 0.2017 |  |
| Site: UCSD (vs UAB) | -0.3904 | 1.3296 | ±2.6593 | -0.294 | 0.7690 |  |
| Site: UW (vs UAB) | -1.0938 | 1.2294 | ±2.4588 | -0.890 | 0.3737 |  |
| **Age (years)** | **-0.3520** | 0.0455 | ±0.0911 | **-7.729** | **1.09e-14** | *** |
| BMI (kg/m2) | +0.0899 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4592 | 1.1396 | ±2.2791 | +0.403 | 0.6870 |  |
| High cholesterol | -0.4962 | 0.9710 | ±1.9420 | -0.511 | 0.6093 |  |
| Kidney disease | -1.3959 | 1.8725 | ±3.7450 | -0.745 | 0.4560 |  |
| **Circulatory disease** | **-3.0720** | 1.4917 | ±2.9833 | **-2.059** | **0.0395** | * |
| Time < 70 (%) | -0.6485 | 0.8699 | ±1.7399 | -0.745 | 0.4560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1309**, F-statistic = **9.10** (p = **4.13e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9337** | 4.1444 | ±8.2887 | **+10.601** | **2.95e-26** | *** |
| Education: graduate level (vs college) | -1.6514 | 0.9783 | ±1.9567 | -1.688 | 0.0914 | . |
| Education: high school or below (vs college) | +2.9863 | 2.3521 | ±4.7043 | +1.270 | 0.2042 |  |
| Site: UCSD (vs UAB) | -0.3727 | 1.3304 | ±2.6608 | -0.280 | 0.7794 |  |
| Site: UW (vs UAB) | -1.0904 | 1.2296 | ±2.4592 | -0.887 | 0.3752 |  |
| **Age (years)** | **-0.3518** | 0.0455 | ±0.0911 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | +0.0900 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4552 | 1.1397 | ±2.2794 | +0.399 | 0.6896 |  |
| High cholesterol | -0.4990 | 0.9712 | ±1.9424 | -0.514 | 0.6074 |  |
| Kidney disease | -1.3970 | 1.8716 | ±3.7432 | -0.746 | 0.4554 |  |
| **Circulatory disease** | **-3.0850** | 1.4942 | ±2.9884 | **-2.065** | **0.0390** | * |
| Avg. daily time < 70 (%) | -0.6693 | 0.8640 | ±1.7280 | -0.775 | 0.4385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **593**, R² = **0.1467**, Adj R² = **0.1305**, F-statistic = **9.08** (p = **4.60e-15**), Residual SE = **11.529** on **581** df, AIC = **4594.3**, BIC = **4647.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7427** | 4.1239 | ±8.2478 | **+10.607** | **2.76e-26** | *** |
| Education: graduate level (vs college) | -1.5675 | 0.9652 | ±1.9304 | -1.624 | 0.1044 |  |
| Education: high school or below (vs college) | +3.1033 | 2.3504 | ±4.7009 | +1.320 | 0.1867 |  |
| Site: UCSD (vs UAB) | -0.3740 | 1.3304 | ±2.6607 | -0.281 | 0.7786 |  |
| Site: UW (vs UAB) | -1.1100 | 1.2294 | ±2.4588 | -0.903 | 0.3666 |  |
| **Age (years)** | **-0.3536** | 0.0453 | ±0.0906 | **-7.806** | **5.91e-15** | *** |
| BMI (kg/m2) | +0.0888 | 0.0838 | ±0.1675 | +1.060 | 0.2889 |  |
| Hypertension | +0.4568 | 1.1408 | ±2.2815 | +0.400 | 0.6889 |  |
| High cholesterol | -0.5435 | 0.9732 | ±1.9464 | -0.558 | 0.5766 |  |
| Kidney disease | -1.3989 | 1.8644 | ±3.7287 | -0.750 | 0.4530 |  |
| **Circulatory disease** | **-3.0975** | 1.5043 | ±3.0087 | **-2.059** | **0.0395** | * |
| Time 181-250, pooled (%) | +0.1041 | 0.1562 | ±0.3124 | +0.667 | 0.5051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.16e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7649** | 4.1168 | ±8.2336 | **+10.631** | **2.14e-26** | *** |
| Education: graduate level (vs college) | -1.5733 | 0.9649 | ±1.9298 | -1.630 | 0.1030 |  |
| Education: high school or below (vs college) | +3.1120 | 2.3490 | ±4.6980 | +1.325 | 0.1852 |  |
| Site: UCSD (vs UAB) | -0.3481 | 1.3304 | ±2.6609 | -0.262 | 0.7936 |  |
| Site: UW (vs UAB) | -1.1109 | 1.2292 | ±2.4584 | -0.904 | 0.3661 |  |
| **Age (years)** | **-0.3540** | 0.0453 | ±0.0906 | **-7.812** | **5.61e-15** | *** |
| BMI (kg/m2) | +0.0876 | 0.0836 | ±0.1672 | +1.047 | 0.2950 |  |
| Hypertension | +0.4605 | 1.1407 | ±2.2815 | +0.404 | 0.6865 |  |
| High cholesterol | -0.5561 | 0.9728 | ±1.9456 | -0.572 | 0.5676 |  |
| Kidney disease | -1.4117 | 1.8590 | ±3.7180 | -0.759 | 0.4476 |  |
| **Circulatory disease** | **-3.1245** | 1.5077 | ±3.0153 | **-2.072** | **0.0382** | * |
| Avg. daily time 181-250 (%) | +0.1363 | 0.1636 | ±0.3272 | +0.833 | 0.4047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **593**, R² = **0.1467**, Adj R² = **0.1305**, F-statistic = **9.08** (p = **4.60e-15**), Residual SE = **11.529** on **581** df, AIC = **4594.3**, BIC = **4647.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7427** | 4.1239 | ±8.2478 | **+10.607** | **2.76e-26** | *** |
| Education: graduate level (vs college) | -1.5675 | 0.9652 | ±1.9304 | -1.624 | 0.1044 |  |
| Education: high school or below (vs college) | +3.1033 | 2.3504 | ±4.7009 | +1.320 | 0.1867 |  |
| Site: UCSD (vs UAB) | -0.3740 | 1.3304 | ±2.6607 | -0.281 | 0.7786 |  |
| Site: UW (vs UAB) | -1.1100 | 1.2294 | ±2.4588 | -0.903 | 0.3666 |  |
| **Age (years)** | **-0.3536** | 0.0453 | ±0.0906 | **-7.806** | **5.91e-15** | *** |
| BMI (kg/m2) | +0.0888 | 0.0838 | ±0.1675 | +1.060 | 0.2889 |  |
| Hypertension | +0.4568 | 1.1408 | ±2.2815 | +0.400 | 0.6889 |  |
| High cholesterol | -0.5435 | 0.9732 | ±1.9464 | -0.558 | 0.5766 |  |
| Kidney disease | -1.3989 | 1.8644 | ±3.7287 | -0.750 | 0.4530 |  |
| **Circulatory disease** | **-3.0975** | 1.5043 | ±3.0087 | **-2.059** | **0.0395** | * |
| Time > 180 (%) | +0.1041 | 0.1562 | ±0.3124 | +0.667 | 0.5051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.16e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7649** | 4.1168 | ±8.2336 | **+10.631** | **2.14e-26** | *** |
| Education: graduate level (vs college) | -1.5733 | 0.9649 | ±1.9298 | -1.630 | 0.1030 |  |
| Education: high school or below (vs college) | +3.1120 | 2.3490 | ±4.6980 | +1.325 | 0.1852 |  |
| Site: UCSD (vs UAB) | -0.3481 | 1.3304 | ±2.6609 | -0.262 | 0.7936 |  |
| Site: UW (vs UAB) | -1.1109 | 1.2292 | ±2.4584 | -0.904 | 0.3661 |  |
| **Age (years)** | **-0.3540** | 0.0453 | ±0.0906 | **-7.812** | **5.61e-15** | *** |
| BMI (kg/m2) | +0.0876 | 0.0836 | ±0.1672 | +1.047 | 0.2950 |  |
| Hypertension | +0.4605 | 1.1407 | ±2.2815 | +0.404 | 0.6865 |  |
| High cholesterol | -0.5561 | 0.9728 | ±1.9456 | -0.572 | 0.5676 |  |
| Kidney disease | -1.4117 | 1.8590 | ±3.7180 | -0.759 | 0.4476 |  |
| **Circulatory disease** | **-3.1245** | 1.5077 | ±3.0153 | **-2.072** | **0.0382** | * |
| Avg. daily time > 180 (%) | +0.1363 | 0.1636 | ±0.3272 | +0.833 | 0.4047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1463**, Adj R² = **0.1301**, F-statistic = **9.05** (p = **5.21e-15**), Residual SE = **11.532** on **581** df, AIC = **4594.6**, BIC = **4647.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7077** | 4.1456 | ±8.2912 | **+10.543** | **5.46e-26** | *** |
| Education: graduate level (vs college) | -1.5621 | 0.9667 | ±1.9334 | -1.616 | 0.1061 |  |
| Education: high school or below (vs college) | +3.1144 | 2.3587 | ±4.7174 | +1.320 | 0.1867 |  |
| Site: UCSD (vs UAB) | -0.4553 | 1.3289 | ±2.6577 | -0.343 | 0.7319 |  |
| Site: UW (vs UAB) | -1.0709 | 1.2308 | ±2.4615 | -0.870 | 0.3842 |  |
| **Age (years)** | **-0.3520** | 0.0456 | ±0.0911 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | +0.0932 | 0.0850 | ±0.1699 | +1.097 | 0.2726 |  |
| Hypertension | +0.4438 | 1.1429 | ±2.2859 | +0.388 | 0.6978 |  |
| High cholesterol | -0.4700 | 0.9777 | ±1.9555 | -0.481 | 0.6307 |  |
| Kidney disease | -1.3669 | 1.8773 | ±3.7547 | -0.728 | 0.4666 |  |
| **Circulatory disease** | **-3.0383** | 1.4910 | ±2.9820 | **-2.038** | **0.0416** | * |
| Nocturnal time > 180 (%) | -0.0454 | 0.1410 | ±0.2821 | -0.322 | 0.7474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 597; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **597**, R² = **0.1491**, Adj R² = **0.1345**, F-statistic = **10.26** (p = **4.91e-16**), Residual SE = **7.427** on **586** df, AIC = **4099.2**, BIC = **4147.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3247** | 3.3385 | ±6.6770 | **+17.770** | **1.21e-70** | *** |
| **Education: graduate level (vs college)** | **-1.7318** | 0.6709 | ±1.3418 | **-2.581** | **0.0098** | ** |
| Education: high school or below (vs college) | -1.1250 | 1.1380 | ±2.2760 | -0.989 | 0.3229 |  |
| Site: UCSD (vs UAB) | -1.5464 | 0.8355 | ±1.6710 | -1.851 | 0.0642 | . |
| **Site: UW (vs UAB)** | **-1.7085** | 0.7873 | ±1.5747 | **-2.170** | **0.0300** | * |
| **Age (years)** | **-0.1047** | 0.0310 | ±0.0620 | **-3.375** | **7.39e-04** | *** |
| **BMI (kg/m2)** | **+0.3104** | 0.0681 | ±0.1362 | **+4.559** | **5.13e-06** | *** |
| Hypertension | +0.7130 | 0.7483 | ±1.4967 | +0.953 | 0.3407 |  |
| High cholesterol | -0.7516 | 0.6361 | ±1.2723 | -1.182 | 0.2374 |  |
| Kidney disease | +0.7480 | 1.2321 | ±2.4642 | +0.607 | 0.5438 |  |
| Circulatory disease | -0.4494 | 0.9357 | ±1.8714 | -0.480 | 0.6310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **597**, R² = **0.1562**, Adj R² = **0.1403**, F-statistic = **9.84** (p = **1.72e-16**), Residual SE = **7.402** on **585** df, AIC = **4096.2**, BIC = **4148.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7437** | 5.3637 | ±10.7275 | **+9.088** | **1.01e-19** | *** |
| **Education: graduate level (vs college)** | **-1.7530** | 0.6644 | ±1.3289 | **-2.638** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.1086 | 1.1457 | ±2.2914 | -0.968 | 0.3332 |  |
| Site: UCSD (vs UAB) | -1.5159 | 0.8245 | ±1.6490 | -1.839 | 0.0660 | . |
| **Site: UW (vs UAB)** | **-1.7166** | 0.7823 | ±1.5645 | **-2.194** | **0.0282** | * |
| **Age (years)** | **-0.1129** | 0.0314 | ±0.0627 | **-3.600** | **3.18e-04** | *** |
| **BMI (kg/m2)** | **+0.2949** | 0.0664 | ±0.1328 | **+4.440** | **8.99e-06** | *** |
| Hypertension | +0.6001 | 0.7490 | ±1.4980 | +0.801 | 0.4230 |  |
| High cholesterol | -0.9383 | 0.6282 | ±1.2564 | -1.494 | 0.1353 |  |
| Kidney disease | +0.7623 | 1.1958 | ±2.3917 | +0.637 | 0.5238 |  |
| Circulatory disease | -0.4145 | 0.9214 | ±1.8428 | -0.450 | 0.6528 |  |
| **HbA1c (%)** | **+2.0870** | 0.9855 | ±1.9711 | **+2.118** | **0.0342** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **597**, R² = **0.1595**, Adj R² = **0.1437**, F-statistic = **10.09** (p = **5.91e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.8**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2431** | 4.0523 | ±8.1046 | **+12.645** | **1.19e-36** | *** |
| **Education: graduate level (vs college)** | **-1.7918** | 0.6673 | ±1.3346 | **-2.685** | **0.0073** | ** |
| Education: high school or below (vs college) | -1.1240 | 1.1155 | ±2.2310 | -1.008 | 0.3137 |  |
| Site: UCSD (vs UAB) | -1.4097 | 0.8242 | ±1.6484 | -1.710 | 0.0872 | . |
| **Site: UW (vs UAB)** | **-1.8287** | 0.7809 | ±1.5617 | **-2.342** | **0.0192** | * |
| **Age (years)** | **-0.1087** | 0.0307 | ±0.0614 | **-3.538** | **4.03e-04** | *** |
| **BMI (kg/m2)** | **+0.2955** | 0.0665 | ±0.1330 | **+4.445** | **8.80e-06** | *** |
| Hypertension | +0.6009 | 0.7466 | ±1.4933 | +0.805 | 0.4209 |  |
| High cholesterol | -0.7904 | 0.6341 | ±1.2682 | -1.246 | 0.2126 |  |
| Kidney disease | +0.5959 | 1.2256 | ±2.4513 | +0.486 | 0.6268 |  |
| Circulatory disease | -0.5664 | 0.9291 | ±1.8583 | -0.610 | 0.5421 |  |
| **Mean glucose (mg/dL)** | **+0.0745** | 0.0254 | ±0.0508 | **+2.934** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **597**, R² = **0.1595**, Adj R² = **0.1437**, F-statistic = **10.09** (p = **5.91e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.8**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9339** | 6.7861 | ±13.5721 | **+6.032** | **1.62e-09** | *** |
| **Education: graduate level (vs college)** | **-1.7918** | 0.6673 | ±1.3346 | **-2.685** | **0.0073** | ** |
| Education: high school or below (vs college) | -1.1240 | 1.1155 | ±2.2310 | -1.008 | 0.3137 |  |
| Site: UCSD (vs UAB) | -1.4097 | 0.8242 | ±1.6484 | -1.710 | 0.0872 | . |
| **Site: UW (vs UAB)** | **-1.8287** | 0.7809 | ±1.5617 | **-2.342** | **0.0192** | * |
| **Age (years)** | **-0.1087** | 0.0307 | ±0.0614 | **-3.538** | **4.03e-04** | *** |
| **BMI (kg/m2)** | **+0.2955** | 0.0665 | ±0.1330 | **+4.445** | **8.80e-06** | *** |
| Hypertension | +0.6009 | 0.7466 | ±1.4933 | +0.805 | 0.4209 |  |
| High cholesterol | -0.7904 | 0.6341 | ±1.2682 | -1.246 | 0.2126 |  |
| Kidney disease | +0.5959 | 1.2256 | ±2.4513 | +0.486 | 0.6268 |  |
| Circulatory disease | -0.5664 | 0.9291 | ±1.8583 | -0.610 | 0.5421 |  |
| **GMI (%)** | **+3.1146** | 1.0615 | ±2.1230 | **+2.934** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **597**, R² = **0.1629**, Adj R² = **0.1472**, F-statistic = **10.35** (p = **1.98e-17**), Residual SE = **7.372** on **585** df, AIC = **4091.4**, BIC = **4144.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2844** | 3.5806 | ±7.1612 | **+14.323** | **1.57e-46** | *** |
| **Education: graduate level (vs college)** | **-1.7586** | 0.6631 | ±1.3261 | **-2.652** | **0.0080** | ** |
| Education: high school or below (vs college) | -1.1810 | 1.1170 | ±2.2340 | -1.057 | 0.2904 |  |
| Site: UCSD (vs UAB) | -1.5122 | 0.8248 | ±1.6496 | -1.833 | 0.0667 | . |
| **Site: UW (vs UAB)** | **-1.8720** | 0.7789 | ±1.5578 | **-2.403** | **0.0162** | * |
| **Age (years)** | **-0.1010** | 0.0305 | ±0.0610 | **-3.312** | **9.27e-04** | *** |
| **BMI (kg/m2)** | **+0.2782** | 0.0651 | ±0.1301 | **+4.276** | **1.90e-05** | *** |
| Hypertension | +0.6371 | 0.7429 | ±1.4858 | +0.858 | 0.3911 |  |
| High cholesterol | -0.8721 | 0.6329 | ±1.2658 | -1.378 | 0.1682 |  |
| Kidney disease | +0.6744 | 1.2073 | ±2.4146 | +0.559 | 0.5764 |  |
| Circulatory disease | -0.5266 | 0.9248 | ±1.8496 | -0.569 | 0.5691 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0750** | 0.0223 | ±0.0445 | **+3.368** | **7.58e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **597**, R² = **0.1538**, Adj R² = **0.1379**, F-statistic = **9.66** (p = **3.66e-16**), Residual SE = **7.412** on **585** df, AIC = **4097.9**, BIC = **4150.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9026** | 3.3928 | ±6.7856 | **+16.772** | **3.93e-63** | *** |
| **Education: graduate level (vs college)** | **-1.6506** | 0.6671 | ±1.3343 | **-2.474** | **0.0134** | * |
| Education: high school or below (vs college) | -1.1108 | 1.1299 | ±2.2597 | -0.983 | 0.3256 |  |
| Site: UCSD (vs UAB) | -1.4250 | 0.8304 | ±1.6608 | -1.716 | 0.0862 | . |
| **Site: UW (vs UAB)** | **-1.7819** | 0.7860 | ±1.5719 | **-2.267** | **0.0234** | * |
| **Age (years)** | **-0.1101** | 0.0316 | ±0.0633 | **-3.482** | **4.98e-04** | *** |
| **BMI (kg/m2)** | **+0.3065** | 0.0669 | ±0.1339 | **+4.579** | **4.67e-06** | *** |
| Hypertension | +0.6297 | 0.7477 | ±1.4953 | +0.842 | 0.3997 |  |
| High cholesterol | -0.7699 | 0.6356 | ±1.2711 | -1.211 | 0.2258 |  |
| Kidney disease | +0.6850 | 1.2377 | ±2.4755 | +0.553 | 0.5800 |  |
| Circulatory disease | -0.4345 | 0.9247 | ±1.8494 | -0.470 | 0.6384 |  |
| Glucose SD, pooled (mg/dL) | +0.1485 | 0.0876 | ±0.1752 | +1.695 | 0.0901 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **597**, R² = **0.1540**, Adj R² = **0.1381**, F-statistic = **9.68** (p = **3.40e-16**), Residual SE = **7.411** on **585** df, AIC = **4097.7**, BIC = **4150.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.0770** | 3.3594 | ±6.7188 | **+16.990** | **9.69e-65** | *** |
| **Education: graduate level (vs college)** | **-1.6678** | 0.6678 | ±1.3356 | **-2.497** | **0.0125** | * |
| Education: high school or below (vs college) | -1.1192 | 1.1289 | ±2.2578 | -0.991 | 0.3215 |  |
| Site: UCSD (vs UAB) | -1.4046 | 0.8278 | ±1.6555 | -1.697 | 0.0897 | . |
| **Site: UW (vs UAB)** | **-1.7823** | 0.7878 | ±1.5757 | **-2.262** | **0.0237** | * |
| **Age (years)** | **-0.1104** | 0.0316 | ±0.0631 | **-3.498** | **4.69e-04** | *** |
| **BMI (kg/m2)** | **+0.3053** | 0.0667 | ±0.1335 | **+4.574** | **4.78e-06** | *** |
| Hypertension | +0.6397 | 0.7514 | ±1.5029 | +0.851 | 0.3946 |  |
| High cholesterol | -0.7659 | 0.6355 | ±1.2709 | -1.205 | 0.2281 |  |
| Kidney disease | +0.6766 | 1.2378 | ±2.4757 | +0.547 | 0.5847 |  |
| Circulatory disease | -0.4394 | 0.9261 | ±1.8522 | -0.475 | 0.6351 |  |
| Avg. daily SD (mg/dL) | +0.1549 | 0.0898 | ±0.1796 | +1.725 | 0.0846 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **597**, R² = **0.1493**, Adj R² = **0.1333**, F-statistic = **9.33** (p = **1.50e-15**), Residual SE = **7.432** on **585** df, AIC = **4101.0**, BIC = **4153.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6069** | 3.6218 | ±7.2437 | **+16.182** | **6.80e-59** | *** |
| **Education: graduate level (vs college)** | **-1.7036** | 0.6729 | ±1.3458 | **-2.532** | **0.0114** | * |
| Education: high school or below (vs college) | -1.1200 | 1.1384 | ±2.2769 | -0.984 | 0.3252 |  |
| Site: UCSD (vs UAB) | -1.5250 | 0.8362 | ±1.6724 | -1.824 | 0.0682 | . |
| **Site: UW (vs UAB)** | **-1.7173** | 0.7889 | ±1.5777 | **-2.177** | **0.0295** | * |
| **Age (years)** | **-0.1057** | 0.0316 | ±0.0632 | **-3.344** | **8.25e-04** | *** |
| **BMI (kg/m2)** | **+0.3107** | 0.0680 | ±0.1360 | **+4.569** | **4.91e-06** | *** |
| Hypertension | +0.6984 | 0.7471 | ±1.4941 | +0.935 | 0.3499 |  |
| High cholesterol | -0.7509 | 0.6375 | ±1.2749 | -1.178 | 0.2388 |  |
| Kidney disease | +0.7430 | 1.2372 | ±2.4744 | +0.601 | 0.5482 |  |
| Circulatory disease | -0.4353 | 0.9358 | ±1.8716 | -0.465 | 0.6418 |  |
| CV (%) | +0.0470 | 0.1178 | ±0.2355 | +0.399 | 0.6901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **597**, R² = **0.1492**, Adj R² = **0.1332**, F-statistic = **9.32** (p = **1.57e-15**), Residual SE = **7.433** on **585** df, AIC = **4101.1**, BIC = **4153.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.8266** | 3.9176 | ±7.8353 | **+15.271** | **1.19e-52** | *** |
| **Education: graduate level (vs college)** | **-1.7123** | 0.6732 | ±1.3465 | **-2.543** | **0.0110** | * |
| Education: high school or below (vs college) | -1.1235 | 1.1385 | ±2.2769 | -0.987 | 0.3237 |  |
| Site: UCSD (vs UAB) | -1.5349 | 0.8364 | ±1.6728 | -1.835 | 0.0665 | . |
| **Site: UW (vs UAB)** | **-1.7167** | 0.7893 | ±1.5787 | **-2.175** | **0.0296** | * |
| **Age (years)** | **-0.1052** | 0.0314 | ±0.0628 | **-3.351** | **8.05e-04** | *** |
| **BMI (kg/m2)** | **+0.3106** | 0.0681 | ±0.1361 | **+4.564** | **5.03e-06** | *** |
| Hypertension | +0.7032 | 0.7470 | ±1.4940 | +0.941 | 0.3465 |  |
| High cholesterol | -0.7501 | 0.6377 | ±1.2753 | -1.176 | 0.2394 |  |
| Kidney disease | +0.7441 | 1.2372 | ±2.4744 | +0.601 | 0.5476 |  |
| Circulatory disease | -0.4398 | 0.9372 | ±1.8744 | -0.469 | 0.6388 |  |
| Mean / SD ratio | -0.0751 | 0.2663 | ±0.5327 | -0.282 | 0.7780 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **597**, R² = **0.1495**, Adj R² = **0.1335**, F-statistic = **9.35** (p = **1.42e-15**), Residual SE = **7.431** on **585** df, AIC = **4100.9**, BIC = **4153.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2754** | 3.8717 | ±7.7434 | **+15.568** | **1.20e-54** | *** |
| **Education: graduate level (vs college)** | **-1.7003** | 0.6733 | ±1.3466 | **-2.525** | **0.0116** | * |
| Education: high school or below (vs college) | -1.1264 | 1.1374 | ±2.2748 | -0.990 | 0.3220 |  |
| Site: UCSD (vs UAB) | -1.5189 | 0.8356 | ±1.6712 | -1.818 | 0.0691 | . |
| **Site: UW (vs UAB)** | **-1.7271** | 0.7907 | ±1.5814 | **-2.184** | **0.0289** | * |
| **Age (years)** | **-0.1059** | 0.0314 | ±0.0628 | **-3.376** | **7.36e-04** | *** |
| **BMI (kg/m2)** | **+0.3100** | 0.0679 | ±0.1359 | **+4.563** | **5.03e-06** | *** |
| Hypertension | +0.7032 | 0.7495 | ±1.4990 | +0.938 | 0.3482 |  |
| High cholesterol | -0.7475 | 0.6379 | ±1.2757 | -1.172 | 0.2412 |  |
| Kidney disease | +0.7368 | 1.2373 | ±2.4745 | +0.595 | 0.5515 |  |
| Circulatory disease | -0.4324 | 0.9358 | ±1.8716 | -0.462 | 0.6440 |  |
| Avg. daily mean/SD | -0.1212 | 0.2163 | ±0.4326 | -0.561 | 0.5751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **597**, R² = **0.1635**, Adj R² = **0.1478**, F-statistic = **10.39** (p = **1.64e-17**), Residual SE = **7.370** on **585** df, AIC = **4091.0**, BIC = **4143.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.0784** | 3.4842 | ±6.9683 | **+15.521** | **2.49e-54** | *** |
| **Education: graduate level (vs college)** | **-1.6808** | 0.6602 | ±1.3204 | **-2.546** | **0.0109** | * |
| Education: high school or below (vs college) | -1.3960 | 1.1350 | ±2.2700 | -1.230 | 0.2187 |  |
| Site: UCSD (vs UAB) | -1.4430 | 0.8290 | ±1.6580 | -1.741 | 0.0817 | . |
| **Site: UW (vs UAB)** | **-1.7003** | 0.7829 | ±1.5658 | **-2.172** | **0.0299** | * |
| **Age (years)** | **-0.1044** | 0.0307 | ±0.0613 | **-3.405** | **6.62e-04** | *** |
| **BMI (kg/m2)** | **+0.3113** | 0.0650 | ±0.1301 | **+4.786** | **1.70e-06** | *** |
| Hypertension | +0.8244 | 0.7494 | ±1.4988 | +1.100 | 0.2713 |  |
| High cholesterol | -0.7584 | 0.6320 | ±1.2641 | -1.200 | 0.2302 |  |
| Kidney disease | +0.5613 | 1.2219 | ±2.4439 | +0.459 | 0.6460 |  |
| Circulatory disease | -0.3181 | 0.9224 | ±1.8448 | -0.345 | 0.7302 |  |
| **MAG (mg/dL/h)** | **+0.1433** | 0.0515 | ±0.1030 | **+2.781** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **597**, R² = **0.1532**, Adj R² = **0.1373**, F-statistic = **9.62** (p = **4.36e-16**), Residual SE = **7.415** on **585** df, AIC = **4098.2**, BIC = **4150.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6292** | 3.6302 | ±7.2604 | **+15.599** | **7.34e-55** | *** |
| **Education: graduate level (vs college)** | **-1.7043** | 0.6692 | ±1.3385 | **-2.547** | **0.0109** | * |
| Education: high school or below (vs college) | -1.1781 | 1.1349 | ±2.2697 | -1.038 | 0.2992 |  |
| Site: UCSD (vs UAB) | -1.4733 | 0.8334 | ±1.6668 | -1.768 | 0.0771 | . |
| **Site: UW (vs UAB)** | **-1.7792** | 0.7882 | ±1.5764 | **-2.257** | **0.0240** | * |
| **Age (years)** | **-0.1089** | 0.0313 | ±0.0627 | **-3.477** | **5.08e-04** | *** |
| **BMI (kg/m2)** | **+0.3132** | 0.0679 | ±0.1357 | **+4.615** | **3.94e-06** | *** |
| Hypertension | +0.6866 | 0.7515 | ±1.5030 | +0.914 | 0.3609 |  |
| High cholesterol | -0.7415 | 0.6368 | ±1.2736 | -1.164 | 0.2443 |  |
| Kidney disease | +0.6689 | 1.2390 | ±2.4779 | +0.540 | 0.5893 |  |
| Circulatory disease | -0.4598 | 0.9258 | ±1.8517 | -0.497 | 0.6195 |  |
| Avg. daily range (mg/dL) | +0.0324 | 0.0199 | ±0.0398 | +1.626 | 0.1040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **597**, R² = **0.1600**, Adj R² = **0.1442**, F-statistic = **10.13** (p = **5.12e-17**), Residual SE = **7.385** on **585** df, AIC = **4093.5**, BIC = **4146.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.5097** | 3.1894 | ±6.3787 | **+18.032** | **1.10e-72** | *** |
| **Education: graduate level (vs college)** | **-1.7206** | 0.6642 | ±1.3283 | **-2.591** | **0.0096** | ** |
| Education: high school or below (vs college) | -1.0935 | 1.1155 | ±2.2311 | -0.980 | 0.3269 |  |
| Site: UCSD (vs UAB) | -1.4722 | 0.8320 | ±1.6640 | -1.769 | 0.0768 | . |
| **Site: UW (vs UAB)** | **-1.7386** | 0.7742 | ±1.5485 | **-2.246** | **0.0247** | * |
| **Age (years)** | **-0.1041** | 0.0306 | ±0.0612 | **-3.402** | **6.68e-04** | *** |
| **BMI (kg/m2)** | **+0.2968** | 0.0663 | ±0.1325 | **+4.479** | **7.49e-06** | *** |
| Hypertension | +0.7027 | 0.7374 | ±1.4748 | +0.953 | 0.3406 |  |
| High cholesterol | -0.8611 | 0.6357 | ±1.2714 | -1.355 | 0.1755 |  |
| Kidney disease | +0.7810 | 1.2054 | ±2.4108 | +0.648 | 0.5171 |  |
| Circulatory disease | -0.4548 | 0.9226 | ±1.8452 | -0.493 | 0.6220 |  |
| **SD of daily means (mg/dL)** | **+0.3800** | 0.1574 | ±0.3148 | **+2.414** | **0.0158** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **597**, R² = **0.1571**, Adj R² = **0.1412**, F-statistic = **9.91** (p = **1.28e-16**), Residual SE = **7.398** on **585** df, AIC = **4095.5**, BIC = **4148.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.5745** | 8.5960 | ±17.1921 | **+9.955** | **2.40e-23** | *** |
| **Education: graduate level (vs college)** | **-1.7194** | 0.6663 | ±1.3325 | **-2.581** | **0.0099** | ** |
| Education: high school or below (vs college) | -1.0615 | 1.1295 | ±2.2590 | -0.940 | 0.3473 |  |
| Site: UCSD (vs UAB) | -1.4184 | 0.8296 | ±1.6592 | -1.710 | 0.0873 | . |
| **Site: UW (vs UAB)** | **-1.7757** | 0.7820 | ±1.5639 | **-2.271** | **0.0232** | * |
| **Age (years)** | **-0.1096** | 0.0311 | ±0.0621 | **-3.527** | **4.20e-04** | *** |
| **BMI (kg/m2)** | **+0.3052** | 0.0668 | ±0.1336 | **+4.568** | **4.93e-06** | *** |
| Hypertension | +0.7104 | 0.7480 | ±1.4960 | +0.950 | 0.3422 |  |
| High cholesterol | -0.8447 | 0.6331 | ±1.2662 | -1.334 | 0.1821 |  |
| Kidney disease | +0.6732 | 1.2229 | ±2.4459 | +0.550 | 0.5820 |  |
| Circulatory disease | -0.5715 | 0.9271 | ±1.8542 | -0.616 | 0.5376 |  |
| **Time in range 70-180, pooled (%)** | **-0.2627** | 0.0746 | ±0.1492 | **-3.523** | **4.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **597**, R² = **0.1578**, Adj R² = **0.1420**, F-statistic = **9.97** (p = **1.01e-16**), Residual SE = **7.395** on **585** df, AIC = **4095.0**, BIC = **4147.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+87.5673** | 9.0612 | ±18.1224 | **+9.664** | **4.29e-22** | *** |
| **Education: graduate level (vs college)** | **-1.7216** | 0.6656 | ±1.3311 | **-2.587** | **0.0097** | ** |
| Education: high school or below (vs college) | -1.0400 | 1.1277 | ±2.2554 | -0.922 | 0.3564 |  |
| Site: UCSD (vs UAB) | -1.4016 | 0.8276 | ±1.6552 | -1.694 | 0.0903 | . |
| **Site: UW (vs UAB)** | **-1.7670** | 0.7808 | ±1.5616 | **-2.263** | **0.0236** | * |
| **Age (years)** | **-0.1095** | 0.0310 | ±0.0621 | **-3.530** | **4.16e-04** | *** |
| **BMI (kg/m2)** | **+0.3035** | 0.0664 | ±0.1329 | **+4.568** | **4.92e-06** | *** |
| Hypertension | +0.7179 | 0.7478 | ±1.4955 | +0.960 | 0.3370 |  |
| High cholesterol | -0.8525 | 0.6322 | ±1.2645 | -1.348 | 0.1775 |  |
| Kidney disease | +0.6638 | 1.2217 | ±2.4435 | +0.543 | 0.5869 |  |
| Circulatory disease | -0.5962 | 0.9269 | ±1.8538 | -0.643 | 0.5201 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.2823** | 0.0790 | ±0.1581 | **-3.571** | **3.56e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **597**, R² = **0.1539**, Adj R² = **0.1380**, F-statistic = **9.67** (p = **3.55e-16**), Residual SE = **7.412** on **585** df, AIC = **4097.8**, BIC = **4150.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.7043** | 3.3543 | ±6.7087 | **+17.799** | **7.18e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8659** | 0.6808 | ±1.3616 | **-2.741** | **0.0061** | ** |
| Education: high school or below (vs college) | -1.2724 | 1.1427 | ±2.2853 | -1.114 | 0.2655 |  |
| Site: UCSD (vs UAB) | -1.4769 | 0.8327 | ±1.6654 | -1.774 | 0.0761 | . |
| **Site: UW (vs UAB)** | **-1.7255** | 0.7865 | ±1.5730 | **-2.194** | **0.0282** | * |
| **Age (years)** | **-0.1053** | 0.0310 | ±0.0621 | **-3.393** | **6.93e-04** | *** |
| **BMI (kg/m2)** | **+0.3087** | 0.0683 | ±0.1367 | **+4.517** | **6.27e-06** | *** |
| Hypertension | +0.7195 | 0.7475 | ±1.4950 | +0.963 | 0.3358 |  |
| High cholesterol | -0.7357 | 0.6366 | ±1.2733 | -1.156 | 0.2479 |  |
| Kidney disease | +0.6985 | 1.2285 | ±2.4570 | +0.569 | 0.5696 |  |
| Circulatory disease | -0.4978 | 0.9354 | ±1.8708 | -0.532 | 0.5946 |  |
| Time 54-69, pooled (%) | -1.0440 | 0.5645 | ±1.1289 | -1.850 | 0.0644 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **597**, R² = **0.1530**, Adj R² = **0.1371**, F-statistic = **9.61** (p = **4.71e-16**), Residual SE = **7.416** on **585** df, AIC = **4098.4**, BIC = **4151.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6230** | 3.3498 | ±6.6996 | **+17.799** | **7.21e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8580** | 0.6808 | ±1.3615 | **-2.729** | **0.0063** | ** |
| Education: high school or below (vs college) | -1.2690 | 1.1424 | ±2.2848 | -1.111 | 0.2666 |  |
| Site: UCSD (vs UAB) | -1.4643 | 0.8325 | ±1.6650 | -1.759 | 0.0786 | . |
| **Site: UW (vs UAB)** | **-1.7183** | 0.7866 | ±1.5731 | **-2.185** | **0.0289** | * |
| **Age (years)** | **-0.1049** | 0.0310 | ±0.0620 | **-3.380** | **7.25e-04** | *** |
| **BMI (kg/m2)** | **+0.3089** | 0.0684 | ±0.1367 | **+4.519** | **6.22e-06** | *** |
| Hypertension | +0.7133 | 0.7479 | ±1.4957 | +0.954 | 0.3402 |  |
| High cholesterol | -0.7414 | 0.6368 | ±1.2735 | -1.164 | 0.2443 |  |
| Kidney disease | +0.7046 | 1.2301 | ±2.4601 | +0.573 | 0.5668 |  |
| Circulatory disease | -0.5076 | 0.9361 | ±1.8722 | -0.542 | 0.5877 |  |
| Avg. daily time 54-69 (%) | -0.9156 | 0.5291 | ±1.0583 | -1.730 | 0.0836 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **597**, R² = **0.1539**, Adj R² = **0.1380**, F-statistic = **9.67** (p = **3.55e-16**), Residual SE = **7.412** on **585** df, AIC = **4097.8**, BIC = **4150.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.7043** | 3.3543 | ±6.7087 | **+17.799** | **7.18e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8659** | 0.6808 | ±1.3616 | **-2.741** | **0.0061** | ** |
| Education: high school or below (vs college) | -1.2724 | 1.1427 | ±2.2853 | -1.114 | 0.2655 |  |
| Site: UCSD (vs UAB) | -1.4769 | 0.8327 | ±1.6654 | -1.774 | 0.0761 | . |
| **Site: UW (vs UAB)** | **-1.7255** | 0.7865 | ±1.5730 | **-2.194** | **0.0282** | * |
| **Age (years)** | **-0.1053** | 0.0310 | ±0.0621 | **-3.393** | **6.93e-04** | *** |
| **BMI (kg/m2)** | **+0.3087** | 0.0683 | ±0.1367 | **+4.517** | **6.27e-06** | *** |
| Hypertension | +0.7195 | 0.7475 | ±1.4950 | +0.963 | 0.3358 |  |
| High cholesterol | -0.7357 | 0.6366 | ±1.2733 | -1.156 | 0.2479 |  |
| Kidney disease | +0.6985 | 1.2285 | ±2.4570 | +0.569 | 0.5696 |  |
| Circulatory disease | -0.4978 | 0.9354 | ±1.8708 | -0.532 | 0.5946 |  |
| Time < 70 (%) | -1.0440 | 0.5645 | ±1.1289 | -1.850 | 0.0644 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **597**, R² = **0.1530**, Adj R² = **0.1371**, F-statistic = **9.61** (p = **4.71e-16**), Residual SE = **7.416** on **585** df, AIC = **4098.4**, BIC = **4151.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6230** | 3.3498 | ±6.6996 | **+17.799** | **7.21e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8580** | 0.6808 | ±1.3615 | **-2.729** | **0.0063** | ** |
| Education: high school or below (vs college) | -1.2690 | 1.1424 | ±2.2848 | -1.111 | 0.2666 |  |
| Site: UCSD (vs UAB) | -1.4643 | 0.8325 | ±1.6650 | -1.759 | 0.0786 | . |
| **Site: UW (vs UAB)** | **-1.7183** | 0.7866 | ±1.5731 | **-2.185** | **0.0289** | * |
| **Age (years)** | **-0.1049** | 0.0310 | ±0.0620 | **-3.380** | **7.25e-04** | *** |
| **BMI (kg/m2)** | **+0.3089** | 0.0684 | ±0.1367 | **+4.519** | **6.22e-06** | *** |
| Hypertension | +0.7133 | 0.7479 | ±1.4957 | +0.954 | 0.3402 |  |
| High cholesterol | -0.7414 | 0.6368 | ±1.2735 | -1.164 | 0.2443 |  |
| Kidney disease | +0.7046 | 1.2301 | ±2.4601 | +0.573 | 0.5668 |  |
| Circulatory disease | -0.5076 | 0.9361 | ±1.8722 | -0.542 | 0.5877 |  |
| Avg. daily time < 70 (%) | -0.9156 | 0.5291 | ±1.0583 | -1.730 | 0.0836 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **597**, R² = **0.1596**, Adj R² = **0.1438**, F-statistic = **10.10** (p = **5.76e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.7**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4061** | 3.2745 | ±6.5490 | **+18.142** | **1.48e-73** | *** |
| **Education: graduate level (vs college)** | **-1.7562** | 0.6650 | ±1.3300 | **-2.641** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.0949 | 1.1286 | ±2.2571 | -0.970 | 0.3320 |  |
| Site: UCSD (vs UAB) | -1.3806 | 0.8272 | ±1.6544 | -1.669 | 0.0951 | . |
| **Site: UW (vs UAB)** | **-1.7899** | 0.7811 | ±1.5621 | **-2.292** | **0.0219** | * |
| **Age (years)** | **-0.1105** | 0.0311 | ±0.0621 | **-3.557** | **3.75e-04** | *** |
| **BMI (kg/m2)** | **+0.3040** | 0.0667 | ±0.1334 | **+4.558** | **5.16e-06** | *** |
| Hypertension | +0.7119 | 0.7476 | ±1.4951 | +0.952 | 0.3409 |  |
| High cholesterol | -0.8532 | 0.6328 | ±1.2655 | -1.348 | 0.1775 |  |
| Kidney disease | +0.6485 | 1.2208 | ±2.4416 | +0.531 | 0.5953 |  |
| Circulatory disease | -0.6025 | 0.9262 | ±1.8524 | -0.650 | 0.5154 |  |
| **Time 181-250, pooled (%)** | **+0.2996** | 0.0750 | ±0.1500 | **+3.995** | **6.47e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **597**, R² = **0.1603**, Adj R² = **0.1445**, F-statistic = **10.16** (p = **4.53e-17**), Residual SE = **7.384** on **585** df, AIC = **4093.2**, BIC = **4145.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4457** | 3.2565 | ±6.5129 | **+18.255** | **1.90e-74** | *** |
| **Education: graduate level (vs college)** | **-1.7642** | 0.6642 | ±1.3285 | **-2.656** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.0792 | 1.1264 | ±2.2528 | -0.958 | 0.3380 |  |
| Site: UCSD (vs UAB) | -1.3544 | 0.8247 | ±1.6495 | -1.642 | 0.1005 |  |
| **Site: UW (vs UAB)** | **-1.7780** | 0.7797 | ±1.5595 | **-2.280** | **0.0226** | * |
| **Age (years)** | **-0.1102** | 0.0310 | ±0.0620 | **-3.556** | **3.77e-04** | *** |
| **BMI (kg/m2)** | **+0.3020** | 0.0663 | ±0.1325 | **+4.558** | **5.17e-06** | *** |
| Hypertension | +0.7187 | 0.7472 | ±1.4944 | +0.962 | 0.3361 |  |
| High cholesterol | -0.8619 | 0.6319 | ±1.2639 | -1.364 | 0.1726 |  |
| Kidney disease | +0.6378 | 1.2199 | ±2.4399 | +0.523 | 0.6011 |  |
| Circulatory disease | -0.6353 | 0.9263 | ±1.8527 | -0.686 | 0.4928 |  |
| **Avg. daily time 181-250 (%)** | **+0.3186** | 0.0785 | ±0.1570 | **+4.059** | **4.92e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **597**, R² = **0.1596**, Adj R² = **0.1438**, F-statistic = **10.10** (p = **5.76e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.7**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4061** | 3.2745 | ±6.5490 | **+18.142** | **1.48e-73** | *** |
| **Education: graduate level (vs college)** | **-1.7562** | 0.6650 | ±1.3300 | **-2.641** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.0949 | 1.1286 | ±2.2571 | -0.970 | 0.3320 |  |
| Site: UCSD (vs UAB) | -1.3806 | 0.8272 | ±1.6544 | -1.669 | 0.0951 | . |
| **Site: UW (vs UAB)** | **-1.7899** | 0.7811 | ±1.5621 | **-2.292** | **0.0219** | * |
| **Age (years)** | **-0.1105** | 0.0311 | ±0.0621 | **-3.557** | **3.75e-04** | *** |
| **BMI (kg/m2)** | **+0.3040** | 0.0667 | ±0.1334 | **+4.558** | **5.16e-06** | *** |
| Hypertension | +0.7119 | 0.7476 | ±1.4951 | +0.952 | 0.3409 |  |
| High cholesterol | -0.8532 | 0.6328 | ±1.2655 | -1.348 | 0.1775 |  |
| Kidney disease | +0.6485 | 1.2208 | ±2.4416 | +0.531 | 0.5953 |  |
| Circulatory disease | -0.6025 | 0.9262 | ±1.8524 | -0.650 | 0.5154 |  |
| **Time > 180 (%)** | **+0.2996** | 0.0750 | ±0.1500 | **+3.995** | **6.47e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **597**, R² = **0.1603**, Adj R² = **0.1445**, F-statistic = **10.16** (p = **4.53e-17**), Residual SE = **7.384** on **585** df, AIC = **4093.2**, BIC = **4145.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4457** | 3.2565 | ±6.5129 | **+18.255** | **1.90e-74** | *** |
| **Education: graduate level (vs college)** | **-1.7642** | 0.6642 | ±1.3285 | **-2.656** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.0792 | 1.1264 | ±2.2528 | -0.958 | 0.3380 |  |
| Site: UCSD (vs UAB) | -1.3544 | 0.8247 | ±1.6495 | -1.642 | 0.1005 |  |
| **Site: UW (vs UAB)** | **-1.7780** | 0.7797 | ±1.5595 | **-2.280** | **0.0226** | * |
| **Age (years)** | **-0.1102** | 0.0310 | ±0.0620 | **-3.556** | **3.77e-04** | *** |
| **BMI (kg/m2)** | **+0.3020** | 0.0663 | ±0.1325 | **+4.558** | **5.17e-06** | *** |
| Hypertension | +0.7187 | 0.7472 | ±1.4944 | +0.962 | 0.3361 |  |
| High cholesterol | -0.8619 | 0.6319 | ±1.2639 | -1.364 | 0.1726 |  |
| Kidney disease | +0.6378 | 1.2199 | ±2.4399 | +0.523 | 0.6011 |  |
| Circulatory disease | -0.6353 | 0.9263 | ±1.8527 | -0.686 | 0.4928 |  |
| **Avg. daily time > 180 (%)** | **+0.3186** | 0.0785 | ±0.1570 | **+4.059** | **4.92e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **597**, R² = **0.1541**, Adj R² = **0.1382**, F-statistic = **9.69** (p = **3.26e-16**), Residual SE = **7.411** on **585** df, AIC = **4097.6**, BIC = **4150.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3811** | 3.2900 | ±6.5800 | **+18.049** | **8.02e-73** | *** |
| **Education: graduate level (vs college)** | **-1.7118** | 0.6667 | ±1.3333 | **-2.568** | **0.0102** | * |
| Education: high school or below (vs college) | -1.2008 | 1.1362 | ±2.2723 | -1.057 | 0.2906 |  |
| Site: UCSD (vs UAB) | -1.4840 | 0.8317 | ±1.6635 | -1.784 | 0.0744 | . |
| **Site: UW (vs UAB)** | **-1.7615** | 0.7865 | ±1.5729 | **-2.240** | **0.0251** | * |
| **Age (years)** | **-0.1027** | 0.0309 | ±0.0617 | **-3.327** | **8.77e-04** | *** |
| **BMI (kg/m2)** | **+0.3000** | 0.0673 | ±0.1345 | **+4.460** | **8.18e-06** | *** |
| Hypertension | +0.7455 | 0.7469 | ±1.4938 | +0.998 | 0.3182 |  |
| High cholesterol | -0.8865 | 0.6407 | ±1.2814 | -1.384 | 0.1665 |  |
| Kidney disease | +0.7628 | 1.2233 | ±2.4466 | +0.624 | 0.5329 |  |
| Circulatory disease | -0.4571 | 0.9311 | ±1.8623 | -0.491 | 0.6235 |  |
| **Nocturnal time > 180 (%)** | **+0.1805** | 0.0538 | ±0.1075 | **+3.358** | **7.85e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 601; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **601**, R² = **0.0357**, Adj R² = **0.0194**, F-statistic = **2.18** (p = **0.0173**), Residual SE = **67.165** on **590** df, AIC = **6773.5**, BIC = **6821.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.5812** | 22.4075 | ±44.8149 | **+18.145** | **1.41e-73** | *** |
| Education: graduate level (vs college) | +0.9673 | 5.8196 | ±11.6392 | +0.166 | 0.8680 |  |
| Education: high school or below (vs college) | -12.5058 | 11.7747 | ±23.5494 | -1.062 | 0.2882 |  |
| Site: UCSD (vs UAB) | -7.8422 | 7.3562 | ±14.7123 | -1.066 | 0.2864 |  |
| Site: UW (vs UAB) | -1.9034 | 7.0625 | ±14.1250 | -0.270 | 0.7875 |  |
| Age (years) | +0.0086 | 0.2512 | ±0.5024 | +0.034 | 0.9725 |  |
| **BMI (kg/m2)** | **-1.0542** | 0.4471 | ±0.8942 | **-2.358** | **0.0184** | * |
| Hypertension | -9.7792 | 6.3759 | ±12.7519 | -1.534 | 0.1251 |  |
| High cholesterol | -5.1673 | 5.6392 | ±11.2783 | -0.916 | 0.3595 |  |
| Kidney disease | -15.7725 | 14.8422 | ±29.6845 | -1.063 | 0.2879 |  |
| Circulatory disease | +18.6708 | 10.2935 | ±20.5869 | +1.814 | 0.0697 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **601**, R² = **0.0478**, Adj R² = **0.0300**, F-statistic = **2.69** (p = **0.0022**), Residual SE = **66.798** on **589** df, AIC = **6767.9**, BIC = **6820.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+524.4715** | 50.6896 | ±101.3791 | **+10.347** | **4.33e-25** | *** |
| Education: graduate level (vs college) | +0.9927 | 5.7959 | ±11.5918 | +0.171 | 0.8640 |  |
| Education: high school or below (vs college) | -12.6057 | 11.6249 | ±23.2499 | -1.084 | 0.2782 |  |
| Site: UCSD (vs UAB) | -8.6214 | 7.3417 | ±14.6834 | -1.174 | 0.2403 |  |
| Site: UW (vs UAB) | -1.8786 | 7.0394 | ±14.0788 | -0.267 | 0.7896 |  |
| Age (years) | +0.1040 | 0.2585 | ±0.5170 | +0.402 | 0.6875 |  |
| **BMI (kg/m2)** | **-0.9014** | 0.4377 | ±0.8754 | **-2.059** | **0.0395** | * |
| Hypertension | -8.6751 | 6.3612 | ±12.7225 | -1.364 | 0.1726 |  |
| High cholesterol | -3.1121 | 5.6342 | ±11.2685 | -0.552 | 0.5807 |  |
| Kidney disease | -15.4265 | 14.5327 | ±29.0653 | -1.062 | 0.2885 |  |
| Circulatory disease | +18.3476 | 10.1483 | ±20.2966 | +1.808 | 0.0706 | . |
| **HbA1c (%)** | **-23.1400** | 9.2898 | ±18.5796 | **-2.491** | **0.0127** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0274**), Residual SE = **67.219** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.9977** | 33.6749 | ±67.3499 | **+12.264** | **1.41e-34** | *** |
| Education: graduate level (vs college) | +1.0250 | 5.8528 | ±11.7056 | +0.175 | 0.8610 |  |
| Education: high school or below (vs college) | -12.4817 | 11.7998 | ±23.5995 | -1.058 | 0.2901 |  |
| Site: UCSD (vs UAB) | -7.9334 | 7.3850 | ±14.7700 | -1.074 | 0.2827 |  |
| Site: UW (vs UAB) | -1.8031 | 7.1417 | ±14.2833 | -0.252 | 0.8007 |  |
| Age (years) | +0.0117 | 0.2529 | ±0.5057 | +0.046 | 0.9630 |  |
| **BMI (kg/m2)** | **-1.0419** | 0.4523 | ±0.9047 | **-2.303** | **0.0213** | * |
| Hypertension | -9.6990 | 6.3736 | ±12.7473 | -1.522 | 0.1281 |  |
| High cholesterol | -5.1274 | 5.6641 | ±11.3281 | -0.905 | 0.3653 |  |
| Kidney disease | -15.6439 | 14.8945 | ±29.7889 | -1.050 | 0.2936 |  |
| Circulatory disease | +18.7344 | 10.3550 | ±20.7101 | +1.809 | 0.0704 | . |
| Mean glucose (mg/dL) | -0.0593 | 0.2564 | ±0.5128 | -0.231 | 0.8172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0274**), Residual SE = **67.219** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+421.2006** | 64.6912 | ±129.3824 | **+6.511** | **7.47e-11** | *** |
| Education: graduate level (vs college) | +1.0250 | 5.8528 | ±11.7056 | +0.175 | 0.8610 |  |
| Education: high school or below (vs college) | -12.4817 | 11.7998 | ±23.5995 | -1.058 | 0.2901 |  |
| Site: UCSD (vs UAB) | -7.9334 | 7.3850 | ±14.7700 | -1.074 | 0.2827 |  |
| Site: UW (vs UAB) | -1.8031 | 7.1417 | ±14.2833 | -0.252 | 0.8007 |  |
| Age (years) | +0.0117 | 0.2529 | ±0.5057 | +0.046 | 0.9630 |  |
| **BMI (kg/m2)** | **-1.0419** | 0.4523 | ±0.9047 | **-2.303** | **0.0213** | * |
| Hypertension | -9.6990 | 6.3736 | ±12.7473 | -1.522 | 0.1281 |  |
| High cholesterol | -5.1274 | 5.6641 | ±11.3281 | -0.905 | 0.3653 |  |
| Kidney disease | -15.6439 | 14.8945 | ±29.7889 | -1.050 | 0.2936 |  |
| Circulatory disease | +18.7344 | 10.3550 | ±20.7101 | +1.809 | 0.0704 | . |
| GMI (%) | -2.4782 | 10.7200 | ±21.4401 | -0.231 | 0.8172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **601**, R² = **0.0394**, Adj R² = **0.0214**, F-statistic = **2.19** (p = **0.0135**), Residual SE = **67.094** on **589** df, AIC = **6773.2**, BIC = **6826.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+441.9977** | 32.1447 | ±64.2895 | **+13.750** | **5.08e-43** | *** |
| Education: graduate level (vs college) | +1.1106 | 5.8074 | ±11.6148 | +0.191 | 0.8483 |  |
| Education: high school or below (vs college) | -12.1833 | 11.7777 | ±23.5554 | -1.034 | 0.3009 |  |
| Site: UCSD (vs UAB) | -7.9886 | 7.3524 | ±14.7047 | -1.087 | 0.2772 |  |
| Site: UW (vs UAB) | -1.1986 | 7.1284 | ±14.2569 | -0.168 | 0.8665 |  |
| Age (years) | -0.0070 | 0.2510 | ±0.5020 | -0.028 | 0.9778 |  |
| **BMI (kg/m2)** | **-0.9115** | 0.4404 | ±0.8807 | **-2.070** | **0.0385** | * |
| Hypertension | -9.4446 | 6.3954 | ±12.7908 | -1.477 | 0.1397 |  |
| High cholesterol | -4.5683 | 5.6749 | ±11.3499 | -0.805 | 0.4208 |  |
| Kidney disease | -15.4473 | 14.7538 | ±29.5075 | -1.047 | 0.2951 |  |
| Circulatory disease | +18.7839 | 10.3313 | ±20.6626 | +1.818 | 0.0690 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.3309 | 0.2211 | ±0.4421 | -1.497 | 0.1345 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0272**), Residual SE = **67.217** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.0485** | 24.1111 | ±48.2222 | **+16.716** | **9.97e-63** | *** |
| Education: graduate level (vs college) | +1.0757 | 5.7874 | ±11.5747 | +0.186 | 0.8526 |  |
| Education: high school or below (vs college) | -12.5504 | 11.8400 | ±23.6799 | -1.060 | 0.2891 |  |
| Site: UCSD (vs UAB) | -7.6569 | 7.4280 | ±14.8559 | -1.031 | 0.3026 |  |
| Site: UW (vs UAB) | -1.9927 | 7.0816 | ±14.1631 | -0.281 | 0.7784 |  |
| Age (years) | +0.0000 | 0.2553 | ±0.5105 | +0.000 | 0.9999 |  |
| **BMI (kg/m2)** | **-1.0587** | 0.4500 | ±0.8999 | **-2.353** | **0.0186** | * |
| Hypertension | -9.8582 | 6.3942 | ±12.7884 | -1.542 | 0.1231 |  |
| High cholesterol | -5.2236 | 5.6782 | ±11.3563 | -0.920 | 0.3576 |  |
| Kidney disease | -15.8720 | 14.8584 | ±29.7168 | -1.068 | 0.2854 |  |
| Circulatory disease | +18.7129 | 10.3043 | ±20.6085 | +1.816 | 0.0694 | . |
| Glucose SD, pooled (mg/dL) | +0.2160 | 0.7827 | ±1.5655 | +0.276 | 0.7826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **601**, R² = **0.0361**, Adj R² = **0.0181**, F-statistic = **2.01** (p = **0.0256**), Residual SE = **67.207** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.8667** | 23.7550 | ±47.5101 | **+16.875** | **6.87e-64** | *** |
| Education: graduate level (vs college) | +1.0966 | 5.7952 | ±11.5904 | +0.189 | 0.8499 |  |
| Education: high school or below (vs college) | -12.6150 | 11.8717 | ±23.7435 | -1.063 | 0.2880 |  |
| Site: UCSD (vs UAB) | -7.4609 | 7.4565 | ±14.9130 | -1.001 | 0.3170 |  |
| Site: UW (vs UAB) | -2.0582 | 7.0795 | ±14.1589 | -0.291 | 0.7713 |  |
| Age (years) | -0.0070 | 0.2555 | ±0.5111 | -0.027 | 0.9783 |  |
| **BMI (kg/m2)** | **-1.0647** | 0.4511 | ±0.9021 | **-2.361** | **0.0182** | * |
| Hypertension | -9.8910 | 6.3913 | ±12.7827 | -1.548 | 0.1217 |  |
| High cholesterol | -5.2522 | 5.6754 | ±11.3508 | -0.925 | 0.3547 |  |
| Kidney disease | -15.9867 | 14.8728 | ±29.7455 | -1.075 | 0.2824 |  |
| Circulatory disease | +18.7128 | 10.3022 | ±20.6045 | +1.816 | 0.0693 | . |
| Avg. daily SD (mg/dL) | +0.3923 | 0.8150 | ±1.6301 | +0.481 | 0.6303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **601**, R² = **0.0360**, Adj R² = **0.0180**, F-statistic = **2.00** (p = **0.0262**), Residual SE = **67.211** on **589** df, AIC = **6775.3**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.7697** | 25.8376 | ±51.6753 | **+15.472** | **5.33e-54** | *** |
| Education: graduate level (vs college) | +1.2337 | 5.7871 | ±11.5743 | +0.213 | 0.8312 |  |
| Education: high school or below (vs college) | -12.5485 | 11.8384 | ±23.6768 | -1.060 | 0.2892 |  |
| Site: UCSD (vs UAB) | -7.6162 | 7.4041 | ±14.8083 | -1.029 | 0.3037 |  |
| Site: UW (vs UAB) | -1.9612 | 7.0647 | ±14.1294 | -0.278 | 0.7813 |  |
| Age (years) | -0.0027 | 0.2536 | ±0.5072 | -0.011 | 0.9916 |  |
| **BMI (kg/m2)** | **-1.0492** | 0.4465 | ±0.8930 | **-2.350** | **0.0188** | * |
| Hypertension | -9.8513 | 6.3967 | ±12.7935 | -1.540 | 0.1235 |  |
| High cholesterol | -5.2064 | 5.6564 | ±11.3129 | -0.920 | 0.3573 |  |
| Kidney disease | -15.8288 | 14.8376 | ±29.6751 | -1.067 | 0.2861 |  |
| Circulatory disease | +18.8125 | 10.3329 | ±20.6657 | +1.821 | 0.0687 | . |
| CV (%) | +0.4452 | 1.0163 | ±2.0326 | +0.438 | 0.6614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **601**, R² = **0.0362**, Adj R² = **0.0182**, F-statistic = **2.01** (p = **0.0252**), Residual SE = **67.203** on **589** df, AIC = **6775.1**, BIC = **6827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+416.0311** | 29.0629 | ±58.1258 | **+14.315** | **1.77e-46** | *** |
| Education: graduate level (vs college) | +1.3166 | 5.7907 | ±11.5814 | +0.227 | 0.8201 |  |
| Education: high school or below (vs college) | -12.5943 | 11.8591 | ±23.7182 | -1.062 | 0.2882 |  |
| Site: UCSD (vs UAB) | -7.5673 | 7.3893 | ±14.7785 | -1.024 | 0.3058 |  |
| Site: UW (vs UAB) | -1.9893 | 7.0645 | ±14.1290 | -0.282 | 0.7783 |  |
| Age (years) | -0.0042 | 0.2532 | ±0.5065 | -0.016 | 0.9869 |  |
| **BMI (kg/m2)** | **-1.0476** | 0.4464 | ±0.8929 | **-2.346** | **0.0190** | * |
| Hypertension | -9.8763 | 6.3952 | ±12.7904 | -1.544 | 0.1225 |  |
| High cholesterol | -5.2057 | 5.6527 | ±11.3053 | -0.921 | 0.3571 |  |
| Kidney disease | -15.8330 | 14.8365 | ±29.6730 | -1.067 | 0.2859 |  |
| Circulatory disease | +18.8675 | 10.3365 | ±20.6730 | +1.825 | 0.0680 | . |
| Mean / SD ratio | -1.4231 | 2.4679 | ±4.9358 | -0.577 | 0.5642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **601**, R² = **0.0366**, Adj R² = **0.0186**, F-statistic = **2.04** (p = **0.0233**), Residual SE = **67.189** on **589** df, AIC = **6774.9**, BIC = **6827.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+418.5574** | 29.1474 | ±58.2947 | **+14.360** | **9.22e-47** | *** |
| Education: graduate level (vs college) | +1.3164 | 5.7902 | ±11.5805 | +0.227 | 0.8201 |  |
| Education: high school or below (vs college) | -12.6814 | 11.9033 | ±23.8067 | -1.065 | 0.2867 |  |
| Site: UCSD (vs UAB) | -7.4000 | 7.4169 | ±14.8339 | -0.998 | 0.3184 |  |
| Site: UW (vs UAB) | -2.0503 | 7.0631 | ±14.1261 | -0.290 | 0.7716 |  |
| Age (years) | -0.0096 | 0.2538 | ±0.5076 | -0.038 | 0.9699 |  |
| **BMI (kg/m2)** | **-1.0549** | 0.4472 | ±0.8945 | **-2.359** | **0.0183** | * |
| Hypertension | -9.7889 | 6.3894 | ±12.7789 | -1.532 | 0.1255 |  |
| High cholesterol | -5.2053 | 5.6510 | ±11.3019 | -0.921 | 0.3570 |  |
| Kidney disease | -15.9454 | 14.8172 | ±29.6345 | -1.076 | 0.2819 |  |
| Circulatory disease | +18.8788 | 10.3122 | ±20.6244 | +1.831 | 0.0671 | . |
| Avg. daily mean/SD | -1.5363 | 2.0809 | ±4.1618 | -0.738 | 0.4603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **601**, R² = **0.0403**, Adj R² = **0.0224**, F-statistic = **2.25** (p = **0.0111**), Residual SE = **67.061** on **589** df, AIC = **6772.6**, BIC = **6825.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+431.7476** | 26.6199 | ±53.2397 | **+16.219** | **3.70e-59** | *** |
| Education: graduate level (vs college) | +0.8530 | 5.8154 | ±11.6309 | +0.147 | 0.8834 |  |
| Education: high school or below (vs college) | -10.9079 | 11.8308 | ±23.6615 | -0.922 | 0.3565 |  |
| Site: UCSD (vs UAB) | -8.3286 | 7.4708 | ±14.9415 | -1.115 | 0.2649 |  |
| Site: UW (vs UAB) | -2.0411 | 7.0782 | ±14.1565 | -0.288 | 0.7731 |  |
| Age (years) | +0.0113 | 0.2513 | ±0.5026 | +0.045 | 0.9642 |  |
| **BMI (kg/m2)** | **-1.0578** | 0.4436 | ±0.8873 | **-2.384** | **0.0171** | * |
| Hypertension | -10.4292 | 6.3641 | ±12.7281 | -1.639 | 0.1013 |  |
| High cholesterol | -5.1074 | 5.6242 | ±11.2485 | -0.908 | 0.3638 |  |
| Kidney disease | -14.7942 | 14.8764 | ±29.7528 | -0.994 | 0.3200 |  |
| Circulatory disease | +17.7045 | 10.3263 | ±20.6527 | +1.715 | 0.0864 | . |
| MAG (mg/dL/h) | -0.6933 | 0.5220 | ±1.0440 | -1.328 | 0.1841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **601**, R² = **0.0370**, Adj R² = **0.0190**, F-statistic = **2.06** (p = **0.0216**), Residual SE = **67.177** on **589** df, AIC = **6774.6**, BIC = **6827.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8318** | 25.7203 | ±51.4406 | **+15.312** | **6.35e-53** | *** |
| Education: graduate level (vs college) | +0.9863 | 5.8225 | ±11.6450 | +0.169 | 0.8655 |  |
| Education: high school or below (vs college) | -12.9612 | 11.9913 | ±23.9825 | -1.081 | 0.2797 |  |
| Site: UCSD (vs UAB) | -7.4314 | 7.4288 | ±14.8576 | -1.000 | 0.3171 |  |
| Site: UW (vs UAB) | -2.1449 | 7.0639 | ±14.1278 | -0.304 | 0.7614 |  |
| Age (years) | -0.0151 | 0.2560 | ±0.5119 | -0.059 | 0.9531 |  |
| **BMI (kg/m2)** | **-1.0367** | 0.4460 | ±0.8920 | **-2.324** | **0.0201** | * |
| Hypertension | -9.7846 | 6.3810 | ±12.7620 | -1.533 | 0.1252 |  |
| High cholesterol | -5.1820 | 5.6511 | ±11.3023 | -0.917 | 0.3592 |  |
| Kidney disease | -16.1997 | 14.9136 | ±29.8271 | -1.086 | 0.2774 |  |
| Circulatory disease | +18.7174 | 10.2827 | ±20.5654 | +1.820 | 0.0687 | . |
| Avg. daily range (mg/dL) | +0.1534 | 0.1937 | ±0.3874 | +0.792 | 0.4282 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **601**, R² = **0.0372**, Adj R² = **0.0193**, F-statistic = **2.07** (p = **0.0206**), Residual SE = **67.168** on **589** df, AIC = **6774.5**, BIC = **6827.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.2534** | 22.9962 | ±45.9924 | **+17.927** | **7.26e-72** | *** |
| Education: graduate level (vs college) | +0.8521 | 5.8161 | ±11.6323 | +0.146 | 0.8835 |  |
| Education: high school or below (vs college) | -12.5636 | 11.7787 | ±23.5575 | -1.067 | 0.2861 |  |
| Site: UCSD (vs UAB) | -8.0165 | 7.3518 | ±14.7036 | -1.090 | 0.2755 |  |
| Site: UW (vs UAB) | -1.7853 | 7.0645 | ±14.1290 | -0.253 | 0.8005 |  |
| Age (years) | +0.0064 | 0.2522 | ±0.5043 | +0.025 | 0.9798 |  |
| **BMI (kg/m2)** | **-1.0100** | 0.4474 | ±0.8949 | **-2.257** | **0.0240** | * |
| Hypertension | -9.8696 | 6.3694 | ±12.7387 | -1.550 | 0.1212 |  |
| High cholesterol | -4.7162 | 5.6538 | ±11.3076 | -0.834 | 0.4042 |  |
| Kidney disease | -15.9004 | 14.7742 | ±29.5483 | -1.076 | 0.2818 |  |
| Circulatory disease | +18.6714 | 10.2417 | ±20.4835 | +1.823 | 0.0683 | . |
| SD of daily means (mg/dL) | -1.1885 | 1.2298 | ±2.4596 | -0.966 | 0.3338 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **601**, R² = **0.0363**, Adj R² = **0.0183**, F-statistic = **2.01** (p = **0.0250**), Residual SE = **67.202** on **589** df, AIC = **6775.1**, BIC = **6827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+467.5277** | 102.3630 | ±204.7261 | **+4.567** | **4.94e-06** | *** |
| Education: graduate level (vs college) | +1.0186 | 5.8155 | ±11.6310 | +0.175 | 0.8610 |  |
| Education: high school or below (vs college) | -12.4527 | 11.7885 | ±23.5770 | -1.056 | 0.2908 |  |
| Site: UCSD (vs UAB) | -7.6192 | 7.3765 | ±14.7531 | -1.033 | 0.3017 |  |
| Site: UW (vs UAB) | -2.1298 | 7.1106 | ±14.2212 | -0.300 | 0.7645 |  |
| Age (years) | -0.0047 | 0.2515 | ±0.5030 | -0.019 | 0.9852 |  |
| **BMI (kg/m2)** | **-1.0676** | 0.4505 | ±0.9011 | **-2.370** | **0.0178** | * |
| Hypertension | -9.7429 | 6.3845 | ±12.7690 | -1.526 | 0.1270 |  |
| High cholesterol | -5.4242 | 5.6925 | ±11.3849 | -0.953 | 0.3407 |  |
| Kidney disease | -15.9943 | 14.8839 | ±29.7678 | -1.075 | 0.2826 |  |
| Circulatory disease | +18.4192 | 10.3985 | ±20.7970 | +1.771 | 0.0765 | . |
| Time in range 70-180, pooled (%) | -0.6079 | 0.9784 | ±1.9568 | -0.621 | 0.5344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **601**, R² = **0.0360**, Adj R² = **0.0180**, F-statistic = **2.00** (p = **0.0263**), Residual SE = **67.211** on **589** df, AIC = **6775.3**, BIC = **6828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+452.1977** | 106.3993 | ±212.7986 | **+4.250** | **2.14e-05** | *** |
| Education: graduate level (vs college) | +0.9991 | 5.8185 | ±11.6370 | +0.172 | 0.8637 |  |
| Education: high school or below (vs college) | -12.4407 | 11.7722 | ±23.5445 | -1.057 | 0.2906 |  |
| Site: UCSD (vs UAB) | -7.6684 | 7.3707 | ±14.7415 | -1.040 | 0.2982 |  |
| Site: UW (vs UAB) | -2.0490 | 7.1131 | ±14.2262 | -0.288 | 0.7733 |  |
| Age (years) | -0.0004 | 0.2515 | ±0.5029 | -0.002 | 0.9986 |  |
| **BMI (kg/m2)** | **-1.0664** | 0.4513 | ±0.9027 | **-2.363** | **0.0181** | * |
| Hypertension | -9.7354 | 6.3870 | ±12.7740 | -1.524 | 0.1274 |  |
| High cholesterol | -5.3603 | 5.6890 | ±11.3779 | -0.942 | 0.3461 |  |
| Kidney disease | -15.9479 | 14.8990 | ±29.7980 | -1.070 | 0.2844 |  |
| Circulatory disease | +18.4495 | 10.4290 | ±20.8580 | +1.769 | 0.0769 | . |
| Avg. daily time in range 70-180 (%) | -0.4545 | 1.0201 | ±2.0401 | -0.446 | 0.6559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **601**, R² = **0.0359**, Adj R² = **0.0179**, F-statistic = **1.99** (p = **0.0270**), Residual SE = **67.216** on **589** df, AIC = **6775.4**, BIC = **6828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.1039** | 22.7729 | ±45.5459 | **+17.877** | **1.79e-71** | *** |
| Education: graduate level (vs college) | +0.7638 | 5.8667 | ±11.7334 | +0.130 | 0.8964 |  |
| Education: high school or below (vs college) | -12.7021 | 11.7846 | ±23.5692 | -1.078 | 0.2811 |  |
| Site: UCSD (vs UAB) | -7.7223 | 7.3755 | ±14.7510 | -1.047 | 0.2951 |  |
| Site: UW (vs UAB) | -1.9002 | 7.0667 | ±14.1335 | -0.269 | 0.7880 |  |
| Age (years) | +0.0085 | 0.2516 | ±0.5031 | +0.034 | 0.9732 |  |
| **BMI (kg/m2)** | **-1.0569** | 0.4490 | ±0.8979 | **-2.354** | **0.0186** | * |
| Hypertension | -9.7972 | 6.3754 | ±12.7507 | -1.537 | 0.1244 |  |
| High cholesterol | -5.1569 | 5.6432 | ±11.2865 | -0.914 | 0.3608 |  |
| Kidney disease | -15.8186 | 14.8850 | ±29.7700 | -1.063 | 0.2879 |  |
| Circulatory disease | +18.6034 | 10.3189 | ±20.6379 | +1.803 | 0.0714 | . |
| Time 54-69, pooled (%) | -1.6483 | 4.7405 | ±9.4810 | -0.348 | 0.7281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **601**, R² = **0.0361**, Adj R² = **0.0181**, F-statistic = **2.01** (p = **0.0257**), Residual SE = **67.207** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.3302** | 22.6344 | ±45.2687 | **+17.996** | **2.09e-72** | *** |
| Education: graduate level (vs college) | +0.6290 | 5.8808 | ±11.7617 | +0.107 | 0.9148 |  |
| Education: high school or below (vs college) | -12.8507 | 11.7906 | ±23.5813 | -1.090 | 0.2758 |  |
| Site: UCSD (vs UAB) | -7.5994 | 7.3862 | ±14.7724 | -1.029 | 0.3035 |  |
| Site: UW (vs UAB) | -1.8897 | 7.0622 | ±14.1244 | -0.268 | 0.7890 |  |
| Age (years) | +0.0091 | 0.2513 | ±0.5027 | +0.036 | 0.9713 |  |
| **BMI (kg/m2)** | **-1.0584** | 0.4477 | ±0.8954 | **-2.364** | **0.0181** | * |
| Hypertension | -9.8233 | 6.3719 | ±12.7438 | -1.542 | 0.1232 |  |
| High cholesterol | -5.1718 | 5.6443 | ±11.2885 | -0.916 | 0.3595 |  |
| Kidney disease | -15.8430 | 14.8903 | ±29.7806 | -1.064 | 0.2873 |  |
| Circulatory disease | +18.5128 | 10.3025 | ±20.6051 | +1.797 | 0.0723 | . |
| Avg. daily time 54-69 (%) | -2.5589 | 4.7620 | ±9.5240 | -0.537 | 0.5910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **601**, R² = **0.0359**, Adj R² = **0.0179**, F-statistic = **1.99** (p = **0.0270**), Residual SE = **67.216** on **589** df, AIC = **6775.4**, BIC = **6828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.1039** | 22.7729 | ±45.5459 | **+17.877** | **1.79e-71** | *** |
| Education: graduate level (vs college) | +0.7638 | 5.8667 | ±11.7334 | +0.130 | 0.8964 |  |
| Education: high school or below (vs college) | -12.7021 | 11.7846 | ±23.5692 | -1.078 | 0.2811 |  |
| Site: UCSD (vs UAB) | -7.7223 | 7.3755 | ±14.7510 | -1.047 | 0.2951 |  |
| Site: UW (vs UAB) | -1.9002 | 7.0667 | ±14.1335 | -0.269 | 0.7880 |  |
| Age (years) | +0.0085 | 0.2516 | ±0.5031 | +0.034 | 0.9732 |  |
| **BMI (kg/m2)** | **-1.0569** | 0.4490 | ±0.8979 | **-2.354** | **0.0186** | * |
| Hypertension | -9.7972 | 6.3754 | ±12.7507 | -1.537 | 0.1244 |  |
| High cholesterol | -5.1569 | 5.6432 | ±11.2865 | -0.914 | 0.3608 |  |
| Kidney disease | -15.8186 | 14.8850 | ±29.7700 | -1.063 | 0.2879 |  |
| Circulatory disease | +18.6034 | 10.3189 | ±20.6379 | +1.803 | 0.0714 | . |
| Time < 70 (%) | -1.6483 | 4.7405 | ±9.4810 | -0.348 | 0.7281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **601**, R² = **0.0361**, Adj R² = **0.0181**, F-statistic = **2.01** (p = **0.0257**), Residual SE = **67.207** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.3302** | 22.6344 | ±45.2687 | **+17.996** | **2.09e-72** | *** |
| Education: graduate level (vs college) | +0.6290 | 5.8808 | ±11.7617 | +0.107 | 0.9148 |  |
| Education: high school or below (vs college) | -12.8507 | 11.7906 | ±23.5813 | -1.090 | 0.2758 |  |
| Site: UCSD (vs UAB) | -7.5994 | 7.3862 | ±14.7724 | -1.029 | 0.3035 |  |
| Site: UW (vs UAB) | -1.8897 | 7.0622 | ±14.1244 | -0.268 | 0.7890 |  |
| Age (years) | +0.0091 | 0.2513 | ±0.5027 | +0.036 | 0.9713 |  |
| **BMI (kg/m2)** | **-1.0584** | 0.4477 | ±0.8954 | **-2.364** | **0.0181** | * |
| Hypertension | -9.8233 | 6.3719 | ±12.7438 | -1.542 | 0.1232 |  |
| High cholesterol | -5.1718 | 5.6443 | ±11.2885 | -0.916 | 0.3595 |  |
| Kidney disease | -15.8430 | 14.8903 | ±29.7806 | -1.064 | 0.2873 |  |
| Circulatory disease | +18.5128 | 10.3025 | ±20.6051 | +1.797 | 0.0723 | . |
| Avg. daily time < 70 (%) | -2.5589 | 4.7620 | ±9.5240 | -0.537 | 0.5910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **601**, R² = **0.0364**, Adj R² = **0.0184**, F-statistic = **2.02** (p = **0.0244**), Residual SE = **67.198** on **589** df, AIC = **6775.0**, BIC = **6827.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9618** | 22.5197 | ±45.0394 | **+18.071** | **5.36e-73** | *** |
| Education: graduate level (vs college) | +0.9413 | 5.8327 | ±11.6655 | +0.161 | 0.8718 |  |
| Education: high school or below (vs college) | -12.5269 | 11.8040 | ±23.6079 | -1.061 | 0.2886 |  |
| Site: UCSD (vs UAB) | -7.5495 | 7.3821 | ±14.7641 | -1.023 | 0.3065 |  |
| Site: UW (vs UAB) | -2.1501 | 7.1163 | ±14.2327 | -0.302 | 0.7625 |  |
| Age (years) | -0.0060 | 0.2521 | ±0.5042 | -0.024 | 0.9810 |  |
| **BMI (kg/m2)** | **-1.0700** | 0.4517 | ±0.9034 | **-2.369** | **0.0178** | * |
| Hypertension | -9.7467 | 6.3847 | ±12.7694 | -1.527 | 0.1269 |  |
| High cholesterol | -5.4444 | 5.6963 | ±11.3925 | -0.956 | 0.3392 |  |
| Kidney disease | -16.0340 | 14.8967 | ±29.7933 | -1.076 | 0.2818 |  |
| Circulatory disease | +18.3680 | 10.4159 | ±20.8318 | +1.763 | 0.0778 | . |
| Time 181-250, pooled (%) | +0.6658 | 1.0030 | ±2.0059 | +0.664 | 0.5068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **601**, R² = **0.0362**, Adj R² = **0.0182**, F-statistic = **2.01** (p = **0.0255**), Residual SE = **67.206** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9511** | 22.5426 | ±45.0851 | **+18.053** | **7.53e-73** | *** |
| Education: graduate level (vs college) | +0.9323 | 5.8376 | ±11.6752 | +0.160 | 0.8731 |  |
| Education: high school or below (vs college) | -12.5011 | 11.7925 | ±23.5850 | -1.060 | 0.2891 |  |
| Site: UCSD (vs UAB) | -7.5741 | 7.3793 | ±14.7585 | -1.026 | 0.3047 |  |
| Site: UW (vs UAB) | -2.0803 | 7.1138 | ±14.2276 | -0.292 | 0.7700 |  |
| Age (years) | -0.0025 | 0.2518 | ±0.5037 | -0.010 | 0.9921 |  |
| **BMI (kg/m2)** | **-1.0702** | 0.4524 | ±0.9047 | **-2.366** | **0.0180** | * |
| Hypertension | -9.7347 | 6.3869 | ±12.7737 | -1.524 | 0.1275 |  |
| High cholesterol | -5.4068 | 5.6970 | ±11.3939 | -0.949 | 0.3426 |  |
| Kidney disease | -16.0047 | 14.9128 | ±29.8257 | -1.073 | 0.2832 |  |
| Circulatory disease | +18.3627 | 10.4489 | ±20.8979 | +1.757 | 0.0789 | . |
| Avg. daily time 181-250 (%) | +0.5617 | 1.0422 | ±2.0845 | +0.539 | 0.5899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **601**, R² = **0.0364**, Adj R² = **0.0184**, F-statistic = **2.02** (p = **0.0244**), Residual SE = **67.198** on **589** df, AIC = **6775.0**, BIC = **6827.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9618** | 22.5197 | ±45.0394 | **+18.071** | **5.36e-73** | *** |
| Education: graduate level (vs college) | +0.9413 | 5.8327 | ±11.6655 | +0.161 | 0.8718 |  |
| Education: high school or below (vs college) | -12.5269 | 11.8040 | ±23.6079 | -1.061 | 0.2886 |  |
| Site: UCSD (vs UAB) | -7.5495 | 7.3821 | ±14.7641 | -1.023 | 0.3065 |  |
| Site: UW (vs UAB) | -2.1501 | 7.1163 | ±14.2327 | -0.302 | 0.7625 |  |
| Age (years) | -0.0060 | 0.2521 | ±0.5042 | -0.024 | 0.9810 |  |
| **BMI (kg/m2)** | **-1.0700** | 0.4517 | ±0.9034 | **-2.369** | **0.0178** | * |
| Hypertension | -9.7467 | 6.3847 | ±12.7694 | -1.527 | 0.1269 |  |
| High cholesterol | -5.4444 | 5.6963 | ±11.3925 | -0.956 | 0.3392 |  |
| Kidney disease | -16.0340 | 14.8967 | ±29.7933 | -1.076 | 0.2818 |  |
| Circulatory disease | +18.3680 | 10.4159 | ±20.8318 | +1.763 | 0.0778 | . |
| Time > 180 (%) | +0.6658 | 1.0030 | ±2.0059 | +0.664 | 0.5068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **601**, R² = **0.0362**, Adj R² = **0.0182**, F-statistic = **2.01** (p = **0.0255**), Residual SE = **67.206** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9511** | 22.5426 | ±45.0851 | **+18.053** | **7.53e-73** | *** |
| Education: graduate level (vs college) | +0.9323 | 5.8376 | ±11.6752 | +0.160 | 0.8731 |  |
| Education: high school or below (vs college) | -12.5011 | 11.7925 | ±23.5850 | -1.060 | 0.2891 |  |
| Site: UCSD (vs UAB) | -7.5741 | 7.3793 | ±14.7585 | -1.026 | 0.3047 |  |
| Site: UW (vs UAB) | -2.0803 | 7.1138 | ±14.2276 | -0.292 | 0.7700 |  |
| Age (years) | -0.0025 | 0.2518 | ±0.5037 | -0.010 | 0.9921 |  |
| **BMI (kg/m2)** | **-1.0702** | 0.4524 | ±0.9047 | **-2.366** | **0.0180** | * |
| Hypertension | -9.7347 | 6.3869 | ±12.7737 | -1.524 | 0.1275 |  |
| High cholesterol | -5.4068 | 5.6970 | ±11.3939 | -0.949 | 0.3426 |  |
| Kidney disease | -16.0047 | 14.9128 | ±29.8257 | -1.073 | 0.2832 |  |
| Circulatory disease | +18.3627 | 10.4489 | ±20.8979 | +1.757 | 0.0789 | . |
| Avg. daily time > 180 (%) | +0.5617 | 1.0422 | ±2.0845 | +0.539 | 0.5899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0273**), Residual SE = **67.218** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.5318** | 22.4085 | ±44.8170 | **+18.142** | **1.49e-73** | *** |
| Education: graduate level (vs college) | +0.9437 | 5.8170 | ±11.6341 | +0.162 | 0.8711 |  |
| Education: high school or below (vs college) | -12.3804 | 11.8300 | ±23.6600 | -1.047 | 0.2953 |  |
| Site: UCSD (vs UAB) | -7.9370 | 7.3512 | ±14.7023 | -1.080 | 0.2803 |  |
| Site: UW (vs UAB) | -1.8487 | 7.0866 | ±14.1731 | -0.261 | 0.7942 |  |
| Age (years) | +0.0066 | 0.2518 | ±0.5036 | +0.026 | 0.9792 |  |
| **BMI (kg/m2)** | **-1.0421** | 0.4470 | ±0.8940 | **-2.331** | **0.0197** | * |
| Hypertension | -9.8351 | 6.3953 | ±12.7907 | -1.538 | 0.1241 |  |
| High cholesterol | -4.9709 | 5.7395 | ±11.4791 | -0.866 | 0.3864 |  |
| Kidney disease | -15.7879 | 14.8386 | ±29.6772 | -1.064 | 0.2873 |  |
| Circulatory disease | +18.6651 | 10.2979 | ±20.5957 | +1.813 | 0.0699 | . |
| Nocturnal time > 180 (%) | -0.2364 | 0.7004 | ±1.4007 | -0.337 | 0.7358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 598; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **598**, R² = **0.1019**, Adj R² = **0.0866**, F-statistic = **6.66** (p = **7.87e-10**), Residual SE = **16.942** on **587** df, AIC = **5092.4**, BIC = **5140.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7537** | 7.2671 | ±14.5341 | **+6.021** | **1.74e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7145** | 1.5343 | ±3.0687 | **-2.421** | **0.0155** | * |
| Education: high school or below (vs college) | -0.9505 | 2.4632 | ±4.9264 | -0.386 | 0.6996 |  |
| Site: UCSD (vs UAB) | +0.7626 | 1.9042 | ±3.8084 | +0.400 | 0.6888 |  |
| Site: UW (vs UAB) | -1.5617 | 1.7548 | ±3.5097 | -0.890 | 0.3735 |  |
| **Age (years)** | **-0.1833** | 0.0709 | ±0.1417 | **-2.588** | **0.0097** | ** |
| **BMI (kg/m2)** | **+0.6030** | 0.1463 | ±0.2925 | **+4.123** | **3.74e-05** | *** |
| Hypertension | +0.7734 | 1.6866 | ±3.3732 | +0.459 | 0.6465 |  |
| High cholesterol | -1.4749 | 1.4733 | ±2.9465 | -1.001 | 0.3168 |  |
| Kidney disease | +3.1862 | 3.0158 | ±6.0316 | +1.057 | 0.2907 |  |
| Circulatory disease | -0.0732 | 2.2723 | ±4.5446 | -0.032 | 0.9743 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **598**, R² = **0.1063**, Adj R² = **0.0895**, F-statistic = **6.34** (p = **5.99e-10**), Residual SE = **16.914** on **586** df, AIC = **5091.4**, BIC = **5144.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.2972** | 12.5339 | ±25.0678 | **+2.018** | **0.0436** | * |
| **Education: graduate level (vs college)** | **-3.7474** | 1.5269 | ±3.0539 | **-2.454** | **0.0141** | * |
| Education: high school or below (vs college) | -0.9235 | 2.4746 | ±4.9491 | -0.373 | 0.7090 |  |
| Site: UCSD (vs UAB) | +0.8435 | 1.8865 | ±3.7729 | +0.447 | 0.6548 |  |
| Site: UW (vs UAB) | -1.5727 | 1.7501 | ±3.5002 | -0.899 | 0.3689 |  |
| **Age (years)** | **-0.1988** | 0.0717 | ±0.1434 | **-2.772** | **0.0056** | ** |
| **BMI (kg/m2)** | **+0.5754** | 0.1435 | ±0.2870 | **+4.009** | **6.10e-05** | *** |
| Hypertension | +0.5809 | 1.6920 | ±3.3840 | +0.343 | 0.7314 |  |
| High cholesterol | -1.8041 | 1.4757 | ±2.9514 | -1.223 | 0.2215 |  |
| Kidney disease | +3.2054 | 2.9611 | ±5.9221 | +1.083 | 0.2790 |  |
| Circulatory disease | -0.0085 | 2.2406 | ±4.4812 | -0.004 | 0.9970 |  |
| HbA1c (%) | +3.6531 | 2.2405 | ±4.4811 | +1.630 | 0.1030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **598**, R² = **0.1100**, Adj R² = **0.0933**, F-statistic = **6.59** (p = **2.04e-10**), Residual SE = **16.879** on **586** df, AIC = **5088.9**, BIC = **5141.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.9775** | 9.2414 | ±18.4828 | **+3.027** | **0.0025** | ** |
| **Education: graduate level (vs college)** | **-3.8518** | 1.5247 | ±3.0494 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | -0.9630 | 2.4459 | ±4.8917 | -0.394 | 0.6938 |  |
| Site: UCSD (vs UAB) | +1.0483 | 1.8941 | ±3.7882 | +0.553 | 0.5799 |  |
| Site: UW (vs UAB) | -1.7898 | 1.7544 | ±3.5088 | -1.020 | 0.3076 |  |
| **Age (years)** | **-0.1915** | 0.0706 | ±0.1412 | **-2.713** | **0.0067** | ** |
| **BMI (kg/m2)** | **+0.5740** | 0.1435 | ±0.2870 | **+4.000** | **6.34e-05** | *** |
| Hypertension | +0.5744 | 1.6813 | ±3.3625 | +0.342 | 0.7326 |  |
| High cholesterol | -1.5338 | 1.4710 | ±2.9419 | -1.043 | 0.2971 |  |
| Kidney disease | +2.8807 | 3.0038 | ±6.0076 | +0.959 | 0.3376 |  |
| Circulatory disease | -0.3116 | 2.2574 | ±4.5148 | -0.138 | 0.8902 |  |
| **Mean glucose (mg/dL)** | **+0.1455** | 0.0613 | ±0.1226 | **+2.374** | **0.0176** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **598**, R² = **0.1100**, Adj R² = **0.0933**, F-statistic = **6.59** (p = **2.04e-10**), Residual SE = **16.879** on **586** df, AIC = **5088.9**, BIC = **5141.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.8402 | 16.0838 | ±32.1677 | +0.487 | 0.6259 |  |
| **Education: graduate level (vs college)** | **-3.8518** | 1.5247 | ±3.0494 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | -0.9630 | 2.4459 | ±4.8917 | -0.394 | 0.6938 |  |
| Site: UCSD (vs UAB) | +1.0483 | 1.8941 | ±3.7882 | +0.553 | 0.5799 |  |
| Site: UW (vs UAB) | -1.7898 | 1.7544 | ±3.5088 | -1.020 | 0.3076 |  |
| **Age (years)** | **-0.1915** | 0.0706 | ±0.1412 | **-2.713** | **0.0067** | ** |
| **BMI (kg/m2)** | **+0.5740** | 0.1435 | ±0.2870 | **+4.000** | **6.34e-05** | *** |
| Hypertension | +0.5744 | 1.6813 | ±3.3625 | +0.342 | 0.7326 |  |
| High cholesterol | -1.5338 | 1.4710 | ±2.9419 | -1.043 | 0.2971 |  |
| Kidney disease | +2.8807 | 3.0038 | ±6.0076 | +0.959 | 0.3376 |  |
| Circulatory disease | -0.3116 | 2.2574 | ±4.5148 | -0.138 | 0.8902 |  |
| **GMI (%)** | **+6.0838** | 2.5629 | ±5.1258 | **+2.374** | **0.0176** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **598**, R² = **0.1144**, Adj R² = **0.0978**, F-statistic = **6.88** (p = **5.68e-11**), Residual SE = **16.837** on **586** df, AIC = **5085.9**, BIC = **5138.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.7830** | 8.1681 | ±16.3362 | **+3.279** | **0.0010** | ** |
| **Education: graduate level (vs college)** | **-3.7834** | 1.5175 | ±3.0349 | **-2.493** | **0.0127** | * |
| Education: high school or below (vs college) | -1.0742 | 2.4497 | ±4.8994 | -0.438 | 0.6610 |  |
| Site: UCSD (vs UAB) | +0.8602 | 1.8849 | ±3.7699 | +0.456 | 0.6481 |  |
| Site: UW (vs UAB) | -1.8925 | 1.7514 | ±3.5028 | -1.081 | 0.2799 |  |
| **Age (years)** | **-0.1761** | 0.0697 | ±0.1394 | **-2.527** | **0.0115** | * |
| **BMI (kg/m2)** | **+0.5353** | 0.1405 | ±0.2811 | **+3.809** | **1.40e-04** | *** |
| Hypertension | +0.6255 | 1.6746 | ±3.3493 | +0.374 | 0.7088 |  |
| High cholesterol | -1.7193 | 1.4679 | ±2.9359 | -1.171 | 0.2415 |  |
| Kidney disease | +3.0276 | 2.9643 | ±5.9285 | +1.021 | 0.3071 |  |
| Circulatory disease | -0.2374 | 2.2370 | ±4.4739 | -0.106 | 0.9155 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.1583** | 0.0539 | ±0.1078 | **+2.938** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **598**, R² = **0.1062**, Adj R² = **0.0895**, F-statistic = **6.33** (p = **6.07e-10**), Residual SE = **16.915** on **586** df, AIC = **5091.4**, BIC = **5144.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.5765** | 7.6601 | ±15.3203 | **+5.036** | **4.75e-07** | *** |
| **Education: graduate level (vs college)** | **-3.5566** | 1.5325 | ±3.0649 | **-2.321** | **0.0203** | * |
| Education: high school or below (vs college) | -0.9298 | 2.4494 | ±4.8988 | -0.380 | 0.7042 |  |
| Site: UCSD (vs UAB) | +1.0244 | 1.8989 | ±3.7979 | +0.539 | 0.5896 |  |
| Site: UW (vs UAB) | -1.7153 | 1.7534 | ±3.5067 | -0.978 | 0.3279 |  |
| **Age (years)** | **-0.1949** | 0.0719 | ±0.1439 | **-2.710** | **0.0067** | ** |
| **BMI (kg/m2)** | **+0.5949** | 0.1442 | ±0.2883 | **+4.127** | **3.68e-05** | *** |
| Hypertension | +0.6077 | 1.6935 | ±3.3869 | +0.359 | 0.7197 |  |
| High cholesterol | -1.5014 | 1.4727 | ±2.9454 | -1.019 | 0.3080 |  |
| Kidney disease | +3.0478 | 3.0014 | ±6.0028 | +1.015 | 0.3099 |  |
| Circulatory disease | -0.0498 | 2.2551 | ±4.5102 | -0.022 | 0.9824 |  |
| Glucose SD, pooled (mg/dL) | +0.3166 | 0.1955 | ±0.3911 | +1.619 | 0.1055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **598**, R² = **0.1050**, Adj R² = **0.0882**, F-statistic = **6.25** (p = **8.58e-10**), Residual SE = **16.926** on **586** df, AIC = **5092.2**, BIC = **5145.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.7573** | 7.5597 | ±15.1194 | **+5.259** | **1.45e-07** | *** |
| **Education: graduate level (vs college)** | **-3.6144** | 1.5327 | ±3.0653 | **-2.358** | **0.0184** | * |
| Education: high school or below (vs college) | -0.9485 | 2.4504 | ±4.9008 | -0.387 | 0.6987 |  |
| Site: UCSD (vs UAB) | +1.0152 | 1.9016 | ±3.8031 | +0.534 | 0.5934 |  |
| Site: UW (vs UAB) | -1.6900 | 1.7570 | ±3.5140 | -0.962 | 0.3361 |  |
| **Age (years)** | **-0.1934** | 0.0719 | ±0.1438 | **-2.690** | **0.0071** | ** |
| **BMI (kg/m2)** | **+0.5942** | 0.1443 | ±0.2887 | **+4.117** | **3.84e-05** | *** |
| Hypertension | +0.6536 | 1.6960 | ±3.3919 | +0.385 | 0.6999 |  |
| High cholesterol | -1.4894 | 1.4748 | ±2.9495 | -1.010 | 0.3125 |  |
| Kidney disease | +3.0564 | 3.0181 | ±6.0363 | +1.013 | 0.3112 |  |
| Circulatory disease | -0.0628 | 2.2635 | ±4.5271 | -0.028 | 0.9779 |  |
| Avg. daily SD (mg/dL) | +0.2744 | 0.2003 | ±0.4005 | +1.370 | 0.1707 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **598**, R² = **0.1025**, Adj R² = **0.0856**, F-statistic = **6.08** (p = **1.79e-09**), Residual SE = **16.951** on **586** df, AIC = **5094.0**, BIC = **5146.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.3289** | 8.2345 | ±16.4690 | **+5.019** | **5.19e-07** | *** |
| **Education: graduate level (vs college)** | **-3.6232** | 1.5454 | ±3.0908 | **-2.345** | **0.0191** | * |
| Education: high school or below (vs college) | -0.9358 | 2.4621 | ±4.9242 | -0.380 | 0.7039 |  |
| Site: UCSD (vs UAB) | +0.8337 | 1.9065 | ±3.8131 | +0.437 | 0.6619 |  |
| Site: UW (vs UAB) | -1.5908 | 1.7565 | ±3.5129 | -0.906 | 0.3651 |  |
| **Age (years)** | **-0.1868** | 0.0717 | ±0.1434 | **-2.606** | **0.0092** | ** |
| **BMI (kg/m2)** | **+0.6041** | 0.1461 | ±0.2923 | **+4.134** | **3.57e-05** | *** |
| Hypertension | +0.7266 | 1.6922 | ±3.3845 | +0.429 | 0.6677 |  |
| High cholesterol | -1.4696 | 1.4761 | ±2.9523 | -0.996 | 0.3194 |  |
| Kidney disease | +3.1683 | 3.0173 | ±6.0345 | +1.050 | 0.2937 |  |
| Circulatory disease | -0.0279 | 2.2730 | ±4.5461 | -0.012 | 0.9902 |  |
| CV (%) | +0.1582 | 0.2654 | ±0.5307 | +0.596 | 0.5511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **598**, R² = **0.1030**, Adj R² = **0.0861**, F-statistic = **6.12** (p = **1.54e-09**), Residual SE = **16.946** on **586** df, AIC = **5093.6**, BIC = **5146.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2823** | 8.4354 | ±16.8708 | **+5.605** | **2.08e-08** | *** |
| **Education: graduate level (vs college)** | **-3.5827** | 1.5434 | ±3.0867 | **-2.321** | **0.0203** | * |
| Education: high school or below (vs college) | -0.9431 | 2.4568 | ±4.9135 | -0.384 | 0.7011 |  |
| Site: UCSD (vs UAB) | +0.8412 | 1.9058 | ±3.8116 | +0.441 | 0.6589 |  |
| Site: UW (vs UAB) | -1.6188 | 1.7562 | ±3.5124 | -0.922 | 0.3566 |  |
| **Age (years)** | **-0.1874** | 0.0715 | ±0.1429 | **-2.622** | **0.0088** | ** |
| **BMI (kg/m2)** | **+0.6043** | 0.1461 | ±0.2921 | **+4.137** | **3.52e-05** | *** |
| Hypertension | +0.7076 | 1.6927 | ±3.3853 | +0.418 | 0.6759 |  |
| High cholesterol | -1.4604 | 1.4760 | ±2.9519 | -0.989 | 0.3225 |  |
| Kidney disease | +3.1574 | 3.0102 | ±6.0203 | +1.049 | 0.2942 |  |
| Circulatory disease | -0.0087 | 2.2727 | ±4.5455 | -0.004 | 0.9970 |  |
| Mean / SD ratio | -0.5294 | 0.6328 | ±1.2656 | -0.837 | 0.4028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **598**, R² = **0.1025**, Adj R² = **0.0857**, F-statistic = **6.08** (p = **1.76e-09**), Residual SE = **16.950** on **586** df, AIC = **5093.9**, BIC = **5146.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.3275** | 8.4171 | ±16.8341 | **+5.504** | **3.71e-08** | *** |
| **Education: graduate level (vs college)** | **-3.6328** | 1.5413 | ±3.0827 | **-2.357** | **0.0184** | * |
| Education: high school or below (vs college) | -0.9566 | 2.4596 | ±4.9192 | -0.389 | 0.6973 |  |
| Site: UCSD (vs UAB) | +0.8353 | 1.9082 | ±3.8164 | +0.438 | 0.6616 |  |
| Site: UW (vs UAB) | -1.6124 | 1.7590 | ±3.5180 | -0.917 | 0.3593 |  |
| **Age (years)** | **-0.1867** | 0.0715 | ±0.1430 | **-2.612** | **0.0090** | ** |
| **BMI (kg/m2)** | **+0.6019** | 0.1459 | ±0.2918 | **+4.125** | **3.70e-05** | *** |
| Hypertension | +0.7491 | 1.6925 | ±3.3849 | +0.443 | 0.6581 |  |
| High cholesterol | -1.4608 | 1.4766 | ±2.9532 | -0.989 | 0.3225 |  |
| Kidney disease | +3.1549 | 3.0212 | ±6.0424 | +1.044 | 0.2964 |  |
| Circulatory disease | -0.0294 | 2.2772 | ±4.5544 | -0.013 | 0.9897 |  |
| Avg. daily mean/SD | -0.3291 | 0.5221 | ±1.0442 | -0.630 | 0.5284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **598**, R² = **0.1063**, Adj R² = **0.0896**, F-statistic = **6.34** (p = **5.91e-10**), Residual SE = **16.914** on **586** df, AIC = **5091.4**, BIC = **5144.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.2653** | 7.9535 | ±15.9070 | **+4.685** | **2.79e-06** | *** |
| **Education: graduate level (vs college)** | **-3.6596** | 1.5266 | ±3.0532 | **-2.397** | **0.0165** | * |
| Education: high school or below (vs college) | -1.2932 | 2.4911 | ±4.9822 | -0.519 | 0.6037 |  |
| Site: UCSD (vs UAB) | +0.8896 | 1.9052 | ±3.8103 | +0.467 | 0.6406 |  |
| Site: UW (vs UAB) | -1.5543 | 1.7508 | ±3.5015 | -0.888 | 0.3747 |  |
| **Age (years)** | **-0.1830** | 0.0709 | ±0.1419 | **-2.580** | **0.0099** | ** |
| **BMI (kg/m2)** | **+0.6041** | 0.1432 | ±0.2865 | **+4.217** | **2.47e-05** | *** |
| Hypertension | +0.9187 | 1.6938 | ±3.3877 | +0.542 | 0.5875 |  |
| High cholesterol | -1.4763 | 1.4709 | ±2.9418 | -1.004 | 0.3155 |  |
| Kidney disease | +2.9511 | 3.0194 | ±6.0388 | +0.977 | 0.3284 |  |
| Circulatory disease | +0.0826 | 2.2772 | ±4.5544 | +0.036 | 0.9711 |  |
| MAG (mg/dL/h) | +0.1772 | 0.1128 | ±0.2256 | +1.571 | 0.1161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **598**, R² = **0.1054**, Adj R² = **0.0886**, F-statistic = **6.28** (p = **7.75e-10**), Residual SE = **16.923** on **586** df, AIC = **5092.0**, BIC = **5144.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.2665** | 8.1535 | ±16.3070 | **+4.693** | **2.69e-06** | *** |
| **Education: graduate level (vs college)** | **-3.6707** | 1.5314 | ±3.0629 | **-2.397** | **0.0165** | * |
| Education: high school or below (vs college) | -1.0660 | 2.4564 | ±4.9129 | -0.434 | 0.6643 |  |
| Site: UCSD (vs UAB) | +0.9210 | 1.9089 | ±3.8177 | +0.482 | 0.6295 |  |
| Site: UW (vs UAB) | -1.7000 | 1.7528 | ±3.5056 | -0.970 | 0.3321 |  |
| **Age (years)** | **-0.1922** | 0.0716 | ±0.1433 | **-2.683** | **0.0073** | ** |
| **BMI (kg/m2)** | **+0.6088** | 0.1464 | ±0.2927 | **+4.159** | **3.19e-05** | *** |
| Hypertension | +0.7305 | 1.6969 | ±3.3937 | +0.430 | 0.6668 |  |
| High cholesterol | -1.4443 | 1.4754 | ±2.9509 | -0.979 | 0.3276 |  |
| Kidney disease | +3.0215 | 3.0178 | ±6.0355 | +1.001 | 0.3167 |  |
| Circulatory disease | -0.0995 | 2.2672 | ±4.5344 | -0.044 | 0.9650 |  |
| Avg. daily range (mg/dL) | +0.0658 | 0.0448 | ±0.0897 | +1.468 | 0.1421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **598**, R² = **0.1094**, Adj R² = **0.0927**, F-statistic = **6.54** (p = **2.47e-10**), Residual SE = **16.885** on **586** df, AIC = **5089.3**, BIC = **5142.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.4232** | 7.1385 | ±14.2771 | **+5.663** | **1.49e-08** | *** |
| **Education: graduate level (vs college)** | **-3.7098** | 1.5250 | ±3.0501 | **-2.433** | **0.0150** | * |
| Education: high school or below (vs college) | -0.9104 | 2.4456 | ±4.8911 | -0.372 | 0.7097 |  |
| Site: UCSD (vs UAB) | +0.8978 | 1.8944 | ±3.7889 | +0.474 | 0.6356 |  |
| Site: UW (vs UAB) | -1.6281 | 1.7386 | ±3.4772 | -0.936 | 0.3491 |  |
| **Age (years)** | **-0.1822** | 0.0704 | ±0.1409 | **-2.587** | **0.0097** | ** |
| **BMI (kg/m2)** | **+0.5776** | 0.1431 | ±0.2861 | **+4.037** | **5.41e-05** | *** |
| Hypertension | +0.7716 | 1.6729 | ±3.3457 | +0.461 | 0.6446 |  |
| High cholesterol | -1.6631 | 1.4656 | ±2.9312 | -1.135 | 0.2565 |  |
| Kidney disease | +3.2357 | 2.9368 | ±5.8736 | +1.102 | 0.2706 |  |
| Circulatory disease | -0.0987 | 2.2419 | ±4.4838 | -0.044 | 0.9649 |  |
| **SD of daily means (mg/dL)** | **+0.7015** | 0.3317 | ±0.6633 | **+2.115** | **0.0344** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **598**, R² = **0.1027**, Adj R² = **0.0859**, F-statistic = **6.10** (p = **1.65e-09**), Residual SE = **16.948** on **586** df, AIC = **5093.8**, BIC = **5146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0354** | 22.8572 | ±45.7144 | **+2.758** | **0.0058** | ** |
| **Education: graduate level (vs college)** | **-3.7053** | 1.5338 | ±3.0676 | **-2.416** | **0.0157** | * |
| Education: high school or below (vs college) | -0.9027 | 2.4616 | ±4.9232 | -0.367 | 0.7138 |  |
| Site: UCSD (vs UAB) | +0.8534 | 1.9064 | ±3.8127 | +0.448 | 0.6544 |  |
| Site: UW (vs UAB) | -1.6105 | 1.7602 | ±3.5204 | -0.915 | 0.3602 |  |
| **Age (years)** | **-0.1868** | 0.0714 | ±0.1428 | **-2.617** | **0.0089** | ** |
| **BMI (kg/m2)** | **+0.5993** | 0.1459 | ±0.2919 | **+4.106** | **4.02e-05** | *** |
| Hypertension | +0.7701 | 1.6893 | ±3.3786 | +0.456 | 0.6485 |  |
| High cholesterol | -1.5436 | 1.4761 | ±2.9521 | -1.046 | 0.2957 |  |
| Kidney disease | +3.1326 | 3.0132 | ±6.0264 | +1.040 | 0.2985 |  |
| Circulatory disease | -0.1625 | 2.2661 | ±4.5322 | -0.072 | 0.9428 |  |
| Time in range 70-180, pooled (%) | -0.1931 | 0.2090 | ±0.4180 | -0.924 | 0.3556 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **598**, R² = **0.1025**, Adj R² = **0.0857**, F-statistic = **6.09** (p = **1.75e-09**), Residual SE = **16.950** on **586** df, AIC = **5093.9**, BIC = **5146.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.2265** | 23.6192 | ±47.2384 | **+2.592** | **0.0095** | ** |
| **Education: graduate level (vs college)** | **-3.7082** | 1.5339 | ±3.0677 | **-2.418** | **0.0156** | * |
| Education: high school or below (vs college) | -0.8969 | 2.4627 | ±4.9255 | -0.364 | 0.7157 |  |
| Site: UCSD (vs UAB) | +0.8485 | 1.9064 | ±3.8128 | +0.445 | 0.6563 |  |
| Site: UW (vs UAB) | -1.5978 | 1.7593 | ±3.5186 | -0.908 | 0.3638 |  |
| **Age (years)** | **-0.1862** | 0.0714 | ±0.1427 | **-2.610** | **0.0091** | ** |
| **BMI (kg/m2)** | **+0.5988** | 0.1461 | ±0.2922 | **+4.099** | **4.16e-05** | *** |
| Hypertension | +0.7751 | 1.6898 | ±3.3796 | +0.459 | 0.6465 |  |
| High cholesterol | -1.5375 | 1.4762 | ±2.9523 | -1.042 | 0.2976 |  |
| Kidney disease | +3.1353 | 3.0162 | ±6.0325 | +1.039 | 0.2986 |  |
| Circulatory disease | -0.1639 | 2.2694 | ±4.5387 | -0.072 | 0.9424 |  |
| Avg. daily time in range 70-180 (%) | -0.1747 | 0.2160 | ±0.4319 | -0.809 | 0.4184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.94e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.5064** | 7.2961 | ±14.5923 | **+6.100** | **1.06e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9748** | 1.5514 | ±3.1027 | **-2.562** | **0.0104** | * |
| Education: high school or below (vs college) | -1.2306 | 2.4697 | ±4.9393 | -0.498 | 0.6183 |  |
| Site: UCSD (vs UAB) | +0.9415 | 1.8982 | ±3.7964 | +0.496 | 0.6199 |  |
| Site: UW (vs UAB) | -1.5723 | 1.7537 | ±3.5074 | -0.897 | 0.3700 |  |
| **Age (years)** | **-0.1858** | 0.0708 | ±0.1416 | **-2.625** | **0.0087** | ** |
| **BMI (kg/m2)** | **+0.5997** | 0.1467 | ±0.2934 | **+4.088** | **4.35e-05** | *** |
| Hypertension | +0.8033 | 1.6844 | ±3.3689 | +0.477 | 0.6335 |  |
| High cholesterol | -1.4351 | 1.4751 | ±2.9503 | -0.973 | 0.3306 |  |
| Kidney disease | +3.0873 | 3.0220 | ±6.0441 | +1.022 | 0.3070 |  |
| Circulatory disease | -0.1611 | 2.2759 | ±4.5517 | -0.071 | 0.9436 |  |
| Time 54-69, pooled (%) | -1.9359 | 1.2716 | ±2.5432 | -1.522 | 0.1279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.97e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.4174** | 7.2873 | ±14.5747 | **+6.095** | **1.09e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9844** | 1.5540 | ±3.1080 | **-2.564** | **0.0103** | * |
| Education: high school or below (vs college) | -1.2521 | 2.4719 | ±4.9438 | -0.507 | 0.6125 |  |
| Site: UCSD (vs UAB) | +0.9841 | 1.8977 | ±3.7954 | +0.519 | 0.6040 |  |
| Site: UW (vs UAB) | -1.5592 | 1.7535 | ±3.5070 | -0.889 | 0.3739 |  |
| **Age (years)** | **-0.1851** | 0.0707 | ±0.1415 | **-2.617** | **0.0089** | ** |
| **BMI (kg/m2)** | **+0.5999** | 0.1468 | ±0.2936 | **+4.087** | **4.38e-05** | *** |
| Hypertension | +0.7921 | 1.6848 | ±3.3696 | +0.470 | 0.6382 |  |
| High cholesterol | -1.4439 | 1.4750 | ±2.9500 | -0.979 | 0.3276 |  |
| Kidney disease | +3.0901 | 3.0222 | ±6.0445 | +1.022 | 0.3066 |  |
| Circulatory disease | -0.1897 | 2.2758 | ±4.5517 | -0.083 | 0.9336 |  |
| Avg. daily time 54-69 (%) | -1.8763 | 1.2846 | ±2.5691 | -1.461 | 0.1441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.94e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.5064** | 7.2961 | ±14.5923 | **+6.100** | **1.06e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9748** | 1.5514 | ±3.1027 | **-2.562** | **0.0104** | * |
| Education: high school or below (vs college) | -1.2306 | 2.4697 | ±4.9393 | -0.498 | 0.6183 |  |
| Site: UCSD (vs UAB) | +0.9415 | 1.8982 | ±3.7964 | +0.496 | 0.6199 |  |
| Site: UW (vs UAB) | -1.5723 | 1.7537 | ±3.5074 | -0.897 | 0.3700 |  |
| **Age (years)** | **-0.1858** | 0.0708 | ±0.1416 | **-2.625** | **0.0087** | ** |
| **BMI (kg/m2)** | **+0.5997** | 0.1467 | ±0.2934 | **+4.088** | **4.35e-05** | *** |
| Hypertension | +0.8033 | 1.6844 | ±3.3689 | +0.477 | 0.6335 |  |
| High cholesterol | -1.4351 | 1.4751 | ±2.9503 | -0.973 | 0.3306 |  |
| Kidney disease | +3.0873 | 3.0220 | ±6.0441 | +1.022 | 0.3070 |  |
| Circulatory disease | -0.1611 | 2.2759 | ±4.5517 | -0.071 | 0.9436 |  |
| Time < 70 (%) | -1.9359 | 1.2716 | ±2.5432 | -1.522 | 0.1279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.97e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.4174** | 7.2873 | ±14.5747 | **+6.095** | **1.09e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9844** | 1.5540 | ±3.1080 | **-2.564** | **0.0103** | * |
| Education: high school or below (vs college) | -1.2521 | 2.4719 | ±4.9438 | -0.507 | 0.6125 |  |
| Site: UCSD (vs UAB) | +0.9841 | 1.8977 | ±3.7954 | +0.519 | 0.6040 |  |
| Site: UW (vs UAB) | -1.5592 | 1.7535 | ±3.5070 | -0.889 | 0.3739 |  |
| **Age (years)** | **-0.1851** | 0.0707 | ±0.1415 | **-2.617** | **0.0089** | ** |
| **BMI (kg/m2)** | **+0.5999** | 0.1468 | ±0.2936 | **+4.087** | **4.38e-05** | *** |
| Hypertension | +0.7921 | 1.6848 | ±3.3696 | +0.470 | 0.6382 |  |
| High cholesterol | -1.4439 | 1.4750 | ±2.9500 | -0.979 | 0.3276 |  |
| Kidney disease | +3.0901 | 3.0222 | ±6.0445 | +1.022 | 0.3066 |  |
| Circulatory disease | -0.1897 | 2.2758 | ±4.5517 | -0.083 | 0.9336 |  |
| Avg. daily time < 70 (%) | -1.8763 | 1.2846 | ±2.5691 | -1.461 | 0.1441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **598**, R² = **0.1036**, Adj R² = **0.0867**, F-statistic = **6.15** (p = **1.31e-09**), Residual SE = **16.940** on **586** df, AIC = **5093.2**, BIC = **5146.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8191** | 7.2316 | ±14.4631 | **+6.059** | **1.37e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7377** | 1.5307 | ±3.0614 | **-2.442** | **0.0146** | * |
| Education: high school or below (vs college) | -0.9232 | 2.4592 | ±4.9183 | -0.375 | 0.7074 |  |
| Site: UCSD (vs UAB) | +0.9124 | 1.9037 | ±3.8075 | +0.479 | 0.6317 |  |
| Site: UW (vs UAB) | -1.6304 | 1.7609 | ±3.5219 | -0.926 | 0.3545 |  |
| **Age (years)** | **-0.1885** | 0.0714 | ±0.1427 | **-2.642** | **0.0083** | ** |
| **BMI (kg/m2)** | **+0.5974** | 0.1457 | ±0.2914 | **+4.100** | **4.14e-05** | *** |
| Hypertension | +0.7729 | 1.6896 | ±3.3792 | +0.457 | 0.6474 |  |
| High cholesterol | -1.5641 | 1.4758 | ±2.9517 | -1.060 | 0.2892 |  |
| Kidney disease | +3.0987 | 3.0109 | ±6.0217 | +1.029 | 0.3034 |  |
| Circulatory disease | -0.2084 | 2.2633 | ±4.5266 | -0.092 | 0.9266 |  |
| Time 181-250, pooled (%) | +0.2662 | 0.2140 | ±0.4280 | +1.244 | 0.2136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **598**, R² = **0.1033**, Adj R² = **0.0865**, F-statistic = **6.14** (p = **1.40e-09**), Residual SE = **16.942** on **586** df, AIC = **5093.4**, BIC = **5146.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8431** | 7.2278 | ±14.4556 | **+6.066** | **1.31e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7419** | 1.5306 | ±3.0611 | **-2.445** | **0.0145** | * |
| Education: high school or below (vs college) | -0.9133 | 2.4591 | ±4.9182 | -0.371 | 0.7103 |  |
| Site: UCSD (vs UAB) | +0.9179 | 1.9034 | ±3.8069 | +0.482 | 0.6297 |  |
| Site: UW (vs UAB) | -1.6140 | 1.7596 | ±3.5192 | -0.917 | 0.3590 |  |
| **Age (years)** | **-0.1878** | 0.0713 | ±0.1426 | **-2.633** | **0.0085** | ** |
| **BMI (kg/m2)** | **+0.5964** | 0.1457 | ±0.2915 | **+4.093** | **4.26e-05** | *** |
| Hypertension | +0.7784 | 1.6900 | ±3.3801 | +0.461 | 0.6451 |  |
| High cholesterol | -1.5620 | 1.4762 | ±2.9524 | -1.058 | 0.2900 |  |
| Kidney disease | +3.0990 | 3.0141 | ±6.0282 | +1.028 | 0.3039 |  |
| Circulatory disease | -0.2212 | 2.2661 | ±4.5322 | -0.098 | 0.9222 |  |
| Avg. daily time 181-250 (%) | +0.2547 | 0.2197 | ±0.4394 | +1.159 | 0.2463 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **598**, R² = **0.1036**, Adj R² = **0.0867**, F-statistic = **6.15** (p = **1.31e-09**), Residual SE = **16.940** on **586** df, AIC = **5093.2**, BIC = **5146.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8191** | 7.2316 | ±14.4631 | **+6.059** | **1.37e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7377** | 1.5307 | ±3.0614 | **-2.442** | **0.0146** | * |
| Education: high school or below (vs college) | -0.9232 | 2.4592 | ±4.9183 | -0.375 | 0.7074 |  |
| Site: UCSD (vs UAB) | +0.9124 | 1.9037 | ±3.8075 | +0.479 | 0.6317 |  |
| Site: UW (vs UAB) | -1.6304 | 1.7609 | ±3.5219 | -0.926 | 0.3545 |  |
| **Age (years)** | **-0.1885** | 0.0714 | ±0.1427 | **-2.642** | **0.0083** | ** |
| **BMI (kg/m2)** | **+0.5974** | 0.1457 | ±0.2914 | **+4.100** | **4.14e-05** | *** |
| Hypertension | +0.7729 | 1.6896 | ±3.3792 | +0.457 | 0.6474 |  |
| High cholesterol | -1.5641 | 1.4758 | ±2.9517 | -1.060 | 0.2892 |  |
| Kidney disease | +3.0987 | 3.0109 | ±6.0217 | +1.029 | 0.3034 |  |
| Circulatory disease | -0.2084 | 2.2633 | ±4.5266 | -0.092 | 0.9266 |  |
| Time > 180 (%) | +0.2662 | 0.2140 | ±0.4280 | +1.244 | 0.2136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **598**, R² = **0.1033**, Adj R² = **0.0865**, F-statistic = **6.14** (p = **1.40e-09**), Residual SE = **16.942** on **586** df, AIC = **5093.4**, BIC = **5146.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8431** | 7.2278 | ±14.4556 | **+6.066** | **1.31e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7419** | 1.5306 | ±3.0611 | **-2.445** | **0.0145** | * |
| Education: high school or below (vs college) | -0.9133 | 2.4591 | ±4.9182 | -0.371 | 0.7103 |  |
| Site: UCSD (vs UAB) | +0.9179 | 1.9034 | ±3.8069 | +0.482 | 0.6297 |  |
| Site: UW (vs UAB) | -1.6140 | 1.7596 | ±3.5192 | -0.917 | 0.3590 |  |
| **Age (years)** | **-0.1878** | 0.0713 | ±0.1426 | **-2.633** | **0.0085** | ** |
| **BMI (kg/m2)** | **+0.5964** | 0.1457 | ±0.2915 | **+4.093** | **4.26e-05** | *** |
| Hypertension | +0.7784 | 1.6900 | ±3.3801 | +0.461 | 0.6451 |  |
| High cholesterol | -1.5620 | 1.4762 | ±2.9524 | -1.058 | 0.2900 |  |
| Kidney disease | +3.0990 | 3.0141 | ±6.0282 | +1.028 | 0.3039 |  |
| Circulatory disease | -0.2212 | 2.2661 | ±4.5322 | -0.098 | 0.9222 |  |
| Avg. daily time > 180 (%) | +0.2547 | 0.2197 | ±0.4394 | +1.159 | 0.2463 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **598**, R² = **0.1035**, Adj R² = **0.0867**, F-statistic = **6.15** (p = **1.33e-09**), Residual SE = **16.941** on **586** df, AIC = **5093.3**, BIC = **5146.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8282** | 7.2185 | ±14.4370 | **+6.072** | **1.27e-09** | *** |
| **Education: graduate level (vs college)** | **-3.6894** | 1.5306 | ±3.0613 | **-2.410** | **0.0159** | * |
| Education: high school or below (vs college) | -1.0457 | 2.4612 | ±4.9224 | -0.425 | 0.6709 |  |
| Site: UCSD (vs UAB) | +0.8445 | 1.8973 | ±3.7946 | +0.445 | 0.6563 |  |
| Site: UW (vs UAB) | -1.6268 | 1.7560 | ±3.5120 | -0.926 | 0.3542 |  |
| **Age (years)** | **-0.1810** | 0.0707 | ±0.1413 | **-2.561** | **0.0104** | * |
| **BMI (kg/m2)** | **+0.5899** | 0.1464 | ±0.2928 | **+4.029** | **5.60e-05** | *** |
| Hypertension | +0.8148 | 1.6872 | ±3.3743 | +0.483 | 0.6292 |  |
| High cholesterol | -1.6446 | 1.4794 | ±2.9588 | -1.112 | 0.2663 |  |
| Kidney disease | +3.2047 | 3.0076 | ±6.0152 | +1.066 | 0.2866 |  |
| Circulatory disease | -0.0822 | 2.2608 | ±4.5216 | -0.036 | 0.9710 |  |
| Nocturnal time > 180 (%) | +0.2272 | 0.1646 | ±0.3292 | +1.380 | 0.1676 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
