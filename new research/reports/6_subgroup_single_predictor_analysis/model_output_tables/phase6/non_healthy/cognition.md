# Phase 6 model output tables - All (analysis base) - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 867; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0819**, F-statistic = **8.73** (p = **1.04e-13**), Residual SE = **3.271** on **856** df, AIC = **4526.2**, BIC = **4578.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5163** | 0.9809 | ±1.9617 | **+29.073** | **7.97e-186** | *** |
| **Education: graduate level (vs college)** | **+1.0578** | 0.2362 | ±0.4724 | **+4.478** | **7.53e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5898** | 0.4017 | ±0.8033 | **-3.958** | **7.56e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5729** | 0.2722 | ±0.5445 | **-2.104** | **0.0353** | * |
| Site: UW (vs UAB) | -0.3199 | 0.2863 | ±0.5726 | -1.117 | 0.2639 |  |
| **Age (years)** | **-0.0512** | 0.0122 | ±0.0244 | **-4.191** | **2.78e-05** | *** |
| BMI (kg/m2) | -0.0042 | 0.0156 | ±0.0311 | -0.272 | 0.7856 |  |
| **Hypertension** | **-0.5943** | 0.2545 | ±0.5090 | **-2.335** | **0.0195** | * |
| High cholesterol | +0.4922 | 0.2517 | ±0.5035 | +1.955 | 0.0506 | . |
| Kidney disease | +0.3460 | 0.3294 | ±0.6589 | +1.050 | 0.2936 |  |
| Circulatory disease | +0.3985 | 0.2662 | ±0.5324 | +1.497 | 0.1344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **867**, R² = **0.0962**, Adj R² = **0.0846**, F-statistic = **8.27** (p = **6.65e-14**), Residual SE = **3.266** on **855** df, AIC = **4524.7**, BIC = **4581.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5086** | 1.1164 | ±2.2328 | **+26.432** | **5.95e-154** | *** |
| **Education: graduate level (vs college)** | **+1.0178** | 0.2368 | ±0.4736 | **+4.298** | **1.72e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5237** | 0.4051 | ±0.8101 | **-3.762** | **1.69e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.5981** | 0.2734 | ±0.5468 | **-2.188** | **0.0287** | * |
| Site: UW (vs UAB) | -0.3417 | 0.2862 | ±0.5725 | -1.194 | 0.2326 |  |
| **Age (years)** | **-0.0503** | 0.0122 | ±0.0244 | **-4.129** | **3.65e-05** | *** |
| BMI (kg/m2) | -0.0018 | 0.0158 | ±0.0315 | -0.111 | 0.9113 |  |
| **Hypertension** | **-0.5919** | 0.2546 | ±0.5093 | **-2.325** | **0.0201** | * |
| High cholesterol | +0.4918 | 0.2515 | ±0.5029 | +1.956 | 0.0505 | . |
| Kidney disease | +0.3565 | 0.3292 | ±0.6584 | +1.083 | 0.2789 |  |
| Circulatory disease | +0.4044 | 0.2652 | ±0.5303 | +1.525 | 0.1273 |  |
| **HbA1c (%)** | **-0.1651** | 0.0838 | ±0.1676 | **-1.970** | **0.0488** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **867**, R² = **0.0984**, Adj R² = **0.0868**, F-statistic = **8.48** (p = **2.63e-14**), Residual SE = **3.262** on **855** df, AIC = **4522.6**, BIC = **4579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4286** | 1.0367 | ±2.0734 | **+28.387** | **2.90e-177** | *** |
| **Education: graduate level (vs college)** | **+1.0156** | 0.2355 | ±0.4711 | **+4.312** | **1.62e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5199** | 0.4044 | ±0.8088 | **-3.758** | **1.71e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6142** | 0.2733 | ±0.5466 | **-2.247** | **0.0246** | * |
| Site: UW (vs UAB) | -0.3392 | 0.2856 | ±0.5712 | -1.188 | 0.2350 |  |
| **Age (years)** | **-0.0500** | 0.0123 | ±0.0245 | **-4.072** | **4.66e-05** | *** |
| BMI (kg/m2) | -0.0030 | 0.0157 | ±0.0315 | -0.192 | 0.8474 |  |
| **Hypertension** | **-0.6066** | 0.2546 | ±0.5092 | **-2.383** | **0.0172** | * |
| High cholesterol | +0.4782 | 0.2511 | ±0.5023 | +1.904 | 0.0569 | . |
| Kidney disease | +0.4037 | 0.3307 | ±0.6614 | +1.221 | 0.2222 |  |
| Circulatory disease | +0.4058 | 0.2636 | ±0.5272 | +1.539 | 0.1237 |  |
| **Mean glucose (mg/dL)** | **-0.0065** | 0.0028 | ±0.0056 | **-2.313** | **0.0207** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **867**, R² = **0.0984**, Adj R² = **0.0868**, F-statistic = **8.48** (p = **2.63e-14**), Residual SE = **3.262** on **855** df, AIC = **4522.6**, BIC = **4579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3248** | 1.2174 | ±2.4348 | **+24.910** | **5.83e-137** | *** |
| **Education: graduate level (vs college)** | **+1.0156** | 0.2355 | ±0.4711 | **+4.312** | **1.62e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5199** | 0.4044 | ±0.8088 | **-3.758** | **1.71e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6142** | 0.2733 | ±0.5466 | **-2.247** | **0.0246** | * |
| Site: UW (vs UAB) | -0.3392 | 0.2856 | ±0.5712 | -1.188 | 0.2350 |  |
| **Age (years)** | **-0.0500** | 0.0123 | ±0.0245 | **-4.072** | **4.66e-05** | *** |
| BMI (kg/m2) | -0.0030 | 0.0157 | ±0.0315 | -0.192 | 0.8474 |  |
| **Hypertension** | **-0.6066** | 0.2546 | ±0.5092 | **-2.383** | **0.0172** | * |
| High cholesterol | +0.4782 | 0.2511 | ±0.5023 | +1.904 | 0.0569 | . |
| Kidney disease | +0.4037 | 0.3307 | ±0.6614 | +1.221 | 0.2222 |  |
| Circulatory disease | +0.4058 | 0.2636 | ±0.5272 | +1.539 | 0.1237 |  |
| **GMI (%)** | **-0.2708** | 0.1171 | ±0.2342 | **-2.313** | **0.0207** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **867**, R² = **0.0987**, Adj R² = **0.0871**, F-statistic = **8.51** (p = **2.25e-14**), Residual SE = **3.262** on **855** df, AIC = **4522.3**, BIC = **4579.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4436** | 1.0374 | ±2.0748 | **+28.383** | **3.31e-177** | *** |
| **Education: graduate level (vs college)** | **+1.0148** | 0.2350 | ±0.4701 | **+4.318** | **1.58e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5216** | 0.4040 | ±0.8079 | **-3.767** | **1.65e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6132** | 0.2734 | ±0.5467 | **-2.243** | **0.0249** | * |
| Site: UW (vs UAB) | -0.3253 | 0.2855 | ±0.5710 | -1.139 | 0.2545 |  |
| **Age (years)** | **-0.0513** | 0.0122 | ±0.0245 | **-4.194** | **2.74e-05** | *** |
| BMI (kg/m2) | -0.0015 | 0.0158 | ±0.0316 | -0.093 | 0.9261 |  |
| **Hypertension** | **-0.6127** | 0.2545 | ±0.5089 | **-2.408** | **0.0160** | * |
| High cholesterol | +0.4819 | 0.2511 | ±0.5023 | +1.919 | 0.0550 | . |
| Kidney disease | +0.3855 | 0.3288 | ±0.6575 | +1.172 | 0.2410 |  |
| Circulatory disease | +0.4065 | 0.2637 | ±0.5273 | +1.542 | 0.1232 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0066** | 0.0028 | ±0.0055 | **-2.369** | **0.0178** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **867**, R² = **0.1022**, Adj R² = **0.0906**, F-statistic = **8.85** (p = **5.07e-15**), Residual SE = **3.255** on **855** df, AIC = **4518.9**, BIC = **4576.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.1966** | 0.9869 | ±1.9738 | **+29.584** | **2.42e-192** | *** |
| **Education: graduate level (vs college)** | **+0.9946** | 0.2356 | ±0.4712 | **+4.222** | **2.42e-05** | *** |
| **Education: high school or below (vs college)** | **-1.4852** | 0.4005 | ±0.8010 | **-3.708** | **2.09e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6256** | 0.2725 | ±0.5449 | **-2.296** | **0.0217** | * |
| Site: UW (vs UAB) | -0.3765 | 0.2866 | ±0.5731 | -1.314 | 0.1888 |  |
| **Age (years)** | **-0.0478** | 0.0125 | ±0.0249 | **-3.831** | **1.27e-04** | *** |
| BMI (kg/m2) | -0.0042 | 0.0158 | ±0.0315 | -0.266 | 0.7904 |  |
| **Hypertension** | **-0.6013** | 0.2540 | ±0.5080 | **-2.367** | **0.0179** | * |
| High cholesterol | +0.4658 | 0.2505 | ±0.5009 | +1.860 | 0.0629 | . |
| Kidney disease | +0.5080 | 0.3289 | ±0.6578 | +1.544 | 0.1225 |  |
| Circulatory disease | +0.4152 | 0.2634 | ±0.5268 | +1.576 | 0.1150 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0250** | 0.0081 | ±0.0162 | **-3.085** | **0.0020** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **867**, R² = **0.1012**, Adj R² = **0.0896**, F-statistic = **8.75** (p = **7.74e-15**), Residual SE = **3.257** on **855** df, AIC = **4519.9**, BIC = **4577.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2048** | 0.9852 | ±1.9704 | **+29.643** | **4.13e-193** | *** |
| **Education: graduate level (vs college)** | **+1.0023** | 0.2360 | ±0.4719 | **+4.248** | **2.16e-05** | *** |
| **Education: high school or below (vs college)** | **-1.4828** | 0.4010 | ±0.8021 | **-3.697** | **2.18e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6200** | 0.2722 | ±0.5444 | **-2.278** | **0.0227** | * |
| Site: UW (vs UAB) | -0.3668 | 0.2866 | ±0.5731 | -1.280 | 0.2005 |  |
| **Age (years)** | **-0.0476** | 0.0125 | ±0.0250 | **-3.804** | **1.42e-04** | *** |
| BMI (kg/m2) | -0.0056 | 0.0157 | ±0.0314 | -0.355 | 0.7230 |  |
| **Hypertension** | **-0.6048** | 0.2543 | ±0.5086 | **-2.378** | **0.0174** | * |
| High cholesterol | +0.4673 | 0.2508 | ±0.5015 | +1.863 | 0.0624 | . |
| Kidney disease | +0.5051 | 0.3301 | ±0.6601 | +1.530 | 0.1259 |  |
| Circulatory disease | +0.4071 | 0.2638 | ±0.5277 | +1.543 | 0.1228 |  |
| **Avg. daily SD (mg/dL)** | **-0.0272** | 0.0094 | ±0.0189 | **-2.877** | **0.0040** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **867**, R² = **0.0971**, Adj R² = **0.0855**, F-statistic = **8.36** (p = **4.45e-14**), Residual SE = **3.264** on **855** df, AIC = **4523.8**, BIC = **4581.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2741** | 0.9968 | ±1.9935 | **+29.369** | **1.37e-189** | *** |
| **Education: graduate level (vs college)** | **+1.0269** | 0.2358 | ±0.4716 | **+4.355** | **1.33e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5318** | 0.3994 | ±0.7989 | **-3.835** | **1.26e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.5992** | 0.2722 | ±0.5444 | **-2.201** | **0.0277** | * |
| Site: UW (vs UAB) | -0.3644 | 0.2880 | ±0.5759 | -1.265 | 0.2058 |  |
| **Age (years)** | **-0.0481** | 0.0125 | ±0.0250 | **-3.844** | **1.21e-04** | *** |
| BMI (kg/m2) | -0.0052 | 0.0156 | ±0.0312 | -0.332 | 0.7402 |  |
| **Hypertension** | **-0.5862** | 0.2538 | ±0.5076 | **-2.309** | **0.0209** | * |
| High cholesterol | +0.4759 | 0.2512 | ±0.5024 | +1.894 | 0.0582 | . |
| Kidney disease | +0.4638 | 0.3270 | ±0.6541 | +1.418 | 0.1561 |  |
| Circulatory disease | +0.4116 | 0.2662 | ±0.5323 | +1.546 | 0.1220 |  |
| **CV (%)** | **-0.0410** | 0.0178 | ±0.0356 | **-2.306** | **0.0211** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **867**, R² = **0.0999**, Adj R² = **0.0883**, F-statistic = **8.63** (p = **1.36e-14**), Residual SE = **3.259** on **855** df, AIC = **4521.1**, BIC = **4578.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.1672** | 1.1316 | ±2.2632 | **+24.008** | **2.31e-127** | *** |
| **Education: graduate level (vs college)** | **+1.0192** | 0.2353 | ±0.4706 | **+4.331** | **1.48e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5094** | 0.3984 | ±0.7969 | **-3.788** | **1.52e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.5954** | 0.2711 | ±0.5422 | **-2.196** | **0.0281** | * |
| Site: UW (vs UAB) | -0.3697 | 0.2868 | ±0.5735 | -1.289 | 0.1973 |  |
| **Age (years)** | **-0.0470** | 0.0125 | ±0.0250 | **-3.765** | **1.66e-04** | *** |
| BMI (kg/m2) | -0.0053 | 0.0156 | ±0.0312 | -0.342 | 0.7327 |  |
| **Hypertension** | **-0.5847** | 0.2534 | ±0.5068 | **-2.308** | **0.0210** | * |
| High cholesterol | +0.4766 | 0.2509 | ±0.5017 | +1.900 | 0.0574 | . |
| Kidney disease | +0.4657 | 0.3265 | ±0.6530 | +1.426 | 0.1538 |  |
| Circulatory disease | +0.4231 | 0.2658 | ±0.5317 | +1.592 | 0.1115 |  |
| **Mean / SD ratio** | **+0.2329** | 0.0797 | ±0.1593 | **+2.923** | **0.0035** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **867**, R² = **0.0970**, Adj R² = **0.0853**, F-statistic = **8.34** (p = **4.81e-14**), Residual SE = **3.265** on **855** df, AIC = **4524.0**, BIC = **4581.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5158** | 1.1299 | ±2.2597 | **+24.353** | **5.35e-131** | *** |
| **Education: graduate level (vs college)** | **+1.0260** | 0.2363 | ±0.4727 | **+4.341** | **1.42e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5316** | 0.3993 | ±0.7986 | **-3.836** | **1.25e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.5753** | 0.2710 | ±0.5419 | **-2.123** | **0.0337** | * |
| Site: UW (vs UAB) | -0.3514 | 0.2869 | ±0.5739 | -1.225 | 0.2207 |  |
| **Age (years)** | **-0.0477** | 0.0125 | ±0.0250 | **-3.807** | **1.40e-04** | *** |
| BMI (kg/m2) | -0.0061 | 0.0156 | ±0.0312 | -0.394 | 0.6937 |  |
| **Hypertension** | **-0.5857** | 0.2538 | ±0.5076 | **-2.308** | **0.0210** | * |
| High cholesterol | +0.4795 | 0.2514 | ±0.5028 | +1.907 | 0.0565 | . |
| Kidney disease | +0.4255 | 0.3275 | ±0.6550 | +1.299 | 0.1939 |  |
| Circulatory disease | +0.4008 | 0.2662 | ±0.5323 | +1.506 | 0.1321 |  |
| **Avg. daily mean/SD** | **+0.1509** | 0.0704 | ±0.1407 | **+2.144** | **0.0321** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **867**, R² = **0.0987**, Adj R² = **0.0871**, F-statistic = **8.52** (p = **2.23e-14**), Residual SE = **3.261** on **855** df, AIC = **4522.3**, BIC = **4579.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8017** | 1.0678 | ±2.1355 | **+27.911** | **1.98e-171** | *** |
| **Education: graduate level (vs college)** | **+1.0079** | 0.2383 | ±0.4766 | **+4.230** | **2.34e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5369** | 0.3984 | ±0.7968 | **-3.858** | **1.14e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6045** | 0.2722 | ±0.5444 | **-2.221** | **0.0264** | * |
| Site: UW (vs UAB) | -0.3974 | 0.2886 | ±0.5772 | -1.377 | 0.1685 |  |
| **Age (years)** | **-0.0518** | 0.0122 | ±0.0245 | **-4.233** | **2.31e-05** | *** |
| BMI (kg/m2) | -0.0039 | 0.0156 | ±0.0313 | -0.249 | 0.8037 |  |
| **Hypertension** | **-0.6092** | 0.2552 | ±0.5103 | **-2.387** | **0.0170** | * |
| High cholesterol | +0.4820 | 0.2518 | ±0.5037 | +1.914 | 0.0556 | . |
| Kidney disease | +0.4173 | 0.3357 | ±0.6714 | +1.243 | 0.2138 |  |
| Circulatory disease | +0.3987 | 0.2652 | ±0.5305 | +1.503 | 0.1328 |  |
| **MAG (mg/dL/h)** | **-0.0282** | 0.0120 | ±0.0241 | **-2.343** | **0.0191** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **867**, R² = **0.0998**, Adj R² = **0.0882**, F-statistic = **8.62** (p = **1.42e-14**), Residual SE = **3.260** on **855** df, AIC = **4521.2**, BIC = **4578.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4070** | 0.9984 | ±1.9968 | **+29.454** | **1.11e-190** | *** |
| **Education: graduate level (vs college)** | **+1.0026** | 0.2364 | ±0.4728 | **+4.241** | **2.23e-05** | *** |
| **Education: high school or below (vs college)** | **-1.4970** | 0.4014 | ±0.8028 | **-3.729** | **1.92e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6212** | 0.2725 | ±0.5450 | **-2.280** | **0.0226** | * |
| Site: UW (vs UAB) | -0.3623 | 0.2869 | ±0.5738 | -1.263 | 0.2067 |  |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0250 | **-3.873** | **1.07e-04** | *** |
| BMI (kg/m2) | -0.0063 | 0.0157 | ±0.0313 | -0.400 | 0.6890 |  |
| **Hypertension** | **-0.6167** | 0.2552 | ±0.5104 | **-2.417** | **0.0157** | * |
| High cholesterol | +0.4774 | 0.2513 | ±0.5026 | +1.900 | 0.0575 | . |
| Kidney disease | +0.4878 | 0.3301 | ±0.6602 | +1.478 | 0.1394 |  |
| Circulatory disease | +0.4102 | 0.2644 | ±0.5288 | +1.552 | 0.1207 |  |
| **Avg. daily range (mg/dL)** | **-0.0070** | 0.0027 | ±0.0055 | **-2.548** | **0.0108** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **867**, R² = **0.1017**, Adj R² = **0.0901**, F-statistic = **8.80** (p = **6.26e-15**), Residual SE = **3.256** on **855** df, AIC = **4519.4**, BIC = **4576.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.9231** | 0.9857 | ±1.9713 | **+29.344** | **2.85e-189** | *** |
| **Education: graduate level (vs college)** | **+0.9828** | 0.2353 | ±0.4705 | **+4.177** | **2.95e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5340** | 0.3975 | ±0.7950 | **-3.859** | **1.14e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6102** | 0.2725 | ±0.5451 | **-2.239** | **0.0252** | * |
| Site: UW (vs UAB) | -0.3739 | 0.2870 | ±0.5740 | -1.303 | 0.1926 |  |
| **Age (years)** | **-0.0510** | 0.0123 | ±0.0245 | **-4.159** | **3.20e-05** | *** |
| BMI (kg/m2) | -0.0015 | 0.0157 | ±0.0315 | -0.097 | 0.9227 |  |
| **Hypertension** | **-0.5812** | 0.2534 | ±0.5068 | **-2.294** | **0.0218** | * |
| High cholesterol | +0.4806 | 0.2503 | ±0.5005 | +1.920 | 0.0548 | . |
| Kidney disease | +0.4429 | 0.3281 | ±0.6562 | +1.350 | 0.1770 |  |
| Circulatory disease | +0.4536 | 0.2650 | ±0.5299 | +1.712 | 0.0869 | . |
| **SD of daily means (mg/dL)** | **-0.0409** | 0.0137 | ±0.0274 | **-2.990** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **867**, R² = **0.0977**, Adj R² = **0.0861**, F-statistic = **8.42** (p = **3.46e-14**), Residual SE = **3.263** on **855** df, AIC = **4523.2**, BIC = **4580.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.6532** | 1.0844 | ±2.1688 | **+25.501** | **1.93e-143** | *** |
| **Education: graduate level (vs college)** | **+1.0164** | 0.2358 | ±0.4716 | **+4.311** | **1.63e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5176** | 0.4041 | ±0.8082 | **-3.755** | **1.73e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6274** | 0.2749 | ±0.5499 | **-2.282** | **0.0225** | * |
| Site: UW (vs UAB) | -0.3437 | 0.2861 | ±0.5723 | -1.201 | 0.2296 |  |
| **Age (years)** | **-0.0494** | 0.0123 | ±0.0246 | **-4.012** | **6.01e-05** | *** |
| BMI (kg/m2) | -0.0028 | 0.0157 | ±0.0315 | -0.179 | 0.8579 |  |
| **Hypertension** | **-0.6163** | 0.2549 | ±0.5099 | **-2.418** | **0.0156** | * |
| High cholesterol | +0.4712 | 0.2511 | ±0.5022 | +1.877 | 0.0606 | . |
| Kidney disease | +0.4105 | 0.3300 | ±0.6599 | +1.244 | 0.2134 |  |
| Circulatory disease | +0.4111 | 0.2638 | ±0.5277 | +1.558 | 0.1192 |  |
| **Time in range 70-180, pooled (%)** | **+0.0098** | 0.0045 | ±0.0091 | **+2.170** | **0.0300** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **867**, R² = **0.0974**, Adj R² = **0.0858**, F-statistic = **8.39** (p = **3.94e-14**), Residual SE = **3.264** on **855** df, AIC = **4523.5**, BIC = **4580.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.6743** | 1.0862 | ±2.1724 | **+25.477** | **3.50e-143** | *** |
| **Education: graduate level (vs college)** | **+1.0189** | 0.2359 | ±0.4717 | **+4.320** | **1.56e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5175** | 0.4045 | ±0.8089 | **-3.752** | **1.76e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6275** | 0.2752 | ±0.5503 | **-2.281** | **0.0226** | * |
| Site: UW (vs UAB) | -0.3429 | 0.2863 | ±0.5725 | -1.198 | 0.2309 |  |
| **Age (years)** | **-0.0494** | 0.0123 | ±0.0246 | **-4.009** | **6.11e-05** | *** |
| BMI (kg/m2) | -0.0028 | 0.0157 | ±0.0315 | -0.179 | 0.8581 |  |
| **Hypertension** | **-0.6162** | 0.2550 | ±0.5101 | **-2.416** | **0.0157** | * |
| High cholesterol | +0.4723 | 0.2511 | ±0.5023 | +1.881 | 0.0600 | . |
| Kidney disease | +0.4109 | 0.3299 | ±0.6598 | +1.246 | 0.2129 |  |
| Circulatory disease | +0.4107 | 0.2639 | ±0.5278 | +1.556 | 0.1196 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0095** | 0.0045 | ±0.0091 | **+2.098** | **0.0359** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **867**, R² = **0.0927**, Adj R² = **0.0810**, F-statistic = **7.94** (p = **2.94e-13**), Residual SE = **3.272** on **855** df, AIC = **4528.0**, BIC = **4585.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4706** | 0.9955 | ±1.9909 | **+28.600** | **6.66e-180** | *** |
| **Education: graduate level (vs college)** | **+1.0580** | 0.2364 | ±0.4728 | **+4.475** | **7.63e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5833** | 0.4055 | ±0.8111 | **-3.904** | **9.45e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5641** | 0.2745 | ±0.5490 | **-2.055** | **0.0399** | * |
| Site: UW (vs UAB) | -0.3100 | 0.2917 | ±0.5833 | -1.063 | 0.2878 |  |
| **Age (years)** | **-0.0508** | 0.0123 | ±0.0246 | **-4.129** | **3.64e-05** | *** |
| BMI (kg/m2) | -0.0046 | 0.0156 | ±0.0312 | -0.296 | 0.7673 |  |
| **Hypertension** | **-0.6002** | 0.2545 | ±0.5090 | **-2.358** | **0.0184** | * |
| **High cholesterol** | **+0.4980** | 0.2519 | ±0.5038 | **+1.977** | **0.0480** | * |
| Kidney disease | +0.3486 | 0.3290 | ±0.6579 | +1.060 | 0.2893 |  |
| Circulatory disease | +0.3916 | 0.2674 | ±0.5348 | +1.464 | 0.1431 |  |
| Any reading < 54 during wear (0/1) | +0.1107 | 0.2623 | ±0.5247 | +0.422 | 0.6731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0809**, F-statistic = **7.93** (p = **3.14e-13**), Residual SE = **3.273** on **855** df, AIC = **4528.2**, BIC = **4585.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5089** | 0.9821 | ±1.9643 | **+29.027** | **2.99e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0592** | 0.2366 | ±0.4732 | **+4.476** | **7.59e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5863** | 0.4025 | ±0.8051 | **-3.941** | **8.13e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5676** | 0.2743 | ±0.5485 | **-2.069** | **0.0385** | * |
| Site: UW (vs UAB) | -0.3137 | 0.2896 | ±0.5792 | -1.083 | 0.2787 |  |
| **Age (years)** | **-0.0511** | 0.0122 | ±0.0244 | **-4.183** | **2.88e-05** | *** |
| BMI (kg/m2) | -0.0043 | 0.0157 | ±0.0313 | -0.278 | 0.7812 |  |
| **Hypertension** | **-0.5956** | 0.2550 | ±0.5100 | **-2.336** | **0.0195** | * |
| High cholesterol | +0.4931 | 0.2522 | ±0.5045 | +1.955 | 0.0506 | . |
| Kidney disease | +0.3475 | 0.3292 | ±0.6585 | +1.055 | 0.2912 |  |
| Circulatory disease | +0.3946 | 0.2670 | ±0.5341 | +1.478 | 0.1395 |  |
| Time < 54 (%) | +0.0537 | 0.4076 | ±0.8152 | +0.132 | 0.8953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0808**, F-statistic = **7.92** (p = **3.20e-13**), Residual SE = **3.273** on **855** df, AIC = **4528.2**, BIC = **4585.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5162** | 0.9815 | ±1.9631 | **+29.052** | **1.44e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0578** | 0.2364 | ±0.4728 | **+4.474** | **7.67e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5897** | 0.4022 | ±0.8045 | **-3.952** | **7.74e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5728** | 0.2735 | ±0.5469 | **-2.095** | **0.0362** | * |
| Site: UW (vs UAB) | -0.3198 | 0.2879 | ±0.5758 | -1.111 | 0.2667 |  |
| **Age (years)** | **-0.0512** | 0.0122 | ±0.0244 | **-4.190** | **2.79e-05** | *** |
| BMI (kg/m2) | -0.0042 | 0.0156 | ±0.0312 | -0.272 | 0.7860 |  |
| **Hypertension** | **-0.5943** | 0.2547 | ±0.5095 | **-2.333** | **0.0196** | * |
| High cholesterol | +0.4922 | 0.2523 | ±0.5045 | +1.951 | 0.0510 | . |
| Kidney disease | +0.3460 | 0.3295 | ±0.6590 | +1.050 | 0.2937 |  |
| Circulatory disease | +0.3984 | 0.2668 | ±0.5336 | +1.493 | 0.1353 |  |
| Avg. daily time < 54 (%) | +0.0011 | 0.3139 | ±0.6277 | +0.003 | 0.9973 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0808**, F-statistic = **7.92** (p = **3.19e-13**), Residual SE = **3.273** on **855** df, AIC = **4528.2**, BIC = **4585.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5174** | 0.9834 | ±1.9667 | **+29.000** | **6.55e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0570** | 0.2373 | ±0.4747 | **+4.453** | **8.46e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5898** | 0.4022 | ±0.8044 | **-3.953** | **7.72e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5743** | 0.2745 | ±0.5491 | **-2.092** | **0.0364** | * |
| Site: UW (vs UAB) | -0.3212 | 0.2883 | ±0.5765 | -1.114 | 0.2651 |  |
| **Age (years)** | **-0.0511** | 0.0122 | ±0.0244 | **-4.188** | **2.81e-05** | *** |
| BMI (kg/m2) | -0.0042 | 0.0156 | ±0.0312 | -0.270 | 0.7869 |  |
| **Hypertension** | **-0.5940** | 0.2549 | ±0.5098 | **-2.330** | **0.0198** | * |
| High cholesterol | +0.4920 | 0.2519 | ±0.5039 | +1.953 | 0.0508 | . |
| Kidney disease | +0.3460 | 0.3297 | ±0.6595 | +1.049 | 0.2940 |  |
| Circulatory disease | +0.3992 | 0.2666 | ±0.5333 | +1.497 | 0.1344 |  |
| Time 54-69, pooled (%) | -0.0054 | 0.0823 | ±0.1646 | -0.066 | 0.9472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0808**, F-statistic = **7.92** (p = **3.19e-13**), Residual SE = **3.273** on **855** df, AIC = **4528.2**, BIC = **4585.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5165** | 0.9825 | ±1.9649 | **+29.026** | **3.11e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0568** | 0.2376 | ±0.4751 | **+4.449** | **8.65e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5897** | 0.4022 | ±0.8043 | **-3.953** | **7.72e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5743** | 0.2744 | ±0.5489 | **-2.093** | **0.0364** | * |
| Site: UW (vs UAB) | -0.3214 | 0.2882 | ±0.5764 | -1.115 | 0.2649 |  |
| **Age (years)** | **-0.0511** | 0.0122 | ±0.0244 | **-4.188** | **2.82e-05** | *** |
| BMI (kg/m2) | -0.0042 | 0.0156 | ±0.0312 | -0.270 | 0.7871 |  |
| **Hypertension** | **-0.5940** | 0.2550 | ±0.5099 | **-2.330** | **0.0198** | * |
| High cholesterol | +0.4919 | 0.2520 | ±0.5039 | +1.952 | 0.0509 | . |
| Kidney disease | +0.3459 | 0.3297 | ±0.6593 | +1.049 | 0.2941 |  |
| Circulatory disease | +0.3991 | 0.2665 | ±0.5331 | +1.497 | 0.1343 |  |
| Avg. daily time 54-69 (%) | -0.0061 | 0.0828 | ±0.1656 | -0.073 | 0.9417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0808**, F-statistic = **7.92** (p = **3.20e-13**), Residual SE = **3.273** on **855** df, AIC = **4528.2**, BIC = **4585.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5166** | 0.9833 | ±1.9666 | **+29.000** | **6.54e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0576** | 0.2372 | ±0.4745 | **+4.458** | **8.26e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5898** | 0.4023 | ±0.8046 | **-3.952** | **7.76e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5732** | 0.2747 | ±0.5493 | **-2.087** | **0.0369** | * |
| Site: UW (vs UAB) | -0.3202 | 0.2886 | ±0.5771 | -1.109 | 0.2672 |  |
| **Age (years)** | **-0.0512** | 0.0122 | ±0.0244 | **-4.189** | **2.80e-05** | *** |
| BMI (kg/m2) | -0.0042 | 0.0156 | ±0.0312 | -0.271 | 0.7861 |  |
| **Hypertension** | **-0.5942** | 0.2550 | ±0.5099 | **-2.331** | **0.0198** | * |
| High cholesterol | +0.4921 | 0.2519 | ±0.5039 | +1.953 | 0.0508 | . |
| Kidney disease | +0.3460 | 0.3296 | ±0.6592 | +1.050 | 0.2939 |  |
| Circulatory disease | +0.3986 | 0.2667 | ±0.5334 | +1.495 | 0.1350 |  |
| Time < 70 (%) | -0.0008 | 0.0680 | ±0.1360 | -0.012 | 0.9906 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **867**, R² = **0.0925**, Adj R² = **0.0808**, F-statistic = **7.92** (p = **3.20e-13**), Residual SE = **3.273** on **855** df, AIC = **4528.2**, BIC = **4585.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5167** | 0.9824 | ±1.9648 | **+29.027** | **3.01e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0570** | 0.2374 | ±0.4747 | **+4.453** | **8.47e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5899** | 0.4022 | ±0.8044 | **-3.953** | **7.72e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5742** | 0.2744 | ±0.5489 | **-2.092** | **0.0364** | * |
| Site: UW (vs UAB) | -0.3213 | 0.2883 | ±0.5766 | -1.114 | 0.2651 |  |
| **Age (years)** | **-0.0511** | 0.0122 | ±0.0244 | **-4.189** | **2.80e-05** | *** |
| BMI (kg/m2) | -0.0042 | 0.0156 | ±0.0312 | -0.270 | 0.7869 |  |
| **Hypertension** | **-0.5940** | 0.2550 | ±0.5099 | **-2.330** | **0.0198** | * |
| High cholesterol | +0.4919 | 0.2519 | ±0.5039 | +1.952 | 0.0509 | . |
| Kidney disease | +0.3459 | 0.3296 | ±0.6592 | +1.049 | 0.2940 |  |
| Circulatory disease | +0.3992 | 0.2665 | ±0.5331 | +1.498 | 0.1342 |  |
| Avg. daily time < 70 (%) | -0.0041 | 0.0663 | ±0.1326 | -0.062 | 0.9509 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **867**, R² = **0.0961**, Adj R² = **0.0845**, F-statistic = **8.27** (p = **6.84e-14**), Residual SE = **3.266** on **855** df, AIC = **4524.8**, BIC = **4581.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2887** | 1.1886 | ±2.3773 | **+22.958** | **1.23e-116** | *** |
| **Education: graduate level (vs college)** | **+1.0190** | 0.2364 | ±0.4728 | **+4.310** | **1.63e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5381** | 0.4045 | ±0.8091 | **-3.802** | **1.43e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6090** | 0.2735 | ±0.5470 | **-2.226** | **0.0260** | * |
| Site: UW (vs UAB) | -0.3586 | 0.2872 | ±0.5744 | -1.249 | 0.2118 |  |
| **Age (years)** | **-0.0517** | 0.0122 | ±0.0244 | **-4.231** | **2.33e-05** | *** |
| BMI (kg/m2) | -0.0035 | 0.0157 | ±0.0315 | -0.219 | 0.8265 |  |
| **Hypertension** | **-0.5910** | 0.2546 | ±0.5092 | **-2.321** | **0.0203** | * |
| High cholesterol | +0.4819 | 0.2512 | ±0.5024 | +1.918 | 0.0551 | . |
| Kidney disease | +0.3845 | 0.3312 | ±0.6624 | +1.161 | 0.2456 |  |
| Circulatory disease | +0.4070 | 0.2644 | ±0.5289 | +1.539 | 0.1238 |  |
| Time 54-250, pooled (%) | +0.0135 | 0.0075 | ±0.0149 | +1.809 | 0.0704 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **867**, R² = **0.0960**, Adj R² = **0.0844**, F-statistic = **8.25** (p = **7.24e-14**), Residual SE = **3.266** on **855** df, AIC = **4524.9**, BIC = **4582.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2849** | 1.2005 | ±2.4010 | **+22.728** | **2.35e-114** | *** |
| **Education: graduate level (vs college)** | **+1.0200** | 0.2364 | ±0.4729 | **+4.314** | **1.60e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5392** | 0.4044 | ±0.8088 | **-3.806** | **1.41e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6087** | 0.2737 | ±0.5474 | **-2.224** | **0.0261** | * |
| Site: UW (vs UAB) | -0.3565 | 0.2872 | ±0.5743 | -1.241 | 0.2145 |  |
| **Age (years)** | **-0.0515** | 0.0122 | ±0.0244 | **-4.216** | **2.48e-05** | *** |
| BMI (kg/m2) | -0.0034 | 0.0157 | ±0.0315 | -0.219 | 0.8268 |  |
| **Hypertension** | **-0.5921** | 0.2546 | ±0.5093 | **-2.325** | **0.0201** | * |
| High cholesterol | +0.4820 | 0.2512 | ±0.5024 | +1.919 | 0.0550 | . |
| Kidney disease | +0.3865 | 0.3312 | ±0.6625 | +1.167 | 0.2433 |  |
| Circulatory disease | +0.4082 | 0.2645 | ±0.5290 | +1.544 | 0.1227 |  |
| Avg. daily time 54-250 (%) | +0.0134 | 0.0076 | ±0.0153 | +1.757 | 0.0789 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **867**, R² = **0.0959**, Adj R² = **0.0843**, F-statistic = **8.24** (p = **7.56e-14**), Residual SE = **3.267** on **855** df, AIC = **4525.0**, BIC = **4582.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5553** | 0.9798 | ±1.9595 | **+29.145** | **9.67e-187** | *** |
| **Education: graduate level (vs college)** | **+1.0424** | 0.2358 | ±0.4716 | **+4.420** | **9.85e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5441** | 0.4027 | ±0.8054 | **-3.835** | **1.26e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6068** | 0.2741 | ±0.5483 | **-2.214** | **0.0269** | * |
| Site: UW (vs UAB) | -0.3108 | 0.2860 | ±0.5721 | -1.086 | 0.2773 |  |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0250 | **-3.865** | **1.11e-04** | *** |
| BMI (kg/m2) | -0.0032 | 0.0156 | ±0.0313 | -0.203 | 0.8395 |  |
| **Hypertension** | **-0.6270** | 0.2561 | ±0.5122 | **-2.449** | **0.0143** | * |
| High cholesterol | +0.4748 | 0.2517 | ±0.5035 | +1.886 | 0.0593 | . |
| Kidney disease | +0.3942 | 0.3283 | ±0.6566 | +1.201 | 0.2298 |  |
| Circulatory disease | +0.4052 | 0.2651 | ±0.5301 | +1.529 | 0.1263 |  |
| Time 181-250, pooled (%) | -0.0130 | 0.0076 | ±0.0152 | -1.713 | 0.0866 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **867**, R² = **0.0957**, Adj R² = **0.0840**, F-statistic = **8.22** (p = **8.38e-14**), Residual SE = **3.267** on **855** df, AIC = **4525.2**, BIC = **4582.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5569** | 0.9802 | ±1.9604 | **+29.133** | **1.37e-186** | *** |
| **Education: graduate level (vs college)** | **+1.0441** | 0.2359 | ±0.4718 | **+4.426** | **9.58e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5428** | 0.4032 | ±0.8063 | **-3.827** | **1.30e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6078** | 0.2743 | ±0.5485 | **-2.216** | **0.0267** | * |
| Site: UW (vs UAB) | -0.3130 | 0.2862 | ±0.5723 | -1.094 | 0.2740 |  |
| **Age (years)** | **-0.0486** | 0.0125 | ±0.0250 | **-3.890** | **1.00e-04** | *** |
| BMI (kg/m2) | -0.0032 | 0.0157 | ±0.0313 | -0.202 | 0.8395 |  |
| **Hypertension** | **-0.6251** | 0.2560 | ±0.5120 | **-2.442** | **0.0146** | * |
| High cholesterol | +0.4762 | 0.2517 | ±0.5035 | +1.892 | 0.0585 | . |
| Kidney disease | +0.3932 | 0.3283 | ±0.6566 | +1.198 | 0.2310 |  |
| Circulatory disease | +0.4041 | 0.2651 | ±0.5302 | +1.524 | 0.1274 |  |
| Avg. daily time 181-250 (%) | -0.0123 | 0.0075 | ±0.0150 | -1.649 | 0.0992 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **867**, R² = **0.0976**, Adj R² = **0.0860**, F-statistic = **8.41** (p = **3.64e-14**), Residual SE = **3.264** on **855** df, AIC = **4523.4**, BIC = **4580.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6318** | 0.9807 | ±1.9614 | **+29.195** | **2.23e-187** | *** |
| **Education: graduate level (vs college)** | **+1.0190** | 0.2357 | ±0.4714 | **+4.323** | **1.54e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5186** | 0.4043 | ±0.8086 | **-3.756** | **1.73e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6227** | 0.2745 | ±0.5490 | **-2.268** | **0.0233** | * |
| Site: UW (vs UAB) | -0.3396 | 0.2860 | ±0.5720 | -1.188 | 0.2350 |  |
| **Age (years)** | **-0.0495** | 0.0123 | ±0.0246 | **-4.020** | **5.82e-05** | *** |
| BMI (kg/m2) | -0.0029 | 0.0157 | ±0.0315 | -0.185 | 0.8531 |  |
| **Hypertension** | **-0.6164** | 0.2550 | ±0.5100 | **-2.417** | **0.0156** | * |
| High cholesterol | +0.4722 | 0.2511 | ±0.5023 | +1.880 | 0.0601 | . |
| Kidney disease | +0.4093 | 0.3298 | ±0.6596 | +1.241 | 0.2146 |  |
| Circulatory disease | +0.4088 | 0.2638 | ±0.5277 | +1.550 | 0.1212 |  |
| **Time > 180 (%)** | **-0.0096** | 0.0045 | ±0.0090 | **-2.143** | **0.0321** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **867**, R² = **0.0973**, Adj R² = **0.0857**, F-statistic = **8.38** (p = **4.15e-14**), Residual SE = **3.264** on **855** df, AIC = **4523.6**, BIC = **4580.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6218** | 0.9813 | ±1.9627 | **+29.166** | **5.22e-187** | *** |
| **Education: graduate level (vs college)** | **+1.0216** | 0.2358 | ±0.4716 | **+4.333** | **1.47e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5188** | 0.4046 | ±0.8092 | **-3.754** | **1.74e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6233** | 0.2747 | ±0.5495 | **-2.269** | **0.0233** | * |
| Site: UW (vs UAB) | -0.3393 | 0.2861 | ±0.5722 | -1.186 | 0.2357 |  |
| **Age (years)** | **-0.0495** | 0.0123 | ±0.0246 | **-4.020** | **5.83e-05** | *** |
| BMI (kg/m2) | -0.0029 | 0.0157 | ±0.0315 | -0.184 | 0.8539 |  |
| **Hypertension** | **-0.6162** | 0.2551 | ±0.5102 | **-2.416** | **0.0157** | * |
| High cholesterol | +0.4734 | 0.2512 | ±0.5023 | +1.885 | 0.0595 | . |
| Kidney disease | +0.4098 | 0.3298 | ±0.6596 | +1.243 | 0.2140 |  |
| Circulatory disease | +0.4088 | 0.2639 | ±0.5278 | +1.549 | 0.1213 |  |
| **Avg. daily time > 180 (%)** | **-0.0093** | 0.0045 | ±0.0090 | **-2.071** | **0.0384** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **867**, R² = **0.0979**, Adj R² = **0.0862**, F-statistic = **8.43** (p = **3.27e-14**), Residual SE = **3.263** on **855** df, AIC = **4523.1**, BIC = **4580.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6146** | 0.9811 | ±1.9622 | **+29.166** | **5.31e-187** | *** |
| **Education: graduate level (vs college)** | **+1.0087** | 0.2352 | ±0.4704 | **+4.289** | **1.80e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5225** | 0.4037 | ±0.8073 | **-3.772** | **1.62e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6301** | 0.2750 | ±0.5499 | **-2.291** | **0.0219** | * |
| Site: UW (vs UAB) | -0.3359 | 0.2858 | ±0.5715 | -1.176 | 0.2398 |  |
| **Age (years)** | **-0.0507** | 0.0122 | ±0.0245 | **-4.143** | **3.42e-05** | *** |
| BMI (kg/m2) | -0.0012 | 0.0158 | ±0.0316 | -0.075 | 0.9406 |  |
| **Hypertension** | **-0.6197** | 0.2544 | ±0.5089 | **-2.436** | **0.0149** | * |
| High cholesterol | +0.4691 | 0.2513 | ±0.5025 | +1.867 | 0.0619 | . |
| Kidney disease | +0.4015 | 0.3280 | ±0.6560 | +1.224 | 0.2209 |  |
| Circulatory disease | +0.4128 | 0.2637 | ±0.5275 | +1.565 | 0.1176 |  |
| **Nocturnal time > 180 (%)** | **-0.0094** | 0.0044 | ±0.0087 | **-2.162** | **0.0306** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **867**, R² = **0.0961**, Adj R² = **0.0844**, F-statistic = **8.26** (p = **7.03e-14**), Residual SE = **3.266** on **855** df, AIC = **4524.8**, BIC = **4582.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6467** | 0.9726 | ±1.9453 | **+29.453** | **1.16e-190** | *** |
| **Education: graduate level (vs college)** | **+1.0166** | 0.2349 | ±0.4698 | **+4.328** | **1.50e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5643** | 0.4020 | ±0.8040 | **-3.891** | **9.98e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.5926** | 0.2721 | ±0.5442 | **-2.178** | **0.0294** | * |
| Site: UW (vs UAB) | -0.3023 | 0.2867 | ±0.5733 | -1.055 | 0.2916 |  |
| **Age (years)** | **-0.0477** | 0.0127 | ±0.0254 | **-3.755** | **1.73e-04** | *** |
| BMI (kg/m2) | -0.0057 | 0.0155 | ±0.0310 | -0.366 | 0.7143 |  |
| **Hypertension** | **-0.6131** | 0.2560 | ±0.5120 | **-2.395** | **0.0166** | * |
| High cholesterol | +0.4853 | 0.2520 | ±0.5040 | +1.926 | 0.0541 | . |
| Kidney disease | +0.4012 | 0.3281 | ±0.6561 | +1.223 | 0.2214 |  |
| Circulatory disease | +0.3893 | 0.2654 | ±0.5309 | +1.467 | 0.1425 |  |
| Any reading > 250 during wear (0/1) | -0.4363 | 0.2307 | ±0.4614 | -1.892 | 0.0585 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **867**, R² = **0.0961**, Adj R² = **0.0845**, F-statistic = **8.27** (p = **6.80e-14**), Residual SE = **3.266** on **855** df, AIC = **4524.8**, BIC = **4581.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6380** | 0.9869 | ±1.9737 | **+29.019** | **3.74e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0194** | 0.2364 | ±0.4728 | **+4.312** | **1.62e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5372** | 0.4046 | ±0.8092 | **-3.799** | **1.45e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6077** | 0.2734 | ±0.5468 | **-2.222** | **0.0263** | * |
| Site: UW (vs UAB) | -0.3571 | 0.2871 | ±0.5742 | -1.244 | 0.2136 |  |
| **Age (years)** | **-0.0517** | 0.0122 | ±0.0244 | **-4.230** | **2.34e-05** | *** |
| BMI (kg/m2) | -0.0035 | 0.0157 | ±0.0315 | -0.221 | 0.8250 |  |
| **Hypertension** | **-0.5914** | 0.2546 | ±0.5093 | **-2.323** | **0.0202** | * |
| High cholesterol | +0.4821 | 0.2512 | ±0.5024 | +1.919 | 0.0550 | . |
| Kidney disease | +0.3849 | 0.3311 | ±0.6623 | +1.162 | 0.2451 |  |
| Circulatory disease | +0.4060 | 0.2645 | ±0.5289 | +1.535 | 0.1247 |  |
| Time > 250 (%) | -0.0135 | 0.0075 | ±0.0149 | -1.811 | 0.0702 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 867)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **867**, R² = **0.0960**, Adj R² = **0.0844**, F-statistic = **8.25** (p = **7.26e-14**), Residual SE = **3.266** on **855** df, AIC = **4524.9**, BIC = **4582.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6242** | 0.9868 | ±1.9736 | **+29.007** | **5.30e-185** | *** |
| **Education: graduate level (vs college)** | **+1.0206** | 0.2364 | ±0.4728 | **+4.317** | **1.58e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5385** | 0.4045 | ±0.8090 | **-3.804** | **1.43e-04** | *** |
| **Site: UCSD (vs UAB)** | **-0.6076** | 0.2736 | ±0.5472 | **-2.221** | **0.0264** | * |
| Site: UW (vs UAB) | -0.3552 | 0.2871 | ±0.5742 | -1.237 | 0.2160 |  |
| **Age (years)** | **-0.0515** | 0.0122 | ±0.0244 | **-4.217** | **2.47e-05** | *** |
| BMI (kg/m2) | -0.0035 | 0.0157 | ±0.0315 | -0.220 | 0.8260 |  |
| **Hypertension** | **-0.5924** | 0.2546 | ±0.5093 | **-2.326** | **0.0200** | * |
| High cholesterol | +0.4824 | 0.2512 | ±0.5024 | +1.920 | 0.0548 | . |
| Kidney disease | +0.3867 | 0.3312 | ±0.6625 | +1.167 | 0.2431 |  |
| Circulatory disease | +0.4074 | 0.2645 | ±0.5290 | +1.540 | 0.1235 |  |
| Avg. daily time > 250 (%) | -0.0134 | 0.0076 | ±0.0153 | -1.755 | 0.0793 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 867; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0538**, LLR χ² = **64.58** (p = **4.87e-10**), AUC = **0.6603**, AIC = **1158.4**, BIC = **1210.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0287** | 0.6346 | ±1.2692 | **-3.197** | **0.0014** | 0.1315 | ** |
| **Education: graduate level (vs college)** | **-0.7389** | 0.1618 | ±0.3236 | **-4.567** | **4.95e-06** | 0.4776 | *** |
| **Education: high school or below (vs college)** | **+0.6590** | 0.2087 | ±0.4173 | **+3.158** | **0.0016** | 1.9329 | ** |
| **Site: UCSD (vs UAB)** | **+0.3766** | 0.1753 | ±0.3506 | **+2.148** | **0.0317** | 1.4573 | * |
| Site: UW (vs UAB) | +0.0218 | 0.1765 | ±0.3529 | +0.124 | 0.9016 | 1.0221 |  |
| **Age (years)** | **+0.0280** | 0.0073 | ±0.0146 | **+3.839** | **1.24e-04** | 1.0284 | *** |
| BMI (kg/m2) | +0.0113 | 0.0102 | ±0.0205 | +1.104 | 0.2697 | 1.0114 |  |
| Hypertension | +0.1943 | 0.1619 | ±0.3237 | +1.200 | 0.2300 | 1.2145 |  |
| High cholesterol | -0.2467 | 0.1518 | ±0.3035 | -1.626 | 0.1041 | 0.7814 |  |
| Kidney disease | -0.2424 | 0.1960 | ±0.3919 | -1.237 | 0.2161 | 0.7847 |  |
| Circulatory disease | -0.1786 | 0.1783 | ±0.3565 | -1.002 | 0.3163 | 0.8364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0568**, LLR χ² = **68.27** (p = **2.61e-10**), AUC = **0.6627**, AIC = **1156.7**, BIC = **1213.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.6902** | 0.7280 | ±1.4560 | **-3.695** | **2.20e-04** | 0.0679 | *** |
| **Education: graduate level (vs college)** | **-0.7165** | 0.1627 | ±0.3254 | **-4.404** | **1.06e-05** | 0.4884 | *** |
| **Education: high school or below (vs college)** | **+0.6169** | 0.2099 | ±0.4198 | **+2.939** | **0.0033** | 1.8532 | ** |
| **Site: UCSD (vs UAB)** | **+0.3929** | 0.1758 | ±0.3516 | **+2.235** | **0.0254** | 1.4812 | * |
| Site: UW (vs UAB) | +0.0363 | 0.1771 | ±0.3542 | +0.205 | 0.8377 | 1.0370 |  |
| **Age (years)** | **+0.0276** | 0.0073 | ±0.0146 | **+3.769** | **1.64e-04** | 1.0279 | *** |
| BMI (kg/m2) | +0.0098 | 0.0103 | ±0.0207 | +0.949 | 0.3425 | 1.0099 |  |
| Hypertension | +0.1944 | 0.1621 | ±0.3242 | +1.199 | 0.2304 | 1.2146 |  |
| High cholesterol | -0.2474 | 0.1521 | ±0.3042 | -1.627 | 0.1038 | 0.7808 |  |
| Kidney disease | -0.2500 | 0.1965 | ±0.3930 | -1.272 | 0.2032 | 0.7788 |  |
| Circulatory disease | -0.1833 | 0.1788 | ±0.3576 | -1.025 | 0.3053 | 0.8325 |  |
| HbA1c (%) | +0.1081 | 0.0570 | ±0.1140 | +1.896 | 0.0579 | 1.1142 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0585**, LLR χ² = **70.27** (p = **1.09e-10**), AUC = **0.6658**, AIC = **1154.7**, BIC = **1211.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.6356** | 0.6895 | ±1.3790 | **-3.823** | **1.32e-04** | 0.0717 | *** |
| **Education: graduate level (vs college)** | **-0.7168** | 0.1626 | ±0.3251 | **-4.410** | **1.04e-05** | 0.4883 | *** |
| **Education: high school or below (vs college)** | **+0.6174** | 0.2098 | ±0.4196 | **+2.942** | **0.0033** | 1.8540 | ** |
| **Site: UCSD (vs UAB)** | **+0.4040** | 0.1761 | ±0.3523 | **+2.294** | **0.0218** | 1.4978 | * |
| Site: UW (vs UAB) | +0.0333 | 0.1771 | ±0.3542 | +0.188 | 0.8509 | 1.0339 |  |
| **Age (years)** | **+0.0274** | 0.0073 | ±0.0146 | **+3.743** | **1.82e-04** | 1.0278 | *** |
| BMI (kg/m2) | +0.0107 | 0.0103 | ±0.0206 | +1.039 | 0.2990 | 1.0108 |  |
| Hypertension | +0.2050 | 0.1624 | ±0.3248 | +1.262 | 0.2069 | 1.2275 |  |
| High cholesterol | -0.2396 | 0.1523 | ±0.3046 | -1.573 | 0.1156 | 0.7869 |  |
| Kidney disease | -0.2819 | 0.1974 | ±0.3949 | -1.428 | 0.1534 | 0.7544 |  |
| Circulatory disease | -0.1863 | 0.1792 | ±0.3584 | -1.039 | 0.2986 | 0.8300 |  |
| **Mean glucose (mg/dL)** | **+0.0042** | 0.0018 | ±0.0036 | **+2.357** | **0.0184** | 1.0042 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0585**, LLR χ² = **70.27** (p = **1.09e-10**), AUC = **0.6658**, AIC = **1154.7**, BIC = **1211.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2164** | 0.8154 | ±1.6308 | **-3.945** | **7.99e-05** | 0.0401 | *** |
| **Education: graduate level (vs college)** | **-0.7168** | 0.1626 | ±0.3251 | **-4.410** | **1.04e-05** | 0.4883 | *** |
| **Education: high school or below (vs college)** | **+0.6174** | 0.2098 | ±0.4196 | **+2.942** | **0.0033** | 1.8540 | ** |
| **Site: UCSD (vs UAB)** | **+0.4040** | 0.1761 | ±0.3523 | **+2.294** | **0.0218** | 1.4978 | * |
| Site: UW (vs UAB) | +0.0333 | 0.1771 | ±0.3542 | +0.188 | 0.8509 | 1.0339 |  |
| **Age (years)** | **+0.0274** | 0.0073 | ±0.0146 | **+3.743** | **1.82e-04** | 1.0278 | *** |
| BMI (kg/m2) | +0.0107 | 0.0103 | ±0.0206 | +1.039 | 0.2990 | 1.0108 |  |
| Hypertension | +0.2050 | 0.1624 | ±0.3248 | +1.262 | 0.2069 | 1.2275 |  |
| High cholesterol | -0.2396 | 0.1523 | ±0.3046 | -1.573 | 0.1156 | 0.7869 |  |
| Kidney disease | -0.2819 | 0.1974 | ±0.3949 | -1.428 | 0.1534 | 0.7544 |  |
| Circulatory disease | -0.1863 | 0.1792 | ±0.3584 | -1.039 | 0.2986 | 0.8300 |  |
| **GMI (%)** | **+0.1755** | 0.0744 | ±0.1489 | **+2.357** | **0.0184** | 1.1918 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0587**, LLR χ² = **70.50** (p = **9.82e-11**), AUC = **0.6661**, AIC = **1154.4**, BIC = **1211.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.6434** | 0.6892 | ±1.3783 | **-3.836** | **1.25e-04** | 0.0711 | *** |
| **Education: graduate level (vs college)** | **-0.7167** | 0.1626 | ±0.3251 | **-4.408** | **1.04e-05** | 0.4884 | *** |
| **Education: high school or below (vs college)** | **+0.6194** | 0.2098 | ±0.4196 | **+2.953** | **0.0032** | 1.8578 | ** |
| **Site: UCSD (vs UAB)** | **+0.4029** | 0.1761 | ±0.3522 | **+2.288** | **0.0221** | 1.4961 | * |
| Site: UW (vs UAB) | +0.0244 | 0.1771 | ±0.3542 | +0.137 | 0.8906 | 1.0246 |  |
| **Age (years)** | **+0.0283** | 0.0073 | ±0.0146 | **+3.864** | **1.11e-04** | 1.0287 | *** |
| BMI (kg/m2) | +0.0098 | 0.0103 | ±0.0207 | +0.947 | 0.3437 | 1.0098 |  |
| Hypertension | +0.2078 | 0.1625 | ±0.3250 | +1.279 | 0.2009 | 1.2310 |  |
| High cholesterol | -0.2423 | 0.1523 | ±0.3046 | -1.591 | 0.1117 | 0.7848 |  |
| Kidney disease | -0.2712 | 0.1972 | ±0.3943 | -1.376 | 0.1690 | 0.7625 |  |
| Circulatory disease | -0.1866 | 0.1793 | ±0.3586 | -1.041 | 0.2980 | 0.8298 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0042** | 0.0018 | ±0.0035 | **+2.401** | **0.0164** | 1.0042 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0587**, LLR χ² = **70.44** (p = **1.01e-10**), AUC = **0.6654**, AIC = **1154.5**, BIC = **1211.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4010** | 0.6590 | ±1.3179 | **-3.644** | **2.69e-04** | 0.0906 | *** |
| **Education: graduate level (vs college)** | **-0.7131** | 0.1627 | ±0.3254 | **-4.383** | **1.17e-05** | 0.4901 | *** |
| **Education: high school or below (vs college)** | **+0.6073** | 0.2101 | ±0.4201 | **+2.891** | **0.0038** | 1.8355 | ** |
| **Site: UCSD (vs UAB)** | **+0.4049** | 0.1763 | ±0.3525 | **+2.297** | **0.0216** | 1.4991 | * |
| Site: UW (vs UAB) | +0.0511 | 0.1775 | ±0.3550 | +0.288 | 0.7737 | 1.0524 |  |
| **Age (years)** | **+0.0265** | 0.0073 | ±0.0147 | **+3.610** | **3.06e-04** | 1.0269 | *** |
| BMI (kg/m2) | +0.0115 | 0.0103 | ±0.0206 | +1.115 | 0.2647 | 1.0116 |  |
| Hypertension | +0.2020 | 0.1624 | ±0.3247 | +1.244 | 0.2134 | 1.2239 |  |
| High cholesterol | -0.2354 | 0.1524 | ±0.3049 | -1.544 | 0.1226 | 0.7903 |  |
| Kidney disease | -0.3271 | 0.1998 | ±0.3996 | -1.637 | 0.1017 | 0.7210 |  |
| Circulatory disease | -0.1895 | 0.1790 | ±0.3581 | -1.058 | 0.2900 | 0.8274 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0128** | 0.0053 | ±0.0107 | **+2.399** | **0.0165** | 1.0129 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0580**, LLR χ² = **69.69** (p = **1.40e-10**), AUC = **0.6653**, AIC = **1155.3**, BIC = **1212.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.3961** | 0.6602 | ±1.3205 | **-3.629** | **2.84e-04** | 0.0911 | *** |
| **Education: graduate level (vs college)** | **-0.7169** | 0.1626 | ±0.3252 | **-4.409** | **1.04e-05** | 0.4882 | *** |
| **Education: high school or below (vs college)** | **+0.6069** | 0.2101 | ±0.4203 | **+2.888** | **0.0039** | 1.8347 | ** |
| **Site: UCSD (vs UAB)** | **+0.4019** | 0.1761 | ±0.3523 | **+2.281** | **0.0225** | 1.4946 | * |
| Site: UW (vs UAB) | +0.0452 | 0.1773 | ±0.3547 | +0.255 | 0.7988 | 1.0462 |  |
| **Age (years)** | **+0.0264** | 0.0073 | ±0.0147 | **+3.595** | **3.25e-04** | 1.0268 | *** |
| BMI (kg/m2) | +0.0122 | 0.0103 | ±0.0206 | +1.180 | 0.2382 | 1.0122 |  |
| Hypertension | +0.2034 | 0.1623 | ±0.3246 | +1.253 | 0.2102 | 1.2256 |  |
| High cholesterol | -0.2354 | 0.1523 | ±0.3047 | -1.545 | 0.1223 | 0.7903 |  |
| Kidney disease | -0.3242 | 0.1999 | ±0.3999 | -1.622 | 0.1049 | 0.7231 |  |
| Circulatory disease | -0.1846 | 0.1789 | ±0.3578 | -1.032 | 0.3022 | 0.8315 |  |
| **Avg. daily SD (mg/dL)** | **+0.0137** | 0.0061 | ±0.0122 | **+2.242** | **0.0250** | 1.0138 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0554**, LLR χ² = **66.50** (p = **5.62e-10**), AUC = **0.6624**, AIC = **1158.4**, BIC = **1215.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.3596** | 0.6815 | ±1.3630 | **-3.462** | **5.35e-04** | 0.0945 | *** |
| **Education: graduate level (vs college)** | **-0.7284** | 0.1622 | ±0.3243 | **-4.492** | **7.07e-06** | 0.4827 | *** |
| **Education: high school or below (vs college)** | **+0.6354** | 0.2095 | ±0.4189 | **+3.033** | **0.0024** | 1.8877 | ** |
| **Site: UCSD (vs UAB)** | **+0.3880** | 0.1757 | ±0.3513 | **+2.209** | **0.0272** | 1.4741 | * |
| Site: UW (vs UAB) | +0.0413 | 0.1773 | ±0.3546 | +0.233 | 0.8158 | 1.0422 |  |
| **Age (years)** | **+0.0268** | 0.0073 | ±0.0147 | **+3.653** | **2.59e-04** | 1.0272 | *** |
| BMI (kg/m2) | +0.0118 | 0.0103 | ±0.0205 | +1.145 | 0.2523 | 1.0118 |  |
| Hypertension | +0.1929 | 0.1620 | ±0.3240 | +1.191 | 0.2338 | 1.2127 |  |
| High cholesterol | -0.2405 | 0.1521 | ±0.3041 | -1.581 | 0.1138 | 0.7863 |  |
| Kidney disease | -0.2921 | 0.1994 | ±0.3988 | -1.465 | 0.1429 | 0.7467 |  |
| Circulatory disease | -0.1844 | 0.1784 | ±0.3569 | -1.034 | 0.3013 | 0.8316 |  |
| CV (%) | +0.0173 | 0.0126 | ±0.0251 | +1.381 | 0.1673 | 1.0175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0560**, LLR χ² = **67.23** (p = **4.10e-10**), AUC = **0.6629**, AIC = **1157.7**, BIC = **1214.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.5120** | 0.7099 | ±1.4198 | **-2.130** | **0.0332** | 0.2205 | * |
| **Education: graduate level (vs college)** | **-0.7271** | 0.1622 | ±0.3245 | **-4.482** | **7.40e-06** | 0.4833 | *** |
| **Education: high school or below (vs college)** | **+0.6286** | 0.2096 | ±0.4192 | **+2.999** | **0.0027** | 1.8749 | ** |
| **Site: UCSD (vs UAB)** | **+0.3861** | 0.1756 | ±0.3512 | **+2.199** | **0.0279** | 1.4712 | * |
| Site: UW (vs UAB) | +0.0416 | 0.1772 | ±0.3545 | +0.234 | 0.8146 | 1.0424 |  |
| **Age (years)** | **+0.0265** | 0.0074 | ±0.0147 | **+3.604** | **3.14e-04** | 1.0269 | *** |
| BMI (kg/m2) | +0.0118 | 0.0103 | ±0.0205 | +1.153 | 0.2491 | 1.0119 |  |
| Hypertension | +0.1928 | 0.1621 | ±0.3241 | +1.190 | 0.2341 | 1.2127 |  |
| High cholesterol | -0.2415 | 0.1521 | ±0.3042 | -1.588 | 0.1123 | 0.7855 |  |
| Kidney disease | -0.2890 | 0.1981 | ±0.3963 | -1.459 | 0.1447 | 0.7490 |  |
| Circulatory disease | -0.1881 | 0.1786 | ±0.3571 | -1.053 | 0.2922 | 0.8285 |  |
| Mean / SD ratio | -0.0918 | 0.0568 | ±0.1135 | -1.618 | 0.1057 | 0.9123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0551**, LLR χ² = **66.16** (p = **6.52e-10**), AUC = **0.6624**, AIC = **1158.8**, BIC = **1216.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.6464** | 0.7040 | ±1.4080 | **-2.339** | **0.0193** | 0.1927 | * |
| **Education: graduate level (vs college)** | **-0.7288** | 0.1622 | ±0.3243 | **-4.494** | **6.98e-06** | 0.4825 | *** |
| **Education: high school or below (vs college)** | **+0.6368** | 0.2094 | ±0.4188 | **+3.041** | **0.0024** | 1.8903 | ** |
| **Site: UCSD (vs UAB)** | **+0.3783** | 0.1754 | ±0.3508 | **+2.157** | **0.0310** | 1.4598 | * |
| Site: UW (vs UAB) | +0.0340 | 0.1770 | ±0.3540 | +0.192 | 0.8478 | 1.0346 |  |
| **Age (years)** | **+0.0267** | 0.0074 | ±0.0147 | **+3.631** | **2.82e-04** | 1.0271 | *** |
| BMI (kg/m2) | +0.0121 | 0.0103 | ±0.0206 | +1.180 | 0.2382 | 1.0122 |  |
| Hypertension | +0.1929 | 0.1620 | ±0.3239 | +1.191 | 0.2336 | 1.2128 |  |
| High cholesterol | -0.2418 | 0.1520 | ±0.3040 | -1.591 | 0.1116 | 0.7852 |  |
| Kidney disease | -0.2736 | 0.1976 | ±0.3951 | -1.385 | 0.1661 | 0.7607 |  |
| Circulatory disease | -0.1786 | 0.1784 | ±0.3567 | -1.001 | 0.3167 | 0.8364 |  |
| Avg. daily mean/SD | -0.0594 | 0.0476 | ±0.0952 | -1.248 | 0.2122 | 0.9424 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0565**, LLR χ² = **67.89** (p = **3.07e-10**), AUC = **0.6620**, AIC = **1157.1**, BIC = **1214.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.6614** | 0.7288 | ±1.4575 | **-3.652** | **2.60e-04** | 0.0699 | *** |
| **Education: graduate level (vs college)** | **-0.7193** | 0.1625 | ±0.3251 | **-4.426** | **9.61e-06** | 0.4871 | *** |
| **Education: high school or below (vs college)** | **+0.6321** | 0.2091 | ±0.4182 | **+3.023** | **0.0025** | 1.8815 | ** |
| **Site: UCSD (vs UAB)** | **+0.3932** | 0.1759 | ±0.3519 | **+2.235** | **0.0254** | 1.4817 | * |
| Site: UW (vs UAB) | +0.0601 | 0.1781 | ±0.3562 | +0.338 | 0.7356 | 1.0620 |  |
| **Age (years)** | **+0.0284** | 0.0073 | ±0.0146 | **+3.887** | **1.02e-04** | 1.0288 | *** |
| BMI (kg/m2) | +0.0112 | 0.0103 | ±0.0205 | +1.095 | 0.2736 | 1.0113 |  |
| Hypertension | +0.2042 | 0.1622 | ±0.3244 | +1.259 | 0.2080 | 1.2266 |  |
| High cholesterol | -0.2429 | 0.1521 | ±0.3043 | -1.596 | 0.1104 | 0.7844 |  |
| Kidney disease | -0.2765 | 0.1974 | ±0.3948 | -1.401 | 0.1614 | 0.7584 |  |
| Circulatory disease | -0.1795 | 0.1787 | ±0.3573 | -1.005 | 0.3149 | 0.8357 |  |
| MAG (mg/dL/h) | +0.0136 | 0.0075 | ±0.0151 | +1.806 | 0.0709 | 1.0137 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0572**, LLR χ² = **68.68** (p = **2.17e-10**), AUC = **0.6648**, AIC = **1156.3**, BIC = **1213.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4864** | 0.6786 | ±1.3573 | **-3.664** | **2.48e-04** | 0.0832 | *** |
| **Education: graduate level (vs college)** | **-0.7171** | 0.1626 | ±0.3252 | **-4.411** | **1.03e-05** | 0.4882 | *** |
| **Education: high school or below (vs college)** | **+0.6145** | 0.2099 | ±0.4198 | **+2.927** | **0.0034** | 1.8488 | ** |
| **Site: UCSD (vs UAB)** | **+0.4015** | 0.1761 | ±0.3522 | **+2.280** | **0.0226** | 1.4941 | * |
| Site: UW (vs UAB) | +0.0424 | 0.1772 | ±0.3545 | +0.239 | 0.8109 | 1.0433 |  |
| **Age (years)** | **+0.0268** | 0.0073 | ±0.0147 | **+3.663** | **2.49e-04** | 1.0272 | *** |
| BMI (kg/m2) | +0.0125 | 0.0103 | ±0.0206 | +1.210 | 0.2265 | 1.0125 |  |
| Hypertension | +0.2089 | 0.1624 | ±0.3248 | +1.286 | 0.1983 | 1.2323 |  |
| High cholesterol | -0.2404 | 0.1522 | ±0.3044 | -1.580 | 0.1141 | 0.7863 |  |
| Kidney disease | -0.3137 | 0.1996 | ±0.3992 | -1.572 | 0.1160 | 0.7307 |  |
| Circulatory disease | -0.1856 | 0.1788 | ±0.3576 | -1.038 | 0.2993 | 0.8306 |  |
| **Avg. daily range (mg/dL)** | **+0.0034** | 0.0017 | ±0.0034 | **+2.014** | **0.0440** | 1.0034 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0599**, LLR χ² = **71.89** (p = **5.33e-11**), AUC = **0.6662**, AIC = **1153.1**, BIC = **1210.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2977** | 0.6482 | ±1.2964 | **-3.545** | **3.93e-04** | 0.1005 | *** |
| **Education: graduate level (vs college)** | **-0.7025** | 0.1630 | ±0.3260 | **-4.310** | **1.63e-05** | 0.4953 | *** |
| **Education: high school or below (vs college)** | **+0.6274** | 0.2096 | ±0.4192 | **+2.993** | **0.0028** | 1.8728 | ** |
| **Site: UCSD (vs UAB)** | **+0.4009** | 0.1763 | ±0.3526 | **+2.273** | **0.0230** | 1.4931 | * |
| Site: UW (vs UAB) | +0.0560 | 0.1776 | ±0.3553 | +0.315 | 0.7526 | 1.0576 |  |
| **Age (years)** | **+0.0283** | 0.0073 | ±0.0147 | **+3.851** | **1.18e-04** | 1.0287 | *** |
| BMI (kg/m2) | +0.0098 | 0.0103 | ±0.0206 | +0.953 | 0.3407 | 1.0099 |  |
| Hypertension | +0.1913 | 0.1625 | ±0.3249 | +1.177 | 0.2390 | 1.2108 |  |
| High cholesterol | -0.2466 | 0.1527 | ±0.3053 | -1.615 | 0.1062 | 0.7814 |  |
| Kidney disease | -0.3017 | 0.1982 | ±0.3963 | -1.522 | 0.1280 | 0.7396 |  |
| Circulatory disease | -0.2137 | 0.1798 | ±0.3596 | -1.188 | 0.2347 | 0.8076 |  |
| **SD of daily means (mg/dL)** | **+0.0246** | 0.0093 | ±0.0185 | **+2.651** | **0.0080** | 1.0249 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0577**, LLR χ² = **69.28** (p = **1.67e-10**), AUC = **0.6640**, AIC = **1155.7**, BIC = **1212.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.5102** | 0.6801 | ±1.3601 | **-2.221** | **0.0264** | 0.2209 | * |
| **Education: graduate level (vs college)** | **-0.7186** | 0.1626 | ±0.3251 | **-4.420** | **9.85e-06** | 0.4874 | *** |
| **Education: high school or below (vs college)** | **+0.6166** | 0.2098 | ±0.4197 | **+2.939** | **0.0033** | 1.8526 | ** |
| **Site: UCSD (vs UAB)** | **+0.4111** | 0.1764 | ±0.3528 | **+2.330** | **0.0198** | 1.5085 | * |
| Site: UW (vs UAB) | +0.0363 | 0.1772 | ±0.3543 | +0.205 | 0.8378 | 1.0369 |  |
| **Age (years)** | **+0.0271** | 0.0073 | ±0.0146 | **+3.698** | **2.18e-04** | 1.0274 | *** |
| BMI (kg/m2) | +0.0106 | 0.0103 | ±0.0206 | +1.028 | 0.3040 | 1.0106 |  |
| Hypertension | +0.2101 | 0.1624 | ±0.3249 | +1.293 | 0.1959 | 1.2338 |  |
| High cholesterol | -0.2352 | 0.1523 | ±0.3045 | -1.545 | 0.1225 | 0.7904 |  |
| Kidney disease | -0.2844 | 0.1975 | ±0.3949 | -1.440 | 0.1498 | 0.7525 |  |
| Circulatory disease | -0.1886 | 0.1790 | ±0.3580 | -1.054 | 0.2920 | 0.8281 |  |
| **Time in range 70-180, pooled (%)** | **-0.0061** | 0.0028 | ±0.0057 | **-2.157** | **0.0310** | 0.9939 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0576**, LLR χ² = **69.21** (p = **1.72e-10**), AUC = **0.6639**, AIC = **1155.7**, BIC = **1212.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.5113** | 0.6805 | ±1.3610 | **-2.221** | **0.0264** | 0.2206 | * |
| **Education: graduate level (vs college)** | **-0.7196** | 0.1625 | ±0.3251 | **-4.428** | **9.53e-06** | 0.4869 | *** |
| **Education: high school or below (vs college)** | **+0.6155** | 0.2099 | ±0.4198 | **+2.933** | **0.0034** | 1.8506 | ** |
| **Site: UCSD (vs UAB)** | **+0.4120** | 0.1764 | ±0.3529 | **+2.335** | **0.0196** | 1.5098 | * |
| Site: UW (vs UAB) | +0.0360 | 0.1772 | ±0.3543 | +0.203 | 0.8388 | 1.0367 |  |
| **Age (years)** | **+0.0270** | 0.0073 | ±0.0146 | **+3.693** | **2.22e-04** | 1.0274 | *** |
| BMI (kg/m2) | +0.0106 | 0.0103 | ±0.0206 | +1.026 | 0.3049 | 1.0106 |  |
| Hypertension | +0.2102 | 0.1624 | ±0.3249 | +1.294 | 0.1957 | 1.2339 |  |
| High cholesterol | -0.2356 | 0.1523 | ±0.3045 | -1.547 | 0.1218 | 0.7901 |  |
| Kidney disease | -0.2857 | 0.1976 | ±0.3951 | -1.446 | 0.1481 | 0.7515 |  |
| Circulatory disease | -0.1886 | 0.1790 | ±0.3580 | -1.054 | 0.2920 | 0.8281 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0060** | 0.0028 | ±0.0056 | **-2.142** | **0.0322** | 0.9940 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0543**, LLR χ² = **65.16** (p = **1.01e-09**), AUC = **0.6621**, AIC = **1159.8**, BIC = **1217.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9792** | 0.6383 | ±1.2766 | **-3.101** | **0.0019** | 0.1382 | ** |
| **Education: graduate level (vs college)** | **-0.7401** | 0.1619 | ±0.3238 | **-4.572** | **4.83e-06** | 0.4770 | *** |
| **Education: high school or below (vs college)** | **+0.6520** | 0.2089 | ±0.4177 | **+3.121** | **0.0018** | 1.9193 | ** |
| **Site: UCSD (vs UAB)** | **+0.3674** | 0.1757 | ±0.3514 | **+2.091** | **0.0365** | 1.4440 | * |
| Site: UW (vs UAB) | +0.0107 | 0.1772 | ±0.3543 | +0.060 | 0.9519 | 1.0107 |  |
| **Age (years)** | **+0.0276** | 0.0073 | ±0.0146 | **+3.774** | **1.60e-04** | 1.0280 | *** |
| BMI (kg/m2) | +0.0117 | 0.0103 | ±0.0205 | +1.143 | 0.2531 | 1.0118 |  |
| Hypertension | +0.2010 | 0.1622 | ±0.3244 | +1.239 | 0.2154 | 1.2226 |  |
| High cholesterol | -0.2539 | 0.1521 | ±0.3042 | -1.669 | 0.0951 | 0.7758 | . |
| Kidney disease | -0.2460 | 0.1962 | ±0.3923 | -1.254 | 0.2099 | 0.7819 |  |
| Circulatory disease | -0.1711 | 0.1786 | ±0.3572 | -0.958 | 0.3379 | 0.8427 |  |
| Any reading < 54 during wear (0/1) | -0.1236 | 0.1634 | ±0.3268 | -0.756 | 0.4495 | 0.8838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0538**, LLR χ² = **64.60** (p = **1.28e-09**), AUC = **0.6601**, AIC = **1160.4**, BIC = **1217.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0313** | 0.6350 | ±1.2701 | **-3.199** | **0.0014** | 0.1312 | ** |
| **Education: graduate level (vs college)** | **-0.7384** | 0.1619 | ±0.3237 | **-4.562** | **5.07e-06** | 0.4779 | *** |
| **Education: high school or below (vs college)** | **+0.6603** | 0.2090 | ±0.4180 | **+3.160** | **0.0016** | 1.9354 | ** |
| **Site: UCSD (vs UAB)** | **+0.3784** | 0.1761 | ±0.3521 | **+2.149** | **0.0316** | 1.4599 | * |
| Site: UW (vs UAB) | +0.0239 | 0.1775 | ±0.3550 | +0.135 | 0.8927 | 1.0242 |  |
| **Age (years)** | **+0.0280** | 0.0073 | ±0.0146 | **+3.840** | **1.23e-04** | 1.0284 | *** |
| BMI (kg/m2) | +0.0113 | 0.0102 | ±0.0205 | +1.099 | 0.2716 | 1.0113 |  |
| Hypertension | +0.1938 | 0.1619 | ±0.3239 | +1.197 | 0.2314 | 1.2138 |  |
| High cholesterol | -0.2463 | 0.1518 | ±0.3036 | -1.623 | 0.1046 | 0.7817 |  |
| Kidney disease | -0.2418 | 0.1960 | ±0.3920 | -1.234 | 0.2173 | 0.7852 |  |
| Circulatory disease | -0.1800 | 0.1787 | ±0.3575 | -1.007 | 0.3138 | 0.8352 |  |
| Time < 54 (%) | +0.0186 | 0.1678 | ±0.3355 | +0.111 | 0.9116 | 1.0188 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0539**, LLR χ² = **64.74** (p = **1.21e-09**), AUC = **0.6607**, AIC = **1160.2**, BIC = **1217.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0330** | 0.6347 | ±1.2695 | **-3.203** | **0.0014** | 0.1309 | ** |
| **Education: graduate level (vs college)** | **-0.7367** | 0.1619 | ±0.3238 | **-4.550** | **5.36e-06** | 0.4787 | *** |
| **Education: high school or below (vs college)** | **+0.6626** | 0.2089 | ±0.4178 | **+3.172** | **0.0015** | 1.9398 | ** |
| **Site: UCSD (vs UAB)** | **+0.3816** | 0.1758 | ±0.3516 | **+2.171** | **0.0299** | 1.4646 | * |
| Site: UW (vs UAB) | +0.0277 | 0.1771 | ±0.3542 | +0.157 | 0.8756 | 1.0281 |  |
| **Age (years)** | **+0.0279** | 0.0073 | ±0.0146 | **+3.833** | **1.26e-04** | 1.0283 | *** |
| BMI (kg/m2) | +0.0112 | 0.0102 | ±0.0205 | +1.096 | 0.2732 | 1.0113 |  |
| Hypertension | +0.1931 | 0.1619 | ±0.3238 | +1.193 | 0.2329 | 1.2131 |  |
| High cholesterol | -0.2447 | 0.1519 | ±0.3037 | -1.611 | 0.1071 | 0.7829 |  |
| Kidney disease | -0.2414 | 0.1960 | ±0.3919 | -1.232 | 0.2179 | 0.7855 |  |
| Circulatory disease | -0.1829 | 0.1786 | ±0.3573 | -1.024 | 0.3059 | 0.8328 |  |
| Avg. daily time < 54 (%) | +0.0625 | 0.1618 | ±0.3236 | +0.387 | 0.6991 | 1.0645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0540**, LLR χ² = **64.84** (p = **1.15e-09**), AUC = **0.6603**, AIC = **1160.1**, BIC = **1217.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0342** | 0.6347 | ±1.2695 | **-3.205** | **0.0014** | 0.1308 | ** |
| **Education: graduate level (vs college)** | **-0.7355** | 0.1620 | ±0.3239 | **-4.541** | **5.61e-06** | 0.4793 | *** |
| **Education: high school or below (vs college)** | **+0.6596** | 0.2087 | ±0.4175 | **+3.160** | **0.0016** | 1.9339 | ** |
| **Site: UCSD (vs UAB)** | **+0.3828** | 0.1758 | ±0.3515 | **+2.178** | **0.0294** | 1.4664 | * |
| Site: UW (vs UAB) | +0.0284 | 0.1770 | ±0.3540 | +0.161 | 0.8724 | 1.0288 |  |
| **Age (years)** | **+0.0279** | 0.0073 | ±0.0146 | **+3.820** | **1.33e-04** | 1.0282 | *** |
| BMI (kg/m2) | +0.0112 | 0.0102 | ±0.0205 | +1.092 | 0.2749 | 1.0112 |  |
| Hypertension | +0.1936 | 0.1619 | ±0.3238 | +1.196 | 0.2318 | 1.2136 |  |
| High cholesterol | -0.2459 | 0.1518 | ±0.3036 | -1.620 | 0.1052 | 0.7820 |  |
| Kidney disease | -0.2423 | 0.1959 | ±0.3918 | -1.237 | 0.2161 | 0.7848 |  |
| Circulatory disease | -0.1818 | 0.1784 | ±0.3568 | -1.019 | 0.3082 | 0.8338 |  |
| Time 54-69, pooled (%) | +0.0245 | 0.0483 | ±0.0967 | +0.508 | 0.6117 | 1.0248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0541**, LLR χ² = **64.98** (p = **1.09e-09**), AUC = **0.6605**, AIC = **1160.0**, BIC = **1217.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0302** | 0.6347 | ±1.2693 | **-3.199** | **0.0014** | 0.1313 | ** |
| **Education: graduate level (vs college)** | **-0.7344** | 0.1620 | ±0.3240 | **-4.533** | **5.81e-06** | 0.4798 | *** |
| **Education: high school or below (vs college)** | **+0.6590** | 0.2087 | ±0.4175 | **+3.157** | **0.0016** | 1.9329 | ** |
| **Site: UCSD (vs UAB)** | **+0.3836** | 0.1757 | ±0.3514 | **+2.183** | **0.0290** | 1.4675 | * |
| Site: UW (vs UAB) | +0.0298 | 0.1770 | ±0.3540 | +0.168 | 0.8664 | 1.0302 |  |
| **Age (years)** | **+0.0278** | 0.0073 | ±0.0146 | **+3.805** | **1.42e-04** | 1.0281 | *** |
| BMI (kg/m2) | +0.0112 | 0.0102 | ±0.0205 | +1.089 | 0.2762 | 1.0112 |  |
| Hypertension | +0.1934 | 0.1619 | ±0.3238 | +1.195 | 0.2322 | 1.2134 |  |
| High cholesterol | -0.2455 | 0.1518 | ±0.3036 | -1.617 | 0.1059 | 0.7823 |  |
| Kidney disease | -0.2419 | 0.1959 | ±0.3918 | -1.235 | 0.2169 | 0.7851 |  |
| Circulatory disease | -0.1819 | 0.1784 | ±0.3568 | -1.020 | 0.3079 | 0.8337 |  |
| Avg. daily time 54-69 (%) | +0.0297 | 0.0473 | ±0.0946 | +0.628 | 0.5300 | 1.0301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0539**, LLR χ² = **64.78** (p = **1.18e-09**), AUC = **0.6603**, AIC = **1160.2**, BIC = **1217.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0351** | 0.6348 | ±1.2696 | **-3.206** | **0.0013** | 0.1307 | ** |
| **Education: graduate level (vs college)** | **-0.7359** | 0.1620 | ±0.3239 | **-4.544** | **5.52e-06** | 0.4791 | *** |
| **Education: high school or below (vs college)** | **+0.6606** | 0.2087 | ±0.4175 | **+3.165** | **0.0016** | 1.9359 | ** |
| **Site: UCSD (vs UAB)** | **+0.3828** | 0.1759 | ±0.3518 | **+2.176** | **0.0295** | 1.4664 | * |
| Site: UW (vs UAB) | +0.0286 | 0.1771 | ±0.3543 | +0.161 | 0.8717 | 1.0290 |  |
| **Age (years)** | **+0.0279** | 0.0073 | ±0.0146 | **+3.827** | **1.30e-04** | 1.0283 | *** |
| BMI (kg/m2) | +0.0112 | 0.0102 | ±0.0205 | +1.091 | 0.2751 | 1.0112 |  |
| Hypertension | +0.1933 | 0.1619 | ±0.3238 | +1.194 | 0.2325 | 1.2132 |  |
| High cholesterol | -0.2458 | 0.1518 | ±0.3036 | -1.619 | 0.1054 | 0.7821 |  |
| Kidney disease | -0.2418 | 0.1959 | ±0.3918 | -1.234 | 0.2171 | 0.7852 |  |
| Circulatory disease | -0.1823 | 0.1785 | ±0.3569 | -1.021 | 0.3072 | 0.8334 |  |
| Time < 70 (%) | +0.0177 | 0.0399 | ±0.0797 | +0.445 | 0.6564 | 1.0179 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0541**, LLR χ² = **64.96** (p = **1.10e-09**), AUC = **0.6606**, AIC = **1160.0**, BIC = **1217.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0315** | 0.6347 | ±1.2694 | **-3.201** | **0.0014** | 0.1311 | ** |
| **Education: graduate level (vs college)** | **-0.7344** | 0.1620 | ±0.3240 | **-4.534** | **5.80e-06** | 0.4798 | *** |
| **Education: high school or below (vs college)** | **+0.6603** | 0.2087 | ±0.4175 | **+3.163** | **0.0016** | 1.9355 | ** |
| **Site: UCSD (vs UAB)** | **+0.3841** | 0.1758 | ±0.3515 | **+2.185** | **0.0289** | 1.4682 | * |
| Site: UW (vs UAB) | +0.0304 | 0.1771 | ±0.3542 | +0.172 | 0.8636 | 1.0309 |  |
| **Age (years)** | **+0.0278** | 0.0073 | ±0.0146 | **+3.810** | **1.39e-04** | 1.0282 | *** |
| BMI (kg/m2) | +0.0111 | 0.0102 | ±0.0205 | +1.089 | 0.2762 | 1.0112 |  |
| Hypertension | +0.1932 | 0.1619 | ±0.3238 | +1.193 | 0.2328 | 1.2131 |  |
| High cholesterol | -0.2450 | 0.1518 | ±0.3037 | -1.614 | 0.1066 | 0.7827 |  |
| Kidney disease | -0.2416 | 0.1959 | ±0.3918 | -1.233 | 0.2174 | 0.7854 |  |
| Circulatory disease | -0.1828 | 0.1784 | ±0.3569 | -1.025 | 0.3055 | 0.8329 |  |
| Avg. daily time < 70 (%) | +0.0238 | 0.0390 | ±0.0780 | +0.610 | 0.5416 | 1.0241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0570**, LLR χ² = **68.43** (p = **2.42e-10**), AUC = **0.6640**, AIC = **1156.5**, BIC = **1213.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1956 | 0.7691 | ±1.5383 | -1.555 | 0.1201 | 0.3025 |  |
| **Education: graduate level (vs college)** | **-0.7151** | 0.1625 | ±0.3251 | **-4.400** | **1.08e-05** | 0.4891 | *** |
| **Education: high school or below (vs college)** | **+0.6251** | 0.2096 | ±0.4191 | **+2.983** | **0.0029** | 1.8684 | ** |
| **Site: UCSD (vs UAB)** | **+0.4000** | 0.1759 | ±0.3518 | **+2.274** | **0.0230** | 1.4918 | * |
| Site: UW (vs UAB) | +0.0462 | 0.1773 | ±0.3545 | +0.261 | 0.7944 | 1.0473 |  |
| **Age (years)** | **+0.0284** | 0.0073 | ±0.0146 | **+3.887** | **1.02e-04** | 1.0288 | *** |
| BMI (kg/m2) | +0.0109 | 0.0103 | ±0.0206 | +1.057 | 0.2905 | 1.0109 |  |
| Hypertension | +0.1938 | 0.1621 | ±0.3242 | +1.195 | 0.2319 | 1.2138 |  |
| High cholesterol | -0.2402 | 0.1521 | ±0.3042 | -1.579 | 0.1142 | 0.7864 |  |
| Kidney disease | -0.2690 | 0.1970 | ±0.3940 | -1.366 | 0.1721 | 0.7641 |  |
| Circulatory disease | -0.1862 | 0.1789 | ±0.3578 | -1.041 | 0.2981 | 0.8301 |  |
| Time 54-250, pooled (%) | -0.0092 | 0.0048 | ±0.0096 | -1.922 | 0.0546 | 0.9908 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0568**, LLR χ² = **68.24** (p = **2.63e-10**), AUC = **0.6638**, AIC = **1156.7**, BIC = **1213.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1981 | 0.7742 | ±1.5483 | -1.548 | 0.1217 | 0.3018 |  |
| **Education: graduate level (vs college)** | **-0.7160** | 0.1625 | ±0.3250 | **-4.405** | **1.06e-05** | 0.4887 | *** |
| **Education: high school or below (vs college)** | **+0.6258** | 0.2096 | ±0.4191 | **+2.987** | **0.0028** | 1.8698 | ** |
| **Site: UCSD (vs UAB)** | **+0.3998** | 0.1759 | ±0.3518 | **+2.272** | **0.0231** | 1.4915 | * |
| Site: UW (vs UAB) | +0.0446 | 0.1772 | ±0.3544 | +0.252 | 0.8012 | 1.0456 |  |
| **Age (years)** | **+0.0283** | 0.0073 | ±0.0146 | **+3.872** | **1.08e-04** | 1.0287 | *** |
| BMI (kg/m2) | +0.0109 | 0.0103 | ±0.0206 | +1.056 | 0.2908 | 1.0109 |  |
| Hypertension | +0.1944 | 0.1621 | ±0.3242 | +1.200 | 0.2303 | 1.2146 |  |
| High cholesterol | -0.2405 | 0.1521 | ±0.3042 | -1.581 | 0.1139 | 0.7863 |  |
| Kidney disease | -0.2702 | 0.1971 | ±0.3942 | -1.371 | 0.1703 | 0.7632 |  |
| Circulatory disease | -0.1870 | 0.1789 | ±0.3578 | -1.045 | 0.2960 | 0.8295 |  |
| Avg. daily time 54-250 (%) | -0.0091 | 0.0049 | ±0.0097 | -1.875 | 0.0609 | 0.9909 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0558**, LLR χ² = **67.01** (p = **4.50e-10**), AUC = **0.6622**, AIC = **1157.9**, BIC = **1215.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0650** | 0.6371 | ±1.2743 | **-3.241** | **0.0012** | 0.1268 | ** |
| **Education: graduate level (vs college)** | **-0.7342** | 0.1622 | ±0.3243 | **-4.528** | **5.96e-06** | 0.4799 | *** |
| **Education: high school or below (vs college)** | **+0.6361** | 0.2093 | ±0.4187 | **+3.039** | **0.0024** | 1.8891 | ** |
| **Site: UCSD (vs UAB)** | **+0.3964** | 0.1760 | ±0.3520 | **+2.252** | **0.0243** | 1.4865 | * |
| Site: UW (vs UAB) | +0.0173 | 0.1768 | ±0.3537 | +0.098 | 0.9222 | 1.0174 |  |
| **Age (years)** | **+0.0266** | 0.0074 | ±0.0147 | **+3.618** | **2.97e-04** | 1.0270 | *** |
| BMI (kg/m2) | +0.0109 | 0.0103 | ±0.0206 | +1.056 | 0.2909 | 1.0109 |  |
| Hypertension | +0.2137 | 0.1626 | ±0.3253 | +1.314 | 0.1888 | 1.2383 |  |
| High cholesterol | -0.2384 | 0.1521 | ±0.3042 | -1.567 | 0.1170 | 0.7879 |  |
| Kidney disease | -0.2710 | 0.1970 | ±0.3941 | -1.375 | 0.1690 | 0.7626 |  |
| Circulatory disease | -0.1836 | 0.1787 | ±0.3573 | -1.028 | 0.3040 | 0.8322 |  |
| Time 181-250, pooled (%) | +0.0072 | 0.0046 | ±0.0092 | +1.557 | 0.1196 | 1.0072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0559**, LLR χ² = **67.08** (p = **4.37e-10**), AUC = **0.6623**, AIC = **1157.9**, BIC = **1215.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0678** | 0.6374 | ±1.2748 | **-3.244** | **0.0012** | 0.1265 | ** |
| **Education: graduate level (vs college)** | **-0.7349** | 0.1622 | ±0.3243 | **-4.532** | **5.85e-06** | 0.4796 | *** |
| **Education: high school or below (vs college)** | **+0.6341** | 0.2094 | ±0.4188 | **+3.028** | **0.0025** | 1.8852 | ** |
| **Site: UCSD (vs UAB)** | **+0.3980** | 0.1761 | ±0.3521 | **+2.260** | **0.0238** | 1.4888 | * |
| Site: UW (vs UAB) | +0.0183 | 0.1768 | ±0.3537 | +0.104 | 0.9175 | 1.0185 |  |
| **Age (years)** | **+0.0267** | 0.0073 | ±0.0147 | **+3.629** | **2.85e-04** | 1.0270 | *** |
| BMI (kg/m2) | +0.0108 | 0.0103 | ±0.0206 | +1.055 | 0.2916 | 1.0109 |  |
| Hypertension | +0.2135 | 0.1626 | ±0.3252 | +1.313 | 0.1892 | 1.2380 |  |
| High cholesterol | -0.2387 | 0.1521 | ±0.3042 | -1.570 | 0.1165 | 0.7876 |  |
| Kidney disease | -0.2719 | 0.1971 | ±0.3942 | -1.380 | 0.1677 | 0.7619 |  |
| Circulatory disease | -0.1831 | 0.1786 | ±0.3573 | -1.025 | 0.3053 | 0.8327 |  |
| Avg. daily time 181-250 (%) | +0.0072 | 0.0046 | ±0.0091 | +1.578 | 0.1145 | 1.0072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0575**, LLR χ² = **69.04** (p = **1.86e-10**), AUC = **0.6638**, AIC = **1155.9**, BIC = **1213.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1155** | 0.6392 | ±1.2785 | **-3.309** | **9.35e-04** | 0.1206 | *** |
| **Education: graduate level (vs college)** | **-0.7203** | 0.1625 | ±0.3250 | **-4.433** | **9.31e-06** | 0.4866 | *** |
| **Education: high school or below (vs college)** | **+0.6177** | 0.2098 | ±0.4196 | **+2.944** | **0.0032** | 1.8547 | ** |
| **Site: UCSD (vs UAB)** | **+0.4077** | 0.1763 | ±0.3526 | **+2.313** | **0.0207** | 1.5034 | * |
| Site: UW (vs UAB) | +0.0335 | 0.1771 | ±0.3542 | +0.189 | 0.8500 | 1.0341 |  |
| **Age (years)** | **+0.0271** | 0.0073 | ±0.0146 | **+3.707** | **2.10e-04** | 1.0275 | *** |
| BMI (kg/m2) | +0.0107 | 0.0103 | ±0.0206 | +1.035 | 0.3009 | 1.0107 |  |
| Hypertension | +0.2099 | 0.1624 | ±0.3249 | +1.292 | 0.1963 | 1.2335 |  |
| High cholesterol | -0.2359 | 0.1522 | ±0.3045 | -1.549 | 0.1213 | 0.7899 |  |
| Kidney disease | -0.2831 | 0.1975 | ±0.3949 | -1.434 | 0.1517 | 0.7535 |  |
| Circulatory disease | -0.1871 | 0.1790 | ±0.3580 | -1.045 | 0.2959 | 0.8294 |  |
| **Time > 180 (%)** | **+0.0059** | 0.0028 | ±0.0056 | **+2.102** | **0.0356** | 1.0059 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0574**, LLR χ² = **68.94** (p = **1.95e-10**), AUC = **0.6635**, AIC = **1156.0**, BIC = **1213.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1106** | 0.6391 | ±1.2782 | **-3.302** | **9.59e-04** | 0.1212 | *** |
| **Education: graduate level (vs college)** | **-0.7215** | 0.1625 | ±0.3250 | **-4.440** | **8.98e-06** | 0.4860 | *** |
| **Education: high school or below (vs college)** | **+0.6170** | 0.2098 | ±0.4197 | **+2.940** | **0.0033** | 1.8534 | ** |
| **Site: UCSD (vs UAB)** | **+0.4087** | 0.1763 | ±0.3526 | **+2.318** | **0.0205** | 1.5048 | * |
| Site: UW (vs UAB) | +0.0334 | 0.1771 | ±0.3542 | +0.189 | 0.8504 | 1.0340 |  |
| **Age (years)** | **+0.0271** | 0.0073 | ±0.0146 | **+3.706** | **2.11e-04** | 1.0275 | *** |
| BMI (kg/m2) | +0.0106 | 0.0103 | ±0.0206 | +1.033 | 0.3018 | 1.0107 |  |
| Hypertension | +0.2098 | 0.1624 | ±0.3248 | +1.292 | 0.1964 | 1.2335 |  |
| High cholesterol | -0.2365 | 0.1522 | ±0.3045 | -1.553 | 0.1204 | 0.7894 |  |
| Kidney disease | -0.2842 | 0.1976 | ±0.3951 | -1.439 | 0.1502 | 0.7526 |  |
| Circulatory disease | -0.1872 | 0.1790 | ±0.3579 | -1.046 | 0.2955 | 0.8293 |  |
| **Avg. daily time > 180 (%)** | **+0.0058** | 0.0028 | ±0.0056 | **+2.077** | **0.0378** | 1.0058 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0575**, LLR χ² = **69.07** (p = **1.83e-10**), AUC = **0.6642**, AIC = **1155.9**, BIC = **1213.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1037** | 0.6389 | ±1.2777 | **-3.293** | **9.92e-04** | 0.1220 | *** |
| **Education: graduate level (vs college)** | **-0.7143** | 0.1626 | ±0.3253 | **-4.392** | **1.12e-05** | 0.4895 | *** |
| **Education: high school or below (vs college)** | **+0.6210** | 0.2097 | ±0.4194 | **+2.962** | **0.0031** | 1.8609 | ** |
| **Site: UCSD (vs UAB)** | **+0.4112** | 0.1764 | ±0.3528 | **+2.331** | **0.0198** | 1.5086 | * |
| Site: UW (vs UAB) | +0.0312 | 0.1771 | ±0.3541 | +0.176 | 0.8602 | 1.0317 |  |
| **Age (years)** | **+0.0279** | 0.0073 | ±0.0146 | **+3.816** | **1.36e-04** | 1.0283 | *** |
| BMI (kg/m2) | +0.0097 | 0.0103 | ±0.0206 | +0.935 | 0.3499 | 1.0097 |  |
| Hypertension | +0.2105 | 0.1625 | ±0.3249 | +1.296 | 0.1951 | 1.2342 |  |
| High cholesterol | -0.2340 | 0.1523 | ±0.3045 | -1.537 | 0.1243 | 0.7913 |  |
| Kidney disease | -0.2780 | 0.1973 | ±0.3945 | -1.409 | 0.1587 | 0.7573 |  |
| Circulatory disease | -0.1894 | 0.1791 | ±0.3581 | -1.058 | 0.2902 | 0.8275 |  |
| **Nocturnal time > 180 (%)** | **+0.0056** | 0.0027 | ±0.0054 | **+2.106** | **0.0352** | 1.0057 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0548**, LLR χ² = **65.86** (p = **7.43e-10**), AUC = **0.6615**, AIC = **1159.1**, BIC = **1216.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0859** | 0.6379 | ±1.2758 | **-3.270** | **0.0011** | 0.1242 | ** |
| **Education: graduate level (vs college)** | **-0.7245** | 0.1624 | ±0.3248 | **-4.462** | **8.13e-06** | 0.4845 | *** |
| **Education: high school or below (vs college)** | **+0.6502** | 0.2089 | ±0.4178 | **+3.112** | **0.0019** | 1.9159 | ** |
| **Site: UCSD (vs UAB)** | **+0.3843** | 0.1756 | ±0.3511 | **+2.189** | **0.0286** | 1.4687 | * |
| Site: UW (vs UAB) | +0.0149 | 0.1767 | ±0.3534 | +0.084 | 0.9327 | 1.0150 |  |
| **Age (years)** | **+0.0267** | 0.0074 | ±0.0148 | **+3.620** | **2.95e-04** | 1.0271 | *** |
| BMI (kg/m2) | +0.0119 | 0.0103 | ±0.0206 | +1.159 | 0.2466 | 1.0120 |  |
| Hypertension | +0.2029 | 0.1622 | ±0.3244 | +1.251 | 0.2109 | 1.2250 |  |
| High cholesterol | -0.2450 | 0.1519 | ±0.3038 | -1.613 | 0.1067 | 0.7827 |  |
| Kidney disease | -0.2643 | 0.1970 | ±0.3940 | -1.342 | 0.1797 | 0.7678 |  |
| Circulatory disease | -0.1755 | 0.1785 | ±0.3570 | -0.983 | 0.3256 | 0.8391 |  |
| Any reading > 250 during wear (0/1) | +0.1706 | 0.1511 | ±0.3023 | +1.129 | 0.2590 | 1.1860 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0570**, LLR χ² = **68.41** (p = **2.45e-10**), AUC = **0.6640**, AIC = **1156.5**, BIC = **1213.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1173** | 0.6387 | ±1.2774 | **-3.315** | **9.17e-04** | 0.1204 | *** |
| **Education: graduate level (vs college)** | **-0.7155** | 0.1625 | ±0.3251 | **-4.402** | **1.07e-05** | 0.4890 | *** |
| **Education: high school or below (vs college)** | **+0.6246** | 0.2096 | ±0.4192 | **+2.980** | **0.0029** | 1.8675 | ** |
| **Site: UCSD (vs UAB)** | **+0.3990** | 0.1759 | ±0.3518 | **+2.268** | **0.0233** | 1.4903 | * |
| Site: UW (vs UAB) | +0.0451 | 0.1772 | ±0.3544 | +0.254 | 0.7993 | 1.0461 |  |
| **Age (years)** | **+0.0284** | 0.0073 | ±0.0146 | **+3.886** | **1.02e-04** | 1.0288 | *** |
| BMI (kg/m2) | +0.0109 | 0.0103 | ±0.0206 | +1.059 | 0.2896 | 1.0110 |  |
| Hypertension | +0.1940 | 0.1621 | ±0.3242 | +1.197 | 0.2313 | 1.2141 |  |
| High cholesterol | -0.2404 | 0.1521 | ±0.3042 | -1.581 | 0.1139 | 0.7863 |  |
| Kidney disease | -0.2692 | 0.1970 | ±0.3941 | -1.366 | 0.1719 | 0.7640 |  |
| Circulatory disease | -0.1854 | 0.1789 | ±0.3578 | -1.036 | 0.3000 | 0.8307 |  |
| Time > 250 (%) | +0.0092 | 0.0048 | ±0.0096 | +1.916 | 0.0553 | 1.0092 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 867)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **867**, events = **419**, McFadden pseudo-R² = **0.0568**, LLR χ² = **68.20** (p = **2.69e-10**), AUC = **0.6636**, AIC = **1156.8**, BIC = **1213.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1071** | 0.6383 | ±1.2765 | **-3.301** | **9.62e-04** | 0.1216 | *** |
| **Education: graduate level (vs college)** | **-0.7165** | 0.1625 | ±0.3250 | **-4.409** | **1.04e-05** | 0.4885 | *** |
| **Education: high school or below (vs college)** | **+0.6255** | 0.2096 | ±0.4191 | **+2.985** | **0.0028** | 1.8693 | ** |
| **Site: UCSD (vs UAB)** | **+0.3989** | 0.1759 | ±0.3518 | **+2.268** | **0.0233** | 1.4901 | * |
| Site: UW (vs UAB) | +0.0436 | 0.1772 | ±0.3544 | +0.246 | 0.8056 | 1.0446 |  |
| **Age (years)** | **+0.0283** | 0.0073 | ±0.0146 | **+3.873** | **1.08e-04** | 1.0287 | *** |
| BMI (kg/m2) | +0.0109 | 0.0103 | ±0.0206 | +1.058 | 0.2902 | 1.0109 |  |
| Hypertension | +0.1946 | 0.1621 | ±0.3242 | +1.201 | 0.2299 | 1.2148 |  |
| High cholesterol | -0.2408 | 0.1521 | ±0.3042 | -1.583 | 0.1133 | 0.7860 |  |
| Kidney disease | -0.2702 | 0.1971 | ±0.3942 | -1.371 | 0.1704 | 0.7632 |  |
| Circulatory disease | -0.1863 | 0.1789 | ±0.3578 | -1.041 | 0.2977 | 0.8300 |  |
| Avg. daily time > 250 (%) | +0.0090 | 0.0049 | ±0.0097 | +1.863 | 0.0625 | 1.0091 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 867; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **867**, R² = **0.0716**, Adj R² = **0.0608**, F-statistic = **6.60** (p = **6.60e-10**), Residual SE = **2.723** on **856** df, AIC = **4208.2**, BIC = **4260.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1568** | 0.8287 | ±1.6574 | **+19.497** | **1.17e-84** | *** |
| Education: graduate level (vs college) | +0.3332 | 0.2044 | ±0.4088 | +1.630 | 0.1031 |  |
| **Education: high school or below (vs college)** | **-1.0060** | 0.3040 | ±0.6079 | **-3.310** | **9.35e-04** | *** |
| Site: UCSD (vs UAB) | +0.1028 | 0.2425 | ±0.4849 | +0.424 | 0.6717 |  |
| Site: UW (vs UAB) | -0.0989 | 0.2288 | ±0.4576 | -0.432 | 0.6657 |  |
| **Age (years)** | **-0.0596** | 0.0104 | ±0.0208 | **-5.719** | **1.07e-08** | *** |
| BMI (kg/m2) | -0.0062 | 0.0134 | ±0.0269 | -0.459 | 0.6459 |  |
| Hypertension | -0.3375 | 0.2067 | ±0.4134 | -1.633 | 0.1025 |  |
| High cholesterol | +0.3121 | 0.2057 | ±0.4114 | +1.517 | 0.1292 |  |
| Kidney disease | +0.3739 | 0.2661 | ±0.5323 | +1.405 | 0.1600 |  |
| Circulatory disease | +0.2877 | 0.2359 | ±0.4717 | +1.220 | 0.2226 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **867**, R² = **0.0756**, Adj R² = **0.0637**, F-statistic = **6.36** (p = **3.50e-10**), Residual SE = **2.718** on **855** df, AIC = **4206.4**, BIC = **4263.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.0096** | 0.9358 | ±1.8717 | **+18.176** | **8.00e-74** | *** |
| Education: graduate level (vs college) | +0.2989 | 0.2043 | ±0.4085 | +1.463 | 0.1434 |  |
| **Education: high school or below (vs college)** | **-0.9491** | 0.3065 | ±0.6130 | **-3.097** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.0811 | 0.2432 | ±0.4865 | +0.333 | 0.7388 |  |
| Site: UW (vs UAB) | -0.1176 | 0.2289 | ±0.4579 | -0.514 | 0.6075 |  |
| **Age (years)** | **-0.0589** | 0.0104 | ±0.0208 | **-5.657** | **1.54e-08** | *** |
| BMI (kg/m2) | -0.0040 | 0.0135 | ±0.0270 | -0.299 | 0.7649 |  |
| Hypertension | -0.3355 | 0.2063 | ±0.4125 | -1.627 | 0.1038 |  |
| High cholesterol | +0.3118 | 0.2051 | ±0.4102 | +1.520 | 0.1285 |  |
| Kidney disease | +0.3829 | 0.2665 | ±0.5330 | +1.437 | 0.1508 |  |
| Circulatory disease | +0.2928 | 0.2354 | ±0.4707 | +1.244 | 0.2135 |  |
| **HbA1c (%)** | **-0.1419** | 0.0672 | ±0.1344 | **-2.111** | **0.0347** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **867**, R² = **0.0746**, Adj R² = **0.0627**, F-statistic = **6.26** (p = **5.36e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.4**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.6913** | 0.8795 | ±1.7591 | **+18.977** | **2.63e-80** | *** |
| Education: graduate level (vs college) | +0.3085 | 0.2045 | ±0.4091 | +1.508 | 0.1315 |  |
| **Education: high school or below (vs college)** | **-0.9650** | 0.3040 | ±0.6080 | **-3.174** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0786 | 0.2435 | ±0.4869 | +0.323 | 0.7469 |  |
| Site: UW (vs UAB) | -0.1102 | 0.2288 | ±0.4576 | -0.482 | 0.6301 |  |
| **Age (years)** | **-0.0589** | 0.0105 | ±0.0209 | **-5.637** | **1.73e-08** | *** |
| BMI (kg/m2) | -0.0055 | 0.0135 | ±0.0270 | -0.405 | 0.6858 |  |
| Hypertension | -0.3447 | 0.2070 | ±0.4141 | -1.665 | 0.0959 | . |
| High cholesterol | +0.3040 | 0.2052 | ±0.4105 | +1.481 | 0.1386 |  |
| Kidney disease | +0.4078 | 0.2677 | ±0.5353 | +1.523 | 0.1277 |  |
| Circulatory disease | +0.2920 | 0.2350 | ±0.4700 | +1.243 | 0.2140 |  |
| Mean glucose (mg/dL) | -0.0038 | 0.0021 | ±0.0043 | -1.782 | 0.0748 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **867**, R² = **0.0746**, Adj R² = **0.0627**, F-statistic = **6.26** (p = **5.36e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.4**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.2164** | 1.0149 | ±2.0297 | **+16.964** | **1.51e-64** | *** |
| Education: graduate level (vs college) | +0.3085 | 0.2045 | ±0.4091 | +1.508 | 0.1315 |  |
| **Education: high school or below (vs college)** | **-0.9650** | 0.3040 | ±0.6080 | **-3.174** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0786 | 0.2435 | ±0.4869 | +0.323 | 0.7469 |  |
| Site: UW (vs UAB) | -0.1102 | 0.2288 | ±0.4576 | -0.482 | 0.6301 |  |
| **Age (years)** | **-0.0589** | 0.0105 | ±0.0209 | **-5.637** | **1.73e-08** | *** |
| BMI (kg/m2) | -0.0055 | 0.0135 | ±0.0270 | -0.405 | 0.6858 |  |
| Hypertension | -0.3447 | 0.2070 | ±0.4141 | -1.665 | 0.0959 | . |
| High cholesterol | +0.3040 | 0.2052 | ±0.4105 | +1.481 | 0.1386 |  |
| Kidney disease | +0.4078 | 0.2677 | ±0.5353 | +1.523 | 0.1277 |  |
| Circulatory disease | +0.2920 | 0.2350 | ±0.4700 | +1.243 | 0.2140 |  |
| GMI (%) | -0.1586 | 0.0890 | ±0.1781 | -1.782 | 0.0748 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **867**, R² = **0.0753**, Adj R² = **0.0634**, F-statistic = **6.33** (p = **4.03e-10**), Residual SE = **2.719** on **855** df, AIC = **4206.7**, BIC = **4263.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7438** | 0.8704 | ±1.7407 | **+19.238** | **1.79e-82** | *** |
| Education: graduate level (vs college) | +0.3060 | 0.2041 | ±0.4081 | +1.500 | 0.1337 |  |
| **Education: high school or below (vs college)** | **-0.9628** | 0.3042 | ±0.6084 | **-3.165** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0773 | 0.2433 | ±0.4866 | +0.318 | 0.7508 |  |
| Site: UW (vs UAB) | -0.1023 | 0.2290 | ±0.4580 | -0.447 | 0.6550 |  |
| **Age (years)** | **-0.0597** | 0.0104 | ±0.0209 | **-5.721** | **1.06e-08** | *** |
| BMI (kg/m2) | -0.0044 | 0.0136 | ±0.0271 | -0.326 | 0.7447 |  |
| Hypertension | -0.3492 | 0.2072 | ±0.4144 | -1.685 | 0.0919 | . |
| High cholesterol | +0.3056 | 0.2051 | ±0.4102 | +1.490 | 0.1363 |  |
| Kidney disease | +0.3989 | 0.2667 | ±0.5335 | +1.495 | 0.1348 |  |
| Circulatory disease | +0.2928 | 0.2346 | ±0.4691 | +1.248 | 0.2120 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0042** | 0.0021 | ±0.0042 | **-1.961** | **0.0498** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **867**, R² = **0.0808**, Adj R² = **0.0690**, F-statistic = **6.83** (p = **4.21e-11**), Residual SE = **2.711** on **855** df, AIC = **4201.5**, BIC = **4258.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7034** | 0.8497 | ±1.6993 | **+19.659** | **4.86e-86** | *** |
| Education: graduate level (vs college) | +0.2825 | 0.2035 | ±0.4071 | +1.388 | 0.1652 |  |
| **Education: high school or below (vs college)** | **-0.9219** | 0.3061 | ±0.6123 | **-3.011** | **0.0026** | ** |
| Site: UCSD (vs UAB) | +0.0605 | 0.2425 | ±0.4849 | +0.249 | 0.8031 |  |
| Site: UW (vs UAB) | -0.1444 | 0.2289 | ±0.4578 | -0.631 | 0.5281 |  |
| **Age (years)** | **-0.0569** | 0.0105 | ±0.0210 | **-5.412** | **6.24e-08** | *** |
| BMI (kg/m2) | -0.0061 | 0.0134 | ±0.0269 | -0.456 | 0.6483 |  |
| Hypertension | -0.3431 | 0.2064 | ±0.4127 | -1.663 | 0.0963 | . |
| High cholesterol | +0.2910 | 0.2043 | ±0.4085 | +1.425 | 0.1543 |  |
| Kidney disease | +0.5041 | 0.2676 | ±0.5353 | +1.883 | 0.0596 | . |
| Circulatory disease | +0.3011 | 0.2338 | ±0.4675 | +1.288 | 0.1977 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0201** | 0.0066 | ±0.0132 | **-3.045** | **0.0023** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **867**, R² = **0.0801**, Adj R² = **0.0682**, F-statistic = **6.76** (p = **5.75e-11**), Residual SE = **2.712** on **855** df, AIC = **4202.3**, BIC = **4259.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7156** | 0.8548 | ±1.7097 | **+19.554** | **3.80e-85** | *** |
| Education: graduate level (vs college) | +0.2882 | 0.2039 | ±0.4077 | +1.414 | 0.1575 |  |
| **Education: high school or below (vs college)** | **-0.9191** | 0.3058 | ±0.6116 | **-3.006** | **0.0026** | ** |
| Site: UCSD (vs UAB) | +0.0645 | 0.2422 | ±0.4845 | +0.266 | 0.7901 |  |
| Site: UW (vs UAB) | -0.1370 | 0.2288 | ±0.4577 | -0.599 | 0.5494 |  |
| **Age (years)** | **-0.0567** | 0.0105 | ±0.0210 | **-5.396** | **6.81e-08** | *** |
| BMI (kg/m2) | -0.0073 | 0.0135 | ±0.0270 | -0.538 | 0.5904 |  |
| Hypertension | -0.3461 | 0.2065 | ±0.4130 | -1.676 | 0.0938 | . |
| High cholesterol | +0.2920 | 0.2047 | ±0.4093 | +1.427 | 0.1537 |  |
| Kidney disease | +0.5031 | 0.2672 | ±0.5345 | +1.882 | 0.0598 | . |
| Circulatory disease | +0.2947 | 0.2341 | ±0.4682 | +1.259 | 0.2080 |  |
| **Avg. daily SD (mg/dL)** | **-0.0220** | 0.0074 | ±0.0148 | **-2.988** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **867**, R² = **0.0805**, Adj R² = **0.0686**, F-statistic = **6.80** (p = **4.84e-11**), Residual SE = **2.711** on **855** df, AIC = **4201.9**, BIC = **4259.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.0203** | 0.8751 | ±1.7502 | **+19.450** | **2.92e-84** | *** |
| Education: graduate level (vs college) | +0.2980 | 0.2032 | ±0.4065 | +1.466 | 0.1426 |  |
| **Education: high school or below (vs college)** | **-0.9399** | 0.3079 | ±0.6157 | **-3.053** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.0727 | 0.2418 | ±0.4837 | +0.301 | 0.7636 |  |
| Site: UW (vs UAB) | -0.1496 | 0.2297 | ±0.4594 | -0.651 | 0.5149 |  |
| **Age (years)** | **-0.0562** | 0.0105 | ±0.0210 | **-5.338** | **9.40e-08** | *** |
| BMI (kg/m2) | -0.0072 | 0.0134 | ±0.0267 | -0.543 | 0.5875 |  |
| Hypertension | -0.3283 | 0.2059 | ±0.4118 | -1.595 | 0.1108 |  |
| High cholesterol | +0.2936 | 0.2045 | ±0.4089 | +1.436 | 0.1510 |  |
| Kidney disease | +0.5082 | 0.2647 | ±0.5295 | +1.919 | 0.0549 | . |
| Circulatory disease | +0.3027 | 0.2347 | ±0.4695 | +1.290 | 0.1972 |  |
| **CV (%)** | **-0.0467** | 0.0154 | ±0.0307 | **-3.044** | **0.0023** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **867**, R² = **0.0794**, Adj R² = **0.0675**, F-statistic = **6.70** (p = **7.67e-11**), Residual SE = **2.713** on **855** df, AIC = **4202.9**, BIC = **4260.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0196** | 0.9066 | ±1.8132 | **+16.567** | **1.21e-61** | *** |
| Education: graduate level (vs college) | +0.3006 | 0.2031 | ±0.4062 | +1.480 | 0.1388 |  |
| **Education: high school or below (vs college)** | **-0.9382** | 0.3079 | ±0.6158 | **-3.047** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.0838 | 0.2419 | ±0.4837 | +0.347 | 0.7289 |  |
| Site: UW (vs UAB) | -0.1409 | 0.2297 | ±0.4595 | -0.613 | 0.5397 |  |
| **Age (years)** | **-0.0561** | 0.0105 | ±0.0209 | **-5.357** | **8.46e-08** | *** |
| BMI (kg/m2) | -0.0071 | 0.0134 | ±0.0268 | -0.530 | 0.5958 |  |
| Hypertension | -0.3295 | 0.2058 | ±0.4116 | -1.601 | 0.1094 |  |
| High cholesterol | +0.2990 | 0.2047 | ±0.4094 | +1.461 | 0.1441 |  |
| Kidney disease | +0.4748 | 0.2649 | ±0.5298 | +1.792 | 0.0731 | . |
| Circulatory disease | +0.3085 | 0.2344 | ±0.4687 | +1.316 | 0.1881 |  |
| **Mean / SD ratio** | **+0.1963** | 0.0666 | ±0.1332 | **+2.947** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **867**, R² = **0.0779**, Adj R² = **0.0660**, F-statistic = **6.56** (p = **1.40e-10**), Residual SE = **2.715** on **855** df, AIC = **4204.3**, BIC = **4261.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1785** | 0.8845 | ±1.7689 | **+17.161** | **5.18e-66** | *** |
| Education: graduate level (vs college) | +0.3021 | 0.2035 | ±0.4069 | +1.485 | 0.1375 |  |
| **Education: high school or below (vs college)** | **-0.9491** | 0.3068 | ±0.6136 | **-3.093** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.1004 | 0.2416 | ±0.4833 | +0.415 | 0.6778 |  |
| Site: UW (vs UAB) | -0.1297 | 0.2301 | ±0.4603 | -0.564 | 0.5730 |  |
| **Age (years)** | **-0.0562** | 0.0104 | ±0.0209 | **-5.381** | **7.43e-08** | *** |
| BMI (kg/m2) | -0.0080 | 0.0135 | ±0.0269 | -0.597 | 0.5503 |  |
| Hypertension | -0.3292 | 0.2059 | ±0.4118 | -1.598 | 0.1099 |  |
| High cholesterol | +0.2998 | 0.2052 | ±0.4103 | +1.461 | 0.1440 |  |
| Kidney disease | +0.4516 | 0.2645 | ±0.5290 | +1.708 | 0.0877 | . |
| Circulatory disease | +0.2900 | 0.2344 | ±0.4687 | +1.237 | 0.2159 |  |
| **Avg. daily mean/SD** | **+0.1475** | 0.0561 | ±0.1122 | **+2.629** | **0.0086** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **867**, R² = **0.0752**, Adj R² = **0.0633**, F-statistic = **6.32** (p = **4.22e-10**), Residual SE = **2.719** on **855** df, AIC = **4206.9**, BIC = **4264.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9566** | 0.9532 | ±1.9065 | **+17.789** | **8.67e-71** | *** |
| Education: graduate level (vs college) | +0.3022 | 0.2061 | ±0.4121 | +1.466 | 0.1425 |  |
| **Education: high school or below (vs college)** | **-0.9730** | 0.3035 | ±0.6070 | **-3.206** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0831 | 0.2421 | ±0.4842 | +0.343 | 0.7314 |  |
| Site: UW (vs UAB) | -0.1471 | 0.2304 | ±0.4607 | -0.639 | 0.5230 |  |
| **Age (years)** | **-0.0600** | 0.0105 | ±0.0209 | **-5.736** | **9.72e-09** | *** |
| BMI (kg/m2) | -0.0060 | 0.0134 | ±0.0269 | -0.443 | 0.6578 |  |
| Hypertension | -0.3468 | 0.2065 | ±0.4131 | -1.679 | 0.0932 | . |
| High cholesterol | +0.3058 | 0.2055 | ±0.4111 | +1.488 | 0.1368 |  |
| Kidney disease | +0.4183 | 0.2698 | ±0.5397 | +1.550 | 0.1211 |  |
| Circulatory disease | +0.2879 | 0.2366 | ±0.4732 | +1.217 | 0.2237 |  |
| MAG (mg/dL/h) | -0.0176 | 0.0095 | ±0.0190 | -1.848 | 0.0646 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **867**, R² = **0.0794**, Adj R² = **0.0675**, F-statistic = **6.70** (p = **7.63e-11**), Residual SE = **2.713** on **855** df, AIC = **4202.9**, BIC = **4260.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9135** | 0.8711 | ±1.7423 | **+19.415** | **5.73e-84** | *** |
| Education: graduate level (vs college) | +0.2863 | 0.2045 | ±0.4090 | +1.400 | 0.1615 |  |
| **Education: high school or below (vs college)** | **-0.9272** | 0.3056 | ±0.6111 | **-3.034** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +0.0617 | 0.2424 | ±0.4847 | +0.255 | 0.7989 |  |
| Site: UW (vs UAB) | -0.1349 | 0.2288 | ±0.4577 | -0.589 | 0.5556 |  |
| **Age (years)** | **-0.0573** | 0.0106 | ±0.0211 | **-5.430** | **5.64e-08** | *** |
| BMI (kg/m2) | -0.0079 | 0.0135 | ±0.0270 | -0.585 | 0.5583 |  |
| Hypertension | -0.3566 | 0.2068 | ±0.4137 | -1.724 | 0.0847 | . |
| High cholesterol | +0.2996 | 0.2048 | ±0.4096 | +1.463 | 0.1436 |  |
| Kidney disease | +0.4944 | 0.2672 | ±0.5343 | +1.851 | 0.0642 | . |
| Circulatory disease | +0.2977 | 0.2344 | ±0.4687 | +1.270 | 0.2040 |  |
| **Avg. daily range (mg/dL)** | **-0.0059** | 0.0021 | ±0.0043 | **-2.791** | **0.0053** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **867**, R² = **0.0784**, Adj R² = **0.0666**, F-statistic = **6.61** (p = **1.13e-10**), Residual SE = **2.714** on **855** df, AIC = **4203.8**, BIC = **4261.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4450** | 0.8311 | ±1.6622 | **+19.787** | **3.83e-87** | *** |
| Education: graduate level (vs college) | +0.2800 | 0.2046 | ±0.4093 | +1.369 | 0.1711 |  |
| **Education: high school or below (vs college)** | **-0.9665** | 0.3055 | ±0.6110 | **-3.164** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.0763 | 0.2425 | ±0.4850 | +0.315 | 0.7530 |  |
| Site: UW (vs UAB) | -0.1372 | 0.2288 | ±0.4575 | -0.600 | 0.5487 |  |
| **Age (years)** | **-0.0595** | 0.0104 | ±0.0209 | **-5.703** | **1.18e-08** | *** |
| BMI (kg/m2) | -0.0043 | 0.0133 | ±0.0267 | -0.319 | 0.7499 |  |
| Hypertension | -0.3283 | 0.2059 | ±0.4118 | -1.594 | 0.1108 |  |
| High cholesterol | +0.3039 | 0.2043 | ±0.4086 | +1.488 | 0.1368 |  |
| Kidney disease | +0.4426 | 0.2681 | ±0.5362 | +1.651 | 0.0988 | . |
| Circulatory disease | +0.3268 | 0.2334 | ±0.4668 | +1.400 | 0.1615 |  |
| **SD of daily means (mg/dL)** | **-0.0290** | 0.0125 | ±0.0251 | **-2.313** | **0.0207** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **867**, R² = **0.0752**, Adj R² = **0.0633**, F-statistic = **6.32** (p = **4.17e-10**), Residual SE = **2.719** on **855** df, AIC = **4206.8**, BIC = **4264.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.5674** | 0.8857 | ±1.7715 | **+17.576** | **3.77e-69** | *** |
| Education: graduate level (vs college) | +0.3049 | 0.2044 | ±0.4088 | +1.492 | 0.1357 |  |
| **Education: high school or below (vs college)** | **-0.9567** | 0.3038 | ±0.6076 | **-3.149** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.0655 | 0.2443 | ±0.4887 | +0.268 | 0.7886 |  |
| Site: UW (vs UAB) | -0.1152 | 0.2289 | ±0.4578 | -0.503 | 0.6148 |  |
| **Age (years)** | **-0.0584** | 0.0105 | ±0.0209 | **-5.584** | **2.35e-08** | *** |
| BMI (kg/m2) | -0.0052 | 0.0135 | ±0.0270 | -0.386 | 0.6997 |  |
| Hypertension | -0.3526 | 0.2075 | ±0.4149 | -1.699 | 0.0892 | . |
| High cholesterol | +0.2978 | 0.2052 | ±0.4104 | +1.451 | 0.1467 |  |
| Kidney disease | +0.4180 | 0.2677 | ±0.5354 | +1.561 | 0.1185 |  |
| Circulatory disease | +0.2963 | 0.2350 | ±0.4701 | +1.261 | 0.2074 |  |
| Time in range 70-180, pooled (%) | +0.0067 | 0.0035 | ±0.0070 | +1.922 | 0.0547 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **867**, R² = **0.0751**, Adj R² = **0.0632**, F-statistic = **6.31** (p = **4.32e-10**), Residual SE = **2.719** on **855** df, AIC = **4206.9**, BIC = **4264.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.5719** | 0.8876 | ±1.7752 | **+17.544** | **6.58e-69** | *** |
| Education: graduate level (vs college) | +0.3062 | 0.2045 | ±0.4090 | +1.497 | 0.1343 |  |
| **Education: high school or below (vs college)** | **-0.9557** | 0.3039 | ±0.6078 | **-3.145** | **0.0017** | ** |
| Site: UCSD (vs UAB) | +0.0648 | 0.2444 | ±0.4889 | +0.265 | 0.7908 |  |
| Site: UW (vs UAB) | -0.1149 | 0.2289 | ±0.4579 | -0.502 | 0.6157 |  |
| **Age (years)** | **-0.0584** | 0.0105 | ±0.0209 | **-5.578** | **2.43e-08** | *** |
| BMI (kg/m2) | -0.0052 | 0.0135 | ±0.0270 | -0.384 | 0.7010 |  |
| Hypertension | -0.3527 | 0.2075 | ±0.4150 | -1.700 | 0.0892 | . |
| High cholesterol | +0.2983 | 0.2053 | ±0.4105 | +1.453 | 0.1461 |  |
| Kidney disease | +0.4190 | 0.2677 | ±0.5353 | +1.566 | 0.1175 |  |
| Circulatory disease | +0.2962 | 0.2350 | ±0.4701 | +1.260 | 0.2075 |  |
| Avg. daily time in range 70-180 (%) | +0.0066 | 0.0035 | ±0.0070 | +1.888 | 0.0590 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **867**, R² = **0.0717**, Adj R² = **0.0598**, F-statistic = **6.00** (p = **1.70e-09**), Residual SE = **2.724** on **855** df, AIC = **4210.1**, BIC = **4267.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1836** | 0.8390 | ±1.6780 | **+19.289** | **6.59e-83** | *** |
| Education: graduate level (vs college) | +0.3331 | 0.2047 | ±0.4094 | +1.627 | 0.1037 |  |
| **Education: high school or below (vs college)** | **-1.0098** | 0.3041 | ±0.6082 | **-3.321** | **8.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.0976 | 0.2428 | ±0.4856 | +0.402 | 0.6877 |  |
| Site: UW (vs UAB) | -0.1046 | 0.2307 | ±0.4615 | -0.453 | 0.6502 |  |
| **Age (years)** | **-0.0598** | 0.0105 | ±0.0210 | **-5.707** | **1.15e-08** | *** |
| BMI (kg/m2) | -0.0059 | 0.0134 | ±0.0267 | -0.445 | 0.6563 |  |
| Hypertension | -0.3340 | 0.2074 | ±0.4147 | -1.611 | 0.1072 |  |
| High cholesterol | +0.3087 | 0.2050 | ±0.4100 | +1.506 | 0.1321 |  |
| Kidney disease | +0.3724 | 0.2662 | ±0.5323 | +1.399 | 0.1617 |  |
| Circulatory disease | +0.2917 | 0.2375 | ±0.4750 | +1.228 | 0.2194 |  |
| Any reading < 54 during wear (0/1) | -0.0648 | 0.2103 | ±0.4205 | -0.308 | 0.7580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **867**, R² = **0.0720**, Adj R² = **0.0601**, F-statistic = **6.03** (p = **1.48e-09**), Residual SE = **2.724** on **855** df, AIC = **4209.8**, BIC = **4267.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1766** | 0.8298 | ±1.6596 | **+19.495** | **1.21e-84** | *** |
| Education: graduate level (vs college) | +0.3293 | 0.2045 | ±0.4091 | +1.610 | 0.1073 |  |
| **Education: high school or below (vs college)** | **-1.0153** | 0.3042 | ±0.6083 | **-3.338** | **8.44e-04** | *** |
| Site: UCSD (vs UAB) | +0.0886 | 0.2432 | ±0.4864 | +0.364 | 0.7155 |  |
| Site: UW (vs UAB) | -0.1151 | 0.2303 | ±0.4606 | -0.500 | 0.6172 |  |
| **Age (years)** | **-0.0597** | 0.0104 | ±0.0209 | **-5.725** | **1.03e-08** | *** |
| BMI (kg/m2) | -0.0059 | 0.0134 | ±0.0268 | -0.438 | 0.6610 |  |
| Hypertension | -0.3338 | 0.2069 | ±0.4138 | -1.613 | 0.1067 |  |
| High cholesterol | +0.3097 | 0.2056 | ±0.4112 | +1.506 | 0.1320 |  |
| Kidney disease | +0.3700 | 0.2663 | ±0.5327 | +1.389 | 0.1647 |  |
| Circulatory disease | +0.2980 | 0.2380 | ±0.4759 | +1.252 | 0.2104 |  |
| Time < 54 (%) | -0.1426 | 0.1558 | ±0.3117 | -0.915 | 0.3603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **867**, R² = **0.0729**, Adj R² = **0.0610**, F-statistic = **6.11** (p = **1.05e-09**), Residual SE = **2.722** on **855** df, AIC = **4209.0**, BIC = **4266.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1721** | 0.8285 | ±1.6571 | **+19.519** | **7.60e-85** | *** |
| Education: graduate level (vs college) | +0.3244 | 0.2047 | ±0.4094 | +1.585 | 0.1130 |  |
| **Education: high school or below (vs college)** | **-1.0189** | 0.3040 | ±0.6079 | **-3.352** | **8.02e-04** | *** |
| Site: UCSD (vs UAB) | +0.0835 | 0.2433 | ±0.4865 | +0.343 | 0.7313 |  |
| Site: UW (vs UAB) | -0.1207 | 0.2299 | ±0.4599 | -0.525 | 0.5998 |  |
| **Age (years)** | **-0.0595** | 0.0104 | ±0.0208 | **-5.703** | **1.18e-08** | *** |
| BMI (kg/m2) | -0.0059 | 0.0134 | ±0.0267 | -0.442 | 0.6586 |  |
| Hypertension | -0.3330 | 0.2070 | ±0.4139 | -1.609 | 0.1077 |  |
| High cholesterol | +0.3049 | 0.2057 | ±0.4114 | +1.482 | 0.1383 |  |
| Kidney disease | +0.3704 | 0.2664 | ±0.5328 | +1.390 | 0.1644 |  |
| Circulatory disease | +0.3031 | 0.2374 | ±0.4749 | +1.276 | 0.2018 |  |
| Avg. daily time < 54 (%) | -0.2345 | 0.1777 | ±0.3554 | -1.320 | 0.1869 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **867**, R² = **0.0737**, Adj R² = **0.0618**, F-statistic = **6.19** (p = **7.48e-10**), Residual SE = **2.721** on **855** df, AIC = **4208.2**, BIC = **4265.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1753** | 0.8286 | ±1.6572 | **+19.522** | **7.19e-85** | *** |
| Education: graduate level (vs college) | +0.3201 | 0.2046 | ±0.4093 | +1.564 | 0.1178 |  |
| **Education: high school or below (vs college)** | **-1.0063** | 0.3040 | ±0.6080 | **-3.310** | **9.32e-04** | *** |
| Site: UCSD (vs UAB) | +0.0797 | 0.2426 | ±0.4852 | +0.329 | 0.7424 |  |
| Site: UW (vs UAB) | -0.1214 | 0.2296 | ±0.4592 | -0.529 | 0.5971 |  |
| **Age (years)** | **-0.0591** | 0.0104 | ±0.0209 | **-5.668** | **1.45e-08** | *** |
| BMI (kg/m2) | -0.0058 | 0.0134 | ±0.0268 | -0.433 | 0.6649 |  |
| Hypertension | -0.3342 | 0.2065 | ±0.4131 | -1.618 | 0.1056 |  |
| High cholesterol | +0.3096 | 0.2055 | ±0.4110 | +1.507 | 0.1319 |  |
| Kidney disease | +0.3739 | 0.2664 | ±0.5328 | +1.404 | 0.1604 |  |
| Circulatory disease | +0.2990 | 0.2375 | ±0.4750 | +1.259 | 0.2080 |  |
| Time 54-69, pooled (%) | -0.0889 | 0.0600 | ±0.1200 | -1.480 | 0.1388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **867**, R² = **0.0748**, Adj R² = **0.0629**, F-statistic = **6.28** (p = **4.89e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.2**, BIC = **4264.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1595** | 0.8282 | ±1.6564 | **+19.512** | **8.67e-85** | *** |
| Education: graduate level (vs college) | +0.3160 | 0.2046 | ±0.4092 | +1.544 | 0.1225 |  |
| **Education: high school or below (vs college)** | **-1.0037** | 0.3040 | ±0.6080 | **-3.302** | **9.61e-04** | *** |
| Site: UCSD (vs UAB) | +0.0777 | 0.2425 | ±0.4850 | +0.320 | 0.7487 |  |
| Site: UW (vs UAB) | -0.1251 | 0.2297 | ±0.4593 | -0.545 | 0.5859 |  |
| **Age (years)** | **-0.0588** | 0.0104 | ±0.0209 | **-5.629** | **1.81e-08** | *** |
| BMI (kg/m2) | -0.0057 | 0.0134 | ±0.0267 | -0.427 | 0.6692 |  |
| Hypertension | -0.3336 | 0.2065 | ±0.4130 | -1.615 | 0.1062 |  |
| High cholesterol | +0.3081 | 0.2054 | ±0.4108 | +1.500 | 0.1336 |  |
| Kidney disease | +0.3718 | 0.2663 | ±0.5327 | +1.396 | 0.1628 |  |
| Circulatory disease | +0.2989 | 0.2374 | ±0.4748 | +1.259 | 0.2079 |  |
| Avg. daily time 54-69 (%) | -0.1055 | 0.0588 | ±0.1176 | -1.794 | 0.0727 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **867**, R² = **0.0735**, Adj R² = **0.0615**, F-statistic = **6.16** (p = **8.37e-10**), Residual SE = **2.722** on **855** df, AIC = **4208.4**, BIC = **4265.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1806** | 0.8286 | ±1.6572 | **+19.528** | **6.34e-85** | *** |
| Education: graduate level (vs college) | +0.3212 | 0.2046 | ±0.4093 | +1.570 | 0.1165 |  |
| **Education: high school or below (vs college)** | **-1.0107** | 0.3039 | ±0.6078 | **-3.326** | **8.82e-04** | *** |
| Site: UCSD (vs UAB) | +0.0782 | 0.2428 | ±0.4856 | +0.322 | 0.7475 |  |
| Site: UW (vs UAB) | -0.1241 | 0.2298 | ±0.4596 | -0.540 | 0.5893 |  |
| **Age (years)** | **-0.0593** | 0.0104 | ±0.0209 | **-5.686** | **1.30e-08** | *** |
| BMI (kg/m2) | -0.0057 | 0.0134 | ±0.0267 | -0.429 | 0.6680 |  |
| Hypertension | -0.3332 | 0.2066 | ±0.4132 | -1.613 | 0.1068 |  |
| High cholesterol | +0.3090 | 0.2055 | ±0.4110 | +1.504 | 0.1326 |  |
| Kidney disease | +0.3720 | 0.2664 | ±0.5328 | +1.396 | 0.1626 |  |
| Circulatory disease | +0.3014 | 0.2377 | ±0.4754 | +1.268 | 0.2048 |  |
| Time < 70 (%) | -0.0686 | 0.0467 | ±0.0933 | -1.471 | 0.1414 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **867**, R² = **0.0747**, Adj R² = **0.0628**, F-statistic = **6.27** (p = **5.16e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.3**, BIC = **4264.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1646** | 0.8279 | ±1.6559 | **+19.524** | **6.86e-85** | *** |
| Education: graduate level (vs college) | +0.3161 | 0.2047 | ±0.4093 | +1.544 | 0.1225 |  |
| **Education: high school or below (vs college)** | **-1.0088** | 0.3038 | ±0.6076 | **-3.321** | **8.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.0755 | 0.2427 | ±0.4854 | +0.311 | 0.7559 |  |
| Site: UW (vs UAB) | -0.1281 | 0.2298 | ±0.4595 | -0.557 | 0.5773 |  |
| **Age (years)** | **-0.0589** | 0.0104 | ±0.0209 | **-5.643** | **1.68e-08** | *** |
| BMI (kg/m2) | -0.0057 | 0.0134 | ±0.0267 | -0.427 | 0.6694 |  |
| Hypertension | -0.3327 | 0.2066 | ±0.4132 | -1.610 | 0.1074 |  |
| High cholesterol | +0.3062 | 0.2054 | ±0.4108 | +1.491 | 0.1360 |  |
| Kidney disease | +0.3709 | 0.2664 | ±0.5327 | +1.392 | 0.1638 |  |
| Circulatory disease | +0.3024 | 0.2375 | ±0.4750 | +1.273 | 0.2029 |  |
| Avg. daily time < 70 (%) | -0.0854 | 0.0465 | ±0.0930 | -1.836 | 0.0663 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **867**, R² = **0.0735**, Adj R² = **0.0615**, F-statistic = **6.16** (p = **8.38e-10**), Residual SE = **2.722** on **855** df, AIC = **4208.4**, BIC = **4265.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.4330** | 0.9643 | ±1.9286 | **+16.004** | **1.19e-57** | *** |
| Education: graduate level (vs college) | +0.3103 | 0.2049 | ±0.4099 | +1.514 | 0.1299 |  |
| **Education: high school or below (vs college)** | **-0.9755** | 0.3043 | ±0.6086 | **-3.206** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0815 | 0.2434 | ±0.4868 | +0.335 | 0.7378 |  |
| Site: UW (vs UAB) | -0.1217 | 0.2295 | ±0.4591 | -0.530 | 0.5959 |  |
| **Age (years)** | **-0.0599** | 0.0104 | ±0.0208 | **-5.751** | **8.88e-09** | *** |
| BMI (kg/m2) | -0.0057 | 0.0135 | ±0.0270 | -0.423 | 0.6726 |  |
| Hypertension | -0.3356 | 0.2067 | ±0.4133 | -1.624 | 0.1044 |  |
| High cholesterol | +0.3060 | 0.2053 | ±0.4106 | +1.491 | 0.1361 |  |
| Kidney disease | +0.3966 | 0.2678 | ±0.5355 | +1.481 | 0.1386 |  |
| Circulatory disease | +0.2927 | 0.2358 | ±0.4717 | +1.241 | 0.2145 |  |
| Time 54-250, pooled (%) | +0.0080 | 0.0055 | ±0.0110 | +1.453 | 0.1462 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **867**, R² = **0.0733**, Adj R² = **0.0613**, F-statistic = **6.14** (p = **9.12e-10**), Residual SE = **2.722** on **855** df, AIC = **4208.6**, BIC = **4265.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.4600** | 0.9680 | ±1.9359 | **+15.972** | **2.02e-57** | *** |
| Education: graduate level (vs college) | +0.3118 | 0.2050 | ±0.4101 | +1.521 | 0.1283 |  |
| **Education: high school or below (vs college)** | **-0.9774** | 0.3042 | ±0.6084 | **-3.213** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0825 | 0.2435 | ±0.4869 | +0.339 | 0.7348 |  |
| Site: UW (vs UAB) | -0.1196 | 0.2295 | ±0.4589 | -0.521 | 0.6023 |  |
| **Age (years)** | **-0.0598** | 0.0104 | ±0.0208 | **-5.741** | **9.42e-09** | *** |
| BMI (kg/m2) | -0.0057 | 0.0135 | ±0.0270 | -0.424 | 0.6719 |  |
| Hypertension | -0.3363 | 0.2067 | ±0.4134 | -1.627 | 0.1037 |  |
| High cholesterol | +0.3064 | 0.2054 | ±0.4108 | +1.492 | 0.1358 |  |
| Kidney disease | +0.3969 | 0.2679 | ±0.5357 | +1.482 | 0.1384 |  |
| Circulatory disease | +0.2932 | 0.2359 | ±0.4718 | +1.243 | 0.2138 |  |
| Avg. daily time 54-250 (%) | +0.0076 | 0.0055 | ±0.0110 | +1.380 | 0.1677 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **867**, R² = **0.0742**, Adj R² = **0.0623**, F-statistic = **6.23** (p = **6.25e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.8**, BIC = **4264.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1849** | 0.8310 | ±1.6621 | **+19.476** | **1.77e-84** | *** |
| Education: graduate level (vs college) | +0.3221 | 0.2041 | ±0.4082 | +1.578 | 0.1146 |  |
| **Education: high school or below (vs college)** | **-0.9731** | 0.3039 | ±0.6077 | **-3.202** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.0784 | 0.2439 | ±0.4879 | +0.321 | 0.7480 |  |
| Site: UW (vs UAB) | -0.0923 | 0.2289 | ±0.4578 | -0.403 | 0.6867 |  |
| **Age (years)** | **-0.0576** | 0.0106 | ±0.0211 | **-5.454** | **4.92e-08** | *** |
| BMI (kg/m2) | -0.0054 | 0.0134 | ±0.0269 | -0.402 | 0.6876 |  |
| Hypertension | -0.3611 | 0.2088 | ±0.4176 | -1.729 | 0.0838 | . |
| High cholesterol | +0.2996 | 0.2058 | ±0.4115 | +1.456 | 0.1453 |  |
| Kidney disease | +0.4086 | 0.2667 | ±0.5333 | +1.532 | 0.1255 |  |
| Circulatory disease | +0.2926 | 0.2349 | ±0.4697 | +1.246 | 0.2129 |  |
| Time 181-250, pooled (%) | -0.0094 | 0.0059 | ±0.0117 | -1.593 | 0.1111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **867**, R² = **0.0742**, Adj R² = **0.0623**, F-statistic = **6.23** (p = **6.20e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.7**, BIC = **4264.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1872** | 0.8316 | ±1.6632 | **+19.466** | **2.15e-84** | *** |
| Education: graduate level (vs college) | +0.3230 | 0.2042 | ±0.4083 | +1.582 | 0.1137 |  |
| **Education: high school or below (vs college)** | **-0.9708** | 0.3041 | ±0.6082 | **-3.192** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.0766 | 0.2441 | ±0.4881 | +0.314 | 0.7536 |  |
| Site: UW (vs UAB) | -0.0938 | 0.2290 | ±0.4579 | -0.409 | 0.6822 |  |
| **Age (years)** | **-0.0577** | 0.0106 | ±0.0211 | **-5.466** | **4.60e-08** | *** |
| BMI (kg/m2) | -0.0054 | 0.0135 | ±0.0269 | -0.399 | 0.6897 |  |
| Hypertension | -0.3606 | 0.2087 | ±0.4174 | -1.728 | 0.0840 | . |
| High cholesterol | +0.3002 | 0.2058 | ±0.4115 | +1.459 | 0.1446 |  |
| Kidney disease | +0.4093 | 0.2665 | ±0.5330 | +1.536 | 0.1246 |  |
| Circulatory disease | +0.2919 | 0.2348 | ±0.4697 | +1.243 | 0.2139 |  |
| Avg. daily time 181-250 (%) | -0.0092 | 0.0058 | ±0.0116 | -1.587 | 0.1124 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **867**, R² = **0.0748**, Adj R² = **0.0629**, F-statistic = **6.28** (p = **4.96e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.2**, BIC = **4264.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2317** | 0.8320 | ±1.6640 | **+19.510** | **9.09e-85** | *** |
| Education: graduate level (vs college) | +0.3081 | 0.2044 | ±0.4088 | +1.507 | 0.1317 |  |
| **Education: high school or below (vs college)** | **-0.9598** | 0.3038 | ±0.6077 | **-3.159** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.0705 | 0.2442 | ±0.4883 | +0.289 | 0.7729 |  |
| Site: UW (vs UAB) | -0.1117 | 0.2289 | ±0.4577 | -0.488 | 0.6255 |  |
| **Age (years)** | **-0.0585** | 0.0105 | ±0.0209 | **-5.595** | **2.21e-08** | *** |
| BMI (kg/m2) | -0.0053 | 0.0135 | ±0.0270 | -0.394 | 0.6937 |  |
| Hypertension | -0.3519 | 0.2076 | ±0.4151 | -1.695 | 0.0900 | . |
| High cholesterol | +0.2992 | 0.2053 | ±0.4106 | +1.457 | 0.1451 |  |
| Kidney disease | +0.4150 | 0.2677 | ±0.5354 | +1.550 | 0.1211 |  |
| Circulatory disease | +0.2944 | 0.2350 | ±0.4701 | +1.253 | 0.2103 |  |
| Time > 180 (%) | -0.0062 | 0.0035 | ±0.0069 | -1.804 | 0.0712 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **867**, R² = **0.0746**, Adj R² = **0.0627**, F-statistic = **6.26** (p = **5.33e-10**), Residual SE = **2.720** on **855** df, AIC = **4207.4**, BIC = **4264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2253** | 0.8321 | ±1.6642 | **+19.499** | **1.11e-84** | *** |
| Education: graduate level (vs college) | +0.3097 | 0.2045 | ±0.4090 | +1.515 | 0.1298 |  |
| **Education: high school or below (vs college)** | **-0.9599** | 0.3039 | ±0.6079 | **-3.158** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.0700 | 0.2443 | ±0.4886 | +0.287 | 0.7743 |  |
| Site: UW (vs UAB) | -0.1115 | 0.2289 | ±0.4578 | -0.487 | 0.6263 |  |
| **Age (years)** | **-0.0585** | 0.0105 | ±0.0209 | **-5.594** | **2.22e-08** | *** |
| BMI (kg/m2) | -0.0053 | 0.0135 | ±0.0270 | -0.393 | 0.6946 |  |
| Hypertension | -0.3517 | 0.2076 | ±0.4152 | -1.695 | 0.0902 | . |
| High cholesterol | +0.2999 | 0.2054 | ±0.4107 | +1.461 | 0.1441 |  |
| Kidney disease | +0.4153 | 0.2677 | ±0.5353 | +1.552 | 0.1207 |  |
| Circulatory disease | +0.2944 | 0.2351 | ±0.4701 | +1.253 | 0.2103 |  |
| Avg. daily time > 180 (%) | -0.0060 | 0.0035 | ±0.0069 | -1.744 | 0.0811 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **867**, R² = **0.0750**, Adj R² = **0.0631**, F-statistic = **6.30** (p = **4.49e-10**), Residual SE = **2.719** on **855** df, AIC = **4207.0**, BIC = **4264.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2214** | 0.8314 | ±1.6629 | **+19.510** | **9.05e-85** | *** |
| Education: graduate level (vs college) | +0.3010 | 0.2041 | ±0.4082 | +1.475 | 0.1403 |  |
| **Education: high school or below (vs college)** | **-0.9618** | 0.3037 | ±0.6073 | **-3.167** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0652 | 0.2443 | ±0.4886 | +0.267 | 0.7895 |  |
| Site: UW (vs UAB) | -0.1094 | 0.2288 | ±0.4576 | -0.478 | 0.6325 |  |
| **Age (years)** | **-0.0593** | 0.0104 | ±0.0209 | **-5.683** | **1.32e-08** | *** |
| BMI (kg/m2) | -0.0042 | 0.0136 | ±0.0271 | -0.307 | 0.7589 |  |
| Hypertension | -0.3542 | 0.2074 | ±0.4148 | -1.708 | 0.0877 | . |
| High cholesterol | +0.2970 | 0.2051 | ±0.4102 | +1.448 | 0.1477 |  |
| Kidney disease | +0.4104 | 0.2671 | ±0.5341 | +1.537 | 0.1244 |  |
| Circulatory disease | +0.2971 | 0.2347 | ±0.4694 | +1.266 | 0.2056 |  |
| Nocturnal time > 180 (%) | -0.0062 | 0.0033 | ±0.0067 | -1.855 | 0.0636 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **867**, R² = **0.0782**, Adj R² = **0.0664**, F-statistic = **6.60** (p = **1.21e-10**), Residual SE = **2.715** on **855** df, AIC = **4204.0**, BIC = **4261.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3032** | 0.8257 | ±1.6515 | **+19.744** | **9.06e-87** | *** |
| Education: graduate level (vs college) | +0.2870 | 0.2035 | ±0.4070 | +1.410 | 0.1585 |  |
| **Education: high school or below (vs college)** | **-0.9774** | 0.3034 | ±0.6068 | **-3.221** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0806 | 0.2418 | ±0.4837 | +0.333 | 0.7388 |  |
| Site: UW (vs UAB) | -0.0791 | 0.2288 | ±0.4576 | -0.346 | 0.7294 |  |
| **Age (years)** | **-0.0557** | 0.0108 | ±0.0215 | **-5.183** | **2.19e-07** | *** |
| BMI (kg/m2) | -0.0078 | 0.0134 | ±0.0268 | -0.581 | 0.5611 |  |
| Hypertension | -0.3587 | 0.2071 | ±0.4141 | -1.732 | 0.0832 | . |
| High cholesterol | +0.3044 | 0.2054 | ±0.4107 | +1.483 | 0.1382 |  |
| Kidney disease | +0.4359 | 0.2671 | ±0.5343 | +1.632 | 0.1028 |  |
| Circulatory disease | +0.2774 | 0.2346 | ±0.4693 | +1.182 | 0.2371 |  |
| **Any reading > 250 during wear (0/1)** | **-0.4900** | 0.1945 | ±0.3890 | **-2.520** | **0.0118** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **867**, R² = **0.0734**, Adj R² = **0.0615**, F-statistic = **6.16** (p = **8.56e-10**), Residual SE = **2.722** on **855** df, AIC = **4208.5**, BIC = **4265.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2274** | 0.8323 | ±1.6646 | **+19.498** | **1.15e-84** | *** |
| Education: graduate level (vs college) | +0.3109 | 0.2049 | ±0.4098 | +1.517 | 0.1292 |  |
| **Education: high school or below (vs college)** | **-0.9755** | 0.3043 | ±0.6087 | **-3.205** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0826 | 0.2434 | ±0.4867 | +0.339 | 0.7343 |  |
| Site: UW (vs UAB) | -0.1205 | 0.2295 | ±0.4589 | -0.525 | 0.5996 |  |
| **Age (years)** | **-0.0599** | 0.0104 | ±0.0208 | **-5.750** | **8.93e-09** | *** |
| BMI (kg/m2) | -0.0057 | 0.0135 | ±0.0270 | -0.424 | 0.6714 |  |
| Hypertension | -0.3358 | 0.2067 | ±0.4133 | -1.625 | 0.1042 |  |
| High cholesterol | +0.3063 | 0.2053 | ±0.4107 | +1.492 | 0.1358 |  |
| Kidney disease | +0.3965 | 0.2678 | ±0.5355 | +1.481 | 0.1387 |  |
| Circulatory disease | +0.2921 | 0.2358 | ±0.4716 | +1.239 | 0.2155 |  |
| Time > 250 (%) | -0.0078 | 0.0055 | ±0.0109 | -1.434 | 0.1516 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 867)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **867**, R² = **0.0732**, Adj R² = **0.0612**, F-statistic = **6.14** (p = **9.44e-10**), Residual SE = **2.722** on **855** df, AIC = **4208.7**, BIC = **4265.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2163** | 0.8319 | ±1.6637 | **+19.494** | **1.23e-84** | *** |
| Education: graduate level (vs college) | +0.3127 | 0.2050 | ±0.4101 | +1.525 | 0.1273 |  |
| **Education: high school or below (vs college)** | **-0.9777** | 0.3042 | ±0.6085 | **-3.214** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0836 | 0.2434 | ±0.4868 | +0.344 | 0.7312 |  |
| Site: UW (vs UAB) | -0.1184 | 0.2294 | ±0.4588 | -0.516 | 0.6059 |  |
| **Age (years)** | **-0.0598** | 0.0104 | ±0.0208 | **-5.741** | **9.43e-09** | *** |
| BMI (kg/m2) | -0.0057 | 0.0135 | ±0.0270 | -0.425 | 0.6708 |  |
| Hypertension | -0.3365 | 0.2067 | ±0.4134 | -1.628 | 0.1036 |  |
| High cholesterol | +0.3068 | 0.2054 | ±0.4108 | +1.493 | 0.1353 |  |
| Kidney disease | +0.3964 | 0.2678 | ±0.5357 | +1.480 | 0.1389 |  |
| Circulatory disease | +0.2926 | 0.2359 | ±0.4717 | +1.241 | 0.2148 |  |
| Avg. daily time > 250 (%) | -0.0074 | 0.0055 | ±0.0110 | -1.346 | 0.1783 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 93 single-predictor tests; 39 with raw p < 0.05 (about 5 expected by chance); FDR rule applied to 93 tests (samples with n >= 500), of which **8** are significant at BH q < 0.05 in the all-tests family and 10 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 867): best single predictor out of sample is **SD (pooled)** (CV R² 0.063 vs 0.054 for covariates alone, gain +0.009; -0.349 per SD, p = 0.002, q = 0.035). FDR-robust associations (4): SD (pooled) (lower outcome, -0.349 per SD, q = 0.035); SD of daily means (lower outcome, -0.337 per SD, q = 0.040); Mean/SD (higher outcome, +0.305 per SD, q = 0.043); SD (daily avg) (lower outcome, -0.331 per SD, q = 0.046).
- **Cognitive impairment (MoCA < 26)** (n = 867): best single predictor out of sample is **Nocturnal mean** (CV AUC 0.646 vs 0.643 for covariates alone, gain +0.004; OR 1.19 per SD, p = 0.016, q = 0.112). No association survives FDR; nominal only: SD of daily means (p = 0.008), Nocturnal mean (p = 0.016), SD (pooled) (p = 0.016), Mean glucose (p = 0.018).
- **MoCA memory index score (0-15)** (n = 867): best single predictor out of sample is **SD (pooled)** (CV R² 0.036 vs 0.029 for covariates alone, gain +0.007; -0.28 per SD, p = 0.002, q = 0.037). FDR-robust associations (4): SD (pooled) (lower outcome, -0.28 per SD, q = 0.037); CV (lower outcome, -0.276 per SD, q = 0.037); SD (daily avg) (lower outcome, -0.269 per SD, q = 0.040); Mean/SD (higher outcome, +0.257 per SD, q = 0.042).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA total score (0-30) (+0.009, via SD (pooled)); MoCA memory index score (0-15) (+0.007, via SD (pooled)); Cognitive impairment (MoCA < 26) (+0.004, via Nocturnal mean). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (8 FDR-significant / 19 raw-significant of 24); CGM level (0 FDR-significant / 7 raw-significant of 9); Band > 180 (0 FDR-significant / 6 raw-significant of 9).
Level metrics: 0 FDR-significant (7 raw); variability metrics: 8 FDR-significant (19 raw); HbA1c alone: 0 FDR-significant (2 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (SD (pooled), ΔAIC -5.8); Cognitive impairment (SD of daily means, ΔAIC -3.6); MoCA memory index score (SD (pooled), ΔAIC -4.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
