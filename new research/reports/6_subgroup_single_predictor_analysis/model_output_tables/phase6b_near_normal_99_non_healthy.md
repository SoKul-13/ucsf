# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Non-healthy group (T2D non-insulin + T2D insulin)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 61; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **61**, R² = **0.1977**, Adj R² = **0.0372**, F-statistic = **1.23** (p = **0.2944**), Residual SE = **2.913** on **50** df, AIC = **313.4**, BIC = **336.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.1339** | 4.7642 | ±9.5284 | **+6.745** | **1.53e-11** | *** |
| Education: graduate level (vs college) | +0.2097 | 0.9348 | ±1.8697 | +0.224 | 0.8225 |  |
| Education: high school or below (vs college) | -2.4861 | 2.0900 | ±4.1801 | -1.190 | 0.2342 |  |
| Site: UCSD (vs UAB) | -0.2549 | 0.9730 | ±1.9459 | -0.262 | 0.7933 |  |
| Site: UW (vs UAB) | -0.3957 | 1.2226 | ±2.4451 | -0.324 | 0.7462 |  |
| Age (years) | -0.0498 | 0.0611 | ±0.1222 | -0.816 | 0.4144 |  |
| BMI (kg/m2) | -0.0560 | 0.0724 | ±0.1447 | -0.775 | 0.4386 |  |
| Hypertension | -1.1236 | 0.8642 | ±1.7283 | -1.300 | 0.1935 |  |
| High cholesterol | -0.4749 | 0.9300 | ±1.8599 | -0.511 | 0.6096 |  |
| Kidney disease | -0.9956 | 2.4563 | ±4.9125 | -0.405 | 0.6852 |  |
| Circulatory disease | -0.0641 | 1.4376 | ±2.8752 | -0.045 | 0.9644 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **61**, R² = **0.2137**, Adj R² = **0.0372**, F-statistic = **1.21** (p = **0.3053**), Residual SE = **2.913** on **49** df, AIC = **314.2**, BIC = **339.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.8456** | 8.0453 | ±16.0906 | **+3.213** | **0.0013** | ** |
| Education: graduate level (vs college) | +0.3583 | 0.9841 | ±1.9682 | +0.364 | 0.7158 |  |
| Education: high school or below (vs college) | -3.1166 | 2.2580 | ±4.5161 | -1.380 | 0.1675 |  |
| Site: UCSD (vs UAB) | -0.3356 | 0.9968 | ±1.9936 | -0.337 | 0.7364 |  |
| Site: UW (vs UAB) | -0.5085 | 1.3066 | ±2.6132 | -0.389 | 0.6971 |  |
| Age (years) | -0.0526 | 0.0600 | ±0.1201 | -0.876 | 0.3813 |  |
| BMI (kg/m2) | -0.0604 | 0.0747 | ±0.1495 | -0.808 | 0.4190 |  |
| Hypertension | -1.2391 | 0.9180 | ±1.8361 | -1.350 | 0.1771 |  |
| High cholesterol | -0.5525 | 0.9217 | ±1.8434 | -0.599 | 0.5489 |  |
| Kidney disease | -0.7250 | 2.3623 | ±4.7246 | -0.307 | 0.7589 |  |
| Circulatory disease | -0.0968 | 1.4927 | ±2.9853 | -0.065 | 0.9483 |  |
| HbA1c (%) | +1.1868 | 1.1688 | ±2.3377 | +1.015 | 0.3099 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **61**, R² = **0.2259**, Adj R² = **0.0522**, F-statistic = **1.30** (p = **0.2528**), Residual SE = **2.890** on **49** df, AIC = **313.2**, BIC = **338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.3492** | 7.6359 | ±15.2717 | **+5.284** | **1.26e-07** | *** |
| Education: graduate level (vs college) | +0.1253 | 0.9365 | ±1.8731 | +0.134 | 0.8935 |  |
| Education: high school or below (vs college) | -2.7338 | 2.1955 | ±4.3910 | -1.245 | 0.2131 |  |
| Site: UCSD (vs UAB) | -0.3239 | 0.9800 | ±1.9599 | -0.331 | 0.7410 |  |
| Site: UW (vs UAB) | -0.3637 | 1.1925 | ±2.3850 | -0.305 | 0.7604 |  |
| Age (years) | -0.0458 | 0.0620 | ±0.1240 | -0.739 | 0.4599 |  |
| BMI (kg/m2) | -0.0636 | 0.0724 | ±0.1447 | -0.879 | 0.3796 |  |
| Hypertension | -1.1211 | 0.8523 | ±1.7047 | -1.315 | 0.1884 |  |
| High cholesterol | -0.5455 | 0.9529 | ±1.9058 | -0.572 | 0.5670 |  |
| Kidney disease | -0.9517 | 2.8951 | ±5.7901 | -0.329 | 0.7424 |  |
| Circulatory disease | +0.2292 | 1.4621 | ±2.9241 | +0.157 | 0.8754 |  |
| Mean glucose (mg/dL) | -0.0710 | 0.0538 | ±0.1076 | -1.320 | 0.1868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **61**, R² = **0.2259**, Adj R² = **0.0522**, F-statistic = **1.30** (p = **0.2528**), Residual SE = **2.890** on **49** df, AIC = **313.2**, BIC = **338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1749** | 14.2403 | ±28.4807 | **+3.523** | **4.26e-04** | *** |
| Education: graduate level (vs college) | +0.1253 | 0.9365 | ±1.8731 | +0.134 | 0.8935 |  |
| Education: high school or below (vs college) | -2.7338 | 2.1955 | ±4.3910 | -1.245 | 0.2131 |  |
| Site: UCSD (vs UAB) | -0.3239 | 0.9800 | ±1.9599 | -0.331 | 0.7410 |  |
| Site: UW (vs UAB) | -0.3637 | 1.1925 | ±2.3850 | -0.305 | 0.7604 |  |
| Age (years) | -0.0458 | 0.0620 | ±0.1240 | -0.739 | 0.4599 |  |
| BMI (kg/m2) | -0.0636 | 0.0724 | ±0.1447 | -0.879 | 0.3796 |  |
| Hypertension | -1.1211 | 0.8523 | ±1.7047 | -1.315 | 0.1884 |  |
| High cholesterol | -0.5455 | 0.9529 | ±1.9058 | -0.572 | 0.5670 |  |
| Kidney disease | -0.9517 | 2.8951 | ±5.7901 | -0.329 | 0.7424 |  |
| Circulatory disease | +0.2292 | 1.4621 | ±2.9241 | +0.157 | 0.8754 |  |
| GMI (%) | -2.9685 | 2.2484 | ±4.4969 | -1.320 | 0.1868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **61**, R² = **0.2364**, Adj R² = **0.0649**, F-statistic = **1.38** (p = **0.2129**), Residual SE = **2.871** on **49** df, AIC = **312.4**, BIC = **337.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.9555** | 7.6253 | ±15.2507 | **+5.109** | **3.24e-07** | *** |
| Education: graduate level (vs college) | +0.2031 | 0.9119 | ±1.8238 | +0.223 | 0.8238 |  |
| Education: high school or below (vs college) | -2.4186 | 2.4002 | ±4.8004 | -1.008 | 0.3136 |  |
| Site: UCSD (vs UAB) | -0.2405 | 1.0144 | ±2.0288 | -0.237 | 0.8126 |  |
| Site: UW (vs UAB) | -0.2789 | 1.2218 | ±2.4436 | -0.228 | 0.8194 |  |
| Age (years) | -0.0532 | 0.0605 | ±0.1210 | -0.879 | 0.3795 |  |
| BMI (kg/m2) | -0.0546 | 0.0744 | ±0.1487 | -0.734 | 0.4631 |  |
| Hypertension | -0.8958 | 0.8717 | ±1.7434 | -1.028 | 0.3041 |  |
| High cholesterol | -0.5860 | 0.9412 | ±1.8825 | -0.623 | 0.5336 |  |
| Kidney disease | -1.3520 | 3.5483 | ±7.0965 | -0.381 | 0.7032 |  |
| Circulatory disease | +0.1183 | 1.5203 | ±3.0407 | +0.078 | 0.9380 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0584 | 0.0430 | ±0.0860 | -1.358 | 0.1745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2037**, Adj R² = **0.0249**, F-statistic = **1.14** (p = **0.3529**), Residual SE = **2.932** on **49** df, AIC = **315.0**, BIC = **340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.1274** | 5.3833 | ±10.7665 | **+6.154** | **7.56e-10** | *** |
| Education: graduate level (vs college) | +0.2177 | 0.9751 | ±1.9503 | +0.223 | 0.8234 |  |
| Education: high school or below (vs college) | -2.4351 | 1.9962 | ±3.9923 | -1.220 | 0.2225 |  |
| Site: UCSD (vs UAB) | -0.1561 | 1.0654 | ±2.1309 | -0.146 | 0.8835 |  |
| Site: UW (vs UAB) | -0.4384 | 1.2272 | ±2.4544 | -0.357 | 0.7209 |  |
| Age (years) | -0.0457 | 0.0622 | ±0.1244 | -0.734 | 0.4627 |  |
| BMI (kg/m2) | -0.0541 | 0.0740 | ±0.1480 | -0.731 | 0.4647 |  |
| Hypertension | -0.9564 | 0.8997 | ±1.7995 | -1.063 | 0.2878 |  |
| High cholesterol | -0.4872 | 0.9269 | ±1.8539 | -0.526 | 0.5992 |  |
| Kidney disease | -0.6971 | 2.5754 | ±5.1507 | -0.271 | 0.7866 |  |
| Circulatory disease | -0.0658 | 1.4233 | ±2.8466 | -0.046 | 0.9631 |  |
| Glucose SD, pooled (mg/dL) | -0.0857 | 0.1695 | ±0.3391 | -0.506 | 0.6131 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **61**, R² = **0.1985**, Adj R² = **0.0185**, F-statistic = **1.10** (p = **0.3790**), Residual SE = **2.941** on **49** df, AIC = **315.4**, BIC = **340.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.8864** | 5.2415 | ±10.4831 | **+6.083** | **1.18e-09** | *** |
| Education: graduate level (vs college) | +0.2099 | 0.9647 | ±1.9294 | +0.218 | 0.8278 |  |
| Education: high school or below (vs college) | -2.4984 | 2.1203 | ±4.2407 | -1.178 | 0.2387 |  |
| Site: UCSD (vs UAB) | -0.3101 | 1.1008 | ±2.2016 | -0.282 | 0.7782 |  |
| Site: UW (vs UAB) | -0.3914 | 1.2549 | ±2.5097 | -0.312 | 0.7551 |  |
| Age (years) | -0.0524 | 0.0613 | ±0.1227 | -0.855 | 0.3927 |  |
| BMI (kg/m2) | -0.0571 | 0.0749 | ±0.1499 | -0.762 | 0.4461 |  |
| Hypertension | -1.1868 | 0.9588 | ±1.9176 | -1.238 | 0.2158 |  |
| High cholesterol | -0.4694 | 0.9547 | ±1.9094 | -0.492 | 0.6229 |  |
| Kidney disease | -1.1023 | 2.6088 | ±5.2176 | -0.423 | 0.6726 |  |
| Circulatory disease | -0.0500 | 1.5136 | ±3.0271 | -0.033 | 0.9736 |  |
| Avg. daily SD (mg/dL) | +0.0320 | 0.1867 | ±0.3735 | +0.172 | 0.8637 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **61**, R² = **0.1985**, Adj R² = **0.0185**, F-statistic = **1.10** (p = **0.3791**), Residual SE = **2.941** on **49** df, AIC = **315.4**, BIC = **340.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.4979** | 5.5395 | ±11.0791 | **+5.867** | **4.45e-09** | *** |
| Education: graduate level (vs college) | +0.2176 | 0.9746 | ±1.9493 | +0.223 | 0.8233 |  |
| Education: high school or below (vs college) | -2.4571 | 2.0711 | ±4.1421 | -1.186 | 0.2355 |  |
| Site: UCSD (vs UAB) | -0.2158 | 1.0702 | ±2.1404 | -0.202 | 0.8402 |  |
| Site: UW (vs UAB) | -0.4132 | 1.2425 | ±2.4850 | -0.333 | 0.7395 |  |
| Age (years) | -0.0487 | 0.0632 | ±0.1265 | -0.770 | 0.4416 |  |
| BMI (kg/m2) | -0.0550 | 0.0742 | ±0.1485 | -0.741 | 0.4586 |  |
| Hypertension | -1.0657 | 0.8848 | ±1.7695 | -1.205 | 0.2284 |  |
| High cholesterol | -0.4736 | 0.9469 | ±1.8939 | -0.500 | 0.6170 |  |
| Kidney disease | -0.8850 | 2.6193 | ±5.2387 | -0.338 | 0.7355 |  |
| Circulatory disease | -0.0817 | 1.4804 | ±2.9608 | -0.055 | 0.9560 |  |
| CV (%) | -0.0355 | 0.2077 | ±0.4154 | -0.171 | 0.8644 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **61**, R² = **0.1979**, Adj R² = **0.0179**, F-statistic = **1.10** (p = **0.3818**), Residual SE = **2.942** on **49** df, AIC = **315.4**, BIC = **340.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.7869** | 6.0075 | ±12.0149 | **+5.291** | **1.21e-07** | *** |
| Education: graduate level (vs college) | +0.2116 | 0.9730 | ±1.9460 | +0.218 | 0.8278 |  |
| Education: high school or below (vs college) | -2.4640 | 2.0838 | ±4.1675 | -1.182 | 0.2370 |  |
| Site: UCSD (vs UAB) | -0.2364 | 1.0491 | ±2.0983 | -0.225 | 0.8218 |  |
| Site: UW (vs UAB) | -0.4085 | 1.2423 | ±2.4847 | -0.329 | 0.7423 |  |
| Age (years) | -0.0494 | 0.0637 | ±0.1274 | -0.775 | 0.4384 |  |
| BMI (kg/m2) | -0.0553 | 0.0745 | ±0.1489 | -0.743 | 0.4577 |  |
| Hypertension | -1.0957 | 0.8734 | ±1.7468 | -1.255 | 0.2096 |  |
| High cholesterol | -0.4738 | 0.9484 | ±1.8968 | -0.500 | 0.6173 |  |
| Kidney disease | -0.9521 | 2.5589 | ±5.1178 | -0.372 | 0.7098 |  |
| Circulatory disease | -0.0790 | 1.4951 | ±2.9902 | -0.053 | 0.9579 |  |
| Mean / SD ratio | +0.0384 | 0.3970 | ±0.7939 | +0.097 | 0.9229 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2023**, Adj R² = **0.0232**, F-statistic = **1.13** (p = **0.3597**), Residual SE = **2.934** on **49** df, AIC = **315.1**, BIC = **340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.6464** | 5.8243 | ±11.6486 | **+5.777** | **7.61e-09** | *** |
| Education: graduate level (vs college) | +0.2071 | 0.9485 | ±1.8969 | +0.218 | 0.8271 |  |
| Education: high school or below (vs college) | -2.6025 | 2.1484 | ±4.2968 | -1.211 | 0.2258 |  |
| Site: UCSD (vs UAB) | -0.3777 | 1.0479 | ±2.0958 | -0.360 | 0.7186 |  |
| Site: UW (vs UAB) | -0.3535 | 1.2401 | ±2.4801 | -0.285 | 0.7756 |  |
| Age (years) | -0.0547 | 0.0624 | ±0.1248 | -0.876 | 0.3811 |  |
| BMI (kg/m2) | -0.0589 | 0.0748 | ±0.1496 | -0.787 | 0.4310 |  |
| Hypertension | -1.2738 | 0.9216 | ±1.8433 | -1.382 | 0.1669 |  |
| High cholesterol | -0.4922 | 0.9731 | ±1.9462 | -0.506 | 0.6130 |  |
| Kidney disease | -1.1443 | 2.6135 | ±5.2269 | -0.438 | 0.6615 |  |
| Circulatory disease | +0.0586 | 1.5720 | ±3.1441 | +0.037 | 0.9703 |  |
| Avg. daily mean/SD | -0.1236 | 0.2932 | ±0.5864 | -0.421 | 0.6734 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **61**, R² = **0.1994**, Adj R² = **0.0197**, F-statistic = **1.11** (p = **0.3741**), Residual SE = **2.939** on **49** df, AIC = **315.3**, BIC = **340.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.4918** | 5.1809 | ±10.3618 | **+6.271** | **3.58e-10** | *** |
| Education: graduate level (vs college) | +0.2215 | 0.9556 | ±1.9111 | +0.232 | 0.8167 |  |
| Education: high school or below (vs college) | -2.3905 | 2.0628 | ±4.1257 | -1.159 | 0.2465 |  |
| Site: UCSD (vs UAB) | -0.1984 | 1.0129 | ±2.0259 | -0.196 | 0.8447 |  |
| Site: UW (vs UAB) | -0.3827 | 1.2451 | ±2.4903 | -0.307 | 0.7586 |  |
| Age (years) | -0.0465 | 0.0597 | ±0.1194 | -0.778 | 0.4363 |  |
| BMI (kg/m2) | -0.0512 | 0.0791 | ±0.1582 | -0.647 | 0.5174 |  |
| Hypertension | -1.0756 | 0.9032 | ±1.8064 | -1.191 | 0.2337 |  |
| High cholesterol | -0.4964 | 0.9268 | ±1.8535 | -0.536 | 0.5922 |  |
| Kidney disease | -1.0507 | 2.5007 | ±5.0013 | -0.420 | 0.6744 |  |
| Circulatory disease | -0.1627 | 1.5513 | ±3.1026 | -0.105 | 0.9165 |  |
| MAG (mg/dL/h) | -0.0223 | 0.0796 | ±0.1593 | -0.281 | 0.7790 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **61**, R² = **0.2052**, Adj R² = **0.0268**, F-statistic = **1.15** (p = **0.3452**), Residual SE = **2.929** on **49** df, AIC = **314.8**, BIC = **340.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.0476** | 5.3532 | ±10.7065 | **+5.800** | **6.64e-09** | *** |
| Education: graduate level (vs college) | +0.2227 | 0.9490 | ±1.8979 | +0.235 | 0.8145 |  |
| Education: high school or below (vs college) | -2.6052 | 2.1141 | ±4.2282 | -1.232 | 0.2178 |  |
| Site: UCSD (vs UAB) | -0.3859 | 1.0596 | ±2.1192 | -0.364 | 0.7157 |  |
| Site: UW (vs UAB) | -0.3742 | 1.2574 | ±2.5148 | -0.298 | 0.7660 |  |
| Age (years) | -0.0588 | 0.0618 | ±0.1236 | -0.952 | 0.3410 |  |
| BMI (kg/m2) | -0.0575 | 0.0741 | ±0.1483 | -0.776 | 0.4379 |  |
| Hypertension | -1.2411 | 0.9517 | ±1.9034 | -1.304 | 0.1922 |  |
| High cholesterol | -0.4771 | 0.9765 | ±1.9530 | -0.489 | 0.6251 |  |
| Kidney disease | -1.1446 | 2.4890 | ±4.9780 | -0.460 | 0.6456 |  |
| Circulatory disease | +0.0582 | 1.5086 | ±3.0171 | +0.039 | 0.9692 |  |
| Avg. daily range (mg/dL) | +0.0228 | 0.0421 | ±0.0842 | +0.541 | 0.5883 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **61**, R² = **0.2094**, Adj R² = **0.0319**, F-statistic = **1.18** (p = **0.3255**), Residual SE = **2.921** on **49** df, AIC = **314.5**, BIC = **339.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.5398** | 5.4462 | ±10.8925 | **+6.158** | **7.35e-10** | *** |
| Education: graduate level (vs college) | +0.1977 | 0.9820 | ±1.9641 | +0.201 | 0.8405 |  |
| Education: high school or below (vs college) | -2.4174 | 1.9477 | ±3.8953 | -1.241 | 0.2145 |  |
| Site: UCSD (vs UAB) | -0.3320 | 0.9645 | ±1.9289 | -0.344 | 0.7306 |  |
| Site: UW (vs UAB) | -0.4754 | 1.2088 | ±2.4177 | -0.393 | 0.6941 |  |
| Age (years) | -0.0578 | 0.0642 | ±0.1284 | -0.901 | 0.3675 |  |
| BMI (kg/m2) | -0.0625 | 0.0759 | ±0.1519 | -0.823 | 0.4103 |  |
| Hypertension | -1.0747 | 0.8582 | ±1.7165 | -1.252 | 0.2105 |  |
| High cholesterol | -0.4274 | 0.9304 | ±1.8608 | -0.459 | 0.6459 |  |
| Kidney disease | -0.6284 | 2.6982 | ±5.3965 | -0.233 | 0.8159 |  |
| Circulatory disease | +0.0886 | 1.4205 | ±2.8409 | +0.062 | 0.9502 |  |
| SD of daily means (mg/dL) | -0.1394 | 0.1922 | ±0.3845 | -0.725 | 0.4684 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **61**, R² = **0.2016**, Adj R² = **0.0224**, F-statistic = **1.12** (p = **0.3632**), Residual SE = **2.935** on **49** df, AIC = **315.1**, BIC = **340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -28.0044 | 128.5614 | ±257.1228 | -0.218 | 0.8276 |  |
| Education: graduate level (vs college) | +0.1805 | 0.9653 | ±1.9306 | +0.187 | 0.8517 |  |
| Education: high school or below (vs college) | -2.5697 | 2.1057 | ±4.2113 | -1.220 | 0.2223 |  |
| Site: UCSD (vs UAB) | -0.2466 | 0.9947 | ±1.9895 | -0.248 | 0.8042 |  |
| Site: UW (vs UAB) | -0.3859 | 1.2339 | ±2.4678 | -0.313 | 0.7545 |  |
| Age (years) | -0.0486 | 0.0623 | ±0.1245 | -0.781 | 0.4348 |  |
| BMI (kg/m2) | -0.0521 | 0.0727 | ±0.1454 | -0.717 | 0.4734 |  |
| Hypertension | -1.0927 | 0.8654 | ±1.7307 | -1.263 | 0.2067 |  |
| High cholesterol | -0.4616 | 0.9326 | ±1.8651 | -0.495 | 0.6206 |  |
| Kidney disease | -0.8538 | 2.4669 | ±4.9338 | -0.346 | 0.7293 |  |
| Circulatory disease | -0.1802 | 1.4848 | ±2.9695 | -0.121 | 0.9034 |  |
| Time in range 70-180, pooled (%) | +0.6020 | 1.2864 | ±2.5727 | +0.468 | 0.6398 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **61**, R² = **0.2183**, Adj R² = **0.0428**, F-statistic = **1.24** (p = **0.2848**), Residual SE = **2.905** on **49** df, AIC = **313.8**, BIC = **339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +170.1062 | 130.4670 | ±260.9340 | +1.304 | 0.1923 |  |
| Education: graduate level (vs college) | +0.3080 | 0.9489 | ±1.8978 | +0.325 | 0.7455 |  |
| Education: high school or below (vs college) | -2.3713 | 2.1175 | ±4.2350 | -1.120 | 0.2628 |  |
| Site: UCSD (vs UAB) | -0.3559 | 1.0286 | ±2.0572 | -0.346 | 0.7293 |  |
| Site: UW (vs UAB) | -0.4149 | 1.2900 | ±2.5799 | -0.322 | 0.7477 |  |
| Age (years) | -0.0631 | 0.0632 | ±0.1264 | -0.999 | 0.3179 |  |
| BMI (kg/m2) | -0.0633 | 0.0735 | ±0.1470 | -0.861 | 0.3893 |  |
| Hypertension | -1.1519 | 0.9172 | ±1.8345 | -1.256 | 0.2092 |  |
| High cholesterol | -0.5153 | 1.0195 | ±2.0390 | -0.505 | 0.6132 |  |
| Kidney disease | -1.3421 | 2.5049 | ±5.0098 | -0.536 | 0.5921 |  |
| Circulatory disease | +0.1676 | 1.3932 | ±2.7863 | +0.120 | 0.9042 |  |
| Avg. daily time in range 70-180 (%) | -1.3746 | 1.3011 | ±2.6022 | -1.056 | 0.2907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **61**, R² = **0.2067**, Adj R² = **0.0286**, F-statistic = **1.16** (p = **0.3382**), Residual SE = **2.926** on **49** df, AIC = **314.7**, BIC = **340.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9749** | 4.8797 | ±9.7594 | **+6.553** | **5.65e-11** | *** |
| Education: graduate level (vs college) | +0.1963 | 0.9290 | ±1.8581 | +0.211 | 0.8327 |  |
| Education: high school or below (vs college) | -2.7355 | 2.1132 | ±4.2263 | -1.295 | 0.1955 |  |
| Site: UCSD (vs UAB) | -0.3048 | 0.9583 | ±1.9165 | -0.318 | 0.7504 |  |
| Site: UW (vs UAB) | -0.4173 | 1.2153 | ±2.4306 | -0.343 | 0.7313 |  |
| Age (years) | -0.0474 | 0.0636 | ±0.1273 | -0.744 | 0.4567 |  |
| BMI (kg/m2) | -0.0605 | 0.0734 | ±0.1467 | -0.825 | 0.4095 |  |
| Hypertension | -1.1804 | 0.9079 | ±1.8158 | -1.300 | 0.1936 |  |
| High cholesterol | -0.4817 | 0.9748 | ±1.9497 | -0.494 | 0.6212 |  |
| Kidney disease | -0.8793 | 2.4639 | ±4.9278 | -0.357 | 0.7212 |  |
| Circulatory disease | +0.0794 | 1.3754 | ±2.7508 | +0.058 | 0.9540 |  |
| Time 54-69, pooled (%) | +1.4722 | 2.1703 | ±4.3406 | +0.678 | 0.4975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **61**, R² = **0.2173**, Adj R² = **0.0416**, F-statistic = **1.24** (p = **0.2893**), Residual SE = **2.906** on **49** df, AIC = **313.9**, BIC = **339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.4045** | 4.7848 | ±9.5696 | **+6.772** | **1.27e-11** | *** |
| Education: graduate level (vs college) | +0.1931 | 0.9172 | ±1.8344 | +0.211 | 0.8332 |  |
| Education: high school or below (vs college) | -2.8345 | 2.0124 | ±4.0249 | -1.408 | 0.1590 |  |
| Site: UCSD (vs UAB) | -0.3466 | 0.9536 | ±1.9071 | -0.363 | 0.7163 |  |
| Site: UW (vs UAB) | -0.3790 | 1.2075 | ±2.4151 | -0.314 | 0.7536 |  |
| Age (years) | -0.0536 | 0.0641 | ±0.1282 | -0.836 | 0.4032 |  |
| BMI (kg/m2) | -0.0639 | 0.0716 | ±0.1432 | -0.893 | 0.3719 |  |
| Hypertension | -1.1613 | 0.8976 | ±1.7951 | -1.294 | 0.1957 |  |
| High cholesterol | -0.5483 | 0.9823 | ±1.9645 | -0.558 | 0.5767 |  |
| Kidney disease | -0.8810 | 2.3288 | ±4.6575 | -0.378 | 0.7052 |  |
| Circulatory disease | +0.1298 | 1.3276 | ±2.6552 | +0.098 | 0.9221 |  |
| Avg. daily time 54-69 (%) | +2.3100 | 1.9364 | ±3.8728 | +1.193 | 0.2329 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **61**, R² = **0.2010**, Adj R² = **0.0216**, F-statistic = **1.12** (p = **0.3663**), Residual SE = **2.937** on **49** df, AIC = **315.2**, BIC = **340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9430** | 4.8904 | ±9.7808 | **+6.532** | **6.50e-11** | *** |
| Education: graduate level (vs college) | +0.2019 | 0.9371 | ±1.8741 | +0.215 | 0.8294 |  |
| Education: high school or below (vs college) | -2.5962 | 2.1270 | ±4.2540 | -1.221 | 0.2222 |  |
| Site: UCSD (vs UAB) | -0.2624 | 0.9774 | ±1.9548 | -0.268 | 0.7883 |  |
| Site: UW (vs UAB) | -0.4027 | 1.2292 | ±2.4585 | -0.328 | 0.7432 |  |
| Age (years) | -0.0469 | 0.0627 | ±0.1255 | -0.748 | 0.4546 |  |
| BMI (kg/m2) | -0.0592 | 0.0736 | ±0.1472 | -0.804 | 0.4213 |  |
| Hypertension | -1.1625 | 0.8969 | ±1.7938 | -1.296 | 0.1949 |  |
| High cholesterol | -0.4655 | 0.9593 | ±1.9186 | -0.485 | 0.6275 |  |
| Kidney disease | -0.9298 | 2.4908 | ±4.9815 | -0.373 | 0.7089 |  |
| Circulatory disease | +0.0248 | 1.4081 | ±2.8163 | +0.018 | 0.9860 |  |
| Time < 70 (%) | +0.7862 | 1.8860 | ±3.7719 | +0.417 | 0.6768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **61**, R² = **0.2193**, Adj R² = **0.0440**, F-statistic = **1.25** (p = **0.2806**), Residual SE = **2.903** on **49** df, AIC = **313.8**, BIC = **339.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.3441** | 4.8054 | ±9.6107 | **+6.731** | **1.69e-11** | *** |
| Education: graduate level (vs college) | +0.2223 | 0.9132 | ±1.8264 | +0.243 | 0.8077 |  |
| Education: high school or below (vs college) | -2.8019 | 1.9995 | ±3.9990 | -1.401 | 0.1611 |  |
| Site: UCSD (vs UAB) | -0.3535 | 0.9559 | ±1.9117 | -0.370 | 0.7115 |  |
| Site: UW (vs UAB) | -0.4056 | 1.1976 | ±2.3953 | -0.339 | 0.7348 |  |
| Age (years) | -0.0527 | 0.0645 | ±0.1290 | -0.817 | 0.4141 |  |
| BMI (kg/m2) | -0.0638 | 0.0720 | ±0.1440 | -0.886 | 0.3755 |  |
| Hypertension | -1.1693 | 0.9036 | ±1.8073 | -1.294 | 0.1956 |  |
| High cholesterol | -0.5748 | 0.9852 | ±1.9704 | -0.583 | 0.5596 |  |
| Kidney disease | -0.8791 | 2.3125 | ±4.6250 | -0.380 | 0.7038 |  |
| Circulatory disease | +0.1471 | 1.3292 | ±2.6584 | +0.111 | 0.9119 |  |
| Avg. daily time < 70 (%) | +2.3239 | 2.0008 | ±4.0016 | +1.161 | 0.2454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.2138**, Adj R² = **0.0374**, F-statistic = **1.21** (p = **0.3047**), Residual SE = **2.913** on **49** df, AIC = **314.2**, BIC = **339.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -529.4310 | 1072.2432 | ±2144.4864 | -0.494 | 0.6215 |  |
| Education: graduate level (vs college) | +0.2522 | 0.9458 | ±1.8916 | +0.267 | 0.7897 |  |
| Education: high school or below (vs college) | -2.6512 | 2.1210 | ±4.2421 | -1.250 | 0.2113 |  |
| Site: UCSD (vs UAB) | -0.4497 | 1.0357 | ±2.0714 | -0.434 | 0.6641 |  |
| Site: UW (vs UAB) | -0.5157 | 1.2803 | ±2.5605 | -0.403 | 0.6871 |  |
| Age (years) | -0.0628 | 0.0608 | ±0.1216 | -1.033 | 0.3014 |  |
| BMI (kg/m2) | -0.0534 | 0.0728 | ±0.1455 | -0.733 | 0.4633 |  |
| Hypertension | -1.1115 | 0.8683 | ±1.7366 | -1.280 | 0.2005 |  |
| High cholesterol | -0.6136 | 0.8984 | ±1.7968 | -0.683 | 0.4946 |  |
| Kidney disease | -0.9658 | 2.4011 | ±4.8021 | -0.402 | 0.6875 |  |
| Circulatory disease | -0.1488 | 1.4341 | ±2.8682 | -0.104 | 0.9174 |  |
| Time 54-250, pooled (%) | +5.6260 | 10.7338 | ±21.4676 | +0.524 | 0.6002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.1982**, Adj R² = **0.0182**, F-statistic = **1.10** (p = **0.3805**), Residual SE = **2.942** on **49** df, AIC = **315.4**, BIC = **340.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -186.4662 | 2193.4304 | ±4386.8609 | -0.085 | 0.9323 |  |
| Education: graduate level (vs college) | +0.1982 | 1.0120 | ±2.0241 | +0.196 | 0.8447 |  |
| Education: high school or below (vs college) | -2.5188 | 2.1084 | ±4.2168 | -1.195 | 0.2322 |  |
| Site: UCSD (vs UAB) | -0.2735 | 1.0298 | ±2.0596 | -0.266 | 0.7905 |  |
| Site: UW (vs UAB) | -0.4077 | 1.3991 | ±2.7982 | -0.291 | 0.7707 |  |
| Age (years) | -0.0513 | 0.0612 | ±0.1224 | -0.839 | 0.4013 |  |
| BMI (kg/m2) | -0.0573 | 0.0729 | ±0.1458 | -0.786 | 0.4317 |  |
| Hypertension | -1.1372 | 0.9338 | ±1.8675 | -1.218 | 0.2233 |  |
| High cholesterol | -0.4699 | 1.0036 | ±2.0072 | -0.468 | 0.6396 |  |
| Kidney disease | -0.9729 | 2.4776 | ±4.9553 | -0.393 | 0.6946 |  |
| Circulatory disease | -0.0780 | 1.4489 | ±2.8979 | -0.054 | 0.9570 |  |
| Avg. daily time 54-250 (%) | +2.1878 | 21.9355 | ±43.8710 | +0.100 | 0.9206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **61**, R² = **0.2117**, Adj R² = **0.0347**, F-statistic = **1.20** (p = **0.3147**), Residual SE = **2.917** on **49** df, AIC = **314.4**, BIC = **339.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.8583** | 4.8964 | ±9.7928 | **+6.506** | **7.69e-11** | *** |
| Education: graduate level (vs college) | +0.1160 | 0.9702 | ±1.9405 | +0.120 | 0.9048 |  |
| Education: high school or below (vs college) | -2.8863 | 2.0857 | ±4.1715 | -1.384 | 0.1664 |  |
| Site: UCSD (vs UAB) | -0.2340 | 0.9941 | ±1.9882 | -0.235 | 0.8139 |  |
| Site: UW (vs UAB) | -0.3628 | 1.2130 | ±2.4260 | -0.299 | 0.7649 |  |
| Age (years) | -0.0412 | 0.0640 | ±0.1279 | -0.644 | 0.5195 |  |
| BMI (kg/m2) | -0.0518 | 0.0732 | ±0.1464 | -0.707 | 0.4795 |  |
| Hypertension | -1.1083 | 0.8679 | ±1.7358 | -1.277 | 0.2016 |  |
| High cholesterol | -0.4143 | 0.9271 | ±1.8542 | -0.447 | 0.6549 |  |
| Kidney disease | -0.5518 | 2.4770 | ±4.9540 | -0.223 | 0.8237 |  |
| Circulatory disease | -0.1794 | 1.4474 | ±2.8949 | -0.124 | 0.9014 |  |
| Time 181-250, pooled (%) | -1.4351 | 1.8860 | ±3.7719 | -0.761 | 0.4467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **61**, R² = **0.2043**, Adj R² = **0.0257**, F-statistic = **1.14** (p = **0.3497**), Residual SE = **2.930** on **49** df, AIC = **314.9**, BIC = **340.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.4668** | 5.0242 | ±10.0484 | **+6.462** | **1.03e-10** | *** |
| Education: graduate level (vs college) | +0.2820 | 0.9714 | ±1.9428 | +0.290 | 0.7716 |  |
| Education: high school or below (vs college) | -2.2703 | 2.3324 | ±4.6649 | -0.973 | 0.3304 |  |
| Site: UCSD (vs UAB) | -0.2965 | 1.0407 | ±2.0815 | -0.285 | 0.7757 |  |
| Site: UW (vs UAB) | -0.4219 | 1.2982 | ±2.5964 | -0.325 | 0.7452 |  |
| Age (years) | -0.0584 | 0.0627 | ±0.1253 | -0.932 | 0.3511 |  |
| BMI (kg/m2) | -0.0584 | 0.0744 | ±0.1489 | -0.785 | 0.4325 |  |
| Hypertension | -1.1339 | 0.9008 | ±1.8016 | -1.259 | 0.2081 |  |
| High cholesterol | -0.4703 | 0.9667 | ±1.9334 | -0.486 | 0.6266 |  |
| Kidney disease | -1.2821 | 2.6325 | ±5.2651 | -0.487 | 0.6262 |  |
| Circulatory disease | +0.0129 | 1.4769 | ±2.9537 | +0.009 | 0.9930 |  |
| Avg. daily time 181-250 (%) | +0.9835 | 1.6286 | ±3.2573 | +0.604 | 0.5459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **61**, R² = **0.2140**, Adj R² = **0.0375**, F-statistic = **1.21** (p = **0.3042**), Residual SE = **2.913** on **49** df, AIC = **314.2**, BIC = **339.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9162** | 4.8828 | ±9.7655 | **+6.536** | **6.30e-11** | *** |
| Education: graduate level (vs college) | +0.1204 | 0.9672 | ±1.9345 | +0.124 | 0.9009 |  |
| Education: high school or below (vs college) | -2.9112 | 2.0715 | ±4.1429 | -1.405 | 0.1599 |  |
| Site: UCSD (vs UAB) | -0.2484 | 0.9817 | ±1.9633 | -0.253 | 0.8002 |  |
| Site: UW (vs UAB) | -0.3844 | 1.2023 | ±2.4046 | -0.320 | 0.7492 |  |
| Age (years) | -0.0411 | 0.0639 | ±0.1278 | -0.643 | 0.5202 |  |
| BMI (kg/m2) | -0.0522 | 0.0731 | ±0.1462 | -0.714 | 0.4751 |  |
| Hypertension | -1.1206 | 0.8670 | ±1.7339 | -1.293 | 0.1962 |  |
| High cholesterol | -0.4230 | 0.9217 | ±1.8434 | -0.459 | 0.6463 |  |
| Kidney disease | -0.5091 | 2.4647 | ±4.9295 | -0.207 | 0.8364 |  |
| Circulatory disease | -0.1857 | 1.4460 | ±2.8921 | -0.128 | 0.8978 |  |
| Time > 180 (%) | -1.5243 | 1.8500 | ±3.7001 | -0.824 | 0.4100 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 61)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **61**, R² = **0.2023**, Adj R² = **0.0232**, F-statistic = **1.13** (p = **0.3599**), Residual SE = **2.934** on **49** df, AIC = **315.1**, BIC = **340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.3616** | 5.0643 | ±10.1286 | **+6.390** | **1.66e-10** | *** |
| Education: graduate level (vs college) | +0.2626 | 0.9765 | ±1.9531 | +0.269 | 0.7880 |  |
| Education: high school or below (vs college) | -2.3106 | 2.3045 | ±4.6090 | -1.003 | 0.3160 |  |
| Site: UCSD (vs UAB) | -0.2797 | 1.0409 | ±2.0819 | -0.269 | 0.7881 |  |
| Site: UW (vs UAB) | -0.4034 | 1.3019 | ±2.6038 | -0.310 | 0.7566 |  |
| Age (years) | -0.0566 | 0.0631 | ±0.1262 | -0.897 | 0.3697 |  |
| BMI (kg/m2) | -0.0576 | 0.0745 | ±0.1491 | -0.772 | 0.4399 |  |
| Hypertension | -1.1244 | 0.9045 | ±1.8089 | -1.243 | 0.2138 |  |
| High cholesterol | -0.4640 | 0.9639 | ±1.9278 | -0.481 | 0.6302 |  |
| Kidney disease | -1.2373 | 2.6124 | ±5.2247 | -0.474 | 0.6358 |  |
| Circulatory disease | -0.0020 | 1.4750 | ±2.9500 | -0.001 | 0.9989 |  |
| Avg. daily time > 180 (%) | +0.7997 | 1.6590 | ±3.3179 | +0.482 | 0.6297 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 61; logistic regression)

