# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 201; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1626**, F-statistic = **4.88** (p = **2.84e-06**), Residual SE = **4756.056** on **190** df, AIC = **3984.9**, BIC = **4021.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20913.1172** | 2797.8902 | ±5595.7803 | **+7.475** | **7.74e-14** | *** |
| Education: graduate level (vs college) | -1113.8693 | 736.7843 | ±1473.5687 | -1.512 | 0.1306 |  |
| Education: high school or below (vs college) | +666.7229 | 1129.7943 | ±2259.5887 | +0.590 | 0.5551 |  |
| Site: UCSD (vs UAB) | +290.4919 | 886.1215 | ±1772.2431 | +0.328 | 0.7430 |  |
| Site: UW (vs UAB) | +1042.5665 | 847.1455 | ±1694.2910 | +1.231 | 0.2184 |  |
| **Age (years)** | **-164.2027** | 31.3096 | ±62.6193 | **-5.244** | **1.57e-07** | *** |
| BMI (kg/m2) | -22.6211 | 47.3429 | ±94.6858 | -0.478 | 0.6328 |  |
| Hypertension | -449.9293 | 838.8805 | ±1677.7611 | -0.536 | 0.5917 |  |
| High cholesterol | +7.2580 | 794.7577 | ±1589.5154 | +0.009 | 0.9927 |  |
| Kidney disease | -1466.4636 | 919.1859 | ±1838.3718 | -1.595 | 0.1106 |  |
| **Circulatory disease** | **-1513.4648** | 671.8725 | ±1343.7450 | **-2.253** | **0.0243** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **201**, R² = **0.2123**, Adj R² = **0.1664**, F-statistic = **4.63** (p = **3.05e-06**), Residual SE = **4745.194** on **189** df, AIC = **3984.9**, BIC = **4024.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18750.9526** | 3597.4392 | ±7194.8783 | **+5.212** | **1.87e-07** | *** |
| Education: graduate level (vs college) | -976.6086 | 777.5427 | ±1555.0855 | -1.256 | 0.2091 |  |
| Education: high school or below (vs college) | +572.7467 | 1113.9227 | ±2227.8455 | +0.514 | 0.6071 |  |
| Site: UCSD (vs UAB) | +354.3065 | 881.5196 | ±1763.0391 | +0.402 | 0.6877 |  |
| Site: UW (vs UAB) | +1086.5417 | 855.8674 | ±1711.7348 | +1.270 | 0.2043 |  |
| **Age (years)** | **-171.9589** | 31.7109 | ±63.4217 | **-5.423** | **5.87e-08** | *** |
| BMI (kg/m2) | -25.2924 | 47.0925 | ±94.1850 | -0.537 | 0.5912 |  |
| Hypertension | -454.8998 | 840.8210 | ±1681.6420 | -0.541 | 0.5885 |  |
| High cholesterol | +35.2516 | 785.7152 | ±1571.4303 | +0.045 | 0.9642 |  |
| Kidney disease | -1473.1461 | 878.7037 | ±1757.4074 | -1.676 | 0.0936 | . |
| **Circulatory disease** | **-1499.7883** | 670.6228 | ±1341.2457 | **-2.236** | **0.0253** | * |
| HbA1c (%) | +413.2523 | 405.2215 | ±810.4430 | +1.020 | 0.3078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **201**, R² = **0.2053**, Adj R² = **0.1590**, F-statistic = **4.44** (p = **6.09e-06**), Residual SE = **4766.149** on **189** df, AIC = **3986.7**, BIC = **4026.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21530.9975** | 3451.6966 | ±6903.3931 | **+6.238** | **4.44e-10** | *** |
| Education: graduate level (vs college) | -1132.5031 | 745.9701 | ±1491.9401 | -1.518 | 0.1290 |  |
| Education: high school or below (vs college) | +690.6101 | 1132.2873 | ±2264.5746 | +0.610 | 0.5419 |  |
| Site: UCSD (vs UAB) | +288.5004 | 898.3152 | ±1796.6304 | +0.321 | 0.7481 |  |
| Site: UW (vs UAB) | +1031.4840 | 853.1697 | ±1706.3394 | +1.209 | 0.2267 |  |
| **Age (years)** | **-163.7911** | 31.2783 | ±62.5566 | **-5.237** | **1.64e-07** | *** |
| BMI (kg/m2) | -22.7728 | 47.4378 | ±94.8757 | -0.480 | 0.6312 |  |
| Hypertension | -454.2907 | 841.3928 | ±1682.7856 | -0.540 | 0.5892 |  |
| High cholesterol | +8.6508 | 799.2567 | ±1598.5134 | +0.011 | 0.9914 |  |
| Kidney disease | -1427.2896 | 927.2261 | ±1854.4522 | -1.539 | 0.1237 |  |
| **Circulatory disease** | **-1502.3347** | 680.2028 | ±1360.4055 | **-2.209** | **0.0272** | * |
| Mean glucose (mg/dL) | -4.6827 | 10.9951 | ±21.9901 | -0.426 | 0.6702 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **201**, R² = **0.2053**, Adj R² = **0.1590**, F-statistic = **4.44** (p = **6.09e-06**), Residual SE = **4766.149** on **189** df, AIC = **3986.7**, BIC = **4026.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22178.9733** | 4548.5593 | ±9097.1185 | **+4.876** | **1.08e-06** | *** |
| Education: graduate level (vs college) | -1132.5031 | 745.9701 | ±1491.9401 | -1.518 | 0.1290 |  |
| Education: high school or below (vs college) | +690.6101 | 1132.2873 | ±2264.5746 | +0.610 | 0.5419 |  |
| Site: UCSD (vs UAB) | +288.5004 | 898.3152 | ±1796.6304 | +0.321 | 0.7481 |  |
| Site: UW (vs UAB) | +1031.4840 | 853.1697 | ±1706.3394 | +1.209 | 0.2267 |  |
| **Age (years)** | **-163.7911** | 31.2783 | ±62.5566 | **-5.237** | **1.64e-07** | *** |
| BMI (kg/m2) | -22.7728 | 47.4378 | ±94.8757 | -0.480 | 0.6312 |  |
| Hypertension | -454.2907 | 841.3928 | ±1682.7856 | -0.540 | 0.5892 |  |
| High cholesterol | +8.6508 | 799.2567 | ±1598.5134 | +0.011 | 0.9914 |  |
| Kidney disease | -1427.2896 | 927.2261 | ±1854.4522 | -1.539 | 0.1237 |  |
| **Circulatory disease** | **-1502.3347** | 680.2028 | ±1360.4055 | **-2.209** | **0.0272** | * |
| GMI (%) | -195.7631 | 459.6596 | ±919.3192 | -0.426 | 0.6702 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.60e-06**), Residual SE = **4768.616** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20884.7376** | 3391.1451 | ±6782.2901 | **+6.159** | **7.34e-10** | *** |
| Education: graduate level (vs college) | -1113.7216 | 739.9618 | ±1479.9237 | -1.505 | 0.1323 |  |
| Education: high school or below (vs college) | +665.6103 | 1133.8174 | ±2267.6349 | +0.587 | 0.5572 |  |
| Site: UCSD (vs UAB) | +290.2894 | 889.8858 | ±1779.7716 | +0.326 | 0.7443 |  |
| Site: UW (vs UAB) | +1042.7546 | 850.4843 | ±1700.9687 | +1.226 | 0.2202 |  |
| **Age (years)** | **-164.1744** | 31.7120 | ±63.4239 | **-5.177** | **2.25e-07** | *** |
| BMI (kg/m2) | -22.6357 | 47.4391 | ±94.8783 | -0.477 | 0.6333 |  |
| Hypertension | -450.4046 | 844.5558 | ±1689.1116 | -0.533 | 0.5938 |  |
| High cholesterol | +6.9313 | 800.2624 | ±1600.5248 | +0.009 | 0.9931 |  |
| Kidney disease | -1466.9155 | 923.8434 | ±1847.6868 | -1.588 | 0.1123 |  |
| **Circulatory disease** | **-1514.1243** | 680.1977 | ±1360.3953 | **-2.226** | **0.0260** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.2134 | 10.5165 | ±21.0330 | +0.020 | 0.9838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2086**, Adj R² = **0.1626**, F-statistic = **4.53** (p = **4.39e-06**), Residual SE = **4756.192** on **189** df, AIC = **3985.9**, BIC = **4025.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21410.6696** | 2906.6588 | ±5813.3176 | **+7.366** | **1.76e-13** | *** |
| Education: graduate level (vs college) | -1218.6975 | 749.8228 | ±1499.6455 | -1.625 | 0.1041 |  |
| Education: high school or below (vs college) | +807.6093 | 1121.5160 | ±2243.0321 | +0.720 | 0.4715 |  |
| Site: UCSD (vs UAB) | +266.2295 | 901.3911 | ±1802.7822 | +0.295 | 0.7677 |  |
| Site: UW (vs UAB) | +996.2267 | 853.8541 | ±1707.7083 | +1.167 | 0.2433 |  |
| **Age (years)** | **-158.2332** | 31.5096 | ±63.0191 | **-5.022** | **5.12e-07** | *** |
| BMI (kg/m2) | -24.7991 | 47.6630 | ±95.3260 | -0.520 | 0.6029 |  |
| Hypertension | -470.7782 | 836.4406 | ±1672.8811 | -0.563 | 0.5735 |  |
| High cholesterol | +3.5531 | 797.6601 | ±1595.3202 | +0.004 | 0.9964 |  |
| Kidney disease | -1257.1407 | 927.8631 | ±1855.7262 | -1.355 | 0.1755 |  |
| **Circulatory disease** | **-1529.3293** | 679.4907 | ±1358.9814 | **-2.251** | **0.0244** | * |
| Glucose SD, pooled (mg/dL) | -22.6556 | 21.6716 | ±43.3433 | -1.045 | 0.2958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2110**, Adj R² = **0.1650**, F-statistic = **4.59** (p = **3.48e-06**), Residual SE = **4749.131** on **189** df, AIC = **3985.3**, BIC = **4024.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21612.3684** | 2916.1222 | ±5832.2444 | **+7.411** | **1.25e-13** | *** |
| Education: graduate level (vs college) | -1248.8566 | 750.0801 | ±1500.1602 | -1.665 | 0.0959 | . |
| Education: high school or below (vs college) | +878.5664 | 1114.8620 | ±2229.7239 | +0.788 | 0.4307 |  |
| Site: UCSD (vs UAB) | +252.8481 | 901.6362 | ±1803.2723 | +0.280 | 0.7791 |  |
| Site: UW (vs UAB) | +995.2793 | 850.2763 | ±1700.5526 | +1.171 | 0.2418 |  |
| **Age (years)** | **-156.8010** | 31.0894 | ±62.1787 | **-5.044** | **4.57e-07** | *** |
| BMI (kg/m2) | -26.5422 | 47.6605 | ±95.3209 | -0.557 | 0.5776 |  |
| Hypertension | -489.6443 | 835.2279 | ±1670.4559 | -0.586 | 0.5577 |  |
| High cholesterol | +18.2285 | 794.9810 | ±1589.9621 | +0.023 | 0.9817 |  |
| Kidney disease | -1201.5965 | 932.8987 | ±1865.7974 | -1.288 | 0.1977 |  |
| **Circulatory disease** | **-1543.1541** | 678.1181 | ±1356.2362 | **-2.276** | **0.0229** | * |
| Avg. daily SD (mg/dL) | -33.5755 | 24.0278 | ±48.0556 | -1.397 | 0.1623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **201**, R² = **0.2082**, Adj R² = **0.1622**, F-statistic = **4.52** (p = **4.55e-06**), Residual SE = **4757.290** on **189** df, AIC = **3985.9**, BIC = **4025.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21674.6713** | 2905.6951 | ±5811.3901 | **+7.459** | **8.69e-14** | *** |
| Education: graduate level (vs college) | -1239.9993 | 746.2879 | ±1492.5758 | -1.662 | 0.0966 | . |
| Education: high school or below (vs college) | +846.5928 | 1124.1222 | ±2248.2444 | +0.753 | 0.4514 |  |
| Site: UCSD (vs UAB) | +274.4087 | 890.1384 | ±1780.2768 | +0.308 | 0.7579 |  |
| Site: UW (vs UAB) | +994.6782 | 855.4078 | ±1710.8156 | +1.163 | 0.2449 |  |
| **Age (years)** | **-154.6823** | 33.2210 | ±66.4420 | **-4.656** | **3.22e-06** | *** |
| BMI (kg/m2) | -25.3099 | 48.0422 | ±96.0844 | -0.527 | 0.5983 |  |
| Hypertension | -477.6368 | 836.9363 | ±1673.8727 | -0.571 | 0.5682 |  |
| High cholesterol | +9.7671 | 797.2985 | ±1594.5970 | +0.012 | 0.9902 |  |
| Kidney disease | -1225.2981 | 935.8356 | ±1871.6711 | -1.309 | 0.1904 |  |
| **Circulatory disease** | **-1547.6238** | 679.5725 | ±1359.1450 | **-2.277** | **0.0228** | * |
| CV (%) | -50.8979 | 46.6975 | ±93.3950 | -1.090 | 0.2757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.59e-06**), Residual SE = **4768.568** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20795.5306** | 3237.7793 | ±6475.5585 | **+6.423** | **1.34e-10** | *** |
| Education: graduate level (vs college) | -1121.9369 | 751.0894 | ±1502.1787 | -1.494 | 0.1352 |  |
| Education: high school or below (vs college) | +679.3662 | 1131.3028 | ±2262.6056 | +0.601 | 0.5482 |  |
| Site: UCSD (vs UAB) | +291.8479 | 888.9467 | ±1777.8933 | +0.328 | 0.7427 |  |
| Site: UW (vs UAB) | +1041.0050 | 853.0599 | ±1706.1197 | +1.220 | 0.2223 |  |
| **Age (years)** | **-163.5184** | 33.4444 | ±66.8889 | **-4.889** | **1.01e-06** | *** |
| BMI (kg/m2) | -22.6934 | 47.6989 | ±95.3979 | -0.476 | 0.6342 |  |
| Hypertension | -452.4183 | 839.6556 | ±1679.3112 | -0.539 | 0.5900 |  |
| High cholesterol | +7.3216 | 797.8162 | ±1595.6325 | +0.009 | 0.9927 |  |
| Kidney disease | -1455.3805 | 941.7194 | ±1883.4389 | -1.545 | 0.1222 |  |
| **Circulatory disease** | **-1512.8772** | 674.5596 | ±1349.1192 | **-2.243** | **0.0249** | * |
| Mean / SD ratio | +17.5600 | 233.7308 | ±467.4616 | +0.075 | 0.9401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.59e-06**), Residual SE = **4768.566** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20797.3123** | 3202.9577 | ±6405.9153 | **+6.493** | **8.41e-11** | *** |
| Education: graduate level (vs college) | -1122.5515 | 747.6938 | ±1495.3877 | -1.501 | 0.1333 |  |
| Education: high school or below (vs college) | +679.7184 | 1120.4898 | ±2240.9796 | +0.607 | 0.5441 |  |
| Site: UCSD (vs UAB) | +292.6101 | 889.0494 | ±1778.0988 | +0.329 | 0.7421 |  |
| Site: UW (vs UAB) | +1042.3019 | 849.8156 | ±1699.6311 | +1.227 | 0.2200 |  |
| **Age (years)** | **-163.5096** | 33.2880 | ±66.5760 | **-4.912** | **9.02e-07** | *** |
| BMI (kg/m2) | -22.7474 | 47.6783 | ±95.3566 | -0.477 | 0.6333 |  |
| Hypertension | -453.6397 | 839.9143 | ±1679.8287 | -0.540 | 0.5891 |  |
| High cholesterol | +9.1265 | 799.8298 | ±1599.6596 | +0.011 | 0.9909 |  |
| Kidney disease | -1458.9358 | 934.3760 | ±1868.7520 | -1.561 | 0.1184 |  |
| **Circulatory disease** | **-1513.5460** | 674.1695 | ±1348.3390 | **-2.245** | **0.0248** | * |
| Avg. daily mean/SD | +14.7017 | 179.4812 | ±358.9625 | +0.082 | 0.9347 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **201**, R² = **0.2050**, Adj R² = **0.1587**, F-statistic = **4.43** (p = **6.27e-06**), Residual SE = **4767.063** on **189** df, AIC = **3986.8**, BIC = **4026.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20530.7174** | 3184.5984 | ±6369.1967 | **+6.447** | **1.14e-10** | *** |
| Education: graduate level (vs college) | -1085.8953 | 748.5260 | ±1497.0520 | -1.451 | 0.1469 |  |
| Education: high school or below (vs college) | +613.1487 | 1130.5464 | ±2261.0929 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | +278.7103 | 885.3691 | ±1770.7382 | +0.315 | 0.7529 |  |
| Site: UW (vs UAB) | +1070.6188 | 858.0461 | ±1716.0922 | +1.248 | 0.2121 |  |
| **Age (years)** | **-165.3058** | 31.4475 | ±62.8950 | **-5.257** | **1.47e-07** | *** |
| BMI (kg/m2) | -24.0653 | 47.3402 | ±94.6803 | -0.508 | 0.6112 |  |
| Hypertension | -433.9506 | 846.5063 | ±1693.0127 | -0.513 | 0.6082 |  |
| High cholesterol | -5.3608 | 803.7705 | ±1607.5409 | -0.007 | 0.9947 |  |
| Kidney disease | -1474.8780 | 925.5948 | ±1851.1896 | -1.593 | 0.1111 |  |
| **Circulatory disease** | **-1511.8332** | 675.9824 | ±1351.9648 | **-2.236** | **0.0253** | * |
| MAG (mg/dL/h) | +10.9812 | 35.1384 | ±70.2767 | +0.313 | 0.7547 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **201**, R² = **0.2077**, Adj R² = **0.1616**, F-statistic = **4.50** (p = **4.80e-06**), Residual SE = **4758.885** on **189** df, AIC = **3986.1**, BIC = **4025.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21621.3742** | 3036.8808 | ±6073.7616 | **+7.120** | **1.08e-12** | *** |
| Education: graduate level (vs college) | -1213.4720 | 752.6429 | ±1505.2857 | -1.612 | 0.1069 |  |
| Education: high school or below (vs college) | +833.0049 | 1121.0632 | ±2242.1263 | +0.743 | 0.4575 |  |
| Site: UCSD (vs UAB) | +280.0490 | 900.3161 | ±1800.6322 | +0.311 | 0.7558 |  |
| Site: UW (vs UAB) | +1019.9341 | 852.1492 | ±1704.2983 | +1.197 | 0.2313 |  |
| **Age (years)** | **-159.2985** | 31.2337 | ±62.4675 | **-5.100** | **3.39e-07** | *** |
| BMI (kg/m2) | -25.4830 | 47.9695 | ±95.9390 | -0.531 | 0.5953 |  |
| Hypertension | -492.7041 | 838.3883 | ±1676.7766 | -0.588 | 0.5567 |  |
| High cholesterol | +30.3793 | 798.5465 | ±1597.0929 | +0.038 | 0.9697 |  |
| Kidney disease | -1280.8065 | 932.0497 | ±1864.0993 | -1.374 | 0.1694 |  |
| **Circulatory disease** | **-1513.2314** | 675.8136 | ±1351.6272 | **-2.239** | **0.0251** | * |
| Avg. daily range (mg/dL) | -6.7043 | 7.3827 | ±14.7654 | -0.908 | 0.3638 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **201**, R² = **0.2045**, Adj R² = **0.1582**, F-statistic = **4.42** (p = **6.58e-06**), Residual SE = **4768.520** on **189** df, AIC = **3986.9**, BIC = **4026.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20889.2901** | 2853.2323 | ±5706.4645 | **+7.321** | **2.46e-13** | *** |
| Education: graduate level (vs college) | -1104.2799 | 761.0679 | ±1522.1358 | -1.451 | 0.1468 |  |
| Education: high school or below (vs college) | +666.1455 | 1141.4003 | ±2282.8006 | +0.584 | 0.5595 |  |
| Site: UCSD (vs UAB) | +290.5192 | 890.5152 | ±1781.0305 | +0.326 | 0.7442 |  |
| Site: UW (vs UAB) | +1047.0358 | 859.2254 | ±1718.4507 | +1.219 | 0.2230 |  |
| **Age (years)** | **-164.5160** | 31.6596 | ±63.3191 | **-5.196** | **2.03e-07** | *** |
| BMI (kg/m2) | -22.5227 | 47.8007 | ±95.6014 | -0.471 | 0.6375 |  |
| Hypertension | -453.8495 | 847.5509 | ±1695.1018 | -0.535 | 0.5923 |  |
| High cholesterol | +9.0747 | 796.8351 | ±1593.6702 | +0.011 | 0.9909 |  |
| Kidney disease | -1479.1445 | 913.5150 | ±1827.0300 | -1.619 | 0.1054 |  |
| **Circulatory disease** | **-1517.3404** | 680.8192 | ±1361.6383 | **-2.229** | **0.0258** | * |
| SD of daily means (mg/dL) | +3.2154 | 38.8064 | ±77.6128 | +0.083 | 0.9340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **201**, R² = **0.2084**, Adj R² = **0.1623**, F-statistic = **4.52** (p = **4.48e-06**), Residual SE = **4756.832** on **189** df, AIC = **3985.9**, BIC = **4025.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19298.6638** | 2868.8442 | ±5737.6885 | **+6.727** | **1.73e-11** | *** |
| Education: graduate level (vs college) | -1219.1405 | 751.7105 | ±1503.4210 | -1.622 | 0.1048 |  |
| Education: high school or below (vs college) | +714.6270 | 1134.0984 | ±2268.1968 | +0.630 | 0.5286 |  |
| Site: UCSD (vs UAB) | +257.9336 | 916.8806 | ±1833.7612 | +0.281 | 0.7785 |  |
| Site: UW (vs UAB) | +1001.4285 | 850.4539 | ±1700.9079 | +1.178 | 0.2390 |  |
| **Age (years)** | **-161.5154** | 31.1029 | ±62.2058 | **-5.193** | **2.07e-07** | *** |
| BMI (kg/m2) | -24.2342 | 47.8066 | ±95.6133 | -0.507 | 0.6122 |  |
| Hypertension | -486.1864 | 835.7017 | ±1671.4035 | -0.582 | 0.5607 |  |
| High cholesterol | +43.9041 | 801.2378 | ±1602.4756 | +0.055 | 0.9563 |  |
| Kidney disease | -1329.0129 | 930.7488 | ±1861.4977 | -1.428 | 0.1533 |  |
| **Circulatory disease** | **-1468.3155** | 680.9181 | ±1361.8363 | **-2.156** | **0.0311** | * |
| Time in range 70-180, pooled (%) | +18.2531 | 18.7856 | ±37.5712 | +0.972 | 0.3312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **201**, R² = **0.2083**, Adj R² = **0.1622**, F-statistic = **4.52** (p = **4.54e-06**), Residual SE = **4757.201** on **189** df, AIC = **3985.9**, BIC = **4025.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19335.0557** | 2891.8769 | ±5783.7539 | **+6.686** | **2.29e-11** | *** |
| Education: graduate level (vs college) | -1216.8282 | 750.6604 | ±1501.3209 | -1.621 | 0.1050 |  |
| Education: high school or below (vs college) | +722.8742 | 1134.9669 | ±2269.9338 | +0.637 | 0.5242 |  |
| Site: UCSD (vs UAB) | +253.7790 | 916.5398 | ±1833.0795 | +0.277 | 0.7819 |  |
| Site: UW (vs UAB) | +998.7071 | 850.6861 | ±1701.3722 | +1.174 | 0.2404 |  |
| **Age (years)** | **-161.6069** | 31.1292 | ±62.2583 | **-5.191** | **2.09e-07** | *** |
| BMI (kg/m2) | -24.5908 | 47.8197 | ±95.6394 | -0.514 | 0.6071 |  |
| Hypertension | -489.9613 | 836.0872 | ±1672.1743 | -0.586 | 0.5579 |  |
| High cholesterol | +44.8226 | 802.6378 | ±1605.2756 | +0.056 | 0.9555 |  |
| Kidney disease | -1327.8548 | 929.1313 | ±1858.2626 | -1.429 | 0.1530 |  |
| **Circulatory disease** | **-1465.9887** | 681.1666 | ±1362.3332 | **-2.152** | **0.0314** | * |
| Avg. daily time in range 70-180 (%) | +17.9517 | 18.7947 | ±37.5895 | +0.955 | 0.3395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2097**, Adj R² = **0.1637**, F-statistic = **4.56** (p = **3.94e-06**), Residual SE = **4752.917** on **189** df, AIC = **3985.6**, BIC = **4025.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21072.0777** | 2813.7074 | ±5627.4149 | **+7.489** | **6.94e-14** | *** |
| Education: graduate level (vs college) | -1167.1468 | 736.1824 | ±1472.3648 | -1.585 | 0.1129 |  |
| Education: high school or below (vs college) | +582.8858 | 1130.3447 | ±2260.6893 | +0.516 | 0.6061 |  |
| Site: UCSD (vs UAB) | +181.9764 | 886.8020 | ±1773.6040 | +0.205 | 0.8374 |  |
| Site: UW (vs UAB) | +896.8272 | 862.0341 | ±1724.0683 | +1.040 | 0.2982 |  |
| **Age (years)** | **-163.2924** | 31.2244 | ±62.4488 | **-5.230** | **1.70e-07** | *** |
| BMI (kg/m2) | -21.8903 | 47.7541 | ±95.5082 | -0.458 | 0.6467 |  |
| Hypertension | -403.5120 | 836.9935 | ±1673.9871 | -0.482 | 0.6297 |  |
| High cholesterol | +21.1273 | 793.0751 | ±1586.1502 | +0.027 | 0.9787 |  |
| Kidney disease | -1482.6712 | 914.9155 | ±1829.8310 | -1.621 | 0.1051 |  |
| **Circulatory disease** | **-1430.0111** | 673.9990 | ±1347.9980 | **-2.122** | **0.0339** | * |
| Time < 54 (%) | -495.0009 | 380.5457 | ±761.0914 | -1.301 | 0.1933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **201**, R² = **0.2122**, Adj R² = **0.1664**, F-statistic = **4.63** (p = **3.07e-06**), Residual SE = **4745.369** on **189** df, AIC = **3984.9**, BIC = **4024.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20961.6241** | 2789.6655 | ±5579.3309 | **+7.514** | **5.73e-14** | *** |
| Education: graduate level (vs college) | -1202.0702 | 742.2988 | ±1484.5976 | -1.619 | 0.1054 |  |
| Education: high school or below (vs college) | +570.2015 | 1131.3633 | ±2262.7266 | +0.504 | 0.6143 |  |
| Site: UCSD (vs UAB) | +178.3029 | 887.9828 | ±1775.9657 | +0.201 | 0.8409 |  |
| Site: UW (vs UAB) | +909.7437 | 859.2001 | ±1718.4001 | +1.059 | 0.2897 |  |
| **Age (years)** | **-161.1019** | 31.3736 | ±62.7471 | **-5.135** | **2.82e-07** | *** |
| BMI (kg/m2) | -22.7107 | 47.1150 | ±94.2301 | -0.482 | 0.6298 |  |
| Hypertension | -418.8048 | 837.7426 | ±1675.4852 | -0.500 | 0.6171 |  |
| High cholesterol | -16.7332 | 791.6705 | ±1583.3410 | -0.021 | 0.9831 |  |
| Kidney disease | -1452.0102 | 916.3045 | ±1832.6091 | -1.585 | 0.1130 |  |
| **Circulatory disease** | **-1417.1558** | 672.4138 | ±1344.8276 | **-2.108** | **0.0351** | * |
| Avg. daily time < 54 (%) | -542.1604 | 293.4102 | ±586.8205 | -1.848 | 0.0646 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2081**, Adj R² = **0.1620**, F-statistic = **4.51** (p = **4.64e-06**), Residual SE = **4757.867** on **189** df, AIC = **3986.0**, BIC = **4025.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20958.4643** | 2814.8929 | ±5629.7858 | **+7.446** | **9.65e-14** | *** |
| Education: graduate level (vs college) | -1230.2639 | 729.9056 | ±1459.8113 | -1.686 | 0.0919 | . |
| Education: high school or below (vs college) | +697.1774 | 1142.3198 | ±2284.6395 | +0.610 | 0.5417 |  |
| Site: UCSD (vs UAB) | +233.9471 | 874.6947 | ±1749.3894 | +0.267 | 0.7891 |  |
| Site: UW (vs UAB) | +1005.9507 | 847.9321 | ±1695.8642 | +1.186 | 0.2355 |  |
| **Age (years)** | **-160.3295** | 32.0908 | ±64.1815 | **-4.996** | **5.85e-07** | *** |
| BMI (kg/m2) | -23.3538 | 48.3477 | ±96.6953 | -0.483 | 0.6291 |  |
| Hypertension | -463.4314 | 837.2533 | ±1674.5066 | -0.554 | 0.5799 |  |
| High cholesterol | +27.9959 | 797.0722 | ±1594.1444 | +0.035 | 0.9720 |  |
| Kidney disease | -1449.6931 | 912.9796 | ±1825.9593 | -1.588 | 0.1123 |  |
| **Circulatory disease** | **-1501.2902** | 675.0257 | ±1350.0515 | **-2.224** | **0.0261** | * |
| Time 54-69, pooled (%) | -125.0139 | 106.3625 | ±212.7249 | -1.175 | 0.2399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **201**, R² = **0.2088**, Adj R² = **0.1628**, F-statistic = **4.53** (p = **4.30e-06**), Residual SE = **4755.587** on **189** df, AIC = **3985.8**, BIC = **4025.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20898.8758** | 2818.3867 | ±5636.7734 | **+7.415** | **1.21e-13** | *** |
| Education: graduate level (vs college) | -1233.3778 | 731.2641 | ±1462.5282 | -1.687 | 0.0917 | . |
| Education: high school or below (vs college) | +712.1018 | 1143.1213 | ±2286.2426 | +0.623 | 0.5333 |  |
| Site: UCSD (vs UAB) | +234.3829 | 875.0327 | ±1750.0653 | +0.268 | 0.7888 |  |
| Site: UW (vs UAB) | +1002.9322 | 849.6336 | ±1699.2671 | +1.180 | 0.2378 |  |
| **Age (years)** | **-159.3316** | 32.3003 | ±64.6007 | **-4.933** | **8.11e-07** | *** |
| BMI (kg/m2) | -23.3884 | 48.0643 | ±96.1285 | -0.487 | 0.6265 |  |
| Hypertension | -462.2409 | 837.4006 | ±1674.8013 | -0.552 | 0.5810 |  |
| High cholesterol | +24.8911 | 796.6637 | ±1593.3274 | +0.031 | 0.9751 |  |
| Kidney disease | -1447.4164 | 913.1651 | ±1826.3303 | -1.585 | 0.1130 |  |
| **Circulatory disease** | **-1503.2535** | 674.6342 | ±1349.2683 | **-2.228** | **0.0259** | * |
| Avg. daily time 54-69 (%) | -129.5705 | 96.6432 | ±193.2864 | -1.341 | 0.1800 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **201**, R² = **0.2090**, Adj R² = **0.1630**, F-statistic = **4.54** (p = **4.22e-06**), Residual SE = **4755.016** on **189** df, AIC = **3985.8**, BIC = **4025.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20992.1193** | 2813.4674 | ±5626.9349 | **+7.461** | **8.57e-14** | *** |
| Education: graduate level (vs college) | -1233.8606 | 730.8425 | ±1461.6849 | -1.688 | 0.0914 | . |
| Education: high school or below (vs college) | +675.2994 | 1137.7617 | ±2275.5234 | +0.594 | 0.5528 |  |
| Site: UCSD (vs UAB) | +212.9151 | 874.7887 | ±1749.5775 | +0.243 | 0.8077 |  |
| Site: UW (vs UAB) | +974.7183 | 848.3431 | ±1696.6862 | +1.149 | 0.2506 |  |
| **Age (years)** | **-160.4111** | 31.8668 | ±63.7336 | **-5.034** | **4.81e-07** | *** |
| BMI (kg/m2) | -23.1276 | 48.3778 | ±96.7555 | -0.478 | 0.6326 |  |
| Hypertension | -451.5735 | 834.2618 | ±1668.5236 | -0.541 | 0.5883 |  |
| High cholesterol | +29.6582 | 795.8794 | ±1591.7587 | +0.037 | 0.9703 |  |
| Kidney disease | -1454.7489 | 911.3598 | ±1822.7196 | -1.596 | 0.1104 |  |
| **Circulatory disease** | **-1482.7382** | 674.1763 | ±1348.3527 | **-2.199** | **0.0279** | * |
| Time < 70 (%) | -115.5224 | 84.0622 | ±168.1244 | -1.374 | 0.1694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **201**, R² = **0.2103**, Adj R² = **0.1644**, F-statistic = **4.58** (p = **3.71e-06**), Residual SE = **4751.073** on **189** df, AIC = **3985.4**, BIC = **4025.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20910.6174** | 2811.9806 | ±5623.9611 | **+7.436** | **1.04e-13** | *** |
| Education: graduate level (vs college) | -1246.5506 | 733.8767 | ±1467.7534 | -1.699 | 0.0894 | . |
| Education: high school or below (vs college) | +687.7795 | 1137.2446 | ±2274.4893 | +0.605 | 0.5453 |  |
| Site: UCSD (vs UAB) | +212.2341 | 875.4896 | ±1750.9792 | +0.242 | 0.8085 |  |
| Site: UW (vs UAB) | +975.2031 | 850.6327 | ±1701.2654 | +1.146 | 0.2516 |  |
| **Age (years)** | **-158.9062** | 32.0945 | ±64.1890 | **-4.951** | **7.38e-07** | *** |
| BMI (kg/m2) | -23.3655 | 47.9197 | ±95.8393 | -0.488 | 0.6258 |  |
| Hypertension | -454.5284 | 835.2902 | ±1670.5803 | -0.544 | 0.5863 |  |
| High cholesterol | +18.4883 | 794.7409 | ±1589.4818 | +0.023 | 0.9814 |  |
| Kidney disease | -1445.2276 | 911.9552 | ±1823.9103 | -1.585 | 0.1130 |  |
| **Circulatory disease** | **-1482.1053** | 673.2370 | ±1346.4740 | **-2.201** | **0.0277** | * |
| Avg. daily time < 70 (%) | -122.2838 | 73.0572 | ±146.1144 | -1.674 | 0.0942 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2092**, Adj R² = **0.1631**, F-statistic = **4.54** (p = **4.16e-06**), Residual SE = **4754.526** on **189** df, AIC = **3985.7**, BIC = **4025.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17321.8300** | 3988.4848 | ±7976.9697 | **+4.343** | **1.41e-05** | *** |
| Education: graduate level (vs college) | -1183.5604 | 739.4034 | ±1478.8067 | -1.601 | 0.1094 |  |
| Education: high school or below (vs college) | +738.1375 | 1131.0068 | ±2262.0135 | +0.653 | 0.5140 |  |
| Site: UCSD (vs UAB) | +251.0995 | 904.2885 | ±1808.5770 | +0.278 | 0.7813 |  |
| Site: UW (vs UAB) | +958.1388 | 850.9489 | ±1701.8979 | +1.126 | 0.2602 |  |
| **Age (years)** | **-164.5887** | 31.3700 | ±62.7399 | **-5.247** | **1.55e-07** | *** |
| BMI (kg/m2) | -24.4740 | 47.3291 | ±94.6582 | -0.517 | 0.6051 |  |
| Hypertension | -443.8624 | 835.9005 | ±1671.8010 | -0.531 | 0.5954 |  |
| High cholesterol | -23.4701 | 796.1858 | ±1592.3716 | -0.029 | 0.9765 |  |
| Kidney disease | -1388.3180 | 925.7504 | ±1851.5008 | -1.500 | 0.1337 |  |
| **Circulatory disease** | **-1453.2222** | 684.1817 | ±1368.3635 | **-2.124** | **0.0337** | * |
| Time 54-250, pooled (%) | +38.5253 | 34.5333 | ±69.0666 | +1.116 | 0.2646 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2072**, Adj R² = **0.1610**, F-statistic = **4.49** (p = **5.07e-06**), Residual SE = **4760.556** on **189** df, AIC = **3986.2**, BIC = **4025.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17841.7264** | 4391.0669 | ±8782.1339 | **+4.063** | **4.84e-05** | *** |
| Education: graduate level (vs college) | -1172.7108 | 740.6671 | ±1481.3343 | -1.583 | 0.1133 |  |
| Education: high school or below (vs college) | +730.3472 | 1131.5741 | ±2263.1483 | +0.645 | 0.5187 |  |
| Site: UCSD (vs UAB) | +263.5997 | 901.7193 | ±1803.4387 | +0.292 | 0.7700 |  |
| Site: UW (vs UAB) | +983.3526 | 851.1621 | ±1702.3242 | +1.155 | 0.2480 |  |
| **Age (years)** | **-164.1233** | 31.3504 | ±62.7008 | **-5.235** | **1.65e-07** | *** |
| BMI (kg/m2) | -24.5300 | 47.5075 | ±95.0149 | -0.516 | 0.6056 |  |
| Hypertension | -446.0872 | 837.6181 | ±1675.2362 | -0.533 | 0.5943 |  |
| High cholesterol | -13.9583 | 797.3742 | ±1594.7484 | -0.018 | 0.9860 |  |
| Kidney disease | -1394.0909 | 922.2625 | ±1844.5251 | -1.512 | 0.1306 |  |
| **Circulatory disease** | **-1457.0558** | 686.6513 | ±1373.3025 | **-2.122** | **0.0338** | * |
| Avg. daily time 54-250 (%) | +32.5766 | 39.3599 | ±78.7198 | +0.828 | 0.4079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2053**, Adj R² = **0.1590**, F-statistic = **4.44** (p = **6.11e-06**), Residual SE = **4766.231** on **189** df, AIC = **3986.7**, BIC = **4026.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20967.4784** | 2847.9273 | ±5695.8546 | **+7.362** | **1.81e-13** | *** |
| Education: graduate level (vs college) | -1151.2012 | 754.1686 | ±1508.3371 | -1.526 | 0.1269 |  |
| Education: high school or below (vs college) | +673.2232 | 1134.8300 | ±2269.6601 | +0.593 | 0.5530 |  |
| Site: UCSD (vs UAB) | +286.6826 | 906.1292 | ±1812.2583 | +0.316 | 0.7517 |  |
| Site: UW (vs UAB) | +1045.4107 | 846.9928 | ±1693.9856 | +1.234 | 0.2171 |  |
| **Age (years)** | **-162.6457** | 30.8728 | ±61.7456 | **-5.268** | **1.38e-07** | *** |
| BMI (kg/m2) | -23.0456 | 47.8486 | ±95.6973 | -0.482 | 0.6301 |  |
| Hypertension | -475.0348 | 834.2968 | ±1668.5935 | -0.569 | 0.5691 |  |
| High cholesterol | +39.8065 | 806.3288 | ±1612.6576 | +0.049 | 0.9606 |  |
| Kidney disease | -1400.2701 | 937.3835 | ±1874.7671 | -1.494 | 0.1352 |  |
| **Circulatory disease** | **-1503.4462** | 677.8223 | ±1355.6445 | **-2.218** | **0.0266** | * |
| Time 181-250, pooled (%) | -12.3319 | 29.4247 | ±58.8495 | -0.419 | 0.6751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **201**, R² = **0.2061**, Adj R² = **0.1599**, F-statistic = **4.46** (p = **5.62e-06**), Residual SE = **4763.707** on **189** df, AIC = **3986.5**, BIC = **4026.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21023.9132** | 2861.7038 | ±5723.4075 | **+7.347** | **2.03e-13** | *** |
| Education: graduate level (vs college) | -1165.2319 | 750.8604 | ±1501.7207 | -1.552 | 0.1207 |  |
| Education: high school or below (vs college) | +680.8094 | 1135.1720 | ±2270.3439 | +0.600 | 0.5487 |  |
| Site: UCSD (vs UAB) | +277.0557 | 911.7997 | ±1823.5994 | +0.304 | 0.7612 |  |
| Site: UW (vs UAB) | +1037.1066 | 847.8776 | ±1695.7551 | +1.223 | 0.2213 |  |
| **Age (years)** | **-162.4164** | 30.9751 | ±61.9502 | **-5.243** | **1.58e-07** | *** |
| BMI (kg/m2) | -23.3932 | 47.8104 | ±95.6207 | -0.489 | 0.6246 |  |
| Hypertension | -488.4146 | 835.1071 | ±1670.2143 | -0.585 | 0.5586 |  |
| High cholesterol | +51.8044 | 805.8674 | ±1611.7348 | +0.064 | 0.9487 |  |
| Kidney disease | -1375.0279 | 935.9892 | ±1871.9785 | -1.469 | 0.1418 |  |
| **Circulatory disease** | **-1499.2133** | 678.0585 | ±1356.1169 | **-2.211** | **0.0270** | * |
| Avg. daily time 181-250 (%) | -17.0825 | 27.8256 | ±55.6512 | -0.614 | 0.5393 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **201**, R² = **0.2070**, Adj R² = **0.1608**, F-statistic = **4.48** (p = **5.15e-06**), Residual SE = **4761.063** on **189** df, AIC = **3986.3**, BIC = **4025.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21068.7417** | 2860.4944 | ±5720.9888 | **+7.365** | **1.77e-13** | *** |
| Education: graduate level (vs college) | -1181.5795 | 749.6790 | ±1499.3581 | -1.576 | 0.1150 |  |
| Education: high school or below (vs college) | +703.2398 | 1132.7838 | ±2265.5676 | +0.621 | 0.5347 |  |
| Site: UCSD (vs UAB) | +274.5663 | 910.7929 | ±1821.5858 | +0.301 | 0.7631 |  |
| Site: UW (vs UAB) | +1018.7044 | 849.8201 | ±1699.6402 | +1.199 | 0.2306 |  |
| **Age (years)** | **-162.5646** | 31.1436 | ±62.2872 | **-5.220** | **1.79e-07** | *** |
| BMI (kg/m2) | -23.8238 | 47.7354 | ±95.4709 | -0.499 | 0.6177 |  |
| Hypertension | -478.1686 | 836.8710 | ±1673.7420 | -0.571 | 0.5677 |  |
| High cholesterol | +33.2297 | 800.8504 | ±1601.7008 | +0.041 | 0.9669 |  |
| Kidney disease | -1360.0881 | 931.0235 | ±1862.0469 | -1.461 | 0.1441 |  |
| **Circulatory disease** | **-1481.8546** | 681.0385 | ±1362.0770 | **-2.176** | **0.0296** | * |
| Time > 180 (%) | -14.3193 | 18.6761 | ±37.3523 | -0.767 | 0.4433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2067**, Adj R² = **0.1605**, F-statistic = **4.48** (p = **5.31e-06**), Residual SE = **4761.962** on **189** df, AIC = **3986.3**, BIC = **4026.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21076.9392** | 2866.3337 | ±5732.6673 | **+7.353** | **1.93e-13** | *** |
| Education: graduate level (vs college) | -1176.7545 | 748.5730 | ±1497.1460 | -1.572 | 0.1160 |  |
| Education: high school or below (vs college) | +706.6925 | 1133.4924 | ±2266.9847 | +0.623 | 0.5330 |  |
| Site: UCSD (vs UAB) | +271.4906 | 910.7353 | ±1821.4707 | +0.298 | 0.7656 |  |
| Site: UW (vs UAB) | +1016.9771 | 850.1641 | ±1700.3281 | +1.196 | 0.2316 |  |
| **Age (years)** | **-162.8330** | 31.1682 | ±62.3363 | **-5.224** | **1.75e-07** | *** |
| BMI (kg/m2) | -24.0225 | 47.8018 | ±95.6037 | -0.503 | 0.6153 |  |
| Hypertension | -479.5764 | 837.0598 | ±1674.1197 | -0.573 | 0.5667 |  |
| High cholesterol | +34.3131 | 802.0112 | ±1604.0224 | +0.043 | 0.9659 |  |
| Kidney disease | -1364.3994 | 928.6853 | ±1857.3706 | -1.469 | 0.1418 |  |
| **Circulatory disease** | **-1481.1694** | 681.1695 | ±1362.3391 | **-2.174** | **0.0297** | * |
| Avg. daily time > 180 (%) | -13.5228 | 18.7363 | ±37.4726 | -0.722 | 0.4705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2073**, Adj R² = **0.1612**, F-statistic = **4.49** (p = **4.99e-06**), Residual SE = **4760.072** on **189** df, AIC = **3986.2**, BIC = **4025.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21055.0947** | 2848.4118 | ±5696.8237 | **+7.392** | **1.45e-13** | *** |
| Education: graduate level (vs college) | -1168.7324 | 742.3009 | ±1484.6018 | -1.574 | 0.1154 |  |
| Education: high school or below (vs college) | +681.3817 | 1138.6277 | ±2277.2554 | +0.598 | 0.5496 |  |
| Site: UCSD (vs UAB) | +283.6155 | 912.5654 | ±1825.1308 | +0.311 | 0.7560 |  |
| Site: UW (vs UAB) | +1015.2296 | 847.3582 | ±1694.7164 | +1.198 | 0.2309 |  |
| **Age (years)** | **-164.2115** | 31.4037 | ±62.8074 | **-5.229** | **1.70e-07** | *** |
| BMI (kg/m2) | -22.8338 | 47.3065 | ±94.6130 | -0.483 | 0.6293 |  |
| Hypertension | -438.1124 | 838.5314 | ±1677.0629 | -0.522 | 0.6013 |  |
| High cholesterol | +39.8841 | 802.7117 | ±1605.4234 | +0.050 | 0.9604 |  |
| Kidney disease | -1408.8518 | 930.4915 | ±1860.9831 | -1.514 | 0.1300 |  |
| **Circulatory disease** | **-1461.3619** | 682.9314 | ±1365.8627 | **-2.140** | **0.0324** | * |
| Nocturnal time > 180 (%) | -14.9065 | 19.2261 | ±38.4522 | -0.775 | 0.4381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2065**, Adj R² = **0.1603**, F-statistic = **4.47** (p = **5.39e-06**), Residual SE = **4762.447** on **189** df, AIC = **3986.4**, BIC = **4026.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20807.0460** | 2838.2566 | ±5676.5132 | **+7.331** | **2.29e-13** | *** |
| Education: graduate level (vs college) | -1042.2967 | 758.7238 | ±1517.4476 | -1.374 | 0.1695 |  |
| Education: high school or below (vs college) | +630.6617 | 1142.1127 | ±2284.2254 | +0.552 | 0.5808 |  |
| Site: UCSD (vs UAB) | +276.8165 | 883.3546 | ±1766.7091 | +0.313 | 0.7540 |  |
| Site: UW (vs UAB) | +987.1419 | 818.4685 | ±1636.9370 | +1.206 | 0.2278 |  |
| **Age (years)** | **-168.4986** | 31.2630 | ±62.5260 | **-5.390** | **7.06e-08** | *** |
| BMI (kg/m2) | -18.8432 | 49.1256 | ±98.2512 | -0.384 | 0.7013 |  |
| Hypertension | -445.4620 | 839.2093 | ±1678.4187 | -0.531 | 0.5955 |  |
| High cholesterol | -9.1527 | 802.8200 | ±1605.6400 | -0.011 | 0.9909 |  |
| Kidney disease | -1585.8557 | 922.8880 | ±1845.7760 | -1.718 | 0.0857 | . |
| **Circulatory disease** | **-1511.4282** | 674.5802 | ±1349.1604 | **-2.241** | **0.0251** | * |
| Any reading > 250 during wear (0/1) | +501.1215 | 753.8858 | ±1507.7716 | +0.665 | 0.5062 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2084**, Adj R² = **0.1624**, F-statistic = **4.52** (p = **4.47e-06**), Residual SE = **4756.733** on **189** df, AIC = **3985.9**, BIC = **4025.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21143.0069** | 2830.5218 | ±5661.0437 | **+7.470** | **8.04e-14** | *** |
| Education: graduate level (vs college) | -1174.4142 | 739.3902 | ±1478.7804 | -1.588 | 0.1122 |  |
| Education: high school or below (vs college) | +738.7173 | 1130.7209 | ±2261.4418 | +0.653 | 0.5136 |  |
| Site: UCSD (vs UAB) | +261.9058 | 902.4817 | ±1804.9634 | +0.290 | 0.7717 |  |
| Site: UW (vs UAB) | +975.0563 | 849.7371 | ±1699.4743 | +1.147 | 0.2512 |  |
| **Age (years)** | **-164.6247** | 31.3891 | ±62.7782 | **-5.245** | **1.57e-07** | *** |
| BMI (kg/m2) | -24.3852 | 47.3383 | ±94.6767 | -0.515 | 0.6065 |  |
| Hypertension | -447.6622 | 836.9064 | ±1673.8128 | -0.535 | 0.5927 |  |
| High cholesterol | -22.1233 | 796.5720 | ±1593.1441 | -0.028 | 0.9778 |  |
| Kidney disease | -1393.1137 | 925.3790 | ±1850.7581 | -1.505 | 0.1322 |  |
| **Circulatory disease** | **-1463.8171** | 684.3174 | ±1368.6349 | **-2.139** | **0.0324** | * |
| Time > 250 (%) | -35.5867 | 34.8488 | ±69.6976 | -1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 201)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2064**, Adj R² = **0.1602**, F-statistic = **4.47** (p = **5.49e-06**), Residual SE = **4762.974** on **189** df, AIC = **3986.4**, BIC = **4026.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21068.3865** | 2832.2355 | ±5664.4710 | **+7.439** | **1.02e-13** | *** |
| Education: graduate level (vs college) | -1159.2087 | 739.9636 | ±1479.9272 | -1.567 | 0.1172 |  |
| Education: high school or below (vs college) | +725.5115 | 1130.7506 | ±2261.5013 | +0.642 | 0.5211 |  |
| Site: UCSD (vs UAB) | +273.4279 | 899.2896 | ±1798.5792 | +0.304 | 0.7611 |  |
| Site: UW (vs UAB) | +999.1821 | 849.9874 | ±1699.9747 | +1.176 | 0.2398 |  |
| **Age (years)** | **-164.2932** | 31.3702 | ±62.7404 | **-5.237** | **1.63e-07** | *** |
| BMI (kg/m2) | -24.2330 | 47.5602 | ±95.1204 | -0.510 | 0.6104 |  |
| Hypertension | -448.2594 | 838.5808 | ±1677.1616 | -0.535 | 0.5930 |  |
| High cholesterol | -9.4874 | 797.8774 | ±1595.7547 | -0.012 | 0.9905 |  |
| Kidney disease | -1405.9134 | 920.9515 | ±1841.9031 | -1.527 | 0.1269 |  |
| **Circulatory disease** | **-1470.5978** | 686.1013 | ±1372.2025 | **-2.143** | **0.0321** | * |
| Avg. daily time > 250 (%) | -27.5861 | 39.1825 | ±78.3651 | -0.704 | 0.4814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 201; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **201**, R² = **0.2272**, Adj R² = **0.1865**, F-statistic = **5.59** (p = **2.70e-07**), Residual SE = **13.517** on **190** df, AIC = **1627.9**, BIC = **1664.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3720** | 8.2431 | ±16.4862 | **+6.596** | **4.22e-11** | *** |
| Education: graduate level (vs college) | -2.9585 | 2.0743 | ±4.1485 | -1.426 | 0.1538 |  |
| Education: high school or below (vs college) | +4.2385 | 3.3740 | ±6.7480 | +1.256 | 0.2090 |  |
| Site: UCSD (vs UAB) | -0.3659 | 2.6696 | ±5.3392 | -0.137 | 0.8910 |  |
| Site: UW (vs UAB) | +2.6003 | 2.3469 | ±4.6939 | +1.108 | 0.2679 |  |
| **Age (years)** | **-0.4882** | 0.0881 | ±0.1763 | **-5.539** | **3.04e-08** | *** |
| BMI (kg/m2) | +0.0393 | 0.1327 | ±0.2655 | +0.296 | 0.7672 |  |
| Hypertension | -1.3215 | 2.4658 | ±4.9315 | -0.536 | 0.5920 |  |
| High cholesterol | -0.1246 | 2.2450 | ±4.4900 | -0.056 | 0.9557 |  |
| Kidney disease | -4.0670 | 2.5958 | ±5.1916 | -1.567 | 0.1172 |  |
| Circulatory disease | -3.5393 | 2.0091 | ±4.0181 | -1.762 | 0.0781 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **201**, R² = **0.2403**, Adj R² = **0.1961**, F-statistic = **5.43** (p = **1.69e-07**), Residual SE = **13.437** on **189** df, AIC = **1626.5**, BIC = **1666.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2971** | 10.4016 | ±20.8032 | **+4.451** | **8.55e-06** | *** |
| Education: graduate level (vs college) | -2.4459 | 2.1586 | ±4.3172 | -1.133 | 0.2572 |  |
| Education: high school or below (vs college) | +3.8875 | 3.3146 | ±6.6291 | +1.173 | 0.2409 |  |
| Site: UCSD (vs UAB) | -0.1276 | 2.6404 | ±5.2808 | -0.048 | 0.9615 |  |
| Site: UW (vs UAB) | +2.7645 | 2.3535 | ±4.7071 | +1.175 | 0.2401 |  |
| **Age (years)** | **-0.5171** | 0.0898 | ±0.1796 | **-5.759** | **8.46e-09** | *** |
| BMI (kg/m2) | +0.0293 | 0.1311 | ±0.2622 | +0.224 | 0.8230 |  |
| Hypertension | -1.3401 | 2.4652 | ±4.9304 | -0.544 | 0.5867 |  |
| High cholesterol | -0.0201 | 2.2124 | ±4.4248 | -0.009 | 0.9928 |  |
| Kidney disease | -4.0920 | 2.4355 | ±4.8709 | -1.680 | 0.0929 | . |
| Circulatory disease | -3.4882 | 1.9792 | ±3.9584 | -1.762 | 0.0780 | . |
| HbA1c (%) | +1.5433 | 1.1801 | ±2.3603 | +1.308 | 0.1910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **201**, R² = **0.2274**, Adj R² = **0.1825**, F-statistic = **5.06** (p = **6.52e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.3528** | 10.2726 | ±20.5452 | **+5.388** | **7.11e-08** | *** |
| Education: graduate level (vs college) | -2.9881 | 2.0921 | ±4.1842 | -1.428 | 0.1532 |  |
| Education: high school or below (vs college) | +4.2764 | 3.3956 | ±6.7913 | +1.259 | 0.2079 |  |
| Site: UCSD (vs UAB) | -0.3691 | 2.7092 | ±5.4183 | -0.136 | 0.8916 |  |
| Site: UW (vs UAB) | +2.5827 | 2.3666 | ±4.7331 | +1.091 | 0.2751 |  |
| **Age (years)** | **-0.4875** | 0.0882 | ±0.1764 | **-5.528** | **3.23e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.1335 | ±0.2670 | +0.293 | 0.7698 |  |
| Hypertension | -1.3285 | 2.4801 | ±4.9603 | -0.536 | 0.5922 |  |
| High cholesterol | -0.1224 | 2.2601 | ±4.5202 | -0.054 | 0.9568 |  |
| Kidney disease | -4.0048 | 2.6105 | ±5.2211 | -1.534 | 0.1250 |  |
| Circulatory disease | -3.5216 | 2.0356 | ±4.0712 | -1.730 | 0.0836 | . |
| Mean glucose (mg/dL) | -0.0074 | 0.0348 | ±0.0696 | -0.214 | 0.8309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **201**, R² = **0.2274**, Adj R² = **0.1825**, F-statistic = **5.06** (p = **6.52e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.3813** | 13.7699 | ±27.5397 | **+4.095** | **4.23e-05** | *** |
| Education: graduate level (vs college) | -2.9881 | 2.0921 | ±4.1842 | -1.428 | 0.1532 |  |
| Education: high school or below (vs college) | +4.2764 | 3.3956 | ±6.7913 | +1.259 | 0.2079 |  |
| Site: UCSD (vs UAB) | -0.3691 | 2.7092 | ±5.4183 | -0.136 | 0.8916 |  |
| Site: UW (vs UAB) | +2.5827 | 2.3666 | ±4.7331 | +1.091 | 0.2751 |  |
| **Age (years)** | **-0.4875** | 0.0882 | ±0.1764 | **-5.528** | **3.23e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.1335 | ±0.2670 | +0.293 | 0.7698 |  |
| Hypertension | -1.3285 | 2.4801 | ±4.9603 | -0.536 | 0.5922 |  |
| High cholesterol | -0.1224 | 2.2601 | ±4.5202 | -0.054 | 0.9568 |  |
| Kidney disease | -4.0048 | 2.6105 | ±5.2211 | -1.534 | 0.1250 |  |
| Circulatory disease | -3.5216 | 2.0356 | ±4.0712 | -1.730 | 0.0836 | . |
| GMI (%) | -0.3107 | 1.4550 | ±2.9101 | -0.214 | 0.8309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **201**, R² = **0.2276**, Adj R² = **0.1826**, F-statistic = **5.06** (p = **6.43e-07**), Residual SE = **13.549** on **189** df, AIC = **1629.8**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.1845** | 10.1213 | ±20.2427 | **+5.255** | **1.48e-07** | *** |
| Education: graduate level (vs college) | -2.9524 | 2.0829 | ±4.1658 | -1.417 | 0.1564 |  |
| Education: high school or below (vs college) | +4.1919 | 3.3966 | ±6.7933 | +1.234 | 0.2172 |  |
| Site: UCSD (vs UAB) | -0.3744 | 2.6740 | ±5.3481 | -0.140 | 0.8887 |  |
| Site: UW (vs UAB) | +2.6081 | 2.3586 | ±4.7172 | +1.106 | 0.2688 |  |
| **Age (years)** | **-0.4870** | 0.0892 | ±0.1784 | **-5.458** | **4.81e-08** | *** |
| BMI (kg/m2) | +0.0387 | 0.1333 | ±0.2665 | +0.290 | 0.7716 |  |
| Hypertension | -1.3414 | 2.4805 | ±4.9610 | -0.541 | 0.5887 |  |
| High cholesterol | -0.1383 | 2.2631 | ±4.5263 | -0.061 | 0.9513 |  |
| Kidney disease | -4.0859 | 2.5941 | ±5.1883 | -1.575 | 0.1152 |  |
| Circulatory disease | -3.5669 | 2.0233 | ±4.0465 | -1.763 | 0.0779 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0089 | 0.0337 | ±0.0673 | +0.265 | 0.7908 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2303**, Adj R² = **0.1855**, F-statistic = **5.14** (p = **4.86e-07**), Residual SE = **13.526** on **189** df, AIC = **1629.1**, BIC = **1668.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.6072** | 8.5579 | ±17.1159 | **+6.498** | **8.15e-11** | *** |
| Education: graduate level (vs college) | -3.2188 | 2.0979 | ±4.1957 | -1.534 | 0.1250 |  |
| Education: high school or below (vs college) | +4.5882 | 3.3785 | ±6.7571 | +1.358 | 0.1744 |  |
| Site: UCSD (vs UAB) | -0.4262 | 2.7277 | ±5.4554 | -0.156 | 0.8758 |  |
| Site: UW (vs UAB) | +2.4852 | 2.3649 | ±4.7299 | +1.051 | 0.2933 |  |
| **Age (years)** | **-0.4734** | 0.0895 | ±0.1790 | **-5.289** | **1.23e-07** | *** |
| BMI (kg/m2) | +0.0339 | 0.1340 | ±0.2681 | +0.253 | 0.8003 |  |
| Hypertension | -1.3733 | 2.4675 | ±4.9350 | -0.557 | 0.5778 |  |
| High cholesterol | -0.1338 | 2.2545 | ±4.5091 | -0.059 | 0.9527 |  |
| Kidney disease | -3.5474 | 2.5968 | ±5.1936 | -1.366 | 0.1719 |  |
| Circulatory disease | -3.5786 | 2.0515 | ±4.1029 | -1.744 | 0.0811 | . |
| Glucose SD, pooled (mg/dL) | -0.0562 | 0.0690 | ±0.1381 | -0.815 | 0.4152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2339**, Adj R² = **0.1893**, F-statistic = **5.24** (p = **3.34e-07**), Residual SE = **13.494** on **189** df, AIC = **1628.1**, BIC = **1667.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.4173** | 8.5777 | ±17.1555 | **+6.577** | **4.79e-11** | *** |
| Education: graduate level (vs college) | -3.3534 | 2.0997 | ±4.1995 | -1.597 | 0.1103 |  |
| Education: high school or below (vs college) | +4.8581 | 3.3519 | ±6.7039 | +1.449 | 0.1472 |  |
| Site: UCSD (vs UAB) | -0.4760 | 2.7206 | ±5.4412 | -0.175 | 0.8611 |  |
| Site: UW (vs UAB) | +2.4620 | 2.3533 | ±4.7066 | +1.046 | 0.2955 |  |
| **Age (years)** | **-0.4665** | 0.0879 | ±0.1758 | **-5.308** | **1.11e-07** | *** |
| BMI (kg/m2) | +0.0278 | 0.1341 | ±0.2681 | +0.208 | 0.8355 |  |
| Hypertension | -1.4377 | 2.4588 | ±4.9175 | -0.585 | 0.5587 |  |
| High cholesterol | -0.0925 | 2.2456 | ±4.4913 | -0.041 | 0.9671 |  |
| Kidney disease | -3.2923 | 2.5938 | ±5.1876 | -1.269 | 0.2043 |  |
| Circulatory disease | -3.6261 | 2.0456 | ±4.0912 | -1.773 | 0.0763 | . |
| Avg. daily SD (mg/dL) | -0.0982 | 0.0734 | ±0.1467 | -1.338 | 0.1807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **201**, R² = **0.2311**, Adj R² = **0.1864**, F-statistic = **5.16** (p = **4.45e-07**), Residual SE = **13.518** on **189** df, AIC = **1628.9**, BIC = **1668.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6127** | 8.4889 | ±16.9778 | **+6.669** | **2.58e-11** | *** |
| Education: graduate level (vs college) | -3.3297 | 2.0930 | ±4.1861 | -1.591 | 0.1117 |  |
| Education: high school or below (vs college) | +4.7677 | 3.3652 | ±6.7304 | +1.417 | 0.1566 |  |
| Site: UCSD (vs UAB) | -0.4132 | 2.6829 | ±5.3658 | -0.154 | 0.8776 |  |
| Site: UW (vs UAB) | +2.4594 | 2.3618 | ±4.7237 | +1.041 | 0.2977 |  |
| **Age (years)** | **-0.4602** | 0.0934 | ±0.1869 | **-4.925** | **8.42e-07** | *** |
| BMI (kg/m2) | +0.0314 | 0.1343 | ±0.2687 | +0.234 | 0.8152 |  |
| Hypertension | -1.4031 | 2.4603 | ±4.9206 | -0.570 | 0.5685 |  |
| High cholesterol | -0.1172 | 2.2517 | ±4.5034 | -0.052 | 0.9585 |  |
| Kidney disease | -3.3574 | 2.5648 | ±5.1295 | -1.309 | 0.1905 |  |
| Circulatory disease | -3.6398 | 2.0379 | ±4.0758 | -1.786 | 0.0741 | . |
| CV (%) | -0.1498 | 0.1340 | ±0.2681 | -1.117 | 0.2639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **201**, R² = **0.2275**, Adj R² = **0.1825**, F-statistic = **5.06** (p = **6.51e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0602** | 9.4996 | ±18.9991 | **+5.586** | **2.33e-08** | *** |
| Education: graduate level (vs college) | -3.0485 | 2.1105 | ±4.2211 | -1.444 | 0.1486 |  |
| Education: high school or below (vs college) | +4.3795 | 3.3758 | ±6.7516 | +1.297 | 0.1945 |  |
| Site: UCSD (vs UAB) | -0.3508 | 2.6789 | ±5.3578 | -0.131 | 0.8958 |  |
| Site: UW (vs UAB) | +2.5828 | 2.3602 | ±4.7204 | +1.094 | 0.2738 |  |
| **Age (years)** | **-0.4805** | 0.0938 | ±0.1876 | **-5.123** | **3.01e-07** | *** |
| BMI (kg/m2) | +0.0385 | 0.1337 | ±0.2675 | +0.288 | 0.7735 |  |
| Hypertension | -1.3493 | 2.4675 | ±4.9351 | -0.547 | 0.5845 |  |
| High cholesterol | -0.1239 | 2.2536 | ±4.5071 | -0.055 | 0.9561 |  |
| Kidney disease | -3.9434 | 2.6042 | ±5.2085 | -1.514 | 0.1300 |  |
| Circulatory disease | -3.5327 | 2.0200 | ±4.0400 | -1.749 | 0.0803 | . |
| Mean / SD ratio | +0.1959 | 0.6449 | ±1.2899 | +0.304 | 0.7613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **201**, R² = **0.2278**, Adj R² = **0.1828**, F-statistic = **5.07** (p = **6.29e-07**), Residual SE = **13.547** on **189** df, AIC = **1629.7**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4769** | 9.3960 | ±18.7919 | **+5.585** | **2.34e-08** | *** |
| Education: graduate level (vs college) | -3.1006 | 2.1122 | ±4.2243 | -1.468 | 0.1421 |  |
| Education: high school or below (vs college) | +4.4511 | 3.3389 | ±6.6778 | +1.333 | 0.1825 |  |
| Site: UCSD (vs UAB) | -0.3313 | 2.6784 | ±5.3569 | -0.124 | 0.9016 |  |
| Site: UW (vs UAB) | +2.5959 | 2.3563 | ±4.7125 | +1.102 | 0.2706 |  |
| **Age (years)** | **-0.4768** | 0.0934 | ±0.1867 | **-5.107** | **3.27e-07** | *** |
| BMI (kg/m2) | +0.0372 | 0.1337 | ±0.2674 | +0.279 | 0.7806 |  |
| Hypertension | -1.3823 | 2.4649 | ±4.9297 | -0.561 | 0.5749 |  |
| High cholesterol | -0.0940 | 2.2621 | ±4.5243 | -0.042 | 0.9668 |  |
| Kidney disease | -3.9438 | 2.6042 | ±5.2084 | -1.514 | 0.1299 |  |
| Circulatory disease | -3.5406 | 2.0167 | ±4.0334 | -1.756 | 0.0792 | . |
| Avg. daily mean/SD | +0.2406 | 0.5022 | ±1.0045 | +0.479 | 0.6319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **201**, R² = **0.2272**, Adj R² = **0.1823**, F-statistic = **5.05** (p = **6.66e-07**), Residual SE = **13.552** on **189** df, AIC = **1629.9**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.0366** | 9.5287 | ±19.0573 | **+5.671** | **1.42e-08** | *** |
| Education: graduate level (vs college) | -2.9340 | 2.1127 | ±4.2254 | -1.389 | 0.1649 |  |
| Education: high school or below (vs college) | +4.1915 | 3.3864 | ±6.7728 | +1.238 | 0.2158 |  |
| Site: UCSD (vs UAB) | -0.3763 | 2.6784 | ±5.3569 | -0.140 | 0.8883 |  |
| Site: UW (vs UAB) | +2.6249 | 2.3750 | ±4.7500 | +1.105 | 0.2691 |  |
| **Age (years)** | **-0.4891** | 0.0881 | ±0.1762 | **-5.551** | **2.83e-08** | *** |
| BMI (kg/m2) | +0.0380 | 0.1326 | ±0.2651 | +0.287 | 0.7742 |  |
| Hypertension | -1.3075 | 2.4894 | ±4.9788 | -0.525 | 0.5994 |  |
| High cholesterol | -0.1357 | 2.2766 | ±4.5531 | -0.060 | 0.9525 |  |
| Kidney disease | -4.0744 | 2.6142 | ±5.2284 | -1.559 | 0.1191 |  |
| Circulatory disease | -3.5378 | 2.0279 | ±4.0559 | -1.745 | 0.0811 | . |
| MAG (mg/dL/h) | +0.0096 | 0.1063 | ±0.2126 | +0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **201**, R² = **0.2309**, Adj R² = **0.1861**, F-statistic = **5.16** (p = **4.55e-07**), Residual SE = **13.520** on **189** df, AIC = **1628.9**, BIC = **1668.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.5532** | 8.9259 | ±17.8517 | **+6.336** | **2.36e-10** | *** |
| Education: graduate level (vs college) | -3.2653 | 2.1091 | ±4.2183 | -1.548 | 0.1216 |  |
| Education: high school or below (vs college) | +4.7506 | 3.3692 | ±6.7385 | +1.410 | 0.1585 |  |
| Site: UCSD (vs UAB) | -0.3981 | 2.7157 | ±5.4314 | -0.147 | 0.8835 |  |
| Site: UW (vs UAB) | +2.5306 | 2.3588 | ±4.7175 | +1.073 | 0.2833 |  |
| **Age (years)** | **-0.4731** | 0.0880 | ±0.1761 | **-5.374** | **7.70e-08** | *** |
| BMI (kg/m2) | +0.0305 | 0.1348 | ±0.2696 | +0.226 | 0.8210 |  |
| Hypertension | -1.4533 | 2.4685 | ±4.9369 | -0.589 | 0.5560 |  |
| High cholesterol | -0.0534 | 2.2569 | ±4.5138 | -0.024 | 0.9811 |  |
| Kidney disease | -3.4952 | 2.5835 | ±5.1670 | -1.353 | 0.1761 |  |
| Circulatory disease | -3.5385 | 2.0319 | ±4.0638 | -1.742 | 0.0816 | . |
| Avg. daily range (mg/dL) | -0.0206 | 0.0220 | ±0.0441 | -0.936 | 0.3490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **201**, R² = **0.2283**, Adj R² = **0.1834**, F-statistic = **5.08** (p = **5.94e-07**), Residual SE = **13.543** on **189** df, AIC = **1629.6**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.9723** | 8.3857 | ±16.7714 | **+6.436** | **1.22e-10** | *** |
| Education: graduate level (vs college) | -2.7977 | 2.1350 | ±4.2701 | -1.310 | 0.1901 |  |
| Education: high school or below (vs college) | +4.2288 | 3.3961 | ±6.7922 | +1.245 | 0.2131 |  |
| Site: UCSD (vs UAB) | -0.3655 | 2.6817 | ±5.3633 | -0.136 | 0.8916 |  |
| Site: UW (vs UAB) | +2.6752 | 2.3812 | ±4.7623 | +1.124 | 0.2612 |  |
| **Age (years)** | **-0.4934** | 0.0893 | ±0.1786 | **-5.525** | **3.29e-08** | *** |
| BMI (kg/m2) | +0.0410 | 0.1339 | ±0.2679 | +0.306 | 0.7598 |  |
| Hypertension | -1.3873 | 2.4884 | ±4.9769 | -0.558 | 0.5772 |  |
| High cholesterol | -0.0941 | 2.2457 | ±4.4913 | -0.042 | 0.9666 |  |
| Kidney disease | -4.2798 | 2.5704 | ±5.1408 | -1.665 | 0.0959 | . |
| Circulatory disease | -3.6043 | 2.0125 | ±4.0251 | -1.791 | 0.0733 | . |
| SD of daily means (mg/dL) | +0.0539 | 0.1256 | ±0.2512 | +0.430 | 0.6675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **201**, R² = **0.2288**, Adj R² = **0.1839**, F-statistic = **5.10** (p = **5.65e-07**), Residual SE = **13.538** on **189** df, AIC = **1629.5**, BIC = **1669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3736** | 8.9530 | ±17.9061 | **+5.738** | **9.57e-09** | *** |
| Education: graduate level (vs college) | -3.1541 | 2.1085 | ±4.2169 | -1.496 | 0.1347 |  |
| Education: high school or below (vs college) | +4.3274 | 3.3968 | ±6.7937 | +1.274 | 0.2027 |  |
| Site: UCSD (vs UAB) | -0.4264 | 2.7677 | ±5.5354 | -0.154 | 0.8776 |  |
| Site: UW (vs UAB) | +2.5239 | 2.3628 | ±4.7256 | +1.068 | 0.2854 |  |
| **Age (years)** | **-0.4832** | 0.0880 | ±0.1761 | **-5.489** | **4.05e-08** | *** |
| BMI (kg/m2) | +0.0363 | 0.1346 | ±0.2693 | +0.270 | 0.7874 |  |
| Hypertension | -1.3889 | 2.4747 | ±4.9494 | -0.561 | 0.5746 |  |
| High cholesterol | -0.0566 | 2.2713 | ±4.5425 | -0.025 | 0.9801 |  |
| Kidney disease | -3.8117 | 2.6343 | ±5.2686 | -1.447 | 0.1479 |  |
| Circulatory disease | -3.4554 | 2.0376 | ±4.0751 | -1.696 | 0.0899 | . |
| Time in range 70-180, pooled (%) | +0.0339 | 0.0614 | ±0.1228 | +0.552 | 0.5807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **201**, R² = **0.2288**, Adj R² = **0.1839**, F-statistic = **5.10** (p = **5.68e-07**), Residual SE = **13.539** on **189** df, AIC = **1629.5**, BIC = **1669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4333** | 8.9759 | ±17.9518 | **+5.730** | **1.00e-08** | *** |
| Education: graduate level (vs college) | -3.1503 | 2.1070 | ±4.2140 | -1.495 | 0.1349 |  |
| Education: high school or below (vs college) | +4.3430 | 3.3991 | ±6.7983 | +1.278 | 0.2014 |  |
| Site: UCSD (vs UAB) | -0.4343 | 2.7698 | ±5.5396 | -0.157 | 0.8754 |  |
| Site: UW (vs UAB) | +2.5186 | 2.3632 | ±4.7265 | +1.066 | 0.2865 |  |
| **Age (years)** | **-0.4833** | 0.0881 | ±0.1761 | **-5.488** | **4.07e-08** | *** |
| BMI (kg/m2) | +0.0356 | 0.1347 | ±0.2695 | +0.264 | 0.7914 |  |
| Hypertension | -1.3961 | 2.4768 | ±4.9536 | -0.564 | 0.5730 |  |
| High cholesterol | -0.0547 | 2.2742 | ±4.5483 | -0.024 | 0.9808 |  |
| Kidney disease | -3.8089 | 2.6290 | ±5.2579 | -1.449 | 0.1474 |  |
| Circulatory disease | -3.4508 | 2.0370 | ±4.0740 | -1.694 | 0.0903 | . |
| Avg. daily time in range 70-180 (%) | +0.0334 | 0.0612 | ±0.1223 | +0.546 | 0.5847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2307**, Adj R² = **0.1859**, F-statistic = **5.15** (p = **4.64e-07**), Residual SE = **13.522** on **189** df, AIC = **1629.0**, BIC = **1668.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.7477** | 8.2676 | ±16.5351 | **+6.622** | **3.54e-11** | *** |
| Education: graduate level (vs college) | -3.0844 | 2.0757 | ±4.1515 | -1.486 | 0.1373 |  |
| Education: high school or below (vs college) | +4.0403 | 3.3794 | ±6.7588 | +1.196 | 0.2319 |  |
| Site: UCSD (vs UAB) | -0.6224 | 2.6692 | ±5.3383 | -0.233 | 0.8156 |  |
| Site: UW (vs UAB) | +2.2559 | 2.3996 | ±4.7992 | +0.940 | 0.3472 |  |
| **Age (years)** | **-0.4860** | 0.0879 | ±0.1757 | **-5.531** | **3.19e-08** | *** |
| BMI (kg/m2) | +0.0410 | 0.1339 | ±0.2678 | +0.306 | 0.7593 |  |
| Hypertension | -1.2118 | 2.4635 | ±4.9270 | -0.492 | 0.6228 |  |
| High cholesterol | -0.0919 | 2.2452 | ±4.4903 | -0.041 | 0.9674 |  |
| Kidney disease | -4.1053 | 2.5882 | ±5.1764 | -1.586 | 0.1127 |  |
| Circulatory disease | -3.3420 | 2.0327 | ±4.0653 | -1.644 | 0.1001 |  |
| Time < 54 (%) | -1.1698 | 1.5336 | ±3.0672 | -0.763 | 0.4456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **201**, R² = **0.2331**, Adj R² = **0.1885**, F-statistic = **5.22** (p = **3.61e-07**), Residual SE = **13.501** on **189** df, AIC = **1628.3**, BIC = **1668.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4944** | 8.2209 | ±16.4418 | **+6.629** | **3.39e-11** | *** |
| Education: graduate level (vs college) | -3.1811 | 2.0882 | ±4.1764 | -1.523 | 0.1277 |  |
| Education: high school or below (vs college) | +3.9949 | 3.3776 | ±6.7552 | +1.183 | 0.2369 |  |
| Site: UCSD (vs UAB) | -0.6490 | 2.6710 | ±5.3420 | -0.243 | 0.8080 |  |
| Site: UW (vs UAB) | +2.2651 | 2.3848 | ±4.7697 | +0.950 | 0.3422 |  |
| **Age (years)** | **-0.4804** | 0.0885 | ±0.1770 | **-5.429** | **5.66e-08** | *** |
| BMI (kg/m2) | +0.0391 | 0.1326 | ±0.2652 | +0.295 | 0.7682 |  |
| Hypertension | -1.2430 | 2.4625 | ±4.9251 | -0.505 | 0.6137 |  |
| High cholesterol | -0.1852 | 2.2451 | ±4.4902 | -0.082 | 0.9343 |  |
| Kidney disease | -4.0305 | 2.5896 | ±5.1793 | -1.556 | 0.1196 |  |
| Circulatory disease | -3.2962 | 2.0273 | ±4.0545 | -1.626 | 0.1040 |  |
| Avg. daily time < 54 (%) | -1.3682 | 1.2412 | ±2.4824 | -1.102 | 0.2703 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **201**, R² = **0.2286**, Adj R² = **0.1837**, F-statistic = **5.09** (p = **5.79e-07**), Residual SE = **13.540** on **189** df, AIC = **1629.5**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4538** | 8.2628 | ±16.5256 | **+6.590** | **4.39e-11** | *** |
| Education: graduate level (vs college) | -3.1684 | 2.0718 | ±4.1435 | -1.529 | 0.1262 |  |
| Education: high school or below (vs college) | +4.2934 | 3.4016 | ±6.8033 | +1.262 | 0.2069 |  |
| Site: UCSD (vs UAB) | -0.4679 | 2.6436 | ±5.2872 | -0.177 | 0.8595 |  |
| Site: UW (vs UAB) | +2.5342 | 2.3521 | ±4.7043 | +1.077 | 0.2813 |  |
| **Age (years)** | **-0.4812** | 0.0900 | ±0.1801 | **-5.344** | **9.10e-08** | *** |
| BMI (kg/m2) | +0.0380 | 0.1341 | ±0.2683 | +0.283 | 0.7771 |  |
| Hypertension | -1.3459 | 2.4656 | ±4.9312 | -0.546 | 0.5852 |  |
| High cholesterol | -0.0872 | 2.2519 | ±4.5038 | -0.039 | 0.9691 |  |
| Kidney disease | -4.0368 | 2.5951 | ±5.1902 | -1.556 | 0.1198 |  |
| Circulatory disease | -3.5173 | 2.0180 | ±4.0361 | -1.743 | 0.0813 | . |
| Time 54-69, pooled (%) | -0.2254 | 0.2761 | ±0.5523 | -0.816 | 0.4144 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **201**, R² = **0.2291**, Adj R² = **0.1843**, F-statistic = **5.11** (p = **5.47e-07**), Residual SE = **13.535** on **189** df, AIC = **1629.4**, BIC = **1669.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3445** | 8.2822 | ±16.5644 | **+6.562** | **5.32e-11** | *** |
| Education: graduate level (vs college) | -3.1895 | 2.0721 | ±4.1442 | -1.539 | 0.1237 |  |
| Education: high school or below (vs college) | +4.3262 | 3.4061 | ±6.8122 | +1.270 | 0.2040 |  |
| Site: UCSD (vs UAB) | -0.4744 | 2.6444 | ±5.2889 | -0.179 | 0.8576 |  |
| Site: UW (vs UAB) | +2.5237 | 2.3564 | ±4.7128 | +1.071 | 0.2842 |  |
| **Age (years)** | **-0.4788** | 0.0907 | ±0.1815 | **-5.276** | **1.32e-07** | *** |
| BMI (kg/m2) | +0.0378 | 0.1338 | ±0.2676 | +0.283 | 0.7775 |  |
| Hypertension | -1.3453 | 2.4656 | ±4.9312 | -0.546 | 0.5853 |  |
| High cholesterol | -0.0905 | 2.2519 | ±4.5038 | -0.040 | 0.9679 |  |
| Kidney disease | -4.0302 | 2.5949 | ±5.1898 | -1.553 | 0.1204 |  |
| Circulatory disease | -3.5195 | 2.0182 | ±4.0365 | -1.744 | 0.0812 | . |
| Avg. daily time 54-69 (%) | -0.2504 | 0.2673 | ±0.5346 | -0.937 | 0.3489 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **201**, R² = **0.2293**, Adj R² = **0.1844**, F-statistic = **5.11** (p = **5.39e-07**), Residual SE = **13.534** on **189** df, AIC = **1629.3**, BIC = **1669.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.5264** | 8.2582 | ±16.5165 | **+6.603** | **4.04e-11** | *** |
| Education: graduate level (vs college) | -3.1930 | 2.0736 | ±4.1473 | -1.540 | 0.1236 |  |
| Education: high school or below (vs college) | +4.2552 | 3.3918 | ±6.7836 | +1.255 | 0.2096 |  |
| Site: UCSD (vs UAB) | -0.5175 | 2.6420 | ±5.2841 | -0.196 | 0.8447 |  |
| Site: UW (vs UAB) | +2.4677 | 2.3549 | ±4.7099 | +1.048 | 0.2947 |  |
| **Age (years)** | **-0.4808** | 0.0895 | ±0.1790 | **-5.371** | **7.83e-08** | *** |
| BMI (kg/m2) | +0.0383 | 0.1343 | ±0.2687 | +0.285 | 0.7755 |  |
| Hypertension | -1.3248 | 2.4583 | ±4.9167 | -0.539 | 0.5900 |  |
| High cholesterol | -0.0809 | 2.2497 | ±4.4995 | -0.036 | 0.9713 |  |
| Kidney disease | -4.0441 | 2.5908 | ±5.1816 | -1.561 | 0.1185 |  |
| Circulatory disease | -3.4792 | 2.0201 | ±4.0402 | -1.722 | 0.0850 | . |
| Time < 70 (%) | -0.2257 | 0.2325 | ±0.4651 | -0.971 | 0.3317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **201**, R² = **0.2303**, Adj R² = **0.1855**, F-statistic = **5.14** (p = **4.84e-07**), Residual SE = **13.525** on **189** df, AIC = **1629.1**, BIC = **1668.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3667** | 8.2693 | ±16.5386 | **+6.575** | **4.88e-11** | *** |
| Education: graduate level (vs college) | -3.2384 | 2.0774 | ±4.1548 | -1.559 | 0.1190 |  |
| Education: high school or below (vs college) | +4.2829 | 3.3925 | ±6.7850 | +1.262 | 0.2068 |  |
| Site: UCSD (vs UAB) | -0.5310 | 2.6438 | ±5.2875 | -0.201 | 0.8408 |  |
| Site: UW (vs UAB) | +2.4582 | 2.3606 | ±4.7212 | +1.041 | 0.2977 |  |
| **Age (years)** | **-0.4770** | 0.0903 | ±0.1807 | **-5.281** | **1.29e-07** | *** |
| BMI (kg/m2) | +0.0377 | 0.1337 | ±0.2674 | +0.282 | 0.7778 |  |
| Hypertension | -1.3312 | 2.4599 | ±4.9199 | -0.541 | 0.5884 |  |
| High cholesterol | -0.1009 | 2.2483 | ±4.4966 | -0.045 | 0.9642 |  |
| Kidney disease | -4.0222 | 2.5914 | ±5.1828 | -1.552 | 0.1206 |  |
| Circulatory disease | -3.4731 | 2.0196 | ±4.0392 | -1.720 | 0.0855 | . |
| Avg. daily time < 70 (%) | -0.2579 | 0.2233 | ±0.4466 | -1.155 | 0.2481 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2287**, Adj R² = **0.1838**, F-statistic = **5.09** (p = **5.72e-07**), Residual SE = **13.539** on **189** df, AIC = **1629.5**, BIC = **1669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5044** | 14.4216 | ±28.8432 | **+3.363** | **7.70e-04** | *** |
| Education: graduate level (vs college) | -3.0724 | 2.0799 | ±4.1599 | -1.477 | 0.1396 |  |
| Education: high school or below (vs college) | +4.3551 | 3.3992 | ±6.7984 | +1.281 | 0.2001 |  |
| Site: UCSD (vs UAB) | -0.4303 | 2.7516 | ±5.5032 | -0.156 | 0.8757 |  |
| Site: UW (vs UAB) | +2.4623 | 2.3665 | ±4.7329 | +1.041 | 0.2981 |  |
| **Age (years)** | **-0.4888** | 0.0885 | ±0.1770 | **-5.522** | **3.36e-08** | *** |
| BMI (kg/m2) | +0.0363 | 0.1334 | ±0.2667 | +0.272 | 0.7856 |  |
| Hypertension | -1.3116 | 2.4732 | ±4.9463 | -0.530 | 0.5959 |  |
| High cholesterol | -0.1748 | 2.2541 | ±4.5082 | -0.078 | 0.9382 |  |
| Kidney disease | -3.9393 | 2.6128 | ±5.2256 | -1.508 | 0.1316 |  |
| Circulatory disease | -3.4408 | 2.0515 | ±4.1029 | -1.677 | 0.0935 | . |
| Time 54-250, pooled (%) | +0.0629 | 0.1302 | ±0.2605 | +0.483 | 0.6289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **201**, R² = **0.2275**, Adj R² = **0.1826**, F-statistic = **5.06** (p = **6.46e-07**), Residual SE = **13.550** on **189** df, AIC = **1629.8**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2215** | 15.4750 | ±30.9500 | **+3.310** | **9.33e-04** | *** |
| Education: graduate level (vs college) | -3.0189 | 2.0844 | ±4.1689 | -1.448 | 0.1475 |  |
| Education: high school or below (vs college) | +4.3037 | 3.3986 | ±6.7972 | +1.266 | 0.2054 |  |
| Site: UCSD (vs UAB) | -0.3935 | 2.7390 | ±5.4779 | -0.144 | 0.8858 |  |
| Site: UW (vs UAB) | +2.5395 | 2.3660 | ±4.7320 | +1.073 | 0.2831 |  |
| **Age (years)** | **-0.4881** | 0.0885 | ±0.1771 | **-5.512** | **3.54e-08** | *** |
| BMI (kg/m2) | +0.0373 | 0.1338 | ±0.2676 | +0.279 | 0.7802 |  |
| Hypertension | -1.3176 | 2.4788 | ±4.9577 | -0.532 | 0.5950 |  |
| High cholesterol | -0.1464 | 2.2566 | ±4.5133 | -0.065 | 0.9483 |  |
| Kidney disease | -3.9928 | 2.5994 | ±5.1988 | -1.536 | 0.1245 |  |
| Circulatory disease | -3.4814 | 2.0464 | ±4.0928 | -1.701 | 0.0889 | . |
| Avg. daily time 54-250 (%) | +0.0334 | 0.1417 | ±0.2834 | +0.236 | 0.8136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2277**, Adj R² = **0.1828**, F-statistic = **5.07** (p = **6.35e-07**), Residual SE = **13.548** on **189** df, AIC = **1629.8**, BIC = **1669.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4972** | 8.3973 | ±16.7945 | **+6.490** | **8.59e-11** | *** |
| Education: graduate level (vs college) | -3.0445 | 2.1111 | ±4.2222 | -1.442 | 0.1493 |  |
| Education: high school or below (vs college) | +4.2534 | 3.3917 | ±6.7835 | +1.254 | 0.2098 |  |
| Site: UCSD (vs UAB) | -0.3747 | 2.7298 | ±5.4596 | -0.137 | 0.8908 |  |
| Site: UW (vs UAB) | +2.6068 | 2.3480 | ±4.6961 | +1.110 | 0.2669 |  |
| **Age (years)** | **-0.4846** | 0.0872 | ±0.1744 | **-5.558** | **2.72e-08** | *** |
| BMI (kg/m2) | +0.0383 | 0.1347 | ±0.2693 | +0.285 | 0.7760 |  |
| Hypertension | -1.3793 | 2.4656 | ±4.9313 | -0.559 | 0.5759 |  |
| High cholesterol | -0.0497 | 2.2842 | ±4.5684 | -0.022 | 0.9826 |  |
| Kidney disease | -3.9146 | 2.6467 | ±5.2935 | -1.479 | 0.1391 |  |
| Circulatory disease | -3.5162 | 2.0268 | ±4.0536 | -1.735 | 0.0828 | . |
| Time 181-250, pooled (%) | -0.0284 | 0.0886 | ±0.1773 | -0.320 | 0.7487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **201**, R² = **0.2285**, Adj R² = **0.1836**, F-statistic = **5.09** (p = **5.85e-07**), Residual SE = **13.541** on **189** df, AIC = **1629.5**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6553** | 8.4414 | ±16.8828 | **+6.475** | **9.50e-11** | *** |
| Education: graduate level (vs college) | -3.0899 | 2.1027 | ±4.2055 | -1.469 | 0.1417 |  |
| Education: high school or below (vs college) | +4.2745 | 3.3936 | ±6.7872 | +1.260 | 0.2078 |  |
| Site: UCSD (vs UAB) | -0.4003 | 2.7498 | ±5.4996 | -0.146 | 0.8843 |  |
| Site: UW (vs UAB) | +2.5863 | 2.3507 | ±4.7014 | +1.100 | 0.2712 |  |
| **Age (years)** | **-0.4836** | 0.0874 | ±0.1747 | **-5.536** | **3.10e-08** | *** |
| BMI (kg/m2) | +0.0373 | 0.1347 | ±0.2693 | +0.277 | 0.7816 |  |
| Hypertension | -1.4200 | 2.4684 | ±4.9367 | -0.575 | 0.5651 |  |
| High cholesterol | -0.0107 | 2.2817 | ±4.5633 | -0.005 | 0.9963 |  |
| Kidney disease | -3.8332 | 2.6443 | ±5.2886 | -1.450 | 0.1472 |  |
| Circulatory disease | -3.5028 | 2.0299 | ±4.0599 | -1.726 | 0.0844 | . |
| Avg. daily time 181-250 (%) | -0.0437 | 0.0845 | ±0.1690 | -0.517 | 0.6051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **201**, R² = **0.2282**, Adj R² = **0.1833**, F-statistic = **5.08** (p = **6.02e-07**), Residual SE = **13.544** on **189** df, AIC = **1629.6**, BIC = **1669.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6577** | 8.4334 | ±16.8667 | **+6.481** | **9.10e-11** | *** |
| Education: graduate level (vs college) | -3.0828 | 2.1009 | ±4.2019 | -1.467 | 0.1423 |  |
| Education: high school or below (vs college) | +4.3055 | 3.3936 | ±6.7873 | +1.269 | 0.2046 |  |
| Site: UCSD (vs UAB) | -0.3952 | 2.7476 | ±5.4953 | -0.144 | 0.8856 |  |
| Site: UW (vs UAB) | +2.5565 | 2.3589 | ±4.7178 | +1.084 | 0.2785 |  |
| **Age (years)** | **-0.4852** | 0.0880 | ±0.1760 | **-5.513** | **3.53e-08** | *** |
| BMI (kg/m2) | +0.0371 | 0.1345 | ±0.2690 | +0.276 | 0.7827 |  |
| Hypertension | -1.3734 | 2.4763 | ±4.9526 | -0.555 | 0.5792 |  |
| High cholesterol | -0.0769 | 2.2690 | ±4.5379 | -0.034 | 0.9729 |  |
| Kidney disease | -3.8717 | 2.6308 | ±5.2617 | -1.472 | 0.1411 |  |
| Circulatory disease | -3.4812 | 2.0363 | ±4.0726 | -1.710 | 0.0873 | . |
| Time > 180 (%) | -0.0263 | 0.0603 | ±0.1207 | -0.436 | 0.6631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2281**, Adj R² = **0.1831**, F-statistic = **5.08** (p = **6.12e-07**), Residual SE = **13.545** on **189** df, AIC = **1629.7**, BIC = **1669.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6653** | 8.4524 | ±16.9048 | **+6.467** | **9.97e-11** | *** |
| Education: graduate level (vs college) | -3.0711 | 2.1002 | ±4.2003 | -1.462 | 0.1436 |  |
| Education: high school or below (vs college) | +4.3100 | 3.3952 | ±6.7904 | +1.269 | 0.2043 |  |
| Site: UCSD (vs UAB) | -0.3999 | 2.7501 | ±5.5003 | -0.145 | 0.8844 |  |
| Site: UW (vs UAB) | +2.5545 | 2.3599 | ±4.7198 | +1.082 | 0.2791 |  |
| **Age (years)** | **-0.4857** | 0.0880 | ±0.1760 | **-5.518** | **3.42e-08** | *** |
| BMI (kg/m2) | +0.0368 | 0.1347 | ±0.2693 | +0.273 | 0.7847 |  |
| Hypertension | -1.3746 | 2.4778 | ±4.9556 | -0.555 | 0.5791 |  |
| High cholesterol | -0.0762 | 2.2716 | ±4.5432 | -0.034 | 0.9732 |  |
| Kidney disease | -3.8843 | 2.6241 | ±5.2482 | -1.480 | 0.1388 |  |
| Circulatory disease | -3.4814 | 2.0349 | ±4.0698 | -1.711 | 0.0871 | . |
| Avg. daily time > 180 (%) | -0.0242 | 0.0604 | ±0.1208 | -0.401 | 0.6886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **201**, R² = **0.2280**, Adj R² = **0.1830**, F-statistic = **5.07** (p = **6.18e-07**), Residual SE = **13.546** on **189** df, AIC = **1629.7**, BIC = **1669.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.5834** | 8.4011 | ±16.8021 | **+6.497** | **8.18e-11** | *** |
| Education: graduate level (vs college) | -3.0402 | 2.0854 | ±4.1707 | -1.458 | 0.1449 |  |
| Education: high school or below (vs college) | +4.2603 | 3.3989 | ±6.7978 | +1.253 | 0.2100 |  |
| Site: UCSD (vs UAB) | -0.3762 | 2.7475 | ±5.4949 | -0.137 | 0.8911 |  |
| Site: UW (vs UAB) | +2.5596 | 2.3544 | ±4.7088 | +1.087 | 0.2770 |  |
| **Age (years)** | **-0.4882** | 0.0885 | ±0.1770 | **-5.516** | **3.47e-08** | *** |
| BMI (kg/m2) | +0.0390 | 0.1334 | ±0.2668 | +0.292 | 0.7701 |  |
| Hypertension | -1.3039 | 2.4715 | ±4.9431 | -0.528 | 0.5978 |  |
| High cholesterol | -0.0761 | 2.2770 | ±4.5540 | -0.033 | 0.9734 |  |
| Kidney disease | -3.9812 | 2.6238 | ±5.2477 | -1.517 | 0.1292 |  |
| Circulatory disease | -3.4617 | 2.0337 | ±4.0675 | -1.702 | 0.0887 | . |
| Nocturnal time > 180 (%) | -0.0222 | 0.0638 | ±0.1275 | -0.348 | 0.7278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2284**, Adj R² = **0.1835**, F-statistic = **5.09** (p = **5.89e-07**), Residual SE = **13.542** on **189** df, AIC = **1629.6**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.1356** | 8.3542 | ±16.7083 | **+6.480** | **9.17e-11** | *** |
| Education: graduate level (vs college) | -2.7990 | 2.1293 | ±4.2587 | -1.314 | 0.1887 |  |
| Education: high school or below (vs college) | +4.1581 | 3.4085 | ±6.8170 | +1.220 | 0.2225 |  |
| Site: UCSD (vs UAB) | -0.3964 | 2.6643 | ±5.3287 | -0.149 | 0.8817 |  |
| Site: UW (vs UAB) | +2.4767 | 2.2927 | ±4.5853 | +1.080 | 0.2800 |  |
| **Age (years)** | **-0.4978** | 0.0883 | ±0.1765 | **-5.639** | **1.71e-08** | *** |
| BMI (kg/m2) | +0.0477 | 0.1381 | ±0.2762 | +0.346 | 0.7297 |  |
| Hypertension | -1.3116 | 2.4684 | ±4.9368 | -0.531 | 0.5952 |  |
| High cholesterol | -0.1612 | 2.2722 | ±4.5444 | -0.071 | 0.9434 |  |
| Kidney disease | -4.3331 | 2.5894 | ±5.1787 | -1.673 | 0.0942 | . |
| Circulatory disease | -3.5347 | 2.0166 | ±4.0331 | -1.753 | 0.0796 | . |
| Any reading > 250 during wear (0/1) | +1.1171 | 2.1523 | ±4.3046 | +0.519 | 0.6038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **201**, R² = **0.2284**, Adj R² = **0.1835**, F-statistic = **5.08** (p = **5.93e-07**), Residual SE = **13.542** on **189** df, AIC = **1629.6**, BIC = **1669.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.7317** | 8.3446 | ±16.6891 | **+6.559** | **5.42e-11** | *** |
| Education: graduate level (vs college) | -3.0533 | 2.0791 | ±4.1582 | -1.469 | 0.1420 |  |
| Education: high school or below (vs college) | +4.3511 | 3.4003 | ±6.8006 | +1.280 | 0.2007 |  |
| Site: UCSD (vs UAB) | -0.4107 | 2.7427 | ±5.4853 | -0.150 | 0.8810 |  |
| Site: UW (vs UAB) | +2.4946 | 2.3613 | ±4.7225 | +1.056 | 0.2907 |  |
| **Age (years)** | **-0.4888** | 0.0886 | ±0.1771 | **-5.520** | **3.39e-08** | *** |
| BMI (kg/m2) | +0.0365 | 0.1334 | ±0.2668 | +0.274 | 0.7841 |  |
| Hypertension | -1.3180 | 2.4763 | ±4.9527 | -0.532 | 0.5946 |  |
| High cholesterol | -0.1706 | 2.2549 | ±4.5099 | -0.076 | 0.9397 |  |
| Kidney disease | -3.9522 | 2.6121 | ±5.2242 | -1.513 | 0.1303 |  |
| Circulatory disease | -3.4616 | 2.0502 | ±4.1003 | -1.688 | 0.0913 | . |
| Time > 250 (%) | -0.0557 | 0.1309 | ±0.2617 | -0.426 | 0.6705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 201)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **201**, R² = **0.2273**, Adj R² = **0.1823**, F-statistic = **5.05** (p = **6.61e-07**), Residual SE = **13.552** on **189** df, AIC = **1629.9**, BIC = **1669.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4826** | 8.3513 | ±16.7026 | **+6.524** | **6.85e-11** | *** |
| Education: graduate level (vs college) | -2.9908 | 2.0825 | ±4.1649 | -1.436 | 0.1509 |  |
| Education: high school or below (vs college) | +4.2803 | 3.3981 | ±6.7962 | +1.260 | 0.2078 |  |
| Site: UCSD (vs UAB) | -0.3781 | 2.7273 | ±5.4547 | -0.139 | 0.8897 |  |
| Site: UW (vs UAB) | +2.5694 | 2.3616 | ±4.7231 | +1.088 | 0.2766 |  |
| **Age (years)** | **-0.4882** | 0.0886 | ±0.1771 | **-5.513** | **3.52e-08** | *** |
| BMI (kg/m2) | +0.0382 | 0.1338 | ±0.2677 | +0.285 | 0.7756 |  |
| Hypertension | -1.3203 | 2.4818 | ±4.9637 | -0.532 | 0.5947 |  |
| High cholesterol | -0.1366 | 2.2579 | ±4.5159 | -0.060 | 0.9518 |  |
| Kidney disease | -4.0239 | 2.5957 | ±5.1913 | -1.550 | 0.1211 |  |
| Circulatory disease | -3.5087 | 2.0425 | ±4.0850 | -1.718 | 0.0858 | . |
| Avg. daily time > 250 (%) | -0.0197 | 0.1417 | ±0.2835 | -0.139 | 0.8897 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 203; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1632**, F-statistic = **4.94** (p = **2.30e-06**), Residual SE = **7.894** on **192** df, AIC = **1425.6**, BIC = **1462.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8645** | 4.6906 | ±9.3813 | **+15.747** | **7.18e-56** | *** |
| **Education: graduate level (vs college)** | **-3.4724** | 1.3207 | ±2.6414 | **-2.629** | **0.0086** | ** |
| Education: high school or below (vs college) | -1.0447 | 1.5160 | ±3.0320 | -0.689 | 0.4908 |  |
| Site: UCSD (vs UAB) | -2.3582 | 1.4896 | ±2.9793 | -1.583 | 0.1134 |  |
| Site: UW (vs UAB) | +0.4190 | 1.5193 | ±3.0386 | +0.276 | 0.7827 |  |
| **Age (years)** | **-0.1835** | 0.0527 | ±0.1054 | **-3.481** | **4.99e-04** | *** |
| **BMI (kg/m2)** | **+0.1677** | 0.0727 | ±0.1455 | **+2.305** | **0.0211** | * |
| Hypertension | +0.5910 | 1.4383 | ±2.8766 | +0.411 | 0.6811 |  |
| High cholesterol | -0.2098 | 1.1606 | ±2.3212 | -0.181 | 0.8566 |  |
| Kidney disease | +0.7400 | 1.6563 | ±3.3125 | +0.447 | 0.6550 |  |
| Circulatory disease | -2.0248 | 1.3627 | ±2.7255 | -1.486 | 0.1373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **203**, R² = **0.2066**, Adj R² = **0.1609**, F-statistic = **4.52** (p = **4.46e-06**), Residual SE = **7.905** on **191** df, AIC = **1427.1**, BIC = **1466.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.0934** | 5.7682 | ±11.5364 | **+12.498** | **7.61e-36** | *** |
| **Education: graduate level (vs college)** | **-3.3602** | 1.3534 | ±2.7068 | **-2.483** | **0.0130** | * |
| Education: high school or below (vs college) | -1.1488 | 1.4884 | ±2.9768 | -0.772 | 0.4402 |  |
| Site: UCSD (vs UAB) | -2.3245 | 1.4879 | ±2.9758 | -1.562 | 0.1182 |  |
| Site: UW (vs UAB) | +0.4546 | 1.5225 | ±3.0449 | +0.299 | 0.7652 |  |
| **Age (years)** | **-0.1894** | 0.0530 | ±0.1060 | **-3.573** | **3.52e-04** | *** |
| **BMI (kg/m2)** | **+0.1655** | 0.0724 | ±0.1447 | **+2.287** | **0.0222** | * |
| Hypertension | +0.5803 | 1.4439 | ±2.8878 | +0.402 | 0.6878 |  |
| High cholesterol | -0.1817 | 1.1632 | ±2.3264 | -0.156 | 0.8758 |  |
| Kidney disease | +0.7362 | 1.6394 | ±3.2788 | +0.449 | 0.6534 |  |
| Circulatory disease | -2.0073 | 1.3715 | ±2.7429 | -1.464 | 0.1433 |  |
| HbA1c (%) | +0.3358 | 0.5894 | ±1.1789 | +0.570 | 0.5689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **203**, R² = **0.2052**, Adj R² = **0.1594**, F-statistic = **4.48** (p = **5.11e-06**), Residual SE = **7.912** on **191** df, AIC = **1427.5**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.0511** | 5.5213 | ±11.0426 | **+13.231** | **5.82e-40** | *** |
| **Education: graduate level (vs college)** | **-3.4467** | 1.3385 | ±2.6770 | **-2.575** | **0.0100** | * |
| Education: high school or below (vs college) | -1.0935 | 1.5139 | ±3.0279 | -0.722 | 0.4701 |  |
| Site: UCSD (vs UAB) | -2.3659 | 1.4945 | ±2.9891 | -1.583 | 0.1134 |  |
| Site: UW (vs UAB) | +0.4332 | 1.5241 | ±3.0481 | +0.284 | 0.7762 |  |
| **Age (years)** | **-0.1838** | 0.0528 | ±0.1056 | **-3.480** | **5.02e-04** | *** |
| **BMI (kg/m2)** | **+0.1679** | 0.0731 | ±0.1462 | **+2.297** | **0.0216** | * |
| Hypertension | +0.5932 | 1.4492 | ±2.8984 | +0.409 | 0.6823 |  |
| High cholesterol | -0.2090 | 1.1694 | ±2.3388 | -0.179 | 0.8581 |  |
| Kidney disease | +0.6898 | 1.6503 | ±3.3007 | +0.418 | 0.6760 |  |
| Circulatory disease | -2.0356 | 1.3799 | ±2.7598 | -1.475 | 0.1402 |  |
| Mean glucose (mg/dL) | +0.0061 | 0.0194 | ±0.0387 | +0.314 | 0.7537 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **203**, R² = **0.2052**, Adj R² = **0.1594**, F-statistic = **4.48** (p = **5.11e-06**), Residual SE = **7.912** on **191** df, AIC = **1427.5**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.2102** | 7.2940 | ±14.5881 | **+9.900** | **4.17e-23** | *** |
| **Education: graduate level (vs college)** | **-3.4467** | 1.3385 | ±2.6770 | **-2.575** | **0.0100** | * |
| Education: high school or below (vs college) | -1.0935 | 1.5139 | ±3.0279 | -0.722 | 0.4701 |  |
| Site: UCSD (vs UAB) | -2.3659 | 1.4945 | ±2.9891 | -1.583 | 0.1134 |  |
| Site: UW (vs UAB) | +0.4332 | 1.5241 | ±3.0481 | +0.284 | 0.7762 |  |
| **Age (years)** | **-0.1838** | 0.0528 | ±0.1056 | **-3.480** | **5.02e-04** | *** |
| **BMI (kg/m2)** | **+0.1679** | 0.0731 | ±0.1462 | **+2.297** | **0.0216** | * |
| Hypertension | +0.5932 | 1.4492 | ±2.8984 | +0.409 | 0.6823 |  |
| High cholesterol | -0.2090 | 1.1694 | ±2.3388 | -0.179 | 0.8581 |  |
| Kidney disease | +0.6898 | 1.6503 | ±3.3007 | +0.418 | 0.6760 |  |
| Circulatory disease | -2.0356 | 1.3799 | ±2.7598 | -1.475 | 0.1402 |  |
| GMI (%) | +0.2541 | 0.8097 | ±1.6195 | +0.314 | 0.7537 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **203**, R² = **0.2055**, Adj R² = **0.1597**, F-statistic = **4.49** (p = **4.96e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.8571** | 5.3942 | ±10.7883 | **+13.507** | **1.43e-41** | *** |
| **Education: graduate level (vs college)** | **-3.4651** | 1.3276 | ±2.6553 | **-2.610** | **0.0091** | ** |
| Education: high school or below (vs college) | -1.0996 | 1.5051 | ±3.0101 | -0.731 | 0.4650 |  |
| Site: UCSD (vs UAB) | -2.3736 | 1.4947 | ±2.9894 | -1.588 | 0.1123 |  |
| Site: UW (vs UAB) | +0.4254 | 1.5201 | ±3.0402 | +0.280 | 0.7796 |  |
| **Age (years)** | **-0.1823** | 0.0531 | ±0.1063 | **-3.431** | **6.02e-04** | *** |
| **BMI (kg/m2)** | **+0.1672** | 0.0729 | ±0.1458 | **+2.294** | **0.0218** | * |
| Hypertension | +0.5718 | 1.4538 | ±2.9076 | +0.393 | 0.6941 |  |
| High cholesterol | -0.2195 | 1.1674 | ±2.3348 | -0.188 | 0.8508 |  |
| Kidney disease | +0.7245 | 1.6385 | ±3.2770 | +0.442 | 0.6584 |  |
| Circulatory disease | -2.0450 | 1.3810 | ±2.7620 | -1.481 | 0.1387 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0075 | 0.0170 | ±0.0339 | +0.441 | 0.6591 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.01e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.2172** | 4.8309 | ±9.6619 | **+15.363** | **2.90e-53** | *** |
| **Education: graduate level (vs college)** | **-3.5459** | 1.3650 | ±2.7299 | **-2.598** | **0.0094** | ** |
| Education: high school or below (vs college) | -0.9284 | 1.5591 | ±3.1181 | -0.595 | 0.5515 |  |
| Site: UCSD (vs UAB) | -2.3633 | 1.4998 | ±2.9995 | -1.576 | 0.1151 |  |
| Site: UW (vs UAB) | +0.3876 | 1.5296 | ±3.0592 | +0.253 | 0.7999 |  |
| **Age (years)** | **-0.1797** | 0.0544 | ±0.1088 | **-3.303** | **9.58e-04** | *** |
| **BMI (kg/m2)** | **+0.1662** | 0.0740 | ±0.1480 | **+2.246** | **0.0247** | * |
| Hypertension | +0.5805 | 1.4408 | ±2.8817 | +0.403 | 0.6871 |  |
| High cholesterol | -0.2149 | 1.1676 | ±2.3351 | -0.184 | 0.8540 |  |
| Kidney disease | +0.8817 | 1.7250 | ±3.4500 | +0.511 | 0.6093 |  |
| Circulatory disease | -2.0396 | 1.3652 | ±2.7304 | -1.494 | 0.1352 |  |
| Glucose SD, pooled (mg/dL) | -0.0154 | 0.0447 | ±0.0895 | -0.345 | 0.7304 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **203**, R² = **0.2065**, Adj R² = **0.1608**, F-statistic = **4.52** (p = **4.50e-06**), Residual SE = **7.906** on **191** df, AIC = **1427.2**, BIC = **1466.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.4912** | 4.8591 | ±9.7183 | **+15.330** | **4.81e-53** | *** |
| **Education: graduate level (vs college)** | **-3.5920** | 1.3622 | ±2.7244 | **-2.637** | **0.0084** | ** |
| Education: high school or below (vs college) | -0.8284 | 1.5762 | ±3.1525 | -0.526 | 0.5992 |  |
| Site: UCSD (vs UAB) | -2.3715 | 1.5010 | ±3.0020 | -1.580 | 0.1141 |  |
| Site: UW (vs UAB) | +0.3782 | 1.5289 | ±3.0578 | +0.247 | 0.8046 |  |
| **Age (years)** | **-0.1775** | 0.0542 | ±0.1084 | **-3.277** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1643** | 0.0742 | ±0.1485 | **+2.214** | **0.0269** | * |
| Hypertension | +0.5631 | 1.4378 | ±2.8756 | +0.392 | 0.6953 |  |
| High cholesterol | -0.2051 | 1.1671 | ±2.3342 | -0.176 | 0.8605 |  |
| Kidney disease | +0.9681 | 1.7292 | ±3.4584 | +0.560 | 0.5756 |  |
| Circulatory disease | -2.0573 | 1.3619 | ±2.7238 | -1.511 | 0.1309 |  |
| Avg. daily SD (mg/dL) | -0.0291 | 0.0534 | ±0.1068 | -0.545 | 0.5858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **203**, R² = **0.2072**, Adj R² = **0.1616**, F-statistic = **4.54** (p = **4.18e-06**), Residual SE = **7.902** on **191** df, AIC = **1427.0**, BIC = **1466.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9233** | 4.9573 | ±9.9146 | **+15.114** | **1.31e-51** | *** |
| **Education: graduate level (vs college)** | **-3.6510** | 1.3812 | ±2.7624 | **-2.643** | **0.0082** | ** |
| Education: high school or below (vs college) | -0.7816 | 1.5583 | ±3.1165 | -0.502 | 0.6160 |  |
| Site: UCSD (vs UAB) | -2.3759 | 1.4976 | ±2.9953 | -1.586 | 0.1126 |  |
| Site: UW (vs UAB) | +0.3545 | 1.5278 | ±3.0557 | +0.232 | 0.8165 |  |
| **Age (years)** | **-0.1709** | 0.0567 | ±0.1134 | **-3.013** | **0.0026** | ** |
| **BMI (kg/m2)** | **+0.1640** | 0.0750 | ±0.1499 | **+2.187** | **0.0287** | * |
| Hypertension | +0.5527 | 1.4332 | ±2.8664 | +0.386 | 0.6998 |  |
| High cholesterol | -0.2047 | 1.1663 | ±2.3326 | -0.176 | 0.8607 |  |
| Kidney disease | +1.0687 | 1.7563 | ±3.5126 | +0.608 | 0.5429 |  |
| Circulatory disease | -2.0726 | 1.3772 | ±2.7543 | -1.505 | 0.1323 |  |
| CV (%) | -0.0692 | 0.1015 | ±0.2030 | -0.681 | 0.4956 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1589**, F-statistic = **4.47** (p = **5.37e-06**), Residual SE = **7.915** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6603** | 5.7887 | ±11.5774 | **+12.725** | **4.31e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4874** | 1.3954 | ±2.7908 | **-2.499** | **0.0124** | * |
| Education: high school or below (vs college) | -1.0213 | 1.5366 | ±3.0732 | -0.665 | 0.5063 |  |
| Site: UCSD (vs UAB) | -2.3559 | 1.4953 | ±2.9906 | -1.576 | 0.1151 |  |
| Site: UW (vs UAB) | +0.4163 | 1.5275 | ±3.0551 | +0.273 | 0.7852 |  |
| **Age (years)** | **-0.1823** | 0.0567 | ±0.1133 | **-3.218** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.1676** | 0.0734 | ±0.1468 | **+2.284** | **0.0224** | * |
| Hypertension | +0.5863 | 1.4337 | ±2.8674 | +0.409 | 0.6826 |  |
| High cholesterol | -0.2093 | 1.1685 | ±2.3370 | -0.179 | 0.8579 |  |
| Kidney disease | +0.7596 | 1.6966 | ±3.3933 | +0.448 | 0.6544 |  |
| Circulatory disease | -2.0237 | 1.3675 | ±2.7349 | -1.480 | 0.1389 |  |
| Mean / SD ratio | +0.0308 | 0.4953 | ±0.9906 | +0.062 | 0.9504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **203**, R² = **0.2049**, Adj R² = **0.1591**, F-statistic = **4.48** (p = **5.25e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.1637** | 5.7933 | ±11.5865 | **+12.629** | **1.46e-36** | *** |
| **Education: graduate level (vs college)** | **-3.5270** | 1.3955 | ±2.7910 | **-2.527** | **0.0115** | * |
| Education: high school or below (vs college) | -0.9616 | 1.5391 | ±3.0782 | -0.625 | 0.5321 |  |
| Site: UCSD (vs UAB) | -2.3447 | 1.4939 | ±2.9878 | -1.570 | 0.1165 |  |
| Site: UW (vs UAB) | +0.4175 | 1.5326 | ±3.0652 | +0.272 | 0.7853 |  |
| **Age (years)** | **-0.1793** | 0.0569 | ±0.1138 | **-3.151** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1669** | 0.0734 | ±0.1468 | **+2.274** | **0.0230** | * |
| Hypertension | +0.5681 | 1.4350 | ±2.8700 | +0.396 | 0.6922 |  |
| High cholesterol | -0.1978 | 1.1769 | ±2.3537 | -0.168 | 0.8665 |  |
| Kidney disease | +0.7861 | 1.6808 | ±3.3617 | +0.468 | 0.6400 |  |
| Circulatory disease | -2.0255 | 1.3683 | ±2.7366 | -1.480 | 0.1388 |  |
| Avg. daily mean/SD | +0.0896 | 0.4086 | ±0.8171 | +0.219 | 0.8263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **203**, R² = **0.2071**, Adj R² = **0.1614**, F-statistic = **4.53** (p = **4.24e-06**), Residual SE = **7.903** on **191** df, AIC = **1427.0**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.2351** | 4.8056 | ±9.6111 | **+15.656** | **3.03e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5718** | 1.3285 | ±2.6571 | **-2.688** | **0.0072** | ** |
| Education: high school or below (vs college) | -0.8275 | 1.5776 | ±3.1553 | -0.525 | 0.5999 |  |
| Site: UCSD (vs UAB) | -2.2979 | 1.4995 | ±2.9990 | -1.532 | 0.1254 |  |
| Site: UW (vs UAB) | +0.3194 | 1.5151 | ±3.0303 | +0.211 | 0.8331 |  |
| **Age (years)** | **-0.1799** | 0.0536 | ±0.1073 | **-3.353** | **7.98e-04** | *** |
| **BMI (kg/m2)** | **+0.1729** | 0.0730 | ±0.1460 | **+2.369** | **0.0178** | * |
| Hypertension | +0.5413 | 1.4454 | ±2.8909 | +0.374 | 0.7081 |  |
| High cholesterol | -0.1705 | 1.1709 | ±2.3419 | -0.146 | 0.8842 |  |
| Kidney disease | +0.7681 | 1.6534 | ±3.3068 | +0.465 | 0.6423 |  |
| Circulatory disease | -2.0371 | 1.3638 | ±2.7276 | -1.494 | 0.1353 |  |
| MAG (mg/dL/h) | -0.0390 | 0.0553 | ±0.1106 | -0.705 | 0.4809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **203**, R² = **0.2061**, Adj R² = **0.1604**, F-statistic = **4.51** (p = **4.66e-06**), Residual SE = **7.908** on **191** df, AIC = **1427.3**, BIC = **1467.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.6604** | 4.9277 | ±9.8553 | **+15.151** | **7.43e-52** | *** |
| **Education: graduate level (vs college)** | **-3.5844** | 1.3640 | ±2.7280 | **-2.628** | **0.0086** | ** |
| Education: high school or below (vs college) | -0.8371 | 1.5816 | ±3.1632 | -0.529 | 0.5966 |  |
| Site: UCSD (vs UAB) | -2.3556 | 1.5010 | ±3.0020 | -1.569 | 0.1166 |  |
| Site: UW (vs UAB) | +0.3943 | 1.5268 | ±3.0536 | +0.258 | 0.7962 |  |
| **Age (years)** | **-0.1784** | 0.0541 | ±0.1082 | **-3.298** | **9.75e-04** | *** |
| **BMI (kg/m2)** | **+0.1646** | 0.0740 | ±0.1479 | **+2.225** | **0.0261** | * |
| Hypertension | +0.5485 | 1.4361 | ±2.8723 | +0.382 | 0.7025 |  |
| High cholesterol | -0.1876 | 1.1699 | ±2.3398 | -0.160 | 0.8726 |  |
| Kidney disease | +0.9434 | 1.7180 | ±3.4359 | +0.549 | 0.5829 |  |
| Circulatory disease | -2.0295 | 1.3628 | ±2.7256 | -1.489 | 0.1364 |  |
| Avg. daily range (mg/dL) | -0.0074 | 0.0147 | ±0.0293 | -0.503 | 0.6147 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1597**, F-statistic = **4.49** (p = **5.00e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6678** | 4.7319 | ±9.4639 | **+15.568** | **1.20e-54** | *** |
| **Education: graduate level (vs college)** | **-3.3971** | 1.3579 | ±2.7157 | **-2.502** | **0.0124** | * |
| Education: high school or below (vs college) | -1.0710 | 1.5095 | ±3.0191 | -0.709 | 0.4780 |  |
| Site: UCSD (vs UAB) | -2.3711 | 1.4923 | ±2.9847 | -1.589 | 0.1121 |  |
| Site: UW (vs UAB) | +0.4532 | 1.5290 | ±3.0580 | +0.296 | 0.7669 |  |
| **Age (years)** | **-0.1856** | 0.0532 | ±0.1065 | **-3.487** | **4.88e-04** | *** |
| **BMI (kg/m2)** | **+0.1684** | 0.0728 | ±0.1457 | **+2.313** | **0.0207** | * |
| Hypertension | +0.5563 | 1.4591 | ±2.9183 | +0.381 | 0.7030 |  |
| High cholesterol | -0.1924 | 1.1657 | ±2.3314 | -0.165 | 0.8689 |  |
| Kidney disease | +0.6434 | 1.6565 | ±3.3129 | +0.388 | 0.6977 |  |
| Circulatory disease | -2.0500 | 1.3707 | ±2.7415 | -1.496 | 0.1348 |  |
| SD of daily means (mg/dL) | +0.0247 | 0.0538 | ±0.1075 | +0.460 | 0.6455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **203**, R² = **0.2053**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.03e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.5**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9445** | 5.3652 | ±10.7305 | **+13.969** | **2.43e-44** | *** |
| **Education: graduate level (vs college)** | **-3.4015** | 1.3654 | ±2.7307 | **-2.491** | **0.0127** | * |
| Education: high school or below (vs college) | -1.1008 | 1.5094 | ±3.0187 | -0.729 | 0.4658 |  |
| Site: UCSD (vs UAB) | -2.3526 | 1.4917 | ±2.9834 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4467 | 1.5313 | ±3.0626 | +0.292 | 0.7705 |  |
| **Age (years)** | **-0.1850** | 0.0527 | ±0.1054 | **-3.510** | **4.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1687** | 0.0733 | ±0.1466 | **+2.301** | **0.0214** | * |
| Hypertension | +0.6092 | 1.4423 | ±2.8846 | +0.422 | 0.6728 |  |
| High cholesterol | -0.2294 | 1.1703 | ±2.3405 | -0.196 | 0.8446 |  |
| Kidney disease | +0.6487 | 1.6676 | ±3.3351 | +0.389 | 0.6973 |  |
| Circulatory disease | -2.0495 | 1.3781 | ±2.7562 | -1.487 | 0.1370 |  |
| Time in range 70-180, pooled (%) | -0.0123 | 0.0349 | ±0.0699 | -0.353 | 0.7240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.02e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9578** | 5.2905 | ±10.5810 | **+14.168** | **1.44e-45** | *** |
| **Education: graduate level (vs college)** | **-3.4007** | 1.3658 | ±2.7315 | **-2.490** | **0.0128** | * |
| Education: high school or below (vs college) | -1.1085 | 1.5083 | ±3.0167 | -0.735 | 0.4624 |  |
| Site: UCSD (vs UAB) | -2.3496 | 1.4915 | ±2.9830 | -1.575 | 0.1152 |  |
| Site: UW (vs UAB) | +0.4496 | 1.5331 | ±3.0663 | +0.293 | 0.7693 |  |
| **Age (years)** | **-0.1850** | 0.0527 | ±0.1053 | **-3.513** | **4.43e-04** | *** |
| **BMI (kg/m2)** | **+0.1690** | 0.0735 | ±0.1469 | **+2.301** | **0.0214** | * |
| Hypertension | +0.6124 | 1.4412 | ±2.8824 | +0.425 | 0.6709 |  |
| High cholesterol | -0.2307 | 1.1684 | ±2.3368 | -0.197 | 0.8435 |  |
| Kidney disease | +0.6447 | 1.6668 | ±3.3337 | +0.387 | 0.6989 |  |
| Circulatory disease | -2.0520 | 1.3785 | ±2.7570 | -1.489 | 0.1366 |  |
| Avg. daily time in range 70-180 (%) | -0.0126 | 0.0338 | ±0.0677 | -0.371 | 0.7105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.2069**, Adj R² = **0.1612**, F-statistic = **4.53** (p = **4.33e-06**), Residual SE = **7.904** on **191** df, AIC = **1427.1**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6934** | 4.6881 | ±9.3761 | **+15.719** | **1.11e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4145** | 1.3205 | ±2.6409 | **-2.586** | **0.0097** | ** |
| Education: high school or below (vs college) | -0.9517 | 1.5316 | ±3.0632 | -0.621 | 0.5344 |  |
| Site: UCSD (vs UAB) | -2.2388 | 1.4919 | ±2.9838 | -1.501 | 0.1334 |  |
| Site: UW (vs UAB) | +0.5761 | 1.5402 | ±3.0804 | +0.374 | 0.7084 |  |
| **Age (years)** | **-0.1845** | 0.0529 | ±0.1057 | **-3.489** | **4.84e-04** | *** |
| **BMI (kg/m2)** | **+0.1669** | 0.0723 | ±0.1447 | **+2.308** | **0.0210** | * |
| Hypertension | +0.5420 | 1.4440 | ±2.8880 | +0.375 | 0.7074 |  |
| High cholesterol | -0.2256 | 1.1694 | ±2.3388 | -0.193 | 0.8470 |  |
| Kidney disease | +0.7571 | 1.6618 | ±3.3237 | +0.456 | 0.6487 |  |
| Circulatory disease | -2.1156 | 1.3597 | ±2.7195 | -1.556 | 0.1197 |  |
| Time < 54 (%) | +0.5339 | 0.6939 | ±1.3878 | +0.769 | 0.4417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **203**, R² = **0.2048**, Adj R² = **0.1590**, F-statistic = **4.47** (p = **5.32e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8754** | 4.7065 | ±9.4130 | **+15.696** | **1.60e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4916** | 1.3262 | ±2.6525 | **-2.633** | **0.0085** | ** |
| Education: high school or below (vs college) | -1.0655 | 1.5182 | ±3.0364 | -0.702 | 0.4828 |  |
| Site: UCSD (vs UAB) | -2.3826 | 1.4982 | ±2.9964 | -1.590 | 0.1118 |  |
| Site: UW (vs UAB) | +0.3904 | 1.5358 | ±3.0717 | +0.254 | 0.7993 |  |
| **Age (years)** | **-0.1828** | 0.0536 | ±0.1073 | **-3.409** | **6.52e-04** | *** |
| **BMI (kg/m2)** | **+0.1677** | 0.0735 | ±0.1469 | **+2.282** | **0.0225** | * |
| Hypertension | +0.5975 | 1.4495 | ±2.8989 | +0.412 | 0.6802 |  |
| High cholesterol | -0.2147 | 1.1706 | ±2.3412 | -0.183 | 0.8545 |  |
| Kidney disease | +0.7431 | 1.6616 | ±3.3232 | +0.447 | 0.6547 |  |
| Circulatory disease | -2.0040 | 1.3995 | ±2.7989 | -1.432 | 0.1522 |  |
| Avg. daily time < 54 (%) | -0.1165 | 1.1633 | ±2.3265 | -0.100 | 0.9202 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.01e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8978** | 4.7193 | ±9.4386 | **+15.659** | **2.90e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5601** | 1.3518 | ±2.7035 | **-2.634** | **0.0084** | ** |
| Education: high school or below (vs college) | -1.0263 | 1.5110 | ±3.0221 | -0.679 | 0.4970 |  |
| Site: UCSD (vs UAB) | -2.4043 | 1.5104 | ±3.0208 | -1.592 | 0.1114 |  |
| Site: UW (vs UAB) | +0.3916 | 1.5225 | ±3.0450 | +0.257 | 0.7970 |  |
| **Age (years)** | **-0.1806** | 0.0533 | ±0.1065 | **-3.390** | **6.99e-04** | *** |
| **BMI (kg/m2)** | **+0.1671** | 0.0735 | ±0.1471 | **+2.273** | **0.0230** | * |
| Hypertension | +0.5792 | 1.4456 | ±2.8913 | +0.401 | 0.6887 |  |
| High cholesterol | -0.1928 | 1.1737 | ±2.3474 | -0.164 | 0.8695 |  |
| Kidney disease | +0.7530 | 1.6589 | ±3.3179 | +0.454 | 0.6499 |  |
| Circulatory disease | -2.0143 | 1.3813 | ±2.7626 | -1.458 | 0.1448 |  |
| Time 54-69, pooled (%) | -0.0935 | 0.2338 | ±0.4677 | -0.400 | 0.6894 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **203**, R² = **0.2069**, Adj R² = **0.1612**, F-statistic = **4.53** (p = **4.31e-06**), Residual SE = **7.904** on **191** df, AIC = **1427.1**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8483** | 4.7199 | ±9.4399 | **+15.646** | **3.54e-55** | *** |
| **Education: graduate level (vs college)** | **-3.6178** | 1.3530 | ±2.7060 | **-2.674** | **0.0075** | ** |
| Education: high school or below (vs college) | -0.9977 | 1.5034 | ±3.0068 | -0.664 | 0.5069 |  |
| Site: UCSD (vs UAB) | -2.4330 | 1.5114 | ±3.0229 | -1.610 | 0.1075 |  |
| Site: UW (vs UAB) | +0.3716 | 1.5163 | ±3.0326 | +0.245 | 0.8064 |  |
| **Age (years)** | **-0.1776** | 0.0536 | ±0.1073 | **-3.311** | **9.28e-04** | *** |
| **BMI (kg/m2)** | **+0.1667** | 0.0737 | ±0.1474 | **+2.262** | **0.0237** | * |
| Hypertension | +0.5727 | 1.4487 | ±2.8974 | +0.395 | 0.6926 |  |
| High cholesterol | -0.1855 | 1.1751 | ±2.3502 | -0.158 | 0.8746 |  |
| Kidney disease | +0.7639 | 1.6544 | ±3.3088 | +0.462 | 0.6443 |  |
| Circulatory disease | -2.0099 | 1.3879 | ±2.7759 | -1.448 | 0.1476 |  |
| Avg. daily time 54-69 (%) | -0.1553 | 0.2389 | ±0.4777 | -0.650 | 0.5155 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **203**, R² = **0.2048**, Adj R² = **0.1590**, F-statistic = **4.47** (p = **5.33e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8846** | 4.7163 | ±9.4327 | **+15.666** | **2.60e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5034** | 1.3423 | ±2.6846 | **-2.610** | **0.0091** | ** |
| Education: high school or below (vs college) | -1.0440 | 1.5188 | ±3.0376 | -0.687 | 0.4918 |  |
| Site: UCSD (vs UAB) | -2.3794 | 1.5090 | ±3.0180 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4016 | 1.5294 | ±3.0589 | +0.263 | 0.7929 |  |
| **Age (years)** | **-0.1825** | 0.0533 | ±0.1066 | **-3.425** | **6.14e-04** | *** |
| **BMI (kg/m2)** | **+0.1676** | 0.0733 | ±0.1466 | **+2.286** | **0.0223** | * |
| Hypertension | +0.5900 | 1.4453 | ±2.8905 | +0.408 | 0.6831 |  |
| High cholesterol | -0.2035 | 1.1727 | ±2.3454 | -0.174 | 0.8622 |  |
| Kidney disease | +0.7431 | 1.6615 | ±3.3230 | +0.447 | 0.6547 |  |
| Circulatory disease | -2.0165 | 1.3780 | ±2.7560 | -1.463 | 0.1434 |  |
| Time < 70 (%) | -0.0296 | 0.1988 | ±0.3975 | -0.149 | 0.8817 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **203**, R² = **0.2064**, Adj R² = **0.1607**, F-statistic = **4.52** (p = **4.54e-06**), Residual SE = **7.906** on **191** df, AIC = **1427.2**, BIC = **1466.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8632** | 4.7201 | ±9.4402 | **+15.649** | **3.40e-55** | *** |
| **Education: graduate level (vs college)** | **-3.5942** | 1.3459 | ±2.6919 | **-2.670** | **0.0076** | ** |
| Education: high school or below (vs college) | -1.0310 | 1.5071 | ±3.0141 | -0.684 | 0.4939 |  |
| Site: UCSD (vs UAB) | -2.4347 | 1.5091 | ±3.0181 | -1.613 | 0.1067 |  |
| Site: UW (vs UAB) | +0.3581 | 1.5200 | ±3.0401 | +0.236 | 0.8137 |  |
| **Age (years)** | **-0.1787** | 0.0539 | ±0.1077 | **-3.317** | **9.10e-04** | *** |
| **BMI (kg/m2)** | **+0.1670** | 0.0737 | ±0.1473 | **+2.267** | **0.0234** | * |
| Hypertension | +0.5841 | 1.4498 | ±2.8997 | +0.403 | 0.6870 |  |
| High cholesterol | -0.1972 | 1.1723 | ±2.3446 | -0.168 | 0.8664 |  |
| Kidney disease | +0.7601 | 1.6564 | ±3.3128 | +0.459 | 0.6463 |  |
| Circulatory disease | -1.9944 | 1.3902 | ±2.7804 | -1.435 | 0.1514 |  |
| Avg. daily time < 70 (%) | -0.1107 | 0.2121 | ±0.4241 | -0.522 | 0.6017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1589**, F-statistic = **4.47** (p = **5.36e-06**), Residual SE = **7.915** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.3349** | 8.4695 | ±16.9389 | **+8.659** | **4.77e-18** | *** |
| **Education: graduate level (vs college)** | **-3.4824** | 1.3367 | ±2.6734 | **-2.605** | **0.0092** | ** |
| Education: high school or below (vs college) | -1.0288 | 1.5423 | ±3.0847 | -0.667 | 0.5048 |  |
| Site: UCSD (vs UAB) | -2.3600 | 1.4947 | ±2.9894 | -1.579 | 0.1144 |  |
| Site: UW (vs UAB) | +0.4064 | 1.5320 | ±3.0639 | +0.265 | 0.7908 |  |
| **Age (years)** | **-0.1836** | 0.0530 | ±0.1060 | **-3.463** | **5.35e-04** | *** |
| **BMI (kg/m2)** | **+0.1675** | 0.0734 | ±0.1469 | **+2.280** | **0.0226** | * |
| Hypertension | +0.5935 | 1.4516 | ±2.9032 | +0.409 | 0.6826 |  |
| High cholesterol | -0.2156 | 1.1723 | ±2.3445 | -0.184 | 0.8540 |  |
| Kidney disease | +0.7511 | 1.6699 | ±3.3397 | +0.450 | 0.6529 |  |
| Circulatory disease | -2.0173 | 1.3863 | ±2.7726 | -1.455 | 0.1456 |  |
| Time 54-250, pooled (%) | +0.0057 | 0.0756 | ±0.1512 | +0.075 | 0.9399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.2049**, Adj R² = **0.1591**, F-statistic = **4.47** (p = **5.26e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.3354** | 7.8908 | ±15.7816 | **+9.547** | **1.33e-21** | *** |
| **Education: graduate level (vs college)** | **-3.4451** | 1.3375 | ±2.6751 | **-2.576** | **0.0100** | * |
| Education: high school or below (vs college) | -1.0911 | 1.5204 | ±3.0408 | -0.718 | 0.4730 |  |
| Site: UCSD (vs UAB) | -2.3572 | 1.4938 | ±2.9877 | -1.578 | 0.1146 |  |
| Site: UW (vs UAB) | +0.4475 | 1.5309 | ±3.0618 | +0.292 | 0.7701 |  |
| **Age (years)** | **-0.1834** | 0.0528 | ±0.1057 | **-3.471** | **5.19e-04** | *** |
| **BMI (kg/m2)** | **+0.1686** | 0.0734 | ±0.1468 | **+2.297** | **0.0216** | * |
| Hypertension | +0.5843 | 1.4480 | ±2.8960 | +0.404 | 0.6866 |  |
| High cholesterol | -0.1955 | 1.1700 | ±2.3399 | -0.167 | 0.8673 |  |
| Kidney disease | +0.7065 | 1.6587 | ±3.3174 | +0.426 | 0.6701 |  |
| Circulatory disease | -2.0477 | 1.3875 | ±2.7750 | -1.476 | 0.1400 |  |
| Avg. daily time 54-250 (%) | -0.0157 | 0.0692 | ±0.1384 | -0.226 | 0.8210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.2071**, Adj R² = **0.1615**, F-statistic = **4.54** (p = **4.22e-06**), Residual SE = **7.903** on **191** df, AIC = **1427.0**, BIC = **1466.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6882** | 4.7534 | ±9.5068 | **+15.502** | **3.35e-54** | *** |
| **Education: graduate level (vs college)** | **-3.3637** | 1.3610 | ±2.7221 | **-2.471** | **0.0135** | * |
| Education: high school or below (vs college) | -1.1002 | 1.4934 | ±2.9869 | -0.737 | 0.4613 |  |
| Site: UCSD (vs UAB) | -2.3710 | 1.4855 | ±2.9711 | -1.596 | 0.1105 |  |
| Site: UW (vs UAB) | +0.4106 | 1.5217 | ±3.0433 | +0.270 | 0.7873 |  |
| **Age (years)** | **-0.1875** | 0.0525 | ±0.1051 | **-3.570** | **3.58e-04** | *** |
| **BMI (kg/m2)** | **+0.1689** | 0.0729 | ±0.1458 | **+2.316** | **0.0206** | * |
| Hypertension | +0.6547 | 1.4391 | ±2.8782 | +0.455 | 0.6492 |  |
| High cholesterol | -0.2968 | 1.1653 | ±2.3306 | -0.255 | 0.7990 |  |
| Kidney disease | +0.5511 | 1.6522 | ±3.3044 | +0.334 | 0.7387 |  |
| Circulatory disease | -2.0453 | 1.3758 | ±2.7516 | -1.487 | 0.1371 |  |
| Time 181-250, pooled (%) | +0.0356 | 0.0507 | ±0.1013 | +0.702 | 0.4826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **203**, R² = **0.2061**, Adj R² = **0.1604**, F-statistic = **4.51** (p = **4.65e-06**), Residual SE = **7.907** on **191** df, AIC = **1427.2**, BIC = **1467.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6779** | 4.7669 | ±9.5339 | **+15.456** | **6.87e-54** | *** |
| **Education: graduate level (vs college)** | **-3.3916** | 1.3607 | ±2.7214 | **-2.493** | **0.0127** | * |
| Education: high school or below (vs college) | -1.0930 | 1.4995 | ±2.9991 | -0.729 | 0.4661 |  |
| Site: UCSD (vs UAB) | -2.3544 | 1.4890 | ±2.9780 | -1.581 | 0.1138 |  |
| Site: UW (vs UAB) | +0.4274 | 1.5259 | ±3.0518 | +0.280 | 0.7794 |  |
| **Age (years)** | **-0.1859** | 0.0526 | ±0.1051 | **-3.537** | **4.04e-04** | *** |
| **BMI (kg/m2)** | **+0.1689** | 0.0731 | ±0.1463 | **+2.309** | **0.0210** | * |
| Hypertension | +0.6447 | 1.4380 | ±2.8760 | +0.448 | 0.6539 |  |
| High cholesterol | -0.2743 | 1.1655 | ±2.3309 | -0.235 | 0.8139 |  |
| Kidney disease | +0.5989 | 1.6592 | ±3.3183 | +0.361 | 0.7181 |  |
| Circulatory disease | -2.0410 | 1.3770 | ±2.7541 | -1.482 | 0.1383 |  |
| Avg. daily time 181-250 (%) | +0.0267 | 0.0499 | ±0.0999 | +0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **203**, R² = **0.2054**, Adj R² = **0.1596**, F-statistic = **4.49** (p = **5.00e-06**), Residual SE = **7.911** on **191** df, AIC = **1427.4**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7164** | 4.7551 | ±9.5103 | **+15.502** | **3.34e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4131** | 1.3550 | ±2.7099 | **-2.519** | **0.0118** | * |
| Education: high school or below (vs college) | -1.1018 | 1.5070 | ±3.0140 | -0.731 | 0.4647 |  |
| Site: UCSD (vs UAB) | -2.3615 | 1.4921 | ±2.9841 | -1.583 | 0.1135 |  |
| Site: UW (vs UAB) | +0.4400 | 1.5277 | ±3.0555 | +0.288 | 0.7734 |  |
| **Age (years)** | **-0.1846** | 0.0527 | ±0.1054 | **-3.505** | **4.57e-04** | *** |
| **BMI (kg/m2)** | **+0.1687** | 0.0733 | ±0.1465 | **+2.303** | **0.0213** | * |
| Hypertension | +0.6092 | 1.4435 | ±2.8869 | +0.422 | 0.6730 |  |
| High cholesterol | -0.2272 | 1.1682 | ±2.3364 | -0.194 | 0.8458 |  |
| Kidney disease | +0.6480 | 1.6610 | ±3.3221 | +0.390 | 0.6964 |  |
| Circulatory disease | -2.0465 | 1.3788 | ±2.7577 | -1.484 | 0.1378 |  |
| Time > 180 (%) | +0.0126 | 0.0333 | ±0.0667 | +0.378 | 0.7052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **203**, R² = **0.2058**, Adj R² = **0.1600**, F-statistic = **4.50** (p = **4.82e-06**), Residual SE = **7.909** on **191** df, AIC = **1427.3**, BIC = **1467.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.6620** | 4.7659 | ±9.5318 | **+15.456** | **6.86e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4004** | 1.3566 | ±2.7132 | **-2.507** | **0.0122** | * |
| Education: high school or below (vs college) | -1.1220 | 1.5006 | ±3.0012 | -0.748 | 0.4546 |  |
| Site: UCSD (vs UAB) | -2.3583 | 1.4906 | ±2.9812 | -1.582 | 0.1136 |  |
| Site: UW (vs UAB) | +0.4485 | 1.5289 | ±3.0578 | +0.293 | 0.7692 |  |
| **Age (years)** | **-0.1847** | 0.0526 | ±0.1052 | **-3.510** | **4.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1692** | 0.0733 | ±0.1466 | **+2.308** | **0.0210** | * |
| Hypertension | +0.6166 | 1.4428 | ±2.8856 | +0.427 | 0.6691 |  |
| High cholesterol | -0.2340 | 1.1657 | ±2.3314 | -0.201 | 0.8409 |  |
| Kidney disease | +0.6244 | 1.6558 | ±3.3117 | +0.377 | 0.7061 |  |
| Circulatory disease | -2.0543 | 1.3799 | ±2.7598 | -1.489 | 0.1366 |  |
| Avg. daily time > 180 (%) | +0.0156 | 0.0322 | ±0.0644 | +0.485 | 0.6277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **203**, R² = **0.2052**, Adj R² = **0.1594**, F-statistic = **4.48** (p = **5.10e-06**), Residual SE = **7.912** on **191** df, AIC = **1427.5**, BIC = **1467.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7557** | 4.7435 | ±9.4870 | **+15.549** | **1.62e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4332** | 1.3463 | ±2.6926 | **-2.550** | **0.0108** | * |
| Education: high school or below (vs college) | -1.0706 | 1.5042 | ±3.0084 | -0.712 | 0.4766 |  |
| Site: UCSD (vs UAB) | -2.3640 | 1.4922 | ±2.9844 | -1.584 | 0.1131 |  |
| Site: UW (vs UAB) | +0.4386 | 1.5251 | ±3.0502 | +0.288 | 0.7737 |  |
| **Age (years)** | **-0.1833** | 0.0528 | ±0.1057 | **-3.469** | **5.22e-04** | *** |
| **BMI (kg/m2)** | **+0.1678** | 0.0729 | ±0.1458 | **+2.302** | **0.0213** | * |
| Hypertension | +0.5783 | 1.4547 | ±2.9093 | +0.398 | 0.6910 |  |
| High cholesterol | -0.2298 | 1.1672 | ±2.3345 | -0.197 | 0.8439 |  |
| Kidney disease | +0.6996 | 1.6511 | ±3.3022 | +0.424 | 0.6718 |  |
| Circulatory disease | -2.0585 | 1.3815 | ±2.7629 | -1.490 | 0.1362 |  |
| Nocturnal time > 180 (%) | +0.0107 | 0.0302 | ±0.0603 | +0.355 | 0.7224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.2047**, Adj R² = **0.1589**, F-statistic = **4.47** (p = **5.36e-06**), Residual SE = **7.915** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8387** | 4.7602 | ±9.5205 | **+15.512** | **2.90e-54** | *** |
| **Education: graduate level (vs college)** | **-3.4559** | 1.3642 | ±2.7284 | **-2.533** | **0.0113** | * |
| Education: high school or below (vs college) | -1.0546 | 1.5169 | ±3.0339 | -0.695 | 0.4869 |  |
| Site: UCSD (vs UAB) | -2.3616 | 1.4977 | ±2.9954 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4067 | 1.5301 | ±3.0602 | +0.266 | 0.7904 |  |
| **Age (years)** | **-0.1844** | 0.0533 | ±0.1067 | **-3.457** | **5.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1685** | 0.0754 | ±0.1507 | **+2.236** | **0.0253** | * |
| Hypertension | +0.5920 | 1.4446 | ±2.8891 | +0.410 | 0.6819 |  |
| High cholesterol | -0.2135 | 1.1686 | ±2.3372 | -0.183 | 0.8550 |  |
| Kidney disease | +0.7135 | 1.6918 | ±3.3837 | +0.422 | 0.6732 |  |
| Circulatory disease | -2.0242 | 1.3713 | ±2.7425 | -1.476 | 0.1399 |  |
| Any reading > 250 during wear (0/1) | +0.1106 | 1.2631 | ±2.5262 | +0.088 | 0.9302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.2048**, Adj R² = **0.1590**, F-statistic = **4.47** (p = **5.33e-06**), Residual SE = **7.914** on **191** df, AIC = **1427.6**, BIC = **1467.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.9274** | 4.7420 | ±9.4840 | **+15.590** | **8.52e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4877** | 1.3356 | ±2.6711 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | -1.0172 | 1.5431 | ±3.0862 | -0.659 | 0.5098 |  |
| Site: UCSD (vs UAB) | -2.3590 | 1.4960 | ±2.9920 | -1.577 | 0.1148 |  |
| Site: UW (vs UAB) | +0.4013 | 1.5299 | ±3.0598 | +0.262 | 0.7931 |  |
| **Age (years)** | **-0.1837** | 0.0531 | ±0.1061 | **-3.462** | **5.36e-04** | *** |
| **BMI (kg/m2)** | **+0.1673** | 0.0734 | ±0.1468 | **+2.279** | **0.0227** | * |
| Hypertension | +0.5943 | 1.4514 | ±2.9029 | +0.409 | 0.6822 |  |
| High cholesterol | -0.2196 | 1.1732 | ±2.3465 | -0.187 | 0.8515 |  |
| Kidney disease | +0.7583 | 1.6707 | ±3.3414 | +0.454 | 0.6499 |  |
| Circulatory disease | -2.0142 | 1.3829 | ±2.7658 | -1.457 | 0.1452 |  |
| Time > 250 (%) | -0.0093 | 0.0733 | ±0.1467 | -0.126 | 0.8995 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 203)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.2049**, Adj R² = **0.1592**, F-statistic = **4.48** (p = **5.24e-06**), Residual SE = **7.913** on **191** df, AIC = **1427.6**, BIC = **1467.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7619** | 4.7332 | ±9.4664 | **+15.584** | **9.36e-55** | *** |
| **Education: graduate level (vs college)** | **-3.4453** | 1.3363 | ±2.6727 | **-2.578** | **0.0099** | ** |
| Education: high school or below (vs college) | -1.0987 | 1.5172 | ±3.0345 | -0.724 | 0.4690 |  |
| Site: UCSD (vs UAB) | -2.3607 | 1.4948 | ±2.9896 | -1.579 | 0.1143 |  |
| Site: UW (vs UAB) | +0.4461 | 1.5289 | ±3.0579 | +0.292 | 0.7705 |  |
| **Age (years)** | **-0.1832** | 0.0528 | ±0.1057 | **-3.468** | **5.25e-04** | *** |
| **BMI (kg/m2)** | **+0.1686** | 0.0733 | ±0.1466 | **+2.301** | **0.0214** | * |
| Hypertension | +0.5846 | 1.4476 | ±2.8953 | +0.404 | 0.6863 |  |
| High cholesterol | -0.1949 | 1.1704 | ±2.3409 | -0.166 | 0.8678 |  |
| Kidney disease | +0.7037 | 1.6565 | ±3.3130 | +0.425 | 0.6710 |  |
| Circulatory disease | -2.0468 | 1.3855 | ±2.7710 | -1.477 | 0.1396 |  |
| Avg. daily time > 250 (%) | +0.0172 | 0.0670 | ±0.1339 | +0.257 | 0.7975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 205; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **205**, R² = **0.0659**, Adj R² = **0.0177**, F-statistic = **1.37** (p = **0.1975**), Residual SE = **68.888** on **194** df, AIC = **2327.8**, BIC = **2364.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8528** | 40.7069 | ±81.4138 | **+9.675** | **3.84e-22** | *** |
| Education: graduate level (vs college) | +10.2617 | 12.7112 | ±25.4224 | +0.807 | 0.4195 |  |
| Education: high school or below (vs college) | -21.2336 | 13.7302 | ±27.4604 | -1.546 | 0.1220 |  |
| Site: UCSD (vs UAB) | -10.2666 | 12.8259 | ±25.6517 | -0.800 | 0.4234 |  |
| Site: UW (vs UAB) | -12.6536 | 12.7582 | ±25.5163 | -0.992 | 0.3213 |  |
| Age (years) | -0.0595 | 0.5377 | ±1.0754 | -0.111 | 0.9119 |  |
| BMI (kg/m2) | -0.3694 | 0.6533 | ±1.3066 | -0.565 | 0.5718 |  |
| **Hypertension** | **-27.1461** | 12.1421 | ±24.2842 | **-2.236** | **0.0254** | * |
| High cholesterol | +7.8438 | 10.2966 | ±20.5931 | +0.762 | 0.4462 |  |
| Kidney disease | +3.4725 | 17.3785 | ±34.7571 | +0.200 | 0.8416 |  |
| Circulatory disease | +1.7522 | 11.6420 | ±23.2841 | +0.151 | 0.8804 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **205**, R² = **0.1089**, Adj R² = **0.0581**, F-statistic = **2.14** (p = **0.0190**), Residual SE = **67.456** on **193** df, AIC = **2320.1**, BIC = **2360.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+461.9602** | 42.7001 | ±85.4002 | **+10.819** | **2.81e-27** | *** |
| Education: graduate level (vs college) | +5.8523 | 12.6761 | ±25.3522 | +0.462 | 0.6443 |  |
| Education: high school or below (vs college) | -16.7549 | 12.4925 | ±24.9850 | -1.341 | 0.1799 |  |
| Site: UCSD (vs UAB) | -11.2141 | 12.4538 | ±24.9075 | -0.900 | 0.3679 |  |
| Site: UW (vs UAB) | -13.9739 | 12.6603 | ±25.3205 | -1.104 | 0.2697 |  |
| Age (years) | +0.1696 | 0.5345 | ±1.0689 | +0.317 | 0.7510 |  |
| BMI (kg/m2) | -0.2797 | 0.6239 | ±1.2479 | -0.448 | 0.6539 |  |
| **Hypertension** | **-26.5696** | 11.7743 | ±23.5486 | **-2.257** | **0.0240** | * |
| High cholesterol | +6.6134 | 10.0139 | ±20.0278 | +0.660 | 0.5090 |  |
| Kidney disease | +3.6253 | 16.8248 | ±33.6496 | +0.215 | 0.8294 |  |
| Circulatory disease | +0.6999 | 11.2778 | ±22.5556 | +0.062 | 0.9505 |  |
| **HbA1c (%)** | **-12.9355** | 3.7701 | ±7.5402 | **-3.431** | **6.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **205**, R² = **0.0865**, Adj R² = **0.0344**, F-statistic = **1.66** (p = **0.0849**), Residual SE = **68.301** on **193** df, AIC = **2325.2**, BIC = **2365.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+434.6785** | 44.5592 | ±89.1183 | **+9.755** | **1.75e-22** | *** |
| Education: graduate level (vs college) | +8.7778 | 12.7798 | ±25.5597 | +0.687 | 0.4922 |  |
| Education: high school or below (vs college) | -18.6017 | 13.1882 | ±26.3765 | -1.410 | 0.1584 |  |
| Site: UCSD (vs UAB) | -10.0326 | 12.4157 | ±24.8313 | -0.808 | 0.4191 |  |
| Site: UW (vs UAB) | -13.2241 | 13.0593 | ±26.1187 | -1.013 | 0.3112 |  |
| Age (years) | -0.0347 | 0.5359 | ±1.0718 | -0.065 | 0.9484 |  |
| BMI (kg/m2) | -0.3796 | 0.6487 | ±1.2974 | -0.585 | 0.5584 |  |
| **Hypertension** | **-26.8413** | 11.9950 | ±23.9900 | **-2.238** | **0.0252** | * |
| High cholesterol | +7.6941 | 10.1512 | ±20.3024 | +0.758 | 0.4485 |  |
| Kidney disease | +6.1194 | 17.6388 | ±35.2776 | +0.347 | 0.7286 |  |
| Circulatory disease | +2.1811 | 11.4786 | ±22.9572 | +0.190 | 0.8493 |  |
| **Mean glucose (mg/dL)** | **-0.3115** | 0.1399 | ±0.2799 | **-2.226** | **0.0260** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **205**, R² = **0.0865**, Adj R² = **0.0344**, F-statistic = **1.66** (p = **0.0849**), Residual SE = **68.301** on **193** df, AIC = **2325.2**, BIC = **2365.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+477.7828** | 55.3233 | ±110.6467 | **+8.636** | **5.81e-18** | *** |
| Education: graduate level (vs college) | +8.7778 | 12.7798 | ±25.5597 | +0.687 | 0.4922 |  |
| Education: high school or below (vs college) | -18.6017 | 13.1882 | ±26.3765 | -1.410 | 0.1584 |  |
| Site: UCSD (vs UAB) | -10.0326 | 12.4157 | ±24.8313 | -0.808 | 0.4191 |  |
| Site: UW (vs UAB) | -13.2241 | 13.0593 | ±26.1187 | -1.013 | 0.3112 |  |
| Age (years) | -0.0347 | 0.5359 | ±1.0718 | -0.065 | 0.9484 |  |
| BMI (kg/m2) | -0.3796 | 0.6487 | ±1.2974 | -0.585 | 0.5584 |  |
| **Hypertension** | **-26.8413** | 11.9950 | ±23.9900 | **-2.238** | **0.0252** | * |
| High cholesterol | +7.6941 | 10.1512 | ±20.3024 | +0.758 | 0.4485 |  |
| Kidney disease | +6.1194 | 17.6388 | ±35.2776 | +0.347 | 0.7286 |  |
| Circulatory disease | +2.1811 | 11.4786 | ±22.9572 | +0.190 | 0.8493 |  |
| **GMI (%)** | **-13.0224** | 5.8503 | ±11.7006 | **-2.226** | **0.0260** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **205**, R² = **0.0800**, Adj R² = **0.0276**, F-statistic = **1.53** (p = **0.1246**), Residual SE = **68.542** on **193** df, AIC = **2326.6**, BIC = **2366.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+427.2895** | 44.7493 | ±89.4985 | **+9.549** | **1.32e-21** | *** |
| Education: graduate level (vs college) | +9.9144 | 12.8383 | ±25.6767 | +0.772 | 0.4400 |  |
| Education: high school or below (vs college) | -19.2807 | 13.2158 | ±26.4316 | -1.459 | 0.1446 |  |
| Site: UCSD (vs UAB) | -10.1747 | 12.5167 | ±25.0334 | -0.813 | 0.4163 |  |
| Site: UW (vs UAB) | -12.7833 | 13.1054 | ±26.2109 | -0.975 | 0.3294 |  |
| Age (years) | -0.0897 | 0.5390 | ±1.0780 | -0.166 | 0.8678 |  |
| BMI (kg/m2) | -0.3640 | 0.6480 | ±1.2960 | -0.562 | 0.5742 |  |
| **Hypertension** | **-26.3089** | 12.1611 | ±24.3222 | **-2.163** | **0.0305** | * |
| High cholesterol | +8.2622 | 10.1466 | ±20.2932 | +0.814 | 0.4155 |  |
| Kidney disease | +4.0661 | 17.5202 | ±35.0404 | +0.232 | 0.8165 |  |
| Circulatory disease | +2.4197 | 11.4745 | ±22.9490 | +0.211 | 0.8330 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.2522 | 0.1446 | ±0.2892 | -1.744 | 0.0811 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0803**, Adj R² = **0.0279**, F-statistic = **1.53** (p = **0.1227**), Residual SE = **68.532** on **193** df, AIC = **2326.6**, BIC = **2366.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.1054** | 40.7028 | ±81.4056 | **+9.977** | **1.92e-23** | *** |
| Education: graduate level (vs college) | +7.4579 | 12.8772 | ±25.7543 | +0.579 | 0.5625 |  |
| Education: high school or below (vs college) | -17.0254 | 13.5636 | ±27.1272 | -1.255 | 0.2094 |  |
| Site: UCSD (vs UAB) | -10.2274 | 12.4993 | ±24.9986 | -0.818 | 0.4132 |  |
| Site: UW (vs UAB) | -13.7174 | 12.9357 | ±25.8715 | -1.060 | 0.2890 |  |
| Age (years) | +0.0777 | 0.5427 | ±1.0854 | +0.143 | 0.8862 |  |
| BMI (kg/m2) | -0.4128 | 0.6498 | ±1.2996 | -0.635 | 0.5253 |  |
| **Hypertension** | **-27.1377** | 11.8882 | ±23.7764 | **-2.283** | **0.0224** | * |
| High cholesterol | +7.4864 | 10.2114 | ±20.4228 | +0.733 | 0.4635 |  |
| Kidney disease | +8.5738 | 18.2937 | ±36.5873 | +0.469 | 0.6393 |  |
| Circulatory disease | +0.9891 | 11.6212 | ±23.2424 | +0.085 | 0.9322 |  |
| Glucose SD, pooled (mg/dL) | -0.5567 | 0.3092 | ±0.6185 | -1.800 | 0.0718 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0765**, Adj R² = **0.0239**, F-statistic = **1.45** (p = **0.1521**), Residual SE = **68.673** on **193** df, AIC = **2327.4**, BIC = **2367.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.6342** | 41.1405 | ±82.2810 | **+9.860** | **6.22e-23** | *** |
| Education: graduate level (vs college) | +7.7983 | 12.7808 | ±25.5616 | +0.610 | 0.5418 |  |
| Education: high school or below (vs college) | -17.0176 | 13.7098 | ±27.4197 | -1.241 | 0.2145 |  |
| Site: UCSD (vs UAB) | -10.2537 | 12.5788 | ±25.1575 | -0.815 | 0.4150 |  |
| Site: UW (vs UAB) | -13.3797 | 12.9495 | ±25.8991 | -1.033 | 0.3015 |  |
| Age (years) | +0.0560 | 0.5416 | ±1.0831 | +0.103 | 0.9177 |  |
| BMI (kg/m2) | -0.4246 | 0.6551 | ±1.3102 | -0.648 | 0.5169 |  |
| **Hypertension** | **-27.3728** | 11.9196 | ±23.8393 | **-2.296** | **0.0217** | * |
| High cholesterol | +7.7704 | 10.2277 | ±20.4555 | +0.760 | 0.4474 |  |
| Kidney disease | +7.8821 | 18.1894 | ±36.3788 | +0.433 | 0.6648 |  |
| Circulatory disease | +0.9204 | 11.7071 | ±23.4142 | +0.079 | 0.9373 |  |
| Avg. daily SD (mg/dL) | -0.5645 | 0.3467 | ±0.6934 | -1.628 | 0.1035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **205**, R² = **0.0670**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2499**), Residual SE = **69.024** on **193** df, AIC = **2329.5**, BIC = **2369.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.4986** | 41.5301 | ±83.0603 | **+9.619** | **6.62e-22** | *** |
| Education: graduate level (vs college) | +9.2557 | 12.9988 | ±25.9975 | +0.712 | 0.4764 |  |
| Education: high school or below (vs college) | -19.8238 | 13.8968 | ±27.7935 | -1.427 | 0.1537 |  |
| Site: UCSD (vs UAB) | -10.2293 | 12.7987 | ±25.5974 | -0.799 | 0.4241 |  |
| Site: UW (vs UAB) | -12.9964 | 12.8026 | ±25.6051 | -1.015 | 0.3100 |  |
| Age (years) | +0.0070 | 0.5621 | ±1.1243 | +0.012 | 0.9901 |  |
| BMI (kg/m2) | -0.3851 | 0.6541 | ±1.3083 | -0.589 | 0.5561 |  |
| **Hypertension** | **-27.2497** | 12.0934 | ±24.1867 | **-2.253** | **0.0242** | * |
| High cholesterol | +7.8104 | 10.3234 | ±20.6468 | +0.757 | 0.4493 |  |
| Kidney disease | +5.2257 | 18.8483 | ±37.6965 | +0.277 | 0.7816 |  |
| Circulatory disease | +1.4120 | 11.7855 | ±23.5711 | +0.120 | 0.9046 |  |
| CV (%) | -0.3731 | 0.7619 | ±1.5238 | -0.490 | 0.6243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **205**, R² = **0.0664**, Adj R² = **0.0132**, F-statistic = **1.25** (p = **0.2575**), Residual SE = **69.046** on **193** df, AIC = **2329.7**, BIC = **2369.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.2335** | 48.7990 | ±97.5980 | **+7.894** | **2.92e-15** | *** |
| Education: graduate level (vs college) | +9.5965 | 12.9575 | ±25.9149 | +0.741 | 0.4589 |  |
| Education: high school or below (vs college) | -20.2467 | 13.9886 | ±27.9771 | -1.447 | 0.1478 |  |
| Site: UCSD (vs UAB) | -10.1136 | 12.8331 | ±25.6661 | -0.788 | 0.4306 |  |
| Site: UW (vs UAB) | -12.7673 | 12.8077 | ±25.6154 | -0.997 | 0.3188 |  |
| Age (years) | -0.0109 | 0.5580 | ±1.1161 | -0.019 | 0.9845 |  |
| BMI (kg/m2) | -0.3736 | 0.6546 | ±1.3092 | -0.571 | 0.5681 |  |
| **Hypertension** | **-27.2902** | 12.1159 | ±24.2318 | **-2.252** | **0.0243** | * |
| High cholesterol | +7.8416 | 10.3243 | ±20.6487 | +0.760 | 0.4475 |  |
| Kidney disease | +4.2883 | 18.2919 | ±36.5838 | +0.234 | 0.8146 |  |
| Circulatory disease | +1.7594 | 11.6890 | ±23.3781 | +0.151 | 0.8804 |  |
| Mean / SD ratio | +1.3006 | 3.9983 | ±7.9965 | +0.325 | 0.7450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0661**, Adj R² = **0.0128**, F-statistic = **1.24** (p = **0.2622**), Residual SE = **69.060** on **193** df, AIC = **2329.7**, BIC = **2369.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.0173** | 46.2554 | ±92.5108 | **+8.410** | **4.09e-17** | *** |
| Education: graduate level (vs college) | +9.8643 | 12.8744 | ±25.7487 | +0.766 | 0.4436 |  |
| Education: high school or below (vs college) | -20.6591 | 14.0068 | ±28.0137 | -1.475 | 0.1402 |  |
| Site: UCSD (vs UAB) | -10.1318 | 12.9143 | ±25.8286 | -0.785 | 0.4327 |  |
| Site: UW (vs UAB) | -12.6638 | 12.8103 | ±25.6206 | -0.989 | 0.3229 |  |
| Age (years) | -0.0315 | 0.5464 | ±1.0928 | -0.058 | 0.9541 |  |
| BMI (kg/m2) | -0.3738 | 0.6569 | ±1.3137 | -0.569 | 0.5693 |  |
| **Hypertension** | **-27.2832** | 12.1142 | ±24.2284 | **-2.252** | **0.0243** | * |
| High cholesterol | +7.9122 | 10.3087 | ±20.6174 | +0.768 | 0.4428 |  |
| Kidney disease | +3.7852 | 17.8639 | ±35.7277 | +0.212 | 0.8322 |  |
| Circulatory disease | +1.7316 | 11.7018 | ±23.4037 | +0.148 | 0.8824 |  |
| Avg. daily mean/SD | +0.6199 | 3.0975 | ±6.1949 | +0.200 | 0.8414 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **205**, R² = **0.1046**, Adj R² = **0.0536**, F-statistic = **2.05** (p = **0.0259**), Residual SE = **67.620** on **193** df, AIC = **2321.1**, BIC = **2361.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+439.0283** | 43.5885 | ±87.1770 | **+10.072** | **7.34e-24** | *** |
| Education: graduate level (vs college) | +6.9205 | 12.5316 | ±25.0632 | +0.552 | 0.5808 |  |
| Education: high school or below (vs college) | -13.9455 | 13.5960 | ±27.1920 | -1.026 | 0.3050 |  |
| Site: UCSD (vs UAB) | -8.4020 | 12.5196 | ±25.0391 | -0.671 | 0.5021 |  |
| Site: UW (vs UAB) | -15.9144 | 12.6269 | ±25.2539 | -1.260 | 0.2075 |  |
| Age (years) | +0.0497 | 0.5339 | ±1.0677 | +0.093 | 0.9259 |  |
| BMI (kg/m2) | -0.2072 | 0.6514 | ±1.3028 | -0.318 | 0.7504 |  |
| **Hypertension** | **-28.7958** | 11.6899 | ±23.3799 | **-2.463** | **0.0138** | * |
| High cholesterol | +9.0167 | 10.1056 | ±20.2112 | +0.892 | 0.3723 |  |
| Kidney disease | +4.3983 | 17.2424 | ±34.4849 | +0.255 | 0.7987 |  |
| Circulatory disease | +1.6602 | 11.6183 | ±23.2366 | +0.143 | 0.8864 |  |
| **MAG (mg/dL/h)** | **-1.2652** | 0.4792 | ±0.9585 | **-2.640** | **0.0083** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **205**, R² = **0.0787**, Adj R² = **0.0262**, F-statistic = **1.50** (p = **0.1341**), Residual SE = **68.589** on **193** df, AIC = **2326.9**, BIC = **2366.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.7207** | 42.0786 | ±84.1572 | **+9.808** | **1.04e-22** | *** |
| Education: graduate level (vs college) | +7.4674 | 12.8377 | ±25.6755 | +0.582 | 0.5608 |  |
| Education: high school or below (vs college) | -16.0895 | 13.8284 | ±27.6569 | -1.164 | 0.2446 |  |
| Site: UCSD (vs UAB) | -10.0492 | 12.5425 | ±25.0851 | -0.801 | 0.4230 |  |
| Site: UW (vs UAB) | -13.1998 | 12.9477 | ±25.8955 | -1.019 | 0.3080 |  |
| Age (years) | +0.0609 | 0.5426 | ±1.0852 | +0.112 | 0.9107 |  |
| BMI (kg/m2) | -0.4391 | 0.6594 | ±1.3188 | -0.666 | 0.5055 |  |
| **Hypertension** | **-27.8680** | 11.8729 | ±23.7457 | **-2.347** | **0.0189** | * |
| High cholesterol | +8.1866 | 10.1994 | ±20.3988 | +0.803 | 0.4222 |  |
| Kidney disease | +8.3452 | 18.2464 | ±36.4928 | +0.457 | 0.6474 |  |
| Circulatory disease | +1.4946 | 11.7150 | ±23.4299 | +0.128 | 0.8985 |  |
| Avg. daily range (mg/dL) | -0.1768 | 0.1030 | ±0.2060 | -1.716 | 0.0861 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **205**, R² = **0.0847**, Adj R² = **0.0325**, F-statistic = **1.62** (p = **0.0946**), Residual SE = **68.367** on **193** df, AIC = **2325.6**, BIC = **2365.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.3204** | 39.8019 | ±79.6038 | **+10.083** | **6.57e-24** | *** |
| Education: graduate level (vs college) | +7.0555 | 13.1066 | ±26.2131 | +0.538 | 0.5904 |  |
| Education: high school or below (vs college) | -20.0945 | 13.2515 | ±26.5030 | -1.516 | 0.1294 |  |
| Site: UCSD (vs UAB) | -9.9577 | 12.4468 | ±24.8936 | -0.800 | 0.4237 |  |
| Site: UW (vs UAB) | -13.9970 | 12.8768 | ±25.7535 | -1.087 | 0.2770 |  |
| Age (years) | +0.0334 | 0.5424 | ±1.0847 | +0.062 | 0.9508 |  |
| BMI (kg/m2) | -0.4023 | 0.6415 | ±1.2830 | -0.627 | 0.5306 |  |
| **Hypertension** | **-25.2742** | 12.0396 | ±24.0791 | **-2.099** | **0.0358** | * |
| High cholesterol | +7.0653 | 10.2369 | ±20.4737 | +0.690 | 0.4901 |  |
| Kidney disease | +7.4136 | 18.0438 | ±36.0875 | +0.411 | 0.6812 |  |
| Circulatory disease | +2.6125 | 11.3704 | ±22.7407 | +0.230 | 0.8183 |  |
| SD of daily means (mg/dL) | -1.0069 | 0.5231 | ±1.0461 | -1.925 | 0.0542 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **205**, R² = **0.0920**, Adj R² = **0.0403**, F-statistic = **1.78** (p = **0.0599**), Residual SE = **68.092** on **193** df, AIC = **2324.0**, BIC = **2363.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+338.1655** | 47.3798 | ±94.7596 | **+7.137** | **9.52e-13** | *** |
| Education: graduate level (vs college) | +6.3525 | 12.8598 | ±25.7196 | +0.494 | 0.6213 |  |
| Education: high school or below (vs college) | -18.2529 | 13.1255 | ±26.2511 | -1.391 | 0.1643 |  |
| Site: UCSD (vs UAB) | -10.7537 | 12.2875 | ±24.5751 | -0.875 | 0.3815 |  |
| Site: UW (vs UAB) | -13.9103 | 12.9611 | ±25.9221 | -1.073 | 0.2832 |  |
| Age (years) | +0.0288 | 0.5334 | ±1.0669 | +0.054 | 0.9570 |  |
| BMI (kg/m2) | -0.4231 | 0.6525 | ±1.3050 | -0.648 | 0.5168 |  |
| **Hypertension** | **-27.3557** | 11.8674 | ±23.7348 | **-2.305** | **0.0212** | * |
| High cholesterol | +8.6894 | 10.0794 | ±20.1587 | +0.862 | 0.3886 |  |
| Kidney disease | +8.1416 | 17.7240 | ±35.4481 | +0.459 | 0.6460 |  |
| Circulatory disease | +2.7740 | 11.4869 | ±22.9737 | +0.241 | 0.8092 |  |
| **Time in range 70-180, pooled (%)** | **+0.6249** | 0.2602 | ±0.5205 | **+2.401** | **0.0163** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **205**, R² = **0.0925**, Adj R² = **0.0407**, F-statistic = **1.79** (p = **0.0584**), Residual SE = **68.077** on **193** df, AIC = **2323.9**, BIC = **2363.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+337.9719** | 47.6355 | ±95.2710 | **+7.095** | **1.29e-12** | *** |
| Education: graduate level (vs college) | +6.3132 | 12.9134 | ±25.8267 | +0.489 | 0.6249 |  |
| Education: high school or below (vs college) | -17.8891 | 13.1238 | ±26.2475 | -1.363 | 0.1728 |  |
| Site: UCSD (vs UAB) | -10.9388 | 12.2940 | ±24.5880 | -0.890 | 0.3736 |  |
| Site: UW (vs UAB) | -14.0260 | 12.9764 | ±25.9527 | -1.081 | 0.2797 |  |
| Age (years) | +0.0288 | 0.5336 | ±1.0672 | +0.054 | 0.9569 |  |
| BMI (kg/m2) | -0.4377 | 0.6547 | ±1.3094 | -0.669 | 0.5037 |  |
| **Hypertension** | **-27.4672** | 11.8932 | ±23.7864 | **-2.309** | **0.0209** | * |
| High cholesterol | +8.7482 | 10.0664 | ±20.1329 | +0.869 | 0.3848 |  |
| Kidney disease | +8.3059 | 17.7765 | ±35.5530 | +0.467 | 0.6403 |  |
| Circulatory disease | +2.8849 | 11.4983 | ±22.9966 | +0.251 | 0.8019 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.6302** | 0.2667 | ±0.5334 | **+2.363** | **0.0181** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **205**, R² = **0.0742**, Adj R² = **0.0215**, F-statistic = **1.41** (p = **0.1723**), Residual SE = **68.757** on **193** df, AIC = **2327.9**, BIC = **2367.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.5639** | 40.6494 | ±81.2989 | **+9.608** | **7.39e-22** | *** |
| Education: graduate level (vs college) | +11.2051 | 12.8272 | ±25.6544 | +0.874 | 0.3824 |  |
| Education: high school or below (vs college) | -19.8533 | 13.7641 | ±27.5283 | -1.442 | 0.1492 |  |
| Site: UCSD (vs UAB) | -8.3356 | 12.9055 | ±25.8111 | -0.646 | 0.5184 |  |
| Site: UW (vs UAB) | -10.0850 | 13.0527 | ±26.1054 | -0.773 | 0.4397 |  |
| Age (years) | -0.0702 | 0.5420 | ±1.0841 | -0.130 | 0.8969 |  |
| BMI (kg/m2) | -0.3760 | 0.6470 | ±1.2940 | -0.581 | 0.5611 |  |
| **Hypertension** | **-27.8316** | 12.1856 | ±24.3713 | **-2.284** | **0.0224** | * |
| High cholesterol | +7.5486 | 10.2911 | ±20.5822 | +0.734 | 0.4633 |  |
| Kidney disease | +3.7796 | 17.4883 | ±34.9767 | +0.216 | 0.8289 |  |
| Circulatory disease | +0.2356 | 11.5197 | ±23.0395 | +0.020 | 0.9837 |  |
| Time < 54 (%) | +8.4301 | 4.5816 | ±9.1632 | +1.840 | 0.0658 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **205**, R² = **0.0708**, Adj R² = **0.0178**, F-statistic = **1.34** (p = **0.2067**), Residual SE = **68.885** on **193** df, AIC = **2328.7**, BIC = **2368.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.0664** | 40.8460 | ±81.6919 | **+9.623** | **6.39e-22** | *** |
| Education: graduate level (vs college) | +11.2428 | 12.8448 | ±25.6896 | +0.875 | 0.3814 |  |
| Education: high school or below (vs college) | -20.2772 | 13.7311 | ±27.4621 | -1.477 | 0.1397 |  |
| Site: UCSD (vs UAB) | -9.0843 | 12.9029 | ±25.8058 | -0.704 | 0.4814 |  |
| Site: UW (vs UAB) | -11.1930 | 12.9207 | ±25.8414 | -0.866 | 0.3863 |  |
| Age (years) | -0.0902 | 0.5435 | ±1.0869 | -0.166 | 0.8682 |  |
| BMI (kg/m2) | -0.3668 | 0.6533 | ±1.3067 | -0.561 | 0.5745 |  |
| **Hypertension** | **-27.4430** | 12.1760 | ±24.3520 | **-2.254** | **0.0242** | * |
| High cholesterol | +8.0886 | 10.2791 | ±20.5583 | +0.787 | 0.4313 |  |
| Kidney disease | +3.3306 | 17.5245 | ±35.0490 | +0.190 | 0.8493 |  |
| Circulatory disease | +0.7262 | 11.5293 | ±23.0585 | +0.063 | 0.9498 |  |
| Avg. daily time < 54 (%) | +5.8324 | 4.6481 | ±9.2962 | +1.255 | 0.2096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **205**, R² = **0.0671**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2493**), Residual SE = **69.022** on **193** df, AIC = **2329.5**, BIC = **2369.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.5258** | 40.9201 | ±81.8401 | **+9.617** | **6.78e-22** | *** |
| Education: graduate level (vs college) | +11.1794 | 12.9121 | ±25.8242 | +0.866 | 0.3866 |  |
| Education: high school or below (vs college) | -21.4370 | 13.8023 | ±27.6047 | -1.553 | 0.1204 |  |
| Site: UCSD (vs UAB) | -9.7867 | 12.8853 | ±25.7707 | -0.760 | 0.4475 |  |
| Site: UW (vs UAB) | -12.3584 | 12.8608 | ±25.7216 | -0.961 | 0.3366 |  |
| Age (years) | -0.0902 | 0.5482 | ±1.0964 | -0.165 | 0.8692 |  |
| BMI (kg/m2) | -0.3639 | 0.6522 | ±1.3044 | -0.558 | 0.5769 |  |
| **Hypertension** | **-27.0724** | 12.2528 | ±24.5056 | **-2.209** | **0.0271** | * |
| High cholesterol | +7.6854 | 10.3447 | ±20.6893 | +0.743 | 0.4575 |  |
| Kidney disease | +3.3437 | 17.5552 | ±35.1103 | +0.190 | 0.8489 |  |
| Circulatory disease | +1.6800 | 11.6975 | ±23.3950 | +0.144 | 0.8858 |  |
| Time 54-69, pooled (%) | +0.9819 | 2.2122 | ±4.4243 | +0.444 | 0.6571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **205**, R² = **0.0663**, Adj R² = **0.0131**, F-statistic = **1.25** (p = **0.2592**), Residual SE = **69.051** on **193** df, AIC = **2329.7**, BIC = **2369.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.9304** | 40.9270 | ±81.8540 | **+9.625** | **6.26e-22** | *** |
| Education: graduate level (vs college) | +10.7718 | 12.9269 | ±25.8537 | +0.833 | 0.4047 |  |
| Education: high school or below (vs college) | -21.4016 | 13.8414 | ±27.6829 | -1.546 | 0.1221 |  |
| Site: UCSD (vs UAB) | -10.0121 | 12.9038 | ±25.8077 | -0.776 | 0.4378 |  |
| Site: UW (vs UAB) | -12.4843 | 12.8307 | ±25.6614 | -0.973 | 0.3306 |  |
| Age (years) | -0.0801 | 0.5485 | ±1.0970 | -0.146 | 0.8838 |  |
| BMI (kg/m2) | -0.3665 | 0.6537 | ±1.3074 | -0.561 | 0.5750 |  |
| **Hypertension** | **-27.1109** | 12.2384 | ±24.4768 | **-2.215** | **0.0267** | * |
| High cholesterol | +7.7705 | 10.3408 | ±20.6817 | +0.751 | 0.4524 |  |
| Kidney disease | +3.3929 | 17.4922 | ±34.9844 | +0.194 | 0.8462 |  |
| Circulatory disease | +1.7227 | 11.7011 | ±23.4023 | +0.147 | 0.8830 |  |
| Avg. daily time 54-69 (%) | +0.5458 | 1.9810 | ±3.9621 | +0.276 | 0.7829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **205**, R² = **0.0685**, Adj R² = **0.0155**, F-statistic = **1.29** (p = **0.2319**), Residual SE = **68.968** on **193** df, AIC = **2329.2**, BIC = **2369.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.9884** | 40.9045 | ±81.8090 | **+9.607** | **7.44e-22** | *** |
| Education: graduate level (vs college) | +11.5127 | 12.9020 | ±25.8040 | +0.892 | 0.3722 |  |
| Education: high school or below (vs college) | -21.2855 | 13.7404 | ±27.4809 | -1.549 | 0.1214 |  |
| Site: UCSD (vs UAB) | -9.4085 | 12.8942 | ±25.7883 | -0.730 | 0.4656 |  |
| Site: UW (vs UAB) | -11.9301 | 12.9111 | ±25.8222 | -0.924 | 0.3555 |  |
| Age (years) | -0.0985 | 0.5481 | ±1.0962 | -0.180 | 0.8574 |  |
| BMI (kg/m2) | -0.3637 | 0.6504 | ±1.3007 | -0.559 | 0.5761 |  |
| **Hypertension** | **-27.1536** | 12.2588 | ±24.5175 | **-2.215** | **0.0268** | * |
| High cholesterol | +7.6091 | 10.3410 | ±20.6820 | +0.736 | 0.4618 |  |
| Kidney disease | +3.3592 | 17.5655 | ±35.1311 | +0.191 | 0.8483 |  |
| Circulatory disease | +1.4492 | 11.6710 | ±23.3421 | +0.124 | 0.9012 |  |
| Time < 70 (%) | +1.1954 | 1.7028 | ±3.4055 | +0.702 | 0.4827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **205**, R² = **0.0671**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2492**), Residual SE = **69.021** on **193** df, AIC = **2329.5**, BIC = **2369.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8583** | 40.9361 | ±81.8721 | **+9.621** | **6.50e-22** | *** |
| Education: graduate level (vs college) | +11.0941 | 12.9302 | ±25.8604 | +0.858 | 0.3909 |  |
| Education: high school or below (vs college) | -21.3421 | 13.7742 | ±27.5484 | -1.549 | 0.1213 |  |
| Site: UCSD (vs UAB) | -9.7617 | 12.9114 | ±25.8229 | -0.756 | 0.4496 |  |
| Site: UW (vs UAB) | -12.2305 | 12.8650 | ±25.7300 | -0.951 | 0.3418 |  |
| Age (years) | -0.0920 | 0.5486 | ±1.0972 | -0.168 | 0.8668 |  |
| BMI (kg/m2) | -0.3650 | 0.6528 | ±1.3057 | -0.559 | 0.5761 |  |
| **Hypertension** | **-27.1359** | 12.2446 | ±24.4891 | **-2.216** | **0.0267** | * |
| High cholesterol | +7.7740 | 10.3385 | ±20.6770 | +0.752 | 0.4521 |  |
| Kidney disease | +3.3440 | 17.5087 | ±35.0174 | +0.191 | 0.8485 |  |
| Circulatory disease | +1.5786 | 11.6747 | ±23.3494 | +0.135 | 0.8924 |  |
| Avg. daily time < 70 (%) | +0.7548 | 1.5239 | ±3.0479 | +0.495 | 0.6204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **205**, R² = **0.0900**, Adj R² = **0.0382**, F-statistic = **1.74** (p = **0.0681**), Residual SE = **68.168** on **193** df, AIC = **2324.4**, BIC = **2364.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+285.8052** | 60.0897 | ±120.1795 | **+4.756** | **1.97e-06** | *** |
| Education: graduate level (vs college) | +8.1879 | 12.7153 | ±25.4307 | +0.644 | 0.5196 |  |
| Education: high school or below (vs college) | -18.2000 | 13.1185 | ±26.2370 | -1.387 | 0.1653 |  |
| Site: UCSD (vs UAB) | -10.8490 | 12.4401 | ±24.8802 | -0.872 | 0.3832 |  |
| Site: UW (vs UAB) | -15.1612 | 12.7348 | ±25.4695 | -1.191 | 0.2338 |  |
| Age (years) | -0.0765 | 0.5242 | ±1.0484 | -0.146 | 0.8839 |  |
| BMI (kg/m2) | -0.4207 | 0.6534 | ±1.3067 | -0.644 | 0.5196 |  |
| **Hypertension** | **-26.2930** | 11.8747 | ±23.7494 | **-2.214** | **0.0268** | * |
| High cholesterol | +6.6256 | 10.1985 | ±20.3970 | +0.650 | 0.5159 |  |
| Kidney disease | +5.7265 | 17.2771 | ±34.5543 | +0.331 | 0.7403 |  |
| Circulatory disease | +3.1999 | 11.5213 | ±23.0426 | +0.278 | 0.7812 |  |
| **Time 54-250, pooled (%)** | **+1.1569** | 0.4708 | ±0.9415 | **+2.457** | **0.0140** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **205**, R² = **0.0932**, Adj R² = **0.0415**, F-statistic = **1.80** (p = **0.0558**), Residual SE = **68.050** on **193** df, AIC = **2323.7**, BIC = **2363.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+265.1368** | 62.3703 | ±124.7407 | **+4.251** | **2.13e-05** | *** |
| Education: graduate level (vs college) | +7.8150 | 12.7251 | ±25.4503 | +0.614 | 0.5391 |  |
| Education: high school or below (vs college) | -17.3868 | 13.0896 | ±26.1793 | -1.328 | 0.1841 |  |
| Site: UCSD (vs UAB) | -10.6384 | 12.3885 | ±24.7769 | -0.859 | 0.3905 |  |
| Site: UW (vs UAB) | -15.0953 | 12.7344 | ±25.4688 | -1.185 | 0.2359 |  |
| Age (years) | -0.0630 | 0.5243 | ±1.0486 | -0.120 | 0.9043 |  |
| BMI (kg/m2) | -0.4458 | 0.6547 | ±1.3094 | -0.681 | 0.4959 |  |
| **Hypertension** | **-26.1771** | 11.8651 | ±23.7303 | **-2.206** | **0.0274** | * |
| High cholesterol | +6.5994 | 10.1890 | ±20.3780 | +0.648 | 0.5172 |  |
| Kidney disease | +6.3897 | 17.3009 | ±34.6018 | +0.369 | 0.7119 |  |
| Circulatory disease | +3.6723 | 11.5332 | ±23.0664 | +0.318 | 0.7502 |  |
| **Avg. daily time 54-250 (%)** | **+1.3632** | 0.5023 | ±1.0045 | **+2.714** | **0.0066** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **205**, R² = **0.0828**, Adj R² = **0.0306**, F-statistic = **1.58** (p = **0.1057**), Residual SE = **68.436** on **193** df, AIC = **2326.0**, BIC = **2365.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.8669** | 40.9260 | ±81.8520 | **+9.697** | **3.10e-22** | *** |
| Education: graduate level (vs college) | +7.5687 | 12.8477 | ±25.6955 | +0.589 | 0.5558 |  |
| Education: high school or below (vs college) | -19.7527 | 13.3827 | ±26.7654 | -1.476 | 0.1399 |  |
| Site: UCSD (vs UAB) | -10.1042 | 12.4207 | ±24.8413 | -0.813 | 0.4159 |  |
| Site: UW (vs UAB) | -12.3047 | 13.1032 | ±26.2063 | -0.939 | 0.3477 |  |
| Age (years) | +0.0356 | 0.5433 | ±1.0867 | +0.066 | 0.9477 |  |
| BMI (kg/m2) | -0.3968 | 0.6501 | ±1.3002 | -0.610 | 0.5416 |  |
| **Hypertension** | **-27.9077** | 12.0328 | ±24.0656 | **-2.319** | **0.0204** | * |
| High cholesterol | +9.5571 | 10.1487 | ±20.2974 | +0.942 | 0.3463 |  |
| Kidney disease | +7.5878 | 17.9694 | ±35.9389 | +0.422 | 0.6728 |  |
| Circulatory disease | +1.9889 | 11.5836 | ±23.1673 | +0.172 | 0.8637 |  |
| Time 181-250, pooled (%) | -0.7632 | 0.4076 | ±0.8153 | -1.872 | 0.0612 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **205**, R² = **0.0829**, Adj R² = **0.0306**, F-statistic = **1.59** (p = **0.1055**), Residual SE = **68.435** on **193** df, AIC = **2326.0**, BIC = **2365.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.2124** | 40.9332 | ±81.8665 | **+9.728** | **2.28e-22** | *** |
| Education: graduate level (vs college) | +7.6416 | 12.9054 | ±25.8107 | +0.592 | 0.5538 |  |
| Education: high school or below (vs college) | -19.6202 | 13.3491 | ±26.6982 | -1.470 | 0.1416 |  |
| Site: UCSD (vs UAB) | -10.5094 | 12.4350 | ±24.8700 | -0.845 | 0.3980 |  |
| Site: UW (vs UAB) | -12.7104 | 13.1144 | ±26.2288 | -0.969 | 0.3324 |  |
| Age (years) | +0.0182 | 0.5414 | ±1.0829 | +0.034 | 0.9732 |  |
| BMI (kg/m2) | -0.4042 | 0.6524 | ±1.3047 | -0.620 | 0.5355 |  |
| **Hypertension** | **-28.0024** | 12.0560 | ±24.1120 | **-2.323** | **0.0202** | * |
| High cholesterol | +9.4837 | 10.1458 | ±20.2916 | +0.935 | 0.3499 |  |
| Kidney disease | +7.4615 | 17.9842 | ±35.9685 | +0.415 | 0.6782 |  |
| Circulatory disease | +2.0003 | 11.6076 | ±23.2152 | +0.172 | 0.8632 |  |
| Avg. daily time 181-250 (%) | -0.7408 | 0.4088 | ±0.8175 | -1.812 | 0.0699 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **205**, R² = **0.0937**, Adj R² = **0.0421**, F-statistic = **1.81** (p = **0.0538**), Residual SE = **68.029** on **193** df, AIC = **2323.6**, BIC = **2363.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.2707** | 40.4826 | ±80.9652 | **+9.887** | **4.72e-23** | *** |
| Education: graduate level (vs college) | +6.9721 | 12.8442 | ±25.6884 | +0.543 | 0.5873 |  |
| Education: high school or below (vs college) | -18.2489 | 13.0875 | ±26.1750 | -1.394 | 0.1632 |  |
| Site: UCSD (vs UAB) | -10.3055 | 12.2610 | ±24.5221 | -0.841 | 0.4006 |  |
| Site: UW (vs UAB) | -13.5413 | 13.0271 | ±26.0542 | -1.039 | 0.2986 |  |
| Age (years) | +0.0091 | 0.5329 | ±1.0659 | +0.017 | 0.9864 |  |
| BMI (kg/m2) | -0.4206 | 0.6494 | ±1.2987 | -0.648 | 0.5172 |  |
| **Hypertension** | **-27.3619** | 11.9021 | ±23.8042 | **-2.299** | **0.0215** | * |
| High cholesterol | +8.5743 | 10.0752 | ±20.1504 | +0.851 | 0.3947 |  |
| Kidney disease | +8.1311 | 17.7460 | ±35.4921 | +0.458 | 0.6468 |  |
| Circulatory disease | +2.6247 | 11.4598 | ±22.9196 | +0.229 | 0.8188 |  |
| **Time > 180 (%)** | **-0.6315** | 0.2563 | ±0.5126 | **-2.464** | **0.0137** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **205**, R² = **0.0938**, Adj R² = **0.0421**, F-statistic = **1.82** (p = **0.0537**), Residual SE = **68.028** on **193** df, AIC = **2323.6**, BIC = **2363.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.0644** | 40.5731 | ±81.1461 | **+9.885** | **4.84e-23** | *** |
| Education: graduate level (vs college) | +6.9752 | 12.8863 | ±25.7725 | +0.541 | 0.5883 |  |
| Education: high school or below (vs college) | -17.9468 | 13.0853 | ±26.1707 | -1.372 | 0.1702 |  |
| Site: UCSD (vs UAB) | -10.5198 | 12.2626 | ±24.5252 | -0.858 | 0.3910 |  |
| Site: UW (vs UAB) | -13.6831 | 13.0585 | ±26.1170 | -1.048 | 0.2947 |  |
| Age (years) | +0.0023 | 0.5330 | ±1.0660 | +0.004 | 0.9966 |  |
| BMI (kg/m2) | -0.4347 | 0.6527 | ±1.3054 | -0.666 | 0.5054 |  |
| **Hypertension** | **-27.4618** | 11.9379 | ±23.8758 | **-2.300** | **0.0214** | * |
| High cholesterol | +8.6985 | 10.0651 | ±20.1301 | +0.864 | 0.3875 |  |
| Kidney disease | +8.2465 | 17.7969 | ±35.5939 | +0.463 | 0.6431 |  |
| Circulatory disease | +2.7500 | 11.4794 | ±22.9588 | +0.240 | 0.8107 |  |
| **Avg. daily time > 180 (%)** | **-0.6365** | 0.2667 | ±0.5334 | **-2.387** | **0.0170** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **205**, R² = **0.0831**, Adj R² = **0.0309**, F-statistic = **1.59** (p = **0.1039**), Residual SE = **68.426** on **193** df, AIC = **2326.0**, BIC = **2365.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.4226** | 40.5053 | ±81.0107 | **+9.836** | **7.85e-23** | *** |
| Education: graduate level (vs college) | +8.3124 | 12.9115 | ±25.8230 | +0.644 | 0.5197 |  |
| Education: high school or below (vs college) | -19.9602 | 13.1835 | ±26.3669 | -1.514 | 0.1300 |  |
| Site: UCSD (vs UAB) | -10.4809 | 12.3977 | ±24.7954 | -0.845 | 0.3979 |  |
| Site: UW (vs UAB) | -13.5152 | 13.0681 | ±26.1361 | -1.034 | 0.3010 |  |
| Age (years) | -0.0583 | 0.5348 | ±1.0696 | -0.109 | 0.9132 |  |
| BMI (kg/m2) | -0.3874 | 0.6496 | ±1.2992 | -0.596 | 0.5509 |  |
| **Hypertension** | **-26.2139** | 12.0933 | ±24.1866 | **-2.168** | **0.0302** | * |
| High cholesterol | +8.8318 | 10.0998 | ±20.1997 | +0.874 | 0.3819 |  |
| Kidney disease | +5.3596 | 17.5896 | ±35.1792 | +0.305 | 0.7606 |  |
| Circulatory disease | +3.2454 | 11.4773 | ±22.9547 | +0.283 | 0.7774 |  |
| Nocturnal time > 180 (%) | -0.4919 | 0.2650 | ±0.5300 | -1.856 | 0.0634 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **205**, R² = **0.0921**, Adj R² = **0.0403**, F-statistic = **1.78** (p = **0.0598**), Residual SE = **68.091** on **193** df, AIC = **2323.9**, BIC = **2363.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.9023** | 40.5000 | ±81.0001 | **+9.849** | **6.89e-23** | *** |
| Education: graduate level (vs college) | +6.4104 | 12.7633 | ±25.5266 | +0.502 | 0.6155 |  |
| Education: high school or below (vs college) | -18.7538 | 13.8310 | ±27.6620 | -1.356 | 0.1751 |  |
| Site: UCSD (vs UAB) | -9.4791 | 12.3029 | ±24.6057 | -0.770 | 0.4410 |  |
| Site: UW (vs UAB) | -9.9111 | 13.1498 | ±26.2997 | -0.754 | 0.4510 |  |
| Age (years) | +0.1416 | 0.5592 | ±1.1184 | +0.253 | 0.8001 |  |
| BMI (kg/m2) | -0.5503 | 0.6399 | ±1.2797 | -0.860 | 0.3898 |  |
| **Hypertension** | **-26.6842** | 11.7820 | ±23.5640 | **-2.265** | **0.0235** | * |
| High cholesterol | +8.4182 | 10.1931 | ±20.3862 | +0.826 | 0.4089 |  |
| Kidney disease | +9.1991 | 17.8918 | ±35.7835 | +0.514 | 0.6071 |  |
| Circulatory disease | +1.2695 | 11.6406 | ±23.2812 | +0.109 | 0.9132 |  |
| **Any reading > 250 during wear (0/1)** | **-23.9643** | 11.3237 | ±22.6475 | **-2.116** | **0.0343** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **205**, R² = **0.0926**, Adj R² = **0.0409**, F-statistic = **1.79** (p = **0.0577**), Residual SE = **68.070** on **193** df, AIC = **2323.8**, BIC = **2363.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.4570** | 39.9793 | ±79.9586 | **+10.042** | **1.00e-23** | *** |
| Education: graduate level (vs college) | +8.2049 | 12.7136 | ±25.4273 | +0.645 | 0.5187 |  |
| Education: high school or below (vs college) | -17.8241 | 13.0996 | ±26.1993 | -1.361 | 0.1736 |  |
| Site: UCSD (vs UAB) | -10.6024 | 12.4094 | ±24.8188 | -0.854 | 0.3929 |  |
| Site: UW (vs UAB) | -14.9334 | 12.7361 | ±25.4723 | -1.173 | 0.2410 |  |
| Age (years) | -0.0791 | 0.5239 | ±1.0478 | -0.151 | 0.8800 |  |
| BMI (kg/m2) | -0.4246 | 0.6517 | ±1.3033 | -0.652 | 0.5147 |  |
| **Hypertension** | **-26.3431** | 11.8706 | ±23.7413 | **-2.219** | **0.0265** | * |
| High cholesterol | +6.5122 | 10.1896 | ±20.3791 | +0.639 | 0.5228 |  |
| Kidney disease | +5.9015 | 17.2679 | ±34.5358 | +0.342 | 0.7325 |  |
| Circulatory disease | +3.0635 | 11.4824 | ±22.9647 | +0.267 | 0.7896 |  |
| **Time > 250 (%)** | **-1.2238** | 0.4704 | ±0.9409 | **-2.601** | **0.0093** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 205)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **205**, R² = **0.0962**, Adj R² = **0.0446**, F-statistic = **1.87** (p = **0.0459**), Residual SE = **67.938** on **193** df, AIC = **2323.0**, BIC = **2362.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.7580** | 39.9952 | ±79.9903 | **+10.045** | **9.65e-24** | *** |
| Education: graduate level (vs college) | +7.9002 | 12.7175 | ±25.4350 | +0.621 | 0.5345 |  |
| Education: high school or below (vs college) | -16.8987 | 13.0883 | ±26.1766 | -1.291 | 0.1967 |  |
| Site: UCSD (vs UAB) | -10.3682 | 12.3535 | ±24.7070 | -0.839 | 0.4013 |  |
| Site: UW (vs UAB) | -14.8904 | 12.7462 | ±25.4924 | -1.168 | 0.2427 |  |
| Age (years) | -0.0709 | 0.5238 | ±1.0475 | -0.135 | 0.8923 |  |
| BMI (kg/m2) | -0.4501 | 0.6540 | ±1.3080 | -0.688 | 0.4913 |  |
| **Hypertension** | **-26.1880** | 11.8644 | ±23.7287 | **-2.207** | **0.0273** | * |
| High cholesterol | +6.5794 | 10.1717 | ±20.3433 | +0.647 | 0.5177 |  |
| Kidney disease | +6.5440 | 17.2989 | ±34.5979 | +0.378 | 0.7052 |  |
| Circulatory disease | +3.5417 | 11.5035 | ±23.0071 | +0.308 | 0.7582 |  |
| **Avg. daily time > 250 (%)** | **-1.4518** | 0.5262 | ±1.0525 | **-2.759** | **0.0058** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 203; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0902**, F-statistic = **3.00** (p = **0.0015**), Residual SE = **17.191** on **192** df, AIC = **1741.6**, BIC = **1778.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6324** | 11.0727 | ±22.1454 | **+6.108** | **1.01e-09** | *** |
| Education: graduate level (vs college) | -4.2421 | 2.8759 | ±5.7519 | -1.475 | 0.1402 |  |
| Education: high school or below (vs college) | -2.1048 | 3.5617 | ±7.1233 | -0.591 | 0.5546 |  |
| Site: UCSD (vs UAB) | +3.7145 | 3.3753 | ±6.7507 | +1.100 | 0.2711 |  |
| Site: UW (vs UAB) | +2.3003 | 3.3203 | ±6.6406 | +0.693 | 0.4884 |  |
| **Age (years)** | **-0.3506** | 0.1247 | ±0.2494 | **-2.811** | **0.0049** | ** |
| BMI (kg/m2) | +0.3236 | 0.1784 | ±0.3569 | +1.813 | 0.0698 | . |
| Hypertension | +1.6360 | 3.0762 | ±6.1523 | +0.532 | 0.5949 |  |
| High cholesterol | +1.1081 | 2.5558 | ±5.1117 | +0.434 | 0.6646 |  |
| Kidney disease | -1.3941 | 4.2140 | ±8.4280 | -0.331 | 0.7408 |  |
| **Circulatory disease** | **-6.4010** | 3.1006 | ±6.2012 | **-2.064** | **0.0390** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **203**, R² = **0.1429**, Adj R² = **0.0936**, F-statistic = **2.90** (p = **0.0015**), Residual SE = **17.159** on **191** df, AIC = **1741.8**, BIC = **1781.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1462** | 13.3881 | ±26.7763 | **+4.492** | **7.04e-06** | *** |
| Education: graduate level (vs college) | -3.7695 | 2.9377 | ±5.8753 | -1.283 | 0.1994 |  |
| Education: high school or below (vs college) | -2.5414 | 3.4876 | ±6.9751 | -0.729 | 0.4662 |  |
| Site: UCSD (vs UAB) | +3.8491 | 3.3698 | ±6.7395 | +1.142 | 0.2534 |  |
| Site: UW (vs UAB) | +2.4517 | 3.2934 | ±6.5868 | +0.744 | 0.4566 |  |
| **Age (years)** | **-0.3759** | 0.1253 | ±0.2506 | **-3.000** | **0.0027** | ** |
| BMI (kg/m2) | +0.3152 | 0.1763 | ±0.3526 | +1.788 | 0.0739 | . |
| Hypertension | +1.5542 | 3.0803 | ±6.1606 | +0.505 | 0.6139 |  |
| High cholesterol | +1.2333 | 2.5726 | ±5.1452 | +0.479 | 0.6316 |  |
| Kidney disease | -1.4062 | 4.1097 | ±8.2194 | -0.342 | 0.7322 |  |
| **Circulatory disease** | **-6.3256** | 3.1465 | ±6.2929 | **-2.010** | **0.0444** | * |
| HbA1c (%) | +1.4186 | 1.3551 | ±2.7101 | +1.047 | 0.2952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **203**, R² = **0.1394**, Adj R² = **0.0899**, F-statistic = **2.81** (p = **0.0020**), Residual SE = **17.194** on **191** df, AIC = **1742.6**, BIC = **1782.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7831** | 12.7656 | ±25.5312 | **+4.918** | **8.74e-07** | *** |
| Education: graduate level (vs college) | -4.0864 | 2.9015 | ±5.8030 | -1.408 | 0.1590 |  |
| Education: high school or below (vs college) | -2.3913 | 3.4901 | ±6.9802 | -0.685 | 0.4932 |  |
| Site: UCSD (vs UAB) | +3.6563 | 3.3925 | ±6.7851 | +1.078 | 0.2811 |  |
| Site: UW (vs UAB) | +2.3845 | 3.3070 | ±6.6139 | +0.721 | 0.4709 |  |
| **Age (years)** | **-0.3525** | 0.1243 | ±0.2487 | **-2.835** | **0.0046** | ** |
| BMI (kg/m2) | +0.3252 | 0.1792 | ±0.3584 | +1.815 | 0.0696 | . |
| Hypertension | +1.6274 | 3.1051 | ±6.2102 | +0.524 | 0.6002 |  |
| High cholesterol | +1.1191 | 2.5819 | ±5.1639 | +0.433 | 0.6647 |  |
| Kidney disease | -1.6906 | 4.1425 | ±8.2849 | -0.408 | 0.6832 |  |
| **Circulatory disease** | **-6.4622** | 3.1481 | ±6.2961 | **-2.053** | **0.0401** | * |
| Mean glucose (mg/dL) | +0.0362 | 0.0434 | ±0.0868 | +0.835 | 0.4040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **203**, R² = **0.1394**, Adj R² = **0.0899**, F-statistic = **2.81** (p = **0.0020**), Residual SE = **17.194** on **191** df, AIC = **1742.6**, BIC = **1782.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7697** | 16.6052 | ±33.2105 | **+3.479** | **5.03e-04** | *** |
| Education: graduate level (vs college) | -4.0864 | 2.9015 | ±5.8030 | -1.408 | 0.1590 |  |
| Education: high school or below (vs college) | -2.3913 | 3.4901 | ±6.9802 | -0.685 | 0.4932 |  |
| Site: UCSD (vs UAB) | +3.6563 | 3.3925 | ±6.7851 | +1.078 | 0.2811 |  |
| Site: UW (vs UAB) | +2.3845 | 3.3070 | ±6.6139 | +0.721 | 0.4709 |  |
| **Age (years)** | **-0.3525** | 0.1243 | ±0.2487 | **-2.835** | **0.0046** | ** |
| BMI (kg/m2) | +0.3252 | 0.1792 | ±0.3584 | +1.815 | 0.0696 | . |
| Hypertension | +1.6274 | 3.1051 | ±6.2102 | +0.524 | 0.6002 |  |
| High cholesterol | +1.1191 | 2.5819 | ±5.1639 | +0.433 | 0.6647 |  |
| Kidney disease | -1.6906 | 4.1425 | ±8.2849 | -0.408 | 0.6832 |  |
| **Circulatory disease** | **-6.4622** | 3.1481 | ±6.2961 | **-2.053** | **0.0401** | * |
| GMI (%) | +1.5146 | 1.8150 | ±3.6300 | +0.835 | 0.4040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **203**, R² = **0.1385**, Adj R² = **0.0889**, F-statistic = **2.79** (p = **0.0022**), Residual SE = **17.204** on **191** df, AIC = **1742.8**, BIC = **1782.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.4252** | 12.7015 | ±25.4031 | **+4.994** | **5.93e-07** | *** |
| Education: graduate level (vs college) | -4.2124 | 2.8847 | ±5.7694 | -1.460 | 0.1442 |  |
| Education: high school or below (vs college) | -2.3316 | 3.5011 | ±7.0023 | -0.666 | 0.5054 |  |
| Site: UCSD (vs UAB) | +3.6445 | 3.3988 | ±6.7975 | +1.072 | 0.2836 |  |
| Site: UW (vs UAB) | +2.3275 | 3.3009 | ±6.6018 | +0.705 | 0.4807 |  |
| **Age (years)** | **-0.3456** | 0.1253 | ±0.2506 | **-2.758** | **0.0058** | ** |
| BMI (kg/m2) | +0.3221 | 0.1789 | ±0.3579 | +1.800 | 0.0718 | . |
| Hypertension | +1.5316 | 3.1129 | ±6.2257 | +0.492 | 0.6227 |  |
| High cholesterol | +1.0721 | 2.5813 | ±5.1627 | +0.415 | 0.6779 |  |
| Kidney disease | -1.4560 | 4.1379 | ±8.2758 | -0.352 | 0.7249 |  |
| **Circulatory disease** | **-6.4844** | 3.1452 | ±6.2903 | **-2.062** | **0.0392** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0312 | 0.0394 | ±0.0789 | +0.793 | 0.4281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **203**, R² = **0.1355**, Adj R² = **0.0857**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.233** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1687** | 11.2682 | ±22.5363 | **+5.961** | **2.51e-09** | *** |
| Education: graduate level (vs college) | -4.1434 | 2.9772 | ±5.9545 | -1.392 | 0.1640 |  |
| Education: high school or below (vs college) | -2.2563 | 3.5308 | ±7.0617 | -0.639 | 0.5228 |  |
| Site: UCSD (vs UAB) | +3.7160 | 3.3895 | ±6.7789 | +1.096 | 0.2729 |  |
| Site: UW (vs UAB) | +2.3409 | 3.3349 | ±6.6699 | +0.702 | 0.4827 |  |
| **Age (years)** | **-0.3556** | 0.1285 | ±0.2569 | **-2.768** | **0.0056** | ** |
| BMI (kg/m2) | +0.3256 | 0.1793 | ±0.3586 | +1.816 | 0.0694 | . |
| Hypertension | +1.6471 | 3.0911 | ±6.1822 | +0.533 | 0.5941 |  |
| High cholesterol | +1.1169 | 2.5744 | ±5.1487 | +0.434 | 0.6644 |  |
| Kidney disease | -1.5805 | 4.2790 | ±8.5580 | -0.369 | 0.7118 |  |
| **Circulatory disease** | **-6.3799** | 3.1161 | ±6.2322 | **-2.047** | **0.0406** | * |
| Glucose SD, pooled (mg/dL) | +0.0203 | 0.0923 | ±0.1846 | +0.220 | 0.8259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5091** | 11.3261 | ±22.6523 | **+5.960** | **2.52e-09** | *** |
| Education: graduate level (vs college) | -4.2178 | 2.9735 | ±5.9469 | -1.418 | 0.1561 |  |
| Education: high school or below (vs college) | -2.1469 | 3.5458 | ±7.0916 | -0.605 | 0.5449 |  |
| Site: UCSD (vs UAB) | +3.7153 | 3.3925 | ±6.7849 | +1.095 | 0.2734 |  |
| Site: UW (vs UAB) | +2.3081 | 3.3385 | ±6.6771 | +0.691 | 0.4893 |  |
| **Age (years)** | **-0.3518** | 0.1286 | ±0.2572 | **-2.735** | **0.0062** | ** |
| BMI (kg/m2) | +0.3242 | 0.1799 | ±0.3598 | +1.802 | 0.0715 | . |
| Hypertension | +1.6413 | 3.0910 | ±6.1819 | +0.531 | 0.5954 |  |
| High cholesterol | +1.1078 | 2.5780 | ±5.1561 | +0.430 | 0.6674 |  |
| Kidney disease | -1.4391 | 4.2813 | ±8.5626 | -0.336 | 0.7368 |  |
| **Circulatory disease** | **-6.3940** | 3.1190 | ±6.2379 | **-2.050** | **0.0404** | * |
| Avg. daily SD (mg/dL) | +0.0057 | 0.1133 | ±0.2267 | +0.051 | 0.9596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **203**, R² = **0.1353**, Adj R² = **0.0855**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.235** on **191** df, AIC = **1743.6**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0742** | 11.4012 | ±22.8023 | **+5.971** | **2.36e-09** | *** |
| Education: graduate level (vs college) | -4.3187 | 3.0363 | ±6.0726 | -1.422 | 0.1549 |  |
| Education: high school or below (vs college) | -1.9960 | 3.5004 | ±7.0008 | -0.570 | 0.5685 |  |
| Site: UCSD (vs UAB) | +3.7113 | 3.3911 | ±6.7823 | +1.094 | 0.2738 |  |
| Site: UW (vs UAB) | +2.2740 | 3.3337 | ±6.6675 | +0.682 | 0.4952 |  |
| **Age (years)** | **-0.3453** | 0.1343 | ±0.2686 | **-2.571** | **0.0101** | * |
| BMI (kg/m2) | +0.3221 | 0.1800 | ±0.3601 | +1.789 | 0.0736 | . |
| Hypertension | +1.6190 | 3.0900 | ±6.1799 | +0.524 | 0.6003 |  |
| High cholesterol | +1.1089 | 2.5687 | ±5.1374 | +0.432 | 0.6660 |  |
| Kidney disease | -1.2565 | 4.3435 | ±8.6870 | -0.289 | 0.7724 |  |
| **Circulatory disease** | **-6.4225** | 3.1128 | ±6.2257 | **-2.063** | **0.0391** | * |
| CV (%) | -0.0289 | 0.2053 | ±0.4105 | -0.141 | 0.8879 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **203**, R² = **0.1366**, Adj R² = **0.0869**, F-statistic = **2.75** (p = **0.0025**), Residual SE = **17.223** on **191** df, AIC = **1743.3**, BIC = **1783.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.1670** | 13.2307 | ±26.4615 | **+5.379** | **7.49e-08** | *** |
| Education: graduate level (vs college) | -3.9774 | 3.0485 | ±6.0969 | -1.305 | 0.1920 |  |
| Education: high school or below (vs college) | -2.5054 | 3.5131 | ±7.0262 | -0.713 | 0.4758 |  |
| Site: UCSD (vs UAB) | +3.6633 | 3.3821 | ±6.7642 | +1.083 | 0.2787 |  |
| Site: UW (vs UAB) | +2.3443 | 3.3224 | ±6.6449 | +0.706 | 0.4804 |  |
| **Age (years)** | **-0.3709** | 0.1334 | ±0.2668 | **-2.781** | **0.0054** | ** |
| BMI (kg/m2) | +0.3257 | 0.1784 | ±0.3567 | +1.826 | 0.0679 | . |
| Hypertension | +1.7238 | 3.0808 | ±6.1616 | +0.560 | 0.5758 |  |
| High cholesterol | +1.1033 | 2.5736 | ±5.1472 | +0.429 | 0.6681 |  |
| Kidney disease | -1.7339 | 4.2404 | ±8.4808 | -0.409 | 0.6826 |  |
| **Circulatory disease** | **-6.4155** | 3.1214 | ±6.2429 | **-2.055** | **0.0398** | * |
| Mean / SD ratio | -0.5329 | 1.0094 | ±2.0188 | -0.528 | 0.5975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **203**, R² = **0.1355**, Adj R² = **0.0857**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.234** on **191** df, AIC = **1743.6**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.0754** | 13.2760 | ±26.5521 | **+5.203** | **1.96e-07** | *** |
| Education: graduate level (vs college) | -4.1262 | 3.0583 | ±6.1166 | -1.349 | 0.1773 |  |
| Education: high school or below (vs college) | -2.2733 | 3.5298 | ±7.0596 | -0.644 | 0.5196 |  |
| Site: UCSD (vs UAB) | +3.6797 | 3.3837 | ±6.7675 | +1.087 | 0.2768 |  |
| Site: UW (vs UAB) | +2.3020 | 3.3408 | ±6.6817 | +0.689 | 0.4908 |  |
| **Age (years)** | **-0.3592** | 0.1344 | ±0.2687 | **-2.673** | **0.0075** | ** |
| BMI (kg/m2) | +0.3250 | 0.1792 | ±0.3584 | +1.814 | 0.0697 | . |
| Hypertension | +1.6879 | 3.0909 | ±6.1818 | +0.546 | 0.5850 |  |
| High cholesterol | +1.0855 | 2.5873 | ±5.1745 | +0.420 | 0.6748 |  |
| Kidney disease | -1.4895 | 4.2304 | ±8.4608 | -0.352 | 0.7248 |  |
| **Circulatory disease** | **-6.3971** | 3.1221 | ±6.2441 | **-2.049** | **0.0405** | * |
| Avg. daily mean/SD | -0.1843 | 0.8672 | ±1.7344 | -0.212 | 0.8317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **203**, R² = **0.1381**, Adj R² = **0.0885**, F-statistic = **2.78** (p = **0.0022**), Residual SE = **17.207** on **191** df, AIC = **1742.9**, BIC = **1782.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7550** | 11.1191 | ±22.2382 | **+6.363** | **1.97e-10** | *** |
| Education: graduate level (vs college) | -4.4921 | 2.9380 | ±5.8760 | -1.529 | 0.1263 |  |
| Education: high school or below (vs college) | -1.6228 | 3.6273 | ±7.2547 | -0.447 | 0.6546 |  |
| Site: UCSD (vs UAB) | +3.9018 | 3.3816 | ±6.7632 | +1.154 | 0.2486 |  |
| Site: UW (vs UAB) | +2.0805 | 3.3291 | ±6.6582 | +0.625 | 0.5320 |  |
| **Age (years)** | **-0.3421** | 0.1269 | ±0.2539 | **-2.695** | **0.0070** | ** |
| BMI (kg/m2) | +0.3364 | 0.1785 | ±0.3570 | +1.885 | 0.0595 | . |
| Hypertension | +1.5075 | 3.0879 | ±6.1759 | +0.488 | 0.6254 |  |
| High cholesterol | +1.1826 | 2.5716 | ±5.1431 | +0.460 | 0.6456 |  |
| Kidney disease | -1.3288 | 4.2012 | ±8.4025 | -0.316 | 0.7518 |  |
| **Circulatory disease** | **-6.4459** | 3.0940 | ±6.1881 | **-2.083** | **0.0372** | * |
| MAG (mg/dL/h) | -0.0893 | 0.1178 | ±0.2355 | -0.758 | 0.4484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6909** | 11.4365 | ±22.8730 | **+5.919** | **3.24e-09** | *** |
| Education: graduate level (vs college) | -4.2508 | 2.9868 | ±5.9737 | -1.423 | 0.1547 |  |
| Education: high school or below (vs college) | -2.0897 | 3.5515 | ±7.1031 | -0.588 | 0.5563 |  |
| Site: UCSD (vs UAB) | +3.7157 | 3.3899 | ±6.7797 | +1.096 | 0.2730 |  |
| Site: UW (vs UAB) | +2.2987 | 3.3394 | ±6.6787 | +0.688 | 0.4912 |  |
| **Age (years)** | **-0.3502** | 0.1290 | ±0.2580 | **-2.715** | **0.0066** | ** |
| BMI (kg/m2) | +0.3234 | 0.1797 | ±0.3595 | +1.799 | 0.0720 | . |
| Hypertension | +1.6326 | 3.0886 | ±6.1771 | +0.529 | 0.5971 |  |
| High cholesterol | +1.1094 | 2.5852 | ±5.1704 | +0.429 | 0.6678 |  |
| Kidney disease | -1.3791 | 4.2658 | ±8.5316 | -0.323 | 0.7465 |  |
| **Circulatory disease** | **-6.4017** | 3.1167 | ±6.2334 | **-2.054** | **0.0400** | * |
| Avg. daily range (mg/dL) | -0.0005 | 0.0312 | ±0.0624 | -0.017 | 0.9860 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **203**, R² = **0.1392**, Adj R² = **0.0896**, F-statistic = **2.81** (p = **0.0020**), Residual SE = **17.197** on **191** df, AIC = **1742.7**, BIC = **1782.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.6814** | 11.1378 | ±22.2756 | **+5.987** | **2.14e-09** | *** |
| Education: graduate level (vs college) | -3.8812 | 2.9587 | ±5.9173 | -1.312 | 0.1896 |  |
| Education: high school or below (vs college) | -2.2300 | 3.5394 | ±7.0788 | -0.630 | 0.5287 |  |
| Site: UCSD (vs UAB) | +3.6491 | 3.3789 | ±6.7577 | +1.080 | 0.2801 |  |
| Site: UW (vs UAB) | +2.4662 | 3.3209 | ±6.6418 | +0.743 | 0.4577 |  |
| **Age (years)** | **-0.3609** | 0.1254 | ±0.2508 | **-2.878** | **0.0040** | ** |
| BMI (kg/m2) | +0.3278 | 0.1769 | ±0.3539 | +1.853 | 0.0639 | . |
| Hypertension | +1.4426 | 3.1121 | ±6.2243 | +0.464 | 0.6430 |  |
| High cholesterol | +1.1959 | 2.5765 | ±5.1529 | +0.464 | 0.6425 |  |
| Kidney disease | -1.8568 | 4.1926 | ±8.3852 | -0.443 | 0.6579 |  |
| **Circulatory disease** | **-6.5223** | 3.1205 | ±6.2411 | **-2.090** | **0.0366** | * |
| SD of daily means (mg/dL) | +0.1192 | 0.1185 | ±0.2369 | +1.006 | 0.3142 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **203**, R² = **0.1401**, Adj R² = **0.0906**, F-statistic = **2.83** (p = **0.0019**), Residual SE = **17.188** on **191** df, AIC = **1742.5**, BIC = **1782.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7003** | 12.6643 | ±25.3286 | **+5.820** | **5.90e-09** | *** |
| Education: graduate level (vs college) | -3.8422 | 2.9489 | ±5.8977 | -1.303 | 0.1926 |  |
| Education: high school or below (vs college) | -2.4164 | 3.4918 | ±6.9836 | -0.692 | 0.4889 |  |
| Site: UCSD (vs UAB) | +3.7361 | 3.3746 | ±6.7492 | +1.107 | 0.2682 |  |
| Site: UW (vs UAB) | +2.4561 | 3.3305 | ±6.6609 | +0.737 | 0.4608 |  |
| **Age (years)** | **-0.3593** | 0.1243 | ±0.2487 | **-2.890** | **0.0039** | ** |
| BMI (kg/m2) | +0.3299 | 0.1781 | ±0.3562 | +1.852 | 0.0640 | . |
| Hypertension | +1.7168 | 3.0861 | ±6.1722 | +0.556 | 0.5780 |  |
| High cholesterol | +1.0033 | 2.5875 | ±5.1749 | +0.388 | 0.6982 |  |
| Kidney disease | -1.9044 | 4.1679 | ±8.3359 | -0.457 | 0.6477 |  |
| **Circulatory disease** | **-6.5374** | 3.1314 | ±6.2627 | **-2.088** | **0.0368** | * |
| Time in range 70-180, pooled (%) | -0.0693 | 0.0738 | ±0.1476 | -0.939 | 0.3477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **203**, R² = **0.1402**, Adj R² = **0.0907**, F-statistic = **2.83** (p = **0.0019**), Residual SE = **17.186** on **191** df, AIC = **1742.4**, BIC = **1782.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.7442** | 12.5534 | ±25.1067 | **+5.874** | **4.24e-09** | *** |
| Education: graduate level (vs college) | -3.8390 | 2.9492 | ±5.8984 | -1.302 | 0.1930 |  |
| Education: high school or below (vs college) | -2.4573 | 3.4923 | ±6.9846 | -0.704 | 0.4817 |  |
| Site: UCSD (vs UAB) | +3.7512 | 3.3738 | ±6.7476 | +1.112 | 0.2662 |  |
| Site: UW (vs UAB) | +2.4712 | 3.3364 | ±6.6729 | +0.741 | 0.4589 |  |
| **Age (years)** | **-0.3593** | 0.1243 | ±0.2486 | **-2.890** | **0.0039** | ** |
| BMI (kg/m2) | +0.3314 | 0.1784 | ±0.3569 | +1.857 | 0.0633 | . |
| Hypertension | +1.7354 | 3.0853 | ±6.1706 | +0.562 | 0.5738 |  |
| High cholesterol | +0.9972 | 2.5849 | ±5.1698 | +0.386 | 0.6997 |  |
| Kidney disease | -1.9244 | 4.1675 | ±8.3349 | -0.462 | 0.6442 |  |
| **Circulatory disease** | **-6.5499** | 3.1335 | ±6.2670 | **-2.090** | **0.0366** | * |
| Avg. daily time in range 70-180 (%) | -0.0702 | 0.0722 | ±0.1444 | -0.973 | 0.3307 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.1412**, Adj R² = **0.0917**, F-statistic = **2.85** (p = **0.0017**), Residual SE = **17.177** on **191** df, AIC = **1742.2**, BIC = **1782.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.0415** | 11.0255 | ±22.0509 | **+6.081** | **1.20e-09** | *** |
| Education: graduate level (vs college) | -4.0421 | 2.8698 | ±5.7397 | -1.408 | 0.1590 |  |
| Education: high school or below (vs college) | -1.7825 | 3.6388 | ±7.2777 | -0.490 | 0.6242 |  |
| Site: UCSD (vs UAB) | +4.1228 | 3.3749 | ±6.7497 | +1.222 | 0.2219 |  |
| Site: UW (vs UAB) | +2.8425 | 3.3526 | ±6.7052 | +0.848 | 0.3965 |  |
| **Age (years)** | **-0.3541** | 0.1251 | ±0.2502 | **-2.831** | **0.0046** | ** |
| BMI (kg/m2) | +0.3212 | 0.1767 | ±0.3535 | +1.817 | 0.0692 | . |
| Hypertension | +1.4572 | 3.0727 | ±6.1453 | +0.474 | 0.6353 |  |
| High cholesterol | +1.0558 | 2.5580 | ±5.1160 | +0.413 | 0.6798 |  |
| Kidney disease | -1.3338 | 4.2262 | ±8.4525 | -0.316 | 0.7523 |  |
| **Circulatory disease** | **-6.7135** | 3.0802 | ±6.1603 | **-2.180** | **0.0293** | * |
| Time < 54 (%) | +1.8419 | 1.2267 | ±2.4534 | +1.502 | 0.1332 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **203**, R² = **0.1360**, Adj R² = **0.0863**, F-statistic = **2.73** (p = **0.0026**), Residual SE = **17.228** on **191** df, AIC = **1743.4**, BIC = **1783.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5754** | 11.0797 | ±22.1593 | **+6.099** | **1.07e-09** | *** |
| Education: graduate level (vs college) | -4.1422 | 2.8861 | ±5.7722 | -1.435 | 0.1512 |  |
| Education: high school or below (vs college) | -1.9959 | 3.6032 | ±7.2065 | -0.554 | 0.5796 |  |
| Site: UCSD (vs UAB) | +3.8420 | 3.3957 | ±6.7914 | +1.131 | 0.2579 |  |
| Site: UW (vs UAB) | +2.4494 | 3.3526 | ±6.7051 | +0.731 | 0.4650 |  |
| **Age (years)** | **-0.3541** | 0.1263 | ±0.2526 | **-2.804** | **0.0050** | ** |
| BMI (kg/m2) | +0.3238 | 0.1788 | ±0.3576 | +1.811 | 0.0701 | . |
| Hypertension | +1.5993 | 3.0842 | ±6.1685 | +0.519 | 0.6041 |  |
| High cholesterol | +1.1344 | 2.5782 | ±5.1565 | +0.440 | 0.6599 |  |
| Kidney disease | -1.4105 | 4.2266 | ±8.4531 | -0.334 | 0.7386 |  |
| **Circulatory disease** | **-6.5098** | 3.1536 | ±6.3072 | **-2.064** | **0.0390** | * |
| Avg. daily time < 54 (%) | +0.6086 | 2.1114 | ±4.2227 | +0.288 | 0.7732 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **203**, R² = **0.1356**, Adj R² = **0.0858**, F-statistic = **2.72** (p = **0.0027**), Residual SE = **17.233** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6826** | 11.1164 | ±22.2329 | **+6.089** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -4.3722 | 2.9633 | ±5.9266 | -1.475 | 0.1401 |  |
| Education: high school or below (vs college) | -2.0773 | 3.5552 | ±7.1103 | -0.584 | 0.5590 |  |
| Site: UCSD (vs UAB) | +3.6451 | 3.4156 | ±6.8311 | +1.067 | 0.2859 |  |
| Site: UW (vs UAB) | +2.2594 | 3.3236 | ±6.6472 | +0.680 | 0.4966 |  |
| **Age (years)** | **-0.3462** | 0.1262 | ±0.2523 | **-2.745** | **0.0061** | ** |
| BMI (kg/m2) | +0.3227 | 0.1793 | ±0.3587 | +1.799 | 0.0720 | . |
| Hypertension | +1.6213 | 3.0951 | ±6.1902 | +0.524 | 0.6004 |  |
| High cholesterol | +1.1333 | 2.5746 | ±5.1493 | +0.440 | 0.6598 |  |
| Kidney disease | -1.3750 | 4.2282 | ±8.4564 | -0.325 | 0.7450 |  |
| **Circulatory disease** | **-6.3851** | 3.1324 | ±6.2648 | **-2.038** | **0.0415** | * |
| Time 54-69, pooled (%) | -0.1393 | 0.5385 | ±1.0771 | -0.259 | 0.7960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **203**, R² = **0.1363**, Adj R² = **0.0866**, F-statistic = **2.74** (p = **0.0026**), Residual SE = **17.225** on **191** df, AIC = **1743.3**, BIC = **1783.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6097** | 11.1117 | ±22.2235 | **+6.085** | **1.17e-09** | *** |
| Education: graduate level (vs college) | -4.4534 | 2.9619 | ±5.9239 | -1.504 | 0.1327 |  |
| Education: high school or below (vs college) | -2.0356 | 3.5372 | ±7.0745 | -0.575 | 0.5650 |  |
| Site: UCSD (vs UAB) | +3.6034 | 3.4237 | ±6.8473 | +1.053 | 0.2926 |  |
| Site: UW (vs UAB) | +2.2306 | 3.3141 | ±6.6282 | +0.673 | 0.5009 |  |
| **Age (years)** | **-0.3420** | 0.1267 | ±0.2533 | **-2.700** | **0.0069** | ** |
| BMI (kg/m2) | +0.3220 | 0.1795 | ±0.3590 | +1.794 | 0.0728 | . |
| Hypertension | +1.6136 | 3.1026 | ±6.2052 | +0.520 | 0.6030 |  |
| High cholesterol | +1.1436 | 2.5769 | ±5.1538 | +0.444 | 0.6572 |  |
| Kidney disease | -1.3596 | 4.2219 | ±8.4439 | -0.322 | 0.7474 |  |
| **Circulatory disease** | **-6.3785** | 3.1373 | ±6.2746 | **-2.033** | **0.0420** | * |
| Avg. daily time 54-69 (%) | -0.2271 | 0.5265 | ±1.0530 | -0.431 | 0.6662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6177** | 11.1101 | ±22.2202 | **+6.086** | **1.16e-09** | *** |
| Education: graduate level (vs college) | -4.2196 | 2.9360 | ±5.8720 | -1.437 | 0.1507 |  |
| Education: high school or below (vs college) | -2.1053 | 3.5853 | ±7.1707 | -0.587 | 0.5571 |  |
| Site: UCSD (vs UAB) | +3.7301 | 3.4081 | ±6.8163 | +1.094 | 0.2738 |  |
| Site: UW (vs UAB) | +2.3130 | 3.3399 | ±6.6798 | +0.693 | 0.4886 |  |
| **Age (years)** | **-0.3513** | 0.1261 | ±0.2523 | **-2.785** | **0.0054** | ** |
| BMI (kg/m2) | +0.3237 | 0.1789 | ±0.3578 | +1.809 | 0.0704 | . |
| Hypertension | +1.6361 | 3.0874 | ±6.1747 | +0.530 | 0.5961 |  |
| High cholesterol | +1.1035 | 2.5697 | ±5.1395 | +0.429 | 0.6676 |  |
| Kidney disease | -1.3964 | 4.2340 | ±8.4681 | -0.330 | 0.7415 |  |
| **Circulatory disease** | **-6.4072** | 3.1271 | ±6.2543 | **-2.049** | **0.0405** | * |
| Time < 70 (%) | +0.0216 | 0.4453 | ±0.8905 | +0.048 | 0.9614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **203**, R² = **0.1356**, Adj R² = **0.0858**, F-statistic = **2.72** (p = **0.0027**), Residual SE = **17.232** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.6317** | 11.1111 | ±22.2222 | **+6.087** | **1.15e-09** | *** |
| Education: graduate level (vs college) | -4.3619 | 2.9408 | ±5.8815 | -1.483 | 0.1380 |  |
| Education: high school or below (vs college) | -2.0910 | 3.5568 | ±7.1136 | -0.588 | 0.5566 |  |
| Site: UCSD (vs UAB) | +3.6381 | 3.4169 | ±6.8339 | +1.065 | 0.2870 |  |
| Site: UW (vs UAB) | +2.2399 | 3.3249 | ±6.6497 | +0.674 | 0.5005 |  |
| **Age (years)** | **-0.3458** | 0.1269 | ±0.2539 | **-2.724** | **0.0064** | ** |
| BMI (kg/m2) | +0.3228 | 0.1794 | ±0.3588 | +1.799 | 0.0720 | . |
| Hypertension | +1.6317 | 3.0977 | ±6.1953 | +0.527 | 0.5984 |  |
| High cholesterol | +1.1205 | 2.5727 | ±5.1454 | +0.436 | 0.6632 |  |
| Kidney disease | -1.3745 | 4.2267 | ±8.4534 | -0.325 | 0.7450 |  |
| **Circulatory disease** | **-6.3706** | 3.1408 | ±6.2817 | **-2.028** | **0.0425** | * |
| Avg. daily time < 70 (%) | -0.1095 | 0.4427 | ±0.8854 | -0.247 | 0.8047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.1353**, Adj R² = **0.0855**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.235** on **191** df, AIC = **1743.6**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.2618** | 19.6976 | ±39.3952 | **+3.516** | **4.38e-04** | *** |
| Education: graduate level (vs college) | -4.2113 | 2.9018 | ±5.8037 | -1.451 | 0.1467 |  |
| Education: high school or below (vs college) | -2.1535 | 3.5995 | ±7.1991 | -0.598 | 0.5497 |  |
| Site: UCSD (vs UAB) | +3.7196 | 3.3883 | ±6.7765 | +1.098 | 0.2723 |  |
| Site: UW (vs UAB) | +2.3389 | 3.3457 | ±6.6914 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.3503** | 0.1250 | ±0.2500 | **-2.802** | **0.0051** | ** |
| BMI (kg/m2) | +0.3244 | 0.1789 | ±0.3577 | +1.814 | 0.0697 | . |
| Hypertension | +1.6262 | 3.0977 | ±6.1954 | +0.525 | 0.5996 |  |
| High cholesterol | +1.1266 | 2.5805 | ±5.1609 | +0.437 | 0.6624 |  |
| Kidney disease | -1.4281 | 4.2295 | ±8.4591 | -0.338 | 0.7356 |  |
| **Circulatory disease** | **-6.4240** | 3.1455 | ±6.2910 | **-2.042** | **0.0411** | * |
| Time 54-250, pooled (%) | -0.0175 | 0.1680 | ±0.3360 | -0.104 | 0.9168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **203**, R² = **0.1358**, Adj R² = **0.0860**, F-statistic = **2.73** (p = **0.0027**), Residual SE = **17.231** on **191** df, AIC = **1743.5**, BIC = **1783.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.3799** | 21.5038 | ±43.0075 | **+3.366** | **7.63e-04** | *** |
| Education: graduate level (vs college) | -4.1539 | 2.9036 | ±5.8071 | -1.431 | 0.1525 |  |
| Education: high school or below (vs college) | -2.2540 | 3.6030 | ±7.2059 | -0.626 | 0.5316 |  |
| Site: UCSD (vs UAB) | +3.7158 | 3.3930 | ±6.7859 | +1.095 | 0.2735 |  |
| Site: UW (vs UAB) | +2.3924 | 3.3433 | ±6.6866 | +0.716 | 0.4742 |  |
| **Age (years)** | **-0.3502** | 0.1248 | ±0.2497 | **-2.805** | **0.0050** | ** |
| BMI (kg/m2) | +0.3265 | 0.1787 | ±0.3573 | +1.828 | 0.0676 | . |
| Hypertension | +1.6093 | 3.0927 | ±6.1855 | +0.520 | 0.6028 |  |
| High cholesterol | +1.1552 | 2.5801 | ±5.1602 | +0.448 | 0.6543 |  |
| Kidney disease | -1.5015 | 4.2275 | ±8.4550 | -0.355 | 0.7225 |  |
| **Circulatory disease** | **-6.4745** | 3.1515 | ±6.3029 | **-2.054** | **0.0399** | * |
| Avg. daily time 54-250 (%) | -0.0505 | 0.1901 | ±0.3802 | -0.266 | 0.7903 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.1457**, Adj R² = **0.0965**, F-statistic = **2.96** (p = **0.0012**), Residual SE = **17.132** on **191** df, AIC = **1741.1**, BIC = **1780.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8734** | 11.1651 | ±22.3301 | **+5.990** | **2.10e-09** | *** |
| Education: graduate level (vs college) | -3.7694 | 2.9396 | ±5.8792 | -1.282 | 0.1997 |  |
| Education: high school or below (vs college) | -2.3379 | 3.4470 | ±6.8939 | -0.678 | 0.4976 |  |
| Site: UCSD (vs UAB) | +3.6417 | 3.3706 | ±6.7412 | +1.080 | 0.2800 |  |
| Site: UW (vs UAB) | +2.2632 | 3.2944 | ±6.5887 | +0.687 | 0.4921 |  |
| **Age (years)** | **-0.3681** | 0.1245 | ±0.2490 | **-2.957** | **0.0031** | ** |
| BMI (kg/m2) | +0.3292 | 0.1779 | ±0.3558 | +1.850 | 0.0643 | . |
| Hypertension | +1.8836 | 3.0940 | ±6.1880 | +0.609 | 0.5427 |  |
| High cholesterol | +0.7419 | 2.5751 | ±5.1501 | +0.288 | 0.7733 |  |
| Kidney disease | -2.2051 | 4.1118 | ±8.2236 | -0.536 | 0.5918 |  |
| **Circulatory disease** | **-6.4845** | 3.1138 | ±6.2276 | **-2.083** | **0.0373** | * |
| Time 181-250, pooled (%) | +0.1533 | 0.1068 | ±0.2136 | +1.436 | 0.1510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **203**, R² = **0.1442**, Adj R² = **0.0949**, F-statistic = **2.92** (p = **0.0014**), Residual SE = **17.147** on **191** df, AIC = **1741.5**, BIC = **1781.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.6725** | 11.1784 | ±22.3569 | **+5.964** | **2.46e-09** | *** |
| Education: graduate level (vs college) | -3.8210 | 2.9420 | ±5.8841 | -1.299 | 0.1940 |  |
| Education: high school or below (vs college) | -2.3472 | 3.4535 | ±6.9070 | -0.680 | 0.4967 |  |
| Site: UCSD (vs UAB) | +3.7157 | 3.3720 | ±6.7439 | +1.102 | 0.2705 |  |
| Site: UW (vs UAB) | +2.3423 | 3.3078 | ±6.6157 | +0.708 | 0.4789 |  |
| **Age (years)** | **-0.3634** | 0.1244 | ±0.2488 | **-2.921** | **0.0035** | ** |
| BMI (kg/m2) | +0.3300 | 0.1783 | ±0.3565 | +1.851 | 0.0641 | . |
| Hypertension | +1.8894 | 3.0939 | ±6.1877 | +0.611 | 0.5414 |  |
| High cholesterol | +0.7845 | 2.5744 | ±5.1488 | +0.305 | 0.7606 |  |
| Kidney disease | -2.1188 | 4.1242 | ±8.2485 | -0.514 | 0.6074 |  |
| **Circulatory disease** | **-6.4791** | 3.1187 | ±6.2373 | **-2.078** | **0.0378** | * |
| Avg. daily time 181-250 (%) | +0.1374 | 0.1034 | ±0.2068 | +1.329 | 0.1840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **203**, R² = **0.1398**, Adj R² = **0.0903**, F-statistic = **2.82** (p = **0.0019**), Residual SE = **17.190** on **191** df, AIC = **1742.5**, BIC = **1782.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8585** | 11.1293 | ±22.2586 | **+6.007** | **1.88e-09** | *** |
| Education: graduate level (vs college) | -3.9306 | 2.9297 | ±5.8594 | -1.342 | 0.1797 |  |
| Education: high school or below (vs college) | -2.3996 | 3.4848 | ±6.9697 | -0.689 | 0.4911 |  |
| Site: UCSD (vs UAB) | +3.6876 | 3.3808 | ±6.7615 | +1.091 | 0.2754 |  |
| Site: UW (vs UAB) | +2.4097 | 3.3217 | ±6.6433 | +0.725 | 0.4682 |  |
| **Age (years)** | **-0.3567** | 0.1243 | ±0.2486 | **-2.870** | **0.0041** | ** |
| BMI (kg/m2) | +0.3292 | 0.1783 | ±0.3566 | +1.846 | 0.0649 | . |
| Hypertension | +1.7123 | 3.0908 | ±6.1815 | +0.554 | 0.5796 |  |
| High cholesterol | +1.0223 | 2.5848 | ±5.1696 | +0.395 | 0.6925 |  |
| Kidney disease | -1.8723 | 4.1608 | ±8.3215 | -0.450 | 0.6527 |  |
| **Circulatory disease** | **-6.5119** | 3.1360 | ±6.2719 | **-2.077** | **0.0378** | * |
| Time > 180 (%) | +0.0659 | 0.0713 | ±0.1425 | +0.924 | 0.3554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **203**, R² = **0.1406**, Adj R² = **0.0911**, F-statistic = **2.84** (p = **0.0018**), Residual SE = **17.183** on **191** df, AIC = **1742.3**, BIC = **1782.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.7042** | 11.1470 | ±22.2941 | **+5.984** | **2.18e-09** | *** |
| Education: graduate level (vs college) | -3.9094 | 2.9313 | ±5.8627 | -1.334 | 0.1823 |  |
| Education: high school or below (vs college) | -2.4553 | 3.4768 | ±6.9537 | -0.706 | 0.4801 |  |
| Site: UCSD (vs UAB) | +3.7019 | 3.3795 | ±6.7590 | +1.095 | 0.2733 |  |
| Site: UW (vs UAB) | +2.4351 | 3.3249 | ±6.6497 | +0.732 | 0.4639 |  |
| **Age (years)** | **-0.3563** | 0.1242 | ±0.2484 | **-2.868** | **0.0041** | ** |
| BMI (kg/m2) | +0.3310 | 0.1785 | ±0.3569 | +1.855 | 0.0636 | . |
| Hypertension | +1.7346 | 3.0915 | ±6.1830 | +0.561 | 0.5747 |  |
| High cholesterol | +1.0031 | 2.5823 | ±5.1647 | +0.388 | 0.6977 |  |
| Kidney disease | -1.9221 | 4.1547 | ±8.3094 | -0.463 | 0.6436 |  |
| **Circulatory disease** | **-6.5330** | 3.1382 | ±6.2763 | **-2.082** | **0.0374** | * |
| Avg. daily time > 180 (%) | +0.0716 | 0.0701 | ±0.1403 | +1.021 | 0.3072 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **203**, R² = **0.1376**, Adj R² = **0.0880**, F-statistic = **2.77** (p = **0.0023**), Residual SE = **17.212** on **191** df, AIC = **1743.0**, BIC = **1782.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1519** | 11.1491 | ±22.2983 | **+6.023** | **1.71e-09** | *** |
| Education: graduate level (vs college) | -4.0704 | 2.9136 | ±5.8273 | -1.397 | 0.1624 |  |
| Education: high school or below (vs college) | -2.2180 | 3.5108 | ±7.0217 | -0.632 | 0.5276 |  |
| Site: UCSD (vs UAB) | +3.6867 | 3.3873 | ±6.7746 | +1.088 | 0.2764 |  |
| Site: UW (vs UAB) | +2.3873 | 3.3197 | ±6.6395 | +0.719 | 0.4721 |  |
| **Age (years)** | **-0.3498** | 0.1247 | ±0.2493 | **-2.806** | **0.0050** | ** |
| BMI (kg/m2) | +0.3245 | 0.1785 | ±0.3569 | +1.818 | 0.0691 | . |
| Hypertension | +1.5665 | 3.1018 | ±6.2037 | +0.505 | 0.6135 |  |
| High cholesterol | +1.0220 | 2.5807 | ±5.1614 | +0.396 | 0.6921 |  |
| Kidney disease | -1.5703 | 4.1710 | ±8.3420 | -0.376 | 0.7066 |  |
| **Circulatory disease** | **-6.5490** | 3.1402 | ±6.2804 | **-2.086** | **0.0370** | * |
| Nocturnal time > 180 (%) | +0.0472 | 0.0656 | ±0.1312 | +0.720 | 0.4716 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.1381**, Adj R² = **0.0884**, F-statistic = **2.78** (p = **0.0022**), Residual SE = **17.208** on **191** df, AIC = **1742.9**, BIC = **1782.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1631** | 11.1244 | ±22.2488 | **+6.037** | **1.57e-09** | *** |
| Education: graduate level (vs college) | -3.9317 | 2.9628 | ±5.9256 | -1.327 | 0.1845 |  |
| Education: high school or below (vs college) | -2.2860 | 3.5171 | ±7.0342 | -0.650 | 0.5157 |  |
| Site: UCSD (vs UAB) | +3.6441 | 3.3858 | ±6.7717 | +1.076 | 0.2818 |  |
| Site: UW (vs UAB) | +2.0716 | 3.3162 | ±6.6325 | +0.625 | 0.5322 |  |
| **Age (years)** | **-0.3673** | 0.1267 | ±0.2533 | **-2.900** | **0.0037** | ** |
| BMI (kg/m2) | +0.3381 | 0.1797 | ±0.3595 | +1.881 | 0.0599 | . |
| Hypertension | +1.6858 | 3.0939 | ±6.1879 | +0.545 | 0.5858 |  |
| High cholesterol | +1.0372 | 2.5789 | ±5.1579 | +0.402 | 0.6875 |  |
| Kidney disease | -1.8838 | 4.2710 | ±8.5420 | -0.441 | 0.6592 |  |
| **Circulatory disease** | **-6.3869** | 3.1290 | ±6.2581 | **-2.041** | **0.0412** | * |
| Any reading > 250 during wear (0/1) | +2.0349 | 2.6747 | ±5.3495 | +0.761 | 0.4468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **203**, R² = **0.1352**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0028**), Residual SE = **17.236** on **191** df, AIC = **1743.6**, BIC = **1783.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.5940** | 11.1018 | ±22.2036 | **+6.089** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -4.2328 | 2.9006 | ±5.8012 | -1.459 | 0.1445 |  |
| Education: high school or below (vs college) | -2.1214 | 3.6049 | ±7.2099 | -0.588 | 0.5562 |  |
| Site: UCSD (vs UAB) | +3.7149 | 3.3920 | ±6.7839 | +1.095 | 0.2734 |  |
| Site: UW (vs UAB) | +2.3111 | 3.3428 | ±6.6856 | +0.691 | 0.4893 |  |
| **Age (years)** | **-0.3505** | 0.1251 | ±0.2503 | **-2.801** | **0.0051** | ** |
| BMI (kg/m2) | +0.3239 | 0.1789 | ±0.3578 | +1.810 | 0.0702 | . |
| Hypertension | +1.6334 | 3.0994 | ±6.1989 | +0.527 | 0.5982 |  |
| High cholesterol | +1.1142 | 2.5813 | ±5.1626 | +0.432 | 0.6660 |  |
| Kidney disease | -1.4053 | 4.2321 | ±8.4642 | -0.332 | 0.7399 |  |
| **Circulatory disease** | **-6.4075** | 3.1426 | ±6.2853 | **-2.039** | **0.0415** | * |
| Time > 250 (%) | +0.0056 | 0.1658 | ±0.3317 | +0.034 | 0.9729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 203)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **203**, R² = **0.1357**, Adj R² = **0.0859**, F-statistic = **2.73** (p = **0.0027**), Residual SE = **17.232** on **191** df, AIC = **1743.5**, BIC = **1783.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.3602** | 11.0966 | ±22.1931 | **+6.070** | **1.28e-09** | *** |
| Education: graduate level (vs college) | -4.1701 | 2.9012 | ±5.8024 | -1.437 | 0.1506 |  |
| Education: high school or below (vs college) | -2.2474 | 3.6107 | ±7.2214 | -0.622 | 0.5337 |  |
| Site: UCSD (vs UAB) | +3.7061 | 3.3985 | ±6.7971 | +1.091 | 0.2755 |  |
| Site: UW (vs UAB) | +2.3722 | 3.3397 | ±6.6794 | +0.710 | 0.4775 |  |
| **Age (years)** | **-0.3500** | 0.1249 | ±0.2498 | **-2.802** | **0.0051** | ** |
| BMI (kg/m2) | +0.3262 | 0.1786 | ±0.3573 | +1.826 | 0.0678 | . |
| Hypertension | +1.6146 | 3.0936 | ±6.1871 | +0.522 | 0.6017 |  |
| High cholesterol | +1.1486 | 2.5803 | ±5.1606 | +0.445 | 0.6562 |  |
| Kidney disease | -1.4897 | 4.2277 | ±8.4554 | -0.352 | 0.7246 |  |
| **Circulatory disease** | **-6.4591** | 3.1518 | ±6.3036 | **-2.049** | **0.0404** | * |
| Avg. daily time > 250 (%) | +0.0456 | 0.1926 | ±0.3852 | +0.237 | 0.8130 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 150 single-predictor tests; 13 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 201): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.106 vs 0.101 for covariates alone, gain +0.005; -409 per SD, p = 0.094). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 201): best single predictor out of sample is **HbA1c** (CV R² 0.124 vs 0.114 for covariates alone, gain +0.010; +1.77 per SD, p = 0.191). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 203): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.070 vs 0.074 for covariates alone, gain -0.004; +0.204 per SD, p = 0.722). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Total sleep time per night (min)** (n = 205): best single predictor out of sample is **HbA1c** (CV R² -0.042 vs -0.080 for covariates alone, gain +0.038; -14.9 per SD, p = 6.0e-04). Raw p < 0.05 (FDR not applicable here): HbA1c (p = 6.0e-04), %>250 (daily avg) (p = 0.006), %54-250 (daily avg) (p = 0.007), MAG (p = 0.008), %>250 (pooled) (p = 0.009).
- **Garmin stress score, mean (0-100)** (n = 203): best single predictor out of sample is **%181-250 (pooled)** (CV R² -0.034 vs -0.036 for covariates alone, gain +0.002; +1.9 per SD, p = 0.151). No glycaemic measure is associated with this outcome (all p > 0.05).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.038, via HbA1c); Brisk-cadence minutes per day (>= 100 steps/min) (+0.010, via HbA1c); Steps per wear-day (+0.005, via %<70 (daily avg)); Garmin stress score, mean (0-100) (+0.002, via %181-250 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band > 250 (0 FDR-significant / 3 raw-significant of 15); CGM level (0 FDR-significant / 2 raw-significant of 15); Range 70-180 (0 FDR-significant / 2 raw-significant of 10).
Level metrics: 0 FDR-significant (2 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
