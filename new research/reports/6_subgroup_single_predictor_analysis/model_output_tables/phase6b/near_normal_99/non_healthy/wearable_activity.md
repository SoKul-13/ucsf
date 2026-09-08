# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 60; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **60**, R² = **0.1901**, Adj R² = **0.0248**, F-statistic = **1.15** (p = **0.3465**), Residual SE = **87.005** on **49** df, AIC = **716.0**, BIC = **739.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+423.8404** | 136.4190 | ±272.8380 | **+3.107** | **0.0019** | ** |
| Education: graduate level (vs college) | +23.1364 | 26.5441 | ±53.0882 | +0.872 | 0.3834 |  |
| Education: high school or below (vs college) | +8.7155 | 79.3907 | ±158.7813 | +0.110 | 0.9126 |  |
| Site: UCSD (vs UAB) | -18.9314 | 34.0278 | ±68.0556 | -0.556 | 0.5780 |  |
| Site: UW (vs UAB) | -28.2900 | 33.4531 | ±66.9062 | -0.846 | 0.3977 |  |
| Age (years) | +0.4666 | 1.8341 | ±3.6683 | +0.254 | 0.7992 |  |
| BMI (kg/m2) | -1.5097 | 2.0780 | ±4.1559 | -0.727 | 0.4675 |  |
| **Hypertension** | **-65.1387** | 30.4914 | ±60.9827 | **-2.136** | **0.0327** | * |
| High cholesterol | -1.3962 | 30.7252 | ±61.4504 | -0.045 | 0.9638 |  |
| Kidney disease | -61.2591 | 48.9994 | ±97.9988 | -1.250 | 0.2112 |  |
| Circulatory disease | +18.9777 | 28.0714 | ±56.1428 | +0.676 | 0.4990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **60**, R² = **0.1934**, Adj R² = **0.0086**, F-statistic = **1.05** (p = **0.4228**), Residual SE = **87.727** on **48** df, AIC = **717.8**, BIC = **742.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+513.7994** | 216.4196 | ±432.8393 | **+2.374** | **0.0176** | * |
| Education: graduate level (vs college) | +21.0955 | 27.2443 | ±54.4886 | +0.774 | 0.4387 |  |
| Education: high school or below (vs college) | +15.9057 | 86.3735 | ±172.7470 | +0.184 | 0.8539 |  |
| Site: UCSD (vs UAB) | -17.9457 | 34.3048 | ±68.6096 | -0.523 | 0.6009 |  |
| Site: UW (vs UAB) | -27.7203 | 33.6907 | ±67.3814 | -0.823 | 0.4106 |  |
| Age (years) | +0.4931 | 1.8386 | ±3.6773 | +0.268 | 0.7885 |  |
| BMI (kg/m2) | -1.4621 | 2.1326 | ±4.2652 | -0.686 | 0.4930 |  |
| **Hypertension** | **-63.6638** | 30.3994 | ±60.7989 | **-2.094** | **0.0362** | * |
| High cholesterol | +0.5564 | 31.0915 | ±62.1830 | +0.018 | 0.9857 |  |
| Kidney disease | -69.1465 | 55.4607 | ±110.9214 | -1.247 | 0.2125 |  |
| Circulatory disease | +18.6326 | 27.8289 | ±55.6577 | +0.670 | 0.5031 |  |
| HbA1c (%) | -16.7508 | 32.1285 | ±64.2571 | -0.521 | 0.6021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **60**, R² = **0.2520**, Adj R² = **0.0806**, F-statistic = **1.47** (p = **0.1743**), Residual SE = **84.481** on **48** df, AIC = **713.3**, BIC = **738.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+785.7917** | 303.9816 | ±607.9632 | **+2.585** | **0.0097** | ** |
| Education: graduate level (vs college) | +19.5178 | 28.6390 | ±57.2780 | +0.682 | 0.4955 |  |
| Education: high school or below (vs college) | -4.6260 | 87.0928 | ±174.1856 | -0.053 | 0.9576 |  |
| Site: UCSD (vs UAB) | -22.1790 | 32.5974 | ±65.1949 | -0.680 | 0.4963 |  |
| Site: UW (vs UAB) | -28.3720 | 34.3150 | ±68.6299 | -0.827 | 0.4083 |  |
| Age (years) | +0.6269 | 1.7643 | ±3.5286 | +0.355 | 0.7224 |  |
| BMI (kg/m2) | -1.8609 | 2.3684 | ±4.7369 | -0.786 | 0.4320 |  |
| **Hypertension** | **-65.2532** | 28.6340 | ±57.2679 | **-2.279** | **0.0227** | * |
| High cholesterol | -3.2452 | 31.0619 | ±62.1238 | -0.104 | 0.9168 |  |
| Kidney disease | -65.2507 | 53.7454 | ±107.4909 | -1.214 | 0.2247 |  |
| Circulatory disease | +30.6645 | 28.1421 | ±56.2841 | +1.090 | 0.2759 |  |
| Mean glucose (mg/dL) | -3.1133 | 2.3837 | ±4.7674 | -1.306 | 0.1915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **60**, R² = **0.2520**, Adj R² = **0.0806**, F-statistic = **1.47** (p = **0.1743**), Residual SE = **84.481** on **48** df, AIC = **713.3**, BIC = **738.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1216.6034** | 614.4585 | ±1228.9169 | **+1.980** | **0.0477** | * |
| Education: graduate level (vs college) | +19.5178 | 28.6390 | ±57.2780 | +0.682 | 0.4955 |  |
| Education: high school or below (vs college) | -4.6260 | 87.0928 | ±174.1856 | -0.053 | 0.9576 |  |
| Site: UCSD (vs UAB) | -22.1790 | 32.5974 | ±65.1949 | -0.680 | 0.4963 |  |
| Site: UW (vs UAB) | -28.3720 | 34.3150 | ±68.6299 | -0.827 | 0.4083 |  |
| Age (years) | +0.6269 | 1.7643 | ±3.5286 | +0.355 | 0.7224 |  |
| BMI (kg/m2) | -1.8609 | 2.3684 | ±4.7369 | -0.786 | 0.4320 |  |
| **Hypertension** | **-65.2532** | 28.6340 | ±57.2679 | **-2.279** | **0.0227** | * |
| High cholesterol | -3.2452 | 31.0619 | ±62.1238 | -0.104 | 0.9168 |  |
| Kidney disease | -65.2507 | 53.7454 | ±107.4909 | -1.214 | 0.2247 |  |
| Circulatory disease | +30.6645 | 28.1421 | ±56.2841 | +1.090 | 0.2759 |  |
| GMI (%) | -130.1546 | 99.6531 | ±199.3061 | -1.306 | 0.1915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **60**, R² = **0.2333**, Adj R² = **0.0575**, F-statistic = **1.33** (p = **0.2390**), Residual SE = **85.532** on **48** df, AIC = **714.8**, BIC = **739.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+641.7859** | 222.1470 | ±444.2941 | **+2.889** | **0.0039** | ** |
| Education: graduate level (vs college) | +23.0367 | 27.2675 | ±54.5350 | +0.845 | 0.3982 |  |
| Education: high school or below (vs college) | +7.4942 | 85.3972 | ±170.7943 | +0.088 | 0.9301 |  |
| Site: UCSD (vs UAB) | -18.7767 | 32.7609 | ±65.5217 | -0.573 | 0.5665 |  |
| Site: UW (vs UAB) | -26.6097 | 34.7996 | ±69.5993 | -0.765 | 0.4445 |  |
| Age (years) | +0.3379 | 1.8295 | ±3.6590 | +0.185 | 0.8535 |  |
| BMI (kg/m2) | -1.4906 | 2.1983 | ±4.3966 | -0.678 | 0.4977 |  |
| **Hypertension** | **-58.2439** | 29.3461 | ±58.6922 | **-1.985** | **0.0472** | * |
| High cholesterol | -3.2207 | 31.4474 | ±62.8948 | -0.102 | 0.9184 |  |
| Kidney disease | -80.5182 | 68.0347 | ±136.0695 | -1.183 | 0.2366 |  |
| Circulatory disease | +23.1581 | 29.5974 | ±59.1947 | +0.782 | 0.4340 |  |
| Nocturnal mean 00-06h (mg/dL) | -1.8462 | 1.4242 | ±2.8485 | -1.296 | 0.1949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **60**, R² = **0.1971**, Adj R² = **0.0131**, F-statistic = **1.07** (p = **0.4033**), Residual SE = **87.524** on **48** df, AIC = **717.5**, BIC = **742.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+455.2137** | 139.3993 | ±278.7987 | **+3.266** | **0.0011** | ** |
| Education: graduate level (vs college) | +23.3685 | 28.0042 | ±56.0084 | +0.834 | 0.4040 |  |
| Education: high school or below (vs college) | +11.0003 | 79.5148 | ±159.0296 | +0.138 | 0.8900 |  |
| Site: UCSD (vs UAB) | -15.7072 | 36.4282 | ±72.8564 | -0.431 | 0.6663 |  |
| Site: UW (vs UAB) | -29.2675 | 34.8632 | ±69.7265 | -0.839 | 0.4012 |  |
| Age (years) | +0.6046 | 2.1392 | ±4.2784 | +0.283 | 0.7774 |  |
| BMI (kg/m2) | -1.4422 | 2.1342 | ±4.2685 | -0.676 | 0.4992 |  |
| **Hypertension** | **-59.7218** | 26.9254 | ±53.8507 | **-2.218** | **0.0266** | * |
| High cholesterol | -2.1160 | 31.7583 | ±63.5166 | -0.067 | 0.9469 |  |
| Kidney disease | -50.1476 | 48.1383 | ±96.2766 | -1.042 | 0.2975 |  |
| Circulatory disease | +19.2303 | 26.4845 | ±52.9690 | +0.726 | 0.4678 |  |
| Glucose SD, pooled (mg/dL) | -2.7469 | 5.6867 | ±11.3734 | -0.483 | 0.6291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **60**, R² = **0.1978**, Adj R² = **0.0139**, F-statistic = **1.08** (p = **0.3999**), Residual SE = **87.488** on **48** df, AIC = **717.5**, BIC = **742.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+446.3504** | 136.3918 | ±272.7837 | **+3.273** | **0.0011** | ** |
| Education: graduate level (vs college) | +23.1042 | 28.2274 | ±56.4548 | +0.819 | 0.4131 |  |
| Education: high school or below (vs college) | +10.4968 | 78.2852 | ±156.5703 | +0.134 | 0.8933 |  |
| Site: UCSD (vs UAB) | -13.7558 | 38.5580 | ±77.1160 | -0.357 | 0.7213 |  |
| Site: UW (vs UAB) | -28.3086 | 34.2804 | ±68.5607 | -0.826 | 0.4089 |  |
| Age (years) | +0.7094 | 2.3130 | ±4.6259 | +0.307 | 0.7591 |  |
| BMI (kg/m2) | -1.4067 | 2.1441 | ±4.2882 | -0.656 | 0.5118 |  |
| **Hypertension** | **-59.2187** | 26.8287 | ±53.6573 | **-2.207** | **0.0273** | * |
| High cholesterol | -2.2281 | 31.9730 | ±63.9460 | -0.070 | 0.9444 |  |
| Kidney disease | -49.8222 | 50.2511 | ±100.5022 | -0.991 | 0.3215 |  |
| Circulatory disease | +17.9745 | 26.9051 | ±53.8103 | +0.668 | 0.5041 |  |
| Avg. daily SD (mg/dL) | -2.9731 | 6.0991 | ±12.1983 | -0.487 | 0.6259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **60**, R² = **0.1902**, Adj R² = **0.0046**, F-statistic = **1.02** (p = **0.4402**), Residual SE = **87.903** on **48** df, AIC = **718.0**, BIC = **743.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+420.6036** | 131.9768 | ±263.9537 | **+3.187** | **0.0014** | ** |
| Education: graduate level (vs college) | +23.0682 | 27.8015 | ±55.6031 | +0.830 | 0.4067 |  |
| Education: high school or below (vs college) | +8.3480 | 81.6065 | ±163.2130 | +0.102 | 0.9185 |  |
| Site: UCSD (vs UAB) | -19.2959 | 37.6839 | ±75.3679 | -0.512 | 0.6086 |  |
| Site: UW (vs UAB) | -28.1932 | 34.3503 | ±68.7007 | -0.821 | 0.4118 |  |
| Age (years) | +0.4551 | 2.0347 | ±4.0693 | +0.224 | 0.8230 |  |
| BMI (kg/m2) | -1.5198 | 2.1626 | ±4.3252 | -0.703 | 0.4822 |  |
| **Hypertension** | **-65.6747** | 27.9065 | ±55.8129 | **-2.353** | **0.0186** | * |
| High cholesterol | -1.3559 | 31.6546 | ±63.3092 | -0.043 | 0.9658 |  |
| Kidney disease | -62.5104 | 50.3509 | ±100.7019 | -1.241 | 0.2144 |  |
| Circulatory disease | +19.0887 | 29.9939 | ±59.9877 | +0.636 | 0.5245 |  |
| CV (%) | +0.3226 | 6.5149 | ±13.0298 | +0.050 | 0.9605 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **60**, R² = **0.1901**, Adj R² = **0.0045**, F-statistic = **1.02** (p = **0.4405**), Residual SE = **87.906** on **48** df, AIC = **718.0**, BIC = **743.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+426.7409** | 215.4782 | ±430.9564 | **+1.980** | **0.0477** | * |
| Education: graduate level (vs college) | +23.1215 | 28.0229 | ±56.0458 | +0.825 | 0.4093 |  |
| Education: high school or below (vs college) | +8.5066 | 81.5612 | ±163.1225 | +0.104 | 0.9169 |  |
| Site: UCSD (vs UAB) | -19.0875 | 36.9732 | ±73.9464 | -0.516 | 0.6057 |  |
| Site: UW (vs UAB) | -28.1989 | 34.8228 | ±69.6456 | -0.810 | 0.4181 |  |
| Age (years) | +0.4624 | 2.0175 | ±4.0350 | +0.229 | 0.8187 |  |
| BMI (kg/m2) | -1.5161 | 2.1858 | ±4.3717 | -0.694 | 0.4879 |  |
| **Hypertension** | **-65.3732** | 28.2602 | ±56.5205 | **-2.313** | **0.0207** | * |
| High cholesterol | -1.3925 | 31.4425 | ±62.8851 | -0.044 | 0.9647 |  |
| Kidney disease | -61.6796 | 48.8158 | ±97.6315 | -1.264 | 0.2064 |  |
| Circulatory disease | +19.0899 | 30.4899 | ±60.9797 | +0.626 | 0.5312 |  |
| Mean / SD ratio | -0.3193 | 12.7980 | ±25.5959 | -0.025 | 0.9801 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **60**, R² = **0.1903**, Adj R² = **0.0047**, F-statistic = **1.03** (p = **0.4395**), Residual SE = **87.896** on **48** df, AIC = **718.0**, BIC = **743.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +414.4574 | 213.2163 | ±426.4326 | +1.944 | 0.0519 | . |
| Education: graduate level (vs college) | +23.1505 | 27.9729 | ±55.9458 | +0.828 | 0.4079 |  |
| Education: high school or below (vs college) | +9.4936 | 80.5722 | ±161.1444 | +0.118 | 0.9062 |  |
| Site: UCSD (vs UAB) | -18.1678 | 38.2309 | ±76.4617 | -0.475 | 0.6346 |  |
| Site: UW (vs UAB) | -28.5146 | 34.6645 | ±69.3290 | -0.823 | 0.4107 |  |
| Age (years) | +0.4967 | 2.1257 | ±4.2514 | +0.234 | 0.8152 |  |
| BMI (kg/m2) | -1.4916 | 2.1753 | ±4.3505 | -0.686 | 0.4929 |  |
| **Hypertension** | **-64.2056** | 28.3737 | ±56.7475 | **-2.263** | **0.0236** | * |
| High cholesterol | -1.3191 | 31.2045 | ±62.4091 | -0.042 | 0.9663 |  |
| Kidney disease | -60.1986 | 49.4307 | ±98.8613 | -1.218 | 0.2233 |  |
| Circulatory disease | +18.2482 | 30.8792 | ±61.7585 | +0.591 | 0.5546 |  |
| Avg. daily mean/SD | +0.7631 | 9.0488 | ±18.0977 | +0.084 | 0.9328 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **60**, R² = **0.2460**, Adj R² = **0.0732**, F-statistic = **1.42** (p = **0.1934**), Residual SE = **84.818** on **48** df, AIC = **713.7**, BIC = **738.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+481.9203** | 143.6654 | ±287.3308 | **+3.354** | **7.95e-04** | *** |
| Education: graduate level (vs college) | +25.0193 | 26.4392 | ±52.8784 | +0.946 | 0.3440 |  |
| Education: high school or below (vs college) | +28.0884 | 85.1132 | ±170.2264 | +0.330 | 0.7414 |  |
| Site: UCSD (vs UAB) | -9.1151 | 36.0915 | ±72.1830 | -0.253 | 0.8006 |  |
| Site: UW (vs UAB) | -24.1509 | 33.9907 | ±67.9815 | -0.711 | 0.4774 |  |
| Age (years) | +1.0561 | 2.1926 | ±4.3851 | +0.482 | 0.6300 |  |
| BMI (kg/m2) | -0.6670 | 2.2625 | ±4.5251 | -0.295 | 0.7681 |  |
| **Hypertension** | **-56.7390** | 28.9257 | ±57.8514 | **-1.962** | **0.0498** | * |
| High cholesterol | -6.6456 | 32.3969 | ±64.7939 | -0.205 | 0.8375 |  |
| Kidney disease | -62.8314 | 47.2875 | ±94.5750 | -1.329 | 0.1839 |  |
| Circulatory disease | +3.8795 | 26.9850 | ±53.9701 | +0.144 | 0.8857 |  |
| MAG (mg/dL/h) | -3.7700 | 2.5460 | ±5.0921 | -1.481 | 0.1387 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **60**, R² = **0.2155**, Adj R² = **0.0357**, F-statistic = **1.20** (p = **0.3134**), Residual SE = **86.515** on **48** df, AIC = **716.1**, BIC = **741.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+481.6949** | 141.3631 | ±282.7262 | **+3.408** | **6.56e-04** | *** |
| Education: graduate level (vs college) | +22.3464 | 28.1885 | ±56.3769 | +0.793 | 0.4279 |  |
| Education: high school or below (vs college) | +17.6271 | 79.8040 | ±159.6080 | +0.221 | 0.8252 |  |
| Site: UCSD (vs UAB) | -11.5394 | 35.8083 | ±71.6167 | -0.322 | 0.7473 |  |
| Site: UW (vs UAB) | -28.0364 | 33.6403 | ±67.2805 | -0.833 | 0.4046 |  |
| Age (years) | +0.9761 | 2.3734 | ±4.7469 | +0.411 | 0.6809 |  |
| BMI (kg/m2) | -1.4102 | 2.1563 | ±4.3125 | -0.654 | 0.5131 |  |
| **Hypertension** | **-58.4868** | 27.5461 | ±55.0921 | **-2.123** | **0.0337** | * |
| High cholesterol | -2.4753 | 31.5153 | ±63.0306 | -0.079 | 0.9374 |  |
| Kidney disease | -47.3984 | 45.8435 | ±91.6870 | -1.034 | 0.3012 |  |
| Circulatory disease | +13.4029 | 26.7054 | ±53.4107 | +0.502 | 0.6158 |  |
| Avg. daily range (mg/dL) | -1.2494 | 1.3450 | ±2.6900 | -0.929 | 0.3529 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **60**, R² = **0.1901**, Adj R² = **0.0045**, F-statistic = **1.02** (p = **0.4405**), Residual SE = **87.906** on **48** df, AIC = **718.0**, BIC = **743.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.1353** | 142.1606 | ±284.3211 | **+2.991** | **0.0028** | ** |
| Education: graduate level (vs college) | +23.1250 | 27.0393 | ±54.0785 | +0.855 | 0.3924 |  |
| Education: high school or below (vs college) | +8.7877 | 83.8289 | ±167.6579 | +0.105 | 0.9165 |  |
| Site: UCSD (vs UAB) | -19.0020 | 34.4325 | ±68.8650 | -0.552 | 0.5810 |  |
| Site: UW (vs UAB) | -28.3586 | 34.0360 | ±68.0720 | -0.833 | 0.4047 |  |
| Age (years) | +0.4593 | 1.8405 | ±3.6810 | +0.250 | 0.8029 |  |
| BMI (kg/m2) | -1.5156 | 2.1195 | ±4.2390 | -0.715 | 0.4745 |  |
| **Hypertension** | **-65.0927** | 30.6035 | ±61.2070 | **-2.127** | **0.0334** | * |
| High cholesterol | -1.3566 | 31.1301 | ±62.2602 | -0.044 | 0.9652 |  |
| Kidney disease | -60.8987 | 45.3077 | ±90.6154 | -1.344 | 0.1789 |  |
| Circulatory disease | +19.1231 | 28.4616 | ±56.9233 | +0.672 | 0.5017 |  |
| SD of daily means (mg/dL) | -0.1290 | 4.6286 | ±9.2572 | -0.028 | 0.9778 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **60**, R² = **0.1901**, Adj R² = **0.0045**, F-statistic = **1.02** (p = **0.4406**), Residual SE = **87.907** on **48** df, AIC = **718.0**, BIC = **743.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +447.6113 | 4839.8169 | ±9679.6337 | +0.092 | 0.9263 |  |
| Education: graduate level (vs college) | +23.1486 | 27.7721 | ±55.5441 | +0.834 | 0.4046 |  |
| Education: high school or below (vs college) | +8.7292 | 79.8422 | ±159.6843 | +0.109 | 0.9129 |  |
| Site: UCSD (vs UAB) | -18.9364 | 34.8334 | ±69.6669 | -0.544 | 0.5867 |  |
| Site: UW (vs UAB) | -28.3054 | 33.9664 | ±67.9327 | -0.833 | 0.4047 |  |
| Age (years) | +0.4660 | 1.9698 | ±3.9396 | +0.237 | 0.8130 |  |
| BMI (kg/m2) | -1.5114 | 2.1413 | ±4.2826 | -0.706 | 0.4803 |  |
| **Hypertension** | **-65.1527** | 30.1729 | ±60.3458 | **-2.159** | **0.0308** | * |
| High cholesterol | -1.3918 | 32.2171 | ±64.4342 | -0.043 | 0.9655 |  |
| Kidney disease | -61.3610 | 52.2651 | ±104.5303 | -1.174 | 0.2404 |  |
| Circulatory disease | +19.0145 | 30.4718 | ±60.9436 | +0.624 | 0.5326 |  |
| Time in range 70-180, pooled (%) | -0.2378 | 47.9931 | ±95.9861 | -0.005 | 0.9960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **60**, R² = **0.1904**, Adj R² = **0.0048**, F-statistic = **1.03** (p = **0.4390**), Residual SE = **87.891** on **48** df, AIC = **718.0**, BIC = **743.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -78.3838 | 5450.1599 | ±10900.3199 | -0.014 | 0.9885 |  |
| Education: graduate level (vs college) | +22.7658 | 28.1753 | ±56.3506 | +0.808 | 0.4191 |  |
| Education: high school or below (vs college) | +8.6896 | 79.6494 | ±159.2988 | +0.109 | 0.9131 |  |
| Site: UCSD (vs UAB) | -18.5288 | 36.2959 | ±72.5918 | -0.510 | 0.6097 |  |
| Site: UW (vs UAB) | -27.9855 | 34.0359 | ±68.0717 | -0.822 | 0.4109 |  |
| Age (years) | +0.5176 | 2.3026 | ±4.6051 | +0.225 | 0.8221 |  |
| BMI (kg/m2) | -1.4802 | 2.1343 | ±4.2687 | -0.694 | 0.4880 |  |
| **Hypertension** | **-65.0002** | 30.8733 | ±61.7466 | **-2.105** | **0.0353** | * |
| High cholesterol | -1.4460 | 32.3520 | ±64.7040 | -0.045 | 0.9643 |  |
| Kidney disease | -59.0642 | 52.1508 | ±104.3015 | -1.133 | 0.2574 |  |
| Circulatory disease | +18.3197 | 30.5549 | ±61.1097 | +0.600 | 0.5488 |  |
| Avg. daily time in range 70-180 (%) | +5.0007 | 53.8117 | ±107.6234 | +0.093 | 0.9260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **60**, R² = **0.2341**, Adj R² = **0.0586**, F-statistic = **1.33** (p = **0.2358**), Residual SE = **85.486** on **48** df, AIC = **714.7**, BIC = **739.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+415.6572** | 127.5094 | ±255.0188 | **+3.260** | **0.0011** | ** |
| Education: graduate level (vs college) | +22.3569 | 26.7163 | ±53.4326 | +0.837 | 0.4027 |  |
| Education: high school or below (vs college) | -11.0977 | 76.4347 | ±152.8693 | -0.145 | 0.8846 |  |
| Site: UCSD (vs UAB) | -22.5314 | 32.8400 | ±65.6800 | -0.686 | 0.4927 |  |
| Site: UW (vs UAB) | -31.7081 | 33.0363 | ±66.0727 | -0.960 | 0.3372 |  |
| Age (years) | +0.6081 | 1.7962 | ±3.5925 | +0.339 | 0.7350 |  |
| BMI (kg/m2) | -1.8321 | 1.9393 | ±3.8785 | -0.945 | 0.3448 |  |
| **Hypertension** | **-69.1954** | 29.3600 | ±58.7199 | **-2.357** | **0.0184** | * |
| High cholesterol | -0.1763 | 31.4024 | ±62.8047 | -0.006 | 0.9955 |  |
| Kidney disease | -61.4795 | 50.7671 | ±101.5342 | -1.211 | 0.2259 |  |
| Circulatory disease | +26.8991 | 33.0293 | ±66.0587 | +0.814 | 0.4154 |  |
| Time 54-69, pooled (%) | +97.3783 | 64.9161 | ±129.8323 | +1.500 | 0.1336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **60**, R² = **0.2199**, Adj R² = **0.0412**, F-statistic = **1.23** (p = **0.2938**), Residual SE = **86.272** on **48** df, AIC = **715.8**, BIC = **740.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+435.5115** | 134.3744 | ±268.7488 | **+3.241** | **0.0012** | ** |
| Education: graduate level (vs college) | +22.6061 | 26.9238 | ±53.8476 | +0.840 | 0.4011 |  |
| Education: high school or below (vs college) | -6.5404 | 76.5509 | ±153.1017 | -0.085 | 0.9319 |  |
| Site: UCSD (vs UAB) | -22.5214 | 33.8409 | ±67.6819 | -0.666 | 0.5057 |  |
| Site: UW (vs UAB) | -29.1416 | 33.8635 | ±67.7270 | -0.861 | 0.3895 |  |
| Age (years) | +0.3130 | 1.8566 | ±3.7133 | +0.169 | 0.8661 |  |
| BMI (kg/m2) | -1.8196 | 2.0169 | ±4.0339 | -0.902 | 0.3670 |  |
| **Hypertension** | **-66.7464** | 30.1151 | ±60.2302 | **-2.216** | **0.0267** | * |
| High cholesterol | -2.8684 | 31.7704 | ±63.5408 | -0.090 | 0.9281 |  |
| Kidney disease | -62.8725 | 54.0577 | ±108.1153 | -1.163 | 0.2448 |  |
| Circulatory disease | +24.9534 | 34.0003 | ±68.0007 | +0.734 | 0.4630 |  |
| Avg. daily time 54-69 (%) | +84.9512 | 74.7636 | ±149.5272 | +1.136 | 0.2558 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **60**, R² = **0.2223**, Adj R² = **0.0440**, F-statistic = **1.25** (p = **0.2836**), Residual SE = **86.143** on **48** df, AIC = **715.6**, BIC = **740.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.8623** | 129.3360 | ±258.6719 | **+3.154** | **0.0016** | ** |
| Education: graduate level (vs college) | +22.4901 | 26.5569 | ±53.1138 | +0.847 | 0.3971 |  |
| Education: high school or below (vs college) | -4.2346 | 76.4161 | ±152.8322 | -0.055 | 0.9558 |  |
| Site: UCSD (vs UAB) | -19.8732 | 32.8107 | ±65.6213 | -0.606 | 0.5447 |  |
| Site: UW (vs UAB) | -30.5330 | 33.2716 | ±66.5433 | -0.918 | 0.3588 |  |
| Age (years) | +0.7219 | 1.8099 | ±3.6198 | +0.399 | 0.6900 |  |
| BMI (kg/m2) | -1.8242 | 1.9657 | ±3.9314 | -0.928 | 0.3534 |  |
| **Hypertension** | **-69.0119** | 29.7061 | ±59.4122 | **-2.323** | **0.0202** | * |
| High cholesterol | +0.8143 | 31.2237 | ±62.4474 | +0.026 | 0.9792 |  |
| Kidney disease | -61.4471 | 49.5500 | ±99.1000 | -1.240 | 0.2149 |  |
| Circulatory disease | +26.0301 | 31.1036 | ±62.2073 | +0.837 | 0.4027 |  |
| Time < 70 (%) | +73.4956 | 53.9454 | ±107.8907 | +1.362 | 0.1731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **60**, R² = **0.2149**, Adj R² = **0.0350**, F-statistic = **1.19** (p = **0.3162**), Residual SE = **86.549** on **48** df, AIC = **716.2**, BIC = **741.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+431.9799** | 134.5623 | ±269.1246 | **+3.210** | **0.0013** | ** |
| Education: graduate level (vs college) | +23.6037 | 26.7642 | ±53.5284 | +0.882 | 0.3778 |  |
| Education: high school or below (vs college) | -3.3968 | 76.5128 | ±153.0255 | -0.044 | 0.9646 |  |
| Site: UCSD (vs UAB) | -22.2590 | 34.0729 | ±68.1459 | -0.653 | 0.5136 |  |
| Site: UW (vs UAB) | -29.8289 | 33.8499 | ±67.6999 | -0.881 | 0.3782 |  |
| Age (years) | +0.3618 | 1.8495 | ±3.6989 | +0.196 | 0.8449 |  |
| BMI (kg/m2) | -1.7743 | 2.0254 | ±4.0508 | -0.876 | 0.3810 |  |
| **Hypertension** | **-66.7816** | 30.2265 | ±60.4530 | **-2.209** | **0.0271** | * |
| High cholesterol | -3.5588 | 31.4937 | ±62.9874 | -0.113 | 0.9100 |  |
| Kidney disease | -62.4072 | 53.5482 | ±107.0965 | -1.165 | 0.2438 |  |
| Circulatory disease | +24.7514 | 32.9655 | ±65.9309 | +0.751 | 0.4528 |  |
| Avg. daily time < 70 (%) | +74.1210 | 67.9240 | ±135.8479 | +1.091 | 0.2752 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **60**, R² = **0.1922**, Adj R² = **0.0070**, F-statistic = **1.04** (p = **0.4294**), Residual SE = **87.793** on **48** df, AIC = **717.9**, BIC = **743.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -5521.2638 | 11683.9598 | ±23367.9196 | -0.473 | 0.6365 |  |
| Education: graduate level (vs college) | +23.5832 | 26.4856 | ±52.9713 | +0.890 | 0.3732 |  |
| Education: high school or below (vs college) | +7.0632 | 80.4232 | ±160.8463 | +0.088 | 0.9300 |  |
| Site: UCSD (vs UAB) | -20.9855 | 35.3340 | ±70.6679 | -0.594 | 0.5526 |  |
| Site: UW (vs UAB) | -29.5039 | 33.9888 | ±67.9777 | -0.868 | 0.3854 |  |
| Age (years) | +0.3298 | 1.8825 | ±3.7650 | +0.175 | 0.8609 |  |
| BMI (kg/m2) | -1.4806 | 2.1147 | ±4.2295 | -0.700 | 0.4838 |  |
| **Hypertension** | **-65.0020** | 30.8220 | ±61.6441 | **-2.109** | **0.0349** | * |
| High cholesterol | -2.9123 | 31.1523 | ±62.3047 | -0.093 | 0.9255 |  |
| Kidney disease | -60.7183 | 49.9420 | ±99.8840 | -1.216 | 0.2241 |  |
| Circulatory disease | +18.1261 | 28.1068 | ±56.2136 | +0.645 | 0.5190 |  |
| Time 54-250, pooled (%) | +59.5600 | 117.2991 | ±234.5983 | +0.508 | 0.6116 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **60**, R² = **0.2036**, Adj R² = **0.0211**, F-statistic = **1.12** (p = **0.3704**), Residual SE = **87.171** on **48** df, AIC = **717.0**, BIC = **742.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -33689.2734 | 31827.9371 | ±63655.8742 | -1.058 | 0.2898 |  |
| Education: graduate level (vs college) | +21.3630 | 27.1355 | ±54.2710 | +0.787 | 0.4311 |  |
| Education: high school or below (vs college) | +3.0161 | 81.1526 | ±162.3052 | +0.037 | 0.9704 |  |
| Site: UCSD (vs UAB) | -21.8959 | 34.4959 | ±68.9918 | -0.635 | 0.5256 |  |
| Site: UW (vs UAB) | -30.5325 | 34.0358 | ±68.0715 | -0.897 | 0.3697 |  |
| Age (years) | +0.2286 | 1.8317 | ±3.6635 | +0.125 | 0.9007 |  |
| BMI (kg/m2) | -1.7155 | 2.1754 | ±4.3508 | -0.789 | 0.4303 |  |
| **Hypertension** | **-67.3027** | 30.8993 | ±61.7986 | **-2.178** | **0.0294** | * |
| High cholesterol | -0.3078 | 30.9789 | ±61.9578 | -0.010 | 0.9921 |  |
| Kidney disease | -59.1695 | 49.7879 | ±99.5758 | -1.188 | 0.2347 |  |
| Circulatory disease | +16.5154 | 27.8956 | ±55.7913 | +0.592 | 0.5538 |  |
| Avg. daily time 54-250 (%) | +341.4105 | 318.8332 | ±637.6664 | +1.071 | 0.2843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **60**, R² = **0.2127**, Adj R² = **0.0323**, F-statistic = **1.18** (p = **0.3263**), Residual SE = **86.670** on **48** df, AIC = **716.3**, BIC = **741.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+411.5957** | 145.5927 | ±291.1854 | **+2.827** | **0.0047** | ** |
| Education: graduate level (vs college) | +19.4829 | 28.3143 | ±56.6286 | +0.688 | 0.4914 |  |
| Education: high school or below (vs college) | -4.0591 | 79.2248 | ±158.4497 | -0.051 | 0.9591 |  |
| Site: UCSD (vs UAB) | -17.9146 | 33.6909 | ±67.3818 | -0.532 | 0.5949 |  |
| Site: UW (vs UAB) | -25.5544 | 32.6426 | ±65.2852 | -0.783 | 0.4337 |  |
| Age (years) | +0.8133 | 2.1756 | ±4.3512 | +0.374 | 0.7085 |  |
| BMI (kg/m2) | -1.3265 | 2.0875 | ±4.1749 | -0.635 | 0.5251 |  |
| **Hypertension** | **-64.3288** | 30.0919 | ±60.1839 | **-2.138** | **0.0325** | * |
| High cholesterol | -0.3315 | 30.4744 | ±60.9487 | -0.011 | 0.9913 |  |
| Kidney disease | -38.4503 | 50.0569 | ±100.1138 | -0.768 | 0.4424 |  |
| Circulatory disease | +15.7544 | 26.9692 | ±53.9385 | +0.584 | 0.5591 |  |
| Time 181-250, pooled (%) | -54.6878 | 56.6965 | ±113.3929 | -0.965 | 0.3348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **60**, R² = **0.2082**, Adj R² = **0.0268**, F-statistic = **1.15** (p = **0.3476**), Residual SE = **86.916** on **48** df, AIC = **716.7**, BIC = **741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.4923** | 150.0891 | ±300.1782 | **+2.702** | **0.0069** | ** |
| Education: graduate level (vs college) | +19.4562 | 28.6700 | ±57.3399 | +0.679 | 0.4974 |  |
| Education: high school or below (vs college) | +0.4857 | 78.3904 | ±156.7808 | +0.006 | 0.9951 |  |
| Site: UCSD (vs UAB) | -16.6339 | 34.1725 | ±68.3451 | -0.487 | 0.6264 |  |
| Site: UW (vs UAB) | -25.4778 | 32.3994 | ±64.7988 | -0.786 | 0.4317 |  |
| Age (years) | +0.9117 | 2.3430 | ±4.6860 | +0.389 | 0.6972 |  |
| BMI (kg/m2) | -1.3701 | 2.0991 | ±4.1982 | -0.653 | 0.5140 |  |
| **Hypertension** | **-64.3982** | 30.2158 | ±60.4317 | **-2.131** | **0.0331** | * |
| High cholesterol | -2.8892 | 31.8083 | ±63.6167 | -0.091 | 0.9276 |  |
| Kidney disease | -40.9965 | 49.0449 | ±98.0897 | -0.836 | 0.4032 |  |
| Circulatory disease | +16.3322 | 27.7868 | ±55.5737 | +0.588 | 0.5567 |  |
| Avg. daily time 181-250 (%) | -48.9680 | 61.5727 | ±123.1455 | -0.795 | 0.4264 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **60**, R² = **0.2143**, Adj R² = **0.0342**, F-statistic = **1.19** (p = **0.3191**), Residual SE = **86.584** on **48** df, AIC = **716.2**, BIC = **741.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+414.1454** | 144.4602 | ±288.9205 | **+2.867** | **0.0041** | ** |
| Education: graduate level (vs college) | +19.7952 | 28.1698 | ±56.3396 | +0.703 | 0.4822 |  |
| Education: high school or below (vs college) | -4.2987 | 79.3029 | ±158.6058 | -0.054 | 0.9568 |  |
| Site: UCSD (vs UAB) | -18.4722 | 33.5452 | ±67.0903 | -0.551 | 0.5819 |  |
| Site: UW (vs UAB) | -26.3872 | 32.5737 | ±65.1474 | -0.810 | 0.4179 |  |
| Age (years) | +0.8037 | 2.1584 | ±4.3168 | +0.372 | 0.7096 |  |
| BMI (kg/m2) | -1.3501 | 2.0876 | ±4.1752 | -0.647 | 0.5178 |  |
| **Hypertension** | **-64.8014** | 30.2700 | ±60.5401 | **-2.141** | **0.0323** | * |
| High cholesterol | -0.7533 | 30.5723 | ±61.1447 | -0.025 | 0.9803 |  |
| Kidney disease | -37.5813 | 50.4834 | ±100.9668 | -0.744 | 0.4566 |  |
| Circulatory disease | +15.7180 | 26.8296 | ±53.6592 | +0.586 | 0.5580 |  |
| Time > 180 (%) | -55.5999 | 55.4680 | ±110.9359 | -1.002 | 0.3162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 60)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **60**, R² = **0.2097**, Adj R² = **0.0286**, F-statistic = **1.16** (p = **0.3406**), Residual SE = **86.836** on **48** df, AIC = **716.6**, BIC = **741.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.8902** | 148.1204 | ±296.2407 | **+2.754** | **0.0059** | ** |
| Education: graduate level (vs college) | +19.7615 | 28.4785 | ±56.9571 | +0.694 | 0.4877 |  |
| Education: high school or below (vs college) | +0.3241 | 78.4360 | ±156.8720 | +0.004 | 0.9967 |  |
| Site: UCSD (vs UAB) | -17.1594 | 33.9115 | ±67.8231 | -0.506 | 0.6129 |  |
| Site: UW (vs UAB) | -26.2928 | 32.3592 | ±64.7184 | -0.813 | 0.4165 |  |
| Age (years) | +0.9039 | 2.3122 | ±4.6244 | +0.391 | 0.6958 |  |
| BMI (kg/m2) | -1.3939 | 2.0987 | ±4.1974 | -0.664 | 0.5066 |  |
| **Hypertension** | **-64.8627** | 30.4549 | ±60.9099 | **-2.130** | **0.0332** | * |
| High cholesterol | -3.3449 | 31.9640 | ±63.9281 | -0.105 | 0.9167 |  |
| Kidney disease | -40.1836 | 49.3627 | ±98.7254 | -0.814 | 0.4156 |  |
| Circulatory disease | +16.3057 | 27.6365 | ±55.2730 | +0.590 | 0.5552 |  |
| Avg. daily time > 180 (%) | -49.7750 | 59.5612 | ±119.1223 | -0.836 | 0.4033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 24 single-predictor tests; 0 with raw p < 0.05 (about 1 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Total sleep time per night (min)** (n = 60): best single predictor out of sample is **%54-69 (pooled)** (CV R² -0.939 vs -1.100 for covariates alone, gain +0.161; +19.5 per SD, p = 0.134). No glycaemic measure is associated with this outcome (all p > 0.05).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.161, via %54-69 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** HbA1c (0 FDR-significant / 0 raw-significant of 1); CGM level (0 FDR-significant / 0 raw-significant of 3); CGM variability (0 FDR-significant / 0 raw-significant of 8).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Total sleep time per night (Mean glucose, ΔAIC -4.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