#### Reference: covariates only
_could not be fitted (LinAlgError)_

#### HbA1c (%)
_could not be fitted (LinAlgError)_

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2453**, LLR χ² = **19.26** (p = **0.0565**), AUC = **0.7738**, AIC = **83.3**, BIC = **108.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -10.8463 | 6.9233 | ±13.8466 | -1.567 | 0.1172 | 0.0000 |  |
| Education: graduate level (vs college) | +0.5189 | 0.7391 | ±1.4782 | +0.702 | 0.4826 | 1.6802 |  |
| Education: high school or below (vs college) | +30.9865 | 1036747.2111 | ±2073494.4223 | +0.000 | 1.0000 | 28658982201553.7930 |  |
| Site: UCSD (vs UAB) | -0.0165 | 0.8401 | ±1.6801 | -0.020 | 0.9844 | 0.9837 |  |
| Site: UW (vs UAB) | -0.3148 | 0.9122 | ±1.8244 | -0.345 | 0.7300 | 0.7299 |  |
| Age (years) | -0.0060 | 0.0361 | ±0.0723 | -0.165 | 0.8690 | 0.9941 |  |
| BMI (kg/m2) | +0.0606 | 0.0586 | ±0.1172 | +1.034 | 0.3013 | 1.0625 |  |
| Hypertension | +0.7039 | 0.7600 | ±1.5200 | +0.926 | 0.3544 | 2.0216 |  |
| High cholesterol | +0.1209 | 0.7341 | ±1.4682 | +0.165 | 0.8692 | 1.1285 |  |
| Kidney disease | +26.9454 | 252838.0725 | ±505676.1450 | +0.000 | 0.9999 | 503784987496.5881 |  |
| Circulatory disease | -1.4563 | 1.2344 | ±2.4689 | -1.180 | 0.2381 | 0.2331 |  |
| Mean glucose (mg/dL) | +0.0672 | 0.0494 | ±0.0989 | +1.360 | 0.1738 | 1.0695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2453**, LLR χ² = **19.26** (p = **0.0565**), AUC = **0.7738**, AIC = **83.3**, BIC = **108.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -20.1502 | 13.3556 | ±26.7113 | -1.509 | 0.1314 | 0.0000 |  |
| Education: graduate level (vs college) | +0.5189 | 0.7391 | ±1.4782 | +0.702 | 0.4826 | 1.6802 |  |
| Education: high school or below (vs college) | +29.9992 | 632792.8155 | ±1265585.6310 | +0.000 | 1.0000 | 10677601430687.9844 |  |
| Site: UCSD (vs UAB) | -0.0165 | 0.8401 | ±1.6801 | -0.020 | 0.9844 | 0.9837 |  |
| Site: UW (vs UAB) | -0.3148 | 0.9122 | ±1.8244 | -0.345 | 0.7300 | 0.7299 |  |
| Age (years) | -0.0060 | 0.0361 | ±0.0723 | -0.165 | 0.8690 | 0.9941 |  |
| BMI (kg/m2) | +0.0606 | 0.0586 | ±0.1172 | +1.034 | 0.3013 | 1.0625 |  |
| Hypertension | +0.7039 | 0.7600 | ±1.5200 | +0.926 | 0.3544 | 2.0216 |  |
| High cholesterol | +0.1209 | 0.7341 | ±1.4682 | +0.165 | 0.8692 | 1.1285 |  |
| Kidney disease | +26.9454 | 252838.0725 | ±505676.1450 | +0.000 | 0.9999 | 503784986665.7881 |  |
| Circulatory disease | -1.4563 | 1.2344 | ±2.4689 | -1.180 | 0.2381 | 0.2331 |  |
| GMI (%) | +2.8108 | 2.0668 | ±4.1336 | +1.360 | 0.1738 | 16.6239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2572**, LLR χ² = **20.20** (p = **0.0426**), AUC = **0.7988**, AIC = **82.3**, BIC = **107.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -9.7691 | 5.4101 | ±10.8203 | -1.806 | 0.0710 | 0.0001 | . |
| Education: graduate level (vs college) | +0.4572 | 0.7252 | ±1.4505 | +0.630 | 0.5284 | 1.5796 |  |
| Education: high school or below (vs college) | +39.1639 | 67108864.0000 | ±134217728.0000 | +0.000 | 1.0000 | 102015588188666192.0000 |  |
| Site: UCSD (vs UAB) | -0.1872 | 0.8411 | ±1.6823 | -0.223 | 0.8239 | 0.8293 |  |
| Site: UW (vs UAB) | -0.4539 | 0.9306 | ±1.8611 | -0.488 | 0.6257 | 0.6352 |  |
| Age (years) | +0.0029 | 0.0360 | ±0.0720 | +0.082 | 0.9348 | 1.0029 |  |
| BMI (kg/m2) | +0.0460 | 0.0573 | ±0.1145 | +0.804 | 0.4214 | 1.0471 |  |
| Hypertension | +0.4834 | 0.7573 | ±1.5145 | +0.638 | 0.5233 | 1.6216 |  |
| High cholesterol | +0.0831 | 0.7283 | ±1.4566 | +0.114 | 0.9092 | 1.0866 |  |
| Kidney disease | +32.7502 | 2502738.3132 | ±5005476.6265 | +0.000 | 1.0000 | 167190899524741.8125 |  |
| Circulatory disease | -1.4343 | 1.2243 | ±2.4486 | -1.171 | 0.2414 | 0.2383 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0587 | 0.0359 | ±0.0718 | +1.635 | 0.1020 | 1.0605 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Glucose SD, pooled (mg/dL)
_could not be fitted (LinAlgError)_

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2243**, LLR χ² = **17.62** (p = **0.0909**), AUC = **0.7393**, AIC = **84.9**, BIC = **110.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.4555 | 3.3355 | ±6.6710 | -0.736 | 0.4616 | 0.0858 |  |
| Education: graduate level (vs college) | +0.4051 | 0.7140 | ±1.4279 | +0.567 | 0.5704 | 1.4995 |  |
| Education: high school or below (vs college) | +33.8689 | 5651585.8738 | ±11303171.7476 | +0.000 | 1.0000 | 511779827572906.0000 |  |
| Site: UCSD (vs UAB) | +0.0183 | 0.8314 | ±1.6628 | +0.022 | 0.9825 | 1.0184 |  |
| Site: UW (vs UAB) | -0.3487 | 0.8944 | ±1.7888 | -0.390 | 0.6967 | 0.7056 |  |
| Age (years) | +0.0026 | 0.0363 | ±0.0727 | +0.072 | 0.9423 | 1.0026 |  |
| BMI (kg/m2) | +0.0564 | 0.0569 | ±0.1138 | +0.991 | 0.3217 | 1.0580 |  |
| Hypertension | +0.6997 | 0.7414 | ±1.4828 | +0.944 | 0.3452 | 2.0132 |  |
| High cholesterol | +0.0924 | 0.7028 | ±1.4055 | +0.131 | 0.8954 | 1.0968 |  |
| Kidney disease | +36.1305 | 27397079.0030 | ±54794158.0059 | +0.000 | 1.0000 | 4912041940288704.0000 |  |
| Circulatory disease | -1.2350 | 1.2277 | ±2.4553 | -1.006 | 0.3144 | 0.2908 |  |
| Avg. daily SD (mg/dL) | -0.0624 | 0.1170 | ±0.2339 | -0.534 | 0.5935 | 0.9395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### CV (%)
_could not be fitted (LinAlgError)_

