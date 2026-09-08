# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 551; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **551**, R² = **0.0793**, Adj R² = **0.0623**, F-statistic = **4.65** (p = **2.21e-06**), Residual SE = **3.436** on **540** df, AIC = **2934.6**, BIC = **2982.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3152** | 1.3070 | ±2.6141 | **+20.899** | **5.52e-97** | *** |
| **Education: graduate level (vs college)** | **+1.0237** | 0.3168 | ±0.6335 | **+3.232** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.4303** | 0.5107 | ±1.0214 | **-2.801** | **0.0051** | ** |
| **Site: UCSD (vs UAB)** | **-0.7323** | 0.3640 | ±0.7281 | **-2.012** | **0.0443** | * |
| Site: UW (vs UAB) | -0.3665 | 0.3713 | ±0.7425 | -0.987 | 0.3235 |  |
| **Age (years)** | **-0.0415** | 0.0163 | ±0.0325 | **-2.554** | **0.0106** | * |
| BMI (kg/m2) | +0.0170 | 0.0205 | ±0.0411 | +0.825 | 0.4092 |  |
| **Hypertension** | **-0.8326** | 0.3455 | ±0.6911 | **-2.409** | **0.0160** | * |
| High cholesterol | +0.4290 | 0.3394 | ±0.6788 | +1.264 | 0.2063 |  |
| Kidney disease | +0.4971 | 0.4095 | ±0.8190 | +1.214 | 0.2248 |  |
| Circulatory disease | +0.3591 | 0.3419 | ±0.6839 | +1.050 | 0.2937 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **551**, R² = **0.0812**, Adj R² = **0.0625**, F-statistic = **4.33** (p = **3.17e-06**), Residual SE = **3.435** on **539** df, AIC = **2935.5**, BIC = **2987.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.1447** | 1.5897 | ±3.1794 | **+17.705** | **3.86e-70** | *** |
| **Education: graduate level (vs college)** | **+1.0021** | 0.3184 | ±0.6369 | **+3.147** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.3824** | 0.5174 | ±1.0349 | **-2.672** | **0.0075** | ** |
| **Site: UCSD (vs UAB)** | **-0.7561** | 0.3669 | ±0.7338 | **-2.061** | **0.0393** | * |
| Site: UW (vs UAB) | -0.3966 | 0.3734 | ±0.7468 | -1.062 | 0.2882 |  |
| **Age (years)** | **-0.0426** | 0.0164 | ±0.0328 | **-2.599** | **0.0094** | ** |
| BMI (kg/m2) | +0.0196 | 0.0207 | ±0.0413 | +0.951 | 0.3415 |  |
| **Hypertension** | **-0.8277** | 0.3460 | ±0.6920 | **-2.392** | **0.0168** | * |
| High cholesterol | +0.4271 | 0.3394 | ±0.6787 | +1.259 | 0.2082 |  |
| Kidney disease | +0.4881 | 0.4093 | ±0.8187 | +1.192 | 0.2331 |  |
| Circulatory disease | +0.3710 | 0.3415 | ±0.6830 | +1.086 | 0.2773 |  |
| HbA1c (%) | -0.1165 | 0.1035 | ±0.2070 | -1.126 | 0.2603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **551**, R² = **0.0823**, Adj R² = **0.0636**, F-statistic = **4.39** (p = **2.46e-06**), Residual SE = **3.433** on **539** df, AIC = **2934.8**, BIC = **2986.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.1795** | 1.5020 | ±3.0039 | **+18.762** | **1.55e-78** | *** |
| **Education: graduate level (vs college)** | **+1.0034** | 0.3177 | ±0.6355 | **+3.158** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.3784** | 0.5164 | ±1.0328 | **-2.669** | **0.0076** | ** |
| **Site: UCSD (vs UAB)** | **-0.7729** | 0.3686 | ±0.7372 | **-2.097** | **0.0360** | * |
| Site: UW (vs UAB) | -0.4019 | 0.3733 | ±0.7466 | -1.077 | 0.2816 |  |
| **Age (years)** | **-0.0430** | 0.0164 | ±0.0328 | **-2.621** | **0.0088** | ** |
| BMI (kg/m2) | +0.0193 | 0.0207 | ±0.0414 | +0.932 | 0.3514 |  |
| **Hypertension** | **-0.8371** | 0.3455 | ±0.6910 | **-2.423** | **0.0154** | * |
| High cholesterol | +0.4197 | 0.3385 | ±0.6770 | +1.240 | 0.2150 |  |
| Kidney disease | +0.5100 | 0.4119 | ±0.8239 | +1.238 | 0.2157 |  |
| Circulatory disease | +0.3844 | 0.3385 | ±0.6770 | +1.135 | 0.2562 |  |
| Mean glucose (mg/dL) | -0.0048 | 0.0036 | ±0.0072 | -1.331 | 0.1833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **551**, R² = **0.0823**, Adj R² = **0.0636**, F-statistic = **4.39** (p = **2.46e-06**), Residual SE = **3.433** on **539** df, AIC = **2934.8**, BIC = **2986.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.8467** | 1.8017 | ±3.6035 | **+16.010** | **1.08e-57** | *** |
| **Education: graduate level (vs college)** | **+1.0034** | 0.3177 | ±0.6355 | **+3.158** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.3784** | 0.5164 | ±1.0328 | **-2.669** | **0.0076** | ** |
| **Site: UCSD (vs UAB)** | **-0.7729** | 0.3686 | ±0.7372 | **-2.097** | **0.0360** | * |
| Site: UW (vs UAB) | -0.4019 | 0.3733 | ±0.7466 | -1.077 | 0.2816 |  |
| **Age (years)** | **-0.0430** | 0.0164 | ±0.0328 | **-2.621** | **0.0088** | ** |
| BMI (kg/m2) | +0.0193 | 0.0207 | ±0.0414 | +0.932 | 0.3514 |  |
| **Hypertension** | **-0.8371** | 0.3455 | ±0.6910 | **-2.423** | **0.0154** | * |
| High cholesterol | +0.4197 | 0.3385 | ±0.6770 | +1.240 | 0.2150 |  |
| Kidney disease | +0.5100 | 0.4119 | ±0.8239 | +1.238 | 0.2157 |  |
| Circulatory disease | +0.3844 | 0.3385 | ±0.6770 | +1.135 | 0.2562 |  |
| GMI (%) | -0.2016 | 0.1515 | ±0.3030 | -1.331 | 0.1833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **551**, R² = **0.0825**, Adj R² = **0.0637**, F-statistic = **4.40** (p = **2.36e-06**), Residual SE = **3.433** on **539** df, AIC = **2934.7**, BIC = **2986.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.1245** | 1.4701 | ±2.9403 | **+19.130** | **1.41e-81** | *** |
| **Education: graduate level (vs college)** | **+0.9955** | 0.3170 | ±0.6341 | **+3.140** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.3855** | 0.5151 | ±1.0302 | **-2.690** | **0.0072** | ** |
| **Site: UCSD (vs UAB)** | **-0.7775** | 0.3696 | ±0.7393 | **-2.103** | **0.0354** | * |
| Site: UW (vs UAB) | -0.3868 | 0.3722 | ±0.7444 | -1.039 | 0.2987 |  |
| **Age (years)** | **-0.0437** | 0.0165 | ±0.0330 | **-2.649** | **0.0081** | ** |
| BMI (kg/m2) | +0.0206 | 0.0208 | ±0.0417 | +0.989 | 0.3226 |  |
| **Hypertension** | **-0.8414** | 0.3454 | ±0.6908 | **-2.436** | **0.0149** | * |
| High cholesterol | +0.4178 | 0.3383 | ±0.6766 | +1.235 | 0.2168 |  |
| Kidney disease | +0.4994 | 0.4099 | ±0.8197 | +1.218 | 0.2231 |  |
| Circulatory disease | +0.3855 | 0.3397 | ±0.6794 | +1.135 | 0.2564 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0046 | 0.0034 | ±0.0068 | -1.372 | 0.1701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **551**, R² = **0.0863**, Adj R² = **0.0677**, F-statistic = **4.63** (p = **9.26e-07**), Residual SE = **3.426** on **539** df, AIC = **2932.4**, BIC = **2984.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.3689** | 1.4065 | ±2.8130 | **+20.170** | **1.81e-90** | *** |
| **Education: graduate level (vs college)** | **+0.9887** | 0.3188 | ±0.6375 | **+3.101** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **-1.3502** | 0.5099 | ±1.0198 | **-2.648** | **0.0081** | ** |
| **Site: UCSD (vs UAB)** | **-0.7778** | 0.3658 | ±0.7317 | **-2.126** | **0.0335** | * |
| Site: UW (vs UAB) | -0.4553 | 0.3777 | ±0.7554 | -1.205 | 0.2281 |  |
| **Age (years)** | **-0.0428** | 0.0163 | ±0.0327 | **-2.622** | **0.0088** | ** |
| BMI (kg/m2) | +0.0193 | 0.0207 | ±0.0415 | +0.928 | 0.3534 |  |
| **Hypertension** | **-0.8221** | 0.3449 | ±0.6898 | **-2.383** | **0.0171** | * |
| High cholesterol | +0.4097 | 0.3370 | ±0.6741 | +1.216 | 0.2241 |  |
| Kidney disease | +0.6195 | 0.4130 | ±0.8261 | +1.500 | 0.1336 |  |
| Circulatory disease | +0.3906 | 0.3378 | ±0.6756 | +1.156 | 0.2476 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0247** | 0.0118 | ±0.0236 | **-2.097** | **0.0360** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **551**, R² = **0.0850**, Adj R² = **0.0663**, F-statistic = **4.55** (p = **1.28e-06**), Residual SE = **3.428** on **539** df, AIC = **2933.2**, BIC = **2985.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.3117** | 1.4107 | ±2.8214 | **+20.069** | **1.37e-89** | *** |
| **Education: graduate level (vs college)** | **+0.9992** | 0.3190 | ±0.6381 | **+3.132** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.3451** | 0.5105 | ±1.0211 | **-2.635** | **0.0084** | ** |
| **Site: UCSD (vs UAB)** | **-0.7731** | 0.3656 | ±0.7313 | **-2.114** | **0.0345** | * |
| Site: UW (vs UAB) | -0.4371 | 0.3763 | ±0.7527 | -1.161 | 0.2455 |  |
| **Age (years)** | **-0.0423** | 0.0163 | ±0.0327 | **-2.591** | **0.0096** | ** |
| BMI (kg/m2) | +0.0172 | 0.0207 | ±0.0414 | +0.830 | 0.4064 |  |
| **Hypertension** | **-0.8319** | 0.3455 | ±0.6910 | **-2.408** | **0.0160** | * |
| High cholesterol | +0.4156 | 0.3379 | ±0.6758 | +1.230 | 0.2188 |  |
| Kidney disease | +0.6179 | 0.4155 | ±0.8309 | +1.487 | 0.1369 |  |
| Circulatory disease | +0.3796 | 0.3391 | ±0.6782 | +1.119 | 0.2630 |  |
| Avg. daily SD (mg/dL) | -0.0255 | 0.0139 | ±0.0278 | -1.834 | 0.0666 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **551**, R² = **0.0806**, Adj R² = **0.0618**, F-statistic = **4.29** (p = **3.72e-06**), Residual SE = **3.436** on **539** df, AIC = **2935.9**, BIC = **2987.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.8675** | 1.3731 | ±2.7462 | **+20.295** | **1.42e-91** | *** |
| **Education: graduate level (vs college)** | **+1.0171** | 0.3175 | ±0.6351 | **+3.203** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.4157** | 0.5100 | ±1.0199 | **-2.776** | **0.0055** | ** |
| **Site: UCSD (vs UAB)** | **-0.7369** | 0.3640 | ±0.7280 | **-2.025** | **0.0429** | * |
| Site: UW (vs UAB) | -0.3946 | 0.3760 | ±0.7519 | -1.050 | 0.2939 |  |
| **Age (years)** | **-0.0413** | 0.0164 | ±0.0327 | **-2.524** | **0.0116** | * |
| BMI (kg/m2) | +0.0167 | 0.0206 | ±0.0411 | +0.814 | 0.4156 |  |
| **Hypertension** | **-0.8198** | 0.3450 | ±0.6900 | **-2.376** | **0.0175** | * |
| High cholesterol | +0.4248 | 0.3392 | ±0.6785 | +1.252 | 0.2105 |  |
| Kidney disease | +0.5571 | 0.4084 | ±0.8169 | +1.364 | 0.1726 |  |
| Circulatory disease | +0.3596 | 0.3422 | ±0.6844 | +1.051 | 0.2933 |  |
| CV (%) | -0.0231 | 0.0234 | ±0.0469 | -0.985 | 0.3247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **551**, R² = **0.0821**, Adj R² = **0.0634**, F-statistic = **4.38** (p = **2.59e-06**), Residual SE = **3.434** on **539** df, AIC = **2935.0**, BIC = **2986.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.4869** | 1.4874 | ±2.9748 | **+17.807** | **6.19e-71** | *** |
| **Education: graduate level (vs college)** | **+1.0115** | 0.3176 | ±0.6352 | **+3.185** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.4151** | 0.5097 | ±1.0195 | **-2.776** | **0.0055** | ** |
| **Site: UCSD (vs UAB)** | **-0.7268** | 0.3628 | ±0.7257 | **-2.003** | **0.0452** | * |
| Site: UW (vs UAB) | -0.3965 | 0.3736 | ±0.7472 | -1.061 | 0.2886 |  |
| **Age (years)** | **-0.0414** | 0.0163 | ±0.0327 | **-2.531** | **0.0114** | * |
| BMI (kg/m2) | +0.0161 | 0.0205 | ±0.0411 | +0.785 | 0.4325 |  |
| **Hypertension** | **-0.8208** | 0.3447 | ±0.6893 | **-2.382** | **0.0172** | * |
| High cholesterol | +0.4350 | 0.3393 | ±0.6785 | +1.282 | 0.1998 |  |
| Kidney disease | +0.5698 | 0.4066 | ±0.8132 | +1.401 | 0.1611 |  |
| Circulatory disease | +0.3693 | 0.3425 | ±0.6850 | +1.078 | 0.2809 |  |
| Mean / SD ratio | +0.1930 | 0.1349 | ±0.2697 | +1.431 | 0.1525 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **551**, R² = **0.0799**, Adj R² = **0.0611**, F-statistic = **4.25** (p = **4.39e-06**), Residual SE = **3.438** on **539** df, AIC = **2936.3**, BIC = **2988.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.9753** | 1.4950 | ±2.9900 | **+18.044** | **8.87e-73** | *** |
| **Education: graduate level (vs college)** | **+1.0184** | 0.3186 | ±0.6372 | **+3.197** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.4219** | 0.5100 | ±1.0199 | **-2.788** | **0.0053** | ** |
| **Site: UCSD (vs UAB)** | **-0.7289** | 0.3640 | ±0.7280 | **-2.002** | **0.0452** | * |
| Site: UW (vs UAB) | -0.3749 | 0.3728 | ±0.7456 | -1.006 | 0.3146 |  |
| **Age (years)** | **-0.0413** | 0.0164 | ±0.0328 | **-2.520** | **0.0117** | * |
| BMI (kg/m2) | +0.0159 | 0.0206 | ±0.0412 | +0.773 | 0.4395 |  |
| **Hypertension** | **-0.8295** | 0.3456 | ±0.6912 | **-2.400** | **0.0164** | * |
| High cholesterol | +0.4300 | 0.3399 | ±0.6799 | +1.265 | 0.2059 |  |
| Kidney disease | +0.5268 | 0.4093 | ±0.8187 | +1.287 | 0.1981 |  |
| Circulatory disease | +0.3592 | 0.3434 | ±0.6868 | +1.046 | 0.2956 |  |
| Avg. daily mean/SD | +0.0697 | 0.1222 | ±0.2444 | +0.570 | 0.5683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **551**, R² = **0.0879**, Adj R² = **0.0692**, F-statistic = **4.72** (p = **6.32e-07**), Residual SE = **3.423** on **539** df, AIC = **2931.5**, BIC = **2983.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2584** | 1.5452 | ±3.0903 | **+18.935** | **5.83e-80** | *** |
| **Education: graduate level (vs college)** | **+0.9748** | 0.3213 | ±0.6426 | **+3.034** | **0.0024** | ** |
| **Education: high school or below (vs college)** | **-1.3752** | 0.5059 | ±1.0118 | **-2.718** | **0.0066** | ** |
| **Site: UCSD (vs UAB)** | **-0.7743** | 0.3639 | ±0.7278 | **-2.128** | **0.0334** | * |
| Site: UW (vs UAB) | -0.4932 | 0.3778 | ±0.7556 | -1.306 | 0.1917 |  |
| **Age (years)** | **-0.0461** | 0.0163 | ±0.0325 | **-2.833** | **0.0046** | ** |
| BMI (kg/m2) | +0.0162 | 0.0206 | ±0.0411 | +0.787 | 0.4314 |  |
| **Hypertension** | **-0.8300** | 0.3468 | ±0.6936 | **-2.393** | **0.0167** | * |
| High cholesterol | +0.4117 | 0.3402 | ±0.6803 | +1.210 | 0.2262 |  |
| Kidney disease | +0.5808 | 0.4218 | ±0.8436 | +1.377 | 0.1685 |  |
| Circulatory disease | +0.3736 | 0.3401 | ±0.6802 | +1.098 | 0.2720 |  |
| **MAG (mg/dL/h)** | **-0.0344** | 0.0160 | ±0.0319 | **-2.155** | **0.0312** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **551**, R² = **0.0841**, Adj R² = **0.0654**, F-statistic = **4.50** (p = **1.57e-06**), Residual SE = **3.430** on **539** df, AIC = **2933.7**, BIC = **2985.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5805** | 1.5039 | ±3.0079 | **+19.004** | **1.59e-80** | *** |
| **Education: graduate level (vs college)** | **+1.0002** | 0.3194 | ±0.6389 | **+3.131** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **-1.3513** | 0.5120 | ±1.0241 | **-2.639** | **0.0083** | ** |
| **Site: UCSD (vs UAB)** | **-0.7733** | 0.3656 | ±0.7312 | **-2.115** | **0.0344** | * |
| Site: UW (vs UAB) | -0.4315 | 0.3767 | ±0.7533 | -1.146 | 0.2520 |  |
| **Age (years)** | **-0.0434** | 0.0163 | ±0.0327 | **-2.657** | **0.0079** | ** |
| BMI (kg/m2) | +0.0162 | 0.0207 | ±0.0414 | +0.784 | 0.4330 |  |
| **Hypertension** | **-0.8444** | 0.3465 | ±0.6930 | **-2.437** | **0.0148** | * |
| High cholesterol | +0.4283 | 0.3395 | ±0.6789 | +1.262 | 0.2071 |  |
| Kidney disease | +0.6153 | 0.4166 | ±0.8332 | +1.477 | 0.1396 |  |
| Circulatory disease | +0.3846 | 0.3396 | ±0.6792 | +1.132 | 0.2575 |  |
| Avg. daily range (mg/dL) | -0.0070 | 0.0043 | ±0.0087 | -1.609 | 0.1077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **551**, R² = **0.0869**, Adj R² = **0.0683**, F-statistic = **4.66** (p = **8.03e-07**), Residual SE = **3.425** on **539** df, AIC = **2932.1**, BIC = **2983.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.9326** | 1.3558 | ±2.7117 | **+20.602** | **2.65e-94** | *** |
| **Education: graduate level (vs college)** | **+0.9629** | 0.3171 | ±0.6341 | **+3.037** | **0.0024** | ** |
| **Education: high school or below (vs college)** | **-1.4106** | 0.5067 | ±1.0134 | **-2.784** | **0.0054** | ** |
| **Site: UCSD (vs UAB)** | **-0.7631** | 0.3654 | ±0.7307 | **-2.089** | **0.0367** | * |
| Site: UW (vs UAB) | -0.4464 | 0.3780 | ±0.7559 | -1.181 | 0.2376 |  |
| **Age (years)** | **-0.0450** | 0.0164 | ±0.0329 | **-2.737** | **0.0062** | ** |
| BMI (kg/m2) | +0.0218 | 0.0206 | ±0.0413 | +1.056 | 0.2912 |  |
| **Hypertension** | **-0.7913** | 0.3450 | ±0.6901 | **-2.293** | **0.0218** | * |
| High cholesterol | +0.4082 | 0.3369 | ±0.6737 | +1.212 | 0.2256 |  |
| Kidney disease | +0.5471 | 0.4094 | ±0.8187 | +1.336 | 0.1814 |  |
| Circulatory disease | +0.4304 | 0.3408 | ±0.6816 | +1.263 | 0.2066 |  |
| **SD of daily means (mg/dL)** | **-0.0364** | 0.0167 | ±0.0334 | **-2.182** | **0.0291** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **551**, R² = **0.0831**, Adj R² = **0.0644**, F-statistic = **4.44** (p = **2.03e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.4**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.7568** | 1.3408 | ±2.6816 | **+19.956** | **1.33e-88** | *** |
| **Education: graduate level (vs college)** | **+1.0057** | 0.3179 | ±0.6358 | **+3.164** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.3684** | 0.5159 | ±1.0317 | **-2.653** | **0.0080** | ** |
| **Site: UCSD (vs UAB)** | **-0.7867** | 0.3703 | ±0.7406 | **-2.124** | **0.0336** | * |
| Site: UW (vs UAB) | -0.4080 | 0.3742 | ±0.7483 | -1.090 | 0.2756 |  |
| **Age (years)** | **-0.0426** | 0.0163 | ±0.0326 | **-2.611** | **0.0090** | ** |
| BMI (kg/m2) | +0.0203 | 0.0206 | ±0.0413 | +0.982 | 0.3263 |  |
| **Hypertension** | **-0.8438** | 0.3453 | ±0.6906 | **-2.444** | **0.0145** | * |
| High cholesterol | +0.4065 | 0.3377 | ±0.6753 | +1.204 | 0.2287 |  |
| Kidney disease | +0.5226 | 0.4117 | ±0.8234 | +1.269 | 0.2043 |  |
| Circulatory disease | +0.3871 | 0.3380 | ±0.6759 | +1.145 | 0.2521 |  |
| Time in range 70-180, pooled (%) | +0.0086 | 0.0059 | ±0.0118 | +1.468 | 0.1421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **551**, R² = **0.0829**, Adj R² = **0.0642**, F-statistic = **4.43** (p = **2.13e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.5**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.7656** | 1.3427 | ±2.6854 | **+19.935** | **2.04e-88** | *** |
| **Education: graduate level (vs college)** | **+1.0082** | 0.3179 | ±0.6358 | **+3.171** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.3674** | 0.5165 | ±1.0329 | **-2.648** | **0.0081** | ** |
| **Site: UCSD (vs UAB)** | **-0.7877** | 0.3708 | ±0.7415 | **-2.125** | **0.0336** | * |
| Site: UW (vs UAB) | -0.4076 | 0.3743 | ±0.7486 | -1.089 | 0.2762 |  |
| **Age (years)** | **-0.0425** | 0.0163 | ±0.0327 | **-2.604** | **0.0092** | ** |
| BMI (kg/m2) | +0.0203 | 0.0207 | ±0.0413 | +0.981 | 0.3264 |  |
| **Hypertension** | **-0.8444** | 0.3453 | ±0.6906 | **-2.445** | **0.0145** | * |
| High cholesterol | +0.4077 | 0.3377 | ±0.6754 | +1.207 | 0.2274 |  |
| Kidney disease | +0.5252 | 0.4118 | ±0.8236 | +1.276 | 0.2021 |  |
| Circulatory disease | +0.3863 | 0.3380 | ±0.6760 | +1.143 | 0.2530 |  |
| Avg. daily time in range 70-180 (%) | +0.0083 | 0.0058 | ±0.0117 | +1.424 | 0.1545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **551**, R² = **0.0794**, Adj R² = **0.0606**, F-statistic = **4.22** (p = **4.98e-06**), Residual SE = **3.439** on **539** df, AIC = **2936.6**, BIC = **2988.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3317** | 1.3143 | ±2.6287 | **+20.795** | **4.79e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0237** | 0.3173 | ±0.6346 | **+3.226** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.4310** | 0.5130 | ±1.0260 | **-2.789** | **0.0053** | ** |
| **Site: UCSD (vs UAB)** | **-0.7351** | 0.3668 | ±0.7335 | **-2.004** | **0.0450** | * |
| Site: UW (vs UAB) | -0.3689 | 0.3761 | ±0.7523 | -0.981 | 0.3266 |  |
| **Age (years)** | **-0.0416** | 0.0162 | ±0.0324 | **-2.568** | **0.0102** | * |
| BMI (kg/m2) | +0.0169 | 0.0206 | ±0.0411 | +0.823 | 0.4103 |  |
| **Hypertension** | **-0.8288** | 0.3470 | ±0.6940 | **-2.388** | **0.0169** | * |
| High cholesterol | +0.4264 | 0.3417 | ±0.6835 | +1.248 | 0.2122 |  |
| Kidney disease | +0.4978 | 0.4109 | ±0.8217 | +1.212 | 0.2257 |  |
| Circulatory disease | +0.3619 | 0.3426 | ±0.6852 | +1.056 | 0.2908 |  |
| Any reading < 54 during wear (0/1) | -0.0416 | 0.3693 | ±0.7385 | -0.113 | 0.9103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **551**, R² = **0.0795**, Adj R² = **0.0607**, F-statistic = **4.23** (p = **4.85e-06**), Residual SE = **3.438** on **539** df, AIC = **2936.5**, BIC = **2988.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3006** | 1.3089 | ±2.6179 | **+20.857** | **1.32e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0268** | 0.3171 | ±0.6342 | **+3.238** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.4254** | 0.5123 | ±1.0245 | **-2.783** | **0.0054** | ** |
| **Site: UCSD (vs UAB)** | **-0.7235** | 0.3637 | ±0.7273 | **-1.989** | **0.0467** | * |
| Site: UW (vs UAB) | -0.3554 | 0.3750 | ±0.7500 | -0.948 | 0.3433 |  |
| **Age (years)** | **-0.0416** | 0.0163 | ±0.0325 | **-2.556** | **0.0106** | * |
| BMI (kg/m2) | +0.0170 | 0.0206 | ±0.0411 | +0.824 | 0.4100 |  |
| **Hypertension** | **-0.8429** | 0.3484 | ±0.6968 | **-2.420** | **0.0155** | * |
| High cholesterol | +0.4367 | 0.3411 | ±0.6822 | +1.280 | 0.2005 |  |
| Kidney disease | +0.4956 | 0.4101 | ±0.8201 | +1.209 | 0.2268 |  |
| Circulatory disease | +0.3657 | 0.3432 | ±0.6865 | +1.065 | 0.2867 |  |
| Time < 54 (%) | +0.1627 | 0.5136 | ±1.0273 | +0.317 | 0.7514 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **551**, R² = **0.0793**, Adj R² = **0.0606**, F-statistic = **4.22** (p = **5.00e-06**), Residual SE = **3.439** on **539** df, AIC = **2936.6**, BIC = **2988.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3149** | 1.3085 | ±2.6171 | **+20.874** | **9.18e-97** | *** |
| **Education: graduate level (vs college)** | **+1.0238** | 0.3170 | ±0.6339 | **+3.230** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.4302** | 0.5118 | ±1.0236 | **-2.794** | **0.0052** | ** |
| **Site: UCSD (vs UAB)** | **-0.7320** | 0.3644 | ±0.7288 | **-2.009** | **0.0446** | * |
| Site: UW (vs UAB) | -0.3662 | 0.3740 | ±0.7480 | -0.979 | 0.3275 |  |
| **Age (years)** | **-0.0415** | 0.0163 | ±0.0325 | **-2.551** | **0.0107** | * |
| BMI (kg/m2) | +0.0169 | 0.0206 | ±0.0411 | +0.825 | 0.4096 |  |
| **Hypertension** | **-0.8329** | 0.3472 | ±0.6944 | **-2.399** | **0.0165** | * |
| High cholesterol | +0.4292 | 0.3406 | ±0.6813 | +1.260 | 0.2076 |  |
| Kidney disease | +0.4970 | 0.4111 | ±0.8222 | +1.209 | 0.2267 |  |
| Circulatory disease | +0.3592 | 0.3427 | ±0.6854 | +1.048 | 0.2945 |  |
| Avg. daily time < 54 (%) | +0.0045 | 0.7071 | ±1.4143 | +0.006 | 0.9949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **551**, R² = **0.0795**, Adj R² = **0.0607**, F-statistic = **4.23** (p = **4.83e-06**), Residual SE = **3.438** on **539** df, AIC = **2936.5**, BIC = **2988.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3356** | 1.3118 | ±2.6235 | **+20.839** | **1.92e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0213** | 0.3174 | ±0.6348 | **+3.218** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.4308** | 0.5111 | ±1.0222 | **-2.799** | **0.0051** | ** |
| **Site: UCSD (vs UAB)** | **-0.7434** | 0.3637 | ±0.7274 | **-2.044** | **0.0410** | * |
| Site: UW (vs UAB) | -0.3767 | 0.3741 | ±0.7481 | -1.007 | 0.3139 |  |
| **Age (years)** | **-0.0414** | 0.0163 | ±0.0326 | **-2.541** | **0.0111** | * |
| BMI (kg/m2) | +0.0167 | 0.0206 | ±0.0412 | +0.813 | 0.4160 |  |
| **Hypertension** | **-0.8237** | 0.3480 | ±0.6961 | **-2.367** | **0.0179** | * |
| High cholesterol | +0.4207 | 0.3413 | ±0.6825 | +1.233 | 0.2177 |  |
| Kidney disease | +0.5020 | 0.4112 | ±0.8224 | +1.221 | 0.2221 |  |
| Circulatory disease | +0.3538 | 0.3433 | ±0.6867 | +1.031 | 0.3028 |  |
| Time 54-69, pooled (%) | -0.0483 | 0.1162 | ±0.2323 | -0.416 | 0.6774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **551**, R² = **0.0794**, Adj R² = **0.0607**, F-statistic = **4.23** (p = **4.87e-06**), Residual SE = **3.439** on **539** df, AIC = **2936.5**, BIC = **2988.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3268** | 1.3110 | ±2.6220 | **+20.845** | **1.71e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0208** | 0.3178 | ±0.6355 | **+3.213** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.4314** | 0.5113 | ±1.0226 | **-2.800** | **0.0051** | ** |
| **Site: UCSD (vs UAB)** | **-0.7418** | 0.3640 | ±0.7280 | **-2.038** | **0.0416** | * |
| Site: UW (vs UAB) | -0.3763 | 0.3740 | ±0.7481 | -1.006 | 0.3144 |  |
| **Age (years)** | **-0.0414** | 0.0163 | ±0.0326 | **-2.540** | **0.0111** | * |
| BMI (kg/m2) | +0.0169 | 0.0206 | ±0.0411 | +0.821 | 0.4119 |  |
| **Hypertension** | **-0.8247** | 0.3483 | ±0.6966 | **-2.368** | **0.0179** | * |
| High cholesterol | +0.4214 | 0.3415 | ±0.6829 | +1.234 | 0.2172 |  |
| Kidney disease | +0.5008 | 0.4106 | ±0.8213 | +1.219 | 0.2227 |  |
| Circulatory disease | +0.3537 | 0.3439 | ±0.6877 | +1.029 | 0.3036 |  |
| Avg. daily time 54-69 (%) | -0.0401 | 0.1107 | ±0.2214 | -0.362 | 0.7175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **551**, R² = **0.0794**, Adj R² = **0.0606**, F-statistic = **4.23** (p = **4.94e-06**), Residual SE = **3.439** on **539** df, AIC = **2936.6**, BIC = **2988.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3282** | 1.3117 | ±2.6234 | **+20.834** | **2.11e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0219** | 0.3174 | ±0.6349 | **+3.219** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.4313** | 0.5114 | ±1.0227 | **-2.799** | **0.0051** | ** |
| **Site: UCSD (vs UAB)** | **-0.7395** | 0.3636 | ±0.7272 | **-2.034** | **0.0420** | * |
| Site: UW (vs UAB) | -0.3736 | 0.3747 | ±0.7495 | -0.997 | 0.3188 |  |
| **Age (years)** | **-0.0414** | 0.0163 | ±0.0326 | **-2.545** | **0.0109** | * |
| BMI (kg/m2) | +0.0168 | 0.0206 | ±0.0412 | +0.818 | 0.4132 |  |
| **Hypertension** | **-0.8263** | 0.3485 | ±0.6970 | **-2.371** | **0.0177** | * |
| High cholesterol | +0.4234 | 0.3415 | ±0.6831 | +1.240 | 0.2151 |  |
| Kidney disease | +0.4999 | 0.4112 | ±0.8223 | +1.216 | 0.2241 |  |
| Circulatory disease | +0.3553 | 0.3436 | ±0.6871 | +1.034 | 0.3011 |  |
| Time < 70 (%) | -0.0254 | 0.0996 | ±0.1993 | -0.255 | 0.7989 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **551**, R² = **0.0794**, Adj R² = **0.0606**, F-statistic = **4.23** (p = **4.92e-06**), Residual SE = **3.439** on **539** df, AIC = **2936.6**, BIC = **2988.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.3241** | 1.3107 | ±2.6213 | **+20.847** | **1.61e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0215** | 0.3176 | ±0.6353 | **+3.216** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.4320** | 0.5115 | ±1.0229 | **-2.800** | **0.0051** | ** |
| **Site: UCSD (vs UAB)** | **-0.7396** | 0.3641 | ±0.7281 | **-2.032** | **0.0422** | * |
| Site: UW (vs UAB) | -0.3744 | 0.3742 | ±0.7485 | -1.001 | 0.3171 |  |
| **Age (years)** | **-0.0414** | 0.0163 | ±0.0326 | **-2.544** | **0.0109** | * |
| BMI (kg/m2) | +0.0169 | 0.0206 | ±0.0411 | +0.823 | 0.4104 |  |
| **Hypertension** | **-0.8262** | 0.3483 | ±0.6965 | **-2.372** | **0.0177** | * |
| High cholesterol | +0.4229 | 0.3415 | ±0.6830 | +1.238 | 0.2156 |  |
| Kidney disease | +0.5000 | 0.4107 | ±0.8214 | +1.217 | 0.2235 |  |
| Circulatory disease | +0.3549 | 0.3437 | ±0.6874 | +1.032 | 0.3019 |  |
| Avg. daily time < 70 (%) | -0.0248 | 0.0894 | ±0.1788 | -0.277 | 0.7817 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **551**, R² = **0.0829**, Adj R² = **0.0641**, F-statistic = **4.43** (p = **2.15e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.5**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.3632** | 1.4123 | ±2.8246 | **+18.667** | **9.17e-78** | *** |
| **Education: graduate level (vs college)** | **+0.9889** | 0.3177 | ±0.6354 | **+3.112** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **-1.3784** | 0.5156 | ±1.0313 | **-2.673** | **0.0075** | ** |
| **Site: UCSD (vs UAB)** | **-0.7745** | 0.3666 | ±0.7333 | **-2.112** | **0.0347** | * |
| Site: UW (vs UAB) | -0.4226 | 0.3742 | ±0.7485 | -1.129 | 0.2588 |  |
| **Age (years)** | **-0.0438** | 0.0164 | ±0.0329 | **-2.661** | **0.0078** | ** |
| BMI (kg/m2) | +0.0187 | 0.0207 | ±0.0415 | +0.904 | 0.3661 |  |
| **Hypertension** | **-0.8168** | 0.3464 | ±0.6928 | **-2.358** | **0.0184** | * |
| High cholesterol | +0.4168 | 0.3387 | ±0.6773 | +1.231 | 0.2184 |  |
| Kidney disease | +0.5216 | 0.4125 | ±0.8251 | +1.264 | 0.2061 |  |
| Circulatory disease | +0.3786 | 0.3392 | ±0.6783 | +1.116 | 0.2643 |  |
| Time 54-250, pooled (%) | +0.0118 | 0.0079 | ±0.0159 | +1.491 | 0.1360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **551**, R² = **0.0827**, Adj R² = **0.0640**, F-statistic = **4.42** (p = **2.21e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.6**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.3521** | 1.4228 | ±2.8456 | **+18.521** | **1.39e-76** | *** |
| **Education: graduate level (vs college)** | **+0.9896** | 0.3178 | ±0.6355 | **+3.114** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.3796** | 0.5154 | ±1.0308 | **-2.677** | **0.0074** | ** |
| **Site: UCSD (vs UAB)** | **-0.7745** | 0.3669 | ±0.7339 | **-2.111** | **0.0348** | * |
| Site: UW (vs UAB) | -0.4200 | 0.3742 | ±0.7483 | -1.122 | 0.2617 |  |
| **Age (years)** | **-0.0435** | 0.0164 | ±0.0328 | **-2.649** | **0.0081** | ** |
| BMI (kg/m2) | +0.0188 | 0.0207 | ±0.0415 | +0.904 | 0.3659 |  |
| **Hypertension** | **-0.8187** | 0.3463 | ±0.6925 | **-2.364** | **0.0181** | * |
| High cholesterol | +0.4171 | 0.3387 | ±0.6773 | +1.232 | 0.2181 |  |
| Kidney disease | +0.5246 | 0.4127 | ±0.8254 | +1.271 | 0.2037 |  |
| Circulatory disease | +0.3801 | 0.3392 | ±0.6784 | +1.121 | 0.2625 |  |
| Avg. daily time 54-250 (%) | +0.0117 | 0.0081 | ±0.0161 | +1.453 | 0.1462 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **551**, R² = **0.0804**, Adj R² = **0.0617**, F-statistic = **4.29** (p = **3.86e-06**), Residual SE = **3.437** on **539** df, AIC = **2936.0**, BIC = **2987.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.4398** | 1.3215 | ±2.6430 | **+20.764** | **9.08e-96** | *** |
| **Education: graduate level (vs college)** | **+1.0311** | 0.3185 | ±0.6371 | **+3.237** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.4076** | 0.5128 | ±1.0255 | **-2.745** | **0.0060** | ** |
| **Site: UCSD (vs UAB)** | **-0.7527** | 0.3686 | ±0.7372 | **-2.042** | **0.0412** | * |
| Site: UW (vs UAB) | -0.3653 | 0.3716 | ±0.7432 | -0.983 | 0.3256 |  |
| **Age (years)** | **-0.0410** | 0.0163 | ±0.0326 | **-2.520** | **0.0117** | * |
| BMI (kg/m2) | +0.0189 | 0.0206 | ±0.0412 | +0.917 | 0.3591 |  |
| **Hypertension** | **-0.8554** | 0.3473 | ±0.6946 | **-2.463** | **0.0138** | * |
| High cholesterol | +0.4175 | 0.3387 | ±0.6774 | +1.233 | 0.2177 |  |
| Kidney disease | +0.5034 | 0.4099 | ±0.8199 | +1.228 | 0.2194 |  |
| Circulatory disease | +0.3729 | 0.3413 | ±0.6827 | +1.092 | 0.2747 |  |
| Time 181-250, pooled (%) | -0.0081 | 0.0105 | ±0.0210 | -0.775 | 0.4382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **551**, R² = **0.0804**, Adj R² = **0.0616**, F-statistic = **4.28** (p = **3.90e-06**), Residual SE = **3.437** on **539** df, AIC = **2936.0**, BIC = **2987.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.4387** | 1.3228 | ±2.6456 | **+20.743** | **1.43e-95** | *** |
| **Education: graduate level (vs college)** | **+1.0324** | 0.3186 | ±0.6372 | **+3.240** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.4050** | 0.5136 | ±1.0272 | **-2.735** | **0.0062** | ** |
| **Site: UCSD (vs UAB)** | **-0.7542** | 0.3689 | ±0.7378 | **-2.045** | **0.0409** | * |
| Site: UW (vs UAB) | -0.3675 | 0.3719 | ±0.7438 | -0.988 | 0.3231 |  |
| **Age (years)** | **-0.0412** | 0.0163 | ±0.0326 | **-2.528** | **0.0115** | * |
| BMI (kg/m2) | +0.0189 | 0.0206 | ±0.0412 | +0.916 | 0.3597 |  |
| **Hypertension** | **-0.8544** | 0.3471 | ±0.6942 | **-2.461** | **0.0138** | * |
| High cholesterol | +0.4184 | 0.3387 | ±0.6775 | +1.235 | 0.2167 |  |
| Kidney disease | +0.5044 | 0.4100 | ±0.8199 | +1.230 | 0.2186 |  |
| Circulatory disease | +0.3716 | 0.3412 | ±0.6825 | +1.089 | 0.2762 |  |
| Avg. daily time 181-250 (%) | -0.0078 | 0.0103 | ±0.0206 | -0.757 | 0.4493 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **551**, R² = **0.0830**, Adj R² = **0.0643**, F-statistic = **4.43** (p = **2.08e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.4**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.6091** | 1.3360 | ±2.6720 | **+20.665** | **7.09e-95** | *** |
| **Education: graduate level (vs college)** | **+1.0066** | 0.3178 | ±0.6357 | **+3.167** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.3693** | 0.5160 | ±1.0320 | **-2.654** | **0.0080** | ** |
| **Site: UCSD (vs UAB)** | **-0.7832** | 0.3699 | ±0.7398 | **-2.117** | **0.0342** | * |
| Site: UW (vs UAB) | -0.4048 | 0.3738 | ±0.7477 | -1.083 | 0.2789 |  |
| **Age (years)** | **-0.0426** | 0.0163 | ±0.0326 | **-2.611** | **0.0090** | ** |
| BMI (kg/m2) | +0.0202 | 0.0207 | ±0.0413 | +0.980 | 0.3271 |  |
| **Hypertension** | **-0.8457** | 0.3453 | ±0.6906 | **-2.449** | **0.0143** | * |
| High cholesterol | +0.4088 | 0.3378 | ±0.6756 | +1.210 | 0.2262 |  |
| Kidney disease | +0.5211 | 0.4116 | ±0.8232 | +1.266 | 0.2055 |  |
| Circulatory disease | +0.3878 | 0.3380 | ±0.6761 | +1.147 | 0.2513 |  |
| Time > 180 (%) | -0.0085 | 0.0058 | ±0.0116 | -1.452 | 0.1465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **551**, R² = **0.0828**, Adj R² = **0.0641**, F-statistic = **4.42** (p = **2.18e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.5**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5902** | 1.3353 | ±2.6706 | **+20.662** | **7.56e-95** | *** |
| **Education: graduate level (vs college)** | **+1.0092** | 0.3178 | ±0.6357 | **+3.175** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.3680** | 0.5166 | ±1.0331 | **-2.648** | **0.0081** | ** |
| **Site: UCSD (vs UAB)** | **-0.7843** | 0.3703 | ±0.7406 | **-2.118** | **0.0342** | * |
| Site: UW (vs UAB) | -0.4042 | 0.3740 | ±0.7479 | -1.081 | 0.2798 |  |
| **Age (years)** | **-0.0425** | 0.0163 | ±0.0327 | **-2.605** | **0.0092** | ** |
| BMI (kg/m2) | +0.0202 | 0.0207 | ±0.0413 | +0.979 | 0.3278 |  |
| **Hypertension** | **-0.8463** | 0.3453 | ±0.6907 | **-2.451** | **0.0143** | * |
| High cholesterol | +0.4101 | 0.3379 | ±0.6757 | +1.214 | 0.2248 |  |
| Kidney disease | +0.5237 | 0.4117 | ±0.8233 | +1.272 | 0.2033 |  |
| Circulatory disease | +0.3872 | 0.3381 | ±0.6761 | +1.145 | 0.2521 |  |
| Avg. daily time > 180 (%) | -0.0082 | 0.0058 | ±0.0116 | -1.409 | 0.1588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **551**, R² = **0.0839**, Adj R² = **0.0652**, F-statistic = **4.48** (p = **1.69e-06**), Residual SE = **3.430** on **539** df, AIC = **2933.9**, BIC = **2985.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5610** | 1.3265 | ±2.6530 | **+20.777** | **7.01e-96** | *** |
| **Education: graduate level (vs college)** | **+0.9875** | 0.3167 | ±0.6334 | **+3.118** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.3746** | 0.5141 | ±1.0283 | **-2.674** | **0.0075** | ** |
| **Site: UCSD (vs UAB)** | **-0.7964** | 0.3706 | ±0.7411 | **-2.149** | **0.0316** | * |
| Site: UW (vs UAB) | -0.3956 | 0.3724 | ±0.7449 | -1.062 | 0.2882 |  |
| **Age (years)** | **-0.0436** | 0.0164 | ±0.0329 | **-2.654** | **0.0080** | ** |
| BMI (kg/m2) | +0.0222 | 0.0208 | ±0.0416 | +1.070 | 0.2847 |  |
| **Hypertension** | **-0.8468** | 0.3444 | ±0.6889 | **-2.459** | **0.0139** | * |
| High cholesterol | +0.3984 | 0.3380 | ±0.6759 | +1.179 | 0.2384 |  |
| Kidney disease | +0.5201 | 0.4096 | ±0.8192 | +1.270 | 0.2042 |  |
| Circulatory disease | +0.3930 | 0.3384 | ±0.6767 | +1.161 | 0.2455 |  |
| Nocturnal time > 180 (%) | -0.0083 | 0.0052 | ±0.0104 | -1.597 | 0.1103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **551**, R² = **0.0829**, Adj R² = **0.0642**, F-statistic = **4.43** (p = **2.14e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.5**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5454** | 1.3327 | ±2.6654 | **+20.669** | **6.58e-95** | *** |
| **Education: graduate level (vs college)** | **+0.9890** | 0.3177 | ±0.6354 | **+3.113** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **-1.3780** | 0.5157 | ±1.0314 | **-2.672** | **0.0075** | ** |
| **Site: UCSD (vs UAB)** | **-0.7739** | 0.3666 | ±0.7332 | **-2.111** | **0.0348** | * |
| Site: UW (vs UAB) | -0.4219 | 0.3741 | ±0.7483 | -1.128 | 0.2594 |  |
| **Age (years)** | **-0.0438** | 0.0164 | ±0.0329 | **-2.661** | **0.0078** | ** |
| BMI (kg/m2) | +0.0187 | 0.0207 | ±0.0415 | +0.904 | 0.3661 |  |
| **Hypertension** | **-0.8175** | 0.3463 | ±0.6927 | **-2.361** | **0.0182** | * |
| High cholesterol | +0.4173 | 0.3387 | ±0.6774 | +1.232 | 0.2179 |  |
| Kidney disease | +0.5215 | 0.4125 | ±0.8250 | +1.264 | 0.2061 |  |
| Circulatory disease | +0.3791 | 0.3391 | ±0.6783 | +1.118 | 0.2636 |  |
| Time > 250 (%) | -0.0119 | 0.0079 | ±0.0159 | -1.493 | 0.1354 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 551)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **551**, R² = **0.0827**, Adj R² = **0.0640**, F-statistic = **4.42** (p = **2.21e-06**), Residual SE = **3.432** on **539** df, AIC = **2934.6**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5235** | 1.3308 | ±2.6616 | **+20.682** | **5.00e-95** | *** |
| **Education: graduate level (vs college)** | **+0.9899** | 0.3177 | ±0.6355 | **+3.115** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **-1.3792** | 0.5155 | ±1.0309 | **-2.676** | **0.0075** | ** |
| **Site: UCSD (vs UAB)** | **-0.7738** | 0.3669 | ±0.7337 | **-2.109** | **0.0349** | * |
| Site: UW (vs UAB) | -0.4191 | 0.3741 | ±0.7481 | -1.120 | 0.2625 |  |
| **Age (years)** | **-0.0435** | 0.0164 | ±0.0328 | **-2.649** | **0.0081** | ** |
| BMI (kg/m2) | +0.0187 | 0.0207 | ±0.0415 | +0.904 | 0.3661 |  |
| **Hypertension** | **-0.8194** | 0.3462 | ±0.6924 | **-2.367** | **0.0179** | * |
| High cholesterol | +0.4178 | 0.3387 | ±0.6774 | +1.233 | 0.2174 |  |
| Kidney disease | +0.5243 | 0.4127 | ±0.8253 | +1.271 | 0.2039 |  |
| Circulatory disease | +0.3805 | 0.3392 | ±0.6784 | +1.122 | 0.2619 |  |
| Avg. daily time > 250 (%) | -0.0117 | 0.0081 | ±0.0161 | -1.452 | 0.1464 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 551; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0476**, LLR χ² = **36.34** (p = **7.36e-05**), AUC = **0.6503**, AIC = **749.4**, BIC = **796.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8006** | 0.8017 | ±1.6034 | **-2.246** | **0.0247** | 0.1652 | * |
| **Education: graduate level (vs college)** | **-0.6278** | 0.2068 | ±0.4136 | **-3.035** | **0.0024** | 0.5338 | ** |
| **Education: high school or below (vs college)** | **+0.5907** | 0.2530 | ±0.5060 | **+2.335** | **0.0196** | 1.8052 | * |
| **Site: UCSD (vs UAB)** | **+0.5022** | 0.2228 | ±0.4456 | **+2.254** | **0.0242** | 1.6524 | * |
| Site: UW (vs UAB) | +0.0039 | 0.2164 | ±0.4328 | +0.018 | 0.9855 | 1.0039 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0184 | **+2.829** | **0.0047** | 1.0264 | ** |
| BMI (kg/m2) | +0.0044 | 0.0130 | ±0.0260 | +0.342 | 0.7326 | 1.0044 |  |
| Hypertension | +0.3036 | 0.2049 | ±0.4098 | +1.482 | 0.1384 | 1.3547 |  |
| High cholesterol | -0.1615 | 0.1951 | ±0.3902 | -0.828 | 0.4077 | 0.8508 |  |
| Kidney disease | -0.3379 | 0.2285 | ±0.4570 | -1.479 | 0.1393 | 0.7133 |  |
| Circulatory disease | -0.1773 | 0.2242 | ±0.4484 | -0.791 | 0.4291 | 0.8376 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0499**, LLR χ² = **38.14** (p = **7.41e-05**), AUC = **0.6527**, AIC = **749.6**, BIC = **801.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4400** | 0.9383 | ±1.8766 | **-2.600** | **0.0093** | 0.0872 | ** |
| **Education: graduate level (vs college)** | **-0.6140** | 0.2077 | ±0.4154 | **-2.956** | **0.0031** | 0.5412 | ** |
| **Education: high school or below (vs college)** | **+0.5529** | 0.2545 | ±0.5089 | **+2.173** | **0.0298** | 1.7384 | * |
| **Site: UCSD (vs UAB)** | **+0.5204** | 0.2235 | ±0.4471 | **+2.328** | **0.0199** | 1.6827 | * |
| Site: UW (vs UAB) | +0.0263 | 0.2175 | ±0.4349 | +0.121 | 0.9036 | 1.0267 |  |
| **Age (years)** | **+0.0270** | 0.0093 | ±0.0186 | **+2.909** | **0.0036** | 1.0274 | ** |
| BMI (kg/m2) | +0.0024 | 0.0131 | ±0.0262 | +0.183 | 0.8544 | 1.0024 |  |
| Hypertension | +0.3003 | 0.2050 | ±0.4100 | +1.465 | 0.1430 | 1.3502 |  |
| High cholesterol | -0.1595 | 0.1954 | ±0.3908 | -0.816 | 0.4143 | 0.8526 |  |
| Kidney disease | -0.3320 | 0.2292 | ±0.4583 | -1.449 | 0.1474 | 0.7175 |  |
| Circulatory disease | -0.1871 | 0.2247 | ±0.4495 | -0.832 | 0.4052 | 0.8294 |  |
| HbA1c (%) | +0.0894 | 0.0673 | ±0.1345 | +1.329 | 0.1840 | 1.0935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0515**, LLR χ² = **39.33** (p = **4.66e-05**), AUC = **0.6538**, AIC = **748.4**, BIC = **800.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4923** | 0.9014 | ±1.8027 | **-2.765** | **0.0057** | 0.0827 | ** |
| **Education: graduate level (vs college)** | **-0.6159** | 0.2076 | ±0.4152 | **-2.967** | **0.0030** | 0.5401 | ** |
| **Education: high school or below (vs college)** | **+0.5494** | 0.2542 | ±0.5085 | **+2.161** | **0.0307** | 1.7322 | * |
| **Site: UCSD (vs UAB)** | **+0.5355** | 0.2241 | ±0.4482 | **+2.389** | **0.0169** | 1.7083 | * |
| Site: UW (vs UAB) | +0.0302 | 0.2175 | ±0.4350 | +0.139 | 0.8894 | 1.0307 |  |
| **Age (years)** | **+0.0273** | 0.0093 | ±0.0186 | **+2.943** | **0.0033** | 1.0277 | ** |
| BMI (kg/m2) | +0.0026 | 0.0131 | ±0.0261 | +0.202 | 0.8400 | 1.0026 |  |
| Hypertension | +0.3086 | 0.2053 | ±0.4106 | +1.503 | 0.1328 | 1.3615 |  |
| High cholesterol | -0.1540 | 0.1956 | ±0.3912 | -0.787 | 0.4310 | 0.8572 |  |
| Kidney disease | -0.3496 | 0.2296 | ±0.4591 | -1.523 | 0.1278 | 0.7050 |  |
| Circulatory disease | -0.2001 | 0.2255 | ±0.4509 | -0.888 | 0.3747 | 0.8186 |  |
| Mean glucose (mg/dL) | +0.0038 | 0.0022 | ±0.0045 | +1.712 | 0.0869 | 1.0038 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0515**, LLR χ² = **39.33** (p = **4.66e-05**), AUC = **0.6538**, AIC = **748.4**, BIC = **800.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0223** | 1.0770 | ±2.1539 | **-2.806** | **0.0050** | 0.0487 | ** |
| **Education: graduate level (vs college)** | **-0.6159** | 0.2076 | ±0.4152 | **-2.967** | **0.0030** | 0.5401 | ** |
| **Education: high school or below (vs college)** | **+0.5494** | 0.2542 | ±0.5085 | **+2.161** | **0.0307** | 1.7322 | * |
| **Site: UCSD (vs UAB)** | **+0.5355** | 0.2241 | ±0.4482 | **+2.389** | **0.0169** | 1.7083 | * |
| Site: UW (vs UAB) | +0.0302 | 0.2175 | ±0.4350 | +0.139 | 0.8894 | 1.0307 |  |
| **Age (years)** | **+0.0273** | 0.0093 | ±0.0186 | **+2.943** | **0.0033** | 1.0277 | ** |
| BMI (kg/m2) | +0.0026 | 0.0131 | ±0.0261 | +0.202 | 0.8400 | 1.0026 |  |
| Hypertension | +0.3086 | 0.2053 | ±0.4106 | +1.503 | 0.1328 | 1.3615 |  |
| High cholesterol | -0.1540 | 0.1956 | ±0.3912 | -0.787 | 0.4310 | 0.8572 |  |
| Kidney disease | -0.3496 | 0.2296 | ±0.4591 | -1.523 | 0.1278 | 0.7050 |  |
| Circulatory disease | -0.2001 | 0.2255 | ±0.4509 | -0.888 | 0.3747 | 0.8186 |  |
| GMI (%) | +0.1601 | 0.0935 | ±0.1870 | +1.712 | 0.0869 | 1.1736 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0511**, LLR χ² = **39.02** (p = **5.26e-05**), AUC = **0.6542**, AIC = **748.7**, BIC = **800.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.3983** | 0.8856 | ±1.7711 | **-2.708** | **0.0068** | 0.0909 | ** |
| **Education: graduate level (vs college)** | **-0.6110** | 0.2076 | ±0.4153 | **-2.943** | **0.0033** | 0.5428 | ** |
| **Education: high school or below (vs college)** | **+0.5581** | 0.2540 | ±0.5079 | **+2.198** | **0.0280** | 1.7474 | * |
| **Site: UCSD (vs UAB)** | **+0.5359** | 0.2242 | ±0.4484 | **+2.390** | **0.0168** | 1.7090 | * |
| Site: UW (vs UAB) | +0.0175 | 0.2170 | ±0.4341 | +0.081 | 0.9358 | 1.0176 |  |
| **Age (years)** | **+0.0278** | 0.0093 | ±0.0186 | **+2.982** | **0.0029** | 1.0282 | ** |
| BMI (kg/m2) | +0.0019 | 0.0131 | ±0.0262 | +0.143 | 0.8862 | 1.0019 |  |
| Hypertension | +0.3102 | 0.2053 | ±0.4107 | +1.511 | 0.1308 | 1.3637 |  |
| High cholesterol | -0.1537 | 0.1956 | ±0.3912 | -0.786 | 0.4321 | 0.8576 |  |
| Kidney disease | -0.3421 | 0.2293 | ±0.4587 | -1.492 | 0.1357 | 0.7102 |  |
| Circulatory disease | -0.1987 | 0.2255 | ±0.4509 | -0.881 | 0.3781 | 0.8198 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0034 | 0.0021 | ±0.0042 | +1.623 | 0.1046 | 1.0034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0523**, LLR χ² = **39.96** (p = **3.63e-05**), AUC = **0.6561**, AIC = **747.7**, BIC = **799.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4244** | 0.8746 | ±1.7491 | **-2.772** | **0.0056** | 0.0885 | ** |
| **Education: graduate level (vs college)** | **-0.6148** | 0.2079 | ±0.4157 | **-2.958** | **0.0031** | 0.5407 | ** |
| **Education: high school or below (vs college)** | **+0.5431** | 0.2542 | ±0.5085 | **+2.136** | **0.0327** | 1.7213 | * |
| **Site: UCSD (vs UAB)** | **+0.5312** | 0.2241 | ±0.4482 | **+2.370** | **0.0178** | 1.7010 | * |
| Site: UW (vs UAB) | +0.0546 | 0.2188 | ±0.4376 | +0.250 | 0.8028 | 1.0562 |  |
| **Age (years)** | **+0.0271** | 0.0093 | ±0.0186 | **+2.914** | **0.0036** | 1.0275 | ** |
| BMI (kg/m2) | +0.0032 | 0.0131 | ±0.0261 | +0.245 | 0.8062 | 1.0032 |  |
| Hypertension | +0.3019 | 0.2053 | ±0.4106 | +1.470 | 0.1414 | 1.3524 |  |
| High cholesterol | -0.1503 | 0.1960 | ±0.3919 | -0.767 | 0.4429 | 0.8604 |  |
| Kidney disease | -0.4102 | 0.2327 | ±0.4653 | -1.763 | 0.0779 | 0.6635 | . |
| Circulatory disease | -0.1984 | 0.2252 | ±0.4504 | -0.881 | 0.3784 | 0.8201 |  |
| Glucose SD, pooled (mg/dL) | +0.0142 | 0.0076 | ±0.0151 | +1.883 | 0.0597 | 1.0143 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0513**, LLR χ² = **39.21** (p = **4.88e-05**), AUC = **0.6558**, AIC = **748.5**, BIC = **800.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.3792** | 0.8780 | ±1.7560 | **-2.710** | **0.0067** | 0.0926 | ** |
| **Education: graduate level (vs college)** | **-0.6199** | 0.2077 | ±0.4154 | **-2.985** | **0.0028** | 0.5380 | ** |
| **Education: high school or below (vs college)** | **+0.5412** | 0.2546 | ±0.5091 | **+2.126** | **0.0335** | 1.7181 | * |
| **Site: UCSD (vs UAB)** | **+0.5284** | 0.2240 | ±0.4480 | **+2.359** | **0.0183** | 1.6961 | * |
| Site: UW (vs UAB) | +0.0432 | 0.2183 | ±0.4365 | +0.198 | 0.8431 | 1.0441 |  |
| **Age (years)** | **+0.0267** | 0.0093 | ±0.0185 | **+2.881** | **0.0040** | 1.0271 | ** |
| BMI (kg/m2) | +0.0044 | 0.0130 | ±0.0261 | +0.334 | 0.7382 | 1.0044 |  |
| Hypertension | +0.3067 | 0.2052 | ±0.4104 | +1.495 | 0.1350 | 1.3589 |  |
| High cholesterol | -0.1522 | 0.1957 | ±0.3914 | -0.778 | 0.4368 | 0.8588 |  |
| Kidney disease | -0.4075 | 0.2330 | ±0.4659 | -1.749 | 0.0803 | 0.6653 | . |
| Circulatory disease | -0.1913 | 0.2249 | ±0.4497 | -0.851 | 0.3948 | 0.8259 |  |
| Avg. daily SD (mg/dL) | +0.0145 | 0.0086 | ±0.0172 | +1.678 | 0.0934 | 1.0146 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0480**, LLR χ² = **36.64** (p = **1.33e-04**), AUC = **0.6507**, AIC = **751.1**, BIC = **802.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0177** | 0.8978 | ±1.7956 | **-2.247** | **0.0246** | 0.1330 | * |
| **Education: graduate level (vs college)** | **-0.6260** | 0.2069 | ±0.4139 | **-3.025** | **0.0025** | 0.5347 | ** |
| **Education: high school or below (vs college)** | **+0.5849** | 0.2532 | ±0.5064 | **+2.310** | **0.0209** | 1.7947 | * |
| **Site: UCSD (vs UAB)** | **+0.5042** | 0.2229 | ±0.4458 | **+2.262** | **0.0237** | 1.6557 | * |
| Site: UW (vs UAB) | +0.0152 | 0.2175 | ±0.4350 | +0.070 | 0.9444 | 1.0153 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0185 | **+2.823** | **0.0048** | 1.0264 | ** |
| BMI (kg/m2) | +0.0045 | 0.0130 | ±0.0260 | +0.346 | 0.7290 | 1.0045 |  |
| Hypertension | +0.2995 | 0.2050 | ±0.4100 | +1.461 | 0.1440 | 1.3492 |  |
| High cholesterol | -0.1598 | 0.1952 | ±0.3904 | -0.818 | 0.4131 | 0.8523 |  |
| Kidney disease | -0.3611 | 0.2325 | ±0.4650 | -1.553 | 0.1204 | 0.6969 |  |
| Circulatory disease | -0.1776 | 0.2242 | ±0.4483 | -0.792 | 0.4283 | 0.8373 |  |
| CV (%) | +0.0090 | 0.0165 | ±0.0330 | +0.543 | 0.5870 | 1.0090 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0480**, LLR χ² = **36.69** (p = **1.30e-04**), AUC = **0.6510**, AIC = **751.0**, BIC = **802.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5721 | 0.8903 | ±1.7807 | -1.766 | 0.0774 | 0.2076 | . |
| **Education: graduate level (vs college)** | **-0.6254** | 0.2070 | ±0.4140 | **-3.022** | **0.0025** | 0.5350 | ** |
| **Education: high school or below (vs college)** | **+0.5863** | 0.2531 | ±0.5061 | **+2.317** | **0.0205** | 1.7974 | * |
| **Site: UCSD (vs UAB)** | **+0.5011** | 0.2229 | ±0.4457 | **+2.248** | **0.0245** | 1.6505 | * |
| Site: UW (vs UAB) | +0.0130 | 0.2171 | ±0.4342 | +0.060 | 0.9523 | 1.0131 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0185 | **+2.828** | **0.0047** | 1.0265 | ** |
| BMI (kg/m2) | +0.0047 | 0.0130 | ±0.0260 | +0.359 | 0.7198 | 1.0047 |  |
| Hypertension | +0.3013 | 0.2049 | ±0.4099 | +1.470 | 0.1415 | 1.3516 |  |
| High cholesterol | -0.1631 | 0.1952 | ±0.3904 | -0.835 | 0.4035 | 0.8495 |  |
| Kidney disease | -0.3581 | 0.2310 | ±0.4621 | -1.550 | 0.1212 | 0.6990 |  |
| Circulatory disease | -0.1802 | 0.2243 | ±0.4485 | -0.803 | 0.4218 | 0.8351 |  |
| Mean / SD ratio | -0.0542 | 0.0920 | ±0.1841 | -0.589 | 0.5561 | 0.9473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0476**, LLR χ² = **36.34** (p = **1.48e-04**), AUC = **0.6505**, AIC = **751.4**, BIC = **803.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7850** | 0.8774 | ±1.7547 | **-2.035** | **0.0419** | 0.1678 | * |
| **Education: graduate level (vs college)** | **-0.6276** | 0.2069 | ±0.4137 | **-3.034** | **0.0024** | 0.5339 | ** |
| **Education: high school or below (vs college)** | **+0.5903** | 0.2532 | ±0.5063 | **+2.332** | **0.0197** | 1.8044 | * |
| **Site: UCSD (vs UAB)** | **+0.5021** | 0.2228 | ±0.4456 | **+2.253** | **0.0242** | 1.6522 | * |
| Site: UW (vs UAB) | +0.0044 | 0.2166 | ±0.4333 | +0.020 | 0.9839 | 1.0044 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0185 | **+2.828** | **0.0047** | 1.0264 | ** |
| BMI (kg/m2) | +0.0045 | 0.0130 | ±0.0260 | +0.344 | 0.7308 | 1.0045 |  |
| Hypertension | +0.3035 | 0.2049 | ±0.4098 | +1.481 | 0.1385 | 1.3546 |  |
| High cholesterol | -0.1615 | 0.1951 | ±0.3902 | -0.828 | 0.4077 | 0.8508 |  |
| Kidney disease | -0.3392 | 0.2306 | ±0.4612 | -1.471 | 0.1413 | 0.7123 |  |
| Circulatory disease | -0.1772 | 0.2242 | ±0.4484 | -0.791 | 0.4292 | 0.8376 |  |
| Avg. daily mean/SD | -0.0033 | 0.0742 | ±0.1484 | -0.044 | 0.9650 | 0.9968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0557**, LLR χ² = **42.50** (p = **1.33e-05**), AUC = **0.6588**, AIC = **745.2**, BIC = **796.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1806** | 0.9923 | ±1.9847 | **-3.205** | **0.0013** | 0.0416 | ** |
| **Education: graduate level (vs college)** | **-0.6057** | 0.2083 | ±0.4167 | **-2.908** | **0.0036** | 0.5457 | ** |
| **Education: high school or below (vs college)** | **+0.5498** | 0.2538 | ±0.5076 | **+2.166** | **0.0303** | 1.7329 | * |
| **Site: UCSD (vs UAB)** | **+0.5390** | 0.2250 | ±0.4499 | **+2.396** | **0.0166** | 1.7142 | * |
| Site: UW (vs UAB) | +0.0916 | 0.2205 | ±0.4410 | +0.415 | 0.6780 | 1.0959 |  |
| **Age (years)** | **+0.0297** | 0.0095 | ±0.0189 | **+3.146** | **0.0017** | 1.0302 | ** |
| BMI (kg/m2) | +0.0052 | 0.0130 | ±0.0260 | +0.399 | 0.6900 | 1.0052 |  |
| Hypertension | +0.3083 | 0.2058 | ±0.4115 | +1.498 | 0.1340 | 1.3611 |  |
| High cholesterol | -0.1501 | 0.1963 | ±0.3926 | -0.765 | 0.4445 | 0.8606 |  |
| Kidney disease | -0.3973 | 0.2317 | ±0.4635 | -1.714 | 0.0864 | 0.6721 | . |
| Circulatory disease | -0.1924 | 0.2256 | ±0.4511 | -0.853 | 0.3936 | 0.8250 |  |
| **MAG (mg/dL/h)** | **+0.0238** | 0.0098 | ±0.0195 | **+2.436** | **0.0148** | 1.0241 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0513**, LLR χ² = **39.21** (p = **4.88e-05**), AUC = **0.6559**, AIC = **748.5**, BIC = **800.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.5979** | 0.9381 | ±1.8762 | **-2.769** | **0.0056** | 0.0744 | ** |
| **Education: graduate level (vs college)** | **-0.6197** | 0.2077 | ±0.4154 | **-2.984** | **0.0028** | 0.5381 | ** |
| **Education: high school or below (vs college)** | **+0.5409** | 0.2545 | ±0.5090 | **+2.125** | **0.0336** | 1.7176 | * |
| **Site: UCSD (vs UAB)** | **+0.5305** | 0.2241 | ±0.4482 | **+2.367** | **0.0179** | 1.6997 | * |
| Site: UW (vs UAB) | +0.0428 | 0.2182 | ±0.4365 | +0.196 | 0.8445 | 1.0437 |  |
| **Age (years)** | **+0.0275** | 0.0093 | ±0.0186 | **+2.951** | **0.0032** | 1.0278 | ** |
| BMI (kg/m2) | +0.0050 | 0.0130 | ±0.0261 | +0.384 | 0.7011 | 1.0050 |  |
| Hypertension | +0.3144 | 0.2053 | ±0.4107 | +1.531 | 0.1257 | 1.3695 |  |
| High cholesterol | -0.1591 | 0.1956 | ±0.3913 | -0.813 | 0.4160 | 0.8529 |  |
| Kidney disease | -0.4119 | 0.2334 | ±0.4669 | -1.764 | 0.0777 | 0.6624 | . |
| Circulatory disease | -0.1951 | 0.2250 | ±0.4501 | -0.867 | 0.3859 | 0.8227 |  |
| Avg. daily range (mg/dL) | +0.0043 | 0.0026 | ±0.0051 | +1.680 | 0.0930 | 1.0043 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0543**, LLR χ² = **41.43** (p = **2.03e-05**), AUC = **0.6584**, AIC = **746.3**, BIC = **798.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2340** | 0.8330 | ±1.6659 | **-2.682** | **0.0073** | 0.1071 | ** |
| **Education: graduate level (vs college)** | **-0.5964** | 0.2083 | ±0.4166 | **-2.864** | **0.0042** | 0.5508 | ** |
| **Education: high school or below (vs college)** | **+0.5760** | 0.2537 | ±0.5074 | **+2.270** | **0.0232** | 1.7789 | * |
| **Site: UCSD (vs UAB)** | **+0.5260** | 0.2242 | ±0.4483 | **+2.347** | **0.0189** | 1.6922 | * |
| Site: UW (vs UAB) | +0.0584 | 0.2187 | ±0.4375 | +0.267 | 0.7894 | 1.0602 |  |
| **Age (years)** | **+0.0288** | 0.0094 | ±0.0188 | **+3.063** | **0.0022** | 1.0292 | ** |
| BMI (kg/m2) | +0.0012 | 0.0131 | ±0.0262 | +0.093 | 0.9257 | 1.0012 |  |
| Hypertension | +0.2823 | 0.2058 | ±0.4117 | +1.371 | 0.1702 | 1.3262 |  |
| High cholesterol | -0.1557 | 0.1964 | ±0.3928 | -0.793 | 0.4279 | 0.8558 |  |
| Kidney disease | -0.3750 | 0.2304 | ±0.4607 | -1.628 | 0.1036 | 0.6873 |  |
| Circulatory disease | -0.2257 | 0.2264 | ±0.4528 | -0.997 | 0.3187 | 0.7979 |  |
| **SD of daily means (mg/dL)** | **+0.0244** | 0.0111 | ±0.0221 | **+2.208** | **0.0273** | 1.0247 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0525**, LLR χ² = **40.08** (p = **3.47e-05**), AUC = **0.6539**, AIC = **747.6**, BIC = **799.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3731 | 0.8342 | ±1.6685 | -1.646 | 0.0998 | 0.2533 | . |
| **Education: graduate level (vs college)** | **-0.6200** | 0.2078 | ±0.4157 | **-2.983** | **0.0029** | 0.5379 | ** |
| **Education: high school or below (vs college)** | **+0.5420** | 0.2544 | ±0.5088 | **+2.130** | **0.0331** | 1.7194 | * |
| **Site: UCSD (vs UAB)** | **+0.5473** | 0.2247 | ±0.4494 | **+2.436** | **0.0149** | 1.7286 | * |
| Site: UW (vs UAB) | +0.0353 | 0.2179 | ±0.4358 | +0.162 | 0.8713 | 1.0359 |  |
| **Age (years)** | **+0.0272** | 0.0093 | ±0.0186 | **+2.924** | **0.0035** | 1.0275 | ** |
| BMI (kg/m2) | +0.0019 | 0.0131 | ±0.0262 | +0.145 | 0.8849 | 1.0019 |  |
| Hypertension | +0.3141 | 0.2056 | ±0.4111 | +1.528 | 0.1265 | 1.3691 |  |
| High cholesterol | -0.1434 | 0.1960 | ±0.3919 | -0.732 | 0.4643 | 0.8664 |  |
| Kidney disease | -0.3602 | 0.2298 | ±0.4596 | -1.567 | 0.1170 | 0.6975 |  |
| Circulatory disease | -0.2023 | 0.2255 | ±0.4510 | -0.897 | 0.3696 | 0.8168 |  |
| Time in range 70-180, pooled (%) | -0.0068 | 0.0035 | ±0.0071 | -1.923 | 0.0545 | 0.9932 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0525**, LLR χ² = **40.07** (p = **3.48e-05**), AUC = **0.6539**, AIC = **747.6**, BIC = **799.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3684 | 0.8350 | ±1.6699 | -1.639 | 0.1012 | 0.2545 |  |
| **Education: graduate level (vs college)** | **-0.6218** | 0.2078 | ±0.4157 | **-2.992** | **0.0028** | 0.5370 | ** |
| **Education: high school or below (vs college)** | **+0.5398** | 0.2545 | ±0.5090 | **+2.121** | **0.0339** | 1.7157 | * |
| **Site: UCSD (vs UAB)** | **+0.5494** | 0.2248 | ±0.4496 | **+2.444** | **0.0145** | 1.7322 | * |
| Site: UW (vs UAB) | +0.0357 | 0.2179 | ±0.4358 | +0.164 | 0.8697 | 1.0364 |  |
| **Age (years)** | **+0.0271** | 0.0093 | ±0.0186 | **+2.919** | **0.0035** | 1.0275 | ** |
| BMI (kg/m2) | +0.0018 | 0.0131 | ±0.0262 | +0.139 | 0.8896 | 1.0018 |  |
| Hypertension | +0.3147 | 0.2056 | ±0.4111 | +1.531 | 0.1258 | 1.3698 |  |
| High cholesterol | -0.1439 | 0.1959 | ±0.3919 | -0.734 | 0.4626 | 0.8660 |  |
| Kidney disease | -0.3631 | 0.2299 | ±0.4599 | -1.579 | 0.1143 | 0.6955 |  |
| Circulatory disease | -0.2023 | 0.2255 | ±0.4510 | -0.897 | 0.3696 | 0.8168 |  |
| Avg. daily time in range 70-180 (%) | -0.0067 | 0.0035 | ±0.0070 | -1.921 | 0.0547 | 0.9933 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0476**, LLR χ² = **36.34** (p = **1.49e-04**), AUC = **0.6501**, AIC = **751.4**, BIC = **803.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7988** | 0.8065 | ±1.6130 | **-2.230** | **0.0257** | 0.1655 | * |
| **Education: graduate level (vs college)** | **-0.6278** | 0.2068 | ±0.4136 | **-3.036** | **0.0024** | 0.5338 | ** |
| **Education: high school or below (vs college)** | **+0.5906** | 0.2530 | ±0.5060 | **+2.334** | **0.0196** | 1.8051 | * |
| **Site: UCSD (vs UAB)** | **+0.5019** | 0.2233 | ±0.4466 | **+2.248** | **0.0246** | 1.6519 | * |
| Site: UW (vs UAB) | +0.0036 | 0.2168 | ±0.4337 | +0.017 | 0.9866 | 1.0036 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0185 | **+2.822** | **0.0048** | 1.0264 | ** |
| BMI (kg/m2) | +0.0044 | 0.0130 | ±0.0260 | +0.342 | 0.7327 | 1.0044 |  |
| Hypertension | +0.3040 | 0.2058 | ±0.4116 | +1.477 | 0.1397 | 1.3552 |  |
| High cholesterol | -0.1618 | 0.1956 | ±0.3912 | -0.827 | 0.4081 | 0.8506 |  |
| Kidney disease | -0.3378 | 0.2285 | ±0.4571 | -1.478 | 0.1394 | 0.7133 |  |
| Circulatory disease | -0.1769 | 0.2247 | ±0.4493 | -0.788 | 0.4309 | 0.8378 |  |
| Any reading < 54 during wear (0/1) | -0.0046 | 0.2177 | ±0.4354 | -0.021 | 0.9833 | 0.9954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0478**, LLR χ² = **36.50** (p = **1.40e-04**), AUC = **0.6508**, AIC = **751.2**, BIC = **802.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8141** | 0.8026 | ±1.6051 | **-2.260** | **0.0238** | 0.1630 | * |
| **Education: graduate level (vs college)** | **-0.6252** | 0.2069 | ±0.4138 | **-3.021** | **0.0025** | 0.5352 | ** |
| **Education: high school or below (vs college)** | **+0.5952** | 0.2533 | ±0.5066 | **+2.350** | **0.0188** | 1.8133 | * |
| **Site: UCSD (vs UAB)** | **+0.5097** | 0.2236 | ±0.4473 | **+2.279** | **0.0226** | 1.6648 | * |
| Site: UW (vs UAB) | +0.0137 | 0.2178 | ±0.4356 | +0.063 | 0.9498 | 1.0138 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0185 | **+2.826** | **0.0047** | 1.0264 | ** |
| BMI (kg/m2) | +0.0044 | 0.0130 | ±0.0260 | +0.341 | 0.7333 | 1.0044 |  |
| Hypertension | +0.2946 | 0.2061 | ±0.4122 | +1.429 | 0.1529 | 1.3425 |  |
| High cholesterol | -0.1549 | 0.1958 | ±0.3917 | -0.791 | 0.4289 | 0.8565 |  |
| Kidney disease | -0.3393 | 0.2285 | ±0.4570 | -1.485 | 0.1375 | 0.7123 |  |
| Circulatory disease | -0.1714 | 0.2246 | ±0.4493 | -0.763 | 0.4455 | 0.8425 |  |
| Time < 54 (%) | +0.1418 | 0.3547 | ±0.7094 | +0.400 | 0.6892 | 1.1524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0480**, LLR χ² = **36.62** (p = **1.33e-04**), AUC = **0.6511**, AIC = **751.1**, BIC = **802.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8111** | 0.8022 | ±1.6045 | **-2.258** | **0.0240** | 0.1635 | * |
| **Education: graduate level (vs college)** | **-0.6255** | 0.2069 | ±0.4137 | **-3.024** | **0.0025** | 0.5350 | ** |
| **Education: high school or below (vs college)** | **+0.5960** | 0.2532 | ±0.5065 | **+2.353** | **0.0186** | 1.8148 | * |
| **Site: UCSD (vs UAB)** | **+0.5099** | 0.2233 | ±0.4466 | **+2.283** | **0.0224** | 1.6650 | * |
| Site: UW (vs UAB) | +0.0142 | 0.2173 | ±0.4346 | +0.065 | 0.9478 | 1.0143 |  |
| **Age (years)** | **+0.0261** | 0.0092 | ±0.0185 | **+2.828** | **0.0047** | 1.0264 | ** |
| BMI (kg/m2) | +0.0043 | 0.0130 | ±0.0260 | +0.333 | 0.7395 | 1.0043 |  |
| Hypertension | +0.2955 | 0.2055 | ±0.4109 | +1.438 | 0.1504 | 1.3438 |  |
| High cholesterol | -0.1542 | 0.1956 | ±0.3913 | -0.788 | 0.4307 | 0.8571 |  |
| Kidney disease | -0.3417 | 0.2286 | ±0.4573 | -1.494 | 0.1351 | 0.7106 |  |
| Circulatory disease | -0.1722 | 0.2244 | ±0.4488 | -0.767 | 0.4430 | 0.8418 |  |
| Avg. daily time < 54 (%) | +0.1385 | 0.2696 | ±0.5391 | +0.514 | 0.6075 | 1.1485 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0493**, LLR χ² = **37.65** (p = **8.98e-05**), AUC = **0.6517**, AIC = **750.1**, BIC = **801.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8528** | 0.8044 | ±1.6089 | **-2.303** | **0.0213** | 0.1568 | * |
| **Education: graduate level (vs college)** | **-0.6238** | 0.2070 | ±0.4140 | **-3.013** | **0.0026** | 0.5359 | ** |
| **Education: high school or below (vs college)** | **+0.5923** | 0.2533 | ±0.5066 | **+2.338** | **0.0194** | 1.8082 | * |
| **Site: UCSD (vs UAB)** | **+0.5280** | 0.2243 | ±0.4485 | **+2.354** | **0.0186** | 1.6955 | * |
| Site: UW (vs UAB) | +0.0278 | 0.2175 | ±0.4351 | +0.128 | 0.8982 | 1.0282 |  |
| **Age (years)** | **+0.0259** | 0.0092 | ±0.0185 | **+2.799** | **0.0051** | 1.0262 | ** |
| BMI (kg/m2) | +0.0049 | 0.0130 | ±0.0260 | +0.376 | 0.7073 | 1.0049 |  |
| Hypertension | +0.2832 | 0.2059 | ±0.4117 | +1.376 | 0.1689 | 1.3274 |  |
| High cholesterol | -0.1421 | 0.1962 | ±0.3924 | -0.724 | 0.4690 | 0.8676 |  |
| Kidney disease | -0.3514 | 0.2289 | ±0.4578 | -1.535 | 0.1247 | 0.7037 |  |
| Circulatory disease | -0.1654 | 0.2244 | ±0.4487 | -0.737 | 0.4610 | 0.8476 |  |
| Time 54-69, pooled (%) | +0.1165 | 0.1037 | ±0.2075 | +1.123 | 0.2616 | 1.1235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0500**, LLR χ² = **38.22** (p = **7.19e-05**), AUC = **0.6524**, AIC = **749.5**, BIC = **801.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8434** | 0.8041 | ±1.6082 | **-2.292** | **0.0219** | 0.1583 | * |
| **Education: graduate level (vs college)** | **-0.6208** | 0.2071 | ±0.4142 | **-2.998** | **0.0027** | 0.5375 | ** |
| **Education: high school or below (vs college)** | **+0.5943** | 0.2534 | ±0.5069 | **+2.345** | **0.0190** | 1.8118 | * |
| **Site: UCSD (vs UAB)** | **+0.5325** | 0.2243 | ±0.4486 | **+2.374** | **0.0176** | 1.7032 | * |
| Site: UW (vs UAB) | +0.0359 | 0.2179 | ±0.4357 | +0.165 | 0.8692 | 1.0365 |  |
| **Age (years)** | **+0.0257** | 0.0093 | ±0.0185 | **+2.778** | **0.0055** | 1.0260 | ** |
| BMI (kg/m2) | +0.0046 | 0.0130 | ±0.0260 | +0.357 | 0.7214 | 1.0047 |  |
| Hypertension | +0.2786 | 0.2059 | ±0.4119 | +1.353 | 0.1762 | 1.3212 |  |
| High cholesterol | -0.1372 | 0.1963 | ±0.3927 | -0.699 | 0.4847 | 0.8718 |  |
| Kidney disease | -0.3533 | 0.2290 | ±0.4581 | -1.542 | 0.1230 | 0.7024 |  |
| Circulatory disease | -0.1605 | 0.2245 | ±0.4490 | -0.715 | 0.4747 | 0.8517 |  |
| Avg. daily time 54-69 (%) | +0.1358 | 0.1029 | ±0.2057 | +1.321 | 0.1866 | 1.1455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0490**, LLR χ² = **37.46** (p = **9.66e-05**), AUC = **0.6511**, AIC = **750.2**, BIC = **802.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8496** | 0.8043 | ±1.6086 | **-2.300** | **0.0215** | 0.1573 | * |
| **Education: graduate level (vs college)** | **-0.6229** | 0.2070 | ±0.4140 | **-3.010** | **0.0026** | 0.5364 | ** |
| **Education: high school or below (vs college)** | **+0.5947** | 0.2533 | ±0.5066 | **+2.348** | **0.0189** | 1.8125 | * |
| **Site: UCSD (vs UAB)** | **+0.5270** | 0.2243 | ±0.4486 | **+2.349** | **0.0188** | 1.6938 | * |
| Site: UW (vs UAB) | +0.0288 | 0.2178 | ±0.4356 | +0.132 | 0.8949 | 1.0292 |  |
| **Age (years)** | **+0.0259** | 0.0092 | ±0.0185 | **+2.803** | **0.0051** | 1.0262 | ** |
| BMI (kg/m2) | +0.0048 | 0.0130 | ±0.0260 | +0.368 | 0.7130 | 1.0048 |  |
| Hypertension | +0.2821 | 0.2061 | ±0.4121 | +1.369 | 0.1710 | 1.3259 |  |
| High cholesterol | -0.1423 | 0.1962 | ±0.3925 | -0.725 | 0.4684 | 0.8674 |  |
| Kidney disease | -0.3492 | 0.2288 | ±0.4576 | -1.526 | 0.1269 | 0.7052 |  |
| Circulatory disease | -0.1642 | 0.2244 | ±0.4489 | -0.732 | 0.4644 | 0.8486 |  |
| Time < 70 (%) | +0.0902 | 0.0866 | ±0.1731 | +1.042 | 0.2975 | 1.0944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0496**, LLR χ² = **37.88** (p = **8.19e-05**), AUC = **0.6522**, AIC = **749.8**, BIC = **801.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8384** | 0.8038 | ±1.6076 | **-2.287** | **0.0222** | 0.1591 | * |
| **Education: graduate level (vs college)** | **-0.6210** | 0.2070 | ±0.4141 | **-3.000** | **0.0027** | 0.5374 | ** |
| **Education: high school or below (vs college)** | **+0.5966** | 0.2534 | ±0.5067 | **+2.355** | **0.0185** | 1.8159 | * |
| **Site: UCSD (vs UAB)** | **+0.5293** | 0.2242 | ±0.4484 | **+2.361** | **0.0182** | 1.6978 | * |
| Site: UW (vs UAB) | +0.0342 | 0.2179 | ±0.4359 | +0.157 | 0.8754 | 1.0348 |  |
| **Age (years)** | **+0.0258** | 0.0093 | ±0.0185 | **+2.789** | **0.0053** | 1.0261 | ** |
| BMI (kg/m2) | +0.0045 | 0.0130 | ±0.0260 | +0.349 | 0.7272 | 1.0045 |  |
| Hypertension | +0.2801 | 0.2059 | ±0.4118 | +1.360 | 0.1737 | 1.3233 |  |
| High cholesterol | -0.1393 | 0.1962 | ±0.3925 | -0.710 | 0.4778 | 0.8700 |  |
| Kidney disease | -0.3517 | 0.2290 | ±0.4580 | -1.536 | 0.1246 | 0.7035 |  |
| Circulatory disease | -0.1615 | 0.2245 | ±0.4491 | -0.719 | 0.4720 | 0.8509 |  |
| Avg. daily time < 70 (%) | +0.0979 | 0.0826 | ±0.1652 | +1.185 | 0.2359 | 1.1029 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0525**, LLR χ² = **40.08** (p = **3.47e-05**), AUC = **0.6538**, AIC = **747.6**, BIC = **799.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0186 | 0.9041 | ±1.8083 | -1.127 | 0.2599 | 0.3611 |  |
| **Education: graduate level (vs college)** | **-0.6030** | 0.2078 | ±0.4156 | **-2.902** | **0.0037** | 0.5472 | ** |
| **Education: high school or below (vs college)** | **+0.5485** | 0.2543 | ±0.5085 | **+2.157** | **0.0310** | 1.7307 | * |
| **Site: UCSD (vs UAB)** | **+0.5367** | 0.2240 | ±0.4479 | **+2.396** | **0.0166** | 1.7103 | * |
| Site: UW (vs UAB) | +0.0470 | 0.2182 | ±0.4364 | +0.215 | 0.8296 | 1.0481 |  |
| **Age (years)** | **+0.0280** | 0.0093 | ±0.0186 | **+3.005** | **0.0027** | 1.0284 | ** |
| BMI (kg/m2) | +0.0030 | 0.0130 | ±0.0261 | +0.231 | 0.8172 | 1.0030 |  |
| Hypertension | +0.2932 | 0.2054 | ±0.4108 | +1.427 | 0.1535 | 1.3407 |  |
| High cholesterol | -0.1515 | 0.1958 | ±0.3917 | -0.774 | 0.4391 | 0.8594 |  |
| Kidney disease | -0.3578 | 0.2298 | ±0.4596 | -1.557 | 0.1194 | 0.6992 |  |
| Circulatory disease | -0.1961 | 0.2255 | ±0.4509 | -0.870 | 0.3844 | 0.8219 |  |
| Time 54-250, pooled (%) | -0.0098 | 0.0052 | ±0.0103 | -1.894 | 0.0582 | 0.9903 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0522**, LLR χ² = **39.88** (p = **3.75e-05**), AUC = **0.6541**, AIC = **747.8**, BIC = **799.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0175 | 0.9089 | ±1.8179 | -1.119 | 0.2630 | 0.3615 |  |
| **Education: graduate level (vs college)** | **-0.6039** | 0.2078 | ±0.4156 | **-2.906** | **0.0037** | 0.5467 | ** |
| **Education: high school or below (vs college)** | **+0.5496** | 0.2542 | ±0.5084 | **+2.162** | **0.0306** | 1.7326 | * |
| **Site: UCSD (vs UAB)** | **+0.5364** | 0.2240 | ±0.4479 | **+2.395** | **0.0166** | 1.7098 | * |
| Site: UW (vs UAB) | +0.0445 | 0.2181 | ±0.4362 | +0.204 | 0.8385 | 1.0455 |  |
| **Age (years)** | **+0.0278** | 0.0093 | ±0.0186 | **+2.985** | **0.0028** | 1.0282 | ** |
| BMI (kg/m2) | +0.0030 | 0.0130 | ±0.0261 | +0.231 | 0.8174 | 1.0030 |  |
| Hypertension | +0.2947 | 0.2054 | ±0.4108 | +1.435 | 0.1514 | 1.3427 |  |
| High cholesterol | -0.1521 | 0.1958 | ±0.3916 | -0.777 | 0.4373 | 0.8589 |  |
| Kidney disease | -0.3601 | 0.2299 | ±0.4597 | -1.567 | 0.1172 | 0.6976 |  |
| Circulatory disease | -0.1971 | 0.2255 | ±0.4510 | -0.874 | 0.3820 | 0.8211 |  |
| Avg. daily time 54-250 (%) | -0.0096 | 0.0052 | ±0.0104 | -1.844 | 0.0652 | 0.9905 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0487**, LLR χ² = **37.20** (p = **1.07e-04**), AUC = **0.6511**, AIC = **750.5**, BIC = **802.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8943** | 0.8097 | ±1.6194 | **-2.340** | **0.0193** | 0.1504 | * |
| **Education: graduate level (vs college)** | **-0.6353** | 0.2074 | ±0.4147 | **-3.064** | **0.0022** | 0.5298 | ** |
| **Education: high school or below (vs college)** | **+0.5752** | 0.2536 | ±0.5071 | **+2.268** | **0.0233** | 1.7774 | * |
| **Site: UCSD (vs UAB)** | **+0.5175** | 0.2236 | ±0.4472 | **+2.314** | **0.0206** | 1.6779 | * |
| Site: UW (vs UAB) | +0.0031 | 0.2167 | ±0.4334 | +0.015 | 0.9884 | 1.0031 |  |
| **Age (years)** | **+0.0259** | 0.0092 | ±0.0185 | **+2.798** | **0.0051** | 1.0262 | ** |
| BMI (kg/m2) | +0.0031 | 0.0131 | ±0.0261 | +0.241 | 0.8097 | 1.0032 |  |
| Hypertension | +0.3198 | 0.2058 | ±0.4116 | +1.554 | 0.1202 | 1.3768 |  |
| High cholesterol | -0.1533 | 0.1954 | ±0.3908 | -0.785 | 0.4327 | 0.8579 |  |
| Kidney disease | -0.3440 | 0.2288 | ±0.4577 | -1.503 | 0.1328 | 0.7089 |  |
| Circulatory disease | -0.1877 | 0.2247 | ±0.4493 | -0.835 | 0.4035 | 0.8289 |  |
| Time 181-250, pooled (%) | +0.0057 | 0.0061 | ±0.0123 | +0.926 | 0.3542 | 1.0057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0489**, LLR χ² = **37.33** (p = **1.01e-04**), AUC = **0.6511**, AIC = **750.4**, BIC = **802.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9033** | 0.8103 | ±1.6206 | **-2.349** | **0.0188** | 0.1491 | * |
| **Education: graduate level (vs college)** | **-0.6371** | 0.2075 | ±0.4149 | **-3.071** | **0.0021** | 0.5288 | ** |
| **Education: high school or below (vs college)** | **+0.5716** | 0.2537 | ±0.5074 | **+2.253** | **0.0243** | 1.7711 | * |
| **Site: UCSD (vs UAB)** | **+0.5203** | 0.2238 | ±0.4475 | **+2.325** | **0.0201** | 1.6825 | * |
| Site: UW (vs UAB) | +0.0047 | 0.2167 | ±0.4335 | +0.022 | 0.9827 | 1.0047 |  |
| **Age (years)** | **+0.0259** | 0.0092 | ±0.0185 | **+2.806** | **0.0050** | 1.0263 | ** |
| BMI (kg/m2) | +0.0030 | 0.0131 | ±0.0262 | +0.232 | 0.8168 | 1.0030 |  |
| Hypertension | +0.3204 | 0.2057 | ±0.4115 | +1.557 | 0.1194 | 1.3777 |  |
| High cholesterol | -0.1531 | 0.1954 | ±0.3908 | -0.783 | 0.4334 | 0.8580 |  |
| Kidney disease | -0.3454 | 0.2289 | ±0.4578 | -1.509 | 0.1313 | 0.7079 |  |
| Circulatory disease | -0.1876 | 0.2246 | ±0.4492 | -0.835 | 0.4035 | 0.8289 |  |
| Avg. daily time 181-250 (%) | +0.0060 | 0.0060 | ±0.0120 | +0.995 | 0.3196 | 1.0060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0522**, LLR χ² = **39.86** (p = **3.78e-05**), AUC = **0.6535**, AIC = **747.8**, BIC = **799.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0401** | 0.8160 | ±1.6321 | **-2.500** | **0.0124** | 0.1300 | * |
| **Education: graduate level (vs college)** | **-0.6207** | 0.2078 | ±0.4156 | **-2.987** | **0.0028** | 0.5376 | ** |
| **Education: high school or below (vs college)** | **+0.5435** | 0.2544 | ±0.5087 | **+2.136** | **0.0326** | 1.7219 | * |
| **Site: UCSD (vs UAB)** | **+0.5437** | 0.2245 | ±0.4490 | **+2.422** | **0.0154** | 1.7224 | * |
| Site: UW (vs UAB) | +0.0322 | 0.2177 | ±0.4355 | +0.148 | 0.8824 | 1.0327 |  |
| **Age (years)** | **+0.0271** | 0.0093 | ±0.0186 | **+2.923** | **0.0035** | 1.0275 | ** |
| BMI (kg/m2) | +0.0020 | 0.0131 | ±0.0262 | +0.150 | 0.8807 | 1.0020 |  |
| Hypertension | +0.3153 | 0.2055 | ±0.4111 | +1.534 | 0.1251 | 1.3707 |  |
| High cholesterol | -0.1455 | 0.1959 | ±0.3917 | -0.743 | 0.4575 | 0.8646 |  |
| Kidney disease | -0.3586 | 0.2297 | ±0.4595 | -1.561 | 0.1185 | 0.6986 |  |
| Circulatory disease | -0.2025 | 0.2255 | ±0.4510 | -0.898 | 0.3692 | 0.8167 |  |
| Time > 180 (%) | +0.0065 | 0.0035 | ±0.0070 | +1.866 | 0.0621 | 1.0066 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0521**, LLR χ² = **39.81** (p = **3.85e-05**), AUC = **0.6533**, AIC = **747.9**, BIC = **799.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0300** | 0.8153 | ±1.6307 | **-2.490** | **0.0128** | 0.1313 | * |
| **Education: graduate level (vs college)** | **-0.6225** | 0.2078 | ±0.4155 | **-2.996** | **0.0027** | 0.5366 | ** |
| **Education: high school or below (vs college)** | **+0.5414** | 0.2545 | ±0.5090 | **+2.128** | **0.0334** | 1.7185 | * |
| **Site: UCSD (vs UAB)** | **+0.5454** | 0.2246 | ±0.4492 | **+2.428** | **0.0152** | 1.7253 | * |
| Site: UW (vs UAB) | +0.0322 | 0.2177 | ±0.4355 | +0.148 | 0.8823 | 1.0328 |  |
| **Age (years)** | **+0.0271** | 0.0093 | ±0.0186 | **+2.917** | **0.0035** | 1.0274 | ** |
| BMI (kg/m2) | +0.0019 | 0.0131 | ±0.0262 | +0.147 | 0.8831 | 1.0019 |  |
| Hypertension | +0.3158 | 0.2055 | ±0.4111 | +1.537 | 0.1244 | 1.3714 |  |
| High cholesterol | -0.1463 | 0.1958 | ±0.3917 | -0.747 | 0.4551 | 0.8639 |  |
| Kidney disease | -0.3613 | 0.2299 | ±0.4597 | -1.572 | 0.1160 | 0.6968 |  |
| Circulatory disease | -0.2024 | 0.2255 | ±0.4509 | -0.898 | 0.3693 | 0.8168 |  |
| Avg. daily time > 180 (%) | +0.0065 | 0.0035 | ±0.0070 | +1.853 | 0.0638 | 1.0065 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0526**, LLR χ² = **40.16** (p = **3.36e-05**), AUC = **0.6543**, AIC = **747.5**, BIC = **799.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9921** | 0.8121 | ±1.6242 | **-2.453** | **0.0142** | 0.1364 | * |
| **Education: graduate level (vs college)** | **-0.6077** | 0.2079 | ±0.4159 | **-2.922** | **0.0035** | 0.5446 | ** |
| **Education: high school or below (vs college)** | **+0.5507** | 0.2542 | ±0.5083 | **+2.167** | **0.0302** | 1.7345 | * |
| **Site: UCSD (vs UAB)** | **+0.5505** | 0.2249 | ±0.4497 | **+2.448** | **0.0143** | 1.7342 | * |
| Site: UW (vs UAB) | +0.0241 | 0.2175 | ±0.4350 | +0.111 | 0.9117 | 1.0244 |  |
| **Age (years)** | **+0.0278** | 0.0093 | ±0.0186 | **+2.984** | **0.0028** | 1.0282 | ** |
| BMI (kg/m2) | +0.0007 | 0.0132 | ±0.0263 | +0.054 | 0.9573 | 1.0007 |  |
| Hypertension | +0.3143 | 0.2056 | ±0.4112 | +1.529 | 0.1263 | 1.3694 |  |
| High cholesterol | -0.1391 | 0.1961 | ±0.3922 | -0.710 | 0.4779 | 0.8701 |  |
| Kidney disease | -0.3572 | 0.2297 | ±0.4594 | -1.555 | 0.1199 | 0.6997 |  |
| Circulatory disease | -0.2044 | 0.2257 | ±0.4513 | -0.906 | 0.3650 | 0.8151 |  |
| Nocturnal time > 180 (%) | +0.0060 | 0.0031 | ±0.0062 | +1.941 | 0.0522 | 1.0060 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0524**, LLR χ² = **40.05** (p = **3.50e-05**), AUC = **0.6538**, AIC = **747.6**, BIC = **799.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9927** | 0.8118 | ±1.6235 | **-2.455** | **0.0141** | 0.1363 | * |
| **Education: graduate level (vs college)** | **-0.6033** | 0.2078 | ±0.4156 | **-2.903** | **0.0037** | 0.5470 | ** |
| **Education: high school or below (vs college)** | **+0.5484** | 0.2543 | ±0.5085 | **+2.157** | **0.0310** | 1.7305 | * |
| **Site: UCSD (vs UAB)** | **+0.5360** | 0.2239 | ±0.4479 | **+2.394** | **0.0167** | 1.7092 | * |
| Site: UW (vs UAB) | +0.0461 | 0.2181 | ±0.4363 | +0.211 | 0.8325 | 1.0472 |  |
| **Age (years)** | **+0.0280** | 0.0093 | ±0.0186 | **+3.004** | **0.0027** | 1.0284 | ** |
| BMI (kg/m2) | +0.0030 | 0.0130 | ±0.0261 | +0.232 | 0.8169 | 1.0030 |  |
| Hypertension | +0.2938 | 0.2054 | ±0.4108 | +1.430 | 0.1526 | 1.3416 |  |
| High cholesterol | -0.1520 | 0.1958 | ±0.3917 | -0.776 | 0.4376 | 0.8590 |  |
| Kidney disease | -0.3577 | 0.2298 | ±0.4596 | -1.557 | 0.1196 | 0.6993 |  |
| Circulatory disease | -0.1965 | 0.2255 | ±0.4510 | -0.871 | 0.3836 | 0.8216 |  |
| Time > 250 (%) | +0.0097 | 0.0051 | ±0.0103 | +1.888 | 0.0590 | 1.0098 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 551)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **551**, events = **280**, McFadden pseudo-R² = **0.0522**, LLR χ² = **39.84** (p = **3.81e-05**), AUC = **0.6538**, AIC = **747.9**, BIC = **799.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9733** | 0.8105 | ±1.6211 | **-2.435** | **0.0149** | 0.1390 | * |
| **Education: graduate level (vs college)** | **-0.6042** | 0.2078 | ±0.4156 | **-2.908** | **0.0036** | 0.5465 | ** |
| **Education: high school or below (vs college)** | **+0.5494** | 0.2542 | ±0.5084 | **+2.161** | **0.0307** | 1.7323 | * |
| **Site: UCSD (vs UAB)** | **+0.5356** | 0.2239 | ±0.4479 | **+2.392** | **0.0168** | 1.7086 | * |
| Site: UW (vs UAB) | +0.0435 | 0.2180 | ±0.4361 | +0.200 | 0.8418 | 1.0445 |  |
| **Age (years)** | **+0.0278** | 0.0093 | ±0.0186 | **+2.984** | **0.0028** | 1.0282 | ** |
| BMI (kg/m2) | +0.0030 | 0.0130 | ±0.0261 | +0.232 | 0.8164 | 1.0030 |  |
| Hypertension | +0.2953 | 0.2054 | ±0.4107 | +1.438 | 0.1505 | 1.3435 |  |
| High cholesterol | -0.1527 | 0.1958 | ±0.3915 | -0.780 | 0.4355 | 0.8584 |  |
| Kidney disease | -0.3597 | 0.2298 | ±0.4597 | -1.565 | 0.1175 | 0.6979 |  |
| Circulatory disease | -0.1974 | 0.2255 | ±0.4510 | -0.875 | 0.3814 | 0.8209 |  |
| Avg. daily time > 250 (%) | +0.0095 | 0.0052 | ±0.0104 | +1.834 | 0.0667 | 1.0096 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 551; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **551**, R² = **0.0735**, Adj R² = **0.0564**, F-statistic = **4.28** (p = **9.07e-06**), Residual SE = **2.839** on **540** df, AIC = **2724.3**, BIC = **2771.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7844** | 1.0638 | ±2.1276 | **+14.838** | **8.37e-50** | *** |
| Education: graduate level (vs college) | +0.2684 | 0.2801 | ±0.5602 | +0.958 | 0.3379 |  |
| **Education: high school or below (vs college)** | **-1.0577** | 0.3848 | ±0.7695 | **-2.749** | **0.0060** | ** |
| Site: UCSD (vs UAB) | -0.0106 | 0.3192 | ±0.6385 | -0.033 | 0.9735 |  |
| Site: UW (vs UAB) | -0.2191 | 0.2969 | ±0.5938 | -0.738 | 0.4606 |  |
| **Age (years)** | **-0.0594** | 0.0131 | ±0.0262 | **-4.525** | **6.04e-06** | *** |
| BMI (kg/m2) | +0.0031 | 0.0177 | ±0.0354 | +0.177 | 0.8597 |  |
| Hypertension | -0.4975 | 0.2759 | ±0.5519 | -1.803 | 0.0714 | . |
| High cholesterol | +0.4532 | 0.2693 | ±0.5386 | +1.683 | 0.0924 | . |
| Kidney disease | +0.4920 | 0.3201 | ±0.6402 | +1.537 | 0.1243 |  |
| Circulatory disease | +0.2448 | 0.3133 | ±0.6267 | +0.781 | 0.4346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **551**, R² = **0.0743**, Adj R² = **0.0554**, F-statistic = **3.93** (p = **1.66e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.8**, BIC = **2777.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2141** | 1.2668 | ±2.5336 | **+12.799** | **1.65e-37** | *** |
| Education: graduate level (vs college) | +0.2572 | 0.2796 | ±0.5591 | +0.920 | 0.3575 |  |
| **Education: high school or below (vs college)** | **-1.0328** | 0.3897 | ±0.7795 | **-2.650** | **0.0080** | ** |
| Site: UCSD (vs UAB) | -0.0229 | 0.3212 | ±0.6423 | -0.071 | 0.9431 |  |
| Site: UW (vs UAB) | -0.2346 | 0.2992 | ±0.5984 | -0.784 | 0.4329 |  |
| **Age (years)** | **-0.0600** | 0.0132 | ±0.0264 | **-4.547** | **5.43e-06** | *** |
| BMI (kg/m2) | +0.0045 | 0.0177 | ±0.0355 | +0.255 | 0.7986 |  |
| Hypertension | -0.4950 | 0.2757 | ±0.5514 | -1.795 | 0.0726 | . |
| High cholesterol | +0.4523 | 0.2693 | ±0.5387 | +1.679 | 0.0931 | . |
| Kidney disease | +0.4874 | 0.3212 | ±0.6424 | +1.517 | 0.1292 |  |
| Circulatory disease | +0.2510 | 0.3148 | ±0.6295 | +0.798 | 0.4251 |  |
| HbA1c (%) | -0.0604 | 0.0823 | ±0.1646 | -0.733 | 0.4635 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **551**, R² = **0.0737**, Adj R² = **0.0548**, F-statistic = **3.90** (p = **1.89e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.2**, BIC = **2777.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9635** | 1.2178 | ±2.4356 | **+13.108** | **2.95e-39** | *** |
| Education: graduate level (vs college) | +0.2642 | 0.2804 | ±0.5608 | +0.942 | 0.3460 |  |
| **Education: high school or below (vs college)** | **-1.0469** | 0.3856 | ±0.7712 | **-2.715** | **0.0066** | ** |
| Site: UCSD (vs UAB) | -0.0190 | 0.3224 | ±0.6448 | -0.059 | 0.9530 |  |
| Site: UW (vs UAB) | -0.2264 | 0.2989 | ±0.5978 | -0.757 | 0.4488 |  |
| **Age (years)** | **-0.0597** | 0.0132 | ±0.0264 | **-4.518** | **6.23e-06** | *** |
| BMI (kg/m2) | +0.0036 | 0.0177 | ±0.0355 | +0.204 | 0.8385 |  |
| Hypertension | -0.4984 | 0.2764 | ±0.5529 | -1.803 | 0.0714 | . |
| High cholesterol | +0.4513 | 0.2694 | ±0.5387 | +1.675 | 0.0938 | . |
| Kidney disease | +0.4947 | 0.3211 | ±0.6422 | +1.541 | 0.1234 |  |
| Circulatory disease | +0.2501 | 0.3146 | ±0.6292 | +0.795 | 0.4267 |  |
| Mean glucose (mg/dL) | -0.0010 | 0.0028 | ±0.0056 | -0.356 | 0.7218 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **551**, R² = **0.0737**, Adj R² = **0.0548**, F-statistic = **3.90** (p = **1.89e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.2**, BIC = **2777.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1018** | 1.4479 | ±2.8958 | **+11.121** | **9.96e-29** | *** |
| Education: graduate level (vs college) | +0.2642 | 0.2804 | ±0.5608 | +0.942 | 0.3460 |  |
| **Education: high school or below (vs college)** | **-1.0469** | 0.3856 | ±0.7712 | **-2.715** | **0.0066** | ** |
| Site: UCSD (vs UAB) | -0.0190 | 0.3224 | ±0.6448 | -0.059 | 0.9530 |  |
| Site: UW (vs UAB) | -0.2264 | 0.2989 | ±0.5978 | -0.757 | 0.4488 |  |
| **Age (years)** | **-0.0597** | 0.0132 | ±0.0264 | **-4.518** | **6.23e-06** | *** |
| BMI (kg/m2) | +0.0036 | 0.0177 | ±0.0355 | +0.204 | 0.8385 |  |
| Hypertension | -0.4984 | 0.2764 | ±0.5529 | -1.803 | 0.0714 | . |
| High cholesterol | +0.4513 | 0.2694 | ±0.5387 | +1.675 | 0.0938 | . |
| Kidney disease | +0.4947 | 0.3211 | ±0.6422 | +1.541 | 0.1234 |  |
| Circulatory disease | +0.2501 | 0.3146 | ±0.6292 | +0.795 | 0.4267 |  |
| GMI (%) | -0.0418 | 0.1173 | ±0.2346 | -0.356 | 0.7218 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **551**, R² = **0.0741**, Adj R² = **0.0552**, F-statistic = **3.92** (p = **1.71e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.9**, BIC = **2777.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0831** | 1.1739 | ±2.3478 | **+13.701** | **1.01e-42** | *** |
| Education: graduate level (vs college) | +0.2580 | 0.2798 | ±0.5596 | +0.922 | 0.3565 |  |
| **Education: high school or below (vs college)** | **-1.0411** | 0.3857 | ±0.7714 | **-2.699** | **0.0069** | ** |
| Site: UCSD (vs UAB) | -0.0273 | 0.3230 | ±0.6460 | -0.084 | 0.9327 |  |
| Site: UW (vs UAB) | -0.2265 | 0.2980 | ±0.5960 | -0.760 | 0.4471 |  |
| **Age (years)** | **-0.0602** | 0.0132 | ±0.0265 | **-4.551** | **5.35e-06** | *** |
| BMI (kg/m2) | +0.0045 | 0.0179 | ±0.0358 | +0.250 | 0.8026 |  |
| Hypertension | -0.5007 | 0.2766 | ±0.5532 | -1.810 | 0.0702 | . |
| High cholesterol | +0.4491 | 0.2689 | ±0.5379 | +1.670 | 0.0949 | . |
| Kidney disease | +0.4929 | 0.3210 | ±0.6420 | +1.535 | 0.1247 |  |
| Circulatory disease | +0.2546 | 0.3140 | ±0.6280 | +0.811 | 0.4175 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0017 | 0.0026 | ±0.0052 | -0.653 | 0.5139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **551**, R² = **0.0779**, Adj R² = **0.0591**, F-statistic = **4.14** (p = **7.04e-06**), Residual SE = **2.834** on **539** df, AIC = **2723.7**, BIC = **2775.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4732** | 1.1980 | ±2.3959 | **+13.751** | **5.02e-43** | *** |
| Education: graduate level (vs college) | +0.2455 | 0.2800 | ±0.5600 | +0.877 | 0.3806 |  |
| **Education: high school or below (vs college)** | **-1.0053** | 0.3886 | ±0.7771 | **-2.587** | **0.0097** | ** |
| Site: UCSD (vs UAB) | -0.0403 | 0.3208 | ±0.6416 | -0.126 | 0.9000 |  |
| Site: UW (vs UAB) | -0.2771 | 0.3005 | ±0.6010 | -0.922 | 0.3565 |  |
| **Age (years)** | **-0.0602** | 0.0132 | ±0.0264 | **-4.564** | **5.01e-06** | *** |
| BMI (kg/m2) | +0.0046 | 0.0176 | ±0.0352 | +0.263 | 0.7925 |  |
| Hypertension | -0.4906 | 0.2756 | ±0.5512 | -1.780 | 0.0751 | . |
| High cholesterol | +0.4406 | 0.2684 | ±0.5367 | +1.642 | 0.1006 |  |
| Kidney disease | +0.5721 | 0.3211 | ±0.6421 | +1.782 | 0.0748 | . |
| Circulatory disease | +0.2654 | 0.3133 | ±0.6265 | +0.847 | 0.3968 |  |
| Glucose SD, pooled (mg/dL) | -0.0162 | 0.0100 | ±0.0200 | -1.621 | 0.1051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **551**, R² = **0.0769**, Adj R² = **0.0581**, F-statistic = **4.08** (p = **8.86e-06**), Residual SE = **2.836** on **539** df, AIC = **2724.2**, BIC = **2776.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4231** | 1.2213 | ±2.4427 | **+13.447** | **3.21e-41** | *** |
| Education: graduate level (vs college) | +0.2527 | 0.2805 | ±0.5610 | +0.901 | 0.3676 |  |
| **Education: high school or below (vs college)** | **-1.0031** | 0.3881 | ±0.7762 | **-2.585** | **0.0097** | ** |
| Site: UCSD (vs UAB) | -0.0367 | 0.3203 | ±0.6407 | -0.115 | 0.9087 |  |
| Site: UW (vs UAB) | -0.2643 | 0.2998 | ±0.5995 | -0.882 | 0.3780 |  |
| **Age (years)** | **-0.0599** | 0.0132 | ±0.0264 | **-4.536** | **5.74e-06** | *** |
| BMI (kg/m2) | +0.0033 | 0.0177 | ±0.0354 | +0.186 | 0.8526 |  |
| Hypertension | -0.4971 | 0.2761 | ±0.5521 | -1.801 | 0.0718 | . |
| High cholesterol | +0.4446 | 0.2691 | ±0.5382 | +1.652 | 0.0984 | . |
| Kidney disease | +0.5695 | 0.3206 | ±0.6411 | +1.776 | 0.0757 | . |
| Circulatory disease | +0.2580 | 0.3138 | ±0.6276 | +0.822 | 0.4110 |  |
| Avg. daily SD (mg/dL) | -0.0163 | 0.0112 | ±0.0225 | -1.453 | 0.1464 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **551**, R² = **0.0783**, Adj R² = **0.0594**, F-statistic = **4.16** (p = **6.48e-06**), Residual SE = **2.834** on **539** df, AIC = **2723.5**, BIC = **2775.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.6766** | 1.2201 | ±2.4403 | **+13.668** | **1.58e-42** | *** |
| Education: graduate level (vs college) | +0.2577 | 0.2797 | ±0.5593 | +0.922 | 0.3568 |  |
| **Education: high school or below (vs college)** | **-1.0340** | 0.3889 | ±0.7777 | **-2.659** | **0.0078** | ** |
| Site: UCSD (vs UAB) | -0.0180 | 0.3183 | ±0.6365 | -0.057 | 0.9548 |  |
| Site: UW (vs UAB) | -0.2644 | 0.2990 | ±0.5981 | -0.884 | 0.3766 |  |
| **Age (years)** | **-0.0591** | 0.0132 | ±0.0264 | **-4.483** | **7.37e-06** | *** |
| BMI (kg/m2) | +0.0028 | 0.0176 | ±0.0352 | +0.159 | 0.8738 |  |
| Hypertension | -0.4768 | 0.2759 | ±0.5519 | -1.728 | 0.0840 | . |
| High cholesterol | +0.4465 | 0.2687 | ±0.5374 | +1.662 | 0.0965 | . |
| Kidney disease | +0.5890 | 0.3163 | ±0.6325 | +1.862 | 0.0625 | . |
| Circulatory disease | +0.2457 | 0.3129 | ±0.6259 | +0.785 | 0.4323 |  |
| CV (%) | -0.0373 | 0.0210 | ±0.0420 | -1.774 | 0.0760 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **551**, R² = **0.0766**, Adj R² = **0.0578**, F-statistic = **4.07** (p = **9.50e-06**), Residual SE = **2.836** on **539** df, AIC = **2724.4**, BIC = **2776.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0563** | 1.1141 | ±2.2283 | **+13.514** | **1.29e-41** | *** |
| Education: graduate level (vs college) | +0.2577 | 0.2796 | ±0.5592 | +0.922 | 0.3567 |  |
| **Education: high school or below (vs college)** | **-1.0443** | 0.3881 | ±0.7762 | **-2.691** | **0.0071** | ** |
| Site: UCSD (vs UAB) | -0.0058 | 0.3183 | ±0.6366 | -0.018 | 0.9855 |  |
| Site: UW (vs UAB) | -0.2454 | 0.2998 | ±0.5996 | -0.819 | 0.4131 |  |
| **Age (years)** | **-0.0593** | 0.0132 | ±0.0264 | **-4.496** | **6.93e-06** | *** |
| BMI (kg/m2) | +0.0024 | 0.0177 | ±0.0354 | +0.136 | 0.8922 |  |
| Hypertension | -0.4872 | 0.2756 | ±0.5513 | -1.767 | 0.0772 | . |
| High cholesterol | +0.4585 | 0.2691 | ±0.5382 | +1.704 | 0.0884 | . |
| Kidney disease | +0.5560 | 0.3170 | ±0.6340 | +1.754 | 0.0795 | . |
| Circulatory disease | +0.2538 | 0.3125 | ±0.6251 | +0.812 | 0.4167 |  |
| Mean / SD ratio | +0.1696 | 0.1231 | ±0.2462 | +1.378 | 0.1682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **551**, R² = **0.0747**, Adj R² = **0.0558**, F-statistic = **3.96** (p = **1.50e-05**), Residual SE = **2.839** on **539** df, AIC = **2725.6**, BIC = **2777.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3709** | 1.0847 | ±2.1694 | **+14.170** | **1.40e-45** | *** |
| Education: graduate level (vs college) | +0.2620 | 0.2804 | ±0.5609 | +0.934 | 0.3502 |  |
| **Education: high school or below (vs college)** | **-1.0474** | 0.3872 | ±0.7744 | **-2.705** | **0.0068** | ** |
| Site: UCSD (vs UAB) | -0.0064 | 0.3192 | ±0.6384 | -0.020 | 0.9839 |  |
| Site: UW (vs UAB) | -0.2292 | 0.2997 | ±0.5995 | -0.765 | 0.4444 |  |
| **Age (years)** | **-0.0591** | 0.0131 | ±0.0263 | **-4.498** | **6.84e-06** | *** |
| BMI (kg/m2) | +0.0019 | 0.0180 | ±0.0360 | +0.106 | 0.9158 |  |
| Hypertension | -0.4937 | 0.2761 | ±0.5522 | -1.788 | 0.0737 | . |
| High cholesterol | +0.4545 | 0.2696 | ±0.5393 | +1.686 | 0.0919 | . |
| Kidney disease | +0.5282 | 0.3179 | ±0.6358 | +1.661 | 0.0966 | . |
| Circulatory disease | +0.2450 | 0.3132 | ±0.6265 | +0.782 | 0.4342 |  |
| Avg. daily mean/SD | +0.0848 | 0.1103 | ±0.2205 | +0.769 | 0.4419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **551**, R² = **0.0754**, Adj R² = **0.0566**, F-statistic = **4.00** (p = **1.26e-05**), Residual SE = **2.838** on **539** df, AIC = **2725.1**, BIC = **2776.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5452** | 1.3699 | ±2.7397 | **+12.078** | **1.38e-33** | *** |
| Education: graduate level (vs college) | +0.2493 | 0.2835 | ±0.5669 | +0.879 | 0.3792 |  |
| **Education: high school or below (vs college)** | **-1.0361** | 0.3846 | ±0.7691 | **-2.694** | **0.0071** | ** |
| Site: UCSD (vs UAB) | -0.0270 | 0.3188 | ±0.6376 | -0.085 | 0.9325 |  |
| Site: UW (vs UAB) | -0.2687 | 0.3024 | ±0.6049 | -0.888 | 0.3744 |  |
| **Age (years)** | **-0.0612** | 0.0134 | ±0.0268 | **-4.572** | **4.83e-06** | *** |
| BMI (kg/m2) | +0.0028 | 0.0178 | ±0.0356 | +0.159 | 0.8738 |  |
| Hypertension | -0.4965 | 0.2765 | ±0.5531 | -1.795 | 0.0726 | . |
| High cholesterol | +0.4465 | 0.2704 | ±0.5409 | +1.651 | 0.0988 | . |
| Kidney disease | +0.5248 | 0.3240 | ±0.6480 | +1.620 | 0.1053 |  |
| Circulatory disease | +0.2505 | 0.3167 | ±0.6333 | +0.791 | 0.4289 |  |
| MAG (mg/dL/h) | -0.0135 | 0.0131 | ±0.0262 | -1.030 | 0.3028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **551**, R² = **0.0766**, Adj R² = **0.0578**, F-statistic = **4.07** (p = **9.58e-06**), Residual SE = **2.836** on **539** df, AIC = **2724.4**, BIC = **2776.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.6213** | 1.3166 | ±2.6332 | **+12.625** | **1.55e-36** | *** |
| Education: graduate level (vs college) | +0.2529 | 0.2812 | ±0.5624 | +0.899 | 0.3685 |  |
| **Education: high school or below (vs college)** | **-1.0054** | 0.3882 | ±0.7764 | **-2.590** | **0.0096** | ** |
| Site: UCSD (vs UAB) | -0.0377 | 0.3200 | ±0.6401 | -0.118 | 0.9062 |  |
| Site: UW (vs UAB) | -0.2620 | 0.2994 | ±0.5988 | -0.875 | 0.3814 |  |
| **Age (years)** | **-0.0606** | 0.0133 | ±0.0266 | **-4.562** | **5.07e-06** | *** |
| BMI (kg/m2) | +0.0027 | 0.0178 | ±0.0356 | +0.149 | 0.8812 |  |
| Hypertension | -0.5053 | 0.2764 | ±0.5528 | -1.828 | 0.0675 | . |
| High cholesterol | +0.4528 | 0.2693 | ±0.5386 | +1.681 | 0.0927 | . |
| Kidney disease | +0.5703 | 0.3203 | ±0.6406 | +1.780 | 0.0750 | . |
| Circulatory disease | +0.2617 | 0.3145 | ±0.6291 | +0.832 | 0.4054 |  |
| Avg. daily range (mg/dL) | -0.0046 | 0.0035 | ±0.0070 | -1.313 | 0.1893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **551**, R² = **0.0770**, Adj R² = **0.0582**, F-statistic = **4.09** (p = **8.68e-06**), Residual SE = **2.836** on **539** df, AIC = **2724.2**, BIC = **2775.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1310** | 1.0979 | ±2.1958 | **+14.693** | **7.16e-49** | *** |
| Education: graduate level (vs college) | +0.2343 | 0.2808 | ±0.5615 | +0.835 | 0.4040 |  |
| **Education: high school or below (vs college)** | **-1.0466** | 0.3864 | ±0.7728 | **-2.709** | **0.0068** | ** |
| Site: UCSD (vs UAB) | -0.0279 | 0.3208 | ±0.6416 | -0.087 | 0.9308 |  |
| Site: UW (vs UAB) | -0.2639 | 0.2999 | ±0.5998 | -0.880 | 0.3789 |  |
| **Age (years)** | **-0.0613** | 0.0132 | ±0.0263 | **-4.664** | **3.11e-06** | *** |
| BMI (kg/m2) | +0.0058 | 0.0175 | ±0.0351 | +0.333 | 0.7393 |  |
| Hypertension | -0.4743 | 0.2747 | ±0.5493 | -1.727 | 0.0842 | . |
| High cholesterol | +0.4416 | 0.2676 | ±0.5352 | +1.650 | 0.0990 | . |
| Kidney disease | +0.5201 | 0.3219 | ±0.6439 | +1.616 | 0.1062 |  |
| Circulatory disease | +0.2849 | 0.3121 | ±0.6242 | +0.913 | 0.3613 |  |
| SD of daily means (mg/dL) | -0.0204 | 0.0158 | ±0.0316 | -1.293 | 0.1959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **551**, R² = **0.0739**, Adj R² = **0.0550**, F-statistic = **3.91** (p = **1.79e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.0**, BIC = **2777.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6307** | 1.0742 | ±2.1485 | **+14.550** | **5.80e-48** | *** |
| Education: graduate level (vs college) | +0.2635 | 0.2803 | ±0.5607 | +0.940 | 0.3473 |  |
| **Education: high school or below (vs college)** | **-1.0406** | 0.3857 | ±0.7713 | **-2.698** | **0.0070** | ** |
| Site: UCSD (vs UAB) | -0.0255 | 0.3235 | ±0.6470 | -0.079 | 0.9370 |  |
| Site: UW (vs UAB) | -0.2305 | 0.2991 | ±0.5982 | -0.770 | 0.4410 |  |
| **Age (years)** | **-0.0597** | 0.0132 | ±0.0264 | **-4.525** | **6.04e-06** | *** |
| BMI (kg/m2) | +0.0040 | 0.0177 | ±0.0354 | +0.228 | 0.8195 |  |
| Hypertension | -0.5006 | 0.2767 | ±0.5533 | -1.809 | 0.0704 | . |
| High cholesterol | +0.4470 | 0.2693 | ±0.5385 | +1.660 | 0.0969 | . |
| Kidney disease | +0.4991 | 0.3211 | ±0.6421 | +1.554 | 0.1201 |  |
| Circulatory disease | +0.2525 | 0.3147 | ±0.6294 | +0.802 | 0.4223 |  |
| Time in range 70-180, pooled (%) | +0.0024 | 0.0046 | ±0.0092 | +0.514 | 0.6074 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **551**, R² = **0.0739**, Adj R² = **0.0550**, F-statistic = **3.91** (p = **1.80e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.0**, BIC = **2777.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6309** | 1.0757 | ±2.1514 | **+14.531** | **7.75e-48** | *** |
| Education: graduate level (vs college) | +0.2641 | 0.2804 | ±0.5609 | +0.942 | 0.3463 |  |
| **Education: high school or below (vs college)** | **-1.0401** | 0.3858 | ±0.7715 | **-2.696** | **0.0070** | ** |
| Site: UCSD (vs UAB) | -0.0261 | 0.3238 | ±0.6476 | -0.081 | 0.9358 |  |
| Site: UW (vs UAB) | -0.2305 | 0.2992 | ±0.5984 | -0.771 | 0.4410 |  |
| **Age (years)** | **-0.0597** | 0.0132 | ±0.0264 | **-4.525** | **6.05e-06** | *** |
| BMI (kg/m2) | +0.0041 | 0.0177 | ±0.0355 | +0.229 | 0.8189 |  |
| Hypertension | -0.5008 | 0.2767 | ±0.5534 | -1.810 | 0.0703 | . |
| High cholesterol | +0.4473 | 0.2693 | ±0.5386 | +1.661 | 0.0967 | . |
| Kidney disease | +0.4999 | 0.3211 | ±0.6421 | +1.557 | 0.1195 |  |
| Circulatory disease | +0.2524 | 0.3147 | ±0.6294 | +0.802 | 0.4224 |  |
| Avg. daily time in range 70-180 (%) | +0.0023 | 0.0046 | ±0.0092 | +0.505 | 0.6137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **551**, R² = **0.0747**, Adj R² = **0.0558**, F-statistic = **3.95** (p = **1.51e-05**), Residual SE = **2.839** on **539** df, AIC = **2725.6**, BIC = **2777.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8808** | 1.0614 | ±2.1229 | **+14.962** | **1.31e-50** | *** |
| Education: graduate level (vs college) | +0.2684 | 0.2807 | ±0.5614 | +0.956 | 0.3390 |  |
| **Education: high school or below (vs college)** | **-1.0617** | 0.3847 | ±0.7693 | **-2.760** | **0.0058** | ** |
| Site: UCSD (vs UAB) | -0.0267 | 0.3191 | ±0.6382 | -0.084 | 0.9334 |  |
| Site: UW (vs UAB) | -0.2332 | 0.2972 | ±0.5944 | -0.785 | 0.4327 |  |
| **Age (years)** | **-0.0601** | 0.0131 | ±0.0261 | **-4.593** | **4.36e-06** | *** |
| BMI (kg/m2) | +0.0031 | 0.0176 | ±0.0352 | +0.174 | 0.8616 |  |
| Hypertension | -0.4754 | 0.2803 | ±0.5605 | -1.696 | 0.0898 | . |
| High cholesterol | +0.4379 | 0.2696 | ±0.5392 | +1.624 | 0.1043 |  |
| Kidney disease | +0.4963 | 0.3217 | ±0.6434 | +1.543 | 0.1229 |  |
| Circulatory disease | +0.2614 | 0.3138 | ±0.6275 | +0.833 | 0.4047 |  |
| Any reading < 54 during wear (0/1) | -0.2432 | 0.2976 | ±0.5953 | -0.817 | 0.4138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **551**, R² = **0.0746**, Adj R² = **0.0557**, F-statistic = **3.95** (p = **1.52e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.6**, BIC = **2777.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8199** | 1.0657 | ±2.1315 | **+14.844** | **7.61e-50** | *** |
| Education: graduate level (vs college) | +0.2608 | 0.2809 | ±0.5619 | +0.928 | 0.3533 |  |
| **Education: high school or below (vs college)** | **-1.0696** | 0.3851 | ±0.7701 | **-2.778** | **0.0055** | ** |
| Site: UCSD (vs UAB) | -0.0321 | 0.3190 | ±0.6379 | -0.101 | 0.9199 |  |
| Site: UW (vs UAB) | -0.2461 | 0.2984 | ±0.5967 | -0.825 | 0.4094 |  |
| **Age (years)** | **-0.0593** | 0.0131 | ±0.0263 | **-4.515** | **6.34e-06** | *** |
| BMI (kg/m2) | +0.0031 | 0.0176 | ±0.0353 | +0.177 | 0.8592 |  |
| Hypertension | -0.4724 | 0.2796 | ±0.5593 | -1.689 | 0.0912 | . |
| High cholesterol | +0.4346 | 0.2708 | ±0.5416 | +1.605 | 0.1085 |  |
| Kidney disease | +0.4957 | 0.3214 | ±0.6427 | +1.543 | 0.1229 |  |
| Circulatory disease | +0.2287 | 0.3147 | ±0.6294 | +0.727 | 0.4674 |  |
| Time < 54 (%) | -0.3951 | 0.5246 | ±1.0492 | -0.753 | 0.4514 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **551**, R² = **0.0759**, Adj R² = **0.0570**, F-statistic = **4.02** (p = **1.14e-05**), Residual SE = **2.838** on **539** df, AIC = **2724.9**, BIC = **2776.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8133** | 1.0623 | ±2.1247 | **+14.886** | **4.09e-50** | *** |
| Education: graduate level (vs college) | +0.2609 | 0.2808 | ±0.5616 | +0.929 | 0.3529 |  |
| **Education: high school or below (vs college)** | **-1.0735** | 0.3849 | ±0.7699 | **-2.789** | **0.0053** | ** |
| Site: UCSD (vs UAB) | -0.0345 | 0.3197 | ±0.6394 | -0.108 | 0.9140 |  |
| Site: UW (vs UAB) | -0.2500 | 0.2983 | ±0.5966 | -0.838 | 0.4020 |  |
| **Age (years)** | **-0.0593** | 0.0131 | ±0.0262 | **-4.525** | **6.05e-06** | *** |
| BMI (kg/m2) | +0.0035 | 0.0175 | ±0.0350 | +0.198 | 0.8432 |  |
| Hypertension | -0.4729 | 0.2775 | ±0.5551 | -1.704 | 0.0884 | . |
| High cholesterol | +0.4301 | 0.2706 | ±0.5412 | +1.589 | 0.1120 |  |
| Kidney disease | +0.5024 | 0.3215 | ±0.6430 | +1.563 | 0.1181 |  |
| Circulatory disease | +0.2295 | 0.3141 | ±0.6283 | +0.731 | 0.4650 |  |
| Avg. daily time < 54 (%) | -0.4143 | 0.3079 | ±0.6158 | -1.346 | 0.1784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **551**, R² = **0.0797**, Adj R² = **0.0609**, F-statistic = **4.24** (p = **4.60e-06**), Residual SE = **2.832** on **539** df, AIC = **2722.6**, BIC = **2774.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8938** | 1.0611 | ±2.1222 | **+14.979** | **1.01e-50** | *** |
| Education: graduate level (vs college) | +0.2555 | 0.2808 | ±0.5617 | +0.910 | 0.3629 |  |
| **Education: high school or below (vs college)** | **-1.0599** | 0.3855 | ±0.7710 | **-2.750** | **0.0060** | ** |
| Site: UCSD (vs UAB) | -0.0700 | 0.3183 | ±0.6365 | -0.220 | 0.8260 |  |
| Site: UW (vs UAB) | -0.2735 | 0.2984 | ±0.5968 | -0.917 | 0.3593 |  |
| **Age (years)** | **-0.0587** | 0.0131 | ±0.0263 | **-4.461** | **8.14e-06** | *** |
| BMI (kg/m2) | +0.0020 | 0.0176 | ±0.0351 | +0.114 | 0.9093 |  |
| Hypertension | -0.4499 | 0.2776 | ±0.5551 | -1.621 | 0.1050 |  |
| High cholesterol | +0.4085 | 0.2696 | ±0.5391 | +1.516 | 0.1296 |  |
| Kidney disease | +0.5184 | 0.3182 | ±0.6363 | +1.629 | 0.1032 |  |
| Circulatory disease | +0.2166 | 0.3169 | ±0.6339 | +0.683 | 0.4943 |  |
| Time 54-69, pooled (%) | -0.2594 | 0.1379 | ±0.2757 | -1.882 | 0.0599 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **551**, R² = **0.0835**, Adj R² = **0.0648**, F-statistic = **4.47** (p = **1.83e-06**), Residual SE = **2.826** on **539** df, AIC = **2720.3**, BIC = **2772.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8754** | 1.0573 | ±2.1147 | **+15.015** | **5.90e-51** | *** |
| Education: graduate level (vs college) | +0.2459 | 0.2805 | ±0.5611 | +0.876 | 0.3808 |  |
| **Education: high school or below (vs college)** | **-1.0661** | 0.3851 | ±0.7703 | **-2.768** | **0.0056** | ** |
| Site: UCSD (vs UAB) | -0.0855 | 0.3183 | ±0.6367 | -0.269 | 0.7882 |  |
| Site: UW (vs UAB) | -0.2959 | 0.2979 | ±0.5958 | -0.993 | 0.3205 |  |
| **Age (years)** | **-0.0582** | 0.0131 | ±0.0263 | **-4.429** | **9.49e-06** | *** |
| BMI (kg/m2) | +0.0025 | 0.0174 | ±0.0349 | +0.145 | 0.8851 |  |
| Hypertension | -0.4355 | 0.2772 | ±0.5545 | -1.571 | 0.1162 |  |
| High cholesterol | +0.3934 | 0.2695 | ±0.5389 | +1.460 | 0.1443 |  |
| Kidney disease | +0.5211 | 0.3180 | ±0.6360 | +1.639 | 0.1013 |  |
| Circulatory disease | +0.2030 | 0.3162 | ±0.6324 | +0.642 | 0.5209 |  |
| **Avg. daily time 54-69 (%)** | **-0.3153** | 0.1152 | ±0.2304 | **-2.736** | **0.0062** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **551**, R² = **0.0790**, Adj R² = **0.0602**, F-statistic = **4.20** (p = **5.40e-06**), Residual SE = **2.833** on **539** df, AIC = **2723.0**, BIC = **2774.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8902** | 1.0607 | ±2.1214 | **+14.981** | **9.82e-51** | *** |
| Education: graduate level (vs college) | +0.2542 | 0.2810 | ±0.5620 | +0.905 | 0.3657 |  |
| **Education: high school or below (vs college)** | **-1.0657** | 0.3854 | ±0.7707 | **-2.766** | **0.0057** | ** |
| Site: UCSD (vs UAB) | -0.0692 | 0.3184 | ±0.6368 | -0.217 | 0.8280 |  |
| Site: UW (vs UAB) | -0.2766 | 0.2983 | ±0.5966 | -0.927 | 0.3538 |  |
| **Age (years)** | **-0.0587** | 0.0131 | ±0.0263 | **-4.471** | **7.77e-06** | *** |
| BMI (kg/m2) | +0.0022 | 0.0175 | ±0.0350 | +0.127 | 0.8988 |  |
| Hypertension | -0.4465 | 0.2784 | ±0.5568 | -1.604 | 0.1088 |  |
| High cholesterol | +0.4079 | 0.2697 | ±0.5394 | +1.512 | 0.1305 |  |
| Kidney disease | +0.5150 | 0.3190 | ±0.6380 | +1.614 | 0.1065 |  |
| Circulatory disease | +0.2139 | 0.3167 | ±0.6334 | +0.675 | 0.4994 |  |
| Time < 70 (%) | -0.2067 | 0.1113 | ±0.2227 | -1.856 | 0.0634 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **551**, R² = **0.0822**, Adj R² = **0.0635**, F-statistic = **4.39** (p = **2.49e-06**), Residual SE = **2.828** on **539** df, AIC = **2721.1**, BIC = **2772.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8681** | 1.0571 | ±2.1143 | **+15.010** | **6.29e-51** | *** |
| Education: graduate level (vs college) | +0.2475 | 0.2807 | ±0.5614 | +0.882 | 0.3780 |  |
| **Education: high school or below (vs college)** | **-1.0729** | 0.3849 | ±0.7698 | **-2.787** | **0.0053** | ** |
| Site: UCSD (vs UAB) | -0.0796 | 0.3187 | ±0.6374 | -0.250 | 0.8028 |  |
| Site: UW (vs UAB) | -0.2934 | 0.2980 | ±0.5960 | -0.985 | 0.3248 |  |
| **Age (years)** | **-0.0584** | 0.0131 | ±0.0262 | **-4.457** | **8.31e-06** | *** |
| BMI (kg/m2) | +0.0029 | 0.0174 | ±0.0348 | +0.165 | 0.8691 |  |
| Hypertension | -0.4378 | 0.2776 | ±0.5551 | -1.577 | 0.1148 |  |
| High cholesterol | +0.3959 | 0.2697 | ±0.5394 | +1.468 | 0.1422 |  |
| Kidney disease | +0.5194 | 0.3190 | ±0.6379 | +1.629 | 0.1034 |  |
| Circulatory disease | +0.2052 | 0.3158 | ±0.6316 | +0.650 | 0.5159 |  |
| **Avg. daily time < 70 (%)** | **-0.2335** | 0.0817 | ±0.1633 | **-2.859** | **0.0042** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **551**, R² = **0.0742**, Adj R² = **0.0553**, F-statistic = **3.93** (p = **1.67e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.9**, BIC = **2777.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.4299** | 1.1407 | ±2.2814 | **+13.527** | **1.09e-41** | *** |
| Education: graduate level (vs college) | +0.2555 | 0.2809 | ±0.5617 | +0.910 | 0.3631 |  |
| **Education: high school or below (vs college)** | **-1.0384** | 0.3859 | ±0.7719 | **-2.690** | **0.0071** | ** |
| Site: UCSD (vs UAB) | -0.0263 | 0.3211 | ±0.6421 | -0.082 | 0.9347 |  |
| Site: UW (vs UAB) | -0.2400 | 0.2991 | ±0.5983 | -0.802 | 0.4225 |  |
| **Age (years)** | **-0.0602** | 0.0132 | ±0.0264 | **-4.555** | **5.23e-06** | *** |
| BMI (kg/m2) | +0.0038 | 0.0178 | ±0.0356 | +0.213 | 0.8311 |  |
| Hypertension | -0.4916 | 0.2761 | ±0.5522 | -1.780 | 0.0750 | . |
| High cholesterol | +0.4487 | 0.2692 | ±0.5385 | +1.667 | 0.0956 | . |
| Kidney disease | +0.5012 | 0.3214 | ±0.6428 | +1.559 | 0.1190 |  |
| Circulatory disease | +0.2521 | 0.3143 | ±0.6287 | +0.802 | 0.4225 |  |
| Time 54-250, pooled (%) | +0.0044 | 0.0059 | ±0.0118 | +0.747 | 0.4552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **551**, R² = **0.0741**, Adj R² = **0.0552**, F-statistic = **3.92** (p = **1.73e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.9**, BIC = **2777.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.4599** | 1.1446 | ±2.2892 | **+13.507** | **1.42e-41** | *** |
| Education: graduate level (vs college) | +0.2569 | 0.2810 | ±0.5621 | +0.914 | 0.3606 |  |
| **Education: high school or below (vs college)** | **-1.0406** | 0.3858 | ±0.7716 | **-2.697** | **0.0070** | ** |
| Site: UCSD (vs UAB) | -0.0248 | 0.3211 | ±0.6423 | -0.077 | 0.9385 |  |
| Site: UW (vs UAB) | -0.2371 | 0.2990 | ±0.5979 | -0.793 | 0.4278 |  |
| **Age (years)** | **-0.0601** | 0.0132 | ±0.0264 | **-4.548** | **5.41e-06** | *** |
| BMI (kg/m2) | +0.0037 | 0.0178 | ±0.0356 | +0.210 | 0.8336 |  |
| Hypertension | -0.4928 | 0.2761 | ±0.5522 | -1.785 | 0.0743 | . |
| High cholesterol | +0.4492 | 0.2693 | ±0.5386 | +1.668 | 0.0953 | . |
| Kidney disease | +0.5013 | 0.3215 | ±0.6429 | +1.559 | 0.1189 |  |
| Circulatory disease | +0.2519 | 0.3144 | ±0.6288 | +0.801 | 0.4230 |  |
| Avg. daily time 54-250 (%) | +0.0040 | 0.0059 | ±0.0118 | +0.671 | 0.5025 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **551**, R² = **0.0735**, Adj R² = **0.0546**, F-statistic = **3.89** (p = **1.98e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.3**, BIC = **2778.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7775** | 1.0909 | ±2.1818 | **+14.463** | **2.09e-47** | *** |
| Education: graduate level (vs college) | +0.2680 | 0.2814 | ±0.5628 | +0.952 | 0.3409 |  |
| **Education: high school or below (vs college)** | **-1.0589** | 0.3849 | ±0.7699 | **-2.751** | **0.0059** | ** |
| Site: UCSD (vs UAB) | -0.0095 | 0.3226 | ±0.6452 | -0.029 | 0.9766 |  |
| Site: UW (vs UAB) | -0.2191 | 0.2975 | ±0.5949 | -0.737 | 0.4613 |  |
| **Age (years)** | **-0.0594** | 0.0131 | ±0.0262 | **-4.527** | **5.98e-06** | *** |
| BMI (kg/m2) | +0.0030 | 0.0177 | ±0.0354 | +0.171 | 0.8643 |  |
| Hypertension | -0.4962 | 0.2798 | ±0.5596 | -1.773 | 0.0762 | . |
| High cholesterol | +0.4539 | 0.2697 | ±0.5395 | +1.683 | 0.0925 | . |
| Kidney disease | +0.4917 | 0.3205 | ±0.6410 | +1.534 | 0.1250 |  |
| Circulatory disease | +0.2441 | 0.3148 | ±0.6295 | +0.775 | 0.4381 |  |
| Time 181-250, pooled (%) | +0.0004 | 0.0084 | ±0.0168 | +0.053 | 0.9575 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **551**, R² = **0.0735**, Adj R² = **0.0546**, F-statistic = **3.89** (p = **1.98e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.3**, BIC = **2778.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7842** | 1.0914 | ±2.1827 | **+14.463** | **2.07e-47** | *** |
| Education: graduate level (vs college) | +0.2684 | 0.2816 | ±0.5631 | +0.953 | 0.3405 |  |
| **Education: high school or below (vs college)** | **-1.0577** | 0.3851 | ±0.7702 | **-2.746** | **0.0060** | ** |
| Site: UCSD (vs UAB) | -0.0106 | 0.3230 | ±0.6459 | -0.033 | 0.9739 |  |
| Site: UW (vs UAB) | -0.2191 | 0.2976 | ±0.5952 | -0.736 | 0.4617 |  |
| **Age (years)** | **-0.0594** | 0.0131 | ±0.0263 | **-4.524** | **6.08e-06** | *** |
| BMI (kg/m2) | +0.0031 | 0.0177 | ±0.0354 | +0.177 | 0.8598 |  |
| Hypertension | -0.4975 | 0.2797 | ±0.5593 | -1.779 | 0.0753 | . |
| High cholesterol | +0.4532 | 0.2697 | ±0.5394 | +1.681 | 0.0928 | . |
| Kidney disease | +0.4920 | 0.3205 | ±0.6409 | +1.535 | 0.1247 |  |
| Circulatory disease | +0.2448 | 0.3146 | ±0.6292 | +0.778 | 0.4365 |  |
| Avg. daily time 181-250 (%) | +0.0000 | 0.0083 | ±0.0166 | +0.001 | 0.9989 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **551**, R² = **0.0738**, Adj R² = **0.0549**, F-statistic = **3.91** (p = **1.85e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.1**, BIC = **2777.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8534** | 1.0950 | ±2.1901 | **+14.478** | **1.68e-47** | *** |
| Education: graduate level (vs college) | +0.2644 | 0.2803 | ±0.5606 | +0.943 | 0.3455 |  |
| **Education: high school or below (vs college)** | **-1.0434** | 0.3856 | ±0.7712 | **-2.706** | **0.0068** | ** |
| Site: UCSD (vs UAB) | -0.0225 | 0.3233 | ±0.6466 | -0.070 | 0.9444 |  |
| Site: UW (vs UAB) | -0.2280 | 0.2990 | ±0.5980 | -0.763 | 0.4456 |  |
| **Age (years)** | **-0.0596** | 0.0132 | ±0.0264 | **-4.521** | **6.17e-06** | *** |
| BMI (kg/m2) | +0.0039 | 0.0177 | ±0.0354 | +0.220 | 0.8258 |  |
| Hypertension | -0.5006 | 0.2768 | ±0.5536 | -1.808 | 0.0706 | . |
| High cholesterol | +0.4485 | 0.2693 | ±0.5387 | +1.665 | 0.0959 | . |
| Kidney disease | +0.4977 | 0.3210 | ±0.6421 | +1.550 | 0.1211 |  |
| Circulatory disease | +0.2516 | 0.3148 | ±0.6295 | +0.799 | 0.4241 |  |
| Time > 180 (%) | -0.0020 | 0.0046 | ±0.0092 | -0.433 | 0.6652 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **551**, R² = **0.0738**, Adj R² = **0.0549**, F-statistic = **3.90** (p = **1.87e-05**), Residual SE = **2.841** on **539** df, AIC = **2726.1**, BIC = **2777.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8452** | 1.0935 | ±2.1870 | **+14.491** | **1.39e-47** | *** |
| Education: graduate level (vs college) | +0.2652 | 0.2804 | ±0.5609 | +0.946 | 0.3443 |  |
| **Education: high school or below (vs college)** | **-1.0439** | 0.3857 | ±0.7714 | **-2.707** | **0.0068** | ** |
| Site: UCSD (vs UAB) | -0.0221 | 0.3236 | ±0.6472 | -0.068 | 0.9456 |  |
| Site: UW (vs UAB) | -0.2274 | 0.2990 | ±0.5980 | -0.760 | 0.4470 |  |
| **Age (years)** | **-0.0596** | 0.0132 | ±0.0264 | **-4.519** | **6.21e-06** | *** |
| BMI (kg/m2) | +0.0039 | 0.0177 | ±0.0355 | +0.217 | 0.8281 |  |
| Hypertension | -0.5005 | 0.2769 | ±0.5537 | -1.808 | 0.0706 | . |
| High cholesterol | +0.4491 | 0.2694 | ±0.5387 | +1.667 | 0.0955 | . |
| Kidney disease | +0.4979 | 0.3210 | ±0.6420 | +1.551 | 0.1208 |  |
| Circulatory disease | +0.2510 | 0.3148 | ±0.6295 | +0.798 | 0.4251 |  |
| Avg. daily time > 180 (%) | -0.0018 | 0.0046 | ±0.0092 | -0.394 | 0.6932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **551**, R² = **0.0744**, Adj R² = **0.0555**, F-statistic = **3.94** (p = **1.60e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.7**, BIC = **2777.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8753** | 1.0806 | ±2.1613 | **+14.691** | **7.38e-49** | *** |
| Education: graduate level (vs college) | +0.2550 | 0.2796 | ±0.5592 | +0.912 | 0.3617 |  |
| **Education: high school or below (vs college)** | **-1.0371** | 0.3852 | ±0.7704 | **-2.692** | **0.0071** | ** |
| Site: UCSD (vs UAB) | -0.0343 | 0.3236 | ±0.6471 | -0.106 | 0.9156 |  |
| Site: UW (vs UAB) | -0.2298 | 0.2980 | ±0.5960 | -0.771 | 0.4406 |  |
| **Age (years)** | **-0.0602** | 0.0132 | ±0.0265 | **-4.541** | **5.60e-06** | *** |
| BMI (kg/m2) | +0.0051 | 0.0179 | ±0.0359 | +0.284 | 0.7767 |  |
| Hypertension | -0.5028 | 0.2763 | ±0.5527 | -1.819 | 0.0689 | . |
| High cholesterol | +0.4419 | 0.2690 | ±0.5379 | +1.643 | 0.1004 |  |
| Kidney disease | +0.5005 | 0.3210 | ±0.6419 | +1.560 | 0.1189 |  |
| Circulatory disease | +0.2574 | 0.3140 | ±0.6279 | +0.820 | 0.4124 |  |
| Nocturnal time > 180 (%) | -0.0031 | 0.0040 | ±0.0081 | -0.762 | 0.4461 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **551**, R² = **0.0742**, Adj R² = **0.0553**, F-statistic = **3.93** (p = **1.68e-05**), Residual SE = **2.840** on **539** df, AIC = **2725.9**, BIC = **2777.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8684** | 1.0782 | ±2.1564 | **+14.718** | **4.97e-49** | *** |
| Education: graduate level (vs college) | +0.2558 | 0.2808 | ±0.5617 | +0.911 | 0.3624 |  |
| **Education: high school or below (vs college)** | **-1.0386** | 0.3859 | ±0.7719 | **-2.691** | **0.0071** | ** |
| Site: UCSD (vs UAB) | -0.0258 | 0.3211 | ±0.6421 | -0.080 | 0.9360 |  |
| Site: UW (vs UAB) | -0.2393 | 0.2991 | ±0.5982 | -0.800 | 0.4237 |  |
| **Age (years)** | **-0.0602** | 0.0132 | ±0.0264 | **-4.554** | **5.27e-06** | *** |
| BMI (kg/m2) | +0.0038 | 0.0178 | ±0.0356 | +0.213 | 0.8316 |  |
| Hypertension | -0.4920 | 0.2761 | ±0.5522 | -1.782 | 0.0748 | . |
| High cholesterol | +0.4490 | 0.2692 | ±0.5385 | +1.668 | 0.0954 | . |
| Kidney disease | +0.5010 | 0.3214 | ±0.6428 | +1.559 | 0.1191 |  |
| Circulatory disease | +0.2522 | 0.3143 | ±0.6287 | +0.802 | 0.4224 |  |
| Time > 250 (%) | -0.0043 | 0.0059 | ±0.0118 | -0.734 | 0.4628 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 551)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **551**, R² = **0.0740**, Adj R² = **0.0551**, F-statistic = **3.92** (p = **1.75e-05**), Residual SE = **2.840** on **539** df, AIC = **2726.0**, BIC = **2777.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8518** | 1.0763 | ±2.1527 | **+14.727** | **4.30e-49** | *** |
| Education: graduate level (vs college) | +0.2575 | 0.2810 | ±0.5621 | +0.916 | 0.3596 |  |
| **Education: high school or below (vs college)** | **-1.0411** | 0.3858 | ±0.7716 | **-2.699** | **0.0070** | ** |
| Site: UCSD (vs UAB) | -0.0240 | 0.3211 | ±0.6422 | -0.075 | 0.9404 |  |
| Site: UW (vs UAB) | -0.2361 | 0.2989 | ±0.5978 | -0.790 | 0.4297 |  |
| **Age (years)** | **-0.0600** | 0.0132 | ±0.0264 | **-4.546** | **5.46e-06** | *** |
| BMI (kg/m2) | +0.0037 | 0.0178 | ±0.0356 | +0.209 | 0.8348 |  |
| Hypertension | -0.4932 | 0.2761 | ±0.5522 | -1.786 | 0.0740 | . |
| High cholesterol | +0.4496 | 0.2693 | ±0.5386 | +1.669 | 0.0950 | . |
| Kidney disease | +0.5009 | 0.3214 | ±0.6428 | +1.558 | 0.1192 |  |
| Circulatory disease | +0.2518 | 0.3144 | ±0.6288 | +0.801 | 0.4232 |  |
| Avg. daily time > 250 (%) | -0.0038 | 0.0059 | ±0.0118 | -0.645 | 0.5192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 90 single-predictor tests; 7 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 90 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family and 0 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 551): best single predictor out of sample is **MAG** (CV R² 0.029 vs 0.022 for covariates alone, gain +0.008; -0.34 per SD, p = 0.031, q = 0.311). No association survives FDR; nominal only: SD of daily means (p = 0.029), MAG (p = 0.031), SD (pooled) (p = 0.036).
- **Cognitive impairment (MoCA < 26)** (n = 551): best single predictor out of sample is **SD of daily means** (CV AUC 0.607 vs 0.599 for covariates alone, gain +0.008; OR 1.24 per SD, p = 0.027, q = 0.311). No association survives FDR; nominal only: MAG (p = 0.015), SD of daily means (p = 0.027).
- **MoCA memory index score (0-15)** (n = 551): best single predictor out of sample is **%54-69 (daily avg)** (CV R² 0.025 vs 0.017 for covariates alone, gain +0.008; -0.298 per SD, p = 0.006, q = 0.260). No association survives FDR; nominal only: %<70 (daily avg) (p = 0.004), %54-69 (daily avg) (p = 0.006).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA memory index score (0-15) (+0.008, via %54-69 (daily avg)); Cognitive impairment (MoCA < 26) (+0.008, via SD of daily means); MoCA total score (0-30) (+0.008, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 5 raw-significant of 24); Band 54-69 (0 FDR-significant / 1 raw-significant of 6); Band < 70 (0 FDR-significant / 1 raw-significant of 6).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (5 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (MAG, ΔAIC -4.0); Cognitive impairment (MAG, ΔAIC -4.4); MoCA memory index score (%54-69 (daily avg), ΔAIC -5.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
