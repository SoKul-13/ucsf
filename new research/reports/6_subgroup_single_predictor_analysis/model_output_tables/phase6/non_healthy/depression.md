# Phase 6 model output tables - All (analysis base) - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


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