#### Mean / SD ratio
_could not be fitted (LinAlgError)_

#### Avg. daily mean / SD
_could not be fitted (LinAlgError)_

#### MAG (mg/dL/h)
_could not be fitted (LinAlgError)_

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2259**, LLR χ² = **17.74** (p = **0.0877**), AUC = **0.7345**, AIC = **84.8**, BIC = **110.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.1070 | 3.4682 | ±6.9363 | -0.608 | 0.5435 | 0.1216 |  |
| Education: graduate level (vs college) | +0.3910 | 0.7127 | ±1.4255 | +0.549 | 0.5833 | 1.4784 |  |
| Education: high school or below (vs college) | +24.4941 | 51310.8499 | ±102621.6997 | +0.000 | 0.9996 | 43417773541.8410 |  |
| Site: UCSD (vs UAB) | +0.0286 | 0.8281 | ±1.6562 | +0.035 | 0.9724 | 1.0290 |  |
| Site: UW (vs UAB) | -0.3314 | 0.8986 | ±1.7973 | -0.369 | 0.7123 | 0.7179 |  |
| Age (years) | +0.0042 | 0.0367 | ±0.0733 | +0.115 | 0.9088 | 1.0042 |  |
| BMI (kg/m2) | +0.0548 | 0.0565 | ±0.1131 | +0.969 | 0.3328 | 1.0563 |  |
| Hypertension | +0.6701 | 0.7246 | ±1.4493 | +0.925 | 0.3551 | 1.9544 |  |
| High cholesterol | +0.1079 | 0.7055 | ±1.4110 | +0.153 | 0.8785 | 1.1139 |  |
| Kidney disease | +31.8000 | 3484118.6193 | ±6968237.2387 | +0.000 | 1.0000 | 64646977421151.8828 |  |
| Circulatory disease | -1.2666 | 1.2310 | ±2.4620 | -1.029 | 0.3035 | 0.2818 |  |
| Avg. daily range (mg/dL) | -0.0172 | 0.0269 | ±0.0538 | -0.639 | 0.5228 | 0.9829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### SD of daily means (mg/dL)
_could not be fitted (LinAlgError)_

#### Time in range 70-180, pooled (%)
_could not be fitted (LinAlgError)_

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2519**, LLR χ² = **19.79** (p = **0.0484**), AUC = **0.7619**, AIC = **82.8**, BIC = **108.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -169.1659 | 110.2890 | ±220.5779 | -1.534 | 0.1251 | 0.0000 |  |
| Education: graduate level (vs college) | +0.3594 | 0.7301 | ±1.4601 | +0.492 | 0.6226 | 1.4324 |  |
| Education: high school or below (vs college) | +25.5760 | 93722.4363 | ±187444.8727 | +0.000 | 0.9998 | 128087060766.7586 |  |
| Site: UCSD (vs UAB) | +0.0919 | 0.8492 | ±1.6985 | +0.108 | 0.9139 | 1.0962 |  |
| Site: UW (vs UAB) | -0.2834 | 0.9507 | ±1.9014 | -0.298 | 0.7657 | 0.7532 |  |
| Age (years) | +0.0116 | 0.0372 | ±0.0743 | +0.313 | 0.7543 | 1.0117 |  |
| BMI (kg/m2) | +0.0612 | 0.0579 | ±0.1157 | +1.057 | 0.2904 | 1.0631 |  |
| Hypertension | +0.6489 | 0.7274 | ±1.4549 | +0.892 | 0.3724 | 1.9134 |  |
| High cholesterol | +0.1503 | 0.7309 | ±1.4619 | +0.206 | 0.8371 | 1.1621 |  |
| Kidney disease | +25.3003 | 104780.7566 | ±209561.5131 | +0.000 | 0.9998 | 97229566670.6414 |  |
| Circulatory disease | -1.4449 | 1.2647 | ±2.5293 | -1.142 | 0.2532 | 0.2358 |  |
| Avg. daily time in range 70-180 (%) | +1.6563 | 1.0983 | ±2.1966 | +1.508 | 0.1315 | 5.2401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2279**, LLR χ² = **17.90** (p = **0.0838**), AUC = **0.7536**, AIC = **84.6**, BIC = **110.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6775 | 3.2398 | ±6.4797 | -0.826 | 0.4086 | 0.0687 |  |
| Education: graduate level (vs college) | +0.4064 | 0.7181 | ±1.4362 | +0.566 | 0.5715 | 1.5014 |  |
| Education: high school or below (vs college) | +26.2584 | 119299.6042 | ±238599.2085 | +0.000 | 0.9998 | 253447630519.7649 |  |
| Site: UCSD (vs UAB) | -0.0606 | 0.8147 | ±1.6293 | -0.074 | 0.9407 | 0.9412 |  |
| Site: UW (vs UAB) | -0.3089 | 0.8957 | ±1.7915 | -0.345 | 0.7302 | 0.7342 |  |
| Age (years) | -0.0044 | 0.0355 | ±0.0710 | -0.123 | 0.9021 | 0.9956 |  |
| BMI (kg/m2) | +0.0537 | 0.0567 | ±0.1134 | +0.947 | 0.3435 | 1.0552 |  |
| Hypertension | +0.6624 | 0.7241 | ±1.4482 | +0.915 | 0.3603 | 1.9394 |  |
| High cholesterol | +0.0587 | 0.7044 | ±1.4088 | +0.083 | 0.9336 | 1.0605 |  |
| Kidney disease | +26.7384 | 307138.4098 | ±614276.8197 | +0.000 | 0.9999 | 409593475438.2344 |  |
| Circulatory disease | -1.1955 | 1.2096 | ±2.4192 | -0.988 | 0.3230 | 0.3025 |  |
| Time 54-69, pooled (%) | -1.2550 | 1.7101 | ±3.4202 | -0.734 | 0.4630 | 0.2851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Avg. daily time 54-69 (%)
_could not be fitted (LinAlgError)_

