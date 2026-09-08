# Phase 6 model output tables - All (analysis base) - Total analysis base - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 2,135; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1032**, F-statistic = **25.55** (p = **3.02e-46**), Residual SE = **4.715** on **2124** df, AIC = **12691.3**, BIC = **12753.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5053** | 0.8327 | ±1.6653 | **+10.215** | **1.71e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8470** | 0.2143 | ±0.4285 | **-3.953** | **7.72e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2921** | 0.4056 | ±0.8112 | **+3.186** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.0775 | 0.2740 | ±0.5480 | +0.283 | 0.7772 |  |
| Site: UW (vs UAB) | +0.0731 | 0.2537 | ±0.5073 | +0.288 | 0.7734 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.909** | **3.79e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.737** | **2.17e-06** | *** |
| Hypertension | +0.2910 | 0.2264 | ±0.4527 | +1.285 | 0.1986 |  |
| **High cholesterol** | **+0.6623** | 0.2123 | ±0.4246 | **+3.120** | **0.0018** | ** |
| **Kidney disease** | **+0.9434** | 0.3768 | ±0.7536 | **+2.504** | **0.0123** | * |
| **Circulatory disease** | **+1.1324** | 0.3188 | ±0.6375 | **+3.553** | **3.81e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2135**, R² = **0.1083**, Adj R² = **0.1037**, F-statistic = **23.44** (p = **5.34e-46**), Residual SE = **4.713** on **2123** df, AIC = **12691.1**, BIC = **12759.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7300** | 1.0312 | ±2.0623 | **+7.496** | **6.56e-14** | *** |
| **Education: graduate level (vs college)** | **-0.8280** | 0.2142 | ±0.4283 | **-3.866** | **1.11e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2328** | 0.4045 | ±0.8091 | **+3.047** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.0916 | 0.2743 | ±0.5486 | +0.334 | 0.7383 |  |
| Site: UW (vs UAB) | +0.0923 | 0.2547 | ±0.5095 | +0.363 | 0.7170 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0191 | **-9.943** | **2.70e-23** | *** |
| **BMI (kg/m2)** | **+0.0750** | 0.0165 | ±0.0331 | **+4.534** | **5.78e-06** | *** |
| Hypertension | +0.2586 | 0.2275 | ±0.4550 | +1.137 | 0.2557 |  |
| **High cholesterol** | **+0.6341** | 0.2123 | ±0.4247 | **+2.986** | **0.0028** | ** |
| **Kidney disease** | **+0.9170** | 0.3780 | ±0.7560 | **+2.426** | **0.0153** | * |
| **Circulatory disease** | **+1.1185** | 0.3179 | ±0.6359 | **+3.518** | **4.35e-04** | *** |
| HbA1c (%) | +0.1526 | 0.1196 | ±0.2392 | +1.276 | 0.2020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.26** (p = **1.24e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.8**, BIC = **12760.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2669** | 0.9142 | ±1.8283 | **+9.043** | **1.52e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8420** | 0.2144 | ±0.4287 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2668** | 0.4071 | ±0.8143 | **+3.112** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0869 | 0.2746 | ±0.5492 | +0.316 | 0.7516 |  |
| Site: UW (vs UAB) | +0.0784 | 0.2541 | ±0.5082 | +0.308 | 0.7577 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0191 | **-9.902** | **4.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0329 | **+4.667** | **3.06e-06** | *** |
| Hypertension | +0.2763 | 0.2269 | ±0.4538 | +1.218 | 0.2234 |  |
| **High cholesterol** | **+0.6531** | 0.2124 | ±0.4248 | **+3.075** | **0.0021** | ** |
| **Kidney disease** | **+0.9192** | 0.3805 | ±0.7611 | **+2.416** | **0.0157** | * |
| **Circulatory disease** | **+1.1255** | 0.3185 | ±0.6370 | **+3.533** | **4.10e-04** | *** |
| Mean glucose (mg/dL) | +0.0022 | 0.0035 | ±0.0071 | +0.623 | 0.5335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.26** (p = **1.24e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.8**, BIC = **12760.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9625** | 1.2006 | ±2.4013 | **+6.632** | **3.31e-11** | *** |
| **Education: graduate level (vs college)** | **-0.8420** | 0.2144 | ±0.4287 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2668** | 0.4071 | ±0.8143 | **+3.112** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0869 | 0.2746 | ±0.5492 | +0.316 | 0.7516 |  |
| Site: UW (vs UAB) | +0.0784 | 0.2541 | ±0.5082 | +0.308 | 0.7577 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0191 | **-9.902** | **4.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0329 | **+4.667** | **3.06e-06** | *** |
| Hypertension | +0.2763 | 0.2269 | ±0.4538 | +1.218 | 0.2234 |  |
| **High cholesterol** | **+0.6531** | 0.2124 | ±0.4248 | **+3.075** | **0.0021** | ** |
| **Kidney disease** | **+0.9192** | 0.3805 | ±0.7611 | **+2.416** | **0.0157** | * |
| **Circulatory disease** | **+1.1255** | 0.3185 | ±0.6370 | **+3.533** | **4.10e-04** | *** |
| GMI (%) | +0.0919 | 0.1476 | ±0.2953 | +0.623 | 0.5335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.39e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.7**, BIC = **12759.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0806** | 0.9171 | ±1.8341 | **+8.811** | **1.24e-18** | *** |
| **Education: graduate level (vs college)** | **-0.8369** | 0.2144 | ±0.4288 | **-3.903** | **9.48e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2491** | 0.4068 | ±0.8137 | **+3.070** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.0897 | 0.2742 | ±0.5483 | +0.327 | 0.7434 |  |
| Site: UW (vs UAB) | +0.0783 | 0.2540 | ±0.5080 | +0.308 | 0.7579 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.898** | **4.26e-23** | *** |
| **BMI (kg/m2)** | **+0.0753** | 0.0165 | ±0.0331 | **+4.556** | **5.22e-06** | *** |
| Hypertension | +0.2704 | 0.2264 | ±0.4528 | +1.194 | 0.2323 |  |
| **High cholesterol** | **+0.6450** | 0.2124 | ±0.4247 | **+3.037** | **0.0024** | ** |
| **Kidney disease** | **+0.9138** | 0.3800 | ±0.7600 | **+2.405** | **0.0162** | * |
| **Circulatory disease** | **+1.1225** | 0.3185 | ±0.6370 | **+3.524** | **4.25e-04** | *** |
| Nocturnal mean 00-06h (mg/dL) | +0.0039 | 0.0036 | ±0.0071 | +1.104 | 0.2695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.40** (p = **6.58e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.5**, BIC = **12759.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2980** | 0.8500 | ±1.7000 | **+9.762** | **1.64e-22** | *** |
| **Education: graduate level (vs college)** | **-0.8307** | 0.2145 | ±0.4289 | **-3.873** | **1.07e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2492** | 0.4063 | ±0.8125 | **+3.075** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1014 | 0.2747 | ±0.5494 | +0.369 | 0.7121 |  |
| Site: UW (vs UAB) | +0.0940 | 0.2542 | ±0.5084 | +0.370 | 0.7114 |  |
| **Age (years)** | **-0.0951** | 0.0095 | ±0.0191 | **-9.968** | **2.10e-23** | *** |
| **BMI (kg/m2)** | **+0.0766** | 0.0165 | ±0.0329 | **+4.654** | **3.25e-06** | *** |
| Hypertension | +0.2585 | 0.2275 | ±0.4550 | +1.136 | 0.2559 |  |
| **High cholesterol** | **+0.6494** | 0.2121 | ±0.4243 | **+3.062** | **0.0022** | ** |
| **Kidney disease** | **+0.8652** | 0.3830 | ±0.7660 | **+2.259** | **0.0239** | * |
| **Circulatory disease** | **+1.1181** | 0.3188 | ±0.6376 | **+3.507** | **4.53e-04** | *** |
| Glucose SD, pooled (mg/dL) | +0.0121 | 0.0095 | ±0.0191 | +1.265 | 0.2059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1030**, F-statistic = **23.29** (p = **1.12e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3750** | 0.8483 | ±1.6966 | **+9.873** | **5.47e-23** | *** |
| **Education: graduate level (vs college)** | **-0.8379** | 0.2143 | ±0.4286 | **-3.910** | **9.24e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2646** | 0.4068 | ±0.8135 | **+3.109** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0915 | 0.2748 | ±0.5496 | +0.333 | 0.7392 |  |
| Site: UW (vs UAB) | +0.0846 | 0.2540 | ±0.5081 | +0.333 | 0.7390 |  |
| **Age (years)** | **-0.0948** | 0.0096 | ±0.0191 | **-9.916** | **3.53e-23** | *** |
| **BMI (kg/m2)** | **+0.0771** | 0.0164 | ±0.0329 | **+4.694** | **2.68e-06** | *** |
| Hypertension | +0.2711 | 0.2277 | ±0.4554 | +1.191 | 0.2338 |  |
| **High cholesterol** | **+0.6541** | 0.2123 | ±0.4246 | **+3.081** | **0.0021** | ** |
| **Kidney disease** | **+0.8937** | 0.3833 | ±0.7665 | **+2.332** | **0.0197** | * |
| **Circulatory disease** | **+1.1248** | 0.3189 | ±0.6378 | **+3.527** | **4.20e-04** | *** |
| Avg. daily SD (mg/dL) | +0.0085 | 0.0107 | ±0.0214 | +0.794 | 0.4273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1031**, F-statistic = **23.29** (p = **1.10e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2281** | 0.8967 | ±1.7934 | **+9.176** | **4.48e-20** | *** |
| **Education: graduate level (vs college)** | **-0.8368** | 0.2145 | ±0.4290 | **-3.901** | **9.57e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2769** | 0.4059 | ±0.8117 | **+3.146** | **0.0017** | ** |
| Site: UCSD (vs UAB) | +0.0928 | 0.2747 | ±0.5494 | +0.338 | 0.7354 |  |
| Site: UW (vs UAB) | +0.0878 | 0.2538 | ±0.5075 | +0.346 | 0.7294 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0190 | **-9.962** | **2.24e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.721** | **2.35e-06** | *** |
| Hypertension | +0.2732 | 0.2273 | ±0.4545 | +1.202 | 0.2293 |  |
| **High cholesterol** | **+0.6603** | 0.2123 | ±0.4245 | **+3.111** | **0.0019** | ** |
| **Kidney disease** | **+0.8958** | 0.3795 | ±0.7590 | **+2.361** | **0.0182** | * |
| **Circulatory disease** | **+1.1257** | 0.3193 | ±0.6385 | **+3.526** | **4.22e-04** | *** |
| CV (%) | +0.0172 | 0.0197 | ±0.0395 | +0.872 | 0.3832 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1031**, F-statistic = **23.31** (p = **1.02e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.4**, BIC = **12760.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.9759** | 0.9561 | ±1.9121 | **+9.388** | **6.09e-21** | *** |
| **Education: graduate level (vs college)** | **-0.8358** | 0.2147 | ±0.4293 | **-3.894** | **9.88e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2740** | 0.4057 | ±0.8114 | **+3.140** | **0.0017** | ** |
| Site: UCSD (vs UAB) | +0.0919 | 0.2746 | ±0.5491 | +0.335 | 0.7377 |  |
| Site: UW (vs UAB) | +0.0842 | 0.2536 | ±0.5072 | +0.332 | 0.7398 |  |
| **Age (years)** | **-0.0949** | 0.0095 | ±0.0191 | **-9.961** | **2.26e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.724** | **2.31e-06** | *** |
| Hypertension | +0.2708 | 0.2273 | ±0.4547 | +1.191 | 0.2336 |  |
| **High cholesterol** | **+0.6590** | 0.2123 | ±0.4246 | **+3.104** | **0.0019** | ** |
| **Kidney disease** | **+0.9027** | 0.3780 | ±0.7559 | **+2.388** | **0.0169** | * |
| **Circulatory disease** | **+1.1247** | 0.3191 | ±0.6381 | **+3.525** | **4.24e-04** | *** |
| Mean / SD ratio | -0.0737 | 0.0750 | ±0.1501 | -0.982 | 0.3263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1028**, F-statistic = **23.22** (p = **1.54e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.3**, BIC = **12761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6053** | 0.9642 | ±1.9283 | **+8.925** | **4.45e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8450** | 0.2144 | ±0.4288 | **-3.941** | **8.12e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2882** | 0.4060 | ±0.8119 | **+3.173** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0796 | 0.2743 | ±0.5487 | +0.290 | 0.7716 |  |
| Site: UW (vs UAB) | +0.0749 | 0.2535 | ±0.5071 | +0.295 | 0.7677 |  |
| **Age (years)** | **-0.0942** | 0.0095 | ±0.0191 | **-9.869** | **5.67e-23** | *** |
| **BMI (kg/m2)** | **+0.0776** | 0.0164 | ±0.0328 | **+4.733** | **2.21e-06** | *** |
| Hypertension | +0.2872 | 0.2276 | ±0.4553 | +1.261 | 0.2071 |  |
| **High cholesterol** | **+0.6618** | 0.2124 | ±0.4248 | **+3.116** | **0.0018** | ** |
| **Kidney disease** | **+0.9351** | 0.3782 | ±0.7565 | **+2.472** | **0.0134** | * |
| **Circulatory disease** | **+1.1318** | 0.3190 | ±0.6380 | **+3.548** | **3.89e-04** | *** |
| Avg. daily mean/SD | -0.0133 | 0.0641 | ±0.1281 | -0.207 | 0.8359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2135**, R² = **0.1096**, Adj R² = **0.1049**, F-statistic = **23.75** (p = **1.27e-46**), Residual SE = **4.710** on **2123** df, AIC = **12688.1**, BIC = **12756.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4335** | 0.9517 | ±1.9035 | **+7.810** | **5.70e-15** | *** |
| **Education: graduate level (vs college)** | **-0.8195** | 0.2144 | ±0.4288 | **-3.822** | **1.32e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2457** | 0.4046 | ±0.8092 | **+3.079** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1169 | 0.2740 | ±0.5480 | +0.427 | 0.6696 |  |
| Site: UW (vs UAB) | +0.1333 | 0.2551 | ±0.5102 | +0.523 | 0.6013 |  |
| **Age (years)** | **-0.0936** | 0.0095 | ±0.0190 | **-9.876** | **5.27e-23** | *** |
| **BMI (kg/m2)** | **+0.0765** | 0.0164 | ±0.0329 | **+4.653** | **3.27e-06** | *** |
| Hypertension | +0.2777 | 0.2265 | ±0.4530 | +1.226 | 0.2201 |  |
| **High cholesterol** | **+0.6652** | 0.2121 | ±0.4242 | **+3.136** | **0.0017** | ** |
| **Kidney disease** | **+0.8771** | 0.3781 | ±0.7562 | **+2.320** | **0.0204** | * |
| **Circulatory disease** | **+1.1234** | 0.3193 | ±0.6385 | **+3.519** | **4.34e-04** | *** |
| **MAG (mg/dL/h)** | **+0.0264** | 0.0122 | ±0.0245 | **+2.155** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.27** (p = **1.19e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.7**, BIC = **12760.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3150** | 0.8713 | ±1.7426 | **+9.543** | **1.39e-21** | *** |
| **Education: graduate level (vs college)** | **-0.8390** | 0.2143 | ±0.4286 | **-3.915** | **9.06e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2680** | 0.4066 | ±0.8133 | **+3.118** | **0.0018** | ** |
| Site: UCSD (vs UAB) | +0.0912 | 0.2748 | ±0.5496 | +0.332 | 0.7399 |  |
| Site: UW (vs UAB) | +0.0841 | 0.2539 | ±0.5078 | +0.331 | 0.7405 |  |
| **Age (years)** | **-0.0946** | 0.0095 | ±0.0191 | **-9.917** | **3.51e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.723** | **2.33e-06** | *** |
| Hypertension | +0.2759 | 0.2274 | ±0.4547 | +1.214 | 0.2249 |  |
| **High cholesterol** | **+0.6557** | 0.2124 | ±0.4248 | **+3.087** | **0.0020** | ** |
| **Kidney disease** | **+0.9010** | 0.3818 | ±0.7637 | **+2.360** | **0.0183** | * |
| **Circulatory disease** | **+1.1247** | 0.3190 | ±0.6380 | **+3.526** | **4.22e-04** | *** |
| Avg. daily range (mg/dL) | +0.0021 | 0.0028 | ±0.0056 | +0.739 | 0.4599 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2135**, R² = **0.1122**, Adj R² = **0.1076**, F-statistic = **24.39** (p = **6.18e-48**), Residual SE = **4.703** on **2123** df, AIC = **12681.8**, BIC = **12749.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1921** | 0.8360 | ±1.6720 | **+9.799** | **1.14e-22** | *** |
| **Education: graduate level (vs college)** | **-0.7982** | 0.2144 | ±0.4288 | **-3.723** | **1.97e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2217** | 0.4038 | ±0.8077 | **+3.025** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +0.1284 | 0.2732 | ±0.5465 | +0.470 | 0.6384 |  |
| Site: UW (vs UAB) | +0.1226 | 0.2537 | ±0.5073 | +0.484 | 0.6287 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0190 | **-9.929** | **3.13e-23** | *** |
| **BMI (kg/m2)** | **+0.0730** | 0.0165 | ±0.0329 | **+4.434** | **9.26e-06** | *** |
| Hypertension | +0.2341 | 0.2264 | ±0.4529 | +1.034 | 0.3012 |  |
| **High cholesterol** | **+0.6295** | 0.2113 | ±0.4226 | **+2.979** | **0.0029** | ** |
| **Kidney disease** | **+0.8212** | 0.3791 | ±0.7582 | **+2.166** | **0.0303** | * |
| **Circulatory disease** | **+1.0728** | 0.3171 | ±0.6343 | **+3.383** | **7.17e-04** | *** |
| **SD of daily means (mg/dL)** | **+0.0564** | 0.0175 | ±0.0349 | **+3.227** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.40** (p = **6.52e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.5**, BIC = **12759.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2275** | 1.0242 | ±2.0484 | **+9.009** | **2.07e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8327** | 0.2145 | ±0.4290 | **-3.882** | **1.04e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2461** | 0.4068 | ±0.8137 | **+3.063** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1047 | 0.2751 | ±0.5502 | +0.381 | 0.7036 |  |
| Site: UW (vs UAB) | +0.0931 | 0.2547 | ±0.5094 | +0.365 | 0.7148 |  |
| **Age (years)** | **-0.0947** | 0.0095 | ±0.0190 | **-9.946** | **2.62e-23** | *** |
| **BMI (kg/m2)** | **+0.0761** | 0.0165 | ±0.0329 | **+4.621** | **3.83e-06** | *** |
| Hypertension | +0.2705 | 0.2265 | ±0.4531 | +1.194 | 0.2324 |  |
| **High cholesterol** | **+0.6494** | 0.2122 | ±0.4245 | **+3.060** | **0.0022** | ** |
| **Kidney disease** | **+0.8904** | 0.3821 | ±0.7642 | **+2.330** | **0.0198** | * |
| **Circulatory disease** | **+1.1183** | 0.3185 | ±0.6370 | **+3.511** | **4.46e-04** | *** |
| Time in range 70-180, pooled (%) | -0.0071 | 0.0059 | ±0.0119 | -1.199 | 0.2305 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.39** (p = **6.93e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.6**, BIC = **12759.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2039** | 1.0265 | ±2.0530 | **+8.966** | **3.07e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8336** | 0.2145 | ±0.4290 | **-3.887** | **1.02e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2472** | 0.4069 | ±0.8138 | **+3.065** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1040 | 0.2751 | ±0.5501 | +0.378 | 0.7053 |  |
| Site: UW (vs UAB) | +0.0924 | 0.2547 | ±0.5093 | +0.363 | 0.7167 |  |
| **Age (years)** | **-0.0947** | 0.0095 | ±0.0190 | **-9.944** | **2.67e-23** | *** |
| **BMI (kg/m2)** | **+0.0761** | 0.0165 | ±0.0330 | **+4.621** | **3.82e-06** | *** |
| Hypertension | +0.2717 | 0.2265 | ±0.4530 | +1.199 | 0.2304 |  |
| **High cholesterol** | **+0.6495** | 0.2123 | ±0.4245 | **+3.060** | **0.0022** | ** |
| **Kidney disease** | **+0.8913** | 0.3820 | ±0.7640 | **+2.333** | **0.0196** | * |
| **Circulatory disease** | **+1.1188** | 0.3185 | ±0.6371 | **+3.512** | **4.44e-04** | *** |
| Avg. daily time in range 70-180 (%) | -0.0069 | 0.0059 | ±0.0119 | -1.156 | 0.2476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2135**, R² = **0.1075**, Adj R² = **0.1029**, F-statistic = **23.26** (p = **1.29e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.9**, BIC = **12760.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4340** | 0.8443 | ±1.6887 | **+9.989** | **1.70e-23** | *** |
| **Education: graduate level (vs college)** | **-0.8434** | 0.2146 | ±0.4292 | **-3.929** | **8.51e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3056** | 0.4057 | ±0.8114 | **+3.218** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0946 | 0.2747 | ±0.5493 | +0.344 | 0.7307 |  |
| Site: UW (vs UAB) | +0.0825 | 0.2538 | ±0.5076 | +0.325 | 0.7450 |  |
| **Age (years)** | **-0.0936** | 0.0095 | ±0.0191 | **-9.806** | **1.06e-22** | *** |
| **BMI (kg/m2)** | **+0.0773** | 0.0164 | ±0.0327 | **+4.723** | **2.32e-06** | *** |
| Hypertension | +0.2897 | 0.2266 | ±0.4532 | +1.278 | 0.2012 |  |
| **High cholesterol** | **+0.6712** | 0.2123 | ±0.4247 | **+3.161** | **0.0016** | ** |
| **Kidney disease** | **+0.9479** | 0.3768 | ±0.7537 | **+2.515** | **0.0119** | * |
| **Circulatory disease** | **+1.1218** | 0.3205 | ±0.6411 | **+3.500** | **4.66e-04** | *** |
| Any reading < 54 during wear (0/1) | +0.1443 | 0.2281 | ±0.4562 | +0.632 | 0.5271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2135**, R² = **0.1075**, Adj R² = **0.1029**, F-statistic = **23.24** (p = **1.38e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.1**, BIC = **12761.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5394** | 0.8377 | ±1.6754 | **+10.194** | **2.11e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8491** | 0.2144 | ±0.4288 | **-3.960** | **7.50e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2838** | 0.4063 | ±0.8126 | **+3.160** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.0623 | 0.2754 | ±0.5508 | +0.226 | 0.8210 |  |
| Site: UW (vs UAB) | +0.0608 | 0.2547 | ±0.5094 | +0.239 | 0.8113 |  |
| **Age (years)** | **-0.0941** | 0.0095 | ±0.0190 | **-9.917** | **3.52e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.736** | **2.18e-06** | *** |
| Hypertension | +0.2888 | 0.2264 | ±0.4529 | +1.276 | 0.2021 |  |
| **High cholesterol** | **+0.6560** | 0.2125 | ±0.4251 | **+3.087** | **0.0020** | ** |
| **Kidney disease** | **+0.9428** | 0.3767 | ±0.7534 | **+2.503** | **0.0123** | * |
| **Circulatory disease** | **+1.1361** | 0.3191 | ±0.6383 | **+3.560** | **3.71e-04** | *** |
| Time < 54 (%) | -0.1034 | 0.1729 | ±0.3459 | -0.598 | 0.5500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1027**, F-statistic = **23.22** (p = **1.57e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.3**, BIC = **12761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5095** | 0.8355 | ±1.6710 | **+10.185** | **2.32e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8476** | 0.2145 | ±0.4290 | **-3.952** | **7.75e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2907** | 0.4064 | ±0.8127 | **+3.176** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0751 | 0.2747 | ±0.5495 | +0.273 | 0.7847 |  |
| Site: UW (vs UAB) | +0.0706 | 0.2545 | ±0.5089 | +0.278 | 0.7814 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.907** | **3.90e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.736** | **2.18e-06** | *** |
| Hypertension | +0.2905 | 0.2266 | ±0.4532 | +1.282 | 0.1999 |  |
| **High cholesterol** | **+0.6613** | 0.2124 | ±0.4247 | **+3.114** | **0.0018** | ** |
| **Kidney disease** | **+0.9435** | 0.3769 | ±0.7537 | **+2.504** | **0.0123** | * |
| **Circulatory disease** | **+1.1332** | 0.3194 | ±0.6387 | **+3.548** | **3.88e-04** | *** |
| Avg. daily time < 54 (%) | -0.0234 | 0.2390 | ±0.4780 | -0.098 | 0.9219 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.27** (p = **1.21e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.8**, BIC = **12760.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4591** | 0.8357 | ±1.6714 | **+10.122** | **4.40e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8398** | 0.2146 | ±0.4292 | **-3.914** | **9.09e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3017** | 0.4055 | ±0.8111 | **+3.210** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0930 | 0.2739 | ±0.5477 | +0.340 | 0.7341 |  |
| Site: UW (vs UAB) | +0.0883 | 0.2534 | ±0.5068 | +0.348 | 0.7276 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.893** | **4.45e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.723** | **2.32e-06** | *** |
| Hypertension | +0.2956 | 0.2263 | ±0.4527 | +1.306 | 0.1916 |  |
| **High cholesterol** | **+0.6686** | 0.2124 | ±0.4248 | **+3.147** | **0.0016** | ** |
| **Kidney disease** | **+0.9435** | 0.3768 | ±0.7535 | **+2.504** | **0.0123** | * |
| **Circulatory disease** | **+1.1295** | 0.3194 | ±0.6388 | **+3.536** | **4.06e-04** | *** |
| Time 54-69, pooled (%) | +0.0530 | 0.0717 | ±0.1433 | +0.740 | 0.4596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2135**, R² = **0.1078**, Adj R² = **0.1031**, F-statistic = **23.31** (p = **1.01e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.4**, BIC = **12760.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4588** | 0.8343 | ±1.6686 | **+10.139** | **3.72e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8368** | 0.2146 | ±0.4291 | **-3.900** | **9.63e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3041** | 0.4055 | ±0.8110 | **+3.216** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0944 | 0.2737 | ±0.5475 | +0.345 | 0.7303 |  |
| Site: UW (vs UAB) | +0.0929 | 0.2534 | ±0.5068 | +0.367 | 0.7139 |  |
| **Age (years)** | **-0.0941** | 0.0095 | ±0.0190 | **-9.909** | **3.80e-23** | *** |
| **BMI (kg/m2)** | **+0.0774** | 0.0164 | ±0.0328 | **+4.720** | **2.36e-06** | *** |
| Hypertension | +0.2970 | 0.2264 | ±0.4527 | +1.312 | 0.1895 |  |
| **High cholesterol** | **+0.6695** | 0.2123 | ±0.4246 | **+3.154** | **0.0016** | ** |
| **Kidney disease** | **+0.9441** | 0.3766 | ±0.7531 | **+2.507** | **0.0122** | * |
| **Circulatory disease** | **+1.1295** | 0.3194 | ±0.6387 | **+3.537** | **4.05e-04** | *** |
| Avg. daily time 54-69 (%) | +0.0680 | 0.0709 | ±0.1418 | +0.959 | 0.3374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2135**, R² = **0.1075**, Adj R² = **0.1028**, F-statistic = **23.23** (p = **1.43e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.1**, BIC = **12761.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4742** | 0.8372 | ±1.6743 | **+10.123** | **4.39e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8430** | 0.2146 | ±0.4292 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2989** | 0.4058 | ±0.8115 | **+3.201** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.0889 | 0.2743 | ±0.5487 | +0.324 | 0.7458 |  |
| Site: UW (vs UAB) | +0.0836 | 0.2538 | ±0.5076 | +0.329 | 0.7419 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.894** | **4.41e-23** | *** |
| **BMI (kg/m2)** | **+0.0776** | 0.0164 | ±0.0328 | **+4.730** | **2.25e-06** | *** |
| Hypertension | +0.2938 | 0.2264 | ±0.4528 | +1.298 | 0.1944 |  |
| **High cholesterol** | **+0.6670** | 0.2125 | ±0.4251 | **+3.138** | **0.0017** | ** |
| **Kidney disease** | **+0.9436** | 0.3769 | ±0.7539 | **+2.503** | **0.0123** | * |
| **Circulatory disease** | **+1.1301** | 0.3195 | ±0.6389 | **+3.538** | **4.04e-04** | *** |
| Time < 70 (%) | +0.0259 | 0.0576 | ±0.1151 | +0.450 | 0.6524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.28** (p = **1.18e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.7**, BIC = **12760.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4660** | 0.8350 | ±1.6699 | **+10.139** | **3.70e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8389** | 0.2146 | ±0.4292 | **-3.909** | **9.27e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3030** | 0.4057 | ±0.8114 | **+3.212** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0936 | 0.2739 | ±0.5479 | +0.342 | 0.7325 |  |
| Site: UW (vs UAB) | +0.0911 | 0.2536 | ±0.5073 | +0.359 | 0.7194 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.910** | **3.78e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.725** | **2.30e-06** | *** |
| Hypertension | +0.2960 | 0.2264 | ±0.4529 | +1.307 | 0.1912 |  |
| **High cholesterol** | **+0.6692** | 0.2123 | ±0.4247 | **+3.152** | **0.0016** | ** |
| **Kidney disease** | **+0.9437** | 0.3767 | ±0.7534 | **+2.505** | **0.0122** | * |
| **Circulatory disease** | **+1.1291** | 0.3194 | ±0.6389 | **+3.535** | **4.08e-04** | *** |
| Avg. daily time < 70 (%) | +0.0457 | 0.0593 | ±0.1185 | +0.771 | 0.4406 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1082**, Adj R² = **0.1035**, F-statistic = **23.41** (p = **6.32e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.4**, BIC = **12759.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7792** | 1.4342 | ±2.8684 | **+6.819** | **9.20e-12** | *** |
| **Education: graduate level (vs college)** | **-0.8304** | 0.2146 | ±0.4292 | **-3.869** | **1.09e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2487** | 0.4056 | ±0.8111 | **+3.079** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1000 | 0.2746 | ±0.5492 | +0.364 | 0.7157 |  |
| Site: UW (vs UAB) | +0.0973 | 0.2554 | ±0.5107 | +0.381 | 0.7032 |  |
| **Age (years)** | **-0.0938** | 0.0095 | ±0.0190 | **-9.880** | **5.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0329 | **+4.662** | **3.12e-06** | *** |
| Hypertension | +0.2763 | 0.2263 | ±0.4526 | +1.221 | 0.2221 |  |
| **High cholesterol** | **+0.6579** | 0.2121 | ±0.4242 | **+3.102** | **0.0019** | ** |
| **Kidney disease** | **+0.9102** | 0.3792 | ±0.7584 | **+2.400** | **0.0164** | * |
| **Circulatory disease** | **+1.1188** | 0.3190 | ±0.6380 | **+3.507** | **4.53e-04** | *** |
| Time 54-250, pooled (%) | -0.0130 | 0.0120 | ±0.0241 | -1.085 | 0.2781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.41e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.8**, BIC = **12759.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.6843** | 1.4604 | ±2.9208 | **+6.631** | **3.33e-11** | *** |
| **Education: graduate level (vs college)** | **-0.8320** | 0.2146 | ±0.4292 | **-3.877** | **1.06e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2526** | 0.4057 | ±0.8113 | **+3.088** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.0977 | 0.2747 | ±0.5493 | +0.356 | 0.7219 |  |
| Site: UW (vs UAB) | +0.0944 | 0.2553 | ±0.5105 | +0.370 | 0.7116 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.889** | **4.65e-23** | *** |
| **BMI (kg/m2)** | **+0.0769** | 0.0165 | ±0.0330 | **+4.666** | **3.07e-06** | *** |
| Hypertension | +0.2782 | 0.2263 | ±0.4525 | +1.229 | 0.2189 |  |
| **High cholesterol** | **+0.6582** | 0.2121 | ±0.4243 | **+3.103** | **0.0019** | ** |
| **Kidney disease** | **+0.9118** | 0.3792 | ±0.7584 | **+2.404** | **0.0162** | * |
| **Circulatory disease** | **+1.1193** | 0.3191 | ±0.6381 | **+3.508** | **4.51e-04** | *** |
| Avg. daily time 54-250 (%) | -0.0120 | 0.0123 | ±0.0245 | -0.979 | 0.3274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1030**, F-statistic = **23.28** (p = **1.13e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5361** | 0.8339 | ±1.6679 | **+10.236** | **1.37e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8429** | 0.2144 | ±0.4287 | **-3.932** | **8.41e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2694** | 0.4076 | ±0.8152 | **+3.114** | **0.0018** | ** |
| Site: UCSD (vs UAB) | +0.0899 | 0.2749 | ±0.5498 | +0.327 | 0.7438 |  |
| Site: UW (vs UAB) | +0.0776 | 0.2540 | ±0.5081 | +0.306 | 0.7599 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0191 | **-9.927** | **3.17e-23** | *** |
| **BMI (kg/m2)** | **+0.0766** | 0.0164 | ±0.0329 | **+4.661** | **3.15e-06** | *** |
| Hypertension | +0.2784 | 0.2267 | ±0.4534 | +1.228 | 0.2194 |  |
| **High cholesterol** | **+0.6513** | 0.2127 | ±0.4254 | **+3.062** | **0.0022** | ** |
| **Kidney disease** | **+0.9098** | 0.3822 | ±0.7645 | **+2.380** | **0.0173** | * |
| **Circulatory disease** | **+1.1264** | 0.3184 | ±0.6368 | **+3.538** | **4.03e-04** | *** |
| Time 181-250, pooled (%) | +0.0069 | 0.0088 | ±0.0176 | +0.781 | 0.4350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1030**, F-statistic = **23.29** (p = **1.11e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5361** | 0.8340 | ±1.6681 | **+10.235** | **1.39e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8432** | 0.2143 | ±0.4287 | **-3.934** | **8.37e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2682** | 0.4077 | ±0.8154 | **+3.110** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0910 | 0.2749 | ±0.5498 | +0.331 | 0.7406 |  |
| Site: UW (vs UAB) | +0.0783 | 0.2540 | ±0.5081 | +0.308 | 0.7578 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0191 | **-9.931** | **3.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0766** | 0.0164 | ±0.0329 | **+4.657** | **3.20e-06** | *** |
| Hypertension | +0.2782 | 0.2267 | ±0.4535 | +1.227 | 0.2199 |  |
| **High cholesterol** | **+0.6509** | 0.2127 | ±0.4254 | **+3.060** | **0.0022** | ** |
| **Kidney disease** | **+0.9088** | 0.3822 | ±0.7644 | **+2.378** | **0.0174** | * |
| **Circulatory disease** | **+1.1265** | 0.3184 | ±0.6369 | **+3.538** | **4.04e-04** | *** |
| Avg. daily time 181-250 (%) | +0.0070 | 0.0087 | ±0.0174 | +0.799 | 0.4243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.39** (p = **6.97e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.6**, BIC = **12759.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5221** | 0.8339 | ±1.6678 | **+10.220** | **1.62e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8344** | 0.2145 | ±0.4289 | **-3.891** | **1.00e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2465** | 0.4069 | ±0.8139 | **+3.063** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1004 | 0.2749 | ±0.5498 | +0.365 | 0.7149 |  |
| Site: UW (vs UAB) | +0.0894 | 0.2546 | ±0.5091 | +0.351 | 0.7255 |  |
| **Age (years)** | **-0.0947** | 0.0095 | ±0.0190 | **-9.944** | **2.69e-23** | *** |
| **BMI (kg/m2)** | **+0.0762** | 0.0165 | ±0.0329 | **+4.627** | **3.71e-06** | *** |
| Hypertension | +0.2708 | 0.2265 | ±0.4531 | +1.195 | 0.2320 |  |
| **High cholesterol** | **+0.6488** | 0.2123 | ±0.4246 | **+3.056** | **0.0022** | ** |
| **Kidney disease** | **+0.8929** | 0.3820 | ±0.7640 | **+2.337** | **0.0194** | * |
| **Circulatory disease** | **+1.1196** | 0.3184 | ±0.6368 | **+3.517** | **4.37e-04** | *** |
| Time > 180 (%) | +0.0068 | 0.0059 | ±0.0118 | +1.152 | 0.2494 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.62e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.8**, BIC = **12759.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5232** | 0.8340 | ±1.6680 | **+10.220** | **1.62e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8357** | 0.2145 | ±0.4289 | **-3.897** | **9.75e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2486** | 0.4070 | ±0.8141 | **+3.068** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1000 | 0.2749 | ±0.5499 | +0.364 | 0.7161 |  |
| Site: UW (vs UAB) | +0.0886 | 0.2545 | ±0.5091 | +0.348 | 0.7277 |  |
| **Age (years)** | **-0.0946** | 0.0095 | ±0.0190 | **-9.940** | **2.80e-23** | *** |
| **BMI (kg/m2)** | **+0.0763** | 0.0165 | ±0.0330 | **+4.629** | **3.68e-06** | *** |
| Hypertension | +0.2723 | 0.2265 | ±0.4531 | +1.202 | 0.2294 |  |
| **High cholesterol** | **+0.6494** | 0.2123 | ±0.4246 | **+3.059** | **0.0022** | ** |
| **Kidney disease** | **+0.8948** | 0.3820 | ±0.7639 | **+2.343** | **0.0192** | * |
| **Circulatory disease** | **+1.1202** | 0.3185 | ±0.6369 | **+3.518** | **4.35e-04** | *** |
| Avg. daily time > 180 (%) | +0.0064 | 0.0059 | ±0.0118 | +1.087 | 0.2771 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2135**, R² = **0.1092**, Adj R² = **0.1046**, F-statistic = **23.66** (p = **1.88e-46**), Residual SE = **4.711** on **2123** df, AIC = **12688.9**, BIC = **12756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5369** | 0.8345 | ±1.6690 | **+10.230** | **1.46e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8195** | 0.2147 | ±0.4294 | **-3.817** | **1.35e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2225** | 0.4062 | ±0.8123 | **+3.010** | **0.0026** | ** |
| Site: UCSD (vs UAB) | +0.1154 | 0.2743 | ±0.5486 | +0.421 | 0.6739 |  |
| Site: UW (vs UAB) | +0.0955 | 0.2544 | ±0.5088 | +0.375 | 0.7074 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0190 | **-9.918** | **3.49e-23** | *** |
| **BMI (kg/m2)** | **+0.0742** | 0.0165 | ±0.0331 | **+4.485** | **7.30e-06** | *** |
| Hypertension | +0.2698 | 0.2262 | ±0.4523 | +1.193 | 0.2330 |  |
| **High cholesterol** | **+0.6445** | 0.2120 | ±0.4240 | **+3.041** | **0.0024** | ** |
| **Kidney disease** | **+0.8803** | 0.3818 | ±0.7637 | **+2.305** | **0.0211** | * |
| **Circulatory disease** | **+1.1148** | 0.3185 | ±0.6369 | **+3.500** | **4.65e-04** | *** |
| Nocturnal time > 180 (%) | +0.0110 | 0.0060 | ±0.0120 | +1.821 | 0.0686 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1028**, F-statistic = **23.23** (p = **1.49e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.2**, BIC = **12761.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4989** | 0.8333 | ±1.6667 | **+10.199** | **2.01e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8429** | 0.2148 | ±0.4296 | **-3.924** | **8.70e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2868** | 0.4058 | ±0.8117 | **+3.171** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0810 | 0.2743 | ±0.5487 | +0.295 | 0.7679 |  |
| Site: UW (vs UAB) | +0.0745 | 0.2537 | ±0.5073 | +0.294 | 0.7689 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0191 | **-9.883** | **4.95e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.736** | **2.17e-06** | *** |
| Hypertension | +0.2842 | 0.2263 | ±0.4527 | +1.256 | 0.2092 |  |
| **High cholesterol** | **+0.6580** | 0.2130 | ±0.4260 | **+3.089** | **0.0020** | ** |
| **Kidney disease** | **+0.9322** | 0.3781 | ±0.7563 | **+2.465** | **0.0137** | * |
| **Circulatory disease** | **+1.1323** | 0.3188 | ±0.6376 | **+3.552** | **3.83e-04** | *** |
| Any reading > 250 during wear (0/1) | +0.0729 | 0.2174 | ±0.4348 | +0.335 | 0.7375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2135**, R² = **0.1082**, Adj R² = **0.1036**, F-statistic = **23.41** (p = **6.13e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.4**, BIC = **12759.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4789** | 0.8345 | ±1.6690 | **+10.160** | **2.99e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8304** | 0.2146 | ±0.4292 | **-3.870** | **1.09e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2469** | 0.4057 | ±0.8113 | **+3.074** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.0984 | 0.2745 | ±0.5489 | +0.359 | 0.7199 |  |
| Site: UW (vs UAB) | +0.0961 | 0.2552 | ±0.5104 | +0.377 | 0.7065 |  |
| **Age (years)** | **-0.0938** | 0.0095 | ±0.0190 | **-9.882** | **5.00e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0330 | **+4.661** | **3.15e-06** | *** |
| Hypertension | +0.2758 | 0.2263 | ±0.4526 | +1.219 | 0.2229 |  |
| **High cholesterol** | **+0.6570** | 0.2121 | ±0.4242 | **+3.098** | **0.0020** | ** |
| **Kidney disease** | **+0.9096** | 0.3792 | ±0.7584 | **+2.399** | **0.0164** | * |
| **Circulatory disease** | **+1.1190** | 0.3190 | ±0.6379 | **+3.508** | **4.51e-04** | *** |
| Time > 250 (%) | +0.0133 | 0.0120 | ±0.0240 | +1.102 | 0.2704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.37e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.7**, BIC = **12759.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4857** | 0.8344 | ±1.6688 | **+10.170** | **2.70e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8323** | 0.2146 | ±0.4291 | **-3.879** | **1.05e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2517** | 0.4057 | ±0.8115 | **+3.085** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.0965 | 0.2746 | ±0.5491 | +0.352 | 0.7251 |  |
| Site: UW (vs UAB) | +0.0932 | 0.2551 | ±0.5103 | +0.365 | 0.7150 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.889** | **4.66e-23** | *** |
| **BMI (kg/m2)** | **+0.0769** | 0.0165 | ±0.0330 | **+4.665** | **3.08e-06** | *** |
| Hypertension | +0.2779 | 0.2263 | ±0.4526 | +1.228 | 0.2194 |  |
| **High cholesterol** | **+0.6577** | 0.2121 | ±0.4243 | **+3.100** | **0.0019** | ** |
| **Kidney disease** | **+0.9117** | 0.3792 | ±0.7584 | **+2.404** | **0.0162** | * |
| **Circulatory disease** | **+1.1197** | 0.3190 | ±0.6380 | **+3.510** | **4.48e-04** | *** |
| Avg. daily time > 250 (%) | +0.0120 | 0.0123 | ±0.0245 | +0.982 | 0.3260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 2,135; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0669**, LLR χ² = **138.37** (p = **9.08e-25**), AUC = **0.6799**, AIC = **1952.1**, BIC = **2014.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4584 | 0.4537 | ±0.9075 | -1.010 | 0.3124 | 0.6323 |  |
| Education: graduate level (vs college) | -0.2185 | 0.1297 | ±0.2594 | -1.684 | 0.0921 | 0.8037 | . |
| Education: high school or below (vs college) | +0.2867 | 0.1712 | ±0.3425 | +1.674 | 0.0940 | 1.3321 | . |
| Site: UCSD (vs UAB) | -0.0662 | 0.1505 | ±0.3010 | -0.440 | 0.6602 | 0.9360 |  |
| Site: UW (vs UAB) | +0.0149 | 0.1389 | ±0.2779 | +0.107 | 0.9148 | 1.0150 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.881** | **5.93e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.285** | **1.83e-05** | 1.0331 | *** |
| Hypertension | +0.1669 | 0.1283 | ±0.2566 | +1.301 | 0.1933 | 1.1817 |  |
| **High cholesterol** | **+0.3597** | 0.1221 | ±0.2441 | **+2.947** | **0.0032** | 1.4330 | ** |
| **Kidney disease** | **+0.4941** | 0.1716 | ±0.3433 | **+2.878** | **0.0040** | 1.6390 | ** |
| **Circulatory disease** | **+0.5014** | 0.1487 | ±0.2975 | **+3.371** | **7.49e-04** | 1.6511 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0692**, LLR χ² = **143.07** (p = **3.86e-25**), AUC = **0.6826**, AIC = **1949.4**, BIC = **2017.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.0296** | 0.5244 | ±1.0489 | **-1.963** | **0.0496** | 0.3572 | * |
| Education: graduate level (vs college) | -0.1991 | 0.1302 | ±0.2604 | -1.529 | 0.1261 | 0.8195 |  |
| Education: high school or below (vs college) | +0.2429 | 0.1730 | ±0.3460 | +1.404 | 0.1604 | 1.2749 |  |
| Site: UCSD (vs UAB) | -0.0505 | 0.1510 | ±0.3020 | -0.335 | 0.7380 | 0.9507 |  |
| Site: UW (vs UAB) | +0.0353 | 0.1397 | ±0.2794 | +0.253 | 0.8004 | 1.0360 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.951** | **3.62e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0307** | 0.0077 | ±0.0154 | **+4.000** | **6.33e-05** | 1.0312 | *** |
| Hypertension | +0.1405 | 0.1292 | ±0.2584 | +1.088 | 0.2768 | 1.1508 |  |
| **High cholesterol** | **+0.3368** | 0.1226 | ±0.2452 | **+2.747** | **0.0060** | 1.4004 | ** |
| **Kidney disease** | **+0.4788** | 0.1721 | ±0.3442 | **+2.782** | **0.0054** | 1.6141 | ** |
| **Circulatory disease** | **+0.4950** | 0.1489 | ±0.2979 | **+3.324** | **8.88e-04** | 1.6405 | *** |
| **HbA1c (%)** | **+0.1095** | 0.0497 | ±0.0994 | **+2.203** | **0.0276** | 1.1157 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0684**, LLR χ² = **141.38** (p = **8.53e-25**), AUC = **0.6821**, AIC = **1951.1**, BIC = **2019.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7684 | 0.4879 | ±0.9757 | -1.575 | 0.1152 | 0.4637 |  |
| Education: graduate level (vs college) | -0.2080 | 0.1300 | ±0.2599 | -1.600 | 0.1096 | 0.8122 |  |
| Education: high school or below (vs college) | +0.2553 | 0.1724 | ±0.3448 | +1.481 | 0.1387 | 1.2908 |  |
| Site: UCSD (vs UAB) | -0.0522 | 0.1509 | ±0.3018 | -0.346 | 0.7291 | 0.9491 |  |
| Site: UW (vs UAB) | +0.0252 | 0.1393 | ±0.2786 | +0.181 | 0.8564 | 1.0255 |  |
| **Age (years)** | **-0.0403** | 0.0058 | ±0.0116 | **-6.937** | **4.02e-12** | 0.9605 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0076 | ±0.0153 | **+4.140** | **3.48e-05** | 1.0322 | *** |
| Hypertension | +0.1471 | 0.1290 | ±0.2580 | +1.140 | 0.2542 | 1.1585 |  |
| **High cholesterol** | **+0.3455** | 0.1224 | ±0.2448 | **+2.823** | **0.0048** | 1.4126 | ** |
| **Kidney disease** | **+0.4655** | 0.1726 | ±0.3453 | **+2.696** | **0.0070** | 1.5927 | ** |
| **Circulatory disease** | **+0.4954** | 0.1488 | ±0.2977 | **+3.328** | **8.74e-04** | 1.6411 | *** |
| Mean glucose (mg/dL) | +0.0028 | 0.0016 | ±0.0031 | +1.754 | 0.0794 | 1.0028 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0684**, LLR χ² = **141.38** (p = **8.53e-25**), AUC = **0.6821**, AIC = **1951.1**, BIC = **2019.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1507 | 0.6023 | ±1.2046 | -1.911 | 0.0561 | 0.3164 | . |
| Education: graduate level (vs college) | -0.2080 | 0.1300 | ±0.2599 | -1.600 | 0.1096 | 0.8122 |  |
| Education: high school or below (vs college) | +0.2553 | 0.1724 | ±0.3448 | +1.481 | 0.1387 | 1.2908 |  |
| Site: UCSD (vs UAB) | -0.0522 | 0.1509 | ±0.3018 | -0.346 | 0.7291 | 0.9491 |  |
| Site: UW (vs UAB) | +0.0252 | 0.1393 | ±0.2786 | +0.181 | 0.8564 | 1.0255 |  |
| **Age (years)** | **-0.0403** | 0.0058 | ±0.0116 | **-6.937** | **4.02e-12** | 0.9605 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0076 | ±0.0153 | **+4.140** | **3.48e-05** | 1.0322 | *** |
| Hypertension | +0.1471 | 0.1290 | ±0.2580 | +1.140 | 0.2542 | 1.1585 |  |
| **High cholesterol** | **+0.3455** | 0.1224 | ±0.2448 | **+2.823** | **0.0048** | 1.4126 | ** |
| **Kidney disease** | **+0.4655** | 0.1726 | ±0.3453 | **+2.696** | **0.0070** | 1.5927 | ** |
| **Circulatory disease** | **+0.4954** | 0.1488 | ±0.2977 | **+3.328** | **8.74e-04** | 1.6411 | *** |
| GMI (%) | +0.1155 | 0.0658 | ±0.1317 | +1.754 | 0.0794 | 1.1224 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0704**, LLR χ² = **145.57** (p = **1.20e-25**), AUC = **0.6855**, AIC = **1946.9**, BIC = **2014.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9315 | 0.4876 | ±0.9752 | -1.910 | 0.0561 | 0.3940 | . |
| Education: graduate level (vs college) | -0.1999 | 0.1301 | ±0.2603 | -1.536 | 0.1246 | 0.8189 |  |
| Education: high school or below (vs college) | +0.2406 | 0.1727 | ±0.3454 | +1.394 | 0.1635 | 1.2720 |  |
| Site: UCSD (vs UAB) | -0.0482 | 0.1510 | ±0.3020 | -0.319 | 0.7494 | 0.9529 |  |
| Site: UW (vs UAB) | +0.0248 | 0.1394 | ±0.2788 | +0.178 | 0.8588 | 1.0251 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.884** | **5.81e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0304** | 0.0077 | ±0.0154 | **+3.954** | **7.68e-05** | 1.0309 | *** |
| Hypertension | +0.1428 | 0.1289 | ±0.2579 | +1.107 | 0.2681 | 1.1535 |  |
| **High cholesterol** | **+0.3385** | 0.1225 | ±0.2450 | **+2.763** | **0.0057** | 1.4028 | ** |
| **Kidney disease** | **+0.4662** | 0.1724 | ±0.3448 | **+2.705** | **0.0068** | 1.5940 | ** |
| **Circulatory disease** | **+0.4964** | 0.1489 | ±0.2979 | **+3.333** | **8.59e-04** | 1.6427 | *** |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0042** | 0.0015 | ±0.0031 | **+2.723** | **0.0065** | 1.0042 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0691**, LLR χ² = **142.95** (p = **4.09e-25**), AUC = **0.6830**, AIC = **1949.5**, BIC = **2017.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6382 | 0.4624 | ±0.9248 | -1.380 | 0.1675 | 0.5282 |  |
| Education: graduate level (vs college) | -0.2002 | 0.1302 | ±0.2604 | -1.538 | 0.1240 | 0.8185 |  |
| Education: high school or below (vs college) | +0.2509 | 0.1724 | ±0.3448 | +1.456 | 0.1455 | 1.2852 |  |
| Site: UCSD (vs UAB) | -0.0470 | 0.1509 | ±0.3019 | -0.311 | 0.7554 | 0.9541 |  |
| Site: UW (vs UAB) | +0.0361 | 0.1396 | ±0.2792 | +0.258 | 0.7961 | 1.0367 |  |
| **Age (years)** | **-0.0409** | 0.0058 | ±0.0117 | **-7.010** | **2.38e-12** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0317** | 0.0076 | ±0.0153 | **+4.147** | **3.37e-05** | 1.0322 | *** |
| Hypertension | +0.1391 | 0.1293 | ±0.2586 | +1.076 | 0.2820 | 1.1492 |  |
| **High cholesterol** | **+0.3468** | 0.1224 | ±0.2447 | **+2.834** | **0.0046** | 1.4145 | ** |
| **Kidney disease** | **+0.4262** | 0.1751 | ±0.3501 | **+2.435** | **0.0149** | 1.5314 | * |
| **Circulatory disease** | **+0.4932** | 0.1490 | ±0.2979 | **+3.311** | **9.29e-04** | 1.6376 | *** |
| **Glucose SD, pooled (mg/dL)** | **+0.0101** | 0.0047 | ±0.0094 | **+2.160** | **0.0307** | 1.0102 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0681**, LLR χ² = **140.96** (p = **1.04e-24**), AUC = **0.6818**, AIC = **1951.5**, BIC = **2019.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5971 | 0.4625 | ±0.9250 | -1.291 | 0.1967 | 0.5504 |  |
| Education: graduate level (vs college) | -0.2056 | 0.1301 | ±0.2601 | -1.581 | 0.1139 | 0.8141 |  |
| Education: high school or below (vs college) | +0.2585 | 0.1723 | ±0.3446 | +1.500 | 0.1335 | 1.2950 |  |
| Site: UCSD (vs UAB) | -0.0529 | 0.1508 | ±0.3016 | -0.351 | 0.7258 | 0.9485 |  |
| Site: UW (vs UAB) | +0.0288 | 0.1394 | ±0.2788 | +0.207 | 0.8363 | 1.0292 |  |
| **Age (years)** | **-0.0407** | 0.0058 | ±0.0117 | **-6.985** | **2.85e-12** | 0.9601 | *** |
| **BMI (kg/m2)** | **+0.0321** | 0.0076 | ±0.0153 | **+4.204** | **2.62e-05** | 1.0326 | *** |
| Hypertension | +0.1466 | 0.1291 | ±0.2582 | +1.136 | 0.2562 | 1.1579 |  |
| **High cholesterol** | **+0.3502** | 0.1223 | ±0.2446 | **+2.863** | **0.0042** | 1.4193 | ** |
| **Kidney disease** | **+0.4412** | 0.1751 | ±0.3501 | **+2.520** | **0.0117** | 1.5546 | * |
| **Circulatory disease** | **+0.4965** | 0.1488 | ±0.2977 | **+3.336** | **8.50e-04** | 1.6430 | *** |
| Avg. daily SD (mg/dL) | +0.0087 | 0.0053 | ±0.0107 | +1.622 | 0.1048 | 1.0087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0674**, LLR χ² = **139.37** (p = **2.19e-24**), AUC = **0.6809**, AIC = **1953.1**, BIC = **2021.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6328 | 0.4863 | ±0.9725 | -1.301 | 0.1932 | 0.5311 |  |
| Education: graduate level (vs college) | -0.2114 | 0.1300 | ±0.2599 | -1.627 | 0.1038 | 0.8095 |  |
| Education: high school or below (vs college) | +0.2767 | 0.1716 | ±0.3432 | +1.612 | 0.1069 | 1.3187 |  |
| Site: UCSD (vs UAB) | -0.0573 | 0.1508 | ±0.3015 | -0.380 | 0.7037 | 0.9443 |  |
| Site: UW (vs UAB) | +0.0249 | 0.1394 | ±0.2788 | +0.179 | 0.8581 | 1.0252 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0117 | **-6.938** | **3.97e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0076 | ±0.0152 | **+4.259** | **2.05e-05** | 1.0330 | *** |
| Hypertension | +0.1557 | 0.1289 | ±0.2578 | +1.208 | 0.2270 | 1.1685 |  |
| **High cholesterol** | **+0.3581** | 0.1221 | ±0.2443 | **+2.932** | **0.0034** | 1.4307 | ** |
| **Kidney disease** | **+0.4619** | 0.1748 | ±0.3496 | **+2.642** | **0.0082** | 1.5870 | ** |
| **Circulatory disease** | **+0.4979** | 0.1488 | ±0.2977 | **+3.345** | **8.24e-04** | 1.6452 | *** |
| CV (%) | +0.0109 | 0.0109 | ±0.0218 | +1.001 | 0.3167 | 1.0110 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0672**, LLR χ² = **139.07** (p = **2.52e-24**), AUC = **0.6806**, AIC = **1953.4**, BIC = **2021.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2245 | 0.5338 | ±1.0676 | -0.421 | 0.6741 | 0.7989 |  |
| Education: graduate level (vs college) | -0.2126 | 0.1299 | ±0.2599 | -1.636 | 0.1018 | 0.8085 |  |
| Education: high school or below (vs college) | +0.2775 | 0.1716 | ±0.3433 | +1.617 | 0.1059 | 1.3198 |  |
| Site: UCSD (vs UAB) | -0.0593 | 0.1507 | ±0.3015 | -0.394 | 0.6939 | 0.9424 |  |
| Site: UW (vs UAB) | +0.0217 | 0.1392 | ±0.2785 | +0.156 | 0.8762 | 1.0219 |  |
| **Age (years)** | **-0.0404** | 0.0058 | ±0.0117 | **-6.925** | **4.37e-12** | 0.9604 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.265** | **2.00e-05** | 1.0330 | *** |
| Hypertension | +0.1575 | 0.1289 | ±0.2578 | +1.222 | 0.2216 | 1.1706 |  |
| **High cholesterol** | **+0.3572** | 0.1221 | ±0.2443 | **+2.925** | **0.0034** | 1.4294 | ** |
| **Kidney disease** | **+0.4735** | 0.1735 | ±0.3469 | **+2.729** | **0.0063** | 1.6056 | ** |
| **Circulatory disease** | **+0.4980** | 0.1489 | ±0.2977 | **+3.345** | **8.22e-04** | 1.6454 | *** |
| Mean / SD ratio | -0.0364 | 0.0439 | ±0.0877 | -0.831 | 0.4061 | 0.9642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0669**, LLR χ² = **138.39** (p = **3.46e-24**), AUC = **0.6800**, AIC = **1954.1**, BIC = **2022.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4231 | 0.5309 | ±1.0617 | -0.797 | 0.4254 | 0.6550 |  |
| Education: graduate level (vs college) | -0.2176 | 0.1299 | ±0.2598 | -1.676 | 0.0938 | 0.8044 | . |
| Education: high school or below (vs college) | +0.2853 | 0.1716 | ±0.3432 | +1.662 | 0.0965 | 1.3301 | . |
| Site: UCSD (vs UAB) | -0.0656 | 0.1506 | ±0.3011 | -0.435 | 0.6632 | 0.9365 |  |
| Site: UW (vs UAB) | +0.0157 | 0.1391 | ±0.2782 | +0.113 | 0.9104 | 1.0158 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0117 | **-6.854** | **7.16e-12** | 0.9607 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.282** | **1.85e-05** | 1.0331 | *** |
| Hypertension | +0.1657 | 0.1287 | ±0.2573 | +1.288 | 0.1977 | 1.1803 |  |
| **High cholesterol** | **+0.3595** | 0.1221 | ±0.2441 | **+2.945** | **0.0032** | 1.4326 | ** |
| **Kidney disease** | **+0.4910** | 0.1733 | ±0.3465 | **+2.834** | **0.0046** | 1.6340 | ** |
| **Circulatory disease** | **+0.5012** | 0.1488 | ±0.2975 | **+3.369** | **7.54e-04** | 1.6507 | *** |
| Avg. daily mean/SD | -0.0047 | 0.0366 | ±0.0731 | -0.128 | 0.8983 | 0.9953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0692**, LLR χ² = **143.22** (p = **3.59e-25**), AUC = **0.6830**, AIC = **1949.2**, BIC = **2017.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0216 | 0.5219 | ±1.0438 | -1.958 | 0.0503 | 0.3600 | . |
| Education: graduate level (vs college) | -0.2010 | 0.1302 | ±0.2603 | -1.544 | 0.1225 | 0.8179 |  |
| Education: high school or below (vs college) | +0.2591 | 0.1722 | ±0.3443 | +1.505 | 0.1323 | 1.2958 |  |
| Site: UCSD (vs UAB) | -0.0440 | 0.1511 | ±0.3022 | -0.292 | 0.7706 | 0.9569 |  |
| Site: UW (vs UAB) | +0.0508 | 0.1402 | ±0.2804 | +0.362 | 0.7173 | 1.0521 |  |
| **Age (years)** | **-0.0398** | 0.0058 | ±0.0116 | **-6.832** | **8.36e-12** | 0.9610 | *** |
| **BMI (kg/m2)** | **+0.0320** | 0.0076 | ±0.0153 | **+4.182** | **2.89e-05** | 1.0325 | *** |
| Hypertension | +0.1597 | 0.1287 | ±0.2574 | +1.241 | 0.2146 | 1.1732 |  |
| **High cholesterol** | **+0.3632** | 0.1224 | ±0.2447 | **+2.968** | **0.0030** | 1.4379 | ** |
| **Kidney disease** | **+0.4620** | 0.1725 | ±0.3450 | **+2.678** | **0.0074** | 1.5872 | ** |
| **Circulatory disease** | **+0.4976** | 0.1490 | ±0.2981 | **+3.339** | **8.41e-04** | 1.6448 | *** |
| **MAG (mg/dL/h)** | **+0.0137** | 0.0062 | ±0.0124 | **+2.216** | **0.0267** | 1.0138 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0679**, LLR χ² = **140.44** (p = **1.32e-24**), AUC = **0.6814**, AIC = **1952.0**, BIC = **2020.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6522 | 0.4738 | ±0.9476 | -1.376 | 0.1687 | 0.5209 |  |
| Education: graduate level (vs college) | -0.2070 | 0.1300 | ±0.2601 | -1.592 | 0.1113 | 0.8130 |  |
| Education: high school or below (vs college) | +0.2617 | 0.1723 | ±0.3446 | +1.519 | 0.1288 | 1.2991 |  |
| Site: UCSD (vs UAB) | -0.0524 | 0.1509 | ±0.3017 | -0.347 | 0.7282 | 0.9489 |  |
| Site: UW (vs UAB) | +0.0277 | 0.1394 | ±0.2787 | +0.199 | 0.8425 | 1.0281 |  |
| **Age (years)** | **-0.0406** | 0.0058 | ±0.0117 | **-6.962** | **3.36e-12** | 0.9602 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.259** | **2.05e-05** | 1.0330 | *** |
| Hypertension | +0.1521 | 0.1289 | ±0.2578 | +1.180 | 0.2379 | 1.1643 |  |
| **High cholesterol** | **+0.3522** | 0.1223 | ±0.2445 | **+2.880** | **0.0040** | 1.4221 | ** |
| **Kidney disease** | **+0.4487** | 0.1748 | ±0.3496 | **+2.567** | **0.0103** | 1.5663 | * |
| **Circulatory disease** | **+0.4951** | 0.1489 | ±0.2978 | **+3.325** | **8.85e-04** | 1.6406 | *** |
| Avg. daily range (mg/dL) | +0.0021 | 0.0015 | ±0.0029 | +1.448 | 0.1477 | 1.0021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0741**, LLR χ² = **153.32** (p = **3.12e-27**), AUC = **0.6891**, AIC = **1939.1**, BIC = **2007.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6570 | 0.4578 | ±0.9155 | -1.435 | 0.1512 | 0.5184 |  |
| Education: graduate level (vs college) | -0.1819 | 0.1307 | ±0.2614 | -1.392 | 0.1640 | 0.8337 |  |
| Education: high school or below (vs college) | +0.2495 | 0.1726 | ±0.3451 | +1.446 | 0.1482 | 1.2834 |  |
| Site: UCSD (vs UAB) | -0.0368 | 0.1515 | ±0.3029 | -0.243 | 0.8082 | 0.9639 |  |
| Site: UW (vs UAB) | +0.0527 | 0.1401 | ±0.2803 | +0.376 | 0.7069 | 1.0541 |  |
| **Age (years)** | **-0.0402** | 0.0058 | ±0.0116 | **-6.913** | **4.74e-12** | 0.9606 | *** |
| **BMI (kg/m2)** | **+0.0303** | 0.0077 | ±0.0154 | **+3.938** | **8.21e-05** | 1.0307 | *** |
| Hypertension | +0.1285 | 0.1296 | ±0.2592 | +0.992 | 0.3214 | 1.1371 |  |
| **High cholesterol** | **+0.3375** | 0.1227 | ±0.2454 | **+2.751** | **0.0059** | 1.4015 | ** |
| **Kidney disease** | **+0.4246** | 0.1740 | ±0.3479 | **+2.441** | **0.0146** | 1.5290 | * |
| **Circulatory disease** | **+0.4735** | 0.1498 | ±0.2996 | **+3.161** | **0.0016** | 1.6056 | ** |
| **SD of daily means (mg/dL)** | **+0.0322** | 0.0082 | ±0.0164 | **+3.926** | **8.65e-05** | 1.0327 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0689**, LLR χ² = **142.54** (p = **4.96e-25**), AUC = **0.6827**, AIC = **1949.9**, BIC = **2017.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0868 | 0.5256 | ±1.0511 | +0.165 | 0.8688 | 1.0907 |  |
| Education: graduate level (vs college) | -0.2021 | 0.1301 | ±0.2603 | -1.553 | 0.1205 | 0.8170 |  |
| Education: high school or below (vs college) | +0.2520 | 0.1724 | ±0.3448 | +1.462 | 0.1438 | 1.2866 |  |
| Site: UCSD (vs UAB) | -0.0422 | 0.1512 | ±0.3023 | -0.279 | 0.7800 | 0.9587 |  |
| Site: UW (vs UAB) | +0.0349 | 0.1396 | ±0.2792 | +0.250 | 0.8023 | 1.0356 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.957** | **3.49e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0077 | ±0.0153 | **+4.112** | **3.92e-05** | 1.0320 | *** |
| Hypertension | +0.1493 | 0.1289 | ±0.2577 | +1.159 | 0.2466 | 1.1610 |  |
| **High cholesterol** | **+0.3470** | 0.1223 | ±0.2447 | **+2.836** | **0.0046** | 1.4148 | ** |
| **Kidney disease** | **+0.4549** | 0.1730 | ±0.3461 | **+2.629** | **0.0086** | 1.5760 | ** |
| **Circulatory disease** | **+0.4939** | 0.1489 | ±0.2978 | **+3.317** | **9.10e-04** | 1.6387 | *** |
| **Time in range 70-180, pooled (%)** | **-0.0055** | 0.0026 | ±0.0053 | **-2.071** | **0.0384** | 0.9945 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0688**, LLR χ² = **142.21** (p = **5.77e-25**), AUC = **0.6826**, AIC = **1950.3**, BIC = **2018.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0681 | 0.5263 | ±1.0526 | +0.129 | 0.8971 | 1.0704 |  |
| Education: graduate level (vs college) | -0.2031 | 0.1301 | ±0.2602 | -1.561 | 0.1186 | 0.8162 |  |
| Education: high school or below (vs college) | +0.2528 | 0.1724 | ±0.3448 | +1.466 | 0.1426 | 1.2876 |  |
| Site: UCSD (vs UAB) | -0.0429 | 0.1512 | ±0.3023 | -0.284 | 0.7767 | 0.9580 |  |
| Site: UW (vs UAB) | +0.0341 | 0.1396 | ±0.2791 | +0.244 | 0.8071 | 1.0347 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.958** | **3.46e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0077 | ±0.0153 | **+4.115** | **3.88e-05** | 1.0320 | *** |
| Hypertension | +0.1504 | 0.1288 | ±0.2577 | +1.167 | 0.2431 | 1.1623 |  |
| **High cholesterol** | **+0.3473** | 0.1223 | ±0.2447 | **+2.839** | **0.0045** | 1.4152 | ** |
| **Kidney disease** | **+0.4556** | 0.1731 | ±0.3461 | **+2.633** | **0.0085** | 1.5772 | ** |
| **Circulatory disease** | **+0.4943** | 0.1489 | ±0.2977 | **+3.320** | **8.99e-04** | 1.6394 | *** |
| **Avg. daily time in range 70-180 (%)** | **-0.0053** | 0.0026 | ±0.0053 | **-1.989** | **0.0467** | 0.9948 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0674**, LLR χ² = **139.42** (p = **2.14e-24**), AUC = **0.6797**, AIC = **1953.0**, BIC = **2021.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5226 | 0.4581 | ±0.9162 | -1.141 | 0.2540 | 0.5930 |  |
| Education: graduate level (vs college) | -0.2157 | 0.1298 | ±0.2596 | -1.662 | 0.0965 | 0.8059 | . |
| Education: high school or below (vs college) | +0.2992 | 0.1718 | ±0.3435 | +1.742 | 0.0815 | 1.3488 | . |
| Site: UCSD (vs UAB) | -0.0504 | 0.1513 | ±0.3027 | -0.333 | 0.7393 | 0.9509 |  |
| Site: UW (vs UAB) | +0.0244 | 0.1393 | ±0.2786 | +0.175 | 0.8612 | 1.0247 |  |
| **Age (years)** | **-0.0396** | 0.0058 | ±0.0116 | **-6.800** | **1.05e-11** | 0.9612 | *** |
| **BMI (kg/m2)** | **+0.0323** | 0.0076 | ±0.0152 | **+4.231** | **2.32e-05** | 1.0328 | *** |
| Hypertension | +0.1651 | 0.1284 | ±0.2568 | +1.286 | 0.1985 | 1.1795 |  |
| **High cholesterol** | **+0.3680** | 0.1224 | ±0.2447 | **+3.007** | **0.0026** | 1.4448 | ** |
| **Kidney disease** | **+0.4967** | 0.1718 | ±0.3435 | **+2.892** | **0.0038** | 1.6434 | ** |
| **Circulatory disease** | **+0.4912** | 0.1491 | ±0.2983 | **+3.293** | **9.90e-04** | 1.6342 | *** |
| Any reading < 54 during wear (0/1) | +0.1280 | 0.1245 | ±0.2490 | +1.028 | 0.3039 | 1.1366 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.55** (p = **3.21e-24**), AUC = **0.6800**, AIC = **1953.9**, BIC = **2021.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4440 | 0.4550 | ±0.9100 | -0.976 | 0.3291 | 0.6415 |  |
| Education: graduate level (vs college) | -0.2188 | 0.1297 | ±0.2594 | -1.687 | 0.0916 | 0.8035 | . |
| Education: high school or below (vs college) | +0.2827 | 0.1715 | ±0.3430 | +1.649 | 0.0992 | 1.3267 | . |
| Site: UCSD (vs UAB) | -0.0738 | 0.1515 | ±0.3031 | -0.487 | 0.6263 | 0.9289 |  |
| Site: UW (vs UAB) | +0.0089 | 0.1396 | ±0.2792 | +0.064 | 0.9492 | 1.0089 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.890** | **5.58e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0327** | 0.0076 | ±0.0152 | **+4.294** | **1.75e-05** | 1.0332 | *** |
| Hypertension | +0.1660 | 0.1283 | ±0.2567 | +1.294 | 0.1958 | 1.1806 |  |
| **High cholesterol** | **+0.3567** | 0.1223 | ±0.2445 | **+2.917** | **0.0035** | 1.4286 | ** |
| **Kidney disease** | **+0.4935** | 0.1717 | ±0.3434 | **+2.874** | **0.0040** | 1.6380 | ** |
| **Circulatory disease** | **+0.5035** | 0.1488 | ±0.2977 | **+3.383** | **7.16e-04** | 1.6546 | *** |
| Time < 54 (%) | -0.0547 | 0.1338 | ±0.2677 | -0.409 | 0.6827 | 0.9468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0669**, LLR χ² = **138.42** (p = **3.41e-24**), AUC = **0.6800**, AIC = **1954.0**, BIC = **2022.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4541 | 0.4541 | ±0.9083 | -1.000 | 0.3174 | 0.6350 |  |
| Education: graduate level (vs college) | -0.2191 | 0.1297 | ±0.2595 | -1.689 | 0.0912 | 0.8032 | . |
| Education: high school or below (vs college) | +0.2849 | 0.1714 | ±0.3429 | +1.662 | 0.0965 | 1.3296 | . |
| Site: UCSD (vs UAB) | -0.0694 | 0.1512 | ±0.3024 | -0.459 | 0.6463 | 0.9330 |  |
| Site: UW (vs UAB) | +0.0118 | 0.1396 | ±0.2792 | +0.085 | 0.9325 | 1.0119 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.880** | **5.97e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.288** | **1.80e-05** | 1.0332 | *** |
| Hypertension | +0.1664 | 0.1283 | ±0.2567 | +1.297 | 0.1948 | 1.1810 |  |
| **High cholesterol** | **+0.3583** | 0.1222 | ±0.2444 | **+2.932** | **0.0034** | 1.4309 | ** |
| **Kidney disease** | **+0.4940** | 0.1717 | ±0.3433 | **+2.878** | **0.0040** | 1.6389 | ** |
| **Circulatory disease** | **+0.5024** | 0.1488 | ±0.2976 | **+3.376** | **7.35e-04** | 1.6527 | *** |
| Avg. daily time < 54 (%) | -0.0312 | 0.1447 | ±0.2894 | -0.216 | 0.8290 | 0.9692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.68** (p = **3.03e-24**), AUC = **0.6802**, AIC = **1953.8**, BIC = **2021.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4761 | 0.4549 | ±0.9098 | -1.047 | 0.2953 | 0.6212 |  |
| Education: graduate level (vs college) | -0.2156 | 0.1299 | ±0.2597 | -1.661 | 0.0968 | 0.8060 | . |
| Education: high school or below (vs college) | +0.2903 | 0.1714 | ±0.3428 | +1.694 | 0.0903 | 1.3369 | . |
| Site: UCSD (vs UAB) | -0.0589 | 0.1511 | ±0.3022 | -0.390 | 0.6966 | 0.9428 |  |
| Site: UW (vs UAB) | +0.0210 | 0.1394 | ±0.2789 | +0.151 | 0.8803 | 1.0212 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.881** | **5.95e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.273** | **1.93e-05** | 1.0331 | *** |
| Hypertension | +0.1689 | 0.1284 | ±0.2568 | +1.316 | 0.1883 | 1.1840 |  |
| **High cholesterol** | **+0.3625** | 0.1222 | ±0.2444 | **+2.967** | **0.0030** | 1.4369 | ** |
| **Kidney disease** | **+0.4940** | 0.1716 | ±0.3433 | **+2.878** | **0.0040** | 1.6389 | ** |
| **Circulatory disease** | **+0.5006** | 0.1488 | ±0.2975 | **+3.365** | **7.65e-04** | 1.6497 | *** |
| Time 54-69, pooled (%) | +0.0211 | 0.0377 | ±0.0754 | +0.559 | 0.5763 | 1.0213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0671**, LLR χ² = **138.70** (p = **2.99e-24**), AUC = **0.6802**, AIC = **1953.8**, BIC = **2021.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4729 | 0.4545 | ±0.9090 | -1.041 | 0.2981 | 0.6232 |  |
| Education: graduate level (vs college) | -0.2151 | 0.1299 | ±0.2598 | -1.656 | 0.0977 | 0.8065 | . |
| Education: high school or below (vs college) | +0.2903 | 0.1714 | ±0.3428 | +1.694 | 0.0903 | 1.3368 | . |
| Site: UCSD (vs UAB) | -0.0598 | 0.1509 | ±0.3019 | -0.396 | 0.6919 | 0.9419 |  |
| Site: UW (vs UAB) | +0.0211 | 0.1394 | ±0.2789 | +0.152 | 0.8795 | 1.0214 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.887** | **5.70e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.273** | **1.93e-05** | 1.0331 | *** |
| Hypertension | +0.1689 | 0.1284 | ±0.2568 | +1.315 | 0.1884 | 1.1840 |  |
| **High cholesterol** | **+0.3624** | 0.1222 | ±0.2443 | **+2.966** | **0.0030** | 1.4367 | ** |
| **Kidney disease** | **+0.4943** | 0.1716 | ±0.3433 | **+2.880** | **0.0040** | 1.6393 | ** |
| **Circulatory disease** | **+0.5010** | 0.1487 | ±0.2975 | **+3.368** | **7.57e-04** | 1.6503 | *** |
| Avg. daily time 54-69 (%) | +0.0216 | 0.0372 | ±0.0743 | +0.581 | 0.5610 | 1.0218 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.49** (p = **3.30e-24**), AUC = **0.6800**, AIC = **1954.0**, BIC = **2022.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4704 | 0.4551 | ±0.9102 | -1.034 | 0.3013 | 0.6248 |  |
| Education: graduate level (vs college) | -0.2169 | 0.1298 | ±0.2596 | -1.671 | 0.0947 | 0.8050 | . |
| Education: high school or below (vs college) | +0.2894 | 0.1714 | ±0.3429 | +1.688 | 0.0914 | 1.3356 | . |
| Site: UCSD (vs UAB) | -0.0609 | 0.1513 | ±0.3026 | -0.402 | 0.6875 | 0.9410 |  |
| Site: UW (vs UAB) | +0.0193 | 0.1396 | ±0.2791 | +0.138 | 0.8901 | 1.0195 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.879** | **6.03e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.277** | **1.90e-05** | 1.0331 | *** |
| Hypertension | +0.1681 | 0.1284 | ±0.2568 | +1.310 | 0.1903 | 1.1831 |  |
| **High cholesterol** | **+0.3618** | 0.1222 | ±0.2444 | **+2.960** | **0.0031** | 1.4359 | ** |
| **Kidney disease** | **+0.4941** | 0.1716 | ±0.3433 | **+2.879** | **0.0040** | 1.6391 | ** |
| **Circulatory disease** | **+0.5006** | 0.1488 | ±0.2975 | **+3.365** | **7.66e-04** | 1.6496 | *** |
| Time < 70 (%) | +0.0108 | 0.0311 | ±0.0622 | +0.347 | 0.7284 | 1.0109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.55** (p = **3.20e-24**), AUC = **0.6801**, AIC = **1953.9**, BIC = **2021.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4694 | 0.4545 | ±0.9090 | -1.033 | 0.3017 | 0.6254 |  |
| Education: graduate level (vs college) | -0.2161 | 0.1299 | ±0.2597 | -1.664 | 0.0962 | 0.8057 | . |
| Education: high school or below (vs college) | +0.2898 | 0.1714 | ±0.3428 | +1.691 | 0.0909 | 1.3362 | . |
| Site: UCSD (vs UAB) | -0.0608 | 0.1511 | ±0.3021 | -0.402 | 0.6876 | 0.9411 |  |
| Site: UW (vs UAB) | +0.0202 | 0.1395 | ±0.2791 | +0.145 | 0.8851 | 1.0204 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.885** | **5.78e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.276** | **1.90e-05** | 1.0331 | *** |
| Hypertension | +0.1684 | 0.1284 | ±0.2568 | +1.311 | 0.1897 | 1.1834 |  |
| **High cholesterol** | **+0.3620** | 0.1222 | ±0.2444 | **+2.963** | **0.0030** | 1.4362 | ** |
| **Kidney disease** | **+0.4942** | 0.1716 | ±0.3433 | **+2.880** | **0.0040** | 1.6392 | ** |
| **Circulatory disease** | **+0.5007** | 0.1487 | ±0.2975 | **+3.366** | **7.63e-04** | 1.6498 | *** |
| Avg. daily time < 70 (%) | +0.0135 | 0.0311 | ±0.0623 | +0.432 | 0.6654 | 1.0136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0679**, LLR χ² = **140.54** (p = **1.27e-24**), AUC = **0.6819**, AIC = **1951.9**, BIC = **2019.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1827 | 0.6236 | ±1.2473 | +0.293 | 0.7696 | 1.2004 |  |
| Education: graduate level (vs college) | -0.2066 | 0.1301 | ±0.2601 | -1.589 | 0.1121 | 0.8133 |  |
| Education: high school or below (vs college) | +0.2624 | 0.1724 | ±0.3447 | +1.522 | 0.1280 | 1.3000 |  |
| Site: UCSD (vs UAB) | -0.0514 | 0.1510 | ±0.3019 | -0.341 | 0.7334 | 0.9499 |  |
| Site: UW (vs UAB) | +0.0310 | 0.1396 | ±0.2792 | +0.222 | 0.8242 | 1.0315 |  |
| **Age (years)** | **-0.0398** | 0.0058 | ±0.0116 | **-6.849** | **7.42e-12** | 0.9610 | *** |
| **BMI (kg/m2)** | **+0.0322** | 0.0076 | ±0.0153 | **+4.224** | **2.40e-05** | 1.0327 | *** |
| Hypertension | +0.1571 | 0.1286 | ±0.2572 | +1.222 | 0.2219 | 1.1701 |  |
| **High cholesterol** | **+0.3554** | 0.1221 | ±0.2442 | **+2.911** | **0.0036** | 1.4268 | ** |
| **Kidney disease** | **+0.4784** | 0.1722 | ±0.3444 | **+2.778** | **0.0055** | 1.6134 | ** |
| **Circulatory disease** | **+0.4981** | 0.1487 | ±0.2975 | **+3.349** | **8.11e-04** | 1.6455 | *** |
| Time 54-250, pooled (%) | -0.0066 | 0.0044 | ±0.0089 | -1.496 | 0.1345 | 0.9934 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0677**, LLR χ² = **140.03** (p = **1.60e-24**), AUC = **0.6817**, AIC = **1952.4**, BIC = **2020.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1181 | 0.6317 | ±1.2634 | +0.187 | 0.8516 | 1.1254 |  |
| Education: graduate level (vs college) | -0.2082 | 0.1300 | ±0.2601 | -1.602 | 0.1093 | 0.8120 |  |
| Education: high school or below (vs college) | +0.2653 | 0.1723 | ±0.3446 | +1.540 | 0.1236 | 1.3038 |  |
| Site: UCSD (vs UAB) | -0.0532 | 0.1509 | ±0.3019 | -0.353 | 0.7244 | 0.9482 |  |
| Site: UW (vs UAB) | +0.0286 | 0.1395 | ±0.2790 | +0.205 | 0.8375 | 1.0290 |  |
| **Age (years)** | **-0.0399** | 0.0058 | ±0.0116 | **-6.861** | **6.82e-12** | 0.9609 | *** |
| **BMI (kg/m2)** | **+0.0322** | 0.0076 | ±0.0152 | **+4.230** | **2.34e-05** | 1.0328 | *** |
| Hypertension | +0.1587 | 0.1286 | ±0.2571 | +1.234 | 0.2170 | 1.1720 |  |
| **High cholesterol** | **+0.3560** | 0.1221 | ±0.2442 | **+2.915** | **0.0036** | 1.4276 | ** |
| **Kidney disease** | **+0.4794** | 0.1722 | ±0.3444 | **+2.784** | **0.0054** | 1.6152 | ** |
| **Circulatory disease** | **+0.4982** | 0.1487 | ±0.2974 | **+3.350** | **8.08e-04** | 1.6458 | *** |
| Avg. daily time 54-250 (%) | -0.0059 | 0.0045 | ±0.0091 | -1.310 | 0.1901 | 0.9941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0685**, LLR χ² = **141.76** (p = **7.14e-25**), AUC = **0.6816**, AIC = **1950.7**, BIC = **2018.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4272 | 0.4547 | ±0.9093 | -0.940 | 0.3474 | 0.6523 |  |
| Education: graduate level (vs college) | -0.2098 | 0.1299 | ±0.2598 | -1.615 | 0.1064 | 0.8107 |  |
| Education: high school or below (vs college) | +0.2636 | 0.1718 | ±0.3435 | +1.534 | 0.1249 | 1.3016 |  |
| Site: UCSD (vs UAB) | -0.0514 | 0.1508 | ±0.3017 | -0.341 | 0.7334 | 0.9499 |  |
| Site: UW (vs UAB) | +0.0224 | 0.1392 | ±0.2784 | +0.161 | 0.8724 | 1.0226 |  |
| **Age (years)** | **-0.0409** | 0.0058 | ±0.0117 | **-7.009** | **2.39e-12** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0314** | 0.0077 | ±0.0153 | **+4.106** | **4.03e-05** | 1.0319 | *** |
| Hypertension | +0.1523 | 0.1288 | ±0.2576 | +1.183 | 0.2370 | 1.1645 |  |
| **High cholesterol** | **+0.3449** | 0.1225 | ±0.2449 | **+2.816** | **0.0049** | 1.4118 | ** |
| **Kidney disease** | **+0.4555** | 0.1731 | ±0.3463 | **+2.631** | **0.0085** | 1.5770 | ** |
| **Circulatory disease** | **+0.4947** | 0.1490 | ±0.2980 | **+3.320** | **8.99e-04** | 1.6400 | *** |
| Time 181-250, pooled (%) | +0.0081 | 0.0043 | ±0.0087 | +1.865 | 0.0622 | 1.0081 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0686**, LLR χ² = **141.93** (p = **6.61e-25**), AUC = **0.6817**, AIC = **1950.5**, BIC = **2018.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4272 | 0.4547 | ±0.9094 | -0.939 | 0.3475 | 0.6523 |  |
| Education: graduate level (vs college) | -0.2100 | 0.1299 | ±0.2598 | -1.617 | 0.1060 | 0.8106 |  |
| Education: high school or below (vs college) | +0.2620 | 0.1718 | ±0.3437 | +1.525 | 0.1273 | 1.2996 |  |
| Site: UCSD (vs UAB) | -0.0500 | 0.1509 | ±0.3018 | -0.332 | 0.7401 | 0.9512 |  |
| Site: UW (vs UAB) | +0.0232 | 0.1392 | ±0.2784 | +0.167 | 0.8675 | 1.0235 |  |
| **Age (years)** | **-0.0409** | 0.0058 | ±0.0117 | **-7.009** | **2.41e-12** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0314** | 0.0077 | ±0.0153 | **+4.098** | **4.16e-05** | 1.0319 | *** |
| Hypertension | +0.1520 | 0.1288 | ±0.2576 | +1.180 | 0.2379 | 1.1642 |  |
| **High cholesterol** | **+0.3444** | 0.1225 | ±0.2450 | **+2.812** | **0.0049** | 1.4111 | ** |
| **Kidney disease** | **+0.4545** | 0.1732 | ±0.3463 | **+2.625** | **0.0087** | 1.5753 | ** |
| **Circulatory disease** | **+0.4950** | 0.1490 | ±0.2979 | **+3.323** | **8.91e-04** | 1.6405 | *** |
| Avg. daily time 181-250 (%) | +0.0081 | 0.0043 | ±0.0085 | +1.910 | 0.0561 | 1.0082 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0688**, LLR χ² = **142.34** (p = **5.44e-25**), AUC = **0.6824**, AIC = **1950.1**, BIC = **2018.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4553 | 0.4545 | ±0.9091 | -1.002 | 0.3165 | 0.6343 |  |
| Education: graduate level (vs college) | -0.2033 | 0.1301 | ±0.2602 | -1.563 | 0.1181 | 0.8160 |  |
| Education: high school or below (vs college) | +0.2519 | 0.1724 | ±0.3449 | +1.461 | 0.1441 | 1.2864 |  |
| Site: UCSD (vs UAB) | -0.0455 | 0.1511 | ±0.3021 | -0.302 | 0.7630 | 0.9555 |  |
| Site: UW (vs UAB) | +0.0322 | 0.1395 | ±0.2790 | +0.231 | 0.8176 | 1.0327 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.955** | **3.52e-12** | 0.9604 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0077 | ±0.0153 | **+4.122** | **3.76e-05** | 1.0320 | *** |
| Hypertension | +0.1493 | 0.1289 | ±0.2577 | +1.159 | 0.2465 | 1.1611 |  |
| **High cholesterol** | **+0.3464** | 0.1223 | ±0.2447 | **+2.831** | **0.0046** | 1.4139 | ** |
| **Kidney disease** | **+0.4561** | 0.1730 | ±0.3460 | **+2.636** | **0.0084** | 1.5780 | ** |
| **Circulatory disease** | **+0.4945** | 0.1489 | ±0.2978 | **+3.322** | **8.95e-04** | 1.6397 | *** |
| **Time > 180 (%)** | **+0.0053** | 0.0026 | ±0.0052 | **+2.022** | **0.0432** | 1.0053 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0687**, LLR χ² = **142.02** (p = **6.32e-25**), AUC = **0.6824**, AIC = **1950.4**, BIC = **2018.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4529 | 0.4545 | ±0.9090 | -0.997 | 0.3190 | 0.6358 |  |
| Education: graduate level (vs college) | -0.2045 | 0.1301 | ±0.2601 | -1.572 | 0.1159 | 0.8151 |  |
| Education: high school or below (vs college) | +0.2527 | 0.1724 | ±0.3449 | +1.466 | 0.1428 | 1.2875 |  |
| Site: UCSD (vs UAB) | -0.0456 | 0.1511 | ±0.3021 | -0.302 | 0.7626 | 0.9554 |  |
| Site: UW (vs UAB) | +0.0315 | 0.1395 | ±0.2790 | +0.226 | 0.8213 | 1.0320 |  |
| **Age (years)** | **-0.0404** | 0.0058 | ±0.0116 | **-6.954** | **3.56e-12** | 0.9604 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0077 | ±0.0153 | **+4.124** | **3.73e-05** | 1.0321 | *** |
| Hypertension | +0.1504 | 0.1288 | ±0.2577 | +1.168 | 0.2429 | 1.1623 |  |
| **High cholesterol** | **+0.3468** | 0.1223 | ±0.2447 | **+2.835** | **0.0046** | 1.4146 | ** |
| **Kidney disease** | **+0.4568** | 0.1730 | ±0.3461 | **+2.640** | **0.0083** | 1.5791 | ** |
| **Circulatory disease** | **+0.4948** | 0.1489 | ±0.2977 | **+3.324** | **8.88e-04** | 1.6402 | *** |
| Avg. daily time > 180 (%) | +0.0051 | 0.0026 | ±0.0052 | +1.937 | 0.0527 | 1.0051 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0710**, LLR χ² = **146.95** (p = **6.25e-26**), AUC = **0.6860**, AIC = **1945.5**, BIC = **2013.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4481 | 0.4553 | ±0.9106 | -0.984 | 0.3251 | 0.6388 |  |
| Education: graduate level (vs college) | -0.1901 | 0.1304 | ±0.2608 | -1.458 | 0.1449 | 0.8269 |  |
| Education: high school or below (vs college) | +0.2402 | 0.1726 | ±0.3453 | +1.391 | 0.1642 | 1.2714 |  |
| Site: UCSD (vs UAB) | -0.0329 | 0.1513 | ±0.3027 | -0.217 | 0.8279 | 0.9676 |  |
| Site: UW (vs UAB) | +0.0373 | 0.1397 | ±0.2795 | +0.267 | 0.7893 | 1.0380 |  |
| **Age (years)** | **-0.0403** | 0.0058 | ±0.0116 | **-6.923** | **4.42e-12** | 0.9605 | *** |
| **BMI (kg/m2)** | **+0.0304** | 0.0077 | ±0.0154 | **+3.950** | **7.81e-05** | 1.0309 | *** |
| Hypertension | +0.1496 | 0.1289 | ±0.2578 | +1.161 | 0.2457 | 1.1614 |  |
| **High cholesterol** | **+0.3446** | 0.1224 | ±0.2448 | **+2.815** | **0.0049** | 1.4114 | ** |
| **Kidney disease** | **+0.4540** | 0.1728 | ±0.3456 | **+2.627** | **0.0086** | 1.5745 | ** |
| **Circulatory disease** | **+0.4947** | 0.1491 | ±0.2981 | **+3.318** | **9.06e-04** | 1.6399 | *** |
| **Nocturnal time > 180 (%)** | **+0.0076** | 0.0025 | ±0.0051 | **+2.991** | **0.0028** | 1.0076 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0676**, LLR χ² = **139.84** (p = **1.75e-24**), AUC = **0.6795**, AIC = **1952.6**, BIC = **2020.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4663 | 0.4543 | ±0.9085 | -1.026 | 0.3047 | 0.6273 |  |
| Education: graduate level (vs college) | -0.2088 | 0.1300 | ±0.2600 | -1.606 | 0.1083 | 0.8116 |  |
| Education: high school or below (vs college) | +0.2767 | 0.1715 | ±0.3430 | +1.614 | 0.1066 | 1.3188 |  |
| Site: UCSD (vs UAB) | -0.0603 | 0.1506 | ±0.3012 | -0.400 | 0.6891 | 0.9415 |  |
| Site: UW (vs UAB) | +0.0175 | 0.1390 | ±0.2780 | +0.126 | 0.8997 | 1.0177 |  |
| **Age (years)** | **-0.0407** | 0.0058 | ±0.0117 | **-6.957** | **3.47e-12** | 0.9602 | *** |
| **BMI (kg/m2)** | **+0.0327** | 0.0076 | ±0.0152 | **+4.291** | **1.78e-05** | 1.0332 | *** |
| Hypertension | +0.1530 | 0.1290 | ±0.2579 | +1.187 | 0.2354 | 1.1654 |  |
| **High cholesterol** | **+0.3511** | 0.1224 | ±0.2447 | **+2.869** | **0.0041** | 1.4206 | ** |
| **Kidney disease** | **+0.4709** | 0.1728 | ±0.3456 | **+2.725** | **0.0064** | 1.6014 | ** |
| **Circulatory disease** | **+0.5012** | 0.1488 | ±0.2976 | **+3.368** | **7.56e-04** | 1.6508 | *** |
| Any reading > 250 during wear (0/1) | +0.1474 | 0.1212 | ±0.2424 | +1.216 | 0.2240 | 1.1588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0680**, LLR χ² = **140.58** (p = **1.24e-24**), AUC = **0.6820**, AIC = **1951.9**, BIC = **2019.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4800 | 0.4546 | ±0.9092 | -1.056 | 0.2910 | 0.6188 |  |
| Education: graduate level (vs college) | -0.2066 | 0.1300 | ±0.2601 | -1.589 | 0.1121 | 0.8133 |  |
| Education: high school or below (vs college) | +0.2617 | 0.1724 | ±0.3448 | +1.518 | 0.1291 | 1.2991 |  |
| Site: UCSD (vs UAB) | -0.0523 | 0.1509 | ±0.3019 | -0.347 | 0.7289 | 0.9490 |  |
| Site: UW (vs UAB) | +0.0304 | 0.1395 | ±0.2791 | +0.218 | 0.8277 | 1.0308 |  |
| **Age (years)** | **-0.0398** | 0.0058 | ±0.0116 | **-6.850** | **7.36e-12** | 0.9610 | *** |
| **BMI (kg/m2)** | **+0.0322** | 0.0076 | ±0.0153 | **+4.225** | **2.39e-05** | 1.0327 | *** |
| Hypertension | +0.1569 | 0.1286 | ±0.2572 | +1.220 | 0.2225 | 1.1699 |  |
| **High cholesterol** | **+0.3550** | 0.1221 | ±0.2442 | **+2.907** | **0.0036** | 1.4262 | ** |
| **Kidney disease** | **+0.4782** | 0.1722 | ±0.3444 | **+2.777** | **0.0055** | 1.6131 | ** |
| **Circulatory disease** | **+0.4983** | 0.1487 | ±0.2974 | **+3.350** | **8.07e-04** | 1.6459 | *** |
| Time > 250 (%) | +0.0067 | 0.0044 | ±0.0089 | +1.510 | 0.1310 | 1.0067 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0677**, LLR χ² = **140.05** (p = **1.59e-24**), AUC = **0.6817**, AIC = **1952.4**, BIC = **2020.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4743 | 0.4544 | ±0.9088 | -1.044 | 0.2966 | 0.6224 |  |
| Education: graduate level (vs college) | -0.2083 | 0.1300 | ±0.2600 | -1.602 | 0.1091 | 0.8119 |  |
| Education: high school or below (vs college) | +0.2648 | 0.1723 | ±0.3447 | +1.537 | 0.1244 | 1.3032 |  |
| Site: UCSD (vs UAB) | -0.0538 | 0.1509 | ±0.3018 | -0.357 | 0.7215 | 0.9476 |  |
| Site: UW (vs UAB) | +0.0281 | 0.1395 | ±0.2790 | +0.201 | 0.8405 | 1.0285 |  |
| **Age (years)** | **-0.0399** | 0.0058 | ±0.0116 | **-6.861** | **6.83e-12** | 0.9609 | *** |
| **BMI (kg/m2)** | **+0.0323** | 0.0076 | ±0.0152 | **+4.230** | **2.33e-05** | 1.0328 | *** |
| Hypertension | +0.1586 | 0.1286 | ±0.2571 | +1.233 | 0.2174 | 1.1718 |  |
| **High cholesterol** | **+0.3557** | 0.1221 | ±0.2442 | **+2.913** | **0.0036** | 1.4271 | ** |
| **Kidney disease** | **+0.4794** | 0.1722 | ±0.3444 | **+2.784** | **0.0054** | 1.6150 | ** |
| **Circulatory disease** | **+0.4984** | 0.1487 | ±0.2974 | **+3.351** | **8.05e-04** | 1.6460 | *** |
| Avg. daily time > 250 (%) | +0.0060 | 0.0045 | ±0.0090 | +1.317 | 0.1877 | 1.0060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
