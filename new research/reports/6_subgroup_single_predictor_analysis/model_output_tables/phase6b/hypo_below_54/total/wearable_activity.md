# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Total analysis base - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 575; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **575**, R² = **0.1606**, Adj R² = **0.1457**, F-statistic = **10.79** (p = **7.14e-17**), Residual SE = **4142.120** on **564** df, AIC = **11221.0**, BIC = **11268.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20170.2242** | 1377.2456 | ±2754.4912 | **+14.645** | **1.44e-48** | *** |
| Education: graduate level (vs college) | -654.3042 | 389.1310 | ±778.2619 | -1.681 | 0.0927 | . |
| Education: high school or below (vs college) | +787.5540 | 705.0046 | ±1410.0093 | +1.117 | 0.2640 |  |
| Site: UCSD (vs UAB) | +220.4969 | 464.3232 | ±928.6463 | +0.475 | 0.6349 |  |
| Site: UW (vs UAB) | +240.8803 | 407.2541 | ±814.5082 | +0.591 | 0.5542 |  |
| **Age (years)** | **-146.5494** | 16.0585 | ±32.1170 | **-9.126** | **7.11e-20** | *** |
| BMI (kg/m2) | -42.8297 | 27.4461 | ±54.8923 | -1.560 | 0.1186 |  |
| Hypertension | -326.6177 | 400.6722 | ±801.3444 | -0.815 | 0.4150 |  |
| High cholesterol | -82.5906 | 363.2356 | ±726.4711 | -0.227 | 0.8201 |  |
| Kidney disease | -869.0912 | 716.8445 | ±1433.6890 | -1.212 | 0.2254 |  |
| Circulatory disease | -574.3306 | 450.8863 | ±901.7726 | -1.274 | 0.2027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **575**, R² = **0.1649**, Adj R² = **0.1486**, F-statistic = **10.11** (p = **6.34e-17**), Residual SE = **4135.047** on **563** df, AIC = **11220.0**, BIC = **11272.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18371.8235** | 2086.6228 | ±4173.2456 | **+8.805** | **1.31e-18** | *** |
| Education: graduate level (vs college) | -604.6126 | 395.9142 | ±791.8284 | -1.527 | 0.1267 |  |
| Education: high school or below (vs college) | +691.3886 | 696.2810 | ±1392.5620 | +0.993 | 0.3207 |  |
| Site: UCSD (vs UAB) | +205.1773 | 464.2113 | ±928.4227 | +0.442 | 0.6585 |  |
| Site: UW (vs UAB) | +293.4581 | 410.4596 | ±820.9191 | +0.715 | 0.4746 |  |
| **Age (years)** | **-150.4708** | 16.2070 | ±32.4140 | **-9.284** | **1.63e-20** | *** |
| BMI (kg/m2) | -46.3519 | 27.2672 | ±54.5344 | -1.700 | 0.0891 | . |
| Hypertension | -385.6929 | 405.9415 | ±811.8829 | -0.950 | 0.3421 |  |
| High cholesterol | -132.6662 | 371.2113 | ±742.4227 | -0.357 | 0.7208 |  |
| Kidney disease | -907.1914 | 706.5372 | ±1413.0745 | -1.284 | 0.1991 |  |
| Circulatory disease | -559.0604 | 451.1610 | ±902.3220 | -1.239 | 0.2153 |  |
| HbA1c (%) | +367.1900 | 297.7031 | ±595.4062 | +1.233 | 0.2174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **575**, R² = **0.1610**, Adj R² = **0.1446**, F-statistic = **9.82** (p = **2.13e-16**), Residual SE = **4144.745** on **563** df, AIC = **11222.7**, BIC = **11274.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20587.6454** | 1700.2985 | ±3400.5969 | **+12.108** | **9.55e-34** | *** |
| Education: graduate level (vs college) | -655.2399 | 389.6653 | ±779.3306 | -1.682 | 0.0927 | . |
| Education: high school or below (vs college) | +812.5592 | 703.1289 | ±1406.2577 | +1.156 | 0.2478 |  |
| Site: UCSD (vs UAB) | +223.6956 | 464.7368 | ±929.4736 | +0.481 | 0.6303 |  |
| Site: UW (vs UAB) | +235.3552 | 408.9722 | ±817.9445 | +0.575 | 0.5650 |  |
| **Age (years)** | **-146.2583** | 16.0445 | ±32.0889 | **-9.116** | **7.81e-20** | *** |
| BMI (kg/m2) | -42.2385 | 27.4149 | ±54.8297 | -1.541 | 0.1234 |  |
| Hypertension | -302.4647 | 407.1648 | ±814.3296 | -0.743 | 0.4576 |  |
| High cholesterol | -66.0284 | 365.4438 | ±730.8875 | -0.181 | 0.8566 |  |
| Kidney disease | -831.3034 | 723.1268 | ±1446.2537 | -1.150 | 0.2503 |  |
| Circulatory disease | -569.7429 | 452.3676 | ±904.7352 | -1.259 | 0.2079 |  |
| Mean glucose (mg/dL) | -3.9150 | 7.8798 | ±15.7596 | -0.497 | 0.6193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **575**, R² = **0.1610**, Adj R² = **0.1446**, F-statistic = **9.82** (p = **2.13e-16**), Residual SE = **4144.745** on **563** df, AIC = **11222.7**, BIC = **11274.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21129.3929** | 2506.1907 | ±5012.3813 | **+8.431** | **3.43e-17** | *** |
| Education: graduate level (vs college) | -655.2399 | 389.6653 | ±779.3306 | -1.682 | 0.0927 | . |
| Education: high school or below (vs college) | +812.5592 | 703.1289 | ±1406.2577 | +1.156 | 0.2478 |  |
| Site: UCSD (vs UAB) | +223.6956 | 464.7368 | ±929.4736 | +0.481 | 0.6303 |  |
| Site: UW (vs UAB) | +235.3552 | 408.9722 | ±817.9445 | +0.575 | 0.5650 |  |
| **Age (years)** | **-146.2583** | 16.0445 | ±32.0889 | **-9.116** | **7.81e-20** | *** |
| BMI (kg/m2) | -42.2385 | 27.4149 | ±54.8297 | -1.541 | 0.1234 |  |
| Hypertension | -302.4647 | 407.1648 | ±814.3296 | -0.743 | 0.4576 |  |
| High cholesterol | -66.0284 | 365.4438 | ±730.8875 | -0.181 | 0.8566 |  |
| Kidney disease | -831.3034 | 723.1268 | ±1446.2537 | -1.150 | 0.2503 |  |
| Circulatory disease | -569.7429 | 452.3676 | ±904.7352 | -1.259 | 0.2079 |  |
| GMI (%) | -163.6699 | 329.4241 | ±658.8481 | -0.497 | 0.6193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **575**, R² = **0.1606**, Adj R² = **0.1442**, F-statistic = **9.79** (p = **2.40e-16**), Residual SE = **4145.692** on **563** df, AIC = **11223.0**, BIC = **11275.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20038.5087** | 1690.5840 | ±3381.1680 | **+11.853** | **2.08e-32** | *** |
| Education: graduate level (vs college) | -654.3046 | 389.6589 | ±779.3179 | -1.679 | 0.0931 | . |
| Education: high school or below (vs college) | +780.2746 | 704.5967 | ±1409.1935 | +1.107 | 0.2681 |  |
| Site: UCSD (vs UAB) | +218.3857 | 462.9645 | ±925.9289 | +0.472 | 0.6371 |  |
| Site: UW (vs UAB) | +241.4338 | 408.1285 | ±816.2571 | +0.592 | 0.5541 |  |
| **Age (years)** | **-146.4712** | 16.1385 | ±32.2771 | **-9.076** | **1.13e-19** | *** |
| BMI (kg/m2) | -43.2007 | 27.4743 | ±54.9487 | -1.572 | 0.1159 |  |
| Hypertension | -334.3476 | 406.8119 | ±813.6239 | -0.822 | 0.4111 |  |
| High cholesterol | -88.6842 | 367.2586 | ±734.5171 | -0.241 | 0.8092 |  |
| Kidney disease | -873.6059 | 718.2853 | ±1436.5706 | -1.216 | 0.2239 |  |
| Circulatory disease | -575.1063 | 452.1430 | ±904.2860 | -1.272 | 0.2034 |  |
| Nocturnal mean 00-06h (mg/dL) | +1.2256 | 7.7636 | ±15.5272 | +0.158 | 0.8746 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1634**, Adj R² = **0.1470**, F-statistic = **10.00** (p = **1.02e-16**), Residual SE = **4138.850** on **563** df, AIC = **11221.1**, BIC = **11273.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20522.8376** | 1424.5444 | ±2849.0888 | **+14.407** | **4.70e-47** | *** |
| Education: graduate level (vs college) | -674.3096 | 389.6834 | ±779.3668 | -1.730 | 0.0836 | . |
| Education: high school or below (vs college) | +895.9372 | 698.8887 | ±1397.7774 | +1.282 | 0.1999 |  |
| Site: UCSD (vs UAB) | +219.6306 | 466.6338 | ±933.2676 | +0.471 | 0.6379 |  |
| Site: UW (vs UAB) | +192.2897 | 411.3500 | ±822.7001 | +0.467 | 0.6402 |  |
| **Age (years)** | **-143.6019** | 16.0970 | ±32.1941 | **-8.921** | **4.62e-19** | *** |
| BMI (kg/m2) | -43.1722 | 27.4404 | ±54.8808 | -1.573 | 0.1156 |  |
| Hypertension | -272.4327 | 402.4590 | ±804.9179 | -0.677 | 0.4985 |  |
| High cholesterol | -63.5834 | 364.4792 | ±728.9584 | -0.174 | 0.8615 |  |
| Kidney disease | -689.2949 | 727.8601 | ±1455.7203 | -0.947 | 0.3436 |  |
| Circulatory disease | -586.5855 | 451.1068 | ±902.2136 | -1.300 | 0.1935 |  |
| Glucose SD, pooled (mg/dL) | -21.1469 | 15.3109 | ±30.6217 | -1.381 | 0.1672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1642**, Adj R² = **0.1479**, F-statistic = **10.06** (p = **7.91e-17**), Residual SE = **4136.812** on **563** df, AIC = **11220.5**, BIC = **11272.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20573.5472** | 1421.7965 | ±2843.5930 | **+14.470** | **1.87e-47** | *** |
| Education: graduate level (vs college) | -680.8277 | 389.8676 | ±779.7351 | -1.746 | 0.0808 | . |
| Education: high school or below (vs college) | +928.1742 | 696.7538 | ±1393.5075 | +1.332 | 0.1828 |  |
| Site: UCSD (vs UAB) | +225.8480 | 465.4551 | ±930.9102 | +0.485 | 0.6275 |  |
| Site: UW (vs UAB) | +192.9973 | 410.2140 | ±820.4280 | +0.470 | 0.6380 |  |
| **Age (years)** | **-142.8911** | 16.0387 | ±32.0774 | **-8.909** | **5.14e-19** | *** |
| BMI (kg/m2) | -43.3774 | 27.4332 | ±54.8663 | -1.581 | 0.1138 |  |
| Hypertension | -268.9828 | 402.0704 | ±804.1407 | -0.669 | 0.5035 |  |
| High cholesterol | -55.7197 | 363.8973 | ±727.7946 | -0.153 | 0.8783 |  |
| Kidney disease | -660.5795 | 728.1605 | ±1456.3211 | -0.907 | 0.3643 |  |
| Circulatory disease | -595.7289 | 449.5958 | ±899.1916 | -1.325 | 0.1852 |  |
| Avg. daily SD (mg/dL) | -27.9504 | 16.9601 | ±33.9201 | -1.648 | 0.0993 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **575**, R² = **0.1637**, Adj R² = **0.1473**, F-statistic = **10.02** (p = **9.37e-17**), Residual SE = **4138.169** on **563** df, AIC = **11220.9**, BIC = **11273.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20864.3288** | 1464.8855 | ±2929.7710 | **+14.243** | **4.96e-46** | *** |
| Education: graduate level (vs college) | -677.2330 | 389.0061 | ±778.0122 | -1.741 | 0.0817 | . |
| Education: high school or below (vs college) | +901.0721 | 700.7867 | ±1401.5734 | +1.286 | 0.1985 |  |
| Site: UCSD (vs UAB) | +223.3038 | 465.4522 | ±930.9045 | +0.480 | 0.6314 |  |
| Site: UW (vs UAB) | +179.1778 | 411.3141 | ±822.6282 | +0.436 | 0.6631 |  |
| **Age (years)** | **-142.2047** | 16.3144 | ±32.6288 | **-8.717** | **2.87e-18** | *** |
| BMI (kg/m2) | -44.1636 | 27.5674 | ±55.1348 | -1.602 | 0.1092 |  |
| Hypertension | -287.2608 | 400.1970 | ±800.3940 | -0.718 | 0.4729 |  |
| High cholesterol | -83.1467 | 363.4563 | ±726.9125 | -0.229 | 0.8191 |  |
| Kidney disease | -670.3688 | 730.5321 | ±1461.0641 | -0.918 | 0.3588 |  |
| Circulatory disease | -597.8658 | 450.4116 | ±900.8232 | -1.327 | 0.1844 |  |
| CV (%) | -44.3301 | 28.3191 | ±56.6383 | -1.565 | 0.1175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **575**, R² = **0.1608**, Adj R² = **0.1444**, F-statistic = **9.80** (p = **2.31e-16**), Residual SE = **4145.373** on **563** df, AIC = **11222.9**, BIC = **11275.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19855.5962** | 1629.0407 | ±3258.0814 | **+12.189** | **3.58e-34** | *** |
| Education: graduate level (vs college) | -655.2927 | 389.5265 | ±779.0530 | -1.682 | 0.0925 | . |
| Education: high school or below (vs college) | +813.4471 | 703.8538 | ±1407.7076 | +1.156 | 0.2478 |  |
| Site: UCSD (vs UAB) | +224.5328 | 464.7463 | ±929.4925 | +0.483 | 0.6290 |  |
| Site: UW (vs UAB) | +231.9637 | 410.0340 | ±820.0680 | +0.566 | 0.5716 |  |
| **Age (years)** | **-145.4823** | 16.3377 | ±32.6753 | **-8.905** | **5.35e-19** | *** |
| BMI (kg/m2) | -42.8766 | 27.5203 | ±55.0405 | -1.558 | 0.1192 |  |
| Hypertension | -318.1394 | 402.0132 | ±804.0264 | -0.791 | 0.4287 |  |
| High cholesterol | -82.3872 | 363.8148 | ±727.6296 | -0.226 | 0.8208 |  |
| Kidney disease | -834.9532 | 731.9654 | ±1463.9308 | -1.141 | 0.2540 |  |
| Circulatory disease | -575.6319 | 451.3578 | ±902.7157 | -1.275 | 0.2022 |  |
| Mean / SD ratio | +47.7094 | 133.4236 | ±266.8471 | +0.358 | 0.7207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1606**, Adj R² = **0.1442**, F-statistic = **9.79** (p = **2.43e-16**), Residual SE = **4145.782** on **563** df, AIC = **11223.0**, BIC = **11275.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20229.3149** | 1628.8848 | ±3257.7697 | **+12.419** | **2.06e-35** | *** |
| Education: graduate level (vs college) | -654.0145 | 389.5682 | ±779.1364 | -1.679 | 0.0932 | . |
| Education: high school or below (vs college) | +782.2072 | 703.1710 | ±1406.3421 | +1.112 | 0.2660 |  |
| Site: UCSD (vs UAB) | +218.9113 | 464.4335 | ±928.8670 | +0.471 | 0.6374 |  |
| Site: UW (vs UAB) | +242.0167 | 408.6004 | ±817.2008 | +0.592 | 0.5536 |  |
| **Age (years)** | **-146.7683** | 16.3413 | ±32.6826 | **-8.981** | **2.67e-19** | *** |
| BMI (kg/m2) | -42.8332 | 27.4803 | ±54.9605 | -1.559 | 0.1191 |  |
| Hypertension | -327.7009 | 401.7399 | ±803.4799 | -0.816 | 0.4147 |  |
| High cholesterol | -82.9478 | 364.0270 | ±728.0540 | -0.228 | 0.8198 |  |
| Kidney disease | -874.7882 | 729.5399 | ±1459.0798 | -1.199 | 0.2305 |  |
| Circulatory disease | -573.7364 | 450.8883 | ±901.7767 | -1.272 | 0.2032 |  |
| Avg. daily mean/SD | -7.3613 | 106.3214 | ±212.6429 | -0.069 | 0.9448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **575**, R² = **0.1619**, Adj R² = **0.1455**, F-statistic = **9.89** (p = **1.62e-16**), Residual SE = **4142.528** on **563** df, AIC = **11222.1**, BIC = **11274.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19462.2168** | 1634.3852 | ±3268.7703 | **+11.908** | **1.08e-32** | *** |
| Education: graduate level (vs college) | -646.2435 | 390.0558 | ±780.1117 | -1.657 | 0.0976 | . |
| Education: high school or below (vs college) | +741.8823 | 705.3531 | ±1410.7063 | +1.052 | 0.2929 |  |
| Site: UCSD (vs UAB) | +202.8243 | 460.8856 | ±921.7712 | +0.440 | 0.6599 |  |
| Site: UW (vs UAB) | +287.8676 | 415.1556 | ±830.3111 | +0.693 | 0.4881 |  |
| **Age (years)** | **-146.6457** | 16.0428 | ±32.0856 | **-9.141** | **6.19e-20** | *** |
| BMI (kg/m2) | -43.4397 | 27.4057 | ±54.8114 | -1.585 | 0.1130 |  |
| Hypertension | -342.8890 | 401.5992 | ±803.1983 | -0.854 | 0.3932 |  |
| High cholesterol | -77.9094 | 363.3517 | ±726.7035 | -0.214 | 0.8302 |  |
| Kidney disease | -894.0062 | 720.7641 | ±1441.5283 | -1.240 | 0.2148 |  |
| Circulatory disease | -570.3695 | 451.1752 | ±902.3505 | -1.264 | 0.2062 |  |
| MAG (mg/dL/h) | +17.5844 | 20.3346 | ±40.6691 | +0.865 | 0.3872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.46e-16**), Residual SE = **4141.716** on **563** df, AIC = **11221.8**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20608.6988** | 1480.5866 | ±2961.1733 | **+13.919** | **4.84e-44** | *** |
| Education: graduate level (vs college) | -673.0084 | 390.7837 | ±781.5673 | -1.722 | 0.0850 | . |
| Education: high school or below (vs college) | +881.9130 | 698.8448 | ±1397.6897 | +1.262 | 0.2070 |  |
| Site: UCSD (vs UAB) | +230.7968 | 464.4311 | ±928.8623 | +0.497 | 0.6192 |  |
| Site: UW (vs UAB) | +211.0373 | 411.4002 | ±822.8005 | +0.513 | 0.6080 |  |
| **Age (years)** | **-144.3189** | 16.1020 | ±32.2039 | **-8.963** | **3.16e-19** | *** |
| BMI (kg/m2) | -44.0868 | 27.5891 | ±55.1783 | -1.598 | 0.1100 |  |
| Hypertension | -294.7057 | 401.8852 | ±803.7704 | -0.733 | 0.4634 |  |
| High cholesterol | -66.4974 | 364.2427 | ±728.4854 | -0.183 | 0.8551 |  |
| Kidney disease | -740.0027 | 727.1365 | ±1454.2730 | -1.018 | 0.3088 |  |
| Circulatory disease | -579.8070 | 450.4733 | ±900.9466 | -1.287 | 0.1981 |  |
| Avg. daily range (mg/dL) | -4.9747 | 4.7607 | ±9.5215 | -1.045 | 0.2960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **575**, R² = **0.1607**, Adj R² = **0.1443**, F-statistic = **9.80** (p = **2.35e-16**), Residual SE = **4145.529** on **563** df, AIC = **11222.9**, BIC = **11275.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20215.8755** | 1409.5840 | ±2819.1680 | **+14.342** | **1.20e-46** | *** |
| Education: graduate level (vs college) | -658.1632 | 391.0592 | ±782.1185 | -1.683 | 0.0924 | . |
| Education: high school or below (vs college) | +791.5185 | 708.5610 | ±1417.1220 | +1.117 | 0.2640 |  |
| Site: UCSD (vs UAB) | +216.6188 | 467.5743 | ±935.1487 | +0.463 | 0.6432 |  |
| Site: UW (vs UAB) | +232.6540 | 411.9691 | ±823.9382 | +0.565 | 0.5723 |  |
| **Age (years)** | **-146.3317** | 16.1016 | ±32.2033 | **-9.088** | **1.01e-19** | *** |
| BMI (kg/m2) | -42.7913 | 27.4531 | ±54.9062 | -1.559 | 0.1191 |  |
| Hypertension | -316.4429 | 404.3091 | ±808.6181 | -0.783 | 0.4338 |  |
| High cholesterol | -80.4399 | 365.3781 | ±730.7561 | -0.220 | 0.8258 |  |
| Kidney disease | -848.3958 | 723.3064 | ±1446.6128 | -1.173 | 0.2408 |  |
| Circulatory disease | -570.3224 | 453.7056 | ±907.4113 | -1.257 | 0.2087 |  |
| SD of daily means (mg/dL) | -7.0007 | 29.7690 | ±59.5380 | -0.235 | 0.8141 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **575**, R² = **0.1632**, Adj R² = **0.1469**, F-statistic = **9.98** (p = **1.08e-16**), Residual SE = **4139.296** on **563** df, AIC = **11221.2**, BIC = **11273.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18395.4471** | 1764.9775 | ±3529.9549 | **+10.422** | **1.96e-25** | *** |
| Education: graduate level (vs college) | -684.1737 | 390.8510 | ±781.7019 | -1.750 | 0.0800 | . |
| Education: high school or below (vs college) | +843.3869 | 706.1644 | ±1412.3288 | +1.194 | 0.2324 |  |
| Site: UCSD (vs UAB) | +198.7483 | 473.1960 | ±946.3919 | +0.420 | 0.6745 |  |
| Site: UW (vs UAB) | +186.6221 | 410.9232 | ±821.8464 | +0.454 | 0.6497 |  |
| **Age (years)** | **-145.3192** | 16.0070 | ±32.0141 | **-9.078** | **1.10e-19** | *** |
| BMI (kg/m2) | -42.6466 | 27.4858 | ±54.9716 | -1.552 | 0.1208 |  |
| Hypertension | -291.2009 | 402.1897 | ±804.3794 | -0.724 | 0.4690 |  |
| High cholesterol | -52.3932 | 364.3973 | ±728.7946 | -0.144 | 0.8857 |  |
| Kidney disease | -735.0410 | 726.6934 | ±1453.3868 | -1.011 | 0.3118 |  |
| Circulatory disease | -564.6911 | 452.2750 | ±904.5500 | -1.249 | 0.2118 |  |
| Time in range 70-180, pooled (%) | +18.3969 | 14.1910 | ±28.3820 | +1.296 | 0.1948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **575**, R² = **0.1631**, Adj R² = **0.1467**, F-statistic = **9.97** (p = **1.12e-16**), Residual SE = **4139.622** on **563** df, AIC = **11221.3**, BIC = **11273.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18437.3947** | 1784.7293 | ±3569.4587 | **+10.331** | **5.12e-25** | *** |
| Education: graduate level (vs college) | -684.2113 | 390.7964 | ±781.5928 | -1.751 | 0.0800 | . |
| Education: high school or below (vs college) | +844.8831 | 706.2160 | ±1412.4321 | +1.196 | 0.2316 |  |
| Site: UCSD (vs UAB) | +199.2511 | 472.4466 | ±944.8932 | +0.422 | 0.6732 |  |
| Site: UW (vs UAB) | +187.1992 | 410.9451 | ±821.8901 | +0.456 | 0.6487 |  |
| **Age (years)** | **-145.2635** | 16.0057 | ±32.0115 | **-9.076** | **1.13e-19** | *** |
| BMI (kg/m2) | -42.6894 | 27.4692 | ±54.9385 | -1.554 | 0.1202 |  |
| Hypertension | -293.3738 | 401.8443 | ±803.6885 | -0.730 | 0.4653 |  |
| High cholesterol | -51.4244 | 365.0717 | ±730.1433 | -0.141 | 0.8880 |  |
| Kidney disease | -737.1333 | 726.1854 | ±1452.3707 | -1.015 | 0.3101 |  |
| Circulatory disease | -564.6302 | 452.2128 | ±904.4256 | -1.249 | 0.2118 |  |
| Avg. daily time in range 70-180 (%) | +17.8433 | 14.1255 | ±28.2509 | +1.263 | 0.2065 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1627**, Adj R² = **0.1463**, F-statistic = **9.95** (p = **1.26e-16**), Residual SE = **4140.563** on **563** df, AIC = **11221.5**, BIC = **11273.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20343.9950** | 1395.3651 | ±2790.7302 | **+14.580** | **3.78e-48** | *** |
| Education: graduate level (vs college) | -665.9722 | 388.8031 | ±777.6062 | -1.713 | 0.0867 | . |
| Education: high school or below (vs college) | +753.8316 | 705.4639 | ±1410.9279 | +1.069 | 0.2853 |  |
| Site: UCSD (vs UAB) | +143.5148 | 471.1757 | ±942.3515 | +0.305 | 0.7607 |  |
| Site: UW (vs UAB) | +175.3340 | 408.8926 | ±817.7852 | +0.429 | 0.6681 |  |
| **Age (years)** | **-146.2828** | 16.0593 | ±32.1187 | **-9.109** | **8.32e-20** | *** |
| BMI (kg/m2) | -43.4427 | 27.6101 | ±55.2201 | -1.573 | 0.1156 |  |
| Hypertension | -345.8960 | 400.2402 | ±800.4803 | -0.864 | 0.3875 |  |
| High cholesterol | -113.5988 | 364.7821 | ±729.5642 | -0.311 | 0.7555 |  |
| Kidney disease | -854.6863 | 715.0338 | ±1430.0677 | -1.195 | 0.2320 |  |
| Circulatory disease | -570.5839 | 451.2019 | ±902.4038 | -1.265 | 0.2060 |  |
| Time < 54 (%) | -230.8858 | 131.2264 | ±262.4528 | -1.759 | 0.0785 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **575**, R² = **0.1630**, Adj R² = **0.1466**, F-statistic = **9.97** (p = **1.15e-16**), Residual SE = **4139.822** on **563** df, AIC = **11221.3**, BIC = **11273.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20269.3782** | 1384.9622 | ±2769.9243 | **+14.635** | **1.67e-48** | *** |
| Education: graduate level (vs college) | -678.7552 | 390.0488 | ±780.0976 | -1.740 | 0.0818 | . |
| Education: high school or below (vs college) | +749.7254 | 705.3428 | ±1410.6857 | +1.063 | 0.2878 |  |
| Site: UCSD (vs UAB) | +150.6283 | 470.4850 | ±940.9700 | +0.320 | 0.7489 |  |
| Site: UW (vs UAB) | +164.2694 | 410.5060 | ±821.0119 | +0.400 | 0.6890 |  |
| **Age (years)** | **-145.3150** | 16.0716 | ±32.1432 | **-9.042** | **1.54e-19** | *** |
| BMI (kg/m2) | -43.2799 | 27.5296 | ±55.0593 | -1.572 | 0.1159 |  |
| Hypertension | -347.4472 | 400.2301 | ±800.4602 | -0.868 | 0.3853 |  |
| High cholesterol | -117.8549 | 363.7664 | ±727.5329 | -0.324 | 0.7459 |  |
| Kidney disease | -847.5084 | 714.5792 | ±1429.1584 | -1.186 | 0.2356 |  |
| Circulatory disease | -567.6092 | 449.9640 | ±899.9279 | -1.261 | 0.2071 |  |
| Avg. daily time < 54 (%) | -285.5050 | 152.5420 | ±305.0840 | -1.872 | 0.0613 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.47e-16**), Residual SE = **4141.744** on **563** df, AIC = **11221.9**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20307.7728** | 1388.8564 | ±2777.7128 | **+14.622** | **2.04e-48** | *** |
| Education: graduate level (vs college) | -681.2575 | 387.8170 | ±775.6339 | -1.757 | 0.0790 | . |
| Education: high school or below (vs college) | +788.8929 | 708.1386 | ±1416.2771 | +1.114 | 0.2653 |  |
| Site: UCSD (vs UAB) | +181.4121 | 462.0513 | ±924.1025 | +0.393 | 0.6946 |  |
| Site: UW (vs UAB) | +195.3388 | 403.5968 | ±807.1935 | +0.484 | 0.6284 |  |
| **Age (years)** | **-145.8620** | 16.0623 | ±32.1245 | **-9.081** | **1.08e-19** | *** |
| BMI (kg/m2) | -42.9305 | 27.7709 | ±55.5419 | -1.546 | 0.1221 |  |
| Hypertension | -347.3897 | 403.1582 | ±806.3165 | -0.862 | 0.3889 |  |
| High cholesterol | -97.9196 | 363.6842 | ±727.3683 | -0.269 | 0.7877 |  |
| Kidney disease | -853.5602 | 714.6579 | ±1429.3158 | -1.194 | 0.2323 |  |
| Circulatory disease | -587.3914 | 450.8216 | ±901.6433 | -1.303 | 0.1926 |  |
| Time 54-69, pooled (%) | -78.7976 | 73.0169 | ±146.0339 | -1.079 | 0.2805 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.46e-16**), Residual SE = **4141.721** on **563** df, AIC = **11221.8**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20267.2553** | 1383.3358 | ±2766.6716 | **+14.651** | **1.33e-48** | *** |
| Education: graduate level (vs college) | -682.8945 | 388.1055 | ±776.2110 | -1.760 | 0.0785 | . |
| Education: high school or below (vs college) | +789.9552 | 708.1576 | ±1416.3153 | +1.116 | 0.2646 |  |
| Site: UCSD (vs UAB) | +186.9076 | 461.9115 | ±923.8230 | +0.405 | 0.6857 |  |
| Site: UW (vs UAB) | +192.7600 | 404.0776 | ±808.1552 | +0.477 | 0.6333 |  |
| **Age (years)** | **-145.4947** | 16.0907 | ±32.1813 | **-9.042** | **1.54e-19** | *** |
| BMI (kg/m2) | -42.8730 | 27.7277 | ±55.4554 | -1.546 | 0.1221 |  |
| Hypertension | -345.8446 | 403.3262 | ±806.6524 | -0.857 | 0.3912 |  |
| High cholesterol | -96.6767 | 363.4152 | ±726.8304 | -0.266 | 0.7902 |  |
| Kidney disease | -853.9739 | 714.5567 | ±1429.1135 | -1.195 | 0.2320 |  |
| Circulatory disease | -586.7207 | 450.2436 | ±900.4871 | -1.303 | 0.1925 |  |
| Avg. daily time 54-69 (%) | -75.8679 | 69.7930 | ±139.5860 | -1.087 | 0.2770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **575**, R² = **0.1628**, Adj R² = **0.1464**, F-statistic = **9.95** (p = **1.23e-16**), Residual SE = **4140.336** on **563** df, AIC = **11221.5**, BIC = **11273.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20354.3103** | 1394.3209 | ±2788.6417 | **+14.598** | **2.89e-48** | *** |
| Education: graduate level (vs college) | -683.2331 | 387.8959 | ±775.7917 | -1.761 | 0.0782 | . |
| Education: high school or below (vs college) | +778.0436 | 707.3559 | ±1414.7118 | +1.100 | 0.2714 |  |
| Site: UCSD (vs UAB) | +159.3783 | 463.6965 | ±927.3930 | +0.344 | 0.7311 |  |
| Site: UW (vs UAB) | +177.3735 | 404.2471 | ±808.4941 | +0.439 | 0.6608 |  |
| **Age (years)** | **-145.8215** | 16.0538 | ±32.1077 | **-9.083** | **1.05e-19** | *** |
| BMI (kg/m2) | -43.1196 | 27.7865 | ±55.5730 | -1.552 | 0.1207 |  |
| Hypertension | -352.1951 | 402.6343 | ±805.2686 | -0.875 | 0.3817 |  |
| High cholesterol | -106.8216 | 363.9684 | ±727.9368 | -0.293 | 0.7691 |  |
| Kidney disease | -849.9702 | 714.0351 | ±1428.0702 | -1.190 | 0.2339 |  |
| Circulatory disease | -585.3486 | 450.9894 | ±901.9788 | -1.298 | 0.1943 |  |
| Time < 70 (%) | -73.6869 | 55.2934 | ±110.5867 | -1.333 | 0.1826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **575**, R² = **0.1627**, Adj R² = **0.1464**, F-statistic = **9.95** (p = **1.25e-16**), Residual SE = **4140.465** on **563** df, AIC = **11221.5**, BIC = **11273.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20286.3727** | 1385.0957 | ±2770.1914 | **+14.646** | **1.42e-48** | *** |
| Education: graduate level (vs college) | -687.3355 | 388.4624 | ±776.9248 | -1.769 | 0.0768 | . |
| Education: high school or below (vs college) | +780.3514 | 707.2153 | ±1414.4306 | +1.103 | 0.2698 |  |
| Site: UCSD (vs UAB) | +171.3980 | 462.9831 | ±925.9661 | +0.370 | 0.7112 |  |
| Site: UW (vs UAB) | +176.4154 | 404.9493 | ±809.8987 | +0.436 | 0.6631 |  |
| **Age (years)** | **-145.2477** | 16.0863 | ±32.1726 | **-9.029** | **1.73e-19** | *** |
| BMI (kg/m2) | -42.9831 | 27.7178 | ±55.4356 | -1.551 | 0.1210 |  |
| Hypertension | -349.9284 | 402.8419 | ±805.6838 | -0.869 | 0.3850 |  |
| High cholesterol | -104.6728 | 363.3740 | ±726.7479 | -0.288 | 0.7733 |  |
| Kidney disease | -849.4608 | 713.9893 | ±1427.9785 | -1.190 | 0.2341 |  |
| Circulatory disease | -584.3132 | 449.9394 | ±899.8788 | -1.299 | 0.1941 |  |
| Avg. daily time < 70 (%) | -71.4214 | 54.5763 | ±109.1526 | -1.309 | 0.1907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1634**, Adj R² = **0.1471**, F-statistic = **10.00** (p = **1.00e-16**), Residual SE = **4138.718** on **563** df, AIC = **11221.0**, BIC = **11273.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16103.2973** | 2934.0237 | ±5868.0474 | **+5.488** | **4.05e-08** | *** |
| Education: graduate level (vs college) | -681.2316 | 389.4004 | ±778.8007 | -1.749 | 0.0802 | . |
| Education: high school or below (vs college) | +841.0016 | 705.1319 | ±1410.2637 | +1.193 | 0.2330 |  |
| Site: UCSD (vs UAB) | +190.0550 | 470.6022 | ±941.2043 | +0.404 | 0.6863 |  |
| Site: UW (vs UAB) | +184.3836 | 409.2060 | ±818.4119 | +0.451 | 0.6523 |  |
| **Age (years)** | **-146.5633** | 16.0549 | ±32.1097 | **-9.129** | **6.92e-20** | *** |
| BMI (kg/m2) | -43.3173 | 27.3886 | ±54.7771 | -1.582 | 0.1137 |  |
| Hypertension | -301.0718 | 399.4671 | ±798.9342 | -0.754 | 0.4510 |  |
| High cholesterol | -91.0586 | 363.2624 | ±726.5247 | -0.251 | 0.8021 |  |
| Kidney disease | -796.4759 | 717.5896 | ±1435.1792 | -1.110 | 0.2670 |  |
| Circulatory disease | -551.6281 | 453.7554 | ±907.5109 | -1.216 | 0.2241 |  |
| Time 54-250, pooled (%) | +41.6817 | 27.8201 | ±55.6403 | +1.498 | 0.1341 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1624**, Adj R² = **0.1460**, F-statistic = **9.92** (p = **1.40e-16**), Residual SE = **4141.376** on **563** df, AIC = **11221.8**, BIC = **11274.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16566.9734** | 3391.1388 | ±6782.2776 | **+4.885** | **1.03e-06** | *** |
| Education: graduate level (vs college) | -678.4425 | 389.9362 | ±779.8724 | -1.740 | 0.0819 | . |
| Education: high school or below (vs college) | +836.1310 | 704.6270 | ±1409.2539 | +1.187 | 0.2354 |  |
| Site: UCSD (vs UAB) | +199.1717 | 469.7532 | ±939.5063 | +0.424 | 0.6716 |  |
| Site: UW (vs UAB) | +197.3360 | 409.2340 | ±818.4680 | +0.482 | 0.6297 |  |
| **Age (years)** | **-146.3190** | 16.0486 | ±32.0972 | **-9.117** | **7.71e-20** | *** |
| BMI (kg/m2) | -43.3883 | 27.4217 | ±54.8435 | -1.582 | 0.1136 |  |
| Hypertension | -306.4865 | 400.0440 | ±800.0880 | -0.766 | 0.4436 |  |
| High cholesterol | -87.2318 | 363.6536 | ±727.3072 | -0.240 | 0.8104 |  |
| Kidney disease | -801.3850 | 717.5601 | ±1435.1202 | -1.117 | 0.2641 |  |
| Circulatory disease | -552.4109 | 454.7112 | ±909.4223 | -1.215 | 0.2244 |  |
| Avg. daily time 54-250 (%) | +36.6828 | 32.6622 | ±65.3244 | +1.123 | 0.2614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1614**, Adj R² = **0.1450**, F-statistic = **9.85** (p = **1.92e-16**), Residual SE = **4143.892** on **563** df, AIC = **11222.5**, BIC = **11274.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20160.9034** | 1377.5521 | ±2755.1042 | **+14.635** | **1.67e-48** | *** |
| Education: graduate level (vs college) | -663.4771 | 390.9008 | ±781.8016 | -1.697 | 0.0896 | . |
| Education: high school or below (vs college) | +812.6052 | 705.1587 | ±1410.3174 | +1.152 | 0.2492 |  |
| Site: UCSD (vs UAB) | +221.1344 | 467.6197 | ±935.2393 | +0.473 | 0.6363 |  |
| Site: UW (vs UAB) | +226.2170 | 409.8444 | ±819.6888 | +0.552 | 0.5810 |  |
| **Age (years)** | **-145.7053** | 15.9904 | ±31.9809 | **-9.112** | **8.09e-20** | *** |
| BMI (kg/m2) | -42.4987 | 27.4561 | ±54.9121 | -1.548 | 0.1217 |  |
| Hypertension | -303.8723 | 405.2551 | ±810.5102 | -0.750 | 0.4534 |  |
| High cholesterol | -53.1588 | 366.3862 | ±732.7725 | -0.145 | 0.8846 |  |
| Kidney disease | -791.9109 | 734.0587 | ±1468.1174 | -1.079 | 0.2807 |  |
| Circulatory disease | -572.2368 | 452.1166 | ±904.2332 | -1.266 | 0.2056 |  |
| Time 181-250, pooled (%) | -14.4335 | 21.8861 | ±43.7722 | -0.659 | 0.5096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **575**, R² = **0.1618**, Adj R² = **0.1454**, F-statistic = **9.88** (p = **1.66e-16**), Residual SE = **4142.767** on **563** df, AIC = **11222.1**, BIC = **11274.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20167.3082** | 1379.0995 | ±2758.1991 | **+14.624** | **1.99e-48** | *** |
| Education: graduate level (vs college) | -665.6183 | 390.4045 | ±780.8090 | -1.705 | 0.0882 | . |
| Education: high school or below (vs college) | +820.3204 | 705.2070 | ±1410.4140 | +1.163 | 0.2447 |  |
| Site: UCSD (vs UAB) | +217.5571 | 468.8253 | ±937.6506 | +0.464 | 0.6426 |  |
| Site: UW (vs UAB) | +219.9334 | 409.9652 | ±819.9305 | +0.536 | 0.5916 |  |
| **Age (years)** | **-145.6340** | 16.0047 | ±32.0094 | **-9.099** | **9.08e-20** | *** |
| BMI (kg/m2) | -42.4121 | 27.4394 | ±54.8788 | -1.546 | 0.1222 |  |
| Hypertension | -298.9556 | 404.1033 | ±808.2067 | -0.740 | 0.4594 |  |
| High cholesterol | -46.2630 | 366.5226 | ±733.0452 | -0.126 | 0.8996 |  |
| Kidney disease | -774.6856 | 732.0717 | ±1464.1435 | -1.058 | 0.2900 |  |
| Circulatory disease | -572.4002 | 451.8978 | ±903.7956 | -1.267 | 0.2053 |  |
| Avg. daily time 181-250 (%) | -17.6447 | 20.6457 | ±41.2914 | -0.855 | 0.3928 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.46e-16**), Residual SE = **4141.740** on **563** df, AIC = **11221.9**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20185.2002** | 1381.3548 | ±2762.7097 | **+14.613** | **2.33e-48** | *** |
| Education: graduate level (vs college) | -672.1950 | 390.8107 | ±781.6213 | -1.720 | 0.0854 | . |
| Education: high school or below (vs college) | +833.5369 | 704.2169 | ±1408.4338 | +1.184 | 0.2366 |  |
| Site: UCSD (vs UAB) | +215.3702 | 469.4671 | ±938.9343 | +0.459 | 0.6464 |  |
| Site: UW (vs UAB) | +210.5426 | 410.2823 | ±820.5646 | +0.513 | 0.6078 |  |
| **Age (years)** | **-145.7211** | 16.0234 | ±32.0468 | **-9.094** | **9.52e-20** | *** |
| BMI (kg/m2) | -42.6278 | 27.4425 | ±54.8851 | -1.553 | 0.1203 |  |
| Hypertension | -293.5943 | 403.3692 | ±806.7384 | -0.728 | 0.4667 |  |
| High cholesterol | -53.9560 | 364.9394 | ±729.8787 | -0.148 | 0.8825 |  |
| Kidney disease | -766.9647 | 727.3540 | ±1454.7081 | -1.054 | 0.2917 |  |
| Circulatory disease | -564.5424 | 452.5856 | ±905.1712 | -1.247 | 0.2123 |  |
| Time > 180 (%) | -14.5333 | 14.5617 | ±29.1234 | -0.998 | 0.3183 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1621**, Adj R² = **0.1458**, F-statistic = **9.90** (p = **1.50e-16**), Residual SE = **4141.949** on **563** df, AIC = **11221.9**, BIC = **11274.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20188.0991** | 1381.3829 | ±2762.7658 | **+14.614** | **2.27e-48** | *** |
| Education: graduate level (vs college) | -671.5183 | 390.5775 | ±781.1550 | -1.719 | 0.0856 | . |
| Education: high school or below (vs college) | +834.5572 | 704.1984 | ±1408.3969 | +1.185 | 0.2360 |  |
| Site: UCSD (vs UAB) | +213.3589 | 469.6439 | ±939.2878 | +0.454 | 0.6496 |  |
| Site: UW (vs UAB) | +211.0102 | 410.1535 | ±820.3069 | +0.514 | 0.6069 |  |
| **Age (years)** | **-145.7857** | 16.0252 | ±32.0504 | **-9.097** | **9.26e-20** | *** |
| BMI (kg/m2) | -42.6877 | 27.4358 | ±54.8717 | -1.556 | 0.1197 |  |
| Hypertension | -295.5615 | 402.8690 | ±805.7381 | -0.734 | 0.4632 |  |
| High cholesterol | -53.4301 | 365.4261 | ±730.8523 | -0.146 | 0.8838 |  |
| Kidney disease | -768.0921 | 726.5975 | ±1453.1950 | -1.057 | 0.2905 |  |
| Circulatory disease | -564.6369 | 452.6414 | ±905.2828 | -1.247 | 0.2122 |  |
| Avg. daily time > 180 (%) | -14.1843 | 14.5056 | ±29.0111 | -0.978 | 0.3281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1626**, Adj R² = **0.1463**, F-statistic = **9.94** (p = **1.28e-16**), Residual SE = **4140.686** on **563** df, AIC = **11221.6**, BIC = **11273.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20180.2711** | 1380.5930 | ±2761.1859 | **+14.617** | **2.18e-48** | *** |
| Education: graduate level (vs college) | -676.1803 | 389.7015 | ±779.4030 | -1.735 | 0.0827 | . |
| Education: high school or below (vs college) | +819.3442 | 707.9268 | ±1415.8535 | +1.157 | 0.2471 |  |
| Site: UCSD (vs UAB) | +211.3012 | 472.2375 | ±944.4749 | +0.447 | 0.6546 |  |
| Site: UW (vs UAB) | +213.7796 | 408.9859 | ±817.9718 | +0.523 | 0.6012 |  |
| **Age (years)** | **-146.3845** | 16.0702 | ±32.1403 | **-9.109** | **8.31e-20** | *** |
| BMI (kg/m2) | -41.7838 | 27.3723 | ±54.7446 | -1.526 | 0.1269 |  |
| Hypertension | -284.7475 | 402.8002 | ±805.6005 | -0.707 | 0.4796 |  |
| High cholesterol | -55.3321 | 365.0961 | ±730.1921 | -0.152 | 0.8795 |  |
| Kidney disease | -814.8635 | 721.5895 | ±1443.1789 | -1.129 | 0.2588 |  |
| Circulatory disease | -557.8745 | 453.5365 | ±907.0730 | -1.230 | 0.2187 |  |
| Nocturnal time > 180 (%) | -16.6306 | 15.4408 | ±30.8816 | -1.077 | 0.2815 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1608**, Adj R² = **0.1444**, F-statistic = **9.81** (p = **2.28e-16**), Residual SE = **4145.299** on **563** df, AIC = **11222.8**, BIC = **11275.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20162.4429** | 1382.4905 | ±2764.9811 | **+14.584** | **3.54e-48** | *** |
| Education: graduate level (vs college) | -646.1765 | 392.9623 | ±785.9247 | -1.644 | 0.1001 |  |
| Education: high school or below (vs college) | +773.7632 | 705.9574 | ±1411.9148 | +1.096 | 0.2731 |  |
| Site: UCSD (vs UAB) | +212.2822 | 460.2952 | ±920.5905 | +0.461 | 0.6447 |  |
| Site: UW (vs UAB) | +245.3992 | 409.8698 | ±819.7396 | +0.599 | 0.5494 |  |
| **Age (years)** | **-147.1892** | 16.0534 | ±32.1067 | **-9.169** | **4.79e-20** | *** |
| BMI (kg/m2) | -42.3409 | 27.7337 | ±55.4674 | -1.527 | 0.1268 |  |
| Hypertension | -341.5049 | 406.6035 | ±813.2070 | -0.840 | 0.4010 |  |
| High cholesterol | -91.0331 | 365.9153 | ±731.8307 | -0.249 | 0.8035 |  |
| Kidney disease | -903.0616 | 732.0779 | ±1464.1557 | -1.234 | 0.2174 |  |
| Circulatory disease | -570.8341 | 451.2208 | ±902.4416 | -1.265 | 0.2058 |  |
| Any reading > 250 during wear (0/1) | +147.2748 | 438.4513 | ±876.9026 | +0.336 | 0.7369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1628**, Adj R² = **0.1464**, F-statistic = **9.95** (p = **1.23e-16**), Residual SE = **4140.320** on **563** df, AIC = **11221.5**, BIC = **11273.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20232.6303** | 1380.3036 | ±2760.6071 | **+14.658** | **1.20e-48** | *** |
| Education: graduate level (vs college) | -676.4742 | 389.5561 | ±779.1121 | -1.737 | 0.0825 | . |
| Education: high school or below (vs college) | +840.7310 | 704.1537 | ±1408.3074 | +1.194 | 0.2325 |  |
| Site: UCSD (vs UAB) | +205.7194 | 468.5634 | ±937.1267 | +0.439 | 0.6606 |  |
| Site: UW (vs UAB) | +200.9867 | 408.6617 | ±817.3234 | +0.492 | 0.6228 |  |
| **Age (years)** | **-146.6048** | 16.0613 | ±32.1226 | **-9.128** | **6.99e-20** | *** |
| BMI (kg/m2) | -43.1663 | 27.3885 | ±54.7770 | -1.576 | 0.1150 |  |
| Hypertension | -300.6915 | 399.8916 | ±799.7833 | -0.752 | 0.4521 |  |
| High cholesterol | -85.1542 | 363.4558 | ±726.9116 | -0.234 | 0.8148 |  |
| Kidney disease | -806.5540 | 717.9546 | ±1435.9093 | -1.123 | 0.2613 |  |
| Circulatory disease | -554.6568 | 453.8010 | ±907.6021 | -1.222 | 0.2216 |  |
| Time > 250 (%) | -37.2300 | 28.6399 | ±57.2798 | -1.300 | 0.1936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1619**, Adj R² = **0.1455**, F-statistic = **9.88** (p = **1.64e-16**), Residual SE = **4142.657** on **563** df, AIC = **11222.1**, BIC = **11274.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20215.1719** | 1380.5096 | ±2761.0191 | **+14.643** | **1.49e-48** | *** |
| Education: graduate level (vs college) | -672.3528 | 389.8129 | ±779.6258 | -1.725 | 0.0846 | . |
| Education: high school or below (vs college) | +833.4882 | 703.4311 | ±1406.8622 | +1.185 | 0.2361 |  |
| Site: UCSD (vs UAB) | +209.8825 | 468.0798 | ±936.1596 | +0.448 | 0.6539 |  |
| Site: UW (vs UAB) | +211.9112 | 408.5128 | ±817.0256 | +0.519 | 0.6039 |  |
| **Age (years)** | **-146.4877** | 16.0568 | ±32.1135 | **-9.123** | **7.30e-20** | *** |
| BMI (kg/m2) | -43.2602 | 27.4245 | ±54.8490 | -1.577 | 0.1147 |  |
| Hypertension | -307.0126 | 400.3429 | ±800.6857 | -0.767 | 0.4432 |  |
| High cholesterol | -82.6854 | 363.8645 | ±727.7289 | -0.227 | 0.8202 |  |
| Kidney disease | -813.2753 | 717.5361 | ±1435.0722 | -1.133 | 0.2570 |  |
| Circulatory disease | -556.2310 | 454.7582 | ±909.5165 | -1.223 | 0.2213 |  |
| Avg. daily time > 250 (%) | -31.5322 | 33.0239 | ±66.0478 | -0.955 | 0.3397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 575; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1658**, F-statistic = **12.40** (p = **1.38e-19**), Residual SE = **12.547** on **564** df, AIC = **4551.5**, BIC = **4599.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9225** | 4.1948 | ±8.3896 | **+13.093** | **3.61e-39** | *** |
| Education: graduate level (vs college) | -1.8636 | 1.1909 | ±2.3819 | -1.565 | 0.1176 |  |
| Education: high school or below (vs college) | +3.0714 | 2.1569 | ±4.3139 | +1.424 | 0.1545 |  |
| Site: UCSD (vs UAB) | +0.0930 | 1.4720 | ±2.9441 | +0.063 | 0.9496 |  |
| Site: UW (vs UAB) | +0.5793 | 1.2428 | ±2.4856 | +0.466 | 0.6411 |  |
| **Age (years)** | **-0.4788** | 0.0488 | ±0.0976 | **-9.813** | **9.87e-23** | *** |
| BMI (kg/m2) | -0.0306 | 0.0806 | ±0.1613 | -0.379 | 0.7045 |  |
| Hypertension | -0.7945 | 1.2017 | ±2.4034 | -0.661 | 0.5085 |  |
| High cholesterol | -0.2534 | 1.0919 | ±2.1838 | -0.232 | 0.8165 |  |
| Kidney disease | -2.5294 | 2.0328 | ±4.0655 | -1.244 | 0.2134 |  |
| Circulatory disease | -1.4825 | 1.3534 | ±2.7068 | -1.095 | 0.2734 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **575**, R² = **0.1875**, Adj R² = **0.1717**, F-statistic = **11.81** (p = **4.91e-20**), Residual SE = **12.502** on **563** df, AIC = **4548.4**, BIC = **4600.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8006** | 6.1233 | ±12.2465 | **+7.806** | **5.88e-15** | *** |
| Education: graduate level (vs college) | -1.6668 | 1.2020 | ±2.4039 | -1.387 | 0.1655 |  |
| Education: high school or below (vs college) | +2.6906 | 2.1192 | ±4.2384 | +1.270 | 0.2042 |  |
| Site: UCSD (vs UAB) | +0.0323 | 1.4665 | ±2.9329 | +0.022 | 0.9824 |  |
| Site: UW (vs UAB) | +0.7875 | 1.2466 | ±2.4932 | +0.632 | 0.5276 |  |
| **Age (years)** | **-0.4943** | 0.0495 | ±0.0990 | **-9.990** | **1.68e-23** | *** |
| BMI (kg/m2) | -0.0445 | 0.0801 | ±0.1601 | -0.556 | 0.5780 |  |
| Hypertension | -1.0285 | 1.2153 | ±2.4307 | -0.846 | 0.3974 |  |
| High cholesterol | -0.4517 | 1.1123 | ±2.2247 | -0.406 | 0.6847 |  |
| Kidney disease | -2.6803 | 1.9832 | ±3.9663 | -1.352 | 0.1765 |  |
| Circulatory disease | -1.4220 | 1.3447 | ±2.6895 | -1.057 | 0.2903 |  |
| HbA1c (%) | +1.4541 | 0.8747 | ±1.7493 | +1.662 | 0.0964 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.03e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0837** | 5.1373 | ±10.2747 | **+10.722** | **8.00e-27** | *** |
| Education: graduate level (vs college) | -1.8639 | 1.1927 | ±2.3854 | -1.563 | 0.1181 |  |
| Education: high school or below (vs college) | +3.0811 | 2.1594 | ±4.3187 | +1.427 | 0.1536 |  |
| Site: UCSD (vs UAB) | +0.0942 | 1.4724 | ±2.9449 | +0.064 | 0.9490 |  |
| Site: UW (vs UAB) | +0.5771 | 1.2474 | ±2.4947 | +0.463 | 0.6436 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.802** | **1.11e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0806 | ±0.1612 | -0.377 | 0.7063 |  |
| Hypertension | -0.7852 | 1.2201 | ±2.4401 | -0.644 | 0.5198 |  |
| High cholesterol | -0.2470 | 1.1030 | ±2.2061 | -0.224 | 0.8228 |  |
| Kidney disease | -2.5148 | 2.0430 | ±4.0860 | -1.231 | 0.2183 |  |
| Circulatory disease | -1.4807 | 1.3573 | ±2.7147 | -1.091 | 0.2753 |  |
| Mean glucose (mg/dL) | -0.0015 | 0.0246 | ±0.0492 | -0.061 | 0.9510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.03e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2928** | 7.6301 | ±15.2602 | **+7.247** | **4.27e-13** | *** |
| Education: graduate level (vs college) | -1.8639 | 1.1927 | ±2.3854 | -1.563 | 0.1181 |  |
| Education: high school or below (vs college) | +3.0811 | 2.1594 | ±4.3187 | +1.427 | 0.1536 |  |
| Site: UCSD (vs UAB) | +0.0942 | 1.4724 | ±2.9449 | +0.064 | 0.9490 |  |
| Site: UW (vs UAB) | +0.5771 | 1.2474 | ±2.4947 | +0.463 | 0.6436 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.802** | **1.11e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0806 | ±0.1612 | -0.377 | 0.7063 |  |
| Hypertension | -0.7852 | 1.2201 | ±2.4401 | -0.644 | 0.5198 |  |
| High cholesterol | -0.2470 | 1.1030 | ±2.2061 | -0.224 | 0.8228 |  |
| Kidney disease | -2.5148 | 2.0430 | ±4.0860 | -1.231 | 0.2183 |  |
| Circulatory disease | -1.4807 | 1.3573 | ±2.7147 | -1.091 | 0.2753 |  |
| GMI (%) | -0.0632 | 1.0276 | ±2.0552 | -0.061 | 0.9510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.27e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.5101** | 5.1395 | ±10.2791 | **+10.411** | **2.20e-25** | *** |
| Education: graduate level (vs college) | -1.8636 | 1.1925 | ±2.3850 | -1.563 | 0.1181 |  |
| Education: high school or below (vs college) | +2.9934 | 2.1623 | ±4.3247 | +1.384 | 0.1663 |  |
| Site: UCSD (vs UAB) | +0.0703 | 1.4651 | ±2.9302 | +0.048 | 0.9617 |  |
| Site: UW (vs UAB) | +0.5852 | 1.2450 | ±2.4899 | +0.470 | 0.6383 |  |
| **Age (years)** | **-0.4779** | 0.0490 | ±0.0980 | **-9.757** | **1.72e-22** | *** |
| BMI (kg/m2) | -0.0346 | 0.0806 | ±0.1612 | -0.429 | 0.6681 |  |
| Hypertension | -0.8774 | 1.2190 | ±2.4379 | -0.720 | 0.4716 |  |
| High cholesterol | -0.3187 | 1.1059 | ±2.2118 | -0.288 | 0.7732 |  |
| Kidney disease | -2.5778 | 2.0282 | ±4.0563 | -1.271 | 0.2037 |  |
| Circulatory disease | -1.4908 | 1.3540 | ±2.7080 | -1.101 | 0.2709 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0131 | 0.0243 | ±0.0486 | +0.541 | 0.5886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1811**, Adj R² = **0.1651**, F-statistic = **11.32** (p = **3.89e-19**), Residual SE = **12.551** on **563** df, AIC = **4553.0**, BIC = **4605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.5045** | 4.3326 | ±8.6651 | **+12.811** | **1.42e-37** | *** |
| Education: graduate level (vs college) | -1.8966 | 1.1921 | ±2.3842 | -1.591 | 0.1116 |  |
| Education: high school or below (vs college) | +3.2503 | 2.1546 | ±4.3093 | +1.509 | 0.1314 |  |
| Site: UCSD (vs UAB) | +0.0915 | 1.4804 | ±2.9608 | +0.062 | 0.9507 |  |
| Site: UW (vs UAB) | +0.4991 | 1.2536 | ±2.5072 | +0.398 | 0.6906 |  |
| **Age (years)** | **-0.4739** | 0.0491 | ±0.0983 | **-9.645** | **5.14e-22** | *** |
| BMI (kg/m2) | -0.0312 | 0.0808 | ±0.1615 | -0.386 | 0.6997 |  |
| Hypertension | -0.7051 | 1.2120 | ±2.4240 | -0.582 | 0.5607 |  |
| High cholesterol | -0.2220 | 1.0995 | ±2.1990 | -0.202 | 0.8400 |  |
| Kidney disease | -2.2326 | 2.0650 | ±4.1299 | -1.081 | 0.2796 |  |
| Circulatory disease | -1.5027 | 1.3600 | ±2.7200 | -1.105 | 0.2692 |  |
| Glucose SD, pooled (mg/dL) | -0.0349 | 0.0495 | ±0.0991 | -0.705 | 0.4809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1820**, Adj R² = **0.1660**, F-statistic = **11.39** (p = **2.91e-19**), Residual SE = **12.544** on **563** df, AIC = **4552.3**, BIC = **4604.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.7743** | 4.3255 | ±8.6510 | **+12.894** | **4.85e-38** | *** |
| Education: graduate level (vs college) | -1.9196 | 1.1920 | ±2.3839 | -1.610 | 0.1073 |  |
| Education: high school or below (vs college) | +3.3684 | 2.1501 | ±4.3001 | +1.567 | 0.1172 |  |
| Site: UCSD (vs UAB) | +0.1043 | 1.4773 | ±2.9546 | +0.071 | 0.9437 |  |
| Site: UW (vs UAB) | +0.4782 | 1.2497 | ±2.4994 | +0.383 | 0.7020 |  |
| **Age (years)** | **-0.4710** | 0.0490 | ±0.0979 | **-9.623** | **6.42e-22** | *** |
| BMI (kg/m2) | -0.0317 | 0.0807 | ±0.1615 | -0.393 | 0.6942 |  |
| Hypertension | -0.6728 | 1.2116 | ±2.4233 | -0.555 | 0.5787 |  |
| High cholesterol | -0.1966 | 1.0981 | ±2.1963 | -0.179 | 0.8579 |  |
| Kidney disease | -2.0890 | 2.0613 | ±4.1227 | -1.013 | 0.3109 |  |
| Circulatory disease | -1.5277 | 1.3562 | ±2.7125 | -1.126 | 0.2600 |  |
| Avg. daily SD (mg/dL) | -0.0590 | 0.0541 | ±0.1081 | -1.092 | 0.2750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **575**, R² = **0.1816**, Adj R² = **0.1656**, F-statistic = **11.35** (p = **3.37e-19**), Residual SE = **12.548** on **563** df, AIC = **4552.6**, BIC = **4604.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.2851** | 4.4666 | ±8.9332 | **+12.601** | **2.07e-36** | *** |
| Education: graduate level (vs college) | -1.9086 | 1.1904 | ±2.3809 | -1.603 | 0.1089 |  |
| Education: high school or below (vs college) | +3.2943 | 2.1562 | ±4.3124 | +1.528 | 0.1266 |  |
| Site: UCSD (vs UAB) | +0.0985 | 1.4774 | ±2.9548 | +0.067 | 0.9469 |  |
| Site: UW (vs UAB) | +0.4582 | 1.2525 | ±2.5049 | +0.366 | 0.7145 |  |
| **Age (years)** | **-0.4702** | 0.0495 | ±0.0990 | **-9.503** | **2.05e-21** | *** |
| BMI (kg/m2) | -0.0332 | 0.0810 | ±0.1619 | -0.410 | 0.6817 |  |
| Hypertension | -0.7173 | 1.2066 | ±2.4133 | -0.594 | 0.5522 |  |
| High cholesterol | -0.2545 | 1.0937 | ±2.1873 | -0.233 | 0.8160 |  |
| Kidney disease | -2.1393 | 2.0676 | ±4.1352 | -1.035 | 0.3008 |  |
| Circulatory disease | -1.5287 | 1.3562 | ±2.7123 | -1.127 | 0.2597 |  |
| CV (%) | -0.0870 | 0.0884 | ±0.1768 | -0.984 | 0.3250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.03e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1015** | 4.9515 | ±9.9029 | **+11.128** | **9.13e-29** | *** |
| Education: graduate level (vs college) | -1.8630 | 1.1924 | ±2.3849 | -1.562 | 0.1182 |  |
| Education: high school or below (vs college) | +3.0567 | 2.1603 | ±4.3206 | +1.415 | 0.1571 |  |
| Site: UCSD (vs UAB) | +0.0907 | 1.4701 | ±2.9402 | +0.062 | 0.9508 |  |
| Site: UW (vs UAB) | +0.5844 | 1.2496 | ±2.4992 | +0.468 | 0.6400 |  |
| **Age (years)** | **-0.4794** | 0.0493 | ±0.0987 | **-9.718** | **2.54e-22** | *** |
| BMI (kg/m2) | -0.0306 | 0.0808 | ±0.1615 | -0.378 | 0.7051 |  |
| Hypertension | -0.7994 | 1.2107 | ±2.4213 | -0.660 | 0.5091 |  |
| High cholesterol | -0.2535 | 1.0938 | ±2.1876 | -0.232 | 0.8167 |  |
| Kidney disease | -2.5488 | 2.0649 | ±4.1298 | -1.234 | 0.2171 |  |
| Circulatory disease | -1.4818 | 1.3549 | ±2.7098 | -1.094 | 0.2741 |  |
| Mean / SD ratio | -0.0271 | 0.4075 | ±0.8150 | -0.067 | 0.9469 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1804**, Adj R² = **0.1644**, F-statistic = **11.27** (p = **4.86e-19**), Residual SE = **12.557** on **563** df, AIC = **4553.5**, BIC = **4605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.7065** | 4.9504 | ±9.9008 | **+11.253** | **2.24e-29** | *** |
| Education: graduate level (vs college) | -1.8597 | 1.1919 | ±2.3838 | -1.560 | 0.1187 |  |
| Education: high school or below (vs college) | +3.0005 | 2.1579 | ±4.3159 | +1.390 | 0.1644 |  |
| Site: UCSD (vs UAB) | +0.0719 | 1.4680 | ±2.9360 | +0.049 | 0.9609 |  |
| Site: UW (vs UAB) | +0.5944 | 1.2450 | ±2.4900 | +0.477 | 0.6331 |  |
| **Age (years)** | **-0.4817** | 0.0493 | ±0.0986 | **-9.769** | **1.53e-22** | *** |
| BMI (kg/m2) | -0.0306 | 0.0807 | ±0.1613 | -0.380 | 0.7041 |  |
| Hypertension | -0.8089 | 1.2080 | ±2.4160 | -0.670 | 0.5031 |  |
| High cholesterol | -0.2581 | 1.0948 | ±2.1895 | -0.236 | 0.8136 |  |
| Kidney disease | -2.6050 | 2.0599 | ±4.1198 | -1.265 | 0.2060 |  |
| Circulatory disease | -1.4746 | 1.3528 | ±2.7055 | -1.090 | 0.2757 |  |
| Avg. daily mean/SD | -0.0977 | 0.3230 | ±0.6459 | -0.302 | 0.7623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **575**, R² = **0.1816**, Adj R² = **0.1656**, F-statistic = **11.36** (p = **3.34e-19**), Residual SE = **12.548** on **563** df, AIC = **4552.6**, BIC = **4604.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7813** | 4.9852 | ±9.9705 | **+10.588** | **3.40e-26** | *** |
| Education: graduate level (vs college) | -1.8392 | 1.1924 | ±2.3848 | -1.542 | 0.1230 |  |
| Education: high school or below (vs college) | +2.9333 | 2.1619 | ±4.3238 | +1.357 | 0.1748 |  |
| Site: UCSD (vs UAB) | +0.0395 | 1.4590 | ±2.9180 | +0.027 | 0.9784 |  |
| Site: UW (vs UAB) | +0.7214 | 1.2595 | ±2.5190 | +0.573 | 0.5668 |  |
| **Age (years)** | **-0.4791** | 0.0488 | ±0.0975 | **-9.822** | **9.01e-23** | *** |
| BMI (kg/m2) | -0.0324 | 0.0805 | ±0.1610 | -0.403 | 0.6871 |  |
| Hypertension | -0.8437 | 1.2065 | ±2.4129 | -0.699 | 0.4843 |  |
| High cholesterol | -0.2392 | 1.0916 | ±2.1832 | -0.219 | 0.8265 |  |
| Kidney disease | -2.6047 | 2.0426 | ±4.0852 | -1.275 | 0.2022 |  |
| Circulatory disease | -1.4705 | 1.3527 | ±2.7053 | -1.087 | 0.2770 |  |
| MAG (mg/dL/h) | +0.0532 | 0.0626 | ±0.1251 | +0.850 | 0.3953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **575**, R² = **0.1811**, Adj R² = **0.1651**, F-statistic = **11.32** (p = **3.86e-19**), Residual SE = **12.551** on **563** df, AIC = **4552.9**, BIC = **4605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8812** | 4.4955 | ±8.9910 | **+12.430** | **1.79e-35** | *** |
| Education: graduate level (vs college) | -1.9044 | 1.1938 | ±2.3876 | -1.595 | 0.1107 |  |
| Education: high school or below (vs college) | +3.2778 | 2.1556 | ±4.3112 | +1.521 | 0.1284 |  |
| Site: UCSD (vs UAB) | +0.1155 | 1.4726 | ±2.9452 | +0.078 | 0.9375 |  |
| Site: UW (vs UAB) | +0.5140 | 1.2521 | ±2.5043 | +0.411 | 0.6814 |  |
| **Age (years)** | **-0.4739** | 0.0490 | ±0.0980 | **-9.671** | **3.99e-22** | *** |
| BMI (kg/m2) | -0.0333 | 0.0811 | ±0.1623 | -0.411 | 0.6812 |  |
| Hypertension | -0.7248 | 1.2100 | ±2.4199 | -0.599 | 0.5492 |  |
| High cholesterol | -0.2182 | 1.0982 | ±2.1965 | -0.199 | 0.8425 |  |
| Kidney disease | -2.2471 | 2.0540 | ±4.1081 | -1.094 | 0.2739 |  |
| Circulatory disease | -1.4945 | 1.3564 | ±2.7129 | -1.102 | 0.2706 |  |
| Avg. daily range (mg/dL) | -0.0109 | 0.0148 | ±0.0296 | -0.735 | 0.4622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **575**, R² = **0.1807**, Adj R² = **0.1647**, F-statistic = **11.29** (p = **4.39e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6429** | 4.2843 | ±8.5687 | **+12.754** | **2.96e-37** | *** |
| Education: graduate level (vs college) | -1.8399 | 1.1970 | ±2.3939 | -1.537 | 0.1243 |  |
| Education: high school or below (vs college) | +3.0472 | 2.1592 | ±4.3184 | +1.411 | 0.1582 |  |
| Site: UCSD (vs UAB) | +0.1167 | 1.4810 | ±2.9620 | +0.079 | 0.9372 |  |
| Site: UW (vs UAB) | +0.6297 | 1.2582 | ±2.5163 | +0.500 | 0.6167 |  |
| **Age (years)** | **-0.4801** | 0.0489 | ±0.0978 | **-9.823** | **9.00e-23** | *** |
| BMI (kg/m2) | -0.0308 | 0.0808 | ±0.1615 | -0.382 | 0.7027 |  |
| Hypertension | -0.8569 | 1.2128 | ±2.4255 | -0.707 | 0.4799 |  |
| High cholesterol | -0.2666 | 1.0971 | ±2.1942 | -0.243 | 0.8080 |  |
| Kidney disease | -2.6562 | 2.0493 | ±4.0986 | -1.296 | 0.1949 |  |
| Circulatory disease | -1.5070 | 1.3530 | ±2.7060 | -1.114 | 0.2653 |  |
| SD of daily means (mg/dL) | +0.0429 | 0.0942 | ±0.1885 | +0.455 | 0.6491 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.24e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4501** | 5.7407 | ±11.4815 | **+9.136** | **6.45e-20** | *** |
| Education: graduate level (vs college) | -1.9052 | 1.1963 | ±2.3926 | -1.593 | 0.1113 |  |
| Education: high school or below (vs college) | +3.1492 | 2.1635 | ±4.3271 | +1.456 | 0.1455 |  |
| Site: UCSD (vs UAB) | +0.0627 | 1.4979 | ±2.9958 | +0.042 | 0.9666 |  |
| Site: UW (vs UAB) | +0.5037 | 1.2548 | ±2.5096 | +0.401 | 0.6881 |  |
| **Age (years)** | **-0.4770** | 0.0488 | ±0.0976 | **-9.778** | **1.40e-22** | *** |
| BMI (kg/m2) | -0.0303 | 0.0808 | ±0.1616 | -0.375 | 0.7073 |  |
| Hypertension | -0.7452 | 1.2067 | ±2.4135 | -0.618 | 0.5369 |  |
| High cholesterol | -0.2113 | 1.1011 | ±2.2022 | -0.192 | 0.8478 |  |
| Kidney disease | -2.3427 | 2.0699 | ±4.1399 | -1.132 | 0.2577 |  |
| Circulatory disease | -1.4691 | 1.3613 | ±2.7227 | -1.079 | 0.2805 |  |
| Time in range 70-180, pooled (%) | +0.0256 | 0.0466 | ±0.0931 | +0.550 | 0.5820 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.27e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4969** | 5.7635 | ±11.5269 | **+9.109** | **8.35e-20** | *** |
| Education: graduate level (vs college) | -1.9054 | 1.1962 | ±2.3924 | -1.593 | 0.1112 |  |
| Education: high school or below (vs college) | +3.1517 | 2.1631 | ±4.3262 | +1.457 | 0.1451 |  |
| Site: UCSD (vs UAB) | +0.0632 | 1.4967 | ±2.9933 | +0.042 | 0.9663 |  |
| Site: UW (vs UAB) | +0.5041 | 1.2546 | ±2.5091 | +0.402 | 0.6878 |  |
| **Age (years)** | **-0.4770** | 0.0488 | ±0.0976 | **-9.776** | **1.43e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0808 | ±0.1616 | -0.376 | 0.7067 |  |
| Hypertension | -0.7480 | 1.2063 | ±2.4127 | -0.620 | 0.5352 |  |
| High cholesterol | -0.2098 | 1.1028 | ±2.2056 | -0.190 | 0.8491 |  |
| Kidney disease | -2.3447 | 2.0675 | ±4.1349 | -1.134 | 0.2568 |  |
| Circulatory disease | -1.4689 | 1.3613 | ±2.7226 | -1.079 | 0.2806 |  |
| Avg. daily time in range 70-180 (%) | +0.0250 | 0.0462 | ±0.0923 | +0.541 | 0.5884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1815**, Adj R² = **0.1655**, F-statistic = **11.35** (p = **3.42e-19**), Residual SE = **12.548** on **563** df, AIC = **4552.7**, BIC = **4604.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.3254** | 4.2465 | ±8.4930 | **+13.028** | **8.43e-39** | *** |
| Education: graduate level (vs college) | -1.8906 | 1.1916 | ±2.3831 | -1.587 | 0.1126 |  |
| Education: high school or below (vs college) | +2.9932 | 2.1573 | ±4.3145 | +1.388 | 0.1653 |  |
| Site: UCSD (vs UAB) | -0.0855 | 1.4967 | ±2.9934 | -0.057 | 0.9544 |  |
| Site: UW (vs UAB) | +0.4273 | 1.2510 | ±2.5021 | +0.342 | 0.7327 |  |
| **Age (years)** | **-0.4781** | 0.0488 | ±0.0976 | **-9.802** | **1.11e-22** | *** |
| BMI (kg/m2) | -0.0320 | 0.0809 | ±0.1617 | -0.396 | 0.6923 |  |
| Hypertension | -0.8392 | 1.2019 | ±2.4037 | -0.698 | 0.4850 |  |
| High cholesterol | -0.3253 | 1.0957 | ±2.1914 | -0.297 | 0.7666 |  |
| Kidney disease | -2.4960 | 2.0295 | ±4.0591 | -1.230 | 0.2188 |  |
| Circulatory disease | -1.4738 | 1.3556 | ±2.7113 | -1.087 | 0.2770 |  |
| Time < 54 (%) | -0.5354 | 0.3859 | ±0.7718 | -1.387 | 0.1654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **575**, R² = **0.1821**, Adj R² = **0.1662**, F-statistic = **11.40** (p = **2.78e-19**), Residual SE = **12.543** on **563** df, AIC = **4552.2**, BIC = **4604.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1893** | 4.2192 | ±8.4385 | **+13.080** | **4.26e-39** | *** |
| Education: graduate level (vs college) | -1.9294 | 1.1953 | ±2.3905 | -1.614 | 0.1065 |  |
| Education: high school or below (vs college) | +2.9696 | 2.1563 | ±4.3125 | +1.377 | 0.1684 |  |
| Site: UCSD (vs UAB) | -0.0951 | 1.4951 | ±2.9901 | -0.064 | 0.9493 |  |
| Site: UW (vs UAB) | +0.3731 | 1.2534 | ±2.5067 | +0.298 | 0.7659 |  |
| **Age (years)** | **-0.4754** | 0.0488 | ±0.0976 | **-9.740** | **2.03e-22** | *** |
| BMI (kg/m2) | -0.0318 | 0.0808 | ±0.1616 | -0.393 | 0.6940 |  |
| Hypertension | -0.8506 | 1.2013 | ±2.4026 | -0.708 | 0.4789 |  |
| High cholesterol | -0.3483 | 1.0934 | ±2.1867 | -0.319 | 0.7501 |  |
| Kidney disease | -2.4713 | 2.0280 | ±4.0561 | -1.219 | 0.2230 |  |
| Circulatory disease | -1.4644 | 1.3540 | ±2.7080 | -1.082 | 0.2795 |  |
| Avg. daily time < 54 (%) | -0.7683 | 0.5185 | ±1.0370 | -1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.25e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1634** | 4.2325 | ±8.4650 | **+13.033** | **7.91e-39** | *** |
| Education: graduate level (vs college) | -1.9108 | 1.1911 | ±2.3821 | -1.604 | 0.1087 |  |
| Education: high school or below (vs college) | +3.0738 | 2.1644 | ±4.3288 | +1.420 | 0.1556 |  |
| Site: UCSD (vs UAB) | +0.0245 | 1.4689 | ±2.9378 | +0.017 | 0.9867 |  |
| Site: UW (vs UAB) | +0.4995 | 1.2368 | ±2.4735 | +0.404 | 0.6863 |  |
| **Age (years)** | **-0.4776** | 0.0488 | ±0.0977 | **-9.779** | **1.38e-22** | *** |
| BMI (kg/m2) | -0.0308 | 0.0812 | ±0.1625 | -0.379 | 0.7049 |  |
| Hypertension | -0.8309 | 1.2087 | ±2.4174 | -0.687 | 0.4918 |  |
| High cholesterol | -0.2802 | 1.0946 | ±2.1891 | -0.256 | 0.7979 |  |
| Kidney disease | -2.5022 | 2.0326 | ±4.0652 | -1.231 | 0.2183 |  |
| Circulatory disease | -1.5054 | 1.3538 | ±2.7076 | -1.112 | 0.2662 |  |
| Time 54-69, pooled (%) | -0.1380 | 0.2140 | ±0.4280 | -0.645 | 0.5191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **575**, R² = **0.1809**, Adj R² = **0.1649**, F-statistic = **11.31** (p = **4.10e-19**), Residual SE = **12.553** on **563** df, AIC = **4553.1**, BIC = **4605.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1087** | 4.2172 | ±8.4345 | **+13.067** | **5.05e-39** | *** |
| Education: graduate level (vs college) | -1.9184 | 1.1910 | ±2.3820 | -1.611 | 0.1072 |  |
| Education: high school or below (vs college) | +3.0760 | 2.1656 | ±4.3311 | +1.420 | 0.1555 |  |
| Site: UCSD (vs UAB) | +0.0285 | 1.4681 | ±2.9362 | +0.019 | 0.9845 |  |
| Site: UW (vs UAB) | +0.4870 | 1.2374 | ±2.4748 | +0.394 | 0.6939 |  |
| **Age (years)** | **-0.4767** | 0.0489 | ±0.0978 | **-9.749** | **1.87e-22** | *** |
| BMI (kg/m2) | -0.0307 | 0.0812 | ±0.1624 | -0.378 | 0.7057 |  |
| Hypertension | -0.8314 | 1.2088 | ±2.4177 | -0.688 | 0.4916 |  |
| High cholesterol | -0.2804 | 1.0936 | ±2.1873 | -0.256 | 0.7976 |  |
| Kidney disease | -2.5004 | 2.0316 | ±4.0632 | -1.231 | 0.2184 |  |
| Circulatory disease | -1.5063 | 1.3530 | ±2.7060 | -1.113 | 0.2656 |  |
| Avg. daily time 54-69 (%) | -0.1456 | 0.2073 | ±0.4145 | -0.702 | 0.4825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **575**, R² = **0.1812**, Adj R² = **0.1652**, F-statistic = **11.32** (p = **3.82e-19**), Residual SE = **12.551** on **563** df, AIC = **4552.9**, BIC = **4605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2768** | 4.2474 | ±8.4949 | **+13.014** | **1.02e-38** | *** |
| Education: graduate level (vs college) | -1.9192 | 1.1915 | ±2.3829 | -1.611 | 0.1072 |  |
| Education: high school or below (vs college) | +3.0531 | 2.1625 | ±4.3251 | +1.412 | 0.1580 |  |
| Site: UCSD (vs UAB) | -0.0247 | 1.4746 | ±2.9492 | -0.017 | 0.9867 |  |
| Site: UW (vs UAB) | +0.4570 | 1.2393 | ±2.4785 | +0.369 | 0.7123 |  |
| **Age (years)** | **-0.4774** | 0.0488 | ±0.0976 | **-9.781** | **1.35e-22** | *** |
| BMI (kg/m2) | -0.0311 | 0.0813 | ±0.1625 | -0.383 | 0.7015 |  |
| Hypertension | -0.8438 | 1.2079 | ±2.4157 | -0.699 | 0.4848 |  |
| High cholesterol | -0.3000 | 1.0954 | ±2.1907 | -0.274 | 0.7842 |  |
| Kidney disease | -2.4926 | 2.0310 | ±4.0619 | -1.227 | 0.2197 |  |
| Circulatory disease | -1.5037 | 1.3545 | ±2.7091 | -1.110 | 0.2669 |  |
| Time < 70 (%) | -0.1418 | 0.1647 | ±0.3295 | -0.861 | 0.3893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **575**, R² = **0.1813**, Adj R² = **0.1653**, F-statistic = **11.34** (p = **3.61e-19**), Residual SE = **12.550** on **563** df, AIC = **4552.8**, BIC = **4605.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1705** | 4.2230 | ±8.4459 | **+13.064** | **5.26e-39** | *** |
| Education: graduate level (vs college) | -1.9341 | 1.1921 | ±2.3843 | -1.622 | 0.1047 |  |
| Education: high school or below (vs college) | +3.0561 | 2.1635 | ±4.3270 | +1.413 | 0.1578 |  |
| Site: UCSD (vs UAB) | -0.0119 | 1.4720 | ±2.9440 | -0.008 | 0.9936 |  |
| Site: UW (vs UAB) | +0.4416 | 1.2398 | ±2.4797 | +0.356 | 0.7217 |  |
| **Age (years)** | **-0.4760** | 0.0489 | ±0.0978 | **-9.738** | **2.08e-22** | *** |
| BMI (kg/m2) | -0.0309 | 0.0812 | ±0.1625 | -0.381 | 0.7035 |  |
| Hypertension | -0.8443 | 1.2080 | ±2.4160 | -0.699 | 0.4846 |  |
| High cholesterol | -0.3005 | 1.0937 | ±2.1873 | -0.275 | 0.7835 |  |
| Kidney disease | -2.4875 | 2.0301 | ±4.0602 | -1.225 | 0.2205 |  |
| Circulatory disease | -1.5038 | 1.3530 | ±2.7060 | -1.111 | 0.2664 |  |
| Avg. daily time < 70 (%) | -0.1525 | 0.1660 | ±0.3321 | -0.918 | 0.3584 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1809**, Adj R² = **0.1649**, F-statistic = **11.30** (p = **4.19e-19**), Residual SE = **12.553** on **563** df, AIC = **4553.1**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3208** | 11.2931 | ±22.5862 | **+4.367** | **1.26e-05** | *** |
| Education: graduate level (vs college) | -1.9006 | 1.1926 | ±2.3852 | -1.594 | 0.1110 |  |
| Education: high school or below (vs college) | +3.1451 | 2.1640 | ±4.3280 | +1.453 | 0.1461 |  |
| Site: UCSD (vs UAB) | +0.0510 | 1.4972 | ±2.9943 | +0.034 | 0.9728 |  |
| Site: UW (vs UAB) | +0.5015 | 1.2522 | ±2.5044 | +0.400 | 0.6888 |  |
| **Age (years)** | **-0.4788** | 0.0488 | ±0.0977 | **-9.804** | **1.08e-22** | *** |
| BMI (kg/m2) | -0.0313 | 0.0807 | ±0.1614 | -0.387 | 0.6985 |  |
| Hypertension | -0.7593 | 1.2011 | ±2.4022 | -0.632 | 0.5272 |  |
| High cholesterol | -0.2651 | 1.0939 | ±2.1879 | -0.242 | 0.8086 |  |
| Kidney disease | -2.4294 | 2.0410 | ±4.0820 | -1.190 | 0.2339 |  |
| Circulatory disease | -1.4512 | 1.3652 | ±2.7304 | -1.063 | 0.2878 |  |
| Time 54-250, pooled (%) | +0.0574 | 0.1090 | ±0.2180 | +0.527 | 0.5984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1804**, Adj R² = **0.1644**, F-statistic = **11.27** (p = **4.84e-19**), Residual SE = **12.557** on **563** df, AIC = **4553.4**, BIC = **4605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0011** | 12.2963 | ±24.5926 | **+4.229** | **2.35e-05** | *** |
| Education: graduate level (vs college) | -1.8831 | 1.1941 | ±2.3882 | -1.577 | 0.1148 |  |
| Education: high school or below (vs college) | +3.1108 | 2.1601 | ±4.3202 | +1.440 | 0.1498 |  |
| Site: UCSD (vs UAB) | +0.0757 | 1.4930 | ±2.9860 | +0.051 | 0.9596 |  |
| Site: UW (vs UAB) | +0.5440 | 1.2515 | ±2.5030 | +0.435 | 0.6638 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.798** | **1.15e-22** | *** |
| BMI (kg/m2) | -0.0310 | 0.0808 | ±0.1616 | -0.384 | 0.7008 |  |
| Hypertension | -0.7782 | 1.2029 | ±2.4059 | -0.647 | 0.5177 |  |
| High cholesterol | -0.2572 | 1.0947 | ±2.1894 | -0.235 | 0.8143 |  |
| Kidney disease | -2.4745 | 2.0392 | ±4.0784 | -1.213 | 0.2250 |  |
| Circulatory disease | -1.4647 | 1.3655 | ±2.7309 | -1.073 | 0.2834 |  |
| Avg. daily time 54-250 (%) | +0.0297 | 0.1192 | ±0.2385 | +0.249 | 0.8030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1804**, Adj R² = **0.1644**, F-statistic = **11.27** (p = **4.83e-19**), Residual SE = **12.557** on **563** df, AIC = **4553.4**, BIC = **4605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9106** | 4.1966 | ±8.3932 | **+13.084** | **4.04e-39** | *** |
| Education: graduate level (vs college) | -1.8752 | 1.1956 | ±2.3911 | -1.569 | 0.1168 |  |
| Education: high school or below (vs college) | +3.1033 | 2.1593 | ±4.3187 | +1.437 | 0.1507 |  |
| Site: UCSD (vs UAB) | +0.0938 | 1.4798 | ±2.9596 | +0.063 | 0.9495 |  |
| Site: UW (vs UAB) | +0.5606 | 1.2499 | ±2.4998 | +0.449 | 0.6538 |  |
| **Age (years)** | **-0.4777** | 0.0487 | ±0.0975 | **-9.800** | **1.13e-22** | *** |
| BMI (kg/m2) | -0.0302 | 0.0807 | ±0.1614 | -0.374 | 0.7085 |  |
| Hypertension | -0.7656 | 1.2139 | ±2.4279 | -0.631 | 0.5283 |  |
| High cholesterol | -0.2159 | 1.1083 | ±2.2167 | -0.195 | 0.8456 |  |
| Kidney disease | -2.4311 | 2.0807 | ±4.1614 | -1.168 | 0.2426 |  |
| Circulatory disease | -1.4798 | 1.3584 | ±2.7169 | -1.089 | 0.2760 |  |
| Time 181-250, pooled (%) | -0.0184 | 0.0662 | ±0.1324 | -0.278 | 0.7813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.50e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9177** | 4.2006 | ±8.4013 | **+13.074** | **4.66e-39** | *** |
| Education: graduate level (vs college) | -1.8822 | 1.1943 | ±2.3887 | -1.576 | 0.1150 |  |
| Education: high school or below (vs college) | +3.1255 | 2.1598 | ±4.3195 | +1.447 | 0.1479 |  |
| Site: UCSD (vs UAB) | +0.0881 | 1.4841 | ±2.9682 | +0.059 | 0.9527 |  |
| Site: UW (vs UAB) | +0.5447 | 1.2503 | ±2.5007 | +0.436 | 0.6631 |  |
| **Age (years)** | **-0.4772** | 0.0487 | ±0.0975 | **-9.791** | **1.23e-22** | *** |
| BMI (kg/m2) | -0.0299 | 0.0807 | ±0.1613 | -0.371 | 0.7109 |  |
| Hypertension | -0.7489 | 1.2115 | ±2.4230 | -0.618 | 0.5365 |  |
| High cholesterol | -0.1934 | 1.1087 | ±2.2174 | -0.174 | 0.8615 |  |
| Kidney disease | -2.3735 | 2.0761 | ±4.1522 | -1.143 | 0.2529 |  |
| Circulatory disease | -1.4793 | 1.3588 | ±2.7175 | -1.089 | 0.2763 |  |
| Avg. daily time 181-250 (%) | -0.0291 | 0.0631 | ±0.1263 | -0.461 | 0.6445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1645**, F-statistic = **11.28** (p = **4.62e-19**), Residual SE = **12.556** on **563** df, AIC = **4553.3**, BIC = **4605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9413** | 4.2075 | ±8.4151 | **+13.058** | **5.73e-39** | *** |
| Education: graduate level (vs college) | -1.8859 | 1.1954 | ±2.3908 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +3.1290 | 2.1593 | ±4.3186 | +1.449 | 0.1473 |  |
| Site: UCSD (vs UAB) | +0.0866 | 1.4860 | ±2.9719 | +0.058 | 0.9536 |  |
| Site: UW (vs UAB) | +0.5413 | 1.2516 | ±2.5033 | +0.432 | 0.6654 |  |
| **Age (years)** | **-0.4777** | 0.0488 | ±0.0976 | **-9.789** | **1.25e-22** | *** |
| BMI (kg/m2) | -0.0303 | 0.0807 | ±0.1615 | -0.376 | 0.7071 |  |
| Hypertension | -0.7532 | 1.2096 | ±2.4193 | -0.623 | 0.5335 |  |
| High cholesterol | -0.2175 | 1.1033 | ±2.2066 | -0.197 | 0.8437 |  |
| Kidney disease | -2.4015 | 2.0664 | ±4.1328 | -1.162 | 0.2452 |  |
| Circulatory disease | -1.4702 | 1.3605 | ±2.7209 | -1.081 | 0.2798 |  |
| Time > 180 (%) | -0.0182 | 0.0471 | ±0.0942 | -0.386 | 0.6993 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1805**, Adj R² = **0.1645**, F-statistic = **11.27** (p = **4.67e-19**), Residual SE = **12.556** on **563** df, AIC = **4553.4**, BIC = **4605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9439** | 4.2080 | ±8.4161 | **+13.057** | **5.80e-39** | *** |
| Education: graduate level (vs college) | -1.8842 | 1.1951 | ±2.3903 | -1.577 | 0.1149 |  |
| Education: high school or below (vs college) | +3.1277 | 2.1582 | ±4.3164 | +1.449 | 0.1473 |  |
| Site: UCSD (vs UAB) | +0.0844 | 1.4871 | ±2.9742 | +0.057 | 0.9547 |  |
| Site: UW (vs UAB) | +0.5435 | 1.2514 | ±2.5028 | +0.434 | 0.6641 |  |
| **Age (years)** | **-0.4778** | 0.0488 | ±0.0976 | **-9.794** | **1.20e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0807 | ±0.1615 | -0.377 | 0.7063 |  |
| Hypertension | -0.7573 | 1.2090 | ±2.4181 | -0.626 | 0.5311 |  |
| High cholesterol | -0.2185 | 1.1045 | ±2.2091 | -0.198 | 0.8432 |  |
| Kidney disease | -2.4084 | 2.0637 | ±4.1273 | -1.167 | 0.2432 |  |
| Circulatory disease | -1.4709 | 1.3605 | ±2.7211 | -1.081 | 0.2796 |  |
| Avg. daily time > 180 (%) | -0.0170 | 0.0468 | ±0.0937 | -0.363 | 0.7169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.54e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9348** | 4.2059 | ±8.4118 | **+13.061** | **5.47e-39** | *** |
| Education: graduate level (vs college) | -1.8902 | 1.1931 | ±2.3862 | -1.584 | 0.1131 |  |
| Education: high school or below (vs college) | +3.1102 | 2.1646 | ±4.3291 | +1.437 | 0.1508 |  |
| Site: UCSD (vs UAB) | +0.0818 | 1.4929 | ±2.9858 | +0.055 | 0.9563 |  |
| Site: UW (vs UAB) | +0.5462 | 1.2491 | ±2.4982 | +0.437 | 0.6619 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.801** | **1.12e-22** | *** |
| BMI (kg/m2) | -0.0293 | 0.0806 | ±0.1611 | -0.364 | 0.7160 |  |
| Hypertension | -0.7435 | 1.2077 | ±2.4153 | -0.616 | 0.5381 |  |
| High cholesterol | -0.2202 | 1.1034 | ±2.2068 | -0.200 | 0.8419 |  |
| Kidney disease | -2.4633 | 2.0480 | ±4.0960 | -1.203 | 0.2291 |  |
| Circulatory disease | -1.4624 | 1.3621 | ±2.7242 | -1.074 | 0.2830 |  |
| Nocturnal time > 180 (%) | -0.0203 | 0.0513 | ±0.1026 | -0.395 | 0.6927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.51e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8910** | 4.2099 | ±8.4198 | **+13.039** | **7.38e-39** | *** |
| Education: graduate level (vs college) | -1.8306 | 1.1992 | ±2.3984 | -1.527 | 0.1269 |  |
| Education: high school or below (vs college) | +3.0156 | 2.1632 | ±4.3264 | +1.394 | 0.1633 |  |
| Site: UCSD (vs UAB) | +0.0597 | 1.4561 | ±2.9121 | +0.041 | 0.9673 |  |
| Site: UW (vs UAB) | +0.5976 | 1.2475 | ±2.4951 | +0.479 | 0.6319 |  |
| **Age (years)** | **-0.4813** | 0.0486 | ±0.0973 | **-9.895** | **4.36e-23** | *** |
| BMI (kg/m2) | -0.0286 | 0.0816 | ±0.1632 | -0.351 | 0.7258 |  |
| Hypertension | -0.8548 | 1.2217 | ±2.4435 | -0.700 | 0.4841 |  |
| High cholesterol | -0.2876 | 1.1032 | ±2.2064 | -0.261 | 0.7943 |  |
| Kidney disease | -2.6669 | 2.0755 | ±4.1510 | -1.285 | 0.1988 |  |
| Circulatory disease | -1.4683 | 1.3544 | ±2.7088 | -1.084 | 0.2783 |  |
| Any reading > 250 during wear (0/1) | +0.5963 | 1.3052 | ±2.6105 | +0.457 | 0.6478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.50e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9994** | 4.2072 | ±8.4144 | **+13.073** | **4.71e-39** | *** |
| Education: graduate level (vs college) | -1.8909 | 1.1924 | ±2.3848 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +3.1370 | 2.1626 | ±4.3251 | +1.451 | 0.1469 |  |
| Site: UCSD (vs UAB) | +0.0748 | 1.4885 | ±2.9771 | +0.050 | 0.9599 |  |
| Site: UW (vs UAB) | +0.5301 | 1.2490 | ±2.4981 | +0.424 | 0.6713 |  |
| **Age (years)** | **-0.4788** | 0.0488 | ±0.0977 | **-9.804** | **1.09e-22** | *** |
| BMI (kg/m2) | -0.0310 | 0.0807 | ±0.1614 | -0.384 | 0.7009 |  |
| Hypertension | -0.7626 | 1.2018 | ±2.4037 | -0.635 | 0.5257 |  |
| High cholesterol | -0.2566 | 1.0949 | ±2.1898 | -0.234 | 0.8147 |  |
| Kidney disease | -2.4523 | 2.0408 | ±4.0815 | -1.202 | 0.2295 |  |
| Circulatory disease | -1.4582 | 1.3645 | ±2.7291 | -1.069 | 0.2852 |  |
| Time > 250 (%) | -0.0459 | 0.1115 | ±0.2230 | -0.412 | 0.6807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.00e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9412** | 4.2089 | ±8.4177 | **+13.054** | **6.05e-39** | *** |
| Education: graduate level (vs college) | -1.8711 | 1.1934 | ±2.3868 | -1.568 | 0.1169 |  |
| Education: high school or below (vs college) | +3.0905 | 2.1571 | ±4.3143 | +1.433 | 0.1519 |  |
| Site: UCSD (vs UAB) | +0.0886 | 1.4855 | ±2.9711 | +0.060 | 0.9525 |  |
| Site: UW (vs UAB) | +0.5672 | 1.2484 | ±2.4969 | +0.454 | 0.6496 |  |
| **Age (years)** | **-0.4787** | 0.0488 | ±0.0977 | **-9.800** | **1.12e-22** | *** |
| BMI (kg/m2) | -0.0308 | 0.0808 | ±0.1616 | -0.381 | 0.7034 |  |
| Hypertension | -0.7864 | 1.2038 | ±2.4075 | -0.653 | 0.5136 |  |
| High cholesterol | -0.2534 | 1.0956 | ±2.1911 | -0.231 | 0.8171 |  |
| Kidney disease | -2.5062 | 2.0373 | ±4.0747 | -1.230 | 0.2187 |  |
| Circulatory disease | -1.4750 | 1.3643 | ±2.7287 | -1.081 | 0.2797 |  |
| Avg. daily time > 250 (%) | -0.0131 | 0.1205 | ±0.2410 | -0.109 | 0.9134 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 576; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **576**, R² = **0.1842**, Adj R² = **0.1698**, F-statistic = **12.76** (p = **3.49e-20**), Residual SE = **7.926** on **565** df, AIC = **4030.4**, BIC = **4078.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4532** | 2.6221 | ±5.2442 | **+26.488** | **1.34e-154** | *** |
| Education: graduate level (vs college) | -1.2153 | 0.7312 | ±1.4624 | -1.662 | 0.0965 | . |
| Education: high school or below (vs college) | -0.2904 | 1.2064 | ±2.4127 | -0.241 | 0.8097 |  |
| **Site: UCSD (vs UAB)** | **-2.5191** | 0.9408 | ±1.8815 | **-2.678** | **0.0074** | ** |
| **Site: UW (vs UAB)** | **-3.0730** | 0.7943 | ±1.5886 | **-3.869** | **1.09e-04** | *** |
| **Age (years)** | **-0.1882** | 0.0308 | ±0.0616 | **-6.107** | **1.01e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0977 | **+4.062** | **4.86e-05** | *** |
| Hypertension | +1.3386 | 0.7535 | ±1.5070 | +1.776 | 0.0757 | . |
| High cholesterol | +0.2025 | 0.7075 | ±1.4150 | +0.286 | 0.7747 |  |
| Kidney disease | +0.9985 | 1.3696 | ±2.7391 | +0.729 | 0.4660 |  |
| Circulatory disease | -0.4305 | 0.9073 | ±1.8146 | -0.475 | 0.6351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **576**, R² = **0.1989**, Adj R² = **0.1832**, F-statistic = **12.73** (p = **1.11e-21**), Residual SE = **7.862** on **564** df, AIC = **4022.0**, BIC = **4074.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0921** | 3.6648 | ±7.3296 | **+17.216** | **2.02e-66** | *** |
| Education: graduate level (vs college) | -1.0349 | 0.7331 | ±1.4662 | -1.412 | 0.1580 |  |
| Education: high school or below (vs college) | -0.6931 | 1.1694 | ±2.3387 | -0.593 | 0.5534 |  |
| **Site: UCSD (vs UAB)** | **-2.6093** | 0.9338 | ±1.8676 | **-2.794** | **0.0052** | ** |
| **Site: UW (vs UAB)** | **-2.8883** | 0.7906 | ±1.5812 | **-3.653** | **2.59e-04** | *** |
| **Age (years)** | **-0.2017** | 0.0306 | ±0.0611 | **-6.602** | **4.06e-11** | *** |
| **BMI (kg/m2)** | **+0.1859** | 0.0480 | ±0.0960 | **+3.872** | **1.08e-04** | *** |
| Hypertension | +1.1147 | 0.7536 | ±1.5072 | +1.479 | 0.1391 |  |
| High cholesterol | +0.0344 | 0.7079 | ±1.4158 | +0.049 | 0.9612 |  |
| Kidney disease | +0.8663 | 1.3390 | ±2.6780 | +0.647 | 0.5176 |  |
| Circulatory disease | -0.3595 | 0.9062 | ±1.8124 | -0.397 | 0.6916 |  |
| **HbA1c (%)** | **+1.2969** | 0.5092 | ±1.0183 | **+2.547** | **0.0109** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **576**, R² = **0.1950**, Adj R² = **0.1793**, F-statistic = **12.42** (p = **3.91e-21**), Residual SE = **7.881** on **564** df, AIC = **4024.7**, BIC = **4077.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.4124** | 3.1378 | ±6.2757 | **+20.846** | **1.64e-96** | *** |
| Education: graduate level (vs college) | -1.2003 | 0.7319 | ±1.4637 | -1.640 | 0.1010 |  |
| Education: high school or below (vs college) | -0.5970 | 1.1784 | ±2.3569 | -0.507 | 0.6124 |  |
| **Site: UCSD (vs UAB)** | **-2.5832** | 0.9338 | ±1.8677 | **-2.766** | **0.0057** | ** |
| **Site: UW (vs UAB)** | **-3.0221** | 0.7871 | ±1.5742 | **-3.840** | **1.23e-04** | *** |
| **Age (years)** | **-0.1905** | 0.0304 | ±0.0608 | **-6.270** | **3.61e-10** | *** |
| **BMI (kg/m2)** | **+0.1927** | 0.0486 | ±0.0971 | **+3.968** | **7.26e-05** | *** |
| Hypertension | +1.0931 | 0.7658 | ±1.5317 | +1.427 | 0.1535 |  |
| High cholesterol | +0.0508 | 0.7017 | ±1.4033 | +0.072 | 0.9422 |  |
| Kidney disease | +0.6359 | 1.3284 | ±2.6569 | +0.479 | 0.6322 |  |
| Circulatory disease | -0.4583 | 0.9140 | ±1.8280 | -0.501 | 0.6160 |  |
| **Mean glucose (mg/dL)** | **+0.0377** | 0.0158 | ±0.0316 | **+2.385** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **576**, R² = **0.1950**, Adj R² = **0.1793**, F-statistic = **12.42** (p = **3.91e-21**), Residual SE = **7.881** on **564** df, AIC = **4024.7**, BIC = **4077.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1922** | 4.7275 | ±9.4550 | **+12.732** | **3.91e-37** | *** |
| Education: graduate level (vs college) | -1.2003 | 0.7319 | ±1.4637 | -1.640 | 0.1010 |  |
| Education: high school or below (vs college) | -0.5970 | 1.1784 | ±2.3569 | -0.507 | 0.6124 |  |
| **Site: UCSD (vs UAB)** | **-2.5832** | 0.9338 | ±1.8677 | **-2.766** | **0.0057** | ** |
| **Site: UW (vs UAB)** | **-3.0221** | 0.7871 | ±1.5742 | **-3.840** | **1.23e-04** | *** |
| **Age (years)** | **-0.1905** | 0.0304 | ±0.0608 | **-6.270** | **3.61e-10** | *** |
| **BMI (kg/m2)** | **+0.1927** | 0.0486 | ±0.0971 | **+3.968** | **7.26e-05** | *** |
| Hypertension | +1.0931 | 0.7658 | ±1.5317 | +1.427 | 0.1535 |  |
| High cholesterol | +0.0508 | 0.7017 | ±1.4033 | +0.072 | 0.9422 |  |
| Kidney disease | +0.6359 | 1.3284 | ±2.6569 | +0.479 | 0.6322 |  |
| Circulatory disease | -0.4583 | 0.9140 | ±1.8280 | -0.501 | 0.6160 |  |
| **GMI (%)** | **+1.5771** | 0.6614 | ±1.3228 | **+2.385** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **576**, R² = **0.1915**, Adj R² = **0.1758**, F-statistic = **12.15** (p = **1.22e-20**), Residual SE = **7.898** on **564** df, AIC = **4027.2**, BIC = **4079.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1123** | 3.0951 | ±6.1902 | **+21.360** | **3.14e-101** | *** |
| Education: graduate level (vs college) | -1.2088 | 0.7324 | ±1.4648 | -1.650 | 0.0989 | . |
| Education: high school or below (vs college) | -0.5139 | 1.1796 | ±2.3592 | -0.436 | 0.6631 |  |
| **Site: UCSD (vs UAB)** | **-2.5920** | 0.9382 | ±1.8764 | **-2.763** | **0.0057** | ** |
| **Site: UW (vs UAB)** | **-3.0583** | 0.7896 | ±1.5792 | **-3.873** | **1.07e-04** | *** |
| **Age (years)** | **-0.1860** | 0.0307 | ±0.0614 | **-6.060** | **1.36e-09** | *** |
| **BMI (kg/m2)** | **+0.1891** | 0.0487 | ±0.0975 | **+3.880** | **1.04e-04** | *** |
| Hypertension | +1.1350 | 0.7667 | ±1.5335 | +1.480 | 0.1388 |  |
| High cholesterol | +0.0514 | 0.7004 | ±1.4009 | +0.073 | 0.9415 |  |
| Kidney disease | +0.8842 | 1.3231 | ±2.6462 | +0.668 | 0.5040 |  |
| Circulatory disease | -0.4408 | 0.9122 | ±1.8244 | -0.483 | 0.6290 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0310** | 0.0145 | ±0.0290 | **+2.138** | **0.0325** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **576**, R² = **0.1961**, Adj R² = **0.1804**, F-statistic = **12.50** (p = **2.78e-21**), Residual SE = **7.876** on **564** df, AIC = **4024.0**, BIC = **4076.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0470** | 2.6580 | ±5.3159 | **+25.601** | **1.48e-144** | *** |
| Education: graduate level (vs college) | -1.1274 | 0.7339 | ±1.4678 | -1.536 | 0.1245 |  |
| Education: high school or below (vs college) | -0.7839 | 1.1924 | ±2.3848 | -0.657 | 0.5109 |  |
| **Site: UCSD (vs UAB)** | **-2.5491** | 0.9284 | ±1.8568 | **-2.746** | **0.0060** | ** |
| **Site: UW (vs UAB)** | **-2.8820** | 0.7869 | ±1.5737 | **-3.663** | **2.50e-04** | *** |
| **Age (years)** | **-0.1994** | 0.0308 | ±0.0616 | **-6.474** | **9.53e-11** | *** |
| **BMI (kg/m2)** | **+0.1998** | 0.0484 | ±0.0967 | **+4.132** | **3.60e-05** | *** |
| Hypertension | +1.1119 | 0.7618 | ±1.5236 | +1.460 | 0.1444 |  |
| High cholesterol | +0.1339 | 0.7055 | ±1.4110 | +0.190 | 0.8495 |  |
| Kidney disease | +0.2914 | 1.3774 | ±2.7548 | +0.212 | 0.8324 |  |
| Circulatory disease | -0.3661 | 0.9047 | ±1.8095 | -0.405 | 0.6857 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0832** | 0.0351 | ±0.0702 | **+2.369** | **0.0178** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **576**, R² = **0.1941**, Adj R² = **0.1784**, F-statistic = **12.35** (p = **5.20e-21**), Residual SE = **7.885** on **564** df, AIC = **4025.4**, BIC = **4077.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.1591** | 2.6609 | ±5.3218 | **+25.615** | **1.04e-144** | *** |
| Education: graduate level (vs college) | -1.1233 | 0.7332 | ±1.4663 | -1.532 | 0.1255 |  |
| Education: high school or below (vs college) | -0.7961 | 1.2019 | ±2.4039 | -0.662 | 0.5078 |  |
| **Site: UCSD (vs UAB)** | **-2.5666** | 0.9309 | ±1.8618 | **-2.757** | **0.0058** | ** |
| **Site: UW (vs UAB)** | **-2.9213** | 0.7871 | ±1.5743 | **-3.711** | **2.06e-04** | *** |
| **Age (years)** | **-0.1994** | 0.0310 | ±0.0620 | **-6.438** | **1.21e-10** | *** |
| **BMI (kg/m2)** | **+0.2002** | 0.0484 | ±0.0969 | **+4.133** | **3.59e-05** | *** |
| Hypertension | +1.1434 | 0.7595 | ±1.5189 | +1.506 | 0.1322 |  |
| High cholesterol | +0.1231 | 0.7077 | ±1.4153 | +0.174 | 0.8619 |  |
| Kidney disease | +0.3380 | 1.3876 | ±2.7751 | +0.244 | 0.8075 |  |
| Circulatory disease | -0.3480 | 0.9058 | ±1.8115 | -0.384 | 0.7008 |  |
| **Avg. daily SD (mg/dL)** | **+0.0886** | 0.0419 | ±0.0839 | **+2.112** | **0.0346** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **576**, R² = **0.1933**, Adj R² = **0.1776**, F-statistic = **12.29** (p = **6.85e-21**), Residual SE = **7.889** on **564** df, AIC = **4026.0**, BIC = **4078.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1334** | 2.7400 | ±5.4800 | **+24.501** | **1.43e-132** | *** |
| Education: graduate level (vs college) | -1.1295 | 0.7331 | ±1.4663 | -1.541 | 0.1234 |  |
| Education: high school or below (vs college) | -0.6951 | 1.1981 | ±2.3962 | -0.580 | 0.5618 |  |
| **Site: UCSD (vs UAB)** | **-2.5384** | 0.9308 | ±1.8617 | **-2.727** | **0.0064** | ** |
| **Site: UW (vs UAB)** | **-2.8652** | 0.7913 | ±1.5825 | **-3.621** | **2.93e-04** | *** |
| **Age (years)** | **-0.2024** | 0.0313 | ±0.0625 | **-6.475** | **9.45e-11** | *** |
| **BMI (kg/m2)** | **+0.2030** | 0.0485 | ±0.0970 | **+4.186** | **2.84e-05** | *** |
| Hypertension | +1.2036 | 0.7566 | ±1.5133 | +1.591 | 0.1117 |  |
| High cholesterol | +0.2028 | 0.7060 | ±1.4120 | +0.287 | 0.7739 |  |
| Kidney disease | +0.3356 | 1.3977 | ±2.7955 | +0.240 | 0.8102 |  |
| Circulatory disease | -0.3475 | 0.9007 | ±1.8014 | -0.386 | 0.6996 |  |
| **CV (%)** | **+0.1473** | 0.0587 | ±0.1174 | **+2.509** | **0.0121** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **576**, R² = **0.1978**, Adj R² = **0.1821**, F-statistic = **12.64** (p = **1.58e-21**), Residual SE = **7.867** on **564** df, AIC = **4022.8**, BIC = **4075.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.8611** | 3.1179 | ±6.2358 | **+24.010** | **2.19e-127** | *** |
| Education: graduate level (vs college) | -1.1861 | 0.7308 | ±1.4617 | -1.623 | 0.1046 |  |
| Education: high school or below (vs college) | -0.7616 | 1.1883 | ±2.3767 | -0.641 | 0.5216 |  |
| **Site: UCSD (vs UAB)** | **-2.5947** | 0.9247 | ±1.8494 | **-2.806** | **0.0050** | ** |
| **Site: UW (vs UAB)** | **-2.9154** | 0.7868 | ±1.5735 | **-3.706** | **2.11e-04** | *** |
| **Age (years)** | **-0.2064** | 0.0311 | ±0.0621 | **-6.644** | **3.05e-11** | *** |
| **BMI (kg/m2)** | **+0.1995** | 0.0483 | ±0.0967 | **+4.127** | **3.68e-05** | *** |
| Hypertension | +1.1899 | 0.7555 | ±1.5111 | +1.575 | 0.1153 |  |
| High cholesterol | +0.1950 | 0.7037 | ±1.4074 | +0.277 | 0.7817 |  |
| Kidney disease | +0.4061 | 1.3781 | ±2.7561 | +0.295 | 0.7682 |  |
| Circulatory disease | -0.4050 | 0.8967 | ±1.7933 | -0.452 | 0.6515 |  |
| **Mean / SD ratio** | **-0.8225** | 0.2581 | ±0.5162 | **-3.187** | **0.0014** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **576**, R² = **0.1951**, Adj R² = **0.1795**, F-statistic = **12.43** (p = **3.75e-21**), Residual SE = **7.880** on **564** df, AIC = **4024.6**, BIC = **4076.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.3090** | 3.1174 | ±6.2347 | **+23.837** | **1.38e-125** | *** |
| Education: graduate level (vs college) | -1.1824 | 0.7303 | ±1.4607 | -1.619 | 0.1054 |  |
| Education: high school or below (vs college) | -0.7489 | 1.1921 | ±2.3843 | -0.628 | 0.5299 |  |
| **Site: UCSD (vs UAB)** | **-2.6556** | 0.9294 | ±1.8588 | **-2.857** | **0.0043** | ** |
| **Site: UW (vs UAB)** | **-2.9758** | 0.7889 | ±1.5779 | **-3.772** | **1.62e-04** | *** |
| **Age (years)** | **-0.2061** | 0.0314 | ±0.0627 | **-6.574** | **4.91e-11** | *** |
| **BMI (kg/m2)** | **+0.1983** | 0.0482 | ±0.0965 | **+4.111** | **3.94e-05** | *** |
| Hypertension | +1.2464 | 0.7531 | ±1.5063 | +1.655 | 0.0979 | . |
| High cholesterol | +0.1704 | 0.7054 | ±1.4108 | +0.242 | 0.8091 |  |
| Kidney disease | +0.5269 | 1.3811 | ±2.7623 | +0.381 | 0.7029 |  |
| Circulatory disease | -0.3789 | 0.8990 | ±1.7980 | -0.421 | 0.6734 |  |
| **Avg. daily mean/SD** | **-0.6060** | 0.2097 | ±0.4193 | **-2.891** | **0.0038** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **576**, R² = **0.1876**, Adj R² = **0.1717**, F-statistic = **11.84** (p = **4.40e-20**), Residual SE = **7.917** on **564** df, AIC = **4030.0**, BIC = **4082.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2750** | 2.9058 | ±5.8116 | **+23.152** | **1.38e-118** | *** |
| Education: graduate level (vs college) | -1.1873 | 0.7313 | ±1.4626 | -1.624 | 0.1045 |  |
| Education: high school or below (vs college) | -0.4532 | 1.2031 | ±2.4061 | -0.377 | 0.7064 |  |
| **Site: UCSD (vs UAB)** | **-2.5860** | 0.9367 | ±1.8735 | **-2.761** | **0.0058** | ** |
| **Site: UW (vs UAB)** | **-2.9279** | 0.7972 | ±1.5943 | **-3.673** | **2.40e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0308 | ±0.0616 | **-6.116** | **9.58e-10** | *** |
| **BMI (kg/m2)** | **+0.1966** | 0.0489 | ±0.0977 | **+4.023** | **5.74e-05** | *** |
| Hypertension | +1.2830 | 0.7528 | ±1.5056 | +1.704 | 0.0883 | . |
| High cholesterol | +0.2191 | 0.7072 | ±1.4144 | +0.310 | 0.7567 |  |
| Kidney disease | +0.9223 | 1.3787 | ±2.7574 | +0.669 | 0.5035 |  |
| Circulatory disease | -0.4125 | 0.9076 | ±1.8153 | -0.454 | 0.6495 |  |
| MAG (mg/dL/h) | +0.0540 | 0.0362 | ±0.0724 | +1.492 | 0.1357 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **576**, R² = **0.1934**, Adj R² = **0.1777**, F-statistic = **12.30** (p = **6.53e-21**), Residual SE = **7.889** on **564** df, AIC = **4025.9**, BIC = **4078.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.4442** | 2.7140 | ±5.4279 | **+24.851** | **2.53e-136** | *** |
| Education: graduate level (vs college) | -1.1227 | 0.7327 | ±1.4654 | -1.532 | 0.1255 |  |
| Education: high school or below (vs college) | -0.7665 | 1.2017 | ±2.4035 | -0.638 | 0.5236 |  |
| **Site: UCSD (vs UAB)** | **-2.5891** | 0.9302 | ±1.8603 | **-2.783** | **0.0054** | ** |
| **Site: UW (vs UAB)** | **-2.9364** | 0.7880 | ±1.5759 | **-3.727** | **1.94e-04** | *** |
| **Age (years)** | **-0.1981** | 0.0310 | ±0.0621 | **-6.383** | **1.74e-10** | *** |
| **BMI (kg/m2)** | **+0.2042** | 0.0485 | ±0.0969 | **+4.213** | **2.52e-05** | *** |
| Hypertension | +1.1837 | 0.7574 | ±1.5148 | +1.563 | 0.1181 |  |
| High cholesterol | +0.1328 | 0.7072 | ±1.4143 | +0.188 | 0.8510 |  |
| Kidney disease | +0.4106 | 1.3834 | ±2.7668 | +0.297 | 0.7666 |  |
| Circulatory disease | -0.3945 | 0.9053 | ±1.8105 | -0.436 | 0.6630 |  |
| **Avg. daily range (mg/dL)** | **+0.0227** | 0.0099 | ±0.0198 | **+2.292** | **0.0219** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **576**, R² = **0.1961**, Adj R² = **0.1805**, F-statistic = **12.51** (p = **2.72e-21**), Residual SE = **7.875** on **564** df, AIC = **4023.9**, BIC = **4076.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.5233** | 2.6400 | ±5.2800 | **+25.956** | **1.57e-148** | *** |
| Education: graduate level (vs college) | -1.1284 | 0.7338 | ±1.4677 | -1.538 | 0.1241 |  |
| Education: high school or below (vs college) | -0.4431 | 1.1860 | ±2.3719 | -0.374 | 0.7087 |  |
| **Site: UCSD (vs UAB)** | **-2.4804** | 0.9289 | ±1.8577 | **-2.670** | **0.0076** | ** |
| **Site: UW (vs UAB)** | **-2.9077** | 0.7901 | ±1.5803 | **-3.680** | **2.33e-04** | *** |
| **Age (years)** | **-0.1921** | 0.0305 | ±0.0610 | **-6.297** | **3.04e-10** | *** |
| **BMI (kg/m2)** | **+0.1976** | 0.0486 | ±0.0971 | **+4.070** | **4.70e-05** | *** |
| Hypertension | +1.1183 | 0.7602 | ±1.5204 | +1.471 | 0.1413 |  |
| High cholesterol | +0.1668 | 0.7026 | ±1.4052 | +0.237 | 0.8123 |  |
| Kidney disease | +0.5849 | 1.3334 | ±2.6667 | +0.439 | 0.6609 |  |
| Circulatory disease | -0.4923 | 0.9029 | ±1.8057 | -0.545 | 0.5856 |  |
| **SD of daily means (mg/dL)** | **+0.1402** | 0.0473 | ±0.0947 | **+2.962** | **0.0031** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **576**, R² = **0.1967**, Adj R² = **0.1810**, F-statistic = **12.55** (p = **2.26e-21**), Residual SE = **7.873** on **564** df, AIC = **4023.5**, BIC = **4075.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.7989** | 3.7866 | ±7.5732 | **+20.282** | **1.86e-91** | *** |
| Education: graduate level (vs college) | -1.0870 | 0.7407 | ±1.4813 | -1.468 | 0.1422 |  |
| Education: high school or below (vs college) | -0.6050 | 1.1677 | ±2.3354 | -0.518 | 0.6044 |  |
| **Site: UCSD (vs UAB)** | **-2.4750** | 0.9277 | ±1.8554 | **-2.668** | **0.0076** | ** |
| **Site: UW (vs UAB)** | **-2.8515** | 0.7886 | ±1.5773 | **-3.616** | **3.00e-04** | *** |
| **Age (years)** | **-0.1928** | 0.0303 | ±0.0607 | **-6.354** | **2.10e-10** | *** |
| **BMI (kg/m2)** | **+0.1975** | 0.0482 | ±0.0963 | **+4.102** | **4.09e-05** | *** |
| Hypertension | +1.1733 | 0.7597 | ±1.5194 | +1.544 | 0.1225 |  |
| High cholesterol | +0.0898 | 0.7034 | ±1.4068 | +0.128 | 0.8984 |  |
| Kidney disease | +0.4461 | 1.3357 | ±2.6713 | +0.334 | 0.7384 |  |
| Circulatory disease | -0.4482 | 0.9083 | ±1.8166 | -0.493 | 0.6217 |  |
| **Time in range 70-180, pooled (%)** | **-0.0763** | 0.0304 | ±0.0607 | **-2.512** | **0.0120** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **576**, R² = **0.1965**, Adj R² = **0.1809**, F-statistic = **12.54** (p = **2.37e-21**), Residual SE = **7.873** on **564** df, AIC = **4023.6**, BIC = **4075.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.7682** | 3.7228 | ±7.4457 | **+20.621** | **1.78e-94** | *** |
| Education: graduate level (vs college) | -1.0841 | 0.7425 | ±1.4850 | -1.460 | 0.1443 |  |
| Education: high school or below (vs college) | -0.6160 | 1.1668 | ±2.3337 | -0.528 | 0.5976 |  |
| **Site: UCSD (vs UAB)** | **-2.4755** | 0.9283 | ±1.8565 | **-2.667** | **0.0077** | ** |
| **Site: UW (vs UAB)** | **-2.8493** | 0.7888 | ±1.5777 | **-3.612** | **3.04e-04** | *** |
| **Age (years)** | **-0.1931** | 0.0304 | ±0.0607 | **-6.360** | **2.02e-10** | *** |
| **BMI (kg/m2)** | **+0.1977** | 0.0482 | ±0.0965 | **+4.098** | **4.17e-05** | *** |
| Hypertension | +1.1794 | 0.7605 | ±1.5209 | +1.551 | 0.1209 |  |
| High cholesterol | +0.0831 | 0.7025 | ±1.4050 | +0.118 | 0.9058 |  |
| Kidney disease | +0.4438 | 1.3349 | ±2.6698 | +0.332 | 0.7395 |  |
| Circulatory disease | -0.4492 | 0.9096 | ±1.8193 | -0.494 | 0.6214 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0755** | 0.0295 | ±0.0589 | **-2.562** | **0.0104** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **576**, R² = **0.1845**, Adj R² = **0.1686**, F-statistic = **11.60** (p = **1.20e-19**), Residual SE = **7.932** on **564** df, AIC = **4032.2**, BIC = **4084.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3399** | 2.6444 | ±5.2888 | **+26.221** | **1.52e-151** | *** |
| Education: graduate level (vs college) | -1.2076 | 0.7316 | ±1.4631 | -1.651 | 0.0988 | . |
| Education: high school or below (vs college) | -0.2681 | 1.2079 | ±2.4158 | -0.222 | 0.8243 |  |
| **Site: UCSD (vs UAB)** | **-2.4687** | 0.9500 | ±1.8999 | **-2.599** | **0.0094** | ** |
| **Site: UW (vs UAB)** | **-3.0302** | 0.8004 | ±1.6007 | **-3.786** | **1.53e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0309 | ±0.0617 | **-6.103** | **1.04e-09** | *** |
| **BMI (kg/m2)** | **+0.1989** | 0.0489 | ±0.0978 | **+4.065** | **4.80e-05** | *** |
| Hypertension | +1.3513 | 0.7550 | ±1.5100 | +1.790 | 0.0735 | . |
| High cholesterol | +0.2226 | 0.7070 | ±1.4139 | +0.315 | 0.7528 |  |
| Kidney disease | +0.9891 | 1.3726 | ±2.7451 | +0.721 | 0.4712 |  |
| Circulatory disease | -0.4331 | 0.9063 | ±1.8126 | -0.478 | 0.6327 |  |
| Time < 54 (%) | +0.1505 | 0.2742 | ±0.5484 | +0.549 | 0.5830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **576**, R² = **0.1843**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4425** | 2.6312 | ±5.2625 | **+26.392** | **1.71e-153** | *** |
| Education: graduate level (vs college) | -1.2126 | 0.7319 | ±1.4637 | -1.657 | 0.0975 | . |
| Education: high school or below (vs college) | -0.2864 | 1.2082 | ±2.4163 | -0.237 | 0.8126 |  |
| **Site: UCSD (vs UAB)** | **-2.5116** | 0.9496 | ±1.8992 | **-2.645** | **0.0082** | ** |
| **Site: UW (vs UAB)** | **-3.0648** | 0.8026 | ±1.6052 | **-3.819** | **1.34e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0310 | ±0.0620 | **-6.072** | **1.26e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0490 | ±0.0980 | **+4.053** | **5.06e-05** | *** |
| Hypertension | +1.3408 | 0.7560 | ±1.5120 | +1.774 | 0.0761 | . |
| High cholesterol | +0.2063 | 0.7081 | ±1.4161 | +0.291 | 0.7708 |  |
| Kidney disease | +0.9962 | 1.3729 | ±2.7458 | +0.726 | 0.4681 |  |
| Circulatory disease | -0.4313 | 0.9090 | ±1.8181 | -0.474 | 0.6352 |  |
| Avg. daily time < 54 (%) | +0.0306 | 0.4285 | ±0.8569 | +0.071 | 0.9431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **576**, R² = **0.1843**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4402** | 2.6457 | ±5.2914 | **+26.246** | **7.89e-152** | *** |
| Education: graduate level (vs college) | -1.2127 | 0.7353 | ±1.4707 | -1.649 | 0.0991 | . |
| Education: high school or below (vs college) | -0.2904 | 1.2074 | ±2.4149 | -0.240 | 0.8099 |  |
| **Site: UCSD (vs UAB)** | **-2.5153** | 0.9486 | ±1.8973 | **-2.651** | **0.0080** | ** |
| **Site: UW (vs UAB)** | **-3.0687** | 0.8009 | ±1.6019 | **-3.831** | **1.27e-04** | *** |
| **Age (years)** | **-0.1883** | 0.0309 | ±0.0618 | **-6.098** | **1.07e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0978 | **+4.058** | **4.96e-05** | *** |
| Hypertension | +1.3406 | 0.7547 | ±1.5094 | +1.776 | 0.0757 | . |
| High cholesterol | +0.2039 | 0.7062 | ±1.4125 | +0.289 | 0.7728 |  |
| Kidney disease | +0.9970 | 1.3723 | ±2.7446 | +0.727 | 0.4675 |  |
| Circulatory disease | -0.4294 | 0.9097 | ±1.8194 | -0.472 | 0.6369 |  |
| Time 54-69, pooled (%) | +0.0074 | 0.1282 | ±0.2564 | +0.058 | 0.9538 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **576**, R² = **0.1842**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4558** | 2.6366 | ±5.2731 | **+26.343** | **6.14e-153** | *** |
| Education: graduate level (vs college) | -1.2160 | 0.7362 | ±1.4725 | -1.652 | 0.0986 | . |
| Education: high school or below (vs college) | -0.2904 | 1.2078 | ±2.4156 | -0.240 | 0.8100 |  |
| **Site: UCSD (vs UAB)** | **-2.5200** | 0.9472 | ±1.8944 | **-2.660** | **0.0078** | ** |
| **Site: UW (vs UAB)** | **-3.0743** | 0.8006 | ±1.6012 | **-3.840** | **1.23e-04** | *** |
| **Age (years)** | **-0.1882** | 0.0309 | ±0.0619 | **-6.082** | **1.19e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0979 | **+4.056** | **4.99e-05** | *** |
| Hypertension | +1.3381 | 0.7550 | ±1.5099 | +1.772 | 0.0763 | . |
| High cholesterol | +0.2022 | 0.7064 | ±1.4127 | +0.286 | 0.7747 |  |
| Kidney disease | +0.9989 | 1.3719 | ±2.7439 | +0.728 | 0.4665 |  |
| Circulatory disease | -0.4308 | 0.9101 | ±1.8202 | -0.473 | 0.6359 |  |
| Avg. daily time 54-69 (%) | -0.0020 | 0.1279 | ±0.2558 | -0.015 | 0.9877 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **576**, R² = **0.1843**, Adj R² = **0.1684**, F-statistic = **11.58** (p = **1.27e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4043** | 2.6506 | ±5.3012 | **+26.185** | **3.98e-151** | *** |
| Education: graduate level (vs college) | -1.2076 | 0.7343 | ±1.4686 | -1.644 | 0.1001 |  |
| Education: high school or below (vs college) | -0.2874 | 1.2068 | ±2.4136 | -0.238 | 0.8118 |  |
| **Site: UCSD (vs UAB)** | **-2.5025** | 0.9516 | ±1.9032 | **-2.630** | **0.0085** | ** |
| **Site: UW (vs UAB)** | **-3.0562** | 0.8029 | ±1.6058 | **-3.806** | **1.41e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0309 | ±0.0618 | **-6.102** | **1.05e-09** | *** |
| **BMI (kg/m2)** | **+0.1986** | 0.0489 | ±0.0978 | **+4.060** | **4.91e-05** | *** |
| Hypertension | +1.3455 | 0.7550 | ±1.5100 | +1.782 | 0.0747 | . |
| High cholesterol | +0.2088 | 0.7060 | ±1.4119 | +0.296 | 0.7674 |  |
| Kidney disease | +0.9934 | 1.3731 | ±2.7461 | +0.723 | 0.4694 |  |
| Circulatory disease | -0.4278 | 0.9091 | ±1.8181 | -0.471 | 0.6379 |  |
| Time < 70 (%) | +0.0195 | 0.1010 | ±0.2019 | +0.193 | 0.8467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **576**, R² = **0.1842**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4519** | 2.6367 | ±5.2735 | **+26.340** | **6.68e-153** | *** |
| Education: graduate level (vs college) | -1.2149 | 0.7356 | ±1.4712 | -1.652 | 0.0986 | . |
| Education: high school or below (vs college) | -0.2903 | 1.2072 | ±2.4144 | -0.241 | 0.8099 |  |
| **Site: UCSD (vs UAB)** | **-2.5186** | 0.9490 | ±1.8979 | **-2.654** | **0.0080** | ** |
| **Site: UW (vs UAB)** | **-3.0723** | 0.8024 | ±1.6048 | **-3.829** | **1.29e-04** | *** |
| **Age (years)** | **-0.1882** | 0.0310 | ±0.0620 | **-6.076** | **1.23e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0979 | **+4.055** | **5.01e-05** | *** |
| Hypertension | +1.3389 | 0.7554 | ±1.5108 | +1.772 | 0.0763 | . |
| High cholesterol | +0.2028 | 0.7061 | ±1.4122 | +0.287 | 0.7740 |  |
| Kidney disease | +0.9983 | 1.3725 | ±2.7450 | +0.727 | 0.4670 |  |
| Circulatory disease | -0.4304 | 0.9101 | ±1.8203 | -0.473 | 0.6363 |  |
| Avg. daily time < 70 (%) | +0.0008 | 0.1081 | ±0.2162 | +0.007 | 0.9941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **576**, R² = **0.1866**, Adj R² = **0.1707**, F-statistic = **11.76** (p = **6.12e-20**), Residual SE = **7.922** on **564** df, AIC = **4030.7**, BIC = **4083.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4069** | 7.9998 | ±15.9997 | **+9.551** | **1.28e-21** | *** |
| Education: graduate level (vs college) | -1.1687 | 0.7360 | ±1.4720 | -1.588 | 0.1123 |  |
| Education: high school or below (vs college) | -0.4204 | 1.1989 | ±2.3978 | -0.351 | 0.7259 |  |
| **Site: UCSD (vs UAB)** | **-2.4896** | 0.9369 | ±1.8739 | **-2.657** | **0.0079** | ** |
| **Site: UW (vs UAB)** | **-2.9786** | 0.7959 | ±1.5918 | **-3.743** | **1.82e-04** | *** |
| **Age (years)** | **-0.1880** | 0.0307 | ±0.0614 | **-6.126** | **9.03e-10** | *** |
| **BMI (kg/m2)** | **+0.1992** | 0.0489 | ±0.0978 | **+4.074** | **4.62e-05** | *** |
| Hypertension | +1.2858 | 0.7575 | ±1.5149 | +1.698 | 0.0896 | . |
| High cholesterol | +0.2239 | 0.7088 | ±1.4176 | +0.316 | 0.7521 |  |
| Kidney disease | +0.8767 | 1.3632 | ±2.7264 | +0.643 | 0.5202 |  |
| Circulatory disease | -0.4585 | 0.9124 | ±1.8248 | -0.503 | 0.6153 |  |
| Time 54-250, pooled (%) | -0.0713 | 0.0778 | ±0.1557 | -0.916 | 0.3595 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **576**, R² = **0.1880**, Adj R² = **0.1722**, F-statistic = **11.87** (p = **3.81e-20**), Residual SE = **7.915** on **564** df, AIC = **4029.7**, BIC = **4082.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.3248** | 7.8121 | ±15.6243 | **+10.154** | **3.18e-24** | *** |
| Education: graduate level (vs college) | -1.1484 | 0.7369 | ±1.4737 | -1.558 | 0.1191 |  |
| Education: high school or below (vs college) | -0.4813 | 1.1932 | ±2.3864 | -0.403 | 0.6867 |  |
| **Site: UCSD (vs UAB)** | **-2.4947** | 0.9362 | ±1.8724 | **-2.665** | **0.0077** | ** |
| **Site: UW (vs UAB)** | **-2.9570** | 0.7949 | ±1.5898 | **-3.720** | **1.99e-04** | *** |
| **Age (years)** | **-0.1885** | 0.0306 | ±0.0613 | **-6.154** | **7.56e-10** | *** |
| **BMI (kg/m2)** | **+0.1998** | 0.0489 | ±0.0977 | **+4.089** | **4.33e-05** | *** |
| Hypertension | +1.2697 | 0.7571 | ±1.5142 | +1.677 | 0.0935 | . |
| High cholesterol | +0.2257 | 0.7079 | ±1.4158 | +0.319 | 0.7499 |  |
| Kidney disease | +0.8165 | 1.3570 | ±2.7139 | +0.602 | 0.5474 |  |
| Circulatory disease | -0.4743 | 0.9131 | ±1.8262 | -0.519 | 0.6035 |  |
| Avg. daily time 54-250 (%) | -0.1006 | 0.0757 | ±0.1514 | -1.329 | 0.1838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **576**, R² = **0.2011**, Adj R² = **0.1855**, F-statistic = **12.91** (p = **5.25e-22**), Residual SE = **7.851** on **564** df, AIC = **4020.4**, BIC = **4072.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.5204** | 2.5856 | ±5.1712 | **+26.888** | **3.07e-159** | *** |
| Education: graduate level (vs college) | -1.1265 | 0.7378 | ±1.4756 | -1.527 | 0.1268 |  |
| Education: high school or below (vs college) | -0.5897 | 1.1681 | ±2.3361 | -0.505 | 0.6136 |  |
| **Site: UCSD (vs UAB)** | **-2.5646** | 0.9254 | ±1.8508 | **-2.771** | **0.0056** | ** |
| **Site: UW (vs UAB)** | **-2.9432** | 0.7839 | ±1.5679 | **-3.754** | **1.74e-04** | *** |
| **Age (years)** | **-0.1953** | 0.0303 | ±0.0606 | **-6.451** | **1.11e-10** | *** |
| **BMI (kg/m2)** | **+0.1954** | 0.0481 | ±0.0961 | **+4.066** | **4.78e-05** | *** |
| Hypertension | +1.1182 | 0.7637 | ±1.5273 | +1.464 | 0.1431 |  |
| High cholesterol | -0.0524 | 0.6946 | ±1.3891 | -0.075 | 0.9398 |  |
| Kidney disease | +0.3071 | 1.3218 | ±2.6436 | +0.232 | 0.8163 |  |
| Circulatory disease | -0.4301 | 0.9087 | ±1.8175 | -0.473 | 0.6360 |  |
| **Time 181-250, pooled (%)** | **+0.1297** | 0.0433 | ±0.0866 | **+2.994** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **576**, R² = **0.1991**, Adj R² = **0.1834**, F-statistic = **12.74** (p = **1.04e-21**), Residual SE = **7.861** on **564** df, AIC = **4021.8**, BIC = **4074.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4587** | 2.5909 | ±5.1818 | **+26.809** | **2.57e-158** | *** |
| Education: graduate level (vs college) | -1.1337 | 0.7396 | ±1.4791 | -1.533 | 0.1253 |  |
| Education: high school or below (vs college) | -0.5744 | 1.1693 | ±2.3385 | -0.491 | 0.6233 |  |
| **Site: UCSD (vs UAB)** | **-2.5343** | 0.9273 | ±1.8547 | **-2.733** | **0.0063** | ** |
| **Site: UW (vs UAB)** | **-2.9343** | 0.7852 | ±1.5704 | **-3.737** | **1.86e-04** | *** |
| **Age (years)** | **-0.1939** | 0.0303 | ±0.0606 | **-6.397** | **1.59e-10** | *** |
| **BMI (kg/m2)** | **+0.1956** | 0.0482 | ±0.0964 | **+4.059** | **4.92e-05** | *** |
| Hypertension | +1.1394 | 0.7653 | ±1.5307 | +1.489 | 0.1366 |  |
| High cholesterol | -0.0324 | 0.6956 | ±1.3912 | -0.047 | 0.9629 |  |
| Kidney disease | +0.3688 | 1.3266 | ±2.6532 | +0.278 | 0.7810 |  |
| Circulatory disease | -0.4267 | 0.9117 | ±1.8234 | -0.468 | 0.6398 |  |
| **Avg. daily time 181-250 (%)** | **+0.1180** | 0.0432 | ±0.0864 | **+2.732** | **0.0063** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **576**, R² = **0.1963**, Adj R² = **0.1807**, F-statistic = **12.53** (p = **2.53e-21**), Residual SE = **7.874** on **564** df, AIC = **4023.8**, BIC = **4076.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3603** | 2.5921 | ±5.1843 | **+26.758** | **1.00e-157** | *** |
| Education: graduate level (vs college) | -1.1186 | 0.7384 | ±1.4767 | -1.515 | 0.1298 |  |
| Education: high school or below (vs college) | -0.6120 | 1.1707 | ±2.3415 | -0.523 | 0.6012 |  |
| **Site: UCSD (vs UAB)** | **-2.5396** | 0.9288 | ±1.8577 | **-2.734** | **0.0063** | ** |
| **Site: UW (vs UAB)** | **-2.9197** | 0.7868 | ±1.5736 | **-3.711** | **2.07e-04** | *** |
| **Age (years)** | **-0.1920** | 0.0303 | ±0.0606 | **-6.338** | **2.33e-10** | *** |
| **BMI (kg/m2)** | **+0.1972** | 0.0483 | ±0.0966 | **+4.083** | **4.45e-05** | *** |
| Hypertension | +1.1489 | 0.7627 | ±1.5254 | +1.506 | 0.1320 |  |
| High cholesterol | +0.0673 | 0.7021 | ±1.4042 | +0.096 | 0.9237 |  |
| Kidney disease | +0.4740 | 1.3308 | ±2.6617 | +0.356 | 0.7217 |  |
| Circulatory disease | -0.4585 | 0.9122 | ±1.8244 | -0.503 | 0.6152 |  |
| **Time > 180 (%)** | **+0.0752** | 0.0301 | ±0.0602 | **+2.499** | **0.0125** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **576**, R² = **0.1967**, Adj R² = **0.1810**, F-statistic = **12.55** (p = **2.27e-21**), Residual SE = **7.873** on **564** df, AIC = **4023.5**, BIC = **4075.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3420** | 2.5964 | ±5.1929 | **+26.707** | **3.94e-157** | *** |
| Education: graduate level (vs college) | -1.1184 | 0.7398 | ±1.4796 | -1.512 | 0.1306 |  |
| Education: high school or below (vs college) | -0.6291 | 1.1688 | ±2.3377 | -0.538 | 0.5905 |  |
| **Site: UCSD (vs UAB)** | **-2.5292** | 0.9290 | ±1.8579 | **-2.723** | **0.0065** | ** |
| **Site: UW (vs UAB)** | **-2.9158** | 0.7871 | ±1.5742 | **-3.704** | **2.12e-04** | *** |
| **Age (years)** | **-0.1918** | 0.0303 | ±0.0606 | **-6.331** | **2.44e-10** | *** |
| **BMI (kg/m2)** | **+0.1975** | 0.0484 | ±0.0967 | **+4.083** | **4.45e-05** | *** |
| Hypertension | +1.1519 | 0.7638 | ±1.5276 | +1.508 | 0.1315 |  |
| High cholesterol | +0.0589 | 0.7004 | ±1.4008 | +0.084 | 0.9330 |  |
| Kidney disease | +0.4590 | 1.3287 | ±2.6573 | +0.345 | 0.7298 |  |
| Circulatory disease | -0.4594 | 0.9134 | ±1.8268 | -0.503 | 0.6150 |  |
| **Avg. daily time > 180 (%)** | **+0.0763** | 0.0292 | ±0.0583 | **+2.618** | **0.0089** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **576**, R² = **0.1901**, Adj R² = **0.1743**, F-statistic = **12.03** (p = **1.95e-20**), Residual SE = **7.905** on **564** df, AIC = **4028.2**, BIC = **4080.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4150** | 2.6092 | ±5.2184 | **+26.604** | **6.10e-156** | *** |
| Education: graduate level (vs college) | -1.1407 | 0.7396 | ±1.4793 | -1.542 | 0.1230 |  |
| Education: high school or below (vs college) | -0.4368 | 1.1767 | ±2.3533 | -0.371 | 0.7105 |  |
| **Site: UCSD (vs UAB)** | **-2.5145** | 0.9341 | ±1.8681 | **-2.692** | **0.0071** | ** |
| **Site: UW (vs UAB)** | **-2.9856** | 0.7915 | ±1.5831 | **-3.772** | **1.62e-04** | *** |
| **Age (years)** | **-0.1885** | 0.0306 | ±0.0612 | **-6.159** | **7.33e-10** | *** |
| **BMI (kg/m2)** | **+0.1950** | 0.0484 | ±0.0968 | **+4.030** | **5.59e-05** | *** |
| Hypertension | +1.1924 | 0.7673 | ±1.5345 | +1.554 | 0.1201 |  |
| High cholesterol | +0.1202 | 0.7044 | ±1.4087 | +0.171 | 0.8645 |  |
| Kidney disease | +0.8247 | 1.3329 | ±2.6658 | +0.619 | 0.5361 |  |
| Circulatory disease | -0.4719 | 0.9125 | ±1.8250 | -0.517 | 0.6050 |  |
| Nocturnal time > 180 (%) | +0.0538 | 0.0288 | ±0.0575 | +1.870 | 0.0615 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **576**, R² = **0.1921**, Adj R² = **0.1764**, F-statistic = **12.19** (p = **1.01e-20**), Residual SE = **7.895** on **564** df, AIC = **4026.8**, BIC = **4079.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3452** | 2.5953 | ±5.1905 | **+26.720** | **2.76e-157** | *** |
| Education: graduate level (vs college) | -1.1141 | 0.7329 | ±1.4658 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | -0.4769 | 1.1946 | ±2.3892 | -0.399 | 0.6897 |  |
| **Site: UCSD (vs UAB)** | **-2.6246** | 0.9313 | ±1.8626 | **-2.818** | **0.0048** | ** |
| **Site: UW (vs UAB)** | **-3.0201** | 0.7884 | ±1.5768 | **-3.831** | **1.28e-04** | *** |
| **Age (years)** | **-0.1957** | 0.0309 | ±0.0618 | **-6.337** | **2.35e-10** | *** |
| **BMI (kg/m2)** | **+0.2044** | 0.0486 | ±0.0973 | **+4.203** | **2.64e-05** | *** |
| Hypertension | +1.1572 | 0.7595 | ±1.5190 | +1.524 | 0.1276 |  |
| High cholesterol | +0.1013 | 0.7051 | ±1.4102 | +0.144 | 0.8857 |  |
| Kidney disease | +0.5865 | 1.3614 | ±2.7228 | +0.431 | 0.6666 |  |
| Circulatory disease | -0.3846 | 0.9077 | ±1.8153 | -0.424 | 0.6718 |  |
| **Any reading > 250 during wear (0/1)** | **+1.7840** | 0.7798 | ±1.5595 | **+2.288** | **0.0221** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **576**, R² = **0.1864**, Adj R² = **0.1705**, F-statistic = **11.75** (p = **6.44e-20**), Residual SE = **7.923** on **564** df, AIC = **4030.9**, BIC = **4083.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3307** | 2.6201 | ±5.2402 | **+26.461** | **2.72e-154** | *** |
| Education: graduate level (vs college) | -1.1732 | 0.7358 | ±1.4717 | -1.594 | 0.1108 |  |
| Education: high school or below (vs college) | -0.4280 | 1.2012 | ±2.4024 | -0.356 | 0.7216 |  |
| **Site: UCSD (vs UAB)** | **-2.5137** | 0.9383 | ±1.8765 | **-2.679** | **0.0074** | ** |
| **Site: UW (vs UAB)** | **-3.0004** | 0.7942 | ±1.5885 | **-3.778** | **1.58e-04** | *** |
| **Age (years)** | **-0.1879** | 0.0307 | ±0.0614 | **-6.124** | **9.10e-10** | *** |
| **BMI (kg/m2)** | **+0.1990** | 0.0489 | ±0.0978 | **+4.070** | **4.70e-05** | *** |
| Hypertension | +1.2810 | 0.7584 | ±1.5169 | +1.689 | 0.0912 | . |
| High cholesterol | +0.2142 | 0.7089 | ±1.4179 | +0.302 | 0.7626 |  |
| Kidney disease | +0.8836 | 1.3616 | ±2.7231 | +0.649 | 0.5164 |  |
| Circulatory disease | -0.4567 | 0.9135 | ±1.8269 | -0.500 | 0.6171 |  |
| Time > 250 (%) | +0.0698 | 0.0771 | ±0.1542 | +0.906 | 0.3651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **576**, R² = **0.1881**, Adj R² = **0.1723**, F-statistic = **11.88** (p = **3.70e-20**), Residual SE = **7.915** on **564** df, AIC = **4029.6**, BIC = **4081.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.2972** | 2.6195 | ±5.2389 | **+26.455** | **3.22e-154** | *** |
| Education: graduate level (vs college) | -1.1553 | 0.7364 | ±1.4727 | -1.569 | 0.1167 |  |
| Education: high school or below (vs college) | -0.5010 | 1.1961 | ±2.3921 | -0.419 | 0.6753 |  |
| **Site: UCSD (vs UAB)** | **-2.5194** | 0.9375 | ±1.8750 | **-2.687** | **0.0072** | ** |
| **Site: UW (vs UAB)** | **-2.9813** | 0.7936 | ±1.5871 | **-3.757** | **1.72e-04** | *** |
| **Age (years)** | **-0.1881** | 0.0306 | ±0.0612 | **-6.142** | **8.15e-10** | *** |
| **BMI (kg/m2)** | **+0.1997** | 0.0489 | ±0.0977 | **+4.087** | **4.37e-05** | *** |
| Hypertension | +1.2599 | 0.7580 | ±1.5161 | +1.662 | 0.0965 | . |
| High cholesterol | +0.2137 | 0.7078 | ±1.4157 | +0.302 | 0.7627 |  |
| Kidney disease | +0.8187 | 1.3548 | ±2.7095 | +0.604 | 0.5456 |  |
| Circulatory disease | -0.4731 | 0.9146 | ±1.8293 | -0.517 | 0.6050 |  |
| Avg. daily time > 250 (%) | +0.1037 | 0.0766 | ±0.1531 | +1.354 | 0.1756 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 588; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **588**, R² = **0.0409**, Adj R² = **0.0243**, F-statistic = **2.46** (p = **0.0069**), Residual SE = **65.535** on **577** df, AIC = **6598.3**, BIC = **6646.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.6830** | 22.6798 | ±45.3596 | **+17.138** | **7.75e-66** | *** |
| Education: graduate level (vs college) | +5.9032 | 6.0751 | ±12.1502 | +0.972 | 0.3312 |  |
| **Education: high school or below (vs college)** | **-24.7347** | 10.6008 | ±21.2017 | **-2.333** | **0.0196** | * |
| Site: UCSD (vs UAB) | -1.1315 | 7.8398 | ±15.6797 | -0.144 | 0.8852 |  |
| Site: UW (vs UAB) | -1.1662 | 6.4178 | ±12.8355 | -0.182 | 0.8558 |  |
| Age (years) | -0.0183 | 0.2712 | ±0.5423 | -0.067 | 0.9462 |  |
| BMI (kg/m2) | -0.5914 | 0.4359 | ±0.8718 | -1.357 | 0.1749 |  |
| **Hypertension** | **-13.6400** | 6.0897 | ±12.1794 | **-2.240** | **0.0251** | * |
| High cholesterol | +5.8658 | 5.5923 | ±11.1845 | +1.049 | 0.2942 |  |
| Kidney disease | -2.0692 | 11.6137 | ±23.2275 | -0.178 | 0.8586 |  |
| Circulatory disease | +4.1510 | 7.9280 | ±15.8559 | +0.524 | 0.6006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **588**, R² = **0.0554**, Adj R² = **0.0373**, F-statistic = **3.07** (p = **5.15e-04**), Residual SE = **65.095** on **576** df, AIC = **6591.3**, BIC = **6643.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+437.2358** | 27.5039 | ±55.0078 | **+15.897** | **6.62e-57** | *** |
| Education: graduate level (vs college) | +4.5624 | 6.0466 | ±12.0932 | +0.755 | 0.4505 |  |
| **Education: high school or below (vs college)** | **-21.3122** | 10.4972 | ±20.9944 | **-2.030** | **0.0423** | * |
| Site: UCSD (vs UAB) | -0.5373 | 7.7701 | ±15.5402 | -0.069 | 0.9449 |  |
| Site: UW (vs UAB) | -2.5681 | 6.4205 | ±12.8409 | -0.400 | 0.6892 |  |
| Age (years) | +0.0818 | 0.2688 | ±0.5375 | +0.304 | 0.7608 |  |
| BMI (kg/m2) | -0.4908 | 0.4366 | ±0.8732 | -1.124 | 0.2609 |  |
| Hypertension | -11.9127 | 6.0930 | ±12.1861 | -1.955 | 0.0506 | . |
| High cholesterol | +7.0892 | 5.5977 | ±11.1954 | +1.266 | 0.2054 |  |
| Kidney disease | -1.1531 | 11.5758 | ±23.1517 | -0.100 | 0.9207 |  |
| Circulatory disease | +3.4644 | 7.8622 | ±15.7243 | +0.441 | 0.6595 |  |
| **HbA1c (%)** | **-9.8950** | 3.1075 | ±6.2151 | **-3.184** | **0.0015** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.65** (p = **0.0026**), Residual SE = **65.345** on **576** df, AIC = **6595.8**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+414.2155** | 25.9640 | ±51.9279 | **+15.953** | **2.69e-57** | *** |
| Education: graduate level (vs college) | +5.7793 | 6.0928 | ±12.1856 | +0.949 | 0.3428 |  |
| **Education: high school or below (vs college)** | **-22.6335** | 10.6004 | ±21.2009 | **-2.135** | **0.0327** | * |
| Site: UCSD (vs UAB) | -0.9322 | 7.7726 | ±15.5452 | -0.120 | 0.9045 |  |
| Site: UW (vs UAB) | -1.4791 | 6.4314 | ±12.8628 | -0.230 | 0.8181 |  |
| Age (years) | -0.0024 | 0.2698 | ±0.5397 | -0.009 | 0.9930 |  |
| BMI (kg/m2) | -0.5562 | 0.4372 | ±0.8743 | -1.272 | 0.2033 |  |
| Hypertension | -12.0347 | 6.1913 | ±12.3825 | -1.944 | 0.0519 | . |
| High cholesterol | +6.7443 | 5.5782 | ±11.1563 | +1.209 | 0.2266 |  |
| Kidney disease | +0.0674 | 11.8000 | ±23.6001 | +0.006 | 0.9954 |  |
| Circulatory disease | +4.2717 | 7.8882 | ±15.7764 | +0.542 | 0.5881 |  |
| **Mean glucose (mg/dL)** | **-0.2384** | 0.1106 | ±0.2212 | **-2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.65** (p = **0.0026**), Residual SE = **65.345** on **576** df, AIC = **6595.8**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+447.2102** | 35.9493 | ±71.8985 | **+12.440** | **1.58e-35** | *** |
| Education: graduate level (vs college) | +5.7793 | 6.0928 | ±12.1856 | +0.949 | 0.3428 |  |
| **Education: high school or below (vs college)** | **-22.6335** | 10.6004 | ±21.2009 | **-2.135** | **0.0327** | * |
| Site: UCSD (vs UAB) | -0.9322 | 7.7726 | ±15.5452 | -0.120 | 0.9045 |  |
| Site: UW (vs UAB) | -1.4791 | 6.4314 | ±12.8628 | -0.230 | 0.8181 |  |
| Age (years) | -0.0024 | 0.2698 | ±0.5397 | -0.009 | 0.9930 |  |
| BMI (kg/m2) | -0.5562 | 0.4372 | ±0.8743 | -1.272 | 0.2033 |  |
| Hypertension | -12.0347 | 6.1913 | ±12.3825 | -1.944 | 0.0519 | . |
| High cholesterol | +6.7443 | 5.5782 | ±11.1563 | +1.209 | 0.2266 |  |
| Kidney disease | +0.0674 | 11.8000 | ±23.6001 | +0.006 | 0.9954 |  |
| Circulatory disease | +4.2717 | 7.8882 | ±15.7764 | +0.542 | 0.5881 |  |
| **GMI (%)** | **-9.9682** | 4.6230 | ±9.2459 | **-2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **65.346** on **576** df, AIC = **6595.9**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+414.2266** | 26.2922 | ±52.5843 | **+15.755** | **6.37e-56** | *** |
| Education: graduate level (vs college) | +5.8878 | 6.0993 | ±12.1987 | +0.965 | 0.3344 |  |
| **Education: high school or below (vs college)** | **-22.8785** | 10.5415 | ±21.0831 | **-2.170** | **0.0300** | * |
| Site: UCSD (vs UAB) | -0.8545 | 7.7870 | ±15.5739 | -0.110 | 0.9126 |  |
| Site: UW (vs UAB) | -1.2957 | 6.4344 | ±12.8688 | -0.201 | 0.8404 |  |
| Age (years) | -0.0331 | 0.2711 | ±0.5422 | -0.122 | 0.9027 |  |
| BMI (kg/m2) | -0.5228 | 0.4370 | ±0.8740 | -1.196 | 0.2316 |  |
| Hypertension | -12.1223 | 6.1912 | ±12.3824 | -1.958 | 0.0502 | . |
| High cholesterol | +7.0193 | 5.5841 | ±11.1681 | +1.257 | 0.2087 |  |
| Kidney disease | -1.2605 | 11.6844 | ±23.3689 | -0.108 | 0.9141 |  |
| Circulatory disease | +4.2156 | 7.8712 | ±15.7423 | +0.536 | 0.5923 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.2371** | 0.1172 | ±0.2344 | **-2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **588**, R² = **0.0448**, Adj R² = **0.0265**, F-statistic = **2.45** (p = **0.0053**), Residual SE = **65.459** on **576** df, AIC = **6597.9**, BIC = **6650.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+394.7748** | 22.8692 | ±45.7383 | **+17.262** | **9.04e-67** | *** |
| Education: graduate level (vs college) | +5.5095 | 6.0825 | ±12.1650 | +0.906 | 0.3650 |  |
| **Education: high school or below (vs college)** | **-22.4650** | 10.7948 | ±21.5896 | **-2.081** | **0.0374** | * |
| Site: UCSD (vs UAB) | -1.0230 | 7.7942 | ±15.5884 | -0.131 | 0.8956 |  |
| Site: UW (vs UAB) | -1.9803 | 6.4391 | ±12.8782 | -0.308 | 0.7584 |  |
| Age (years) | +0.0297 | 0.2721 | ±0.5442 | +0.109 | 0.9131 |  |
| BMI (kg/m2) | -0.5939 | 0.4368 | ±0.8736 | -1.360 | 0.1739 |  |
| **Hypertension** | **-12.5791** | 6.1228 | ±12.2456 | **-2.054** | **0.0399** | * |
| High cholesterol | +6.1060 | 5.5809 | ±11.1618 | +1.094 | 0.2739 |  |
| Kidney disease | +0.8464 | 12.1097 | ±24.2195 | +0.070 | 0.9443 |  |
| Circulatory disease | +3.7996 | 7.9342 | ±15.8685 | +0.479 | 0.6320 |  |
| Glucose SD, pooled (mg/dL) | -0.3639 | 0.2317 | ±0.4634 | -1.571 | 0.1163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **588**, R² = **0.0437**, Adj R² = **0.0255**, F-statistic = **2.39** (p = **0.0066**), Residual SE = **65.494** on **576** df, AIC = **6598.5**, BIC = **6651.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.9268** | 22.8985 | ±45.7970 | **+17.203** | **2.51e-66** | *** |
| Education: graduate level (vs college) | +5.5174 | 6.0695 | ±12.1391 | +0.909 | 0.3633 |  |
| **Education: high school or below (vs college)** | **-22.5670** | 10.8358 | ±21.6715 | **-2.083** | **0.0373** | * |
| Site: UCSD (vs UAB) | -0.9197 | 7.8130 | ±15.6261 | -0.118 | 0.9063 |  |
| Site: UW (vs UAB) | -1.7646 | 6.4399 | ±12.8798 | -0.274 | 0.7841 |  |
| Age (years) | +0.0265 | 0.2720 | ±0.5441 | +0.097 | 0.9224 |  |
| BMI (kg/m2) | -0.5950 | 0.4372 | ±0.8743 | -1.361 | 0.1735 |  |
| **Hypertension** | **-12.7970** | 6.1299 | ±12.2597 | **-2.088** | **0.0368** | * |
| High cholesterol | +6.1447 | 5.5865 | ±11.1730 | +1.100 | 0.2714 |  |
| Kidney disease | +0.4952 | 12.0478 | ±24.0957 | +0.041 | 0.9672 |  |
| Circulatory disease | +3.7600 | 7.9506 | ±15.9012 | +0.473 | 0.6363 |  |
| Avg. daily SD (mg/dL) | -0.3622 | 0.2581 | ±0.5162 | -1.403 | 0.1606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **588**, R² = **0.0411**, Adj R² = **0.0227**, F-statistic = **2.24** (p = **0.0114**), Residual SE = **65.586** on **576** df, AIC = **6600.2**, BIC = **6652.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+391.0985** | 23.3288 | ±46.6575 | **+16.765** | **4.43e-63** | *** |
| Education: graduate level (vs college) | +5.8132 | 6.0741 | ±12.1482 | +0.957 | 0.3385 |  |
| **Education: high school or below (vs college)** | **-24.2912** | 10.8090 | ±21.6179 | **-2.247** | **0.0246** | * |
| Site: UCSD (vs UAB) | -1.0940 | 7.8471 | ±15.6942 | -0.139 | 0.8891 |  |
| Site: UW (vs UAB) | -1.3772 | 6.4404 | ±12.8809 | -0.214 | 0.8307 |  |
| Age (years) | -0.0037 | 0.2768 | ±0.5537 | -0.013 | 0.9895 |  |
| BMI (kg/m2) | -0.5952 | 0.4360 | ±0.8719 | -1.365 | 0.1722 |  |
| **Hypertension** | **-13.4844** | 6.1010 | ±12.2020 | **-2.210** | **0.0271** | * |
| High cholesterol | +5.8571 | 5.6013 | ±11.2026 | +1.046 | 0.2957 |  |
| Kidney disease | -1.4097 | 12.0515 | ±24.1030 | -0.117 | 0.9069 |  |
| Circulatory disease | +4.0517 | 7.9573 | ±15.9146 | +0.509 | 0.6106 |  |
| CV (%) | -0.1546 | 0.4726 | ±0.9452 | -0.327 | 0.7436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **588**, R² = **0.0410**, Adj R² = **0.0227**, F-statistic = **2.24** (p = **0.0115**), Residual SE = **65.588** on **576** df, AIC = **6600.2**, BIC = **6652.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.1472** | 27.4273 | ±54.8546 | **+14.042** | **8.57e-45** | *** |
| Education: graduate level (vs college) | +5.8796 | 6.0786 | ±12.1571 | +0.967 | 0.3334 |  |
| **Education: high school or below (vs college)** | **-24.4151** | 10.7620 | ±21.5239 | **-2.269** | **0.0233** | * |
| Site: UCSD (vs UAB) | -1.0604 | 7.8493 | ±15.6987 | -0.135 | 0.8925 |  |
| Site: UW (vs UAB) | -1.2639 | 6.4284 | ±12.8568 | -0.197 | 0.8441 |  |
| Age (years) | -0.0066 | 0.2769 | ±0.5539 | -0.024 | 0.9809 |  |
| BMI (kg/m2) | -0.5918 | 0.4361 | ±0.8723 | -1.357 | 0.1748 |  |
| **Hypertension** | **-13.5425** | 6.0949 | ±12.1898 | **-2.222** | **0.0263** | * |
| High cholesterol | +5.8715 | 5.5990 | ±11.1980 | +1.049 | 0.2943 |  |
| Kidney disease | -1.6954 | 11.8854 | ±23.7708 | -0.143 | 0.8866 |  |
| Circulatory disease | +4.1358 | 7.9418 | ±15.8836 | +0.521 | 0.6025 |  |
| Mean / SD ratio | +0.5381 | 2.1232 | ±4.2464 | +0.253 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **588**, R² = **0.0414**, Adj R² = **0.0231**, F-statistic = **2.26** (p = **0.0107**), Residual SE = **65.576** on **576** df, AIC = **6600.0**, BIC = **6652.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.9448** | 27.0783 | ±54.1565 | **+14.068** | **5.95e-45** | *** |
| Education: graduate level (vs college) | +5.8496 | 6.0757 | ±12.1514 | +0.963 | 0.3357 |  |
| **Education: high school or below (vs college)** | **-23.9831** | 10.7833 | ±21.5665 | **-2.224** | **0.0261** | * |
| Site: UCSD (vs UAB) | -0.8442 | 7.8631 | ±15.7262 | -0.107 | 0.9145 |  |
| Site: UW (vs UAB) | -1.3100 | 6.4285 | ±12.8571 | -0.204 | 0.8385 |  |
| Age (years) | +0.0095 | 0.2757 | ±0.5513 | +0.035 | 0.9724 |  |
| BMI (kg/m2) | -0.5903 | 0.4362 | ±0.8723 | -1.353 | 0.1759 |  |
| **Hypertension** | **-13.5099** | 6.0918 | ±12.1836 | **-2.218** | **0.0266** | * |
| High cholesterol | +5.9304 | 5.5961 | ±11.1921 | +1.060 | 0.2893 |  |
| Kidney disease | -1.3312 | 11.8118 | ±23.6235 | -0.113 | 0.9103 |  |
| Circulatory disease | +4.0925 | 7.9426 | ±15.8852 | +0.515 | 0.6064 |  |
| Avg. daily mean/SD | +0.9662 | 1.7096 | ±3.4191 | +0.565 | 0.5720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **588**, R² = **0.0727**, Adj R² = **0.0550**, F-statistic = **4.10** (p = **7.87e-06**), Residual SE = **64.495** on **576** df, AIC = **6580.5**, BIC = **6633.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+440.5311** | 24.9730 | ±49.9459 | **+17.640** | **1.21e-69** | *** |
| Education: graduate level (vs college) | +5.2860 | 5.9491 | ±11.8982 | +0.889 | 0.3742 |  |
| Education: high school or below (vs college) | -20.5308 | 10.6279 | ±21.2559 | -1.932 | 0.0534 | . |
| Site: UCSD (vs UAB) | +0.5428 | 7.7009 | ±15.4018 | +0.070 | 0.9438 |  |
| Site: UW (vs UAB) | -4.4992 | 6.2793 | ±12.5586 | -0.717 | 0.4737 |  |
| Age (years) | -0.0194 | 0.2652 | ±0.5303 | -0.073 | 0.9415 |  |
| BMI (kg/m2) | -0.5475 | 0.4235 | ±0.8470 | -1.293 | 0.1960 |  |
| **Hypertension** | **-12.3314** | 5.9712 | ±11.9424 | **-2.065** | **0.0389** | * |
| High cholesterol | +5.5483 | 5.5709 | ±11.1418 | +0.996 | 0.3193 |  |
| Kidney disease | -0.5871 | 11.6144 | ±23.2289 | -0.051 | 0.9597 |  |
| Circulatory disease | +3.8857 | 7.8835 | ±15.7670 | +0.493 | 0.6221 |  |
| **MAG (mg/dL/h)** | **-1.2816** | 0.3026 | ±0.6052 | **-4.236** | **2.28e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **588**, R² = **0.0445**, Adj R² = **0.0262**, F-statistic = **2.44** (p = **0.0056**), Residual SE = **65.469** on **576** df, AIC = **6598.1**, BIC = **6650.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.3006** | 23.4770 | ±46.9540 | **+16.966** | **1.48e-64** | *** |
| Education: graduate level (vs college) | +5.4475 | 6.0741 | ±12.1481 | +0.897 | 0.3698 |  |
| **Education: high school or below (vs college)** | **-22.3119** | 10.8438 | ±21.6875 | **-2.058** | **0.0396** | * |
| Site: UCSD (vs UAB) | -0.7990 | 7.8142 | ±15.6284 | -0.102 | 0.9186 |  |
| Site: UW (vs UAB) | -1.8024 | 6.4312 | ±12.8624 | -0.280 | 0.7793 |  |
| Age (years) | +0.0276 | 0.2716 | ±0.5432 | +0.101 | 0.9192 |  |
| BMI (kg/m2) | -0.6170 | 0.4379 | ±0.8758 | -1.409 | 0.1588 |  |
| **Hypertension** | **-12.8701** | 6.1092 | ±12.2183 | **-2.107** | **0.0351** | * |
| High cholesterol | +6.1443 | 5.5942 | ±11.1885 | +1.098 | 0.2721 |  |
| Kidney disease | +0.6249 | 11.9881 | ±23.9762 | +0.052 | 0.9584 |  |
| Circulatory disease | +3.9228 | 7.9621 | ±15.9242 | +0.493 | 0.6222 |  |
| Avg. daily range (mg/dL) | -0.1082 | 0.0694 | ±0.1388 | -1.558 | 0.1192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **588**, R² = **0.0466**, Adj R² = **0.0284**, F-statistic = **2.56** (p = **0.0036**), Residual SE = **65.396** on **576** df, AIC = **6596.8**, BIC = **6649.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.5888** | 22.6556 | ±45.3112 | **+17.373** | **1.33e-67** | *** |
| Education: graduate level (vs college) | +5.4879 | 6.1044 | ±12.2088 | +0.899 | 0.3687 |  |
| **Education: high school or below (vs college)** | **-23.7944** | 10.5487 | ±21.0975 | **-2.256** | **0.0241** | * |
| Site: UCSD (vs UAB) | -1.4969 | 7.7593 | ±15.5186 | -0.193 | 0.8470 |  |
| Site: UW (vs UAB) | -2.0621 | 6.4461 | ±12.8922 | -0.320 | 0.7490 |  |
| Age (years) | +0.0032 | 0.2719 | ±0.5438 | +0.012 | 0.9907 |  |
| BMI (kg/m2) | -0.5865 | 0.4356 | ±0.8713 | -1.346 | 0.1782 |  |
| **Hypertension** | **-12.4056** | 6.0989 | ±12.1979 | **-2.034** | **0.0419** | * |
| High cholesterol | +6.0156 | 5.5726 | ±11.1453 | +1.079 | 0.2804 |  |
| Kidney disease | -0.0482 | 11.9162 | ±23.8323 | -0.004 | 0.9968 |  |
| Circulatory disease | +4.4246 | 7.8519 | ±15.7038 | +0.564 | 0.5731 |  |
| SD of daily means (mg/dL) | -0.7480 | 0.4231 | ±0.8462 | -1.768 | 0.0771 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **588**, R² = **0.0476**, Adj R² = **0.0294**, F-statistic = **2.62** (p = **0.0029**), Residual SE = **65.363** on **576** df, AIC = **6596.2**, BIC = **6648.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+347.2395** | 31.6215 | ±63.2431 | **+10.981** | **4.71e-28** | *** |
| Education: graduate level (vs college) | +5.1421 | 6.0992 | ±12.1985 | +0.843 | 0.3992 |  |
| **Education: high school or below (vs college)** | **-22.7772** | 10.6094 | ±21.2188 | **-2.147** | **0.0318** | * |
| Site: UCSD (vs UAB) | -1.6238 | 7.7418 | ±15.4835 | -0.210 | 0.8339 |  |
| Site: UW (vs UAB) | -2.3990 | 6.4527 | ±12.9054 | -0.372 | 0.7101 |  |
| Age (years) | +0.0073 | 0.2707 | ±0.5414 | +0.027 | 0.9786 |  |
| BMI (kg/m2) | -0.5878 | 0.4366 | ±0.8732 | -1.346 | 0.1782 |  |
| **Hypertension** | **-12.5901** | 6.0925 | ±12.1849 | **-2.066** | **0.0388** | * |
| High cholesterol | +6.4255 | 5.5733 | ±11.1466 | +1.153 | 0.2489 |  |
| Kidney disease | +0.8490 | 11.9566 | ±23.9132 | +0.071 | 0.9434 |  |
| Circulatory disease | +4.1847 | 7.9041 | ±15.8081 | +0.529 | 0.5965 |  |
| **Time in range 70-180, pooled (%)** | **+0.4312** | 0.2191 | ±0.4382 | **+1.968** | **0.0491** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **588**, R² = **0.0473**, Adj R² = **0.0292**, F-statistic = **2.60** (p = **0.0031**), Residual SE = **65.370** on **576** df, AIC = **6596.3**, BIC = **6648.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+347.8095** | 31.8596 | ±63.7192 | **+10.917** | **9.57e-28** | *** |
| Education: graduate level (vs college) | +5.1301 | 6.1067 | ±12.2134 | +0.840 | 0.4009 |  |
| **Education: high school or below (vs college)** | **-22.7304** | 10.6193 | ±21.2386 | **-2.140** | **0.0323** | * |
| Site: UCSD (vs UAB) | -1.6198 | 7.7471 | ±15.4943 | -0.209 | 0.8344 |  |
| Site: UW (vs UAB) | -2.3991 | 6.4563 | ±12.9125 | -0.372 | 0.7102 |  |
| Age (years) | +0.0089 | 0.2709 | ±0.5418 | +0.033 | 0.9737 |  |
| BMI (kg/m2) | -0.5893 | 0.4368 | ±0.8736 | -1.349 | 0.1773 |  |
| **Hypertension** | **-12.6359** | 6.0961 | ±12.1923 | **-2.073** | **0.0382** | * |
| High cholesterol | +6.4614 | 5.5737 | ±11.1475 | +1.159 | 0.2463 |  |
| Kidney disease | +0.8464 | 11.9901 | ±23.9803 | +0.071 | 0.9437 |  |
| Circulatory disease | +4.1944 | 7.9096 | ±15.8192 | +0.530 | 0.5959 |  |
| Avg. daily time in range 70-180 (%) | +0.4226 | 0.2220 | ±0.4441 | +1.903 | 0.0570 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **588**, R² = **0.0409**, Adj R² = **0.0226**, F-statistic = **2.23** (p = **0.0118**), Residual SE = **65.592** on **576** df, AIC = **6600.3**, BIC = **6652.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.7359** | 22.6853 | ±45.3707 | **+17.136** | **8.00e-66** | *** |
| Education: graduate level (vs college) | +5.8997 | 6.0823 | ±12.1647 | +0.970 | 0.3321 |  |
| **Education: high school or below (vs college)** | **-24.7446** | 10.5945 | ±21.1891 | **-2.336** | **0.0195** | * |
| Site: UCSD (vs UAB) | -1.1542 | 7.9167 | ±15.8333 | -0.146 | 0.8841 |  |
| Site: UW (vs UAB) | -1.1855 | 6.5063 | ±13.0125 | -0.182 | 0.8554 |  |
| Age (years) | -0.0183 | 0.2715 | ±0.5431 | -0.067 | 0.9464 |  |
| BMI (kg/m2) | -0.5916 | 0.4366 | ±0.8732 | -1.355 | 0.1754 |  |
| **Hypertension** | **-13.6457** | 6.1038 | ±12.2077 | **-2.236** | **0.0254** | * |
| High cholesterol | +5.8573 | 5.6124 | ±11.2247 | +1.044 | 0.2967 |  |
| Kidney disease | -2.0659 | 11.6355 | ±23.2710 | -0.178 | 0.8591 |  |
| Circulatory disease | +4.1534 | 7.9371 | ±15.8743 | +0.523 | 0.6008 |  |
| Time < 54 (%) | -0.0669 | 2.6398 | ±5.2796 | -0.025 | 0.9798 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **588**, R² = **0.0409**, Adj R² = **0.0226**, F-statistic = **2.23** (p = **0.0118**), Residual SE = **65.592** on **576** df, AIC = **6600.3**, BIC = **6652.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.7517** | 22.6807 | ±45.3614 | **+17.140** | **7.44e-66** | *** |
| Education: graduate level (vs college) | +5.8874 | 6.0956 | ±12.1912 | +0.966 | 0.3341 |  |
| **Education: high school or below (vs college)** | **-24.7585** | 10.5962 | ±21.1925 | **-2.337** | **0.0195** | * |
| Site: UCSD (vs UAB) | -1.1754 | 7.8919 | ±15.7839 | -0.149 | 0.8816 |  |
| Site: UW (vs UAB) | -1.2155 | 6.5024 | ±13.0048 | -0.187 | 0.8517 |  |
| Age (years) | -0.0176 | 0.2724 | ±0.5447 | -0.065 | 0.9485 |  |
| BMI (kg/m2) | -0.5917 | 0.4363 | ±0.8725 | -1.356 | 0.1750 |  |
| **Hypertension** | **-13.6537** | 6.1100 | ±12.2200 | **-2.235** | **0.0254** | * |
| High cholesterol | +5.8446 | 5.6191 | ±11.2381 | +1.040 | 0.2983 |  |
| Kidney disease | -2.0575 | 11.6370 | ±23.2740 | -0.177 | 0.8597 |  |
| Circulatory disease | +4.1577 | 7.9383 | ±15.8766 | +0.524 | 0.6005 |  |
| Avg. daily time < 54 (%) | -0.1818 | 2.8833 | ±5.7665 | -0.063 | 0.9497 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **588**, R² = **0.0415**, Adj R² = **0.0232**, F-statistic = **2.27** (p = **0.0104**), Residual SE = **65.570** on **576** df, AIC = **6599.9**, BIC = **6652.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.4005** | 22.6179 | ±45.2358 | **+17.128** | **9.17e-66** | *** |
| Education: graduate level (vs college) | +6.1286 | 6.0864 | ±12.1728 | +1.007 | 0.3140 |  |
| **Education: high school or below (vs college)** | **-24.7432** | 10.6088 | ±21.2176 | **-2.332** | **0.0197** | * |
| Site: UCSD (vs UAB) | -0.7561 | 7.8602 | ±15.7204 | -0.096 | 0.9234 |  |
| Site: UW (vs UAB) | -0.7521 | 6.4392 | ±12.8783 | -0.117 | 0.9070 |  |
| Age (years) | -0.0240 | 0.2721 | ±0.5441 | -0.088 | 0.9297 |  |
| BMI (kg/m2) | -0.5906 | 0.4362 | ±0.8724 | -1.354 | 0.1757 |  |
| **Hypertension** | **-13.4432** | 6.1378 | ±12.2756 | **-2.190** | **0.0285** | * |
| High cholesterol | +5.9844 | 5.6028 | ±11.2057 | +1.068 | 0.2855 |  |
| Kidney disease | -2.1833 | 11.6226 | ±23.2453 | -0.188 | 0.8510 |  |
| Circulatory disease | +4.2355 | 7.9296 | ±15.8593 | +0.534 | 0.5932 |  |
| Time 54-69, pooled (%) | +0.7337 | 1.0762 | ±2.1523 | +0.682 | 0.4954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **588**, R² = **0.0413**, Adj R² = **0.0230**, F-statistic = **2.26** (p = **0.0108**), Residual SE = **65.577** on **576** df, AIC = **6600.0**, BIC = **6652.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.9494** | 22.6336 | ±45.2673 | **+17.140** | **7.41e-66** | *** |
| Education: graduate level (vs college) | +6.0985 | 6.0939 | ±12.1878 | +1.001 | 0.3169 |  |
| **Education: high school or below (vs college)** | **-24.7504** | 10.6174 | ±21.2348 | **-2.331** | **0.0197** | * |
| Site: UCSD (vs UAB) | -0.8743 | 7.8603 | ±15.7206 | -0.111 | 0.9114 |  |
| Site: UW (vs UAB) | -0.8120 | 6.4377 | ±12.8755 | -0.126 | 0.8996 |  |
| Age (years) | -0.0256 | 0.2724 | ±0.5448 | -0.094 | 0.9250 |  |
| BMI (kg/m2) | -0.5913 | 0.4364 | ±0.8729 | -1.355 | 0.1755 |  |
| **Hypertension** | **-13.4903** | 6.1348 | ±12.2695 | **-2.199** | **0.0279** | * |
| High cholesterol | +5.9501 | 5.6035 | ±11.2071 | +1.062 | 0.2883 |  |
| Kidney disease | -2.1611 | 11.6158 | ±23.2316 | -0.186 | 0.8524 |  |
| Circulatory disease | +4.2131 | 7.9339 | ±15.8677 | +0.531 | 0.5954 |  |
| Avg. daily time 54-69 (%) | +0.5716 | 1.0260 | ±2.0521 | +0.557 | 0.5774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **588**, R² = **0.0413**, Adj R² = **0.0230**, F-statistic = **2.26** (p = **0.0109**), Residual SE = **65.578** on **576** df, AIC = **6600.0**, BIC = **6652.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.4910** | 22.6177 | ±45.2355 | **+17.132** | **8.54e-66** | *** |
| Education: graduate level (vs college) | +6.0716 | 6.0873 | ±12.1745 | +0.997 | 0.3186 |  |
| **Education: high school or below (vs college)** | **-24.6700** | 10.6001 | ±21.2002 | **-2.327** | **0.0199** | * |
| Site: UCSD (vs UAB) | -0.7322 | 7.8795 | ±15.7591 | -0.093 | 0.9260 |  |
| Site: UW (vs UAB) | -0.7656 | 6.4612 | ±12.9225 | -0.118 | 0.9057 |  |
| Age (years) | -0.0223 | 0.2721 | ±0.5442 | -0.082 | 0.9347 |  |
| BMI (kg/m2) | -0.5895 | 0.4360 | ±0.8721 | -1.352 | 0.1764 |  |
| **Hypertension** | **-13.4737** | 6.1344 | ±12.2688 | **-2.196** | **0.0281** | * |
| High cholesterol | +6.0013 | 5.6070 | ±11.2140 | +1.070 | 0.2845 |  |
| Kidney disease | -2.1649 | 11.6300 | ±23.2600 | -0.186 | 0.8523 |  |
| Circulatory disease | +4.1886 | 7.9304 | ±15.8609 | +0.528 | 0.5974 |  |
| Time < 70 (%) | +0.4694 | 0.8332 | ±1.6664 | +0.563 | 0.5731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **588**, R² = **0.0412**, Adj R² = **0.0228**, F-statistic = **2.25** (p = **0.0112**), Residual SE = **65.583** on **576** df, AIC = **6600.1**, BIC = **6652.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.0607** | 22.6363 | ±45.2726 | **+17.143** | **7.05e-66** | *** |
| Education: graduate level (vs college) | +6.0636 | 6.0974 | ±12.1949 | +0.994 | 0.3200 |  |
| **Education: high school or below (vs college)** | **-24.6960** | 10.6061 | ±21.2122 | **-2.328** | **0.0199** | * |
| Site: UCSD (vs UAB) | -0.8727 | 7.8709 | ±15.7417 | -0.111 | 0.9117 |  |
| Site: UW (vs UAB) | -0.8323 | 6.4538 | ±12.9075 | -0.129 | 0.8974 |  |
| Age (years) | -0.0246 | 0.2726 | ±0.5451 | -0.090 | 0.9282 |  |
| BMI (kg/m2) | -0.5906 | 0.4363 | ±0.8726 | -1.354 | 0.1758 |  |
| **Hypertension** | **-13.5136** | 6.1333 | ±12.2665 | **-2.203** | **0.0276** | * |
| High cholesterol | +5.9647 | 5.6079 | ±11.2158 | +1.064 | 0.2875 |  |
| Kidney disease | -2.1534 | 11.6210 | ±23.2420 | -0.185 | 0.8530 |  |
| Circulatory disease | +4.1780 | 7.9347 | ±15.8695 | +0.527 | 0.5985 |  |
| Avg. daily time < 70 (%) | +0.3746 | 0.8051 | ±1.6102 | +0.465 | 0.6418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **588**, R² = **0.0503**, Adj R² = **0.0322**, F-statistic = **2.78** (p = **0.0016**), Residual SE = **65.268** on **576** df, AIC = **6594.5**, BIC = **6647.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+280.5287** | 48.9210 | ±97.8420 | **+5.734** | **9.79e-09** | *** |
| Education: graduate level (vs college) | +5.1939 | 6.0887 | ±12.1774 | +0.853 | 0.3936 |  |
| **Education: high school or below (vs college)** | **-22.7163** | 10.5145 | ±21.0289 | **-2.160** | **0.0307** | * |
| Site: UCSD (vs UAB) | -1.7861 | 7.7460 | ±15.4919 | -0.231 | 0.8176 |  |
| Site: UW (vs UAB) | -2.6477 | 6.4345 | ±12.8691 | -0.411 | 0.6807 |  |
| Age (years) | -0.0222 | 0.2684 | ±0.5369 | -0.083 | 0.9342 |  |
| BMI (kg/m2) | -0.6017 | 0.4367 | ±0.8734 | -1.378 | 0.1682 |  |
| **Hypertension** | **-12.7562** | 6.0580 | ±12.1161 | **-2.106** | **0.0352** | * |
| High cholesterol | +5.5033 | 5.5672 | ±11.1345 | +0.989 | 0.3229 |  |
| Kidney disease | -0.3282 | 11.6667 | ±23.3333 | -0.028 | 0.9776 |  |
| Circulatory disease | +4.5591 | 7.8867 | ±15.7734 | +0.578 | 0.5632 |  |
| **Time 54-250, pooled (%)** | **+1.1091** | 0.4379 | ±0.8759 | **+2.533** | **0.0113** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **588**, R² = **0.0516**, Adj R² = **0.0334**, F-statistic = **2.85** (p = **0.0012**), Residual SE = **65.226** on **576** df, AIC = **6593.7**, BIC = **6646.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+260.9390** | 51.0205 | ±102.0410 | **+5.114** | **3.15e-07** | *** |
| Education: graduate level (vs college) | +5.0574 | 6.0907 | ±12.1815 | +0.830 | 0.4063 |  |
| **Education: high school or below (vs college)** | **-22.2476** | 10.5224 | ±21.0447 | **-2.114** | **0.0345** | * |
| Site: UCSD (vs UAB) | -1.6872 | 7.7297 | ±15.4595 | -0.218 | 0.8272 |  |
| Site: UW (vs UAB) | -2.6829 | 6.4333 | ±12.8666 | -0.417 | 0.6767 |  |
| Age (years) | -0.0143 | 0.2686 | ±0.5372 | -0.053 | 0.9575 |  |
| BMI (kg/m2) | -0.6086 | 0.4368 | ±0.8735 | -1.394 | 0.1635 |  |
| **Hypertension** | **-12.6867** | 6.0567 | ±12.1133 | **-2.095** | **0.0362** | * |
| High cholesterol | +5.5400 | 5.5648 | ±11.1296 | +0.996 | 0.3195 |  |
| Kidney disease | +0.1159 | 11.7015 | ±23.4030 | +0.010 | 0.9921 |  |
| Circulatory disease | +4.6810 | 7.8859 | ±15.7718 | +0.594 | 0.5528 |  |
| **Avg. daily time 54-250 (%)** | **+1.3014** | 0.4600 | ±0.9200 | **+2.829** | **0.0047** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **588**, R² = **0.0446**, Adj R² = **0.0263**, F-statistic = **2.44** (p = **0.0055**), Residual SE = **65.466** on **576** df, AIC = **6598.0**, BIC = **6650.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.5176** | 22.7706 | ±45.5412 | **+17.062** | **2.83e-65** | *** |
| Education: graduate level (vs college) | +5.5202 | 6.0930 | ±12.1860 | +0.906 | 0.3649 |  |
| **Education: high school or below (vs college)** | **-23.4674** | 10.6388 | ±21.2775 | **-2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | -1.1502 | 7.7785 | ±15.5571 | -0.148 | 0.8825 |  |
| Site: UW (vs UAB) | -1.6151 | 6.4479 | ±12.8958 | -0.250 | 0.8022 |  |
| Age (years) | +0.0074 | 0.2717 | ±0.5435 | +0.027 | 0.9782 |  |
| BMI (kg/m2) | -0.5826 | 0.4363 | ±0.8725 | -1.336 | 0.1817 |  |
| **Hypertension** | **-12.7480** | 6.1337 | ±12.2674 | **-2.078** | **0.0377** | * |
| High cholesterol | +6.7018 | 5.6094 | ±11.2187 | +1.195 | 0.2322 |  |
| Kidney disease | +0.2904 | 12.0227 | ±24.0453 | +0.024 | 0.9807 |  |
| Circulatory disease | +4.0693 | 7.9282 | ±15.8563 | +0.513 | 0.6078 |  |
| Time 181-250, pooled (%) | -0.4679 | 0.3301 | ±0.6602 | -1.418 | 0.1563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **588**, R² = **0.0444**, Adj R² = **0.0261**, F-statistic = **2.43** (p = **0.0058**), Residual SE = **65.473** on **576** df, AIC = **6598.2**, BIC = **6650.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.7487** | 22.7667 | ±45.5334 | **+17.075** | **2.27e-65** | *** |
| Education: graduate level (vs college) | +5.5327 | 6.0990 | ±12.1980 | +0.907 | 0.3643 |  |
| **Education: high school or below (vs college)** | **-23.4946** | 10.6353 | ±21.2707 | **-2.209** | **0.0272** | * |
| Site: UCSD (vs UAB) | -1.2547 | 7.7810 | ±15.5621 | -0.161 | 0.8719 |  |
| Site: UW (vs UAB) | -1.6670 | 6.4502 | ±12.9004 | -0.258 | 0.7961 |  |
| Age (years) | +0.0032 | 0.2716 | ±0.5431 | +0.012 | 0.9907 |  |
| BMI (kg/m2) | -0.5832 | 0.4366 | ±0.8732 | -1.336 | 0.1816 |  |
| **Hypertension** | **-12.7974** | 6.1396 | ±12.2792 | **-2.084** | **0.0371** | * |
| High cholesterol | +6.6650 | 5.6072 | ±11.2143 | +1.189 | 0.2346 |  |
| Kidney disease | +0.1681 | 12.0374 | ±24.0748 | +0.014 | 0.9889 |  |
| Circulatory disease | +4.0644 | 7.9383 | ±15.8765 | +0.512 | 0.6087 |  |
| Avg. daily time 181-250 (%) | -0.4422 | 0.3269 | ±0.6539 | -1.353 | 0.1762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **588**, R² = **0.0483**, Adj R² = **0.0302**, F-statistic = **2.66** (p = **0.0025**), Residual SE = **65.337** on **576** df, AIC = **6595.7**, BIC = **6648.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.2950** | 22.7257 | ±45.4514 | **+17.130** | **8.84e-66** | *** |
| Education: graduate level (vs college) | +5.2627 | 6.1040 | ±12.2081 | +0.862 | 0.3886 |  |
| **Education: high school or below (vs college)** | **-22.6045** | 10.5968 | ±21.1936 | **-2.133** | **0.0329** | * |
| Site: UCSD (vs UAB) | -1.2641 | 7.7357 | ±15.4714 | -0.163 | 0.8702 |  |
| Site: UW (vs UAB) | -2.0797 | 6.4489 | ±12.8977 | -0.322 | 0.7471 |  |
| Age (years) | +0.0048 | 0.2703 | ±0.5407 | +0.018 | 0.9858 |  |
| BMI (kg/m2) | -0.5857 | 0.4364 | ±0.8728 | -1.342 | 0.1795 |  |
| **Hypertension** | **-12.3698** | 6.1201 | ±12.2402 | **-2.021** | **0.0433** | * |
| High cholesterol | +6.5884 | 5.5713 | ±11.1425 | +1.183 | 0.2370 |  |
| Kidney disease | +0.9203 | 11.9531 | ±23.9063 | +0.077 | 0.9386 |  |
| Circulatory disease | +4.2230 | 7.8933 | ±15.7866 | +0.535 | 0.5926 |  |
| **Time > 180 (%)** | **-0.4554** | 0.2208 | ±0.4416 | **-2.063** | **0.0391** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **65.346** on **576** df, AIC = **6595.9**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.4065** | 22.7380 | ±45.4759 | **+17.126** | **9.53e-66** | *** |
| Education: graduate level (vs college) | +5.2743 | 6.1084 | ±12.2167 | +0.863 | 0.3879 |  |
| **Education: high school or below (vs college)** | **-22.5596** | 10.6075 | ±21.2151 | **-2.127** | **0.0334** | * |
| Site: UCSD (vs UAB) | -1.3400 | 7.7381 | ±15.4762 | -0.173 | 0.8625 |  |
| Site: UW (vs UAB) | -2.0757 | 6.4528 | ±12.9056 | -0.322 | 0.7477 |  |
| Age (years) | +0.0031 | 0.2705 | ±0.5409 | +0.011 | 0.9909 |  |
| BMI (kg/m2) | -0.5882 | 0.4369 | ±0.8738 | -1.346 | 0.1782 |  |
| **Hypertension** | **-12.4222** | 6.1256 | ±12.2512 | **-2.028** | **0.0426** | * |
| High cholesterol | +6.6169 | 5.5721 | ±11.1442 | +1.188 | 0.2350 |  |
| Kidney disease | +0.9264 | 11.9879 | ±23.9759 | +0.077 | 0.9384 |  |
| Circulatory disease | +4.2294 | 7.9010 | ±15.8020 | +0.535 | 0.5924 |  |
| **Avg. daily time > 180 (%)** | **-0.4488** | 0.2276 | ±0.4552 | **-1.972** | **0.0486** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **588**, R² = **0.0461**, Adj R² = **0.0279**, F-statistic = **2.53** (p = **0.0040**), Residual SE = **65.413** on **576** df, AIC = **6597.1**, BIC = **6649.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.1392** | 22.6981 | ±45.3961 | **+17.144** | **6.95e-66** | *** |
| Education: graduate level (vs college) | +5.3370 | 6.1136 | ±12.2273 | +0.873 | 0.3827 |  |
| **Education: high school or below (vs college)** | **-23.5539** | 10.5377 | ±21.0754 | **-2.235** | **0.0254** | * |
| Site: UCSD (vs UAB) | -1.4553 | 7.7609 | ±15.5217 | -0.188 | 0.8513 |  |
| Site: UW (vs UAB) | -1.8293 | 6.4603 | ±12.9206 | -0.283 | 0.7771 |  |
| Age (years) | -0.0159 | 0.2709 | ±0.5419 | -0.059 | 0.9532 |  |
| BMI (kg/m2) | -0.5713 | 0.4354 | ±0.8708 | -1.312 | 0.1895 |  |
| **Hypertension** | **-12.5438** | 6.1189 | ±12.2379 | **-2.050** | **0.0404** | * |
| High cholesterol | +6.4417 | 5.5741 | ±11.1481 | +1.156 | 0.2478 |  |
| Kidney disease | -0.8704 | 11.7536 | ±23.5073 | -0.074 | 0.9410 |  |
| Circulatory disease | +4.4063 | 7.8994 | ±15.7988 | +0.558 | 0.5770 |  |
| Nocturnal time > 180 (%) | -0.3927 | 0.2508 | ±0.5015 | -1.566 | 0.1173 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **588**, R² = **0.0416**, Adj R² = **0.0233**, F-statistic = **2.27** (p = **0.0102**), Residual SE = **65.568** on **576** df, AIC = **6599.9**, BIC = **6652.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.9674** | 22.7199 | ±45.4399 | **+17.120** | **1.05e-65** | *** |
| Education: graduate level (vs college) | +5.6434 | 6.1050 | ±12.2099 | +0.924 | 0.3553 |  |
| **Education: high school or below (vs college)** | **-24.2464** | 10.6030 | ±21.2060 | **-2.287** | **0.0222** | * |
| Site: UCSD (vs UAB) | -0.9102 | 7.8636 | ±15.7273 | -0.116 | 0.9079 |  |
| Site: UW (vs UAB) | -1.2726 | 6.4376 | ±12.8752 | -0.198 | 0.8433 |  |
| Age (years) | -0.0010 | 0.2744 | ±0.5488 | -0.004 | 0.9969 |  |
| BMI (kg/m2) | -0.6065 | 0.4374 | ±0.8747 | -1.387 | 0.1655 |  |
| **Hypertension** | **-13.1517** | 6.1431 | ±12.2862 | **-2.141** | **0.0323** | * |
| High cholesterol | +6.0527 | 5.6025 | ±11.2050 | +1.080 | 0.2800 |  |
| Kidney disease | -1.2097 | 11.8972 | ±23.7944 | -0.102 | 0.9190 |  |
| Circulatory disease | +3.9753 | 7.9968 | ±15.9937 | +0.497 | 0.6191 |  |
| Any reading > 250 during wear (0/1) | -4.0743 | 6.5443 | ±13.0886 | -0.623 | 0.5336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **588**, R² = **0.0506**, Adj R² = **0.0325**, F-statistic = **2.79** (p = **0.0015**), Residual SE = **65.259** on **576** df, AIC = **6594.3**, BIC = **6646.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.6177** | 22.5993 | ±45.1987 | **+17.284** | **6.16e-67** | *** |
| Education: graduate level (vs college) | +5.2331 | 6.0909 | ±12.1818 | +0.859 | 0.3902 |  |
| **Education: high school or below (vs college)** | **-22.4902** | 10.5238 | ±21.0475 | **-2.137** | **0.0326** | * |
| Site: UCSD (vs UAB) | -1.4179 | 7.7404 | ±15.4808 | -0.183 | 0.8547 |  |
| Site: UW (vs UAB) | -2.3592 | 6.4239 | ±12.8478 | -0.367 | 0.7134 |  |
| Age (years) | -0.0231 | 0.2685 | ±0.5370 | -0.086 | 0.9314 |  |
| BMI (kg/m2) | -0.5985 | 0.4364 | ±0.8729 | -1.371 | 0.1703 |  |
| **Hypertension** | **-12.6337** | 6.0671 | ±12.1341 | **-2.082** | **0.0373** | * |
| High cholesterol | +5.6380 | 5.5632 | ±11.1265 | +1.013 | 0.3109 |  |
| Kidney disease | -0.3351 | 11.6656 | ±23.3312 | -0.029 | 0.9771 |  |
| Circulatory disease | +4.5303 | 7.8751 | ±15.7503 | +0.575 | 0.5651 |  |
| **Time > 250 (%)** | **-1.1399** | 0.4393 | ±0.8786 | **-2.595** | **0.0095** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **588**, R² = **0.0519**, Adj R² = **0.0338**, F-statistic = **2.87** (p = **0.0011**), Residual SE = **65.215** on **576** df, AIC = **6593.5**, BIC = **6646.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.6537** | 22.6112 | ±45.2224 | **+17.277** | **7.01e-67** | *** |
| Education: graduate level (vs college) | +5.1446 | 6.0902 | ±12.1804 | +0.845 | 0.3983 |  |
| **Education: high school or below (vs college)** | **-21.9849** | 10.5410 | ±21.0820 | **-2.086** | **0.0370** | * |
| Site: UCSD (vs UAB) | -1.3818 | 7.7251 | ±15.4503 | -0.179 | 0.8580 |  |
| Site: UW (vs UAB) | -2.3698 | 6.4248 | ±12.8497 | -0.369 | 0.7122 |  |
| Age (years) | -0.0194 | 0.2685 | ±0.5371 | -0.072 | 0.9423 |  |
| BMI (kg/m2) | -0.6068 | 0.4369 | ±0.8739 | -1.389 | 0.1649 |  |
| **Hypertension** | **-12.5518** | 6.0664 | ±12.1327 | **-2.069** | **0.0385** | * |
| High cholesterol | +5.6858 | 5.5596 | ±11.1192 | +1.023 | 0.3065 |  |
| Kidney disease | +0.1056 | 11.6976 | ±23.3951 | +0.009 | 0.9928 |  |
| Circulatory disease | +4.6501 | 7.8749 | ±15.7498 | +0.590 | 0.5549 |  |
| **Avg. daily time > 250 (%)** | **-1.3466** | 0.4771 | ±0.9542 | **-2.822** | **0.0048** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 577; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **577**, R² = **0.1182**, Adj R² = **0.1027**, F-statistic = **7.59** (p = **2.06e-11**), Residual SE = **16.872** on **566** df, AIC = **4909.2**, BIC = **4957.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1190** | 6.0827 | ±12.1654 | **+11.034** | **2.61e-28** | *** |
| Education: graduate level (vs college) | -2.6214 | 1.5393 | ±3.0785 | -1.703 | 0.0886 | . |
| Education: high school or below (vs college) | +0.3677 | 2.6656 | ±5.3312 | +0.138 | 0.8903 |  |
| Site: UCSD (vs UAB) | +1.9482 | 2.0475 | ±4.0949 | +0.952 | 0.3413 |  |
| Site: UW (vs UAB) | -3.1233 | 1.6824 | ±3.3648 | -1.856 | 0.0634 | . |
| **Age (years)** | **-0.3932** | 0.0703 | ±0.1407 | **-5.590** | **2.27e-08** | *** |
| **BMI (kg/m2)** | **+0.2972** | 0.1095 | ±0.2190 | **+2.713** | **0.0067** | ** |
| Hypertension | +1.3338 | 1.6243 | ±3.2486 | +0.821 | 0.4115 |  |
| High cholesterol | +1.8563 | 1.5172 | ±3.0344 | +1.224 | 0.2211 |  |
| Kidney disease | -0.9888 | 3.0864 | ±6.1728 | -0.320 | 0.7487 |  |
| Circulatory disease | -2.4511 | 1.9500 | ±3.8999 | -1.257 | 0.2088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **577**, R² = **0.1328**, Adj R² = **0.1159**, F-statistic = **7.87** (p = **8.89e-13**), Residual SE = **16.747** on **565** df, AIC = **4901.6**, BIC = **4953.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.1031** | 7.9721 | ±15.9443 | **+6.787** | **1.15e-11** | *** |
| Education: graduate level (vs college) | -2.2575 | 1.5416 | ±3.0831 | -1.464 | 0.1431 |  |
| Education: high school or below (vs college) | -0.4541 | 2.6307 | ±5.2614 | -0.173 | 0.8629 |  |
| Site: UCSD (vs UAB) | +1.7601 | 2.0401 | ±4.0803 | +0.863 | 0.3883 |  |
| Site: UW (vs UAB) | -2.7521 | 1.6733 | ±3.3466 | -1.645 | 0.1000 |  |
| **Age (years)** | **-0.4207** | 0.0707 | ±0.1413 | **-5.954** | **2.62e-09** | *** |
| **BMI (kg/m2)** | **+0.2717** | 0.1076 | ±0.2152 | **+2.525** | **0.0116** | * |
| Hypertension | +0.8684 | 1.6269 | ±3.2537 | +0.534 | 0.5935 |  |
| High cholesterol | +1.5203 | 1.5212 | ±3.0423 | +0.999 | 0.3176 |  |
| Kidney disease | -1.2548 | 2.9860 | ±5.9720 | -0.420 | 0.6743 |  |
| Circulatory disease | -2.3033 | 1.9620 | ±3.9241 | -1.174 | 0.2404 |  |
| **HbA1c (%)** | **+2.6515** | 1.0813 | ±2.1625 | **+2.452** | **0.0142** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **577**, R² = **0.1265**, Adj R² = **0.1095**, F-statistic = **7.44** (p = **5.49e-12**), Residual SE = **16.807** on **565** df, AIC = **4905.7**, BIC = **4958.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.8472** | 7.0267 | ±14.0534 | **+8.517** | **1.64e-17** | *** |
| Education: graduate level (vs college) | -2.5935 | 1.5372 | ±3.0744 | -1.687 | 0.0916 | . |
| Education: high school or below (vs college) | -0.1807 | 2.6530 | ±5.3061 | -0.068 | 0.9457 |  |
| Site: UCSD (vs UAB) | +1.8215 | 2.0451 | ±4.0902 | +0.891 | 0.3731 |  |
| Site: UW (vs UAB) | -3.0360 | 1.6728 | ±3.3456 | -1.815 | 0.0695 | . |
| **Age (years)** | **-0.3974** | 0.0702 | ±0.1404 | **-5.662** | **1.50e-08** | *** |
| **BMI (kg/m2)** | **+0.2867** | 0.1094 | ±0.2188 | **+2.621** | **0.0088** | ** |
| Hypertension | +0.8892 | 1.6431 | ±3.2863 | +0.541 | 0.5884 |  |
| High cholesterol | +1.5898 | 1.5190 | ±3.0379 | +1.047 | 0.2953 |  |
| Kidney disease | -1.6388 | 3.0145 | ±6.0289 | -0.544 | 0.5867 |  |
| Circulatory disease | -2.4968 | 1.9689 | ±3.9377 | -1.268 | 0.2047 |  |
| **Mean glucose (mg/dL)** | **+0.0679** | 0.0337 | ±0.0673 | **+2.016** | **0.0438** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **577**, R² = **0.1265**, Adj R² = **0.1095**, F-statistic = **7.44** (p = **5.49e-12**), Residual SE = **16.807** on **565** df, AIC = **4905.7**, BIC = **4958.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.4546** | 10.2105 | ±20.4210 | **+4.941** | **7.75e-07** | *** |
| Education: graduate level (vs college) | -2.5935 | 1.5372 | ±3.0744 | -1.687 | 0.0916 | . |
| Education: high school or below (vs college) | -0.1807 | 2.6530 | ±5.3061 | -0.068 | 0.9457 |  |
| Site: UCSD (vs UAB) | +1.8215 | 2.0451 | ±4.0902 | +0.891 | 0.3731 |  |
| Site: UW (vs UAB) | -3.0360 | 1.6728 | ±3.3456 | -1.815 | 0.0695 | . |
| **Age (years)** | **-0.3974** | 0.0702 | ±0.1404 | **-5.662** | **1.50e-08** | *** |
| **BMI (kg/m2)** | **+0.2867** | 0.1094 | ±0.2188 | **+2.621** | **0.0088** | ** |
| Hypertension | +0.8892 | 1.6431 | ±3.2863 | +0.541 | 0.5884 |  |
| High cholesterol | +1.5898 | 1.5190 | ±3.0379 | +1.047 | 0.2953 |  |
| Kidney disease | -1.6388 | 3.0145 | ±6.0289 | -0.544 | 0.5867 |  |
| Circulatory disease | -2.4968 | 1.9689 | ±3.9377 | -1.268 | 0.2047 |  |
| **GMI (%)** | **+2.8376** | 1.4078 | ±2.8155 | **+2.016** | **0.0438** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **577**, R² = **0.1226**, Adj R² = **0.1056**, F-statistic = **7.18** (p = **1.69e-11**), Residual SE = **16.845** on **565** df, AIC = **4908.3**, BIC = **4960.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.7994** | 7.0225 | ±14.0450 | **+8.800** | **1.37e-18** | *** |
| Education: graduate level (vs college) | -2.6152 | 1.5398 | ±3.0796 | -1.698 | 0.0894 | . |
| Education: high school or below (vs college) | +0.0135 | 2.6465 | ±5.2930 | +0.005 | 0.9959 |  |
| Site: UCSD (vs UAB) | +1.8294 | 2.0520 | ±4.1040 | +0.892 | 0.3727 |  |
| Site: UW (vs UAB) | -3.1054 | 1.6784 | ±3.3567 | -1.850 | 0.0643 | . |
| **Age (years)** | **-0.3896** | 0.0704 | ±0.1408 | **-5.533** | **3.15e-08** | *** |
| **BMI (kg/m2)** | **+0.2824** | 0.1097 | ±0.2194 | **+2.574** | **0.0101** | * |
| Hypertension | +1.0051 | 1.6428 | ±3.2855 | +0.612 | 0.5407 |  |
| High cholesterol | +1.6221 | 1.5153 | ±3.0307 | +1.070 | 0.2844 |  |
| Kidney disease | -1.1672 | 3.0229 | ±6.0459 | -0.386 | 0.6994 |  |
| Circulatory disease | -2.4653 | 1.9646 | ±3.9291 | -1.255 | 0.2095 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0493 | 0.0316 | ±0.0632 | +1.558 | 0.1192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **577**, R² = **0.1268**, Adj R² = **0.1098**, F-statistic = **7.46** (p = **5.06e-12**), Residual SE = **16.805** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.6672** | 6.1530 | ±12.3060 | **+10.510** | **7.78e-26** | *** |
| Education: graduate level (vs college) | -2.4692 | 1.5411 | ±3.0822 | -1.602 | 0.1091 |  |
| Education: high school or below (vs college) | -0.4887 | 2.6862 | ±5.3724 | -0.182 | 0.8556 |  |
| Site: UCSD (vs UAB) | +1.8803 | 2.0311 | ±4.0622 | +0.926 | 0.3546 |  |
| Site: UW (vs UAB) | -2.7990 | 1.6775 | ±3.3549 | -1.669 | 0.0952 | . |
| **Age (years)** | **-0.4125** | 0.0711 | ±0.1421 | **-5.805** | **6.44e-09** | *** |
| **BMI (kg/m2)** | **+0.2990** | 0.1090 | ±0.2181 | **+2.742** | **0.0061** | ** |
| Hypertension | +0.9439 | 1.6319 | ±3.2638 | +0.578 | 0.5630 |  |
| High cholesterol | +1.7454 | 1.5197 | ±3.0394 | +1.149 | 0.2507 |  |
| Kidney disease | -2.2187 | 3.1049 | ±6.2097 | -0.715 | 0.4749 |  |
| Circulatory disease | -2.3329 | 1.9604 | ±3.9208 | -1.190 | 0.2340 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1451** | 0.0695 | ±0.1391 | **+2.086** | **0.0370** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **577**, R² = **0.1252**, Adj R² = **0.1081**, F-statistic = **7.35** (p = **8.18e-12**), Residual SE = **16.821** on **565** df, AIC = **4906.6**, BIC = **4958.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.9111** | 6.1598 | ±12.3197 | **+10.538** | **5.78e-26** | *** |
| Education: graduate level (vs college) | -2.4626 | 1.5397 | ±3.0795 | -1.599 | 0.1097 |  |
| Education: high school or below (vs college) | -0.4912 | 2.7014 | ±5.4028 | -0.182 | 0.8557 |  |
| Site: UCSD (vs UAB) | +1.8466 | 2.0337 | ±4.0674 | +0.908 | 0.3639 |  |
| Site: UW (vs UAB) | -2.8724 | 1.6794 | ±3.3588 | -1.710 | 0.0872 | . |
| **Age (years)** | **-0.4122** | 0.0714 | ±0.1429 | **-5.771** | **7.88e-09** | *** |
| **BMI (kg/m2)** | **+0.2995** | 0.1092 | ±0.2185 | **+2.741** | **0.0061** | ** |
| Hypertension | +1.0070 | 1.6304 | ±3.2607 | +0.618 | 0.5368 |  |
| High cholesterol | +1.7299 | 1.5244 | ±3.0487 | +1.135 | 0.2565 |  |
| Kidney disease | -2.1151 | 3.1242 | ±6.2484 | -0.677 | 0.4984 |  |
| Circulatory disease | -2.3028 | 1.9650 | ±3.9300 | -1.172 | 0.2412 |  |
| Avg. daily SD (mg/dL) | +0.1514 | 0.0844 | ±0.1688 | +1.794 | 0.0728 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **577**, R² = **0.1252**, Adj R² = **0.1082**, F-statistic = **7.35** (p = **8.04e-12**), Residual SE = **16.820** on **565** df, AIC = **4906.6**, BIC = **4958.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9624** | 6.3407 | ±12.6814 | **+9.930** | **3.09e-23** | *** |
| Education: graduate level (vs college) | -2.4701 | 1.5395 | ±3.0789 | -1.605 | 0.1086 |  |
| Education: high school or below (vs college) | -0.3543 | 2.6954 | ±5.3908 | -0.131 | 0.8954 |  |
| Site: UCSD (vs UAB) | +1.8989 | 2.0304 | ±4.0608 | +0.935 | 0.3497 |  |
| Site: UW (vs UAB) | -2.7606 | 1.6811 | ±3.3623 | -1.642 | 0.1006 |  |
| **Age (years)** | **-0.4185** | 0.0717 | ±0.1435 | **-5.835** | **5.39e-09** | *** |
| **BMI (kg/m2)** | **+0.3046** | 0.1092 | ±0.2185 | **+2.789** | **0.0053** | ** |
| Hypertension | +1.1030 | 1.6237 | ±3.2475 | +0.679 | 0.4969 |  |
| High cholesterol | +1.8649 | 1.5169 | ±3.0338 | +1.229 | 0.2189 |  |
| Kidney disease | -2.1747 | 3.1574 | ±6.3147 | -0.689 | 0.4910 |  |
| Circulatory disease | -2.2968 | 1.9477 | ±3.8954 | -1.179 | 0.2383 |  |
| **CV (%)** | **+0.2640** | 0.1275 | ±0.2549 | **+2.071** | **0.0383** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **577**, R² = **0.1308**, Adj R² = **0.1139**, F-statistic = **7.73** (p = **1.60e-12**), Residual SE = **16.767** on **565** df, AIC = **4902.9**, BIC = **4955.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.7535** | 7.0954 | ±14.1908 | **+10.958** | **6.06e-28** | *** |
| Education: graduate level (vs college) | -2.5686 | 1.5327 | ±3.0653 | -1.676 | 0.0938 | . |
| Education: high school or below (vs college) | -0.5556 | 2.6872 | ±5.3744 | -0.207 | 0.8362 |  |
| Site: UCSD (vs UAB) | +1.7838 | 2.0173 | ±4.0346 | +0.884 | 0.3766 |  |
| Site: UW (vs UAB) | -2.8260 | 1.6716 | ±3.3432 | -1.691 | 0.0909 | . |
| **Age (years)** | **-0.4287** | 0.0710 | ±0.1421 | **-6.035** | **1.59e-09** | *** |
| **BMI (kg/m2)** | **+0.2981** | 0.1089 | ±0.2178 | **+2.737** | **0.0062** | ** |
| Hypertension | +1.0605 | 1.6202 | ±3.2405 | +0.655 | 0.5128 |  |
| High cholesterol | +1.8503 | 1.5113 | ±3.0226 | +1.224 | 0.2208 |  |
| Kidney disease | -2.1516 | 3.1047 | ±6.2093 | -0.693 | 0.4883 |  |
| Circulatory disease | -2.3951 | 1.9478 | ±3.8956 | -1.230 | 0.2188 |  |
| **Mean / SD ratio** | **-1.6172** | 0.5458 | ±1.0917 | **-2.963** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **577**, R² = **0.1269**, Adj R² = **0.1099**, F-statistic = **7.46** (p = **4.96e-12**), Residual SE = **16.804** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.9527** | 7.1222 | ±14.2445 | **+10.664** | **1.50e-26** | *** |
| Education: graduate level (vs college) | -2.5633 | 1.5340 | ±3.0680 | -1.671 | 0.0947 | . |
| Education: high school or below (vs college) | -0.4621 | 2.6942 | ±5.3883 | -0.172 | 0.8638 |  |
| Site: UCSD (vs UAB) | +1.6822 | 2.0241 | ±4.0483 | +0.831 | 0.4059 |  |
| Site: UW (vs UAB) | -2.9572 | 1.6783 | ±3.3566 | -1.762 | 0.0781 | . |
| **Age (years)** | **-0.4255** | 0.0717 | ±0.1434 | **-5.934** | **2.95e-09** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.1089 | ±0.2178 | **+2.717** | **0.0066** | ** |
| Hypertension | +1.1833 | 1.6216 | ±3.2431 | +0.730 | 0.4655 |  |
| High cholesterol | +1.8060 | 1.5157 | ±3.0313 | +1.192 | 0.2334 |  |
| Kidney disease | -1.8449 | 3.1107 | ±6.2213 | -0.593 | 0.5531 |  |
| Circulatory disease | -2.3510 | 1.9507 | ±3.9015 | -1.205 | 0.2281 |  |
| **Avg. daily mean/SD** | **-1.1019** | 0.4515 | ±0.9030 | **-2.440** | **0.0147** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **577**, R² = **0.1201**, Adj R² = **0.1029**, F-statistic = **7.01** (p = **3.51e-11**), Residual SE = **16.870** on **565** df, AIC = **4910.0**, BIC = **4962.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8320** | 6.5570 | ±13.1139 | **+9.735** | **2.14e-22** | *** |
| Education: graduate level (vs college) | -2.5748 | 1.5386 | ±3.0772 | -1.673 | 0.0942 | . |
| Education: high school or below (vs college) | +0.1266 | 2.6900 | ±5.3800 | +0.047 | 0.9625 |  |
| Site: UCSD (vs UAB) | +1.8272 | 2.0445 | ±4.0891 | +0.894 | 0.3715 |  |
| Site: UW (vs UAB) | -2.9090 | 1.6907 | ±3.3814 | -1.721 | 0.0853 | . |
| **Age (years)** | **-0.3934** | 0.0704 | ±0.1408 | **-5.587** | **2.31e-08** | *** |
| **BMI (kg/m2)** | **+0.2938** | 0.1099 | ±0.2198 | **+2.673** | **0.0075** | ** |
| Hypertension | +1.2549 | 1.6284 | ±3.2569 | +0.771 | 0.4409 |  |
| High cholesterol | +1.8884 | 1.5191 | ±3.0381 | +1.243 | 0.2138 |  |
| Kidney disease | -1.1028 | 3.0979 | ±6.1957 | -0.356 | 0.7219 |  |
| Circulatory disease | -2.4173 | 1.9547 | ±3.9093 | -1.237 | 0.2162 |  |
| MAG (mg/dL/h) | +0.0817 | 0.0773 | ±0.1547 | +1.056 | 0.2909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **577**, R² = **0.1247**, Adj R² = **0.1077**, F-statistic = **7.32** (p = **9.26e-12**), Residual SE = **16.825** on **565** df, AIC = **4906.9**, BIC = **4959.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.6845** | 6.2572 | ±12.5144 | **+10.178** | **2.49e-24** | *** |
| Education: graduate level (vs college) | -2.4570 | 1.5396 | ±3.0791 | -1.596 | 0.1105 |  |
| Education: high school or below (vs college) | -0.4404 | 2.7068 | ±5.4137 | -0.163 | 0.8708 |  |
| Site: UCSD (vs UAB) | +1.7971 | 2.0338 | ±4.0676 | +0.884 | 0.3769 |  |
| Site: UW (vs UAB) | -2.8984 | 1.6809 | ±3.3617 | -1.724 | 0.0846 | . |
| **Age (years)** | **-0.4100** | 0.0716 | ±0.1432 | **-5.725** | **1.03e-08** | *** |
| **BMI (kg/m2)** | **+0.3061** | 0.1094 | ±0.2188 | **+2.797** | **0.0052** | ** |
| Hypertension | +1.0779 | 1.6289 | ±3.2578 | +0.662 | 0.5081 |  |
| High cholesterol | +1.7485 | 1.5221 | ±3.0443 | +1.149 | 0.2507 |  |
| Kidney disease | -1.9943 | 3.1209 | ±6.2419 | -0.639 | 0.5228 |  |
| Circulatory disease | -2.3790 | 1.9592 | ±3.9184 | -1.214 | 0.2247 |  |
| Avg. daily range (mg/dL) | +0.0388 | 0.0208 | ±0.0415 | +1.870 | 0.0614 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **577**, R² = **0.1285**, Adj R² = **0.1116**, F-statistic = **7.58** (p = **3.07e-12**), Residual SE = **16.788** on **565** df, AIC = **4904.4**, BIC = **4956.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.3320** | 6.1323 | ±12.2645 | **+10.654** | **1.67e-26** | *** |
| Education: graduate level (vs college) | -2.4670 | 1.5425 | ±3.0850 | -1.599 | 0.1097 |  |
| Education: high school or below (vs college) | +0.0762 | 2.6548 | ±5.3096 | +0.029 | 0.9771 |  |
| Site: UCSD (vs UAB) | +2.0249 | 2.0249 | ±4.0498 | +1.000 | 0.3173 |  |
| Site: UW (vs UAB) | -2.8182 | 1.6733 | ±3.3467 | -1.684 | 0.0921 | . |
| **Age (years)** | **-0.4005** | 0.0701 | ±0.1402 | **-5.713** | **1.11e-08** | *** |
| **BMI (kg/m2)** | **+0.2958** | 0.1091 | ±0.2183 | **+2.710** | **0.0067** | ** |
| Hypertension | +0.9111 | 1.6324 | ±3.2647 | +0.558 | 0.5767 |  |
| High cholesterol | +1.7960 | 1.5128 | ±3.0257 | +1.187 | 0.2352 |  |
| Kidney disease | -1.7717 | 3.0330 | ±6.0660 | -0.584 | 0.5591 |  |
| Circulatory disease | -2.5678 | 1.9533 | ±3.9065 | -1.315 | 0.1886 |  |
| **SD of daily means (mg/dL)** | **+0.2670** | 0.0996 | ±0.1991 | **+2.682** | **0.0073** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **577**, R² = **0.1268**, Adj R² = **0.1098**, F-statistic = **7.46** (p = **5.15e-12**), Residual SE = **16.805** on **565** df, AIC = **4905.6**, BIC = **4957.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.5721** | 8.4500 | ±16.8999 | **+9.417** | **4.65e-21** | *** |
| Education: graduate level (vs college) | -2.4035 | 1.5507 | ±3.1014 | -1.550 | 0.1212 |  |
| Education: high school or below (vs college) | -0.1632 | 2.6421 | ±5.2842 | -0.062 | 0.9508 |  |
| Site: UCSD (vs UAB) | +2.0145 | 2.0302 | ±4.0603 | +0.992 | 0.3211 |  |
| Site: UW (vs UAB) | -2.7513 | 1.6832 | ±3.3664 | -1.635 | 0.1021 |  |
| **Age (years)** | **-0.4009** | 0.0700 | ±0.1400 | **-5.725** | **1.03e-08** | *** |
| **BMI (kg/m2)** | **+0.2955** | 0.1087 | ±0.2175 | **+2.718** | **0.0066** | ** |
| Hypertension | +1.0503 | 1.6358 | ±3.2716 | +0.642 | 0.5208 |  |
| High cholesterol | +1.6705 | 1.5193 | ±3.0386 | +1.100 | 0.2715 |  |
| Kidney disease | -1.9233 | 3.0320 | ±6.0640 | -0.634 | 0.5259 |  |
| Circulatory disease | -2.4777 | 1.9602 | ±3.9205 | -1.264 | 0.2062 |  |
| **Time in range 70-180, pooled (%)** | **-0.1294** | 0.0622 | ±0.1244 | **-2.080** | **0.0375** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **577**, R² = **0.1263**, Adj R² = **0.1093**, F-statistic = **7.43** (p = **5.83e-12**), Residual SE = **16.809** on **565** df, AIC = **4905.9**, BIC = **4958.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.2752** | 8.3821 | ±16.7643 | **+9.458** | **3.15e-21** | *** |
| Education: graduate level (vs college) | -2.4031 | 1.5530 | ±3.1059 | -1.547 | 0.1218 |  |
| Education: high school or below (vs college) | -0.1707 | 2.6439 | ±5.2878 | -0.065 | 0.9485 |  |
| Site: UCSD (vs UAB) | +2.0112 | 2.0307 | ±4.0614 | +0.990 | 0.3220 |  |
| Site: UW (vs UAB) | -2.7553 | 1.6842 | ±3.3684 | -1.636 | 0.1018 |  |
| **Age (years)** | **-0.4013** | 0.0701 | ±0.1402 | **-5.727** | **1.02e-08** | *** |
| **BMI (kg/m2)** | **+0.2958** | 0.1089 | ±0.2178 | **+2.717** | **0.0066** | ** |
| Hypertension | +1.0666 | 1.6366 | ±3.2731 | +0.652 | 0.5146 |  |
| High cholesterol | +1.6636 | 1.5190 | ±3.0380 | +1.095 | 0.2734 |  |
| Kidney disease | -1.9085 | 3.0361 | ±6.0722 | -0.629 | 0.5296 |  |
| Circulatory disease | -2.4785 | 1.9619 | ±3.9238 | -1.263 | 0.2065 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.1255** | 0.0610 | ±0.1219 | **-2.058** | **0.0396** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **577**, R² = **0.1183**, Adj R² = **0.1012**, F-statistic = **6.89** (p = **5.74e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9667** | 6.1116 | ±12.2231 | **+10.957** | **6.13e-28** | *** |
| Education: graduate level (vs college) | -2.6113 | 1.5396 | ±3.0792 | -1.696 | 0.0899 | . |
| Education: high school or below (vs college) | +0.3976 | 2.6685 | ±5.3370 | +0.149 | 0.8816 |  |
| Site: UCSD (vs UAB) | +2.0160 | 2.0612 | ±4.1224 | +0.978 | 0.3280 |  |
| Site: UW (vs UAB) | -3.0659 | 1.6920 | ±3.3839 | -1.812 | 0.0700 | . |
| **Age (years)** | **-0.3934** | 0.0705 | ±0.1409 | **-5.583** | **2.36e-08** | *** |
| **BMI (kg/m2)** | **+0.2977** | 0.1098 | ±0.2196 | **+2.712** | **0.0067** | ** |
| Hypertension | +1.3504 | 1.6261 | ±3.2522 | +0.830 | 0.4063 |  |
| High cholesterol | +1.8834 | 1.5170 | ±3.0340 | +1.241 | 0.2144 |  |
| Kidney disease | -1.0014 | 3.0888 | ±6.1777 | -0.324 | 0.7458 |  |
| Circulatory disease | -2.4545 | 1.9508 | ±3.9015 | -1.258 | 0.2083 |  |
| Time < 54 (%) | +0.2018 | 0.8937 | ±1.7874 | +0.226 | 0.8214 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **577**, R² = **0.1182**, Adj R² = **0.1011**, F-statistic = **6.89** (p = **5.90e-11**), Residual SE = **16.887** on **565** df, AIC = **4911.2**, BIC = **4963.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1372** | 6.0931 | ±12.1861 | **+11.019** | **3.11e-28** | *** |
| Education: graduate level (vs college) | -2.6259 | 1.5393 | ±3.0786 | -1.706 | 0.0880 | . |
| Education: high school or below (vs college) | +0.3608 | 2.6701 | ±5.3402 | +0.135 | 0.8925 |  |
| Site: UCSD (vs UAB) | +1.9354 | 2.0594 | ±4.1189 | +0.940 | 0.3473 |  |
| Site: UW (vs UAB) | -3.1372 | 1.6942 | ±3.3883 | -1.852 | 0.0641 | . |
| **Age (years)** | **-0.3930** | 0.0707 | ±0.1414 | **-5.558** | **2.72e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1098 | ±0.2196 | **+2.705** | **0.0068** | ** |
| Hypertension | +1.3301 | 1.6270 | ±3.2539 | +0.818 | 0.4136 |  |
| High cholesterol | +1.8500 | 1.5205 | ±3.0411 | +1.217 | 0.2237 |  |
| Kidney disease | -0.9849 | 3.0931 | ±6.1862 | -0.318 | 0.7502 |  |
| Circulatory disease | -2.4498 | 1.9559 | ±3.9118 | -1.253 | 0.2104 |  |
| Avg. daily time < 54 (%) | -0.0518 | 1.0308 | ±2.0615 | -0.050 | 0.9599 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **577**, R² = **0.1183**, Adj R² = **0.1011**, F-statistic = **6.89** (p = **5.80e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2289** | 6.1373 | ±12.2745 | **+10.954** | **6.34e-28** | *** |
| Education: graduate level (vs college) | -2.6428 | 1.5418 | ±3.0835 | -1.714 | 0.0865 | . |
| Education: high school or below (vs college) | +0.3673 | 2.6682 | ±5.3364 | +0.138 | 0.8905 |  |
| Site: UCSD (vs UAB) | +1.9156 | 2.0600 | ±4.1200 | +0.930 | 0.3524 |  |
| Site: UW (vs UAB) | -3.1595 | 1.6884 | ±3.3768 | -1.871 | 0.0613 | . |
| **Age (years)** | **-0.3926** | 0.0703 | ±0.1407 | **-5.581** | **2.39e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1098 | ±0.2195 | **+2.706** | **0.0068** | ** |
| Hypertension | +1.3173 | 1.6235 | ±3.2470 | +0.811 | 0.4171 |  |
| High cholesterol | +1.8446 | 1.5168 | ±3.0335 | +1.216 | 0.2239 |  |
| Kidney disease | -0.9764 | 3.0919 | ±6.1838 | -0.316 | 0.7522 |  |
| Circulatory disease | -2.4607 | 1.9560 | ±3.9120 | -1.258 | 0.2084 |  |
| Time 54-69, pooled (%) | -0.0625 | 0.3208 | ±0.6415 | -0.195 | 0.8456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **577**, R² = **0.1184**, Adj R² = **0.1012**, F-statistic = **6.90** (p = **5.65e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2402** | 6.1174 | ±12.2349 | **+10.992** | **4.20e-28** | *** |
| Education: graduate level (vs college) | -2.6567 | 1.5436 | ±3.0872 | -1.721 | 0.0852 | . |
| Education: high school or below (vs college) | +0.3687 | 2.6679 | ±5.3357 | +0.138 | 0.8901 |  |
| Site: UCSD (vs UAB) | +1.9042 | 2.0587 | ±4.1173 | +0.925 | 0.3550 |  |
| Site: UW (vs UAB) | -3.1828 | 1.6867 | ±3.3735 | -1.887 | 0.0592 | . |
| **Age (years)** | **-0.3919** | 0.0704 | ±0.1408 | **-5.567** | **2.59e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1098 | ±0.2196 | **+2.706** | **0.0068** | ** |
| Hypertension | +1.3098 | 1.6242 | ±3.2484 | +0.806 | 0.4200 |  |
| High cholesterol | +1.8398 | 1.5164 | ±3.0328 | +1.213 | 0.2250 |  |
| Kidney disease | -0.9699 | 3.0904 | ±6.1807 | -0.314 | 0.7536 |  |
| Circulatory disease | -2.4653 | 1.9565 | ±3.9131 | -1.260 | 0.2077 |  |
| Avg. daily time 54-69 (%) | -0.0935 | 0.3196 | ±0.6392 | -0.293 | 0.7699 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **577**, R² = **0.1183**, Adj R² = **0.1011**, F-statistic = **6.89** (p = **5.89e-11**), Residual SE = **16.887** on **565** df, AIC = **4911.2**, BIC = **4963.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1714** | 6.1404 | ±12.2808 | **+10.939** | **7.48e-28** | *** |
| Education: graduate level (vs college) | -2.6296 | 1.5402 | ±3.0804 | -1.707 | 0.0878 | . |
| Education: high school or below (vs college) | +0.3645 | 2.6678 | ±5.3357 | +0.137 | 0.8913 |  |
| Site: UCSD (vs UAB) | +1.9303 | 2.0638 | ±4.1276 | +0.935 | 0.3496 |  |
| Site: UW (vs UAB) | -3.1413 | 1.6920 | ±3.3840 | -1.857 | 0.0634 | . |
| **Age (years)** | **-0.3930** | 0.0704 | ±0.1407 | **-5.584** | **2.35e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1097 | ±0.2195 | **+2.707** | **0.0068** | ** |
| Hypertension | +1.3266 | 1.6241 | ±3.2482 | +0.817 | 0.4140 |  |
| High cholesterol | +1.8496 | 1.5166 | ±3.0333 | +1.220 | 0.2226 |  |
| Kidney disease | -0.9834 | 3.0931 | ±6.1862 | -0.318 | 0.7505 |  |
| Circulatory disease | -2.4539 | 1.9554 | ±3.9108 | -1.255 | 0.2095 |  |
| Time < 70 (%) | -0.0209 | 0.2550 | ±0.5101 | -0.082 | 0.9348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **577**, R² = **0.1184**, Adj R² = **0.1012**, F-statistic = **6.90** (p = **5.71e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2293** | 6.1129 | ±12.2258 | **+10.998** | **3.91e-28** | *** |
| Education: graduate level (vs college) | -2.6524 | 1.5426 | ±3.0852 | -1.719 | 0.0855 | . |
| Education: high school or below (vs college) | +0.3596 | 2.6673 | ±5.3346 | +0.135 | 0.8928 |  |
| Site: UCSD (vs UAB) | +1.9001 | 2.0607 | ±4.1213 | +0.922 | 0.3565 |  |
| Site: UW (vs UAB) | -3.1839 | 1.6899 | ±3.3798 | -1.884 | 0.0596 | . |
| **Age (years)** | **-0.3920** | 0.0705 | ±0.1409 | **-5.562** | **2.66e-08** | *** |
| **BMI (kg/m2)** | **+0.2970** | 0.1098 | ±0.2196 | **+2.705** | **0.0068** | ** |
| Hypertension | +1.3118 | 1.6247 | ±3.2494 | +0.807 | 0.4194 |  |
| High cholesterol | +1.8362 | 1.5165 | ±3.0330 | +1.211 | 0.2260 |  |
| Kidney disease | -0.9702 | 3.0920 | ±6.1839 | -0.314 | 0.7537 |  |
| Circulatory disease | -2.4596 | 1.9573 | ±3.9146 | -1.257 | 0.2089 |  |
| Avg. daily time < 70 (%) | -0.0670 | 0.2674 | ±0.5347 | -0.251 | 0.8021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **577**, R² = **0.1192**, Adj R² = **0.1021**, F-statistic = **6.95** (p = **4.49e-11**), Residual SE = **16.878** on **565** df, AIC = **4910.5**, BIC = **4962.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2986** | 17.2109 | ±34.4218 | **+4.433** | **9.29e-06** | *** |
| Education: graduate level (vs college) | -2.5597 | 1.5456 | ±3.0912 | -1.656 | 0.0977 | . |
| Education: high school or below (vs college) | +0.1965 | 2.6813 | ±5.3626 | +0.073 | 0.9416 |  |
| Site: UCSD (vs UAB) | +1.9861 | 2.0453 | ±4.0906 | +0.971 | 0.3315 |  |
| Site: UW (vs UAB) | -2.9989 | 1.6908 | ±3.3815 | -1.774 | 0.0761 | . |
| **Age (years)** | **-0.3928** | 0.0703 | ±0.1406 | **-5.589** | **2.28e-08** | *** |
| **BMI (kg/m2)** | **+0.2981** | 0.1095 | ±0.2191 | **+2.722** | **0.0065** | ** |
| Hypertension | +1.2628 | 1.6298 | ±3.2596 | +0.775 | 0.4384 |  |
| High cholesterol | +1.8853 | 1.5220 | ±3.0439 | +1.239 | 0.2154 |  |
| Kidney disease | -1.1494 | 3.0905 | ±6.1809 | -0.372 | 0.7100 |  |
| Circulatory disease | -2.4875 | 1.9649 | ±3.9299 | -1.266 | 0.2055 |  |
| Time 54-250, pooled (%) | -0.0942 | 0.1636 | ±0.3271 | -0.576 | 0.5648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **577**, R² = **0.1197**, Adj R² = **0.1026**, F-statistic = **6.99** (p = **3.86e-11**), Residual SE = **16.873** on **565** df, AIC = **4910.2**, BIC = **4962.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.8329** | 19.7415 | ±39.4830 | **+4.044** | **5.26e-05** | *** |
| Education: graduate level (vs college) | -2.5349 | 1.5473 | ±3.0945 | -1.638 | 0.1014 |  |
| Education: high school or below (vs college) | +0.1224 | 2.6912 | ±5.3824 | +0.045 | 0.9637 |  |
| Site: UCSD (vs UAB) | +1.9782 | 2.0451 | ±4.0901 | +0.967 | 0.3334 |  |
| Site: UW (vs UAB) | -2.9742 | 1.6898 | ±3.3797 | -1.760 | 0.0784 | . |
| **Age (years)** | **-0.3936** | 0.0703 | ±0.1405 | **-5.601** | **2.13e-08** | *** |
| **BMI (kg/m2)** | **+0.2989** | 0.1095 | ±0.2190 | **+2.730** | **0.0063** | ** |
| Hypertension | +1.2435 | 1.6300 | ±3.2600 | +0.763 | 0.4455 |  |
| High cholesterol | +1.8871 | 1.5224 | ±3.0448 | +1.240 | 0.2151 |  |
| Kidney disease | -1.2228 | 3.0951 | ±6.1902 | -0.395 | 0.6928 |  |
| Circulatory disease | -2.5068 | 1.9683 | ±3.9366 | -1.274 | 0.2028 |  |
| Avg. daily time 54-250 (%) | -0.1295 | 0.1898 | ±0.3796 | -0.682 | 0.4949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **577**, R² = **0.1317**, Adj R² = **0.1148**, F-statistic = **7.79** (p = **1.23e-12**), Residual SE = **16.758** on **565** df, AIC = **4902.3**, BIC = **4954.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2409** | 6.0543 | ±12.1087 | **+11.106** | **1.17e-28** | *** |
| Education: graduate level (vs college) | -2.4586 | 1.5454 | ±3.0908 | -1.591 | 0.1116 |  |
| Education: high school or below (vs college) | -0.1757 | 2.6325 | ±5.2650 | -0.067 | 0.9468 |  |
| Site: UCSD (vs UAB) | +1.8504 | 2.0269 | ±4.0539 | +0.913 | 0.3613 |  |
| Site: UW (vs UAB) | -2.8922 | 1.6726 | ±3.3452 | -1.729 | 0.0838 | . |
| **Age (years)** | **-0.4061** | 0.0701 | ±0.1402 | **-5.792** | **6.96e-09** | *** |
| **BMI (kg/m2)** | **+0.2913** | 0.1086 | ±0.2172 | **+2.683** | **0.0073** | ** |
| Hypertension | +0.9300 | 1.6440 | ±3.2880 | +0.566 | 0.5716 |  |
| High cholesterol | +1.3983 | 1.5040 | ±3.0079 | +0.930 | 0.3525 |  |
| Kidney disease | -2.2503 | 2.9909 | ±5.9819 | -0.752 | 0.4518 |  |
| Circulatory disease | -2.4448 | 1.9567 | ±3.9133 | -1.249 | 0.2115 |  |
| **Time 181-250, pooled (%)** | **+0.2372** | 0.0885 | ±0.1769 | **+2.682** | **0.0073** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **577**, R² = **0.1300**, Adj R² = **0.1131**, F-statistic = **7.68** (p = **1.99e-12**), Residual SE = **16.774** on **565** df, AIC = **4903.4**, BIC = **4955.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1285** | 6.0604 | ±12.1208 | **+11.077** | **1.63e-28** | *** |
| Education: graduate level (vs college) | -2.4714 | 1.5479 | ±3.0958 | -1.597 | 0.1103 |  |
| Education: high school or below (vs college) | -0.1471 | 2.6344 | ±5.2687 | -0.056 | 0.9555 |  |
| Site: UCSD (vs UAB) | +1.9050 | 2.0286 | ±4.0572 | +0.939 | 0.3477 |  |
| Site: UW (vs UAB) | -2.8761 | 1.6756 | ±3.3513 | -1.716 | 0.0861 | . |
| **Age (years)** | **-0.4036** | 0.0701 | ±0.1402 | **-5.757** | **8.57e-09** | *** |
| **BMI (kg/m2)** | **+0.2916** | 0.1087 | ±0.2175 | **+2.682** | **0.0073** | ** |
| Hypertension | +0.9692 | 1.6445 | ±3.2891 | +0.589 | 0.5556 |  |
| High cholesterol | +1.4354 | 1.5054 | ±3.0108 | +0.954 | 0.3403 |  |
| Kidney disease | -2.1369 | 3.0012 | ±6.0024 | -0.712 | 0.4765 |  |
| Circulatory disease | -2.4382 | 1.9601 | ±3.9203 | -1.244 | 0.2135 |  |
| **Avg. daily time 181-250 (%)** | **+0.2157** | 0.0862 | ±0.1725 | **+2.502** | **0.0124** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **577**, R² = **0.1269**, Adj R² = **0.1099**, F-statistic = **7.46** (p = **4.98e-12**), Residual SE = **16.804** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9571** | 6.0581 | ±12.1163 | **+11.052** | **2.13e-28** | *** |
| Education: graduate level (vs college) | -2.4532 | 1.5475 | ±3.0950 | -1.585 | 0.1129 |  |
| Education: high school or below (vs college) | -0.1864 | 2.6413 | ±5.2827 | -0.071 | 0.9438 |  |
| Site: UCSD (vs UAB) | +1.9032 | 2.0336 | ±4.0673 | +0.936 | 0.3493 |  |
| Site: UW (vs UAB) | -2.8615 | 1.6783 | ±3.3565 | -1.705 | 0.0882 | . |
| **Age (years)** | **-0.3997** | 0.0700 | ±0.1400 | **-5.711** | **1.12e-08** | *** |
| **BMI (kg/m2)** | **+0.2949** | 0.1089 | ±0.2178 | **+2.709** | **0.0068** | ** |
| Hypertension | +1.0033 | 1.6391 | ±3.2782 | +0.612 | 0.5405 |  |
| High cholesterol | +1.6276 | 1.5185 | ±3.0370 | +1.072 | 0.2838 |  |
| Kidney disease | -1.8949 | 3.0266 | ±6.0531 | -0.626 | 0.5313 |  |
| Circulatory disease | -2.4958 | 1.9661 | ±3.9321 | -1.269 | 0.2043 |  |
| **Time > 180 (%)** | **+0.1302** | 0.0622 | ±0.1244 | **+2.093** | **0.0363** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **577**, R² = **0.1269**, Adj R² = **0.1099**, F-statistic = **7.46** (p = **4.97e-12**), Residual SE = **16.804** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9282** | 6.0649 | ±12.1298 | **+11.035** | **2.58e-28** | *** |
| Education: graduate level (vs college) | -2.4548 | 1.5490 | ±3.0981 | -1.585 | 0.1130 |  |
| Education: high school or below (vs college) | -0.2079 | 2.6416 | ±5.2831 | -0.079 | 0.9373 |  |
| Site: UCSD (vs UAB) | +1.9200 | 2.0331 | ±4.0663 | +0.944 | 0.3450 |  |
| Site: UW (vs UAB) | -2.8588 | 1.6794 | ±3.3587 | -1.702 | 0.0887 | . |
| **Age (years)** | **-0.3993** | 0.0700 | ±0.1400 | **-5.704** | **1.17e-08** | *** |
| **BMI (kg/m2)** | **+0.2954** | 0.1090 | ±0.2179 | **+2.711** | **0.0067** | ** |
| Hypertension | +1.0130 | 1.6401 | ±3.2801 | +0.618 | 0.5368 |  |
| High cholesterol | +1.6168 | 1.5171 | ±3.0341 | +1.066 | 0.2865 |  |
| Kidney disease | -1.9087 | 3.0267 | ±6.0535 | -0.631 | 0.5283 |  |
| Circulatory disease | -2.4962 | 1.9677 | ±3.9354 | -1.269 | 0.2046 |  |
| **Avg. daily time > 180 (%)** | **+0.1304** | 0.0613 | ±0.1225 | **+2.129** | **0.0332** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **577**, R² = **0.1216**, Adj R² = **0.1045**, F-statistic = **7.11** (p = **2.28e-11**), Residual SE = **16.855** on **565** df, AIC = **4909.0**, BIC = **4961.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.0539** | 6.0840 | ±12.1679 | **+11.021** | **3.01e-28** | *** |
| Education: graduate level (vs college) | -2.5095 | 1.5507 | ±3.1013 | -1.618 | 0.1056 |  |
| Education: high school or below (vs college) | +0.1411 | 2.6404 | ±5.2807 | +0.053 | 0.9574 |  |
| Site: UCSD (vs UAB) | +1.9544 | 2.0429 | ±4.0859 | +0.957 | 0.3387 |  |
| Site: UW (vs UAB) | -2.9919 | 1.6833 | ±3.3666 | -1.777 | 0.0755 | . |
| **Age (years)** | **-0.3936** | 0.0703 | ±0.1405 | **-5.602** | **2.11e-08** | *** |
| **BMI (kg/m2)** | **+0.2919** | 0.1092 | ±0.2184 | **+2.673** | **0.0075** | ** |
| Hypertension | +1.1056 | 1.6414 | ±3.2827 | +0.674 | 0.5006 |  |
| High cholesterol | +1.7325 | 1.5193 | ±3.0385 | +1.140 | 0.2541 |  |
| Kidney disease | -1.2561 | 3.0451 | ±6.0902 | -0.413 | 0.6800 |  |
| Circulatory disease | -2.5142 | 1.9624 | ±3.9249 | -1.281 | 0.2001 |  |
| Nocturnal time > 180 (%) | +0.0833 | 0.0602 | ±0.1203 | +1.385 | 0.1662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **577**, R² = **0.1248**, Adj R² = **0.1078**, F-statistic = **7.33** (p = **8.95e-12**), Residual SE = **16.824** on **565** df, AIC = **4906.8**, BIC = **4959.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9319** | 6.0420 | ±12.0840 | **+11.078** | **1.61e-28** | *** |
| Education: graduate level (vs college) | -2.4276 | 1.5383 | ±3.0767 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +0.0189 | 2.6843 | ±5.3685 | +0.007 | 0.9944 |  |
| Site: UCSD (vs UAB) | +1.7439 | 2.0350 | ±4.0700 | +0.857 | 0.3915 |  |
| Site: UW (vs UAB) | -3.0237 | 1.6743 | ±3.3486 | -1.806 | 0.0709 | . |
| **Age (years)** | **-0.4072** | 0.0708 | ±0.1415 | **-5.754** | **8.73e-09** | *** |
| **BMI (kg/m2)** | **+0.3074** | 0.1088 | ±0.2176 | **+2.825** | **0.0047** | ** |
| Hypertension | +1.0146 | 1.6249 | ±3.2499 | +0.624 | 0.5324 |  |
| High cholesterol | +1.6631 | 1.5195 | ±3.0389 | +1.095 | 0.2737 |  |
| Kidney disease | -1.7649 | 3.0829 | ±6.1659 | -0.572 | 0.5670 |  |
| Circulatory disease | -2.3641 | 1.9580 | ±3.9159 | -1.207 | 0.2273 |  |
| **Any reading > 250 during wear (0/1)** | **+3.3430** | 1.6438 | ±3.2877 | **+2.034** | **0.0420** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **577**, R² = **0.1191**, Adj R² = **0.1020**, F-statistic = **6.95** (p = **4.58e-11**), Residual SE = **16.879** on **565** df, AIC = **4910.6**, BIC = **4962.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9571** | 6.0821 | ±12.1641 | **+11.009** | **3.46e-28** | *** |
| Education: graduate level (vs college) | -2.5657 | 1.5457 | ±3.0915 | -1.660 | 0.0969 | . |
| Education: high school or below (vs college) | +0.1866 | 2.6865 | ±5.3729 | +0.069 | 0.9446 |  |
| Site: UCSD (vs UAB) | +1.9543 | 2.0480 | ±4.0960 | +0.954 | 0.3400 |  |
| Site: UW (vs UAB) | -3.0278 | 1.6875 | ±3.3749 | -1.794 | 0.0728 | . |
| **Age (years)** | **-0.3927** | 0.0703 | ±0.1405 | **-5.589** | **2.28e-08** | *** |
| **BMI (kg/m2)** | **+0.2979** | 0.1095 | ±0.2191 | **+2.719** | **0.0065** | ** |
| Hypertension | +1.2568 | 1.6308 | ±3.2616 | +0.771 | 0.4409 |  |
| High cholesterol | +1.8723 | 1.5229 | ±3.0457 | +1.229 | 0.2189 |  |
| Kidney disease | -1.1401 | 3.0897 | ±6.1794 | -0.369 | 0.7121 |  |
| Circulatory disease | -2.4852 | 1.9666 | ±3.9332 | -1.264 | 0.2063 |  |
| Time > 250 (%) | +0.0921 | 0.1667 | ±0.3334 | +0.552 | 0.5806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **577**, R² = **0.1198**, Adj R² = **0.1027**, F-statistic = **6.99** (p = **3.77e-11**), Residual SE = **16.872** on **565** df, AIC = **4910.1**, BIC = **4962.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9147** | 6.0834 | ±12.1668 | **+11.000** | **3.84e-28** | *** |
| Education: graduate level (vs college) | -2.5425 | 1.5466 | ±3.0931 | -1.644 | 0.1002 |  |
| Education: high school or below (vs college) | +0.0930 | 2.7010 | ±5.4021 | +0.034 | 0.9725 |  |
| Site: UCSD (vs UAB) | +1.9461 | 2.0486 | ±4.0971 | +0.950 | 0.3421 |  |
| Site: UW (vs UAB) | -3.0037 | 1.6865 | ±3.3730 | -1.781 | 0.0749 | . |
| **Age (years)** | **-0.3930** | 0.0702 | ±0.1405 | **-5.595** | **2.20e-08** | *** |
| **BMI (kg/m2)** | **+0.2988** | 0.1095 | ±0.2190 | **+2.729** | **0.0064** | ** |
| Hypertension | +1.2296 | 1.6307 | ±3.2614 | +0.754 | 0.4508 |  |
| High cholesterol | +1.8719 | 1.5237 | ±3.0475 | +1.228 | 0.2193 |  |
| Kidney disease | -1.2234 | 3.0940 | ±6.1881 | -0.395 | 0.6925 |  |
| Circulatory disease | -2.5060 | 1.9711 | ±3.9423 | -1.271 | 0.2036 |  |
| Avg. daily time > 250 (%) | +0.1356 | 0.1991 | ±0.3981 | +0.681 | 0.4959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 150 single-predictor tests; 45 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 150 tests (samples with n >= 500), of which **12** are significant at BH q < 0.05 in the all-tests family and 20 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 575): best single predictor out of sample is **HbA1c** (CV R² 0.126 vs 0.124 for covariates alone, gain +0.001; +312 per SD, p = 0.217, q = 0.425). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 575): best single predictor out of sample is **HbA1c** (CV R² 0.147 vs 0.141 for covariates alone, gain +0.006; +1.24 per SD, p = 0.096, q = 0.233). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 576): best single predictor out of sample is **Mean/SD** (CV R² 0.155 vs 0.144 for covariates alone, gain +0.010; -1.07 per SD, p = 0.001, q = 0.023). FDR-robust associations (5): Mean/SD (lower outcome, -1.07 per SD, q = 0.023); %181-250 (pooled) (higher outcome, +1.19 per SD, q = 0.028); SD of daily means (higher outcome, +0.979 per SD, q = 0.029); Mean/SD (daily avg) (lower outcome, -0.962 per SD, q = 0.032); %181-250 (daily avg) (higher outcome, +1.11 per SD, q = 0.042).
- **Total sleep time per night (min)** (n = 588): best single predictor out of sample is **MAG** (CV R² 0.004 vs -0.017 for covariates alone, gain +0.021; -12.1 per SD, p = 2.3e-05, q = 0.002). FDR-robust associations (4): MAG (lower outcome, -12.1 per SD, q = 0.002); HbA1c (lower outcome, -8.46 per SD, q = 0.023); %54-250 (daily avg) (higher outcome, +7.03 per SD, q = 0.036); %>250 (daily avg) (lower outcome, -7.14 per SD, q = 0.036).
- **Garmin stress score, mean (0-100)** (n = 577): best single predictor out of sample is **HbA1c** (CV R² 0.095 vs 0.086 for covariates alone, gain +0.009; +2.28 per SD, p = 0.014, q = 0.071). FDR-robust associations (3): Mean/SD (lower outcome, -2.11 per SD, q = 0.029); SD of daily means (higher outcome, +1.87 per SD, q = 0.047); %181-250 (pooled) (higher outcome, +2.17 per SD, q = 0.047).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.021, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.010, via Mean/SD); Garmin stress score, mean (0-100) (+0.009, via HbA1c); Brisk-cadence minutes per day (>= 100 steps/min) (+0.006, via HbA1c). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (6 FDR-significant / 13 raw-significant of 40); Band 181-250 (3 FDR-significant / 4 raw-significant of 10); Band > 250 (1 FDR-significant / 4 raw-significant of 15).
Level metrics: 0 FDR-significant (8 raw); variability metrics: 6 FDR-significant (13 raw); HbA1c alone: 1 FDR-significant (3 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Total sleep time per night (MAG, ΔAIC -10.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