#### Predictor entered alone: Time < 70, pooled (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2240**, LLR χ² = **17.60** (p = **0.0914**), AUC = **0.7488**, AIC = **84.9**, BIC = **110.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6377 | 3.2539 | ±6.5078 | -0.811 | 0.4176 | 0.0715 |  |
| Education: graduate level (vs college) | +0.3882 | 0.7141 | ±1.4283 | +0.544 | 0.5867 | 1.4743 |  |
| Education: high school or below (vs college) | +25.9051 | 106409.3295 | ±212818.6590 | +0.000 | 0.9998 | 178001834258.2281 |  |
| Site: UCSD (vs UAB) | -0.0917 | 0.8084 | ±1.6168 | -0.113 | 0.9097 | 0.9124 |  |
| Site: UW (vs UAB) | -0.3062 | 0.8911 | ±1.7822 | -0.344 | 0.7311 | 0.7362 |  |
| Age (years) | -0.0052 | 0.0357 | ±0.0714 | -0.145 | 0.8845 | 0.9948 |  |
| BMI (kg/m2) | +0.0536 | 0.0564 | ±0.1129 | +0.950 | 0.3421 | 1.0551 |  |
| Hypertension | +0.6411 | 0.7237 | ±1.4473 | +0.886 | 0.3757 | 1.8986 |  |
| High cholesterol | +0.0524 | 0.7017 | ±1.4034 | +0.075 | 0.9405 | 1.0538 |  |
| Kidney disease | +26.6080 | 283819.9433 | ±567639.8867 | +0.000 | 0.9999 | 359504038807.0883 |  |
| Circulatory disease | -1.1843 | 1.2059 | ±2.4117 | -0.982 | 0.3260 | 0.3060 |  |
| Time < 70 (%) | -0.7200 | 1.4122 | ±2.8244 | -0.510 | 0.6102 | 0.4868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2509**, LLR χ² = **19.71** (p = **0.0495**), AUC = **0.7929**, AIC = **82.8**, BIC = **108.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -3.1458 | 3.2884 | ±6.5767 | -0.957 | 0.3387 | 0.0430 |  |
| Education: graduate level (vs college) | +0.4359 | 0.7419 | ±1.4838 | +0.588 | 0.5568 | 1.5464 |  |
| Education: high school or below (vs college) | +27.3410 | 179855.1317 | ±359710.2633 | +0.000 | 0.9999 | 748216022468.7404 |  |
| Site: UCSD (vs UAB) | -0.0029 | 0.8530 | ±1.7060 | -0.003 | 0.9972 | 0.9971 |  |
| Site: UW (vs UAB) | -0.3302 | 0.9308 | ±1.8615 | -0.355 | 0.7228 | 0.7188 |  |
| Age (years) | +0.0030 | 0.0365 | ±0.0731 | +0.082 | 0.9344 | 1.0030 |  |
| BMI (kg/m2) | +0.0567 | 0.0578 | ±0.1155 | +0.981 | 0.3267 | 1.0583 |  |
| Hypertension | +0.7055 | 0.7356 | ±1.4712 | +0.959 | 0.3375 | 2.0249 |  |
| High cholesterol | +0.1299 | 0.7257 | ±1.4513 | +0.179 | 0.8579 | 1.1388 |  |
| Kidney disease | +27.2211 | 409558.3926 | ±819116.7851 | +0.000 | 0.9999 | 663735167116.2079 |  |
| Circulatory disease | -1.2683 | 1.2308 | ±2.4617 | -1.030 | 0.3028 | 0.2813 |  |
| Avg. daily time < 70 (%) | -2.9780 | 2.2070 | ±4.4140 | -1.349 | 0.1772 | 0.0509 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2296**, LLR χ² = **18.03** (p = **0.0808**), AUC = **0.7798**, AIC = **84.5**, BIC = **109.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +344.6527 | 419.8782 | ±839.7564 | +0.821 | 0.4117 | 479482642258989345929845330320936879832723133195644113783742328295273845268453216196124092748598371150448050396256710145466033842184802383072143081472.0000 |  |
| Education: graduate level (vs college) | +0.3901 | 0.7165 | ±1.4330 | +0.545 | 0.5861 | 1.4772 |  |
| Education: high school or below (vs college) | +25.6756 | 93355.5334 | ±186711.0669 | +0.000 | 0.9998 | 141511410345.7853 |  |
| Site: UCSD (vs UAB) | +0.0481 | 0.8239 | ±1.6477 | +0.058 | 0.9534 | 1.0493 |  |
| Site: UW (vs UAB) | -0.2783 | 0.8785 | ±1.7570 | -0.317 | 0.7514 | 0.7571 |  |
| Age (years) | +0.0064 | 0.0368 | ±0.0735 | +0.174 | 0.8618 | 1.0064 |  |
| BMI (kg/m2) | +0.0540 | 0.0574 | ±0.1148 | +0.941 | 0.3466 | 1.0555 |  |
| Hypertension | +0.5681 | 0.7025 | ±1.4050 | +0.809 | 0.4187 | 1.7649 |  |
| High cholesterol | +0.2081 | 0.7212 | ±1.4425 | +0.289 | 0.7730 | 1.2313 |  |
| Kidney disease | +28.3207 | 694915.7929 | ±1389831.5858 | +0.000 | 1.0000 | 1993129384361.3550 |  |
| Circulatory disease | -1.1119 | 1.2061 | ±2.4122 | -0.922 | 0.3566 | 0.3289 |  |
| Time 54-250, pooled (%) | -3.4834 | 4.2089 | ±8.4178 | -0.828 | 0.4079 | 0.0307 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Avg. daily time 54-250 (%)
_could not be fitted (LinAlgError)_

#### Time 181-250, pooled (%)
_could not be fitted (LinAlgError)_

#### Avg. daily time 181-250 (%)
_could not be fitted (LinAlgError)_

