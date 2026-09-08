# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 178; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **178**, R² = **0.1606**, Adj R² = **0.1104**, F-statistic = **3.20** (p = **8.81e-04**), Residual SE = **4727.096** on **167** df, AIC = **3527.9**, BIC = **3562.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19149.5784** | 3837.4555 | ±7674.9111 | **+4.990** | **6.03e-07** | *** |
| **Education: graduate level (vs college)** | **-2405.1759** | 797.8611 | ±1595.7223 | **-3.015** | **0.0026** | ** |
| Education: high school or below (vs college) | -577.5979 | 1277.7398 | ±2555.4795 | -0.452 | 0.6512 |  |
| Site: UCSD (vs UAB) | +616.3652 | 978.2886 | ±1956.5772 | +0.630 | 0.5287 |  |
| Site: UW (vs UAB) | +975.2728 | 994.3411 | ±1988.6821 | +0.981 | 0.3267 |  |
| **Age (years)** | **-151.5931** | 48.6109 | ±97.2218 | **-3.118** | **0.0018** | ** |
| BMI (kg/m2) | +24.4758 | 64.6193 | ±129.2386 | +0.379 | 0.7049 |  |
| Hypertension | +899.1291 | 838.2152 | ±1676.4304 | +1.073 | 0.2834 |  |
| High cholesterol | -268.9596 | 763.5564 | ±1527.1129 | -0.352 | 0.7247 |  |
| Kidney disease | +229.7934 | 1329.2332 | ±2658.4664 | +0.173 | 0.8627 |  |
| Circulatory disease | -1285.2118 | 899.5281 | ±1799.0561 | -1.429 | 0.1531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **178**, R² = **0.1613**, Adj R² = **0.1058**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.312** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17713.3614** | 5020.3351 | ±10040.6703 | **+3.528** | **4.18e-04** | *** |
| **Education: graduate level (vs college)** | **-2392.6068** | 809.0551 | ±1618.1102 | **-2.957** | **0.0031** | ** |
| Education: high school or below (vs college) | -593.4636 | 1280.1873 | ±2560.3745 | -0.464 | 0.6430 |  |
| Site: UCSD (vs UAB) | +617.0316 | 979.9453 | ±1959.8906 | +0.630 | 0.5289 |  |
| Site: UW (vs UAB) | +981.0610 | 997.4329 | ±1994.8657 | +0.984 | 0.3253 |  |
| **Age (years)** | **-151.7249** | 48.8125 | ±97.6249 | **-3.108** | **0.0019** | ** |
| BMI (kg/m2) | +20.8062 | 64.6936 | ±129.3873 | +0.322 | 0.7477 |  |
| Hypertension | +872.6109 | 852.2424 | ±1704.4848 | +1.024 | 0.3059 |  |
| High cholesterol | -303.4039 | 751.8787 | ±1503.7575 | -0.404 | 0.6866 |  |
| Kidney disease | +285.7445 | 1366.3393 | ±2732.6786 | +0.209 | 0.8343 |  |
| Circulatory disease | -1334.8402 | 903.3490 | ±1806.6981 | -1.478 | 0.1395 |  |
| HbA1c (%) | +267.8141 | 631.3275 | ±1262.6549 | +0.424 | 0.6714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **178**, R² = **0.1650**, Adj R² = **0.1097**, F-statistic = **2.98** (p = **0.0012**), Residual SE = **4728.892** on **166** df, AIC = **3529.0**, BIC = **3567.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16026.1227** | 5210.9305 | ±10421.8610 | **+3.075** | **0.0021** | ** |
| **Education: graduate level (vs college)** | **-2389.0896** | 805.7743 | ±1611.5485 | **-2.965** | **0.0030** | ** |
| Education: high school or below (vs college) | -505.2159 | 1284.9296 | ±2569.8593 | -0.393 | 0.6942 |  |
| Site: UCSD (vs UAB) | +580.0215 | 988.0389 | ±1976.0778 | +0.587 | 0.5572 |  |
| Site: UW (vs UAB) | +964.7312 | 996.7543 | ±1993.5085 | +0.968 | 0.3331 |  |
| **Age (years)** | **-151.2298** | 48.9617 | ±97.9233 | **-3.089** | **0.0020** | ** |
| BMI (kg/m2) | +20.9364 | 65.3928 | ±130.7856 | +0.320 | 0.7488 |  |
| Hypertension | +857.8647 | 839.9703 | ±1679.9405 | +1.021 | 0.3071 |  |
| High cholesterol | -257.8261 | 773.9917 | ±1547.9834 | -0.333 | 0.7390 |  |
| Kidney disease | +118.2300 | 1339.9149 | ±2679.8298 | +0.088 | 0.9297 |  |
| Circulatory disease | -1359.7530 | 908.2412 | ±1816.4824 | -1.497 | 0.1344 |  |
| Mean glucose (mg/dL) | +25.7424 | 29.8352 | ±59.6705 | +0.863 | 0.3882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **178**, R² = **0.1650**, Adj R² = **0.1097**, F-statistic = **2.98** (p = **0.0012**), Residual SE = **4728.892** on **166** df, AIC = **3529.0**, BIC = **3567.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +12463.9374 | 8542.0985 | ±17084.1970 | +1.459 | 0.1445 |  |
| **Education: graduate level (vs college)** | **-2389.0896** | 805.7743 | ±1611.5485 | **-2.965** | **0.0030** | ** |
| Education: high school or below (vs college) | -505.2159 | 1284.9296 | ±2569.8593 | -0.393 | 0.6942 |  |
| Site: UCSD (vs UAB) | +580.0215 | 988.0389 | ±1976.0778 | +0.587 | 0.5572 |  |
| Site: UW (vs UAB) | +964.7312 | 996.7543 | ±1993.5085 | +0.968 | 0.3331 |  |
| **Age (years)** | **-151.2298** | 48.9617 | ±97.9233 | **-3.089** | **0.0020** | ** |
| BMI (kg/m2) | +20.9364 | 65.3928 | ±130.7856 | +0.320 | 0.7488 |  |
| Hypertension | +857.8647 | 839.9703 | ±1679.9405 | +1.021 | 0.3071 |  |
| High cholesterol | -257.8261 | 773.9917 | ±1547.9834 | -0.333 | 0.7390 |  |
| Kidney disease | +118.2300 | 1339.9149 | ±2679.8298 | +0.088 | 0.9297 |  |
| Circulatory disease | -1359.7530 | 908.2412 | ±1816.4824 | -1.497 | 0.1344 |  |
| GMI (%) | +1076.1889 | 1247.2929 | ±2494.5858 | +0.863 | 0.3882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **178**, R² = **0.1750**, Adj R² = **0.1204**, F-statistic = **3.20** (p = **5.69e-04**), Residual SE = **4700.409** on **166** df, AIC = **3526.8**, BIC = **3565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13961.9304** | 4937.6165 | ±9875.2329 | **+2.828** | **0.0047** | ** |
| **Education: graduate level (vs college)** | **-2412.9715** | 800.0017 | ±1600.0034 | **-3.016** | **0.0026** | ** |
| Education: high school or below (vs college) | -502.4193 | 1259.1623 | ±2518.3246 | -0.399 | 0.6899 |  |
| Site: UCSD (vs UAB) | +519.1473 | 984.1564 | ±1968.3127 | +0.528 | 0.5978 |  |
| Site: UW (vs UAB) | +928.2613 | 981.5185 | ±1963.0371 | +0.946 | 0.3443 |  |
| **Age (years)** | **-147.2569** | 48.7380 | ±97.4760 | **-3.021** | **0.0025** | ** |
| BMI (kg/m2) | +17.2820 | 64.8134 | ±129.6268 | +0.267 | 0.7897 |  |
| Hypertension | +827.5272 | 827.6829 | ±1655.3657 | +1.000 | 0.3174 |  |
| High cholesterol | -282.1590 | 767.9040 | ±1535.8081 | -0.367 | 0.7133 |  |
| Kidney disease | +213.1038 | 1297.0208 | ±2594.0417 | +0.164 | 0.8695 |  |
| Circulatory disease | -1472.4765 | 895.0329 | ±1790.0658 | -1.645 | 0.0999 | . |
| Nocturnal mean 00-06h (mg/dL) | +41.8241 | 24.5246 | ±49.0492 | +1.705 | 0.0881 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4740.081** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18696.1611** | 4236.2260 | ±8472.4520 | **+4.413** | **1.02e-05** | *** |
| **Education: graduate level (vs college)** | **-2419.3664** | 795.5618 | ±1591.1236 | **-3.041** | **0.0024** | ** |
| Education: high school or below (vs college) | -632.5813 | 1298.7389 | ±2597.4779 | -0.487 | 0.6262 |  |
| Site: UCSD (vs UAB) | +628.9506 | 984.4360 | ±1968.8721 | +0.639 | 0.5229 |  |
| Site: UW (vs UAB) | +1011.7674 | 1020.0129 | ±2040.0258 | +0.992 | 0.3212 |  |
| **Age (years)** | **-152.1765** | 48.8413 | ±97.6826 | **-3.116** | **0.0018** | ** |
| BMI (kg/m2) | +24.6807 | 64.8791 | ±129.7582 | +0.380 | 0.7036 |  |
| Hypertension | +857.0480 | 844.7100 | ±1689.4201 | +1.015 | 0.3103 |  |
| High cholesterol | -256.2115 | 769.5576 | ±1539.1152 | -0.333 | 0.7392 |  |
| Kidney disease | +176.5226 | 1349.6066 | ±2699.2132 | +0.131 | 0.8959 |  |
| Circulatory disease | -1310.6130 | 896.4448 | ±1792.8895 | -1.462 | 0.1437 |  |
| Glucose SD, pooled (mg/dL) | +23.4949 | 75.0619 | ±150.1238 | +0.313 | 0.7543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.933** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18703.1846** | 4155.8109 | ±8311.6217 | **+4.500** | **6.78e-06** | *** |
| **Education: graduate level (vs college)** | **-2419.7094** | 794.2264 | ±1588.4528 | **-3.047** | **0.0023** | ** |
| Education: high school or below (vs college) | -621.5559 | 1295.4885 | ±2590.9771 | -0.480 | 0.6314 |  |
| Site: UCSD (vs UAB) | +616.2010 | 983.6210 | ±1967.2420 | +0.626 | 0.5310 |  |
| Site: UW (vs UAB) | +999.8289 | 1012.1002 | ±2024.2003 | +0.988 | 0.3232 |  |
| **Age (years)** | **-152.2608** | 48.9731 | ±97.9462 | **-3.109** | **0.0019** | ** |
| BMI (kg/m2) | +24.9098 | 64.8949 | ±129.7897 | +0.384 | 0.7011 |  |
| Hypertension | +845.7544 | 840.0251 | ±1680.0503 | +1.007 | 0.3140 |  |
| High cholesterol | -252.5667 | 770.8291 | ±1541.6583 | -0.328 | 0.7432 |  |
| Kidney disease | +188.3610 | 1337.9194 | ±2675.8388 | +0.141 | 0.8880 |  |
| Circulatory disease | -1305.1388 | 895.9222 | ±1791.8443 | -1.457 | 0.1452 |  |
| Avg. daily SD (mg/dL) | +25.4350 | 76.9779 | ±153.9558 | +0.330 | 0.7411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **178**, R² = **0.1609**, Adj R² = **0.1053**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.613** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19565.6229** | 4485.9303 | ±8971.8606 | **+4.362** | **1.29e-05** | *** |
| **Education: graduate level (vs college)** | **-2391.5060** | 792.3217 | ±1584.6433 | **-3.018** | **0.0025** | ** |
| Education: high school or below (vs college) | -516.6836 | 1349.8512 | ±2699.7024 | -0.383 | 0.7019 |  |
| Site: UCSD (vs UAB) | +600.1978 | 989.0444 | ±1978.0888 | +0.607 | 0.5440 |  |
| Site: UW (vs UAB) | +941.1995 | 1039.9829 | ±2079.9657 | +0.905 | 0.3655 |  |
| **Age (years)** | **-151.0033** | 48.8983 | ±97.7967 | **-3.088** | **0.0020** | ** |
| BMI (kg/m2) | +23.8026 | 66.6201 | ±133.2403 | +0.357 | 0.7209 |  |
| Hypertension | +931.2217 | 846.0240 | ±1692.0480 | +1.101 | 0.2710 |  |
| High cholesterol | -278.3968 | 763.8414 | ±1527.6828 | -0.364 | 0.7155 |  |
| Kidney disease | +261.9820 | 1331.5300 | ±2663.0599 | +0.197 | 0.8440 |  |
| Circulatory disease | -1274.9849 | 902.3257 | ±1804.6513 | -1.413 | 0.1577 |  |
| CV (%) | -26.2110 | 106.1421 | ±212.2842 | -0.247 | 0.8050 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **178**, R² = **0.1608**, Adj R² = **0.1051**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.932** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19494.6448** | 4027.0838 | ±8054.1677 | **+4.841** | **1.29e-06** | *** |
| **Education: graduate level (vs college)** | **-2412.4168** | 793.3928 | ±1586.7856 | **-3.041** | **0.0024** | ** |
| Education: high school or below (vs college) | -617.0220 | 1326.4930 | ±2652.9861 | -0.465 | 0.6418 |  |
| Site: UCSD (vs UAB) | +624.7704 | 987.7162 | ±1975.4324 | +0.633 | 0.5270 |  |
| Site: UW (vs UAB) | +997.2314 | 1035.4481 | ±2070.8962 | +0.963 | 0.3355 |  |
| **Age (years)** | **-152.0594** | 48.8012 | ±97.6024 | **-3.116** | **0.0018** | ** |
| BMI (kg/m2) | +24.5958 | 65.0049 | ±130.0097 | +0.378 | 0.7052 |  |
| Hypertension | +874.6127 | 836.5225 | ±1673.0449 | +1.046 | 0.2958 |  |
| High cholesterol | -265.5494 | 765.9498 | ±1531.8997 | -0.347 | 0.7288 |  |
| Kidney disease | +207.3859 | 1332.8824 | ±2665.7648 | +0.156 | 0.8764 |  |
| Circulatory disease | -1289.3262 | 898.3926 | ±1796.7852 | -1.435 | 0.1512 |  |
| Mean / SD ratio | -50.2076 | 262.1276 | ±524.2552 | -0.192 | 0.8481 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1616**, Adj R² = **0.1061**, F-statistic = **2.91** (p = **0.0016**), Residual SE = **4738.449** on **166** df, AIC = **3529.7**, BIC = **3567.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20015.0916** | 4005.8768 | ±8011.7537 | **+4.996** | **5.84e-07** | *** |
| **Education: graduate level (vs college)** | **-2419.7053** | 793.4337 | ±1586.8673 | **-3.050** | **0.0023** | ** |
| Education: high school or below (vs college) | -657.0748 | 1314.8143 | ±2629.6286 | -0.500 | 0.6173 |  |
| Site: UCSD (vs UAB) | +610.8266 | 980.9443 | ±1961.8885 | +0.623 | 0.5335 |  |
| Site: UW (vs UAB) | +1016.1299 | 1020.0291 | ±2040.0582 | +0.996 | 0.3192 |  |
| **Age (years)** | **-153.1541** | 48.8418 | ±97.6835 | **-3.136** | **0.0017** | ** |
| BMI (kg/m2) | +24.8951 | 64.6214 | ±129.2429 | +0.385 | 0.7001 |  |
| Hypertension | +818.4550 | 827.6036 | ±1655.2073 | +0.989 | 0.3227 |  |
| High cholesterol | -263.0757 | 766.5792 | ±1533.1585 | -0.343 | 0.7315 |  |
| Kidney disease | +188.7485 | 1332.6887 | ±2665.3775 | +0.142 | 0.8874 |  |
| Circulatory disease | -1278.9587 | 899.3863 | ±1798.7727 | -1.422 | 0.1550 |  |
| Avg. daily mean/SD | -105.7075 | 199.1247 | ±398.2494 | -0.531 | 0.5955 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **178**, R² = **0.1663**, Adj R² = **0.1110**, F-statistic = **3.01** (p = **0.0011**), Residual SE = **4725.322** on **166** df, AIC = **3528.7**, BIC = **3566.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17236.1774** | 4390.8386 | ±8781.6773 | **+3.925** | **8.66e-05** | *** |
| **Education: graduate level (vs college)** | **-2426.2631** | 793.6668 | ±1587.3337 | **-3.057** | **0.0022** | ** |
| Education: high school or below (vs college) | -660.8586 | 1281.8812 | ±2563.7624 | -0.516 | 0.6062 |  |
| Site: UCSD (vs UAB) | +580.9377 | 983.7802 | ±1967.5605 | +0.591 | 0.5548 |  |
| Site: UW (vs UAB) | +1014.8974 | 996.4034 | ±1992.8067 | +1.019 | 0.3084 |  |
| **Age (years)** | **-151.6554** | 48.2783 | ±96.5566 | **-3.141** | **0.0017** | ** |
| BMI (kg/m2) | +21.1104 | 66.5114 | ±133.0228 | +0.317 | 0.7509 |  |
| Hypertension | +865.5028 | 828.3125 | ±1656.6250 | +1.045 | 0.2961 |  |
| High cholesterol | -304.6983 | 775.2724 | ±1550.5449 | -0.393 | 0.6943 |  |
| Kidney disease | +242.7381 | 1338.2147 | ±2676.4295 | +0.181 | 0.8561 |  |
| Circulatory disease | -1281.0712 | 901.1194 | ±1802.2389 | -1.422 | 0.1551 |  |
| MAG (mg/dL/h) | +57.2671 | 50.4798 | ±100.9597 | +1.134 | 0.2566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **178**, R² = **0.1609**, Adj R² = **0.1053**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.600** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18733.6082** | 4319.4615 | ±8638.9231 | **+4.337** | **1.44e-05** | *** |
| **Education: graduate level (vs college)** | **-2411.3539** | 795.0274 | ±1590.0549 | **-3.033** | **0.0024** | ** |
| Education: high school or below (vs college) | -605.9445 | 1301.3671 | ±2602.7341 | -0.466 | 0.6415 |  |
| Site: UCSD (vs UAB) | +622.9549 | 986.3909 | ±1972.7818 | +0.632 | 0.5277 |  |
| Site: UW (vs UAB) | +993.6306 | 1014.6396 | ±2029.2792 | +0.979 | 0.3274 |  |
| **Age (years)** | **-152.1176** | 49.2147 | ±98.4295 | **-3.091** | **0.0020** | ** |
| BMI (kg/m2) | +25.3333 | 65.6904 | ±131.3809 | +0.386 | 0.6998 |  |
| Hypertension | +872.8862 | 839.6415 | ±1679.2830 | +1.040 | 0.2985 |  |
| High cholesterol | -261.7282 | 771.8471 | ±1543.6943 | -0.339 | 0.7345 |  |
| Kidney disease | +209.3650 | 1324.7246 | ±2649.4492 | +0.158 | 0.8744 |  |
| Circulatory disease | -1295.9740 | 898.4080 | ±1796.8159 | -1.443 | 0.1492 |  |
| Avg. daily range (mg/dL) | +4.5084 | 19.4643 | ±38.9286 | +0.232 | 0.8168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **178**, R² = **0.1609**, Adj R² = **0.1053**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.630** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19323.7622** | 4061.0322 | ±8122.0643 | **+4.758** | **1.95e-06** | *** |
| **Education: graduate level (vs college)** | **-2398.4894** | 807.4603 | ±1614.9205 | **-2.970** | **0.0030** | ** |
| Education: high school or below (vs college) | -524.0588 | 1277.1820 | ±2554.3640 | -0.410 | 0.6816 |  |
| Site: UCSD (vs UAB) | +585.9635 | 945.9885 | ±1891.9769 | +0.619 | 0.5356 |  |
| Site: UW (vs UAB) | +937.5211 | 974.0746 | ±1948.1491 | +0.962 | 0.3358 |  |
| **Age (years)** | **-150.9970** | 48.5180 | ±97.0360 | **-3.112** | **0.0019** | ** |
| BMI (kg/m2) | +24.6740 | 65.3262 | ±130.6524 | +0.378 | 0.7057 |  |
| Hypertension | +891.2842 | 839.5942 | ±1679.1884 | +1.062 | 0.2884 |  |
| High cholesterol | -264.7969 | 764.6391 | ±1529.2781 | -0.346 | 0.7291 |  |
| Kidney disease | +277.0599 | 1448.7383 | ±2897.4765 | +0.191 | 0.8483 |  |
| Circulatory disease | -1248.4353 | 929.1795 | ±1858.3589 | -1.344 | 0.1791 |  |
| SD of daily means (mg/dL) | -32.3132 | 163.6310 | ±327.2620 | -0.197 | 0.8435 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **178**, R² = **0.1614**, Adj R² = **0.1058**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.227** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +16195.9622 | 9224.1234 | ±18448.2469 | +1.756 | 0.0791 | . |
| **Education: graduate level (vs college)** | **-2380.2750** | 813.7383 | ±1627.4766 | **-2.925** | **0.0034** | ** |
| Education: high school or below (vs college) | -551.6219 | 1285.0332 | ±2570.0664 | -0.429 | 0.6677 |  |
| Site: UCSD (vs UAB) | +603.4786 | 977.6018 | ±1955.2037 | +0.617 | 0.5370 |  |
| Site: UW (vs UAB) | +960.0792 | 1009.0997 | ±2018.1994 | +0.951 | 0.3414 |  |
| **Age (years)** | **-150.0843** | 48.8069 | ±97.6137 | **-3.075** | **0.0021** | ** |
| BMI (kg/m2) | +25.5522 | 65.3762 | ±130.7523 | +0.391 | 0.6959 |  |
| Hypertension | +912.5736 | 843.4410 | ±1686.8820 | +1.082 | 0.2793 |  |
| High cholesterol | -288.4023 | 766.0345 | ±1532.0691 | -0.376 | 0.7066 |  |
| Kidney disease | +306.2584 | 1398.6704 | ±2797.3407 | +0.219 | 0.8267 |  |
| Circulatory disease | -1245.7599 | 915.6430 | ±1831.2861 | -1.361 | 0.1737 |  |
| Time in range 70-180, pooled (%) | +29.2979 | 82.1818 | ±164.3635 | +0.357 | 0.7215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4740.033** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +16782.9742 | 9665.3629 | ±19330.7257 | +1.736 | 0.0825 | . |
| **Education: graduate level (vs college)** | **-2387.3699** | 814.1489 | ±1628.2977 | **-2.932** | **0.0034** | ** |
| Education: high school or below (vs college) | -561.9855 | 1284.1380 | ±2568.2759 | -0.438 | 0.6616 |  |
| Site: UCSD (vs UAB) | +606.5810 | 978.1152 | ±1956.2304 | +0.620 | 0.5352 |  |
| Site: UW (vs UAB) | +967.8660 | 1008.8301 | ±2017.6602 | +0.959 | 0.3374 |  |
| **Age (years)** | **-150.3338** | 48.8491 | ±97.6983 | **-3.078** | **0.0021** | ** |
| BMI (kg/m2) | +25.1538 | 65.2954 | ±130.5908 | +0.385 | 0.7001 |  |
| Hypertension | +913.2698 | 843.0741 | ±1686.1483 | +1.083 | 0.2787 |  |
| High cholesterol | -284.9248 | 766.7357 | ±1533.4713 | -0.372 | 0.7102 |  |
| Kidney disease | +291.6162 | 1402.5633 | ±2805.1266 | +0.208 | 0.8353 |  |
| Circulatory disease | -1252.9958 | 917.5154 | ±1835.0309 | -1.366 | 0.1721 |  |
| Avg. daily time in range 70-180 (%) | +23.4492 | 86.8830 | ±173.7659 | +0.270 | 0.7872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **178**, R² = **0.1678**, Adj R² = **0.1126**, F-statistic = **3.04** (p = **9.89e-04**), Residual SE = **4721.061** on **166** df, AIC = **3528.4**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18863.9488** | 3842.0389 | ±7684.0777 | **+4.910** | **9.11e-07** | *** |
| **Education: graduate level (vs college)** | **-2290.6821** | 799.7933 | ±1599.5866 | **-2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | -384.9944 | 1303.4872 | ±2606.9745 | -0.295 | 0.7677 |  |
| Site: UCSD (vs UAB) | +557.8203 | 976.9686 | ±1953.9372 | +0.571 | 0.5680 |  |
| Site: UW (vs UAB) | +941.3417 | 989.8756 | ±1979.7512 | +0.951 | 0.3416 |  |
| **Age (years)** | **-144.1000** | 48.7583 | ±97.5165 | **-2.955** | **0.0031** | ** |
| BMI (kg/m2) | +22.5309 | 65.3803 | ±130.7607 | +0.345 | 0.7304 |  |
| Hypertension | +890.6150 | 837.1433 | ±1674.2866 | +1.064 | 0.2874 |  |
| High cholesterol | -202.9383 | 765.4867 | ±1530.9735 | -0.265 | 0.7909 |  |
| Kidney disease | +160.7665 | 1329.6462 | ±2659.2923 | +0.121 | 0.9038 |  |
| Circulatory disease | -1191.0297 | 922.2869 | ±1844.5737 | -1.291 | 0.1966 |  |
| Time 54-69, pooled (%) | -1439.0991 | 1069.3678 | ±2138.7355 | -1.346 | 0.1784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **178**, R² = **0.1722**, Adj R² = **0.1174**, F-statistic = **3.14** (p = **7.07e-04**), Residual SE = **4708.443** on **166** df, AIC = **3527.5**, BIC = **3565.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18718.4211** | 3841.1485 | ±7682.2970 | **+4.873** | **1.10e-06** | *** |
| **Education: graduate level (vs college)** | **-2267.6349** | 799.1261 | ±1598.2522 | **-2.838** | **0.0045** | ** |
| Education: high school or below (vs college) | -360.3082 | 1295.4246 | ±2590.8491 | -0.278 | 0.7809 |  |
| Site: UCSD (vs UAB) | +594.7354 | 975.2873 | ±1950.5746 | +0.610 | 0.5420 |  |
| Site: UW (vs UAB) | +966.1005 | 987.2956 | ±1974.5913 | +0.979 | 0.3278 |  |
| **Age (years)** | **-141.5779** | 48.8255 | ±97.6511 | **-2.900** | **0.0037** | ** |
| BMI (kg/m2) | +21.7161 | 65.6073 | ±131.2147 | +0.331 | 0.7406 |  |
| Hypertension | +908.2729 | 838.6042 | ±1677.2083 | +1.083 | 0.2788 |  |
| High cholesterol | -189.6931 | 764.0367 | ±1528.0734 | -0.248 | 0.8039 |  |
| Kidney disease | +100.0648 | 1325.1856 | ±2650.3712 | +0.076 | 0.9398 |  |
| Circulatory disease | -1193.8821 | 924.9294 | ±1849.8589 | -1.291 | 0.1968 |  |
| Avg. daily time 54-69 (%) | -1758.2371 | 1018.8077 | ±2037.6155 | -1.726 | 0.0844 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **178**, R² = **0.1678**, Adj R² = **0.1126**, F-statistic = **3.04** (p = **9.89e-04**), Residual SE = **4721.061** on **166** df, AIC = **3528.4**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18863.9488** | 3842.0389 | ±7684.0777 | **+4.910** | **9.11e-07** | *** |
| **Education: graduate level (vs college)** | **-2290.6821** | 799.7933 | ±1599.5866 | **-2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | -384.9944 | 1303.4872 | ±2606.9745 | -0.295 | 0.7677 |  |
| Site: UCSD (vs UAB) | +557.8203 | 976.9686 | ±1953.9372 | +0.571 | 0.5680 |  |
| Site: UW (vs UAB) | +941.3417 | 989.8756 | ±1979.7512 | +0.951 | 0.3416 |  |
| **Age (years)** | **-144.1000** | 48.7583 | ±97.5165 | **-2.955** | **0.0031** | ** |
| BMI (kg/m2) | +22.5309 | 65.3803 | ±130.7607 | +0.345 | 0.7304 |  |
| Hypertension | +890.6150 | 837.1433 | ±1674.2866 | +1.064 | 0.2874 |  |
| High cholesterol | -202.9383 | 765.4867 | ±1530.9735 | -0.265 | 0.7909 |  |
| Kidney disease | +160.7665 | 1329.6462 | ±2659.2923 | +0.121 | 0.9038 |  |
| Circulatory disease | -1191.0297 | 922.2869 | ±1844.5737 | -1.291 | 0.1966 |  |
| Time < 70 (%) | -1439.0991 | 1069.3678 | ±2138.7355 | -1.346 | 0.1784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **178**, R² = **0.1722**, Adj R² = **0.1174**, F-statistic = **3.14** (p = **7.07e-04**), Residual SE = **4708.443** on **166** df, AIC = **3527.5**, BIC = **3565.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18718.4211** | 3841.1485 | ±7682.2970 | **+4.873** | **1.10e-06** | *** |
| **Education: graduate level (vs college)** | **-2267.6349** | 799.1261 | ±1598.2522 | **-2.838** | **0.0045** | ** |
| Education: high school or below (vs college) | -360.3082 | 1295.4246 | ±2590.8491 | -0.278 | 0.7809 |  |
| Site: UCSD (vs UAB) | +594.7354 | 975.2873 | ±1950.5746 | +0.610 | 0.5420 |  |
| Site: UW (vs UAB) | +966.1005 | 987.2956 | ±1974.5913 | +0.979 | 0.3278 |  |
| **Age (years)** | **-141.5779** | 48.8255 | ±97.6511 | **-2.900** | **0.0037** | ** |
| BMI (kg/m2) | +21.7161 | 65.6073 | ±131.2147 | +0.331 | 0.7406 |  |
| Hypertension | +908.2729 | 838.6042 | ±1677.2083 | +1.083 | 0.2788 |  |
| High cholesterol | -189.6931 | 764.0367 | ±1528.0734 | -0.248 | 0.8039 |  |
| Kidney disease | +100.0648 | 1325.1856 | ±2650.3712 | +0.076 | 0.9398 |  |
| Circulatory disease | -1193.8821 | 924.9294 | ±1849.8589 | -1.291 | 0.1968 |  |
| Avg. daily time < 70 (%) | -1758.2371 | 1018.8077 | ±2037.6155 | -1.726 | 0.0844 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.990** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19135.3508** | 3852.7456 | ±7705.4912 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2387.3500** | 812.4438 | ±1624.8876 | **-2.938** | **0.0033** | ** |
| Education: high school or below (vs college) | -560.1788 | 1283.9921 | ±2567.9842 | -0.436 | 0.6626 |  |
| Site: UCSD (vs UAB) | +607.1287 | 978.5005 | ±1957.0009 | +0.620 | 0.5349 |  |
| Site: UW (vs UAB) | +963.8184 | 1008.2625 | ±2016.5251 | +0.956 | 0.3391 |  |
| **Age (years)** | **-150.5219** | 48.8468 | ±97.6935 | **-3.082** | **0.0021** | ** |
| BMI (kg/m2) | +25.3572 | 65.3476 | ±130.6953 | +0.388 | 0.6980 |  |
| Hypertension | +909.8845 | 843.5293 | ±1687.0586 | +1.079 | 0.2807 |  |
| High cholesterol | -285.3771 | 766.5676 | ±1533.1352 | -0.372 | 0.7097 |  |
| Kidney disease | +291.2957 | 1399.0770 | ±2798.1540 | +0.208 | 0.8351 |  |
| Circulatory disease | -1255.5668 | 913.9697 | ±1827.9395 | -1.374 | 0.1695 |  |
| Time 181-250, pooled (%) | -23.1396 | 81.6050 | ±163.2101 | -0.284 | 0.7768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **178**, R² = **0.1608**, Adj R² = **0.1052**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.769** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19139.2948** | 3853.4888 | ±7706.9775 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2394.8707** | 812.8105 | ±1625.6211 | **-2.946** | **0.0032** | ** |
| Education: high school or below (vs college) | -569.3943 | 1283.1861 | ±2566.3722 | -0.444 | 0.6572 |  |
| Site: UCSD (vs UAB) | +610.2384 | 979.0058 | ±1958.0117 | +0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +970.5727 | 1007.8694 | ±2015.7389 | +0.963 | 0.3356 |  |
| **Age (years)** | **-150.8668** | 48.8870 | ±97.7741 | **-3.086** | **0.0020** | ** |
| BMI (kg/m2) | +24.9370 | 65.2502 | ±130.5003 | +0.382 | 0.7023 |  |
| Hypertension | +908.1743 | 843.1997 | ±1686.3994 | +1.077 | 0.2815 |  |
| High cholesterol | -279.9428 | 767.4102 | ±1534.8203 | -0.365 | 0.7153 |  |
| Kidney disease | +270.7989 | 1403.2719 | ±2806.5437 | +0.193 | 0.8470 |  |
| Circulatory disease | -1265.2114 | 916.0140 | ±1832.0281 | -1.381 | 0.1672 |  |
| Avg. daily time 181-250 (%) | -15.1298 | 86.1420 | ±172.2841 | -0.176 | 0.8606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.990** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19135.3508** | 3852.7456 | ±7705.4912 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2387.3500** | 812.4438 | ±1624.8876 | **-2.938** | **0.0033** | ** |
| Education: high school or below (vs college) | -560.1788 | 1283.9921 | ±2567.9842 | -0.436 | 0.6626 |  |
| Site: UCSD (vs UAB) | +607.1287 | 978.5005 | ±1957.0009 | +0.620 | 0.5349 |  |
| Site: UW (vs UAB) | +963.8184 | 1008.2625 | ±2016.5251 | +0.956 | 0.3391 |  |
| **Age (years)** | **-150.5219** | 48.8468 | ±97.6935 | **-3.082** | **0.0021** | ** |
| BMI (kg/m2) | +25.3572 | 65.3476 | ±130.6953 | +0.388 | 0.6980 |  |
| Hypertension | +909.8845 | 843.5293 | ±1687.0586 | +1.079 | 0.2807 |  |
| High cholesterol | -285.3771 | 766.5676 | ±1533.1352 | -0.372 | 0.7097 |  |
| Kidney disease | +291.2957 | 1399.0770 | ±2798.1540 | +0.208 | 0.8351 |  |
| Circulatory disease | -1255.5668 | 913.9697 | ±1827.9395 | -1.374 | 0.1695 |  |
| Time > 180 (%) | -23.1396 | 81.6050 | ±163.2101 | -0.284 | 0.7768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1608**, Adj R² = **0.1052**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.769** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19139.2948** | 3853.4888 | ±7706.9775 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2394.8707** | 812.8105 | ±1625.6211 | **-2.946** | **0.0032** | ** |
| Education: high school or below (vs college) | -569.3943 | 1283.1861 | ±2566.3722 | -0.444 | 0.6572 |  |
| Site: UCSD (vs UAB) | +610.2384 | 979.0058 | ±1958.0117 | +0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +970.5727 | 1007.8694 | ±2015.7389 | +0.963 | 0.3356 |  |
| **Age (years)** | **-150.8668** | 48.8870 | ±97.7741 | **-3.086** | **0.0020** | ** |
| BMI (kg/m2) | +24.9370 | 65.2502 | ±130.5003 | +0.382 | 0.7023 |  |
| Hypertension | +908.1743 | 843.1997 | ±1686.3994 | +1.077 | 0.2815 |  |
| High cholesterol | -279.9428 | 767.4102 | ±1534.8203 | -0.365 | 0.7153 |  |
| Kidney disease | +270.7989 | 1403.2719 | ±2806.5437 | +0.193 | 0.8470 |  |
| Circulatory disease | -1265.2114 | 916.0140 | ±1832.0281 | -1.381 | 0.1672 |  |
| Avg. daily time > 180 (%) | -15.1298 | 86.1420 | ±172.2841 | -0.176 | 0.8606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1617**, Adj R² = **0.1061**, F-statistic = **2.91** (p = **0.0016**), Residual SE = **4738.275** on **166** df, AIC = **3529.7**, BIC = **3567.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19228.5095** | 3867.1984 | ±7734.3968 | **+4.972** | **6.62e-07** | *** |
| **Education: graduate level (vs college)** | **-2416.7269** | 801.9250 | ±1603.8501 | **-3.014** | **0.0026** | ** |
| Education: high school or below (vs college) | -636.7166 | 1269.0908 | ±2538.1816 | -0.502 | 0.6159 |  |
| Site: UCSD (vs UAB) | +661.5990 | 980.2501 | ±1960.5002 | +0.675 | 0.4997 |  |
| Site: UW (vs UAB) | +1015.3458 | 992.4434 | ±1984.8869 | +1.023 | 0.3063 |  |
| **Age (years)** | **-152.8780** | 48.7806 | ±97.5613 | **-3.134** | **0.0017** | ** |
| BMI (kg/m2) | +21.2759 | 65.5960 | ±131.1920 | +0.324 | 0.7457 |  |
| Hypertension | +922.3182 | 850.7696 | ±1701.5391 | +1.084 | 0.2783 |  |
| High cholesterol | -262.8456 | 767.4595 | ±1534.9189 | -0.342 | 0.7320 |  |
| Kidney disease | +135.5237 | 1385.6018 | ±2771.2036 | +0.098 | 0.9221 |  |
| Circulatory disease | -1346.5467 | 916.6399 | ±1833.2798 | -1.469 | 0.1418 |  |
| Nocturnal time > 180 (%) | +34.2332 | 77.0663 | ±154.1326 | +0.444 | 0.6569 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 178; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1490**, F-statistic = **4.10** (p = **4.60e-05**), Residual SE = **13.609** on **167** df, AIC = **1445.2**, BIC = **1480.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5621** | 11.1678 | ±22.3356 | **+3.901** | **9.59e-05** | *** |
| **Education: graduate level (vs college)** | **-6.4973** | 2.2573 | ±4.5145 | **-2.878** | **0.0040** | ** |
| Education: high school or below (vs college) | -1.1003 | 3.8989 | ±7.7979 | -0.282 | 0.7778 |  |
| Site: UCSD (vs UAB) | +0.8730 | 2.7864 | ±5.5727 | +0.313 | 0.7540 |  |
| Site: UW (vs UAB) | +1.9945 | 2.7207 | ±5.4415 | +0.733 | 0.4635 |  |
| **Age (years)** | **-0.4422** | 0.1211 | ±0.2423 | **-3.651** | **2.61e-04** | *** |
| BMI (kg/m2) | +0.3475 | 0.2224 | ±0.4447 | +1.563 | 0.1181 |  |
| Hypertension | +1.5684 | 2.3833 | ±4.7666 | +0.658 | 0.5105 |  |
| High cholesterol | -0.1847 | 2.0547 | ±4.1094 | -0.090 | 0.9284 |  |
| Kidney disease | +1.4043 | 3.6991 | ±7.3981 | +0.380 | 0.7042 |  |
| Circulatory disease | -4.0232 | 2.5629 | ±5.1257 | -1.570 | 0.1165 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **178**, R² = **0.1998**, Adj R² = **0.1468**, F-statistic = **3.77** (p = **7.88e-05**), Residual SE = **13.627** on **166** df, AIC = **1446.6**, BIC = **1484.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+35.3124** | 15.8653 | ±31.7307 | **+2.226** | **0.0260** | * |
| **Education: graduate level (vs college)** | **-6.4251** | 2.2905 | ±4.5810 | **-2.805** | **0.0050** | ** |
| Education: high school or below (vs college) | -1.1914 | 3.8980 | ±7.7959 | -0.306 | 0.7599 |  |
| Site: UCSD (vs UAB) | +0.8768 | 2.7819 | ±5.5638 | +0.315 | 0.7526 |  |
| Site: UW (vs UAB) | +2.0277 | 2.7312 | ±5.4625 | +0.742 | 0.4578 |  |
| **Age (years)** | **-0.4430** | 0.1215 | ±0.2430 | **-3.646** | **2.66e-04** | *** |
| BMI (kg/m2) | +0.3264 | 0.2180 | ±0.4360 | +1.497 | 0.1343 |  |
| Hypertension | +1.4160 | 2.4106 | ±4.8212 | +0.587 | 0.5569 |  |
| High cholesterol | -0.3826 | 2.0462 | ±4.0924 | -0.187 | 0.8517 |  |
| Kidney disease | +1.7257 | 3.7276 | ±7.4552 | +0.463 | 0.6434 |  |
| Circulatory disease | -4.3083 | 2.6165 | ±5.2330 | -1.647 | 0.0996 | . |
| HbA1c (%) | +1.5383 | 1.8884 | ±3.7768 | +0.815 | 0.4153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **178**, R² = **0.2020**, Adj R² = **0.1491**, F-statistic = **3.82** (p = **6.59e-05**), Residual SE = **13.608** on **166** df, AIC = **1446.1**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.8965** | 15.7384 | ±31.4768 | **+2.154** | **0.0313** | * |
| **Education: graduate level (vs college)** | **-6.4475** | 2.2809 | ±4.5618 | **-2.827** | **0.0047** | ** |
| Education: high school or below (vs college) | -0.8763 | 3.9242 | ±7.8484 | -0.223 | 0.8233 |  |
| Site: UCSD (vs UAB) | +0.7605 | 2.8089 | ±5.6177 | +0.271 | 0.7866 |  |
| Site: UW (vs UAB) | +1.9618 | 2.7188 | ±5.4375 | +0.722 | 0.4705 |  |
| **Age (years)** | **-0.4411** | 0.1219 | ±0.2437 | **-3.620** | **2.95e-04** | *** |
| BMI (kg/m2) | +0.3366 | 0.2240 | ±0.4479 | +1.503 | 0.1329 |  |
| Hypertension | +1.4407 | 2.3827 | ±4.7654 | +0.605 | 0.5454 |  |
| High cholesterol | -0.1503 | 2.0762 | ±4.1525 | -0.072 | 0.9423 |  |
| Kidney disease | +1.0591 | 3.7488 | ±7.4977 | +0.283 | 0.7776 |  |
| Circulatory disease | -4.2539 | 2.5804 | ±5.1609 | -1.649 | 0.0992 | . |
| Mean glucose (mg/dL) | +0.0797 | 0.0837 | ±0.1674 | +0.952 | 0.3413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **178**, R² = **0.2020**, Adj R² = **0.1491**, F-statistic = **3.82** (p = **6.59e-05**), Residual SE = **13.608** on **166** df, AIC = **1446.1**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +22.8732 | 25.2414 | ±50.4829 | +0.906 | 0.3648 |  |
| **Education: graduate level (vs college)** | **-6.4475** | 2.2809 | ±4.5618 | **-2.827** | **0.0047** | ** |
| Education: high school or below (vs college) | -0.8763 | 3.9242 | ±7.8484 | -0.223 | 0.8233 |  |
| Site: UCSD (vs UAB) | +0.7605 | 2.8089 | ±5.6177 | +0.271 | 0.7866 |  |
| Site: UW (vs UAB) | +1.9618 | 2.7188 | ±5.4375 | +0.722 | 0.4705 |  |
| **Age (years)** | **-0.4411** | 0.1219 | ±0.2437 | **-3.620** | **2.95e-04** | *** |
| BMI (kg/m2) | +0.3366 | 0.2240 | ±0.4479 | +1.503 | 0.1329 |  |
| Hypertension | +1.4407 | 2.3827 | ±4.7654 | +0.605 | 0.5454 |  |
| High cholesterol | -0.1503 | 2.0762 | ±4.1525 | -0.072 | 0.9423 |  |
| Kidney disease | +1.0591 | 3.7488 | ±7.4977 | +0.283 | 0.7776 |  |
| Circulatory disease | -4.2539 | 2.5804 | ±5.1609 | -1.649 | 0.0992 | . |
| GMI (%) | +3.3303 | 3.4998 | ±6.9996 | +0.952 | 0.3413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **178**, R² = **0.2114**, Adj R² = **0.1591**, F-statistic = **4.04** (p = **2.99e-05**), Residual SE = **13.528** on **166** df, AIC = **1444.0**, BIC = **1482.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +28.3870 | 14.9769 | ±29.9539 | +1.895 | 0.0580 | . |
| **Education: graduate level (vs college)** | **-6.5201** | 2.2629 | ±4.5259 | **-2.881** | **0.0040** | ** |
| Education: high school or below (vs college) | -0.8804 | 3.8387 | ±7.6774 | -0.229 | 0.8186 |  |
| Site: UCSD (vs UAB) | +0.5886 | 2.7947 | ±5.5894 | +0.211 | 0.8332 |  |
| Site: UW (vs UAB) | +1.8569 | 2.6910 | ±5.3820 | +0.690 | 0.4902 |  |
| **Age (years)** | **-0.4295** | 0.1222 | ±0.2443 | **-3.516** | **4.38e-04** | *** |
| BMI (kg/m2) | +0.3265 | 0.2219 | ±0.4439 | +1.471 | 0.1413 |  |
| Hypertension | +1.3589 | 2.3723 | ±4.7446 | +0.573 | 0.5668 |  |
| High cholesterol | -0.2233 | 2.0656 | ±4.1311 | -0.108 | 0.9139 |  |
| Kidney disease | +1.3555 | 3.5934 | ±7.1868 | +0.377 | 0.7060 |  |
| Circulatory disease | -4.5710 | 2.5398 | ±5.0797 | -1.800 | 0.0719 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.1223 | 0.0734 | ±0.1468 | +1.667 | 0.0954 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.75e-05**), Residual SE = **13.648** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.8684** | 12.9079 | ±25.8159 | **+3.321** | **8.97e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5190** | 2.2461 | ±4.4922 | **-2.902** | **0.0037** | ** |
| Education: high school or below (vs college) | -1.1844 | 3.9634 | ±7.9268 | -0.299 | 0.7651 |  |
| Site: UCSD (vs UAB) | +0.8923 | 2.7956 | ±5.5911 | +0.319 | 0.7496 |  |
| Site: UW (vs UAB) | +2.0503 | 2.7735 | ±5.5469 | +0.739 | 0.4598 |  |
| **Age (years)** | **-0.4431** | 0.1215 | ±0.2431 | **-3.646** | **2.66e-04** | *** |
| BMI (kg/m2) | +0.3478 | 0.2246 | ±0.4491 | +1.549 | 0.1214 |  |
| Hypertension | +1.5040 | 2.4494 | ±4.8987 | +0.614 | 0.5392 |  |
| High cholesterol | -0.1652 | 2.0802 | ±4.1604 | -0.079 | 0.9367 |  |
| Kidney disease | +1.3228 | 3.7613 | ±7.5225 | +0.352 | 0.7251 |  |
| Circulatory disease | -4.0621 | 2.5865 | ±5.1730 | -1.570 | 0.1163 |  |
| Glucose SD, pooled (mg/dL) | +0.0359 | 0.2220 | ±0.4440 | +0.162 | 0.8714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.79e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.0855** | 12.6079 | ±25.2159 | **+3.417** | **6.32e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5128** | 2.2433 | ±4.4866 | **-2.903** | **0.0037** | ** |
| Education: high school or below (vs college) | -1.1472 | 3.9546 | ±7.9092 | -0.290 | 0.7717 |  |
| Site: UCSD (vs UAB) | +0.8728 | 2.8000 | ±5.6001 | +0.312 | 0.7552 |  |
| Site: UW (vs UAB) | +2.0207 | 2.7561 | ±5.5122 | +0.733 | 0.4635 |  |
| **Age (years)** | **-0.4429** | 0.1219 | ±0.2437 | **-3.635** | **2.78e-04** | *** |
| BMI (kg/m2) | +0.3480 | 0.2251 | ±0.4502 | +1.546 | 0.1221 |  |
| Hypertension | +1.5114 | 2.4524 | ±4.9048 | +0.616 | 0.5377 |  |
| High cholesterol | -0.1672 | 2.0839 | ±4.1678 | -0.080 | 0.9360 |  |
| Kidney disease | +1.3601 | 3.7281 | ±7.4562 | +0.365 | 0.7152 |  |
| Circulatory disease | -4.0445 | 2.5805 | ±5.1609 | -1.567 | 0.1170 |  |
| Avg. daily SD (mg/dL) | +0.0272 | 0.2222 | ±0.4443 | +0.122 | 0.9027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **178**, R² = **0.1983**, Adj R² = **0.1452**, F-statistic = **3.73** (p = **8.90e-05**), Residual SE = **13.639** on **166** df, AIC = **1446.9**, BIC = **1485.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2821** | 13.7106 | ±27.4213 | **+3.376** | **7.36e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4079** | 2.2464 | ±4.4929 | **-2.852** | **0.0043** | ** |
| Education: high school or below (vs college) | -0.7020 | 4.1200 | ±8.2399 | -0.170 | 0.8647 |  |
| Site: UCSD (vs UAB) | +0.7673 | 2.8009 | ±5.6017 | +0.274 | 0.7841 |  |
| Site: UW (vs UAB) | +1.7717 | 2.8134 | ±5.6267 | +0.630 | 0.5289 |  |
| **Age (years)** | **-0.4384** | 0.1222 | ±0.2443 | **-3.588** | **3.33e-04** | *** |
| BMI (kg/m2) | +0.3431 | 0.2327 | ±0.4655 | +1.474 | 0.1404 |  |
| Hypertension | +1.7782 | 2.4711 | ±4.9423 | +0.720 | 0.4718 |  |
| High cholesterol | -0.2464 | 2.0699 | ±4.1398 | -0.119 | 0.9052 |  |
| Kidney disease | +1.6148 | 3.6871 | ±7.3742 | +0.438 | 0.6614 |  |
| Circulatory disease | -3.9564 | 2.5975 | ±5.1951 | -1.523 | 0.1277 |  |
| CV (%) | -0.1714 | 0.3318 | ±0.6636 | -0.516 | 0.6055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **178**, R² = **0.1973**, Adj R² = **0.1441**, F-statistic = **3.71** (p = **9.73e-05**), Residual SE = **13.648** on **166** df, AIC = **1447.2**, BIC = **1485.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.5222** | 11.6222 | ±23.2444 | **+3.659** | **2.53e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4755** | 2.2519 | ±4.5038 | **-2.876** | **0.0040** | ** |
| Education: high school or below (vs college) | -0.9815 | 4.0465 | ±8.0930 | -0.243 | 0.8084 |  |
| Site: UCSD (vs UAB) | +0.8477 | 2.8023 | ±5.6046 | +0.302 | 0.7623 |  |
| Site: UW (vs UAB) | +1.9283 | 2.8024 | ±5.6047 | +0.688 | 0.4914 |  |
| **Age (years)** | **-0.4408** | 0.1220 | ±0.2441 | **-3.612** | **3.04e-04** | *** |
| BMI (kg/m2) | +0.3472 | 0.2256 | ±0.4513 | +1.538 | 0.1239 |  |
| Hypertension | +1.6422 | 2.4543 | ±4.9086 | +0.669 | 0.5034 |  |
| High cholesterol | -0.1950 | 2.0692 | ±4.1384 | -0.094 | 0.9249 |  |
| Kidney disease | +1.4719 | 3.6906 | ±7.3813 | +0.399 | 0.6900 |  |
| Circulatory disease | -4.0108 | 2.5817 | ±5.1634 | -1.554 | 0.1203 |  |
| Mean / SD ratio | +0.1513 | 0.7818 | ±1.5635 | +0.194 | 0.8465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.78e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.2436** | 11.5168 | ±23.0337 | **+3.842** | **1.22e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5088** | 2.2518 | ±4.5036 | **-2.890** | **0.0038** | ** |
| Education: high school or below (vs college) | -1.1629 | 4.0109 | ±8.0218 | -0.290 | 0.7719 |  |
| Site: UCSD (vs UAB) | +0.8687 | 2.7955 | ±5.5910 | +0.311 | 0.7560 |  |
| Site: UW (vs UAB) | +2.0266 | 2.7650 | ±5.5301 | +0.733 | 0.4636 |  |
| **Age (years)** | **-0.4434** | 0.1223 | ±0.2446 | **-3.626** | **2.87e-04** | *** |
| BMI (kg/m2) | +0.3478 | 0.2242 | ±0.4483 | +1.552 | 0.1207 |  |
| Hypertension | +1.5048 | 2.4531 | ±4.9062 | +0.613 | 0.5396 |  |
| High cholesterol | -0.1801 | 2.0704 | ±4.1409 | -0.087 | 0.9307 |  |
| Kidney disease | +1.3720 | 3.6964 | ±7.3929 | +0.371 | 0.7105 |  |
| Circulatory disease | -4.0183 | 2.5740 | ±5.1480 | -1.561 | 0.1185 |  |
| Avg. daily mean/SD | -0.0832 | 0.5850 | ±1.1699 | -0.142 | 0.8868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **178**, R² = **0.1997**, Adj R² = **0.1467**, F-statistic = **3.77** (p = **7.92e-05**), Residual SE = **13.627** on **166** df, AIC = **1446.6**, BIC = **1484.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.7191** | 11.8744 | ±23.7488 | **+3.345** | **8.23e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5397** | 2.2649 | ±4.5299 | **-2.887** | **0.0039** | ** |
| Education: high school or below (vs college) | -1.2675 | 3.9167 | ±7.8335 | -0.324 | 0.7462 |  |
| Site: UCSD (vs UAB) | +0.8019 | 2.8069 | ±5.6138 | +0.286 | 0.7751 |  |
| Site: UW (vs UAB) | +2.0740 | 2.7121 | ±5.4243 | +0.765 | 0.4444 |  |
| **Age (years)** | **-0.4423** | 0.1209 | ±0.2418 | **-3.659** | **2.53e-04** | *** |
| BMI (kg/m2) | +0.3408 | 0.2272 | ±0.4544 | +1.500 | 0.1337 |  |
| Hypertension | +1.5008 | 2.3794 | ±4.7589 | +0.631 | 0.5282 |  |
| High cholesterol | -0.2565 | 2.0727 | ±4.1453 | -0.124 | 0.9015 |  |
| Kidney disease | +1.4303 | 3.7356 | ±7.4712 | +0.383 | 0.7018 |  |
| Circulatory disease | -4.0149 | 2.5657 | ±5.1313 | -1.565 | 0.1176 |  |
| MAG (mg/dL/h) | +0.1150 | 0.1385 | ±0.2770 | +0.830 | 0.4063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5872** | 13.5021 | ±27.0041 | **+3.228** | **0.0012** | ** |
| **Education: graduate level (vs college)** | **-6.4969** | 2.2521 | ±4.5042 | **-2.885** | **0.0039** | ** |
| Education: high school or below (vs college) | -1.0986 | 3.9717 | ±7.9434 | -0.277 | 0.7821 |  |
| Site: UCSD (vs UAB) | +0.8726 | 2.8029 | ±5.6057 | +0.311 | 0.7555 |  |
| Site: UW (vs UAB) | +1.9933 | 2.7643 | ±5.5286 | +0.721 | 0.4708 |  |
| **Age (years)** | **-0.4422** | 0.1223 | ±0.2446 | **-3.615** | **3.01e-04** | *** |
| BMI (kg/m2) | +0.3475 | 0.2293 | ±0.4587 | +1.515 | 0.1298 |  |
| Hypertension | +1.5699 | 2.4265 | ±4.8530 | +0.647 | 0.5176 |  |
| High cholesterol | -0.1852 | 2.0806 | ±4.1613 | -0.089 | 0.9291 |  |
| Kidney disease | +1.4056 | 3.6922 | ±7.3843 | +0.381 | 0.7034 |  |
| Circulatory disease | -4.0226 | 2.5873 | ±5.1747 | -1.555 | 0.1200 |  |
| Avg. daily range (mg/dL) | -0.0003 | 0.0583 | ±0.1166 | -0.005 | 0.9963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6324** | 12.1403 | ±24.2806 | **+3.594** | **3.26e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4946** | 2.2799 | ±4.5598 | **-2.849** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0787 | 3.8743 | ±7.7486 | -0.278 | 0.7807 |  |
| Site: UCSD (vs UAB) | +0.8607 | 2.6752 | ±5.3505 | +0.322 | 0.7476 |  |
| Site: UW (vs UAB) | +1.9792 | 2.6909 | ±5.3819 | +0.736 | 0.4620 |  |
| **Age (years)** | **-0.4420** | 0.1197 | ±0.2394 | **-3.693** | **2.22e-04** | *** |
| BMI (kg/m2) | +0.3476 | 0.2239 | ±0.4478 | +1.553 | 0.1205 |  |
| Hypertension | +1.5652 | 2.3887 | ±4.7774 | +0.655 | 0.5123 |  |
| High cholesterol | -0.1830 | 2.0641 | ±4.1281 | -0.089 | 0.9293 |  |
| Kidney disease | +1.4234 | 4.0706 | ±8.1413 | +0.350 | 0.7266 |  |
| Circulatory disease | -4.0084 | 2.6696 | ±5.3393 | -1.501 | 0.1332 |  |
| SD of daily means (mg/dL) | -0.0130 | 0.4890 | ±0.9779 | -0.027 | 0.9787 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **178**, R² = **0.1973**, Adj R² = **0.1441**, F-statistic = **3.71** (p = **9.69e-05**), Residual SE = **13.648** on **166** df, AIC = **1447.2**, BIC = **1485.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +39.1123 | 23.7927 | ±47.5853 | +1.644 | 0.1002 |  |
| **Education: graduate level (vs college)** | **-6.4598** | 2.2749 | ±4.5498 | **-2.840** | **0.0045** | ** |
| Education: high school or below (vs college) | -1.0611 | 3.9079 | ±7.8158 | -0.272 | 0.7860 |  |
| Site: UCSD (vs UAB) | +0.8536 | 2.7866 | ±5.5732 | +0.306 | 0.7594 |  |
| Site: UW (vs UAB) | +1.9716 | 2.7488 | ±5.4976 | +0.717 | 0.4732 |  |
| **Age (years)** | **-0.4399** | 0.1209 | ±0.2418 | **-3.639** | **2.74e-04** | *** |
| BMI (kg/m2) | +0.3491 | 0.2231 | ±0.4462 | +1.565 | 0.1176 |  |
| Hypertension | +1.5886 | 2.3999 | ±4.7998 | +0.662 | 0.5080 |  |
| High cholesterol | -0.2140 | 2.0618 | ±4.1237 | -0.104 | 0.9173 |  |
| Kidney disease | +1.5195 | 3.8781 | ±7.7562 | +0.392 | 0.6952 |  |
| Circulatory disease | -3.9638 | 2.6145 | ±5.2290 | -1.516 | 0.1295 |  |
| Time in range 70-180, pooled (%) | +0.0441 | 0.2198 | ±0.4395 | +0.201 | 0.8408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.80e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +41.2458 | 24.4872 | ±48.9745 | +1.684 | 0.0921 | . |
| **Education: graduate level (vs college)** | **-6.4799** | 2.2750 | ±4.5500 | **-2.848** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0850 | 3.9068 | ±7.8137 | -0.278 | 0.7812 |  |
| Site: UCSD (vs UAB) | +0.8634 | 2.7876 | ±5.5751 | +0.310 | 0.7568 |  |
| Site: UW (vs UAB) | +1.9872 | 2.7461 | ±5.4921 | +0.724 | 0.4693 |  |
| **Age (years)** | **-0.4410** | 0.1209 | ±0.2418 | **-3.648** | **2.65e-04** | *** |
| BMI (kg/m2) | +0.3482 | 0.2230 | ±0.4460 | +1.561 | 0.1184 |  |
| Hypertension | +1.5822 | 2.3998 | ±4.7996 | +0.659 | 0.5097 |  |
| High cholesterol | -0.2003 | 2.0627 | ±4.1255 | -0.097 | 0.9226 |  |
| Kidney disease | +1.4648 | 3.8864 | ±7.7728 | +0.377 | 0.7062 |  |
| Circulatory disease | -3.9917 | 2.6150 | ±5.2301 | -1.526 | 0.1269 |  |
| Avg. daily time in range 70-180 (%) | +0.0230 | 0.2269 | ±0.4539 | +0.101 | 0.9194 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **178**, R² = **0.2041**, Adj R² = **0.1514**, F-statistic = **3.87** (p = **5.51e-05**), Residual SE = **13.590** on **166** df, AIC = **1445.6**, BIC = **1483.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.7309** | 11.3132 | ±22.6263 | **+3.777** | **1.59e-04** | *** |
| **Education: graduate level (vs college)** | **-6.1641** | 2.2562 | ±4.5124 | **-2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | -0.5398 | 3.9697 | ±7.9393 | -0.136 | 0.8918 |  |
| Site: UCSD (vs UAB) | +0.7027 | 2.7690 | ±5.5381 | +0.254 | 0.7997 |  |
| Site: UW (vs UAB) | +1.8957 | 2.7120 | ±5.4239 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.4204** | 0.1243 | ±0.2485 | **-3.383** | **7.17e-04** | *** |
| BMI (kg/m2) | +0.3419 | 0.2253 | ±0.4506 | +1.517 | 0.1292 |  |
| Hypertension | +1.5436 | 2.3680 | ±4.7360 | +0.652 | 0.5145 |  |
| High cholesterol | +0.0074 | 2.0514 | ±4.1028 | +0.004 | 0.9971 |  |
| Kidney disease | +1.2035 | 3.7003 | ±7.4005 | +0.325 | 0.7450 |  |
| Circulatory disease | -3.7492 | 2.6192 | ±5.2385 | -1.431 | 0.1523 |  |
| Time 54-69, pooled (%) | -4.1876 | 3.2870 | ±6.5740 | -1.274 | 0.2027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **178**, R² = **0.2105**, Adj R² = **0.1582**, F-statistic = **4.02** (p = **3.21e-05**), Residual SE = **13.535** on **166** df, AIC = **1444.2**, BIC = **1482.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1973** | 11.3114 | ±22.6227 | **+3.731** | **1.91e-04** | *** |
| **Education: graduate level (vs college)** | **-6.0620** | 2.2500 | ±4.4999 | **-2.694** | **0.0071** | ** |
| Education: high school or below (vs college) | -0.4125 | 3.9406 | ±7.8812 | -0.105 | 0.9166 |  |
| Site: UCSD (vs UAB) | +0.8045 | 2.7610 | ±5.5220 | +0.291 | 0.7707 |  |
| Site: UW (vs UAB) | +1.9654 | 2.7065 | ±5.4129 | +0.726 | 0.4677 |  |
| **Age (years)** | **-0.4105** | 0.1239 | ±0.2478 | **-3.314** | **9.21e-04** | *** |
| BMI (kg/m2) | +0.3388 | 0.2265 | ±0.4529 | +1.496 | 0.1346 |  |
| Hypertension | +1.5973 | 2.3628 | ±4.7255 | +0.676 | 0.4990 |  |
| High cholesterol | +0.0662 | 2.0396 | ±4.0792 | +0.032 | 0.9741 |  |
| Kidney disease | +0.9937 | 3.6705 | ±7.3411 | +0.271 | 0.7866 |  |
| Circulatory disease | -3.7341 | 2.6286 | ±5.2572 | -1.421 | 0.1554 |  |
| Avg. daily time 54-69 (%) | -5.5654 | 2.9333 | ±5.8666 | -1.897 | 0.0578 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **178**, R² = **0.2041**, Adj R² = **0.1514**, F-statistic = **3.87** (p = **5.51e-05**), Residual SE = **13.590** on **166** df, AIC = **1445.6**, BIC = **1483.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.7309** | 11.3132 | ±22.6263 | **+3.777** | **1.59e-04** | *** |
| **Education: graduate level (vs college)** | **-6.1641** | 2.2562 | ±4.5124 | **-2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | -0.5398 | 3.9697 | ±7.9393 | -0.136 | 0.8918 |  |
| Site: UCSD (vs UAB) | +0.7027 | 2.7690 | ±5.5381 | +0.254 | 0.7997 |  |
| Site: UW (vs UAB) | +1.8957 | 2.7120 | ±5.4239 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.4204** | 0.1243 | ±0.2485 | **-3.383** | **7.17e-04** | *** |
| BMI (kg/m2) | +0.3419 | 0.2253 | ±0.4506 | +1.517 | 0.1292 |  |
| Hypertension | +1.5436 | 2.3680 | ±4.7360 | +0.652 | 0.5145 |  |
| High cholesterol | +0.0074 | 2.0514 | ±4.1028 | +0.004 | 0.9971 |  |
| Kidney disease | +1.2035 | 3.7003 | ±7.4005 | +0.325 | 0.7450 |  |
| Circulatory disease | -3.7492 | 2.6192 | ±5.2385 | -1.431 | 0.1523 |  |
| Time < 70 (%) | -4.1876 | 3.2870 | ±6.5740 | -1.274 | 0.2027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **178**, R² = **0.2105**, Adj R² = **0.1582**, F-statistic = **4.02** (p = **3.21e-05**), Residual SE = **13.535** on **166** df, AIC = **1444.2**, BIC = **1482.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1973** | 11.3114 | ±22.6227 | **+3.731** | **1.91e-04** | *** |
| **Education: graduate level (vs college)** | **-6.0620** | 2.2500 | ±4.4999 | **-2.694** | **0.0071** | ** |
| Education: high school or below (vs college) | -0.4125 | 3.9406 | ±7.8812 | -0.105 | 0.9166 |  |
| Site: UCSD (vs UAB) | +0.8045 | 2.7610 | ±5.5220 | +0.291 | 0.7707 |  |
| Site: UW (vs UAB) | +1.9654 | 2.7065 | ±5.4129 | +0.726 | 0.4677 |  |
| **Age (years)** | **-0.4105** | 0.1239 | ±0.2478 | **-3.314** | **9.21e-04** | *** |
| BMI (kg/m2) | +0.3388 | 0.2265 | ±0.4529 | +1.496 | 0.1346 |  |
| Hypertension | +1.5973 | 2.3628 | ±4.7255 | +0.676 | 0.4990 |  |
| High cholesterol | +0.0662 | 2.0396 | ±4.0792 | +0.032 | 0.9741 |  |
| Kidney disease | +0.9937 | 3.6705 | ±7.3411 | +0.271 | 0.7866 |  |
| Circulatory disease | -3.7341 | 2.6286 | ±5.2572 | -1.421 | 0.1554 |  |
| Avg. daily time < 70 (%) | -5.5654 | 2.9333 | ±5.8666 | -1.897 | 0.0578 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.78e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5455** | 11.2095 | ±22.4189 | **+3.885** | **1.02e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4766** | 2.2739 | ±4.5478 | **-2.848** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0800 | 3.9071 | ±7.8143 | -0.276 | 0.7822 |  |
| Site: UCSD (vs UAB) | +0.8623 | 2.7892 | ±5.5783 | +0.309 | 0.7572 |  |
| Site: UW (vs UAB) | +1.9812 | 2.7464 | ±5.4927 | +0.721 | 0.4707 |  |
| **Age (years)** | **-0.4410** | 0.1210 | ±0.2420 | **-3.644** | **2.68e-04** | *** |
| BMI (kg/m2) | +0.3485 | 0.2230 | ±0.4460 | +1.563 | 0.1180 |  |
| Hypertension | +1.5808 | 2.4004 | ±4.8008 | +0.659 | 0.5102 |  |
| High cholesterol | -0.2038 | 2.0634 | ±4.1267 | -0.099 | 0.9213 |  |
| Kidney disease | +1.4758 | 3.8807 | ±7.7615 | +0.380 | 0.7037 |  |
| Circulatory disease | -3.9888 | 2.6100 | ±5.2200 | -1.528 | 0.1264 |  |
| Time 181-250, pooled (%) | -0.0269 | 0.2184 | ±0.4368 | -0.123 | 0.9020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5637** | 11.2031 | ±22.4062 | **+3.889** | **1.01e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4989** | 2.2742 | ±4.5484 | **-2.858** | **0.0043** | ** |
| Education: high school or below (vs college) | -1.1015 | 3.9058 | ±7.8116 | -0.282 | 0.7779 |  |
| Site: UCSD (vs UAB) | +0.8740 | 2.7900 | ±5.5801 | +0.313 | 0.7541 |  |
| Site: UW (vs UAB) | +1.9952 | 2.7431 | ±5.4861 | +0.727 | 0.4670 |  |
| **Age (years)** | **-0.4423** | 0.1210 | ±0.2420 | **-3.656** | **2.56e-04** | *** |
| BMI (kg/m2) | +0.3474 | 0.2228 | ±0.4456 | +1.559 | 0.1189 |  |
| Hypertension | +1.5670 | 2.4003 | ±4.8005 | +0.653 | 0.5139 |  |
| High cholesterol | -0.1830 | 2.0646 | ±4.1291 | -0.089 | 0.9294 |  |
| Kidney disease | +1.3980 | 3.8900 | ±7.7801 | +0.359 | 0.7193 |  |
| Circulatory disease | -4.0263 | 2.6107 | ±5.2213 | -1.542 | 0.1230 |  |
| Avg. daily time 181-250 (%) | +0.0023 | 0.2256 | ±0.4512 | +0.010 | 0.9917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.78e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5455** | 11.2095 | ±22.4189 | **+3.885** | **1.02e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4766** | 2.2739 | ±4.5478 | **-2.848** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0800 | 3.9071 | ±7.8143 | -0.276 | 0.7822 |  |
| Site: UCSD (vs UAB) | +0.8623 | 2.7892 | ±5.5783 | +0.309 | 0.7572 |  |
| Site: UW (vs UAB) | +1.9812 | 2.7464 | ±5.4927 | +0.721 | 0.4707 |  |
| **Age (years)** | **-0.4410** | 0.1210 | ±0.2420 | **-3.644** | **2.68e-04** | *** |
| BMI (kg/m2) | +0.3485 | 0.2230 | ±0.4460 | +1.563 | 0.1180 |  |
| Hypertension | +1.5808 | 2.4004 | ±4.8008 | +0.659 | 0.5102 |  |
| High cholesterol | -0.2038 | 2.0634 | ±4.1267 | -0.099 | 0.9213 |  |
| Kidney disease | +1.4758 | 3.8807 | ±7.7615 | +0.380 | 0.7037 |  |
| Circulatory disease | -3.9888 | 2.6100 | ±5.2200 | -1.528 | 0.1264 |  |
| Time > 180 (%) | -0.0269 | 0.2184 | ±0.4368 | -0.123 | 0.9020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5637** | 11.2031 | ±22.4062 | **+3.889** | **1.01e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4989** | 2.2742 | ±4.5484 | **-2.858** | **0.0043** | ** |
| Education: high school or below (vs college) | -1.1015 | 3.9058 | ±7.8116 | -0.282 | 0.7779 |  |
| Site: UCSD (vs UAB) | +0.8740 | 2.7900 | ±5.5801 | +0.313 | 0.7541 |  |
| Site: UW (vs UAB) | +1.9952 | 2.7431 | ±5.4861 | +0.727 | 0.4670 |  |
| **Age (years)** | **-0.4423** | 0.1210 | ±0.2420 | **-3.656** | **2.56e-04** | *** |
| BMI (kg/m2) | +0.3474 | 0.2228 | ±0.4456 | +1.559 | 0.1189 |  |
| Hypertension | +1.5670 | 2.4003 | ±4.8005 | +0.653 | 0.5139 |  |
| High cholesterol | -0.1830 | 2.0646 | ±4.1291 | -0.089 | 0.9294 |  |
| Kidney disease | +1.3980 | 3.8900 | ±7.7801 | +0.359 | 0.7193 |  |
| Circulatory disease | -4.0263 | 2.6107 | ±5.2213 | -1.542 | 0.1230 |  |
| Avg. daily time > 180 (%) | +0.0023 | 0.2256 | ±0.4512 | +0.010 | 0.9917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **178**, R² = **0.2014**, Adj R² = **0.1485**, F-statistic = **3.81** (p = **6.91e-05**), Residual SE = **13.613** on **166** df, AIC = **1446.2**, BIC = **1484.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.0260** | 11.2865 | ±22.5730 | **+3.901** | **9.59e-05** | *** |
| **Education: graduate level (vs college)** | **-6.5652** | 2.2652 | ±4.5305 | **-2.898** | **0.0038** | ** |
| Education: high school or below (vs college) | -1.4478 | 3.8529 | ±7.7058 | -0.376 | 0.7071 |  |
| Site: UCSD (vs UAB) | +1.1389 | 2.8139 | ±5.6277 | +0.405 | 0.6857 |  |
| Site: UW (vs UAB) | +2.2300 | 2.6927 | ±5.3855 | +0.828 | 0.4076 |  |
| **Age (years)** | **-0.4498** | 0.1222 | ±0.2443 | **-3.682** | **2.32e-04** | *** |
| BMI (kg/m2) | +0.3287 | 0.2249 | ±0.4498 | +1.462 | 0.1439 |  |
| Hypertension | +1.7047 | 2.4280 | ±4.8560 | +0.702 | 0.4826 |  |
| High cholesterol | -0.1488 | 2.0750 | ±4.1501 | -0.072 | 0.9428 |  |
| Kidney disease | +0.8502 | 3.8579 | ±7.7158 | +0.220 | 0.8256 |  |
| Circulatory disease | -4.3837 | 2.5942 | ±5.1884 | -1.690 | 0.0911 | . |
| Nocturnal time > 180 (%) | +0.2012 | 0.2503 | ±0.5007 | +0.804 | 0.4215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 177; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2077**, F-statistic = **5.61** (p = **3.30e-07**), Residual SE = **8.026** on **166** df, AIC = **1250.2**, BIC = **1285.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5749** | 5.9627 | ±11.9255 | **+12.842** | **9.51e-38** | *** |
| **Education: graduate level (vs college)** | **-3.4460** | 1.3908 | ±2.7815 | **-2.478** | **0.0132** | * |
| **Education: high school or below (vs college)** | **-4.0112** | 2.0130 | ±4.0260 | **-1.993** | **0.0463** | * |
| Site: UCSD (vs UAB) | -1.4843 | 1.7025 | ±3.4049 | -0.872 | 0.3833 |  |
| Site: UW (vs UAB) | -0.8727 | 1.6431 | ±3.2862 | -0.531 | 0.5953 |  |
| **Age (years)** | **-0.2794** | 0.0749 | ±0.1499 | **-3.728** | **1.93e-04** | *** |
| **BMI (kg/m2)** | **+0.1894** | 0.0962 | ±0.1925 | **+1.968** | **0.0490** | * |
| Hypertension | +1.4911 | 1.5123 | ±3.0246 | +0.986 | 0.3241 |  |
| High cholesterol | +0.3730 | 1.2943 | ±2.5885 | +0.288 | 0.7732 |  |
| **Kidney disease** | **+6.7713** | 1.8211 | ±3.6421 | **+3.718** | **2.01e-04** | *** |
| Circulatory disease | -0.3238 | 1.8606 | ±3.7212 | -0.174 | 0.8618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **177**, R² = **0.2533**, Adj R² = **0.2035**, F-statistic = **5.09** (p = **7.82e-07**), Residual SE = **8.048** on **165** df, AIC = **1252.1**, BIC = **1290.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.3842** | 8.6535 | ±17.3070 | **+8.596** | **8.27e-18** | *** |
| **Education: graduate level (vs college)** | **-3.4269** | 1.4101 | ±2.8202 | **-2.430** | **0.0151** | * |
| **Education: high school or below (vs college)** | **-4.0355** | 2.0173 | ±4.0345 | **-2.000** | **0.0455** | * |
| Site: UCSD (vs UAB) | -1.4831 | 1.7067 | ±3.4135 | -0.869 | 0.3849 |  |
| Site: UW (vs UAB) | -0.8638 | 1.6557 | ±3.3113 | -0.522 | 0.6019 |  |
| **Age (years)** | **-0.2796** | 0.0753 | ±0.1505 | **-3.714** | **2.04e-04** | *** |
| BMI (kg/m2) | +0.1838 | 0.0988 | ±0.1976 | +1.861 | 0.0628 | . |
| Hypertension | +1.4506 | 1.5262 | ±3.0523 | +0.951 | 0.3419 |  |
| High cholesterol | +0.3206 | 1.3245 | ±2.6490 | +0.242 | 0.8088 |  |
| **Kidney disease** | **+6.8563** | 1.8363 | ±3.6726 | **+3.734** | **1.89e-04** | *** |
| Circulatory disease | -0.3995 | 1.8643 | ±3.7287 | -0.214 | 0.8303 |  |
| HbA1c (%) | +0.4085 | 1.2964 | ±2.5927 | +0.315 | 0.7527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **177**, R² = **0.2598**, Adj R² = **0.2104**, F-statistic = **5.26** (p = **4.22e-07**), Residual SE = **8.013** on **165** df, AIC = **1250.6**, BIC = **1288.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4529** | 8.2139 | ±16.4277 | **+8.456** | **2.78e-17** | *** |
| **Education: graduate level (vs college)** | **-3.3827** | 1.4059 | ±2.8118 | **-2.406** | **0.0161** | * |
| Education: high school or below (vs college) | -3.8330 | 2.0302 | ±4.0604 | -1.888 | 0.0590 | . |
| Site: UCSD (vs UAB) | -1.6001 | 1.7033 | ±3.4067 | -0.939 | 0.3475 |  |
| Site: UW (vs UAB) | -0.9175 | 1.6379 | ±3.2758 | -0.560 | 0.5754 |  |
| **Age (years)** | **-0.2782** | 0.0752 | ±0.1504 | **-3.700** | **2.15e-04** | *** |
| BMI (kg/m2) | +0.1806 | 0.0974 | ±0.1948 | +1.854 | 0.0637 | . |
| Hypertension | +1.3938 | 1.4950 | ±2.9900 | +0.932 | 0.3512 |  |
| High cholesterol | +0.3676 | 1.3020 | ±2.6041 | +0.282 | 0.7777 |  |
| **Kidney disease** | **+6.5856** | 1.8243 | ±3.6486 | **+3.610** | **3.06e-04** | *** |
| Circulatory disease | -0.5045 | 1.8391 | ±3.6783 | -0.274 | 0.7839 |  |
| Mean glucose (mg/dL) | +0.0589 | 0.0477 | ±0.0953 | +1.237 | 0.2163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **177**, R² = **0.2598**, Adj R² = **0.2104**, F-statistic = **5.26** (p = **4.22e-07**), Residual SE = **8.013** on **165** df, AIC = **1250.6**, BIC = **1288.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.2962** | 13.5700 | ±27.1400 | **+4.517** | **6.27e-06** | *** |
| **Education: graduate level (vs college)** | **-3.3827** | 1.4059 | ±2.8118 | **-2.406** | **0.0161** | * |
| Education: high school or below (vs college) | -3.8330 | 2.0302 | ±4.0604 | -1.888 | 0.0590 | . |
| Site: UCSD (vs UAB) | -1.6001 | 1.7033 | ±3.4067 | -0.939 | 0.3475 |  |
| Site: UW (vs UAB) | -0.9175 | 1.6379 | ±3.2758 | -0.560 | 0.5754 |  |
| **Age (years)** | **-0.2782** | 0.0752 | ±0.1504 | **-3.700** | **2.15e-04** | *** |
| BMI (kg/m2) | +0.1806 | 0.0974 | ±0.1948 | +1.854 | 0.0637 | . |
| Hypertension | +1.3938 | 1.4950 | ±2.9900 | +0.932 | 0.3512 |  |
| High cholesterol | +0.3676 | 1.3020 | ±2.6041 | +0.282 | 0.7777 |  |
| **Kidney disease** | **+6.5856** | 1.8243 | ±3.6486 | **+3.610** | **3.06e-04** | *** |
| Circulatory disease | -0.5045 | 1.8391 | ±3.6783 | -0.274 | 0.7839 |  |
| GMI (%) | +2.4643 | 1.9929 | ±3.9858 | +1.237 | 0.2163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **177**, R² = **0.2574**, Adj R² = **0.2079**, F-statistic = **5.20** (p = **5.30e-07**), Residual SE = **8.026** on **165** df, AIC = **1251.1**, BIC = **1289.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.2904** | 7.0019 | ±14.0037 | **+10.182** | **2.39e-24** | *** |
| **Education: graduate level (vs college)** | **-3.4387** | 1.3958 | ±2.7915 | **-2.464** | **0.0138** | * |
| Education: high school or below (vs college) | -3.9271 | 2.0345 | ±4.0690 | -1.930 | 0.0536 | . |
| Site: UCSD (vs UAB) | -1.6025 | 1.7053 | ±3.4105 | -0.940 | 0.3474 |  |
| Site: UW (vs UAB) | -0.9327 | 1.6449 | ±3.2899 | -0.567 | 0.5707 |  |
| **Age (years)** | **-0.2747** | 0.0747 | ±0.1493 | **-3.680** | **2.33e-04** | *** |
| BMI (kg/m2) | +0.1816 | 0.0984 | ±0.1968 | +1.846 | 0.0648 | . |
| Hypertension | +1.4163 | 1.5046 | ±3.0091 | +0.941 | 0.3465 |  |
| High cholesterol | +0.3417 | 1.3049 | ±2.6098 | +0.262 | 0.7935 |  |
| **Kidney disease** | **+6.7945** | 1.7934 | ±3.5867 | **+3.789** | **1.51e-04** | *** |
| Circulatory disease | -0.5210 | 1.8397 | ±3.6793 | -0.283 | 0.7770 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0427 | 0.0423 | ±0.0846 | +1.010 | 0.3125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.19e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4244** | 6.1574 | ±12.3149 | **+12.412** | **2.26e-35** | *** |
| **Education: graduate level (vs college)** | **-3.4497** | 1.3889 | ±2.7778 | **-2.484** | **0.0130** | * |
| **Education: high school or below (vs college)** | **-4.0291** | 2.0195 | ±4.0391 | **-1.995** | **0.0460** | * |
| Site: UCSD (vs UAB) | -1.4813 | 1.7131 | ±3.4262 | -0.865 | 0.3872 |  |
| Site: UW (vs UAB) | -0.8613 | 1.6962 | ±3.3924 | -0.508 | 0.6116 |  |
| **Age (years)** | **-0.2795** | 0.0759 | ±0.1518 | **-3.683** | **2.30e-04** | *** |
| BMI (kg/m2) | +0.1894 | 0.0967 | ±0.1933 | +1.960 | 0.0500 | . |
| Hypertension | +1.4769 | 1.5343 | ±3.0686 | +0.963 | 0.3358 |  |
| High cholesterol | +0.3761 | 1.2961 | ±2.5923 | +0.290 | 0.7717 |  |
| **Kidney disease** | **+6.7561** | 1.8265 | ±3.6529 | **+3.699** | **2.16e-04** | *** |
| Circulatory disease | -0.3327 | 1.8595 | ±3.7190 | -0.179 | 0.8580 |  |
| Glucose SD, pooled (mg/dL) | +0.0079 | 0.1316 | ±0.2632 | +0.060 | 0.9524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.08** (p = **8.15e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2768** | 6.0625 | ±12.1250 | **+12.582** | **2.66e-36** | *** |
| **Education: graduate level (vs college)** | **-3.4535** | 1.3878 | ±2.7757 | **-2.488** | **0.0128** | * |
| **Education: high school or below (vs college)** | **-4.0397** | 2.0223 | ±4.0446 | **-1.998** | **0.0458** | * |
| Site: UCSD (vs UAB) | -1.4873 | 1.7096 | ±3.4193 | -0.870 | 0.3843 |  |
| Site: UW (vs UAB) | -0.8580 | 1.6784 | ±3.3567 | -0.511 | 0.6092 |  |
| **Age (years)** | **-0.2798** | 0.0761 | ±0.1522 | **-3.675** | **2.37e-04** | *** |
| **BMI (kg/m2)** | **+0.1896** | 0.0966 | ±0.1932 | **+1.963** | **0.0496** | * |
| Hypertension | +1.4549 | 1.5268 | ±3.0536 | +0.953 | 0.3406 |  |
| High cholesterol | +0.3813 | 1.2974 | ±2.5947 | +0.294 | 0.7688 |  |
| **Kidney disease** | **+6.7495** | 1.8213 | ±3.6425 | **+3.706** | **2.11e-04** | *** |
| Circulatory disease | -0.3381 | 1.8560 | ±3.7120 | -0.182 | 0.8554 |  |
| Avg. daily SD (mg/dL) | +0.0171 | 0.1333 | ±0.2667 | +0.129 | 0.8977 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **177**, R² = **0.2548**, Adj R² = **0.2051**, F-statistic = **5.13** (p = **6.78e-07**), Residual SE = **8.040** on **165** df, AIC = **1251.8**, BIC = **1289.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.7158** | 6.3584 | ±12.7167 | **+12.380** | **3.36e-35** | *** |
| **Education: graduate level (vs college)** | **-3.3789** | 1.3864 | ±2.7729 | **-2.437** | **0.0148** | * |
| Education: high school or below (vs college) | -3.6988 | 2.0445 | ±4.0890 | -1.809 | 0.0704 | . |
| Site: UCSD (vs UAB) | -1.5635 | 1.7166 | ±3.4331 | -0.911 | 0.3624 |  |
| Site: UW (vs UAB) | -1.0457 | 1.6956 | ±3.3913 | -0.617 | 0.5374 |  |
| **Age (years)** | **-0.2764** | 0.0760 | ±0.1520 | **-3.636** | **2.77e-04** | *** |
| BMI (kg/m2) | +0.1860 | 0.0965 | ±0.1930 | +1.928 | 0.0539 | . |
| Hypertension | +1.6569 | 1.5416 | ±3.0831 | +1.075 | 0.2825 |  |
| High cholesterol | +0.3282 | 1.2922 | ±2.5843 | +0.254 | 0.7995 |  |
| **Kidney disease** | **+6.9283** | 1.8117 | ±3.6233 | **+3.824** | **1.31e-04** | *** |
| Circulatory disease | -0.2699 | 1.8736 | ±3.7473 | -0.144 | 0.8855 |  |
| CV (%) | -0.1351 | 0.1870 | ±0.3740 | -0.722 | 0.4700 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **177**, R² = **0.2531**, Adj R² = **0.2034**, F-statistic = **5.08** (p = **7.91e-07**), Residual SE = **8.049** on **165** df, AIC = **1252.1**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5118** | 7.3131 | ±14.6261 | **+10.326** | **5.40e-25** | *** |
| **Education: graduate level (vs college)** | **-3.4252** | 1.3897 | ±2.7794 | **-2.465** | **0.0137** | * |
| Education: high school or below (vs college) | -3.8906 | 2.0431 | ±4.0861 | -1.904 | 0.0569 | . |
| Site: UCSD (vs UAB) | -1.5083 | 1.7132 | ±3.4265 | -0.880 | 0.3786 |  |
| Site: UW (vs UAB) | -0.9391 | 1.6868 | ±3.3737 | -0.557 | 0.5777 |  |
| **Age (years)** | **-0.2779** | 0.0763 | ±0.1527 | **-3.641** | **2.72e-04** | *** |
| BMI (kg/m2) | +0.1891 | 0.0969 | ±0.1937 | +1.952 | 0.0510 | . |
| Hypertension | +1.5666 | 1.5330 | ±3.0659 | +1.022 | 0.3068 |  |
| High cholesterol | +0.3642 | 1.2970 | ±2.5941 | +0.281 | 0.7789 |  |
| **Kidney disease** | **+6.8363** | 1.8183 | ±3.6366 | **+3.760** | **1.70e-04** | *** |
| Circulatory disease | -0.3106 | 1.8713 | ±3.7425 | -0.166 | 0.8682 |  |
| Mean / SD ratio | +0.1544 | 0.4956 | ±0.9912 | +0.312 | 0.7553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.19e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.3545** | 7.2285 | ±14.4569 | **+10.563** | **4.42e-26** | *** |
| **Education: graduate level (vs college)** | **-3.4427** | 1.3908 | ±2.7816 | **-2.475** | **0.0133** | * |
| Education: high school or below (vs college) | -3.9912 | 2.0417 | ±4.0834 | -1.955 | 0.0506 | . |
| Site: UCSD (vs UAB) | -1.4824 | 1.7064 | ±3.4128 | -0.869 | 0.3850 |  |
| Site: UW (vs UAB) | -0.8828 | 1.6738 | ±3.3476 | -0.527 | 0.5979 |  |
| **Age (years)** | **-0.2790** | 0.0769 | ±0.1537 | **-3.630** | **2.84e-04** | *** |
| BMI (kg/m2) | +0.1893 | 0.0969 | ±0.1939 | +1.953 | 0.0508 | . |
| Hypertension | +1.5116 | 1.5294 | ±3.0588 | +0.988 | 0.3230 |  |
| High cholesterol | +0.3719 | 1.3004 | ±2.6008 | +0.286 | 0.7749 |  |
| **Kidney disease** | **+6.7806** | 1.8209 | ±3.6418 | **+3.724** | **1.96e-04** | *** |
| Circulatory disease | -0.3253 | 1.8781 | ±3.7562 | -0.173 | 0.8625 |  |
| Avg. daily mean/SD | +0.0269 | 0.3884 | ±0.7768 | +0.069 | 0.9449 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **177**, R² = **0.2592**, Adj R² = **0.2098**, F-statistic = **5.25** (p = **4.47e-07**), Residual SE = **8.016** on **165** df, AIC = **1250.7**, BIC = **1288.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.9142** | 6.2660 | ±12.5321 | **+11.636** | **2.69e-31** | *** |
| **Education: graduate level (vs college)** | **-3.4778** | 1.3925 | ±2.7851 | **-2.497** | **0.0125** | * |
| **Education: high school or below (vs college)** | **-4.1668** | 1.9981 | ±3.9961 | **-2.085** | **0.0370** | * |
| Site: UCSD (vs UAB) | -1.5629 | 1.7027 | ±3.4055 | -0.918 | 0.3587 |  |
| Site: UW (vs UAB) | -0.8034 | 1.6332 | ±3.2665 | -0.492 | 0.6228 |  |
| **Age (years)** | **-0.2794** | 0.0748 | ±0.1496 | **-3.734** | **1.88e-04** | *** |
| BMI (kg/m2) | +0.1827 | 0.0970 | ±0.1940 | +1.883 | 0.0597 | . |
| Hypertension | +1.4257 | 1.5077 | ±3.0155 | +0.946 | 0.3444 |  |
| High cholesterol | +0.2943 | 1.3073 | ±2.6147 | +0.225 | 0.8219 |  |
| **Kidney disease** | **+6.8189** | 1.8246 | ±3.6493 | **+3.737** | **1.86e-04** | *** |
| Circulatory disease | -0.3191 | 1.8332 | ±3.6664 | -0.174 | 0.8618 |  |
| MAG (mg/dL/h) | +0.1099 | 0.0909 | ±0.1819 | +1.208 | 0.2271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **177**, R² = **0.2541**, Adj R² = **0.2044**, F-statistic = **5.11** (p = **7.21e-07**), Residual SE = **8.043** on **165** df, AIC = **1251.9**, BIC = **1290.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.8283** | 6.0299 | ±12.0597 | **+12.410** | **2.32e-35** | *** |
| **Education: graduate level (vs college)** | **-3.4637** | 1.3890 | ±2.7781 | **-2.494** | **0.0126** | * |
| **Education: high school or below (vs college)** | **-4.1269** | 2.0357 | ±4.0714 | **-2.027** | **0.0426** | * |
| Site: UCSD (vs UAB) | -1.4668 | 1.7133 | ±3.4266 | -0.856 | 0.3919 |  |
| Site: UW (vs UAB) | -0.8017 | 1.6776 | ±3.3552 | -0.478 | 0.6327 |  |
| **Age (years)** | **-0.2815** | 0.0768 | ±0.1536 | **-3.666** | **2.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1928** | 0.0963 | ±0.1927 | **+2.001** | **0.0453** | * |
| Hypertension | +1.3794 | 1.5094 | ±3.0189 | +0.914 | 0.3608 |  |
| High cholesterol | +0.3937 | 1.3028 | ±2.6056 | +0.302 | 0.7625 |  |
| **Kidney disease** | **+6.7072** | 1.8232 | ±3.6464 | **+3.679** | **2.34e-04** | *** |
| Circulatory disease | -0.3724 | 1.8380 | ±3.6760 | -0.203 | 0.8394 |  |
| Avg. daily range (mg/dL) | +0.0190 | 0.0351 | ±0.0701 | +0.543 | 0.5871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **177**, R² = **0.2537**, Adj R² = **0.2040**, F-statistic = **5.10** (p = **7.50e-07**), Residual SE = **8.045** on **165** df, AIC = **1252.0**, BIC = **1290.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.1966** | 6.1224 | ±12.2447 | **+12.609** | **1.88e-36** | *** |
| **Education: graduate level (vs college)** | **-3.4226** | 1.4013 | ±2.8027 | **-2.442** | **0.0146** | * |
| Education: high school or below (vs college) | -3.8201 | 1.9799 | ±3.9598 | -1.929 | 0.0537 | . |
| Site: UCSD (vs UAB) | -1.5923 | 1.7176 | ±3.4352 | -0.927 | 0.3539 |  |
| Site: UW (vs UAB) | -1.0072 | 1.6864 | ±3.3727 | -0.597 | 0.5503 |  |
| **Age (years)** | **-0.2772** | 0.0756 | ±0.1511 | **-3.668** | **2.44e-04** | *** |
| **BMI (kg/m2)** | **+0.1901** | 0.0967 | ±0.1934 | **+1.966** | **0.0494** | * |
| Hypertension | +1.4631 | 1.5129 | ±3.0259 | +0.967 | 0.3335 |  |
| High cholesterol | +0.3884 | 1.3059 | ±2.6117 | +0.297 | 0.7661 |  |
| **Kidney disease** | **+6.9388** | 1.8591 | ±3.7181 | **+3.732** | **1.90e-04** | *** |
| Circulatory disease | -0.1923 | 1.9013 | ±3.8025 | -0.101 | 0.9195 |  |
| SD of daily means (mg/dL) | -0.1155 | 0.2648 | ±0.5297 | -0.436 | 0.6629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.08** (p = **8.16e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.1210** | 15.8690 | ±31.7380 | **+4.734** | **2.20e-06** | *** |
| **Education: graduate level (vs college)** | **-3.4375** | 1.4035 | ±2.8069 | **-2.449** | **0.0143** | * |
| **Education: high school or below (vs college)** | **-4.0002** | 2.0232 | ±4.0465 | **-1.977** | **0.0480** | * |
| Site: UCSD (vs UAB) | -1.4860 | 1.7109 | ±3.4218 | -0.869 | 0.3851 |  |
| Site: UW (vs UAB) | -0.8772 | 1.6682 | ±3.3364 | -0.526 | 0.5990 |  |
| **Age (years)** | **-0.2787** | 0.0754 | ±0.1508 | **-3.695** | **2.20e-04** | *** |
| BMI (kg/m2) | +0.1900 | 0.0978 | ±0.1955 | +1.944 | 0.0519 | . |
| Hypertension | +1.4981 | 1.5166 | ±3.0331 | +0.988 | 0.3232 |  |
| High cholesterol | +0.3678 | 1.2972 | ±2.5944 | +0.284 | 0.7768 |  |
| **Kidney disease** | **+6.7989** | 1.8524 | ±3.7048 | **+3.670** | **2.42e-04** | *** |
| Circulatory disease | -0.3031 | 1.8942 | ±3.7884 | -0.160 | 0.8729 |  |
| Time in range 70-180, pooled (%) | +0.0144 | 0.1431 | ±0.2863 | +0.100 | 0.9200 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2029**, F-statistic = **5.07** (p = **8.20e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.9252** | 16.3474 | ±32.6947 | **+4.644** | **3.41e-06** | *** |
| **Education: graduate level (vs college)** | **-3.4429** | 1.4037 | ±2.8074 | **-2.453** | **0.0142** | * |
| **Education: high school or below (vs college)** | **-4.0078** | 2.0217 | ±4.0433 | **-1.982** | **0.0474** | * |
| Site: UCSD (vs UAB) | -1.4848 | 1.7104 | ±3.4209 | -0.868 | 0.3853 |  |
| Site: UW (vs UAB) | -0.8734 | 1.6639 | ±3.3278 | -0.525 | 0.5997 |  |
| **Age (years)** | **-0.2790** | 0.0754 | ±0.1509 | **-3.699** | **2.16e-04** | *** |
| BMI (kg/m2) | +0.1896 | 0.0976 | ±0.1952 | +1.943 | 0.0520 | . |
| Hypertension | +1.4951 | 1.5143 | ±3.0285 | +0.987 | 0.3235 |  |
| High cholesterol | +0.3706 | 1.2976 | ±2.5952 | +0.286 | 0.7752 |  |
| **Kidney disease** | **+6.7836** | 1.8553 | ±3.7105 | **+3.656** | **2.56e-04** | *** |
| Circulatory disease | -0.3144 | 1.8973 | ±3.7945 | -0.166 | 0.8684 |  |
| Avg. daily time in range 70-180 (%) | +0.0064 | 0.1486 | ±0.2972 | +0.043 | 0.9655 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **177**, R² = **0.2746**, Adj R² = **0.2263**, F-statistic = **5.68** (p = **1.01e-07**), Residual SE = **7.932** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.6936** | 5.9855 | ±11.9709 | **+12.646** | **1.17e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0733** | 1.4021 | ±2.8043 | **-2.192** | **0.0284** | * |
| Education: high school or below (vs college) | -3.4004 | 1.9598 | ±3.9196 | -1.735 | 0.0827 | . |
| Site: UCSD (vs UAB) | -1.6845 | 1.6790 | ±3.3579 | -1.003 | 0.3157 |  |
| Site: UW (vs UAB) | -0.9896 | 1.6343 | ±3.2686 | -0.606 | 0.5448 |  |
| **Age (years)** | **-0.2557** | 0.0748 | ±0.1496 | **-3.418** | **6.32e-04** | *** |
| BMI (kg/m2) | +0.1829 | 0.0955 | ±0.1911 | +1.915 | 0.0555 | . |
| Hypertension | +1.4630 | 1.4575 | ±2.9151 | +1.004 | 0.3155 |  |
| High cholesterol | +0.5646 | 1.2879 | ±2.5758 | +0.438 | 0.6611 |  |
| **Kidney disease** | **+6.5899** | 1.8155 | ±3.6310 | **+3.630** | **2.84e-04** | *** |
| Circulatory disease | -0.0333 | 1.8570 | ±3.7139 | -0.018 | 0.9857 |  |
| **Time 54-69, pooled (%)** | **-4.5166** | 1.6904 | ±3.3807 | **-2.672** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **177**, R² = **0.2744**, Adj R² = **0.2260**, F-statistic = **5.67** (p = **1.03e-07**), Residual SE = **7.933** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5279** | 6.0035 | ±12.0070 | **+12.581** | **2.70e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0993** | 1.4051 | ±2.8102 | **-2.206** | **0.0274** | * |
| Education: high school or below (vs college) | -3.4739 | 1.9450 | ±3.8899 | -1.786 | 0.0741 | . |
| Site: UCSD (vs UAB) | -1.5488 | 1.6817 | ±3.3634 | -0.921 | 0.3571 |  |
| Site: UW (vs UAB) | -0.9024 | 1.6361 | ±3.2722 | -0.552 | 0.5812 |  |
| **Age (years)** | **-0.2547** | 0.0750 | ±0.1500 | **-3.395** | **6.85e-04** | *** |
| BMI (kg/m2) | +0.1824 | 0.0958 | ±0.1916 | +1.904 | 0.0569 | . |
| Hypertension | +1.5125 | 1.4579 | ±2.9157 | +1.037 | 0.2995 |  |
| High cholesterol | +0.5565 | 1.2891 | ±2.5782 | +0.432 | 0.6659 |  |
| **Kidney disease** | **+6.4776** | 1.8276 | ±3.6552 | **+3.544** | **3.94e-04** | *** |
| Circulatory disease | -0.1033 | 1.8432 | ±3.6865 | -0.056 | 0.9553 |  |
| **Avg. daily time 54-69 (%)** | **-4.3124** | 1.8551 | ±3.7103 | **-2.325** | **0.0201** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **177**, R² = **0.2746**, Adj R² = **0.2263**, F-statistic = **5.68** (p = **1.01e-07**), Residual SE = **7.932** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.6936** | 5.9855 | ±11.9709 | **+12.646** | **1.17e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0733** | 1.4021 | ±2.8043 | **-2.192** | **0.0284** | * |
| Education: high school or below (vs college) | -3.4004 | 1.9598 | ±3.9196 | -1.735 | 0.0827 | . |
| Site: UCSD (vs UAB) | -1.6845 | 1.6790 | ±3.3579 | -1.003 | 0.3157 |  |
| Site: UW (vs UAB) | -0.9896 | 1.6343 | ±3.2686 | -0.606 | 0.5448 |  |
| **Age (years)** | **-0.2557** | 0.0748 | ±0.1496 | **-3.418** | **6.32e-04** | *** |
| BMI (kg/m2) | +0.1829 | 0.0955 | ±0.1911 | +1.915 | 0.0555 | . |
| Hypertension | +1.4630 | 1.4575 | ±2.9151 | +1.004 | 0.3155 |  |
| High cholesterol | +0.5646 | 1.2879 | ±2.5758 | +0.438 | 0.6611 |  |
| **Kidney disease** | **+6.5899** | 1.8155 | ±3.6310 | **+3.630** | **2.84e-04** | *** |
| Circulatory disease | -0.0333 | 1.8570 | ±3.7139 | -0.018 | 0.9857 |  |
| **Time < 70 (%)** | **-4.5166** | 1.6904 | ±3.3807 | **-2.672** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **177**, R² = **0.2744**, Adj R² = **0.2260**, F-statistic = **5.67** (p = **1.03e-07**), Residual SE = **7.933** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5279** | 6.0035 | ±12.0070 | **+12.581** | **2.70e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0993** | 1.4051 | ±2.8102 | **-2.206** | **0.0274** | * |
| Education: high school or below (vs college) | -3.4739 | 1.9450 | ±3.8899 | -1.786 | 0.0741 | . |
| Site: UCSD (vs UAB) | -1.5488 | 1.6817 | ±3.3634 | -0.921 | 0.3571 |  |
| Site: UW (vs UAB) | -0.9024 | 1.6361 | ±3.2722 | -0.552 | 0.5812 |  |
| **Age (years)** | **-0.2547** | 0.0750 | ±0.1500 | **-3.395** | **6.85e-04** | *** |
| BMI (kg/m2) | +0.1824 | 0.0958 | ±0.1916 | +1.904 | 0.0569 | . |
| Hypertension | +1.5125 | 1.4579 | ±2.9157 | +1.037 | 0.2995 |  |
| High cholesterol | +0.5565 | 1.2891 | ±2.5782 | +0.432 | 0.6659 |  |
| **Kidney disease** | **+6.4776** | 1.8276 | ±3.6552 | **+3.544** | **3.94e-04** | *** |
| Circulatory disease | -0.1033 | 1.8432 | ±3.6865 | -0.056 | 0.9553 |  |
| **Avg. daily time < 70 (%)** | **-4.3124** | 1.8551 | ±3.7103 | **-2.325** | **0.0201** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2029**, F-statistic = **5.07** (p = **8.20e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5789** | 6.0043 | ±12.0086 | **+12.754** | **2.96e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4482** | 1.4027 | ±2.8054 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **-4.0140** | 2.0230 | ±4.0460 | **-1.984** | **0.0472** | * |
| Site: UCSD (vs UAB) | -1.4840 | 1.7112 | ±3.4224 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6655 | ±3.3310 | -0.523 | 0.6008 |  |
| **Age (years)** | **-0.2795** | 0.0754 | ±0.1509 | **-3.705** | **2.11e-04** | *** |
| BMI (kg/m2) | +0.1892 | 0.0978 | ±0.1956 | +1.935 | 0.0530 | . |
| Hypertension | +1.4889 | 1.5161 | ±3.0322 | +0.982 | 0.3261 |  |
| High cholesterol | +0.3747 | 1.2968 | ±2.5935 | +0.289 | 0.7726 |  |
| **Kidney disease** | **+6.7626** | 1.8534 | ±3.7067 | **+3.649** | **2.63e-04** | *** |
| Circulatory disease | -0.3299 | 1.8898 | ±3.7795 | -0.175 | 0.8614 |  |
| Time 181-250, pooled (%) | +0.0044 | 0.1429 | ±0.2859 | +0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.17e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5886** | 6.0044 | ±12.0088 | **+12.755** | **2.91e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4516** | 1.4028 | ±2.8056 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **-4.0169** | 2.0219 | ±4.0438 | **-1.987** | **0.0470** | * |
| Site: UCSD (vs UAB) | -1.4834 | 1.7105 | ±3.4211 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6618 | ±3.3235 | -0.524 | 0.6000 |  |
| **Age (years)** | **-0.2800** | 0.0754 | ±0.1509 | **-3.711** | **2.06e-04** | *** |
| BMI (kg/m2) | +0.1889 | 0.0976 | ±0.1952 | +1.935 | 0.0530 | . |
| Hypertension | +1.4824 | 1.5136 | ±3.0271 | +0.979 | 0.3274 |  |
| High cholesterol | +0.3786 | 1.2970 | ±2.5940 | +0.292 | 0.7704 |  |
| **Kidney disease** | **+6.7437** | 1.8566 | ±3.7131 | **+3.632** | **2.81e-04** | *** |
| Circulatory disease | -0.3436 | 1.8928 | ±3.7856 | -0.182 | 0.8560 |  |
| Avg. daily time 181-250 (%) | +0.0139 | 0.1473 | ±0.2946 | +0.094 | 0.9251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2029**, F-statistic = **5.07** (p = **8.20e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5789** | 6.0043 | ±12.0086 | **+12.754** | **2.96e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4482** | 1.4027 | ±2.8054 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **-4.0140** | 2.0230 | ±4.0460 | **-1.984** | **0.0472** | * |
| Site: UCSD (vs UAB) | -1.4840 | 1.7112 | ±3.4224 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6655 | ±3.3310 | -0.523 | 0.6008 |  |
| **Age (years)** | **-0.2795** | 0.0754 | ±0.1509 | **-3.705** | **2.11e-04** | *** |
| BMI (kg/m2) | +0.1892 | 0.0978 | ±0.1956 | +1.935 | 0.0530 | . |
| Hypertension | +1.4889 | 1.5161 | ±3.0322 | +0.982 | 0.3261 |  |
| High cholesterol | +0.3747 | 1.2968 | ±2.5935 | +0.289 | 0.7726 |  |
| **Kidney disease** | **+6.7626** | 1.8534 | ±3.7067 | **+3.649** | **2.63e-04** | *** |
| Circulatory disease | -0.3299 | 1.8898 | ±3.7795 | -0.175 | 0.8614 |  |
| Time > 180 (%) | +0.0044 | 0.1429 | ±0.2859 | +0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.17e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5886** | 6.0044 | ±12.0088 | **+12.755** | **2.91e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4516** | 1.4028 | ±2.8056 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **-4.0169** | 2.0219 | ±4.0438 | **-1.987** | **0.0470** | * |
| Site: UCSD (vs UAB) | -1.4834 | 1.7105 | ±3.4211 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6618 | ±3.3235 | -0.524 | 0.6000 |  |
| **Age (years)** | **-0.2800** | 0.0754 | ±0.1509 | **-3.711** | **2.06e-04** | *** |
| BMI (kg/m2) | +0.1889 | 0.0976 | ±0.1952 | +1.935 | 0.0530 | . |
| Hypertension | +1.4824 | 1.5136 | ±3.0271 | +0.979 | 0.3274 |  |
| High cholesterol | +0.3786 | 1.2970 | ±2.5940 | +0.292 | 0.7704 |  |
| **Kidney disease** | **+6.7437** | 1.8566 | ±3.7131 | **+3.632** | **2.81e-04** | *** |
| Circulatory disease | -0.3436 | 1.8928 | ±3.7856 | -0.182 | 0.8560 |  |
| Avg. daily time > 180 (%) | +0.0139 | 0.1473 | ±0.2946 | +0.094 | 0.9251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2531**, Adj R² = **0.2033**, F-statistic = **5.08** (p = **7.96e-07**), Residual SE = **8.049** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4930** | 6.0317 | ±12.0633 | **+12.682** | **7.45e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4380** | 1.3941 | ±2.7882 | **-2.466** | **0.0137** | * |
| **Education: high school or below (vs college)** | **-3.9545** | 2.0089 | ±4.0177 | **-1.969** | **0.0490** | * |
| Site: UCSD (vs UAB) | -1.5247 | 1.7155 | ±3.4309 | -0.889 | 0.3741 |  |
| Site: UW (vs UAB) | -0.9096 | 1.6512 | ±3.3025 | -0.551 | 0.5817 |  |
| **Age (years)** | **-0.2781** | 0.0755 | ±0.1510 | **-3.684** | **2.30e-04** | *** |
| BMI (kg/m2) | +0.1926 | 0.0991 | ±0.1981 | +1.945 | 0.0518 | . |
| Hypertension | +1.4685 | 1.5204 | ±3.0408 | +0.966 | 0.3341 |  |
| High cholesterol | +0.3709 | 1.2962 | ±2.5923 | +0.286 | 0.7748 |  |
| **Kidney disease** | **+6.8553** | 1.8806 | ±3.7613 | **+3.645** | **2.67e-04** | *** |
| Circulatory disease | -0.2620 | 1.9129 | ±3.8259 | -0.137 | 0.8911 |  |
| Nocturnal time > 180 (%) | -0.0338 | 0.1017 | ±0.2035 | -0.332 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 178; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **178**, R² = **0.1152**, Adj R² = **0.0623**, F-statistic = **2.18** (p = **0.0216**), Residual SE = **71.380** on **167** df, AIC = **2035.2**, BIC = **2070.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+366.0457** | 48.0780 | ±96.1560 | **+7.614** | **2.67e-14** | *** |
| Education: graduate level (vs college) | +17.1206 | 11.5506 | ±23.1013 | +1.482 | 0.1383 |  |
| Education: high school or below (vs college) | -2.1903 | 17.9742 | ±35.9485 | -0.122 | 0.9030 |  |
| **Site: UCSD (vs UAB)** | **-28.5363** | 13.8605 | ±27.7210 | **-2.059** | **0.0395** | * |
| Site: UW (vs UAB) | -5.0337 | 13.9517 | ±27.9033 | -0.361 | 0.7183 |  |
| Age (years) | +1.1124 | 0.6107 | ±1.2214 | +1.822 | 0.0685 | . |
| BMI (kg/m2) | -1.4447 | 0.7412 | ±1.4823 | -1.949 | 0.0513 | . |
| **Hypertension** | **-34.6500** | 13.5104 | ±27.0208 | **-2.565** | **0.0103** | * |
| High cholesterol | -3.5576 | 11.2899 | ±22.5798 | -0.315 | 0.7527 |  |
| Kidney disease | +1.6589 | 20.0899 | ±40.1797 | +0.083 | 0.9342 |  |
| Circulatory disease | -0.7041 | 14.1888 | ±28.3776 | -0.050 | 0.9604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **178**, R² = **0.1170**, Adj R² = **0.0584**, F-statistic = **2.00** (p = **0.0314**), Residual SE = **71.525** on **166** df, AIC = **2036.9**, BIC = **2075.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.5859** | 72.7463 | ±145.4926 | **+5.479** | **4.27e-08** | *** |
| Education: graduate level (vs college) | +16.7821 | 11.7041 | ±23.4083 | +1.434 | 0.1516 |  |
| Education: high school or below (vs college) | -1.6868 | 18.1628 | ±36.3256 | -0.093 | 0.9260 |  |
| **Site: UCSD (vs UAB)** | **-28.5733** | 13.8728 | ±27.7456 | **-2.060** | **0.0394** | * |
| Site: UW (vs UAB) | -5.0585 | 14.0189 | ±28.0377 | -0.361 | 0.7182 |  |
| Age (years) | +1.1187 | 0.6154 | ±1.2308 | +1.818 | 0.0691 | . |
| BMI (kg/m2) | -1.3543 | 0.7420 | ±1.4840 | -1.825 | 0.0680 | . |
| **Hypertension** | **-33.8936** | 13.4774 | ±26.9548 | **-2.515** | **0.0119** | * |
| High cholesterol | -2.8135 | 11.5144 | ±23.0288 | -0.244 | 0.8070 |  |
| Kidney disease | +0.2389 | 20.1334 | ±40.2668 | +0.012 | 0.9905 |  |
| Circulatory disease | +0.2983 | 14.4453 | ±28.8906 | +0.021 | 0.9835 |  |
| HbA1c (%) | -6.1513 | 10.1664 | ±20.3329 | -0.605 | 0.5451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **178**, R² = **0.1290**, Adj R² = **0.0713**, F-statistic = **2.23** (p = **0.0148**), Residual SE = **71.036** on **166** df, AIC = **2034.4**, BIC = **2072.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+445.6348** | 77.3786 | ±154.7572 | **+5.759** | **8.45e-09** | *** |
| Education: graduate level (vs college) | +16.6110 | 11.6067 | ±23.2133 | +1.431 | 0.1524 |  |
| Education: high school or below (vs college) | -3.8545 | 18.0396 | ±36.0792 | -0.214 | 0.8308 |  |
| **Site: UCSD (vs UAB)** | **-27.9128** | 13.7052 | ±27.4104 | **-2.037** | **0.0417** | * |
| Site: UW (vs UAB) | -4.5433 | 14.0077 | ±28.0155 | -0.324 | 0.7457 |  |
| Age (years) | +1.1161 | 0.6054 | ±1.2108 | +1.844 | 0.0652 | . |
| BMI (kg/m2) | -1.3194 | 0.7454 | ±1.4908 | -1.770 | 0.0767 | . |
| **Hypertension** | **-33.5783** | 13.0756 | ±26.1511 | **-2.568** | **0.0102** | * |
| High cholesterol | -3.8208 | 11.3663 | ±22.7325 | -0.336 | 0.7368 |  |
| Kidney disease | +5.1317 | 20.4478 | ±40.8956 | +0.251 | 0.8018 |  |
| Circulatory disease | +1.0676 | 14.4101 | ±28.8201 | +0.074 | 0.9409 |  |
| Mean glucose (mg/dL) | -0.6717 | 0.4969 | ±0.9938 | -1.352 | 0.1764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **178**, R² = **0.1290**, Adj R² = **0.0713**, F-statistic = **2.23** (p = **0.0148**), Residual SE = **71.036** on **166** df, AIC = **2034.4**, BIC = **2072.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+538.5838** | 137.9447 | ±275.8894 | **+3.904** | **9.45e-05** | *** |
| Education: graduate level (vs college) | +16.6110 | 11.6067 | ±23.2133 | +1.431 | 0.1524 |  |
| Education: high school or below (vs college) | -3.8545 | 18.0396 | ±36.0792 | -0.214 | 0.8308 |  |
| **Site: UCSD (vs UAB)** | **-27.9128** | 13.7052 | ±27.4104 | **-2.037** | **0.0417** | * |
| Site: UW (vs UAB) | -4.5433 | 14.0077 | ±28.0155 | -0.324 | 0.7457 |  |
| Age (years) | +1.1161 | 0.6054 | ±1.2108 | +1.844 | 0.0652 | . |
| BMI (kg/m2) | -1.3194 | 0.7454 | ±1.4908 | -1.770 | 0.0767 | . |
| **Hypertension** | **-33.5783** | 13.0756 | ±26.1511 | **-2.568** | **0.0102** | * |
| High cholesterol | -3.8208 | 11.3663 | ±22.7325 | -0.336 | 0.7368 |  |
| Kidney disease | +5.1317 | 20.4478 | ±40.8956 | +0.251 | 0.8018 |  |
| Circulatory disease | +1.0676 | 14.4101 | ±28.8201 | +0.074 | 0.9409 |  |
| GMI (%) | -28.0813 | 20.7728 | ±41.5456 | -1.352 | 0.1764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **178**, R² = **0.1258**, Adj R² = **0.0678**, F-statistic = **2.17** (p = **0.0182**), Residual SE = **71.168** on **166** df, AIC = **2035.1**, BIC = **2073.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+430.2091** | 75.4196 | ±150.8393 | **+5.704** | **1.17e-08** | *** |
| Education: graduate level (vs college) | +17.0670 | 11.5834 | ±23.1667 | +1.473 | 0.1406 |  |
| Education: high school or below (vs college) | -3.0559 | 17.9633 | ±35.9265 | -0.170 | 0.8649 |  |
| Site: UCSD (vs UAB) | -27.3152 | 13.9762 | ±27.9525 | -1.954 | 0.0507 | . |
| Site: UW (vs UAB) | -4.1620 | 13.9016 | ±27.8032 | -0.299 | 0.7646 |  |
| Age (years) | +1.0656 | 0.6052 | ±1.2103 | +1.761 | 0.0783 | . |
| BMI (kg/m2) | -1.3260 | 0.7471 | ±1.4941 | -1.775 | 0.0759 | . |
| **Hypertension** | **-33.6981** | 13.1356 | ±26.2712 | **-2.565** | **0.0103** | * |
| High cholesterol | -3.2666 | 11.3168 | ±22.6335 | -0.289 | 0.7728 |  |
| Kidney disease | +2.3340 | 20.4500 | ±40.9000 | +0.114 | 0.9091 |  |
| Circulatory disease | +1.5645 | 14.3407 | ±28.6814 | +0.109 | 0.9131 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.5295 | 0.4682 | ±0.9365 | -1.131 | 0.2581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1215**, Adj R² = **0.0633**, F-statistic = **2.09** (p = **0.0238**), Residual SE = **71.340** on **166** df, AIC = **2035.9**, BIC = **2074.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.2629** | 54.6889 | ±109.3778 | **+7.136** | **9.60e-13** | *** |
| Education: graduate level (vs college) | +17.7717 | 11.4782 | ±22.9563 | +1.548 | 0.1215 |  |
| Education: high school or below (vs college) | +0.9422 | 18.1632 | ±36.3264 | +0.052 | 0.9586 |  |
| **Site: UCSD (vs UAB)** | **-29.3034** | 13.7049 | ±27.4097 | **-2.138** | **0.0325** | * |
| Site: UW (vs UAB) | -7.0434 | 14.3579 | ±28.7159 | -0.491 | 0.6237 |  |
| Age (years) | +1.1550 | 0.6305 | ±1.2609 | +1.832 | 0.0669 | . |
| BMI (kg/m2) | -1.4455 | 0.7397 | ±1.4794 | -1.954 | 0.0507 | . |
| **Hypertension** | **-32.2901** | 12.9291 | ±25.8582 | **-2.497** | **0.0125** | * |
| High cholesterol | -4.2295 | 11.3843 | ±22.7687 | -0.372 | 0.7102 |  |
| Kidney disease | +4.9138 | 20.0051 | ±40.0102 | +0.246 | 0.8060 |  |
| Circulatory disease | +0.6297 | 14.1839 | ±28.3678 | +0.044 | 0.9646 |  |
| Glucose SD, pooled (mg/dL) | -1.3059 | 1.4402 | ±2.8804 | -0.907 | 0.3645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1261**, Adj R² = **0.0682**, F-statistic = **2.18** (p = **0.0179**), Residual SE = **71.155** on **166** df, AIC = **2035.0**, BIC = **2073.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7546** | 52.9981 | ±105.9961 | **+7.467** | **8.18e-14** | *** |
| Education: graduate level (vs college) | +17.9381 | 11.4614 | ±22.9229 | +1.565 | 0.1176 |  |
| Education: high school or below (vs college) | +0.9221 | 17.7289 | ±35.4578 | +0.052 | 0.9585 |  |
| **Site: UCSD (vs UAB)** | **-28.5918** | 13.7300 | ±27.4600 | **-2.082** | **0.0373** | * |
| Site: UW (vs UAB) | -6.6427 | 14.1446 | ±28.2891 | -0.470 | 0.6386 |  |
| Age (years) | +1.1709 | 0.6320 | ±1.2641 | +1.853 | 0.0639 | . |
| **BMI (kg/m2)** | **-1.4644** | 0.7368 | ±1.4736 | **-1.988** | **0.0469** | * |
| **Hypertension** | **-30.9404** | 12.8257 | ±25.6514 | **-2.412** | **0.0158** | * |
| High cholesterol | -4.6503 | 11.4146 | ±22.8293 | -0.407 | 0.6837 |  |
| Kidney disease | +5.0545 | 19.8336 | ±39.6671 | +0.255 | 0.7988 |  |
| Circulatory disease | +0.5784 | 14.1727 | ±28.3455 | +0.041 | 0.9674 |  |
| Avg. daily SD (mg/dL) | -1.7568 | 1.3722 | ±2.7444 | -1.280 | 0.2005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **178**, R² = **0.1160**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0332**), Residual SE = **71.562** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+376.8782** | 56.8539 | ±113.7079 | **+6.629** | **3.38e-11** | *** |
| Education: graduate level (vs college) | +17.4461 | 11.4541 | ±22.9082 | +1.523 | 0.1277 |  |
| Education: high school or below (vs college) | -0.5677 | 18.6057 | ±37.2114 | -0.031 | 0.9757 |  |
| **Site: UCSD (vs UAB)** | **-28.9558** | 13.7981 | ±27.5962 | **-2.099** | **0.0359** | * |
| Site: UW (vs UAB) | -5.9647 | 14.5028 | ±29.0056 | -0.411 | 0.6809 |  |
| Age (years) | +1.1308 | 0.6316 | ±1.2631 | +1.790 | 0.0734 | . |
| **BMI (kg/m2)** | **-1.4623** | 0.7430 | ±1.4859 | **-1.968** | **0.0490** | * |
| **Hypertension** | **-33.7977** | 13.2182 | ±26.4363 | **-2.557** | **0.0106** | * |
| High cholesterol | -3.7978 | 11.3781 | ±22.7562 | -0.334 | 0.7385 |  |
| Kidney disease | +2.5423 | 19.9342 | ±39.8684 | +0.128 | 0.8985 |  |
| Circulatory disease | -0.4352 | 14.2411 | ±28.4821 | -0.031 | 0.9756 |  |
| CV (%) | -0.6935 | 2.1160 | ±4.2319 | -0.328 | 0.7431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **178**, R² = **0.1158**, Adj R² = **0.0572**, F-statistic = **1.98** (p = **0.0336**), Residual SE = **71.571** on **166** df, AIC = **2037.1**, BIC = **2075.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+355.1251** | 66.6714 | ±133.3429 | **+5.326** | **1.00e-07** | *** |
| Education: graduate level (vs college) | +17.3172 | 11.5148 | ±23.0296 | +1.504 | 0.1326 |  |
| Education: high school or below (vs college) | -0.9803 | 18.3976 | ±36.7951 | -0.053 | 0.9575 |  |
| **Site: UCSD (vs UAB)** | **-28.7686** | 13.8052 | ±27.6104 | **-2.084** | **0.0372** | * |
| Site: UW (vs UAB) | -5.7562 | 14.5244 | ±29.0488 | -0.396 | 0.6919 |  |
| Age (years) | +1.1300 | 0.6409 | ±1.2818 | +1.763 | 0.0779 | . |
| BMI (kg/m2) | -1.4473 | 0.7438 | ±1.4876 | -1.946 | 0.0517 | . |
| **Hypertension** | **-33.8846** | 13.1456 | ±26.2911 | **-2.578** | **0.0099** | ** |
| High cholesterol | -3.6528 | 11.4103 | ±22.8206 | -0.320 | 0.7489 |  |
| Kidney disease | +2.3604 | 19.8900 | ±39.7800 | +0.119 | 0.9055 |  |
| Circulatory disease | -0.5590 | 14.2806 | ±28.5613 | -0.039 | 0.9688 |  |
| Mean / SD ratio | +1.5551 | 5.8688 | ±11.7376 | +0.265 | 0.7910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1189**, Adj R² = **0.0605**, F-statistic = **2.04** (p = **0.0279**), Residual SE = **71.446** on **166** df, AIC = **2036.5**, BIC = **2074.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+341.1126** | 62.5984 | ±125.1968 | **+5.449** | **5.06e-08** | *** |
| Education: graduate level (vs college) | +17.4570 | 11.5531 | ±23.1062 | +1.511 | 0.1308 |  |
| Education: high school or below (vs college) | +0.0293 | 17.9051 | ±35.8101 | +0.002 | 0.9987 |  |
| **Site: UCSD (vs UAB)** | **-28.2864** | 13.9358 | ±27.8716 | **-2.030** | **0.0424** | * |
| Site: UW (vs UAB) | -6.2538 | 14.2199 | ±28.4399 | -0.440 | 0.6601 |  |
| Age (years) | +1.1645 | 0.6452 | ±1.2904 | +1.805 | 0.0711 | . |
| **BMI (kg/m2)** | **-1.4544** | 0.7362 | ±1.4725 | **-1.975** | **0.0482** | * |
| **Hypertension** | **-32.3516** | 13.1848 | ±26.3695 | **-2.454** | **0.0141** | * |
| High cholesterol | -3.6907 | 11.3909 | ±22.7818 | -0.324 | 0.7459 |  |
| Kidney disease | +2.9167 | 19.8414 | ±39.6828 | +0.147 | 0.8831 |  |
| Circulatory disease | -0.8311 | 14.1872 | ±28.3744 | -0.059 | 0.9533 |  |
| Avg. daily mean/SD | +2.9707 | 4.0230 | ±8.0460 | +0.738 | 0.4603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **178**, R² = **0.1494**, Adj R² = **0.0930**, F-statistic = **2.65** (p = **0.0038**), Residual SE = **70.201** on **166** df, AIC = **2030.2**, BIC = **2068.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+432.1665** | 50.7666 | ±101.5331 | **+8.513** | **1.70e-17** | *** |
| Education: graduate level (vs college) | +17.9629 | 11.3525 | ±22.7050 | +1.582 | 0.1136 |  |
| Education: high school or below (vs college) | +1.9592 | 16.9729 | ±33.9459 | +0.115 | 0.9081 |  |
| **Site: UCSD (vs UAB)** | **-27.6463** | 13.5458 | ±27.0916 | **-2.041** | **0.0413** | * |
| Site: UW (vs UAB) | -6.8337 | 13.5464 | ±27.0928 | -0.504 | 0.6139 |  |
| Age (years) | +1.1454 | 0.6129 | ±1.2259 | +1.869 | 0.0617 | . |
| BMI (kg/m2) | -1.2926 | 0.7591 | ±1.5181 | -1.703 | 0.0886 | . |
| **Hypertension** | **-33.0148** | 12.9251 | ±25.8501 | **-2.554** | **0.0106** | * |
| High cholesterol | -2.4377 | 11.1407 | ±22.2815 | -0.219 | 0.8268 |  |
| Kidney disease | +0.7746 | 20.1008 | ±40.2015 | +0.039 | 0.9693 |  |
| Circulatory disease | -1.1343 | 14.1218 | ±28.2436 | -0.080 | 0.9360 |  |
| **MAG (mg/dL/h)** | **-2.0728** | 0.7655 | ±1.5310 | **-2.708** | **0.0068** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **178**, R² = **0.1204**, Adj R² = **0.0621**, F-statistic = **2.07** (p = **0.0255**), Residual SE = **71.387** on **166** df, AIC = **2036.2**, BIC = **2074.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.2750** | 57.2250 | ±114.4500 | **+6.855** | **7.13e-12** | *** |
| Education: graduate level (vs college) | +17.3832 | 11.5446 | ±23.0893 | +1.506 | 0.1321 |  |
| Education: high school or below (vs college) | -0.3645 | 17.7576 | ±35.5152 | -0.021 | 0.9836 |  |
| **Site: UCSD (vs UAB)** | **-28.9939** | 13.8008 | ±27.6015 | **-2.101** | **0.0357** | * |
| Site: UW (vs UAB) | -6.3804 | 14.2933 | ±28.5866 | -0.446 | 0.6553 |  |
| Age (years) | +1.1625 | 0.6355 | ±1.2709 | +1.829 | 0.0674 | . |
| **BMI (kg/m2)** | **-1.4888** | 0.7481 | ±1.4963 | **-1.990** | **0.0466** | * |
| **Hypertension** | **-32.8961** | 12.9212 | ±25.8425 | **-2.546** | **0.0109** | * |
| High cholesterol | -4.0519 | 11.4389 | ±22.8778 | -0.354 | 0.7232 |  |
| Kidney disease | +3.2055 | 19.8346 | ±39.6691 | +0.162 | 0.8716 |  |
| Circulatory disease | +0.0068 | 14.3282 | ±28.6563 | +0.000 | 0.9996 |  |
| Avg. daily range (mg/dL) | -0.2984 | 0.3462 | ±0.6924 | -0.862 | 0.3887 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **178**, R² = **0.1155**, Adj R² = **0.0569**, F-statistic = **1.97** (p = **0.0343**), Residual SE = **71.585** on **166** df, AIC = **2037.2**, BIC = **2075.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+363.7480** | 48.7389 | ±97.4779 | **+7.463** | **8.45e-14** | *** |
| Education: graduate level (vs college) | +17.0432 | 11.5485 | ±23.0971 | +1.476 | 0.1400 |  |
| Education: high school or below (vs college) | -2.9511 | 18.9958 | ±37.9915 | -0.155 | 0.8765 |  |
| **Site: UCSD (vs UAB)** | **-28.0811** | 13.8579 | ±27.7157 | **-2.026** | **0.0427** | * |
| Site: UW (vs UAB) | -4.4668 | 14.2415 | ±28.4830 | -0.314 | 0.7538 |  |
| Age (years) | +1.1034 | 0.6248 | ±1.2497 | +1.766 | 0.0774 | . |
| BMI (kg/m2) | -1.4516 | 0.7532 | ±1.5065 | -1.927 | 0.0540 | . |
| **Hypertension** | **-34.5342** | 13.7558 | ±27.5117 | **-2.511** | **0.0121** | * |
| High cholesterol | -3.6750 | 11.4672 | ±22.9345 | -0.320 | 0.7486 |  |
| Kidney disease | +1.0179 | 20.1165 | ±40.2329 | +0.051 | 0.9596 |  |
| Circulatory disease | -1.2164 | 14.5812 | ±29.1624 | -0.083 | 0.9335 |  |
| SD of daily means (mg/dL) | +0.4611 | 2.4929 | ±4.9859 | +0.185 | 0.8533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **178**, R² = **0.1158**, Adj R² = **0.0572**, F-statistic = **1.98** (p = **0.0336**), Residual SE = **71.572** on **166** df, AIC = **2037.1**, BIC = **2075.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+327.9608** | 122.5213 | ±245.0426 | **+2.677** | **0.0074** | ** |
| Education: graduate level (vs college) | +17.3754 | 11.6048 | ±23.2096 | +1.497 | 0.1343 |  |
| Education: high school or below (vs college) | -1.8385 | 18.0945 | ±36.1890 | -0.102 | 0.9191 |  |
| **Site: UCSD (vs UAB)** | **-28.7101** | 13.8294 | ±27.6589 | **-2.076** | **0.0379** | * |
| Site: UW (vs UAB) | -5.1799 | 14.0339 | ±28.0678 | -0.369 | 0.7121 |  |
| Age (years) | +1.1323 | 0.6219 | ±1.2438 | +1.821 | 0.0687 | . |
| BMI (kg/m2) | -1.4270 | 0.7403 | ±1.4806 | -1.928 | 0.0539 | . |
| **Hypertension** | **-34.4474** | 13.4871 | ±26.9741 | **-2.554** | **0.0106** | * |
| High cholesterol | -3.7742 | 11.3586 | ±22.7172 | -0.332 | 0.7397 |  |
| Kidney disease | +2.7730 | 20.7061 | ±41.4122 | +0.134 | 0.8935 |  |
| Circulatory disease | -0.2710 | 14.2553 | ±28.5106 | -0.019 | 0.9848 |  |
| Time in range 70-180, pooled (%) | +0.3759 | 1.1410 | ±2.2820 | +0.329 | 0.7418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **178**, R² = **0.1161**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0331**), Residual SE = **71.561** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+318.4931** | 122.8436 | ±245.6873 | **+2.593** | **0.0095** | ** |
| Education: graduate level (vs college) | +17.4020 | 11.5996 | ±23.1992 | +1.500 | 0.1336 |  |
| Education: high school or below (vs college) | -1.8579 | 18.0571 | ±36.1141 | -0.103 | 0.9180 |  |
| **Site: UCSD (vs UAB)** | **-28.7514** | 13.8178 | ±27.6357 | **-2.081** | **0.0375** | * |
| Site: UW (vs UAB) | -5.1153 | 14.0357 | ±28.0715 | -0.364 | 0.7155 |  |
| Age (years) | +1.1378 | 0.6218 | ±1.2436 | +1.830 | 0.0673 | . |
| BMI (kg/m2) | -1.4265 | 0.7412 | ±1.4824 | -1.925 | 0.0543 | . |
| **Hypertension** | **-34.3363** | 13.4705 | ±26.9411 | **-2.549** | **0.0108** | * |
| High cholesterol | -3.8331 | 11.3632 | ±22.7264 | -0.337 | 0.7359 |  |
| Kidney disease | +3.0725 | 20.7463 | ±41.4926 | +0.148 | 0.8823 |  |
| Circulatory disease | -0.1496 | 14.2614 | ±28.5228 | -0.010 | 0.9916 |  |
| Avg. daily time in range 70-180 (%) | +0.4692 | 1.1432 | ±2.2864 | +0.410 | 0.6815 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **178**, R² = **0.1227**, Adj R² = **0.0646**, F-statistic = **2.11** (p = **0.0221**), Residual SE = **71.292** on **166** df, AIC = **2035.7**, BIC = **2073.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.2083** | 48.3286 | ±96.6571 | **+7.660** | **1.86e-14** | *** |
| Education: graduate level (vs college) | +15.6591 | 11.5341 | ±23.0682 | +1.358 | 0.1746 |  |
| Education: high school or below (vs college) | -5.2673 | 18.3978 | ±36.7956 | -0.286 | 0.7746 |  |
| **Site: UCSD (vs UAB)** | **-27.9331** | 13.8766 | ±27.7532 | **-2.013** | **0.0441** | * |
| Site: UW (vs UAB) | -4.6883 | 13.8254 | ±27.6508 | -0.339 | 0.7345 |  |
| Age (years) | +1.0057 | 0.6240 | ±1.2481 | +1.612 | 0.1071 |  |
| BMI (kg/m2) | -1.4147 | 0.7396 | ±1.4792 | -1.913 | 0.0558 | . |
| **Hypertension** | **-34.8756** | 13.6787 | ±27.3575 | **-2.550** | **0.0108** | * |
| High cholesterol | -4.6687 | 11.1806 | ±22.3611 | -0.418 | 0.6763 |  |
| Kidney disease | +2.9659 | 20.1668 | ±40.3337 | +0.147 | 0.8831 |  |
| Circulatory disease | -1.7661 | 14.7569 | ±29.5138 | -0.120 | 0.9047 |  |
| Time 54-69, pooled (%) | +21.4511 | 24.6594 | ±49.3189 | +0.870 | 0.3844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **178**, R² = **0.1207**, Adj R² = **0.0624**, F-statistic = **2.07** (p = **0.0250**), Residual SE = **71.374** on **166** df, AIC = **2036.1**, BIC = **2074.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.3134** | 48.6127 | ±97.2255 | **+7.618** | **2.58e-14** | *** |
| Education: graduate level (vs college) | +15.9612 | 11.5192 | ±23.0384 | +1.386 | 0.1659 |  |
| Education: high school or below (vs college) | -4.5048 | 18.2855 | ±36.5711 | -0.246 | 0.8054 |  |
| **Site: UCSD (vs UAB)** | **-28.5451** | 13.8944 | ±27.7889 | **-2.054** | **0.0399** | * |
| Site: UW (vs UAB) | -5.0863 | 13.9220 | ±27.8440 | -0.365 | 0.7149 |  |
| Age (years) | +1.0165 | 0.6264 | ±1.2528 | +1.623 | 0.1046 |  |
| BMI (kg/m2) | -1.4172 | 0.7394 | ±1.4789 | -1.917 | 0.0553 | . |
| **Hypertension** | **-35.0308** | 13.7929 | ±27.5858 | **-2.540** | **0.0111** | * |
| High cholesterol | -4.4736 | 11.1962 | ±22.3924 | -0.400 | 0.6895 |  |
| Kidney disease | +3.1571 | 20.2423 | ±40.4847 | +0.156 | 0.8761 |  |
| Circulatory disease | -1.3324 | 14.9062 | ±29.8124 | -0.089 | 0.9288 |  |
| Avg. daily time 54-69 (%) | +17.5579 | 25.0491 | ±50.0983 | +0.701 | 0.4833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **178**, R² = **0.1227**, Adj R² = **0.0646**, F-statistic = **2.11** (p = **0.0221**), Residual SE = **71.292** on **166** df, AIC = **2035.7**, BIC = **2073.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.2083** | 48.3286 | ±96.6571 | **+7.660** | **1.86e-14** | *** |
| Education: graduate level (vs college) | +15.6591 | 11.5341 | ±23.0682 | +1.358 | 0.1746 |  |
| Education: high school or below (vs college) | -5.2673 | 18.3978 | ±36.7956 | -0.286 | 0.7746 |  |
| **Site: UCSD (vs UAB)** | **-27.9331** | 13.8766 | ±27.7532 | **-2.013** | **0.0441** | * |
| Site: UW (vs UAB) | -4.6883 | 13.8254 | ±27.6508 | -0.339 | 0.7345 |  |
| Age (years) | +1.0057 | 0.6240 | ±1.2481 | +1.612 | 0.1071 |  |
| BMI (kg/m2) | -1.4147 | 0.7396 | ±1.4792 | -1.913 | 0.0558 | . |
| **Hypertension** | **-34.8756** | 13.6787 | ±27.3575 | **-2.550** | **0.0108** | * |
| High cholesterol | -4.6687 | 11.1806 | ±22.3611 | -0.418 | 0.6763 |  |
| Kidney disease | +2.9659 | 20.1668 | ±40.3337 | +0.147 | 0.8831 |  |
| Circulatory disease | -1.7661 | 14.7569 | ±29.5138 | -0.120 | 0.9047 |  |
| Time < 70 (%) | +21.4511 | 24.6594 | ±49.3189 | +0.870 | 0.3844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **178**, R² = **0.1207**, Adj R² = **0.0624**, F-statistic = **2.07** (p = **0.0250**), Residual SE = **71.374** on **166** df, AIC = **2036.1**, BIC = **2074.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.3134** | 48.6127 | ±97.2255 | **+7.618** | **2.58e-14** | *** |
| Education: graduate level (vs college) | +15.9612 | 11.5192 | ±23.0384 | +1.386 | 0.1659 |  |
| Education: high school or below (vs college) | -4.5048 | 18.2855 | ±36.5711 | -0.246 | 0.8054 |  |
| **Site: UCSD (vs UAB)** | **-28.5451** | 13.8944 | ±27.7889 | **-2.054** | **0.0399** | * |
| Site: UW (vs UAB) | -5.0863 | 13.9220 | ±27.8440 | -0.365 | 0.7149 |  |
| Age (years) | +1.0165 | 0.6264 | ±1.2528 | +1.623 | 0.1046 |  |
| BMI (kg/m2) | -1.4172 | 0.7394 | ±1.4789 | -1.917 | 0.0553 | . |
| **Hypertension** | **-35.0308** | 13.7929 | ±27.5858 | **-2.540** | **0.0111** | * |
| High cholesterol | -4.4736 | 11.1962 | ±22.3924 | -0.400 | 0.6895 |  |
| Kidney disease | +3.1571 | 20.2423 | ±40.4847 | +0.156 | 0.8761 |  |
| Circulatory disease | -1.3324 | 14.9062 | ±29.8124 | -0.089 | 0.9288 |  |
| Avg. daily time < 70 (%) | +17.5579 | 25.0491 | ±50.0983 | +0.701 | 0.4833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **178**, R² = **0.1161**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0331**), Residual SE = **71.561** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.5325** | 48.4092 | ±96.8183 | **+7.551** | **4.32e-14** | *** |
| Education: graduate level (vs college) | +17.3985 | 11.6043 | ±23.2087 | +1.499 | 0.1338 |  |
| Education: high school or below (vs college) | -1.8290 | 18.0824 | ±36.1648 | -0.101 | 0.9194 |  |
| **Site: UCSD (vs UAB)** | **-28.7343** | 13.8310 | ±27.6621 | **-2.078** | **0.0378** | * |
| Site: UW (vs UAB) | -5.2037 | 14.0340 | ±28.0681 | -0.371 | 0.7108 |  |
| Age (years) | +1.1343 | 0.6209 | ±1.2418 | +1.827 | 0.0677 | . |
| BMI (kg/m2) | -1.4226 | 0.7404 | ±1.4808 | -1.921 | 0.0547 | . |
| **Hypertension** | **-34.4090** | 13.4785 | ±26.9571 | **-2.553** | **0.0107** | * |
| High cholesterol | -3.8440 | 11.3562 | ±22.7124 | -0.338 | 0.7350 |  |
| Kidney disease | +3.0381 | 20.7105 | ±41.4210 | +0.147 | 0.8834 |  |
| Circulatory disease | -0.2014 | 14.2800 | ±28.5599 | -0.014 | 0.9887 |  |
| Time 181-250, pooled (%) | -0.4559 | 1.1339 | ±2.2677 | -0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **178**, R² = **0.1164**, Adj R² = **0.0578**, F-statistic = **1.99** (p = **0.0325**), Residual SE = **71.549** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.4463** | 48.3957 | ±96.7913 | **+7.551** | **4.31e-14** | *** |
| Education: graduate level (vs college) | +17.4085 | 11.6013 | ±23.2026 | +1.501 | 0.1335 |  |
| Education: high school or below (vs college) | -1.8793 | 18.0522 | ±36.1043 | -0.104 | 0.9171 |  |
| **Site: UCSD (vs UAB)** | **-28.7838** | 13.8165 | ±27.6330 | **-2.083** | **0.0372** | * |
| Site: UW (vs UAB) | -5.1291 | 14.0352 | ±28.0705 | -0.365 | 0.7148 |  |
| Age (years) | +1.1387 | 0.6205 | ±1.2410 | +1.835 | 0.0665 | . |
| BMI (kg/m2) | -1.4230 | 0.7411 | ±1.4821 | -1.920 | 0.0548 | . |
| **Hypertension** | **-34.3011** | 13.4604 | ±26.9208 | **-2.548** | **0.0108** | * |
| High cholesterol | -3.9024 | 11.3601 | ±22.7202 | -0.344 | 0.7312 |  |
| Kidney disease | +3.3299 | 20.7487 | ±41.4973 | +0.160 | 0.8725 |  |
| Circulatory disease | -0.0860 | 14.2902 | ±28.5803 | -0.006 | 0.9952 |  |
| Avg. daily time 181-250 (%) | -0.5393 | 1.1405 | ±2.2810 | -0.473 | 0.6363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **178**, R² = **0.1161**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0331**), Residual SE = **71.561** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.5325** | 48.4092 | ±96.8183 | **+7.551** | **4.32e-14** | *** |
| Education: graduate level (vs college) | +17.3985 | 11.6043 | ±23.2087 | +1.499 | 0.1338 |  |
| Education: high school or below (vs college) | -1.8290 | 18.0824 | ±36.1648 | -0.101 | 0.9194 |  |
| **Site: UCSD (vs UAB)** | **-28.7343** | 13.8310 | ±27.6621 | **-2.078** | **0.0378** | * |
| Site: UW (vs UAB) | -5.2037 | 14.0340 | ±28.0681 | -0.371 | 0.7108 |  |
| Age (years) | +1.1343 | 0.6209 | ±1.2418 | +1.827 | 0.0677 | . |
| BMI (kg/m2) | -1.4226 | 0.7404 | ±1.4808 | -1.921 | 0.0547 | . |
| **Hypertension** | **-34.4090** | 13.4785 | ±26.9571 | **-2.553** | **0.0107** | * |
| High cholesterol | -3.8440 | 11.3562 | ±22.7124 | -0.338 | 0.7350 |  |
| Kidney disease | +3.0381 | 20.7105 | ±41.4210 | +0.147 | 0.8834 |  |
| Circulatory disease | -0.2014 | 14.2800 | ±28.5599 | -0.014 | 0.9887 |  |
| Time > 180 (%) | -0.4559 | 1.1339 | ±2.2677 | -0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1164**, Adj R² = **0.0578**, F-statistic = **1.99** (p = **0.0325**), Residual SE = **71.549** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.4463** | 48.3957 | ±96.7913 | **+7.551** | **4.31e-14** | *** |
| Education: graduate level (vs college) | +17.4085 | 11.6013 | ±23.2026 | +1.501 | 0.1335 |  |
| Education: high school or below (vs college) | -1.8793 | 18.0522 | ±36.1043 | -0.104 | 0.9171 |  |
| **Site: UCSD (vs UAB)** | **-28.7838** | 13.8165 | ±27.6330 | **-2.083** | **0.0372** | * |
| Site: UW (vs UAB) | -5.1291 | 14.0352 | ±28.0705 | -0.365 | 0.7148 |  |
| Age (years) | +1.1387 | 0.6205 | ±1.2410 | +1.835 | 0.0665 | . |
| BMI (kg/m2) | -1.4230 | 0.7411 | ±1.4821 | -1.920 | 0.0548 | . |
| **Hypertension** | **-34.3011** | 13.4604 | ±26.9208 | **-2.548** | **0.0108** | * |
| High cholesterol | -3.9024 | 11.3601 | ±22.7202 | -0.344 | 0.7312 |  |
| Kidney disease | +3.3299 | 20.7487 | ±41.4973 | +0.160 | 0.8725 |  |
| Circulatory disease | -0.0860 | 14.2902 | ±28.5803 | -0.006 | 0.9952 |  |
| Avg. daily time > 180 (%) | -0.5393 | 1.1405 | ±2.2810 | -0.473 | 0.6363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1165**, Adj R² = **0.0579**, F-statistic = **1.99** (p = **0.0323**), Residual SE = **71.544** on **166** df, AIC = **2036.9**, BIC = **2075.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+367.5027** | 47.9618 | ±95.9236 | **+7.662** | **1.82e-14** | *** |
| Education: graduate level (vs college) | +17.0125 | 11.6310 | ±23.2620 | +1.463 | 0.1436 |  |
| Education: high school or below (vs college) | -3.1627 | 19.0072 | ±38.0144 | -0.166 | 0.8678 |  |
| **Site: UCSD (vs UAB)** | **-27.8724** | 13.7824 | ±27.5648 | **-2.022** | **0.0431** | * |
| Site: UW (vs UAB) | -4.4741 | 14.1277 | ±28.2555 | -0.317 | 0.7515 |  |
| Age (years) | +1.0921 | 0.6134 | ±1.2269 | +1.780 | 0.0750 | . |
| **BMI (kg/m2)** | **-1.4994** | 0.7362 | ±1.4724 | **-2.037** | **0.0417** | * |
| **Hypertension** | **-34.3532** | 13.6831 | ±27.3662 | **-2.511** | **0.0121** | * |
| High cholesterol | -3.5182 | 11.3598 | ±22.7196 | -0.310 | 0.7568 |  |
| Kidney disease | +0.0266 | 20.2930 | ±40.5859 | +0.001 | 0.9990 |  |
| Circulatory disease | -1.6060 | 14.2416 | ±28.4833 | -0.113 | 0.9102 |  |
| Nocturnal time > 180 (%) | +0.5457 | 1.6657 | ±3.3314 | +0.328 | 0.7432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 177; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **177**, R² = **0.2618**, Adj R² = **0.2173**, F-statistic = **5.89** (p = **1.37e-07**), Residual SE = **17.041** on **166** df, AIC = **1516.8**, BIC = **1551.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.8966** | 11.2249 | ±22.4497 | **+7.296** | **2.96e-13** | *** |
| **Education: graduate level (vs college)** | **-11.4577** | 2.9128 | ±5.8256 | **-3.934** | **8.37e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8835** | 4.1657 | ±8.3315 | **-2.133** | **0.0330** | * |
| Site: UCSD (vs UAB) | +5.2193 | 3.5231 | ±7.0461 | +1.481 | 0.1385 |  |
| Site: UW (vs UAB) | +2.3350 | 3.3520 | ±6.7040 | +0.697 | 0.4861 |  |
| **Age (years)** | **-0.6347** | 0.1392 | ±0.2784 | **-4.559** | **5.13e-06** | *** |
| **BMI (kg/m2)** | **+0.3868** | 0.1921 | ±0.3841 | **+2.014** | **0.0441** | * |
| Hypertension | +2.4090 | 3.3493 | ±6.6986 | +0.719 | 0.4720 |  |
| High cholesterol | +0.8607 | 2.6988 | ±5.3975 | +0.319 | 0.7498 |  |
| **Kidney disease** | **+12.7271** | 3.6397 | ±7.2794 | **+3.497** | **4.71e-04** | *** |
| Circulatory disease | -2.1897 | 3.6840 | ±7.3681 | -0.594 | 0.5523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2126**, F-statistic = **5.32** (p = **3.47e-07**), Residual SE = **17.092** on **165** df, AIC = **1518.7**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.4101** | 17.6539 | ±35.3078 | **+4.725** | **2.30e-06** | *** |
| **Education: graduate level (vs college)** | **-11.4709** | 2.9339 | ±5.8678 | **-3.910** | **9.24e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8668** | 4.1742 | ±8.3484 | **-2.124** | **0.0337** | * |
| Site: UCSD (vs UAB) | +5.2185 | 3.5407 | ±7.0813 | +1.474 | 0.1405 |  |
| Site: UW (vs UAB) | +2.3289 | 3.3740 | ±6.7481 | +0.690 | 0.4900 |  |
| **Age (years)** | **-0.6345** | 0.1402 | ±0.2804 | **-4.526** | **6.01e-06** | *** |
| **BMI (kg/m2)** | **+0.3906** | 0.1973 | ±0.3946 | **+1.980** | **0.0477** | * |
| Hypertension | +2.4370 | 3.3632 | ±6.7264 | +0.725 | 0.4687 |  |
| High cholesterol | +0.8969 | 2.7502 | ±5.5004 | +0.326 | 0.7443 |  |
| **Kidney disease** | **+12.6684** | 3.6948 | ±7.3897 | **+3.429** | **6.07e-04** | *** |
| Circulatory disease | -2.1374 | 3.7103 | ±7.4205 | -0.576 | 0.5646 |  |
| HbA1c (%) | -0.2822 | 2.6315 | ±5.2630 | -0.107 | 0.9146 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **177**, R² = **0.2621**, Adj R² = **0.2129**, F-statistic = **5.33** (p = **3.41e-07**), Residual SE = **17.090** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0038** | 16.1176 | ±32.2353 | **+4.902** | **9.50e-07** | *** |
| **Education: graduate level (vs college)** | **-11.4320** | 2.9338 | ±5.8675 | **-3.897** | **9.75e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8111** | 4.2332 | ±8.4664 | **-2.081** | **0.0374** | * |
| Site: UCSD (vs UAB) | +5.1723 | 3.5382 | ±7.0763 | +1.462 | 0.1438 |  |
| Site: UW (vs UAB) | +2.3168 | 3.3725 | ±6.7451 | +0.687 | 0.4921 |  |
| **Age (years)** | **-0.6342** | 0.1397 | ±0.2794 | **-4.540** | **5.63e-06** | *** |
| **BMI (kg/m2)** | **+0.3832** | 0.1940 | ±0.3880 | **+1.975** | **0.0482** | * |
| Hypertension | +2.3695 | 3.3604 | ±6.7209 | +0.705 | 0.4807 |  |
| High cholesterol | +0.8585 | 2.7155 | ±5.4310 | +0.316 | 0.7519 |  |
| **Kidney disease** | **+12.6517** | 3.6732 | ±7.3464 | **+3.444** | **5.72e-04** | *** |
| Circulatory disease | -2.2631 | 3.6896 | ±7.3792 | -0.613 | 0.5396 |  |
| Mean glucose (mg/dL) | +0.0239 | 0.0988 | ±0.1976 | +0.242 | 0.8085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **177**, R² = **0.2621**, Adj R² = **0.2129**, F-statistic = **5.33** (p = **3.41e-07**), Residual SE = **17.090** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.6907** | 27.5878 | ±55.1755 | **+2.744** | **0.0061** | ** |
| **Education: graduate level (vs college)** | **-11.4320** | 2.9338 | ±5.8675 | **-3.897** | **9.75e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8111** | 4.2332 | ±8.4664 | **-2.081** | **0.0374** | * |
| Site: UCSD (vs UAB) | +5.1723 | 3.5382 | ±7.0763 | +1.462 | 0.1438 |  |
| Site: UW (vs UAB) | +2.3168 | 3.3725 | ±6.7451 | +0.687 | 0.4921 |  |
| **Age (years)** | **-0.6342** | 0.1397 | ±0.2794 | **-4.540** | **5.63e-06** | *** |
| **BMI (kg/m2)** | **+0.3832** | 0.1940 | ±0.3880 | **+1.975** | **0.0482** | * |
| Hypertension | +2.3695 | 3.3604 | ±6.7209 | +0.705 | 0.4807 |  |
| High cholesterol | +0.8585 | 2.7155 | ±5.4310 | +0.316 | 0.7519 |  |
| **Kidney disease** | **+12.6517** | 3.6732 | ±7.3464 | **+3.444** | **5.72e-04** | *** |
| Circulatory disease | -2.2631 | 3.6896 | ±7.3792 | -0.613 | 0.5396 |  |
| GMI (%) | +1.0009 | 4.1301 | ±8.2603 | +0.242 | 0.8085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **177**, R² = **0.2618**, Adj R² = **0.2126**, F-statistic = **5.32** (p = **3.49e-07**), Residual SE = **17.093** on **165** df, AIC = **1518.8**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.9498** | 15.0413 | ±30.0827 | **+5.448** | **5.09e-08** | *** |
| **Education: graduate level (vs college)** | **-11.4578** | 2.9281 | ±5.8561 | **-3.913** | **9.11e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8844** | 4.1966 | ±8.3932 | **-2.117** | **0.0343** | * |
| Site: UCSD (vs UAB) | +5.2205 | 3.5325 | ±7.0651 | +1.478 | 0.1394 |  |
| Site: UW (vs UAB) | +2.3356 | 3.3654 | ±6.7308 | +0.694 | 0.4877 |  |
| **Age (years)** | **-0.6347** | 0.1397 | ±0.2793 | **-4.545** | **5.49e-06** | *** |
| **BMI (kg/m2)** | **+0.3868** | 0.1947 | ±0.3895 | **+1.987** | **0.0470** | * |
| Hypertension | +2.4098 | 3.3637 | ±6.7274 | +0.716 | 0.4737 |  |
| High cholesterol | +0.8610 | 2.7151 | ±5.4301 | +0.317 | 0.7511 |  |
| **Kidney disease** | **+12.7269** | 3.6609 | ±7.3219 | **+3.476** | **5.08e-04** | *** |
| Circulatory disease | -2.1877 | 3.7050 | ±7.4100 | -0.590 | 0.5549 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0004 | 0.0884 | ±0.1767 | -0.005 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2620**, Adj R² = **0.2128**, F-statistic = **5.32** (p = **3.44e-07**), Residual SE = **17.091** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.9550** | 12.1483 | ±24.2966 | **+6.829** | **8.58e-12** | *** |
| **Education: graduate level (vs college)** | **-11.4314** | 2.9128 | ±5.8257 | **-3.924** | **8.69e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7575** | 4.2302 | ±8.4604 | **-2.070** | **0.0384** | * |
| Site: UCSD (vs UAB) | +5.1984 | 3.5497 | ±7.0995 | +1.464 | 0.1431 |  |
| Site: UW (vs UAB) | +2.2546 | 3.3804 | ±6.7608 | +0.667 | 0.5048 |  |
| **Age (years)** | **-0.6334** | 0.1407 | ±0.2815 | **-4.501** | **6.78e-06** | *** |
| **BMI (kg/m2)** | **+0.3865** | 0.1930 | ±0.3859 | **+2.003** | **0.0452** | * |
| Hypertension | +2.5087 | 3.3695 | ±6.7390 | +0.745 | 0.4566 |  |
| High cholesterol | +0.8389 | 2.7063 | ±5.4127 | +0.310 | 0.7566 |  |
| **Kidney disease** | **+12.8340** | 3.7929 | ±7.5859 | **+3.384** | **7.15e-04** | *** |
| Circulatory disease | -2.1273 | 3.7108 | ±7.4215 | -0.573 | 0.5664 |  |
| Glucose SD, pooled (mg/dL) | -0.0553 | 0.2838 | ±0.5676 | -0.195 | 0.8456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2621**, Adj R² = **0.2129**, F-statistic = **5.33** (p = **3.40e-07**), Residual SE = **17.089** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.1927** | 11.8998 | ±23.7996 | **+6.991** | **2.73e-12** | *** |
| **Education: graduate level (vs college)** | **-11.4253** | 2.9090 | ±5.8180 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7595** | 4.1940 | ±8.3880 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2323 | 3.5439 | ±7.0877 | +1.476 | 0.1398 |  |
| Site: UW (vs UAB) | +2.2710 | 3.3714 | ±6.7429 | +0.674 | 0.5006 |  |
| **Age (years)** | **-0.6329** | 0.1410 | ±0.2821 | **-4.487** | **7.21e-06** | *** |
| **BMI (kg/m2)** | **+0.3857** | 0.1927 | ±0.3854 | **+2.002** | **0.0453** | * |
| Hypertension | +2.5664 | 3.3678 | ±6.7357 | +0.762 | 0.4460 |  |
| High cholesterol | +0.8245 | 2.7105 | ±5.4209 | +0.304 | 0.7610 |  |
| **Kidney disease** | **+12.8219** | 3.7372 | ±7.4745 | **+3.431** | **6.02e-04** | *** |
| Circulatory disease | -2.1275 | 3.7047 | ±7.4094 | -0.574 | 0.5658 |  |
| Avg. daily SD (mg/dL) | -0.0745 | 0.2868 | ±0.5736 | -0.260 | 0.7950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **177**, R² = **0.2623**, Adj R² = **0.2131**, F-statistic = **5.33** (p = **3.33e-07**), Residual SE = **17.087** on **165** df, AIC = **1518.6**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+84.1792** | 12.6666 | ±25.3331 | **+6.646** | **3.02e-11** | *** |
| **Education: graduate level (vs college)** | **-11.3862** | 2.9079 | ±5.8158 | **-3.916** | **9.02e-05** | *** |
| **Education: high school or below (vs college)** | **-8.5504** | 4.3225 | ±8.6450 | **-1.978** | **0.0479** | * |
| Site: UCSD (vs UAB) | +5.1349 | 3.5512 | ±7.1023 | +1.446 | 0.1482 |  |
| Site: UW (vs UAB) | +2.1505 | 3.3912 | ±6.7824 | +0.634 | 0.5260 |  |
| **Age (years)** | **-0.6315** | 0.1405 | ±0.2810 | **-4.495** | **6.96e-06** | *** |
| **BMI (kg/m2)** | **+0.3831** | 0.1927 | ±0.3854 | **+1.989** | **0.0467** | * |
| Hypertension | +2.5858 | 3.3739 | ±6.7478 | +0.766 | 0.4434 |  |
| High cholesterol | +0.8130 | 2.7089 | ±5.4177 | +0.300 | 0.7641 |  |
| **Kidney disease** | **+12.8946** | 3.7758 | ±7.5517 | **+3.415** | **6.38e-04** | *** |
| Circulatory disease | -2.1321 | 3.7183 | ±7.4367 | -0.573 | 0.5664 |  |
| CV (%) | -0.1441 | 0.4017 | ±0.8035 | -0.359 | 0.7199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **177**, R² = **0.2622**, Adj R² = **0.2130**, F-statistic = **5.33** (p = **3.37e-07**), Residual SE = **17.088** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.7310** | 13.5345 | ±27.0689 | **+5.891** | **3.84e-09** | *** |
| **Education: graduate level (vs college)** | **-11.4154** | 2.9142 | ±5.8283 | **-3.917** | **8.96e-05** | *** |
| **Education: high school or below (vs college)** | **-8.6379** | 4.2829 | ±8.5658 | **-2.017** | **0.0437** | * |
| Site: UCSD (vs UAB) | +5.1703 | 3.5447 | ±7.0894 | +1.459 | 0.1447 |  |
| Site: UW (vs UAB) | +2.1998 | 3.3851 | ±6.7703 | +0.650 | 0.5158 |  |
| **Age (years)** | **-0.6318** | 0.1405 | ±0.2811 | **-4.496** | **6.93e-06** | *** |
| **BMI (kg/m2)** | **+0.3861** | 0.1933 | ±0.3866 | **+1.997** | **0.0458** | * |
| Hypertension | +2.5629 | 3.3760 | ±6.7520 | +0.759 | 0.4478 |  |
| High cholesterol | +0.8428 | 2.7087 | ±5.4173 | +0.311 | 0.7557 |  |
| **Kidney disease** | **+12.8597** | 3.7418 | ±7.4835 | **+3.437** | **5.89e-04** | *** |
| Circulatory disease | -2.1628 | 3.7207 | ±7.4414 | -0.581 | 0.5610 |  |
| Mean / SD ratio | +0.3146 | 1.0403 | ±2.0807 | +0.302 | 0.7623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2127**, F-statistic = **5.32** (p = **3.46e-07**), Residual SE = **17.092** on **165** df, AIC = **1518.7**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.9084** | 13.3671 | ±26.7341 | **+6.053** | **1.42e-09** | *** |
| **Education: graduate level (vs college)** | **-11.4430** | 2.9133 | ±5.8265 | **-3.928** | **8.57e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7938** | 4.2092 | ±8.4185 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2279 | 3.5345 | ±7.0690 | +1.479 | 0.1391 |  |
| Site: UW (vs UAB) | +2.2899 | 3.3709 | ±6.7419 | +0.679 | 0.4969 |  |
| **Age (years)** | **-0.6329** | 0.1414 | ±0.2829 | **-4.475** | **7.63e-06** | *** |
| **BMI (kg/m2)** | **+0.3863** | 0.1935 | ±0.3871 | **+1.996** | **0.0459** | * |
| Hypertension | +2.5011 | 3.3919 | ±6.7838 | +0.737 | 0.4609 |  |
| High cholesterol | +0.8561 | 2.7128 | ±5.4256 | +0.316 | 0.7523 |  |
| **Kidney disease** | **+12.7691** | 3.6938 | ±7.3875 | **+3.457** | **5.46e-04** | *** |
| Circulatory disease | -2.1961 | 3.7266 | ±7.4531 | -0.589 | 0.5556 |  |
| Avg. daily mean/SD | +0.1204 | 0.7994 | ±1.5988 | +0.151 | 0.8802 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **177**, R² = **0.2622**, Adj R² = **0.2130**, F-statistic = **5.33** (p = **3.37e-07**), Residual SE = **17.088** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.0051** | 13.2429 | ±26.4859 | **+6.041** | **1.53e-09** | *** |
| **Education: graduate level (vs college)** | **-11.4742** | 2.9258 | ±5.8515 | **-3.922** | **8.79e-05** | *** |
| **Education: high school or below (vs college)** | **-8.9639** | 4.1864 | ±8.3728 | **-2.141** | **0.0323** | * |
| Site: UCSD (vs UAB) | +5.1787 | 3.5569 | ±7.1138 | +1.456 | 0.1454 |  |
| Site: UW (vs UAB) | +2.3708 | 3.3561 | ±6.7121 | +0.706 | 0.4799 |  |
| **Age (years)** | **-0.6347** | 0.1402 | ±0.2804 | **-4.526** | **6.00e-06** | *** |
| **BMI (kg/m2)** | **+0.3833** | 0.1937 | ±0.3874 | **+1.979** | **0.0478** | * |
| Hypertension | +2.3752 | 3.3789 | ±6.7577 | +0.703 | 0.4821 |  |
| High cholesterol | +0.8201 | 2.7124 | ±5.4249 | +0.302 | 0.7624 |  |
| **Kidney disease** | **+12.7517** | 3.6601 | ±7.3202 | **+3.484** | **4.94e-04** | *** |
| Circulatory disease | -2.1873 | 3.6939 | ±7.3877 | -0.592 | 0.5538 |  |
| MAG (mg/dL/h) | +0.0568 | 0.2148 | ±0.4297 | +0.264 | 0.7916 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2127**, F-statistic = **5.32** (p = **3.44e-07**), Residual SE = **17.091** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.1060** | 12.5871 | ±25.1743 | **+6.602** | **4.04e-11** | *** |
| **Education: graduate level (vs college)** | **-11.4455** | 2.9206 | ±5.8413 | **-3.919** | **8.90e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8034** | 4.1958 | ±8.3916 | **-2.098** | **0.0359** | * |
| Site: UCSD (vs UAB) | +5.2072 | 3.5496 | ±7.0992 | +1.467 | 0.1424 |  |
| Site: UW (vs UAB) | +2.2859 | 3.3902 | ±6.7805 | +0.674 | 0.5001 |  |
| **Age (years)** | **-0.6332** | 0.1420 | ±0.2840 | **-4.459** | **8.24e-06** | *** |
| **BMI (kg/m2)** | **+0.3844** | 0.1931 | ±0.3863 | **+1.990** | **0.0466** | * |
| Hypertension | +2.4863 | 3.3399 | ±6.6798 | +0.744 | 0.4566 |  |
| High cholesterol | +0.8464 | 2.7104 | ±5.4208 | +0.312 | 0.7548 |  |
| **Kidney disease** | **+12.7715** | 3.6926 | ±7.3851 | **+3.459** | **5.43e-04** | *** |
| Circulatory disease | -2.1561 | 3.7058 | ±7.4116 | -0.582 | 0.5607 |  |
| Avg. daily range (mg/dL) | -0.0132 | 0.0757 | ±0.1515 | -0.174 | 0.8618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2126**, F-statistic = **5.32** (p = **3.47e-07**), Residual SE = **17.092** on **165** df, AIC = **1518.7**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.2173** | 11.6769 | ±23.3538 | **+7.041** | **1.91e-12** | *** |
| **Education: graduate level (vs college)** | **-11.4457** | 2.9350 | ±5.8700 | **-3.900** | **9.63e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7850** | 4.3497 | ±8.6995 | **-2.020** | **0.0434** | * |
| Site: UCSD (vs UAB) | +5.1636 | 3.5400 | ±7.0800 | +1.459 | 0.1447 |  |
| Site: UW (vs UAB) | +2.2657 | 3.3987 | ±6.7974 | +0.667 | 0.5050 |  |
| **Age (years)** | **-0.6336** | 0.1393 | ±0.2787 | **-4.547** | **5.44e-06** | *** |
| **BMI (kg/m2)** | **+0.3871** | 0.1931 | ±0.3861 | **+2.005** | **0.0450** | * |
| Hypertension | +2.3946 | 3.3575 | ±6.7151 | +0.713 | 0.4757 |  |
| High cholesterol | +0.8687 | 2.7156 | ±5.4312 | +0.320 | 0.7491 |  |
| **Kidney disease** | **+12.8135** | 3.7786 | ±7.5572 | **+3.391** | **6.96e-04** | *** |
| Circulatory disease | -2.1218 | 3.7895 | ±7.5791 | -0.560 | 0.5755 |  |
| SD of daily means (mg/dL) | -0.0595 | 0.5122 | ±1.0245 | -0.116 | 0.9075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **177**, R² = **0.2656**, Adj R² = **0.2167**, F-statistic = **5.43** (p = **2.41e-07**), Residual SE = **17.048** on **165** df, AIC = **1517.8**, BIC = **1555.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.4316** | 28.1804 | ±56.3607 | **+1.967** | **0.0492** | * |
| **Education: graduate level (vs college)** | **-11.3037** | 2.9164 | ±5.8328 | **-3.876** | **1.06e-04** | *** |
| **Education: high school or below (vs college)** | **-8.6838** | 4.1858 | ±8.3715 | **-2.075** | **0.0380** | * |
| Site: UCSD (vs UAB) | +5.1885 | 3.5444 | ±7.0888 | +1.464 | 0.1432 |  |
| Site: UW (vs UAB) | +2.2526 | 3.3577 | ±6.7154 | +0.671 | 0.5023 |  |
| **Age (years)** | **-0.6220** | 0.1404 | ±0.2809 | **-4.429** | **9.47e-06** | *** |
| **BMI (kg/m2)** | **+0.3982** | 0.1920 | ±0.3840 | **+2.074** | **0.0381** | * |
| Hypertension | +2.5362 | 3.3363 | ±6.6725 | +0.760 | 0.4471 |  |
| High cholesterol | +0.7667 | 2.6885 | ±5.3771 | +0.285 | 0.7755 |  |
| **Kidney disease** | **+13.2300** | 3.8259 | ±7.6519 | **+3.458** | **5.44e-04** | *** |
| Circulatory disease | -1.8116 | 3.7607 | ±7.5214 | -0.482 | 0.6300 |  |
| Time in range 70-180, pooled (%) | +0.2617 | 0.2494 | ±0.4987 | +1.050 | 0.2939 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **177**, R² = **0.2656**, Adj R² = **0.2166**, F-statistic = **5.42** (p = **2.43e-07**), Residual SE = **17.049** on **165** df, AIC = **1517.9**, BIC = **1556.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +55.0116 | 28.3938 | ±56.7876 | +1.937 | 0.0527 | . |
| **Education: graduate level (vs college)** | **-11.3284** | 2.9181 | ±5.8361 | **-3.882** | **1.04e-04** | *** |
| **Education: high school or below (vs college)** | **-8.7408** | 4.1778 | ±8.3556 | **-2.092** | **0.0364** | * |
| Site: UCSD (vs UAB) | +5.1976 | 3.5459 | ±7.0917 | +1.466 | 0.1427 |  |
| Site: UW (vs UAB) | +2.3074 | 3.3584 | ±6.7169 | +0.687 | 0.4920 |  |
| **Age (years)** | **-0.6213** | 0.1404 | ±0.2808 | **-4.426** | **9.62e-06** | *** |
| **BMI (kg/m2)** | **+0.3963** | 0.1918 | ±0.3835 | **+2.067** | **0.0388** | * |
| Hypertension | +2.5767 | 3.3369 | ±6.6738 | +0.772 | 0.4400 |  |
| High cholesterol | +0.7641 | 2.6905 | ±5.3809 | +0.284 | 0.7764 |  |
| **Kidney disease** | **+13.2368** | 3.8203 | ±7.6406 | **+3.465** | **5.30e-04** | *** |
| Circulatory disease | -1.7977 | 3.7514 | ±7.5028 | -0.479 | 0.6318 |  |
| Avg. daily time in range 70-180 (%) | +0.2656 | 0.2531 | ±0.5062 | +1.049 | 0.2940 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **177**, R² = **0.2800**, Adj R² = **0.2320**, F-statistic = **5.83** (p = **5.96e-08**), Residual SE = **16.881** on **165** df, AIC = **1514.3**, BIC = **1552.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1805** | 11.2192 | ±22.4384 | **+7.147** | **8.89e-13** | *** |
| **Education: graduate level (vs college)** | **-10.7319** | 2.8938 | ±5.7876 | **-3.709** | **2.08e-04** | *** |
| Education: high school or below (vs college) | -7.6941 | 4.2020 | ±8.4041 | -1.831 | 0.0671 | . |
| Site: UCSD (vs UAB) | +4.8294 | 3.4648 | ±6.9297 | +1.394 | 0.1634 |  |
| Site: UW (vs UAB) | +2.1074 | 3.3351 | ±6.6702 | +0.632 | 0.5275 |  |
| **Age (years)** | **-0.5886** | 0.1400 | ±0.2801 | **-4.203** | **2.63e-05** | *** |
| **BMI (kg/m2)** | **+0.3742** | 0.1902 | ±0.3804 | **+1.967** | **0.0491** | * |
| Hypertension | +2.3543 | 3.2671 | ±6.5342 | +0.721 | 0.4712 |  |
| High cholesterol | +1.2339 | 2.6803 | ±5.3605 | +0.460 | 0.6453 |  |
| **Kidney disease** | **+12.3739** | 3.6290 | ±7.2579 | **+3.410** | **6.50e-04** | *** |
| Circulatory disease | -1.6239 | 3.7015 | ±7.4031 | -0.439 | 0.6609 |  |
| **Time 54-69, pooled (%)** | **-8.7954** | 3.4685 | ±6.9370 | **-2.536** | **0.0112** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **177**, R² = **0.2805**, Adj R² = **0.2326**, F-statistic = **5.85** (p = **5.63e-08**), Residual SE = **16.874** on **165** df, AIC = **1514.2**, BIC = **1552.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.8164** | 11.2079 | ±22.4158 | **+7.121** | **1.07e-12** | *** |
| **Education: graduate level (vs college)** | **-10.7690** | 2.8948 | ±5.7897 | **-3.720** | **1.99e-04** | *** |
| Education: high school or below (vs college) | -7.8159 | 4.1606 | ±8.3212 | -1.879 | 0.0603 | . |
| Site: UCSD (vs UAB) | +5.0912 | 3.4656 | ±6.9313 | +1.469 | 0.1418 |  |
| Site: UW (vs UAB) | +2.2759 | 3.3397 | ±6.6794 | +0.681 | 0.4956 |  |
| **Age (years)** | **-0.5857** | 0.1397 | ±0.2794 | **-4.192** | **2.77e-05** | *** |
| **BMI (kg/m2)** | **+0.3728** | 0.1897 | ±0.3793 | **+1.966** | **0.0493** | * |
| Hypertension | +2.4517 | 3.2642 | ±6.5284 | +0.751 | 0.4526 |  |
| High cholesterol | +1.2255 | 2.6862 | ±5.3724 | +0.456 | 0.6482 |  |
| **Kidney disease** | **+12.1436** | 3.6163 | ±7.2326 | **+3.358** | **7.85e-04** | *** |
| Circulatory disease | -1.7515 | 3.6671 | ±7.3342 | -0.478 | 0.6329 |  |
| **Avg. daily time 54-69 (%)** | **-8.5686** | 3.6355 | ±7.2710 | **-2.357** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **177**, R² = **0.2800**, Adj R² = **0.2320**, F-statistic = **5.83** (p = **5.96e-08**), Residual SE = **16.881** on **165** df, AIC = **1514.3**, BIC = **1552.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1805** | 11.2192 | ±22.4384 | **+7.147** | **8.89e-13** | *** |
| **Education: graduate level (vs college)** | **-10.7319** | 2.8938 | ±5.7876 | **-3.709** | **2.08e-04** | *** |
| Education: high school or below (vs college) | -7.6941 | 4.2020 | ±8.4041 | -1.831 | 0.0671 | . |
| Site: UCSD (vs UAB) | +4.8294 | 3.4648 | ±6.9297 | +1.394 | 0.1634 |  |
| Site: UW (vs UAB) | +2.1074 | 3.3351 | ±6.6702 | +0.632 | 0.5275 |  |
| **Age (years)** | **-0.5886** | 0.1400 | ±0.2801 | **-4.203** | **2.63e-05** | *** |
| **BMI (kg/m2)** | **+0.3742** | 0.1902 | ±0.3804 | **+1.967** | **0.0491** | * |
| Hypertension | +2.3543 | 3.2671 | ±6.5342 | +0.721 | 0.4712 |  |
| High cholesterol | +1.2339 | 2.6803 | ±5.3605 | +0.460 | 0.6453 |  |
| **Kidney disease** | **+12.3739** | 3.6290 | ±7.2579 | **+3.410** | **6.50e-04** | *** |
| Circulatory disease | -1.6239 | 3.7015 | ±7.4031 | -0.439 | 0.6609 |  |
| **Time < 70 (%)** | **-8.7954** | 3.4685 | ±6.9370 | **-2.536** | **0.0112** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **177**, R² = **0.2805**, Adj R² = **0.2326**, F-statistic = **5.85** (p = **5.63e-08**), Residual SE = **16.874** on **165** df, AIC = **1514.2**, BIC = **1552.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.8164** | 11.2079 | ±22.4158 | **+7.121** | **1.07e-12** | *** |
| **Education: graduate level (vs college)** | **-10.7690** | 2.8948 | ±5.7897 | **-3.720** | **1.99e-04** | *** |
| Education: high school or below (vs college) | -7.8159 | 4.1606 | ±8.3212 | -1.879 | 0.0603 | . |
| Site: UCSD (vs UAB) | +5.0912 | 3.4656 | ±6.9313 | +1.469 | 0.1418 |  |
| Site: UW (vs UAB) | +2.2759 | 3.3397 | ±6.6794 | +0.681 | 0.4956 |  |
| **Age (years)** | **-0.5857** | 0.1397 | ±0.2794 | **-4.192** | **2.77e-05** | *** |
| **BMI (kg/m2)** | **+0.3728** | 0.1897 | ±0.3793 | **+1.966** | **0.0493** | * |
| Hypertension | +2.4517 | 3.2642 | ±6.5284 | +0.751 | 0.4526 |  |
| High cholesterol | +1.2255 | 2.6862 | ±5.3724 | +0.456 | 0.6482 |  |
| **Kidney disease** | **+12.1436** | 3.6163 | ±7.2326 | **+3.358** | **7.85e-04** | *** |
| Circulatory disease | -1.7515 | 3.6671 | ±7.3342 | -0.478 | 0.6329 |  |
| **Avg. daily time < 70 (%)** | **-8.5686** | 3.6355 | ±7.2710 | **-2.357** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **177**, R² = **0.2646**, Adj R² = **0.2156**, F-statistic = **5.40** (p = **2.67e-07**), Residual SE = **17.060** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6940** | 11.2200 | ±22.4401 | **+7.281** | **3.31e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3457** | 2.9183 | ±5.8365 | **-3.888** | **1.01e-04** | *** |
| **Education: high school or below (vs college)** | **-8.7445** | 4.1864 | ±8.3729 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2031 | 3.5462 | ±7.0923 | +1.467 | 0.1423 |  |
| Site: UW (vs UAB) | +2.2710 | 3.3597 | ±6.7194 | +0.676 | 0.4991 |  |
| **Age (years)** | **-0.6251** | 0.1405 | ±0.2810 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3967** | 0.1923 | ±0.3847 | **+2.063** | **0.0392** | * |
| Hypertension | +2.5180 | 3.3432 | ±6.6863 | +0.753 | 0.4513 |  |
| High cholesterol | +0.7718 | 2.6919 | ±5.3838 | +0.287 | 0.7743 |  |
| **Kidney disease** | **+13.1614** | 3.8136 | ±7.6273 | **+3.451** | **5.58e-04** | *** |
| Circulatory disease | -1.8841 | 3.7535 | ±7.5070 | -0.502 | 0.6157 |  |
| Time 181-250, pooled (%) | -0.2214 | 0.2508 | ±0.5017 | -0.883 | 0.3774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **177**, R² = **0.2644**, Adj R² = **0.2154**, F-statistic = **5.39** (p = **2.71e-07**), Residual SE = **17.062** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6784** | 11.2254 | ±22.4507 | **+7.276** | **3.43e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3682** | 2.9198 | ±5.8397 | **-3.893** | **9.88e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7927** | 4.1812 | ±8.3625 | **-2.103** | **0.0355** | * |
| Site: UCSD (vs UAB) | +5.2046 | 3.5466 | ±7.0933 | +1.467 | 0.1422 |  |
| Site: UW (vs UAB) | +2.3137 | 3.3607 | ±6.7214 | +0.688 | 0.4912 |  |
| **Age (years)** | **-0.6249** | 0.1404 | ±0.2808 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3950** | 0.1922 | ±0.3843 | **+2.056** | **0.0398** | * |
| Hypertension | +2.5469 | 3.3443 | ±6.6885 | +0.762 | 0.4463 |  |
| High cholesterol | +0.7713 | 2.6939 | ±5.3878 | +0.286 | 0.7746 |  |
| **Kidney disease** | **+13.1645** | 3.8095 | ±7.6191 | **+3.456** | **5.49e-04** | *** |
| Circulatory disease | -1.8761 | 3.7452 | ±7.4903 | -0.501 | 0.6164 |  |
| Avg. daily time 181-250 (%) | -0.2201 | 0.2536 | ±0.5071 | -0.868 | 0.3854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **177**, R² = **0.2646**, Adj R² = **0.2156**, F-statistic = **5.40** (p = **2.67e-07**), Residual SE = **17.060** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6940** | 11.2200 | ±22.4401 | **+7.281** | **3.31e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3457** | 2.9183 | ±5.8365 | **-3.888** | **1.01e-04** | *** |
| **Education: high school or below (vs college)** | **-8.7445** | 4.1864 | ±8.3729 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2031 | 3.5462 | ±7.0923 | +1.467 | 0.1423 |  |
| Site: UW (vs UAB) | +2.2710 | 3.3597 | ±6.7194 | +0.676 | 0.4991 |  |
| **Age (years)** | **-0.6251** | 0.1405 | ±0.2810 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3967** | 0.1923 | ±0.3847 | **+2.063** | **0.0392** | * |
| Hypertension | +2.5180 | 3.3432 | ±6.6863 | +0.753 | 0.4513 |  |
| High cholesterol | +0.7718 | 2.6919 | ±5.3838 | +0.287 | 0.7743 |  |
| **Kidney disease** | **+13.1614** | 3.8136 | ±7.6273 | **+3.451** | **5.58e-04** | *** |
| Circulatory disease | -1.8841 | 3.7535 | ±7.5070 | -0.502 | 0.6157 |  |
| Time > 180 (%) | -0.2214 | 0.2508 | ±0.5017 | -0.883 | 0.3774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2644**, Adj R² = **0.2154**, F-statistic = **5.39** (p = **2.71e-07**), Residual SE = **17.062** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6784** | 11.2254 | ±22.4507 | **+7.276** | **3.43e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3682** | 2.9198 | ±5.8397 | **-3.893** | **9.88e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7927** | 4.1812 | ±8.3625 | **-2.103** | **0.0355** | * |
| Site: UCSD (vs UAB) | +5.2046 | 3.5466 | ±7.0933 | +1.467 | 0.1422 |  |
| Site: UW (vs UAB) | +2.3137 | 3.3607 | ±6.7214 | +0.688 | 0.4912 |  |
| **Age (years)** | **-0.6249** | 0.1404 | ±0.2808 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3950** | 0.1922 | ±0.3843 | **+2.056** | **0.0398** | * |
| Hypertension | +2.5469 | 3.3443 | ±6.6885 | +0.762 | 0.4463 |  |
| High cholesterol | +0.7713 | 2.6939 | ±5.3878 | +0.286 | 0.7746 |  |
| **Kidney disease** | **+13.1645** | 3.8095 | ±7.6191 | **+3.456** | **5.49e-04** | *** |
| Circulatory disease | -1.8761 | 3.7452 | ±7.4903 | -0.501 | 0.6164 |  |
| Avg. daily time > 180 (%) | -0.2201 | 0.2536 | ±0.5071 | -0.868 | 0.3854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2626**, Adj R² = **0.2134**, F-statistic = **5.34** (p = **3.25e-07**), Residual SE = **17.084** on **165** df, AIC = **1518.6**, BIC = **1556.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6277** | 11.3507 | ±22.7014 | **+7.191** | **6.41e-13** | *** |
| **Education: graduate level (vs college)** | **-11.4315** | 2.9213 | ±5.8425 | **-3.913** | **9.11e-05** | *** |
| **Education: high school or below (vs college)** | **-8.6971** | 4.2448 | ±8.4896 | **-2.049** | **0.0405** | * |
| Site: UCSD (vs UAB) | +5.0865 | 3.5676 | ±7.1352 | +1.426 | 0.1539 |  |
| Site: UW (vs UAB) | +2.2138 | 3.3586 | ±6.7172 | +0.659 | 0.5098 |  |
| **Age (years)** | **-0.6307** | 0.1404 | ±0.2808 | **-4.492** | **7.07e-06** | *** |
| **BMI (kg/m2)** | **+0.3974** | 0.1972 | ±0.3944 | **+2.015** | **0.0439** | * |
| Hypertension | +2.3350 | 3.3750 | ±6.7499 | +0.692 | 0.4890 |  |
| High cholesterol | +0.8540 | 2.7035 | ±5.4070 | +0.316 | 0.7521 |  |
| **Kidney disease** | **+13.0033** | 3.8709 | ±7.7419 | **+3.359** | **7.82e-04** | *** |
| Circulatory disease | -1.9865 | 3.7699 | ±7.5398 | -0.527 | 0.5982 |  |
| Nocturnal time > 180 (%) | -0.1110 | 0.2727 | ±0.5454 | -0.407 | 0.6838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 115 single-predictor tests; 9 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 178): best single predictor out of sample is **Nocturnal mean** (CV R² 0.008 vs 0.002 for covariates alone, gain +0.006; +612 per SD, p = 0.088). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 178): best single predictor out of sample is **Nocturnal mean** (CV R² 0.041 vs 0.035 for covariates alone, gain +0.006; +1.79 per SD, p = 0.095). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 177): best single predictor out of sample is **%54-69 (pooled)** (CV R² 0.128 vs 0.121 for covariates alone, gain +0.007; -1.38 per SD, p = 0.008). Raw p < 0.05 (FDR not applicable here): %54-69 (pooled) (p = 0.008), %<70 (pooled) (p = 0.008), %54-69 (daily avg) (p = 0.020), %<70 (daily avg) (p = 0.020).
- **Total sleep time per night (min)** (n = 178): best single predictor out of sample is **MAG** (CV R² -0.091 vs -0.103 for covariates alone, gain +0.012; -13.8 per SD, p = 0.007). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.007).
- **Garmin stress score, mean (0-100)** (n = 177): best single predictor out of sample is **%<70 (pooled)** (CV R² 0.153 vs 0.147 for covariates alone, gain +0.006; -2.7 per SD, p = 0.011). Raw p < 0.05 (FDR not applicable here): %54-69 (pooled) (p = 0.011), %<70 (pooled) (p = 0.011), %54-69 (daily avg) (p = 0.018), %<70 (daily avg) (p = 0.018).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.012, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.007, via %54-69 (pooled)); Brisk-cadence minutes per day (>= 100 steps/min) (+0.006, via Nocturnal mean); Garmin stress score, mean (0-100) (+0.006, via %<70 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band 54-69 (0 FDR-significant / 4 raw-significant of 10); Band < 70 (0 FDR-significant / 4 raw-significant of 10); CGM variability (0 FDR-significant / 1 raw-significant of 40).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Steps per wear-day (Nocturnal mean, ΔAIC -2.9); Brisk-cadence minutes per day (Nocturnal mean, ΔAIC -2.6); Resting heart-rate proxy (%<70 (pooled), ΔAIC -5.1); Total sleep time per night (MAG, ΔAIC -6.7); Garmin stress score, mean (%<70 (daily avg), ΔAIC -4.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
