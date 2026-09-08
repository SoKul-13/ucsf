# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 241; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **241**, R² = **0.1624**, Adj R² = **0.1144**, F-statistic = **3.39** (p = **8.90e-05**), Residual SE = **0.825** on **227** df, AIC = **604.7**, BIC = **653.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1336** | 0.5030 | ±1.0061 | **+4.241** | **2.22e-05** | *** |
| Education: graduate level (vs college) | -0.0537 | 0.1117 | ±0.2235 | -0.481 | 0.6305 |  |
| Education: high school or below (vs college) | +0.3861 | 0.2752 | ±0.5505 | +1.403 | 0.1607 |  |
| Site: UCSD (vs UAB) | -0.1314 | 0.1697 | ±0.3394 | -0.774 | 0.4389 |  |
| **Site: UW (vs UAB)** | **-0.4893** | 0.1618 | ±0.3235 | **-3.025** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0692 | 0.1528 | ±0.3056 | -0.453 | 0.6505 |  |
| Season: summer (vs autumn) | +0.0572 | 0.1543 | ±0.3087 | +0.371 | 0.7107 |  |
| Season: winter (vs autumn) | -0.0180 | 0.1550 | ±0.3101 | -0.116 | 0.9074 |  |
| **Age (years)** | **-0.0113** | 0.0051 | ±0.0102 | **-2.204** | **0.0275** | * |
| BMI (kg/m2) | +0.0174 | 0.0101 | ±0.0203 | +1.720 | 0.0854 | . |
| Hypertension | -0.0594 | 0.1240 | ±0.2480 | -0.479 | 0.6321 |  |
| High cholesterol | +0.1759 | 0.1113 | ±0.2227 | +1.580 | 0.1141 |  |
| Kidney disease | -0.2383 | 0.2087 | ±0.4174 | -1.142 | 0.2535 |  |
| Circulatory disease | +0.2646 | 0.2054 | ±0.4107 | +1.288 | 0.1976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **241**, R² = **0.1636**, Adj R² = **0.1118**, F-statistic = **3.16** (p = **1.53e-04**), Residual SE = **0.826** on **226** df, AIC = **606.3**, BIC = **658.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3174** | 0.5933 | ±1.1865 | **+3.906** | **9.38e-05** | *** |
| Education: graduate level (vs college) | -0.0533 | 0.1121 | ±0.2242 | -0.475 | 0.6347 |  |
| Education: high school or below (vs college) | +0.4078 | 0.2851 | ±0.5702 | +1.430 | 0.1526 |  |
| Site: UCSD (vs UAB) | -0.1318 | 0.1700 | ±0.3400 | -0.775 | 0.4383 |  |
| **Site: UW (vs UAB)** | **-0.4872** | 0.1611 | ±0.3221 | **-3.025** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0691 | 0.1529 | ±0.3057 | -0.452 | 0.6512 |  |
| Season: summer (vs autumn) | +0.0520 | 0.1564 | ±0.3128 | +0.332 | 0.7397 |  |
| Season: winter (vs autumn) | -0.0172 | 0.1552 | ±0.3103 | -0.111 | 0.9116 |  |
| **Age (years)** | **-0.0112** | 0.0051 | ±0.0102 | **-2.192** | **0.0284** | * |
| BMI (kg/m2) | +0.0179 | 0.0101 | ±0.0203 | +1.772 | 0.0764 | . |
| Hypertension | -0.0590 | 0.1242 | ±0.2483 | -0.475 | 0.6344 |  |
| High cholesterol | +0.1803 | 0.1118 | ±0.2236 | +1.613 | 0.1069 |  |
| Kidney disease | -0.2452 | 0.2105 | ±0.4211 | -1.165 | 0.2442 |  |
| Circulatory disease | +0.2839 | 0.2151 | ±0.4301 | +1.320 | 0.1869 |  |
| HbA1c (%) | -0.0347 | 0.0465 | ±0.0929 | -0.747 | 0.4548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **241**, R² = **0.1648**, Adj R² = **0.1131**, F-statistic = **3.19** (p = **1.35e-04**), Residual SE = **0.825** on **226** df, AIC = **606.0**, BIC = **658.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3201** | 0.5407 | ±1.0813 | **+4.291** | **1.78e-05** | *** |
| Education: graduate level (vs college) | -0.0460 | 0.1121 | ±0.2243 | -0.410 | 0.6818 |  |
| Education: high school or below (vs college) | +0.4197 | 0.2847 | ±0.5695 | +1.474 | 0.1405 |  |
| Site: UCSD (vs UAB) | -0.1387 | 0.1705 | ±0.3410 | -0.814 | 0.4159 |  |
| **Site: UW (vs UAB)** | **-0.4877** | 0.1616 | ±0.3233 | **-3.018** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0675 | 0.1534 | ±0.3067 | -0.440 | 0.6600 |  |
| Season: summer (vs autumn) | +0.0413 | 0.1567 | ±0.3134 | +0.263 | 0.7923 |  |
| Season: winter (vs autumn) | -0.0280 | 0.1543 | ±0.3087 | -0.181 | 0.8562 |  |
| **Age (years)** | **-0.0114** | 0.0051 | ±0.0103 | **-2.213** | **0.0269** | * |
| BMI (kg/m2) | +0.0185 | 0.0103 | ±0.0205 | +1.801 | 0.0716 | . |
| Hypertension | -0.0565 | 0.1240 | ±0.2480 | -0.456 | 0.6485 |  |
| High cholesterol | +0.1804 | 0.1117 | ±0.2235 | +1.614 | 0.1065 |  |
| Kidney disease | -0.2366 | 0.2078 | ±0.4157 | -1.138 | 0.2550 |  |
| Circulatory disease | +0.2848 | 0.2106 | ±0.4211 | +1.352 | 0.1762 |  |
| Mean glucose (mg/dL) | -0.0015 | 0.0016 | ±0.0031 | -0.994 | 0.3201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **241**, R² = **0.1648**, Adj R² = **0.1131**, F-statistic = **3.19** (p = **1.35e-04**), Residual SE = **0.825** on **226** df, AIC = **606.0**, BIC = **658.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5345** | 0.6510 | ±1.3020 | **+3.893** | **9.89e-05** | *** |
| Education: graduate level (vs college) | -0.0460 | 0.1121 | ±0.2243 | -0.410 | 0.6818 |  |
| Education: high school or below (vs college) | +0.4197 | 0.2847 | ±0.5695 | +1.474 | 0.1405 |  |
| Site: UCSD (vs UAB) | -0.1387 | 0.1705 | ±0.3410 | -0.814 | 0.4159 |  |
| **Site: UW (vs UAB)** | **-0.4877** | 0.1616 | ±0.3233 | **-3.018** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0675 | 0.1534 | ±0.3067 | -0.440 | 0.6600 |  |
| Season: summer (vs autumn) | +0.0413 | 0.1567 | ±0.3134 | +0.263 | 0.7923 |  |
| Season: winter (vs autumn) | -0.0280 | 0.1543 | ±0.3087 | -0.181 | 0.8562 |  |
| **Age (years)** | **-0.0114** | 0.0051 | ±0.0103 | **-2.213** | **0.0269** | * |
| BMI (kg/m2) | +0.0185 | 0.0103 | ±0.0205 | +1.801 | 0.0716 | . |
| Hypertension | -0.0565 | 0.1240 | ±0.2480 | -0.456 | 0.6485 |  |
| High cholesterol | +0.1804 | 0.1117 | ±0.2235 | +1.614 | 0.1065 |  |
| Kidney disease | -0.2366 | 0.2078 | ±0.4157 | -1.138 | 0.2550 |  |
| Circulatory disease | +0.2848 | 0.2106 | ±0.4211 | +1.352 | 0.1762 |  |
| GMI (%) | -0.0648 | 0.0651 | ±0.1303 | -0.994 | 0.3201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **241**, R² = **0.1655**, Adj R² = **0.1138**, F-statistic = **3.20** (p = **1.26e-04**), Residual SE = **0.825** on **226** df, AIC = **605.8**, BIC = **658.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3158** | 0.5301 | ±1.0603 | **+4.368** | **1.25e-05** | *** |
| Education: graduate level (vs college) | -0.0490 | 0.1122 | ±0.2244 | -0.436 | 0.6626 |  |
| Education: high school or below (vs college) | +0.4201 | 0.2833 | ±0.5665 | +1.483 | 0.1380 |  |
| Site: UCSD (vs UAB) | -0.1345 | 0.1701 | ±0.3403 | -0.790 | 0.4293 |  |
| **Site: UW (vs UAB)** | **-0.4887** | 0.1618 | ±0.3236 | **-3.020** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0630 | 0.1537 | ±0.3074 | -0.410 | 0.6820 |  |
| Season: summer (vs autumn) | +0.0377 | 0.1584 | ±0.3168 | +0.238 | 0.8120 |  |
| Season: winter (vs autumn) | -0.0251 | 0.1543 | ±0.3087 | -0.162 | 0.8710 |  |
| **Age (years)** | **-0.0115** | 0.0051 | ±0.0103 | **-2.240** | **0.0251** | * |
| BMI (kg/m2) | +0.0189 | 0.0103 | ±0.0206 | +1.834 | 0.0667 | . |
| Hypertension | -0.0568 | 0.1237 | ±0.2474 | -0.459 | 0.6462 |  |
| High cholesterol | +0.1813 | 0.1116 | ±0.2232 | +1.624 | 0.1043 |  |
| Kidney disease | -0.2497 | 0.2097 | ±0.4193 | -1.191 | 0.2337 |  |
| Circulatory disease | +0.2836 | 0.2096 | ±0.4191 | +1.353 | 0.1759 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0016 | 0.0014 | ±0.0028 | -1.117 | 0.2641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **241**, R² = **0.1632**, Adj R² = **0.1113**, F-statistic = **3.15** (p = **1.59e-04**), Residual SE = **0.826** on **226** df, AIC = **606.4**, BIC = **658.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2190** | 0.4984 | ±0.9968 | **+4.452** | **8.50e-06** | *** |
| Education: graduate level (vs college) | -0.0531 | 0.1122 | ±0.2245 | -0.474 | 0.6358 |  |
| Education: high school or below (vs college) | +0.3887 | 0.2763 | ±0.5525 | +1.407 | 0.1594 |  |
| Site: UCSD (vs UAB) | -0.1385 | 0.1700 | ±0.3401 | -0.814 | 0.4155 |  |
| **Site: UW (vs UAB)** | **-0.4927** | 0.1623 | ±0.3247 | **-3.035** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.0688 | 0.1533 | ±0.3066 | -0.449 | 0.6536 |  |
| Season: summer (vs autumn) | +0.0532 | 0.1560 | ±0.3121 | +0.341 | 0.7334 |  |
| Season: winter (vs autumn) | -0.0213 | 0.1552 | ±0.3103 | -0.137 | 0.8909 |  |
| **Age (years)** | **-0.0112** | 0.0052 | ±0.0103 | **-2.171** | **0.0299** | * |
| BMI (kg/m2) | +0.0180 | 0.0107 | ±0.0213 | +1.690 | 0.0910 | . |
| Hypertension | -0.0562 | 0.1238 | ±0.2476 | -0.454 | 0.6498 |  |
| High cholesterol | +0.1698 | 0.1120 | ±0.2241 | +1.515 | 0.1297 |  |
| Kidney disease | -0.2235 | 0.2088 | ±0.4175 | -1.071 | 0.2844 |  |
| Circulatory disease | +0.2757 | 0.2101 | ±0.4202 | +1.312 | 0.1894 |  |
| Glucose SD, pooled (mg/dL) | -0.0034 | 0.0072 | ±0.0145 | -0.471 | 0.6379 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **241**, R² = **0.1624**, Adj R² = **0.1105**, F-statistic = **3.13** (p = **1.72e-04**), Residual SE = **0.827** on **226** df, AIC = **606.6**, BIC = **658.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1198** | 0.4906 | ±0.9811 | **+4.321** | **1.55e-05** | *** |
| Education: graduate level (vs college) | -0.0541 | 0.1123 | ±0.2246 | -0.482 | 0.6299 |  |
| Education: high school or below (vs college) | +0.3860 | 0.2765 | ±0.5530 | +1.396 | 0.1627 |  |
| Site: UCSD (vs UAB) | -0.1302 | 0.1699 | ±0.3399 | -0.766 | 0.4437 |  |
| **Site: UW (vs UAB)** | **-0.4889** | 0.1621 | ±0.3242 | **-3.016** | **0.0026** | ** |
| Season: spring (vs autumn) | -0.0689 | 0.1534 | ±0.3068 | -0.449 | 0.6533 |  |
| Season: summer (vs autumn) | +0.0579 | 0.1559 | ±0.3117 | +0.371 | 0.7103 |  |
| Season: winter (vs autumn) | -0.0174 | 0.1557 | ±0.3115 | -0.112 | 0.9112 |  |
| **Age (years)** | **-0.0113** | 0.0052 | ±0.0103 | **-2.190** | **0.0285** | * |
| BMI (kg/m2) | +0.0173 | 0.0109 | ±0.0218 | +1.588 | 0.1122 |  |
| Hypertension | -0.0601 | 0.1233 | ±0.2466 | -0.487 | 0.6260 |  |
| High cholesterol | +0.1769 | 0.1118 | ±0.2237 | +1.582 | 0.1137 |  |
| Kidney disease | -0.2408 | 0.2143 | ±0.4285 | -1.124 | 0.2612 |  |
| Circulatory disease | +0.2626 | 0.2099 | ±0.4197 | +1.251 | 0.2108 |  |
| Avg. daily SD (mg/dL) | +0.0006 | 0.0082 | ±0.0163 | +0.077 | 0.9389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **241**, R² = **0.1628**, Adj R² = **0.1110**, F-statistic = **3.14** (p = **1.65e-04**), Residual SE = **0.826** on **226** df, AIC = **606.5**, BIC = **658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0500** | 0.5239 | ±1.0478 | **+3.913** | **9.12e-05** | *** |
| Education: graduate level (vs college) | -0.0504 | 0.1132 | ±0.2264 | -0.445 | 0.6561 |  |
| Education: high school or below (vs college) | +0.3954 | 0.2828 | ±0.5656 | +1.398 | 0.1621 |  |
| Site: UCSD (vs UAB) | -0.1271 | 0.1703 | ±0.3406 | -0.746 | 0.4554 |  |
| **Site: UW (vs UAB)** | **-0.4845** | 0.1624 | ±0.3248 | **-2.984** | **0.0028** | ** |
| Season: spring (vs autumn) | -0.0693 | 0.1541 | ±0.3082 | -0.450 | 0.6529 |  |
| Season: summer (vs autumn) | +0.0552 | 0.1546 | ±0.3093 | +0.357 | 0.7212 |  |
| Season: winter (vs autumn) | -0.0192 | 0.1555 | ±0.3110 | -0.124 | 0.9017 |  |
| **Age (years)** | **-0.0114** | 0.0052 | ±0.0103 | **-2.205** | **0.0275** | * |
| BMI (kg/m2) | +0.0173 | 0.0103 | ±0.0206 | +1.680 | 0.0930 | . |
| Hypertension | -0.0601 | 0.1241 | ±0.2481 | -0.484 | 0.6282 |  |
| High cholesterol | +0.1838 | 0.1143 | ±0.2286 | +1.608 | 0.1078 |  |
| Kidney disease | -0.2488 | 0.2163 | ±0.4327 | -1.150 | 0.2501 |  |
| Circulatory disease | +0.2630 | 0.2060 | ±0.4119 | +1.277 | 0.2017 |  |
| CV (%) | +0.0039 | 0.0122 | ±0.0244 | +0.322 | 0.7472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **241**, R² = **0.1635**, Adj R² = **0.1117**, F-statistic = **3.16** (p = **1.54e-04**), Residual SE = **0.826** on **226** df, AIC = **606.3**, BIC = **658.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2886** | 0.6387 | ±1.2774 | **+3.583** | **3.39e-04** | *** |
| Education: graduate level (vs college) | -0.0515 | 0.1125 | ±0.2250 | -0.457 | 0.6475 |  |
| Education: high school or below (vs college) | +0.3979 | 0.2808 | ±0.5616 | +1.417 | 0.1565 |  |
| Site: UCSD (vs UAB) | -0.1262 | 0.1699 | ±0.3397 | -0.743 | 0.4575 |  |
| **Site: UW (vs UAB)** | **-0.4823** | 0.1622 | ±0.3243 | **-2.974** | **0.0029** | ** |
| Season: spring (vs autumn) | -0.0699 | 0.1546 | ±0.3093 | -0.452 | 0.6514 |  |
| Season: summer (vs autumn) | +0.0521 | 0.1548 | ±0.3095 | +0.336 | 0.7365 |  |
| Season: winter (vs autumn) | -0.0228 | 0.1561 | ±0.3122 | -0.146 | 0.8837 |  |
| **Age (years)** | **-0.0114** | 0.0052 | ±0.0103 | **-2.215** | **0.0268** | * |
| BMI (kg/m2) | +0.0173 | 0.0102 | ±0.0205 | +1.693 | 0.0905 | . |
| Hypertension | -0.0628 | 0.1234 | ±0.2467 | -0.509 | 0.6108 |  |
| High cholesterol | +0.1864 | 0.1141 | ±0.2283 | +1.633 | 0.1025 |  |
| Kidney disease | -0.2526 | 0.2182 | ±0.4363 | -1.158 | 0.2469 |  |
| Circulatory disease | +0.2623 | 0.2057 | ±0.4114 | +1.275 | 0.2022 |  |
| Mean / SD ratio | -0.0319 | 0.0627 | ±0.1255 | -0.508 | 0.6113 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **241**, R² = **0.1687**, Adj R² = **0.1172**, F-statistic = **3.28** (p = **9.04e-05**), Residual SE = **0.823** on **226** df, AIC = **604.8**, BIC = **657.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4854** | 0.6321 | ±1.2643 | **+3.932** | **8.44e-05** | *** |
| Education: graduate level (vs college) | -0.0535 | 0.1115 | ±0.2230 | -0.479 | 0.6317 |  |
| Education: high school or below (vs college) | +0.4153 | 0.2790 | ±0.5581 | +1.488 | 0.1367 |  |
| Site: UCSD (vs UAB) | -0.1212 | 0.1691 | ±0.3383 | -0.716 | 0.4737 |  |
| **Site: UW (vs UAB)** | **-0.4723** | 0.1610 | ±0.3220 | **-2.934** | **0.0033** | ** |
| Season: spring (vs autumn) | -0.0614 | 0.1546 | ±0.3093 | -0.397 | 0.6915 |  |
| Season: summer (vs autumn) | +0.0460 | 0.1526 | ±0.3052 | +0.302 | 0.7629 |  |
| Season: winter (vs autumn) | -0.0265 | 0.1542 | ±0.3084 | -0.172 | 0.8633 |  |
| **Age (years)** | **-0.0117** | 0.0052 | ±0.0103 | **-2.272** | **0.0231** | * |
| BMI (kg/m2) | +0.0168 | 0.0103 | ±0.0206 | +1.634 | 0.1023 |  |
| Hypertension | -0.0703 | 0.1223 | ±0.2445 | -0.575 | 0.5654 |  |
| High cholesterol | +0.1990 | 0.1131 | ±0.2262 | +1.760 | 0.0784 | . |
| Kidney disease | -0.2735 | 0.2211 | ±0.4422 | -1.237 | 0.2161 |  |
| Circulatory disease | +0.2614 | 0.2042 | ±0.4085 | +1.280 | 0.2006 |  |
| Avg. daily mean/SD | -0.0588 | 0.0484 | ±0.0969 | -1.213 | 0.2251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **241**, R² = **0.1723**, Adj R² = **0.1211**, F-statistic = **3.36** (p = **6.24e-05**), Residual SE = **0.822** on **226** df, AIC = **603.8**, BIC = **656.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6672** | 0.5245 | ±1.0489 | **+3.179** | **0.0015** | ** |
| Education: graduate level (vs college) | -0.0332 | 0.1119 | ±0.2239 | -0.297 | 0.7666 |  |
| Education: high school or below (vs college) | +0.3958 | 0.2711 | ±0.5422 | +1.460 | 0.1443 |  |
| Site: UCSD (vs UAB) | -0.0927 | 0.1700 | ±0.3400 | -0.545 | 0.5857 |  |
| **Site: UW (vs UAB)** | **-0.4374** | 0.1637 | ±0.3273 | **-2.673** | **0.0075** | ** |
| Season: spring (vs autumn) | -0.0781 | 0.1534 | ±0.3068 | -0.509 | 0.6106 |  |
| Season: summer (vs autumn) | +0.0798 | 0.1529 | ±0.3059 | +0.522 | 0.6018 |  |
| Season: winter (vs autumn) | -0.0063 | 0.1541 | ±0.3081 | -0.041 | 0.9672 |  |
| **Age (years)** | **-0.0112** | 0.0050 | ±0.0101 | **-2.232** | **0.0256** | * |
| BMI (kg/m2) | +0.0146 | 0.0104 | ±0.0209 | +1.396 | 0.1627 |  |
| Hypertension | -0.0314 | 0.1262 | ±0.2525 | -0.249 | 0.8036 |  |
| High cholesterol | +0.2144 | 0.1117 | ±0.2234 | +1.919 | 0.0550 | . |
| Kidney disease | -0.2351 | 0.2099 | ±0.4198 | -1.120 | 0.2627 |  |
| Circulatory disease | +0.2443 | 0.2058 | ±0.4116 | +1.187 | 0.2352 |  |
| MAG (mg/dL/h) | +0.0105 | 0.0060 | ±0.0120 | +1.754 | 0.0794 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **241**, R² = **0.1632**, Adj R² = **0.1114**, F-statistic = **3.15** (p = **1.58e-04**), Residual SE = **0.826** on **226** df, AIC = **606.4**, BIC = **658.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0101** | 0.5123 | ±1.0246 | **+3.924** | **8.71e-05** | *** |
| Education: graduate level (vs college) | -0.0546 | 0.1121 | ±0.2242 | -0.487 | 0.6264 |  |
| Education: high school or below (vs college) | +0.3844 | 0.2754 | ±0.5507 | +1.396 | 0.1627 |  |
| Site: UCSD (vs UAB) | -0.1215 | 0.1698 | ±0.3396 | -0.715 | 0.4744 |  |
| **Site: UW (vs UAB)** | **-0.4822** | 0.1615 | ±0.3229 | **-2.986** | **0.0028** | ** |
| Season: spring (vs autumn) | -0.0707 | 0.1545 | ±0.3090 | -0.457 | 0.6474 |  |
| Season: summer (vs autumn) | +0.0603 | 0.1546 | ±0.3093 | +0.390 | 0.6965 |  |
| Season: winter (vs autumn) | -0.0154 | 0.1559 | ±0.3117 | -0.099 | 0.9213 |  |
| **Age (years)** | **-0.0113** | 0.0051 | ±0.0103 | **-2.200** | **0.0278** | * |
| BMI (kg/m2) | +0.0168 | 0.0107 | ±0.0214 | +1.572 | 0.1160 |  |
| Hypertension | -0.0603 | 0.1240 | ±0.2480 | -0.487 | 0.6265 |  |
| High cholesterol | +0.1860 | 0.1112 | ±0.2223 | +1.673 | 0.0943 | . |
| Kidney disease | -0.2479 | 0.2149 | ±0.4297 | -1.154 | 0.2485 |  |
| Circulatory disease | +0.2551 | 0.2086 | ±0.4172 | +1.223 | 0.2215 |  |
| Avg. daily range (mg/dL) | +0.0010 | 0.0023 | ±0.0046 | +0.427 | 0.6695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **241**, R² = **0.1685**, Adj R² = **0.1169**, F-statistic = **3.27** (p = **9.31e-05**), Residual SE = **0.824** on **226** df, AIC = **604.9**, BIC = **657.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2040** | 0.5005 | ±1.0010 | **+4.403** | **1.07e-05** | *** |
| Education: graduate level (vs college) | -0.0643 | 0.1122 | ±0.2244 | -0.573 | 0.5667 |  |
| Education: high school or below (vs college) | +0.4046 | 0.2777 | ±0.5554 | +1.457 | 0.1451 |  |
| Site: UCSD (vs UAB) | -0.1372 | 0.1695 | ±0.3390 | -0.809 | 0.4183 |  |
| **Site: UW (vs UAB)** | **-0.4907** | 0.1620 | ±0.3240 | **-3.029** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0412 | 0.1581 | ±0.3162 | -0.261 | 0.7943 |  |
| Season: summer (vs autumn) | +0.0557 | 0.1529 | ±0.3057 | +0.364 | 0.7158 |  |
| Season: winter (vs autumn) | -0.0075 | 0.1561 | ±0.3121 | -0.048 | 0.9615 |  |
| **Age (years)** | **-0.0109** | 0.0051 | ±0.0102 | **-2.122** | **0.0339** | * |
| BMI (kg/m2) | +0.0186 | 0.0103 | ±0.0206 | +1.803 | 0.0713 | . |
| Hypertension | -0.0635 | 0.1242 | ±0.2484 | -0.512 | 0.6090 |  |
| High cholesterol | +0.1694 | 0.1121 | ±0.2242 | +1.511 | 0.1307 |  |
| Kidney disease | -0.2281 | 0.2042 | ±0.4084 | -1.117 | 0.2640 |  |
| Circulatory disease | +0.2730 | 0.2053 | ±0.4105 | +1.330 | 0.1835 |  |
| SD of daily means (mg/dL) | -0.0149 | 0.0109 | ±0.0218 | -1.364 | 0.1727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **241**, R² = **0.1641**, Adj R² = **0.1123**, F-statistic = **3.17** (p = **1.45e-04**), Residual SE = **0.826** on **226** df, AIC = **606.2**, BIC = **658.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9043** | 0.5875 | ±1.1750 | **+3.241** | **0.0012** | ** |
| Education: graduate level (vs college) | -0.0494 | 0.1118 | ±0.2236 | -0.442 | 0.6588 |  |
| Education: high school or below (vs college) | +0.4057 | 0.2808 | ±0.5616 | +1.445 | 0.1485 |  |
| Site: UCSD (vs UAB) | -0.1385 | 0.1705 | ±0.3410 | -0.812 | 0.4168 |  |
| **Site: UW (vs UAB)** | **-0.4910** | 0.1620 | ±0.3239 | **-3.032** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.0697 | 0.1533 | ±0.3066 | -0.454 | 0.6495 |  |
| Season: summer (vs autumn) | +0.0423 | 0.1571 | ±0.3142 | +0.269 | 0.7876 |  |
| Season: winter (vs autumn) | -0.0223 | 0.1543 | ±0.3087 | -0.144 | 0.8851 |  |
| **Age (years)** | **-0.0113** | 0.0052 | ±0.0103 | **-2.199** | **0.0279** | * |
| BMI (kg/m2) | +0.0186 | 0.0104 | ±0.0209 | +1.778 | 0.0754 | . |
| Hypertension | -0.0579 | 0.1246 | ±0.2491 | -0.465 | 0.6419 |  |
| High cholesterol | +0.1768 | 0.1116 | ±0.2232 | +1.585 | 0.1130 |  |
| Kidney disease | -0.2293 | 0.2065 | ±0.4130 | -1.110 | 0.2669 |  |
| Circulatory disease | +0.2772 | 0.2090 | ±0.4181 | +1.326 | 0.1849 |  |
| Time in range 70-180, pooled (%) | +0.0023 | 0.0032 | ±0.0065 | +0.720 | 0.4713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **241**, R² = **0.1638**, Adj R² = **0.1120**, F-statistic = **3.16** (p = **1.50e-04**), Residual SE = **0.826** on **226** df, AIC = **606.3**, BIC = **658.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9282** | 0.5909 | ±1.1817 | **+3.263** | **0.0011** | ** |
| Education: graduate level (vs college) | -0.0496 | 0.1119 | ±0.2237 | -0.443 | 0.6576 |  |
| Education: high school or below (vs college) | +0.4030 | 0.2805 | ±0.5610 | +1.436 | 0.1509 |  |
| Site: UCSD (vs UAB) | -0.1383 | 0.1705 | ±0.3411 | -0.811 | 0.4174 |  |
| **Site: UW (vs UAB)** | **-0.4913** | 0.1621 | ±0.3241 | **-3.031** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.0692 | 0.1533 | ±0.3067 | -0.451 | 0.6519 |  |
| Season: summer (vs autumn) | +0.0439 | 0.1572 | ±0.3144 | +0.280 | 0.7798 |  |
| Season: winter (vs autumn) | -0.0218 | 0.1545 | ±0.3090 | -0.141 | 0.8879 |  |
| **Age (years)** | **-0.0113** | 0.0052 | ±0.0103 | **-2.197** | **0.0280** | * |
| BMI (kg/m2) | +0.0185 | 0.0105 | ±0.0210 | +1.761 | 0.0783 | . |
| Hypertension | -0.0580 | 0.1245 | ±0.2491 | -0.466 | 0.6415 |  |
| High cholesterol | +0.1767 | 0.1116 | ±0.2232 | +1.584 | 0.1132 |  |
| Kidney disease | -0.2298 | 0.2069 | ±0.4138 | -1.111 | 0.2666 |  |
| Circulatory disease | +0.2755 | 0.2087 | ±0.4174 | +1.320 | 0.1869 |  |
| Avg. daily time in range 70-180 (%) | +0.0021 | 0.0032 | ±0.0063 | +0.654 | 0.5129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.1631**, Adj R² = **0.1113**, F-statistic = **3.15** (p = **1.60e-04**), Residual SE = **0.826** on **226** df, AIC = **606.4**, BIC = **658.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1444** | 0.5015 | ±1.0030 | **+4.276** | **1.90e-05** | *** |
| Education: graduate level (vs college) | -0.0585 | 0.1134 | ±0.2268 | -0.516 | 0.6061 |  |
| Education: high school or below (vs college) | +0.3766 | 0.2877 | ±0.5755 | +1.309 | 0.1906 |  |
| Site: UCSD (vs UAB) | -0.1312 | 0.1708 | ±0.3416 | -0.768 | 0.4425 |  |
| **Site: UW (vs UAB)** | **-0.4920** | 0.1619 | ±0.3237 | **-3.040** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.0720 | 0.1534 | ±0.3069 | -0.469 | 0.6390 |  |
| Season: summer (vs autumn) | +0.0535 | 0.1573 | ±0.3146 | +0.340 | 0.7338 |  |
| Season: winter (vs autumn) | -0.0208 | 0.1580 | ±0.3161 | -0.131 | 0.8954 |  |
| **Age (years)** | **-0.0112** | 0.0052 | ±0.0105 | **-2.141** | **0.0323** | * |
| BMI (kg/m2) | +0.0177 | 0.0103 | ±0.0207 | +1.709 | 0.0874 | . |
| Hypertension | -0.0607 | 0.1242 | ±0.2484 | -0.488 | 0.6253 |  |
| High cholesterol | +0.1714 | 0.1120 | ±0.2240 | +1.530 | 0.1260 |  |
| Kidney disease | -0.2325 | 0.2081 | ±0.4162 | -1.117 | 0.2639 |  |
| Circulatory disease | +0.2647 | 0.2052 | ±0.4104 | +1.290 | 0.1970 |  |
| Any reading < 54 during wear (0/1) | -0.0543 | 0.1369 | ±0.2738 | -0.396 | 0.6918 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.1625**, Adj R² = **0.1106**, F-statistic = **3.13** (p = **1.70e-04**), Residual SE = **0.827** on **226** df, AIC = **606.6**, BIC = **658.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1390** | 0.5073 | ±1.0146 | **+4.217** | **2.48e-05** | *** |
| Education: graduate level (vs college) | -0.0557 | 0.1132 | ±0.2263 | -0.492 | 0.6226 |  |
| Education: high school or below (vs college) | +0.3831 | 0.2761 | ±0.5521 | +1.388 | 0.1653 |  |
| Site: UCSD (vs UAB) | -0.1334 | 0.1721 | ±0.3441 | -0.775 | 0.4381 |  |
| **Site: UW (vs UAB)** | **-0.4925** | 0.1647 | ±0.3294 | **-2.991** | **0.0028** | ** |
| Season: spring (vs autumn) | -0.0692 | 0.1529 | ±0.3059 | -0.453 | 0.6508 |  |
| Season: summer (vs autumn) | +0.0568 | 0.1545 | ±0.3089 | +0.368 | 0.7129 |  |
| Season: winter (vs autumn) | -0.0158 | 0.1559 | ±0.3118 | -0.101 | 0.9192 |  |
| **Age (years)** | **-0.0112** | 0.0051 | ±0.0103 | **-2.183** | **0.0290** | * |
| BMI (kg/m2) | +0.0173 | 0.0103 | ±0.0205 | +1.685 | 0.0920 | . |
| Hypertension | -0.0605 | 0.1243 | ±0.2486 | -0.487 | 0.6263 |  |
| High cholesterol | +0.1740 | 0.1118 | ±0.2236 | +1.556 | 0.1198 |  |
| Kidney disease | -0.2388 | 0.2088 | ±0.4176 | -1.143 | 0.2529 |  |
| Circulatory disease | +0.2642 | 0.2054 | ±0.4107 | +1.287 | 0.1982 |  |
| Time < 54 (%) | -0.0103 | 0.0772 | ±0.1545 | -0.133 | 0.8939 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.1624**, Adj R² = **0.1106**, F-statistic = **3.13** (p = **1.71e-04**), Residual SE = **0.827** on **226** df, AIC = **606.6**, BIC = **658.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1365** | 0.5072 | ±1.0143 | **+4.213** | **2.52e-05** | *** |
| Education: graduate level (vs college) | -0.0549 | 0.1132 | ±0.2264 | -0.485 | 0.6276 |  |
| Education: high school or below (vs college) | +0.3841 | 0.2760 | ±0.5520 | +1.392 | 0.1640 |  |
| Site: UCSD (vs UAB) | -0.1326 | 0.1721 | ±0.3443 | -0.771 | 0.4410 |  |
| **Site: UW (vs UAB)** | **-0.4916** | 0.1651 | ±0.3302 | **-2.978** | **0.0029** | ** |
| Season: spring (vs autumn) | -0.0691 | 0.1529 | ±0.3058 | -0.452 | 0.6514 |  |
| Season: summer (vs autumn) | +0.0568 | 0.1545 | ±0.3090 | +0.367 | 0.7133 |  |
| Season: winter (vs autumn) | -0.0164 | 0.1561 | ±0.3122 | -0.105 | 0.9166 |  |
| **Age (years)** | **-0.0112** | 0.0051 | ±0.0103 | **-2.189** | **0.0286** | * |
| BMI (kg/m2) | +0.0173 | 0.0102 | ±0.0204 | +1.697 | 0.0897 | . |
| Hypertension | -0.0602 | 0.1243 | ±0.2487 | -0.484 | 0.6283 |  |
| High cholesterol | +0.1744 | 0.1119 | ±0.2238 | +1.559 | 0.1191 |  |
| Kidney disease | -0.2386 | 0.2088 | ±0.4176 | -1.143 | 0.2532 |  |
| Circulatory disease | +0.2645 | 0.2054 | ±0.4109 | +1.287 | 0.1979 |  |
| Avg. daily time < 54 (%) | -0.0086 | 0.0567 | ±0.1134 | -0.151 | 0.8801 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.1635**, Adj R² = **0.1117**, F-statistic = **3.16** (p = **1.53e-04**), Residual SE = **0.826** on **226** df, AIC = **606.3**, BIC = **658.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1389** | 0.5051 | ±1.0102 | **+4.235** | **2.29e-05** | *** |
| Education: graduate level (vs college) | -0.0618 | 0.1142 | ±0.2284 | -0.541 | 0.5884 |  |
| Education: high school or below (vs college) | +0.3731 | 0.2807 | ±0.5614 | +1.329 | 0.1838 |  |
| Site: UCSD (vs UAB) | -0.1352 | 0.1708 | ±0.3416 | -0.792 | 0.4286 |  |
| **Site: UW (vs UAB)** | **-0.4984** | 0.1634 | ±0.3269 | **-3.049** | **0.0023** | ** |
| Season: spring (vs autumn) | -0.0695 | 0.1530 | ±0.3061 | -0.454 | 0.6495 |  |
| Season: summer (vs autumn) | +0.0514 | 0.1566 | ±0.3132 | +0.328 | 0.7426 |  |
| Season: winter (vs autumn) | -0.0135 | 0.1564 | ±0.3127 | -0.086 | 0.9314 |  |
| **Age (years)** | **-0.0112** | 0.0052 | ±0.0103 | **-2.160** | **0.0308** | * |
| BMI (kg/m2) | +0.0179 | 0.0103 | ±0.0205 | +1.744 | 0.0812 | . |
| Hypertension | -0.0628 | 0.1245 | ±0.2490 | -0.504 | 0.6141 |  |
| High cholesterol | +0.1664 | 0.1137 | ±0.2273 | +1.464 | 0.1432 |  |
| Kidney disease | -0.2366 | 0.2102 | ±0.4203 | -1.126 | 0.2604 |  |
| Circulatory disease | +0.2621 | 0.2056 | ±0.4112 | +1.275 | 0.2024 |  |
| Time 54-69, pooled (%) | -0.0240 | 0.0986 | ±0.1973 | -0.244 | 0.8074 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **241**, R² = **0.1633**, Adj R² = **0.1114**, F-statistic = **3.15** (p = **1.58e-04**), Residual SE = **0.826** on **226** df, AIC = **606.4**, BIC = **658.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1373** | 0.5052 | ±1.0103 | **+4.231** | **2.33e-05** | *** |
| Education: graduate level (vs college) | -0.0608 | 0.1147 | ±0.2294 | -0.530 | 0.5962 |  |
| Education: high school or below (vs college) | +0.3747 | 0.2811 | ±0.5622 | +1.333 | 0.1825 |  |
| Site: UCSD (vs UAB) | -0.1349 | 0.1709 | ±0.3419 | -0.789 | 0.4301 |  |
| **Site: UW (vs UAB)** | **-0.4981** | 0.1638 | ±0.3276 | **-3.041** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.0688 | 0.1530 | ±0.3060 | -0.450 | 0.6529 |  |
| Season: summer (vs autumn) | +0.0523 | 0.1567 | ±0.3135 | +0.334 | 0.7385 |  |
| Season: winter (vs autumn) | -0.0126 | 0.1560 | ±0.3119 | -0.081 | 0.9357 |  |
| **Age (years)** | **-0.0112** | 0.0052 | ±0.0104 | **-2.154** | **0.0313** | * |
| BMI (kg/m2) | +0.0178 | 0.0102 | ±0.0205 | +1.736 | 0.0825 | . |
| Hypertension | -0.0626 | 0.1245 | ±0.2489 | -0.503 | 0.6150 |  |
| High cholesterol | +0.1672 | 0.1146 | ±0.2293 | +1.459 | 0.1447 |  |
| Kidney disease | -0.2371 | 0.2097 | ±0.4193 | -1.131 | 0.2580 |  |
| Circulatory disease | +0.2624 | 0.2057 | ±0.4114 | +1.276 | 0.2021 |  |
| Avg. daily time 54-69 (%) | -0.0198 | 0.1008 | ±0.2016 | -0.197 | 0.8440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **241**, R² = **0.1632**, Adj R² = **0.1114**, F-statistic = **3.15** (p = **1.59e-04**), Residual SE = **0.826** on **226** df, AIC = **606.4**, BIC = **658.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1436** | 0.5059 | ±1.0119 | **+4.237** | **2.27e-05** | *** |
| Education: graduate level (vs college) | -0.0608 | 0.1140 | ±0.2281 | -0.533 | 0.5939 |  |
| Education: high school or below (vs college) | +0.3748 | 0.2788 | ±0.5576 | +1.344 | 0.1788 |  |
| Site: UCSD (vs UAB) | -0.1362 | 0.1717 | ±0.3434 | -0.793 | 0.4276 |  |
| **Site: UW (vs UAB)** | **-0.4985** | 0.1647 | ±0.3294 | **-3.026** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0694 | 0.1528 | ±0.3056 | -0.454 | 0.6498 |  |
| Season: summer (vs autumn) | +0.0535 | 0.1551 | ±0.3103 | +0.345 | 0.7304 |  |
| Season: winter (vs autumn) | -0.0126 | 0.1560 | ±0.3120 | -0.081 | 0.9358 |  |
| **Age (years)** | **-0.0111** | 0.0052 | ±0.0103 | **-2.153** | **0.0313** | * |
| BMI (kg/m2) | +0.0175 | 0.0102 | ±0.0204 | +1.719 | 0.0856 | . |
| Hypertension | -0.0628 | 0.1244 | ±0.2488 | -0.505 | 0.6137 |  |
| High cholesterol | +0.1680 | 0.1123 | ±0.2246 | +1.496 | 0.1346 |  |
| Kidney disease | -0.2379 | 0.2093 | ±0.4186 | -1.137 | 0.2556 |  |
| Circulatory disease | +0.2627 | 0.2054 | ±0.4107 | +1.279 | 0.2009 |  |
| Time < 70 (%) | -0.0135 | 0.0400 | ±0.0800 | -0.337 | 0.7363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **241**, R² = **0.1630**, Adj R² = **0.1111**, F-statistic = **3.14** (p = **1.63e-04**), Residual SE = **0.826** on **226** df, AIC = **606.5**, BIC = **658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1398** | 0.5057 | ±1.0114 | **+4.231** | **2.32e-05** | *** |
| Education: graduate level (vs college) | -0.0595 | 0.1143 | ±0.2285 | -0.521 | 0.6027 |  |
| Education: high school or below (vs college) | +0.3767 | 0.2792 | ±0.5585 | +1.349 | 0.1774 |  |
| Site: UCSD (vs UAB) | -0.1352 | 0.1716 | ±0.3432 | -0.788 | 0.4309 |  |
| **Site: UW (vs UAB)** | **-0.4976** | 0.1648 | ±0.3296 | **-3.019** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0688 | 0.1529 | ±0.3058 | -0.450 | 0.6528 |  |
| Season: summer (vs autumn) | +0.0537 | 0.1555 | ±0.3110 | +0.345 | 0.7298 |  |
| Season: winter (vs autumn) | -0.0125 | 0.1560 | ±0.3120 | -0.080 | 0.9361 |  |
| **Age (years)** | **-0.0112** | 0.0052 | ±0.0104 | **-2.155** | **0.0312** | * |
| BMI (kg/m2) | +0.0175 | 0.0102 | ±0.0204 | +1.723 | 0.0848 | . |
| Hypertension | -0.0624 | 0.1244 | ±0.2488 | -0.501 | 0.6161 |  |
| High cholesterol | +0.1687 | 0.1131 | ±0.2262 | +1.492 | 0.1358 |  |
| Kidney disease | -0.2380 | 0.2090 | ±0.4180 | -1.139 | 0.2549 |  |
| Circulatory disease | +0.2631 | 0.2055 | ±0.4109 | +1.281 | 0.2003 |  |
| Avg. daily time < 70 (%) | -0.0117 | 0.0504 | ±0.1007 | -0.233 | 0.8161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.1629**, Adj R² = **0.1111**, F-statistic = **3.14** (p = **1.63e-04**), Residual SE = **0.826** on **226** df, AIC = **606.5**, BIC = **658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9456** | 0.5366 | ±1.0731 | **+3.626** | **2.88e-04** | *** |
| Education: graduate level (vs college) | -0.0541 | 0.1120 | ±0.2241 | -0.482 | 0.6295 |  |
| Education: high school or below (vs college) | +0.4008 | 0.2873 | ±0.5746 | +1.395 | 0.1630 |  |
| Site: UCSD (vs UAB) | -0.1343 | 0.1713 | ±0.3426 | -0.784 | 0.4330 |  |
| **Site: UW (vs UAB)** | **-0.4914** | 0.1628 | ±0.3257 | **-3.017** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0680 | 0.1535 | ±0.3069 | -0.443 | 0.6577 |  |
| Season: summer (vs autumn) | +0.0526 | 0.1556 | ±0.3112 | +0.338 | 0.7355 |  |
| Season: winter (vs autumn) | -0.0187 | 0.1552 | ±0.3103 | -0.121 | 0.9038 |  |
| **Age (years)** | **-0.0114** | 0.0051 | ±0.0103 | **-2.208** | **0.0272** | * |
| BMI (kg/m2) | +0.0176 | 0.0101 | ±0.0202 | +1.735 | 0.0827 | . |
| Hypertension | -0.0609 | 0.1248 | ±0.2496 | -0.488 | 0.6253 |  |
| High cholesterol | +0.1738 | 0.1116 | ±0.2232 | +1.557 | 0.1194 |  |
| Kidney disease | -0.2402 | 0.2091 | ±0.4181 | -1.149 | 0.2505 |  |
| Circulatory disease | +0.2753 | 0.2115 | ±0.4229 | +1.302 | 0.1930 |  |
| Time 54-250, pooled (%) | +0.0020 | 0.0033 | ±0.0066 | +0.592 | 0.5540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.1629**, Adj R² = **0.1110**, F-statistic = **3.14** (p = **1.64e-04**), Residual SE = **0.826** on **226** df, AIC = **606.5**, BIC = **658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9515** | 0.5435 | ±1.0869 | **+3.591** | **3.30e-04** | *** |
| Education: graduate level (vs college) | -0.0539 | 0.1120 | ±0.2240 | -0.481 | 0.6303 |  |
| Education: high school or below (vs college) | +0.4003 | 0.2876 | ±0.5751 | +1.392 | 0.1639 |  |
| Site: UCSD (vs UAB) | -0.1342 | 0.1712 | ±0.3425 | -0.784 | 0.4333 |  |
| **Site: UW (vs UAB)** | **-0.4911** | 0.1627 | ±0.3254 | **-3.018** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0682 | 0.1534 | ±0.3068 | -0.445 | 0.6567 |  |
| Season: summer (vs autumn) | +0.0527 | 0.1557 | ±0.3113 | +0.338 | 0.7351 |  |
| Season: winter (vs autumn) | -0.0190 | 0.1551 | ±0.3102 | -0.123 | 0.9024 |  |
| **Age (years)** | **-0.0113** | 0.0051 | ±0.0103 | **-2.208** | **0.0273** | * |
| BMI (kg/m2) | +0.0176 | 0.0101 | ±0.0203 | +1.736 | 0.0825 | . |
| Hypertension | -0.0607 | 0.1247 | ±0.2495 | -0.487 | 0.6263 |  |
| High cholesterol | +0.1738 | 0.1116 | ±0.2232 | +1.557 | 0.1194 |  |
| Kidney disease | -0.2403 | 0.2092 | ±0.4183 | -1.149 | 0.2506 |  |
| Circulatory disease | +0.2749 | 0.2116 | ±0.4232 | +1.299 | 0.1938 |  |
| Avg. daily time 54-250 (%) | +0.0019 | 0.0033 | ±0.0067 | +0.562 | 0.5742 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.1638**, Adj R² = **0.1120**, F-statistic = **3.16** (p = **1.49e-04**), Residual SE = **0.826** on **226** df, AIC = **606.2**, BIC = **658.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1246** | 0.5067 | ±1.0133 | **+4.193** | **2.75e-05** | *** |
| Education: graduate level (vs college) | -0.0454 | 0.1125 | ±0.2250 | -0.403 | 0.6868 |  |
| Education: high school or below (vs college) | +0.3912 | 0.2753 | ±0.5506 | +1.421 | 0.1554 |  |
| Site: UCSD (vs UAB) | -0.1363 | 0.1691 | ±0.3381 | -0.806 | 0.4201 |  |
| **Site: UW (vs UAB)** | **-0.4869** | 0.1619 | ±0.3238 | **-3.008** | **0.0026** | ** |
| Season: spring (vs autumn) | -0.0721 | 0.1547 | ±0.3094 | -0.466 | 0.6412 |  |
| Season: summer (vs autumn) | +0.0439 | 0.1573 | ±0.3145 | +0.279 | 0.7800 |  |
| Season: winter (vs autumn) | -0.0239 | 0.1544 | ±0.3088 | -0.155 | 0.8770 |  |
| **Age (years)** | **-0.0113** | 0.0052 | ±0.0104 | **-2.175** | **0.0296** | * |
| BMI (kg/m2) | +0.0188 | 0.0111 | ±0.0221 | +1.702 | 0.0888 | . |
| Hypertension | -0.0538 | 0.1259 | ±0.2517 | -0.428 | 0.6688 |  |
| High cholesterol | +0.1825 | 0.1145 | ±0.2290 | +1.594 | 0.1109 |  |
| Kidney disease | -0.2214 | 0.2109 | ±0.4219 | -1.049 | 0.2940 |  |
| Circulatory disease | +0.2647 | 0.2050 | ±0.4100 | +1.291 | 0.1966 |  |
| Time 181-250, pooled (%) | -0.0035 | 0.0073 | ±0.0146 | -0.483 | 0.6291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **241**, R² = **0.1635**, Adj R² = **0.1117**, F-statistic = **3.16** (p = **1.54e-04**), Residual SE = **0.826** on **226** df, AIC = **606.3**, BIC = **658.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1258** | 0.5071 | ±1.0142 | **+4.192** | **2.76e-05** | *** |
| Education: graduate level (vs college) | -0.0464 | 0.1127 | ±0.2254 | -0.411 | 0.6807 |  |
| Education: high school or below (vs college) | +0.3896 | 0.2756 | ±0.5512 | +1.414 | 0.1574 |  |
| Site: UCSD (vs UAB) | -0.1365 | 0.1691 | ±0.3382 | -0.807 | 0.4197 |  |
| **Site: UW (vs UAB)** | **-0.4881** | 0.1620 | ±0.3240 | **-3.012** | **0.0026** | ** |
| Season: spring (vs autumn) | -0.0709 | 0.1544 | ±0.3089 | -0.459 | 0.6463 |  |
| Season: summer (vs autumn) | +0.0460 | 0.1572 | ±0.3143 | +0.293 | 0.7699 |  |
| Season: winter (vs autumn) | -0.0227 | 0.1546 | ±0.3092 | -0.147 | 0.8830 |  |
| **Age (years)** | **-0.0113** | 0.0052 | ±0.0104 | **-2.176** | **0.0296** | * |
| BMI (kg/m2) | +0.0186 | 0.0110 | ±0.0221 | +1.685 | 0.0919 | . |
| Hypertension | -0.0547 | 0.1258 | ±0.2516 | -0.435 | 0.6638 |  |
| High cholesterol | +0.1818 | 0.1145 | ±0.2289 | +1.588 | 0.1123 |  |
| Kidney disease | -0.2230 | 0.2116 | ±0.4233 | -1.054 | 0.2920 |  |
| Circulatory disease | +0.2642 | 0.2051 | ±0.4102 | +1.288 | 0.1977 |  |
| Avg. daily time 181-250 (%) | -0.0030 | 0.0070 | ±0.0140 | -0.428 | 0.6688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **241**, R² = **0.1638**, Adj R² = **0.1120**, F-statistic = **3.16** (p = **1.49e-04**), Residual SE = **0.826** on **226** df, AIC = **606.2**, BIC = **658.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1348** | 0.5033 | ±1.0066 | **+4.241** | **2.22e-05** | *** |
| Education: graduate level (vs college) | -0.0487 | 0.1118 | ±0.2237 | -0.435 | 0.6634 |  |
| Education: high school or below (vs college) | +0.4056 | 0.2816 | ±0.5632 | +1.440 | 0.1498 |  |
| Site: UCSD (vs UAB) | -0.1370 | 0.1703 | ±0.3406 | -0.805 | 0.4209 |  |
| **Site: UW (vs UAB)** | **-0.4895** | 0.1617 | ±0.3235 | **-3.026** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0696 | 0.1534 | ±0.3067 | -0.454 | 0.6499 |  |
| Season: summer (vs autumn) | +0.0443 | 0.1568 | ±0.3137 | +0.283 | 0.7775 |  |
| Season: winter (vs autumn) | -0.0228 | 0.1543 | ±0.3085 | -0.148 | 0.8827 |  |
| **Age (years)** | **-0.0114** | 0.0052 | ±0.0103 | **-2.201** | **0.0278** | * |
| BMI (kg/m2) | +0.0184 | 0.0104 | ±0.0209 | +1.765 | 0.0775 | . |
| Hypertension | -0.0575 | 0.1245 | ±0.2490 | -0.462 | 0.6440 |  |
| High cholesterol | +0.1780 | 0.1118 | ±0.2235 | +1.592 | 0.1113 |  |
| Kidney disease | -0.2302 | 0.2068 | ±0.4137 | -1.113 | 0.2658 |  |
| Circulatory disease | +0.2763 | 0.2089 | ±0.4179 | +1.322 | 0.1861 |  |
| Time > 180 (%) | -0.0021 | 0.0032 | ±0.0063 | -0.663 | 0.5073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **241**, R² = **0.1636**, Adj R² = **0.1118**, F-statistic = **3.16** (p = **1.53e-04**), Residual SE = **0.826** on **226** df, AIC = **606.3**, BIC = **658.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1337** | 0.5035 | ±1.0069 | **+4.238** | **2.25e-05** | *** |
| Education: graduate level (vs college) | -0.0490 | 0.1119 | ±0.2238 | -0.438 | 0.6615 |  |
| Education: high school or below (vs college) | +0.4030 | 0.2812 | ±0.5624 | +1.433 | 0.1518 |  |
| Site: UCSD (vs UAB) | -0.1371 | 0.1703 | ±0.3407 | -0.805 | 0.4208 |  |
| **Site: UW (vs UAB)** | **-0.4898** | 0.1619 | ±0.3237 | **-3.026** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0693 | 0.1534 | ±0.3067 | -0.452 | 0.6516 |  |
| Season: summer (vs autumn) | +0.0456 | 0.1569 | ±0.3138 | +0.291 | 0.7711 |  |
| Season: winter (vs autumn) | -0.0224 | 0.1544 | ±0.3088 | -0.145 | 0.8848 |  |
| **Age (years)** | **-0.0113** | 0.0052 | ±0.0103 | **-2.199** | **0.0278** | * |
| BMI (kg/m2) | +0.0183 | 0.0105 | ±0.0209 | +1.752 | 0.0798 | . |
| Hypertension | -0.0576 | 0.1245 | ±0.2489 | -0.463 | 0.6435 |  |
| High cholesterol | +0.1778 | 0.1118 | ±0.2236 | +1.591 | 0.1116 |  |
| Kidney disease | -0.2306 | 0.2072 | ±0.4144 | -1.113 | 0.2657 |  |
| Circulatory disease | +0.2748 | 0.2086 | ±0.4173 | +1.317 | 0.1879 |  |
| Avg. daily time > 180 (%) | -0.0019 | 0.0031 | ±0.0062 | -0.608 | 0.5432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **241**, R² = **0.1649**, Adj R² = **0.1131**, F-statistic = **3.19** (p = **1.34e-04**), Residual SE = **0.825** on **226** df, AIC = **605.9**, BIC = **658.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1225** | 0.5038 | ±1.0076 | **+4.213** | **2.52e-05** | *** |
| Education: graduate level (vs college) | -0.0532 | 0.1120 | ±0.2240 | -0.475 | 0.6345 |  |
| Education: high school or below (vs college) | +0.4038 | 0.2792 | ±0.5584 | +1.446 | 0.1481 |  |
| Site: UCSD (vs UAB) | -0.1355 | 0.1698 | ±0.3396 | -0.798 | 0.4249 |  |
| **Site: UW (vs UAB)** | **-0.4905** | 0.1617 | ±0.3234 | **-3.033** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.0624 | 0.1535 | ±0.3070 | -0.407 | 0.6842 |  |
| Season: summer (vs autumn) | +0.0420 | 0.1578 | ±0.3156 | +0.266 | 0.7901 |  |
| Season: winter (vs autumn) | -0.0185 | 0.1546 | ±0.3093 | -0.120 | 0.9045 |  |
| **Age (years)** | **-0.0115** | 0.0052 | ±0.0104 | **-2.221** | **0.0263** | * |
| BMI (kg/m2) | +0.0190 | 0.0105 | ±0.0211 | +1.801 | 0.0717 | . |
| Hypertension | -0.0600 | 0.1242 | ±0.2485 | -0.483 | 0.6293 |  |
| High cholesterol | +0.1804 | 0.1118 | ±0.2236 | +1.613 | 0.1068 |  |
| Kidney disease | -0.2447 | 0.2079 | ±0.4158 | -1.177 | 0.2391 |  |
| Circulatory disease | +0.2761 | 0.2085 | ±0.4169 | +1.324 | 0.1854 |  |
| Nocturnal time > 180 (%) | -0.0026 | 0.0031 | ±0.0061 | -0.865 | 0.3872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.1629**, Adj R² = **0.1110**, F-statistic = **3.14** (p = **1.64e-04**), Residual SE = **0.826** on **226** df, AIC = **606.5**, BIC = **658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1394** | 0.5052 | ±1.0103 | **+4.235** | **2.28e-05** | *** |
| Education: graduate level (vs college) | -0.0537 | 0.1120 | ±0.2239 | -0.479 | 0.6316 |  |
| Education: high school or below (vs college) | +0.4008 | 0.2879 | ±0.5758 | +1.392 | 0.1639 |  |
| Site: UCSD (vs UAB) | -0.1338 | 0.1710 | ±0.3420 | -0.783 | 0.4339 |  |
| **Site: UW (vs UAB)** | **-0.4907** | 0.1625 | ±0.3250 | **-3.020** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0680 | 0.1535 | ±0.3069 | -0.443 | 0.6575 |  |
| Season: summer (vs autumn) | +0.0528 | 0.1556 | ±0.3111 | +0.339 | 0.7342 |  |
| Season: winter (vs autumn) | -0.0191 | 0.1551 | ±0.3102 | -0.123 | 0.9018 |  |
| **Age (years)** | **-0.0114** | 0.0051 | ±0.0103 | **-2.208** | **0.0272** | * |
| BMI (kg/m2) | +0.0176 | 0.0101 | ±0.0203 | +1.736 | 0.0825 | . |
| Hypertension | -0.0607 | 0.1247 | ±0.2494 | -0.487 | 0.6266 |  |
| High cholesterol | +0.1742 | 0.1115 | ±0.2231 | +1.562 | 0.1183 |  |
| Kidney disease | -0.2401 | 0.2090 | ±0.4181 | -1.148 | 0.2508 |  |
| Circulatory disease | +0.2750 | 0.2114 | ±0.4227 | +1.301 | 0.1933 |  |
| Time > 250 (%) | -0.0019 | 0.0033 | ±0.0066 | -0.573 | 0.5665 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 241)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **241**, R² = **0.1629**, Adj R² = **0.1110**, F-statistic = **3.14** (p = **1.64e-04**), Residual SE = **0.826** on **226** df, AIC = **606.5**, BIC = **658.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1385** | 0.5048 | ±1.0096 | **+4.237** | **2.27e-05** | *** |
| Education: graduate level (vs college) | -0.0537 | 0.1120 | ±0.2239 | -0.479 | 0.6317 |  |
| Education: high school or below (vs college) | +0.4004 | 0.2880 | ±0.5760 | +1.390 | 0.1644 |  |
| Site: UCSD (vs UAB) | -0.1338 | 0.1710 | ±0.3420 | -0.783 | 0.4338 |  |
| **Site: UW (vs UAB)** | **-0.4906** | 0.1624 | ±0.3248 | **-3.020** | **0.0025** | ** |
| Season: spring (vs autumn) | -0.0682 | 0.1534 | ±0.3068 | -0.445 | 0.6564 |  |
| Season: summer (vs autumn) | +0.0529 | 0.1556 | ±0.3113 | +0.340 | 0.7341 |  |
| Season: winter (vs autumn) | -0.0194 | 0.1551 | ±0.3101 | -0.125 | 0.9006 |  |
| **Age (years)** | **-0.0114** | 0.0051 | ±0.0103 | **-2.208** | **0.0272** | * |
| BMI (kg/m2) | +0.0176 | 0.0101 | ±0.0203 | +1.737 | 0.0824 | . |
| Hypertension | -0.0606 | 0.1247 | ±0.2494 | -0.486 | 0.6272 |  |
| High cholesterol | +0.1742 | 0.1116 | ±0.2231 | +1.561 | 0.1185 |  |
| Kidney disease | -0.2402 | 0.2092 | ±0.4183 | -1.148 | 0.2508 |  |
| Circulatory disease | +0.2748 | 0.2115 | ±0.4230 | +1.299 | 0.1939 |  |
| Avg. daily time > 250 (%) | -0.0018 | 0.0033 | ±0.0066 | -0.554 | 0.5794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 241; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **241**, R² = **0.3641**, Adj R² = **0.3277**, F-statistic = **10.00** (p = **1.65e-16**), Residual SE = **1.903** on **227** df, AIC = **1007.7**, BIC = **1056.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8565** | 1.0474 | ±2.0948 | **+21.822** | **1.44e-105** | *** |
| Education: graduate level (vs college) | -0.4363 | 0.2572 | ±0.5144 | -1.697 | 0.0898 | . |
| Education: high school or below (vs college) | -0.2579 | 0.5406 | ±1.0811 | -0.477 | 0.6333 |  |
| Site: UCSD (vs UAB) | -0.2124 | 0.3622 | ±0.7245 | -0.586 | 0.5576 |  |
| **Site: UW (vs UAB)** | **-1.3264** | 0.3193 | ±0.6386 | **-4.154** | **3.27e-05** | *** |
| Season: spring (vs autumn) | -0.4261 | 0.3347 | ±0.6693 | -1.273 | 0.2030 |  |
| **Season: summer (vs autumn)** | **+2.2895** | 0.4342 | ±0.8684 | **+5.273** | **1.34e-07** | *** |
| **Season: winter (vs autumn)** | **-1.0791** | 0.3215 | ±0.6429 | **-3.357** | **7.88e-04** | *** |
| **Age (years)** | **+0.0303** | 0.0124 | ±0.0247 | **+2.452** | **0.0142** | * |
| BMI (kg/m2) | -0.0003 | 0.0205 | ±0.0409 | -0.015 | 0.9880 |  |
| Hypertension | +0.0482 | 0.2830 | ±0.5660 | +0.170 | 0.8647 |  |
| High cholesterol | +0.3283 | 0.2610 | ±0.5219 | +1.258 | 0.2084 |  |
| **Kidney disease** | **+1.1482** | 0.4462 | ±0.8924 | **+2.573** | **0.0101** | * |
| Circulatory disease | -0.2697 | 0.3592 | ±0.7184 | -0.751 | 0.4527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **241**, R² = **0.3679**, Adj R² = **0.3288**, F-statistic = **9.40** (p = **2.89e-16**), Residual SE = **1.902** on **226** df, AIC = **1008.3**, BIC = **1060.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.9811** | 1.3708 | ±2.7415 | **+16.036** | **7.21e-58** | *** |
| Education: graduate level (vs college) | -0.4386 | 0.2605 | ±0.5211 | -1.683 | 0.0923 | . |
| Education: high school or below (vs college) | -0.3612 | 0.5591 | ±1.1181 | -0.646 | 0.5182 |  |
| Site: UCSD (vs UAB) | -0.2107 | 0.3607 | ±0.7213 | -0.584 | 0.5591 |  |
| **Site: UW (vs UAB)** | **-1.3367** | 0.3180 | ±0.6361 | **-4.203** | **2.64e-05** | *** |
| Season: spring (vs autumn) | -0.4266 | 0.3410 | ±0.6820 | -1.251 | 0.2109 |  |
| **Season: summer (vs autumn)** | **+2.3146** | 0.4330 | ±0.8659 | **+5.346** | **8.99e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0830** | 0.3206 | ±0.6412 | **-3.378** | **7.30e-04** | *** |
| **Age (years)** | **+0.0300** | 0.0124 | ±0.0248 | **+2.427** | **0.0152** | * |
| BMI (kg/m2) | -0.0028 | 0.0201 | ±0.0401 | -0.141 | 0.8880 |  |
| Hypertension | +0.0466 | 0.2831 | ±0.5663 | +0.165 | 0.8693 |  |
| High cholesterol | +0.3073 | 0.2615 | ±0.5230 | +1.175 | 0.2400 |  |
| **Kidney disease** | **+1.1812** | 0.4416 | ±0.8831 | **+2.675** | **0.0075** | ** |
| Circulatory disease | -0.3616 | 0.3707 | ±0.7413 | -0.975 | 0.3293 |  |
| HbA1c (%) | +0.1655 | 0.1616 | ±0.3232 | +1.024 | 0.3059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **241**, R² = **0.3716**, Adj R² = **0.3327**, F-statistic = **9.55** (p = **1.58e-16**), Residual SE = **1.896** on **226** df, AIC = **1006.8**, BIC = **1059.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.9824** | 1.1463 | ±2.2927 | **+19.176** | **5.84e-82** | *** |
| Education: graduate level (vs college) | -0.4727 | 0.2625 | ±0.5249 | -1.801 | 0.0717 | . |
| Education: high school or below (vs college) | -0.4156 | 0.5465 | ±1.0931 | -0.760 | 0.4470 |  |
| Site: UCSD (vs UAB) | -0.1781 | 0.3600 | ±0.7201 | -0.495 | 0.6209 |  |
| **Site: UW (vs UAB)** | **-1.3339** | 0.3174 | ±0.6348 | **-4.202** | **2.64e-05** | *** |
| Season: spring (vs autumn) | -0.4344 | 0.3380 | ±0.6760 | -1.285 | 0.1987 |  |
| **Season: summer (vs autumn)** | **+2.3644** | 0.4307 | ±0.8614 | **+5.490** | **4.03e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0326** | 0.3195 | ±0.6391 | **-3.232** | **0.0012** | ** |
| **Age (years)** | **+0.0306** | 0.0123 | ±0.0246 | **+2.495** | **0.0126** | * |
| BMI (kg/m2) | -0.0053 | 0.0197 | ±0.0394 | -0.267 | 0.7891 |  |
| Hypertension | +0.0348 | 0.2816 | ±0.5631 | +0.123 | 0.9017 |  |
| High cholesterol | +0.3074 | 0.2591 | ±0.5182 | +1.186 | 0.2355 |  |
| **Kidney disease** | **+1.1401** | 0.4370 | ±0.8740 | **+2.609** | **0.0091** | ** |
| Circulatory disease | -0.3643 | 0.3621 | ±0.7243 | -1.006 | 0.3144 |  |
| Mean glucose (mg/dL) | +0.0073 | 0.0041 | ±0.0082 | +1.780 | 0.0751 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **241**, R² = **0.3716**, Adj R² = **0.3327**, F-statistic = **9.55** (p = **1.58e-16**), Residual SE = **1.896** on **226** df, AIC = **1006.8**, BIC = **1059.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20.9778** | 1.4728 | ±2.9455 | **+14.244** | **4.90e-46** | *** |
| Education: graduate level (vs college) | -0.4727 | 0.2625 | ±0.5249 | -1.801 | 0.0717 | . |
| Education: high school or below (vs college) | -0.4156 | 0.5465 | ±1.0931 | -0.760 | 0.4470 |  |
| Site: UCSD (vs UAB) | -0.1781 | 0.3600 | ±0.7201 | -0.495 | 0.6209 |  |
| **Site: UW (vs UAB)** | **-1.3339** | 0.3174 | ±0.6348 | **-4.202** | **2.64e-05** | *** |
| Season: spring (vs autumn) | -0.4344 | 0.3380 | ±0.6760 | -1.285 | 0.1987 |  |
| **Season: summer (vs autumn)** | **+2.3644** | 0.4307 | ±0.8614 | **+5.490** | **4.03e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0326** | 0.3195 | ±0.6391 | **-3.232** | **0.0012** | ** |
| **Age (years)** | **+0.0306** | 0.0123 | ±0.0246 | **+2.495** | **0.0126** | * |
| BMI (kg/m2) | -0.0053 | 0.0197 | ±0.0394 | -0.267 | 0.7891 |  |
| Hypertension | +0.0348 | 0.2816 | ±0.5631 | +0.123 | 0.9017 |  |
| High cholesterol | +0.3074 | 0.2591 | ±0.5182 | +1.186 | 0.2355 |  |
| **Kidney disease** | **+1.1401** | 0.4370 | ±0.8740 | **+2.609** | **0.0091** | ** |
| Circulatory disease | -0.3643 | 0.3621 | ±0.7243 | -1.006 | 0.3144 |  |
| GMI (%) | +0.3035 | 0.1705 | ±0.3411 | +1.780 | 0.0751 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **241**, R² = **0.3693**, Adj R² = **0.3302**, F-statistic = **9.45** (p = **2.33e-16**), Residual SE = **1.900** on **226** df, AIC = **1007.8**, BIC = **1060.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.2339** | 1.1225 | ±2.2450 | **+19.807** | **2.58e-87** | *** |
| Education: graduate level (vs college) | -0.4527 | 0.2604 | ±0.5207 | -1.739 | 0.0821 | . |
| Education: high school or below (vs college) | -0.3742 | 0.5519 | ±1.1037 | -0.678 | 0.4977 |  |
| Site: UCSD (vs UAB) | -0.2019 | 0.3591 | ±0.7181 | -0.562 | 0.5739 |  |
| **Site: UW (vs UAB)** | **-1.3286** | 0.3180 | ±0.6360 | **-4.178** | **2.94e-05** | *** |
| Season: spring (vs autumn) | -0.4475 | 0.3379 | ±0.6758 | -1.324 | 0.1854 |  |
| **Season: summer (vs autumn)** | **+2.3564** | 0.4329 | ±0.8658 | **+5.443** | **5.24e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0551** | 0.3213 | ±0.6426 | **-3.284** | **0.0010** | ** |
| **Age (years)** | **+0.0311** | 0.0123 | ±0.0246 | **+2.527** | **0.0115** | * |
| BMI (kg/m2) | -0.0053 | 0.0199 | ±0.0399 | -0.267 | 0.7896 |  |
| Hypertension | +0.0394 | 0.2819 | ±0.5638 | +0.140 | 0.8889 |  |
| High cholesterol | +0.3099 | 0.2606 | ±0.5211 | +1.190 | 0.2342 |  |
| **Kidney disease** | **+1.1872** | 0.4382 | ±0.8764 | **+2.709** | **0.0067** | ** |
| Circulatory disease | -0.3348 | 0.3616 | ±0.7231 | -0.926 | 0.3545 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0054 | 0.0037 | ±0.0073 | +1.485 | 0.1374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **241**, R² = **0.3829**, Adj R² = **0.3447**, F-statistic = **10.02** (p = **2.44e-17**), Residual SE = **1.879** on **226** df, AIC = **1002.5**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.7436** | 1.1272 | ±2.2544 | **+19.290** | **6.50e-83** | *** |
| Education: graduate level (vs college) | -0.4441 | 0.2542 | ±0.5083 | -1.747 | 0.0806 | . |
| Education: high school or below (vs college) | -0.2924 | 0.5117 | ±1.0235 | -0.571 | 0.5678 |  |
| Site: UCSD (vs UAB) | -0.1203 | 0.3584 | ±0.7169 | -0.336 | 0.7371 |  |
| **Site: UW (vs UAB)** | **-1.2831** | 0.3133 | ±0.6267 | **-4.095** | **4.22e-05** | *** |
| Season: spring (vs autumn) | -0.4318 | 0.3372 | ±0.6744 | -1.281 | 0.2003 |  |
| **Season: summer (vs autumn)** | **+2.3427** | 0.4259 | ±0.8517 | **+5.501** | **3.78e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0370** | 0.3170 | ±0.6339 | **-3.272** | **0.0011** | ** |
| **Age (years)** | **+0.0292** | 0.0122 | ±0.0244 | **+2.395** | **0.0166** | * |
| BMI (kg/m2) | -0.0085 | 0.0201 | ±0.0401 | -0.422 | 0.6731 |  |
| Hypertension | +0.0069 | 0.2776 | ±0.5551 | +0.025 | 0.9802 |  |
| High cholesterol | +0.4083 | 0.2560 | ±0.5119 | +1.595 | 0.1107 |  |
| **Kidney disease** | **+0.9553** | 0.4449 | ±0.8899 | **+2.147** | **0.0318** | * |
| Circulatory disease | -0.4142 | 0.3746 | ±0.7492 | -1.106 | 0.2688 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0444** | 0.0171 | ±0.0342 | **+2.590** | **0.0096** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **241**, R² = **0.3824**, Adj R² = **0.3441**, F-statistic = **9.99** (p = **2.67e-17**), Residual SE = **1.880** on **226** df, AIC = **1002.7**, BIC = **1055.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.8409** | 1.1003 | ±2.2007 | **+19.849** | **1.11e-87** | *** |
| Education: graduate level (vs college) | -0.4623 | 0.2552 | ±0.5103 | -1.812 | 0.0700 | . |
| Education: high school or below (vs college) | -0.2644 | 0.5110 | ±1.0220 | -0.517 | 0.6048 |  |
| Site: UCSD (vs UAB) | -0.1226 | 0.3565 | ±0.7131 | -0.344 | 0.7310 |  |
| **Site: UW (vs UAB)** | **-1.2914** | 0.3148 | ±0.6296 | **-4.102** | **4.09e-05** | *** |
| Season: spring (vs autumn) | -0.4022 | 0.3360 | ±0.6720 | -1.197 | 0.2313 |  |
| **Season: summer (vs autumn)** | **+2.3382** | 0.4260 | ±0.8519 | **+5.489** | **4.03e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0293** | 0.3169 | ±0.6338 | **-3.248** | **0.0012** | ** |
| **Age (years)** | **+0.0294** | 0.0123 | ±0.0245 | **+2.400** | **0.0164** | * |
| BMI (kg/m2) | -0.0095 | 0.0203 | ±0.0405 | -0.467 | 0.6403 |  |
| Hypertension | -0.0048 | 0.2786 | ±0.5573 | -0.017 | 0.9861 |  |
| High cholesterol | +0.4030 | 0.2562 | ±0.5124 | +1.573 | 0.1157 |  |
| **Kidney disease** | **+0.9655** | 0.4507 | ±0.9015 | **+2.142** | **0.0322** | * |
| Circulatory disease | -0.4154 | 0.3762 | ±0.7523 | -1.104 | 0.2694 |  |
| **Avg. daily SD (mg/dL)** | **+0.0462** | 0.0176 | ±0.0353 | **+2.619** | **0.0088** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **241**, R² = **0.3724**, Adj R² = **0.3335**, F-statistic = **9.58** (p = **1.40e-16**), Residual SE = **1.895** on **226** df, AIC = **1006.6**, BIC = **1058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.9050** | 1.2117 | ±2.4234 | **+18.078** | **4.75e-73** | *** |
| Education: graduate level (vs college) | -0.3983 | 0.2538 | ±0.5075 | -1.570 | 0.1165 |  |
| Education: high school or below (vs college) | -0.1522 | 0.5288 | ±1.0575 | -0.288 | 0.7735 |  |
| Site: UCSD (vs UAB) | -0.1637 | 0.3616 | ±0.7232 | -0.453 | 0.6508 |  |
| **Site: UW (vs UAB)** | **-1.2714** | 0.3157 | ±0.6314 | **-4.027** | **5.64e-05** | *** |
| Season: spring (vs autumn) | -0.4269 | 0.3362 | ±0.6724 | -1.270 | 0.2041 |  |
| **Season: summer (vs autumn)** | **+2.2662** | 0.4298 | ±0.8596 | **+5.272** | **1.35e-07** | *** |
| **Season: winter (vs autumn)** | **-1.0925** | 0.3193 | ±0.6386 | **-3.422** | **6.23e-04** | *** |
| **Age (years)** | **+0.0290** | 0.0123 | ±0.0246 | **+2.359** | **0.0183** | * |
| BMI (kg/m2) | -0.0018 | 0.0207 | ±0.0415 | -0.089 | 0.9293 |  |
| Hypertension | +0.0402 | 0.2815 | ±0.5631 | +0.143 | 0.8864 |  |
| High cholesterol | +0.4186 | 0.2628 | ±0.5257 | +1.593 | 0.1113 |  |
| **Kidney disease** | **+1.0283** | 0.4591 | ±0.9182 | **+2.240** | **0.0251** | * |
| Circulatory disease | -0.2883 | 0.3677 | ±0.7354 | -0.784 | 0.4330 |  |
| CV (%) | +0.0449 | 0.0264 | ±0.0528 | +1.698 | 0.0895 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **241**, R² = **0.3729**, Adj R² = **0.3341**, F-statistic = **9.60** (p = **1.28e-16**), Residual SE = **1.894** on **226** df, AIC = **1006.4**, BIC = **1058.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0081** | 1.1909 | ±2.3818 | **+20.159** | **2.23e-90** | *** |
| Education: graduate level (vs college) | -0.4193 | 0.2540 | ±0.5079 | -1.651 | 0.0988 | . |
| Education: high school or below (vs college) | -0.1705 | 0.5293 | ±1.0587 | -0.322 | 0.7474 |  |
| Site: UCSD (vs UAB) | -0.1739 | 0.3603 | ±0.7206 | -0.483 | 0.6293 |  |
| **Site: UW (vs UAB)** | **-1.2738** | 0.3165 | ±0.6330 | **-4.024** | **5.71e-05** | *** |
| Season: spring (vs autumn) | -0.4309 | 0.3356 | ±0.6711 | -1.284 | 0.1991 |  |
| **Season: summer (vs autumn)** | **+2.2511** | 0.4286 | ±0.8573 | **+5.252** | **1.51e-07** | *** |
| **Season: winter (vs autumn)** | **-1.1148** | 0.3191 | ±0.6382 | **-3.494** | **4.76e-04** | *** |
| **Age (years)** | **+0.0294** | 0.0123 | ±0.0245 | **+2.396** | **0.0166** | * |
| BMI (kg/m2) | -0.0010 | 0.0206 | ±0.0413 | -0.048 | 0.9614 |  |
| Hypertension | +0.0229 | 0.2824 | ±0.5647 | +0.081 | 0.9353 |  |
| High cholesterol | +0.4059 | 0.2612 | ±0.5224 | +1.554 | 0.1202 |  |
| **Kidney disease** | **+1.0416** | 0.4551 | ±0.9102 | **+2.289** | **0.0221** | * |
| Circulatory disease | -0.2868 | 0.3705 | ±0.7410 | -0.774 | 0.4388 |  |
| Mean / SD ratio | -0.2368 | 0.1317 | ±0.2634 | -1.798 | 0.0721 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **241**, R² = **0.3739**, Adj R² = **0.3351**, F-statistic = **9.64** (p = **1.08e-16**), Residual SE = **1.893** on **226** df, AIC = **1006.0**, BIC = **1058.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0133** | 1.2005 | ±2.4009 | **+20.003** | **5.17e-89** | *** |
| Education: graduate level (vs college) | -0.4354 | 0.2544 | ±0.5088 | -1.711 | 0.0871 | . |
| Education: high school or below (vs college) | -0.1619 | 0.5273 | ±1.0546 | -0.307 | 0.7589 |  |
| Site: UCSD (vs UAB) | -0.1789 | 0.3591 | ±0.7182 | -0.498 | 0.6184 |  |
| **Site: UW (vs UAB)** | **-1.2704** | 0.3172 | ±0.6344 | **-4.005** | **6.20e-05** | *** |
| Season: spring (vs autumn) | -0.4003 | 0.3362 | ±0.6724 | -1.191 | 0.2338 |  |
| **Season: summer (vs autumn)** | **+2.2526** | 0.4275 | ±0.8549 | **+5.270** | **1.36e-07** | *** |
| **Season: winter (vs autumn)** | **-1.1071** | 0.3194 | ±0.6387 | **-3.467** | **5.27e-04** | *** |
| **Age (years)** | **+0.0289** | 0.0123 | ±0.0246 | **+2.352** | **0.0187** | * |
| BMI (kg/m2) | -0.0022 | 0.0207 | ±0.0413 | -0.109 | 0.9135 |  |
| Hypertension | +0.0124 | 0.2822 | ±0.5645 | +0.044 | 0.9650 |  |
| High cholesterol | +0.4042 | 0.2589 | ±0.5178 | +1.561 | 0.1184 |  |
| **Kidney disease** | **+1.0324** | 0.4566 | ±0.9132 | **+2.261** | **0.0238** | * |
| Circulatory disease | -0.2803 | 0.3740 | ±0.7481 | -0.750 | 0.4536 |  |
| Avg. daily mean/SD | -0.1932 | 0.0996 | ±0.1993 | -1.939 | 0.0525 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **241**, R² = **0.3721**, Adj R² = **0.3332**, F-statistic = **9.57** (p = **1.46e-16**), Residual SE = **1.895** on **226** df, AIC = **1006.7**, BIC = **1058.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.7511** | 1.1980 | ±2.3959 | **+18.157** | **1.14e-73** | *** |
| Education: graduate level (vs college) | -0.3877 | 0.2551 | ±0.5102 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | -0.2349 | 0.5259 | ±1.0517 | -0.447 | 0.6551 |  |
| Site: UCSD (vs UAB) | -0.1207 | 0.3595 | ±0.7190 | -0.336 | 0.7372 |  |
| **Site: UW (vs UAB)** | **-1.2033** | 0.3208 | ±0.6416 | **-3.751** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.4472 | 0.3364 | ±0.6729 | -1.329 | 0.1838 |  |
| **Season: summer (vs autumn)** | **+2.3429** | 0.4394 | ±0.8789 | **+5.332** | **9.73e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0514** | 0.3196 | ±0.6392 | **-3.290** | **0.0010** | ** |
| **Age (years)** | **+0.0305** | 0.0125 | ±0.0251 | **+2.429** | **0.0152** | * |
| BMI (kg/m2) | -0.0071 | 0.0215 | ±0.0431 | -0.329 | 0.7424 |  |
| Hypertension | +0.1146 | 0.2858 | ±0.5717 | +0.401 | 0.6886 |  |
| High cholesterol | +0.4194 | 0.2591 | ±0.5181 | +1.619 | 0.1055 |  |
| **Kidney disease** | **+1.1558** | 0.4480 | ±0.8960 | **+2.580** | **0.0099** | ** |
| Circulatory disease | -0.3178 | 0.3781 | ±0.7562 | -0.841 | 0.4006 |  |
| MAG (mg/dL/h) | +0.0249 | 0.0153 | ±0.0306 | +1.626 | 0.1039 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **241**, R² = **0.3842**, Adj R² = **0.3461**, F-statistic = **10.07** (p = **1.95e-17**), Residual SE = **1.877** on **226** df, AIC = **1002.0**, BIC = **1054.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21.2712** | 1.1821 | ±2.3642 | **+17.995** | **2.15e-72** | *** |
| Education: graduate level (vs college) | -0.4470 | 0.2535 | ±0.5069 | -1.764 | 0.0778 | . |
| Education: high school or below (vs college) | -0.2795 | 0.5131 | ±1.0263 | -0.545 | 0.5859 |  |
| Site: UCSD (vs UAB) | -0.0852 | 0.3557 | ±0.7115 | -0.239 | 0.8108 |  |
| **Site: UW (vs UAB)** | **-1.2344** | 0.3134 | ±0.6269 | **-3.938** | **8.20e-05** | *** |
| Season: spring (vs autumn) | -0.4446 | 0.3346 | ±0.6692 | -1.329 | 0.1839 |  |
| **Season: summer (vs autumn)** | **+2.3289** | 0.4283 | ±0.8566 | **+5.438** | **5.39e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0452** | 0.3163 | ±0.6327 | **-3.304** | **9.53e-04** | *** |
| **Age (years)** | **+0.0303** | 0.0122 | ±0.0245 | **+2.474** | **0.0133** | * |
| BMI (kg/m2) | -0.0079 | 0.0202 | ±0.0403 | -0.390 | 0.6967 |  |
| Hypertension | +0.0359 | 0.2783 | ±0.5565 | +0.129 | 0.8974 |  |
| High cholesterol | +0.4575 | 0.2585 | ±0.5169 | +1.770 | 0.0767 | . |
| **Kidney disease** | **+1.0244** | 0.4519 | ±0.9037 | **+2.267** | **0.0234** | * |
| Circulatory disease | -0.3922 | 0.3774 | ±0.7548 | -1.039 | 0.2987 |  |
| **Avg. daily range (mg/dL)** | **+0.0126** | 0.0044 | ±0.0088 | **+2.854** | **0.0043** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **241**, R² = **0.3669**, Adj R² = **0.3277**, F-statistic = **9.36** (p = **3.40e-16**), Residual SE = **1.903** on **226** df, AIC = **1008.6**, BIC = **1060.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7297** | 1.0689 | ±2.1378 | **+21.264** | **2.43e-100** | *** |
| Education: graduate level (vs college) | -0.4174 | 0.2573 | ±0.5146 | -1.622 | 0.1048 |  |
| Education: high school or below (vs college) | -0.2911 | 0.5413 | ±1.0825 | -0.538 | 0.5906 |  |
| Site: UCSD (vs UAB) | -0.2020 | 0.3638 | ±0.7276 | -0.555 | 0.5787 |  |
| **Site: UW (vs UAB)** | **-1.3240** | 0.3176 | ±0.6353 | **-4.168** | **3.07e-05** | *** |
| Season: spring (vs autumn) | -0.4766 | 0.3432 | ±0.6864 | -1.389 | 0.1650 |  |
| **Season: summer (vs autumn)** | **+2.2923** | 0.4345 | ±0.8689 | **+5.276** | **1.32e-07** | *** |
| **Season: winter (vs autumn)** | **-1.0981** | 0.3189 | ±0.6379 | **-3.443** | **5.75e-04** | *** |
| **Age (years)** | **+0.0295** | 0.0124 | ±0.0247 | **+2.390** | **0.0169** | * |
| BMI (kg/m2) | -0.0024 | 0.0203 | ±0.0406 | -0.119 | 0.9051 |  |
| Hypertension | +0.0557 | 0.2815 | ±0.5631 | +0.198 | 0.8432 |  |
| High cholesterol | +0.3399 | 0.2608 | ±0.5217 | +1.303 | 0.1925 |  |
| **Kidney disease** | **+1.1299** | 0.4488 | ±0.8977 | **+2.517** | **0.0118** | * |
| Circulatory disease | -0.2850 | 0.3578 | ±0.7156 | -0.796 | 0.4258 |  |
| SD of daily means (mg/dL) | +0.0268 | 0.0305 | ±0.0610 | +0.880 | 0.3788 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **241**, R² = **0.3807**, Adj R² = **0.3423**, F-statistic = **9.92** (p = **3.53e-17**), Residual SE = **1.882** on **226** df, AIC = **1003.3**, BIC = **1055.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7469** | 1.2980 | ±2.5960 | **+19.065** | **4.89e-81** | *** |
| Education: graduate level (vs college) | -0.4725 | 0.2605 | ±0.5210 | -1.814 | 0.0697 | . |
| Education: high school or below (vs college) | -0.4196 | 0.5287 | ±1.0573 | -0.794 | 0.4274 |  |
| Site: UCSD (vs UAB) | -0.1542 | 0.3560 | ±0.7119 | -0.433 | 0.6649 |  |
| **Site: UW (vs UAB)** | **-1.3124** | 0.3150 | ±0.6301 | **-4.166** | **3.10e-05** | *** |
| Season: spring (vs autumn) | -0.4224 | 0.3391 | ±0.6782 | -1.246 | 0.2129 |  |
| **Season: summer (vs autumn)** | **+2.4124** | 0.4300 | ±0.8601 | **+5.610** | **2.03e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0440** | 0.3152 | ±0.6305 | **-3.312** | **9.27e-04** | *** |
| **Age (years)** | **+0.0307** | 0.0123 | ±0.0245 | **+2.508** | **0.0121** | * |
| BMI (kg/m2) | -0.0097 | 0.0194 | ±0.0387 | -0.502 | 0.6158 |  |
| Hypertension | +0.0362 | 0.2795 | ±0.5590 | +0.129 | 0.8971 |  |
| High cholesterol | +0.3207 | 0.2558 | ±0.5115 | +1.254 | 0.2099 |  |
| **Kidney disease** | **+1.0738** | 0.4319 | ±0.8638 | **+2.486** | **0.0129** | * |
| Circulatory disease | -0.3734 | 0.3686 | ±0.7371 | -1.013 | 0.3111 |  |
| **Time in range 70-180, pooled (%)** | **-0.0192** | 0.0077 | ±0.0154 | **-2.494** | **0.0126** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **241**, R² = **0.3804**, Adj R² = **0.3420**, F-statistic = **9.91** (p = **3.70e-17**), Residual SE = **1.883** on **226** df, AIC = **1003.5**, BIC = **1055.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7231** | 1.2860 | ±2.5719 | **+19.225** | **2.27e-82** | *** |
| Education: graduate level (vs college) | -0.4743 | 0.2607 | ±0.5214 | -1.819 | 0.0689 | . |
| Education: high school or below (vs college) | -0.4112 | 0.5288 | ±1.0576 | -0.778 | 0.4368 |  |
| Site: UCSD (vs UAB) | -0.1495 | 0.3562 | ±0.7123 | -0.420 | 0.6747 |  |
| **Site: UW (vs UAB)** | **-1.3090** | 0.3153 | ±0.6306 | **-4.151** | **3.31e-05** | *** |
| Season: spring (vs autumn) | -0.4265 | 0.3390 | ±0.6781 | -1.258 | 0.2083 |  |
| **Season: summer (vs autumn)** | **+2.4104** | 0.4302 | ±0.8604 | **+5.603** | **2.11e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0451** | 0.3153 | ±0.6306 | **-3.315** | **9.18e-04** | *** |
| **Age (years)** | **+0.0307** | 0.0123 | ±0.0245 | **+2.500** | **0.0124** | * |
| BMI (kg/m2) | -0.0097 | 0.0194 | ±0.0388 | -0.501 | 0.6166 |  |
| Hypertension | +0.0354 | 0.2794 | ±0.5589 | +0.127 | 0.8991 |  |
| High cholesterol | +0.3205 | 0.2560 | ±0.5120 | +1.252 | 0.2105 |  |
| **Kidney disease** | **+1.0715** | 0.4334 | ±0.8667 | **+2.472** | **0.0134** | * |
| Circulatory disease | -0.3685 | 0.3686 | ±0.7371 | -1.000 | 0.3174 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0188** | 0.0075 | ±0.0150 | **-2.500** | **0.0124** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.3651**, Adj R² = **0.3258**, F-statistic = **9.28** (p = **4.55e-16**), Residual SE = **1.906** on **226** df, AIC = **1009.3**, BIC = **1061.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8227** | 1.0647 | ±2.1294 | **+21.436** | **6.16e-102** | *** |
| Education: graduate level (vs college) | -0.4215 | 0.2563 | ±0.5127 | -1.644 | 0.1001 |  |
| Education: high school or below (vs college) | -0.2283 | 0.5333 | ±1.0667 | -0.428 | 0.6686 |  |
| Site: UCSD (vs UAB) | -0.2131 | 0.3626 | ±0.7252 | -0.588 | 0.5567 |  |
| **Site: UW (vs UAB)** | **-1.3181** | 0.3211 | ±0.6422 | **-4.105** | **4.05e-05** | *** |
| Season: spring (vs autumn) | -0.4176 | 0.3389 | ±0.6778 | -1.232 | 0.2179 |  |
| **Season: summer (vs autumn)** | **+2.3012** | 0.4405 | ±0.8810 | **+5.224** | **1.75e-07** | *** |
| **Season: winter (vs autumn)** | **-1.0706** | 0.3247 | ±0.6495 | **-3.297** | **9.78e-04** | *** |
| **Age (years)** | **+0.0301** | 0.0124 | ±0.0247 | **+2.432** | **0.0150** | * |
| BMI (kg/m2) | -0.0010 | 0.0208 | ±0.0417 | -0.050 | 0.9599 |  |
| Hypertension | +0.0522 | 0.2845 | ±0.5690 | +0.184 | 0.8544 |  |
| High cholesterol | +0.3424 | 0.2615 | ±0.5230 | +1.309 | 0.1904 |  |
| **Kidney disease** | **+1.1301** | 0.4570 | ±0.9141 | **+2.473** | **0.0134** | * |
| Circulatory disease | -0.2702 | 0.3674 | ±0.7347 | -0.736 | 0.4620 |  |
| Any reading < 54 during wear (0/1) | +0.1695 | 0.3114 | ±0.6228 | +0.544 | 0.5862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.3785**, Adj R² = **0.3400**, F-statistic = **9.83** (p = **5.09e-17**), Residual SE = **1.886** on **226** df, AIC = **1004.2**, BIC = **1056.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6993** | 1.0400 | ±2.0799 | **+21.827** | **1.28e-105** | *** |
| Education: graduate level (vs college) | -0.3793 | 0.2554 | ±0.5108 | -1.485 | 0.1375 |  |
| Education: high school or below (vs college) | -0.1693 | 0.5369 | ±1.0739 | -0.315 | 0.7526 |  |
| Site: UCSD (vs UAB) | -0.1532 | 0.3572 | ±0.7144 | -0.429 | 0.6681 |  |
| **Site: UW (vs UAB)** | **-1.2347** | 0.3161 | ±0.6322 | **-3.906** | **9.40e-05** | *** |
| Season: spring (vs autumn) | -0.4267 | 0.3337 | ±0.6675 | -1.278 | 0.2011 |  |
| **Season: summer (vs autumn)** | **+2.3012** | 0.4330 | ±0.8661 | **+5.314** | **1.07e-07** | *** |
| **Season: winter (vs autumn)** | **-1.1443** | 0.3146 | ±0.6292 | **-3.638** | **2.75e-04** | *** |
| **Age (years)** | **+0.0283** | 0.0123 | ±0.0246 | **+2.299** | **0.0215** | * |
| BMI (kg/m2) | +0.0038 | 0.0201 | ±0.0403 | +0.187 | 0.8519 |  |
| Hypertension | +0.0817 | 0.2807 | ±0.5614 | +0.291 | 0.7710 |  |
| High cholesterol | +0.3851 | 0.2582 | ±0.5163 | +1.492 | 0.1358 |  |
| **Kidney disease** | **+1.1620** | 0.4428 | ±0.8855 | **+2.624** | **0.0087** | ** |
| Circulatory disease | -0.2586 | 0.3610 | ±0.7220 | -0.716 | 0.4738 |  |
| Time < 54 (%) | +0.3008 | 0.1634 | ±0.3268 | +1.841 | 0.0656 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.3780**, Adj R² = **0.3394**, F-statistic = **9.81** (p = **5.56e-17**), Residual SE = **1.887** on **226** df, AIC = **1004.4**, BIC = **1056.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7213** | 1.0382 | ±2.0764 | **+21.886** | **3.55e-106** | *** |
| Education: graduate level (vs college) | -0.3834 | 0.2557 | ±0.5115 | -1.499 | 0.1338 |  |
| Education: high school or below (vs college) | -0.1677 | 0.5357 | ±1.0713 | -0.313 | 0.7542 |  |
| Site: UCSD (vs UAB) | -0.1555 | 0.3559 | ±0.7118 | -0.437 | 0.6623 |  |
| **Site: UW (vs UAB)** | **-1.2234** | 0.3171 | ±0.6343 | **-3.858** | **1.14e-04** | *** |
| Season: spring (vs autumn) | -0.4329 | 0.3332 | ±0.6665 | -1.299 | 0.1939 |  |
| **Season: summer (vs autumn)** | **+2.3109** | 0.4339 | ±0.8677 | **+5.326** | **1.00e-07** | *** |
| **Season: winter (vs autumn)** | **-1.1563** | 0.3144 | ±0.6287 | **-3.678** | **2.35e-04** | *** |
| **Age (years)** | **+0.0283** | 0.0124 | ±0.0247 | **+2.295** | **0.0217** | * |
| BMI (kg/m2) | +0.0029 | 0.0201 | ±0.0402 | +0.142 | 0.8871 |  |
| Hypertension | +0.0848 | 0.2811 | ±0.5623 | +0.302 | 0.7629 |  |
| High cholesterol | +0.3972 | 0.2587 | ±0.5175 | +1.535 | 0.1248 |  |
| **Kidney disease** | **+1.1603** | 0.4430 | ±0.8860 | **+2.619** | **0.0088** | ** |
| Circulatory disease | -0.2649 | 0.3590 | ±0.7179 | -0.738 | 0.4605 |  |
| **Avg. daily time < 54 (%)** | **+0.3908** | 0.0951 | ±0.1903 | **+4.108** | **3.99e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.3664**, Adj R² = **0.3271**, F-statistic = **9.34** (p = **3.72e-16**), Residual SE = **1.904** on **226** df, AIC = **1008.8**, BIC = **1061.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8368** | 1.0509 | ±2.1019 | **+21.730** | **1.07e-104** | *** |
| Education: graduate level (vs college) | -0.4065 | 0.2606 | ±0.5211 | -1.560 | 0.1188 |  |
| Education: high school or below (vs college) | -0.2096 | 0.5431 | ±1.0862 | -0.386 | 0.6995 |  |
| Site: UCSD (vs UAB) | -0.1982 | 0.3630 | ±0.7259 | -0.546 | 0.5850 |  |
| **Site: UW (vs UAB)** | **-1.2930** | 0.3221 | ±0.6442 | **-4.014** | **5.96e-05** | *** |
| Season: spring (vs autumn) | -0.4249 | 0.3359 | ±0.6719 | -1.265 | 0.2059 |  |
| **Season: summer (vs autumn)** | **+2.3110** | 0.4387 | ±0.8774 | **+5.268** | **1.38e-07** | *** |
| **Season: winter (vs autumn)** | **-1.0961** | 0.3221 | ±0.6441 | **-3.403** | **6.66e-04** | *** |
| **Age (years)** | **+0.0299** | 0.0124 | ±0.0248 | **+2.415** | **0.0157** | * |
| BMI (kg/m2) | -0.0021 | 0.0210 | ±0.0419 | -0.098 | 0.9219 |  |
| Hypertension | +0.0608 | 0.2820 | ±0.5641 | +0.216 | 0.8292 |  |
| High cholesterol | +0.3635 | 0.2636 | ±0.5272 | +1.379 | 0.1679 |  |
| **Kidney disease** | **+1.1418** | 0.4479 | ±0.8958 | **+2.549** | **0.0108** | * |
| Circulatory disease | -0.2604 | 0.3626 | ±0.7252 | -0.718 | 0.4727 |  |
| Time 54-69, pooled (%) | +0.0890 | 0.2493 | ±0.4987 | +0.357 | 0.7210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **241**, R² = **0.3663**, Adj R² = **0.3270**, F-statistic = **9.33** (p = **3.78e-16**), Residual SE = **1.904** on **226** df, AIC = **1008.9**, BIC = **1061.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8410** | 1.0497 | ±2.0994 | **+21.759** | **5.67e-105** | *** |
| Education: graduate level (vs college) | -0.4068 | 0.2614 | ±0.5229 | -1.556 | 0.1197 |  |
| Education: high school or below (vs college) | -0.2101 | 0.5437 | ±1.0874 | -0.386 | 0.6992 |  |
| Site: UCSD (vs UAB) | -0.1978 | 0.3627 | ±0.7254 | -0.545 | 0.5855 |  |
| **Site: UW (vs UAB)** | **-1.2899** | 0.3224 | ±0.6448 | **-4.001** | **6.30e-05** | *** |
| Season: spring (vs autumn) | -0.4278 | 0.3352 | ±0.6704 | -1.276 | 0.2019 |  |
| **Season: summer (vs autumn)** | **+2.3101** | 0.4384 | ±0.8769 | **+5.269** | **1.37e-07** | *** |
| **Season: winter (vs autumn)** | **-1.1020** | 0.3197 | ±0.6394 | **-3.447** | **5.66e-04** | *** |
| **Age (years)** | **+0.0298** | 0.0124 | ±0.0248 | **+2.405** | **0.0162** | * |
| BMI (kg/m2) | -0.0018 | 0.0209 | ±0.0418 | -0.087 | 0.9305 |  |
| Hypertension | +0.0617 | 0.2818 | ±0.5636 | +0.219 | 0.8267 |  |
| High cholesterol | +0.3647 | 0.2653 | ±0.5306 | +1.375 | 0.1692 |  |
| **Kidney disease** | **+1.1434** | 0.4475 | ±0.8951 | **+2.555** | **0.0106** | * |
| Circulatory disease | -0.2604 | 0.3619 | ±0.7238 | -0.720 | 0.4718 |  |
| Avg. daily time 54-69 (%) | +0.0831 | 0.2418 | ±0.4836 | +0.344 | 0.7310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **241**, R² = **0.3726**, Adj R² = **0.3338**, F-statistic = **9.59** (p = **1.34e-16**), Residual SE = **1.895** on **226** df, AIC = **1006.5**, BIC = **1058.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7702** | 1.0475 | ±2.0951 | **+21.737** | **9.22e-105** | *** |
| Education: graduate level (vs college) | -0.3754 | 0.2570 | ±0.5139 | -1.461 | 0.1440 |  |
| Education: high school or below (vs college) | -0.1608 | 0.5386 | ±1.0771 | -0.299 | 0.7653 |  |
| Site: UCSD (vs UAB) | -0.1710 | 0.3590 | ±0.7181 | -0.476 | 0.6339 |  |
| **Site: UW (vs UAB)** | **-1.2475** | 0.3191 | ±0.6382 | **-3.910** | **9.25e-05** | *** |
| Season: spring (vs autumn) | -0.4248 | 0.3352 | ±0.6703 | -1.267 | 0.2050 |  |
| **Season: summer (vs autumn)** | **+2.3220** | 0.4346 | ±0.8692 | **+5.343** | **9.16e-08** | *** |
| **Season: winter (vs autumn)** | **-1.1264** | 0.3164 | ±0.6327 | **-3.561** | **3.70e-04** | *** |
| **Age (years)** | **+0.0290** | 0.0124 | ±0.0247 | **+2.347** | **0.0189** | * |
| BMI (kg/m2) | -0.0010 | 0.0207 | ±0.0414 | -0.049 | 0.9607 |  |
| Hypertension | +0.0776 | 0.2807 | ±0.5615 | +0.276 | 0.7823 |  |
| High cholesterol | +0.3961 | 0.2589 | ±0.5178 | +1.530 | 0.1261 |  |
| **Kidney disease** | **+1.1452** | 0.4449 | ±0.8898 | **+2.574** | **0.0101** | * |
| Circulatory disease | -0.2532 | 0.3631 | ±0.7263 | -0.697 | 0.4856 |  |
| Time < 70 (%) | +0.1161 | 0.1225 | ±0.2449 | +0.948 | 0.3432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **241**, R² = **0.3705**, Adj R² = **0.3315**, F-statistic = **9.50** (p = **1.92e-16**), Residual SE = **1.898** on **226** df, AIC = **1007.3**, BIC = **1059.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8016** | 1.0471 | ±2.0943 | **+21.775** | **4.01e-105** | *** |
| Education: graduate level (vs college) | -0.3858 | 0.2583 | ±0.5165 | -1.494 | 0.1353 |  |
| Education: high school or below (vs college) | -0.1747 | 0.5397 | ±1.0794 | -0.324 | 0.7461 |  |
| Site: UCSD (vs UAB) | -0.1792 | 0.3594 | ±0.7188 | -0.499 | 0.6180 |  |
| **Site: UW (vs UAB)** | **-1.2539** | 0.3200 | ±0.6400 | **-3.918** | **8.91e-05** | *** |
| Season: spring (vs autumn) | -0.4300 | 0.3347 | ±0.6694 | -1.285 | 0.1989 |  |
| **Season: summer (vs autumn)** | **+2.3207** | 0.4360 | ±0.8721 | **+5.322** | **1.02e-07** | *** |
| **Season: winter (vs autumn)** | **-1.1279** | 0.3158 | ±0.6315 | **-3.572** | **3.54e-04** | *** |
| **Age (years)** | **+0.0292** | 0.0124 | ±0.0248 | **+2.355** | **0.0185** | * |
| BMI (kg/m2) | -0.0014 | 0.0208 | ±0.0415 | -0.065 | 0.9480 |  |
| Hypertension | +0.0746 | 0.2810 | ±0.5620 | +0.265 | 0.7907 |  |
| High cholesterol | +0.3917 | 0.2616 | ±0.5231 | +1.497 | 0.1343 |  |
| **Kidney disease** | **+1.1454** | 0.4455 | ±0.8911 | **+2.571** | **0.0101** | * |
| Circulatory disease | -0.2569 | 0.3613 | ±0.7226 | -0.711 | 0.4771 |  |
| Avg. daily time < 70 (%) | +0.1031 | 0.1442 | ±0.2885 | +0.715 | 0.4745 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.3711**, Adj R² = **0.3321**, F-statistic = **9.53** (p = **1.73e-16**), Residual SE = **1.897** on **226** df, AIC = **1007.1**, BIC = **1059.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.6420** | 1.6622 | ±3.3244 | **+14.825** | **1.01e-49** | *** |
| Education: graduate level (vs college) | -0.4334 | 0.2594 | ±0.5188 | -1.671 | 0.0948 | . |
| Education: high school or below (vs college) | -0.3976 | 0.5596 | ±1.1192 | -0.711 | 0.4774 |  |
| Site: UCSD (vs UAB) | -0.1848 | 0.3583 | ±0.7165 | -0.516 | 0.6059 |  |
| **Site: UW (vs UAB)** | **-1.3071** | 0.3193 | ±0.6386 | **-4.094** | **4.24e-05** | *** |
| Season: spring (vs autumn) | -0.4379 | 0.3389 | ±0.6777 | -1.292 | 0.1963 |  |
| **Season: summer (vs autumn)** | **+2.3339** | 0.4352 | ±0.8704 | **+5.363** | **8.19e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0724** | 0.3192 | ±0.6383 | **-3.360** | **7.79e-04** | *** |
| **Age (years)** | **+0.0309** | 0.0123 | ±0.0247 | **+2.509** | **0.0121** | * |
| BMI (kg/m2) | -0.0017 | 0.0201 | ±0.0401 | -0.085 | 0.9323 |  |
| Hypertension | +0.0630 | 0.2812 | ±0.5623 | +0.224 | 0.8226 |  |
| High cholesterol | +0.3485 | 0.2590 | ±0.5180 | +1.346 | 0.1784 |  |
| **Kidney disease** | **+1.1666** | 0.4415 | ±0.8831 | **+2.642** | **0.0082** | ** |
| Circulatory disease | -0.3713 | 0.3715 | ±0.7430 | -1.000 | 0.3175 |  |
| Time 54-250, pooled (%) | -0.0185 | 0.0129 | ±0.0259 | -1.432 | 0.1520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.3706**, Adj R² = **0.3317**, F-statistic = **9.51** (p = **1.86e-16**), Residual SE = **1.898** on **226** df, AIC = **1007.2**, BIC = **1059.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.6306** | 1.6652 | ±3.3305 | **+14.791** | **1.68e-49** | *** |
| Education: graduate level (vs college) | -0.4347 | 0.2595 | ±0.5190 | -1.675 | 0.0939 | . |
| Education: high school or below (vs college) | -0.3961 | 0.5604 | ±1.1208 | -0.707 | 0.4797 |  |
| Site: UCSD (vs UAB) | -0.1854 | 0.3586 | ±0.7172 | -0.517 | 0.6052 |  |
| **Site: UW (vs UAB)** | **-1.3096** | 0.3193 | ±0.6387 | **-4.101** | **4.11e-05** | *** |
| Season: spring (vs autumn) | -0.4362 | 0.3389 | ±0.6777 | -1.287 | 0.1980 |  |
| **Season: summer (vs autumn)** | **+2.3340** | 0.4354 | ±0.8708 | **+5.361** | **8.29e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0696** | 0.3196 | ±0.6391 | **-3.347** | **8.16e-04** | *** |
| **Age (years)** | **+0.0309** | 0.0123 | ±0.0247 | **+2.506** | **0.0122** | * |
| BMI (kg/m2) | -0.0019 | 0.0201 | ±0.0401 | -0.096 | 0.9234 |  |
| Hypertension | +0.0615 | 0.2812 | ±0.5625 | +0.219 | 0.8268 |  |
| High cholesterol | +0.3485 | 0.2592 | ±0.5184 | +1.344 | 0.1788 |  |
| **Kidney disease** | **+1.1678** | 0.4422 | ±0.8843 | **+2.641** | **0.0083** | ** |
| Circulatory disease | -0.3704 | 0.3708 | ±0.7417 | -0.999 | 0.3179 |  |
| Avg. daily time 54-250 (%) | -0.0183 | 0.0130 | ±0.0259 | -1.412 | 0.1579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.3771**, Adj R² = **0.3385**, F-statistic = **9.77** (p = **6.43e-17**), Residual SE = **1.888** on **226** df, AIC = **1004.7**, BIC = **1057.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9274** | 1.0354 | ±2.0708 | **+22.144** | **1.20e-108** | *** |
| Education: graduate level (vs college) | -0.5028 | 0.2600 | ±0.5201 | -1.934 | 0.0532 | . |
| Education: high school or below (vs college) | -0.2982 | 0.5263 | ±1.0526 | -0.567 | 0.5710 |  |
| Site: UCSD (vs UAB) | -0.1736 | 0.3601 | ±0.7202 | -0.482 | 0.6298 |  |
| **Site: UW (vs UAB)** | **-1.3456** | 0.3156 | ±0.6311 | **-4.264** | **2.01e-05** | *** |
| Season: spring (vs autumn) | -0.4033 | 0.3356 | ±0.6712 | -1.202 | 0.2295 |  |
| **Season: summer (vs autumn)** | **+2.3951** | 0.4266 | ±0.8531 | **+5.615** | **1.97e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0327** | 0.3158 | ±0.6315 | **-3.270** | **0.0011** | ** |
| **Age (years)** | **+0.0302** | 0.0123 | ±0.0246 | **+2.452** | **0.0142** | * |
| BMI (kg/m2) | -0.0114 | 0.0196 | ±0.0392 | -0.581 | 0.5616 |  |
| Hypertension | +0.0043 | 0.2816 | ±0.5632 | +0.015 | 0.9878 |  |
| High cholesterol | +0.2756 | 0.2595 | ±0.5190 | +1.062 | 0.2882 |  |
| **Kidney disease** | **+1.0141** | 0.4315 | ±0.8630 | **+2.350** | **0.0188** | * |
| Circulatory disease | -0.2706 | 0.3511 | ±0.7022 | -0.771 | 0.4409 |  |
| **Time 181-250, pooled (%)** | **+0.0279** | 0.0132 | ±0.0263 | **+2.124** | **0.0337** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **241**, R² = **0.3775**, Adj R² = **0.3390**, F-statistic = **9.79** (p = **5.98e-17**), Residual SE = **1.887** on **226** df, AIC = **1004.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9284** | 1.0364 | ±2.0728 | **+22.123** | **1.89e-108** | *** |
| Education: graduate level (vs college) | -0.5043 | 0.2603 | ±0.5205 | -1.938 | 0.0527 | . |
| Education: high school or below (vs college) | -0.2905 | 0.5246 | ±1.0491 | -0.554 | 0.5798 |  |
| Site: UCSD (vs UAB) | -0.1656 | 0.3599 | ±0.7198 | -0.460 | 0.6454 |  |
| **Site: UW (vs UAB)** | **-1.3382** | 0.3153 | ±0.6307 | **-4.244** | **2.20e-05** | *** |
| Season: spring (vs autumn) | -0.4109 | 0.3361 | ±0.6721 | -1.223 | 0.2214 |  |
| **Season: summer (vs autumn)** | **+2.3932** | 0.4268 | ±0.8537 | **+5.607** | **2.06e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0358** | 0.3159 | ±0.6317 | **-3.279** | **0.0010** | ** |
| **Age (years)** | **+0.0301** | 0.0123 | ±0.0246 | **+2.448** | **0.0144** | * |
| BMI (kg/m2) | -0.0112 | 0.0196 | ±0.0391 | -0.571 | 0.5681 |  |
| Hypertension | +0.0049 | 0.2811 | ±0.5623 | +0.017 | 0.9862 |  |
| High cholesterol | +0.2742 | 0.2596 | ±0.5192 | +1.056 | 0.2908 |  |
| **Kidney disease** | **+1.0075** | 0.4322 | ±0.8644 | **+2.331** | **0.0198** | * |
| Circulatory disease | -0.2661 | 0.3525 | ±0.7049 | -0.755 | 0.4502 |  |
| **Avg. daily time 181-250 (%)** | **+0.0276** | 0.0128 | ±0.0255 | **+2.162** | **0.0306** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **241**, R² = **0.3778**, Adj R² = **0.3393**, F-statistic = **9.80** (p = **5.70e-17**), Residual SE = **1.887** on **226** df, AIC = **1004.5**, BIC = **1056.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8466** | 1.0377 | ±2.0754 | **+22.016** | **2.01e-107** | *** |
| Education: graduate level (vs college) | -0.4780 | 0.2615 | ±0.5230 | -1.828 | 0.0675 | . |
| Education: high school or below (vs college) | -0.4183 | 0.5325 | ±1.0649 | -0.786 | 0.4321 |  |
| Site: UCSD (vs UAB) | -0.1660 | 0.3574 | ±0.7148 | -0.465 | 0.6423 |  |
| **Site: UW (vs UAB)** | **-1.3255** | 0.3161 | ±0.6322 | **-4.194** | **2.75e-05** | *** |
| Season: spring (vs autumn) | -0.4229 | 0.3386 | ±0.6772 | -1.249 | 0.2116 |  |
| **Season: summer (vs autumn)** | **+2.3956** | 0.4302 | ±0.8605 | **+5.568** | **2.57e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0404** | 0.3165 | ±0.6330 | **-3.287** | **0.0010** | ** |
| **Age (years)** | **+0.0309** | 0.0123 | ±0.0245 | **+2.520** | **0.0117** | * |
| BMI (kg/m2) | -0.0087 | 0.0194 | ±0.0387 | -0.449 | 0.6531 |  |
| Hypertension | +0.0330 | 0.2800 | ±0.5601 | +0.118 | 0.9063 |  |
| High cholesterol | +0.3113 | 0.2568 | ±0.5137 | +1.212 | 0.2255 |  |
| **Kidney disease** | **+1.0815** | 0.4334 | ±0.8668 | **+2.495** | **0.0126** | * |
| Circulatory disease | -0.3657 | 0.3667 | ±0.7335 | -0.997 | 0.3187 |  |
| **Time > 180 (%)** | **+0.0173** | 0.0074 | ±0.0149 | **+2.321** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **241**, R² = **0.3780**, Adj R² = **0.3395**, F-statistic = **9.81** (p = **5.53e-17**), Residual SE = **1.887** on **226** df, AIC = **1004.4**, BIC = **1056.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8551** | 1.0385 | ±2.0770 | **+22.008** | **2.41e-107** | *** |
| Education: graduate level (vs college) | -0.4796 | 0.2617 | ±0.5233 | -1.833 | 0.0668 | . |
| Education: high school or below (vs college) | -0.4123 | 0.5324 | ±1.0649 | -0.774 | 0.4387 |  |
| Site: UCSD (vs UAB) | -0.1603 | 0.3574 | ±0.7148 | -0.448 | 0.6539 |  |
| **Site: UW (vs UAB)** | **-1.3225** | 0.3160 | ±0.6321 | **-4.185** | **2.86e-05** | *** |
| Season: spring (vs autumn) | -0.4259 | 0.3386 | ±0.6773 | -1.258 | 0.2086 |  |
| **Season: summer (vs autumn)** | **+2.3952** | 0.4303 | ±0.8607 | **+5.566** | **2.61e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0398** | 0.3165 | ±0.6331 | **-3.285** | **0.0010** | ** |
| **Age (years)** | **+0.0308** | 0.0123 | ±0.0245 | **+2.512** | **0.0120** | * |
| BMI (kg/m2) | -0.0087 | 0.0194 | ±0.0387 | -0.452 | 0.6513 |  |
| Hypertension | +0.0321 | 0.2799 | ±0.5598 | +0.115 | 0.9087 |  |
| High cholesterol | +0.3106 | 0.2569 | ±0.5138 | +1.209 | 0.2267 |  |
| **Kidney disease** | **+1.0783** | 0.4344 | ±0.8689 | **+2.482** | **0.0131** | * |
| Circulatory disease | -0.3625 | 0.3671 | ±0.7342 | -0.987 | 0.3234 |  |
| **Avg. daily time > 180 (%)** | **+0.0172** | 0.0073 | ±0.0147 | **+2.348** | **0.0189** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **241**, R² = **0.3719**, Adj R² = **0.3330**, F-statistic = **9.56** (p = **1.52e-16**), Residual SE = **1.896** on **226** df, AIC = **1006.7**, BIC = **1059.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9086** | 1.0456 | ±2.0912 | **+21.910** | **2.10e-106** | *** |
| Education: graduate level (vs college) | -0.4387 | 0.2580 | ±0.5160 | -1.700 | 0.0891 | . |
| Education: high school or below (vs college) | -0.3409 | 0.5403 | ±1.0806 | -0.631 | 0.5280 |  |
| Site: UCSD (vs UAB) | -0.1931 | 0.3563 | ±0.7125 | -0.542 | 0.5878 |  |
| **Site: UW (vs UAB)** | **-1.3210** | 0.3178 | ±0.6357 | **-4.156** | **3.24e-05** | *** |
| Season: spring (vs autumn) | -0.4580 | 0.3384 | ±0.6768 | -1.353 | 0.1759 |  |
| **Season: summer (vs autumn)** | **+2.3610** | 0.4338 | ±0.8676 | **+5.442** | **5.26e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0768** | 0.3200 | ±0.6401 | **-3.365** | **7.67e-04** | *** |
| **Age (years)** | **+0.0313** | 0.0123 | ±0.0247 | **+2.536** | **0.0112** | * |
| BMI (kg/m2) | -0.0076 | 0.0197 | ±0.0394 | -0.388 | 0.6980 |  |
| Hypertension | +0.0510 | 0.2810 | ±0.5620 | +0.181 | 0.8560 |  |
| High cholesterol | +0.3073 | 0.2597 | ±0.5195 | +1.183 | 0.2368 |  |
| **Kidney disease** | **+1.1785** | 0.4354 | ±0.8709 | **+2.706** | **0.0068** | ** |
| Circulatory disease | -0.3237 | 0.3688 | ±0.7376 | -0.878 | 0.3801 |  |
| Nocturnal time > 180 (%) | +0.0124 | 0.0071 | ±0.0142 | +1.740 | 0.0819 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.3695**, Adj R² = **0.3304**, F-statistic = **9.46** (p = **2.25e-16**), Residual SE = **1.899** on **226** df, AIC = **1007.7**, BIC = **1059.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8059** | 1.0471 | ±2.0943 | **+21.779** | **3.66e-105** | *** |
| Education: graduate level (vs college) | -0.4368 | 0.2599 | ±0.5198 | -1.681 | 0.0928 | . |
| Education: high school or below (vs college) | -0.3853 | 0.5609 | ±1.1218 | -0.687 | 0.4922 |  |
| Site: UCSD (vs UAB) | -0.1914 | 0.3595 | ±0.7190 | -0.532 | 0.5945 |  |
| **Site: UW (vs UAB)** | **-1.3144** | 0.3199 | ±0.6398 | **-4.109** | **3.97e-05** | *** |
| Season: spring (vs autumn) | -0.4364 | 0.3384 | ±0.6769 | -1.289 | 0.1973 |  |
| **Season: summer (vs autumn)** | **+2.3278** | 0.4352 | ±0.8704 | **+5.349** | **8.87e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0697** | 0.3202 | ±0.6404 | **-3.341** | **8.35e-04** | *** |
| **Age (years)** | **+0.0310** | 0.0123 | ±0.0247 | **+2.512** | **0.0120** | * |
| BMI (kg/m2) | -0.0018 | 0.0201 | ±0.0402 | -0.087 | 0.9305 |  |
| Hypertension | +0.0594 | 0.2817 | ±0.5634 | +0.211 | 0.8329 |  |
| High cholesterol | +0.3430 | 0.2597 | ±0.5195 | +1.320 | 0.1867 |  |
| **Kidney disease** | **+1.1636** | 0.4423 | ±0.8846 | **+2.631** | **0.0085** | ** |
| Circulatory disease | -0.3595 | 0.3701 | ±0.7402 | -0.971 | 0.3313 |  |
| Time > 250 (%) | +0.0163 | 0.0125 | ±0.0250 | +1.301 | 0.1932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 241)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **241**, R² = **0.3694**, Adj R² = **0.3304**, F-statistic = **9.46** (p = **2.27e-16**), Residual SE = **1.900** on **226** df, AIC = **1007.7**, BIC = **1060.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8121** | 1.0469 | ±2.0939 | **+21.789** | **2.92e-105** | *** |
| Education: graduate level (vs college) | -0.4371 | 0.2598 | ±0.5196 | -1.682 | 0.0925 | . |
| Education: high school or below (vs college) | -0.3865 | 0.5615 | ±1.1230 | -0.688 | 0.4913 |  |
| Site: UCSD (vs UAB) | -0.1904 | 0.3596 | ±0.7192 | -0.530 | 0.5964 |  |
| **Site: UW (vs UAB)** | **-1.3156** | 0.3197 | ±0.6394 | **-4.115** | **3.87e-05** | *** |
| Season: spring (vs autumn) | -0.4349 | 0.3386 | ±0.6771 | -1.285 | 0.1989 |  |
| **Season: summer (vs autumn)** | **+2.3288** | 0.4354 | ±0.8707 | **+5.349** | **8.85e-08** | *** |
| **Season: winter (vs autumn)** | **-1.0673** | 0.3204 | ±0.6407 | **-3.331** | **8.64e-04** | *** |
| **Age (years)** | **+0.0309** | 0.0123 | ±0.0247 | **+2.509** | **0.0121** | * |
| BMI (kg/m2) | -0.0019 | 0.0201 | ±0.0402 | -0.095 | 0.9245 |  |
| Hypertension | +0.0587 | 0.2817 | ±0.5633 | +0.208 | 0.8349 |  |
| High cholesterol | +0.3436 | 0.2597 | ±0.5195 | +1.323 | 0.1859 |  |
| **Kidney disease** | **+1.1654** | 0.4427 | ±0.8854 | **+2.633** | **0.0085** | ** |
| Circulatory disease | -0.3608 | 0.3699 | ±0.7398 | -0.975 | 0.3294 |  |
| Avg. daily time > 250 (%) | +0.0165 | 0.0126 | ±0.0252 | +1.309 | 0.1906 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 241; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **241**, R² = **0.2682**, Adj R² = **0.2263**, F-statistic = **6.40** (p = **2.72e-10**), Residual SE = **5.967** on **227** df, AIC = **1558.4**, BIC = **1607.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5790** | 3.3481 | ±6.6962 | **+14.509** | **1.06e-47** | *** |
| Education: graduate level (vs college) | -0.1630 | 0.8585 | ±1.7170 | -0.190 | 0.8494 |  |
| Education: high school or below (vs college) | +0.4257 | 1.3148 | ±2.6296 | +0.324 | 0.7461 |  |
| Site: UCSD (vs UAB) | +2.0694 | 1.1872 | ±2.3744 | +1.743 | 0.0813 | . |
| Site: UW (vs UAB) | -1.8802 | 1.0310 | ±2.0620 | -1.824 | 0.0682 | . |
| Season: spring (vs autumn) | -1.4857 | 1.1339 | ±2.2677 | -1.310 | 0.1901 |  |
| **Season: summer (vs autumn)** | **+2.5623** | 1.3011 | ±2.6021 | **+1.969** | **0.0489** | * |
| **Season: winter (vs autumn)** | **-5.1913** | 1.0548 | ±2.1096 | **-4.922** | **8.58e-07** | *** |
| Age (years) | -0.0544 | 0.0373 | ±0.0747 | -1.457 | 0.1451 |  |
| BMI (kg/m2) | +0.0409 | 0.0620 | ±0.1239 | +0.660 | 0.5090 |  |
| Hypertension | -0.3682 | 0.9189 | ±1.8377 | -0.401 | 0.6887 |  |
| High cholesterol | -1.0963 | 0.8038 | ±1.6075 | -1.364 | 0.1726 |  |
| Kidney disease | -1.8645 | 1.6886 | ±3.3773 | -1.104 | 0.2695 |  |
| Circulatory disease | +2.2430 | 1.3394 | ±2.6789 | +1.675 | 0.0940 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **241**, R² = **0.2703**, Adj R² = **0.2251**, F-statistic = **5.98** (p = **5.41e-10**), Residual SE = **5.971** on **226** df, AIC = **1559.8**, BIC = **1612.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6966** | 3.9221 | ±7.8442 | **+11.906** | **1.10e-32** | *** |
| Education: graduate level (vs college) | -0.1680 | 0.8573 | ±1.7146 | -0.196 | 0.8447 |  |
| Education: high school or below (vs college) | +0.2035 | 1.3554 | ±2.7109 | +0.150 | 0.8807 |  |
| Site: UCSD (vs UAB) | +2.0731 | 1.1894 | ±2.3788 | +1.743 | 0.0813 | . |
| Site: UW (vs UAB) | -1.9022 | 1.0344 | ±2.0688 | -1.839 | 0.0659 | . |
| Season: spring (vs autumn) | -1.4868 | 1.1311 | ±2.2621 | -1.315 | 0.1887 |  |
| **Season: summer (vs autumn)** | **+2.6163** | 1.3107 | ±2.6215 | **+1.996** | **0.0459** | * |
| **Season: winter (vs autumn)** | **-5.1996** | 1.0552 | ±2.1104 | **-4.928** | **8.33e-07** | *** |
| Age (years) | -0.0550 | 0.0376 | ±0.0752 | -1.463 | 0.1434 |  |
| BMI (kg/m2) | +0.0355 | 0.0618 | ±0.1235 | +0.575 | 0.5654 |  |
| Hypertension | -0.3716 | 0.9203 | ±1.8407 | -0.404 | 0.6864 |  |
| High cholesterol | -1.1414 | 0.8106 | ±1.6212 | -1.408 | 0.1591 |  |
| Kidney disease | -1.7936 | 1.7067 | ±3.4133 | -1.051 | 0.2933 |  |
| Circulatory disease | +2.0455 | 1.3805 | ±2.7610 | +1.482 | 0.1384 |  |
| HbA1c (%) | +0.3558 | 0.3251 | ±0.6502 | +1.094 | 0.2738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **241**, R² = **0.2697**, Adj R² = **0.2245**, F-statistic = **5.96** (p = **5.83e-10**), Residual SE = **5.974** on **226** df, AIC = **1560.0**, BIC = **1612.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4393** | 3.8960 | ±7.7920 | **+12.176** | **4.15e-34** | *** |
| Education: graduate level (vs college) | -0.2105 | 0.8583 | ±1.7166 | -0.245 | 0.8063 |  |
| Education: high school or below (vs college) | +0.2201 | 1.3666 | ±2.7331 | +0.161 | 0.8721 |  |
| Site: UCSD (vs UAB) | +2.1142 | 1.2047 | ±2.4095 | +1.755 | 0.0793 | . |
| Site: UW (vs UAB) | -1.8900 | 1.0353 | ±2.0706 | -1.826 | 0.0679 | . |
| Season: spring (vs autumn) | -1.4965 | 1.1372 | ±2.2743 | -1.316 | 0.1882 |  |
| **Season: summer (vs autumn)** | **+2.6600** | 1.3059 | ±2.6119 | **+2.037** | **0.0417** | * |
| **Season: winter (vs autumn)** | **-5.1307** | 1.0625 | ±2.1250 | **-4.829** | **1.37e-06** | *** |
| Age (years) | -0.0540 | 0.0377 | ±0.0753 | -1.434 | 0.1517 |  |
| BMI (kg/m2) | +0.0344 | 0.0618 | ±0.1237 | +0.557 | 0.5776 |  |
| Hypertension | -0.3857 | 0.9198 | ±1.8396 | -0.419 | 0.6750 |  |
| High cholesterol | -1.1235 | 0.8064 | ±1.6128 | -1.393 | 0.1635 |  |
| Kidney disease | -1.8750 | 1.7081 | ±3.4162 | -1.098 | 0.2723 |  |
| Circulatory disease | +2.1196 | 1.3999 | ±2.7998 | +1.514 | 0.1300 |  |
| Mean glucose (mg/dL) | +0.0095 | 0.0122 | ±0.0244 | +0.775 | 0.4386 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **241**, R² = **0.2697**, Adj R² = **0.2245**, F-statistic = **5.96** (p = **5.83e-10**), Residual SE = **5.974** on **226** df, AIC = **1560.0**, BIC = **1612.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.1294** | 4.9920 | ±9.9839 | **+9.241** | **2.45e-20** | *** |
| Education: graduate level (vs college) | -0.2105 | 0.8583 | ±1.7166 | -0.245 | 0.8063 |  |
| Education: high school or below (vs college) | +0.2201 | 1.3666 | ±2.7331 | +0.161 | 0.8721 |  |
| Site: UCSD (vs UAB) | +2.1142 | 1.2047 | ±2.4095 | +1.755 | 0.0793 | . |
| Site: UW (vs UAB) | -1.8900 | 1.0353 | ±2.0706 | -1.826 | 0.0679 | . |
| Season: spring (vs autumn) | -1.4965 | 1.1372 | ±2.2743 | -1.316 | 0.1882 |  |
| **Season: summer (vs autumn)** | **+2.6600** | 1.3059 | ±2.6119 | **+2.037** | **0.0417** | * |
| **Season: winter (vs autumn)** | **-5.1307** | 1.0625 | ±2.1250 | **-4.829** | **1.37e-06** | *** |
| Age (years) | -0.0540 | 0.0377 | ±0.0753 | -1.434 | 0.1517 |  |
| BMI (kg/m2) | +0.0344 | 0.0618 | ±0.1237 | +0.557 | 0.5776 |  |
| Hypertension | -0.3857 | 0.9198 | ±1.8396 | -0.419 | 0.6750 |  |
| High cholesterol | -1.1235 | 0.8064 | ±1.6128 | -1.393 | 0.1635 |  |
| Kidney disease | -1.8750 | 1.7081 | ±3.4162 | -1.098 | 0.2723 |  |
| Circulatory disease | +2.1196 | 1.3999 | ±2.7998 | +1.514 | 0.1300 |  |
| GMI (%) | +0.3958 | 0.5109 | ±1.0218 | +0.775 | 0.4386 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **241**, R² = **0.2702**, Adj R² = **0.2250**, F-statistic = **5.98** (p = **5.46e-10**), Residual SE = **5.972** on **226** df, AIC = **1559.8**, BIC = **1612.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4437** | 3.7453 | ±7.4905 | **+12.668** | **8.94e-37** | *** |
| Education: graduate level (vs college) | -0.1929 | 0.8598 | ±1.7196 | -0.224 | 0.8225 |  |
| Education: high school or below (vs college) | +0.2136 | 1.3650 | ±2.7300 | +0.156 | 0.8757 |  |
| Site: UCSD (vs UAB) | +2.0885 | 1.1958 | ±2.3916 | +1.747 | 0.0807 | . |
| Site: UW (vs UAB) | -1.8841 | 1.0377 | ±2.0755 | -1.816 | 0.0694 | . |
| Season: spring (vs autumn) | -1.5247 | 1.1417 | ±2.2833 | -1.336 | 0.1817 |  |
| **Season: summer (vs autumn)** | **+2.6842** | 1.3002 | ±2.6004 | **+2.064** | **0.0390** | * |
| **Season: winter (vs autumn)** | **-5.1476** | 1.0596 | ±2.1192 | **-4.858** | **1.18e-06** | *** |
| Age (years) | -0.0530 | 0.0377 | ±0.0754 | -1.406 | 0.1597 |  |
| BMI (kg/m2) | +0.0318 | 0.0623 | ±0.1246 | +0.510 | 0.6100 |  |
| Hypertension | -0.3843 | 0.9209 | ±1.8419 | -0.417 | 0.6765 |  |
| High cholesterol | -1.1297 | 0.8053 | ±1.6105 | -1.403 | 0.1606 |  |
| Kidney disease | -1.7934 | 1.7184 | ±3.4367 | -1.044 | 0.2966 |  |
| Circulatory disease | +2.1244 | 1.3873 | ±2.7747 | +1.531 | 0.1257 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0099 | 0.0110 | ±0.0219 | +0.902 | 0.3673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **241**, R² = **0.2695**, Adj R² = **0.2243**, F-statistic = **5.96** (p = **5.96e-10**), Residual SE = **5.974** on **226** df, AIC = **1560.0**, BIC = **1612.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4436** | 3.7036 | ±7.4072 | **+13.350** | **1.18e-40** | *** |
| Education: graduate level (vs college) | -0.1570 | 0.8603 | ±1.7205 | -0.183 | 0.8552 |  |
| Education: high school or below (vs college) | +0.4525 | 1.3250 | ±2.6501 | +0.341 | 0.7327 |  |
| Site: UCSD (vs UAB) | +1.9978 | 1.1928 | ±2.3856 | +1.675 | 0.0940 | . |
| Site: UW (vs UAB) | -1.9138 | 1.0363 | ±2.0726 | -1.847 | 0.0648 | . |
| Season: spring (vs autumn) | -1.4812 | 1.1398 | ±2.2795 | -1.300 | 0.1937 |  |
| Season: summer (vs autumn) | +2.5209 | 1.3069 | ±2.6138 | +1.929 | 0.0537 | . |
| **Season: winter (vs autumn)** | **-5.2241** | 1.0588 | ±2.1175 | **-4.934** | **8.05e-07** | *** |
| Age (years) | -0.0535 | 0.0373 | ±0.0745 | -1.437 | 0.1506 |  |
| BMI (kg/m2) | +0.0473 | 0.0633 | ±0.1266 | +0.747 | 0.4553 |  |
| Hypertension | -0.3361 | 0.9138 | ±1.8276 | -0.368 | 0.7130 |  |
| High cholesterol | -1.1585 | 0.7998 | ±1.5996 | -1.449 | 0.1475 |  |
| Kidney disease | -1.7146 | 1.6959 | ±3.3918 | -1.011 | 0.3120 |  |
| Circulatory disease | +2.3552 | 1.3540 | ±2.7081 | +1.739 | 0.0820 | . |
| Glucose SD, pooled (mg/dL) | -0.0345 | 0.0545 | ±0.1090 | -0.632 | 0.5272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **241**, R² = **0.2683**, Adj R² = **0.2230**, F-statistic = **5.92** (p = **7.04e-10**), Residual SE = **5.980** on **226** df, AIC = **1560.4**, BIC = **1612.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7703** | 3.6884 | ±7.3769 | **+13.222** | **6.51e-40** | *** |
| Education: graduate level (vs college) | -0.1582 | 0.8569 | ±1.7139 | -0.185 | 0.8536 |  |
| Education: high school or below (vs college) | +0.4269 | 1.3249 | ±2.6497 | +0.322 | 0.7473 |  |
| Site: UCSD (vs UAB) | +2.0524 | 1.1921 | ±2.3842 | +1.722 | 0.0851 | . |
| Site: UW (vs UAB) | -1.8867 | 1.0383 | ±2.0765 | -1.817 | 0.0692 | . |
| Season: spring (vs autumn) | -1.4902 | 1.1365 | ±2.2729 | -1.311 | 0.1898 |  |
| Season: summer (vs autumn) | +2.5531 | 1.3118 | ±2.6237 | +1.946 | 0.0516 | . |
| **Season: winter (vs autumn)** | **-5.2007** | 1.0603 | ±2.1206 | **-4.905** | **9.35e-07** | *** |
| Age (years) | -0.0542 | 0.0375 | ±0.0749 | -1.447 | 0.1478 |  |
| BMI (kg/m2) | +0.0426 | 0.0638 | ±0.1276 | +0.668 | 0.5039 |  |
| Hypertension | -0.3582 | 0.9129 | ±1.8258 | -0.392 | 0.6948 |  |
| High cholesterol | -1.1104 | 0.8037 | ±1.6074 | -1.382 | 0.1671 |  |
| Kidney disease | -1.8301 | 1.7072 | ±3.4144 | -1.072 | 0.2837 |  |
| Circulatory disease | +2.2704 | 1.3611 | ±2.7222 | +1.668 | 0.0953 | . |
| Avg. daily SD (mg/dL) | -0.0087 | 0.0589 | ±0.1178 | -0.148 | 0.8826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **241**, R² = **0.2713**, Adj R² = **0.2262**, F-statistic = **6.01** (p = **4.69e-10**), Residual SE = **5.967** on **226** df, AIC = **1559.4**, BIC = **1611.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2934** | 3.7466 | ±7.4932 | **+13.424** | **4.39e-41** | *** |
| Education: graduate level (vs college) | -0.2315 | 0.8723 | ±1.7447 | -0.265 | 0.7907 |  |
| Education: high school or below (vs college) | +0.2353 | 1.3611 | ±2.7222 | +0.173 | 0.8628 |  |
| Site: UCSD (vs UAB) | +1.9815 | 1.1862 | ±2.3724 | +1.670 | 0.0948 | . |
| Site: UW (vs UAB) | -1.9792 | 1.0354 | ±2.0708 | -1.911 | 0.0559 | . |
| Season: spring (vs autumn) | -1.4842 | 1.1366 | ±2.2733 | -1.306 | 0.1916 |  |
| **Season: summer (vs autumn)** | **+2.6043** | 1.3027 | ±2.6054 | **+1.999** | **0.0456** | * |
| **Season: winter (vs autumn)** | **-5.1673** | 1.0624 | ±2.1248 | **-4.864** | **1.15e-06** | *** |
| Age (years) | -0.0520 | 0.0374 | ±0.0748 | -1.392 | 0.1638 |  |
| BMI (kg/m2) | +0.0437 | 0.0626 | ±0.1253 | +0.697 | 0.4857 |  |
| Hypertension | -0.3538 | 0.9188 | ±1.8375 | -0.385 | 0.7002 |  |
| High cholesterol | -1.2591 | 0.8008 | ±1.6016 | -1.572 | 0.1159 |  |
| Kidney disease | -1.6484 | 1.7285 | ±3.4570 | -0.954 | 0.3403 |  |
| Circulatory disease | +2.2763 | 1.3372 | ±2.6744 | +1.702 | 0.0887 | . |
| CV (%) | -0.0808 | 0.0846 | ±0.1693 | -0.955 | 0.3397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **241**, R² = **0.2742**, Adj R² = **0.2292**, F-statistic = **6.10** (p = **3.19e-10**), Residual SE = **5.955** on **226** df, AIC = **1558.5**, BIC = **1610.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.7952** | 4.1255 | ±8.2510 | **+11.100** | **1.25e-28** | *** |
| Education: graduate level (vs college) | -0.2043 | 0.8623 | ±1.7245 | -0.237 | 0.8127 |  |
| Education: high school or below (vs college) | +0.2145 | 1.3594 | ±2.7187 | +0.158 | 0.8746 |  |
| Site: UCSD (vs UAB) | +1.9763 | 1.1845 | ±2.3690 | +1.668 | 0.0952 | . |
| Site: UW (vs UAB) | -2.0074 | 1.0299 | ±2.0597 | -1.949 | 0.0513 | . |
| Season: spring (vs autumn) | -1.4740 | 1.1341 | ±2.2681 | -1.300 | 0.1937 |  |
| **Season: summer (vs autumn)** | **+2.6551** | 1.3005 | ±2.6011 | **+2.042** | **0.0412** | * |
| **Season: winter (vs autumn)** | **-5.1052** | 1.0642 | ±2.1283 | **-4.797** | **1.61e-06** | *** |
| Age (years) | -0.0521 | 0.0374 | ±0.0747 | -1.394 | 0.1633 |  |
| BMI (kg/m2) | +0.0426 | 0.0620 | ±0.1241 | +0.686 | 0.4924 |  |
| Hypertension | -0.3070 | 0.9156 | ±1.8311 | -0.335 | 0.7374 |  |
| High cholesterol | -1.2840 | 0.7940 | ±1.5880 | -1.617 | 0.1059 |  |
| Kidney disease | -1.6069 | 1.7096 | ±3.4192 | -0.940 | 0.3473 |  |
| Circulatory disease | +2.2843 | 1.3427 | ±2.6855 | +1.701 | 0.0889 | . |
| Mean / SD ratio | +0.5725 | 0.4428 | ±0.8855 | +1.293 | 0.1960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **241**, R² = **0.2690**, Adj R² = **0.2237**, F-statistic = **5.94** (p = **6.41e-10**), Residual SE = **5.977** on **226** df, AIC = **1560.2**, BIC = **1612.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6218** | 3.9931 | ±7.9862 | **+11.926** | **8.67e-33** | *** |
| Education: graduate level (vs college) | -0.1639 | 0.8614 | ±1.7229 | -0.190 | 0.8491 |  |
| Education: high school or below (vs college) | +0.3463 | 1.3568 | ±2.7137 | +0.255 | 0.7986 |  |
| Site: UCSD (vs UAB) | +2.0416 | 1.1847 | ±2.3693 | +1.723 | 0.0848 | . |
| Site: UW (vs UAB) | -1.9265 | 1.0312 | ±2.0624 | -1.868 | 0.0617 | . |
| Season: spring (vs autumn) | -1.5070 | 1.1388 | ±2.2776 | -1.323 | 0.1857 |  |
| **Season: summer (vs autumn)** | **+2.5928** | 1.3017 | ±2.6033 | **+1.992** | **0.0464** | * |
| **Season: winter (vs autumn)** | **-5.1682** | 1.0647 | ±2.1294 | **-4.854** | **1.21e-06** | *** |
| Age (years) | -0.0532 | 0.0376 | ±0.0751 | -1.418 | 0.1562 |  |
| BMI (kg/m2) | +0.0425 | 0.0624 | ±0.1248 | +0.682 | 0.4955 |  |
| Hypertension | -0.3385 | 0.9173 | ±1.8346 | -0.369 | 0.7121 |  |
| High cholesterol | -1.1592 | 0.8031 | ±1.6061 | -1.443 | 0.1489 |  |
| Kidney disease | -1.7687 | 1.7181 | ±3.4363 | -1.029 | 0.3033 |  |
| Circulatory disease | +2.2517 | 1.3461 | ±2.6922 | +1.673 | 0.0944 | . |
| Avg. daily mean/SD | +0.1599 | 0.3333 | ±0.6666 | +0.480 | 0.6315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **241**, R² = **0.2682**, Adj R² = **0.2229**, F-statistic = **5.92** (p = **7.10e-10**), Residual SE = **5.980** on **226** df, AIC = **1560.4**, BIC = **1612.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6787** | 4.1455 | ±8.2909 | **+11.743** | **7.70e-32** | *** |
| Education: graduate level (vs college) | -0.1674 | 0.8773 | ±1.7546 | -0.191 | 0.8486 |  |
| Education: high school or below (vs college) | +0.4236 | 1.3188 | ±2.6375 | +0.321 | 0.7480 |  |
| Site: UCSD (vs UAB) | +2.0611 | 1.2366 | ±2.4733 | +1.667 | 0.0956 | . |
| Site: UW (vs UAB) | -1.8913 | 1.0860 | ±2.1720 | -1.741 | 0.0816 | . |
| Season: spring (vs autumn) | -1.4838 | 1.1431 | ±2.2862 | -1.298 | 0.1943 |  |
| **Season: summer (vs autumn)** | **+2.5575** | 1.3011 | ±2.6022 | **+1.966** | **0.0493** | * |
| **Season: winter (vs autumn)** | **-5.1938** | 1.0635 | ±2.1270 | **-4.884** | **1.04e-06** | *** |
| Age (years) | -0.0544 | 0.0375 | ±0.0749 | -1.453 | 0.1462 |  |
| BMI (kg/m2) | +0.0415 | 0.0624 | ±0.1249 | +0.665 | 0.5059 |  |
| Hypertension | -0.3741 | 0.9546 | ±1.9091 | -0.392 | 0.6951 |  |
| High cholesterol | -1.1045 | 0.8461 | ±1.6923 | -1.305 | 0.1918 |  |
| Kidney disease | -1.8652 | 1.6974 | ±3.3949 | -1.099 | 0.2718 |  |
| Circulatory disease | +2.2473 | 1.3568 | ±2.7136 | +1.656 | 0.0977 | . |
| MAG (mg/dL/h) | -0.0022 | 0.0471 | ±0.0943 | -0.048 | 0.9620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **241**, R² = **0.2682**, Adj R² = **0.2229**, F-statistic = **5.92** (p = **7.09e-10**), Residual SE = **5.980** on **226** df, AIC = **1560.4**, BIC = **1612.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4391** | 4.0221 | ±8.0442 | **+12.043** | **2.10e-33** | *** |
| Education: graduate level (vs college) | -0.1640 | 0.8593 | ±1.7185 | -0.191 | 0.8486 |  |
| Education: high school or below (vs college) | +0.4238 | 1.3192 | ±2.6385 | +0.321 | 0.7480 |  |
| Site: UCSD (vs UAB) | +2.0806 | 1.2013 | ±2.4026 | +1.732 | 0.0833 | . |
| Site: UW (vs UAB) | -1.8720 | 1.0501 | ±2.1003 | -1.783 | 0.0746 | . |
| Season: spring (vs autumn) | -1.4873 | 1.1399 | ±2.2798 | -1.305 | 0.1920 |  |
| **Season: summer (vs autumn)** | **+2.5658** | 1.3080 | ±2.6160 | **+1.962** | **0.0498** | * |
| **Season: winter (vs autumn)** | **-5.1883** | 1.0602 | ±2.1203 | **-4.894** | **9.88e-07** | *** |
| Age (years) | -0.0544 | 0.0375 | ±0.0750 | -1.451 | 0.1468 |  |
| BMI (kg/m2) | +0.0402 | 0.0629 | ±0.1259 | +0.639 | 0.5226 |  |
| Hypertension | -0.3692 | 0.9195 | ±1.8390 | -0.402 | 0.6880 |  |
| High cholesterol | -1.0849 | 0.8158 | ±1.6315 | -1.330 | 0.1835 |  |
| Kidney disease | -1.8754 | 1.7119 | ±3.4238 | -1.096 | 0.2733 |  |
| Circulatory disease | +2.2321 | 1.3541 | ±2.7082 | +1.648 | 0.0993 | . |
| Avg. daily range (mg/dL) | +0.0011 | 0.0147 | ±0.0294 | +0.075 | 0.9399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **241**, R² = **0.2703**, Adj R² = **0.2251**, F-statistic = **5.98** (p = **5.38e-10**), Residual SE = **5.971** on **226** df, AIC = **1559.8**, BIC = **1612.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8989** | 3.4154 | ±6.8307 | **+14.317** | **1.71e-46** | *** |
| Education: graduate level (vs college) | -0.2109 | 0.8695 | ±1.7390 | -0.243 | 0.8084 |  |
| Education: high school or below (vs college) | +0.5096 | 1.3037 | ±2.6074 | +0.391 | 0.6959 |  |
| Site: UCSD (vs UAB) | +2.0431 | 1.1974 | ±2.3948 | +1.706 | 0.0880 | . |
| Site: UW (vs UAB) | -1.8862 | 1.0304 | ±2.0608 | -1.831 | 0.0672 | . |
| Season: spring (vs autumn) | -1.3583 | 1.1526 | ±2.3053 | -1.178 | 0.2386 |  |
| Season: summer (vs autumn) | +2.5551 | 1.3043 | ±2.6086 | +1.959 | 0.0501 | . |
| **Season: winter (vs autumn)** | **-5.1436** | 1.0572 | ±2.1143 | **-4.866** | **1.14e-06** | *** |
| Age (years) | -0.0524 | 0.0371 | ±0.0741 | -1.415 | 0.1571 |  |
| BMI (kg/m2) | +0.0462 | 0.0627 | ±0.1255 | +0.737 | 0.4610 |  |
| Hypertension | -0.3870 | 0.9205 | ±1.8410 | -0.420 | 0.6742 |  |
| High cholesterol | -1.1257 | 0.8038 | ±1.6075 | -1.401 | 0.1613 |  |
| Kidney disease | -1.8183 | 1.7064 | ±3.4128 | -1.066 | 0.2866 |  |
| Circulatory disease | +2.2813 | 1.3403 | ±2.6805 | +1.702 | 0.0887 | . |
| SD of daily means (mg/dL) | -0.0677 | 0.0853 | ±0.1707 | -0.793 | 0.4279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **241**, R² = **0.2690**, Adj R² = **0.2238**, F-statistic = **5.94** (p = **6.38e-10**), Residual SE = **5.976** on **226** df, AIC = **1560.2**, BIC = **1612.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8068** | 3.8524 | ±7.7048 | **+12.929** | **3.10e-38** | *** |
| Education: graduate level (vs college) | -0.1865 | 0.8574 | ±1.7147 | -0.218 | 0.8278 |  |
| Education: high school or below (vs college) | +0.3207 | 1.3362 | ±2.6724 | +0.240 | 0.8103 |  |
| Site: UCSD (vs UAB) | +2.1072 | 1.2013 | ±2.4026 | +1.754 | 0.0794 | . |
| Site: UW (vs UAB) | -1.8711 | 1.0381 | ±2.0762 | -1.802 | 0.0715 | . |
| Season: spring (vs autumn) | -1.4832 | 1.1356 | ±2.2712 | -1.306 | 0.1915 |  |
| **Season: summer (vs autumn)** | **+2.6421** | 1.3008 | ±2.6017 | **+2.031** | **0.0422** | * |
| **Season: winter (vs autumn)** | **-5.1685** | 1.0576 | ±2.1152 | **-4.887** | **1.02e-06** | *** |
| Age (years) | -0.0541 | 0.0376 | ±0.0753 | -1.438 | 0.1503 |  |
| BMI (kg/m2) | +0.0348 | 0.0629 | ±0.1257 | +0.554 | 0.5798 |  |
| Hypertension | -0.3760 | 0.9208 | ±1.8416 | -0.408 | 0.6830 |  |
| High cholesterol | -1.1012 | 0.8074 | ±1.6147 | -1.364 | 0.1726 |  |
| Kidney disease | -1.9128 | 1.7070 | ±3.4140 | -1.121 | 0.2625 |  |
| Circulatory disease | +2.1757 | 1.3719 | ±2.7438 | +1.586 | 0.1128 |  |
| Time in range 70-180, pooled (%) | -0.0124 | 0.0225 | ±0.0450 | -0.552 | 0.5807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **241**, R² = **0.2693**, Adj R² = **0.2240**, F-statistic = **5.95** (p = **6.18e-10**), Residual SE = **5.976** on **226** df, AIC = **1560.1**, BIC = **1612.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9680** | 3.8568 | ±7.7137 | **+12.956** | **2.18e-38** | *** |
| Education: graduate level (vs college) | -0.1913 | 0.8573 | ±1.7147 | -0.223 | 0.8235 |  |
| Education: high school or below (vs college) | +0.3116 | 1.3347 | ±2.6695 | +0.233 | 0.8154 |  |
| Site: UCSD (vs UAB) | +2.1162 | 1.2012 | ±2.4025 | +1.762 | 0.0781 | . |
| Site: UW (vs UAB) | -1.8672 | 1.0385 | ±2.0771 | -1.798 | 0.0722 | . |
| Season: spring (vs autumn) | -1.4860 | 1.1360 | ±2.2720 | -1.308 | 0.1908 |  |
| **Season: summer (vs autumn)** | **+2.6523** | 1.3008 | ±2.6016 | **+2.039** | **0.0415** | * |
| **Season: winter (vs autumn)** | **-5.1660** | 1.0571 | ±2.1141 | **-4.887** | **1.02e-06** | *** |
| Age (years) | -0.0542 | 0.0376 | ±0.0753 | -1.439 | 0.1501 |  |
| BMI (kg/m2) | +0.0339 | 0.0630 | ±0.1260 | +0.539 | 0.5901 |  |
| Hypertension | -0.3777 | 0.9207 | ±1.8413 | -0.410 | 0.6817 |  |
| High cholesterol | -1.1020 | 0.8076 | ±1.6151 | -1.365 | 0.1724 |  |
| Kidney disease | -1.9216 | 1.7085 | ±3.4171 | -1.125 | 0.2607 |  |
| Circulatory disease | +2.1695 | 1.3713 | ±2.7426 | +1.582 | 0.1136 |  |
| Avg. daily time in range 70-180 (%) | -0.0140 | 0.0221 | ±0.0442 | -0.632 | 0.5271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.2692**, Adj R² = **0.2239**, F-statistic = **5.95** (p = **6.28e-10**), Residual SE = **5.976** on **226** df, AIC = **1560.1**, BIC = **1612.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6746** | 3.3462 | ±6.6924 | **+14.546** | **6.17e-48** | *** |
| Education: graduate level (vs college) | -0.2049 | 0.8705 | ±1.7411 | -0.235 | 0.8139 |  |
| Education: high school or below (vs college) | +0.3419 | 1.3402 | ±2.6804 | +0.255 | 0.7986 |  |
| Site: UCSD (vs UAB) | +2.0712 | 1.1943 | ±2.3887 | +1.734 | 0.0829 | . |
| Site: UW (vs UAB) | -1.9036 | 1.0371 | ±2.0743 | -1.835 | 0.0664 | . |
| Season: spring (vs autumn) | -1.5098 | 1.1407 | ±2.2815 | -1.324 | 0.1857 |  |
| Season: summer (vs autumn) | +2.5291 | 1.3036 | ±2.6072 | +1.940 | 0.0524 | . |
| **Season: winter (vs autumn)** | **-5.2155** | 1.0560 | ±2.1119 | **-4.939** | **7.85e-07** | *** |
| Age (years) | -0.0536 | 0.0376 | ±0.0752 | -1.425 | 0.1541 |  |
| BMI (kg/m2) | +0.0430 | 0.0630 | ±0.1260 | +0.683 | 0.4947 |  |
| Hypertension | -0.3795 | 0.9193 | ±1.8386 | -0.413 | 0.6797 |  |
| High cholesterol | -1.1364 | 0.8019 | ±1.6037 | -1.417 | 0.1564 |  |
| Kidney disease | -1.8132 | 1.7055 | ±3.4110 | -1.063 | 0.2877 |  |
| Circulatory disease | +2.2443 | 1.3468 | ±2.6935 | +1.666 | 0.0956 | . |
| Any reading < 54 during wear (0/1) | -0.4800 | 0.9291 | ±1.8582 | -0.517 | 0.6055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.2733**, Adj R² = **0.2283**, F-statistic = **6.07** (p = **3.58e-10**), Residual SE = **5.959** on **226** df, AIC = **1558.7**, BIC = **1611.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8537** | 3.3476 | ±6.6952 | **+14.594** | **3.08e-48** | *** |
| Education: graduate level (vs college) | -0.2627 | 0.8646 | ±1.7292 | -0.304 | 0.7613 |  |
| Education: high school or below (vs college) | +0.2709 | 1.3088 | ±2.6177 | +0.207 | 0.8360 |  |
| Site: UCSD (vs UAB) | +1.9658 | 1.1869 | ±2.3737 | +1.656 | 0.0977 | . |
| **Site: UW (vs UAB)** | **-2.0404** | 1.0407 | ±2.0813 | **-1.961** | **0.0499** | * |
| Season: spring (vs autumn) | -1.4847 | 1.1306 | ±2.2612 | -1.313 | 0.1891 |  |
| **Season: summer (vs autumn)** | **+2.5419** | 1.2966 | ±2.5932 | **+1.960** | **0.0499** | * |
| **Season: winter (vs autumn)** | **-5.0774** | 1.0622 | ±2.1244 | **-4.780** | **1.75e-06** | *** |
| Age (years) | -0.0509 | 0.0374 | ±0.0748 | -1.361 | 0.1735 |  |
| BMI (kg/m2) | +0.0338 | 0.0621 | ±0.1241 | +0.545 | 0.5860 |  |
| Hypertension | -0.4267 | 0.9224 | ±1.8447 | -0.463 | 0.6436 |  |
| High cholesterol | -1.1957 | 0.8051 | ±1.6101 | -1.485 | 0.1375 |  |
| Kidney disease | -1.8887 | 1.6840 | ±3.3680 | -1.122 | 0.2621 |  |
| Circulatory disease | +2.2234 | 1.3329 | ±2.6659 | +1.668 | 0.0953 | . |
| Time < 54 (%) | -0.5257 | 0.2910 | ±0.5821 | -1.806 | 0.0709 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.2730**, Adj R² = **0.2280**, F-statistic = **6.06** (p = **3.75e-10**), Residual SE = **5.960** on **226** df, AIC = **1558.9**, BIC = **1611.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8118** | 3.3449 | ±6.6898 | **+14.593** | **3.12e-48** | *** |
| Education: graduate level (vs college) | -0.2542 | 0.8640 | ±1.7281 | -0.294 | 0.7686 |  |
| Education: high school or below (vs college) | +0.2704 | 1.3091 | ±2.6183 | +0.207 | 0.8364 |  |
| Site: UCSD (vs UAB) | +1.9712 | 1.1847 | ±2.3695 | +1.664 | 0.0961 | . |
| **Site: UW (vs UAB)** | **-2.0575** | 1.0421 | ±2.0841 | **-1.974** | **0.0483** | * |
| Season: spring (vs autumn) | -1.4739 | 1.1317 | ±2.2635 | -1.302 | 0.1928 |  |
| Season: summer (vs autumn) | +2.5254 | 1.2978 | ±2.5955 | +1.946 | 0.0517 | . |
| **Season: winter (vs autumn)** | **-5.0584** | 1.0684 | ±2.1369 | **-4.734** | **2.20e-06** | *** |
| Age (years) | -0.0510 | 0.0374 | ±0.0749 | -1.362 | 0.1733 |  |
| BMI (kg/m2) | +0.0355 | 0.0620 | ±0.1241 | +0.572 | 0.5675 |  |
| Hypertension | -0.4312 | 0.9257 | ±1.8515 | -0.466 | 0.6414 |  |
| High cholesterol | -1.2150 | 0.8078 | ±1.6155 | -1.504 | 0.1325 |  |
| Kidney disease | -1.8853 | 1.6815 | ±3.3630 | -1.121 | 0.2622 |  |
| Circulatory disease | +2.2346 | 1.3295 | ±2.6589 | +1.681 | 0.0928 | . |
| Avg. daily time < 54 (%) | -0.6731 | 0.4789 | ±0.9578 | -1.406 | 0.1599 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.2685**, Adj R² = **0.2231**, F-statistic = **5.92** (p = **6.88e-10**), Residual SE = **5.979** on **226** df, AIC = **1560.4**, BIC = **1612.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5601** | 3.3500 | ±6.7001 | **+14.495** | **1.30e-47** | *** |
| Education: graduate level (vs college) | -0.1343 | 0.8746 | ±1.7492 | -0.154 | 0.8780 |  |
| Education: high school or below (vs college) | +0.4722 | 1.3303 | ±2.6605 | +0.355 | 0.7226 |  |
| Site: UCSD (vs UAB) | +2.0831 | 1.1885 | ±2.3770 | +1.753 | 0.0797 | . |
| Site: UW (vs UAB) | -1.8480 | 1.0354 | ±2.0709 | -1.785 | 0.0743 | . |
| Season: spring (vs autumn) | -1.4845 | 1.1375 | ±2.2750 | -1.305 | 0.1919 |  |
| **Season: summer (vs autumn)** | **+2.5830** | 1.2986 | ±2.5973 | **+1.989** | **0.0467** | * |
| **Season: winter (vs autumn)** | **-5.2077** | 1.0673 | ±2.1347 | **-4.879** | **1.07e-06** | *** |
| Age (years) | -0.0548 | 0.0374 | ±0.0748 | -1.466 | 0.1425 |  |
| BMI (kg/m2) | +0.0392 | 0.0626 | ±0.1253 | +0.626 | 0.5312 |  |
| Hypertension | -0.3560 | 0.9238 | ±1.8476 | -0.385 | 0.7000 |  |
| High cholesterol | -1.0624 | 0.8102 | ±1.6203 | -1.311 | 0.1898 |  |
| Kidney disease | -1.8707 | 1.6932 | ±3.3863 | -1.105 | 0.2692 |  |
| Circulatory disease | +2.2520 | 1.3428 | ±2.6857 | +1.677 | 0.0935 | . |
| Time 54-69, pooled (%) | +0.0858 | 0.2491 | ±0.4981 | +0.345 | 0.7304 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **241**, R² = **0.2690**, Adj R² = **0.2238**, F-statistic = **5.94** (p = **6.37e-10**), Residual SE = **5.976** on **226** df, AIC = **1560.2**, BIC = **1612.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5511** | 3.3491 | ±6.6982 | **+14.497** | **1.27e-47** | *** |
| Education: graduate level (vs college) | -0.1097 | 0.8729 | ±1.7458 | -0.126 | 0.8999 |  |
| Education: high school or below (vs college) | +0.5121 | 1.3315 | ±2.6631 | +0.385 | 0.7006 |  |
| Site: UCSD (vs UAB) | +2.0958 | 1.1874 | ±2.3749 | +1.765 | 0.0776 | . |
| Site: UW (vs UAB) | -1.8142 | 1.0348 | ±2.0696 | -1.753 | 0.0796 | . |
| Season: spring (vs autumn) | -1.4887 | 1.1369 | ±2.2737 | -1.310 | 0.1904 |  |
| **Season: summer (vs autumn)** | **+2.5995** | 1.2995 | ±2.5989 | **+2.000** | **0.0455** | * |
| **Season: winter (vs autumn)** | **-5.2327** | 1.0685 | ±2.1370 | **-4.897** | **9.72e-07** | *** |
| Age (years) | -0.0553 | 0.0373 | ±0.0747 | -1.482 | 0.1383 |  |
| BMI (kg/m2) | +0.0382 | 0.0624 | ±0.1248 | +0.612 | 0.5407 |  |
| Hypertension | -0.3438 | 0.9237 | ±1.8473 | -0.372 | 0.7097 |  |
| High cholesterol | -1.0305 | 0.8097 | ±1.6194 | -1.273 | 0.2031 |  |
| Kidney disease | -1.8732 | 1.6917 | ±3.3834 | -1.107 | 0.2682 |  |
| Circulatory disease | +2.2598 | 1.3415 | ±2.6830 | +1.685 | 0.0921 | . |
| Avg. daily time 54-69 (%) | +0.1502 | 0.2304 | ±0.4609 | +0.652 | 0.5146 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **241**, R² = **0.2689**, Adj R² = **0.2236**, F-statistic = **5.94** (p = **6.52e-10**), Residual SE = **5.977** on **226** df, AIC = **1560.2**, BIC = **1612.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6486** | 3.3531 | ±6.7063 | **+14.508** | **1.07e-47** | *** |
| Education: graduate level (vs college) | -0.2122 | 0.8731 | ±1.7462 | -0.243 | 0.8080 |  |
| Education: high school or below (vs college) | +0.3474 | 1.3293 | ±2.6587 | +0.261 | 0.7938 |  |
| Site: UCSD (vs UAB) | +2.0359 | 1.1883 | ±2.3765 | +1.713 | 0.0866 | . |
| Site: UW (vs UAB) | -1.9438 | 1.0399 | ±2.0797 | -1.869 | 0.0616 | . |
| Season: spring (vs autumn) | -1.4867 | 1.1361 | ±2.2722 | -1.309 | 0.1907 |  |
| Season: summer (vs autumn) | +2.5360 | 1.3009 | ±2.6018 | +1.949 | 0.0512 | . |
| **Season: winter (vs autumn)** | **-5.1532** | 1.0725 | ±2.1451 | **-4.805** | **1.55e-06** | *** |
| Age (years) | -0.0533 | 0.0375 | ±0.0749 | -1.424 | 0.1545 |  |
| BMI (kg/m2) | +0.0415 | 0.0628 | ±0.1256 | +0.660 | 0.5090 |  |
| Hypertension | -0.3919 | 0.9272 | ±1.8543 | -0.423 | 0.6726 |  |
| High cholesterol | -1.1510 | 0.8100 | ±1.6199 | -1.421 | 0.1553 |  |
| Kidney disease | -1.8621 | 1.6911 | ±3.3822 | -1.101 | 0.2708 |  |
| Circulatory disease | +2.2296 | 1.3408 | ±2.6816 | +1.663 | 0.0963 | . |
| Time < 70 (%) | -0.0937 | 0.2580 | ±0.5160 | -0.363 | 0.7166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **241**, R² = **0.2683**, Adj R² = **0.2229**, F-statistic = **5.92** (p = **7.07e-10**), Residual SE = **5.980** on **226** df, AIC = **1560.4**, BIC = **1612.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5916** | 3.3563 | ±6.7126 | **+14.478** | **1.68e-47** | *** |
| Education: graduate level (vs college) | -0.1747 | 0.8718 | ±1.7437 | -0.200 | 0.8412 |  |
| Education: high school or below (vs college) | +0.4066 | 1.3302 | ±2.6605 | +0.306 | 0.7599 |  |
| Site: UCSD (vs UAB) | +2.0617 | 1.1879 | ±2.3758 | +1.736 | 0.0826 | . |
| Site: UW (vs UAB) | -1.8968 | 1.0388 | ±2.0776 | -1.826 | 0.0679 | . |
| Season: spring (vs autumn) | -1.4848 | 1.1374 | ±2.2749 | -1.305 | 0.1918 |  |
| **Season: summer (vs autumn)** | **+2.5551** | 1.3017 | ±2.6034 | **+1.963** | **0.0497** | * |
| **Season: winter (vs autumn)** | **-5.1801** | 1.0745 | ±2.1491 | **-4.821** | **1.43e-06** | *** |
| Age (years) | -0.0541 | 0.0374 | ±0.0748 | -1.447 | 0.1480 |  |
| BMI (kg/m2) | +0.0412 | 0.0628 | ±0.1256 | +0.655 | 0.5122 |  |
| Hypertension | -0.3742 | 0.9277 | ±1.8553 | -0.403 | 0.6867 |  |
| High cholesterol | -1.1109 | 0.8110 | ±1.6219 | -1.370 | 0.1708 |  |
| Kidney disease | -1.8639 | 1.6908 | ±3.3816 | -1.102 | 0.2703 |  |
| Circulatory disease | +2.2400 | 1.3408 | ±2.6817 | +1.671 | 0.0948 | . |
| Avg. daily time < 70 (%) | -0.0237 | 0.2424 | ±0.4848 | -0.098 | 0.9222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.2704**, Adj R² = **0.2252**, F-statistic = **5.98** (p = **5.31e-10**), Residual SE = **5.971** on **226** df, AIC = **1559.7**, BIC = **1612.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.5130** | 4.1460 | ±8.2920 | **+12.425** | **1.92e-35** | *** |
| Education: graduate level (vs college) | -0.1582 | 0.8583 | ±1.7166 | -0.184 | 0.8537 |  |
| Education: high school or below (vs college) | +0.1961 | 1.3707 | ±2.7415 | +0.143 | 0.8862 |  |
| Site: UCSD (vs UAB) | +2.1147 | 1.1976 | ±2.3952 | +1.766 | 0.0774 | . |
| Site: UW (vs UAB) | -1.8485 | 1.0391 | ±2.0782 | -1.779 | 0.0752 | . |
| Season: spring (vs autumn) | -1.5050 | 1.1360 | ±2.2720 | -1.325 | 0.1852 |  |
| **Season: summer (vs autumn)** | **+2.6352** | 1.3043 | ±2.6085 | **+2.020** | **0.0433** | * |
| **Season: winter (vs autumn)** | **-5.1804** | 1.0579 | ±2.1157 | **-4.897** | **9.73e-07** | *** |
| Age (years) | -0.0534 | 0.0375 | ±0.0751 | -1.423 | 0.1548 |  |
| BMI (kg/m2) | +0.0386 | 0.0620 | ±0.1240 | +0.623 | 0.5334 |  |
| Hypertension | -0.3438 | 0.9238 | ±1.8477 | -0.372 | 0.7098 |  |
| High cholesterol | -1.0630 | 0.8052 | ±1.6103 | -1.320 | 0.1868 |  |
| Kidney disease | -1.8343 | 1.7003 | ±3.4007 | -1.079 | 0.2807 |  |
| Circulatory disease | +2.0760 | 1.3809 | ±2.7617 | +1.503 | 0.1327 |  |
| Time 54-250, pooled (%) | -0.0304 | 0.0294 | ±0.0588 | -1.035 | 0.3008 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.2706**, Adj R² = **0.2254**, F-statistic = **5.99** (p = **5.16e-10**), Residual SE = **5.970** on **226** df, AIC = **1559.7**, BIC = **1611.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7327** | 4.2114 | ±8.4229 | **+12.284** | **1.11e-34** | *** |
| Education: graduate level (vs college) | -0.1602 | 0.8577 | ±1.7154 | -0.187 | 0.8518 |  |
| Education: high school or below (vs college) | +0.1799 | 1.3714 | ±2.7428 | +0.131 | 0.8956 |  |
| Site: UCSD (vs UAB) | +2.1175 | 1.1973 | ±2.3946 | +1.769 | 0.0770 | . |
| Site: UW (vs UAB) | -1.8503 | 1.0387 | ±2.0773 | -1.781 | 0.0748 | . |
| Season: spring (vs autumn) | -1.5036 | 1.1354 | ±2.2707 | -1.324 | 0.1854 |  |
| **Season: summer (vs autumn)** | **+2.6415** | 1.3046 | ±2.6092 | **+2.025** | **0.0429** | * |
| **Season: winter (vs autumn)** | **-5.1745** | 1.0579 | ±2.1159 | **-4.891** | **1.00e-06** | *** |
| Age (years) | -0.0534 | 0.0376 | ±0.0751 | -1.421 | 0.1552 |  |
| BMI (kg/m2) | +0.0380 | 0.0620 | ±0.1240 | +0.613 | 0.5396 |  |
| Hypertension | -0.3445 | 0.9234 | ±1.8469 | -0.373 | 0.7091 |  |
| High cholesterol | -1.0603 | 0.8052 | ±1.6105 | -1.317 | 0.1879 |  |
| Kidney disease | -1.8296 | 1.7009 | ±3.4019 | -1.076 | 0.2821 |  |
| Circulatory disease | +2.0640 | 1.3824 | ±2.7648 | +1.493 | 0.1354 |  |
| Avg. daily time 54-250 (%) | -0.0325 | 0.0303 | ±0.0606 | -1.074 | 0.2830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.2683**, Adj R² = **0.2229**, F-statistic = **5.92** (p = **7.07e-10**), Residual SE = **5.980** on **226** df, AIC = **1560.4**, BIC = **1612.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5668** | 3.3579 | ±6.7157 | **+14.464** | **2.06e-47** | *** |
| Education: graduate level (vs college) | -0.1516 | 0.8600 | ±1.7201 | -0.176 | 0.8601 |  |
| Education: high school or below (vs college) | +0.4326 | 1.3159 | ±2.6317 | +0.329 | 0.7423 |  |
| Site: UCSD (vs UAB) | +2.0627 | 1.1915 | ±2.3830 | +1.731 | 0.0834 | . |
| Site: UW (vs UAB) | -1.8769 | 1.0331 | ±2.0662 | -1.817 | 0.0693 | . |
| Season: spring (vs autumn) | -1.4896 | 1.1341 | ±2.2682 | -1.313 | 0.1890 |  |
| **Season: summer (vs autumn)** | **+2.5441** | 1.2966 | ±2.5932 | **+1.962** | **0.0497** | * |
| **Season: winter (vs autumn)** | **-5.1993** | 1.0575 | ±2.1151 | **-4.916** | **8.81e-07** | *** |
| Age (years) | -0.0544 | 0.0375 | ±0.0750 | -1.450 | 0.1470 |  |
| BMI (kg/m2) | +0.0428 | 0.0642 | ±0.1284 | +0.667 | 0.5048 |  |
| Hypertension | -0.3606 | 0.9247 | ±1.8493 | -0.390 | 0.6965 |  |
| High cholesterol | -1.0872 | 0.8073 | ±1.6146 | -1.347 | 0.1780 |  |
| Kidney disease | -1.8414 | 1.6853 | ±3.3705 | -1.093 | 0.2745 |  |
| Circulatory disease | +2.2431 | 1.3416 | ±2.6833 | +1.672 | 0.0945 | . |
| Time 181-250, pooled (%) | -0.0048 | 0.0400 | ±0.0800 | -0.120 | 0.9044 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **241**, R² = **0.2682**, Adj R² = **0.2229**, F-statistic = **5.92** (p = **7.10e-10**), Residual SE = **5.980** on **226** df, AIC = **1560.4**, BIC = **1612.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5739** | 3.3609 | ±6.7218 | **+14.453** | **2.41e-47** | *** |
| Education: graduate level (vs college) | -0.1583 | 0.8609 | ±1.7218 | -0.184 | 0.8542 |  |
| Education: high school or below (vs college) | +0.4280 | 1.3179 | ±2.6357 | +0.325 | 0.7454 |  |
| Site: UCSD (vs UAB) | +2.0661 | 1.1920 | ±2.3840 | +1.733 | 0.0830 | . |
| Site: UW (vs UAB) | -1.8793 | 1.0339 | ±2.0678 | -1.818 | 0.0691 | . |
| Season: spring (vs autumn) | -1.4867 | 1.1354 | ±2.2707 | -1.309 | 0.1904 |  |
| **Season: summer (vs autumn)** | **+2.5550** | 1.2959 | ±2.5919 | **+1.972** | **0.0487** | * |
| **Season: winter (vs autumn)** | **-5.1944** | 1.0566 | ±2.1131 | **-4.916** | **8.82e-07** | *** |
| Age (years) | -0.0544 | 0.0375 | ±0.0750 | -1.450 | 0.1470 |  |
| BMI (kg/m2) | +0.0417 | 0.0643 | ±0.1286 | +0.648 | 0.5169 |  |
| Hypertension | -0.3651 | 0.9247 | ±1.8495 | -0.395 | 0.6930 |  |
| High cholesterol | -1.0925 | 0.8081 | ±1.6163 | -1.352 | 0.1764 |  |
| Kidney disease | -1.8546 | 1.6881 | ±3.3762 | -1.099 | 0.2719 |  |
| Circulatory disease | +2.2427 | 1.3424 | ±2.6847 | +1.671 | 0.0948 | . |
| Avg. daily time 181-250 (%) | -0.0019 | 0.0387 | ±0.0774 | -0.050 | 0.9598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **241**, R² = **0.2692**, Adj R² = **0.2239**, F-statistic = **5.95** (p = **6.24e-10**), Residual SE = **5.976** on **226** df, AIC = **1560.1**, BIC = **1612.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5713** | 3.3778 | ±6.7557 | **+14.379** | **6.97e-47** | *** |
| Education: graduate level (vs college) | -0.1957 | 0.8568 | ±1.7136 | -0.228 | 0.8193 |  |
| Education: high school or below (vs college) | +0.2999 | 1.3388 | ±2.6777 | +0.224 | 0.8227 |  |
| Site: UCSD (vs UAB) | +2.1057 | 1.2003 | ±2.4006 | +1.754 | 0.0794 | . |
| Site: UW (vs UAB) | -1.8795 | 1.0362 | ±2.0725 | -1.814 | 0.0697 | . |
| Season: spring (vs autumn) | -1.4832 | 1.1353 | ±2.2706 | -1.306 | 0.1914 |  |
| **Season: summer (vs autumn)** | **+2.6455** | 1.3017 | ±2.6033 | **+2.032** | **0.0421** | * |
| **Season: winter (vs autumn)** | **-5.1610** | 1.0578 | ±2.1156 | **-4.879** | **1.07e-06** | *** |
| Age (years) | -0.0540 | 0.0377 | ±0.0753 | -1.433 | 0.1520 |  |
| BMI (kg/m2) | +0.0343 | 0.0627 | ±0.1254 | +0.548 | 0.5839 |  |
| Hypertension | -0.3801 | 0.9204 | ±1.8409 | -0.413 | 0.6796 |  |
| High cholesterol | -1.1096 | 0.8073 | ±1.6145 | -1.374 | 0.1693 |  |
| Kidney disease | -1.9168 | 1.7075 | ±3.4149 | -1.123 | 0.2616 |  |
| Circulatory disease | +2.1677 | 1.3730 | ±2.7460 | +1.579 | 0.1144 |  |
| Time > 180 (%) | +0.0136 | 0.0222 | ±0.0443 | +0.612 | 0.5407 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **241**, R² = **0.2693**, Adj R² = **0.2240**, F-statistic = **5.95** (p = **6.15e-10**), Residual SE = **5.975** on **226** df, AIC = **1560.1**, BIC = **1612.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5779** | 3.3764 | ±6.7527 | **+14.388** | **6.19e-47** | *** |
| Education: graduate level (vs college) | -0.1984 | 0.8571 | ±1.7142 | -0.232 | 0.8169 |  |
| Education: high school or below (vs college) | +0.2993 | 1.3372 | ±2.6743 | +0.224 | 0.8229 |  |
| Site: UCSD (vs UAB) | +2.1121 | 1.2006 | ±2.4012 | +1.759 | 0.0786 | . |
| Site: UW (vs UAB) | -1.8770 | 1.0366 | ±2.0732 | -1.811 | 0.0702 | . |
| Season: spring (vs autumn) | -1.4855 | 1.1358 | ±2.2716 | -1.308 | 0.1909 |  |
| **Season: summer (vs autumn)** | **+2.6488** | 1.3015 | ±2.6029 | **+2.035** | **0.0418** | * |
| **Season: winter (vs autumn)** | **-5.1591** | 1.0572 | ±2.1143 | **-4.880** | **1.06e-06** | *** |
| Age (years) | -0.0540 | 0.0377 | ±0.0753 | -1.434 | 0.1516 |  |
| BMI (kg/m2) | +0.0340 | 0.0628 | ±0.1257 | +0.541 | 0.5884 |  |
| Hypertension | -0.3813 | 0.9205 | ±1.8410 | -0.414 | 0.6787 |  |
| High cholesterol | -1.1108 | 0.8076 | ±1.6152 | -1.375 | 0.1690 |  |
| Kidney disease | -1.9217 | 1.7078 | ±3.4156 | -1.125 | 0.2605 |  |
| Circulatory disease | +2.1671 | 1.3717 | ±2.7434 | +1.580 | 0.1141 |  |
| Avg. daily time > 180 (%) | +0.0141 | 0.0219 | ±0.0437 | +0.644 | 0.5193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **241**, R² = **0.2698**, Adj R² = **0.2246**, F-statistic = **5.96** (p = **5.77e-10**), Residual SE = **5.973** on **226** df, AIC = **1559.9**, BIC = **1612.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6477** | 3.3782 | ±6.7565 | **+14.400** | **5.15e-47** | *** |
| Education: graduate level (vs college) | -0.1661 | 0.8600 | ±1.7201 | -0.193 | 0.8468 |  |
| Education: high school or below (vs college) | +0.3163 | 1.3364 | ±2.6727 | +0.237 | 0.8129 |  |
| Site: UCSD (vs UAB) | +2.0948 | 1.1933 | ±2.3867 | +1.755 | 0.0792 | . |
| Site: UW (vs UAB) | -1.8730 | 1.0373 | ±2.0746 | -1.806 | 0.0710 | . |
| Season: spring (vs autumn) | -1.5277 | 1.1430 | ±2.2860 | -1.337 | 0.1814 |  |
| **Season: summer (vs autumn)** | **+2.6565** | 1.2901 | ±2.5802 | **+2.059** | **0.0395** | * |
| **Season: winter (vs autumn)** | **-5.1882** | 1.0580 | ±2.1159 | **-4.904** | **9.39e-07** | *** |
| Age (years) | -0.0531 | 0.0376 | ±0.0752 | -1.412 | 0.1578 |  |
| BMI (kg/m2) | +0.0313 | 0.0642 | ±0.1285 | +0.487 | 0.6265 |  |
| Hypertension | -0.3645 | 0.9207 | ±1.8413 | -0.396 | 0.6922 |  |
| High cholesterol | -1.1239 | 0.8071 | ±1.6143 | -1.392 | 0.1638 |  |
| Kidney disease | -1.8246 | 1.7166 | ±3.4333 | -1.063 | 0.2878 |  |
| Circulatory disease | +2.1718 | 1.3583 | ±2.7166 | +1.599 | 0.1098 |  |
| Nocturnal time > 180 (%) | +0.0163 | 0.0199 | ±0.0397 | +0.822 | 0.4113 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.2711**, Adj R² = **0.2259**, F-statistic = **6.00** (p = **4.86e-10**), Residual SE = **5.968** on **226** df, AIC = **1559.5**, BIC = **1611.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4709** | 3.3777 | ±6.7554 | **+14.350** | **1.06e-46** | *** |
| Education: graduate level (vs college) | -0.1641 | 0.8566 | ±1.7132 | -0.192 | 0.8480 |  |
| Education: high school or below (vs college) | +0.1534 | 1.3708 | ±2.7415 | +0.112 | 0.9109 |  |
| Site: UCSD (vs UAB) | +2.1143 | 1.1956 | ±2.3912 | +1.768 | 0.0770 | . |
| Site: UW (vs UAB) | -1.8546 | 1.0375 | ±2.0750 | -1.788 | 0.0739 | . |
| Season: spring (vs autumn) | -1.5077 | 1.1349 | ±2.2698 | -1.328 | 0.1840 |  |
| **Season: summer (vs autumn)** | **+2.6442** | 1.3040 | ±2.6080 | **+2.028** | **0.0426** | * |
| **Season: winter (vs autumn)** | **-5.1713** | 1.0573 | ±2.1147 | **-4.891** | **1.00e-06** | *** |
| Age (years) | -0.0531 | 0.0376 | ±0.0751 | -1.412 | 0.1579 |  |
| BMI (kg/m2) | +0.0378 | 0.0619 | ±0.1238 | +0.611 | 0.5410 |  |
| Hypertension | -0.3442 | 0.9225 | ±1.8450 | -0.373 | 0.7091 |  |
| High cholesterol | -1.0649 | 0.8053 | ±1.6107 | -1.322 | 0.1861 |  |
| Kidney disease | -1.8317 | 1.7012 | ±3.4023 | -1.077 | 0.2816 |  |
| Circulatory disease | +2.0511 | 1.3809 | ±2.7619 | +1.485 | 0.1375 |  |
| Time > 250 (%) | +0.0348 | 0.0290 | ±0.0580 | +1.199 | 0.2306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 241)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **241**, R² = **0.2711**, Adj R² = **0.2260**, F-statistic = **6.00** (p = **4.83e-10**), Residual SE = **5.968** on **226** df, AIC = **1559.5**, BIC = **1611.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4830** | 3.3767 | ±6.7535 | **+14.358** | **9.50e-47** | *** |
| Education: graduate level (vs college) | -0.1648 | 0.8565 | ±1.7130 | -0.192 | 0.8474 |  |
| Education: high school or below (vs college) | +0.1474 | 1.3715 | ±2.7430 | +0.107 | 0.9144 |  |
| Site: UCSD (vs UAB) | +2.1170 | 1.1958 | ±2.3916 | +1.770 | 0.0767 | . |
| Site: UW (vs UAB) | -1.8568 | 1.0374 | ±2.0749 | -1.790 | 0.0735 | . |
| Season: spring (vs autumn) | -1.5048 | 1.1344 | ±2.2689 | -1.326 | 0.1847 |  |
| **Season: summer (vs autumn)** | **+2.6474** | 1.3045 | ±2.6089 | **+2.029** | **0.0424** | * |
| **Season: winter (vs autumn)** | **-5.1657** | 1.0576 | ±2.1152 | **-4.884** | **1.04e-06** | *** |
| Age (years) | -0.0531 | 0.0376 | ±0.0751 | -1.413 | 0.1576 |  |
| BMI (kg/m2) | +0.0375 | 0.0619 | ±0.1239 | +0.605 | 0.5453 |  |
| Hypertension | -0.3455 | 0.9224 | ±1.8447 | -0.375 | 0.7080 |  |
| High cholesterol | -1.0631 | 0.8054 | ±1.6108 | -1.320 | 0.1869 |  |
| Kidney disease | -1.8273 | 1.7014 | ±3.4028 | -1.074 | 0.2828 |  |
| Circulatory disease | +2.0458 | 1.3818 | ±2.7635 | +1.481 | 0.1387 |  |
| Avg. daily time > 250 (%) | +0.0357 | 0.0301 | ±0.0601 | +1.189 | 0.2345 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 241; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **241**, R² = **0.1391**, Adj R² = **0.0897**, F-statistic = **2.82** (p = **9.10e-04**), Residual SE = **14.381** on **227** df, AIC = **1982.5**, BIC = **2031.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.9568** | 8.7335 | ±17.4671 | **+14.880** | **4.43e-50** | *** |
| Education: graduate level (vs college) | -2.0512 | 1.9743 | ±3.9486 | -1.039 | 0.2988 |  |
| Education: high school or below (vs college) | +9.6672 | 5.4109 | ±10.8219 | +1.787 | 0.0740 | . |
| Site: UCSD (vs UAB) | +0.3258 | 2.9304 | ±5.8607 | +0.111 | 0.9115 |  |
| **Site: UW (vs UAB)** | **-6.1309** | 2.5829 | ±5.1657 | **-2.374** | **0.0176** | * |
| **Season: spring (vs autumn)** | **+5.2652** | 2.6849 | ±5.3697 | **+1.961** | **0.0499** | * |
| Season: summer (vs autumn) | -1.3868 | 3.2519 | ±6.5038 | -0.426 | 0.6698 |  |
| Season: winter (vs autumn) | -1.6027 | 2.6483 | ±5.2966 | -0.605 | 0.5451 |  |
| Age (years) | -0.1535 | 0.0898 | ±0.1796 | -1.710 | 0.0873 | . |
| BMI (kg/m2) | +0.2688 | 0.1803 | ±0.3607 | +1.491 | 0.1361 |  |
| Hypertension | -0.4189 | 2.1737 | ±4.3473 | -0.193 | 0.8472 |  |
| High cholesterol | +1.3678 | 1.9664 | ±3.9329 | +0.696 | 0.4867 |  |
| Kidney disease | -1.5716 | 3.9656 | ±7.9312 | -0.396 | 0.6919 |  |
| Circulatory disease | -1.8781 | 3.3403 | ±6.6805 | -0.562 | 0.5739 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **241**, R² = **0.1530**, Adj R² = **0.1006**, F-statistic = **2.92** (p = **4.33e-04**), Residual SE = **14.295** on **226** df, AIC = **1980.5**, BIC = **2032.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+140.8750** | 10.8912 | ±21.7825 | **+12.935** | **2.87e-38** | *** |
| Education: graduate level (vs college) | -2.0226 | 1.9592 | ±3.9183 | -1.032 | 0.3019 |  |
| **Education: high school or below (vs college)** | **+10.9560** | 5.4388 | ±10.8776 | **+2.014** | **0.0440** | * |
| Site: UCSD (vs UAB) | +0.3040 | 2.9275 | ±5.8550 | +0.104 | 0.9173 |  |
| **Site: UW (vs UAB)** | **-6.0029** | 2.5625 | ±5.1251 | **-2.343** | **0.0192** | * |
| **Season: spring (vs autumn)** | **+5.2720** | 2.6707 | ±5.3414 | **+1.974** | **0.0484** | * |
| Season: summer (vs autumn) | -1.6999 | 3.2414 | ±6.4829 | -0.524 | 0.6000 |  |
| Season: winter (vs autumn) | -1.5545 | 2.6351 | ±5.2702 | -0.590 | 0.5552 |  |
| Age (years) | -0.1499 | 0.0896 | ±0.1792 | -1.673 | 0.0943 | . |
| BMI (kg/m2) | +0.3002 | 0.1802 | ±0.3605 | +1.666 | 0.0958 | . |
| Hypertension | -0.3987 | 2.1362 | ±4.2724 | -0.187 | 0.8519 |  |
| High cholesterol | +1.6296 | 1.9431 | ±3.8862 | +0.839 | 0.4016 |  |
| Kidney disease | -1.9827 | 4.0337 | ±8.0675 | -0.492 | 0.6230 |  |
| Circulatory disease | -0.7326 | 3.4696 | ±6.9392 | -0.211 | 0.8328 |  |
| HbA1c (%) | -2.0637 | 1.0920 | ±2.1841 | -1.890 | 0.0588 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **241**, R² = **0.1417**, Adj R² = **0.0885**, F-statistic = **2.66** (p = **0.0013**), Residual SE = **14.391** on **226** df, AIC = **1983.7**, BIC = **2036.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.3067** | 10.4181 | ±20.8362 | **+12.796** | **1.73e-37** | *** |
| Education: graduate level (vs college) | -1.9117 | 1.9714 | ±3.9428 | -0.970 | 0.3322 |  |
| Education: high school or below (vs college) | +10.2716 | 5.4710 | ±10.9420 | +1.877 | 0.0605 | . |
| Site: UCSD (vs UAB) | +0.1940 | 2.9465 | ±5.8930 | +0.066 | 0.9475 |  |
| **Site: UW (vs UAB)** | **-6.1021** | 2.5847 | ±5.1693 | **-2.361** | **0.0182** | * |
| **Season: spring (vs autumn)** | **+5.2970** | 2.6994 | ±5.3987 | **+1.962** | **0.0497** | * |
| Season: summer (vs autumn) | -1.6739 | 3.2816 | ±6.5631 | -0.510 | 0.6100 |  |
| Season: winter (vs autumn) | -1.7808 | 2.6785 | ±5.3571 | -0.665 | 0.5061 |  |
| Age (years) | -0.1547 | 0.0907 | ±0.1814 | -1.705 | 0.0881 | . |
| BMI (kg/m2) | +0.2878 | 0.1816 | ±0.3632 | +1.585 | 0.1130 |  |
| Hypertension | -0.3673 | 2.1916 | ±4.3833 | -0.168 | 0.8669 |  |
| High cholesterol | +1.4479 | 1.9599 | ±3.9198 | +0.739 | 0.4601 |  |
| Kidney disease | -1.5407 | 4.0034 | ±8.0068 | -0.385 | 0.7004 |  |
| Circulatory disease | -1.5156 | 3.4668 | ±6.9337 | -0.437 | 0.6620 |  |
| Mean glucose (mg/dL) | -0.0278 | 0.0399 | ±0.0797 | -0.698 | 0.4851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **241**, R² = **0.1417**, Adj R² = **0.0885**, F-statistic = **2.66** (p = **0.0013**), Residual SE = **14.391** on **226** df, AIC = **1983.7**, BIC = **2036.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.1573** | 14.2377 | ±28.4754 | **+9.633** | **5.78e-22** | *** |
| Education: graduate level (vs college) | -1.9117 | 1.9714 | ±3.9428 | -0.970 | 0.3322 |  |
| Education: high school or below (vs college) | +10.2716 | 5.4710 | ±10.9420 | +1.877 | 0.0605 | . |
| Site: UCSD (vs UAB) | +0.1940 | 2.9465 | ±5.8930 | +0.066 | 0.9475 |  |
| **Site: UW (vs UAB)** | **-6.1021** | 2.5847 | ±5.1693 | **-2.361** | **0.0182** | * |
| **Season: spring (vs autumn)** | **+5.2970** | 2.6994 | ±5.3987 | **+1.962** | **0.0497** | * |
| Season: summer (vs autumn) | -1.6739 | 3.2816 | ±6.5631 | -0.510 | 0.6100 |  |
| Season: winter (vs autumn) | -1.7808 | 2.6785 | ±5.3571 | -0.665 | 0.5061 |  |
| Age (years) | -0.1547 | 0.0907 | ±0.1814 | -1.705 | 0.0881 | . |
| BMI (kg/m2) | +0.2878 | 0.1816 | ±0.3632 | +1.585 | 0.1130 |  |
| Hypertension | -0.3673 | 2.1916 | ±4.3833 | -0.168 | 0.8669 |  |
| High cholesterol | +1.4479 | 1.9599 | ±3.9198 | +0.739 | 0.4601 |  |
| Kidney disease | -1.5407 | 4.0034 | ±8.0068 | -0.385 | 0.7004 |  |
| Circulatory disease | -1.5156 | 3.4668 | ±6.9337 | -0.437 | 0.6620 |  |
| GMI (%) | -1.1633 | 1.6662 | ±3.3324 | -0.698 | 0.4851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **241**, R² = **0.1418**, Adj R² = **0.0886**, F-statistic = **2.67** (p = **0.0013**), Residual SE = **14.390** on **226** df, AIC = **1983.7**, BIC = **2036.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.9076** | 10.1938 | ±20.3876 | **+13.038** | **7.43e-39** | *** |
| Education: graduate level (vs college) | -1.9737 | 1.9726 | ±3.9451 | -1.001 | 0.3170 |  |
| Education: high school or below (vs college) | +10.2186 | 5.4664 | ±10.9329 | +1.869 | 0.0616 | . |
| Site: UCSD (vs UAB) | +0.2760 | 2.9472 | ±5.8944 | +0.094 | 0.9254 |  |
| **Site: UW (vs UAB)** | **-6.1206** | 2.5857 | ±5.1715 | **-2.367** | **0.0179** | * |
| **Season: spring (vs autumn)** | **+5.3667** | 2.7052 | ±5.4105 | **+1.984** | **0.0473** | * |
| Season: summer (vs autumn) | -1.7037 | 3.2764 | ±6.5528 | -0.520 | 0.6031 |  |
| Season: winter (vs autumn) | -1.7164 | 2.6698 | ±5.3395 | -0.643 | 0.5203 |  |
| Age (years) | -0.1571 | 0.0914 | ±0.1827 | -1.720 | 0.0855 | . |
| BMI (kg/m2) | +0.2926 | 0.1816 | ±0.3632 | +1.611 | 0.1071 |  |
| Hypertension | -0.3770 | 2.1895 | ±4.3789 | -0.172 | 0.8633 |  |
| High cholesterol | +1.4546 | 1.9562 | ±3.9123 | +0.744 | 0.4571 |  |
| Kidney disease | -1.7565 | 4.0114 | ±8.0228 | -0.438 | 0.6615 |  |
| Circulatory disease | -1.5699 | 3.4396 | ±6.8793 | -0.456 | 0.6481 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0257 | 0.0368 | ±0.0736 | -0.698 | 0.4851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **241**, R² = **0.1451**, Adj R² = **0.0922**, F-statistic = **2.74** (p = **9.21e-04**), Residual SE = **14.362** on **226** df, AIC = **1982.8**, BIC = **2035.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.0692** | 9.1791 | ±18.3583 | **+14.606** | **2.58e-48** | *** |
| Education: graduate level (vs college) | -2.0224 | 1.9729 | ±3.9457 | -1.025 | 0.3053 |  |
| Education: high school or below (vs college) | +9.7947 | 5.4060 | ±10.8121 | +1.812 | 0.0700 | . |
| Site: UCSD (vs UAB) | -0.0145 | 2.9442 | ±5.8883 | -0.005 | 0.9961 |  |
| **Site: UW (vs UAB)** | **-6.2909** | 2.5792 | ±5.1584 | **-2.439** | **0.0147** | * |
| **Season: spring (vs autumn)** | **+5.2863** | 2.6866 | ±5.3733 | **+1.968** | **0.0491** | * |
| Season: summer (vs autumn) | -1.5836 | 3.2856 | ±6.5711 | -0.482 | 0.6298 |  |
| Season: winter (vs autumn) | -1.7584 | 2.6591 | ±5.3181 | -0.661 | 0.5084 |  |
| Age (years) | -0.1494 | 0.0910 | ±0.1820 | -1.642 | 0.1006 |  |
| BMI (kg/m2) | +0.2989 | 0.1787 | ±0.3574 | +1.673 | 0.0943 | . |
| Hypertension | -0.2662 | 2.1596 | ±4.3191 | -0.123 | 0.9019 |  |
| High cholesterol | +1.0719 | 1.9921 | ±3.9842 | +0.538 | 0.5905 |  |
| Kidney disease | -0.8588 | 4.0536 | ±8.1072 | -0.212 | 0.8322 |  |
| Circulatory disease | -1.3442 | 3.4348 | ±6.8696 | -0.391 | 0.6955 |  |
| Glucose SD, pooled (mg/dL) | -0.1639 | 0.1352 | ±0.2704 | -1.212 | 0.2254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **241**, R² = **0.1421**, Adj R² = **0.0890**, F-statistic = **2.67** (p = **0.0012**), Residual SE = **14.387** on **226** df, AIC = **1983.6**, BIC = **2035.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6735** | 9.0084 | ±18.0168 | **+14.728** | **4.28e-49** | *** |
| Education: graduate level (vs college) | -1.9818 | 1.9777 | ±3.9555 | -1.002 | 0.3163 |  |
| Education: high school or below (vs college) | +9.6848 | 5.4367 | ±10.8734 | +1.781 | 0.0749 | . |
| Site: UCSD (vs UAB) | +0.0854 | 2.9391 | ±5.8782 | +0.029 | 0.9768 |  |
| **Site: UW (vs UAB)** | **-6.2244** | 2.5848 | ±5.1695 | **-2.408** | **0.0160** | * |
| Season: spring (vs autumn) | +5.2011 | 2.7045 | ±5.4090 | +1.923 | 0.0545 | . |
| Season: summer (vs autumn) | -1.5171 | 3.2867 | ±6.5733 | -0.462 | 0.6444 |  |
| Season: winter (vs autumn) | -1.7360 | 2.6817 | ±5.3634 | -0.647 | 0.5174 |  |
| Age (years) | -0.1511 | 0.0912 | ±0.1824 | -1.656 | 0.0977 | . |
| BMI (kg/m2) | +0.2933 | 0.1812 | ±0.3625 | +1.618 | 0.1056 |  |
| Hypertension | -0.2769 | 2.1795 | ±4.3589 | -0.127 | 0.8989 |  |
| High cholesterol | +1.1678 | 1.9924 | ±3.9847 | +0.586 | 0.5578 |  |
| Kidney disease | -1.0827 | 4.0417 | ±8.0834 | -0.268 | 0.7888 |  |
| Circulatory disease | -1.4884 | 3.4447 | ±6.8894 | -0.432 | 0.6657 |  |
| Avg. daily SD (mg/dL) | -0.1236 | 0.1506 | ±0.3012 | -0.821 | 0.4119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **241**, R² = **0.1425**, Adj R² = **0.0894**, F-statistic = **2.68** (p = **0.0012**), Residual SE = **14.384** on **226** df, AIC = **1983.5**, BIC = **2035.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.9564** | 9.1044 | ±18.2088 | **+14.713** | **5.29e-49** | *** |
| Education: graduate level (vs college) | -2.2108 | 1.9819 | ±3.9638 | -1.116 | 0.2646 |  |
| Education: high school or below (vs college) | +9.2229 | 5.5135 | ±11.0271 | +1.673 | 0.0944 | . |
| Site: UCSD (vs UAB) | +0.1207 | 2.9395 | ±5.8791 | +0.041 | 0.9672 |  |
| **Site: UW (vs UAB)** | **-6.3619** | 2.5821 | ±5.1642 | **-2.464** | **0.0137** | * |
| Season: spring (vs autumn) | +5.2687 | 2.6888 | ±5.3776 | +1.959 | 0.0501 | . |
| Season: summer (vs autumn) | -1.2887 | 3.2671 | ±6.5343 | -0.394 | 0.6932 |  |
| Season: winter (vs autumn) | -1.5466 | 2.6378 | ±5.2756 | -0.586 | 0.5576 |  |
| Age (years) | -0.1480 | 0.0920 | ±0.1840 | -1.609 | 0.1077 |  |
| BMI (kg/m2) | +0.2752 | 0.1799 | ±0.3597 | +1.530 | 0.1259 |  |
| Hypertension | -0.3853 | 2.1653 | ±4.3307 | -0.178 | 0.8588 |  |
| High cholesterol | +0.9880 | 1.9850 | ±3.9700 | +0.498 | 0.6187 |  |
| Kidney disease | -1.0675 | 4.0290 | ±8.0579 | -0.265 | 0.7910 |  |
| Circulatory disease | -1.8002 | 3.3477 | ±6.6953 | -0.538 | 0.5908 |  |
| CV (%) | -0.1885 | 0.2044 | ±0.4088 | -0.922 | 0.3563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **241**, R² = **0.1407**, Adj R² = **0.0874**, F-statistic = **2.64** (p = **0.0014**), Residual SE = **14.399** on **226** df, AIC = **1984.0**, BIC = **2036.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.7473** | 11.1183 | ±22.2367 | **+11.400** | **4.19e-30** | *** |
| Education: graduate level (vs college) | -2.0987 | 1.9779 | ±3.9557 | -1.061 | 0.2886 |  |
| Education: high school or below (vs college) | +9.4238 | 5.4964 | ±10.9928 | +1.715 | 0.0864 | . |
| Site: UCSD (vs UAB) | +0.2185 | 2.9439 | ±5.8877 | +0.074 | 0.9408 |  |
| **Site: UW (vs UAB)** | **-6.2776** | 2.5855 | ±5.1710 | **-2.428** | **0.0152** | * |
| **Season: spring (vs autumn)** | **+5.2786** | 2.6890 | ±5.3780 | **+1.963** | **0.0496** | * |
| Season: summer (vs autumn) | -1.2797 | 3.2649 | ±6.5299 | -0.392 | 0.6951 |  |
| Season: winter (vs autumn) | -1.5034 | 2.6340 | ±5.2681 | -0.571 | 0.5682 |  |
| Age (years) | -0.1508 | 0.0916 | ±0.1832 | -1.646 | 0.0997 | . |
| BMI (kg/m2) | +0.2707 | 0.1802 | ±0.3603 | +1.503 | 0.1329 |  |
| Hypertension | -0.3484 | 2.1609 | ±4.3219 | -0.161 | 0.8719 |  |
| High cholesterol | +1.1515 | 1.9694 | ±3.9387 | +0.585 | 0.5588 |  |
| Kidney disease | -1.2746 | 4.0399 | ±8.0797 | -0.315 | 0.7524 |  |
| Circulatory disease | -1.8304 | 3.3447 | ±6.6894 | -0.547 | 0.5842 |  |
| Mean / SD ratio | +0.6601 | 1.1248 | ±2.2496 | +0.587 | 0.5573 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **241**, R² = **0.1391**, Adj R² = **0.0858**, F-statistic = **2.61** (p = **0.0016**), Residual SE = **14.412** on **226** df, AIC = **1984.5**, BIC = **2036.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.5094** | 11.1337 | ±22.2673 | **+11.632** | **2.83e-31** | *** |
| Education: graduate level (vs college) | -2.0515 | 1.9826 | ±3.9652 | -1.035 | 0.3008 |  |
| Education: high school or below (vs college) | +9.6301 | 5.5012 | ±11.0024 | +1.751 | 0.0800 | . |
| Site: UCSD (vs UAB) | +0.3128 | 2.9394 | ±5.8787 | +0.106 | 0.9152 |  |
| **Site: UW (vs UAB)** | **-6.1525** | 2.5852 | ±5.1705 | **-2.380** | **0.0173** | * |
| Season: spring (vs autumn) | +5.2552 | 2.7138 | ±5.4276 | +1.936 | 0.0528 | . |
| Season: summer (vs autumn) | -1.3725 | 3.2673 | ±6.5346 | -0.420 | 0.6744 |  |
| Season: winter (vs autumn) | -1.5919 | 2.6483 | ±5.2966 | -0.601 | 0.5478 |  |
| Age (years) | -0.1529 | 0.0926 | ±0.1851 | -1.652 | 0.0985 | . |
| BMI (kg/m2) | +0.2696 | 0.1816 | ±0.3632 | +1.484 | 0.1377 |  |
| Hypertension | -0.4050 | 2.1671 | ±4.3343 | -0.187 | 0.8517 |  |
| High cholesterol | +1.3385 | 1.9813 | ±3.9625 | +0.676 | 0.4993 |  |
| Kidney disease | -1.5268 | 4.0417 | ±8.0833 | -0.378 | 0.7056 |  |
| Circulatory disease | -1.8740 | 3.3527 | ±6.7054 | -0.559 | 0.5762 |  |
| Avg. daily mean/SD | +0.0747 | 0.8871 | ±1.7742 | +0.084 | 0.9329 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **241**, R² = **0.1418**, Adj R² = **0.0886**, F-statistic = **2.67** (p = **0.0013**), Residual SE = **14.390** on **226** df, AIC = **1983.7**, BIC = **2036.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.1346** | 9.6019 | ±19.2038 | **+13.970** | **2.39e-44** | *** |
| Education: graduate level (vs college) | -2.2350 | 1.9734 | ±3.9467 | -1.133 | 0.2574 |  |
| Education: high school or below (vs college) | +9.5805 | 5.4104 | ±10.8209 | +1.771 | 0.0766 | . |
| Site: UCSD (vs UAB) | -0.0211 | 3.0112 | ±6.0225 | -0.007 | 0.9944 |  |
| **Site: UW (vs UAB)** | **-6.5960** | 2.6195 | ±5.2389 | **-2.518** | **0.0118** | * |
| **Season: spring (vs autumn)** | **+5.3448** | 2.7033 | ±5.4066 | **+1.977** | **0.0480** | * |
| Season: summer (vs autumn) | -1.5888 | 3.2197 | ±6.4394 | -0.493 | 0.6217 |  |
| Season: winter (vs autumn) | -1.7075 | 2.6629 | ±5.3258 | -0.641 | 0.5214 |  |
| Age (years) | -0.1540 | 0.0899 | ±0.1799 | -1.712 | 0.0869 | . |
| BMI (kg/m2) | +0.2944 | 0.1844 | ±0.3687 | +1.597 | 0.1103 |  |
| Hypertension | -0.6696 | 2.2232 | ±4.4463 | -0.301 | 0.7633 |  |
| High cholesterol | +1.0233 | 2.0736 | ±4.1472 | +0.493 | 0.6217 |  |
| Kidney disease | -1.6002 | 3.9183 | ±7.8366 | -0.408 | 0.6830 |  |
| Circulatory disease | -1.6963 | 3.3813 | ±6.7626 | -0.502 | 0.6159 |  |
| MAG (mg/dL/h) | -0.0941 | 0.1264 | ±0.2529 | -0.744 | 0.4567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **241**, R² = **0.1416**, Adj R² = **0.0884**, F-statistic = **2.66** (p = **0.0013**), Residual SE = **14.392** on **226** df, AIC = **1983.8**, BIC = **2036.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.6091** | 9.2815 | ±18.5630 | **+14.395** | **5.54e-47** | *** |
| Education: graduate level (vs college) | -2.0265 | 1.9775 | ±3.9550 | -1.025 | 0.3055 |  |
| Education: high school or below (vs college) | +9.7171 | 5.4573 | ±10.9145 | +1.781 | 0.0750 | . |
| Site: UCSD (vs UAB) | +0.0326 | 2.9261 | ±5.8522 | +0.011 | 0.9911 |  |
| **Site: UW (vs UAB)** | **-6.3429** | 2.5773 | ±5.1546 | **-2.461** | **0.0139** | * |
| **Season: spring (vs autumn)** | **+5.3078** | 2.6872 | ±5.3743 | **+1.975** | **0.0482** | * |
| Season: summer (vs autumn) | -1.4777 | 3.2720 | ±6.5440 | -0.452 | 0.6516 |  |
| Season: winter (vs autumn) | -1.6808 | 2.6880 | ±5.3760 | -0.625 | 0.5318 |  |
| Age (years) | -0.1534 | 0.0909 | ±0.1817 | -1.688 | 0.0914 | . |
| BMI (kg/m2) | +0.2862 | 0.1831 | ±0.3662 | +1.563 | 0.1181 |  |
| Hypertension | -0.3905 | 2.1754 | ±4.3508 | -0.179 | 0.8576 |  |
| High cholesterol | +1.0700 | 2.0218 | ±4.0437 | +0.529 | 0.5967 |  |
| Kidney disease | -1.2863 | 3.9894 | ±7.9788 | -0.322 | 0.7471 |  |
| Circulatory disease | -1.5960 | 3.4382 | ±6.8764 | -0.464 | 0.6425 |  |
| Avg. daily range (mg/dL) | -0.0289 | 0.0420 | ±0.0841 | -0.688 | 0.4916 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **241**, R² = **0.1490**, Adj R² = **0.0963**, F-statistic = **2.83** (p = **6.39e-04**), Residual SE = **14.329** on **226** df, AIC = **1981.7**, BIC = **2033.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.5066** | 8.8312 | ±17.6623 | **+14.891** | **3.76e-50** | *** |
| Education: graduate level (vs college) | -2.2830 | 1.9937 | ±3.9874 | -1.145 | 0.2522 |  |
| Education: high school or below (vs college) | +10.0739 | 5.4267 | ±10.8534 | +1.856 | 0.0634 | . |
| Site: UCSD (vs UAB) | +0.1985 | 2.9550 | ±5.9099 | +0.067 | 0.9464 |  |
| **Site: UW (vs UAB)** | **-6.1602** | 2.5625 | ±5.1249 | **-2.404** | **0.0162** | * |
| **Season: spring (vs autumn)** | **+5.8820** | 2.7268 | ±5.4537 | **+2.157** | **0.0310** | * |
| Season: summer (vs autumn) | -1.4217 | 3.2580 | ±6.5159 | -0.436 | 0.6626 |  |
| Season: winter (vs autumn) | -1.3714 | 2.6069 | ±5.2138 | -0.526 | 0.5988 |  |
| Age (years) | -0.1439 | 0.0896 | ±0.1791 | -1.607 | 0.1081 |  |
| BMI (kg/m2) | +0.2946 | 0.1770 | ±0.3539 | +1.665 | 0.0959 | . |
| Hypertension | -0.5102 | 2.1321 | ±4.2642 | -0.239 | 0.8109 |  |
| High cholesterol | +1.2252 | 1.9894 | ±3.9788 | +0.616 | 0.5380 |  |
| Kidney disease | -1.3477 | 4.0340 | ±8.0681 | -0.334 | 0.7383 |  |
| Circulatory disease | -1.6921 | 3.3469 | ±6.6939 | -0.506 | 0.6132 |  |
| SD of daily means (mg/dL) | -0.3278 | 0.2111 | ±0.4221 | -1.553 | 0.1205 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **241**, R² = **0.1422**, Adj R² = **0.0890**, F-statistic = **2.68** (p = **0.0012**), Residual SE = **14.386** on **226** df, AIC = **1983.6**, BIC = **2035.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6184** | 10.5446 | ±21.0891 | **+11.818** | **3.14e-32** | *** |
| Education: graduate level (vs college) | -1.9491 | 1.9662 | ±3.9324 | -0.991 | 0.3215 |  |
| Education: high school or below (vs college) | +10.1239 | 5.4202 | ±10.8404 | +1.868 | 0.0618 | . |
| Site: UCSD (vs UAB) | +0.1612 | 2.9314 | ±5.8627 | +0.055 | 0.9561 |  |
| **Site: UW (vs UAB)** | **-6.1704** | 2.5850 | ±5.1701 | **-2.387** | **0.0170** | * |
| Season: spring (vs autumn) | +5.2547 | 2.7089 | ±5.4177 | +1.940 | 0.0524 | . |
| Season: summer (vs autumn) | -1.7339 | 3.2895 | ±6.5790 | -0.527 | 0.5981 |  |
| Season: winter (vs autumn) | -1.7018 | 2.6523 | ±5.3046 | -0.642 | 0.5211 |  |
| Age (years) | -0.1546 | 0.0911 | ±0.1822 | -1.698 | 0.0896 | . |
| BMI (kg/m2) | +0.2954 | 0.1813 | ±0.3626 | +1.629 | 0.1032 |  |
| Hypertension | -0.3849 | 2.1822 | ±4.3644 | -0.176 | 0.8600 |  |
| High cholesterol | +1.3892 | 1.9730 | ±3.9460 | +0.704 | 0.4814 |  |
| Kidney disease | -1.3615 | 3.9861 | ±7.9722 | -0.342 | 0.7327 |  |
| Circulatory disease | -1.5855 | 3.4281 | ±6.8562 | -0.462 | 0.6437 |  |
| Time in range 70-180, pooled (%) | +0.0541 | 0.0751 | ±0.1502 | +0.720 | 0.4715 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **241**, R² = **0.1417**, Adj R² = **0.0885**, F-statistic = **2.66** (p = **0.0013**), Residual SE = **14.391** on **226** df, AIC = **1983.7**, BIC = **2036.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0947** | 10.6235 | ±21.2470 | **+11.775** | **5.23e-32** | *** |
| Education: graduate level (vs college) | -1.9524 | 1.9669 | ±3.9338 | -0.993 | 0.3209 |  |
| Education: high school or below (vs college) | +10.0665 | 5.4161 | ±10.8322 | +1.859 | 0.0631 | . |
| Site: UCSD (vs UAB) | +0.1619 | 2.9302 | ±5.8605 | +0.055 | 0.9560 |  |
| **Site: UW (vs UAB)** | **-6.1763** | 2.5880 | ±5.1761 | **-2.387** | **0.0170** | * |
| Season: spring (vs autumn) | +5.2664 | 2.7070 | ±5.4139 | +1.945 | 0.0517 | . |
| Season: summer (vs autumn) | -1.7017 | 3.2896 | ±6.5791 | -0.517 | 0.6049 |  |
| Season: winter (vs autumn) | -1.6913 | 2.6539 | ±5.3078 | -0.637 | 0.5239 |  |
| Age (years) | -0.1543 | 0.0910 | ±0.1820 | -1.696 | 0.0899 | . |
| BMI (kg/m2) | +0.2933 | 0.1823 | ±0.3646 | +1.609 | 0.1077 |  |
| Hypertension | -0.3856 | 2.1859 | ±4.3717 | -0.176 | 0.8600 |  |
| High cholesterol | +1.3880 | 1.9741 | ±3.9483 | +0.703 | 0.4820 |  |
| Kidney disease | -1.3718 | 3.9898 | ±7.9797 | -0.344 | 0.7310 |  |
| Circulatory disease | -1.6208 | 3.4280 | ±6.8560 | -0.473 | 0.6363 |  |
| Avg. daily time in range 70-180 (%) | +0.0489 | 0.0739 | ±0.1478 | +0.662 | 0.5080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.1391**, Adj R² = **0.0857**, F-statistic = **2.61** (p = **0.0016**), Residual SE = **14.413** on **226** df, AIC = **1984.5**, BIC = **2036.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.9746** | 8.6574 | ±17.3149 | **+15.013** | **6.03e-51** | *** |
| Education: graduate level (vs college) | -2.0590 | 1.9887 | ±3.9774 | -1.035 | 0.3005 |  |
| Education: high school or below (vs college) | +9.6516 | 5.5588 | ±11.1176 | +1.736 | 0.0825 | . |
| Site: UCSD (vs UAB) | +0.3261 | 2.9491 | ±5.8982 | +0.111 | 0.9119 |  |
| **Site: UW (vs UAB)** | **-6.1353** | 2.5706 | ±5.1412 | **-2.387** | **0.0170** | * |
| Season: spring (vs autumn) | +5.2607 | 2.7202 | ±5.4404 | +1.934 | 0.0531 | . |
| Season: summer (vs autumn) | -1.3929 | 3.2737 | ±6.5474 | -0.425 | 0.6705 |  |
| Season: winter (vs autumn) | -1.6072 | 2.6800 | ±5.3600 | -0.600 | 0.5487 |  |
| Age (years) | -0.1533 | 0.0915 | ±0.1830 | -1.676 | 0.0938 | . |
| BMI (kg/m2) | +0.2692 | 0.1841 | ±0.3681 | +1.462 | 0.1436 |  |
| Hypertension | -0.4210 | 2.1833 | ±4.3667 | -0.193 | 0.8471 |  |
| High cholesterol | +1.3603 | 1.9770 | ±3.9541 | +0.688 | 0.4914 |  |
| Kidney disease | -1.5620 | 3.9921 | ±7.9841 | -0.391 | 0.6956 |  |
| Circulatory disease | -1.8778 | 3.3571 | ±6.7142 | -0.559 | 0.5759 |  |
| Any reading < 54 during wear (0/1) | -0.0897 | 2.3593 | ±4.7186 | -0.038 | 0.9697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.1428**, Adj R² = **0.0897**, F-statistic = **2.69** (p = **0.0011**), Residual SE = **14.381** on **226** df, AIC = **1983.4**, BIC = **2035.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4769** | 8.7666 | ±17.5332 | **+14.883** | **4.23e-50** | *** |
| Education: graduate level (vs college) | -2.2398 | 1.9879 | ±3.9759 | -1.127 | 0.2599 |  |
| Education: high school or below (vs college) | +9.3741 | 5.4248 | ±10.8497 | +1.728 | 0.0840 | . |
| Site: UCSD (vs UAB) | +0.1297 | 2.9551 | ±5.9102 | +0.044 | 0.9650 |  |
| **Site: UW (vs UAB)** | **-6.4344** | 2.6119 | ±5.2237 | **-2.464** | **0.0138** | * |
| Season: spring (vs autumn) | +5.2670 | 2.7037 | ±5.4075 | +1.948 | 0.0514 | . |
| Season: summer (vs autumn) | -1.4254 | 3.2590 | ±6.5180 | -0.437 | 0.6618 |  |
| Season: winter (vs autumn) | -1.3870 | 2.6589 | ±5.3178 | -0.522 | 0.6019 |  |
| Age (years) | -0.1469 | 0.0905 | ±0.1809 | -1.623 | 0.1045 |  |
| BMI (kg/m2) | +0.2554 | 0.1835 | ±0.3669 | +1.392 | 0.1640 |  |
| Hypertension | -0.5297 | 2.1771 | ±4.3542 | -0.243 | 0.8078 |  |
| High cholesterol | +1.1797 | 1.9846 | ±3.9693 | +0.594 | 0.5522 |  |
| Kidney disease | -1.6174 | 3.9830 | ±7.9661 | -0.406 | 0.6847 |  |
| Circulatory disease | -1.9150 | 3.3604 | ±6.7207 | -0.570 | 0.5688 |  |
| Time < 54 (%) | -0.9952 | 4.1449 | ±8.2898 | -0.240 | 0.8102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **241**, R² = **0.1435**, Adj R² = **0.0905**, F-statistic = **2.71** (p = **0.0011**), Residual SE = **14.375** on **226** df, AIC = **1983.2**, BIC = **2035.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4570** | 8.7552 | ±17.5103 | **+14.901** | **3.27e-50** | *** |
| Education: graduate level (vs college) | -2.2471 | 1.9824 | ±3.9647 | -1.134 | 0.2570 |  |
| Education: high school or below (vs college) | +9.3334 | 5.4023 | ±10.8046 | +1.728 | 0.0840 | . |
| Site: UCSD (vs UAB) | +0.1149 | 2.9488 | ±5.8976 | +0.039 | 0.9689 |  |
| **Site: UW (vs UAB)** | **-6.5120** | 2.6127 | ±5.2254 | **-2.492** | **0.0127** | * |
| **Season: spring (vs autumn)** | **+5.2904** | 2.6918 | ±5.3836 | **+1.965** | **0.0494** | * |
| Season: summer (vs autumn) | -1.4661 | 3.2566 | ±6.5132 | -0.450 | 0.6526 |  |
| Season: winter (vs autumn) | -1.3170 | 2.6673 | ±5.3345 | -0.494 | 0.6215 |  |
| Age (years) | -0.1461 | 0.0901 | ±0.1802 | -1.622 | 0.1049 |  |
| BMI (kg/m2) | +0.2571 | 0.1822 | ±0.3645 | +1.411 | 0.1583 |  |
| Hypertension | -0.5543 | 2.1793 | ±4.3586 | -0.254 | 0.7992 |  |
| High cholesterol | +1.1127 | 1.9863 | ±3.9725 | +0.560 | 0.5753 |  |
| Kidney disease | -1.6162 | 3.9812 | ±7.9624 | -0.406 | 0.6848 |  |
| Circulatory disease | -1.8960 | 3.3685 | ±6.7371 | -0.563 | 0.5735 |  |
| Avg. daily time < 54 (%) | -1.4465 | 2.7961 | ±5.5922 | -0.517 | 0.6049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **241**, R² = **0.1521**, Adj R² = **0.0996**, F-statistic = **2.90** (p = **4.75e-04**), Residual SE = **14.303** on **226** df, AIC = **1980.8**, BIC = **2033.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.2632** | 8.8074 | ±17.6148 | **+14.790** | **1.69e-49** | *** |
| Education: graduate level (vs college) | -2.5171 | 1.9842 | ±3.9684 | -1.269 | 0.2046 |  |
| Education: high school or below (vs college) | +8.9145 | 5.4583 | ±10.9166 | +1.633 | 0.1024 |  |
| Site: UCSD (vs UAB) | +0.1037 | 2.9195 | ±5.8390 | +0.036 | 0.9717 |  |
| **Site: UW (vs UAB)** | **-6.6521** | 2.5783 | ±5.1566 | **-2.580** | **0.0099** | ** |
| Season: spring (vs autumn) | +5.2470 | 2.6817 | ±5.3634 | +1.957 | 0.0504 | . |
| Season: summer (vs autumn) | -1.7222 | 3.2427 | ±6.4854 | -0.531 | 0.5954 |  |
| Season: winter (vs autumn) | -1.3383 | 2.6302 | ±5.2603 | -0.509 | 0.6109 |  |
| Age (years) | -0.1467 | 0.0898 | ±0.1796 | -1.634 | 0.1023 |  |
| BMI (kg/m2) | +0.2961 | 0.1859 | ±0.3718 | +1.593 | 0.1112 |  |
| Hypertension | -0.6158 | 2.1742 | ±4.3484 | -0.283 | 0.7770 |  |
| High cholesterol | +0.8184 | 1.9664 | ±3.9327 | +0.416 | 0.6773 |  |
| Kidney disease | -1.4715 | 3.9164 | ±7.8327 | -0.376 | 0.7071 |  |
| Circulatory disease | -2.0244 | 3.3552 | ±6.7104 | -0.603 | 0.5463 |  |
| **Time 54-69, pooled (%)** | **-1.3894** | 0.4467 | ±0.8934 | **-3.110** | **0.0019** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **241**, R² = **0.1526**, Adj R² = **0.1001**, F-statistic = **2.91** (p = **4.51e-04**), Residual SE = **14.299** on **226** df, AIC = **1980.6**, BIC = **2032.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.2088** | 8.7976 | ±17.5952 | **+14.800** | **1.45e-49** | *** |
| Education: graduate level (vs college) | -2.5319 | 1.9851 | ±3.9701 | -1.275 | 0.2021 |  |
| Education: high school or below (vs college) | +8.8883 | 5.4598 | ±10.9196 | +1.628 | 0.1035 |  |
| Site: UCSD (vs UAB) | +0.0874 | 2.9159 | ±5.8318 | +0.030 | 0.9761 |  |
| **Site: UW (vs UAB)** | **-6.7257** | 2.5780 | ±5.1560 | **-2.609** | **0.0091** | ** |
| **Season: spring (vs autumn)** | **+5.2930** | 2.6805 | ±5.3609 | **+1.975** | **0.0483** | * |
| Season: summer (vs autumn) | -1.7221 | 3.2477 | ±6.4954 | -0.530 | 0.5959 |  |
| Season: winter (vs autumn) | -1.2301 | 2.6324 | ±5.2647 | -0.467 | 0.6403 |  |
| Age (years) | -0.1452 | 0.0898 | ±0.1796 | -1.616 | 0.1060 |  |
| BMI (kg/m2) | +0.2935 | 0.1849 | ±0.3698 | +1.587 | 0.1124 |  |
| Hypertension | -0.6383 | 2.1739 | ±4.3478 | -0.294 | 0.7690 |  |
| High cholesterol | +0.7741 | 1.9720 | ±3.9439 | +0.393 | 0.6947 |  |
| Kidney disease | -1.4934 | 3.9169 | ±7.8339 | -0.381 | 0.7030 |  |
| Circulatory disease | -2.0301 | 3.3585 | ±6.7170 | -0.604 | 0.5455 |  |
| **Avg. daily time 54-69 (%)** | **-1.3544** | 0.4160 | ±0.8320 | **-3.256** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **241**, R² = **0.1506**, Adj R² = **0.0980**, F-statistic = **2.86** (p = **5.48e-04**), Residual SE = **14.316** on **226** df, AIC = **1981.2**, BIC = **2033.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.6103** | 8.7608 | ±17.5216 | **+14.908** | **2.90e-50** | *** |
| Education: graduate level (vs college) | -2.5126 | 1.9901 | ±3.9803 | -1.263 | 0.2068 |  |
| Education: high school or below (vs college) | +8.9319 | 5.4339 | ±10.8679 | +1.644 | 0.1002 |  |
| Site: UCSD (vs UAB) | +0.0120 | 2.9322 | ±5.8644 | +0.004 | 0.9967 |  |
| **Site: UW (vs UAB)** | **-6.7288** | 2.5970 | ±5.1941 | **-2.591** | **0.0096** | ** |
| Season: spring (vs autumn) | +5.2553 | 2.6828 | ±5.3656 | +1.959 | 0.0501 | . |
| Season: summer (vs autumn) | -1.6332 | 3.2422 | ±6.4844 | -0.504 | 0.6145 |  |
| Season: winter (vs autumn) | -1.2448 | 2.6425 | ±5.2851 | -0.471 | 0.6376 |  |
| Age (years) | -0.1434 | 0.0901 | ±0.1802 | -1.591 | 0.1116 |  |
| BMI (kg/m2) | +0.2742 | 0.1824 | ±0.3648 | +1.503 | 0.1328 |  |
| Hypertension | -0.6414 | 2.1749 | ±4.3498 | -0.295 | 0.7681 |  |
| High cholesterol | +0.8539 | 1.9734 | ±3.9468 | +0.433 | 0.6652 |  |
| Kidney disease | -1.5486 | 3.9477 | ±7.8954 | -0.392 | 0.6948 |  |
| Circulatory disease | -2.0033 | 3.3668 | ±6.7336 | -0.595 | 0.5518 |  |
| **Time < 70 (%)** | **-0.8793** | 0.4212 | ±0.8423 | **-2.088** | **0.0368** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **241**, R² = **0.1513**, Adj R² = **0.0987**, F-statistic = **2.88** (p = **5.14e-04**), Residual SE = **14.310** on **226** df, AIC = **1981.0**, BIC = **2033.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4520** | 8.7607 | ±17.5213 | **+14.891** | **3.79e-50** | *** |
| Education: graduate level (vs college) | -2.5077 | 1.9881 | ±3.9762 | -1.261 | 0.2072 |  |
| Education: high school or below (vs college) | +8.9168 | 5.4383 | ±10.8766 | +1.640 | 0.1011 |  |
| Site: UCSD (vs UAB) | +0.0261 | 2.9261 | ±5.8523 | +0.009 | 0.9929 |  |
| **Site: UW (vs UAB)** | **-6.7852** | 2.5942 | ±5.1884 | **-2.616** | **0.0089** | ** |
| **Season: spring (vs autumn)** | **+5.3005** | 2.6833 | ±5.3666 | **+1.975** | **0.0482** | * |
| Season: summer (vs autumn) | -1.6684 | 3.2478 | ±6.4956 | -0.514 | 0.6075 |  |
| Season: winter (vs autumn) | -1.1626 | 2.6463 | ±5.2926 | -0.439 | 0.6604 |  |
| Age (years) | -0.1430 | 0.0900 | ±0.1800 | -1.589 | 0.1120 |  |
| BMI (kg/m2) | +0.2782 | 0.1822 | ±0.3644 | +1.527 | 0.1267 |  |
| Hypertension | -0.6569 | 2.1762 | ±4.3524 | -0.302 | 0.7628 |  |
| High cholesterol | +0.7954 | 1.9800 | ±3.9600 | +0.402 | 0.6879 |  |
| Kidney disease | -1.5466 | 3.9412 | ±7.8823 | -0.392 | 0.6948 |  |
| Circulatory disease | -1.9941 | 3.3707 | ±6.7414 | -0.592 | 0.5541 |  |
| **Avg. daily time < 70 (%)** | **-0.9312** | 0.3570 | ±0.7140 | **-2.608** | **0.0091** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.1542**, Adj R² = **0.1018**, F-statistic = **2.94** (p = **3.86e-04**), Residual SE = **14.285** on **226** df, AIC = **1980.2**, BIC = **2032.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+112.8224** | 11.2007 | ±22.4014 | **+10.073** | **7.29e-24** | *** |
| Education: graduate level (vs college) | -2.0792 | 1.9708 | ±3.9415 | -1.055 | 0.2914 |  |
| **Education: high school or below (vs college)** | **+11.0082** | 5.3919 | ±10.7837 | **+2.042** | **0.0412** | * |
| Site: UCSD (vs UAB) | +0.0607 | 2.9360 | ±5.8721 | +0.021 | 0.9835 |  |
| **Site: UW (vs UAB)** | **-6.3159** | 2.5683 | ±5.1366 | **-2.459** | **0.0139** | * |
| **Season: spring (vs autumn)** | **+5.3781** | 2.6927 | ±5.3853 | **+1.997** | **0.0458** | * |
| Season: summer (vs autumn) | -1.8126 | 3.2553 | ±6.5106 | -0.557 | 0.5776 |  |
| Season: winter (vs autumn) | -1.6668 | 2.6388 | ±5.2776 | -0.632 | 0.5276 |  |
| Age (years) | -0.1592 | 0.0902 | ±0.1803 | -1.766 | 0.0775 | . |
| BMI (kg/m2) | +0.2822 | 0.1772 | ±0.3545 | +1.592 | 0.1113 |  |
| Hypertension | -0.5613 | 2.1366 | ±4.2732 | -0.263 | 0.7928 |  |
| High cholesterol | +1.1734 | 1.9685 | ±3.9370 | +0.596 | 0.5511 |  |
| Kidney disease | -1.7477 | 4.0400 | ±8.0799 | -0.433 | 0.6653 |  |
| Circulatory disease | -0.9030 | 3.4809 | ±6.9618 | -0.259 | 0.7953 |  |
| **Time 54-250, pooled (%)** | **+0.1778** | 0.0850 | ±0.1699 | **+2.093** | **0.0364** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **241**, R² = **0.1541**, Adj R² = **0.1017**, F-statistic = **2.94** (p = **3.90e-04**), Residual SE = **14.286** on **226** df, AIC = **1980.2**, BIC = **2032.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+112.4157** | 11.4447 | ±22.8894 | **+9.822** | **9.01e-23** | *** |
| Education: graduate level (vs college) | -2.0668 | 1.9708 | ±3.9415 | -1.049 | 0.2943 |  |
| **Education: high school or below (vs college)** | **+11.0342** | 5.4021 | ±10.8042 | **+2.043** | **0.0411** | * |
| Site: UCSD (vs UAB) | +0.0583 | 2.9372 | ±5.8744 | +0.020 | 0.9842 |  |
| **Site: UW (vs UAB)** | **-6.2970** | 2.5671 | ±5.1341 | **-2.453** | **0.0142** | * |
| **Season: spring (vs autumn)** | **+5.3652** | 2.6927 | ±5.3855 | **+1.992** | **0.0463** | * |
| Season: summer (vs autumn) | -1.8272 | 3.2565 | ±6.5129 | -0.561 | 0.5747 |  |
| Season: winter (vs autumn) | -1.6965 | 2.6401 | ±5.2802 | -0.643 | 0.5205 |  |
| Age (years) | -0.1592 | 0.0902 | ±0.1803 | -1.765 | 0.0775 | . |
| BMI (kg/m2) | +0.2848 | 0.1770 | ±0.3539 | +1.610 | 0.1075 |  |
| Hypertension | -0.5506 | 2.1369 | ±4.2739 | -0.258 | 0.7967 |  |
| High cholesterol | +1.1677 | 1.9701 | ±3.9403 | +0.593 | 0.5534 |  |
| Kidney disease | -1.7655 | 4.0449 | ±8.0899 | -0.436 | 0.6625 |  |
| Circulatory disease | -0.8827 | 3.4885 | ±6.9770 | -0.253 | 0.8002 |  |
| **Avg. daily time 54-250 (%)** | **+0.1809** | 0.0877 | ±0.1754 | **+2.062** | **0.0392** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.1425**, Adj R² = **0.0894**, F-statistic = **2.68** (p = **0.0012**), Residual SE = **14.384** on **226** df, AIC = **1983.5**, BIC = **2035.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.1947** | 8.8445 | ±17.6889 | **+14.720** | **4.76e-49** | *** |
| Education: graduate level (vs college) | -2.2743 | 1.9684 | ±3.9368 | -1.155 | 0.2479 |  |
| Education: high school or below (vs college) | +9.5320 | 5.4090 | ±10.8181 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | +0.4562 | 2.9486 | ±5.8973 | +0.155 | 0.8771 |  |
| **Site: UW (vs UAB)** | **-6.1952** | 2.5992 | ±5.1984 | **-2.383** | **0.0171** | * |
| **Season: spring (vs autumn)** | **+5.3416** | 2.7024 | ±5.4048 | **+1.977** | **0.0481** | * |
| Season: summer (vs autumn) | -1.0324 | 3.2589 | ±6.5178 | -0.317 | 0.7514 |  |
| Season: winter (vs autumn) | -1.4469 | 2.6779 | ±5.3559 | -0.540 | 0.5890 |  |
| Age (years) | -0.1540 | 0.0902 | ±0.1804 | -1.707 | 0.0877 | . |
| BMI (kg/m2) | +0.2317 | 0.1905 | ±0.3809 | +1.216 | 0.2239 |  |
| Hypertension | -0.5662 | 2.2421 | ±4.4842 | -0.253 | 0.8006 |  |
| High cholesterol | +1.1912 | 1.9999 | ±3.9999 | +0.596 | 0.5514 |  |
| Kidney disease | -2.0217 | 3.9975 | ±7.9950 | -0.506 | 0.6130 |  |
| Circulatory disease | -1.8810 | 3.3583 | ±6.7166 | -0.560 | 0.5754 |  |
| Time 181-250, pooled (%) | +0.0937 | 0.1390 | ±0.2779 | +0.674 | 0.5001 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **241**, R² = **0.1429**, Adj R² = **0.0898**, F-statistic = **2.69** (p = **0.0011**), Residual SE = **14.381** on **226** df, AIC = **1983.4**, BIC = **2035.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.2062** | 8.8249 | ±17.6497 | **+14.754** | **2.88e-49** | *** |
| Education: graduate level (vs college) | -2.2868 | 1.9674 | ±3.9348 | -1.162 | 0.2451 |  |
| Education: high school or below (vs college) | +9.5542 | 5.4118 | ±10.8237 | +1.765 | 0.0775 | . |
| Site: UCSD (vs UAB) | +0.4882 | 2.9446 | ±5.8892 | +0.166 | 0.8683 |  |
| **Site: UW (vs UAB)** | **-6.1719** | 2.6004 | ±5.2008 | **-2.373** | **0.0176** | * |
| **Season: spring (vs autumn)** | **+5.3177** | 2.6989 | ±5.3978 | **+1.970** | **0.0488** | * |
| Season: summer (vs autumn) | -1.0271 | 3.2589 | ±6.5179 | -0.315 | 0.7526 |  |
| Season: winter (vs autumn) | -1.4525 | 2.6771 | ±5.3542 | -0.543 | 0.5874 |  |
| Age (years) | -0.1543 | 0.0901 | ±0.1803 | -1.712 | 0.0870 | . |
| BMI (kg/m2) | +0.2311 | 0.1907 | ±0.3814 | +1.212 | 0.2255 |  |
| Hypertension | -0.5692 | 2.2364 | ±4.4728 | -0.255 | 0.7991 |  |
| High cholesterol | +1.1805 | 1.9976 | ±3.9952 | +0.591 | 0.5545 |  |
| Kidney disease | -2.0597 | 3.9956 | ±7.9911 | -0.516 | 0.6062 |  |
| Circulatory disease | -1.8655 | 3.3536 | ±6.7072 | -0.556 | 0.5780 |  |
| Avg. daily time 181-250 (%) | +0.0958 | 0.1334 | ±0.2667 | +0.718 | 0.4728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **241**, R² = **0.1409**, Adj R² = **0.0877**, F-statistic = **2.65** (p = **0.0014**), Residual SE = **14.397** on **226** df, AIC = **1984.0**, BIC = **2036.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.9804** | 8.7458 | ±17.4915 | **+14.862** | **5.81e-50** | *** |
| Education: graduate level (vs college) | -1.9517 | 1.9675 | ±3.9350 | -0.992 | 0.3212 |  |
| Education: high school or below (vs college) | +10.0498 | 5.4343 | ±10.8686 | +1.849 | 0.0644 | . |
| Site: UCSD (vs UAB) | +0.2151 | 2.9345 | ±5.8691 | +0.073 | 0.9416 |  |
| **Site: UW (vs UAB)** | **-6.1329** | 2.5869 | ±5.1739 | **-2.371** | **0.0178** | * |
| Season: spring (vs autumn) | +5.2576 | 2.7072 | ±5.4144 | +1.942 | 0.0521 | . |
| Season: summer (vs autumn) | -1.6398 | 3.2883 | ±6.5766 | -0.499 | 0.6180 |  |
| Season: winter (vs autumn) | -1.6951 | 2.6616 | ±5.3233 | -0.637 | 0.5242 |  |
| Age (years) | -0.1548 | 0.0912 | ±0.1824 | -1.698 | 0.0896 | . |
| BMI (kg/m2) | +0.2888 | 0.1821 | ±0.3642 | +1.586 | 0.1127 |  |
| Hypertension | -0.3825 | 2.1943 | ±4.3886 | -0.174 | 0.8616 |  |
| High cholesterol | +1.4082 | 1.9709 | ±3.9418 | +0.715 | 0.4749 |  |
| Kidney disease | -1.4125 | 3.9819 | ±7.9637 | -0.355 | 0.7228 |  |
| Circulatory disease | -1.6492 | 3.4305 | ±6.8610 | -0.481 | 0.6307 |  |
| Time > 180 (%) | -0.0412 | 0.0755 | ±0.1509 | -0.546 | 0.5848 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **241**, R² = **0.1405**, Adj R² = **0.0873**, F-statistic = **2.64** (p = **0.0014**), Residual SE = **14.400** on **226** df, AIC = **1984.1**, BIC = **2036.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.9597** | 8.7495 | ±17.4990 | **+14.853** | **6.62e-50** | *** |
| Education: graduate level (vs college) | -1.9597 | 1.9679 | ±3.9359 | -0.996 | 0.3193 |  |
| Education: high school or below (vs college) | +9.9940 | 5.4295 | ±10.8589 | +1.841 | 0.0657 | . |
| Site: UCSD (vs UAB) | +0.2154 | 2.9339 | ±5.8678 | +0.073 | 0.9415 |  |
| **Site: UW (vs UAB)** | **-6.1391** | 2.5899 | ±5.1798 | **-2.370** | **0.0178** | * |
| Season: spring (vs autumn) | +5.2647 | 2.7056 | ±5.4112 | +1.946 | 0.0517 | . |
| Season: summer (vs autumn) | -1.6103 | 3.2878 | ±6.5755 | -0.490 | 0.6243 |  |
| Season: winter (vs autumn) | -1.6859 | 2.6635 | ±5.3270 | -0.633 | 0.5268 |  |
| Age (years) | -0.1545 | 0.0911 | ±0.1822 | -1.696 | 0.0899 | . |
| BMI (kg/m2) | +0.2867 | 0.1829 | ±0.3659 | +1.567 | 0.1171 |  |
| Hypertension | -0.3848 | 2.1974 | ±4.3948 | -0.175 | 0.8610 |  |
| High cholesterol | +1.4052 | 1.9715 | ±3.9429 | +0.713 | 0.4760 |  |
| Kidney disease | -1.4238 | 3.9847 | ±7.9694 | -0.357 | 0.7209 |  |
| Circulatory disease | -1.6819 | 3.4298 | ±6.8596 | -0.490 | 0.6239 |  |
| Avg. daily time > 180 (%) | -0.0364 | 0.0743 | ±0.1486 | -0.490 | 0.6239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **241**, R² = **0.1422**, Adj R² = **0.0890**, F-statistic = **2.68** (p = **0.0012**), Residual SE = **14.387** on **226** df, AIC = **1983.6**, BIC = **2035.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.7423** | 8.6757 | ±17.3514 | **+14.955** | **1.45e-50** | *** |
| Education: graduate level (vs college) | -2.0416 | 1.9748 | ±3.9497 | -1.034 | 0.3012 |  |
| Education: high school or below (vs college) | +10.0088 | 5.4018 | ±10.8035 | +1.853 | 0.0639 | . |
| Site: UCSD (vs UAB) | +0.2463 | 2.9347 | ±5.8693 | +0.084 | 0.9331 |  |
| **Site: UW (vs UAB)** | **-6.1531** | 2.5867 | ±5.1733 | **-2.379** | **0.0174** | * |
| **Season: spring (vs autumn)** | **+5.3964** | 2.6915 | ±5.3830 | **+2.005** | **0.0450** | * |
| Season: summer (vs autumn) | -1.6809 | 3.2669 | ±6.5338 | -0.515 | 0.6069 |  |
| Season: winter (vs autumn) | -1.6124 | 2.6503 | ±5.3007 | -0.608 | 0.5429 |  |
| Age (years) | -0.1575 | 0.0921 | ±0.1842 | -1.711 | 0.0871 | . |
| BMI (kg/m2) | +0.2989 | 0.1797 | ±0.3595 | +1.663 | 0.0963 | . |
| Hypertension | -0.4303 | 2.1684 | ±4.3368 | -0.198 | 0.8427 |  |
| High cholesterol | +1.4540 | 1.9613 | ±3.9226 | +0.741 | 0.4585 |  |
| Kidney disease | -1.6960 | 3.9687 | ±7.9373 | -0.427 | 0.6691 |  |
| Circulatory disease | -1.6561 | 3.4048 | ±6.8096 | -0.486 | 0.6267 |  |
| Nocturnal time > 180 (%) | -0.0510 | 0.0742 | ±0.1484 | -0.687 | 0.4923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **241**, R² = **0.1530**, Adj R² = **0.1005**, F-statistic = **2.92** (p = **4.34e-04**), Residual SE = **14.295** on **226** df, AIC = **1980.5**, BIC = **2032.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4886** | 8.7065 | ±17.4131 | **+14.987** | **8.87e-51** | *** |
| Education: graduate level (vs college) | -2.0458 | 1.9714 | ±3.9427 | -1.038 | 0.2994 |  |
| **Education: high school or below (vs college)** | **+11.0067** | 5.3982 | ±10.7965 | **+2.039** | **0.0415** | * |
| Site: UCSD (vs UAB) | +0.1046 | 2.9349 | ±5.8697 | +0.036 | 0.9716 |  |
| **Site: UW (vs UAB)** | **-6.2566** | 2.5679 | ±5.1359 | **-2.436** | **0.0148** | * |
| **Season: spring (vs autumn)** | **+5.3734** | 2.6911 | ±5.3822 | **+1.997** | **0.0459** | * |
| Season: summer (vs autumn) | -1.7896 | 3.2572 | ±6.5143 | -0.549 | 0.5827 |  |
| Season: winter (vs autumn) | -1.7014 | 2.6427 | ±5.2853 | -0.644 | 0.5197 |  |
| Age (years) | -0.1601 | 0.0903 | ±0.1806 | -1.774 | 0.0761 | . |
| BMI (kg/m2) | +0.2840 | 0.1776 | ±0.3553 | +1.599 | 0.1099 |  |
| Hypertension | -0.5367 | 2.1387 | ±4.2774 | -0.251 | 0.8018 |  |
| High cholesterol | +1.2132 | 1.9679 | ±3.9357 | +0.617 | 0.5376 |  |
| Kidney disease | -1.7331 | 4.0339 | ±8.0679 | -0.430 | 0.6675 |  |
| Circulatory disease | -0.9343 | 3.4786 | ±6.9571 | -0.269 | 0.7882 |  |
| **Time > 250 (%)** | **-0.1709** | 0.0860 | ±0.1719 | **-1.989** | **0.0467** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 241)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **241**, R² = **0.1531**, Adj R² = **0.1006**, F-statistic = **2.92** (p = **4.33e-04**), Residual SE = **14.295** on **226** df, AIC = **1980.5**, BIC = **2032.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4255** | 8.7005 | ±17.4010 | **+14.991** | **8.46e-51** | *** |
| Education: graduate level (vs college) | -2.0426 | 1.9712 | ±3.9425 | -1.036 | 0.3001 |  |
| **Education: high school or below (vs college)** | **+11.0265** | 5.4061 | ±10.8123 | **+2.040** | **0.0414** | * |
| Site: UCSD (vs UAB) | +0.0931 | 2.9365 | ±5.8730 | +0.032 | 0.9747 |  |
| **Site: UW (vs UAB)** | **-6.2452** | 2.5671 | ±5.1343 | **-2.433** | **0.0150** | * |
| **Season: spring (vs autumn)** | **+5.3586** | 2.6912 | ±5.3824 | **+1.991** | **0.0465** | * |
| Season: summer (vs autumn) | -1.8022 | 3.2576 | ±6.5151 | -0.553 | 0.5801 |  |
| Season: winter (vs autumn) | -1.7277 | 2.6438 | ±5.2876 | -0.653 | 0.5134 |  |
| Age (years) | -0.1598 | 0.0903 | ±0.1805 | -1.771 | 0.0766 | . |
| BMI (kg/m2) | +0.2857 | 0.1773 | ±0.3546 | +1.611 | 0.1071 |  |
| Hypertension | -0.5296 | 2.1387 | ±4.2774 | -0.248 | 0.8044 |  |
| High cholesterol | +1.2055 | 1.9692 | ±3.9385 | +0.612 | 0.5404 |  |
| Kidney disease | -1.7534 | 4.0403 | ±8.0805 | -0.434 | 0.6643 |  |
| Circulatory disease | -0.9154 | 3.4851 | ±6.9702 | -0.263 | 0.7928 |  |
| **Avg. daily time > 250 (%)** | **-0.1746** | 0.0881 | ±0.1761 | **-1.982** | **0.0474** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 120 single-predictor tests; 18 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 241): best single predictor out of sample is **MAG** (CV R² 0.019 vs 0.010 for covariates alone, gain +0.009; +0.0966 per SD, p = 0.079). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor temperature, mean (deg C)** (n = 241): best single predictor out of sample is **SD (pooled)** (CV R² 0.263 vs 0.239 for covariates alone, gain +0.024; +0.34 per SD, p = 0.010). Raw p < 0.05 (FDR not applicable here): %<54 (daily avg) (p = 4.0e-05), Daily range (p = 0.004), SD (daily avg) (p = 0.009), SD (pooled) (p = 0.010), TIR 70-180 (daily avg) (p = 0.012).
- **Indoor relative humidity, mean (%)** (n = 241): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.097 vs 0.097 for covariates alone, gain -0.000; -0.489 per SD, p = 0.160). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 241): best single predictor out of sample is **%54-69 (daily avg)** (CV R² -0.013 vs -0.028 for covariates alone, gain +0.015; -1.85 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): %54-69 (daily avg) (p = 0.001), %54-69 (pooled) (p = 0.002), %<70 (daily avg) (p = 0.009), %54-250 (pooled) (p = 0.036), %<70 (pooled) (p = 0.037).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor temperature, mean (deg C) (+0.024, via SD (pooled)); Indoor VOC index, mean (+0.015, via %54-69 (daily avg)); Indoor PM2.5, log(1 + mean ug/m3) (+0.009, via MAG); Indoor relative humidity, mean (%) (-0.000, via %<54 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 3 raw-significant of 32); Range 70-180 (0 FDR-significant / 2 raw-significant of 8); Band 54-69 (0 FDR-significant / 2 raw-significant of 8).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (3 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor PM2.5, log(1 + mean ug/m3) (MAG, ΔAIC -2.5); Indoor temperature, mean (Daily range, ΔAIC -6.3).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
