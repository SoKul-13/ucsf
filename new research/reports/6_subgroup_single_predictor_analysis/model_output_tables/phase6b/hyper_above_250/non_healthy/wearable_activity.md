# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


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


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 150 single-predictor tests; 36 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 472): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.136 vs 0.131 for covariates alone, gain +0.005; -484 per SD, p = 0.010). Raw p < 0.05 (FDR not applicable here): %<54 (daily avg) (p = 2.2e-06), %<54 (pooled) (p = 7.3e-04), %<70 (daily avg) (p = 0.010), %<70 (pooled) (p = 0.047).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 472): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.150 vs 0.146 for covariates alone, gain +0.004; -1.1 per SD, p = 6.4e-07). Raw p < 0.05 (FDR not applicable here): %<54 (daily avg) (p = 6.4e-07), %<54 (pooled) (p = 0.008), %<70 (daily avg) (p = 0.035).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 474): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.131 vs 0.123 for covariates alone, gain +0.008; +1.1 per SD, p = 0.004). Raw p < 0.05 (FDR not applicable here): %181-250 (pooled) (p = 0.004), %181-250 (daily avg) (p = 0.005), %>180 (daily avg) (p = 0.005), %>180 (pooled) (p = 0.005), TIR 70-180 (pooled) (p = 0.006).
- **Total sleep time per night (min)** (n = 479): best single predictor out of sample is **MAG** (CV R² -0.007 vs -0.018 for covariates alone, gain +0.011; -7.92 per SD, p = 0.009). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.009).
- **Garmin stress score, mean (0-100)** (n = 474): best single predictor out of sample is **%>180 (pooled)** (CV R² 0.109 vs 0.090 for covariates alone, gain +0.020; +2.8 per SD, p = 9.0e-04). Raw p < 0.05 (FDR not applicable here): %>180 (pooled) (p = 9.0e-04), %>180 (daily avg) (p = 0.001), TIR 70-180 (pooled) (p = 0.001), TIR 70-180 (daily avg) (p = 0.001), HbA1c (p = 0.002).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Garmin stress score, mean (0-100) (+0.020, via %>180 (pooled)); Total sleep time per night (min) (+0.011, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.008, via %181-250 (pooled)); Steps per wear-day (+0.005, via %<70 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM level (0 FDR-significant / 6 raw-significant of 15); Band > 180 (0 FDR-significant / 6 raw-significant of 15); Range 70-180 (0 FDR-significant / 4 raw-significant of 10).
Level metrics: 0 FDR-significant (6 raw); variability metrics: 0 FDR-significant (2 raw); HbA1c alone: 0 FDR-significant (2 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Steps per wear-day (%<70 (daily avg), ΔAIC -3.8); Brisk-cadence minutes per day (MAG, ΔAIC -2.7); Resting heart-rate proxy (%>180 (pooled), ΔAIC -4.3); Total sleep time per night (MAG, ΔAIC -5.6); Garmin stress score, mean (%>180 (pooled), ΔAIC -2.4).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
