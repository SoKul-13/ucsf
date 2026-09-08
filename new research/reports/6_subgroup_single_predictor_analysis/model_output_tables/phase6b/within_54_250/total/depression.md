# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Total analysis base - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 889; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0733**, F-statistic = **8.03** (p = **1.79e-12**), Residual SE = **4.637** on **878** df, AIC = **5261.3**, BIC = **5314.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4156** | 1.2776 | ±2.5552 | **+6.587** | **4.49e-11** | *** |
| Education: graduate level (vs college) | -0.6325 | 0.3318 | ±0.6635 | -1.906 | 0.0566 | . |
| Education: high school or below (vs college) | +0.8848 | 0.6702 | ±1.3404 | +1.320 | 0.1868 |  |
| Site: UCSD (vs UAB) | -0.3348 | 0.4164 | ±0.8328 | -0.804 | 0.4213 |  |
| Site: UW (vs UAB) | +0.1650 | 0.4223 | ±0.8446 | +0.391 | 0.6959 |  |
| **Age (years)** | **-0.0867** | 0.0150 | ±0.0300 | **-5.774** | **7.76e-09** | *** |
| **BMI (kg/m2)** | **+0.0688** | 0.0250 | ±0.0500 | **+2.753** | **0.0059** | ** |
| Hypertension | +0.2493 | 0.3525 | ±0.7051 | +0.707 | 0.4795 |  |
| **High cholesterol** | **+0.7273** | 0.3274 | ±0.6548 | **+2.221** | **0.0263** | * |
| Kidney disease | +1.0851 | 0.6768 | ±1.3535 | +1.603 | 0.1089 |  |
| Circulatory disease | +0.7759 | 0.5319 | ±1.0638 | +1.459 | 0.1446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **889**, R² = **0.0844**, Adj R² = **0.0729**, F-statistic = **7.35** (p = **4.13e-12**), Residual SE = **4.638** on **877** df, AIC = **5262.8**, BIC = **5320.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9049** | 2.4324 | ±4.8647 | **+4.072** | **4.66e-05** | *** |
| Education: graduate level (vs college) | -0.6321 | 0.3321 | ±0.6642 | -1.903 | 0.0570 | . |
| Education: high school or below (vs college) | +0.8995 | 0.6728 | ±1.3457 | +1.337 | 0.1812 |  |
| Site: UCSD (vs UAB) | -0.3404 | 0.4171 | ±0.8343 | -0.816 | 0.4145 |  |
| Site: UW (vs UAB) | +0.1598 | 0.4240 | ±0.8480 | +0.377 | 0.7063 |  |
| **Age (years)** | **-0.0861** | 0.0151 | ±0.0303 | **-5.692** | **1.26e-08** | *** |
| **BMI (kg/m2)** | **+0.0721** | 0.0255 | ±0.0509 | **+2.831** | **0.0046** | ** |
| Hypertension | +0.2853 | 0.3577 | ±0.7154 | +0.798 | 0.4251 |  |
| **High cholesterol** | **+0.7604** | 0.3271 | ±0.6541 | **+2.325** | **0.0201** | * |
| Kidney disease | +1.0809 | 0.6776 | ±1.3552 | +1.595 | 0.1107 |  |
| Circulatory disease | +0.7961 | 0.5327 | ±1.0653 | +1.494 | 0.1351 |  |
| HbA1c (%) | -0.2907 | 0.4140 | ±0.8281 | -0.702 | 0.4827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **889**, R² = **0.0849**, Adj R² = **0.0734**, F-statistic = **7.40** (p = **3.27e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.3**, BIC = **5319.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9392** | 1.9121 | ±3.8243 | **+5.198** | **2.01e-07** | *** |
| Education: graduate level (vs college) | -0.6187 | 0.3329 | ±0.6657 | -1.859 | 0.0631 | . |
| Education: high school or below (vs college) | +0.8905 | 0.6692 | ±1.3385 | +1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | -0.3522 | 0.4152 | ±0.8303 | -0.848 | 0.3962 |  |
| Site: UW (vs UAB) | +0.1764 | 0.4233 | ±0.8465 | +0.417 | 0.6769 |  |
| **Age (years)** | **-0.0864** | 0.0150 | ±0.0301 | **-5.740** | **9.47e-09** | *** |
| **BMI (kg/m2)** | **+0.0719** | 0.0251 | ±0.0501 | **+2.867** | **0.0041** | ** |
| Hypertension | +0.2897 | 0.3555 | ±0.7110 | +0.815 | 0.4151 |  |
| **High cholesterol** | **+0.7331** | 0.3274 | ±0.6548 | **+2.239** | **0.0251** | * |
| Kidney disease | +1.1222 | 0.6736 | ±1.3472 | +1.666 | 0.0957 | . |
| Circulatory disease | +0.8069 | 0.5325 | ±1.0650 | +1.515 | 0.1297 |  |
| Mean glucose (mg/dL) | -0.0138 | 0.0133 | ±0.0266 | -1.036 | 0.3003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **889**, R² = **0.0849**, Adj R² = **0.0734**, F-statistic = **7.40** (p = **3.27e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.3**, BIC = **5319.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8451** | 3.5040 | ±7.0080 | **+3.380** | **7.24e-04** | *** |
| Education: graduate level (vs college) | -0.6187 | 0.3329 | ±0.6657 | -1.859 | 0.0631 | . |
| Education: high school or below (vs college) | +0.8905 | 0.6692 | ±1.3385 | +1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | -0.3522 | 0.4152 | ±0.8303 | -0.848 | 0.3962 |  |
| Site: UW (vs UAB) | +0.1764 | 0.4233 | ±0.8465 | +0.417 | 0.6769 |  |
| **Age (years)** | **-0.0864** | 0.0150 | ±0.0301 | **-5.740** | **9.47e-09** | *** |
| **BMI (kg/m2)** | **+0.0719** | 0.0251 | ±0.0501 | **+2.867** | **0.0041** | ** |
| Hypertension | +0.2897 | 0.3555 | ±0.7110 | +0.815 | 0.4151 |  |
| **High cholesterol** | **+0.7331** | 0.3274 | ±0.6548 | **+2.239** | **0.0251** | * |
| Kidney disease | +1.1222 | 0.6736 | ±1.3472 | +1.666 | 0.0957 | . |
| Circulatory disease | +0.8069 | 0.5325 | ±1.0650 | +1.515 | 0.1297 |  |
| GMI (%) | -0.5758 | 0.5559 | ±1.1119 | -1.036 | 0.3003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.29** (p = **5.21e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6581** | 1.8016 | ±3.6032 | **+4.806** | **1.54e-06** | *** |
| Education: graduate level (vs college) | -0.6306 | 0.3333 | ±0.6665 | -1.892 | 0.0585 | . |
| Education: high school or below (vs college) | +0.8857 | 0.6714 | ±1.3428 | +1.319 | 0.1871 |  |
| Site: UCSD (vs UAB) | -0.3351 | 0.4168 | ±0.8336 | -0.804 | 0.4214 |  |
| Site: UW (vs UAB) | +0.1677 | 0.4239 | ±0.8478 | +0.396 | 0.6923 |  |
| **Age (years)** | **-0.0869** | 0.0150 | ±0.0300 | **-5.788** | **7.14e-09** | *** |
| **BMI (kg/m2)** | **+0.0698** | 0.0255 | ±0.0510 | **+2.736** | **0.0062** | ** |
| Hypertension | +0.2539 | 0.3528 | ±0.7055 | +0.720 | 0.4717 |  |
| **High cholesterol** | **+0.7306** | 0.3279 | ±0.6557 | **+2.228** | **0.0259** | * |
| Kidney disease | +1.0877 | 0.6765 | ±1.3531 | +1.608 | 0.1079 |  |
| Circulatory disease | +0.7812 | 0.5339 | ±1.0678 | +1.463 | 0.1434 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0022 | 0.0122 | ±0.0244 | -0.181 | 0.8563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **889**, R² = **0.0840**, Adj R² = **0.0725**, F-statistic = **7.31** (p = **4.75e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7380** | 1.4133 | ±2.8266 | **+6.183** | **6.30e-10** | *** |
| Education: graduate level (vs college) | -0.6356 | 0.3317 | ±0.6634 | -1.916 | 0.0553 | . |
| Education: high school or below (vs college) | +0.9027 | 0.6738 | ±1.3476 | +1.340 | 0.1803 |  |
| Site: UCSD (vs UAB) | -0.3493 | 0.4163 | ±0.8326 | -0.839 | 0.4015 |  |
| Site: UW (vs UAB) | +0.1619 | 0.4226 | ±0.8452 | +0.383 | 0.7017 |  |
| **Age (years)** | **-0.0862** | 0.0151 | ±0.0301 | **-5.724** | **1.04e-08** | *** |
| **BMI (kg/m2)** | **+0.0694** | 0.0251 | ±0.0502 | **+2.767** | **0.0056** | ** |
| Hypertension | +0.2714 | 0.3571 | ±0.7142 | +0.760 | 0.4473 |  |
| **High cholesterol** | **+0.7304** | 0.3280 | ±0.6559 | **+2.227** | **0.0259** | * |
| Kidney disease | +1.1066 | 0.6760 | ±1.3519 | +1.637 | 0.1016 |  |
| Circulatory disease | +0.7840 | 0.5335 | ±1.0670 | +1.470 | 0.1416 |  |
| Glucose SD, pooled (mg/dL) | -0.0191 | 0.0383 | ±0.0765 | -0.498 | 0.6186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **889**, R² = **0.0842**, Adj R² = **0.0727**, F-statistic = **7.33** (p = **4.47e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.0**, BIC = **5320.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7841** | 1.3943 | ±2.7886 | **+6.300** | **2.98e-10** | *** |
| Education: graduate level (vs college) | -0.6341 | 0.3318 | ±0.6636 | -1.911 | 0.0560 | . |
| Education: high school or below (vs college) | +0.9043 | 0.6728 | ±1.3456 | +1.344 | 0.1789 |  |
| Site: UCSD (vs UAB) | -0.3515 | 0.4162 | ±0.8323 | -0.845 | 0.3983 |  |
| Site: UW (vs UAB) | +0.1632 | 0.4227 | ±0.8454 | +0.386 | 0.6994 |  |
| **Age (years)** | **-0.0861** | 0.0150 | ±0.0301 | **-5.719** | **1.07e-08** | *** |
| **BMI (kg/m2)** | **+0.0697** | 0.0251 | ±0.0502 | **+2.777** | **0.0055** | ** |
| Hypertension | +0.2777 | 0.3577 | ±0.7154 | +0.776 | 0.4376 |  |
| **High cholesterol** | **+0.7293** | 0.3278 | ±0.6556 | **+2.225** | **0.0261** | * |
| Kidney disease | +1.1095 | 0.6766 | ±1.3532 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.7827 | 0.5331 | ±1.0663 | +1.468 | 0.1421 |  |
| Avg. daily SD (mg/dL) | -0.0243 | 0.0389 | ±0.0779 | -0.624 | 0.5327 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.29** (p = **5.29e-12**), Residual SE = **4.640** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4152** | 1.4958 | ±2.9915 | **+5.626** | **1.84e-08** | *** |
| Education: graduate level (vs college) | -0.6325 | 0.3318 | ±0.6636 | -1.906 | 0.0566 | . |
| Education: high school or below (vs college) | +0.8848 | 0.6723 | ±1.3445 | +1.316 | 0.1881 |  |
| Site: UCSD (vs UAB) | -0.3348 | 0.4173 | ±0.8346 | -0.802 | 0.4224 |  |
| Site: UW (vs UAB) | +0.1650 | 0.4230 | ±0.8459 | +0.390 | 0.6964 |  |
| **Age (years)** | **-0.0867** | 0.0150 | ±0.0301 | **-5.767** | **8.08e-09** | *** |
| **BMI (kg/m2)** | **+0.0688** | 0.0250 | ±0.0500 | **+2.751** | **0.0059** | ** |
| Hypertension | +0.2492 | 0.3546 | ±0.7092 | +0.703 | 0.4821 |  |
| **High cholesterol** | **+0.7273** | 0.3279 | ±0.6557 | **+2.218** | **0.0265** | * |
| Kidney disease | +1.0850 | 0.6760 | ±1.3520 | +1.605 | 0.1085 |  |
| Circulatory disease | +0.7759 | 0.5325 | ±1.0651 | +1.457 | 0.1451 |  |
| CV (%) | +0.0000 | 0.0518 | ±0.1037 | +0.001 | 0.9996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.29** (p = **5.27e-12**), Residual SE = **4.640** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5012** | 1.5676 | ±3.1352 | **+5.423** | **5.86e-08** | *** |
| Education: graduate level (vs college) | -0.6306 | 0.3320 | ±0.6640 | -1.900 | 0.0575 | . |
| Education: high school or below (vs college) | +0.8815 | 0.6717 | ±1.3434 | +1.312 | 0.1894 |  |
| Site: UCSD (vs UAB) | -0.3331 | 0.4171 | ±0.8342 | -0.799 | 0.4245 |  |
| Site: UW (vs UAB) | +0.1655 | 0.4227 | ±0.8454 | +0.392 | 0.6953 |  |
| **Age (years)** | **-0.0868** | 0.0151 | ±0.0301 | **-5.763** | **8.28e-09** | *** |
| **BMI (kg/m2)** | **+0.0688** | 0.0250 | ±0.0501 | **+2.750** | **0.0060** | ** |
| Hypertension | +0.2464 | 0.3538 | ±0.7075 | +0.697 | 0.4861 |  |
| **High cholesterol** | **+0.7272** | 0.3278 | ±0.6556 | **+2.218** | **0.0265** | * |
| Kidney disease | +1.0822 | 0.6756 | ±1.3512 | +1.602 | 0.1092 |  |
| Circulatory disease | +0.7762 | 0.5323 | ±1.0645 | +1.458 | 0.1447 |  |
| Mean / SD ratio | -0.0128 | 0.1279 | ±0.2559 | -0.100 | 0.9204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **889**, R² = **0.0839**, Adj R² = **0.0724**, F-statistic = **7.30** (p = **5.06e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.2**, BIC = **5320.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1441** | 1.5639 | ±3.1278 | **+5.207** | **1.91e-07** | *** |
| Education: graduate level (vs college) | -0.6375 | 0.3315 | ±0.6630 | -1.923 | 0.0545 | . |
| Education: high school or below (vs college) | +0.8940 | 0.6711 | ±1.3421 | +1.332 | 0.1828 |  |
| Site: UCSD (vs UAB) | -0.3396 | 0.4169 | ±0.8338 | -0.815 | 0.4153 |  |
| Site: UW (vs UAB) | +0.1646 | 0.4228 | ±0.8457 | +0.389 | 0.6970 |  |
| **Age (years)** | **-0.0864** | 0.0151 | ±0.0301 | **-5.739** | **9.51e-09** | *** |
| **BMI (kg/m2)** | **+0.0690** | 0.0251 | ±0.0501 | **+2.751** | **0.0059** | ** |
| Hypertension | +0.2581 | 0.3546 | ±0.7092 | +0.728 | 0.4667 |  |
| **High cholesterol** | **+0.7268** | 0.3278 | ±0.6556 | **+2.217** | **0.0266** | * |
| Kidney disease | +1.0942 | 0.6773 | ±1.3545 | +1.616 | 0.1062 |  |
| Circulatory disease | +0.7719 | 0.5312 | ±1.0624 | +1.453 | 0.1462 |  |
| Avg. daily mean/SD | +0.0345 | 0.1079 | ±0.2158 | +0.320 | 0.7488 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **889**, R² = **0.0858**, Adj R² = **0.0743**, F-statistic = **7.48** (p = **2.28e-12**), Residual SE = **4.635** on **877** df, AIC = **5261.4**, BIC = **5318.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2244** | 1.4567 | ±2.9133 | **+4.960** | **7.06e-07** | *** |
| Education: graduate level (vs college) | -0.6338 | 0.3321 | ±0.6642 | -1.908 | 0.0563 | . |
| Education: high school or below (vs college) | +0.8312 | 0.6725 | ±1.3449 | +1.236 | 0.2165 |  |
| Site: UCSD (vs UAB) | -0.3219 | 0.4156 | ±0.8312 | -0.775 | 0.4386 |  |
| Site: UW (vs UAB) | +0.1791 | 0.4217 | ±0.8434 | +0.425 | 0.6710 |  |
| **Age (years)** | **-0.0863** | 0.0150 | ±0.0300 | **-5.744** | **9.25e-09** | *** |
| **BMI (kg/m2)** | **+0.0689** | 0.0249 | ±0.0498 | **+2.766** | **0.0057** | ** |
| Hypertension | +0.2587 | 0.3532 | ±0.7064 | +0.733 | 0.4639 |  |
| **High cholesterol** | **+0.7251** | 0.3277 | ±0.6554 | **+2.213** | **0.0269** | * |
| Kidney disease | +1.0607 | 0.6740 | ±1.3480 | +1.574 | 0.1155 |  |
| Circulatory disease | +0.7901 | 0.5335 | ±1.0669 | +1.481 | 0.1386 |  |
| MAG (mg/dL/h) | +0.0321 | 0.0229 | ±0.0458 | +1.405 | 0.1602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.30** (p = **5.15e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6073** | 1.4558 | ±2.9115 | **+5.913** | **3.37e-09** | *** |
| Education: graduate level (vs college) | -0.6318 | 0.3323 | ±0.6646 | -1.902 | 0.0572 | . |
| Education: high school or below (vs college) | +0.8931 | 0.6724 | ±1.3449 | +1.328 | 0.1841 |  |
| Site: UCSD (vs UAB) | -0.3398 | 0.4166 | ±0.8332 | -0.816 | 0.4147 |  |
| Site: UW (vs UAB) | +0.1647 | 0.4227 | ±0.8454 | +0.390 | 0.6969 |  |
| **Age (years)** | **-0.0865** | 0.0151 | ±0.0302 | **-5.737** | **9.66e-09** | *** |
| **BMI (kg/m2)** | **+0.0686** | 0.0250 | ±0.0501 | **+2.743** | **0.0061** | ** |
| Hypertension | +0.2565 | 0.3551 | ±0.7101 | +0.722 | 0.4701 |  |
| **High cholesterol** | **+0.7274** | 0.3278 | ±0.6555 | **+2.219** | **0.0265** | * |
| Kidney disease | +1.0931 | 0.6755 | ±1.3510 | +1.618 | 0.1056 |  |
| Circulatory disease | +0.7784 | 0.5330 | ±1.0659 | +1.461 | 0.1441 |  |
| Avg. daily range (mg/dL) | -0.0022 | 0.0089 | ±0.0178 | -0.251 | 0.8016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **889**, R² = **0.0840**, Adj R² = **0.0725**, F-statistic = **7.31** (p = **4.83e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2661** | 1.2950 | ±2.5900 | **+6.383** | **1.74e-10** | *** |
| Education: graduate level (vs college) | -0.6321 | 0.3319 | ±0.6639 | -1.904 | 0.0569 | . |
| Education: high school or below (vs college) | +0.8691 | 0.6769 | ±1.3538 | +1.284 | 0.1992 |  |
| Site: UCSD (vs UAB) | -0.3250 | 0.4180 | ±0.8359 | -0.778 | 0.4368 |  |
| Site: UW (vs UAB) | +0.1698 | 0.4228 | ±0.8457 | +0.402 | 0.6880 |  |
| **Age (years)** | **-0.0867** | 0.0150 | ±0.0301 | **-5.764** | **8.20e-09** | *** |
| **BMI (kg/m2)** | **+0.0678** | 0.0252 | ±0.0504 | **+2.693** | **0.0071** | ** |
| Hypertension | +0.2498 | 0.3528 | ±0.7057 | +0.708 | 0.4790 |  |
| **High cholesterol** | **+0.7147** | 0.3309 | ±0.6618 | **+2.160** | **0.0308** | * |
| Kidney disease | +1.0754 | 0.6749 | ±1.3498 | +1.593 | 0.1111 |  |
| Circulatory disease | +0.7585 | 0.5310 | ±1.0620 | +1.428 | 0.1532 |  |
| SD of daily means (mg/dL) | +0.0303 | 0.0668 | ±0.1337 | +0.453 | 0.6504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **889**, R² = **0.0850**, Adj R² = **0.0735**, F-statistic = **7.41** (p = **3.13e-12**), Residual SE = **4.636** on **877** df, AIC = **5262.2**, BIC = **5319.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3326 | 5.1609 | ±10.3218 | +0.646 | 0.5185 |  |
| Education: graduate level (vs college) | -0.6268 | 0.3318 | ±0.6636 | -1.889 | 0.0589 | . |
| Education: high school or below (vs college) | +0.9013 | 0.6712 | ±1.3424 | +1.343 | 0.1793 |  |
| Site: UCSD (vs UAB) | -0.3653 | 0.4145 | ±0.8289 | -0.881 | 0.3781 |  |
| Site: UW (vs UAB) | +0.1572 | 0.4221 | ±0.8443 | +0.372 | 0.7095 |  |
| **Age (years)** | **-0.0859** | 0.0150 | ±0.0301 | **-5.715** | **1.10e-08** | *** |
| **BMI (kg/m2)** | **+0.0704** | 0.0250 | ±0.0500 | **+2.817** | **0.0049** | ** |
| Hypertension | +0.2756 | 0.3562 | ±0.7123 | +0.774 | 0.4390 |  |
| **High cholesterol** | **+0.7447** | 0.3273 | ±0.6547 | **+2.275** | **0.0229** | * |
| Kidney disease | +1.1358 | 0.6744 | ±1.3488 | +1.684 | 0.0921 | . |
| Circulatory disease | +0.8106 | 0.5337 | ±1.0674 | +1.519 | 0.1288 |  |
| Time in range 70-180, pooled (%) | +0.0509 | 0.0499 | ±0.0998 | +1.020 | 0.3075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **889**, R² = **0.0854**, Adj R² = **0.0739**, F-statistic = **7.44** (p = **2.66e-12**), Residual SE = **4.636** on **877** df, AIC = **5261.8**, BIC = **5319.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.4705 | 5.1861 | ±10.3722 | +0.476 | 0.6338 |  |
| Education: graduate level (vs college) | -0.6269 | 0.3317 | ±0.6634 | -1.890 | 0.0588 | . |
| Education: high school or below (vs college) | +0.8985 | 0.6708 | ±1.3417 | +1.339 | 0.1805 |  |
| Site: UCSD (vs UAB) | -0.3699 | 0.4144 | ±0.8289 | -0.893 | 0.3721 |  |
| Site: UW (vs UAB) | +0.1563 | 0.4220 | ±0.8440 | +0.370 | 0.7111 |  |
| **Age (years)** | **-0.0858** | 0.0150 | ±0.0301 | **-5.714** | **1.11e-08** | *** |
| **BMI (kg/m2)** | **+0.0708** | 0.0250 | ±0.0500 | **+2.831** | **0.0046** | ** |
| Hypertension | +0.2791 | 0.3560 | ±0.7120 | +0.784 | 0.4331 |  |
| **High cholesterol** | **+0.7480** | 0.3273 | ±0.6546 | **+2.286** | **0.0223** | * |
| Kidney disease | +1.1460 | 0.6742 | ±1.3484 | +1.700 | 0.0892 | . |
| Circulatory disease | +0.8178 | 0.5336 | ±1.0672 | +1.533 | 0.1254 |  |
| Avg. daily time in range 70-180 (%) | +0.0595 | 0.0502 | ±0.1003 | +1.186 | 0.2355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **889**, R² = **0.0842**, Adj R² = **0.0727**, F-statistic = **7.33** (p = **4.51e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.0**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4667** | 1.2806 | ±2.5612 | **+6.611** | **3.81e-11** | *** |
| Education: graduate level (vs college) | -0.6480 | 0.3339 | ±0.6679 | -1.940 | 0.0523 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6718 | ±1.3435 | +1.297 | 0.1947 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.4164 | ±0.8327 | -0.788 | 0.4305 |  |
| Site: UW (vs UAB) | +0.1609 | 0.4224 | ±0.8448 | +0.381 | 0.7033 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0300 | **-5.766** | **8.11e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.736** | **0.0062** | ** |
| Hypertension | +0.2463 | 0.3528 | ±0.7056 | +0.698 | 0.4851 |  |
| **High cholesterol** | **+0.7330** | 0.3278 | ±0.6556 | **+2.236** | **0.0254** | * |
| Kidney disease | +1.0777 | 0.6791 | ±1.3583 | +1.587 | 0.1126 |  |
| Circulatory disease | +0.7705 | 0.5314 | ±1.0628 | +1.450 | 0.1470 |  |
| Time 54-69, pooled (%) | -0.1954 | 0.3012 | ±0.6023 | -0.649 | 0.5164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **889**, R² = **0.0841**, Adj R² = **0.0726**, F-statistic = **7.32** (p = **4.66e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4544** | 1.2798 | ±2.5596 | **+6.606** | **3.95e-11** | *** |
| Education: graduate level (vs college) | -0.6468 | 0.3336 | ±0.6673 | -1.939 | 0.0525 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6720 | ±1.3439 | +1.296 | 0.1948 |  |
| Site: UCSD (vs UAB) | -0.3252 | 0.4160 | ±0.8321 | -0.782 | 0.4344 |  |
| Site: UW (vs UAB) | +0.1627 | 0.4224 | ±0.8449 | +0.385 | 0.7002 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0301 | **-5.760** | **8.41e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.737** | **0.0062** | ** |
| Hypertension | +0.2466 | 0.3528 | ±0.7056 | +0.699 | 0.4845 |  |
| **High cholesterol** | **+0.7318** | 0.3279 | ±0.6558 | **+2.232** | **0.0256** | * |
| Kidney disease | +1.0782 | 0.6789 | ±1.3578 | +1.588 | 0.1123 |  |
| Circulatory disease | +0.7685 | 0.5318 | ±1.0636 | +1.445 | 0.1485 |  |
| Avg. daily time 54-69 (%) | -0.1679 | 0.3019 | ±0.6039 | -0.556 | 0.5781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **889**, R² = **0.0842**, Adj R² = **0.0727**, F-statistic = **7.33** (p = **4.51e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.0**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4667** | 1.2806 | ±2.5612 | **+6.611** | **3.81e-11** | *** |
| Education: graduate level (vs college) | -0.6480 | 0.3339 | ±0.6679 | -1.940 | 0.0523 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6718 | ±1.3435 | +1.297 | 0.1947 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.4164 | ±0.8327 | -0.788 | 0.4305 |  |
| Site: UW (vs UAB) | +0.1609 | 0.4224 | ±0.8448 | +0.381 | 0.7033 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0300 | **-5.766** | **8.11e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.736** | **0.0062** | ** |
| Hypertension | +0.2463 | 0.3528 | ±0.7056 | +0.698 | 0.4851 |  |
| **High cholesterol** | **+0.7330** | 0.3278 | ±0.6556 | **+2.236** | **0.0254** | * |
| Kidney disease | +1.0777 | 0.6791 | ±1.3583 | +1.587 | 0.1126 |  |
| Circulatory disease | +0.7705 | 0.5314 | ±1.0628 | +1.450 | 0.1470 |  |
| Time < 70 (%) | -0.1954 | 0.3012 | ±0.6023 | -0.649 | 0.5164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **889**, R² = **0.0841**, Adj R² = **0.0726**, F-statistic = **7.32** (p = **4.66e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4544** | 1.2798 | ±2.5596 | **+6.606** | **3.95e-11** | *** |
| Education: graduate level (vs college) | -0.6468 | 0.3336 | ±0.6673 | -1.939 | 0.0525 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6720 | ±1.3439 | +1.296 | 0.1948 |  |
| Site: UCSD (vs UAB) | -0.3252 | 0.4160 | ±0.8321 | -0.782 | 0.4344 |  |
| Site: UW (vs UAB) | +0.1627 | 0.4224 | ±0.8449 | +0.385 | 0.7002 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0301 | **-5.760** | **8.41e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.737** | **0.0062** | ** |
| Hypertension | +0.2466 | 0.3528 | ±0.7056 | +0.699 | 0.4845 |  |
| **High cholesterol** | **+0.7318** | 0.3279 | ±0.6558 | **+2.232** | **0.0256** | * |
| Kidney disease | +1.0782 | 0.6789 | ±1.3578 | +1.588 | 0.1123 |  |
| Circulatory disease | +0.7685 | 0.5318 | ±1.0636 | +1.445 | 0.1485 |  |
| Avg. daily time < 70 (%) | -0.1679 | 0.3019 | ±0.6039 | -0.556 | 0.5781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **889**, R² = **0.0848**, Adj R² = **0.0733**, F-statistic = **7.39** (p = **3.42e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.4**, BIC = **5319.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4113** | 1.2769 | ±2.5538 | **+6.587** | **4.48e-11** | *** |
| Education: graduate level (vs college) | -0.6237 | 0.3321 | ±0.6642 | -1.878 | 0.0604 | . |
| Education: high school or below (vs college) | +0.9030 | 0.6715 | ±1.3431 | +1.345 | 0.1787 |  |
| Site: UCSD (vs UAB) | -0.3640 | 0.4145 | ±0.8290 | -0.878 | 0.3799 |  |
| Site: UW (vs UAB) | +0.1590 | 0.4222 | ±0.8445 | +0.376 | 0.7066 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0301 | **-5.721** | **1.06e-08** | *** |
| **BMI (kg/m2)** | **+0.0704** | 0.0250 | ±0.0500 | **+2.813** | **0.0049** | ** |
| Hypertension | +0.2738 | 0.3561 | ±0.7123 | +0.769 | 0.4419 |  |
| **High cholesterol** | **+0.7417** | 0.3274 | ±0.6547 | **+2.266** | **0.0235** | * |
| Kidney disease | +1.1327 | 0.6750 | ±1.3499 | +1.678 | 0.0933 | . |
| Circulatory disease | +0.8086 | 0.5341 | ±1.0681 | +1.514 | 0.1300 |  |
| Time 181-250, pooled (%) | -0.0461 | 0.0495 | ±0.0990 | -0.931 | 0.3520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **889**, R² = **0.0852**, Adj R² = **0.0737**, F-statistic = **7.42** (p = **2.93e-12**), Residual SE = **4.636** on **877** df, AIC = **5262.0**, BIC = **5319.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4089** | 1.2769 | ±2.5538 | **+6.585** | **4.54e-11** | *** |
| Education: graduate level (vs college) | -0.6227 | 0.3319 | ±0.6639 | -1.876 | 0.0607 | . |
| Education: high school or below (vs college) | +0.9018 | 0.6711 | ±1.3421 | +1.344 | 0.1790 |  |
| Site: UCSD (vs UAB) | -0.3702 | 0.4144 | ±0.8289 | -0.893 | 0.3717 |  |
| Site: UW (vs UAB) | +0.1578 | 0.4221 | ±0.8441 | +0.374 | 0.7085 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0300 | **-5.722** | **1.05e-08** | *** |
| **BMI (kg/m2)** | **+0.0707** | 0.0250 | ±0.0500 | **+2.828** | **0.0047** | ** |
| Hypertension | +0.2775 | 0.3560 | ±0.7119 | +0.780 | 0.4357 |  |
| **High cholesterol** | **+0.7448** | 0.3273 | ±0.6546 | **+2.276** | **0.0229** | * |
| Kidney disease | +1.1432 | 0.6748 | ±1.3496 | +1.694 | 0.0902 | . |
| Circulatory disease | +0.8168 | 0.5341 | ±1.0682 | +1.529 | 0.1262 |  |
| Avg. daily time 181-250 (%) | -0.0547 | 0.0498 | ±0.0995 | -1.099 | 0.2719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **889**, R² = **0.0848**, Adj R² = **0.0733**, F-statistic = **7.39** (p = **3.42e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.4**, BIC = **5319.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4113** | 1.2769 | ±2.5538 | **+6.587** | **4.48e-11** | *** |
| Education: graduate level (vs college) | -0.6237 | 0.3321 | ±0.6642 | -1.878 | 0.0604 | . |
| Education: high school or below (vs college) | +0.9030 | 0.6715 | ±1.3431 | +1.345 | 0.1787 |  |
| Site: UCSD (vs UAB) | -0.3640 | 0.4145 | ±0.8290 | -0.878 | 0.3799 |  |
| Site: UW (vs UAB) | +0.1590 | 0.4222 | ±0.8445 | +0.376 | 0.7066 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0301 | **-5.721** | **1.06e-08** | *** |
| **BMI (kg/m2)** | **+0.0704** | 0.0250 | ±0.0500 | **+2.813** | **0.0049** | ** |
| Hypertension | +0.2738 | 0.3561 | ±0.7123 | +0.769 | 0.4419 |  |
| **High cholesterol** | **+0.7417** | 0.3274 | ±0.6547 | **+2.266** | **0.0235** | * |
| Kidney disease | +1.1327 | 0.6750 | ±1.3499 | +1.678 | 0.0933 | . |
| Circulatory disease | +0.8086 | 0.5341 | ±1.0681 | +1.514 | 0.1300 |  |
| Time > 180 (%) | -0.0461 | 0.0495 | ±0.0990 | -0.931 | 0.3520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **889**, R² = **0.0852**, Adj R² = **0.0737**, F-statistic = **7.42** (p = **2.93e-12**), Residual SE = **4.636** on **877** df, AIC = **5262.0**, BIC = **5319.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4089** | 1.2769 | ±2.5538 | **+6.585** | **4.54e-11** | *** |
| Education: graduate level (vs college) | -0.6227 | 0.3319 | ±0.6639 | -1.876 | 0.0607 | . |
| Education: high school or below (vs college) | +0.9018 | 0.6711 | ±1.3421 | +1.344 | 0.1790 |  |
| Site: UCSD (vs UAB) | -0.3702 | 0.4144 | ±0.8289 | -0.893 | 0.3717 |  |
| Site: UW (vs UAB) | +0.1578 | 0.4221 | ±0.8441 | +0.374 | 0.7085 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0300 | **-5.722** | **1.05e-08** | *** |
| **BMI (kg/m2)** | **+0.0707** | 0.0250 | ±0.0500 | **+2.828** | **0.0047** | ** |
| Hypertension | +0.2775 | 0.3560 | ±0.7119 | +0.780 | 0.4357 |  |
| **High cholesterol** | **+0.7448** | 0.3273 | ±0.6546 | **+2.276** | **0.0229** | * |
| Kidney disease | +1.1432 | 0.6748 | ±1.3496 | +1.694 | 0.0902 | . |
| Circulatory disease | +0.8168 | 0.5341 | ±1.0682 | +1.529 | 0.1262 |  |
| Avg. daily time > 180 (%) | -0.0547 | 0.0498 | ±0.0995 | -1.099 | 0.2719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **889**, R² = **0.0858**, Adj R² = **0.0744**, F-statistic = **7.49** (p = **2.19e-12**), Residual SE = **4.634** on **877** df, AIC = **5261.3**, BIC = **5318.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4470** | 1.2799 | ±2.5598 | **+6.600** | **4.12e-11** | *** |
| Education: graduate level (vs college) | -0.6300 | 0.3317 | ±0.6634 | -1.899 | 0.0575 | . |
| Education: high school or below (vs college) | +0.8313 | 0.6773 | ±1.3546 | +1.227 | 0.2197 |  |
| Site: UCSD (vs UAB) | -0.2936 | 0.4172 | ±0.8344 | -0.704 | 0.4815 |  |
| Site: UW (vs UAB) | +0.1805 | 0.4221 | ±0.8442 | +0.428 | 0.6689 |  |
| **Age (years)** | **-0.0861** | 0.0151 | ±0.0302 | **-5.708** | **1.14e-08** | *** |
| **BMI (kg/m2)** | **+0.0643** | 0.0252 | ±0.0504 | **+2.550** | **0.0108** | * |
| Hypertension | +0.2580 | 0.3528 | ±0.7057 | +0.731 | 0.4646 |  |
| **High cholesterol** | **+0.6817** | 0.3290 | ±0.6581 | **+2.072** | **0.0383** | * |
| Kidney disease | +1.0359 | 0.6858 | ±1.3715 | +1.511 | 0.1309 |  |
| Circulatory disease | +0.7405 | 0.5372 | ±1.0744 | +1.379 | 0.1680 |  |
| Nocturnal time > 180 (%) | +0.0603 | 0.0514 | ±0.1029 | +1.173 | 0.2409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 889; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.79** (p = **3.46e-08**), AUC = **0.6769**, AIC = **789.9**, BIC = **842.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2484 | 0.7192 | ±1.4383 | -0.345 | 0.7298 | 0.7800 |  |
| Education: graduate level (vs college) | -0.1145 | 0.2033 | ±0.4066 | -0.563 | 0.5734 | 0.8918 |  |
| Education: high school or below (vs college) | +0.4034 | 0.2851 | ±0.5702 | +1.415 | 0.1571 | 1.4969 |  |
| Site: UCSD (vs UAB) | -0.0951 | 0.2475 | ±0.4951 | -0.384 | 0.7009 | 0.9093 |  |
| Site: UW (vs UAB) | +0.2127 | 0.2324 | ±0.4648 | +0.915 | 0.3600 | 1.2370 |  |
| **Age (years)** | **-0.0450** | 0.0092 | ±0.0184 | **-4.888** | **1.02e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0287** | 0.0128 | ±0.0256 | **+2.244** | **0.0248** | 1.0291 | * |
| Hypertension | +0.1567 | 0.2039 | ±0.4078 | +0.769 | 0.4421 | 1.1696 |  |
| **High cholesterol** | **+0.5100** | 0.1932 | ±0.3863 | **+2.640** | **0.0083** | 1.6653 | ** |
| Kidney disease | +0.5648 | 0.3035 | ±0.6069 | +1.861 | 0.0627 | 1.7591 | . |
| Circulatory disease | +0.2961 | 0.2678 | ±0.5356 | +1.106 | 0.2688 | 1.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.08** (p = **7.50e-08**), AUC = **0.6776**, AIC = **791.6**, BIC = **849.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3687 | 1.3558 | ±2.7116 | +0.272 | 0.7857 | 1.4458 |  |
| Education: graduate level (vs college) | -0.1157 | 0.2034 | ±0.4068 | -0.569 | 0.5695 | 0.8907 |  |
| Education: high school or below (vs college) | +0.4087 | 0.2853 | ±0.5706 | +1.432 | 0.1521 | 1.5048 |  |
| Site: UCSD (vs UAB) | -0.1008 | 0.2477 | ±0.4953 | -0.407 | 0.6840 | 0.9041 |  |
| Site: UW (vs UAB) | +0.2118 | 0.2322 | ±0.4644 | +0.912 | 0.3617 | 1.2359 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.872** | **1.10e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0301** | 0.0130 | ±0.0260 | **+2.314** | **0.0206** | 1.0305 | * |
| Hypertension | +0.1746 | 0.2065 | ±0.4130 | +0.846 | 0.3978 | 1.1908 |  |
| **High cholesterol** | **+0.5264** | 0.1957 | ±0.3913 | **+2.690** | **0.0071** | 1.6927 | ** |
| Kidney disease | +0.5643 | 0.3037 | ±0.6075 | +1.858 | 0.0632 | 1.7582 | . |
| Circulatory disease | +0.3064 | 0.2682 | ±0.5364 | +1.142 | 0.2533 | 1.3585 |  |
| HbA1c (%) | -0.1198 | 0.2234 | ±0.4468 | -0.536 | 0.5918 | 0.8871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0672**, LLR χ² = **55.30** (p = **6.82e-08**), AUC = **0.6783**, AIC = **791.4**, BIC = **848.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8575 | 1.1111 | ±2.2223 | -0.772 | 0.4403 | 0.4242 |  |
| Education: graduate level (vs college) | -0.1186 | 0.2035 | ±0.4071 | -0.583 | 0.5601 | 0.8882 |  |
| Education: high school or below (vs college) | +0.4050 | 0.2848 | ±0.5696 | +1.422 | 0.1550 | 1.4994 |  |
| Site: UCSD (vs UAB) | -0.0859 | 0.2480 | ±0.4959 | -0.346 | 0.7290 | 0.9177 |  |
| Site: UW (vs UAB) | +0.2080 | 0.2325 | ±0.4649 | +0.895 | 0.3708 | 1.2313 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0184 | **-4.901** | **9.55e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0275** | 0.0129 | ±0.0258 | **+2.126** | **0.0335** | 1.0279 | * |
| Hypertension | +0.1425 | 0.2048 | ±0.4096 | +0.696 | 0.4864 | 1.1532 |  |
| **High cholesterol** | **+0.5037** | 0.1933 | ±0.3866 | **+2.606** | **0.0092** | 1.6548 | ** |
| Kidney disease | +0.5487 | 0.3041 | ±0.6082 | +1.804 | 0.0712 | 1.7310 | . |
| Circulatory disease | +0.2833 | 0.2686 | ±0.5372 | +1.055 | 0.2915 | 1.3275 |  |
| Mean glucose (mg/dL) | +0.0055 | 0.0076 | ±0.0152 | +0.720 | 0.4716 | 1.0055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0672**, LLR χ² = **55.30** (p = **6.82e-08**), AUC = **0.6783**, AIC = **791.4**, BIC = **848.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6158 | 2.0315 | ±4.0631 | -0.795 | 0.4264 | 0.1987 |  |
| Education: graduate level (vs college) | -0.1186 | 0.2035 | ±0.4071 | -0.583 | 0.5601 | 0.8882 |  |
| Education: high school or below (vs college) | +0.4050 | 0.2848 | ±0.5696 | +1.422 | 0.1550 | 1.4994 |  |
| Site: UCSD (vs UAB) | -0.0859 | 0.2480 | ±0.4959 | -0.346 | 0.7290 | 0.9177 |  |
| Site: UW (vs UAB) | +0.2080 | 0.2325 | ±0.4649 | +0.895 | 0.3708 | 1.2313 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0184 | **-4.901** | **9.55e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0275** | 0.0129 | ±0.0258 | **+2.126** | **0.0335** | 1.0279 | * |
| Hypertension | +0.1425 | 0.2048 | ±0.4096 | +0.696 | 0.4864 | 1.1532 |  |
| **High cholesterol** | **+0.5037** | 0.1933 | ±0.3866 | **+2.606** | **0.0092** | 1.6548 | ** |
| Kidney disease | +0.5487 | 0.3041 | ±0.6082 | +1.804 | 0.0712 | 1.7310 | . |
| Circulatory disease | +0.2833 | 0.2686 | ±0.5372 | +1.055 | 0.2915 | 1.3275 |  |
| GMI (%) | +0.2291 | 0.3183 | ±0.6366 | +0.720 | 0.4716 | 1.2575 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0716**, LLR χ² = **58.94** (p = **1.46e-08**), AUC = **0.6858**, AIC = **787.8**, BIC = **845.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.7767 | 1.0417 | ±2.0834 | -1.706 | 0.0881 | 0.1692 | . |
| Education: graduate level (vs college) | -0.1237 | 0.2041 | ±0.4081 | -0.606 | 0.5444 | 0.8836 |  |
| Education: high school or below (vs college) | +0.4058 | 0.2852 | ±0.5703 | +1.423 | 0.1547 | 1.5005 |  |
| Site: UCSD (vs UAB) | -0.0867 | 0.2482 | ±0.4964 | -0.349 | 0.7268 | 0.9169 |  |
| Site: UW (vs UAB) | +0.1968 | 0.2330 | ±0.4659 | +0.845 | 0.3983 | 1.2175 |  |
| **Age (years)** | **-0.0442** | 0.0092 | ±0.0185 | **-4.785** | **1.71e-06** | 0.9568 | *** |
| BMI (kg/m2) | +0.0235 | 0.0133 | ±0.0265 | +1.769 | 0.0770 | 1.0238 | . |
| Hypertension | +0.1301 | 0.2042 | ±0.4085 | +0.637 | 0.5242 | 1.1389 |  |
| **High cholesterol** | **+0.4839** | 0.1938 | ±0.3877 | **+2.496** | **0.0126** | 1.6224 | * |
| Kidney disease | +0.5523 | 0.3036 | ±0.6071 | +1.819 | 0.0689 | 1.7372 | . |
| Circulatory disease | +0.2625 | 0.2693 | ±0.5385 | +0.975 | 0.3295 | 1.3002 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0137** | 0.0067 | ±0.0134 | **+2.045** | **0.0409** | 1.0138 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.80** (p = **8.44e-08**), AUC = **0.6773**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2872 | 0.8182 | ±1.6364 | -0.351 | 0.7256 | 0.7504 |  |
| Education: graduate level (vs college) | -0.1141 | 0.2033 | ±0.4067 | -0.561 | 0.5746 | 0.8921 |  |
| Education: high school or below (vs college) | +0.4013 | 0.2859 | ±0.5718 | +1.404 | 0.1604 | 1.4938 |  |
| Site: UCSD (vs UAB) | -0.0927 | 0.2487 | ±0.4975 | -0.373 | 0.7095 | 0.9115 |  |
| Site: UW (vs UAB) | +0.2137 | 0.2326 | ±0.4653 | +0.919 | 0.3583 | 1.2383 |  |
| **Age (years)** | **-0.0451** | 0.0092 | ±0.0185 | **-4.885** | **1.04e-06** | 0.9559 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0128 | ±0.0256 | **+2.235** | **0.0254** | 1.0290 | * |
| Hypertension | +0.1542 | 0.2055 | ±0.4109 | +0.750 | 0.4530 | 1.1667 |  |
| **High cholesterol** | **+0.5091** | 0.1933 | ±0.3867 | **+2.633** | **0.0085** | 1.6639 | ** |
| Kidney disease | +0.5622 | 0.3045 | ±0.6091 | +1.846 | 0.0649 | 1.7545 | . |
| Circulatory disease | +0.2953 | 0.2679 | ±0.5358 | +1.102 | 0.2704 | 1.3435 |  |
| Glucose SD, pooled (mg/dL) | +0.0023 | 0.0228 | ±0.0455 | +0.099 | 0.9208 | 1.0023 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.80** (p = **8.44e-08**), AUC = **0.6772**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2839 | 0.8024 | ±1.6049 | -0.354 | 0.7235 | 0.7529 |  |
| Education: graduate level (vs college) | -0.1143 | 0.2033 | ±0.4066 | -0.562 | 0.5739 | 0.8920 |  |
| Education: high school or below (vs college) | +0.4016 | 0.2857 | ±0.5713 | +1.406 | 0.1598 | 1.4942 |  |
| Site: UCSD (vs UAB) | -0.0930 | 0.2484 | ±0.4968 | -0.374 | 0.7081 | 0.9112 |  |
| Site: UW (vs UAB) | +0.2133 | 0.2325 | ±0.4649 | +0.917 | 0.3589 | 1.2377 |  |
| **Age (years)** | **-0.0451** | 0.0092 | ±0.0185 | **-4.884** | **1.04e-06** | 0.9559 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0128 | ±0.0256 | **+2.233** | **0.0255** | 1.0290 | * |
| Hypertension | +0.1541 | 0.2056 | ±0.4111 | +0.750 | 0.4535 | 1.1666 |  |
| **High cholesterol** | **+0.5094** | 0.1932 | ±0.3865 | **+2.636** | **0.0084** | 1.6643 | ** |
| Kidney disease | +0.5624 | 0.3044 | ±0.6088 | +1.848 | 0.0647 | 1.7549 | . |
| Circulatory disease | +0.2957 | 0.2678 | ±0.5356 | +1.104 | 0.2695 | 1.3441 |  |
| Avg. daily SD (mg/dL) | +0.0023 | 0.0233 | ±0.0465 | +0.100 | 0.9206 | 1.0023 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.87** (p = **8.20e-08**), AUC = **0.6761**, AIC = **791.9**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1063 | 0.8795 | ±1.7590 | -0.121 | 0.9038 | 0.8991 |  |
| Education: graduate level (vs college) | -0.1170 | 0.2035 | ±0.4070 | -0.575 | 0.5655 | 0.8896 |  |
| Education: high school or below (vs college) | +0.4106 | 0.2863 | ±0.5726 | +1.434 | 0.1515 | 1.5078 |  |
| Site: UCSD (vs UAB) | -0.1011 | 0.2484 | ±0.4968 | -0.407 | 0.6841 | 0.9039 |  |
| Site: UW (vs UAB) | +0.2084 | 0.2328 | ±0.4656 | +0.895 | 0.3707 | 1.2317 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0185 | **-4.861** | **1.17e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0128 | ±0.0256 | **+2.241** | **0.0250** | 1.0291 | * |
| Hypertension | +0.1620 | 0.2047 | ±0.4095 | +0.791 | 0.4287 | 1.1759 |  |
| **High cholesterol** | **+0.5111** | 0.1932 | ±0.3864 | **+2.645** | **0.0082** | 1.6670 | ** |
| Kidney disease | +0.5699 | 0.3041 | ±0.6081 | +1.874 | 0.0609 | 1.7681 | . |
| Circulatory disease | +0.2957 | 0.2678 | ±0.5356 | +1.104 | 0.2695 | 1.3440 |  |
| CV (%) | -0.0092 | 0.0326 | ±0.0653 | -0.281 | 0.7791 | 0.9909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.79** (p = **8.45e-08**), AUC = **0.6768**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2882 | 0.9010 | ±1.8021 | -0.320 | 0.7491 | 0.7496 |  |
| Education: graduate level (vs college) | -0.1153 | 0.2036 | ±0.4072 | -0.566 | 0.5713 | 0.8911 |  |
| Education: high school or below (vs college) | +0.4052 | 0.2861 | ±0.5723 | +1.416 | 0.1568 | 1.4995 |  |
| Site: UCSD (vs UAB) | -0.0962 | 0.2480 | ±0.4960 | -0.388 | 0.6981 | 0.9083 |  |
| Site: UW (vs UAB) | +0.2119 | 0.2326 | ±0.4652 | +0.911 | 0.3623 | 1.2360 |  |
| **Age (years)** | **-0.0450** | 0.0092 | ±0.0185 | **-4.875** | **1.09e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0287** | 0.0128 | ±0.0256 | **+2.244** | **0.0248** | 1.0291 | * |
| Hypertension | +0.1580 | 0.2047 | ±0.4094 | +0.772 | 0.4401 | 1.1712 |  |
| **High cholesterol** | **+0.5102** | 0.1932 | ±0.3864 | **+2.641** | **0.0083** | 1.6656 | ** |
| Kidney disease | +0.5661 | 0.3040 | ±0.6080 | +1.862 | 0.0626 | 1.7614 | . |
| Circulatory disease | +0.2957 | 0.2678 | ±0.5357 | +1.104 | 0.2695 | 1.3441 |  |
| Mean / SD ratio | +0.0060 | 0.0814 | ±0.1629 | +0.073 | 0.9416 | 1.0060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.85** (p = **8.26e-08**), AUC = **0.6765**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3751 | 0.8809 | ±1.7617 | -0.426 | 0.6702 | 0.6872 |  |
| Education: graduate level (vs college) | -0.1167 | 0.2035 | ±0.4071 | -0.574 | 0.5662 | 0.8898 |  |
| Education: high school or below (vs college) | +0.4083 | 0.2858 | ±0.5716 | +1.429 | 0.1531 | 1.5043 |  |
| Site: UCSD (vs UAB) | -0.0977 | 0.2477 | ±0.4955 | -0.394 | 0.6934 | 0.9070 |  |
| Site: UW (vs UAB) | +0.2113 | 0.2324 | ±0.4648 | +0.909 | 0.3633 | 1.2353 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0185 | **-4.858** | **1.19e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0287** | 0.0128 | ±0.0256 | **+2.249** | **0.0245** | 1.0292 | * |
| Hypertension | +0.1608 | 0.2045 | ±0.4090 | +0.786 | 0.4318 | 1.1744 |  |
| **High cholesterol** | **+0.5100** | 0.1931 | ±0.3863 | **+2.641** | **0.0083** | 1.6653 | ** |
| Kidney disease | +0.5691 | 0.3040 | ±0.6079 | +1.872 | 0.0612 | 1.7668 | . |
| Circulatory disease | +0.2932 | 0.2681 | ±0.5361 | +1.094 | 0.2740 | 1.3407 |  |
| Avg. daily mean/SD | +0.0161 | 0.0645 | ±0.1291 | +0.249 | 0.8031 | 1.0162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0705**, LLR χ² = **58.00** (p = **2.18e-08**), AUC = **0.6862**, AIC = **788.7**, BIC = **846.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1547 | 0.8835 | ±1.7670 | -1.307 | 0.1912 | 0.3151 |  |
| Education: graduate level (vs college) | -0.1093 | 0.2039 | ±0.4078 | -0.536 | 0.5919 | 0.8965 |  |
| Education: high school or below (vs college) | +0.3673 | 0.2866 | ±0.5732 | +1.282 | 0.1999 | 1.4439 |  |
| Site: UCSD (vs UAB) | -0.0813 | 0.2483 | ±0.4966 | -0.327 | 0.7435 | 0.9220 |  |
| Site: UW (vs UAB) | +0.2224 | 0.2328 | ±0.4656 | +0.955 | 0.3394 | 1.2490 |  |
| **Age (years)** | **-0.0448** | 0.0092 | ±0.0185 | **-4.852** | **1.22e-06** | 0.9562 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0129 | ±0.0258 | **+2.218** | **0.0265** | 1.0290 | * |
| Hypertension | +0.1637 | 0.2043 | ±0.4085 | +0.802 | 0.4228 | 1.1779 |  |
| **High cholesterol** | **+0.5155** | 0.1940 | ±0.3880 | **+2.657** | **0.0079** | 1.6745 | ** |
| Kidney disease | +0.5489 | 0.3041 | ±0.6082 | +1.805 | 0.0711 | 1.7313 | . |
| Circulatory disease | +0.3102 | 0.2685 | ±0.5370 | +1.155 | 0.2479 | 1.3637 |  |
| MAG (mg/dL/h) | +0.0242 | 0.0135 | ±0.0269 | +1.797 | 0.0723 | 1.0245 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.90** (p = **8.09e-08**), AUC = **0.6774**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4055 | 0.8602 | ±1.7204 | -0.471 | 0.6374 | 0.6666 |  |
| Education: graduate level (vs college) | -0.1150 | 0.2034 | ±0.4067 | -0.565 | 0.5717 | 0.8914 |  |
| Education: high school or below (vs college) | +0.3967 | 0.2858 | ±0.5715 | +1.388 | 0.1651 | 1.4869 |  |
| Site: UCSD (vs UAB) | -0.0889 | 0.2483 | ±0.4965 | -0.358 | 0.7202 | 0.9149 |  |
| Site: UW (vs UAB) | +0.2143 | 0.2325 | ±0.4650 | +0.922 | 0.3566 | 1.2390 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0185 | **-4.899** | **9.65e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0288** | 0.0128 | ±0.0256 | **+2.253** | **0.0243** | 1.0292 | * |
| Hypertension | +0.1510 | 0.2046 | ±0.4093 | +0.738 | 0.4606 | 1.1630 |  |
| **High cholesterol** | **+0.5092** | 0.1932 | ±0.3864 | **+2.635** | **0.0084** | 1.6639 | ** |
| Kidney disease | +0.5572 | 0.3043 | ±0.6086 | +1.831 | 0.0671 | 1.7457 | . |
| Circulatory disease | +0.2947 | 0.2679 | ±0.5357 | +1.100 | 0.2713 | 1.3427 |  |
| Avg. daily range (mg/dL) | +0.0018 | 0.0055 | ±0.0111 | +0.333 | 0.7392 | 1.0018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0673**, LLR χ² = **55.33** (p = **6.73e-08**), AUC = **0.6791**, AIC = **791.4**, BIC = **848.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4057 | 0.7505 | ±1.5010 | -0.541 | 0.5888 | 0.6665 |  |
| Education: graduate level (vs college) | -0.1106 | 0.2036 | ±0.4071 | -0.543 | 0.5870 | 0.8953 |  |
| Education: high school or below (vs college) | +0.3902 | 0.2858 | ±0.5715 | +1.366 | 0.1721 | 1.4773 |  |
| Site: UCSD (vs UAB) | -0.0812 | 0.2486 | ±0.4972 | -0.327 | 0.7440 | 0.9220 |  |
| Site: UW (vs UAB) | +0.2231 | 0.2333 | ±0.4667 | +0.956 | 0.3390 | 1.2499 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.873** | **1.10e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0279** | 0.0129 | ±0.0257 | **+2.169** | **0.0301** | 1.0283 | * |
| Hypertension | +0.1577 | 0.2040 | ±0.4080 | +0.773 | 0.4395 | 1.1708 |  |
| **High cholesterol** | **+0.4948** | 0.1942 | ±0.3884 | **+2.548** | **0.0108** | 1.6402 | * |
| Kidney disease | +0.5575 | 0.3035 | ±0.6070 | +1.837 | 0.0662 | 1.7463 | . |
| Circulatory disease | +0.2800 | 0.2690 | ±0.5379 | +1.041 | 0.2978 | 1.3231 |  |
| SD of daily means (mg/dL) | +0.0284 | 0.0382 | ±0.0764 | +0.742 | 0.4579 | 1.0288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.01** (p = **7.73e-08**), AUC = **0.6776**, AIC = **791.7**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.9472 | 2.6383 | ±5.2765 | +0.359 | 0.7196 | 2.5785 |  |
| Education: graduate level (vs college) | -0.1171 | 0.2035 | ±0.4070 | -0.575 | 0.5650 | 0.8895 |  |
| Education: high school or below (vs college) | +0.4003 | 0.2850 | ±0.5699 | +1.405 | 0.1601 | 1.4923 |  |
| Site: UCSD (vs UAB) | -0.0855 | 0.2484 | ±0.4968 | -0.344 | 0.7308 | 0.9181 |  |
| Site: UW (vs UAB) | +0.2158 | 0.2325 | ±0.4651 | +0.928 | 0.3533 | 1.2409 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.905** | **9.33e-07** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.202** | **0.0276** | 1.0287 | * |
| Hypertension | +0.1530 | 0.2040 | ±0.4080 | +0.750 | 0.4532 | 1.1654 |  |
| **High cholesterol** | **+0.5032** | 0.1936 | ±0.3873 | **+2.599** | **0.0094** | 1.6540 | ** |
| Kidney disease | +0.5532 | 0.3043 | ±0.6087 | +1.818 | 0.0691 | 1.7388 | . |
| Circulatory disease | +0.2873 | 0.2686 | ±0.5372 | +1.069 | 0.2849 | 1.3328 |  |
| Time in range 70-180, pooled (%) | -0.0119 | 0.0253 | ±0.0506 | -0.471 | 0.6374 | 0.9882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.93** (p = **7.99e-08**), AUC = **0.6776**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7414 | 2.7140 | ±5.4280 | +0.273 | 0.7847 | 2.0989 |  |
| Education: graduate level (vs college) | -0.1162 | 0.2034 | ±0.4069 | -0.571 | 0.5677 | 0.8903 |  |
| Education: high school or below (vs college) | +0.4018 | 0.2849 | ±0.5699 | +1.410 | 0.1585 | 1.4946 |  |
| Site: UCSD (vs UAB) | -0.0875 | 0.2484 | ±0.4967 | -0.352 | 0.7247 | 0.9163 |  |
| Site: UW (vs UAB) | +0.2150 | 0.2325 | ±0.4650 | +0.925 | 0.3552 | 1.2398 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.900** | **9.60e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.208** | **0.0273** | 1.0287 | * |
| Hypertension | +0.1536 | 0.2040 | ±0.4080 | +0.753 | 0.4514 | 1.1661 |  |
| **High cholesterol** | **+0.5044** | 0.1937 | ±0.3873 | **+2.605** | **0.0092** | 1.6560 | ** |
| Kidney disease | +0.5548 | 0.3045 | ±0.6090 | +1.822 | 0.0684 | 1.7416 | . |
| Circulatory disease | +0.2887 | 0.2686 | ±0.5372 | +1.075 | 0.2824 | 1.3347 |  |
| Avg. daily time in range 70-180 (%) | -0.0099 | 0.0261 | ±0.0521 | -0.378 | 0.7051 | 0.9902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.92** (p = **8.01e-08**), AUC = **0.6762**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2296 | 0.7209 | ±1.4418 | -0.318 | 0.7501 | 0.7949 |  |
| Education: graduate level (vs college) | -0.1187 | 0.2036 | ±0.4072 | -0.583 | 0.5600 | 0.8881 |  |
| Education: high school or below (vs college) | +0.3999 | 0.2852 | ±0.5704 | +1.402 | 0.1608 | 1.4917 |  |
| Site: UCSD (vs UAB) | -0.0938 | 0.2476 | ±0.4952 | -0.379 | 0.7049 | 0.9105 |  |
| Site: UW (vs UAB) | +0.2095 | 0.2325 | ±0.4649 | +0.901 | 0.3675 | 1.2331 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.879** | **1.07e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.229** | **0.0258** | 1.0289 | * |
| Hypertension | +0.1546 | 0.2039 | ±0.4077 | +0.758 | 0.4482 | 1.1672 |  |
| **High cholesterol** | **+0.5114** | 0.1932 | ±0.3863 | **+2.648** | **0.0081** | 1.6677 | ** |
| Kidney disease | +0.5610 | 0.3037 | ±0.6073 | +1.848 | 0.0647 | 1.7525 | . |
| Circulatory disease | +0.2958 | 0.2678 | ±0.5356 | +1.105 | 0.2693 | 1.3442 |  |
| Time 54-69, pooled (%) | -0.0802 | 0.2242 | ±0.4483 | -0.358 | 0.7206 | 0.9230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.88** (p = **8.15e-08**), AUC = **0.6766**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2351 | 0.7204 | ±1.4408 | -0.326 | 0.7441 | 0.7905 |  |
| Education: graduate level (vs college) | -0.1181 | 0.2036 | ±0.4073 | -0.580 | 0.5619 | 0.8886 |  |
| Education: high school or below (vs college) | +0.4001 | 0.2852 | ±0.5705 | +1.403 | 0.1607 | 1.4919 |  |
| Site: UCSD (vs UAB) | -0.0923 | 0.2477 | ±0.4954 | -0.373 | 0.7094 | 0.9118 |  |
| Site: UW (vs UAB) | +0.2107 | 0.2324 | ±0.4648 | +0.907 | 0.3646 | 1.2345 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.877** | **1.08e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.231** | **0.0257** | 1.0289 | * |
| Hypertension | +0.1550 | 0.2039 | ±0.4078 | +0.760 | 0.4470 | 1.1677 |  |
| **High cholesterol** | **+0.5109** | 0.1931 | ±0.3863 | **+2.645** | **0.0082** | 1.6668 | ** |
| Kidney disease | +0.5614 | 0.3037 | ±0.6074 | +1.849 | 0.0645 | 1.7531 | . |
| Circulatory disease | +0.2946 | 0.2678 | ±0.5357 | +1.100 | 0.2714 | 1.3425 |  |
| Avg. daily time 54-69 (%) | -0.0647 | 0.2198 | ±0.4397 | -0.294 | 0.7686 | 0.9374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.92** (p = **8.01e-08**), AUC = **0.6762**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2296 | 0.7209 | ±1.4418 | -0.318 | 0.7501 | 0.7949 |  |
| Education: graduate level (vs college) | -0.1187 | 0.2036 | ±0.4072 | -0.583 | 0.5600 | 0.8881 |  |
| Education: high school or below (vs college) | +0.3999 | 0.2852 | ±0.5704 | +1.402 | 0.1608 | 1.4917 |  |
| Site: UCSD (vs UAB) | -0.0938 | 0.2476 | ±0.4952 | -0.379 | 0.7049 | 0.9105 |  |
| Site: UW (vs UAB) | +0.2095 | 0.2325 | ±0.4649 | +0.901 | 0.3675 | 1.2331 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.879** | **1.07e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.229** | **0.0258** | 1.0289 | * |
| Hypertension | +0.1546 | 0.2039 | ±0.4077 | +0.758 | 0.4482 | 1.1672 |  |
| **High cholesterol** | **+0.5114** | 0.1932 | ±0.3863 | **+2.648** | **0.0081** | 1.6677 | ** |
| Kidney disease | +0.5610 | 0.3037 | ±0.6073 | +1.848 | 0.0647 | 1.7525 | . |
| Circulatory disease | +0.2958 | 0.2678 | ±0.5356 | +1.105 | 0.2693 | 1.3442 |  |
| Time < 70 (%) | -0.0802 | 0.2242 | ±0.4483 | -0.358 | 0.7206 | 0.9230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.88** (p = **8.15e-08**), AUC = **0.6766**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2351 | 0.7204 | ±1.4408 | -0.326 | 0.7441 | 0.7905 |  |
| Education: graduate level (vs college) | -0.1181 | 0.2036 | ±0.4073 | -0.580 | 0.5619 | 0.8886 |  |
| Education: high school or below (vs college) | +0.4001 | 0.2852 | ±0.5705 | +1.403 | 0.1607 | 1.4919 |  |
| Site: UCSD (vs UAB) | -0.0923 | 0.2477 | ±0.4954 | -0.373 | 0.7094 | 0.9118 |  |
| Site: UW (vs UAB) | +0.2107 | 0.2324 | ±0.4648 | +0.907 | 0.3646 | 1.2345 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.877** | **1.08e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.231** | **0.0257** | 1.0289 | * |
| Hypertension | +0.1550 | 0.2039 | ±0.4078 | +0.760 | 0.4470 | 1.1677 |  |
| **High cholesterol** | **+0.5109** | 0.1931 | ±0.3863 | **+2.645** | **0.0082** | 1.6668 | ** |
| Kidney disease | +0.5614 | 0.3037 | ±0.6074 | +1.849 | 0.0645 | 1.7531 | . |
| Circulatory disease | +0.2946 | 0.2678 | ±0.5357 | +1.100 | 0.2714 | 1.3425 |  |
| Avg. daily time < 70 (%) | -0.0647 | 0.2198 | ±0.4397 | -0.294 | 0.7686 | 0.9374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.04** (p = **7.61e-08**), AUC = **0.6777**, AIC = **791.7**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2410 | 0.7198 | ±1.4397 | -0.335 | 0.7378 | 0.7859 |  |
| Education: graduate level (vs college) | -0.1180 | 0.2035 | ±0.4071 | -0.580 | 0.5619 | 0.8887 |  |
| Education: high school or below (vs college) | +0.3994 | 0.2850 | ±0.5699 | +1.402 | 0.1610 | 1.4910 |  |
| Site: UCSD (vs UAB) | -0.0844 | 0.2484 | ±0.4969 | -0.340 | 0.7339 | 0.9190 |  |
| Site: UW (vs UAB) | +0.2156 | 0.2325 | ±0.4650 | +0.927 | 0.3538 | 1.2406 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.907** | **9.23e-07** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0282** | 0.0128 | ±0.0257 | **+2.197** | **0.0280** | 1.0286 | * |
| Hypertension | +0.1524 | 0.2040 | ±0.4080 | +0.747 | 0.4550 | 1.1647 |  |
| **High cholesterol** | **+0.5029** | 0.1936 | ±0.3872 | **+2.598** | **0.0094** | 1.6535 | ** |
| Kidney disease | +0.5517 | 0.3044 | ±0.6088 | +1.812 | 0.0699 | 1.7361 | . |
| Circulatory disease | +0.2865 | 0.2686 | ±0.5372 | +1.067 | 0.2861 | 1.3318 |  |
| Time 181-250, pooled (%) | +0.0128 | 0.0250 | ±0.0500 | +0.512 | 0.6085 | 1.0129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.96** (p = **7.90e-08**), AUC = **0.6776**, AIC = **791.8**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2422 | 0.7198 | ±1.4396 | -0.337 | 0.7365 | 0.7849 |  |
| Education: graduate level (vs college) | -0.1171 | 0.2035 | ±0.4070 | -0.575 | 0.5651 | 0.8895 |  |
| Education: high school or below (vs college) | +0.4011 | 0.2849 | ±0.5699 | +1.408 | 0.1592 | 1.4935 |  |
| Site: UCSD (vs UAB) | -0.0863 | 0.2484 | ±0.4969 | -0.347 | 0.7283 | 0.9173 |  |
| Site: UW (vs UAB) | +0.2148 | 0.2325 | ±0.4649 | +0.924 | 0.3554 | 1.2396 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.901** | **9.52e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.202** | **0.0276** | 1.0287 | * |
| Hypertension | +0.1531 | 0.2040 | ±0.4080 | +0.750 | 0.4530 | 1.1654 |  |
| **High cholesterol** | **+0.5041** | 0.1936 | ±0.3873 | **+2.603** | **0.0092** | 1.6555 | ** |
| Kidney disease | +0.5534 | 0.3046 | ±0.6092 | +1.817 | 0.0692 | 1.7392 | . |
| Circulatory disease | +0.2878 | 0.2687 | ±0.5373 | +1.071 | 0.2840 | 1.3335 |  |
| Avg. daily time 181-250 (%) | +0.0106 | 0.0258 | ±0.0515 | +0.413 | 0.6795 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.04** (p = **7.61e-08**), AUC = **0.6777**, AIC = **791.7**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2410 | 0.7198 | ±1.4397 | -0.335 | 0.7378 | 0.7859 |  |
| Education: graduate level (vs college) | -0.1180 | 0.2035 | ±0.4071 | -0.580 | 0.5619 | 0.8887 |  |
| Education: high school or below (vs college) | +0.3994 | 0.2850 | ±0.5699 | +1.402 | 0.1610 | 1.4910 |  |
| Site: UCSD (vs UAB) | -0.0844 | 0.2484 | ±0.4969 | -0.340 | 0.7339 | 0.9190 |  |
| Site: UW (vs UAB) | +0.2156 | 0.2325 | ±0.4650 | +0.927 | 0.3538 | 1.2406 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.907** | **9.23e-07** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0282** | 0.0128 | ±0.0257 | **+2.197** | **0.0280** | 1.0286 | * |
| Hypertension | +0.1524 | 0.2040 | ±0.4080 | +0.747 | 0.4550 | 1.1647 |  |
| **High cholesterol** | **+0.5029** | 0.1936 | ±0.3872 | **+2.598** | **0.0094** | 1.6535 | ** |
| Kidney disease | +0.5517 | 0.3044 | ±0.6088 | +1.812 | 0.0699 | 1.7361 | . |
| Circulatory disease | +0.2865 | 0.2686 | ±0.5372 | +1.067 | 0.2861 | 1.3318 |  |
| Time > 180 (%) | +0.0128 | 0.0250 | ±0.0500 | +0.512 | 0.6085 | 1.0129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.96** (p = **7.90e-08**), AUC = **0.6776**, AIC = **791.8**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2422 | 0.7198 | ±1.4396 | -0.337 | 0.7365 | 0.7849 |  |
| Education: graduate level (vs college) | -0.1171 | 0.2035 | ±0.4070 | -0.575 | 0.5651 | 0.8895 |  |
| Education: high school or below (vs college) | +0.4011 | 0.2849 | ±0.5699 | +1.408 | 0.1592 | 1.4935 |  |
| Site: UCSD (vs UAB) | -0.0863 | 0.2484 | ±0.4969 | -0.347 | 0.7283 | 0.9173 |  |
| Site: UW (vs UAB) | +0.2148 | 0.2325 | ±0.4649 | +0.924 | 0.3554 | 1.2396 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.901** | **9.52e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.202** | **0.0276** | 1.0287 | * |
| Hypertension | +0.1531 | 0.2040 | ±0.4080 | +0.750 | 0.4530 | 1.1654 |  |
| **High cholesterol** | **+0.5041** | 0.1936 | ±0.3873 | **+2.603** | **0.0092** | 1.6555 | ** |
| Kidney disease | +0.5534 | 0.3046 | ±0.6092 | +1.817 | 0.0692 | 1.7392 | . |
| Circulatory disease | +0.2878 | 0.2687 | ±0.5373 | +1.071 | 0.2840 | 1.3335 |  |
| Avg. daily time > 180 (%) | +0.0106 | 0.0258 | ±0.0515 | +0.413 | 0.6795 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0730**, LLR χ² = **60.03** (p = **9.15e-09**), AUC = **0.6843**, AIC = **786.7**, BIC = **844.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1992 | 0.7259 | ±1.4518 | -0.274 | 0.7838 | 0.8194 |  |
| Education: graduate level (vs college) | -0.1151 | 0.2042 | ±0.4084 | -0.564 | 0.5729 | 0.8913 |  |
| Education: high school or below (vs college) | +0.3596 | 0.2868 | ±0.5735 | +1.254 | 0.2098 | 1.4328 |  |
| Site: UCSD (vs UAB) | -0.0477 | 0.2492 | ±0.4983 | -0.191 | 0.8482 | 0.9534 |  |
| Site: UW (vs UAB) | +0.2310 | 0.2338 | ±0.4677 | +0.988 | 0.3233 | 1.2598 |  |
| **Age (years)** | **-0.0451** | 0.0093 | ±0.0185 | **-4.870** | **1.12e-06** | 0.9559 | *** |
| BMI (kg/m2) | +0.0248 | 0.0130 | ±0.0261 | +1.904 | 0.0569 | 1.0252 | . |
| Hypertension | +0.1806 | 0.2046 | ±0.4091 | +0.883 | 0.3774 | 1.1979 |  |
| **High cholesterol** | **+0.4622** | 0.1948 | ±0.3896 | **+2.373** | **0.0177** | 1.5875 | * |
| Kidney disease | +0.5299 | 0.3048 | ±0.6096 | +1.738 | 0.0822 | 1.6987 | . |
| Circulatory disease | +0.2626 | 0.2703 | ±0.5405 | +0.972 | 0.3312 | 1.3004 |  |
| **Nocturnal time > 180 (%)** | **+0.0467** | 0.0205 | ±0.0410 | **+2.277** | **0.0228** | 1.0478 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 46 single-predictor tests; 2 with raw p < 0.05 (about 2 expected by chance); FDR rule applied to 46 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family and 0 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 889): best single predictor out of sample is **GMI** (CV R² 0.050 vs 0.049 for covariates alone, gain +0.001; -0.167 per SD, p = 0.300, q = 0.630). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 889): best single predictor out of sample is **Nocturnal mean** (CV AUC 0.651 vs 0.643 for covariates alone, gain +0.008; OR 1.20 per SD, p = 0.041, q = 0.199). No association survives FDR; nominal only: %>180 nocturnal (p = 0.023), Nocturnal mean (p = 0.041).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.008, via Nocturnal mean); CES-D-10 depressive symptoms (0-30) (+0.001, via GMI). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM level (0 FDR-significant / 1 raw-significant of 6); Band > 180 (0 FDR-significant / 1 raw-significant of 6); HbA1c (0 FDR-significant / 0 raw-significant of 2).
Level metrics: 0 FDR-significant (1 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Clinically relevant depressive symptoms (%>180 nocturnal, ΔAIC -5.0).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
