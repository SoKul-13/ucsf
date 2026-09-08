# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Non-healthy group (T2D non-insulin + T2D insulin)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 550; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **550**, R² = **0.1453**, Adj R² = **0.1294**, F-statistic = **9.16** (p = **4.71e-14**), Residual SE = **4.879** on **539** df, AIC = **3315.2**, BIC = **3362.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.9379** | 1.8688 | ±3.7377 | **+6.388** | **1.68e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4384** | 0.4456 | ±0.8913 | **-3.228** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1599 | 0.6846 | ±1.3691 | +1.694 | 0.0902 | . |
| Site: UCSD (vs UAB) | +0.1170 | 0.5598 | ±1.1195 | +0.209 | 0.8345 |  |
| Site: UW (vs UAB) | -0.4161 | 0.4977 | ±0.9953 | -0.836 | 0.4031 |  |
| **Age (years)** | **-0.1219** | 0.0206 | ±0.0413 | **-5.906** | **3.50e-09** | *** |
| BMI (kg/m2) | +0.0378 | 0.0309 | ±0.0618 | +1.223 | 0.2215 |  |
| Hypertension | +0.2668 | 0.4644 | ±0.9288 | +0.574 | 0.5657 |  |
| High cholesterol | +0.3226 | 0.4621 | ±0.9242 | +0.698 | 0.4851 |  |
| Kidney disease | +0.8311 | 0.5671 | ±1.1342 | +1.466 | 0.1428 |  |
| **Circulatory disease** | **+1.9482** | 0.5868 | ±1.1737 | **+3.320** | **9.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **550**, R² = **0.1532**, Adj R² = **0.1359**, F-statistic = **8.85** (p = **1.52e-14**), Residual SE = **4.861** on **538** df, AIC = **3312.0**, BIC = **3363.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4520** | 2.2750 | ±4.5500 | **+4.155** | **3.26e-05** | *** |
| **Education: graduate level (vs college)** | **-1.3727** | 0.4471 | ±0.8942 | **-3.070** | **0.0021** | ** |
| Education: high school or below (vs college) | +1.0124 | 0.6709 | ±1.3418 | +1.509 | 0.1313 |  |
| Site: UCSD (vs UAB) | +0.1882 | 0.5566 | ±1.1132 | +0.338 | 0.7353 |  |
| Site: UW (vs UAB) | -0.3283 | 0.4994 | ±0.9988 | -0.657 | 0.5109 |  |
| **Age (years)** | **-0.1187** | 0.0206 | ±0.0413 | **-5.752** | **8.81e-09** | *** |
| BMI (kg/m2) | +0.0296 | 0.0314 | ±0.0629 | +0.942 | 0.3463 |  |
| Hypertension | +0.2518 | 0.4652 | ±0.9304 | +0.541 | 0.5883 |  |
| High cholesterol | +0.3278 | 0.4603 | ±0.9206 | +0.712 | 0.4764 |  |
| Kidney disease | +0.8594 | 0.5692 | ±1.1385 | +1.510 | 0.1311 |  |
| **Circulatory disease** | **+1.9097** | 0.5870 | ±1.1741 | **+3.253** | **0.0011** | ** |
| HbA1c (%) | +0.3505 | 0.1791 | ±0.3581 | +1.957 | 0.0503 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **550**, R² = **0.1480**, Adj R² = **0.1306**, F-statistic = **8.50** (p = **6.76e-14**), Residual SE = **4.876** on **538** df, AIC = **3315.4**, BIC = **3367.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.7189** | 2.1383 | ±4.2767 | **+5.013** | **5.37e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4090** | 0.4473 | ±0.8947 | **-3.150** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0828 | 0.6801 | ±1.3602 | +1.592 | 0.1114 |  |
| Site: UCSD (vs UAB) | +0.1743 | 0.5591 | ±1.1183 | +0.312 | 0.7553 |  |
| Site: UW (vs UAB) | -0.3685 | 0.5013 | ±1.0025 | -0.735 | 0.4623 |  |
| **Age (years)** | **-0.1200** | 0.0207 | ±0.0414 | **-5.802** | **6.57e-09** | *** |
| BMI (kg/m2) | +0.0344 | 0.0311 | ±0.0622 | +1.104 | 0.2694 |  |
| Hypertension | +0.2729 | 0.4630 | ±0.9260 | +0.589 | 0.5555 |  |
| High cholesterol | +0.3354 | 0.4618 | ±0.9237 | +0.726 | 0.4676 |  |
| Kidney disease | +0.8141 | 0.5739 | ±1.1477 | +1.419 | 0.1560 |  |
| **Circulatory disease** | **+1.9098** | 0.5864 | ±1.1728 | **+3.257** | **0.0011** | ** |
| Mean glucose (mg/dL) | +0.0069 | 0.0058 | ±0.0117 | +1.176 | 0.2397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **550**, R² = **0.1480**, Adj R² = **0.1306**, F-statistic = **8.50** (p = **6.76e-14**), Residual SE = **4.876** on **538** df, AIC = **3315.4**, BIC = **3367.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7706** | 2.6231 | ±5.2462 | **+3.725** | **1.95e-04** | *** |
| **Education: graduate level (vs college)** | **-1.4090** | 0.4473 | ±0.8947 | **-3.150** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0828 | 0.6801 | ±1.3602 | +1.592 | 0.1114 |  |
| Site: UCSD (vs UAB) | +0.1743 | 0.5591 | ±1.1183 | +0.312 | 0.7553 |  |
| Site: UW (vs UAB) | -0.3685 | 0.5013 | ±1.0025 | -0.735 | 0.4623 |  |
| **Age (years)** | **-0.1200** | 0.0207 | ±0.0414 | **-5.802** | **6.57e-09** | *** |
| BMI (kg/m2) | +0.0344 | 0.0311 | ±0.0622 | +1.104 | 0.2694 |  |
| Hypertension | +0.2729 | 0.4630 | ±0.9260 | +0.589 | 0.5555 |  |
| High cholesterol | +0.3354 | 0.4618 | ±0.9237 | +0.726 | 0.4676 |  |
| Kidney disease | +0.8141 | 0.5739 | ±1.1477 | +1.419 | 0.1560 |  |
| **Circulatory disease** | **+1.9098** | 0.5864 | ±1.1728 | **+3.257** | **0.0011** | ** |
| GMI (%) | +0.2865 | 0.2437 | ±0.4874 | +1.176 | 0.2397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **550**, R² = **0.1491**, Adj R² = **0.1317**, F-statistic = **8.57** (p = **4.98e-14**), Residual SE = **4.873** on **538** df, AIC = **3314.7**, BIC = **3366.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.6294** | 2.0896 | ±4.1793 | **+5.087** | **3.64e-07** | *** |
| **Education: graduate level (vs college)** | **-1.3919** | 0.4484 | ±0.8968 | **-3.104** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.0838 | 0.6784 | ±1.3568 | +1.598 | 0.1101 |  |
| Site: UCSD (vs UAB) | +0.1902 | 0.5574 | ±1.1147 | +0.341 | 0.7330 |  |
| Site: UW (vs UAB) | -0.3855 | 0.4996 | ±0.9992 | -0.772 | 0.4403 |  |
| **Age (years)** | **-0.1184** | 0.0208 | ±0.0415 | **-5.705** | **1.16e-08** | *** |
| BMI (kg/m2) | +0.0318 | 0.0312 | ±0.0623 | +1.019 | 0.3080 |  |
| Hypertension | +0.2809 | 0.4627 | ±0.9253 | +0.607 | 0.5438 |  |
| High cholesterol | +0.3404 | 0.4612 | ±0.9225 | +0.738 | 0.4605 |  |
| Kidney disease | +0.8285 | 0.5721 | ±1.1442 | +1.448 | 0.1476 |  |
| **Circulatory disease** | **+1.9029** | 0.5860 | ±1.1721 | **+3.247** | **0.0012** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0076 | 0.0053 | ±0.0106 | +1.423 | 0.1548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **550**, R² = **0.1554**, Adj R² = **0.1381**, F-statistic = **9.00** (p = **8.13e-15**), Residual SE = **4.855** on **538** df, AIC = **3310.6**, BIC = **3362.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0737** | 2.0209 | ±4.0418 | **+4.985** | **6.21e-07** | *** |
| **Education: graduate level (vs college)** | **-1.3761** | 0.4464 | ±0.8929 | **-3.082** | **0.0021** | ** |
| Education: high school or below (vs college) | +1.0166 | 0.6815 | ±1.3631 | +1.492 | 0.1358 |  |
| Site: UCSD (vs UAB) | +0.1974 | 0.5554 | ±1.1107 | +0.355 | 0.7222 |  |
| Site: UW (vs UAB) | -0.2598 | 0.5007 | ±1.0015 | -0.519 | 0.6039 |  |
| **Age (years)** | **-0.1196** | 0.0207 | ±0.0413 | **-5.788** | **7.13e-09** | *** |
| BMI (kg/m2) | +0.0337 | 0.0313 | ±0.0625 | +1.076 | 0.2818 |  |
| Hypertension | +0.2480 | 0.4609 | ±0.9219 | +0.538 | 0.5905 |  |
| High cholesterol | +0.3566 | 0.4582 | ±0.9164 | +0.778 | 0.4364 |  |
| Kidney disease | +0.6145 | 0.5853 | ±1.1705 | +1.050 | 0.2937 |  |
| **Circulatory disease** | **+1.8914** | 0.5897 | ±1.1795 | **+3.207** | **0.0013** | ** |
| **Glucose SD, pooled (mg/dL)** | **+0.0439** | 0.0177 | ±0.0354 | **+2.480** | **0.0131** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **550**, R² = **0.1508**, Adj R² = **0.1334**, F-statistic = **8.68** (p = **3.05e-14**), Residual SE = **4.868** on **538** df, AIC = **3313.6**, BIC = **3365.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4888** | 2.0165 | ±4.0331 | **+5.201** | **1.98e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4026** | 0.4466 | ±0.8932 | **-3.141** | **0.0017** | ** |
| Education: high school or below (vs college) | +1.0354 | 0.6879 | ±1.3758 | +1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | +0.1763 | 0.5583 | ±1.1166 | +0.316 | 0.7521 |  |
| Site: UW (vs UAB) | -0.3138 | 0.5017 | ±1.0034 | -0.625 | 0.5317 |  |
| **Age (years)** | **-0.1208** | 0.0206 | ±0.0413 | **-5.852** | **4.86e-09** | *** |
| BMI (kg/m2) | +0.0374 | 0.0311 | ±0.0622 | +1.202 | 0.2293 |  |
| Hypertension | +0.2658 | 0.4623 | ±0.9246 | +0.575 | 0.5653 |  |
| High cholesterol | +0.3421 | 0.4605 | ±0.9211 | +0.743 | 0.4576 |  |
| Kidney disease | +0.6554 | 0.5878 | ±1.1755 | +1.115 | 0.2648 |  |
| **Circulatory disease** | **+1.9180** | 0.5899 | ±1.1798 | **+3.251** | **0.0011** | ** |
| Avg. daily SD (mg/dL) | +0.0371 | 0.0203 | ±0.0407 | +1.825 | 0.0681 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **550**, R² = **0.1499**, Adj R² = **0.1325**, F-statistic = **8.62** (p = **3.95e-14**), Residual SE = **4.870** on **538** df, AIC = **3314.2**, BIC = **3365.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3490** | 2.1015 | ±4.2029 | **+4.925** | **8.45e-07** | *** |
| **Education: graduate level (vs college)** | **-1.4202** | 0.4455 | ±0.8909 | **-3.188** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1221 | 0.6890 | ±1.3780 | +1.629 | 0.1034 |  |
| Site: UCSD (vs UAB) | +0.1306 | 0.5586 | ±1.1172 | +0.234 | 0.8151 |  |
| Site: UW (vs UAB) | -0.3328 | 0.4997 | ±0.9994 | -0.666 | 0.5054 |  |
| **Age (years)** | **-0.1223** | 0.0206 | ±0.0412 | **-5.936** | **2.93e-09** | *** |
| BMI (kg/m2) | +0.0384 | 0.0311 | ±0.0622 | +1.235 | 0.2168 |  |
| Hypertension | +0.2305 | 0.4648 | ±0.9296 | +0.496 | 0.6200 |  |
| High cholesterol | +0.3350 | 0.4610 | ±0.9220 | +0.727 | 0.4675 |  |
| Kidney disease | +0.6580 | 0.5764 | ±1.1529 | +1.142 | 0.2536 |  |
| **Circulatory disease** | **+1.9496** | 0.5909 | ±1.1817 | **+3.300** | **9.68e-04** | *** |
| CV (%) | +0.0659 | 0.0394 | ±0.0789 | +1.671 | 0.0946 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **550**, R² = **0.1510**, Adj R² = **0.1336**, F-statistic = **8.70** (p = **2.89e-14**), Residual SE = **4.867** on **538** df, AIC = **3313.5**, BIC = **3365.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.6857** | 2.0793 | ±4.1586 | **+6.582** | **4.64e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4132** | 0.4453 | ±0.8906 | **-3.174** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.1317 | 0.6880 | ±1.3761 | +1.645 | 0.1000 |  |
| Site: UCSD (vs UAB) | +0.1059 | 0.5579 | ±1.1159 | +0.190 | 0.8495 |  |
| Site: UW (vs UAB) | -0.3491 | 0.4988 | ±0.9976 | -0.700 | 0.4839 |  |
| **Age (years)** | **-0.1221** | 0.0206 | ±0.0412 | **-5.931** | **3.01e-09** | *** |
| BMI (kg/m2) | +0.0396 | 0.0310 | ±0.0620 | +1.276 | 0.2020 |  |
| Hypertension | +0.2420 | 0.4641 | ±0.9282 | +0.522 | 0.6020 |  |
| High cholesterol | +0.3104 | 0.4599 | ±0.9199 | +0.675 | 0.4998 |  |
| Kidney disease | +0.6749 | 0.5723 | ±1.1446 | +1.179 | 0.2383 |  |
| **Circulatory disease** | **+1.9295** | 0.5906 | ±1.1812 | **+3.267** | **0.0011** | ** |
| Mean / SD ratio | -0.4100 | 0.2226 | ±0.4452 | -1.842 | 0.0655 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **550**, R² = **0.1473**, Adj R² = **0.1298**, F-statistic = **8.45** (p = **8.39e-14**), Residual SE = **4.878** on **538** df, AIC = **3315.9**, BIC = **3367.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.8850** | 2.0675 | ±4.1351 | **+6.232** | **4.60e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4240** | 0.4459 | ±0.8918 | **-3.193** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1388 | 0.6894 | ±1.3788 | +1.652 | 0.0986 | . |
| Site: UCSD (vs UAB) | +0.1077 | 0.5593 | ±1.1187 | +0.193 | 0.8473 |  |
| Site: UW (vs UAB) | -0.3904 | 0.4989 | ±0.9979 | -0.783 | 0.4339 |  |
| **Age (years)** | **-0.1225** | 0.0206 | ±0.0412 | **-5.940** | **2.85e-09** | *** |
| BMI (kg/m2) | +0.0406 | 0.0309 | ±0.0618 | +1.314 | 0.1890 |  |
| Hypertension | +0.2583 | 0.4654 | ±0.9309 | +0.555 | 0.5790 |  |
| High cholesterol | +0.3200 | 0.4620 | ±0.9241 | +0.693 | 0.4886 |  |
| Kidney disease | +0.7465 | 0.5724 | ±1.1449 | +1.304 | 0.1922 |  |
| **Circulatory disease** | **+1.9499** | 0.5898 | ±1.1795 | **+3.306** | **9.45e-04** | *** |
| Avg. daily mean/SD | -0.1958 | 0.1767 | ±0.3535 | -1.108 | 0.2679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **550**, R² = **0.1589**, Adj R² = **0.1417**, F-statistic = **9.24** (p = **2.94e-15**), Residual SE = **4.845** on **538** df, AIC = **3308.4**, BIC = **3360.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3389** | 2.2862 | ±4.5725 | **+3.647** | **2.65e-04** | *** |
| **Education: graduate level (vs college)** | **-1.3462** | 0.4470 | ±0.8940 | **-3.012** | **0.0026** | ** |
| Education: high school or below (vs college) | +1.0510 | 0.6749 | ±1.3497 | +1.557 | 0.1194 |  |
| Site: UCSD (vs UAB) | +0.1943 | 0.5547 | ±1.1094 | +0.350 | 0.7261 |  |
| Site: UW (vs UAB) | -0.1853 | 0.5043 | ±1.0086 | -0.367 | 0.7133 |  |
| **Age (years)** | **-0.1136** | 0.0206 | ±0.0412 | **-5.515** | **3.49e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.0308 | ±0.0616 | +1.269 | 0.2045 |  |
| Hypertension | +0.2615 | 0.4597 | ±0.9194 | +0.569 | 0.5695 |  |
| High cholesterol | +0.3540 | 0.4556 | ±0.9112 | +0.777 | 0.4372 |  |
| Kidney disease | +0.6777 | 0.5772 | ±1.1543 | +1.174 | 0.2403 |  |
| **Circulatory disease** | **+1.9165** | 0.5923 | ±1.1846 | **+3.236** | **0.0012** | ** |
| **MAG (mg/dL/h)** | **+0.0640** | 0.0236 | ±0.0473 | **+2.709** | **0.0067** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **550**, R² = **0.1497**, Adj R² = **0.1324**, F-statistic = **8.61** (p = **4.13e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.3**, BIC = **3366.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.1422** | 2.1865 | ±4.3730 | **+4.639** | **3.51e-06** | *** |
| **Education: graduate level (vs college)** | **-1.4048** | 0.4465 | ±0.8930 | **-3.146** | **0.0017** | ** |
| Education: high school or below (vs college) | +1.0464 | 0.6899 | ±1.3799 | +1.517 | 0.1293 |  |
| Site: UCSD (vs UAB) | +0.1751 | 0.5587 | ±1.1174 | +0.313 | 0.7540 |  |
| Site: UW (vs UAB) | -0.3247 | 0.5023 | ±1.0046 | -0.646 | 0.5180 |  |
| **Age (years)** | **-0.1193** | 0.0207 | ±0.0415 | **-5.753** | **8.77e-09** | *** |
| BMI (kg/m2) | +0.0388 | 0.0311 | ±0.0622 | +1.247 | 0.2124 |  |
| Hypertension | +0.2835 | 0.4618 | ±0.9235 | +0.614 | 0.5392 |  |
| High cholesterol | +0.3235 | 0.4604 | ±0.9208 | +0.703 | 0.4823 |  |
| Kidney disease | +0.6634 | 0.5881 | ±1.1761 | +1.128 | 0.2593 |  |
| **Circulatory disease** | **+1.9111** | 0.5901 | ±1.1801 | **+3.239** | **0.0012** | ** |
| Avg. daily range (mg/dL) | +0.0099 | 0.0061 | ±0.0122 | +1.631 | 0.1028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **550**, R² = **0.1662**, Adj R² = **0.1492**, F-statistic = **9.75** (p = **3.35e-16**), Residual SE = **4.823** on **538** df, AIC = **3303.5**, BIC = **3355.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4372** | 1.8811 | ±3.7622 | **+5.549** | **2.88e-08** | *** |
| **Education: graduate level (vs college)** | **-1.2881** | 0.4464 | ±0.8928 | **-2.885** | **0.0039** | ** |
| Education: high school or below (vs college) | +1.1060 | 0.6685 | ±1.3369 | +1.655 | 0.0980 | . |
| Site: UCSD (vs UAB) | +0.1919 | 0.5519 | ±1.1038 | +0.348 | 0.7280 |  |
| Site: UW (vs UAB) | -0.2243 | 0.4908 | ±0.9816 | -0.457 | 0.6476 |  |
| **Age (years)** | **-0.1136** | 0.0209 | ±0.0419 | **-5.423** | **5.86e-08** | *** |
| BMI (kg/m2) | +0.0258 | 0.0307 | ±0.0614 | +0.841 | 0.4004 |  |
| Hypertension | +0.1651 | 0.4630 | ±0.9260 | +0.357 | 0.7213 |  |
| High cholesterol | +0.3730 | 0.4545 | ±0.9090 | +0.821 | 0.4118 |  |
| Kidney disease | +0.7104 | 0.5714 | ±1.1427 | +1.243 | 0.2137 |  |
| **Circulatory disease** | **+1.7689** | 0.5828 | ±1.1656 | **+3.035** | **0.0024** | ** |
| **SD of daily means (mg/dL)** | **+0.0894** | 0.0249 | ±0.0497 | **+3.593** | **3.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **550**, R² = **0.1497**, Adj R² = **0.1323**, F-statistic = **8.61** (p = **4.19e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.3**, BIC = **3366.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.8425** | 1.9632 | ±3.9264 | **+6.542** | **6.08e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4089** | 0.4466 | ±0.8932 | **-3.155** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0571 | 0.6814 | ±1.3629 | +1.551 | 0.1208 |  |
| Site: UCSD (vs UAB) | +0.2036 | 0.5594 | ±1.1188 | +0.364 | 0.7159 |  |
| Site: UW (vs UAB) | -0.3527 | 0.5005 | ±1.0009 | -0.705 | 0.4810 |  |
| **Age (years)** | **-0.1202** | 0.0207 | ±0.0414 | **-5.811** | **6.23e-09** | *** |
| BMI (kg/m2) | +0.0324 | 0.0311 | ±0.0622 | +1.041 | 0.2979 |  |
| Hypertension | +0.2844 | 0.4622 | ±0.9244 | +0.615 | 0.5383 |  |
| High cholesterol | +0.3582 | 0.4614 | ±0.9229 | +0.776 | 0.4376 |  |
| Kidney disease | +0.7917 | 0.5765 | ±1.1529 | +1.373 | 0.1696 |  |
| **Circulatory disease** | **+1.9006** | 0.5847 | ±1.1694 | **+3.251** | **0.0012** | ** |
| Time in range 70-180, pooled (%) | -0.0138 | 0.0087 | ±0.0174 | -1.586 | 0.1128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **550**, R² = **0.1492**, Adj R² = **0.1318**, F-statistic = **8.57** (p = **4.88e-14**), Residual SE = **4.873** on **538** df, AIC = **3314.7**, BIC = **3366.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.7968** | 1.9724 | ±3.9449 | **+6.488** | **8.71e-11** | *** |
| **Education: graduate level (vs college)** | **-1.4138** | 0.4465 | ±0.8931 | **-3.166** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.0591 | 0.6824 | ±1.3647 | +1.552 | 0.1206 |  |
| Site: UCSD (vs UAB) | +0.2021 | 0.5595 | ±1.1191 | +0.361 | 0.7179 |  |
| Site: UW (vs UAB) | -0.3556 | 0.5002 | ±1.0005 | -0.711 | 0.4772 |  |
| **Age (years)** | **-0.1205** | 0.0207 | ±0.0414 | **-5.822** | **5.83e-09** | *** |
| BMI (kg/m2) | +0.0326 | 0.0312 | ±0.0624 | +1.044 | 0.2965 |  |
| Hypertension | +0.2848 | 0.4623 | ±0.9247 | +0.616 | 0.5379 |  |
| High cholesterol | +0.3551 | 0.4617 | ±0.9235 | +0.769 | 0.4419 |  |
| Kidney disease | +0.7890 | 0.5761 | ±1.1522 | +1.370 | 0.1708 |  |
| **Circulatory disease** | **+1.9034** | 0.5852 | ±1.1703 | **+3.253** | **0.0011** | ** |
| Avg. daily time in range 70-180 (%) | -0.0129 | 0.0087 | ±0.0174 | -1.480 | 0.1389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **550**, R² = **0.1498**, Adj R² = **0.1324**, F-statistic = **8.62** (p = **4.07e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.3**, BIC = **3366.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5721** | 1.8761 | ±3.7521 | **+6.168** | **6.90e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4396** | 0.4450 | ±0.8901 | **-3.235** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1816 | 0.6827 | ±1.3655 | +1.731 | 0.0835 | . |
| Site: UCSD (vs UAB) | +0.1753 | 0.5552 | ±1.1105 | +0.316 | 0.7522 |  |
| Site: UW (vs UAB) | -0.3597 | 0.4979 | ±0.9958 | -0.722 | 0.4701 |  |
| **Age (years)** | **-0.1193** | 0.0209 | ±0.0418 | **-5.710** | **1.13e-08** | *** |
| BMI (kg/m2) | +0.0381 | 0.0307 | ±0.0614 | +1.240 | 0.2151 |  |
| Hypertension | +0.1884 | 0.4672 | ±0.9345 | +0.403 | 0.6867 |  |
| High cholesterol | +0.3781 | 0.4610 | ±0.9219 | +0.820 | 0.4121 |  |
| Kidney disease | +0.8130 | 0.5668 | ±1.1335 | +1.434 | 0.1514 |  |
| **Circulatory disease** | **+1.8946** | 0.5939 | ±1.1879 | **+3.190** | **0.0014** | ** |
| Any reading < 54 during wear (0/1) | +0.8680 | 0.5149 | ±1.0298 | +1.686 | 0.0918 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **550**, R² = **0.1464**, Adj R² = **0.1289**, F-statistic = **8.39** (p = **1.08e-13**), Residual SE = **4.881** on **538** df, AIC = **3316.5**, BIC = **3368.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8741** | 1.8817 | ±3.7634 | **+6.310** | **2.78e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4249** | 0.4459 | ±0.8918 | **-3.196** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1814 | 0.6845 | ±1.3690 | +1.726 | 0.0844 | . |
| Site: UCSD (vs UAB) | +0.1550 | 0.5594 | ±1.1189 | +0.277 | 0.7817 |  |
| Site: UW (vs UAB) | -0.3680 | 0.5000 | ±0.9999 | -0.736 | 0.4617 |  |
| **Age (years)** | **-0.1221** | 0.0207 | ±0.0414 | **-5.898** | **3.67e-09** | *** |
| BMI (kg/m2) | +0.0378 | 0.0312 | ±0.0624 | +1.211 | 0.2259 |  |
| Hypertension | +0.2224 | 0.4686 | ±0.9372 | +0.475 | 0.6351 |  |
| High cholesterol | +0.3556 | 0.4646 | ±0.9293 | +0.765 | 0.4441 |  |
| Kidney disease | +0.8244 | 0.5690 | ±1.1381 | +1.449 | 0.1474 |  |
| **Circulatory disease** | **+1.9770** | 0.5873 | ±1.1745 | **+3.366** | **7.61e-04** | *** |
| Time < 54 (%) | +0.6991 | 0.9768 | ±1.9536 | +0.716 | 0.4742 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **550**, R² = **0.1475**, Adj R² = **0.1301**, F-statistic = **8.46** (p = **7.78e-14**), Residual SE = **4.877** on **538** df, AIC = **3315.7**, BIC = **3367.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8857** | 1.8780 | ±3.7560 | **+6.329** | **2.47e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4253** | 0.4459 | ±0.8918 | **-3.196** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.1882 | 0.6849 | ±1.3697 | +1.735 | 0.0827 | . |
| Site: UCSD (vs UAB) | +0.1589 | 0.5600 | ±1.1200 | +0.284 | 0.7766 |  |
| Site: UW (vs UAB) | -0.3616 | 0.5000 | ±1.0001 | -0.723 | 0.4696 |  |
| **Age (years)** | **-0.1220** | 0.0207 | ±0.0414 | **-5.891** | **3.85e-09** | *** |
| BMI (kg/m2) | +0.0372 | 0.0311 | ±0.0622 | +1.194 | 0.2323 |  |
| Hypertension | +0.2238 | 0.4657 | ±0.9314 | +0.481 | 0.6308 |  |
| High cholesterol | +0.3631 | 0.4631 | ±0.9263 | +0.784 | 0.4330 |  |
| Kidney disease | +0.8127 | 0.5701 | ±1.1402 | +1.426 | 0.1540 |  |
| **Circulatory disease** | **+1.9754** | 0.5878 | ±1.1755 | **+3.361** | **7.77e-04** | *** |
| Avg. daily time < 54 (%) | +0.7242 | 0.9502 | ±1.9004 | +0.762 | 0.4459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **550**, R² = **0.1506**, Adj R² = **0.1332**, F-statistic = **8.67** (p = **3.21e-14**), Residual SE = **4.868** on **538** df, AIC = **3313.7**, BIC = **3365.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7333** | 1.8731 | ±3.7463 | **+6.264** | **3.75e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4183** | 0.4469 | ±0.8938 | **-3.174** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.1713 | 0.6855 | ±1.3711 | +1.709 | 0.0875 | . |
| Site: UCSD (vs UAB) | +0.2170 | 0.5592 | ±1.1184 | +0.388 | 0.6980 |  |
| Site: UW (vs UAB) | -0.3191 | 0.5024 | ±1.0049 | -0.635 | 0.5254 |  |
| **Age (years)** | **-0.1229** | 0.0207 | ±0.0414 | **-5.929** | **3.06e-09** | *** |
| BMI (kg/m2) | +0.0397 | 0.0311 | ±0.0622 | +1.277 | 0.2016 |  |
| Hypertension | +0.1879 | 0.4642 | ±0.9284 | +0.405 | 0.6856 |  |
| High cholesterol | +0.3981 | 0.4635 | ±0.9270 | +0.859 | 0.3904 |  |
| Kidney disease | +0.7841 | 0.5700 | ±1.1400 | +1.376 | 0.1689 |  |
| **Circulatory disease** | **+2.0010** | 0.5930 | ±1.1860 | **+3.374** | **7.40e-04** | *** |
| Time 54-69, pooled (%) | +0.4327 | 0.2659 | ±0.5317 | +1.627 | 0.1037 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **550**, R² = **0.1530**, Adj R² = **0.1357**, F-statistic = **8.83** (p = **1.62e-14**), Residual SE = **4.862** on **538** df, AIC = **3312.2**, BIC = **3363.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7656** | 1.8732 | ±3.7465 | **+6.281** | **3.37e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4047** | 0.4456 | ±0.8913 | **-3.152** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.1832 | 0.6854 | ±1.3709 | +1.726 | 0.0843 | . |
| Site: UCSD (vs UAB) | +0.2363 | 0.5593 | ±1.1186 | +0.423 | 0.6726 |  |
| Site: UW (vs UAB) | -0.2869 | 0.5005 | ±1.0011 | -0.573 | 0.5665 |  |
| **Age (years)** | **-0.1235** | 0.0207 | ±0.0414 | **-5.960** | **2.52e-09** | *** |
| BMI (kg/m2) | +0.0388 | 0.0311 | ±0.0623 | +1.247 | 0.2122 |  |
| Hypertension | +0.1698 | 0.4635 | ±0.9270 | +0.366 | 0.7142 |  |
| High cholesterol | +0.4182 | 0.4613 | ±0.9225 | +0.907 | 0.3646 |  |
| Kidney disease | +0.7813 | 0.5678 | ±1.1357 | +1.376 | 0.1688 |  |
| **Circulatory disease** | **+2.0217** | 0.5914 | ±1.1828 | **+3.419** | **6.30e-04** | *** |
| **Avg. daily time 54-69 (%)** | **+0.4969** | 0.2172 | ±0.4343 | **+2.288** | **0.0221** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **550**, R² = **0.1501**, Adj R² = **0.1327**, F-statistic = **8.64** (p = **3.73e-14**), Residual SE = **4.870** on **538** df, AIC = **3314.1**, BIC = **3365.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7423** | 1.8775 | ±3.7550 | **+6.254** | **4.00e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4157** | 0.4464 | ±0.8928 | **-3.171** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.1797 | 0.6854 | ±1.3708 | +1.721 | 0.0852 | . |
| Site: UCSD (vs UAB) | +0.2160 | 0.5589 | ±1.1179 | +0.386 | 0.6992 |  |
| Site: UW (vs UAB) | -0.3145 | 0.5017 | ±1.0033 | -0.627 | 0.5307 |  |
| **Age (years)** | **-0.1228** | 0.0207 | ±0.0414 | **-5.925** | **3.13e-09** | *** |
| BMI (kg/m2) | +0.0393 | 0.0312 | ±0.0624 | +1.261 | 0.2072 |  |
| Hypertension | +0.1816 | 0.4654 | ±0.9308 | +0.390 | 0.6964 |  |
| High cholesterol | +0.3995 | 0.4641 | ±0.9282 | +0.861 | 0.3894 |  |
| Kidney disease | +0.7901 | 0.5702 | ±1.1404 | +1.386 | 0.1658 |  |
| **Circulatory disease** | **+2.0048** | 0.5913 | ±1.1825 | **+3.391** | **6.97e-04** | *** |
| Time < 70 (%) | +0.3467 | 0.2163 | ±0.4325 | +1.603 | 0.1089 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **550**, R² = **0.1522**, Adj R² = **0.1349**, F-statistic = **8.78** (p = **2.01e-14**), Residual SE = **4.864** on **538** df, AIC = **3312.7**, BIC = **3364.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7814** | 1.8767 | ±3.7533 | **+6.278** | **3.43e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4063** | 0.4455 | ±0.8910 | **-3.157** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.1920 | 0.6852 | ±1.3704 | +1.740 | 0.0819 | . |
| Site: UCSD (vs UAB) | +0.2284 | 0.5590 | ±1.1180 | +0.408 | 0.6829 |  |
| Site: UW (vs UAB) | -0.2908 | 0.5000 | ±0.9999 | -0.582 | 0.5608 |  |
| **Age (years)** | **-0.1232** | 0.0207 | ±0.0414 | **-5.945** | **2.77e-09** | *** |
| BMI (kg/m2) | +0.0383 | 0.0312 | ±0.0624 | +1.227 | 0.2199 |  |
| Hypertension | +0.1717 | 0.4641 | ±0.9283 | +0.370 | 0.7115 |  |
| High cholesterol | +0.4154 | 0.4622 | ±0.9244 | +0.899 | 0.3688 |  |
| Kidney disease | +0.7842 | 0.5684 | ±1.1368 | +1.380 | 0.1677 |  |
| **Circulatory disease** | **+2.0175** | 0.5902 | ±1.1805 | **+3.418** | **6.31e-04** | *** |
| **Avg. daily time < 70 (%)** | **+0.3737** | 0.1632 | ±0.3264 | **+2.290** | **0.0220** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **550**, R² = **0.1496**, Adj R² = **0.1322**, F-statistic = **8.60** (p = **4.31e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.4**, BIC = **3366.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.4986** | 2.1956 | ±4.3911 | **+6.148** | **7.84e-10** | *** |
| **Education: graduate level (vs college)** | **-1.3811** | 0.4474 | ±0.8948 | **-3.087** | **0.0020** | ** |
| Education: high school or below (vs college) | +1.0730 | 0.6790 | ±1.3579 | +1.580 | 0.1140 |  |
| Site: UCSD (vs UAB) | +0.1856 | 0.5580 | ±1.1159 | +0.333 | 0.7394 |  |
| Site: UW (vs UAB) | -0.3262 | 0.5051 | ±1.0102 | -0.646 | 0.5184 |  |
| **Age (years)** | **-0.1183** | 0.0208 | ±0.0415 | **-5.701** | **1.19e-08** | *** |
| BMI (kg/m2) | +0.0348 | 0.0313 | ±0.0627 | +1.111 | 0.2667 |  |
| Hypertension | +0.2409 | 0.4629 | ±0.9258 | +0.520 | 0.6028 |  |
| High cholesterol | +0.3422 | 0.4614 | ±0.9228 | +0.742 | 0.4582 |  |
| Kidney disease | +0.7919 | 0.5739 | ±1.1478 | +1.380 | 0.1676 |  |
| **Circulatory disease** | **+1.9147** | 0.5885 | ±1.1770 | **+3.253** | **0.0011** | ** |
| Time 54-250, pooled (%) | -0.0193 | 0.0142 | ±0.0284 | -1.361 | 0.1736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **550**, R² = **0.1488**, Adj R² = **0.1314**, F-statistic = **8.55** (p = **5.35e-14**), Residual SE = **4.873** on **538** df, AIC = **3314.9**, BIC = **3366.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.3988** | 2.2272 | ±4.4543 | **+6.016** | **1.79e-09** | *** |
| **Education: graduate level (vs college)** | **-1.3866** | 0.4473 | ±0.8946 | **-3.100** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.0813 | 0.6795 | ±1.3590 | +1.591 | 0.1116 |  |
| Site: UCSD (vs UAB) | +0.1804 | 0.5586 | ±1.1171 | +0.323 | 0.7467 |  |
| Site: UW (vs UAB) | -0.3369 | 0.5048 | ±1.0095 | -0.667 | 0.5045 |  |
| **Age (years)** | **-0.1190** | 0.0207 | ±0.0415 | **-5.739** | **9.50e-09** | *** |
| BMI (kg/m2) | +0.0350 | 0.0314 | ±0.0627 | +1.116 | 0.2644 |  |
| Hypertension | +0.2456 | 0.4632 | ±0.9264 | +0.530 | 0.5959 |  |
| High cholesterol | +0.3403 | 0.4619 | ±0.9238 | +0.737 | 0.4613 |  |
| Kidney disease | +0.7902 | 0.5738 | ±1.1475 | +1.377 | 0.1684 |  |
| **Circulatory disease** | **+1.9149** | 0.5888 | ±1.1775 | **+3.252** | **0.0011** | ** |
| Avg. daily time 54-250 (%) | -0.0177 | 0.0145 | ±0.0289 | -1.225 | 0.2204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **550**, R² = **0.1462**, Adj R² = **0.1287**, F-statistic = **8.37** (p = **1.14e-13**), Residual SE = **4.881** on **538** df, AIC = **3316.6**, BIC = **3368.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7737** | 1.8828 | ±3.7657 | **+6.253** | **4.02e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4481** | 0.4464 | ±0.8929 | **-3.244** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1270 | 0.6884 | ±1.3767 | +1.637 | 0.1016 |  |
| Site: UCSD (vs UAB) | +0.1445 | 0.5623 | ±1.1245 | +0.257 | 0.7972 |  |
| Site: UW (vs UAB) | -0.4193 | 0.4979 | ±0.9959 | -0.842 | 0.3997 |  |
| **Age (years)** | **-0.1226** | 0.0207 | ±0.0414 | **-5.918** | **3.25e-09** | *** |
| BMI (kg/m2) | +0.0351 | 0.0310 | ±0.0620 | +1.133 | 0.2573 |  |
| Hypertension | +0.2978 | 0.4647 | ±0.9294 | +0.641 | 0.5217 |  |
| High cholesterol | +0.3380 | 0.4623 | ±0.9247 | +0.731 | 0.4648 |  |
| Kidney disease | +0.8232 | 0.5715 | ±1.1430 | +1.440 | 0.1498 |  |
| **Circulatory disease** | **+1.9280** | 0.5836 | ±1.1673 | **+3.303** | **9.55e-04** | *** |
| Time 181-250, pooled (%) | +0.0111 | 0.0141 | ±0.0282 | +0.785 | 0.4322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **550**, R² = **0.1462**, Adj R² = **0.1287**, F-statistic = **8.37** (p = **1.14e-13**), Residual SE = **4.881** on **538** df, AIC = **3316.6**, BIC = **3368.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7720** | 1.8831 | ±3.7663 | **+6.251** | **4.07e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4501** | 0.4466 | ±0.8932 | **-3.247** | **0.0012** | ** |
| Education: high school or below (vs college) | +1.1226 | 0.6894 | ±1.3788 | +1.628 | 0.1034 |  |
| Site: UCSD (vs UAB) | +0.1472 | 0.5618 | ±1.1237 | +0.262 | 0.7933 |  |
| Site: UW (vs UAB) | -0.4164 | 0.4981 | ±0.9962 | -0.836 | 0.4032 |  |
| **Age (years)** | **-0.1225** | 0.0207 | ±0.0414 | **-5.913** | **3.35e-09** | *** |
| BMI (kg/m2) | +0.0350 | 0.0310 | ±0.0620 | +1.130 | 0.2587 |  |
| Hypertension | +0.2969 | 0.4639 | ±0.9279 | +0.640 | 0.5222 |  |
| High cholesterol | +0.3370 | 0.4623 | ±0.9247 | +0.729 | 0.4660 |  |
| Kidney disease | +0.8217 | 0.5716 | ±1.1432 | +1.438 | 0.1505 |  |
| **Circulatory disease** | **+1.9293** | 0.5842 | ±1.1684 | **+3.302** | **9.59e-04** | *** |
| Avg. daily time 181-250 (%) | +0.0108 | 0.0139 | ±0.0277 | +0.780 | 0.4352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **550**, R² = **0.1492**, Adj R² = **0.1319**, F-statistic = **8.58** (p = **4.75e-14**), Residual SE = **4.872** on **538** df, AIC = **3314.6**, BIC = **3366.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4960** | 1.8913 | ±3.7827 | **+6.078** | **1.22e-09** | *** |
| **Education: graduate level (vs college)** | **-1.4115** | 0.4466 | ±0.8933 | **-3.160** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.0623 | 0.6814 | ±1.3627 | +1.559 | 0.1190 |  |
| Site: UCSD (vs UAB) | +0.1949 | 0.5597 | ±1.1193 | +0.348 | 0.7277 |  |
| Site: UW (vs UAB) | -0.3602 | 0.5004 | ±1.0007 | -0.720 | 0.4717 |  |
| **Age (years)** | **-0.1203** | 0.0207 | ±0.0414 | **-5.815** | **6.05e-09** | *** |
| BMI (kg/m2) | +0.0326 | 0.0311 | ±0.0622 | +1.049 | 0.2940 |  |
| Hypertension | +0.2866 | 0.4624 | ±0.9249 | +0.620 | 0.5354 |  |
| High cholesterol | +0.3533 | 0.4615 | ±0.9230 | +0.766 | 0.4440 |  |
| Kidney disease | +0.7955 | 0.5759 | ±1.1518 | +1.381 | 0.1672 |  |
| **Circulatory disease** | **+1.9013** | 0.5846 | ±1.1693 | **+3.252** | **0.0011** | ** |
| Time > 180 (%) | +0.0130 | 0.0086 | ±0.0173 | +1.506 | 0.1320 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **550**, R² = **0.1486**, Adj R² = **0.1312**, F-statistic = **8.54** (p = **5.65e-14**), Residual SE = **4.874** on **538** df, AIC = **3315.0**, BIC = **3366.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5472** | 1.8896 | ±3.7792 | **+6.111** | **9.91e-10** | *** |
| **Education: graduate level (vs college)** | **-1.4166** | 0.4466 | ±0.8932 | **-3.172** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.0655 | 0.6823 | ±1.3646 | +1.562 | 0.1184 |  |
| Site: UCSD (vs UAB) | +0.1923 | 0.5598 | ±1.1196 | +0.344 | 0.7312 |  |
| Site: UW (vs UAB) | -0.3641 | 0.5002 | ±1.0003 | -0.728 | 0.4667 |  |
| **Age (years)** | **-0.1205** | 0.0207 | ±0.0414 | **-5.826** | **5.66e-09** | *** |
| BMI (kg/m2) | +0.0329 | 0.0312 | ±0.0624 | +1.056 | 0.2910 |  |
| Hypertension | +0.2865 | 0.4626 | ±0.9252 | +0.619 | 0.5357 |  |
| High cholesterol | +0.3497 | 0.4619 | ±0.9237 | +0.757 | 0.4490 |  |
| Kidney disease | +0.7936 | 0.5755 | ±1.1510 | +1.379 | 0.1679 |  |
| **Circulatory disease** | **+1.9045** | 0.5851 | ±1.1702 | **+3.255** | **0.0011** | ** |
| Avg. daily time > 180 (%) | +0.0119 | 0.0086 | ±0.0173 | +1.381 | 0.1674 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **550**, R² = **0.1504**, Adj R² = **0.1331**, F-statistic = **8.66** (p = **3.39e-14**), Residual SE = **4.869** on **538** df, AIC = **3313.8**, BIC = **3365.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5597** | 1.8788 | ±3.7577 | **+6.153** | **7.63e-10** | *** |
| **Education: graduate level (vs college)** | **-1.3807** | 0.4479 | ±0.8958 | **-3.082** | **0.0021** | ** |
| Education: high school or below (vs college) | +1.0689 | 0.6792 | ±1.3584 | +1.574 | 0.1155 |  |
| Site: UCSD (vs UAB) | +0.2176 | 0.5574 | ±1.1149 | +0.390 | 0.6963 |  |
| Site: UW (vs UAB) | -0.3729 | 0.4992 | ±0.9985 | -0.747 | 0.4551 |  |
| **Age (years)** | **-0.1187** | 0.0208 | ±0.0415 | **-5.718** | **1.08e-08** | *** |
| BMI (kg/m2) | +0.0294 | 0.0314 | ±0.0628 | +0.936 | 0.3493 |  |
| Hypertension | +0.2890 | 0.4619 | ±0.9239 | +0.626 | 0.5315 |  |
| High cholesterol | +0.3704 | 0.4608 | ±0.9217 | +0.804 | 0.4216 |  |
| Kidney disease | +0.7960 | 0.5745 | ±1.1491 | +1.386 | 0.1659 |  |
| **Circulatory disease** | **+1.8924** | 0.5846 | ±1.1693 | **+3.237** | **0.0012** | ** |
| Nocturnal time > 180 (%) | +0.0131 | 0.0075 | ±0.0150 | +1.742 | 0.0815 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **550**, R² = **0.1495**, Adj R² = **0.1321**, F-statistic = **8.60** (p = **4.39e-14**), Residual SE = **4.871** on **538** df, AIC = **3314.4**, BIC = **3366.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5717** | 1.8961 | ±3.7923 | **+6.103** | **1.04e-09** | *** |
| **Education: graduate level (vs college)** | **-1.3819** | 0.4474 | ±0.8947 | **-3.089** | **0.0020** | ** |
| Education: high school or below (vs college) | +1.0731 | 0.6789 | ±1.3579 | +1.581 | 0.1140 |  |
| Site: UCSD (vs UAB) | +0.1840 | 0.5580 | ±1.1160 | +0.330 | 0.7416 |  |
| Site: UW (vs UAB) | -0.3282 | 0.5049 | ±1.0099 | -0.650 | 0.5157 |  |
| **Age (years)** | **-0.1183** | 0.0208 | ±0.0415 | **-5.702** | **1.18e-08** | *** |
| BMI (kg/m2) | +0.0348 | 0.0313 | ±0.0627 | +1.112 | 0.2663 |  |
| Hypertension | +0.2423 | 0.4629 | ±0.9258 | +0.523 | 0.6007 |  |
| High cholesterol | +0.3412 | 0.4614 | ±0.9227 | +0.739 | 0.4596 |  |
| Kidney disease | +0.7924 | 0.5738 | ±1.1476 | +1.381 | 0.1673 |  |
| **Circulatory disease** | **+1.9141** | 0.5885 | ±1.1771 | **+3.252** | **0.0011** | ** |
| Time > 250 (%) | +0.0192 | 0.0142 | ±0.0284 | +1.352 | 0.1765 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **550**, R² = **0.1487**, Adj R² = **0.1313**, F-statistic = **8.54** (p = **5.52e-14**), Residual SE = **4.874** on **538** df, AIC = **3314.9**, BIC = **3366.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6338** | 1.8932 | ±3.7864 | **+6.145** | **8.00e-10** | *** |
| **Education: graduate level (vs college)** | **-1.3877** | 0.4473 | ±0.8946 | **-3.102** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.0818 | 0.6795 | ±1.3590 | +1.592 | 0.1114 |  |
| Site: UCSD (vs UAB) | +0.1784 | 0.5586 | ±1.1172 | +0.319 | 0.7494 |  |
| Site: UW (vs UAB) | -0.3395 | 0.5046 | ±1.0092 | -0.673 | 0.5011 |  |
| **Age (years)** | **-0.1190** | 0.0207 | ±0.0415 | **-5.742** | **9.35e-09** | *** |
| BMI (kg/m2) | +0.0351 | 0.0314 | ±0.0627 | +1.118 | 0.2635 |  |
| Hypertension | +0.2470 | 0.4632 | ±0.9265 | +0.533 | 0.5939 |  |
| High cholesterol | +0.3390 | 0.4619 | ±0.9238 | +0.734 | 0.4629 |  |
| Kidney disease | +0.7913 | 0.5736 | ±1.1472 | +1.380 | 0.1677 |  |
| **Circulatory disease** | **+1.9148** | 0.5888 | ±1.1776 | **+3.252** | **0.0011** | ** |
| Avg. daily time > 250 (%) | +0.0174 | 0.0144 | ±0.0289 | +1.208 | 0.2272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 550; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0836**, LLR χ² = **47.80** (p = **6.76e-07**), AUC = **0.6958**, AIC = **546.1**, BIC = **593.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3288 | 0.9419 | ±1.8838 | +0.349 | 0.7270 | 1.3893 |  |
| Education: graduate level (vs college) | -0.4556 | 0.2774 | ±0.5549 | -1.642 | 0.1005 | 0.6341 |  |
| Education: high school or below (vs college) | +0.1559 | 0.2820 | ±0.5640 | +0.553 | 0.5803 | 1.1688 |  |
| Site: UCSD (vs UAB) | -0.1128 | 0.2777 | ±0.5555 | -0.406 | 0.6847 | 0.8933 |  |
| Site: UW (vs UAB) | -0.1774 | 0.2676 | ±0.5353 | -0.663 | 0.5075 | 0.8375 |  |
| **Age (years)** | **-0.0454** | 0.0117 | ±0.0234 | **-3.882** | **1.04e-04** | 0.9556 | *** |
| BMI (kg/m2) | +0.0241 | 0.0147 | ±0.0294 | +1.639 | 0.1012 | 1.0243 |  |
| Hypertension | +0.2948 | 0.2627 | ±0.5254 | +1.122 | 0.2618 | 1.3428 |  |
| High cholesterol | +0.2010 | 0.2431 | ±0.4862 | +0.827 | 0.4084 | 1.2226 |  |
| Kidney disease | +0.3505 | 0.2689 | ±0.5379 | +1.303 | 0.1925 | 1.4198 |  |
| **Circulatory disease** | **+0.7290** | 0.2578 | ±0.5157 | **+2.827** | **0.0047** | 2.0729 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0931**, LLR χ² = **53.24** (p = **1.62e-07**), AUC = **0.7067**, AIC = **542.7**, BIC = **594.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9497 | 1.0962 | ±2.1924 | -0.866 | 0.3863 | 0.3869 |  |
| Education: graduate level (vs college) | -0.4142 | 0.2790 | ±0.5580 | -1.485 | 0.1376 | 0.6609 |  |
| Education: high school or below (vs college) | +0.0746 | 0.2878 | ±0.5757 | +0.259 | 0.7956 | 1.0774 |  |
| Site: UCSD (vs UAB) | -0.0649 | 0.2810 | ±0.5619 | -0.231 | 0.8174 | 0.9372 |  |
| Site: UW (vs UAB) | -0.1024 | 0.2713 | ±0.5426 | -0.377 | 0.7058 | 0.9027 |  |
| **Age (years)** | **-0.0431** | 0.0118 | ±0.0236 | **-3.658** | **2.54e-04** | 0.9578 | *** |
| BMI (kg/m2) | +0.0202 | 0.0149 | ±0.0297 | +1.362 | 0.1732 | 1.0204 |  |
| Hypertension | +0.2842 | 0.2650 | ±0.5300 | +1.073 | 0.2834 | 1.3288 |  |
| High cholesterol | +0.1986 | 0.2445 | ±0.4889 | +0.812 | 0.4165 | 1.2197 |  |
| Kidney disease | +0.3789 | 0.2706 | ±0.5412 | +1.400 | 0.1615 | 1.4607 |  |
| **Circulatory disease** | **+0.7218** | 0.2589 | ±0.5177 | **+2.788** | **0.0053** | 2.0581 | ** |
| **HbA1c (%)** | **+0.1702** | 0.0723 | ±0.1446 | **+2.355** | **0.0185** | 1.1856 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0869**, LLR χ² = **49.68** (p = **7.14e-07**), AUC = **0.7016**, AIC = **546.2**, BIC = **597.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3288 | 1.0572 | ±2.1144 | -0.311 | 0.7558 | 0.7198 |  |
| Education: graduate level (vs college) | -0.4295 | 0.2784 | ±0.5568 | -1.543 | 0.1229 | 0.6508 |  |
| Education: high school or below (vs college) | +0.1184 | 0.2846 | ±0.5691 | +0.416 | 0.6774 | 1.1257 |  |
| Site: UCSD (vs UAB) | -0.0778 | 0.2796 | ±0.5591 | -0.278 | 0.7809 | 0.9252 |  |
| Site: UW (vs UAB) | -0.1404 | 0.2696 | ±0.5392 | -0.521 | 0.6025 | 0.8690 |  |
| **Age (years)** | **-0.0439** | 0.0117 | ±0.0234 | **-3.746** | **1.80e-04** | 0.9570 | *** |
| BMI (kg/m2) | +0.0227 | 0.0148 | ±0.0295 | +1.535 | 0.1248 | 1.0229 |  |
| Hypertension | +0.2929 | 0.2633 | ±0.5266 | +1.113 | 0.2659 | 1.3404 |  |
| High cholesterol | +0.2035 | 0.2435 | ±0.4870 | +0.836 | 0.4034 | 1.2256 |  |
| Kidney disease | +0.3483 | 0.2694 | ±0.5387 | +1.293 | 0.1959 | 1.4167 |  |
| **Circulatory disease** | **+0.7155** | 0.2579 | ±0.5159 | **+2.774** | **0.0055** | 2.0452 | ** |
| Mean glucose (mg/dL) | +0.0034 | 0.0025 | ±0.0049 | +1.382 | 0.1669 | 1.0034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0869**, LLR χ² = **49.68** (p = **7.14e-07**), AUC = **0.7016**, AIC = **546.2**, BIC = **597.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8010 | 1.2494 | ±2.4987 | -0.641 | 0.5214 | 0.4489 |  |
| Education: graduate level (vs college) | -0.4295 | 0.2784 | ±0.5568 | -1.543 | 0.1229 | 0.6508 |  |
| Education: high school or below (vs college) | +0.1184 | 0.2846 | ±0.5691 | +0.416 | 0.6774 | 1.1257 |  |
| Site: UCSD (vs UAB) | -0.0778 | 0.2796 | ±0.5591 | -0.278 | 0.7809 | 0.9252 |  |
| Site: UW (vs UAB) | -0.1404 | 0.2696 | ±0.5392 | -0.521 | 0.6025 | 0.8690 |  |
| **Age (years)** | **-0.0439** | 0.0117 | ±0.0234 | **-3.746** | **1.80e-04** | 0.9570 | *** |
| BMI (kg/m2) | +0.0227 | 0.0148 | ±0.0295 | +1.535 | 0.1248 | 1.0229 |  |
| Hypertension | +0.2929 | 0.2633 | ±0.5266 | +1.113 | 0.2659 | 1.3404 |  |
| High cholesterol | +0.2035 | 0.2435 | ±0.4870 | +0.836 | 0.4034 | 1.2256 |  |
| Kidney disease | +0.3483 | 0.2694 | ±0.5387 | +1.293 | 0.1959 | 1.4167 |  |
| **Circulatory disease** | **+0.7155** | 0.2579 | ±0.5159 | **+2.774** | **0.0055** | 2.0452 | ** |
| GMI (%) | +0.1427 | 0.1032 | ±0.2064 | +1.382 | 0.1669 | 1.1533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0901**, LLR χ² = **51.53** (p = **3.31e-07**), AUC = **0.7067**, AIC = **544.4**, BIC = **596.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5122 | 1.0387 | ±2.0774 | -0.493 | 0.6219 | 0.5992 |  |
| Education: graduate level (vs college) | -0.4077 | 0.2792 | ±0.5585 | -1.460 | 0.1443 | 0.6652 |  |
| Education: high school or below (vs college) | +0.1152 | 0.2850 | ±0.5699 | +0.404 | 0.6861 | 1.1221 |  |
| Site: UCSD (vs UAB) | -0.0601 | 0.2804 | ±0.5607 | -0.214 | 0.8304 | 0.9417 |  |
| Site: UW (vs UAB) | -0.1462 | 0.2693 | ±0.5387 | -0.543 | 0.5873 | 0.8640 |  |
| **Age (years)** | **-0.0430** | 0.0117 | ±0.0235 | **-3.658** | **2.54e-04** | 0.9579 | *** |
| BMI (kg/m2) | +0.0211 | 0.0148 | ±0.0297 | +1.426 | 0.1540 | 1.0214 |  |
| Hypertension | +0.2986 | 0.2640 | ±0.5280 | +1.131 | 0.2580 | 1.3480 |  |
| High cholesterol | +0.2112 | 0.2443 | ±0.4887 | +0.865 | 0.3873 | 1.2352 |  |
| Kidney disease | +0.3606 | 0.2698 | ±0.5396 | +1.336 | 0.1814 | 1.4341 |  |
| **Circulatory disease** | **+0.7123** | 0.2582 | ±0.5164 | **+2.759** | **0.0058** | 2.0387 | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0045 | 0.0023 | ±0.0046 | +1.946 | 0.0516 | 1.0045 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0994**, LLR χ² = **56.85** (p = **3.55e-08**), AUC = **0.7135**, AIC = **539.1**, BIC = **590.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8584 | 1.0269 | ±2.0537 | -0.836 | 0.4032 | 0.4238 |  |
| Education: graduate level (vs college) | -0.4000 | 0.2804 | ±0.5608 | -1.427 | 0.1537 | 0.6703 |  |
| Education: high school or below (vs college) | +0.0679 | 0.2875 | ±0.5749 | +0.236 | 0.8133 | 1.0702 |  |
| Site: UCSD (vs UAB) | -0.0919 | 0.2812 | ±0.5623 | -0.327 | 0.7438 | 0.9122 |  |
| Site: UW (vs UAB) | -0.0738 | 0.2720 | ±0.5440 | -0.271 | 0.7861 | 0.9288 |  |
| **Age (years)** | **-0.0433** | 0.0117 | ±0.0234 | **-3.701** | **2.15e-04** | 0.9576 | *** |
| BMI (kg/m2) | +0.0218 | 0.0149 | ±0.0297 | +1.469 | 0.1419 | 1.0221 |  |
| Hypertension | +0.2837 | 0.2654 | ±0.5309 | +1.069 | 0.2852 | 1.3280 |  |
| High cholesterol | +0.2229 | 0.2455 | ±0.4911 | +0.908 | 0.3639 | 1.2497 |  |
| Kidney disease | +0.2061 | 0.2766 | ±0.5531 | +0.745 | 0.4561 | 1.2289 |  |
| **Circulatory disease** | **+0.7205** | 0.2600 | ±0.5201 | **+2.771** | **0.0056** | 2.0554 | ** |
| **Glucose SD, pooled (mg/dL)** | **+0.0261** | 0.0087 | ±0.0175 | **+2.995** | **0.0027** | 1.0265 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0923**, LLR χ² = **52.77** (p = **1.97e-07**), AUC = **0.7060**, AIC = **543.1**, BIC = **594.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5850 | 1.0310 | ±2.0619 | -0.567 | 0.5704 | 0.5571 |  |
| Education: graduate level (vs college) | -0.4192 | 0.2791 | ±0.5583 | -1.502 | 0.1332 | 0.6576 |  |
| Education: high school or below (vs college) | +0.0771 | 0.2865 | ±0.5730 | +0.269 | 0.7878 | 1.0802 |  |
| Site: UCSD (vs UAB) | -0.0990 | 0.2795 | ±0.5591 | -0.354 | 0.7234 | 0.9058 |  |
| Site: UW (vs UAB) | -0.1107 | 0.2705 | ±0.5410 | -0.409 | 0.6823 | 0.8952 |  |
| **Age (years)** | **-0.0442** | 0.0117 | ±0.0234 | **-3.775** | **1.60e-04** | 0.9567 | *** |
| BMI (kg/m2) | +0.0239 | 0.0148 | ±0.0295 | +1.621 | 0.1050 | 1.0242 |  |
| Hypertension | +0.2948 | 0.2640 | ±0.5280 | +1.117 | 0.2642 | 1.3428 |  |
| High cholesterol | +0.2146 | 0.2444 | ±0.4887 | +0.878 | 0.3799 | 1.2394 |  |
| Kidney disease | +0.2317 | 0.2763 | ±0.5527 | +0.838 | 0.4018 | 1.2607 |  |
| **Circulatory disease** | **+0.7301** | 0.2590 | ±0.5179 | **+2.819** | **0.0048** | 2.0754 | ** |
| **Avg. daily SD (mg/dL)** | **+0.0222** | 0.0099 | ±0.0199 | **+2.234** | **0.0255** | 1.0224 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0908**, LLR χ² = **51.95** (p = **2.78e-07**), AUC = **0.7053**, AIC = **544.0**, BIC = **595.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6396 | 1.0546 | ±2.1091 | -0.606 | 0.5442 | 0.5275 |  |
| Education: graduate level (vs college) | -0.4459 | 0.2790 | ±0.5579 | -1.599 | 0.1099 | 0.6402 |  |
| Education: high school or below (vs college) | +0.1254 | 0.2839 | ±0.5678 | +0.442 | 0.6587 | 1.1336 |  |
| Site: UCSD (vs UAB) | -0.1322 | 0.2790 | ±0.5580 | -0.474 | 0.6355 | 0.8761 |  |
| Site: UW (vs UAB) | -0.1379 | 0.2695 | ±0.5390 | -0.512 | 0.6089 | 0.8712 |  |
| **Age (years)** | **-0.0457** | 0.0117 | ±0.0234 | **-3.902** | **9.54e-05** | 0.9553 | *** |
| BMI (kg/m2) | +0.0241 | 0.0147 | ±0.0295 | +1.638 | 0.1013 | 1.0244 |  |
| Hypertension | +0.2777 | 0.2637 | ±0.5274 | +1.053 | 0.2923 | 1.3201 |  |
| High cholesterol | +0.2134 | 0.2441 | ±0.4881 | +0.875 | 0.3818 | 1.2379 |  |
| Kidney disease | +0.2195 | 0.2790 | ±0.5579 | +0.787 | 0.4314 | 1.2454 |  |
| **Circulatory disease** | **+0.7435** | 0.2597 | ±0.5193 | **+2.863** | **0.0042** | 2.1033 | ** |
| **CV (%)** | **+0.0406** | 0.0199 | ±0.0398 | **+2.042** | **0.0411** | 1.0414 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0896**, LLR χ² = **51.26** (p = **3.71e-07**), AUC = **0.7028**, AIC = **544.6**, BIC = **596.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.2547 | 1.0758 | ±2.1515 | +1.166 | 0.2435 | 3.5067 |  |
| Education: graduate level (vs college) | -0.4428 | 0.2789 | ±0.5577 | -1.588 | 0.1123 | 0.6422 |  |
| Education: high school or below (vs college) | +0.1367 | 0.2835 | ±0.5670 | +0.482 | 0.6298 | 1.1465 |  |
| Site: UCSD (vs UAB) | -0.1409 | 0.2793 | ±0.5587 | -0.504 | 0.6140 | 0.8686 |  |
| Site: UW (vs UAB) | -0.1477 | 0.2692 | ±0.5384 | -0.549 | 0.5831 | 0.8626 |  |
| **Age (years)** | **-0.0455** | 0.0117 | ±0.0235 | **-3.877** | **1.06e-04** | 0.9555 | *** |
| BMI (kg/m2) | +0.0246 | 0.0147 | ±0.0295 | +1.667 | 0.0956 | 1.0249 | . |
| Hypertension | +0.2916 | 0.2633 | ±0.5267 | +1.107 | 0.2682 | 1.3386 |  |
| High cholesterol | +0.1978 | 0.2438 | ±0.4875 | +0.811 | 0.4172 | 1.2187 |  |
| Kidney disease | +0.2511 | 0.2761 | ±0.5522 | +0.910 | 0.3631 | 1.2855 |  |
| **Circulatory disease** | **+0.7254** | 0.2595 | ±0.5190 | **+2.795** | **0.0052** | 2.0656 | ** |
| Mean / SD ratio | -0.2158 | 0.1187 | ±0.2373 | -1.818 | 0.0690 | 0.8059 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0848**, LLR χ² = **48.52** (p = **1.15e-06**), AUC = **0.6980**, AIC = **547.4**, BIC = **599.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7054 | 1.0442 | ±2.0883 | +0.676 | 0.4993 | 2.0246 |  |
| Education: graduate level (vs college) | -0.4484 | 0.2780 | ±0.5560 | -1.613 | 0.1067 | 0.6386 |  |
| Education: high school or below (vs college) | +0.1450 | 0.2826 | ±0.5652 | +0.513 | 0.6079 | 1.1560 |  |
| Site: UCSD (vs UAB) | -0.1273 | 0.2785 | ±0.5570 | -0.457 | 0.6476 | 0.8805 |  |
| Site: UW (vs UAB) | -0.1717 | 0.2680 | ±0.5359 | -0.641 | 0.5216 | 0.8422 |  |
| **Age (years)** | **-0.0456** | 0.0117 | ±0.0234 | **-3.892** | **9.94e-05** | 0.9554 | *** |
| BMI (kg/m2) | +0.0250 | 0.0147 | ±0.0295 | +1.697 | 0.0897 | 1.0253 | . |
| Hypertension | +0.2957 | 0.2627 | ±0.5254 | +1.126 | 0.2603 | 1.3441 |  |
| High cholesterol | +0.2013 | 0.2432 | ±0.4864 | +0.828 | 0.4079 | 1.2230 |  |
| Kidney disease | +0.3088 | 0.2740 | ±0.5480 | +1.127 | 0.2597 | 1.3618 |  |
| **Circulatory disease** | **+0.7311** | 0.2585 | ±0.5169 | **+2.829** | **0.0047** | 2.0774 | ** |
| Avg. daily mean/SD | -0.0773 | 0.0919 | ±0.1839 | -0.841 | 0.4003 | 0.9256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0941**, LLR χ² = **53.80** (p = **1.28e-07**), AUC = **0.7036**, AIC = **542.1**, BIC = **593.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1730 | 1.1312 | ±2.2624 | -1.037 | 0.2998 | 0.3094 |  |
| Education: graduate level (vs college) | -0.4064 | 0.2796 | ±0.5592 | -1.454 | 0.1460 | 0.6660 |  |
| Education: high school or below (vs college) | +0.0830 | 0.2877 | ±0.5755 | +0.288 | 0.7730 | 1.0866 |  |
| Site: UCSD (vs UAB) | -0.0979 | 0.2798 | ±0.5595 | -0.350 | 0.7263 | 0.9067 |  |
| Site: UW (vs UAB) | -0.0685 | 0.2727 | ±0.5453 | -0.251 | 0.8015 | 0.9337 |  |
| **Age (years)** | **-0.0418** | 0.0118 | ±0.0237 | **-3.533** | **4.11e-04** | 0.9590 | *** |
| BMI (kg/m2) | +0.0245 | 0.0148 | ±0.0297 | +1.651 | 0.0986 | 1.0248 | . |
| Hypertension | +0.2994 | 0.2655 | ±0.5310 | +1.127 | 0.2595 | 1.3490 |  |
| High cholesterol | +0.2070 | 0.2449 | ±0.4897 | +0.845 | 0.3980 | 1.2299 |  |
| Kidney disease | +0.2908 | 0.2723 | ±0.5445 | +1.068 | 0.2855 | 1.3375 |  |
| **Circulatory disease** | **+0.7248** | 0.2596 | ±0.5192 | **+2.792** | **0.0052** | 2.0644 | ** |
| **MAG (mg/dL/h)** | **+0.0264** | 0.0108 | ±0.0215 | **+2.455** | **0.0141** | 1.0267 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0919**, LLR χ² = **52.56** (p = **2.15e-07**), AUC = **0.7053**, AIC = **543.3**, BIC = **595.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8795 | 1.0976 | ±2.1951 | -0.801 | 0.4230 | 0.4150 |  |
| Education: graduate level (vs college) | -0.4153 | 0.2791 | ±0.5582 | -1.488 | 0.1367 | 0.6601 |  |
| Education: high school or below (vs college) | +0.0718 | 0.2870 | ±0.5740 | +0.250 | 0.8026 | 1.0744 |  |
| Site: UCSD (vs UAB) | -0.0955 | 0.2793 | ±0.5587 | -0.342 | 0.7326 | 0.9090 |  |
| Site: UW (vs UAB) | -0.1190 | 0.2702 | ±0.5403 | -0.440 | 0.6597 | 0.8878 |  |
| **Age (years)** | **-0.0434** | 0.0118 | ±0.0235 | **-3.691** | **2.23e-04** | 0.9575 | *** |
| BMI (kg/m2) | +0.0246 | 0.0148 | ±0.0295 | +1.669 | 0.0951 | 1.0249 | . |
| Hypertension | +0.3120 | 0.2643 | ±0.5287 | +1.180 | 0.2379 | 1.3661 |  |
| High cholesterol | +0.2001 | 0.2442 | ±0.4884 | +0.819 | 0.4126 | 1.2215 |  |
| Kidney disease | +0.2238 | 0.2774 | ±0.5548 | +0.807 | 0.4198 | 1.2509 |  |
| **Circulatory disease** | **+0.7224** | 0.2592 | ±0.5184 | **+2.787** | **0.0053** | 2.0594 | ** |
| **Avg. daily range (mg/dL)** | **+0.0065** | 0.0030 | ±0.0060 | **+2.186** | **0.0288** | 1.0065 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.1133**, LLR χ² = **64.82** (p = **1.16e-09**), AUC = **0.7327**, AIC = **531.1**, BIC = **582.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6676 | 0.9717 | ±1.9433 | -0.687 | 0.4920 | 0.5129 |  |
| Education: graduate level (vs college) | -0.3653 | 0.2831 | ±0.5661 | -1.290 | 0.1969 | 0.6940 |  |
| Education: high school or below (vs college) | +0.1373 | 0.2886 | ±0.5773 | +0.476 | 0.6342 | 1.1472 |  |
| Site: UCSD (vs UAB) | -0.0841 | 0.2849 | ±0.5699 | -0.295 | 0.7679 | 0.9193 |  |
| Site: UW (vs UAB) | -0.0441 | 0.2739 | ±0.5478 | -0.161 | 0.8721 | 0.9569 |  |
| **Age (years)** | **-0.0399** | 0.0116 | ±0.0233 | **-3.432** | **5.99e-04** | 0.9609 | *** |
| BMI (kg/m2) | +0.0193 | 0.0151 | ±0.0301 | +1.283 | 0.1996 | 1.0195 |  |
| Hypertension | +0.2392 | 0.2689 | ±0.5378 | +0.890 | 0.3736 | 1.2703 |  |
| High cholesterol | +0.2352 | 0.2487 | ±0.4975 | +0.946 | 0.3444 | 1.2652 |  |
| Kidney disease | +0.2859 | 0.2758 | ±0.5515 | +1.037 | 0.2999 | 1.3309 |  |
| **Circulatory disease** | **+0.6489** | 0.2641 | ±0.5282 | **+2.457** | **0.0140** | 1.9135 | * |
| **SD of daily means (mg/dL)** | **+0.0494** | 0.0121 | ±0.0242 | **+4.085** | **4.40e-05** | 1.0506 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0890**, LLR χ² = **50.90** (p = **4.32e-07**), AUC = **0.7047**, AIC = **545.0**, BIC = **596.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7275 | 0.9698 | ±1.9397 | +0.750 | 0.4532 | 2.0700 |  |
| Education: graduate level (vs college) | -0.4257 | 0.2786 | ±0.5572 | -1.528 | 0.1265 | 0.6533 |  |
| Education: high school or below (vs college) | +0.1069 | 0.2849 | ±0.5699 | +0.375 | 0.7076 | 1.1128 |  |
| Site: UCSD (vs UAB) | -0.0600 | 0.2804 | ±0.5608 | -0.214 | 0.8306 | 0.9418 |  |
| Site: UW (vs UAB) | -0.1277 | 0.2701 | ±0.5402 | -0.473 | 0.6363 | 0.8801 |  |
| **Age (years)** | **-0.0438** | 0.0117 | ±0.0234 | **-3.743** | **1.82e-04** | 0.9572 | *** |
| BMI (kg/m2) | +0.0216 | 0.0148 | ±0.0296 | +1.458 | 0.1448 | 1.0218 |  |
| Hypertension | +0.3006 | 0.2638 | ±0.5276 | +1.140 | 0.2545 | 1.3507 |  |
| High cholesterol | +0.2136 | 0.2441 | ±0.4881 | +0.875 | 0.3814 | 1.2381 |  |
| Kidney disease | +0.3371 | 0.2698 | ±0.5397 | +1.249 | 0.2116 | 1.4009 |  |
| **Circulatory disease** | **+0.7101** | 0.2584 | ±0.5169 | **+2.747** | **0.0060** | 2.0341 | ** |
| Time in range 70-180, pooled (%) | -0.0072 | 0.0041 | ±0.0081 | -1.771 | 0.0765 | 0.9928 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0883**, LLR χ² = **50.51** (p = **5.07e-07**), AUC = **0.7041**, AIC = **545.4**, BIC = **597.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7133 | 0.9713 | ±1.9426 | +0.734 | 0.4627 | 2.0406 |  |
| Education: graduate level (vs college) | -0.4296 | 0.2784 | ±0.5569 | -1.543 | 0.1228 | 0.6507 |  |
| Education: high school or below (vs college) | +0.1072 | 0.2850 | ±0.5699 | +0.376 | 0.7068 | 1.1132 |  |
| Site: UCSD (vs UAB) | -0.0612 | 0.2804 | ±0.5608 | -0.218 | 0.8273 | 0.9406 |  |
| Site: UW (vs UAB) | -0.1307 | 0.2700 | ±0.5400 | -0.484 | 0.6282 | 0.8775 |  |
| **Age (years)** | **-0.0440** | 0.0117 | ±0.0234 | **-3.762** | **1.69e-04** | 0.9570 | *** |
| BMI (kg/m2) | +0.0216 | 0.0148 | ±0.0296 | +1.458 | 0.1447 | 1.0218 |  |
| Hypertension | +0.3018 | 0.2637 | ±0.5274 | +1.144 | 0.2525 | 1.3522 |  |
| High cholesterol | +0.2124 | 0.2439 | ±0.4878 | +0.871 | 0.3839 | 1.2367 |  |
| Kidney disease | +0.3352 | 0.2698 | ±0.5396 | +1.242 | 0.2141 | 1.3983 |  |
| **Circulatory disease** | **+0.7112** | 0.2583 | ±0.5167 | **+2.753** | **0.0059** | 2.0364 | ** |
| Avg. daily time in range 70-180 (%) | -0.0067 | 0.0041 | ±0.0081 | -1.657 | 0.0976 | 0.9933 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0918**, LLR χ² = **52.52** (p = **2.20e-07**), AUC = **0.7041**, AIC = **543.4**, BIC = **595.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0944 | 0.9520 | ±1.9040 | +0.099 | 0.9210 | 1.0990 |  |
| Education: graduate level (vs college) | -0.4734 | 0.2798 | ±0.5596 | -1.692 | 0.0906 | 0.6229 | . |
| Education: high school or below (vs college) | +0.1687 | 0.2832 | ±0.5663 | +0.596 | 0.5513 | 1.1838 |  |
| Site: UCSD (vs UAB) | -0.0765 | 0.2796 | ±0.5591 | -0.274 | 0.7844 | 0.9264 |  |
| Site: UW (vs UAB) | -0.1443 | 0.2696 | ±0.5391 | -0.535 | 0.5923 | 0.8656 |  |
| **Age (years)** | **-0.0437** | 0.0118 | ±0.0235 | **-3.720** | **1.99e-04** | 0.9572 | *** |
| BMI (kg/m2) | +0.0241 | 0.0147 | ±0.0295 | +1.632 | 0.1028 | 1.0244 |  |
| Hypertension | +0.2388 | 0.2651 | ±0.5302 | +0.901 | 0.3678 | 1.2697 |  |
| High cholesterol | +0.2482 | 0.2455 | ±0.4910 | +1.011 | 0.3120 | 1.2818 |  |
| Kidney disease | +0.3342 | 0.2709 | ±0.5418 | +1.234 | 0.2173 | 1.3969 |  |
| **Circulatory disease** | **+0.6934** | 0.2599 | ±0.5197 | **+2.668** | **0.0076** | 2.0005 | ** |
| **Any reading < 54 during wear (0/1)** | **+0.5481** | 0.2487 | ±0.4974 | **+2.204** | **0.0275** | 1.7299 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0861**, LLR χ² = **49.22** (p = **8.65e-07**), AUC = **0.6971**, AIC = **546.7**, BIC = **598.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2892 | 0.9436 | ±1.8873 | +0.306 | 0.7592 | 1.3354 |  |
| Education: graduate level (vs college) | -0.4472 | 0.2780 | ±0.5560 | -1.608 | 0.1077 | 0.6394 |  |
| Education: high school or below (vs college) | +0.1747 | 0.2826 | ±0.5651 | +0.618 | 0.5364 | 1.1909 |  |
| Site: UCSD (vs UAB) | -0.0893 | 0.2790 | ±0.5581 | -0.320 | 0.7490 | 0.9146 |  |
| Site: UW (vs UAB) | -0.1428 | 0.2697 | ±0.5395 | -0.529 | 0.5966 | 0.8670 |  |
| **Age (years)** | **-0.0455** | 0.0117 | ±0.0234 | **-3.889** | **1.00e-04** | 0.9555 | *** |
| BMI (kg/m2) | +0.0238 | 0.0147 | ±0.0294 | +1.622 | 0.1049 | 1.0241 |  |
| Hypertension | +0.2616 | 0.2645 | ±0.5291 | +0.989 | 0.3226 | 1.2990 |  |
| High cholesterol | +0.2242 | 0.2443 | ±0.4886 | +0.918 | 0.3587 | 1.2514 |  |
| Kidney disease | +0.3459 | 0.2693 | ±0.5386 | +1.284 | 0.1990 | 1.4132 |  |
| **Circulatory disease** | **+0.7548** | 0.2590 | ±0.5179 | **+2.915** | **0.0036** | 2.1271 | ** |
| Time < 54 (%) | +0.4642 | 0.3895 | ±0.7789 | +1.192 | 0.2333 | 1.5908 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0867**, LLR χ² = **49.56** (p = **7.52e-07**), AUC = **0.6973**, AIC = **546.4**, BIC = **598.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2988 | 0.9433 | ±1.8866 | +0.317 | 0.7515 | 1.3482 |  |
| Education: graduate level (vs college) | -0.4489 | 0.2778 | ±0.5556 | -1.616 | 0.1061 | 0.6383 |  |
| Education: high school or below (vs college) | +0.1744 | 0.2825 | ±0.5650 | +0.617 | 0.5369 | 1.1906 |  |
| Site: UCSD (vs UAB) | -0.0919 | 0.2787 | ±0.5574 | -0.330 | 0.7415 | 0.9122 |  |
| Site: UW (vs UAB) | -0.1465 | 0.2691 | ±0.5382 | -0.544 | 0.5862 | 0.8638 |  |
| **Age (years)** | **-0.0454** | 0.0117 | ±0.0234 | **-3.878** | **1.05e-04** | 0.9557 | *** |
| BMI (kg/m2) | +0.0236 | 0.0147 | ±0.0294 | +1.605 | 0.1085 | 1.0239 |  |
| Hypertension | +0.2695 | 0.2637 | ±0.5274 | +1.022 | 0.3068 | 1.3093 |  |
| High cholesterol | +0.2244 | 0.2444 | ±0.4887 | +0.918 | 0.3585 | 1.2516 |  |
| Kidney disease | +0.3396 | 0.2695 | ±0.5390 | +1.260 | 0.2077 | 1.4044 |  |
| **Circulatory disease** | **+0.7465** | 0.2583 | ±0.5165 | **+2.890** | **0.0038** | 2.1096 | ** |
| Avg. daily time < 54 (%) | +0.3815 | 0.3291 | ±0.6583 | +1.159 | 0.2464 | 1.4645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0883**, LLR χ² = **50.52** (p = **5.05e-07**), AUC = **0.7013**, AIC = **545.4**, BIC = **597.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2469 | 0.9455 | ±1.8910 | +0.261 | 0.7940 | 1.2800 |  |
| Education: graduate level (vs college) | -0.4542 | 0.2787 | ±0.5573 | -1.630 | 0.1031 | 0.6350 |  |
| Education: high school or below (vs college) | +0.1583 | 0.2829 | ±0.5658 | +0.560 | 0.5758 | 1.1715 |  |
| Site: UCSD (vs UAB) | -0.0781 | 0.2790 | ±0.5580 | -0.280 | 0.7796 | 0.9249 |  |
| Site: UW (vs UAB) | -0.1438 | 0.2697 | ±0.5394 | -0.533 | 0.5939 | 0.8661 |  |
| **Age (years)** | **-0.0459** | 0.0117 | ±0.0234 | **-3.919** | **8.88e-05** | 0.9551 | *** |
| BMI (kg/m2) | +0.0251 | 0.0147 | ±0.0294 | +1.706 | 0.0880 | 1.0254 | . |
| Hypertension | +0.2561 | 0.2640 | ±0.5280 | +0.970 | 0.3320 | 1.2919 |  |
| High cholesterol | +0.2303 | 0.2441 | ±0.4881 | +0.943 | 0.3455 | 1.2589 |  |
| Kidney disease | +0.3246 | 0.2706 | ±0.5412 | +1.200 | 0.2303 | 1.3835 |  |
| **Circulatory disease** | **+0.7582** | 0.2593 | ±0.5186 | **+2.924** | **0.0035** | 2.1343 | ** |
| Time 54-69, pooled (%) | +0.1833 | 0.1082 | ±0.2165 | +1.694 | 0.0903 | 1.2012 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0903**, LLR χ² = **51.67** (p = **3.13e-07**), AUC = **0.7010**, AIC = **544.2**, BIC = **596.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2560 | 0.9456 | ±1.8911 | +0.271 | 0.7866 | 1.2918 |  |
| Education: graduate level (vs college) | -0.4452 | 0.2786 | ±0.5572 | -1.598 | 0.1101 | 0.6407 |  |
| Education: high school or below (vs college) | +0.1648 | 0.2835 | ±0.5669 | +0.581 | 0.5610 | 1.1791 |  |
| Site: UCSD (vs UAB) | -0.0694 | 0.2794 | ±0.5588 | -0.248 | 0.8038 | 0.9329 |  |
| Site: UW (vs UAB) | -0.1274 | 0.2703 | ±0.5406 | -0.471 | 0.6375 | 0.8804 |  |
| **Age (years)** | **-0.0462** | 0.0117 | ±0.0234 | **-3.944** | **8.02e-05** | 0.9549 | *** |
| BMI (kg/m2) | +0.0247 | 0.0147 | ±0.0294 | +1.682 | 0.0926 | 1.0250 | . |
| Hypertension | +0.2474 | 0.2643 | ±0.5286 | +0.936 | 0.3493 | 1.2807 |  |
| High cholesterol | +0.2416 | 0.2448 | ±0.4897 | +0.987 | 0.3236 | 1.2733 |  |
| Kidney disease | +0.3240 | 0.2706 | ±0.5412 | +1.197 | 0.2312 | 1.3827 |  |
| **Circulatory disease** | **+0.7690** | 0.2595 | ±0.5190 | **+2.964** | **0.0030** | 2.1575 | ** |
| **Avg. daily time 54-69 (%)** | **+0.2070** | 0.1039 | ±0.2078 | **+1.992** | **0.0463** | 1.2300 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0885**, LLR χ² = **50.61** (p = **4.86e-07**), AUC = **0.7005**, AIC = **545.3**, BIC = **597.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2450 | 0.9457 | ±1.8914 | +0.259 | 0.7955 | 1.2777 |  |
| Education: graduate level (vs college) | -0.4515 | 0.2787 | ±0.5573 | -1.620 | 0.1052 | 0.6367 |  |
| Education: high school or below (vs college) | +0.1644 | 0.2829 | ±0.5658 | +0.581 | 0.5611 | 1.1787 |  |
| Site: UCSD (vs UAB) | -0.0751 | 0.2793 | ±0.5585 | -0.269 | 0.7880 | 0.9277 |  |
| Site: UW (vs UAB) | -0.1367 | 0.2700 | ±0.5400 | -0.506 | 0.6126 | 0.8722 |  |
| **Age (years)** | **-0.0459** | 0.0117 | ±0.0234 | **-3.917** | **8.97e-05** | 0.9552 | *** |
| BMI (kg/m2) | +0.0248 | 0.0147 | ±0.0294 | +1.691 | 0.0909 | 1.0252 | . |
| Hypertension | +0.2500 | 0.2644 | ±0.5288 | +0.945 | 0.3445 | 1.2840 |  |
| High cholesterol | +0.2340 | 0.2443 | ±0.4886 | +0.958 | 0.3382 | 1.2636 |  |
| Kidney disease | +0.3267 | 0.2704 | ±0.5409 | +1.208 | 0.2270 | 1.3864 |  |
| **Circulatory disease** | **+0.7629** | 0.2594 | ±0.5188 | **+2.941** | **0.0033** | 2.1444 | ** |
| Time < 70 (%) | +0.1572 | 0.0915 | ±0.1829 | +1.719 | 0.0857 | 1.1702 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0902**, LLR χ² = **51.57** (p = **3.26e-07**), AUC = **0.7007**, AIC = **544.3**, BIC = **596.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2600 | 0.9455 | ±1.8909 | +0.275 | 0.7833 | 1.2970 |  |
| Education: graduate level (vs college) | -0.4452 | 0.2785 | ±0.5569 | -1.599 | 0.1099 | 0.6407 |  |
| Education: high school or below (vs college) | +0.1696 | 0.2833 | ±0.5665 | +0.599 | 0.5495 | 1.1848 |  |
| Site: UCSD (vs UAB) | -0.0705 | 0.2794 | ±0.5588 | -0.252 | 0.8008 | 0.9319 |  |
| Site: UW (vs UAB) | -0.1252 | 0.2703 | ±0.5405 | -0.463 | 0.6433 | 0.8823 |  |
| **Age (years)** | **-0.0460** | 0.0117 | ±0.0234 | **-3.929** | **8.51e-05** | 0.9550 | *** |
| BMI (kg/m2) | +0.0244 | 0.0147 | ±0.0294 | +1.658 | 0.0973 | 1.0247 | . |
| Hypertension | +0.2466 | 0.2644 | ±0.5288 | +0.933 | 0.3509 | 1.2797 |  |
| High cholesterol | +0.2417 | 0.2449 | ±0.4897 | +0.987 | 0.3235 | 1.2735 |  |
| Kidney disease | +0.3236 | 0.2706 | ±0.5411 | +1.196 | 0.2316 | 1.3821 |  |
| **Circulatory disease** | **+0.7678** | 0.2593 | ±0.5186 | **+2.961** | **0.0031** | 2.1551 | ** |
| Avg. daily time < 70 (%) | +0.1649 | 0.0878 | ±0.1756 | +1.878 | 0.0604 | 1.1792 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0861**, LLR χ² = **49.23** (p = **8.61e-07**), AUC = **0.7000**, AIC = **546.7**, BIC = **598.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.8140 | 1.0241 | ±2.0482 | +0.795 | 0.4267 | 2.2570 |  |
| Education: graduate level (vs college) | -0.4281 | 0.2786 | ±0.5572 | -1.537 | 0.1244 | 0.6518 |  |
| Education: high school or below (vs college) | +0.1248 | 0.2844 | ±0.5688 | +0.439 | 0.6609 | 1.1329 |  |
| Site: UCSD (vs UAB) | -0.0835 | 0.2792 | ±0.5584 | -0.299 | 0.7648 | 0.9199 |  |
| Site: UW (vs UAB) | -0.1386 | 0.2701 | ±0.5402 | -0.513 | 0.6079 | 0.8706 |  |
| **Age (years)** | **-0.0438** | 0.0118 | ±0.0235 | **-3.729** | **1.92e-04** | 0.9571 | *** |
| BMI (kg/m2) | +0.0232 | 0.0147 | ±0.0294 | +1.578 | 0.1146 | 1.0235 |  |
| Hypertension | +0.2809 | 0.2632 | ±0.5265 | +1.067 | 0.2859 | 1.3243 |  |
| High cholesterol | +0.2012 | 0.2432 | ±0.4864 | +0.827 | 0.4082 | 1.2228 |  |
| Kidney disease | +0.3421 | 0.2693 | ±0.5387 | +1.270 | 0.2041 | 1.4079 |  |
| **Circulatory disease** | **+0.7238** | 0.2576 | ±0.5153 | **+2.810** | **0.0050** | 2.0623 | ** |
| Time 54-250, pooled (%) | -0.0064 | 0.0053 | ±0.0106 | -1.210 | 0.2262 | 0.9936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0853**, LLR χ² = **48.76** (p = **1.05e-06**), AUC = **0.6985**, AIC = **547.2**, BIC = **598.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7442 | 1.0314 | ±2.0627 | +0.722 | 0.4706 | 2.1047 |  |
| Education: graduate level (vs college) | -0.4333 | 0.2785 | ±0.5570 | -1.556 | 0.1197 | 0.6483 |  |
| Education: high school or below (vs college) | +0.1303 | 0.2841 | ±0.5682 | +0.459 | 0.6466 | 1.1391 |  |
| Site: UCSD (vs UAB) | -0.0883 | 0.2791 | ±0.5582 | -0.316 | 0.7517 | 0.9155 |  |
| Site: UW (vs UAB) | -0.1465 | 0.2698 | ±0.5397 | -0.543 | 0.5872 | 0.8637 |  |
| **Age (years)** | **-0.0442** | 0.0117 | ±0.0235 | **-3.768** | **1.65e-04** | 0.9567 | *** |
| BMI (kg/m2) | +0.0233 | 0.0147 | ±0.0294 | +1.586 | 0.1129 | 1.0236 |  |
| Hypertension | +0.2846 | 0.2631 | ±0.5261 | +1.082 | 0.2792 | 1.3293 |  |
| High cholesterol | +0.2011 | 0.2431 | ±0.4863 | +0.827 | 0.4083 | 1.2227 |  |
| Kidney disease | +0.3417 | 0.2693 | ±0.5386 | +1.269 | 0.2045 | 1.4073 |  |
| **Circulatory disease** | **+0.7239** | 0.2576 | ±0.5153 | **+2.810** | **0.0050** | 2.0625 | ** |
| Avg. daily time 54-250 (%) | -0.0053 | 0.0054 | ±0.0107 | -0.989 | 0.3225 | 0.9947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0872**, LLR χ² = **49.88** (p = **6.57e-07**), AUC = **0.7012**, AIC = **546.0**, BIC = **597.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1137 | 0.9533 | ±1.9065 | +0.119 | 0.9051 | 1.1204 |  |
| Education: graduate level (vs college) | -0.4567 | 0.2781 | ±0.5561 | -1.642 | 0.1005 | 0.6334 |  |
| Education: high school or below (vs college) | +0.1341 | 0.2829 | ±0.5658 | +0.474 | 0.6356 | 1.1435 |  |
| Site: UCSD (vs UAB) | -0.0839 | 0.2793 | ±0.5585 | -0.300 | 0.7638 | 0.9195 |  |
| Site: UW (vs UAB) | -0.1702 | 0.2684 | ±0.5367 | -0.634 | 0.5259 | 0.8435 |  |
| **Age (years)** | **-0.0456** | 0.0117 | ±0.0234 | **-3.903** | **9.50e-05** | 0.9554 | *** |
| BMI (kg/m2) | +0.0217 | 0.0148 | ±0.0297 | +1.458 | 0.1447 | 1.0219 |  |
| Hypertension | +0.3289 | 0.2650 | ±0.5301 | +1.241 | 0.2146 | 1.3895 |  |
| High cholesterol | +0.2173 | 0.2445 | ±0.4890 | +0.889 | 0.3741 | 1.2427 |  |
| Kidney disease | +0.3460 | 0.2696 | ±0.5392 | +1.283 | 0.1994 | 1.4134 |  |
| **Circulatory disease** | **+0.7070** | 0.2591 | ±0.5182 | **+2.728** | **0.0064** | 2.0279 | ** |
| Time 181-250, pooled (%) | +0.0108 | 0.0075 | ±0.0150 | +1.449 | 0.1473 | 1.0109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0876**, LLR χ² = **50.09** (p = **6.04e-07**), AUC = **0.7015**, AIC = **545.8**, BIC = **597.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1040 | 0.9534 | ±1.9068 | +0.109 | 0.9131 | 1.1096 |  |
| Education: graduate level (vs college) | -0.4595 | 0.2782 | ±0.5563 | -1.652 | 0.0986 | 0.6316 | . |
| Education: high school or below (vs college) | +0.1278 | 0.2832 | ±0.5664 | +0.451 | 0.6517 | 1.1364 |  |
| Site: UCSD (vs UAB) | -0.0796 | 0.2794 | ±0.5588 | -0.285 | 0.7756 | 0.9234 |  |
| Site: UW (vs UAB) | -0.1676 | 0.2685 | ±0.5370 | -0.624 | 0.5325 | 0.8457 |  |
| **Age (years)** | **-0.0455** | 0.0117 | ±0.0234 | **-3.893** | **9.88e-05** | 0.9556 | *** |
| BMI (kg/m2) | +0.0214 | 0.0149 | ±0.0297 | +1.441 | 0.1497 | 1.0216 |  |
| Hypertension | +0.3302 | 0.2651 | ±0.5302 | +1.246 | 0.2129 | 1.3912 |  |
| High cholesterol | +0.2171 | 0.2445 | ±0.4889 | +0.888 | 0.3745 | 1.2425 |  |
| Kidney disease | +0.3449 | 0.2696 | ±0.5393 | +1.279 | 0.2008 | 1.4119 |  |
| **Circulatory disease** | **+0.7078** | 0.2591 | ±0.5181 | **+2.732** | **0.0063** | 2.0295 | ** |
| Avg. daily time 181-250 (%) | +0.0111 | 0.0073 | ±0.0147 | +1.519 | 0.1288 | 1.0112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0885**, LLR χ² = **50.61** (p = **4.86e-07**), AUC = **0.7038**, AIC = **545.3**, BIC = **597.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0272 | 0.9603 | ±1.9205 | +0.028 | 0.9774 | 1.0276 |  |
| Education: graduate level (vs college) | -0.4274 | 0.2785 | ±0.5570 | -1.535 | 0.1248 | 0.6522 |  |
| Education: high school or below (vs college) | +0.1092 | 0.2848 | ±0.5696 | +0.384 | 0.7013 | 1.1154 |  |
| Site: UCSD (vs UAB) | -0.0642 | 0.2802 | ±0.5604 | -0.229 | 0.8187 | 0.9378 |  |
| Site: UW (vs UAB) | -0.1318 | 0.2699 | ±0.5398 | -0.489 | 0.6252 | 0.8765 |  |
| **Age (years)** | **-0.0438** | 0.0117 | ±0.0234 | **-3.749** | **1.78e-04** | 0.9571 | *** |
| BMI (kg/m2) | +0.0217 | 0.0148 | ±0.0296 | +1.466 | 0.1427 | 1.0219 |  |
| Hypertension | +0.3020 | 0.2638 | ±0.5275 | +1.145 | 0.2522 | 1.3525 |  |
| High cholesterol | +0.2116 | 0.2440 | ±0.4879 | +0.867 | 0.3857 | 1.2357 |  |
| Kidney disease | +0.3388 | 0.2697 | ±0.5395 | +1.256 | 0.2092 | 1.4032 |  |
| **Circulatory disease** | **+0.7097** | 0.2584 | ±0.5168 | **+2.746** | **0.0060** | 2.0334 | ** |
| Time > 180 (%) | +0.0068 | 0.0040 | ±0.0081 | +1.688 | 0.0914 | 1.0068 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0877**, LLR χ² = **50.18** (p = **5.81e-07**), AUC = **0.7028**, AIC = **545.7**, BIC = **597.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0641 | 0.9584 | ±1.9168 | +0.067 | 0.9467 | 1.0662 |  |
| Education: graduate level (vs college) | -0.4318 | 0.2783 | ±0.5567 | -1.551 | 0.1208 | 0.6494 |  |
| Education: high school or below (vs college) | +0.1100 | 0.2848 | ±0.5697 | +0.386 | 0.6993 | 1.1163 |  |
| Site: UCSD (vs UAB) | -0.0661 | 0.2802 | ±0.5603 | -0.236 | 0.8134 | 0.9360 |  |
| Site: UW (vs UAB) | -0.1356 | 0.2698 | ±0.5395 | -0.503 | 0.6152 | 0.8732 |  |
| **Age (years)** | **-0.0441** | 0.0117 | ±0.0234 | **-3.768** | **1.65e-04** | 0.9569 | *** |
| BMI (kg/m2) | +0.0218 | 0.0148 | ±0.0296 | +1.470 | 0.1415 | 1.0220 |  |
| Hypertension | +0.3029 | 0.2636 | ±0.5272 | +1.149 | 0.2505 | 1.3538 |  |
| High cholesterol | +0.2100 | 0.2438 | ±0.4876 | +0.862 | 0.3889 | 1.2337 |  |
| Kidney disease | +0.3372 | 0.2697 | ±0.5394 | +1.250 | 0.2113 | 1.4010 |  |
| **Circulatory disease** | **+0.7110** | 0.2583 | ±0.5166 | **+2.753** | **0.0059** | 2.0361 | ** |
| Avg. daily time > 180 (%) | +0.0063 | 0.0040 | ±0.0081 | +1.553 | 0.1205 | 1.0063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0922**, LLR χ² = **52.74** (p = **2.00e-07**), AUC = **0.7084**, AIC = **543.2**, BIC = **594.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0152 | 0.9539 | ±1.9078 | +0.016 | 0.9873 | 1.0154 |  |
| Education: graduate level (vs college) | -0.4009 | 0.2796 | ±0.5592 | -1.434 | 0.1516 | 0.6697 |  |
| Education: high school or below (vs college) | +0.1117 | 0.2849 | ±0.5699 | +0.392 | 0.6950 | 1.1182 |  |
| Site: UCSD (vs UAB) | -0.0369 | 0.2816 | ±0.5632 | -0.131 | 0.8957 | 0.9638 |  |
| Site: UW (vs UAB) | -0.1332 | 0.2699 | ±0.5399 | -0.494 | 0.6217 | 0.8753 |  |
| **Age (years)** | **-0.0430** | 0.0117 | ±0.0234 | **-3.676** | **2.37e-04** | 0.9579 | *** |
| BMI (kg/m2) | +0.0197 | 0.0149 | ±0.0298 | +1.325 | 0.1853 | 1.0199 |  |
| Hypertension | +0.3067 | 0.2646 | ±0.5293 | +1.159 | 0.2465 | 1.3590 |  |
| High cholesterol | +0.2291 | 0.2451 | ±0.4902 | +0.935 | 0.3499 | 1.2575 |  |
| Kidney disease | +0.3433 | 0.2702 | ±0.5405 | +1.270 | 0.2039 | 1.4096 |  |
| **Circulatory disease** | **+0.7034** | 0.2588 | ±0.5177 | **+2.717** | **0.0066** | 2.0206 | ** |
| **Nocturnal time > 180 (%)** | **+0.0079** | 0.0035 | ±0.0071 | **+2.242** | **0.0250** | 1.0080 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0860**, LLR χ² = **49.19** (p = **8.75e-07**), AUC = **0.6999**, AIC = **546.7**, BIC = **598.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1767 | 0.9523 | ±1.9047 | +0.186 | 0.8528 | 1.1933 |  |
| Education: graduate level (vs college) | -0.4286 | 0.2786 | ±0.5572 | -1.539 | 0.1239 | 0.6514 |  |
| Education: high school or below (vs college) | +0.1249 | 0.2844 | ±0.5688 | +0.439 | 0.6604 | 1.1331 |  |
| Site: UCSD (vs UAB) | -0.0842 | 0.2792 | ±0.5584 | -0.302 | 0.7628 | 0.9192 |  |
| Site: UW (vs UAB) | -0.1395 | 0.2700 | ±0.5401 | -0.517 | 0.6053 | 0.8698 |  |
| **Age (years)** | **-0.0438** | 0.0118 | ±0.0235 | **-3.731** | **1.91e-04** | 0.9571 | *** |
| BMI (kg/m2) | +0.0232 | 0.0147 | ±0.0294 | +1.579 | 0.1143 | 1.0235 |  |
| Hypertension | +0.2815 | 0.2632 | ±0.5264 | +1.070 | 0.2848 | 1.3252 |  |
| High cholesterol | +0.2008 | 0.2432 | ±0.4864 | +0.826 | 0.4089 | 1.2224 |  |
| Kidney disease | +0.3422 | 0.2693 | ±0.5386 | +1.271 | 0.2038 | 1.4081 |  |
| **Circulatory disease** | **+0.7236** | 0.2576 | ±0.5153 | **+2.809** | **0.0050** | 2.0618 | ** |
| Time > 250 (%) | +0.0063 | 0.0053 | ±0.0106 | +1.193 | 0.2327 | 1.0063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 550)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **550**, events = **118**, McFadden pseudo-R² = **0.0852**, LLR χ² = **48.70** (p = **1.07e-06**), AUC = **0.6984**, AIC = **547.2**, BIC = **598.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2163 | 0.9503 | ±1.9006 | +0.228 | 0.8200 | 1.2414 |  |
| Education: graduate level (vs college) | -0.4341 | 0.2785 | ±0.5569 | -1.559 | 0.1190 | 0.6479 |  |
| Education: high school or below (vs college) | +0.1307 | 0.2841 | ±0.5682 | +0.460 | 0.6455 | 1.1396 |  |
| Site: UCSD (vs UAB) | -0.0893 | 0.2791 | ±0.5581 | -0.320 | 0.7490 | 0.9146 |  |
| Site: UW (vs UAB) | -0.1477 | 0.2698 | ±0.5395 | -0.548 | 0.5840 | 0.8627 |  |
| **Age (years)** | **-0.0443** | 0.0117 | ±0.0235 | **-3.771** | **1.63e-04** | 0.9567 | *** |
| BMI (kg/m2) | +0.0234 | 0.0147 | ±0.0294 | +1.587 | 0.1124 | 1.0236 |  |
| Hypertension | +0.2853 | 0.2630 | ±0.5261 | +1.085 | 0.2781 | 1.3301 |  |
| High cholesterol | +0.2007 | 0.2431 | ±0.4863 | +0.826 | 0.4091 | 1.2223 |  |
| Kidney disease | +0.3420 | 0.2693 | ±0.5386 | +1.270 | 0.2041 | 1.4078 |  |
| **Circulatory disease** | **+0.7239** | 0.2576 | ±0.5153 | **+2.810** | **0.0050** | 2.0624 | ** |
| Avg. daily time > 250 (%) | +0.0052 | 0.0054 | ±0.0108 | +0.962 | 0.3359 | 1.0052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1846**, F-statistic = **10.42** (p = **8.88e-20**), Residual SE = **0.920** on **528** df, AIC = **1461.9**, BIC = **1522.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7380** | 0.4078 | ±0.8157 | **+9.166** | **4.92e-20** | *** |
| Education: graduate level (vs college) | -0.1110 | 0.0853 | ±0.1705 | -1.302 | 0.1930 |  |
| **Education: high school or below (vs college)** | **+0.4965** | 0.1321 | ±0.2642 | **+3.759** | **1.70e-04** | *** |
| Site: UCSD (vs UAB) | +0.0542 | 0.0870 | ±0.1739 | +0.623 | 0.5333 |  |
| **Site: UW (vs UAB)** | **-0.4309** | 0.1013 | ±0.2026 | **-4.255** | **2.09e-05** | *** |
| Season: spring (vs autumn) | -0.1216 | 0.1129 | ±0.2259 | -1.077 | 0.2814 |  |
| Season: summer (vs autumn) | +0.0856 | 0.1089 | ±0.2179 | +0.786 | 0.4320 |  |
| Season: winter (vs autumn) | +0.1012 | 0.1227 | ±0.2455 | +0.824 | 0.4097 |  |
| **Age (years)** | **-0.0281** | 0.0041 | ±0.0082 | **-6.855** | **7.14e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0133 | +0.435 | 0.6635 |  |
| Hypertension | +0.0426 | 0.0855 | ±0.1709 | +0.498 | 0.6186 |  |
| High cholesterol | -0.0315 | 0.0857 | ±0.1714 | -0.367 | 0.7135 |  |
| Kidney disease | +0.0039 | 0.0996 | ±0.1992 | +0.039 | 0.9685 |  |
| Circulatory disease | -0.0159 | 0.0933 | ±0.1866 | -0.171 | 0.8645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.2200**, Adj R² = **0.1993**, F-statistic = **10.62** (p = **2.29e-21**), Residual SE = **0.912** on **527** df, AIC = **1453.0**, BIC = **1517.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0377** | 0.4783 | ±0.9565 | **+6.352** | **2.13e-10** | *** |
| Education: graduate level (vs college) | -0.0928 | 0.0861 | ±0.1722 | -1.077 | 0.2813 |  |
| **Education: high school or below (vs college)** | **+0.4572** | 0.1271 | ±0.2543 | **+3.596** | **3.23e-04** | *** |
| Site: UCSD (vs UAB) | +0.0765 | 0.0875 | ±0.1750 | +0.875 | 0.3816 |  |
| **Site: UW (vs UAB)** | **-0.4047** | 0.0991 | ±0.1982 | **-4.085** | **4.41e-05** | *** |
| Season: spring (vs autumn) | -0.1030 | 0.1123 | ±0.2246 | -0.918 | 0.3589 |  |
| Season: summer (vs autumn) | +0.1106 | 0.1078 | ±0.2157 | +1.025 | 0.3053 |  |
| Season: winter (vs autumn) | +0.0993 | 0.1210 | ±0.2421 | +0.820 | 0.4121 |  |
| **Age (years)** | **-0.0273** | 0.0041 | ±0.0081 | **-6.722** | **1.80e-11** | *** |
| BMI (kg/m2) | +0.0008 | 0.0068 | ±0.0136 | +0.118 | 0.9065 |  |
| Hypertension | +0.0372 | 0.0854 | ±0.1707 | +0.436 | 0.6628 |  |
| High cholesterol | -0.0287 | 0.0859 | ±0.1718 | -0.334 | 0.7385 |  |
| Kidney disease | +0.0097 | 0.0998 | ±0.1996 | +0.097 | 0.9225 |  |
| Circulatory disease | -0.0269 | 0.0922 | ±0.1844 | -0.291 | 0.7707 |  |
| **HbA1c (%)** | **+0.0967** | 0.0400 | ±0.0799 | **+2.420** | **0.0155** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.2115**, Adj R² = **0.1906**, F-statistic = **10.10** (p = **3.12e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.8**, BIC = **1523.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3443** | 0.4486 | ±0.8973 | **+7.454** | **9.03e-14** | *** |
| Education: graduate level (vs college) | -0.1003 | 0.0857 | ±0.1715 | -1.170 | 0.2421 |  |
| **Education: high school or below (vs college)** | **+0.4741** | 0.1283 | ±0.2567 | **+3.693** | **2.21e-04** | *** |
| Site: UCSD (vs UAB) | +0.0725 | 0.0866 | ±0.1732 | +0.838 | 0.4023 |  |
| **Site: UW (vs UAB)** | **-0.4147** | 0.1004 | ±0.2009 | **-4.129** | **3.64e-05** | *** |
| Season: spring (vs autumn) | -0.1287 | 0.1136 | ±0.2273 | -1.133 | 0.2572 |  |
| Season: summer (vs autumn) | +0.0996 | 0.1086 | ±0.2172 | +0.917 | 0.3591 |  |
| Season: winter (vs autumn) | +0.0882 | 0.1218 | ±0.2436 | +0.724 | 0.4688 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.744** | **1.55e-11** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0135 | +0.283 | 0.7775 |  |
| Hypertension | +0.0428 | 0.0858 | ±0.1716 | +0.498 | 0.6183 |  |
| High cholesterol | -0.0259 | 0.0862 | ±0.1724 | -0.300 | 0.7640 |  |
| Kidney disease | -0.0033 | 0.0995 | ±0.1989 | -0.034 | 0.9731 |  |
| Circulatory disease | -0.0272 | 0.0927 | ±0.1855 | -0.293 | 0.7693 |  |
| Mean glucose (mg/dL) | +0.0022 | 0.0012 | ±0.0024 | +1.858 | 0.0632 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.2115**, Adj R² = **0.1906**, F-statistic = **10.10** (p = **3.12e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.8**, BIC = **1523.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0396** | 0.5379 | ±1.0759 | **+5.650** | **1.60e-08** | *** |
| Education: graduate level (vs college) | -0.1003 | 0.0857 | ±0.1715 | -1.170 | 0.2421 |  |
| **Education: high school or below (vs college)** | **+0.4741** | 0.1283 | ±0.2567 | **+3.693** | **2.21e-04** | *** |
| Site: UCSD (vs UAB) | +0.0725 | 0.0866 | ±0.1732 | +0.838 | 0.4023 |  |
| **Site: UW (vs UAB)** | **-0.4147** | 0.1004 | ±0.2009 | **-4.129** | **3.64e-05** | *** |
| Season: spring (vs autumn) | -0.1287 | 0.1136 | ±0.2273 | -1.133 | 0.2572 |  |
| Season: summer (vs autumn) | +0.0996 | 0.1086 | ±0.2172 | +0.917 | 0.3591 |  |
| Season: winter (vs autumn) | +0.0882 | 0.1218 | ±0.2436 | +0.724 | 0.4688 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.744** | **1.55e-11** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0135 | +0.283 | 0.7775 |  |
| Hypertension | +0.0428 | 0.0858 | ±0.1716 | +0.498 | 0.6183 |  |
| High cholesterol | -0.0259 | 0.0862 | ±0.1724 | -0.300 | 0.7640 |  |
| Kidney disease | -0.0033 | 0.0995 | ±0.1989 | -0.034 | 0.9731 |  |
| Circulatory disease | -0.0272 | 0.0927 | ±0.1855 | -0.293 | 0.7693 |  |
| GMI (%) | +0.0921 | 0.0496 | ±0.0991 | +1.858 | 0.0632 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.2170**, Adj R² = **0.1962**, F-statistic = **10.43** (p = **5.75e-21**), Residual SE = **0.914** on **527** df, AIC = **1455.0**, BIC = **1519.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.2668** | 0.4319 | ±0.8638 | **+7.564** | **3.91e-14** | *** |
| Education: graduate level (vs college) | -0.0925 | 0.0858 | ±0.1716 | -1.078 | 0.2809 |  |
| **Education: high school or below (vs college)** | **+0.4712** | 0.1279 | ±0.2558 | **+3.685** | **2.29e-04** | *** |
| Site: UCSD (vs UAB) | +0.0805 | 0.0863 | ±0.1725 | +0.933 | 0.3511 |  |
| **Site: UW (vs UAB)** | **-0.4198** | 0.1002 | ±0.2004 | **-4.189** | **2.80e-05** | *** |
| Season: spring (vs autumn) | -0.1362 | 0.1133 | ±0.2266 | -1.202 | 0.2292 |  |
| Season: summer (vs autumn) | +0.1012 | 0.1079 | ±0.2158 | +0.938 | 0.3483 |  |
| Season: winter (vs autumn) | +0.0828 | 0.1211 | ±0.2422 | +0.684 | 0.4941 |  |
| **Age (years)** | **-0.0269** | 0.0041 | ±0.0082 | **-6.597** | **4.18e-11** | *** |
| BMI (kg/m2) | +0.0008 | 0.0068 | ±0.0136 | +0.120 | 0.9047 |  |
| Hypertension | +0.0454 | 0.0857 | ±0.1714 | +0.530 | 0.5960 |  |
| High cholesterol | -0.0238 | 0.0859 | ±0.1718 | -0.276 | 0.7822 |  |
| Kidney disease | +0.0020 | 0.0983 | ±0.1966 | +0.020 | 0.9840 |  |
| Circulatory disease | -0.0310 | 0.0926 | ±0.1852 | -0.334 | 0.7383 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0027** | 0.0011 | ±0.0022 | **+2.488** | **0.0129** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2084**, Adj R² = **0.1874**, F-statistic = **9.91** (p = **8.03e-20**), Residual SE = **0.919** on **527** df, AIC = **1461.0**, BIC = **1525.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5002** | 0.4321 | ±0.8642 | **+8.100** | **5.48e-16** | *** |
| Education: graduate level (vs college) | -0.1013 | 0.0856 | ±0.1712 | -1.183 | 0.2367 |  |
| **Education: high school or below (vs college)** | **+0.4794** | 0.1317 | ±0.2635 | **+3.639** | **2.74e-04** | *** |
| Site: UCSD (vs UAB) | +0.0648 | 0.0869 | ±0.1738 | +0.746 | 0.4555 |  |
| **Site: UW (vs UAB)** | **-0.4105** | 0.1005 | ±0.2010 | **-4.085** | **4.41e-05** | *** |
| Season: spring (vs autumn) | -0.1276 | 0.1131 | ±0.2262 | -1.128 | 0.2591 |  |
| Season: summer (vs autumn) | +0.0981 | 0.1096 | ±0.2192 | +0.896 | 0.3705 |  |
| Season: winter (vs autumn) | +0.0922 | 0.1221 | ±0.2442 | +0.755 | 0.4503 |  |
| **Age (years)** | **-0.0279** | 0.0041 | ±0.0082 | **-6.798** | **1.06e-11** | *** |
| BMI (kg/m2) | +0.0024 | 0.0066 | ±0.0132 | +0.370 | 0.7115 |  |
| Hypertension | +0.0382 | 0.0859 | ±0.1717 | +0.445 | 0.6561 |  |
| High cholesterol | -0.0250 | 0.0864 | ±0.1727 | -0.289 | 0.7726 |  |
| Kidney disease | -0.0254 | 0.0980 | ±0.1960 | -0.259 | 0.7956 |  |
| Circulatory disease | -0.0230 | 0.0930 | ±0.1860 | -0.247 | 0.8046 |  |
| Glucose SD, pooled (mg/dL) | +0.0056 | 0.0032 | ±0.0064 | +1.754 | 0.0794 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2053**, Adj R² = **0.1842**, F-statistic = **9.73** (p = **2.06e-19**), Residual SE = **0.920** on **527** df, AIC = **1463.1**, BIC = **1527.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6065** | 0.4379 | ±0.8757 | **+8.237** | **1.77e-16** | *** |
| Education: graduate level (vs college) | -0.1069 | 0.0857 | ±0.1714 | -1.247 | 0.2122 |  |
| **Education: high school or below (vs college)** | **+0.4858** | 0.1326 | ±0.2652 | **+3.663** | **2.49e-04** | *** |
| Site: UCSD (vs UAB) | +0.0598 | 0.0873 | ±0.1746 | +0.685 | 0.4935 |  |
| **Site: UW (vs UAB)** | **-0.4214** | 0.1012 | ±0.2024 | **-4.164** | **3.13e-05** | *** |
| Season: spring (vs autumn) | -0.1253 | 0.1129 | ±0.2257 | -1.110 | 0.2668 |  |
| Season: summer (vs autumn) | +0.0928 | 0.1102 | ±0.2204 | +0.842 | 0.3998 |  |
| Season: winter (vs autumn) | +0.0980 | 0.1225 | ±0.2450 | +0.800 | 0.4240 |  |
| **Age (years)** | **-0.0281** | 0.0041 | ±0.0082 | **-6.820** | **9.07e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0133 | +0.435 | 0.6634 |  |
| Hypertension | +0.0414 | 0.0858 | ±0.1716 | +0.483 | 0.6293 |  |
| High cholesterol | -0.0286 | 0.0862 | ±0.1724 | -0.331 | 0.7404 |  |
| Kidney disease | -0.0127 | 0.0985 | ±0.1969 | -0.129 | 0.8970 |  |
| Circulatory disease | -0.0184 | 0.0934 | ±0.1868 | -0.197 | 0.8436 |  |
| Avg. daily SD (mg/dL) | +0.0034 | 0.0036 | ±0.0073 | +0.932 | 0.3513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1831**, F-statistic = **9.66** (p = **2.90e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.8**, BIC = **1528.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7048** | 0.4701 | ±0.9401 | **+7.881** | **3.24e-15** | *** |
| Education: graduate level (vs college) | -0.1105 | 0.0854 | ±0.1709 | -1.293 | 0.1961 |  |
| **Education: high school or below (vs college)** | **+0.4957** | 0.1333 | ±0.2667 | **+3.718** | **2.01e-04** | *** |
| Site: UCSD (vs UAB) | +0.0545 | 0.0871 | ±0.1743 | +0.626 | 0.5316 |  |
| **Site: UW (vs UAB)** | **-0.4292** | 0.1015 | ±0.2031 | **-4.227** | **2.37e-05** | *** |
| Season: spring (vs autumn) | -0.1216 | 0.1132 | ±0.2264 | -1.074 | 0.2827 |  |
| Season: summer (vs autumn) | +0.0863 | 0.1095 | ±0.2191 | +0.788 | 0.4309 |  |
| Season: winter (vs autumn) | +0.1010 | 0.1230 | ±0.2460 | +0.821 | 0.4114 |  |
| **Age (years)** | **-0.0282** | 0.0041 | ±0.0082 | **-6.843** | **7.74e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0067 | ±0.0133 | +0.435 | 0.6636 |  |
| Hypertension | +0.0417 | 0.0857 | ±0.1713 | +0.487 | 0.6265 |  |
| High cholesterol | -0.0311 | 0.0860 | ±0.1719 | -0.361 | 0.7179 |  |
| Kidney disease | +0.0002 | 0.0986 | ±0.1971 | +0.002 | 0.9981 |  |
| Circulatory disease | -0.0160 | 0.0934 | ±0.1869 | -0.171 | 0.8643 |  |
| CV (%) | +0.0014 | 0.0080 | ±0.0160 | +0.174 | 0.8619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1830**, F-statistic = **9.66** (p = **2.93e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.9**, BIC = **1528.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7573** | 0.4453 | ±0.8906 | **+8.438** | **3.24e-17** | *** |
| Education: graduate level (vs college) | -0.1107 | 0.0855 | ±0.1710 | -1.295 | 0.1954 |  |
| **Education: high school or below (vs college)** | **+0.4962** | 0.1333 | ±0.2667 | **+3.721** | **1.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.0541 | 0.0871 | ±0.1741 | +0.621 | 0.5343 |  |
| **Site: UW (vs UAB)** | **-0.4302** | 0.1017 | ±0.2035 | **-4.229** | **2.35e-05** | *** |
| Season: spring (vs autumn) | -0.1218 | 0.1129 | ±0.2258 | -1.079 | 0.2805 |  |
| Season: summer (vs autumn) | +0.0855 | 0.1090 | ±0.2180 | +0.784 | 0.4330 |  |
| Season: winter (vs autumn) | +0.1009 | 0.1231 | ±0.2462 | +0.820 | 0.4122 |  |
| **Age (years)** | **-0.0282** | 0.0041 | ±0.0082 | **-6.843** | **7.77e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0067 | ±0.0133 | +0.436 | 0.6627 |  |
| Hypertension | +0.0422 | 0.0856 | ±0.1713 | +0.493 | 0.6218 |  |
| High cholesterol | -0.0315 | 0.0859 | ±0.1718 | -0.367 | 0.7135 |  |
| Kidney disease | +0.0022 | 0.0988 | ±0.1976 | +0.023 | 0.9819 |  |
| Circulatory disease | -0.0162 | 0.0935 | ±0.1870 | -0.173 | 0.8627 |  |
| Mean / SD ratio | -0.0045 | 0.0451 | ±0.0903 | -0.099 | 0.9213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2049**, Adj R² = **0.1837**, F-statistic = **9.70** (p = **2.39e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.4**, BIC = **1527.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6284** | 0.4340 | ±0.8679 | **+8.361** | **6.21e-17** | *** |
| Education: graduate level (vs college) | -0.1129 | 0.0857 | ±0.1714 | -1.317 | 0.1879 |  |
| **Education: high school or below (vs college)** | **+0.4993** | 0.1332 | ±0.2664 | **+3.748** | **1.78e-04** | *** |
| Site: UCSD (vs UAB) | +0.0549 | 0.0871 | ±0.1743 | +0.630 | 0.5290 |  |
| **Site: UW (vs UAB)** | **-0.4338** | 0.1018 | ±0.2036 | **-4.261** | **2.04e-05** | *** |
| Season: spring (vs autumn) | -0.1219 | 0.1133 | ±0.2265 | -1.076 | 0.2818 |  |
| Season: summer (vs autumn) | +0.0850 | 0.1092 | ±0.2184 | +0.778 | 0.4363 |  |
| Season: winter (vs autumn) | +0.1009 | 0.1228 | ±0.2457 | +0.821 | 0.4116 |  |
| **Age (years)** | **-0.0281** | 0.0041 | ±0.0082 | **-6.840** | **7.93e-12** | *** |
| BMI (kg/m2) | +0.0026 | 0.0067 | ±0.0135 | +0.379 | 0.7049 |  |
| Hypertension | +0.0437 | 0.0856 | ±0.1711 | +0.511 | 0.6094 |  |
| High cholesterol | -0.0315 | 0.0857 | ±0.1715 | -0.367 | 0.7134 |  |
| Kidney disease | +0.0136 | 0.0994 | ±0.1988 | +0.137 | 0.8914 |  |
| Circulatory disease | -0.0158 | 0.0934 | ±0.1869 | -0.169 | 0.8661 |  |
| Avg. daily mean/SD | +0.0225 | 0.0388 | ±0.0776 | +0.579 | 0.5623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1831**, F-statistic = **9.66** (p = **2.90e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.8**, BIC = **1528.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6952** | 0.4622 | ±0.9245 | **+7.994** | **1.31e-15** | *** |
| Education: graduate level (vs college) | -0.1098 | 0.0859 | ±0.1717 | -1.279 | 0.2010 |  |
| **Education: high school or below (vs college)** | **+0.4954** | 0.1310 | ±0.2620 | **+3.782** | **1.56e-04** | *** |
| Site: UCSD (vs UAB) | +0.0550 | 0.0872 | ±0.1743 | +0.631 | 0.5281 |  |
| **Site: UW (vs UAB)** | **-0.4282** | 0.1024 | ±0.2049 | **-4.180** | **2.92e-05** | *** |
| Season: spring (vs autumn) | -0.1218 | 0.1133 | ±0.2267 | -1.075 | 0.2824 |  |
| Season: summer (vs autumn) | +0.0874 | 0.1091 | ±0.2182 | +0.801 | 0.4232 |  |
| Season: winter (vs autumn) | +0.1013 | 0.1229 | ±0.2457 | +0.825 | 0.4095 |  |
| **Age (years)** | **-0.0280** | 0.0041 | ±0.0082 | **-6.815** | **9.44e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0133 | +0.437 | 0.6622 |  |
| Hypertension | +0.0424 | 0.0857 | ±0.1714 | +0.495 | 0.6205 |  |
| High cholesterol | -0.0311 | 0.0861 | ±0.1722 | -0.361 | 0.7184 |  |
| Kidney disease | +0.0020 | 0.1012 | ±0.2024 | +0.020 | 0.9841 |  |
| Circulatory disease | -0.0162 | 0.0934 | ±0.1868 | -0.173 | 0.8624 |  |
| MAG (mg/dL/h) | +0.0008 | 0.0042 | ±0.0083 | +0.181 | 0.8567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.2047**, Adj R² = **0.1836**, F-statistic = **9.69** (p = **2.48e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.5**, BIC = **1527.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6126** | 0.4605 | ±0.9209 | **+7.845** | **4.31e-15** | *** |
| Education: graduate level (vs college) | -0.1082 | 0.0858 | ±0.1717 | -1.260 | 0.2075 |  |
| **Education: high school or below (vs college)** | **+0.4889** | 0.1326 | ±0.2652 | **+3.688** | **2.26e-04** | *** |
| Site: UCSD (vs UAB) | +0.0584 | 0.0873 | ±0.1745 | +0.669 | 0.5034 |  |
| **Site: UW (vs UAB)** | **-0.4244** | 0.1015 | ±0.2031 | **-4.180** | **2.92e-05** | *** |
| Season: spring (vs autumn) | -0.1252 | 0.1127 | ±0.2255 | -1.110 | 0.2670 |  |
| Season: summer (vs autumn) | +0.0882 | 0.1095 | ±0.2191 | +0.805 | 0.4209 |  |
| Season: winter (vs autumn) | +0.0982 | 0.1226 | ±0.2452 | +0.801 | 0.4234 |  |
| **Age (years)** | **-0.0280** | 0.0041 | ±0.0083 | **-6.775** | **1.24e-11** | *** |
| BMI (kg/m2) | +0.0030 | 0.0066 | ±0.0133 | +0.447 | 0.6549 |  |
| Hypertension | +0.0430 | 0.0858 | ±0.1715 | +0.502 | 0.6158 |  |
| High cholesterol | -0.0309 | 0.0860 | ±0.1720 | -0.359 | 0.7198 |  |
| Kidney disease | -0.0083 | 0.0985 | ±0.1970 | -0.085 | 0.9325 |  |
| Circulatory disease | -0.0184 | 0.0937 | ±0.1874 | -0.196 | 0.8444 |  |
| Avg. daily range (mg/dL) | +0.0007 | 0.0011 | ±0.0021 | +0.656 | 0.5118 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.2218**, Adj R² = **0.2011**, F-statistic = **10.73** (p = **1.32e-21**), Residual SE = **0.911** on **527** df, AIC = **1451.8**, BIC = **1516.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4699** | 0.4049 | ±0.8099 | **+8.569** | **1.04e-17** | *** |
| Education: graduate level (vs college) | -0.0818 | 0.0854 | ±0.1707 | -0.958 | 0.3379 |  |
| **Education: high school or below (vs college)** | **+0.4892** | 0.1290 | ±0.2581 | **+3.791** | **1.50e-04** | *** |
| Site: UCSD (vs UAB) | +0.0702 | 0.0862 | ±0.1723 | +0.814 | 0.4154 |  |
| **Site: UW (vs UAB)** | **-0.3956** | 0.0993 | ±0.1986 | **-3.985** | **6.76e-05** | *** |
| Season: spring (vs autumn) | -0.1187 | 0.1125 | ±0.2251 | -1.055 | 0.2914 |  |
| Season: summer (vs autumn) | +0.0963 | 0.1081 | ±0.2162 | +0.891 | 0.3727 |  |
| Season: winter (vs autumn) | +0.0775 | 0.1206 | ±0.2411 | +0.643 | 0.5204 |  |
| **Age (years)** | **-0.0268** | 0.0041 | ±0.0081 | **-6.582** | **4.64e-11** | *** |
| BMI (kg/m2) | +0.0009 | 0.0065 | ±0.0129 | +0.141 | 0.8876 |  |
| Hypertension | +0.0226 | 0.0859 | ±0.1718 | +0.264 | 0.7921 |  |
| High cholesterol | -0.0193 | 0.0856 | ±0.1712 | -0.225 | 0.8219 |  |
| Kidney disease | -0.0206 | 0.0963 | ±0.1925 | -0.214 | 0.8307 |  |
| Circulatory disease | -0.0495 | 0.0914 | ±0.1828 | -0.542 | 0.5879 |  |
| **SD of daily means (mg/dL)** | **+0.0161** | 0.0050 | ±0.0099 | **+3.236** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.2121**, Adj R² = **0.1912**, F-statistic = **10.14** (p = **2.60e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.4**, BIC = **1522.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.9754** | 0.4304 | ±0.8607 | **+9.237** | **2.53e-20** | *** |
| Education: graduate level (vs college) | -0.1024 | 0.0858 | ±0.1715 | -1.194 | 0.2324 |  |
| **Education: high school or below (vs college)** | **+0.4716** | 0.1285 | ±0.2569 | **+3.671** | **2.41e-04** | *** |
| Site: UCSD (vs UAB) | +0.0772 | 0.0865 | ±0.1730 | +0.892 | 0.3724 |  |
| **Site: UW (vs UAB)** | **-0.4132** | 0.1002 | ±0.2004 | **-4.124** | **3.73e-05** | *** |
| Season: spring (vs autumn) | -0.1299 | 0.1135 | ±0.2269 | -1.145 | 0.2523 |  |
| Season: summer (vs autumn) | +0.0967 | 0.1084 | ±0.2168 | +0.892 | 0.3725 |  |
| Season: winter (vs autumn) | +0.0864 | 0.1218 | ±0.2436 | +0.709 | 0.4781 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0134 | +0.236 | 0.8131 |  |
| Hypertension | +0.0454 | 0.0859 | ±0.1718 | +0.528 | 0.5974 |  |
| High cholesterol | -0.0206 | 0.0865 | ±0.1729 | -0.238 | 0.8116 |  |
| Kidney disease | -0.0082 | 0.0990 | ±0.1980 | -0.083 | 0.9341 |  |
| Circulatory disease | -0.0274 | 0.0920 | ±0.1841 | -0.298 | 0.7661 |  |
| **Time in range 70-180, pooled (%)** | **-0.0036** | 0.0018 | ±0.0035 | **-2.065** | **0.0389** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.2120**, Adj R² = **0.1911**, F-statistic = **10.13** (p = **2.70e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.5**, BIC = **1522.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.9768** | 0.4312 | ±0.8623 | **+9.224** | **2.87e-20** | *** |
| Education: graduate level (vs college) | -0.1035 | 0.0857 | ±0.1715 | -1.207 | 0.2276 |  |
| **Education: high school or below (vs college)** | **+0.4706** | 0.1284 | ±0.2568 | **+3.665** | **2.47e-04** | *** |
| Site: UCSD (vs UAB) | +0.0781 | 0.0865 | ±0.1730 | +0.903 | 0.3665 |  |
| **Site: UW (vs UAB)** | **-0.4130** | 0.1002 | ±0.2005 | **-4.121** | **3.77e-05** | *** |
| Season: spring (vs autumn) | -0.1306 | 0.1135 | ±0.2270 | -1.151 | 0.2498 |  |
| Season: summer (vs autumn) | +0.0950 | 0.1084 | ±0.2167 | +0.877 | 0.3805 |  |
| Season: winter (vs autumn) | +0.0849 | 0.1219 | ±0.2437 | +0.697 | 0.4861 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.811** | **9.71e-12** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0134 | +0.232 | 0.8166 |  |
| Hypertension | +0.0457 | 0.0860 | ±0.1719 | +0.532 | 0.5947 |  |
| High cholesterol | -0.0210 | 0.0864 | ±0.1729 | -0.243 | 0.8076 |  |
| Kidney disease | -0.0095 | 0.0989 | ±0.1978 | -0.096 | 0.9237 |  |
| Circulatory disease | -0.0273 | 0.0921 | ±0.1843 | -0.296 | 0.7669 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0036** | 0.0017 | ±0.0035 | **-2.053** | **0.0401** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2059**, Adj R² = **0.1848**, F-statistic = **9.76** (p = **1.76e-19**), Residual SE = **0.920** on **527** df, AIC = **1462.7**, BIC = **1527.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6965** | 0.4066 | ±0.8132 | **+9.091** | **9.79e-20** | *** |
| Education: graduate level (vs college) | -0.1108 | 0.0855 | ±0.1710 | -1.296 | 0.1949 |  |
| **Education: high school or below (vs college)** | **+0.4986** | 0.1321 | ±0.2643 | **+3.774** | **1.61e-04** | *** |
| Site: UCSD (vs UAB) | +0.0611 | 0.0870 | ±0.1739 | +0.702 | 0.4825 |  |
| **Site: UW (vs UAB)** | **-0.4247** | 0.1012 | ±0.2024 | **-4.197** | **2.71e-05** | *** |
| Season: spring (vs autumn) | -0.1229 | 0.1133 | ±0.2267 | -1.084 | 0.2783 |  |
| Season: summer (vs autumn) | +0.0878 | 0.1091 | ±0.2183 | +0.804 | 0.4213 |  |
| Season: winter (vs autumn) | +0.1091 | 0.1229 | ±0.2459 | +0.888 | 0.3748 |  |
| **Age (years)** | **-0.0279** | 0.0041 | ±0.0082 | **-6.789** | **1.13e-11** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0132 | +0.434 | 0.6646 |  |
| Hypertension | +0.0331 | 0.0862 | ±0.1724 | +0.384 | 0.7011 |  |
| High cholesterol | -0.0246 | 0.0868 | ±0.1736 | -0.283 | 0.7773 |  |
| Kidney disease | +0.0016 | 0.0990 | ±0.1980 | +0.016 | 0.9875 |  |
| Circulatory disease | -0.0224 | 0.0945 | ±0.1891 | -0.237 | 0.8129 |  |
| Any reading < 54 during wear (0/1) | +0.1034 | 0.1038 | ±0.2075 | +0.997 | 0.3189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2102**, Adj R² = **0.1892**, F-statistic = **10.02** (p = **4.76e-20**), Residual SE = **0.918** on **527** df, AIC = **1459.8**, BIC = **1524.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7038** | 0.4054 | ±0.8108 | **+9.136** | **6.50e-20** | *** |
| Education: graduate level (vs college) | -0.1041 | 0.0852 | ±0.1703 | -1.223 | 0.2213 |  |
| **Education: high school or below (vs college)** | **+0.5067** | 0.1314 | ±0.2627 | **+3.857** | **1.15e-04** | *** |
| Site: UCSD (vs UAB) | +0.0717 | 0.0877 | ±0.1754 | +0.818 | 0.4134 |  |
| **Site: UW (vs UAB)** | **-0.4086** | 0.1010 | ±0.2020 | **-4.046** | **5.21e-05** | *** |
| Season: spring (vs autumn) | -0.1134 | 0.1139 | ±0.2278 | -0.996 | 0.3192 |  |
| Season: summer (vs autumn) | +0.0975 | 0.1087 | ±0.2174 | +0.897 | 0.3699 |  |
| Season: winter (vs autumn) | +0.1167 | 0.1238 | ±0.2477 | +0.943 | 0.3459 |  |
| **Age (years)** | **-0.0283** | 0.0041 | ±0.0083 | **-6.844** | **7.72e-12** | *** |
| BMI (kg/m2) | +0.0028 | 0.0065 | ±0.0130 | +0.439 | 0.6609 |  |
| Hypertension | +0.0224 | 0.0867 | ±0.1735 | +0.258 | 0.7966 |  |
| High cholesterol | -0.0157 | 0.0884 | ±0.1767 | -0.178 | 0.8588 |  |
| Kidney disease | +0.0000 | 0.0984 | ±0.1968 | +0.000 | 0.9998 |  |
| Circulatory disease | -0.0022 | 0.0926 | ±0.1851 | -0.023 | 0.9813 |  |
| Time < 54 (%) | +0.3179 | 0.2991 | ±0.5982 | +1.063 | 0.2878 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2089**, Adj R² = **0.1879**, F-statistic = **9.94** (p = **6.89e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.6**, BIC = **1525.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7149** | 0.4055 | ±0.8109 | **+9.162** | **5.08e-20** | *** |
| Education: graduate level (vs college) | -0.1065 | 0.0849 | ±0.1698 | -1.254 | 0.2100 |  |
| **Education: high school or below (vs college)** | **+0.5048** | 0.1315 | ±0.2630 | **+3.839** | **1.23e-04** | *** |
| Site: UCSD (vs UAB) | +0.0666 | 0.0875 | ±0.1751 | +0.760 | 0.4470 |  |
| **Site: UW (vs UAB)** | **-0.4152** | 0.1029 | ±0.2057 | **-4.036** | **5.44e-05** | *** |
| Season: spring (vs autumn) | -0.1046 | 0.1138 | ±0.2275 | -0.919 | 0.3580 |  |
| Season: summer (vs autumn) | +0.1020 | 0.1087 | ±0.2173 | +0.939 | 0.3479 |  |
| Season: winter (vs autumn) | +0.1165 | 0.1236 | ±0.2472 | +0.943 | 0.3459 |  |
| **Age (years)** | **-0.0282** | 0.0042 | ±0.0083 | **-6.775** | **1.25e-11** | *** |
| BMI (kg/m2) | +0.0027 | 0.0065 | ±0.0130 | +0.415 | 0.6782 |  |
| Hypertension | +0.0306 | 0.0864 | ±0.1728 | +0.354 | 0.7231 |  |
| High cholesterol | -0.0195 | 0.0872 | ±0.1745 | -0.224 | 0.8228 |  |
| Kidney disease | -0.0022 | 0.1016 | ±0.2031 | -0.022 | 0.9826 |  |
| Circulatory disease | -0.0083 | 0.0931 | ±0.1861 | -0.089 | 0.9289 |  |
| Avg. daily time < 54 (%) | +0.2053 | 0.5683 | ±1.1365 | +0.361 | 0.7179 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2067**, Adj R² = **0.1856**, F-statistic = **9.81** (p = **1.35e-19**), Residual SE = **0.920** on **527** df, AIC = **1462.1**, BIC = **1526.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7071** | 0.4064 | ±0.8128 | **+9.122** | **7.37e-20** | *** |
| Education: graduate level (vs college) | -0.1076 | 0.0854 | ±0.1708 | -1.260 | 0.2077 |  |
| **Education: high school or below (vs college)** | **+0.4972** | 0.1327 | ±0.2654 | **+3.747** | **1.79e-04** | *** |
| Site: UCSD (vs UAB) | +0.0678 | 0.0869 | ±0.1738 | +0.780 | 0.4353 |  |
| **Site: UW (vs UAB)** | **-0.4182** | 0.1009 | ±0.2018 | **-4.144** | **3.41e-05** | *** |
| Season: spring (vs autumn) | -0.1109 | 0.1145 | ±0.2290 | -0.969 | 0.3327 |  |
| Season: summer (vs autumn) | +0.0955 | 0.1094 | ±0.2188 | +0.873 | 0.3829 |  |
| Season: winter (vs autumn) | +0.1116 | 0.1242 | ±0.2485 | +0.898 | 0.3692 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.820** | **9.12e-12** | *** |
| BMI (kg/m2) | +0.0032 | 0.0066 | ±0.0132 | +0.478 | 0.6328 |  |
| Hypertension | +0.0319 | 0.0855 | ±0.1710 | +0.373 | 0.7089 |  |
| High cholesterol | -0.0206 | 0.0876 | ±0.1753 | -0.235 | 0.8143 |  |
| Kidney disease | -0.0024 | 0.0984 | ±0.1968 | -0.024 | 0.9808 |  |
| Circulatory disease | -0.0095 | 0.0933 | ±0.1866 | -0.102 | 0.9190 |  |
| Time 54-69, pooled (%) | +0.0582 | 0.0590 | ±0.1180 | +0.986 | 0.3240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.2075**, Adj R² = **0.1864**, F-statistic = **9.85** (p = **1.08e-19**), Residual SE = **0.919** on **527** df, AIC = **1461.6**, BIC = **1526.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7126** | 0.4061 | ±0.8121 | **+9.143** | **6.09e-20** | *** |
| Education: graduate level (vs college) | -0.1059 | 0.0851 | ±0.1702 | -1.245 | 0.2133 |  |
| **Education: high school or below (vs college)** | **+0.4984** | 0.1328 | ±0.2656 | **+3.753** | **1.75e-04** | *** |
| Site: UCSD (vs UAB) | +0.0696 | 0.0869 | ±0.1737 | +0.801 | 0.4231 |  |
| **Site: UW (vs UAB)** | **-0.4149** | 0.1006 | ±0.2011 | **-4.126** | **3.70e-05** | *** |
| Season: spring (vs autumn) | -0.1093 | 0.1143 | ±0.2286 | -0.956 | 0.3388 |  |
| Season: summer (vs autumn) | +0.0966 | 0.1092 | ±0.2184 | +0.885 | 0.3761 |  |
| Season: winter (vs autumn) | +0.1124 | 0.1242 | ±0.2483 | +0.906 | 0.3652 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.828** | **8.59e-12** | *** |
| BMI (kg/m2) | +0.0030 | 0.0066 | ±0.0132 | +0.460 | 0.6454 |  |
| Hypertension | +0.0301 | 0.0855 | ±0.1711 | +0.352 | 0.7246 |  |
| High cholesterol | -0.0185 | 0.0877 | ±0.1754 | -0.211 | 0.8328 |  |
| Kidney disease | -0.0024 | 0.0981 | ±0.1962 | -0.024 | 0.9806 |  |
| Circulatory disease | -0.0074 | 0.0928 | ±0.1855 | -0.080 | 0.9364 |  |
| Avg. daily time 54-69 (%) | +0.0632 | 0.0572 | ±0.1144 | +1.106 | 0.2688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.2079**, Adj R² = **0.1868**, F-statistic = **9.88** (p = **9.51e-20**), Residual SE = **0.919** on **527** df, AIC = **1461.3**, BIC = **1525.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7002** | 0.4062 | ±0.8125 | **+9.109** | **8.34e-20** | *** |
| Education: graduate level (vs college) | -0.1063 | 0.0853 | ±0.1706 | -1.245 | 0.2130 |  |
| **Education: high school or below (vs college)** | **+0.4991** | 0.1326 | ±0.2651 | **+3.765** | **1.66e-04** | *** |
| Site: UCSD (vs UAB) | +0.0713 | 0.0871 | ±0.1742 | +0.818 | 0.4131 |  |
| **Site: UW (vs UAB)** | **-0.4138** | 0.1008 | ±0.2016 | **-4.104** | **4.06e-05** | *** |
| Season: spring (vs autumn) | -0.1092 | 0.1144 | ±0.2287 | -0.955 | 0.3396 |  |
| Season: summer (vs autumn) | +0.0978 | 0.1093 | ±0.2186 | +0.895 | 0.3706 |  |
| Season: winter (vs autumn) | +0.1146 | 0.1244 | ±0.2489 | +0.921 | 0.3570 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.828** | **8.62e-12** | *** |
| BMI (kg/m2) | +0.0031 | 0.0066 | ±0.0131 | +0.479 | 0.6319 |  |
| Hypertension | +0.0280 | 0.0858 | ±0.1716 | +0.326 | 0.7443 |  |
| High cholesterol | -0.0175 | 0.0882 | ±0.1763 | -0.198 | 0.8430 |  |
| Kidney disease | -0.0032 | 0.0982 | ±0.1963 | -0.033 | 0.9739 |  |
| Circulatory disease | -0.0068 | 0.0931 | ±0.1862 | -0.073 | 0.9416 |  |
| Time < 70 (%) | +0.0592 | 0.0523 | ±0.1047 | +1.131 | 0.2581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.2085**, Adj R² = **0.1875**, F-statistic = **9.92** (p = **7.86e-20**), Residual SE = **0.919** on **527** df, AIC = **1460.9**, BIC = **1525.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7085** | 0.4056 | ±0.8112 | **+9.143** | **6.06e-20** | *** |
| Education: graduate level (vs college) | -0.1051 | 0.0850 | ±0.1700 | -1.237 | 0.2162 |  |
| **Education: high school or below (vs college)** | **+0.5005** | 0.1326 | ±0.2652 | **+3.775** | **1.60e-04** | *** |
| Site: UCSD (vs UAB) | +0.0716 | 0.0869 | ±0.1738 | +0.824 | 0.4099 |  |
| **Site: UW (vs UAB)** | **-0.4119** | 0.1005 | ±0.2011 | **-4.097** | **4.19e-05** | *** |
| Season: spring (vs autumn) | -0.1057 | 0.1142 | ±0.2284 | -0.925 | 0.3548 |  |
| Season: summer (vs autumn) | +0.1002 | 0.1091 | ±0.2181 | +0.919 | 0.3582 |  |
| Season: winter (vs autumn) | +0.1157 | 0.1243 | ±0.2485 | +0.931 | 0.3518 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.832** | **8.39e-12** | *** |
| BMI (kg/m2) | +0.0030 | 0.0066 | ±0.0131 | +0.452 | 0.6510 |  |
| Hypertension | +0.0279 | 0.0856 | ±0.1713 | +0.326 | 0.7442 |  |
| High cholesterol | -0.0164 | 0.0879 | ±0.1758 | -0.186 | 0.8522 |  |
| Kidney disease | -0.0035 | 0.0980 | ±0.1961 | -0.036 | 0.9714 |  |
| Circulatory disease | -0.0061 | 0.0926 | ±0.1853 | -0.065 | 0.9478 |  |
| Avg. daily time < 70 (%) | +0.0574 | 0.0545 | ±0.1089 | +1.054 | 0.2919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2096**, Adj R² = **0.1886**, F-statistic = **9.98** (p = **5.59e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.1**, BIC = **1524.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.0797** | 0.4753 | ±0.9507 | **+8.583** | **9.26e-18** | *** |
| Education: graduate level (vs college) | -0.0968 | 0.0866 | ±0.1732 | -1.118 | 0.2634 |  |
| **Education: high school or below (vs college)** | **+0.4788** | 0.1287 | ±0.2575 | **+3.720** | **2.00e-04** | *** |
| Site: UCSD (vs UAB) | +0.0694 | 0.0869 | ±0.1738 | +0.799 | 0.4245 |  |
| **Site: UW (vs UAB)** | **-0.4108** | 0.1005 | ±0.2009 | **-4.089** | **4.34e-05** | *** |
| Season: spring (vs autumn) | -0.1212 | 0.1137 | ±0.2273 | -1.066 | 0.2863 |  |
| Season: summer (vs autumn) | +0.1049 | 0.1092 | ±0.2183 | +0.961 | 0.3365 |  |
| Season: winter (vs autumn) | +0.0984 | 0.1221 | ±0.2442 | +0.806 | 0.4205 |  |
| **Age (years)** | **-0.0274** | 0.0041 | ±0.0082 | **-6.643** | **3.07e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.339 | 0.7343 |  |
| Hypertension | +0.0353 | 0.0857 | ±0.1713 | +0.412 | 0.6803 |  |
| High cholesterol | -0.0257 | 0.0864 | ±0.1727 | -0.297 | 0.7662 |  |
| Kidney disease | -0.0057 | 0.1002 | ±0.2005 | -0.057 | 0.9544 |  |
| Circulatory disease | -0.0230 | 0.0935 | ±0.1871 | -0.246 | 0.8059 |  |
| Time 54-250, pooled (%) | -0.0043 | 0.0029 | ±0.0058 | -1.484 | 0.1378 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2098**, Adj R² = **0.1888**, F-statistic = **9.99** (p = **5.34e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.0**, BIC = **1524.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.0953** | 0.4779 | ±0.9558 | **+8.569** | **1.04e-17** | *** |
| Education: graduate level (vs college) | -0.0968 | 0.0866 | ±0.1731 | -1.118 | 0.2636 |  |
| **Education: high school or below (vs college)** | **+0.4786** | 0.1287 | ±0.2574 | **+3.718** | **2.00e-04** | *** |
| Site: UCSD (vs UAB) | +0.0699 | 0.0868 | ±0.1735 | +0.806 | 0.4203 |  |
| **Site: UW (vs UAB)** | **-0.4112** | 0.1004 | ±0.2009 | **-4.094** | **4.24e-05** | *** |
| Season: spring (vs autumn) | -0.1220 | 0.1137 | ±0.2273 | -1.074 | 0.2830 |  |
| Season: summer (vs autumn) | +0.1038 | 0.1090 | ±0.2180 | +0.953 | 0.3408 |  |
| Season: winter (vs autumn) | +0.0974 | 0.1221 | ±0.2442 | +0.798 | 0.4249 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.667** | **2.60e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.335 | 0.7376 |  |
| Hypertension | +0.0358 | 0.0857 | ±0.1713 | +0.418 | 0.6763 |  |
| High cholesterol | -0.0256 | 0.0863 | ±0.1726 | -0.297 | 0.7666 |  |
| Kidney disease | -0.0072 | 0.1002 | ±0.2004 | -0.072 | 0.9429 |  |
| Circulatory disease | -0.0238 | 0.0936 | ±0.1873 | -0.254 | 0.7994 |  |
| Avg. daily time 54-250 (%) | -0.0044 | 0.0029 | ±0.0058 | -1.513 | 0.1303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2079**, Adj R² = **0.1869**, F-statistic = **9.88** (p = **9.43e-20**), Residual SE = **0.919** on **527** df, AIC = **1461.3**, BIC = **1525.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6755** | 0.4019 | ±0.8038 | **+9.145** | **5.96e-20** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0857 | ±0.1714 | -1.347 | 0.1781 |  |
| **Education: high school or below (vs college)** | **+0.4847** | 0.1318 | ±0.2637 | **+3.677** | **2.36e-04** | *** |
| Site: UCSD (vs UAB) | +0.0651 | 0.0867 | ±0.1735 | +0.751 | 0.4528 |  |
| **Site: UW (vs UAB)** | **-0.4313** | 0.1011 | ±0.2022 | **-4.266** | **1.99e-05** | *** |
| Season: spring (vs autumn) | -0.1328 | 0.1131 | ±0.2263 | -1.174 | 0.2405 |  |
| Season: summer (vs autumn) | +0.0784 | 0.1091 | ±0.2181 | +0.719 | 0.4722 |  |
| Season: winter (vs autumn) | +0.0856 | 0.1238 | ±0.2476 | +0.691 | 0.4893 |  |
| **Age (years)** | **-0.0284** | 0.0041 | ±0.0082 | **-6.933** | **4.11e-12** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0133 | +0.289 | 0.7728 |  |
| Hypertension | +0.0541 | 0.0855 | ±0.1711 | +0.633 | 0.5270 |  |
| High cholesterol | -0.0252 | 0.0860 | ±0.1720 | -0.293 | 0.7693 |  |
| Kidney disease | -0.0002 | 0.0987 | ±0.1974 | -0.002 | 0.9982 |  |
| Circulatory disease | -0.0229 | 0.0915 | ±0.1829 | -0.250 | 0.8024 |  |
| Time 181-250, pooled (%) | +0.0044 | 0.0028 | ±0.0056 | +1.561 | 0.1185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.2076**, Adj R² = **0.1866**, F-statistic = **9.86** (p = **1.03e-19**), Residual SE = **0.919** on **527** df, AIC = **1461.5**, BIC = **1525.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6767** | 0.4018 | ±0.8037 | **+9.150** | **5.69e-20** | *** |
| Education: graduate level (vs college) | -0.1161 | 0.0858 | ±0.1716 | -1.353 | 0.1761 |  |
| **Education: high school or below (vs college)** | **+0.4835** | 0.1318 | ±0.2636 | **+3.668** | **2.44e-04** | *** |
| Site: UCSD (vs UAB) | +0.0658 | 0.0868 | ±0.1736 | +0.758 | 0.4486 |  |
| **Site: UW (vs UAB)** | **-0.4301** | 0.1011 | ±0.2023 | **-4.253** | **2.11e-05** | *** |
| Season: spring (vs autumn) | -0.1324 | 0.1132 | ±0.2265 | -1.169 | 0.2425 |  |
| Season: summer (vs autumn) | +0.0785 | 0.1091 | ±0.2183 | +0.720 | 0.4718 |  |
| Season: winter (vs autumn) | +0.0853 | 0.1238 | ±0.2477 | +0.689 | 0.4907 |  |
| **Age (years)** | **-0.0283** | 0.0041 | ±0.0082 | **-6.917** | **4.62e-12** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0134 | +0.291 | 0.7708 |  |
| Hypertension | +0.0534 | 0.0857 | ±0.1715 | +0.623 | 0.5335 |  |
| High cholesterol | -0.0259 | 0.0860 | ±0.1720 | -0.301 | 0.7635 |  |
| Kidney disease | -0.0006 | 0.0987 | ±0.1974 | -0.006 | 0.9955 |  |
| Circulatory disease | -0.0221 | 0.0916 | ±0.1833 | -0.241 | 0.8094 |  |
| Avg. daily time 181-250 (%) | +0.0041 | 0.0027 | ±0.0054 | +1.518 | 0.1291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.2116**, Adj R² = **0.1906**, F-statistic = **10.10** (p = **3.09e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.8**, BIC = **1523.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6190** | 0.4063 | ±0.8127 | **+8.906** | **5.27e-19** | *** |
| Education: graduate level (vs college) | -0.1031 | 0.0857 | ±0.1715 | -1.202 | 0.2294 |  |
| **Education: high school or below (vs college)** | **+0.4725** | 0.1285 | ±0.2569 | **+3.678** | **2.35e-04** | *** |
| Site: UCSD (vs UAB) | +0.0752 | 0.0866 | ±0.1732 | +0.868 | 0.3853 |  |
| **Site: UW (vs UAB)** | **-0.4150** | 0.1003 | ±0.2007 | **-4.137** | **3.53e-05** | *** |
| Season: spring (vs autumn) | -0.1303 | 0.1135 | ±0.2271 | -1.148 | 0.2511 |  |
| Season: summer (vs autumn) | +0.0955 | 0.1085 | ±0.2169 | +0.880 | 0.3787 |  |
| Season: winter (vs autumn) | +0.0863 | 0.1219 | ±0.2438 | +0.708 | 0.4792 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0134 | +0.242 | 0.8088 |  |
| Hypertension | +0.0461 | 0.0859 | ±0.1718 | +0.537 | 0.5914 |  |
| High cholesterol | -0.0219 | 0.0864 | ±0.1728 | -0.254 | 0.7997 |  |
| Kidney disease | -0.0072 | 0.0992 | ±0.1983 | -0.073 | 0.9418 |  |
| Circulatory disease | -0.0274 | 0.0921 | ±0.1841 | -0.298 | 0.7658 |  |
| **Time > 180 (%)** | **+0.0035** | 0.0018 | ±0.0035 | **+1.981** | **0.0476** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2114**, Adj R² = **0.1904**, F-statistic = **10.09** (p = **3.28e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.9**, BIC = **1523.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6258** | 0.4061 | ±0.8121 | **+8.929** | **4.30e-19** | *** |
| Education: graduate level (vs college) | -0.1042 | 0.0857 | ±0.1715 | -1.215 | 0.2244 |  |
| **Education: high school or below (vs college)** | **+0.4716** | 0.1284 | ±0.2568 | **+3.673** | **2.40e-04** | *** |
| Site: UCSD (vs UAB) | +0.0760 | 0.0866 | ±0.1732 | +0.877 | 0.3803 |  |
| **Site: UW (vs UAB)** | **-0.4150** | 0.1004 | ±0.2007 | **-4.135** | **3.54e-05** | *** |
| Season: spring (vs autumn) | -0.1312 | 0.1136 | ±0.2272 | -1.155 | 0.2482 |  |
| Season: summer (vs autumn) | +0.0937 | 0.1084 | ±0.2168 | +0.864 | 0.3873 |  |
| Season: winter (vs autumn) | +0.0848 | 0.1220 | ±0.2440 | +0.695 | 0.4870 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.809** | **9.80e-12** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0135 | +0.240 | 0.8103 |  |
| Hypertension | +0.0464 | 0.0859 | ±0.1719 | +0.540 | 0.5889 |  |
| High cholesterol | -0.0224 | 0.0863 | ±0.1727 | -0.260 | 0.7950 |  |
| Kidney disease | -0.0084 | 0.0991 | ±0.1982 | -0.085 | 0.9325 |  |
| Circulatory disease | -0.0274 | 0.0922 | ±0.1844 | -0.297 | 0.7667 |  |
| Avg. daily time > 180 (%) | +0.0034 | 0.0017 | ±0.0035 | +1.957 | 0.0503 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2130**, Adj R² = **0.1921**, F-statistic = **10.19** (p = **2.01e-20**), Residual SE = **0.916** on **527** df, AIC = **1457.8**, BIC = **1522.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6409** | 0.4034 | ±0.8068 | **+9.025** | **1.79e-19** | *** |
| Education: graduate level (vs college) | -0.0950 | 0.0861 | ±0.1722 | -1.103 | 0.2700 |  |
| **Education: high school or below (vs college)** | **+0.4750** | 0.1287 | ±0.2575 | **+3.689** | **2.25e-04** | *** |
| Site: UCSD (vs UAB) | +0.0799 | 0.0865 | ±0.1731 | +0.923 | 0.3558 |  |
| **Site: UW (vs UAB)** | **-0.4196** | 0.1004 | ±0.2008 | **-4.180** | **2.92e-05** | *** |
| Season: spring (vs autumn) | -0.1318 | 0.1132 | ±0.2265 | -1.164 | 0.2446 |  |
| Season: summer (vs autumn) | +0.0976 | 0.1078 | ±0.2157 | +0.905 | 0.3654 |  |
| Season: winter (vs autumn) | +0.0854 | 0.1219 | ±0.2438 | +0.700 | 0.4838 |  |
| **Age (years)** | **-0.0273** | 0.0041 | ±0.0081 | **-6.706** | **1.99e-11** | *** |
| BMI (kg/m2) | +0.0008 | 0.0068 | ±0.0135 | +0.121 | 0.9035 |  |
| Hypertension | +0.0468 | 0.0857 | ±0.1714 | +0.546 | 0.5854 |  |
| High cholesterol | -0.0188 | 0.0862 | ±0.1725 | -0.218 | 0.8277 |  |
| Kidney disease | -0.0057 | 0.0989 | ±0.1977 | -0.057 | 0.9543 |  |
| Circulatory disease | -0.0292 | 0.0925 | ±0.1851 | -0.315 | 0.7526 |  |
| **Nocturnal time > 180 (%)** | **+0.0034** | 0.0015 | ±0.0031 | **+2.184** | **0.0290** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2095**, Adj R² = **0.1885**, F-statistic = **9.97** (p = **5.87e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.3**, BIC = **1524.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6548** | 0.4134 | ±0.8267 | **+8.842** | **9.43e-19** | *** |
| Education: graduate level (vs college) | -0.0971 | 0.0866 | ±0.1732 | -1.122 | 0.2620 |  |
| **Education: high school or below (vs college)** | **+0.4790** | 0.1287 | ±0.2574 | **+3.722** | **1.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.0689 | 0.0869 | ±0.1738 | +0.793 | 0.4277 |  |
| **Site: UW (vs UAB)** | **-0.4114** | 0.1005 | ±0.2010 | **-4.093** | **4.25e-05** | *** |
| Season: spring (vs autumn) | -0.1213 | 0.1136 | ±0.2273 | -1.067 | 0.2858 |  |
| Season: summer (vs autumn) | +0.1045 | 0.1092 | ±0.2184 | +0.957 | 0.3387 |  |
| Season: winter (vs autumn) | +0.0982 | 0.1221 | ±0.2443 | +0.804 | 0.4213 |  |
| **Age (years)** | **-0.0274** | 0.0041 | ±0.0082 | **-6.645** | **3.03e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.341 | 0.7333 |  |
| Hypertension | +0.0357 | 0.0857 | ±0.1713 | +0.416 | 0.6771 |  |
| High cholesterol | -0.0260 | 0.0863 | ±0.1727 | -0.301 | 0.7635 |  |
| Kidney disease | -0.0055 | 0.1003 | ±0.2005 | -0.055 | 0.9561 |  |
| Circulatory disease | -0.0231 | 0.0935 | ±0.1871 | -0.246 | 0.8053 |  |
| Time > 250 (%) | +0.0042 | 0.0029 | ±0.0058 | +1.459 | 0.1446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.2096**, Adj R² = **0.1886**, F-statistic = **9.98** (p = **5.69e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.2**, BIC = **1524.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6612** | 0.4130 | ±0.8260 | **+8.865** | **7.67e-19** | *** |
| Education: graduate level (vs college) | -0.0971 | 0.0866 | ±0.1732 | -1.122 | 0.2619 |  |
| **Education: high school or below (vs college)** | **+0.4788** | 0.1287 | ±0.2574 | **+3.721** | **1.99e-04** | *** |
| Site: UCSD (vs UAB) | +0.0694 | 0.0868 | ±0.1735 | +0.799 | 0.4240 |  |
| **Site: UW (vs UAB)** | **-0.4119** | 0.1005 | ±0.2009 | **-4.099** | **4.14e-05** | *** |
| Season: spring (vs autumn) | -0.1224 | 0.1137 | ±0.2273 | -1.077 | 0.2816 |  |
| Season: summer (vs autumn) | +0.1032 | 0.1090 | ±0.2180 | +0.946 | 0.3441 |  |
| Season: winter (vs autumn) | +0.0972 | 0.1221 | ±0.2442 | +0.796 | 0.4262 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.670** | **2.56e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.337 | 0.7361 |  |
| Hypertension | +0.0361 | 0.0857 | ±0.1713 | +0.422 | 0.6731 |  |
| High cholesterol | -0.0260 | 0.0863 | ±0.1725 | -0.301 | 0.7633 |  |
| Kidney disease | -0.0068 | 0.1002 | ±0.2005 | -0.068 | 0.9456 |  |
| Circulatory disease | -0.0238 | 0.0937 | ±0.1873 | -0.254 | 0.7993 |  |
| Avg. daily time > 250 (%) | +0.0043 | 0.0029 | ±0.0058 | +1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2559**, F-statistic = **15.31** (p = **1.41e-29**), Residual SE = **2.036** on **528** df, AIC = **2322.5**, BIC = **2382.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3803** | 0.7956 | ±1.5911 | **+29.388** | **7.76e-190** | *** |
| Education: graduate level (vs college) | -0.1217 | 0.2020 | ±0.4040 | -0.603 | 0.5467 |  |
| Education: high school or below (vs college) | +0.1466 | 0.2573 | ±0.5145 | +0.570 | 0.5688 |  |
| Site: UCSD (vs UAB) | +0.0765 | 0.2194 | ±0.4388 | +0.349 | 0.7275 |  |
| **Site: UW (vs UAB)** | **-1.2098** | 0.2192 | ±0.4384 | **-5.520** | **3.40e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2389 | ±0.4777 | -0.663 | 0.5074 |  |
| **Season: summer (vs autumn)** | **+1.9130** | 0.2706 | ±0.5411 | **+7.071** | **1.54e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9427** | 0.2532 | ±0.5064 | **-3.723** | **1.97e-04** | *** |
| Age (years) | +0.0153 | 0.0097 | ±0.0195 | +1.574 | 0.1154 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0271 | +1.437 | 0.1508 |  |
| Hypertension | +0.1339 | 0.1932 | ±0.3863 | +0.693 | 0.4882 |  |
| High cholesterol | -0.0451 | 0.1951 | ±0.3903 | -0.231 | 0.8172 |  |
| Kidney disease | -0.0735 | 0.2233 | ±0.4467 | -0.329 | 0.7420 |  |
| Circulatory disease | +0.2037 | 0.2352 | ±0.4704 | +0.866 | 0.3865 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.55e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4693** | 1.0238 | ±2.0475 | **+22.925** | **2.63e-116** | *** |
| Education: graduate level (vs college) | -0.1241 | 0.2055 | ±0.4110 | -0.604 | 0.5460 |  |
| Education: high school or below (vs college) | +0.1516 | 0.2587 | ±0.5174 | +0.586 | 0.5579 |  |
| Site: UCSD (vs UAB) | +0.0736 | 0.2233 | ±0.4466 | +0.330 | 0.7416 |  |
| **Site: UW (vs UAB)** | **-1.2132** | 0.2202 | ±0.4405 | **-5.509** | **3.62e-08** | *** |
| Season: spring (vs autumn) | -0.1607 | 0.2421 | ±0.4842 | -0.664 | 0.5068 |  |
| **Season: summer (vs autumn)** | **+1.9098** | 0.2736 | ±0.5472 | **+6.980** | **2.94e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9424** | 0.2540 | ±0.5081 | **-3.710** | **2.07e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0196 | +1.557 | 0.1194 |  |
| BMI (kg/m2) | +0.0197 | 0.0139 | ±0.0278 | +1.419 | 0.1559 |  |
| Hypertension | +0.1346 | 0.1936 | ±0.3872 | +0.695 | 0.4871 |  |
| High cholesterol | -0.0455 | 0.1960 | ±0.3920 | -0.232 | 0.8165 |  |
| Kidney disease | -0.0742 | 0.2257 | ±0.4514 | -0.329 | 0.7422 |  |
| Circulatory disease | +0.2051 | 0.2374 | ±0.4748 | +0.864 | 0.3877 |  |
| HbA1c (%) | -0.0123 | 0.0940 | ±0.1879 | -0.131 | 0.8959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **4.95e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5875** | 0.8904 | ±1.7808 | **+26.491** | **1.22e-154** | *** |
| Education: graduate level (vs college) | -0.1274 | 0.2027 | ±0.4053 | -0.629 | 0.5297 |  |
| Education: high school or below (vs college) | +0.1584 | 0.2600 | ±0.5200 | +0.609 | 0.5423 |  |
| Site: UCSD (vs UAB) | +0.0668 | 0.2216 | ±0.4433 | +0.301 | 0.7631 |  |
| **Site: UW (vs UAB)** | **-1.2184** | 0.2219 | ±0.4439 | **-5.490** | **4.03e-08** | *** |
| Season: spring (vs autumn) | -0.1546 | 0.2392 | ±0.4785 | -0.646 | 0.5181 |  |
| **Season: summer (vs autumn)** | **+1.9057** | 0.2723 | ±0.5446 | **+6.998** | **2.59e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9358** | 0.2545 | ±0.5089 | **-3.678** | **2.35e-04** | *** |
| Age (years) | +0.0150 | 0.0097 | ±0.0195 | +1.541 | 0.1234 |  |
| BMI (kg/m2) | +0.0200 | 0.0136 | ±0.0273 | +1.466 | 0.1428 |  |
| Hypertension | +0.1338 | 0.1937 | ±0.3874 | +0.691 | 0.4897 |  |
| High cholesterol | -0.0481 | 0.1956 | ±0.3913 | -0.246 | 0.8060 |  |
| Kidney disease | -0.0697 | 0.2230 | ±0.4461 | -0.312 | 0.7547 |  |
| Circulatory disease | +0.2096 | 0.2370 | ±0.4740 | +0.884 | 0.3765 |  |
| Mean glucose (mg/dL) | -0.0012 | 0.0024 | ±0.0048 | -0.488 | 0.6258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **4.95e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7478** | 1.0779 | ±2.1559 | **+22.031** | **1.47e-107** | *** |
| Education: graduate level (vs college) | -0.1274 | 0.2027 | ±0.4053 | -0.629 | 0.5297 |  |
| Education: high school or below (vs college) | +0.1584 | 0.2600 | ±0.5200 | +0.609 | 0.5423 |  |
| Site: UCSD (vs UAB) | +0.0668 | 0.2216 | ±0.4433 | +0.301 | 0.7631 |  |
| **Site: UW (vs UAB)** | **-1.2184** | 0.2219 | ±0.4439 | **-5.490** | **4.03e-08** | *** |
| Season: spring (vs autumn) | -0.1546 | 0.2392 | ±0.4785 | -0.646 | 0.5181 |  |
| **Season: summer (vs autumn)** | **+1.9057** | 0.2723 | ±0.5446 | **+6.998** | **2.59e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9358** | 0.2545 | ±0.5089 | **-3.678** | **2.35e-04** | *** |
| Age (years) | +0.0150 | 0.0097 | ±0.0195 | +1.541 | 0.1234 |  |
| BMI (kg/m2) | +0.0200 | 0.0136 | ±0.0273 | +1.466 | 0.1428 |  |
| Hypertension | +0.1338 | 0.1937 | ±0.3874 | +0.691 | 0.4897 |  |
| High cholesterol | -0.0481 | 0.1956 | ±0.3913 | -0.246 | 0.8060 |  |
| Kidney disease | -0.0697 | 0.2230 | ±0.4461 | -0.312 | 0.7547 |  |
| Circulatory disease | +0.2096 | 0.2370 | ±0.4740 | +0.884 | 0.3765 |  |
| GMI (%) | -0.0485 | 0.0994 | ±0.1987 | -0.488 | 0.6258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.2739**, Adj R² = **0.2546**, F-statistic = **14.20** (p = **5.40e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.4**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4888** | 0.8729 | ±1.7458 | **+26.908** | **1.75e-159** | *** |
| Education: graduate level (vs college) | -0.1260 | 0.2031 | ±0.4063 | -0.620 | 0.5351 |  |
| Education: high school or below (vs college) | +0.1524 | 0.2596 | ±0.5191 | +0.587 | 0.5571 |  |
| Site: UCSD (vs UAB) | +0.0704 | 0.2218 | ±0.4437 | +0.317 | 0.7509 |  |
| **Site: UW (vs UAB)** | **-1.2124** | 0.2211 | ±0.4422 | **-5.484** | **4.16e-08** | *** |
| Season: spring (vs autumn) | -0.1550 | 0.2397 | ±0.4794 | -0.647 | 0.5179 |  |
| **Season: summer (vs autumn)** | **+1.9094** | 0.2719 | ±0.5437 | **+7.023** | **2.17e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9384** | 0.2544 | ±0.5089 | **-3.688** | **2.26e-04** | *** |
| Age (years) | +0.0151 | 0.0098 | ±0.0196 | +1.539 | 0.1239 |  |
| BMI (kg/m2) | +0.0200 | 0.0138 | ±0.0277 | +1.442 | 0.1493 |  |
| Hypertension | +0.1332 | 0.1939 | ±0.3878 | +0.687 | 0.4921 |  |
| High cholesterol | -0.0469 | 0.1957 | ±0.3914 | -0.240 | 0.8106 |  |
| Kidney disease | -0.0731 | 0.2235 | ±0.4470 | -0.327 | 0.7437 |  |
| Circulatory disease | +0.2071 | 0.2373 | ±0.4745 | +0.873 | 0.3827 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0006 | 0.0023 | ±0.0046 | -0.275 | 0.7836 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2550**, F-statistic = **14.22** (p = **4.73e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5707** | 0.8563 | ±1.7126 | **+27.527** | **8.41e-167** | *** |
| Education: graduate level (vs college) | -0.1295 | 0.2028 | ±0.4057 | -0.638 | 0.5232 |  |
| Education: high school or below (vs college) | +0.1603 | 0.2598 | ±0.5195 | +0.617 | 0.5371 |  |
| Site: UCSD (vs UAB) | +0.0679 | 0.2211 | ±0.4423 | +0.307 | 0.7587 |  |
| **Site: UW (vs UAB)** | **-1.2262** | 0.2232 | ±0.4465 | **-5.492** | **3.96e-08** | *** |
| Season: spring (vs autumn) | -0.1535 | 0.2394 | ±0.4787 | -0.641 | 0.5212 |  |
| **Season: summer (vs autumn)** | **+1.9030** | 0.2723 | ±0.5446 | **+6.989** | **2.78e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9354** | 0.2536 | ±0.5072 | **-3.688** | **2.26e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0195 | +1.552 | 0.1207 |  |
| BMI (kg/m2) | +0.0198 | 0.0136 | ±0.0272 | +1.457 | 0.1451 |  |
| Hypertension | +0.1373 | 0.1936 | ±0.3871 | +0.710 | 0.4780 |  |
| High cholesterol | -0.0503 | 0.1954 | ±0.3908 | -0.258 | 0.7967 |  |
| Kidney disease | -0.0500 | 0.2263 | ±0.4527 | -0.221 | 0.8250 |  |
| Circulatory disease | +0.2093 | 0.2365 | ±0.4731 | +0.885 | 0.3762 |  |
| Glucose SD, pooled (mg/dL) | -0.0045 | 0.0077 | ±0.0155 | -0.582 | 0.5604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2748**, Adj R² = **0.2555**, F-statistic = **14.26** (p = **3.97e-29**), Residual SE = **2.036** on **527** df, AIC = **2323.8**, BIC = **2388.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6645** | 0.8631 | ±1.7263 | **+27.417** | **1.71e-165** | *** |
| Education: graduate level (vs college) | -0.1306 | 0.2028 | ±0.4056 | -0.644 | 0.5196 |  |
| Education: high school or below (vs college) | +0.1699 | 0.2600 | ±0.5200 | +0.653 | 0.5135 |  |
| Site: UCSD (vs UAB) | +0.0644 | 0.2208 | ±0.4417 | +0.291 | 0.7707 |  |
| **Site: UW (vs UAB)** | **-1.2304** | 0.2222 | ±0.4443 | **-5.538** | **3.05e-08** | *** |
| Season: spring (vs autumn) | -0.1504 | 0.2394 | ±0.4788 | -0.628 | 0.5299 |  |
| **Season: summer (vs autumn)** | **+1.8975** | 0.2721 | ±0.5442 | **+6.973** | **3.10e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9357** | 0.2534 | ±0.5067 | **-3.693** | **2.21e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0196 | +1.553 | 0.1203 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.432 | 0.1521 |  |
| Hypertension | +0.1364 | 0.1935 | ±0.3870 | +0.705 | 0.4810 |  |
| High cholesterol | -0.0514 | 0.1952 | ±0.3905 | -0.263 | 0.7924 |  |
| Kidney disease | -0.0375 | 0.2259 | ±0.4517 | -0.166 | 0.8681 |  |
| Circulatory disease | +0.2091 | 0.2364 | ±0.4727 | +0.885 | 0.3764 |  |
| Avg. daily SD (mg/dL) | -0.0073 | 0.0085 | ±0.0170 | -0.858 | 0.3909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.59e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4305** | 0.8766 | ±1.7532 | **+26.729** | **2.17e-157** | *** |
| Education: graduate level (vs college) | -0.1226 | 0.2024 | ±0.4048 | -0.606 | 0.5448 |  |
| Education: high school or below (vs college) | +0.1478 | 0.2581 | ±0.5163 | +0.573 | 0.5668 |  |
| Site: UCSD (vs UAB) | +0.0760 | 0.2199 | ±0.4398 | +0.345 | 0.7297 |  |
| **Site: UW (vs UAB)** | **-1.2125** | 0.2208 | ±0.4416 | **-5.491** | **4.00e-08** | *** |
| Season: spring (vs autumn) | -0.1584 | 0.2394 | ±0.4788 | -0.662 | 0.5081 |  |
| **Season: summer (vs autumn)** | **+1.9119** | 0.2710 | ±0.5420 | **+7.056** | **1.72e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9424** | 0.2537 | ±0.5073 | **-3.715** | **2.03e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.574 | 0.1156 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.431 | 0.1524 |  |
| Hypertension | +0.1352 | 0.1947 | ±0.3894 | +0.694 | 0.4875 |  |
| High cholesterol | -0.0457 | 0.1954 | ±0.3908 | -0.234 | 0.8149 |  |
| Kidney disease | -0.0679 | 0.2289 | ±0.4578 | -0.297 | 0.7667 |  |
| Circulatory disease | +0.2038 | 0.2356 | ±0.4712 | +0.865 | 0.3871 |  |
| CV (%) | -0.0021 | 0.0157 | ±0.0315 | -0.134 | 0.8938 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.2739**, Adj R² = **0.2546**, F-statistic = **14.20** (p = **5.40e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.4**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4992** | 0.8906 | ±1.7812 | **+26.385** | **2.03e-153** | *** |
| Education: graduate level (vs college) | -0.1198 | 0.2021 | ±0.4042 | -0.593 | 0.5533 |  |
| Education: high school or below (vs college) | +0.1444 | 0.2583 | ±0.5166 | +0.559 | 0.5760 |  |
| Site: UCSD (vs UAB) | +0.0760 | 0.2197 | ±0.4394 | +0.346 | 0.7295 |  |
| **Site: UW (vs UAB)** | **-1.2055** | 0.2203 | ±0.4406 | **-5.472** | **4.45e-08** | *** |
| Season: spring (vs autumn) | -0.1594 | 0.2395 | ±0.4790 | -0.666 | 0.5056 |  |
| **Season: summer (vs autumn)** | **+1.9122** | 0.2710 | ±0.5421 | **+7.055** | **1.72e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9441** | 0.2537 | ±0.5073 | **-3.722** | **1.97e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.569 | 0.1165 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0272 | +1.443 | 0.1490 |  |
| Hypertension | +0.1320 | 0.1941 | ±0.3882 | +0.680 | 0.4965 |  |
| High cholesterol | -0.0456 | 0.1956 | ±0.3911 | -0.233 | 0.8158 |  |
| Kidney disease | -0.0839 | 0.2271 | ±0.4541 | -0.370 | 0.7117 |  |
| Circulatory disease | +0.2021 | 0.2351 | ±0.4702 | +0.860 | 0.3899 |  |
| Mean / SD ratio | -0.0274 | 0.0875 | ±0.1751 | -0.313 | 0.7544 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.63e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3572** | 0.8824 | ±1.7648 | **+26.470** | **2.13e-154** | *** |
| Education: graduate level (vs college) | -0.1221 | 0.2026 | ±0.4052 | -0.603 | 0.5466 |  |
| Education: high school or below (vs college) | +0.1472 | 0.2583 | ±0.5165 | +0.570 | 0.5688 |  |
| Site: UCSD (vs UAB) | +0.0766 | 0.2198 | ±0.4397 | +0.348 | 0.7275 |  |
| **Site: UW (vs UAB)** | **-1.2105** | 0.2198 | ±0.4397 | **-5.506** | **3.67e-08** | *** |
| Season: spring (vs autumn) | -0.1584 | 0.2396 | ±0.4791 | -0.661 | 0.5085 |  |
| **Season: summer (vs autumn)** | **+1.9129** | 0.2712 | ±0.5424 | **+7.054** | **1.74e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9427** | 0.2538 | ±0.5076 | **-3.715** | **2.04e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.574 | 0.1156 |  |
| BMI (kg/m2) | +0.0194 | 0.0137 | ±0.0274 | +1.417 | 0.1565 |  |
| Hypertension | +0.1341 | 0.1940 | ±0.3880 | +0.691 | 0.4893 |  |
| High cholesterol | -0.0451 | 0.1954 | ±0.3908 | -0.231 | 0.8174 |  |
| Kidney disease | -0.0715 | 0.2269 | ±0.4538 | -0.315 | 0.7528 |  |
| Circulatory disease | +0.2037 | 0.2358 | ±0.4716 | +0.864 | 0.3877 |  |
| Avg. daily mean/SD | +0.0047 | 0.0783 | ±0.1567 | +0.061 | 0.9518 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.81e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6853** | 0.9466 | ±1.8931 | **+25.023** | **3.47e-138** | *** |
| Education: graduate level (vs college) | -0.1304 | 0.2043 | ±0.4085 | -0.638 | 0.5233 |  |
| Education: high school or below (vs college) | +0.1544 | 0.2561 | ±0.5122 | +0.603 | 0.5465 |  |
| Site: UCSD (vs UAB) | +0.0707 | 0.2194 | ±0.4389 | +0.322 | 0.7473 |  |
| **Site: UW (vs UAB)** | **-1.2294** | 0.2195 | ±0.4391 | **-5.600** | **2.15e-08** | *** |
| Season: spring (vs autumn) | -0.1571 | 0.2397 | ±0.4795 | -0.655 | 0.5123 |  |
| **Season: summer (vs autumn)** | **+1.9004** | 0.2707 | ±0.5415 | **+7.019** | **2.23e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9438** | 0.2536 | ±0.5072 | **-3.722** | **1.98e-04** | *** |
| Age (years) | +0.0146 | 0.0098 | ±0.0196 | +1.491 | 0.1359 |  |
| BMI (kg/m2) | +0.0193 | 0.0136 | ±0.0272 | +1.424 | 0.1543 |  |
| Hypertension | +0.1348 | 0.1934 | ±0.3869 | +0.697 | 0.4859 |  |
| High cholesterol | -0.0481 | 0.1955 | ±0.3910 | -0.246 | 0.8058 |  |
| Kidney disease | -0.0599 | 0.2257 | ±0.4513 | -0.265 | 0.7907 |  |
| Circulatory disease | +0.2056 | 0.2357 | ±0.4715 | +0.872 | 0.3831 |  |
| MAG (mg/dL/h) | -0.0054 | 0.0090 | ±0.0180 | -0.596 | 0.5513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.80e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6437** | 0.9039 | ±1.8078 | **+26.157** | **8.10e-151** | *** |
| Education: graduate level (vs college) | -0.1277 | 0.2026 | ±0.4052 | -0.630 | 0.5286 |  |
| Education: high school or below (vs college) | +0.1626 | 0.2594 | ±0.5188 | +0.627 | 0.5307 |  |
| Site: UCSD (vs UAB) | +0.0676 | 0.2204 | ±0.4408 | +0.307 | 0.7590 |  |
| **Site: UW (vs UAB)** | **-1.2236** | 0.2218 | ±0.4436 | **-5.517** | **3.45e-08** | *** |
| Season: spring (vs autumn) | -0.1510 | 0.2397 | ±0.4795 | -0.630 | 0.5288 |  |
| **Season: summer (vs autumn)** | **+1.9076** | 0.2711 | ±0.5421 | **+7.038** | **1.96e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9363** | 0.2540 | ±0.5080 | **-3.686** | **2.27e-04** | *** |
| Age (years) | +0.0150 | 0.0098 | ±0.0195 | +1.533 | 0.1253 |  |
| BMI (kg/m2) | +0.0193 | 0.0136 | ±0.0273 | +1.416 | 0.1568 |  |
| Hypertension | +0.1329 | 0.1934 | ±0.3868 | +0.687 | 0.4921 |  |
| High cholesterol | -0.0464 | 0.1953 | ±0.3906 | -0.238 | 0.8122 |  |
| Kidney disease | -0.0477 | 0.2271 | ±0.4541 | -0.210 | 0.8335 |  |
| Circulatory disease | +0.2088 | 0.2362 | ±0.4725 | +0.884 | 0.3767 |  |
| Avg. daily range (mg/dL) | -0.0015 | 0.0024 | ±0.0049 | -0.605 | 0.5454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.47e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3360** | 0.8144 | ±1.6289 | **+28.653** | **1.47e-180** | *** |
| Education: graduate level (vs college) | -0.1169 | 0.2036 | ±0.4071 | -0.574 | 0.5657 |  |
| Education: high school or below (vs college) | +0.1454 | 0.2584 | ±0.5168 | +0.563 | 0.5737 |  |
| Site: UCSD (vs UAB) | +0.0791 | 0.2215 | ±0.4430 | +0.357 | 0.7210 |  |
| **Site: UW (vs UAB)** | **-1.2040** | 0.2248 | ±0.4496 | **-5.356** | **8.51e-08** | *** |
| Season: spring (vs autumn) | -0.1579 | 0.2393 | ±0.4787 | -0.660 | 0.5095 |  |
| **Season: summer (vs autumn)** | **+1.9148** | 0.2718 | ±0.5435 | **+7.046** | **1.85e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9466** | 0.2536 | ±0.5073 | **-3.732** | **1.90e-04** | *** |
| Age (years) | +0.0156 | 0.0098 | ±0.0195 | +1.593 | 0.1111 |  |
| BMI (kg/m2) | +0.0192 | 0.0138 | ±0.0276 | +1.389 | 0.1647 |  |
| Hypertension | +0.1306 | 0.1929 | ±0.3859 | +0.677 | 0.4985 |  |
| High cholesterol | -0.0431 | 0.1957 | ±0.3915 | -0.220 | 0.8257 |  |
| Kidney disease | -0.0776 | 0.2254 | ±0.4509 | -0.344 | 0.7308 |  |
| Circulatory disease | +0.1981 | 0.2370 | ±0.4740 | +0.836 | 0.4032 |  |
| SD of daily means (mg/dL) | +0.0027 | 0.0130 | ±0.0260 | +0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.89e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2548** | 0.8456 | ±1.6912 | **+27.501** | **1.73e-166** | *** |
| Education: graduate level (vs college) | -0.1263 | 0.2026 | ±0.4052 | -0.623 | 0.5331 |  |
| Education: high school or below (vs college) | +0.1598 | 0.2604 | ±0.5208 | +0.614 | 0.5395 |  |
| Site: UCSD (vs UAB) | +0.0643 | 0.2215 | ±0.4429 | +0.290 | 0.7715 |  |
| **Site: UW (vs UAB)** | **-1.2192** | 0.2221 | ±0.4442 | **-5.489** | **4.04e-08** | *** |
| Season: spring (vs autumn) | -0.1540 | 0.2394 | ±0.4788 | -0.643 | 0.5201 |  |
| **Season: summer (vs autumn)** | **+1.9071** | 0.2723 | ±0.5446 | **+7.004** | **2.49e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9348** | 0.2546 | ±0.5093 | **-3.671** | **2.41e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.552 | 0.1207 |  |
| BMI (kg/m2) | +0.0202 | 0.0137 | ±0.0273 | +1.477 | 0.1396 |  |
| Hypertension | +0.1324 | 0.1940 | ±0.3880 | +0.683 | 0.4949 |  |
| High cholesterol | -0.0509 | 0.1959 | ±0.3918 | -0.260 | 0.7952 |  |
| Kidney disease | -0.0671 | 0.2225 | ±0.4450 | -0.302 | 0.7630 |  |
| Circulatory disease | +0.2097 | 0.2370 | ±0.4741 | +0.885 | 0.3763 |  |
| Time in range 70-180, pooled (%) | +0.0019 | 0.0038 | ±0.0075 | +0.512 | 0.6084 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.2743**, Adj R² = **0.2550**, F-statistic = **14.23** (p = **4.60e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2281** | 0.8465 | ±1.6930 | **+27.440** | **9.25e-166** | *** |
| Education: graduate level (vs college) | -0.1265 | 0.2025 | ±0.4050 | -0.625 | 0.5321 |  |
| Education: high school or below (vs college) | +0.1631 | 0.2605 | ±0.5211 | +0.626 | 0.5312 |  |
| Site: UCSD (vs UAB) | +0.0612 | 0.2216 | ±0.4431 | +0.276 | 0.7823 |  |
| **Site: UW (vs UAB)** | **-1.2212** | 0.2222 | ±0.4444 | **-5.496** | **3.88e-08** | *** |
| Season: spring (vs autumn) | -0.1526 | 0.2394 | ±0.4787 | -0.638 | 0.5237 |  |
| **Season: summer (vs autumn)** | **+1.9070** | 0.2721 | ±0.5443 | **+7.008** | **2.43e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9323** | 0.2549 | ±0.5098 | **-3.658** | **2.55e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.550 | 0.1213 |  |
| BMI (kg/m2) | +0.0203 | 0.0137 | ±0.0273 | +1.489 | 0.1365 |  |
| Hypertension | +0.1319 | 0.1941 | ±0.3881 | +0.679 | 0.4968 |  |
| High cholesterol | -0.0518 | 0.1959 | ±0.3917 | -0.264 | 0.7916 |  |
| Kidney disease | -0.0650 | 0.2223 | ±0.4446 | -0.292 | 0.7701 |  |
| Circulatory disease | +0.2109 | 0.2371 | ±0.4741 | +0.890 | 0.3736 |  |
| Avg. daily time in range 70-180 (%) | +0.0023 | 0.0037 | ±0.0075 | +0.609 | 0.5422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2745**, Adj R² = **0.2552**, F-statistic = **14.24** (p = **4.37e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.0**, BIC = **2388.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4440** | 0.8108 | ±1.6216 | **+28.915** | **7.78e-184** | *** |
| Education: graduate level (vs college) | -0.1220 | 0.2023 | ±0.4047 | -0.603 | 0.5466 |  |
| Education: high school or below (vs college) | +0.1434 | 0.2564 | ±0.5127 | +0.559 | 0.5759 |  |
| Site: UCSD (vs UAB) | +0.0659 | 0.2221 | ±0.4442 | +0.297 | 0.7667 |  |
| **Site: UW (vs UAB)** | **-1.2194** | 0.2200 | ±0.4399 | **-5.544** | **2.96e-08** | *** |
| Season: spring (vs autumn) | -0.1565 | 0.2391 | ±0.4782 | -0.654 | 0.5128 |  |
| **Season: summer (vs autumn)** | **+1.9097** | 0.2710 | ±0.5420 | **+7.047** | **1.83e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9548** | 0.2528 | ±0.5056 | **-3.777** | **1.59e-04** | *** |
| Age (years) | +0.0149 | 0.0098 | ±0.0197 | +1.515 | 0.1297 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.435 | 0.1512 |  |
| Hypertension | +0.1484 | 0.1958 | ±0.3917 | +0.758 | 0.4486 |  |
| High cholesterol | -0.0557 | 0.1938 | ±0.3877 | -0.287 | 0.7738 |  |
| Kidney disease | -0.0699 | 0.2237 | ±0.4475 | -0.312 | 0.7548 |  |
| Circulatory disease | +0.2136 | 0.2348 | ±0.4695 | +0.910 | 0.3629 |  |
| Any reading < 54 during wear (0/1) | -0.1586 | 0.2060 | ±0.4121 | -0.770 | 0.4416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **5.04e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.3**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3989** | 0.7977 | ±1.5955 | **+29.332** | **4.11e-189** | *** |
| Education: graduate level (vs college) | -0.1255 | 0.2021 | ±0.4042 | -0.621 | 0.5347 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2574 | ±0.5148 | +0.548 | 0.5837 |  |
| Site: UCSD (vs UAB) | +0.0669 | 0.2213 | ±0.4427 | +0.302 | 0.7624 |  |
| **Site: UW (vs UAB)** | **-1.2220** | 0.2203 | ±0.4407 | **-5.546** | **2.93e-08** | *** |
| Season: spring (vs autumn) | -0.1628 | 0.2397 | ±0.4795 | -0.679 | 0.4971 |  |
| **Season: summer (vs autumn)** | **+1.9065** | 0.2704 | ±0.5409 | **+7.050** | **1.79e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9511** | 0.2532 | ±0.5064 | **-3.756** | **1.73e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.579 | 0.1143 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0271 | +1.437 | 0.1506 |  |
| Hypertension | +0.1449 | 0.1959 | ±0.3918 | +0.740 | 0.4596 |  |
| High cholesterol | -0.0537 | 0.1954 | ±0.3908 | -0.275 | 0.7835 |  |
| Kidney disease | -0.0714 | 0.2237 | ±0.4475 | -0.319 | 0.7497 |  |
| Circulatory disease | +0.1962 | 0.2360 | ±0.4720 | +0.831 | 0.4058 |  |
| Time < 54 (%) | -0.1730 | 0.2859 | ±0.5719 | -0.605 | 0.5452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2744**, Adj R² = **0.2551**, F-statistic = **14.23** (p = **4.53e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3999** | 0.7966 | ±1.5932 | **+29.375** | **1.15e-189** | *** |
| Education: graduate level (vs college) | -0.1256 | 0.2021 | ±0.4042 | -0.621 | 0.5343 |  |
| Education: high school or below (vs college) | +0.1396 | 0.2575 | ±0.5149 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | +0.0660 | 0.2206 | ±0.4411 | +0.299 | 0.7648 |  |
| **Site: UW (vs UAB)** | **-1.2232** | 0.2203 | ±0.4406 | **-5.553** | **2.81e-08** | *** |
| Season: spring (vs autumn) | -0.1728 | 0.2401 | ±0.4801 | -0.720 | 0.4716 |  |
| **Season: summer (vs autumn)** | **+1.8991** | 0.2712 | ±0.5425 | **+7.001** | **2.53e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9557** | 0.2537 | ±0.5073 | **-3.768** | **1.65e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.580 | 0.1140 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0271 | +1.447 | 0.1478 |  |
| Hypertension | +0.1440 | 0.1943 | ±0.3887 | +0.741 | 0.4587 |  |
| High cholesterol | -0.0552 | 0.1953 | ±0.3907 | -0.283 | 0.7774 |  |
| Kidney disease | -0.0683 | 0.2238 | ±0.4477 | -0.305 | 0.7602 |  |
| Circulatory disease | +0.1972 | 0.2356 | ±0.4712 | +0.837 | 0.4025 |  |
| Avg. daily time < 54 (%) | -0.1739 | 0.2390 | ±0.4781 | -0.728 | 0.4668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2740**, Adj R² = **0.2547**, F-statistic = **14.21** (p = **5.16e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.3**, BIC = **2388.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3577** | 0.8002 | ±1.6005 | **+29.189** | **2.70e-187** | *** |
| Education: graduate level (vs college) | -0.1192 | 0.2030 | ±0.4059 | -0.588 | 0.5568 |  |
| Education: high school or below (vs college) | +0.1471 | 0.2575 | ±0.5150 | +0.571 | 0.5678 |  |
| Site: UCSD (vs UAB) | +0.0865 | 0.2211 | ±0.4423 | +0.391 | 0.6959 |  |
| **Site: UW (vs UAB)** | **-1.2005** | 0.2217 | ±0.4435 | **-5.414** | **6.17e-08** | *** |
| Season: spring (vs autumn) | -0.1505 | 0.2379 | ±0.4759 | -0.632 | 0.5271 |  |
| **Season: summer (vs autumn)** | **+1.9202** | 0.2693 | ±0.5385 | **+7.131** | **9.94e-13** | *** |
| **Season: winter (vs autumn)** | **-0.9350** | 0.2521 | ±0.5043 | **-3.709** | **2.08e-04** | *** |
| Age (years) | +0.0152 | 0.0097 | ±0.0195 | +1.558 | 0.1192 |  |
| BMI (kg/m2) | +0.0197 | 0.0136 | ±0.0273 | +1.444 | 0.1488 |  |
| Hypertension | +0.1261 | 0.1971 | ±0.3942 | +0.640 | 0.5223 |  |
| High cholesterol | -0.0371 | 0.1961 | ±0.3923 | -0.189 | 0.8499 |  |
| Kidney disease | -0.0781 | 0.2245 | ±0.4490 | -0.348 | 0.7278 |  |
| Circulatory disease | +0.2084 | 0.2374 | ±0.4748 | +0.878 | 0.3801 |  |
| Time 54-69, pooled (%) | +0.0427 | 0.1123 | ±0.2246 | +0.380 | 0.7040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.2744**, Adj R² = **0.2551**, F-statistic = **14.23** (p = **4.55e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3547** | 0.7983 | ±1.5966 | **+29.256** | **3.75e-188** | *** |
| Education: graduate level (vs college) | -0.1167 | 0.2025 | ±0.4051 | -0.576 | 0.5646 |  |
| Education: high school or below (vs college) | +0.1485 | 0.2574 | ±0.5147 | +0.577 | 0.5640 |  |
| Site: UCSD (vs UAB) | +0.0920 | 0.2209 | ±0.4417 | +0.417 | 0.6770 |  |
| **Site: UW (vs UAB)** | **-1.1937** | 0.2211 | ±0.4422 | **-5.398** | **6.72e-08** | *** |
| Season: spring (vs autumn) | -0.1459 | 0.2379 | ±0.4757 | -0.613 | 0.5396 |  |
| **Season: summer (vs autumn)** | **+1.9242** | 0.2695 | ±0.5390 | **+7.140** | **9.32e-13** | *** |
| **Season: winter (vs autumn)** | **-0.9313** | 0.2526 | ±0.5052 | **-3.687** | **2.27e-04** | *** |
| Age (years) | +0.0150 | 0.0097 | ±0.0195 | +1.545 | 0.1223 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0272 | +1.442 | 0.1494 |  |
| Hypertension | +0.1214 | 0.1966 | ±0.3931 | +0.617 | 0.5370 |  |
| High cholesterol | -0.0321 | 0.1959 | ±0.3918 | -0.164 | 0.8700 |  |
| Kidney disease | -0.0799 | 0.2244 | ±0.4488 | -0.356 | 0.7219 |  |
| Circulatory disease | +0.2123 | 0.2367 | ±0.4733 | +0.897 | 0.3698 |  |
| Avg. daily time 54-69 (%) | +0.0638 | 0.1019 | ±0.2038 | +0.626 | 0.5315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.48e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3671** | 0.8002 | ±1.6004 | **+29.201** | **1.89e-187** | *** |
| Education: graduate level (vs college) | -0.1201 | 0.2028 | ±0.4055 | -0.592 | 0.5537 |  |
| Education: high school or below (vs college) | +0.1475 | 0.2576 | ±0.5152 | +0.573 | 0.5669 |  |
| Site: UCSD (vs UAB) | +0.0825 | 0.2213 | ±0.4427 | +0.373 | 0.7095 |  |
| **Site: UW (vs UAB)** | **-1.2038** | 0.2215 | ±0.4430 | **-5.435** | **5.47e-08** | *** |
| Season: spring (vs autumn) | -0.1540 | 0.2384 | ±0.4768 | -0.646 | 0.5183 |  |
| **Season: summer (vs autumn)** | **+1.9173** | 0.2694 | ±0.5387 | **+7.118** | **1.10e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9379** | 0.2521 | ±0.5042 | **-3.720** | **1.99e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.565 | 0.1177 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0272 | +1.438 | 0.1506 |  |
| Hypertension | +0.1288 | 0.1976 | ±0.3952 | +0.652 | 0.5146 |  |
| High cholesterol | -0.0402 | 0.1960 | ±0.3920 | -0.205 | 0.8375 |  |
| Kidney disease | -0.0760 | 0.2243 | ±0.4486 | -0.339 | 0.7347 |  |
| Circulatory disease | +0.2069 | 0.2371 | ±0.4742 | +0.872 | 0.3829 |  |
| Time < 70 (%) | +0.0208 | 0.0881 | ±0.1762 | +0.236 | 0.8138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.2739**, Adj R² = **0.2546**, F-statistic = **14.20** (p = **5.35e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.4**, BIC = **2388.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3674** | 0.7981 | ±1.5962 | **+29.279** | **1.95e-188** | *** |
| Education: graduate level (vs college) | -0.1192 | 0.2024 | ±0.4049 | -0.589 | 0.5561 |  |
| Education: high school or below (vs college) | +0.1483 | 0.2576 | ±0.5151 | +0.576 | 0.5646 |  |
| Site: UCSD (vs UAB) | +0.0841 | 0.2210 | ±0.4421 | +0.381 | 0.7035 |  |
| **Site: UW (vs UAB)** | **-1.2015** | 0.2211 | ±0.4421 | **-5.435** | **5.48e-08** | *** |
| Season: spring (vs autumn) | -0.1513 | 0.2383 | ±0.4766 | -0.635 | 0.5253 |  |
| **Season: summer (vs autumn)** | **+1.9194** | 0.2697 | ±0.5395 | **+7.116** | **1.11e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9363** | 0.2525 | ±0.5049 | **-3.709** | **2.08e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0195 | +1.560 | 0.1189 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.435 | 0.1512 |  |
| Hypertension | +0.1275 | 0.1965 | ±0.3931 | +0.649 | 0.5165 |  |
| High cholesterol | -0.0385 | 0.1957 | ±0.3915 | -0.197 | 0.8441 |  |
| Kidney disease | -0.0768 | 0.2243 | ±0.4487 | -0.342 | 0.7322 |  |
| Circulatory disease | +0.2080 | 0.2364 | ±0.4727 | +0.880 | 0.3789 |  |
| Avg. daily time < 70 (%) | +0.0252 | 0.0875 | ±0.1749 | +0.288 | 0.7735 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3900** | 0.9239 | ±1.8477 | **+25.318** | **2.05e-141** | *** |
| Education: graduate level (vs college) | -0.1213 | 0.2033 | ±0.4066 | -0.597 | 0.5506 |  |
| Education: high school or below (vs college) | +0.1461 | 0.2593 | ±0.5187 | +0.563 | 0.5732 |  |
| Site: UCSD (vs UAB) | +0.0769 | 0.2221 | ±0.4442 | +0.346 | 0.7291 |  |
| **Site: UW (vs UAB)** | **-1.2093** | 0.2225 | ±0.4450 | **-5.434** | **5.50e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2395 | ±0.4790 | -0.661 | 0.5086 |  |
| **Season: summer (vs autumn)** | **+1.9136** | 0.2725 | ±0.5450 | **+7.022** | **2.19e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9427** | 0.2538 | ±0.5076 | **-3.715** | **2.04e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0196 | +1.571 | 0.1161 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.424 | 0.1543 |  |
| Hypertension | +0.1337 | 0.1926 | ±0.3851 | +0.694 | 0.4875 |  |
| High cholesterol | -0.0450 | 0.1956 | ±0.3912 | -0.230 | 0.8182 |  |
| Kidney disease | -0.0738 | 0.2238 | ±0.4476 | -0.330 | 0.7416 |  |
| Circulatory disease | +0.2035 | 0.2368 | ±0.4735 | +0.859 | 0.3901 |  |
| Time 54-250, pooled (%) | -0.0001 | 0.0055 | ±0.0111 | -0.022 | 0.9825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3663** | 0.9347 | ±1.8694 | **+24.999** | **6.26e-138** | *** |
| Education: graduate level (vs college) | -0.1223 | 0.2034 | ±0.4067 | -0.601 | 0.5476 |  |
| Education: high school or below (vs college) | +0.1473 | 0.2592 | ±0.5184 | +0.568 | 0.5699 |  |
| Site: UCSD (vs UAB) | +0.0759 | 0.2221 | ±0.4443 | +0.341 | 0.7328 |  |
| **Site: UW (vs UAB)** | **-1.2106** | 0.2225 | ±0.4450 | **-5.441** | **5.31e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2394 | ±0.4789 | -0.661 | 0.5085 |  |
| **Season: summer (vs autumn)** | **+1.9123** | 0.2725 | ±0.5451 | **+7.016** | **2.28e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9425** | 0.2538 | ±0.5076 | **-3.714** | **2.04e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.568 | 0.1169 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.427 | 0.1536 |  |
| Hypertension | +0.1342 | 0.1926 | ±0.3852 | +0.697 | 0.4861 |  |
| High cholesterol | -0.0453 | 0.1956 | ±0.3912 | -0.232 | 0.8167 |  |
| Kidney disease | -0.0731 | 0.2238 | ±0.4476 | -0.327 | 0.7440 |  |
| Circulatory disease | +0.2040 | 0.2369 | ±0.4737 | +0.861 | 0.3891 |  |
| Avg. daily time 54-250 (%) | +0.0002 | 0.0056 | ±0.0112 | +0.030 | 0.9757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2751**, Adj R² = **0.2559**, F-statistic = **14.29** (p = **3.48e-29**), Residual SE = **2.036** on **527** df, AIC = **2323.5**, BIC = **2387.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4691** | 0.7961 | ±1.5922 | **+29.480** | **5.21e-191** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.2023 | ±0.4046 | -0.571 | 0.5683 |  |
| Education: high school or below (vs college) | +0.1633 | 0.2591 | ±0.5182 | +0.630 | 0.5284 |  |
| Site: UCSD (vs UAB) | +0.0609 | 0.2186 | ±0.4371 | +0.279 | 0.7804 |  |
| **Site: UW (vs UAB)** | **-1.2093** | 0.2202 | ±0.4404 | **-5.491** | **3.99e-08** | *** |
| Season: spring (vs autumn) | -0.1425 | 0.2403 | ±0.4807 | -0.593 | 0.5532 |  |
| **Season: summer (vs autumn)** | **+1.9232** | 0.2698 | ±0.5397 | **+7.127** | **1.02e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9205** | 0.2565 | ±0.5131 | **-3.588** | **3.33e-04** | *** |
| Age (years) | +0.0157 | 0.0098 | ±0.0196 | +1.600 | 0.1096 |  |
| BMI (kg/m2) | +0.0208 | 0.0136 | ±0.0271 | +1.537 | 0.1243 |  |
| Hypertension | +0.1175 | 0.1951 | ±0.3903 | +0.602 | 0.5472 |  |
| High cholesterol | -0.0540 | 0.1960 | ±0.3921 | -0.275 | 0.7830 |  |
| Kidney disease | -0.0676 | 0.2226 | ±0.4452 | -0.304 | 0.7613 |  |
| Circulatory disease | +0.2136 | 0.2363 | ±0.4726 | +0.904 | 0.3661 |  |
| Time 181-250, pooled (%) | -0.0062 | 0.0060 | ±0.0120 | -1.032 | 0.3022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.2755**, Adj R² = **0.2563**, F-statistic = **14.31** (p = **3.09e-29**), Residual SE = **2.035** on **527** df, AIC = **2323.2**, BIC = **2387.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4813** | 0.7976 | ±1.5952 | **+29.440** | **1.70e-190** | *** |
| Education: graduate level (vs college) | -0.1134 | 0.2022 | ±0.4045 | -0.561 | 0.5751 |  |
| Education: high school or below (vs college) | +0.1680 | 0.2595 | ±0.5190 | +0.647 | 0.5173 |  |
| Site: UCSD (vs UAB) | +0.0573 | 0.2187 | ±0.4373 | +0.262 | 0.7931 |  |
| **Site: UW (vs UAB)** | **-1.2112** | 0.2204 | ±0.4407 | **-5.497** | **3.87e-08** | *** |
| Season: spring (vs autumn) | -0.1407 | 0.2403 | ±0.4806 | -0.585 | 0.5583 |  |
| **Season: summer (vs autumn)** | **+1.9247** | 0.2699 | ±0.5398 | **+7.131** | **9.99e-13** | *** |
| **Season: winter (vs autumn)** | **-0.9165** | 0.2570 | ±0.5140 | **-3.566** | **3.62e-04** | *** |
| Age (years) | +0.0156 | 0.0098 | ±0.0195 | +1.596 | 0.1105 |  |
| BMI (kg/m2) | +0.0210 | 0.0136 | ±0.0271 | +1.551 | 0.1210 |  |
| Hypertension | +0.1160 | 0.1951 | ±0.3903 | +0.595 | 0.5521 |  |
| High cholesterol | -0.0543 | 0.1960 | ±0.3920 | -0.277 | 0.7816 |  |
| Kidney disease | -0.0661 | 0.2224 | ±0.4448 | -0.297 | 0.7663 |  |
| Circulatory disease | +0.2139 | 0.2364 | ±0.4728 | +0.905 | 0.3657 |  |
| Avg. daily time 181-250 (%) | -0.0068 | 0.0059 | ±0.0119 | -1.142 | 0.2536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.88e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4463** | 0.8007 | ±1.6013 | **+29.284** | **1.66e-188** | *** |
| Education: graduate level (vs college) | -0.1261 | 0.2026 | ±0.4051 | -0.623 | 0.5335 |  |
| Education: high school or below (vs college) | +0.1599 | 0.2604 | ±0.5208 | +0.614 | 0.5391 |  |
| Site: UCSD (vs UAB) | +0.0648 | 0.2213 | ±0.4425 | +0.293 | 0.7695 |  |
| **Site: UW (vs UAB)** | **-1.2187** | 0.2219 | ±0.4438 | **-5.492** | **3.97e-08** | *** |
| Season: spring (vs autumn) | -0.1536 | 0.2394 | ±0.4788 | -0.641 | 0.5212 |  |
| **Season: summer (vs autumn)** | **+1.9075** | 0.2722 | ±0.5445 | **+7.007** | **2.43e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9344** | 0.2546 | ±0.5092 | **-3.670** | **2.43e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.551 | 0.1208 |  |
| BMI (kg/m2) | +0.0202 | 0.0137 | ±0.0273 | +1.478 | 0.1395 |  |
| Hypertension | +0.1319 | 0.1941 | ±0.3882 | +0.680 | 0.4968 |  |
| High cholesterol | -0.0504 | 0.1958 | ±0.3917 | -0.257 | 0.7968 |  |
| Kidney disease | -0.0673 | 0.2226 | ±0.4451 | -0.302 | 0.7623 |  |
| Circulatory disease | +0.2100 | 0.2371 | ±0.4742 | +0.886 | 0.3757 |  |
| Time > 180 (%) | -0.0019 | 0.0037 | ±0.0075 | -0.519 | 0.6040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2743**, Adj R² = **0.2551**, F-statistic = **14.23** (p = **4.57e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4561** | 0.8003 | ±1.6006 | **+29.309** | **7.95e-189** | *** |
| Education: graduate level (vs college) | -0.1264 | 0.2025 | ±0.4050 | -0.624 | 0.5326 |  |
| Education: high school or below (vs college) | +0.1635 | 0.2605 | ±0.5211 | +0.627 | 0.5304 |  |
| Site: UCSD (vs UAB) | +0.0618 | 0.2214 | ±0.4427 | +0.279 | 0.7802 |  |
| **Site: UW (vs UAB)** | **-1.2206** | 0.2220 | ±0.4439 | **-5.499** | **3.82e-08** | *** |
| Season: spring (vs autumn) | -0.1519 | 0.2394 | ±0.4787 | -0.635 | 0.5256 |  |
| **Season: summer (vs autumn)** | **+1.9075** | 0.2720 | ±0.5441 | **+7.012** | **2.35e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9316** | 0.2549 | ±0.5098 | **-3.655** | **2.57e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.548 | 0.1215 |  |
| BMI (kg/m2) | +0.0203 | 0.0137 | ±0.0273 | +1.489 | 0.1364 |  |
| Hypertension | +0.1313 | 0.1942 | ±0.3884 | +0.676 | 0.4991 |  |
| High cholesterol | -0.0512 | 0.1958 | ±0.3917 | -0.262 | 0.7937 |  |
| Kidney disease | -0.0652 | 0.2223 | ±0.4446 | -0.293 | 0.7694 |  |
| Circulatory disease | +0.2114 | 0.2371 | ±0.4743 | +0.891 | 0.3727 |  |
| Avg. daily time > 180 (%) | -0.0023 | 0.0037 | ±0.0074 | -0.620 | 0.5350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **4.98e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.3**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4259** | 0.7982 | ±1.5963 | **+29.350** | **2.40e-189** | *** |
| Education: graduate level (vs college) | -0.1293 | 0.2035 | ±0.4070 | -0.635 | 0.5253 |  |
| Education: high school or below (vs college) | +0.1567 | 0.2598 | ±0.5195 | +0.603 | 0.5463 |  |
| Site: UCSD (vs UAB) | +0.0644 | 0.2219 | ±0.4439 | +0.290 | 0.7717 |  |
| **Site: UW (vs UAB)** | **-1.2151** | 0.2215 | ±0.4430 | **-5.486** | **4.11e-08** | *** |
| Season: spring (vs autumn) | -0.1536 | 0.2396 | ±0.4792 | -0.641 | 0.5215 |  |
| **Season: summer (vs autumn)** | **+1.9074** | 0.2719 | ±0.5438 | **+7.015** | **2.30e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9352** | 0.2544 | ±0.5089 | **-3.676** | **2.37e-04** | *** |
| Age (years) | +0.0150 | 0.0098 | ±0.0195 | +1.530 | 0.1260 |  |
| BMI (kg/m2) | +0.0204 | 0.0139 | ±0.0278 | +1.471 | 0.1414 |  |
| Hypertension | +0.1319 | 0.1941 | ±0.3882 | +0.680 | 0.4968 |  |
| High cholesterol | -0.0511 | 0.1957 | ±0.3914 | -0.261 | 0.7941 |  |
| Kidney disease | -0.0690 | 0.2226 | ±0.4451 | -0.310 | 0.7565 |  |
| Circulatory disease | +0.2099 | 0.2375 | ±0.4750 | +0.884 | 0.3769 |  |
| Nocturnal time > 180 (%) | -0.0016 | 0.0034 | ±0.0068 | -0.460 | 0.6453 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3772** | 0.8019 | ±1.6038 | **+29.152** | **7.95e-187** | *** |
| Education: graduate level (vs college) | -0.1212 | 0.2033 | ±0.4066 | -0.596 | 0.5509 |  |
| Education: high school or below (vs college) | +0.1459 | 0.2593 | ±0.5187 | +0.563 | 0.5736 |  |
| Site: UCSD (vs UAB) | +0.0770 | 0.2220 | ±0.4441 | +0.347 | 0.7287 |  |
| **Site: UW (vs UAB)** | **-1.2091** | 0.2224 | ±0.4449 | **-5.436** | **5.46e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2395 | ±0.4790 | -0.661 | 0.5086 |  |
| **Season: summer (vs autumn)** | **+1.9137** | 0.2725 | ±0.5450 | **+7.023** | **2.18e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9428** | 0.2538 | ±0.5076 | **-3.715** | **2.03e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0196 | +1.572 | 0.1160 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.424 | 0.1544 |  |
| Hypertension | +0.1336 | 0.1926 | ±0.3852 | +0.694 | 0.4877 |  |
| High cholesterol | -0.0449 | 0.1956 | ±0.3912 | -0.230 | 0.8184 |  |
| Kidney disease | -0.0739 | 0.2238 | ±0.4476 | -0.330 | 0.7414 |  |
| Circulatory disease | +0.2034 | 0.2368 | ±0.4736 | +0.859 | 0.3903 |  |
| Time > 250 (%) | +0.0002 | 0.0055 | ±0.0111 | +0.028 | 0.9776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3822** | 0.8005 | ±1.6011 | **+29.208** | **1.55e-187** | *** |
| Education: graduate level (vs college) | -0.1221 | 0.2034 | ±0.4067 | -0.600 | 0.5483 |  |
| Education: high school or below (vs college) | +0.1470 | 0.2592 | ±0.5185 | +0.567 | 0.5706 |  |
| Site: UCSD (vs UAB) | +0.0761 | 0.2221 | ±0.4441 | +0.343 | 0.7318 |  |
| **Site: UW (vs UAB)** | **-1.2103** | 0.2224 | ±0.4449 | **-5.441** | **5.29e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2395 | ±0.4789 | -0.661 | 0.5085 |  |
| **Season: summer (vs autumn)** | **+1.9126** | 0.2725 | ±0.5450 | **+7.019** | **2.24e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9426** | 0.2538 | ±0.5075 | **-3.714** | **2.04e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.569 | 0.1166 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.426 | 0.1538 |  |
| Hypertension | +0.1340 | 0.1926 | ±0.3852 | +0.696 | 0.4865 |  |
| High cholesterol | -0.0452 | 0.1956 | ±0.3912 | -0.231 | 0.8171 |  |
| Kidney disease | -0.0732 | 0.2238 | ±0.4476 | -0.327 | 0.7434 |  |
| Circulatory disease | +0.2039 | 0.2369 | ±0.4738 | +0.861 | 0.3895 |  |
| Avg. daily time > 250 (%) | -0.0001 | 0.0056 | ±0.0112 | -0.019 | 0.9852 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2315**, F-statistic = **13.53** (p = **4.25e-26**), Residual SE = **6.040** on **528** df, AIC = **3501.4**, BIC = **3561.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1538** | 2.3990 | ±4.7980 | **+21.323** | **6.97e-101** | *** |
| Education: graduate level (vs college) | +0.1829 | 0.6303 | ±1.2605 | +0.290 | 0.7717 |  |
| Education: high school or below (vs college) | +0.4016 | 0.7317 | ±1.4634 | +0.549 | 0.5831 |  |
| **Site: UCSD (vs UAB)** | **+3.4065** | 0.6552 | ±1.3104 | **+5.199** | **2.00e-07** | *** |
| Site: UW (vs UAB) | -0.4409 | 0.6334 | ±1.2667 | -0.696 | 0.4863 |  |
| **Season: spring (vs autumn)** | **-2.3146** | 0.7562 | ±1.5123 | **-3.061** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5325** | 0.7352 | ±1.4705 | **+2.084** | **0.0371** | * |
| **Season: winter (vs autumn)** | **-5.7683** | 0.8499 | ±1.6997 | **-6.787** | **1.14e-11** | *** |
| Age (years) | -0.0526 | 0.0275 | ±0.0550 | -1.911 | 0.0560 | . |
| BMI (kg/m2) | -0.0602 | 0.0406 | ±0.0812 | -1.483 | 0.1380 |  |
| Hypertension | -1.0000 | 0.6180 | ±1.2361 | -1.618 | 0.1057 |  |
| High cholesterol | -0.2631 | 0.5833 | ±1.1666 | -0.451 | 0.6520 |  |
| **Kidney disease** | **+1.5243** | 0.6625 | ±1.3251 | **+2.301** | **0.0214** | * |
| Circulatory disease | -0.2638 | 0.6638 | ±1.3277 | -0.397 | 0.6911 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.58** (p = **1.37e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3221** | 2.7314 | ±5.4627 | **+18.424** | **8.48e-76** | *** |
| Education: graduate level (vs college) | +0.2045 | 0.6299 | ±1.2599 | +0.325 | 0.7455 |  |
| Education: high school or below (vs college) | +0.3549 | 0.7330 | ±1.4660 | +0.484 | 0.6282 |  |
| **Site: UCSD (vs UAB)** | **+3.4330** | 0.6601 | ±1.3201 | **+5.201** | **1.98e-07** | *** |
| Site: UW (vs UAB) | -0.4098 | 0.6359 | ±1.2718 | -0.644 | 0.5193 |  |
| **Season: spring (vs autumn)** | **-2.2925** | 0.7598 | ±1.5197 | **-3.017** | **0.0026** | ** |
| **Season: summer (vs autumn)** | **+1.5622** | 0.7382 | ±1.4763 | **+2.116** | **0.0343** | * |
| **Season: winter (vs autumn)** | **-5.7706** | 0.8522 | ±1.7044 | **-6.771** | **1.28e-11** | *** |
| Age (years) | -0.0516 | 0.0275 | ±0.0550 | -1.875 | 0.0607 | . |
| BMI (kg/m2) | -0.0627 | 0.0409 | ±0.0818 | -1.533 | 0.1253 |  |
| Hypertension | -1.0063 | 0.6183 | ±1.2366 | -1.628 | 0.1036 |  |
| High cholesterol | -0.2598 | 0.5839 | ±1.1679 | -0.445 | 0.6564 |  |
| **Kidney disease** | **+1.5311** | 0.6623 | ±1.3245 | **+2.312** | **0.0208** | * |
| Circulatory disease | -0.2768 | 0.6648 | ±1.3296 | -0.416 | 0.6771 |  |
| HbA1c (%) | +0.1149 | 0.2000 | ±0.3999 | +0.574 | 0.5657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.2518**, Adj R² = **0.2319**, F-statistic = **12.67** (p = **8.86e-26**), Residual SE = **6.039** on **527** df, AIC = **3502.1**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8365** | 2.5483 | ±5.0965 | **+19.557** | **3.60e-85** | *** |
| Education: graduate level (vs college) | +0.2187 | 0.6303 | ±1.2607 | +0.347 | 0.7287 |  |
| Education: high school or below (vs college) | +0.3264 | 0.7312 | ±1.4624 | +0.446 | 0.6553 |  |
| **Site: UCSD (vs UAB)** | **+3.4678** | 0.6615 | ±1.3230 | **+5.242** | **1.59e-07** | *** |
| Site: UW (vs UAB) | -0.3868 | 0.6375 | ±1.2750 | -0.607 | 0.5440 |  |
| **Season: spring (vs autumn)** | **-2.3384** | 0.7566 | ±1.5131 | **-3.091** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5793** | 0.7372 | ±1.4745 | **+2.142** | **0.0322** | * |
| **Season: winter (vs autumn)** | **-5.8117** | 0.8532 | ±1.7063 | **-6.812** | **9.63e-12** | *** |
| Age (years) | -0.0505 | 0.0274 | ±0.0548 | -1.845 | 0.0651 | . |
| BMI (kg/m2) | -0.0635 | 0.0408 | ±0.0815 | -1.557 | 0.1194 |  |
| Hypertension | -0.9993 | 0.6186 | ±1.2372 | -1.615 | 0.1062 |  |
| High cholesterol | -0.2444 | 0.5842 | ±1.1684 | -0.418 | 0.6757 |  |
| **Kidney disease** | **+1.4999** | 0.6605 | ±1.3211 | **+2.271** | **0.0232** | * |
| Circulatory disease | -0.3016 | 0.6637 | ±1.3275 | -0.454 | 0.6496 |  |
| Mean glucose (mg/dL) | +0.0074 | 0.0068 | ±0.0136 | +1.084 | 0.2784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.2518**, Adj R² = **0.2319**, F-statistic = **12.67** (p = **8.86e-26**), Residual SE = **6.039** on **527** df, AIC = **3502.1**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8167** | 3.0169 | ±6.0339 | **+16.181** | **6.89e-59** | *** |
| Education: graduate level (vs college) | +0.2187 | 0.6303 | ±1.2607 | +0.347 | 0.7287 |  |
| Education: high school or below (vs college) | +0.3264 | 0.7312 | ±1.4624 | +0.446 | 0.6553 |  |
| **Site: UCSD (vs UAB)** | **+3.4678** | 0.6615 | ±1.3230 | **+5.242** | **1.59e-07** | *** |
| Site: UW (vs UAB) | -0.3868 | 0.6375 | ±1.2750 | -0.607 | 0.5440 |  |
| **Season: spring (vs autumn)** | **-2.3384** | 0.7566 | ±1.5131 | **-3.091** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5793** | 0.7372 | ±1.4745 | **+2.142** | **0.0322** | * |
| **Season: winter (vs autumn)** | **-5.8117** | 0.8532 | ±1.7063 | **-6.812** | **9.63e-12** | *** |
| Age (years) | -0.0505 | 0.0274 | ±0.0548 | -1.845 | 0.0651 | . |
| BMI (kg/m2) | -0.0635 | 0.0408 | ±0.0815 | -1.557 | 0.1194 |  |
| Hypertension | -0.9993 | 0.6186 | ±1.2372 | -1.615 | 0.1062 |  |
| High cholesterol | -0.2444 | 0.5842 | ±1.1684 | -0.418 | 0.6757 |  |
| **Kidney disease** | **+1.4999** | 0.6605 | ±1.3211 | **+2.271** | **0.0232** | * |
| Circulatory disease | -0.3016 | 0.6637 | ±1.3275 | -0.454 | 0.6496 |  |
| GMI (%) | +0.3081 | 0.2842 | ±0.5684 | +1.084 | 0.2784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.2507**, Adj R² = **0.2308**, F-statistic = **12.59** (p = **1.26e-25**), Residual SE = **6.043** on **527** df, AIC = **3502.9**, BIC = **3567.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3977** | 2.5126 | ±5.0252 | **+20.058** | **1.72e-89** | *** |
| Education: graduate level (vs college) | +0.2125 | 0.6318 | ±1.2637 | +0.336 | 0.7366 |  |
| Education: high school or below (vs college) | +0.3611 | 0.7323 | ±1.4646 | +0.493 | 0.6220 |  |
| **Site: UCSD (vs UAB)** | **+3.4486** | 0.6627 | ±1.3254 | **+5.204** | **1.95e-07** | *** |
| Site: UW (vs UAB) | -0.4230 | 0.6357 | ±1.2714 | -0.665 | 0.5058 |  |
| **Season: spring (vs autumn)** | **-2.3380** | 0.7569 | ±1.5137 | **-3.089** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5576** | 0.7373 | ±1.4746 | **+2.113** | **0.0346** | * |
| **Season: winter (vs autumn)** | **-5.7978** | 0.8538 | ±1.7076 | **-6.791** | **1.12e-11** | *** |
| Age (years) | -0.0506 | 0.0274 | ±0.0548 | -1.847 | 0.0647 | . |
| BMI (kg/m2) | -0.0635 | 0.0411 | ±0.0822 | -1.545 | 0.1222 |  |
| Hypertension | -0.9954 | 0.6185 | ±1.2371 | -1.609 | 0.1076 |  |
| High cholesterol | -0.2507 | 0.5843 | ±1.1686 | -0.429 | 0.6678 |  |
| **Kidney disease** | **+1.5211** | 0.6624 | ±1.3248 | **+2.296** | **0.0217** | * |
| Circulatory disease | -0.2879 | 0.6644 | ±1.3288 | -0.433 | 0.6647 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0044 | 0.0062 | ±0.0123 | +0.711 | 0.4770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.41e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6633** | 2.6154 | ±5.2309 | **+19.371** | **1.36e-83** | *** |
| Education: graduate level (vs college) | +0.2029 | 0.6347 | ±1.2693 | +0.320 | 0.7492 |  |
| Education: high school or below (vs college) | +0.3662 | 0.7282 | ±1.4564 | +0.503 | 0.6150 |  |
| **Site: UCSD (vs UAB)** | **+3.4284** | 0.6623 | ±1.3245 | **+5.177** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.3989 | 0.6422 | ±1.2845 | -0.621 | 0.5346 |  |
| **Season: spring (vs autumn)** | **-2.3270** | 0.7559 | ±1.5117 | **-3.079** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5584** | 0.7426 | ±1.4852 | **+2.099** | **0.0358** | * |
| **Season: winter (vs autumn)** | **-5.7869** | 0.8490 | ±1.6981 | **-6.816** | **9.38e-12** | *** |
| Age (years) | -0.0521 | 0.0276 | ±0.0552 | -1.889 | 0.0588 | . |
| BMI (kg/m2) | -0.0612 | 0.0407 | ±0.0814 | -1.503 | 0.1329 |  |
| Hypertension | -1.0089 | 0.6183 | ±1.2366 | -1.632 | 0.1027 |  |
| High cholesterol | -0.2497 | 0.5847 | ±1.1695 | -0.427 | 0.6694 |  |
| **Kidney disease** | **+1.4638** | 0.6665 | ±1.3330 | **+2.196** | **0.0281** | * |
| Circulatory disease | -0.2784 | 0.6668 | ±1.3336 | -0.418 | 0.6763 |  |
| Glucose SD, pooled (mg/dL) | +0.0116 | 0.0216 | ±0.0432 | +0.538 | 0.5908 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.57** (p = **1.39e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6125** | 2.6118 | ±5.2235 | **+19.379** | **1.17e-83** | *** |
| Education: graduate level (vs college) | +0.1997 | 0.6346 | ±1.2693 | +0.315 | 0.7530 |  |
| Education: high school or below (vs college) | +0.3573 | 0.7294 | ±1.4588 | +0.490 | 0.6243 |  |
| **Site: UCSD (vs UAB)** | **+3.4295** | 0.6632 | ±1.3263 | **+5.171** | **2.32e-07** | *** |
| Site: UW (vs UAB) | -0.4017 | 0.6418 | ±1.2837 | -0.626 | 0.5314 |  |
| **Season: spring (vs autumn)** | **-2.3298** | 0.7557 | ±1.5113 | **-3.083** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5622** | 0.7436 | ±1.4873 | **+2.101** | **0.0357** | * |
| **Season: winter (vs autumn)** | **-5.7816** | 0.8489 | ±1.6977 | **-6.811** | **9.69e-12** | *** |
| Age (years) | -0.0523 | 0.0276 | ±0.0552 | -1.896 | 0.0580 | . |
| BMI (kg/m2) | -0.0602 | 0.0407 | ±0.0814 | -1.479 | 0.1391 |  |
| Hypertension | -1.0047 | 0.6186 | ±1.2371 | -1.624 | 0.1043 |  |
| High cholesterol | -0.2511 | 0.5843 | ±1.1687 | -0.430 | 0.6674 |  |
| **Kidney disease** | **+1.4556** | 0.6674 | ±1.3349 | **+2.181** | **0.0292** | * |
| Circulatory disease | -0.2741 | 0.6667 | ±1.3333 | -0.411 | 0.6809 |  |
| Avg. daily SD (mg/dL) | +0.0139 | 0.0249 | ±0.0498 | +0.560 | 0.5758 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.44e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7043** | 2.7987 | ±5.5975 | **+18.474** | **3.34e-76** | *** |
| Education: graduate level (vs college) | +0.1740 | 0.6337 | ±1.2673 | +0.275 | 0.7836 |  |
| Education: high school or below (vs college) | +0.4153 | 0.7293 | ±1.4585 | +0.569 | 0.5691 |  |
| **Site: UCSD (vs UAB)** | **+3.4010** | 0.6572 | ±1.3144 | **+5.175** | **2.28e-07** | *** |
| Site: UW (vs UAB) | -0.4695 | 0.6380 | ±1.2760 | -0.736 | 0.4618 |  |
| **Season: spring (vs autumn)** | **-2.3153** | 0.7572 | ±1.5145 | **-3.058** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5209** | 0.7377 | ±1.4755 | **+2.062** | **0.0392** | * |
| **Season: winter (vs autumn)** | **-5.7660** | 0.8519 | ±1.7039 | **-6.768** | **1.30e-11** | *** |
| Age (years) | -0.0523 | 0.0275 | ±0.0550 | -1.900 | 0.0574 | . |
| BMI (kg/m2) | -0.0605 | 0.0406 | ±0.0813 | -1.489 | 0.1365 |  |
| Hypertension | -0.9857 | 0.6171 | ±1.2342 | -1.597 | 0.1102 |  |
| High cholesterol | -0.2700 | 0.5842 | ±1.1684 | -0.462 | 0.6439 |  |
| **Kidney disease** | **+1.5856** | 0.6675 | ±1.3350 | **+2.375** | **0.0175** | * |
| Circulatory disease | -0.2629 | 0.6644 | ±1.3287 | -0.396 | 0.6923 |  |
| CV (%) | -0.0230 | 0.0486 | ±0.0971 | -0.474 | 0.6352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6595** | 2.5242 | ±5.0483 | **+20.070** | **1.36e-89** | *** |
| Education: graduate level (vs college) | +0.1749 | 0.6345 | ±1.2691 | +0.276 | 0.7828 |  |
| Education: high school or below (vs college) | +0.4106 | 0.7295 | ±1.4590 | +0.563 | 0.5735 |  |
| **Site: UCSD (vs UAB)** | **+3.4086** | 0.6558 | ±1.3116 | **+5.198** | **2.02e-07** | *** |
| Site: UW (vs UAB) | -0.4588 | 0.6366 | ±1.2732 | -0.721 | 0.4710 |  |
| **Season: spring (vs autumn)** | **-2.3101** | 0.7565 | ±1.5129 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5358** | 0.7347 | ±1.4695 | **+2.090** | **0.0366** | * |
| **Season: winter (vs autumn)** | **-5.7621** | 0.8509 | ±1.7018 | **-6.772** | **1.27e-11** | *** |
| Age (years) | -0.0524 | 0.0275 | ±0.0551 | -1.904 | 0.0569 | . |
| BMI (kg/m2) | -0.0607 | 0.0407 | ±0.0814 | -1.492 | 0.1358 |  |
| Hypertension | -0.9921 | 0.6174 | ±1.2348 | -1.607 | 0.1081 |  |
| High cholesterol | -0.2612 | 0.5845 | ±1.1690 | -0.447 | 0.6549 |  |
| **Kidney disease** | **+1.5675** | 0.6630 | ±1.3260 | **+2.364** | **0.0181** | * |
| Circulatory disease | -0.2574 | 0.6654 | ±1.3309 | -0.387 | 0.6990 |  |
| Mean / SD ratio | +0.1139 | 0.2693 | ±0.5386 | +0.423 | 0.6723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.50e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7566** | 2.5434 | ±5.0868 | **+19.956** | **1.33e-88** | *** |
| Education: graduate level (vs college) | +0.1761 | 0.6351 | ±1.2703 | +0.277 | 0.7816 |  |
| Education: high school or below (vs college) | +0.4116 | 0.7304 | ±1.4608 | +0.564 | 0.5731 |  |
| **Site: UCSD (vs UAB)** | **+3.4089** | 0.6559 | ±1.3117 | **+5.198** | **2.02e-07** | *** |
| Site: UW (vs UAB) | -0.4513 | 0.6361 | ±1.2722 | -0.710 | 0.4780 |  |
| **Season: spring (vs autumn)** | **-2.3156** | 0.7581 | ±1.5162 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5304** | 0.7372 | ±1.4743 | **+2.076** | **0.0379** | * |
| **Season: winter (vs autumn)** | **-5.7695** | 0.8529 | ±1.7058 | **-6.765** | **1.34e-11** | *** |
| Age (years) | -0.0523 | 0.0276 | ±0.0552 | -1.894 | 0.0582 | . |
| BMI (kg/m2) | -0.0614 | 0.0410 | ±0.0819 | -1.500 | 0.1337 |  |
| Hypertension | -0.9958 | 0.6181 | ±1.2362 | -1.611 | 0.1072 |  |
| High cholesterol | -0.2632 | 0.5845 | ±1.1689 | -0.450 | 0.6525 |  |
| **Kidney disease** | **+1.5592** | 0.6619 | ±1.3238 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.2632 | 0.6644 | ±1.3289 | -0.396 | 0.6920 |  |
| Avg. daily mean/SD | +0.0814 | 0.2304 | ±0.4609 | +0.353 | 0.7239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.56e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7809** | 2.7914 | ±5.5828 | **+18.192** | **5.97e-74** | *** |
| Education: graduate level (vs college) | +0.1934 | 0.6364 | ±1.2728 | +0.304 | 0.7612 |  |
| Education: high school or below (vs college) | +0.3921 | 0.7326 | ±1.4653 | +0.535 | 0.5926 |  |
| **Site: UCSD (vs UAB)** | **+3.4135** | 0.6595 | ±1.3190 | **+5.176** | **2.27e-07** | *** |
| Site: UW (vs UAB) | -0.4171 | 0.6449 | ±1.2897 | -0.647 | 0.5178 |  |
| **Season: spring (vs autumn)** | **-2.3161** | 0.7575 | ±1.5151 | **-3.057** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5480** | 0.7416 | ±1.4833 | **+2.087** | **0.0369** | * |
| **Season: winter (vs autumn)** | **-5.7670** | 0.8516 | ±1.7031 | **-6.772** | **1.27e-11** | *** |
| Age (years) | -0.0517 | 0.0275 | ±0.0550 | -1.882 | 0.0599 | . |
| BMI (kg/m2) | -0.0601 | 0.0406 | ±0.0813 | -1.478 | 0.1394 |  |
| Hypertension | -1.0011 | 0.6188 | ±1.2376 | -1.618 | 0.1057 |  |
| High cholesterol | -0.2595 | 0.5838 | ±1.1675 | -0.445 | 0.6567 |  |
| **Kidney disease** | **+1.5076** | 0.6634 | ±1.3267 | **+2.273** | **0.0230** | * |
| Circulatory disease | -0.2662 | 0.6642 | ±1.3284 | -0.401 | 0.6886 |  |
| MAG (mg/dL/h) | +0.0065 | 0.0263 | ±0.0526 | +0.249 | 0.8036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.2501**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.51e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6806** | 2.7430 | ±5.4859 | **+18.477** | **3.18e-76** | *** |
| Education: graduate level (vs college) | +0.1935 | 0.6350 | ±1.2699 | +0.305 | 0.7605 |  |
| Education: high school or below (vs college) | +0.3729 | 0.7300 | ±1.4601 | +0.511 | 0.6095 |  |
| **Site: UCSD (vs UAB)** | **+3.4224** | 0.6635 | ±1.3270 | **+5.158** | **2.49e-07** | *** |
| Site: UW (vs UAB) | -0.4162 | 0.6424 | ±1.2849 | -0.648 | 0.5171 |  |
| **Season: spring (vs autumn)** | **-2.3279** | 0.7539 | ±1.5078 | **-3.088** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5422** | 0.7394 | ±1.4788 | **+2.086** | **0.0370** | * |
| **Season: winter (vs autumn)** | **-5.7797** | 0.8487 | ±1.6975 | **-6.810** | **9.77e-12** | *** |
| Age (years) | -0.0519 | 0.0275 | ±0.0551 | -1.886 | 0.0592 | . |
| BMI (kg/m2) | -0.0599 | 0.0407 | ±0.0814 | -1.471 | 0.1413 |  |
| Hypertension | -0.9982 | 0.6196 | ±1.2392 | -1.611 | 0.1072 |  |
| High cholesterol | -0.2608 | 0.5843 | ±1.1686 | -0.446 | 0.6553 |  |
| **Kidney disease** | **+1.4779** | 0.6646 | ±1.3292 | **+2.224** | **0.0262** | * |
| Circulatory disease | -0.2731 | 0.6654 | ±1.3309 | -0.410 | 0.6815 |  |
| Avg. daily range (mg/dL) | +0.0026 | 0.0072 | ±0.0143 | +0.369 | 0.7119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.56e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0341** | 2.4812 | ±4.9624 | **+20.568** | **5.27e-94** | *** |
| Education: graduate level (vs college) | +0.1959 | 0.6333 | ±1.2667 | +0.309 | 0.7571 |  |
| Education: high school or below (vs college) | +0.3984 | 0.7321 | ±1.4643 | +0.544 | 0.5864 |  |
| **Site: UCSD (vs UAB)** | **+3.4136** | 0.6584 | ±1.3168 | **+5.185** | **2.16e-07** | *** |
| Site: UW (vs UAB) | -0.4251 | 0.6376 | ±1.2751 | -0.667 | 0.5049 |  |
| **Season: spring (vs autumn)** | **-2.3133** | 0.7581 | ±1.5162 | **-3.052** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5374** | 0.7380 | ±1.4759 | **+2.083** | **0.0372** | * |
| **Season: winter (vs autumn)** | **-5.7789** | 0.8543 | ±1.7086 | **-6.764** | **1.34e-11** | *** |
| Age (years) | -0.0520 | 0.0276 | ±0.0552 | -1.882 | 0.0598 | . |
| BMI (kg/m2) | -0.0611 | 0.0404 | ±0.0809 | -1.511 | 0.1308 |  |
| Hypertension | -1.0089 | 0.6205 | ±1.2411 | -1.626 | 0.1040 |  |
| High cholesterol | -0.2577 | 0.5847 | ±1.1695 | -0.441 | 0.6595 |  |
| **Kidney disease** | **+1.5133** | 0.6630 | ±1.3260 | **+2.283** | **0.0225** | * |
| Circulatory disease | -0.2788 | 0.6717 | ±1.3434 | -0.415 | 0.6781 |  |
| SD of daily means (mg/dL) | +0.0072 | 0.0307 | ±0.0613 | +0.234 | 0.8149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.43e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4894** | 2.5734 | ±5.1467 | **+20.009** | **4.63e-89** | *** |
| Education: graduate level (vs college) | +0.1950 | 0.6310 | ±1.2620 | +0.309 | 0.7573 |  |
| Education: high school or below (vs college) | +0.3664 | 0.7326 | ±1.4652 | +0.500 | 0.6170 |  |
| **Site: UCSD (vs UAB)** | **+3.4389** | 0.6637 | ±1.3274 | **+5.181** | **2.20e-07** | *** |
| Site: UW (vs UAB) | -0.4160 | 0.6376 | ±1.2753 | -0.652 | 0.5142 |  |
| **Season: spring (vs autumn)** | **-2.3263** | 0.7561 | ±1.5122 | **-3.077** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5482** | 0.7387 | ±1.4774 | **+2.096** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7892** | 0.8537 | ±1.7074 | **-6.781** | **1.19e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0549 | -1.893 | 0.0584 | . |
| BMI (kg/m2) | -0.0621 | 0.0410 | ±0.0821 | -1.513 | 0.1303 |  |
| Hypertension | -0.9960 | 0.6190 | ±1.2381 | -1.609 | 0.1076 |  |
| High cholesterol | -0.2478 | 0.5847 | ±1.1695 | -0.424 | 0.6718 |  |
| **Kidney disease** | **+1.5071** | 0.6632 | ±1.3264 | **+2.273** | **0.0231** | * |
| Circulatory disease | -0.2800 | 0.6650 | ±1.3300 | -0.421 | 0.6737 |  |
| Time in range 70-180, pooled (%) | -0.0051 | 0.0111 | ±0.0222 | -0.464 | 0.6423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.41e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.5156** | 2.5766 | ±5.1531 | **+19.994** | **6.22e-89** | *** |
| Education: graduate level (vs college) | +0.1943 | 0.6311 | ±1.2622 | +0.308 | 0.7582 |  |
| Education: high school or below (vs college) | +0.3623 | 0.7326 | ±1.4651 | +0.495 | 0.6209 |  |
| **Site: UCSD (vs UAB)** | **+3.4427** | 0.6645 | ±1.3291 | **+5.181** | **2.21e-07** | *** |
| Site: UW (vs UAB) | -0.4138 | 0.6378 | ±1.2755 | -0.649 | 0.5164 |  |
| **Season: spring (vs autumn)** | **-2.3282** | 0.7560 | ±1.5120 | **-3.080** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5469** | 0.7382 | ±1.4764 | **+2.095** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7930** | 0.8542 | ±1.7084 | **-6.782** | **1.19e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0549 | -1.893 | 0.0584 | . |
| BMI (kg/m2) | -0.0622 | 0.0410 | ±0.0821 | -1.517 | 0.1293 |  |
| Hypertension | -0.9952 | 0.6191 | ±1.2381 | -1.608 | 0.1079 |  |
| High cholesterol | -0.2473 | 0.5845 | ±1.1690 | -0.423 | 0.6722 |  |
| **Kidney disease** | **+1.5039** | 0.6632 | ±1.3264 | **+2.268** | **0.0233** | * |
| Circulatory disease | -0.2811 | 0.6652 | ±1.3303 | -0.423 | 0.6726 |  |
| Avg. daily time in range 70-180 (%) | -0.0054 | 0.0110 | ±0.0220 | -0.494 | 0.6210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2505**, Adj R² = **0.2306**, F-statistic = **12.58** (p = **1.34e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9955** | 2.4476 | ±4.8951 | **+20.835** | **2.08e-96** | *** |
| Education: graduate level (vs college) | +0.1835 | 0.6309 | ±1.2617 | +0.291 | 0.7712 |  |
| Education: high school or below (vs college) | +0.4096 | 0.7336 | ±1.4672 | +0.558 | 0.5766 |  |
| **Site: UCSD (vs UAB)** | **+3.4327** | 0.6580 | ±1.3159 | **+5.217** | **1.82e-07** | *** |
| Site: UW (vs UAB) | -0.4172 | 0.6338 | ±1.2677 | -0.658 | 0.5104 |  |
| **Season: spring (vs autumn)** | **-2.3193** | 0.7586 | ±1.5172 | **-3.057** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5408** | 0.7383 | ±1.4766 | **+2.087** | **0.0369** | * |
| **Season: winter (vs autumn)** | **-5.7380** | 0.8525 | ±1.7050 | **-6.731** | **1.69e-11** | *** |
| Age (years) | -0.0515 | 0.0277 | ±0.0554 | -1.861 | 0.0628 | . |
| BMI (kg/m2) | -0.0603 | 0.0407 | ±0.0815 | -1.481 | 0.1386 |  |
| Hypertension | -1.0360 | 0.6225 | ±1.2450 | -1.664 | 0.0961 | . |
| High cholesterol | -0.2367 | 0.5866 | ±1.1731 | -0.404 | 0.6865 |  |
| **Kidney disease** | **+1.5152** | 0.6637 | ±1.3274 | **+2.283** | **0.0224** | * |
| Circulatory disease | -0.2885 | 0.6693 | ±1.3387 | -0.431 | 0.6665 |  |
| Any reading < 54 during wear (0/1) | +0.3943 | 0.6480 | ±1.2961 | +0.608 | 0.5429 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2501**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.51e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1947** | 2.4240 | ±4.8480 | **+21.120** | **5.20e-99** | *** |
| Education: graduate level (vs college) | +0.1747 | 0.6308 | ±1.2616 | +0.277 | 0.7818 |  |
| Education: high school or below (vs college) | +0.3895 | 0.7329 | ±1.4657 | +0.531 | 0.5951 |  |
| **Site: UCSD (vs UAB)** | **+3.3855** | 0.6577 | ±1.3154 | **+5.148** | **2.64e-07** | *** |
| Site: UW (vs UAB) | -0.4676 | 0.6343 | ±1.2685 | -0.737 | 0.4610 |  |
| **Season: spring (vs autumn)** | **-2.3244** | 0.7598 | ±1.5197 | **-3.059** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5183** | 0.7386 | ±1.4771 | **+2.056** | **0.0398** | * |
| **Season: winter (vs autumn)** | **-5.7869** | 0.8597 | ±1.7195 | **-6.731** | **1.68e-11** | *** |
| Age (years) | -0.0524 | 0.0275 | ±0.0550 | -1.904 | 0.0569 | . |
| BMI (kg/m2) | -0.0602 | 0.0408 | ±0.0816 | -1.474 | 0.1405 |  |
| Hypertension | -0.9758 | 0.6212 | ±1.2424 | -1.571 | 0.1162 |  |
| High cholesterol | -0.2819 | 0.5882 | ±1.1763 | -0.479 | 0.6317 |  |
| **Kidney disease** | **+1.5289** | 0.6650 | ±1.3301 | **+2.299** | **0.0215** | * |
| Circulatory disease | -0.2803 | 0.6643 | ±1.3285 | -0.422 | 0.6731 |  |
| Time < 54 (%) | -0.3803 | 1.2618 | ±2.5236 | -0.301 | 0.7631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.56e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1741** | 2.4132 | ±4.8263 | **+21.206** | **8.37e-100** | *** |
| Education: graduate level (vs college) | +0.1789 | 0.6308 | ±1.2616 | +0.284 | 0.7767 |  |
| Education: high school or below (vs college) | +0.3944 | 0.7329 | ±1.4659 | +0.538 | 0.5905 |  |
| **Site: UCSD (vs UAB)** | **+3.3956** | 0.6572 | ±1.3144 | **+5.167** | **2.38e-07** | *** |
| Site: UW (vs UAB) | -0.4548 | 0.6365 | ±1.2730 | -0.714 | 0.4749 |  |
| **Season: spring (vs autumn)** | **-2.3296** | 0.7624 | ±1.5248 | **-3.056** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5181** | 0.7415 | ±1.4831 | **+2.047** | **0.0406** | * |
| **Season: winter (vs autumn)** | **-5.7818** | 0.8586 | ±1.7171 | **-6.734** | **1.65e-11** | *** |
| Age (years) | -0.0525 | 0.0276 | ±0.0551 | -1.905 | 0.0568 | . |
| BMI (kg/m2) | -0.0601 | 0.0407 | ±0.0815 | -1.475 | 0.1402 |  |
| Hypertension | -0.9895 | 0.6196 | ±1.2391 | -1.597 | 0.1102 |  |
| High cholesterol | -0.2736 | 0.5860 | ±1.1720 | -0.467 | 0.6406 |  |
| **Kidney disease** | **+1.5296** | 0.6671 | ±1.3342 | **+2.293** | **0.0219** | * |
| Circulatory disease | -0.2705 | 0.6647 | ±1.3294 | -0.407 | 0.6840 |  |
| Avg. daily time < 54 (%) | -0.1804 | 1.5089 | ±3.0179 | -0.120 | 0.9049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.43e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2318** | 2.4072 | ±4.8144 | **+21.283** | **1.64e-100** | *** |
| Education: graduate level (vs college) | +0.1743 | 0.6309 | ±1.2617 | +0.276 | 0.7824 |  |
| Education: high school or below (vs college) | +0.3999 | 0.7322 | ±1.4643 | +0.546 | 0.5849 |  |
| **Site: UCSD (vs UAB)** | **+3.3720** | 0.6583 | ±1.3166 | **+5.122** | **3.02e-07** | *** |
| Site: UW (vs UAB) | -0.4732 | 0.6337 | ±1.2674 | -0.747 | 0.4553 |  |
| **Season: spring (vs autumn)** | **-2.3418** | 0.7648 | ±1.5296 | **-3.062** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5076** | 0.7381 | ±1.4762 | **+2.043** | **0.0411** | * |
| **Season: winter (vs autumn)** | **-5.7946** | 0.8616 | ±1.7231 | **-6.726** | **1.75e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0551 | -1.891 | 0.0586 | . |
| BMI (kg/m2) | -0.0609 | 0.0407 | ±0.0813 | -1.498 | 0.1341 |  |
| Hypertension | -0.9731 | 0.6169 | ±1.2338 | -1.577 | 0.1147 |  |
| High cholesterol | -0.2906 | 0.5876 | ±1.1752 | -0.495 | 0.6209 |  |
| **Kidney disease** | **+1.5402** | 0.6663 | ±1.3326 | **+2.312** | **0.0208** | * |
| Circulatory disease | -0.2801 | 0.6649 | ±1.3297 | -0.421 | 0.6736 |  |
| Time 54-69, pooled (%) | -0.1471 | 0.3801 | ±0.7602 | -0.387 | 0.6987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.58** (p = **1.37e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2194** | 2.4002 | ±4.8005 | **+21.339** | **4.90e-101** | *** |
| Education: graduate level (vs college) | +0.1698 | 0.6308 | ±1.2617 | +0.269 | 0.7878 |  |
| Education: high school or below (vs college) | +0.3968 | 0.7317 | ±1.4634 | +0.542 | 0.5876 |  |
| **Site: UCSD (vs UAB)** | **+3.3666** | 0.6577 | ±1.3155 | **+5.118** | **3.08e-07** | *** |
| Site: UW (vs UAB) | -0.4825 | 0.6337 | ±1.2674 | -0.761 | 0.4464 |  |
| **Season: spring (vs autumn)** | **-2.3465** | 0.7651 | ±1.5301 | **-3.067** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5039** | 0.7383 | ±1.4765 | **+2.037** | **0.0416** | * |
| **Season: winter (vs autumn)** | **-5.7975** | 0.8619 | ±1.7237 | **-6.727** | **1.74e-11** | *** |
| Age (years) | -0.0518 | 0.0275 | ±0.0551 | -1.881 | 0.0599 | . |
| BMI (kg/m2) | -0.0606 | 0.0406 | ±0.0812 | -1.493 | 0.1355 |  |
| Hypertension | -0.9679 | 0.6164 | ±1.2328 | -1.570 | 0.1164 |  |
| High cholesterol | -0.2966 | 0.5882 | ±1.1764 | -0.504 | 0.6141 |  |
| **Kidney disease** | **+1.5406** | 0.6654 | ±1.3308 | **+2.315** | **0.0206** | * |
| Circulatory disease | -0.2859 | 0.6642 | ±1.3284 | -0.430 | 0.6669 |  |
| Avg. daily time 54-69 (%) | -0.1637 | 0.3642 | ±0.7285 | -0.449 | 0.6532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.42e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2342** | 2.4124 | ±4.8248 | **+21.238** | **4.29e-100** | *** |
| Education: graduate level (vs college) | +0.1728 | 0.6307 | ±1.2614 | +0.274 | 0.7841 |  |
| Education: high school or below (vs college) | +0.3961 | 0.7320 | ±1.4640 | +0.541 | 0.5884 |  |
| **Site: UCSD (vs UAB)** | **+3.3700** | 0.6586 | ±1.3172 | **+5.117** | **3.10e-07** | *** |
| Site: UW (vs UAB) | -0.4774 | 0.6338 | ±1.2675 | -0.753 | 0.4513 |  |
| **Season: spring (vs autumn)** | **-2.3411** | 0.7643 | ±1.5287 | **-3.063** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5065** | 0.7386 | ±1.4771 | **+2.040** | **0.0414** | * |
| **Season: winter (vs autumn)** | **-5.7970** | 0.8624 | ±1.7248 | **-6.722** | **1.80e-11** | *** |
| Age (years) | -0.0521 | 0.0275 | ±0.0550 | -1.893 | 0.0584 | . |
| BMI (kg/m2) | -0.0608 | 0.0407 | ±0.0814 | -1.493 | 0.1354 |  |
| Hypertension | -0.9690 | 0.6177 | ±1.2354 | -1.569 | 0.1167 |  |
| High cholesterol | -0.2929 | 0.5881 | ±1.1761 | -0.498 | 0.6184 |  |
| **Kidney disease** | **+1.5394** | 0.6663 | ±1.3325 | **+2.311** | **0.0209** | * |
| Circulatory disease | -0.2832 | 0.6647 | ±1.3294 | -0.426 | 0.6700 |  |
| Time < 70 (%) | -0.1260 | 0.3108 | ±0.6215 | -0.406 | 0.6851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.40e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2146** | 2.4044 | ±4.8088 | **+21.300** | **1.13e-100** | *** |
| Education: graduate level (vs college) | +0.1708 | 0.6308 | ±1.2616 | +0.271 | 0.7866 |  |
| Education: high school or below (vs college) | +0.3934 | 0.7319 | ±1.4639 | +0.538 | 0.5909 |  |
| **Site: UCSD (vs UAB)** | **+3.3705** | 0.6576 | ±1.3153 | **+5.125** | **2.97e-07** | *** |
| Site: UW (vs UAB) | -0.4801 | 0.6340 | ±1.2680 | -0.757 | 0.4489 |  |
| **Season: spring (vs autumn)** | **-2.3475** | 0.7651 | ±1.5303 | **-3.068** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5024** | 0.7397 | ±1.4795 | **+2.031** | **0.0423** | * |
| **Season: winter (vs autumn)** | **-5.7983** | 0.8618 | ±1.7235 | **-6.728** | **1.72e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0551 | -1.888 | 0.0591 | . |
| BMI (kg/m2) | -0.0604 | 0.0406 | ±0.0813 | -1.486 | 0.1372 |  |
| Hypertension | -0.9699 | 0.6170 | ±1.2341 | -1.572 | 0.1160 |  |
| High cholesterol | -0.2942 | 0.5874 | ±1.1748 | -0.501 | 0.6164 |  |
| **Kidney disease** | **+1.5396** | 0.6654 | ±1.3307 | **+2.314** | **0.0207** | * |
| Circulatory disease | -0.2842 | 0.6642 | ±1.3285 | -0.428 | 0.6688 |  |
| Avg. daily time < 70 (%) | -0.1184 | 0.2831 | ±0.5661 | -0.418 | 0.6757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6547** | 2.8198 | ±5.6395 | **+18.319** | **5.85e-75** | *** |
| Education: graduate level (vs college) | +0.2036 | 0.6307 | ±1.2615 | +0.323 | 0.7468 |  |
| Education: high school or below (vs college) | +0.3757 | 0.7349 | ±1.4699 | +0.511 | 0.6093 |  |
| **Site: UCSD (vs UAB)** | **+3.4287** | 0.6624 | ±1.3248 | **+5.176** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.4114 | 0.6407 | ±1.2814 | -0.642 | 0.5208 |  |
| **Season: spring (vs autumn)** | **-2.3140** | 0.7583 | ±1.5165 | **-3.052** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5609** | 0.7395 | ±1.4790 | **+2.111** | **0.0348** | * |
| **Season: winter (vs autumn)** | **-5.7724** | 0.8515 | ±1.7029 | **-6.779** | **1.21e-11** | *** |
| Age (years) | -0.0515 | 0.0275 | ±0.0549 | -1.874 | 0.0609 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0106 | 0.6198 | ±1.2395 | -1.631 | 0.1030 |  |
| High cholesterol | -0.2546 | 0.5849 | ±1.1699 | -0.435 | 0.6633 |  |
| **Kidney disease** | **+1.5101** | 0.6639 | ±1.3278 | **+2.275** | **0.0229** | * |
| Circulatory disease | -0.2742 | 0.6646 | ±1.3292 | -0.413 | 0.6799 |  |
| Time 54-250, pooled (%) | -0.0063 | 0.0153 | ±0.0305 | -0.410 | 0.6821 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.48e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6650** | 2.8599 | ±5.7198 | **+18.065** | **5.99e-73** | *** |
| Education: graduate level (vs college) | +0.2032 | 0.6309 | ±1.2618 | +0.322 | 0.7474 |  |
| Education: high school or below (vs college) | +0.3760 | 0.7353 | ±1.4705 | +0.511 | 0.6091 |  |
| **Site: UCSD (vs UAB)** | **+3.4290** | 0.6625 | ±1.3249 | **+5.176** | **2.27e-07** | *** |
| Site: UW (vs UAB) | -0.4127 | 0.6406 | ±1.2812 | -0.644 | 0.5194 |  |
| **Season: spring (vs autumn)** | **-2.3152** | 0.7582 | ±1.5164 | **-3.053** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5587** | 0.7387 | ±1.4775 | **+2.110** | **0.0349** | * |
| **Season: winter (vs autumn)** | **-5.7737** | 0.8518 | ±1.7036 | **-6.778** | **1.22e-11** | *** |
| Age (years) | -0.0516 | 0.0275 | ±0.0549 | -1.880 | 0.0601 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0097 | 0.6196 | ±1.2392 | -1.630 | 0.1032 |  |
| High cholesterol | -0.2547 | 0.5847 | ±1.1695 | -0.436 | 0.6631 |  |
| **Kidney disease** | **+1.5084** | 0.6644 | ±1.3287 | **+2.270** | **0.0232** | * |
| Circulatory disease | -0.2751 | 0.6644 | ±1.3289 | -0.414 | 0.6789 |  |
| Avg. daily time 54-250 (%) | -0.0062 | 0.0156 | ±0.0313 | -0.399 | 0.6899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2501**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.50e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0577** | 2.4084 | ±4.8169 | **+21.199** | **9.66e-100** | *** |
| Education: graduate level (vs college) | +0.1760 | 0.6318 | ±1.2637 | +0.279 | 0.7805 |  |
| Education: high school or below (vs college) | +0.3835 | 0.7305 | ±1.4609 | +0.525 | 0.5995 |  |
| **Site: UCSD (vs UAB)** | **+3.4233** | 0.6583 | ±1.3166 | **+5.200** | **1.99e-07** | *** |
| Site: UW (vs UAB) | -0.4415 | 0.6356 | ±1.2712 | -0.695 | 0.4873 |  |
| **Season: spring (vs autumn)** | **-2.3317** | 0.7537 | ±1.5075 | **-3.094** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5215** | 0.7346 | ±1.4692 | **+2.071** | **0.0383** | * |
| **Season: winter (vs autumn)** | **-5.7922** | 0.8549 | ±1.7098 | **-6.775** | **1.24e-11** | *** |
| Age (years) | -0.0529 | 0.0276 | ±0.0552 | -1.918 | 0.0552 | . |
| BMI (kg/m2) | -0.0617 | 0.0408 | ±0.0816 | -1.512 | 0.1307 |  |
| Hypertension | -0.9822 | 0.6184 | ±1.2369 | -1.588 | 0.1122 |  |
| High cholesterol | -0.2535 | 0.5841 | ±1.1681 | -0.434 | 0.6643 |  |
| **Kidney disease** | **+1.5179** | 0.6629 | ±1.3259 | **+2.290** | **0.0220** | * |
| Circulatory disease | -0.2745 | 0.6663 | ±1.3326 | -0.412 | 0.6803 |  |
| Time 181-250, pooled (%) | +0.0067 | 0.0190 | ±0.0380 | +0.352 | 0.7248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.2**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0375** | 2.4120 | ±4.8240 | **+21.160** | **2.24e-99** | *** |
| Education: graduate level (vs college) | +0.1732 | 0.6318 | ±1.2635 | +0.274 | 0.7839 |  |
| Education: high school or below (vs college) | +0.3770 | 0.7300 | ±1.4599 | +0.516 | 0.6055 |  |
| **Site: UCSD (vs UAB)** | **+3.4285** | 0.6592 | ±1.3184 | **+5.201** | **1.98e-07** | *** |
| Site: UW (vs UAB) | -0.4393 | 0.6355 | ±1.2711 | -0.691 | 0.4894 |  |
| **Season: spring (vs autumn)** | **-2.3350** | 0.7538 | ±1.5076 | **-3.098** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5191** | 0.7344 | ±1.4688 | **+2.069** | **0.0386** | * |
| **Season: winter (vs autumn)** | **-5.7984** | 0.8552 | ±1.7105 | **-6.780** | **1.20e-11** | *** |
| Age (years) | -0.0529 | 0.0276 | ±0.0551 | -1.918 | 0.0551 | . |
| BMI (kg/m2) | -0.0620 | 0.0408 | ±0.0816 | -1.519 | 0.1287 |  |
| Hypertension | -0.9794 | 0.6183 | ±1.2367 | -1.584 | 0.1132 |  |
| High cholesterol | -0.2525 | 0.5840 | ±1.1679 | -0.432 | 0.6655 |  |
| **Kidney disease** | **+1.5157** | 0.6628 | ±1.3255 | **+2.287** | **0.0222** | * |
| Circulatory disease | -0.2756 | 0.6665 | ±1.3330 | -0.413 | 0.6793 |  |
| Avg. daily time 181-250 (%) | +0.0078 | 0.0185 | ±0.0370 | +0.421 | 0.6736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.42e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9731** | 2.3953 | ±4.7905 | **+21.281** | **1.71e-100** | *** |
| Education: graduate level (vs college) | +0.1949 | 0.6311 | ±1.2622 | +0.309 | 0.7574 |  |
| Education: high school or below (vs college) | +0.3652 | 0.7324 | ±1.4648 | +0.499 | 0.6181 |  |
| **Site: UCSD (vs UAB)** | **+3.4383** | 0.6632 | ±1.3264 | **+5.184** | **2.17e-07** | *** |
| Site: UW (vs UAB) | -0.4168 | 0.6375 | ±1.2750 | -0.654 | 0.5133 |  |
| **Season: spring (vs autumn)** | **-2.3277** | 0.7560 | ±1.5120 | **-3.079** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5476** | 0.7383 | ±1.4767 | **+2.096** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7910** | 0.8541 | ±1.7081 | **-6.780** | **1.20e-11** | *** |
| Age (years) | -0.0519 | 0.0274 | ±0.0549 | -1.892 | 0.0586 | . |
| BMI (kg/m2) | -0.0621 | 0.0410 | ±0.0821 | -1.515 | 0.1299 |  |
| Hypertension | -0.9946 | 0.6190 | ±1.2379 | -1.607 | 0.1081 |  |
| High cholesterol | -0.2486 | 0.5846 | ±1.1693 | -0.425 | 0.6707 |  |
| **Kidney disease** | **+1.5073** | 0.6631 | ±1.3263 | **+2.273** | **0.0230** | * |
| Circulatory disease | -0.2813 | 0.6650 | ±1.3299 | -0.423 | 0.6723 |  |
| Time > 180 (%) | +0.0053 | 0.0110 | ±0.0220 | +0.480 | 0.6310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.57** (p = **1.39e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9693** | 2.3940 | ±4.7880 | **+21.290** | **1.40e-100** | *** |
| Education: graduate level (vs college) | +0.1941 | 0.6311 | ±1.2622 | +0.308 | 0.7584 |  |
| Education: high school or below (vs college) | +0.3606 | 0.7325 | ±1.4650 | +0.492 | 0.6225 |  |
| **Site: UCSD (vs UAB)** | **+3.4422** | 0.6640 | ±1.3279 | **+5.184** | **2.17e-07** | *** |
| Site: UW (vs UAB) | -0.4148 | 0.6376 | ±1.2751 | -0.651 | 0.5153 |  |
| **Season: spring (vs autumn)** | **-2.3303** | 0.7559 | ±1.5119 | **-3.083** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5459** | 0.7378 | ±1.4756 | **+2.095** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7952** | 0.8547 | ±1.7094 | **-6.781** | **1.20e-11** | *** |
| Age (years) | -0.0519 | 0.0274 | ±0.0549 | -1.892 | 0.0585 | . |
| BMI (kg/m2) | -0.0623 | 0.0410 | ±0.0821 | -1.519 | 0.1288 |  |
| Hypertension | -0.9936 | 0.6190 | ±1.2379 | -1.605 | 0.1084 |  |
| High cholesterol | -0.2483 | 0.5844 | ±1.1688 | -0.425 | 0.6710 |  |
| **Kidney disease** | **+1.5040** | 0.6632 | ±1.3264 | **+2.268** | **0.0233** | * |
| Circulatory disease | -0.2826 | 0.6651 | ±1.3303 | -0.425 | 0.6709 |  |
| Avg. daily time > 180 (%) | +0.0056 | 0.0109 | ±0.0219 | +0.513 | 0.6077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.57e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2101** | 2.4036 | ±4.8071 | **+21.306** | **1.00e-100** | *** |
| Education: graduate level (vs college) | +0.1736 | 0.6323 | ±1.2645 | +0.275 | 0.7837 |  |
| Education: high school or below (vs college) | +0.4142 | 0.7351 | ±1.4702 | +0.563 | 0.5732 |  |
| **Site: UCSD (vs UAB)** | **+3.3916** | 0.6655 | ±1.3311 | **+5.096** | **3.47e-07** | *** |
| Site: UW (vs UAB) | -0.4475 | 0.6363 | ±1.2725 | -0.703 | 0.4819 |  |
| **Season: spring (vs autumn)** | **-2.3088** | 0.7558 | ±1.5116 | **-3.055** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5256** | 0.7380 | ±1.4761 | **+2.067** | **0.0387** | * |
| **Season: winter (vs autumn)** | **-5.7591** | 0.8543 | ±1.7086 | **-6.741** | **1.57e-11** | *** |
| Age (years) | -0.0531 | 0.0275 | ±0.0550 | -1.929 | 0.0538 | . |
| BMI (kg/m2) | -0.0590 | 0.0413 | ±0.0826 | -1.430 | 0.1528 |  |
| Hypertension | -1.0024 | 0.6191 | ±1.2382 | -1.619 | 0.1054 |  |
| High cholesterol | -0.2705 | 0.5843 | ±1.1687 | -0.463 | 0.6435 |  |
| **Kidney disease** | **+1.5298** | 0.6646 | ±1.3292 | **+2.302** | **0.0213** | * |
| Circulatory disease | -0.2561 | 0.6642 | ±1.3285 | -0.386 | 0.6998 |  |
| Nocturnal time > 180 (%) | -0.0019 | 0.0095 | ±0.0189 | -0.206 | 0.8369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0286** | 2.3887 | ±4.7774 | **+21.363** | **2.98e-101** | *** |
| Education: graduate level (vs college) | +0.2037 | 0.6307 | ±1.2615 | +0.323 | 0.7467 |  |
| Education: high school or below (vs college) | +0.3752 | 0.7350 | ±1.4699 | +0.510 | 0.6097 |  |
| **Site: UCSD (vs UAB)** | **+3.4286** | 0.6623 | ±1.3246 | **+5.177** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.4115 | 0.6406 | ±1.2812 | -0.642 | 0.5206 |  |
| **Season: spring (vs autumn)** | **-2.3141** | 0.7582 | ±1.5165 | **-3.052** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5610** | 0.7394 | ±1.4788 | **+2.111** | **0.0348** | * |
| **Season: winter (vs autumn)** | **-5.7728** | 0.8515 | ±1.7031 | **-6.779** | **1.21e-11** | *** |
| Age (years) | -0.0515 | 0.0275 | ±0.0549 | -1.874 | 0.0610 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0104 | 0.6197 | ±1.2395 | -1.630 | 0.1030 |  |
| High cholesterol | -0.2548 | 0.5849 | ±1.1698 | -0.436 | 0.6631 |  |
| **Kidney disease** | **+1.5100** | 0.6639 | ±1.3278 | **+2.275** | **0.0229** | * |
| Circulatory disease | -0.2746 | 0.6645 | ±1.3291 | -0.413 | 0.6795 |  |
| Time > 250 (%) | +0.0063 | 0.0153 | ±0.0305 | +0.414 | 0.6788 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0407** | 2.3856 | ±4.7712 | **+21.395** | **1.48e-101** | *** |
| Education: graduate level (vs college) | +0.2033 | 0.6309 | ±1.2618 | +0.322 | 0.7473 |  |
| Education: high school or below (vs college) | +0.3755 | 0.7353 | ±1.4707 | +0.511 | 0.6096 |  |
| **Site: UCSD (vs UAB)** | **+3.4288** | 0.6624 | ±1.3247 | **+5.177** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.4128 | 0.6404 | ±1.2809 | -0.645 | 0.5192 |  |
| **Season: spring (vs autumn)** | **-2.3157** | 0.7582 | ±1.5163 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5584** | 0.7386 | ±1.4771 | **+2.110** | **0.0348** | * |
| **Season: winter (vs autumn)** | **-5.7742** | 0.8519 | ±1.7038 | **-6.778** | **1.22e-11** | *** |
| Age (years) | -0.0516 | 0.0274 | ±0.0549 | -1.880 | 0.0601 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0095 | 0.6196 | ±1.2392 | -1.629 | 0.1033 |  |
| High cholesterol | -0.2550 | 0.5847 | ±1.1694 | -0.436 | 0.6627 |  |
| **Kidney disease** | **+1.5084** | 0.6643 | ±1.3286 | **+2.271** | **0.0232** | * |
| Circulatory disease | -0.2755 | 0.6644 | ±1.3288 | -0.415 | 0.6785 |  |
| Avg. daily time > 250 (%) | +0.0063 | 0.0156 | ±0.0313 | +0.403 | 0.6870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0453**, F-statistic = **2.97** (p = **3.23e-04**), Residual SE = **17.841** on **528** df, AIC = **4675.5**, BIC = **4735.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2272** | 9.3794 | ±18.7588 | **+13.565** | **6.50e-42** | *** |
| Education: graduate level (vs college) | -0.6600 | 1.5982 | ±3.1965 | -0.413 | 0.6796 |  |
| **Education: high school or below (vs college)** | **+5.9711** | 2.5465 | ±5.0929 | **+2.345** | **0.0190** | * |
| Site: UCSD (vs UAB) | +3.6077 | 2.0811 | ±4.1621 | +1.734 | 0.0830 | . |
| Site: UW (vs UAB) | -1.6926 | 1.7492 | ±3.4984 | -0.968 | 0.3332 |  |
| Season: spring (vs autumn) | +3.3906 | 1.8794 | ±3.7589 | +1.804 | 0.0712 | . |
| **Season: summer (vs autumn)** | **+5.0010** | 1.9597 | ±3.9195 | **+2.552** | **0.0107** | * |
| **Season: winter (vs autumn)** | **+6.5554** | 2.5277 | ±5.0555 | **+2.593** | **0.0095** | ** |
| Age (years) | -0.1647 | 0.0958 | ±0.1917 | -1.719 | 0.0857 | . |
| BMI (kg/m2) | +0.1399 | 0.1435 | ±0.2869 | +0.975 | 0.3295 |  |
| Hypertension | +0.6836 | 1.9658 | ±3.9316 | +0.348 | 0.7280 |  |
| High cholesterol | +2.2853 | 1.8143 | ±3.6286 | +1.260 | 0.2078 |  |
| Kidney disease | -1.9852 | 1.9576 | ±3.9152 | -1.014 | 0.3105 |  |
| Circulatory disease | +0.8686 | 2.0390 | ±4.0779 | +0.426 | 0.6701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.0779**, Adj R² = **0.0534**, F-statistic = **3.18** (p = **7.88e-05**), Residual SE = **17.765** on **527** df, AIC = **4671.8**, BIC = **4736.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.0407** | 10.0581 | ±20.1162 | **+13.625** | **2.85e-42** | *** |
| Education: graduate level (vs college) | -0.9152 | 1.5909 | ±3.1817 | -0.575 | 0.5651 |  |
| **Education: high school or below (vs college)** | **+6.5225** | 2.5323 | ±5.0646 | **+2.576** | **0.0100** | * |
| Site: UCSD (vs UAB) | +3.2945 | 2.0812 | ±4.1625 | +1.583 | 0.1134 |  |
| Site: UW (vs UAB) | -2.0599 | 1.7453 | ±3.4906 | -1.180 | 0.2379 |  |
| Season: spring (vs autumn) | +3.1296 | 1.8815 | ±3.7629 | +1.663 | 0.0962 | . |
| **Season: summer (vs autumn)** | **+4.6512** | 1.9713 | ±3.9425 | **+2.359** | **0.0183** | * |
| **Season: winter (vs autumn)** | **+6.5820** | 2.5149 | ±5.0299 | **+2.617** | **0.0089** | ** |
| Age (years) | -0.1767 | 0.0960 | ±0.1920 | -1.841 | 0.0657 | . |
| BMI (kg/m2) | +0.1692 | 0.1438 | ±0.2876 | +1.176 | 0.2395 |  |
| Hypertension | +0.7583 | 1.9509 | ±3.9018 | +0.389 | 0.6975 |  |
| High cholesterol | +2.2462 | 1.7998 | ±3.5996 | +1.248 | 0.2120 |  |
| Kidney disease | -2.0661 | 1.9475 | ±3.8950 | -1.061 | 0.2887 |  |
| Circulatory disease | +1.0221 | 2.0298 | ±4.0595 | +0.504 | 0.6146 |  |
| **HbA1c (%)** | **-1.3552** | 0.6140 | ±1.2280 | **-2.207** | **0.0273** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.0756**, Adj R² = **0.0511**, F-statistic = **3.08** (p = **1.27e-04**), Residual SE = **17.787** on **527** df, AIC = **4673.2**, BIC = **4737.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.3027** | 10.4583 | ±20.9166 | **+12.842** | **9.57e-38** | *** |
| Education: graduate level (vs college) | -0.8523 | 1.5846 | ±3.1692 | -0.538 | 0.5907 |  |
| **Education: high school or below (vs college)** | **+6.3752** | 2.5430 | ±5.0861 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2781 | 2.1095 | ±4.2189 | +1.554 | 0.1202 |  |
| Site: UW (vs UAB) | -1.9832 | 1.7530 | ±3.5060 | -1.131 | 0.2579 |  |
| Season: spring (vs autumn) | +3.5181 | 1.8830 | ±3.7661 | +1.868 | 0.0617 | . |
| **Season: summer (vs autumn)** | **+4.7498** | 1.9772 | ±3.9544 | **+2.402** | **0.0163** | * |
| **Season: winter (vs autumn)** | **+6.7882** | 2.4854 | ±4.9708 | **+2.731** | **0.0063** | ** |
| Age (years) | -0.1759 | 0.0973 | ±0.1947 | -1.807 | 0.0708 | . |
| BMI (kg/m2) | +0.1575 | 0.1421 | ±0.2841 | +1.108 | 0.2677 |  |
| Hypertension | +0.6798 | 1.9560 | ±3.9120 | +0.348 | 0.7282 |  |
| High cholesterol | +2.1847 | 1.8030 | ±3.6061 | +1.212 | 0.2256 |  |
| Kidney disease | -1.8544 | 1.9612 | ±3.9224 | -0.946 | 0.3444 |  |
| Circulatory disease | +1.0713 | 2.0324 | ±4.0647 | +0.527 | 0.5981 |  |
| Mean glucose (mg/dL) | -0.0396 | 0.0203 | ±0.0405 | -1.953 | 0.0509 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.0756**, Adj R² = **0.0511**, F-statistic = **3.08** (p = **1.27e-04**), Residual SE = **17.787** on **527** df, AIC = **4673.2**, BIC = **4737.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+139.7798** | 11.9943 | ±23.9885 | **+11.654** | **2.19e-31** | *** |
| Education: graduate level (vs college) | -0.8523 | 1.5846 | ±3.1692 | -0.538 | 0.5907 |  |
| **Education: high school or below (vs college)** | **+6.3752** | 2.5430 | ±5.0861 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2781 | 2.1095 | ±4.2189 | +1.554 | 0.1202 |  |
| Site: UW (vs UAB) | -1.9832 | 1.7530 | ±3.5060 | -1.131 | 0.2579 |  |
| Season: spring (vs autumn) | +3.5181 | 1.8830 | ±3.7661 | +1.868 | 0.0617 | . |
| **Season: summer (vs autumn)** | **+4.7498** | 1.9772 | ±3.9544 | **+2.402** | **0.0163** | * |
| **Season: winter (vs autumn)** | **+6.7882** | 2.4854 | ±4.9708 | **+2.731** | **0.0063** | ** |
| Age (years) | -0.1759 | 0.0973 | ±0.1947 | -1.807 | 0.0708 | . |
| BMI (kg/m2) | +0.1575 | 0.1421 | ±0.2841 | +1.108 | 0.2677 |  |
| Hypertension | +0.6798 | 1.9560 | ±3.9120 | +0.348 | 0.7282 |  |
| High cholesterol | +2.1847 | 1.8030 | ±3.6061 | +1.212 | 0.2256 |  |
| Kidney disease | -1.8544 | 1.9612 | ±3.9224 | -0.946 | 0.3444 |  |
| Circulatory disease | +1.0713 | 2.0324 | ±4.0647 | +0.527 | 0.5981 |  |
| GMI (%) | -1.6547 | 0.8474 | ±1.6948 | -1.953 | 0.0509 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.0740**, Adj R² = **0.0494**, F-statistic = **3.01** (p = **1.80e-04**), Residual SE = **17.802** on **527** df, AIC = **4674.1**, BIC = **4738.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.8842** | 10.6615 | ±21.3231 | **+12.464** | **1.18e-35** | *** |
| Education: graduate level (vs college) | -0.8820 | 1.5855 | ±3.1710 | -0.556 | 0.5780 |  |
| **Education: high school or below (vs college)** | **+6.2747** | 2.5219 | ±5.0438 | **+2.488** | **0.0128** | * |
| Site: UCSD (vs UAB) | +3.2924 | 2.1157 | ±4.2315 | +1.556 | 0.1197 |  |
| Site: UW (vs UAB) | -1.8264 | 1.7487 | ±3.4975 | -1.044 | 0.2963 |  |
| Season: spring (vs autumn) | +3.5655 | 1.8786 | ±3.7571 | +1.898 | 0.0577 | . |
| **Season: summer (vs autumn)** | **+4.8136** | 1.9770 | ±3.9539 | **+2.435** | **0.0149** | * |
| **Season: winter (vs autumn)** | **+6.7757** | 2.4844 | ±4.9687 | **+2.727** | **0.0064** | ** |
| Age (years) | -0.1798 | 0.0988 | ±0.1975 | -1.820 | 0.0687 | . |
| BMI (kg/m2) | +0.1648 | 0.1416 | ±0.2832 | +1.163 | 0.2446 |  |
| Hypertension | +0.6491 | 1.9604 | ±3.9209 | +0.331 | 0.7406 |  |
| High cholesterol | +2.1926 | 1.8012 | ±3.6023 | +1.217 | 0.2235 |  |
| Kidney disease | -1.9617 | 1.9616 | ±3.9232 | -1.000 | 0.3173 |  |
| Circulatory disease | +1.0490 | 2.0255 | ±4.0510 | +0.518 | 0.6045 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0328 | 0.0214 | ±0.0429 | -1.529 | 0.1263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.0711**, Adj R² = **0.0465**, F-statistic = **2.88** (p = **3.25e-04**), Residual SE = **17.830** on **527** df, AIC = **4675.8**, BIC = **4740.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.7447** | 9.5610 | ±19.1219 | **+13.675** | **1.44e-42** | *** |
| Education: graduate level (vs college) | -0.8033 | 1.6015 | ±3.2030 | -0.502 | 0.6159 |  |
| **Education: high school or below (vs college)** | **+6.2250** | 2.5474 | ±5.0947 | **+2.444** | **0.0145** | * |
| Site: UCSD (vs UAB) | +3.4501 | 2.1052 | ±4.2105 | +1.639 | 0.1013 |  |
| Site: UW (vs UAB) | -1.9942 | 1.7685 | ±3.5370 | -1.128 | 0.2595 |  |
| Season: spring (vs autumn) | +3.4793 | 1.8921 | ±3.7842 | +1.839 | 0.0659 | . |
| **Season: summer (vs autumn)** | **+4.8154** | 1.9733 | ±3.9466 | **+2.440** | **0.0147** | * |
| **Season: winter (vs autumn)** | **+6.6887** | 2.5233 | ±5.0465 | **+2.651** | **0.0080** | ** |
| Age (years) | -0.1681 | 0.0958 | ±0.1917 | -1.754 | 0.0794 | . |
| BMI (kg/m2) | +0.1466 | 0.1442 | ±0.2883 | +1.017 | 0.3093 |  |
| Hypertension | +0.7474 | 1.9549 | ±3.9097 | +0.382 | 0.7022 |  |
| High cholesterol | +2.1890 | 1.7971 | ±3.5942 | +1.218 | 0.2232 |  |
| Kidney disease | -1.5516 | 1.9639 | ±3.9277 | -0.790 | 0.4295 |  |
| Circulatory disease | +0.9733 | 2.0305 | ±4.0610 | +0.479 | 0.6317 |  |
| Glucose SD, pooled (mg/dL) | -0.0834 | 0.0747 | ±0.1494 | -1.116 | 0.2643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.0689**, Adj R² = **0.0442**, F-statistic = **2.79** (p = **5.08e-04**), Residual SE = **17.851** on **527** df, AIC = **4677.1**, BIC = **4741.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.0657** | 9.7908 | ±19.5817 | **+13.182** | **1.11e-39** | *** |
| Education: graduate level (vs college) | -0.7172 | 1.6058 | ±3.2116 | -0.447 | 0.6551 |  |
| **Education: high school or below (vs college)** | **+6.1218** | 2.5445 | ±5.0891 | **+2.406** | **0.0161** | * |
| Site: UCSD (vs UAB) | +3.5294 | 2.0973 | ±4.1945 | +1.683 | 0.0924 | . |
| Site: UW (vs UAB) | -1.8259 | 1.7678 | ±3.5355 | -1.033 | 0.3017 |  |
| Season: spring (vs autumn) | +3.4421 | 1.8884 | ±3.7768 | +1.823 | 0.0683 | . |
| **Season: summer (vs autumn)** | **+4.9005** | 1.9801 | ±3.9602 | **+2.475** | **0.0133** | * |
| **Season: winter (vs autumn)** | **+6.6005** | 2.5356 | ±5.0712 | **+2.603** | **0.0092** | ** |
| Age (years) | -0.1657 | 0.0960 | ±0.1920 | -1.726 | 0.0843 | . |
| BMI (kg/m2) | +0.1399 | 0.1435 | ±0.2871 | +0.975 | 0.3297 |  |
| Hypertension | +0.6996 | 1.9635 | ±3.9269 | +0.356 | 0.7216 |  |
| High cholesterol | +2.2446 | 1.8092 | ±3.6184 | +1.241 | 0.2147 |  |
| Kidney disease | -1.7522 | 1.9655 | ±3.9309 | -0.892 | 0.3727 |  |
| Circulatory disease | +0.9036 | 2.0416 | ±4.0832 | +0.443 | 0.6581 |  |
| Avg. daily SD (mg/dL) | -0.0473 | 0.0725 | ±0.1450 | -0.652 | 0.5141 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.0683**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.78e-04**), Residual SE = **17.857** on **527** df, AIC = **4677.4**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5309** | 9.0795 | ±18.1591 | **+13.936** | **3.84e-44** | *** |
| Education: graduate level (vs college) | -0.6488 | 1.6102 | ±3.2203 | -0.403 | 0.6870 |  |
| **Education: high school or below (vs college)** | **+5.9538** | 2.5494 | ±5.0987 | **+2.335** | **0.0195** | * |
| Site: UCSD (vs UAB) | +3.6146 | 2.0864 | ±4.1727 | +1.733 | 0.0832 | . |
| Site: UW (vs UAB) | -1.6564 | 1.7564 | ±3.5128 | -0.943 | 0.3456 |  |
| Season: spring (vs autumn) | +3.3915 | 1.8835 | ±3.7669 | +1.801 | 0.0718 | . |
| **Season: summer (vs autumn)** | **+5.0158** | 1.9556 | ±3.9112 | **+2.565** | **0.0103** | * |
| **Season: winter (vs autumn)** | **+6.5526** | 2.5368 | ±5.0736 | **+2.583** | **0.0098** | ** |
| Age (years) | -0.1651 | 0.0965 | ±0.1931 | -1.710 | 0.0872 | . |
| BMI (kg/m2) | +0.1402 | 0.1433 | ±0.2865 | +0.979 | 0.3276 |  |
| Hypertension | +0.6656 | 1.9493 | ±3.8986 | +0.341 | 0.7328 |  |
| High cholesterol | +2.2940 | 1.8139 | ±3.6278 | +1.265 | 0.2060 |  |
| Kidney disease | -2.0628 | 1.9620 | ±3.9241 | -1.051 | 0.2931 |  |
| Circulatory disease | +0.8674 | 2.0424 | ±4.0848 | +0.425 | 0.6710 |  |
| CV (%) | +0.0291 | 0.1418 | ±0.2836 | +0.205 | 0.8372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.0683**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.76e-04**), Residual SE = **17.857** on **527** df, AIC = **4677.4**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0299** | 10.7918 | ±21.5835 | **+11.864** | **1.83e-32** | *** |
| Education: graduate level (vs college) | -0.6471 | 1.6121 | ±3.2242 | -0.401 | 0.6881 |  |
| **Education: high school or below (vs college)** | **+5.9565** | 2.5465 | ±5.0930 | **+2.339** | **0.0193** | * |
| Site: UCSD (vs UAB) | +3.6043 | 2.0851 | ±4.1702 | +1.729 | 0.0839 | . |
| Site: UW (vs UAB) | -1.6635 | 1.7534 | ±3.5068 | -0.949 | 0.3428 |  |
| Season: spring (vs autumn) | +3.3832 | 1.8879 | ±3.7758 | +1.792 | 0.0731 | . |
| **Season: summer (vs autumn)** | **+4.9958** | 1.9639 | ±3.9277 | **+2.544** | **0.0110** | * |
| **Season: winter (vs autumn)** | **+6.5453** | 2.5444 | ±5.0888 | **+2.572** | **0.0101** | * |
| Age (years) | -0.1650 | 0.0963 | ±0.1926 | -1.713 | 0.0867 | . |
| BMI (kg/m2) | +0.1407 | 0.1429 | ±0.2858 | +0.985 | 0.3247 |  |
| Hypertension | +0.6708 | 1.9581 | ±3.9161 | +0.343 | 0.7319 |  |
| High cholesterol | +2.2822 | 1.8192 | ±3.6384 | +1.255 | 0.2097 |  |
| Kidney disease | -2.0555 | 1.9519 | ±3.9038 | -1.053 | 0.2923 |  |
| Circulatory disease | +0.8581 | 2.0400 | ±4.0800 | +0.421 | 0.6740 |  |
| Mean / SD ratio | -0.1850 | 0.8001 | ±1.6001 | -0.231 | 0.8172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.0697**, Adj R² = **0.0450**, F-statistic = **2.82** (p = **4.34e-04**), Residual SE = **17.844** on **527** df, AIC = **4676.6**, BIC = **4741.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.1044** | 10.1742 | ±20.3484 | **+12.788** | **1.92e-37** | *** |
| Education: graduate level (vs college) | -0.6110 | 1.6139 | ±3.2278 | -0.379 | 0.7050 |  |
| **Education: high school or below (vs college)** | **+5.8988** | 2.5400 | ±5.0799 | **+2.322** | **0.0202** | * |
| Site: UCSD (vs UAB) | +3.5902 | 2.0862 | ±4.1725 | +1.721 | 0.0853 | . |
| Site: UW (vs UAB) | -1.6171 | 1.7531 | ±3.5061 | -0.922 | 0.3563 |  |
| Season: spring (vs autumn) | +3.3976 | 1.8840 | ±3.7679 | +1.803 | 0.0713 | . |
| **Season: summer (vs autumn)** | **+5.0167** | 1.9576 | ±3.9151 | **+2.563** | **0.0104** | * |
| **Season: winter (vs autumn)** | **+6.5639** | 2.5256 | ±5.0513 | **+2.599** | **0.0094** | ** |
| Age (years) | -0.1671 | 0.0965 | ±0.1930 | -1.732 | 0.0833 | . |
| BMI (kg/m2) | +0.1486 | 0.1425 | ±0.2849 | +1.043 | 0.2969 |  |
| Hypertension | +0.6533 | 1.9651 | ±3.9303 | +0.332 | 0.7396 |  |
| High cholesterol | +2.2859 | 1.8187 | ±3.6373 | +1.257 | 0.2088 |  |
| Kidney disease | -2.2382 | 1.9629 | ±3.9257 | -1.140 | 0.2542 |  |
| Circulatory disease | +0.8643 | 2.0394 | ±4.0788 | +0.424 | 0.6717 |  |
| Avg. daily mean/SD | -0.5898 | 0.6093 | ±1.2186 | -0.968 | 0.3330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.84e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6264** | 9.5731 | ±19.1462 | **+13.227** | **6.10e-40** | *** |
| Education: graduate level (vs college) | -0.6430 | 1.6061 | ±3.2122 | -0.400 | 0.6889 |  |
| **Education: high school or below (vs college)** | **+5.9556** | 2.5719 | ±5.1438 | **+2.316** | **0.0206** | * |
| Site: UCSD (vs UAB) | +3.6191 | 2.0753 | ±4.1505 | +1.744 | 0.0812 | . |
| Site: UW (vs UAB) | -1.6542 | 1.7388 | ±3.4777 | -0.951 | 0.3414 |  |
| Season: spring (vs autumn) | +3.3881 | 1.8849 | ±3.7699 | +1.797 | 0.0723 | . |
| **Season: summer (vs autumn)** | **+5.0259** | 1.9621 | ±3.9241 | **+2.562** | **0.0104** | * |
| **Season: winter (vs autumn)** | **+6.5576** | 2.5305 | ±5.0610 | **+2.591** | **0.0096** | ** |
| Age (years) | -0.1634 | 0.0941 | ±0.1881 | -1.737 | 0.0824 | . |
| BMI (kg/m2) | +0.1402 | 0.1435 | ±0.2871 | +0.976 | 0.3288 |  |
| Hypertension | +0.6819 | 1.9697 | ±3.9394 | +0.346 | 0.7292 |  |
| High cholesterol | +2.2910 | 1.8264 | ±3.6527 | +1.254 | 0.2097 |  |
| Kidney disease | -2.0121 | 1.9267 | ±3.8534 | -1.044 | 0.2963 |  |
| Circulatory disease | +0.8648 | 2.0496 | ±4.0993 | +0.422 | 0.6731 |  |
| MAG (mg/dL/h) | +0.0105 | 0.0882 | ±0.1763 | +0.120 | 0.9048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.0684**, Adj R² = **0.0437**, F-statistic = **2.77** (p = **5.60e-04**), Residual SE = **17.856** on **527** df, AIC = **4677.4**, BIC = **4741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.6548** | 10.0538 | ±20.1075 | **+12.797** | **1.71e-37** | *** |
| Education: graduate level (vs college) | -0.6921 | 1.6064 | ±3.2129 | -0.431 | 0.6666 |  |
| **Education: high school or below (vs college)** | **+6.0579** | 2.5446 | ±5.0891 | **+2.381** | **0.0173** | * |
| Site: UCSD (vs UAB) | +3.5597 | 2.0934 | ±4.1868 | +1.700 | 0.0891 | . |
| Site: UW (vs UAB) | -1.7672 | 1.7595 | ±3.5189 | -1.004 | 0.3152 |  |
| Season: spring (vs autumn) | +3.4305 | 1.8924 | ±3.7849 | +1.813 | 0.0699 | . |
| **Season: summer (vs autumn)** | **+4.9718** | 1.9682 | ±3.9364 | **+2.526** | **0.0115** | * |
| **Season: winter (vs autumn)** | **+6.5898** | 2.5441 | ±5.0882 | **+2.590** | **0.0096** | ** |
| Age (years) | -0.1667 | 0.0961 | ±0.1922 | -1.735 | 0.0828 | . |
| BMI (kg/m2) | +0.1389 | 0.1435 | ±0.2871 | +0.968 | 0.3331 |  |
| Hypertension | +0.6781 | 1.9685 | ±3.9371 | +0.344 | 0.7305 |  |
| High cholesterol | +2.2783 | 1.8143 | ±3.6287 | +1.256 | 0.2092 |  |
| Kidney disease | -1.8455 | 1.9535 | ±3.9070 | -0.945 | 0.3448 |  |
| Circulatory disease | +0.8966 | 2.0408 | ±4.0816 | +0.439 | 0.6604 |  |
| Avg. daily range (mg/dL) | -0.0080 | 0.0213 | ±0.0426 | -0.375 | 0.7080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.0785**, Adj R² = **0.0540**, F-statistic = **3.21** (p = **6.91e-05**), Residual SE = **17.759** on **527** df, AIC = **4671.5**, BIC = **4735.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.9011** | 9.3642 | ±18.7284 | **+13.979** | **2.10e-44** | *** |
| Education: graduate level (vs college) | -1.0600 | 1.6023 | ±3.2046 | -0.662 | 0.5083 |  |
| **Education: high school or below (vs college)** | **+6.0714** | 2.5207 | ±5.0413 | **+2.409** | **0.0160** | * |
| Site: UCSD (vs UAB) | +3.3887 | 2.1021 | ±4.2041 | +1.612 | 0.1069 |  |
| Site: UW (vs UAB) | -2.1767 | 1.7713 | ±3.5426 | -1.229 | 0.2191 |  |
| Season: spring (vs autumn) | +3.3508 | 1.8715 | ±3.7431 | +1.790 | 0.0734 | . |
| **Season: summer (vs autumn)** | **+4.8536** | 1.9489 | ±3.8979 | **+2.490** | **0.0128** | * |
| **Season: winter (vs autumn)** | **+6.8801** | 2.4829 | ±4.9658 | **+2.771** | **0.0056** | ** |
| Age (years) | -0.1838 | 0.0958 | ±0.1916 | -1.919 | 0.0550 | . |
| BMI (kg/m2) | +0.1669 | 0.1489 | ±0.2977 | +1.121 | 0.2622 |  |
| Hypertension | +0.9566 | 1.9556 | ±3.9113 | +0.489 | 0.6247 |  |
| High cholesterol | +2.1181 | 1.7861 | ±3.5723 | +1.186 | 0.2357 |  |
| Kidney disease | -1.6493 | 1.9674 | ±3.9349 | -0.838 | 0.4019 |  |
| Circulatory disease | +1.3292 | 1.9863 | ±3.9727 | +0.669 | 0.5034 |  |
| SD of daily means (mg/dL) | -0.2203 | 0.1542 | ±0.3084 | -1.428 | 0.1532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.0741**, Adj R² = **0.0495**, F-statistic = **3.01** (p = **1.76e-04**), Residual SE = **17.801** on **527** df, AIC = **4674.1**, BIC = **4738.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.5735** | 9.5437 | ±19.0874 | **+12.948** | **2.41e-38** | *** |
| Education: graduate level (vs college) | -0.7921 | 1.5815 | ±3.1630 | -0.501 | 0.6165 |  |
| **Education: high school or below (vs college)** | **+6.3551** | 2.5546 | ±5.1092 | **+2.488** | **0.0129** | * |
| Site: UCSD (vs UAB) | +3.2540 | 2.1054 | ±4.2109 | +1.546 | 0.1222 |  |
| Site: UW (vs UAB) | -1.9645 | 1.7411 | ±3.4821 | -1.128 | 0.2592 |  |
| Season: spring (vs autumn) | +3.5178 | 1.8761 | ±3.7521 | +1.875 | 0.0608 | . |
| **Season: summer (vs autumn)** | **+4.8303** | 1.9696 | ±3.9391 | **+2.452** | **0.0142** | * |
| **Season: winter (vs autumn)** | **+6.7826** | 2.4802 | ±4.9605 | **+2.735** | **0.0062** | ** |
| Age (years) | -0.1715 | 0.0970 | ±0.1941 | -1.767 | 0.0772 | . |
| BMI (kg/m2) | +0.1599 | 0.1431 | ±0.2863 | +1.117 | 0.2639 |  |
| Hypertension | +0.6404 | 1.9566 | ±3.9132 | +0.327 | 0.7435 |  |
| High cholesterol | +2.1183 | 1.8105 | ±3.6211 | +1.170 | 0.2420 |  |
| Kidney disease | -1.7988 | 1.9680 | ±3.9360 | -0.914 | 0.3607 |  |
| Circulatory disease | +1.0450 | 2.0359 | ±4.0718 | +0.513 | 0.6078 |  |
| Time in range 70-180, pooled (%) | +0.0560 | 0.0322 | ±0.0644 | +1.741 | 0.0818 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.0748**, Adj R² = **0.0502**, F-statistic = **3.04** (p = **1.51e-04**), Residual SE = **17.794** on **527** df, AIC = **4673.6**, BIC = **4738.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.3001** | 9.5342 | ±19.0684 | **+12.932** | **2.95e-38** | *** |
| Education: graduate level (vs college) | -0.7840 | 1.5827 | ±3.1654 | -0.495 | 0.6203 |  |
| **Education: high school or below (vs college)** | **+6.3979** | 2.5515 | ±5.1031 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2141 | 2.1077 | ±4.2154 | +1.525 | 0.1273 |  |
| Site: UW (vs UAB) | -1.9865 | 1.7410 | ±3.4819 | -1.141 | 0.2539 |  |
| Season: spring (vs autumn) | +3.5384 | 1.8751 | ±3.7502 | +1.887 | 0.0592 | . |
| **Season: summer (vs autumn)** | **+4.8454** | 1.9658 | ±3.9315 | **+2.465** | **0.0137** | * |
| **Season: winter (vs autumn)** | **+6.8233** | 2.4750 | ±4.9500 | **+2.757** | **0.0058** | ** |
| Age (years) | -0.1714 | 0.0970 | ±0.1941 | -1.766 | 0.0774 | . |
| BMI (kg/m2) | +0.1617 | 0.1429 | ±0.2858 | +1.132 | 0.2577 |  |
| Hypertension | +0.6314 | 1.9561 | ±3.9122 | +0.323 | 0.7469 |  |
| High cholesterol | +2.1138 | 1.8089 | ±3.6178 | +1.169 | 0.2426 |  |
| Kidney disease | -1.7647 | 1.9649 | ±3.9299 | -0.898 | 0.3691 |  |
| Circulatory disease | +1.0559 | 2.0358 | ±4.0715 | +0.519 | 0.6040 |  |
| Avg. daily time in range 70-180 (%) | +0.0589 | 0.0320 | ±0.0640 | +1.843 | 0.0654 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.0685**, Adj R² = **0.0438**, F-statistic = **2.77** (p = **5.53e-04**), Residual SE = **17.855** on **527** df, AIC = **4677.3**, BIC = **4741.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9144** | 9.0365 | ±18.0730 | **+14.045** | **8.31e-45** | *** |
| Education: graduate level (vs college) | -0.6589 | 1.6030 | ±3.2060 | -0.411 | 0.6811 |  |
| **Education: high school or below (vs college)** | **+5.9868** | 2.5429 | ±5.0858 | **+2.354** | **0.0186** | * |
| Site: UCSD (vs UAB) | +3.6596 | 2.0856 | ±4.1713 | +1.755 | 0.0793 | . |
| Site: UW (vs UAB) | -1.6458 | 1.7260 | ±3.4520 | -0.954 | 0.3403 |  |
| Season: spring (vs autumn) | +3.3813 | 1.8907 | ±3.7815 | +1.788 | 0.0737 | . |
| **Season: summer (vs autumn)** | **+5.0174** | 1.9569 | ±3.9139 | **+2.564** | **0.0104** | * |
| **Season: winter (vs autumn)** | **+6.6152** | 2.5593 | ±5.1186 | **+2.585** | **0.0097** | ** |
| Age (years) | -0.1627 | 0.0939 | ±0.1878 | -1.732 | 0.0832 | . |
| BMI (kg/m2) | +0.1397 | 0.1439 | ±0.2878 | +0.971 | 0.3317 |  |
| Hypertension | +0.6125 | 1.9706 | ±3.9413 | +0.311 | 0.7560 |  |
| High cholesterol | +2.3373 | 1.8347 | ±3.6694 | +1.274 | 0.2027 |  |
| Kidney disease | -2.0031 | 1.9641 | ±3.9282 | -1.020 | 0.3078 |  |
| Circulatory disease | +0.8199 | 2.0347 | ±4.0693 | +0.403 | 0.6870 |  |
| Any reading < 54 during wear (0/1) | +0.7789 | 2.2245 | ±4.4491 | +0.350 | 0.7262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.0683**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.74e-04**), Residual SE = **17.857** on **527** df, AIC = **4677.4**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1421** | 9.3470 | ±18.6940 | **+13.602** | **3.87e-42** | *** |
| Education: graduate level (vs college) | -0.6430 | 1.5999 | ±3.1998 | -0.402 | 0.6878 |  |
| **Education: high school or below (vs college)** | **+5.9964** | 2.5406 | ±5.0812 | **+2.360** | **0.0183** | * |
| Site: UCSD (vs UAB) | +3.6514 | 2.0957 | ±4.1914 | +1.742 | 0.0815 | . |
| Site: UW (vs UAB) | -1.6371 | 1.7543 | ±3.5086 | -0.933 | 0.3507 |  |
| Season: spring (vs autumn) | +3.4110 | 1.8887 | ±3.7773 | +1.806 | 0.0709 | . |
| **Season: summer (vs autumn)** | **+5.0306** | 1.9686 | ±3.9373 | **+2.555** | **0.0106** | * |
| **Season: winter (vs autumn)** | **+6.5941** | 2.5397 | ±5.0794 | **+2.596** | **0.0094** | ** |
| Age (years) | -0.1651 | 0.0961 | ±0.1922 | -1.718 | 0.0858 | . |
| BMI (kg/m2) | +0.1398 | 0.1438 | ±0.2875 | +0.972 | 0.3309 |  |
| Hypertension | +0.6334 | 1.9743 | ±3.9487 | +0.321 | 0.7484 |  |
| High cholesterol | +2.3244 | 1.8236 | ±3.6471 | +1.275 | 0.2024 |  |
| Kidney disease | -1.9950 | 1.9632 | ±3.9263 | -1.016 | 0.3095 |  |
| Circulatory disease | +0.9028 | 2.0477 | ±4.0955 | +0.441 | 0.6593 |  |
| Time < 54 (%) | +0.7908 | 2.6356 | ±5.2712 | +0.300 | 0.7641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.87e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2133** | 9.3637 | ±18.7273 | **+13.586** | **4.86e-42** | *** |
| Education: graduate level (vs college) | -0.6573 | 1.5993 | ±3.1987 | -0.411 | 0.6811 |  |
| **Education: high school or below (vs college)** | **+5.9760** | 2.5465 | ±5.0931 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | +3.6151 | 2.0881 | ±4.1761 | +1.731 | 0.0834 | . |
| Site: UW (vs UAB) | -1.6832 | 1.7553 | ±3.5106 | -0.959 | 0.3376 |  |
| Season: spring (vs autumn) | +3.4008 | 1.8899 | ±3.7799 | +1.799 | 0.0719 | . |
| **Season: summer (vs autumn)** | **+5.0109** | 1.9749 | ±3.9498 | **+2.537** | **0.0112** | * |
| **Season: winter (vs autumn)** | **+6.5646** | 2.5371 | ±5.0742 | **+2.587** | **0.0097** | ** |
| Age (years) | -0.1648 | 0.0960 | ±0.1919 | -1.717 | 0.0859 | . |
| BMI (kg/m2) | +0.1398 | 0.1438 | ±0.2876 | +0.972 | 0.3310 |  |
| Hypertension | +0.6765 | 1.9756 | ±3.9513 | +0.342 | 0.7320 |  |
| High cholesterol | +2.2924 | 1.8250 | ±3.6501 | +1.256 | 0.2091 |  |
| Kidney disease | -1.9889 | 1.9647 | ±3.9293 | -1.012 | 0.3114 |  |
| Circulatory disease | +0.8732 | 2.0423 | ±4.0845 | +0.428 | 0.6690 |  |
| Avg. daily time < 54 (%) | +0.1231 | 1.5991 | ±3.1983 | +0.077 | 0.9386 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.0684**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.70e-04**), Residual SE = **17.856** on **527** df, AIC = **4677.4**, BIC = **4741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0942** | 9.3288 | ±18.6577 | **+13.624** | **2.89e-42** | *** |
| Education: graduate level (vs college) | -0.6454 | 1.6069 | ±3.2137 | -0.402 | 0.6880 |  |
| **Education: high school or below (vs college)** | **+5.9740** | 2.5470 | ±5.0940 | **+2.346** | **0.0190** | * |
| Site: UCSD (vs UAB) | +3.6663 | 2.0927 | ±4.1855 | +1.752 | 0.0798 | . |
| Site: UW (vs UAB) | -1.6377 | 1.7576 | ±3.5151 | -0.932 | 0.3514 |  |
| Season: spring (vs autumn) | +3.4368 | 1.8749 | ±3.7497 | +1.833 | 0.0668 | . |
| **Season: summer (vs autumn)** | **+5.0436** | 1.9498 | ±3.8997 | **+2.587** | **0.0097** | ** |
| **Season: winter (vs autumn)** | **+6.6001** | 2.5163 | ±5.0327 | **+2.623** | **0.0087** | ** |
| Age (years) | -0.1656 | 0.0964 | ±0.1928 | -1.718 | 0.0858 | . |
| BMI (kg/m2) | +0.1410 | 0.1431 | ±0.2863 | +0.985 | 0.3244 |  |
| Hypertension | +0.6378 | 1.9629 | ±3.9257 | +0.325 | 0.7452 |  |
| High cholesterol | +2.3321 | 1.8347 | ±3.6693 | +1.271 | 0.2037 |  |
| Kidney disease | -2.0124 | 1.9653 | ±3.9305 | -1.024 | 0.3058 |  |
| Circulatory disease | +0.8963 | 2.0453 | ±4.0906 | +0.438 | 0.6612 |  |
| Time 54-69, pooled (%) | +0.2506 | 0.8006 | ±1.6012 | +0.313 | 0.7543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.86e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2509** | 9.3386 | ±18.6771 | **+13.626** | **2.79e-42** | *** |
| Education: graduate level (vs college) | -0.6648 | 1.6060 | ±3.2119 | -0.414 | 0.6789 |  |
| **Education: high school or below (vs college)** | **+5.9693** | 2.5484 | ±5.0968 | **+2.342** | **0.0192** | * |
| Site: UCSD (vs UAB) | +3.5933 | 2.0922 | ±4.1844 | +1.717 | 0.0859 | . |
| Site: UW (vs UAB) | -1.7077 | 1.7589 | ±3.5178 | -0.971 | 0.3316 |  |
| Season: spring (vs autumn) | +3.3790 | 1.8737 | ±3.7475 | +1.803 | 0.0713 | . |
| **Season: summer (vs autumn)** | **+4.9907** | 1.9499 | ±3.8999 | **+2.559** | **0.0105** | * |
| **Season: winter (vs autumn)** | **+6.5449** | 2.5199 | ±5.0398 | **+2.597** | **0.0094** | ** |
| Age (years) | -0.1645 | 0.0965 | ±0.1930 | -1.705 | 0.0883 | . |
| BMI (kg/m2) | +0.1398 | 0.1433 | ±0.2867 | +0.975 | 0.3296 |  |
| Hypertension | +0.6953 | 1.9654 | ±3.9308 | +0.354 | 0.7235 |  |
| High cholesterol | +2.2731 | 1.8381 | ±3.6762 | +1.237 | 0.2162 |  |
| Kidney disease | -1.9793 | 1.9627 | ±3.9253 | -1.008 | 0.3132 |  |
| Circulatory disease | +0.8606 | 2.0449 | ±4.0898 | +0.421 | 0.6739 |  |
| Avg. daily time 54-69 (%) | -0.0593 | 0.7153 | ±1.4307 | -0.083 | 0.9340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.0684**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.68e-04**), Residual SE = **17.856** on **527** df, AIC = **4677.4**, BIC = **4741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0851** | 9.3240 | ±18.6480 | **+13.630** | **2.66e-42** | *** |
| Education: graduate level (vs college) | -0.6422 | 1.6063 | ±3.2125 | -0.400 | 0.6893 |  |
| **Education: high school or below (vs college)** | **+5.9808** | 2.5453 | ±5.0906 | **+2.350** | **0.0188** | * |
| Site: UCSD (vs UAB) | +3.6721 | 2.0952 | ±4.1903 | +1.753 | 0.0797 | . |
| Site: UW (vs UAB) | -1.6282 | 1.7576 | ±3.5152 | -0.926 | 0.3542 |  |
| Season: spring (vs autumn) | +3.4374 | 1.8788 | ±3.7576 | +1.830 | 0.0673 | . |
| **Season: summer (vs autumn)** | **+5.0471** | 1.9534 | ±3.9067 | **+2.584** | **0.0098** | ** |
| **Season: winter (vs autumn)** | **+6.6060** | 2.5199 | ±5.0398 | **+2.622** | **0.0088** | ** |
| Age (years) | -0.1656 | 0.0964 | ±0.1928 | -1.718 | 0.0858 | . |
| BMI (kg/m2) | +0.1409 | 0.1432 | ±0.2864 | +0.984 | 0.3252 |  |
| Hypertension | +0.6288 | 1.9646 | ±3.9292 | +0.320 | 0.7489 |  |
| High cholesterol | +2.3379 | 1.8346 | ±3.6692 | +1.274 | 0.2025 |  |
| Kidney disease | -2.0121 | 1.9663 | ±3.9326 | -1.023 | 0.3062 |  |
| Circulatory disease | +0.9029 | 2.0461 | ±4.0923 | +0.441 | 0.6590 |  |
| Time < 70 (%) | +0.2226 | 0.6548 | ±1.3097 | +0.340 | 0.7339 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.87e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2409** | 9.3397 | ±18.6795 | **+13.624** | **2.90e-42** | *** |
| Education: graduate level (vs college) | -0.6627 | 1.6045 | ±3.2091 | -0.413 | 0.6796 |  |
| **Education: high school or below (vs college)** | **+5.9692** | 2.5477 | ±5.0954 | **+2.343** | **0.0191** | * |
| Site: UCSD (vs UAB) | +3.5996 | 2.0920 | ±4.1840 | +1.721 | 0.0853 | . |
| Site: UW (vs UAB) | -1.7015 | 1.7586 | ±3.5171 | -0.968 | 0.3333 |  |
| Season: spring (vs autumn) | +3.3832 | 1.8765 | ±3.7530 | +1.803 | 0.0714 | . |
| **Season: summer (vs autumn)** | **+4.9942** | 1.9545 | ±3.9089 | **+2.555** | **0.0106** | * |
| **Season: winter (vs autumn)** | **+6.5487** | 2.5222 | ±5.0443 | **+2.596** | **0.0094** | ** |
| Age (years) | -0.1646 | 0.0964 | ±0.1927 | -1.708 | 0.0876 | . |
| BMI (kg/m2) | +0.1399 | 0.1435 | ±0.2869 | +0.975 | 0.3296 |  |
| Hypertension | +0.6904 | 1.9689 | ±3.9378 | +0.351 | 0.7258 |  |
| High cholesterol | +2.2782 | 1.8368 | ±3.6736 | +1.240 | 0.2148 |  |
| Kidney disease | -1.9818 | 1.9636 | ±3.9273 | -1.009 | 0.3129 |  |
| Circulatory disease | +0.8640 | 2.0446 | ±4.0892 | +0.423 | 0.6726 |  |
| Avg. daily time < 70 (%) | -0.0267 | 0.5009 | ±1.0018 | -0.053 | 0.9575 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.0761**, Adj R² = **0.0516**, F-statistic = **3.10** (p = **1.16e-04**), Residual SE = **17.782** on **527** df, AIC = **4672.9**, BIC = **4737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.8760** | 9.6513 | ±19.3027 | **+12.421** | **2.02e-35** | *** |
| Education: graduate level (vs college) | -0.9648 | 1.5949 | ±3.1899 | -0.605 | 0.5453 |  |
| **Education: high school or below (vs college)** | **+6.3524** | 2.5440 | ±5.0881 | **+2.497** | **0.0125** | * |
| Site: UCSD (vs UAB) | +3.2807 | 2.1145 | ±4.2290 | +1.552 | 0.1208 |  |
| Site: UW (vs UAB) | -2.1256 | 1.7719 | ±3.5438 | -1.200 | 0.2303 |  |
| Season: spring (vs autumn) | +3.3809 | 1.8938 | ±3.7875 | +1.785 | 0.0742 | . |
| **Season: summer (vs autumn)** | **+4.5853** | 1.9985 | ±3.9969 | **+2.294** | **0.0218** | * |
| **Season: winter (vs autumn)** | **+6.6156** | 2.5057 | ±5.0114 | **+2.640** | **0.0083** | ** |
| Age (years) | -0.1807 | 0.0972 | ±0.1945 | -1.859 | 0.0630 | . |
| BMI (kg/m2) | +0.1529 | 0.1420 | ±0.2840 | +1.077 | 0.2817 |  |
| Hypertension | +0.8398 | 1.9506 | ±3.9013 | +0.431 | 0.6668 |  |
| High cholesterol | +2.1608 | 1.7991 | ±3.5981 | +1.201 | 0.2297 |  |
| Kidney disease | -1.7775 | 1.9531 | ±3.9063 | -0.910 | 0.3628 |  |
| Circulatory disease | +1.0206 | 2.0325 | ±4.0650 | +0.502 | 0.6156 |  |
| **Time 54-250, pooled (%)** | **+0.0918** | 0.0468 | ±0.0937 | **+1.960** | **0.0500** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.0769**, Adj R² = **0.0523**, F-statistic = **3.13** (p = **9.82e-05**), Residual SE = **17.775** on **527** df, AIC = **4672.4**, BIC = **4736.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.2812** | 9.6541 | ±19.3081 | **+12.356** | **4.55e-35** | *** |
| Education: graduate level (vs college) | -0.9763 | 1.5952 | ±3.1905 | -0.612 | 0.5405 |  |
| **Education: high school or below (vs college)** | **+6.3691** | 2.5393 | ±5.0785 | **+2.508** | **0.0121** | * |
| Site: UCSD (vs UAB) | +3.2579 | 2.1138 | ±4.2276 | +1.541 | 0.1233 |  |
| Site: UW (vs UAB) | -2.1319 | 1.7688 | ±3.5376 | -1.205 | 0.2281 |  |
| Season: spring (vs autumn) | +3.3992 | 1.8933 | ±3.7866 | +1.795 | 0.0726 | . |
| **Season: summer (vs autumn)** | **+4.5952** | 1.9947 | ±3.9895 | **+2.304** | **0.0212** | * |
| **Season: winter (vs autumn)** | **+6.6390** | 2.5033 | ±5.0066 | **+2.652** | **0.0080** | ** |
| Age (years) | -0.1797 | 0.0971 | ±0.1943 | -1.850 | 0.0643 | . |
| BMI (kg/m2) | +0.1539 | 0.1416 | ±0.2832 | +1.087 | 0.2771 |  |
| Hypertension | +0.8346 | 1.9510 | ±3.9019 | +0.428 | 0.6688 |  |
| High cholesterol | +2.1552 | 1.7985 | ±3.5969 | +1.198 | 0.2308 |  |
| Kidney disease | -1.7382 | 1.9498 | ±3.8996 | -0.891 | 0.3727 |  |
| Circulatory disease | +1.0438 | 2.0346 | ±4.0692 | +0.513 | 0.6079 |  |
| **Avg. daily time 54-250 (%)** | **+0.0970** | 0.0480 | ±0.0961 | **+2.018** | **0.0435** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.0688**, Adj R² = **0.0441**, F-statistic = **2.78** (p = **5.18e-04**), Residual SE = **17.852** on **527** df, AIC = **4677.1**, BIC = **4741.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.6836** | 9.4537 | ±18.9074 | **+13.506** | **1.44e-41** | *** |
| Education: graduate level (vs college) | -0.6275 | 1.6160 | ±3.2319 | -0.388 | 0.6978 |  |
| **Education: high school or below (vs college)** | **+6.0571** | 2.5609 | ±5.1219 | **+2.365** | **0.0180** | * |
| Site: UCSD (vs UAB) | +3.5279 | 2.0807 | ±4.1614 | +1.696 | 0.0900 | . |
| Site: UW (vs UAB) | -1.6899 | 1.7550 | ±3.5099 | -0.963 | 0.3356 |  |
| Season: spring (vs autumn) | +3.4719 | 1.8747 | ±3.7494 | +1.852 | 0.0640 | . |
| **Season: summer (vs autumn)** | **+5.0535** | 1.9527 | ±3.9053 | **+2.588** | **0.0097** | ** |
| **Season: winter (vs autumn)** | **+6.6690** | 2.4539 | ±4.9079 | **+2.718** | **0.0066** | ** |
| Age (years) | -0.1631 | 0.0967 | ±0.1934 | -1.687 | 0.0916 | . |
| BMI (kg/m2) | +0.1469 | 0.1451 | ±0.2903 | +1.012 | 0.3115 |  |
| Hypertension | +0.5993 | 1.9280 | ±3.8560 | +0.311 | 0.7559 |  |
| High cholesterol | +2.2396 | 1.8360 | ±3.6720 | +1.220 | 0.2225 |  |
| Kidney disease | -1.9549 | 1.9730 | ±3.9461 | -0.991 | 0.3218 |  |
| Circulatory disease | +0.9195 | 2.0436 | ±4.0872 | +0.450 | 0.6528 |  |
| Time 181-250, pooled (%) | -0.0318 | 0.0642 | ±0.1284 | -0.495 | 0.6208 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.0690**, Adj R² = **0.0443**, F-statistic = **2.79** (p = **5.00e-04**), Residual SE = **17.850** on **527** df, AIC = **4677.0**, BIC = **4741.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7537** | 9.4520 | ±18.9040 | **+13.516** | **1.26e-41** | *** |
| Education: graduate level (vs college) | -0.6164 | 1.6179 | ±3.2359 | -0.381 | 0.7032 |  |
| **Education: high school or below (vs college)** | **+6.0827** | 2.5620 | ±5.1241 | **+2.374** | **0.0176** | * |
| Site: UCSD (vs UAB) | +3.5080 | 2.0844 | ±4.1688 | +1.683 | 0.0924 | . |
| Site: UW (vs UAB) | -1.6997 | 1.7511 | ±3.5023 | -0.971 | 0.3317 |  |
| Season: spring (vs autumn) | +3.4828 | 1.8742 | ±3.7484 | +1.858 | 0.0631 | . |
| **Season: summer (vs autumn)** | **+5.0617** | 1.9531 | ±3.9061 | **+2.592** | **0.0096** | ** |
| **Season: winter (vs autumn)** | **+6.6916** | 2.4506 | ±4.9011 | **+2.731** | **0.0063** | ** |
| Age (years) | -0.1634 | 0.0967 | ±0.1934 | -1.690 | 0.0910 | . |
| BMI (kg/m2) | +0.1480 | 0.1454 | ±0.2907 | +1.018 | 0.3087 |  |
| Hypertension | +0.5905 | 1.9321 | ±3.8641 | +0.306 | 0.7599 |  |
| High cholesterol | +2.2372 | 1.8320 | ±3.6641 | +1.221 | 0.2220 |  |
| Kidney disease | -1.9467 | 1.9737 | ±3.9473 | -0.986 | 0.3240 |  |
| Circulatory disease | +0.9217 | 2.0409 | ±4.0818 | +0.452 | 0.6515 |  |
| Avg. daily time 181-250 (%) | -0.0353 | 0.0614 | ±0.1228 | -0.574 | 0.5657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.0741**, Adj R² = **0.0495**, F-statistic = **3.01** (p = **1.76e-04**), Residual SE = **17.801** on **527** df, AIC = **4674.1**, BIC = **4738.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.1263** | 9.5501 | ±19.1001 | **+13.521** | **1.18e-41** | *** |
| Education: graduate level (vs college) | -0.7865 | 1.5822 | ±3.1645 | -0.497 | 0.6191 |  |
| **Education: high school or below (vs college)** | **+6.3544** | 2.5539 | ±5.1078 | **+2.488** | **0.0128** | * |
| Site: UCSD (vs UAB) | +3.2730 | 2.1037 | ±4.2074 | +1.556 | 0.1197 |  |
| Site: UW (vs UAB) | -1.9462 | 1.7415 | ±3.4830 | -1.118 | 0.2638 |  |
| Season: spring (vs autumn) | +3.5285 | 1.8758 | ±3.7517 | +1.881 | 0.0600 | . |
| **Season: summer (vs autumn)** | **+4.8432** | 1.9686 | ±3.9372 | **+2.460** | **0.0139** | * |
| **Season: winter (vs autumn)** | **+6.7934** | 2.4783 | ±4.9565 | **+2.741** | **0.0061** | ** |
| Age (years) | -0.1716 | 0.0971 | ±0.1941 | -1.768 | 0.0770 | . |
| BMI (kg/m2) | +0.1600 | 0.1431 | ±0.2862 | +1.118 | 0.2635 |  |
| Hypertension | +0.6270 | 1.9560 | ±3.9119 | +0.321 | 0.7485 |  |
| High cholesterol | +2.1328 | 1.8100 | ±3.6201 | +1.178 | 0.2387 |  |
| Kidney disease | -1.8071 | 1.9673 | ±3.9347 | -0.919 | 0.3583 |  |
| Circulatory disease | +1.0521 | 2.0357 | ±4.0714 | +0.517 | 0.6053 |  |
| Time > 180 (%) | -0.0556 | 0.0319 | ±0.0639 | -1.740 | 0.0819 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.0747**, Adj R² = **0.0501**, F-statistic = **3.04** (p = **1.54e-04**), Residual SE = **17.795** on **527** df, AIC = **4673.7**, BIC = **4738.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.1372** | 9.5468 | ±19.0936 | **+13.527** | **1.09e-41** | *** |
| Education: graduate level (vs college) | -0.7764 | 1.5835 | ±3.1671 | -0.490 | 0.6239 |  |
| **Education: high school or below (vs college)** | **+6.3959** | 2.5515 | ±5.1029 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2373 | 2.1057 | ±4.2115 | +1.537 | 0.1242 |  |
| Site: UW (vs UAB) | -1.9631 | 1.7413 | ±3.4826 | -1.127 | 0.2596 |  |
| Season: spring (vs autumn) | +3.5524 | 1.8751 | ±3.7501 | +1.895 | 0.0582 | . |
| **Season: summer (vs autumn)** | **+4.8624** | 1.9649 | ±3.9297 | **+2.475** | **0.0133** | * |
| **Season: winter (vs autumn)** | **+6.8342** | 2.4730 | ±4.9460 | **+2.763** | **0.0057** | ** |
| Age (years) | -0.1716 | 0.0971 | ±0.1942 | -1.767 | 0.0772 | . |
| BMI (kg/m2) | +0.1615 | 0.1429 | ±0.2857 | +1.131 | 0.2582 |  |
| Hypertension | +0.6173 | 1.9556 | ±3.9112 | +0.316 | 0.7523 |  |
| High cholesterol | +2.1315 | 1.8086 | ±3.6171 | +1.179 | 0.2386 |  |
| Kidney disease | -1.7754 | 1.9644 | ±3.9289 | -0.904 | 0.3661 |  |
| Circulatory disease | +1.0633 | 2.0356 | ±4.0712 | +0.522 | 0.6014 |  |
| Avg. daily time > 180 (%) | -0.0581 | 0.0318 | ±0.0636 | -1.829 | 0.0674 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.0703**, Adj R² = **0.0456**, F-statistic = **2.84** (p = **3.88e-04**), Residual SE = **17.838** on **527** df, AIC = **4676.3**, BIC = **4740.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0676** | 9.5606 | ±19.1212 | **+13.395** | **6.44e-41** | *** |
| Education: graduate level (vs college) | -0.7986 | 1.5748 | ±3.1496 | -0.507 | 0.6121 |  |
| **Education: high school or below (vs college)** | **+6.1578** | 2.5498 | ±5.0996 | **+2.415** | **0.0157** | * |
| Site: UCSD (vs UAB) | +3.3852 | 2.1157 | ±4.2314 | +1.600 | 0.1096 |  |
| Site: UW (vs UAB) | -1.7902 | 1.7396 | ±3.4791 | -1.029 | 0.3034 |  |
| Season: spring (vs autumn) | +3.4782 | 1.8740 | ±3.7479 | +1.856 | 0.0634 | . |
| **Season: summer (vs autumn)** | **+4.8970** | 1.9764 | ±3.9527 | **+2.478** | **0.0132** | * |
| **Season: winter (vs autumn)** | **+6.6923** | 2.4806 | ±4.9613 | **+2.698** | **0.0070** | ** |
| Age (years) | -0.1720 | 0.0978 | ±0.1957 | -1.758 | 0.0788 | . |
| BMI (kg/m2) | +0.1578 | 0.1435 | ±0.2869 | +1.100 | 0.2714 |  |
| Hypertension | +0.6473 | 1.9645 | ±3.9289 | +0.329 | 0.7418 |  |
| High cholesterol | +2.1753 | 1.8146 | ±3.6292 | +1.199 | 0.2306 |  |
| Kidney disease | -1.9022 | 1.9718 | ±3.9435 | -0.965 | 0.3347 |  |
| Circulatory disease | +0.9832 | 2.0291 | ±4.0583 | +0.485 | 0.6280 |  |
| Nocturnal time > 180 (%) | -0.0291 | 0.0318 | ±0.0636 | -0.914 | 0.3610 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.0761**, Adj R² = **0.0516**, F-statistic = **3.10** (p = **1.15e-04**), Residual SE = **17.782** on **527** df, AIC = **4672.9**, BIC = **4737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.0457** | 9.4915 | ±18.9830 | **+13.596** | **4.23e-42** | *** |
| Education: graduate level (vs college) | -0.9630 | 1.5951 | ±3.1902 | -0.604 | 0.5460 |  |
| **Education: high school or below (vs college)** | **+6.3557** | 2.5438 | ±5.0876 | **+2.498** | **0.0125** | * |
| Site: UCSD (vs UAB) | +3.2855 | 2.1139 | ±4.2277 | +1.554 | 0.1201 |  |
| Site: UW (vs UAB) | -2.1196 | 1.7714 | ±3.5429 | -1.197 | 0.2315 |  |
| Season: spring (vs autumn) | +3.3833 | 1.8938 | ±3.7876 | +1.787 | 0.0740 | . |
| **Season: summer (vs autumn)** | **+4.5884** | 1.9979 | ±3.9957 | **+2.297** | **0.0216** | * |
| **Season: winter (vs autumn)** | **+6.6202** | 2.5055 | ±5.0110 | **+2.642** | **0.0082** | ** |
| Age (years) | -0.1808 | 0.0972 | ±0.1945 | -1.859 | 0.0630 | . |
| BMI (kg/m2) | +0.1529 | 0.1420 | ±0.2839 | +1.077 | 0.2816 |  |
| Hypertension | +0.8341 | 1.9507 | ±3.9015 | +0.428 | 0.6690 |  |
| High cholesterol | +2.1652 | 1.7993 | ±3.5986 | +1.203 | 0.2288 |  |
| Kidney disease | -1.7785 | 1.9529 | ±3.9058 | -0.911 | 0.3625 |  |
| Circulatory disease | +1.0247 | 2.0324 | ±4.0648 | +0.504 | 0.6141 |  |
| **Time > 250 (%)** | **-0.0919** | 0.0469 | ±0.0937 | **-1.961** | **0.0499** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.0769**, Adj R² = **0.0524**, F-statistic = **3.13** (p = **9.81e-05**), Residual SE = **17.775** on **527** df, AIC = **4672.4**, BIC = **4736.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.9670** | 9.4775 | ±18.9550 | **+13.608** | **3.60e-42** | *** |
| Education: graduate level (vs college) | -0.9742 | 1.5953 | ±3.1906 | -0.611 | 0.5414 |  |
| **Education: high school or below (vs college)** | **+6.3731** | 2.5393 | ±5.0785 | **+2.510** | **0.0121** | * |
| Site: UCSD (vs UAB) | +3.2637 | 2.1131 | ±4.2262 | +1.544 | 0.1225 |  |
| Site: UW (vs UAB) | -2.1245 | 1.7682 | ±3.5364 | -1.201 | 0.2296 |  |
| Season: spring (vs autumn) | +3.4073 | 1.8932 | ±3.7863 | +1.800 | 0.0719 | . |
| **Season: summer (vs autumn)** | **+4.6029** | 1.9936 | ±3.9873 | **+2.309** | **0.0210** | * |
| **Season: winter (vs autumn)** | **+6.6462** | 2.5031 | ±5.0062 | **+2.655** | **0.0079** | ** |
| Age (years) | -0.1798 | 0.0972 | ±0.1943 | -1.850 | 0.0643 | . |
| BMI (kg/m2) | +0.1538 | 0.1416 | ±0.2832 | +1.086 | 0.2774 |  |
| Hypertension | +0.8290 | 1.9510 | ±3.9019 | +0.425 | 0.6709 |  |
| High cholesterol | +2.1608 | 1.7988 | ±3.5976 | +1.201 | 0.2296 |  |
| Kidney disease | -1.7411 | 1.9496 | ±3.8991 | -0.893 | 0.3718 |  |
| Circulatory disease | +1.0474 | 2.0345 | ±4.0691 | +0.515 | 0.6067 |  |
| **Avg. daily time > 250 (%)** | **-0.0970** | 0.0481 | ±0.0962 | **-2.017** | **0.0437** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 472; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **472**, R² = **0.1966**, Adj R² = **0.1791**, F-statistic = **11.28** (p = **2.43e-17**), Residual SE = **4872.087** on **461** df, AIC = **9366.1**, BIC = **9411.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24856.2959** | 2073.1925 | ±4146.3851 | **+11.989** | **4.04e-33** | *** |
| Education: graduate level (vs college) | +487.4421 | 536.2052 | ±1072.4104 | +0.909 | 0.3633 |  |
| Education: high school or below (vs college) | +534.7551 | 675.5884 | ±1351.1768 | +0.792 | 0.4286 |  |
| Site: UCSD (vs UAB) | +338.4270 | 574.5626 | ±1149.1252 | +0.589 | 0.5559 |  |
| Site: UW (vs UAB) | -30.1623 | 576.3463 | ±1152.6926 | -0.052 | 0.9583 |  |
| **Age (years)** | **-191.8012** | 22.3149 | ±44.6297 | **-8.595** | **8.31e-18** | *** |
| **BMI (kg/m2)** | **-73.8345** | 35.9253 | ±71.8506 | **-2.055** | **0.0399** | * |
| Hypertension | -214.1809 | 512.1864 | ±1024.3727 | -0.418 | 0.6758 |  |
| High cholesterol | +57.3563 | 500.1355 | ±1000.2710 | +0.115 | 0.9087 |  |
| **Kidney disease** | **-1685.8688** | 520.9521 | ±1041.9043 | **-3.236** | **0.0012** | ** |
| **Circulatory disease** | **-1592.1991** | 505.6109 | ±1011.2218 | **-3.149** | **0.0016** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **472**, R² = **0.1978**, Adj R² = **0.1787**, F-statistic = **10.31** (p = **6.03e-17**), Residual SE = **4873.512** on **460** df, AIC = **9367.4**, BIC = **9417.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23888.0976** | 2348.4632 | ±4696.9264 | **+10.172** | **2.65e-24** | *** |
| Education: graduate level (vs college) | +520.3795 | 540.6789 | ±1081.3577 | +0.962 | 0.3358 |  |
| Education: high school or below (vs college) | +483.2041 | 666.7410 | ±1333.4820 | +0.725 | 0.4686 |  |
| Site: UCSD (vs UAB) | +354.2709 | 575.4884 | ±1150.9768 | +0.616 | 0.5382 |  |
| Site: UW (vs UAB) | +0.0035 | 575.8740 | ±1151.7480 | +0.000 | 1.0000 |  |
| **Age (years)** | **-190.8131** | 22.2563 | ±44.5127 | **-8.573** | **1.00e-17** | *** |
| **BMI (kg/m2)** | **-78.1112** | 36.4444 | ±72.8887 | **-2.143** | **0.0321** | * |
| Hypertension | -226.9564 | 514.4663 | ±1028.9325 | -0.441 | 0.6591 |  |
| High cholesterol | +69.0176 | 502.2258 | ±1004.4517 | +0.137 | 0.8907 |  |
| **Kidney disease** | **-1659.0903** | 520.5958 | ±1041.1917 | **-3.187** | **0.0014** | ** |
| **Circulatory disease** | **-1589.2781** | 505.2722 | ±1010.5444 | **-3.145** | **0.0017** | ** |
| HbA1c (%) | +142.7373 | 181.4808 | ±362.9616 | +0.787 | 0.4316 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **472**, R² = **0.1966**, Adj R² = **0.1774**, F-statistic = **10.23** (p = **8.38e-17**), Residual SE = **4877.297** on **460** df, AIC = **9368.1**, BIC = **9418.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24737.1970** | 2229.0426 | ±4458.0851 | **+11.098** | **1.29e-28** | *** |
| Education: graduate level (vs college) | +490.8379 | 541.2748 | ±1082.5495 | +0.907 | 0.3645 |  |
| Education: high school or below (vs college) | +527.4510 | 660.9869 | ±1321.9737 | +0.798 | 0.4249 |  |
| Site: UCSD (vs UAB) | +342.3679 | 575.7320 | ±1151.4639 | +0.595 | 0.5521 |  |
| Site: UW (vs UAB) | -26.1578 | 575.6442 | ±1151.2885 | -0.045 | 0.9638 |  |
| **Age (years)** | **-191.6273** | 22.1867 | ±44.3733 | **-8.637** | **5.77e-18** | *** |
| **BMI (kg/m2)** | **-74.2945** | 36.2915 | ±72.5829 | **-2.047** | **0.0406** | * |
| Hypertension | -213.9367 | 513.2078 | ±1026.4155 | -0.417 | 0.6768 |  |
| High cholesterol | +60.6203 | 505.5785 | ±1011.1569 | +0.120 | 0.9046 |  |
| **Kidney disease** | **-1686.9359** | 522.8744 | ±1045.7489 | **-3.226** | **0.0013** | ** |
| **Circulatory disease** | **-1596.8934** | 506.8937 | ±1013.7875 | **-3.150** | **0.0016** | ** |
| Mean glucose (mg/dL) | +0.6974 | 6.1722 | ±12.3445 | +0.113 | 0.9100 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **472**, R² = **0.1966**, Adj R² = **0.1774**, F-statistic = **10.23** (p = **8.38e-17**), Residual SE = **4877.297** on **460** df, AIC = **9368.1**, BIC = **9418.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24640.6914** | 2668.6822 | ±5337.3643 | **+9.233** | **2.62e-20** | *** |
| Education: graduate level (vs college) | +490.8379 | 541.2748 | ±1082.5495 | +0.907 | 0.3645 |  |
| Education: high school or below (vs college) | +527.4510 | 660.9869 | ±1321.9737 | +0.798 | 0.4249 |  |
| Site: UCSD (vs UAB) | +342.3679 | 575.7320 | ±1151.4639 | +0.595 | 0.5521 |  |
| Site: UW (vs UAB) | -26.1578 | 575.6442 | ±1151.2885 | -0.045 | 0.9638 |  |
| **Age (years)** | **-191.6273** | 22.1867 | ±44.3733 | **-8.637** | **5.77e-18** | *** |
| **BMI (kg/m2)** | **-74.2945** | 36.2915 | ±72.5829 | **-2.047** | **0.0406** | * |
| Hypertension | -213.9367 | 513.2078 | ±1026.4155 | -0.417 | 0.6768 |  |
| High cholesterol | +60.6203 | 505.5785 | ±1011.1569 | +0.120 | 0.9046 |  |
| **Kidney disease** | **-1686.9359** | 522.8744 | ±1045.7489 | **-3.226** | **0.0013** | ** |
| **Circulatory disease** | **-1596.8934** | 506.8937 | ±1013.7875 | **-3.150** | **0.0016** | ** |
| GMI (%) | +29.1558 | 258.0369 | ±516.0738 | +0.113 | 0.9100 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **472**, R² = **0.1975**, Adj R² = **0.1783**, F-statistic = **10.29** (p = **6.59e-17**), Residual SE = **4874.524** on **460** df, AIC = **9367.6**, BIC = **9417.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24218.9790** | 2215.1590 | ±4430.3181 | **+10.933** | **7.99e-28** | *** |
| Education: graduate level (vs college) | +511.1832 | 542.6258 | ±1085.2516 | +0.942 | 0.3462 |  |
| Education: high school or below (vs college) | +493.8170 | 661.3536 | ±1322.7071 | +0.747 | 0.4553 |  |
| Site: UCSD (vs UAB) | +363.4905 | 574.1850 | ±1148.3700 | +0.633 | 0.5267 |  |
| Site: UW (vs UAB) | -19.9773 | 576.3492 | ±1152.6984 | -0.035 | 0.9723 |  |
| **Age (years)** | **-190.2390** | 22.1609 | ±44.3218 | **-8.584** | **9.13e-18** | *** |
| **BMI (kg/m2)** | **-77.6420** | 36.5020 | ±73.0041 | **-2.127** | **0.0334** | * |
| Hypertension | -211.3419 | 513.2093 | ±1026.4186 | -0.412 | 0.6805 |  |
| High cholesterol | +82.1271 | 506.9042 | ±1013.8085 | +0.162 | 0.8713 |  |
| **Kidney disease** | **-1679.5204** | 521.7854 | ±1043.5709 | **-3.219** | **0.0013** | ** |
| **Circulatory disease** | **-1620.0609** | 506.8653 | ±1013.7307 | **-3.196** | **0.0014** | ** |
| Nocturnal mean 00-06h (mg/dL) | +3.8768 | 6.1239 | ±12.2479 | +0.633 | 0.5267 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **472**, R² = **0.1967**, Adj R² = **0.1775**, F-statistic = **10.24** (p = **8.18e-17**), Residual SE = **4877.009** on **460** df, AIC = **9368.0**, BIC = **9417.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25052.7720** | 2123.5877 | ±4247.1754 | **+11.797** | **4.03e-32** | *** |
| Education: graduate level (vs college) | +479.6230 | 541.8128 | ±1083.6257 | +0.885 | 0.3760 |  |
| Education: high school or below (vs college) | +551.1204 | 663.0522 | ±1326.1044 | +0.831 | 0.4059 |  |
| Site: UCSD (vs UAB) | +328.6554 | 573.2123 | ±1146.4246 | +0.573 | 0.5664 |  |
| Site: UW (vs UAB) | -49.7659 | 574.5659 | ±1149.1318 | -0.087 | 0.9310 |  |
| **Age (years)** | **-191.8788** | 22.3423 | ±44.6847 | **-8.588** | **8.84e-18** | *** |
| **BMI (kg/m2)** | **-73.2712** | 36.1547 | ±72.3094 | **-2.027** | **0.0427** | * |
| Hypertension | -210.3977 | 514.1540 | ±1028.3079 | -0.409 | 0.6824 |  |
| High cholesterol | +50.2988 | 503.8650 | ±1007.7300 | +0.100 | 0.9205 |  |
| **Kidney disease** | **-1662.8579** | 532.7681 | ±1065.5361 | **-3.121** | **0.0018** | ** |
| **Circulatory disease** | **-1586.0967** | 508.4601 | ±1016.9203 | **-3.119** | **0.0018** | ** |
| Glucose SD, pooled (mg/dL) | -4.9546 | 20.0507 | ±40.1013 | -0.247 | 0.8048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **472**, R² = **0.1971**, Adj R² = **0.1779**, F-statistic = **10.26** (p = **7.42e-17**), Residual SE = **4875.899** on **460** df, AIC = **9367.8**, BIC = **9417.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25276.3620** | 2151.8218 | ±4303.6436 | **+11.746** | **7.36e-32** | *** |
| Education: graduate level (vs college) | +474.3909 | 539.8283 | ±1079.6567 | +0.879 | 0.3795 |  |
| Education: high school or below (vs college) | +573.5174 | 664.3306 | ±1328.6612 | +0.863 | 0.3880 |  |
| Site: UCSD (vs UAB) | +316.7143 | 572.9173 | ±1145.8345 | +0.553 | 0.5804 |  |
| Site: UW (vs UAB) | -66.6565 | 575.0616 | ±1150.1233 | -0.116 | 0.9077 |  |
| **Age (years)** | **-191.7849** | 22.3517 | ±44.7034 | **-8.580** | **9.46e-18** | *** |
| **BMI (kg/m2)** | **-73.6618** | 35.8988 | ±71.7977 | **-2.052** | **0.0402** | * |
| Hypertension | -210.6451 | 513.6065 | ±1027.2130 | -0.410 | 0.6817 |  |
| High cholesterol | +45.9295 | 502.4943 | ±1004.9887 | +0.091 | 0.9272 |  |
| **Kidney disease** | **-1634.2794** | 533.2022 | ±1066.4045 | **-3.065** | **0.0022** | ** |
| **Circulatory disease** | **-1582.4897** | 508.3294 | ±1016.6588 | **-3.113** | **0.0019** | ** |
| Avg. daily SD (mg/dL) | -11.3779 | 21.5799 | ±43.1599 | -0.527 | 0.5980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **472**, R² = **0.1979**, Adj R² = **0.1788**, F-statistic = **10.32** (p = **5.88e-17**), Residual SE = **4873.222** on **460** df, AIC = **9367.3**, BIC = **9417.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25708.4941** | 2223.5758 | ±4447.1517 | **+11.562** | **6.44e-31** | *** |
| Education: graduate level (vs college) | +474.9714 | 537.8134 | ±1075.6267 | +0.883 | 0.3772 |  |
| Education: high school or below (vs college) | +560.9847 | 674.8927 | ±1349.7855 | +0.831 | 0.4058 |  |
| Site: UCSD (vs UAB) | +316.3178 | 572.8769 | ±1145.7537 | +0.552 | 0.5808 |  |
| Site: UW (vs UAB) | -88.3409 | 579.4757 | ±1158.9514 | -0.152 | 0.8788 |  |
| **Age (years)** | **-190.9486** | 22.3465 | ±44.6930 | **-8.545** | **1.29e-17** | *** |
| **BMI (kg/m2)** | **-74.5347** | 35.6637 | ±71.3274 | **-2.090** | **0.0366** | * |
| Hypertension | -190.9760 | 513.9631 | ±1027.9261 | -0.372 | 0.7102 |  |
| High cholesterol | +50.4577 | 501.4311 | ±1002.8621 | +0.101 | 0.9198 |  |
| **Kidney disease** | **-1593.9241** | 526.4171 | ±1052.8342 | **-3.028** | **0.0025** | ** |
| **Circulatory disease** | **-1602.5226** | 505.9413 | ±1011.8827 | **-3.167** | **0.0015** | ** |
| CV (%) | -36.4406 | 38.3218 | ±76.6436 | -0.951 | 0.3417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **472**, R² = **0.1966**, Adj R² = **0.1774**, F-statistic = **10.23** (p = **8.42e-17**), Residual SE = **4877.347** on **460** df, AIC = **9368.1**, BIC = **9418.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24935.4062** | 2341.3200 | ±4682.6400 | **+10.650** | **1.74e-26** | *** |
| Education: graduate level (vs college) | +488.6715 | 537.4979 | ±1074.9957 | +0.909 | 0.3633 |  |
| Education: high school or below (vs college) | +533.0363 | 676.7142 | ±1353.4283 | +0.788 | 0.4309 |  |
| Site: UCSD (vs UAB) | +339.1553 | 574.9922 | ±1149.9844 | +0.590 | 0.5553 |  |
| Site: UW (vs UAB) | -26.0772 | 576.7979 | ±1153.5958 | -0.045 | 0.9639 |  |
| **Age (years)** | **-191.8511** | 22.3720 | ±44.7440 | **-8.576** | **9.87e-18** | *** |
| **BMI (kg/m2)** | **-73.7238** | 35.9372 | ±71.8744 | **-2.051** | **0.0402** | * |
| Hypertension | -215.5875 | 513.7061 | ±1027.4121 | -0.420 | 0.6747 |  |
| High cholesterol | +56.5940 | 501.7317 | ±1003.4634 | +0.113 | 0.9102 |  |
| **Kidney disease** | **-1692.9940** | 525.6472 | ±1051.2943 | **-3.221** | **0.0013** | ** |
| **Circulatory disease** | **-1592.3263** | 506.3200 | ±1012.6399 | **-3.145** | **0.0017** | ** |
| Mean / SD ratio | -18.0897 | 206.7329 | ±413.4658 | -0.088 | 0.9303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **472**, R² = **0.1966**, Adj R² = **0.1774**, F-statistic = **10.24** (p = **8.27e-17**), Residual SE = **4877.137** on **460** df, AIC = **9368.1**, BIC = **9418.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25052.1438** | 2266.0598 | ±4532.1196 | **+11.055** | **2.06e-28** | *** |
| Education: graduate level (vs college) | +490.8290 | 535.9536 | ±1071.9073 | +0.916 | 0.3598 |  |
| Education: high school or below (vs college) | +529.4317 | 678.4491 | ±1356.8983 | +0.780 | 0.4352 |  |
| Site: UCSD (vs UAB) | +340.5606 | 575.1998 | ±1150.3995 | +0.592 | 0.5538 |  |
| Site: UW (vs UAB) | -21.4711 | 576.1889 | ±1152.3777 | -0.037 | 0.9703 |  |
| **Age (years)** | **-192.0338** | 22.3537 | ±44.7074 | **-8.591** | **8.65e-18** | *** |
| **BMI (kg/m2)** | **-73.1172** | 35.9473 | ±71.8945 | **-2.034** | **0.0420** | * |
| Hypertension | -216.8175 | 513.1376 | ±1026.2752 | -0.423 | 0.6726 |  |
| High cholesterol | +55.9260 | 501.1922 | ±1002.3844 | +0.112 | 0.9112 |  |
| **Kidney disease** | **-1703.3793** | 523.5691 | ±1047.1383 | **-3.253** | **0.0011** | ** |
| **Circulatory disease** | **-1590.1595** | 505.8402 | ±1011.6804 | **-3.144** | **0.0017** | ** |
| Avg. daily mean/SD | -39.7600 | 163.2009 | ±326.4018 | -0.244 | 0.8075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **472**, R² = **0.2008**, Adj R² = **0.1817**, F-statistic = **10.51** (p = **2.72e-17**), Residual SE = **4864.397** on **460** df, AIC = **9365.6**, BIC = **9415.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22887.6926** | 2374.2988 | ±4748.5975 | **+9.640** | **5.43e-22** | *** |
| Education: graduate level (vs college) | +538.4126 | 536.7123 | ±1073.4246 | +1.003 | 0.3158 |  |
| Education: high school or below (vs college) | +476.2087 | 667.6142 | ±1335.2283 | +0.713 | 0.4757 |  |
| Site: UCSD (vs UAB) | +419.1568 | 580.9594 | ±1161.9189 | +0.721 | 0.4706 |  |
| Site: UW (vs UAB) | +103.2652 | 576.1255 | ±1152.2510 | +0.179 | 0.8577 |  |
| **Age (years)** | **-188.2987** | 22.0414 | ±44.0829 | **-8.543** | **1.31e-17** | *** |
| **BMI (kg/m2)** | **-72.7218** | 36.0468 | ±72.0935 | **-2.017** | **0.0437** | * |
| Hypertension | -220.8093 | 514.0453 | ±1028.0905 | -0.430 | 0.6675 |  |
| High cholesterol | +80.2234 | 503.8692 | ±1007.7383 | +0.159 | 0.8735 |  |
| **Kidney disease** | **-1773.8427** | 526.8181 | ±1053.6361 | **-3.367** | **7.60e-04** | *** |
| **Circulatory disease** | **-1610.6189** | 505.9266 | ±1011.8532 | **-3.184** | **0.0015** | ** |
| MAG (mg/dL/h) | +36.1214 | 26.2193 | ±52.4386 | +1.378 | 0.1683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **472**, R² = **0.1967**, Adj R² = **0.1775**, F-statistic = **10.24** (p = **8.24e-17**), Residual SE = **4877.095** on **460** df, AIC = **9368.1**, BIC = **9417.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25110.9771** | 2279.5387 | ±4559.0773 | **+11.016** | **3.21e-28** | *** |
| Education: graduate level (vs college) | +482.1776 | 538.9272 | ±1077.8545 | +0.895 | 0.3709 |  |
| Education: high school or below (vs college) | +552.3919 | 665.7120 | ±1331.4240 | +0.830 | 0.4067 |  |
| Site: UCSD (vs UAB) | +327.3399 | 573.7980 | ±1147.5961 | +0.570 | 0.5684 |  |
| Site: UW (vs UAB) | -46.3970 | 576.7245 | ±1153.4489 | -0.080 | 0.9359 |  |
| **Age (years)** | **-192.0004** | 22.3361 | ±44.6722 | **-8.596** | **8.26e-18** | *** |
| **BMI (kg/m2)** | **-73.9462** | 35.9457 | ±71.8914 | **-2.057** | **0.0397** | * |
| Hypertension | -215.4750 | 512.9893 | ±1025.9785 | -0.420 | 0.6745 |  |
| High cholesterol | +54.7009 | 501.7339 | ±1003.4678 | +0.109 | 0.9132 |  |
| **Kidney disease** | **-1661.1369** | 532.2009 | ±1064.4019 | **-3.121** | **0.0018** | ** |
| **Circulatory disease** | **-1587.6197** | 507.3135 | ±1014.6271 | **-3.129** | **0.0018** | ** |
| Avg. daily range (mg/dL) | -1.4794 | 6.3850 | ±12.7701 | -0.232 | 0.8168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **472**, R² = **0.1982**, Adj R² = **0.1790**, F-statistic = **10.34** (p = **5.51e-17**), Residual SE = **4872.467** on **460** df, AIC = **9367.2**, BIC = **9417.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24471.2344** | 2066.5902 | ±4133.1804 | **+11.841** | **2.39e-32** | *** |
| Education: graduate level (vs college) | +526.1227 | 548.2164 | ±1096.4328 | +0.960 | 0.3372 |  |
| Education: high school or below (vs college) | +520.6946 | 670.8157 | ±1341.6314 | +0.776 | 0.4376 |  |
| Site: UCSD (vs UAB) | +349.8111 | 575.9623 | ±1151.9245 | +0.607 | 0.5436 |  |
| Site: UW (vs UAB) | +21.5932 | 575.0096 | ±1150.0192 | +0.038 | 0.9700 |  |
| **Age (years)** | **-189.8566** | 22.0593 | ±44.1187 | **-8.607** | **7.52e-18** | *** |
| **BMI (kg/m2)** | **-77.7818** | 36.5201 | ±73.0403 | **-2.130** | **0.0332** | * |
| Hypertension | -250.2581 | 514.8015 | ±1029.6030 | -0.486 | 0.6269 |  |
| High cholesterol | +88.8973 | 503.6034 | ±1007.2068 | +0.177 | 0.8599 |  |
| **Kidney disease** | **-1704.7346** | 523.7186 | ±1047.4372 | **-3.255** | **0.0011** | ** |
| **Circulatory disease** | **-1640.0796** | 510.6499 | ±1021.2998 | **-3.212** | **0.0013** | ** |
| SD of daily means (mg/dL) | +25.4993 | 29.9583 | ±59.9165 | +0.851 | 0.3947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **472**, R² = **0.1967**, Adj R² = **0.1775**, F-statistic = **10.24** (p = **8.15e-17**), Residual SE = **4876.968** on **460** df, AIC = **9368.0**, BIC = **9417.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25033.7301** | 2232.4568 | ±4464.9136 | **+11.214** | **3.50e-29** | *** |
| Education: graduate level (vs college) | +493.6082 | 540.5579 | ±1081.1158 | +0.913 | 0.3612 |  |
| Education: high school or below (vs college) | +517.1435 | 658.9473 | ±1317.8946 | +0.785 | 0.4326 |  |
| Site: UCSD (vs UAB) | +350.5883 | 576.2462 | ±1152.4923 | +0.608 | 0.5429 |  |
| Site: UW (vs UAB) | -20.3446 | 576.7102 | ±1153.4203 | -0.035 | 0.9719 |  |
| **Age (years)** | **-191.5999** | 22.2928 | ±44.5855 | **-8.595** | **8.35e-18** | *** |
| **BMI (kg/m2)** | **-75.0602** | 36.1595 | ±72.3190 | **-2.076** | **0.0379** | * |
| Hypertension | -212.0918 | 513.0459 | ±1026.0918 | -0.413 | 0.6793 |  |
| High cholesterol | +68.2545 | 506.0960 | ±1012.1921 | +0.135 | 0.8927 |  |
| **Kidney disease** | **-1689.9793** | 524.0556 | ±1048.1112 | **-3.225** | **0.0013** | ** |
| **Circulatory disease** | **-1602.9568** | 504.2986 | ±1008.5973 | **-3.179** | **0.0015** | ** |
| Time in range 70-180, pooled (%) | -2.4992 | 9.8571 | ±19.7142 | -0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **472**, R² = **0.1967**, Adj R² = **0.1775**, F-statistic = **10.24** (p = **8.14e-17**), Residual SE = **4876.956** on **460** df, AIC = **9368.0**, BIC = **9417.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25038.4238** | 2234.1587 | ±4468.3173 | **+11.207** | **3.76e-29** | *** |
| Education: graduate level (vs college) | +492.9544 | 540.1703 | ±1080.3406 | +0.913 | 0.3615 |  |
| Education: high school or below (vs college) | +515.9629 | 657.8218 | ±1315.6436 | +0.784 | 0.4328 |  |
| Site: UCSD (vs UAB) | +351.7427 | 576.1781 | ±1152.3561 | +0.610 | 0.5415 |  |
| Site: UW (vs UAB) | -20.0393 | 576.4228 | ±1152.8457 | -0.035 | 0.9723 |  |
| **Age (years)** | **-191.6337** | 22.3020 | ±44.6040 | **-8.593** | **8.50e-18** | *** |
| **BMI (kg/m2)** | **-75.1004** | 36.1770 | ±72.3539 | **-2.076** | **0.0379** | * |
| Hypertension | -211.5730 | 513.0393 | ±1026.0786 | -0.412 | 0.6801 |  |
| High cholesterol | +68.1627 | 506.1891 | ±1012.3782 | +0.135 | 0.8929 |  |
| **Kidney disease** | **-1691.1719** | 524.5761 | ±1049.1522 | **-3.224** | **0.0013** | ** |
| **Circulatory disease** | **-1602.9333** | 504.5241 | ±1009.0482 | **-3.177** | **0.0015** | ** |
| Avg. daily time in range 70-180 (%) | -2.5129 | 9.7296 | ±19.4593 | -0.258 | 0.7962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **472**, R² = **0.2016**, Adj R² = **0.1825**, F-statistic = **10.56** (p = **2.20e-17**), Residual SE = **4861.974** on **460** df, AIC = **9365.1**, BIC = **9415.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25208.1120** | 2086.9314 | ±4173.8628 | **+12.079** | **1.36e-33** | *** |
| Education: graduate level (vs college) | +482.5402 | 536.2380 | ±1072.4761 | +0.900 | 0.3682 |  |
| Education: high school or below (vs college) | +501.9026 | 671.8134 | ±1343.6268 | +0.747 | 0.4550 |  |
| Site: UCSD (vs UAB) | +268.8560 | 579.3246 | ±1158.6493 | +0.464 | 0.6426 |  |
| Site: UW (vs UAB) | -75.3573 | 580.0214 | ±1160.0427 | -0.130 | 0.8966 |  |
| **Age (years)** | **-193.6459** | 22.3793 | ±44.7586 | **-8.653** | **5.02e-18** | *** |
| **BMI (kg/m2)** | **-74.8774** | 36.2154 | ±72.4307 | **-2.068** | **0.0387** | * |
| Hypertension | -149.0226 | 518.2242 | ±1036.4484 | -0.288 | 0.7737 |  |
| High cholesterol | +30.7080 | 500.2047 | ±1000.4094 | +0.061 | 0.9510 |  |
| **Kidney disease** | **-1682.4165** | 523.5731 | ±1047.1462 | **-3.213** | **0.0013** | ** |
| **Circulatory disease** | **-1534.5012** | 507.0351 | ±1014.0702 | **-3.026** | **0.0025** | ** |
| Any reading < 54 during wear (0/1) | -930.8223 | 567.7548 | ±1135.5097 | -1.639 | 0.1011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **472**, R² = **0.2030**, Adj R² = **0.1840**, F-statistic = **10.65** (p = **1.51e-17**), Residual SE = **4857.687** on **460** df, AIC = **9364.3**, BIC = **9414.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24992.3275** | 2072.3007 | ±4144.6015 | **+12.060** | **1.71e-33** | *** |
| Education: graduate level (vs college) | +442.9991 | 535.3685 | ±1070.7370 | +0.827 | 0.4080 |  |
| Education: high school or below (vs college) | +462.2141 | 673.8487 | ±1347.6973 | +0.686 | 0.4928 |  |
| Site: UCSD (vs UAB) | +248.7230 | 575.9567 | ±1151.9134 | +0.432 | 0.6659 |  |
| Site: UW (vs UAB) | -152.0790 | 581.8127 | ±1163.6254 | -0.261 | 0.7938 |  |
| **Age (years)** | **-190.9346** | 22.2600 | ±44.5200 | **-8.577** | **9.70e-18** | *** |
| **BMI (kg/m2)** | **-73.9339** | 35.8262 | ±71.6525 | **-2.064** | **0.0390** | * |
| Hypertension | -94.5576 | 512.3875 | ±1024.7751 | -0.185 | 0.8536 |  |
| High cholesterol | -21.1480 | 498.3698 | ±996.7395 | -0.042 | 0.9662 |  |
| **Kidney disease** | **-1676.1717** | 520.2173 | ±1040.4347 | **-3.222** | **0.0013** | ** |
| **Circulatory disease** | **-1676.0414** | 506.0715 | ±1012.1429 | **-3.312** | **9.27e-04** | *** |
| **Time < 54 (%)** | **-1642.8202** | 486.2399 | ±972.4798 | **-3.379** | **7.29e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **472**, R² = **0.2020**, Adj R² = **0.1829**, F-statistic = **10.58** (p = **2.02e-17**), Residual SE = **4861.000** on **460** df, AIC = **9364.9**, BIC = **9414.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24918.9921** | 2070.6937 | ±4141.3873 | **+12.034** | **2.35e-33** | *** |
| Education: graduate level (vs college) | +459.5687 | 536.3437 | ±1072.6873 | +0.857 | 0.3915 |  |
| Education: high school or below (vs college) | +476.7803 | 674.4462 | ±1348.8923 | +0.707 | 0.4796 |  |
| Site: UCSD (vs UAB) | +273.8240 | 575.9194 | ±1151.8389 | +0.475 | 0.6345 |  |
| Site: UW (vs UAB) | -118.4147 | 579.1015 | ±1158.2031 | -0.204 | 0.8380 |  |
| **Age (years)** | **-191.4210** | 22.3045 | ±44.6089 | **-8.582** | **9.31e-18** | *** |
| **BMI (kg/m2)** | **-72.8590** | 35.8053 | ±71.6105 | **-2.035** | **0.0419** | * |
| Hypertension | -137.2236 | 512.7578 | ±1025.5156 | -0.268 | 0.7890 |  |
| High cholesterol | -6.8353 | 499.2560 | ±998.5119 | -0.014 | 0.9891 |  |
| **Kidney disease** | **-1660.5171** | 519.7564 | ±1039.5128 | **-3.195** | **0.0014** | ** |
| **Circulatory disease** | **-1643.7037** | 506.0519 | ±1012.1038 | **-3.248** | **0.0012** | ** |
| **Avg. daily time < 54 (%)** | **-1074.2954** | 227.1004 | ±454.2009 | **-4.730** | **2.24e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **472**, R² = **0.2025**, Adj R² = **0.1834**, F-statistic = **10.62** (p = **1.77e-17**), Residual SE = **4859.458** on **460** df, AIC = **9364.6**, BIC = **9414.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25029.4470** | 2059.4526 | ±4118.9052 | **+12.153** | **5.50e-34** | *** |
| Education: graduate level (vs college) | +433.3787 | 533.0507 | ±1066.1015 | +0.813 | 0.4162 |  |
| Education: high school or below (vs college) | +514.1001 | 673.6914 | ±1347.3828 | +0.763 | 0.4454 |  |
| Site: UCSD (vs UAB) | +222.3543 | 571.0100 | ±1142.0200 | +0.389 | 0.6970 |  |
| Site: UW (vs UAB) | -156.3763 | 578.3763 | ±1156.7527 | -0.270 | 0.7869 |  |
| **Age (years)** | **-189.3162** | 22.2675 | ±44.5351 | **-8.502** | **1.87e-17** | *** |
| **BMI (kg/m2)** | **-76.1642** | 35.6796 | ±71.3593 | **-2.135** | **0.0328** | * |
| Hypertension | -126.4062 | 504.5471 | ±1009.0943 | -0.251 | 0.8022 |  |
| High cholesterol | -28.1995 | 495.7320 | ±991.4640 | -0.057 | 0.9546 |  |
| **Kidney disease** | **-1671.8230** | 521.3893 | ±1042.7785 | **-3.206** | **0.0013** | ** |
| **Circulatory disease** | **-1690.2115** | 505.8468 | ±1011.6935 | **-3.341** | **8.34e-04** | *** |
| Time 54-69, pooled (%) | -477.2339 | 290.5960 | ±581.1921 | -1.642 | 0.1005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **472**, R² = **0.2036**, Adj R² = **0.1846**, F-statistic = **10.69** (p = **1.30e-17**), Residual SE = **4855.968** on **460** df, AIC = **9364.0**, BIC = **9413.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24973.3618** | 2062.3022 | ±4124.6044 | **+12.109** | **9.41e-34** | *** |
| Education: graduate level (vs college) | +433.3511 | 533.5813 | ±1067.1626 | +0.812 | 0.4167 |  |
| Education: high school or below (vs college) | +505.5020 | 671.1381 | ±1342.2763 | +0.753 | 0.4513 |  |
| Site: UCSD (vs UAB) | +215.8312 | 572.3741 | ±1144.7482 | +0.377 | 0.7061 |  |
| Site: UW (vs UAB) | -168.9019 | 579.6447 | ±1159.2895 | -0.291 | 0.7708 |  |
| **Age (years)** | **-189.0249** | 22.2304 | ±44.4608 | **-8.503** | **1.85e-17** | *** |
| **BMI (kg/m2)** | **-75.1794** | 35.7678 | ±71.5357 | **-2.102** | **0.0356** | * |
| Hypertension | -117.1512 | 505.7275 | ±1011.4550 | -0.232 | 0.8168 |  |
| High cholesterol | -33.0514 | 494.8005 | ±989.6010 | -0.067 | 0.9467 |  |
| **Kidney disease** | **-1663.9340** | 521.3611 | ±1042.7222 | **-3.192** | **0.0014** | ** |
| **Circulatory disease** | **-1690.9213** | 506.5594 | ±1013.1188 | **-3.338** | **8.44e-04** | *** |
| Avg. daily time 54-69 (%) | -473.4001 | 247.2760 | ±494.5520 | -1.914 | 0.0556 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **472**, R² = **0.2036**, Adj R² = **0.1846**, F-statistic = **10.69** (p = **1.30e-17**), Residual SE = **4855.973** on **460** df, AIC = **9364.0**, BIC = **9413.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25048.7959** | 2060.5316 | ±4121.0633 | **+12.156** | **5.30e-34** | *** |
| Education: graduate level (vs college) | +426.8194 | 533.1013 | ±1066.2027 | +0.801 | 0.4233 |  |
| Education: high school or below (vs college) | +496.9844 | 672.9455 | ±1345.8910 | +0.739 | 0.4602 |  |
| Site: UCSD (vs UAB) | +209.7743 | 571.9109 | ±1143.8218 | +0.367 | 0.7138 |  |
| Site: UW (vs UAB) | -176.4648 | 579.6736 | ±1159.3473 | -0.304 | 0.7608 |  |
| **Age (years)** | **-189.3240** | 22.2423 | ±44.4845 | **-8.512** | **1.71e-17** | *** |
| **BMI (kg/m2)** | **-75.9694** | 35.7018 | ±71.4036 | **-2.128** | **0.0333** | * |
| Hypertension | -103.2754 | 504.8330 | ±1009.6660 | -0.205 | 0.8379 |  |
| High cholesterol | -40.7286 | 495.6622 | ±991.3244 | -0.082 | 0.9345 |  |
| **Kidney disease** | **-1670.6051** | 520.9169 | ±1041.8338 | **-3.207** | **0.0013** | ** |
| **Circulatory disease** | **-1702.9630** | 505.9775 | ±1011.9549 | **-3.366** | **7.64e-04** | *** |
| **Time < 70 (%)** | **-431.9765** | 217.7740 | ±435.5481 | **-1.984** | **0.0473** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **472**, R² = **0.2043**, Adj R² = **0.1853**, F-statistic = **10.74** (p = **1.08e-17**), Residual SE = **4853.848** on **460** df, AIC = **9363.5**, BIC = **9413.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24975.1865** | 2063.1898 | ±4126.3796 | **+12.105** | **9.92e-34** | *** |
| Education: graduate level (vs college) | +432.9048 | 534.1945 | ±1068.3889 | +0.810 | 0.4177 |  |
| Education: high school or below (vs college) | +489.7272 | 670.9468 | ±1341.8936 | +0.730 | 0.4654 |  |
| Site: UCSD (vs UAB) | +214.3022 | 573.3932 | ±1146.7863 | +0.374 | 0.7086 |  |
| Site: UW (vs UAB) | -176.1149 | 579.8553 | ±1159.7106 | -0.304 | 0.7613 |  |
| **Age (years)** | **-189.3823** | 22.2156 | ±44.4313 | **-8.525** | **1.53e-17** | *** |
| **BMI (kg/m2)** | **-74.5864** | 35.7684 | ±71.5368 | **-2.085** | **0.0370** | * |
| Hypertension | -106.5898 | 507.1787 | ±1014.3574 | -0.210 | 0.8335 |  |
| High cholesterol | -40.1715 | 495.6516 | ±991.3032 | -0.081 | 0.9354 |  |
| **Kidney disease** | **-1658.6663** | 520.5809 | ±1041.1618 | **-3.186** | **0.0014** | ** |
| **Circulatory disease** | **-1691.9650** | 506.3475 | ±1012.6949 | **-3.342** | **8.33e-04** | *** |
| **Avg. daily time < 70 (%)** | **-388.9792** | 150.5993 | ±301.1986 | **-2.583** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **472**, R² = **0.1971**, Adj R² = **0.1779**, F-statistic = **10.27** (p = **7.32e-17**), Residual SE = **4875.736** on **460** df, AIC = **9367.8**, BIC = **9417.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24273.6521** | 2515.2406 | ±5030.4812 | **+9.651** | **4.89e-22** | *** |
| Education: graduate level (vs college) | +462.1670 | 545.6693 | ±1091.3387 | +0.847 | 0.3970 |  |
| Education: high school or below (vs college) | +562.7770 | 663.0492 | ±1326.0983 | +0.849 | 0.3960 |  |
| Site: UCSD (vs UAB) | +324.2654 | 573.3087 | ±1146.6174 | +0.566 | 0.5717 |  |
| Site: UW (vs UAB) | -60.7133 | 575.5717 | ±1151.1435 | -0.105 | 0.9160 |  |
| **Age (years)** | **-193.0328** | 22.0859 | ±44.1717 | **-8.740** | **2.33e-18** | *** |
| **BMI (kg/m2)** | **-72.2562** | 36.2766 | ±72.5533 | **-1.992** | **0.0464** | * |
| Hypertension | -202.4291 | 512.9726 | ±1025.9453 | -0.395 | 0.6931 |  |
| High cholesterol | +43.6911 | 504.7269 | ±1009.4539 | +0.087 | 0.9310 |  |
| **Kidney disease** | **-1673.1374** | 523.8636 | ±1047.7272 | **-3.194** | **0.0014** | ** |
| **Circulatory disease** | **-1579.3541** | 508.4572 | ±1016.9145 | **-3.106** | **0.0019** | ** |
| Time 54-250, pooled (%) | +6.9636 | 14.0026 | ±28.0051 | +0.497 | 0.6190 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **472**, R² = **0.1970**, Adj R² = **0.1778**, F-statistic = **10.26** (p = **7.59e-17**), Residual SE = **4876.147** on **460** df, AIC = **9367.9**, BIC = **9417.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24334.4784** | 2498.5598 | ±4997.1197 | **+9.739** | **2.05e-22** | *** |
| Education: graduate level (vs college) | +465.8921 | 545.7944 | ±1091.5887 | +0.854 | 0.3933 |  |
| Education: high school or below (vs college) | +558.7820 | 663.8004 | ±1327.6007 | +0.842 | 0.3999 |  |
| Site: UCSD (vs UAB) | +325.5173 | 573.5413 | ±1147.0825 | +0.568 | 0.5703 |  |
| Site: UW (vs UAB) | -55.9095 | 575.5585 | ±1151.1170 | -0.097 | 0.9226 |  |
| **Age (years)** | **-192.7364** | 22.1238 | ±44.2477 | **-8.712** | **2.99e-18** | *** |
| **BMI (kg/m2)** | **-72.4278** | 36.2322 | ±72.4644 | **-1.999** | **0.0456** | * |
| Hypertension | -204.8821 | 513.2260 | ±1026.4520 | -0.399 | 0.6897 |  |
| High cholesterol | +45.4245 | 504.6200 | ±1009.2399 | +0.090 | 0.9283 |  |
| **Kidney disease** | **-1672.7643** | 524.4235 | ±1048.8471 | **-3.190** | **0.0014** | ** |
| **Circulatory disease** | **-1579.8739** | 508.1911 | ±1016.3821 | **-3.109** | **0.0019** | ** |
| Avg. daily time 54-250 (%) | +6.0962 | 13.5566 | ±27.1133 | +0.450 | 0.6529 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **472**, R² = **0.1995**, Adj R² = **0.1803**, F-statistic = **10.42** (p = **3.93e-17**), Residual SE = **4868.588** on **460** df, AIC = **9366.4**, BIC = **9416.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24609.6743** | 2094.0659 | ±4188.1319 | **+11.752** | **6.89e-32** | *** |
| Education: graduate level (vs college) | +461.8852 | 534.2312 | ±1068.4624 | +0.865 | 0.3873 |  |
| Education: high school or below (vs college) | +473.3231 | 668.8240 | ±1337.6481 | +0.708 | 0.4791 |  |
| Site: UCSD (vs UAB) | +390.3034 | 577.9499 | ±1155.8998 | +0.675 | 0.4995 |  |
| Site: UW (vs UAB) | -44.6537 | 577.7453 | ±1155.4907 | -0.077 | 0.9384 |  |
| **Age (years)** | **-193.6267** | 22.3699 | ±44.7398 | **-8.656** | **4.90e-18** | *** |
| **BMI (kg/m2)** | **-79.2174** | 35.6857 | ±71.3714 | **-2.220** | **0.0264** | * |
| Hypertension | -159.9374 | 509.2703 | ±1018.5406 | -0.314 | 0.7535 |  |
| High cholesterol | +101.8159 | 501.0360 | ±1002.0721 | +0.203 | 0.8390 |  |
| **Kidney disease** | **-1681.6021** | 521.5228 | ±1043.0456 | **-3.224** | **0.0013** | ** |
| **Circulatory disease** | **-1645.5991** | 500.0285 | ±1000.0571 | **-3.291** | **9.98e-04** | *** |
| Time 181-250, pooled (%) | +20.0349 | 15.3850 | ±30.7699 | +1.302 | 0.1928 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **472**, R² = **0.1991**, Adj R² = **0.1799**, F-statistic = **10.39** (p = **4.37e-17**), Residual SE = **4869.806** on **460** df, AIC = **9366.6**, BIC = **9416.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24621.9688** | 2091.4368 | ±4182.8737 | **+11.773** | **5.39e-32** | *** |
| Education: graduate level (vs college) | +460.9452 | 534.6779 | ±1069.3558 | +0.862 | 0.3886 |  |
| Education: high school or below (vs college) | +469.2471 | 665.1577 | ±1330.3153 | +0.705 | 0.4805 |  |
| Site: UCSD (vs UAB) | +391.6210 | 578.1336 | ±1156.2672 | +0.677 | 0.4982 |  |
| Site: UW (vs UAB) | -39.0483 | 577.9000 | ±1155.8000 | -0.068 | 0.9461 |  |
| **Age (years)** | **-193.2734** | 22.3834 | ±44.7668 | **-8.635** | **5.89e-18** | *** |
| **BMI (kg/m2)** | **-78.8560** | 35.8252 | ±71.6503 | **-2.201** | **0.0277** | * |
| Hypertension | -163.7935 | 510.7680 | ±1021.5360 | -0.321 | 0.7485 |  |
| High cholesterol | +96.5316 | 501.9985 | ±1003.9969 | +0.192 | 0.8475 |  |
| **Kidney disease** | **-1684.3101** | 521.8061 | ±1043.6122 | **-3.228** | **0.0012** | ** |
| **Circulatory disease** | **-1636.9495** | 501.5141 | ±1003.0283 | **-3.264** | **0.0011** | ** |
| Avg. daily time 181-250 (%) | +18.2029 | 15.0436 | ±30.0872 | +1.210 | 0.2263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **472**, R² = **0.1968**, Adj R² = **0.1776**, F-statistic = **10.25** (p = **7.96e-17**), Residual SE = **4876.693** on **460** df, AIC = **9368.0**, BIC = **9417.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24764.8599** | 2081.3041 | ±4162.6082 | **+11.899** | **1.20e-32** | *** |
| Education: graduate level (vs college) | +494.8927 | 540.2005 | ±1080.4010 | +0.916 | 0.3596 |  |
| Education: high school or below (vs college) | +511.9112 | 658.8485 | ±1317.6971 | +0.777 | 0.4372 |  |
| Site: UCSD (vs UAB) | +353.0545 | 576.1950 | ±1152.3900 | +0.613 | 0.5401 |  |
| Site: UW (vs UAB) | -18.6684 | 576.7111 | ±1153.4221 | -0.032 | 0.9742 |  |
| **Age (years)** | **-191.5249** | 22.2863 | ±44.5727 | **-8.594** | **8.41e-18** | *** |
| **BMI (kg/m2)** | **-75.4207** | 36.1378 | ±72.2756 | **-2.087** | **0.0369** | * |
| Hypertension | -210.6823 | 512.9239 | ±1025.8478 | -0.411 | 0.6813 |  |
| High cholesterol | +70.5920 | 505.9591 | ±1011.9182 | +0.140 | 0.8890 |  |
| **Kidney disease** | **-1691.0220** | 524.0432 | ±1048.0864 | **-3.227** | **0.0013** | ** |
| **Circulatory disease** | **-1606.8029** | 504.0849 | ±1008.1699 | **-3.188** | **0.0014** | ** |
| Time > 180 (%) | +3.2019 | 9.7710 | ±19.5420 | +0.328 | 0.7431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **472**, R² = **0.1968**, Adj R² = **0.1776**, F-statistic = **10.25** (p = **7.90e-17**), Residual SE = **4876.608** on **460** df, AIC = **9368.0**, BIC = **9417.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24764.5448** | 2080.1460 | ±4160.2920 | **+11.905** | **1.11e-32** | *** |
| Education: graduate level (vs college) | +494.3642 | 539.8089 | ±1079.6179 | +0.916 | 0.3598 |  |
| Education: high school or below (vs college) | +509.1554 | 657.5172 | ±1315.0343 | +0.774 | 0.4387 |  |
| Site: UCSD (vs UAB) | +355.2141 | 576.1175 | ±1152.2351 | +0.617 | 0.5375 |  |
| Site: UW (vs UAB) | -17.8474 | 576.4496 | ±1152.8991 | -0.031 | 0.9753 |  |
| **Age (years)** | **-191.5555** | 22.2940 | ±44.5881 | **-8.592** | **8.53e-18** | *** |
| **BMI (kg/m2)** | **-75.5392** | 36.1590 | ±72.3180 | **-2.089** | **0.0367** | * |
| Hypertension | -209.7500 | 512.9214 | ±1025.8428 | -0.409 | 0.6826 |  |
| High cholesterol | +71.0077 | 506.0897 | ±1012.1794 | +0.140 | 0.8884 |  |
| **Kidney disease** | **-1692.7470** | 524.5375 | ±1049.0750 | **-3.227** | **0.0013** | ** |
| **Circulatory disease** | **-1607.4636** | 504.3216 | ±1008.6433 | **-3.187** | **0.0014** | ** |
| Avg. daily time > 180 (%) | +3.3710 | 9.6673 | ±19.3345 | +0.349 | 0.7273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **472**, R² = **0.1974**, Adj R² = **0.1782**, F-statistic = **10.29** (p = **6.75e-17**), Residual SE = **4874.807** on **460** df, AIC = **9367.6**, BIC = **9417.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24729.4822** | 2083.2914 | ±4166.5828 | **+11.870** | **1.69e-32** | *** |
| Education: graduate level (vs college) | +510.8817 | 543.7700 | ±1087.5399 | +0.940 | 0.3475 |  |
| Education: high school or below (vs college) | +495.5909 | 660.9264 | ±1321.8527 | +0.750 | 0.4533 |  |
| Site: UCSD (vs UAB) | +369.2364 | 573.7652 | ±1147.5304 | +0.644 | 0.5199 |  |
| Site: UW (vs UAB) | -15.9764 | 576.5084 | ±1153.0167 | -0.028 | 0.9779 |  |
| **Age (years)** | **-190.6542** | 22.2925 | ±44.5850 | **-8.552** | **1.21e-17** | *** |
| **BMI (kg/m2)** | **-78.0125** | 36.1924 | ±72.3849 | **-2.155** | **0.0311** | * |
| Hypertension | -212.1486 | 513.1577 | ±1026.3154 | -0.413 | 0.6793 |  |
| High cholesterol | +93.0011 | 508.1024 | ±1016.2048 | +0.183 | 0.8548 |  |
| **Kidney disease** | **-1691.5252** | 524.2558 | ±1048.5116 | **-3.227** | **0.0013** | ** |
| **Circulatory disease** | **-1620.9812** | 503.7826 | ±1007.5652 | **-3.218** | **0.0013** | ** |
| Nocturnal time > 180 (%) | +5.5033 | 8.7955 | ±17.5911 | +0.626 | 0.5315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **472**, R² = **0.1971**, Adj R² = **0.1779**, F-statistic = **10.26** (p = **7.42e-17**), Residual SE = **4875.899** on **460** df, AIC = **9367.8**, BIC = **9417.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24963.6552** | 2063.7254 | ±4127.4508 | **+12.096** | **1.10e-33** | *** |
| Education: graduate level (vs college) | +463.6367 | 545.5757 | ±1091.1514 | +0.850 | 0.3954 |  |
| Education: high school or below (vs college) | +561.6375 | 662.8904 | ±1325.7807 | +0.847 | 0.3969 |  |
| Site: UCSD (vs UAB) | +325.3496 | 573.3751 | ±1146.7501 | +0.567 | 0.5704 |  |
| Site: UW (vs UAB) | -58.6624 | 575.5419 | ±1151.0839 | -0.102 | 0.9188 |  |
| **Age (years)** | **-192.9734** | 22.0841 | ±44.1683 | **-8.738** | **2.37e-18** | *** |
| **BMI (kg/m2)** | **-72.3365** | 36.2774 | ±72.5548 | **-1.994** | **0.0462** | * |
| Hypertension | -203.5105 | 512.9798 | ±1025.9595 | -0.397 | 0.6916 |  |
| High cholesterol | +44.7048 | 504.6722 | ±1009.3444 | +0.089 | 0.9294 |  |
| **Kidney disease** | **-1673.8267** | 523.8958 | ±1047.7915 | **-3.195** | **0.0014** | ** |
| **Circulatory disease** | **-1579.6729** | 508.4246 | ±1016.8491 | **-3.107** | **0.0019** | ** |
| Time > 250 (%) | -6.6079 | 14.0086 | ±28.0172 | -0.472 | 0.6371 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 472)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **472**, R² = **0.1969**, Adj R² = **0.1777**, F-statistic = **10.25** (p = **7.71e-17**), Residual SE = **4876.326** on **460** df, AIC = **9367.9**, BIC = **9417.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24937.1623** | 2065.5429 | ±4131.0857 | **+12.073** | **1.47e-33** | *** |
| Education: graduate level (vs college) | +467.6599 | 545.6702 | ±1091.3405 | +0.857 | 0.3914 |  |
| Education: high school or below (vs college) | +557.2783 | 663.6263 | ±1327.2526 | +0.840 | 0.4011 |  |
| Site: UCSD (vs UAB) | +326.8277 | 573.6007 | ±1147.2015 | +0.570 | 0.5688 |  |
| Site: UW (vs UAB) | -53.5090 | 575.5574 | ±1151.1148 | -0.093 | 0.9259 |  |
| **Age (years)** | **-192.6680** | 22.1224 | ±44.2449 | **-8.709** | **3.06e-18** | *** |
| **BMI (kg/m2)** | **-72.5388** | 36.2324 | ±72.4648 | **-2.002** | **0.0453** | * |
| Hypertension | -205.9856 | 513.2309 | ±1026.4619 | -0.401 | 0.6882 |  |
| High cholesterol | +46.6592 | 504.5614 | ±1009.1228 | +0.092 | 0.9263 |  |
| **Kidney disease** | **-1673.8834** | 524.4262 | ±1048.8524 | **-3.192** | **0.0014** | ** |
| **Circulatory disease** | **-1580.5311** | 508.1361 | ±1016.2721 | **-3.110** | **0.0019** | ** |
| Avg. daily time > 250 (%) | -5.6375 | 13.5693 | ±27.1387 | -0.415 | 0.6778 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 472; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **472**, R² = **0.2121**, Adj R² = **0.1950**, F-statistic = **12.41** (p = **3.61e-19**), Residual SE = **13.939** on **461** df, AIC = **3837.5**, BIC = **3883.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.8941** | 5.8002 | ±11.6003 | **+11.706** | **1.19e-31** | *** |
| Education: graduate level (vs college) | +0.5302 | 1.5494 | ±3.0988 | +0.342 | 0.7322 |  |
| Education: high school or below (vs college) | +1.6591 | 1.9241 | ±3.8481 | +0.862 | 0.3885 |  |
| Site: UCSD (vs UAB) | +1.1197 | 1.6778 | ±3.3557 | +0.667 | 0.5045 |  |
| Site: UW (vs UAB) | +0.4899 | 1.5770 | ±3.1540 | +0.311 | 0.7560 |  |
| **Age (years)** | **-0.6036** | 0.0644 | ±0.1289 | **-9.367** | **7.47e-21** | *** |
| BMI (kg/m2) | -0.1336 | 0.0978 | ±0.1956 | -1.365 | 0.1721 |  |
| Hypertension | -0.7683 | 1.5051 | ±3.0101 | -0.510 | 0.6097 |  |
| High cholesterol | +0.1806 | 1.3945 | ±2.7889 | +0.130 | 0.8969 |  |
| **Kidney disease** | **-3.6706** | 1.5346 | ±3.0693 | **-2.392** | **0.0168** | * |
| **Circulatory disease** | **-3.8430** | 1.4588 | ±2.9176 | **-2.634** | **0.0084** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **472**, R² = **0.2140**, Adj R² = **0.1952**, F-statistic = **11.39** (p = **7.84e-19**), Residual SE = **13.937** on **460** df, AIC = **3838.3**, BIC = **3888.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.4700** | 6.4477 | ±12.8954 | **+9.999** | **1.54e-23** | *** |
| Education: graduate level (vs college) | +0.6467 | 1.5554 | ±3.1107 | +0.416 | 0.6776 |  |
| Education: high school or below (vs college) | +1.4768 | 1.9062 | ±3.8123 | +0.775 | 0.4385 |  |
| Site: UCSD (vs UAB) | +1.1758 | 1.6772 | ±3.3544 | +0.701 | 0.4833 |  |
| Site: UW (vs UAB) | +0.5966 | 1.5756 | ±3.1512 | +0.379 | 0.7049 |  |
| **Age (years)** | **-0.6001** | 0.0642 | ±0.1284 | **-9.345** | **9.21e-21** | *** |
| BMI (kg/m2) | -0.1487 | 0.0996 | ±0.1993 | -1.492 | 0.1357 |  |
| Hypertension | -0.8134 | 1.5110 | ±3.0220 | -0.538 | 0.5903 |  |
| High cholesterol | +0.2219 | 1.4012 | ±2.8025 | +0.158 | 0.8742 |  |
| **Kidney disease** | **-3.5759** | 1.5275 | ±3.0550 | **-2.341** | **0.0192** | * |
| **Circulatory disease** | **-3.8326** | 1.4541 | ±2.9083 | **-2.636** | **0.0084** | ** |
| HbA1c (%) | +0.5048 | 0.4852 | ±0.9704 | +1.040 | 0.2981 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **472**, R² = **0.2122**, Adj R² = **0.1933**, F-statistic = **11.26** (p = **1.30e-18**), Residual SE = **13.953** on **460** df, AIC = **3839.4**, BIC = **3889.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.4326** | 6.0590 | ±12.1181 | **+11.129** | **9.04e-29** | *** |
| Education: graduate level (vs college) | +0.5434 | 1.5649 | ±3.1297 | +0.347 | 0.7284 |  |
| Education: high school or below (vs college) | +1.6308 | 1.8918 | ±3.7836 | +0.862 | 0.3887 |  |
| Site: UCSD (vs UAB) | +1.1350 | 1.6729 | ±3.3457 | +0.678 | 0.4975 |  |
| Site: UW (vs UAB) | +0.5055 | 1.5670 | ±3.1339 | +0.323 | 0.7470 |  |
| **Age (years)** | **-0.6029** | 0.0639 | ±0.1279 | **-9.428** | **4.18e-21** | *** |
| BMI (kg/m2) | -0.1353 | 0.0990 | ±0.1981 | -1.366 | 0.1718 |  |
| Hypertension | -0.7673 | 1.5078 | ±3.0157 | -0.509 | 0.6108 |  |
| High cholesterol | +0.1933 | 1.4094 | ±2.8189 | +0.137 | 0.8909 |  |
| **Kidney disease** | **-3.6747** | 1.5388 | ±3.0776 | **-2.388** | **0.0169** | * |
| **Circulatory disease** | **-3.8611** | 1.4648 | ±2.9295 | **-2.636** | **0.0084** | ** |
| Mean glucose (mg/dL) | +0.0027 | 0.0169 | ±0.0338 | +0.160 | 0.8730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **472**, R² = **0.2122**, Adj R² = **0.1933**, F-statistic = **11.26** (p = **1.30e-18**), Residual SE = **13.953** on **460** df, AIC = **3839.4**, BIC = **3889.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.0587** | 7.1599 | ±14.3197 | **+9.366** | **7.54e-21** | *** |
| Education: graduate level (vs college) | +0.5434 | 1.5649 | ±3.1297 | +0.347 | 0.7284 |  |
| Education: high school or below (vs college) | +1.6308 | 1.8918 | ±3.7836 | +0.862 | 0.3887 |  |
| Site: UCSD (vs UAB) | +1.1350 | 1.6729 | ±3.3457 | +0.678 | 0.4975 |  |
| Site: UW (vs UAB) | +0.5055 | 1.5670 | ±3.1339 | +0.323 | 0.7470 |  |
| **Age (years)** | **-0.6029** | 0.0639 | ±0.1279 | **-9.428** | **4.18e-21** | *** |
| BMI (kg/m2) | -0.1353 | 0.0990 | ±0.1981 | -1.366 | 0.1718 |  |
| Hypertension | -0.7673 | 1.5078 | ±3.0157 | -0.509 | 0.6108 |  |
| High cholesterol | +0.1933 | 1.4094 | ±2.8189 | +0.137 | 0.8909 |  |
| **Kidney disease** | **-3.6747** | 1.5388 | ±3.0776 | **-2.388** | **0.0169** | * |
| **Circulatory disease** | **-3.8611** | 1.4648 | ±2.9295 | **-2.636** | **0.0084** | ** |
| GMI (%) | +0.1130 | 0.7066 | ±1.4131 | +0.160 | 0.8730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **472**, R² = **0.2130**, Adj R² = **0.1942**, F-statistic = **11.32** (p = **1.04e-18**), Residual SE = **13.946** on **460** df, AIC = **3839.0**, BIC = **3888.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1314** | 6.0304 | ±12.0608 | **+10.966** | **5.55e-28** | *** |
| Education: graduate level (vs college) | +0.5959 | 1.5697 | ±3.1395 | +0.380 | 0.7042 |  |
| Education: high school or below (vs college) | +1.5459 | 1.8958 | ±3.7916 | +0.815 | 0.4148 |  |
| Site: UCSD (vs UAB) | +1.1891 | 1.6683 | ±3.3365 | +0.713 | 0.4760 |  |
| Site: UW (vs UAB) | +0.5181 | 1.5742 | ±3.1483 | +0.329 | 0.7421 |  |
| **Age (years)** | **-0.5992** | 0.0637 | ±0.1274 | **-9.404** | **5.24e-21** | *** |
| BMI (kg/m2) | -0.1441 | 0.0997 | ±0.1994 | -1.445 | 0.1485 |  |
| Hypertension | -0.7604 | 1.5082 | ±3.0164 | -0.504 | 0.6141 |  |
| High cholesterol | +0.2491 | 1.4142 | ±2.8283 | +0.176 | 0.8602 |  |
| **Kidney disease** | **-3.6530** | 1.5334 | ±3.0669 | **-2.382** | **0.0172** | * |
| **Circulatory disease** | **-3.9200** | 1.4657 | ±2.9315 | **-2.674** | **0.0075** | ** |
| Nocturnal mean 00-06h (mg/dL) | +0.0107 | 0.0170 | ±0.0341 | +0.630 | 0.5288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1935**, F-statistic = **11.27** (p = **1.24e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.3**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1302** | 5.9112 | ±11.8224 | **+11.356** | **6.89e-30** | *** |
| Education: graduate level (vs college) | +0.5606 | 1.5653 | ±3.1306 | +0.358 | 0.7202 |  |
| Education: high school or below (vs college) | +1.5955 | 1.8932 | ±3.7863 | +0.843 | 0.3994 |  |
| Site: UCSD (vs UAB) | +1.1577 | 1.6696 | ±3.3393 | +0.693 | 0.4881 |  |
| Site: UW (vs UAB) | +0.5662 | 1.5599 | ±3.1197 | +0.363 | 0.7166 |  |
| **Age (years)** | **-0.6033** | 0.0645 | ±0.1290 | **-9.352** | **8.59e-21** | *** |
| BMI (kg/m2) | -0.1358 | 0.0985 | ±0.1970 | -1.378 | 0.1682 |  |
| Hypertension | -0.7830 | 1.5134 | ±3.0268 | -0.517 | 0.6049 |  |
| High cholesterol | +0.2081 | 1.4028 | ±2.8057 | +0.148 | 0.8821 |  |
| **Kidney disease** | **-3.7601** | 1.5703 | ±3.1405 | **-2.395** | **0.0166** | * |
| **Circulatory disease** | **-3.8667** | 1.4605 | ±2.9210 | **-2.648** | **0.0081** | ** |
| Glucose SD, pooled (mg/dL) | +0.0193 | 0.0568 | ±0.1135 | +0.339 | 0.7343 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **472**, R² = **0.2121**, Adj R² = **0.1933**, F-statistic = **11.26** (p = **1.32e-18**), Residual SE = **13.954** on **460** df, AIC = **3839.5**, BIC = **3889.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.8944** | 5.9750 | ±11.9501 | **+11.363** | **6.39e-30** | *** |
| Education: graduate level (vs college) | +0.5302 | 1.5613 | ±3.1227 | +0.340 | 0.7342 |  |
| Education: high school or below (vs college) | +1.6592 | 1.9011 | ±3.8022 | +0.873 | 0.3828 |  |
| Site: UCSD (vs UAB) | +1.1197 | 1.6690 | ±3.3380 | +0.671 | 0.5023 |  |
| Site: UW (vs UAB) | +0.4899 | 1.5616 | ±3.1232 | +0.314 | 0.7537 |  |
| **Age (years)** | **-0.6036** | 0.0646 | ±0.1292 | **-9.341** | **9.53e-21** | *** |
| BMI (kg/m2) | -0.1336 | 0.0980 | ±0.1960 | -1.363 | 0.1729 |  |
| Hypertension | -0.7683 | 1.5107 | ±3.0215 | -0.509 | 0.6111 |  |
| High cholesterol | +0.1806 | 1.4006 | ±2.8013 | +0.129 | 0.8974 |  |
| **Kidney disease** | **-3.6705** | 1.5710 | ±3.1421 | **-2.336** | **0.0195** | * |
| **Circulatory disease** | **-3.8430** | 1.4623 | ±2.9246 | **-2.628** | **0.0086** | ** |
| Avg. daily SD (mg/dL) | -0.0000 | 0.0616 | ±0.1231 | -0.000 | 0.9999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1934**, F-statistic = **11.27** (p = **1.27e-18**), Residual SE = **13.953** on **460** df, AIC = **3839.4**, BIC = **3889.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6653** | 6.2764 | ±12.5528 | **+10.940** | **7.40e-28** | *** |
| Education: graduate level (vs college) | +0.5189 | 1.5530 | ±3.1059 | +0.334 | 0.7383 |  |
| Education: high school or below (vs college) | +1.6829 | 1.9259 | ±3.8517 | +0.874 | 0.3822 |  |
| Site: UCSD (vs UAB) | +1.0997 | 1.6768 | ±3.3536 | +0.656 | 0.5119 |  |
| Site: UW (vs UAB) | +0.4373 | 1.5873 | ±3.1745 | +0.275 | 0.7829 |  |
| **Age (years)** | **-0.6028** | 0.0646 | ±0.1292 | **-9.329** | **1.07e-20** | *** |
| BMI (kg/m2) | -0.1342 | 0.0978 | ±0.1957 | -1.372 | 0.1702 |  |
| Hypertension | -0.7473 | 1.5114 | ±3.0228 | -0.494 | 0.6210 |  |
| High cholesterol | +0.1744 | 1.3965 | ±2.7929 | +0.125 | 0.9006 |  |
| **Kidney disease** | **-3.5874** | 1.5543 | ±3.1085 | **-2.308** | **0.0210** | * |
| **Circulatory disease** | **-3.8523** | 1.4618 | ±2.9237 | **-2.635** | **0.0084** | ** |
| CV (%) | -0.0330 | 0.1073 | ±0.2146 | -0.307 | 0.7585 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **472**, R² = **0.2130**, Adj R² = **0.1942**, F-statistic = **11.32** (p = **1.03e-18**), Residual SE = **13.946** on **460** df, AIC = **3838.9**, BIC = **3888.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.9758** | 6.5101 | ±13.0202 | **+10.749** | **6.00e-27** | *** |
| Education: graduate level (vs college) | +0.5626 | 1.5524 | ±3.1048 | +0.362 | 0.7171 |  |
| Education: high school or below (vs college) | +1.6139 | 1.9255 | ±3.8509 | +0.838 | 0.4019 |  |
| Site: UCSD (vs UAB) | +1.1389 | 1.6806 | ±3.3612 | +0.678 | 0.4980 |  |
| Site: UW (vs UAB) | +0.5974 | 1.5759 | ±3.1518 | +0.379 | 0.7046 |  |
| **Age (years)** | **-0.6049** | 0.0647 | ±0.1294 | **-9.351** | **8.70e-21** | *** |
| BMI (kg/m2) | -0.1307 | 0.0986 | ±0.1971 | -1.325 | 0.1850 |  |
| Hypertension | -0.8053 | 1.5089 | ±3.0177 | -0.534 | 0.5936 |  |
| High cholesterol | +0.1606 | 1.3983 | ±2.7966 | +0.115 | 0.9086 |  |
| **Kidney disease** | **-3.8581** | 1.5542 | ±3.1085 | **-2.482** | **0.0131** | * |
| **Circulatory disease** | **-3.8463** | 1.4564 | ±2.9128 | **-2.641** | **0.0083** | ** |
| Mean / SD ratio | -0.4760 | 0.5573 | ±1.1146 | -0.854 | 0.3930 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **472**, R² = **0.2130**, Adj R² = **0.1941**, F-statistic = **11.32** (p = **1.05e-18**), Residual SE = **13.946** on **460** df, AIC = **3839.0**, BIC = **3888.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.7206** | 6.3481 | ±12.6962 | **+10.983** | **4.62e-28** | *** |
| Education: graduate level (vs college) | +0.5618 | 1.5492 | ±3.0985 | +0.363 | 0.7169 |  |
| Education: high school or below (vs college) | +1.6095 | 1.9319 | ±3.8639 | +0.833 | 0.4048 |  |
| Site: UCSD (vs UAB) | +1.1396 | 1.6804 | ±3.3608 | +0.678 | 0.4977 |  |
| Site: UW (vs UAB) | +0.5710 | 1.5767 | ±3.1533 | +0.362 | 0.7172 |  |
| **Age (years)** | **-0.6057** | 0.0647 | ±0.1294 | **-9.359** | **8.05e-21** | *** |
| BMI (kg/m2) | -0.1269 | 0.0986 | ±0.1973 | -1.286 | 0.1984 |  |
| Hypertension | -0.7928 | 1.5069 | ±3.0138 | -0.526 | 0.5988 |  |
| High cholesterol | +0.1673 | 1.3974 | ±2.7949 | +0.120 | 0.9047 |  |
| **Kidney disease** | **-3.8339** | 1.5426 | ±3.0851 | **-2.485** | **0.0129** | * |
| **Circulatory disease** | **-3.8239** | 1.4564 | ±2.9128 | **-2.626** | **0.0086** | ** |
| Avg. daily mean/SD | -0.3708 | 0.4450 | ±0.8900 | -0.833 | 0.4047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **472**, R² = **0.2184**, Adj R² = **0.1998**, F-statistic = **11.69** (p = **2.35e-19**), Residual SE = **13.898** on **460** df, AIC = **3835.7**, BIC = **3885.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.9756** | 6.6032 | ±13.2064 | **+9.234** | **2.60e-20** | *** |
| Education: graduate level (vs college) | +0.7094 | 1.5503 | ±3.1005 | +0.458 | 0.6473 |  |
| Education: high school or below (vs college) | +1.4534 | 1.9060 | ±3.8120 | +0.763 | 0.4458 |  |
| Site: UCSD (vs UAB) | +1.4035 | 1.6878 | ±3.3756 | +0.832 | 0.4057 |  |
| Site: UW (vs UAB) | +0.9589 | 1.5618 | ±3.1236 | +0.614 | 0.5393 |  |
| **Age (years)** | **-0.5912** | 0.0635 | ±0.1269 | **-9.315** | **1.22e-20** | *** |
| BMI (kg/m2) | -0.1297 | 0.0983 | ±0.1966 | -1.319 | 0.1872 |  |
| Hypertension | -0.7916 | 1.5110 | ±3.0220 | -0.524 | 0.6004 |  |
| High cholesterol | +0.2610 | 1.4061 | ±2.8122 | +0.186 | 0.8528 |  |
| **Kidney disease** | **-3.9798** | 1.5402 | ±3.0804 | **-2.584** | **0.0098** | ** |
| **Circulatory disease** | **-3.9077** | 1.4563 | ±2.9126 | **-2.683** | **0.0073** | ** |
| MAG (mg/dL/h) | +0.1269 | 0.0739 | ±0.1477 | +1.719 | 0.0857 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1935**, F-statistic = **11.27** (p = **1.24e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.3**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.7617** | 6.3000 | ±12.6000 | **+10.597** | **3.07e-26** | *** |
| Education: graduate level (vs college) | +0.5536 | 1.5581 | ±3.1161 | +0.355 | 0.7223 |  |
| Education: high school or below (vs college) | +1.5807 | 1.9068 | ±3.8136 | +0.829 | 0.4071 |  |
| Site: UCSD (vs UAB) | +1.1690 | 1.6716 | ±3.3432 | +0.699 | 0.4843 |  |
| Site: UW (vs UAB) | +0.5621 | 1.5678 | ±3.1357 | +0.359 | 0.7199 |  |
| **Age (years)** | **-0.6027** | 0.0644 | ±0.1288 | **-9.359** | **8.08e-21** | *** |
| BMI (kg/m2) | -0.1331 | 0.0982 | ±0.1964 | -1.355 | 0.1755 |  |
| Hypertension | -0.7625 | 1.5076 | ±3.0153 | -0.506 | 0.6130 |  |
| High cholesterol | +0.1924 | 1.4000 | ±2.8000 | +0.137 | 0.8907 |  |
| **Kidney disease** | **-3.7805** | 1.5675 | ±3.1351 | **-2.412** | **0.0159** | * |
| **Circulatory disease** | **-3.8633** | 1.4583 | ±2.9166 | **-2.649** | **0.0081** | ** |
| Avg. daily range (mg/dL) | +0.0066 | 0.0184 | ±0.0368 | +0.358 | 0.7207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **472**, R² = **0.2146**, Adj R² = **0.1958**, F-statistic = **11.43** (p = **6.70e-19**), Residual SE = **13.932** on **460** df, AIC = **3838.0**, BIC = **3887.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.5157** | 5.7908 | ±11.5816 | **+11.486** | **1.54e-30** | *** |
| Education: graduate level (vs college) | +0.6687 | 1.5759 | ±3.1519 | +0.424 | 0.6713 |  |
| Education: high school or below (vs college) | +1.6088 | 1.9091 | ±3.8182 | +0.843 | 0.3994 |  |
| Site: UCSD (vs UAB) | +1.1605 | 1.6766 | ±3.3532 | +0.692 | 0.4888 |  |
| Site: UW (vs UAB) | +0.6752 | 1.5679 | ±3.1358 | +0.431 | 0.6667 |  |
| **Age (years)** | **-0.5966** | 0.0637 | ±0.1274 | **-9.364** | **7.71e-21** | *** |
| BMI (kg/m2) | -0.1477 | 0.0990 | ±0.1981 | -1.491 | 0.1359 |  |
| Hypertension | -0.8974 | 1.5163 | ±3.0325 | -0.592 | 0.5539 |  |
| High cholesterol | +0.2935 | 1.3996 | ±2.7993 | +0.210 | 0.8339 |  |
| **Kidney disease** | **-3.7381** | 1.5377 | ±3.0755 | **-2.431** | **0.0151** | * |
| **Circulatory disease** | **-4.0144** | 1.4613 | ±2.9226 | **-2.747** | **0.0060** | ** |
| SD of daily means (mg/dL) | +0.0913 | 0.0817 | ±0.1633 | +1.118 | 0.2637 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1934**, F-statistic = **11.27** (p = **1.26e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.4**, BIC = **3889.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.4525** | 6.3788 | ±12.7576 | **+10.731** | **7.26e-27** | *** |
| Education: graduate level (vs college) | +0.5496 | 1.5632 | ±3.1264 | +0.352 | 0.7251 |  |
| Education: high school or below (vs college) | +1.6037 | 1.8920 | ±3.7841 | +0.848 | 0.3967 |  |
| Site: UCSD (vs UAB) | +1.1580 | 1.6696 | ±3.3392 | +0.694 | 0.4879 |  |
| Site: UW (vs UAB) | +0.5208 | 1.5652 | ±3.1304 | +0.333 | 0.7393 |  |
| **Age (years)** | **-0.6029** | 0.0643 | ±0.1285 | **-9.382** | **6.50e-21** | *** |
| BMI (kg/m2) | -0.1374 | 0.0988 | ±0.1976 | -1.391 | 0.1642 |  |
| Hypertension | -0.7617 | 1.5060 | ±3.0120 | -0.506 | 0.6130 |  |
| High cholesterol | +0.2149 | 1.4129 | ±2.8258 | +0.152 | 0.8791 |  |
| **Kidney disease** | **-3.6835** | 1.5411 | ±3.0822 | **-2.390** | **0.0168** | * |
| **Circulatory disease** | **-3.8768** | 1.4602 | ±2.9205 | **-2.655** | **0.0079** | ** |
| Time in range 70-180, pooled (%) | -0.0079 | 0.0269 | ±0.0538 | -0.292 | 0.7701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1935**, F-statistic = **11.27** (p = **1.25e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.4**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.4921** | 6.3871 | ±12.7743 | **+10.723** | **7.90e-27** | *** |
| Education: graduate level (vs college) | +0.5483 | 1.5620 | ±3.1241 | +0.351 | 0.7256 |  |
| Education: high school or below (vs college) | +1.5974 | 1.8894 | ±3.7788 | +0.845 | 0.3979 |  |
| Site: UCSD (vs UAB) | +1.1635 | 1.6685 | ±3.3369 | +0.697 | 0.4856 |  |
| Site: UW (vs UAB) | +0.5232 | 1.5644 | ±3.1289 | +0.334 | 0.7381 |  |
| **Age (years)** | **-0.6030** | 0.0643 | ±0.1286 | **-9.375** | **6.89e-21** | *** |
| BMI (kg/m2) | -0.1377 | 0.0989 | ±0.1977 | -1.393 | 0.1636 |  |
| Hypertension | -0.7597 | 1.5056 | ±3.0112 | -0.505 | 0.6139 |  |
| High cholesterol | +0.2161 | 1.4128 | ±2.8257 | +0.153 | 0.8784 |  |
| **Kidney disease** | **-3.6880** | 1.5424 | ±3.0848 | **-2.391** | **0.0168** | * |
| **Circulatory disease** | **-3.8782** | 1.4605 | ±2.9210 | **-2.655** | **0.0079** | ** |
| Avg. daily time in range 70-180 (%) | -0.0083 | 0.0266 | ±0.0533 | -0.310 | 0.7568 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **472**, R² = **0.2142**, Adj R² = **0.1954**, F-statistic = **11.40** (p = **7.50e-19**), Residual SE = **13.935** on **460** df, AIC = **3838.2**, BIC = **3888.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.5437** | 5.8731 | ±11.7462 | **+11.671** | **1.80e-31** | *** |
| Education: graduate level (vs college) | +0.5212 | 1.5502 | ±3.1003 | +0.336 | 0.7367 |  |
| Education: high school or below (vs college) | +1.5985 | 1.9236 | ±3.8471 | +0.831 | 0.4060 |  |
| Site: UCSD (vs UAB) | +0.9913 | 1.6930 | ±3.3860 | +0.586 | 0.5582 |  |
| Site: UW (vs UAB) | +0.4065 | 1.5888 | ±3.1776 | +0.256 | 0.7981 |  |
| **Age (years)** | **-0.6070** | 0.0647 | ±0.1295 | **-9.375** | **6.93e-21** | *** |
| BMI (kg/m2) | -0.1355 | 0.0987 | ±0.1973 | -1.373 | 0.1697 |  |
| Hypertension | -0.6479 | 1.5194 | ±3.0389 | -0.426 | 0.6698 |  |
| High cholesterol | +0.1314 | 1.3941 | ±2.7882 | +0.094 | 0.9249 |  |
| **Kidney disease** | **-3.6642** | 1.5399 | ±3.0798 | **-2.379** | **0.0173** | * |
| **Circulatory disease** | **-3.7364** | 1.4652 | ±2.9305 | **-2.550** | **0.0108** | * |
| Any reading < 54 during wear (0/1) | -1.7188 | 1.6081 | ±3.2161 | -1.069 | 0.2851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **472**, R² = **0.2171**, Adj R² = **0.1984**, F-statistic = **11.60** (p = **3.36e-19**), Residual SE = **13.909** on **460** df, AIC = **3836.5**, BIC = **3886.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.2400** | 5.8072 | ±11.6144 | **+11.751** | **6.98e-32** | *** |
| Education: graduate level (vs college) | +0.4172 | 1.5458 | ±3.0916 | +0.270 | 0.7873 |  |
| Education: high school or below (vs college) | +1.4746 | 1.9269 | ±3.8539 | +0.765 | 0.4441 |  |
| Site: UCSD (vs UAB) | +0.8916 | 1.6817 | ±3.3634 | +0.530 | 0.5960 |  |
| Site: UW (vs UAB) | +0.1799 | 1.5922 | ±3.1843 | +0.113 | 0.9101 |  |
| **Age (years)** | **-0.6014** | 0.0644 | ±0.1287 | **-9.342** | **9.42e-21** | *** |
| BMI (kg/m2) | -0.1338 | 0.0977 | ±0.1955 | -1.369 | 0.1709 |  |
| Hypertension | -0.4640 | 1.5071 | ±3.0142 | -0.308 | 0.7582 |  |
| High cholesterol | -0.0190 | 1.3902 | ±2.7803 | -0.014 | 0.9891 |  |
| **Kidney disease** | **-3.6459** | 1.5298 | ±3.0597 | **-2.383** | **0.0172** | * |
| **Circulatory disease** | **-4.0562** | 1.4613 | ±2.9227 | **-2.776** | **0.0055** | ** |
| **Time < 54 (%)** | **-4.1782** | 1.5671 | ±3.1342 | **-2.666** | **0.0077** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **472**, R² = **0.2170**, Adj R² = **0.1982**, F-statistic = **11.59** (p = **3.51e-19**), Residual SE = **13.911** on **460** df, AIC = **3836.6**, BIC = **3886.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0659** | 5.7984 | ±11.5968 | **+11.739** | **8.06e-32** | *** |
| Education: graduate level (vs college) | +0.4538 | 1.5483 | ±3.0966 | +0.293 | 0.7694 |  |
| Education: high school or below (vs college) | +1.5002 | 1.9231 | ±3.8462 | +0.780 | 0.4353 |  |
| Site: UCSD (vs UAB) | +0.9426 | 1.6816 | ±3.3633 | +0.561 | 0.5751 |  |
| Site: UW (vs UAB) | +0.2480 | 1.5857 | ±3.1714 | +0.156 | 0.8757 |  |
| **Age (years)** | **-0.6025** | 0.0645 | ±0.1290 | **-9.341** | **9.53e-21** | *** |
| BMI (kg/m2) | -0.1309 | 0.0976 | ±0.1951 | -1.341 | 0.1798 |  |
| Hypertension | -0.5573 | 1.5061 | ±3.0121 | -0.370 | 0.7114 |  |
| High cholesterol | +0.0046 | 1.3933 | ±2.7866 | +0.003 | 0.9973 |  |
| **Kidney disease** | **-3.6011** | 1.5289 | ±3.0579 | **-2.355** | **0.0185** | * |
| **Circulatory disease** | **-3.9842** | 1.4600 | ±2.9201 | **-2.729** | **0.0064** | ** |
| **Avg. daily time < 54 (%)** | **-2.9451** | 0.5914 | ±1.1828 | **-4.980** | **6.37e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **472**, R² = **0.2156**, Adj R² = **0.1969**, F-statistic = **11.50** (p = **5.07e-19**), Residual SE = **13.923** on **460** df, AIC = **3837.4**, BIC = **3887.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.2801** | 5.7742 | ±11.5484 | **+11.825** | **2.90e-32** | *** |
| Education: graduate level (vs college) | +0.4097 | 1.5406 | ±3.0813 | +0.266 | 0.7903 |  |
| Education: high school or below (vs college) | +1.6131 | 1.9248 | ±3.8496 | +0.838 | 0.4020 |  |
| Site: UCSD (vs UAB) | +0.8610 | 1.6713 | ±3.3426 | +0.515 | 0.6064 |  |
| Site: UW (vs UAB) | +0.2086 | 1.5878 | ±3.1756 | +0.131 | 0.8955 |  |
| **Age (years)** | **-0.5980** | 0.0644 | ±0.1288 | **-9.286** | **1.61e-20** | *** |
| BMI (kg/m2) | -0.1388 | 0.0974 | ±0.1948 | -1.425 | 0.1542 |  |
| Hypertension | -0.5726 | 1.4888 | ±2.9775 | -0.385 | 0.7005 |  |
| High cholesterol | -0.0101 | 1.3845 | ±2.7691 | -0.007 | 0.9942 |  |
| **Kidney disease** | **-3.6393** | 1.5338 | ±3.0675 | **-2.373** | **0.0177** | * |
| **Circulatory disease** | **-4.0615** | 1.4633 | ±2.9266 | **-2.776** | **0.0055** | ** |
| Time 54-69, pooled (%) | -1.0639 | 0.7948 | ±1.5896 | -1.339 | 0.1807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **472**, R² = **0.2168**, Adj R² = **0.1981**, F-statistic = **11.58** (p = **3.69e-19**), Residual SE = **13.912** on **460** df, AIC = **3836.7**, BIC = **3886.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.1697** | 5.7798 | ±11.5596 | **+11.794** | **4.17e-32** | *** |
| Education: graduate level (vs college) | +0.4029 | 1.5412 | ±3.0823 | +0.261 | 0.7938 |  |
| Education: high school or below (vs college) | +1.5903 | 1.9179 | ±3.8359 | +0.829 | 0.4070 |  |
| Site: UCSD (vs UAB) | +0.8311 | 1.6750 | ±3.3499 | +0.496 | 0.6197 |  |
| Site: UW (vs UAB) | +0.1633 | 1.5929 | ±3.1858 | +0.103 | 0.9183 |  |
| **Age (years)** | **-0.5970** | 0.0644 | ±0.1287 | **-9.274** | **1.79e-20** | *** |
| BMI (kg/m2) | -0.1367 | 0.0976 | ±0.1952 | -1.401 | 0.1612 |  |
| Hypertension | -0.5398 | 1.4908 | ±2.9815 | -0.362 | 0.7173 |  |
| High cholesterol | -0.0322 | 1.3820 | ±2.7640 | -0.023 | 0.9814 |  |
| **Kidney disease** | **-3.6189** | 1.5334 | ±3.0668 | **-2.360** | **0.0183** | * |
| **Circulatory disease** | **-4.0754** | 1.4646 | ±2.9293 | **-2.783** | **0.0054** | ** |
| Avg. daily time 54-69 (%) | -1.1145 | 0.7051 | ±1.4101 | -1.581 | 0.1139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **472**, R² = **0.2166**, Adj R² = **0.1979**, F-statistic = **11.56** (p = **3.89e-19**), Residual SE = **13.914** on **460** df, AIC = **3836.8**, BIC = **3886.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.3378** | 5.7777 | ±11.5555 | **+11.828** | **2.80e-32** | *** |
| Education: graduate level (vs college) | +0.3905 | 1.5404 | ±3.0808 | +0.253 | 0.7999 |  |
| Education: high school or below (vs college) | +1.5720 | 1.9240 | ±3.8480 | +0.817 | 0.4139 |  |
| Site: UCSD (vs UAB) | +0.8232 | 1.6729 | ±3.3458 | +0.492 | 0.6227 |  |
| Site: UW (vs UAB) | +0.1527 | 1.5906 | ±3.1811 | +0.096 | 0.9235 |  |
| **Age (years)** | **-0.5978** | 0.0643 | ±0.1287 | **-9.292** | **1.51e-20** | *** |
| BMI (kg/m2) | -0.1385 | 0.0975 | ±0.1949 | -1.421 | 0.1554 |  |
| Hypertension | -0.5126 | 1.4894 | ±2.9788 | -0.344 | 0.7307 |  |
| High cholesterol | -0.0455 | 1.3841 | ±2.7682 | -0.033 | 0.9738 |  |
| **Kidney disease** | **-3.6354** | 1.5320 | ±3.0641 | **-2.373** | **0.0176** | * |
| **Circulatory disease** | **-4.0983** | 1.4636 | ±2.9272 | **-2.800** | **0.0051** | ** |
| Time < 70 (%) | -0.9958 | 0.6082 | ±1.2164 | -1.637 | 0.1016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **472**, R² = **0.2177**, Adj R² = **0.1990**, F-statistic = **11.64** (p = **2.88e-19**), Residual SE = **13.904** on **460** df, AIC = **3836.1**, BIC = **3886.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.1856** | 5.7819 | ±11.5638 | **+11.793** | **4.24e-32** | *** |
| Education: graduate level (vs college) | +0.3965 | 1.5424 | ±3.0848 | +0.257 | 0.7971 |  |
| Education: high school or below (vs college) | +1.5487 | 1.9170 | ±3.8341 | +0.808 | 0.4192 |  |
| Site: UCSD (vs UAB) | +0.8154 | 1.6770 | ±3.3539 | +0.486 | 0.6268 |  |
| Site: UW (vs UAB) | +0.1321 | 1.5928 | ±3.1857 | +0.083 | 0.9339 |  |
| **Age (years)** | **-0.5976** | 0.0643 | ±0.1287 | **-9.290** | **1.55e-20** | *** |
| BMI (kg/m2) | -0.1354 | 0.0976 | ±0.1952 | -1.388 | 0.1652 |  |
| Hypertension | -0.5045 | 1.4939 | ±2.9878 | -0.338 | 0.7356 |  |
| High cholesterol | -0.0585 | 1.3842 | ±2.7683 | -0.042 | 0.9663 |  |
| **Kidney disease** | **-3.6039** | 1.5310 | ±3.0621 | **-2.354** | **0.0186** | * |
| **Circulatory disease** | **-4.0876** | 1.4637 | ±2.9273 | **-2.793** | **0.0052** | ** |
| **Avg. daily time < 70 (%)** | **-0.9537** | 0.4517 | ±0.9035 | **-2.111** | **0.0348** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **472**, R² = **0.2124**, Adj R² = **0.1936**, F-statistic = **11.28** (p = **1.22e-18**), Residual SE = **13.951** on **460** df, AIC = **3839.3**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.7064** | 7.1122 | ±14.2244 | **+9.379** | **6.65e-21** | *** |
| Education: graduate level (vs college) | +0.4787 | 1.5809 | ±3.1618 | +0.303 | 0.7620 |  |
| Education: high school or below (vs college) | +1.7162 | 1.8946 | ±3.7893 | +0.906 | 0.3650 |  |
| Site: UCSD (vs UAB) | +1.0909 | 1.6701 | ±3.3401 | +0.653 | 0.5136 |  |
| Site: UW (vs UAB) | +0.4277 | 1.5591 | ±3.1183 | +0.274 | 0.7839 |  |
| **Age (years)** | **-0.6061** | 0.0637 | ±0.1273 | **-9.520** | **1.73e-21** | *** |
| BMI (kg/m2) | -0.1303 | 0.0989 | ±0.1978 | -1.318 | 0.1876 |  |
| Hypertension | -0.7443 | 1.5101 | ±3.0202 | -0.493 | 0.6221 |  |
| High cholesterol | +0.1528 | 1.4077 | ±2.8153 | +0.109 | 0.9136 |  |
| **Kidney disease** | **-3.6446** | 1.5448 | ±3.0895 | **-2.359** | **0.0183** | * |
| **Circulatory disease** | **-3.8168** | 1.4686 | ±2.9373 | **-2.599** | **0.0094** | ** |
| Time 54-250, pooled (%) | +0.0142 | 0.0387 | ±0.0773 | +0.367 | 0.7135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1935**, F-statistic = **11.27** (p = **1.25e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.4**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8989** | 7.0640 | ±14.1281 | **+9.470** | **2.79e-21** | *** |
| Education: graduate level (vs college) | +0.4891 | 1.5812 | ±3.1624 | +0.309 | 0.7571 |  |
| Education: high school or below (vs college) | +1.7049 | 1.8963 | ±3.7927 | +0.899 | 0.3686 |  |
| Site: UCSD (vs UAB) | +1.0951 | 1.6702 | ±3.3404 | +0.656 | 0.5120 |  |
| Site: UW (vs UAB) | +0.4408 | 1.5601 | ±3.1202 | +0.283 | 0.7775 |  |
| **Age (years)** | **-0.6053** | 0.0638 | ±0.1276 | **-9.490** | **2.31e-21** | *** |
| BMI (kg/m2) | -0.1309 | 0.0988 | ±0.1975 | -1.325 | 0.1851 |  |
| Hypertension | -0.7505 | 1.5106 | ±3.0213 | -0.497 | 0.6193 |  |
| High cholesterol | +0.1579 | 1.4073 | ±2.8146 | +0.112 | 0.9107 |  |
| **Kidney disease** | **-3.6456** | 1.5461 | ±3.0922 | **-2.358** | **0.0184** | * |
| **Circulatory disease** | **-3.8195** | 1.4676 | ±2.9352 | **-2.603** | **0.0093** | ** |
| Avg. daily time 54-250 (%) | +0.0116 | 0.0375 | ±0.0750 | +0.310 | 0.7565 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **472**, R² = **0.2142**, Adj R² = **0.1955**, F-statistic = **11.40** (p = **7.40e-19**), Residual SE = **13.935** on **460** df, AIC = **3838.2**, BIC = **3888.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2845** | 5.8165 | ±11.6330 | **+11.568** | **5.99e-31** | *** |
| Education: graduate level (vs college) | +0.4671 | 1.5465 | ±3.0930 | +0.302 | 0.7626 |  |
| Education: high school or below (vs college) | +1.5073 | 1.9164 | ±3.8327 | +0.787 | 0.4316 |  |
| Site: UCSD (vs UAB) | +1.2480 | 1.6785 | ±3.3570 | +0.743 | 0.4572 |  |
| Site: UW (vs UAB) | +0.4541 | 1.5859 | ±3.1718 | +0.286 | 0.7746 |  |
| **Age (years)** | **-0.6081** | 0.0650 | ±0.1300 | **-9.354** | **8.41e-21** | *** |
| BMI (kg/m2) | -0.1469 | 0.0977 | ±0.1953 | -1.504 | 0.1326 |  |
| Hypertension | -0.6342 | 1.4893 | ±2.9786 | -0.426 | 0.6702 |  |
| High cholesterol | +0.2905 | 1.4010 | ±2.8020 | +0.207 | 0.8357 |  |
| **Kidney disease** | **-3.6600** | 1.5333 | ±3.0667 | **-2.387** | **0.0170** | * |
| **Circulatory disease** | **-3.9749** | 1.4511 | ±2.9023 | **-2.739** | **0.0062** | ** |
| Time 181-250, pooled (%) | +0.0495 | 0.0428 | ±0.0856 | +1.157 | 0.2474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **472**, R² = **0.2140**, Adj R² = **0.1952**, F-statistic = **11.39** (p = **7.88e-19**), Residual SE = **13.937** on **460** df, AIC = **3838.3**, BIC = **3888.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.3051** | 5.8039 | ±11.6078 | **+11.597** | **4.29e-31** | *** |
| Education: graduate level (vs college) | +0.4636 | 1.5472 | ±3.0944 | +0.300 | 0.7644 |  |
| Education: high school or below (vs college) | +1.4945 | 1.9084 | ±3.8168 | +0.783 | 0.4336 |  |
| Site: UCSD (vs UAB) | +1.2534 | 1.6776 | ±3.3552 | +0.747 | 0.4550 |  |
| Site: UW (vs UAB) | +0.4676 | 1.5852 | ±3.1703 | +0.295 | 0.7680 |  |
| **Age (years)** | **-0.6073** | 0.0650 | ±0.1300 | **-9.344** | **9.25e-21** | *** |
| BMI (kg/m2) | -0.1462 | 0.0981 | ±0.1961 | -1.491 | 0.1361 |  |
| Hypertension | -0.6416 | 1.4928 | ±2.9856 | -0.430 | 0.6673 |  |
| High cholesterol | +0.2791 | 1.4030 | ±2.8060 | +0.199 | 0.8423 |  |
| **Kidney disease** | **-3.6667** | 1.5340 | ±3.0679 | **-2.390** | **0.0168** | * |
| **Circulatory disease** | **-3.9554** | 1.4547 | ±2.9094 | **-2.719** | **0.0065** | ** |
| Avg. daily time 181-250 (%) | +0.0458 | 0.0418 | ±0.0836 | +1.094 | 0.2740 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **472**, R² = **0.2124**, Adj R² = **0.1935**, F-statistic = **11.27** (p = **1.23e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.3**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6241** | 5.7586 | ±11.5172 | **+11.743** | **7.66e-32** | *** |
| Education: graduate level (vs college) | +0.5522 | 1.5622 | ±3.1244 | +0.353 | 0.7237 |  |
| Education: high school or below (vs college) | +1.5917 | 1.8919 | ±3.7838 | +0.841 | 0.4002 |  |
| Site: UCSD (vs UAB) | +1.1629 | 1.6701 | ±3.3403 | +0.696 | 0.4862 |  |
| Site: UW (vs UAB) | +0.5239 | 1.5666 | ±3.1332 | +0.334 | 0.7381 |  |
| **Age (years)** | **-0.6027** | 0.0642 | ±0.1285 | **-9.382** | **6.48e-21** | *** |
| BMI (kg/m2) | -0.1382 | 0.0987 | ±0.1975 | -1.400 | 0.1615 |  |
| Hypertension | -0.7579 | 1.5053 | ±3.0105 | -0.504 | 0.6146 |  |
| High cholesterol | +0.2197 | 1.4125 | ±2.8250 | +0.156 | 0.8764 |  |
| **Kidney disease** | **-3.6858** | 1.5407 | ±3.0815 | **-2.392** | **0.0167** | * |
| **Circulatory disease** | **-3.8861** | 1.4600 | ±2.9200 | **-2.662** | **0.0078** | ** |
| Time > 180 (%) | +0.0095 | 0.0267 | ±0.0533 | +0.355 | 0.7228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **472**, R² = **0.2124**, Adj R² = **0.1936**, F-statistic = **11.28** (p = **1.22e-18**), Residual SE = **13.951** on **460** df, AIC = **3839.3**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6129** | 5.7597 | ±11.5194 | **+11.739** | **8.04e-32** | *** |
| Education: graduate level (vs college) | +0.5514 | 1.5610 | ±3.1221 | +0.353 | 0.7239 |  |
| Education: high school or below (vs college) | +1.5807 | 1.8887 | ±3.7774 | +0.837 | 0.4026 |  |
| Site: UCSD (vs UAB) | +1.1712 | 1.6690 | ±3.3379 | +0.702 | 0.4828 |  |
| Site: UW (vs UAB) | +0.5277 | 1.5660 | ±3.1319 | +0.337 | 0.7361 |  |
| **Age (years)** | **-0.6028** | 0.0643 | ±0.1286 | **-9.376** | **6.87e-21** | *** |
| BMI (kg/m2) | -0.1388 | 0.0988 | ±0.1976 | -1.404 | 0.1602 |  |
| Hypertension | -0.7547 | 1.5048 | ±3.0096 | -0.502 | 0.6160 |  |
| High cholesterol | +0.2224 | 1.4126 | ±2.8252 | +0.157 | 0.8749 |  |
| **Kidney disease** | **-3.6917** | 1.5419 | ±3.0837 | **-2.394** | **0.0167** | * |
| **Circulatory disease** | **-3.8897** | 1.4602 | ±2.9205 | **-2.664** | **0.0077** | ** |
| Avg. daily time > 180 (%) | +0.0103 | 0.0265 | ±0.0529 | +0.390 | 0.6962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **472**, R² = **0.2129**, Adj R² = **0.1940**, F-statistic = **11.31** (p = **1.08e-18**), Residual SE = **13.947** on **460** df, AIC = **3839.0**, BIC = **3888.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5513** | 5.7881 | ±11.5762 | **+11.671** | **1.80e-31** | *** |
| Education: graduate level (vs college) | +0.5936 | 1.5725 | ±3.1451 | +0.377 | 0.7058 |  |
| Education: high school or below (vs college) | +1.5533 | 1.8985 | ±3.7970 | +0.818 | 0.4133 |  |
| Site: UCSD (vs UAB) | +1.2030 | 1.6650 | ±3.3300 | +0.723 | 0.4700 |  |
| Site: UW (vs UAB) | +0.5283 | 1.5713 | ±3.1426 | +0.336 | 0.7367 |  |
| **Age (years)** | **-0.6005** | 0.0641 | ±0.1281 | **-9.373** | **7.05e-21** | *** |
| BMI (kg/m2) | -0.1449 | 0.0988 | ±0.1976 | -1.466 | 0.1425 |  |
| Hypertension | -0.7628 | 1.5080 | ±3.0160 | -0.506 | 0.6130 |  |
| High cholesterol | +0.2770 | 1.4211 | ±2.8422 | +0.195 | 0.8455 |  |
| **Kidney disease** | **-3.6859** | 1.5412 | ±3.0824 | **-2.392** | **0.0168** | * |
| **Circulatory disease** | **-3.9208** | 1.4597 | ±2.9194 | **-2.686** | **0.0072** | ** |
| Nocturnal time > 180 (%) | +0.0149 | 0.0244 | ±0.0488 | +0.610 | 0.5420 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **472**, R² = **0.2124**, Adj R² = **0.1935**, F-statistic = **11.27** (p = **1.23e-18**), Residual SE = **13.952** on **460** df, AIC = **3839.3**, BIC = **3889.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.1100** | 5.7470 | ±11.4939 | **+11.851** | **2.11e-32** | *** |
| Education: graduate level (vs college) | +0.4823 | 1.5806 | ±3.1612 | +0.305 | 0.7602 |  |
| Education: high school or below (vs college) | +1.7132 | 1.8943 | ±3.7887 | +0.904 | 0.3658 |  |
| Site: UCSD (vs UAB) | +1.0934 | 1.6703 | ±3.3406 | +0.655 | 0.5127 |  |
| Site: UW (vs UAB) | +0.4326 | 1.5593 | ±3.1187 | +0.277 | 0.7814 |  |
| **Age (years)** | **-0.6059** | 0.0637 | ±0.1273 | **-9.519** | **1.75e-21** | *** |
| BMI (kg/m2) | -0.1305 | 0.0989 | ±0.1979 | -1.320 | 0.1869 |  |
| Hypertension | -0.7468 | 1.5100 | ±3.0200 | -0.495 | 0.6209 |  |
| High cholesterol | +0.1552 | 1.4075 | ±2.8150 | +0.110 | 0.9122 |  |
| **Kidney disease** | **-3.6464** | 1.5447 | ±3.0895 | **-2.361** | **0.0183** | * |
| **Circulatory disease** | **-3.8178** | 1.4686 | ±2.9371 | **-2.600** | **0.0093** | ** |
| Time > 250 (%) | -0.0133 | 0.0387 | ±0.0773 | -0.344 | 0.7310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 472)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **472**, R² = **0.2123**, Adj R² = **0.1934**, F-statistic = **11.27** (p = **1.27e-18**), Residual SE = **13.953** on **460** df, AIC = **3839.4**, BIC = **3889.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0428** | 5.7571 | ±11.5142 | **+11.819** | **3.12e-32** | *** |
| Education: graduate level (vs college) | +0.4938 | 1.5809 | ±3.1617 | +0.312 | 0.7547 |  |
| Education: high school or below (vs college) | +1.7005 | 1.8960 | ±3.7920 | +0.897 | 0.3698 |  |
| Site: UCSD (vs UAB) | +1.0984 | 1.6704 | ±3.3409 | +0.658 | 0.5108 |  |
| Site: UW (vs UAB) | +0.4470 | 1.5604 | ±3.1208 | +0.286 | 0.7745 |  |
| **Age (years)** | **-0.6052** | 0.0638 | ±0.1276 | **-9.488** | **2.35e-21** | *** |
| BMI (kg/m2) | -0.1312 | 0.0988 | ±0.1975 | -1.328 | 0.1841 |  |
| Hypertension | -0.7532 | 1.5106 | ±3.0211 | -0.499 | 0.6181 |  |
| High cholesterol | +0.1609 | 1.4071 | ±2.8143 | +0.114 | 0.9089 |  |
| **Kidney disease** | **-3.6485** | 1.5460 | ±3.0919 | **-2.360** | **0.0183** | * |
| **Circulatory disease** | **-3.8215** | 1.4674 | ±2.9348 | **-2.604** | **0.0092** | ** |
| Avg. daily time > 250 (%) | -0.0104 | 0.0375 | ±0.0750 | -0.276 | 0.7823 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 474; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **474**, R² = **0.1894**, Adj R² = **0.1719**, F-statistic = **10.82** (p = **1.32e-16**), Residual SE = **8.391** on **463** df, AIC = **3372.6**, BIC = **3418.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.9435** | 3.5979 | ±7.1958 | **+22.219** | **2.23e-109** | *** |
| Education: graduate level (vs college) | -0.7684 | 0.9387 | ±1.8774 | -0.819 | 0.4130 |  |
| Education: high school or below (vs college) | +1.5314 | 1.0233 | ±2.0465 | +1.497 | 0.1345 |  |
| Site: UCSD (vs UAB) | -1.1080 | 1.0475 | ±2.0951 | -1.058 | 0.2902 |  |
| Site: UW (vs UAB) | +0.5693 | 0.9676 | ±1.9352 | +0.588 | 0.5563 |  |
| **Age (years)** | **-0.2783** | 0.0392 | ±0.0783 | **-7.107** | **1.18e-12** | *** |
| **BMI (kg/m2)** | **+0.1415** | 0.0599 | ±0.1197 | **+2.363** | **0.0181** | * |
| Hypertension | +0.0303 | 0.9108 | ±1.8217 | +0.033 | 0.9735 |  |
| High cholesterol | -0.2184 | 0.8808 | ±1.7617 | -0.248 | 0.8042 |  |
| Kidney disease | -0.8583 | 0.9712 | ±1.9425 | -0.884 | 0.3769 |  |
| Circulatory disease | -1.5306 | 0.9741 | ±1.9483 | -1.571 | 0.1161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **474**, R² = **0.1960**, Adj R² = **0.1769**, F-statistic = **10.24** (p = **7.93e-17**), Residual SE = **8.366** on **462** df, AIC = **3370.7**, BIC = **3420.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.1514** | 4.1160 | ±8.2320 | **+18.501** | **2.01e-76** | *** |
| Education: graduate level (vs college) | -0.6401 | 0.9389 | ±1.8778 | -0.682 | 0.4954 |  |
| Education: high school or below (vs college) | +1.3224 | 1.0116 | ±2.0232 | +1.307 | 0.1911 |  |
| Site: UCSD (vs UAB) | -1.0522 | 1.0434 | ±2.0868 | -1.008 | 0.3133 |  |
| Site: UW (vs UAB) | +0.6873 | 0.9758 | ±1.9516 | +0.704 | 0.4812 |  |
| **Age (years)** | **-0.2743** | 0.0390 | ±0.0780 | **-7.036** | **1.98e-12** | *** |
| **BMI (kg/m2)** | **+0.1248** | 0.0604 | ±0.1209 | **+2.065** | **0.0390** | * |
| Hypertension | -0.0232 | 0.9117 | ±1.8233 | -0.025 | 0.9797 |  |
| High cholesterol | -0.1691 | 0.8811 | ±1.7623 | -0.192 | 0.8478 |  |
| Kidney disease | -0.7520 | 0.9695 | ±1.9390 | -0.776 | 0.4380 |  |
| Circulatory disease | -1.5168 | 0.9731 | ±1.9462 | -1.559 | 0.1191 |  |
| **HbA1c (%)** | **+0.5581** | 0.2566 | ±0.5131 | **+2.175** | **0.0296** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **474**, R² = **0.2017**, Adj R² = **0.1826**, F-statistic = **10.61** (p = **1.79e-17**), Residual SE = **8.337** on **462** df, AIC = **3367.4**, BIC = **3417.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5827** | 4.0529 | ±8.1058 | **+18.649** | **1.28e-77** | *** |
| Education: graduate level (vs college) | -0.6493 | 0.9322 | ±1.8644 | -0.697 | 0.4861 |  |
| Education: high school or below (vs college) | +1.2508 | 1.0061 | ±2.0122 | +1.243 | 0.2138 |  |
| Site: UCSD (vs UAB) | -0.9735 | 1.0419 | ±2.0837 | -0.934 | 0.3501 |  |
| Site: UW (vs UAB) | +0.7223 | 0.9747 | ±1.9494 | +0.741 | 0.4586 |  |
| **Age (years)** | **-0.2717** | 0.0387 | ±0.0775 | **-7.012** | **2.35e-12** | *** |
| **BMI (kg/m2)** | **+0.1253** | 0.0605 | ±0.1210 | **+2.071** | **0.0384** | * |
| Hypertension | +0.0329 | 0.9106 | ±1.8211 | +0.036 | 0.9711 |  |
| High cholesterol | -0.0919 | 0.8799 | ±1.7598 | -0.104 | 0.9168 |  |
| Kidney disease | -0.8870 | 0.9723 | ±1.9446 | -0.912 | 0.3616 |  |
| Circulatory disease | -1.6908 | 0.9675 | ±1.9350 | -1.748 | 0.0805 | . |
| **Mean glucose (mg/dL)** | **+0.0253** | 0.0096 | ±0.0193 | **+2.626** | **0.0086** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **474**, R² = **0.2017**, Adj R² = **0.1826**, F-statistic = **10.61** (p = **1.79e-17**), Residual SE = **8.337** on **462** df, AIC = **3367.4**, BIC = **3417.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.0785** | 4.8289 | ±9.6578 | **+14.927** | **2.21e-50** | *** |
| Education: graduate level (vs college) | -0.6493 | 0.9322 | ±1.8644 | -0.697 | 0.4861 |  |
| Education: high school or below (vs college) | +1.2508 | 1.0061 | ±2.0122 | +1.243 | 0.2138 |  |
| Site: UCSD (vs UAB) | -0.9735 | 1.0419 | ±2.0837 | -0.934 | 0.3501 |  |
| Site: UW (vs UAB) | +0.7223 | 0.9747 | ±1.9494 | +0.741 | 0.4586 |  |
| **Age (years)** | **-0.2717** | 0.0387 | ±0.0775 | **-7.012** | **2.35e-12** | *** |
| **BMI (kg/m2)** | **+0.1253** | 0.0605 | ±0.1210 | **+2.071** | **0.0384** | * |
| Hypertension | +0.0329 | 0.9106 | ±1.8211 | +0.036 | 0.9711 |  |
| High cholesterol | -0.0919 | 0.8799 | ±1.7598 | -0.104 | 0.9168 |  |
| Kidney disease | -0.8870 | 0.9723 | ±1.9446 | -0.912 | 0.3616 |  |
| Circulatory disease | -1.6908 | 0.9675 | ±1.9350 | -1.748 | 0.0805 | . |
| **GMI (%)** | **+1.0587** | 0.4031 | ±0.8063 | **+2.626** | **0.0086** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **474**, R² = **0.2010**, Adj R² = **0.1819**, F-statistic = **10.56** (p = **2.15e-17**), Residual SE = **8.341** on **462** df, AIC = **3367.8**, BIC = **3417.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.0879** | 3.9802 | ±7.9604 | **+19.117** | **1.84e-81** | *** |
| Education: graduate level (vs college) | -0.6293 | 0.9373 | ±1.8746 | -0.671 | 0.5020 |  |
| Education: high school or below (vs college) | +1.2776 | 1.0015 | ±2.0031 | +1.276 | 0.2021 |  |
| Site: UCSD (vs UAB) | -0.9602 | 1.0427 | ±2.0854 | -0.921 | 0.3571 |  |
| Site: UW (vs UAB) | +0.6376 | 0.9707 | ±1.9414 | +0.657 | 0.5113 |  |
| **Age (years)** | **-0.2688** | 0.0390 | ±0.0781 | **-6.885** | **5.79e-12** | *** |
| **BMI (kg/m2)** | **+0.1191** | 0.0606 | ±0.1212 | **+1.966** | **0.0493** | * |
| Hypertension | +0.0446 | 0.9103 | ±1.8207 | +0.049 | 0.9610 |  |
| High cholesterol | -0.0654 | 0.8831 | ±1.7662 | -0.074 | 0.9410 |  |
| Kidney disease | -0.8122 | 0.9749 | ±1.9498 | -0.833 | 0.4048 |  |
| Circulatory disease | -1.6905 | 0.9694 | ±1.9388 | -1.744 | 0.0812 | . |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0233** | 0.0092 | ±0.0185 | **+2.523** | **0.0117** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **474**, R² = **0.1909**, Adj R² = **0.1716**, F-statistic = **9.91** (p = **3.09e-16**), Residual SE = **8.393** on **462** df, AIC = **3373.8**, BIC = **3423.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.7800** | 3.7402 | ±7.4805 | **+21.063** | **1.74e-98** | *** |
| Education: graduate level (vs college) | -0.7234 | 0.9408 | ±1.8816 | -0.769 | 0.4419 |  |
| Education: high school or below (vs college) | +1.4243 | 1.0265 | ±2.0529 | +1.388 | 0.1652 |  |
| Site: UCSD (vs UAB) | -1.0595 | 1.0524 | ±2.1048 | -1.007 | 0.3140 |  |
| Site: UW (vs UAB) | +0.6848 | 0.9884 | ±1.9767 | +0.693 | 0.4884 |  |
| **Age (years)** | **-0.2777** | 0.0390 | ±0.0781 | **-7.114** | **1.12e-12** | *** |
| **BMI (kg/m2)** | **+0.1382** | 0.0605 | ±0.1210 | **+2.285** | **0.0223** | * |
| Hypertension | +0.0029 | 0.9186 | ±1.8372 | +0.003 | 0.9974 |  |
| High cholesterol | -0.1714 | 0.8858 | ±1.7716 | -0.194 | 0.8465 |  |
| Kidney disease | -0.9905 | 0.9819 | ±1.9637 | -1.009 | 0.3131 |  |
| Circulatory disease | -1.5625 | 0.9740 | ±1.9479 | -1.604 | 0.1087 |  |
| Glucose SD, pooled (mg/dL) | +0.0291 | 0.0330 | ±0.0661 | +0.880 | 0.3791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **474**, R² = **0.1901**, Adj R² = **0.1709**, F-statistic = **9.86** (p = **3.77e-16**), Residual SE = **8.397** on **462** df, AIC = **3374.2**, BIC = **3424.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0850** | 3.7881 | ±7.5761 | **+20.877** | **8.58e-97** | *** |
| Education: graduate level (vs college) | -0.7421 | 0.9396 | ±1.8791 | -0.790 | 0.4296 |  |
| Education: high school or below (vs college) | +1.4455 | 1.0283 | ±2.0565 | +1.406 | 0.1598 |  |
| Site: UCSD (vs UAB) | -1.0700 | 1.0538 | ±2.1076 | -1.015 | 0.3099 |  |
| Site: UW (vs UAB) | +0.6430 | 0.9874 | ±1.9747 | +0.651 | 0.5149 |  |
| **Age (years)** | **-0.2782** | 0.0392 | ±0.0783 | **-7.107** | **1.19e-12** | *** |
| **BMI (kg/m2)** | **+0.1411** | 0.0601 | ±0.1202 | **+2.347** | **0.0189** | * |
| Hypertension | +0.0197 | 0.9154 | ±1.8309 | +0.022 | 0.9828 |  |
| High cholesterol | -0.1916 | 0.8843 | ±1.7686 | -0.217 | 0.8284 |  |
| Kidney disease | -0.9620 | 0.9916 | ±1.9832 | -0.970 | 0.3320 |  |
| Circulatory disease | -1.5483 | 0.9737 | ±1.9475 | -1.590 | 0.1118 |  |
| Avg. daily SD (mg/dL) | +0.0231 | 0.0374 | ±0.0747 | +0.619 | 0.5359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **474**, R² = **0.1940**, Adj R² = **0.1748**, F-statistic = **10.11** (p = **1.37e-16**), Residual SE = **8.377** on **462** df, AIC = **3371.9**, BIC = **3421.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.6035** | 3.7546 | ±7.5091 | **+22.001** | **2.83e-107** | *** |
| Education: graduate level (vs college) | -0.8081 | 0.9384 | ±1.8769 | -0.861 | 0.3892 |  |
| Education: high school or below (vs college) | +1.6244 | 1.0186 | ±2.0372 | +1.595 | 0.1108 |  |
| Site: UCSD (vs UAB) | -1.1660 | 1.0450 | ±2.0900 | -1.116 | 0.2645 |  |
| Site: UW (vs UAB) | +0.3911 | 0.9799 | ±1.9598 | +0.399 | 0.6898 |  |
| **Age (years)** | **-0.2758** | 0.0395 | ±0.0790 | **-6.982** | **2.91e-12** | *** |
| **BMI (kg/m2)** | **+0.1395** | 0.0597 | ±0.1195 | **+2.335** | **0.0195** | * |
| Hypertension | +0.1084 | 0.9190 | ±1.8379 | +0.118 | 0.9061 |  |
| High cholesterol | -0.2453 | 0.8823 | ±1.7646 | -0.278 | 0.7810 |  |
| Kidney disease | -0.5706 | 1.0145 | ±2.0291 | -0.562 | 0.5738 |  |
| Circulatory disease | -1.5641 | 0.9739 | ±1.9478 | -1.606 | 0.1083 |  |
| CV (%) | -0.1138 | 0.0725 | ±0.1451 | -1.568 | 0.1168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **474**, R² = **0.1934**, Adj R² = **0.1742**, F-statistic = **10.07** (p = **1.60e-16**), Residual SE = **8.380** on **462** df, AIC = **3372.3**, BIC = **3422.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.3574** | 4.1902 | ±8.3804 | **+18.462** | **4.21e-76** | *** |
| Education: graduate level (vs college) | -0.8096 | 0.9379 | ±1.8758 | -0.863 | 0.3880 |  |
| Education: high school or below (vs college) | +1.5957 | 1.0176 | ±2.0352 | +1.568 | 0.1168 |  |
| Site: UCSD (vs UAB) | -1.1230 | 1.0425 | ±2.0850 | -1.077 | 0.2814 |  |
| Site: UW (vs UAB) | +0.4397 | 0.9767 | ±1.9535 | +0.450 | 0.6526 |  |
| **Age (years)** | **-0.2768** | 0.0393 | ±0.0787 | **-7.036** | **1.97e-12** | *** |
| **BMI (kg/m2)** | **+0.1381** | 0.0595 | ±0.1189 | **+2.323** | **0.0202** | * |
| Hypertension | +0.0806 | 0.9164 | ±1.8328 | +0.088 | 0.9299 |  |
| High cholesterol | -0.1975 | 0.8799 | ±1.7598 | -0.224 | 0.8224 |  |
| Kidney disease | -0.6242 | 1.0019 | ±2.0037 | -0.623 | 0.5332 |  |
| Circulatory disease | -1.5266 | 0.9731 | ±1.9462 | -1.569 | 0.1167 |  |
| Mean / SD ratio | +0.5904 | 0.3952 | ±0.7904 | +1.494 | 0.1352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **474**, R² = **0.1944**, Adj R² = **0.1752**, F-statistic = **10.13** (p = **1.24e-16**), Residual SE = **8.375** on **462** df, AIC = **3371.7**, BIC = **3421.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.3018** | 4.0705 | ±8.1410 | **+18.991** | **2.03e-80** | *** |
| Education: graduate level (vs college) | -0.8162 | 0.9371 | ±1.8743 | -0.871 | 0.3838 |  |
| Education: high school or below (vs college) | +1.6096 | 1.0159 | ±2.0318 | +1.584 | 0.1131 |  |
| Site: UCSD (vs UAB) | -1.1276 | 1.0438 | ±2.0877 | -1.080 | 0.2800 |  |
| Site: UW (vs UAB) | +0.4591 | 0.9724 | ±1.9447 | +0.472 | 0.6368 |  |
| **Age (years)** | **-0.2752** | 0.0393 | ±0.0786 | **-7.007** | **2.44e-12** | *** |
| **BMI (kg/m2)** | **+0.1322** | 0.0597 | ±0.1194 | **+2.216** | **0.0267** | * |
| Hypertension | +0.0697 | 0.9142 | ±1.8283 | +0.076 | 0.9392 |  |
| High cholesterol | -0.2023 | 0.8800 | ±1.7600 | -0.230 | 0.8182 |  |
| Kidney disease | -0.6191 | 1.0034 | ±2.0067 | -0.617 | 0.5372 |  |
| Circulatory disease | -1.5558 | 0.9751 | ±1.9501 | -1.596 | 0.1106 |  |
| Avg. daily mean/SD | +0.5336 | 0.3124 | ±0.6248 | +1.708 | 0.0876 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **474**, R² = **0.1970**, Adj R² = **0.1778**, F-statistic = **10.30** (p = **6.24e-17**), Residual SE = **8.361** on **462** df, AIC = **3370.2**, BIC = **3420.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.4503** | 4.3683 | ±8.7367 | **+17.272** | **7.63e-67** | *** |
| Education: graduate level (vs college) | -0.6562 | 0.9359 | ±1.8719 | -0.701 | 0.4833 |  |
| Education: high school or below (vs college) | +1.3752 | 1.0249 | ±2.0497 | +1.342 | 0.1796 |  |
| Site: UCSD (vs UAB) | -0.9423 | 1.0547 | ±2.1093 | -0.893 | 0.3716 |  |
| Site: UW (vs UAB) | +0.8758 | 0.9878 | ±1.9756 | +0.887 | 0.3753 |  |
| **Age (years)** | **-0.2700** | 0.0390 | ±0.0781 | **-6.917** | **4.61e-12** | *** |
| **BMI (kg/m2)** | **+0.1443** | 0.0606 | ±0.1212 | **+2.381** | **0.0173** | * |
| Hypertension | +0.0047 | 0.9108 | ±1.8217 | +0.005 | 0.9959 |  |
| High cholesterol | -0.1547 | 0.8787 | ±1.7574 | -0.176 | 0.8603 |  |
| Kidney disease | -1.0488 | 0.9932 | ±1.9865 | -1.056 | 0.2910 |  |
| Circulatory disease | -1.5618 | 0.9713 | ±1.9427 | -1.608 | 0.1079 |  |
| MAG (mg/dL/h) | +0.0818 | 0.0424 | ±0.0849 | +1.928 | 0.0538 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **474**, R² = **0.1901**, Adj R² = **0.1709**, F-statistic = **9.86** (p = **3.77e-16**), Residual SE = **8.397** on **462** df, AIC = **3374.2**, BIC = **3424.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.7547** | 3.9770 | ±7.9541 | **+19.802** | **2.84e-87** | *** |
| Education: graduate level (vs college) | -0.7443 | 0.9398 | ±1.8795 | -0.792 | 0.4284 |  |
| Education: high school or below (vs college) | +1.4430 | 1.0285 | ±2.0569 | +1.403 | 0.1606 |  |
| Site: UCSD (vs UAB) | -1.0618 | 1.0547 | ±2.1094 | -1.007 | 0.3140 |  |
| Site: UW (vs UAB) | +0.6446 | 0.9885 | ±1.9770 | +0.652 | 0.5143 |  |
| **Age (years)** | **-0.2773** | 0.0391 | ±0.0783 | **-7.084** | **1.40e-12** | *** |
| **BMI (kg/m2)** | **+0.1420** | 0.0601 | ±0.1201 | **+2.364** | **0.0181** | * |
| Hypertension | +0.0333 | 0.9122 | ±1.8243 | +0.036 | 0.9709 |  |
| High cholesterol | -0.2028 | 0.8836 | ±1.7672 | -0.230 | 0.8184 |  |
| Kidney disease | -0.9720 | 0.9951 | ±1.9903 | -0.977 | 0.3287 |  |
| Circulatory disease | -1.5499 | 0.9726 | ±1.9452 | -1.594 | 0.1110 |  |
| Avg. daily range (mg/dL) | +0.0069 | 0.0109 | ±0.0218 | +0.632 | 0.5277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **474**, R² = **0.1978**, Adj R² = **0.1787**, F-statistic = **10.36** (p = **4.94e-17**), Residual SE = **8.357** on **462** df, AIC = **3369.7**, BIC = **3419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.4122** | 3.5933 | ±7.1865 | **+21.822** | **1.43e-105** | *** |
| Education: graduate level (vs college) | -0.6213 | 0.9437 | ±1.8874 | -0.658 | 0.5103 |  |
| Education: high school or below (vs college) | +1.4501 | 1.0129 | ±2.0258 | +1.432 | 0.1522 |  |
| Site: UCSD (vs UAB) | -1.0837 | 1.0490 | ±2.0979 | -1.033 | 0.3015 |  |
| Site: UW (vs UAB) | +0.7743 | 0.9743 | ±1.9487 | +0.795 | 0.4268 |  |
| **Age (years)** | **-0.2703** | 0.0385 | ±0.0770 | **-7.018** | **2.25e-12** | *** |
| **BMI (kg/m2)** | **+0.1264** | 0.0604 | ±0.1209 | **+2.092** | **0.0365** | * |
| Hypertension | -0.1220 | 0.9253 | ±1.8506 | -0.132 | 0.8951 |  |
| High cholesterol | -0.0823 | 0.8870 | ±1.7740 | -0.093 | 0.9261 |  |
| Kidney disease | -0.9225 | 0.9593 | ±1.9186 | -0.962 | 0.3362 |  |
| Circulatory disease | -1.7054 | 0.9747 | ±1.9494 | -1.750 | 0.0802 | . |
| **SD of daily means (mg/dL)** | **+0.0991** | 0.0459 | ±0.0918 | **+2.160** | **0.0308** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **474**, R² = **0.2030**, Adj R² = **0.1840**, F-statistic = **10.69** (p = **1.26e-17**), Residual SE = **8.330** on **462** df, AIC = **3366.6**, BIC = **3416.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.9391** | 3.6936 | ±7.3872 | **+22.455** | **1.15e-111** | *** |
| Education: graduate level (vs college) | -0.6675 | 0.9313 | ±1.8626 | -0.717 | 0.4736 |  |
| Education: high school or below (vs college) | +1.2124 | 1.0058 | ±2.0116 | +1.205 | 0.2280 |  |
| Site: UCSD (vs UAB) | -0.9102 | 1.0466 | ±2.0931 | -0.870 | 0.3844 |  |
| Site: UW (vs UAB) | +0.7454 | 0.9739 | ±1.9478 | +0.765 | 0.4441 |  |
| **Age (years)** | **-0.2745** | 0.0387 | ±0.0775 | **-7.086** | **1.38e-12** | *** |
| **BMI (kg/m2)** | **+0.1211** | 0.0603 | ±0.1207 | **+2.006** | **0.0448** | * |
| Hypertension | +0.0588 | 0.9126 | ±1.8253 | +0.064 | 0.9487 |  |
| High cholesterol | -0.0228 | 0.8816 | ±1.7632 | -0.026 | 0.9794 |  |
| Kidney disease | -0.9176 | 0.9680 | ±1.9360 | -0.948 | 0.3432 |  |
| Circulatory disease | -1.7033 | 0.9612 | ±1.9224 | -1.772 | 0.0764 | . |
| **Time in range 70-180, pooled (%)** | **-0.0428** | 0.0156 | ±0.0313 | **-2.732** | **0.0063** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **474**, R² = **0.2026**, Adj R² = **0.1836**, F-statistic = **10.67** (p = **1.40e-17**), Residual SE = **8.332** on **462** df, AIC = **3366.9**, BIC = **3416.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.9340** | 3.6976 | ±7.3952 | **+22.429** | **2.05e-111** | *** |
| Education: graduate level (vs college) | -0.6811 | 0.9318 | ±1.8636 | -0.731 | 0.4648 |  |
| Education: high school or below (vs college) | +1.2012 | 1.0055 | ±2.0109 | +1.195 | 0.2322 |  |
| Site: UCSD (vs UAB) | -0.8970 | 1.0476 | ±2.0953 | -0.856 | 0.3919 |  |
| Site: UW (vs UAB) | +0.7455 | 0.9743 | ±1.9486 | +0.765 | 0.4442 |  |
| **Age (years)** | **-0.2752** | 0.0388 | ±0.0776 | **-7.096** | **1.28e-12** | *** |
| **BMI (kg/m2)** | **+0.1210** | 0.0605 | ±0.1210 | **+1.999** | **0.0456** | * |
| Hypertension | +0.0664 | 0.9127 | ±1.8253 | +0.073 | 0.9420 |  |
| High cholesterol | -0.0295 | 0.8826 | ±1.7653 | -0.033 | 0.9733 |  |
| Kidney disease | -0.9358 | 0.9690 | ±1.9380 | -0.966 | 0.3342 |  |
| Circulatory disease | -1.6980 | 0.9627 | ±1.9254 | -1.764 | 0.0778 | . |
| **Avg. daily time in range 70-180 (%)** | **-0.0418** | 0.0155 | ±0.0309 | **-2.703** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **474**, R² = **0.1896**, Adj R² = **0.1703**, F-statistic = **9.83** (p = **4.32e-16**), Residual SE = **8.400** on **462** df, AIC = **3374.5**, BIC = **3424.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.0564** | 3.6173 | ±7.2347 | **+22.131** | **1.58e-108** | *** |
| Education: graduate level (vs college) | -0.7696 | 0.9397 | ±1.8795 | -0.819 | 0.4128 |  |
| Education: high school or below (vs college) | +1.5243 | 1.0244 | ±2.0488 | +1.488 | 0.1368 |  |
| Site: UCSD (vs UAB) | -1.1272 | 1.0528 | ±2.1055 | -1.071 | 0.2843 |  |
| Site: UW (vs UAB) | +0.5549 | 0.9729 | ±1.9457 | +0.570 | 0.5684 |  |
| **Age (years)** | **-0.2789** | 0.0392 | ±0.0785 | **-7.110** | **1.16e-12** | *** |
| **BMI (kg/m2)** | **+0.1411** | 0.0601 | ±0.1202 | **+2.348** | **0.0189** | * |
| Hypertension | +0.0519 | 0.9267 | ±1.8535 | +0.056 | 0.9553 |  |
| High cholesterol | -0.2282 | 0.8877 | ±1.7754 | -0.257 | 0.7971 |  |
| Kidney disease | -0.8582 | 0.9746 | ±1.9491 | -0.881 | 0.3785 |  |
| Circulatory disease | -1.5140 | 0.9747 | ±1.9494 | -1.553 | 0.1204 |  |
| Any reading < 54 during wear (0/1) | -0.2888 | 0.9125 | ±1.8251 | -0.316 | 0.7516 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **474**, R² = **0.1898**, Adj R² = **0.1705**, F-statistic = **9.84** (p = **4.16e-16**), Residual SE = **8.399** on **462** df, AIC = **3374.4**, BIC = **3424.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.9953** | 3.6181 | ±7.2363 | **+22.109** | **2.56e-108** | *** |
| Education: graduate level (vs college) | -0.7852 | 0.9394 | ±1.8788 | -0.836 | 0.4032 |  |
| Education: high school or below (vs college) | +1.5037 | 1.0269 | ±2.0538 | +1.464 | 0.1431 |  |
| Site: UCSD (vs UAB) | -1.1423 | 1.0539 | ±2.1079 | -1.084 | 0.2784 |  |
| Site: UW (vs UAB) | +0.5229 | 0.9808 | ±1.9616 | +0.533 | 0.5939 |  |
| **Age (years)** | **-0.2780** | 0.0393 | ±0.0786 | **-7.071** | **1.54e-12** | *** |
| **BMI (kg/m2)** | **+0.1414** | 0.0605 | ±0.1209 | **+2.339** | **0.0193** | * |
| Hypertension | +0.0755 | 0.9234 | ±1.8467 | +0.082 | 0.9348 |  |
| High cholesterol | -0.2480 | 0.8875 | ±1.7749 | -0.279 | 0.7799 |  |
| Kidney disease | -0.8547 | 0.9738 | ±1.9476 | -0.878 | 0.3801 |  |
| Circulatory disease | -1.5624 | 0.9810 | ±1.9620 | -1.593 | 0.1112 |  |
| Time < 54 (%) | -0.6227 | 1.9536 | ±3.9071 | -0.319 | 0.7499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **474**, R² = **0.1918**, Adj R² = **0.1726**, F-statistic = **9.97** (p = **2.44e-16**), Residual SE = **8.388** on **462** df, AIC = **3373.2**, BIC = **3423.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.0156** | 3.6214 | ±7.2428 | **+22.095** | **3.50e-108** | *** |
| Education: graduate level (vs college) | -0.7999 | 0.9386 | ±1.8771 | -0.852 | 0.3941 |  |
| Education: high school or below (vs college) | +1.4654 | 1.0240 | ±2.0479 | +1.431 | 0.1524 |  |
| Site: UCSD (vs UAB) | -1.1817 | 1.0526 | ±2.1051 | -1.123 | 0.2616 |  |
| Site: UW (vs UAB) | +0.4688 | 0.9768 | ±1.9536 | +0.480 | 0.6313 |  |
| **Age (years)** | **-0.2779** | 0.0394 | ±0.0787 | **-7.061** | **1.65e-12** | *** |
| **BMI (kg/m2)** | **+0.1426** | 0.0606 | ±0.1213 | **+2.351** | **0.0187** | * |
| Hypertension | +0.1174 | 0.9151 | ±1.8302 | +0.128 | 0.8979 |  |
| High cholesterol | -0.2911 | 0.8843 | ±1.7686 | -0.329 | 0.7420 |  |
| Kidney disease | -0.8298 | 0.9768 | ±1.9536 | -0.850 | 0.3956 |  |
| Circulatory disease | -1.5892 | 0.9774 | ±1.9547 | -1.626 | 0.1039 |  |
| Avg. daily time < 54 (%) | -1.2188 | 2.0617 | ±4.1235 | -0.591 | 0.5544 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **474**, R² = **0.1937**, Adj R² = **0.1745**, F-statistic = **10.09** (p = **1.47e-16**), Residual SE = **8.378** on **462** df, AIC = **3372.1**, BIC = **3422.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1826** | 3.5998 | ±7.1995 | **+22.274** | **6.53e-110** | *** |
| Education: graduate level (vs college) | -0.8493 | 0.9393 | ±1.8787 | -0.904 | 0.3659 |  |
| Education: high school or below (vs college) | +1.4974 | 1.0228 | ±2.0456 | +1.464 | 0.1432 |  |
| Site: UCSD (vs UAB) | -1.2790 | 1.0529 | ±2.1058 | -1.215 | 0.2245 |  |
| Site: UW (vs UAB) | +0.3883 | 0.9796 | ±1.9592 | +0.396 | 0.6918 |  |
| **Age (years)** | **-0.2746** | 0.0394 | ±0.0787 | **-6.976** | **3.05e-12** | *** |
| **BMI (kg/m2)** | **+0.1383** | 0.0604 | ±0.1208 | **+2.290** | **0.0220** | * |
| Hypertension | +0.1575 | 0.9136 | ±1.8273 | +0.172 | 0.8631 |  |
| High cholesterol | -0.3416 | 0.8898 | ±1.7796 | -0.384 | 0.7010 |  |
| Kidney disease | -0.8337 | 0.9784 | ±1.9568 | -0.852 | 0.3942 |  |
| Circulatory disease | -1.6703 | 0.9800 | ±1.9600 | -1.704 | 0.0883 | . |
| Time 54-69, pooled (%) | -0.6985 | 0.4398 | ±0.8795 | -1.588 | 0.1122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **474**, R² = **0.1960**, Adj R² = **0.1769**, F-statistic = **10.24** (p = **7.97e-17**), Residual SE = **8.366** on **462** df, AIC = **3370.7**, BIC = **3420.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1207** | 3.6008 | ±7.2017 | **+22.251** | **1.12e-109** | *** |
| Education: graduate level (vs college) | -0.8605 | 0.9376 | ±1.8752 | -0.918 | 0.3588 |  |
| Education: high school or below (vs college) | +1.4787 | 1.0198 | ±2.0396 | +1.450 | 0.1471 |  |
| Site: UCSD (vs UAB) | -1.3126 | 1.0519 | ±2.1037 | -1.248 | 0.2121 |  |
| Site: UW (vs UAB) | +0.3434 | 0.9774 | ±1.9548 | +0.351 | 0.7254 |  |
| **Age (years)** | **-0.2736** | 0.0394 | ±0.0788 | **-6.945** | **3.79e-12** | *** |
| **BMI (kg/m2)** | **+0.1395** | 0.0605 | ±0.1209 | **+2.308** | **0.0210** | * |
| Hypertension | +0.1902 | 0.9108 | ±1.8216 | +0.209 | 0.8346 |  |
| High cholesterol | -0.3664 | 0.8871 | ±1.7743 | -0.413 | 0.6796 |  |
| Kidney disease | -0.8169 | 0.9790 | ±1.9581 | -0.834 | 0.4040 |  |
| Circulatory disease | -1.6901 | 0.9801 | ±1.9602 | -1.724 | 0.0846 | . |
| Avg. daily time 54-69 (%) | -0.7865 | 0.4128 | ±0.8256 | -1.905 | 0.0567 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **474**, R² = **0.1929**, Adj R² = **0.1737**, F-statistic = **10.04** (p = **1.83e-16**), Residual SE = **8.383** on **462** df, AIC = **3372.6**, BIC = **3422.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1644** | 3.6111 | ±7.2222 | **+22.199** | **3.48e-109** | *** |
| Education: graduate level (vs college) | -0.8425 | 0.9396 | ±1.8792 | -0.897 | 0.3699 |  |
| Education: high school or below (vs college) | +1.4830 | 1.0237 | ±2.0474 | +1.449 | 0.1474 |  |
| Site: UCSD (vs UAB) | -1.2636 | 1.0547 | ±2.1094 | -1.198 | 0.2309 |  |
| Site: UW (vs UAB) | +0.3961 | 0.9817 | ±1.9635 | +0.403 | 0.6866 |  |
| **Age (years)** | **-0.2753** | 0.0394 | ±0.0787 | **-6.992** | **2.71e-12** | *** |
| **BMI (kg/m2)** | **+0.1391** | 0.0606 | ±0.1213 | **+2.294** | **0.0218** | * |
| Hypertension | +0.1625 | 0.9168 | ±1.8336 | +0.177 | 0.8593 |  |
| High cholesterol | -0.3347 | 0.8909 | ±1.7818 | -0.376 | 0.7072 |  |
| Kidney disease | -0.8370 | 0.9776 | ±1.9552 | -0.856 | 0.3919 |  |
| Circulatory disease | -1.6609 | 0.9804 | ±1.9608 | -1.694 | 0.0902 | . |
| Time < 70 (%) | -0.5190 | 0.3577 | ±0.7153 | -1.451 | 0.1467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **474**, R² = **0.1956**, Adj R² = **0.1764**, F-statistic = **10.21** (p = **9.00e-17**), Residual SE = **8.369** on **462** df, AIC = **3371.0**, BIC = **3420.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1127** | 3.6113 | ±7.2225 | **+22.184** | **4.89e-109** | *** |
| Education: graduate level (vs college) | -0.8534 | 0.9377 | ±1.8754 | -0.910 | 0.3628 |  |
| Education: high school or below (vs college) | +1.4593 | 1.0204 | ±2.0407 | +1.430 | 0.1527 |  |
| Site: UCSD (vs UAB) | -1.2987 | 1.0529 | ±2.1058 | -1.233 | 0.2174 |  |
| Site: UW (vs UAB) | +0.3494 | 0.9777 | ±1.9554 | +0.357 | 0.7208 |  |
| **Age (years)** | **-0.2745** | 0.0394 | ±0.0787 | **-6.977** | **3.02e-12** | *** |
| **BMI (kg/m2)** | **+0.1405** | 0.0607 | ±0.1214 | **+2.316** | **0.0206** | * |
| Hypertension | +0.1937 | 0.9125 | ±1.8251 | +0.212 | 0.8319 |  |
| High cholesterol | -0.3658 | 0.8874 | ±1.7748 | -0.412 | 0.6802 |  |
| Kidney disease | -0.8131 | 0.9779 | ±1.9558 | -0.832 | 0.4057 |  |
| Circulatory disease | -1.6798 | 0.9794 | ±1.9588 | -1.715 | 0.0863 | . |
| **Avg. daily time < 70 (%)** | **-0.5947** | 0.2979 | ±0.5957 | **-1.997** | **0.0459** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **474**, R² = **0.1946**, Adj R² = **0.1754**, F-statistic = **10.15** (p = **1.17e-16**), Residual SE = **8.374** on **462** df, AIC = **3371.6**, BIC = **3421.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.0088** | 3.9383 | ±7.8767 | **+21.077** | **1.29e-98** | *** |
| Education: graduate level (vs college) | -0.6367 | 0.9404 | ±1.8807 | -0.677 | 0.4984 |  |
| Education: high school or below (vs college) | +1.3754 | 1.0117 | ±2.0235 | +1.359 | 0.1740 |  |
| Site: UCSD (vs UAB) | -1.0375 | 1.0465 | ±2.0930 | -0.991 | 0.3215 |  |
| Site: UW (vs UAB) | +0.7346 | 0.9831 | ±1.9661 | +0.747 | 0.4549 |  |
| **Age (years)** | **-0.2717** | 0.0391 | ±0.0781 | **-6.954** | **3.55e-12** | *** |
| **BMI (kg/m2)** | **+0.1334** | 0.0606 | ±0.1212 | **+2.201** | **0.0277** | * |
| Hypertension | -0.0351 | 0.9159 | ±1.8319 | -0.038 | 0.9695 |  |
| High cholesterol | -0.1421 | 0.8811 | ±1.7621 | -0.161 | 0.8719 |  |
| Kidney disease | -0.9207 | 0.9740 | ±1.9481 | -0.945 | 0.3445 |  |
| Circulatory disease | -1.5935 | 0.9714 | ±1.9428 | -1.640 | 0.1009 |  |
| Time 54-250, pooled (%) | -0.0368 | 0.0222 | ±0.0445 | -1.658 | 0.0974 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **474**, R² = **0.1950**, Adj R² = **0.1758**, F-statistic = **10.17** (p = **1.05e-16**), Residual SE = **8.372** on **462** df, AIC = **3371.4**, BIC = **3421.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.2352** | 3.9647 | ±7.9294 | **+20.994** | **7.44e-98** | *** |
| Education: graduate level (vs college) | -0.6339 | 0.9397 | ±1.8793 | -0.675 | 0.5000 |  |
| Education: high school or below (vs college) | +1.3696 | 1.0118 | ±2.0236 | +1.354 | 0.1759 |  |
| Site: UCSD (vs UAB) | -1.0317 | 1.0466 | ±2.0932 | -0.986 | 0.3242 |  |
| Site: UW (vs UAB) | +0.7365 | 0.9830 | ±1.9660 | +0.749 | 0.4537 |  |
| **Age (years)** | **-0.2722** | 0.0390 | ±0.0780 | **-6.976** | **3.04e-12** | *** |
| **BMI (kg/m2)** | **+0.1328** | 0.0607 | ±0.1215 | **+2.186** | **0.0288** | * |
| Hypertension | -0.0326 | 0.9153 | ±1.8305 | -0.036 | 0.9716 |  |
| High cholesterol | -0.1379 | 0.8812 | ±1.7624 | -0.156 | 0.8757 |  |
| Kidney disease | -0.9361 | 0.9746 | ±1.9492 | -0.960 | 0.3368 |  |
| Circulatory disease | -1.6032 | 0.9720 | ±1.9439 | -1.649 | 0.0991 | . |
| Avg. daily time 54-250 (%) | -0.0387 | 0.0226 | ±0.0452 | -1.713 | 0.0866 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **474**, R² = **0.2030**, Adj R² = **0.1841**, F-statistic = **10.70** (p = **1.23e-17**), Residual SE = **8.330** on **462** df, AIC = **3366.6**, BIC = **3416.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.9918** | 3.5919 | ±7.1838 | **+21.992** | **3.46e-107** | *** |
| Education: graduate level (vs college) | -0.8674 | 0.9301 | ±1.8601 | -0.933 | 0.3510 |  |
| Education: high school or below (vs college) | +1.2876 | 1.0227 | ±2.0455 | +1.259 | 0.2080 |  |
| Site: UCSD (vs UAB) | -0.9241 | 1.0470 | ±2.0941 | -0.883 | 0.3775 |  |
| Site: UW (vs UAB) | +0.5226 | 0.9586 | ±1.9172 | +0.545 | 0.5856 |  |
| **Age (years)** | **-0.2848** | 0.0394 | ±0.0787 | **-7.237** | **4.58e-13** | *** |
| **BMI (kg/m2)** | **+0.1220** | 0.0595 | ±0.1190 | **+2.050** | **0.0404** | * |
| Hypertension | +0.2256 | 0.9125 | ±1.8251 | +0.247 | 0.8047 |  |
| High cholesterol | -0.0451 | 0.8823 | ±1.7647 | -0.051 | 0.9592 |  |
| Kidney disease | -0.8327 | 0.9633 | ±1.9265 | -0.865 | 0.3873 |  |
| Circulatory disease | -1.7191 | 0.9589 | ±1.9178 | -1.793 | 0.0730 | . |
| **Time 181-250, pooled (%)** | **+0.0745** | 0.0257 | ±0.0515 | **+2.893** | **0.0038** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **474**, R² = **0.2020**, Adj R² = **0.1830**, F-statistic = **10.63** (p = **1.64e-17**), Residual SE = **8.335** on **462** df, AIC = **3367.2**, BIC = **3417.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0111** | 3.5958 | ±7.1915 | **+21.973** | **5.17e-107** | *** |
| Education: graduate level (vs college) | -0.8739 | 0.9320 | ±1.8639 | -0.938 | 0.3484 |  |
| Education: high school or below (vs college) | +1.2664 | 1.0195 | ±2.0389 | +1.242 | 0.2142 |  |
| Site: UCSD (vs UAB) | -0.9107 | 1.0485 | ±2.0970 | -0.869 | 0.3851 |  |
| Site: UW (vs UAB) | +0.5417 | 0.9603 | ±1.9207 | +0.564 | 0.5727 |  |
| **Age (years)** | **-0.2837** | 0.0393 | ±0.0787 | **-7.215** | **5.40e-13** | *** |
| **BMI (kg/m2)** | **+0.1226** | 0.0597 | ±0.1194 | **+2.055** | **0.0399** | * |
| Hypertension | +0.2188 | 0.9135 | ±1.8271 | +0.240 | 0.8107 |  |
| High cholesterol | -0.0609 | 0.8838 | ±1.7677 | -0.069 | 0.9450 |  |
| Kidney disease | -0.8436 | 0.9642 | ±1.9285 | -0.875 | 0.3816 |  |
| Circulatory disease | -1.6939 | 0.9619 | ±1.9237 | -1.761 | 0.0782 | . |
| **Avg. daily time 181-250 (%)** | **+0.0700** | 0.0250 | ±0.0499 | **+2.806** | **0.0050** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **474**, R² = **0.2033**, Adj R² = **0.1844**, F-statistic = **10.72** (p = **1.14e-17**), Residual SE = **8.328** on **462** df, AIC = **3366.4**, BIC = **3416.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.6744** | 3.6258 | ±7.2516 | **+21.699** | **2.12e-104** | *** |
| Education: graduate level (vs college) | -0.6730 | 0.9307 | ±1.8614 | -0.723 | 0.4696 |  |
| Education: high school or below (vs college) | +1.2065 | 1.0056 | ±2.0112 | +1.200 | 0.2302 |  |
| Site: UCSD (vs UAB) | -0.9219 | 1.0458 | ±2.0917 | -0.881 | 0.3780 |  |
| Site: UW (vs UAB) | +0.7321 | 0.9726 | ±1.9451 | +0.753 | 0.4516 |  |
| **Age (years)** | **-0.2743** | 0.0387 | ±0.0775 | **-7.078** | **1.46e-12** | *** |
| **BMI (kg/m2)** | **+0.1207** | 0.0604 | ±0.1208 | **+1.999** | **0.0456** | * |
| Hypertension | +0.0699 | 0.9120 | ±1.8240 | +0.077 | 0.9389 |  |
| High cholesterol | -0.0312 | 0.8808 | ±1.7616 | -0.035 | 0.9717 |  |
| Kidney disease | -0.9162 | 0.9682 | ±1.9365 | -0.946 | 0.3440 |  |
| Circulatory disease | -1.7151 | 0.9612 | ±1.9224 | -1.784 | 0.0744 | . |
| **Time > 180 (%)** | **+0.0430** | 0.0154 | ±0.0309 | **+2.785** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **474**, R² = **0.2033**, Adj R² = **0.1843**, F-statistic = **10.72** (p = **1.16e-17**), Residual SE = **8.328** on **462** df, AIC = **3366.5**, BIC = **3416.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.7428** | 3.6283 | ±7.2565 | **+21.703** | **1.94e-104** | *** |
| Education: graduate level (vs college) | -0.6855 | 0.9311 | ±1.8623 | -0.736 | 0.4616 |  |
| Education: high school or below (vs college) | +1.1894 | 1.0048 | ±2.0097 | +1.184 | 0.2365 |  |
| Site: UCSD (vs UAB) | -0.9064 | 1.0469 | ±2.0937 | -0.866 | 0.3866 |  |
| Site: UW (vs UAB) | +0.7332 | 0.9729 | ±1.9458 | +0.754 | 0.4510 |  |
| **Age (years)** | **-0.2749** | 0.0388 | ±0.0776 | **-7.088** | **1.36e-12** | *** |
| **BMI (kg/m2)** | **+0.1205** | 0.0606 | ±0.1211 | **+1.989** | **0.0467** | * |
| Hypertension | +0.0788 | 0.9119 | ±1.8238 | +0.086 | 0.9311 |  |
| High cholesterol | -0.0363 | 0.8818 | ±1.7636 | -0.041 | 0.9672 |  |
| Kidney disease | -0.9341 | 0.9691 | ±1.9382 | -0.964 | 0.3351 |  |
| Circulatory disease | -1.7121 | 0.9627 | ±1.9254 | -1.778 | 0.0753 | . |
| **Avg. daily time > 180 (%)** | **+0.0426** | 0.0153 | ±0.0306 | **+2.789** | **0.0053** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **474**, R² = **0.2000**, Adj R² = **0.1809**, F-statistic = **10.50** (p = **2.80e-17**), Residual SE = **8.346** on **462** df, AIC = **3368.4**, BIC = **3418.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.1473** | 3.6161 | ±7.2323 | **+21.887** | **3.44e-106** | *** |
| Education: graduate level (vs college) | -0.6303 | 0.9401 | ±1.8801 | -0.670 | 0.5026 |  |
| Education: high school or below (vs college) | +1.2867 | 1.0025 | ±2.0050 | +1.283 | 0.1993 |  |
| Site: UCSD (vs UAB) | -0.9241 | 1.0475 | ±2.0951 | -0.882 | 0.3777 |  |
| Site: UW (vs UAB) | +0.6626 | 0.9693 | ±1.9386 | +0.684 | 0.4943 |  |
| **Age (years)** | **-0.2712** | 0.0391 | ±0.0782 | **-6.933** | **4.13e-12** | *** |
| BMI (kg/m2) | +0.1167 | 0.0606 | ±0.1212 | +1.925 | 0.0542 | . |
| Hypertension | +0.0399 | 0.9136 | ±1.8271 | +0.044 | 0.9651 |  |
| High cholesterol | +0.0014 | 0.8832 | ±1.7665 | +0.002 | 0.9987 |  |
| Kidney disease | -0.8842 | 0.9691 | ±1.9382 | -0.912 | 0.3615 |  |
| Circulatory disease | -1.6971 | 0.9634 | ±1.9268 | -1.762 | 0.0781 | . |
| **Nocturnal time > 180 (%)** | **+0.0333** | 0.0137 | ±0.0273 | **+2.436** | **0.0148** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **474**, R² = **0.1946**, Adj R² = **0.1755**, F-statistic = **10.15** (p = **1.16e-16**), Residual SE = **8.374** on **462** df, AIC = **3371.6**, BIC = **3421.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.3252** | 3.6424 | ±7.2848 | **+21.778** | **3.74e-105** | *** |
| Education: graduate level (vs college) | -0.6373 | 0.9403 | ±1.8805 | -0.678 | 0.4979 |  |
| Education: high school or below (vs college) | +1.3732 | 1.0117 | ±2.0234 | +1.357 | 0.1747 |  |
| Site: UCSD (vs UAB) | -1.0393 | 1.0465 | ±2.0930 | -0.993 | 0.3206 |  |
| Site: UW (vs UAB) | +0.7324 | 0.9827 | ±1.9655 | +0.745 | 0.4561 |  |
| **Age (years)** | **-0.2716** | 0.0391 | ±0.0781 | **-6.952** | **3.60e-12** | *** |
| **BMI (kg/m2)** | **+0.1333** | 0.0606 | ±0.1212 | **+2.200** | **0.0278** | * |
| Hypertension | -0.0326 | 0.9157 | ±1.8314 | -0.036 | 0.9716 |  |
| High cholesterol | -0.1436 | 0.8810 | ±1.7620 | -0.163 | 0.8705 |  |
| Kidney disease | -0.9207 | 0.9740 | ±1.9481 | -0.945 | 0.3445 |  |
| Circulatory disease | -1.5956 | 0.9714 | ±1.9428 | -1.643 | 0.1005 |  |
| Time > 250 (%) | +0.0370 | 0.0222 | ±0.0443 | +1.668 | 0.0954 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 474)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **474**, R² = **0.1951**, Adj R² = **0.1760**, F-statistic = **10.18** (p = **1.01e-16**), Residual SE = **8.371** on **462** df, AIC = **3371.3**, BIC = **3421.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.3614** | 3.6439 | ±7.2878 | **+21.779** | **3.65e-105** | *** |
| Education: graduate level (vs college) | -0.6331 | 0.9395 | ±1.8791 | -0.674 | 0.5004 |  |
| Education: high school or below (vs college) | +1.3653 | 1.0116 | ±2.0232 | +1.350 | 0.1771 |  |
| Site: UCSD (vs UAB) | -1.0331 | 1.0465 | ±2.0931 | -0.987 | 0.3236 |  |
| Site: UW (vs UAB) | +0.7355 | 0.9827 | ±1.9654 | +0.748 | 0.4542 |  |
| **Age (years)** | **-0.2721** | 0.0390 | ±0.0780 | **-6.973** | **3.10e-12** | *** |
| **BMI (kg/m2)** | **+0.1327** | 0.0608 | ±0.1216 | **+2.184** | **0.0290** | * |
| Hypertension | -0.0306 | 0.9150 | ±1.8300 | -0.033 | 0.9733 |  |
| High cholesterol | -0.1391 | 0.8811 | ±1.7621 | -0.158 | 0.8745 |  |
| Kidney disease | -0.9362 | 0.9746 | ±1.9492 | -0.961 | 0.3367 |  |
| Circulatory disease | -1.6060 | 0.9720 | ±1.9440 | -1.652 | 0.0985 | . |
| Avg. daily time > 250 (%) | +0.0392 | 0.0226 | ±0.0451 | +1.738 | 0.0823 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 479; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **479**, R² = **0.0520**, Adj R² = **0.0318**, F-statistic = **2.57** (p = **0.0049**), Residual SE = **66.480** on **468** df, AIC = **5390.8**, BIC = **5436.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+357.6747** | 25.1344 | ±50.2689 | **+14.230** | **5.93e-46** | *** |
| Education: graduate level (vs college) | -2.7909 | 7.4066 | ±14.8133 | -0.377 | 0.7063 |  |
| Education: high school or below (vs college) | -10.8160 | 8.2446 | ±16.4891 | -1.312 | 0.1896 |  |
| **Site: UCSD (vs UAB)** | **-18.6024** | 7.0133 | ±14.0266 | **-2.652** | **0.0080** | ** |
| Site: UW (vs UAB) | +2.7241 | 8.3553 | ±16.7105 | +0.326 | 0.7444 |  |
| Age (years) | +0.5252 | 0.3037 | ±0.6075 | +1.729 | 0.0838 | . |
| **BMI (kg/m2)** | **-0.9236** | 0.4101 | ±0.8201 | **-2.252** | **0.0243** | * |
| Hypertension | -13.3118 | 6.8628 | ±13.7255 | -1.940 | 0.0524 | . |
| High cholesterol | +2.6978 | 6.4070 | ±12.8141 | +0.421 | 0.6737 |  |
| Kidney disease | +5.3090 | 8.0156 | ±16.0311 | +0.662 | 0.5078 |  |
| Circulatory disease | +12.5842 | 8.3833 | ±16.7667 | +1.501 | 0.1333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **479**, R² = **0.0539**, Adj R² = **0.0316**, F-statistic = **2.42** (p = **0.0062**), Residual SE = **66.486** on **467** df, AIC = **5391.9**, BIC = **5442.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.7371** | 28.6510 | ±57.3020 | **+13.010** | **1.08e-38** | *** |
| Education: graduate level (vs college) | -3.2803 | 7.4487 | ±14.8974 | -0.440 | 0.6597 |  |
| Education: high school or below (vs college) | -10.0765 | 8.1610 | ±16.3220 | -1.235 | 0.2169 |  |
| **Site: UCSD (vs UAB)** | **-18.8209** | 7.0193 | ±14.0386 | **-2.681** | **0.0073** | ** |
| Site: UW (vs UAB) | +2.2639 | 8.3539 | ±16.7078 | +0.271 | 0.7864 |  |
| Age (years) | +0.5086 | 0.3042 | ±0.6084 | +1.672 | 0.0945 | . |
| **BMI (kg/m2)** | **-0.8598** | 0.4219 | ±0.8439 | **-2.038** | **0.0416** | * |
| Hypertension | -13.1550 | 6.8604 | ±13.7208 | -1.918 | 0.0552 | . |
| High cholesterol | +2.5020 | 6.4152 | ±12.8305 | +0.390 | 0.6965 |  |
| Kidney disease | +4.9094 | 8.0115 | ±16.0231 | +0.613 | 0.5400 |  |
| Circulatory disease | +12.5516 | 8.3509 | ±16.7019 | +1.503 | 0.1328 |  |
| HbA1c (%) | -2.1960 | 1.9704 | ±3.9408 | -1.114 | 0.2651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **479**, R² = **0.0525**, Adj R² = **0.0302**, F-statistic = **2.35** (p = **0.0079**), Residual SE = **66.534** on **467** df, AIC = **5392.6**, BIC = **5442.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+351.2729** | 27.5675 | ±55.1350 | **+12.742** | **3.44e-37** | *** |
| Education: graduate level (vs college) | -2.5768 | 7.4454 | ±14.8909 | -0.346 | 0.7293 |  |
| Education: high school or below (vs college) | -11.1268 | 8.2441 | ±16.4883 | -1.350 | 0.1771 |  |
| **Site: UCSD (vs UAB)** | **-18.4042** | 7.0471 | ±14.0941 | **-2.612** | **0.0090** | ** |
| Site: UW (vs UAB) | +2.9312 | 8.3541 | ±16.7082 | +0.351 | 0.7257 |  |
| Age (years) | +0.5338 | 0.3043 | ±0.6085 | +1.754 | 0.0794 | . |
| **BMI (kg/m2)** | **-0.9475** | 0.4162 | ±0.8325 | **-2.276** | **0.0228** | * |
| Hypertension | -13.2950 | 6.8789 | ±13.7579 | -1.933 | 0.0533 | . |
| High cholesterol | +2.8667 | 6.4144 | ±12.8288 | +0.447 | 0.6549 |  |
| Kidney disease | +5.2360 | 8.0220 | ±16.0439 | +0.653 | 0.5139 |  |
| Circulatory disease | +12.3464 | 8.4183 | ±16.8366 | +1.467 | 0.1425 |  |
| Mean glucose (mg/dL) | +0.0376 | 0.0759 | ±0.1519 | +0.495 | 0.6203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **479**, R² = **0.0525**, Adj R² = **0.0302**, F-statistic = **2.35** (p = **0.0079**), Residual SE = **66.534** on **467** df, AIC = **5392.6**, BIC = **5442.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+346.0677** | 33.3068 | ±66.6137 | **+10.390** | **2.75e-25** | *** |
| Education: graduate level (vs college) | -2.5768 | 7.4454 | ±14.8909 | -0.346 | 0.7293 |  |
| Education: high school or below (vs college) | -11.1268 | 8.2441 | ±16.4883 | -1.350 | 0.1771 |  |
| **Site: UCSD (vs UAB)** | **-18.4042** | 7.0471 | ±14.0941 | **-2.612** | **0.0090** | ** |
| Site: UW (vs UAB) | +2.9312 | 8.3541 | ±16.7082 | +0.351 | 0.7257 |  |
| Age (years) | +0.5338 | 0.3043 | ±0.6085 | +1.754 | 0.0794 | . |
| **BMI (kg/m2)** | **-0.9475** | 0.4162 | ±0.8325 | **-2.276** | **0.0228** | * |
| Hypertension | -13.2950 | 6.8789 | ±13.7579 | -1.933 | 0.0533 | . |
| High cholesterol | +2.8667 | 6.4144 | ±12.8288 | +0.447 | 0.6549 |  |
| Kidney disease | +5.2360 | 8.0220 | ±16.0439 | +0.653 | 0.5139 |  |
| Circulatory disease | +12.3464 | 8.4183 | ±16.8366 | +1.467 | 0.1425 |  |
| GMI (%) | +1.5726 | 3.1743 | ±6.3487 | +0.495 | 0.6203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **479**, R² = **0.0534**, Adj R² = **0.0311**, F-statistic = **2.40** (p = **0.0068**), Residual SE = **66.503** on **467** df, AIC = **5392.2**, BIC = **5442.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+347.8926** | 26.9922 | ±53.9844 | **+12.889** | **5.22e-38** | *** |
| Education: graduate level (vs college) | -2.3897 | 7.4457 | ±14.8914 | -0.321 | 0.7483 |  |
| Education: high school or below (vs college) | -11.3046 | 8.2476 | ±16.4952 | -1.371 | 0.1705 |  |
| **Site: UCSD (vs UAB)** | **-18.2033** | 7.0678 | ±14.1357 | **-2.576** | **0.0100** | * |
| Site: UW (vs UAB) | +2.8710 | 8.3494 | ±16.6988 | +0.344 | 0.7310 |  |
| Age (years) | +0.5478 | 0.3038 | ±0.6077 | +1.803 | 0.0714 | . |
| **BMI (kg/m2)** | **-0.9786** | 0.4215 | ±0.8429 | **-2.322** | **0.0202** | * |
| Hypertension | -13.2313 | 6.8785 | ±13.7570 | -1.924 | 0.0544 | . |
| High cholesterol | +3.0505 | 6.4313 | ±12.8626 | +0.474 | 0.6353 |  |
| Kidney disease | +5.3343 | 8.0025 | ±16.0049 | +0.667 | 0.5050 |  |
| Circulatory disease | +12.1699 | 8.4241 | ±16.8483 | +1.445 | 0.1486 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0594 | 0.0726 | ±0.1453 | +0.818 | 0.4135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **479**, R² = **0.0532**, Adj R² = **0.0309**, F-statistic = **2.39** (p = **0.0070**), Residual SE = **66.508** on **467** df, AIC = **5392.2**, BIC = **5442.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.2047** | 26.8068 | ±53.6135 | **+13.624** | **2.90e-42** | *** |
| Education: graduate level (vs college) | -3.1478 | 7.4603 | ±14.9206 | -0.422 | 0.6731 |  |
| Education: high school or below (vs college) | -10.1569 | 8.2255 | ±16.4511 | -1.235 | 0.2169 |  |
| **Site: UCSD (vs UAB)** | **-18.9060** | 7.0288 | ±14.0575 | **-2.690** | **0.0071** | ** |
| Site: UW (vs UAB) | +1.9575 | 8.4278 | ±16.8556 | +0.232 | 0.8163 |  |
| Age (years) | +0.5230 | 0.3035 | ±0.6070 | +1.723 | 0.0849 | . |
| **BMI (kg/m2)** | **-0.8954** | 0.4165 | ±0.8329 | **-2.150** | **0.0316** | * |
| Hypertension | -13.1633 | 6.8761 | ±13.7523 | -1.914 | 0.0556 | . |
| High cholesterol | +2.4043 | 6.3966 | ±12.7931 | +0.376 | 0.7070 |  |
| Kidney disease | +6.1884 | 8.2916 | ±16.5831 | +0.746 | 0.4555 |  |
| Circulatory disease | +12.7752 | 8.3422 | ±16.6844 | +1.531 | 0.1257 |  |
| Glucose SD, pooled (mg/dL) | -0.1953 | 0.2400 | ±0.4799 | -0.814 | 0.4157 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **479**, R² = **0.0527**, Adj R² = **0.0304**, F-statistic = **2.36** (p = **0.0077**), Residual SE = **66.529** on **467** df, AIC = **5392.5**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+363.4611** | 27.1004 | ±54.2007 | **+13.412** | **5.17e-41** | *** |
| Education: graduate level (vs college) | -3.0151 | 7.4454 | ±14.8908 | -0.405 | 0.6855 |  |
| Education: high school or below (vs college) | -10.2641 | 8.2533 | ±16.5067 | -1.244 | 0.2136 |  |
| **Site: UCSD (vs UAB)** | **-18.8366** | 7.0351 | ±14.0703 | **-2.678** | **0.0074** | ** |
| Site: UW (vs UAB) | +2.2173 | 8.4400 | ±16.8799 | +0.263 | 0.7928 |  |
| Age (years) | +0.5261 | 0.3038 | ±0.6076 | +1.732 | 0.0833 | . |
| **BMI (kg/m2)** | **-0.9160** | 0.4129 | ±0.8258 | **-2.219** | **0.0265** | * |
| Hypertension | -13.2540 | 6.8705 | ±13.7410 | -1.929 | 0.0537 | . |
| High cholesterol | +2.5244 | 6.3921 | ±12.7841 | +0.395 | 0.6929 |  |
| Kidney disease | +6.0292 | 8.2793 | ±16.5586 | +0.728 | 0.4665 |  |
| Circulatory disease | +12.6929 | 8.3568 | ±16.7137 | +1.519 | 0.1288 |  |
| Avg. daily SD (mg/dL) | -0.1620 | 0.2699 | ±0.5398 | -0.600 | 0.5485 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **479**, R² = **0.0537**, Adj R² = **0.0315**, F-statistic = **2.41** (p = **0.0064**), Residual SE = **66.491** on **467** df, AIC = **5392.0**, BIC = **5442.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+369.4065** | 28.3347 | ±56.6694 | **+13.037** | **7.51e-39** | *** |
| Education: graduate level (vs college) | -2.9948 | 7.4201 | ±14.8401 | -0.404 | 0.6865 |  |
| Education: high school or below (vs college) | -10.3410 | 8.2619 | ±16.5238 | -1.252 | 0.2107 |  |
| **Site: UCSD (vs UAB)** | **-18.8220** | 7.0156 | ±14.0312 | **-2.683** | **0.0073** | ** |
| Site: UW (vs UAB) | +1.9113 | 8.4364 | ±16.8729 | +0.227 | 0.8208 |  |
| Age (years) | +0.5366 | 0.3032 | ±0.6065 | +1.770 | 0.0768 | . |
| **BMI (kg/m2)** | **-0.9234** | 0.4128 | ±0.8255 | **-2.237** | **0.0253** | * |
| Hypertension | -13.0021 | 6.8976 | ±13.7952 | -1.885 | 0.0594 | . |
| High cholesterol | +2.5628 | 6.4013 | ±12.8026 | +0.400 | 0.6889 |  |
| Kidney disease | +6.5304 | 8.3749 | ±16.7498 | +0.780 | 0.4355 |  |
| Circulatory disease | +12.4202 | 8.3528 | ±16.7056 | +1.487 | 0.1370 |  |
| CV (%) | -0.5111 | 0.5485 | ±1.0970 | -0.932 | 0.3515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **479**, R² = **0.0557**, Adj R² = **0.0335**, F-statistic = **2.51** (p = **0.0045**), Residual SE = **66.421** on **467** df, AIC = **5391.0**, BIC = **5441.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+338.5529** | 28.4987 | ±56.9973 | **+11.880** | **1.51e-32** | *** |
| Education: graduate level (vs college) | -3.1392 | 7.4122 | ±14.8244 | -0.424 | 0.6719 |  |
| Education: high school or below (vs college) | -10.1925 | 8.2496 | ±16.4992 | -1.236 | 0.2166 |  |
| **Site: UCSD (vs UAB)** | **-18.6674** | 6.9944 | ±13.9888 | **-2.669** | **0.0076** | ** |
| Site: UW (vs UAB) | +1.7596 | 8.4393 | ±16.8787 | +0.209 | 0.8348 |  |
| Age (years) | +0.5386 | 0.3032 | ±0.6064 | +1.776 | 0.0757 | . |
| **BMI (kg/m2)** | **-0.9337** | 0.4142 | ±0.8284 | **-2.254** | **0.0242** | * |
| Hypertension | -13.0234 | 6.8754 | ±13.7508 | -1.894 | 0.0582 | . |
| High cholesterol | +2.8747 | 6.4028 | ±12.8056 | +0.449 | 0.6535 |  |
| Kidney disease | +6.8619 | 8.2905 | ±16.5810 | +0.828 | 0.4078 |  |
| Circulatory disease | +12.5794 | 8.3171 | ±16.6341 | +1.512 | 0.1304 |  |
| Mean / SD ratio | +4.2546 | 3.0129 | ±6.0258 | +1.412 | 0.1579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **479**, R² = **0.0542**, Adj R² = **0.0319**, F-statistic = **2.43** (p = **0.0060**), Residual SE = **66.476** on **467** df, AIC = **5391.8**, BIC = **5441.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+344.4441** | 27.6556 | ±55.3113 | **+12.455** | **1.32e-35** | *** |
| Education: graduate level (vs college) | -3.0689 | 7.4063 | ±14.8125 | -0.414 | 0.6786 |  |
| Education: high school or below (vs college) | -10.3482 | 8.2658 | ±16.5316 | -1.252 | 0.2106 |  |
| **Site: UCSD (vs UAB)** | **-18.6213** | 7.0112 | ±14.0225 | **-2.656** | **0.0079** | ** |
| Site: UW (vs UAB) | +2.1776 | 8.4268 | ±16.8537 | +0.258 | 0.7961 |  |
| Age (years) | +0.5416 | 0.3036 | ±0.6073 | +1.784 | 0.0745 | . |
| **BMI (kg/m2)** | **-0.9578** | 0.4151 | ±0.8301 | **-2.308** | **0.0210** | * |
| Hypertension | -13.1589 | 6.8680 | ±13.7359 | -1.916 | 0.0554 | . |
| High cholesterol | +2.8000 | 6.4114 | ±12.8227 | +0.437 | 0.6623 |  |
| Kidney disease | +6.3821 | 8.1931 | ±16.3861 | +0.779 | 0.4360 |  |
| Circulatory disease | +12.4319 | 8.3703 | ±16.7407 | +1.485 | 0.1375 |  |
| Avg. daily mean/SD | +2.5969 | 2.3650 | ±4.7300 | +1.098 | 0.2722 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **479**, R² = **0.0650**, Adj R² = **0.0429**, F-statistic = **2.95** (p = **8.61e-04**), Residual SE = **66.095** on **467** df, AIC = **5386.3**, BIC = **5436.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.0742** | 30.8678 | ±61.7356 | **+12.961** | **2.04e-38** | *** |
| Education: graduate level (vs college) | -4.0798 | 7.4183 | ±14.8366 | -0.550 | 0.5823 |  |
| Education: high school or below (vs college) | -9.4099 | 8.1391 | ±16.2783 | -1.156 | 0.2476 |  |
| **Site: UCSD (vs UAB)** | **-19.9124** | 6.9862 | ±13.9723 | **-2.850** | **0.0044** | ** |
| Site: UW (vs UAB) | -0.0867 | 8.3286 | ±16.6572 | -0.010 | 0.9917 |  |
| Age (years) | +0.4542 | 0.3063 | ±0.6126 | +1.483 | 0.1381 |  |
| **BMI (kg/m2)** | **-0.9406** | 0.4109 | ±0.8218 | **-2.289** | **0.0221** | * |
| Hypertension | -13.0483 | 6.8132 | ±13.6264 | -1.915 | 0.0555 | . |
| High cholesterol | +2.3234 | 6.4078 | ±12.8155 | +0.363 | 0.7169 |  |
| Kidney disease | +7.0670 | 8.0936 | ±16.1873 | +0.873 | 0.3826 |  |
| Circulatory disease | +12.7577 | 8.2514 | ±16.5028 | +1.546 | 0.1221 |  |
| **MAG (mg/dL/h)** | **-0.7922** | 0.3014 | ±0.6028 | **-2.628** | **0.0086** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **479**, R² = **0.0527**, Adj R² = **0.0304**, F-statistic = **2.36** (p = **0.0076**), Residual SE = **66.526** on **467** df, AIC = **5392.5**, BIC = **5442.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+366.3154** | 28.8518 | ±57.7036 | **+12.696** | **6.19e-37** | *** |
| Education: graduate level (vs college) | -2.9982 | 7.4423 | ±14.8846 | -0.403 | 0.6870 |  |
| Education: high school or below (vs college) | -10.1876 | 8.2654 | ±16.5308 | -1.233 | 0.2177 |  |
| **Site: UCSD (vs UAB)** | **-18.8928** | 7.0364 | ±14.0727 | **-2.685** | **0.0073** | ** |
| Site: UW (vs UAB) | +2.1703 | 8.4490 | ±16.8980 | +0.257 | 0.7973 |  |
| Age (years) | +0.5192 | 0.3046 | ±0.6092 | +1.704 | 0.0883 | . |
| **BMI (kg/m2)** | **-0.9233** | 0.4123 | ±0.8247 | **-2.239** | **0.0252** | * |
| Hypertension | -13.3431 | 6.8585 | ±13.7171 | -1.945 | 0.0517 | . |
| High cholesterol | +2.6053 | 6.4053 | ±12.8105 | +0.407 | 0.6842 |  |
| Kidney disease | +6.1357 | 8.2678 | ±16.5356 | +0.742 | 0.4580 |  |
| Circulatory disease | +12.7119 | 8.3501 | ±16.7002 | +1.522 | 0.1279 |  |
| Avg. daily range (mg/dL) | -0.0513 | 0.0799 | ±0.1598 | -0.642 | 0.5206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **479**, R² = **0.0538**, Adj R² = **0.0315**, F-statistic = **2.41** (p = **0.0063**), Residual SE = **66.489** on **467** df, AIC = **5391.9**, BIC = **5442.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+362.5760** | 25.6454 | ±51.2908 | **+14.138** | **2.21e-45** | *** |
| Education: graduate level (vs college) | -3.3263 | 7.4889 | ±14.9778 | -0.444 | 0.6569 |  |
| Education: high school or below (vs college) | -10.5835 | 8.1974 | ±16.3947 | -1.291 | 0.1967 |  |
| **Site: UCSD (vs UAB)** | **-18.7450** | 7.0030 | ±14.0059 | **-2.677** | **0.0074** | ** |
| Site: UW (vs UAB) | +2.0285 | 8.3932 | ±16.7865 | +0.242 | 0.8090 |  |
| Age (years) | +0.5007 | 0.3046 | ±0.6092 | +1.644 | 0.1002 |  |
| **BMI (kg/m2)** | **-0.8688** | 0.4184 | ±0.8367 | **-2.077** | **0.0378** | * |
| Hypertension | -12.8475 | 6.9111 | ±13.8223 | -1.859 | 0.0630 | . |
| High cholesterol | +2.2806 | 6.4235 | ±12.8469 | +0.355 | 0.7226 |  |
| Kidney disease | +5.5687 | 8.1052 | ±16.2104 | +0.687 | 0.4920 |  |
| Circulatory disease | +13.1460 | 8.3506 | ±16.7012 | +1.574 | 0.1154 |  |
| SD of daily means (mg/dL) | -0.3342 | 0.3654 | ±0.7308 | -0.915 | 0.3604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **479**, R² = **0.0525**, Adj R² = **0.0302**, F-statistic = **2.35** (p = **0.0079**), Residual SE = **66.534** on **467** df, AIC = **5392.6**, BIC = **5442.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+361.9538** | 26.8894 | ±53.7789 | **+13.461** | **2.66e-41** | *** |
| Education: graduate level (vs college) | -2.6070 | 7.4348 | ±14.8695 | -0.351 | 0.7259 |  |
| Education: high school or below (vs college) | -11.1756 | 8.2632 | ±16.5264 | -1.352 | 0.1762 |  |
| **Site: UCSD (vs UAB)** | **-18.3274** | 7.0654 | ±14.1308 | **-2.594** | **0.0095** | ** |
| Site: UW (vs UAB) | +2.9586 | 8.3748 | ±16.7495 | +0.353 | 0.7239 |  |
| Age (years) | +0.5292 | 0.3045 | ±0.6089 | +1.738 | 0.0822 | . |
| **BMI (kg/m2)** | **-0.9530** | 0.4174 | ±0.8348 | **-2.283** | **0.0224** | * |
| Hypertension | -13.2517 | 6.8856 | ±13.7712 | -1.925 | 0.0543 | . |
| High cholesterol | +2.9526 | 6.4249 | ±12.8498 | +0.460 | 0.6458 |  |
| Kidney disease | +5.1974 | 8.0314 | ±16.0629 | +0.647 | 0.5175 |  |
| Circulatory disease | +12.3568 | 8.3979 | ±16.7957 | +1.471 | 0.1412 |  |
| Time in range 70-180, pooled (%) | -0.0597 | 0.1209 | ±0.2418 | -0.493 | 0.6217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **479**, R² = **0.0526**, Adj R² = **0.0303**, F-statistic = **2.36** (p = **0.0077**), Residual SE = **66.530** on **467** df, AIC = **5392.5**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+362.4303** | 26.9641 | ±53.9281 | **+13.441** | **3.47e-41** | *** |
| Education: graduate level (vs college) | -2.6077 | 7.4309 | ±14.8618 | -0.351 | 0.7256 |  |
| Education: high school or below (vs college) | -11.2393 | 8.2673 | ±16.5346 | -1.359 | 0.1740 |  |
| **Site: UCSD (vs UAB)** | **-18.2725** | 7.0765 | ±14.1530 | **-2.582** | **0.0098** | ** |
| Site: UW (vs UAB) | +2.9873 | 8.3762 | ±16.7524 | +0.357 | 0.7214 |  |
| Age (years) | +0.5287 | 0.3044 | ±0.6088 | +1.737 | 0.0824 | . |
| **BMI (kg/m2)** | **-0.9564** | 0.4171 | ±0.8343 | **-2.293** | **0.0219** | * |
| Hypertension | -13.2345 | 6.8870 | ±13.7741 | -1.922 | 0.0546 | . |
| High cholesterol | +2.9728 | 6.4198 | ±12.8396 | +0.463 | 0.6433 |  |
| Kidney disease | +5.1566 | 8.0364 | ±16.0727 | +0.642 | 0.5211 |  |
| Circulatory disease | +12.3375 | 8.3962 | ±16.7924 | +1.469 | 0.1417 |  |
| Avg. daily time in range 70-180 (%) | -0.0650 | 0.1200 | ±0.2400 | -0.542 | 0.5878 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **479**, R² = **0.0528**, Adj R² = **0.0305**, F-statistic = **2.37** (p = **0.0075**), Residual SE = **66.523** on **467** df, AIC = **5392.4**, BIC = **5442.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+359.5169** | 25.6301 | ±51.2601 | **+14.027** | **1.06e-44** | *** |
| Education: graduate level (vs college) | -2.8410 | 7.4176 | ±14.8352 | -0.383 | 0.7017 |  |
| Education: high school or below (vs college) | -10.8630 | 8.2685 | ±16.5371 | -1.314 | 0.1889 |  |
| **Site: UCSD (vs UAB)** | **-18.9225** | 7.0159 | ±14.0318 | **-2.697** | **0.0070** | ** |
| Site: UW (vs UAB) | +2.4902 | 8.3510 | ±16.7020 | +0.298 | 0.7656 |  |
| Age (years) | +0.5144 | 0.3059 | ±0.6118 | +1.681 | 0.0927 | . |
| **BMI (kg/m2)** | **-0.9282** | 0.4103 | ±0.8205 | **-2.263** | **0.0237** | * |
| Hypertension | -12.9730 | 6.9163 | ±13.8325 | -1.876 | 0.0607 | . |
| High cholesterol | +2.5328 | 6.4220 | ±12.8440 | +0.394 | 0.6933 |  |
| Kidney disease | +5.3026 | 8.0181 | ±16.0362 | +0.661 | 0.5084 |  |
| Circulatory disease | +12.8204 | 8.3908 | ±16.7817 | +1.528 | 0.1265 |  |
| Any reading < 54 during wear (0/1) | -4.5805 | 7.3130 | ±14.6260 | -0.626 | 0.5311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **479**, R² = **0.0526**, Adj R² = **0.0303**, F-statistic = **2.36** (p = **0.0077**), Residual SE = **66.529** on **467** df, AIC = **5392.5**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+358.2624** | 25.1674 | ±50.3349 | **+14.235** | **5.54e-46** | *** |
| Education: graduate level (vs college) | -2.9608 | 7.4100 | ±14.8201 | -0.400 | 0.6895 |  |
| Education: high school or below (vs college) | -11.0447 | 8.2739 | ±16.5479 | -1.335 | 0.1819 |  |
| **Site: UCSD (vs UAB)** | **-18.9470** | 7.0262 | ±14.0525 | **-2.697** | **0.0070** | ** |
| Site: UW (vs UAB) | +2.2482 | 8.3879 | ±16.7757 | +0.268 | 0.7887 |  |
| Age (years) | +0.5277 | 0.3037 | ±0.6073 | +1.738 | 0.0823 | . |
| **BMI (kg/m2)** | **-0.9235** | 0.4102 | ±0.8203 | **-2.252** | **0.0243** | * |
| Hypertension | -12.8771 | 6.9009 | ±13.8018 | -1.866 | 0.0620 | . |
| High cholesterol | +2.3897 | 6.4512 | ±12.9024 | +0.370 | 0.7111 |  |
| Kidney disease | +5.3378 | 8.0215 | ±16.0429 | +0.665 | 0.5058 |  |
| Circulatory disease | +12.2536 | 8.4024 | ±16.8048 | +1.458 | 0.1447 |  |
| Time < 54 (%) | -6.3295 | 8.7583 | ±17.5166 | -0.723 | 0.4699 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **479**, R² = **0.0520**, Adj R² = **0.0297**, F-statistic = **2.33** (p = **0.0085**), Residual SE = **66.551** on **467** df, AIC = **5392.8**, BIC = **5442.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+357.6835** | 25.1514 | ±50.3029 | **+14.221** | **6.77e-46** | *** |
| Education: graduate level (vs college) | -2.7941 | 7.4096 | ±14.8192 | -0.377 | 0.7061 |  |
| Education: high school or below (vs college) | -10.8220 | 8.2642 | ±16.5285 | -1.309 | 0.1904 |  |
| **Site: UCSD (vs UAB)** | **-18.6098** | 7.0398 | ±14.0797 | **-2.644** | **0.0082** | ** |
| Site: UW (vs UAB) | +2.7135 | 8.3917 | ±16.7835 | +0.323 | 0.7464 |  |
| Age (years) | +0.5253 | 0.3039 | ±0.6078 | +1.728 | 0.0839 | . |
| **BMI (kg/m2)** | **-0.9235** | 0.4106 | ±0.8212 | **-2.249** | **0.0245** | * |
| Hypertension | -13.3032 | 6.8890 | ±13.7781 | -1.931 | 0.0535 | . |
| High cholesterol | +2.6900 | 6.4422 | ±12.8844 | +0.418 | 0.6763 |  |
| Kidney disease | +5.3117 | 8.0303 | ±16.0606 | +0.661 | 0.5083 |  |
| Circulatory disease | +12.5779 | 8.3979 | ±16.7959 | +1.498 | 0.1342 |  |
| Avg. daily time < 54 (%) | -0.1279 | 6.5388 | ±13.0776 | -0.020 | 0.9844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **479**, R² = **0.0553**, Adj R² = **0.0331**, F-statistic = **2.49** (p = **0.0049**), Residual SE = **66.435** on **467** df, AIC = **5391.2**, BIC = **5441.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+355.9998** | 25.2853 | ±50.5706 | **+14.079** | **5.09e-45** | *** |
| Education: graduate level (vs college) | -2.2810 | 7.4116 | ±14.8232 | -0.308 | 0.7583 |  |
| Education: high school or below (vs college) | -10.7181 | 8.2361 | ±16.4721 | -1.301 | 0.1931 |  |
| **Site: UCSD (vs UAB)** | **-17.5535** | 7.0379 | ±14.0759 | **-2.494** | **0.0126** | * |
| Site: UW (vs UAB) | +3.9049 | 8.3906 | ±16.7811 | +0.465 | 0.6416 |  |
| Age (years) | +0.5050 | 0.3047 | ±0.6094 | +1.657 | 0.0975 | . |
| **BMI (kg/m2)** | **-0.9082** | 0.4105 | ±0.8210 | **-2.212** | **0.0269** | * |
| **Hypertension** | **-14.0860** | 6.9887 | ±13.9774 | **-2.016** | **0.0438** | * |
| High cholesterol | +3.5412 | 6.5240 | ±13.0480 | +0.543 | 0.5873 |  |
| Kidney disease | +5.1825 | 8.0496 | ±16.0992 | +0.644 | 0.5197 |  |
| Circulatory disease | +13.5122 | 8.4487 | ±16.8973 | +1.599 | 0.1097 |  |
| Time 54-69, pooled (%) | +4.4720 | 4.7718 | ±9.5437 | +0.937 | 0.3487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **479**, R² = **0.0557**, Adj R² = **0.0334**, F-statistic = **2.50** (p = **0.0046**), Residual SE = **66.423** on **467** df, AIC = **5391.0**, BIC = **5441.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.6059** | 25.2097 | ±50.4195 | **+14.146** | **1.99e-45** | *** |
| Education: graduate level (vs college) | -2.2938 | 7.4081 | ±14.8161 | -0.310 | 0.7568 |  |
| Education: high school or below (vs college) | -10.6306 | 8.2340 | ±16.4681 | -1.291 | 0.1967 |  |
| **Site: UCSD (vs UAB)** | **-17.5510** | 7.0383 | ±14.0765 | **-2.494** | **0.0126** | * |
| Site: UW (vs UAB) | +3.9675 | 8.3863 | ±16.7726 | +0.473 | 0.6361 |  |
| Age (years) | +0.5028 | 0.3048 | ±0.6096 | +1.650 | 0.0990 | . |
| **BMI (kg/m2)** | **-0.9184** | 0.4109 | ±0.8218 | **-2.235** | **0.0254** | * |
| **Hypertension** | **-14.1403** | 6.9798 | ±13.9596 | **-2.026** | **0.0428** | * |
| High cholesterol | +3.5531 | 6.5196 | ±13.0392 | +0.545 | 0.5858 |  |
| Kidney disease | +5.1192 | 8.0486 | ±16.0972 | +0.636 | 0.5247 |  |
| Circulatory disease | +13.4869 | 8.4385 | ±16.8771 | +1.598 | 0.1100 |  |
| Avg. daily time 54-69 (%) | +4.2701 | 3.9961 | ±7.9921 | +1.069 | 0.2853 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **479**, R² = **0.0537**, Adj R² = **0.0315**, F-statistic = **2.41** (p = **0.0064**), Residual SE = **66.491** on **467** df, AIC = **5392.0**, BIC = **5442.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.4273** | 25.2782 | ±50.5564 | **+14.100** | **3.79e-45** | *** |
| Education: graduate level (vs college) | -2.4149 | 7.4147 | ±14.8293 | -0.326 | 0.7447 |  |
| Education: high school or below (vs college) | -10.6612 | 8.2512 | ±16.5025 | -1.292 | 0.1963 |  |
| **Site: UCSD (vs UAB)** | **-17.8311** | 7.0425 | ±14.0850 | **-2.532** | **0.0113** | * |
| Site: UW (vs UAB) | +3.6295 | 8.4015 | ±16.8030 | +0.432 | 0.6657 |  |
| Age (years) | +0.5121 | 0.3045 | ±0.6089 | +1.682 | 0.0926 | . |
| **BMI (kg/m2)** | **-0.9145** | 0.4108 | ±0.8216 | **-2.226** | **0.0260** | * |
| **Hypertension** | **-13.9571** | 6.9785 | ±13.9571 | **-2.000** | **0.0455** | * |
| High cholesterol | +3.3310 | 6.5366 | ±13.0731 | +0.510 | 0.6103 |  |
| Kidney disease | +5.2213 | 8.0471 | ±16.0943 | +0.649 | 0.5164 |  |
| Circulatory disease | +13.2774 | 8.4434 | ±16.8868 | +1.573 | 0.1158 |  |
| Time < 70 (%) | +2.6689 | 3.6708 | ±7.3415 | +0.727 | 0.4672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **479**, R² = **0.0542**, Adj R² = **0.0320**, F-statistic = **2.44** (p = **0.0059**), Residual SE = **66.473** on **467** df, AIC = **5391.7**, BIC = **5441.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.8391** | 25.2057 | ±50.4115 | **+14.157** | **1.69e-45** | *** |
| Education: graduate level (vs college) | -2.4201 | 7.4089 | ±14.8178 | -0.327 | 0.7439 |  |
| Education: high school or below (vs college) | -10.5812 | 8.2454 | ±16.4908 | -1.283 | 0.1994 |  |
| **Site: UCSD (vs UAB)** | **-17.8065** | 7.0393 | ±14.0787 | **-2.530** | **0.0114** | * |
| Site: UW (vs UAB) | +3.7028 | 8.3882 | ±16.7764 | +0.441 | 0.6589 |  |
| Age (years) | +0.5110 | 0.3045 | ±0.6091 | +1.678 | 0.0933 | . |
| **BMI (kg/m2)** | **-0.9230** | 0.4112 | ±0.8225 | **-2.245** | **0.0248** | * |
| **Hypertension** | **-13.9958** | 6.9522 | ±13.9044 | **-2.013** | **0.0441** | * |
| High cholesterol | +3.3819 | 6.5142 | ±13.0283 | +0.519 | 0.6036 |  |
| Kidney disease | +5.1362 | 8.0480 | ±16.0960 | +0.638 | 0.5233 |  |
| Circulatory disease | +13.2663 | 8.4259 | ±16.8518 | +1.574 | 0.1154 |  |
| Avg. daily time < 70 (%) | +2.6165 | 2.7358 | ±5.4716 | +0.956 | 0.3389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **479**, R² = **0.0526**, Adj R² = **0.0303**, F-statistic = **2.36** (p = **0.0078**), Residual SE = **66.531** on **467** df, AIC = **5392.6**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.2953** | 29.7575 | ±59.5151 | **+12.276** | **1.22e-34** | *** |
| Education: graduate level (vs college) | -2.4583 | 7.5042 | ±15.0085 | -0.328 | 0.7432 |  |
| Education: high school or below (vs college) | -11.0814 | 8.2089 | ±16.4179 | -1.350 | 0.1770 |  |
| **Site: UCSD (vs UAB)** | **-18.4201** | 7.0414 | ±14.0827 | **-2.616** | **0.0089** | ** |
| Site: UW (vs UAB) | +3.1076 | 8.3210 | ±16.6420 | +0.373 | 0.7088 |  |
| Age (years) | +0.5410 | 0.3041 | ±0.6082 | +1.779 | 0.0752 | . |
| **BMI (kg/m2)** | **-0.9430** | 0.4139 | ±0.8279 | **-2.278** | **0.0227** | * |
| Hypertension | -13.4530 | 6.8758 | ±13.7517 | -1.957 | 0.0504 | . |
| High cholesterol | +2.8868 | 6.4285 | ±12.8570 | +0.449 | 0.6534 |  |
| Kidney disease | +5.1354 | 8.0510 | ±16.1019 | +0.638 | 0.5236 |  |
| Circulatory disease | +12.4099 | 8.4412 | ±16.8824 | +1.470 | 0.1415 |  |
| Time 54-250, pooled (%) | -0.0913 | 0.1682 | ±0.3364 | -0.543 | 0.5875 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **479**, R² = **0.0527**, Adj R² = **0.0303**, F-statistic = **2.36** (p = **0.0077**), Residual SE = **66.529** on **467** df, AIC = **5392.5**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.9416** | 30.0252 | ±60.0504 | **+12.188** | **3.61e-34** | *** |
| Education: graduate level (vs college) | -2.4477 | 7.5046 | ±15.0093 | -0.326 | 0.7443 |  |
| Education: high school or below (vs college) | -11.0947 | 8.2083 | ±16.4165 | -1.352 | 0.1765 |  |
| **Site: UCSD (vs UAB)** | **-18.4024** | 7.0445 | ±14.0890 | **-2.612** | **0.0090** | ** |
| Site: UW (vs UAB) | +3.1156 | 8.3199 | ±16.6399 | +0.374 | 0.7081 |  |
| Age (years) | +0.5397 | 0.3038 | ±0.6077 | +1.776 | 0.0757 | . |
| **BMI (kg/m2)** | **-0.9445** | 0.4138 | ±0.8277 | **-2.282** | **0.0225** | * |
| Hypertension | -13.4467 | 6.8744 | ±13.7488 | -1.956 | 0.0505 | . |
| High cholesterol | +2.8995 | 6.4263 | ±12.8525 | +0.451 | 0.6518 |  |
| Kidney disease | +5.0926 | 8.0607 | ±16.1213 | +0.632 | 0.5275 |  |
| Circulatory disease | +12.3825 | 8.4466 | ±16.8931 | +1.466 | 0.1427 |  |
| Avg. daily time 54-250 (%) | -0.0968 | 0.1703 | ±0.3406 | -0.569 | 0.5696 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **479**, R² = **0.0521**, Adj R² = **0.0297**, F-statistic = **2.33** (p = **0.0085**), Residual SE = **66.550** on **467** df, AIC = **5392.8**, BIC = **5442.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+357.3674** | 25.3858 | ±50.7716 | **+14.077** | **5.22e-45** | *** |
| Education: graduate level (vs college) | -2.8091 | 7.4305 | ±14.8610 | -0.378 | 0.7054 |  |
| Education: high school or below (vs college) | -10.9006 | 8.3468 | ±16.6935 | -1.306 | 0.1916 |  |
| **Site: UCSD (vs UAB)** | **-18.5384** | 7.0670 | ±14.1341 | **-2.623** | **0.0087** | ** |
| Site: UW (vs UAB) | +2.7097 | 8.3609 | ±16.7218 | +0.324 | 0.7459 |  |
| Age (years) | +0.5225 | 0.3049 | ±0.6097 | +1.714 | 0.0865 | . |
| **BMI (kg/m2)** | **-0.9312** | 0.4154 | ±0.8308 | **-2.242** | **0.0250** | * |
| Hypertension | -13.2383 | 6.9245 | ±13.8490 | -1.912 | 0.0559 | . |
| High cholesterol | +2.7520 | 6.4206 | ±12.8412 | +0.429 | 0.6682 |  |
| Kidney disease | +5.3106 | 8.0270 | ±16.0540 | +0.662 | 0.5082 |  |
| Circulatory disease | +12.5274 | 8.3440 | ±16.6879 | +1.501 | 0.1333 |  |
| Time 181-250, pooled (%) | +0.0269 | 0.2207 | ±0.4415 | +0.122 | 0.9029 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **479**, R² = **0.0521**, Adj R² = **0.0298**, F-statistic = **2.33** (p = **0.0084**), Residual SE = **66.548** on **467** df, AIC = **5392.8**, BIC = **5442.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+357.2293** | 25.3715 | ±50.7430 | **+14.080** | **5.04e-45** | *** |
| Education: graduate level (vs college) | -2.8222 | 7.4313 | ±14.8627 | -0.380 | 0.7041 |  |
| Education: high school or below (vs college) | -10.9522 | 8.3639 | ±16.7277 | -1.309 | 0.1904 |  |
| **Site: UCSD (vs UAB)** | **-18.5001** | 7.0803 | ±14.1607 | **-2.613** | **0.0090** | ** |
| Site: UW (vs UAB) | +2.7135 | 8.3643 | ±16.7287 | +0.324 | 0.7456 |  |
| Age (years) | +0.5218 | 0.3049 | ±0.6099 | +1.711 | 0.0870 | . |
| **BMI (kg/m2)** | **-0.9343** | 0.4154 | ±0.8308 | **-2.249** | **0.0245** | * |
| Hypertension | -13.2088 | 6.9230 | ±13.8461 | -1.908 | 0.0564 | . |
| High cholesterol | +2.7699 | 6.4160 | ±12.8321 | +0.432 | 0.6659 |  |
| Kidney disease | +5.3066 | 8.0249 | ±16.0498 | +0.661 | 0.5084 |  |
| Circulatory disease | +12.5129 | 8.3467 | ±16.6934 | +1.499 | 0.1338 |  |
| Avg. daily time 181-250 (%) | +0.0371 | 0.2154 | ±0.4308 | +0.172 | 0.8633 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **479**, R² = **0.0524**, Adj R² = **0.0301**, F-statistic = **2.35** (p = **0.0080**), Residual SE = **66.537** on **467** df, AIC = **5392.6**, BIC = **5442.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.1697** | 25.2666 | ±50.5333 | **+14.096** | **3.99e-45** | *** |
| Education: graduate level (vs college) | -2.6317 | 7.4344 | ±14.8688 | -0.354 | 0.7233 |  |
| Education: high school or below (vs college) | -11.1453 | 8.2639 | ±16.5279 | -1.349 | 0.1774 |  |
| **Site: UCSD (vs UAB)** | **-18.3686** | 7.0627 | ±14.1253 | **-2.601** | **0.0093** | ** |
| Site: UW (vs UAB) | +2.9184 | 8.3743 | ±16.7485 | +0.349 | 0.7275 |  |
| Age (years) | +0.5291 | 0.3044 | ±0.6088 | +1.738 | 0.0822 | . |
| **BMI (kg/m2)** | **-0.9504** | 0.4173 | ±0.8347 | **-2.277** | **0.0228** | * |
| Hypertension | -13.2442 | 6.8866 | ±13.7732 | -1.923 | 0.0545 | . |
| High cholesterol | +2.9161 | 6.4215 | ±12.8430 | +0.454 | 0.6497 |  |
| Kidney disease | +5.2095 | 8.0310 | ±16.0620 | +0.649 | 0.5165 |  |
| Circulatory disease | +12.3638 | 8.3963 | ±16.7926 | +1.473 | 0.1409 |  |
| Time > 180 (%) | +0.0541 | 0.1203 | ±0.2405 | +0.450 | 0.6527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **479**, R² = **0.0525**, Adj R² = **0.0302**, F-statistic = **2.35** (p = **0.0079**), Residual SE = **66.534** on **467** df, AIC = **5392.6**, BIC = **5442.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.1296** | 25.2258 | ±50.4516 | **+14.118** | **2.96e-45** | *** |
| Education: graduate level (vs college) | -2.6354 | 7.4307 | ±14.8615 | -0.355 | 0.7228 |  |
| Education: high school or below (vs college) | -11.1996 | 8.2678 | ±16.5357 | -1.355 | 0.1755 |  |
| **Site: UCSD (vs UAB)** | **-18.3252** | 7.0724 | ±14.1448 | **-2.591** | **0.0096** | ** |
| Site: UW (vs UAB) | +2.9376 | 8.3752 | ±16.7505 | +0.351 | 0.7258 |  |
| Age (years) | +0.5286 | 0.3043 | ±0.6086 | +1.737 | 0.0824 | . |
| **BMI (kg/m2)** | **-0.9529** | 0.4170 | ±0.8340 | **-2.285** | **0.0223** | * |
| Hypertension | -13.2275 | 6.8884 | ±13.7769 | -1.920 | 0.0548 | . |
| High cholesterol | +2.9284 | 6.4164 | ±12.8327 | +0.456 | 0.6481 |  |
| Kidney disease | +5.1766 | 8.0357 | ±16.0713 | +0.644 | 0.5194 |  |
| Circulatory disease | +12.3485 | 8.3947 | ±16.7894 | +1.471 | 0.1413 |  |
| Avg. daily time > 180 (%) | +0.0581 | 0.1195 | ±0.2391 | +0.486 | 0.6267 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **479**, R² = **0.0541**, Adj R² = **0.0318**, F-statistic = **2.43** (p = **0.0060**), Residual SE = **66.479** on **467** df, AIC = **5391.8**, BIC = **5441.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+355.2322** | 25.0914 | ±50.1827 | **+14.158** | **1.68e-45** | *** |
| Education: graduate level (vs college) | -2.3014 | 7.4416 | ±14.8833 | -0.309 | 0.7571 |  |
| Education: high school or below (vs college) | -11.4628 | 8.2618 | ±16.5236 | -1.387 | 0.1653 |  |
| **Site: UCSD (vs UAB)** | **-17.9504** | 7.1113 | ±14.2225 | **-2.524** | **0.0116** | * |
| Site: UW (vs UAB) | +3.0115 | 8.3530 | ±16.7061 | +0.361 | 0.7184 |  |
| Age (years) | +0.5459 | 0.3035 | ±0.6071 | +1.799 | 0.0721 | . |
| **BMI (kg/m2)** | **-1.0045** | 0.4226 | ±0.8451 | **-2.377** | **0.0174** | * |
| Hypertension | -13.2154 | 6.8806 | ±13.7612 | -1.921 | 0.0548 | . |
| High cholesterol | +3.3740 | 6.4557 | ±12.9114 | +0.523 | 0.6012 |  |
| Kidney disease | +5.1331 | 8.0144 | ±16.0289 | +0.640 | 0.5219 |  |
| Circulatory disease | +12.0529 | 8.3982 | ±16.7963 | +1.435 | 0.1512 |  |
| Nocturnal time > 180 (%) | +0.1084 | 0.1062 | ±0.2125 | +1.020 | 0.3076 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **479**, R² = **0.0526**, Adj R² = **0.0303**, F-statistic = **2.36** (p = **0.0077**), Residual SE = **66.531** on **467** df, AIC = **5392.6**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.1550** | 25.0819 | ±50.1638 | **+14.200** | **9.20e-46** | *** |
| Education: graduate level (vs college) | -2.4557 | 7.5033 | ±15.0067 | -0.327 | 0.7435 |  |
| Education: high school or below (vs college) | -11.0888 | 8.2088 | ±16.4176 | -1.351 | 0.1767 |  |
| **Site: UCSD (vs UAB)** | **-18.4224** | 7.0410 | ±14.0821 | **-2.616** | **0.0089** | ** |
| Site: UW (vs UAB) | +3.1065 | 8.3212 | ±16.6424 | +0.373 | 0.7089 |  |
| Age (years) | +0.5412 | 0.3041 | ±0.6082 | +1.780 | 0.0751 | . |
| **BMI (kg/m2)** | **-0.9433** | 0.4139 | ±0.8278 | **-2.279** | **0.0227** | * |
| Hypertension | -13.4488 | 6.8756 | ±13.7512 | -1.956 | 0.0505 | . |
| High cholesterol | +2.8851 | 6.4277 | ±12.8555 | +0.449 | 0.6535 |  |
| Kidney disease | +5.1332 | 8.0504 | ±16.1007 | +0.638 | 0.5237 |  |
| Circulatory disease | +12.4024 | 8.4423 | ±16.8845 | +1.469 | 0.1418 |  |
| Time > 250 (%) | +0.0927 | 0.1682 | ±0.3364 | +0.551 | 0.5818 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 479)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **479**, R² = **0.0527**, Adj R² = **0.0303**, F-statistic = **2.36** (p = **0.0077**), Residual SE = **66.529** on **467** df, AIC = **5392.5**, BIC = **5442.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+356.2632** | 25.0651 | ±50.1301 | **+14.214** | **7.55e-46** | *** |
| Education: graduate level (vs college) | -2.4499 | 7.5038 | ±15.0076 | -0.326 | 0.7441 |  |
| Education: high school or below (vs college) | -11.0994 | 8.2080 | ±16.4160 | -1.352 | 0.1763 |  |
| **Site: UCSD (vs UAB)** | **-18.4079** | 7.0437 | ±14.0874 | **-2.613** | **0.0090** | ** |
| Site: UW (vs UAB) | +3.1078 | 8.3198 | ±16.6396 | +0.374 | 0.7087 |  |
| Age (years) | +0.5398 | 0.3038 | ±0.6076 | +1.777 | 0.0756 | . |
| **BMI (kg/m2)** | **-0.9444** | 0.4138 | ±0.8275 | **-2.283** | **0.0225** | * |
| Hypertension | -13.4403 | 6.8742 | ±13.7484 | -1.955 | 0.0506 | . |
| High cholesterol | +2.8937 | 6.4254 | ±12.8508 | +0.450 | 0.6525 |  |
| Kidney disease | +5.0946 | 8.0598 | ±16.1195 | +0.632 | 0.5273 |  |
| Circulatory disease | +12.3776 | 8.4475 | ±16.8950 | +1.465 | 0.1429 |  |
| Avg. daily time > 250 (%) | +0.0969 | 0.1704 | ±0.3408 | +0.569 | 0.5695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 474; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **474**, R² = **0.1628**, Adj R² = **0.1447**, F-statistic = **9.00** (p = **1.33e-13**), Residual SE = **17.243** on **463** df, AIC = **4055.4**, BIC = **4101.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.3622** | 7.1671 | ±14.3342 | **+10.934** | **7.96e-28** | *** |
| Education: graduate level (vs college) | -1.6362 | 1.9359 | ±3.8718 | -0.845 | 0.3980 |  |
| Education: high school or below (vs college) | +1.8928 | 2.1170 | ±4.2340 | +0.894 | 0.3713 |  |
| **Site: UCSD (vs UAB)** | **+4.2463** | 2.0999 | ±4.1999 | **+2.022** | **0.0432** | * |
| Site: UW (vs UAB) | +3.2015 | 1.9533 | ±3.9065 | +1.639 | 0.1012 |  |
| **Age (years)** | **-0.4987** | 0.0828 | ±0.1656 | **-6.025** | **1.69e-09** | *** |
| **BMI (kg/m2)** | **+0.3427** | 0.1105 | ±0.2209 | **+3.102** | **0.0019** | ** |
| Hypertension | -0.2764 | 1.9196 | ±3.8391 | -0.144 | 0.8855 |  |
| High cholesterol | -0.5439 | 1.7950 | ±3.5901 | -0.303 | 0.7619 |  |
| Kidney disease | -3.1588 | 2.1203 | ±4.2406 | -1.490 | 0.1363 |  |
| Circulatory disease | -3.6517 | 2.0068 | ±4.0135 | -1.820 | 0.0688 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **474**, R² = **0.1795**, Adj R² = **0.1600**, F-statistic = **9.19** (p = **5.95e-15**), Residual SE = **17.088** on **462** df, AIC = **4047.8**, BIC = **4097.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1487** | 8.2678 | ±16.5356 | **+8.001** | **1.24e-15** | *** |
| Education: graduate level (vs college) | -1.2233 | 1.9195 | ±3.8390 | -0.637 | 0.5239 |  |
| Education: high school or below (vs college) | +1.2183 | 2.1043 | ±4.2086 | +0.579 | 0.5626 |  |
| **Site: UCSD (vs UAB)** | **+4.4321** | 2.0762 | ±4.1525 | **+2.135** | **0.0328** | * |
| Site: UW (vs UAB) | +3.5815 | 1.9649 | ±3.9298 | +1.823 | 0.0683 | . |
| **Age (years)** | **-0.4862** | 0.0814 | ±0.1628 | **-5.973** | **2.32e-09** | *** |
| **BMI (kg/m2)** | **+0.2903** | 0.1108 | ±0.2216 | **+2.620** | **0.0088** | ** |
| Hypertension | -0.4860 | 1.9122 | ±3.8245 | -0.254 | 0.7994 |  |
| High cholesterol | -0.3744 | 1.7906 | ±3.5813 | -0.209 | 0.8344 |  |
| Kidney disease | -2.8128 | 2.0768 | ±4.1537 | -1.354 | 0.1756 |  |
| Circulatory disease | -3.6053 | 1.9944 | ±3.9887 | -1.808 | 0.0706 | . |
| **HbA1c (%)** | **+1.7967** | 0.5689 | ±1.1379 | **+3.158** | **0.0016** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **474**, R² = **0.1824**, Adj R² = **0.1629**, F-statistic = **9.37** (p = **2.84e-15**), Residual SE = **17.058** on **462** df, AIC = **4046.1**, BIC = **4096.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1723** | 8.0844 | ±16.1689 | **+8.309** | **9.67e-17** | *** |
| Education: graduate level (vs college) | -1.3274 | 1.9123 | ±3.8247 | -0.694 | 0.4876 |  |
| Education: high school or below (vs college) | +1.1740 | 2.0783 | ±4.1566 | +0.565 | 0.5722 |  |
| **Site: UCSD (vs UAB)** | **+4.5920** | 2.0810 | ±4.1621 | **+2.207** | **0.0273** | * |
| Site: UW (vs UAB) | +3.5937 | 1.9664 | ±3.9328 | +1.828 | 0.0676 | . |
| **Age (years)** | **-0.4821** | 0.0811 | ±0.1623 | **-5.942** | **2.82e-09** | *** |
| **BMI (kg/m2)** | **+0.3028** | 0.1106 | ±0.2212 | **+2.737** | **0.0062** | ** |
| Hypertension | -0.3148 | 1.9143 | ±3.8287 | -0.164 | 0.8694 |  |
| High cholesterol | -0.2032 | 1.8032 | ±3.6063 | -0.113 | 0.9103 |  |
| Kidney disease | -3.2260 | 2.0948 | ±4.1896 | -1.540 | 0.1236 |  |
| **Circulatory disease** | **-4.0584** | 1.9802 | ±3.9604 | **-2.049** | **0.0404** | * |
| **Mean glucose (mg/dL)** | **+0.0649** | 0.0214 | ±0.0428 | **+3.036** | **0.0024** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **474**, R² = **0.1824**, Adj R² = **0.1629**, F-statistic = **9.37** (p = **2.84e-15**), Residual SE = **17.058** on **462** df, AIC = **4046.1**, BIC = **4096.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.1849** | 9.8658 | ±19.7317 | **+5.898** | **3.69e-09** | *** |
| Education: graduate level (vs college) | -1.3274 | 1.9123 | ±3.8247 | -0.694 | 0.4876 |  |
| Education: high school or below (vs college) | +1.1740 | 2.0783 | ±4.1566 | +0.565 | 0.5722 |  |
| **Site: UCSD (vs UAB)** | **+4.5920** | 2.0810 | ±4.1621 | **+2.207** | **0.0273** | * |
| Site: UW (vs UAB) | +3.5937 | 1.9664 | ±3.9328 | +1.828 | 0.0676 | . |
| **Age (years)** | **-0.4821** | 0.0811 | ±0.1623 | **-5.942** | **2.82e-09** | *** |
| **BMI (kg/m2)** | **+0.3028** | 0.1106 | ±0.2212 | **+2.737** | **0.0062** | ** |
| Hypertension | -0.3148 | 1.9143 | ±3.8287 | -0.164 | 0.8694 |  |
| High cholesterol | -0.2032 | 1.8032 | ±3.6063 | -0.113 | 0.9103 |  |
| Kidney disease | -3.2260 | 2.0948 | ±4.1896 | -1.540 | 0.1236 |  |
| **Circulatory disease** | **-4.0584** | 1.9802 | ±3.9604 | **-2.049** | **0.0404** | * |
| **GMI (%)** | **+2.7152** | 0.8943 | ±1.7885 | **+3.036** | **0.0024** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **474**, R² = **0.1792**, Adj R² = **0.1597**, F-statistic = **9.17** (p = **6.41e-15**), Residual SE = **17.091** on **462** df, AIC = **4048.0**, BIC = **4097.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.0354** | 7.9527 | ±15.9054 | **+8.681** | **3.93e-18** | *** |
| Education: graduate level (vs college) | -1.2999 | 1.9222 | ±3.8445 | -0.676 | 0.4989 |  |
| Education: high school or below (vs college) | +1.2776 | 2.0745 | ±4.1490 | +0.616 | 0.5380 |  |
| **Site: UCSD (vs UAB)** | **+4.6101** | 2.0885 | ±4.1770 | **+2.207** | **0.0273** | * |
| Site: UW (vs UAB) | +3.3667 | 1.9575 | ±3.9151 | +1.720 | 0.0855 | . |
| **Age (years)** | **-0.4759** | 0.0819 | ±0.1638 | **-5.810** | **6.25e-09** | *** |
| **BMI (kg/m2)** | **+0.2902** | 0.1109 | ±0.2217 | **+2.617** | **0.0089** | ** |
| Hypertension | -0.2849 | 1.9151 | ±3.8301 | -0.149 | 0.8817 |  |
| High cholesterol | -0.1615 | 1.8147 | ±3.6293 | -0.089 | 0.9291 |  |
| Kidney disease | -3.0429 | 2.1043 | ±4.2087 | -1.446 | 0.1482 |  |
| **Circulatory disease** | **-4.0360** | 1.9881 | ±3.9761 | **-2.030** | **0.0423** | * |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0563** | 0.0206 | ±0.0412 | **+2.734** | **0.0063** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **474**, R² = **0.1670**, Adj R² = **0.1472**, F-statistic = **8.42** (p = **1.42e-13**), Residual SE = **17.218** on **462** df, AIC = **4055.0**, BIC = **4104.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.3078** | 7.6104 | ±15.2208 | **+9.764** | **1.61e-22** | *** |
| Education: graduate level (vs college) | -1.4754 | 1.9393 | ±3.8787 | -0.761 | 0.4468 |  |
| Education: high school or below (vs college) | +1.5225 | 2.1217 | ±4.2434 | +0.718 | 0.4730 |  |
| **Site: UCSD (vs UAB)** | **+4.4095** | 2.1103 | ±4.2206 | **+2.089** | **0.0367** | * |
| Site: UW (vs UAB) | +3.6031 | 2.0102 | ±4.0203 | +1.792 | 0.0731 | . |
| **Age (years)** | **-0.4967** | 0.0822 | ±0.1644 | **-6.043** | **1.51e-09** | *** |
| **BMI (kg/m2)** | **+0.3318** | 0.1114 | ±0.2227 | **+2.979** | **0.0029** | ** |
| Hypertension | -0.3880 | 1.9354 | ±3.8708 | -0.200 | 0.8411 |  |
| High cholesterol | -0.3717 | 1.8070 | ±3.6141 | -0.206 | 0.8370 |  |
| Kidney disease | -3.6153 | 2.1242 | ±4.2483 | -1.702 | 0.0888 | . |
| Circulatory disease | -3.7594 | 1.9981 | ±3.9962 | -1.881 | 0.0599 | . |
| Glucose SD, pooled (mg/dL) | +0.1012 | 0.0710 | ±0.1420 | +1.426 | 0.1539 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **474**, R² = **0.1671**, Adj R² = **0.1473**, F-statistic = **8.43** (p = **1.38e-13**), Residual SE = **17.217** on **462** df, AIC = **4054.9**, BIC = **4104.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.9813** | 7.7277 | ±15.4553 | **+9.574** | **1.03e-21** | *** |
| Education: graduate level (vs college) | -1.4955 | 1.9348 | ±3.8695 | -0.773 | 0.4395 |  |
| Education: high school or below (vs college) | +1.4593 | 2.1306 | ±4.2613 | +0.685 | 0.4934 |  |
| **Site: UCSD (vs UAB)** | **+4.4296** | 2.1096 | ±4.2192 | **+2.100** | **0.0358** | * |
| Site: UW (vs UAB) | +3.5766 | 2.0083 | ±4.0166 | +1.781 | 0.0749 | . |
| **Age (years)** | **-0.4985** | 0.0824 | ±0.1647 | **-6.052** | **1.43e-09** | *** |
| **BMI (kg/m2)** | **+0.3411** | 0.1109 | ±0.2218 | **+3.076** | **0.0021** | ** |
| Hypertension | -0.3444 | 1.9323 | ±3.8645 | -0.178 | 0.8585 |  |
| High cholesterol | -0.3970 | 1.8040 | ±3.6081 | -0.220 | 0.8258 |  |
| Kidney disease | -3.6831 | 2.1374 | ±4.2747 | -1.723 | 0.0849 | . |
| Circulatory disease | -3.7375 | 1.9972 | ±3.9945 | -1.871 | 0.0613 | . |
| Avg. daily SD (mg/dL) | +0.1180 | 0.0849 | ±0.1698 | +1.390 | 0.1645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **474**, R² = **0.1674**, Adj R² = **0.1475**, F-statistic = **8.44** (p = **1.31e-13**), Residual SE = **17.214** on **462** df, AIC = **4054.8**, BIC = **4104.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.7750** | 7.7628 | ±15.5257 | **+10.792** | **3.76e-27** | *** |
| Education: graduate level (vs college) | -1.7223 | 1.9355 | ±3.8710 | -0.890 | 0.3735 |  |
| Education: high school or below (vs college) | +2.0777 | 2.0928 | ±4.1856 | +0.993 | 0.3208 |  |
| **Site: UCSD (vs UAB)** | **+4.1385** | 2.0962 | ±4.1925 | **+1.974** | **0.0484** | * |
| Site: UW (vs UAB) | +2.8396 | 1.9790 | ±3.9580 | +1.435 | 0.1513 |  |
| **Age (years)** | **-0.4935** | 0.0833 | ±0.1667 | **-5.922** | **3.18e-09** | *** |
| **BMI (kg/m2)** | **+0.3389** | 0.1104 | ±0.2209 | **+3.069** | **0.0021** | ** |
| Hypertension | -0.1183 | 1.9198 | ±3.8396 | -0.062 | 0.9509 |  |
| High cholesterol | -0.6035 | 1.7902 | ±3.5804 | -0.337 | 0.7360 |  |
| Kidney disease | -2.5759 | 2.1596 | ±4.3191 | -1.193 | 0.2329 |  |
| Circulatory disease | -3.7230 | 2.0095 | ±4.0190 | -1.853 | 0.0639 | . |
| CV (%) | -0.2316 | 0.1495 | ±0.2990 | -1.549 | 0.1214 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **474**, R² = **0.1661**, Adj R² = **0.1462**, F-statistic = **8.37** (p = **1.79e-13**), Residual SE = **17.227** on **462** df, AIC = **4055.5**, BIC = **4105.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.5550** | 8.1140 | ±16.2280 | **+9.065** | **1.24e-19** | *** |
| Education: graduate level (vs college) | -1.7168 | 1.9346 | ±3.8693 | -0.887 | 0.3749 |  |
| Education: high school or below (vs college) | +2.0089 | 2.1052 | ±4.2105 | +0.954 | 0.3400 |  |
| **Site: UCSD (vs UAB)** | **+4.2267** | 2.0938 | ±4.1876 | **+2.019** | **0.0435** | * |
| Site: UW (vs UAB) | +2.9613 | 1.9714 | ±3.9427 | +1.502 | 0.1331 |  |
| **Age (years)** | **-0.4959** | 0.0831 | ±0.1662 | **-5.966** | **2.44e-09** | *** |
| **BMI (kg/m2)** | **+0.3367** | 0.1100 | ±0.2199 | **+3.062** | **0.0022** | ** |
| Hypertension | -0.1864 | 1.9209 | ±3.8418 | -0.097 | 0.9227 |  |
| High cholesterol | -0.5079 | 1.7920 | ±3.5841 | -0.283 | 0.7769 |  |
| Kidney disease | -2.7256 | 2.1537 | ±4.3074 | -1.266 | 0.2057 |  |
| Circulatory disease | -3.6464 | 2.0008 | ±4.0016 | -1.822 | 0.0684 | . |
| Mean / SD ratio | +1.0971 | 0.8129 | ±1.6259 | +1.350 | 0.1772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **474**, R² = **0.1659**, Adj R² = **0.1460**, F-statistic = **8.35** (p = **1.89e-13**), Residual SE = **17.230** on **462** df, AIC = **4055.6**, BIC = **4105.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.1003** | 7.9563 | ±15.9125 | **+9.313** | **1.24e-20** | *** |
| Education: graduate level (vs college) | -1.7192 | 1.9337 | ±3.8673 | -0.889 | 0.3740 |  |
| Education: high school or below (vs college) | +2.0138 | 2.1024 | ±4.2048 | +0.958 | 0.3381 |  |
| **Site: UCSD (vs UAB)** | **+4.2271** | 2.0998 | ±4.1996 | **+2.013** | **0.0441** | * |
| Site: UW (vs UAB) | +3.0248 | 1.9611 | ±3.9222 | +1.542 | 0.1230 |  |
| **Age (years)** | **-0.4938** | 0.0831 | ±0.1661 | **-5.944** | **2.77e-09** | *** |
| **BMI (kg/m2)** | **+0.3283** | 0.1105 | ±0.2209 | **+2.972** | **0.0030** | ** |
| Hypertension | -0.2189 | 1.9196 | ±3.8392 | -0.114 | 0.9092 |  |
| High cholesterol | -0.5219 | 1.7930 | ±3.5860 | -0.291 | 0.7710 |  |
| Kidney disease | -2.7757 | 2.1580 | ±4.3160 | -1.286 | 0.1984 |  |
| Circulatory disease | -3.6955 | 2.0062 | ±4.0124 | -1.842 | 0.0655 | . |
| Avg. daily mean/SD | +0.8603 | 0.6336 | ±1.2672 | +1.358 | 0.1745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **474**, R² = **0.1683**, Adj R² = **0.1485**, F-statistic = **8.50** (p = **1.02e-13**), Residual SE = **17.204** on **462** df, AIC = **4054.2**, BIC = **4104.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.5459** | 8.4671 | ±16.9342 | **+8.332** | **7.96e-17** | *** |
| Education: graduate level (vs college) | -1.4256 | 1.9323 | ±3.8647 | -0.738 | 0.4607 |  |
| Education: high school or below (vs college) | +1.6335 | 2.1270 | ±4.2540 | +0.768 | 0.4425 |  |
| **Site: UCSD (vs UAB)** | **+4.5043** | 2.1108 | ±4.2216 | **+2.134** | **0.0328** | * |
| Site: UW (vs UAB) | +3.7324 | 2.0056 | ±4.0113 | +1.861 | 0.0627 | . |
| **Age (years)** | **-0.4842** | 0.0821 | ±0.1643 | **-5.895** | **3.75e-09** | *** |
| **BMI (kg/m2)** | **+0.3469** | 0.1118 | ±0.2235 | **+3.103** | **0.0019** | ** |
| Hypertension | -0.3153 | 1.9234 | ±3.8468 | -0.164 | 0.8698 |  |
| High cholesterol | -0.4202 | 1.8021 | ±3.6042 | -0.233 | 0.8156 |  |
| Kidney disease | -3.4829 | 2.1487 | ±4.2974 | -1.621 | 0.1050 |  |
| Circulatory disease | -3.6972 | 2.0028 | ±4.0056 | -1.846 | 0.0649 | . |
| MAG (mg/dL/h) | +0.1425 | 0.0842 | ±0.1685 | +1.691 | 0.0908 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **474**, R² = **0.1651**, Adj R² = **0.1452**, F-statistic = **8.31** (p = **2.29e-13**), Residual SE = **17.238** on **462** df, AIC = **4056.0**, BIC = **4106.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.9118** | 8.1262 | ±16.2523 | **+9.096** | **9.41e-20** | *** |
| Education: graduate level (vs college) | -1.5375 | 1.9396 | ±3.8792 | -0.793 | 0.4280 |  |
| Education: high school or below (vs college) | +1.5682 | 2.1288 | ±4.2577 | +0.737 | 0.4613 |  |
| **Site: UCSD (vs UAB)** | **+4.4039** | 2.1155 | ±4.2310 | **+2.082** | **0.0374** | * |
| Site: UW (vs UAB) | +3.4821 | 2.0142 | ±4.0284 | +1.729 | 0.0838 | . |
| **Age (years)** | **-0.4950** | 0.0826 | ±0.1651 | **-5.996** | **2.03e-09** | *** |
| **BMI (kg/m2)** | **+0.3446** | 0.1109 | ±0.2217 | **+3.108** | **0.0019** | ** |
| Hypertension | -0.2718 | 1.9282 | ±3.8564 | -0.141 | 0.8879 |  |
| High cholesterol | -0.4759 | 1.8051 | ±3.6102 | -0.264 | 0.7921 |  |
| Kidney disease | -3.5794 | 2.1419 | ±4.2837 | -1.671 | 0.0947 | . |
| Circulatory disease | -3.7186 | 1.9988 | ±3.9976 | -1.860 | 0.0628 | . |
| Avg. daily range (mg/dL) | +0.0257 | 0.0247 | ±0.0495 | +1.041 | 0.2981 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **474**, R² = **0.1666**, Adj R² = **0.1468**, F-statistic = **8.40** (p = **1.57e-13**), Residual SE = **17.222** on **462** df, AIC = **4055.2**, BIC = **4105.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2573** | 7.2768 | ±14.5536 | **+10.480** | **1.07e-25** | *** |
| Education: graduate level (vs college) | -1.4351 | 1.9526 | ±3.9052 | -0.735 | 0.4623 |  |
| Education: high school or below (vs college) | +1.7799 | 2.0994 | ±4.1988 | +0.848 | 0.3966 |  |
| **Site: UCSD (vs UAB)** | **+4.2839** | 2.1080 | ±4.2159 | **+2.032** | **0.0421** | * |
| Site: UW (vs UAB) | +3.4832 | 1.9770 | ±3.9540 | +1.762 | 0.0781 | . |
| **Age (years)** | **-0.4879** | 0.0823 | ±0.1646 | **-5.927** | **3.08e-09** | *** |
| **BMI (kg/m2)** | **+0.3227** | 0.1104 | ±0.2208 | **+2.923** | **0.0035** | ** |
| Hypertension | -0.5026 | 1.9437 | ±3.8875 | -0.259 | 0.7960 |  |
| High cholesterol | -0.3530 | 1.8135 | ±3.6270 | -0.195 | 0.8457 |  |
| Kidney disease | -3.2456 | 2.1135 | ±4.2270 | -1.536 | 0.1246 |  |
| Circulatory disease | -3.8913 | 2.0108 | ±4.0217 | -1.935 | 0.0530 | . |
| SD of daily means (mg/dL) | +0.1361 | 0.0888 | ±0.1776 | +1.533 | 0.1254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **474**, R² = **0.1833**, Adj R² = **0.1638**, F-statistic = **9.42** (p = **2.26e-15**), Residual SE = **17.049** on **462** df, AIC = **4045.6**, BIC = **4095.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.8193** | 7.3714 | ±14.7427 | **+11.642** | **2.51e-31** | *** |
| Education: graduate level (vs college) | -1.3835 | 1.9119 | ±3.8237 | -0.724 | 0.4693 |  |
| Education: high school or below (vs college) | +1.0975 | 2.0818 | ±4.1637 | +0.527 | 0.5981 |  |
| **Site: UCSD (vs UAB)** | **+4.7428** | 2.0964 | ±4.1928 | **+2.262** | **0.0237** | * |
| Site: UW (vs UAB) | +3.6402 | 1.9627 | ±3.9254 | +1.855 | 0.0636 | . |
| **Age (years)** | **-0.4896** | 0.0814 | ±0.1629 | **-6.012** | **1.83e-09** | *** |
| **BMI (kg/m2)** | **+0.2933** | 0.1108 | ±0.2216 | **+2.647** | **0.0081** | ** |
| Hypertension | -0.2452 | 1.9183 | ±3.8366 | -0.128 | 0.8983 |  |
| High cholesterol | -0.0439 | 1.8082 | ±3.6163 | -0.024 | 0.9806 |  |
| Kidney disease | -3.3018 | 2.0881 | ±4.1762 | -1.581 | 0.1138 |  |
| **Circulatory disease** | **-4.0791** | 1.9746 | ±3.9493 | **-2.066** | **0.0389** | * |
| **Time in range 70-180, pooled (%)** | **-0.1065** | 0.0325 | ±0.0649 | **-3.280** | **0.0010** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **474**, R² = **0.1826**, Adj R² = **0.1631**, F-statistic = **9.38** (p = **2.71e-15**), Residual SE = **17.056** on **462** df, AIC = **4046.0**, BIC = **4096.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.7857** | 7.3899 | ±14.7799 | **+11.608** | **3.73e-31** | *** |
| Education: graduate level (vs college) | -1.4178 | 1.9135 | ±3.8271 | -0.741 | 0.4587 |  |
| Education: high school or below (vs college) | +1.0721 | 2.0827 | ±4.1654 | +0.515 | 0.6067 |  |
| **Site: UCSD (vs UAB)** | **+4.7734** | 2.0998 | ±4.1997 | **+2.273** | **0.0230** | * |
| Site: UW (vs UAB) | +3.6391 | 1.9640 | ±3.9280 | +1.853 | 0.0639 | . |
| **Age (years)** | **-0.4913** | 0.0816 | ±0.1631 | **-6.023** | **1.71e-09** | *** |
| **BMI (kg/m2)** | **+0.2931** | 0.1113 | ±0.2225 | **+2.634** | **0.0084** | ** |
| Hypertension | -0.2248 | 1.9186 | ±3.8372 | -0.117 | 0.9067 |  |
| High cholesterol | -0.0622 | 1.8088 | ±3.6176 | -0.034 | 0.9726 |  |
| Kidney disease | -3.3465 | 2.0899 | ±4.1798 | -1.601 | 0.1093 |  |
| **Circulatory disease** | **-4.0647** | 1.9778 | ±3.9556 | **-2.055** | **0.0399** | * |
| **Avg. daily time in range 70-180 (%)** | **-0.1038** | 0.0322 | ±0.0644 | **-3.225** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **474**, R² = **0.1635**, Adj R² = **0.1436**, F-statistic = **8.21** (p = **3.41e-13**), Residual SE = **17.254** on **462** df, AIC = **4056.9**, BIC = **4106.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.8495** | 7.2384 | ±14.4768 | **+10.893** | **1.24e-27** | *** |
| Education: graduate level (vs college) | -1.6411 | 1.9388 | ±3.8776 | -0.846 | 0.3973 |  |
| Education: high school or below (vs college) | +1.8617 | 2.1212 | ±4.2424 | +0.878 | 0.3801 |  |
| **Site: UCSD (vs UAB)** | **+4.1643** | 2.1110 | ±4.2221 | **+1.973** | **0.0485** | * |
| Site: UW (vs UAB) | +3.1392 | 1.9674 | ±3.9347 | +1.596 | 0.1106 |  |
| **Age (years)** | **-0.5015** | 0.0831 | ±0.1662 | **-6.035** | **1.59e-09** | *** |
| **BMI (kg/m2)** | **+0.3416** | 0.1110 | ±0.2221 | **+3.077** | **0.0021** | ** |
| Hypertension | -0.1949 | 1.9361 | ±3.8723 | -0.101 | 0.9198 |  |
| High cholesterol | -0.5827 | 1.8004 | ±3.6008 | -0.324 | 0.7462 |  |
| Kidney disease | -3.1569 | 2.1262 | ±4.2525 | -1.485 | 0.1376 |  |
| Circulatory disease | -3.5787 | 2.0023 | ±4.0046 | -1.787 | 0.0739 | . |
| Any reading < 54 during wear (0/1) | -1.2516 | 1.9071 | ±3.8141 | -0.656 | 0.5116 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **474**, R² = **0.1633**, Adj R² = **0.1434**, F-statistic = **8.20** (p = **3.63e-13**), Residual SE = **17.257** on **462** df, AIC = **4057.1**, BIC = **4107.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.4969** | 7.2106 | ±14.4211 | **+10.886** | **1.34e-27** | *** |
| Education: graduate level (vs college) | -1.6803 | 1.9399 | ±3.8798 | -0.866 | 0.3864 |  |
| Education: high school or below (vs college) | +1.8203 | 2.1292 | ±4.2584 | +0.855 | 0.3926 |  |
| **Site: UCSD (vs UAB)** | **+4.1576** | 2.1193 | ±4.2386 | **+1.962** | **0.0498** | * |
| Site: UW (vs UAB) | +3.0808 | 1.9833 | ±3.9666 | +1.553 | 0.1203 |  |
| **Age (years)** | **-0.4978** | 0.0830 | ±0.1660 | **-5.998** | **2.00e-09** | *** |
| **BMI (kg/m2)** | **+0.3426** | 0.1118 | ±0.2237 | **+3.064** | **0.0022** | ** |
| Hypertension | -0.1593 | 1.9452 | ±3.8904 | -0.082 | 0.9347 |  |
| High cholesterol | -0.6212 | 1.8113 | ±3.6226 | -0.343 | 0.7316 |  |
| Kidney disease | -3.1495 | 2.1243 | ±4.2487 | -1.483 | 0.1382 |  |
| Circulatory disease | -3.7346 | 2.0213 | ±4.0427 | -1.848 | 0.0647 | . |
| Time < 54 (%) | -1.6212 | 3.4293 | ±6.8586 | -0.473 | 0.6364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **474**, R² = **0.1646**, Adj R² = **0.1447**, F-statistic = **8.27** (p = **2.62e-13**), Residual SE = **17.243** on **462** df, AIC = **4056.3**, BIC = **4106.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.4908** | 7.1981 | ±14.3962 | **+10.904** | **1.10e-27** | *** |
| Education: graduate level (vs college) | -1.6919 | 1.9365 | ±3.8731 | -0.874 | 0.3823 |  |
| Education: high school or below (vs college) | +1.7754 | 2.1200 | ±4.2401 | +0.837 | 0.4023 |  |
| Site: UCSD (vs UAB) | +4.1138 | 2.1112 | ±4.2223 | +1.949 | 0.0513 | . |
| Site: UW (vs UAB) | +3.0221 | 1.9703 | ±3.9407 | +1.534 | 0.1251 |  |
| **Age (years)** | **-0.4979** | 0.0829 | ±0.1659 | **-6.004** | **1.92e-09** | *** |
| **BMI (kg/m2)** | **+0.3447** | 0.1117 | ±0.2234 | **+3.085** | **0.0020** | ** |
| Hypertension | -0.1213 | 1.9278 | ±3.8557 | -0.063 | 0.9498 |  |
| High cholesterol | -0.6731 | 1.8027 | ±3.6054 | -0.373 | 0.7089 |  |
| Kidney disease | -3.1076 | 2.1254 | ±4.2508 | -1.462 | 0.1437 |  |
| Circulatory disease | -3.7559 | 2.0120 | ±4.0240 | -1.867 | 0.0619 | . |
| Avg. daily time < 54 (%) | -2.1749 | 3.1612 | ±6.3223 | -0.688 | 0.4914 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **474**, R² = **0.1664**, Adj R² = **0.1466**, F-statistic = **8.39** (p = **1.64e-13**), Residual SE = **17.224** on **462** df, AIC = **4055.3**, BIC = **4105.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.8107** | 7.1867 | ±14.3734 | **+10.966** | **5.56e-28** | *** |
| Education: graduate level (vs college) | -1.7864 | 1.9400 | ±3.8799 | -0.921 | 0.3571 |  |
| Education: high school or below (vs college) | +1.8302 | 2.1118 | ±4.2236 | +0.867 | 0.3861 |  |
| Site: UCSD (vs UAB) | +3.9227 | 2.1077 | ±4.2154 | +1.861 | 0.0627 | . |
| Site: UW (vs UAB) | +2.8613 | 1.9750 | ±3.9499 | +1.449 | 0.1474 |  |
| **Age (years)** | **-0.4918** | 0.0831 | ±0.1662 | **-5.918** | **3.26e-09** | *** |
| **BMI (kg/m2)** | **+0.3370** | 0.1114 | ±0.2228 | **+3.024** | **0.0025** | ** |
| Hypertension | -0.0445 | 1.9198 | ±3.8396 | -0.023 | 0.9815 |  |
| High cholesterol | -0.7715 | 1.8001 | ±3.6002 | -0.429 | 0.6682 |  |
| Kidney disease | -3.1108 | 2.1217 | ±4.2434 | -1.466 | 0.1426 |  |
| Circulatory disease | -3.9125 | 2.0205 | ±4.0410 | -1.936 | 0.0528 | . |
| Time 54-69, pooled (%) | -1.3116 | 0.8641 | ±1.7282 | -1.518 | 0.1290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **474**, R² = **0.1675**, Adj R² = **0.1476**, F-statistic = **8.45** (p = **1.27e-13**), Residual SE = **17.213** on **462** df, AIC = **4054.7**, BIC = **4104.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.6649** | 7.1770 | ±14.3539 | **+10.961** | **5.90e-28** | *** |
| Education: graduate level (vs college) | -1.7907 | 1.9370 | ±3.8739 | -0.924 | 0.3552 |  |
| Education: high school or below (vs college) | +1.8047 | 2.1066 | ±4.2132 | +0.857 | 0.3916 |  |
| Site: UCSD (vs UAB) | +3.8919 | 2.1089 | ±4.2177 | +1.846 | 0.0650 | . |
| Site: UW (vs UAB) | +2.8148 | 1.9741 | ±3.9482 | +1.426 | 0.1539 |  |
| **Age (years)** | **-0.4907** | 0.0831 | ±0.1662 | **-5.904** | **3.54e-09** | *** |
| **BMI (kg/m2)** | **+0.3396** | 0.1113 | ±0.2226 | **+3.051** | **0.0023** | ** |
| Hypertension | -0.0109 | 1.9170 | ±3.8340 | -0.006 | 0.9955 |  |
| High cholesterol | -0.7918 | 1.7966 | ±3.5932 | -0.441 | 0.6594 |  |
| Kidney disease | -3.0857 | 2.1217 | ±4.2434 | -1.454 | 0.1458 |  |
| Circulatory disease | -3.9222 | 2.0199 | ±4.0399 | -1.942 | 0.0522 | . |
| Avg. daily time 54-69 (%) | -1.3445 | 0.7741 | ±1.5482 | -1.737 | 0.0824 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **474**, R² = **0.1659**, Adj R² = **0.1460**, F-statistic = **8.35** (p = **1.88e-13**), Residual SE = **17.229** on **462** df, AIC = **4055.6**, BIC = **4105.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.7886** | 7.2026 | ±14.4052 | **+10.939** | **7.51e-28** | *** |
| Education: graduate level (vs college) | -1.7783 | 1.9413 | ±3.8826 | -0.916 | 0.3596 |  |
| Education: high school or below (vs college) | +1.8000 | 2.1152 | ±4.2304 | +0.851 | 0.3948 |  |
| Site: UCSD (vs UAB) | +3.9439 | 2.1144 | ±4.2287 | +1.865 | 0.0621 | . |
| Site: UW (vs UAB) | +2.8666 | 1.9806 | ±3.9613 | +1.447 | 0.1478 |  |
| **Age (years)** | **-0.4929** | 0.0831 | ±0.1662 | **-5.931** | **3.01e-09** | *** |
| **BMI (kg/m2)** | **+0.3383** | 0.1119 | ±0.2238 | **+3.023** | **0.0025** | ** |
| Hypertension | -0.0266 | 1.9256 | ±3.8512 | -0.014 | 0.9890 |  |
| High cholesterol | -0.7658 | 1.8048 | ±3.6096 | -0.424 | 0.6713 |  |
| Kidney disease | -3.1164 | 2.1225 | ±4.2450 | -1.468 | 0.1420 |  |
| Circulatory disease | -3.9025 | 2.0214 | ±4.0428 | -1.931 | 0.0535 | . |
| Time < 70 (%) | -1.0032 | 0.7063 | ±1.4126 | -1.420 | 0.1555 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **474**, R² = **0.1672**, Adj R² = **0.1474**, F-statistic = **8.43** (p = **1.36e-13**), Residual SE = **17.216** on **462** df, AIC = **4054.9**, BIC = **4104.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.6535** | 7.1883 | ±14.3766 | **+10.942** | **7.27e-28** | *** |
| Education: graduate level (vs college) | -1.7802 | 1.9369 | ±3.8738 | -0.919 | 0.3580 |  |
| Education: high school or below (vs college) | +1.7703 | 2.1092 | ±4.2185 | +0.839 | 0.4013 |  |
| Site: UCSD (vs UAB) | +3.9138 | 2.1119 | ±4.2239 | +1.853 | 0.0639 | . |
| Site: UW (vs UAB) | +2.8222 | 1.9749 | ±3.9497 | +1.429 | 0.1530 |  |
| **Age (years)** | **-0.4922** | 0.0830 | ±0.1660 | **-5.929** | **3.04e-09** | *** |
| **BMI (kg/m2)** | **+0.3412** | 0.1117 | ±0.2233 | **+3.056** | **0.0022** | ** |
| Hypertension | -0.0009 | 1.9203 | ±3.8406 | -0.000 | 0.9996 |  |
| High cholesterol | -0.7938 | 1.7997 | ±3.5995 | -0.441 | 0.6592 |  |
| Kidney disease | -3.0790 | 2.1214 | ±4.2428 | -1.451 | 0.1467 |  |
| Circulatory disease | -3.9071 | 2.0180 | ±4.0361 | -1.936 | 0.0529 | . |
| Avg. daily time < 70 (%) | -1.0249 | 0.5512 | ±1.1024 | -1.859 | 0.0630 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **474**, R² = **0.1722**, Adj R² = **0.1525**, F-statistic = **8.74** (p = **3.87e-14**), Residual SE = **17.164** on **462** df, AIC = **4052.0**, BIC = **4101.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+86.7464** | 8.2403 | ±16.4806 | **+10.527** | **6.48e-26** | *** |
| Education: graduate level (vs college) | -1.2760 | 1.9329 | ±3.8658 | -0.660 | 0.5092 |  |
| Education: high school or below (vs college) | +1.4651 | 2.0970 | ±4.1939 | +0.699 | 0.4847 |  |
| **Site: UCSD (vs UAB)** | **+4.4415** | 2.0931 | ±4.1863 | **+2.122** | **0.0338** | * |
| Site: UW (vs UAB) | +3.6539 | 1.9918 | ±3.9836 | +1.834 | 0.0666 | . |
| **Age (years)** | **-0.4806** | 0.0815 | ±0.1630 | **-5.896** | **3.72e-09** | *** |
| **BMI (kg/m2)** | **+0.3211** | 0.1107 | ±0.2214 | **+2.901** | **0.0037** | ** |
| Hypertension | -0.4698 | 1.9323 | ±3.8646 | -0.243 | 0.8079 |  |
| High cholesterol | -0.3309 | 1.8086 | ±3.6173 | -0.183 | 0.8548 |  |
| Kidney disease | -3.3282 | 2.1094 | ±4.2188 | -1.578 | 0.1146 |  |
| Circulatory disease | -3.8231 | 1.9893 | ±3.9786 | -1.922 | 0.0546 | . |
| **Time 54-250, pooled (%)** | **-0.1008** | 0.0513 | ±0.1027 | **-1.964** | **0.0496** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **474**, R² = **0.1727**, Adj R² = **0.1530**, F-statistic = **8.77** (p = **3.42e-14**), Residual SE = **17.159** on **462** df, AIC = **4051.7**, BIC = **4101.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+87.2531** | 8.3379 | ±16.6758 | **+10.465** | **1.26e-25** | *** |
| Education: graduate level (vs college) | -1.2728 | 1.9317 | ±3.8634 | -0.659 | 0.5100 |  |
| Education: high school or below (vs college) | +1.4550 | 2.0955 | ±4.1909 | +0.694 | 0.4875 |  |
| **Site: UCSD (vs UAB)** | **+4.4547** | 2.0931 | ±4.1861 | **+2.128** | **0.0333** | * |
| Site: UW (vs UAB) | +3.6533 | 1.9903 | ±3.9807 | +1.835 | 0.0664 | . |
| **Age (years)** | **-0.4823** | 0.0815 | ±0.1629 | **-5.921** | **3.20e-09** | *** |
| **BMI (kg/m2)** | **+0.3199** | 0.1110 | ±0.2220 | **+2.881** | **0.0040** | ** |
| Hypertension | -0.4608 | 1.9300 | ±3.8601 | -0.239 | 0.8113 |  |
| High cholesterol | -0.3223 | 1.8087 | ±3.6174 | -0.178 | 0.8586 |  |
| Kidney disease | -3.3675 | 2.1096 | ±4.2192 | -1.596 | 0.1104 |  |
| Circulatory disease | -3.8470 | 1.9896 | ±3.9792 | -1.934 | 0.0532 | . |
| **Avg. daily time 54-250 (%)** | **-0.1045** | 0.0523 | ±0.1046 | **-1.998** | **0.0457** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **474**, R² = **0.1801**, Adj R² = **0.1606**, F-statistic = **9.23** (p = **5.12e-15**), Residual SE = **17.082** on **462** df, AIC = **4047.5**, BIC = **4097.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.1828** | 7.2556 | ±14.5112 | **+10.500** | **8.65e-26** | *** |
| Education: graduate level (vs college) | -1.8600 | 1.9208 | ±3.8416 | -0.968 | 0.3329 |  |
| Education: high school or below (vs college) | +1.3360 | 2.1083 | ±4.2166 | +0.634 | 0.5263 |  |
| **Site: UCSD (vs UAB)** | **+4.6680** | 2.1050 | ±4.2100 | **+2.218** | **0.0266** | * |
| Site: UW (vs UAB) | +3.0946 | 1.9312 | ±3.8625 | +1.602 | 0.1091 |  |
| **Age (years)** | **-0.5139** | 0.0829 | ±0.1658 | **-6.198** | **5.73e-10** | *** |
| **BMI (kg/m2)** | **+0.2995** | 0.1115 | ±0.2230 | **+2.686** | **0.0072** | ** |
| Hypertension | +0.1299 | 1.9169 | ±3.8338 | +0.068 | 0.9460 |  |
| High cholesterol | -0.1342 | 1.8007 | ±3.6013 | -0.075 | 0.9406 |  |
| Kidney disease | -3.0950 | 2.0902 | ±4.1805 | -1.481 | 0.1387 |  |
| **Circulatory disease** | **-4.0790** | 1.9930 | ±3.9861 | **-2.047** | **0.0407** | * |
| **Time 181-250, pooled (%)** | **+0.1701** | 0.0546 | ±0.1093 | **+3.114** | **0.0018** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **474**, R² = **0.1786**, Adj R² = **0.1590**, F-statistic = **9.13** (p = **7.53e-15**), Residual SE = **17.098** on **462** df, AIC = **4048.3**, BIC = **4098.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2368** | 7.2642 | ±14.5284 | **+10.495** | **9.12e-26** | *** |
| Education: graduate level (vs college) | -1.8733 | 1.9255 | ±3.8510 | -0.973 | 0.3306 |  |
| Education: high school or below (vs college) | +1.2908 | 2.1073 | ±4.2147 | +0.613 | 0.5402 |  |
| **Site: UCSD (vs UAB)** | **+4.6953** | 2.1092 | ±4.2185 | **+2.226** | **0.0260** | * |
| Site: UW (vs UAB) | +3.1385 | 1.9357 | ±3.8715 | +1.621 | 0.1049 |  |
| **Age (years)** | **-0.5113** | 0.0829 | ±0.1658 | **-6.168** | **6.94e-10** | *** |
| **BMI (kg/m2)** | **+0.3011** | 0.1119 | ±0.2238 | **+2.691** | **0.0071** | ** |
| Hypertension | +0.1152 | 1.9195 | ±3.8391 | +0.060 | 0.9521 |  |
| High cholesterol | -0.1722 | 1.8023 | ±3.6045 | -0.096 | 0.9239 |  |
| Kidney disease | -3.1201 | 2.0932 | ±4.1864 | -1.491 | 0.1361 |  |
| **Circulatory disease** | **-4.0196** | 1.9990 | ±3.9979 | **-2.011** | **0.0443** | * |
| **Avg. daily time 181-250 (%)** | **+0.1592** | 0.0535 | ±0.1070 | **+2.976** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **474**, R² = **0.1836**, Adj R² = **0.1642**, F-statistic = **9.45** (p = **2.05e-15**), Residual SE = **17.045** on **462** df, AIC = **4045.4**, BIC = **4095.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.2092** | 7.1944 | ±14.3887 | **+10.454** | **1.41e-25** | *** |
| Education: graduate level (vs college) | -1.3982 | 1.9109 | ±3.8218 | -0.732 | 0.4644 |  |
| Education: high school or below (vs college) | +1.0864 | 2.0813 | ±4.1626 | +0.522 | 0.6017 |  |
| **Site: UCSD (vs UAB)** | **+4.7114** | 2.0945 | ±4.1891 | **+2.249** | **0.0245** | * |
| Site: UW (vs UAB) | +3.6052 | 1.9597 | ±3.9193 | +1.840 | 0.0658 | . |
| **Age (years)** | **-0.4890** | 0.0814 | ±0.1629 | **-6.004** | **1.92e-09** | *** |
| **BMI (kg/m2)** | **+0.2927** | 0.1109 | ±0.2218 | **+2.639** | **0.0083** | ** |
| Hypertension | -0.2186 | 1.9165 | ±3.8330 | -0.114 | 0.9092 |  |
| High cholesterol | -0.0667 | 1.8060 | ±3.6120 | -0.037 | 0.9705 |  |
| Kidney disease | -3.2975 | 2.0879 | ±4.1757 | -1.579 | 0.1143 |  |
| **Circulatory disease** | **-4.1065** | 1.9752 | ±3.9505 | **-2.079** | **0.0376** | * |
| **Time > 180 (%)** | **+0.1067** | 0.0321 | ±0.0643 | **+3.320** | **9.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **474**, R² = **0.1832**, Adj R² = **0.1638**, F-statistic = **9.42** (p = **2.28e-15**), Residual SE = **17.050** on **462** df, AIC = **4045.6**, BIC = **4095.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.4031** | 7.2039 | ±14.4077 | **+10.467** | **1.22e-25** | *** |
| Education: graduate level (vs college) | -1.4303 | 1.9126 | ±3.8252 | -0.748 | 0.4546 |  |
| Education: high school or below (vs college) | +1.0512 | 2.0814 | ±4.1628 | +0.505 | 0.6135 |  |
| **Site: UCSD (vs UAB)** | **+4.7448** | 2.0978 | ±4.1955 | **+2.262** | **0.0237** | * |
| Site: UW (vs UAB) | +3.6047 | 1.9607 | ±3.9214 | +1.839 | 0.0660 | . |
| **Age (years)** | **-0.4905** | 0.0816 | ±0.1631 | **-6.015** | **1.80e-09** | *** |
| **BMI (kg/m2)** | **+0.2924** | 0.1114 | ±0.2228 | **+2.625** | **0.0087** | ** |
| Hypertension | -0.1961 | 1.9165 | ±3.8330 | -0.102 | 0.9185 |  |
| High cholesterol | -0.0829 | 1.8063 | ±3.6126 | -0.046 | 0.9634 |  |
| Kidney disease | -3.3402 | 2.0893 | ±4.1786 | -1.599 | 0.1099 |  |
| **Circulatory disease** | **-4.0950** | 1.9785 | ±3.9569 | **-2.070** | **0.0385** | * |
| **Avg. daily time > 180 (%)** | **+0.1049** | 0.0319 | ±0.0638 | **+3.287** | **0.0010** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **474**, R² = **0.1766**, Adj R² = **0.1570**, F-statistic = **9.01** (p = **1.25e-14**), Residual SE = **17.119** on **462** df, AIC = **4049.5**, BIC = **4099.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5117** | 7.2101 | ±14.4201 | **+10.612** | **2.63e-26** | *** |
| Education: graduate level (vs college) | -1.3179 | 1.9302 | ±3.8604 | -0.683 | 0.4948 |  |
| Education: high school or below (vs college) | +1.3228 | 2.0797 | ±4.1594 | +0.636 | 0.5247 |  |
| **Site: UCSD (vs UAB)** | **+4.6807** | 2.1018 | ±4.2036 | **+2.227** | **0.0259** | * |
| Site: UW (vs UAB) | +3.4182 | 1.9536 | ±3.9073 | +1.750 | 0.0802 | . |
| **Age (years)** | **-0.4824** | 0.0825 | ±0.1650 | **-5.847** | **5.01e-09** | *** |
| **BMI (kg/m2)** | **+0.2864** | 0.1117 | ±0.2234 | **+2.564** | **0.0104** | * |
| Hypertension | -0.2825 | 1.9210 | ±3.8420 | -0.147 | 0.8831 |  |
| High cholesterol | -0.0279 | 1.8132 | ±3.6265 | -0.015 | 0.9877 |  |
| Kidney disease | -3.2170 | 2.1047 | ±4.2093 | -1.529 | 0.1264 |  |
| **Circulatory disease** | **-4.0372** | 1.9844 | ±3.9688 | **-2.034** | **0.0419** | * |
| **Nocturnal time > 180 (%)** | **+0.0772** | 0.0283 | ±0.0566 | **+2.726** | **0.0064** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **474**, R² = **0.1722**, Adj R² = **0.1525**, F-statistic = **8.74** (p = **3.81e-14**), Residual SE = **17.164** on **462** df, AIC = **4052.0**, BIC = **4101.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.6687** | 7.1663 | ±14.3325 | **+10.699** | **1.03e-26** | *** |
| Education: graduate level (vs college) | -1.2776 | 1.9327 | ±3.8654 | -0.661 | 0.5086 |  |
| Education: high school or below (vs college) | +1.4593 | 2.0968 | ±4.1937 | +0.696 | 0.4865 |  |
| **Site: UCSD (vs UAB)** | **+4.4366** | 2.0929 | ±4.1858 | **+2.120** | **0.0340** | * |
| Site: UW (vs UAB) | +3.6477 | 1.9908 | ±3.9816 | +1.832 | 0.0669 | . |
| **Age (years)** | **-0.4805** | 0.0815 | ±0.1630 | **-5.894** | **3.76e-09** | *** |
| **BMI (kg/m2)** | **+0.3210** | 0.1107 | ±0.2215 | **+2.899** | **0.0037** | ** |
| Hypertension | -0.4631 | 1.9315 | ±3.8629 | -0.240 | 0.8105 |  |
| High cholesterol | -0.3351 | 1.8081 | ±3.6163 | -0.185 | 0.8530 |  |
| Kidney disease | -3.3281 | 2.1094 | ±4.2189 | -1.578 | 0.1146 |  |
| Circulatory disease | -3.8288 | 1.9893 | ±3.9787 | -1.925 | 0.0543 | . |
| **Time > 250 (%)** | **+0.1011** | 0.0513 | ±0.1025 | **+1.972** | **0.0486** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 474)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **474**, R² = **0.1728**, Adj R² = **0.1531**, F-statistic = **8.78** (p = **3.27e-14**), Residual SE = **17.158** on **462** df, AIC = **4051.6**, BIC = **4101.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.7945** | 7.1692 | ±14.3383 | **+10.712** | **8.96e-27** | *** |
| Education: graduate level (vs college) | -1.2723 | 1.9315 | ±3.8629 | -0.659 | 0.5101 |  |
| Education: high school or below (vs college) | +1.4454 | 2.0951 | ±4.1902 | +0.690 | 0.4903 |  |
| **Site: UCSD (vs UAB)** | **+4.4501** | 2.0927 | ±4.1854 | **+2.127** | **0.0335** | * |
| Site: UW (vs UAB) | +3.6486 | 1.9893 | ±3.9787 | +1.834 | 0.0666 | . |
| **Age (years)** | **-0.4821** | 0.0815 | ±0.1629 | **-5.919** | **3.24e-09** | *** |
| **BMI (kg/m2)** | **+0.3197** | 0.1111 | ±0.2222 | **+2.879** | **0.0040** | ** |
| Hypertension | -0.4550 | 1.9292 | ±3.8583 | -0.236 | 0.8136 |  |
| High cholesterol | -0.3265 | 1.8079 | ±3.6159 | -0.181 | 0.8567 |  |
| Kidney disease | -3.3669 | 2.1094 | ±4.2189 | -1.596 | 0.1105 |  |
| Circulatory disease | -3.8538 | 1.9896 | ±3.9793 | -1.937 | 0.0528 | . |
| **Avg. daily time > 250 (%)** | **+0.1054** | 0.0523 | ±0.1046 | **+2.015** | **0.0439** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
