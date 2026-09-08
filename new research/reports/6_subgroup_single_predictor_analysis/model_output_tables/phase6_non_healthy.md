# Phase 6 model output tables - All (analysis base) - Non-healthy group (T2D non-insulin + T2D insulin)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 865; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **865**, R² = **0.1224**, Adj R² = **0.1121**, F-statistic = **11.91** (p = **2.11e-19**), Residual SE = **4.882** on **854** df, AIC = **5208.7**, BIC = **5261.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4708** | 1.4406 | ±2.8813 | **+7.268** | **3.64e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4728** | 0.3493 | ±0.6986 | **-4.216** | **2.48e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2177** | 0.5734 | ±1.1468 | **+2.124** | **0.0337** | * |
| Site: UCSD (vs UAB) | +0.4734 | 0.4399 | ±0.8798 | +1.076 | 0.2819 |  |
| Site: UW (vs UAB) | +0.0949 | 0.4116 | ±0.8233 | +0.230 | 0.8177 |  |
| **Age (years)** | **-0.1060** | 0.0159 | ±0.0319 | **-6.656** | **2.82e-11** | *** |
| **BMI (kg/m2)** | **+0.0485** | 0.0234 | ±0.0467 | **+2.077** | **0.0378** | * |
| Hypertension | -0.0296 | 0.3730 | ±0.7460 | -0.079 | 0.9367 |  |
| High cholesterol | +0.6042 | 0.3529 | ±0.7058 | +1.712 | 0.0869 | . |
| **Kidney disease** | **+1.0421** | 0.4950 | ±0.9901 | **+2.105** | **0.0353** | * |
| **Circulatory disease** | **+1.3380** | 0.4669 | ±0.9337 | **+2.866** | **0.0042** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **865**, R² = **0.1257**, Adj R² = **0.1144**, F-statistic = **11.15** (p = **1.68e-19**), Residual SE = **4.875** on **853** df, AIC = **5207.4**, BIC = **5264.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.0476** | 1.7054 | ±3.4109 | **+5.305** | **1.13e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4151** | 0.3509 | ±0.7019 | **-4.032** | **5.53e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1199** | 0.5673 | ±1.1347 | **+1.974** | **0.0484** | * |
| Site: UCSD (vs UAB) | +0.5087 | 0.4384 | ±0.8768 | +1.160 | 0.2459 |  |
| Site: UW (vs UAB) | +0.1252 | 0.4128 | ±0.8256 | +0.303 | 0.7616 |  |
| **Age (years)** | **-0.1072** | 0.0160 | ±0.0319 | **-6.713** | **1.90e-11** | *** |
| BMI (kg/m2) | +0.0449 | 0.0237 | ±0.0473 | +1.898 | 0.0577 | . |
| Hypertension | -0.0323 | 0.3737 | ±0.7473 | -0.087 | 0.9311 |  |
| High cholesterol | +0.6041 | 0.3525 | ±0.7049 | +1.714 | 0.0866 | . |
| **Kidney disease** | **+1.0277** | 0.4981 | ±0.9963 | **+2.063** | **0.0391** | * |
| **Circulatory disease** | **+1.3289** | 0.4655 | ±0.9311 | **+2.855** | **0.0043** | ** |
| HbA1c (%) | +0.2377 | 0.1523 | ±0.3046 | +1.561 | 0.1185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **865**, R² = **0.1233**, Adj R² = **0.1120**, F-statistic = **10.91** (p = **4.96e-19**), Residual SE = **4.882** on **853** df, AIC = **5209.7**, BIC = **5266.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9233** | 1.5588 | ±3.1177 | **+6.366** | **1.94e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4471** | 0.3509 | ±0.7018 | **-4.124** | **3.72e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1736** | 0.5724 | ±1.1448 | **+2.050** | **0.0403** | * |
| Site: UCSD (vs UAB) | +0.4977 | 0.4394 | ±0.8787 | +1.133 | 0.2573 |  |
| Site: UW (vs UAB) | +0.1058 | 0.4124 | ±0.8248 | +0.256 | 0.7976 |  |
| **Age (years)** | **-0.1067** | 0.0160 | ±0.0320 | **-6.666** | **2.63e-11** | *** |
| **BMI (kg/m2)** | **+0.0477** | 0.0235 | ±0.0469 | **+2.034** | **0.0420** | * |
| Hypertension | -0.0218 | 0.3735 | ±0.7470 | -0.058 | 0.9535 |  |
| High cholesterol | +0.6122 | 0.3531 | ±0.7061 | +1.734 | 0.0830 | . |
| **Kidney disease** | **+1.0077** | 0.5015 | ±1.0029 | **+2.009** | **0.0445** | * |
| **Circulatory disease** | **+1.3331** | 0.4662 | ±0.9324 | **+2.859** | **0.0042** | ** |
| Mean glucose (mg/dL) | +0.0039 | 0.0045 | ±0.0091 | +0.864 | 0.3877 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **865**, R² = **0.1233**, Adj R² = **0.1120**, F-statistic = **10.91** (p = **4.96e-19**), Residual SE = **4.882** on **853** df, AIC = **5209.7**, BIC = **5266.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.3816** | 1.8866 | ±3.7732 | **+4.973** | **6.60e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4471** | 0.3509 | ±0.7018 | **-4.124** | **3.72e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1736** | 0.5724 | ±1.1448 | **+2.050** | **0.0403** | * |
| Site: UCSD (vs UAB) | +0.4977 | 0.4394 | ±0.8787 | +1.133 | 0.2573 |  |
| Site: UW (vs UAB) | +0.1058 | 0.4124 | ±0.8248 | +0.256 | 0.7976 |  |
| **Age (years)** | **-0.1067** | 0.0160 | ±0.0320 | **-6.666** | **2.63e-11** | *** |
| **BMI (kg/m2)** | **+0.0477** | 0.0235 | ±0.0469 | **+2.034** | **0.0420** | * |
| Hypertension | -0.0218 | 0.3735 | ±0.7470 | -0.058 | 0.9535 |  |
| High cholesterol | +0.6122 | 0.3531 | ±0.7061 | +1.734 | 0.0830 | . |
| **Kidney disease** | **+1.0077** | 0.5015 | ±1.0029 | **+2.009** | **0.0445** | * |
| **Circulatory disease** | **+1.3331** | 0.4662 | ±0.9324 | **+2.859** | **0.0042** | ** |
| GMI (%) | +0.1636 | 0.1894 | ±0.3788 | +0.864 | 0.3877 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **865**, R² = **0.1249**, Adj R² = **0.1136**, F-statistic = **11.07** (p = **2.42e-19**), Residual SE = **4.878** on **853** df, AIC = **5208.2**, BIC = **5265.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.5813** | 1.5686 | ±3.1372 | **+6.108** | **1.01e-09** | *** |
| **Education: graduate level (vs college)** | **-1.4312** | 0.3512 | ±0.7024 | **-4.075** | **4.59e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1497** | 0.5713 | ±1.1427 | **+2.012** | **0.0442** | * |
| Site: UCSD (vs UAB) | +0.5115 | 0.4382 | ±0.8763 | +1.167 | 0.2430 |  |
| Site: UW (vs UAB) | +0.0991 | 0.4129 | ±0.8257 | +0.240 | 0.8103 |  |
| **Age (years)** | **-0.1059** | 0.0160 | ±0.0319 | **-6.631** | **3.33e-11** | *** |
| BMI (kg/m2) | +0.0458 | 0.0235 | ±0.0471 | +1.946 | 0.0516 | . |
| Hypertension | -0.0114 | 0.3733 | ±0.7467 | -0.030 | 0.9757 |  |
| High cholesterol | +0.6136 | 0.3524 | ±0.7049 | +1.741 | 0.0817 | . |
| **Kidney disease** | **+1.0046** | 0.5005 | ±1.0010 | **+2.007** | **0.0447** | * |
| **Circulatory disease** | **+1.3296** | 0.4656 | ±0.9311 | **+2.856** | **0.0043** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0063 | 0.0044 | ±0.0088 | +1.440 | 0.1498 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **865**, R² = **0.1250**, Adj R² = **0.1137**, F-statistic = **11.07** (p = **2.35e-19**), Residual SE = **4.878** on **853** df, AIC = **5208.1**, BIC = **5265.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9390** | 1.4783 | ±2.9566 | **+6.723** | **1.78e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4232** | 0.3506 | ±0.7013 | **-4.059** | **4.93e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1342** | 0.5758 | ±1.1516 | **+1.970** | **0.0489** | * |
| Site: UCSD (vs UAB) | +0.5138 | 0.4385 | ±0.8769 | +1.172 | 0.2413 |  |
| Site: UW (vs UAB) | +0.1392 | 0.4124 | ±0.8248 | +0.338 | 0.7357 |  |
| **Age (years)** | **-0.1087** | 0.0161 | ±0.0321 | **-6.766** | **1.32e-11** | *** |
| **BMI (kg/m2)** | **+0.0484** | 0.0235 | ±0.0471 | **+2.058** | **0.0396** | * |
| Hypertension | -0.0233 | 0.3731 | ±0.7463 | -0.062 | 0.9502 |  |
| High cholesterol | +0.6243 | 0.3525 | ±0.7049 | +1.771 | 0.0765 | . |
| Kidney disease | +0.9152 | 0.5093 | ±1.0187 | +1.797 | 0.0724 | . |
| **Circulatory disease** | **+1.3252** | 0.4665 | ±0.9331 | **+2.840** | **0.0045** | ** |
| Glucose SD, pooled (mg/dL) | +0.0196 | 0.0130 | ±0.0260 | +1.504 | 0.1325 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **865**, R² = **0.1235**, Adj R² = **0.1122**, F-statistic = **10.93** (p = **4.47e-19**), Residual SE = **4.881** on **853** df, AIC = **5209.5**, BIC = **5266.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0900** | 1.4763 | ±2.9526 | **+6.835** | **8.23e-12** | *** |
| **Education: graduate level (vs college)** | **-1.4420** | 0.3500 | ±0.7001 | **-4.120** | **3.80e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1575** | 0.5781 | ±1.1562 | **+2.002** | **0.0453** | * |
| Site: UCSD (vs UAB) | +0.4989 | 0.4396 | ±0.8793 | +1.135 | 0.2564 |  |
| Site: UW (vs UAB) | +0.1209 | 0.4125 | ±0.8251 | +0.293 | 0.7694 |  |
| **Age (years)** | **-0.1080** | 0.0161 | ±0.0322 | **-6.702** | **2.06e-11** | *** |
| **BMI (kg/m2)** | **+0.0492** | 0.0235 | ±0.0469 | **+2.098** | **0.0359** | * |
| Hypertension | -0.0232 | 0.3734 | ±0.7468 | -0.062 | 0.9505 |  |
| High cholesterol | +0.6176 | 0.3531 | ±0.7062 | +1.749 | 0.0803 | . |
| Kidney disease | +0.9539 | 0.5100 | ±1.0201 | +1.870 | 0.0614 | . |
| **Circulatory disease** | **+1.3335** | 0.4670 | ±0.9341 | **+2.855** | **0.0043** | ** |
| Avg. daily SD (mg/dL) | +0.0151 | 0.0148 | ±0.0296 | +1.016 | 0.3096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **865**, R² = **0.1232**, Adj R² = **0.1119**, F-statistic = **10.89** (p = **5.26e-19**), Residual SE = **4.882** on **853** df, AIC = **5209.9**, BIC = **5267.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9911** | 1.5436 | ±3.0872 | **+6.473** | **9.64e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4535** | 0.3495 | ±0.6989 | **-4.159** | **3.19e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1819** | 0.5794 | ±1.1588 | **+2.040** | **0.0414** | * |
| Site: UCSD (vs UAB) | +0.4898 | 0.4400 | ±0.8801 | +1.113 | 0.2656 |  |
| Site: UW (vs UAB) | +0.1236 | 0.4127 | ±0.8253 | +0.300 | 0.7645 |  |
| **Age (years)** | **-0.1079** | 0.0160 | ±0.0320 | **-6.739** | **1.59e-11** | *** |
| **BMI (kg/m2)** | **+0.0491** | 0.0234 | ±0.0469 | **+2.096** | **0.0361** | * |
| Hypertension | -0.0344 | 0.3734 | ±0.7468 | -0.092 | 0.9267 |  |
| High cholesterol | +0.6144 | 0.3532 | ±0.7064 | +1.740 | 0.0819 | . |
| Kidney disease | +0.9675 | 0.5049 | ±1.0098 | +1.916 | 0.0553 | . |
| **Circulatory disease** | **+1.3305** | 0.4682 | ±0.9364 | **+2.842** | **0.0045** | ** |
| CV (%) | +0.0258 | 0.0301 | ±0.0603 | +0.857 | 0.3916 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **865**, R² = **0.1230**, Adj R² = **0.1117**, F-statistic = **10.88** (p = **5.71e-19**), Residual SE = **4.883** on **853** df, AIC = **5210.0**, BIC = **5267.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.0604** | 1.6419 | ±3.2838 | **+6.736** | **1.62e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4560** | 0.3498 | ±0.6997 | **-4.162** | **3.16e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1830** | 0.5798 | ±1.1595 | **+2.041** | **0.0413** | * |
| Site: UCSD (vs UAB) | +0.4832 | 0.4401 | ±0.8803 | +1.098 | 0.2723 |  |
| Site: UW (vs UAB) | +0.1172 | 0.4128 | ±0.8256 | +0.284 | 0.7764 |  |
| **Age (years)** | **-0.1078** | 0.0160 | ±0.0320 | **-6.732** | **1.67e-11** | *** |
| **BMI (kg/m2)** | **+0.0490** | 0.0234 | ±0.0468 | **+2.094** | **0.0362** | * |
| Hypertension | -0.0336 | 0.3735 | ±0.7470 | -0.090 | 0.9282 |  |
| High cholesterol | +0.6111 | 0.3532 | ±0.7064 | +1.730 | 0.0836 | . |
| **Kidney disease** | **+0.9893** | 0.5022 | ±1.0043 | **+1.970** | **0.0488** | * |
| **Circulatory disease** | **+1.3276** | 0.4679 | ±0.9358 | **+2.837** | **0.0045** | ** |
| Mean / SD ratio | -0.1021 | 0.1335 | ±0.2669 | -0.765 | 0.4444 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **865**, R² = **0.1225**, Adj R² = **0.1112**, F-statistic = **10.82** (p = **7.16e-19**), Residual SE = **4.884** on **853** df, AIC = **5210.5**, BIC = **5267.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.7133** | 1.6312 | ±3.2624 | **+6.568** | **5.11e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4651** | 0.3497 | ±0.6993 | **-4.190** | **2.79e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2039** | 0.5790 | ±1.1581 | **+2.079** | **0.0376** | * |
| Site: UCSD (vs UAB) | +0.4740 | 0.4401 | ±0.8803 | +1.077 | 0.2815 |  |
| Site: UW (vs UAB) | +0.1028 | 0.4127 | ±0.8253 | +0.249 | 0.8033 |  |
| **Age (years)** | **-0.1068** | 0.0161 | ±0.0321 | **-6.646** | **3.00e-11** | *** |
| **BMI (kg/m2)** | **+0.0490** | 0.0233 | ±0.0467 | **+2.097** | **0.0360** | * |
| Hypertension | -0.0316 | 0.3736 | ±0.7471 | -0.085 | 0.9325 |  |
| High cholesterol | +0.6073 | 0.3536 | ±0.7072 | +1.718 | 0.0859 | . |
| **Kidney disease** | **+1.0226** | 0.5001 | ±1.0003 | **+2.045** | **0.0409** | * |
| **Circulatory disease** | **+1.3376** | 0.4676 | ±0.9351 | **+2.861** | **0.0042** | ** |
| Avg. daily mean/SD | -0.0367 | 0.1102 | ±0.2203 | -0.333 | 0.7390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **865**, R² = **0.1324**, Adj R² = **0.1212**, F-statistic = **11.83** (p = **7.98e-21**), Residual SE = **4.857** on **853** df, AIC = **5200.7**, BIC = **5257.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0111** | 1.6647 | ±3.3293 | **+4.812** | **1.49e-06** | *** |
| **Education: graduate level (vs college)** | **-1.3765** | 0.3505 | ±0.7011 | **-3.927** | **8.60e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1118** | 0.5656 | ±1.1311 | **+1.966** | **0.0493** | * |
| Site: UCSD (vs UAB) | +0.5334 | 0.4357 | ±0.8714 | +1.224 | 0.2209 |  |
| Site: UW (vs UAB) | +0.2413 | 0.4138 | ±0.8276 | +0.583 | 0.5597 |  |
| **Age (years)** | **-0.1049** | 0.0159 | ±0.0318 | **-6.608** | **3.90e-11** | *** |
| **BMI (kg/m2)** | **+0.0478** | 0.0234 | ±0.0469 | **+2.038** | **0.0416** | * |
| Hypertension | -0.0009 | 0.3729 | ±0.7458 | -0.002 | 0.9981 |  |
| High cholesterol | +0.6229 | 0.3500 | ±0.7000 | +1.780 | 0.0751 | . |
| Kidney disease | +0.9065 | 0.5026 | ±1.0052 | +1.804 | 0.0713 | . |
| **Circulatory disease** | **+1.3353** | 0.4669 | ±0.9339 | **+2.860** | **0.0042** | ** |
| **MAG (mg/dL/h)** | **+0.0542** | 0.0182 | ±0.0364 | **+2.977** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **865**, R² = **0.1234**, Adj R² = **0.1121**, F-statistic = **10.91** (p = **4.83e-19**), Residual SE = **4.882** on **853** df, AIC = **5209.7**, BIC = **5266.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9747** | 1.5240 | ±3.0481 | **+6.545** | **5.95e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4419** | 0.3500 | ±0.7001 | **-4.119** | **3.80e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1648** | 0.5782 | ±1.1565 | **+2.014** | **0.0440** | * |
| Site: UCSD (vs UAB) | +0.4998 | 0.4396 | ±0.8793 | +1.137 | 0.2557 |  |
| Site: UW (vs UAB) | +0.1184 | 0.4125 | ±0.8249 | +0.287 | 0.7740 |  |
| **Age (years)** | **-0.1075** | 0.0160 | ±0.0321 | **-6.701** | **2.07e-11** | *** |
| **BMI (kg/m2)** | **+0.0496** | 0.0235 | ±0.0470 | **+2.113** | **0.0346** | * |
| Hypertension | -0.0165 | 0.3738 | ±0.7476 | -0.044 | 0.9648 |  |
| High cholesterol | +0.6121 | 0.3530 | ±0.7060 | +1.734 | 0.0829 | . |
| Kidney disease | +0.9630 | 0.5085 | ±1.0171 | +1.894 | 0.0583 | . |
| **Circulatory disease** | **+1.3315** | 0.4671 | ±0.9342 | **+2.851** | **0.0044** | ** |
| Avg. daily range (mg/dL) | +0.0039 | 0.0041 | ±0.0083 | +0.944 | 0.3451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **865**, R² = **0.1345**, Adj R² = **0.1234**, F-statistic = **12.05** (p = **3.01e-21**), Residual SE = **4.851** on **853** df, AIC = **5198.6**, BIC = **5255.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7713** | 1.4446 | ±2.8892 | **+6.764** | **1.34e-11** | *** |
| **Education: graduate level (vs college)** | **-1.3416** | 0.3508 | ±0.7016 | **-3.825** | **1.31e-04** | *** |
| **Education: high school or below (vs college)** | **+1.1160** | 0.5669 | ±1.1337 | **+1.969** | **0.0490** | * |
| Site: UCSD (vs UAB) | +0.5371 | 0.4344 | ±0.8687 | +1.236 | 0.2163 |  |
| Site: UW (vs UAB) | +0.1871 | 0.4088 | ±0.8176 | +0.458 | 0.6472 |  |
| **Age (years)** | **-0.1064** | 0.0160 | ±0.0319 | **-6.663** | **2.69e-11** | *** |
| BMI (kg/m2) | +0.0437 | 0.0234 | ±0.0467 | +1.870 | 0.0615 | . |
| Hypertension | -0.0515 | 0.3723 | ±0.7446 | -0.138 | 0.8899 |  |
| High cholesterol | +0.6233 | 0.3496 | ±0.6991 | +1.783 | 0.0746 | . |
| Kidney disease | +0.8744 | 0.4994 | ±0.9987 | +1.751 | 0.0799 | . |
| **Circulatory disease** | **+1.2405** | 0.4621 | ±0.9243 | **+2.684** | **0.0073** | ** |
| **SD of daily means (mg/dL)** | **+0.0713** | 0.0212 | ±0.0425 | **+3.356** | **7.90e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **865**, R² = **0.1240**, Adj R² = **0.1127**, F-statistic = **10.98** (p = **3.61e-19**), Residual SE = **4.880** on **853** df, AIC = **5209.0**, BIC = **5266.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.2083** | 1.5878 | ±3.1755 | **+7.059** | **1.67e-12** | *** |
| **Education: graduate level (vs college)** | **-1.4375** | 0.3509 | ±0.7018 | **-4.097** | **4.19e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1538** | 0.5736 | ±1.1471 | **+2.012** | **0.0443** | * |
| Site: UCSD (vs UAB) | +0.5187 | 0.4400 | ±0.8799 | +1.179 | 0.2384 |  |
| Site: UW (vs UAB) | +0.1142 | 0.4125 | ±0.8250 | +0.277 | 0.7819 |  |
| **Age (years)** | **-0.1076** | 0.0160 | ±0.0321 | **-6.708** | **1.98e-11** | *** |
| **BMI (kg/m2)** | **+0.0472** | 0.0235 | ±0.0470 | **+2.012** | **0.0442** | * |
| Hypertension | -0.0102 | 0.3740 | ±0.7481 | -0.027 | 0.9783 |  |
| High cholesterol | +0.6212 | 0.3528 | ±0.7057 | +1.761 | 0.0783 | . |
| **Kidney disease** | **+0.9879** | 0.5032 | ±1.0065 | **+1.963** | **0.0496** | * |
| **Circulatory disease** | **+1.3269** | 0.4658 | ±0.9316 | **+2.849** | **0.0044** | ** |
| Time in range 70-180, pooled (%) | -0.0084 | 0.0071 | ±0.0143 | -1.172 | 0.2411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **865**, R² = **0.1238**, Adj R² = **0.1125**, F-statistic = **10.96** (p = **3.90e-19**), Residual SE = **4.881** on **853** df, AIC = **5209.2**, BIC = **5266.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1724** | 1.5929 | ±3.1858 | **+7.014** | **2.32e-12** | *** |
| **Education: graduate level (vs college)** | **-1.4404** | 0.3508 | ±0.7016 | **-4.106** | **4.02e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1553** | 0.5740 | ±1.1480 | **+2.013** | **0.0441** | * |
| Site: UCSD (vs UAB) | +0.5176 | 0.4399 | ±0.8799 | +1.176 | 0.2394 |  |
| Site: UW (vs UAB) | +0.1130 | 0.4124 | ±0.8249 | +0.274 | 0.7841 |  |
| **Age (years)** | **-0.1075** | 0.0160 | ±0.0321 | **-6.701** | **2.07e-11** | *** |
| **BMI (kg/m2)** | **+0.0473** | 0.0235 | ±0.0470 | **+2.012** | **0.0442** | * |
| Hypertension | -0.0108 | 0.3740 | ±0.7480 | -0.029 | 0.9770 |  |
| High cholesterol | +0.6199 | 0.3529 | ±0.7058 | +1.757 | 0.0790 | . |
| **Kidney disease** | **+0.9890** | 0.5030 | ±1.0060 | **+1.966** | **0.0493** | * |
| **Circulatory disease** | **+1.3274** | 0.4659 | ±0.9319 | **+2.849** | **0.0044** | ** |
| Avg. daily time in range 70-180 (%) | -0.0079 | 0.0071 | ±0.0142 | -1.106 | 0.2685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **865**, R² = **0.1229**, Adj R² = **0.1116**, F-statistic = **10.87** (p = **5.93e-19**), Residual SE = **4.883** on **853** df, AIC = **5210.1**, BIC = **5267.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3522** | 1.4533 | ±2.9066 | **+7.123** | **1.05e-12** | *** |
| **Education: graduate level (vs college)** | **-1.4724** | 0.3496 | ±0.6992 | **-4.212** | **2.53e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2352** | 0.5733 | ±1.1467 | **+2.154** | **0.0312** | * |
| Site: UCSD (vs UAB) | +0.4954 | 0.4398 | ±0.8797 | +1.126 | 0.2601 |  |
| Site: UW (vs UAB) | +0.1207 | 0.4109 | ±0.8219 | +0.294 | 0.7690 |  |
| **Age (years)** | **-0.1050** | 0.0161 | ±0.0322 | **-6.516** | **7.22e-11** | *** |
| **BMI (kg/m2)** | **+0.0476** | 0.0234 | ±0.0468 | **+2.031** | **0.0422** | * |
| Hypertension | -0.0440 | 0.3742 | ±0.7483 | -0.118 | 0.9065 |  |
| High cholesterol | +0.6188 | 0.3535 | ±0.7070 | +1.751 | 0.0800 | . |
| **Kidney disease** | **+1.0478** | 0.4948 | ±0.9895 | **+2.118** | **0.0342** | * |
| **Circulatory disease** | **+1.3220** | 0.4712 | ±0.9425 | **+2.805** | **0.0050** | ** |
| Any reading < 54 during wear (0/1) | +0.2767 | 0.3737 | ±0.7475 | +0.740 | 0.4591 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **865**, R² = **0.1225**, Adj R² = **0.1111**, F-statistic = **10.82** (p = **7.25e-19**), Residual SE = **4.884** on **853** df, AIC = **5210.6**, BIC = **5267.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4869** | 1.4424 | ±2.8847 | **+7.271** | **3.58e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4760** | 0.3499 | ±0.6998 | **-4.218** | **2.46e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2101** | 0.5727 | ±1.1454 | **+2.113** | **0.0346** | * |
| Site: UCSD (vs UAB) | +0.4618 | 0.4419 | ±0.8838 | +1.045 | 0.2959 |  |
| Site: UW (vs UAB) | +0.0816 | 0.4135 | ±0.8271 | +0.197 | 0.8436 |  |
| **Age (years)** | **-0.1061** | 0.0159 | ±0.0319 | **-6.654** | **2.84e-11** | *** |
| **BMI (kg/m2)** | **+0.0488** | 0.0234 | ±0.0468 | **+2.082** | **0.0374** | * |
| Hypertension | -0.0266 | 0.3731 | ±0.7461 | -0.071 | 0.9431 |  |
| High cholesterol | +0.6022 | 0.3532 | ±0.7065 | +1.705 | 0.0882 | . |
| **Kidney disease** | **+1.0388** | 0.4950 | ±0.9899 | **+2.099** | **0.0358** | * |
| **Circulatory disease** | **+1.3464** | 0.4702 | ±0.9405 | **+2.863** | **0.0042** | ** |
| Time < 54 (%) | -0.1166 | 0.4534 | ±0.9068 | -0.257 | 0.7971 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **865**, R² = **0.1224**, Adj R² = **0.1111**, F-statistic = **10.81** (p = **7.53e-19**), Residual SE = **4.885** on **853** df, AIC = **5210.7**, BIC = **5267.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4720** | 1.4414 | ±2.8829 | **+7.265** | **3.73e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4735** | 0.3495 | ±0.6990 | **-4.216** | **2.49e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2166** | 0.5728 | ±1.1455 | **+2.124** | **0.0337** | * |
| Site: UCSD (vs UAB) | +0.4718 | 0.4405 | ±0.8810 | +1.071 | 0.2841 |  |
| Site: UW (vs UAB) | +0.0931 | 0.4128 | ±0.8257 | +0.226 | 0.8216 |  |
| **Age (years)** | **-0.1060** | 0.0159 | ±0.0319 | **-6.649** | **2.96e-11** | *** |
| **BMI (kg/m2)** | **+0.0485** | 0.0234 | ±0.0468 | **+2.075** | **0.0380** | * |
| Hypertension | -0.0292 | 0.3732 | ±0.7464 | -0.078 | 0.9375 |  |
| High cholesterol | +0.6036 | 0.3535 | ±0.7070 | +1.708 | 0.0877 | . |
| **Kidney disease** | **+1.0418** | 0.4951 | ±0.9903 | **+2.104** | **0.0354** | * |
| **Circulatory disease** | **+1.3392** | 0.4709 | ±0.9418 | **+2.844** | **0.0045** | ** |
| Avg. daily time < 54 (%) | -0.0190 | 0.5949 | ±1.1898 | -0.032 | 0.9745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **865**, R² = **0.1232**, Adj R² = **0.1118**, F-statistic = **10.89** (p = **5.31e-19**), Residual SE = **4.883** on **853** df, AIC = **5209.9**, BIC = **5267.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4482** | 1.4420 | ±2.8841 | **+7.246** | **4.31e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4584** | 0.3498 | ±0.6996 | **-4.169** | **3.06e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2186** | 0.5740 | ±1.1481 | **+2.123** | **0.0338** | * |
| Site: UCSD (vs UAB) | +0.4988 | 0.4394 | ±0.8787 | +1.135 | 0.2562 |  |
| Site: UW (vs UAB) | +0.1205 | 0.4113 | ±0.8226 | +0.293 | 0.7696 |  |
| **Age (years)** | **-0.1065** | 0.0159 | ±0.0318 | **-6.689** | **2.25e-11** | *** |
| **BMI (kg/m2)** | **+0.0481** | 0.0234 | ±0.0468 | **+2.055** | **0.0399** | * |
| Hypertension | -0.0330 | 0.3729 | ±0.7457 | -0.089 | 0.9295 |  |
| High cholesterol | +0.6070 | 0.3531 | ±0.7062 | +1.719 | 0.0856 | . |
| **Kidney disease** | **+1.0417** | 0.4948 | ±0.9896 | **+2.105** | **0.0353** | * |
| **Circulatory disease** | **+1.3261** | 0.4702 | ±0.9404 | **+2.820** | **0.0048** | ** |
| Time 54-69, pooled (%) | +0.0986 | 0.1103 | ±0.2205 | +0.894 | 0.3711 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **865**, R² = **0.1234**, Adj R² = **0.1121**, F-statistic = **10.91** (p = **4.81e-19**), Residual SE = **4.882** on **853** df, AIC = **5209.7**, BIC = **5266.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4654** | 1.4416 | ±2.8833 | **+7.259** | **3.89e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4552** | 0.3496 | ±0.6992 | **-4.163** | **3.14e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2160** | 0.5744 | ±1.1487 | **+2.117** | **0.0342** | * |
| Site: UCSD (vs UAB) | +0.4991 | 0.4391 | ±0.8783 | +1.137 | 0.2557 |  |
| Site: UW (vs UAB) | +0.1227 | 0.4112 | ±0.8224 | +0.298 | 0.7655 |  |
| **Age (years)** | **-0.1068** | 0.0159 | ±0.0319 | **-6.707** | **1.99e-11** | *** |
| **BMI (kg/m2)** | **+0.0480** | 0.0234 | ±0.0468 | **+2.053** | **0.0401** | * |
| Hypertension | -0.0333 | 0.3729 | ±0.7458 | -0.089 | 0.9288 |  |
| High cholesterol | +0.6083 | 0.3530 | ±0.7061 | +1.723 | 0.0849 | . |
| **Kidney disease** | **+1.0439** | 0.4945 | ±0.9890 | **+2.111** | **0.0348** | * |
| **Circulatory disease** | **+1.3272** | 0.4698 | ±0.9397 | **+2.825** | **0.0047** | ** |
| Avg. daily time 54-69 (%) | +0.1086 | 0.1067 | ±0.2134 | +1.018 | 0.3089 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **865**, R² = **0.1228**, Adj R² = **0.1115**, F-statistic = **10.86** (p = **6.19e-19**), Residual SE = **4.884** on **853** df, AIC = **5210.2**, BIC = **5267.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4484** | 1.4425 | ±2.8849 | **+7.243** | **4.37e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4622** | 0.3498 | ±0.6996 | **-4.180** | **2.91e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2222** | 0.5734 | ±1.1468 | **+2.131** | **0.0331** | * |
| Site: UCSD (vs UAB) | +0.4952 | 0.4398 | ±0.8796 | +1.126 | 0.2601 |  |
| Site: UW (vs UAB) | +0.1177 | 0.4115 | ±0.8230 | +0.286 | 0.7749 |  |
| **Age (years)** | **-0.1063** | 0.0159 | ±0.0318 | **-6.673** | **2.50e-11** | *** |
| **BMI (kg/m2)** | **+0.0481** | 0.0234 | ±0.0468 | **+2.054** | **0.0400** | * |
| Hypertension | -0.0333 | 0.3729 | ±0.7458 | -0.089 | 0.9289 |  |
| High cholesterol | +0.6070 | 0.3532 | ±0.7064 | +1.718 | 0.0857 | . |
| **Kidney disease** | **+1.0435** | 0.4950 | ±0.9901 | **+2.108** | **0.0350** | * |
| **Circulatory disease** | **+1.3261** | 0.4706 | ±0.9412 | **+2.818** | **0.0048** | ** |
| Time < 70 (%) | +0.0611 | 0.0991 | ±0.1983 | +0.617 | 0.5375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **865**, R² = **0.1230**, Adj R² = **0.1117**, F-statistic = **10.88** (p = **5.59e-19**), Residual SE = **4.883** on **853** df, AIC = **5210.0**, BIC = **5267.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4624** | 1.4419 | ±2.8838 | **+7.256** | **3.98e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4582** | 0.3496 | ±0.6991 | **-4.172** | **3.03e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2206** | 0.5737 | ±1.1475 | **+2.127** | **0.0334** | * |
| Site: UCSD (vs UAB) | +0.4967 | 0.4393 | ±0.8785 | +1.131 | 0.2582 |  |
| Site: UW (vs UAB) | +0.1204 | 0.4113 | ±0.8225 | +0.293 | 0.7697 |  |
| **Age (years)** | **-0.1066** | 0.0159 | ±0.0319 | **-6.692** | **2.20e-11** | *** |
| **BMI (kg/m2)** | **+0.0481** | 0.0234 | ±0.0468 | **+2.055** | **0.0399** | * |
| Hypertension | -0.0335 | 0.3729 | ±0.7459 | -0.090 | 0.9283 |  |
| High cholesterol | +0.6092 | 0.3531 | ±0.7063 | +1.725 | 0.0845 | . |
| **Kidney disease** | **+1.0444** | 0.4948 | ±0.9896 | **+2.111** | **0.0348** | * |
| **Circulatory disease** | **+1.3259** | 0.4702 | ±0.9404 | **+2.820** | **0.0048** | ** |
| Avg. daily time < 70 (%) | +0.0732 | 0.0978 | ±0.1957 | +0.748 | 0.4546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **865**, R² = **0.1256**, Adj R² = **0.1143**, F-statistic = **11.14** (p = **1.79e-19**), Residual SE = **4.876** on **853** df, AIC = **5207.5**, BIC = **5264.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.2211** | 1.8882 | ±3.7764 | **+6.472** | **9.65e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4175** | 0.3508 | ±0.7016 | **-4.041** | **5.33e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1417** | 0.5701 | ±1.1402 | **+2.002** | **0.0452** | * |
| Site: UCSD (vs UAB) | +0.5238 | 0.4385 | ±0.8769 | +1.195 | 0.2323 |  |
| Site: UW (vs UAB) | +0.1490 | 0.4146 | ±0.8292 | +0.359 | 0.7193 |  |
| **Age (years)** | **-0.1053** | 0.0159 | ±0.0319 | **-6.606** | **3.96e-11** | *** |
| **BMI (kg/m2)** | **+0.0473** | 0.0236 | ±0.0473 | **+2.003** | **0.0452** | * |
| Hypertension | -0.0335 | 0.3724 | ±0.7449 | -0.090 | 0.9283 |  |
| High cholesterol | +0.6182 | 0.3526 | ±0.7051 | +1.753 | 0.0796 | . |
| **Kidney disease** | **+0.9880** | 0.5004 | ±1.0008 | **+1.974** | **0.0483** | * |
| **Circulatory disease** | **+1.3254** | 0.4663 | ±0.9327 | **+2.842** | **0.0045** | ** |
| Time 54-250, pooled (%) | -0.0192 | 0.0134 | ±0.0269 | -1.430 | 0.1526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **865**, R² = **0.1250**, Adj R² = **0.1138**, F-statistic = **11.08** (p = **2.26e-19**), Residual SE = **4.877** on **853** df, AIC = **5208.0**, BIC = **5265.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.1079** | 1.9184 | ±3.8368 | **+6.311** | **2.77e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4226** | 0.3507 | ±0.7014 | **-4.056** | **4.99e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1483** | 0.5704 | ±1.1409 | **+2.013** | **0.0441** | * |
| Site: UCSD (vs UAB) | +0.5201 | 0.4388 | ±0.8776 | +1.185 | 0.2359 |  |
| Site: UW (vs UAB) | +0.1425 | 0.4145 | ±0.8289 | +0.344 | 0.7309 |  |
| **Age (years)** | **-0.1056** | 0.0159 | ±0.0319 | **-6.622** | **3.55e-11** | *** |
| **BMI (kg/m2)** | **+0.0474** | 0.0236 | ±0.0473 | **+2.006** | **0.0449** | * |
| Hypertension | -0.0319 | 0.3726 | ±0.7453 | -0.086 | 0.9318 |  |
| High cholesterol | +0.6170 | 0.3528 | ±0.7055 | +1.749 | 0.0803 | . |
| **Kidney disease** | **+0.9889** | 0.5003 | ±1.0006 | **+1.977** | **0.0481** | * |
| **Circulatory disease** | **+1.3245** | 0.4665 | ±0.9331 | **+2.839** | **0.0045** | ** |
| Avg. daily time 54-250 (%) | -0.0178 | 0.0137 | ±0.0274 | -1.297 | 0.1948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **865**, R² = **0.1224**, Adj R² = **0.1111**, F-statistic = **10.82** (p = **7.36e-19**), Residual SE = **4.885** on **853** df, AIC = **5210.6**, BIC = **5267.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4642** | 1.4423 | ±2.8846 | **+7.255** | **4.01e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4698** | 0.3500 | ±0.7000 | **-4.200** | **2.67e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2085** | 0.5764 | ±1.1529 | **+2.097** | **0.0360** | * |
| Site: UCSD (vs UAB) | +0.4797 | 0.4415 | ±0.8829 | +1.087 | 0.2772 |  |
| Site: UW (vs UAB) | +0.0930 | 0.4125 | ±0.8250 | +0.225 | 0.8217 |  |
| **Age (years)** | **-0.1065** | 0.0162 | ±0.0323 | **-6.593** | **4.30e-11** | *** |
| **BMI (kg/m2)** | **+0.0483** | 0.0234 | ±0.0468 | **+2.064** | **0.0390** | * |
| Hypertension | -0.0232 | 0.3751 | ±0.7503 | -0.062 | 0.9506 |  |
| High cholesterol | +0.6074 | 0.3529 | ±0.7058 | +1.721 | 0.0852 | . |
| **Kidney disease** | **+1.0330** | 0.5009 | ±1.0018 | **+2.062** | **0.0392** | * |
| **Circulatory disease** | **+1.3366** | 0.4667 | ±0.9334 | **+2.864** | **0.0042** | ** |
| Time 181-250, pooled (%) | +0.0025 | 0.0108 | ±0.0217 | +0.229 | 0.8187 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **865**, R² = **0.1225**, Adj R² = **0.1111**, F-statistic = **10.82** (p = **7.28e-19**), Residual SE = **4.885** on **853** df, AIC = **5210.6**, BIC = **5267.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4623** | 1.4425 | ±2.8850 | **+7.253** | **4.08e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4695** | 0.3500 | ±0.6999 | **-4.199** | **2.68e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2059** | 0.5769 | ±1.1538 | **+2.090** | **0.0366** | * |
| Site: UCSD (vs UAB) | +0.4815 | 0.4412 | ±0.8823 | +1.091 | 0.2751 |  |
| Site: UW (vs UAB) | +0.0930 | 0.4125 | ±0.8250 | +0.225 | 0.8216 |  |
| **Age (years)** | **-0.1066** | 0.0161 | ±0.0323 | **-6.605** | **3.97e-11** | *** |
| **BMI (kg/m2)** | **+0.0482** | 0.0234 | ±0.0468 | **+2.061** | **0.0393** | * |
| Hypertension | -0.0221 | 0.3748 | ±0.7496 | -0.059 | 0.9530 |  |
| High cholesterol | +0.6078 | 0.3529 | ±0.7059 | +1.722 | 0.0850 | . |
| **Kidney disease** | **+1.0310** | 0.5008 | ±1.0017 | **+2.058** | **0.0395** | * |
| **Circulatory disease** | **+1.3365** | 0.4668 | ±0.9335 | **+2.863** | **0.0042** | ** |
| Avg. daily time 181-250 (%) | +0.0029 | 0.0106 | ±0.0213 | +0.277 | 0.7820 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **865**, R² = **0.1239**, Adj R² = **0.1126**, F-statistic = **10.96** (p = **3.87e-19**), Residual SE = **4.881** on **853** df, AIC = **5209.2**, BIC = **5266.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3811** | 1.4448 | ±2.8895 | **+7.185** | **6.70e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4409** | 0.3508 | ±0.7015 | **-4.108** | **3.99e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1570** | 0.5733 | ±1.1465 | **+2.018** | **0.0436** | * |
| Site: UCSD (vs UAB) | +0.5132 | 0.4399 | ±0.8799 | +1.167 | 0.2434 |  |
| Site: UW (vs UAB) | +0.1101 | 0.4125 | ±0.8250 | +0.267 | 0.7895 |  |
| **Age (years)** | **-0.1074** | 0.0160 | ±0.0321 | **-6.701** | **2.07e-11** | *** |
| **BMI (kg/m2)** | **+0.0474** | 0.0235 | ±0.0469 | **+2.018** | **0.0436** | * |
| Hypertension | -0.0108 | 0.3741 | ±0.7481 | -0.029 | 0.9769 |  |
| High cholesterol | +0.6199 | 0.3529 | ±0.7057 | +1.757 | 0.0790 | . |
| **Kidney disease** | **+0.9909** | 0.5030 | ±1.0060 | **+1.970** | **0.0489** | * |
| **Circulatory disease** | **+1.3290** | 0.4657 | ±0.9314 | **+2.854** | **0.0043** | ** |
| Time > 180 (%) | +0.0079 | 0.0070 | ±0.0140 | +1.120 | 0.2625 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **865**, R² = **0.1237**, Adj R² = **0.1124**, F-statistic = **10.94** (p = **4.20e-19**), Residual SE = **4.881** on **853** df, AIC = **5209.4**, BIC = **5266.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3924** | 1.4448 | ±2.8896 | **+7.193** | **6.34e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4441** | 0.3507 | ±0.7014 | **-4.118** | **3.82e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1592** | 0.5736 | ±1.1473 | **+2.021** | **0.0433** | * |
| Site: UCSD (vs UAB) | +0.5122 | 0.4400 | ±0.8800 | +1.164 | 0.2443 |  |
| Site: UW (vs UAB) | +0.1092 | 0.4124 | ±0.8249 | +0.265 | 0.7911 |  |
| **Age (years)** | **-0.1074** | 0.0160 | ±0.0321 | **-6.693** | **2.18e-11** | *** |
| **BMI (kg/m2)** | **+0.0474** | 0.0235 | ±0.0470 | **+2.018** | **0.0436** | * |
| Hypertension | -0.0117 | 0.3740 | ±0.7481 | -0.031 | 0.9751 |  |
| High cholesterol | +0.6183 | 0.3529 | ±0.7059 | +1.752 | 0.0798 | . |
| **Kidney disease** | **+0.9923** | 0.5028 | ±1.0056 | **+1.974** | **0.0484** | * |
| **Circulatory disease** | **+1.3293** | 0.4659 | ±0.9317 | **+2.853** | **0.0043** | ** |
| Avg. daily time > 180 (%) | +0.0073 | 0.0070 | ±0.0140 | +1.046 | 0.2955 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **865**, R² = **0.1255**, Adj R² = **0.1142**, F-statistic = **11.13** (p = **1.83e-19**), Residual SE = **4.876** on **853** df, AIC = **5207.6**, BIC = **5264.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3622** | 1.4460 | ±2.8919 | **+7.166** | **7.71e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4156** | 0.3520 | ±0.7040 | **-4.022** | **5.78e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1369** | 0.5715 | ±1.1431 | **+1.989** | **0.0467** | * |
| Site: UCSD (vs UAB) | +0.5388 | 0.4385 | ±0.8769 | +1.229 | 0.2192 |  |
| Site: UW (vs UAB) | +0.1124 | 0.4126 | ±0.8251 | +0.272 | 0.7853 |  |
| **Age (years)** | **-0.1066** | 0.0160 | ±0.0320 | **-6.667** | **2.61e-11** | *** |
| BMI (kg/m2) | +0.0449 | 0.0236 | ±0.0472 | +1.902 | 0.0572 | . |
| Hypertension | +0.0005 | 0.3737 | ±0.7473 | +0.001 | 0.9989 |  |
| High cholesterol | +0.6303 | 0.3522 | ±0.7044 | +1.789 | 0.0735 | . |
| Kidney disease | +0.9784 | 0.5024 | ±1.0049 | +1.947 | 0.0515 | . |
| **Circulatory disease** | **+1.3208** | 0.4654 | ±0.9308 | **+2.838** | **0.0045** | ** |
| Nocturnal time > 180 (%) | +0.0109 | 0.0067 | ±0.0134 | +1.637 | 0.1016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **865**, R² = **0.1224**, Adj R² = **0.1111**, F-statistic = **10.81** (p = **7.50e-19**), Residual SE = **4.885** on **853** df, AIC = **5210.6**, BIC = **5267.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4817** | 1.4433 | ±2.8867 | **+7.262** | **3.81e-13** | *** |
| **Education: graduate level (vs college)** | **-1.4763** | 0.3507 | ±0.7014 | **-4.209** | **2.56e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2200** | 0.5744 | ±1.1487 | **+2.124** | **0.0337** | * |
| Site: UCSD (vs UAB) | +0.4718 | 0.4407 | ±0.8813 | +1.071 | 0.2843 |  |
| Site: UW (vs UAB) | +0.0963 | 0.4131 | ±0.8262 | +0.233 | 0.8156 |  |
| **Age (years)** | **-0.1057** | 0.0163 | ±0.0326 | **-6.493** | **8.41e-11** | *** |
| **BMI (kg/m2)** | **+0.0484** | 0.0234 | ±0.0468 | **+2.067** | **0.0387** | * |
| Hypertension | -0.0313 | 0.3747 | ±0.7493 | -0.084 | 0.9334 |  |
| High cholesterol | +0.6037 | 0.3530 | ±0.7061 | +1.710 | 0.0873 | . |
| **Kidney disease** | **+1.0467** | 0.4976 | ±0.9951 | **+2.104** | **0.0354** | * |
| **Circulatory disease** | **+1.3371** | 0.4678 | ±0.9355 | **+2.858** | **0.0043** | ** |
| Any reading > 250 during wear (0/1) | -0.0367 | 0.3628 | ±0.7256 | -0.101 | 0.9193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **865**, R² = **0.1256**, Adj R² = **0.1143**, F-statistic = **11.14** (p = **1.77e-19**), Residual SE = **4.876** on **853** df, AIC = **5207.5**, BIC = **5264.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3024** | 1.4515 | ±2.9030 | **+7.098** | **1.27e-12** | *** |
| **Education: graduate level (vs college)** | **-1.4179** | 0.3507 | ±0.7015 | **-4.042** | **5.29e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1403** | 0.5701 | ±1.1401 | **+2.000** | **0.0455** | * |
| Site: UCSD (vs UAB) | +0.5219 | 0.4384 | ±0.8768 | +1.191 | 0.2338 |  |
| Site: UW (vs UAB) | +0.1469 | 0.4145 | ±0.8290 | +0.355 | 0.7230 |  |
| **Age (years)** | **-0.1053** | 0.0159 | ±0.0319 | **-6.607** | **3.93e-11** | *** |
| **BMI (kg/m2)** | **+0.0474** | 0.0236 | ±0.0473 | **+2.005** | **0.0450** | * |
| Hypertension | -0.0330 | 0.3725 | ±0.7449 | -0.089 | 0.9293 |  |
| High cholesterol | +0.6178 | 0.3525 | ±0.7051 | +1.753 | 0.0797 | . |
| **Kidney disease** | **+0.9873** | 0.5004 | ±1.0008 | **+1.973** | **0.0485** | * |
| **Circulatory disease** | **+1.3268** | 0.4662 | ±0.9324 | **+2.846** | **0.0044** | ** |
| Time > 250 (%) | +0.0192 | 0.0134 | ±0.0268 | +1.436 | 0.1510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **865**, R² = **0.1250**, Adj R² = **0.1138**, F-statistic = **11.08** (p = **2.26e-19**), Residual SE = **4.877** on **853** df, AIC = **5208.0**, BIC = **5265.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3322** | 1.4506 | ±2.9013 | **+7.123** | **1.06e-12** | *** |
| **Education: graduate level (vs college)** | **-1.4232** | 0.3507 | ±0.7014 | **-4.058** | **4.94e-05** | *** |
| **Education: high school or below (vs college)** | **+1.1474** | 0.5704 | ±1.1408 | **+2.012** | **0.0443** | * |
| Site: UCSD (vs UAB) | +0.5186 | 0.4388 | ±0.8775 | +1.182 | 0.2372 |  |
| Site: UW (vs UAB) | +0.1409 | 0.4144 | ±0.8287 | +0.340 | 0.7339 |  |
| **Age (years)** | **-0.1055** | 0.0159 | ±0.0319 | **-6.621** | **3.56e-11** | *** |
| **BMI (kg/m2)** | **+0.0474** | 0.0236 | ±0.0473 | **+2.007** | **0.0448** | * |
| Hypertension | -0.0315 | 0.3727 | ±0.7453 | -0.085 | 0.9326 |  |
| High cholesterol | +0.6165 | 0.3528 | ±0.7055 | +1.748 | 0.0805 | . |
| **Kidney disease** | **+0.9887** | 0.5003 | ±1.0006 | **+1.976** | **0.0481** | * |
| **Circulatory disease** | **+1.3257** | 0.4664 | ±0.9329 | **+2.842** | **0.0045** | ** |
| Avg. daily time > 250 (%) | +0.0178 | 0.0137 | ±0.0274 | +1.298 | 0.1942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 865; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0549**, LLR χ² = **49.55** (p = **3.23e-07**), AUC = **0.6606**, AIC = **875.6**, BIC = **928.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0885 | 0.7320 | ±1.4640 | -0.121 | 0.9038 | 0.9153 |  |
| **Education: graduate level (vs college)** | **-0.4207** | 0.2056 | ±0.4111 | **-2.046** | **0.0407** | 0.6566 | * |
| Education: high school or below (vs college) | +0.2391 | 0.2274 | ±0.4549 | +1.051 | 0.2932 | 1.2701 |  |
| Site: UCSD (vs UAB) | +0.0581 | 0.2148 | ±0.4295 | +0.270 | 0.7869 | 1.0598 |  |
| Site: UW (vs UAB) | +0.0684 | 0.2097 | ±0.4195 | +0.326 | 0.7443 | 1.0708 |  |
| **Age (years)** | **-0.0354** | 0.0089 | ±0.0178 | **-3.979** | **6.93e-05** | 0.9652 | *** |
| BMI (kg/m2) | +0.0178 | 0.0115 | ±0.0230 | +1.546 | 0.1222 | 1.0179 |  |
| Hypertension | +0.0579 | 0.1981 | ±0.3961 | +0.293 | 0.7699 | 1.0596 |  |
| High cholesterol | +0.2897 | 0.1864 | ±0.3728 | +1.554 | 0.1202 | 1.3360 |  |
| **Kidney disease** | **+0.4993** | 0.2204 | ±0.4408 | **+2.266** | **0.0235** | 1.6476 | * |
| **Circulatory disease** | **+0.4745** | 0.2015 | ±0.4031 | **+2.354** | **0.0186** | 1.6072 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0604**, LLR χ² = **54.55** (p = **9.38e-08**), AUC = **0.6672**, AIC = **872.6**, BIC = **929.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9432 | 0.8271 | ±1.6541 | -1.140 | 0.2541 | 0.3894 |  |
| Education: graduate level (vs college) | -0.3814 | 0.2069 | ±0.4137 | -1.844 | 0.0653 | 0.6829 | . |
| Education: high school or below (vs college) | +0.1796 | 0.2304 | ±0.4608 | +0.780 | 0.4357 | 1.1968 |  |
| Site: UCSD (vs UAB) | +0.0861 | 0.2162 | ±0.4324 | +0.398 | 0.6905 | 1.0899 |  |
| Site: UW (vs UAB) | +0.1014 | 0.2111 | ±0.4223 | +0.480 | 0.6312 | 1.1067 |  |
| **Age (years)** | **-0.0358** | 0.0089 | ±0.0178 | **-4.018** | **5.86e-05** | 0.9648 | *** |
| BMI (kg/m2) | +0.0157 | 0.0116 | ±0.0231 | +1.362 | 0.1733 | 1.0159 |  |
| Hypertension | +0.0526 | 0.1991 | ±0.3982 | +0.264 | 0.7916 | 1.0540 |  |
| High cholesterol | +0.2884 | 0.1871 | ±0.3742 | +1.541 | 0.1233 | 1.3342 |  |
| **Kidney disease** | **+0.4975** | 0.2212 | ±0.4423 | **+2.250** | **0.0245** | 1.6446 | * |
| **Circulatory disease** | **+0.4774** | 0.2021 | ±0.4042 | **+2.362** | **0.0182** | 1.6118 | * |
| **HbA1c (%)** | **+0.1371** | 0.0605 | ±0.1211 | **+2.264** | **0.0236** | 1.1469 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0577**, LLR χ² = **52.07** (p = **2.64e-07**), AUC = **0.6651**, AIC = **875.0**, BIC = **932.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5416 | 0.7856 | ±1.5712 | -0.689 | 0.4906 | 0.5818 |  |
| Education: graduate level (vs college) | -0.3935 | 0.2066 | ±0.4132 | -1.905 | 0.0568 | 0.6747 | . |
| Education: high school or below (vs college) | +0.2050 | 0.2290 | ±0.4580 | +0.895 | 0.3708 | 1.2275 |  |
| Site: UCSD (vs UAB) | +0.0805 | 0.2157 | ±0.4314 | +0.373 | 0.7092 | 1.0838 |  |
| Site: UW (vs UAB) | +0.0844 | 0.2103 | ±0.4206 | +0.401 | 0.6881 | 1.0881 |  |
| **Age (years)** | **-0.0359** | 0.0089 | ±0.0178 | **-4.032** | **5.53e-05** | 0.9648 | *** |
| BMI (kg/m2) | +0.0172 | 0.0115 | ±0.0230 | +1.495 | 0.1349 | 1.0174 |  |
| Hypertension | +0.0619 | 0.1985 | ±0.3970 | +0.312 | 0.7552 | 1.0639 |  |
| High cholesterol | +0.2958 | 0.1869 | ±0.3737 | +1.583 | 0.1134 | 1.3442 |  |
| **Kidney disease** | **+0.4755** | 0.2212 | ±0.4425 | **+2.149** | **0.0316** | 1.6088 | * |
| **Circulatory disease** | **+0.4763** | 0.2017 | ±0.4034 | **+2.361** | **0.0182** | 1.6101 | * |
| Mean glucose (mg/dL) | +0.0031 | 0.0019 | ±0.0039 | +1.603 | 0.1089 | 1.0031 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0577**, LLR χ² = **52.07** (p = **2.64e-07**), AUC = **0.6651**, AIC = **875.0**, BIC = **932.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9730 | 0.9180 | ±1.8361 | -1.060 | 0.2892 | 0.3779 |  |
| Education: graduate level (vs college) | -0.3935 | 0.2066 | ±0.4132 | -1.905 | 0.0568 | 0.6747 | . |
| Education: high school or below (vs college) | +0.2050 | 0.2290 | ±0.4580 | +0.895 | 0.3708 | 1.2275 |  |
| Site: UCSD (vs UAB) | +0.0805 | 0.2157 | ±0.4314 | +0.373 | 0.7092 | 1.0838 |  |
| Site: UW (vs UAB) | +0.0844 | 0.2103 | ±0.4206 | +0.401 | 0.6881 | 1.0881 |  |
| **Age (years)** | **-0.0359** | 0.0089 | ±0.0178 | **-4.032** | **5.53e-05** | 0.9648 | *** |
| BMI (kg/m2) | +0.0172 | 0.0115 | ±0.0230 | +1.495 | 0.1349 | 1.0174 |  |
| Hypertension | +0.0619 | 0.1985 | ±0.3970 | +0.312 | 0.7552 | 1.0639 |  |
| High cholesterol | +0.2958 | 0.1869 | ±0.3737 | +1.583 | 0.1134 | 1.3442 |  |
| **Kidney disease** | **+0.4755** | 0.2212 | ±0.4425 | **+2.149** | **0.0316** | 1.6088 | * |
| **Circulatory disease** | **+0.4763** | 0.2017 | ±0.4034 | **+2.361** | **0.0182** | 1.6101 | * |
| GMI (%) | +0.1304 | 0.0813 | ±0.1626 | +1.603 | 0.1089 | 1.1392 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0611**, LLR χ² = **55.19** (p = **7.15e-08**), AUC = **0.6709**, AIC = **871.9**, BIC = **929.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7492 | 0.7838 | ±1.5676 | -0.956 | 0.3392 | 0.4728 |  |
| Education: graduate level (vs college) | -0.3783 | 0.2070 | ±0.4139 | -1.828 | 0.0676 | 0.6850 | . |
| Education: high school or below (vs college) | +0.1933 | 0.2295 | ±0.4589 | +0.842 | 0.3996 | 1.2132 |  |
| Site: UCSD (vs UAB) | +0.0929 | 0.2162 | ±0.4324 | +0.430 | 0.6673 | 1.0974 |  |
| Site: UW (vs UAB) | +0.0802 | 0.2106 | ±0.4212 | +0.381 | 0.7035 | 1.0835 |  |
| **Age (years)** | **-0.0354** | 0.0089 | ±0.0178 | **-3.971** | **7.15e-05** | 0.9653 | *** |
| BMI (kg/m2) | +0.0161 | 0.0116 | ±0.0231 | +1.389 | 0.1649 | 1.0162 |  |
| Hypertension | +0.0689 | 0.1990 | ±0.3980 | +0.346 | 0.7290 | 1.0714 |  |
| High cholesterol | +0.2999 | 0.1874 | ±0.3748 | +1.600 | 0.1095 | 1.3497 |  |
| **Kidney disease** | **+0.4792** | 0.2213 | ±0.4427 | **+2.165** | **0.0304** | 1.6147 | * |
| **Circulatory disease** | **+0.4788** | 0.2020 | ±0.4040 | **+2.371** | **0.0178** | 1.6142 | * |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0045** | 0.0019 | ±0.0038 | **+2.401** | **0.0164** | 1.0045 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0608**, LLR χ² = **54.88** (p = **8.16e-08**), AUC = **0.6678**, AIC = **872.2**, BIC = **929.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5005 | 0.7540 | ±1.5079 | -0.664 | 0.5068 | 0.6062 |  |
| Education: graduate level (vs college) | -0.3766 | 0.2072 | ±0.4144 | -1.818 | 0.0691 | 0.6862 | . |
| Education: high school or below (vs college) | +0.1816 | 0.2297 | ±0.4594 | +0.791 | 0.4292 | 1.1992 |  |
| Site: UCSD (vs UAB) | +0.0808 | 0.2156 | ±0.4313 | +0.375 | 0.7080 | 1.0841 |  |
| Site: UW (vs UAB) | +0.1057 | 0.2110 | ±0.4220 | +0.501 | 0.6165 | 1.1115 |  |
| **Age (years)** | **-0.0370** | 0.0089 | ±0.0178 | **-4.143** | **3.43e-05** | 0.9637 | *** |
| BMI (kg/m2) | +0.0177 | 0.0115 | ±0.0230 | +1.538 | 0.1241 | 1.0179 |  |
| Hypertension | +0.0631 | 0.1990 | ±0.3980 | +0.317 | 0.7513 | 1.0651 |  |
| High cholesterol | +0.3056 | 0.1874 | ±0.3749 | +1.631 | 0.1030 | 1.3575 |  |
| Kidney disease | +0.4070 | 0.2249 | ±0.4498 | +1.810 | 0.0704 | 1.5022 | . |
| **Circulatory disease** | **+0.4748** | 0.2021 | ±0.4042 | **+2.349** | **0.0188** | 1.6077 | * |
| **Glucose SD, pooled (mg/dL)** | **+0.0140** | 0.0060 | ±0.0120 | **+2.322** | **0.0202** | 1.0141 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0581**, LLR χ² = **52.43** (p = **2.28e-07**), AUC = **0.6648**, AIC = **874.7**, BIC = **931.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4104 | 0.7565 | ±1.5129 | -0.543 | 0.5875 | 0.6634 |  |
| Education: graduate level (vs college) | -0.3896 | 0.2068 | ±0.4135 | -1.885 | 0.0595 | 0.6773 | . |
| Education: high school or below (vs college) | +0.1924 | 0.2296 | ±0.4592 | +0.838 | 0.4020 | 1.2122 |  |
| Site: UCSD (vs UAB) | +0.0728 | 0.2152 | ±0.4304 | +0.338 | 0.7351 | 1.0755 |  |
| Site: UW (vs UAB) | +0.0918 | 0.2105 | ±0.4210 | +0.436 | 0.6627 | 1.0962 |  |
| **Age (years)** | **-0.0367** | 0.0089 | ±0.0179 | **-4.111** | **3.93e-05** | 0.9639 | *** |
| BMI (kg/m2) | +0.0183 | 0.0115 | ±0.0230 | +1.594 | 0.1109 | 1.0185 |  |
| Hypertension | +0.0640 | 0.1986 | ±0.3972 | +0.322 | 0.7472 | 1.0661 |  |
| High cholesterol | +0.3017 | 0.1871 | ±0.3742 | +1.613 | 0.1069 | 1.3521 |  |
| Kidney disease | +0.4280 | 0.2249 | ±0.4498 | +1.903 | 0.0570 | 1.5342 | . |
| **Circulatory disease** | **+0.4777** | 0.2018 | ±0.4036 | **+2.367** | **0.0179** | 1.6124 | * |
| Avg. daily SD (mg/dL) | +0.0118 | 0.0069 | ±0.0139 | +1.707 | 0.0877 | 1.0119 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0564**, LLR χ² = **50.97** (p = **4.19e-07**), AUC = **0.6628**, AIC = **876.2**, BIC = **933.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4281 | 0.7847 | ±1.5693 | -0.546 | 0.5854 | 0.6518 |  |
| **Education: graduate level (vs college)** | **-0.4056** | 0.2062 | ±0.4124 | **-1.967** | **0.0492** | 0.6666 | * |
| Education: high school or below (vs college) | +0.2148 | 0.2285 | ±0.4570 | +0.940 | 0.3473 | 1.2396 |  |
| Site: UCSD (vs UAB) | +0.0639 | 0.2148 | ±0.4296 | +0.298 | 0.7660 | 1.0660 |  |
| Site: UW (vs UAB) | +0.0864 | 0.2105 | ±0.4209 | +0.411 | 0.6813 | 1.0903 |  |
| **Age (years)** | **-0.0365** | 0.0089 | ±0.0179 | **-4.079** | **4.53e-05** | 0.9642 | *** |
| BMI (kg/m2) | +0.0181 | 0.0115 | ±0.0230 | +1.576 | 0.1150 | 1.0183 |  |
| Hypertension | +0.0563 | 0.1983 | ±0.3966 | +0.284 | 0.7765 | 1.0579 |  |
| High cholesterol | +0.2971 | 0.1868 | ±0.3736 | +1.591 | 0.1117 | 1.3460 |  |
| **Kidney disease** | **+0.4447** | 0.2254 | ±0.4507 | **+1.973** | **0.0485** | 1.5600 | * |
| **Circulatory disease** | **+0.4715** | 0.2017 | ±0.4035 | **+2.337** | **0.0194** | 1.6024 | * |
| CV (%) | +0.0177 | 0.0148 | ±0.0295 | +1.196 | 0.2317 | 1.0178 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0556**, LLR χ² = **50.22** (p = **5.71e-07**), AUC = **0.6617**, AIC = **876.9**, BIC = **934.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2246 | 0.8259 | ±1.6517 | +0.272 | 0.7856 | 1.2518 |  |
| **Education: graduate level (vs college)** | **-0.4099** | 0.2061 | ±0.4122 | **-1.989** | **0.0467** | 0.6637 | * |
| Education: high school or below (vs college) | +0.2208 | 0.2286 | ±0.4571 | +0.966 | 0.3339 | 1.2471 |  |
| Site: UCSD (vs UAB) | +0.0599 | 0.2147 | ±0.4295 | +0.279 | 0.7805 | 1.0617 |  |
| Site: UW (vs UAB) | +0.0794 | 0.2102 | ±0.4204 | +0.378 | 0.7057 | 1.0826 |  |
| **Age (years)** | **-0.0362** | 0.0090 | ±0.0179 | **-4.047** | **5.20e-05** | 0.9644 | *** |
| BMI (kg/m2) | +0.0180 | 0.0115 | ±0.0230 | +1.563 | 0.1179 | 1.0181 |  |
| Hypertension | +0.0587 | 0.1982 | ±0.3964 | +0.296 | 0.7673 | 1.0604 |  |
| High cholesterol | +0.2920 | 0.1866 | ±0.3732 | +1.565 | 0.1176 | 1.3390 |  |
| **Kidney disease** | **+0.4697** | 0.2234 | ±0.4468 | **+2.102** | **0.0355** | 1.5994 | * |
| **Circulatory disease** | **+0.4699** | 0.2017 | ±0.4034 | **+2.329** | **0.0198** | 1.5998 | * |
| Mean / SD ratio | -0.0555 | 0.0681 | ±0.1363 | -0.814 | 0.4155 | 0.9460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0549**, LLR χ² = **49.58** (p = **7.46e-07**), AUC = **0.6600**, AIC = **877.5**, BIC = **934.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0305 | 0.8148 | ±1.6296 | -0.037 | 0.9701 | 0.9699 |  |
| **Education: graduate level (vs college)** | **-0.4184** | 0.2061 | ±0.4121 | **-2.030** | **0.0423** | 0.6581 | * |
| Education: high school or below (vs college) | +0.2356 | 0.2284 | ±0.4569 | +1.031 | 0.3023 | 1.2657 |  |
| Site: UCSD (vs UAB) | +0.0574 | 0.2148 | ±0.4296 | +0.267 | 0.7891 | 1.0591 |  |
| Site: UW (vs UAB) | +0.0700 | 0.2099 | ±0.4199 | +0.333 | 0.7389 | 1.0725 |  |
| **Age (years)** | **-0.0356** | 0.0090 | ±0.0179 | **-3.969** | **7.23e-05** | 0.9651 | *** |
| BMI (kg/m2) | +0.0179 | 0.0115 | ±0.0230 | +1.553 | 0.1205 | 1.0180 |  |
| Hypertension | +0.0581 | 0.1981 | ±0.3962 | +0.293 | 0.7694 | 1.0598 |  |
| High cholesterol | +0.2903 | 0.1865 | ±0.3729 | +1.557 | 0.1196 | 1.3368 |  |
| **Kidney disease** | **+0.4942** | 0.2226 | ±0.4452 | **+2.220** | **0.0264** | 1.6393 | * |
| **Circulatory disease** | **+0.4744** | 0.2015 | ±0.4031 | **+2.354** | **0.0186** | 1.6071 | * |
| Avg. daily mean/SD | -0.0090 | 0.0557 | ±0.1113 | -0.162 | 0.8715 | 0.9910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0636**, LLR χ² = **57.48** (p = **2.72e-08**), AUC = **0.6702**, AIC = **869.6**, BIC = **926.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2078 | 0.8374 | ±1.6748 | -1.442 | 0.1492 | 0.2988 |  |
| Education: graduate level (vs college) | -0.3707 | 0.2074 | ±0.4148 | -1.787 | 0.0739 | 0.6903 | . |
| Education: high school or below (vs college) | +0.1833 | 0.2304 | ±0.4609 | +0.795 | 0.4263 | 1.2012 |  |
| Site: UCSD (vs UAB) | +0.0823 | 0.2163 | ±0.4325 | +0.381 | 0.7036 | 1.0858 |  |
| Site: UW (vs UAB) | +0.1446 | 0.2124 | ±0.4248 | +0.681 | 0.4959 | 1.1556 |  |
| **Age (years)** | **-0.0348** | 0.0089 | ±0.0179 | **-3.890** | **1.00e-04** | 0.9658 | *** |
| BMI (kg/m2) | +0.0174 | 0.0116 | ±0.0231 | +1.509 | 0.1314 | 1.0176 |  |
| Hypertension | +0.0756 | 0.1997 | ±0.3993 | +0.379 | 0.7050 | 1.0785 |  |
| High cholesterol | +0.3031 | 0.1879 | ±0.3758 | +1.613 | 0.1067 | 1.3541 |  |
| **Kidney disease** | **+0.4413** | 0.2227 | ±0.4454 | **+1.982** | **0.0475** | 1.5547 | * |
| **Circulatory disease** | **+0.4777** | 0.2027 | ±0.4055 | **+2.356** | **0.0185** | 1.6124 | * |
| **MAG (mg/dL/h)** | **+0.0240** | 0.0085 | ±0.0170 | **+2.827** | **0.0047** | 1.0243 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0578**, LLR χ² = **52.21** (p = **2.50e-07**), AUC = **0.6649**, AIC = **874.9**, BIC = **932.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5151 | 0.7780 | ±1.5559 | -0.662 | 0.5079 | 0.5974 |  |
| Education: graduate level (vs college) | -0.3874 | 0.2069 | ±0.4138 | -1.873 | 0.0611 | 0.6788 | . |
| Education: high school or below (vs college) | +0.1955 | 0.2295 | ±0.4590 | +0.852 | 0.3944 | 1.2159 |  |
| Site: UCSD (vs UAB) | +0.0753 | 0.2153 | ±0.4305 | +0.350 | 0.7267 | 1.0782 |  |
| Site: UW (vs UAB) | +0.0886 | 0.2104 | ±0.4208 | +0.421 | 0.6736 | 1.0927 |  |
| **Age (years)** | **-0.0365** | 0.0089 | ±0.0179 | **-4.085** | **4.40e-05** | 0.9642 | *** |
| BMI (kg/m2) | +0.0187 | 0.0115 | ±0.0230 | +1.621 | 0.1051 | 1.0188 |  |
| Hypertension | +0.0711 | 0.1988 | ±0.3976 | +0.358 | 0.7207 | 1.0737 |  |
| High cholesterol | +0.2976 | 0.1870 | ±0.3741 | +1.591 | 0.1116 | 1.3466 |  |
| Kidney disease | +0.4312 | 0.2249 | ±0.4498 | +1.917 | 0.0552 | 1.5390 | . |
| **Circulatory disease** | **+0.4744** | 0.2019 | ±0.4037 | **+2.350** | **0.0188** | 1.6070 | * |
| Avg. daily range (mg/dL) | +0.0032 | 0.0020 | ±0.0039 | +1.637 | 0.1016 | 1.0032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0730**, LLR χ² = **65.89** (p = **7.32e-10**), AUC = **0.6860**, AIC = **861.2**, BIC = **918.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5503 | 0.7415 | ±1.4831 | -0.742 | 0.4581 | 0.5768 |  |
| Education: graduate level (vs college) | -0.3379 | 0.2089 | ±0.4178 | -1.618 | 0.1057 | 0.7132 |  |
| Education: high school or below (vs college) | +0.1912 | 0.2306 | ±0.4611 | +0.829 | 0.4070 | 1.2107 |  |
| Site: UCSD (vs UAB) | +0.0909 | 0.2177 | ±0.4355 | +0.418 | 0.6762 | 1.0952 |  |
| Site: UW (vs UAB) | +0.1363 | 0.2126 | ±0.4252 | +0.641 | 0.5214 | 1.1461 |  |
| **Age (years)** | **-0.0353** | 0.0089 | ±0.0178 | **-3.975** | **7.05e-05** | 0.9653 | *** |
| BMI (kg/m2) | +0.0157 | 0.0117 | ±0.0233 | +1.349 | 0.1772 | 1.0158 |  |
| Hypertension | +0.0421 | 0.2009 | ±0.4017 | +0.209 | 0.8341 | 1.0430 |  |
| High cholesterol | +0.3092 | 0.1892 | ±0.3783 | +1.635 | 0.1021 | 1.3624 |  |
| Kidney disease | +0.4092 | 0.2245 | ±0.4490 | +1.823 | 0.0683 | 1.5056 | . |
| **Circulatory disease** | **+0.4297** | 0.2044 | ±0.4088 | **+2.102** | **0.0355** | 1.5368 | * |
| **SD of daily means (mg/dL)** | **+0.0396** | 0.0098 | ±0.0195 | **+4.059** | **4.92e-05** | 1.0404 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0581**, LLR χ² = **52.51** (p = **2.20e-07**), AUC = **0.6654**, AIC = **874.6**, BIC = **931.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3752 | 0.7789 | ±1.5577 | +0.482 | 0.6300 | 1.4552 |  |
| Education: graduate level (vs college) | -0.3891 | 0.2068 | ±0.4136 | -1.882 | 0.0599 | 0.6777 | . |
| Education: high school or below (vs college) | +0.1997 | 0.2291 | ±0.4583 | +0.871 | 0.3836 | 1.2210 |  |
| Site: UCSD (vs UAB) | +0.0917 | 0.2161 | ±0.4323 | +0.424 | 0.6713 | 1.0961 |  |
| Site: UW (vs UAB) | +0.0900 | 0.2105 | ±0.4210 | +0.428 | 0.6690 | 1.0942 |  |
| **Age (years)** | **-0.0362** | 0.0089 | ±0.0178 | **-4.070** | **4.70e-05** | 0.9644 | *** |
| BMI (kg/m2) | +0.0170 | 0.0115 | ±0.0231 | +1.473 | 0.1406 | 1.0171 |  |
| Hypertension | +0.0691 | 0.1987 | ±0.3974 | +0.348 | 0.7281 | 1.0715 |  |
| High cholesterol | +0.3003 | 0.1870 | ±0.3741 | +1.606 | 0.1084 | 1.3503 |  |
| **Kidney disease** | **+0.4667** | 0.2216 | ±0.4432 | **+2.106** | **0.0352** | 1.5948 | * |
| **Circulatory disease** | **+0.4735** | 0.2018 | ±0.4035 | **+2.347** | **0.0189** | 1.6056 | * |
| Time in range 70-180, pooled (%) | -0.0055 | 0.0032 | ±0.0064 | -1.738 | 0.0823 | 0.9945 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0578**, LLR χ² = **52.23** (p = **2.48e-07**), AUC = **0.6651**, AIC = **874.9**, BIC = **932.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3577 | 0.7800 | ±1.5601 | +0.459 | 0.6466 | 1.4300 |  |
| Education: graduate level (vs college) | -0.3914 | 0.2067 | ±0.4134 | -1.893 | 0.0583 | 0.6761 | . |
| Education: high school or below (vs college) | +0.2000 | 0.2292 | ±0.4584 | +0.873 | 0.3829 | 1.2214 |  |
| Site: UCSD (vs UAB) | +0.0911 | 0.2161 | ±0.4323 | +0.421 | 0.6735 | 1.0953 |  |
| Site: UW (vs UAB) | +0.0886 | 0.2104 | ±0.4209 | +0.421 | 0.6738 | 1.0926 |  |
| **Age (years)** | **-0.0363** | 0.0089 | ±0.0178 | **-4.071** | **4.69e-05** | 0.9644 | *** |
| BMI (kg/m2) | +0.0170 | 0.0115 | ±0.0231 | +1.473 | 0.1408 | 1.0171 |  |
| Hypertension | +0.0691 | 0.1987 | ±0.3974 | +0.348 | 0.7280 | 1.0715 |  |
| High cholesterol | +0.2996 | 0.1870 | ±0.3740 | +1.602 | 0.1091 | 1.3493 |  |
| **Kidney disease** | **+0.4670** | 0.2216 | ±0.4432 | **+2.107** | **0.0351** | 1.5952 | * |
| **Circulatory disease** | **+0.4736** | 0.2017 | ±0.4034 | **+2.348** | **0.0189** | 1.6058 | * |
| Avg. daily time in range 70-180 (%) | -0.0052 | 0.0032 | ±0.0063 | -1.651 | 0.0987 | 0.9948 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0552**, LLR χ² = **49.83** (p = **6.71e-07**), AUC = **0.6612**, AIC = **877.3**, BIC = **934.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1372 | 0.7375 | ±1.4751 | -0.186 | 0.8524 | 0.8718 |  |
| **Education: graduate level (vs college)** | **-0.4221** | 0.2057 | ±0.4114 | **-2.052** | **0.0402** | 0.6557 | * |
| Education: high school or below (vs college) | +0.2461 | 0.2278 | ±0.4557 | +1.080 | 0.2801 | 1.2790 |  |
| Site: UCSD (vs UAB) | +0.0662 | 0.2153 | ±0.4307 | +0.307 | 0.7586 | 1.0684 |  |
| Site: UW (vs UAB) | +0.0778 | 0.2106 | ±0.4211 | +0.369 | 0.7118 | 1.0809 |  |
| **Age (years)** | **-0.0349** | 0.0089 | ±0.0179 | **-3.912** | **9.17e-05** | 0.9657 | *** |
| BMI (kg/m2) | +0.0174 | 0.0115 | ±0.0230 | +1.511 | 0.1308 | 1.0176 |  |
| Hypertension | +0.0524 | 0.1984 | ±0.3967 | +0.264 | 0.7917 | 1.0538 |  |
| High cholesterol | +0.2957 | 0.1868 | ±0.3736 | +1.583 | 0.1134 | 1.3441 |  |
| **Kidney disease** | **+0.5012** | 0.2204 | ±0.4409 | **+2.274** | **0.0230** | 1.6507 | * |
| **Circulatory disease** | **+0.4678** | 0.2019 | ±0.4039 | **+2.317** | **0.0205** | 1.5965 | * |
| Any reading < 54 during wear (0/1) | +0.1029 | 0.1923 | ±0.3847 | +0.535 | 0.5928 | 1.1083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0551**, LLR χ² = **49.79** (p = **6.82e-07**), AUC = **0.6597**, AIC = **877.3**, BIC = **934.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0731 | 0.7326 | ±1.4651 | -0.100 | 0.9205 | 0.9295 |  |
| **Education: graduate level (vs college)** | **-0.4228** | 0.2055 | ±0.4111 | **-2.057** | **0.0397** | 0.6552 | * |
| Education: high school or below (vs college) | +0.2317 | 0.2280 | ±0.4560 | +1.016 | 0.3096 | 1.2607 |  |
| Site: UCSD (vs UAB) | +0.0473 | 0.2158 | ±0.4316 | +0.219 | 0.8265 | 1.0484 |  |
| Site: UW (vs UAB) | +0.0565 | 0.2110 | ±0.4221 | +0.268 | 0.7889 | 1.0581 |  |
| **Age (years)** | **-0.0355** | 0.0089 | ±0.0178 | **-3.989** | **6.63e-05** | 0.9651 | *** |
| BMI (kg/m2) | +0.0181 | 0.0115 | ±0.0230 | +1.570 | 0.1164 | 1.0182 |  |
| Hypertension | +0.0598 | 0.1981 | ±0.3962 | +0.302 | 0.7626 | 1.0617 |  |
| High cholesterol | +0.2881 | 0.1865 | ±0.3729 | +1.545 | 0.1224 | 1.3339 |  |
| **Kidney disease** | **+0.4963** | 0.2206 | ±0.4411 | **+2.250** | **0.0245** | 1.6426 | * |
| **Circulatory disease** | **+0.4813** | 0.2020 | ±0.4041 | **+2.382** | **0.0172** | 1.6183 | * |
| Time < 54 (%) | -0.1044 | 0.2218 | ±0.4436 | -0.471 | 0.6380 | 0.9009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0549**, LLR χ² = **49.58** (p = **7.46e-07**), AUC = **0.6605**, AIC = **877.5**, BIC = **934.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0912 | 0.7322 | ±1.4644 | -0.125 | 0.9008 | 0.9128 |  |
| **Education: graduate level (vs college)** | **-0.4194** | 0.2058 | ±0.4115 | **-2.038** | **0.0415** | 0.6575 | * |
| Education: high school or below (vs college) | +0.2410 | 0.2278 | ±0.4555 | +1.058 | 0.2900 | 1.2725 |  |
| Site: UCSD (vs UAB) | +0.0608 | 0.2155 | ±0.4309 | +0.282 | 0.7779 | 1.0626 |  |
| Site: UW (vs UAB) | +0.0713 | 0.2105 | ±0.4211 | +0.339 | 0.7349 | 1.0739 |  |
| **Age (years)** | **-0.0354** | 0.0089 | ±0.0178 | **-3.980** | **6.89e-05** | 0.9652 | *** |
| BMI (kg/m2) | +0.0177 | 0.0115 | ±0.0230 | +1.542 | 0.1230 | 1.0179 |  |
| Hypertension | +0.0574 | 0.1981 | ±0.3962 | +0.290 | 0.7721 | 1.0591 |  |
| High cholesterol | +0.2907 | 0.1865 | ±0.3731 | +1.558 | 0.1191 | 1.3374 |  |
| **Kidney disease** | **+0.5001** | 0.2204 | ±0.4408 | **+2.269** | **0.0233** | 1.6488 | * |
| **Circulatory disease** | **+0.4724** | 0.2020 | ±0.4039 | **+2.339** | **0.0193** | 1.6039 | * |
| Avg. daily time < 54 (%) | +0.0289 | 0.1779 | ±0.3558 | +0.162 | 0.8711 | 1.0293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0549**, LLR χ² = **49.62** (p = **7.31e-07**), AUC = **0.6604**, AIC = **877.5**, BIC = **934.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0939 | 0.7324 | ±1.4648 | -0.128 | 0.8980 | 0.9104 |  |
| **Education: graduate level (vs college)** | **-0.4181** | 0.2058 | ±0.4117 | **-2.031** | **0.0422** | 0.6583 | * |
| Education: high school or below (vs college) | +0.2397 | 0.2274 | ±0.4549 | +1.054 | 0.2920 | 1.2708 |  |
| Site: UCSD (vs UAB) | +0.0626 | 0.2154 | ±0.4308 | +0.290 | 0.7715 | 1.0646 |  |
| Site: UW (vs UAB) | +0.0721 | 0.2102 | ±0.4204 | +0.343 | 0.7317 | 1.0747 |  |
| **Age (years)** | **-0.0354** | 0.0089 | ±0.0178 | **-3.983** | **6.82e-05** | 0.9652 | *** |
| BMI (kg/m2) | +0.0177 | 0.0115 | ±0.0230 | +1.539 | 0.1238 | 1.0179 |  |
| Hypertension | +0.0566 | 0.1981 | ±0.3963 | +0.286 | 0.7749 | 1.0583 |  |
| High cholesterol | +0.2894 | 0.1864 | ±0.3728 | +1.552 | 0.1206 | 1.3356 |  |
| **Kidney disease** | **+0.4994** | 0.2204 | ±0.4407 | **+2.266** | **0.0234** | 1.6478 | * |
| **Circulatory disease** | **+0.4725** | 0.2017 | ±0.4033 | **+2.343** | **0.0191** | 1.6040 | * |
| Time 54-69, pooled (%) | +0.0153 | 0.0554 | ±0.1109 | +0.277 | 0.7819 | 1.0155 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0551**, LLR χ² = **49.72** (p = **7.04e-07**), AUC = **0.6608**, AIC = **877.4**, BIC = **934.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0928 | 0.7323 | ±1.4645 | -0.127 | 0.8991 | 0.9113 |  |
| **Education: graduate level (vs college)** | **-0.4162** | 0.2059 | ±0.4118 | **-2.021** | **0.0433** | 0.6595 | * |
| Education: high school or below (vs college) | +0.2393 | 0.2275 | ±0.4549 | +1.052 | 0.2928 | 1.2703 |  |
| Site: UCSD (vs UAB) | +0.0641 | 0.2153 | ±0.4306 | +0.298 | 0.7660 | 1.0662 |  |
| Site: UW (vs UAB) | +0.0736 | 0.2102 | ±0.4204 | +0.350 | 0.7260 | 1.0764 |  |
| **Age (years)** | **-0.0355** | 0.0089 | ±0.0178 | **-3.990** | **6.62e-05** | 0.9651 | *** |
| BMI (kg/m2) | +0.0177 | 0.0115 | ±0.0230 | +1.537 | 0.1242 | 1.0178 |  |
| Hypertension | +0.0560 | 0.1981 | ±0.3963 | +0.283 | 0.7774 | 1.0576 |  |
| High cholesterol | +0.2896 | 0.1864 | ±0.3728 | +1.554 | 0.1203 | 1.3359 |  |
| **Kidney disease** | **+0.5000** | 0.2204 | ±0.4407 | **+2.269** | **0.0233** | 1.6488 | * |
| **Circulatory disease** | **+0.4721** | 0.2016 | ±0.4032 | **+2.341** | **0.0192** | 1.6033 | * |
| Avg. daily time 54-69 (%) | +0.0223 | 0.0537 | ±0.1075 | +0.415 | 0.6781 | 1.0226 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0549**, LLR χ² = **49.56** (p = **7.50e-07**), AUC = **0.6605**, AIC = **877.6**, BIC = **934.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0911 | 0.7324 | ±1.4648 | -0.124 | 0.9010 | 0.9129 |  |
| **Education: graduate level (vs college)** | **-0.4197** | 0.2058 | ±0.4116 | **-2.039** | **0.0414** | 0.6573 | * |
| Education: high school or below (vs college) | +0.2397 | 0.2275 | ±0.4550 | +1.054 | 0.2921 | 1.2709 |  |
| Site: UCSD (vs UAB) | +0.0602 | 0.2156 | ±0.4312 | +0.279 | 0.7802 | 1.0620 |  |
| Site: UW (vs UAB) | +0.0703 | 0.2104 | ±0.4208 | +0.334 | 0.7383 | 1.0728 |  |
| **Age (years)** | **-0.0354** | 0.0089 | ±0.0178 | **-3.979** | **6.91e-05** | 0.9652 | *** |
| BMI (kg/m2) | +0.0177 | 0.0115 | ±0.0230 | +1.542 | 0.1232 | 1.0179 |  |
| Hypertension | +0.0574 | 0.1981 | ±0.3963 | +0.290 | 0.7721 | 1.0591 |  |
| High cholesterol | +0.2897 | 0.1864 | ±0.3728 | +1.554 | 0.1202 | 1.3360 |  |
| **Kidney disease** | **+0.4995** | 0.2204 | ±0.4408 | **+2.267** | **0.0234** | 1.6480 | * |
| **Circulatory disease** | **+0.4734** | 0.2018 | ±0.4035 | **+2.346** | **0.0190** | 1.6055 | * |
| Time < 70 (%) | +0.0052 | 0.0461 | ±0.0922 | +0.113 | 0.9099 | 1.0052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0550**, LLR χ² = **49.69** (p = **7.12e-07**), AUC = **0.6606**, AIC = **877.4**, BIC = **934.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0933 | 0.7323 | ±1.4645 | -0.127 | 0.8986 | 0.9109 |  |
| **Education: graduate level (vs college)** | **-0.4166** | 0.2059 | ±0.4118 | **-2.023** | **0.0431** | 0.6593 | * |
| Education: high school or below (vs college) | +0.2404 | 0.2275 | ±0.4549 | +1.057 | 0.2906 | 1.2717 |  |
| Site: UCSD (vs UAB) | +0.0641 | 0.2154 | ±0.4308 | +0.298 | 0.7659 | 1.0662 |  |
| Site: UW (vs UAB) | +0.0740 | 0.2103 | ±0.4207 | +0.352 | 0.7249 | 1.0768 |  |
| **Age (years)** | **-0.0355** | 0.0089 | ±0.0178 | **-3.987** | **6.68e-05** | 0.9652 | *** |
| BMI (kg/m2) | +0.0177 | 0.0115 | ±0.0230 | +1.537 | 0.1242 | 1.0178 |  |
| Hypertension | +0.0562 | 0.1982 | ±0.3963 | +0.283 | 0.7768 | 1.0578 |  |
| High cholesterol | +0.2902 | 0.1864 | ±0.3729 | +1.557 | 0.1195 | 1.3367 |  |
| **Kidney disease** | **+0.5003** | 0.2204 | ±0.4407 | **+2.270** | **0.0232** | 1.6492 | * |
| **Circulatory disease** | **+0.4715** | 0.2017 | ±0.4034 | **+2.337** | **0.0194** | 1.6023 | * |
| Avg. daily time < 70 (%) | +0.0166 | 0.0438 | ±0.0876 | +0.379 | 0.7046 | 1.0167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0576**, LLR χ² = **52.01** (p = **2.72e-07**), AUC = **0.6656**, AIC = **875.1**, BIC = **932.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.6013 | 0.8501 | ±1.7002 | +0.707 | 0.4794 | 1.8245 |  |
| Education: graduate level (vs college) | -0.3918 | 0.2067 | ±0.4134 | -1.896 | 0.0580 | 0.6758 | . |
| Education: high school or below (vs college) | +0.2065 | 0.2291 | ±0.4583 | +0.901 | 0.3675 | 1.2294 |  |
| Site: UCSD (vs UAB) | +0.0836 | 0.2158 | ±0.4317 | +0.388 | 0.6984 | 1.0872 |  |
| Site: UW (vs UAB) | +0.0978 | 0.2110 | ±0.4219 | +0.463 | 0.6430 | 1.1027 |  |
| **Age (years)** | **-0.0350** | 0.0089 | ±0.0178 | **-3.931** | **8.47e-05** | 0.9656 | *** |
| BMI (kg/m2) | +0.0174 | 0.0115 | ±0.0230 | +1.509 | 0.1312 | 1.0175 |  |
| Hypertension | +0.0528 | 0.1984 | ±0.3968 | +0.266 | 0.7901 | 1.0542 |  |
| High cholesterol | +0.2923 | 0.1866 | ±0.3733 | +1.566 | 0.1174 | 1.3395 |  |
| **Kidney disease** | **+0.4796** | 0.2211 | ±0.4423 | **+2.169** | **0.0301** | 1.6155 | * |
| **Circulatory disease** | **+0.4767** | 0.2015 | ±0.4030 | **+2.365** | **0.0180** | 1.6107 | * |
| Time 54-250, pooled (%) | -0.0077 | 0.0049 | ±0.0097 | -1.594 | 0.1110 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0569**, LLR χ² = **51.40** (p = **3.51e-07**), AUC = **0.6650**, AIC = **875.7**, BIC = **932.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.5290 | 0.8574 | ±1.7149 | +0.617 | 0.5373 | 1.6972 |  |
| Education: graduate level (vs college) | -0.3959 | 0.2066 | ±0.4132 | -1.916 | 0.0553 | 0.6731 | . |
| Education: high school or below (vs college) | +0.2108 | 0.2290 | ±0.4579 | +0.921 | 0.3571 | 1.2347 |  |
| Site: UCSD (vs UAB) | +0.0806 | 0.2157 | ±0.4315 | +0.374 | 0.7087 | 1.0839 |  |
| Site: UW (vs UAB) | +0.0930 | 0.2108 | ±0.4216 | +0.441 | 0.6590 | 1.0975 |  |
| **Age (years)** | **-0.0351** | 0.0089 | ±0.0178 | **-3.950** | **7.82e-05** | 0.9655 | *** |
| BMI (kg/m2) | +0.0174 | 0.0115 | ±0.0230 | +1.512 | 0.1306 | 1.0176 |  |
| Hypertension | +0.0543 | 0.1983 | ±0.3966 | +0.274 | 0.7841 | 1.0558 |  |
| High cholesterol | +0.2920 | 0.1866 | ±0.3731 | +1.565 | 0.1176 | 1.3391 |  |
| **Kidney disease** | **+0.4806** | 0.2211 | ±0.4423 | **+2.173** | **0.0298** | 1.6170 | * |
| **Circulatory disease** | **+0.4756** | 0.2015 | ±0.4030 | **+2.361** | **0.0182** | 1.6091 | * |
| Avg. daily time 54-250 (%) | -0.0068 | 0.0049 | ±0.0099 | -1.381 | 0.1673 | 0.9932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0564**, LLR χ² = **50.95** (p = **4.23e-07**), AUC = **0.6631**, AIC = **876.2**, BIC = **933.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1188 | 0.7318 | ±1.4636 | -0.162 | 0.8710 | 0.8880 |  |
| **Education: graduate level (vs college)** | **-0.4082** | 0.2061 | ±0.4121 | **-1.981** | **0.0476** | 0.6648 | * |
| Education: high school or below (vs college) | +0.2195 | 0.2281 | ±0.4562 | +0.962 | 0.3360 | 1.2454 |  |
| Site: UCSD (vs UAB) | +0.0744 | 0.2154 | ±0.4308 | +0.346 | 0.7297 | 1.0773 |  |
| Site: UW (vs UAB) | +0.0677 | 0.2099 | ±0.4197 | +0.323 | 0.7470 | 1.0700 |  |
| **Age (years)** | **-0.0367** | 0.0090 | ±0.0179 | **-4.095** | **4.22e-05** | 0.9640 | *** |
| BMI (kg/m2) | +0.0172 | 0.0115 | ±0.0230 | +1.492 | 0.1357 | 1.0173 |  |
| Hypertension | +0.0755 | 0.1990 | ±0.3981 | +0.379 | 0.7046 | 1.0784 |  |
| High cholesterol | +0.2998 | 0.1870 | ±0.3741 | +1.603 | 0.1089 | 1.3496 |  |
| **Kidney disease** | **+0.4774** | 0.2213 | ±0.4426 | **+2.157** | **0.0310** | 1.6119 | * |
| **Circulatory disease** | **+0.4719** | 0.2018 | ±0.4037 | **+2.338** | **0.0194** | 1.6031 | * |
| Time 181-250, pooled (%) | +0.0065 | 0.0054 | ±0.0109 | +1.189 | 0.2344 | 1.0065 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0566**, LLR χ² = **51.14** (p = **3.90e-07**), AUC = **0.6634**, AIC = **876.0**, BIC = **933.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1212 | 0.7319 | ±1.4637 | -0.166 | 0.8685 | 0.8859 |  |
| **Education: graduate level (vs college)** | **-0.4082** | 0.2061 | ±0.4121 | **-1.981** | **0.0476** | 0.6649 | * |
| Education: high school or below (vs college) | +0.2161 | 0.2283 | ±0.4566 | +0.947 | 0.3438 | 1.2413 |  |
| Site: UCSD (vs UAB) | +0.0768 | 0.2155 | ±0.4309 | +0.356 | 0.7217 | 1.0798 |  |
| Site: UW (vs UAB) | +0.0684 | 0.2099 | ±0.4198 | +0.326 | 0.7446 | 1.0708 |  |
| **Age (years)** | **-0.0367** | 0.0090 | ±0.0179 | **-4.101** | **4.12e-05** | 0.9639 | *** |
| BMI (kg/m2) | +0.0171 | 0.0115 | ±0.0231 | +1.485 | 0.1376 | 1.0173 |  |
| Hypertension | +0.0764 | 0.1991 | ±0.3981 | +0.384 | 0.7011 | 1.0794 |  |
| High cholesterol | +0.3000 | 0.1870 | ±0.3741 | +1.604 | 0.1087 | 1.3499 |  |
| **Kidney disease** | **+0.4758** | 0.2213 | ±0.4427 | **+2.149** | **0.0316** | 1.6093 | * |
| **Circulatory disease** | **+0.4725** | 0.2018 | ±0.4037 | **+2.341** | **0.0192** | 1.6040 | * |
| Avg. daily time 181-250 (%) | +0.0068 | 0.0053 | ±0.0107 | +1.270 | 0.2041 | 1.0068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0580**, LLR χ² = **52.42** (p = **2.29e-07**), AUC = **0.6653**, AIC = **874.7**, BIC = **931.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1718 | 0.7337 | ±1.4674 | -0.234 | 0.8148 | 0.8421 |  |
| Education: graduate level (vs college) | -0.3909 | 0.2067 | ±0.4134 | -1.891 | 0.0586 | 0.6764 | . |
| Education: high school or below (vs college) | +0.2000 | 0.2291 | ±0.4583 | +0.873 | 0.3827 | 1.2215 |  |
| Site: UCSD (vs UAB) | +0.0887 | 0.2160 | ±0.4320 | +0.411 | 0.6814 | 1.0927 |  |
| Site: UW (vs UAB) | +0.0875 | 0.2104 | ±0.4208 | +0.416 | 0.6775 | 1.0914 |  |
| **Age (years)** | **-0.0362** | 0.0089 | ±0.0178 | **-4.067** | **4.76e-05** | 0.9644 | *** |
| BMI (kg/m2) | +0.0171 | 0.0115 | ±0.0231 | +1.479 | 0.1391 | 1.0172 |  |
| Hypertension | +0.0694 | 0.1987 | ±0.3974 | +0.349 | 0.7270 | 1.0718 |  |
| High cholesterol | +0.3000 | 0.1870 | ±0.3740 | +1.604 | 0.1087 | 1.3498 |  |
| **Kidney disease** | **+0.4674** | 0.2216 | ±0.4432 | **+2.109** | **0.0349** | 1.5958 | * |
| **Circulatory disease** | **+0.4746** | 0.2018 | ±0.4035 | **+2.352** | **0.0187** | 1.6073 | * |
| Time > 180 (%) | +0.0054 | 0.0031 | ±0.0063 | +1.709 | 0.0874 | 1.0054 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0577**, LLR χ² = **52.09** (p = **2.63e-07**), AUC = **0.6649**, AIC = **875.0**, BIC = **932.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1612 | 0.7334 | ±1.4668 | -0.220 | 0.8261 | 0.8512 |  |
| Education: graduate level (vs college) | -0.3936 | 0.2066 | ±0.4132 | -1.905 | 0.0567 | 0.6746 | . |
| Education: high school or below (vs college) | +0.2009 | 0.2292 | ±0.4584 | +0.877 | 0.3807 | 1.2225 |  |
| Site: UCSD (vs UAB) | +0.0881 | 0.2160 | ±0.4320 | +0.408 | 0.6834 | 1.0921 |  |
| Site: UW (vs UAB) | +0.0862 | 0.2103 | ±0.4207 | +0.410 | 0.6819 | 1.0900 |  |
| **Age (years)** | **-0.0362** | 0.0089 | ±0.0178 | **-4.065** | **4.81e-05** | 0.9645 | *** |
| BMI (kg/m2) | +0.0170 | 0.0115 | ±0.0230 | +1.478 | 0.1394 | 1.0172 |  |
| Hypertension | +0.0692 | 0.1987 | ±0.3973 | +0.349 | 0.7274 | 1.0717 |  |
| High cholesterol | +0.2990 | 0.1870 | ±0.3739 | +1.599 | 0.1097 | 1.3485 |  |
| **Kidney disease** | **+0.4679** | 0.2216 | ±0.4432 | **+2.111** | **0.0347** | 1.5966 | * |
| **Circulatory disease** | **+0.4744** | 0.2017 | ±0.4034 | **+2.352** | **0.0187** | 1.6071 | * |
| Avg. daily time > 180 (%) | +0.0050 | 0.0031 | ±0.0063 | +1.608 | 0.1079 | 1.0051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0614**, LLR χ² = **55.44** (p = **6.44e-08**), AUC = **0.6701**, AIC = **871.7**, BIC = **928.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1888 | 0.7337 | ±1.4674 | -0.257 | 0.7969 | 0.8279 |  |
| Education: graduate level (vs college) | -0.3699 | 0.2074 | ±0.4147 | -1.784 | 0.0744 | 0.6908 | . |
| Education: high school or below (vs college) | +0.1909 | 0.2294 | ±0.4587 | +0.832 | 0.4051 | 1.2104 |  |
| Site: UCSD (vs UAB) | +0.1112 | 0.2168 | ±0.4336 | +0.513 | 0.6079 | 1.1177 |  |
| Site: UW (vs UAB) | +0.0917 | 0.2108 | ±0.4216 | +0.435 | 0.6635 | 1.0960 |  |
| **Age (years)** | **-0.0358** | 0.0089 | ±0.0178 | **-4.028** | **5.62e-05** | 0.9648 | *** |
| BMI (kg/m2) | +0.0156 | 0.0116 | ±0.0232 | +1.351 | 0.1767 | 1.0158 |  |
| Hypertension | +0.0777 | 0.1992 | ±0.3984 | +0.390 | 0.6966 | 1.0808 |  |
| High cholesterol | +0.3101 | 0.1876 | ±0.3752 | +1.653 | 0.0984 | 1.3636 | . |
| **Kidney disease** | **+0.4632** | 0.2218 | ±0.4435 | **+2.089** | **0.0367** | 1.5891 | * |
| **Circulatory disease** | **+0.4730** | 0.2021 | ±0.4042 | **+2.340** | **0.0193** | 1.6048 | * |
| **Nocturnal time > 180 (%)** | **+0.0072** | 0.0029 | ±0.0059 | **+2.463** | **0.0138** | 1.0073 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0549**, LLR χ² = **49.62** (p = **7.32e-07**), AUC = **0.6604**, AIC = **877.5**, BIC = **934.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1024 | 0.7338 | ±1.4676 | -0.140 | 0.8890 | 0.9027 |  |
| **Education: graduate level (vs college)** | **-0.4153** | 0.2065 | ±0.4131 | **-2.011** | **0.0443** | 0.6601 | * |
| Education: high school or below (vs college) | +0.2364 | 0.2277 | ±0.4553 | +1.038 | 0.2991 | 1.2666 |  |
| Site: UCSD (vs UAB) | +0.0597 | 0.2148 | ±0.4297 | +0.278 | 0.7812 | 1.0615 |  |
| Site: UW (vs UAB) | +0.0668 | 0.2098 | ±0.4196 | +0.318 | 0.7503 | 1.0691 |  |
| **Age (years)** | **-0.0358** | 0.0090 | ±0.0180 | **-3.968** | **7.24e-05** | 0.9649 | *** |
| BMI (kg/m2) | +0.0179 | 0.0115 | ±0.0230 | +1.556 | 0.1198 | 1.0181 |  |
| Hypertension | +0.0601 | 0.1983 | ±0.3966 | +0.303 | 0.7618 | 1.0619 |  |
| High cholesterol | +0.2909 | 0.1865 | ±0.3731 | +1.560 | 0.1189 | 1.3376 |  |
| **Kidney disease** | **+0.4931** | 0.2216 | ±0.4431 | **+2.225** | **0.0260** | 1.6374 | * |
| **Circulatory disease** | **+0.4762** | 0.2017 | ±0.4033 | **+2.361** | **0.0182** | 1.6099 | * |
| Any reading > 250 during wear (0/1) | +0.0492 | 0.1821 | ±0.3643 | +0.270 | 0.7869 | 1.0505 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0576**, LLR χ² = **52.04** (p = **2.68e-07**), AUC = **0.6655**, AIC = **875.1**, BIC = **932.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1725 | 0.7350 | ±1.4700 | -0.235 | 0.8145 | 0.8416 |  |
| Education: graduate level (vs college) | -0.3919 | 0.2067 | ±0.4133 | -1.896 | 0.0579 | 0.6758 | . |
| Education: high school or below (vs college) | +0.2057 | 0.2292 | ±0.4584 | +0.898 | 0.3694 | 1.2284 |  |
| Site: UCSD (vs UAB) | +0.0829 | 0.2158 | ±0.4316 | +0.384 | 0.7009 | 1.0864 |  |
| Site: UW (vs UAB) | +0.0970 | 0.2109 | ±0.4218 | +0.460 | 0.6457 | 1.1018 |  |
| **Age (years)** | **-0.0350** | 0.0089 | ±0.0178 | **-3.931** | **8.44e-05** | 0.9656 | *** |
| BMI (kg/m2) | +0.0174 | 0.0115 | ±0.0230 | +1.511 | 0.1308 | 1.0176 |  |
| Hypertension | +0.0529 | 0.1984 | ±0.3968 | +0.267 | 0.7896 | 1.0544 |  |
| High cholesterol | +0.2922 | 0.1866 | ±0.3733 | +1.565 | 0.1175 | 1.3393 |  |
| **Kidney disease** | **+0.4793** | 0.2212 | ±0.4423 | **+2.167** | **0.0302** | 1.6149 | * |
| **Circulatory disease** | **+0.4772** | 0.2015 | ±0.4031 | **+2.368** | **0.0179** | 1.6116 | * |
| Time > 250 (%) | +0.0078 | 0.0049 | ±0.0097 | +1.604 | 0.1088 | 1.0078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 865)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **865**, events = **187**, McFadden pseudo-R² = **0.0569**, LLR χ² = **51.38** (p = **3.53e-07**), AUC = **0.6649**, AIC = **875.7**, BIC = **932.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1528 | 0.7343 | ±1.4685 | -0.208 | 0.8351 | 0.8583 |  |
| Education: graduate level (vs college) | -0.3963 | 0.2066 | ±0.4131 | -1.918 | 0.0551 | 0.6728 | . |
| Education: high school or below (vs college) | +0.2105 | 0.2290 | ±0.4580 | +0.919 | 0.3579 | 1.2343 |  |
| Site: UCSD (vs UAB) | +0.0799 | 0.2157 | ±0.4314 | +0.370 | 0.7111 | 1.0832 |  |
| Site: UW (vs UAB) | +0.0922 | 0.2108 | ±0.4215 | +0.438 | 0.6617 | 1.0966 |  |
| **Age (years)** | **-0.0351** | 0.0089 | ±0.0178 | **-3.950** | **7.82e-05** | 0.9655 | *** |
| BMI (kg/m2) | +0.0174 | 0.0115 | ±0.0230 | +1.513 | 0.1304 | 1.0176 |  |
| Hypertension | +0.0545 | 0.1983 | ±0.3966 | +0.275 | 0.7835 | 1.0560 |  |
| High cholesterol | +0.2917 | 0.1866 | ±0.3731 | +1.564 | 0.1179 | 1.3387 |  |
| **Kidney disease** | **+0.4805** | 0.2211 | ±0.4423 | **+2.173** | **0.0298** | 1.6169 | * |
| **Circulatory disease** | **+0.4761** | 0.2015 | ±0.4030 | **+2.363** | **0.0181** | 1.6098 | * |
| Avg. daily time > 250 (%) | +0.0068 | 0.0049 | ±0.0099 | +1.375 | 0.1690 | 1.0068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.1679**, Adj R² = **0.1549**, F-statistic = **12.96** (p = **2.60e-26**), Residual SE = **0.922** on **835** df, AIC = **2286.0**, BIC = **2352.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1741** | 0.3074 | ±0.6148 | **+10.327** | **5.35e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2316** | 0.0653 | ±0.1306 | **-3.547** | **3.90e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4494** | 0.1130 | ±0.2260 | **+3.977** | **6.97e-05** | *** |
| Site: UCSD (vs UAB) | +0.1177 | 0.0748 | ±0.1496 | +1.574 | 0.1156 |  |
| **Site: UW (vs UAB)** | **-0.3126** | 0.0822 | ±0.1645 | **-3.801** | **1.44e-04** | *** |
| Season: spring (vs autumn) | -0.1711 | 0.0886 | ±0.1772 | -1.931 | 0.0535 | . |
| Season: summer (vs autumn) | +0.0442 | 0.0891 | ±0.1783 | +0.496 | 0.6200 |  |
| Season: winter (vs autumn) | +0.0051 | 0.0957 | ±0.1914 | +0.053 | 0.9576 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.735** | **1.64e-11** | *** |
| BMI (kg/m2) | +0.0075 | 0.0051 | ±0.0102 | +1.464 | 0.1431 |  |
| Hypertension | +0.0983 | 0.0661 | ±0.1322 | +1.487 | 0.1370 |  |
| High cholesterol | -0.0738 | 0.0669 | ±0.1338 | -1.103 | 0.2699 |  |
| Kidney disease | -0.0557 | 0.0833 | ±0.1667 | -0.669 | 0.5036 |  |
| Circulatory disease | +0.0133 | 0.0787 | ±0.1574 | +0.168 | 0.8663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.1790**, Adj R² = **0.1652**, F-statistic = **12.99** (p = **5.17e-28**), Residual SE = **0.917** on **834** df, AIC = **2276.6**, BIC = **2347.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6657** | 0.3407 | ±0.6813 | **+7.825** | **5.08e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2112** | 0.0660 | ±0.1321 | **-3.197** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **+0.4155** | 0.1097 | ±0.2195 | **+3.787** | **1.52e-04** | *** |
| Site: UCSD (vs UAB) | +0.1321 | 0.0747 | ±0.1494 | +1.768 | 0.0770 | . |
| **Site: UW (vs UAB)** | **-0.3006** | 0.0812 | ±0.1624 | **-3.702** | **2.14e-04** | *** |
| Season: spring (vs autumn) | -0.1628 | 0.0880 | ±0.1761 | -1.849 | 0.0644 | . |
| Season: summer (vs autumn) | +0.0558 | 0.0887 | ±0.1773 | +0.629 | 0.5295 |  |
| Season: winter (vs autumn) | -0.0006 | 0.0949 | ±0.1899 | -0.006 | 0.9952 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.933** | **4.11e-12** | *** |
| BMI (kg/m2) | +0.0062 | 0.0052 | ±0.0104 | +1.191 | 0.2336 |  |
| Hypertension | +0.0975 | 0.0658 | ±0.1317 | +1.481 | 0.1387 |  |
| High cholesterol | -0.0735 | 0.0669 | ±0.1337 | -1.100 | 0.2713 |  |
| Kidney disease | -0.0617 | 0.0828 | ±0.1656 | -0.746 | 0.4559 |  |
| Circulatory disease | +0.0093 | 0.0780 | ±0.1560 | +0.119 | 0.9055 |  |
| **HbA1c (%)** | **+0.0841** | 0.0320 | ±0.0640 | **+2.626** | **0.0086** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.1704**, Adj R² = **0.1565**, F-statistic = **12.24** (p = **2.93e-26**), Residual SE = **0.922** on **834** df, AIC = **2285.4**, BIC = **2356.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9995** | 0.3223 | ±0.6447 | **+9.306** | **1.33e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2231** | 0.0661 | ±0.1322 | **-3.375** | **7.37e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4362** | 0.1111 | ±0.2223 | **+3.925** | **8.66e-05** | *** |
| Site: UCSD (vs UAB) | +0.1264 | 0.0744 | ±0.1488 | +1.698 | 0.0894 | . |
| **Site: UW (vs UAB)** | **-0.3086** | 0.0819 | ±0.1639 | **-3.766** | **1.66e-04** | *** |
| Season: spring (vs autumn) | -0.1739 | 0.0889 | ±0.1779 | -1.955 | 0.0506 | . |
| Season: summer (vs autumn) | +0.0477 | 0.0891 | ±0.1783 | +0.536 | 0.5923 |  |
| Season: winter (vs autumn) | -0.0017 | 0.0956 | ±0.1912 | -0.018 | 0.9856 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0063 | **-6.799** | **1.05e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.403 | 0.1606 |  |
| Hypertension | +0.1005 | 0.0660 | ±0.1320 | +1.523 | 0.1278 |  |
| High cholesterol | -0.0709 | 0.0672 | ±0.1343 | -1.055 | 0.2913 |  |
| Kidney disease | -0.0673 | 0.0832 | ±0.1664 | -0.809 | 0.4186 |  |
| Circulatory disease | +0.0118 | 0.0787 | ±0.1575 | +0.149 | 0.8812 |  |
| Mean glucose (mg/dL) | +0.0013 | 0.0010 | ±0.0019 | +1.308 | 0.1910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.1704**, Adj R² = **0.1565**, F-statistic = **12.24** (p = **2.93e-26**), Residual SE = **0.922** on **834** df, AIC = **2285.4**, BIC = **2356.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8256** | 0.3860 | ±0.7720 | **+7.321** | **2.47e-13** | *** |
| **Education: graduate level (vs college)** | **-0.2231** | 0.0661 | ±0.1322 | **-3.375** | **7.37e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4362** | 0.1111 | ±0.2223 | **+3.925** | **8.66e-05** | *** |
| Site: UCSD (vs UAB) | +0.1264 | 0.0744 | ±0.1488 | +1.698 | 0.0894 | . |
| **Site: UW (vs UAB)** | **-0.3086** | 0.0819 | ±0.1639 | **-3.766** | **1.66e-04** | *** |
| Season: spring (vs autumn) | -0.1739 | 0.0889 | ±0.1779 | -1.955 | 0.0506 | . |
| Season: summer (vs autumn) | +0.0477 | 0.0891 | ±0.1783 | +0.536 | 0.5923 |  |
| Season: winter (vs autumn) | -0.0017 | 0.0956 | ±0.1912 | -0.018 | 0.9856 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0063 | **-6.799** | **1.05e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.403 | 0.1606 |  |
| Hypertension | +0.1005 | 0.0660 | ±0.1320 | +1.523 | 0.1278 |  |
| High cholesterol | -0.0709 | 0.0672 | ±0.1343 | -1.055 | 0.2913 |  |
| Kidney disease | -0.0673 | 0.0832 | ±0.1664 | -0.809 | 0.4186 |  |
| Circulatory disease | +0.0118 | 0.0787 | ±0.1575 | +0.149 | 0.8812 |  |
| GMI (%) | +0.0525 | 0.0402 | ±0.0803 | +1.308 | 0.1910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.1720**, Adj R² = **0.1581**, F-statistic = **12.38** (p = **1.39e-26**), Residual SE = **0.921** on **834** df, AIC = **2283.8**, BIC = **2355.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9549** | 0.3188 | ±0.6375 | **+9.270** | **1.86e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2208** | 0.0660 | ±0.1321 | **-3.344** | **8.25e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4333** | 0.1108 | ±0.2216 | **+3.911** | **9.21e-05** | *** |
| Site: UCSD (vs UAB) | +0.1282 | 0.0745 | ±0.1489 | +1.722 | 0.0850 | . |
| **Site: UW (vs UAB)** | **-0.3113** | 0.0820 | ±0.1641 | **-3.795** | **1.48e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1766** | 0.0889 | ±0.1779 | **-1.986** | **0.0471** | * |
| Season: summer (vs autumn) | +0.0481 | 0.0890 | ±0.1780 | +0.540 | 0.5892 |  |
| Season: winter (vs autumn) | -0.0046 | 0.0955 | ±0.1910 | -0.049 | 0.9612 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.762** | **1.36e-11** | *** |
| BMI (kg/m2) | +0.0068 | 0.0052 | ±0.0104 | +1.307 | 0.1914 |  |
| Hypertension | +0.1023 | 0.0660 | ±0.1320 | +1.551 | 0.1210 |  |
| High cholesterol | -0.0712 | 0.0670 | ±0.1341 | -1.061 | 0.2885 |  |
| Kidney disease | -0.0653 | 0.0826 | ±0.1651 | -0.790 | 0.4294 |  |
| Circulatory disease | +0.0115 | 0.0788 | ±0.1575 | +0.146 | 0.8837 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0016 | 0.0010 | ±0.0019 | +1.646 | 0.0998 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.1714**, Adj R² = **0.1575**, F-statistic = **12.33** (p = **1.83e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.4**, BIC = **2355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0552** | 0.3070 | ±0.6140 | **+9.952** | **2.47e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2194** | 0.0659 | ±0.1318 | **-3.328** | **8.74e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4313** | 0.1127 | ±0.2254 | **+3.827** | **1.29e-04** | *** |
| Site: UCSD (vs UAB) | +0.1285 | 0.0743 | ±0.1485 | +1.731 | 0.0835 | . |
| **Site: UW (vs UAB)** | **-0.3018** | 0.0817 | ±0.1634 | **-3.695** | **2.20e-04** | *** |
| Season: spring (vs autumn) | -0.1734 | 0.0888 | ±0.1777 | -1.952 | 0.0509 | . |
| Season: summer (vs autumn) | +0.0501 | 0.0893 | ±0.1785 | +0.561 | 0.5749 |  |
| Season: winter (vs autumn) | -0.0012 | 0.0955 | ±0.1909 | -0.012 | 0.9903 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0063 | **-6.843** | **7.75e-12** | *** |
| BMI (kg/m2) | +0.0074 | 0.0051 | ±0.0102 | +1.458 | 0.1447 |  |
| Hypertension | +0.0993 | 0.0661 | ±0.1322 | +1.503 | 0.1330 |  |
| High cholesterol | -0.0683 | 0.0671 | ±0.1343 | -1.018 | 0.3087 |  |
| Kidney disease | -0.0850 | 0.0822 | ±0.1644 | -1.034 | 0.3010 |  |
| Circulatory disease | +0.0102 | 0.0785 | ±0.1570 | +0.129 | 0.8970 |  |
| Glucose SD, pooled (mg/dL) | +0.0045 | 0.0024 | ±0.0049 | +1.837 | 0.0662 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.1696**, Adj R² = **0.1557**, F-statistic = **12.17** (p = **4.26e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.3**, BIC = **2357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0844** | 0.3091 | ±0.6182 | **+9.979** | **1.88e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2236** | 0.0660 | ±0.1319 | **-3.390** | **7.00e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4356** | 0.1133 | ±0.2265 | **+3.846** | **1.20e-04** | *** |
| Site: UCSD (vs UAB) | +0.1249 | 0.0744 | ±0.1488 | +1.679 | 0.0931 | . |
| **Site: UW (vs UAB)** | **-0.3059** | 0.0819 | ±0.1638 | **-3.735** | **1.88e-04** | *** |
| Season: spring (vs autumn) | -0.1730 | 0.0888 | ±0.1776 | -1.948 | 0.0514 | . |
| Season: summer (vs autumn) | +0.0492 | 0.0895 | ±0.1789 | +0.550 | 0.5823 |  |
| Season: winter (vs autumn) | +0.0016 | 0.0956 | ±0.1912 | +0.017 | 0.9863 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0064 | **-6.785** | **1.16e-11** | *** |
| BMI (kg/m2) | +0.0076 | 0.0051 | ±0.0102 | +1.496 | 0.1347 |  |
| Hypertension | +0.0994 | 0.0661 | ±0.1322 | +1.503 | 0.1328 |  |
| High cholesterol | -0.0700 | 0.0671 | ±0.1342 | -1.042 | 0.2972 |  |
| Kidney disease | -0.0769 | 0.0823 | ±0.1645 | -0.935 | 0.3496 |  |
| Circulatory disease | +0.0122 | 0.0786 | ±0.1573 | +0.155 | 0.8770 |  |
| Avg. daily SD (mg/dL) | +0.0036 | 0.0027 | ±0.0055 | +1.318 | 0.1876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.1708**, Adj R² = **0.1569**, F-statistic = **12.27** (p = **2.46e-26**), Residual SE = **0.921** on **834** df, AIC = **2285.1**, BIC = **2356.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9981** | 0.3235 | ±0.6470 | **+9.268** | **1.90e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2235** | 0.0654 | ±0.1307 | **-3.419** | **6.28e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4366** | 0.1144 | ±0.2288 | **+3.816** | **1.36e-04** | *** |
| Site: UCSD (vs UAB) | +0.1252 | 0.0744 | ±0.1489 | +1.681 | 0.0928 | . |
| **Site: UW (vs UAB)** | **-0.3013** | 0.0823 | ±0.1645 | **-3.663** | **2.50e-04** | *** |
| Season: spring (vs autumn) | -0.1702 | 0.0888 | ±0.1777 | -1.915 | 0.0554 | . |
| Season: summer (vs autumn) | +0.0475 | 0.0894 | ±0.1787 | +0.532 | 0.5947 |  |
| Season: winter (vs autumn) | +0.0036 | 0.0958 | ±0.1916 | +0.038 | 0.9698 |  |
| **Age (years)** | **-0.0218** | 0.0032 | ±0.0064 | **-6.837** | **8.09e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0051 | ±0.0102 | +1.511 | 0.1309 |  |
| Hypertension | +0.0964 | 0.0662 | ±0.1323 | +1.457 | 0.1450 |  |
| High cholesterol | -0.0693 | 0.0670 | ±0.1340 | -1.034 | 0.3010 |  |
| Kidney disease | -0.0830 | 0.0826 | ±0.1652 | -1.005 | 0.3149 |  |
| Circulatory disease | +0.0101 | 0.0785 | ±0.1569 | +0.129 | 0.8976 |  |
| CV (%) | +0.0096 | 0.0060 | ±0.0119 | +1.604 | 0.1088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.1714**, Adj R² = **0.1575**, F-statistic = **12.33** (p = **1.84e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.4**, BIC = **2355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4514** | 0.3477 | ±0.6955 | **+9.925** | **3.24e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2230** | 0.0653 | ±0.1306 | **-3.414** | **6.41e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4340** | 0.1145 | ±0.2291 | **+3.789** | **1.51e-04** | *** |
| Site: UCSD (vs UAB) | +0.1240 | 0.0745 | ±0.1491 | +1.664 | 0.0962 | . |
| **Site: UW (vs UAB)** | **-0.3014** | 0.0824 | ±0.1647 | **-3.659** | **2.53e-04** | *** |
| Season: spring (vs autumn) | -0.1716 | 0.0887 | ±0.1774 | -1.935 | 0.0530 | . |
| Season: summer (vs autumn) | +0.0438 | 0.0891 | ±0.1783 | +0.492 | 0.6230 |  |
| Season: winter (vs autumn) | +0.0016 | 0.0958 | ±0.1915 | +0.017 | 0.9866 |  |
| **Age (years)** | **-0.0219** | 0.0032 | ±0.0064 | **-6.855** | **7.14e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0051 | ±0.0101 | +1.511 | 0.1308 |  |
| Hypertension | +0.0963 | 0.0661 | ±0.1321 | +1.458 | 0.1450 |  |
| High cholesterol | -0.0699 | 0.0668 | ±0.1337 | -1.046 | 0.2956 |  |
| Kidney disease | -0.0795 | 0.0826 | ±0.1653 | -0.962 | 0.3361 |  |
| Circulatory disease | +0.0082 | 0.0783 | ±0.1566 | +0.105 | 0.9166 |  |
| Mean / SD ratio | -0.0474 | 0.0250 | ±0.0500 | -1.898 | 0.0576 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.1697**, Adj R² = **0.1558**, F-statistic = **12.18** (p = **4.13e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.2**, BIC = **2357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3616** | 0.3402 | ±0.6804 | **+9.881** | **5.05e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2249** | 0.0655 | ±0.1310 | **-3.433** | **5.97e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4390** | 0.1148 | ±0.2295 | **+3.825** | **1.31e-04** | *** |
| Site: UCSD (vs UAB) | +0.1193 | 0.0748 | ±0.1495 | +1.595 | 0.1106 |  |
| **Site: UW (vs UAB)** | **-0.3060** | 0.0825 | ±0.1649 | **-3.711** | **2.06e-04** | *** |
| Season: spring (vs autumn) | -0.1700 | 0.0888 | ±0.1775 | -1.916 | 0.0554 | . |
| Season: summer (vs autumn) | +0.0458 | 0.0894 | ±0.1787 | +0.513 | 0.6081 |  |
| Season: winter (vs autumn) | +0.0044 | 0.0959 | ±0.1918 | +0.046 | 0.9633 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0064 | **-6.796** | **1.08e-11** | *** |
| BMI (kg/m2) | +0.0078 | 0.0051 | ±0.0102 | +1.536 | 0.1244 |  |
| Hypertension | +0.0967 | 0.0661 | ±0.1323 | +1.462 | 0.1439 |  |
| High cholesterol | -0.0709 | 0.0669 | ±0.1338 | -1.061 | 0.2889 |  |
| Kidney disease | -0.0703 | 0.0827 | ±0.1655 | -0.849 | 0.3957 |  |
| Circulatory disease | +0.0129 | 0.0787 | ±0.1573 | +0.164 | 0.8699 |  |
| Avg. daily mean/SD | -0.0282 | 0.0212 | ±0.0425 | -1.330 | 0.1836 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.1693**, Adj R² = **0.1554**, F-statistic = **12.14** (p = **4.95e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.6**, BIC = **2357.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9923** | 0.3232 | ±0.6464 | **+9.258** | **2.09e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2240** | 0.0658 | ±0.1317 | **-3.402** | **6.68e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4423** | 0.1120 | ±0.2240 | **+3.949** | **7.86e-05** | *** |
| Site: UCSD (vs UAB) | +0.1225 | 0.0744 | ±0.1487 | +1.647 | 0.0996 | . |
| **Site: UW (vs UAB)** | **-0.3014** | 0.0822 | ±0.1645 | **-3.665** | **2.47e-04** | *** |
| Season: spring (vs autumn) | -0.1712 | 0.0888 | ±0.1776 | -1.927 | 0.0539 | . |
| Season: summer (vs autumn) | +0.0500 | 0.0887 | ±0.1774 | +0.564 | 0.5729 |  |
| Season: winter (vs autumn) | +0.0052 | 0.0956 | ±0.1912 | +0.054 | 0.9566 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.728** | **1.72e-11** | *** |
| BMI (kg/m2) | +0.0074 | 0.0051 | ±0.0102 | +1.450 | 0.1471 |  |
| Hypertension | +0.1000 | 0.0660 | ±0.1320 | +1.515 | 0.1297 |  |
| High cholesterol | -0.0721 | 0.0670 | ±0.1340 | -1.076 | 0.2820 |  |
| Kidney disease | -0.0659 | 0.0842 | ±0.1684 | -0.782 | 0.4340 |  |
| Circulatory disease | +0.0136 | 0.0788 | ±0.1577 | +0.172 | 0.8632 |  |
| MAG (mg/dL/h) | +0.0040 | 0.0033 | ±0.0066 | +1.203 | 0.2290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.1697**, Adj R² = **0.1557**, F-statistic = **12.17** (p = **4.16e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.2**, BIC = **2357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0460** | 0.3152 | ±0.6305 | **+9.662** | **4.36e-22** | *** |
| **Education: graduate level (vs college)** | **-0.2229** | 0.0661 | ±0.1323 | **-3.370** | **7.50e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4364** | 0.1131 | ±0.2262 | **+3.858** | **1.14e-04** | *** |
| Site: UCSD (vs UAB) | +0.1258 | 0.0742 | ±0.1485 | +1.694 | 0.0902 | . |
| **Site: UW (vs UAB)** | **-0.3059** | 0.0820 | ±0.1640 | **-3.731** | **1.91e-04** | *** |
| Season: spring (vs autumn) | -0.1738 | 0.0888 | ±0.1776 | -1.957 | 0.0503 | . |
| Season: summer (vs autumn) | +0.0470 | 0.0893 | ±0.1786 | +0.527 | 0.5983 |  |
| Season: winter (vs autumn) | +0.0010 | 0.0956 | ±0.1912 | +0.010 | 0.9916 |  |
| **Age (years)** | **-0.0215** | 0.0032 | ±0.0063 | **-6.796** | **1.08e-11** | *** |
| BMI (kg/m2) | +0.0078 | 0.0051 | ±0.0102 | +1.516 | 0.1296 |  |
| Hypertension | +0.1014 | 0.0660 | ±0.1320 | +1.536 | 0.1245 |  |
| High cholesterol | -0.0712 | 0.0670 | ±0.1341 | -1.063 | 0.2879 |  |
| Kidney disease | -0.0765 | 0.0823 | ±0.1645 | -0.930 | 0.3526 |  |
| Circulatory disease | +0.0114 | 0.0787 | ±0.1575 | +0.145 | 0.8845 |  |
| Avg. daily range (mg/dL) | +0.0010 | 0.0008 | ±0.0015 | +1.353 | 0.1762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.1797**, Adj R² = **0.1660**, F-statistic = **13.05** (p = **3.63e-28**), Residual SE = **0.916** on **834** df, AIC = **2275.9**, BIC = **2347.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0450** | 0.3004 | ±0.6009 | **+10.135** | **3.86e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2060** | 0.0656 | ±0.1312 | **-3.141** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **+0.4318** | 0.1106 | ±0.2213 | **+3.903** | **9.50e-05** | *** |
| Site: UCSD (vs UAB) | +0.1331 | 0.0742 | ±0.1484 | +1.795 | 0.0727 | . |
| **Site: UW (vs UAB)** | **-0.2935** | 0.0811 | ±0.1621 | **-3.620** | **2.94e-04** | *** |
| Season: spring (vs autumn) | -0.1703 | 0.0885 | ±0.1769 | -1.925 | 0.0542 | . |
| Season: summer (vs autumn) | +0.0435 | 0.0888 | ±0.1777 | +0.490 | 0.6240 |  |
| Season: winter (vs autumn) | -0.0091 | 0.0947 | ±0.1895 | -0.096 | 0.9236 |  |
| **Age (years)** | **-0.0212** | 0.0031 | ±0.0062 | **-6.812** | **9.65e-12** | *** |
| BMI (kg/m2) | +0.0065 | 0.0051 | ±0.0102 | +1.279 | 0.2008 |  |
| Hypertension | +0.0945 | 0.0660 | ±0.1320 | +1.432 | 0.1521 |  |
| High cholesterol | -0.0690 | 0.0667 | ±0.1334 | -1.034 | 0.3009 |  |
| Kidney disease | -0.0887 | 0.0815 | ±0.1629 | -1.089 | 0.2761 |  |
| Circulatory disease | -0.0064 | 0.0781 | ±0.1562 | -0.082 | 0.9349 |  |
| **SD of daily means (mg/dL)** | **+0.0137** | 0.0044 | ±0.0089 | **+3.084** | **0.0020** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.1731**, Adj R² = **0.1593**, F-statistic = **12.47** (p = **8.20e-27**), Residual SE = **0.920** on **834** df, AIC = **2282.7**, BIC = **2353.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4321** | 0.3454 | ±0.6907 | **+9.938** | **2.86e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2188** | 0.0658 | ±0.1316 | **-3.325** | **8.83e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4287** | 0.1109 | ±0.2218 | **+3.866** | **1.11e-04** | *** |
| Site: UCSD (vs UAB) | +0.1350 | 0.0741 | ±0.1482 | +1.821 | 0.0686 | . |
| **Site: UW (vs UAB)** | **-0.3050** | 0.0817 | ±0.1635 | **-3.732** | **1.90e-04** | *** |
| Season: spring (vs autumn) | -0.1735 | 0.0888 | ±0.1777 | -1.953 | 0.0508 | . |
| Season: summer (vs autumn) | +0.0497 | 0.0889 | ±0.1777 | +0.559 | 0.5764 |  |
| Season: winter (vs autumn) | -0.0044 | 0.0953 | ±0.1907 | -0.046 | 0.9633 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.880** | **5.99e-12** | *** |
| BMI (kg/m2) | +0.0070 | 0.0052 | ±0.0103 | +1.366 | 0.1720 |  |
| Hypertension | +0.1047 | 0.0660 | ±0.1321 | +1.585 | 0.1130 |  |
| High cholesterol | -0.0674 | 0.0672 | ±0.1344 | -1.003 | 0.3161 |  |
| Kidney disease | -0.0752 | 0.0829 | ±0.1658 | -0.907 | 0.3643 |  |
| Circulatory disease | +0.0095 | 0.0783 | ±0.1566 | +0.121 | 0.9033 |  |
| **Time in range 70-180, pooled (%)** | **-0.0029** | 0.0014 | ±0.0029 | **-2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.1731**, Adj R² = **0.1592**, F-statistic = **12.47** (p = **8.27e-27**), Residual SE = **0.920** on **834** df, AIC = **2282.7**, BIC = **2353.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4334** | 0.3459 | ±0.6918 | **+9.926** | **3.20e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2193** | 0.0658 | ±0.1316 | **-3.333** | **8.58e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4281** | 0.1108 | ±0.2217 | **+3.862** | **1.13e-04** | *** |
| Site: UCSD (vs UAB) | +0.1355 | 0.0741 | ±0.1481 | +1.829 | 0.0674 | . |
| **Site: UW (vs UAB)** | **-0.3051** | 0.0817 | ±0.1635 | **-3.732** | **1.90e-04** | *** |
| Season: spring (vs autumn) | -0.1740 | 0.0888 | ±0.1777 | -1.959 | 0.0501 | . |
| Season: summer (vs autumn) | +0.0488 | 0.0889 | ±0.1777 | +0.549 | 0.5833 |  |
| Season: winter (vs autumn) | -0.0054 | 0.0953 | ±0.1907 | -0.057 | 0.9546 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.883** | **5.88e-12** | *** |
| BMI (kg/m2) | +0.0070 | 0.0052 | ±0.0103 | +1.362 | 0.1731 |  |
| Hypertension | +0.1048 | 0.0661 | ±0.1322 | +1.586 | 0.1127 |  |
| High cholesterol | -0.0676 | 0.0672 | ±0.1344 | -1.006 | 0.3146 |  |
| Kidney disease | -0.0758 | 0.0828 | ±0.1657 | -0.916 | 0.3598 |  |
| Circulatory disease | +0.0095 | 0.0783 | ±0.1566 | +0.121 | 0.9034 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0029** | 0.0014 | ±0.0029 | **-2.023** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.1714**, Adj R² = **0.1575**, F-statistic = **12.32** (p = **1.89e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.5**, BIC = **2355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1155** | 0.3054 | ±0.6109 | **+10.200** | **1.98e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2321** | 0.0655 | ±0.1310 | **-3.545** | **3.93e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4576** | 0.1128 | ±0.2256 | **+4.057** | **4.98e-05** | *** |
| Site: UCSD (vs UAB) | +0.1285 | 0.0746 | ±0.1492 | +1.723 | 0.0848 | . |
| **Site: UW (vs UAB)** | **-0.2997** | 0.0827 | ±0.1653 | **-3.626** | **2.88e-04** | *** |
| Season: spring (vs autumn) | -0.1701 | 0.0887 | ±0.1774 | -1.918 | 0.0551 | . |
| Season: summer (vs autumn) | +0.0479 | 0.0886 | ±0.1773 | +0.540 | 0.5893 |  |
| Season: winter (vs autumn) | +0.0144 | 0.0955 | ±0.1910 | +0.151 | 0.8798 |  |
| **Age (years)** | **-0.0206** | 0.0031 | ±0.0063 | **-6.565** | **5.22e-11** | *** |
| BMI (kg/m2) | +0.0070 | 0.0051 | ±0.0102 | +1.367 | 0.1716 |  |
| Hypertension | +0.0908 | 0.0658 | ±0.1317 | +1.379 | 0.1680 |  |
| High cholesterol | -0.0669 | 0.0670 | ±0.1341 | -0.999 | 0.3179 |  |
| Kidney disease | -0.0529 | 0.0832 | ±0.1665 | -0.635 | 0.5253 |  |
| Circulatory disease | +0.0049 | 0.0790 | ±0.1579 | +0.062 | 0.9509 |  |
| Any reading < 54 during wear (0/1) | +0.1365 | 0.0786 | ±0.1571 | +1.737 | 0.0824 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.1801**, Adj R² = **0.1664**, F-statistic = **13.09** (p = **3.00e-28**), Residual SE = **0.916** on **834** df, AIC = **2275.4**, BIC = **2346.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1318** | 0.3055 | ±0.6111 | **+10.250** | **1.19e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2246** | 0.0651 | ±0.1302 | **-3.449** | **5.64e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4675** | 0.1131 | ±0.2262 | **+4.133** | **3.57e-05** | *** |
| Site: UCSD (vs UAB) | +0.1453 | 0.0746 | ±0.1491 | +1.949 | 0.0513 | . |
| **Site: UW (vs UAB)** | **-0.2806** | 0.0823 | ±0.1647 | **-3.408** | **6.54e-04** | *** |
| Season: spring (vs autumn) | -0.1611 | 0.0890 | ±0.1780 | -1.810 | 0.0703 | . |
| Season: summer (vs autumn) | +0.0498 | 0.0876 | ±0.1752 | +0.568 | 0.5699 |  |
| Season: winter (vs autumn) | +0.0153 | 0.0954 | ±0.1907 | +0.161 | 0.8724 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0063 | **-6.650** | **2.93e-11** | *** |
| BMI (kg/m2) | +0.0069 | 0.0049 | ±0.0098 | +1.393 | 0.1637 |  |
| Hypertension | +0.0920 | 0.0667 | ±0.1334 | +1.380 | 0.1677 |  |
| High cholesterol | -0.0694 | 0.0666 | ±0.1333 | -1.041 | 0.2979 |  |
| Kidney disease | -0.0489 | 0.0822 | ±0.1645 | -0.595 | 0.5518 |  |
| Circulatory disease | -0.0064 | 0.0779 | ±0.1558 | -0.082 | 0.9347 |  |
| **Time < 54 (%)** | **+0.2665** | 0.0959 | ±0.1918 | **+2.779** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.1816**, Adj R² = **0.1679**, F-statistic = **13.22** (p = **1.48e-28**), Residual SE = **0.915** on **834** df, AIC = **2273.9**, BIC = **2345.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1496** | 0.3036 | ±0.6073 | **+10.373** | **3.31e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2213** | 0.0646 | ±0.1292 | **-3.427** | **6.11e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4647** | 0.1129 | ±0.2257 | **+4.118** | **3.83e-05** | *** |
| Site: UCSD (vs UAB) | +0.1411 | 0.0742 | ±0.1485 | +1.901 | 0.0573 | . |
| **Site: UW (vs UAB)** | **-0.2859** | 0.0818 | ±0.1636 | **-3.494** | **4.76e-04** | *** |
| Season: spring (vs autumn) | -0.1546 | 0.0887 | ±0.1774 | -1.743 | 0.0813 | . |
| Season: summer (vs autumn) | +0.0505 | 0.0879 | ±0.1759 | +0.574 | 0.5656 |  |
| Season: winter (vs autumn) | +0.0139 | 0.0957 | ±0.1913 | +0.145 | 0.8848 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0063 | **-6.773** | **1.26e-11** | *** |
| BMI (kg/m2) | +0.0071 | 0.0049 | ±0.0099 | +1.445 | 0.1485 |  |
| Hypertension | +0.0939 | 0.0664 | ±0.1327 | +1.415 | 0.1572 |  |
| High cholesterol | -0.0653 | 0.0667 | ±0.1333 | -0.980 | 0.3270 |  |
| Kidney disease | -0.0527 | 0.0818 | ±0.1636 | -0.644 | 0.5194 |  |
| Circulatory disease | -0.0051 | 0.0787 | ±0.1575 | -0.064 | 0.9488 |  |
| Avg. daily time < 54 (%) | +0.2695 | 0.1462 | ±0.2923 | +1.844 | 0.0652 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.1853**, Adj R² = **0.1716**, F-statistic = **13.55** (p = **2.59e-29**), Residual SE = **0.913** on **834** df, AIC = **2270.1**, BIC = **2341.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1442** | 0.3042 | ±0.6085 | **+10.335** | **4.88e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2176** | 0.0646 | ±0.1292 | **-3.367** | **7.59e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4498** | 0.1134 | ±0.2267 | **+3.968** | **7.26e-05** | *** |
| Site: UCSD (vs UAB) | +0.1420 | 0.0743 | ±0.1486 | +1.910 | 0.0561 | . |
| **Site: UW (vs UAB)** | **-0.2883** | 0.0820 | ±0.1641 | **-3.514** | **4.41e-04** | *** |
| Season: spring (vs autumn) | -0.1505 | 0.0888 | ±0.1776 | -1.696 | 0.0900 | . |
| Season: summer (vs autumn) | +0.0579 | 0.0874 | ±0.1747 | +0.663 | 0.5075 |  |
| Season: winter (vs autumn) | +0.0244 | 0.0952 | ±0.1903 | +0.257 | 0.7975 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.891** | **5.52e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0050 | ±0.0099 | +1.422 | 0.1549 |  |
| Hypertension | +0.0947 | 0.0662 | ±0.1325 | +1.429 | 0.1529 |  |
| High cholesterol | -0.0709 | 0.0664 | ±0.1328 | -1.068 | 0.2857 |  |
| Kidney disease | -0.0566 | 0.0828 | ±0.1655 | -0.684 | 0.4942 |  |
| Circulatory disease | +0.0025 | 0.0774 | ±0.1548 | +0.032 | 0.9745 |  |
| **Time 54-69, pooled (%)** | **+0.0898** | 0.0325 | ±0.0650 | **+2.762** | **0.0057** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.1858**, Adj R² = **0.1721**, F-statistic = **13.59** (p = **2.05e-29**), Residual SE = **0.913** on **834** df, AIC = **2269.6**, BIC = **2340.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1613** | 0.3040 | ±0.6079 | **+10.400** | **2.47e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2164** | 0.0644 | ±0.1289 | **-3.358** | **7.85e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4476** | 0.1135 | ±0.2271 | **+3.943** | **8.06e-05** | *** |
| Site: UCSD (vs UAB) | +0.1400 | 0.0743 | ±0.1486 | +1.884 | 0.0596 | . |
| **Site: UW (vs UAB)** | **-0.2889** | 0.0819 | ±0.1638 | **-3.528** | **4.18e-04** | *** |
| Season: spring (vs autumn) | -0.1514 | 0.0887 | ±0.1774 | -1.707 | 0.0879 | . |
| Season: summer (vs autumn) | +0.0563 | 0.0874 | ±0.1747 | +0.644 | 0.5195 |  |
| Season: winter (vs autumn) | +0.0227 | 0.0951 | ±0.1902 | +0.239 | 0.8114 |  |
| **Age (years)** | **-0.0218** | 0.0031 | ±0.0063 | **-6.955** | **3.54e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0050 | ±0.0099 | +1.421 | 0.1553 |  |
| Hypertension | +0.0947 | 0.0662 | ±0.1324 | +1.431 | 0.1524 |  |
| High cholesterol | -0.0698 | 0.0665 | ±0.1329 | -1.051 | 0.2933 |  |
| Kidney disease | -0.0548 | 0.0822 | ±0.1644 | -0.666 | 0.5053 |  |
| Circulatory disease | +0.0046 | 0.0774 | ±0.1549 | +0.060 | 0.9522 |  |
| **Avg. daily time 54-69 (%)** | **+0.0884** | 0.0326 | ±0.0651 | **+2.715** | **0.0066** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.1861**, Adj R² = **0.1724**, F-statistic = **13.62** (p = **1.74e-29**), Residual SE = **0.913** on **834** df, AIC = **2269.3**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1368** | 0.3039 | ±0.6079 | **+10.321** | **5.68e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2177** | 0.0646 | ±0.1293 | **-3.369** | **7.56e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4549** | 0.1134 | ±0.2268 | **+4.011** | **6.06e-05** | *** |
| **Site: UCSD (vs UAB)** | **+0.1461** | 0.0743 | ±0.1486 | **+1.966** | **0.0492** | * |
| **Site: UW (vs UAB)** | **-0.2829** | 0.0821 | ±0.1642 | **-3.446** | **5.68e-04** | *** |
| Season: spring (vs autumn) | -0.1508 | 0.0888 | ±0.1777 | -1.698 | 0.0896 | . |
| Season: summer (vs autumn) | +0.0574 | 0.0871 | ±0.1743 | +0.659 | 0.5101 |  |
| Season: winter (vs autumn) | +0.0244 | 0.0951 | ±0.1902 | +0.256 | 0.7979 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.849** | **7.46e-12** | *** |
| BMI (kg/m2) | +0.0069 | 0.0049 | ±0.0099 | +1.407 | 0.1593 |  |
| Hypertension | +0.0934 | 0.0663 | ±0.1327 | +1.409 | 0.1589 |  |
| High cholesterol | -0.0701 | 0.0663 | ±0.1327 | -1.056 | 0.2910 |  |
| Kidney disease | -0.0545 | 0.0824 | ±0.1648 | -0.661 | 0.5084 |  |
| Circulatory disease | -0.0015 | 0.0773 | ±0.1546 | -0.019 | 0.9848 |  |
| **Time < 70 (%)** | **+0.0760** | 0.0255 | ±0.0511 | **+2.977** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.1871**, Adj R² = **0.1734**, F-statistic = **13.71** (p = **1.10e-29**), Residual SE = **0.912** on **834** df, AIC = **2268.3**, BIC = **2339.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1563** | 0.3032 | ±0.6065 | **+10.408** | **2.28e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2157** | 0.0643 | ±0.1287 | **-3.352** | **8.02e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4522** | 0.1135 | ±0.2270 | **+3.984** | **6.78e-05** | *** |
| Site: UCSD (vs UAB) | +0.1434 | 0.0742 | ±0.1483 | +1.933 | 0.0532 | . |
| **Site: UW (vs UAB)** | **-0.2848** | 0.0817 | ±0.1635 | **-3.484** | **4.95e-04** | *** |
| Season: spring (vs autumn) | -0.1496 | 0.0887 | ±0.1774 | -1.686 | 0.0917 | . |
| Season: summer (vs autumn) | +0.0563 | 0.0872 | ±0.1743 | +0.646 | 0.5182 |  |
| Season: winter (vs autumn) | +0.0226 | 0.0951 | ±0.1901 | +0.238 | 0.8119 |  |
| **Age (years)** | **-0.0218** | 0.0031 | ±0.0063 | **-6.934** | **4.08e-12** | *** |
| BMI (kg/m2) | +0.0070 | 0.0049 | ±0.0099 | +1.422 | 0.1549 |  |
| Hypertension | +0.0940 | 0.0662 | ±0.1325 | +1.419 | 0.1558 |  |
| High cholesterol | -0.0680 | 0.0664 | ±0.1329 | -1.024 | 0.3058 |  |
| Kidney disease | -0.0540 | 0.0819 | ±0.1637 | -0.660 | 0.5092 |  |
| Circulatory disease | +0.0007 | 0.0774 | ±0.1548 | +0.010 | 0.9924 |  |
| **Avg. daily time < 70 (%)** | **+0.0757** | 0.0265 | ±0.0529 | **+2.861** | **0.0042** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.1722**, Adj R² = **0.1583**, F-statistic = **12.40** (p = **1.26e-26**), Residual SE = **0.921** on **834** df, AIC = **2283.6**, BIC = **2354.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5693** | 0.4058 | ±0.8116 | **+8.795** | **1.43e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2182** | 0.0663 | ±0.1326 | **-3.291** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **+0.4328** | 0.1105 | ±0.2210 | **+3.916** | **9.00e-05** | *** |
| Site: UCSD (vs UAB) | +0.1298 | 0.0744 | ±0.1488 | +1.746 | 0.0809 | . |
| **Site: UW (vs UAB)** | **-0.3000** | 0.0816 | ±0.1632 | **-3.675** | **2.38e-04** | *** |
| Season: spring (vs autumn) | -0.1689 | 0.0889 | ±0.1777 | -1.900 | 0.0574 | . |
| Season: summer (vs autumn) | +0.0580 | 0.0890 | ±0.1779 | +0.651 | 0.5147 |  |
| Season: winter (vs autumn) | +0.0030 | 0.0954 | ±0.1908 | +0.031 | 0.9752 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0062 | **-6.709** | **1.96e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.395 | 0.1630 |  |
| Hypertension | +0.0967 | 0.0662 | ±0.1324 | +1.461 | 0.1439 |  |
| High cholesterol | -0.0703 | 0.0672 | ±0.1343 | -1.046 | 0.2954 |  |
| Kidney disease | -0.0687 | 0.0837 | ±0.1674 | -0.821 | 0.4114 |  |
| Circulatory disease | +0.0105 | 0.0787 | ±0.1574 | +0.134 | 0.8937 |  |
| Time 54-250, pooled (%) | -0.0044 | 0.0027 | ±0.0055 | -1.591 | 0.1115 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.1723**, Adj R² = **0.1584**, F-statistic = **12.40** (p = **1.21e-26**), Residual SE = **0.920** on **834** df, AIC = **2283.5**, BIC = **2354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5824** | 0.4084 | ±0.8168 | **+8.772** | **1.75e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2182** | 0.0663 | ±0.1326 | **-3.292** | **9.95e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4327** | 0.1105 | ±0.2210 | **+3.916** | **9.02e-05** | *** |
| Site: UCSD (vs UAB) | +0.1301 | 0.0743 | ±0.1487 | +1.751 | 0.0800 | . |
| **Site: UW (vs UAB)** | **-0.3004** | 0.0816 | ±0.1632 | **-3.680** | **2.33e-04** | *** |
| Season: spring (vs autumn) | -0.1695 | 0.0889 | ±0.1778 | -1.908 | 0.0565 | . |
| Season: summer (vs autumn) | +0.0571 | 0.0889 | ±0.1779 | +0.642 | 0.5208 |  |
| Season: winter (vs autumn) | +0.0022 | 0.0954 | ±0.1908 | +0.023 | 0.9818 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.726** | **1.74e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.392 | 0.1640 |  |
| Hypertension | +0.0970 | 0.0662 | ±0.1324 | +1.466 | 0.1426 |  |
| High cholesterol | -0.0702 | 0.0671 | ±0.1343 | -1.045 | 0.2958 |  |
| Kidney disease | -0.0698 | 0.0836 | ±0.1673 | -0.834 | 0.4042 |  |
| Circulatory disease | +0.0100 | 0.0788 | ±0.1575 | +0.127 | 0.8992 |  |
| Avg. daily time 54-250 (%) | -0.0044 | 0.0028 | ±0.0055 | -1.614 | 0.1065 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.1695**, Adj R² = **0.1556**, F-statistic = **12.16** (p = **4.49e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.4**, BIC = **2357.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1695** | 0.3053 | ±0.6105 | **+10.383** | **2.96e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2285** | 0.0654 | ±0.1308 | **-3.496** | **4.73e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4407** | 0.1130 | ±0.2260 | **+3.900** | **9.61e-05** | *** |
| Site: UCSD (vs UAB) | +0.1253 | 0.0745 | ±0.1491 | +1.682 | 0.0926 | . |
| **Site: UW (vs UAB)** | **-0.3141** | 0.0823 | ±0.1646 | **-3.816** | **1.36e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1753** | 0.0888 | ±0.1776 | **-1.974** | **0.0484** | * |
| Season: summer (vs autumn) | +0.0404 | 0.0894 | ±0.1788 | +0.452 | 0.6514 |  |
| Season: winter (vs autumn) | -0.0028 | 0.0962 | ±0.1924 | -0.029 | 0.9766 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0064 | **-6.752** | **1.46e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0051 | ±0.0103 | +1.415 | 0.1572 |  |
| Hypertension | +0.1052 | 0.0656 | ±0.1312 | +1.603 | 0.1089 |  |
| High cholesterol | -0.0702 | 0.0671 | ±0.1341 | -1.046 | 0.2954 |  |
| Kidney disease | -0.0656 | 0.0827 | ±0.1653 | -0.793 | 0.4278 |  |
| Circulatory disease | +0.0118 | 0.0785 | ±0.1570 | +0.151 | 0.8802 |  |
| Time 181-250, pooled (%) | +0.0027 | 0.0021 | ±0.0043 | +1.242 | 0.2144 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.1695**, Adj R² = **0.1555**, F-statistic = **12.15** (p = **4.62e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.4**, BIC = **2357.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1689** | 0.3053 | ±0.6105 | **+10.381** | **3.01e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2288** | 0.0654 | ±0.1308 | **-3.500** | **4.65e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4402** | 0.1129 | ±0.2259 | **+3.898** | **9.71e-05** | *** |
| Site: UCSD (vs UAB) | +0.1257 | 0.0745 | ±0.1490 | +1.687 | 0.0917 | . |
| **Site: UW (vs UAB)** | **-0.3137** | 0.0823 | ±0.1646 | **-3.811** | **1.38e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1752** | 0.0888 | ±0.1776 | **-1.972** | **0.0486** | * |
| Season: summer (vs autumn) | +0.0404 | 0.0894 | ±0.1788 | +0.452 | 0.6511 |  |
| Season: winter (vs autumn) | -0.0031 | 0.0962 | ±0.1924 | -0.032 | 0.9745 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0064 | **-6.749** | **1.49e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0051 | ±0.0103 | +1.413 | 0.1575 |  |
| Hypertension | +0.1049 | 0.0657 | ±0.1314 | +1.597 | 0.1104 |  |
| High cholesterol | -0.0705 | 0.0671 | ±0.1341 | -1.051 | 0.2934 |  |
| Kidney disease | -0.0655 | 0.0826 | ±0.1653 | -0.793 | 0.4280 |  |
| Circulatory disease | +0.0121 | 0.0785 | ±0.1570 | +0.154 | 0.8778 |  |
| Avg. daily time 181-250 (%) | +0.0026 | 0.0021 | ±0.0042 | +1.224 | 0.2208 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.1718**, Adj R² = **0.1579**, F-statistic = **12.35** (p = **1.58e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.1**, BIC = **2355.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1473** | 0.3044 | ±0.6089 | **+10.338** | **4.72e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2212** | 0.0659 | ±0.1318 | **-3.357** | **7.87e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4317** | 0.1110 | ±0.2221 | **+3.888** | **1.01e-04** | *** |
| Site: UCSD (vs UAB) | +0.1314 | 0.0743 | ±0.1486 | +1.769 | 0.0769 | . |
| **Site: UW (vs UAB)** | **-0.3071** | 0.0819 | ±0.1637 | **-3.752** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.1738 | 0.0889 | ±0.1777 | -1.956 | 0.0505 | . |
| Season: summer (vs autumn) | +0.0484 | 0.0890 | ±0.1780 | +0.544 | 0.5866 |  |
| Season: winter (vs autumn) | -0.0036 | 0.0955 | ±0.1910 | -0.037 | 0.9702 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.843** | **7.74e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0052 | ±0.0103 | +1.382 | 0.1670 |  |
| Hypertension | +0.1039 | 0.0660 | ±0.1320 | +1.574 | 0.1156 |  |
| High cholesterol | -0.0685 | 0.0672 | ±0.1344 | -1.019 | 0.3082 |  |
| Kidney disease | -0.0723 | 0.0830 | ±0.1660 | -0.871 | 0.3838 |  |
| Circulatory disease | +0.0106 | 0.0785 | ±0.1570 | +0.135 | 0.8930 |  |
| Time > 180 (%) | +0.0025 | 0.0014 | ±0.0029 | +1.716 | 0.0861 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.1717**, Adj R² = **0.1578**, F-statistic = **12.35** (p = **1.63e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.2**, BIC = **2355.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1497** | 0.3046 | ±0.6091 | **+10.342** | **4.56e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2217** | 0.0659 | ±0.1317 | **-3.366** | **7.63e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4313** | 0.1110 | ±0.2220 | **+3.886** | **1.02e-04** | *** |
| Site: UCSD (vs UAB) | +0.1319 | 0.0743 | ±0.1485 | +1.776 | 0.0758 | . |
| **Site: UW (vs UAB)** | **-0.3071** | 0.0819 | ±0.1637 | **-3.752** | **1.76e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1743** | 0.0889 | ±0.1778 | **-1.960** | **0.0499** | * |
| Season: summer (vs autumn) | +0.0476 | 0.0890 | ±0.1780 | +0.535 | 0.5924 |  |
| Season: winter (vs autumn) | -0.0043 | 0.0955 | ±0.1911 | -0.045 | 0.9637 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.842** | **7.80e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0052 | ±0.0103 | +1.379 | 0.1679 |  |
| Hypertension | +0.1039 | 0.0660 | ±0.1321 | +1.574 | 0.1155 |  |
| High cholesterol | -0.0687 | 0.0672 | ±0.1344 | -1.023 | 0.3063 |  |
| Kidney disease | -0.0727 | 0.0830 | ±0.1659 | -0.877 | 0.3805 |  |
| Circulatory disease | +0.0105 | 0.0785 | ±0.1570 | +0.134 | 0.8936 |  |
| Avg. daily time > 180 (%) | +0.0024 | 0.0014 | ±0.0029 | +1.703 | 0.0886 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.1729**, Adj R² = **0.1590**, F-statistic = **12.45** (p = **9.37e-27**), Residual SE = **0.920** on **834** df, AIC = **2283.0**, BIC = **2354.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1493** | 0.3041 | ±0.6082 | **+10.356** | **3.94e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2171** | 0.0661 | ±0.1321 | **-3.286** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **+0.4306** | 0.1108 | ±0.2216 | **+3.887** | **1.02e-04** | *** |
| Site: UCSD (vs UAB) | +0.1348 | 0.0743 | ±0.1486 | +1.814 | 0.0697 | . |
| **Site: UW (vs UAB)** | **-0.3080** | 0.0818 | ±0.1637 | **-3.764** | **1.67e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1752** | 0.0888 | ±0.1776 | **-1.972** | **0.0486** | * |
| Season: summer (vs autumn) | +0.0497 | 0.0887 | ±0.1775 | +0.560 | 0.5753 |  |
| Season: winter (vs autumn) | -0.0054 | 0.0955 | ±0.1910 | -0.056 | 0.9552 |  |
| **Age (years)** | **-0.0212** | 0.0031 | ±0.0062 | **-6.801** | **1.04e-11** | *** |
| BMI (kg/m2) | +0.0066 | 0.0052 | ±0.0104 | +1.270 | 0.2042 |  |
| Hypertension | +0.1053 | 0.0661 | ±0.1322 | +1.592 | 0.1114 |  |
| High cholesterol | -0.0674 | 0.0671 | ±0.1342 | -1.005 | 0.3151 |  |
| Kidney disease | -0.0714 | 0.0828 | ±0.1656 | -0.863 | 0.3882 |  |
| Circulatory disease | +0.0095 | 0.0786 | ±0.1571 | +0.121 | 0.9040 |  |
| Nocturnal time > 180 (%) | +0.0027 | 0.0014 | ±0.0027 | +1.951 | 0.0511 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.1680**, Adj R² = **0.1540**, F-statistic = **12.03** (p = **9.22e-26**), Residual SE = **0.923** on **834** df, AIC = **2288.0**, BIC = **2359.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1682** | 0.3063 | ±0.6126 | **+10.344** | **4.46e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2296** | 0.0661 | ±0.1323 | **-3.472** | **5.17e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4484** | 0.1131 | ±0.2261 | **+3.965** | **7.33e-05** | *** |
| Site: UCSD (vs UAB) | +0.1188 | 0.0746 | ±0.1493 | +1.592 | 0.1114 |  |
| **Site: UW (vs UAB)** | **-0.3132** | 0.0824 | ±0.1649 | **-3.800** | **1.45e-04** | *** |
| Season: spring (vs autumn) | -0.1708 | 0.0887 | ±0.1774 | -1.926 | 0.0541 | . |
| Season: summer (vs autumn) | +0.0441 | 0.0893 | ±0.1786 | +0.494 | 0.6212 |  |
| Season: winter (vs autumn) | +0.0049 | 0.0958 | ±0.1916 | +0.051 | 0.9592 |  |
| **Age (years)** | **-0.0212** | 0.0032 | ±0.0065 | **-6.576** | **4.83e-11** | *** |
| BMI (kg/m2) | +0.0075 | 0.0051 | ±0.0102 | +1.472 | 0.1409 |  |
| Hypertension | +0.0994 | 0.0659 | ±0.1317 | +1.508 | 0.1315 |  |
| High cholesterol | -0.0735 | 0.0670 | ±0.1340 | -1.097 | 0.2727 |  |
| Kidney disease | -0.0581 | 0.0832 | ±0.1664 | -0.699 | 0.4846 |  |
| Circulatory disease | +0.0136 | 0.0788 | ±0.1576 | +0.173 | 0.8629 |  |
| Any reading > 250 during wear (0/1) | +0.0204 | 0.0694 | ±0.1388 | +0.294 | 0.7685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.1718**, Adj R² = **0.1579**, F-statistic = **12.36** (p = **1.52e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.0**, BIC = **2355.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1364** | 0.3077 | ±0.6153 | **+10.194** | **2.11e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2189** | 0.0663 | ±0.1327 | **-3.300** | **9.66e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4333** | 0.1105 | ±0.2209 | **+3.922** | **8.78e-05** | *** |
| Site: UCSD (vs UAB) | +0.1288 | 0.0744 | ±0.1489 | +1.731 | 0.0835 | . |
| **Site: UW (vs UAB)** | **-0.3011** | 0.0817 | ±0.1633 | **-3.687** | **2.27e-04** | *** |
| Season: spring (vs autumn) | -0.1691 | 0.0889 | ±0.1777 | -1.903 | 0.0570 | . |
| Season: summer (vs autumn) | +0.0572 | 0.0890 | ±0.1780 | +0.643 | 0.5203 |  |
| Season: winter (vs autumn) | +0.0029 | 0.0955 | ±0.1909 | +0.030 | 0.9757 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0062 | **-6.712** | **1.93e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.399 | 0.1618 |  |
| Hypertension | +0.0969 | 0.0662 | ±0.1323 | +1.464 | 0.1432 |  |
| High cholesterol | -0.0705 | 0.0672 | ±0.1343 | -1.050 | 0.2938 |  |
| Kidney disease | -0.0682 | 0.0837 | ±0.1674 | -0.815 | 0.4151 |  |
| Circulatory disease | +0.0110 | 0.0788 | ±0.1575 | +0.139 | 0.8894 |  |
| Time > 250 (%) | +0.0041 | 0.0027 | ±0.0055 | +1.513 | 0.1302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.1719**, Adj R² = **0.1580**, F-statistic = **12.36** (p = **1.49e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.0**, BIC = **2355.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1404** | 0.3077 | ±0.6154 | **+10.206** | **1.87e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2190** | 0.0663 | ±0.1326 | **-3.303** | **9.57e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4333** | 0.1105 | ±0.2210 | **+3.922** | **8.78e-05** | *** |
| Site: UCSD (vs UAB) | +0.1291 | 0.0744 | ±0.1488 | +1.736 | 0.0826 | . |
| **Site: UW (vs UAB)** | **-0.3014** | 0.0817 | ±0.1633 | **-3.691** | **2.23e-04** | *** |
| Season: spring (vs autumn) | -0.1699 | 0.0889 | ±0.1778 | -1.911 | 0.0560 | . |
| Season: summer (vs autumn) | +0.0563 | 0.0889 | ±0.1779 | +0.633 | 0.5265 |  |
| Season: winter (vs autumn) | +0.0022 | 0.0954 | ±0.1909 | +0.023 | 0.9817 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.726** | **1.75e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.396 | 0.1628 |  |
| Hypertension | +0.0972 | 0.0662 | ±0.1323 | +1.468 | 0.1420 |  |
| High cholesterol | -0.0705 | 0.0671 | ±0.1343 | -1.050 | 0.2936 |  |
| Kidney disease | -0.0691 | 0.0837 | ±0.1674 | -0.826 | 0.4090 |  |
| Circulatory disease | +0.0104 | 0.0788 | ±0.1576 | +0.132 | 0.8946 |  |
| Avg. daily time > 250 (%) | +0.0042 | 0.0028 | ±0.0055 | +1.528 | 0.1266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.2625**, Adj R² = **0.2510**, F-statistic = **22.86** (p = **3.79e-47**), Residual SE = **2.114** on **835** df, AIC = **3694.1**, BIC = **3760.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1179** | 0.6462 | ±1.2923 | **+37.324** | **6.59e-305** | *** |
| Education: graduate level (vs college) | -0.0720 | 0.1621 | ±0.3243 | -0.444 | 0.6571 |  |
| Education: high school or below (vs college) | +0.2181 | 0.2229 | ±0.4457 | +0.979 | 0.3278 |  |
| Site: UCSD (vs UAB) | -0.1349 | 0.1780 | ±0.3559 | -0.758 | 0.4485 |  |
| **Site: UW (vs UAB)** | **-1.3869** | 0.1836 | ±0.3672 | **-7.555** | **4.20e-14** | *** |
| Season: spring (vs autumn) | -0.2256 | 0.1965 | ±0.3929 | -1.148 | 0.2509 |  |
| **Season: summer (vs autumn)** | **+1.7911** | 0.2210 | ±0.4419 | **+8.106** | **5.24e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2022** | 0.2132 | ±0.4264 | **-5.639** | **1.71e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.263 | 0.2065 |  |
| BMI (kg/m2) | +0.0134 | 0.0106 | ±0.0211 | +1.269 | 0.2043 |  |
| Hypertension | +0.3099 | 0.1596 | ±0.3192 | +1.942 | 0.0521 | . |
| High cholesterol | -0.1579 | 0.1570 | ±0.3140 | -1.006 | 0.3146 |  |
| Kidney disease | -0.1452 | 0.1912 | ±0.3824 | -0.760 | 0.4475 |  |
| Circulatory disease | +0.2291 | 0.1913 | ±0.3826 | +1.197 | 0.2311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.2628**, Adj R² = **0.2504**, F-statistic = **21.24** (p = **1.60e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.8**, BIC = **3766.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3107** | 0.7821 | ±1.5643 | **+31.082** | **4.17e-212** | *** |
| Education: graduate level (vs college) | -0.0797 | 0.1644 | ±0.3289 | -0.485 | 0.6278 |  |
| Education: high school or below (vs college) | +0.2309 | 0.2239 | ±0.4478 | +1.031 | 0.3023 |  |
| Site: UCSD (vs UAB) | -0.1403 | 0.1796 | ±0.3592 | -0.781 | 0.4346 |  |
| **Site: UW (vs UAB)** | **-1.3915** | 0.1842 | ±0.3684 | **-7.554** | **4.22e-14** | *** |
| Season: spring (vs autumn) | -0.2288 | 0.1973 | ±0.3947 | -1.159 | 0.2464 |  |
| **Season: summer (vs autumn)** | **+1.7868** | 0.2223 | ±0.4445 | **+8.039** | **9.08e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2001** | 0.2139 | ±0.4277 | **-5.611** | **2.01e-08** | *** |
| Age (years) | +0.0096 | 0.0075 | ±0.0150 | +1.280 | 0.2006 |  |
| BMI (kg/m2) | +0.0139 | 0.0108 | ±0.0215 | +1.291 | 0.1968 |  |
| Hypertension | +0.3102 | 0.1600 | ±0.3199 | +1.940 | 0.0524 | . |
| High cholesterol | -0.1580 | 0.1573 | ±0.3147 | -1.004 | 0.3153 |  |
| Kidney disease | -0.1430 | 0.1915 | ±0.3830 | -0.746 | 0.4554 |  |
| Circulatory disease | +0.2306 | 0.1918 | ±0.3836 | +1.202 | 0.2293 |  |
| HbA1c (%) | -0.0319 | 0.0744 | ±0.1489 | -0.428 | 0.6684 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.2633**, Adj R² = **0.2509**, F-statistic = **21.29** (p = **1.23e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.2**, BIC = **3766.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3492** | 0.7002 | ±1.4003 | **+34.776** | **5.58e-265** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.1629 | ±0.3257 | -0.511 | 0.6093 |  |
| Education: high school or below (vs college) | +0.2356 | 0.2243 | ±0.4485 | +1.051 | 0.2934 |  |
| Site: UCSD (vs UAB) | -0.1464 | 0.1794 | ±0.3588 | -0.816 | 0.4146 |  |
| **Site: UW (vs UAB)** | **-1.3921** | 0.1846 | ±0.3692 | **-7.540** | **4.69e-14** | *** |
| Season: spring (vs autumn) | -0.2219 | 0.1963 | ±0.3925 | -1.131 | 0.2581 |  |
| **Season: summer (vs autumn)** | **+1.7865** | 0.2216 | ±0.4431 | **+8.063** | **7.45e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1932** | 0.2143 | ±0.4286 | **-5.568** | **2.58e-08** | *** |
| Age (years) | +0.0098 | 0.0075 | ±0.0150 | +1.302 | 0.1928 |  |
| BMI (kg/m2) | +0.0137 | 0.0106 | ±0.0213 | +1.290 | 0.1971 |  |
| Hypertension | +0.3070 | 0.1604 | ±0.3208 | +1.914 | 0.0556 | . |
| High cholesterol | -0.1618 | 0.1575 | ±0.3150 | -1.027 | 0.3044 |  |
| Kidney disease | -0.1299 | 0.1908 | ±0.3817 | -0.681 | 0.4960 |  |
| Circulatory disease | +0.2310 | 0.1916 | ±0.3832 | +1.206 | 0.2279 |  |
| Mean glucose (mg/dL) | -0.0017 | 0.0019 | ±0.0039 | -0.860 | 0.3900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.2633**, Adj R² = **0.2509**, F-statistic = **21.29** (p = **1.23e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.2**, BIC = **3766.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5796** | 0.8390 | ±1.6779 | **+29.298** | **1.10e-188** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.1629 | ±0.3257 | -0.511 | 0.6093 |  |
| Education: high school or below (vs college) | +0.2356 | 0.2243 | ±0.4485 | +1.051 | 0.2934 |  |
| Site: UCSD (vs UAB) | -0.1464 | 0.1794 | ±0.3588 | -0.816 | 0.4146 |  |
| **Site: UW (vs UAB)** | **-1.3921** | 0.1846 | ±0.3692 | **-7.540** | **4.69e-14** | *** |
| Season: spring (vs autumn) | -0.2219 | 0.1963 | ±0.3925 | -1.131 | 0.2581 |  |
| **Season: summer (vs autumn)** | **+1.7865** | 0.2216 | ±0.4431 | **+8.063** | **7.45e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1932** | 0.2143 | ±0.4286 | **-5.568** | **2.58e-08** | *** |
| Age (years) | +0.0098 | 0.0075 | ±0.0150 | +1.302 | 0.1928 |  |
| BMI (kg/m2) | +0.0137 | 0.0106 | ±0.0213 | +1.290 | 0.1971 |  |
| Hypertension | +0.3070 | 0.1604 | ±0.3208 | +1.914 | 0.0556 | . |
| High cholesterol | -0.1618 | 0.1575 | ±0.3150 | -1.027 | 0.3044 |  |
| Kidney disease | -0.1299 | 0.1908 | ±0.3817 | -0.681 | 0.4960 |  |
| Circulatory disease | +0.2310 | 0.1916 | ±0.3832 | +1.206 | 0.2279 |  |
| GMI (%) | -0.0696 | 0.0810 | ±0.1620 | -0.860 | 0.3900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2507**, F-statistic = **21.27** (p = **1.36e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3150** | 0.6946 | ±1.3891 | **+35.007** | **1.74e-268** | *** |
| Education: graduate level (vs college) | -0.0816 | 0.1630 | ±0.3259 | -0.501 | 0.6164 |  |
| Education: high school or below (vs college) | +0.2326 | 0.2242 | ±0.4484 | +1.038 | 0.2994 |  |
| Site: UCSD (vs UAB) | -0.1444 | 0.1793 | ±0.3586 | -0.805 | 0.4207 |  |
| **Site: UW (vs UAB)** | **-1.3880** | 0.1841 | ±0.3683 | **-7.538** | **4.79e-14** | *** |
| Season: spring (vs autumn) | -0.2206 | 0.1964 | ±0.3928 | -1.123 | 0.2613 |  |
| **Season: summer (vs autumn)** | **+1.7877** | 0.2215 | ±0.4430 | **+8.070** | **7.00e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1935** | 0.2143 | ±0.4286 | **-5.569** | **2.56e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.259 | 0.2080 |  |
| BMI (kg/m2) | +0.0140 | 0.0107 | ±0.0215 | +1.308 | 0.1910 |  |
| Hypertension | +0.3063 | 0.1606 | ±0.3211 | +1.908 | 0.0564 | . |
| High cholesterol | -0.1603 | 0.1574 | ±0.3149 | -1.018 | 0.3087 |  |
| Kidney disease | -0.1367 | 0.1907 | ±0.3814 | -0.717 | 0.4736 |  |
| Circulatory disease | +0.2306 | 0.1917 | ±0.3833 | +1.203 | 0.2289 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0014 | 0.0019 | ±0.0038 | -0.742 | 0.4581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2507**, F-statistic = **21.27** (p = **1.36e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2337** | 0.6721 | ±1.3441 | **+36.059** | **1.01e-284** | *** |
| Education: graduate level (vs college) | -0.0838 | 0.1632 | ±0.3264 | -0.514 | 0.6076 |  |
| Education: high school or below (vs college) | +0.2357 | 0.2245 | ±0.4490 | +1.050 | 0.2937 |  |
| Site: UCSD (vs UAB) | -0.1454 | 0.1795 | ±0.3589 | -0.810 | 0.4178 |  |
| **Site: UW (vs UAB)** | **-1.3974** | 0.1850 | ±0.3700 | **-7.554** | **4.24e-14** | *** |
| Season: spring (vs autumn) | -0.2234 | 0.1962 | ±0.3924 | -1.138 | 0.2550 |  |
| **Season: summer (vs autumn)** | **+1.7854** | 0.2220 | ±0.4439 | **+8.044** | **8.69e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1962** | 0.2136 | ±0.4272 | **-5.600** | **2.14e-08** | *** |
| Age (years) | +0.0101 | 0.0075 | ±0.0151 | +1.336 | 0.1814 |  |
| BMI (kg/m2) | +0.0134 | 0.0106 | ±0.0213 | +1.265 | 0.2057 |  |
| Hypertension | +0.3090 | 0.1600 | ±0.3200 | +1.931 | 0.0535 | . |
| High cholesterol | -0.1632 | 0.1577 | ±0.3154 | -1.035 | 0.3006 |  |
| Kidney disease | -0.1167 | 0.1941 | ±0.3881 | -0.601 | 0.5475 |  |
| Circulatory disease | +0.2321 | 0.1918 | ±0.3835 | +1.210 | 0.2262 |  |
| Glucose SD, pooled (mg/dL) | -0.0044 | 0.0059 | ±0.0118 | -0.740 | 0.4593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2634**, Adj R² = **0.2510**, F-statistic = **21.30** (p = **1.15e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.1**, BIC = **3766.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2726** | 0.6759 | ±1.3519 | **+35.910** | **2.16e-282** | *** |
| Education: graduate level (vs college) | -0.0857 | 0.1633 | ±0.3265 | -0.525 | 0.5997 |  |
| Education: high school or below (vs college) | +0.2420 | 0.2243 | ±0.4486 | +1.079 | 0.2808 |  |
| Site: UCSD (vs UAB) | -0.1473 | 0.1791 | ±0.3582 | -0.822 | 0.4108 |  |
| **Site: UW (vs UAB)** | **-1.3985** | 0.1845 | ±0.3691 | **-7.579** | **3.49e-14** | *** |
| Season: spring (vs autumn) | -0.2224 | 0.1962 | ±0.3924 | -1.134 | 0.2569 |  |
| **Season: summer (vs autumn)** | **+1.7825** | 0.2221 | ±0.4441 | **+8.027** | **1.00e-15** | *** |
| **Season: winter (vs autumn)** | **-1.1963** | 0.2134 | ±0.4269 | **-5.605** | **2.08e-08** | *** |
| Age (years) | +0.0103 | 0.0076 | ±0.0151 | +1.367 | 0.1717 |  |
| BMI (kg/m2) | +0.0131 | 0.0106 | ±0.0213 | +1.234 | 0.2172 |  |
| Hypertension | +0.3081 | 0.1600 | ±0.3199 | +1.926 | 0.0541 | . |
| High cholesterol | -0.1645 | 0.1576 | ±0.3153 | -1.043 | 0.2967 |  |
| Kidney disease | -0.1086 | 0.1938 | ±0.3876 | -0.561 | 0.5751 |  |
| Circulatory disease | +0.2309 | 0.1917 | ±0.3834 | +1.205 | 0.2283 |  |
| Avg. daily SD (mg/dL) | -0.0062 | 0.0065 | ±0.0131 | -0.950 | 0.3422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.2625**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.83e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.1**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1540** | 0.7012 | ±1.4025 | **+34.444** | **5.47e-260** | *** |
| Education: graduate level (vs college) | -0.0736 | 0.1626 | ±0.3252 | -0.453 | 0.6506 |  |
| Education: high school or below (vs college) | +0.2207 | 0.2241 | ±0.4481 | +0.985 | 0.3246 |  |
| Site: UCSD (vs UAB) | -0.1364 | 0.1786 | ±0.3571 | -0.764 | 0.4449 |  |
| **Site: UW (vs UAB)** | **-1.3892** | 0.1843 | ±0.3686 | **-7.537** | **4.80e-14** | *** |
| Season: spring (vs autumn) | -0.2258 | 0.1967 | ±0.3935 | -1.148 | 0.2511 |  |
| **Season: summer (vs autumn)** | **+1.7905** | 0.2216 | ±0.4432 | **+8.080** | **6.49e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2019** | 0.2134 | ±0.4268 | **-5.632** | **1.78e-08** | *** |
| Age (years) | +0.0096 | 0.0075 | ±0.0151 | +1.275 | 0.2022 |  |
| BMI (kg/m2) | +0.0134 | 0.0106 | ±0.0212 | +1.261 | 0.2072 |  |
| Hypertension | +0.3103 | 0.1600 | ±0.3200 | +1.939 | 0.0525 | . |
| High cholesterol | -0.1588 | 0.1575 | ±0.3150 | -1.008 | 0.3133 |  |
| Kidney disease | -0.1396 | 0.1954 | ±0.3908 | -0.715 | 0.4749 |  |
| Circulatory disease | +0.2297 | 0.1913 | ±0.3827 | +1.201 | 0.2299 |  |
| CV (%) | -0.0020 | 0.0129 | ±0.0259 | -0.152 | 0.8794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.80e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2018** | 0.7162 | ±1.4325 | **+33.791** | **2.70e-250** | *** |
| Education: graduate level (vs college) | -0.0694 | 0.1626 | ±0.3252 | -0.427 | 0.6697 |  |
| Education: high school or below (vs college) | +0.2134 | 0.2241 | ±0.4482 | +0.952 | 0.3409 |  |
| Site: UCSD (vs UAB) | -0.1330 | 0.1783 | ±0.3566 | -0.746 | 0.4558 |  |
| **Site: UW (vs UAB)** | **-1.3835** | 0.1840 | ±0.3679 | **-7.520** | **5.46e-14** | *** |
| Season: spring (vs autumn) | -0.2257 | 0.1968 | ±0.3936 | -1.147 | 0.2514 |  |
| **Season: summer (vs autumn)** | **+1.7910** | 0.2213 | ±0.4426 | **+8.093** | **5.82e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2033** | 0.2134 | ±0.4268 | **-5.639** | **1.71e-08** | *** |
| Age (years) | +0.0092 | 0.0075 | ±0.0150 | +1.221 | 0.2221 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.271 | 0.2036 |  |
| Hypertension | +0.3093 | 0.1600 | ±0.3199 | +1.934 | 0.0532 | . |
| High cholesterol | -0.1567 | 0.1574 | ±0.3148 | -0.996 | 0.3195 |  |
| Kidney disease | -0.1524 | 0.1945 | ±0.3891 | -0.784 | 0.4333 |  |
| Circulatory disease | +0.2275 | 0.1912 | ±0.3824 | +1.190 | 0.2340 |  |
| Mean / SD ratio | -0.0144 | 0.0627 | ±0.1254 | -0.229 | 0.8189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2625**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.85e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.1**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0946** | 0.7092 | ±1.4184 | **+33.974** | **5.32e-253** | *** |
| Education: graduate level (vs college) | -0.0728 | 0.1632 | ±0.3264 | -0.446 | 0.6555 |  |
| Education: high school or below (vs college) | +0.2194 | 0.2237 | ±0.4474 | +0.981 | 0.3267 |  |
| Site: UCSD (vs UAB) | -0.1351 | 0.1782 | ±0.3564 | -0.758 | 0.4484 |  |
| **Site: UW (vs UAB)** | **-1.3877** | 0.1833 | ±0.3666 | **-7.570** | **3.74e-14** | *** |
| Season: spring (vs autumn) | -0.2257 | 0.1971 | ±0.3942 | -1.145 | 0.2520 |  |
| **Season: summer (vs autumn)** | **+1.7909** | 0.2217 | ±0.4434 | **+8.078** | **6.60e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2022** | 0.2135 | ±0.4270 | **-5.631** | **1.79e-08** | *** |
| Age (years) | +0.0095 | 0.0075 | ±0.0151 | +1.266 | 0.2056 |  |
| BMI (kg/m2) | +0.0134 | 0.0107 | ±0.0213 | +1.254 | 0.2097 |  |
| Hypertension | +0.3101 | 0.1601 | ±0.3202 | +1.937 | 0.0527 | . |
| High cholesterol | -0.1582 | 0.1574 | ±0.3149 | -1.005 | 0.3148 |  |
| Kidney disease | -0.1434 | 0.1939 | ±0.3879 | -0.740 | 0.4596 |  |
| Circulatory disease | +0.2291 | 0.1915 | ±0.3830 | +1.196 | 0.2315 |  |
| Avg. daily mean/SD | +0.0035 | 0.0544 | ±0.1088 | +0.064 | 0.9486 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.2637**, Adj R² = **0.2513**, F-statistic = **21.33** (p = **9.95e-47**), Residual SE = **2.113** on **834** df, AIC = **3694.8**, BIC = **3765.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5149** | 0.7556 | ±1.5111 | **+32.445** | **6.28e-231** | *** |
| Education: graduate level (vs college) | -0.0885 | 0.1640 | ±0.3279 | -0.540 | 0.5895 |  |
| Education: high school or below (vs college) | +0.2337 | 0.2221 | ±0.4443 | +1.052 | 0.2928 |  |
| Site: UCSD (vs UAB) | -0.1453 | 0.1778 | ±0.3555 | -0.817 | 0.4137 |  |
| **Site: UW (vs UAB)** | **-1.4112** | 0.1837 | ±0.3675 | **-7.681** | **1.58e-14** | *** |
| Season: spring (vs autumn) | -0.2254 | 0.1965 | ±0.3929 | -1.147 | 0.2512 |  |
| **Season: summer (vs autumn)** | **+1.7784** | 0.2221 | ±0.4443 | **+8.006** | **1.19e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2025** | 0.2134 | ±0.4268 | **-5.635** | **1.75e-08** | *** |
| Age (years) | +0.0093 | 0.0075 | ±0.0150 | +1.239 | 0.2152 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.279 | 0.2010 |  |
| Hypertension | +0.3062 | 0.1600 | ±0.3200 | +1.914 | 0.0557 | . |
| High cholesterol | -0.1617 | 0.1570 | ±0.3141 | -1.030 | 0.3032 |  |
| Kidney disease | -0.1231 | 0.1927 | ±0.3853 | -0.639 | 0.5229 |  |
| Circulatory disease | +0.2283 | 0.1918 | ±0.3835 | +1.191 | 0.2337 |  |
| MAG (mg/dL/h) | -0.0086 | 0.0078 | ±0.0156 | -1.110 | 0.2672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.27** (p = **1.32e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3018** | 0.6952 | ±1.3904 | **+34.956** | **1.05e-267** | *** |
| Education: graduate level (vs college) | -0.0844 | 0.1631 | ±0.3263 | -0.517 | 0.6049 |  |
| Education: high school or below (vs college) | +0.2369 | 0.2240 | ±0.4479 | +1.058 | 0.2902 |  |
| Site: UCSD (vs UAB) | -0.1465 | 0.1789 | ±0.3578 | -0.819 | 0.4128 |  |
| **Site: UW (vs UAB)** | **-1.3965** | 0.1844 | ±0.3688 | **-7.573** | **3.64e-14** | *** |
| Season: spring (vs autumn) | -0.2217 | 0.1962 | ±0.3924 | -1.130 | 0.2585 |  |
| **Season: summer (vs autumn)** | **+1.7871** | 0.2215 | ±0.4430 | **+8.069** | **7.10e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1964** | 0.2136 | ±0.4272 | **-5.601** | **2.14e-08** | *** |
| Age (years) | +0.0101 | 0.0075 | ±0.0151 | +1.335 | 0.1819 |  |
| BMI (kg/m2) | +0.0130 | 0.0107 | ±0.0213 | +1.223 | 0.2215 |  |
| Hypertension | +0.3055 | 0.1601 | ±0.3202 | +1.908 | 0.0564 | . |
| High cholesterol | -0.1616 | 0.1575 | ±0.3150 | -1.026 | 0.3050 |  |
| Kidney disease | -0.1155 | 0.1943 | ±0.3887 | -0.594 | 0.5524 |  |
| Circulatory disease | +0.2317 | 0.1916 | ±0.3833 | +1.209 | 0.2267 |  |
| Avg. daily range (mg/dL) | -0.0015 | 0.0018 | ±0.0036 | -0.808 | 0.4189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.83e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.1**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1319** | 0.6570 | ±1.3139 | **+36.732** | **2.24e-295** | *** |
| Education: graduate level (vs college) | -0.0747 | 0.1631 | ±0.3263 | -0.458 | 0.6468 |  |
| Education: high school or below (vs college) | +0.2200 | 0.2242 | ±0.4484 | +0.981 | 0.3265 |  |
| Site: UCSD (vs UAB) | -0.1366 | 0.1799 | ±0.3599 | -0.759 | 0.4479 |  |
| **Site: UW (vs UAB)** | **-1.3890** | 0.1863 | ±0.3725 | **-7.457** | **8.83e-14** | *** |
| Season: spring (vs autumn) | -0.2257 | 0.1966 | ±0.3932 | -1.148 | 0.2510 |  |
| **Season: summer (vs autumn)** | **+1.7912** | 0.2212 | ±0.4423 | **+8.099** | **5.55e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2007** | 0.2137 | ±0.4274 | **-5.619** | **1.92e-08** | *** |
| Age (years) | +0.0095 | 0.0075 | ±0.0150 | +1.263 | 0.2068 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0213 | +1.270 | 0.2040 |  |
| Hypertension | +0.3103 | 0.1598 | ±0.3196 | +1.942 | 0.0521 | . |
| High cholesterol | -0.1584 | 0.1575 | ±0.3150 | -1.006 | 0.3145 |  |
| Kidney disease | -0.1417 | 0.1935 | ±0.3869 | -0.732 | 0.4640 |  |
| Circulatory disease | +0.2312 | 0.1918 | ±0.3836 | +1.206 | 0.2280 |  |
| SD of daily means (mg/dL) | -0.0015 | 0.0112 | ±0.0224 | -0.132 | 0.8946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2507**, F-statistic = **21.27** (p = **1.37e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9140** | 0.7069 | ±1.4138 | **+33.830** | **7.15e-251** | *** |
| Education: graduate level (vs college) | -0.0820 | 0.1631 | ±0.3261 | -0.503 | 0.6149 |  |
| Education: high school or below (vs college) | +0.2345 | 0.2250 | ±0.4501 | +1.042 | 0.2974 |  |
| Site: UCSD (vs UAB) | -0.1485 | 0.1798 | ±0.3595 | -0.826 | 0.4086 |  |
| **Site: UW (vs UAB)** | **-1.3929** | 0.1848 | ±0.3695 | **-7.539** | **4.75e-14** | *** |
| Season: spring (vs autumn) | -0.2237 | 0.1964 | ±0.3927 | -1.139 | 0.2546 |  |
| **Season: summer (vs autumn)** | **+1.7868** | 0.2219 | ±0.4438 | **+8.052** | **8.12e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1948** | 0.2140 | ±0.4280 | **-5.582** | **2.37e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.311 | 0.1898 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.295 | 0.1955 |  |
| Hypertension | +0.3049 | 0.1606 | ±0.3213 | +1.898 | 0.0577 | . |
| High cholesterol | -0.1630 | 0.1578 | ±0.3155 | -1.033 | 0.3016 |  |
| Kidney disease | -0.1298 | 0.1905 | ±0.3811 | -0.681 | 0.4956 |  |
| Circulatory disease | +0.2320 | 0.1917 | ±0.3834 | +1.210 | 0.2261 |  |
| Time in range 70-180, pooled (%) | +0.0023 | 0.0031 | ±0.0062 | +0.737 | 0.4610 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.28** (p = **1.31e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.3**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8962** | 0.7076 | ±1.4151 | **+33.773** | **4.90e-250** | *** |
| Education: graduate level (vs college) | -0.0825 | 0.1631 | ±0.3261 | -0.506 | 0.6130 |  |
| Education: high school or below (vs college) | +0.2363 | 0.2251 | ±0.4502 | +1.050 | 0.2937 |  |
| Site: UCSD (vs UAB) | -0.1501 | 0.1798 | ±0.3597 | -0.835 | 0.4040 |  |
| **Site: UW (vs UAB)** | **-1.3933** | 0.1848 | ±0.3695 | **-7.541** | **4.67e-14** | *** |
| Season: spring (vs autumn) | -0.2231 | 0.1963 | ±0.3927 | -1.136 | 0.2558 |  |
| **Season: summer (vs autumn)** | **+1.7872** | 0.2218 | ±0.4435 | **+8.060** | **7.65e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1933** | 0.2141 | ±0.4283 | **-5.572** | **2.51e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.318 | 0.1876 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.298 | 0.1945 |  |
| Hypertension | +0.3044 | 0.1607 | ±0.3213 | +1.894 | 0.0582 | . |
| High cholesterol | -0.1632 | 0.1577 | ±0.3155 | -1.035 | 0.3008 |  |
| Kidney disease | -0.1280 | 0.1904 | ±0.3809 | -0.672 | 0.5014 |  |
| Circulatory disease | +0.2323 | 0.1917 | ±0.3834 | +1.212 | 0.2256 |  |
| Avg. daily time in range 70-180 (%) | +0.0025 | 0.0031 | ±0.0062 | +0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2628**, Adj R² = **0.2504**, F-statistic = **21.23** (p = **1.64e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.8**, BIC = **3767.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1542** | 0.6507 | ±1.3013 | **+37.122** | **1.25e-301** | *** |
| Education: graduate level (vs college) | -0.0716 | 0.1623 | ±0.3247 | -0.441 | 0.6590 |  |
| Education: high school or below (vs college) | +0.2130 | 0.2226 | ±0.4452 | +0.957 | 0.3386 |  |
| Site: UCSD (vs UAB) | -0.1416 | 0.1791 | ±0.3583 | -0.790 | 0.4292 |  |
| **Site: UW (vs UAB)** | **-1.3949** | 0.1845 | ±0.3690 | **-7.560** | **4.04e-14** | *** |
| Season: spring (vs autumn) | -0.2262 | 0.1965 | ±0.3929 | -1.151 | 0.2496 |  |
| **Season: summer (vs autumn)** | **+1.7889** | 0.2212 | ±0.4424 | **+8.088** | **6.07e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2081** | 0.2139 | ±0.4278 | **-5.647** | **1.63e-08** | *** |
| Age (years) | +0.0092 | 0.0075 | ±0.0150 | +1.221 | 0.2223 |  |
| BMI (kg/m2) | +0.0137 | 0.0105 | ±0.0211 | +1.302 | 0.1928 |  |
| **Hypertension** | **+0.3146** | 0.1602 | ±0.3205 | **+1.963** | **0.0496** | * |
| High cholesterol | -0.1621 | 0.1562 | ±0.3123 | -1.038 | 0.2992 |  |
| Kidney disease | -0.1470 | 0.1912 | ±0.3825 | -0.769 | 0.4421 |  |
| Circulatory disease | +0.2343 | 0.1915 | ±0.3829 | +1.224 | 0.2211 |  |
| Any reading < 54 during wear (0/1) | -0.0846 | 0.1658 | ±0.3316 | -0.510 | 0.6099 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.80e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1110** | 0.6467 | ±1.2934 | **+37.284** | **3.01e-304** | *** |
| Education: graduate level (vs college) | -0.0708 | 0.1623 | ±0.3246 | -0.436 | 0.6625 |  |
| Education: high school or below (vs college) | +0.2210 | 0.2226 | ±0.4451 | +0.993 | 0.3207 |  |
| Site: UCSD (vs UAB) | -0.1304 | 0.1786 | ±0.3572 | -0.730 | 0.4653 |  |
| **Site: UW (vs UAB)** | **-1.3817** | 0.1839 | ±0.3678 | **-7.513** | **5.77e-14** | *** |
| Season: spring (vs autumn) | -0.2240 | 0.1968 | ±0.3935 | -1.138 | 0.2550 |  |
| **Season: summer (vs autumn)** | **+1.7920** | 0.2209 | ±0.4417 | **+8.114** | **4.91e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2006** | 0.2140 | ±0.4281 | **-5.609** | **2.03e-08** | *** |
| Age (years) | +0.0095 | 0.0075 | ±0.0150 | +1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.0133 | 0.0106 | ±0.0212 | +1.259 | 0.2079 |  |
| Hypertension | +0.3089 | 0.1604 | ±0.3209 | +1.925 | 0.0542 | . |
| High cholesterol | -0.1572 | 0.1570 | ±0.3141 | -1.001 | 0.3169 |  |
| Kidney disease | -0.1441 | 0.1913 | ±0.3826 | -0.753 | 0.4512 |  |
| Circulatory disease | +0.2259 | 0.1909 | ±0.3819 | +1.183 | 0.2368 |  |
| Time < 54 (%) | +0.0431 | 0.1788 | ±0.3576 | +0.241 | 0.8093 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.75e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1125** | 0.6462 | ±1.2924 | **+37.313** | **1.00e-304** | *** |
| Education: graduate level (vs college) | -0.0697 | 0.1621 | ±0.3243 | -0.430 | 0.6671 |  |
| Education: high school or below (vs college) | +0.2214 | 0.2225 | ±0.4449 | +0.995 | 0.3196 |  |
| Site: UCSD (vs UAB) | -0.1298 | 0.1787 | ±0.3573 | -0.726 | 0.4675 |  |
| **Site: UW (vs UAB)** | **-1.3811** | 0.1841 | ±0.3682 | **-7.503** | **6.25e-14** | *** |
| Season: spring (vs autumn) | -0.2220 | 0.1968 | ±0.3937 | -1.128 | 0.2594 |  |
| **Season: summer (vs autumn)** | **+1.7925** | 0.2210 | ±0.4421 | **+8.110** | **5.08e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2003** | 0.2141 | ±0.4282 | **-5.607** | **2.06e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.255 | 0.2096 |  |
| BMI (kg/m2) | +0.0133 | 0.0106 | ±0.0212 | +1.262 | 0.2070 |  |
| Hypertension | +0.3090 | 0.1602 | ±0.3203 | +1.929 | 0.0537 | . |
| High cholesterol | -0.1561 | 0.1569 | ±0.3138 | -0.995 | 0.3199 |  |
| Kidney disease | -0.1446 | 0.1912 | ±0.3825 | -0.756 | 0.4497 |  |
| Circulatory disease | +0.2251 | 0.1912 | ±0.3823 | +1.177 | 0.2390 |  |
| Avg. daily time < 54 (%) | +0.0587 | 0.1998 | ±0.3996 | +0.294 | 0.7689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.28** (p = **1.30e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.3**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1038** | 0.6475 | ±1.2949 | **+37.227** | **2.45e-303** | *** |
| Education: graduate level (vs college) | -0.0654 | 0.1626 | ±0.3251 | -0.402 | 0.6876 |  |
| Education: high school or below (vs college) | +0.2183 | 0.2230 | ±0.4459 | +0.979 | 0.3276 |  |
| Site: UCSD (vs UAB) | -0.1235 | 0.1788 | ±0.3575 | -0.691 | 0.4898 |  |
| **Site: UW (vs UAB)** | **-1.3754** | 0.1836 | ±0.3673 | **-7.490** | **6.89e-14** | *** |
| Season: spring (vs autumn) | -0.2159 | 0.1966 | ±0.3932 | -1.098 | 0.2721 |  |
| **Season: summer (vs autumn)** | **+1.7976** | 0.2205 | ±0.4410 | **+8.152** | **3.57e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1931** | 0.2142 | ±0.4284 | **-5.571** | **2.54e-08** | *** |
| Age (years) | +0.0092 | 0.0075 | ±0.0149 | +1.232 | 0.2181 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0213 | +1.245 | 0.2132 |  |
| Hypertension | +0.3082 | 0.1601 | ±0.3202 | +1.925 | 0.0542 | . |
| High cholesterol | -0.1565 | 0.1571 | ±0.3142 | -0.996 | 0.3191 |  |
| Kidney disease | -0.1456 | 0.1916 | ±0.3832 | -0.760 | 0.4472 |  |
| Circulatory disease | +0.2240 | 0.1912 | ±0.3824 | +1.171 | 0.2414 |  |
| Time 54-69, pooled (%) | +0.0423 | 0.0512 | ±0.1025 | +0.826 | 0.4087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.2636**, Adj R² = **0.2512**, F-statistic = **21.32** (p = **1.04e-46**), Residual SE = **2.113** on **834** df, AIC = **3694.9**, BIC = **3766.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1103** | 0.6466 | ±1.2931 | **+37.290** | **2.41e-304** | *** |
| Education: graduate level (vs college) | -0.0630 | 0.1624 | ±0.3249 | -0.388 | 0.6983 |  |
| Education: high school or below (vs college) | +0.2170 | 0.2231 | ±0.4462 | +0.973 | 0.3307 |  |
| Site: UCSD (vs UAB) | -0.1217 | 0.1787 | ±0.3575 | -0.681 | 0.4959 |  |
| **Site: UW (vs UAB)** | **-1.3729** | 0.1836 | ±0.3671 | **-7.479** | **7.47e-14** | *** |
| Season: spring (vs autumn) | -0.2139 | 0.1965 | ±0.3930 | -1.089 | 0.2763 |  |
| **Season: summer (vs autumn)** | **+1.7983** | 0.2204 | ±0.4409 | **+8.158** | **3.41e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1918** | 0.2142 | ±0.4283 | **-5.565** | **2.62e-08** | *** |
| Age (years) | +0.0090 | 0.0075 | ±0.0149 | +1.207 | 0.2275 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.240 | 0.2148 |  |
| Hypertension | +0.3078 | 0.1600 | ±0.3199 | +1.924 | 0.0543 | . |
| High cholesterol | -0.1556 | 0.1571 | ±0.3142 | -0.990 | 0.3220 |  |
| Kidney disease | -0.1447 | 0.1914 | ±0.3829 | -0.756 | 0.4499 |  |
| Circulatory disease | +0.2240 | 0.1911 | ±0.3823 | +1.172 | 0.2413 |  |
| Avg. daily time 54-69 (%) | +0.0524 | 0.0485 | ±0.0971 | +1.080 | 0.2803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.2630**, Adj R² = **0.2507**, F-statistic = **21.26** (p = **1.40e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.5**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1025** | 0.6477 | ±1.2953 | **+37.214** | **4.00e-303** | *** |
| Education: graduate level (vs college) | -0.0663 | 0.1625 | ±0.3251 | -0.408 | 0.6835 |  |
| Education: high school or below (vs college) | +0.2203 | 0.2227 | ±0.4455 | +0.989 | 0.3225 |  |
| Site: UCSD (vs UAB) | -0.1232 | 0.1788 | ±0.3576 | -0.689 | 0.4908 |  |
| **Site: UW (vs UAB)** | **-1.3747** | 0.1837 | ±0.3673 | **-7.484** | **7.20e-14** | *** |
| Season: spring (vs autumn) | -0.2173 | 0.1967 | ±0.3934 | -1.105 | 0.2694 |  |
| **Season: summer (vs autumn)** | **+1.7966** | 0.2205 | ±0.4410 | **+8.148** | **3.69e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1943** | 0.2142 | ±0.4284 | **-5.576** | **2.46e-08** | *** |
| Age (years) | +0.0093 | 0.0075 | ±0.0150 | +1.241 | 0.2144 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.244 | 0.2137 |  |
| Hypertension | +0.3079 | 0.1602 | ±0.3205 | +1.922 | 0.0546 | . |
| High cholesterol | -0.1564 | 0.1571 | ±0.3142 | -0.995 | 0.3196 |  |
| Kidney disease | -0.1447 | 0.1916 | ±0.3832 | -0.755 | 0.4500 |  |
| Circulatory disease | +0.2230 | 0.1911 | ±0.3821 | +1.167 | 0.2431 |  |
| Time < 70 (%) | +0.0313 | 0.0418 | ±0.0837 | +0.748 | 0.4543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.2634**, Adj R² = **0.2510**, F-statistic = **21.30** (p = **1.16e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.1**, BIC = **3766.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1086** | 0.6466 | ±1.2933 | **+37.283** | **3.08e-304** | *** |
| Education: graduate level (vs college) | -0.0637 | 0.1624 | ±0.3248 | -0.393 | 0.6947 |  |
| Education: high school or below (vs college) | +0.2195 | 0.2229 | ±0.4457 | +0.985 | 0.3246 |  |
| Site: UCSD (vs UAB) | -0.1216 | 0.1788 | ±0.3576 | -0.680 | 0.4963 |  |
| **Site: UW (vs UAB)** | **-1.3725** | 0.1836 | ±0.3673 | **-7.474** | **7.76e-14** | *** |
| Season: spring (vs autumn) | -0.2145 | 0.1966 | ±0.3933 | -1.091 | 0.2754 |  |
| **Season: summer (vs autumn)** | **+1.7974** | 0.2205 | ±0.4410 | **+8.151** | **3.61e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1932** | 0.2142 | ±0.4283 | **-5.571** | **2.53e-08** | *** |
| Age (years) | +0.0091 | 0.0075 | ±0.0149 | +1.216 | 0.2240 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.243 | 0.2139 |  |
| Hypertension | +0.3077 | 0.1600 | ±0.3201 | +1.923 | 0.0545 | . |
| High cholesterol | -0.1549 | 0.1571 | ±0.3141 | -0.986 | 0.3240 |  |
| Kidney disease | -0.1444 | 0.1914 | ±0.3828 | -0.754 | 0.4507 |  |
| Circulatory disease | +0.2226 | 0.1910 | ±0.3821 | +1.165 | 0.2439 |  |
| Avg. daily time < 70 (%) | +0.0392 | 0.0409 | ±0.0819 | +0.956 | 0.3389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.75e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9689** | 0.8084 | ±1.6168 | **+29.650** | **3.43e-193** | *** |
| Education: graduate level (vs college) | -0.0770 | 0.1632 | ±0.3263 | -0.472 | 0.6369 |  |
| Education: high school or below (vs college) | +0.2244 | 0.2245 | ±0.4490 | +0.999 | 0.3176 |  |
| Site: UCSD (vs UAB) | -0.1395 | 0.1799 | ±0.3597 | -0.775 | 0.4381 |  |
| **Site: UW (vs UAB)** | **-1.3916** | 0.1854 | ±0.3707 | **-7.508** | **6.02e-14** | *** |
| Season: spring (vs autumn) | -0.2264 | 0.1967 | ±0.3934 | -1.151 | 0.2496 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2228 | ±0.4456 | **+8.016** | **1.10e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2015** | 0.2135 | ±0.4271 | **-5.626** | **1.84e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.256 | 0.2090 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.273 | 0.2030 |  |
| Hypertension | +0.3105 | 0.1596 | ±0.3192 | +1.946 | 0.0517 | . |
| High cholesterol | -0.1592 | 0.1574 | ±0.3148 | -1.012 | 0.3118 |  |
| Kidney disease | -0.1403 | 0.1914 | ±0.3827 | -0.733 | 0.4634 |  |
| Circulatory disease | +0.2301 | 0.1917 | ±0.3834 | +1.200 | 0.2300 |  |
| Time 54-250, pooled (%) | +0.0016 | 0.0052 | ±0.0105 | +0.313 | 0.7540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.74e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.9**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9536** | 0.8181 | ±1.6361 | **+29.281** | **1.82e-188** | *** |
| Education: graduate level (vs college) | -0.0774 | 0.1632 | ±0.3264 | -0.474 | 0.6355 |  |
| Education: high school or below (vs college) | +0.2248 | 0.2244 | ±0.4489 | +1.002 | 0.3164 |  |
| Site: UCSD (vs UAB) | -0.1399 | 0.1799 | ±0.3597 | -0.778 | 0.4367 |  |
| **Site: UW (vs UAB)** | **-1.3918** | 0.1853 | ±0.3707 | **-7.510** | **5.92e-14** | *** |
| Season: spring (vs autumn) | -0.2262 | 0.1966 | ±0.3933 | -1.150 | 0.2499 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2227 | ±0.4455 | **+8.018** | **1.07e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2011** | 0.2135 | ±0.4271 | **-5.625** | **1.86e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.259 | 0.2082 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.274 | 0.2028 |  |
| Hypertension | +0.3104 | 0.1596 | ±0.3193 | +1.945 | 0.0518 | . |
| High cholesterol | -0.1593 | 0.1574 | ±0.3148 | -1.012 | 0.3114 |  |
| Kidney disease | -0.1396 | 0.1914 | ±0.3828 | -0.729 | 0.4659 |  |
| Circulatory disease | +0.2304 | 0.1917 | ±0.3835 | +1.202 | 0.2295 |  |
| Avg. daily time 54-250 (%) | +0.0018 | 0.0053 | ±0.0106 | +0.336 | 0.7369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2635**, Adj R² = **0.2511**, F-statistic = **21.31** (p = **1.11e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.0**, BIC = **3766.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1265** | 0.6482 | ±1.2964 | **+37.219** | **3.31e-303** | *** |
| Education: graduate level (vs college) | -0.0776 | 0.1626 | ±0.3252 | -0.478 | 0.6330 |  |
| Education: high school or below (vs college) | +0.2344 | 0.2240 | ±0.4480 | +1.046 | 0.2954 |  |
| Site: UCSD (vs UAB) | -0.1491 | 0.1783 | ±0.3566 | -0.836 | 0.4031 |  |
| **Site: UW (vs UAB)** | **-1.3841** | 0.1839 | ±0.3678 | **-7.527** | **5.21e-14** | *** |
| Season: spring (vs autumn) | -0.2179 | 0.1965 | ±0.3929 | -1.109 | 0.2675 |  |
| **Season: summer (vs autumn)** | **+1.7982** | 0.2200 | ±0.4399 | **+8.175** | **2.95e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1876** | 0.2149 | ±0.4297 | **-5.527** | **3.26e-08** | *** |
| Age (years) | +0.0105 | 0.0076 | ±0.0152 | +1.381 | 0.1673 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.301 | 0.1931 |  |
| Hypertension | +0.2971 | 0.1612 | ±0.3224 | +1.843 | 0.0653 | . |
| High cholesterol | -0.1646 | 0.1578 | ±0.3157 | -1.043 | 0.2969 |  |
| Kidney disease | -0.1270 | 0.1902 | ±0.3803 | -0.668 | 0.5043 |  |
| Circulatory disease | +0.2317 | 0.1916 | ±0.3832 | +1.209 | 0.2265 |  |
| Time 181-250, pooled (%) | -0.0049 | 0.0048 | ±0.0097 | -1.020 | 0.3079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.2637**, Adj R² = **0.2513**, F-statistic = **21.33** (p = **1.00e-46**), Residual SE = **2.113** on **834** df, AIC = **3694.8**, BIC = **3765.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1285** | 0.6486 | ±1.2972 | **+37.202** | **6.41e-303** | *** |
| Education: graduate level (vs college) | -0.0776 | 0.1626 | ±0.3251 | -0.478 | 0.6330 |  |
| Education: high school or below (vs college) | +0.2371 | 0.2241 | ±0.4483 | +1.058 | 0.2900 |  |
| Site: UCSD (vs UAB) | -0.1513 | 0.1784 | ±0.3568 | -0.848 | 0.3963 |  |
| **Site: UW (vs UAB)** | **-1.3847** | 0.1839 | ±0.3678 | **-7.528** | **5.13e-14** | *** |
| Season: spring (vs autumn) | -0.2172 | 0.1964 | ±0.3928 | -1.106 | 0.2688 |  |
| **Season: summer (vs autumn)** | **+1.7989** | 0.2200 | ±0.4399 | **+8.179** | **2.87e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1854** | 0.2150 | ±0.4301 | **-5.512** | **3.54e-08** | *** |
| Age (years) | +0.0106 | 0.0076 | ±0.0152 | +1.389 | 0.1649 |  |
| BMI (kg/m2) | +0.0139 | 0.0106 | ±0.0213 | +1.305 | 0.1918 |  |
| Hypertension | +0.2963 | 0.1612 | ±0.3223 | +1.838 | 0.0660 | . |
| High cholesterol | -0.1648 | 0.1578 | ±0.3156 | -1.044 | 0.2963 |  |
| Kidney disease | -0.1251 | 0.1900 | ±0.3800 | -0.658 | 0.5104 |  |
| Circulatory disease | +0.2315 | 0.1916 | ±0.3833 | +1.208 | 0.2270 |  |
| Avg. daily time 181-250 (%) | -0.0053 | 0.0048 | ±0.0095 | -1.109 | 0.2673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2508**, F-statistic = **21.27** (p = **1.32e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1440** | 0.6487 | ±1.2974 | **+37.219** | **3.41e-303** | *** |
| Education: graduate level (vs college) | -0.0821 | 0.1630 | ±0.3260 | -0.503 | 0.6147 |  |
| Education: high school or below (vs college) | +0.2354 | 0.2249 | ±0.4497 | +1.047 | 0.2952 |  |
| Site: UCSD (vs UAB) | -0.1483 | 0.1796 | ±0.3591 | -0.826 | 0.4090 |  |
| **Site: UW (vs UAB)** | **-1.3922** | 0.1846 | ±0.3693 | **-7.540** | **4.71e-14** | *** |
| Season: spring (vs autumn) | -0.2230 | 0.1963 | ±0.3927 | -1.136 | 0.2561 |  |
| **Season: summer (vs autumn)** | **+1.7871** | 0.2218 | ±0.4436 | **+8.057** | **7.80e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1938** | 0.2141 | ±0.4282 | **-5.576** | **2.46e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.313 | 0.1892 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.293 | 0.1959 |  |
| Hypertension | +0.3045 | 0.1607 | ±0.3215 | +1.895 | 0.0581 | . |
| High cholesterol | -0.1631 | 0.1578 | ±0.3155 | -1.034 | 0.3012 |  |
| Kidney disease | -0.1291 | 0.1906 | ±0.3811 | -0.678 | 0.4981 |  |
| Circulatory disease | +0.2317 | 0.1917 | ±0.3834 | +1.209 | 0.2267 |  |
| Time > 180 (%) | -0.0024 | 0.0031 | ±0.0062 | -0.778 | 0.4363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2633**, Adj R² = **0.2509**, F-statistic = **21.29** (p = **1.24e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.2**, BIC = **3766.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1442** | 0.6487 | ±1.2975 | **+37.217** | **3.56e-303** | *** |
| Education: graduate level (vs college) | -0.0826 | 0.1630 | ±0.3260 | -0.507 | 0.6123 |  |
| Education: high school or below (vs college) | +0.2376 | 0.2249 | ±0.4498 | +1.056 | 0.2908 |  |
| Site: UCSD (vs UAB) | -0.1502 | 0.1796 | ±0.3593 | -0.836 | 0.4032 |  |
| **Site: UW (vs UAB)** | **-1.3927** | 0.1847 | ±0.3693 | **-7.542** | **4.61e-14** | *** |
| Season: spring (vs autumn) | -0.2222 | 0.1963 | ±0.3926 | -1.132 | 0.2577 |  |
| **Season: summer (vs autumn)** | **+1.7874** | 0.2216 | ±0.4433 | **+8.065** | **7.34e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1921** | 0.2142 | ±0.4284 | **-5.565** | **2.62e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.320 | 0.1869 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.297 | 0.1945 |  |
| Hypertension | +0.3039 | 0.1608 | ±0.3215 | +1.890 | 0.0587 | . |
| High cholesterol | -0.1634 | 0.1577 | ±0.3154 | -1.036 | 0.3003 |  |
| Kidney disease | -0.1269 | 0.1904 | ±0.3809 | -0.666 | 0.5052 |  |
| Circulatory disease | +0.2320 | 0.1917 | ±0.3834 | +1.211 | 0.2261 |  |
| Avg. daily time > 180 (%) | -0.0026 | 0.0031 | ±0.0062 | -0.852 | 0.3942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.28** (p = **1.28e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.3**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1402** | 0.6485 | ±1.2969 | **+37.227** | **2.51e-303** | *** |
| Education: graduate level (vs college) | -0.0850 | 0.1636 | ±0.3271 | -0.519 | 0.6035 |  |
| Education: high school or below (vs college) | +0.2350 | 0.2246 | ±0.4492 | +1.046 | 0.2954 |  |
| Site: UCSD (vs UAB) | -0.1502 | 0.1799 | ±0.3598 | -0.835 | 0.4038 |  |
| **Site: UW (vs UAB)** | **-1.3910** | 0.1846 | ±0.3693 | **-7.534** | **4.92e-14** | *** |
| Season: spring (vs autumn) | -0.2220 | 0.1963 | ±0.3926 | -1.131 | 0.2582 |  |
| **Season: summer (vs autumn)** | **+1.7862** | 0.2218 | ±0.4436 | **+8.053** | **8.07e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1929** | 0.2140 | ±0.4280 | **-5.574** | **2.49e-08** | *** |
| Age (years) | +0.0096 | 0.0075 | ±0.0150 | +1.277 | 0.2016 |  |
| BMI (kg/m2) | +0.0142 | 0.0107 | ±0.0215 | +1.323 | 0.1857 |  |
| Hypertension | +0.3037 | 0.1608 | ±0.3215 | +1.889 | 0.0589 | . |
| High cholesterol | -0.1636 | 0.1577 | ±0.3153 | -1.038 | 0.2994 |  |
| Kidney disease | -0.1311 | 0.1901 | ±0.3803 | -0.690 | 0.4904 |  |
| Circulatory disease | +0.2325 | 0.1918 | ±0.3836 | +1.212 | 0.2255 |  |
| Nocturnal time > 180 (%) | -0.0024 | 0.0030 | ±0.0060 | -0.807 | 0.4195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2627**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.69e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.9**, BIC = **3767.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1374** | 0.6510 | ±1.3019 | **+37.079** | **6.16e-301** | *** |
| Education: graduate level (vs college) | -0.0785 | 0.1634 | ±0.3269 | -0.480 | 0.6311 |  |
| Education: high school or below (vs college) | +0.2216 | 0.2231 | ±0.4462 | +0.993 | 0.3206 |  |
| Site: UCSD (vs UAB) | -0.1386 | 0.1786 | ±0.3573 | -0.776 | 0.4378 |  |
| **Site: UW (vs UAB)** | **-1.3847** | 0.1838 | ±0.3675 | **-7.536** | **4.85e-14** | *** |
| Season: spring (vs autumn) | -0.2265 | 0.1966 | ±0.3933 | -1.152 | 0.2495 |  |
| **Season: summer (vs autumn)** | **+1.7914** | 0.2210 | ±0.4420 | **+8.106** | **5.23e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2017** | 0.2135 | ±0.4270 | **-5.629** | **1.82e-08** | *** |
| Age (years) | +0.0100 | 0.0076 | ±0.0153 | +1.310 | 0.1901 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.246 | 0.2126 |  |
| Hypertension | +0.3065 | 0.1604 | ±0.3208 | +1.911 | 0.0560 | . |
| High cholesterol | -0.1589 | 0.1574 | ±0.3148 | -1.010 | 0.3126 |  |
| Kidney disease | -0.1373 | 0.1916 | ±0.3832 | -0.716 | 0.4737 |  |
| Circulatory disease | +0.2279 | 0.1916 | ±0.3833 | +1.189 | 0.2343 |  |
| Any reading > 250 during wear (0/1) | -0.0675 | 0.1616 | ±0.3233 | -0.418 | 0.6762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.75e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1331** | 0.6487 | ±1.2974 | **+37.203** | **6.03e-303** | *** |
| Education: graduate level (vs college) | -0.0771 | 0.1632 | ±0.3263 | -0.472 | 0.6367 |  |
| Education: high school or below (vs college) | +0.2246 | 0.2245 | ±0.4491 | +1.000 | 0.3172 |  |
| Site: UCSD (vs UAB) | -0.1394 | 0.1798 | ±0.3595 | -0.775 | 0.4382 |  |
| **Site: UW (vs UAB)** | **-1.3915** | 0.1853 | ±0.3706 | **-7.510** | **5.92e-14** | *** |
| Season: spring (vs autumn) | -0.2264 | 0.1967 | ±0.3934 | -1.151 | 0.2497 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2228 | ±0.4456 | **+8.015** | **1.10e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2014** | 0.2135 | ±0.4271 | **-5.626** | **1.85e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.256 | 0.2090 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.273 | 0.2031 |  |
| Hypertension | +0.3105 | 0.1596 | ±0.3192 | +1.945 | 0.0517 | . |
| High cholesterol | -0.1592 | 0.1574 | ±0.3148 | -1.011 | 0.3118 |  |
| Kidney disease | -0.1402 | 0.1914 | ±0.3827 | -0.733 | 0.4638 |  |
| Circulatory disease | +0.2300 | 0.1917 | ±0.3834 | +1.200 | 0.2302 |  |
| Time > 250 (%) | -0.0017 | 0.0052 | ±0.0105 | -0.319 | 0.7499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2627**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.73e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.9**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1326** | 0.6482 | ±1.2963 | **+37.233** | **2.02e-303** | *** |
| Education: graduate level (vs college) | -0.0774 | 0.1632 | ±0.3264 | -0.474 | 0.6352 |  |
| Education: high school or below (vs college) | +0.2251 | 0.2244 | ±0.4489 | +1.003 | 0.3158 |  |
| Site: UCSD (vs UAB) | -0.1399 | 0.1798 | ±0.3596 | -0.778 | 0.4366 |  |
| **Site: UW (vs UAB)** | **-1.3918** | 0.1853 | ±0.3705 | **-7.512** | **5.82e-14** | *** |
| Season: spring (vs autumn) | -0.2261 | 0.1966 | ±0.3933 | -1.150 | 0.2501 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2227 | ±0.4455 | **+8.018** | **1.07e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2010** | 0.2135 | ±0.4271 | **-5.624** | **1.86e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.258 | 0.2083 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0213 | +1.274 | 0.2028 |  |
| Hypertension | +0.3104 | 0.1597 | ±0.3193 | +1.944 | 0.0518 | . |
| High cholesterol | -0.1593 | 0.1574 | ±0.3148 | -1.012 | 0.3115 |  |
| Kidney disease | -0.1394 | 0.1914 | ±0.3828 | -0.728 | 0.4664 |  |
| Circulatory disease | +0.2303 | 0.1917 | ±0.3834 | +1.201 | 0.2297 |  |
| Avg. daily time > 250 (%) | -0.0018 | 0.0053 | ±0.0106 | -0.345 | 0.7301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2139**, F-statistic = **18.75** (p = **1.01e-38**), Residual SE = **6.185** on **835** df, AIC = **5517.2**, BIC = **5583.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0582** | 1.9391 | ±3.8782 | **+25.815** | **5.97e-147** | *** |
| Education: graduate level (vs college) | +0.0789 | 0.4778 | ±0.9557 | +0.165 | 0.8688 |  |
| Education: high school or below (vs college) | +0.2951 | 0.6343 | ±1.2685 | +0.465 | 0.6417 |  |
| **Site: UCSD (vs UAB)** | **+3.4705** | 0.5184 | ±1.0369 | **+6.694** | **2.17e-11** | *** |
| Site: UW (vs UAB) | -0.3932 | 0.5183 | ±1.0365 | -0.759 | 0.4480 |  |
| **Season: spring (vs autumn)** | **-2.0506** | 0.6033 | ±1.2066 | **-3.399** | **6.76e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3622** | 0.5794 | ±1.1588 | **+2.351** | **0.0187** | * |
| **Season: winter (vs autumn)** | **-5.9896** | 0.6729 | ±1.3458 | **-8.901** | **5.54e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0214 | ±0.0427 | **-2.233** | **0.0256** | * |
| BMI (kg/m2) | -0.0270 | 0.0337 | ±0.0674 | -0.801 | 0.4234 |  |
| Hypertension | -0.2595 | 0.4895 | ±0.9791 | -0.530 | 0.5961 |  |
| **High cholesterol** | **-0.9368** | 0.4668 | ±0.9336 | **-2.007** | **0.0448** | * |
| **Kidney disease** | **+1.2889** | 0.5516 | ±1.1031 | **+2.337** | **0.0195** | * |
| Circulatory disease | -0.1407 | 0.5400 | ±1.0799 | -0.261 | 0.7944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.23e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.4232** | 2.1999 | ±4.3997 | **+22.921** | **2.87e-116** | *** |
| Education: graduate level (vs college) | +0.0643 | 0.4804 | ±0.9609 | +0.134 | 0.8936 |  |
| Education: high school or below (vs college) | +0.3194 | 0.6380 | ±1.2760 | +0.501 | 0.6166 |  |
| **Site: UCSD (vs UAB)** | **+3.4602** | 0.5227 | ±1.0454 | **+6.620** | **3.60e-11** | *** |
| Site: UW (vs UAB) | -0.4018 | 0.5205 | ±1.0410 | -0.772 | 0.4401 |  |
| **Season: spring (vs autumn)** | **-2.0566** | 0.6051 | ±1.2102 | **-3.399** | **6.77e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3540** | 0.5804 | ±1.1607 | **+2.333** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9855** | 0.6743 | ±1.3486 | **-8.876** | **6.90e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0429 | **-2.210** | **0.0271** | * |
| BMI (kg/m2) | -0.0261 | 0.0339 | ±0.0678 | -0.769 | 0.4419 |  |
| Hypertension | -0.2589 | 0.4901 | ±0.9803 | -0.528 | 0.5974 |  |
| **High cholesterol** | **-0.9370** | 0.4674 | ±0.9347 | **-2.005** | **0.0450** | * |
| **Kidney disease** | **+1.2932** | 0.5536 | ±1.1072 | **+2.336** | **0.0195** | * |
| Circulatory disease | -0.1378 | 0.5412 | ±1.0825 | -0.255 | 0.7990 |  |
| HbA1c (%) | -0.0604 | 0.1754 | ±0.3509 | -0.344 | 0.7308 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2129**, F-statistic = **17.39** (p = **4.49e-38**), Residual SE = **6.189** on **834** df, AIC = **5519.2**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0187** | 2.0427 | ±4.0855 | **+24.486** | **2.07e-132** | *** |
| Education: graduate level (vs college) | +0.0809 | 0.4796 | ±0.9593 | +0.169 | 0.8661 |  |
| Education: high school or below (vs college) | +0.2921 | 0.6369 | ±1.2738 | +0.459 | 0.6465 |  |
| **Site: UCSD (vs UAB)** | **+3.4725** | 0.5247 | ±1.0494 | **+6.618** | **3.64e-11** | *** |
| Site: UW (vs UAB) | -0.3923 | 0.5208 | ±1.0416 | -0.753 | 0.4513 |  |
| **Season: spring (vs autumn)** | **-2.0512** | 0.6036 | ±1.2073 | **-3.398** | **6.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3630** | 0.5801 | ±1.1602 | **+2.350** | **0.0188** | * |
| **Season: winter (vs autumn)** | **-5.9911** | 0.6766 | ±1.3532 | **-8.854** | **8.41e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0215 | ±0.0429 | **-2.226** | **0.0260** | * |
| BMI (kg/m2) | -0.0270 | 0.0339 | ±0.0677 | -0.798 | 0.4251 |  |
| Hypertension | -0.2590 | 0.4908 | ±0.9816 | -0.528 | 0.5978 |  |
| **High cholesterol** | **-0.9361** | 0.4677 | ±0.9354 | **-2.002** | **0.0453** | * |
| **Kidney disease** | **+1.2862** | 0.5531 | ±1.1062 | **+2.325** | **0.0200** | * |
| Circulatory disease | -0.1410 | 0.5408 | ±1.0816 | -0.261 | 0.7942 |  |
| Mean glucose (mg/dL) | +0.0003 | 0.0055 | ±0.0110 | +0.052 | 0.9588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2129**, F-statistic = **17.39** (p = **4.49e-38**), Residual SE = **6.189** on **834** df, AIC = **5519.2**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9794** | 2.3950 | ±4.7900 | **+20.868** | **1.05e-96** | *** |
| Education: graduate level (vs college) | +0.0809 | 0.4796 | ±0.9593 | +0.169 | 0.8661 |  |
| Education: high school or below (vs college) | +0.2921 | 0.6369 | ±1.2738 | +0.459 | 0.6465 |  |
| **Site: UCSD (vs UAB)** | **+3.4725** | 0.5247 | ±1.0494 | **+6.618** | **3.64e-11** | *** |
| Site: UW (vs UAB) | -0.3923 | 0.5208 | ±1.0416 | -0.753 | 0.4513 |  |
| **Season: spring (vs autumn)** | **-2.0512** | 0.6036 | ±1.2073 | **-3.398** | **6.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3630** | 0.5801 | ±1.1602 | **+2.350** | **0.0188** | * |
| **Season: winter (vs autumn)** | **-5.9911** | 0.6766 | ±1.3532 | **-8.854** | **8.41e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0215 | ±0.0429 | **-2.226** | **0.0260** | * |
| BMI (kg/m2) | -0.0270 | 0.0339 | ±0.0677 | -0.798 | 0.4251 |  |
| Hypertension | -0.2590 | 0.4908 | ±0.9816 | -0.528 | 0.5978 |  |
| **High cholesterol** | **-0.9361** | 0.4677 | ±0.9354 | **-2.002** | **0.0453** | * |
| **Kidney disease** | **+1.2862** | 0.5531 | ±1.1062 | **+2.325** | **0.0200** | * |
| Circulatory disease | -0.1410 | 0.5408 | ±1.0816 | -0.261 | 0.7942 |  |
| GMI (%) | +0.0119 | 0.2301 | ±0.4603 | +0.052 | 0.9588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.39** (p = **4.39e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2200** | 2.0238 | ±4.0476 | **+24.815** | **6.19e-136** | *** |
| Education: graduate level (vs college) | +0.0710 | 0.4799 | ±0.9597 | +0.148 | 0.8824 |  |
| Education: high school or below (vs college) | +0.3070 | 0.6365 | ±1.2729 | +0.482 | 0.6295 |  |
| **Site: UCSD (vs UAB)** | **+3.4628** | 0.5243 | ±1.0486 | **+6.605** | **3.99e-11** | *** |
| Site: UW (vs UAB) | -0.3941 | 0.5192 | ±1.0385 | -0.759 | 0.4478 |  |
| **Season: spring (vs autumn)** | **-2.0465** | 0.6032 | ±1.2064 | **-3.393** | **6.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3594** | 0.5802 | ±1.1604 | **+2.343** | **0.0191** | * |
| **Season: winter (vs autumn)** | **-5.9824** | 0.6769 | ±1.3539 | **-8.837** | **9.80e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0214 | ±0.0428 | **-2.230** | **0.0257** | * |
| BMI (kg/m2) | -0.0265 | 0.0341 | ±0.0682 | -0.776 | 0.4378 |  |
| Hypertension | -0.2624 | 0.4914 | ±0.9828 | -0.534 | 0.5933 |  |
| **High cholesterol** | **-0.9387** | 0.4673 | ±0.9347 | **-2.009** | **0.0446** | * |
| **Kidney disease** | **+1.2959** | 0.5523 | ±1.1047 | **+2.346** | **0.0190** | * |
| Circulatory disease | -0.1394 | 0.5408 | ±1.0816 | -0.258 | 0.7966 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0012 | 0.0053 | ±0.0107 | -0.219 | 0.8266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2132**, F-statistic = **17.41** (p = **3.97e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2740** | 2.0122 | ±4.0243 | **+24.985** | **8.87e-138** | *** |
| Education: graduate level (vs college) | +0.0569 | 0.4830 | ±0.9659 | +0.118 | 0.9063 |  |
| Education: high school or below (vs college) | +0.3280 | 0.6346 | ±1.2691 | +0.517 | 0.6053 |  |
| **Site: UCSD (vs UAB)** | **+3.4510** | 0.5254 | ±1.0509 | **+6.568** | **5.11e-11** | *** |
| Site: UW (vs UAB) | -0.4128 | 0.5239 | ±1.0478 | -0.788 | 0.4307 |  |
| **Season: spring (vs autumn)** | **-2.0464** | 0.6031 | ±1.2062 | **-3.393** | **6.91e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3516** | 0.5804 | ±1.1609 | **+2.329** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-5.9782** | 0.6750 | ±1.3499 | **-8.857** | **8.20e-19** | *** |
| **Age (years)** | **-0.0465** | 0.0214 | ±0.0429 | **-2.168** | **0.0302** | * |
| BMI (kg/m2) | -0.0269 | 0.0336 | ±0.0673 | -0.800 | 0.4235 |  |
| Hypertension | -0.2612 | 0.4904 | ±0.9808 | -0.533 | 0.5943 |  |
| **High cholesterol** | **-0.9467** | 0.4678 | ±0.9355 | **-2.024** | **0.0430** | * |
| **Kidney disease** | **+1.3420** | 0.5563 | ±1.1126 | **+2.412** | **0.0159** | * |
| Circulatory disease | -0.1351 | 0.5404 | ±1.0808 | -0.250 | 0.8026 |  |
| Glucose SD, pooled (mg/dL) | -0.0081 | 0.0157 | ±0.0313 | -0.518 | 0.6043 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.22e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2236** | 2.0171 | ±4.0342 | **+24.899** | **7.68e-137** | *** |
| Education: graduate level (vs college) | +0.0643 | 0.4828 | ±0.9655 | +0.133 | 0.8941 |  |
| Education: high school or below (vs college) | +0.3206 | 0.6354 | ±1.2708 | +0.505 | 0.6139 |  |
| **Site: UCSD (vs UAB)** | **+3.4573** | 0.5252 | ±1.0505 | **+6.582** | **4.63e-11** | *** |
| Site: UW (vs UAB) | -0.4056 | 0.5238 | ±1.0475 | -0.774 | 0.4387 |  |
| **Season: spring (vs autumn)** | **-2.0472** | 0.6032 | ±1.2065 | **-3.394** | **6.90e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3530** | 0.5809 | ±1.1618 | **+2.329** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-5.9832** | 0.6744 | ±1.3488 | **-8.872** | **7.20e-19** | *** |
| **Age (years)** | **-0.0468** | 0.0215 | ±0.0430 | **-2.176** | **0.0295** | * |
| BMI (kg/m2) | -0.0273 | 0.0336 | ±0.0673 | -0.811 | 0.4176 |  |
| Hypertension | -0.2614 | 0.4906 | ±0.9812 | -0.533 | 0.5942 |  |
| **High cholesterol** | **-0.9438** | 0.4677 | ±0.9354 | **-2.018** | **0.0436** | * |
| **Kidney disease** | **+1.3280** | 0.5563 | ±1.1126 | **+2.387** | **0.0170** | * |
| Circulatory disease | -0.1387 | 0.5402 | ±1.0805 | -0.257 | 0.7974 |  |
| Avg. daily SD (mg/dL) | -0.0066 | 0.0179 | ±0.0357 | -0.371 | 0.7105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.2265**, Adj R² = **0.2135**, F-statistic = **17.45** (p = **3.31e-38**), Residual SE = **6.186** on **834** df, AIC = **5518.5**, BIC = **5589.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6122** | 2.1463 | ±4.2927 | **+23.581** | **6.08e-123** | *** |
| Education: graduate level (vs college) | +0.0535 | 0.4824 | ±0.9647 | +0.111 | 0.9117 |  |
| Education: high school or below (vs college) | +0.3355 | 0.6330 | ±1.2660 | +0.530 | 0.5961 |  |
| **Site: UCSD (vs UAB)** | **+3.4471** | 0.5221 | ±1.0443 | **+6.602** | **4.06e-11** | *** |
| Site: UW (vs UAB) | -0.4288 | 0.5235 | ±1.0469 | -0.819 | 0.4127 |  |
| **Season: spring (vs autumn)** | **-2.0535** | 0.6035 | ±1.2069 | **-3.403** | **6.67e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3517** | 0.5800 | ±1.1600 | **+2.331** | **0.0198** | * |
| **Season: winter (vs autumn)** | **-5.9850** | 0.6739 | ±1.3479 | **-8.881** | **6.64e-19** | *** |
| **Age (years)** | **-0.0453** | 0.0214 | ±0.0427 | **-2.122** | **0.0339** | * |
| BMI (kg/m2) | -0.0276 | 0.0337 | ±0.0674 | -0.818 | 0.4131 |  |
| Hypertension | -0.2535 | 0.4896 | ±0.9792 | -0.518 | 0.6046 |  |
| **High cholesterol** | **-0.9509** | 0.4674 | ±0.9349 | **-2.034** | **0.0419** | * |
| **Kidney disease** | **+1.3747** | 0.5571 | ±1.1142 | **+2.468** | **0.0136** | * |
| Circulatory disease | -0.1308 | 0.5399 | ±1.0798 | -0.242 | 0.8086 |  |
| CV (%) | -0.0301 | 0.0370 | ±0.0741 | -0.814 | 0.4159 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.41** (p = **4.05e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5964** | 2.0259 | ±4.0518 | **+24.481** | **2.34e-132** | *** |
| Education: graduate level (vs college) | +0.0646 | 0.4830 | ±0.9659 | +0.134 | 0.8936 |  |
| Education: high school or below (vs college) | +0.3209 | 0.6337 | ±1.2673 | +0.506 | 0.6126 |  |
| **Site: UCSD (vs UAB)** | **+3.4600** | 0.5212 | ±1.0424 | **+6.638** | **3.17e-11** | *** |
| Site: UW (vs UAB) | -0.4119 | 0.5232 | ±1.0463 | -0.787 | 0.4311 |  |
| **Season: spring (vs autumn)** | **-2.0498** | 0.6037 | ±1.2073 | **-3.396** | **6.85e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3629** | 0.5801 | ±1.1601 | **+2.350** | **0.0188** | * |
| **Season: winter (vs autumn)** | **-5.9838** | 0.6741 | ±1.3481 | **-8.877** | **6.85e-19** | *** |
| **Age (years)** | **-0.0462** | 0.0214 | ±0.0428 | **-2.160** | **0.0308** | * |
| BMI (kg/m2) | -0.0273 | 0.0338 | ±0.0675 | -0.808 | 0.4191 |  |
| Hypertension | -0.2561 | 0.4898 | ±0.9796 | -0.523 | 0.6010 |  |
| **High cholesterol** | **-0.9433** | 0.4674 | ±0.9349 | **-2.018** | **0.0436** | * |
| **Kidney disease** | **+1.3284** | 0.5548 | ±1.1096 | **+2.394** | **0.0166** | * |
| Circulatory disease | -0.1323 | 0.5401 | ±1.0801 | -0.245 | 0.8065 |  |
| Mean / SD ratio | +0.0790 | 0.1623 | ±0.3246 | +0.487 | 0.6263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.39** (p = **4.42e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8849** | 2.0340 | ±4.0681 | **+24.525** | **7.99e-133** | *** |
| Education: graduate level (vs college) | +0.0728 | 0.4837 | ±0.9674 | +0.150 | 0.8804 |  |
| Education: high school or below (vs college) | +0.3048 | 0.6345 | ±1.2690 | +0.480 | 0.6310 |  |
| **Site: UCSD (vs UAB)** | **+3.4691** | 0.5196 | ±1.0391 | **+6.677** | **2.44e-11** | *** |
| Site: UW (vs UAB) | -0.3993 | 0.5224 | ±1.0449 | -0.764 | 0.4447 |  |
| **Season: spring (vs autumn)** | **-2.0516** | 0.6041 | ±1.2081 | **-3.396** | **6.83e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3608** | 0.5805 | ±1.1610 | **+2.344** | **0.0191** | * |
| **Season: winter (vs autumn)** | **-5.9889** | 0.6738 | ±1.3475 | **-8.889** | **6.18e-19** | *** |
| **Age (years)** | **-0.0471** | 0.0215 | ±0.0431 | **-2.186** | **0.0288** | * |
| BMI (kg/m2) | -0.0273 | 0.0339 | ±0.0678 | -0.804 | 0.4212 |  |
| Hypertension | -0.2579 | 0.4898 | ±0.9796 | -0.527 | 0.5985 |  |
| **High cholesterol** | **-0.9394** | 0.4673 | ±0.9347 | **-2.010** | **0.0444** | * |
| **Kidney disease** | **+1.3023** | 0.5526 | ±1.1053 | **+2.357** | **0.0184** | * |
| Circulatory disease | -0.1404 | 0.5402 | ±1.0805 | -0.260 | 0.7950 |  |
| Avg. daily mean/SD | +0.0261 | 0.1351 | ±0.2701 | +0.193 | 0.8468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2129**, F-statistic = **17.39** (p = **4.46e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9264** | 2.1905 | ±4.3811 | **+22.792** | **5.53e-115** | *** |
| Education: graduate level (vs college) | +0.0844 | 0.4832 | ±0.9663 | +0.175 | 0.8613 |  |
| Education: high school or below (vs college) | +0.2899 | 0.6351 | ±1.2702 | +0.457 | 0.6480 |  |
| **Site: UCSD (vs UAB)** | **+3.4740** | 0.5228 | ±1.0456 | **+6.645** | **3.03e-11** | *** |
| Site: UW (vs UAB) | -0.3851 | 0.5283 | ±1.0566 | -0.729 | 0.4660 |  |
| **Season: spring (vs autumn)** | **-2.0507** | 0.6041 | ±1.2082 | **-3.395** | **6.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3665** | 0.5799 | ±1.1599 | **+2.356** | **0.0185** | * |
| **Season: winter (vs autumn)** | **-5.9895** | 0.6737 | ±1.3473 | **-8.891** | **6.07e-19** | *** |
| **Age (years)** | **-0.0476** | 0.0214 | ±0.0427 | **-2.230** | **0.0258** | * |
| BMI (kg/m2) | -0.0270 | 0.0337 | ±0.0674 | -0.801 | 0.4231 |  |
| Hypertension | -0.2582 | 0.4905 | ±0.9810 | -0.526 | 0.5986 |  |
| **High cholesterol** | **-0.9355** | 0.4672 | ±0.9345 | **-2.002** | **0.0453** | * |
| **Kidney disease** | **+1.2815** | 0.5528 | ±1.1055 | **+2.318** | **0.0204** | * |
| Circulatory disease | -0.1405 | 0.5408 | ±1.0817 | -0.260 | 0.7951 |  |
| MAG (mg/dL/h) | +0.0029 | 0.0213 | ±0.0426 | +0.135 | 0.8928 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.41** (p = **4.06e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3560** | 2.0683 | ±4.1366 | **+24.347** | **6.29e-131** | *** |
| Education: graduate level (vs college) | +0.0588 | 0.4833 | ±0.9666 | +0.122 | 0.9031 |  |
| Education: high school or below (vs college) | +0.3255 | 0.6361 | ±1.2722 | +0.512 | 0.6088 |  |
| **Site: UCSD (vs UAB)** | **+3.4518** | 0.5259 | ±1.0519 | **+6.563** | **5.27e-11** | *** |
| Site: UW (vs UAB) | -0.4088 | 0.5239 | ±1.0478 | -0.780 | 0.4352 |  |
| **Season: spring (vs autumn)** | **-2.0443** | 0.6031 | ±1.2061 | **-3.390** | **6.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3556** | 0.5803 | ±1.1606 | **+2.336** | **0.0195** | * |
| **Season: winter (vs autumn)** | **-5.9801** | 0.6747 | ±1.3493 | **-8.864** | **7.73e-19** | *** |
| **Age (years)** | **-0.0467** | 0.0215 | ±0.0430 | **-2.174** | **0.0297** | * |
| BMI (kg/m2) | -0.0276 | 0.0336 | ±0.0673 | -0.821 | 0.4119 |  |
| Hypertension | -0.2666 | 0.4916 | ±0.9832 | -0.542 | 0.5876 |  |
| **High cholesterol** | **-0.9427** | 0.4674 | ±0.9348 | **-2.017** | **0.0437** | * |
| **Kidney disease** | **+1.3370** | 0.5551 | ±1.1102 | **+2.409** | **0.0160** | * |
| Circulatory disease | -0.1365 | 0.5400 | ±1.0800 | -0.253 | 0.8005 |  |
| Avg. daily range (mg/dL) | -0.0024 | 0.0050 | ±0.0099 | -0.480 | 0.6315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.2265**, Adj R² = **0.2135**, F-statistic = **17.44** (p = **3.39e-38**), Residual SE = **6.186** on **834** df, AIC = **5518.6**, BIC = **5589.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2515** | 1.9639 | ±3.9277 | **+25.588** | **2.07e-144** | *** |
| Education: graduate level (vs college) | +0.0406 | 0.4820 | ±0.9639 | +0.084 | 0.9328 |  |
| Education: high school or below (vs college) | +0.3214 | 0.6352 | ±1.2703 | +0.506 | 0.6128 |  |
| **Site: UCSD (vs UAB)** | **+3.4475** | 0.5225 | ±1.0449 | **+6.599** | **4.15e-11** | *** |
| Site: UW (vs UAB) | -0.4218 | 0.5211 | ±1.0422 | -0.809 | 0.4183 |  |
| **Season: spring (vs autumn)** | **-2.0518** | 0.6032 | ±1.2063 | **-3.402** | **6.69e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3632** | 0.5795 | ±1.1591 | **+2.352** | **0.0187** | * |
| **Season: winter (vs autumn)** | **-5.9684** | 0.6763 | ±1.3527 | **-8.825** | **1.10e-18** | *** |
| **Age (years)** | **-0.0475** | 0.0214 | ±0.0427 | **-2.223** | **0.0262** | * |
| BMI (kg/m2) | -0.0255 | 0.0337 | ±0.0674 | -0.757 | 0.4488 |  |
| Hypertension | -0.2538 | 0.4899 | ±0.9799 | -0.518 | 0.6045 |  |
| **High cholesterol** | **-0.9440** | 0.4673 | ±0.9347 | **-2.020** | **0.0434** | * |
| **Kidney disease** | **+1.3383** | 0.5523 | ±1.1047 | **+2.423** | **0.0154** | * |
| Circulatory disease | -0.1113 | 0.5431 | ±1.0863 | -0.205 | 0.8376 |  |
| SD of daily means (mg/dL) | -0.0205 | 0.0268 | ±0.0535 | -0.767 | 0.4432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.43** (p = **3.65e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.7**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5600** | 2.1212 | ±4.2424 | **+23.364** | **9.91e-121** | *** |
| Education: graduate level (vs college) | +0.0543 | 0.4795 | ±0.9590 | +0.113 | 0.9098 |  |
| Education: high school or below (vs college) | +0.3352 | 0.6388 | ±1.2775 | +0.525 | 0.5997 |  |
| **Site: UCSD (vs UAB)** | **+3.4372** | 0.5275 | ±1.0550 | **+6.516** | **7.22e-11** | *** |
| Site: UW (vs UAB) | -0.4078 | 0.5204 | ±1.0408 | -0.784 | 0.4333 |  |
| **Season: spring (vs autumn)** | **-2.0459** | 0.6028 | ±1.2056 | **-3.394** | **6.89e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3517** | 0.5805 | ±1.1610 | **+2.328** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-5.9713** | 0.6759 | ±1.3519 | **-8.834** | **1.01e-18** | *** |
| **Age (years)** | **-0.0466** | 0.0215 | ±0.0430 | **-2.166** | **0.0303** | * |
| BMI (kg/m2) | -0.0261 | 0.0338 | ±0.0675 | -0.774 | 0.4390 |  |
| Hypertension | -0.2717 | 0.4911 | ±0.9822 | -0.553 | 0.5800 |  |
| **High cholesterol** | **-0.9492** | 0.4676 | ±0.9352 | **-2.030** | **0.0424** | * |
| **Kidney disease** | **+1.3265** | 0.5554 | ±1.1108 | **+2.388** | **0.0169** | * |
| Circulatory disease | -0.1335 | 0.5404 | ±1.0807 | -0.247 | 0.8049 |  |
| Time in range 70-180, pooled (%) | +0.0056 | 0.0089 | ±0.0179 | +0.628 | 0.5297 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.70e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.7**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5730** | 2.1258 | ±4.2516 | **+23.320** | **2.79e-120** | *** |
| Education: graduate level (vs college) | +0.0559 | 0.4796 | ±0.9592 | +0.117 | 0.9072 |  |
| Education: high school or below (vs college) | +0.3351 | 0.6388 | ±1.2776 | +0.525 | 0.5999 |  |
| **Site: UCSD (vs UAB)** | **+3.4373** | 0.5280 | ±1.0560 | **+6.510** | **7.53e-11** | *** |
| Site: UW (vs UAB) | -0.4073 | 0.5204 | ±1.0409 | -0.783 | 0.4339 |  |
| **Season: spring (vs autumn)** | **-2.0451** | 0.6028 | ±1.2056 | **-3.393** | **6.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3537** | 0.5804 | ±1.1608 | **+2.332** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9699** | 0.6763 | ±1.3527 | **-8.827** | **1.08e-18** | *** |
| **Age (years)** | **-0.0466** | 0.0215 | ±0.0431 | **-2.165** | **0.0304** | * |
| BMI (kg/m2) | -0.0261 | 0.0338 | ±0.0675 | -0.774 | 0.4390 |  |
| Hypertension | -0.2716 | 0.4912 | ±0.9823 | -0.553 | 0.5803 |  |
| **High cholesterol** | **-0.9484** | 0.4675 | ±0.9350 | **-2.029** | **0.0425** | * |
| **Kidney disease** | **+1.3265** | 0.5553 | ±1.1106 | **+2.389** | **0.0169** | * |
| Circulatory disease | -0.1337 | 0.5404 | ±1.0807 | -0.247 | 0.8046 |  |
| Avg. daily time in range 70-180 (%) | +0.0054 | 0.0089 | ±0.0178 | +0.606 | 0.5442 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.39** (p = **4.39e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1044** | 1.9571 | ±3.9142 | **+25.601** | **1.47e-144** | *** |
| Education: graduate level (vs college) | +0.0794 | 0.4784 | ±0.9567 | +0.166 | 0.8682 |  |
| Education: high school or below (vs college) | +0.2887 | 0.6352 | ±1.2703 | +0.454 | 0.6495 |  |
| **Site: UCSD (vs UAB)** | **+3.4620** | 0.5201 | ±1.0402 | **+6.657** | **2.80e-11** | *** |
| Site: UW (vs UAB) | -0.4034 | 0.5162 | ±1.0325 | -0.781 | 0.4346 |  |
| **Season: spring (vs autumn)** | **-2.0513** | 0.6042 | ±1.2084 | **-3.395** | **6.86e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3594** | 0.5804 | ±1.1608 | **+2.342** | **0.0192** | * |
| **Season: winter (vs autumn)** | **-5.9970** | 0.6766 | ±1.3532 | **-8.864** | **7.75e-19** | *** |
| **Age (years)** | **-0.0481** | 0.0214 | ±0.0428 | **-2.248** | **0.0246** | * |
| BMI (kg/m2) | -0.0266 | 0.0336 | ±0.0671 | -0.791 | 0.4288 |  |
| Hypertension | -0.2535 | 0.4931 | ±0.9862 | -0.514 | 0.6072 |  |
| **High cholesterol** | **-0.9422** | 0.4676 | ±0.9353 | **-2.015** | **0.0439** | * |
| **Kidney disease** | **+1.2866** | 0.5523 | ±1.1045 | **+2.330** | **0.0198** | * |
| Circulatory disease | -0.1341 | 0.5420 | ±1.0839 | -0.247 | 0.8046 |  |
| Any reading < 54 during wear (0/1) | -0.1076 | 0.5046 | ±1.0093 | -0.213 | 0.8312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2132**, F-statistic = **17.41** (p = **3.91e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.9**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1021** | 1.9484 | ±3.8969 | **+25.714** | **8.18e-146** | *** |
| Education: graduate level (vs college) | +0.0717 | 0.4784 | ±0.9568 | +0.150 | 0.8809 |  |
| Education: high school or below (vs college) | +0.2764 | 0.6339 | ±1.2678 | +0.436 | 0.6628 |  |
| **Site: UCSD (vs UAB)** | **+3.4419** | 0.5214 | ±1.0428 | **+6.601** | **4.08e-11** | *** |
| Site: UW (vs UAB) | -0.4264 | 0.5195 | ±1.0390 | -0.821 | 0.4118 |  |
| **Season: spring (vs autumn)** | **-2.0610** | 0.6047 | ±1.2095 | **-3.408** | **6.54e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3564** | 0.5827 | ±1.1655 | **+2.328** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-6.0002** | 0.6760 | ±1.3521 | **-8.876** | **6.95e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0213 | ±0.0427 | **-2.240** | **0.0251** | * |
| BMI (kg/m2) | -0.0263 | 0.0338 | ±0.0675 | -0.780 | 0.4356 |  |
| Hypertension | -0.2529 | 0.4903 | ±0.9807 | -0.516 | 0.6060 |  |
| **High cholesterol** | **-0.9414** | 0.4679 | ±0.9357 | **-2.012** | **0.0442** | * |
| **Kidney disease** | **+1.2818** | 0.5516 | ±1.1031 | **+2.324** | **0.0201** | * |
| Circulatory disease | -0.1203 | 0.5394 | ±1.0787 | -0.223 | 0.8235 |  |
| Time < 54 (%) | -0.2766 | 0.7618 | ±1.5236 | -0.363 | 0.7166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2265**, Adj R² = **0.2135**, F-statistic = **17.44** (p = **3.39e-38**), Residual SE = **6.186** on **834** df, AIC = **5518.6**, BIC = **5589.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0923** | 1.9382 | ±3.8763 | **+25.845** | **2.75e-147** | *** |
| Education: graduate level (vs college) | +0.0647 | 0.4785 | ±0.9570 | +0.135 | 0.8924 |  |
| Education: high school or below (vs college) | +0.2738 | 0.6338 | ±1.2675 | +0.432 | 0.6657 |  |
| **Site: UCSD (vs UAB)** | **+3.4379** | 0.5192 | ±1.0384 | **+6.622** | **3.55e-11** | *** |
| Site: UW (vs UAB) | -0.4304 | 0.5188 | ±1.0376 | -0.830 | 0.4068 |  |
| **Season: spring (vs autumn)** | **-2.0735** | 0.6050 | ±1.2100 | **-3.427** | **6.09e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3535** | 0.5830 | ±1.1661 | **+2.321** | **0.0203** | * |
| **Season: winter (vs autumn)** | **-6.0018** | 0.6754 | ±1.3507 | **-8.887** | **6.30e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0427 | **-2.219** | **0.0265** | * |
| BMI (kg/m2) | -0.0265 | 0.0337 | ±0.0673 | -0.787 | 0.4313 |  |
| Hypertension | -0.2533 | 0.4902 | ±0.9803 | -0.517 | 0.6054 |  |
| **High cholesterol** | **-0.9485** | 0.4680 | ±0.9360 | **-2.027** | **0.0427** | * |
| **Kidney disease** | **+1.2846** | 0.5522 | ±1.1044 | **+2.326** | **0.0200** | * |
| Circulatory disease | -0.1153 | 0.5392 | ±1.0784 | -0.214 | 0.8308 |  |
| Avg. daily time < 54 (%) | -0.3747 | 0.6872 | ±1.3743 | -0.545 | 0.5855 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.40** (p = **4.31e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0724** | 1.9439 | ±3.8879 | **+25.758** | **2.60e-146** | *** |
| Education: graduate level (vs college) | +0.0723 | 0.4786 | ±0.9572 | +0.151 | 0.8799 |  |
| Education: high school or below (vs college) | +0.2949 | 0.6348 | ±1.2697 | +0.465 | 0.6422 |  |
| **Site: UCSD (vs UAB)** | **+3.4590** | 0.5215 | ±1.0430 | **+6.633** | **3.30e-11** | *** |
| Site: UW (vs UAB) | -0.4047 | 0.5166 | ±1.0331 | -0.784 | 0.4333 |  |
| **Season: spring (vs autumn)** | **-2.0603** | 0.6044 | ±1.2088 | **-3.409** | **6.53e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3558** | 0.5816 | ±1.1631 | **+2.331** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9987** | 0.6774 | ±1.3549 | **-8.855** | **8.35e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0428 | **-2.217** | **0.0267** | * |
| BMI (kg/m2) | -0.0268 | 0.0337 | ±0.0675 | -0.794 | 0.4274 |  |
| Hypertension | -0.2577 | 0.4909 | ±0.9818 | -0.525 | 0.5996 |  |
| **High cholesterol** | **-0.9382** | 0.4677 | ±0.9354 | **-2.006** | **0.0449** | * |
| **Kidney disease** | **+1.2893** | 0.5524 | ±1.1048 | **+2.334** | **0.0196** | * |
| Circulatory disease | -0.1356 | 0.5402 | ±1.0804 | -0.251 | 0.8018 |  |
| Time 54-69, pooled (%) | -0.0425 | 0.1797 | ±0.3594 | -0.237 | 0.8128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2132**, F-statistic = **17.41** (p = **3.95e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0688** | 1.9400 | ±3.8801 | **+25.808** | **7.20e-147** | *** |
| Education: graduate level (vs college) | +0.0664 | 0.4788 | ±0.9577 | +0.139 | 0.8898 |  |
| Education: high school or below (vs college) | +0.2966 | 0.6350 | ±1.2700 | +0.467 | 0.6404 |  |
| **Site: UCSD (vs UAB)** | **+3.4521** | 0.5211 | ±1.0423 | **+6.624** | **3.49e-11** | *** |
| Site: UW (vs UAB) | -0.4128 | 0.5170 | ±1.0340 | -0.798 | 0.4246 |  |
| **Season: spring (vs autumn)** | **-2.0669** | 0.6043 | ±1.2087 | **-3.420** | **6.26e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3523** | 0.5812 | ±1.1625 | **+2.327** | **0.0200** | * |
| **Season: winter (vs autumn)** | **-6.0041** | 0.6772 | ±1.3545 | **-8.866** | **7.60e-19** | *** |
| **Age (years)** | **-0.0471** | 0.0214 | ±0.0428 | **-2.199** | **0.0279** | * |
| BMI (kg/m2) | -0.0266 | 0.0337 | ±0.0674 | -0.789 | 0.4298 |  |
| Hypertension | -0.2565 | 0.4907 | ±0.9814 | -0.523 | 0.6012 |  |
| **High cholesterol** | **-0.9400** | 0.4677 | ±0.9353 | **-2.010** | **0.0444** | * |
| **Kidney disease** | **+1.2881** | 0.5520 | ±1.1040 | **+2.333** | **0.0196** | * |
| Circulatory disease | -0.1336 | 0.5401 | ±1.0802 | -0.247 | 0.8046 |  |
| Avg. daily time 54-69 (%) | -0.0731 | 0.1709 | ±0.3418 | -0.428 | 0.6690 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.21e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0800** | 1.9449 | ±3.8897 | **+25.750** | **3.23e-146** | *** |
| Education: graduate level (vs college) | +0.0709 | 0.4786 | ±0.9571 | +0.148 | 0.8823 |  |
| Education: high school or below (vs college) | +0.2919 | 0.6341 | ±1.2682 | +0.460 | 0.6452 |  |
| **Site: UCSD (vs UAB)** | **+3.4540** | 0.5217 | ±1.0434 | **+6.621** | **3.57e-11** | *** |
| Site: UW (vs UAB) | -0.4105 | 0.5166 | ±1.0332 | -0.795 | 0.4268 |  |
| **Season: spring (vs autumn)** | **-2.0624** | 0.6046 | ±1.2091 | **-3.411** | **6.46e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3546** | 0.5814 | ±1.1628 | **+2.330** | **0.0198** | * |
| **Season: winter (vs autumn)** | **-6.0008** | 0.6775 | ±1.3549 | **-8.858** | **8.16e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0428 | **-2.219** | **0.0265** | * |
| BMI (kg/m2) | -0.0267 | 0.0337 | ±0.0675 | -0.790 | 0.4293 |  |
| Hypertension | -0.2566 | 0.4909 | ±0.9817 | -0.523 | 0.6011 |  |
| **High cholesterol** | **-0.9390** | 0.4677 | ±0.9353 | **-2.008** | **0.0447** | * |
| **Kidney disease** | **+1.2881** | 0.5522 | ±1.1043 | **+2.333** | **0.0197** | * |
| Circulatory disease | -0.1321 | 0.5399 | ±1.0798 | -0.245 | 0.8067 |  |
| Time < 70 (%) | -0.0442 | 0.1477 | ±0.2953 | -0.300 | 0.7645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.76e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0750** | 1.9393 | ±3.8787 | **+25.821** | **5.22e-147** | *** |
| Education: graduate level (vs college) | +0.0640 | 0.4788 | ±0.9575 | +0.134 | 0.8937 |  |
| Education: high school or below (vs college) | +0.2925 | 0.6342 | ±1.2685 | +0.461 | 0.6446 |  |
| **Site: UCSD (vs UAB)** | **+3.4464** | 0.5209 | ±1.0418 | **+6.616** | **3.68e-11** | *** |
| Site: UW (vs UAB) | -0.4193 | 0.5171 | ±1.0342 | -0.811 | 0.4174 |  |
| **Season: spring (vs autumn)** | **-2.0708** | 0.6045 | ±1.2090 | **-3.426** | **6.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3509** | 0.5813 | ±1.1626 | **+2.324** | **0.0201** | * |
| **Season: winter (vs autumn)** | **-6.0061** | 0.6772 | ±1.3543 | **-8.869** | **7.35e-19** | *** |
| **Age (years)** | **-0.0470** | 0.0214 | ±0.0428 | **-2.198** | **0.0279** | * |
| BMI (kg/m2) | -0.0265 | 0.0337 | ±0.0674 | -0.787 | 0.4310 |  |
| Hypertension | -0.2554 | 0.4906 | ±0.9812 | -0.521 | 0.6026 |  |
| **High cholesterol** | **-0.9422** | 0.4676 | ±0.9353 | **-2.015** | **0.0439** | * |
| **Kidney disease** | **+1.2873** | 0.5519 | ±1.1039 | **+2.332** | **0.0197** | * |
| Circulatory disease | -0.1289 | 0.5397 | ±1.0794 | -0.239 | 0.8112 |  |
| Avg. daily time < 70 (%) | -0.0712 | 0.1380 | ±0.2760 | -0.516 | 0.6060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.17e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5532** | 2.4328 | ±4.8656 | **+20.369** | **3.16e-92** | *** |
| Education: graduate level (vs college) | +0.0618 | 0.4787 | ±0.9574 | +0.129 | 0.8972 |  |
| Education: high school or below (vs college) | +0.3164 | 0.6394 | ±1.2787 | +0.495 | 0.6207 |  |
| **Site: UCSD (vs UAB)** | **+3.4550** | 0.5242 | ±1.0483 | **+6.592** | **4.35e-11** | *** |
| Site: UW (vs UAB) | -0.4093 | 0.5232 | ±1.0464 | -0.782 | 0.4340 |  |
| **Season: spring (vs autumn)** | **-2.0535** | 0.6043 | ±1.2086 | **-3.398** | **6.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3447** | 0.5809 | ±1.1617 | **+2.315** | **0.0206** | * |
| **Season: winter (vs autumn)** | **-5.9869** | 0.6743 | ±1.3487 | **-8.878** | **6.79e-19** | *** |
| **Age (years)** | **-0.0479** | 0.0214 | ±0.0427 | **-2.240** | **0.0251** | * |
| BMI (kg/m2) | -0.0266 | 0.0338 | ±0.0677 | -0.787 | 0.4312 |  |
| Hypertension | -0.2574 | 0.4898 | ±0.9795 | -0.526 | 0.5992 |  |
| **High cholesterol** | **-0.9413** | 0.4675 | ±0.9349 | **-2.014** | **0.0440** | * |
| **Kidney disease** | **+1.3055** | 0.5543 | ±1.1086 | **+2.355** | **0.0185** | * |
| Circulatory disease | -0.1372 | 0.5404 | ±1.0808 | -0.254 | 0.7996 |  |
| Time 54-250, pooled (%) | +0.0056 | 0.0145 | ±0.0291 | +0.383 | 0.7018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.17e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5421** | 2.4742 | ±4.9485 | **+20.023** | **3.46e-89** | *** |
| Education: graduate level (vs college) | +0.0620 | 0.4788 | ±0.9575 | +0.130 | 0.8969 |  |
| Education: high school or below (vs college) | +0.3163 | 0.6396 | ±1.2792 | +0.495 | 0.6209 |  |
| **Site: UCSD (vs UAB)** | **+3.4548** | 0.5243 | ±1.0486 | **+6.590** | **4.41e-11** | *** |
| Site: UW (vs UAB) | -0.4087 | 0.5231 | ±1.0461 | -0.781 | 0.4347 |  |
| **Season: spring (vs autumn)** | **-2.0526** | 0.6042 | ±1.2084 | **-3.397** | **6.81e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3459** | 0.5805 | ±1.1610 | **+2.318** | **0.0204** | * |
| **Season: winter (vs autumn)** | **-5.9859** | 0.6745 | ±1.3491 | **-8.874** | **7.06e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0214 | ±0.0427 | **-2.236** | **0.0254** | * |
| BMI (kg/m2) | -0.0266 | 0.0338 | ±0.0677 | -0.786 | 0.4316 |  |
| Hypertension | -0.2578 | 0.4898 | ±0.9796 | -0.526 | 0.5986 |  |
| **High cholesterol** | **-0.9413** | 0.4674 | ±0.9348 | **-2.014** | **0.0440** | * |
| **Kidney disease** | **+1.3066** | 0.5545 | ±1.1091 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.1366 | 0.5404 | ±1.0807 | -0.253 | 0.8005 |  |
| Avg. daily time 54-250 (%) | +0.0056 | 0.0149 | ±0.0299 | +0.376 | 0.7069 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.43** (p = **3.66e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.7**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0743** | 1.9428 | ±3.8856 | **+25.775** | **1.71e-146** | *** |
| Education: graduate level (vs college) | +0.0684 | 0.4789 | ±0.9579 | +0.143 | 0.8864 |  |
| Education: high school or below (vs college) | +0.3254 | 0.6354 | ±1.2708 | +0.512 | 0.6086 |  |
| **Site: UCSD (vs UAB)** | **+3.4442** | 0.5247 | ±1.0493 | **+6.565** | **5.22e-11** | *** |
| Site: UW (vs UAB) | -0.3880 | 0.5177 | ±1.0355 | -0.749 | 0.4536 |  |
| **Season: spring (vs autumn)** | **-2.0362** | 0.6019 | ±1.2038 | **-3.383** | **7.17e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3754** | 0.5802 | ±1.1605 | **+2.370** | **0.0178** | * |
| **Season: winter (vs autumn)** | **-5.9623** | 0.6767 | ±1.3534 | **-8.811** | **1.24e-18** | *** |
| **Age (years)** | **-0.0457** | 0.0216 | ±0.0432 | **-2.114** | **0.0346** | * |
| BMI (kg/m2) | -0.0262 | 0.0337 | ±0.0673 | -0.779 | 0.4362 |  |
| Hypertension | -0.2832 | 0.4929 | ±0.9859 | -0.575 | 0.5656 |  |
| **High cholesterol** | **-0.9493** | 0.4675 | ±0.9351 | **-2.030** | **0.0423** | * |
| **Kidney disease** | **+1.3227** | 0.5542 | ±1.1083 | **+2.387** | **0.0170** | * |
| Circulatory disease | -0.1358 | 0.5406 | ±1.0812 | -0.251 | 0.8017 |  |
| Time 181-250, pooled (%) | -0.0092 | 0.0144 | ±0.0288 | -0.635 | 0.5255 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.79e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0748** | 1.9426 | ±3.8852 | **+25.777** | **1.60e-146** | *** |
| Education: graduate level (vs college) | +0.0702 | 0.4789 | ±0.9579 | +0.147 | 0.8835 |  |
| Education: high school or below (vs college) | +0.3246 | 0.6353 | ±1.2706 | +0.511 | 0.6093 |  |
| **Site: UCSD (vs UAB)** | **+3.4451** | 0.5253 | ±1.0506 | **+6.558** | **5.44e-11** | *** |
| Site: UW (vs UAB) | -0.3898 | 0.5180 | ±1.0359 | -0.753 | 0.4517 |  |
| **Season: spring (vs autumn)** | **-2.0375** | 0.6020 | ±1.2040 | **-3.384** | **7.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3743** | 0.5802 | ±1.1604 | **+2.369** | **0.0179** | * |
| **Season: winter (vs autumn)** | **-5.9635** | 0.6770 | ±1.3539 | **-8.809** | **1.26e-18** | *** |
| **Age (years)** | **-0.0460** | 0.0216 | ±0.0432 | **-2.129** | **0.0332** | * |
| BMI (kg/m2) | -0.0263 | 0.0337 | ±0.0673 | -0.780 | 0.4354 |  |
| Hypertension | -0.2806 | 0.4929 | ±0.9859 | -0.569 | 0.5692 |  |
| **High cholesterol** | **-0.9475** | 0.4675 | ±0.9350 | **-2.027** | **0.0427** | * |
| **Kidney disease** | **+1.3201** | 0.5539 | ±1.1079 | **+2.383** | **0.0172** | * |
| Circulatory disease | -0.1369 | 0.5406 | ±1.0812 | -0.253 | 0.8001 |  |
| Avg. daily time 181-250 (%) | -0.0082 | 0.0141 | ±0.0283 | -0.580 | 0.5619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.73e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1156** | 1.9411 | ±3.8822 | **+25.818** | **5.59e-147** | *** |
| Education: graduate level (vs college) | +0.0568 | 0.4794 | ±0.9588 | +0.119 | 0.9057 |  |
| Education: high school or below (vs college) | +0.3331 | 0.6384 | ±1.2768 | +0.522 | 0.6018 |  |
| **Site: UCSD (vs UAB)** | **+3.4412** | 0.5267 | ±1.0534 | **+6.534** | **6.41e-11** | *** |
| Site: UW (vs UAB) | -0.4048 | 0.5202 | ±1.0404 | -0.778 | 0.4364 |  |
| **Season: spring (vs autumn)** | **-2.0448** | 0.6028 | ±1.2055 | **-3.392** | **6.93e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3533** | 0.5805 | ±1.1610 | **+2.331** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9711** | 0.6763 | ±1.3525 | **-8.830** | **1.05e-18** | *** |
| **Age (years)** | **-0.0467** | 0.0215 | ±0.0430 | **-2.171** | **0.0299** | * |
| BMI (kg/m2) | -0.0262 | 0.0338 | ±0.0675 | -0.776 | 0.4375 |  |
| Hypertension | -0.2713 | 0.4913 | ±0.9826 | -0.552 | 0.5808 |  |
| **High cholesterol** | **-0.9482** | 0.4676 | ±0.9352 | **-2.028** | **0.0426** | * |
| **Kidney disease** | **+1.3243** | 0.5552 | ±1.1103 | **+2.385** | **0.0171** | * |
| Circulatory disease | -0.1349 | 0.5405 | ±1.0809 | -0.250 | 0.8028 |  |
| Time > 180 (%) | -0.0053 | 0.0089 | ±0.0177 | -0.595 | 0.5521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.81e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1077** | 1.9409 | ±3.8818 | **+25.817** | **5.75e-147** | *** |
| Education: graduate level (vs college) | +0.0590 | 0.4794 | ±0.9589 | +0.123 | 0.9020 |  |
| Education: high school or below (vs college) | +0.3317 | 0.6384 | ±1.2768 | +0.520 | 0.6034 |  |
| **Site: UCSD (vs UAB)** | **+3.4419** | 0.5272 | ±1.0545 | **+6.528** | **6.66e-11** | *** |
| Site: UW (vs UAB) | -0.4042 | 0.5202 | ±1.0405 | -0.777 | 0.4372 |  |
| **Season: spring (vs autumn)** | **-2.0442** | 0.6027 | ±1.2055 | **-3.391** | **6.95e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3553** | 0.5804 | ±1.1608 | **+2.335** | **0.0195** | * |
| **Season: winter (vs autumn)** | **-5.9705** | 0.6767 | ±1.3534 | **-8.823** | **1.12e-18** | *** |
| **Age (years)** | **-0.0467** | 0.0215 | ±0.0430 | **-2.173** | **0.0298** | * |
| BMI (kg/m2) | -0.0262 | 0.0338 | ±0.0676 | -0.777 | 0.4373 |  |
| Hypertension | -0.2708 | 0.4914 | ±0.9828 | -0.551 | 0.5816 |  |
| **High cholesterol** | **-0.9470** | 0.4675 | ±0.9350 | **-2.026** | **0.0428** | * |
| **Kidney disease** | **+1.3233** | 0.5552 | ±1.1103 | **+2.384** | **0.0171** | * |
| Circulatory disease | -0.1351 | 0.5405 | ±1.0810 | -0.250 | 0.8026 |  |
| Avg. daily time > 180 (%) | -0.0049 | 0.0088 | ±0.0177 | -0.557 | 0.5777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2272**, Adj R² = **0.2142**, F-statistic = **17.51** (p = **2.36e-38**), Residual SE = **6.184** on **834** df, AIC = **5517.8**, BIC = **5588.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1451** | 1.9407 | ±3.8813 | **+25.839** | **3.21e-147** | *** |
| Education: graduate level (vs college) | +0.0284 | 0.4800 | ±0.9600 | +0.059 | 0.9529 |  |
| Education: high school or below (vs college) | +0.3609 | 0.6389 | ±1.2778 | +0.565 | 0.5722 |  |
| **Site: UCSD (vs UAB)** | **+3.4109** | 0.5275 | ±1.0549 | **+6.467** | **1.00e-10** | *** |
| Site: UW (vs UAB) | -0.4092 | 0.5193 | ±1.0386 | -0.788 | 0.4307 |  |
| **Season: spring (vs autumn)** | **-2.0364** | 0.6016 | ±1.2032 | **-3.385** | **7.11e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3430** | 0.5801 | ±1.1602 | **+2.315** | **0.0206** | * |
| **Season: winter (vs autumn)** | **-5.9530** | 0.6762 | ±1.3525 | **-8.803** | **1.33e-18** | *** |
| **Age (years)** | **-0.0472** | 0.0214 | ±0.0429 | **-2.202** | **0.0277** | * |
| BMI (kg/m2) | -0.0239 | 0.0339 | ±0.0678 | -0.705 | 0.4806 |  |
| Hypertension | -0.2837 | 0.4912 | ±0.9825 | -0.578 | 0.5636 |  |
| **High cholesterol** | **-0.9590** | 0.4669 | ±0.9338 | **-2.054** | **0.0400** | * |
| **Kidney disease** | **+1.3438** | 0.5544 | ±1.1088 | **+2.424** | **0.0154** | * |
| Circulatory disease | -0.1275 | 0.5397 | ±1.0794 | -0.236 | 0.8133 |  |
| Nocturnal time > 180 (%) | -0.0094 | 0.0084 | ±0.0167 | -1.121 | 0.2623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2286**, Adj R² = **0.2157**, F-statistic = **17.65** (p = **1.13e-38**), Residual SE = **6.178** on **834** df, AIC = **5516.2**, BIC = **5587.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2821** | 1.9487 | ±3.8974 | **+25.803** | **8.29e-147** | *** |
| Education: graduate level (vs college) | +0.0042 | 0.4810 | ±0.9620 | +0.009 | 0.9930 |  |
| Education: high school or below (vs college) | +0.3353 | 0.6336 | ±1.2673 | +0.529 | 0.5967 |  |
| **Site: UCSD (vs UAB)** | **+3.4279** | 0.5208 | ±1.0416 | **+6.582** | **4.64e-11** | *** |
| Site: UW (vs UAB) | -0.3685 | 0.5165 | ±1.0329 | -0.713 | 0.4756 |  |
| **Season: spring (vs autumn)** | **-2.0605** | 0.6019 | ±1.2038 | **-3.423** | **6.18e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3654** | 0.5795 | ±1.1590 | **+2.356** | **0.0185** | * |
| **Season: winter (vs autumn)** | **-5.9827** | 0.6732 | ±1.3464 | **-8.887** | **6.29e-19** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0431 | -1.922 | 0.0547 | . |
| BMI (kg/m2) | -0.0291 | 0.0333 | ±0.0667 | -0.874 | 0.3821 |  |
| Hypertension | -0.2990 | 0.4931 | ±0.9861 | -0.606 | 0.5443 |  |
| **High cholesterol** | **-0.9488** | 0.4655 | ±0.9311 | **-2.038** | **0.0415** | * |
| **Kidney disease** | **+1.3801** | 0.5527 | ±1.1054 | **+2.497** | **0.0125** | * |
| Circulatory disease | -0.1538 | 0.5390 | ±1.0780 | -0.285 | 0.7753 |  |
| Any reading > 250 during wear (0/1) | -0.7738 | 0.4632 | ±0.9264 | -1.670 | 0.0948 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.19e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1069** | 1.9360 | ±3.8721 | **+25.881** | **1.08e-147** | *** |
| Education: graduate level (vs college) | +0.0627 | 0.4787 | ±0.9573 | +0.131 | 0.8959 |  |
| Education: high school or below (vs college) | +0.3159 | 0.6394 | ±1.2788 | +0.494 | 0.6212 |  |
| **Site: UCSD (vs UAB)** | **+3.4562** | 0.5239 | ±1.0478 | **+6.597** | **4.20e-11** | *** |
| Site: UW (vs UAB) | -0.4080 | 0.5230 | ±1.0460 | -0.780 | 0.4353 |  |
| **Season: spring (vs autumn)** | **-2.0531** | 0.6043 | ±1.2086 | **-3.398** | **6.80e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3455** | 0.5809 | ±1.1617 | **+2.316** | **0.0205** | * |
| **Season: winter (vs autumn)** | **-5.9868** | 0.6744 | ±1.3487 | **-8.878** | **6.84e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0214 | ±0.0427 | **-2.239** | **0.0252** | * |
| BMI (kg/m2) | -0.0267 | 0.0338 | ±0.0677 | -0.788 | 0.4308 |  |
| Hypertension | -0.2576 | 0.4898 | ±0.9795 | -0.526 | 0.5989 |  |
| **High cholesterol** | **-0.9410** | 0.4674 | ±0.9349 | **-2.013** | **0.0441** | * |
| **Kidney disease** | **+1.3050** | 0.5542 | ±1.1085 | **+2.355** | **0.0185** | * |
| Circulatory disease | -0.1377 | 0.5405 | ±1.0810 | -0.255 | 0.7988 |  |
| Time > 250 (%) | -0.0053 | 0.0145 | ±0.0291 | -0.367 | 0.7133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.20e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1007** | 1.9357 | ±3.8715 | **+25.882** | **1.06e-147** | *** |
| Education: graduate level (vs college) | +0.0632 | 0.4787 | ±0.9574 | +0.132 | 0.8950 |  |
| Education: high school or below (vs college) | +0.3154 | 0.6396 | ±1.2792 | +0.493 | 0.6220 |  |
| **Site: UCSD (vs UAB)** | **+3.4562** | 0.5241 | ±1.0482 | **+6.594** | **4.27e-11** | *** |
| Site: UW (vs UAB) | -0.4072 | 0.5229 | ±1.0458 | -0.779 | 0.4361 |  |
| **Season: spring (vs autumn)** | **-2.0521** | 0.6042 | ±1.2083 | **-3.397** | **6.82e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3470** | 0.5805 | ±1.1609 | **+2.321** | **0.0203** | * |
| **Season: winter (vs autumn)** | **-5.9859** | 0.6746 | ±1.3492 | **-8.873** | **7.11e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0214 | ±0.0427 | **-2.236** | **0.0254** | * |
| BMI (kg/m2) | -0.0266 | 0.0338 | ±0.0677 | -0.787 | 0.4312 |  |
| Hypertension | -0.2580 | 0.4898 | ±0.9796 | -0.527 | 0.5984 |  |
| **High cholesterol** | **-0.9409** | 0.4674 | ±0.9348 | **-2.013** | **0.0441** | * |
| **Kidney disease** | **+1.3057** | 0.5545 | ±1.1090 | **+2.355** | **0.0185** | * |
| Circulatory disease | -0.1372 | 0.5405 | ±1.0809 | -0.254 | 0.7997 |  |
| Avg. daily time > 250 (%) | -0.0053 | 0.0149 | ±0.0299 | -0.354 | 0.7231 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.0712**, Adj R² = **0.0567**, F-statistic = **4.92** (p = **2.22e-08**), Residual SE = **17.168** on **835** df, AIC = **7250.7**, BIC = **7317.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5407** | 6.4186 | ±12.8371 | **+19.559** | **3.46e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2550** | 1.2468 | ±2.4937 | **-2.611** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+5.2031** | 1.9923 | ±3.9847 | **+2.612** | **0.0090** | ** |
| **Site: UCSD (vs UAB)** | **+3.1181** | 1.5346 | ±3.0692 | **+2.032** | **0.0422** | * |
| Site: UW (vs UAB) | -1.1792 | 1.4059 | ±2.8117 | -0.839 | 0.4016 |  |
| Season: spring (vs autumn) | +2.5114 | 1.5082 | ±3.0164 | +1.665 | 0.0959 | . |
| Season: summer (vs autumn) | +2.6492 | 1.6239 | ±3.2478 | +1.631 | 0.1028 |  |
| **Season: winter (vs autumn)** | **+6.0552** | 1.9047 | ±3.8095 | **+3.179** | **0.0015** | ** |
| Age (years) | -0.1216 | 0.0672 | ±0.1344 | -1.809 | 0.0704 | . |
| BMI (kg/m2) | +0.1767 | 0.0989 | ±0.1977 | +1.787 | 0.0739 | . |
| Hypertension | +0.6411 | 1.4360 | ±2.8720 | +0.446 | 0.6553 |  |
| High cholesterol | +1.1973 | 1.3271 | ±2.6542 | +0.902 | 0.3669 |  |
| Kidney disease | -2.1222 | 1.5943 | ±3.1887 | -1.331 | 0.1832 |  |
| Circulatory disease | -0.0933 | 1.5859 | ±3.1718 | -0.059 | 0.9531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.0738**, Adj R² = **0.0582**, F-statistic = **4.74** (p = **1.98e-08**), Residual SE = **17.154** on **834** df, AIC = **7250.3**, BIC = **7321.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.8444** | 7.0824 | ±14.1649 | **+18.333** | **4.49e-75** | *** |
| **Education: graduate level (vs college)** | **-3.4278** | 1.2323 | ±2.4645 | **-2.782** | **0.0054** | ** |
| **Education: high school or below (vs college)** | **+5.4899** | 2.0087 | ±4.0174 | **+2.733** | **0.0063** | ** |
| Site: UCSD (vs UAB) | +2.9965 | 1.5360 | ±3.0721 | +1.951 | 0.0511 | . |
| Site: UW (vs UAB) | -1.2808 | 1.4032 | ±2.8064 | -0.913 | 0.3614 |  |
| Season: spring (vs autumn) | +2.4411 | 1.5095 | ±3.0190 | +1.617 | 0.1058 |  |
| Season: summer (vs autumn) | +2.5514 | 1.6261 | ±3.2522 | +1.569 | 0.1166 |  |
| **Season: winter (vs autumn)** | **+6.1031** | 1.8961 | ±3.7923 | **+3.219** | **0.0013** | ** |
| Age (years) | -0.1178 | 0.0675 | ±0.1350 | -1.746 | 0.0808 | . |
| BMI (kg/m2) | +0.1873 | 0.0986 | ±0.1971 | +1.900 | 0.0574 | . |
| Hypertension | +0.6478 | 1.4367 | ±2.8734 | +0.451 | 0.6520 |  |
| High cholesterol | +1.1952 | 1.3239 | ±2.6478 | +0.903 | 0.3666 |  |
| Kidney disease | -2.0713 | 1.5891 | ±3.1782 | -1.303 | 0.1924 |  |
| Circulatory disease | -0.0595 | 1.5866 | ±3.1732 | -0.038 | 0.9701 |  |
| HbA1c (%) | -0.7117 | 0.5220 | ±1.0441 | -1.363 | 0.1728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.0724**, Adj R² = **0.0568**, F-statistic = **4.65** (p = **3.28e-08**), Residual SE = **17.167** on **834** df, AIC = **7251.6**, BIC = **7322.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.6598** | 7.0311 | ±14.0623 | **+18.156** | **1.14e-73** | *** |
| **Education: graduate level (vs college)** | **-3.3582** | 1.2329 | ±2.4658 | **-2.724** | **0.0065** | ** |
| **Education: high school or below (vs college)** | **+5.3637** | 2.0033 | ±4.0066 | **+2.677** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +3.0129 | 1.5496 | ±3.0993 | +1.944 | 0.0519 | . |
| Site: UW (vs UAB) | -1.2271 | 1.4059 | ±2.8118 | -0.873 | 0.3828 |  |
| Season: spring (vs autumn) | +2.5449 | 1.5088 | ±3.0175 | +1.687 | 0.0917 | . |
| Season: summer (vs autumn) | +2.6063 | 1.6290 | ±3.2580 | +1.600 | 0.1096 |  |
| **Season: winter (vs autumn)** | **+6.1379** | 1.8818 | ±3.7637 | **+3.262** | **0.0011** | ** |
| Age (years) | -0.1185 | 0.0672 | ±0.1343 | -1.765 | 0.0776 | . |
| BMI (kg/m2) | +0.1795 | 0.0985 | ±0.1969 | +1.824 | 0.0682 | . |
| Hypertension | +0.6143 | 1.4341 | ±2.8683 | +0.428 | 0.6684 |  |
| High cholesterol | +1.1618 | 1.3231 | ±2.6462 | +0.878 | 0.3799 |  |
| Kidney disease | -1.9818 | 1.5952 | ±3.1904 | -1.242 | 0.2141 |  |
| Circulatory disease | -0.0753 | 1.5883 | ±3.1766 | -0.047 | 0.9622 |  |
| Mean glucose (mg/dL) | -0.0153 | 0.0159 | ±0.0318 | -0.958 | 0.3382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.0724**, Adj R² = **0.0568**, F-statistic = **4.65** (p = **3.28e-08**), Residual SE = **17.167** on **834** df, AIC = **7251.6**, BIC = **7322.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.7704** | 8.1963 | ±16.3926 | **+15.833** | **1.85e-56** | *** |
| **Education: graduate level (vs college)** | **-3.3582** | 1.2329 | ±2.4658 | **-2.724** | **0.0065** | ** |
| **Education: high school or below (vs college)** | **+5.3637** | 2.0033 | ±4.0066 | **+2.677** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +3.0129 | 1.5496 | ±3.0993 | +1.944 | 0.0519 | . |
| Site: UW (vs UAB) | -1.2271 | 1.4059 | ±2.8118 | -0.873 | 0.3828 |  |
| Season: spring (vs autumn) | +2.5449 | 1.5088 | ±3.0175 | +1.687 | 0.0917 | . |
| Season: summer (vs autumn) | +2.6063 | 1.6290 | ±3.2580 | +1.600 | 0.1096 |  |
| **Season: winter (vs autumn)** | **+6.1379** | 1.8818 | ±3.7637 | **+3.262** | **0.0011** | ** |
| Age (years) | -0.1185 | 0.0672 | ±0.1343 | -1.765 | 0.0776 | . |
| BMI (kg/m2) | +0.1795 | 0.0985 | ±0.1969 | +1.824 | 0.0682 | . |
| Hypertension | +0.6143 | 1.4341 | ±2.8683 | +0.428 | 0.6684 |  |
| High cholesterol | +1.1618 | 1.3231 | ±2.6462 | +0.878 | 0.3799 |  |
| Kidney disease | -1.9818 | 1.5952 | ±3.1904 | -1.242 | 0.2141 |  |
| Circulatory disease | -0.0753 | 1.5883 | ±3.1766 | -0.047 | 0.9622 |  |
| GMI (%) | -0.6376 | 0.6657 | ±1.3315 | -0.958 | 0.3382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.0731**, Adj R² = **0.0575**, F-statistic = **4.69** (p = **2.59e-08**), Residual SE = **17.161** on **834** df, AIC = **7251.0**, BIC = **7322.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.1173** | 7.2043 | ±14.4086 | **+17.783** | **9.49e-71** | *** |
| **Education: graduate level (vs college)** | **-3.3814** | 1.2343 | ±2.4687 | **-2.739** | **0.0062** | ** |
| **Education: high school or below (vs college)** | **+5.3931** | 1.9889 | ±3.9778 | **+2.712** | **0.0067** | ** |
| Site: UCSD (vs UAB) | +2.9942 | 1.5491 | ±3.0983 | +1.933 | 0.0533 | . |
| Site: UW (vs UAB) | -1.1939 | 1.4072 | ±2.8143 | -0.848 | 0.3962 |  |
| Season: spring (vs autumn) | +2.5764 | 1.5076 | ±3.0152 | +1.709 | 0.0875 | . |
| Season: summer (vs autumn) | +2.6039 | 1.6277 | ±3.2555 | +1.600 | 0.1097 |  |
| **Season: winter (vs autumn)** | **+6.1696** | 1.8768 | ±3.7535 | **+3.287** | **0.0010** | ** |
| Age (years) | -0.1218 | 0.0676 | ±0.1351 | -1.803 | 0.0713 | . |
| BMI (kg/m2) | +0.1846 | 0.0980 | ±0.1960 | +1.884 | 0.0595 | . |
| Hypertension | +0.5937 | 1.4319 | ±2.8638 | +0.415 | 0.6784 |  |
| High cholesterol | +1.1666 | 1.3223 | ±2.6446 | +0.882 | 0.3777 |  |
| Kidney disease | -2.0103 | 1.5980 | ±3.1960 | -1.258 | 0.2084 |  |
| Circulatory disease | -0.0729 | 1.5870 | ±3.1739 | -0.046 | 0.9633 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0186 | 0.0177 | ±0.0353 | -1.053 | 0.2922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.0712**, Adj R² = **0.0556**, F-statistic = **4.57** (p = **5.09e-08**), Residual SE = **17.178** on **834** df, AIC = **7252.7**, BIC = **7323.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3967** | 6.4739 | ±12.9477 | **+19.370** | **1.39e-83** | *** |
| **Education: graduate level (vs college)** | **-3.2403** | 1.2385 | ±2.4771 | **-2.616** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+5.1811** | 2.0078 | ±4.0156 | **+2.581** | **0.0099** | ** |
| **Site: UCSD (vs UAB)** | **+3.1311** | 1.5534 | ±3.1068 | **+2.016** | **0.0438** | * |
| Site: UW (vs UAB) | -1.1661 | 1.4045 | ±2.8090 | -0.830 | 0.4064 |  |
| Season: spring (vs autumn) | +2.5086 | 1.5106 | ±3.0211 | +1.661 | 0.0968 | . |
| Season: summer (vs autumn) | +2.6563 | 1.6267 | ±3.2534 | +1.633 | 0.1025 |  |
| **Season: winter (vs autumn)** | **+6.0476** | 1.9022 | ±3.8044 | **+3.179** | **0.0015** | ** |
| Age (years) | -0.1224 | 0.0680 | ±0.1360 | -1.800 | 0.0719 | . |
| BMI (kg/m2) | +0.1766 | 0.0990 | ±0.1981 | +1.783 | 0.0745 | . |
| Hypertension | +0.6423 | 1.4382 | ±2.8764 | +0.447 | 0.6552 |  |
| High cholesterol | +1.2039 | 1.3210 | ±2.6420 | +0.911 | 0.3621 |  |
| Kidney disease | -2.1577 | 1.5982 | ±3.1963 | -1.350 | 0.1770 |  |
| Circulatory disease | -0.0971 | 1.5879 | ±3.1757 | -0.061 | 0.9512 |  |
| Glucose SD, pooled (mg/dL) | +0.0054 | 0.0496 | ±0.0992 | +0.109 | 0.9130 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.0718**, Adj R² = **0.0562**, F-statistic = **4.61** (p = **4.13e-08**), Residual SE = **17.172** on **834** df, AIC = **7252.2**, BIC = **7323.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6262** | 6.5361 | ±13.0721 | **+19.068** | **4.70e-81** | *** |
| **Education: graduate level (vs college)** | **-3.1739** | 1.2425 | ±2.4850 | **-2.555** | **0.0106** | * |
| **Education: high school or below (vs college)** | **+5.0620** | 2.0031 | ±4.0062 | **+2.527** | **0.0115** | * |
| **Site: UCSD (vs UAB)** | **+3.1914** | 1.5439 | ±3.0877 | **+2.067** | **0.0387** | * |
| Site: UW (vs UAB) | -1.1107 | 1.4047 | ±2.8094 | -0.791 | 0.4291 |  |
| Season: spring (vs autumn) | +2.4924 | 1.5086 | ±3.0171 | +1.652 | 0.0985 | . |
| Season: summer (vs autumn) | +2.7002 | 1.6264 | ±3.2527 | +1.660 | 0.0969 | . |
| **Season: winter (vs autumn)** | **+6.0201** | 1.9067 | ±3.8133 | **+3.157** | **0.0016** | ** |
| Age (years) | -0.1267 | 0.0675 | ±0.1349 | -1.879 | 0.0603 | . |
| BMI (kg/m2) | +0.1784 | 0.0991 | ±0.1983 | +1.799 | 0.0720 | . |
| Hypertension | +0.6518 | 1.4370 | ±2.8739 | +0.454 | 0.6501 |  |
| High cholesterol | +1.2364 | 1.3247 | ±2.6494 | +0.933 | 0.3507 |  |
| Kidney disease | -2.3385 | 1.5984 | ±3.1969 | -1.463 | 0.1435 |  |
| Circulatory disease | -0.1044 | 1.5867 | ±3.1735 | -0.066 | 0.9475 |  |
| Avg. daily SD (mg/dL) | +0.0367 | 0.0489 | ±0.0977 | +0.751 | 0.4527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.0733**, Adj R² = **0.0577**, F-statistic = **4.71** (p = **2.40e-08**), Residual SE = **17.159** on **834** df, AIC = **7250.8**, BIC = **7322.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.9435** | 6.3035 | ±12.6069 | **+19.504** | **1.01e-84** | *** |
| **Education: graduate level (vs college)** | **-3.1356** | 1.2499 | ±2.4998 | **-2.509** | **0.0121** | * |
| **Education: high school or below (vs college)** | **+5.0138** | 2.0041 | ±4.0082 | **+2.502** | **0.0124** | * |
| **Site: UCSD (vs UAB)** | **+3.2279** | 1.5416 | ±3.0832 | **+2.094** | **0.0363** | * |
| Site: UW (vs UAB) | -1.0122 | 1.4021 | ±2.8041 | -0.722 | 0.4703 |  |
| Season: spring (vs autumn) | +2.5249 | 1.5079 | ±3.0158 | +1.674 | 0.0940 | . |
| Season: summer (vs autumn) | +2.6985 | 1.6200 | ±3.2401 | +1.666 | 0.0958 | . |
| **Season: winter (vs autumn)** | **+6.0336** | 1.9110 | ±3.8219 | **+3.157** | **0.0016** | ** |
| Age (years) | -0.1326 | 0.0693 | ±0.1386 | -1.913 | 0.0558 | . |
| BMI (kg/m2) | +0.1796 | 0.0989 | ±0.1977 | +1.817 | 0.0693 | . |
| Hypertension | +0.6133 | 1.4335 | ±2.8670 | +0.428 | 0.6688 |  |
| High cholesterol | +1.2635 | 1.3258 | ±2.6516 | +0.953 | 0.3406 |  |
| Kidney disease | -2.5247 | 1.5931 | ±3.1861 | -1.585 | 0.1130 |  |
| Circulatory disease | -0.1399 | 1.5853 | ±3.1706 | -0.088 | 0.9297 |  |
| CV (%) | +0.1412 | 0.1028 | ±0.2056 | +1.374 | 0.1694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.0743**, Adj R² = **0.0587**, F-statistic = **4.78** (p = **1.64e-08**), Residual SE = **17.149** on **834** df, AIC = **7249.9**, BIC = **7321.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.0910** | 7.4121 | ±14.8242 | **+17.551** | **5.83e-69** | *** |
| **Education: graduate level (vs college)** | **-3.1135** | 1.2480 | ±2.4960 | **-2.495** | **0.0126** | * |
| **Education: high school or below (vs college)** | **+4.9490** | 2.0056 | ±4.0111 | **+2.468** | **0.0136** | * |
| **Site: UCSD (vs UAB)** | **+3.2216** | 1.5375 | ±3.0749 | **+2.095** | **0.0361** | * |
| Site: UW (vs UAB) | -0.9950 | 1.4024 | ±2.8048 | -0.709 | 0.4780 |  |
| Season: spring (vs autumn) | +2.5039 | 1.5080 | ±3.0159 | +1.660 | 0.0968 | . |
| Season: summer (vs autumn) | +2.6430 | 1.6234 | ±3.2468 | +1.628 | 0.1035 |  |
| **Season: winter (vs autumn)** | **+5.9981** | 1.9115 | ±3.8230 | **+3.138** | **0.0017** | ** |
| **Age (years)** | **-0.1361** | 0.0694 | ±0.1388 | **-1.962** | **0.0498** | * |
| BMI (kg/m2) | +0.1798 | 0.0988 | ±0.1977 | +1.819 | 0.0689 | . |
| Hypertension | +0.6081 | 1.4333 | ±2.8666 | +0.424 | 0.6714 |  |
| High cholesterol | +1.2612 | 1.3255 | ±2.6509 | +0.952 | 0.3413 |  |
| Kidney disease | -2.5120 | 1.5979 | ±3.1958 | -1.572 | 0.1159 |  |
| Circulatory disease | -0.1763 | 1.5863 | ±3.1725 | -0.111 | 0.9115 |  |
| Mean / SD ratio | -0.7787 | 0.4434 | ±0.8867 | -1.756 | 0.0790 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.0769**, Adj R² = **0.0614**, F-statistic = **4.96** (p = **6.11e-09**), Residual SE = **17.125** on **834** df, AIC = **7247.5**, BIC = **7318.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.4044** | 7.1142 | ±14.2284 | **+18.471** | **3.55e-76** | *** |
| **Education: graduate level (vs college)** | **-3.0466** | 1.2526 | ±2.5052 | **-2.432** | **0.0150** | * |
| **Education: high school or below (vs college)** | **+4.8757** | 1.9959 | ±3.9919 | **+2.443** | **0.0146** | * |
| **Site: UCSD (vs UAB)** | **+3.1675** | 1.5306 | ±3.0612 | **+2.069** | **0.0385** | * |
| Site: UW (vs UAB) | -0.9734 | 1.4038 | ±2.8077 | -0.693 | 0.4881 |  |
| Season: spring (vs autumn) | +2.5444 | 1.5066 | ±3.0131 | +1.689 | 0.0912 | . |
| Season: summer (vs autumn) | +2.6998 | 1.6195 | ±3.2389 | +1.667 | 0.0955 | . |
| **Season: winter (vs autumn)** | **+6.0340** | 1.9078 | ±3.8156 | **+3.163** | **0.0016** | ** |
| **Age (years)** | **-0.1428** | 0.0689 | ±0.1378 | **-2.072** | **0.0382** | * |
| BMI (kg/m2) | +0.1874 | 0.0984 | ±0.1968 | +1.905 | 0.0568 | . |
| Hypertension | +0.5895 | 1.4321 | ±2.8641 | +0.412 | 0.6806 |  |
| High cholesterol | +1.2862 | 1.3262 | ±2.6523 | +0.970 | 0.3321 |  |
| Kidney disease | -2.5770 | 1.6004 | ±3.2007 | -1.610 | 0.1073 |  |
| Circulatory disease | -0.1049 | 1.5816 | ±3.1632 | -0.066 | 0.9471 |  |
| **Avg. daily mean/SD** | **-0.8830** | 0.3452 | ±0.6905 | **-2.558** | **0.0105** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.0719**, Adj R² = **0.0563**, F-statistic = **4.61** (p = **3.97e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.1**, BIC = **7323.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.3076** | 6.6568 | ±13.3136 | **+18.524** | **1.33e-76** | *** |
| **Education: graduate level (vs college)** | **-3.1623** | 1.2407 | ±2.4813 | **-2.549** | **0.0108** | * |
| **Education: high school or below (vs college)** | **+5.1153** | 2.0174 | ±4.0347 | **+2.536** | **0.0112** | * |
| **Site: UCSD (vs UAB)** | **+3.1765** | 1.5283 | ±3.0567 | **+2.078** | **0.0377** | * |
| Site: UW (vs UAB) | -1.0423 | 1.3958 | ±2.7917 | -0.747 | 0.4553 |  |
| Season: spring (vs autumn) | +2.5104 | 1.5097 | ±3.0193 | +1.663 | 0.0963 | . |
| Season: summer (vs autumn) | +2.7206 | 1.6176 | ±3.2351 | +1.682 | 0.0926 | . |
| **Season: winter (vs autumn)** | **+6.0566** | 1.9084 | ±3.8168 | **+3.174** | **0.0015** | ** |
| Age (years) | -0.1206 | 0.0670 | ±0.1341 | -1.799 | 0.0720 | . |
| BMI (kg/m2) | +0.1761 | 0.0992 | ±0.1984 | +1.775 | 0.0760 | . |
| Hypertension | +0.6619 | 1.4367 | ±2.8734 | +0.461 | 0.6450 |  |
| High cholesterol | +1.2186 | 1.3327 | ±2.6653 | +0.914 | 0.3605 |  |
| Kidney disease | -2.2467 | 1.5788 | ±3.1576 | -1.423 | 0.1547 |  |
| Circulatory disease | -0.0893 | 1.5863 | ±3.1726 | -0.056 | 0.9551 |  |
| MAG (mg/dL/h) | +0.0486 | 0.0670 | ±0.1340 | +0.726 | 0.4680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.0722**, Adj R² = **0.0566**, F-statistic = **4.63** (p = **3.58e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.8**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.8817** | 6.6401 | ±13.2802 | **+18.657** | **1.11e-77** | *** |
| **Education: graduate level (vs college)** | **-3.1429** | 1.2419 | ±2.4838 | **-2.531** | **0.0114** | * |
| **Education: high school or below (vs college)** | **+5.0338** | 2.0038 | ±4.0077 | **+2.512** | **0.0120** | * |
| **Site: UCSD (vs UAB)** | **+3.2227** | 1.5427 | ±3.0853 | **+2.089** | **0.0367** | * |
| Site: UW (vs UAB) | -1.0922 | 1.4027 | ±2.8054 | -0.779 | 0.4362 |  |
| Season: spring (vs autumn) | +2.4761 | 1.5095 | ±3.0190 | +1.640 | 0.1009 |  |
| Season: summer (vs autumn) | +2.6860 | 1.6229 | ±3.2458 | +1.655 | 0.0979 | . |
| **Season: winter (vs autumn)** | **+6.0023** | 1.9083 | ±3.8166 | **+3.145** | **0.0017** | ** |
| Age (years) | -0.1271 | 0.0673 | ±0.1347 | -1.887 | 0.0591 | . |
| BMI (kg/m2) | +0.1803 | 0.0992 | ±0.1985 | +1.816 | 0.0693 | . |
| Hypertension | +0.6809 | 1.4358 | ±2.8716 | +0.474 | 0.6354 |  |
| High cholesterol | +1.2305 | 1.3268 | ±2.6536 | +0.927 | 0.3537 |  |
| Kidney disease | -2.3906 | 1.5925 | ±3.1850 | -1.501 | 0.1333 |  |
| Circulatory disease | -0.1168 | 1.5865 | ±3.1730 | -0.074 | 0.9413 |  |
| Avg. daily range (mg/dL) | +0.0133 | 0.0138 | ±0.0277 | +0.959 | 0.3376 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.0735**, Adj R² = **0.0579**, F-statistic = **4.73** (p = **2.20e-08**), Residual SE = **17.157** on **834** df, AIC = **7250.6**, BIC = **7321.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5396** | 6.4098 | ±12.8196 | **+19.742** | **9.48e-87** | *** |
| **Education: graduate level (vs college)** | **-3.4529** | 1.2387 | ±2.4774 | **-2.787** | **0.0053** | ** |
| **Education: high school or below (vs college)** | **+5.3391** | 1.9937 | ±3.9873 | **+2.678** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +2.9988 | 1.5610 | ±3.1220 | +1.921 | 0.0547 | . |
| Site: UW (vs UAB) | -1.3269 | 1.4104 | ±2.8208 | -0.941 | 0.3468 |  |
| Season: spring (vs autumn) | +2.5049 | 1.5087 | ±3.0175 | +1.660 | 0.0969 | . |
| Season: summer (vs autumn) | +2.6542 | 1.6222 | ±3.2444 | +1.636 | 0.1018 |  |
| **Season: winter (vs autumn)** | **+6.1649** | 1.8853 | ±3.7705 | **+3.270** | **0.0011** | ** |
| Age (years) | -0.1206 | 0.0677 | ±0.1354 | -1.782 | 0.0748 | . |
| BMI (kg/m2) | +0.1841 | 0.1004 | ±0.2008 | +1.835 | 0.0666 | . |
| Hypertension | +0.6705 | 1.4410 | ±2.8821 | +0.465 | 0.6417 |  |
| High cholesterol | +1.1601 | 1.3206 | ±2.6413 | +0.878 | 0.3797 |  |
| Kidney disease | -1.8669 | 1.6090 | ±3.2181 | -1.160 | 0.2459 |  |
| Circulatory disease | +0.0586 | 1.5712 | ±3.1425 | +0.037 | 0.9703 |  |
| SD of daily means (mg/dL) | -0.1060 | 0.1271 | ±0.2542 | -0.834 | 0.4042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.0718**, Adj R² = **0.0562**, F-statistic = **4.61** (p = **4.08e-08**), Residual SE = **17.172** on **834** df, AIC = **7252.1**, BIC = **7323.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.9866** | 6.6884 | ±13.3769 | **+18.537** | **1.03e-76** | *** |
| **Education: graduate level (vs college)** | **-3.3317** | 1.2291 | ±2.4582 | **-2.711** | **0.0067** | ** |
| **Education: high school or below (vs college)** | **+5.3281** | 2.0087 | ±4.0174 | **+2.652** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +3.0140 | 1.5512 | ±3.1024 | +1.943 | 0.0520 | . |
| Site: UW (vs UAB) | -1.2247 | 1.4030 | ±2.8061 | -0.873 | 0.3827 |  |
| Season: spring (vs autumn) | +2.5259 | 1.5083 | ±3.0166 | +1.675 | 0.0940 | . |
| Season: summer (vs autumn) | +2.6164 | 1.6293 | ±3.2586 | +1.606 | 0.1083 |  |
| **Season: winter (vs autumn)** | **+6.1122** | 1.8806 | ±3.7612 | **+3.250** | **0.0012** | ** |
| Age (years) | -0.1182 | 0.0672 | ±0.1345 | -1.758 | 0.0788 | . |
| BMI (kg/m2) | +0.1793 | 0.0985 | ±0.1971 | +1.819 | 0.0689 | . |
| Hypertension | +0.6027 | 1.4291 | ±2.8581 | +0.422 | 0.6732 |  |
| High cholesterol | +1.1586 | 1.3261 | ±2.6522 | +0.874 | 0.3823 |  |
| Kidney disease | -2.0048 | 1.6010 | ±3.2020 | -1.252 | 0.2105 |  |
| Circulatory disease | -0.0708 | 1.5882 | ±3.1765 | -0.045 | 0.9645 |  |
| Time in range 70-180, pooled (%) | +0.0175 | 0.0261 | ±0.0523 | +0.671 | 0.5024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.0720**, Adj R² = **0.0564**, F-statistic = **4.62** (p = **3.85e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.0**, BIC = **7323.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.7887** | 6.6839 | ±13.3679 | **+18.520** | **1.41e-76** | *** |
| **Education: graduate level (vs college)** | **-3.3380** | 1.2298 | ±2.4595 | **-2.714** | **0.0066** | ** |
| **Education: high school or below (vs college)** | **+5.3474** | 2.0073 | ±4.0147 | **+2.664** | **0.0077** | ** |
| Site: UCSD (vs UAB) | +2.9979 | 1.5525 | ±3.1049 | +1.931 | 0.0535 | . |
| Site: UW (vs UAB) | -1.2299 | 1.4031 | ±2.8063 | -0.877 | 0.3808 |  |
| Season: spring (vs autumn) | +2.5312 | 1.5080 | ±3.0161 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.6185 | 1.6282 | ±3.2565 | +1.608 | 0.1078 |  |
| **Season: winter (vs autumn)** | **+6.1263** | 1.8777 | ±3.7553 | **+3.263** | **0.0011** | ** |
| Age (years) | -0.1177 | 0.0673 | ±0.1345 | -1.750 | 0.0801 | . |
| BMI (kg/m2) | +0.1797 | 0.0985 | ±0.1969 | +1.825 | 0.0681 | . |
| Hypertension | +0.5972 | 1.4290 | ±2.8580 | +0.418 | 0.6760 |  |
| High cholesterol | +1.1552 | 1.3256 | ±2.6512 | +0.871 | 0.3835 |  |
| Kidney disease | -1.9863 | 1.5995 | ±3.1989 | -1.242 | 0.2143 |  |
| Circulatory disease | -0.0680 | 1.5884 | ±3.1768 | -0.043 | 0.9658 |  |
| Avg. daily time in range 70-180 (%) | +0.0195 | 0.0261 | ±0.0522 | +0.748 | 0.4547 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.0713**, Adj R² = **0.0557**, F-statistic = **4.57** (p = **5.01e-08**), Residual SE = **17.177** on **834** df, AIC = **7252.6**, BIC = **7323.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6734** | 6.2605 | ±12.5210 | **+20.074** | **1.24e-89** | *** |
| **Education: graduate level (vs college)** | **-3.2538** | 1.2484 | ±2.4969 | **-2.606** | **0.0092** | ** |
| **Education: high school or below (vs college)** | **+5.1846** | 1.9842 | ±3.9684 | **+2.613** | **0.0090** | ** |
| **Site: UCSD (vs UAB)** | **+3.0936** | 1.5362 | ±3.0723 | **+2.014** | **0.0440** | * |
| Site: UW (vs UAB) | -1.2083 | 1.3923 | ±2.7846 | -0.868 | 0.3855 |  |
| Season: spring (vs autumn) | +2.5092 | 1.5095 | ±3.0191 | +1.662 | 0.0965 | . |
| Season: summer (vs autumn) | +2.6409 | 1.6226 | ±3.2452 | +1.628 | 0.1036 |  |
| **Season: winter (vs autumn)** | **+6.0340** | 1.9140 | ±3.8279 | **+3.153** | **0.0016** | ** |
| Age (years) | -0.1226 | 0.0661 | ±0.1322 | -1.856 | 0.0635 | . |
| BMI (kg/m2) | +0.1778 | 0.1004 | ±0.2008 | +1.772 | 0.0765 | . |
| Hypertension | +0.6581 | 1.4408 | ±2.8817 | +0.457 | 0.6478 |  |
| High cholesterol | +1.1818 | 1.3351 | ±2.6702 | +0.885 | 0.3760 |  |
| Kidney disease | -2.1287 | 1.5981 | ±3.1961 | -1.332 | 0.1828 |  |
| Circulatory disease | -0.0743 | 1.5752 | ±3.1504 | -0.047 | 0.9624 |  |
| Any reading < 54 during wear (0/1) | -0.3089 | 1.4398 | ±2.8797 | -0.215 | 0.8301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.0716**, Adj R² = **0.0560**, F-statistic = **4.59** (p = **4.49e-08**), Residual SE = **17.175** on **834** df, AIC = **7252.4**, BIC = **7323.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4136** | 6.4121 | ±12.8242 | **+19.559** | **3.46e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2339** | 1.2502 | ±2.5004 | **-2.587** | **0.0097** | ** |
| **Education: high school or below (vs college)** | **+5.2572** | 1.9885 | ±3.9771 | **+2.644** | **0.0082** | ** |
| **Site: UCSD (vs UAB)** | **+3.2010** | 1.5418 | ±3.0835 | **+2.076** | **0.0379** | * |
| Site: UW (vs UAB) | -1.0833 | 1.4143 | ±2.8286 | -0.766 | 0.4437 |  |
| Season: spring (vs autumn) | +2.5415 | 1.5112 | ±3.0224 | +1.682 | 0.0926 | . |
| Season: summer (vs autumn) | +2.6660 | 1.6241 | ±3.2481 | +1.642 | 0.1007 |  |
| **Season: winter (vs autumn)** | **+6.0859** | 1.9046 | ±3.8092 | **+3.195** | **0.0014** | ** |
| Age (years) | -0.1212 | 0.0672 | ±0.1344 | -1.803 | 0.0714 | . |
| BMI (kg/m2) | +0.1748 | 0.0993 | ±0.1986 | +1.761 | 0.0783 | . |
| Hypertension | +0.6221 | 1.4365 | ±2.8730 | +0.433 | 0.6649 |  |
| High cholesterol | +1.2107 | 1.3278 | ±2.6557 | +0.912 | 0.3619 |  |
| Kidney disease | -2.1018 | 1.5925 | ±3.1851 | -1.320 | 0.1869 |  |
| Circulatory disease | -0.1523 | 1.5843 | ±3.1687 | -0.096 | 0.9234 |  |
| Time < 54 (%) | +0.8004 | 0.9856 | ±1.9711 | +0.812 | 0.4167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.0722**, Adj R² = **0.0566**, F-statistic = **4.64** (p = **3.55e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.8**, BIC = **7322.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4246** | 6.4144 | ±12.8288 | **+19.554** | **3.84e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2066** | 1.2486 | ±2.4972 | **-2.568** | **0.0102** | * |
| **Education: high school or below (vs college)** | **+5.2755** | 1.9904 | ±3.9809 | **+2.650** | **0.0080** | ** |
| **Site: UCSD (vs UAB)** | **+3.2290** | 1.5395 | ±3.0789 | **+2.097** | **0.0360** | * |
| Site: UW (vs UAB) | -1.0527 | 1.4133 | ±2.8266 | -0.745 | 0.4564 |  |
| Season: spring (vs autumn) | +2.5895 | 1.5123 | ±3.0246 | +1.712 | 0.0868 | . |
| Season: summer (vs autumn) | +2.6791 | 1.6251 | ±3.2503 | +1.649 | 0.0992 | . |
| **Season: winter (vs autumn)** | **+6.0967** | 1.9045 | ±3.8090 | **+3.201** | **0.0014** | ** |
| Age (years) | -0.1226 | 0.0673 | ±0.1346 | -1.822 | 0.0684 | . |
| BMI (kg/m2) | +0.1751 | 0.0991 | ±0.1981 | +1.768 | 0.0771 | . |
| Hypertension | +0.6200 | 1.4348 | ±2.8696 | +0.432 | 0.6656 |  |
| High cholesterol | +1.2373 | 1.3278 | ±2.6555 | +0.932 | 0.3514 |  |
| Kidney disease | -2.1078 | 1.5919 | ±3.1839 | -1.324 | 0.1855 |  |
| Circulatory disease | -0.1800 | 1.5890 | ±3.1780 | -0.113 | 0.9098 |  |
| Avg. daily time < 54 (%) | +1.2758 | 1.0453 | ±2.0907 | +1.221 | 0.2223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0566**, F-statistic = **4.63** (p = **3.62e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.8**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4183** | 6.4185 | ±12.8369 | **+19.540** | **5.00e-85** | *** |
| **Education: graduate level (vs college)** | **-3.1976** | 1.2501 | ±2.5002 | **-2.558** | **0.0105** | * |
| **Education: high school or below (vs college)** | **+5.2045** | 1.9969 | ±3.9938 | **+2.606** | **0.0092** | ** |
| **Site: UCSD (vs UAB)** | **+3.2175** | 1.5387 | ±3.0775 | **+2.091** | **0.0365** | * |
| Site: UW (vs UAB) | -1.0795 | 1.4182 | ±2.8365 | -0.761 | 0.4465 |  |
| Season: spring (vs autumn) | +2.5956 | 1.5116 | ±3.0232 | +1.717 | 0.0860 | . |
| Season: summer (vs autumn) | +2.7053 | 1.6220 | ±3.2440 | +1.668 | 0.0953 | . |
| **Season: winter (vs autumn)** | **+6.1344** | 1.8957 | ±3.7914 | **+3.236** | **0.0012** | ** |
| Age (years) | -0.1237 | 0.0675 | ±0.1351 | -1.832 | 0.0669 | . |
| BMI (kg/m2) | +0.1750 | 0.0993 | ±0.1986 | +1.762 | 0.0780 | . |
| Hypertension | +0.6262 | 1.4348 | ±2.8695 | +0.436 | 0.6625 |  |
| High cholesterol | +1.2093 | 1.3280 | ±2.6560 | +0.911 | 0.3625 |  |
| Kidney disease | -2.1257 | 1.5916 | ±3.1832 | -1.336 | 0.1817 |  |
| Circulatory disease | -0.1375 | 1.5858 | ±3.1716 | -0.087 | 0.9309 |  |
| Time 54-69, pooled (%) | +0.3679 | 0.3629 | ±0.7258 | +1.014 | 0.3106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.0720**, Adj R² = **0.0564**, F-statistic = **4.62** (p = **3.87e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.0**, BIC = **7323.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4942** | 6.4209 | ±12.8418 | **+19.545** | **4.58e-85** | *** |
| **Education: graduate level (vs college)** | **-3.1998** | 1.2496 | ±2.4992 | **-2.561** | **0.0104** | * |
| **Education: high school or below (vs college)** | **+5.1965** | 1.9976 | ±3.9953 | **+2.601** | **0.0093** | ** |
| **Site: UCSD (vs UAB)** | **+3.1988** | 1.5381 | ±3.0763 | **+2.080** | **0.0376** | * |
| Site: UW (vs UAB) | -1.0933 | 1.4187 | ±2.8374 | -0.771 | 0.4409 |  |
| Season: spring (vs autumn) | +2.5828 | 1.5122 | ±3.0244 | +1.708 | 0.0876 | . |
| Season: summer (vs autumn) | +2.6929 | 1.6232 | ±3.2464 | +1.659 | 0.0971 | . |
| **Season: winter (vs autumn)** | **+6.1190** | 1.8971 | ±3.7943 | **+3.225** | **0.0013** | ** |
| Age (years) | -0.1243 | 0.0677 | ±0.1353 | -1.837 | 0.0662 | . |
| BMI (kg/m2) | +0.1752 | 0.0992 | ±0.1984 | +1.766 | 0.0774 | . |
| Hypertension | +0.6281 | 1.4345 | ±2.8690 | +0.438 | 0.6615 |  |
| High cholesterol | +1.2116 | 1.3285 | ±2.6570 | +0.912 | 0.3618 |  |
| Kidney disease | -2.1187 | 1.5928 | ±3.1855 | -1.330 | 0.1834 |  |
| Circulatory disease | -0.1246 | 1.5863 | ±3.1726 | -0.079 | 0.9374 |  |
| Avg. daily time 54-69 (%) | +0.3206 | 0.3446 | ±0.6892 | +0.930 | 0.3523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0565**, F-statistic = **4.63** (p = **3.69e-08**), Residual SE = **17.170** on **834** df, AIC = **7251.9**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3955** | 6.4157 | ±12.8314 | **+19.545** | **4.54e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2011** | 1.2505 | ±2.5010 | **-2.560** | **0.0105** | * |
| **Education: high school or below (vs college)** | **+5.2243** | 1.9945 | ±3.9890 | **+2.619** | **0.0088** | ** |
| **Site: UCSD (vs UAB)** | **+3.2285** | 1.5398 | ±3.0796 | **+2.097** | **0.0360** | * |
| Site: UW (vs UAB) | -1.0637 | 1.4187 | ±2.8374 | -0.750 | 0.4534 |  |
| Season: spring (vs autumn) | +2.5902 | 1.5114 | ±3.0227 | +1.714 | 0.0866 | . |
| Season: summer (vs autumn) | +2.7005 | 1.6222 | ±3.2443 | +1.665 | 0.0960 | . |
| **Season: winter (vs autumn)** | **+6.1302** | 1.8970 | ±3.7939 | **+3.232** | **0.0012** | ** |
| Age (years) | -0.1231 | 0.0675 | ±0.1349 | -1.826 | 0.0679 | . |
| BMI (kg/m2) | +0.1746 | 0.0993 | ±0.1987 | +1.758 | 0.0788 | . |
| Hypertension | +0.6221 | 1.4347 | ±2.8694 | +0.434 | 0.6646 |  |
| High cholesterol | +1.2119 | 1.3280 | ±2.6561 | +0.913 | 0.3615 |  |
| Kidney disease | -2.1174 | 1.5917 | ±3.1833 | -1.330 | 0.1834 |  |
| Circulatory disease | -0.1506 | 1.5853 | ±3.1706 | -0.095 | 0.9243 |  |
| Time < 70 (%) | +0.2955 | 0.2819 | ±0.5639 | +1.048 | 0.2945 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0565**, F-statistic = **4.63** (p = **3.65e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.9**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4719** | 6.4187 | ±12.8374 | **+19.548** | **4.30e-85** | *** |
| **Education: graduate level (vs college)** | **-3.1938** | 1.2495 | ±2.4991 | **-2.556** | **0.0106** | * |
| **Education: high school or below (vs college)** | **+5.2137** | 1.9959 | ±3.9918 | **+2.612** | **0.0090** | ** |
| **Site: UCSD (vs UAB)** | **+3.2168** | 1.5388 | ±3.0776 | **+2.091** | **0.0366** | * |
| Site: UW (vs UAB) | -1.0722 | 1.4188 | ±2.8375 | -0.756 | 0.4498 |  |
| Season: spring (vs autumn) | +2.5941 | 1.5123 | ±3.0245 | +1.715 | 0.0863 | . |
| Season: summer (vs autumn) | +2.6958 | 1.6234 | ±3.2468 | +1.661 | 0.0968 | . |
| **Season: winter (vs autumn)** | **+6.1227** | 1.8981 | ±3.7963 | **+3.226** | **0.0013** | ** |
| Age (years) | -0.1243 | 0.0676 | ±0.1352 | -1.839 | 0.0660 | . |
| BMI (kg/m2) | +0.1749 | 0.0992 | ±0.1984 | +1.764 | 0.0778 | . |
| Hypertension | +0.6245 | 1.4342 | ±2.8685 | +0.435 | 0.6633 |  |
| High cholesterol | +1.2195 | 1.3287 | ±2.6573 | +0.918 | 0.3587 |  |
| Kidney disease | -2.1157 | 1.5920 | ±3.1841 | -1.329 | 0.1839 |  |
| Circulatory disease | -0.1415 | 1.5861 | ±3.1721 | -0.089 | 0.9289 |  |
| Avg. daily time < 70 (%) | +0.2914 | 0.2624 | ±0.5249 | +1.111 | 0.2668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.0749**, Adj R² = **0.0594**, F-statistic = **4.83** (p = **1.29e-08**), Residual SE = **17.143** on **834** df, AIC = **7249.3**, BIC = **7320.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.0980** | 7.1120 | ±14.2240 | **+16.746** | **6.05e-63** | *** |
| **Education: graduate level (vs college)** | **-3.4732** | 1.2425 | ±2.4849 | **-2.795** | **0.0052** | ** |
| **Education: high school or below (vs college)** | **+5.4751** | 1.9993 | ±3.9985 | **+2.739** | **0.0062** | ** |
| Site: UCSD (vs UAB) | +2.9201 | 1.5553 | ±3.1105 | +1.878 | 0.0604 | . |
| Site: UW (vs UAB) | -1.3847 | 1.4138 | ±2.8276 | -0.979 | 0.3274 |  |
| Season: spring (vs autumn) | +2.4749 | 1.5150 | ±3.0299 | +1.634 | 0.1023 |  |
| Season: summer (vs autumn) | +2.4248 | 1.6431 | ±3.2863 | +1.476 | 0.1400 |  |
| **Season: winter (vs autumn)** | **+6.0898** | 1.8941 | ±3.7881 | **+3.215** | **0.0013** | ** |
| Age (years) | -0.1237 | 0.0675 | ±0.1350 | -1.833 | 0.0668 | . |
| BMI (kg/m2) | +0.1810 | 0.0981 | ±0.1963 | +1.844 | 0.0651 | . |
| Hypertension | +0.6672 | 1.4347 | ±2.8694 | +0.465 | 0.6419 |  |
| High cholesterol | +1.1399 | 1.3203 | ±2.6407 | +0.863 | 0.3880 |  |
| Kidney disease | -1.9100 | 1.5884 | ±3.1767 | -1.203 | 0.2292 |  |
| Circulatory disease | -0.0487 | 1.5854 | ±3.1709 | -0.031 | 0.9755 |  |
| Time 54-250, pooled (%) | +0.0710 | 0.0429 | ±0.0857 | +1.657 | 0.0976 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.0753**, Adj R² = **0.0598**, F-statistic = **4.85** (p = **1.12e-08**), Residual SE = **17.140** on **834** df, AIC = **7248.9**, BIC = **7320.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+118.6331** | 7.1480 | ±14.2959 | **+16.597** | **7.36e-62** | *** |
| **Education: graduate level (vs college)** | **-3.4815** | 1.2426 | ±2.4852 | **-2.802** | **0.0051** | ** |
| **Education: high school or below (vs college)** | **+5.4866** | 1.9967 | ±3.9934 | **+2.748** | **0.0060** | ** |
| Site: UCSD (vs UAB) | +2.9077 | 1.5547 | ±3.1095 | +1.870 | 0.0615 | . |
| Site: UW (vs UAB) | -1.3858 | 1.4126 | ±2.8253 | -0.981 | 0.3266 |  |
| Season: spring (vs autumn) | +2.4850 | 1.5144 | ±3.0288 | +1.641 | 0.1008 |  |
| Season: summer (vs autumn) | +2.4309 | 1.6412 | ±3.2825 | +1.481 | 0.1386 |  |
| **Season: winter (vs autumn)** | **+6.1044** | 1.8924 | ±3.7848 | **+3.226** | **0.0013** | ** |
| Age (years) | -0.1229 | 0.0674 | ±0.1349 | -1.823 | 0.0684 | . |
| BMI (kg/m2) | +0.1813 | 0.0980 | ±0.1960 | +1.850 | 0.0643 | . |
| Hypertension | +0.6628 | 1.4346 | ±2.8691 | +0.462 | 0.6441 |  |
| High cholesterol | +1.1365 | 1.3200 | ±2.6400 | +0.861 | 0.3893 |  |
| Kidney disease | -1.8846 | 1.5859 | ±3.1718 | -1.188 | 0.2347 |  |
| Circulatory disease | -0.0379 | 1.5861 | ±3.1722 | -0.024 | 0.9809 |  |
| Avg. daily time 54-250 (%) | +0.0752 | 0.0442 | ±0.0883 | +1.702 | 0.0888 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.0715**, Adj R² = **0.0559**, F-statistic = **4.59** (p = **4.59e-08**), Residual SE = **17.175** on **834** df, AIC = **7252.4**, BIC = **7323.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5058** | 6.4219 | ±12.8438 | **+19.543** | **4.69e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2322** | 1.2370 | ±2.4740 | **-2.613** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+5.1376** | 2.0043 | ±4.0086 | **+2.563** | **0.0104** | * |
| **Site: UCSD (vs UAB)** | **+3.1751** | 1.5366 | ±3.0732 | **+2.066** | **0.0388** | * |
| Site: UW (vs UAB) | -1.1905 | 1.4127 | ±2.8254 | -0.843 | 0.3994 |  |
| Season: spring (vs autumn) | +2.4802 | 1.5110 | ±3.0221 | +1.641 | 0.1007 |  |
| Season: summer (vs autumn) | +2.6207 | 1.6257 | ±3.2514 | +1.612 | 0.1070 |  |
| **Season: winter (vs autumn)** | **+5.9961** | 1.8673 | ±3.7345 | **+3.211** | **0.0013** | ** |
| Age (years) | -0.1259 | 0.0675 | ±0.1349 | -1.865 | 0.0621 | . |
| BMI (kg/m2) | +0.1750 | 0.0988 | ±0.1976 | +1.772 | 0.0765 | . |
| Hypertension | +0.6925 | 1.4095 | ±2.8190 | +0.491 | 0.6232 |  |
| High cholesterol | +1.2244 | 1.3356 | ±2.6711 | +0.917 | 0.3593 |  |
| Kidney disease | -2.1956 | 1.6145 | ±3.2290 | -1.360 | 0.1738 |  |
| Circulatory disease | -0.1040 | 1.5879 | ±3.1758 | -0.065 | 0.9478 |  |
| Time 181-250, pooled (%) | +0.0198 | 0.0466 | ±0.0933 | +0.425 | 0.6708 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.0714**, Adj R² = **0.0558**, F-statistic = **4.58** (p = **4.75e-08**), Residual SE = **17.176** on **834** df, AIC = **7252.5**, BIC = **7323.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5080** | 6.4240 | ±12.8480 | **+19.537** | **5.29e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2377** | 1.2381 | ±2.4763 | **-2.615** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+5.1447** | 2.0044 | ±4.0088 | **+2.567** | **0.0103** | * |
| **Site: UCSD (vs UAB)** | **+3.1684** | 1.5392 | ±3.0783 | **+2.059** | **0.0395** | * |
| Site: UW (vs UAB) | -1.1860 | 1.4112 | ±2.8224 | -0.840 | 0.4007 |  |
| Season: spring (vs autumn) | +2.4856 | 1.5109 | ±3.0217 | +1.645 | 0.0999 | . |
| Season: summer (vs autumn) | +2.6254 | 1.6257 | ±3.2514 | +1.615 | 0.1063 |  |
| **Season: winter (vs autumn)** | **+6.0036** | 1.8656 | ±3.7313 | **+3.218** | **0.0013** | ** |
| Age (years) | -0.1250 | 0.0675 | ±0.1349 | -1.853 | 0.0639 | . |
| BMI (kg/m2) | +0.1753 | 0.0988 | ±0.1977 | +1.773 | 0.0762 | . |
| Hypertension | +0.6829 | 1.4113 | ±2.8226 | +0.484 | 0.6285 |  |
| High cholesterol | +1.2184 | 1.3342 | ±2.6684 | +0.913 | 0.3611 |  |
| Kidney disease | -2.1840 | 1.6149 | ±3.2298 | -1.352 | 0.1762 |  |
| Circulatory disease | -0.1008 | 1.5876 | ±3.1753 | -0.064 | 0.9494 |  |
| Avg. daily time 181-250 (%) | +0.0162 | 0.0452 | ±0.0904 | +0.359 | 0.7197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.0719**, Adj R² = **0.0563**, F-statistic = **4.62** (p = **3.94e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.0**, BIC = **7323.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7430** | 6.4671 | ±12.9341 | **+19.444** | **3.30e-84** | *** |
| **Education: graduate level (vs college)** | **-3.3330** | 1.2298 | ±2.4596 | **-2.710** | **0.0067** | ** |
| **Education: high school or below (vs college)** | **+5.3370** | 2.0078 | ±4.0157 | **+2.658** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +3.0147 | 1.5496 | ±3.0992 | +1.945 | 0.0517 | . |
| Site: UW (vs UAB) | -1.2202 | 1.4034 | ±2.8069 | -0.869 | 0.3846 |  |
| Season: spring (vs autumn) | +2.5317 | 1.5080 | ±3.0159 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.6176 | 1.6288 | ±3.2576 | +1.607 | 0.1080 |  |
| **Season: winter (vs autumn)** | **+6.1204** | 1.8786 | ±3.7572 | **+3.258** | **0.0011** | ** |
| Age (years) | -0.1181 | 0.0672 | ±0.1345 | -1.757 | 0.0790 | . |
| BMI (kg/m2) | +0.1793 | 0.0985 | ±0.1971 | +1.819 | 0.0689 | . |
| Hypertension | +0.5992 | 1.4287 | ±2.8574 | +0.419 | 0.6749 |  |
| High cholesterol | +1.1572 | 1.3258 | ±2.6517 | +0.873 | 0.3828 |  |
| Kidney disease | -1.9974 | 1.6009 | ±3.2018 | -1.248 | 0.2122 |  |
| Circulatory disease | -0.0730 | 1.5883 | ±3.1766 | -0.046 | 0.9633 |  |
| Time > 180 (%) | -0.0186 | 0.0258 | ±0.0517 | -0.720 | 0.4717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0565**, F-statistic = **4.63** (p = **3.70e-08**), Residual SE = **17.170** on **834** df, AIC = **7251.9**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7480** | 6.4666 | ±12.9331 | **+19.446** | **3.16e-84** | *** |
| **Education: graduate level (vs college)** | **-3.3385** | 1.2306 | ±2.4612 | **-2.713** | **0.0067** | ** |
| **Education: high school or below (vs college)** | **+5.3565** | 2.0066 | ±4.0132 | **+2.669** | **0.0076** | ** |
| Site: UCSD (vs UAB) | +2.9980 | 1.5509 | ±3.1017 | +1.933 | 0.0532 | . |
| Site: UW (vs UAB) | -1.2252 | 1.4034 | ±2.8068 | -0.873 | 0.3827 |  |
| Season: spring (vs autumn) | +2.5382 | 1.5077 | ±3.0154 | +1.683 | 0.0923 | . |
| Season: summer (vs autumn) | +2.6200 | 1.6278 | ±3.2555 | +1.610 | 0.1075 |  |
| **Season: winter (vs autumn)** | **+6.1351** | 1.8758 | ±3.7516 | **+3.271** | **0.0011** | ** |
| Age (years) | -0.1177 | 0.0672 | ±0.1345 | -1.750 | 0.0802 | . |
| BMI (kg/m2) | +0.1797 | 0.0985 | ±0.1969 | +1.825 | 0.0680 | . |
| Hypertension | +0.5934 | 1.4286 | ±2.8573 | +0.415 | 0.6779 |  |
| High cholesterol | +1.1544 | 1.3253 | ±2.6506 | +0.871 | 0.3837 |  |
| Kidney disease | -1.9780 | 1.5995 | ±3.1990 | -1.237 | 0.2162 |  |
| Circulatory disease | -0.0700 | 1.5883 | ±3.1767 | -0.044 | 0.9649 |  |
| Avg. daily time > 180 (%) | -0.0207 | 0.0259 | ±0.0517 | -0.799 | 0.4245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.0716**, Adj R² = **0.0560**, F-statistic = **4.60** (p = **4.38e-08**), Residual SE = **17.174** on **834** df, AIC = **7252.3**, BIC = **7323.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6687** | 6.4752 | ±12.9504 | **+19.408** | **6.64e-84** | *** |
| **Education: graduate level (vs college)** | **-3.3295** | 1.2257 | ±2.4515 | **-2.716** | **0.0066** | ** |
| **Education: high school or below (vs college)** | **+5.3000** | 2.0028 | ±4.0056 | **+2.646** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +3.0302 | 1.5552 | ±3.1103 | +1.948 | 0.0514 | . |
| Site: UW (vs UAB) | -1.2028 | 1.4035 | ±2.8070 | -0.857 | 0.3915 |  |
| Season: spring (vs autumn) | +2.5322 | 1.5066 | ±3.0131 | +1.681 | 0.0928 | . |
| Season: summer (vs autumn) | +2.6208 | 1.6307 | ±3.2614 | +1.607 | 0.1080 |  |
| **Season: winter (vs autumn)** | **+6.1090** | 1.8732 | ±3.7464 | **+3.261** | **0.0011** | ** |
| Age (years) | -0.1208 | 0.0674 | ±0.1347 | -1.794 | 0.0728 | . |
| BMI (kg/m2) | +0.1812 | 0.0984 | ±0.1967 | +1.842 | 0.0655 | . |
| Hypertension | +0.6053 | 1.4291 | ±2.8581 | +0.424 | 0.6719 |  |
| High cholesterol | +1.1645 | 1.3261 | ±2.6523 | +0.878 | 0.3799 |  |
| Kidney disease | -2.0414 | 1.6055 | ±3.2110 | -1.271 | 0.2036 |  |
| Circulatory disease | -0.0739 | 1.5864 | ±3.1729 | -0.047 | 0.9629 |  |
| Nocturnal time > 180 (%) | -0.0138 | 0.0277 | ±0.0555 | -0.498 | 0.6188 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.0734**, Adj R² = **0.0579**, F-statistic = **4.72** (p = **2.26e-08**), Residual SE = **17.157** on **834** df, AIC = **7250.7**, BIC = **7321.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0251** | 6.4404 | ±12.8808 | **+19.413** | **6.04e-84** | *** |
| **Education: graduate level (vs college)** | **-3.0829** | 1.2369 | ±2.4738 | **-2.492** | **0.0127** | * |
| **Education: high school or below (vs college)** | **+5.1105** | 1.9957 | ±3.9915 | **+2.561** | **0.0104** | * |
| **Site: UCSD (vs UAB)** | **+3.2162** | 1.5356 | ±3.0713 | **+2.094** | **0.0362** | * |
| Site: UW (vs UAB) | -1.2362 | 1.4088 | ±2.8176 | -0.877 | 0.3802 |  |
| Season: spring (vs autumn) | +2.5342 | 1.5110 | ±3.0220 | +1.677 | 0.0935 | . |
| Season: summer (vs autumn) | +2.6420 | 1.6216 | ±3.2432 | +1.629 | 0.1033 |  |
| **Season: winter (vs autumn)** | **+6.0394** | 1.9074 | ±3.8148 | **+3.166** | **0.0015** | ** |
| **Age (years)** | **-0.1360** | 0.0670 | ±0.1340 | **-2.029** | **0.0425** | * |
| BMI (kg/m2) | +0.1817 | 0.0995 | ±0.1990 | +1.826 | 0.0678 | . |
| Hypertension | +0.7321 | 1.4265 | ±2.8530 | +0.513 | 0.6078 |  |
| High cholesterol | +1.2250 | 1.3286 | ±2.6573 | +0.922 | 0.3565 |  |
| Kidney disease | -2.3325 | 1.5912 | ±3.1824 | -1.466 | 0.1427 |  |
| Circulatory disease | -0.0631 | 1.5856 | ±3.1711 | -0.040 | 0.9683 |  |
| Any reading > 250 during wear (0/1) | +1.7822 | 1.2101 | ±2.4203 | +1.473 | 0.1408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.0750**, Adj R² = **0.0595**, F-statistic = **4.83** (p = **1.26e-08**), Residual SE = **17.143** on **834** df, AIC = **7249.2**, BIC = **7320.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1916** | 6.4653 | ±12.9307 | **+19.518** | **7.69e-85** | *** |
| **Education: graduate level (vs college)** | **-3.4726** | 1.2423 | ±2.4847 | **-2.795** | **0.0052** | ** |
| **Education: high school or below (vs college)** | **+5.4815** | 1.9993 | ±3.9986 | **+2.742** | **0.0061** | ** |
| Site: UCSD (vs UAB) | +2.9264 | 1.5543 | ±3.1086 | +1.883 | 0.0597 | . |
| Site: UW (vs UAB) | -1.3773 | 1.4132 | ±2.8264 | -0.975 | 0.3298 |  |
| Season: spring (vs autumn) | +2.4773 | 1.5149 | ±3.0299 | +1.635 | 0.1020 |  |
| Season: summer (vs autumn) | +2.4251 | 1.6429 | ±3.2858 | +1.476 | 0.1399 |  |
| **Season: winter (vs autumn)** | **+6.0927** | 1.8937 | ±3.7875 | **+3.217** | **0.0013** | ** |
| Age (years) | -0.1237 | 0.0675 | ±0.1350 | -1.832 | 0.0669 | . |
| BMI (kg/m2) | +0.1809 | 0.0981 | ±0.1963 | +1.843 | 0.0654 | . |
| Hypertension | +0.6656 | 1.4347 | ±2.8694 | +0.464 | 0.6427 |  |
| High cholesterol | +1.1407 | 1.3204 | ±2.6407 | +0.864 | 0.3876 |  |
| Kidney disease | -1.9070 | 1.5881 | ±3.1763 | -1.201 | 0.2298 |  |
| Circulatory disease | -0.0537 | 1.5856 | ±3.1711 | -0.034 | 0.9730 |  |
| Time > 250 (%) | -0.0714 | 0.0428 | ±0.0856 | -1.668 | 0.0954 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.0754**, Adj R² = **0.0599**, F-statistic = **4.86** (p = **1.08e-08**), Residual SE = **17.139** on **834** df, AIC = **7248.8**, BIC = **7320.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1514** | 6.4587 | ±12.9173 | **+19.532** | **5.86e-85** | *** |
| **Education: graduate level (vs college)** | **-3.4815** | 1.2425 | ±2.4850 | **-2.802** | **0.0051** | ** |
| **Education: high school or below (vs college)** | **+5.4946** | 1.9967 | ±3.9935 | **+2.752** | **0.0059** | ** |
| Site: UCSD (vs UAB) | +2.9116 | 1.5539 | ±3.1077 | +1.874 | 0.0610 | . |
| Site: UW (vs UAB) | -1.3809 | 1.4121 | ±2.8242 | -0.978 | 0.3281 |  |
| Season: spring (vs autumn) | +2.4894 | 1.5142 | ±3.0285 | +1.644 | 0.1002 |  |
| Season: summer (vs autumn) | +2.4299 | 1.6409 | ±3.2817 | +1.481 | 0.1386 |  |
| **Season: winter (vs autumn)** | **+6.1075** | 1.8920 | ±3.7840 | **+3.228** | **0.0012** | ** |
| Age (years) | -0.1230 | 0.0674 | ±0.1349 | -1.824 | 0.0682 | . |
| BMI (kg/m2) | +0.1813 | 0.0980 | ±0.1960 | +1.850 | 0.0643 | . |
| Hypertension | +0.6618 | 1.4345 | ±2.8689 | +0.461 | 0.6446 |  |
| High cholesterol | +1.1381 | 1.3201 | ±2.6402 | +0.862 | 0.3886 |  |
| Kidney disease | -1.8806 | 1.5858 | ±3.1716 | -1.186 | 0.2357 |  |
| Circulatory disease | -0.0424 | 1.5860 | ±3.1720 | -0.027 | 0.9787 |  |
| Avg. daily time > 250 (%) | -0.0761 | 0.0442 | ±0.0884 | -1.724 | 0.0848 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 747; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **747**, R² = **0.1694**, Adj R² = **0.1582**, F-statistic = **15.01** (p = **1.46e-24**), Residual SE = **4823.625** on **736** df, AIC = **14801.8**, BIC = **14852.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22896.8765** | 1631.3955 | ±3262.7910 | **+14.035** | **9.50e-45** | *** |
| Education: graduate level (vs college) | -696.2819 | 403.1870 | ±806.3740 | -1.727 | 0.0842 | . |
| Education: high school or below (vs college) | +437.7198 | 547.3088 | ±1094.6176 | +0.800 | 0.4238 |  |
| Site: UCSD (vs UAB) | +327.7064 | 456.4743 | ±912.9486 | +0.718 | 0.4728 |  |
| Site: UW (vs UAB) | +264.5933 | 441.0142 | ±882.0285 | +0.600 | 0.5485 |  |
| **Age (years)** | **-173.8411** | 17.7217 | ±35.4434 | **-9.810** | **1.02e-22** | *** |
| BMI (kg/m2) | -50.8967 | 27.7714 | ±55.5427 | -1.833 | 0.0668 | . |
| Hypertension | +133.3352 | 397.2713 | ±794.5426 | +0.336 | 0.7372 |  |
| High cholesterol | -93.0342 | 382.8025 | ±765.6049 | -0.243 | 0.8080 |  |
| **Kidney disease** | **-1301.2750** | 463.6459 | ±927.2918 | **-2.807** | **0.0050** | ** |
| **Circulatory disease** | **-1492.6051** | 382.7634 | ±765.5267 | **-3.900** | **9.64e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **747**, R² = **0.1718**, Adj R² = **0.1594**, F-statistic = **13.86** (p = **2.19e-24**), Residual SE = **4820.099** on **735** df, AIC = **14801.7**, BIC = **14857.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21750.8367** | 1846.5925 | ±3693.1850 | **+11.779** | **5.01e-32** | *** |
| Education: graduate level (vs college) | -648.4204 | 408.0994 | ±816.1987 | -1.589 | 0.1121 |  |
| Education: high school or below (vs college) | +359.0257 | 542.0590 | ±1084.1181 | +0.662 | 0.5078 |  |
| Site: UCSD (vs UAB) | +351.1726 | 455.8054 | ±911.6107 | +0.770 | 0.4410 |  |
| Site: UW (vs UAB) | +288.5321 | 441.5409 | ±883.0817 | +0.653 | 0.5135 |  |
| **Age (years)** | **-175.2586** | 17.8284 | ±35.6568 | **-9.830** | **8.34e-23** | *** |
| BMI (kg/m2) | -54.7609 | 27.9921 | ±55.9843 | -1.956 | 0.0504 | . |
| Hypertension | +122.1013 | 398.0673 | ±796.1347 | +0.307 | 0.7590 |  |
| High cholesterol | -82.2744 | 383.3416 | ±766.6832 | -0.215 | 0.8301 |  |
| **Kidney disease** | **-1293.8297** | 462.0113 | ±924.0227 | **-2.800** | **0.0051** | ** |
| **Circulatory disease** | **-1482.0097** | 382.7081 | ±765.4163 | **-3.872** | **1.08e-04** | *** |
| HbA1c (%) | +199.3120 | 157.7974 | ±315.5949 | +1.263 | 0.2066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **747**, R² = **0.1704**, Adj R² = **0.1579**, F-statistic = **13.72** (p = **3.98e-24**), Residual SE = **4824.255** on **735** df, AIC = **14803.0**, BIC = **14858.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22378.9938** | 1737.0707 | ±3474.1414 | **+12.883** | **5.60e-38** | *** |
| Education: graduate level (vs college) | -672.5696 | 407.6295 | ±815.2590 | -1.650 | 0.0990 | . |
| Education: high school or below (vs college) | +393.2181 | 539.3925 | ±1078.7850 | +0.729 | 0.4660 |  |
| Site: UCSD (vs UAB) | +345.6453 | 456.3398 | ±912.6795 | +0.757 | 0.4488 |  |
| Site: UW (vs UAB) | +273.5984 | 441.4005 | ±882.8010 | +0.620 | 0.5354 |  |
| **Age (years)** | **-174.7849** | 17.9268 | ±35.8536 | **-9.750** | **1.85e-22** | *** |
| BMI (kg/m2) | -52.1158 | 27.8907 | ±55.7813 | -1.869 | 0.0617 | . |
| Hypertension | +138.6660 | 397.2594 | ±794.5187 | +0.349 | 0.7270 |  |
| High cholesterol | -76.2155 | 384.6326 | ±769.2652 | -0.198 | 0.8429 |  |
| **Kidney disease** | **-1332.9725** | 468.9191 | ±937.8382 | **-2.843** | **0.0045** | ** |
| **Circulatory disease** | **-1499.3563** | 382.7487 | ±765.4974 | **-3.917** | **8.95e-05** | *** |
| Mean glucose (mg/dL) | +3.9022 | 5.0973 | ±10.1946 | +0.766 | 0.4440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **747**, R² = **0.1704**, Adj R² = **0.1579**, F-statistic = **13.72** (p = **3.98e-24**), Residual SE = **4824.255** on **735** df, AIC = **14803.0**, BIC = **14858.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21839.0207** | 2084.1413 | ±4168.2825 | **+10.479** | **1.08e-25** | *** |
| Education: graduate level (vs college) | -672.5696 | 407.6295 | ±815.2590 | -1.650 | 0.0990 | . |
| Education: high school or below (vs college) | +393.2181 | 539.3925 | ±1078.7850 | +0.729 | 0.4660 |  |
| Site: UCSD (vs UAB) | +345.6453 | 456.3398 | ±912.6795 | +0.757 | 0.4488 |  |
| Site: UW (vs UAB) | +273.5984 | 441.4005 | ±882.8010 | +0.620 | 0.5354 |  |
| **Age (years)** | **-174.7849** | 17.9268 | ±35.8536 | **-9.750** | **1.85e-22** | *** |
| BMI (kg/m2) | -52.1158 | 27.8907 | ±55.7813 | -1.869 | 0.0617 | . |
| Hypertension | +138.6660 | 397.2594 | ±794.5187 | +0.349 | 0.7270 |  |
| High cholesterol | -76.2155 | 384.6326 | ±769.2652 | -0.198 | 0.8429 |  |
| **Kidney disease** | **-1332.9725** | 468.9191 | ±937.8382 | **-2.843** | **0.0045** | ** |
| **Circulatory disease** | **-1499.3563** | 382.7487 | ±765.4974 | **-3.917** | **8.95e-05** | *** |
| GMI (%) | +163.1339 | 213.0987 | ±426.1973 | +0.766 | 0.4440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **747**, R² = **0.1718**, Adj R² = **0.1594**, F-statistic = **13.86** (p = **2.19e-24**), Residual SE = **4820.094** on **735** df, AIC = **14801.7**, BIC = **14857.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22075.7880** | 1748.2392 | ±3496.4784 | **+12.627** | **1.49e-36** | *** |
| Education: graduate level (vs college) | -659.5331 | 407.4757 | ±814.9514 | -1.619 | 0.1055 |  |
| Education: high school or below (vs college) | +364.3722 | 538.7331 | ±1077.4662 | +0.676 | 0.4988 |  |
| Site: UCSD (vs UAB) | +354.6826 | 455.1517 | ±910.3033 | +0.779 | 0.4358 |  |
| Site: UW (vs UAB) | +265.6078 | 441.4025 | ±882.8050 | +0.602 | 0.5473 |  |
| **Age (years)** | **-174.1165** | 17.7790 | ±35.5580 | **-9.793** | **1.20e-22** | *** |
| BMI (kg/m2) | -54.1982 | 28.0127 | ±56.0254 | -1.935 | 0.0530 | . |
| Hypertension | +144.2356 | 397.0354 | ±794.0708 | +0.363 | 0.7164 |  |
| High cholesterol | -64.2889 | 384.2368 | ±768.4736 | -0.167 | 0.8671 |  |
| **Kidney disease** | **-1327.9262** | 466.3595 | ±932.7191 | **-2.847** | **0.0044** | ** |
| **Circulatory disease** | **-1504.6844** | 382.4096 | ±764.8193 | **-3.935** | **8.33e-05** | *** |
| Nocturnal mean 00-06h (mg/dL) | +6.1736 | 5.2174 | ±10.4347 | +1.183 | 0.2367 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **747**, R² = **0.1697**, Adj R² = **0.1573**, F-statistic = **13.66** (p = **5.15e-24**), Residual SE = **4826.040** on **735** df, AIC = **14803.6**, BIC = **14859.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22732.9905** | 1648.3569 | ±3296.7138 | **+13.791** | **2.88e-43** | *** |
| Education: graduate level (vs college) | -681.7240 | 408.7397 | ±817.4794 | -1.668 | 0.0953 | . |
| Education: high school or below (vs college) | +406.3790 | 541.6726 | ±1083.3451 | +0.750 | 0.4531 |  |
| Site: UCSD (vs UAB) | +343.5407 | 455.7170 | ±911.4339 | +0.754 | 0.4509 |  |
| Site: UW (vs UAB) | +282.9836 | 440.7624 | ±881.5247 | +0.642 | 0.5209 |  |
| **Age (years)** | **-174.9726** | 18.2134 | ±36.4267 | **-9.607** | **7.48e-22** | *** |
| BMI (kg/m2) | -51.1117 | 27.8724 | ±55.7449 | -1.834 | 0.0667 | . |
| Hypertension | +132.6295 | 397.8787 | ±795.7574 | +0.333 | 0.7389 |  |
| High cholesterol | -81.8711 | 383.9312 | ±767.8624 | -0.213 | 0.8311 |  |
| **Kidney disease** | **-1343.1423** | 479.2337 | ±958.4673 | **-2.803** | **0.0051** | ** |
| **Circulatory disease** | **-1496.2134** | 382.8951 | ±765.7902 | **-3.908** | **9.32e-05** | *** |
| Glucose SD, pooled (mg/dL) | +6.7722 | 14.7360 | ±29.4720 | +0.460 | 0.6458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **747**, R² = **0.1696**, Adj R² = **0.1572**, F-statistic = **13.65** (p = **5.37e-24**), Residual SE = **4826.343** on **735** df, AIC = **14803.7**, BIC = **14859.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22752.7763** | 1654.3112 | ±3308.6224 | **+13.754** | **4.84e-43** | *** |
| Education: graduate level (vs college) | -685.4309 | 407.4998 | ±814.9997 | -1.682 | 0.0926 | . |
| Education: high school or below (vs college) | +410.7650 | 543.6482 | ±1087.2964 | +0.756 | 0.4499 |  |
| Site: UCSD (vs UAB) | +340.4434 | 455.9633 | ±911.9265 | +0.747 | 0.4553 |  |
| Site: UW (vs UAB) | +278.0785 | 440.8591 | ±881.7182 | +0.631 | 0.5282 |  |
| **Age (years)** | **-174.8281** | 18.2045 | ±36.4089 | **-9.604** | **7.72e-22** | *** |
| BMI (kg/m2) | -50.7032 | 27.8944 | ±55.7889 | -1.818 | 0.0691 | . |
| Hypertension | +133.6349 | 397.7053 | ±795.4106 | +0.336 | 0.7369 |  |
| High cholesterol | -84.4198 | 383.5568 | ±767.1135 | -0.220 | 0.8258 |  |
| **Kidney disease** | **-1336.6628** | 479.2294 | ±958.4589 | **-2.789** | **0.0053** | ** |
| **Circulatory disease** | **-1494.6490** | 382.8021 | ±765.6041 | **-3.904** | **9.44e-05** | *** |
| Avg. daily SD (mg/dL) | +6.2737 | 16.2929 | ±32.5859 | +0.385 | 0.7002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **747**, R² = **0.1695**, Adj R² = **0.1571**, F-statistic = **13.64** (p = **5.65e-24**), Residual SE = **4826.693** on **735** df, AIC = **14803.8**, BIC = **14859.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23036.5824** | 1690.5611 | ±3381.1223 | **+13.627** | **2.78e-42** | *** |
| Education: graduate level (vs college) | -700.9607 | 405.9293 | ±811.8586 | -1.727 | 0.0842 | . |
| Education: high school or below (vs college) | +450.5768 | 549.6316 | ±1099.2632 | +0.820 | 0.4123 |  |
| Site: UCSD (vs UAB) | +319.8540 | 455.9809 | ±911.9617 | +0.701 | 0.4830 |  |
| Site: UW (vs UAB) | +253.2318 | 442.3018 | ±884.6036 | +0.573 | 0.5670 |  |
| **Age (years)** | **-173.1734** | 18.0772 | ±36.1543 | **-9.580** | **9.74e-22** | *** |
| BMI (kg/m2) | -51.0606 | 27.8164 | ±55.6329 | -1.836 | 0.0664 | . |
| Hypertension | +136.2422 | 399.0820 | ±798.1639 | +0.341 | 0.7328 |  |
| High cholesterol | -96.8420 | 382.9440 | ±765.8879 | -0.253 | 0.8004 |  |
| **Kidney disease** | **-1279.5219** | 473.8578 | ±947.7156 | **-2.700** | **0.0069** | ** |
| **Circulatory disease** | **-1491.6986** | 383.1128 | ±766.2256 | **-3.894** | **9.88e-05** | *** |
| CV (%) | -7.8992 | 29.7658 | ±59.5316 | -0.265 | 0.7907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **747**, R² = **0.1703**, Adj R² = **0.1579**, F-statistic = **13.71** (p = **4.07e-24**), Residual SE = **4824.410** on **735** df, AIC = **14803.1**, BIC = **14858.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23614.0945** | 1859.1314 | ±3718.2627 | **+12.702** | **5.79e-37** | *** |
| Education: graduate level (vs college) | -681.3781 | 404.9398 | ±809.8796 | -1.683 | 0.0924 | . |
| Education: high school or below (vs college) | +390.5818 | 550.6083 | ±1101.2166 | +0.709 | 0.4781 |  |
| Site: UCSD (vs UAB) | +347.9004 | 455.8354 | ±911.6709 | +0.763 | 0.4453 |  |
| Site: UW (vs UAB) | +300.2516 | 441.6933 | ±883.3866 | +0.680 | 0.4966 |  |
| **Age (years)** | **-176.1961** | 18.1511 | ±36.3021 | **-9.707** | **2.81e-22** | *** |
| BMI (kg/m2) | -50.4738 | 27.8823 | ±55.7646 | -1.810 | 0.0703 | . |
| Hypertension | +121.6165 | 398.9982 | ±797.9964 | +0.305 | 0.7605 |  |
| High cholesterol | -83.4100 | 382.9152 | ±765.8304 | -0.218 | 0.8276 |  |
| **Kidney disease** | **-1363.1527** | 472.3450 | ±944.6899 | **-2.886** | **0.0039** | ** |
| **Circulatory disease** | **-1501.2116** | 382.9520 | ±765.9040 | **-3.920** | **8.85e-05** | *** |
| Mean / SD ratio | -119.9734 | 128.1409 | ±256.2818 | -0.936 | 0.3491 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **747**, R² = **0.1712**, Adj R² = **0.1588**, F-statistic = **13.80** (p = **2.80e-24**), Residual SE = **4821.803** on **735** df, AIC = **14802.3**, BIC = **14857.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23871.1806** | 1827.1086 | ±3654.2171 | **+13.065** | **5.22e-39** | *** |
| Education: graduate level (vs college) | -673.6459 | 403.5632 | ±807.1264 | -1.669 | 0.0951 | . |
| Education: high school or below (vs college) | +376.2582 | 551.7983 | ±1103.5967 | +0.682 | 0.4953 |  |
| Site: UCSD (vs UAB) | +342.5636 | 456.4261 | ±912.8522 | +0.751 | 0.4529 |  |
| Site: UW (vs UAB) | +306.8491 | 440.7354 | ±881.4708 | +0.696 | 0.4863 |  |
| **Age (years)** | **-177.4154** | 18.1602 | ±36.3205 | **-9.769** | **1.52e-22** | *** |
| BMI (kg/m2) | -49.0874 | 27.9129 | ±55.8259 | -1.759 | 0.0786 | . |
| Hypertension | +116.5335 | 398.2153 | ±796.4307 | +0.293 | 0.7698 |  |
| High cholesterol | -79.8816 | 382.7923 | ±765.5845 | -0.209 | 0.8347 |  |
| **Kidney disease** | **-1375.4271** | 468.5213 | ±937.0427 | **-2.936** | **0.0033** | ** |
| **Circulatory disease** | **-1493.1843** | 382.7394 | ±765.4788 | **-3.901** | **9.57e-05** | *** |
| Avg. daily mean/SD | -143.2049 | 101.5535 | ±203.1070 | -1.410 | 0.1585 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **747**, R² = **0.1743**, Adj R² = **0.1620**, F-statistic = **14.11** (p = **7.53e-25**), Residual SE = **4812.667** on **735** df, AIC = **14799.4**, BIC = **14854.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21268.7737** | 1792.1671 | ±3584.3343 | **+11.868** | **1.74e-32** | *** |
| Education: graduate level (vs college) | -636.0084 | 405.1868 | ±810.3736 | -1.570 | 0.1165 |  |
| Education: high school or below (vs college) | +359.3908 | 541.4294 | ±1082.8588 | +0.664 | 0.5068 |  |
| Site: UCSD (vs UAB) | +392.8607 | 455.4899 | ±910.9798 | +0.863 | 0.3884 |  |
| Site: UW (vs UAB) | +369.9061 | 438.8271 | ±877.6541 | +0.843 | 0.3993 |  |
| **Age (years)** | **-174.3463** | 17.7280 | ±35.4561 | **-9.834** | **8.00e-23** | *** |
| BMI (kg/m2) | -51.8612 | 27.9523 | ±55.9046 | -1.855 | 0.0635 | . |
| Hypertension | +149.6239 | 396.0529 | ±792.1058 | +0.378 | 0.7056 |  |
| High cholesterol | -70.1943 | 382.6215 | ±765.2430 | -0.183 | 0.8544 |  |
| **Kidney disease** | **-1395.7751** | 470.8287 | ±941.6575 | **-2.965** | **0.0030** | ** |
| **Circulatory disease** | **-1494.8572** | 382.9132 | ±765.8265 | **-3.904** | **9.47e-05** | *** |
| MAG (mg/dL/h) | +37.9425 | 20.9625 | ±41.9250 | +1.810 | 0.0703 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **747**, R² = **0.1700**, Adj R² = **0.1575**, F-statistic = **13.68** (p = **4.67e-24**), Residual SE = **4825.362** on **735** df, AIC = **14803.4**, BIC = **14858.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22551.9872** | 1695.1830 | ±3390.3660 | **+13.304** | **2.21e-40** | *** |
| Education: graduate level (vs college) | -677.5888 | 407.3966 | ±814.7933 | -1.663 | 0.0963 | . |
| Education: high school or below (vs college) | +393.9918 | 544.9396 | ±1089.8791 | +0.723 | 0.4697 |  |
| Site: UCSD (vs UAB) | +352.0563 | 456.1239 | ±912.2477 | +0.772 | 0.4402 |  |
| Site: UW (vs UAB) | +287.2043 | 441.2734 | ±882.5468 | +0.651 | 0.5151 |  |
| **Age (years)** | **-175.2866** | 18.1252 | ±36.2504 | **-9.671** | **4.01e-22** | *** |
| BMI (kg/m2) | -50.2859 | 27.9752 | ±55.9505 | -1.798 | 0.0723 | . |
| Hypertension | +140.0680 | 396.5404 | ±793.0807 | +0.353 | 0.7239 |  |
| High cholesterol | -81.7749 | 383.4524 | ±766.9049 | -0.213 | 0.8311 |  |
| **Kidney disease** | **-1359.6536** | 476.7443 | ±953.4886 | **-2.852** | **0.0043** | ** |
| **Circulatory disease** | **-1496.7565** | 382.6192 | ±765.2385 | **-3.912** | **9.16e-05** | *** |
| Avg. daily range (mg/dL) | +2.9345 | 4.5857 | ±9.1714 | +0.640 | 0.5222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **747**, R² = **0.1708**, Adj R² = **0.1584**, F-statistic = **13.77** (p = **3.26e-24**), Residual SE = **4822.856** on **735** df, AIC = **14802.6**, BIC = **14858.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22692.1613** | 1634.8769 | ±3269.7537 | **+13.880** | **8.37e-44** | *** |
| Education: graduate level (vs college) | -657.2874 | 412.3148 | ±824.6295 | -1.594 | 0.1109 |  |
| Education: high school or below (vs college) | +399.5646 | 541.0532 | ±1082.1064 | +0.738 | 0.4602 |  |
| Site: UCSD (vs UAB) | +345.9899 | 455.9964 | ±911.9928 | +0.759 | 0.4480 |  |
| Site: UW (vs UAB) | +298.2248 | 440.3825 | ±880.7651 | +0.677 | 0.4983 |  |
| **Age (years)** | **-174.3812** | 17.8353 | ±35.6707 | **-9.777** | **1.41e-22** | *** |
| BMI (kg/m2) | -52.9337 | 27.8968 | ±55.7937 | -1.897 | 0.0578 | . |
| Hypertension | +118.9547 | 398.3945 | ±796.7890 | +0.299 | 0.7653 |  |
| High cholesterol | -73.5656 | 383.8833 | ±767.7666 | -0.192 | 0.8480 |  |
| **Kidney disease** | **-1345.5166** | 471.4552 | ±942.9104 | **-2.854** | **0.0043** | ** |
| **Circulatory disease** | **-1520.9306** | 383.9905 | ±767.9810 | **-3.961** | **7.47e-05** | *** |
| SD of daily means (mg/dL) | +24.5974 | 26.0883 | ±52.1767 | +0.943 | 0.3458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **747**, R² = **0.1699**, Adj R² = **0.1575**, F-statistic = **13.68** (p = **4.81e-24**), Residual SE = **4825.568** on **735** df, AIC = **14803.4**, BIC = **14858.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23317.8506** | 1833.4971 | ±3666.9943 | **+12.718** | **4.72e-37** | *** |
| Education: graduate level (vs college) | -680.0611 | 408.1855 | ±816.3711 | -1.666 | 0.0957 | . |
| Education: high school or below (vs college) | +402.4416 | 538.6840 | ±1077.3679 | +0.747 | 0.4550 |  |
| Site: UCSD (vs UAB) | +349.7711 | 456.7396 | ±913.4793 | +0.766 | 0.4438 |  |
| Site: UW (vs UAB) | +274.2992 | 441.5300 | ±883.0600 | +0.621 | 0.5344 |  |
| **Age (years)** | **-174.8512** | 18.0352 | ±36.0704 | **-9.695** | **3.17e-22** | *** |
| BMI (kg/m2) | -51.9467 | 27.7827 | ±55.5655 | -1.870 | 0.0615 | . |
| Hypertension | +141.1427 | 396.9685 | ±793.9370 | +0.356 | 0.7222 |  |
| High cholesterol | -76.7589 | 384.1611 | ±768.3223 | -0.200 | 0.8416 |  |
| **Kidney disease** | **-1326.7829** | 471.0003 | ±942.0007 | **-2.817** | **0.0048** | ** |
| **Circulatory disease** | **-1500.6513** | 382.4438 | ±764.8875 | **-3.924** | **8.71e-05** | *** |
| Time in range 70-180, pooled (%) | -4.5107 | 8.2336 | ±16.4672 | -0.548 | 0.5838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **747**, R² = **0.1699**, Adj R² = **0.1575**, F-statistic = **13.68** (p = **4.75e-24**), Residual SE = **4825.478** on **735** df, AIC = **14803.4**, BIC = **14858.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23334.3898** | 1835.2933 | ±3670.5866 | **+12.714** | **4.93e-37** | *** |
| Education: graduate level (vs college) | -680.2590 | 407.9285 | ±815.8570 | -1.668 | 0.0954 | . |
| Education: high school or below (vs college) | +400.0161 | 538.2557 | ±1076.5114 | +0.743 | 0.4574 |  |
| Site: UCSD (vs UAB) | +351.5688 | 456.6527 | ±913.3054 | +0.770 | 0.4414 |  |
| Site: UW (vs UAB) | +274.4722 | 441.4662 | ±882.9323 | +0.622 | 0.5341 |  |
| **Age (years)** | **-174.9323** | 18.0500 | ±36.1001 | **-9.692** | **3.28e-22** | *** |
| BMI (kg/m2) | -51.9941 | 27.7999 | ±55.5997 | -1.870 | 0.0614 | . |
| Hypertension | +141.8673 | 397.0071 | ±794.0143 | +0.357 | 0.7208 |  |
| High cholesterol | -76.3837 | 384.2176 | ±768.4353 | -0.199 | 0.8424 |  |
| **Kidney disease** | **-1328.8688** | 471.3044 | ±942.6088 | **-2.820** | **0.0048** | ** |
| **Circulatory disease** | **-1500.8335** | 382.5661 | ±765.1321 | **-3.923** | **8.74e-05** | *** |
| Avg. daily time in range 70-180 (%) | -4.6362 | 8.1724 | ±16.3448 | -0.567 | 0.5705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **747**, R² = **0.1782**, Adj R² = **0.1659**, F-statistic = **14.49** (p = **1.47e-25**), Residual SE = **4801.356** on **735** df, AIC = **14795.9**, BIC = **14851.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23382.7068** | 1628.8125 | ±3257.6250 | **+14.356** | **9.82e-47** | *** |
| Education: graduate level (vs college) | -684.0118 | 400.8453 | ±801.6906 | -1.706 | 0.0879 | . |
| Education: high school or below (vs college) | +363.6285 | 545.8261 | ±1091.6522 | +0.666 | 0.5053 |  |
| Site: UCSD (vs UAB) | +203.6197 | 455.1447 | ±910.2895 | +0.447 | 0.6546 |  |
| Site: UW (vs UAB) | +159.0873 | 442.1534 | ±884.3068 | +0.360 | 0.7190 |  |
| **Age (years)** | **-177.5069** | 17.6599 | ±35.3199 | **-10.051** | **9.06e-24** | *** |
| BMI (kg/m2) | -47.6814 | 27.9522 | ±55.9045 | -1.706 | 0.0880 | . |
| Hypertension | +184.7941 | 397.9753 | ±795.9506 | +0.464 | 0.6424 |  |
| High cholesterol | -146.1653 | 381.5488 | ±763.0977 | -0.383 | 0.7017 |  |
| **Kidney disease** | **-1333.5765** | 461.6937 | ±923.3873 | **-2.888** | **0.0039** | ** |
| **Circulatory disease** | **-1419.8840** | 380.4074 | ±760.8148 | **-3.733** | **1.90e-04** | *** |
| **Any reading < 54 during wear (0/1)** | **-1131.2767** | 403.6328 | ±807.2656 | **-2.803** | **0.0051** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **747**, R² = **0.1752**, Adj R² = **0.1629**, F-statistic = **14.20** (p = **5.14e-25**), Residual SE = **4810.018** on **735** df, AIC = **14798.6**, BIC = **14854.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23015.2234** | 1631.6900 | ±3263.3799 | **+14.105** | **3.53e-45** | *** |
| Education: graduate level (vs college) | -723.3768 | 401.2761 | ±802.5522 | -1.803 | 0.0714 | . |
| Education: high school or below (vs college) | +369.9107 | 545.8583 | ±1091.7166 | +0.678 | 0.4980 |  |
| Site: UCSD (vs UAB) | +234.1810 | 457.6978 | ±915.3955 | +0.512 | 0.6089 |  |
| Site: UW (vs UAB) | +157.2025 | 443.3983 | ±886.7966 | +0.355 | 0.7229 |  |
| **Age (years)** | **-174.2916** | 17.6461 | ±35.2922 | **-9.877** | **5.23e-23** | *** |
| BMI (kg/m2) | -48.8254 | 28.0262 | ±56.0523 | -1.742 | 0.0815 | . |
| Hypertension | +169.0388 | 395.7161 | ±791.4321 | +0.427 | 0.6693 |  |
| High cholesterol | -110.3477 | 382.2705 | ±764.5410 | -0.289 | 0.7728 |  |
| **Kidney disease** | **-1329.1676** | 461.9566 | ±923.9132 | **-2.877** | **0.0040** | ** |
| **Circulatory disease** | **-1425.3355** | 382.4762 | ±764.9524 | **-3.727** | **1.94e-04** | *** |
| Time < 54 (%) | -909.1131 | 529.9611 | ±1059.9223 | -1.715 | 0.0863 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **747**, R² = **0.1747**, Adj R² = **0.1624**, F-statistic = **14.15** (p = **6.38e-25**), Residual SE = **4811.512** on **735** df, AIC = **14799.1**, BIC = **14854.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22943.4010** | 1626.9293 | ±3253.8587 | **+14.102** | **3.68e-45** | *** |
| Education: graduate level (vs college) | -731.8619 | 403.0806 | ±806.1613 | -1.816 | 0.0694 | . |
| Education: high school or below (vs college) | +384.5053 | 546.3726 | ±1092.7451 | +0.704 | 0.4816 |  |
| Site: UCSD (vs UAB) | +256.8384 | 457.5951 | ±915.1903 | +0.561 | 0.5746 |  |
| Site: UW (vs UAB) | +183.5070 | 441.9671 | ±883.9342 | +0.415 | 0.6780 |  |
| **Age (years)** | **-173.1045** | 17.6821 | ±35.3643 | **-9.790** | **1.25e-22** | *** |
| BMI (kg/m2) | -49.9559 | 27.7586 | ±55.5172 | -1.800 | 0.0719 | . |
| Hypertension | +159.0360 | 396.3108 | ±792.6216 | +0.401 | 0.6882 |  |
| High cholesterol | -121.0651 | 382.1148 | ±764.2296 | -0.317 | 0.7514 |  |
| **Kidney disease** | **-1318.2972** | 462.7717 | ±925.5435 | **-2.849** | **0.0044** | ** |
| **Circulatory disease** | **-1435.0309** | 381.8223 | ±763.6446 | **-3.758** | **1.71e-04** | *** |
| **Avg. daily time < 54 (%)** | **-824.9736** | 327.3777 | ±654.7554 | **-2.520** | **0.0117** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **747**, R² = **0.1746**, Adj R² = **0.1623**, F-statistic = **14.14** (p = **6.60e-25**), Residual SE = **4811.744** on **735** df, AIC = **14799.1**, BIC = **14854.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22962.2654** | 1631.6984 | ±3263.3968 | **+14.073** | **5.60e-45** | *** |
| Education: graduate level (vs college) | -738.0457 | 400.9982 | ±801.9965 | -1.841 | 0.0657 | . |
| Education: high school or below (vs college) | +437.2664 | 548.5601 | ±1097.1201 | +0.797 | 0.4254 |  |
| Site: UCSD (vs UAB) | +246.5928 | 454.5978 | ±909.1957 | +0.542 | 0.5875 |  |
| Site: UW (vs UAB) | +193.4040 | 440.5642 | ±881.1285 | +0.439 | 0.6607 |  |
| **Age (years)** | **-172.3954** | 17.7036 | ±35.4073 | **-9.738** | **2.08e-22** | *** |
| BMI (kg/m2) | -50.0575 | 28.0908 | ±56.1815 | -1.782 | 0.0748 | . |
| Hypertension | +151.7451 | 395.5419 | ±791.0838 | +0.384 | 0.7012 |  |
| High cholesterol | -108.9446 | 382.3668 | ±764.7335 | -0.285 | 0.7757 |  |
| **Kidney disease** | **-1315.3352** | 460.6518 | ±921.3035 | **-2.855** | **0.0043** | ** |
| **Circulatory disease** | **-1460.8141** | 383.5404 | ±767.0808 | **-3.809** | **1.40e-04** | *** |
| **Time 54-69, pooled (%)** | **-252.3201** | 92.5968 | ±185.1936 | **-2.725** | **0.0064** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **747**, R² = **0.1752**, Adj R² = **0.1628**, F-statistic = **14.19** (p = **5.33e-25**), Residual SE = **4810.261** on **735** df, AIC = **14798.7**, BIC = **14854.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22914.9666** | 1631.2593 | ±3262.5186 | **+14.047** | **7.99e-45** | *** |
| Education: graduate level (vs college) | -738.7756 | 401.3398 | ±802.6796 | -1.841 | 0.0657 | . |
| Education: high school or below (vs college) | +444.6294 | 548.0661 | ±1096.1323 | +0.811 | 0.4172 |  |
| Site: UCSD (vs UAB) | +252.0299 | 454.9439 | ±909.8878 | +0.554 | 0.5796 |  |
| Site: UW (vs UAB) | +195.5482 | 441.1951 | ±882.3902 | +0.443 | 0.6576 |  |
| **Age (years)** | **-171.7073** | 17.7277 | ±35.4554 | **-9.686** | **3.46e-22** | *** |
| BMI (kg/m2) | -50.1341 | 28.0107 | ±56.0215 | -1.790 | 0.0735 | . |
| Hypertension | +152.7561 | 395.5525 | ±791.1049 | +0.386 | 0.6994 |  |
| High cholesterol | -110.8565 | 382.0943 | ±764.1886 | -0.290 | 0.7717 |  |
| **Kidney disease** | **-1317.9167** | 460.9099 | ±921.8199 | **-2.859** | **0.0042** | ** |
| **Circulatory disease** | **-1462.0073** | 383.4636 | ±766.9271 | **-3.813** | **1.37e-04** | *** |
| **Avg. daily time 54-69 (%)** | **-253.7134** | 86.9968 | ±173.9937 | **-2.916** | **0.0035** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **747**, R² = **0.1754**, Adj R² = **0.1631**, F-statistic = **14.22** (p = **4.74e-25**), Residual SE = **4809.453** on **735** df, AIC = **14798.4**, BIC = **14853.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22983.2364** | 1631.2686 | ±3262.5372 | **+14.089** | **4.43e-45** | *** |
| Education: graduate level (vs college) | -739.6078 | 400.8049 | ±801.6098 | -1.845 | 0.0650 | . |
| Education: high school or below (vs college) | +420.7763 | 547.8631 | ±1095.7261 | +0.768 | 0.4425 |  |
| Site: UCSD (vs UAB) | +233.5791 | 454.9516 | ±909.9032 | +0.513 | 0.6077 |  |
| Site: UW (vs UAB) | +175.8074 | 440.6526 | ±881.3052 | +0.399 | 0.6899 |  |
| **Age (years)** | **-172.6801** | 17.6743 | ±35.3486 | **-9.770** | **1.51e-22** | *** |
| BMI (kg/m2) | -49.6536 | 28.1038 | ±56.2075 | -1.767 | 0.0773 | . |
| Hypertension | +158.2310 | 395.2084 | ±790.4168 | +0.400 | 0.6889 |  |
| High cholesterol | -111.2456 | 382.1520 | ±764.3040 | -0.291 | 0.7710 |  |
| **Kidney disease** | **-1320.4411** | 460.5241 | ±921.0482 | **-2.867** | **0.0041** | ** |
| **Circulatory disease** | **-1448.2439** | 383.5137 | ±767.0275 | **-3.776** | **1.59e-04** | *** |
| **Time < 70 (%)** | **-221.8172** | 78.5558 | ±157.1117 | **-2.824** | **0.0047** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **747**, R² = **0.1758**, Adj R² = **0.1635**, F-statistic = **14.25** (p = **4.06e-25**), Residual SE = **4808.375** on **735** df, AIC = **14798.1**, BIC = **14853.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22924.9532** | 1629.7105 | ±3259.4209 | **+14.067** | **6.07e-45** | *** |
| Education: graduate level (vs college) | -742.5901 | 401.5652 | ±803.1304 | -1.849 | 0.0644 | . |
| Education: high school or below (vs college) | +429.5251 | 547.2210 | ±1094.4419 | +0.785 | 0.4325 |  |
| Site: UCSD (vs UAB) | +243.2368 | 455.4016 | ±910.8032 | +0.534 | 0.5933 |  |
| Site: UW (vs UAB) | +183.1472 | 441.1941 | ±882.3881 | +0.415 | 0.6781 |  |
| **Age (years)** | **-171.7956** | 17.7083 | ±35.4166 | **-9.701** | **2.97e-22** | *** |
| BMI (kg/m2) | -49.9851 | 27.9668 | ±55.9336 | -1.787 | 0.0739 | . |
| Hypertension | +157.0153 | 395.4467 | ±790.8934 | +0.397 | 0.6913 |  |
| High cholesterol | -115.9499 | 381.8327 | ±763.6654 | -0.304 | 0.7614 |  |
| **Kidney disease** | **-1320.2336** | 460.9883 | ±921.9766 | **-2.864** | **0.0042** | ** |
| **Circulatory disease** | **-1450.7442** | 383.2088 | ±766.4176 | **-3.786** | **1.53e-04** | *** |
| **Avg. daily time < 70 (%)** | **-219.8705** | 67.9469 | ±135.8938 | **-3.236** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **747**, R² = **0.1697**, Adj R² = **0.1573**, F-statistic = **13.66** (p = **5.13e-24**), Residual SE = **4826.015** on **735** df, AIC = **14803.6**, BIC = **14859.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22338.8189** | 2147.4479 | ±4294.8958 | **+10.402** | **2.42e-25** | *** |
| Education: graduate level (vs college) | -714.3731 | 410.8365 | ±821.6730 | -1.739 | 0.0821 | . |
| Education: high school or below (vs college) | +460.7446 | 538.4174 | ±1076.8349 | +0.856 | 0.3921 |  |
| Site: UCSD (vs UAB) | +316.1577 | 455.3581 | ±910.7163 | +0.694 | 0.4875 |  |
| Site: UW (vs UAB) | +248.1186 | 440.8835 | ±881.7671 | +0.563 | 0.5736 |  |
| **Age (years)** | **-174.0084** | 17.7125 | ±35.4250 | **-9.824** | **8.87e-23** | *** |
| BMI (kg/m2) | -50.2496 | 27.8019 | ±55.6039 | -1.807 | 0.0707 | . |
| Hypertension | +136.2106 | 397.7303 | ±795.4605 | +0.342 | 0.7320 |  |
| High cholesterol | -101.9916 | 384.3880 | ±768.7761 | -0.265 | 0.7908 |  |
| **Kidney disease** | **-1285.8397** | 467.4576 | ±934.9153 | **-2.751** | **0.0059** | ** |
| **Circulatory disease** | **-1488.7977** | 383.9093 | ±767.8186 | **-3.878** | **1.05e-04** | *** |
| Time 54-250, pooled (%) | +5.9898 | 13.6854 | ±27.3709 | +0.438 | 0.6616 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **747**, R² = **0.1697**, Adj R² = **0.1573**, F-statistic = **13.65** (p = **5.27e-24**), Residual SE = **4826.209** on **735** df, AIC = **14803.6**, BIC = **14859.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22390.5476** | 2131.0647 | ±4262.1294 | **+10.507** | **8.04e-26** | *** |
| Education: graduate level (vs college) | -712.0607 | 410.8516 | ±821.7033 | -1.733 | 0.0831 | . |
| Education: high school or below (vs college) | +457.9560 | 538.9578 | ±1077.9156 | +0.850 | 0.3955 |  |
| Site: UCSD (vs UAB) | +317.2452 | 455.4804 | ±910.9608 | +0.697 | 0.4861 |  |
| Site: UW (vs UAB) | +250.5440 | 440.9178 | ±881.8356 | +0.568 | 0.5699 |  |
| **Age (years)** | **-173.9162** | 17.7316 | ±35.4633 | **-9.808** | **1.04e-22** | *** |
| BMI (kg/m2) | -50.3082 | 27.7907 | ±55.5814 | -1.810 | 0.0703 | . |
| Hypertension | +135.3974 | 397.7765 | ±795.5530 | +0.340 | 0.7336 |  |
| High cholesterol | -101.0486 | 384.3369 | ±768.6739 | -0.263 | 0.7926 |  |
| **Kidney disease** | **-1286.3387** | 467.7790 | ±935.5580 | **-2.750** | **0.0060** | ** |
| **Circulatory disease** | **-1488.4758** | 383.8131 | ±767.6262 | **-3.878** | **1.05e-04** | *** |
| Avg. daily time 54-250 (%) | +5.3681 | 13.3649 | ±26.7299 | +0.402 | 0.6879 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **747**, R² = **0.1730**, Adj R² = **0.1606**, F-statistic = **13.98** (p = **1.32e-24**), Residual SE = **4816.545** on **735** df, AIC = **14800.6**, BIC = **14856.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22905.4757** | 1637.6807 | ±3275.3614 | **+13.987** | **1.88e-44** | *** |
| Education: graduate level (vs college) | -687.8761 | 402.3613 | ±804.7226 | -1.710 | 0.0873 | . |
| Education: high school or below (vs college) | +356.1963 | 544.6885 | ±1089.3770 | +0.654 | 0.5131 |  |
| Site: UCSD (vs UAB) | +381.8415 | 457.0044 | ±914.0089 | +0.836 | 0.4034 |  |
| Site: UW (vs UAB) | +246.5459 | 441.6357 | ±883.2714 | +0.558 | 0.5767 |  |
| **Age (years)** | **-178.8846** | 18.1247 | ±36.2493 | **-9.870** | **5.63e-23** | *** |
| BMI (kg/m2) | -53.3844 | 27.7990 | ±55.5979 | -1.920 | 0.0548 | . |
| Hypertension | +180.1305 | 393.8982 | ±787.7964 | +0.457 | 0.6475 |  |
| High cholesterol | -51.0378 | 382.3929 | ±764.7858 | -0.133 | 0.8938 |  |
| **Kidney disease** | **-1365.4844** | 469.0337 | ±938.0674 | **-2.911** | **0.0036** | ** |
| **Circulatory disease** | **-1513.5489** | 381.8315 | ±763.6630 | **-3.964** | **7.37e-05** | *** |
| Time 181-250, pooled (%) | +20.4892 | 12.1873 | ±24.3747 | +1.681 | 0.0927 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **747**, R² = **0.1729**, Adj R² = **0.1605**, F-statistic = **13.96** (p = **1.40e-24**), Residual SE = **4816.980** on **735** df, AIC = **14800.8**, BIC = **14856.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22899.1917** | 1638.3324 | ±3276.6648 | **+13.977** | **2.15e-44** | *** |
| Education: graduate level (vs college) | -689.3998 | 402.4148 | ±804.8297 | -1.713 | 0.0867 | . |
| Education: high school or below (vs college) | +352.2677 | 542.8553 | ±1085.7106 | +0.649 | 0.5164 |  |
| Site: UCSD (vs UAB) | +384.8629 | 456.9422 | ±913.8845 | +0.842 | 0.3996 |  |
| Site: UW (vs UAB) | +249.6428 | 441.7732 | ±883.5465 | +0.565 | 0.5720 |  |
| **Age (years)** | **-178.5903** | 18.1285 | ±36.2570 | **-9.851** | **6.76e-23** | *** |
| BMI (kg/m2) | -53.3419 | 27.8521 | ±55.7042 | -1.915 | 0.0555 | . |
| Hypertension | +178.6886 | 394.6166 | ±789.2332 | +0.453 | 0.6507 |  |
| High cholesterol | -53.0585 | 382.7237 | ±765.4474 | -0.139 | 0.8897 |  |
| **Kidney disease** | **-1365.0364** | 469.2198 | ±938.4396 | **-2.909** | **0.0036** | ** |
| **Circulatory disease** | **-1510.0480** | 382.3670 | ±764.7340 | **-3.949** | **7.84e-05** | *** |
| Avg. daily time 181-250 (%) | +19.7100 | 12.0370 | ±24.0740 | +1.637 | 0.1015 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **747**, R² = **0.1702**, Adj R² = **0.1577**, F-statistic = **13.70** (p = **4.32e-24**), Residual SE = **4824.815** on **735** df, AIC = **14803.2**, BIC = **14858.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22861.8764** | 1635.7458 | ±3271.4917 | **+13.976** | **2.17e-44** | *** |
| Education: graduate level (vs college) | -677.3349 | 407.5781 | ±815.1562 | -1.662 | 0.0965 | . |
| Education: high school or below (vs college) | +393.7203 | 538.5466 | ±1077.0932 | +0.731 | 0.4647 |  |
| Site: UCSD (vs UAB) | +352.5955 | 456.5501 | ±913.1002 | +0.772 | 0.4399 |  |
| Site: UW (vs UAB) | +274.3515 | 441.5543 | ±883.1085 | +0.621 | 0.5344 |  |
| **Age (years)** | **-175.0596** | 18.0131 | ±36.0263 | **-9.718** | **2.52e-22** | *** |
| BMI (kg/m2) | -52.1624 | 27.8078 | ±55.6155 | -1.876 | 0.0607 | . |
| Hypertension | +143.6039 | 396.8475 | ±793.6949 | +0.362 | 0.7175 |  |
| High cholesterol | -73.3891 | 384.1064 | ±768.2127 | -0.191 | 0.8485 |  |
| **Kidney disease** | **-1333.2626** | 471.0464 | ±942.0928 | **-2.830** | **0.0046** | ** |
| **Circulatory disease** | **-1501.4292** | 382.4323 | ±764.8646 | **-3.926** | **8.64e-05** | *** |
| Time > 180 (%) | +5.5714 | 8.1218 | ±16.2436 | +0.686 | 0.4927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **747**, R² = **0.1702**, Adj R² = **0.1578**, F-statistic = **13.71** (p = **4.21e-24**), Residual SE = **4824.639** on **735** df, AIC = **14803.1**, BIC = **14858.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22865.0611** | 1636.0713 | ±3272.1426 | **+13.976** | **2.20e-44** | *** |
| Education: graduate level (vs college) | -677.5206 | 407.3120 | ±814.6240 | -1.663 | 0.0962 | . |
| Education: high school or below (vs college) | +390.4918 | 538.0660 | ±1076.1319 | +0.726 | 0.4680 |  |
| Site: UCSD (vs UAB) | +355.2394 | 456.4508 | ±912.9017 | +0.778 | 0.4364 |  |
| Site: UW (vs UAB) | +274.7699 | 441.5088 | ±883.0176 | +0.622 | 0.5337 |  |
| **Age (years)** | **-175.1479** | 18.0205 | ±36.0410 | **-9.719** | **2.49e-22** | *** |
| BMI (kg/m2) | -52.2411 | 27.8236 | ±55.6472 | -1.878 | 0.0604 | . |
| Hypertension | +144.5964 | 396.8779 | ±793.7558 | +0.364 | 0.7156 |  |
| High cholesterol | -72.8752 | 384.1966 | ±768.3931 | -0.190 | 0.8496 |  |
| **Kidney disease** | **-1336.1801** | 471.3883 | ±942.7766 | **-2.835** | **0.0046** | ** |
| **Circulatory disease** | **-1501.7644** | 382.5340 | ±765.0681 | **-3.926** | **8.64e-05** | *** |
| Avg. daily time > 180 (%) | +5.7809 | 8.0754 | ±16.1509 | +0.716 | 0.4741 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **747**, R² = **0.1703**, Adj R² = **0.1579**, F-statistic = **13.72** (p = **4.00e-24**), Residual SE = **4824.286** on **735** df, AIC = **14803.0**, BIC = **14858.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22868.2534** | 1638.3757 | ±3276.7515 | **+13.958** | **2.82e-44** | *** |
| Education: graduate level (vs college) | -669.7610 | 410.0107 | ±820.0213 | -1.634 | 0.1024 |  |
| Education: high school or below (vs college) | +390.0850 | 537.8147 | ±1075.6295 | +0.725 | 0.4683 |  |
| Site: UCSD (vs UAB) | +357.8062 | 455.0776 | ±910.1552 | +0.786 | 0.4317 |  |
| Site: UW (vs UAB) | +273.1026 | 441.4885 | ±882.9770 | +0.619 | 0.5362 |  |
| **Age (years)** | **-174.3793** | 17.8329 | ±35.6658 | **-9.779** | **1.39e-22** | *** |
| BMI (kg/m2) | -53.3545 | 27.8002 | ±55.6004 | -1.919 | 0.0550 | . |
| Hypertension | +143.3720 | 396.9726 | ±793.9452 | +0.361 | 0.7180 |  |
| High cholesterol | -65.7334 | 384.5669 | ±769.1338 | -0.171 | 0.8643 |  |
| **Kidney disease** | **-1329.1855** | 469.7470 | ±939.4941 | **-2.830** | **0.0047** | ** |
| **Circulatory disease** | **-1504.9735** | 382.2710 | ±764.5419 | **-3.937** | **8.25e-05** | *** |
| Nocturnal time > 180 (%) | +5.9740 | 7.9222 | ±15.8444 | +0.754 | 0.4508 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **747**, R² = **0.1716**, Adj R² = **0.1592**, F-statistic = **13.84** (p = **2.39e-24**), Residual SE = **4820.682** on **735** df, AIC = **14801.9**, BIC = **14857.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22774.2808** | 1636.6457 | ±3273.2913 | **+13.915** | **5.12e-44** | *** |
| Education: graduate level (vs college) | -657.8749 | 406.0707 | ±812.1415 | -1.620 | 0.1052 |  |
| Education: high school or below (vs college) | +399.5804 | 549.0796 | ±1098.1593 | +0.728 | 0.4668 |  |
| Site: UCSD (vs UAB) | +355.6094 | 456.0517 | ±912.1034 | +0.780 | 0.4355 |  |
| Site: UW (vs UAB) | +248.6755 | 441.5916 | ±883.1833 | +0.563 | 0.5733 |  |
| **Age (years)** | **-178.2321** | 18.3404 | ±36.6808 | **-9.718** | **2.53e-22** | *** |
| BMI (kg/m2) | -49.5975 | 28.0635 | ±56.1270 | -1.767 | 0.0772 | . |
| Hypertension | +152.1352 | 395.2994 | ±790.5989 | +0.385 | 0.7003 |  |
| High cholesterol | -79.2242 | 383.2390 | ±766.4781 | -0.207 | 0.8362 |  |
| **Kidney disease** | **-1366.4884** | 471.3200 | ±942.6400 | **-2.899** | **0.0037** | ** |
| **Circulatory disease** | **-1476.8169** | 384.9705 | ±769.9409 | **-3.836** | **1.25e-04** | *** |
| Any reading > 250 during wear (0/1) | +519.8984 | 392.8283 | ±785.6567 | +1.323 | 0.1857 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **747**, R² = **0.1697**, Adj R² = **0.1572**, F-statistic = **13.65** (p = **5.28e-24**), Residual SE = **4826.225** on **735** df, AIC = **14803.6**, BIC = **14859.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22931.9174** | 1629.6113 | ±3259.2225 | **+14.072** | **5.64e-45** | *** |
| Education: graduate level (vs college) | -711.9180 | 410.6987 | ±821.3974 | -1.733 | 0.0830 | . |
| Education: high school or below (vs college) | +458.2083 | 538.2245 | ±1076.4489 | +0.851 | 0.3946 |  |
| Site: UCSD (vs UAB) | +318.1634 | 455.4314 | ±910.8629 | +0.699 | 0.4848 |  |
| Site: UW (vs UAB) | +250.8300 | 440.8972 | ±881.7944 | +0.569 | 0.5694 |  |
| **Age (years)** | **-173.9845** | 17.7142 | ±35.4284 | **-9.822** | **9.07e-23** | *** |
| BMI (kg/m2) | -50.3437 | 27.8067 | ±55.6134 | -1.810 | 0.0702 | . |
| Hypertension | +135.6398 | 397.7464 | ±795.4927 | +0.341 | 0.7331 |  |
| High cholesterol | -100.7536 | 384.3886 | ±768.7772 | -0.262 | 0.7932 |  |
| **Kidney disease** | **-1287.6410** | 467.5993 | ±935.1986 | **-2.754** | **0.0059** | ** |
| **Circulatory disease** | **-1489.6684** | 383.8715 | ±767.7429 | **-3.881** | **1.04e-04** | *** |
| Time > 250 (%) | -5.2285 | 13.6940 | ±27.3880 | -0.382 | 0.7026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 747)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **747**, R² = **0.1696**, Adj R² = **0.1572**, F-statistic = **13.65** (p = **5.41e-24**), Residual SE = **4826.395** on **735** df, AIC = **14803.7**, BIC = **14859.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22922.6886** | 1630.3462 | ±3260.6923 | **+14.060** | **6.69e-45** | *** |
| Education: graduate level (vs college) | -709.5816 | 410.6517 | ±821.3034 | -1.728 | 0.0840 | . |
| Education: high school or below (vs college) | +455.3269 | 538.8251 | ±1077.6502 | +0.845 | 0.3981 |  |
| Site: UCSD (vs UAB) | +319.1519 | 455.5202 | ±911.0405 | +0.701 | 0.4835 |  |
| Site: UW (vs UAB) | +253.0263 | 440.9389 | ±881.8778 | +0.574 | 0.5661 |  |
| **Age (years)** | **-173.9095** | 17.7309 | ±35.4618 | **-9.808** | **1.04e-22** | *** |
| BMI (kg/m2) | -50.3985 | 27.7962 | ±55.5924 | -1.813 | 0.0698 | . |
| Hypertension | +134.9562 | 397.7844 | ±795.5689 | +0.339 | 0.7344 |  |
| High cholesterol | -99.7340 | 384.3377 | ±768.6754 | -0.259 | 0.7953 |  |
| **Kidney disease** | **-1288.4031** | 467.9006 | ±935.8012 | **-2.754** | **0.0059** | ** |
| **Circulatory disease** | **-1489.3932** | 383.7776 | ±767.5552 | **-3.881** | **1.04e-04** | *** |
| Avg. daily time > 250 (%) | -4.5920 | 13.3843 | ±26.7685 | -0.343 | 0.7315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 747; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **747**, R² = **0.1910**, Adj R² = **0.1800**, F-statistic = **17.37** (p = **1.48e-28**), Residual SE = **13.823** on **736** df, AIC = **6054.5**, BIC = **6105.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3074** | 4.7080 | ±9.4161 | **+12.809** | **1.45e-37** | *** |
| Education: graduate level (vs college) | -2.2136 | 1.1666 | ±2.3331 | -1.898 | 0.0578 | . |
| Education: high school or below (vs college) | +1.7628 | 1.6022 | ±3.2044 | +1.100 | 0.2712 |  |
| Site: UCSD (vs UAB) | +0.7415 | 1.3242 | ±2.6484 | +0.560 | 0.5755 |  |
| Site: UW (vs UAB) | +0.8747 | 1.2298 | ±2.4595 | +0.711 | 0.4769 |  |
| **Age (years)** | **-0.5398** | 0.0496 | ±0.0992 | **-10.886** | **1.35e-27** | *** |
| BMI (kg/m2) | -0.0210 | 0.0817 | ±0.1634 | -0.257 | 0.7971 |  |
| Hypertension | +0.0438 | 1.1606 | ±2.3211 | +0.038 | 0.9699 |  |
| High cholesterol | -0.1091 | 1.0666 | ±2.1331 | -0.102 | 0.9185 |  |
| **Kidney disease** | **-2.6392** | 1.3318 | ±2.6637 | **-1.982** | **0.0475** | * |
| **Circulatory disease** | **-3.8092** | 1.1154 | ±2.2307 | **-3.415** | **6.37e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **747**, R² = **0.1932**, Adj R² = **0.1811**, F-statistic = **16.00** (p = **2.44e-28**), Residual SE = **13.813** on **735** df, AIC = **6054.5**, BIC = **6109.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.0702** | 5.2039 | ±10.4077 | **+10.967** | **5.51e-28** | *** |
| Education: graduate level (vs college) | -2.0785 | 1.1761 | ±2.3522 | -1.767 | 0.0772 | . |
| Education: high school or below (vs college) | +1.5405 | 1.5987 | ±3.1974 | +0.964 | 0.3352 |  |
| Site: UCSD (vs UAB) | +0.8078 | 1.3194 | ±2.6389 | +0.612 | 0.5404 |  |
| Site: UW (vs UAB) | +0.9423 | 1.2312 | ±2.4623 | +0.765 | 0.4441 |  |
| **Age (years)** | **-0.5438** | 0.0499 | ±0.0998 | **-10.904** | **1.11e-27** | *** |
| BMI (kg/m2) | -0.0319 | 0.0823 | ±0.1646 | -0.388 | 0.6981 |  |
| Hypertension | +0.0121 | 1.1621 | ±2.3242 | +0.010 | 0.9917 |  |
| High cholesterol | -0.0788 | 1.0677 | ±2.1355 | -0.074 | 0.9412 |  |
| **Kidney disease** | **-2.6182** | 1.3232 | ±2.6464 | **-1.979** | **0.0479** | * |
| **Circulatory disease** | **-3.7793** | 1.1132 | ±2.2263 | **-3.395** | **6.86e-04** | *** |
| HbA1c (%) | +0.5630 | 0.4231 | ±0.8462 | +1.331 | 0.1833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **747**, R² = **0.1913**, Adj R² = **0.1792**, F-statistic = **15.80** (p = **5.59e-28**), Residual SE = **13.830** on **735** df, AIC = **6056.3**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4489** | 4.8992 | ±9.7984 | **+12.134** | **6.94e-34** | *** |
| Education: graduate level (vs college) | -2.1743 | 1.1814 | ±2.3627 | -1.841 | 0.0657 | . |
| Education: high school or below (vs college) | +1.6890 | 1.5911 | ±3.1823 | +1.062 | 0.2885 |  |
| Site: UCSD (vs UAB) | +0.7712 | 1.3206 | ±2.6412 | +0.584 | 0.5592 |  |
| Site: UW (vs UAB) | +0.8896 | 1.2290 | ±2.4580 | +0.724 | 0.4692 |  |
| **Age (years)** | **-0.5414** | 0.0503 | ±0.1005 | **-10.772** | **4.65e-27** | *** |
| BMI (kg/m2) | -0.0230 | 0.0820 | ±0.1641 | -0.281 | 0.7789 |  |
| Hypertension | +0.0527 | 1.1602 | ±2.3205 | +0.045 | 0.9638 |  |
| High cholesterol | -0.0813 | 1.0702 | ±2.1404 | -0.076 | 0.9395 |  |
| **Kidney disease** | **-2.6918** | 1.3431 | ±2.6862 | **-2.004** | **0.0451** | * |
| **Circulatory disease** | **-3.8204** | 1.1158 | ±2.2316 | **-3.424** | **6.17e-04** | *** |
| Mean glucose (mg/dL) | +0.0065 | 0.0141 | ±0.0283 | +0.458 | 0.6472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **747**, R² = **0.1913**, Adj R² = **0.1792**, F-statistic = **15.80** (p = **5.59e-28**), Residual SE = **13.830** on **735** df, AIC = **6056.3**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5537** | 5.7683 | ±11.5366 | **+10.151** | **3.28e-24** | *** |
| Education: graduate level (vs college) | -2.1743 | 1.1814 | ±2.3627 | -1.841 | 0.0657 | . |
| Education: high school or below (vs college) | +1.6890 | 1.5911 | ±3.1823 | +1.062 | 0.2885 |  |
| Site: UCSD (vs UAB) | +0.7712 | 1.3206 | ±2.6412 | +0.584 | 0.5592 |  |
| Site: UW (vs UAB) | +0.8896 | 1.2290 | ±2.4580 | +0.724 | 0.4692 |  |
| **Age (years)** | **-0.5414** | 0.0503 | ±0.1005 | **-10.772** | **4.65e-27** | *** |
| BMI (kg/m2) | -0.0230 | 0.0820 | ±0.1641 | -0.281 | 0.7789 |  |
| Hypertension | +0.0527 | 1.1602 | ±2.3205 | +0.045 | 0.9638 |  |
| High cholesterol | -0.0813 | 1.0702 | ±2.1404 | -0.076 | 0.9395 |  |
| **Kidney disease** | **-2.6918** | 1.3431 | ±2.6862 | **-2.004** | **0.0451** | * |
| **Circulatory disease** | **-3.8204** | 1.1158 | ±2.2316 | **-3.424** | **6.17e-04** | *** |
| GMI (%) | +0.2704 | 0.5908 | ±1.1817 | +0.458 | 0.6472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **747**, R² = **0.1922**, Adj R² = **0.1801**, F-statistic = **15.89** (p = **3.82e-28**), Residual SE = **13.822** on **735** df, AIC = **6055.4**, BIC = **6110.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6147** | 4.9311 | ±9.8622 | **+11.887** | **1.39e-32** | *** |
| Education: graduate level (vs college) | -2.1379 | 1.1809 | ±2.3618 | -1.810 | 0.0702 | . |
| Education: high school or below (vs college) | +1.6116 | 1.5923 | ±3.1847 | +1.012 | 0.3115 |  |
| Site: UCSD (vs UAB) | +0.7971 | 1.3176 | ±2.6353 | +0.605 | 0.5452 |  |
| Site: UW (vs UAB) | +0.8768 | 1.2323 | ±2.4647 | +0.711 | 0.4768 |  |
| **Age (years)** | **-0.5404** | 0.0498 | ±0.0996 | **-10.851** | **1.97e-27** | *** |
| BMI (kg/m2) | -0.0278 | 0.0823 | ±0.1647 | -0.338 | 0.7355 |  |
| Hypertension | +0.0663 | 1.1595 | ±2.3191 | +0.057 | 0.9544 |  |
| High cholesterol | -0.0499 | 1.0707 | ±2.1414 | -0.047 | 0.9628 |  |
| **Kidney disease** | **-2.6942** | 1.3361 | ±2.6722 | **-2.016** | **0.0438** | * |
| **Circulatory disease** | **-3.8341** | 1.1147 | ±2.2294 | **-3.440** | **5.83e-04** | *** |
| Nocturnal mean 00-06h (mg/dL) | +0.0127 | 0.0146 | ±0.0293 | +0.869 | 0.3846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **747**, R² = **0.1913**, Adj R² = **0.1792**, F-statistic = **15.80** (p = **5.59e-28**), Residual SE = **13.830** on **735** df, AIC = **6056.3**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.8311** | 4.7358 | ±9.4717 | **+12.634** | **1.38e-36** | *** |
| Education: graduate level (vs college) | -2.1713 | 1.1837 | ±2.3674 | -1.834 | 0.0666 | . |
| Education: high school or below (vs college) | +1.6717 | 1.5961 | ±3.1922 | +1.047 | 0.2949 |  |
| Site: UCSD (vs UAB) | +0.7875 | 1.3188 | ±2.6377 | +0.597 | 0.5504 |  |
| Site: UW (vs UAB) | +0.9281 | 1.2238 | ±2.4476 | +0.758 | 0.4482 |  |
| **Age (years)** | **-0.5431** | 0.0511 | ±0.1022 | **-10.626** | **2.26e-26** | *** |
| BMI (kg/m2) | -0.0216 | 0.0819 | ±0.1639 | -0.264 | 0.7917 |  |
| Hypertension | +0.0418 | 1.1623 | ±2.3247 | +0.036 | 0.9713 |  |
| High cholesterol | -0.0767 | 1.0672 | ±2.1343 | -0.072 | 0.9427 |  |
| **Kidney disease** | **-2.7609** | 1.3712 | ±2.7424 | **-2.013** | **0.0441** | * |
| **Circulatory disease** | **-3.8197** | 1.1151 | ±2.2301 | **-3.426** | **6.14e-04** | *** |
| Glucose SD, pooled (mg/dL) | +0.0197 | 0.0422 | ±0.0844 | +0.466 | 0.6409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **747**, R² = **0.1911**, Adj R² = **0.1790**, F-statistic = **15.79** (p = **5.99e-28**), Residual SE = **13.831** on **735** df, AIC = **6056.4**, BIC = **6111.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.9556** | 4.7575 | ±9.5149 | **+12.602** | **2.05e-36** | *** |
| Education: graduate level (vs college) | -2.1872 | 1.1818 | ±2.3636 | -1.851 | 0.0642 | . |
| Education: high school or below (vs college) | +1.6969 | 1.6021 | ±3.2041 | +1.059 | 0.2895 |  |
| Site: UCSD (vs UAB) | +0.7726 | 1.3197 | ±2.6394 | +0.585 | 0.5583 |  |
| Site: UW (vs UAB) | +0.9076 | 1.2244 | ±2.4488 | +0.741 | 0.4585 |  |
| **Age (years)** | **-0.5422** | 0.0511 | ±0.1022 | **-10.609** | **2.72e-26** | *** |
| BMI (kg/m2) | -0.0205 | 0.0820 | ±0.1641 | -0.250 | 0.8023 |  |
| Hypertension | +0.0446 | 1.1618 | ±2.3235 | +0.038 | 0.9694 |  |
| High cholesterol | -0.0881 | 1.0666 | ±2.1332 | -0.083 | 0.9342 |  |
| **Kidney disease** | **-2.7256** | 1.3706 | ±2.7412 | **-1.989** | **0.0467** | * |
| **Circulatory disease** | **-3.8142** | 1.1155 | ±2.2311 | **-3.419** | **6.28e-04** | *** |
| Avg. daily SD (mg/dL) | +0.0153 | 0.0470 | ±0.0940 | +0.326 | 0.7445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **747**, R² = **0.1910**, Adj R² = **0.1789**, F-statistic = **15.77** (p = **6.33e-28**), Residual SE = **13.832** on **735** df, AIC = **6056.5**, BIC = **6111.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4400** | 4.8953 | ±9.7907 | **+12.346** | **5.09e-35** | *** |
| Education: graduate level (vs college) | -2.2181 | 1.1744 | ±2.3488 | -1.889 | 0.0589 | . |
| Education: high school or below (vs college) | +1.7750 | 1.6103 | ±3.2206 | +1.102 | 0.2703 |  |
| Site: UCSD (vs UAB) | +0.7340 | 1.3235 | ±2.6470 | +0.555 | 0.5791 |  |
| Site: UW (vs UAB) | +0.8639 | 1.2322 | ±2.4643 | +0.701 | 0.4832 |  |
| **Age (years)** | **-0.5392** | 0.0507 | ±0.1013 | **-10.641** | **1.92e-26** | *** |
| BMI (kg/m2) | -0.0212 | 0.0820 | ±0.1640 | -0.258 | 0.7962 |  |
| Hypertension | +0.0466 | 1.1662 | ±2.3324 | +0.040 | 0.9681 |  |
| High cholesterol | -0.1128 | 1.0652 | ±2.1303 | -0.106 | 0.9157 |  |
| Kidney disease | -2.6186 | 1.3569 | ±2.7139 | -1.930 | 0.0536 | . |
| **Circulatory disease** | **-3.8083** | 1.1165 | ±2.2330 | **-3.411** | **6.47e-04** | *** |
| CV (%) | -0.0075 | 0.0846 | ±0.1692 | -0.089 | 0.9294 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **747**, R² = **0.1918**, Adj R² = **0.1797**, F-statistic = **15.86** (p = **4.41e-28**), Residual SE = **13.825** on **735** df, AIC = **6055.7**, BIC = **6111.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3744** | 5.3360 | ±10.6720 | **+11.689** | **1.44e-31** | *** |
| Education: graduate level (vs college) | -2.1707 | 1.1725 | ±2.3450 | -1.851 | 0.0641 | . |
| Education: high school or below (vs college) | +1.6269 | 1.6118 | ±3.2236 | +1.009 | 0.3128 |  |
| Site: UCSD (vs UAB) | +0.7997 | 1.3227 | ±2.6455 | +0.605 | 0.5455 |  |
| Site: UW (vs UAB) | +0.9774 | 1.2283 | ±2.4566 | +0.796 | 0.4262 |  |
| **Age (years)** | **-0.5466** | 0.0510 | ±0.1020 | **-10.718** | **8.42e-27** | *** |
| BMI (kg/m2) | -0.0198 | 0.0820 | ±0.1640 | -0.241 | 0.8092 |  |
| Hypertension | +0.0101 | 1.1663 | ±2.3326 | +0.009 | 0.9931 |  |
| High cholesterol | -0.0814 | 1.0662 | ±2.1323 | -0.076 | 0.9391 |  |
| **Kidney disease** | **-2.8175** | 1.3527 | ±2.7055 | **-2.083** | **0.0373** | * |
| **Circulatory disease** | **-3.8340** | 1.1155 | ±2.2309 | **-3.437** | **5.88e-04** | *** |
| Mean / SD ratio | -0.3458 | 0.3660 | ±0.7321 | -0.945 | 0.3448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **747**, R² = **0.1925**, Adj R² = **0.1804**, F-statistic = **15.93** (p = **3.29e-28**), Residual SE = **13.819** on **735** df, AIC = **6055.1**, BIC = **6110.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9467** | 5.2443 | ±10.4886 | **+12.003** | **3.43e-33** | *** |
| Education: graduate level (vs college) | -2.1523 | 1.1700 | ±2.3400 | -1.840 | 0.0658 | . |
| Education: high school or below (vs college) | +1.5963 | 1.6140 | ±3.2281 | +0.989 | 0.3227 |  |
| Site: UCSD (vs UAB) | +0.7817 | 1.3241 | ±2.6482 | +0.590 | 0.5549 |  |
| Site: UW (vs UAB) | +0.9891 | 1.2262 | ±2.4524 | +0.807 | 0.4199 |  |
| **Age (years)** | **-0.5495** | 0.0510 | ±0.1021 | **-10.765** | **5.02e-27** | *** |
| BMI (kg/m2) | -0.0161 | 0.0822 | ±0.1644 | -0.196 | 0.8446 |  |
| Hypertension | -0.0017 | 1.1645 | ±2.3290 | -0.001 | 0.9989 |  |
| High cholesterol | -0.0735 | 1.0660 | ±2.1321 | -0.069 | 0.9450 |  |
| **Kidney disease** | **-2.8401** | 1.3422 | ±2.6845 | **-2.116** | **0.0343** | * |
| **Circulatory disease** | **-3.8108** | 1.1150 | ±2.2301 | **-3.418** | **6.32e-04** | *** |
| Avg. daily mean/SD | -0.3879 | 0.2922 | ±0.5844 | -1.328 | 0.1843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **747**, R² = **0.1953**, Adj R² = **0.1833**, F-statistic = **16.22** (p = **9.65e-29**), Residual SE = **13.795** on **735** df, AIC = **6052.5**, BIC = **6107.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8458** | 5.0613 | ±10.1227 | **+11.034** | **2.62e-28** | *** |
| Education: graduate level (vs college) | -2.0485 | 1.1722 | ±2.3444 | -1.748 | 0.0805 | . |
| Education: high school or below (vs college) | +1.5481 | 1.5910 | ±3.1821 | +0.973 | 0.3305 |  |
| Site: UCSD (vs UAB) | +0.9200 | 1.3190 | ±2.6380 | +0.698 | 0.4855 |  |
| Site: UW (vs UAB) | +1.1633 | 1.2155 | ±2.4310 | +0.957 | 0.3386 |  |
| **Age (years)** | **-0.5412** | 0.0496 | ±0.0993 | **-10.906** | **1.08e-27** | *** |
| BMI (kg/m2) | -0.0237 | 0.0825 | ±0.1649 | -0.287 | 0.7742 |  |
| Hypertension | +0.0885 | 1.1565 | ±2.3130 | +0.077 | 0.9390 |  |
| High cholesterol | -0.0466 | 1.0665 | ±2.1329 | -0.044 | 0.9652 |  |
| **Kidney disease** | **-2.8982** | 1.3451 | ±2.6901 | **-2.155** | **0.0312** | * |
| **Circulatory disease** | **-3.8154** | 1.1151 | ±2.2302 | **-3.422** | **6.23e-04** | *** |
| MAG (mg/dL/h) | +0.1040 | 0.0597 | ±0.1194 | +1.742 | 0.0815 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **747**, R² = **0.1914**, Adj R² = **0.1793**, F-statistic = **15.82** (p = **5.29e-28**), Residual SE = **13.829** on **735** df, AIC = **6056.1**, BIC = **6111.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4135** | 4.8679 | ±9.7357 | **+12.205** | **2.91e-34** | *** |
| Education: graduate level (vs college) | -2.1652 | 1.1816 | ±2.3631 | -1.832 | 0.0669 | . |
| Education: high school or below (vs college) | +1.6494 | 1.6070 | ±3.2141 | +1.026 | 0.3047 |  |
| Site: UCSD (vs UAB) | +0.8046 | 1.3207 | ±2.6413 | +0.609 | 0.5424 |  |
| Site: UW (vs UAB) | +0.9333 | 1.2264 | ±2.4528 | +0.761 | 0.4467 |  |
| **Age (years)** | **-0.5436** | 0.0509 | ±0.1018 | **-10.678** | **1.29e-26** | *** |
| BMI (kg/m2) | -0.0194 | 0.0823 | ±0.1645 | -0.236 | 0.8133 |  |
| Hypertension | +0.0613 | 1.1575 | ±2.3151 | +0.053 | 0.9578 |  |
| High cholesterol | -0.0800 | 1.0668 | ±2.1336 | -0.075 | 0.9402 |  |
| **Kidney disease** | **-2.7905** | 1.3645 | ±2.7290 | **-2.045** | **0.0408** | * |
| **Circulatory disease** | **-3.8200** | 1.1149 | ±2.2297 | **-3.426** | **6.12e-04** | *** |
| Avg. daily range (mg/dL) | +0.0076 | 0.0133 | ±0.0266 | +0.571 | 0.5681 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **747**, R² = **0.1922**, Adj R² = **0.1801**, F-statistic = **15.89** (p = **3.81e-28**), Residual SE = **13.822** on **735** df, AIC = **6055.4**, BIC = **6110.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.7591** | 4.7040 | ±9.4081 | **+12.704** | **5.63e-37** | *** |
| Education: graduate level (vs college) | -2.1092 | 1.1880 | ±2.3759 | -1.775 | 0.0758 | . |
| Education: high school or below (vs college) | +1.6606 | 1.5902 | ±3.1804 | +1.044 | 0.2964 |  |
| Site: UCSD (vs UAB) | +0.7905 | 1.3197 | ±2.6394 | +0.599 | 0.5492 |  |
| Site: UW (vs UAB) | +0.9648 | 1.2248 | ±2.4497 | +0.788 | 0.4309 |  |
| **Age (years)** | **-0.5413** | 0.0499 | ±0.0997 | **-10.855** | **1.89e-27** | *** |
| BMI (kg/m2) | -0.0265 | 0.0820 | ±0.1639 | -0.323 | 0.7467 |  |
| Hypertension | +0.0053 | 1.1646 | ±2.3293 | +0.005 | 0.9964 |  |
| High cholesterol | -0.0570 | 1.0674 | ±2.1349 | -0.053 | 0.9574 |  |
| **Kidney disease** | **-2.7577** | 1.3500 | ±2.6999 | **-2.043** | **0.0411** | * |
| **Circulatory disease** | **-3.8851** | 1.1147 | ±2.2294 | **-3.485** | **4.92e-04** | *** |
| SD of daily means (mg/dL) | +0.0659 | 0.0715 | ±0.1431 | +0.921 | 0.3570 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **747**, R² = **0.1911**, Adj R² = **0.1790**, F-statistic = **15.78** (p = **6.10e-28**), Residual SE = **13.831** on **735** df, AIC = **6056.4**, BIC = **6111.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.8643** | 5.3978 | ±10.7955 | **+11.276** | **1.73e-29** | *** |
| Education: graduate level (vs college) | -2.1922 | 1.1829 | ±2.3657 | -1.853 | 0.0638 | . |
| Education: high school or below (vs college) | +1.7161 | 1.5929 | ±3.1859 | +1.077 | 0.2813 |  |
| Site: UCSD (vs UAB) | +0.7707 | 1.3186 | ±2.6371 | +0.584 | 0.5589 |  |
| Site: UW (vs UAB) | +0.8875 | 1.2268 | ±2.4535 | +0.723 | 0.4694 |  |
| **Age (years)** | **-0.5412** | 0.0507 | ±0.1014 | **-10.672** | **1.38e-26** | *** |
| BMI (kg/m2) | -0.0224 | 0.0819 | ±0.1637 | -0.274 | 0.7844 |  |
| Hypertension | +0.0542 | 1.1578 | ±2.3157 | +0.047 | 0.9627 |  |
| High cholesterol | -0.0876 | 1.0689 | ±2.1377 | -0.082 | 0.9347 |  |
| **Kidney disease** | **-2.6730** | 1.3477 | ±2.6954 | **-1.983** | **0.0473** | * |
| **Circulatory disease** | **-3.8198** | 1.1159 | ±2.2318 | **-3.423** | **6.19e-04** | *** |
| Time in range 70-180, pooled (%) | -0.0060 | 0.0229 | ±0.0459 | -0.260 | 0.7947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **747**, R² = **0.1911**, Adj R² = **0.1790**, F-statistic = **15.78** (p = **6.05e-28**), Residual SE = **13.831** on **735** df, AIC = **6056.4**, BIC = **6111.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.9216** | 5.4054 | ±10.8108 | **+11.271** | **1.83e-29** | *** |
| Education: graduate level (vs college) | -2.1912 | 1.1822 | ±2.3644 | -1.853 | 0.0638 | . |
| Education: high school or below (vs college) | +1.7098 | 1.5923 | ±3.1846 | +1.074 | 0.2829 |  |
| Site: UCSD (vs UAB) | +0.7750 | 1.3180 | ±2.6360 | +0.588 | 0.5565 |  |
| Site: UW (vs UAB) | +0.8885 | 1.2267 | ±2.4534 | +0.724 | 0.4689 |  |
| **Age (years)** | **-0.5414** | 0.0508 | ±0.1015 | **-10.664** | **1.50e-26** | *** |
| BMI (kg/m2) | -0.0226 | 0.0819 | ±0.1638 | -0.275 | 0.7830 |  |
| Hypertension | +0.0558 | 1.1577 | ±2.3154 | +0.048 | 0.9615 |  |
| High cholesterol | -0.0858 | 1.0690 | ±2.1380 | -0.080 | 0.9361 |  |
| **Kidney disease** | **-2.6780** | 1.3485 | ±2.6969 | **-1.986** | **0.0470** | * |
| **Circulatory disease** | **-3.8208** | 1.1161 | ±2.2321 | **-3.423** | **6.18e-04** | *** |
| Avg. daily time in range 70-180 (%) | -0.0065 | 0.0228 | ±0.0457 | -0.285 | 0.7755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **747**, R² = **0.1957**, Adj R² = **0.1836**, F-statistic = **16.25** (p = **8.38e-29**), Residual SE = **13.792** on **735** df, AIC = **6052.2**, BIC = **6107.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.3381** | 4.7050 | ±9.4100 | **+13.037** | **7.55e-39** | *** |
| Education: graduate level (vs college) | -2.1876 | 1.1620 | ±2.3240 | -1.883 | 0.0598 | . |
| Education: high school or below (vs college) | +1.6056 | 1.6071 | ±3.2142 | +0.999 | 0.3178 |  |
| Site: UCSD (vs UAB) | +0.4782 | 1.3275 | ±2.6550 | +0.360 | 0.7187 |  |
| Site: UW (vs UAB) | +0.6508 | 1.2391 | ±2.4781 | +0.525 | 0.5994 |  |
| **Age (years)** | **-0.5476** | 0.0496 | ±0.0993 | **-11.031** | **2.70e-28** | *** |
| BMI (kg/m2) | -0.0142 | 0.0821 | ±0.1642 | -0.173 | 0.8628 |  |
| Hypertension | +0.1530 | 1.1627 | ±2.3254 | +0.132 | 0.8953 |  |
| High cholesterol | -0.2219 | 1.0633 | ±2.1267 | -0.209 | 0.8347 |  |
| **Kidney disease** | **-2.7077** | 1.3280 | ±2.6559 | **-2.039** | **0.0414** | * |
| **Circulatory disease** | **-3.6549** | 1.1129 | ±2.2258 | **-3.284** | **0.0010** | ** |
| **Any reading < 54 during wear (0/1)** | **-2.4002** | 1.1555 | ±2.3109 | **-2.077** | **0.0378** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **747**, R² = **0.1943**, Adj R² = **0.1823**, F-statistic = **16.12** (p = **1.49e-28**), Residual SE = **13.803** on **735** df, AIC = **6053.4**, BIC = **6108.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5689** | 4.7048 | ±9.4095 | **+12.874** | **6.31e-38** | *** |
| Education: graduate level (vs college) | -2.2735 | 1.1620 | ±2.3239 | -1.957 | 0.0504 | . |
| Education: high school or below (vs college) | +1.6129 | 1.6035 | ±3.2069 | +1.006 | 0.3145 |  |
| Site: UCSD (vs UAB) | +0.5348 | 1.3308 | ±2.6615 | +0.402 | 0.6878 |  |
| Site: UW (vs UAB) | +0.6374 | 1.2423 | ±2.4847 | +0.513 | 0.6079 |  |
| **Age (years)** | **-0.5408** | 0.0495 | ±0.0990 | **-10.929** | **8.35e-28** | *** |
| BMI (kg/m2) | -0.0164 | 0.0823 | ±0.1645 | -0.200 | 0.8416 |  |
| Hypertension | +0.1227 | 1.1575 | ±2.3150 | +0.106 | 0.9156 |  |
| High cholesterol | -0.1474 | 1.0666 | ±2.1331 | -0.138 | 0.8901 |  |
| **Kidney disease** | **-2.7008** | 1.3285 | ±2.6571 | **-2.033** | **0.0421** | * |
| **Circulatory disease** | **-3.6606** | 1.1171 | ±2.2342 | **-3.277** | **0.0010** | ** |
| Time < 54 (%) | -2.0088 | 1.7135 | ±3.4271 | -1.172 | 0.2411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **747**, R² = **0.1944**, Adj R² = **0.1823**, F-statistic = **16.12** (p = **1.47e-28**), Residual SE = **13.803** on **735** df, AIC = **6053.4**, BIC = **6108.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4155** | 4.6972 | ±9.3945 | **+12.862** | **7.37e-38** | *** |
| **Education: graduate level (vs college)** | **-2.2963** | 1.1658 | ±2.3317 | **-1.970** | **0.0489** | * |
| Education: high school or below (vs college) | +1.6391 | 1.6022 | ±3.2043 | +1.023 | 0.3063 |  |
| Site: UCSD (vs UAB) | +0.5768 | 1.3285 | ±2.6570 | +0.434 | 0.6642 |  |
| Site: UW (vs UAB) | +0.6862 | 1.2362 | ±2.4723 | +0.555 | 0.5788 |  |
| **Age (years)** | **-0.5381** | 0.0496 | ±0.0991 | **-10.860** | **1.79e-27** | *** |
| BMI (kg/m2) | -0.0188 | 0.0817 | ±0.1635 | -0.230 | 0.8178 |  |
| Hypertension | +0.1036 | 1.1585 | ±2.3169 | +0.089 | 0.9288 |  |
| High cholesterol | -0.1743 | 1.0664 | ±2.1327 | -0.163 | 0.8702 |  |
| **Kidney disease** | **-2.6788** | 1.3297 | ±2.6594 | **-2.015** | **0.0439** | * |
| **Circulatory disease** | **-3.6754** | 1.1156 | ±2.2312 | **-3.295** | **9.86e-04** | *** |
| Avg. daily time < 54 (%) | -1.9175 | 1.2763 | ±2.5526 | -1.502 | 0.1330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **747**, R² = **0.1933**, Adj R² = **0.1812**, F-statistic = **16.01** (p = **2.37e-28**), Residual SE = **13.813** on **735** df, AIC = **6054.4**, BIC = **6109.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4331** | 4.7070 | ±9.4139 | **+12.839** | **9.91e-38** | *** |
| **Education: graduate level (vs college)** | **-2.2939** | 1.1623 | ±2.3246 | **-1.974** | **0.0484** | * |
| Education: high school or below (vs college) | +1.7619 | 1.6072 | ±3.2144 | +1.096 | 0.2730 |  |
| Site: UCSD (vs UAB) | +0.5856 | 1.3221 | ±2.6443 | +0.443 | 0.6578 |  |
| Site: UW (vs UAB) | +0.7378 | 1.2338 | ±2.4677 | +0.598 | 0.5498 |  |
| **Age (years)** | **-0.5371** | 0.0497 | ±0.0993 | **-10.816** | **2.90e-27** | *** |
| BMI (kg/m2) | -0.0194 | 0.0822 | ±0.1645 | -0.236 | 0.8135 |  |
| Hypertension | +0.0792 | 1.1575 | ±2.3149 | +0.068 | 0.9454 |  |
| High cholesterol | -0.1397 | 1.0656 | ±2.1311 | -0.131 | 0.8957 |  |
| **Kidney disease** | **-2.6662** | 1.3272 | ±2.6544 | **-2.009** | **0.0445** | * |
| **Circulatory disease** | **-3.7481** | 1.1179 | ±2.2357 | **-3.353** | **8.00e-04** | *** |
| Time 54-69, pooled (%) | -0.4851 | 0.2593 | ±0.5185 | -1.871 | 0.0614 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **747**, R² = **0.1937**, Adj R² = **0.1816**, F-statistic = **16.05** (p = **1.95e-28**), Residual SE = **13.809** on **735** df, AIC = **6054.0**, BIC = **6109.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3437** | 4.7087 | ±9.4174 | **+12.815** | **1.35e-37** | *** |
| **Education: graduate level (vs college)** | **-2.2990** | 1.1628 | ±2.3257 | **-1.977** | **0.0480** | * |
| Education: high school or below (vs college) | +1.7766 | 1.6063 | ±3.2125 | +1.106 | 0.2687 |  |
| Site: UCSD (vs UAB) | +0.5895 | 1.3228 | ±2.6456 | +0.446 | 0.6559 |  |
| Site: UW (vs UAB) | +0.7360 | 1.2355 | ±2.4711 | +0.596 | 0.5514 |  |
| **Age (years)** | **-0.5355** | 0.0497 | ±0.0995 | **-10.768** | **4.88e-27** | *** |
| BMI (kg/m2) | -0.0195 | 0.0821 | ±0.1643 | -0.237 | 0.8125 |  |
| Hypertension | +0.0829 | 1.1574 | ±2.3148 | +0.072 | 0.9429 |  |
| High cholesterol | -0.1450 | 1.0649 | ±2.1299 | -0.136 | 0.8917 |  |
| **Kidney disease** | **-2.6726** | 1.3273 | ±2.6545 | **-2.014** | **0.0440** | * |
| **Circulatory disease** | **-3.7477** | 1.1180 | ±2.2360 | **-3.352** | **8.02e-04** | *** |
| **Avg. daily time 54-69 (%)** | **-0.5097** | 0.2561 | ±0.5122 | **-1.990** | **0.0465** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **747**, R² = **0.1938**, Adj R² = **0.1817**, F-statistic = **16.06** (p = **1.88e-28**), Residual SE = **13.808** on **735** df, AIC = **6053.9**, BIC = **6109.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4793** | 4.7051 | ±9.4103 | **+12.854** | **8.18e-38** | *** |
| **Education: graduate level (vs college)** | **-2.2999** | 1.1617 | ±2.3234 | **-1.980** | **0.0477** | * |
| Education: high school or below (vs college) | +1.7290 | 1.6065 | ±3.2129 | +1.076 | 0.2818 |  |
| Site: UCSD (vs UAB) | +0.5542 | 1.3232 | ±2.6465 | +0.419 | 0.6754 |  |
| Site: UW (vs UAB) | +0.6980 | 1.2348 | ±2.4695 | +0.565 | 0.5719 |  |
| **Age (years)** | **-0.5375** | 0.0496 | ±0.0992 | **-10.841** | **2.21e-27** | *** |
| BMI (kg/m2) | -0.0185 | 0.0823 | ±0.1645 | -0.225 | 0.8217 |  |
| Hypertension | +0.0934 | 1.1567 | ±2.3134 | +0.081 | 0.9356 |  |
| High cholesterol | -0.1454 | 1.0652 | ±2.1304 | -0.136 | 0.8914 |  |
| **Kidney disease** | **-2.6774** | 1.3267 | ±2.6535 | **-2.018** | **0.0436** | * |
| **Circulatory disease** | **-3.7209** | 1.1182 | ±2.2363 | **-3.328** | **8.76e-04** | *** |
| Time < 70 (%) | -0.4415 | 0.2269 | ±0.4538 | -1.946 | 0.0517 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **747**, R² = **0.1942**, Adj R² = **0.1822**, F-statistic = **16.11** (p = **1.55e-28**), Residual SE = **13.804** on **735** df, AIC = **6053.5**, BIC = **6108.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3657** | 4.7051 | ±9.4103 | **+12.830** | **1.12e-37** | *** |
| **Education: graduate level (vs college)** | **-2.3099** | 1.1631 | ±2.3262 | **-1.986** | **0.0470** | * |
| Education: high school or below (vs college) | +1.7457 | 1.6048 | ±3.2095 | +1.088 | 0.2767 |  |
| Site: UCSD (vs UAB) | +0.5659 | 1.3239 | ±2.6478 | +0.427 | 0.6690 |  |
| Site: UW (vs UAB) | +0.7054 | 1.2359 | ±2.4718 | +0.571 | 0.5682 |  |
| **Age (years)** | **-0.5356** | 0.0497 | ±0.0994 | **-10.779** | **4.34e-27** | *** |
| BMI (kg/m2) | -0.0191 | 0.0821 | ±0.1641 | -0.233 | 0.8158 |  |
| Hypertension | +0.0931 | 1.1570 | ±2.3141 | +0.080 | 0.9359 |  |
| High cholesterol | -0.1568 | 1.0644 | ±2.1288 | -0.147 | 0.8829 |  |
| **Kidney disease** | **-2.6786** | 1.3271 | ±2.6542 | **-2.018** | **0.0435** | * |
| **Circulatory disease** | **-3.7222** | 1.1179 | ±2.2358 | **-3.330** | **8.70e-04** | *** |
| **Avg. daily time < 70 (%)** | **-0.4571** | 0.2149 | ±0.4297 | **-2.127** | **0.0334** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **747**, R² = **0.1914**, Adj R² = **0.1793**, F-statistic = **15.81** (p = **5.38e-28**), Residual SE = **13.829** on **735** df, AIC = **6056.2**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4852** | 6.2179 | ±12.4358 | **+9.406** | **5.16e-21** | *** |
| Education: graduate level (vs college) | -2.2727 | 1.1902 | ±2.3804 | -1.910 | 0.0562 | . |
| Education: high school or below (vs college) | +1.8379 | 1.5844 | ±3.1688 | +1.160 | 0.2460 |  |
| Site: UCSD (vs UAB) | +0.7038 | 1.3186 | ±2.6372 | +0.534 | 0.5935 |  |
| Site: UW (vs UAB) | +0.8209 | 1.2201 | ±2.4402 | +0.673 | 0.5011 |  |
| **Age (years)** | **-0.5404** | 0.0495 | ±0.0991 | **-10.911** | **1.02e-27** | *** |
| BMI (kg/m2) | -0.0189 | 0.0819 | ±0.1638 | -0.231 | 0.8175 |  |
| Hypertension | +0.0532 | 1.1627 | ±2.3253 | +0.046 | 0.9635 |  |
| High cholesterol | -0.1384 | 1.0702 | ±2.1404 | -0.129 | 0.8971 |  |
| Kidney disease | -2.5888 | 1.3427 | ±2.6854 | -1.928 | 0.0538 | . |
| **Circulatory disease** | **-3.7968** | 1.1197 | ±2.2394 | **-3.391** | **6.97e-04** | *** |
| Time 54-250, pooled (%) | +0.0196 | 0.0376 | ±0.0752 | +0.520 | 0.6028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **747**, R² = **0.1913**, Adj R² = **0.1792**, F-statistic = **15.80** (p = **5.56e-28**), Residual SE = **13.830** on **735** df, AIC = **6056.2**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6323** | 6.1710 | ±12.3420 | **+9.501** | **2.07e-21** | *** |
| Education: graduate level (vs college) | -2.2658 | 1.1903 | ±2.3806 | -1.904 | 0.0570 | . |
| Education: high school or below (vs college) | +1.8297 | 1.5855 | ±3.1710 | +1.154 | 0.2485 |  |
| Site: UCSD (vs UAB) | +0.7069 | 1.3188 | ±2.6376 | +0.536 | 0.5919 |  |
| Site: UW (vs UAB) | +0.8282 | 1.2207 | ±2.4415 | +0.678 | 0.4975 |  |
| **Age (years)** | **-0.5401** | 0.0496 | ±0.0992 | **-10.889** | **1.30e-27** | *** |
| BMI (kg/m2) | -0.0191 | 0.0818 | ±0.1637 | -0.233 | 0.8158 |  |
| Hypertension | +0.0507 | 1.1627 | ±2.3254 | +0.044 | 0.9652 |  |
| High cholesterol | -0.1357 | 1.0701 | ±2.1402 | -0.127 | 0.8991 |  |
| Kidney disease | -2.5898 | 1.3435 | ±2.6870 | -1.928 | 0.0539 | . |
| **Circulatory disease** | **-3.7955** | 1.1194 | ±2.2388 | **-3.391** | **6.97e-04** | *** |
| Avg. daily time 54-250 (%) | +0.0178 | 0.0367 | ±0.0734 | +0.484 | 0.6285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **747**, R² = **0.1926**, Adj R² = **0.1805**, F-statistic = **15.94** (p = **3.14e-28**), Residual SE = **13.818** on **735** df, AIC = **6055.0**, BIC = **6110.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3243** | 4.7265 | ±9.4530 | **+12.763** | **2.64e-37** | *** |
| Education: graduate level (vs college) | -2.1971 | 1.1668 | ±2.3336 | -1.883 | 0.0597 | . |
| Education: high school or below (vs college) | +1.6025 | 1.6075 | ±3.2151 | +0.997 | 0.3188 |  |
| Site: UCSD (vs UAB) | +0.8479 | 1.3224 | ±2.6448 | +0.641 | 0.5214 |  |
| Site: UW (vs UAB) | +0.8392 | 1.2352 | ±2.4704 | +0.679 | 0.4969 |  |
| **Age (years)** | **-0.5497** | 0.0512 | ±0.1024 | **-10.741** | **6.50e-27** | *** |
| BMI (kg/m2) | -0.0259 | 0.0819 | ±0.1638 | -0.316 | 0.7517 |  |
| Hypertension | +0.1358 | 1.1481 | ±2.2961 | +0.118 | 0.9058 |  |
| High cholesterol | -0.0266 | 1.0649 | ±2.1298 | -0.025 | 0.9801 |  |
| **Kidney disease** | **-2.7654** | 1.3413 | ±2.6826 | **-2.062** | **0.0392** | * |
| **Circulatory disease** | **-3.8504** | 1.1143 | ±2.2287 | **-3.455** | **5.50e-04** | *** |
| Time 181-250, pooled (%) | +0.0403 | 0.0347 | ±0.0693 | +1.162 | 0.2454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **747**, R² = **0.1925**, Adj R² = **0.1805**, F-statistic = **15.93** (p = **3.22e-28**), Residual SE = **13.819** on **735** df, AIC = **6055.1**, BIC = **6110.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3119** | 4.7270 | ±9.4540 | **+12.759** | **2.78e-37** | *** |
| Education: graduate level (vs college) | -2.2001 | 1.1668 | ±2.3336 | -1.886 | 0.0594 | . |
| Education: high school or below (vs college) | +1.5941 | 1.6041 | ±3.2081 | +0.994 | 0.3203 |  |
| Site: UCSD (vs UAB) | +0.8543 | 1.3215 | ±2.6431 | +0.646 | 0.5180 |  |
| Site: UW (vs UAB) | +0.8452 | 1.2352 | ±2.4705 | +0.684 | 0.4938 |  |
| **Age (years)** | **-0.5492** | 0.0512 | ±0.1023 | **-10.733** | **7.12e-27** | *** |
| BMI (kg/m2) | -0.0258 | 0.0820 | ±0.1640 | -0.315 | 0.7527 |  |
| Hypertension | +0.1334 | 1.1497 | ±2.2993 | +0.116 | 0.9077 |  |
| High cholesterol | -0.0302 | 1.0657 | ±2.1314 | -0.028 | 0.9774 |  |
| **Kidney disease** | **-2.7651** | 1.3416 | ±2.6833 | **-2.061** | **0.0393** | * |
| **Circulatory disease** | **-3.8436** | 1.1155 | ±2.2310 | **-3.446** | **5.70e-04** | *** |
| Avg. daily time 181-250 (%) | +0.0389 | 0.0343 | ±0.0686 | +1.135 | 0.2565 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **747**, R² = **0.1912**, Adj R² = **0.1791**, F-statistic = **15.79** (p = **5.87e-28**), Residual SE = **13.831** on **735** df, AIC = **6056.4**, BIC = **6111.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2562** | 4.7068 | ±9.4137 | **+12.802** | **1.60e-37** | *** |
| Education: graduate level (vs college) | -2.1859 | 1.1813 | ±2.3626 | -1.850 | 0.0643 | . |
| Education: high school or below (vs college) | +1.6984 | 1.5929 | ±3.1858 | +1.066 | 0.2863 |  |
| Site: UCSD (vs UAB) | +0.7779 | 1.3186 | ±2.6372 | +0.590 | 0.5552 |  |
| Site: UW (vs UAB) | +0.8890 | 1.2279 | ±2.4557 | +0.724 | 0.4691 |  |
| **Age (years)** | **-0.5416** | 0.0506 | ±0.1013 | **-10.695** | **1.07e-26** | *** |
| BMI (kg/m2) | -0.0229 | 0.0819 | ±0.1638 | -0.279 | 0.7801 |  |
| Hypertension | +0.0589 | 1.1574 | ±2.3149 | +0.051 | 0.9594 |  |
| High cholesterol | -0.0804 | 1.0690 | ±2.1380 | -0.075 | 0.9400 |  |
| **Kidney disease** | **-2.6860** | 1.3476 | ±2.6952 | **-1.993** | **0.0462** | * |
| **Circulatory disease** | **-3.8221** | 1.1157 | ±2.2315 | **-3.426** | **6.13e-04** | *** |
| Time > 180 (%) | +0.0081 | 0.0226 | ±0.0452 | +0.361 | 0.7184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **747**, R² = **0.1912**, Adj R² = **0.1791**, F-statistic = **15.80** (p = **5.77e-28**), Residual SE = **13.830** on **735** df, AIC = **6056.3**, BIC = **6111.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2581** | 4.7091 | ±9.4183 | **+12.796** | **1.73e-37** | *** |
| Education: graduate level (vs college) | -2.1846 | 1.1806 | ±2.3613 | -1.850 | 0.0643 | . |
| Education: high school or below (vs college) | +1.6896 | 1.5920 | ±3.1840 | +1.061 | 0.2886 |  |
| Site: UCSD (vs UAB) | +0.7841 | 1.3179 | ±2.6359 | +0.595 | 0.5519 |  |
| Site: UW (vs UAB) | +0.8904 | 1.2278 | ±2.4556 | +0.725 | 0.4683 |  |
| **Age (years)** | **-0.5419** | 0.0507 | ±0.1013 | **-10.694** | **1.09e-26** | *** |
| BMI (kg/m2) | -0.0231 | 0.0819 | ±0.1639 | -0.282 | 0.7780 |  |
| Hypertension | +0.0613 | 1.1573 | ±2.3146 | +0.053 | 0.9578 |  |
| High cholesterol | -0.0779 | 1.0693 | ±2.1385 | -0.073 | 0.9419 |  |
| **Kidney disease** | **-2.6933** | 1.3484 | ±2.6968 | **-1.997** | **0.0458** | * |
| **Circulatory disease** | **-3.8234** | 1.1159 | ±2.2317 | **-3.426** | **6.12e-04** | *** |
| Avg. daily time > 180 (%) | +0.0090 | 0.0225 | ±0.0451 | +0.397 | 0.6911 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **747**, R² = **0.1913**, Adj R² = **0.1792**, F-statistic = **15.81** (p = **5.47e-28**), Residual SE = **13.829** on **735** df, AIC = **6056.2**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2557** | 4.7161 | ±9.4322 | **+12.777** | **2.22e-37** | *** |
| Education: graduate level (vs college) | -2.1658 | 1.1867 | ±2.3735 | -1.825 | 0.0680 | . |
| Education: high school or below (vs college) | +1.6767 | 1.5932 | ±3.1865 | +1.052 | 0.2926 |  |
| Site: UCSD (vs UAB) | +0.7959 | 1.3153 | ±2.6306 | +0.605 | 0.5451 |  |
| Site: UW (vs UAB) | +0.8900 | 1.2286 | ±2.4573 | +0.724 | 0.4688 |  |
| **Age (years)** | **-0.5408** | 0.0500 | ±0.1000 | **-10.812** | **3.04e-27** | *** |
| BMI (kg/m2) | -0.0255 | 0.0820 | ±0.1639 | -0.311 | 0.7561 |  |
| Hypertension | +0.0620 | 1.1584 | ±2.3168 | +0.053 | 0.9573 |  |
| High cholesterol | -0.0598 | 1.0718 | ±2.1436 | -0.056 | 0.9555 |  |
| **Kidney disease** | **-2.6896** | 1.3457 | ±2.6913 | **-1.999** | **0.0456** | * |
| **Circulatory disease** | **-3.8315** | 1.1156 | ±2.2312 | **-3.434** | **5.94e-04** | *** |
| Nocturnal time > 180 (%) | +0.0108 | 0.0222 | ±0.0444 | +0.485 | 0.6273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **747**, R² = **0.1916**, Adj R² = **0.1795**, F-statistic = **15.84** (p = **4.82e-28**), Residual SE = **13.827** on **735** df, AIC = **6055.9**, BIC = **6111.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1123** | 4.7068 | ±9.4136 | **+12.771** | **2.37e-37** | *** |
| Education: graduate level (vs college) | -2.1525 | 1.1775 | ±2.3550 | -1.828 | 0.0675 | . |
| Education: high school or below (vs college) | +1.7021 | 1.6108 | ±3.2217 | +1.057 | 0.2907 |  |
| Site: UCSD (vs UAB) | +0.7859 | 1.3243 | ±2.6486 | +0.593 | 0.5529 |  |
| Site: UW (vs UAB) | +0.8494 | 1.2327 | ±2.4654 | +0.689 | 0.4908 |  |
| **Age (years)** | **-0.5468** | 0.0515 | ±0.1031 | **-10.612** | **2.61e-26** | *** |
| BMI (kg/m2) | -0.0189 | 0.0823 | ±0.1645 | -0.230 | 0.8178 |  |
| Hypertension | +0.0738 | 1.1562 | ±2.3123 | +0.064 | 0.9491 |  |
| High cholesterol | -0.0872 | 1.0658 | ±2.1316 | -0.082 | 0.9348 |  |
| **Kidney disease** | **-2.7430** | 1.3485 | ±2.6970 | **-2.034** | **0.0419** | * |
| **Circulatory disease** | **-3.7841** | 1.1207 | ±2.2415 | **-3.376** | **7.34e-04** | *** |
| Any reading > 250 during wear (0/1) | +0.8271 | 1.1273 | ±2.2545 | +0.734 | 0.4631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **747**, R² = **0.1913**, Adj R² = **0.1792**, F-statistic = **15.81** (p = **5.52e-28**), Residual SE = **13.829** on **735** df, AIC = **6056.2**, BIC = **6111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4271** | 4.6878 | ±9.3757 | **+12.890** | **5.11e-38** | *** |
| Education: graduate level (vs college) | -2.2671 | 1.1898 | ±2.3796 | -1.905 | 0.0567 | . |
| Education: high school or below (vs college) | +1.8327 | 1.5842 | ±3.1683 | +1.157 | 0.2473 |  |
| Site: UCSD (vs UAB) | +0.7089 | 1.3188 | ±2.6377 | +0.538 | 0.5909 |  |
| Site: UW (vs UAB) | +0.8277 | 1.2205 | ±2.4409 | +0.678 | 0.4977 |  |
| **Age (years)** | **-0.5403** | 0.0495 | ±0.0991 | **-10.909** | **1.05e-27** | *** |
| BMI (kg/m2) | -0.0191 | 0.0819 | ±0.1638 | -0.234 | 0.8153 |  |
| Hypertension | +0.0517 | 1.1626 | ±2.3253 | +0.044 | 0.9645 |  |
| High cholesterol | -0.1355 | 1.0702 | ±2.1405 | -0.127 | 0.8992 |  |
| Kidney disease | -2.5926 | 1.3430 | ±2.6859 | -1.931 | 0.0535 | . |
| **Circulatory disease** | **-3.7992** | 1.1195 | ±2.2390 | **-3.394** | **6.90e-04** | *** |
| Time > 250 (%) | -0.0179 | 0.0376 | ±0.0751 | -0.475 | 0.6346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 747)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **747**, R² = **0.1912**, Adj R² = **0.1791**, F-statistic = **15.80** (p = **5.70e-28**), Residual SE = **13.830** on **735** df, AIC = **6056.3**, BIC = **6111.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3970** | 4.6925 | ±9.3851 | **+12.871** | **6.57e-38** | *** |
| Education: graduate level (vs college) | -2.2598 | 1.1898 | ±2.3796 | -1.899 | 0.0575 | . |
| Education: high school or below (vs college) | +1.8239 | 1.5854 | ±3.1708 | +1.150 | 0.2500 |  |
| Site: UCSD (vs UAB) | +0.7118 | 1.3189 | ±2.6379 | +0.540 | 0.5894 |  |
| Site: UW (vs UAB) | +0.8345 | 1.2211 | ±2.4422 | +0.683 | 0.4943 |  |
| **Age (years)** | **-0.5401** | 0.0496 | ±0.0992 | **-10.890** | **1.29e-27** | *** |
| BMI (kg/m2) | -0.0193 | 0.0819 | ±0.1637 | -0.236 | 0.8138 |  |
| Hypertension | +0.0495 | 1.1627 | ±2.3253 | +0.043 | 0.9661 |  |
| High cholesterol | -0.1324 | 1.0701 | ±2.1403 | -0.124 | 0.9015 |  |
| Kidney disease | -2.5945 | 1.3437 | ±2.6874 | -1.931 | 0.0535 | . |
| **Circulatory disease** | **-3.7980** | 1.1192 | ±2.2384 | **-3.393** | **6.90e-04** | *** |
| Avg. daily time > 250 (%) | -0.0159 | 0.0367 | ±0.0735 | -0.434 | 0.6641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 749; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **749**, R² = **0.1647**, Adj R² = **0.1534**, F-statistic = **14.55** (p = **8.82e-24**), Residual SE = **8.360** on **738** df, AIC = **5317.5**, BIC = **5368.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8305** | 2.7974 | ±5.5949 | **+27.822** | **2.35e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9337** | 0.7147 | ±1.4294 | **-2.706** | **0.0068** | ** |
| Education: high school or below (vs college) | -0.0200 | 0.8568 | ±1.7136 | -0.023 | 0.9814 |  |
| **Site: UCSD (vs UAB)** | **-1.8424** | 0.8089 | ±1.6178 | **-2.278** | **0.0227** | * |
| Site: UW (vs UAB) | -0.4645 | 0.7700 | ±1.5401 | -0.603 | 0.5464 |  |
| **Age (years)** | **-0.2429** | 0.0310 | ±0.0621 | **-7.825** | **5.06e-15** | *** |
| **BMI (kg/m2)** | **+0.1409** | 0.0450 | ±0.0900 | **+3.131** | **0.0017** | ** |
| Hypertension | +0.5730 | 0.7022 | ±1.4044 | +0.816 | 0.4145 |  |
| High cholesterol | -0.4368 | 0.6653 | ±1.3305 | -0.657 | 0.5115 |  |
| Kidney disease | +0.5891 | 0.8446 | ±1.6892 | +0.698 | 0.4855 |  |
| Circulatory disease | -1.2623 | 0.7802 | ±1.5605 | -1.618 | 0.1057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **749**, R² = **0.1737**, Adj R² = **0.1614**, F-statistic = **14.08** (p = **8.26e-25**), Residual SE = **8.321** on **737** df, AIC = **5311.4**, BIC = **5366.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.9426** | 3.1790 | ±6.3579 | **+23.260** | **1.13e-119** | *** |
| **Education: graduate level (vs college)** | **-1.7726** | 0.7180 | ±1.4360 | **-2.469** | **0.0136** | * |
| Education: high school or below (vs college) | -0.2961 | 0.8406 | ±1.6812 | -0.352 | 0.7246 |  |
| **Site: UCSD (vs UAB)** | **-1.7654** | 0.8031 | ±1.6062 | **-2.198** | **0.0279** | * |
| Site: UW (vs UAB) | -0.3826 | 0.7714 | ±1.5428 | -0.496 | 0.6199 |  |
| **Age (years)** | **-0.2475** | 0.0308 | ±0.0616 | **-8.032** | **9.55e-16** | *** |
| **BMI (kg/m2)** | **+0.1278** | 0.0452 | ±0.0905 | **+2.826** | **0.0047** | ** |
| Hypertension | +0.5309 | 0.7006 | ±1.4012 | +0.758 | 0.4486 |  |
| High cholesterol | -0.3949 | 0.6632 | ±1.3264 | -0.595 | 0.5515 |  |
| Kidney disease | +0.6079 | 0.8504 | ±1.7009 | +0.715 | 0.4747 |  |
| Circulatory disease | -1.2245 | 0.7819 | ±1.5638 | -1.566 | 0.1173 |  |
| **HbA1c (%)** | **+0.6741** | 0.2294 | ±0.4588 | **+2.939** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **749**, R² = **0.1773**, Adj R² = **0.1650**, F-statistic = **14.44** (p = **1.80e-25**), Residual SE = **8.303** on **737** df, AIC = **5308.1**, BIC = **5363.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.4790** | 3.0655 | ±6.1310 | **+24.296** | **2.17e-130** | *** |
| **Education: graduate level (vs college)** | **-1.7798** | 0.7138 | ±1.4276 | **-2.493** | **0.0127** | * |
| Education: high school or below (vs college) | -0.3197 | 0.8355 | ±1.6711 | -0.383 | 0.7020 |  |
| **Site: UCSD (vs UAB)** | **-1.7305** | 0.8040 | ±1.6080 | **-2.152** | **0.0314** | * |
| Site: UW (vs UAB) | -0.4035 | 0.7664 | ±1.5327 | -0.527 | 0.5985 |  |
| **Age (years)** | **-0.2486** | 0.0308 | ±0.0617 | **-8.060** | **7.63e-16** | *** |
| **BMI (kg/m2)** | **+0.1334** | 0.0453 | ±0.0906 | **+2.945** | **0.0032** | ** |
| Hypertension | +0.6048 | 0.6996 | ±1.3993 | +0.864 | 0.3874 |  |
| High cholesterol | -0.3258 | 0.6620 | ±1.3239 | -0.492 | 0.6226 |  |
| Kidney disease | +0.3873 | 0.8513 | ±1.7026 | +0.455 | 0.6491 |  |
| Circulatory disease | -1.3014 | 0.7811 | ±1.5622 | -1.666 | 0.0957 | . |
| **Mean glucose (mg/dL)** | **+0.0250** | 0.0078 | ±0.0155 | **+3.219** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **749**, R² = **0.1773**, Adj R² = **0.1650**, F-statistic = **14.44** (p = **1.80e-25**), Residual SE = **8.303** on **737** df, AIC = **5308.1**, BIC = **5363.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.0170** | 3.6464 | ±7.2928 | **+19.476** | **1.75e-84** | *** |
| **Education: graduate level (vs college)** | **-1.7798** | 0.7138 | ±1.4276 | **-2.493** | **0.0127** | * |
| Education: high school or below (vs college) | -0.3197 | 0.8355 | ±1.6711 | -0.383 | 0.7020 |  |
| **Site: UCSD (vs UAB)** | **-1.7305** | 0.8040 | ±1.6080 | **-2.152** | **0.0314** | * |
| Site: UW (vs UAB) | -0.4035 | 0.7664 | ±1.5327 | -0.527 | 0.5985 |  |
| **Age (years)** | **-0.2486** | 0.0308 | ±0.0617 | **-8.060** | **7.63e-16** | *** |
| **BMI (kg/m2)** | **+0.1334** | 0.0453 | ±0.0906 | **+2.945** | **0.0032** | ** |
| Hypertension | +0.6048 | 0.6996 | ±1.3993 | +0.864 | 0.3874 |  |
| High cholesterol | -0.3258 | 0.6620 | ±1.3239 | -0.492 | 0.6226 |  |
| Kidney disease | +0.3873 | 0.8513 | ±1.7026 | +0.455 | 0.6491 |  |
| Circulatory disease | -1.3014 | 0.7811 | ±1.5622 | -1.666 | 0.0957 | . |
| **GMI (%)** | **+1.0459** | 0.3250 | ±0.6499 | **+3.219** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **749**, R² = **0.1760**, Adj R² = **0.1637**, F-statistic = **14.31** (p = **3.11e-25**), Residual SE = **8.309** on **737** df, AIC = **5309.3**, BIC = **5364.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.6928** | 3.0521 | ±6.1043 | **+24.472** | **2.92e-132** | *** |
| **Education: graduate level (vs college)** | **-1.7927** | 0.7156 | ±1.4312 | **-2.505** | **0.0122** | * |
| Education: high school or below (vs college) | -0.3068 | 0.8350 | ±1.6701 | -0.367 | 0.7133 |  |
| **Site: UCSD (vs UAB)** | **-1.7403** | 0.8052 | ±1.6104 | **-2.161** | **0.0307** | * |
| Site: UW (vs UAB) | -0.4580 | 0.7663 | ±1.5325 | -0.598 | 0.5500 |  |
| **Age (years)** | **-0.2437** | 0.0309 | ±0.0618 | **-7.883** | **3.20e-15** | *** |
| **BMI (kg/m2)** | **+0.1286** | 0.0452 | ±0.0904 | **+2.845** | **0.0044** | ** |
| Hypertension | +0.6138 | 0.6999 | ±1.3998 | +0.877 | 0.3805 |  |
| High cholesterol | -0.3267 | 0.6635 | ±1.3270 | -0.492 | 0.6224 |  |
| Kidney disease | +0.4887 | 0.8483 | ±1.6966 | +0.576 | 0.5646 |  |
| Circulatory disease | -1.3056 | 0.7813 | ±1.5626 | -1.671 | 0.0947 | . |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0234** | 0.0077 | ±0.0154 | **+3.032** | **0.0024** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **749**, R² = **0.1688**, Adj R² = **0.1564**, F-statistic = **13.61** (p = **6.39e-24**), Residual SE = **8.345** on **737** df, AIC = **5315.8**, BIC = **5371.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.7704** | 2.8484 | ±5.6968 | **+26.952** | **5.42e-160** | *** |
| **Education: graduate level (vs college)** | **-1.8404** | 0.7187 | ±1.4373 | **-2.561** | **0.0104** | * |
| Education: high school or below (vs college) | -0.2336 | 0.8551 | ±1.7102 | -0.273 | 0.7847 |  |
| **Site: UCSD (vs UAB)** | **-1.7471** | 0.8101 | ±1.6202 | **-2.157** | **0.0310** | * |
| Site: UW (vs UAB) | -0.3468 | 0.7716 | ±1.5433 | -0.449 | 0.6531 |  |
| **Age (years)** | **-0.2498** | 0.0314 | ±0.0627 | **-7.965** | **1.65e-15** | *** |
| **BMI (kg/m2)** | **+0.1396** | 0.0452 | ±0.0903 | **+3.090** | **0.0020** | ** |
| Hypertension | +0.5638 | 0.7022 | ±1.4044 | +0.803 | 0.4220 |  |
| High cholesterol | -0.3600 | 0.6645 | ±1.3290 | -0.542 | 0.5879 |  |
| Kidney disease | +0.3196 | 0.8632 | ±1.7264 | +0.370 | 0.7112 |  |
| Circulatory disease | -1.2823 | 0.7802 | ±1.5604 | -1.644 | 0.1003 |  |
| Glucose SD, pooled (mg/dL) | +0.0431 | 0.0235 | ±0.0470 | +1.836 | 0.0664 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **749**, R² = **0.1678**, Adj R² = **0.1554**, F-statistic = **13.51** (p = **9.56e-24**), Residual SE = **8.350** on **737** df, AIC = **5316.7**, BIC = **5372.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.8253** | 2.8586 | ±5.7171 | **+26.875** | **4.25e-159** | *** |
| **Education: graduate level (vs college)** | **-1.8578** | 0.7181 | ±1.4363 | **-2.587** | **0.0097** | ** |
| Education: high school or below (vs college) | -0.2174 | 0.8571 | ±1.7142 | -0.254 | 0.7998 |  |
| **Site: UCSD (vs UAB)** | **-1.7595** | 0.8107 | ±1.6213 | **-2.170** | **0.0300** | * |
| Site: UW (vs UAB) | -0.3719 | 0.7716 | ±1.5432 | -0.482 | 0.6298 |  |
| **Age (years)** | **-0.2495** | 0.0314 | ±0.0629 | **-7.938** | **2.05e-15** | *** |
| **BMI (kg/m2)** | **+0.1422** | 0.0452 | ±0.0903 | **+3.148** | **0.0016** | ** |
| Hypertension | +0.5712 | 0.7021 | ±1.4041 | +0.814 | 0.4159 |  |
| High cholesterol | -0.3729 | 0.6642 | ±1.3285 | -0.561 | 0.5746 |  |
| Kidney disease | +0.3416 | 0.8674 | ±1.7347 | +0.394 | 0.6937 |  |
| Circulatory disease | -1.2747 | 0.7800 | ±1.5600 | -1.634 | 0.1022 |  |
| Avg. daily SD (mg/dL) | +0.0433 | 0.0266 | ±0.0532 | +1.627 | 0.1038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **749**, R² = **0.1648**, Adj R² = **0.1523**, F-statistic = **13.22** (p = **3.36e-23**), Residual SE = **8.365** on **737** df, AIC = **5319.4**, BIC = **5374.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.0861** | 2.8726 | ±5.7452 | **+27.183** | **1.02e-162** | *** |
| **Education: graduate level (vs college)** | **-1.9423** | 0.7180 | ±1.4360 | **-2.705** | **0.0068** | ** |
| Education: high school or below (vs college) | +0.0047 | 0.8654 | ±1.7309 | +0.005 | 0.9957 |  |
| **Site: UCSD (vs UAB)** | **-1.8563** | 0.8135 | ±1.6270 | **-2.282** | **0.0225** | * |
| Site: UW (vs UAB) | -0.4850 | 0.7756 | ±1.5512 | -0.625 | 0.5317 |  |
| **Age (years)** | **-0.2417** | 0.0318 | ±0.0636 | **-7.596** | **3.04e-14** | *** |
| **BMI (kg/m2)** | **+0.1406** | 0.0450 | ±0.0901 | **+3.121** | **0.0018** | ** |
| Hypertension | +0.5788 | 0.7058 | ±1.4116 | +0.820 | 0.4122 |  |
| High cholesterol | -0.4443 | 0.6663 | ±1.3326 | -0.667 | 0.5049 |  |
| Kidney disease | +0.6297 | 0.8680 | ±1.7360 | +0.725 | 0.4682 |  |
| Circulatory disease | -1.2607 | 0.7811 | ±1.5622 | -1.614 | 0.1065 |  |
| CV (%) | -0.0144 | 0.0538 | ±0.1076 | -0.268 | 0.7891 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **749**, R² = **0.1649**, Adj R² = **0.1525**, F-statistic = **13.23** (p = **3.19e-23**), Residual SE = **8.365** on **737** df, AIC = **5319.3**, BIC = **5374.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.4409** | 3.2410 | ±6.4820 | **+24.203** | **2.09e-129** | *** |
| **Education: graduate level (vs college)** | **-1.9205** | 0.7181 | ±1.4362 | **-2.674** | **0.0075** | ** |
| Education: high school or below (vs college) | -0.0614 | 0.8661 | ±1.7322 | -0.071 | 0.9434 |  |
| **Site: UCSD (vs UAB)** | **-1.8255** | 0.8114 | ±1.6229 | **-2.250** | **0.0245** | * |
| Site: UW (vs UAB) | -0.4345 | 0.7737 | ±1.5473 | -0.562 | 0.5744 |  |
| **Age (years)** | **-0.2448** | 0.0318 | ±0.0636 | **-7.705** | **1.30e-14** | *** |
| **BMI (kg/m2)** | **+0.1412** | 0.0450 | ±0.0901 | **+3.135** | **0.0017** | ** |
| Hypertension | +0.5628 | 0.7052 | ±1.4104 | +0.798 | 0.4249 |  |
| High cholesterol | -0.4283 | 0.6652 | ±1.3303 | -0.644 | 0.5197 |  |
| Kidney disease | +0.5353 | 0.8567 | ±1.7134 | +0.625 | 0.5321 |  |
| Circulatory disease | -1.2698 | 0.7807 | ±1.5615 | -1.626 | 0.1038 |  |
| Mean / SD ratio | -0.1022 | 0.2313 | ±0.4625 | -0.442 | 0.6584 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **749**, R² = **0.1648**, Adj R² = **0.1523**, F-statistic = **13.22** (p = **3.41e-23**), Residual SE = **8.366** on **737** df, AIC = **5319.4**, BIC = **5374.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.1006** | 3.1997 | ±6.3994 | **+24.409** | **1.38e-131** | *** |
| **Education: graduate level (vs college)** | **-1.9272** | 0.7189 | ±1.4377 | **-2.681** | **0.0073** | ** |
| Education: high school or below (vs college) | -0.0374 | 0.8651 | ±1.7303 | -0.043 | 0.9655 |  |
| **Site: UCSD (vs UAB)** | **-1.8385** | 0.8107 | ±1.6213 | **-2.268** | **0.0233** | * |
| Site: UW (vs UAB) | -0.4531 | 0.7726 | ±1.5452 | -0.586 | 0.5576 |  |
| **Age (years)** | **-0.2438** | 0.0319 | ±0.0638 | **-7.649** | **2.02e-14** | *** |
| **BMI (kg/m2)** | **+0.1413** | 0.0450 | ±0.0900 | **+3.141** | **0.0017** | ** |
| Hypertension | +0.5683 | 0.7045 | ±1.4091 | +0.807 | 0.4199 |  |
| High cholesterol | -0.4331 | 0.6652 | ±1.3304 | -0.651 | 0.5150 |  |
| Kidney disease | +0.5681 | 0.8548 | ±1.7096 | +0.665 | 0.5063 |  |
| Circulatory disease | -1.2627 | 0.7808 | ±1.5617 | -1.617 | 0.1059 |  |
| Avg. daily mean/SD | -0.0397 | 0.1890 | ±0.3779 | -0.210 | 0.8338 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **749**, R² = **0.1726**, Adj R² = **0.1603**, F-statistic = **13.98** (p = **1.30e-24**), Residual SE = **8.326** on **737** df, AIC = **5312.4**, BIC = **5367.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.2442** | 3.1059 | ±6.2118 | **+23.904** | **2.78e-126** | *** |
| **Education: graduate level (vs college)** | **-1.8052** | 0.7157 | ±1.4315 | **-2.522** | **0.0117** | * |
| Education: high school or below (vs college) | -0.2108 | 0.8520 | ±1.7041 | -0.247 | 0.8046 |  |
| **Site: UCSD (vs UAB)** | **-1.7098** | 0.8093 | ±1.6186 | **-2.113** | **0.0346** | * |
| Site: UW (vs UAB) | -0.2298 | 0.7714 | ±1.5428 | -0.298 | 0.7658 |  |
| **Age (years)** | **-0.2437** | 0.0309 | ±0.0618 | **-7.889** | **3.06e-15** | *** |
| **BMI (kg/m2)** | **+0.1390** | 0.0454 | ±0.0908 | **+3.061** | **0.0022** | ** |
| Hypertension | +0.5999 | 0.6989 | ±1.3978 | +0.858 | 0.3907 |  |
| High cholesterol | -0.3756 | 0.6639 | ±1.3279 | -0.566 | 0.5716 |  |
| Kidney disease | +0.3842 | 0.8648 | ±1.7297 | +0.444 | 0.6568 |  |
| Circulatory disease | -1.2595 | 0.7781 | ±1.5562 | -1.619 | 0.1055 |  |
| **MAG (mg/dL/h)** | **+0.0830** | 0.0328 | ±0.0657 | **+2.528** | **0.0115** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **749**, R² = **0.1682**, Adj R² = **0.1558**, F-statistic = **13.55** (p = **8.16e-24**), Residual SE = **8.348** on **737** df, AIC = **5316.3**, BIC = **5371.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2959** | 2.9055 | ±5.8110 | **+26.259** | **5.62e-152** | *** |
| **Education: graduate level (vs college)** | **-1.8507** | 0.7190 | ±1.4379 | **-2.574** | **0.0101** | * |
| Education: high school or below (vs college) | -0.2240 | 0.8571 | ±1.7141 | -0.261 | 0.7938 |  |
| **Site: UCSD (vs UAB)** | **-1.7391** | 0.8110 | ±1.6219 | **-2.144** | **0.0320** | * |
| Site: UW (vs UAB) | -0.3646 | 0.7717 | ±1.5435 | -0.472 | 0.6366 |  |
| **Age (years)** | **-0.2491** | 0.0314 | ±0.0629 | **-7.923** | **2.31e-15** | *** |
| **BMI (kg/m2)** | **+0.1436** | 0.0452 | ±0.0904 | **+3.177** | **0.0015** | ** |
| Hypertension | +0.5988 | 0.7006 | ±1.4012 | +0.855 | 0.3927 |  |
| High cholesterol | -0.3823 | 0.6645 | ±1.3290 | -0.575 | 0.5651 |  |
| Kidney disease | +0.3274 | 0.8681 | ±1.7361 | +0.377 | 0.7060 |  |
| Circulatory disease | -1.2788 | 0.7794 | ±1.5589 | -1.641 | 0.1009 |  |
| Avg. daily range (mg/dL) | +0.0130 | 0.0074 | ±0.0147 | +1.762 | 0.0781 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **749**, R² = **0.1730**, Adj R² = **0.1606**, F-statistic = **14.01** (p = **1.12e-24**), Residual SE = **8.324** on **737** df, AIC = **5312.0**, BIC = **5367.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.9446** | 2.8066 | ±5.6132 | **+27.416** | **1.79e-165** | *** |
| **Education: graduate level (vs college)** | **-1.7713** | 0.7192 | ±1.4384 | **-2.463** | **0.0138** | * |
| Education: high school or below (vs college) | -0.2022 | 0.8455 | ±1.6910 | -0.239 | 0.8110 |  |
| **Site: UCSD (vs UAB)** | **-1.7761** | 0.8082 | ±1.6164 | **-2.198** | **0.0280** | * |
| Site: UW (vs UAB) | -0.3208 | 0.7702 | ±1.5403 | -0.417 | 0.6770 |  |
| **Age (years)** | **-0.2447** | 0.0309 | ±0.0618 | **-7.920** | **2.38e-15** | *** |
| **BMI (kg/m2)** | **+0.1326** | 0.0449 | ±0.0899 | **+2.950** | **0.0032** | ** |
| Hypertension | +0.5047 | 0.7039 | ±1.4078 | +0.717 | 0.4734 |  |
| High cholesterol | -0.3453 | 0.6647 | ±1.3294 | -0.520 | 0.6034 |  |
| Kidney disease | +0.4043 | 0.8444 | ±1.6888 | +0.479 | 0.6320 |  |
| Circulatory disease | -1.3739 | 0.7823 | ±1.5646 | -1.756 | 0.0791 | . |
| **SD of daily means (mg/dL)** | **+0.1028** | 0.0398 | ±0.0796 | **+2.583** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **749**, R² = **0.1779**, Adj R² = **0.1656**, F-statistic = **14.50** (p = **1.39e-25**), Residual SE = **8.300** on **737** df, AIC = **5307.5**, BIC = **5363.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6912** | 2.9543 | ±5.9086 | **+27.652** | **2.68e-168** | *** |
| **Education: graduate level (vs college)** | **-1.7841** | 0.7134 | ±1.4269 | **-2.501** | **0.0124** | * |
| Education: high school or below (vs college) | -0.3627 | 0.8366 | ±1.6733 | -0.434 | 0.6646 |  |
| **Site: UCSD (vs UAB)** | **-1.6437** | 0.8073 | ±1.6145 | **-2.036** | **0.0417** | * |
| Site: UW (vs UAB) | -0.3708 | 0.7659 | ±1.5317 | -0.484 | 0.6283 |  |
| **Age (years)** | **-0.2519** | 0.0309 | ±0.0619 | **-8.139** | **3.99e-16** | *** |
| **BMI (kg/m2)** | **+0.1315** | 0.0450 | ±0.0899 | **+2.923** | **0.0035** | ** |
| Hypertension | +0.6403 | 0.7003 | ±1.4006 | +0.914 | 0.3606 |  |
| High cholesterol | -0.2799 | 0.6615 | ±1.3230 | -0.423 | 0.6722 |  |
| Kidney disease | +0.3545 | 0.8542 | ±1.7084 | +0.415 | 0.6782 |  |
| Circulatory disease | -1.3309 | 0.7782 | ±1.5565 | -1.710 | 0.0872 | . |
| **Time in range 70-180, pooled (%)** | **-0.0417** | 0.0128 | ±0.0256 | **-3.256** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **749**, R² = **0.1777**, Adj R² = **0.1654**, F-statistic = **14.48** (p = **1.53e-25**), Residual SE = **8.301** on **737** df, AIC = **5307.7**, BIC = **5363.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6804** | 2.9549 | ±5.9099 | **+27.642** | **3.48e-168** | *** |
| **Education: graduate level (vs college)** | **-1.7918** | 0.7134 | ±1.4268 | **-2.512** | **0.0120** | * |
| Education: high school or below (vs college) | -0.3709 | 0.8369 | ±1.6739 | -0.443 | 0.6576 |  |
| **Site: UCSD (vs UAB)** | **-1.6362** | 0.8077 | ±1.6153 | **-2.026** | **0.0428** | * |
| Site: UW (vs UAB) | -0.3731 | 0.7661 | ±1.5321 | -0.487 | 0.6263 |  |
| **Age (years)** | **-0.2522** | 0.0310 | ±0.0619 | **-8.144** | **3.83e-16** | *** |
| **BMI (kg/m2)** | **+0.1314** | 0.0450 | ±0.0901 | **+2.917** | **0.0035** | ** |
| Hypertension | +0.6438 | 0.7004 | ±1.4008 | +0.919 | 0.3580 |  |
| High cholesterol | -0.2828 | 0.6620 | ±1.3240 | -0.427 | 0.6693 |  |
| Kidney disease | +0.3456 | 0.8549 | ±1.7097 | +0.404 | 0.6860 |  |
| Circulatory disease | -1.3296 | 0.7789 | ±1.5578 | -1.707 | 0.0878 | . |
| **Avg. daily time in range 70-180 (%)** | **-0.0411** | 0.0127 | ±0.0254 | **-3.239** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **749**, R² = **0.1648**, Adj R² = **0.1523**, F-statistic = **13.22** (p = **3.42e-23**), Residual SE = **8.366** on **737** df, AIC = **5319.4**, BIC = **5374.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8854** | 2.8027 | ±5.6053 | **+27.790** | **5.75e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9317** | 0.7160 | ±1.4319 | **-2.698** | **0.0070** | ** |
| Education: high school or below (vs college) | -0.0273 | 0.8552 | ±1.7105 | -0.032 | 0.9745 |  |
| **Site: UCSD (vs UAB)** | **-1.8555** | 0.8126 | ±1.6252 | **-2.283** | **0.0224** | * |
| Site: UW (vs UAB) | -0.4766 | 0.7754 | ±1.5508 | -0.615 | 0.5387 |  |
| **Age (years)** | **-0.2433** | 0.0311 | ±0.0621 | **-7.833** | **4.76e-15** | *** |
| **BMI (kg/m2)** | **+0.1412** | 0.0452 | ±0.0904 | **+3.125** | **0.0018** | ** |
| Hypertension | +0.5796 | 0.7068 | ±1.4137 | +0.820 | 0.4122 |  |
| High cholesterol | -0.4438 | 0.6713 | ±1.3427 | -0.661 | 0.5085 |  |
| Kidney disease | +0.5854 | 0.8461 | ±1.6923 | +0.692 | 0.4891 |  |
| Circulatory disease | -1.2548 | 0.7813 | ±1.5626 | -1.606 | 0.1083 |  |
| Any reading < 54 during wear (0/1) | -0.1270 | 0.6844 | ±1.3689 | -0.185 | 0.8528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **749**, R² = **0.1652**, Adj R² = **0.1527**, F-statistic = **13.25** (p = **2.91e-23**), Residual SE = **8.364** on **737** df, AIC = **5319.1**, BIC = **5374.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.7741** | 2.7940 | ±5.5880 | **+27.836** | **1.58e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9217** | 0.7149 | ±1.4298 | **-2.688** | **0.0072** | ** |
| Education: high school or below (vs college) | +0.0116 | 0.8575 | ±1.7150 | +0.014 | 0.9892 |  |
| **Site: UCSD (vs UAB)** | **-1.7985** | 0.8127 | ±1.6255 | **-2.213** | **0.0269** | * |
| Site: UW (vs UAB) | -0.4134 | 0.7752 | ±1.5504 | -0.533 | 0.5938 |  |
| **Age (years)** | **-0.2427** | 0.0310 | ±0.0621 | **-7.821** | **5.25e-15** | *** |
| **BMI (kg/m2)** | **+0.1399** | 0.0449 | ±0.0898 | **+3.117** | **0.0018** | ** |
| Hypertension | +0.5559 | 0.7040 | ±1.4081 | +0.790 | 0.4298 |  |
| High cholesterol | -0.4279 | 0.6657 | ±1.3315 | -0.643 | 0.5204 |  |
| Kidney disease | +0.6023 | 0.8449 | ±1.6897 | +0.713 | 0.4759 |  |
| Circulatory disease | -1.2934 | 0.7804 | ±1.5607 | -1.657 | 0.0974 | . |
| Time < 54 (%) | +0.4269 | 0.6310 | ±1.2619 | +0.677 | 0.4987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **749**, R² = **0.1647**, Adj R² = **0.1523**, F-statistic = **13.21** (p = **3.47e-23**), Residual SE = **8.366** on **737** df, AIC = **5319.5**, BIC = **5374.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8340** | 2.7988 | ±5.5976 | **+27.810** | **3.31e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9361** | 0.7148 | ±1.4297 | **-2.708** | **0.0068** | ** |
| Education: high school or below (vs college) | -0.0237 | 0.8565 | ±1.7131 | -0.028 | 0.9779 |  |
| **Site: UCSD (vs UAB)** | **-1.8474** | 0.8132 | ±1.6264 | **-2.272** | **0.0231** | * |
| Site: UW (vs UAB) | -0.4702 | 0.7745 | ±1.5491 | -0.607 | 0.5438 |  |
| **Age (years)** | **-0.2428** | 0.0311 | ±0.0623 | **-7.800** | **6.21e-15** | *** |
| **BMI (kg/m2)** | **+0.1409** | 0.0450 | ±0.0901 | **+3.128** | **0.0018** | ** |
| Hypertension | +0.5749 | 0.7037 | ±1.4075 | +0.817 | 0.4140 |  |
| High cholesterol | -0.4388 | 0.6664 | ±1.3329 | -0.658 | 0.5103 |  |
| Kidney disease | +0.5880 | 0.8447 | ±1.6893 | +0.696 | 0.4864 |  |
| Circulatory disease | -1.2583 | 0.7853 | ±1.5705 | -1.602 | 0.1091 |  |
| Avg. daily time < 54 (%) | -0.0578 | 1.0375 | ±2.0750 | -0.056 | 0.9556 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **749**, R² = **0.1652**, Adj R² = **0.1527**, F-statistic = **13.26** (p = **2.89e-23**), Residual SE = **8.364** on **737** df, AIC = **5319.1**, BIC = **5374.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8633** | 2.8004 | ±5.6007 | **+27.805** | **3.80e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9543** | 0.7161 | ±1.4322 | **-2.729** | **0.0064** | ** |
| Education: high school or below (vs college) | -0.0205 | 0.8559 | ±1.7117 | -0.024 | 0.9809 |  |
| **Site: UCSD (vs UAB)** | **-1.8838** | 0.8154 | ±1.6309 | **-2.310** | **0.0209** | * |
| Site: UW (vs UAB) | -0.5007 | 0.7726 | ±1.5453 | -0.648 | 0.5169 |  |
| **Age (years)** | **-0.2421** | 0.0311 | ±0.0623 | **-7.776** | **7.51e-15** | *** |
| **BMI (kg/m2)** | **+0.1413** | 0.0451 | ±0.0902 | **+3.132** | **0.0017** | ** |
| Hypertension | +0.5825 | 0.7038 | ±1.4076 | +0.828 | 0.4078 |  |
| High cholesterol | -0.4452 | 0.6660 | ±1.3320 | -0.669 | 0.5038 |  |
| Kidney disease | +0.5827 | 0.8443 | ±1.6886 | +0.690 | 0.4901 |  |
| Circulatory disease | -1.2463 | 0.7829 | ±1.5658 | -1.592 | 0.1114 |  |
| Time 54-69, pooled (%) | -0.1276 | 0.1874 | ±0.3748 | -0.681 | 0.4958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **749**, R² = **0.1657**, Adj R² = **0.1532**, F-statistic = **13.31** (p = **2.33e-23**), Residual SE = **8.361** on **737** df, AIC = **5318.6**, BIC = **5374.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8431** | 2.8010 | ±5.6021 | **+27.791** | **5.58e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9634** | 0.7162 | ±1.4324 | **-2.741** | **0.0061** | ** |
| Education: high school or below (vs college) | -0.0155 | 0.8551 | ±1.7101 | -0.018 | 0.9855 |  |
| **Site: UCSD (vs UAB)** | **-1.8969** | 0.8150 | ±1.6299 | **-2.328** | **0.0199** | * |
| Site: UW (vs UAB) | -0.5137 | 0.7715 | ±1.5430 | -0.666 | 0.5055 |  |
| **Age (years)** | **-0.2413** | 0.0312 | ±0.0624 | **-7.734** | **1.04e-14** | *** |
| **BMI (kg/m2)** | **+0.1414** | 0.0451 | ±0.0903 | **+3.133** | **0.0017** | ** |
| Hypertension | +0.5869 | 0.7039 | ±1.4079 | +0.834 | 0.4044 |  |
| High cholesterol | -0.4497 | 0.6656 | ±1.3313 | -0.676 | 0.4993 |  |
| Kidney disease | +0.5785 | 0.8440 | ±1.6881 | +0.685 | 0.4931 |  |
| Circulatory disease | -1.2405 | 0.7836 | ±1.5672 | -1.583 | 0.1134 |  |
| Avg. daily time 54-69 (%) | -0.1802 | 0.1932 | ±0.3864 | -0.933 | 0.3511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **749**, R² = **0.1649**, Adj R² = **0.1524**, F-statistic = **13.23** (p = **3.27e-23**), Residual SE = **8.365** on **737** df, AIC = **5319.3**, BIC = **5374.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8543** | 2.7999 | ±5.5999 | **+27.806** | **3.69e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9453** | 0.7156 | ±1.4313 | **-2.718** | **0.0066** | ** |
| Education: high school or below (vs college) | -0.0248 | 0.8563 | ±1.7125 | -0.029 | 0.9769 |  |
| **Site: UCSD (vs UAB)** | **-1.8685** | 0.8156 | ±1.6312 | **-2.291** | **0.0220** | * |
| Site: UW (vs UAB) | -0.4891 | 0.7739 | ±1.5479 | -0.632 | 0.5274 |  |
| **Age (years)** | **-0.2425** | 0.0311 | ±0.0622 | **-7.794** | **6.52e-15** | *** |
| **BMI (kg/m2)** | **+0.1412** | 0.0451 | ±0.0902 | **+3.131** | **0.0017** | ** |
| Hypertension | +0.5800 | 0.7040 | ±1.4080 | +0.824 | 0.4100 |  |
| High cholesterol | -0.4421 | 0.6661 | ±1.3322 | -0.664 | 0.5069 |  |
| Kidney disease | +0.5842 | 0.8444 | ±1.6887 | +0.692 | 0.4890 |  |
| Circulatory disease | -1.2502 | 0.7825 | ±1.5650 | -1.598 | 0.1101 |  |
| Time < 70 (%) | -0.0611 | 0.1621 | ±0.3242 | -0.377 | 0.7062 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **749**, R² = **0.1654**, Adj R² = **0.1530**, F-statistic = **13.28** (p = **2.62e-23**), Residual SE = **8.362** on **737** df, AIC = **5318.8**, BIC = **5374.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8467** | 2.8012 | ±5.6024 | **+27.790** | **5.68e-170** | *** |
| **Education: graduate level (vs college)** | **-1.9596** | 0.7158 | ±1.4316 | **-2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | -0.0249 | 0.8552 | ±1.7103 | -0.029 | 0.9768 |  |
| **Site: UCSD (vs UAB)** | **-1.8910** | 0.8150 | ±1.6299 | **-2.320** | **0.0203** | * |
| Site: UW (vs UAB) | -0.5111 | 0.7723 | ±1.5447 | -0.662 | 0.5081 |  |
| **Age (years)** | **-0.2417** | 0.0312 | ±0.0624 | **-7.744** | **9.66e-15** | *** |
| **BMI (kg/m2)** | **+0.1414** | 0.0451 | ±0.0903 | **+3.132** | **0.0017** | ** |
| Hypertension | +0.5866 | 0.7041 | ±1.4082 | +0.833 | 0.4048 |  |
| High cholesterol | -0.4501 | 0.6658 | ±1.3316 | -0.676 | 0.4990 |  |
| Kidney disease | +0.5792 | 0.8441 | ±1.6883 | +0.686 | 0.4926 |  |
| Circulatory disease | -1.2386 | 0.7837 | ±1.5675 | -1.580 | 0.1140 |  |
| Avg. daily time < 70 (%) | -0.1250 | 0.1745 | ±0.3491 | -0.716 | 0.4740 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **749**, R² = **0.1699**, Adj R² = **0.1576**, F-statistic = **13.72** (p = **3.97e-24**), Residual SE = **8.340** on **737** df, AIC = **5314.8**, BIC = **5370.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.7953** | 3.3041 | ±6.6081 | **+24.756** | **2.67e-135** | *** |
| **Education: graduate level (vs college)** | **-1.8067** | 0.7181 | ±1.4361 | **-2.516** | **0.0119** | * |
| Education: high school or below (vs college) | -0.1930 | 0.8440 | ±1.6880 | -0.229 | 0.8191 |  |
| **Site: UCSD (vs UAB)** | **-1.7630** | 0.8076 | ±1.6152 | **-2.183** | **0.0290** | * |
| Site: UW (vs UAB) | -0.3439 | 0.7746 | ±1.5491 | -0.444 | 0.6570 |  |
| **Age (years)** | **-0.2415** | 0.0309 | ±0.0617 | **-7.825** | **5.06e-15** | *** |
| **BMI (kg/m2)** | **+0.1364** | 0.0454 | ±0.0908 | **+3.006** | **0.0027** | ** |
| Hypertension | +0.5488 | 0.7030 | ±1.4060 | +0.781 | 0.4350 |  |
| High cholesterol | -0.3677 | 0.6636 | ±1.3272 | -0.554 | 0.5795 |  |
| Kidney disease | +0.4791 | 0.8513 | ±1.7025 | +0.563 | 0.5735 |  |
| Circulatory disease | -1.2856 | 0.7799 | ±1.5598 | -1.648 | 0.0993 | . |
| **Time 54-250, pooled (%)** | **-0.0427** | 0.0215 | ±0.0429 | **-1.990** | **0.0466** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **749**, R² = **0.1701**, Adj R² = **0.1577**, F-statistic = **13.73** (p = **3.71e-24**), Residual SE = **8.339** on **737** df, AIC = **5314.6**, BIC = **5370.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.9594** | 3.3285 | ±6.6571 | **+24.623** | **7.13e-134** | *** |
| **Education: graduate level (vs college)** | **-1.8066** | 0.7177 | ±1.4355 | **-2.517** | **0.0118** | * |
| Education: high school or below (vs college) | -0.1955 | 0.8443 | ±1.6886 | -0.232 | 0.8169 |  |
| **Site: UCSD (vs UAB)** | **-1.7604** | 0.8078 | ±1.6156 | **-2.179** | **0.0293** | * |
| Site: UW (vs UAB) | -0.3464 | 0.7745 | ±1.5491 | -0.447 | 0.6547 |  |
| **Age (years)** | **-0.2421** | 0.0309 | ±0.0617 | **-7.843** | **4.38e-15** | *** |
| **BMI (kg/m2)** | **+0.1362** | 0.0455 | ±0.0910 | **+2.995** | **0.0027** | ** |
| Hypertension | +0.5519 | 0.7027 | ±1.4053 | +0.785 | 0.4322 |  |
| High cholesterol | -0.3655 | 0.6638 | ±1.3276 | -0.551 | 0.5819 |  |
| Kidney disease | +0.4671 | 0.8517 | ±1.7034 | +0.548 | 0.5834 |  |
| Circulatory disease | -1.2919 | 0.7802 | ±1.5604 | -1.656 | 0.0977 | . |
| **Avg. daily time 54-250 (%)** | **-0.0439** | 0.0218 | ±0.0436 | **-2.015** | **0.0440** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **749**, R² = **0.1785**, Adj R² = **0.1662**, F-statistic = **14.56** (p = **1.09e-25**), Residual SE = **8.297** on **737** df, AIC = **5307.0**, BIC = **5362.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8333** | 2.7884 | ±5.5768 | **+27.913** | **1.84e-171** | *** |
| **Education: graduate level (vs college)** | **-1.9022** | 0.7089 | ±1.4179 | **-2.683** | **0.0073** | ** |
| Education: high school or below (vs college) | -0.3102 | 0.8451 | ±1.6902 | -0.367 | 0.7135 |  |
| **Site: UCSD (vs UAB)** | **-1.6628** | 0.8070 | ±1.6140 | **-2.060** | **0.0394** | * |
| Site: UW (vs UAB) | -0.5241 | 0.7607 | ±1.5213 | -0.689 | 0.4908 |  |
| **Age (years)** | **-0.2597** | 0.0315 | ±0.0629 | **-8.252** | **1.56e-16** | *** |
| **BMI (kg/m2)** | **+0.1327** | 0.0445 | ±0.0890 | **+2.982** | **0.0029** | ** |
| Hypertension | +0.7299 | 0.7008 | ±1.4017 | +1.041 | 0.2977 |  |
| High cholesterol | -0.2922 | 0.6624 | ±1.3248 | -0.441 | 0.6591 |  |
| Kidney disease | +0.3734 | 0.8496 | ±1.6992 | +0.439 | 0.6603 |  |
| Circulatory disease | -1.3302 | 0.7793 | ±1.5585 | -1.707 | 0.0878 | . |
| **Time 181-250, pooled (%)** | **+0.0695** | 0.0201 | ±0.0402 | **+3.463** | **5.34e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **749**, R² = **0.1781**, Adj R² = **0.1658**, F-statistic = **14.52** (p = **1.30e-25**), Residual SE = **8.299** on **737** df, AIC = **5307.4**, BIC = **5362.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.8141** | 2.7884 | ±5.5768 | **+27.907** | **2.22e-171** | *** |
| **Education: graduate level (vs college)** | **-1.9072** | 0.7095 | ±1.4189 | **-2.688** | **0.0072** | ** |
| Education: high school or below (vs college) | -0.3242 | 0.8438 | ±1.6877 | -0.384 | 0.7008 |  |
| **Site: UCSD (vs UAB)** | **-1.6507** | 0.8073 | ±1.6145 | **-2.045** | **0.0409** | * |
| Site: UW (vs UAB) | -0.5142 | 0.7613 | ±1.5226 | -0.675 | 0.4994 |  |
| **Age (years)** | **-0.2588** | 0.0314 | ±0.0628 | **-8.235** | **1.79e-16** | *** |
| **BMI (kg/m2)** | **+0.1327** | 0.0445 | ±0.0891 | **+2.980** | **0.0029** | ** |
| Hypertension | +0.7264 | 0.7014 | ±1.4028 | +1.036 | 0.3004 |  |
| High cholesterol | -0.2986 | 0.6630 | ±1.3260 | -0.450 | 0.6524 |  |
| Kidney disease | +0.3732 | 0.8503 | ±1.7006 | +0.439 | 0.6607 |  |
| Circulatory disease | -1.3192 | 0.7804 | ±1.5608 | -1.690 | 0.0910 | . |
| **Avg. daily time 181-250 (%)** | **+0.0673** | 0.0196 | ±0.0393 | **+3.429** | **6.06e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **749**, R² = **0.1778**, Adj R² = **0.1655**, F-statistic = **14.49** (p = **1.45e-25**), Residual SE = **8.300** on **737** df, AIC = **5307.6**, BIC = **5363.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.5431** | 2.7984 | ±5.5967 | **+27.710** | **5.26e-169** | *** |
| **Education: graduate level (vs college)** | **-1.7943** | 0.7130 | ±1.4260 | **-2.516** | **0.0119** | * |
| Education: high school or below (vs college) | -0.3605 | 0.8360 | ±1.6720 | -0.431 | 0.6663 |  |
| **Site: UCSD (vs UAB)** | **-1.6644** | 0.8066 | ±1.6133 | **-2.063** | **0.0391** | * |
| Site: UW (vs UAB) | -0.3888 | 0.7652 | ±1.5304 | -0.508 | 0.6114 |  |
| **Age (years)** | **-0.2515** | 0.0309 | ±0.0619 | **-8.129** | **4.31e-16** | *** |
| **BMI (kg/m2)** | **+0.1318** | 0.0450 | ±0.0900 | **+2.928** | **0.0034** | ** |
| Hypertension | +0.6439 | 0.7004 | ±1.4008 | +0.919 | 0.3579 |  |
| High cholesterol | -0.2860 | 0.6616 | ±1.3232 | -0.432 | 0.6656 |  |
| Kidney disease | +0.3549 | 0.8536 | ±1.7073 | +0.416 | 0.6776 |  |
| Circulatory disease | -1.3217 | 0.7792 | ±1.5585 | -1.696 | 0.0899 | . |
| **Time > 180 (%)** | **+0.0410** | 0.0126 | ±0.0252 | **+3.260** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **749**, R² = **0.1779**, Adj R² = **0.1656**, F-statistic = **14.49** (p = **1.42e-25**), Residual SE = **8.300** on **737** df, AIC = **5307.6**, BIC = **5363.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.5758** | 2.7999 | ±5.5999 | **+27.706** | **5.86e-169** | *** |
| **Education: graduate level (vs college)** | **-1.8008** | 0.7129 | ±1.4259 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | -0.3713 | 0.8359 | ±1.6717 | -0.444 | 0.6569 |  |
| **Site: UCSD (vs UAB)** | **-1.6529** | 0.8070 | ±1.6140 | **-2.048** | **0.0405** | * |
| Site: UW (vs UAB) | -0.3887 | 0.7653 | ±1.5307 | -0.508 | 0.6116 |  |
| **Age (years)** | **-0.2518** | 0.0310 | ±0.0619 | **-8.135** | **4.12e-16** | *** |
| **BMI (kg/m2)** | **+0.1316** | 0.0451 | ±0.0902 | **+2.919** | **0.0035** | ** |
| Hypertension | +0.6480 | 0.7005 | ±1.4009 | +0.925 | 0.3550 |  |
| High cholesterol | -0.2877 | 0.6620 | ±1.3240 | -0.435 | 0.6639 |  |
| Kidney disease | +0.3432 | 0.8544 | ±1.7087 | +0.402 | 0.6879 |  |
| Circulatory disease | -1.3216 | 0.7798 | ±1.5597 | -1.695 | 0.0901 | . |
| **Avg. daily time > 180 (%)** | **+0.0410** | 0.0125 | ±0.0250 | **+3.280** | **0.0010** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **749**, R² = **0.1749**, Adj R² = **0.1626**, F-statistic = **14.20** (p = **4.91e-25**), Residual SE = **8.315** on **737** df, AIC = **5310.3**, BIC = **5365.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.6427** | 2.8028 | ±5.6055 | **+27.702** | **6.58e-169** | *** |
| **Education: graduate level (vs college)** | **-1.7808** | 0.7183 | ±1.4366 | **-2.479** | **0.0132** | * |
| Education: high school or below (vs college) | -0.3064 | 0.8353 | ±1.6705 | -0.367 | 0.7138 |  |
| **Site: UCSD (vs UAB)** | **-1.6687** | 0.8085 | ±1.6169 | **-2.064** | **0.0390** | * |
| Site: UW (vs UAB) | -0.4110 | 0.7660 | ±1.5320 | -0.537 | 0.5916 |  |
| **Age (years)** | **-0.2458** | 0.0310 | ±0.0620 | **-7.927** | **2.24e-15** | *** |
| **BMI (kg/m2)** | **+0.1268** | 0.0450 | ±0.0899 | **+2.821** | **0.0048** | ** |
| Hypertension | +0.6286 | 0.7016 | ±1.4032 | +0.896 | 0.3703 |  |
| High cholesterol | -0.2737 | 0.6627 | ±1.3254 | -0.413 | 0.6796 |  |
| Kidney disease | +0.4269 | 0.8483 | ±1.6967 | +0.503 | 0.6148 |  |
| Circulatory disease | -1.3301 | 0.7790 | ±1.5580 | -1.707 | 0.0877 | . |
| **Nocturnal time > 180 (%)** | **+0.0348** | 0.0121 | ±0.0242 | **+2.876** | **0.0040** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **749**, R² = **0.1691**, Adj R² = **0.1567**, F-statistic = **13.64** (p = **5.61e-24**), Residual SE = **8.344** on **737** df, AIC = **5315.5**, BIC = **5370.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.5166** | 2.8109 | ±5.6218 | **+27.577** | **2.10e-167** | *** |
| **Education: graduate level (vs college)** | **-1.8397** | 0.7197 | ±1.4393 | **-2.556** | **0.0106** | * |
| Education: high school or below (vs college) | -0.1188 | 0.8491 | ±1.6982 | -0.140 | 0.8887 |  |
| **Site: UCSD (vs UAB)** | **-1.7692** | 0.8086 | ±1.6172 | **-2.188** | **0.0287** | * |
| Site: UW (vs UAB) | -0.5025 | 0.7680 | ±1.5360 | -0.654 | 0.5129 |  |
| **Age (years)** | **-0.2536** | 0.0315 | ±0.0629 | **-8.060** | **7.66e-16** | *** |
| **BMI (kg/m2)** | **+0.1441** | 0.0451 | ±0.0903 | **+3.194** | **0.0014** | ** |
| Hypertension | +0.6179 | 0.7010 | ±1.4019 | +0.882 | 0.3780 |  |
| High cholesterol | -0.3992 | 0.6648 | ±1.3295 | -0.601 | 0.5481 |  |
| Kidney disease | +0.4159 | 0.8610 | ±1.7219 | +0.483 | 0.6290 |  |
| Circulatory disease | -1.2232 | 0.7845 | ±1.5690 | -1.559 | 0.1190 |  |
| Any reading > 250 during wear (0/1) | +1.2878 | 0.6609 | ±1.3219 | +1.948 | 0.0514 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **749**, R² = **0.1698**, Adj R² = **0.1575**, F-statistic = **13.71** (p = **4.14e-24**), Residual SE = **8.340** on **737** df, AIC = **5314.9**, BIC = **5370.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.5329** | 2.8173 | ±5.6347 | **+27.520** | **1.02e-166** | *** |
| **Education: graduate level (vs college)** | **-1.8093** | 0.7181 | ±1.4361 | **-2.520** | **0.0117** | * |
| Education: high school or below (vs college) | -0.1943 | 0.8440 | ±1.6880 | -0.230 | 0.8180 |  |
| **Site: UCSD (vs UAB)** | **-1.7683** | 0.8076 | ±1.6152 | **-2.190** | **0.0286** | * |
| Site: UW (vs UAB) | -0.3503 | 0.7742 | ±1.5484 | -0.452 | 0.6509 |  |
| **Age (years)** | **-0.2416** | 0.0309 | ±0.0617 | **-7.825** | **5.06e-15** | *** |
| **BMI (kg/m2)** | **+0.1366** | 0.0454 | ±0.0908 | **+3.008** | **0.0026** | ** |
| Hypertension | +0.5507 | 0.7029 | ±1.4059 | +0.783 | 0.4333 |  |
| High cholesterol | -0.3693 | 0.6636 | ±1.3273 | -0.557 | 0.5778 |  |
| Kidney disease | +0.4790 | 0.8512 | ±1.7023 | +0.563 | 0.5736 |  |
| Circulatory disease | -1.2822 | 0.7801 | ±1.5603 | -1.644 | 0.1003 |  |
| **Time > 250 (%)** | **+0.0423** | 0.0214 | ±0.0427 | **+1.978** | **0.0479** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 749)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **749**, R² = **0.1701**, Adj R² = **0.1577**, F-statistic = **13.73** (p = **3.70e-24**), Residual SE = **8.339** on **737** df, AIC = **5314.6**, BIC = **5370.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.5680** | 2.8193 | ±5.6385 | **+27.514** | **1.21e-166** | *** |
| **Education: graduate level (vs college)** | **-1.8084** | 0.7177 | ±1.4353 | **-2.520** | **0.0117** | * |
| Education: high school or below (vs college) | -0.1984 | 0.8442 | ±1.6883 | -0.235 | 0.8142 |  |
| **Site: UCSD (vs UAB)** | **-1.7642** | 0.8078 | ±1.6155 | **-2.184** | **0.0290** | * |
| Site: UW (vs UAB) | -0.3507 | 0.7743 | ±1.5485 | -0.453 | 0.6506 |  |
| **Age (years)** | **-0.2420** | 0.0309 | ±0.0617 | **-7.841** | **4.46e-15** | *** |
| **BMI (kg/m2)** | **+0.1363** | 0.0455 | ±0.0910 | **+2.995** | **0.0027** | ** |
| Hypertension | +0.5533 | 0.7026 | ±1.4053 | +0.787 | 0.4310 |  |
| High cholesterol | -0.3670 | 0.6638 | ±1.3276 | -0.553 | 0.5804 |  |
| Kidney disease | +0.4661 | 0.8516 | ±1.7033 | +0.547 | 0.5841 |  |
| Circulatory disease | -1.2889 | 0.7804 | ±1.5607 | -1.652 | 0.0986 | . |
| **Avg. daily time > 250 (%)** | **+0.0439** | 0.0218 | ±0.0435 | **+2.020** | **0.0434** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 756; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **756**, R² = **0.0504**, Adj R² = **0.0376**, F-statistic = **3.95** (p = **2.85e-05**), Residual SE = **68.570** on **745** df, AIC = **8548.9**, BIC = **8599.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.1504** | 20.3971 | ±40.7942 | **+18.294** | **9.19e-75** | *** |
| Education: graduate level (vs college) | +5.6114 | 5.8430 | ±11.6859 | +0.960 | 0.3369 |  |
| **Education: high school or below (vs college)** | **-14.2667** | 6.8522 | ±13.7045 | **-2.082** | **0.0373** | * |
| **Site: UCSD (vs UAB)** | **-17.9203** | 6.1472 | ±12.2944 | **-2.915** | **0.0036** | ** |
| Site: UW (vs UAB) | -3.1928 | 6.5146 | ±13.0292 | -0.490 | 0.6241 |  |
| Age (years) | +0.3794 | 0.2510 | ±0.5019 | +1.512 | 0.1306 |  |
| **BMI (kg/m2)** | **-0.7870** | 0.3305 | ±0.6610 | **-2.381** | **0.0172** | * |
| **Hypertension** | **-20.8433** | 5.7111 | ±11.4221 | **-3.650** | **2.63e-04** | *** |
| High cholesterol | +2.5059 | 5.1981 | ±10.3962 | +0.482 | 0.6297 |  |
| Kidney disease | +3.8403 | 7.3688 | ±14.7377 | +0.521 | 0.6023 |  |
| Circulatory disease | +9.4203 | 6.4291 | ±12.8582 | +1.465 | 0.1429 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **756**, R² = **0.0565**, Adj R² = **0.0426**, F-statistic = **4.05** (p = **8.75e-06**), Residual SE = **68.394** on **744** df, AIC = **8546.0**, BIC = **8601.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.2874** | 22.4883 | ±44.9766 | **+17.711** | **3.46e-70** | *** |
| Education: graduate level (vs college) | +4.5369 | 5.8766 | ±11.7533 | +0.772 | 0.4401 |  |
| Education: high school or below (vs college) | -12.5511 | 6.7881 | ±13.5761 | -1.849 | 0.0645 | . |
| **Site: UCSD (vs UAB)** | **-18.3273** | 6.1080 | ±12.2160 | **-3.001** | **0.0027** | ** |
| Site: UW (vs UAB) | -3.5933 | 6.5213 | ±13.0426 | -0.551 | 0.5816 |  |
| Age (years) | +0.4075 | 0.2507 | ±0.5013 | +1.626 | 0.1040 |  |
| **BMI (kg/m2)** | **-0.7029** | 0.3342 | ±0.6684 | **-2.103** | **0.0355** | * |
| **Hypertension** | **-20.5559** | 5.6711 | ±11.3422 | **-3.625** | **2.89e-04** | *** |
| High cholesterol | +2.2341 | 5.1830 | ±10.3660 | +0.431 | 0.6664 |  |
| Kidney disease | +3.7825 | 7.3385 | ±14.6771 | +0.515 | 0.6063 |  |
| Circulatory disease | +9.1472 | 6.4068 | ±12.8136 | +1.428 | 0.1534 |  |
| **HbA1c (%)** | **-4.3528** | 1.7399 | ±3.4797 | **-2.502** | **0.0124** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **756**, R² = **0.0521**, Adj R² = **0.0381**, F-statistic = **3.72** (p = **3.53e-05**), Residual SE = **68.554** on **744** df, AIC = **8549.5**, BIC = **8605.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.6236** | 21.4362 | ±42.8725 | **+17.849** | **2.92e-71** | *** |
| Education: graduate level (vs college) | +5.1126 | 5.8856 | ±11.7711 | +0.869 | 0.3850 |  |
| **Education: high school or below (vs college)** | **-13.5136** | 6.8321 | ±13.6641 | **-1.978** | **0.0479** | * |
| **Site: UCSD (vs UAB)** | **-18.1961** | 6.1134 | ±12.2267 | **-2.976** | **0.0029** | ** |
| Site: UW (vs UAB) | -3.2733 | 6.5307 | ±13.0614 | -0.501 | 0.6162 |  |
| Age (years) | +0.3971 | 0.2534 | ±0.5068 | +1.567 | 0.1171 |  |
| **BMI (kg/m2)** | **-0.7641** | 0.3325 | ±0.6650 | **-2.298** | **0.0215** | * |
| **Hypertension** | **-20.9007** | 5.6986 | ±11.3972 | **-3.668** | **2.45e-04** | *** |
| High cholesterol | +2.2015 | 5.2019 | ±10.4038 | +0.423 | 0.6721 |  |
| Kidney disease | +4.5141 | 7.4377 | ±14.8755 | +0.607 | 0.5439 |  |
| Circulatory disease | +9.5145 | 6.4235 | ±12.8470 | +1.481 | 0.1386 |  |
| Mean glucose (mg/dL) | -0.0721 | 0.0640 | ±0.1280 | -1.126 | 0.2601 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **756**, R² = **0.0521**, Adj R² = **0.0381**, F-statistic = **3.72** (p = **3.53e-05**), Residual SE = **68.554** on **744** df, AIC = **8549.5**, BIC = **8605.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.5994** | 25.6111 | ±51.2223 | **+15.329** | **4.88e-53** | *** |
| Education: graduate level (vs college) | +5.1126 | 5.8856 | ±11.7711 | +0.869 | 0.3850 |  |
| **Education: high school or below (vs college)** | **-13.5136** | 6.8321 | ±13.6641 | **-1.978** | **0.0479** | * |
| **Site: UCSD (vs UAB)** | **-18.1961** | 6.1134 | ±12.2267 | **-2.976** | **0.0029** | ** |
| Site: UW (vs UAB) | -3.2733 | 6.5307 | ±13.0614 | -0.501 | 0.6162 |  |
| Age (years) | +0.3971 | 0.2534 | ±0.5068 | +1.567 | 0.1171 |  |
| **BMI (kg/m2)** | **-0.7641** | 0.3325 | ±0.6650 | **-2.298** | **0.0215** | * |
| **Hypertension** | **-20.9007** | 5.6986 | ±11.3972 | **-3.668** | **2.45e-04** | *** |
| High cholesterol | +2.2015 | 5.2019 | ±10.4038 | +0.423 | 0.6721 |  |
| Kidney disease | +4.5141 | 7.4377 | ±14.8755 | +0.607 | 0.5439 |  |
| Circulatory disease | +9.5145 | 6.4235 | ±12.8470 | +1.481 | 0.1386 |  |
| GMI (%) | -3.0138 | 2.6760 | ±5.3521 | -1.126 | 0.2601 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **756**, R² = **0.0510**, Adj R² = **0.0370**, F-statistic = **3.63** (p = **4.95e-05**), Residual SE = **68.593** on **744** df, AIC = **8550.4**, BIC = **8605.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+378.8169** | 21.3502 | ±42.7003 | **+17.743** | **1.95e-70** | *** |
| Education: graduate level (vs college) | +5.3253 | 5.8887 | ±11.7773 | +0.904 | 0.3658 |  |
| **Education: high school or below (vs college)** | **-13.8095** | 6.8292 | ±13.6583 | **-2.022** | **0.0432** | * |
| **Site: UCSD (vs UAB)** | **-18.0823** | 6.1296 | ±12.2591 | **-2.950** | **0.0032** | ** |
| Site: UW (vs UAB) | -3.1520 | 6.5299 | ±13.0599 | -0.483 | 0.6293 |  |
| Age (years) | +0.3815 | 0.2518 | ±0.5037 | +1.515 | 0.1299 |  |
| **BMI (kg/m2)** | **-0.7645** | 0.3345 | ±0.6690 | **-2.285** | **0.0223** | * |
| **Hypertension** | **-20.9116** | 5.7136 | ±11.4273 | **-3.660** | **2.52e-04** | *** |
| High cholesterol | +2.3206 | 5.2083 | ±10.4165 | +0.446 | 0.6559 |  |
| Kidney disease | +4.0969 | 7.4137 | ±14.8275 | +0.553 | 0.5805 |  |
| Circulatory disease | +9.4913 | 6.4281 | ±12.8561 | +1.477 | 0.1398 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0429 | 0.0631 | ±0.1262 | -0.679 | 0.4969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **756**, R² = **0.0559**, Adj R² = **0.0419**, F-statistic = **4.00** (p = **1.07e-05**), Residual SE = **68.417** on **744** df, AIC = **8546.5**, BIC = **8602.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.1975** | 20.7959 | ±41.5918 | **+18.379** | **1.95e-75** | *** |
| Education: graduate level (vs college) | +4.6401 | 5.8865 | ±11.7730 | +0.788 | 0.4305 |  |
| Education: high school or below (vs college) | -12.3893 | 6.8437 | ±13.6874 | -1.810 | 0.0702 | . |
| **Site: UCSD (vs UAB)** | **-18.6597** | 6.0731 | ±12.1462 | **-3.073** | **0.0021** | ** |
| Site: UW (vs UAB) | -4.1063 | 6.5583 | ±13.1167 | -0.626 | 0.5312 |  |
| Age (years) | +0.4434 | 0.2546 | ±0.5091 | +1.742 | 0.0815 | . |
| **BMI (kg/m2)** | **-0.7661** | 0.3324 | ±0.6648 | **-2.305** | **0.0212** | * |
| **Hypertension** | **-20.7165** | 5.6586 | ±11.3172 | **-3.661** | **2.51e-04** | *** |
| High cholesterol | +1.8515 | 5.1794 | ±10.3589 | +0.357 | 0.7207 |  |
| Kidney disease | +6.3621 | 7.6050 | ±15.2100 | +0.837 | 0.4028 |  |
| Circulatory disease | +9.5199 | 6.3891 | ±12.7782 | +1.490 | 0.1362 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.3866** | 0.1859 | ±0.3718 | **-2.080** | **0.0376** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **756**, R² = **0.0556**, Adj R² = **0.0417**, F-statistic = **3.98** (p = **1.16e-05**), Residual SE = **68.426** on **744** df, AIC = **8546.7**, BIC = **8602.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+382.7762** | 20.9042 | ±41.8084 | **+18.311** | **6.77e-75** | *** |
| Education: graduate level (vs college) | +4.7170 | 5.8718 | ±11.7436 | +0.803 | 0.4218 |  |
| Education: high school or below (vs college) | -12.3413 | 6.8585 | ±13.7170 | -1.799 | 0.0720 | . |
| **Site: UCSD (vs UAB)** | **-18.6127** | 6.0775 | ±12.1550 | **-3.063** | **0.0022** | ** |
| Site: UW (vs UAB) | -3.9750 | 6.5507 | ±13.1015 | -0.607 | 0.5440 |  |
| Age (years) | +0.4471 | 0.2549 | ±0.5097 | +1.754 | 0.0794 | . |
| **BMI (kg/m2)** | **-0.7912** | 0.3322 | ±0.6643 | **-2.382** | **0.0172** | * |
| **Hypertension** | **-20.7692** | 5.6577 | ±11.3154 | **-3.671** | **2.42e-04** | *** |
| High cholesterol | +1.8957 | 5.1768 | ±10.3537 | +0.366 | 0.7142 |  |
| Kidney disease | +6.4320 | 7.5951 | ±15.1902 | +0.847 | 0.3971 |  |
| Circulatory disease | +9.4712 | 6.4005 | ±12.8010 | +1.480 | 0.1389 |  |
| **Avg. daily SD (mg/dL)** | **-0.4340** | 0.2133 | ±0.4266 | **-2.035** | **0.0419** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **756**, R² = **0.0538**, Adj R² = **0.0398**, F-statistic = **3.85** (p = **2.05e-05**), Residual SE = **68.491** on **744** df, AIC = **8548.1**, BIC = **8603.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.7221** | 21.8524 | ±43.7048 | **+17.651** | **9.95e-70** | *** |
| Education: graduate level (vs college) | +5.0902 | 5.8635 | ±11.7270 | +0.868 | 0.3853 |  |
| Education: high school or below (vs college) | -12.9605 | 6.8875 | ±13.7750 | -1.882 | 0.0599 | . |
| **Site: UCSD (vs UAB)** | **-18.5403** | 6.0944 | ±12.1888 | **-3.042** | **0.0023** | ** |
| Site: UW (vs UAB) | -4.1659 | 6.5618 | ±13.1237 | -0.635 | 0.5255 |  |
| Age (years) | +0.4387 | 0.2554 | ±0.5108 | +1.717 | 0.0859 | . |
| **BMI (kg/m2)** | **-0.7936** | 0.3323 | ±0.6647 | **-2.388** | **0.0169** | * |
| **Hypertension** | **-20.5571** | 5.6794 | ±11.3588 | **-3.620** | **2.95e-04** | *** |
| High cholesterol | +2.1361 | 5.1834 | ±10.3667 | +0.412 | 0.6803 |  |
| Kidney disease | +5.8770 | 7.6061 | ±15.2122 | +0.773 | 0.4397 |  |
| Circulatory disease | +9.4486 | 6.4047 | ±12.8093 | +1.475 | 0.1401 |  |
| CV (%) | -0.7195 | 0.4497 | ±0.8994 | -1.600 | 0.1096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **756**, R² = **0.0543**, Adj R² = **0.0403**, F-statistic = **3.88** (p = **1.79e-05**), Residual SE = **68.475** on **744** df, AIC = **8547.8**, BIC = **8603.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+352.5146** | 24.6159 | ±49.2319 | **+14.321** | **1.63e-46** | *** |
| Education: graduate level (vs college) | +5.0795 | 5.8690 | ±11.7381 | +0.865 | 0.3868 |  |
| Education: high school or below (vs college) | -12.7845 | 6.8908 | ±13.7815 | -1.855 | 0.0636 | . |
| **Site: UCSD (vs UAB)** | **-18.4323** | 6.0860 | ±12.1721 | **-3.029** | **0.0025** | ** |
| Site: UW (vs UAB) | -4.1585 | 6.5738 | ±13.1475 | -0.633 | 0.5270 |  |
| Age (years) | +0.4466 | 0.2583 | ±0.5166 | +1.729 | 0.0838 | . |
| **BMI (kg/m2)** | **-0.7916** | 0.3318 | ±0.6636 | **-2.386** | **0.0170** | * |
| **Hypertension** | **-20.5060** | 5.6776 | ±11.3551 | **-3.612** | **3.04e-04** | *** |
| High cholesterol | +2.2432 | 5.1849 | ±10.3698 | +0.433 | 0.6653 |  |
| Kidney disease | +5.6555 | 7.5107 | ±15.0214 | +0.753 | 0.4515 |  |
| Circulatory disease | +9.6215 | 6.4026 | ±12.8052 | +1.503 | 0.1329 |  |
| Mean / SD ratio | +3.4138 | 2.2078 | ±4.4156 | +1.546 | 0.1221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **756**, R² = **0.0547**, Adj R² = **0.0407**, F-statistic = **3.91** (p = **1.55e-05**), Residual SE = **68.459** on **744** df, AIC = **8547.4**, BIC = **8602.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+352.4012** | 23.7279 | ±47.4558 | **+14.852** | **6.78e-50** | *** |
| Education: graduate level (vs college) | +5.0206 | 5.8538 | ±11.7075 | +0.858 | 0.3911 |  |
| Education: high school or below (vs college) | -12.8717 | 6.8710 | ±13.7419 | -1.873 | 0.0610 | . |
| **Site: UCSD (vs UAB)** | **-18.1292** | 6.1048 | ±12.2096 | **-2.970** | **0.0030** | ** |
| Site: UW (vs UAB) | -4.0198 | 6.5517 | ±13.1034 | -0.614 | 0.5395 |  |
| Age (years) | +0.4549 | 0.2575 | ±0.5149 | +1.767 | 0.0773 | . |
| **BMI (kg/m2)** | **-0.8170** | 0.3331 | ±0.6662 | **-2.453** | **0.0142** | * |
| **Hypertension** | **-20.4829** | 5.6761 | ±11.3521 | **-3.609** | **3.08e-04** | *** |
| High cholesterol | +2.2485 | 5.1817 | ±10.3634 | +0.434 | 0.6643 |  |
| Kidney disease | +5.4616 | 7.4432 | ±14.8864 | +0.734 | 0.4631 |  |
| Circulatory disease | +9.4074 | 6.4186 | ±12.8372 | +1.466 | 0.1427 |  |
| Avg. daily mean/SD | +3.0097 | 1.7376 | ±3.4752 | +1.732 | 0.0832 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **756**, R² = **0.0673**, Adj R² = **0.0535**, F-statistic = **4.88** (p = **2.59e-07**), Residual SE = **68.002** on **744** df, AIC = **8537.3**, BIC = **8592.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.8294** | 23.3661 | ±46.7322 | **+17.668** | **7.41e-70** | *** |
| Education: graduate level (vs college) | +3.9431 | 5.8475 | ±11.6949 | +0.674 | 0.5001 |  |
| Education: high school or below (vs college) | -12.1011 | 6.7405 | ±13.4810 | -1.795 | 0.0726 | . |
| **Site: UCSD (vs UAB)** | **-19.1740** | 6.0679 | ±12.1358 | **-3.160** | **0.0016** | ** |
| Site: UW (vs UAB) | -5.6305 | 6.4985 | ±12.9971 | -0.866 | 0.3863 |  |
| Age (years) | +0.3945 | 0.2503 | ±0.5007 | +1.576 | 0.1151 |  |
| **BMI (kg/m2)** | **-0.7562** | 0.3325 | ±0.6650 | **-2.274** | **0.0230** | * |
| **Hypertension** | **-21.0828** | 5.6265 | ±11.2530 | **-3.747** | **1.79e-04** | *** |
| High cholesterol | +2.0138 | 5.1609 | ±10.3218 | +0.390 | 0.6964 |  |
| Kidney disease | +6.1872 | 7.4398 | ±14.8797 | +0.832 | 0.4056 |  |
| Circulatory disease | +9.3529 | 6.3700 | ±12.7401 | +1.468 | 0.1420 |  |
| **MAG (mg/dL/h)** | **-0.9391** | 0.2614 | ±0.5227 | **-3.593** | **3.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **756**, R² = **0.0553**, Adj R² = **0.0413**, F-statistic = **3.96** (p = **1.28e-05**), Residual SE = **68.437** on **744** df, AIC = **8546.9**, BIC = **8602.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+386.7869** | 21.5579 | ±43.1159 | **+17.942** | **5.57e-72** | *** |
| Education: graduate level (vs college) | +4.7383 | 5.8810 | ±11.7619 | +0.806 | 0.4204 |  |
| Education: high school or below (vs college) | -12.4141 | 6.8597 | ±13.7194 | -1.810 | 0.0703 | . |
| **Site: UCSD (vs UAB)** | **-18.7126** | 6.0763 | ±12.1525 | **-3.080** | **0.0021** | ** |
| Site: UW (vs UAB) | -3.9834 | 6.5584 | ±13.1168 | -0.607 | 0.5436 |  |
| Age (years) | +0.4382 | 0.2549 | ±0.5098 | +1.719 | 0.0856 | . |
| **BMI (kg/m2)** | **-0.8046** | 0.3329 | ±0.6657 | **-2.417** | **0.0156** | * |
| **Hypertension** | **-21.0105** | 5.6670 | ±11.3339 | **-3.708** | **2.09e-04** | *** |
| High cholesterol | +2.0396 | 5.1810 | ±10.3619 | +0.394 | 0.6938 |  |
| Kidney disease | +6.3245 | 7.5695 | ±15.1390 | +0.836 | 0.4034 |  |
| Circulatory disease | +9.5138 | 6.4070 | ±12.8140 | +1.485 | 0.1376 |  |
| Avg. daily range (mg/dL) | -0.1190 | 0.0612 | ±0.1224 | -1.944 | 0.0519 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **756**, R² = **0.0541**, Adj R² = **0.0402**, F-statistic = **3.87** (p = **1.85e-05**), Residual SE = **68.479** on **744** df, AIC = **8547.9**, BIC = **8603.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+377.3680** | 20.4374 | ±40.8748 | **+18.465** | **3.98e-76** | *** |
| Education: graduate level (vs college) | +4.6989 | 5.9255 | ±11.8511 | +0.793 | 0.4278 |  |
| Education: high school or below (vs college) | -13.3240 | 6.7993 | ±13.5985 | -1.960 | 0.0500 | . |
| **Site: UCSD (vs UAB)** | **-18.2792** | 6.1037 | ±12.2074 | **-2.995** | **0.0027** | ** |
| Site: UW (vs UAB) | -3.8772 | 6.5557 | ±13.1115 | -0.591 | 0.5542 |  |
| Age (years) | +0.3913 | 0.2518 | ±0.5036 | +1.554 | 0.1202 |  |
| **BMI (kg/m2)** | **-0.7368** | 0.3319 | ±0.6638 | **-2.220** | **0.0264** | * |
| **Hypertension** | **-20.4723** | 5.6945 | ±11.3891 | **-3.595** | **3.24e-04** | *** |
| High cholesterol | +2.0785 | 5.1950 | ±10.3900 | +0.400 | 0.6891 |  |
| Kidney disease | +4.9052 | 7.5089 | ±15.0178 | +0.653 | 0.5136 |  |
| Circulatory disease | +9.9421 | 6.3764 | ±12.7527 | +1.559 | 0.1189 |  |
| SD of daily means (mg/dL) | -0.5372 | 0.3093 | ±0.6185 | -1.737 | 0.0824 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **756**, R² = **0.0517**, Adj R² = **0.0376**, F-statistic = **3.68** (p = **4.02e-05**), Residual SE = **68.569** on **744** df, AIC = **8549.8**, BIC = **8605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+363.6112** | 23.0106 | ±46.0212 | **+15.802** | **3.02e-56** | *** |
| Education: graduate level (vs college) | +5.1842 | 5.8853 | ±11.7706 | +0.881 | 0.3784 |  |
| **Education: high school or below (vs college)** | **-13.5101** | 6.8415 | ±13.6830 | **-1.975** | **0.0483** | * |
| **Site: UCSD (vs UAB)** | **-18.3614** | 6.1212 | ±12.2423 | **-3.000** | **0.0027** | ** |
| Site: UW (vs UAB) | -3.3496 | 6.5395 | ±13.0789 | -0.512 | 0.6085 |  |
| Age (years) | +0.4020 | 0.2542 | ±0.5084 | +1.582 | 0.1137 |  |
| **BMI (kg/m2)** | **-0.7624** | 0.3325 | ±0.6650 | **-2.293** | **0.0219** | * |
| **Hypertension** | **-20.9858** | 5.7075 | ±11.4151 | **-3.677** | **2.36e-04** | *** |
| High cholesterol | +2.1420 | 5.2086 | ±10.4171 | +0.411 | 0.6809 |  |
| Kidney disease | +4.4909 | 7.4498 | ±14.8996 | +0.603 | 0.5466 |  |
| Circulatory disease | +9.5544 | 6.4172 | ±12.8344 | +1.489 | 0.1365 |  |
| Time in range 70-180, pooled (%) | +0.1016 | 0.1006 | ±0.2012 | +1.009 | 0.3128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **756**, R² = **0.0517**, Adj R² = **0.0376**, F-statistic = **3.68** (p = **4.02e-05**), Residual SE = **68.569** on **744** df, AIC = **8549.8**, BIC = **8605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+363.5784** | 23.0821 | ±46.1641 | **+15.752** | **6.70e-56** | *** |
| Education: graduate level (vs college) | +5.2012 | 5.8839 | ±11.7677 | +0.884 | 0.3767 |  |
| **Education: high school or below (vs college)** | **-13.4805** | 6.8422 | ±13.6845 | **-1.970** | **0.0488** | * |
| **Site: UCSD (vs UAB)** | **-18.3858** | 6.1254 | ±12.2508 | **-3.002** | **0.0027** | ** |
| Site: UW (vs UAB) | -3.3471 | 6.5401 | ±13.0802 | -0.512 | 0.6088 |  |
| Age (years) | +0.4030 | 0.2545 | ±0.5090 | +1.583 | 0.1134 |  |
| **BMI (kg/m2)** | **-0.7623** | 0.3326 | ±0.6653 | **-2.292** | **0.0219** | * |
| **Hypertension** | **-20.9945** | 5.7088 | ±11.4175 | **-3.678** | **2.35e-04** | *** |
| High cholesterol | +2.1455 | 5.2074 | ±10.4149 | +0.412 | 0.6803 |  |
| Kidney disease | +4.5168 | 7.4600 | ±14.9201 | +0.605 | 0.5449 |  |
| Circulatory disease | +9.5531 | 6.4178 | ±12.8356 | +1.489 | 0.1366 |  |
| Avg. daily time in range 70-180 (%) | +0.1009 | 0.1004 | ±0.2009 | +1.004 | 0.3153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **756**, R² = **0.0522**, Adj R² = **0.0382**, F-statistic = **3.72** (p = **3.44e-05**), Residual SE = **68.551** on **744** df, AIC = **8549.4**, BIC = **8605.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.0572** | 20.8083 | ±41.6166 | **+17.784** | **9.39e-71** | *** |
| Education: graduate level (vs college) | +5.5568 | 5.8398 | ±11.6796 | +0.952 | 0.3413 |  |
| **Education: high school or below (vs college)** | **-13.9581** | 6.8683 | ±13.7366 | **-2.032** | **0.0421** | * |
| **Site: UCSD (vs UAB)** | **-17.2162** | 6.1709 | ±12.3418 | **-2.790** | **0.0053** | ** |
| Site: UW (vs UAB) | -2.5569 | 6.5204 | ±13.0409 | -0.392 | 0.6950 |  |
| Age (years) | +0.4043 | 0.2532 | ±0.5063 | +1.597 | 0.1103 |  |
| **BMI (kg/m2)** | **-0.8077** | 0.3288 | ±0.6577 | **-2.456** | **0.0140** | * |
| **Hypertension** | **-21.1157** | 5.7127 | ±11.4254 | **-3.696** | **2.19e-04** | *** |
| High cholesterol | +2.8443 | 5.2144 | ±10.4288 | +0.545 | 0.5854 |  |
| Kidney disease | +4.0461 | 7.3805 | ±14.7610 | +0.548 | 0.5835 |  |
| Circulatory disease | +9.0289 | 6.4720 | ±12.9439 | +1.395 | 0.1630 |  |
| Any reading < 54 during wear (0/1) | +6.7882 | 5.7530 | ±11.5059 | +1.180 | 0.2380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **756**, R² = **0.0539**, Adj R² = **0.0399**, F-statistic = **3.85** (p = **2.03e-05**), Residual SE = **68.490** on **744** df, AIC = **8548.1**, BIC = **8603.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+371.6369** | 20.3806 | ±40.7611 | **+18.235** | **2.73e-74** | *** |
| Education: graduate level (vs college) | +5.9006 | 5.8491 | ±11.6982 | +1.009 | 0.3131 |  |
| **Education: high school or below (vs college)** | **-13.6104** | 6.8541 | ±13.7081 | **-1.986** | **0.0471** | * |
| **Site: UCSD (vs UAB)** | **-16.9170** | 6.1790 | ±12.3580 | **-2.738** | **0.0062** | ** |
| Site: UW (vs UAB) | -2.0353 | 6.5514 | ±13.1028 | -0.311 | 0.7561 |  |
| Age (years) | +0.3871 | 0.2508 | ±0.5015 | +1.543 | 0.1227 |  |
| **BMI (kg/m2)** | **-0.8074** | 0.3276 | ±0.6551 | **-2.465** | **0.0137** | * |
| **Hypertension** | **-21.1354** | 5.7088 | ±11.4175 | **-3.702** | **2.14e-04** | *** |
| High cholesterol | +2.6719 | 5.1913 | ±10.3827 | +0.515 | 0.6068 |  |
| Kidney disease | +4.1374 | 7.3711 | ±14.7423 | +0.561 | 0.5746 |  |
| Circulatory disease | +8.7006 | 6.4219 | ±12.8439 | +1.355 | 0.1755 |  |
| **Time < 54 (%)** | **+9.3738** | 4.6170 | ±9.2339 | **+2.030** | **0.0423** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **756**, R² = **0.0522**, Adj R² = **0.0381**, F-statistic = **3.72** (p = **3.44e-05**), Residual SE = **68.551** on **744** df, AIC = **8549.4**, BIC = **8605.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.6544** | 20.4087 | ±40.8174 | **+18.260** | **1.74e-74** | *** |
| Education: graduate level (vs college) | +5.8937 | 5.8564 | ±11.7128 | +1.006 | 0.3142 |  |
| **Education: high school or below (vs college)** | **-13.8822** | 6.8505 | ±13.7010 | **-2.026** | **0.0427** | * |
| **Site: UCSD (vs UAB)** | **-17.3578** | 6.1718 | ±12.3437 | **-2.812** | **0.0049** | ** |
| Site: UW (vs UAB) | -2.5384 | 6.5370 | ±13.0740 | -0.388 | 0.6978 |  |
| Age (years) | +0.3752 | 0.2512 | ±0.5023 | +1.494 | 0.1352 |  |
| **BMI (kg/m2)** | **-0.7942** | 0.3297 | ±0.6595 | **-2.409** | **0.0160** | * |
| **Hypertension** | **-21.0075** | 5.7117 | ±11.4234 | **-3.678** | **2.35e-04** | *** |
| High cholesterol | +2.7229 | 5.1960 | ±10.3920 | +0.524 | 0.6002 |  |
| Kidney disease | +3.9770 | 7.3763 | ±14.7526 | +0.539 | 0.5898 |  |
| Circulatory disease | +8.9754 | 6.4193 | ±12.8385 | +1.398 | 0.1621 |  |
| Avg. daily time < 54 (%) | +6.4070 | 3.8212 | ±7.6424 | +1.677 | 0.0936 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **756**, R² = **0.0514**, Adj R² = **0.0373**, F-statistic = **3.66** (p = **4.40e-05**), Residual SE = **68.580** on **744** df, AIC = **8550.1**, BIC = **8605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.7147** | 20.4324 | ±40.8648 | **+18.241** | **2.42e-74** | *** |
| Education: graduate level (vs college) | +5.8580 | 5.8628 | ±11.7256 | +0.999 | 0.3177 |  |
| **Education: high school or below (vs college)** | **-14.2986** | 6.8598 | ±13.7195 | **-2.084** | **0.0371** | * |
| **Site: UCSD (vs UAB)** | **-17.4444** | 6.1619 | ±12.3239 | **-2.831** | **0.0046** | ** |
| Site: UW (vs UAB) | -2.7683 | 6.5390 | ±13.0779 | -0.423 | 0.6720 |  |
| Age (years) | +0.3721 | 0.2514 | ±0.5029 | +1.480 | 0.1390 |  |
| **BMI (kg/m2)** | **-0.7930** | 0.3291 | ±0.6582 | **-2.410** | **0.0160** | * |
| **Hypertension** | **-20.9385** | 5.7249 | ±11.4499 | **-3.657** | **2.55e-04** | *** |
| High cholesterol | +2.6030 | 5.2109 | ±10.4219 | +0.500 | 0.6174 |  |
| Kidney disease | +3.9217 | 7.3962 | ±14.7924 | +0.530 | 0.5960 |  |
| Circulatory disease | +9.2564 | 6.4498 | ±12.8997 | +1.435 | 0.1512 |  |
| Time 54-69, pooled (%) | +1.4737 | 1.8558 | ±3.7117 | +0.794 | 0.4272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **756**, R² = **0.0510**, Adj R² = **0.0369**, F-statistic = **3.63** (p = **4.99e-05**), Residual SE = **68.594** on **744** df, AIC = **8550.4**, BIC = **8605.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.0432** | 20.4182 | ±40.8364 | **+18.270** | **1.43e-74** | *** |
| Education: graduate level (vs college) | +5.7989 | 5.8645 | ±11.7290 | +0.989 | 0.3228 |  |
| **Education: high school or below (vs college)** | **-14.3191** | 6.8618 | ±13.7237 | **-2.087** | **0.0369** | * |
| **Site: UCSD (vs UAB)** | **-17.5951** | 6.1618 | ±12.3236 | **-2.856** | **0.0043** | ** |
| Site: UW (vs UAB) | -2.8907 | 6.5352 | ±13.0705 | -0.442 | 0.6583 |  |
| Age (years) | +0.3710 | 0.2514 | ±0.5028 | +1.476 | 0.1400 |  |
| **BMI (kg/m2)** | **-0.7913** | 0.3297 | ±0.6595 | **-2.400** | **0.0164** | * |
| **Hypertension** | **-20.9179** | 5.7244 | ±11.4488 | **-3.654** | **2.58e-04** | *** |
| High cholesterol | +2.5845 | 5.2127 | ±10.4255 | +0.496 | 0.6200 |  |
| Kidney disease | +3.9102 | 7.3880 | ±14.7761 | +0.529 | 0.5966 |  |
| Circulatory disease | +9.3057 | 6.4473 | ±12.8946 | +1.443 | 0.1489 |  |
| Avg. daily time 54-69 (%) | +1.0930 | 1.7127 | ±3.4255 | +0.638 | 0.5234 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **756**, R² = **0.0520**, Adj R² = **0.0380**, F-statistic = **3.71** (p = **3.65e-05**), Residual SE = **68.558** on **744** df, AIC = **8549.6**, BIC = **8605.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.4501** | 20.4271 | ±40.8541 | **+18.233** | **2.82e-74** | *** |
| Education: graduate level (vs college) | +5.9150 | 5.8612 | ±11.7224 | +1.009 | 0.3129 |  |
| **Education: high school or below (vs college)** | **-14.1926** | 6.8550 | ±13.7099 | **-2.070** | **0.0384** | * |
| **Site: UCSD (vs UAB)** | **-17.2616** | 6.1673 | ±12.3345 | **-2.799** | **0.0051** | ** |
| Site: UW (vs UAB) | -2.5623 | 6.5458 | ±13.0917 | -0.391 | 0.6955 |  |
| Age (years) | +0.3730 | 0.2514 | ±0.5029 | +1.484 | 0.1379 |  |
| **BMI (kg/m2)** | **-0.7965** | 0.3284 | ±0.6569 | **-2.425** | **0.0153** | * |
| **Hypertension** | **-20.9900** | 5.7241 | ±11.4483 | **-3.667** | **2.45e-04** | *** |
| High cholesterol | +2.6340 | 5.2071 | ±10.4143 | +0.506 | 0.6130 |  |
| Kidney disease | +3.9735 | 7.3936 | ±14.7872 | +0.537 | 0.5910 |  |
| Circulatory disease | +9.1323 | 6.4475 | ±12.8951 | +1.416 | 0.1567 |  |
| Time < 70 (%) | +1.5321 | 1.4007 | ±2.8013 | +1.094 | 0.2740 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **756**, R² = **0.0513**, Adj R² = **0.0373**, F-statistic = **3.66** (p = **4.51e-05**), Residual SE = **68.583** on **744** df, AIC = **8550.1**, BIC = **8605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.9546** | 20.4171 | ±40.8342 | **+18.267** | **1.52e-74** | *** |
| Education: graduate level (vs college) | +5.8520 | 5.8647 | ±11.7294 | +0.998 | 0.3184 |  |
| **Education: high school or below (vs college)** | **-14.2533** | 6.8565 | ±13.7129 | **-2.079** | **0.0376** | * |
| **Site: UCSD (vs UAB)** | **-17.4903** | 6.1657 | ±12.3313 | **-2.837** | **0.0046** | ** |
| Site: UW (vs UAB) | -2.7704 | 6.5390 | ±13.0781 | -0.424 | 0.6718 |  |
| Age (years) | +0.3701 | 0.2514 | ±0.5028 | +1.472 | 0.1410 |  |
| **BMI (kg/m2)** | **-0.7927** | 0.3295 | ±0.6590 | **-2.406** | **0.0161** | * |
| **Hypertension** | **-20.9481** | 5.7234 | ±11.4468 | **-3.660** | **2.52e-04** | *** |
| High cholesterol | +2.6239 | 5.2110 | ±10.4219 | +0.504 | 0.6146 |  |
| Kidney disease | +3.9355 | 7.3864 | ±14.7729 | +0.533 | 0.5942 |  |
| Circulatory disease | +9.2258 | 6.4438 | ±12.8876 | +1.432 | 0.1522 |  |
| Avg. daily time < 70 (%) | +1.1158 | 1.2932 | ±2.5864 | +0.863 | 0.3882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **756**, R² = **0.0504**, Adj R² = **0.0364**, F-statistic = **3.59** (p = **5.90e-05**), Residual SE = **68.614** on **744** df, AIC = **8550.8**, BIC = **8606.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.1861** | 26.2332 | ±52.4664 | **+14.111** | **3.23e-45** | *** |
| Education: graduate level (vs college) | +5.5127 | 5.9228 | ±11.8456 | +0.931 | 0.3520 |  |
| **Education: high school or below (vs college)** | **-14.1659** | 6.8172 | ±13.6345 | **-2.078** | **0.0377** | * |
| **Site: UCSD (vs UAB)** | **-17.9724** | 6.1452 | ±12.2904 | **-2.925** | **0.0034** | ** |
| Site: UW (vs UAB) | -3.2696 | 6.5093 | ±13.0185 | -0.502 | 0.6155 |  |
| Age (years) | +0.3785 | 0.2509 | ±0.5018 | +1.508 | 0.1315 |  |
| **BMI (kg/m2)** | **-0.7836** | 0.3324 | ±0.6647 | **-2.358** | **0.0184** | * |
| **Hypertension** | **-20.8256** | 5.7116 | ±11.4233 | **-3.646** | **2.66e-04** | *** |
| High cholesterol | +2.4565 | 5.2079 | ±10.4158 | +0.472 | 0.6372 |  |
| Kidney disease | +3.9305 | 7.4247 | ±14.8495 | +0.529 | 0.5965 |  |
| Circulatory disease | +9.4407 | 6.4333 | ±12.8666 | +1.467 | 0.1422 |  |
| Time 54-250, pooled (%) | +0.0318 | 0.1598 | ±0.3196 | +0.199 | 0.8422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **756**, R² = **0.0504**, Adj R² = **0.0364**, F-statistic = **3.59** (p = **5.92e-05**), Residual SE = **68.614** on **744** df, AIC = **8550.8**, BIC = **8606.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.5081** | 26.5184 | ±53.0369 | **+13.972** | **2.32e-44** | *** |
| Education: graduate level (vs college) | +5.5268 | 5.9228 | ±11.8456 | +0.933 | 0.3507 |  |
| **Education: high school or below (vs college)** | **-14.1793** | 6.8168 | ±13.6337 | **-2.080** | **0.0375** | * |
| **Site: UCSD (vs UAB)** | **-17.9666** | 6.1467 | ±12.2934 | **-2.923** | **0.0035** | ** |
| Site: UW (vs UAB) | -3.2569 | 6.5080 | ±13.0160 | -0.500 | 0.6168 |  |
| Age (years) | +0.3790 | 0.2511 | ±0.5022 | +1.509 | 0.1312 |  |
| **BMI (kg/m2)** | **-0.7840** | 0.3323 | ±0.6647 | **-2.359** | **0.0183** | * |
| **Hypertension** | **-20.8303** | 5.7121 | ±11.4241 | **-3.647** | **2.66e-04** | *** |
| High cholesterol | +2.4621 | 5.2075 | ±10.4151 | +0.473 | 0.6364 |  |
| Kidney disease | +3.9256 | 7.4343 | ±14.8687 | +0.528 | 0.5975 |  |
| Circulatory disease | +9.4419 | 6.4341 | ±12.8681 | +1.467 | 0.1422 |  |
| Avg. daily time 54-250 (%) | +0.0280 | 0.1628 | ±0.3256 | +0.172 | 0.8634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **756**, R² = **0.0534**, Adj R² = **0.0394**, F-statistic = **3.81** (p = **2.36e-05**), Residual SE = **68.507** on **744** df, AIC = **8548.5**, BIC = **8604.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.8899** | 20.4253 | ±40.8506 | **+18.256** | **1.84e-74** | *** |
| Education: graduate level (vs college) | +5.3767 | 5.8494 | ±11.6987 | +0.919 | 0.3580 |  |
| Education: high school or below (vs college) | -13.1982 | 6.8763 | ±13.7527 | -1.919 | 0.0549 | . |
| **Site: UCSD (vs UAB)** | **-18.5178** | 6.1143 | ±12.2285 | **-3.029** | **0.0025** | ** |
| Site: UW (vs UAB) | -2.9027 | 6.5310 | ±13.0620 | -0.444 | 0.6567 |  |
| Age (years) | +0.4416 | 0.2577 | ±0.5154 | +1.713 | 0.0866 | . |
| **BMI (kg/m2)** | **-0.7538** | 0.3306 | ±0.6613 | **-2.280** | **0.0226** | * |
| **Hypertension** | **-21.3512** | 5.7195 | ±11.4391 | **-3.733** | **1.89e-04** | *** |
| High cholesterol | +2.0135 | 5.2031 | ±10.4061 | +0.387 | 0.6988 |  |
| Kidney disease | +4.7499 | 7.4359 | ±14.8718 | +0.639 | 0.5230 |  |
| Circulatory disease | +9.5624 | 6.4302 | ±12.8603 | +1.487 | 0.1370 |  |
| Time 181-250, pooled (%) | -0.2508 | 0.1724 | ±0.3448 | -1.455 | 0.1458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **756**, R² = **0.0533**, Adj R² = **0.0393**, F-statistic = **3.81** (p = **2.39e-05**), Residual SE = **68.509** on **744** df, AIC = **8548.5**, BIC = **8604.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.9777** | 20.4300 | ±40.8599 | **+18.256** | **1.84e-74** | *** |
| Education: graduate level (vs college) | +5.3968 | 5.8499 | ±11.6998 | +0.923 | 0.3562 |  |
| Education: high school or below (vs college) | -13.1331 | 6.8801 | ±13.7602 | -1.909 | 0.0563 | . |
| **Site: UCSD (vs UAB)** | **-18.5731** | 6.1189 | ±12.2379 | **-3.035** | **0.0024** | ** |
| Site: UW (vs UAB) | -2.9395 | 6.5334 | ±13.0668 | -0.450 | 0.6528 |  |
| Age (years) | +0.4388 | 0.2576 | ±0.5152 | +1.703 | 0.0885 | . |
| **BMI (kg/m2)** | **-0.7541** | 0.3310 | ±0.6621 | **-2.278** | **0.0227** | * |
| **Hypertension** | **-21.3409** | 5.7192 | ±11.4383 | **-3.731** | **1.90e-04** | *** |
| High cholesterol | +2.0306 | 5.2019 | ±10.4038 | +0.390 | 0.6963 |  |
| Kidney disease | +4.7531 | 7.4410 | ±14.8820 | +0.639 | 0.5230 |  |
| Circulatory disease | +9.5280 | 6.4364 | ±12.8728 | +1.480 | 0.1388 |  |
| Avg. daily time 181-250 (%) | -0.2450 | 0.1694 | ±0.3389 | -1.446 | 0.1482 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **756**, R² = **0.0519**, Adj R² = **0.0378**, F-statistic = **3.70** (p = **3.79e-05**), Residual SE = **68.562** on **744** df, AIC = **8549.7**, BIC = **8605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.7531** | 20.4158 | ±40.8317 | **+18.307** | **7.28e-75** | *** |
| Education: graduate level (vs college) | +5.1813 | 5.8810 | ±11.7619 | +0.881 | 0.3783 |  |
| **Education: high school or below (vs college)** | **-13.4621** | 6.8401 | ±13.6802 | **-1.968** | **0.0491** | * |
| **Site: UCSD (vs UAB)** | **-18.3402** | 6.1196 | ±12.2393 | **-2.997** | **0.0027** | ** |
| Site: UW (vs UAB) | -3.3143 | 6.5386 | ±13.0771 | -0.507 | 0.6122 |  |
| Age (years) | +0.4029 | 0.2541 | ±0.5081 | +1.586 | 0.1128 |  |
| **BMI (kg/m2)** | **-0.7617** | 0.3324 | ±0.6648 | **-2.292** | **0.0219** | * |
| **Hypertension** | **-21.0041** | 5.7074 | ±11.4148 | **-3.680** | **2.33e-04** | *** |
| High cholesterol | +2.1304 | 5.2074 | ±10.4147 | +0.409 | 0.6825 |  |
| Kidney disease | +4.5371 | 7.4507 | ±14.9014 | +0.609 | 0.5426 |  |
| Circulatory disease | +9.5418 | 6.4182 | ±12.8365 | +1.487 | 0.1371 |  |
| Time > 180 (%) | -0.1073 | 0.0997 | ±0.1995 | -1.076 | 0.2820 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **756**, R² = **0.0518**, Adj R² = **0.0378**, F-statistic = **3.70** (p = **3.85e-05**), Residual SE = **68.564** on **744** df, AIC = **8549.7**, BIC = **8605.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.6675** | 20.4210 | ±40.8420 | **+18.298** | **8.55e-75** | *** |
| Education: graduate level (vs college) | +5.2065 | 5.8796 | ±11.7591 | +0.886 | 0.3759 |  |
| **Education: high school or below (vs college)** | **-13.4459** | 6.8408 | ±13.6816 | **-1.966** | **0.0493** | * |
| **Site: UCSD (vs UAB)** | **-18.3650** | 6.1234 | ±12.2467 | **-2.999** | **0.0027** | ** |
| Site: UW (vs UAB) | -3.3139 | 6.5393 | ±13.0785 | -0.507 | 0.6123 |  |
| Age (years) | +0.4031 | 0.2543 | ±0.5087 | +1.585 | 0.1130 |  |
| **BMI (kg/m2)** | **-0.7618** | 0.3325 | ±0.6651 | **-2.291** | **0.0220** | * |
| **Hypertension** | **-21.0107** | 5.7091 | ±11.4181 | **-3.680** | **2.33e-04** | *** |
| High cholesterol | +2.1413 | 5.2060 | ±10.4120 | +0.411 | 0.6808 |  |
| Kidney disease | +4.5545 | 7.4608 | ±14.9216 | +0.610 | 0.5416 |  |
| Circulatory disease | +9.5404 | 6.4192 | ±12.8384 | +1.486 | 0.1372 |  |
| Avg. daily time > 180 (%) | -0.1051 | 0.0997 | ±0.1995 | -1.054 | 0.2919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **756**, R² = **0.0504**, Adj R² = **0.0364**, F-statistic = **3.59** (p = **5.89e-05**), Residual SE = **68.614** on **744** df, AIC = **8550.8**, BIC = **8606.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.2334** | 20.4137 | ±40.8275 | **+18.283** | **1.12e-74** | *** |
| Education: graduate level (vs college) | +5.5190 | 5.8982 | ±11.7964 | +0.936 | 0.3494 |  |
| **Education: high school or below (vs college)** | **-14.1230** | 6.8382 | ±13.6764 | **-2.065** | **0.0389** | * |
| **Site: UCSD (vs UAB)** | **-18.0138** | 6.1578 | ±12.3157 | **-2.925** | **0.0034** | ** |
| Site: UW (vs UAB) | -3.2108 | 6.5315 | ±13.0631 | -0.492 | 0.6230 |  |
| Age (years) | +0.3812 | 0.2522 | ±0.5045 | +1.511 | 0.1307 |  |
| **BMI (kg/m2)** | **-0.7790** | 0.3347 | ±0.6695 | **-2.327** | **0.0200** | * |
| **Hypertension** | **-20.8745** | 5.7218 | ±11.4435 | **-3.648** | **2.64e-04** | *** |
| High cholesterol | +2.4202 | 5.2223 | ±10.4445 | +0.463 | 0.6430 |  |
| Kidney disease | +3.9476 | 7.4390 | ±14.8780 | +0.531 | 0.5957 |  |
| Circulatory disease | +9.4541 | 6.4213 | ±12.8426 | +1.472 | 0.1409 |  |
| Nocturnal time > 180 (%) | -0.0193 | 0.0932 | ±0.1863 | -0.208 | 0.8355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **756**, R² = **0.0590**, Adj R² = **0.0451**, F-statistic = **4.24** (p = **3.87e-06**), Residual SE = **68.302** on **744** df, AIC = **8543.9**, BIC = **8599.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+376.4911** | 20.3024 | ±40.6049 | **+18.544** | **9.10e-77** | *** |
| Education: graduate level (vs college) | +4.4787 | 5.8428 | ±11.6856 | +0.767 | 0.4434 |  |
| Education: high school or below (vs college) | -13.1200 | 6.8722 | ±13.7444 | -1.909 | 0.0562 | . |
| **Site: UCSD (vs UAB)** | **-18.5734** | 6.0637 | ±12.1275 | **-3.063** | **0.0022** | ** |
| Site: UW (vs UAB) | -2.5298 | 6.5129 | ±13.0258 | -0.388 | 0.6977 |  |
| Age (years) | +0.4939 | 0.2615 | ±0.5230 | +1.889 | 0.0589 | . |
| **BMI (kg/m2)** | **-0.8224** | 0.3286 | ±0.6572 | **-2.503** | **0.0123** | * |
| **Hypertension** | **-21.1783** | 5.6593 | ±11.3185 | **-3.742** | **1.82e-04** | *** |
| High cholesterol | +2.1129 | 5.1746 | ±10.3491 | +0.408 | 0.6830 |  |
| Kidney disease | +5.8565 | 7.4290 | ±14.8580 | +0.788 | 0.4305 |  |
| Circulatory disease | +8.9245 | 6.4751 | ±12.9503 | +1.378 | 0.1681 |  |
| **Any reading > 250 during wear (0/1)** | **-13.9584** | 5.6708 | ±11.3417 | **-2.461** | **0.0138** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **756**, R² = **0.0504**, Adj R² = **0.0364**, F-statistic = **3.59** (p = **5.86e-05**), Residual SE = **68.613** on **744** df, AIC = **8550.8**, BIC = **8606.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.4156** | 20.3748 | ±40.7496 | **+18.327** | **5.01e-75** | *** |
| Education: graduate level (vs college) | +5.4890 | 5.9211 | ±11.8423 | +0.927 | 0.3539 |  |
| **Education: high school or below (vs college)** | **-14.1377** | 6.8165 | ±13.6330 | **-2.074** | **0.0381** | * |
| **Site: UCSD (vs UAB)** | **-17.9813** | 6.1441 | ±12.2882 | **-2.927** | **0.0034** | ** |
| Site: UW (vs UAB) | -3.2840 | 6.5095 | ±13.0189 | -0.505 | 0.6139 |  |
| Age (years) | +0.3783 | 0.2509 | ±0.5018 | +1.508 | 0.1317 |  |
| **BMI (kg/m2)** | **-0.7829** | 0.3324 | ±0.6648 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-20.8223** | 5.7112 | ±11.4223 | **-3.646** | **2.66e-04** | *** |
| High cholesterol | +2.4447 | 5.2081 | ±10.4161 | +0.469 | 0.6388 |  |
| Kidney disease | +3.9545 | 7.4248 | ±14.8496 | +0.533 | 0.5943 |  |
| Circulatory disease | +9.4428 | 6.4323 | ±12.8647 | +1.468 | 0.1421 |  |
| Time > 250 (%) | -0.0398 | 0.1601 | ±0.3202 | -0.249 | 0.8035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 756)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **756**, R² = **0.0504**, Adj R² = **0.0364**, F-statistic = **3.59** (p = **5.89e-05**), Residual SE = **68.614** on **744** df, AIC = **8550.8**, BIC = **8606.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+373.3432** | 20.3798 | ±40.7595 | **+18.319** | **5.80e-75** | *** |
| Education: graduate level (vs college) | +5.5094 | 5.9208 | ±11.8416 | +0.931 | 0.3521 |  |
| **Education: high school or below (vs college)** | **-14.1577** | 6.8161 | ±13.6323 | **-2.077** | **0.0378** | * |
| **Site: UCSD (vs UAB)** | **-17.9740** | 6.1457 | ±12.2913 | **-2.925** | **0.0034** | ** |
| Site: UW (vs UAB) | -3.2677 | 6.5082 | ±13.0163 | -0.502 | 0.6156 |  |
| Age (years) | +0.3788 | 0.2511 | ±0.5021 | +1.509 | 0.1313 |  |
| **BMI (kg/m2)** | **-0.7834** | 0.3324 | ±0.6647 | **-2.357** | **0.0184** | * |
| **Hypertension** | **-20.8283** | 5.7118 | ±11.4235 | **-3.647** | **2.66e-04** | *** |
| High cholesterol | +2.4535 | 5.2075 | ±10.4149 | +0.471 | 0.6375 |  |
| Kidney disease | +3.9454 | 7.4343 | ±14.8687 | +0.531 | 0.5956 |  |
| Circulatory disease | +9.4443 | 6.4333 | ±12.8667 | +1.468 | 0.1421 |  |
| Avg. daily time > 250 (%) | -0.0343 | 0.1632 | ±0.3264 | -0.210 | 0.8337 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 749; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **749**, R² = **0.1347**, Adj R² = **0.1230**, F-statistic = **11.49** (p = **1.81e-18**), Residual SE = **17.485** on **738** df, AIC = **6422.8**, BIC = **6473.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.8517** | 5.7166 | ±11.4332 | **+13.269** | **3.52e-40** | *** |
| **Education: graduate level (vs college)** | **-4.9465** | 1.5137 | ±3.0273 | **-3.268** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.4562 | 1.7586 | ±3.5173 | -0.259 | 0.7953 |  |
| **Site: UCSD (vs UAB)** | **+3.5253** | 1.6779 | ±3.3558 | **+2.101** | **0.0356** | * |
| Site: UW (vs UAB) | +1.6404 | 1.5791 | ±3.1583 | +1.039 | 0.2989 |  |
| **Age (years)** | **-0.4478** | 0.0655 | ±0.1311 | **-6.834** | **8.28e-12** | *** |
| **BMI (kg/m2)** | **+0.3104** | 0.0901 | ±0.1801 | **+3.446** | **5.69e-04** | *** |
| Hypertension | +0.7133 | 1.5003 | ±3.0006 | +0.475 | 0.6345 |  |
| High cholesterol | -0.5973 | 1.3896 | ±2.7791 | -0.430 | 0.6673 |  |
| Kidney disease | +0.1349 | 1.8285 | ±3.6570 | +0.074 | 0.9412 |  |
| **Circulatory disease** | **-3.6837** | 1.6338 | ±3.2676 | **-2.255** | **0.0242** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **749**, R² = **0.1520**, Adj R² = **0.1393**, F-statistic = **12.01** (p = **6.50e-21**), Residual SE = **17.322** on **737** df, AIC = **6409.7**, BIC = **6465.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.7696** | 6.4364 | ±12.8728 | **+10.063** | **8.05e-24** | *** |
| **Education: graduate level (vs college)** | **-4.4870** | 1.5081 | ±3.0162 | **-2.975** | **0.0029** | ** |
| Education: high school or below (vs college) | -1.2442 | 1.7302 | ±3.4604 | -0.719 | 0.4721 |  |
| **Site: UCSD (vs UAB)** | **+3.7450** | 1.6565 | ±3.3130 | **+2.261** | **0.0238** | * |
| Site: UW (vs UAB) | +1.8731 | 1.5707 | ±3.1413 | +1.193 | 0.2331 |  |
| **Age (years)** | **-0.4612** | 0.0645 | ±0.1289 | **-7.155** | **8.38e-13** | *** |
| **BMI (kg/m2)** | **+0.2738** | 0.0895 | ±0.1790 | **+3.060** | **0.0022** | ** |
| Hypertension | +0.5769 | 1.4870 | ±2.9740 | +0.388 | 0.6980 |  |
| High cholesterol | -0.4740 | 1.3779 | ±2.7558 | -0.344 | 0.7308 |  |
| Kidney disease | +0.1909 | 1.8109 | ±3.6218 | +0.105 | 0.9161 |  |
| **Circulatory disease** | **-3.5751** | 1.6298 | ±3.2595 | **-2.194** | **0.0283** | * |
| **HbA1c (%)** | **+1.9215** | 0.4908 | ±0.9816 | **+3.915** | **9.04e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **749**, R² = **0.1537**, Adj R² = **0.1410**, F-statistic = **12.17** (p = **3.25e-21**), Residual SE = **17.304** on **737** df, AIC = **6408.2**, BIC = **6463.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.3958** | 6.1667 | ±12.3333 | **+10.929** | **8.37e-28** | *** |
| **Education: graduate level (vs college)** | **-4.5557** | 1.5031 | ±3.0061 | **-3.031** | **0.0024** | ** |
| Education: high school or below (vs college) | -1.2118 | 1.7113 | ±3.4226 | -0.708 | 0.4789 |  |
| **Site: UCSD (vs UAB)** | **+3.8038** | 1.6637 | ±3.3273 | **+2.286** | **0.0222** | * |
| Site: UW (vs UAB) | +1.7931 | 1.5630 | ±3.1261 | +1.147 | 0.2513 |  |
| **Age (years)** | **-0.4624** | 0.0648 | ±0.1296 | **-7.138** | **9.49e-13** | *** |
| **BMI (kg/m2)** | **+0.2920** | 0.0896 | ±0.1792 | **+3.258** | **0.0011** | ** |
| Hypertension | +0.7758 | 1.4870 | ±2.9740 | +0.522 | 0.6019 |  |
| High cholesterol | -0.3109 | 1.3819 | ±2.7638 | -0.225 | 0.8220 |  |
| Kidney disease | -0.3705 | 1.8247 | ±3.6493 | -0.203 | 0.8391 |  |
| **Circulatory disease** | **-3.7801** | 1.6204 | ±3.2408 | **-2.333** | **0.0197** | * |
| **Mean glucose (mg/dL)** | **+0.0631** | 0.0168 | ±0.0337 | **+3.752** | **1.76e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **749**, R² = **0.1537**, Adj R² = **0.1410**, F-statistic = **12.17** (p = **3.25e-21**), Residual SE = **17.304** on **737** df, AIC = **6408.2**, BIC = **6463.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6610** | 7.4131 | ±14.8262 | **+7.913** | **2.51e-15** | *** |
| **Education: graduate level (vs college)** | **-4.5557** | 1.5031 | ±3.0061 | **-3.031** | **0.0024** | ** |
| Education: high school or below (vs college) | -1.2118 | 1.7113 | ±3.4226 | -0.708 | 0.4789 |  |
| **Site: UCSD (vs UAB)** | **+3.8038** | 1.6637 | ±3.3273 | **+2.286** | **0.0222** | * |
| Site: UW (vs UAB) | +1.7931 | 1.5630 | ±3.1261 | +1.147 | 0.2513 |  |
| **Age (years)** | **-0.4624** | 0.0648 | ±0.1296 | **-7.138** | **9.49e-13** | *** |
| **BMI (kg/m2)** | **+0.2920** | 0.0896 | ±0.1792 | **+3.258** | **0.0011** | ** |
| Hypertension | +0.7758 | 1.4870 | ±2.9740 | +0.522 | 0.6019 |  |
| High cholesterol | -0.3109 | 1.3819 | ±2.7638 | -0.225 | 0.8220 |  |
| Kidney disease | -0.3705 | 1.8247 | ±3.6493 | -0.203 | 0.8391 |  |
| **Circulatory disease** | **-3.7801** | 1.6204 | ±3.2408 | **-2.333** | **0.0197** | * |
| **GMI (%)** | **+2.6389** | 0.7034 | ±1.4068 | **+3.752** | **1.76e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **749**, R² = **0.1506**, Adj R² = **0.1379**, F-statistic = **11.88** (p = **1.13e-20**), Residual SE = **17.336** on **737** df, AIC = **6410.9**, BIC = **6466.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.2003** | 6.1717 | ±12.3434 | **+11.051** | **2.18e-28** | *** |
| **Education: graduate level (vs college)** | **-4.6022** | 1.5068 | ±3.0136 | **-3.054** | **0.0023** | ** |
| Education: high school or below (vs college) | -1.1566 | 1.7148 | ±3.4296 | -0.674 | 0.5000 |  |
| **Site: UCSD (vs UAB)** | **+3.7742** | 1.6683 | ±3.3366 | **+2.262** | **0.0237** | * |
| Site: UW (vs UAB) | +1.6554 | 1.5641 | ±3.1282 | +1.058 | 0.2899 |  |
| **Age (years)** | **-0.4499** | 0.0649 | ±0.1299 | **-6.930** | **4.21e-12** | *** |
| **BMI (kg/m2)** | **+0.2811** | 0.0896 | ±0.1791 | **+3.139** | **0.0017** | ** |
| Hypertension | +0.7937 | 1.4888 | ±2.9776 | +0.533 | 0.5939 |  |
| High cholesterol | -0.3243 | 1.3871 | ±2.7741 | -0.234 | 0.8152 |  |
| Kidney disease | -0.1071 | 1.8226 | ±3.6452 | -0.059 | 0.9531 |  |
| **Circulatory disease** | **-3.7882** | 1.6232 | ±3.2463 | **-2.334** | **0.0196** | * |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0571** | 0.0168 | ±0.0336 | **+3.394** | **6.89e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **749**, R² = **0.1423**, Adj R² = **0.1295**, F-statistic = **11.12** (p = **3.11e-19**), Residual SE = **17.420** on **737** df, AIC = **6418.2**, BIC = **6473.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.8726** | 5.8140 | ±11.6281 | **+12.534** | **4.87e-36** | *** |
| **Education: graduate level (vs college)** | **-4.6808** | 1.5195 | ±3.0389 | **-3.081** | **0.0021** | ** |
| Education: high school or below (vs college) | -1.0540 | 1.7419 | ±3.4839 | -0.605 | 0.5451 |  |
| **Site: UCSD (vs UAB)** | **+3.7870** | 1.6775 | ±3.3551 | **+2.257** | **0.0240** | * |
| Site: UW (vs UAB) | +1.9703 | 1.5814 | ±3.1627 | +1.246 | 0.2128 |  |
| **Age (years)** | **-0.4674** | 0.0659 | ±0.1318 | **-7.095** | **1.30e-12** | *** |
| **BMI (kg/m2)** | **+0.3068** | 0.0899 | ±0.1798 | **+3.414** | **6.41e-04** | *** |
| Hypertension | +0.6828 | 1.4970 | ±2.9939 | +0.456 | 0.6483 |  |
| High cholesterol | -0.3773 | 1.3877 | ±2.7754 | -0.272 | 0.7857 |  |
| Kidney disease | -0.6202 | 1.8506 | ±3.7012 | -0.335 | 0.7375 |  |
| **Circulatory disease** | **-3.7378** | 1.6282 | ±3.2564 | **-2.296** | **0.0217** | * |
| **Glucose SD, pooled (mg/dL)** | **+0.1211** | 0.0500 | ±0.1000 | **+2.423** | **0.0154** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **749**, R² = **0.1419**, Adj R² = **0.1291**, F-statistic = **11.08** (p = **3.67e-19**), Residual SE = **17.424** on **737** df, AIC = **6418.5**, BIC = **6474.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.7064** | 5.8429 | ±11.6858 | **+12.444** | **1.52e-35** | *** |
| **Education: graduate level (vs college)** | **-4.7037** | 1.5180 | ±3.0361 | **-3.098** | **0.0019** | ** |
| Education: high school or below (vs college) | -1.0700 | 1.7450 | ±3.4900 | -0.613 | 0.5397 |  |
| **Site: UCSD (vs UAB)** | **+3.7755** | 1.6773 | ±3.3546 | **+2.251** | **0.0244** | * |
| Site: UW (vs UAB) | +1.9289 | 1.5813 | ±3.1626 | +1.220 | 0.2226 |  |
| **Age (years)** | **-0.4686** | 0.0661 | ±0.1322 | **-7.090** | **1.34e-12** | *** |
| **BMI (kg/m2)** | **+0.3146** | 0.0900 | ±0.1800 | **+3.494** | **4.75e-04** | *** |
| Hypertension | +0.7045 | 1.4978 | ±2.9957 | +0.470 | 0.6381 |  |
| High cholesterol | -0.3916 | 1.3868 | ±2.7736 | -0.282 | 0.7776 |  |
| Kidney disease | -0.6368 | 1.8589 | ±3.7178 | -0.343 | 0.7319 |  |
| **Circulatory disease** | **-3.7194** | 1.6281 | ±3.2562 | **-2.284** | **0.0223** | * |
| **Avg. daily SD (mg/dL)** | **+0.1354** | 0.0587 | ±0.1174 | **+2.308** | **0.0210** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **749**, R² = **0.1347**, Adj R² = **0.1218**, F-statistic = **10.43** (p = **6.33e-18**), Residual SE = **17.497** on **737** df, AIC = **6424.8**, BIC = **6480.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.0439** | 5.9773 | ±11.9546 | **+12.722** | **4.45e-37** | *** |
| **Education: graduate level (vs college)** | **-4.9532** | 1.5222 | ±3.0443 | **-3.254** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.4378 | 1.7599 | ±3.5199 | -0.249 | 0.8036 |  |
| **Site: UCSD (vs UAB)** | **+3.5152** | 1.6853 | ±3.3706 | **+2.086** | **0.0370** | * |
| Site: UW (vs UAB) | +1.6250 | 1.5909 | ±3.1819 | +1.021 | 0.3071 |  |
| **Age (years)** | **-0.4469** | 0.0667 | ±0.1335 | **-6.698** | **2.11e-11** | *** |
| **BMI (kg/m2)** | **+0.3102** | 0.0902 | ±0.1803 | **+3.440** | **5.82e-04** | *** |
| Hypertension | +0.7174 | 1.5041 | ±3.0082 | +0.477 | 0.6334 |  |
| High cholesterol | -0.6031 | 1.3898 | ±2.7797 | -0.434 | 0.6644 |  |
| Kidney disease | +0.1653 | 1.8497 | ±3.6994 | +0.089 | 0.9288 |  |
| **Circulatory disease** | **-3.6826** | 1.6356 | ±3.2712 | **-2.252** | **0.0243** | * |
| CV (%) | -0.0108 | 0.1128 | ±0.2255 | -0.096 | 0.9235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **749**, R² = **0.1351**, Adj R² = **0.1222**, F-statistic = **10.47** (p = **5.38e-18**), Residual SE = **17.493** on **737** df, AIC = **6424.4**, BIC = **6479.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.6355** | 6.4774 | ±12.9549 | **+11.986** | **4.23e-33** | *** |
| **Education: graduate level (vs college)** | **-4.9072** | 1.5215 | ±3.0429 | **-3.225** | **0.0013** | ** |
| Education: high school or below (vs college) | -0.5764 | 1.7670 | ±3.5340 | -0.326 | 0.7443 |  |
| **Site: UCSD (vs UAB)** | **+3.5730** | 1.6827 | ±3.3654 | **+2.123** | **0.0337** | * |
| Site: UW (vs UAB) | +1.7279 | 1.5876 | ±3.1752 | +1.088 | 0.2764 |  |
| **Age (years)** | **-0.4536** | 0.0664 | ±0.1328 | **-6.829** | **8.55e-12** | *** |
| **BMI (kg/m2)** | **+0.3113** | 0.0902 | ±0.1804 | **+3.452** | **5.56e-04** | *** |
| Hypertension | +0.6852 | 1.5030 | ±3.0061 | +0.456 | 0.6485 |  |
| High cholesterol | -0.5722 | 1.3902 | ±2.7804 | -0.412 | 0.6807 |  |
| Kidney disease | -0.0224 | 1.8422 | ±3.6844 | -0.012 | 0.9903 |  |
| **Circulatory disease** | **-3.7053** | 1.6364 | ±3.2728 | **-2.264** | **0.0236** | * |
| Mean / SD ratio | -0.2988 | 0.4840 | ±0.9680 | -0.617 | 0.5371 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **749**, R² = **0.1349**, Adj R² = **0.1220**, F-statistic = **10.45** (p = **5.86e-18**), Residual SE = **17.495** on **737** df, AIC = **6424.6**, BIC = **6480.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.0358** | 6.4202 | ±12.8404 | **+11.999** | **3.60e-33** | *** |
| **Education: graduate level (vs college)** | **-4.9170** | 1.5226 | ±3.0453 | **-3.229** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5318 | 1.7650 | ±3.5300 | -0.301 | 0.7632 |  |
| **Site: UCSD (vs UAB)** | **+3.5406** | 1.6811 | ±3.3622 | **+2.106** | **0.0352** | * |
| Site: UW (vs UAB) | +1.6900 | 1.5851 | ±3.1702 | +1.066 | 0.2863 |  |
| **Age (years)** | **-0.4521** | 0.0667 | ±0.1333 | **-6.781** | **1.19e-11** | *** |
| **BMI (kg/m2)** | **+0.3124** | 0.0902 | ±0.1804 | **+3.463** | **5.34e-04** | *** |
| Hypertension | +0.6939 | 1.5032 | ±3.0063 | +0.462 | 0.6444 |  |
| High cholesterol | -0.5806 | 1.3902 | ±2.7804 | -0.418 | 0.6762 |  |
| Kidney disease | +0.0427 | 1.8428 | ±3.6857 | +0.023 | 0.9815 |  |
| **Circulatory disease** | **-3.6849** | 1.6361 | ±3.2722 | **-2.252** | **0.0243** | * |
| Avg. daily mean/SD | -0.1738 | 0.3984 | ±0.7969 | -0.436 | 0.6627 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **749**, R² = **0.1402**, Adj R² = **0.1273**, F-statistic = **10.92** (p = **7.36e-19**), Residual SE = **17.442** on **737** df, AIC = **6420.1**, BIC = **6475.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.7395** | 6.3759 | ±12.7519 | **+10.938** | **7.59e-28** | *** |
| **Education: graduate level (vs college)** | **-4.7174** | 1.5160 | ±3.0320 | **-3.112** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.7732 | 1.7573 | ±3.5146 | -0.440 | 0.6600 |  |
| **Site: UCSD (vs UAB)** | **+3.7329** | 1.6812 | ±3.3623 | **+2.220** | **0.0264** | * |
| Site: UW (vs UAB) | +2.0388 | 1.5898 | ±3.1797 | +1.282 | 0.1997 |  |
| **Age (years)** | **-0.4492** | 0.0653 | ±0.1306 | **-6.880** | **6.00e-12** | *** |
| **BMI (kg/m2)** | **+0.3066** | 0.0910 | ±0.1821 | **+3.368** | **7.57e-04** | *** |
| Hypertension | +0.7658 | 1.4953 | ±2.9907 | +0.512 | 0.6086 |  |
| High cholesterol | -0.4851 | 1.3913 | ±2.7827 | -0.349 | 0.7273 |  |
| Kidney disease | -0.2105 | 1.8584 | ±3.7167 | -0.113 | 0.9098 |  |
| **Circulatory disease** | **-3.6737** | 1.6300 | ±3.2600 | **-2.254** | **0.0242** | * |
| **MAG (mg/dL/h)** | **+0.1415** | 0.0679 | ±0.1358 | **+2.085** | **0.0371** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **749**, R² = **0.1405**, Adj R² = **0.1277**, F-statistic = **10.95** (p = **6.50e-19**), Residual SE = **17.439** on **737** df, AIC = **6419.8**, BIC = **6475.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.7984** | 5.9538 | ±11.9077 | **+12.059** | **1.73e-33** | *** |
| **Education: graduate level (vs college)** | **-4.7194** | 1.5220 | ±3.0441 | **-3.101** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.9891 | 1.7480 | ±3.4960 | -0.566 | 0.5715 |  |
| **Site: UCSD (vs UAB)** | **+3.7843** | 1.6810 | ±3.3620 | **+2.251** | **0.0244** | * |
| Site: UW (vs UAB) | +1.9028 | 1.5841 | ±3.1682 | +1.201 | 0.2297 |  |
| **Age (years)** | **-0.4642** | 0.0662 | ±0.1325 | **-7.009** | **2.41e-12** | *** |
| **BMI (kg/m2)** | **+0.3173** | 0.0902 | ±0.1804 | **+3.518** | **4.34e-04** | *** |
| Hypertension | +0.7824 | 1.4964 | ±2.9928 | +0.523 | 0.6011 |  |
| High cholesterol | -0.4464 | 1.3886 | ±2.7771 | -0.321 | 0.7478 |  |
| Kidney disease | -0.5529 | 1.8600 | ±3.7200 | -0.297 | 0.7663 |  |
| **Circulatory disease** | **-3.7230** | 1.6285 | ±3.2571 | **-2.286** | **0.0222** | * |
| **Avg. daily range (mg/dL)** | **+0.0342** | 0.0163 | ±0.0326 | **+2.100** | **0.0358** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **749**, R² = **0.1415**, Adj R² = **0.1286**, F-statistic = **11.04** (p = **4.43e-19**), Residual SE = **17.429** on **737** df, AIC = **6419.0**, BIC = **6474.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.2064** | 5.7367 | ±11.4734 | **+12.935** | **2.84e-38** | *** |
| **Education: graduate level (vs college)** | **-4.6458** | 1.5237 | ±3.0474 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | -0.7959 | 1.7356 | ±3.4712 | -0.459 | 0.6465 |  |
| **Site: UCSD (vs UAB)** | **+3.6503** | 1.6774 | ±3.3548 | **+2.176** | **0.0295** | * |
| Site: UW (vs UAB) | +1.9070 | 1.5783 | ±3.1566 | +1.208 | 0.2270 |  |
| **Age (years)** | **-0.4514** | 0.0652 | ±0.1303 | **-6.926** | **4.32e-12** | *** |
| **BMI (kg/m2)** | **+0.2953** | 0.0892 | ±0.1785 | **+3.309** | **9.35e-04** | *** |
| Hypertension | +0.5775 | 1.5006 | ±3.0012 | +0.385 | 0.7004 |  |
| High cholesterol | -0.4263 | 1.3917 | ±2.7835 | -0.306 | 0.7594 |  |
| Kidney disease | -0.2074 | 1.8275 | ±3.6549 | -0.113 | 0.9096 |  |
| **Circulatory disease** | **-3.8909** | 1.6364 | ±3.2728 | **-2.378** | **0.0174** | * |
| **SD of daily means (mg/dL)** | **+0.1910** | 0.0776 | ±0.1552 | **+2.462** | **0.0138** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **749**, R² = **0.1533**, Adj R² = **0.1406**, F-statistic = **12.13** (p = **3.84e-21**), Residual SE = **17.309** on **737** df, AIC = **6408.6**, BIC = **6464.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.2578** | 6.0939 | ±12.1879 | **+13.991** | **1.78e-44** | *** |
| **Education: graduate level (vs college)** | **-4.5807** | 1.5040 | ±3.0079 | **-3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | -1.2911 | 1.7140 | ±3.4281 | -0.753 | 0.4513 |  |
| **Site: UCSD (vs UAB)** | **+4.0075** | 1.6704 | ±3.3408 | **+2.399** | **0.0164** | * |
| Site: UW (vs UAB) | +1.8681 | 1.5637 | ±3.1274 | +1.195 | 0.2322 |  |
| **Age (years)** | **-0.4699** | 0.0651 | ±0.1302 | **-7.220** | **5.18e-13** | *** |
| **BMI (kg/m2)** | **+0.2879** | 0.0893 | ±0.1785 | **+3.225** | **0.0013** | ** |
| Hypertension | +0.8639 | 1.4882 | ±2.9764 | +0.581 | 0.5616 |  |
| High cholesterol | -0.2109 | 1.3841 | ±2.7683 | -0.152 | 0.8789 |  |
| Kidney disease | -0.4342 | 1.8287 | ±3.6575 | -0.237 | 0.8123 |  |
| **Circulatory disease** | **-3.8496** | 1.6205 | ±3.2410 | **-2.376** | **0.0175** | * |
| **Time in range 70-180, pooled (%)** | **-0.1016** | 0.0263 | ±0.0526 | **-3.865** | **1.11e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **749**, R² = **0.1529**, Adj R² = **0.1403**, F-statistic = **12.09** (p = **4.44e-21**), Residual SE = **17.312** on **737** df, AIC = **6408.9**, BIC = **6464.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.2234** | 6.1004 | ±12.2008 | **+13.970** | **2.37e-44** | *** |
| **Education: graduate level (vs college)** | **-4.5996** | 1.5041 | ±3.0083 | **-3.058** | **0.0022** | ** |
| Education: high school or below (vs college) | -1.3102 | 1.7149 | ±3.4298 | -0.764 | 0.4449 |  |
| **Site: UCSD (vs UAB)** | **+4.0248** | 1.6714 | ±3.3427 | **+2.408** | **0.0160** | * |
| Site: UW (vs UAB) | +1.8622 | 1.5645 | ±3.1290 | +1.190 | 0.2339 |  |
| **Age (years)** | **-0.4707** | 0.0651 | ±0.1303 | **-7.227** | **4.95e-13** | *** |
| **BMI (kg/m2)** | **+0.2878** | 0.0895 | ±0.1790 | **+3.216** | **0.0013** | ** |
| Hypertension | +0.8728 | 1.4886 | ±2.9772 | +0.586 | 0.5577 |  |
| High cholesterol | -0.2180 | 1.3845 | ±2.7691 | -0.157 | 0.8749 |  |
| Kidney disease | -0.4554 | 1.8298 | ±3.6595 | -0.249 | 0.8034 |  |
| **Circulatory disease** | **-3.8462** | 1.6218 | ±3.2436 | **-2.372** | **0.0177** | * |
| **Avg. daily time in range 70-180 (%)** | **-0.1001** | 0.0261 | ±0.0522 | **-3.833** | **1.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **749**, R² = **0.1358**, Adj R² = **0.1229**, F-statistic = **10.53** (p = **4.20e-18**), Residual SE = **17.486** on **737** df, AIC = **6423.9**, BIC = **6479.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4519** | 5.7611 | ±11.5222 | **+13.270** | **3.44e-40** | *** |
| **Education: graduate level (vs college)** | **-4.9240** | 1.5154 | ±3.0307 | **-3.249** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5365 | 1.7561 | ±3.5122 | -0.305 | 0.7600 |  |
| **Site: UCSD (vs UAB)** | **+3.3821** | 1.6881 | ±3.3763 | **+2.003** | **0.0451** | * |
| Site: UW (vs UAB) | +1.5069 | 1.5962 | ±3.1924 | +0.944 | 0.3452 |  |
| **Age (years)** | **-0.4524** | 0.0658 | ±0.1316 | **-6.876** | **6.14e-12** | *** |
| **BMI (kg/m2)** | **+0.3145** | 0.0902 | ±0.1804 | **+3.486** | **4.90e-04** | *** |
| Hypertension | +0.7780 | 1.5060 | ±3.0120 | +0.517 | 0.6054 |  |
| High cholesterol | -0.6725 | 1.3949 | ±2.7897 | -0.482 | 0.6297 |  |
| Kidney disease | +0.0946 | 1.8341 | ±3.6683 | +0.052 | 0.9589 |  |
| **Circulatory disease** | **-3.6007** | 1.6302 | ±3.2603 | **-2.209** | **0.0272** | * |
| Any reading < 54 during wear (0/1) | -1.3896 | 1.4658 | ±2.9316 | -0.948 | 0.3431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **749**, R² = **0.1351**, Adj R² = **0.1222**, F-statistic = **10.47** (p = **5.50e-18**), Residual SE = **17.493** on **737** df, AIC = **6424.5**, BIC = **6479.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.7441** | 5.7146 | ±11.4292 | **+13.254** | **4.25e-40** | *** |
| **Education: graduate level (vs college)** | **-4.9237** | 1.5138 | ±3.0276 | **-3.253** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.3960 | 1.7668 | ±3.5337 | -0.224 | 0.8227 |  |
| **Site: UCSD (vs UAB)** | **+3.6092** | 1.6860 | ±3.3720 | **+2.141** | **0.0323** | * |
| Site: UW (vs UAB) | +1.7379 | 1.5929 | ±3.1858 | +1.091 | 0.2753 |  |
| **Age (years)** | **-0.4474** | 0.0656 | ±0.1311 | **-6.825** | **8.78e-12** | *** |
| **BMI (kg/m2)** | **+0.3086** | 0.0901 | ±0.1802 | **+3.425** | **6.14e-04** | *** |
| Hypertension | +0.6807 | 1.5018 | ±3.0036 | +0.453 | 0.6504 |  |
| High cholesterol | -0.5806 | 1.3909 | ±2.7818 | -0.417 | 0.6764 |  |
| Kidney disease | +0.1599 | 1.8310 | ±3.6621 | +0.087 | 0.9304 |  |
| **Circulatory disease** | **-3.7430** | 1.6370 | ±3.2740 | **-2.286** | **0.0222** | * |
| Time < 54 (%) | +0.8143 | 1.3729 | ±2.7458 | +0.593 | 0.5531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **749**, R² = **0.1347**, Adj R² = **0.1218**, F-statistic = **10.43** (p = **6.34e-18**), Residual SE = **17.497** on **737** df, AIC = **6424.8**, BIC = **6480.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.8467** | 5.7183 | ±11.4367 | **+13.264** | **3.76e-40** | *** |
| **Education: graduate level (vs college)** | **-4.9430** | 1.5149 | ±3.0297 | **-3.263** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.4508 | 1.7628 | ±3.5257 | -0.256 | 0.7982 |  |
| **Site: UCSD (vs UAB)** | **+3.5326** | 1.6862 | ±3.3724 | **+2.095** | **0.0362** | * |
| Site: UW (vs UAB) | +1.6488 | 1.5892 | ±3.1784 | +1.038 | 0.2995 |  |
| **Age (years)** | **-0.4479** | 0.0657 | ±0.1313 | **-6.822** | **8.98e-12** | *** |
| **BMI (kg/m2)** | **+0.3103** | 0.0902 | ±0.1804 | **+3.440** | **5.81e-04** | *** |
| Hypertension | +0.7106 | 1.5023 | ±3.0047 | +0.473 | 0.6362 |  |
| High cholesterol | -0.5944 | 1.3934 | ±2.7869 | -0.427 | 0.6697 |  |
| Kidney disease | +0.1366 | 1.8298 | ±3.6597 | +0.075 | 0.9405 |  |
| **Circulatory disease** | **-3.6895** | 1.6425 | ±3.2851 | **-2.246** | **0.0247** | * |
| Avg. daily time < 54 (%) | +0.0841 | 1.9281 | ±3.8562 | +0.044 | 0.9652 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **749**, R² = **0.1360**, Adj R² = **0.1231**, F-statistic = **10.55** (p = **3.79e-18**), Residual SE = **17.484** on **737** df, AIC = **6423.7**, BIC = **6479.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.9674** | 5.7208 | ±11.4416 | **+13.279** | **3.06e-40** | *** |
| **Education: graduate level (vs college)** | **-5.0186** | 1.5205 | ±3.0410 | **-3.301** | **9.65e-04** | *** |
| Education: high school or below (vs college) | -0.4575 | 1.7515 | ±3.5030 | -0.261 | 0.7939 |  |
| **Site: UCSD (vs UAB)** | **+3.3782** | 1.6911 | ±3.3822 | **+1.998** | **0.0458** | * |
| Site: UW (vs UAB) | +1.5123 | 1.5823 | ±3.1646 | +0.956 | 0.3392 |  |
| **Age (years)** | **-0.4452** | 0.0657 | ±0.1313 | **-6.781** | **1.20e-11** | *** |
| **BMI (kg/m2)** | **+0.3119** | 0.0903 | ±0.1806 | **+3.455** | **5.51e-04** | *** |
| Hypertension | +0.7456 | 1.5055 | ±3.0110 | +0.495 | 0.6204 |  |
| High cholesterol | -0.6263 | 1.3907 | ±2.7814 | -0.450 | 0.6525 |  |
| Kidney disease | +0.1127 | 1.8279 | ±3.6559 | +0.062 | 0.9508 |  |
| **Circulatory disease** | **-3.6270** | 1.6386 | ±3.2771 | **-2.213** | **0.0269** | * |
| Time 54-69, pooled (%) | -0.4502 | 0.4675 | ±0.9350 | -0.963 | 0.3355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **749**, R² = **0.1364**, Adj R² = **0.1235**, F-statistic = **10.58** (p = **3.27e-18**), Residual SE = **17.480** on **737** df, AIC = **6423.3**, BIC = **6478.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.8861** | 5.7179 | ±11.4358 | **+13.272** | **3.38e-40** | *** |
| **Education: graduate level (vs college)** | **-5.0264** | 1.5212 | ±3.0424 | **-3.304** | **9.52e-04** | *** |
| Education: high school or below (vs college) | -0.4435 | 1.7490 | ±3.4980 | -0.254 | 0.7998 |  |
| **Site: UCSD (vs UAB)** | **+3.3757** | 1.6913 | ±3.3827 | **+1.996** | **0.0459** | * |
| Site: UW (vs UAB) | +1.5063 | 1.5806 | ±3.1613 | +0.953 | 0.3406 |  |
| **Age (years)** | **-0.4437** | 0.0657 | ±0.1314 | **-6.752** | **1.46e-11** | *** |
| **BMI (kg/m2)** | **+0.3119** | 0.0902 | ±0.1805 | **+3.457** | **5.47e-04** | *** |
| Hypertension | +0.7495 | 1.5063 | ±3.0127 | +0.498 | 0.6188 |  |
| High cholesterol | -0.6313 | 1.3902 | ±2.7804 | -0.454 | 0.6497 |  |
| Kidney disease | +0.1065 | 1.8278 | ±3.6557 | +0.058 | 0.9535 |  |
| **Circulatory disease** | **-3.6240** | 1.6391 | ±3.2782 | **-2.211** | **0.0270** | * |
| Avg. daily time 54-69 (%) | -0.4898 | 0.4621 | ±0.9241 | -1.060 | 0.2892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **749**, R² = **0.1354**, Adj R² = **0.1224**, F-statistic = **10.49** (p = **4.96e-18**), Residual SE = **17.491** on **737** df, AIC = **6424.3**, BIC = **6479.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.9511** | 5.7223 | ±11.4447 | **+13.273** | **3.33e-40** | *** |
| **Education: graduate level (vs college)** | **-4.9946** | 1.5186 | ±3.0372 | **-3.289** | **0.0010** | ** |
| Education: high school or below (vs college) | -0.4758 | 1.7552 | ±3.5105 | -0.271 | 0.7863 |  |
| **Site: UCSD (vs UAB)** | **+3.4156** | 1.6910 | ±3.3820 | **+2.020** | **0.0434** | * |
| Site: UW (vs UAB) | +1.5372 | 1.5866 | ±3.1733 | +0.969 | 0.3326 |  |
| **Age (years)** | **-0.4465** | 0.0656 | ±0.1313 | **-6.801** | **1.04e-11** | *** |
| **BMI (kg/m2)** | **+0.3118** | 0.0904 | ±0.1807 | **+3.451** | **5.59e-04** | *** |
| Hypertension | +0.7419 | 1.5048 | ±3.0096 | +0.493 | 0.6220 |  |
| High cholesterol | -0.6190 | 1.3915 | ±2.7829 | -0.445 | 0.6564 |  |
| Kidney disease | +0.1144 | 1.8290 | ±3.6581 | +0.063 | 0.9501 |  |
| **Circulatory disease** | **-3.6329** | 1.6392 | ±3.2784 | **-2.216** | **0.0267** | * |
| Time < 70 (%) | -0.2554 | 0.4000 | ±0.7999 | -0.639 | 0.5231 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **749**, R² = **0.1358**, Adj R² = **0.1229**, F-statistic = **10.53** (p = **4.12e-18**), Residual SE = **17.486** on **737** df, AIC = **6423.8**, BIC = **6479.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.8939** | 5.7195 | ±11.4391 | **+13.269** | **3.49e-40** | *** |
| **Education: graduate level (vs college)** | **-5.0133** | 1.5196 | ±3.0393 | **-3.299** | **9.70e-04** | *** |
| Education: high school or below (vs college) | -0.4685 | 1.7521 | ±3.5041 | -0.267 | 0.7892 |  |
| **Site: UCSD (vs UAB)** | **+3.3977** | 1.6906 | ±3.3812 | **+2.010** | **0.0445** | * |
| Site: UW (vs UAB) | +1.5189 | 1.5834 | ±3.1667 | +0.959 | 0.3374 |  |
| **Age (years)** | **-0.4448** | 0.0657 | ±0.1315 | **-6.767** | **1.32e-11** | *** |
| **BMI (kg/m2)** | **+0.3117** | 0.0903 | ±0.1806 | **+3.452** | **5.56e-04** | *** |
| Hypertension | +0.7476 | 1.5056 | ±3.0112 | +0.497 | 0.6195 |  |
| High cholesterol | -0.6312 | 1.3910 | ±2.7821 | -0.454 | 0.6500 |  |
| Kidney disease | +0.1094 | 1.8286 | ±3.6571 | +0.060 | 0.9523 |  |
| **Circulatory disease** | **-3.6215** | 1.6400 | ±3.2799 | **-2.208** | **0.0272** | * |
| Avg. daily time < 70 (%) | -0.3255 | 0.3947 | ±0.7895 | -0.825 | 0.4096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **749**, R² = **0.1433**, Adj R² = **0.1306**, F-statistic = **11.21** (p = **2.09e-19**), Residual SE = **17.410** on **737** df, AIC = **6417.3**, BIC = **6472.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+86.3276** | 7.1779 | ±14.3557 | **+12.027** | **2.57e-33** | *** |
| **Education: graduate level (vs college)** | **-4.6109** | 1.5167 | ±3.0333 | **-3.040** | **0.0024** | ** |
| Education: high school or below (vs college) | -0.9137 | 1.7328 | ±3.4657 | -0.527 | 0.5980 |  |
| **Site: UCSD (vs UAB)** | **+3.7351** | 1.6709 | ±3.3418 | **+2.235** | **0.0254** | * |
| Site: UW (vs UAB) | +1.9587 | 1.5877 | ±3.1754 | +1.234 | 0.2173 |  |
| **Age (years)** | **-0.4443** | 0.0648 | ±0.1296 | **-6.859** | **6.95e-12** | *** |
| **BMI (kg/m2)** | **+0.2988** | 0.0900 | ±0.1799 | **+3.322** | **8.94e-04** | *** |
| Hypertension | +0.6434 | 1.4980 | ±2.9960 | +0.430 | 0.6675 |  |
| High cholesterol | -0.4135 | 1.3905 | ±2.7810 | -0.297 | 0.7662 |  |
| Kidney disease | -0.1550 | 1.8299 | ±3.6599 | -0.085 | 0.9325 |  |
| **Circulatory disease** | **-3.7448** | 1.6252 | ±3.2505 | **-2.304** | **0.0212** | * |
| **Time 54-250, pooled (%)** | **-0.1129** | 0.0483 | ±0.0967 | **-2.335** | **0.0195** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **749**, R² = **0.1435**, Adj R² = **0.1308**, F-statistic = **11.23** (p = **1.93e-19**), Residual SE = **17.408** on **737** df, AIC = **6417.1**, BIC = **6472.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+86.7175** | 7.2651 | ±14.5301 | **+11.936** | **7.66e-33** | *** |
| **Education: graduate level (vs college)** | **-4.6121** | 1.5163 | ±3.0325 | **-3.042** | **0.0024** | ** |
| Education: high school or below (vs college) | -0.9185 | 1.7322 | ±3.4644 | -0.530 | 0.5960 |  |
| **Site: UCSD (vs UAB)** | **+3.7412** | 1.6710 | ±3.3420 | **+2.239** | **0.0252** | * |
| Site: UW (vs UAB) | +1.9511 | 1.5871 | ±3.1742 | +1.229 | 0.2189 |  |
| **Age (years)** | **-0.4458** | 0.0648 | ±0.1296 | **-6.878** | **6.05e-12** | *** |
| **BMI (kg/m2)** | **+0.2984** | 0.0902 | ±0.1803 | **+3.309** | **9.36e-04** | *** |
| Hypertension | +0.6521 | 1.4972 | ±2.9943 | +0.436 | 0.6631 |  |
| High cholesterol | -0.4083 | 1.3908 | ±2.7816 | -0.294 | 0.7691 |  |
| Kidney disease | -0.1855 | 1.8305 | ±3.6610 | -0.101 | 0.9193 |  |
| **Circulatory disease** | **-3.7612** | 1.6256 | ±3.2512 | **-2.314** | **0.0207** | * |
| **Avg. daily time 54-250 (%)** | **-0.1156** | 0.0493 | ±0.0987 | **-2.343** | **0.0191** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **749**, R² = **0.1524**, Adj R² = **0.1397**, F-statistic = **12.04** (p = **5.49e-21**), Residual SE = **17.318** on **737** df, AIC = **6409.4**, BIC = **6464.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.8582** | 5.6960 | ±11.3919 | **+13.318** | **1.82e-40** | *** |
| **Education: graduate level (vs college)** | **-4.8708** | 1.4986 | ±2.9972 | **-3.250** | **0.0012** | ** |
| Education: high school or below (vs college) | -1.1313 | 1.7275 | ±3.4550 | -0.655 | 0.5125 |  |
| **Site: UCSD (vs UAB)** | **+3.9400** | 1.6751 | ±3.3502 | **+2.352** | **0.0187** | * |
| Site: UW (vs UAB) | +1.5006 | 1.5541 | ±3.1081 | +0.966 | 0.3342 |  |
| **Age (years)** | **-0.4871** | 0.0660 | ±0.1320 | **-7.380** | **1.58e-13** | *** |
| **BMI (kg/m2)** | **+0.2917** | 0.0893 | ±0.1786 | **+3.267** | **0.0011** | ** |
| Hypertension | +1.0653 | 1.4914 | ±2.9829 | +0.714 | 0.4751 |  |
| High cholesterol | -0.2554 | 1.3829 | ±2.7658 | -0.185 | 0.8535 |  |
| Kidney disease | -0.3645 | 1.8269 | ±3.6538 | -0.200 | 0.8418 |  |
| **Circulatory disease** | **-3.8400** | 1.6274 | ±3.2549 | **-2.360** | **0.0183** | * |
| **Time 181-250, pooled (%)** | **+0.1619** | 0.0415 | ±0.0829 | **+3.905** | **9.41e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **749**, R² = **0.1517**, Adj R² = **0.1391**, F-statistic = **11.98** (p = **7.14e-21**), Residual SE = **17.324** on **737** df, AIC = **6409.9**, BIC = **6465.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.8136** | 5.6971 | ±11.3941 | **+13.308** | **2.09e-40** | *** |
| **Education: graduate level (vs college)** | **-4.8823** | 1.5000 | ±3.0000 | **-3.255** | **0.0011** | ** |
| Education: high school or below (vs college) | -1.1609 | 1.7266 | ±3.4533 | -0.672 | 0.5014 |  |
| **Site: UCSD (vs UAB)** | **+3.9658** | 1.6759 | ±3.3518 | **+2.366** | **0.0180** | * |
| Site: UW (vs UAB) | +1.5241 | 1.5560 | ±3.1120 | +0.980 | 0.3273 |  |
| **Age (years)** | **-0.4849** | 0.0659 | ±0.1319 | **-7.355** | **1.91e-13** | *** |
| **BMI (kg/m2)** | **+0.2919** | 0.0894 | ±0.1788 | **+3.264** | **0.0011** | ** |
| Hypertension | +1.0565 | 1.4929 | ±2.9858 | +0.708 | 0.4792 |  |
| High cholesterol | -0.2713 | 1.3835 | ±2.7670 | -0.196 | 0.8445 |  |
| Kidney disease | -0.3629 | 1.8282 | ±3.6564 | -0.198 | 0.8427 |  |
| **Circulatory disease** | **-3.8136** | 1.6297 | ±3.2594 | **-2.340** | **0.0193** | * |
| **Avg. daily time 181-250 (%)** | **+0.1562** | 0.0407 | ±0.0814 | **+3.838** | **1.24e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **749**, R² = **0.1533**, Adj R² = **0.1407**, F-statistic = **12.13** (p = **3.75e-21**), Residual SE = **17.308** on **737** df, AIC = **6408.5**, BIC = **6464.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.1475** | 5.6691 | ±11.3382 | **+13.256** | **4.19e-40** | *** |
| **Education: graduate level (vs college)** | **-4.6034** | 1.5033 | ±3.0066 | **-3.062** | **0.0022** | ** |
| Education: high school or below (vs college) | -1.2903 | 1.7123 | ±3.4246 | -0.754 | 0.4511 |  |
| **Site: UCSD (vs UAB)** | **+3.9593** | 1.6697 | ±3.3393 | **+2.371** | **0.0177** | * |
| Site: UW (vs UAB) | +1.8251 | 1.5619 | ±3.1238 | +1.168 | 0.2426 |  |
| **Age (years)** | **-0.4691** | 0.0651 | ±0.1301 | **-7.209** | **5.64e-13** | *** |
| **BMI (kg/m2)** | **+0.2887** | 0.0893 | ±0.1787 | **+3.231** | **0.0012** | ** |
| Hypertension | +0.8736 | 1.4887 | ±2.9773 | +0.587 | 0.5573 |  |
| High cholesterol | -0.2234 | 1.3839 | ±2.7679 | -0.161 | 0.8718 |  |
| Kidney disease | -0.4364 | 1.8281 | ±3.6561 | -0.239 | 0.8113 |  |
| **Circulatory disease** | **-3.8279** | 1.6215 | ±3.2430 | **-2.361** | **0.0182** | * |
| **Time > 180 (%)** | **+0.1005** | 0.0259 | ±0.0518 | **+3.883** | **1.03e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **749**, R² = **0.1532**, Adj R² = **0.1406**, F-statistic = **12.12** (p = **3.94e-21**), Residual SE = **17.309** on **737** df, AIC = **6408.6**, BIC = **6464.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.2308** | 5.6748 | ±11.3497 | **+13.257** | **4.11e-40** | *** |
| **Education: graduate level (vs college)** | **-4.6209** | 1.5034 | ±3.0069 | **-3.074** | **0.0021** | ** |
| Education: high school or below (vs college) | -1.3119 | 1.7124 | ±3.4249 | -0.766 | 0.4436 |  |
| **Site: UCSD (vs UAB)** | **+3.9844** | 1.6706 | ±3.3412 | **+2.385** | **0.0171** | * |
| Site: UW (vs UAB) | +1.8244 | 1.5625 | ±3.1251 | +1.168 | 0.2430 |  |
| **Age (years)** | **-0.4697** | 0.0651 | ±0.1302 | **-7.213** | **5.46e-13** | *** |
| **BMI (kg/m2)** | **+0.2883** | 0.0895 | ±0.1791 | **+3.220** | **0.0013** | ** |
| Hypertension | +0.8829 | 1.4890 | ±2.9781 | +0.593 | 0.5532 |  |
| High cholesterol | -0.2293 | 1.3841 | ±2.7681 | -0.166 | 0.8684 |  |
| Kidney disease | -0.4619 | 1.8292 | ±3.6583 | -0.252 | 0.8007 |  |
| **Circulatory disease** | **-3.8267** | 1.6226 | ±3.2453 | **-2.358** | **0.0184** | * |
| **Avg. daily time > 180 (%)** | **+0.0998** | 0.0258 | ±0.0515 | **+3.877** | **1.06e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **749**, R² = **0.1483**, Adj R² = **0.1356**, F-statistic = **11.67** (p = **2.83e-20**), Residual SE = **17.359** on **737** df, AIC = **6412.9**, BIC = **6468.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.4058** | 5.7045 | ±11.4090 | **+13.219** | **6.85e-40** | *** |
| **Education: graduate level (vs college)** | **-4.5846** | 1.5136 | ±3.0273 | **-3.029** | **0.0025** | ** |
| Education: high school or below (vs college) | -1.1371 | 1.7151 | ±3.4302 | -0.663 | 0.5073 |  |
| **Site: UCSD (vs UAB)** | **+3.9393** | 1.6750 | ±3.3501 | **+2.352** | **0.0187** | * |
| Site: UW (vs UAB) | +1.7671 | 1.5654 | ±3.1309 | +1.129 | 0.2590 |  |
| **Age (years)** | **-0.4549** | 0.0654 | ±0.1307 | **-6.958** | **3.44e-12** | *** |
| **BMI (kg/m2)** | **+0.2775** | 0.0897 | ±0.1794 | **+3.094** | **0.0020** | ** |
| Hypertension | +0.8339 | 1.4940 | ±2.9879 | +0.558 | 0.5767 |  |
| High cholesterol | -0.2086 | 1.3890 | ±2.7779 | -0.150 | 0.8806 |  |
| Kidney disease | -0.2488 | 1.8275 | ±3.6550 | -0.136 | 0.8917 |  |
| **Circulatory disease** | **-3.8445** | 1.6239 | ±3.2477 | **-2.368** | **0.0179** | * |
| **Nocturnal time > 180 (%)** | **+0.0824** | 0.0247 | ±0.0493 | **+3.345** | **8.24e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **749**, R² = **0.1414**, Adj R² = **0.1286**, F-statistic = **11.04** (p = **4.47e-19**), Residual SE = **17.429** on **737** df, AIC = **6419.0**, BIC = **6474.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.0541** | 5.7011 | ±11.4021 | **+13.165** | **1.40e-39** | *** |
| **Education: graduate level (vs college)** | **-4.7072** | 1.5183 | ±3.0365 | **-3.100** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.7062 | 1.7387 | ±3.4773 | -0.406 | 0.6846 |  |
| **Site: UCSD (vs UAB)** | **+3.7099** | 1.6761 | ±3.3522 | **+2.213** | **0.0269** | * |
| Site: UW (vs UAB) | +1.5441 | 1.5693 | ±3.1387 | +0.984 | 0.3252 |  |
| **Age (years)** | **-0.4751** | 0.0665 | ±0.1331 | **-7.140** | **9.31e-13** | *** |
| **BMI (kg/m2)** | **+0.3184** | 0.0895 | ±0.1789 | **+3.559** | **3.72e-04** | *** |
| Hypertension | +0.8372 | 1.4940 | ±2.9880 | +0.560 | 0.5752 |  |
| High cholesterol | -0.5037 | 1.3844 | ±2.7688 | -0.364 | 0.7160 |  |
| Kidney disease | -0.3066 | 1.8600 | ±3.7200 | -0.165 | 0.8691 |  |
| **Circulatory disease** | **-3.5844** | 1.6380 | ±3.2761 | **-2.188** | **0.0287** | * |
| **Any reading > 250 during wear (0/1)** | **+3.2730** | 1.3829 | ±2.7658 | **+2.367** | **0.0179** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **749**, R² = **0.1432**, Adj R² = **0.1304**, F-statistic = **11.20** (p = **2.19e-19**), Residual SE = **17.411** on **737** df, AIC = **6417.4**, BIC = **6472.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.0634** | 5.6952 | ±11.3904 | **+13.180** | **1.14e-39** | *** |
| **Education: graduate level (vs college)** | **-4.6169** | 1.5167 | ±3.0334 | **-3.044** | **0.0023** | ** |
| Education: high school or below (vs college) | -0.9181 | 1.7327 | ±3.4655 | -0.530 | 0.5962 |  |
| **Site: UCSD (vs UAB)** | **+3.7218** | 1.6709 | ±3.3418 | **+2.227** | **0.0259** | * |
| Site: UW (vs UAB) | +1.9426 | 1.5868 | ±3.1736 | +1.224 | 0.2209 |  |
| **Age (years)** | **-0.4444** | 0.0648 | ±0.1296 | **-6.859** | **6.92e-12** | *** |
| **BMI (kg/m2)** | **+0.2992** | 0.0900 | ±0.1800 | **+3.325** | **8.85e-04** | *** |
| Hypertension | +0.6485 | 1.4979 | ±2.9959 | +0.433 | 0.6651 |  |
| High cholesterol | -0.4174 | 1.3905 | ±2.7809 | -0.300 | 0.7641 |  |
| Kidney disease | -0.1559 | 1.8299 | ±3.6599 | -0.085 | 0.9321 |  |
| **Circulatory disease** | **-3.7362** | 1.6257 | ±3.2514 | **-2.298** | **0.0216** | * |
| **Time > 250 (%)** | **+0.1119** | 0.0481 | ±0.0963 | **+2.324** | **0.0201** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 749)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **749**, R² = **0.1435**, Adj R² = **0.1307**, F-statistic = **11.23** (p = **1.95e-19**), Residual SE = **17.408** on **737** df, AIC = **6417.2**, BIC = **6472.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.1619** | 5.7007 | ±11.4015 | **+13.185** | **1.08e-39** | *** |
| **Education: graduate level (vs college)** | **-4.6175** | 1.5162 | ±3.0323 | **-3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | -0.9250 | 1.7319 | ±3.4639 | -0.534 | 0.5933 |  |
| **Site: UCSD (vs UAB)** | **+3.7308** | 1.6710 | ±3.3419 | **+2.233** | **0.0256** | * |
| Site: UW (vs UAB) | +1.9390 | 1.5863 | ±3.1727 | +1.222 | 0.2216 |  |
| **Age (years)** | **-0.4457** | 0.0648 | ±0.1296 | **-6.877** | **6.13e-12** | *** |
| **BMI (kg/m2)** | **+0.2985** | 0.0902 | ±0.1804 | **+3.310** | **9.34e-04** | *** |
| Hypertension | +0.6559 | 1.4971 | ±2.9942 | +0.438 | 0.6613 |  |
| High cholesterol | -0.4126 | 1.3905 | ±2.7810 | -0.297 | 0.7667 |  |
| Kidney disease | -0.1873 | 1.8305 | ±3.6610 | -0.102 | 0.9185 |  |
| **Circulatory disease** | **-3.7531** | 1.6259 | ±3.2518 | **-2.308** | **0.0210** | * |
| **Avg. daily time > 250 (%)** | **+0.1154** | 0.0493 | ±0.0985 | **+2.343** | **0.0191** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
