# Phase 6 model output tables - All (analysis base) - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


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
