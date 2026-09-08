# Phase 6 model output tables - All (analysis base) - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 1,270; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0914**, F-statistic = **13.77** (p = **2.80e-23**), Residual SE = **4.595** on **1259** df, AIC = **7488.4**, BIC = **7545.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4220** | 1.0738 | ±2.1476 | **+6.912** | **4.79e-12** | *** |
| Education: graduate level (vs college) | -0.4358 | 0.2745 | ±0.5489 | -1.588 | 0.1123 |  |
| **Education: high school or below (vs college)** | **+1.3322** | 0.5851 | ±1.1702 | **+2.277** | **0.0228** | * |
| Site: UCSD (vs UAB) | -0.2311 | 0.3587 | ±0.7174 | -0.644 | 0.5194 |  |
| Site: UW (vs UAB) | +0.0039 | 0.3349 | ±0.6699 | +0.012 | 0.9908 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.226** | **4.99e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.099** | **4.14e-05** | *** |
| Hypertension | +0.5028 | 0.2981 | ±0.5963 | +1.687 | 0.0917 | . |
| **High cholesterol** | **+0.7229** | 0.2676 | ±0.5353 | **+2.701** | **0.0069** | ** |
| Kidney disease | +0.8364 | 0.5977 | ±1.1953 | +1.399 | 0.1617 |  |
| **Circulatory disease** | **+0.9609** | 0.4401 | ±0.8803 | **+2.183** | **0.0290** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5651** | 1.7905 | ±3.5810 | **+4.225** | **2.39e-05** | *** |
| Education: graduate level (vs college) | -0.4356 | 0.2749 | ±0.5497 | -1.585 | 0.1130 |  |
| **Education: high school or below (vs college)** | **+1.3360** | 0.5895 | ±1.1790 | **+2.266** | **0.0234** | * |
| Site: UCSD (vs UAB) | -0.2304 | 0.3589 | ±0.7177 | -0.642 | 0.5208 |  |
| Site: UW (vs UAB) | +0.0049 | 0.3353 | ±0.6706 | +0.015 | 0.9883 |  |
| **Age (years)** | **-0.0881** | 0.0124 | ±0.0247 | **-7.128** | **1.02e-12** | *** |
| **BMI (kg/m2)** | **+0.0982** | 0.0238 | ±0.0477 | **+4.121** | **3.77e-05** | *** |
| Hypertension | +0.5043 | 0.2989 | ±0.5977 | +1.688 | 0.0915 | . |
| **High cholesterol** | **+0.7259** | 0.2705 | ±0.5409 | **+2.684** | **0.0073** | ** |
| Kidney disease | +0.8360 | 0.5984 | ±1.1967 | +1.397 | 0.1624 |  |
| **Circulatory disease** | **+0.9631** | 0.4397 | ±0.8795 | **+2.190** | **0.0285** | * |
| HbA1c (%) | -0.0281 | 0.2814 | ±0.5627 | -0.100 | 0.9205 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.68e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7712** | 1.3806 | ±2.7612 | **+5.629** | **1.81e-08** | *** |
| Education: graduate level (vs college) | -0.4282 | 0.2756 | ±0.5511 | -1.554 | 0.1202 |  |
| **Education: high school or below (vs college)** | **+1.3477** | 0.5901 | ±1.1802 | **+2.284** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2329 | 0.3590 | ±0.7180 | -0.649 | 0.5165 |  |
| Site: UW (vs UAB) | +0.0134 | 0.3365 | ±0.6731 | +0.040 | 0.9683 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0245 | **-7.187** | **6.61e-13** | *** |
| **BMI (kg/m2)** | **+0.0984** | 0.0239 | ±0.0477 | **+4.124** | **3.73e-05** | *** |
| Hypertension | +0.5133 | 0.2994 | ±0.5989 | +1.714 | 0.0865 | . |
| **High cholesterol** | **+0.7292** | 0.2681 | ±0.5361 | **+2.720** | **0.0065** | ** |
| Kidney disease | +0.8463 | 0.5982 | ±1.1964 | +1.415 | 0.1572 |  |
| **Circulatory disease** | **+0.9711** | 0.4410 | ±0.8820 | **+2.202** | **0.0277** | * |
| Mean glucose (mg/dL) | -0.0032 | 0.0078 | ±0.0156 | -0.414 | 0.6792 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.68e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2182** | 2.2246 | ±4.4492 | **+3.694** | **2.21e-04** | *** |
| Education: graduate level (vs college) | -0.4282 | 0.2756 | ±0.5511 | -1.554 | 0.1202 |  |
| **Education: high school or below (vs college)** | **+1.3477** | 0.5901 | ±1.1802 | **+2.284** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2329 | 0.3590 | ±0.7180 | -0.649 | 0.5165 |  |
| Site: UW (vs UAB) | +0.0134 | 0.3365 | ±0.6731 | +0.040 | 0.9683 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0245 | **-7.187** | **6.61e-13** | *** |
| **BMI (kg/m2)** | **+0.0984** | 0.0239 | ±0.0477 | **+4.124** | **3.73e-05** | *** |
| Hypertension | +0.5133 | 0.2994 | ±0.5989 | +1.714 | 0.0865 | . |
| **High cholesterol** | **+0.7292** | 0.2681 | ±0.5361 | **+2.720** | **0.0065** | ** |
| Kidney disease | +0.8463 | 0.5982 | ±1.1964 | +1.415 | 0.1572 |  |
| **Circulatory disease** | **+0.9711** | 0.4410 | ±0.8820 | **+2.202** | **0.0277** | * |
| GMI (%) | -0.1350 | 0.3265 | ±0.6531 | -0.414 | 0.6792 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.00e-22**), Residual SE = **4.596** on **1258** df, AIC = **7490.3**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.6920** | 1.3362 | ±2.6724 | **+5.757** | **8.58e-09** | *** |
| Education: graduate level (vs college) | -0.4314 | 0.2755 | ±0.5509 | -1.566 | 0.1173 |  |
| **Education: high school or below (vs college)** | **+1.3451** | 0.5902 | ±1.1803 | **+2.279** | **0.0227** | * |
| Site: UCSD (vs UAB) | -0.2289 | 0.3590 | ±0.7180 | -0.638 | 0.5237 |  |
| Site: UW (vs UAB) | +0.0111 | 0.3360 | ±0.6720 | +0.033 | 0.9735 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.232** | **4.76e-13** | *** |
| **BMI (kg/m2)** | **+0.0990** | 0.0240 | ±0.0480 | **+4.128** | **3.65e-05** | *** |
| Hypertension | +0.5095 | 0.2982 | ±0.5964 | +1.708 | 0.0876 | . |
| **High cholesterol** | **+0.7300** | 0.2680 | ±0.5360 | **+2.724** | **0.0065** | ** |
| Kidney disease | +0.8376 | 0.5976 | ±1.1952 | +1.402 | 0.1610 |  |
| **Circulatory disease** | **+0.9662** | 0.4409 | ±0.8817 | **+2.192** | **0.0284** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0026 | 0.0076 | ±0.0151 | -0.338 | 0.7354 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4523** | 1.1550 | ±2.3101 | **+6.452** | **1.10e-10** | *** |
| Education: graduate level (vs college) | -0.4355 | 0.2747 | ±0.5493 | -1.586 | 0.1128 |  |
| **Education: high school or below (vs college)** | **+1.3324** | 0.5856 | ±1.1711 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | -0.2325 | 0.3583 | ±0.7166 | -0.649 | 0.5163 |  |
| Site: UW (vs UAB) | +0.0047 | 0.3362 | ±0.6725 | +0.014 | 0.9890 |  |
| **Age (years)** | **-0.0881** | 0.0123 | ±0.0245 | **-7.186** | **6.68e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.099** | **4.14e-05** | *** |
| Hypertension | +0.5048 | 0.3006 | ±0.6012 | +1.679 | 0.0931 | . |
| **High cholesterol** | **+0.7228** | 0.2678 | ±0.5357 | **+2.699** | **0.0070** | ** |
| Kidney disease | +0.8397 | 0.5978 | ±1.1956 | +1.405 | 0.1601 |  |
| **Circulatory disease** | **+0.9625** | 0.4410 | ±0.8821 | **+2.182** | **0.0291** | * |
| Glucose SD, pooled (mg/dL) | -0.0017 | 0.0206 | ±0.0412 | -0.081 | 0.9358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.02e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.3**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5380** | 1.1435 | ±2.2870 | **+6.592** | **4.34e-11** | *** |
| Education: graduate level (vs college) | -0.4340 | 0.2747 | ±0.5494 | -1.580 | 0.1141 |  |
| **Education: high school or below (vs college)** | **+1.3332** | 0.5861 | ±1.1722 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | -0.2364 | 0.3581 | ±0.7162 | -0.660 | 0.5092 |  |
| Site: UW (vs UAB) | +0.0078 | 0.3367 | ±0.6734 | +0.023 | 0.9816 |  |
| **Age (years)** | **-0.0879** | 0.0123 | ±0.0246 | **-7.159** | **8.10e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0239 | ±0.0478 | **+4.109** | **3.97e-05** | *** |
| Hypertension | +0.5109 | 0.3005 | ±0.6010 | +1.700 | 0.0891 | . |
| **High cholesterol** | **+0.7229** | 0.2678 | ±0.5356 | **+2.699** | **0.0069** | ** |
| Kidney disease | +0.8509 | 0.5983 | ±1.1967 | +1.422 | 0.1550 |  |
| **Circulatory disease** | **+0.9674** | 0.4410 | ±0.8820 | **+2.194** | **0.0282** | * |
| Avg. daily SD (mg/dL) | -0.0073 | 0.0225 | ±0.0450 | -0.326 | 0.7446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.51** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2921** | 1.2139 | ±2.4279 | **+6.007** | **1.89e-09** | *** |
| Education: graduate level (vs college) | -0.4339 | 0.2751 | ±0.5501 | -1.577 | 0.1147 |  |
| **Education: high school or below (vs college)** | **+1.3360** | 0.5873 | ±1.1746 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | -0.2258 | 0.3578 | ±0.7157 | -0.631 | 0.5281 |  |
| Site: UW (vs UAB) | +0.0047 | 0.3348 | ±0.6697 | +0.014 | 0.9887 |  |
| **Age (years)** | **-0.0884** | 0.0122 | ±0.0245 | **-7.215** | **5.38e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0240 | ±0.0479 | **+4.092** | **4.27e-05** | *** |
| Hypertension | +0.4992 | 0.2994 | ±0.5987 | +1.668 | 0.0954 | . |
| **High cholesterol** | **+0.7258** | 0.2678 | ±0.5356 | **+2.710** | **0.0067** | ** |
| Kidney disease | +0.8283 | 0.5970 | ±1.1941 | +1.387 | 0.1653 |  |
| **Circulatory disease** | **+0.9590** | 0.4406 | ±0.8813 | **+2.176** | **0.0295** | * |
| CV (%) | +0.0077 | 0.0304 | ±0.0608 | +0.252 | 0.8013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.54** (p = **9.35e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7759** | 1.2268 | ±2.4536 | **+6.338** | **2.32e-10** | *** |
| Education: graduate level (vs college) | -0.4309 | 0.2751 | ±0.5502 | -1.566 | 0.1173 |  |
| **Education: high school or below (vs college)** | **+1.3353** | 0.5850 | ±1.1700 | **+2.282** | **0.0225** | * |
| Site: UCSD (vs UAB) | -0.2204 | 0.3580 | ±0.7159 | -0.616 | 0.5380 |  |
| Site: UW (vs UAB) | +0.0024 | 0.3355 | ±0.6709 | +0.007 | 0.9942 |  |
| **Age (years)** | **-0.0886** | 0.0123 | ±0.0245 | **-7.227** | **4.95e-13** | *** |
| **BMI (kg/m2)** | **+0.0982** | 0.0239 | ±0.0479 | **+4.101** | **4.11e-05** | *** |
| Hypertension | +0.4939 | 0.2995 | ±0.5990 | +1.649 | 0.0992 | . |
| **High cholesterol** | **+0.7274** | 0.2677 | ±0.5355 | **+2.717** | **0.0066** | ** |
| Kidney disease | +0.8225 | 0.5962 | ±1.1924 | +1.380 | 0.1677 |  |
| **Circulatory disease** | **+0.9581** | 0.4406 | ±0.8811 | **+2.175** | **0.0297** | * |
| Mean / SD ratio | -0.0574 | 0.1017 | ±0.2034 | -0.564 | 0.5727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.05e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2850** | 1.2499 | ±2.4999 | **+5.828** | **5.60e-09** | *** |
| Education: graduate level (vs college) | -0.4367 | 0.2748 | ±0.5496 | -1.589 | 0.1120 |  |
| **Education: high school or below (vs college)** | **+1.3321** | 0.5860 | ±1.1720 | **+2.273** | **0.0230** | * |
| Site: UCSD (vs UAB) | -0.2342 | 0.3579 | ±0.7158 | -0.654 | 0.5128 |  |
| Site: UW (vs UAB) | +0.0050 | 0.3359 | ±0.6719 | +0.015 | 0.9881 |  |
| **Age (years)** | **-0.0880** | 0.0123 | ±0.0245 | **-7.169** | **7.57e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.099** | **4.16e-05** | *** |
| Hypertension | +0.5053 | 0.2992 | ±0.5984 | +1.689 | 0.0913 | . |
| **High cholesterol** | **+0.7213** | 0.2677 | ±0.5355 | **+2.694** | **0.0071** | ** |
| Kidney disease | +0.8432 | 0.5981 | ±1.1962 | +1.410 | 0.1586 |  |
| **Circulatory disease** | **+0.9616** | 0.4405 | ±0.8810 | **+2.183** | **0.0290** | * |
| Avg. daily mean/SD | +0.0183 | 0.0870 | ±0.1741 | +0.210 | 0.8333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4770** | 1.2256 | ±2.4511 | **+6.101** | **1.05e-09** | *** |
| Education: graduate level (vs college) | -0.4362 | 0.2747 | ±0.5494 | -1.588 | 0.1123 |  |
| **Education: high school or below (vs college)** | **+1.3329** | 0.5864 | ±1.1728 | **+2.273** | **0.0230** | * |
| Site: UCSD (vs UAB) | -0.2329 | 0.3594 | ±0.7188 | -0.648 | 0.5170 |  |
| Site: UW (vs UAB) | +0.0020 | 0.3355 | ±0.6709 | +0.006 | 0.9953 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.239** | **4.54e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0479 | **+4.094** | **4.25e-05** | *** |
| Hypertension | +0.5026 | 0.2983 | ±0.5965 | +1.685 | 0.0919 | . |
| **High cholesterol** | **+0.7217** | 0.2688 | ±0.5375 | **+2.686** | **0.0072** | ** |
| Kidney disease | +0.8376 | 0.5978 | ±1.1955 | +1.401 | 0.1611 |  |
| **Circulatory disease** | **+0.9614** | 0.4407 | ±0.8814 | **+2.182** | **0.0291** | * |
| MAG (mg/dL/h) | -0.0014 | 0.0170 | ±0.0339 | -0.080 | 0.9359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.51** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5354** | 1.1866 | ±2.3731 | **+6.351** | **2.15e-10** | *** |
| Education: graduate level (vs college) | -0.4344 | 0.2747 | ±0.5494 | -1.581 | 0.1138 |  |
| **Education: high school or below (vs college)** | **+1.3335** | 0.5858 | ±1.1717 | **+2.276** | **0.0228** | * |
| Site: UCSD (vs UAB) | -0.2352 | 0.3584 | ±0.7168 | -0.656 | 0.5117 |  |
| Site: UW (vs UAB) | +0.0051 | 0.3358 | ±0.6716 | +0.015 | 0.9879 |  |
| **Age (years)** | **-0.0880** | 0.0123 | ±0.0245 | **-7.177** | **7.14e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0240 | ±0.0481 | **+4.070** | **4.70e-05** | *** |
| Hypertension | +0.5068 | 0.2996 | ±0.5991 | +1.692 | 0.0907 | . |
| **High cholesterol** | **+0.7215** | 0.2677 | ±0.5355 | **+2.695** | **0.0070** | ** |
| Kidney disease | +0.8445 | 0.5978 | ±1.1955 | +1.413 | 0.1577 |  |
| **Circulatory disease** | **+0.9652** | 0.4407 | ±0.8814 | **+2.190** | **0.0285** | * |
| Avg. daily range (mg/dL) | -0.0012 | 0.0052 | ±0.0103 | -0.237 | 0.8128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1270**, R² = **0.0990**, Adj R² = **0.0911**, F-statistic = **12.56** (p = **8.33e-23**), Residual SE = **4.596** on **1258** df, AIC = **7489.9**, BIC = **7551.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2639** | 1.0951 | ±2.1901 | **+6.633** | **3.28e-11** | *** |
| Education: graduate level (vs college) | -0.4367 | 0.2745 | ±0.5490 | -1.591 | 0.1117 |  |
| **Education: high school or below (vs college)** | **+1.3329** | 0.5849 | ±1.1699 | **+2.279** | **0.0227** | * |
| Site: UCSD (vs UAB) | -0.2191 | 0.3600 | ±0.7199 | -0.609 | 0.5428 |  |
| Site: UW (vs UAB) | +0.0006 | 0.3352 | ±0.6704 | +0.002 | 0.9987 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.227** | **4.92e-13** | *** |
| **BMI (kg/m2)** | **+0.0970** | 0.0238 | ±0.0477 | **+4.071** | **4.69e-05** | *** |
| Hypertension | +0.4996 | 0.2984 | ±0.5968 | +1.674 | 0.0941 | . |
| **High cholesterol** | **+0.7188** | 0.2679 | ±0.5357 | **+2.683** | **0.0073** | ** |
| Kidney disease | +0.8337 | 0.5990 | ±1.1979 | +1.392 | 0.1639 |  |
| **Circulatory disease** | **+0.9496** | 0.4405 | ±0.8810 | **+2.156** | **0.0311** | * |
| SD of daily means (mg/dL) | +0.0290 | 0.0356 | ±0.0712 | +0.816 | 0.4145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0910**, F-statistic = **12.54** (p = **9.16e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2654** | 2.2524 | ±4.5047 | **+3.670** | **2.43e-04** | *** |
| Education: graduate level (vs college) | -0.4397 | 0.2751 | ±0.5503 | -1.598 | 0.1100 |  |
| **Education: high school or below (vs college)** | **+1.3254** | 0.5861 | ±1.1721 | **+2.261** | **0.0237** | * |
| Site: UCSD (vs UAB) | -0.2201 | 0.3597 | ±0.7193 | -0.612 | 0.5405 |  |
| Site: UW (vs UAB) | +0.0041 | 0.3353 | ±0.6707 | +0.012 | 0.9903 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.218** | **5.26e-13** | *** |
| **BMI (kg/m2)** | **+0.0976** | 0.0239 | ±0.0478 | **+4.086** | **4.39e-05** | *** |
| Hypertension | +0.4950 | 0.2997 | ±0.5995 | +1.652 | 0.0986 | . |
| **High cholesterol** | **+0.7191** | 0.2682 | ±0.5363 | **+2.682** | **0.0073** | ** |
| Kidney disease | +0.8216 | 0.5992 | ±1.1984 | +1.371 | 0.1703 |  |
| **Circulatory disease** | **+0.9484** | 0.4425 | ±0.8850 | **+2.143** | **0.0321** | * |
| Time in range 70-180, pooled (%) | -0.0086 | 0.0208 | ±0.0416 | -0.415 | 0.6784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1270**, R² = **0.0989**, Adj R² = **0.0910**, F-statistic = **12.55** (p = **8.91e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.0**, BIC = **7551.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3352** | 2.2542 | ±4.5083 | **+3.698** | **2.18e-04** | *** |
| Education: graduate level (vs college) | -0.4401 | 0.2752 | ±0.5503 | -1.600 | 0.1097 |  |
| **Education: high school or below (vs college)** | **+1.3258** | 0.5857 | ±1.1715 | **+2.264** | **0.0236** | * |
| Site: UCSD (vs UAB) | -0.2198 | 0.3596 | ±0.7193 | -0.611 | 0.5412 |  |
| Site: UW (vs UAB) | +0.0043 | 0.3353 | ±0.6706 | +0.013 | 0.9898 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.220** | **5.21e-13** | *** |
| **BMI (kg/m2)** | **+0.0975** | 0.0239 | ±0.0478 | **+4.085** | **4.41e-05** | *** |
| Hypertension | +0.4947 | 0.2996 | ±0.5993 | +1.651 | 0.0988 | . |
| **High cholesterol** | **+0.7183** | 0.2682 | ±0.5365 | **+2.678** | **0.0074** | ** |
| Kidney disease | +0.8202 | 0.5993 | ±1.1986 | +1.369 | 0.1711 |  |
| **Circulatory disease** | **+0.9474** | 0.4425 | ±0.8851 | **+2.141** | **0.0323** | * |
| Avg. daily time in range 70-180 (%) | -0.0093 | 0.0207 | ±0.0413 | -0.449 | 0.6531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3852** | 1.0926 | ±2.1853 | **+6.759** | **1.39e-11** | *** |
| Education: graduate level (vs college) | -0.4325 | 0.2752 | ±0.5504 | -1.571 | 0.1161 |  |
| **Education: high school or below (vs college)** | **+1.3403** | 0.5864 | ±1.1728 | **+2.286** | **0.0223** | * |
| Site: UCSD (vs UAB) | -0.2199 | 0.3611 | ±0.7222 | -0.609 | 0.5425 |  |
| Site: UW (vs UAB) | +0.0088 | 0.3362 | ±0.6724 | +0.026 | 0.9791 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0245 | **-7.188** | **6.57e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0238 | ±0.0477 | **+4.103** | **4.09e-05** | *** |
| Hypertension | +0.5026 | 0.2984 | ±0.5969 | +1.684 | 0.0922 | . |
| **High cholesterol** | **+0.7268** | 0.2678 | ±0.5356 | **+2.714** | **0.0066** | ** |
| Kidney disease | +0.8370 | 0.5984 | ±1.1967 | +1.399 | 0.1619 |  |
| **Circulatory disease** | **+0.9539** | 0.4414 | ±0.8828 | **+2.161** | **0.0307** | * |
| Any reading < 54 during wear (0/1) | +0.0749 | 0.2896 | ±0.5791 | +0.259 | 0.7959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **9.97e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.3**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4578** | 1.0835 | ±2.1670 | **+6.883** | **5.86e-12** | *** |
| Education: graduate level (vs college) | -0.4380 | 0.2748 | ±0.5496 | -1.594 | 0.1110 |  |
| **Education: high school or below (vs college)** | **+1.3236** | 0.5874 | ±1.1748 | **+2.253** | **0.0242** | * |
| Site: UCSD (vs UAB) | -0.2476 | 0.3603 | ±0.7206 | -0.687 | 0.4919 |  |
| Site: UW (vs UAB) | -0.0083 | 0.3364 | ±0.6729 | -0.025 | 0.9803 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.229** | **4.87e-13** | *** |
| **BMI (kg/m2)** | **+0.0979** | 0.0240 | ±0.0479 | **+4.086** | **4.38e-05** | *** |
| Hypertension | +0.4995 | 0.2982 | ±0.5965 | +1.675 | 0.0939 | . |
| **High cholesterol** | **+0.7155** | 0.2686 | ±0.5372 | **+2.664** | **0.0077** | ** |
| Kidney disease | +0.8389 | 0.5978 | ±1.1955 | +1.403 | 0.1605 |  |
| **Circulatory disease** | **+0.9607** | 0.4401 | ±0.8803 | **+2.183** | **0.0291** | * |
| Time < 54 (%) | -0.0907 | 0.2173 | ±0.4346 | -0.417 | 0.6764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4251** | 1.0801 | ±2.1601 | **+6.875** | **6.21e-12** | *** |
| Education: graduate level (vs college) | -0.4362 | 0.2750 | ±0.5500 | -1.586 | 0.1127 |  |
| **Education: high school or below (vs college)** | **+1.3312** | 0.5882 | ±1.1764 | **+2.263** | **0.0236** | * |
| Site: UCSD (vs UAB) | -0.2328 | 0.3593 | ±0.7186 | -0.648 | 0.5170 |  |
| Site: UW (vs UAB) | +0.0022 | 0.3360 | ±0.6719 | +0.007 | 0.9947 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.221** | **5.17e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0479 | **+4.092** | **4.27e-05** | *** |
| Hypertension | +0.5022 | 0.2986 | ±0.5973 | +1.682 | 0.0926 | . |
| **High cholesterol** | **+0.7221** | 0.2681 | ±0.5362 | **+2.693** | **0.0071** | ** |
| Kidney disease | +0.8367 | 0.5980 | ±1.1960 | +1.399 | 0.1617 |  |
| **Circulatory disease** | **+0.9608** | 0.4401 | ±0.8803 | **+2.183** | **0.0290** | * |
| Avg. daily time < 54 (%) | -0.0146 | 0.2485 | ±0.4971 | -0.059 | 0.9533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.51** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3960** | 1.0804 | ±2.1609 | **+6.845** | **7.63e-12** | *** |
| Education: graduate level (vs college) | -0.4322 | 0.2751 | ±0.5503 | -1.571 | 0.1162 |  |
| **Education: high school or below (vs college)** | **+1.3408** | 0.5884 | ±1.1767 | **+2.279** | **0.0227** | * |
| Site: UCSD (vs UAB) | -0.2238 | 0.3585 | ±0.7170 | -0.624 | 0.5325 |  |
| Site: UW (vs UAB) | +0.0116 | 0.3350 | ±0.6700 | +0.035 | 0.9723 |  |
| **Age (years)** | **-0.0881** | 0.0122 | ±0.0244 | **-7.208** | **5.70e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0239 | ±0.0478 | **+4.092** | **4.28e-05** | *** |
| Hypertension | +0.5056 | 0.2981 | ±0.5962 | +1.696 | 0.0899 | . |
| **High cholesterol** | **+0.7267** | 0.2683 | ±0.5365 | **+2.709** | **0.0068** | ** |
| Kidney disease | +0.8368 | 0.5982 | ±1.1963 | +1.399 | 0.1618 |  |
| **Circulatory disease** | **+0.9608** | 0.4403 | ±0.8807 | **+2.182** | **0.0291** | * |
| Time 54-69, pooled (%) | +0.0235 | 0.0999 | ±0.1999 | +0.236 | 0.8138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.74e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3824** | 1.0780 | ±2.1559 | **+6.848** | **7.46e-12** | *** |
| Education: graduate level (vs college) | -0.4288 | 0.2752 | ±0.5505 | -1.558 | 0.1193 |  |
| **Education: high school or below (vs college)** | **+1.3489** | 0.5887 | ±1.1774 | **+2.291** | **0.0219** | * |
| Site: UCSD (vs UAB) | -0.2206 | 0.3585 | ±0.7169 | -0.615 | 0.5383 |  |
| Site: UW (vs UAB) | +0.0178 | 0.3350 | ±0.6700 | +0.053 | 0.9575 |  |
| **Age (years)** | **-0.0881** | 0.0122 | ±0.0244 | **-7.211** | **5.56e-13** | *** |
| **BMI (kg/m2)** | **+0.0977** | 0.0239 | ±0.0478 | **+4.089** | **4.34e-05** | *** |
| Hypertension | +0.5085 | 0.2982 | ±0.5964 | +1.705 | 0.0881 | . |
| **High cholesterol** | **+0.7290** | 0.2680 | ±0.5360 | **+2.720** | **0.0065** | ** |
| Kidney disease | +0.8374 | 0.5979 | ±1.1957 | +1.401 | 0.1613 |  |
| **Circulatory disease** | **+0.9609** | 0.4403 | ±0.8805 | **+2.183** | **0.0291** | * |
| Avg. daily time 54-69 (%) | +0.0426 | 0.1003 | ±0.2006 | +0.424 | 0.6712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4139** | 1.0838 | ±2.1677 | **+6.841** | **7.89e-12** | *** |
| Education: graduate level (vs college) | -0.4349 | 0.2752 | ±0.5504 | -1.580 | 0.1141 |  |
| **Education: high school or below (vs college)** | **+1.3346** | 0.5889 | ±1.1778 | **+2.266** | **0.0234** | * |
| Site: UCSD (vs UAB) | -0.2284 | 0.3591 | ±0.7182 | -0.636 | 0.5247 |  |
| Site: UW (vs UAB) | +0.0064 | 0.3357 | ±0.6713 | +0.019 | 0.9849 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.216** | **5.35e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.097** | **4.18e-05** | *** |
| Hypertension | +0.5036 | 0.2982 | ±0.5963 | +1.689 | 0.0912 | . |
| **High cholesterol** | **+0.7242** | 0.2686 | ±0.5371 | **+2.697** | **0.0070** | ** |
| Kidney disease | +0.8363 | 0.5984 | ±1.1967 | +1.398 | 0.1622 |  |
| **Circulatory disease** | **+0.9609** | 0.4403 | ±0.8806 | **+2.182** | **0.0291** | * |
| Time < 70 (%) | +0.0054 | 0.0780 | ±0.1560 | +0.069 | 0.9452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.01e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.3**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3889** | 1.0797 | ±2.1593 | **+6.844** | **7.71e-12** | *** |
| Education: graduate level (vs college) | -0.4303 | 0.2753 | ±0.5506 | -1.563 | 0.1181 |  |
| **Education: high school or below (vs college)** | **+1.3456** | 0.5893 | ±1.1786 | **+2.283** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2205 | 0.3587 | ±0.7173 | -0.615 | 0.5387 |  |
| Site: UW (vs UAB) | +0.0167 | 0.3354 | ±0.6707 | +0.050 | 0.9604 |  |
| **Age (years)** | **-0.0881** | 0.0122 | ±0.0244 | **-7.216** | **5.34e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0239 | ±0.0478 | **+4.093** | **4.25e-05** | *** |
| Hypertension | +0.5079 | 0.2983 | ±0.5967 | +1.702 | 0.0887 | . |
| **High cholesterol** | **+0.7286** | 0.2681 | ±0.5362 | **+2.718** | **0.0066** | ** |
| Kidney disease | +0.8365 | 0.5980 | ±1.1961 | +1.399 | 0.1619 |  |
| **Circulatory disease** | **+0.9611** | 0.4403 | ±0.8805 | **+2.183** | **0.0290** | * |
| Avg. daily time < 70 (%) | +0.0289 | 0.0812 | ±0.1624 | +0.355 | 0.7223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0915**, F-statistic = **12.61** (p = **6.61e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.4**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7369 | 3.1673 | ±6.3345 | +1.496 | 0.1348 |  |
| Education: graduate level (vs college) | -0.4340 | 0.2744 | ±0.5488 | -1.582 | 0.1137 |  |
| **Education: high school or below (vs college)** | **+1.3641** | 0.5906 | ±1.1812 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2422 | 0.3590 | ±0.7179 | -0.675 | 0.4999 |  |
| Site: UW (vs UAB) | -0.0034 | 0.3354 | ±0.6708 | -0.010 | 0.9919 |  |
| **Age (years)** | **-0.0884** | 0.0122 | ±0.0244 | **-7.240** | **4.47e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.103** | **4.09e-05** | *** |
| Hypertension | +0.5049 | 0.2981 | ±0.5963 | +1.694 | 0.0903 | . |
| **High cholesterol** | **+0.7184** | 0.2678 | ±0.5355 | **+2.683** | **0.0073** | ** |
| Kidney disease | +0.8413 | 0.5976 | ±1.1953 | +1.408 | 0.1592 |  |
| **Circulatory disease** | **+0.9890** | 0.4412 | ±0.8825 | **+2.241** | **0.0250** | * |
| Time 54-250, pooled (%) | +0.0271 | 0.0305 | ±0.0609 | +0.891 | 0.3730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0914**, F-statistic = **12.61** (p = **6.84e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.5**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7703 | 3.3166 | ±6.6333 | +1.438 | 0.1504 |  |
| Education: graduate level (vs college) | -0.4340 | 0.2744 | ±0.5488 | -1.582 | 0.1137 |  |
| **Education: high school or below (vs college)** | **+1.3639** | 0.5907 | ±1.1814 | **+2.309** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2404 | 0.3590 | ±0.7180 | -0.670 | 0.5032 |  |
| Site: UW (vs UAB) | -0.0024 | 0.3354 | ±0.6708 | -0.007 | 0.9943 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.238** | **4.56e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0239 | ±0.0478 | **+4.106** | **4.03e-05** | *** |
| Hypertension | +0.5048 | 0.2982 | ±0.5963 | +1.693 | 0.0905 | . |
| **High cholesterol** | **+0.7191** | 0.2678 | ±0.5355 | **+2.686** | **0.0072** | ** |
| Kidney disease | +0.8404 | 0.5977 | ±1.1955 | +1.406 | 0.1598 |  |
| **Circulatory disease** | **+0.9884** | 0.4413 | ±0.8825 | **+2.240** | **0.0251** | * |
| Avg. daily time 54-250 (%) | +0.0267 | 0.0319 | ±0.0638 | +0.838 | 0.4021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1270**, R² = **0.1005**, Adj R² = **0.0926**, F-statistic = **12.77** (p = **3.12e-23**), Residual SE = **4.592** on **1258** df, AIC = **7487.8**, BIC = **7549.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4234** | 1.0762 | ±2.1524 | **+6.898** | **5.28e-12** | *** |
| Education: graduate level (vs college) | -0.4550 | 0.2755 | ±0.5509 | -1.652 | 0.0986 | . |
| **Education: high school or below (vs college)** | **+1.3328** | 0.5838 | ±1.1676 | **+2.283** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2117 | 0.3587 | ±0.7175 | -0.590 | 0.5551 |  |
| Site: UW (vs UAB) | -0.0163 | 0.3364 | ±0.6728 | -0.049 | 0.9613 |  |
| **Age (years)** | **-0.0888** | 0.0122 | ±0.0245 | **-7.260** | **3.88e-13** | *** |
| **BMI (kg/m2)** | **+0.0967** | 0.0239 | ±0.0478 | **+4.043** | **5.28e-05** | *** |
| Hypertension | +0.4697 | 0.3010 | ±0.6020 | +1.560 | 0.1186 |  |
| **High cholesterol** | **+0.6960** | 0.2682 | ±0.5363 | **+2.596** | **0.0094** | ** |
| Kidney disease | +0.7815 | 0.5995 | ±1.1989 | +1.304 | 0.1923 |  |
| **Circulatory disease** | **+0.9466** | 0.4404 | ±0.8808 | **+2.149** | **0.0316** | * |
| Time 181-250, pooled (%) | +0.0352 | 0.0303 | ±0.0607 | +1.161 | 0.2457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1270**, R² = **0.1004**, Adj R² = **0.0925**, F-statistic = **12.76** (p = **3.31e-23**), Residual SE = **4.592** on **1258** df, AIC = **7487.9**, BIC = **7549.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4248** | 1.0755 | ±2.1510 | **+6.904** | **5.07e-12** | *** |
| Education: graduate level (vs college) | -0.4551 | 0.2755 | ±0.5510 | -1.652 | 0.0986 | . |
| **Education: high school or below (vs college)** | **+1.3360** | 0.5838 | ±1.1676 | **+2.288** | **0.0221** | * |
| Site: UCSD (vs UAB) | -0.2098 | 0.3588 | ±0.7175 | -0.585 | 0.5587 |  |
| Site: UW (vs UAB) | -0.0137 | 0.3362 | ±0.6725 | -0.041 | 0.9676 |  |
| **Age (years)** | **-0.0887** | 0.0122 | ±0.0245 | **-7.255** | **4.01e-13** | *** |
| **BMI (kg/m2)** | **+0.0966** | 0.0239 | ±0.0478 | **+4.045** | **5.22e-05** | *** |
| Hypertension | +0.4710 | 0.3008 | ±0.6015 | +1.566 | 0.1173 |  |
| **High cholesterol** | **+0.6964** | 0.2683 | ±0.5366 | **+2.596** | **0.0094** | ** |
| Kidney disease | +0.7816 | 0.6000 | ±1.2000 | +1.303 | 0.1927 |  |
| **Circulatory disease** | **+0.9465** | 0.4406 | ±0.8811 | **+2.148** | **0.0317** | * |
| Avg. daily time 181-250 (%) | +0.0339 | 0.0301 | ±0.0602 | +1.127 | 0.2598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.54** (p = **9.23e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4169** | 1.0759 | ±2.1519 | **+6.893** | **5.45e-12** | *** |
| Education: graduate level (vs college) | -0.4411 | 0.2754 | ±0.5508 | -1.602 | 0.1092 |  |
| **Education: high school or below (vs college)** | **+1.3217** | 0.5874 | ±1.1748 | **+2.250** | **0.0244** | * |
| Site: UCSD (vs UAB) | -0.2246 | 0.3594 | ±0.7188 | -0.625 | 0.5321 |  |
| Site: UW (vs UAB) | +0.0002 | 0.3355 | ±0.6710 | +0.001 | 0.9996 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0245 | **-7.220** | **5.21e-13** | *** |
| **BMI (kg/m2)** | **+0.0977** | 0.0239 | ±0.0478 | **+4.085** | **4.41e-05** | *** |
| Hypertension | +0.4939 | 0.2999 | ±0.5999 | +1.647 | 0.0996 | . |
| **High cholesterol** | **+0.7172** | 0.2684 | ±0.5368 | **+2.672** | **0.0075** | ** |
| Kidney disease | +0.8220 | 0.5991 | ±1.1983 | +1.372 | 0.1701 |  |
| **Circulatory disease** | **+0.9488** | 0.4424 | ±0.8849 | **+2.144** | **0.0320** | * |
| Time > 180 (%) | +0.0084 | 0.0210 | ±0.0420 | +0.400 | 0.6891 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.54** (p = **9.26e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4181** | 1.0756 | ±2.1512 | **+6.897** | **5.32e-12** | *** |
| Education: graduate level (vs college) | -0.4413 | 0.2754 | ±0.5508 | -1.602 | 0.1091 |  |
| **Education: high school or below (vs college)** | **+1.3227** | 0.5870 | ±1.1741 | **+2.253** | **0.0242** | * |
| Site: UCSD (vs UAB) | -0.2240 | 0.3594 | ±0.7188 | -0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +0.0006 | 0.3355 | ±0.6710 | +0.002 | 0.9986 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0245 | **-7.220** | **5.21e-13** | *** |
| **BMI (kg/m2)** | **+0.0976** | 0.0239 | ±0.0478 | **+4.085** | **4.40e-05** | *** |
| Hypertension | +0.4941 | 0.2999 | ±0.5997 | +1.648 | 0.0994 | . |
| **High cholesterol** | **+0.7172** | 0.2684 | ±0.5368 | **+2.672** | **0.0075** | ** |
| Kidney disease | +0.8220 | 0.5993 | ±1.1986 | +1.372 | 0.1702 |  |
| **Circulatory disease** | **+0.9488** | 0.4425 | ±0.8849 | **+2.144** | **0.0320** | * |
| Avg. daily time > 180 (%) | +0.0083 | 0.0209 | ±0.0417 | +0.396 | 0.6918 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1270**, R² = **0.1001**, Adj R² = **0.0922**, F-statistic = **12.72** (p = **4.07e-23**), Residual SE = **4.593** on **1258** df, AIC = **7488.4**, BIC = **7550.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4463** | 1.0751 | ±2.1502 | **+6.926** | **4.32e-12** | *** |
| Education: graduate level (vs college) | -0.4381 | 0.2751 | ±0.5501 | -1.593 | 0.1112 |  |
| **Education: high school or below (vs college)** | **+1.3017** | 0.5882 | ±1.1764 | **+2.213** | **0.0269** | * |
| Site: UCSD (vs UAB) | -0.2206 | 0.3600 | ±0.7199 | -0.613 | 0.5400 |  |
| Site: UW (vs UAB) | -0.0040 | 0.3352 | ±0.6704 | -0.012 | 0.9905 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0244 | **-7.203** | **5.90e-13** | *** |
| **BMI (kg/m2)** | **+0.0957** | 0.0239 | ±0.0478 | **+4.002** | **6.28e-05** | *** |
| Hypertension | +0.4914 | 0.2998 | ±0.5996 | +1.639 | 0.1012 |  |
| **High cholesterol** | **+0.7028** | 0.2687 | ±0.5374 | **+2.615** | **0.0089** | ** |
| Kidney disease | +0.8379 | 0.5998 | ±1.1996 | +1.397 | 0.1624 |  |
| **Circulatory disease** | **+0.9491** | 0.4434 | ±0.8868 | **+2.141** | **0.0323** | * |
| Nocturnal time > 180 (%) | +0.0222 | 0.0254 | ±0.0509 | +0.873 | 0.3829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.52e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3809** | 1.0799 | ±2.1598 | **+6.835** | **8.22e-12** | *** |
| Education: graduate level (vs college) | -0.4349 | 0.2748 | ±0.5496 | -1.583 | 0.1135 |  |
| **Education: high school or below (vs college)** | **+1.3339** | 0.5847 | ±1.1693 | **+2.281** | **0.0225** | * |
| Site: UCSD (vs UAB) | -0.2267 | 0.3585 | ±0.7169 | -0.632 | 0.5271 |  |
| Site: UW (vs UAB) | +0.0023 | 0.3355 | ±0.6710 | +0.007 | 0.9946 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.227** | **4.95e-13** | *** |
| **BMI (kg/m2)** | **+0.0987** | 0.0241 | ±0.0482 | **+4.096** | **4.20e-05** | *** |
| Hypertension | +0.4930 | 0.2987 | ±0.5974 | +1.650 | 0.0988 | . |
| **High cholesterol** | **+0.7198** | 0.2680 | ±0.5360 | **+2.686** | **0.0072** | ** |
| Kidney disease | +0.8333 | 0.5971 | ±1.1942 | +1.396 | 0.1628 |  |
| **Circulatory disease** | **+0.9607** | 0.4405 | ±0.8810 | **+2.181** | **0.0292** | * |
| Any reading > 250 during wear (0/1) | +0.1666 | 0.3351 | ±0.6702 | +0.497 | 0.6191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0914**, F-statistic = **12.60** (p = **6.87e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.5**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4389** | 1.0740 | ±2.1479 | **+6.927** | **4.31e-12** | *** |
| Education: graduate level (vs college) | -0.4335 | 0.2744 | ±0.5488 | -1.580 | 0.1142 |  |
| **Education: high school or below (vs college)** | **+1.3654** | 0.5911 | ±1.1823 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2370 | 0.3589 | ±0.7177 | -0.660 | 0.5090 |  |
| Site: UW (vs UAB) | +0.0004 | 0.3353 | ±0.6705 | +0.001 | 0.9991 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.238** | **4.54e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.104** | **4.07e-05** | *** |
| Hypertension | +0.5058 | 0.2982 | ±0.5964 | +1.696 | 0.0898 | . |
| **High cholesterol** | **+0.7207** | 0.2678 | ±0.5356 | **+2.691** | **0.0071** | ** |
| Kidney disease | +0.8404 | 0.5978 | ±1.1957 | +1.406 | 0.1598 |  |
| **Circulatory disease** | **+0.9880** | 0.4412 | ±0.8823 | **+2.240** | **0.0251** | * |
| Time > 250 (%) | -0.0262 | 0.0309 | ±0.0618 | -0.848 | 0.3965 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0914**, F-statistic = **12.61** (p = **6.84e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.5**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4366** | 1.0738 | ±2.1475 | **+6.926** | **4.34e-12** | *** |
| Education: graduate level (vs college) | -0.4333 | 0.2744 | ±0.5489 | -1.579 | 0.1143 |  |
| **Education: high school or below (vs college)** | **+1.3659** | 0.5912 | ±1.1824 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2372 | 0.3589 | ±0.7178 | -0.661 | 0.5087 |  |
| Site: UW (vs UAB) | +0.0007 | 0.3352 | ±0.6705 | +0.002 | 0.9984 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.238** | **4.55e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0239 | ±0.0478 | **+4.107** | **4.02e-05** | *** |
| Hypertension | +0.5059 | 0.2982 | ±0.5964 | +1.697 | 0.0898 | . |
| **High cholesterol** | **+0.7205** | 0.2678 | ±0.5356 | **+2.690** | **0.0071** | ** |
| Kidney disease | +0.8398 | 0.5978 | ±1.1957 | +1.405 | 0.1601 |  |
| **Circulatory disease** | **+0.9886** | 0.4412 | ±0.8824 | **+2.241** | **0.0250** | * |
| Avg. daily time > 250 (%) | -0.0268 | 0.0322 | ±0.0644 | -0.832 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 1,270; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.48** (p = **4.30e-15**), AUC = **0.6934**, AIC = **1089.8**, BIC = **1146.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6455 | 0.5975 | ±1.1951 | -1.080 | 0.2800 | 0.5244 |  |
| Education: graduate level (vs college) | -0.0601 | 0.1710 | ±0.3419 | -0.351 | 0.7254 | 0.9417 |  |
| Education: high school or below (vs college) | +0.3418 | 0.2620 | ±0.5240 | +1.305 | 0.1920 | 1.4075 |  |
| Site: UCSD (vs UAB) | -0.1869 | 0.2125 | ±0.4251 | -0.879 | 0.3793 | 0.8296 |  |
| Site: UW (vs UAB) | -0.0335 | 0.1881 | ±0.3763 | -0.178 | 0.8585 | 0.9670 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.799** | **6.69e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.434** | **9.24e-06** | 1.0471 | *** |
| Hypertension | +0.2435 | 0.1729 | ±0.3458 | +1.408 | 0.1591 | 1.2757 |  |
| **High cholesterol** | **+0.4268** | 0.1644 | ±0.3288 | **+2.596** | **0.0094** | 1.5323 | ** |
| Kidney disease | +0.4740 | 0.2801 | ±0.5602 | +1.692 | 0.0906 | 1.6064 | . |
| **Circulatory disease** | **+0.5643** | 0.2216 | ±0.4433 | **+2.546** | **0.0109** | 1.7581 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0789**, LLR χ² = **91.34** (p = **9.08e-15**), AUC = **0.6938**, AIC = **1090.9**, BIC = **1152.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2567 | 0.8776 | ±1.7552 | -1.432 | 0.1521 | 0.2846 |  |
| Education: graduate level (vs college) | -0.0585 | 0.1710 | ±0.3421 | -0.342 | 0.7324 | 0.9432 |  |
| Education: high school or below (vs college) | +0.3287 | 0.2624 | ±0.5247 | +1.253 | 0.2103 | 1.3892 |  |
| Site: UCSD (vs UAB) | -0.1869 | 0.2126 | ±0.4253 | -0.879 | 0.3794 | 0.8295 |  |
| Site: UW (vs UAB) | -0.0372 | 0.1883 | ±0.3766 | -0.198 | 0.8434 | 0.9635 |  |
| **Age (years)** | **-0.0461** | 0.0079 | ±0.0158 | **-5.847** | **4.99e-09** | 0.9549 | *** |
| **BMI (kg/m2)** | **+0.0452** | 0.0104 | ±0.0208 | **+4.343** | **1.41e-05** | 1.0463 | *** |
| Hypertension | +0.2367 | 0.1731 | ±0.3461 | +1.367 | 0.1715 | 1.2670 |  |
| **High cholesterol** | **+0.4144** | 0.1650 | ±0.3299 | **+2.512** | **0.0120** | 1.5135 | * |
| Kidney disease | +0.4739 | 0.2802 | ±0.5604 | +1.691 | 0.0908 | 1.6062 | . |
| **Circulatory disease** | **+0.5536** | 0.2221 | ±0.4442 | **+2.492** | **0.0127** | 1.7395 | * |
| HbA1c (%) | +0.1199 | 0.1258 | ±0.2515 | +0.953 | 0.3404 | 1.1274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0787**, LLR χ² = **91.20** (p = **9.70e-15**), AUC = **0.6944**, AIC = **1091.1**, BIC = **1152.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9895 | 0.7198 | ±1.4395 | -1.375 | 0.1692 | 0.3717 |  |
| Education: graduate level (vs college) | -0.0674 | 0.1712 | ±0.3425 | -0.394 | 0.6939 | 0.9348 |  |
| Education: high school or below (vs college) | +0.3285 | 0.2623 | ±0.5247 | +1.252 | 0.2105 | 1.3889 |  |
| Site: UCSD (vs UAB) | -0.1857 | 0.2126 | ±0.4251 | -0.873 | 0.3824 | 0.8306 |  |
| Site: UW (vs UAB) | -0.0424 | 0.1884 | ±0.3769 | -0.225 | 0.8219 | 0.9585 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.822** | **5.83e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0457** | 0.0104 | ±0.0208 | **+4.391** | **1.13e-05** | 1.0467 | *** |
| Hypertension | +0.2344 | 0.1734 | ±0.3467 | +1.352 | 0.1764 | 1.2641 |  |
| **High cholesterol** | **+0.4178** | 0.1647 | ±0.3295 | **+2.536** | **0.0112** | 1.5186 | * |
| Kidney disease | +0.4607 | 0.2809 | ±0.5619 | +1.640 | 0.1010 | 1.5853 |  |
| **Circulatory disease** | **+0.5519** | 0.2223 | ±0.4447 | **+2.482** | **0.0131** | 1.7366 | * |
| Mean glucose (mg/dL) | +0.0032 | 0.0037 | ±0.0074 | +0.860 | 0.3897 | 1.0032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0787**, LLR χ² = **91.20** (p = **9.70e-15**), AUC = **0.6944**, AIC = **1091.1**, BIC = **1152.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4288 | 1.0901 | ±2.1801 | -1.311 | 0.1899 | 0.2396 |  |
| Education: graduate level (vs college) | -0.0674 | 0.1712 | ±0.3425 | -0.394 | 0.6939 | 0.9348 |  |
| Education: high school or below (vs college) | +0.3285 | 0.2623 | ±0.5247 | +1.252 | 0.2105 | 1.3889 |  |
| Site: UCSD (vs UAB) | -0.1857 | 0.2126 | ±0.4251 | -0.873 | 0.3824 | 0.8306 |  |
| Site: UW (vs UAB) | -0.0424 | 0.1884 | ±0.3769 | -0.225 | 0.8219 | 0.9585 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.822** | **5.83e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0457** | 0.0104 | ±0.0208 | **+4.391** | **1.13e-05** | 1.0467 | *** |
| Hypertension | +0.2344 | 0.1734 | ±0.3467 | +1.352 | 0.1764 | 1.2641 |  |
| **High cholesterol** | **+0.4178** | 0.1647 | ±0.3295 | **+2.536** | **0.0112** | 1.5186 | * |
| Kidney disease | +0.4607 | 0.2809 | ±0.5619 | +1.640 | 0.1010 | 1.5853 |  |
| **Circulatory disease** | **+0.5519** | 0.2223 | ±0.4447 | **+2.482** | **0.0131** | 1.7366 | * |
| GMI (%) | +0.1327 | 0.1543 | ±0.3086 | +0.860 | 0.3897 | 1.1419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0801**, LLR χ² = **92.72** (p = **4.87e-15**), AUC = **0.6961**, AIC = **1089.5**, BIC = **1151.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2101 | 0.7037 | ±1.4073 | -1.720 | 0.0855 | 0.2982 | . |
| Education: graduate level (vs college) | -0.0684 | 0.1712 | ±0.3424 | -0.400 | 0.6894 | 0.9339 |  |
| Education: high school or below (vs college) | +0.3158 | 0.2627 | ±0.5255 | +1.202 | 0.2293 | 1.3714 |  |
| Site: UCSD (vs UAB) | -0.1918 | 0.2126 | ±0.4253 | -0.902 | 0.3670 | 0.8254 |  |
| Site: UW (vs UAB) | -0.0488 | 0.1885 | ±0.3770 | -0.259 | 0.7955 | 0.9523 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.787** | **7.18e-09** | 0.9556 | *** |
| **BMI (kg/m2)** | **+0.0444** | 0.0104 | ±0.0209 | **+4.253** | **2.11e-05** | 1.0454 | *** |
| Hypertension | +0.2309 | 0.1733 | ±0.3466 | +1.332 | 0.1827 | 1.2597 |  |
| **High cholesterol** | **+0.4079** | 0.1650 | ±0.3300 | **+2.473** | **0.0134** | 1.5037 | * |
| Kidney disease | +0.4713 | 0.2806 | ±0.5612 | +1.680 | 0.0930 | 1.6020 | . |
| **Circulatory disease** | **+0.5513** | 0.2222 | ±0.4444 | **+2.481** | **0.0131** | 1.7354 | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0053 | 0.0034 | ±0.0069 | +1.528 | 0.1266 | 1.0053 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0783**, LLR χ² = **90.68** (p = **1.23e-14**), AUC = **0.6933**, AIC = **1091.6**, BIC = **1153.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7385 | 0.6329 | ±1.2658 | -1.167 | 0.2433 | 0.4778 |  |
| Education: graduate level (vs college) | -0.0614 | 0.1710 | ±0.3420 | -0.359 | 0.7198 | 0.9405 |  |
| Education: high school or below (vs college) | +0.3414 | 0.2620 | ±0.5240 | +1.303 | 0.1925 | 1.4069 |  |
| Site: UCSD (vs UAB) | -0.1819 | 0.2128 | ±0.4257 | -0.855 | 0.3927 | 0.8337 |  |
| Site: UW (vs UAB) | -0.0347 | 0.1882 | ±0.3764 | -0.184 | 0.8537 | 0.9659 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.813** | **6.14e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.424** | **9.67e-06** | 1.0470 | *** |
| Hypertension | +0.2372 | 0.1736 | ±0.3472 | +1.367 | 0.1718 | 1.2677 |  |
| **High cholesterol** | **+0.4262** | 0.1644 | ±0.3289 | **+2.592** | **0.0095** | 1.5315 | ** |
| Kidney disease | +0.4611 | 0.2818 | ±0.5636 | +1.636 | 0.1018 | 1.5858 |  |
| **Circulatory disease** | **+0.5587** | 0.2221 | ±0.4442 | **+2.516** | **0.0119** | 1.7485 | * |
| Glucose SD, pooled (mg/dL) | +0.0052 | 0.0116 | ±0.0233 | +0.447 | 0.6551 | 1.0052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.52** (p = **1.32e-14**), AUC = **0.6935**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6836 | 0.6290 | ±1.2580 | -1.087 | 0.2771 | 0.5048 |  |
| Education: graduate level (vs college) | -0.0608 | 0.1710 | ±0.3420 | -0.355 | 0.7224 | 0.9410 |  |
| Education: high school or below (vs college) | +0.3417 | 0.2620 | ±0.5240 | +1.304 | 0.1922 | 1.4073 |  |
| Site: UCSD (vs UAB) | -0.1849 | 0.2128 | ±0.4255 | -0.869 | 0.3847 | 0.8312 |  |
| Site: UW (vs UAB) | -0.0343 | 0.1882 | ±0.3764 | -0.182 | 0.8554 | 0.9663 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.799** | **6.69e-09** | 0.9554 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.426** | **9.61e-06** | 1.0471 | *** |
| Hypertension | +0.2409 | 0.1735 | ±0.3469 | +1.389 | 0.1649 | 1.2724 |  |
| **High cholesterol** | **+0.4264** | 0.1644 | ±0.3289 | **+2.594** | **0.0095** | 1.5318 | ** |
| Kidney disease | +0.4679 | 0.2820 | ±0.5640 | +1.659 | 0.0971 | 1.5966 | . |
| **Circulatory disease** | **+0.5619** | 0.2220 | ±0.4440 | **+2.531** | **0.0114** | 1.7539 | * |
| Avg. daily SD (mg/dL) | +0.0024 | 0.0125 | ±0.0251 | +0.194 | 0.8460 | 1.0024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.49** (p = **1.34e-14**), AUC = **0.6935**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6284 | 0.6796 | ±1.3591 | -0.925 | 0.3551 | 0.5335 |  |
| Education: graduate level (vs college) | -0.0602 | 0.1710 | ±0.3420 | -0.352 | 0.7247 | 0.9416 |  |
| Education: high school or below (vs college) | +0.3414 | 0.2621 | ±0.5242 | +1.303 | 0.1927 | 1.4069 |  |
| Site: UCSD (vs UAB) | -0.1877 | 0.2131 | ±0.4263 | -0.881 | 0.3785 | 0.8289 |  |
| Site: UW (vs UAB) | -0.0339 | 0.1882 | ±0.3765 | -0.180 | 0.8572 | 0.9667 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.784** | **7.31e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.434** | **9.27e-06** | 1.0471 | *** |
| Hypertension | +0.2441 | 0.1732 | ±0.3464 | +1.409 | 0.1588 | 1.2764 |  |
| **High cholesterol** | **+0.4264** | 0.1646 | ±0.3291 | **+2.591** | **0.0096** | 1.5317 | ** |
| Kidney disease | +0.4753 | 0.2811 | ±0.5622 | +1.691 | 0.0909 | 1.6084 | . |
| **Circulatory disease** | **+0.5645** | 0.2217 | ±0.4434 | **+2.546** | **0.0109** | 1.7585 | * |
| CV (%) | -0.0010 | 0.0195 | ±0.0390 | -0.053 | 0.9578 | 0.9990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.54** (p = **1.31e-14**), AUC = **0.6935**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5522 | 0.7197 | ±1.4395 | -0.767 | 0.4430 | 0.5757 |  |
| Education: graduate level (vs college) | -0.0591 | 0.1710 | ±0.3420 | -0.346 | 0.7295 | 0.9426 |  |
| Education: high school or below (vs college) | +0.3421 | 0.2621 | ±0.5241 | +1.305 | 0.1918 | 1.4079 |  |
| Site: UCSD (vs UAB) | -0.1833 | 0.2131 | ±0.4262 | -0.860 | 0.3897 | 0.8325 |  |
| Site: UW (vs UAB) | -0.0327 | 0.1882 | ±0.3764 | -0.174 | 0.8621 | 0.9678 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.800** | **6.62e-09** | 0.9554 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.438** | **9.09e-06** | 1.0472 | *** |
| Hypertension | +0.2408 | 0.1733 | ±0.3467 | +1.389 | 0.1647 | 1.2723 |  |
| **High cholesterol** | **+0.4280** | 0.1645 | ±0.3290 | **+2.602** | **0.0093** | 1.5343 | ** |
| Kidney disease | +0.4698 | 0.2807 | ±0.5614 | +1.674 | 0.0942 | 1.5997 | . |
| **Circulatory disease** | **+0.5637** | 0.2217 | ±0.4434 | **+2.543** | **0.0110** | 1.7572 | * |
| Mean / SD ratio | -0.0150 | 0.0643 | ±0.1287 | -0.232 | 0.8163 | 0.9852 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6940**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7626 | 0.7202 | ±1.4404 | -1.059 | 0.2897 | 0.4665 |  |
| Education: graduate level (vs college) | -0.0607 | 0.1710 | ±0.3420 | -0.355 | 0.7224 | 0.9411 |  |
| Education: high school or below (vs college) | +0.3423 | 0.2619 | ±0.5239 | +1.307 | 0.1913 | 1.4081 |  |
| Site: UCSD (vs UAB) | -0.1902 | 0.2128 | ±0.4256 | -0.894 | 0.3715 | 0.8268 |  |
| Site: UW (vs UAB) | -0.0341 | 0.1881 | ±0.3763 | -0.181 | 0.8563 | 0.9665 |  |
| **Age (years)** | **-0.0454** | 0.0079 | ±0.0157 | **-5.760** | **8.41e-09** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.437** | **9.10e-06** | 1.0472 | *** |
| Hypertension | +0.2457 | 0.1730 | ±0.3461 | +1.420 | 0.1556 | 1.2785 |  |
| **High cholesterol** | **+0.4253** | 0.1645 | ±0.3289 | **+2.586** | **0.0097** | 1.5300 | ** |
| Kidney disease | +0.4809 | 0.2811 | ±0.5621 | +1.711 | 0.0871 | 1.6175 | . |
| **Circulatory disease** | **+0.5648** | 0.2216 | ±0.4433 | **+2.548** | **0.0108** | 1.7591 | * |
| Avg. daily mean/SD | +0.0155 | 0.0532 | ±0.1065 | +0.292 | 0.7706 | 1.0156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.50** (p = **1.33e-14**), AUC = **0.6934**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7012 | 0.7146 | ±1.4293 | -0.981 | 0.3265 | 0.4960 |  |
| Education: graduate level (vs college) | -0.0597 | 0.1710 | ±0.3420 | -0.349 | 0.7269 | 0.9420 |  |
| Education: high school or below (vs college) | +0.3413 | 0.2620 | ±0.5241 | +1.302 | 0.1928 | 1.4067 |  |
| Site: UCSD (vs UAB) | -0.1846 | 0.2131 | ±0.4263 | -0.866 | 0.3865 | 0.8315 |  |
| Site: UW (vs UAB) | -0.0313 | 0.1888 | ±0.3777 | -0.166 | 0.8685 | 0.9692 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.794** | **6.87e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.432** | **9.35e-06** | 1.0471 | *** |
| Hypertension | +0.2434 | 0.1729 | ±0.3459 | +1.407 | 0.1593 | 1.2756 |  |
| **High cholesterol** | **+0.4285** | 0.1648 | ±0.3297 | **+2.599** | **0.0093** | 1.5349 | ** |
| Kidney disease | +0.4727 | 0.2802 | ±0.5605 | +1.687 | 0.0916 | 1.6044 | . |
| **Circulatory disease** | **+0.5636** | 0.2217 | ±0.4434 | **+2.542** | **0.0110** | 1.7570 | * |
| MAG (mg/dL/h) | +0.0014 | 0.0097 | ±0.0195 | +0.142 | 0.8870 | 1.0014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.49** (p = **1.34e-14**), AUC = **0.6934**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6643 | 0.6550 | ±1.3100 | -1.014 | 0.3105 | 0.5146 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1710 | ±0.3421 | -0.353 | 0.7241 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3415 | 0.2620 | ±0.5241 | +1.303 | 0.1924 | 1.4071 |  |
| Site: UCSD (vs UAB) | -0.1860 | 0.2129 | ±0.4257 | -0.874 | 0.3821 | 0.8302 |  |
| Site: UW (vs UAB) | -0.0335 | 0.1881 | ±0.3763 | -0.178 | 0.8586 | 0.9670 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.792** | **6.94e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.435** | **9.21e-06** | 1.0472 | *** |
| Hypertension | +0.2429 | 0.1732 | ±0.3464 | +1.402 | 0.1608 | 1.2749 |  |
| **High cholesterol** | **+0.4270** | 0.1644 | ±0.3289 | **+2.597** | **0.0094** | 1.5326 | ** |
| Kidney disease | +0.4722 | 0.2813 | ±0.5626 | +1.679 | 0.0932 | 1.6035 | . |
| **Circulatory disease** | **+0.5633** | 0.2221 | ±0.4441 | **+2.537** | **0.0112** | 1.7565 | * |
| Avg. daily range (mg/dL) | +0.0002 | 0.0030 | ±0.0060 | +0.070 | 0.9441 | 1.0002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0791**, LLR χ² = **91.63** (p = **8.00e-15**), AUC = **0.6928**, AIC = **1090.6**, BIC = **1152.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7738 | 0.6088 | ±1.2176 | -1.271 | 0.2037 | 0.4613 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1711 | ±0.3422 | -0.353 | 0.7240 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3445 | 0.2619 | ±0.5238 | +1.315 | 0.1884 | 1.4113 |  |
| Site: UCSD (vs UAB) | -0.1755 | 0.2129 | ±0.4258 | -0.825 | 0.4096 | 0.8390 |  |
| Site: UW (vs UAB) | -0.0340 | 0.1883 | ±0.3766 | -0.181 | 0.8567 | 0.9666 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.816** | **6.02e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0453** | 0.0104 | ±0.0208 | **+4.350** | **1.36e-05** | 1.0463 | *** |
| Hypertension | +0.2402 | 0.1732 | ±0.3463 | +1.387 | 0.1654 | 1.2715 |  |
| **High cholesterol** | **+0.4215** | 0.1645 | ±0.3291 | **+2.561** | **0.0104** | 1.5242 | * |
| Kidney disease | +0.4723 | 0.2801 | ±0.5601 | +1.686 | 0.0917 | 1.6036 | . |
| **Circulatory disease** | **+0.5601** | 0.2218 | ±0.4435 | **+2.526** | **0.0115** | 1.7509 | * |
| SD of daily means (mg/dL) | +0.0242 | 0.0223 | ±0.0445 | +1.085 | 0.2779 | 1.0245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0801**, LLR χ² = **92.72** (p = **4.88e-15**), AUC = **0.6956**, AIC = **1089.5**, BIC = **1151.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4596 | 0.9360 | ±1.8720 | +0.491 | 0.6234 | 1.5834 |  |
| Education: graduate level (vs college) | -0.0666 | 0.1713 | ±0.3426 | -0.389 | 0.6973 | 0.9356 |  |
| Education: high school or below (vs college) | +0.3327 | 0.2622 | ±0.5244 | +1.269 | 0.2044 | 1.3948 |  |
| Site: UCSD (vs UAB) | -0.1732 | 0.2130 | ±0.4259 | -0.813 | 0.4160 | 0.8410 |  |
| Site: UW (vs UAB) | -0.0317 | 0.1885 | ±0.3769 | -0.168 | 0.8665 | 0.9688 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.811** | **6.21e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.380** | **1.19e-05** | 1.0466 | *** |
| Hypertension | +0.2337 | 0.1734 | ±0.3467 | +1.348 | 0.1775 | 1.2633 |  |
| **High cholesterol** | **+0.4192** | 0.1647 | ±0.3293 | **+2.546** | **0.0109** | 1.5208 | * |
| Kidney disease | +0.4475 | 0.2816 | ±0.5632 | +1.589 | 0.1121 | 1.5644 |  |
| **Circulatory disease** | **+0.5440** | 0.2227 | ±0.4453 | **+2.443** | **0.0146** | 1.7228 | * |
| Time in range 70-180, pooled (%) | -0.0112 | 0.0073 | ±0.0146 | -1.534 | 0.1251 | 0.9888 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0800**, LLR χ² = **92.66** (p = **5.00e-15**), AUC = **0.6955**, AIC = **1089.6**, BIC = **1151.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4452 | 0.9356 | ±1.8711 | +0.476 | 0.6342 | 1.5608 |  |
| Education: graduate level (vs college) | -0.0666 | 0.1713 | ±0.3425 | -0.389 | 0.6976 | 0.9356 |  |
| Education: high school or below (vs college) | +0.3343 | 0.2621 | ±0.5242 | +1.276 | 0.2021 | 1.3970 |  |
| Site: UCSD (vs UAB) | -0.1738 | 0.2130 | ±0.4259 | -0.816 | 0.4145 | 0.8405 |  |
| Site: UW (vs UAB) | -0.0313 | 0.1884 | ±0.3769 | -0.166 | 0.8683 | 0.9692 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.814** | **6.11e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0455** | 0.0104 | ±0.0208 | **+4.378** | **1.20e-05** | 1.0466 | *** |
| Hypertension | +0.2339 | 0.1734 | ±0.3467 | +1.349 | 0.1773 | 1.2635 |  |
| **High cholesterol** | **+0.4188** | 0.1647 | ±0.3293 | **+2.543** | **0.0110** | 1.5202 | * |
| Kidney disease | +0.4476 | 0.2816 | ±0.5633 | +1.589 | 0.1120 | 1.5645 |  |
| **Circulatory disease** | **+0.5448** | 0.2226 | ±0.4452 | **+2.448** | **0.0144** | 1.7243 | * |
| Avg. daily time in range 70-180 (%) | -0.0110 | 0.0073 | ±0.0146 | -1.515 | 0.1298 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0789**, LLR χ² = **91.43** (p = **8.75e-15**), AUC = **0.6927**, AIC = **1090.8**, BIC = **1152.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7245 | 0.6030 | ±1.2059 | -1.202 | 0.2295 | 0.4846 |  |
| Education: graduate level (vs college) | -0.0514 | 0.1713 | ±0.3426 | -0.300 | 0.7640 | 0.9499 |  |
| Education: high school or below (vs college) | +0.3604 | 0.2631 | ±0.5262 | +1.370 | 0.1707 | 1.4339 |  |
| Site: UCSD (vs UAB) | -0.1600 | 0.2144 | ±0.4289 | -0.746 | 0.4556 | 0.8522 |  |
| Site: UW (vs UAB) | -0.0205 | 0.1887 | ±0.3775 | -0.108 | 0.9136 | 0.9797 |  |
| **Age (years)** | **-0.0452** | 0.0079 | ±0.0157 | **-5.750** | **8.92e-09** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.389** | **1.14e-05** | 1.0467 | *** |
| Hypertension | +0.2417 | 0.1731 | ±0.3462 | +1.396 | 0.1627 | 1.2734 |  |
| **High cholesterol** | **+0.4355** | 0.1648 | ±0.3295 | **+2.643** | **0.0082** | 1.5457 | ** |
| Kidney disease | +0.4708 | 0.2803 | ±0.5606 | +1.679 | 0.0931 | 1.6013 | . |
| **Circulatory disease** | **+0.5482** | 0.2225 | ±0.4450 | **+2.464** | **0.0138** | 1.7302 | * |
| Any reading < 54 during wear (0/1) | +0.1616 | 0.1655 | ±0.3310 | +0.976 | 0.3289 | 1.1754 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.49** (p = **1.34e-14**), AUC = **0.6936**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6420 | 0.5993 | ±1.1986 | -1.071 | 0.2840 | 0.5262 |  |
| Education: graduate level (vs college) | -0.0600 | 0.1710 | ±0.3419 | -0.351 | 0.7254 | 0.9417 |  |
| Education: high school or below (vs college) | +0.3410 | 0.2622 | ±0.5244 | +1.300 | 0.1935 | 1.4063 |  |
| Site: UCSD (vs UAB) | -0.1890 | 0.2143 | ±0.4287 | -0.882 | 0.3780 | 0.8278 |  |
| Site: UW (vs UAB) | -0.0349 | 0.1890 | ±0.3780 | -0.185 | 0.8534 | 0.9657 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.799** | **6.66e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.434** | **9.24e-06** | 1.0472 | *** |
| Hypertension | +0.2431 | 0.1730 | ±0.3460 | +1.405 | 0.1599 | 1.2752 |  |
| **High cholesterol** | **+0.4258** | 0.1650 | ±0.3299 | **+2.581** | **0.0099** | 1.5308 | ** |
| Kidney disease | +0.4745 | 0.2802 | ±0.5604 | +1.693 | 0.0904 | 1.6072 | . |
| **Circulatory disease** | **+0.5643** | 0.2216 | ±0.4433 | **+2.546** | **0.0109** | 1.7582 | * |
| Time < 54 (%) | -0.0125 | 0.1663 | ±0.3325 | -0.075 | 0.9402 | 0.9876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0784**, LLR χ² = **90.76** (p = **1.18e-14**), AUC = **0.6944**, AIC = **1091.5**, BIC = **1153.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6316 | 0.5982 | ±1.1964 | -1.056 | 0.2910 | 0.5317 |  |
| Education: graduate level (vs college) | -0.0607 | 0.1710 | ±0.3419 | -0.355 | 0.7228 | 0.9411 |  |
| Education: high school or below (vs college) | +0.3358 | 0.2621 | ±0.5242 | +1.281 | 0.2001 | 1.3991 |  |
| Site: UCSD (vs UAB) | -0.2000 | 0.2139 | ±0.4277 | -0.935 | 0.3497 | 0.8187 |  |
| Site: UW (vs UAB) | -0.0450 | 0.1893 | ±0.3785 | -0.238 | 0.8122 | 0.9560 |  |
| **Age (years)** | **-0.0455** | 0.0078 | ±0.0157 | **-5.794** | **6.88e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0463** | 0.0104 | ±0.0208 | **+4.445** | **8.79e-06** | 1.0474 | *** |
| Hypertension | +0.2389 | 0.1731 | ±0.3463 | +1.380 | 0.1677 | 1.2698 |  |
| **High cholesterol** | **+0.4211** | 0.1647 | ±0.3295 | **+2.557** | **0.0106** | 1.5237 | * |
| Kidney disease | +0.4772 | 0.2803 | ±0.5605 | +1.703 | 0.0886 | 1.6116 | . |
| **Circulatory disease** | **+0.5631** | 0.2217 | ±0.4434 | **+2.540** | **0.0111** | 1.7562 | * |
| Avg. daily time < 54 (%) | -0.1284 | 0.2593 | ±0.5185 | -0.495 | 0.6203 | 0.8795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0784**, LLR χ² = **90.79** (p = **1.17e-14**), AUC = **0.6937**, AIC = **1091.5**, BIC = **1153.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6739 | 0.5998 | ±1.1996 | -1.124 | 0.2612 | 0.5097 |  |
| Education: graduate level (vs college) | -0.0561 | 0.1712 | ±0.3424 | -0.328 | 0.7432 | 0.9455 |  |
| Education: high school or below (vs college) | +0.3513 | 0.2628 | ±0.5255 | +1.337 | 0.1812 | 1.4209 |  |
| Site: UCSD (vs UAB) | -0.1757 | 0.2136 | ±0.4272 | -0.823 | 0.4107 | 0.8389 |  |
| Site: UW (vs UAB) | -0.0233 | 0.1892 | ±0.3784 | -0.123 | 0.9022 | 0.9770 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.794** | **6.85e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.419** | **9.90e-06** | 1.0470 | *** |
| Hypertension | +0.2488 | 0.1732 | ±0.3464 | +1.436 | 0.1509 | 1.2825 |  |
| **High cholesterol** | **+0.4334** | 0.1649 | ±0.3298 | **+2.628** | **0.0086** | 1.5424 | ** |
| Kidney disease | +0.4740 | 0.2802 | ±0.5603 | +1.692 | 0.0907 | 1.6063 | . |
| **Circulatory disease** | **+0.5659** | 0.2217 | ±0.4433 | **+2.553** | **0.0107** | 1.7610 | * |
| Time 54-69, pooled (%) | +0.0288 | 0.0511 | ±0.1022 | +0.565 | 0.5724 | 1.0293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0783**, LLR χ² = **90.69** (p = **1.22e-14**), AUC = **0.6935**, AIC = **1091.6**, BIC = **1153.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6650 | 0.5992 | ±1.1983 | -1.110 | 0.2670 | 0.5143 |  |
| Education: graduate level (vs college) | -0.0565 | 0.1712 | ±0.3425 | -0.330 | 0.7413 | 0.9450 |  |
| Education: high school or below (vs college) | +0.3503 | 0.2628 | ±0.5256 | +1.333 | 0.1825 | 1.4196 |  |
| Site: UCSD (vs UAB) | -0.1795 | 0.2132 | ±0.4264 | -0.842 | 0.3998 | 0.8357 |  |
| Site: UW (vs UAB) | -0.0254 | 0.1891 | ±0.3782 | -0.134 | 0.8933 | 0.9750 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.799** | **6.68e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.422** | **9.77e-06** | 1.0470 | *** |
| Hypertension | +0.2479 | 0.1732 | ±0.3464 | +1.431 | 0.1524 | 1.2813 |  |
| **High cholesterol** | **+0.4317** | 0.1648 | ±0.3296 | **+2.619** | **0.0088** | 1.5398 | ** |
| Kidney disease | +0.4744 | 0.2801 | ±0.5603 | +1.693 | 0.0904 | 1.6070 | . |
| **Circulatory disease** | **+0.5659** | 0.2217 | ±0.4433 | **+2.553** | **0.0107** | 1.7611 | * |
| Avg. daily time 54-69 (%) | +0.0236 | 0.0512 | ±0.1024 | +0.461 | 0.6448 | 1.0239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0783**, LLR χ² = **90.67** (p = **1.23e-14**), AUC = **0.6933**, AIC = **1091.6**, BIC = **1153.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6688 | 0.6000 | ±1.2001 | -1.115 | 0.2650 | 0.5123 |  |
| Education: graduate level (vs college) | -0.0576 | 0.1711 | ±0.3423 | -0.336 | 0.7366 | 0.9441 |  |
| Education: high school or below (vs college) | +0.3491 | 0.2627 | ±0.5254 | +1.329 | 0.1839 | 1.4178 |  |
| Site: UCSD (vs UAB) | -0.1765 | 0.2140 | ±0.4279 | -0.825 | 0.4094 | 0.8382 |  |
| Site: UW (vs UAB) | -0.0248 | 0.1893 | ±0.3787 | -0.131 | 0.8956 | 0.9755 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.794** | **6.85e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.423** | **9.72e-06** | 1.0470 | *** |
| Hypertension | +0.2475 | 0.1732 | ±0.3464 | +1.429 | 0.1530 | 1.2808 |  |
| **High cholesterol** | **+0.4325** | 0.1650 | ±0.3300 | **+2.622** | **0.0088** | 1.5412 | ** |
| Kidney disease | +0.4732 | 0.2801 | ±0.5603 | +1.689 | 0.0912 | 1.6051 | . |
| **Circulatory disease** | **+0.5653** | 0.2217 | ±0.4433 | **+2.550** | **0.0108** | 1.7599 | * |
| Time < 70 (%) | +0.0184 | 0.0420 | ±0.0839 | +0.438 | 0.6617 | 1.0185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.56** (p = **1.29e-14**), AUC = **0.6934**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6576 | 0.5991 | ±1.1982 | -1.098 | 0.2723 | 0.5181 |  |
| Education: graduate level (vs college) | -0.0581 | 0.1712 | ±0.3423 | -0.339 | 0.7344 | 0.9436 |  |
| Education: high school or below (vs college) | +0.3470 | 0.2627 | ±0.5255 | +1.321 | 0.1866 | 1.4149 |  |
| Site: UCSD (vs UAB) | -0.1815 | 0.2134 | ±0.4269 | -0.850 | 0.3952 | 0.8340 |  |
| Site: UW (vs UAB) | -0.0279 | 0.1893 | ±0.3786 | -0.147 | 0.8829 | 0.9725 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.799** | **6.66e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.426** | **9.59e-06** | 1.0471 | *** |
| Hypertension | +0.2464 | 0.1732 | ±0.3464 | +1.422 | 0.1550 | 1.2794 |  |
| **High cholesterol** | **+0.4300** | 0.1648 | ±0.3297 | **+2.609** | **0.0091** | 1.5373 | ** |
| Kidney disease | +0.4738 | 0.2801 | ±0.5602 | +1.692 | 0.0907 | 1.6061 | . |
| **Circulatory disease** | **+0.5653** | 0.2217 | ±0.4433 | **+2.550** | **0.0108** | 1.7599 | * |
| Avg. daily time < 70 (%) | +0.0127 | 0.0443 | ±0.0886 | +0.287 | 0.7744 | 1.0128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6934**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2546 | 1.4514 | ±2.9029 | -0.175 | 0.8608 | 0.7752 |  |
| Education: graduate level (vs college) | -0.0603 | 0.1710 | ±0.3420 | -0.353 | 0.7241 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3381 | 0.2623 | ±0.5246 | +1.289 | 0.1973 | 1.4023 |  |
| Site: UCSD (vs UAB) | -0.1857 | 0.2126 | ±0.4251 | -0.874 | 0.3822 | 0.8305 |  |
| Site: UW (vs UAB) | -0.0328 | 0.1882 | ±0.3764 | -0.174 | 0.8617 | 0.9677 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.796** | **6.78e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.433** | **9.30e-06** | 1.0471 | *** |
| Hypertension | +0.2431 | 0.1729 | ±0.3458 | +1.406 | 0.1597 | 1.2752 |  |
| **High cholesterol** | **+0.4282** | 0.1645 | ±0.3289 | **+2.604** | **0.0092** | 1.5345 | ** |
| Kidney disease | +0.4734 | 0.2801 | ±0.5602 | +1.690 | 0.0910 | 1.6054 | . |
| **Circulatory disease** | **+0.5591** | 0.2224 | ±0.4448 | **+2.514** | **0.0119** | 1.7491 | * |
| Time 54-250, pooled (%) | -0.0039 | 0.0133 | ±0.0267 | -0.295 | 0.7677 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6934**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2394 | 1.4727 | ±2.9453 | -0.163 | 0.8709 | 0.7871 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1710 | ±0.3420 | -0.353 | 0.7240 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3378 | 0.2623 | ±0.5246 | +1.288 | 0.1978 | 1.4019 |  |
| Site: UCSD (vs UAB) | -0.1859 | 0.2125 | ±0.4251 | -0.874 | 0.3819 | 0.8304 |  |
| Site: UW (vs UAB) | -0.0328 | 0.1882 | ±0.3763 | -0.174 | 0.8615 | 0.9677 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.797** | **6.74e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.432** | **9.33e-06** | 1.0471 | *** |
| Hypertension | +0.2431 | 0.1729 | ±0.3458 | +1.406 | 0.1597 | 1.2752 |  |
| **High cholesterol** | **+0.4282** | 0.1645 | ±0.3289 | **+2.603** | **0.0092** | 1.5344 | ** |
| Kidney disease | +0.4735 | 0.2801 | ±0.5602 | +1.690 | 0.0909 | 1.6056 | . |
| **Circulatory disease** | **+0.5590** | 0.2224 | ±0.4448 | **+2.513** | **0.0120** | 1.7489 | * |
| Avg. daily time 54-250 (%) | -0.0041 | 0.0135 | ±0.0270 | -0.302 | 0.7629 | 0.9959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0813**, LLR χ² = **94.18** (p = **2.52e-15**), AUC = **0.6978**, AIC = **1088.1**, BIC = **1149.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6400 | 0.5983 | ±1.1966 | -1.070 | 0.2847 | 0.5273 |  |
| Education: graduate level (vs college) | -0.0752 | 0.1716 | ±0.3431 | -0.438 | 0.6610 | 0.9275 |  |
| Education: high school or below (vs college) | +0.3430 | 0.2622 | ±0.5244 | +1.308 | 0.1909 | 1.4092 |  |
| Site: UCSD (vs UAB) | -0.1744 | 0.2131 | ±0.4261 | -0.818 | 0.4131 | 0.8400 |  |
| Site: UW (vs UAB) | -0.0436 | 0.1887 | ±0.3774 | -0.231 | 0.8172 | 0.9573 |  |
| **Age (years)** | **-0.0460** | 0.0079 | ±0.0157 | **-5.844** | **5.09e-09** | 0.9551 | *** |
| **BMI (kg/m2)** | **+0.0453** | 0.0104 | ±0.0208 | **+4.343** | **1.40e-05** | 1.0463 | *** |
| Hypertension | +0.2231 | 0.1739 | ±0.3478 | +1.283 | 0.1994 | 1.2500 |  |
| **High cholesterol** | **+0.3983** | 0.1654 | ±0.3307 | **+2.408** | **0.0160** | 1.4893 | * |
| Kidney disease | +0.4236 | 0.2835 | ±0.5671 | +1.494 | 0.1352 | 1.5274 |  |
| **Circulatory disease** | **+0.5553** | 0.2223 | ±0.4447 | **+2.497** | **0.0125** | 1.7424 | * |
| **Time 181-250, pooled (%)** | **+0.0223** | 0.0114 | ±0.0228 | **+1.962** | **0.0497** | 1.0226 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0812**, LLR χ² = **94.10** (p = **2.61e-15**), AUC = **0.6976**, AIC = **1088.2**, BIC = **1149.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6403 | 0.5982 | ±1.1964 | -1.070 | 0.2844 | 0.5271 |  |
| Education: graduate level (vs college) | -0.0751 | 0.1716 | ±0.3431 | -0.438 | 0.6614 | 0.9276 |  |
| Education: high school or below (vs college) | +0.3458 | 0.2621 | ±0.5243 | +1.319 | 0.1870 | 1.4132 |  |
| Site: UCSD (vs UAB) | -0.1729 | 0.2131 | ±0.4261 | -0.811 | 0.4172 | 0.8412 |  |
| Site: UW (vs UAB) | -0.0419 | 0.1886 | ±0.3773 | -0.222 | 0.8242 | 0.9590 |  |
| **Age (years)** | **-0.0459** | 0.0079 | ±0.0157 | **-5.841** | **5.19e-09** | 0.9551 | *** |
| **BMI (kg/m2)** | **+0.0453** | 0.0104 | ±0.0208 | **+4.344** | **1.40e-05** | 1.0463 | *** |
| Hypertension | +0.2233 | 0.1739 | ±0.3477 | +1.285 | 0.1990 | 1.2502 |  |
| **High cholesterol** | **+0.3988** | 0.1654 | ±0.3307 | **+2.412** | **0.0159** | 1.4901 | * |
| Kidney disease | +0.4226 | 0.2836 | ±0.5672 | +1.490 | 0.1362 | 1.5259 |  |
| **Circulatory disease** | **+0.5557** | 0.2223 | ±0.4446 | **+2.500** | **0.0124** | 1.7431 | * |
| Avg. daily time 181-250 (%) | +0.0218 | 0.0112 | ±0.0224 | +1.944 | 0.0519 | 1.0221 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0799**, LLR χ² = **92.49** (p = **5.41e-15**), AUC = **0.6954**, AIC = **1089.8**, BIC = **1151.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6494 | 0.5982 | ±1.1964 | -1.086 | 0.2777 | 0.5224 |  |
| Education: graduate level (vs college) | -0.0677 | 0.1713 | ±0.3425 | -0.395 | 0.6927 | 0.9346 |  |
| Education: high school or below (vs college) | +0.3292 | 0.2622 | ±0.5244 | +1.256 | 0.2092 | 1.3899 |  |
| Site: UCSD (vs UAB) | -0.1798 | 0.2128 | ±0.4256 | -0.845 | 0.3982 | 0.8354 |  |
| Site: UW (vs UAB) | -0.0367 | 0.1884 | ±0.3768 | -0.195 | 0.8453 | 0.9639 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.813** | **6.15e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.388** | **1.14e-05** | 1.0467 | *** |
| Hypertension | +0.2320 | 0.1734 | ±0.3468 | +1.338 | 0.1809 | 1.2612 |  |
| **High cholesterol** | **+0.4163** | 0.1647 | ±0.3294 | **+2.528** | **0.0115** | 1.5164 | * |
| Kidney disease | +0.4494 | 0.2815 | ±0.5631 | +1.596 | 0.1104 | 1.5674 |  |
| **Circulatory disease** | **+0.5445** | 0.2226 | ±0.4453 | **+2.446** | **0.0145** | 1.7237 | * |
| Time > 180 (%) | +0.0106 | 0.0073 | ±0.0146 | +1.454 | 0.1459 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0799**, LLR χ² = **92.52** (p = **5.33e-15**), AUC = **0.6954**, AIC = **1089.7**, BIC = **1151.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6484 | 0.5982 | ±1.1963 | -1.084 | 0.2784 | 0.5229 |  |
| Education: graduate level (vs college) | -0.0680 | 0.1713 | ±0.3425 | -0.397 | 0.6913 | 0.9342 |  |
| Education: high school or below (vs college) | +0.3303 | 0.2621 | ±0.5243 | +1.260 | 0.2077 | 1.3914 |  |
| Site: UCSD (vs UAB) | -0.1787 | 0.2128 | ±0.4256 | -0.839 | 0.4012 | 0.8364 |  |
| Site: UW (vs UAB) | -0.0361 | 0.1884 | ±0.3768 | -0.192 | 0.8481 | 0.9646 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.813** | **6.15e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.386** | **1.15e-05** | 1.0467 | *** |
| Hypertension | +0.2319 | 0.1734 | ±0.3468 | +1.337 | 0.1812 | 1.2609 |  |
| **High cholesterol** | **+0.4164** | 0.1647 | ±0.3294 | **+2.528** | **0.0115** | 1.5165 | * |
| Kidney disease | +0.4486 | 0.2816 | ±0.5632 | +1.593 | 0.1111 | 1.5661 |  |
| **Circulatory disease** | **+0.5446** | 0.2226 | ±0.4452 | **+2.446** | **0.0144** | 1.7239 | * |
| Avg. daily time > 180 (%) | +0.0107 | 0.0073 | ±0.0146 | +1.466 | 0.1425 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0831**, LLR χ² = **96.29** (p = **9.65e-16**), AUC = **0.7006**, AIC = **1086.0**, BIC = **1147.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6243 | 0.5997 | ±1.1994 | -1.041 | 0.2979 | 0.5356 |  |
| Education: graduate level (vs college) | -0.0621 | 0.1716 | ±0.3431 | -0.362 | 0.7173 | 0.9398 |  |
| Education: high school or below (vs college) | +0.3148 | 0.2632 | ±0.5264 | +1.196 | 0.2317 | 1.3700 |  |
| Site: UCSD (vs UAB) | -0.1801 | 0.2132 | ±0.4264 | -0.845 | 0.3982 | 0.8352 |  |
| Site: UW (vs UAB) | -0.0388 | 0.1889 | ±0.3778 | -0.206 | 0.8371 | 0.9619 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0158 | **-5.785** | **7.24e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0444** | 0.0105 | ±0.0209 | **+4.247** | **2.16e-05** | 1.0454 | *** |
| Hypertension | +0.2338 | 0.1737 | ±0.3474 | +1.346 | 0.1783 | 1.2634 |  |
| **High cholesterol** | **+0.4056** | 0.1652 | ±0.3305 | **+2.455** | **0.0141** | 1.5002 | * |
| Kidney disease | +0.4787 | 0.2806 | ±0.5613 | +1.706 | 0.0880 | 1.6140 | . |
| **Circulatory disease** | **+0.5497** | 0.2230 | ±0.4459 | **+2.465** | **0.0137** | 1.7327 | * |
| **Nocturnal time > 180 (%)** | **+0.0181** | 0.0075 | ±0.0150 | **+2.414** | **0.0158** | 1.0183 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0797**, LLR χ² = **92.27** (p = **5.99e-15**), AUC = **0.6933**, AIC = **1090.0**, BIC = **1151.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6994 | 0.5996 | ±1.1993 | -1.166 | 0.2435 | 0.4969 |  |
| Education: graduate level (vs college) | -0.0595 | 0.1711 | ±0.3421 | -0.348 | 0.7279 | 0.9422 |  |
| Education: high school or below (vs college) | +0.3438 | 0.2625 | ±0.5249 | +1.310 | 0.1902 | 1.4103 |  |
| Site: UCSD (vs UAB) | -0.1816 | 0.2128 | ±0.4256 | -0.853 | 0.3934 | 0.8339 |  |
| Site: UW (vs UAB) | -0.0353 | 0.1883 | ±0.3767 | -0.188 | 0.8512 | 0.9653 |  |
| **Age (years)** | **-0.0458** | 0.0079 | ±0.0157 | **-5.825** | **5.70e-09** | 0.9552 | *** |
| **BMI (kg/m2)** | **+0.0470** | 0.0104 | ±0.0208 | **+4.513** | **6.40e-06** | 1.0481 | *** |
| Hypertension | +0.2277 | 0.1737 | ±0.3473 | +1.311 | 0.1898 | 1.2557 |  |
| **High cholesterol** | **+0.4218** | 0.1646 | ±0.3293 | **+2.562** | **0.0104** | 1.5248 | * |
| Kidney disease | +0.4619 | 0.2812 | ±0.5623 | +1.643 | 0.1004 | 1.5871 |  |
| **Circulatory disease** | **+0.5612** | 0.2221 | ±0.4442 | **+2.527** | **0.0115** | 1.7527 | * |
| Any reading > 250 during wear (0/1) | +0.2607 | 0.1927 | ±0.3854 | +1.353 | 0.1761 | 1.2978 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6933**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6472 | 0.5977 | ±1.1955 | -1.083 | 0.2789 | 0.5235 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1710 | ±0.3420 | -0.353 | 0.7241 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3377 | 0.2623 | ±0.5246 | +1.288 | 0.1979 | 1.4018 |  |
| Site: UCSD (vs UAB) | -0.1864 | 0.2125 | ±0.4251 | -0.877 | 0.3804 | 0.8299 |  |
| Site: UW (vs UAB) | -0.0332 | 0.1882 | ±0.3763 | -0.177 | 0.8598 | 0.9673 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.797** | **6.76e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.433** | **9.29e-06** | 1.0471 | *** |
| Hypertension | +0.2430 | 0.1729 | ±0.3458 | +1.405 | 0.1600 | 1.2750 |  |
| **High cholesterol** | **+0.4279** | 0.1644 | ±0.3289 | **+2.602** | **0.0093** | 1.5340 | ** |
| Kidney disease | +0.4735 | 0.2801 | ±0.5602 | +1.690 | 0.0910 | 1.6056 | . |
| **Circulatory disease** | **+0.5590** | 0.2224 | ±0.4448 | **+2.513** | **0.0120** | 1.7489 | * |
| Time > 250 (%) | +0.0040 | 0.0133 | ±0.0266 | +0.302 | 0.7623 | 1.0040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.59** (p = **1.28e-14**), AUC = **0.6933**, AIC = **1091.7**, BIC = **1153.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6469 | 0.5978 | ±1.1955 | -1.082 | 0.2791 | 0.5236 |  |
| Education: graduate level (vs college) | -0.0605 | 0.1710 | ±0.3420 | -0.354 | 0.7237 | 0.9413 |  |
| Education: high school or below (vs college) | +0.3371 | 0.2624 | ±0.5247 | +1.285 | 0.1988 | 1.4009 |  |
| Site: UCSD (vs UAB) | -0.1863 | 0.2125 | ±0.4251 | -0.876 | 0.3808 | 0.8301 |  |
| Site: UW (vs UAB) | -0.0332 | 0.1882 | ±0.3763 | -0.176 | 0.8599 | 0.9673 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.797** | **6.75e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.432** | **9.32e-06** | 1.0471 | *** |
| Hypertension | +0.2429 | 0.1729 | ±0.3458 | +1.405 | 0.1601 | 1.2749 |  |
| **High cholesterol** | **+0.4281** | 0.1644 | ±0.3289 | **+2.603** | **0.0092** | 1.5343 | ** |
| Kidney disease | +0.4736 | 0.2801 | ±0.5602 | +1.691 | 0.0909 | 1.6058 | . |
| **Circulatory disease** | **+0.5584** | 0.2224 | ±0.4449 | **+2.510** | **0.0121** | 1.7479 | * |
| Avg. daily time > 250 (%) | +0.0045 | 0.0134 | ±0.0269 | +0.335 | 0.7379 | 1.0045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
