# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.1493**, Adj R² = **0.0891**, F-statistic = **2.48** (p = **0.0038**), Residual SE = **0.836** on **184** df, AIC = **504.4**, BIC = **550.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7859** | 0.5826 | ±1.1651 | **+3.066** | **0.0022** | ** |
| **Education: graduate level (vs college)** | **-0.2419** | 0.1222 | ±0.2443 | **-1.980** | **0.0477** | * |
| **Education: high school or below (vs college)** | **+0.4842** | 0.2466 | ±0.4931 | **+1.964** | **0.0496** | * |
| Site: UCSD (vs UAB) | +0.1612 | 0.1639 | ±0.3277 | +0.984 | 0.3252 |  |
| Site: UW (vs UAB) | -0.0740 | 0.1579 | ±0.3157 | -0.469 | 0.6393 |  |
| Season: spring (vs autumn) | +0.0746 | 0.1737 | ±0.3475 | +0.429 | 0.6676 |  |
| Season: summer (vs autumn) | +0.0553 | 0.1658 | ±0.3315 | +0.334 | 0.7388 |  |
| Season: winter (vs autumn) | +0.0259 | 0.1502 | ±0.3004 | +0.173 | 0.8630 |  |
| Age (years) | -0.0084 | 0.0067 | ±0.0134 | -1.264 | 0.2064 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0211 | +1.815 | 0.0695 | . |
| Hypertension | +0.1426 | 0.1418 | ±0.2836 | +1.006 | 0.3144 |  |
| High cholesterol | -0.0802 | 0.1253 | ±0.2506 | -0.640 | 0.5219 |  |
| Kidney disease | -0.0778 | 0.1869 | ±0.3737 | -0.417 | 0.6770 |  |
| Circulatory disease | -0.0159 | 0.1670 | ±0.3340 | -0.095 | 0.9241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.1495**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6261** | 0.7716 | ±1.5431 | **+2.108** | **0.0351** | * |
| Education: graduate level (vs college) | -0.2408 | 0.1231 | ±0.2462 | -1.956 | 0.0505 | . |
| Education: high school or below (vs college) | +0.4829 | 0.2464 | ±0.4928 | +1.960 | 0.0500 | . |
| Site: UCSD (vs UAB) | +0.1615 | 0.1643 | ±0.3287 | +0.983 | 0.3257 |  |
| Site: UW (vs UAB) | -0.0735 | 0.1584 | ±0.3167 | -0.464 | 0.6427 |  |
| Season: spring (vs autumn) | +0.0755 | 0.1742 | ±0.3483 | +0.434 | 0.6645 |  |
| Season: summer (vs autumn) | +0.0516 | 0.1663 | ±0.3325 | +0.311 | 0.7561 |  |
| Season: winter (vs autumn) | +0.0237 | 0.1510 | ±0.3021 | +0.157 | 0.8754 |  |
| Age (years) | -0.0085 | 0.0067 | ±0.0134 | -1.268 | 0.2048 |  |
| BMI (kg/m2) | +0.0187 | 0.0111 | ±0.0221 | +1.691 | 0.0909 | . |
| Hypertension | +0.1417 | 0.1425 | ±0.2850 | +0.994 | 0.3202 |  |
| High cholesterol | -0.0833 | 0.1256 | ±0.2512 | -0.663 | 0.5071 |  |
| Kidney disease | -0.0732 | 0.1866 | ±0.3732 | -0.392 | 0.6949 |  |
| Circulatory disease | -0.0225 | 0.1707 | ±0.3413 | -0.132 | 0.8951 |  |
| HbA1c (%) | +0.0301 | 0.1069 | ±0.2138 | +0.282 | 0.7780 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.1506**, Adj R² = **0.0856**, F-statistic = **2.32** (p = **0.0059**), Residual SE = **0.837** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0988** | 0.7522 | ±1.5044 | **+2.790** | **0.0053** | ** |
| **Education: graduate level (vs college)** | **-0.2419** | 0.1227 | ±0.2454 | **-1.971** | **0.0487** | * |
| Education: high school or below (vs college) | +0.4781 | 0.2482 | ±0.4965 | +1.926 | 0.0541 | . |
| Site: UCSD (vs UAB) | +0.1607 | 0.1641 | ±0.3282 | +0.979 | 0.3276 |  |
| Site: UW (vs UAB) | -0.0768 | 0.1589 | ±0.3178 | -0.483 | 0.6288 |  |
| Season: spring (vs autumn) | +0.0771 | 0.1754 | ±0.3509 | +0.440 | 0.6602 |  |
| Season: summer (vs autumn) | +0.0653 | 0.1681 | ±0.3362 | +0.388 | 0.6977 |  |
| Season: winter (vs autumn) | +0.0302 | 0.1524 | ±0.3048 | +0.198 | 0.8430 |  |
| Age (years) | -0.0085 | 0.0067 | ±0.0135 | -1.262 | 0.2068 |  |
| BMI (kg/m2) | +0.0196 | 0.0108 | ±0.0216 | +1.812 | 0.0700 | . |
| Hypertension | +0.1470 | 0.1424 | ±0.2848 | +1.032 | 0.3019 |  |
| High cholesterol | -0.0828 | 0.1257 | ±0.2513 | -0.659 | 0.5097 |  |
| Kidney disease | -0.0699 | 0.1889 | ±0.3778 | -0.370 | 0.7113 |  |
| Circulatory disease | -0.0122 | 0.1676 | ±0.3353 | -0.073 | 0.9421 |  |
| Mean glucose (mg/dL) | -0.0026 | 0.0048 | ±0.0096 | -0.537 | 0.5915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.1506**, Adj R² = **0.0856**, F-statistic = **2.32** (p = **0.0059**), Residual SE = **0.837** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.4557 | 1.2846 | ±2.5692 | +1.912 | 0.0559 | . |
| **Education: graduate level (vs college)** | **-0.2419** | 0.1227 | ±0.2454 | **-1.971** | **0.0487** | * |
| Education: high school or below (vs college) | +0.4781 | 0.2482 | ±0.4965 | +1.926 | 0.0541 | . |
| Site: UCSD (vs UAB) | +0.1607 | 0.1641 | ±0.3282 | +0.979 | 0.3276 |  |
| Site: UW (vs UAB) | -0.0768 | 0.1589 | ±0.3178 | -0.483 | 0.6288 |  |
| Season: spring (vs autumn) | +0.0771 | 0.1754 | ±0.3509 | +0.440 | 0.6602 |  |
| Season: summer (vs autumn) | +0.0653 | 0.1681 | ±0.3362 | +0.388 | 0.6977 |  |
| Season: winter (vs autumn) | +0.0302 | 0.1524 | ±0.3048 | +0.198 | 0.8430 |  |
| Age (years) | -0.0085 | 0.0067 | ±0.0135 | -1.262 | 0.2068 |  |
| BMI (kg/m2) | +0.0196 | 0.0108 | ±0.0216 | +1.812 | 0.0700 | . |
| Hypertension | +0.1470 | 0.1424 | ±0.2848 | +1.032 | 0.3019 |  |
| High cholesterol | -0.0828 | 0.1257 | ±0.2513 | -0.659 | 0.5097 |  |
| Kidney disease | -0.0699 | 0.1889 | ±0.3778 | -0.370 | 0.7113 |  |
| Circulatory disease | -0.0122 | 0.1676 | ±0.3353 | -0.073 | 0.9421 |  |
| GMI (%) | -0.1078 | 0.2009 | ±0.4018 | -0.537 | 0.5915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.1504**, Adj R² = **0.0854**, F-statistic = **2.31** (p = **0.0060**), Residual SE = **0.838** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0459** | 0.6840 | ±1.3679 | **+2.991** | **0.0028** | ** |
| Education: graduate level (vs college) | -0.2396 | 0.1231 | ±0.2462 | -1.947 | 0.0516 | . |
| Education: high school or below (vs college) | +0.4805 | 0.2488 | ±0.4976 | +1.931 | 0.0535 | . |
| Site: UCSD (vs UAB) | +0.1626 | 0.1650 | ±0.3300 | +0.986 | 0.3243 |  |
| Site: UW (vs UAB) | -0.0747 | 0.1591 | ±0.3182 | -0.470 | 0.6386 |  |
| Season: spring (vs autumn) | +0.0750 | 0.1747 | ±0.3494 | +0.429 | 0.6676 |  |
| Season: summer (vs autumn) | +0.0618 | 0.1666 | ±0.3333 | +0.371 | 0.7107 |  |
| Season: winter (vs autumn) | +0.0262 | 0.1514 | ±0.3027 | +0.173 | 0.8625 |  |
| Age (years) | -0.0087 | 0.0067 | ±0.0135 | -1.299 | 0.1940 |  |
| BMI (kg/m2) | +0.0197 | 0.0109 | ±0.0219 | +1.796 | 0.0724 | . |
| Hypertension | +0.1441 | 0.1420 | ±0.2841 | +1.015 | 0.3103 |  |
| High cholesterol | -0.0794 | 0.1257 | ±0.2514 | -0.631 | 0.5277 |  |
| Kidney disease | -0.0769 | 0.1874 | ±0.3748 | -0.410 | 0.6815 |  |
| Circulatory disease | -0.0104 | 0.1683 | ±0.3365 | -0.062 | 0.9505 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0021 | 0.0044 | ±0.0088 | -0.472 | 0.6370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1603**, Adj R² = **0.0960**, F-statistic = **2.49** (p = **0.0029**), Residual SE = **0.833** on **183** df, AIC = **503.8**, BIC = **553.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.3737** | 0.5927 | ±1.1854 | **+2.318** | **0.0205** | * |
| **Education: graduate level (vs college)** | **-0.2556** | 0.1208 | ±0.2415 | **-2.116** | **0.0343** | * |
| Education: high school or below (vs college) | +0.4305 | 0.2462 | ±0.4925 | +1.748 | 0.0804 | . |
| Site: UCSD (vs UAB) | +0.1801 | 0.1627 | ±0.3254 | +1.107 | 0.2684 |  |
| Site: UW (vs UAB) | -0.0364 | 0.1564 | ±0.3128 | -0.233 | 0.8158 |  |
| Season: spring (vs autumn) | +0.0757 | 0.1727 | ±0.3454 | +0.439 | 0.6610 |  |
| Season: summer (vs autumn) | +0.0576 | 0.1640 | ±0.3280 | +0.351 | 0.7257 |  |
| Season: winter (vs autumn) | +0.0269 | 0.1491 | ±0.2983 | +0.180 | 0.8571 |  |
| Age (years) | -0.0092 | 0.0067 | ±0.0133 | -1.385 | 0.1661 |  |
| BMI (kg/m2) | +0.0194 | 0.0104 | ±0.0208 | +1.861 | 0.0628 | . |
| Hypertension | +0.1079 | 0.1449 | ±0.2898 | +0.745 | 0.4563 |  |
| High cholesterol | -0.0659 | 0.1255 | ±0.2510 | -0.525 | 0.5995 |  |
| Kidney disease | -0.1212 | 0.1900 | ±0.3800 | -0.638 | 0.5236 |  |
| Circulatory disease | -0.0313 | 0.1638 | ±0.3275 | -0.191 | 0.8485 |  |
| Glucose SD, pooled (mg/dL) | +0.0214 | 0.0127 | ±0.0255 | +1.678 | 0.0934 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1559**, Adj R² = **0.0913**, F-statistic = **2.41** (p = **0.0040**), Residual SE = **0.835** on **183** df, AIC = **504.8**, BIC = **554.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4931** | 0.5915 | ±1.1830 | **+2.524** | **0.0116** | * |
| **Education: graduate level (vs college)** | **-0.2508** | 0.1213 | ±0.2425 | **-2.068** | **0.0386** | * |
| Education: high school or below (vs college) | +0.4500 | 0.2470 | ±0.4939 | +1.822 | 0.0684 | . |
| Site: UCSD (vs UAB) | +0.1665 | 0.1636 | ±0.3272 | +1.018 | 0.3088 |  |
| Site: UW (vs UAB) | -0.0533 | 0.1574 | ±0.3149 | -0.339 | 0.7348 |  |
| Season: spring (vs autumn) | +0.0810 | 0.1726 | ±0.3452 | +0.469 | 0.6387 |  |
| Season: summer (vs autumn) | +0.0630 | 0.1655 | ±0.3310 | +0.381 | 0.7035 |  |
| Season: winter (vs autumn) | +0.0301 | 0.1495 | ±0.2991 | +0.201 | 0.8407 |  |
| Age (years) | -0.0091 | 0.0067 | ±0.0134 | -1.356 | 0.1752 |  |
| BMI (kg/m2) | +0.0193 | 0.0104 | ±0.0209 | +1.853 | 0.0640 | . |
| Hypertension | +0.1090 | 0.1447 | ±0.2894 | +0.753 | 0.4512 |  |
| High cholesterol | -0.0686 | 0.1265 | ±0.2530 | -0.543 | 0.5875 |  |
| Kidney disease | -0.1016 | 0.1869 | ±0.3737 | -0.544 | 0.5865 |  |
| Circulatory disease | -0.0195 | 0.1658 | ±0.3316 | -0.117 | 0.9065 |  |
| Avg. daily SD (mg/dL) | +0.0168 | 0.0122 | ±0.0243 | +1.379 | 0.1678 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.1723**, Adj R² = **0.1090**, F-statistic = **2.72** (p = **0.0012**), Residual SE = **0.827** on **183** df, AIC = **500.9**, BIC = **550.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0552 | 0.6253 | ±1.2506 | +1.688 | 0.0915 | . |
| **Education: graduate level (vs college)** | **-0.2639** | 0.1188 | ±0.2376 | **-2.221** | **0.0263** | * |
| Education: high school or below (vs college) | +0.3744 | 0.2481 | ±0.4961 | +1.509 | 0.1312 |  |
| Site: UCSD (vs UAB) | +0.1933 | 0.1625 | ±0.3249 | +1.190 | 0.2340 |  |
| Site: UW (vs UAB) | -0.0162 | 0.1562 | ±0.3124 | -0.104 | 0.9173 |  |
| Season: spring (vs autumn) | +0.0815 | 0.1721 | ±0.3441 | +0.473 | 0.6359 |  |
| Season: summer (vs autumn) | +0.0830 | 0.1656 | ±0.3312 | +0.501 | 0.6164 |  |
| Season: winter (vs autumn) | +0.0335 | 0.1490 | ±0.2981 | +0.225 | 0.8222 |  |
| Age (years) | -0.0099 | 0.0067 | ±0.0133 | -1.490 | 0.1362 |  |
| **BMI (kg/m2)** | **+0.0205** | 0.0103 | ±0.0205 | **+1.996** | **0.0459** | * |
| Hypertension | +0.0933 | 0.1429 | ±0.2859 | +0.653 | 0.5138 |  |
| High cholesterol | -0.0621 | 0.1236 | ±0.2473 | -0.503 | 0.6152 |  |
| Kidney disease | -0.1343 | 0.1856 | ±0.3713 | -0.723 | 0.4694 |  |
| Circulatory disease | -0.0296 | 0.1601 | ±0.3202 | -0.185 | 0.8531 |  |
| **CV (%)** | **+0.0462** | 0.0194 | ±0.0388 | **+2.378** | **0.0174** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.1681**, Adj R² = **0.1045**, F-statistic = **2.64** (p = **0.0016**), Residual SE = **0.829** on **183** df, AIC = **501.9**, BIC = **551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5297** | 0.6592 | ±1.3183 | **+3.838** | **1.24e-04** | *** |
| **Education: graduate level (vs college)** | **-0.2580** | 0.1204 | ±0.2409 | **-2.143** | **0.0321** | * |
| Education: high school or below (vs college) | +0.3967 | 0.2469 | ±0.4938 | +1.607 | 0.1081 |  |
| Site: UCSD (vs UAB) | +0.1835 | 0.1630 | ±0.3259 | +1.126 | 0.2601 |  |
| Site: UW (vs UAB) | -0.0283 | 0.1560 | ±0.3121 | -0.181 | 0.8561 |  |
| Season: spring (vs autumn) | +0.0801 | 0.1718 | ±0.3436 | +0.466 | 0.6409 |  |
| Season: summer (vs autumn) | +0.0776 | 0.1655 | ±0.3311 | +0.469 | 0.6392 |  |
| Season: winter (vs autumn) | +0.0302 | 0.1491 | ±0.2983 | +0.202 | 0.8397 |  |
| Age (years) | -0.0098 | 0.0066 | ±0.0133 | -1.479 | 0.1391 |  |
| BMI (kg/m2) | +0.0196 | 0.0104 | ±0.0207 | +1.891 | 0.0587 | . |
| Hypertension | +0.0956 | 0.1422 | ±0.2845 | +0.672 | 0.5017 |  |
| High cholesterol | -0.0695 | 0.1235 | ±0.2471 | -0.563 | 0.5737 |  |
| Kidney disease | -0.1268 | 0.1854 | ±0.3709 | -0.684 | 0.4940 |  |
| Circulatory disease | -0.0209 | 0.1612 | ±0.3223 | -0.129 | 0.8970 |  |
| **Mean / SD ratio** | **-0.1085** | 0.0467 | ±0.0933 | **-2.326** | **0.0200** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1612**, Adj R² = **0.0971**, F-statistic = **2.51** (p = **0.0027**), Residual SE = **0.832** on **183** df, AIC = **503.6**, BIC = **552.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3261** | 0.6549 | ±1.3098 | **+3.552** | **3.83e-04** | *** |
| **Education: graduate level (vs college)** | **-0.2484** | 0.1215 | ±0.2430 | **-2.045** | **0.0409** | * |
| Education: high school or below (vs college) | +0.4304 | 0.2472 | ±0.4944 | +1.741 | 0.0816 | . |
| Site: UCSD (vs UAB) | +0.1594 | 0.1630 | ±0.3259 | +0.978 | 0.3280 |  |
| Site: UW (vs UAB) | -0.0489 | 0.1567 | ±0.3133 | -0.312 | 0.7551 |  |
| Season: spring (vs autumn) | +0.0824 | 0.1722 | ±0.3444 | +0.479 | 0.6323 |  |
| Season: summer (vs autumn) | +0.0780 | 0.1667 | ±0.3334 | +0.468 | 0.6401 |  |
| Season: winter (vs autumn) | +0.0380 | 0.1502 | ±0.3005 | +0.253 | 0.8005 |  |
| Age (years) | -0.0096 | 0.0067 | ±0.0134 | -1.435 | 0.1513 |  |
| BMI (kg/m2) | +0.0193 | 0.0104 | ±0.0208 | +1.862 | 0.0626 | . |
| Hypertension | +0.0931 | 0.1427 | ±0.2853 | +0.653 | 0.5140 |  |
| High cholesterol | -0.0763 | 0.1245 | ±0.2491 | -0.613 | 0.5401 |  |
| Kidney disease | -0.1055 | 0.1842 | ±0.3683 | -0.573 | 0.5668 |  |
| Circulatory disease | -0.0023 | 0.1647 | ±0.3294 | -0.014 | 0.9891 |  |
| Avg. daily mean/SD | -0.0661 | 0.0366 | ±0.0733 | -1.805 | 0.0710 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.1553**, Adj R² = **0.0907**, F-statistic = **2.40** (p = **0.0042**), Residual SE = **0.835** on **183** df, AIC = **504.9**, BIC = **554.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4050** | 0.5938 | ±1.1875 | **+2.366** | **0.0180** | * |
| **Education: graduate level (vs college)** | **-0.2446** | 0.1218 | ±0.2436 | **-2.009** | **0.0446** | * |
| Education: high school or below (vs college) | +0.4661 | 0.2490 | ±0.4980 | +1.872 | 0.0612 | . |
| Site: UCSD (vs UAB) | +0.1606 | 0.1645 | ±0.3289 | +0.976 | 0.3289 |  |
| Site: UW (vs UAB) | -0.0645 | 0.1575 | ±0.3150 | -0.409 | 0.6822 |  |
| Season: spring (vs autumn) | +0.0777 | 0.1733 | ±0.3466 | +0.448 | 0.6540 |  |
| Season: summer (vs autumn) | +0.0580 | 0.1637 | ±0.3274 | +0.354 | 0.7230 |  |
| Season: winter (vs autumn) | +0.0306 | 0.1511 | ±0.3023 | +0.203 | 0.8393 |  |
| Age (years) | -0.0083 | 0.0066 | ±0.0133 | -1.247 | 0.2124 |  |
| BMI (kg/m2) | +0.0188 | 0.0106 | ±0.0213 | +1.770 | 0.0767 | . |
| Hypertension | +0.1331 | 0.1430 | ±0.2859 | +0.931 | 0.3520 |  |
| High cholesterol | -0.0866 | 0.1246 | ±0.2492 | -0.695 | 0.4873 |  |
| Kidney disease | -0.0769 | 0.1875 | ±0.3750 | -0.410 | 0.6819 |  |
| Circulatory disease | -0.0038 | 0.1679 | ±0.3358 | -0.023 | 0.9818 |  |
| MAG (mg/dL/h) | +0.0106 | 0.0076 | ±0.0152 | +1.402 | 0.1608 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.1603**, Adj R² = **0.0960**, F-statistic = **2.50** (p = **0.0029**), Residual SE = **0.833** on **183** df, AIC = **503.8**, BIC = **553.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.2989** | 0.6104 | ±1.2209 | **+2.128** | **0.0334** | * |
| **Education: graduate level (vs college)** | **-0.2479** | 0.1210 | ±0.2420 | **-2.049** | **0.0405** | * |
| Education: high school or below (vs college) | +0.4490 | 0.2480 | ±0.4960 | +1.811 | 0.0702 | . |
| Site: UCSD (vs UAB) | +0.1739 | 0.1631 | ±0.3262 | +1.066 | 0.2865 |  |
| Site: UW (vs UAB) | -0.0487 | 0.1568 | ±0.3137 | -0.310 | 0.7562 |  |
| Season: spring (vs autumn) | +0.0786 | 0.1729 | ±0.3457 | +0.455 | 0.6494 |  |
| Season: summer (vs autumn) | +0.0682 | 0.1638 | ±0.3277 | +0.416 | 0.6774 |  |
| Season: winter (vs autumn) | +0.0346 | 0.1495 | ±0.2991 | +0.231 | 0.8171 |  |
| Age (years) | -0.0093 | 0.0066 | ±0.0133 | -1.404 | 0.1604 |  |
| BMI (kg/m2) | +0.0201 | 0.0103 | ±0.0207 | +1.940 | 0.0524 | . |
| Hypertension | +0.1109 | 0.1435 | ±0.2870 | +0.773 | 0.4396 |  |
| High cholesterol | -0.0735 | 0.1250 | ±0.2500 | -0.588 | 0.5566 |  |
| Kidney disease | -0.0969 | 0.1850 | ±0.3699 | -0.524 | 0.6004 |  |
| Circulatory disease | -0.0145 | 0.1665 | ±0.3331 | -0.087 | 0.9307 |  |
| Avg. daily range (mg/dL) | +0.0054 | 0.0029 | ±0.0058 | +1.837 | 0.0662 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.1678**, Adj R² = **0.1041**, F-statistic = **2.64** (p = **0.0016**), Residual SE = **0.829** on **183** df, AIC = **502.0**, BIC = **551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4751** | 0.5852 | ±1.1705 | **+2.521** | **0.0117** | * |
| **Education: graduate level (vs college)** | **-0.2567** | 0.1214 | ±0.2428 | **-2.114** | **0.0345** | * |
| Education: high school or below (vs college) | +0.4154 | 0.2366 | ±0.4732 | +1.756 | 0.0791 | . |
| Site: UCSD (vs UAB) | +0.2145 | 0.1572 | ±0.3144 | +1.365 | 0.1724 |  |
| Site: UW (vs UAB) | -0.0129 | 0.1522 | ±0.3043 | -0.085 | 0.9326 |  |
| Season: spring (vs autumn) | +0.0507 | 0.1724 | ±0.3447 | +0.294 | 0.7686 |  |
| Season: summer (vs autumn) | +0.0077 | 0.1629 | ±0.3258 | +0.047 | 0.9622 |  |
| Season: winter (vs autumn) | +0.0230 | 0.1495 | ±0.2989 | +0.154 | 0.8777 |  |
| Age (years) | -0.0088 | 0.0066 | ±0.0131 | -1.333 | 0.1825 |  |
| BMI (kg/m2) | +0.0190 | 0.0105 | ±0.0210 | +1.809 | 0.0705 | . |
| Hypertension | +0.1639 | 0.1440 | ±0.2881 | +1.138 | 0.2551 |  |
| High cholesterol | -0.0878 | 0.1247 | ±0.2493 | -0.705 | 0.4811 |  |
| Kidney disease | -0.1447 | 0.2062 | ±0.4124 | -0.702 | 0.4827 |  |
| Circulatory disease | -0.0862 | 0.1577 | ±0.3154 | -0.546 | 0.5848 |  |
| SD of daily means (mg/dL) | +0.0515 | 0.0317 | ±0.0634 | +1.626 | 0.1040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.1495**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.4659 | 1.4994 | ±2.9989 | +0.978 | 0.3283 |  |
| Education: graduate level (vs college) | -0.2400 | 0.1229 | ±0.2458 | -1.953 | 0.0508 | . |
| **Education: high school or below (vs college)** | **+0.4882** | 0.2477 | ±0.4953 | **+1.971** | **0.0487** | * |
| Site: UCSD (vs UAB) | +0.1584 | 0.1633 | ±0.3266 | +0.970 | 0.3322 |  |
| Site: UW (vs UAB) | -0.0769 | 0.1595 | ±0.3189 | -0.482 | 0.6295 |  |
| Season: spring (vs autumn) | +0.0743 | 0.1746 | ±0.3491 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0576 | 0.1672 | ±0.3344 | +0.344 | 0.7305 |  |
| Season: winter (vs autumn) | +0.0272 | 0.1520 | ±0.3039 | +0.179 | 0.8580 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.219 | 0.2227 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0213 | +1.807 | 0.0708 | . |
| Hypertension | +0.1445 | 0.1424 | ±0.2849 | +1.014 | 0.3105 |  |
| High cholesterol | -0.0821 | 0.1270 | ±0.2540 | -0.647 | 0.5177 |  |
| Kidney disease | -0.0713 | 0.1927 | ±0.3854 | -0.370 | 0.7113 |  |
| Circulatory disease | -0.0141 | 0.1677 | ±0.3354 | -0.084 | 0.9330 |  |
| Time in range 70-180, pooled (%) | +0.0032 | 0.0128 | ±0.0257 | +0.250 | 0.8029 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.1494**, Adj R² = **0.0843**, F-statistic = **2.30** (p = **0.0064**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.5317 | 1.5583 | ±3.1166 | +0.983 | 0.3256 |  |
| Education: graduate level (vs college) | -0.2406 | 0.1229 | ±0.2457 | -1.958 | 0.0502 | . |
| **Education: high school or below (vs college)** | **+0.4868** | 0.2474 | ±0.4947 | **+1.968** | **0.0491** | * |
| Site: UCSD (vs UAB) | +0.1590 | 0.1632 | ±0.3264 | +0.974 | 0.3299 |  |
| Site: UW (vs UAB) | -0.0759 | 0.1594 | ±0.3187 | -0.476 | 0.6341 |  |
| Season: spring (vs autumn) | +0.0742 | 0.1744 | ±0.3489 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0572 | 0.1672 | ±0.3344 | +0.342 | 0.7324 |  |
| Season: winter (vs autumn) | +0.0270 | 0.1520 | ±0.3039 | +0.177 | 0.8591 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.222 | 0.2218 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0212 | +1.808 | 0.0707 | . |
| Hypertension | +0.1444 | 0.1425 | ±0.2850 | +1.013 | 0.3108 |  |
| High cholesterol | -0.0816 | 0.1271 | ±0.2541 | -0.642 | 0.5206 |  |
| Kidney disease | -0.0727 | 0.1930 | ±0.3860 | -0.376 | 0.7066 |  |
| Circulatory disease | -0.0146 | 0.1678 | ±0.3355 | -0.087 | 0.9309 |  |
| Avg. daily time in range 70-180 (%) | +0.0025 | 0.0135 | ±0.0270 | +0.189 | 0.8504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.1651**, Adj R² = **0.1012**, F-statistic = **2.58** (p = **0.0020**), Residual SE = **0.830** on **183** df, AIC = **502.6**, BIC = **552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8165** | 0.6040 | ±1.2081 | **+3.007** | **0.0026** | ** |
| **Education: graduate level (vs college)** | **-0.2575** | 0.1211 | ±0.2422 | **-2.127** | **0.0335** | * |
| Education: high school or below (vs college) | +0.4341 | 0.2448 | ±0.4896 | +1.773 | 0.0761 | . |
| Site: UCSD (vs UAB) | +0.1813 | 0.1625 | ±0.3251 | +1.116 | 0.2646 |  |
| Site: UW (vs UAB) | -0.0683 | 0.1655 | ±0.3310 | -0.413 | 0.6799 |  |
| Season: spring (vs autumn) | +0.1051 | 0.1738 | ±0.3476 | +0.605 | 0.5452 |  |
| Season: summer (vs autumn) | +0.0728 | 0.1733 | ±0.3465 | +0.420 | 0.6745 |  |
| Season: winter (vs autumn) | +0.0600 | 0.1539 | ±0.3079 | +0.390 | 0.6966 |  |
| Age (years) | -0.0103 | 0.0073 | ±0.0145 | -1.413 | 0.1577 |  |
| BMI (kg/m2) | +0.0201 | 0.0105 | ±0.0210 | +1.909 | 0.0562 | . |
| Hypertension | +0.1320 | 0.1430 | ±0.2861 | +0.923 | 0.3562 |  |
| High cholesterol | -0.0949 | 0.1248 | ±0.2496 | -0.761 | 0.4469 |  |
| Kidney disease | -0.0608 | 0.1886 | ±0.3771 | -0.322 | 0.7472 |  |
| Circulatory disease | -0.0178 | 0.1681 | ±0.3363 | -0.106 | 0.9157 |  |
| Time 54-69, pooled (%) | +0.4201 | 0.5556 | ±1.1113 | +0.756 | 0.4497 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.1579**, Adj R² = **0.0934**, F-statistic = **2.45** (p = **0.0035**), Residual SE = **0.834** on **183** df, AIC = **504.3**, BIC = **553.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8215** | 0.6066 | ±1.2133 | **+3.003** | **0.0027** | ** |
| **Education: graduate level (vs college)** | **-0.2530** | 0.1210 | ±0.2419 | **-2.092** | **0.0365** | * |
| Education: high school or below (vs college) | +0.4486 | 0.2475 | ±0.4951 | +1.812 | 0.0700 | . |
| Site: UCSD (vs UAB) | +0.1689 | 0.1630 | ±0.3260 | +1.036 | 0.3002 |  |
| Site: UW (vs UAB) | -0.0754 | 0.1649 | ±0.3298 | -0.457 | 0.6475 |  |
| Season: spring (vs autumn) | +0.0974 | 0.1735 | ±0.3470 | +0.561 | 0.5746 |  |
| Season: summer (vs autumn) | +0.0758 | 0.1748 | ±0.3496 | +0.433 | 0.6647 |  |
| Season: winter (vs autumn) | +0.0499 | 0.1536 | ±0.3073 | +0.325 | 0.7455 |  |
| Age (years) | -0.0099 | 0.0072 | ±0.0145 | -1.364 | 0.1725 |  |
| BMI (kg/m2) | +0.0198 | 0.0105 | ±0.0211 | +1.878 | 0.0604 | . |
| Hypertension | +0.1306 | 0.1429 | ±0.2858 | +0.914 | 0.3606 |  |
| High cholesterol | -0.0910 | 0.1251 | ±0.2501 | -0.727 | 0.4670 |  |
| Kidney disease | -0.0605 | 0.1874 | ±0.3748 | -0.323 | 0.7470 |  |
| Circulatory disease | -0.0098 | 0.1707 | ±0.3414 | -0.058 | 0.9541 |  |
| Avg. daily time 54-69 (%) | +0.3017 | 0.5277 | ±1.0554 | +0.572 | 0.5675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.1651**, Adj R² = **0.1012**, F-statistic = **2.58** (p = **0.0020**), Residual SE = **0.830** on **183** df, AIC = **502.6**, BIC = **552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8165** | 0.6040 | ±1.2081 | **+3.007** | **0.0026** | ** |
| **Education: graduate level (vs college)** | **-0.2575** | 0.1211 | ±0.2422 | **-2.127** | **0.0335** | * |
| Education: high school or below (vs college) | +0.4341 | 0.2448 | ±0.4896 | +1.773 | 0.0761 | . |
| Site: UCSD (vs UAB) | +0.1813 | 0.1625 | ±0.3251 | +1.116 | 0.2646 |  |
| Site: UW (vs UAB) | -0.0683 | 0.1655 | ±0.3310 | -0.413 | 0.6799 |  |
| Season: spring (vs autumn) | +0.1051 | 0.1738 | ±0.3476 | +0.605 | 0.5452 |  |
| Season: summer (vs autumn) | +0.0728 | 0.1733 | ±0.3465 | +0.420 | 0.6745 |  |
| Season: winter (vs autumn) | +0.0600 | 0.1539 | ±0.3079 | +0.390 | 0.6966 |  |
| Age (years) | -0.0103 | 0.0073 | ±0.0145 | -1.413 | 0.1577 |  |
| BMI (kg/m2) | +0.0201 | 0.0105 | ±0.0210 | +1.909 | 0.0562 | . |
| Hypertension | +0.1320 | 0.1430 | ±0.2861 | +0.923 | 0.3562 |  |
| High cholesterol | -0.0949 | 0.1248 | ±0.2496 | -0.761 | 0.4469 |  |
| Kidney disease | -0.0608 | 0.1886 | ±0.3771 | -0.322 | 0.7472 |  |
| Circulatory disease | -0.0178 | 0.1681 | ±0.3363 | -0.106 | 0.9157 |  |
| Time < 70 (%) | +0.4201 | 0.5556 | ±1.1113 | +0.756 | 0.4497 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.1579**, Adj R² = **0.0934**, F-statistic = **2.45** (p = **0.0035**), Residual SE = **0.834** on **183** df, AIC = **504.3**, BIC = **553.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8215** | 0.6066 | ±1.2133 | **+3.003** | **0.0027** | ** |
| **Education: graduate level (vs college)** | **-0.2530** | 0.1210 | ±0.2419 | **-2.092** | **0.0365** | * |
| Education: high school or below (vs college) | +0.4486 | 0.2475 | ±0.4951 | +1.812 | 0.0700 | . |
| Site: UCSD (vs UAB) | +0.1689 | 0.1630 | ±0.3260 | +1.036 | 0.3002 |  |
| Site: UW (vs UAB) | -0.0754 | 0.1649 | ±0.3298 | -0.457 | 0.6475 |  |
| Season: spring (vs autumn) | +0.0974 | 0.1735 | ±0.3470 | +0.561 | 0.5746 |  |
| Season: summer (vs autumn) | +0.0758 | 0.1748 | ±0.3496 | +0.433 | 0.6647 |  |
| Season: winter (vs autumn) | +0.0499 | 0.1536 | ±0.3073 | +0.325 | 0.7455 |  |
| Age (years) | -0.0099 | 0.0072 | ±0.0145 | -1.364 | 0.1725 |  |
| BMI (kg/m2) | +0.0198 | 0.0105 | ±0.0211 | +1.878 | 0.0604 | . |
| Hypertension | +0.1306 | 0.1429 | ±0.2858 | +0.914 | 0.3606 |  |
| High cholesterol | -0.0910 | 0.1251 | ±0.2501 | -0.727 | 0.4670 |  |
| Kidney disease | -0.0605 | 0.1874 | ±0.3748 | -0.323 | 0.7470 |  |
| Circulatory disease | -0.0098 | 0.1707 | ±0.3414 | -0.058 | 0.9541 |  |
| Avg. daily time < 70 (%) | +0.3017 | 0.5277 | ±1.0554 | +0.572 | 0.5675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.1498**, Adj R² = **0.0848**, F-statistic = **2.30** (p = **0.0062**), Residual SE = **0.838** on **183** df, AIC = **506.2**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7866** | 0.5850 | ±1.1700 | **+3.054** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2394 | 0.1230 | ±0.2459 | -1.946 | 0.0516 | . |
| **Education: high school or below (vs college)** | **+0.4894** | 0.2479 | ±0.4957 | **+1.975** | **0.0483** | * |
| Site: UCSD (vs UAB) | +0.1574 | 0.1635 | ±0.3269 | +0.963 | 0.3357 |  |
| Site: UW (vs UAB) | -0.0781 | 0.1598 | ±0.3196 | -0.489 | 0.6249 |  |
| Season: spring (vs autumn) | +0.0744 | 0.1748 | ±0.3496 | +0.426 | 0.6702 |  |
| Season: summer (vs autumn) | +0.0587 | 0.1677 | ±0.3354 | +0.350 | 0.7261 |  |
| Season: winter (vs autumn) | +0.0281 | 0.1523 | ±0.3047 | +0.184 | 0.8537 |  |
| Age (years) | -0.0082 | 0.0068 | ±0.0135 | -1.217 | 0.2237 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0213 | +1.810 | 0.0703 | . |
| Hypertension | +0.1451 | 0.1423 | ±0.2845 | +1.020 | 0.3077 |  |
| High cholesterol | -0.0831 | 0.1270 | ±0.2541 | -0.654 | 0.5130 |  |
| Kidney disease | -0.0684 | 0.1922 | ±0.3845 | -0.356 | 0.7221 |  |
| Circulatory disease | -0.0134 | 0.1679 | ±0.3358 | -0.080 | 0.9366 |  |
| Time 181-250, pooled (%) | -0.0046 | 0.0126 | ±0.0252 | -0.362 | 0.7174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.1496**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7863** | 0.5850 | ±1.1701 | **+3.053** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2401 | 0.1229 | ±0.2459 | -1.953 | 0.0508 | . |
| **Education: high school or below (vs college)** | **+0.4875** | 0.2475 | ±0.4950 | **+1.970** | **0.0489** | * |
| Site: UCSD (vs UAB) | +0.1582 | 0.1633 | ±0.3267 | +0.968 | 0.3329 |  |
| Site: UW (vs UAB) | -0.0766 | 0.1596 | ±0.3192 | -0.480 | 0.6311 |  |
| Season: spring (vs autumn) | +0.0743 | 0.1747 | ±0.3493 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0582 | 0.1676 | ±0.3353 | +0.347 | 0.7285 |  |
| Season: winter (vs autumn) | +0.0277 | 0.1523 | ±0.3046 | +0.182 | 0.8557 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.221 | 0.2222 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0212 | +1.809 | 0.0704 | . |
| Hypertension | +0.1450 | 0.1424 | ±0.2847 | +1.019 | 0.3083 |  |
| High cholesterol | -0.0823 | 0.1271 | ±0.2542 | -0.648 | 0.5172 |  |
| Kidney disease | -0.0703 | 0.1927 | ±0.3854 | -0.365 | 0.7153 |  |
| Circulatory disease | -0.0139 | 0.1680 | ±0.3359 | -0.083 | 0.9339 |  |
| Avg. daily time 181-250 (%) | -0.0036 | 0.0132 | ±0.0264 | -0.273 | 0.7849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.1498**, Adj R² = **0.0848**, F-statistic = **2.30** (p = **0.0062**), Residual SE = **0.838** on **183** df, AIC = **506.2**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7866** | 0.5850 | ±1.1700 | **+3.054** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2394 | 0.1230 | ±0.2459 | -1.946 | 0.0516 | . |
| **Education: high school or below (vs college)** | **+0.4894** | 0.2479 | ±0.4957 | **+1.975** | **0.0483** | * |
| Site: UCSD (vs UAB) | +0.1574 | 0.1635 | ±0.3269 | +0.963 | 0.3357 |  |
| Site: UW (vs UAB) | -0.0781 | 0.1598 | ±0.3196 | -0.489 | 0.6249 |  |
| Season: spring (vs autumn) | +0.0744 | 0.1748 | ±0.3496 | +0.426 | 0.6702 |  |
| Season: summer (vs autumn) | +0.0587 | 0.1677 | ±0.3354 | +0.350 | 0.7261 |  |
| Season: winter (vs autumn) | +0.0281 | 0.1523 | ±0.3047 | +0.184 | 0.8537 |  |
| Age (years) | -0.0082 | 0.0068 | ±0.0135 | -1.217 | 0.2237 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0213 | +1.810 | 0.0703 | . |
| Hypertension | +0.1451 | 0.1423 | ±0.2845 | +1.020 | 0.3077 |  |
| High cholesterol | -0.0831 | 0.1270 | ±0.2541 | -0.654 | 0.5130 |  |
| Kidney disease | -0.0684 | 0.1922 | ±0.3845 | -0.356 | 0.7221 |  |
| Circulatory disease | -0.0134 | 0.1679 | ±0.3358 | -0.080 | 0.9366 |  |
| Time > 180 (%) | -0.0046 | 0.0126 | ±0.0252 | -0.362 | 0.7174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1496**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7863** | 0.5850 | ±1.1701 | **+3.053** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2401 | 0.1229 | ±0.2459 | -1.953 | 0.0508 | . |
| **Education: high school or below (vs college)** | **+0.4875** | 0.2475 | ±0.4950 | **+1.970** | **0.0489** | * |
| Site: UCSD (vs UAB) | +0.1582 | 0.1633 | ±0.3267 | +0.968 | 0.3329 |  |
| Site: UW (vs UAB) | -0.0766 | 0.1596 | ±0.3192 | -0.480 | 0.6311 |  |
| Season: spring (vs autumn) | +0.0743 | 0.1747 | ±0.3493 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0582 | 0.1676 | ±0.3353 | +0.347 | 0.7285 |  |
| Season: winter (vs autumn) | +0.0277 | 0.1523 | ±0.3046 | +0.182 | 0.8557 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.221 | 0.2222 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0212 | +1.809 | 0.0704 | . |
| Hypertension | +0.1450 | 0.1424 | ±0.2847 | +1.019 | 0.3083 |  |
| High cholesterol | -0.0823 | 0.1271 | ±0.2542 | -0.648 | 0.5172 |  |
| Kidney disease | -0.0703 | 0.1927 | ±0.3854 | -0.365 | 0.7153 |  |
| Circulatory disease | -0.0139 | 0.1680 | ±0.3359 | -0.083 | 0.9339 |  |
| Avg. daily time > 180 (%) | -0.0036 | 0.0132 | ±0.0264 | -0.273 | 0.7849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1504**, Adj R² = **0.0854**, F-statistic = **2.31** (p = **0.0060**), Residual SE = **0.838** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7841** | 0.5887 | ±1.1773 | **+3.031** | **0.0024** | ** |
| Education: graduate level (vs college) | -0.2401 | 0.1225 | ±0.2451 | -1.960 | 0.0500 | . |
| **Education: high school or below (vs college)** | **+0.4970** | 0.2472 | ±0.4944 | **+2.010** | **0.0444** | * |
| Site: UCSD (vs UAB) | +0.1506 | 0.1620 | ±0.3240 | +0.930 | 0.3525 |  |
| Site: UW (vs UAB) | -0.0841 | 0.1582 | ±0.3165 | -0.531 | 0.5953 |  |
| Season: spring (vs autumn) | +0.0778 | 0.1753 | ±0.3506 | +0.444 | 0.6571 |  |
| Season: summer (vs autumn) | +0.0628 | 0.1665 | ±0.3331 | +0.377 | 0.7059 |  |
| Season: winter (vs autumn) | +0.0280 | 0.1519 | ±0.3037 | +0.184 | 0.8539 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.230 | 0.2186 |  |
| BMI (kg/m2) | +0.0196 | 0.0108 | ±0.0217 | +1.806 | 0.0709 | . |
| Hypertension | +0.1372 | 0.1419 | ±0.2837 | +0.967 | 0.3336 |  |
| High cholesterol | -0.0799 | 0.1257 | ±0.2515 | -0.635 | 0.5254 |  |
| Kidney disease | -0.0639 | 0.1923 | ±0.3847 | -0.332 | 0.7396 |  |
| Circulatory disease | -0.0107 | 0.1671 | ±0.3342 | -0.064 | 0.9491 |  |
| Nocturnal time > 180 (%) | -0.0060 | 0.0125 | ±0.0250 | -0.482 | 0.6299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.2980**, Adj R² = **0.2484**, F-statistic = **6.01** (p = **2.88e-09**), Residual SE = **2.178** on **184** df, AIC = **883.6**, BIC = **929.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6150** | 1.6023 | ±3.2046 | **+16.610** | **5.87e-62** | *** |
| Education: graduate level (vs college) | -0.2084 | 0.3448 | ±0.6897 | -0.604 | 0.5457 |  |
| Education: high school or below (vs college) | +0.2547 | 0.5604 | ±1.1207 | +0.455 | 0.6494 |  |
| Site: UCSD (vs UAB) | -0.4989 | 0.3962 | ±0.7924 | -1.259 | 0.2079 |  |
| **Site: UW (vs UAB)** | **-1.9201** | 0.4689 | ±0.9378 | **-4.095** | **4.22e-05** | *** |
| Season: spring (vs autumn) | -0.8118 | 0.4526 | ±0.9053 | -1.793 | 0.0729 | . |
| Season: summer (vs autumn) | +0.6945 | 0.5145 | ±1.0291 | +1.350 | 0.1771 |  |
| **Season: winter (vs autumn)** | **-2.3175** | 0.4997 | ±0.9994 | **-4.638** | **3.52e-06** | *** |
| Age (years) | -0.0121 | 0.0153 | ±0.0306 | -0.789 | 0.4301 |  |
| BMI (kg/m2) | +0.0001 | 0.0236 | ±0.0473 | +0.004 | 0.9967 |  |
| Hypertension | +0.4953 | 0.3824 | ±0.7648 | +1.295 | 0.1952 |  |
| High cholesterol | +0.0309 | 0.3335 | ±0.6670 | +0.093 | 0.9261 |  |
| Kidney disease | +0.1632 | 0.4678 | ±0.9355 | +0.349 | 0.7272 |  |
| Circulatory disease | +0.0199 | 0.4591 | ±0.9181 | +0.043 | 0.9654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.2985**, Adj R² = **0.2448**, F-statistic = **5.56** (p = **6.94e-09**), Residual SE = **2.183** on **183** df, AIC = **885.4**, BIC = **934.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2234** | 2.4556 | ±4.9112 | **+11.086** | **1.46e-28** | *** |
| Education: graduate level (vs college) | -0.2127 | 0.3456 | ±0.6912 | -0.615 | 0.5383 |  |
| Education: high school or below (vs college) | +0.2596 | 0.5639 | ±1.1277 | +0.460 | 0.6453 |  |
| Site: UCSD (vs UAB) | -0.5000 | 0.3981 | ±0.7962 | -1.256 | 0.2091 |  |
| **Site: UW (vs UAB)** | **-1.9221** | 0.4712 | ±0.9424 | **-4.079** | **4.52e-05** | *** |
| Season: spring (vs autumn) | -0.8153 | 0.4520 | ±0.9040 | -1.804 | 0.0713 | . |
| Season: summer (vs autumn) | +0.7084 | 0.5260 | ±1.0520 | +1.347 | 0.1780 |  |
| **Season: winter (vs autumn)** | **-2.3090** | 0.5043 | ±1.0086 | **-4.579** | **4.68e-06** | *** |
| Age (years) | -0.0120 | 0.0156 | ±0.0311 | -0.768 | 0.4422 |  |
| BMI (kg/m2) | +0.0019 | 0.0246 | ±0.0493 | +0.077 | 0.9383 |  |
| Hypertension | +0.4991 | 0.3846 | ±0.7692 | +1.298 | 0.1944 |  |
| High cholesterol | +0.0427 | 0.3412 | ±0.6823 | +0.125 | 0.9003 |  |
| Kidney disease | +0.1455 | 0.4711 | ±0.9422 | +0.309 | 0.7575 |  |
| Circulatory disease | +0.0450 | 0.4797 | ±0.9593 | +0.094 | 0.9252 |  |
| HbA1c (%) | -0.1148 | 0.3919 | ±0.7838 | -0.293 | 0.7697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.3017**, Adj R² = **0.2483**, F-statistic = **5.65** (p = **4.82e-09**), Residual SE = **2.178** on **183** df, AIC = **884.5**, BIC = **933.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.1160** | 2.1437 | ±4.2873 | **+13.116** | **2.67e-39** | *** |
| Education: graduate level (vs college) | -0.2081 | 0.3457 | ±0.6914 | -0.602 | 0.5471 |  |
| Education: high school or below (vs college) | +0.2252 | 0.5580 | ±1.1160 | +0.404 | 0.6865 |  |
| Site: UCSD (vs UAB) | -0.5016 | 0.3972 | ±0.7944 | -1.263 | 0.2066 |  |
| **Site: UW (vs UAB)** | **-1.9336** | 0.4746 | ±0.9492 | **-4.074** | **4.62e-05** | *** |
| Season: spring (vs autumn) | -0.7997 | 0.4550 | ±0.9100 | -1.758 | 0.0788 | . |
| Season: summer (vs autumn) | +0.7426 | 0.5264 | ±1.0527 | +1.411 | 0.1583 |  |
| **Season: winter (vs autumn)** | **-2.2970** | 0.5050 | ±1.0101 | **-4.548** | **5.41e-06** | *** |
| Age (years) | -0.0123 | 0.0155 | ±0.0310 | -0.795 | 0.4269 |  |
| BMI (kg/m2) | +0.0021 | 0.0240 | ±0.0479 | +0.086 | 0.9312 |  |
| Hypertension | +0.5164 | 0.3884 | ±0.7768 | +1.329 | 0.1837 |  |
| High cholesterol | +0.0185 | 0.3329 | ±0.6658 | +0.056 | 0.9557 |  |
| Kidney disease | +0.2011 | 0.4591 | ±0.9181 | +0.438 | 0.6613 |  |
| Circulatory disease | +0.0378 | 0.4603 | ±0.9206 | +0.082 | 0.9346 |  |
| Mean glucose (mg/dL) | -0.0124 | 0.0131 | ±0.0262 | -0.945 | 0.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.3017**, Adj R² = **0.2483**, F-statistic = **5.65** (p = **4.82e-09**), Residual SE = **2.178** on **183** df, AIC = **884.5**, BIC = **933.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8283** | 3.6091 | ±7.2181 | **+8.265** | **1.40e-16** | *** |
| Education: graduate level (vs college) | -0.2081 | 0.3457 | ±0.6914 | -0.602 | 0.5471 |  |
| Education: high school or below (vs college) | +0.2252 | 0.5580 | ±1.1160 | +0.404 | 0.6865 |  |
| Site: UCSD (vs UAB) | -0.5016 | 0.3972 | ±0.7944 | -1.263 | 0.2066 |  |
| **Site: UW (vs UAB)** | **-1.9336** | 0.4746 | ±0.9492 | **-4.074** | **4.62e-05** | *** |
| Season: spring (vs autumn) | -0.7997 | 0.4550 | ±0.9100 | -1.758 | 0.0788 | . |
| Season: summer (vs autumn) | +0.7426 | 0.5264 | ±1.0527 | +1.411 | 0.1583 |  |
| **Season: winter (vs autumn)** | **-2.2970** | 0.5050 | ±1.0101 | **-4.548** | **5.41e-06** | *** |
| Age (years) | -0.0123 | 0.0155 | ±0.0310 | -0.795 | 0.4269 |  |
| BMI (kg/m2) | +0.0021 | 0.0240 | ±0.0479 | +0.086 | 0.9312 |  |
| Hypertension | +0.5164 | 0.3884 | ±0.7768 | +1.329 | 0.1837 |  |
| High cholesterol | +0.0185 | 0.3329 | ±0.6658 | +0.056 | 0.9557 |  |
| Kidney disease | +0.2011 | 0.4591 | ±0.9181 | +0.438 | 0.6613 |  |
| Circulatory disease | +0.0378 | 0.4603 | ±0.9206 | +0.082 | 0.9346 |  |
| GMI (%) | -0.5173 | 0.5473 | ±1.0946 | -0.945 | 0.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.3051**, Adj R² = **0.2520**, F-statistic = **5.74** (p = **3.29e-09**), Residual SE = **2.172** on **183** df, AIC = **883.5**, BIC = **932.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5052** | 2.0048 | ±4.0095 | **+14.219** | **7.02e-46** | *** |
| Education: graduate level (vs college) | -0.1918 | 0.3459 | ±0.6917 | -0.555 | 0.5791 |  |
| Education: high school or below (vs college) | +0.2277 | 0.5616 | ±1.1233 | +0.405 | 0.6852 |  |
| Site: UCSD (vs UAB) | -0.4888 | 0.3961 | ±0.7921 | -1.234 | 0.2171 |  |
| **Site: UW (vs UAB)** | **-1.9253** | 0.4706 | ±0.9412 | **-4.091** | **4.29e-05** | *** |
| Season: spring (vs autumn) | -0.8086 | 0.4521 | ±0.9042 | -1.789 | 0.0737 | . |
| Season: summer (vs autumn) | +0.7420 | 0.5229 | ±1.0459 | +1.419 | 0.1559 |  |
| **Season: winter (vs autumn)** | **-2.3153** | 0.5024 | ±1.0048 | **-4.608** | **4.06e-06** | *** |
| Age (years) | -0.0142 | 0.0154 | ±0.0309 | -0.918 | 0.3584 |  |
| BMI (kg/m2) | +0.0037 | 0.0239 | ±0.0479 | +0.156 | 0.8757 |  |
| Hypertension | +0.5059 | 0.3898 | ±0.7796 | +1.298 | 0.1943 |  |
| High cholesterol | +0.0372 | 0.3310 | ±0.6620 | +0.113 | 0.9104 |  |
| Kidney disease | +0.1699 | 0.4560 | ±0.9120 | +0.373 | 0.7094 |  |
| Circulatory disease | +0.0596 | 0.4599 | ±0.9197 | +0.130 | 0.8969 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0151 | 0.0113 | ±0.0227 | -1.328 | 0.1840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2980**, Adj R² = **0.2443**, F-statistic = **5.55** (p = **7.31e-09**), Residual SE = **2.184** on **183** df, AIC = **885.6**, BIC = **934.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6698** | 1.8937 | ±3.7874 | **+14.083** | **4.81e-45** | *** |
| Education: graduate level (vs college) | -0.2065 | 0.3475 | ±0.6949 | -0.594 | 0.5522 |  |
| Education: high school or below (vs college) | +0.2618 | 0.5626 | ±1.1253 | +0.465 | 0.6416 |  |
| Site: UCSD (vs UAB) | -0.5015 | 0.3986 | ±0.7971 | -1.258 | 0.2083 |  |
| **Site: UW (vs UAB)** | **-1.9251** | 0.4789 | ±0.9578 | **-4.020** | **5.82e-05** | *** |
| Season: spring (vs autumn) | -0.8119 | 0.4554 | ±0.9109 | -1.783 | 0.0746 | . |
| Season: summer (vs autumn) | +0.6942 | 0.5169 | ±1.0338 | +1.343 | 0.1792 |  |
| **Season: winter (vs autumn)** | **-2.3176** | 0.5022 | ±1.0043 | **-4.615** | **3.93e-06** | *** |
| Age (years) | -0.0120 | 0.0151 | ±0.0302 | -0.792 | 0.4283 |  |
| BMI (kg/m2) | +0.0001 | 0.0239 | ±0.0477 | +0.003 | 0.9977 |  |
| Hypertension | +0.5000 | 0.3906 | ±0.7812 | +1.280 | 0.2005 |  |
| High cholesterol | +0.0290 | 0.3325 | ±0.6650 | +0.087 | 0.9304 |  |
| Kidney disease | +0.1689 | 0.4752 | ±0.9505 | +0.355 | 0.7223 |  |
| Circulatory disease | +0.0219 | 0.4629 | ±0.9258 | +0.047 | 0.9622 |  |
| Glucose SD, pooled (mg/dL) | -0.0028 | 0.0355 | ±0.0709 | -0.080 | 0.9362 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2982**, Adj R² = **0.2445**, F-statistic = **5.55** (p = **7.17e-09**), Residual SE = **2.183** on **183** df, AIC = **885.5**, BIC = **934.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.4724** | 1.8634 | ±3.7268 | **+14.206** | **8.36e-46** | *** |
| Education: graduate level (vs college) | -0.2127 | 0.3465 | ±0.6930 | -0.614 | 0.5393 |  |
| Education: high school or below (vs college) | +0.2381 | 0.5614 | ±1.1229 | +0.424 | 0.6716 |  |
| Site: UCSD (vs UAB) | -0.4964 | 0.3974 | ±0.7948 | -1.249 | 0.2116 |  |
| **Site: UW (vs UAB)** | **-1.9101** | 0.4755 | ±0.9511 | **-4.017** | **5.90e-05** | *** |
| Season: spring (vs autumn) | -0.8086 | 0.4577 | ±0.9154 | -1.767 | 0.0773 | . |
| Season: summer (vs autumn) | +0.6983 | 0.5188 | ±1.0377 | +1.346 | 0.1783 |  |
| **Season: winter (vs autumn)** | **-2.3155** | 0.5040 | ±1.0081 | **-4.594** | **4.35e-06** | *** |
| Age (years) | -0.0124 | 0.0151 | ±0.0303 | -0.818 | 0.4134 |  |
| BMI (kg/m2) | +0.0002 | 0.0238 | ±0.0476 | +0.008 | 0.9940 |  |
| Hypertension | +0.4790 | 0.3884 | ±0.7768 | +1.233 | 0.2175 |  |
| High cholesterol | +0.0366 | 0.3328 | ±0.6655 | +0.110 | 0.9124 |  |
| Kidney disease | +0.1516 | 0.4741 | ±0.9482 | +0.320 | 0.7492 |  |
| Circulatory disease | +0.0181 | 0.4627 | ±0.9253 | +0.039 | 0.9687 |  |
| Avg. daily SD (mg/dL) | +0.0082 | 0.0352 | ±0.0703 | +0.233 | 0.8161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.2991**, Adj R² = **0.2454**, F-statistic = **5.58** (p = **6.48e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.1569** | 2.0819 | ±4.1637 | **+12.564** | **3.32e-36** | *** |
| Education: graduate level (vs college) | -0.2222 | 0.3445 | ±0.6891 | -0.645 | 0.5190 |  |
| Education: high school or below (vs college) | +0.1859 | 0.5684 | ±1.1368 | +0.327 | 0.7436 |  |
| Site: UCSD (vs UAB) | -0.4788 | 0.3965 | ±0.7930 | -1.208 | 0.2272 |  |
| **Site: UW (vs UAB)** | **-1.8839** | 0.4738 | ±0.9476 | **-3.976** | **7.00e-05** | *** |
| Season: spring (vs autumn) | -0.8075 | 0.4574 | ±0.9148 | -1.765 | 0.0775 | . |
| Season: summer (vs autumn) | +0.7119 | 0.5226 | ±1.0453 | +1.362 | 0.1732 |  |
| **Season: winter (vs autumn)** | **-2.3127** | 0.5050 | ±1.0100 | **-4.580** | **4.65e-06** | *** |
| Age (years) | -0.0130 | 0.0150 | ±0.0301 | -0.865 | 0.3872 |  |
| BMI (kg/m2) | +0.0009 | 0.0241 | ±0.0481 | +0.038 | 0.9697 |  |
| Hypertension | +0.4644 | 0.3932 | ±0.7864 | +1.181 | 0.2375 |  |
| High cholesterol | +0.0423 | 0.3329 | ±0.6657 | +0.127 | 0.8989 |  |
| Kidney disease | +0.1278 | 0.4796 | ±0.9592 | +0.266 | 0.7899 |  |
| Circulatory disease | +0.0113 | 0.4633 | ±0.9267 | +0.024 | 0.9806 |  |
| CV (%) | +0.0289 | 0.0583 | ±0.1166 | +0.496 | 0.6197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.2987**, Adj R² = **0.2451**, F-statistic = **5.57** (p = **6.75e-09**), Residual SE = **2.182** on **183** df, AIC = **885.4**, BIC = **934.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0366** | 1.6536 | ±3.3071 | **+16.351** | **4.30e-60** | *** |
| Education: graduate level (vs college) | -0.2175 | 0.3442 | ±0.6883 | -0.632 | 0.5274 |  |
| Education: high school or below (vs college) | +0.2051 | 0.5637 | ±1.1274 | +0.364 | 0.7160 |  |
| Site: UCSD (vs UAB) | -0.4863 | 0.3974 | ±0.7949 | -1.224 | 0.2211 |  |
| **Site: UW (vs UAB)** | **-1.8942** | 0.4702 | ±0.9403 | **-4.029** | **5.60e-05** | *** |
| Season: spring (vs autumn) | -0.8086 | 0.4588 | ±0.9176 | -1.763 | 0.0780 | . |
| Season: summer (vs autumn) | +0.7072 | 0.5252 | ±1.0504 | +1.346 | 0.1781 |  |
| **Season: winter (vs autumn)** | **-2.3151** | 0.5055 | ±1.0110 | **-4.580** | **4.65e-06** | *** |
| Age (years) | -0.0129 | 0.0150 | ±0.0300 | -0.856 | 0.3920 |  |
| BMI (kg/m2) | +0.0003 | 0.0240 | ±0.0479 | +0.014 | 0.9891 |  |
| Hypertension | +0.4687 | 0.3903 | ±0.7806 | +1.201 | 0.2298 |  |
| High cholesterol | +0.0370 | 0.3342 | ±0.6683 | +0.111 | 0.9118 |  |
| Kidney disease | +0.1354 | 0.4813 | ±0.9627 | +0.281 | 0.7785 |  |
| Circulatory disease | +0.0171 | 0.4645 | ±0.9290 | +0.037 | 0.9707 |  |
| Mean / SD ratio | -0.0615 | 0.1747 | ±0.3494 | -0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2995**, Adj R² = **0.2459**, F-statistic = **5.59** (p = **6.20e-09**), Residual SE = **2.181** on **183** df, AIC = **885.1**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.1629** | 1.6414 | ±3.2828 | **+16.549** | **1.63e-61** | *** |
| Education: graduate level (vs college) | -0.2150 | 0.3455 | ±0.6911 | -0.622 | 0.5338 |  |
| Education: high school or below (vs college) | +0.2002 | 0.5621 | ±1.1241 | +0.356 | 0.7217 |  |
| Site: UCSD (vs UAB) | -0.5008 | 0.3957 | ±0.7915 | -1.265 | 0.2057 |  |
| **Site: UW (vs UAB)** | **-1.8946** | 0.4682 | ±0.9364 | **-4.047** | **5.19e-05** | *** |
| Season: spring (vs autumn) | -0.8039 | 0.4616 | ±0.9233 | -1.741 | 0.0816 | . |
| Season: summer (vs autumn) | +0.7175 | 0.5310 | ±1.0620 | +1.351 | 0.1766 |  |
| **Season: winter (vs autumn)** | **-2.3053** | 0.5123 | ±1.0247 | **-4.499** | **6.81e-06** | *** |
| Age (years) | -0.0133 | 0.0150 | ±0.0301 | -0.882 | 0.3779 |  |
| BMI (kg/m2) | +0.0003 | 0.0239 | ±0.0479 | +0.012 | 0.9905 |  |
| Hypertension | +0.4451 | 0.3903 | ±0.7806 | +1.140 | 0.2542 |  |
| High cholesterol | +0.0349 | 0.3351 | ±0.6701 | +0.104 | 0.9169 |  |
| Kidney disease | +0.1351 | 0.4775 | ±0.9550 | +0.283 | 0.7772 |  |
| Circulatory disease | +0.0337 | 0.4687 | ±0.9373 | +0.072 | 0.9426 |  |
| Avg. daily mean/SD | -0.0671 | 0.1461 | ±0.2922 | -0.459 | 0.6461 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.2991**, Adj R² = **0.2455**, F-statistic = **5.58** (p = **6.46e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0861** | 2.1094 | ±4.2188 | **+12.841** | **9.72e-38** | *** |
| Education: graduate level (vs college) | -0.2050 | 0.3473 | ±0.6947 | -0.590 | 0.5551 |  |
| Education: high school or below (vs college) | +0.2771 | 0.5659 | ±1.1317 | +0.490 | 0.6243 |  |
| Site: UCSD (vs UAB) | -0.4981 | 0.3974 | ±0.7947 | -1.254 | 0.2100 |  |
| **Site: UW (vs UAB)** | **-1.9319** | 0.4695 | ±0.9390 | **-4.115** | **3.88e-05** | *** |
| Season: spring (vs autumn) | -0.8155 | 0.4578 | ±0.9156 | -1.782 | 0.0748 | . |
| Season: summer (vs autumn) | +0.6911 | 0.5196 | ±1.0392 | +1.330 | 0.1835 |  |
| **Season: winter (vs autumn)** | **-2.3233** | 0.5043 | ±1.0086 | **-4.607** | **4.08e-06** | *** |
| Age (years) | -0.0123 | 0.0154 | ±0.0307 | -0.801 | 0.4231 |  |
| BMI (kg/m2) | +0.0005 | 0.0236 | ±0.0473 | +0.023 | 0.9819 |  |
| Hypertension | +0.5072 | 0.3832 | ±0.7664 | +1.324 | 0.1856 |  |
| High cholesterol | +0.0388 | 0.3372 | ±0.6745 | +0.115 | 0.9085 |  |
| Kidney disease | +0.1619 | 0.4657 | ±0.9314 | +0.348 | 0.7280 |  |
| Circulatory disease | +0.0049 | 0.4626 | ±0.9251 | +0.011 | 0.9915 |  |
| MAG (mg/dL/h) | -0.0132 | 0.0271 | ±0.0541 | -0.486 | 0.6267 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.2980**, Adj R² = **0.2443**, F-statistic = **5.55** (p = **7.33e-09**), Residual SE = **2.184** on **183** df, AIC = **885.6**, BIC = **934.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6091** | 2.0042 | ±4.0083 | **+13.277** | **3.15e-40** | *** |
| Education: graduate level (vs college) | -0.2084 | 0.3469 | ±0.6938 | -0.601 | 0.5480 |  |
| Education: high school or below (vs college) | +0.2543 | 0.5640 | ±1.1280 | +0.451 | 0.6521 |  |
| Site: UCSD (vs UAB) | -0.4988 | 0.3978 | ±0.7956 | -1.254 | 0.2099 |  |
| **Site: UW (vs UAB)** | **-1.9198** | 0.4747 | ±0.9494 | **-4.044** | **5.25e-05** | *** |
| Season: spring (vs autumn) | -0.8117 | 0.4568 | ±0.9136 | -1.777 | 0.0756 | . |
| Season: summer (vs autumn) | +0.6947 | 0.5204 | ±1.0409 | +1.335 | 0.1819 |  |
| **Season: winter (vs autumn)** | **-2.3174** | 0.5052 | ±1.0104 | **-4.587** | **4.49e-06** | *** |
| Age (years) | -0.0121 | 0.0151 | ±0.0302 | -0.802 | 0.4227 |  |
| BMI (kg/m2) | +0.0001 | 0.0242 | ±0.0484 | +0.004 | 0.9965 |  |
| Hypertension | +0.4950 | 0.3846 | ±0.7693 | +1.287 | 0.1982 |  |
| High cholesterol | +0.0310 | 0.3339 | ±0.6678 | +0.093 | 0.9260 |  |
| Kidney disease | +0.1629 | 0.4709 | ±0.9418 | +0.346 | 0.7293 |  |
| Circulatory disease | +0.0199 | 0.4614 | ±0.9228 | +0.043 | 0.9656 |  |
| Avg. daily range (mg/dL) | +0.0001 | 0.0088 | ±0.0176 | +0.007 | 0.9941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.3067**, Adj R² = **0.2537**, F-statistic = **5.78** (p = **2.75e-09**), Residual SE = **2.170** on **183** df, AIC = **883.1**, BIC = **932.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2280** | 1.6562 | ±3.3123 | **+16.440** | **9.82e-61** | *** |
| Education: graduate level (vs college) | -0.1791 | 0.3435 | ±0.6870 | -0.521 | 0.6020 |  |
| Education: high school or below (vs college) | +0.3905 | 0.5661 | ±1.1322 | +0.690 | 0.4904 |  |
| Site: UCSD (vs UAB) | -0.6040 | 0.3999 | ±0.7998 | -1.510 | 0.1310 |  |
| **Site: UW (vs UAB)** | **-2.0407** | 0.4731 | ±0.9461 | **-4.314** | **1.61e-05** | *** |
| Season: spring (vs autumn) | -0.7646 | 0.4474 | ±0.8948 | -1.709 | 0.0874 | . |
| Season: summer (vs autumn) | +0.7883 | 0.5229 | ±1.0457 | +1.508 | 0.1316 |  |
| **Season: winter (vs autumn)** | **-2.3117** | 0.4971 | ±0.9942 | **-4.650** | **3.32e-06** | *** |
| Age (years) | -0.0115 | 0.0150 | ±0.0299 | -0.767 | 0.4432 |  |
| BMI (kg/m2) | +0.0004 | 0.0237 | ±0.0475 | +0.017 | 0.9864 |  |
| Hypertension | +0.4534 | 0.3786 | ±0.7572 | +1.198 | 0.2311 |  |
| High cholesterol | +0.0459 | 0.3355 | ±0.6710 | +0.137 | 0.8911 |  |
| Kidney disease | +0.2951 | 0.4803 | ±0.9606 | +0.614 | 0.5389 |  |
| Circulatory disease | +0.1585 | 0.4723 | ±0.9445 | +0.336 | 0.7372 |  |
| SD of daily means (mg/dL) | -0.1016 | 0.0723 | ±0.1447 | -1.404 | 0.1602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.2993**, Adj R² = **0.2457**, F-statistic = **5.58** (p = **6.32e-09**), Residual SE = **2.182** on **183** df, AIC = **885.2**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5796** | 3.7379 | ±7.4758 | **+6.576** | **4.84e-11** | *** |
| Education: graduate level (vs college) | -0.1962 | 0.3492 | ±0.6983 | -0.562 | 0.5741 |  |
| Education: high school or below (vs college) | +0.2804 | 0.5621 | ±1.1242 | +0.499 | 0.6179 |  |
| Site: UCSD (vs UAB) | -0.5171 | 0.3989 | ±0.7979 | -1.296 | 0.1949 |  |
| **Site: UW (vs UAB)** | **-1.9388** | 0.4775 | ±0.9549 | **-4.061** | **4.89e-05** | *** |
| Season: spring (vs autumn) | -0.8140 | 0.4530 | ±0.9061 | -1.797 | 0.0724 | . |
| Season: summer (vs autumn) | +0.7092 | 0.5164 | ±1.0328 | +1.373 | 0.1697 |  |
| **Season: winter (vs autumn)** | **-2.3094** | 0.5006 | ±1.0011 | **-4.614** | **3.96e-06** | *** |
| Age (years) | -0.0111 | 0.0155 | ±0.0309 | -0.715 | 0.4745 |  |
| BMI (kg/m2) | +0.0004 | 0.0238 | ±0.0476 | +0.017 | 0.9861 |  |
| Hypertension | +0.5069 | 0.3876 | ±0.7751 | +1.308 | 0.1909 |  |
| High cholesterol | +0.0189 | 0.3323 | ±0.6647 | +0.057 | 0.9547 |  |
| Kidney disease | +0.2047 | 0.4616 | ±0.9232 | +0.443 | 0.6574 |  |
| Circulatory disease | +0.0314 | 0.4604 | ±0.9207 | +0.068 | 0.9457 |  |
| Time in range 70-180, pooled (%) | +0.0204 | 0.0342 | ±0.0683 | +0.596 | 0.5511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.2995**, Adj R² = **0.2459**, F-statistic = **5.59** (p = **6.19e-09**), Residual SE = **2.181** on **183** df, AIC = **885.1**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3922** | 3.8625 | ±7.7249 | **+6.315** | **2.70e-10** | *** |
| Education: graduate level (vs college) | -0.1967 | 0.3487 | ±0.6975 | -0.564 | 0.5727 |  |
| Education: high school or below (vs college) | +0.2776 | 0.5605 | ±1.1209 | +0.495 | 0.6204 |  |
| Site: UCSD (vs UAB) | -0.5184 | 0.3989 | ±0.7979 | -1.299 | 0.1938 |  |
| **Site: UW (vs UAB)** | **-1.9363** | 0.4768 | ±0.9536 | **-4.061** | **4.88e-05** | *** |
| Season: spring (vs autumn) | -0.8154 | 0.4529 | ±0.9058 | -1.800 | 0.0718 | . |
| Season: summer (vs autumn) | +0.7109 | 0.5161 | ±1.0322 | +1.378 | 0.1683 |  |
| **Season: winter (vs autumn)** | **-2.3083** | 0.5004 | ±1.0008 | **-4.613** | **3.97e-06** | *** |
| Age (years) | -0.0109 | 0.0154 | ±0.0309 | -0.709 | 0.4785 |  |
| BMI (kg/m2) | +0.0003 | 0.0238 | ±0.0476 | +0.013 | 0.9899 |  |
| Hypertension | +0.5108 | 0.3878 | ±0.7756 | +1.317 | 0.1878 |  |
| High cholesterol | +0.0189 | 0.3321 | ±0.6642 | +0.057 | 0.9546 |  |
| Kidney disease | +0.2085 | 0.4605 | ±0.9211 | +0.453 | 0.6507 |  |
| Circulatory disease | +0.0317 | 0.4603 | ±0.9207 | +0.069 | 0.9452 |  |
| Avg. daily time in range 70-180 (%) | +0.0222 | 0.0357 | ±0.0715 | +0.622 | 0.5340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.3035**, Adj R² = **0.2502**, F-statistic = **5.69** (p = **3.97e-09**), Residual SE = **2.175** on **183** df, AIC = **884.0**, BIC = **933.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5634** | 1.5946 | ±3.1891 | **+16.659** | **2.61e-62** | *** |
| Education: graduate level (vs college) | -0.1820 | 0.3449 | ±0.6898 | -0.528 | 0.5977 |  |
| Education: high school or below (vs college) | +0.3393 | 0.5618 | ±1.1235 | +0.604 | 0.5458 |  |
| Site: UCSD (vs UAB) | -0.5329 | 0.3951 | ±0.7903 | -1.349 | 0.1775 |  |
| **Site: UW (vs UAB)** | **-1.9298** | 0.4703 | ±0.9406 | **-4.103** | **4.07e-05** | *** |
| Season: spring (vs autumn) | -0.8633 | 0.4635 | ±0.9270 | -1.863 | 0.0625 | . |
| Season: summer (vs autumn) | +0.6650 | 0.5169 | ±1.0338 | +1.286 | 0.1983 |  |
| **Season: winter (vs autumn)** | **-2.3751** | 0.5073 | ±1.0146 | **-4.682** | **2.84e-06** | *** |
| Age (years) | -0.0090 | 0.0151 | ±0.0301 | -0.599 | 0.5494 |  |
| BMI (kg/m2) | -0.0014 | 0.0237 | ±0.0475 | -0.060 | 0.9519 |  |
| Hypertension | +0.5134 | 0.3829 | ±0.7657 | +1.341 | 0.1800 |  |
| High cholesterol | +0.0557 | 0.3376 | ±0.6752 | +0.165 | 0.8689 |  |
| Kidney disease | +0.1344 | 0.4663 | ±0.9327 | +0.288 | 0.7733 |  |
| Circulatory disease | +0.0231 | 0.4609 | ±0.9218 | +0.050 | 0.9601 |  |
| Time 54-69, pooled (%) | -0.7097 | 0.5364 | ±1.0727 | -1.323 | 0.1858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.3007**, Adj R² = **0.2472**, F-statistic = **5.62** (p = **5.38e-09**), Residual SE = **2.179** on **183** df, AIC = **884.8**, BIC = **934.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5572** | 1.5939 | ±3.1878 | **+16.662** | **2.50e-62** | *** |
| Education: graduate level (vs college) | -0.1903 | 0.3449 | ±0.6898 | -0.552 | 0.5812 |  |
| Education: high school or below (vs college) | +0.3126 | 0.5616 | ±1.1231 | +0.557 | 0.5777 |  |
| Site: UCSD (vs UAB) | -0.5114 | 0.3963 | ±0.7925 | -1.291 | 0.1969 |  |
| **Site: UW (vs UAB)** | **-1.9178** | 0.4709 | ±0.9417 | **-4.073** | **4.64e-05** | *** |
| Season: spring (vs autumn) | -0.8488 | 0.4660 | ±0.9321 | -1.821 | 0.0686 | . |
| Season: summer (vs autumn) | +0.6612 | 0.5209 | ±1.0417 | +1.269 | 0.2043 |  |
| **Season: winter (vs autumn)** | **-2.3565** | 0.5092 | ±1.0184 | **-4.628** | **3.70e-06** | *** |
| Age (years) | -0.0098 | 0.0151 | ±0.0303 | -0.646 | 0.5186 |  |
| BMI (kg/m2) | -0.0009 | 0.0238 | ±0.0475 | -0.039 | 0.9692 |  |
| Hypertension | +0.5149 | 0.3856 | ±0.7713 | +1.335 | 0.1818 |  |
| High cholesterol | +0.0484 | 0.3386 | ±0.6773 | +0.143 | 0.8864 |  |
| Kidney disease | +0.1349 | 0.4688 | ±0.9375 | +0.288 | 0.7735 |  |
| Circulatory disease | +0.0100 | 0.4612 | ±0.9224 | +0.022 | 0.9827 |  |
| Avg. daily time 54-69 (%) | -0.4909 | 0.5074 | ±1.0147 | -0.967 | 0.3333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.3035**, Adj R² = **0.2502**, F-statistic = **5.69** (p = **3.97e-09**), Residual SE = **2.175** on **183** df, AIC = **884.0**, BIC = **933.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5634** | 1.5946 | ±3.1891 | **+16.659** | **2.61e-62** | *** |
| Education: graduate level (vs college) | -0.1820 | 0.3449 | ±0.6898 | -0.528 | 0.5977 |  |
| Education: high school or below (vs college) | +0.3393 | 0.5618 | ±1.1235 | +0.604 | 0.5458 |  |
| Site: UCSD (vs UAB) | -0.5329 | 0.3951 | ±0.7903 | -1.349 | 0.1775 |  |
| **Site: UW (vs UAB)** | **-1.9298** | 0.4703 | ±0.9406 | **-4.103** | **4.07e-05** | *** |
| Season: spring (vs autumn) | -0.8633 | 0.4635 | ±0.9270 | -1.863 | 0.0625 | . |
| Season: summer (vs autumn) | +0.6650 | 0.5169 | ±1.0338 | +1.286 | 0.1983 |  |
| **Season: winter (vs autumn)** | **-2.3751** | 0.5073 | ±1.0146 | **-4.682** | **2.84e-06** | *** |
| Age (years) | -0.0090 | 0.0151 | ±0.0301 | -0.599 | 0.5494 |  |
| BMI (kg/m2) | -0.0014 | 0.0237 | ±0.0475 | -0.060 | 0.9519 |  |
| Hypertension | +0.5134 | 0.3829 | ±0.7657 | +1.341 | 0.1800 |  |
| High cholesterol | +0.0557 | 0.3376 | ±0.6752 | +0.165 | 0.8689 |  |
| Kidney disease | +0.1344 | 0.4663 | ±0.9327 | +0.288 | 0.7733 |  |
| Circulatory disease | +0.0231 | 0.4609 | ±0.9218 | +0.050 | 0.9601 |  |
| Time < 70 (%) | -0.7097 | 0.5364 | ±1.0727 | -1.323 | 0.1858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.3007**, Adj R² = **0.2472**, F-statistic = **5.62** (p = **5.38e-09**), Residual SE = **2.179** on **183** df, AIC = **884.8**, BIC = **934.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5572** | 1.5939 | ±3.1878 | **+16.662** | **2.50e-62** | *** |
| Education: graduate level (vs college) | -0.1903 | 0.3449 | ±0.6898 | -0.552 | 0.5812 |  |
| Education: high school or below (vs college) | +0.3126 | 0.5616 | ±1.1231 | +0.557 | 0.5777 |  |
| Site: UCSD (vs UAB) | -0.5114 | 0.3963 | ±0.7925 | -1.291 | 0.1969 |  |
| **Site: UW (vs UAB)** | **-1.9178** | 0.4709 | ±0.9417 | **-4.073** | **4.64e-05** | *** |
| Season: spring (vs autumn) | -0.8488 | 0.4660 | ±0.9321 | -1.821 | 0.0686 | . |
| Season: summer (vs autumn) | +0.6612 | 0.5209 | ±1.0417 | +1.269 | 0.2043 |  |
| **Season: winter (vs autumn)** | **-2.3565** | 0.5092 | ±1.0184 | **-4.628** | **3.70e-06** | *** |
| Age (years) | -0.0098 | 0.0151 | ±0.0303 | -0.646 | 0.5186 |  |
| BMI (kg/m2) | -0.0009 | 0.0238 | ±0.0475 | -0.039 | 0.9692 |  |
| Hypertension | +0.5149 | 0.3856 | ±0.7713 | +1.335 | 0.1818 |  |
| High cholesterol | +0.0484 | 0.3386 | ±0.6773 | +0.143 | 0.8864 |  |
| Kidney disease | +0.1349 | 0.4688 | ±0.9375 | +0.288 | 0.7735 |  |
| Circulatory disease | +0.0100 | 0.4612 | ±0.9224 | +0.022 | 0.9827 |  |
| Avg. daily time < 70 (%) | -0.4909 | 0.5074 | ±1.0147 | -0.967 | 0.3333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.2990**, Adj R² = **0.2454**, F-statistic = **5.58** (p = **6.54e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6176** | 1.6134 | ±3.2268 | **+16.498** | **3.79e-61** | *** |
| Education: graduate level (vs college) | -0.1985 | 0.3489 | ±0.6978 | -0.569 | 0.5695 |  |
| Education: high school or below (vs college) | +0.2749 | 0.5623 | ±1.1245 | +0.489 | 0.6248 |  |
| Site: UCSD (vs UAB) | -0.5139 | 0.3988 | ±0.7976 | -1.289 | 0.1976 |  |
| **Site: UW (vs UAB)** | **-1.9361** | 0.4773 | ±0.9547 | **-4.056** | **4.99e-05** | *** |
| Season: spring (vs autumn) | -0.8124 | 0.4531 | ±0.9062 | -1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +0.7080 | 0.5168 | ±1.0336 | +1.370 | 0.1707 |  |
| **Season: winter (vs autumn)** | **-2.3090** | 0.5008 | ±1.0016 | **-4.610** | **4.02e-06** | *** |
| Age (years) | -0.0113 | 0.0154 | ±0.0309 | -0.729 | 0.4660 |  |
| BMI (kg/m2) | +0.0004 | 0.0238 | ±0.0476 | +0.017 | 0.9862 |  |
| Hypertension | +0.5050 | 0.3871 | ±0.7742 | +1.305 | 0.1920 |  |
| High cholesterol | +0.0198 | 0.3326 | ±0.6653 | +0.060 | 0.9525 |  |
| Kidney disease | +0.2000 | 0.4632 | ±0.9265 | +0.432 | 0.6659 |  |
| Circulatory disease | +0.0298 | 0.4607 | ±0.9214 | +0.065 | 0.9484 |  |
| Time 181-250, pooled (%) | -0.0177 | 0.0336 | ±0.0673 | -0.527 | 0.5985 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.2992**, Adj R² = **0.2456**, F-statistic = **5.58** (p = **6.37e-09**), Residual SE = **2.182** on **183** df, AIC = **885.2**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6173** | 1.6129 | ±3.2258 | **+16.503** | **3.51e-61** | *** |
| Education: graduate level (vs college) | -0.1986 | 0.3485 | ±0.6971 | -0.570 | 0.5688 |  |
| Education: high school or below (vs college) | +0.2730 | 0.5608 | ±1.1216 | +0.487 | 0.6264 |  |
| Site: UCSD (vs UAB) | -0.5159 | 0.3989 | ±0.7978 | -1.293 | 0.1959 |  |
| **Site: UW (vs UAB)** | **-1.9348** | 0.4768 | ±0.9536 | **-4.058** | **4.95e-05** | *** |
| Season: spring (vs autumn) | -0.8135 | 0.4528 | ±0.9057 | -1.796 | 0.0724 | . |
| Season: summer (vs autumn) | +0.7107 | 0.5165 | ±1.0330 | +1.376 | 0.1688 |  |
| **Season: winter (vs autumn)** | **-2.3076** | 0.5006 | ±1.0012 | **-4.610** | **4.03e-06** | *** |
| Age (years) | -0.0112 | 0.0154 | ±0.0309 | -0.722 | 0.4702 |  |
| BMI (kg/m2) | +0.0003 | 0.0238 | ±0.0476 | +0.014 | 0.9892 |  |
| Hypertension | +0.5085 | 0.3873 | ±0.7746 | +1.313 | 0.1892 |  |
| High cholesterol | +0.0194 | 0.3324 | ±0.6647 | +0.058 | 0.9535 |  |
| Kidney disease | +0.2052 | 0.4620 | ±0.9241 | +0.444 | 0.6570 |  |
| Circulatory disease | +0.0309 | 0.4607 | ±0.9214 | +0.067 | 0.9465 |  |
| Avg. daily time 181-250 (%) | -0.0200 | 0.0352 | ±0.0704 | -0.569 | 0.5694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.2990**, Adj R² = **0.2454**, F-statistic = **5.58** (p = **6.54e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6176** | 1.6134 | ±3.2268 | **+16.498** | **3.79e-61** | *** |
| Education: graduate level (vs college) | -0.1985 | 0.3489 | ±0.6978 | -0.569 | 0.5695 |  |
| Education: high school or below (vs college) | +0.2749 | 0.5623 | ±1.1245 | +0.489 | 0.6248 |  |
| Site: UCSD (vs UAB) | -0.5139 | 0.3988 | ±0.7976 | -1.289 | 0.1976 |  |
| **Site: UW (vs UAB)** | **-1.9361** | 0.4773 | ±0.9547 | **-4.056** | **4.99e-05** | *** |
| Season: spring (vs autumn) | -0.8124 | 0.4531 | ±0.9062 | -1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +0.7080 | 0.5168 | ±1.0336 | +1.370 | 0.1707 |  |
| **Season: winter (vs autumn)** | **-2.3090** | 0.5008 | ±1.0016 | **-4.610** | **4.02e-06** | *** |
| Age (years) | -0.0113 | 0.0154 | ±0.0309 | -0.729 | 0.4660 |  |
| BMI (kg/m2) | +0.0004 | 0.0238 | ±0.0476 | +0.017 | 0.9862 |  |
| Hypertension | +0.5050 | 0.3871 | ±0.7742 | +1.305 | 0.1920 |  |
| High cholesterol | +0.0198 | 0.3326 | ±0.6653 | +0.060 | 0.9525 |  |
| Kidney disease | +0.2000 | 0.4632 | ±0.9265 | +0.432 | 0.6659 |  |
| Circulatory disease | +0.0298 | 0.4607 | ±0.9214 | +0.065 | 0.9484 |  |
| Time > 180 (%) | -0.0177 | 0.0336 | ±0.0673 | -0.527 | 0.5985 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.2992**, Adj R² = **0.2456**, F-statistic = **5.58** (p = **6.37e-09**), Residual SE = **2.182** on **183** df, AIC = **885.2**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6173** | 1.6129 | ±3.2258 | **+16.503** | **3.51e-61** | *** |
| Education: graduate level (vs college) | -0.1986 | 0.3485 | ±0.6971 | -0.570 | 0.5688 |  |
| Education: high school or below (vs college) | +0.2730 | 0.5608 | ±1.1216 | +0.487 | 0.6264 |  |
| Site: UCSD (vs UAB) | -0.5159 | 0.3989 | ±0.7978 | -1.293 | 0.1959 |  |
| **Site: UW (vs UAB)** | **-1.9348** | 0.4768 | ±0.9536 | **-4.058** | **4.95e-05** | *** |
| Season: spring (vs autumn) | -0.8135 | 0.4528 | ±0.9057 | -1.796 | 0.0724 | . |
| Season: summer (vs autumn) | +0.7107 | 0.5165 | ±1.0330 | +1.376 | 0.1688 |  |
| **Season: winter (vs autumn)** | **-2.3076** | 0.5006 | ±1.0012 | **-4.610** | **4.03e-06** | *** |
| Age (years) | -0.0112 | 0.0154 | ±0.0309 | -0.722 | 0.4702 |  |
| BMI (kg/m2) | +0.0003 | 0.0238 | ±0.0476 | +0.014 | 0.9892 |  |
| Hypertension | +0.5085 | 0.3873 | ±0.7746 | +1.313 | 0.1892 |  |
| High cholesterol | +0.0194 | 0.3324 | ±0.6647 | +0.058 | 0.9535 |  |
| Kidney disease | +0.2052 | 0.4620 | ±0.9241 | +0.444 | 0.6570 |  |
| Circulatory disease | +0.0309 | 0.4607 | ±0.9214 | +0.067 | 0.9465 |  |
| Avg. daily time > 180 (%) | -0.0200 | 0.0352 | ±0.0704 | -0.569 | 0.5694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.3017**, Adj R² = **0.2482**, F-statistic = **5.65** (p = **4.86e-09**), Residual SE = **2.178** on **183** df, AIC = **884.5**, BIC = **933.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6055** | 1.6189 | ±3.2378 | **+16.434** | **1.09e-60** | *** |
| Education: graduate level (vs college) | -0.1992 | 0.3446 | ±0.6892 | -0.578 | 0.5633 |  |
| Education: high school or below (vs college) | +0.3216 | 0.5594 | ±1.1188 | +0.575 | 0.5653 |  |
| Site: UCSD (vs UAB) | -0.5544 | 0.4000 | ±0.8000 | -1.386 | 0.1657 |  |
| **Site: UW (vs UAB)** | **-1.9728** | 0.4743 | ±0.9487 | **-4.159** | **3.20e-05** | *** |
| Season: spring (vs autumn) | -0.7949 | 0.4518 | ±0.9037 | -1.759 | 0.0785 | . |
| Season: summer (vs autumn) | +0.7341 | 0.5172 | ±1.0344 | +1.419 | 0.1558 |  |
| **Season: winter (vs autumn)** | **-2.3068** | 0.4990 | ±0.9981 | **-4.623** | **3.79e-06** | *** |
| Age (years) | -0.0115 | 0.0155 | ±0.0309 | -0.743 | 0.4577 |  |
| BMI (kg/m2) | +0.0021 | 0.0238 | ±0.0477 | +0.090 | 0.9282 |  |
| Hypertension | +0.4666 | 0.3852 | ±0.7704 | +1.211 | 0.2258 |  |
| High cholesterol | +0.0330 | 0.3334 | ±0.6668 | +0.099 | 0.9213 |  |
| Kidney disease | +0.2361 | 0.4606 | ±0.9212 | +0.513 | 0.6083 |  |
| Circulatory disease | +0.0473 | 0.4595 | ±0.9189 | +0.103 | 0.9179 |  |
| Nocturnal time > 180 (%) | -0.0316 | 0.0374 | ±0.0748 | -0.845 | 0.3982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.2033**, Adj R² = **0.1471**, F-statistic = **3.61** (p = **4.41e-05**), Residual SE = **6.052** on **184** df, AIC = **1288.3**, BIC = **1334.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5249** | 4.4140 | ±8.8279 | **+10.540** | **5.63e-26** | *** |
| Education: graduate level (vs college) | +0.8800 | 0.9510 | ±1.9019 | +0.925 | 0.3548 |  |
| Education: high school or below (vs college) | +1.9575 | 1.5702 | ±3.1404 | +1.247 | 0.2125 |  |
| **Site: UCSD (vs UAB)** | **+3.3000** | 1.1410 | ±2.2820 | **+2.892** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.1772 | 1.1973 | ±2.3947 | -0.148 | 0.8824 |  |
| Season: spring (vs autumn) | -1.6612 | 1.3032 | ±2.6065 | -1.275 | 0.2024 |  |
| Season: summer (vs autumn) | +0.9150 | 1.3015 | ±2.6031 | +0.703 | 0.4820 |  |
| **Season: winter (vs autumn)** | **-5.0494** | 1.4693 | ±2.9386 | **-3.437** | **5.89e-04** | *** |
| Age (years) | +0.0296 | 0.0485 | ±0.0969 | +0.611 | 0.5410 |  |
| BMI (kg/m2) | -0.0545 | 0.0619 | ±0.1239 | -0.880 | 0.3788 |  |
| Hypertension | +0.3463 | 1.0546 | ±2.1091 | +0.328 | 0.7426 |  |
| **High cholesterol** | **-2.0735** | 0.9908 | ±1.9816 | **-2.093** | **0.0364** | * |
| Kidney disease | +1.5245 | 1.3547 | ±2.7093 | +1.125 | 0.2604 |  |
| Circulatory disease | -0.2756 | 1.2153 | ±2.4307 | -0.227 | 0.8206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.2036**, Adj R² = **0.1426**, F-statistic = **3.34** (p = **8.63e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5578** | 6.8209 | ±13.6417 | **+6.972** | **3.12e-12** | *** |
| Education: graduate level (vs college) | +0.8726 | 0.9590 | ±1.9179 | +0.910 | 0.3628 |  |
| Education: high school or below (vs college) | +1.9658 | 1.5793 | ±3.1586 | +1.245 | 0.2132 |  |
| **Site: UCSD (vs UAB)** | **+3.2981** | 1.1482 | ±2.2963 | **+2.873** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1806 | 1.2036 | ±2.4072 | -0.150 | 0.8807 |  |
| Season: spring (vs autumn) | -1.6673 | 1.3103 | ±2.6207 | -1.272 | 0.2032 |  |
| Season: summer (vs autumn) | +0.9386 | 1.3060 | ±2.6120 | +0.719 | 0.4723 |  |
| **Season: winter (vs autumn)** | **-5.0349** | 1.4768 | ±2.9536 | **-3.409** | **6.51e-04** | *** |
| Age (years) | +0.0298 | 0.0491 | ±0.0983 | +0.607 | 0.5437 |  |
| BMI (kg/m2) | -0.0514 | 0.0658 | ±0.1316 | -0.782 | 0.4345 |  |
| Hypertension | +0.3528 | 1.0573 | ±2.1147 | +0.334 | 0.7387 |  |
| **High cholesterol** | **-2.0535** | 1.0084 | ±2.0169 | **-2.036** | **0.0417** | * |
| Kidney disease | +1.4944 | 1.3790 | ±2.7579 | +1.084 | 0.2785 |  |
| Circulatory disease | -0.2329 | 1.2344 | ±2.4688 | -0.189 | 0.8504 |  |
| HbA1c (%) | -0.1948 | 1.0888 | ±2.1775 | -0.179 | 0.8580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.2111**, Adj R² = **0.1507**, F-statistic = **3.50** (p = **4.44e-05**), Residual SE = **6.039** on **183** df, AIC = **1288.4**, BIC = **1337.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9091** | 6.5000 | ±12.9999 | **+6.294** | **3.10e-10** | *** |
| Education: graduate level (vs college) | +0.8791 | 0.9556 | ±1.9111 | +0.920 | 0.3576 |  |
| Education: high school or below (vs college) | +2.0679 | 1.5547 | ±3.1093 | +1.330 | 0.1835 |  |
| **Site: UCSD (vs UAB)** | **+3.3101** | 1.1321 | ±2.2641 | **+2.924** | **0.0035** | ** |
| Site: UW (vs UAB) | -0.1269 | 1.1969 | ±2.3938 | -0.106 | 0.9156 |  |
| Season: spring (vs autumn) | -1.7064 | 1.3047 | ±2.6094 | -1.308 | 0.1909 |  |
| Season: summer (vs autumn) | +0.7350 | 1.2979 | ±2.5959 | +0.566 | 0.5712 |  |
| **Season: winter (vs autumn)** | **-5.1261** | 1.4569 | ±2.9138 | **-3.518** | **4.34e-04** | *** |
| Age (years) | +0.0305 | 0.0488 | ±0.0976 | +0.625 | 0.5318 |  |
| BMI (kg/m2) | -0.0619 | 0.0625 | ±0.1251 | -0.990 | 0.3222 |  |
| Hypertension | +0.2676 | 1.0844 | ±2.1688 | +0.247 | 0.8051 |  |
| **High cholesterol** | **-2.0269** | 0.9884 | ±1.9768 | **-2.051** | **0.0403** | * |
| Kidney disease | +1.3824 | 1.3249 | ±2.6498 | +1.043 | 0.2968 |  |
| Circulatory disease | -0.3426 | 1.1936 | ±2.3872 | -0.287 | 0.7741 |  |
| Mean glucose (mg/dL) | +0.0463 | 0.0381 | ±0.0762 | +1.215 | 0.2244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.2111**, Adj R² = **0.1507**, F-statistic = **3.50** (p = **4.44e-05**), Residual SE = **6.039** on **183** df, AIC = **1288.4**, BIC = **1337.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.5026** | 10.9649 | ±21.9298 | **+3.147** | **0.0017** | ** |
| Education: graduate level (vs college) | +0.8791 | 0.9556 | ±1.9111 | +0.920 | 0.3576 |  |
| Education: high school or below (vs college) | +2.0679 | 1.5547 | ±3.1093 | +1.330 | 0.1835 |  |
| **Site: UCSD (vs UAB)** | **+3.3101** | 1.1321 | ±2.2641 | **+2.924** | **0.0035** | ** |
| Site: UW (vs UAB) | -0.1269 | 1.1969 | ±2.3938 | -0.106 | 0.9156 |  |
| Season: spring (vs autumn) | -1.7064 | 1.3047 | ±2.6094 | -1.308 | 0.1909 |  |
| Season: summer (vs autumn) | +0.7350 | 1.2979 | ±2.5959 | +0.566 | 0.5712 |  |
| **Season: winter (vs autumn)** | **-5.1261** | 1.4569 | ±2.9138 | **-3.518** | **4.34e-04** | *** |
| Age (years) | +0.0305 | 0.0488 | ±0.0976 | +0.625 | 0.5318 |  |
| BMI (kg/m2) | -0.0619 | 0.0625 | ±0.1251 | -0.990 | 0.3222 |  |
| Hypertension | +0.2676 | 1.0844 | ±2.1688 | +0.247 | 0.8051 |  |
| **High cholesterol** | **-2.0269** | 0.9884 | ±1.9768 | **-2.051** | **0.0403** | * |
| Kidney disease | +1.3824 | 1.3249 | ±2.6498 | +1.043 | 0.2968 |  |
| Circulatory disease | -0.3426 | 1.1936 | ±2.3872 | -0.287 | 0.7741 |  |
| GMI (%) | +1.9355 | 1.5931 | ±3.1863 | +1.215 | 0.2244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.2090**, Adj R² = **0.1484**, F-statistic = **3.45** (p = **5.37e-05**), Residual SE = **6.047** on **183** df, AIC = **1288.9**, BIC = **1338.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1632** | 5.8859 | ±11.7718 | **+7.163** | **7.87e-13** | *** |
| Education: graduate level (vs college) | +0.8418 | 0.9579 | ±1.9157 | +0.879 | 0.3795 |  |
| Education: high school or below (vs college) | +2.0199 | 1.5629 | ±3.1257 | +1.292 | 0.1962 |  |
| **Site: UCSD (vs UAB)** | **+3.2767** | 1.1402 | ±2.2804 | **+2.874** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1652 | 1.1974 | ±2.3949 | -0.138 | 0.8903 |  |
| Season: spring (vs autumn) | -1.6684 | 1.3030 | ±2.6060 | -1.280 | 0.2004 |  |
| Season: summer (vs autumn) | +0.8055 | 1.2961 | ±2.5922 | +0.621 | 0.5343 |  |
| **Season: winter (vs autumn)** | **-5.0543** | 1.4656 | ±2.9312 | **-3.449** | **5.63e-04** | *** |
| Age (years) | +0.0345 | 0.0491 | ±0.0983 | +0.702 | 0.4829 |  |
| BMI (kg/m2) | -0.0629 | 0.0639 | ±0.1278 | -0.985 | 0.3248 |  |
| Hypertension | +0.3219 | 1.0719 | ±2.1439 | +0.300 | 0.7640 |  |
| **High cholesterol** | **-2.0880** | 0.9841 | ±1.9682 | **-2.122** | **0.0339** | * |
| Kidney disease | +1.5089 | 1.3370 | ±2.6740 | +1.129 | 0.2591 |  |
| Circulatory disease | -0.3672 | 1.2076 | ±2.4153 | -0.304 | 0.7611 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0348 | 0.0333 | ±0.0667 | +1.043 | 0.2969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2174**, Adj R² = **0.1575**, F-statistic = **3.63** (p = **2.52e-05**), Residual SE = **6.015** on **183** df, AIC = **1286.8**, BIC = **1336.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.0448** | 4.7457 | ±9.4914 | **+9.070** | **1.19e-19** | *** |
| Education: graduate level (vs college) | +0.7644 | 0.9490 | ±1.8980 | +0.806 | 0.4205 |  |
| Education: high school or below (vs college) | +1.5041 | 1.5662 | ±3.1323 | +0.960 | 0.3368 |  |
| **Site: UCSD (vs UAB)** | **+3.4594** | 1.1360 | ±2.2720 | **+3.045** | **0.0023** | ** |
| Site: UW (vs UAB) | +0.1400 | 1.2049 | ±2.4098 | +0.116 | 0.9075 |  |
| Season: spring (vs autumn) | -1.6517 | 1.2982 | ±2.5964 | -1.272 | 0.2033 |  |
| Season: summer (vs autumn) | +0.9342 | 1.2793 | ±2.5586 | +0.730 | 0.4652 |  |
| **Season: winter (vs autumn)** | **-5.0415** | 1.4551 | ±2.9103 | **-3.465** | **5.31e-04** | *** |
| Age (years) | +0.0232 | 0.0482 | ±0.0964 | +0.481 | 0.6305 |  |
| BMI (kg/m2) | -0.0528 | 0.0626 | ±0.1253 | -0.844 | 0.3989 |  |
| Hypertension | +0.0534 | 1.0761 | ±2.1522 | +0.050 | 0.9604 |  |
| **High cholesterol** | **-1.9525** | 0.9896 | ±1.9792 | **-1.973** | **0.0485** | * |
| Kidney disease | +1.1586 | 1.2859 | ±2.5718 | +0.901 | 0.3676 |  |
| Circulatory disease | -0.4055 | 1.1764 | ±2.3529 | -0.345 | 0.7303 |  |
| Glucose SD, pooled (mg/dL) | +0.1804 | 0.0934 | ±0.1867 | +1.932 | 0.0534 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2137**, Adj R² = **0.1536**, F-statistic = **3.55** (p = **3.50e-05**), Residual SE = **6.029** on **183** df, AIC = **1287.7**, BIC = **1337.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7804** | 4.7393 | ±9.4785 | **+9.238** | **2.52e-20** | *** |
| Education: graduate level (vs college) | +0.7963 | 0.9511 | ±1.9022 | +0.837 | 0.4025 |  |
| Education: high school or below (vs college) | +1.6369 | 1.5644 | ±3.1288 | +1.046 | 0.2954 |  |
| **Site: UCSD (vs UAB)** | **+3.3493** | 1.1345 | ±2.2691 | **+2.952** | **0.0032** | ** |
| Site: UW (vs UAB) | +0.0165 | 1.2042 | ±2.4084 | +0.014 | 0.9891 |  |
| Season: spring (vs autumn) | -1.6011 | 1.3008 | ±2.6015 | -1.231 | 0.2184 |  |
| Season: summer (vs autumn) | +0.9872 | 1.2900 | ±2.5800 | +0.765 | 0.4441 |  |
| **Season: winter (vs autumn)** | **-5.0106** | 1.4577 | ±2.9153 | **-3.437** | **5.87e-04** | *** |
| Age (years) | +0.0237 | 0.0482 | ±0.0964 | +0.492 | 0.6228 |  |
| BMI (kg/m2) | -0.0529 | 0.0626 | ±0.1251 | -0.846 | 0.3975 |  |
| Hypertension | +0.0313 | 1.0793 | ±2.1586 | +0.029 | 0.9768 |  |
| **High cholesterol** | **-1.9646** | 0.9920 | ±1.9840 | **-1.981** | **0.0476** | * |
| Kidney disease | +1.3014 | 1.3020 | ±2.6041 | +1.000 | 0.3176 |  |
| Circulatory disease | -0.3090 | 1.1961 | ±2.3922 | -0.258 | 0.7961 |  |
| Avg. daily SD (mg/dL) | +0.1573 | 0.0944 | ±0.1888 | +1.666 | 0.0956 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.2100**, Adj R² = **0.1495**, F-statistic = **3.47** (p = **4.91e-05**), Residual SE = **6.043** on **183** df, AIC = **1288.7**, BIC = **1338.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5967** | 5.0953 | ±10.1906 | **+8.556** | **1.17e-17** | *** |
| Education: graduate level (vs college) | +0.7916 | 0.9496 | ±1.8991 | +0.834 | 0.4044 |  |
| Education: high school or below (vs college) | +1.5176 | 1.6561 | ±3.3121 | +0.916 | 0.3594 |  |
| **Site: UCSD (vs UAB)** | **+3.4287** | 1.1563 | ±2.3127 | **+2.965** | **0.0030** | ** |
| Site: UW (vs UAB) | +0.0544 | 1.2217 | ±2.4433 | +0.045 | 0.9645 |  |
| Season: spring (vs autumn) | -1.6337 | 1.3022 | ±2.6043 | -1.255 | 0.2096 |  |
| Season: summer (vs autumn) | +1.0260 | 1.2941 | ±2.5882 | +0.793 | 0.4279 |  |
| **Season: winter (vs autumn)** | **-5.0190** | 1.4679 | ±2.9357 | **-3.419** | **6.28e-04** | *** |
| Age (years) | +0.0238 | 0.0485 | ±0.0970 | +0.490 | 0.6242 |  |
| BMI (kg/m2) | -0.0493 | 0.0631 | ±0.1261 | -0.781 | 0.4345 |  |
| Hypertension | +0.1487 | 1.0607 | ±2.1213 | +0.140 | 0.8885 |  |
| **High cholesterol** | **-2.0010** | 0.9994 | ±1.9988 | **-2.002** | **0.0453** | * |
| Kidney disease | +1.2983 | 1.3318 | ±2.6636 | +0.975 | 0.3296 |  |
| Circulatory disease | -0.3306 | 1.2033 | ±2.4065 | -0.275 | 0.7835 |  |
| CV (%) | +0.1849 | 0.1493 | ±0.2986 | +1.239 | 0.2155 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.2071**, Adj R² = **0.1465**, F-statistic = **3.41** (p = **6.30e-05**), Residual SE = **6.054** on **183** df, AIC = **1289.4**, BIC = **1338.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0202** | 4.9441 | ±9.8883 | **+9.915** | **3.59e-23** | *** |
| Education: graduate level (vs college) | +0.8259 | 0.9508 | ±1.9015 | +0.869 | 0.3850 |  |
| Education: high school or below (vs college) | +1.6640 | 1.6411 | ±3.2822 | +1.014 | 0.3106 |  |
| **Site: UCSD (vs UAB)** | **+3.3747** | 1.1530 | ±2.3059 | **+2.927** | **0.0034** | ** |
| Site: UW (vs UAB) | -0.0238 | 1.2163 | ±2.4326 | -0.020 | 0.9844 |  |
| Season: spring (vs autumn) | -1.6427 | 1.3087 | ±2.6174 | -1.255 | 0.2094 |  |
| Season: summer (vs autumn) | +0.9899 | 1.3023 | ±2.6046 | +0.760 | 0.4472 |  |
| **Season: winter (vs autumn)** | **-5.0352** | 1.4715 | ±2.9429 | **-3.422** | **6.22e-04** | *** |
| Age (years) | +0.0250 | 0.0485 | ±0.0970 | +0.516 | 0.6057 |  |
| BMI (kg/m2) | -0.0531 | 0.0627 | ±0.1255 | -0.847 | 0.3970 |  |
| Hypertension | +0.1884 | 1.0647 | ±2.1295 | +0.177 | 0.8596 |  |
| **High cholesterol** | **-2.0375** | 0.9978 | ±1.9957 | **-2.042** | **0.0412** | * |
| Kidney disease | +1.3601 | 1.3462 | ±2.6924 | +1.010 | 0.3123 |  |
| Circulatory disease | -0.2922 | 1.2068 | ±2.4137 | -0.242 | 0.8087 |  |
| Mean / SD ratio | -0.3641 | 0.3773 | ±0.7546 | -0.965 | 0.3346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2051**, Adj R² = **0.1443**, F-statistic = **3.37** (p = **7.55e-05**), Residual SE = **6.062** on **183** df, AIC = **1289.9**, BIC = **1339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.0590** | 4.8382 | ±9.6764 | **+9.933** | **2.98e-23** | *** |
| Education: graduate level (vs college) | +0.8614 | 0.9534 | ±1.9068 | +0.904 | 0.3662 |  |
| Education: high school or below (vs college) | +1.8048 | 1.6104 | ±3.2208 | +1.121 | 0.2624 |  |
| **Site: UCSD (vs UAB)** | **+3.2948** | 1.1406 | ±2.2811 | **+2.889** | **0.0039** | ** |
| Site: UW (vs UAB) | -0.1058 | 1.2114 | ±2.4227 | -0.087 | 0.9304 |  |
| Season: spring (vs autumn) | -1.6391 | 1.3119 | ±2.6239 | -1.249 | 0.2115 |  |
| Season: summer (vs autumn) | +0.9794 | 1.3124 | ±2.6248 | +0.746 | 0.4555 |  |
| **Season: winter (vs autumn)** | **-5.0152** | 1.4744 | ±2.9488 | **-3.402** | **6.70e-04** | *** |
| Age (years) | +0.0263 | 0.0488 | ±0.0976 | +0.539 | 0.5901 |  |
| BMI (kg/m2) | -0.0540 | 0.0627 | ±0.1255 | -0.861 | 0.3895 |  |
| Hypertension | +0.2056 | 1.0698 | ±2.1396 | +0.192 | 0.8476 |  |
| **High cholesterol** | **-2.0623** | 0.9951 | ±1.9902 | **-2.072** | **0.0382** | * |
| Kidney disease | +1.4460 | 1.3529 | ±2.7058 | +1.069 | 0.2851 |  |
| Circulatory disease | -0.2368 | 1.2287 | ±2.4575 | -0.193 | 0.8472 |  |
| Avg. daily mean/SD | -0.1878 | 0.2856 | ±0.5712 | -0.658 | 0.5107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.2130**, Adj R² = **0.1528**, F-statistic = **3.54** (p = **3.73e-05**), Residual SE = **6.032** on **183** df, AIC = **1287.9**, BIC = **1337.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.9232** | 5.2165 | ±10.4329 | **+8.228** | **1.90e-16** | *** |
| Education: graduate level (vs college) | +0.8543 | 0.9508 | ±1.9016 | +0.898 | 0.3689 |  |
| Education: high school or below (vs college) | +1.7862 | 1.5447 | ±3.0893 | +1.156 | 0.2475 |  |
| **Site: UCSD (vs UAB)** | **+3.2937** | 1.1299 | ±2.2599 | **+2.915** | **0.0036** | ** |
| Site: UW (vs UAB) | -0.0872 | 1.1926 | ±2.3851 | -0.073 | 0.9417 |  |
| Season: spring (vs autumn) | -1.6322 | 1.3110 | ±2.6219 | -1.245 | 0.2131 |  |
| Season: summer (vs autumn) | +0.9409 | 1.2984 | ±2.5968 | +0.725 | 0.4687 |  |
| **Season: winter (vs autumn)** | **-5.0047** | 1.4707 | ±2.9414 | **-3.403** | **6.67e-04** | *** |
| Age (years) | +0.0314 | 0.0479 | ±0.0957 | +0.656 | 0.5118 |  |
| BMI (kg/m2) | -0.0579 | 0.0619 | ±0.1238 | -0.935 | 0.3499 |  |
| Hypertension | +0.2557 | 1.0601 | ±2.1203 | +0.241 | 0.8094 |  |
| **High cholesterol** | **-2.1333** | 0.9812 | ±1.9625 | **-2.174** | **0.0297** | * |
| Kidney disease | +1.5339 | 1.3405 | ±2.6810 | +1.144 | 0.2525 |  |
| Circulatory disease | -0.1614 | 1.2228 | ±2.4457 | -0.132 | 0.8950 |  |
| MAG (mg/dL/h) | +0.1006 | 0.0709 | ±0.1417 | +1.420 | 0.1557 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.2129**, Adj R² = **0.1527**, F-statistic = **3.54** (p = **3.78e-05**), Residual SE = **6.032** on **183** df, AIC = **1288.0**, BIC = **1337.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.1376** | 5.0318 | ±10.0636 | **+8.573** | **1.01e-17** | *** |
| Education: graduate level (vs college) | +0.8383 | 0.9518 | ±1.9035 | +0.881 | 0.3784 |  |
| Education: high school or below (vs college) | +1.7129 | 1.5622 | ±3.1243 | +1.096 | 0.2729 |  |
| **Site: UCSD (vs UAB)** | **+3.3878** | 1.1377 | ±2.2753 | **+2.978** | **0.0029** | ** |
| Site: UW (vs UAB) | -0.0011 | 1.2076 | ±2.4151 | -0.001 | 0.9993 |  |
| Season: spring (vs autumn) | -1.6337 | 1.3031 | ±2.6061 | -1.254 | 0.2099 |  |
| Season: summer (vs autumn) | +1.0046 | 1.2895 | ±2.5791 | +0.779 | 0.4359 |  |
| **Season: winter (vs autumn)** | **-4.9892** | 1.4619 | ±2.9238 | **-3.413** | **6.43e-04** | *** |
| Age (years) | +0.0235 | 0.0480 | ±0.0959 | +0.489 | 0.6245 |  |
| BMI (kg/m2) | -0.0483 | 0.0634 | ±0.1268 | -0.761 | 0.4464 |  |
| Hypertension | +0.1254 | 1.0583 | ±2.1166 | +0.118 | 0.9057 |  |
| **High cholesterol** | **-2.0264** | 0.9875 | ±1.9750 | **-2.052** | **0.0402** | * |
| Kidney disease | +1.3921 | 1.3152 | ±2.6304 | +1.058 | 0.2899 |  |
| Circulatory disease | -0.2657 | 1.2021 | ±2.4043 | -0.221 | 0.8251 |  |
| Avg. daily range (mg/dL) | +0.0372 | 0.0230 | ±0.0460 | +1.617 | 0.1058 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.2080**, Adj R² = **0.1474**, F-statistic = **3.43** (p = **5.86e-05**), Residual SE = **6.051** on **183** df, AIC = **1289.2**, BIC = **1338.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.3633** | 4.4103 | ±8.8206 | **+10.286** | **8.17e-25** | *** |
| Education: graduate level (vs college) | +0.8246 | 0.9555 | ±1.9110 | +0.863 | 0.3881 |  |
| Education: high school or below (vs college) | +1.7003 | 1.5877 | ±3.1754 | +1.071 | 0.2842 |  |
| **Site: UCSD (vs UAB)** | **+3.4990** | 1.1319 | ±2.2638 | **+3.091** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.0513 | 1.1707 | ±2.3414 | +0.044 | 0.9650 |  |
| Season: spring (vs autumn) | -1.7506 | 1.2970 | ±2.5940 | -1.350 | 0.1771 |  |
| Season: summer (vs autumn) | +0.7372 | 1.2872 | ±2.5743 | +0.573 | 0.5668 |  |
| **Season: winter (vs autumn)** | **-5.0604** | 1.4731 | ±2.9461 | **-3.435** | **5.92e-04** | *** |
| Age (years) | +0.0285 | 0.0490 | ±0.0980 | +0.581 | 0.5611 |  |
| BMI (kg/m2) | -0.0551 | 0.0626 | ±0.1252 | -0.880 | 0.3789 |  |
| Hypertension | +0.4258 | 1.0554 | ±2.1107 | +0.403 | 0.6866 |  |
| **High cholesterol** | **-2.1019** | 0.9885 | ±1.9770 | **-2.126** | **0.0335** | * |
| Kidney disease | +1.2745 | 1.3360 | ±2.6720 | +0.954 | 0.3401 |  |
| Circulatory disease | -0.5382 | 1.1967 | ±2.3934 | -0.450 | 0.6529 |  |
| SD of daily means (mg/dL) | +0.1925 | 0.2040 | ±0.4079 | +0.944 | 0.3452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.2093**, Adj R² = **0.1488**, F-statistic = **3.46** (p = **5.21e-05**), Residual SE = **6.046** on **183** df, AIC = **1288.9**, BIC = **1338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7244** | 12.5329 | ±25.0659 | **+4.606** | **4.11e-06** | *** |
| Education: graduate level (vs college) | +0.8132 | 0.9537 | ±1.9074 | +0.853 | 0.3938 |  |
| Education: high school or below (vs college) | +1.8162 | 1.5576 | ±3.1151 | +1.166 | 0.2436 |  |
| **Site: UCSD (vs UAB)** | **+3.4000** | 1.1511 | ±2.3022 | **+2.954** | **0.0031** | ** |
| Site: UW (vs UAB) | -0.0743 | 1.1986 | ±2.3972 | -0.062 | 0.9506 |  |
| Season: spring (vs autumn) | -1.6487 | 1.3012 | ±2.6024 | -1.267 | 0.2051 |  |
| Season: summer (vs autumn) | +0.8344 | 1.2889 | ±2.5777 | +0.647 | 0.5174 |  |
| **Season: winter (vs autumn)** | **-5.0939** | 1.4579 | ±2.9157 | **-3.494** | **4.76e-04** | *** |
| Age (years) | +0.0240 | 0.0489 | ±0.0978 | +0.490 | 0.6243 |  |
| BMI (kg/m2) | -0.0563 | 0.0627 | ±0.1253 | -0.898 | 0.3691 |  |
| Hypertension | +0.2826 | 1.0939 | ±2.1879 | +0.258 | 0.7962 |  |
| **High cholesterol** | **-2.0071** | 0.9920 | ±1.9840 | **-2.023** | **0.0430** | * |
| Kidney disease | +1.2960 | 1.3361 | ±2.6723 | +0.970 | 0.3321 |  |
| Circulatory disease | -0.3387 | 1.1952 | ±2.3904 | -0.283 | 0.7769 |  |
| Time in range 70-180, pooled (%) | -0.1121 | 0.1226 | ±0.2452 | -0.914 | 0.3607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.2104**, Adj R² = **0.1500**, F-statistic = **3.48** (p = **4.73e-05**), Residual SE = **6.042** on **183** df, AIC = **1288.6**, BIC = **1337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.9925** | 12.3697 | ±24.7394 | **+4.769** | **1.85e-06** | *** |
| Education: graduate level (vs college) | +0.8147 | 0.9532 | ±1.9064 | +0.855 | 0.3927 |  |
| Education: high school or below (vs college) | +1.8291 | 1.5562 | ±3.1125 | +1.175 | 0.2399 |  |
| **Site: UCSD (vs UAB)** | **+3.4090** | 1.1480 | ±2.2960 | **+2.970** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.0863 | 1.1969 | ±2.3937 | -0.072 | 0.9425 |  |
| Season: spring (vs autumn) | -1.6411 | 1.2989 | ±2.5978 | -1.263 | 0.2064 |  |
| Season: summer (vs autumn) | +0.8229 | 1.2877 | ±2.5753 | +0.639 | 0.5228 |  |
| **Season: winter (vs autumn)** | **-5.1010** | 1.4568 | ±2.9137 | **-3.501** | **4.63e-04** | *** |
| Age (years) | +0.0233 | 0.0490 | ±0.0979 | +0.475 | 0.6345 |  |
| BMI (kg/m2) | -0.0557 | 0.0626 | ±0.1252 | -0.889 | 0.3738 |  |
| Hypertension | +0.2595 | 1.0948 | ±2.1896 | +0.237 | 0.8126 |  |
| **High cholesterol** | **-2.0059** | 0.9890 | ±1.9780 | **-2.028** | **0.0425** | * |
| Kidney disease | +1.2701 | 1.3277 | ±2.6554 | +0.957 | 0.3388 |  |
| Circulatory disease | -0.3417 | 1.1926 | ±2.3853 | -0.286 | 0.7745 |  |
| Avg. daily time in range 70-180 (%) | -0.1247 | 0.1201 | ±0.2403 | -1.038 | 0.2994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.2036**, Adj R² = **0.1426**, F-statistic = **3.34** (p = **8.62e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5513** | 4.4921 | ±8.9843 | **+10.363** | **3.66e-25** | *** |
| Education: graduate level (vs college) | +0.8665 | 0.9553 | ±1.9106 | +0.907 | 0.3644 |  |
| Education: high school or below (vs college) | +1.9142 | 1.5812 | ±3.1625 | +1.211 | 0.2261 |  |
| **Site: UCSD (vs UAB)** | **+3.3173** | 1.1455 | ±2.2911 | **+2.896** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.1722 | 1.2040 | ±2.4081 | -0.143 | 0.8863 |  |
| Season: spring (vs autumn) | -1.6349 | 1.3194 | ±2.6389 | -1.239 | 0.2153 |  |
| Season: summer (vs autumn) | +0.9301 | 1.3379 | ±2.6757 | +0.695 | 0.4869 |  |
| **Season: winter (vs autumn)** | **-5.0199** | 1.4895 | ±2.9790 | **-3.370** | **7.51e-04** | *** |
| Age (years) | +0.0281 | 0.0515 | ±0.1031 | +0.544 | 0.5861 |  |
| BMI (kg/m2) | -0.0537 | 0.0619 | ±0.1237 | -0.869 | 0.3851 |  |
| Hypertension | +0.3371 | 1.0571 | ±2.1143 | +0.319 | 0.7498 |  |
| **High cholesterol** | **-2.0862** | 0.9906 | ±1.9811 | **-2.106** | **0.0352** | * |
| Kidney disease | +1.5392 | 1.3597 | ±2.7194 | +1.132 | 0.2576 |  |
| Circulatory disease | -0.2772 | 1.2413 | ±2.4827 | -0.223 | 0.8233 |  |
| Time 54-69, pooled (%) | +0.3632 | 2.0561 | ±4.1121 | +0.177 | 0.8598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.2034**, Adj R² = **0.1424**, F-statistic = **3.34** (p = **8.76e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5075** | 4.4746 | ±8.9492 | **+10.394** | **2.65e-25** | *** |
| Education: graduate level (vs college) | +0.8854 | 0.9558 | ±1.9116 | +0.926 | 0.3543 |  |
| Education: high school or below (vs college) | +1.9749 | 1.5854 | ±3.1709 | +1.246 | 0.2129 |  |
| **Site: UCSD (vs UAB)** | **+3.2962** | 1.1486 | ±2.2971 | **+2.870** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1765 | 1.2033 | ±2.4066 | -0.147 | 0.8834 |  |
| Season: spring (vs autumn) | -1.6723 | 1.3189 | ±2.6377 | -1.268 | 0.2048 |  |
| Season: summer (vs autumn) | +0.9050 | 1.3308 | ±2.6616 | +0.680 | 0.4965 |  |
| **Season: winter (vs autumn)** | **-5.0611** | 1.4838 | ±2.9676 | **-3.411** | **6.47e-04** | *** |
| Age (years) | +0.0303 | 0.0508 | ±0.1016 | +0.597 | 0.5504 |  |
| BMI (kg/m2) | -0.0548 | 0.0617 | ±0.1235 | -0.888 | 0.3746 |  |
| Hypertension | +0.3522 | 1.0585 | ±2.1171 | +0.333 | 0.7394 |  |
| **High cholesterol** | **-2.0683** | 0.9890 | ±1.9780 | **-2.091** | **0.0365** | * |
| Kidney disease | +1.5160 | 1.3632 | ±2.7264 | +1.112 | 0.2661 |  |
| Circulatory disease | -0.2785 | 1.2312 | ±2.4625 | -0.226 | 0.8210 |  |
| Avg. daily time 54-69 (%) | -0.1469 | 1.6214 | ±3.2429 | -0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.2036**, Adj R² = **0.1426**, F-statistic = **3.34** (p = **8.62e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5513** | 4.4921 | ±8.9843 | **+10.363** | **3.66e-25** | *** |
| Education: graduate level (vs college) | +0.8665 | 0.9553 | ±1.9106 | +0.907 | 0.3644 |  |
| Education: high school or below (vs college) | +1.9142 | 1.5812 | ±3.1625 | +1.211 | 0.2261 |  |
| **Site: UCSD (vs UAB)** | **+3.3173** | 1.1455 | ±2.2911 | **+2.896** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.1722 | 1.2040 | ±2.4081 | -0.143 | 0.8863 |  |
| Season: spring (vs autumn) | -1.6349 | 1.3194 | ±2.6389 | -1.239 | 0.2153 |  |
| Season: summer (vs autumn) | +0.9301 | 1.3379 | ±2.6757 | +0.695 | 0.4869 |  |
| **Season: winter (vs autumn)** | **-5.0199** | 1.4895 | ±2.9790 | **-3.370** | **7.51e-04** | *** |
| Age (years) | +0.0281 | 0.0515 | ±0.1031 | +0.544 | 0.5861 |  |
| BMI (kg/m2) | -0.0537 | 0.0619 | ±0.1237 | -0.869 | 0.3851 |  |
| Hypertension | +0.3371 | 1.0571 | ±2.1143 | +0.319 | 0.7498 |  |
| **High cholesterol** | **-2.0862** | 0.9906 | ±1.9811 | **-2.106** | **0.0352** | * |
| Kidney disease | +1.5392 | 1.3597 | ±2.7194 | +1.132 | 0.2576 |  |
| Circulatory disease | -0.2772 | 1.2413 | ±2.4827 | -0.223 | 0.8233 |  |
| Time < 70 (%) | +0.3632 | 2.0561 | ±4.1121 | +0.177 | 0.8598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.2034**, Adj R² = **0.1424**, F-statistic = **3.34** (p = **8.76e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5075** | 4.4746 | ±8.9492 | **+10.394** | **2.65e-25** | *** |
| Education: graduate level (vs college) | +0.8854 | 0.9558 | ±1.9116 | +0.926 | 0.3543 |  |
| Education: high school or below (vs college) | +1.9749 | 1.5854 | ±3.1709 | +1.246 | 0.2129 |  |
| **Site: UCSD (vs UAB)** | **+3.2962** | 1.1486 | ±2.2971 | **+2.870** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1765 | 1.2033 | ±2.4066 | -0.147 | 0.8834 |  |
| Season: spring (vs autumn) | -1.6723 | 1.3189 | ±2.6377 | -1.268 | 0.2048 |  |
| Season: summer (vs autumn) | +0.9050 | 1.3308 | ±2.6616 | +0.680 | 0.4965 |  |
| **Season: winter (vs autumn)** | **-5.0611** | 1.4838 | ±2.9676 | **-3.411** | **6.47e-04** | *** |
| Age (years) | +0.0303 | 0.0508 | ±0.1016 | +0.597 | 0.5504 |  |
| BMI (kg/m2) | -0.0548 | 0.0617 | ±0.1235 | -0.888 | 0.3746 |  |
| Hypertension | +0.3522 | 1.0585 | ±2.1171 | +0.333 | 0.7394 |  |
| **High cholesterol** | **-2.0683** | 0.9890 | ±1.9780 | **-2.091** | **0.0365** | * |
| Kidney disease | +1.5160 | 1.3632 | ±2.7264 | +1.112 | 0.2661 |  |
| Circulatory disease | -0.2785 | 1.2312 | ±2.4625 | -0.226 | 0.8210 |  |
| Avg. daily time < 70 (%) | -0.1469 | 1.6214 | ±3.2429 | -0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.2091**, Adj R² = **0.1486**, F-statistic = **3.46** (p = **5.30e-05**), Residual SE = **6.047** on **183** df, AIC = **1288.9**, BIC = **1338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5089** | 4.4797 | ±8.9595 | **+10.382** | **2.99e-25** | *** |
| Education: graduate level (vs college) | +0.8189 | 0.9537 | ±1.9073 | +0.859 | 0.3905 |  |
| Education: high school or below (vs college) | +1.8328 | 1.5595 | ±3.1190 | +1.175 | 0.2399 |  |
| **Site: UCSD (vs UAB)** | **+3.3923** | 1.1506 | ±2.3012 | **+2.948** | **0.0032** | ** |
| Site: UW (vs UAB) | -0.0783 | 1.1989 | ±2.3978 | -0.065 | 0.9479 |  |
| Season: spring (vs autumn) | -1.6570 | 1.3018 | ±2.6036 | -1.273 | 0.2031 |  |
| Season: summer (vs autumn) | +0.8318 | 1.2890 | ±2.5780 | +0.645 | 0.5187 |  |
| **Season: winter (vs autumn)** | **-5.1017** | 1.4586 | ±2.9173 | **-3.498** | **4.69e-04** | *** |
| Age (years) | +0.0246 | 0.0488 | ±0.0977 | +0.503 | 0.6149 |  |
| BMI (kg/m2) | -0.0565 | 0.0626 | ±0.1252 | -0.902 | 0.3671 |  |
| Hypertension | +0.2869 | 1.0930 | ±2.1859 | +0.262 | 0.7929 |  |
| **High cholesterol** | **-2.0049** | 0.9926 | ±1.9853 | **-2.020** | **0.0434** | * |
| Kidney disease | +1.2972 | 1.3391 | ±2.6783 | +0.969 | 0.3327 |  |
| Circulatory disease | -0.3367 | 1.1950 | ±2.3899 | -0.282 | 0.7781 |  |
| Time 181-250, pooled (%) | +0.1093 | 0.1215 | ±0.2430 | +0.900 | 0.3683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.2103**, Adj R² = **0.1499**, F-statistic = **3.48** (p = **4.76e-05**), Residual SE = **6.042** on **183** df, AIC = **1288.6**, BIC = **1337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5106** | 4.4713 | ±8.9426 | **+10.402** | **2.43e-25** | *** |
| Education: graduate level (vs college) | +0.8201 | 0.9531 | ±1.9062 | +0.861 | 0.3895 |  |
| Education: high school or below (vs college) | +1.8453 | 1.5573 | ±3.1146 | +1.185 | 0.2360 |  |
| **Site: UCSD (vs UAB)** | **+3.4044** | 1.1477 | ±2.2953 | **+2.966** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.0870 | 1.1969 | ±2.3939 | -0.073 | 0.9421 |  |
| Season: spring (vs autumn) | -1.6506 | 1.2994 | ±2.5988 | -1.270 | 0.2040 |  |
| Season: summer (vs autumn) | +0.8158 | 1.2872 | ±2.5744 | +0.634 | 0.5262 |  |
| **Season: winter (vs autumn)** | **-5.1101** | 1.4572 | ±2.9145 | **-3.507** | **4.54e-04** | *** |
| Age (years) | +0.0239 | 0.0489 | ±0.0977 | +0.490 | 0.6242 |  |
| BMI (kg/m2) | -0.0559 | 0.0625 | ±0.1251 | -0.894 | 0.3714 |  |
| Hypertension | +0.2656 | 1.0936 | ±2.1872 | +0.243 | 0.8081 |  |
| **High cholesterol** | **-2.0025** | 0.9892 | ±1.9785 | **-2.024** | **0.0429** | * |
| Kidney disease | +1.2664 | 1.3303 | ±2.6605 | +0.952 | 0.3411 |  |
| Circulatory disease | -0.3433 | 1.1921 | ±2.3842 | -0.288 | 0.7734 |  |
| Avg. daily time 181-250 (%) | +0.1230 | 0.1190 | ±0.2380 | +1.034 | 0.3013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.2091**, Adj R² = **0.1486**, F-statistic = **3.46** (p = **5.30e-05**), Residual SE = **6.047** on **183** df, AIC = **1288.9**, BIC = **1338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5089** | 4.4797 | ±8.9595 | **+10.382** | **2.99e-25** | *** |
| Education: graduate level (vs college) | +0.8189 | 0.9537 | ±1.9073 | +0.859 | 0.3905 |  |
| Education: high school or below (vs college) | +1.8328 | 1.5595 | ±3.1190 | +1.175 | 0.2399 |  |
| **Site: UCSD (vs UAB)** | **+3.3923** | 1.1506 | ±2.3012 | **+2.948** | **0.0032** | ** |
| Site: UW (vs UAB) | -0.0783 | 1.1989 | ±2.3978 | -0.065 | 0.9479 |  |
| Season: spring (vs autumn) | -1.6570 | 1.3018 | ±2.6036 | -1.273 | 0.2031 |  |
| Season: summer (vs autumn) | +0.8318 | 1.2890 | ±2.5780 | +0.645 | 0.5187 |  |
| **Season: winter (vs autumn)** | **-5.1017** | 1.4586 | ±2.9173 | **-3.498** | **4.69e-04** | *** |
| Age (years) | +0.0246 | 0.0488 | ±0.0977 | +0.503 | 0.6149 |  |
| BMI (kg/m2) | -0.0565 | 0.0626 | ±0.1252 | -0.902 | 0.3671 |  |
| Hypertension | +0.2869 | 1.0930 | ±2.1859 | +0.262 | 0.7929 |  |
| **High cholesterol** | **-2.0049** | 0.9926 | ±1.9853 | **-2.020** | **0.0434** | * |
| Kidney disease | +1.2972 | 1.3391 | ±2.6783 | +0.969 | 0.3327 |  |
| Circulatory disease | -0.3367 | 1.1950 | ±2.3899 | -0.282 | 0.7781 |  |
| Time > 180 (%) | +0.1093 | 0.1215 | ±0.2430 | +0.900 | 0.3683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.2103**, Adj R² = **0.1499**, F-statistic = **3.48** (p = **4.76e-05**), Residual SE = **6.042** on **183** df, AIC = **1288.6**, BIC = **1337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5106** | 4.4713 | ±8.9426 | **+10.402** | **2.43e-25** | *** |
| Education: graduate level (vs college) | +0.8201 | 0.9531 | ±1.9062 | +0.861 | 0.3895 |  |
| Education: high school or below (vs college) | +1.8453 | 1.5573 | ±3.1146 | +1.185 | 0.2360 |  |
| **Site: UCSD (vs UAB)** | **+3.4044** | 1.1477 | ±2.2953 | **+2.966** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.0870 | 1.1969 | ±2.3939 | -0.073 | 0.9421 |  |
| Season: spring (vs autumn) | -1.6506 | 1.2994 | ±2.5988 | -1.270 | 0.2040 |  |
| Season: summer (vs autumn) | +0.8158 | 1.2872 | ±2.5744 | +0.634 | 0.5262 |  |
| **Season: winter (vs autumn)** | **-5.1101** | 1.4572 | ±2.9145 | **-3.507** | **4.54e-04** | *** |
| Age (years) | +0.0239 | 0.0489 | ±0.0977 | +0.490 | 0.6242 |  |
| BMI (kg/m2) | -0.0559 | 0.0625 | ±0.1251 | -0.894 | 0.3714 |  |
| Hypertension | +0.2656 | 1.0936 | ±2.1872 | +0.243 | 0.8081 |  |
| **High cholesterol** | **-2.0025** | 0.9892 | ±1.9785 | **-2.024** | **0.0429** | * |
| Kidney disease | +1.2664 | 1.3303 | ±2.6605 | +0.952 | 0.3411 |  |
| Circulatory disease | -0.3433 | 1.1921 | ±2.3842 | -0.288 | 0.7734 |  |
| Avg. daily time > 180 (%) | +0.1230 | 0.1190 | ±0.2380 | +1.034 | 0.3013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.2075**, Adj R² = **0.1468**, F-statistic = **3.42** (p = **6.13e-05**), Residual SE = **6.053** on **183** df, AIC = **1289.3**, BIC = **1338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5512** | 4.4483 | ±8.8966 | **+10.465** | **1.25e-25** | *** |
| Education: graduate level (vs college) | +0.8547 | 0.9546 | ±1.9092 | +0.895 | 0.3706 |  |
| Education: high school or below (vs college) | +1.7734 | 1.5744 | ±3.1489 | +1.126 | 0.2600 |  |
| **Site: UCSD (vs UAB)** | **+3.4526** | 1.1692 | ±2.3384 | **+2.953** | **0.0031** | ** |
| Site: UW (vs UAB) | -0.0322 | 1.1982 | ±2.3963 | -0.027 | 0.9786 |  |
| Season: spring (vs autumn) | -1.7076 | 1.3036 | ±2.6072 | -1.310 | 0.1902 |  |
| Season: summer (vs autumn) | +0.8060 | 1.2831 | ±2.5662 | +0.628 | 0.5299 |  |
| **Season: winter (vs autumn)** | **-5.0788** | 1.4548 | ±2.9095 | **-3.491** | **4.81e-04** | *** |
| Age (years) | +0.0280 | 0.0488 | ±0.0976 | +0.574 | 0.5661 |  |
| BMI (kg/m2) | -0.0602 | 0.0620 | ±0.1241 | -0.970 | 0.3322 |  |
| Hypertension | +0.4254 | 1.0651 | ±2.1302 | +0.399 | 0.6896 |  |
| **High cholesterol** | **-2.0790** | 0.9847 | ±1.9694 | **-2.111** | **0.0347** | * |
| Kidney disease | +1.3238 | 1.3471 | ±2.6941 | +0.983 | 0.3257 |  |
| Circulatory disease | -0.3512 | 1.2138 | ±2.4276 | -0.289 | 0.7724 |  |
| Nocturnal time > 180 (%) | +0.0869 | 0.1265 | ±0.2531 | +0.687 | 0.4922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.1205**, Adj R² = **0.0584**, F-statistic = **1.94** (p = **0.0283**), Residual SE = **16.521** on **184** df, AIC = **1686.0**, BIC = **1732.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5849** | 11.1530 | ±22.3061 | **+12.157** | **5.28e-34** | *** |
| **Education: graduate level (vs college)** | **-5.6870** | 2.4925 | ±4.9850 | **-2.282** | **0.0225** | * |
| Education: high school or below (vs college) | +7.3691 | 4.4314 | ±8.8628 | +1.663 | 0.0963 | . |
| Site: UCSD (vs UAB) | +3.0172 | 3.1864 | ±6.3728 | +0.947 | 0.3437 |  |
| Site: UW (vs UAB) | -0.2211 | 3.2829 | ±6.5658 | -0.067 | 0.9463 |  |
| Season: spring (vs autumn) | -0.1182 | 3.5615 | ±7.1231 | -0.033 | 0.9735 |  |
| Season: summer (vs autumn) | +0.8371 | 3.8640 | ±7.7280 | +0.217 | 0.8285 |  |
| Season: winter (vs autumn) | +4.7515 | 4.0906 | ±8.1812 | +1.162 | 0.2454 |  |
| Age (years) | -0.2303 | 0.1284 | ±0.2567 | -1.794 | 0.0728 | . |
| BMI (kg/m2) | +0.1509 | 0.1792 | ±0.3583 | +0.842 | 0.3998 |  |
| Hypertension | +0.7651 | 2.6569 | ±5.3139 | +0.288 | 0.7734 |  |
| High cholesterol | -0.8232 | 2.5495 | ±5.0990 | -0.323 | 0.7468 |  |
| Kidney disease | -4.2389 | 3.6895 | ±7.3791 | -1.149 | 0.2506 |  |
| Circulatory disease | -0.2007 | 3.2430 | ±6.4860 | -0.062 | 0.9506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.1207**, Adj R² = **0.0534**, F-statistic = **1.79** (p = **0.0422**), Residual SE = **16.564** on **183** df, AIC = **1688.0**, BIC = **1737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.0881** | 21.0413 | ±42.0825 | **+6.325** | **2.53e-10** | *** |
| **Education: graduate level (vs college)** | **-5.6692** | 2.4911 | ±4.9823 | **-2.276** | **0.0229** | * |
| Education: high school or below (vs college) | +7.3492 | 4.5119 | ±9.0238 | +1.629 | 0.1033 |  |
| Site: UCSD (vs UAB) | +3.0216 | 3.2038 | ±6.4077 | +0.943 | 0.3456 |  |
| Site: UW (vs UAB) | -0.2128 | 3.3124 | ±6.6247 | -0.064 | 0.9488 |  |
| Season: spring (vs autumn) | -0.1035 | 3.5530 | ±7.1059 | -0.029 | 0.9768 |  |
| Season: summer (vs autumn) | +0.7801 | 4.1221 | ±8.2441 | +0.189 | 0.8499 |  |
| Season: winter (vs autumn) | +4.7166 | 4.2469 | ±8.4938 | +1.111 | 0.2667 |  |
| Age (years) | -0.2308 | 0.1290 | ±0.2579 | -1.790 | 0.0735 | . |
| BMI (kg/m2) | +0.1434 | 0.1667 | ±0.3334 | +0.860 | 0.3896 |  |
| Hypertension | +0.7496 | 2.6780 | ±5.3560 | +0.280 | 0.7796 |  |
| High cholesterol | -0.8715 | 2.4740 | ±4.9481 | -0.352 | 0.7246 |  |
| Kidney disease | -4.1663 | 3.7045 | ±7.4089 | -1.125 | 0.2607 |  |
| Circulatory disease | -0.3039 | 3.5633 | ±7.1266 | -0.085 | 0.9320 |  |
| HbA1c (%) | +0.4709 | 3.2948 | ±6.5897 | +0.143 | 0.8864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.1244**, Adj R² = **0.0575**, F-statistic = **1.86** (p = **0.0336**), Residual SE = **16.529** on **183** df, AIC = **1687.1**, BIC = **1736.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1537** | 15.3413 | ±30.6827 | **+8.158** | **3.41e-16** | *** |
| **Education: graduate level (vs college)** | **-5.6887** | 2.5132 | ±5.0263 | **-2.264** | **0.0236** | * |
| Education: high school or below (vs college) | +7.5741 | 4.3785 | ±8.7570 | +1.730 | 0.0837 | . |
| Site: UCSD (vs UAB) | +3.0359 | 3.2036 | ±6.4071 | +0.948 | 0.3433 |  |
| Site: UW (vs UAB) | -0.1277 | 3.3168 | ±6.6336 | -0.039 | 0.9693 |  |
| Season: spring (vs autumn) | -0.2020 | 3.6016 | ±7.2032 | -0.056 | 0.9553 |  |
| Season: summer (vs autumn) | +0.5028 | 4.0486 | ±8.0972 | +0.124 | 0.9012 |  |
| Season: winter (vs autumn) | +4.6091 | 4.1715 | ±8.3430 | +1.105 | 0.2692 |  |
| Age (years) | -0.2286 | 0.1290 | ±0.2580 | -1.773 | 0.0763 | . |
| BMI (kg/m2) | +0.1371 | 0.1777 | ±0.3553 | +0.772 | 0.4402 |  |
| Hypertension | +0.6189 | 2.6347 | ±5.2695 | +0.235 | 0.8143 |  |
| High cholesterol | -0.7367 | 2.5814 | ±5.1629 | -0.285 | 0.7754 |  |
| Kidney disease | -4.5028 | 3.7298 | ±7.4597 | -1.207 | 0.2273 |  |
| Circulatory disease | -0.3251 | 3.2826 | ±6.5651 | -0.099 | 0.9211 |  |
| Mean glucose (mg/dL) | +0.0860 | 0.1046 | ±0.2092 | +0.822 | 0.4109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.1244**, Adj R² = **0.0575**, F-statistic = **1.86** (p = **0.0336**), Residual SE = **16.529** on **183** df, AIC = **1687.1**, BIC = **1736.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+113.2540** | 27.4362 | ±54.8725 | **+4.128** | **3.66e-05** | *** |
| **Education: graduate level (vs college)** | **-5.6887** | 2.5132 | ±5.0263 | **-2.264** | **0.0236** | * |
| Education: high school or below (vs college) | +7.5741 | 4.3785 | ±8.7570 | +1.730 | 0.0837 | . |
| Site: UCSD (vs UAB) | +3.0359 | 3.2036 | ±6.4071 | +0.948 | 0.3433 |  |
| Site: UW (vs UAB) | -0.1277 | 3.3168 | ±6.6336 | -0.039 | 0.9693 |  |
| Season: spring (vs autumn) | -0.2020 | 3.6016 | ±7.2032 | -0.056 | 0.9553 |  |
| Season: summer (vs autumn) | +0.5028 | 4.0486 | ±8.0972 | +0.124 | 0.9012 |  |
| Season: winter (vs autumn) | +4.6091 | 4.1715 | ±8.3430 | +1.105 | 0.2692 |  |
| Age (years) | -0.2286 | 0.1290 | ±0.2580 | -1.773 | 0.0763 | . |
| BMI (kg/m2) | +0.1371 | 0.1777 | ±0.3553 | +0.772 | 0.4402 |  |
| Hypertension | +0.6189 | 2.6347 | ±5.2695 | +0.235 | 0.8143 |  |
| High cholesterol | -0.7367 | 2.5814 | ±5.1629 | -0.285 | 0.7754 |  |
| Kidney disease | -4.5028 | 3.7298 | ±7.4597 | -1.207 | 0.2273 |  |
| Circulatory disease | -0.3251 | 3.2826 | ±6.5651 | -0.099 | 0.9211 |  |
| GMI (%) | +3.5951 | 4.3724 | ±8.7448 | +0.822 | 0.4109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.1209**, Adj R² = **0.0536**, F-statistic = **1.80** (p = **0.0417**), Residual SE = **16.562** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6290** | 15.4452 | ±30.8903 | **+8.587** | **8.92e-18** | *** |
| **Education: graduate level (vs college)** | **-5.7129** | 2.5270 | ±5.0540 | **-2.261** | **0.0238** | * |
| Education: high school or below (vs college) | +7.4114 | 4.4091 | ±8.8182 | +1.681 | 0.0928 | . |
| Site: UCSD (vs UAB) | +3.0014 | 3.2125 | ±6.4251 | +0.934 | 0.3502 |  |
| Site: UW (vs UAB) | -0.2130 | 3.3085 | ±6.6171 | -0.064 | 0.9487 |  |
| Season: spring (vs autumn) | -0.1230 | 3.5893 | ±7.1785 | -0.034 | 0.9727 |  |
| Season: summer (vs autumn) | +0.7629 | 4.0060 | ±8.0120 | +0.190 | 0.8490 |  |
| Season: winter (vs autumn) | +4.7482 | 4.1173 | ±8.2347 | +1.153 | 0.2488 |  |
| Age (years) | -0.2270 | 0.1296 | ±0.2591 | -1.752 | 0.0797 | . |
| BMI (kg/m2) | +0.1451 | 0.1807 | ±0.3614 | +0.803 | 0.4218 |  |
| Hypertension | +0.7486 | 2.6594 | ±5.3189 | +0.281 | 0.7783 |  |
| High cholesterol | -0.8330 | 2.5637 | ±5.1273 | -0.325 | 0.7452 |  |
| Kidney disease | -4.2494 | 3.7081 | ±7.4163 | -1.146 | 0.2518 |  |
| Circulatory disease | -0.2628 | 3.2600 | ±6.5200 | -0.081 | 0.9358 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0236 | 0.0922 | ±0.1844 | +0.256 | 0.7982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1265**, Adj R² = **0.0597**, F-statistic = **1.89** (p = **0.0295**), Residual SE = **16.509** on **183** df, AIC = **1686.6**, BIC = **1736.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.6635** | 10.6649 | ±21.3297 | **+12.158** | **5.20e-34** | *** |
| **Education: graduate level (vs college)** | **-5.8837** | 2.5388 | ±5.0775 | **-2.318** | **0.0205** | * |
| Education: high school or below (vs college) | +6.5977 | 4.7201 | ±9.4402 | +1.398 | 0.1622 |  |
| Site: UCSD (vs UAB) | +3.2884 | 3.2695 | ±6.5390 | +1.006 | 0.3145 |  |
| Site: UW (vs UAB) | +0.3185 | 3.3736 | ±6.7472 | +0.094 | 0.9248 |  |
| Season: spring (vs autumn) | -0.1019 | 3.5340 | ±7.0681 | -0.029 | 0.9770 |  |
| Season: summer (vs autumn) | +0.8698 | 3.8727 | ±7.7455 | +0.225 | 0.8223 |  |
| Season: winter (vs autumn) | +4.7649 | 4.0812 | ±8.1623 | +1.168 | 0.2430 |  |
| Age (years) | -0.2413 | 0.1334 | ±0.2668 | -1.809 | 0.0705 | . |
| BMI (kg/m2) | +0.1537 | 0.1803 | ±0.3606 | +0.853 | 0.3939 |  |
| Hypertension | +0.2667 | 2.6108 | ±5.2217 | +0.102 | 0.9186 |  |
| High cholesterol | -0.6173 | 2.5673 | ±5.1347 | -0.240 | 0.8100 |  |
| Kidney disease | -4.8615 | 3.7119 | ±7.4238 | -1.310 | 0.1903 |  |
| Circulatory disease | -0.4218 | 3.2884 | ±6.5768 | -0.128 | 0.8979 |  |
| Glucose SD, pooled (mg/dL) | +0.3069 | 0.2993 | ±0.5987 | +1.025 | 0.3053 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1276**, Adj R² = **0.0609**, F-statistic = **1.91** (p = **0.0276**), Residual SE = **16.499** on **183** df, AIC = **1686.4**, BIC = **1735.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.6827** | 10.3636 | ±20.7272 | **+12.513** | **6.31e-36** | *** |
| **Education: graduate level (vs college)** | **-5.8671** | 2.5250 | ±5.0501 | **-2.324** | **0.0201** | * |
| Education: high school or below (vs college) | +6.6796 | 4.5789 | ±9.1579 | +1.459 | 0.1446 |  |
| Site: UCSD (vs UAB) | +3.1233 | 3.2193 | ±6.4385 | +0.970 | 0.3320 |  |
| Site: UW (vs UAB) | +0.1954 | 3.3381 | ±6.6763 | +0.059 | 0.9533 |  |
| Season: spring (vs autumn) | +0.0111 | 3.4973 | ±6.9946 | +0.003 | 0.9975 |  |
| Season: summer (vs autumn) | +0.9925 | 3.8282 | ±7.6564 | +0.259 | 0.7954 |  |
| Season: winter (vs autumn) | +4.8351 | 4.0592 | ±8.1184 | +1.191 | 0.2336 |  |
| Age (years) | -0.2430 | 0.1337 | ±0.2674 | -1.818 | 0.0691 | . |
| BMI (kg/m2) | +0.1543 | 0.1799 | ±0.3597 | +0.858 | 0.3911 |  |
| Hypertension | +0.0877 | 2.6017 | ±5.2033 | +0.034 | 0.9731 |  |
| High cholesterol | -0.5891 | 2.5660 | ±5.1319 | -0.230 | 0.8184 |  |
| Kidney disease | -4.7186 | 3.6785 | ±7.3569 | -1.283 | 0.1996 |  |
| Circulatory disease | -0.2727 | 3.2550 | ±6.5101 | -0.084 | 0.9332 |  |
| Avg. daily SD (mg/dL) | +0.3383 | 0.2845 | ±0.5689 | +1.189 | 0.2344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.1236**, Adj R² = **0.0566**, F-statistic = **1.84** (p = **0.0354**), Residual SE = **16.537** on **183** df, AIC = **1687.3**, BIC = **1736.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.3668** | 10.6387 | ±21.2774 | **+12.254** | **1.60e-34** | *** |
| **Education: graduate level (vs college)** | **-5.8445** | 2.5233 | ±5.0466 | **-2.316** | **0.0205** | * |
| Education: high school or below (vs college) | +6.5852 | 4.7352 | ±9.4705 | +1.391 | 0.1643 |  |
| Site: UCSD (vs UAB) | +3.2466 | 3.2848 | ±6.5695 | +0.988 | 0.3230 |  |
| Site: UW (vs UAB) | +0.1915 | 3.3615 | ±6.7229 | +0.057 | 0.9546 |  |
| Season: spring (vs autumn) | -0.0692 | 3.5311 | ±7.0622 | -0.020 | 0.9844 |  |
| Season: summer (vs autumn) | +1.0349 | 3.8401 | ±7.6802 | +0.269 | 0.7876 |  |
| Season: winter (vs autumn) | +4.8057 | 4.0713 | ±8.1426 | +1.180 | 0.2379 |  |
| Age (years) | -0.2408 | 0.1332 | ±0.2664 | -1.808 | 0.0707 | . |
| BMI (kg/m2) | +0.1602 | 0.1797 | ±0.3593 | +0.892 | 0.3727 |  |
| Hypertension | +0.4129 | 2.6490 | ±5.2979 | +0.156 | 0.8761 |  |
| High cholesterol | -0.6940 | 2.5443 | ±5.0886 | -0.273 | 0.7850 |  |
| Kidney disease | -4.6419 | 3.6767 | ±7.3534 | -1.263 | 0.2068 |  |
| Circulatory disease | -0.2988 | 3.2618 | ±6.5235 | -0.092 | 0.9270 |  |
| CV (%) | +0.3296 | 0.3743 | ±0.7486 | +0.880 | 0.3786 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.1284**, Adj R² = **0.0617**, F-statistic = **1.93** (p = **0.0262**), Residual SE = **16.491** on **183** df, AIC = **1686.2**, BIC = **1735.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+144.9412** | 14.8741 | ±29.7482 | **+9.745** | **1.95e-22** | *** |
| **Education: graduate level (vs college)** | **-5.8900** | 2.5180 | ±5.0361 | **-2.339** | **0.0193** | * |
| Education: high school or below (vs college) | +6.2683 | 4.6556 | ±9.3112 | +1.346 | 0.1782 |  |
| Site: UCSD (vs UAB) | +3.2974 | 3.2354 | ±6.4708 | +1.019 | 0.3081 |  |
| Site: UW (vs UAB) | +0.3538 | 3.3501 | ±6.7001 | +0.106 | 0.9159 |  |
| Season: spring (vs autumn) | -0.0485 | 3.5164 | ±7.0327 | -0.014 | 0.9890 |  |
| Season: summer (vs autumn) | +1.1181 | 3.8611 | ±7.7223 | +0.290 | 0.7721 |  |
| Season: winter (vs autumn) | +4.8048 | 4.0653 | ±8.1305 | +1.182 | 0.2372 |  |
| Age (years) | -0.2475 | 0.1323 | ±0.2646 | -1.870 | 0.0614 | . |
| BMI (kg/m2) | +0.1560 | 0.1798 | ±0.3596 | +0.868 | 0.3856 |  |
| Hypertension | +0.1728 | 2.6309 | ±5.2617 | +0.066 | 0.9476 |  |
| High cholesterol | -0.6880 | 2.5367 | ±5.0734 | -0.271 | 0.7862 |  |
| Kidney disease | -4.8552 | 3.6727 | ±7.3454 | -1.322 | 0.1862 |  |
| Circulatory disease | -0.2630 | 3.2480 | ±6.4961 | -0.081 | 0.9355 |  |
| Mean / SD ratio | -1.3653 | 0.9275 | ±1.8550 | -1.472 | 0.1410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1298**, Adj R² = **0.0632**, F-statistic = **1.95** (p = **0.0240**), Residual SE = **16.478** on **183** df, AIC = **1685.9**, BIC = **1735.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+144.8233** | 14.1236 | ±28.2473 | **+10.254** | **1.14e-24** | *** |
| **Education: graduate level (vs college)** | **-5.7987** | 2.5041 | ±5.0082 | **-2.316** | **0.0206** | * |
| Education: high school or below (vs college) | +6.4496 | 4.5141 | ±9.0283 | +1.429 | 0.1531 |  |
| Site: UCSD (vs UAB) | +2.9858 | 3.1840 | ±6.3681 | +0.938 | 0.3484 |  |
| Site: UW (vs UAB) | +0.2088 | 3.3150 | ±6.6300 | +0.063 | 0.9498 |  |
| Season: spring (vs autumn) | +0.0151 | 3.5159 | ±7.0318 | +0.004 | 0.9966 |  |
| Season: summer (vs autumn) | +1.2249 | 3.8520 | ±7.7040 | +0.318 | 0.7505 |  |
| Season: winter (vs autumn) | +4.9576 | 4.0504 | ±8.1008 | +1.224 | 0.2210 |  |
| Age (years) | -0.2503 | 0.1322 | ±0.2643 | -1.894 | 0.0582 | . |
| BMI (kg/m2) | +0.1540 | 0.1791 | ±0.3582 | +0.860 | 0.3899 |  |
| Hypertension | -0.0824 | 2.6343 | ±5.2685 | -0.031 | 0.9750 |  |
| High cholesterol | -0.7558 | 2.5343 | ±5.0686 | -0.298 | 0.7655 |  |
| Kidney disease | -4.7114 | 3.6687 | ±7.3374 | -1.284 | 0.1991 |  |
| Circulatory disease | +0.0327 | 3.2284 | ±6.4568 | +0.010 | 0.9919 |  |
| Avg. daily mean/SD | -1.1312 | 0.6498 | ±1.2996 | -1.741 | 0.0817 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.1214**, Adj R² = **0.0542**, F-statistic = **1.81** (p = **0.0404**), Residual SE = **16.557** on **183** df, AIC = **1687.8**, BIC = **1737.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6769** | 13.4891 | ±26.9783 | **+9.836** | **7.89e-23** | *** |
| **Education: graduate level (vs college)** | **-5.7078** | 2.5149 | ±5.0297 | **-2.270** | **0.0232** | * |
| Education: high school or below (vs college) | +7.2308 | 4.5468 | ±9.0936 | +1.590 | 0.1118 |  |
| Site: UCSD (vs UAB) | +3.0121 | 3.2054 | ±6.4107 | +0.940 | 0.3474 |  |
| Site: UW (vs UAB) | -0.1485 | 3.2778 | ±6.5556 | -0.045 | 0.9639 |  |
| Season: spring (vs autumn) | -0.0947 | 3.5541 | ±7.1082 | -0.027 | 0.9787 |  |
| Season: summer (vs autumn) | +0.8580 | 3.8531 | ±7.7062 | +0.223 | 0.8238 |  |
| Season: winter (vs autumn) | +4.7876 | 4.0810 | ±8.1621 | +1.173 | 0.2407 |  |
| Age (years) | -0.2289 | 0.1289 | ±0.2578 | -1.776 | 0.0758 | . |
| BMI (kg/m2) | +0.1481 | 0.1784 | ±0.3568 | +0.830 | 0.4063 |  |
| Hypertension | +0.6920 | 2.6833 | ±5.3666 | +0.258 | 0.7965 |  |
| High cholesterol | -0.8714 | 2.5282 | ±5.0563 | -0.345 | 0.7303 |  |
| Kidney disease | -4.2313 | 3.7045 | ±7.4089 | -1.142 | 0.2534 |  |
| Circulatory disease | -0.1085 | 3.2168 | ±6.4335 | -0.034 | 0.9731 |  |
| MAG (mg/dL/h) | +0.0812 | 0.2016 | ±0.4032 | +0.403 | 0.6870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.1219**, Adj R² = **0.0547**, F-statistic = **1.81** (p = **0.0392**), Residual SE = **16.552** on **183** df, AIC = **1687.7**, BIC = **1737.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.1885** | 11.0434 | ±22.0868 | **+11.970** | **5.11e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7289** | 2.5179 | ±5.0357 | **-2.275** | **0.0229** | * |
| Education: high school or below (vs college) | +7.1238 | 4.5532 | ±9.1064 | +1.565 | 0.1177 |  |
| Site: UCSD (vs UAB) | +3.1052 | 3.2392 | ±6.4784 | +0.959 | 0.3377 |  |
| Site: UW (vs UAB) | -0.0446 | 3.2989 | ±6.5978 | -0.014 | 0.9892 |  |
| Season: spring (vs autumn) | -0.0905 | 3.5501 | ±7.1003 | -0.026 | 0.9797 |  |
| Season: summer (vs autumn) | +0.9270 | 3.8070 | ±7.6139 | +0.244 | 0.8076 |  |
| Season: winter (vs autumn) | +4.8119 | 4.0625 | ±8.1251 | +1.184 | 0.2362 |  |
| Age (years) | -0.2365 | 0.1340 | ±0.2679 | -1.765 | 0.0775 | . |
| BMI (kg/m2) | +0.1571 | 0.1818 | ±0.3635 | +0.864 | 0.3874 |  |
| Hypertension | +0.5436 | 2.6461 | ±5.2921 | +0.205 | 0.8372 |  |
| High cholesterol | -0.7760 | 2.5771 | ±5.1541 | -0.301 | 0.7633 |  |
| Kidney disease | -4.3716 | 3.7015 | ±7.4030 | -1.181 | 0.2376 |  |
| Circulatory disease | -0.1908 | 3.2603 | ±6.5206 | -0.059 | 0.9533 |  |
| Avg. daily range (mg/dL) | +0.0373 | 0.0704 | ±0.1408 | +0.530 | 0.5960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.1301**, Adj R² = **0.0636**, F-statistic = **1.96** (p = **0.0235**), Residual SE = **16.475** on **183** df, AIC = **1685.8**, BIC = **1735.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.2293** | 11.5171 | ±23.0342 | **+11.394** | **4.47e-30** | *** |
| **Education: graduate level (vs college)** | **-5.8948** | 2.5502 | ±5.1003 | **-2.312** | **0.0208** | * |
| Education: high school or below (vs college) | +6.4044 | 4.9685 | ±9.9370 | +1.289 | 0.1974 |  |
| Site: UCSD (vs UAB) | +3.7634 | 3.3089 | ±6.6179 | +1.137 | 0.2554 |  |
| Site: UW (vs UAB) | +0.6355 | 3.4419 | ±6.8838 | +0.185 | 0.8535 |  |
| Season: spring (vs autumn) | -0.4531 | 3.6165 | ±7.2330 | -0.125 | 0.9003 |  |
| Season: summer (vs autumn) | +0.1705 | 4.1957 | ±8.3915 | +0.041 | 0.9676 |  |
| Season: winter (vs autumn) | +4.7105 | 4.0697 | ±8.1393 | +1.157 | 0.2471 |  |
| Age (years) | -0.2346 | 0.1290 | ±0.2580 | -1.819 | 0.0690 | . |
| BMI (kg/m2) | +0.1487 | 0.1790 | ±0.3580 | +0.831 | 0.4062 |  |
| Hypertension | +1.0632 | 2.6750 | ±5.3500 | +0.397 | 0.6910 |  |
| High cholesterol | -0.9296 | 2.5201 | ±5.0402 | -0.369 | 0.7122 |  |
| Kidney disease | -5.1763 | 3.8434 | ±7.6868 | -1.347 | 0.1780 |  |
| Circulatory disease | -1.1855 | 3.3426 | ±6.6853 | -0.355 | 0.7228 |  |
| SD of daily means (mg/dL) | +0.7219 | 0.6744 | ±1.3489 | +1.070 | 0.2844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.1229**, Adj R² = **0.0558**, F-statistic = **1.83** (p = **0.0369**), Residual SE = **16.543** on **183** df, AIC = **1687.5**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+154.0705** | 40.2900 | ±80.5801 | **+3.824** | **1.31e-04** | *** |
| **Education: graduate level (vs college)** | **-5.7973** | 2.5611 | ±5.1222 | **-2.264** | **0.0236** | * |
| Education: high school or below (vs college) | +7.1359 | 4.5859 | ±9.1718 | +1.556 | 0.1197 |  |
| Site: UCSD (vs UAB) | +3.1823 | 3.2875 | ±6.5751 | +0.968 | 0.3331 |  |
| Site: UW (vs UAB) | -0.0513 | 3.3602 | ±6.7204 | -0.015 | 0.9878 |  |
| Season: spring (vs autumn) | -0.0975 | 3.5607 | ±7.1214 | -0.027 | 0.9782 |  |
| Season: summer (vs autumn) | +0.7040 | 4.0192 | ±8.0383 | +0.175 | 0.8609 |  |
| Season: winter (vs autumn) | +4.6781 | 4.1898 | ±8.3797 | +1.117 | 0.2642 |  |
| Age (years) | -0.2397 | 0.1368 | ±0.2737 | -1.751 | 0.0799 | . |
| BMI (kg/m2) | +0.1480 | 0.1802 | ±0.3604 | +0.821 | 0.4116 |  |
| Hypertension | +0.6599 | 2.6398 | ±5.2796 | +0.250 | 0.8026 |  |
| High cholesterol | -0.7136 | 2.5933 | ±5.1866 | -0.275 | 0.7832 |  |
| Kidney disease | -4.6160 | 3.8388 | ±7.6776 | -1.202 | 0.2292 |  |
| Circulatory disease | -0.3050 | 3.3065 | ±6.6131 | -0.092 | 0.9265 |  |
| Time in range 70-180, pooled (%) | -0.1850 | 0.3538 | ±0.7077 | -0.523 | 0.6011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.1226**, Adj R² = **0.0555**, F-statistic = **1.83** (p = **0.0375**), Residual SE = **16.546** on **183** df, AIC = **1687.5**, BIC = **1736.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+153.4531** | 41.0295 | ±82.0589 | **+3.740** | **1.84e-04** | *** |
| **Education: graduate level (vs college)** | **-5.7805** | 2.5580 | ±5.1160 | **-2.260** | **0.0238** | * |
| Education: high school or below (vs college) | +7.1850 | 4.5511 | ±9.1021 | +1.579 | 0.1144 |  |
| Site: UCSD (vs UAB) | +3.1734 | 3.2874 | ±6.5749 | +0.965 | 0.3344 |  |
| Site: UW (vs UAB) | -0.0909 | 3.3614 | ±6.7227 | -0.027 | 0.9784 |  |
| Season: spring (vs autumn) | -0.0892 | 3.5519 | ±7.1038 | -0.025 | 0.9800 |  |
| Season: summer (vs autumn) | +0.7052 | 4.0197 | ±8.0393 | +0.175 | 0.8607 |  |
| Season: winter (vs autumn) | +4.6775 | 4.1940 | ±8.3880 | +1.115 | 0.2647 |  |
| Age (years) | -0.2394 | 0.1372 | ±0.2743 | -1.745 | 0.0809 | . |
| BMI (kg/m2) | +0.1492 | 0.1803 | ±0.3606 | +0.827 | 0.4080 |  |
| Hypertension | +0.6407 | 2.6271 | ±5.2541 | +0.244 | 0.8073 |  |
| High cholesterol | -0.7263 | 2.5934 | ±5.1869 | -0.280 | 0.7794 |  |
| Kidney disease | -4.6035 | 3.8448 | ±7.6896 | -1.197 | 0.2312 |  |
| Circulatory disease | -0.2955 | 3.3046 | ±6.6092 | -0.089 | 0.9288 |  |
| Avg. daily time in range 70-180 (%) | -0.1787 | 0.3609 | ±0.7219 | -0.495 | 0.6206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.1211**, Adj R² = **0.0538**, F-statistic = **1.80** (p = **0.0412**), Residual SE = **16.560** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4705** | 11.2172 | ±22.4345 | **+12.077** | **1.40e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6287** | 2.5005 | ±5.0010 | **-2.251** | **0.0244** | * |
| Education: high school or below (vs college) | +7.5566 | 4.4579 | ±8.9158 | +1.695 | 0.0901 | . |
| Site: UCSD (vs UAB) | +2.9419 | 3.2290 | ±6.4580 | +0.911 | 0.3622 |  |
| Site: UW (vs UAB) | -0.2426 | 3.3038 | ±6.6076 | -0.073 | 0.9415 |  |
| Season: spring (vs autumn) | -0.2324 | 3.6269 | ±7.2537 | -0.064 | 0.9489 |  |
| Season: summer (vs autumn) | +0.7717 | 3.8975 | ±7.7950 | +0.198 | 0.8431 |  |
| Season: winter (vs autumn) | +4.6239 | 4.1499 | ±8.2997 | +1.114 | 0.2652 |  |
| Age (years) | -0.2235 | 0.1313 | ±0.2626 | -1.702 | 0.0887 | . |
| BMI (kg/m2) | +0.1475 | 0.1794 | ±0.3588 | +0.822 | 0.4111 |  |
| Hypertension | +0.8051 | 2.6778 | ±5.3557 | +0.301 | 0.7637 |  |
| High cholesterol | -0.7683 | 2.5702 | ±5.1405 | -0.299 | 0.7650 |  |
| Kidney disease | -4.3027 | 3.7081 | ±7.4163 | -1.160 | 0.2459 |  |
| Circulatory disease | -0.1937 | 3.2516 | ±6.5032 | -0.060 | 0.9525 |  |
| Time 54-69, pooled (%) | -1.5724 | 4.1474 | ±8.2947 | -0.379 | 0.7046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.1206**, Adj R² = **0.0534**, F-statistic = **1.79** (p = **0.0423**), Residual SE = **16.564** on **183** df, AIC = **1688.0**, BIC = **1737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4959** | 11.2107 | ±22.4215 | **+12.086** | **1.25e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6593** | 2.5031 | ±5.0062 | **-2.261** | **0.0238** | * |
| Education: high school or below (vs college) | +7.4582 | 4.4386 | ±8.8772 | +1.680 | 0.0929 | . |
| Site: UCSD (vs UAB) | +2.9980 | 3.2083 | ±6.4166 | +0.934 | 0.3501 |  |
| Site: UW (vs UAB) | -0.2176 | 3.2962 | ±6.5924 | -0.066 | 0.9474 |  |
| Season: spring (vs autumn) | -0.1751 | 3.6145 | ±7.2290 | -0.048 | 0.9614 |  |
| Season: summer (vs autumn) | +0.7859 | 3.9234 | ±7.8469 | +0.200 | 0.8412 |  |
| Season: winter (vs autumn) | +4.6916 | 4.1439 | ±8.2877 | +1.132 | 0.2576 |  |
| Age (years) | -0.2268 | 0.1314 | ±0.2629 | -1.725 | 0.0845 | . |
| BMI (kg/m2) | +0.1493 | 0.1796 | ±0.3591 | +0.831 | 0.4057 |  |
| Hypertension | +0.7952 | 2.6814 | ±5.3628 | +0.297 | 0.7668 |  |
| High cholesterol | -0.7964 | 2.5649 | ±5.1298 | -0.310 | 0.7562 |  |
| Kidney disease | -4.2823 | 3.7205 | ±7.4410 | -1.151 | 0.2497 |  |
| Circulatory disease | -0.2159 | 3.2672 | ±6.5344 | -0.066 | 0.9473 |  |
| Avg. daily time 54-69 (%) | -0.7546 | 3.6930 | ±7.3860 | -0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.1211**, Adj R² = **0.0538**, F-statistic = **1.80** (p = **0.0412**), Residual SE = **16.560** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4705** | 11.2172 | ±22.4345 | **+12.077** | **1.40e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6287** | 2.5005 | ±5.0010 | **-2.251** | **0.0244** | * |
| Education: high school or below (vs college) | +7.5566 | 4.4579 | ±8.9158 | +1.695 | 0.0901 | . |
| Site: UCSD (vs UAB) | +2.9419 | 3.2290 | ±6.4580 | +0.911 | 0.3622 |  |
| Site: UW (vs UAB) | -0.2426 | 3.3038 | ±6.6076 | -0.073 | 0.9415 |  |
| Season: spring (vs autumn) | -0.2324 | 3.6269 | ±7.2537 | -0.064 | 0.9489 |  |
| Season: summer (vs autumn) | +0.7717 | 3.8975 | ±7.7950 | +0.198 | 0.8431 |  |
| Season: winter (vs autumn) | +4.6239 | 4.1499 | ±8.2997 | +1.114 | 0.2652 |  |
| Age (years) | -0.2235 | 0.1313 | ±0.2626 | -1.702 | 0.0887 | . |
| BMI (kg/m2) | +0.1475 | 0.1794 | ±0.3588 | +0.822 | 0.4111 |  |
| Hypertension | +0.8051 | 2.6778 | ±5.3557 | +0.301 | 0.7637 |  |
| High cholesterol | -0.7683 | 2.5702 | ±5.1405 | -0.299 | 0.7650 |  |
| Kidney disease | -4.3027 | 3.7081 | ±7.4163 | -1.160 | 0.2459 |  |
| Circulatory disease | -0.1937 | 3.2516 | ±6.5032 | -0.060 | 0.9525 |  |
| Time < 70 (%) | -1.5724 | 4.1474 | ±8.2947 | -0.379 | 0.7046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.1206**, Adj R² = **0.0534**, F-statistic = **1.79** (p = **0.0423**), Residual SE = **16.564** on **183** df, AIC = **1688.0**, BIC = **1737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4959** | 11.2107 | ±22.4215 | **+12.086** | **1.25e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6593** | 2.5031 | ±5.0062 | **-2.261** | **0.0238** | * |
| Education: high school or below (vs college) | +7.4582 | 4.4386 | ±8.8772 | +1.680 | 0.0929 | . |
| Site: UCSD (vs UAB) | +2.9980 | 3.2083 | ±6.4166 | +0.934 | 0.3501 |  |
| Site: UW (vs UAB) | -0.2176 | 3.2962 | ±6.5924 | -0.066 | 0.9474 |  |
| Season: spring (vs autumn) | -0.1751 | 3.6145 | ±7.2290 | -0.048 | 0.9614 |  |
| Season: summer (vs autumn) | +0.7859 | 3.9234 | ±7.8469 | +0.200 | 0.8412 |  |
| Season: winter (vs autumn) | +4.6916 | 4.1439 | ±8.2877 | +1.132 | 0.2576 |  |
| Age (years) | -0.2268 | 0.1314 | ±0.2629 | -1.725 | 0.0845 | . |
| BMI (kg/m2) | +0.1493 | 0.1796 | ±0.3591 | +0.831 | 0.4057 |  |
| Hypertension | +0.7952 | 2.6814 | ±5.3628 | +0.297 | 0.7668 |  |
| High cholesterol | -0.7964 | 2.5649 | ±5.1298 | -0.310 | 0.7562 |  |
| Kidney disease | -4.2823 | 3.7205 | ±7.4410 | -1.151 | 0.2497 |  |
| Circulatory disease | -0.2159 | 3.2672 | ±6.5344 | -0.066 | 0.9473 |  |
| Avg. daily time < 70 (%) | -0.7546 | 3.6930 | ±7.3860 | -0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.1230**, Adj R² = **0.0559**, F-statistic = **1.83** (p = **0.0367**), Residual SE = **16.542** on **183** df, AIC = **1687.4**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5575** | 11.2787 | ±22.5575 | **+12.019** | **2.83e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7919** | 2.5590 | ±5.1181 | **-2.263** | **0.0236** | * |
| Education: high school or below (vs college) | +7.1549 | 4.5670 | ±9.1341 | +1.567 | 0.1172 |  |
| Site: UCSD (vs UAB) | +3.1757 | 3.2806 | ±6.5612 | +0.968 | 0.3330 |  |
| Site: UW (vs UAB) | -0.0514 | 3.3602 | ±6.7204 | -0.015 | 0.9878 |  |
| Season: spring (vs autumn) | -0.1109 | 3.5730 | ±7.1461 | -0.031 | 0.9753 |  |
| Season: summer (vs autumn) | +0.6943 | 4.0252 | ±8.0504 | +0.172 | 0.8631 |  |
| Season: winter (vs autumn) | +4.6618 | 4.2039 | ±8.4078 | +1.109 | 0.2675 |  |
| Age (years) | -0.2390 | 0.1360 | ±0.2721 | -1.757 | 0.0790 | . |
| BMI (kg/m2) | +0.1475 | 0.1801 | ±0.3602 | +0.819 | 0.4128 |  |
| Hypertension | +0.6631 | 2.6417 | ±5.2833 | +0.251 | 0.8018 |  |
| High cholesterol | -0.7054 | 2.5956 | ±5.1912 | -0.272 | 0.7858 |  |
| Kidney disease | -4.6291 | 3.8425 | ±7.6849 | -1.205 | 0.2283 |  |
| Circulatory disease | -0.3057 | 3.3052 | ±6.6105 | -0.092 | 0.9263 |  |
| Time 181-250, pooled (%) | +0.1877 | 0.3516 | ±0.7032 | +0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.1227**, Adj R² = **0.0555**, F-statistic = **1.83** (p = **0.0375**), Residual SE = **16.545** on **183** df, AIC = **1687.5**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5642** | 11.2700 | ±22.5399 | **+12.029** | **2.51e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7738** | 2.5554 | ±5.1108 | **-2.259** | **0.0239** | * |
| Education: high school or below (vs college) | +7.2064 | 4.5344 | ±9.0687 | +1.589 | 0.1120 |  |
| Site: UCSD (vs UAB) | +3.1685 | 3.2824 | ±6.5647 | +0.965 | 0.3344 |  |
| Site: UW (vs UAB) | -0.0904 | 3.3615 | ±6.7230 | -0.027 | 0.9785 |  |
| Season: spring (vs autumn) | -0.1027 | 3.5648 | ±7.1296 | -0.029 | 0.9770 |  |
| Season: summer (vs autumn) | +0.6933 | 4.0305 | ±8.0609 | +0.172 | 0.8634 |  |
| Season: winter (vs autumn) | +4.6636 | 4.2076 | ±8.4152 | +1.108 | 0.2677 |  |
| Age (years) | -0.2386 | 0.1362 | ±0.2725 | -1.751 | 0.0799 | . |
| BMI (kg/m2) | +0.1488 | 0.1802 | ±0.3604 | +0.826 | 0.4089 |  |
| Hypertension | +0.6481 | 2.6302 | ±5.2604 | +0.246 | 0.8054 |  |
| High cholesterol | -0.7202 | 2.5954 | ±5.1908 | -0.278 | 0.7814 |  |
| Kidney disease | -4.6129 | 3.8483 | ±7.6965 | -1.199 | 0.2306 |  |
| Circulatory disease | -0.2988 | 3.3053 | ±6.6105 | -0.090 | 0.9280 |  |
| Avg. daily time 181-250 (%) | +0.1783 | 0.3577 | ±0.7154 | +0.498 | 0.6182 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.1230**, Adj R² = **0.0559**, F-statistic = **1.83** (p = **0.0367**), Residual SE = **16.542** on **183** df, AIC = **1687.4**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5575** | 11.2787 | ±22.5575 | **+12.019** | **2.83e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7919** | 2.5590 | ±5.1181 | **-2.263** | **0.0236** | * |
| Education: high school or below (vs college) | +7.1549 | 4.5670 | ±9.1341 | +1.567 | 0.1172 |  |
| Site: UCSD (vs UAB) | +3.1757 | 3.2806 | ±6.5612 | +0.968 | 0.3330 |  |
| Site: UW (vs UAB) | -0.0514 | 3.3602 | ±6.7204 | -0.015 | 0.9878 |  |
| Season: spring (vs autumn) | -0.1109 | 3.5730 | ±7.1461 | -0.031 | 0.9753 |  |
| Season: summer (vs autumn) | +0.6943 | 4.0252 | ±8.0504 | +0.172 | 0.8631 |  |
| Season: winter (vs autumn) | +4.6618 | 4.2039 | ±8.4078 | +1.109 | 0.2675 |  |
| Age (years) | -0.2390 | 0.1360 | ±0.2721 | -1.757 | 0.0790 | . |
| BMI (kg/m2) | +0.1475 | 0.1801 | ±0.3602 | +0.819 | 0.4128 |  |
| Hypertension | +0.6631 | 2.6417 | ±5.2833 | +0.251 | 0.8018 |  |
| High cholesterol | -0.7054 | 2.5956 | ±5.1912 | -0.272 | 0.7858 |  |
| Kidney disease | -4.6291 | 3.8425 | ±7.6849 | -1.205 | 0.2283 |  |
| Circulatory disease | -0.3057 | 3.3052 | ±6.6105 | -0.092 | 0.9263 |  |
| Time > 180 (%) | +0.1877 | 0.3516 | ±0.7032 | +0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1227**, Adj R² = **0.0555**, F-statistic = **1.83** (p = **0.0375**), Residual SE = **16.545** on **183** df, AIC = **1687.5**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5642** | 11.2700 | ±22.5399 | **+12.029** | **2.51e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7738** | 2.5554 | ±5.1108 | **-2.259** | **0.0239** | * |
| Education: high school or below (vs college) | +7.2064 | 4.5344 | ±9.0687 | +1.589 | 0.1120 |  |
| Site: UCSD (vs UAB) | +3.1685 | 3.2824 | ±6.5647 | +0.965 | 0.3344 |  |
| Site: UW (vs UAB) | -0.0904 | 3.3615 | ±6.7230 | -0.027 | 0.9785 |  |
| Season: spring (vs autumn) | -0.1027 | 3.5648 | ±7.1296 | -0.029 | 0.9770 |  |
| Season: summer (vs autumn) | +0.6933 | 4.0305 | ±8.0609 | +0.172 | 0.8634 |  |
| Season: winter (vs autumn) | +4.6636 | 4.2076 | ±8.4152 | +1.108 | 0.2677 |  |
| Age (years) | -0.2386 | 0.1362 | ±0.2725 | -1.751 | 0.0799 | . |
| BMI (kg/m2) | +0.1488 | 0.1802 | ±0.3604 | +0.826 | 0.4089 |  |
| Hypertension | +0.6481 | 2.6302 | ±5.2604 | +0.246 | 0.8054 |  |
| High cholesterol | -0.7202 | 2.5954 | ±5.1908 | -0.278 | 0.7814 |  |
| Kidney disease | -4.6129 | 3.8483 | ±7.6965 | -1.199 | 0.2306 |  |
| Circulatory disease | -0.2988 | 3.3053 | ±6.6105 | -0.090 | 0.9280 |  |
| Avg. daily time > 180 (%) | +0.1783 | 0.3577 | ±0.7154 | +0.498 | 0.6182 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1209**, Adj R² = **0.0536**, F-statistic = **1.80** (p = **0.0417**), Residual SE = **16.562** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5640** | 11.2799 | ±22.5598 | **+12.018** | **2.85e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6670** | 2.5095 | ±5.0189 | **-2.258** | **0.0239** | * |
| Education: high school or below (vs college) | +7.5154 | 4.6878 | ±9.3756 | +1.603 | 0.1089 |  |
| Site: UCSD (vs UAB) | +2.8959 | 3.3825 | ±6.7649 | +0.856 | 0.3919 |  |
| Site: UW (vs UAB) | -0.3363 | 3.4553 | ±6.9106 | -0.097 | 0.9225 |  |
| Season: spring (vs autumn) | -0.0813 | 3.6111 | ±7.2222 | -0.023 | 0.9820 |  |
| Season: summer (vs autumn) | +0.9237 | 4.0004 | ±8.0008 | +0.231 | 0.8174 |  |
| Season: winter (vs autumn) | +4.7749 | 4.1307 | ±8.2614 | +1.156 | 0.2477 |  |
| Age (years) | -0.2290 | 0.1305 | ±0.2609 | -1.755 | 0.0792 | . |
| BMI (kg/m2) | +0.1553 | 0.1827 | ±0.3653 | +0.850 | 0.3951 |  |
| Hypertension | +0.7023 | 2.7336 | ±5.4672 | +0.257 | 0.7972 |  |
| High cholesterol | -0.8188 | 2.5676 | ±5.1353 | -0.319 | 0.7498 |  |
| Kidney disease | -4.0795 | 3.8070 | ±7.6141 | -1.072 | 0.2839 |  |
| Circulatory disease | -0.1407 | 3.2407 | ±6.4813 | -0.043 | 0.9654 |  |
| Nocturnal time > 180 (%) | -0.0690 | 0.2624 | ±0.5249 | -0.263 | 0.7925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