#### Time > 180, pooled (%)
_could not be fitted (LinAlgError)_

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 61)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **61**, events = **21**, McFadden pseudo-R² = **0.2288**, LLR χ² = **17.97** (p = **0.0823**), AUC = **0.7429**, AIC = **84.6**, BIC = **109.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -3.2533 | 3.3028 | ±6.6055 | -0.985 | 0.3246 | 0.0386 |  |
| Education: graduate level (vs college) | +0.3412 | 0.7141 | ±1.4282 | +0.478 | 0.6328 | 1.4066 |  |
| Education: high school or below (vs college) | +33.0509 | 4169941.9120 | ±8339883.8241 | +0.000 | 1.0000 | 225841138807446.1562 |  |
| Site: UCSD (vs UAB) | -0.0307 | 0.8136 | ±1.6272 | -0.038 | 0.9699 | 0.9697 |  |
| Site: UW (vs UAB) | -0.2761 | 0.9046 | ±1.8092 | -0.305 | 0.7602 | 0.7587 |  |
| Age (years) | +0.0062 | 0.0368 | ±0.0736 | +0.167 | 0.8673 | 1.0062 |  |
| BMI (kg/m2) | +0.0559 | 0.0567 | ±0.1134 | +0.986 | 0.3241 | 1.0575 |  |
| Hypertension | +0.5893 | 0.7114 | ±1.4229 | +0.828 | 0.4075 | 1.8027 |  |
| High cholesterol | +0.0818 | 0.7044 | ±1.4088 | +0.116 | 0.9075 | 1.0852 |  |
| Kidney disease | +31.8811 | 3149575.0456 | ±6299150.0912 | +0.000 | 1.0000 | 70110800897509.4062 |  |
| Circulatory disease | -1.2453 | 1.2156 | ±2.4311 | -1.024 | 0.3056 | 0.2878 |  |
| Avg. daily time > 180 (%) | -1.0205 | 1.3061 | ±2.6123 | -0.781 | 0.4346 | 0.3604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 61; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **61**, R² = **0.1853**, Adj R² = **0.0224**, F-statistic = **1.14** (p = **0.3545**), Residual SE = **2.685** on **50** df, AIC = **303.5**, BIC = **326.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6195** | 5.4288 | ±10.8576 | **+2.140** | **0.0323** | * |
| Education: graduate level (vs college) | +0.1249 | 0.9300 | ±1.8599 | +0.134 | 0.8932 |  |
| Education: high school or below (vs college) | -3.8699 | 3.0166 | ±6.0333 | -1.283 | 0.1995 |  |
| Site: UCSD (vs UAB) | +0.8010 | 1.3006 | ±2.6012 | +0.616 | 0.5380 |  |
| Site: UW (vs UAB) | +1.1053 | 1.4901 | ±2.9801 | +0.742 | 0.4582 |  |
| Age (years) | +0.0022 | 0.0461 | ±0.0923 | +0.048 | 0.9617 |  |
| BMI (kg/m2) | +0.0311 | 0.0787 | ±0.1574 | +0.395 | 0.6929 |  |
| Hypertension | -0.7435 | 0.9713 | ±1.9426 | -0.765 | 0.4440 |  |
| High cholesterol | -0.0627 | 0.9301 | ±1.8602 | -0.067 | 0.9462 |  |
| Kidney disease | +0.7317 | 2.4327 | ±4.8654 | +0.301 | 0.7636 |  |
| Circulatory disease | -0.0477 | 0.9714 | ±1.9428 | -0.049 | 0.9609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **61**, R² = **0.1868**, Adj R² = **0.0042**, F-statistic = **1.02** (p = **0.4410**), Residual SE = **2.709** on **49** df, AIC = **305.4**, BIC = **330.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +9.8878 | 8.8025 | ±17.6049 | +1.123 | 0.2613 |  |
| Education: graduate level (vs college) | +0.1658 | 0.9207 | ±1.8414 | +0.180 | 0.8571 |  |
| Education: high school or below (vs college) | -4.0435 | 3.5729 | ±7.1458 | -1.132 | 0.2578 |  |
| Site: UCSD (vs UAB) | +0.7788 | 1.3394 | ±2.6788 | +0.581 | 0.5609 |  |
| Site: UW (vs UAB) | +1.0743 | 1.4881 | ±2.9763 | +0.722 | 0.4704 |  |
| Age (years) | +0.0015 | 0.0463 | ±0.0926 | +0.032 | 0.9747 |  |
| BMI (kg/m2) | +0.0299 | 0.0829 | ±0.1658 | +0.360 | 0.7187 |  |
| Hypertension | -0.7753 | 0.9542 | ±1.9084 | -0.813 | 0.4165 |  |
| High cholesterol | -0.0841 | 0.9436 | ±1.8871 | -0.089 | 0.9290 |  |
| Kidney disease | +0.8062 | 2.6494 | ±5.2988 | +0.304 | 0.7609 |  |
| Circulatory disease | -0.0567 | 0.9983 | ±1.9966 | -0.057 | 0.9547 |  |
| HbA1c (%) | +0.3268 | 1.1822 | ±2.3644 | +0.276 | 0.7822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **61**, R² = **0.1922**, Adj R² = **0.0109**, F-statistic = **1.06** (p = **0.4118**), Residual SE = **2.700** on **49** df, AIC = **304.9**, BIC = **330.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3277** | 7.5826 | ±15.1652 | **+2.021** | **0.0432** | * |
| Education: graduate level (vs college) | +0.0868 | 0.9749 | ±1.9499 | +0.089 | 0.9291 |  |
| Education: high school or below (vs college) | -3.9817 | 3.0980 | ±6.1959 | -1.285 | 0.1987 |  |
| Site: UCSD (vs UAB) | +0.7699 | 1.2802 | ±2.5605 | +0.601 | 0.5476 |  |
| Site: UW (vs UAB) | +1.1198 | 1.5048 | ±3.0096 | +0.744 | 0.4568 |  |
| Age (years) | +0.0040 | 0.0462 | ±0.0924 | +0.088 | 0.9303 |  |
| BMI (kg/m2) | +0.0277 | 0.0787 | ±0.1574 | +0.352 | 0.7252 |  |
| Hypertension | -0.7423 | 0.9663 | ±1.9327 | -0.768 | 0.4424 |  |
| High cholesterol | -0.0946 | 0.9269 | ±1.8538 | -0.102 | 0.9187 |  |
| Kidney disease | +0.7515 | 2.5741 | ±5.1481 | +0.292 | 0.7703 |  |
| Circulatory disease | +0.0847 | 0.9851 | ±1.9702 | +0.086 | 0.9315 |  |
| Mean glucose (mg/dL) | -0.0321 | 0.0567 | ±0.1134 | -0.565 | 0.5718 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **61**, R² = **0.1922**, Adj R² = **0.0109**, F-statistic = **1.06** (p = **0.4118**), Residual SE = **2.700** on **49** df, AIC = **304.9**, BIC = **330.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +19.7627 | 14.2816 | ±28.5632 | +1.384 | 0.1664 |  |
| Education: graduate level (vs college) | +0.0868 | 0.9749 | ±1.9499 | +0.089 | 0.9291 |  |
| Education: high school or below (vs college) | -3.9817 | 3.0980 | ±6.1959 | -1.285 | 0.1987 |  |
| Site: UCSD (vs UAB) | +0.7699 | 1.2802 | ±2.5605 | +0.601 | 0.5476 |  |
| Site: UW (vs UAB) | +1.1198 | 1.5048 | ±3.0096 | +0.744 | 0.4568 |  |
| Age (years) | +0.0040 | 0.0462 | ±0.0924 | +0.088 | 0.9303 |  |
| BMI (kg/m2) | +0.0277 | 0.0787 | ±0.1574 | +0.352 | 0.7252 |  |
| Hypertension | -0.7423 | 0.9663 | ±1.9327 | -0.768 | 0.4424 |  |
| High cholesterol | -0.0946 | 0.9269 | ±1.8538 | -0.102 | 0.9187 |  |
| Kidney disease | +0.7515 | 2.5741 | ±5.1481 | +0.292 | 0.7703 |  |
| Circulatory disease | +0.0847 | 0.9851 | ±1.9702 | +0.086 | 0.9315 |  |
| GMI (%) | -1.3399 | 2.3698 | ±4.7395 | -0.565 | 0.5718 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **61**, R² = **0.1927**, Adj R² = **0.0115**, F-statistic = **1.06** (p = **0.4091**), Residual SE = **2.700** on **49** df, AIC = **304.9**, BIC = **330.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3432** | 6.6741 | ±13.3483 | **+2.149** | **0.0316** | * |
| Education: graduate level (vs college) | +0.1222 | 0.9407 | ±1.8815 | +0.130 | 0.8966 |  |
| Education: high school or below (vs college) | -3.8429 | 3.1864 | ±6.3728 | -1.206 | 0.2278 |  |
| Site: UCSD (vs UAB) | +0.8068 | 1.2970 | ±2.5941 | +0.622 | 0.5339 |  |
| Site: UW (vs UAB) | +1.1520 | 1.5257 | ±3.0513 | +0.755 | 0.4502 |  |
| Age (years) | +0.0009 | 0.0463 | ±0.0925 | +0.019 | 0.9848 |  |
| BMI (kg/m2) | +0.0317 | 0.0790 | ±0.1581 | +0.401 | 0.6887 |  |
| Hypertension | -0.6525 | 0.9962 | ±1.9924 | -0.655 | 0.5125 |  |
| High cholesterol | -0.1071 | 0.9315 | ±1.8630 | -0.115 | 0.9085 |  |
| Kidney disease | +0.5894 | 2.8021 | ±5.6042 | +0.210 | 0.8334 |  |
| Circulatory disease | +0.0252 | 0.9794 | ±1.9589 | +0.026 | 0.9795 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0233 | 0.0376 | ±0.0752 | -0.620 | 0.5351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **61**, R² = **0.1910**, Adj R² = **0.0094**, F-statistic = **1.05** (p = **0.4180**), Residual SE = **2.702** on **49** df, AIC = **305.0**, BIC = **330.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.5072** | 4.9920 | ±9.9839 | **+2.505** | **0.0122** | * |
| Education: graduate level (vs college) | +0.1319 | 0.9467 | ±1.8933 | +0.139 | 0.8891 |  |
| Education: high school or below (vs college) | -3.8243 | 3.0084 | ±6.0169 | -1.271 | 0.2037 |  |
| Site: UCSD (vs UAB) | +0.8893 | 1.3618 | ±2.7236 | +0.653 | 0.5137 |  |
| Site: UW (vs UAB) | +1.0672 | 1.4738 | ±2.9475 | +0.724 | 0.4690 |  |
| Age (years) | +0.0059 | 0.0525 | ±0.1050 | +0.113 | 0.9100 |  |
| BMI (kg/m2) | +0.0328 | 0.0789 | ±0.1579 | +0.416 | 0.6777 |  |
| Hypertension | -0.5941 | 1.0427 | ±2.0853 | -0.570 | 0.5688 |  |
| High cholesterol | -0.0737 | 0.9275 | ±1.8550 | -0.079 | 0.9367 |  |
| Kidney disease | +0.9984 | 2.2985 | ±4.5970 | +0.434 | 0.6640 |  |
| Circulatory disease | -0.0492 | 0.9314 | ±1.8628 | -0.053 | 0.9579 |  |
| Glucose SD, pooled (mg/dL) | -0.0766 | 0.1424 | ±0.2848 | -0.538 | 0.5906 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **61**, R² = **0.1854**, Adj R² = **0.0026**, F-statistic = **1.01** (p = **0.4484**), Residual SE = **2.712** on **49** df, AIC = **305.5**, BIC = **330.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5341** | 5.2263 | ±10.4526 | **+2.207** | **0.0273** | * |
| Education: graduate level (vs college) | +0.1249 | 0.9523 | ±1.9047 | +0.131 | 0.8956 |  |
| Education: high school or below (vs college) | -3.8741 | 3.0449 | ±6.0899 | -1.272 | 0.2033 |  |
| Site: UCSD (vs UAB) | +0.7820 | 1.3881 | ±2.7763 | +0.563 | 0.5732 |  |
| Site: UW (vs UAB) | +1.1068 | 1.5007 | ±3.0015 | +0.738 | 0.4608 |  |
| Age (years) | +0.0013 | 0.0531 | ±0.1062 | +0.025 | 0.9800 |  |
| BMI (kg/m2) | +0.0307 | 0.0811 | ±0.1622 | +0.379 | 0.7050 |  |
| Hypertension | -0.7653 | 1.0325 | ±2.0649 | -0.741 | 0.4586 |  |
| High cholesterol | -0.0608 | 0.9372 | ±1.8743 | -0.065 | 0.9482 |  |
| Kidney disease | +0.6949 | 2.4175 | ±4.8350 | +0.287 | 0.7738 |  |
| Circulatory disease | -0.0428 | 1.0262 | ±2.0525 | -0.042 | 0.9667 |  |
| Avg. daily SD (mg/dL) | +0.0111 | 0.1451 | ±0.2901 | +0.076 | 0.9392 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **61**, R² = **0.1873**, Adj R² = **0.0048**, F-statistic = **1.03** (p = **0.4383**), Residual SE = **2.709** on **49** df, AIC = **305.3**, BIC = **330.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.1568** | 5.1371 | ±10.2743 | **+2.366** | **0.0180** | * |
| Education: graduate level (vs college) | +0.1365 | 0.9628 | ±1.9257 | +0.142 | 0.8873 |  |
| Education: high school or below (vs college) | -3.8270 | 3.0179 | ±6.0358 | -1.268 | 0.2048 |  |
| Site: UCSD (vs UAB) | +0.8587 | 1.3580 | ±2.7161 | +0.632 | 0.5272 |  |
| Site: UW (vs UAB) | +1.0796 | 1.4944 | ±2.9888 | +0.722 | 0.4700 |  |
| Age (years) | +0.0040 | 0.0520 | ±0.1039 | +0.076 | 0.9390 |  |
| BMI (kg/m2) | +0.0326 | 0.0801 | ±0.1602 | +0.407 | 0.6843 |  |
| Hypertension | -0.6580 | 1.0154 | ±2.0307 | -0.648 | 0.5170 |  |
| High cholesterol | -0.0608 | 0.9359 | ±1.8719 | -0.065 | 0.9482 |  |
| Kidney disease | +0.8949 | 2.3707 | ±4.7415 | +0.377 | 0.7058 |  |
| Circulatory disease | -0.0736 | 0.9864 | ±1.9728 | -0.075 | 0.9405 |  |
| CV (%) | -0.0524 | 0.1708 | ±0.3417 | -0.307 | 0.7592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **61**, R² = **0.1900**, Adj R² = **0.0081**, F-statistic = **1.04** (p = **0.4238**), Residual SE = **2.704** on **49** df, AIC = **305.1**, BIC = **330.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.2264 | 7.4219 | ±14.8437 | +1.378 | 0.1682 |  |
| Education: graduate level (vs college) | +0.1325 | 0.9653 | ±1.9307 | +0.137 | 0.8908 |  |
| Education: high school or below (vs college) | -3.7810 | 3.0068 | ±6.0136 | -1.257 | 0.2086 |  |
| Site: UCSD (vs UAB) | +0.8754 | 1.3534 | ±2.7068 | +0.647 | 0.5178 |  |
| Site: UW (vs UAB) | +1.0541 | 1.4897 | ±2.9794 | +0.708 | 0.4792 |  |
| Age (years) | +0.0042 | 0.0528 | ±0.1055 | +0.079 | 0.9368 |  |
| BMI (kg/m2) | +0.0340 | 0.0803 | ±0.1606 | +0.424 | 0.6717 |  |
| Hypertension | -0.6313 | 1.0049 | ±2.0097 | -0.628 | 0.5299 |  |
| High cholesterol | -0.0584 | 0.9321 | ±1.8643 | -0.063 | 0.9500 |  |
| Kidney disease | +0.9062 | 2.3385 | ±4.6770 | +0.388 | 0.6984 |  |
| Circulatory disease | -0.1076 | 0.9814 | ±1.9627 | -0.110 | 0.9127 |  |
| Mean / SD ratio | +0.1543 | 0.3374 | ±0.6747 | +0.457 | 0.6474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **61**, R² = **0.1855**, Adj R² = **0.0026**, F-statistic = **1.01** (p = **0.4481**), Residual SE = **2.712** on **49** df, AIC = **305.4**, BIC = **330.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +11.8826 | 6.7949 | ±13.5897 | +1.749 | 0.0803 | . |
| Education: graduate level (vs college) | +0.1244 | 0.9602 | ±1.9204 | +0.130 | 0.8969 |  |
| Education: high school or below (vs college) | -3.8901 | 3.0783 | ±6.1566 | -1.264 | 0.2063 |  |
| Site: UCSD (vs UAB) | +0.7797 | 1.3498 | ±2.6996 | +0.578 | 0.5635 |  |
| Site: UW (vs UAB) | +1.1127 | 1.5144 | ±3.0287 | +0.735 | 0.4625 |  |
| Age (years) | +0.0014 | 0.0514 | ±0.1027 | +0.027 | 0.9786 |  |
| BMI (kg/m2) | +0.0306 | 0.0813 | ±0.1625 | +0.376 | 0.7067 |  |
| Hypertension | -0.7696 | 0.9672 | ±1.9344 | -0.796 | 0.4262 |  |
| High cholesterol | -0.0657 | 0.9400 | ±1.8800 | -0.070 | 0.9442 |  |
| Kidney disease | +0.7059 | 2.4829 | ±4.9658 | +0.284 | 0.7762 |  |
| Circulatory disease | -0.0263 | 1.0700 | ±2.1401 | -0.025 | 0.9804 |  |
| Avg. daily mean/SD | -0.0215 | 0.2432 | ±0.4865 | -0.088 | 0.9296 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **61**, R² = **0.1909**, Adj R² = **0.0093**, F-statistic = **1.05** (p = **0.4186**), Residual SE = **2.703** on **49** df, AIC = **305.0**, BIC = **330.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.0326** | 5.3744 | ±10.7488 | **+2.053** | **0.0401** | * |
| Education: graduate level (vs college) | +0.1055 | 0.9445 | ±1.8890 | +0.112 | 0.9110 |  |
| Education: high school or below (vs college) | -4.0267 | 3.0149 | ±6.0298 | -1.336 | 0.1817 |  |
| Site: UCSD (vs UAB) | +0.7084 | 1.3127 | ±2.6254 | +0.540 | 0.5894 |  |
| Site: UW (vs UAB) | +1.0840 | 1.5052 | ±3.0104 | +0.720 | 0.4714 |  |
| Age (years) | -0.0033 | 0.0482 | ±0.0965 | -0.068 | 0.9455 |  |
| BMI (kg/m2) | +0.0231 | 0.0803 | ±0.1606 | +0.288 | 0.7733 |  |
| Hypertension | -0.8223 | 0.9870 | ±1.9741 | -0.833 | 0.4048 |  |
| High cholesterol | -0.0275 | 0.9244 | ±1.8488 | -0.030 | 0.9762 |  |
| Kidney disease | +0.8222 | 2.4171 | ±4.8342 | +0.340 | 0.7337 |  |
| Circulatory disease | +0.1140 | 1.0392 | ±2.0785 | +0.110 | 0.9126 |  |
| MAG (mg/dL/h) | +0.0367 | 0.0479 | ±0.0959 | +0.765 | 0.4445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **61**, R² = **0.1865**, Adj R² = **0.0038**, F-statistic = **1.02** (p = **0.4427**), Residual SE = **2.710** on **49** df, AIC = **305.4**, BIC = **330.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.2325** | 5.0212 | ±10.0424 | **+2.237** | **0.0253** | * |
| Education: graduate level (vs college) | +0.1295 | 0.9554 | ±1.9108 | +0.136 | 0.8922 |  |
| Education: high school or below (vs college) | -3.9123 | 3.0355 | ±6.0711 | -1.289 | 0.1975 |  |
| Site: UCSD (vs UAB) | +0.7544 | 1.3865 | ±2.7731 | +0.544 | 0.5864 |  |
| Site: UW (vs UAB) | +1.1130 | 1.5133 | ±3.0267 | +0.735 | 0.4621 |  |
| Age (years) | -0.0010 | 0.0547 | ±0.1093 | -0.018 | 0.9855 |  |
| BMI (kg/m2) | +0.0306 | 0.0810 | ±0.1621 | +0.377 | 0.7062 |  |
| Hypertension | -0.7853 | 1.0542 | ±2.1085 | -0.745 | 0.4563 |  |
| High cholesterol | -0.0635 | 0.9526 | ±1.9053 | -0.067 | 0.9468 |  |
| Kidney disease | +0.6786 | 2.3943 | ±4.7886 | +0.283 | 0.7768 |  |
| Circulatory disease | -0.0041 | 1.0336 | ±2.0672 | -0.004 | 0.9968 |  |
| Avg. daily range (mg/dL) | +0.0081 | 0.0336 | ±0.0672 | +0.242 | 0.8089 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **61**, R² = **0.2150**, Adj R² = **0.0387**, F-statistic = **1.22** (p = **0.2996**), Residual SE = **2.662** on **49** df, AIC = **303.2**, BIC = **328.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.6696** | 5.1357 | ±10.2714 | **+2.662** | **0.0078** | ** |
| Education: graduate level (vs college) | +0.1073 | 0.9267 | ±1.8535 | +0.116 | 0.9078 |  |
| Education: high school or below (vs college) | -3.7696 | 3.1456 | ±6.2912 | -1.198 | 0.2308 |  |
| Site: UCSD (vs UAB) | +0.6885 | 1.2443 | ±2.4886 | +0.553 | 0.5800 |  |
| Site: UW (vs UAB) | +0.9891 | 1.4462 | ±2.8924 | +0.684 | 0.4940 |  |
| Age (years) | -0.0095 | 0.0455 | ±0.0910 | -0.208 | 0.8355 |  |
| BMI (kg/m2) | +0.0216 | 0.0742 | ±0.1484 | +0.291 | 0.7707 |  |
| Hypertension | -0.6722 | 0.9571 | ±1.9142 | -0.702 | 0.4825 |  |
| High cholesterol | +0.0065 | 0.9238 | ±1.8475 | +0.007 | 0.9944 |  |
| Kidney disease | +1.2672 | 2.2836 | ±4.5672 | +0.555 | 0.5790 |  |
| Circulatory disease | +0.1751 | 0.8761 | ±1.7521 | +0.200 | 0.8416 |  |
| SD of daily means (mg/dL) | -0.2033 | 0.1606 | ±0.3211 | -1.266 | 0.2055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **61**, R² = **0.1937**, Adj R² = **0.0126**, F-statistic = **1.07** (p = **0.4041**), Residual SE = **2.698** on **49** df, AIC = **304.8**, BIC = **330.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -68.6234 | 145.2843 | ±290.5687 | -0.472 | 0.6367 |  |
| Education: graduate level (vs college) | +0.0858 | 0.9641 | ±1.9282 | +0.089 | 0.9291 |  |
| Education: high school or below (vs college) | -3.9814 | 3.1003 | ±6.2006 | -1.284 | 0.1991 |  |
| Site: UCSD (vs UAB) | +0.8121 | 1.3289 | ±2.6578 | +0.611 | 0.5411 |  |
| Site: UW (vs UAB) | +1.1184 | 1.5024 | ±3.0049 | +0.744 | 0.4566 |  |
| Age (years) | +0.0038 | 0.0508 | ±0.1017 | +0.076 | 0.9397 |  |
| BMI (kg/m2) | +0.0363 | 0.0819 | ±0.1638 | +0.443 | 0.6577 |  |
| Hypertension | -0.7022 | 1.0239 | ±2.0477 | -0.686 | 0.4928 |  |
| High cholesterol | -0.0450 | 0.9527 | ±1.9054 | -0.047 | 0.9624 |  |
| Kidney disease | +0.9210 | 2.4821 | ±4.9642 | +0.371 | 0.7106 |  |
| Circulatory disease | -0.2025 | 1.0342 | ±2.0683 | -0.196 | 0.8447 |  |
| Time in range 70-180, pooled (%) | +0.8032 | 1.4233 | ±2.8466 | +0.564 | 0.5725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **61**, R² = **0.1869**, Adj R² = **0.0044**, F-statistic = **1.02** (p = **0.4402**), Residual SE = **2.709** on **49** df, AIC = **305.3**, BIC = **330.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +46.7573 | 151.6497 | ±303.2994 | +0.308 | 0.7578 |  |
| Education: graduate level (vs college) | +0.1499 | 1.0086 | ±2.0172 | +0.149 | 0.8818 |  |
| Education: high school or below (vs college) | -3.8406 | 3.0231 | ±6.0462 | -1.270 | 0.2039 |  |
| Site: UCSD (vs UAB) | +0.7753 | 1.3973 | ±2.7946 | +0.555 | 0.5790 |  |
| Site: UW (vs UAB) | +1.1005 | 1.5906 | ±3.1812 | +0.692 | 0.4890 |  |
| Age (years) | -0.0012 | 0.0573 | ±0.1147 | -0.020 | 0.9838 |  |
| BMI (kg/m2) | +0.0292 | 0.0839 | ±0.1677 | +0.349 | 0.7274 |  |
| Hypertension | -0.7507 | 1.0348 | ±2.0696 | -0.725 | 0.4682 |  |
| High cholesterol | -0.0730 | 0.9962 | ±1.9924 | -0.073 | 0.9416 |  |
| Kidney disease | +0.6435 | 2.3716 | ±4.7433 | +0.271 | 0.7861 |  |
| Circulatory disease | +0.0113 | 1.0324 | ±2.0649 | +0.011 | 0.9912 |  |
| Avg. daily time in range 70-180 (%) | -0.3501 | 1.4742 | ±2.9484 | -0.237 | 0.8123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **61**, R² = **0.1948**, Adj R² = **0.0141**, F-statistic = **1.08** (p = **0.3979**), Residual SE = **2.696** on **49** df, AIC = **304.7**, BIC = **330.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4699** | 5.5008 | ±11.0017 | **+2.085** | **0.0371** | * |
| Education: graduate level (vs college) | +0.1122 | 0.9358 | ±1.8717 | +0.120 | 0.9045 |  |
| Education: high school or below (vs college) | -4.1044 | 2.8850 | ±5.7700 | -1.423 | 0.1548 |  |
| Site: UCSD (vs UAB) | +0.7541 | 1.2631 | ±2.5262 | +0.597 | 0.5505 |  |
| Site: UW (vs UAB) | +1.0850 | 1.4861 | ±2.9722 | +0.730 | 0.4653 |  |
| Age (years) | +0.0046 | 0.0462 | ±0.0925 | +0.098 | 0.9216 |  |
| BMI (kg/m2) | +0.0269 | 0.0780 | ±0.1559 | +0.345 | 0.7303 |  |
| Hypertension | -0.7969 | 0.9742 | ±1.9484 | -0.818 | 0.4134 |  |
| High cholesterol | -0.0691 | 0.9457 | ±1.8914 | -0.073 | 0.9418 |  |
| Kidney disease | +0.8411 | 2.3492 | ±4.6984 | +0.358 | 0.7203 |  |
| Circulatory disease | +0.0872 | 0.9471 | ±1.8943 | +0.092 | 0.9266 |  |
| Time 54-69, pooled (%) | +1.3846 | 1.8022 | ±3.6045 | +0.768 | 0.4423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **61**, R² = **0.2120**, Adj R² = **0.0351**, F-statistic = **1.20** (p = **0.3130**), Residual SE = **2.667** on **49** df, AIC = **303.4**, BIC = **328.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.9084** | 5.3097 | ±10.6195 | **+2.243** | **0.0249** | * |
| Education: graduate level (vs college) | +0.1071 | 0.9366 | ±1.8732 | +0.114 | 0.9089 |  |
| Education: high school or below (vs college) | -4.2418 | 2.8277 | ±5.6554 | -1.500 | 0.1336 |  |
| Site: UCSD (vs UAB) | +0.7032 | 1.2467 | ±2.4933 | +0.564 | 0.5727 |  |
| Site: UW (vs UAB) | +1.1231 | 1.4932 | ±2.9863 | +0.752 | 0.4519 |  |
| Age (years) | -0.0018 | 0.0450 | ±0.0899 | -0.039 | 0.9689 |  |
| BMI (kg/m2) | +0.0227 | 0.0762 | ±0.1524 | +0.297 | 0.7663 |  |
| Hypertension | -0.7837 | 0.9612 | ±1.9225 | -0.815 | 0.4149 |  |
| High cholesterol | -0.1411 | 0.9327 | ±1.8654 | -0.151 | 0.8797 |  |
| Kidney disease | +0.8541 | 2.2745 | ±4.5489 | +0.376 | 0.7073 |  |
| Circulatory disease | +0.1593 | 0.9740 | ±1.9480 | +0.164 | 0.8701 |  |
| Avg. daily time 54-69 (%) | +2.4662 | 1.5842 | ±3.1685 | +1.557 | 0.1195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **61**, R² = **0.1905**, Adj R² = **0.0088**, F-statistic = **1.05** (p = **0.4206**), Residual SE = **2.703** on **49** df, AIC = **305.1**, BIC = **330.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.3993** | 5.5263 | ±11.0526 | **+2.063** | **0.0391** | * |
| Education: graduate level (vs college) | +0.1158 | 0.9357 | ±1.8713 | +0.124 | 0.9015 |  |
| Education: high school or below (vs college) | -3.9969 | 2.9323 | ±5.8645 | -1.363 | 0.1729 |  |
| Site: UCSD (vs UAB) | +0.7923 | 1.2909 | ±2.5818 | +0.614 | 0.5394 |  |
| Site: UW (vs UAB) | +1.0973 | 1.4994 | ±2.9988 | +0.732 | 0.4643 |  |
| Age (years) | +0.0056 | 0.0460 | ±0.0921 | +0.121 | 0.9033 |  |
| BMI (kg/m2) | +0.0275 | 0.0785 | ±0.1571 | +0.350 | 0.7266 |  |
| Hypertension | -0.7883 | 0.9887 | ±1.9773 | -0.797 | 0.4253 |  |
| High cholesterol | -0.0519 | 0.9486 | ±1.8972 | -0.055 | 0.9563 |  |
| Kidney disease | +0.8076 | 2.3833 | ±4.7665 | +0.339 | 0.7347 |  |
| Circulatory disease | +0.0548 | 0.9489 | ±1.8978 | +0.058 | 0.9539 |  |
| Time < 70 (%) | +0.9069 | 1.5777 | ±3.1555 | +0.575 | 0.5654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **61**, R² = **0.2188**, Adj R² = **0.0435**, F-statistic = **1.25** (p = **0.2826**), Residual SE = **2.656** on **49** df, AIC = **302.9**, BIC = **328.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8590** | 5.3153 | ±10.6307 | **+2.231** | **0.0257** | * |
| Education: graduate level (vs college) | +0.1392 | 0.9315 | ±1.8631 | +0.149 | 0.8813 |  |
| Education: high school or below (vs college) | -4.2297 | 2.8236 | ±5.6472 | -1.498 | 0.1341 |  |
| Site: UCSD (vs UAB) | +0.6887 | 1.2425 | ±2.4850 | +0.554 | 0.5794 |  |
| Site: UW (vs UAB) | +1.0940 | 1.4841 | ±2.9682 | +0.737 | 0.4610 |  |
| Age (years) | -0.0010 | 0.0449 | ±0.0898 | -0.023 | 0.9818 |  |
| BMI (kg/m2) | +0.0222 | 0.0764 | ±0.1528 | +0.291 | 0.7713 |  |
| Hypertension | -0.7956 | 0.9596 | ±1.9192 | -0.829 | 0.4071 |  |
| High cholesterol | -0.1766 | 0.9325 | ±1.8649 | -0.189 | 0.8498 |  |
| Kidney disease | +0.8644 | 2.2561 | ±4.5123 | +0.383 | 0.7016 |  |
| Circulatory disease | +0.1930 | 0.9734 | ±1.9469 | +0.198 | 0.8428 |  |
| Avg. daily time < 70 (%) | +2.6480 | 1.5561 | ±3.1122 | +1.702 | 0.0888 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.2100**, Adj R² = **0.0326**, F-statistic = **1.18** (p = **0.3226**), Residual SE = **2.671** on **49** df, AIC = **303.6**, BIC = **328.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -622.8465 | 1224.9194 | ±2449.8388 | -0.508 | 0.6111 |  |
| Education: graduate level (vs college) | +0.1729 | 0.9325 | ±1.8651 | +0.185 | 0.8529 |  |
| Education: high school or below (vs college) | -4.0563 | 3.0860 | ±6.1720 | -1.314 | 0.1887 |  |
| Site: UCSD (vs UAB) | +0.5809 | 1.2116 | ±2.4232 | +0.479 | 0.6316 |  |
| Site: UW (vs UAB) | +0.9697 | 1.4149 | ±2.8298 | +0.685 | 0.4931 |  |
| Age (years) | -0.0125 | 0.0434 | ±0.0868 | -0.287 | 0.7740 |  |
| BMI (kg/m2) | +0.0341 | 0.0824 | ±0.1648 | +0.414 | 0.6791 |  |
| Hypertension | -0.7298 | 1.0172 | ±2.0344 | -0.717 | 0.4731 |  |
| High cholesterol | -0.2194 | 0.8323 | ±1.6646 | -0.264 | 0.7920 |  |
| Kidney disease | +0.7653 | 2.4325 | ±4.8651 | +0.315 | 0.7530 |  |
| Circulatory disease | -0.1433 | 1.0006 | ±2.0013 | -0.143 | 0.8861 |  |
| Time 54-250, pooled (%) | +6.3564 | 12.2437 | ±24.4873 | +0.519 | 0.6037 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.1973**, Adj R² = **0.0171**, F-statistic = **1.10** (p = **0.3849**), Residual SE = **2.692** on **49** df, AIC = **304.6**, BIC = **329.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -986.1333 | 3884.7624 | ±7769.5248 | -0.254 | 0.7996 |  |
| Education: graduate level (vs college) | +0.0724 | 1.2230 | ±2.4460 | +0.059 | 0.9528 |  |
| Education: high school or below (vs college) | -4.0188 | 3.1058 | ±6.2117 | -1.294 | 0.1957 |  |
| Site: UCSD (vs UAB) | +0.7159 | 1.3396 | ±2.6791 | +0.534 | 0.5930 |  |
| Site: UW (vs UAB) | +1.0504 | 1.7844 | ±3.5689 | +0.589 | 0.5561 |  |
| Age (years) | -0.0046 | 0.0445 | ±0.0889 | -0.104 | 0.9172 |  |
| BMI (kg/m2) | +0.0252 | 0.0767 | ±0.1534 | +0.328 | 0.7426 |  |
| Hypertension | -0.8052 | 1.0526 | ±2.1052 | -0.765 | 0.4443 |  |
| High cholesterol | -0.0398 | 1.1984 | ±2.3968 | -0.033 | 0.9735 |  |
| Kidney disease | +0.8352 | 2.4431 | ±4.8861 | +0.342 | 0.7324 |  |
| Circulatory disease | -0.1113 | 1.0152 | ±2.0305 | -0.110 | 0.9127 |  |
| Avg. daily time 54-250 (%) | +9.9856 | 38.8301 | ±77.6602 | +0.257 | 0.7971 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **61**, R² = **0.2073**, Adj R² = **0.0294**, F-statistic = **1.16** (p = **0.3352**), Residual SE = **2.675** on **49** df, AIC = **303.8**, BIC = **329.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.3032** | 5.6883 | ±11.3767 | **+1.987** | **0.0469** | * |
| Education: graduate level (vs college) | +0.0173 | 0.9610 | ±1.9221 | +0.018 | 0.9856 |  |
| Education: high school or below (vs college) | -4.3291 | 2.9868 | ±5.9735 | -1.449 | 0.1472 |  |
| Site: UCSD (vs UAB) | +0.8250 | 1.2916 | ±2.5833 | +0.639 | 0.5230 |  |
| Site: UW (vs UAB) | +1.1431 | 1.4753 | ±2.9506 | +0.775 | 0.4384 |  |
| Age (years) | +0.0121 | 0.0572 | ±0.1145 | +0.212 | 0.8321 |  |
| BMI (kg/m2) | +0.0360 | 0.0791 | ±0.1582 | +0.455 | 0.6492 |  |
| Hypertension | -0.7259 | 0.9832 | ±1.9665 | -0.738 | 0.4604 |  |
| High cholesterol | +0.0068 | 0.9686 | ±1.9372 | +0.007 | 0.9944 |  |
| Kidney disease | +1.2410 | 2.3279 | ±4.6559 | +0.533 | 0.5940 |  |
| Circulatory disease | -0.1799 | 0.9844 | ±1.9688 | -0.183 | 0.8550 |  |
| Time 181-250, pooled (%) | -1.6470 | 1.8366 | ±3.6731 | -0.897 | 0.3698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **61**, R² = **0.1885**, Adj R² = **0.0063**, F-statistic = **1.03** (p = **0.4319**), Residual SE = **2.707** on **49** df, AIC = **305.2**, BIC = **330.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +11.4103 | 6.0959 | ±12.1919 | +1.872 | 0.0612 | . |
| Education: graduate level (vs college) | +0.0795 | 1.0103 | ±2.0205 | +0.079 | 0.9373 |  |
| Education: high school or below (vs college) | -4.0055 | 3.0012 | ±6.0024 | -1.335 | 0.1820 |  |
| Site: UCSD (vs UAB) | +0.8272 | 1.3679 | ±2.7359 | +0.605 | 0.5454 |  |
| Site: UW (vs UAB) | +1.1218 | 1.5626 | ±3.1253 | +0.718 | 0.4728 |  |
| Age (years) | +0.0076 | 0.0610 | ±0.1220 | +0.125 | 0.9007 |  |
| BMI (kg/m2) | +0.0326 | 0.0818 | ±0.1637 | +0.398 | 0.6906 |  |
| Hypertension | -0.7370 | 1.0121 | ±2.0241 | -0.728 | 0.4665 |  |
| High cholesterol | -0.0656 | 0.9523 | ±1.9046 | -0.069 | 0.9451 |  |
| Kidney disease | +0.9118 | 2.3015 | ±4.6030 | +0.396 | 0.6920 |  |
| Circulatory disease | -0.0960 | 1.0161 | ±2.0323 | -0.095 | 0.9247 |  |
| Avg. daily time 181-250 (%) | -0.6179 | 1.9520 | ±3.9041 | -0.317 | 0.7516 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **61**, R² = **0.2164**, Adj R² = **0.0404**, F-statistic = **1.23** (p = **0.2934**), Residual SE = **2.660** on **49** df, AIC = **303.1**, BIC = **328.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.3444** | 5.6512 | ±11.3024 | **+2.007** | **0.0447** | * |
| Education: graduate level (vs college) | +0.0120 | 0.9629 | ±1.9259 | +0.012 | 0.9901 |  |
| Education: high school or below (vs college) | -4.4070 | 2.9916 | ±5.9833 | -1.473 | 0.1407 |  |
| Site: UCSD (vs UAB) | +0.8092 | 1.2782 | ±2.5563 | +0.633 | 0.5267 |  |
| Site: UW (vs UAB) | +1.1196 | 1.4555 | ±2.9110 | +0.769 | 0.4418 |  |
| Age (years) | +0.0133 | 0.0581 | ±0.1161 | +0.229 | 0.8190 |  |
| BMI (kg/m2) | +0.0359 | 0.0787 | ±0.1574 | +0.456 | 0.6483 |  |
| Hypertension | -0.7396 | 0.9756 | ±1.9513 | -0.758 | 0.4484 |  |
| High cholesterol | +0.0029 | 0.9646 | ±1.9292 | +0.003 | 0.9976 |  |
| Kidney disease | +1.3465 | 2.3159 | ±4.6319 | +0.581 | 0.5610 |  |
| Circulatory disease | -0.2013 | 0.9826 | ±1.9651 | -0.205 | 0.8377 |  |
| Time > 180 (%) | -1.9261 | 1.9869 | ±3.9738 | -0.969 | 0.3323 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 61)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **61**, R² = **0.1930**, Adj R² = **0.0118**, F-statistic = **1.07** (p = **0.4076**), Residual SE = **2.699** on **49** df, AIC = **304.9**, BIC = **330.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +11.3499 | 6.1238 | ±12.2476 | +1.853 | 0.0638 | . |
| Education: graduate level (vs college) | +0.0622 | 1.0218 | ±2.0436 | +0.061 | 0.9514 |  |
| Education: high school or below (vs college) | -4.0778 | 2.9997 | ±5.9995 | -1.359 | 0.1740 |  |
| Site: UCSD (vs UAB) | +0.8304 | 1.3651 | ±2.7302 | +0.608 | 0.5430 |  |
| Site: UW (vs UAB) | +1.1145 | 1.5568 | ±3.1135 | +0.716 | 0.4740 |  |
| Age (years) | +0.0102 | 0.0626 | ±0.1253 | +0.163 | 0.8706 |  |
| BMI (kg/m2) | +0.0329 | 0.0816 | ±0.1633 | +0.403 | 0.6871 |  |
| Hypertension | -0.7426 | 1.0102 | ±2.0204 | -0.735 | 0.4623 |  |
| High cholesterol | -0.0756 | 0.9470 | ±1.8939 | -0.080 | 0.9364 |  |
| Kidney disease | +1.0181 | 2.2912 | ±4.5823 | +0.444 | 0.6568 |  |
| Circulatory disease | -0.1213 | 1.0199 | ±2.0398 | -0.119 | 0.9053 |  |
| Avg. daily time > 180 (%) | -0.9474 | 2.1766 | ±4.3533 | -0.435 | 0.6634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 61; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **61**, R² = **0.2226**, Adj R² = **0.0671**, F-statistic = **1.43** (p = **0.1943**), Residual SE = **5.569** on **50** df, AIC = **392.5**, BIC = **415.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.1432 | 8.0957 | ±16.1913 | +0.635 | 0.5252 |  |
| Education: graduate level (vs college) | -2.1151 | 1.7368 | ±3.4737 | -1.218 | 0.2233 |  |
| Education: high school or below (vs college) | +6.8963 | 5.8881 | ±11.7761 | +1.171 | 0.2415 |  |
| Site: UCSD (vs UAB) | +1.2167 | 1.9737 | ±3.9474 | +0.616 | 0.5376 |  |
| Site: UW (vs UAB) | +2.0298 | 2.4459 | ±4.8919 | +0.830 | 0.4066 |  |
| Age (years) | -0.0036 | 0.0899 | ±0.1797 | -0.040 | 0.9683 |  |
| BMI (kg/m2) | +0.0326 | 0.1402 | ±0.2804 | +0.233 | 0.8161 |  |
| Hypertension | +0.1610 | 1.7511 | ±3.5022 | +0.092 | 0.9268 |  |
| High cholesterol | +0.2873 | 1.6909 | ±3.3819 | +0.170 | 0.8651 |  |
| Kidney disease | +2.2120 | 5.6878 | ±11.3757 | +0.389 | 0.6973 |  |
| Circulatory disease | -2.7416 | 3.6962 | ±7.3923 | -0.742 | 0.4582 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **61**, R² = **0.2318**, Adj R² = **0.0593**, F-statistic = **1.34** (p = **0.2299**), Residual SE = **5.592** on **49** df, AIC = **393.7**, BIC = **419.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +14.4105 | 13.4260 | ±26.8520 | +1.073 | 0.2831 |  |
| Education: graduate level (vs college) | -2.3341 | 1.7926 | ±3.5852 | -1.302 | 0.1929 |  |
| Education: high school or below (vs college) | +7.8253 | 5.6712 | ±11.3424 | +1.380 | 0.1676 |  |
| Site: UCSD (vs UAB) | +1.3356 | 1.9868 | ±3.9737 | +0.672 | 0.5014 |  |
| Site: UW (vs UAB) | +2.1961 | 2.4911 | ±4.9822 | +0.882 | 0.3780 |  |
| Age (years) | +0.0004 | 0.0904 | ±0.1808 | +0.005 | 0.9962 |  |
| BMI (kg/m2) | +0.0390 | 0.1394 | ±0.2787 | +0.280 | 0.7794 |  |
| Hypertension | +0.3312 | 1.7724 | ±3.5448 | +0.187 | 0.8518 |  |
| High cholesterol | +0.4016 | 1.7650 | ±3.5301 | +0.228 | 0.8200 |  |
| Kidney disease | +1.8133 | 5.8147 | ±11.6294 | +0.312 | 0.7552 |  |
| Circulatory disease | -2.6934 | 3.6893 | ±7.3786 | -0.730 | 0.4654 |  |
| HbA1c (%) | -1.7490 | 2.3371 | ±4.6743 | -0.748 | 0.4542 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **61**, R² = **0.2269**, Adj R² = **0.0533**, F-statistic = **1.31** (p = **0.2490**), Residual SE = **5.609** on **49** df, AIC = **394.1**, BIC = **419.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0944 | 12.2910 | ±24.5820 | -0.089 | 0.9291 |  |
| Education: graduate level (vs college) | -2.0510 | 1.7027 | ±3.4054 | -1.205 | 0.2284 |  |
| Education: high school or below (vs college) | +7.0843 | 6.0435 | ±12.0870 | +1.172 | 0.2411 |  |
| Site: UCSD (vs UAB) | +1.2691 | 1.9837 | ±3.9673 | +0.640 | 0.5223 |  |
| Site: UW (vs UAB) | +2.0055 | 2.4664 | ±4.9328 | +0.813 | 0.4162 |  |
| Age (years) | -0.0066 | 0.0913 | ±0.1825 | -0.073 | 0.9420 |  |
| BMI (kg/m2) | +0.0383 | 0.1435 | ±0.2871 | +0.267 | 0.7894 |  |
| Hypertension | +0.1590 | 1.7772 | ±3.5543 | +0.089 | 0.9287 |  |
| High cholesterol | +0.3409 | 1.7185 | ±3.4370 | +0.198 | 0.8428 |  |
| Kidney disease | +2.1787 | 5.6579 | ±11.3158 | +0.385 | 0.7002 |  |
| Circulatory disease | -2.9643 | 3.7125 | ±7.4250 | -0.798 | 0.4246 |  |
| Mean glucose (mg/dL) | +0.0539 | 0.0853 | ±0.1705 | +0.632 | 0.5272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **61**, R² = **0.2269**, Adj R² = **0.0533**, F-statistic = **1.31** (p = **0.2490**), Residual SE = **5.609** on **49** df, AIC = **394.1**, BIC = **419.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -8.5546 | 22.4835 | ±44.9670 | -0.380 | 0.7036 |  |
| Education: graduate level (vs college) | -2.0510 | 1.7027 | ±3.4054 | -1.205 | 0.2284 |  |
| Education: high school or below (vs college) | +7.0843 | 6.0435 | ±12.0870 | +1.172 | 0.2411 |  |
| Site: UCSD (vs UAB) | +1.2691 | 1.9837 | ±3.9673 | +0.640 | 0.5223 |  |
| Site: UW (vs UAB) | +2.0055 | 2.4664 | ±4.9328 | +0.813 | 0.4162 |  |
| Age (years) | -0.0066 | 0.0913 | ±0.1825 | -0.073 | 0.9420 |  |
| BMI (kg/m2) | +0.0383 | 0.1435 | ±0.2871 | +0.267 | 0.7894 |  |
| Hypertension | +0.1590 | 1.7772 | ±3.5543 | +0.089 | 0.9287 |  |
| High cholesterol | +0.3409 | 1.7185 | ±3.4370 | +0.198 | 0.8428 |  |
| Kidney disease | +2.1787 | 5.6579 | ±11.3158 | +0.385 | 0.7002 |  |
| Circulatory disease | -2.9643 | 3.7125 | ±7.4250 | -0.798 | 0.4246 |  |
| GMI (%) | +2.2538 | 3.5645 | ±7.1290 | +0.632 | 0.5272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **61**, R² = **0.2504**, Adj R² = **0.0821**, F-statistic = **1.49** (p = **0.1665**), Residual SE = **5.523** on **49** df, AIC = **392.2**, BIC = **417.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -6.0990 | 13.5294 | ±27.0588 | -0.451 | 0.6521 |  |
| Education: graduate level (vs college) | -2.1041 | 1.6937 | ±3.3873 | -1.242 | 0.2141 |  |
| Education: high school or below (vs college) | +6.7850 | 6.0828 | ±12.1655 | +1.115 | 0.2647 |  |
| Site: UCSD (vs UAB) | +1.1930 | 1.9282 | ±3.8564 | +0.619 | 0.5361 |  |
| Site: UW (vs UAB) | +1.8374 | 2.4542 | ±4.9084 | +0.749 | 0.4541 |  |
| Age (years) | +0.0019 | 0.0912 | ±0.1824 | +0.021 | 0.9831 |  |
| BMI (kg/m2) | +0.0302 | 0.1541 | ±0.3082 | +0.196 | 0.8446 |  |
| Hypertension | -0.2145 | 1.7382 | ±3.4763 | -0.123 | 0.9018 |  |
| High cholesterol | +0.4703 | 1.7393 | ±3.4787 | +0.270 | 0.7869 |  |
| Kidney disease | +2.7994 | 5.2967 | ±10.5935 | +0.529 | 0.5971 |  |
| Circulatory disease | -3.0422 | 3.6575 | ±7.3150 | -0.832 | 0.4055 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0963 | 0.0735 | ±0.1471 | +1.309 | 0.1904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2288**, Adj R² = **0.0557**, F-statistic = **1.32** (p = **0.2414**), Residual SE = **5.602** on **49** df, AIC = **394.0**, BIC = **419.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.1723 | 8.8385 | ±17.6770 | +0.359 | 0.7197 |  |
| Education: graduate level (vs college) | -2.1308 | 1.7758 | ±3.5515 | -1.200 | 0.2302 |  |
| Education: high school or below (vs college) | +6.7951 | 6.3358 | ±12.6716 | +1.072 | 0.2835 |  |
| Site: UCSD (vs UAB) | +1.0207 | 2.0180 | ±4.0361 | +0.506 | 0.6130 |  |
| Site: UW (vs UAB) | +2.1144 | 2.5703 | ±5.1405 | +0.823 | 0.4107 |  |
| Age (years) | -0.0118 | 0.0914 | ±0.1829 | -0.129 | 0.8970 |  |
| BMI (kg/m2) | +0.0288 | 0.1538 | ±0.3075 | +0.187 | 0.8516 |  |
| Hypertension | -0.1708 | 1.6563 | ±3.3126 | -0.103 | 0.9179 |  |
| High cholesterol | +0.3116 | 1.7162 | ±3.4325 | +0.182 | 0.8559 |  |
| Kidney disease | +1.6200 | 6.6895 | ±13.3791 | +0.242 | 0.8087 |  |
| Circulatory disease | -2.7382 | 3.8315 | ±7.6629 | -0.715 | 0.4748 |  |
| Glucose SD, pooled (mg/dL) | +0.1701 | 0.3477 | ±0.6953 | +0.489 | 0.6247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2456**, Adj R² = **0.0763**, F-statistic = **1.45** (p = **0.1813**), Residual SE = **5.541** on **49** df, AIC = **392.6**, BIC = **418.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.5280 | 8.8897 | ±17.7794 | +0.284 | 0.7761 |  |
| Education: graduate level (vs college) | -2.1138 | 1.7129 | ±3.4257 | -1.234 | 0.2172 |  |
| Education: high school or below (vs college) | +6.7666 | 6.1906 | ±12.3811 | +1.093 | 0.2744 |  |
| Site: UCSD (vs UAB) | +0.6338 | 1.9324 | ±3.8649 | +0.328 | 0.7429 |  |
| Site: UW (vs UAB) | +2.0757 | 2.4584 | ±4.9168 | +0.844 | 0.3985 |  |
| Age (years) | -0.0307 | 0.0898 | ±0.1796 | -0.342 | 0.7324 |  |
| BMI (kg/m2) | +0.0215 | 0.1541 | ±0.3082 | +0.139 | 0.8892 |  |
| Hypertension | -0.5066 | 1.6819 | ±3.3638 | -0.301 | 0.7632 |  |
| High cholesterol | +0.3453 | 1.7050 | ±3.4100 | +0.203 | 0.8395 |  |
| Kidney disease | +1.0839 | 6.3480 | ±12.6960 | +0.171 | 0.8644 |  |
| Circulatory disease | -2.5928 | 3.7050 | ±7.4100 | -0.700 | 0.4840 |  |
| Avg. daily SD (mg/dL) | +0.3386 | 0.3316 | ±0.6632 | +1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **61**, R² = **0.2249**, Adj R² = **0.0508**, F-statistic = **1.29** (p = **0.2572**), Residual SE = **5.617** on **49** df, AIC = **394.3**, BIC = **419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.9077 | 8.8169 | ±17.6338 | +0.443 | 0.6576 |  |
| Education: graduate level (vs college) | -2.1418 | 1.8219 | ±3.6438 | -1.176 | 0.2398 |  |
| Education: high school or below (vs college) | +6.7977 | 6.1496 | ±12.2991 | +1.105 | 0.2690 |  |
| Site: UCSD (vs UAB) | +1.0841 | 2.0156 | ±4.0313 | +0.538 | 0.5907 |  |
| Site: UW (vs UAB) | +2.0890 | 2.5868 | ±5.1737 | +0.808 | 0.4194 |  |
| Age (years) | -0.0076 | 0.0912 | ±0.1824 | -0.084 | 0.9334 |  |
| BMI (kg/m2) | +0.0292 | 0.1499 | ±0.2997 | +0.195 | 0.8457 |  |
| Hypertension | -0.0356 | 1.6626 | ±3.3252 | -0.021 | 0.9829 |  |
| High cholesterol | +0.2829 | 1.7367 | ±3.4734 | +0.163 | 0.8706 |  |
| Kidney disease | +1.8368 | 6.5896 | ±13.1791 | +0.279 | 0.7804 |  |
| Circulatory disease | -2.6819 | 3.9332 | ±7.8663 | -0.682 | 0.4953 |  |
| CV (%) | +0.1204 | 0.3886 | ±0.7772 | +0.310 | 0.7566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **61**, R² = **0.2257**, Adj R² = **0.0518**, F-statistic = **1.30** (p = **0.2539**), Residual SE = **5.614** on **49** df, AIC = **394.2**, BIC = **419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.5644 | 10.9967 | ±21.9934 | +0.688 | 0.4915 |  |
| Education: graduate level (vs college) | -2.1283 | 1.7953 | ±3.5906 | -1.185 | 0.2358 |  |
| Education: high school or below (vs college) | +6.7418 | 6.1212 | ±12.2423 | +1.101 | 0.2707 |  |
| Site: UCSD (vs UAB) | +1.0874 | 2.0027 | ±4.0055 | +0.543 | 0.5871 |  |
| Site: UW (vs UAB) | +2.1188 | 2.5981 | ±5.1963 | +0.816 | 0.4148 |  |
| Age (years) | -0.0070 | 0.0907 | ±0.1813 | -0.077 | 0.9385 |  |
| BMI (kg/m2) | +0.0275 | 0.1507 | ±0.3014 | +0.182 | 0.8554 |  |
| Hypertension | -0.0341 | 1.6819 | ±3.3638 | -0.020 | 0.9838 |  |
| High cholesterol | +0.2798 | 1.7286 | ±3.4572 | +0.162 | 0.8714 |  |
| Kidney disease | +1.9088 | 6.2945 | ±12.5890 | +0.303 | 0.7617 |  |
| Circulatory disease | -2.6375 | 3.9453 | ±7.8907 | -0.668 | 0.5038 |  |
| Mean / SD ratio | -0.2682 | 0.6884 | ±1.3768 | -0.390 | 0.6969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **61**, R² = **0.2363**, Adj R² = **0.0648**, F-statistic = **1.38** (p = **0.2133**), Residual SE = **5.575** on **49** df, AIC = **393.4**, BIC = **418.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.2076 | 10.2178 | ±20.4357 | +0.999 | 0.3178 |  |
| Education: graduate level (vs college) | -2.1238 | 1.7835 | ±3.5671 | -1.191 | 0.2337 |  |
| Education: high school or below (vs college) | +6.5067 | 6.1275 | ±12.2549 | +1.062 | 0.2883 |  |
| Site: UCSD (vs UAB) | +0.8057 | 1.9996 | ±3.9992 | +0.403 | 0.6870 |  |
| Site: UW (vs UAB) | +2.1709 | 2.5426 | ±5.0853 | +0.854 | 0.3932 |  |
| Age (years) | -0.0197 | 0.0897 | ±0.1794 | -0.219 | 0.8266 |  |
| BMI (kg/m2) | +0.0230 | 0.1506 | ±0.3012 | +0.153 | 0.8784 |  |
| Hypertension | -0.3420 | 1.7363 | ±3.4727 | -0.197 | 0.8438 |  |
| High cholesterol | +0.2292 | 1.7325 | ±3.4649 | +0.132 | 0.8947 |  |
| Kidney disease | +1.7142 | 6.1443 | ±12.2886 | +0.279 | 0.7803 |  |
| Circulatory disease | -2.3308 | 3.9123 | ±7.8245 | -0.596 | 0.5513 |  |
| Avg. daily mean/SD | -0.4137 | 0.4856 | ±0.9712 | -0.852 | 0.3942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **61**, R² = **0.2340**, Adj R² = **0.0620**, F-statistic = **1.36** (p = **0.2217**), Residual SE = **5.584** on **49** df, AIC = **393.6**, BIC = **418.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3658 | 9.2429 | ±18.4857 | +0.364 | 0.7157 |  |
| Education: graduate level (vs college) | -2.1737 | 1.8083 | ±3.6166 | -1.202 | 0.2293 |  |
| Education: high school or below (vs college) | +6.4214 | 6.0126 | ±12.0251 | +1.068 | 0.2855 |  |
| Site: UCSD (vs UAB) | +0.9362 | 1.9400 | ±3.8800 | +0.483 | 0.6294 |  |
| Site: UW (vs UAB) | +1.9651 | 2.4357 | ±4.8714 | +0.807 | 0.4198 |  |
| Age (years) | -0.0203 | 0.0860 | ±0.1719 | -0.236 | 0.8137 |  |
| BMI (kg/m2) | +0.0086 | 0.1521 | ±0.3041 | +0.056 | 0.9550 |  |
| Hypertension | -0.0777 | 1.6848 | ±3.3697 | -0.046 | 0.9632 |  |
| High cholesterol | +0.3938 | 1.6654 | ±3.3309 | +0.236 | 0.8131 |  |
| Kidney disease | +2.4860 | 5.5327 | ±11.0654 | +0.449 | 0.6532 |  |
| Circulatory disease | -2.2519 | 4.1188 | ±8.2377 | -0.547 | 0.5846 |  |
| MAG (mg/dL/h) | +0.1110 | 0.1690 | ±0.3381 | +0.657 | 0.5114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **61**, R² = **0.2389**, Adj R² = **0.0681**, F-statistic = **1.40** (p = **0.2039**), Residual SE = **5.566** on **49** df, AIC = **393.2**, BIC = **418.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.0363 | 9.4933 | ±18.9866 | +0.214 | 0.8302 |  |
| Education: graduate level (vs college) | -2.0780 | 1.7079 | ±3.4159 | -1.217 | 0.2237 |  |
| Education: high school or below (vs college) | +6.5558 | 6.0433 | ±12.0867 | +1.085 | 0.2780 |  |
| Site: UCSD (vs UAB) | +0.8421 | 1.8981 | ±3.7962 | +0.444 | 0.6573 |  |
| Site: UW (vs UAB) | +2.0912 | 2.4900 | ±4.9800 | +0.840 | 0.4010 |  |
| Age (years) | -0.0293 | 0.0895 | ±0.1789 | -0.327 | 0.7434 |  |
| BMI (kg/m2) | +0.0284 | 0.1489 | ±0.2978 | +0.191 | 0.8486 |  |
| Hypertension | -0.1749 | 1.6731 | ±3.3461 | -0.105 | 0.9168 |  |
| High cholesterol | +0.2810 | 1.7370 | ±3.4740 | +0.162 | 0.8715 |  |
| Kidney disease | +1.7857 | 5.9169 | ±11.8338 | +0.302 | 0.7628 |  |
| Circulatory disease | -2.3918 | 3.8844 | ±7.7688 | -0.616 | 0.5381 |  |
| Avg. daily range (mg/dL) | +0.0652 | 0.0803 | ±0.1606 | +0.812 | 0.4167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **61**, R² = **0.2280**, Adj R² = **0.0547**, F-statistic = **1.32** (p = **0.2444**), Residual SE = **5.605** on **49** df, AIC = **394.0**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.0150 | 8.2722 | ±16.5445 | +0.848 | 0.3964 |  |
| Education: graduate level (vs college) | -2.1311 | 1.7918 | ±3.5836 | -1.189 | 0.2343 |  |
| Education: high school or below (vs college) | +6.9878 | 5.9745 | ±11.9489 | +1.170 | 0.2422 |  |
| Site: UCSD (vs UAB) | +1.1140 | 1.9389 | ±3.8779 | +0.575 | 0.5656 |  |
| Site: UW (vs UAB) | +1.9236 | 2.6392 | ±5.2784 | +0.729 | 0.4661 |  |
| Age (years) | -0.0142 | 0.0955 | ±0.1911 | -0.149 | 0.8817 |  |
| BMI (kg/m2) | +0.0240 | 0.1352 | ±0.2703 | +0.177 | 0.8591 |  |
| Hypertension | +0.2261 | 1.7338 | ±3.4677 | +0.130 | 0.8963 |  |
| High cholesterol | +0.3505 | 1.7748 | ±3.5496 | +0.197 | 0.8435 |  |
| Kidney disease | +2.7010 | 6.7968 | ±13.5936 | +0.397 | 0.6911 |  |
| Circulatory disease | -2.5382 | 3.6167 | ±7.2335 | -0.702 | 0.4828 |  |
| SD of daily means (mg/dL) | -0.1856 | 0.4424 | ±0.8848 | -0.420 | 0.6748 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **61**, R² = **0.2242**, Adj R² = **0.0501**, F-statistic = **1.29** (p = **0.2597**), Residual SE = **5.619** on **49** df, AIC = **394.3**, BIC = **419.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -71.6746 | 280.3807 | ±560.7615 | -0.256 | 0.7982 |  |
| Education: graduate level (vs college) | -2.1525 | 1.7572 | ±3.5145 | -1.225 | 0.2206 |  |
| Education: high school or below (vs college) | +6.7895 | 5.9169 | ±11.8338 | +1.147 | 0.2512 |  |
| Site: UCSD (vs UAB) | +1.2274 | 1.9874 | ±3.9748 | +0.618 | 0.5369 |  |
| Site: UW (vs UAB) | +2.0423 | 2.5935 | ±5.1871 | +0.787 | 0.4310 |  |
| Age (years) | -0.0020 | 0.0909 | ±0.1818 | -0.022 | 0.9824 |  |
| BMI (kg/m2) | +0.0376 | 0.1391 | ±0.2781 | +0.270 | 0.7868 |  |
| Hypertension | +0.2005 | 1.7604 | ±3.5209 | +0.114 | 0.9093 |  |
| High cholesterol | +0.3043 | 1.7834 | ±3.5668 | +0.171 | 0.8645 |  |
| Kidney disease | +2.3932 | 6.0506 | ±12.1013 | +0.396 | 0.6925 |  |
| Circulatory disease | -2.8898 | 4.2038 | ±8.4075 | -0.687 | 0.4918 |  |
| Time in range 70-180, pooled (%) | +0.7689 | 2.8274 | ±5.6548 | +0.272 | 0.7857 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **61**, R² = **0.2229**, Adj R² = **0.0484**, F-statistic = **1.28** (p = **0.2653**), Residual SE = **5.624** on **49** df, AIC = **394.4**, BIC = **419.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +38.5458 | 332.0928 | ±664.1857 | +0.116 | 0.9076 |  |
| Education: graduate level (vs college) | -2.0913 | 1.7128 | ±3.4256 | -1.221 | 0.2221 |  |
| Education: high school or below (vs college) | +6.9241 | 5.8893 | ±11.7786 | +1.176 | 0.2397 |  |
| Site: UCSD (vs UAB) | +1.1923 | 1.9793 | ±3.9585 | +0.602 | 0.5469 |  |
| Site: UW (vs UAB) | +2.0251 | 2.5949 | ±5.1898 | +0.780 | 0.4351 |  |
| Age (years) | -0.0068 | 0.0862 | ±0.1724 | -0.079 | 0.9373 |  |
| BMI (kg/m2) | +0.0309 | 0.1407 | ±0.2814 | +0.219 | 0.8264 |  |
| Hypertension | +0.1541 | 1.7741 | ±3.5481 | +0.087 | 0.9308 |  |
| High cholesterol | +0.2775 | 1.8192 | ±3.6384 | +0.153 | 0.8788 |  |
| Kidney disease | +2.1281 | 6.1488 | ±12.2976 | +0.346 | 0.7293 |  |
| Circulatory disease | -2.6855 | 4.2412 | ±8.4824 | -0.633 | 0.5266 |  |
| Avg. daily time in range 70-180 (%) | -0.3328 | 3.3282 | ±6.6564 | -0.100 | 0.9204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **61**, R² = **0.2344**, Adj R² = **0.0626**, F-statistic = **1.36** (p = **0.2200**), Residual SE = **5.582** on **49** df, AIC = **393.5**, BIC = **418.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.4984 | 8.8852 | ±17.7705 | +0.619 | 0.5360 |  |
| Education: graduate level (vs college) | -2.0850 | 1.8592 | ±3.7183 | -1.121 | 0.2621 |  |
| Education: high school or below (vs college) | +7.4532 | 6.8938 | ±13.7876 | +1.081 | 0.2796 |  |
| Site: UCSD (vs UAB) | +1.3282 | 1.9662 | ±3.9325 | +0.676 | 0.4993 |  |
| Site: UW (vs UAB) | +2.0781 | 2.6964 | ±5.3927 | +0.771 | 0.4409 |  |
| Age (years) | -0.0091 | 0.0976 | ±0.1953 | -0.093 | 0.9256 |  |
| BMI (kg/m2) | +0.0426 | 0.1458 | ±0.2916 | +0.292 | 0.7702 |  |
| Hypertension | +0.2877 | 1.8053 | ±3.6107 | +0.159 | 0.8734 |  |
| High cholesterol | +0.3024 | 1.7803 | ±3.5606 | +0.170 | 0.8651 |  |
| Kidney disease | +1.9525 | 6.3106 | ±12.6211 | +0.309 | 0.7570 |  |
| Circulatory disease | -3.0620 | 4.3668 | ±8.7337 | -0.701 | 0.4832 |  |
| Time 54-69, pooled (%) | -3.2878 | 5.4290 | ±10.8580 | -0.606 | 0.5448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **61**, R² = **0.2251**, Adj R² = **0.0511**, F-statistic = **1.29** (p = **0.2562**), Residual SE = **5.616** on **49** df, AIC = **394.3**, BIC = **419.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.9539 | 8.1940 | ±16.3880 | +0.605 | 0.5455 |  |
| Education: graduate level (vs college) | -2.1034 | 1.9154 | ±3.8308 | -1.098 | 0.2721 |  |
| Education: high school or below (vs college) | +7.1400 | 6.6033 | ±13.2066 | +1.081 | 0.2796 |  |
| Site: UCSD (vs UAB) | +1.2809 | 1.9855 | ±3.9709 | +0.645 | 0.5188 |  |
| Site: UW (vs UAB) | +2.0181 | 2.8151 | ±5.6303 | +0.717 | 0.4734 |  |
| Age (years) | -0.0010 | 0.0900 | ±0.1801 | -0.011 | 0.9914 |  |
| BMI (kg/m2) | +0.0381 | 0.1416 | ±0.2832 | +0.269 | 0.7877 |  |
| Hypertension | +0.1873 | 1.8008 | ±3.6015 | +0.104 | 0.9172 |  |
| High cholesterol | +0.3386 | 1.9221 | ±3.8441 | +0.176 | 0.8601 |  |
| Kidney disease | +2.1319 | 6.1254 | ±12.2508 | +0.348 | 0.7278 |  |
| Circulatory disease | -2.8772 | 4.4514 | ±8.9027 | -0.646 | 0.5180 |  |
| Avg. daily time 54-69 (%) | -1.6162 | 6.9138 | ±13.8276 | -0.234 | 0.8152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **61**, R² = **0.2414**, Adj R² = **0.0711**, F-statistic = **1.42** (p = **0.1954**), Residual SE = **5.557** on **49** df, AIC = **393.0**, BIC = **418.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +6.0318 | 9.1141 | ±18.2282 | +0.662 | 0.5081 |  |
| Education: graduate level (vs college) | -2.0785 | 1.8233 | ±3.6467 | -1.140 | 0.2543 |  |
| Education: high school or below (vs college) | +7.4087 | 6.7639 | ±13.5278 | +1.095 | 0.2734 |  |
| Site: UCSD (vs UAB) | +1.2518 | 1.9756 | ±3.9512 | +0.634 | 0.5263 |  |
| Site: UW (vs UAB) | +2.0622 | 2.6752 | ±5.3505 | +0.771 | 0.4408 |  |
| Age (years) | -0.0172 | 0.1001 | ±0.2001 | -0.172 | 0.8636 |  |
| BMI (kg/m2) | +0.0472 | 0.1470 | ±0.2941 | +0.321 | 0.7482 |  |
| Hypertension | +0.3418 | 1.8055 | ±3.6111 | +0.189 | 0.8499 |  |
| High cholesterol | +0.2437 | 1.7299 | ±3.4598 | +0.141 | 0.8880 |  |
| Kidney disease | +1.9062 | 6.2946 | ±12.5891 | +0.303 | 0.7620 |  |
| Circulatory disease | -3.1552 | 4.2640 | ±8.5281 | -0.740 | 0.4593 |  |
| Time < 70 (%) | -3.6592 | 4.1336 | ±8.2671 | -0.885 | 0.3760 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **61**, R² = **0.2267**, Adj R² = **0.0531**, F-statistic = **1.31** (p = **0.2499**), Residual SE = **5.610** on **49** df, AIC = **394.1**, BIC = **419.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.9652 | 8.3116 | ±16.6231 | +0.597 | 0.5503 |  |
| Education: graduate level (vs college) | -2.1257 | 1.8708 | ±3.7416 | -1.136 | 0.2559 |  |
| Education: high school or below (vs college) | +7.1637 | 6.5401 | ±13.0802 | +1.095 | 0.2734 |  |
| Site: UCSD (vs UAB) | +1.3002 | 1.9879 | ±3.9758 | +0.654 | 0.5131 |  |
| Site: UW (vs UAB) | +2.0382 | 2.7547 | ±5.5094 | +0.740 | 0.4594 |  |
| Age (years) | -0.0012 | 0.0911 | ±0.1822 | -0.013 | 0.9898 |  |
| BMI (kg/m2) | +0.0392 | 0.1430 | ±0.2860 | +0.274 | 0.7840 |  |
| Hypertension | +0.1997 | 1.7996 | ±3.5991 | +0.111 | 0.9117 |  |
| High cholesterol | +0.3719 | 1.9498 | ±3.8996 | +0.191 | 0.8487 |  |
| Kidney disease | +2.1134 | 6.1466 | ±12.2931 | +0.344 | 0.7310 |  |
| Circulatory disease | -2.9205 | 4.4259 | ±8.8517 | -0.660 | 0.5093 |  |
| Avg. daily time < 70 (%) | -1.9684 | 6.3136 | ±12.6273 | -0.312 | 0.7552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.2379**, Adj R² = **0.0668**, F-statistic = **1.39** (p = **0.2073**), Residual SE = **5.569** on **49** df, AIC = **393.3**, BIC = **418.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1059.2279 | 700.1632 | ±1400.3265 | -1.513 | 0.1303 |  |
| Education: graduate level (vs college) | -2.0345 | 1.7480 | ±3.4961 | -1.164 | 0.2445 |  |
| Education: high school or below (vs college) | +6.5835 | 5.9574 | ±11.9148 | +1.105 | 0.2691 |  |
| Site: UCSD (vs UAB) | +0.8474 | 2.0187 | ±4.0375 | +0.420 | 0.6746 |  |
| Site: UW (vs UAB) | +1.8023 | 2.4475 | ±4.8950 | +0.736 | 0.4615 |  |
| Age (years) | -0.0282 | 0.0926 | ±0.1852 | -0.304 | 0.7609 |  |
| BMI (kg/m2) | +0.0377 | 0.1436 | ±0.2872 | +0.262 | 0.7930 |  |
| Hypertension | +0.1839 | 1.7808 | ±3.5616 | +0.103 | 0.9178 |  |
| High cholesterol | +0.0244 | 1.7256 | ±3.4513 | +0.014 | 0.9887 |  |
| Kidney disease | +2.2684 | 5.6594 | ±11.3187 | +0.401 | 0.6886 |  |
| Circulatory disease | -2.9021 | 3.6965 | ±7.3929 | -0.785 | 0.4324 |  |
| Time 54-250, pooled (%) | +10.6633 | 7.0229 | ±14.0457 | +1.518 | 0.1289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **61**, R² = **0.2290**, Adj R² = **0.0559**, F-statistic = **1.32** (p = **0.2407**), Residual SE = **5.602** on **49** df, AIC = **394.0**, BIC = **419.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1543.3750 | 2520.4766 | ±5040.9532 | -0.612 | 0.5403 |  |
| Education: graduate level (vs college) | -2.1965 | 1.7822 | ±3.5643 | -1.232 | 0.2178 |  |
| Education: high school or below (vs college) | +6.6651 | 5.9260 | ±11.8521 | +1.125 | 0.2607 |  |
| Site: UCSD (vs UAB) | +1.0846 | 2.0255 | ±4.0510 | +0.535 | 0.5923 |  |
| Site: UW (vs UAB) | +1.9445 | 2.5392 | ±5.0783 | +0.766 | 0.4438 |  |
| Age (years) | -0.0142 | 0.0944 | ±0.1888 | -0.150 | 0.8806 |  |
| BMI (kg/m2) | +0.0235 | 0.1434 | ±0.2869 | +0.164 | 0.8699 |  |
| Hypertension | +0.0652 | 1.8077 | ±3.6155 | +0.036 | 0.9712 |  |
| High cholesterol | +0.3228 | 1.7568 | ±3.5136 | +0.184 | 0.8542 |  |
| Kidney disease | +2.3726 | 5.7305 | ±11.4610 | +0.414 | 0.6788 |  |
| Circulatory disease | -2.8403 | 3.7080 | ±7.4159 | -0.766 | 0.4437 |  |
| Avg. daily time 54-250 (%) | +15.4977 | 25.2216 | ±50.4433 | +0.614 | 0.5389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **61**, R² = **0.2271**, Adj R² = **0.0536**, F-statistic = **1.31** (p = **0.2481**), Residual SE = **5.609** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.4482 | 8.4729 | ±16.9458 | +0.643 | 0.5202 |  |
| Education: graduate level (vs college) | -2.0113 | 1.6639 | ±3.3277 | -1.209 | 0.2267 |  |
| Education: high school or below (vs college) | +7.3391 | 6.3383 | ±12.6766 | +1.158 | 0.2469 |  |
| Site: UCSD (vs UAB) | +1.1936 | 1.9889 | ±3.9778 | +0.600 | 0.5484 |  |
| Site: UW (vs UAB) | +1.9934 | 2.4593 | ±4.9186 | +0.811 | 0.4176 |  |
| Age (years) | -0.0131 | 0.0918 | ±0.1835 | -0.143 | 0.8862 |  |
| BMI (kg/m2) | +0.0279 | 0.1494 | ±0.2988 | +0.187 | 0.8520 |  |
| Hypertension | +0.1440 | 1.7927 | ±3.5854 | +0.080 | 0.9360 |  |
| High cholesterol | +0.2202 | 1.7750 | ±3.5499 | +0.124 | 0.9013 |  |
| Kidney disease | +1.7209 | 6.2856 | ±12.5712 | +0.274 | 0.7843 |  |
| Circulatory disease | -2.6140 | 3.8707 | ±7.7415 | -0.675 | 0.4995 |  |
| Time 181-250, pooled (%) | +1.5883 | 3.3756 | ±6.7512 | +0.471 | 0.6380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **61**, R² = **0.2273**, Adj R² = **0.0539**, F-statistic = **1.31** (p = **0.2471**), Residual SE = **5.608** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.6932 | 8.5842 | ±17.1685 | +0.663 | 0.5072 |  |
| Education: graduate level (vs college) | -1.9957 | 1.6239 | ±3.2478 | -1.229 | 0.2191 |  |
| Education: high school or below (vs college) | +7.2528 | 6.3172 | ±12.6344 | +1.148 | 0.2509 |  |
| Site: UCSD (vs UAB) | +1.1480 | 1.9837 | ±3.9674 | +0.579 | 0.5628 |  |
| Site: UW (vs UAB) | +1.9865 | 2.4623 | ±4.9246 | +0.807 | 0.4198 |  |
| Age (years) | -0.0178 | 0.0921 | ±0.1842 | -0.193 | 0.8472 |  |
| BMI (kg/m2) | +0.0287 | 0.1502 | ±0.3005 | +0.191 | 0.8487 |  |
| Hypertension | +0.1440 | 1.7896 | ±3.5792 | +0.080 | 0.9359 |  |
| High cholesterol | +0.2949 | 1.7282 | ±3.4564 | +0.171 | 0.8645 |  |
| Kidney disease | +1.7387 | 6.3148 | ±12.6297 | +0.275 | 0.7831 |  |
| Circulatory disease | -2.6144 | 3.9008 | ±7.8016 | -0.670 | 0.5027 |  |
| Avg. daily time 181-250 (%) | +1.6247 | 3.4632 | ±6.9263 | +0.469 | 0.6390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **61**, R² = **0.2272**, Adj R² = **0.0537**, F-statistic = **1.31** (p = **0.2476**), Residual SE = **5.608** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.3699 | 8.4333 | ±16.8665 | +0.637 | 0.5243 |  |
| Education: graduate level (vs college) | -2.0220 | 1.6702 | ±3.3404 | -1.211 | 0.2260 |  |
| Education: high school or below (vs college) | +7.3389 | 6.3146 | ±12.6292 | +1.162 | 0.2451 |  |
| Site: UCSD (vs UAB) | +1.2100 | 1.9904 | ±3.9807 | +0.608 | 0.5432 |  |
| Site: UW (vs UAB) | +2.0180 | 2.4692 | ±4.9384 | +0.817 | 0.4138 |  |
| Age (years) | -0.0127 | 0.0912 | ±0.1824 | -0.139 | 0.8893 |  |
| BMI (kg/m2) | +0.0286 | 0.1490 | ±0.2980 | +0.192 | 0.8476 |  |
| Hypertension | +0.1578 | 1.7934 | ±3.5868 | +0.088 | 0.9299 |  |
| High cholesterol | +0.2332 | 1.7626 | ±3.5252 | +0.132 | 0.8947 |  |
| Kidney disease | +1.7054 | 6.2875 | ±12.5749 | +0.271 | 0.7862 |  |
| Circulatory disease | -2.6150 | 3.8640 | ±7.7280 | -0.677 | 0.4986 |  |
| Time > 180 (%) | +1.5874 | 3.2718 | ±6.5436 | +0.485 | 0.6276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 61)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **61**, R² = **0.2275**, Adj R² = **0.0540**, F-statistic = **1.31** (p = **0.2466**), Residual SE = **5.607** on **49** df, AIC = **394.1**, BIC = **419.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.6016 | 8.5255 | ±17.0510 | +0.657 | 0.5112 |  |
| Education: graduate level (vs college) | -2.0086 | 1.6352 | ±3.2704 | -1.228 | 0.2193 |  |
| Education: high school or below (vs college) | +7.2497 | 6.2911 | ±12.5822 | +1.152 | 0.2492 |  |
| Site: UCSD (vs UAB) | +1.1667 | 1.9818 | ±3.9635 | +0.589 | 0.5560 |  |
| Site: UW (vs UAB) | +2.0142 | 2.4765 | ±4.9530 | +0.813 | 0.4160 |  |
| Age (years) | -0.0171 | 0.0912 | ±0.1824 | -0.188 | 0.8509 |  |
| BMI (kg/m2) | +0.0295 | 0.1498 | ±0.2995 | +0.197 | 0.8437 |  |
| Hypertension | +0.1595 | 1.7936 | ±3.5872 | +0.089 | 0.9292 |  |
| High cholesterol | +0.3092 | 1.7199 | ±3.4397 | +0.180 | 0.8573 |  |
| Kidney disease | +1.7253 | 6.3126 | ±12.6251 | +0.273 | 0.7846 |  |
| Circulatory disease | -2.6165 | 3.8913 | ±7.7826 | -0.672 | 0.5013 |  |
| Avg. daily time > 180 (%) | +1.6105 | 3.3380 | ±6.6760 | +0.482 | 0.6295 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 61; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **61**, events = **14**, McFadden pseudo-R² = **0.2203**, LLR χ² = **14.48** (p = **0.1523**), AUC = **0.7918**, AIC = **73.2**, BIC = **96.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0737 | 3.4742 | ±6.9484 | -0.309 | 0.7573 | 0.3418 |  |
| Education: graduate level (vs college) | -1.4373 | 0.9328 | ±1.8656 | -1.541 | 0.1234 | 0.2376 |  |
| **Education: high school or below (vs college)** | **+3.1891** | 1.5120 | ±3.0240 | **+2.109** | **0.0349** | 24.2668 | * |
| Site: UCSD (vs UAB) | -0.0642 | 0.9548 | ±1.9095 | -0.067 | 0.9464 | 0.9378 |  |
| Site: UW (vs UAB) | +1.2479 | 1.0258 | ±2.0516 | +1.217 | 0.2238 | 3.4829 |  |
| Age (years) | +0.0151 | 0.0418 | ±0.0835 | +0.361 | 0.7184 | 1.0152 |  |
| BMI (kg/m2) | -0.0339 | 0.0601 | ±0.1203 | -0.563 | 0.5731 | 0.9667 |  |
| Hypertension | +0.7195 | 0.8346 | ±1.6692 | +0.862 | 0.3887 | 2.0533 |  |
| High cholesterol | -0.8834 | 0.7722 | ±1.5445 | -1.144 | 0.2527 | 0.4134 |  |
| Kidney disease | +1.1169 | 2.5161 | ±5.0321 | +0.444 | 0.6571 | 3.0554 |  |
| Circulatory disease | -1.5827 | 1.4856 | ±2.9712 | -1.065 | 0.2867 | 0.2054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


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
