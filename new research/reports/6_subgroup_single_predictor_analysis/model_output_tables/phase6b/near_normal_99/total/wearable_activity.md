# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Total analysis base - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 401; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1291**, F-statistic = **6.93** (p = **5.17e-10**), Residual SE = **3608.410** on **390** df, AIC = **7718.0**, BIC = **7762.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19101.4172** | 1443.8136 | ±2887.6271 | **+13.230** | **5.90e-40** | *** |
| **Education: graduate level (vs college)** | **-812.1959** | 369.3449 | ±738.6898 | **-2.199** | **0.0279** | * |
| Education: high school or below (vs college) | +579.0916 | 857.3039 | ±1714.6078 | +0.675 | 0.4994 |  |
| Site: UCSD (vs UAB) | -348.0806 | 496.0577 | ±992.1153 | -0.702 | 0.4829 |  |
| Site: UW (vs UAB) | -845.5695 | 456.1415 | ±912.2830 | -1.854 | 0.0638 | . |
| **Age (years)** | **-113.0683** | 19.0635 | ±38.1271 | **-5.931** | **3.01e-09** | *** |
| **BMI (kg/m2)** | **-55.6804** | 24.5643 | ±49.1287 | **-2.267** | **0.0234** | * |
| Hypertension | +795.5484 | 450.6364 | ±901.2728 | +1.765 | 0.0775 | . |
| High cholesterol | -420.9695 | 388.7029 | ±777.4058 | -1.083 | 0.2788 |  |
| Kidney disease | -582.1246 | 756.8236 | ±1513.6473 | -0.769 | 0.4418 |  |
| Circulatory disease | -981.1135 | 643.0391 | ±1286.0782 | -1.526 | 0.1271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **401**, R² = **0.1538**, Adj R² = **0.1299**, F-statistic = **6.43** (p = **7.89e-10**), Residual SE = **3606.812** on **389** df, AIC = **7718.7**, BIC = **7766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15371.8000** | 3444.4295 | ±6888.8591 | **+4.463** | **8.09e-06** | *** |
| **Education: graduate level (vs college)** | **-789.8550** | 368.6381 | ±737.2762 | **-2.143** | **0.0321** | * |
| Education: high school or below (vs college) | +536.7820 | 859.3253 | ±1718.6507 | +0.625 | 0.5322 |  |
| Site: UCSD (vs UAB) | -316.4580 | 495.5244 | ±991.0489 | -0.639 | 0.5231 |  |
| Site: UW (vs UAB) | -809.5543 | 455.6139 | ±911.2279 | -1.777 | 0.0756 | . |
| **Age (years)** | **-115.1302** | 19.3007 | ±38.6014 | **-5.965** | **2.45e-09** | *** |
| **BMI (kg/m2)** | **-59.0868** | 23.9197 | ±47.8394 | **-2.470** | **0.0135** | * |
| Hypertension | +755.8718 | 450.5498 | ±901.0996 | +1.678 | 0.0934 | . |
| High cholesterol | -528.6720 | 396.5169 | ±793.0338 | -1.333 | 0.1824 |  |
| Kidney disease | -521.7083 | 766.3973 | ±1532.7946 | -0.681 | 0.4960 |  |
| Circulatory disease | -954.0728 | 645.0540 | ±1290.1080 | -1.479 | 0.1391 |  |
| HbA1c (%) | +718.0817 | 600.2386 | ±1200.4772 | +1.196 | 0.2316 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **401**, R² = **0.1513**, Adj R² = **0.1273**, F-statistic = **6.30** (p = **1.32e-09**), Residual SE = **3612.228** on **389** df, AIC = **7719.9**, BIC = **7767.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17940.4760** | 3295.8092 | ±6591.6185 | **+5.443** | **5.23e-08** | *** |
| **Education: graduate level (vs college)** | **-807.1641** | 369.7909 | ±739.5817 | **-2.183** | **0.0291** | * |
| Education: high school or below (vs college) | +593.3343 | 859.5789 | ±1719.1579 | +0.690 | 0.4900 |  |
| Site: UCSD (vs UAB) | -357.3731 | 498.3359 | ±996.6718 | -0.717 | 0.4733 |  |
| Site: UW (vs UAB) | -856.1279 | 459.0762 | ±918.1524 | -1.865 | 0.0622 | . |
| **Age (years)** | **-112.7654** | 19.1042 | ±38.2085 | **-5.903** | **3.58e-09** | *** |
| **BMI (kg/m2)** | **-56.4131** | 24.5127 | ±49.0254 | **-2.301** | **0.0214** | * |
| Hypertension | +781.9682 | 452.1798 | ±904.3596 | +1.729 | 0.0837 | . |
| High cholesterol | -415.6585 | 391.3484 | ±782.6968 | -1.062 | 0.2882 |  |
| Kidney disease | -582.8490 | 767.7277 | ±1535.4554 | -0.759 | 0.4477 |  |
| Circulatory disease | -984.9572 | 645.1277 | ±1290.2553 | -1.527 | 0.1268 |  |
| Mean glucose (mg/dL) | +10.2502 | 26.1080 | ±52.2160 | +0.393 | 0.6946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **401**, R² = **0.1513**, Adj R² = **0.1273**, F-statistic = **6.30** (p = **1.32e-09**), Residual SE = **3612.228** on **389** df, AIC = **7719.9**, BIC = **7767.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16522.0736** | 6731.2193 | ±13462.4386 | **+2.455** | **0.0141** | * |
| **Education: graduate level (vs college)** | **-807.1641** | 369.7909 | ±739.5817 | **-2.183** | **0.0291** | * |
| Education: high school or below (vs college) | +593.3343 | 859.5789 | ±1719.1579 | +0.690 | 0.4900 |  |
| Site: UCSD (vs UAB) | -357.3731 | 498.3359 | ±996.6718 | -0.717 | 0.4733 |  |
| Site: UW (vs UAB) | -856.1279 | 459.0762 | ±918.1524 | -1.865 | 0.0622 | . |
| **Age (years)** | **-112.7654** | 19.1042 | ±38.2085 | **-5.903** | **3.58e-09** | *** |
| **BMI (kg/m2)** | **-56.4131** | 24.5127 | ±49.0254 | **-2.301** | **0.0214** | * |
| Hypertension | +781.9682 | 452.1798 | ±904.3596 | +1.729 | 0.0837 | . |
| High cholesterol | -415.6585 | 391.3484 | ±782.6968 | -1.062 | 0.2882 |  |
| Kidney disease | -582.8490 | 767.7277 | ±1535.4554 | -0.759 | 0.4477 |  |
| Circulatory disease | -984.9572 | 645.1277 | ±1290.2553 | -1.527 | 0.1268 |  |
| GMI (%) | +428.5203 | 1091.4721 | ±2182.9442 | +0.393 | 0.6946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **401**, R² = **0.1561**, Adj R² = **0.1322**, F-statistic = **6.54** (p = **5.03e-10**), Residual SE = **3602.059** on **389** df, AIC = **7717.6**, BIC = **7765.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15639.1422** | 2811.5559 | ±5623.1118 | **+5.562** | **2.66e-08** | *** |
| **Education: graduate level (vs college)** | **-776.7281** | 370.8631 | ±741.7263 | **-2.094** | **0.0362** | * |
| Education: high school or below (vs college) | +627.4198 | 857.7357 | ±1715.4714 | +0.731 | 0.4645 |  |
| Site: UCSD (vs UAB) | -422.1595 | 493.4946 | ±986.9892 | -0.855 | 0.3923 |  |
| **Site: UW (vs UAB)** | **-902.8418** | 452.1841 | ±904.3681 | **-1.997** | **0.0459** | * |
| **Age (years)** | **-108.6941** | 19.5353 | ±39.0707 | **-5.564** | **2.64e-08** | *** |
| **BMI (kg/m2)** | **-61.8070** | 24.1193 | ±48.2385 | **-2.563** | **0.0104** | * |
| Hypertension | +743.4495 | 442.6630 | ±885.3260 | +1.679 | 0.0931 | . |
| High cholesterol | -418.2443 | 387.1745 | ±774.3490 | -1.080 | 0.2800 |  |
| Kidney disease | -518.4573 | 772.4589 | ±1544.9178 | -0.671 | 0.5021 |  |
| Circulatory disease | -968.0467 | 643.2632 | ±1286.5264 | -1.505 | 0.1323 |  |
| Nocturnal mean 00-06h (mg/dL) | +29.7234 | 19.7440 | ±39.4880 | +1.505 | 0.1322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1516**, Adj R² = **0.1276**, F-statistic = **6.32** (p = **1.23e-09**), Residual SE = **3611.513** on **389** df, AIC = **7719.7**, BIC = **7767.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19826.7034** | 2117.3870 | ±4234.7739 | **+9.364** | **7.69e-21** | *** |
| **Education: graduate level (vs college)** | **-830.7556** | 374.4271 | ±748.8542 | **-2.219** | **0.0265** | * |
| Education: high school or below (vs college) | +568.7302 | 857.9425 | ±1715.8850 | +0.663 | 0.5074 |  |
| Site: UCSD (vs UAB) | -363.1286 | 499.4295 | ±998.8590 | -0.727 | 0.4672 |  |
| Site: UW (vs UAB) | -864.1048 | 467.3144 | ±934.6289 | -1.849 | 0.0644 | . |
| **Age (years)** | **-112.8479** | 19.1403 | ±38.2806 | **-5.896** | **3.73e-09** | *** |
| **BMI (kg/m2)** | **-55.0361** | 24.6748 | ±49.3495 | **-2.230** | **0.0257** | * |
| Hypertension | +810.3104 | 446.1984 | ±892.3968 | +1.816 | 0.0694 | . |
| High cholesterol | -436.4135 | 388.7730 | ±777.5460 | -1.123 | 0.2616 |  |
| Kidney disease | -531.5888 | 759.8074 | ±1519.6148 | -0.700 | 0.4842 |  |
| Circulatory disease | -971.1691 | 646.9602 | ±1293.9203 | -1.501 | 0.1333 |  |
| Glucose SD, pooled (mg/dL) | -43.9526 | 86.7836 | ±173.5672 | -0.506 | 0.6125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1519**, Adj R² = **0.1279**, F-statistic = **6.33** (p = **1.16e-09**), Residual SE = **3610.939** on **389** df, AIC = **7719.6**, BIC = **7767.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19864.5556** | 2026.1894 | ±4052.3789 | **+9.804** | **1.08e-22** | *** |
| **Education: graduate level (vs college)** | **-836.4183** | 376.7328 | ±753.4657 | **-2.220** | **0.0264** | * |
| Education: high school or below (vs college) | +561.1172 | 858.7534 | ±1717.5069 | +0.653 | 0.5135 |  |
| Site: UCSD (vs UAB) | -363.7308 | 498.5702 | ±997.1404 | -0.730 | 0.4657 |  |
| Site: UW (vs UAB) | -866.3103 | 466.5564 | ±933.1127 | -1.857 | 0.0633 | . |
| **Age (years)** | **-112.7082** | 19.1489 | ±38.2978 | **-5.886** | **3.96e-09** | *** |
| **BMI (kg/m2)** | **-54.5694** | 24.7562 | ±49.5125 | **-2.204** | **0.0275** | * |
| Hypertension | +805.8953 | 448.1778 | ±896.3555 | +1.798 | 0.0722 | . |
| High cholesterol | -437.3766 | 388.2555 | ±776.5110 | -1.127 | 0.2599 |  |
| Kidney disease | -525.5178 | 757.5389 | ±1515.0778 | -0.694 | 0.4879 |  |
| Circulatory disease | -978.7882 | 647.9175 | ±1295.8350 | -1.511 | 0.1309 |  |
| Avg. daily SD (mg/dL) | -51.3157 | 86.0827 | ±172.1654 | -0.596 | 0.5511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **401**, R² = **0.1524**, Adj R² = **0.1285**, F-statistic = **6.36** (p = **1.04e-09**), Residual SE = **3609.781** on **389** df, AIC = **7719.3**, BIC = **7767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20139.0642** | 2039.3795 | ±4078.7590 | **+9.875** | **5.34e-23** | *** |
| **Education: graduate level (vs college)** | **-834.3579** | 373.7362 | ±747.4724 | **-2.232** | **0.0256** | * |
| Education: high school or below (vs college) | +576.1801 | 858.6817 | ±1717.3635 | +0.671 | 0.5022 |  |
| Site: UCSD (vs UAB) | -377.3052 | 499.8729 | ±999.7458 | -0.755 | 0.4504 |  |
| Site: UW (vs UAB) | -881.0845 | 471.1860 | ±942.3719 | -1.870 | 0.0615 | . |
| **Age (years)** | **-112.5227** | 19.1303 | ±38.2606 | **-5.882** | **4.06e-09** | *** |
| **BMI (kg/m2)** | **-55.4284** | 24.4916 | ±48.9832 | **-2.263** | **0.0236** | * |
| Hypertension | +804.0900 | 449.9806 | ±899.9611 | +1.787 | 0.0739 | . |
| High cholesterol | -439.1486 | 387.1757 | ±774.3514 | -1.134 | 0.2567 |  |
| Kidney disease | -511.8392 | 751.2670 | ±1502.5339 | -0.681 | 0.4957 |  |
| Circulatory disease | -969.3311 | 647.8608 | ±1295.7217 | -1.496 | 0.1346 |  |
| CV (%) | -70.8332 | 88.3599 | ±176.7198 | -0.802 | 0.4228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **401**, R² = **0.1526**, Adj R² = **0.1286**, F-statistic = **6.37** (p = **1.01e-09**), Residual SE = **3609.444** on **389** df, AIC = **7719.2**, BIC = **7767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18049.8742** | 1823.6816 | ±3647.3633 | **+9.897** | **4.27e-23** | *** |
| **Education: graduate level (vs college)** | **-838.2429** | 373.3250 | ±746.6500 | **-2.245** | **0.0247** | * |
| Education: high school or below (vs college) | +581.5853 | 859.6115 | ±1719.2230 | +0.677 | 0.4987 |  |
| Site: UCSD (vs UAB) | -374.7870 | 498.9595 | ±997.9190 | -0.751 | 0.4526 |  |
| Site: UW (vs UAB) | -878.7875 | 468.2257 | ±936.4514 | -1.877 | 0.0605 | . |
| **Age (years)** | **-112.5713** | 19.1382 | ±38.2764 | **-5.882** | **4.05e-09** | *** |
| **BMI (kg/m2)** | **-55.4574** | 24.4519 | ±48.9037 | **-2.268** | **0.0233** | * |
| Hypertension | +803.9728 | 450.0505 | ±900.1010 | +1.786 | 0.0740 | . |
| High cholesterol | -441.7956 | 387.1657 | ±774.3315 | -1.141 | 0.2538 |  |
| Kidney disease | -526.2434 | 748.1382 | ±1496.2763 | -0.703 | 0.4818 |  |
| Circulatory disease | -975.2500 | 647.3513 | ±1294.7026 | -1.507 | 0.1319 |  |
| Mean / SD ratio | +151.5161 | 175.0364 | ±350.0728 | +0.866 | 0.3867 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1525**, Adj R² = **0.1285**, F-statistic = **6.36** (p = **1.03e-09**), Residual SE = **3609.653** on **389** df, AIC = **7719.3**, BIC = **7767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18178.3672** | 1747.5301 | ±3495.0603 | **+10.402** | **2.42e-25** | *** |
| **Education: graduate level (vs college)** | **-839.5560** | 374.5158 | ±749.0316 | **-2.242** | **0.0250** | * |
| Education: high school or below (vs college) | +577.8222 | 860.3634 | ±1720.7269 | +0.672 | 0.5018 |  |
| Site: UCSD (vs UAB) | -370.4445 | 497.5374 | ±995.0747 | -0.745 | 0.4565 |  |
| Site: UW (vs UAB) | -876.6372 | 466.1166 | ±932.2333 | -1.881 | 0.0600 | . |
| **Age (years)** | **-112.4000** | 19.1423 | ±38.2846 | **-5.872** | **4.31e-09** | *** |
| **BMI (kg/m2)** | **-54.9459** | 24.5719 | ±49.1438 | **-2.236** | **0.0253** | * |
| Hypertension | +796.4802 | 451.9645 | ±903.9290 | +1.762 | 0.0780 | . |
| High cholesterol | -435.3898 | 387.4963 | ±774.9925 | -1.124 | 0.2612 |  |
| Kidney disease | -526.8860 | 750.9918 | ±1501.9836 | -0.702 | 0.4829 |  |
| Circulatory disease | -991.6395 | 648.1465 | ±1296.2930 | -1.530 | 0.1260 |  |
| Avg. daily mean/SD | +114.5108 | 133.3499 | ±266.6998 | +0.859 | 0.3905 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **401**, R² = **0.1551**, Adj R² = **0.1312**, F-statistic = **6.49** (p = **6.12e-10**), Residual SE = **3604.132** on **389** df, AIC = **7718.1**, BIC = **7766.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17432.0582** | 2081.8272 | ±4163.6543 | **+8.373** | **5.60e-17** | *** |
| **Education: graduate level (vs college)** | **-806.6450** | 370.5338 | ±741.0676 | **-2.177** | **0.0295** | * |
| Education: high school or below (vs college) | +510.1064 | 859.3773 | ±1718.7546 | +0.594 | 0.5528 |  |
| Site: UCSD (vs UAB) | -321.1410 | 496.1677 | ±992.3355 | -0.647 | 0.5175 |  |
| Site: UW (vs UAB) | -781.6477 | 469.0526 | ±938.1052 | -1.666 | 0.0956 | . |
| **Age (years)** | **-110.8887** | 19.2142 | ±38.4285 | **-5.771** | **7.87e-09** | *** |
| **BMI (kg/m2)** | **-54.0433** | 24.6333 | ±49.2667 | **-2.194** | **0.0282** | * |
| Hypertension | +817.6605 | 454.0104 | ±908.0208 | +1.801 | 0.0717 | . |
| High cholesterol | -438.0272 | 392.1328 | ±784.2656 | -1.117 | 0.2640 |  |
| Kidney disease | -669.0389 | 769.8659 | ±1539.7318 | -0.869 | 0.3848 |  |
| Circulatory disease | -971.6631 | 642.4045 | ±1284.8089 | -1.513 | 0.1304 |  |
| MAG (mg/dL/h) | +43.0031 | 36.6039 | ±73.2079 | +1.175 | 0.2401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **401**, R² = **0.1510**, Adj R² = **0.1270**, F-statistic = **6.29** (p = **1.39e-09**), Residual SE = **3612.849** on **389** df, AIC = **7720.0**, BIC = **7767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19378.5965** | 2179.8366 | ±4359.6732 | **+8.890** | **6.11e-19** | *** |
| **Education: graduate level (vs college)** | **-816.2970** | 373.8453 | ±747.6906 | **-2.184** | **0.0290** | * |
| Education: high school or below (vs college) | +577.9933 | 858.9147 | ±1717.8294 | +0.673 | 0.5010 |  |
| Site: UCSD (vs UAB) | -352.4134 | 498.9680 | ±997.9359 | -0.706 | 0.4800 |  |
| Site: UW (vs UAB) | -851.5448 | 465.9616 | ±931.9232 | -1.827 | 0.0676 | . |
| **Age (years)** | **-113.0115** | 19.1542 | ±38.3083 | **-5.900** | **3.63e-09** | *** |
| **BMI (kg/m2)** | **-56.0521** | 24.5796 | ±49.1592 | **-2.280** | **0.0226** | * |
| Hypertension | +792.4093 | 456.8321 | ±913.6642 | +1.735 | 0.0828 | . |
| High cholesterol | -422.4641 | 389.5121 | ±779.0243 | -1.085 | 0.2781 |  |
| Kidney disease | -569.8180 | 762.3867 | ±1524.7734 | -0.747 | 0.4548 |  |
| Circulatory disease | -979.6115 | 645.6542 | ±1291.3085 | -1.517 | 0.1292 |  |
| Avg. daily range (mg/dL) | -3.2994 | 18.6530 | ±37.3061 | -0.177 | 0.8596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1269**, F-statistic = **6.29** (p = **1.42e-09**), Residual SE = **3613.045** on **389** df, AIC = **7720.0**, BIC = **7768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19100.7284** | 1516.0609 | ±3032.1218 | **+12.599** | **2.14e-36** | *** |
| **Education: graduate level (vs college)** | **-812.2124** | 372.3333 | ±744.6667 | **-2.181** | **0.0292** | * |
| Education: high school or below (vs college) | +579.0456 | 865.5825 | ±1731.1650 | +0.669 | 0.5035 |  |
| Site: UCSD (vs UAB) | -348.0528 | 496.9053 | ±993.8105 | -0.700 | 0.4837 |  |
| Site: UW (vs UAB) | -845.5783 | 457.6862 | ±915.3725 | -1.848 | 0.0647 | . |
| **Age (years)** | **-113.0681** | 19.1343 | ±38.2686 | **-5.909** | **3.44e-09** | *** |
| **BMI (kg/m2)** | **-55.6811** | 24.6891 | ±49.3782 | **-2.255** | **0.0241** | * |
| Hypertension | +795.4974 | 453.4651 | ±906.9303 | +1.754 | 0.0794 | . |
| High cholesterol | -420.9792 | 389.5108 | ±779.0216 | -1.081 | 0.2798 |  |
| Kidney disease | -582.1308 | 758.0705 | ±1516.1410 | -0.768 | 0.4425 |  |
| Circulatory disease | -981.1651 | 648.0670 | ±1296.1340 | -1.514 | 0.1300 |  |
| SD of daily means (mg/dL) | +0.1419 | 107.0074 | ±214.0149 | +0.001 | 0.9989 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **401**, R² = **0.1587**, Adj R² = **0.1349**, F-statistic = **6.67** (p = **2.92e-10**), Residual SE = **3596.357** on **389** df, AIC = **7716.3**, BIC = **7764.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133600.6138** | 59427.8562 | ±118855.7125 | **+2.248** | **0.0246** | * |
| **Education: graduate level (vs college)** | **-775.8487** | 371.6431 | ±743.2863 | **-2.088** | **0.0368** | * |
| Education: high school or below (vs college) | +620.7344 | 859.3958 | ±1718.7916 | +0.722 | 0.4701 |  |
| Site: UCSD (vs UAB) | -295.9307 | 495.1461 | ±990.2922 | -0.598 | 0.5501 |  |
| Site: UW (vs UAB) | -813.1291 | 454.8706 | ±909.7411 | -1.788 | 0.0738 | . |
| **Age (years)** | **-112.0086** | 19.0139 | ±38.0277 | **-5.891** | **3.84e-09** | *** |
| **BMI (kg/m2)** | **-54.6911** | 25.6804 | ±51.3607 | **-2.130** | **0.0332** | * |
| Hypertension | +784.3496 | 448.0556 | ±896.1113 | +1.751 | 0.0800 | . |
| High cholesterol | -429.4102 | 389.3858 | ±778.7716 | -1.103 | 0.2701 |  |
| Kidney disease | -686.3348 | 797.5094 | ±1595.0188 | -0.861 | 0.3895 |  |
| Circulatory disease | -975.4175 | 641.8190 | ±1283.6379 | -1.520 | 0.1286 |  |
| Time in range 70-180, pooled (%) | -1151.5188 | 598.5569 | ±1197.1138 | -1.924 | 0.0544 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **401**, R² = **0.1577**, Adj R² = **0.1339**, F-statistic = **6.62** (p = **3.63e-10**), Residual SE = **3598.625** on **389** df, AIC = **7716.8**, BIC = **7764.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121810.7804** | 60026.0517 | ±120052.1035 | **+2.029** | **0.0424** | * |
| **Education: graduate level (vs college)** | **-768.5902** | 373.3644 | ±746.7289 | **-2.059** | **0.0395** | * |
| Education: high school or below (vs college) | +627.9809 | 858.8032 | ±1717.6063 | +0.731 | 0.4646 |  |
| Site: UCSD (vs UAB) | -318.3323 | 495.0681 | ±990.1362 | -0.643 | 0.5202 |  |
| Site: UW (vs UAB) | -845.4835 | 453.1142 | ±906.2284 | -1.866 | 0.0620 | . |
| **Age (years)** | **-112.0028** | 19.0260 | ±38.0520 | **-5.887** | **3.94e-09** | *** |
| **BMI (kg/m2)** | **-55.6780** | 24.9104 | ±49.8209 | **-2.235** | **0.0254** | * |
| Hypertension | +828.6250 | 453.8469 | ±907.6937 | +1.826 | 0.0679 | . |
| High cholesterol | -442.5252 | 390.1082 | ±780.2165 | -1.134 | 0.2566 |  |
| Kidney disease | -639.6173 | 786.5672 | ±1573.1345 | -0.813 | 0.4161 |  |
| Circulatory disease | -1004.3856 | 640.2535 | ±1280.5069 | -1.569 | 0.1167 |  |
| Avg. daily time in range 70-180 (%) | -1032.1091 | 604.3881 | ±1208.7762 | -1.708 | 0.0877 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1510**, Adj R² = **0.1270**, F-statistic = **6.29** (p = **1.40e-09**), Residual SE = **3612.923** on **389** df, AIC = **7720.0**, BIC = **7767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19077.8958** | 1455.0139 | ±2910.0278 | **+13.112** | **2.82e-39** | *** |
| **Education: graduate level (vs college)** | **-811.5551** | 370.6549 | ±741.3098 | **-2.190** | **0.0286** | * |
| Education: high school or below (vs college) | +583.0088 | 858.4565 | ±1716.9130 | +0.679 | 0.4971 |  |
| Site: UCSD (vs UAB) | -336.6834 | 501.1887 | ±1002.3774 | -0.672 | 0.5017 |  |
| Site: UW (vs UAB) | -839.5041 | 457.5806 | ±915.1612 | -1.835 | 0.0666 | . |
| **Age (years)** | **-113.0003** | 19.0658 | ±38.1317 | **-5.927** | **3.09e-09** | *** |
| **BMI (kg/m2)** | **-55.6815** | 24.6176 | ±49.2351 | **-2.262** | **0.0237** | * |
| Hypertension | +791.8182 | 453.8990 | ±907.7981 | +1.744 | 0.0811 | . |
| High cholesterol | -420.3300 | 389.7867 | ±779.5734 | -1.078 | 0.2809 |  |
| Kidney disease | -573.6825 | 763.5632 | ±1527.1264 | -0.751 | 0.4525 |  |
| Circulatory disease | -984.5085 | 643.7624 | ±1287.5249 | -1.529 | 0.1262 |  |
| Any reading < 54 during wear (0/1) | +77.6735 | 440.3772 | ±880.7544 | +0.176 | 0.8600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1560**, Adj R² = **0.1321**, F-statistic = **6.54** (p = **5.12e-10**), Residual SE = **3602.244** on **389** df, AIC = **7717.6**, BIC = **7765.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18940.1113** | 1446.5647 | ±2893.1294 | **+13.093** | **3.60e-39** | *** |
| **Education: graduate level (vs college)** | **-807.9931** | 369.7976 | ±739.5952 | **-2.185** | **0.0289** | * |
| Education: high school or below (vs college) | +652.7703 | 859.8852 | ±1719.7703 | +0.759 | 0.4478 |  |
| Site: UCSD (vs UAB) | -263.9821 | 498.2131 | ±996.4262 | -0.530 | 0.5962 |  |
| Site: UW (vs UAB) | -808.0082 | 455.9219 | ±911.8438 | -1.772 | 0.0764 | . |
| **Age (years)** | **-111.0265** | 18.9563 | ±37.9125 | **-5.857** | **4.71e-09** | *** |
| **BMI (kg/m2)** | **-58.8027** | 24.2102 | ±48.4204 | **-2.429** | **0.0151** | * |
| Hypertension | +737.3744 | 452.3169 | ±904.6338 | +1.630 | 0.1031 |  |
| High cholesterol | -398.5974 | 389.6348 | ±779.2696 | -1.023 | 0.3063 |  |
| Kidney disease | -523.9172 | 761.0841 | ±1522.1683 | -0.688 | 0.4912 |  |
| Circulatory disease | -1029.3565 | 652.4372 | ±1304.8744 | -1.578 | 0.1146 |  |
| Time < 54 (%) | +5028.1461 | 4314.3281 | ±8628.6562 | +1.165 | 0.2438 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1558**, Adj R² = **0.1319**, F-statistic = **6.53** (p = **5.32e-10**), Residual SE = **3602.652** on **389** df, AIC = **7717.7**, BIC = **7765.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19040.6409** | 1444.4180 | ±2888.8360 | **+13.182** | **1.11e-39** | *** |
| **Education: graduate level (vs college)** | **-813.7213** | 370.1590 | ±740.3179 | **-2.198** | **0.0279** | * |
| Education: high school or below (vs college) | +608.4122 | 856.9782 | ±1713.9564 | +0.710 | 0.4777 |  |
| Site: UCSD (vs UAB) | -314.7492 | 495.1912 | ±990.3824 | -0.636 | 0.5250 |  |
| Site: UW (vs UAB) | -847.7718 | 458.2825 | ±916.5650 | -1.850 | 0.0643 | . |
| **Age (years)** | **-112.4893** | 19.0159 | ±38.0319 | **-5.916** | **3.31e-09** | *** |
| **BMI (kg/m2)** | **-57.1689** | 24.5495 | ±49.0991 | **-2.329** | **0.0199** | * |
| Hypertension | +782.6857 | 452.0221 | ±904.0442 | +1.732 | 0.0834 | . |
| High cholesterol | -415.6809 | 389.0628 | ±778.1257 | -1.068 | 0.2853 |  |
| Kidney disease | -542.7620 | 762.1471 | ±1524.2942 | -0.712 | 0.4764 |  |
| Circulatory disease | -1059.0234 | 654.0814 | ±1308.1627 | -1.619 | 0.1054 |  |
| Avg. daily time < 54 (%) | +6477.0577 | 6181.5890 | ±12363.1779 | +1.048 | 0.2947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1269**, F-statistic = **6.29** (p = **1.42e-09**), Residual SE = **3613.020** on **389** df, AIC = **7720.0**, BIC = **7768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19088.0517** | 1477.8511 | ±2955.7023 | **+12.916** | **3.65e-38** | *** |
| **Education: graduate level (vs college)** | **-811.3459** | 371.7726 | ±743.5453 | **-2.182** | **0.0291** | * |
| Education: high school or below (vs college) | +576.0881 | 864.4729 | ±1728.9458 | +0.666 | 0.5052 |  |
| Site: UCSD (vs UAB) | -345.9909 | 495.7078 | ±991.4156 | -0.698 | 0.4852 |  |
| Site: UW (vs UAB) | -843.3176 | 459.7280 | ±919.4559 | -1.834 | 0.0666 | . |
| **Age (years)** | **-113.0570** | 19.1195 | ±38.2391 | **-5.913** | **3.36e-09** | *** |
| **BMI (kg/m2)** | **-55.6562** | 24.6497 | ±49.2993 | **-2.258** | **0.0240** | * |
| Hypertension | +797.9438 | 452.9008 | ±905.8015 | +1.762 | 0.0781 | . |
| High cholesterol | -423.6817 | 396.1855 | ±792.3710 | -1.069 | 0.2849 |  |
| Kidney disease | -580.0687 | 760.0674 | ±1520.1348 | -0.763 | 0.4454 |  |
| Circulatory disease | -980.4200 | 643.2379 | ±1286.4758 | -1.524 | 0.1275 |  |
| Time 54-69, pooled (%) | +74.1497 | 953.5028 | ±1907.0057 | +0.078 | 0.9380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **401**, R² = **0.1511**, Adj R² = **0.1271**, F-statistic = **6.29** (p = **1.38e-09**), Residual SE = **3612.712** on **389** df, AIC = **7720.0**, BIC = **7767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19137.4833** | 1469.8458 | ±2939.6915 | **+13.020** | **9.41e-39** | *** |
| **Education: graduate level (vs college)** | **-817.9046** | 373.0929 | ±746.1858 | **-2.192** | **0.0284** | * |
| Education: high school or below (vs college) | +589.0735 | 862.7151 | ±1725.4302 | +0.683 | 0.4947 |  |
| Site: UCSD (vs UAB) | -352.1885 | 495.6456 | ±991.2912 | -0.711 | 0.4774 |  |
| Site: UW (vs UAB) | -848.9792 | 458.7847 | ±917.5694 | -1.850 | 0.0642 | . |
| **Age (years)** | **-113.0106** | 19.0906 | ±38.1811 | **-5.920** | **3.23e-09** | *** |
| **BMI (kg/m2)** | **-55.6780** | 24.5739 | ±49.1478 | **-2.266** | **0.0235** | * |
| Hypertension | +779.1709 | 458.6941 | ±917.3882 | +1.699 | 0.0894 | . |
| High cholesterol | -412.4068 | 396.0297 | ±792.0595 | -1.041 | 0.2977 |  |
| Kidney disease | -588.1078 | 759.7688 | ±1519.5377 | -0.774 | 0.4389 |  |
| Circulatory disease | -977.3979 | 645.8491 | ±1291.6983 | -1.513 | 0.1302 |  |
| Avg. daily time 54-69 (%) | -274.7874 | 982.0377 | ±1964.0753 | -0.280 | 0.7796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **401**, R² = **0.1514**, Adj R² = **0.1274**, F-statistic = **6.31** (p = **1.29e-09**), Residual SE = **3612.010** on **389** df, AIC = **7719.8**, BIC = **7767.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19013.2290** | 1478.2677 | ±2956.5354 | **+12.862** | **7.38e-38** | *** |
| **Education: graduate level (vs college)** | **-807.0876** | 372.0105 | ±744.0211 | **-2.170** | **0.0300** | * |
| Education: high school or below (vs college) | +568.3542 | 863.4215 | ±1726.8430 | +0.658 | 0.5104 |  |
| Site: UCSD (vs UAB) | -329.4288 | 495.7493 | ±991.4986 | -0.665 | 0.5064 |  |
| Site: UW (vs UAB) | -829.8533 | 458.9126 | ±917.8253 | -1.808 | 0.0706 | . |
| **Age (years)** | **-112.8368** | 19.1276 | ±38.2551 | **-5.899** | **3.65e-09** | *** |
| **BMI (kg/m2)** | **-55.8027** | 24.6448 | ±49.2896 | **-2.264** | **0.0236** | * |
| Hypertension | +804.1602 | 452.7826 | ±905.5652 | +1.776 | 0.0757 | . |
| High cholesterol | -434.3135 | 394.6886 | ±789.3772 | -1.100 | 0.2712 |  |
| Kidney disease | -565.8005 | 760.3679 | ±1520.7359 | -0.744 | 0.4568 |  |
| Circulatory disease | -981.2139 | 645.3174 | ±1290.6347 | -1.521 | 0.1284 |  |
| Time < 70 (%) | +415.3355 | 932.6231 | ±1865.2463 | +0.445 | 0.6561 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1269**, F-statistic = **6.29** (p = **1.42e-09**), Residual SE = **3613.017** on **389** df, AIC = **7720.0**, BIC = **7768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19091.2664** | 1467.2293 | ±2934.4587 | **+13.012** | **1.05e-38** | *** |
| **Education: graduate level (vs college)** | **-810.7133** | 374.0660 | ±748.1320 | **-2.167** | **0.0302** | * |
| Education: high school or below (vs college) | +576.7964 | 862.6142 | ±1725.2283 | +0.669 | 0.5037 |  |
| Site: UCSD (vs UAB) | -346.6301 | 495.7843 | ±991.5686 | -0.699 | 0.4845 |  |
| Site: UW (vs UAB) | -844.6984 | 458.3159 | ±916.6318 | -1.843 | 0.0653 | . |
| **Age (years)** | **-113.0770** | 19.0938 | ±38.1876 | **-5.922** | **3.18e-09** | *** |
| **BMI (kg/m2)** | **-55.6976** | 24.6349 | ±49.2699 | **-2.261** | **0.0238** | * |
| Hypertension | +799.7070 | 459.3524 | ±918.7049 | +1.741 | 0.0817 | . |
| High cholesterol | -423.1597 | 395.1551 | ±790.3101 | -1.071 | 0.2842 |  |
| Kidney disease | -580.1144 | 760.0402 | ±1520.0805 | -0.763 | 0.4453 |  |
| Circulatory disease | -982.9577 | 647.2370 | ±1294.4740 | -1.519 | 0.1288 |  |
| Avg. daily time < 70 (%) | +72.1785 | 962.2243 | ±1924.4486 | +0.075 | 0.9402 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1556**, Adj R² = **0.1317**, F-statistic = **6.51** (p = **5.57e-10**), Residual SE = **3603.140** on **389** df, AIC = **7717.8**, BIC = **7765.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +489099.0439 | 415449.5913 | ±830899.1826 | +1.177 | 0.2391 |  |
| **Education: graduate level (vs college)** | **-808.1648** | 369.9693 | ±739.9386 | **-2.184** | **0.0289** | * |
| Education: high school or below (vs college) | +650.9342 | 859.8454 | ±1719.6909 | +0.757 | 0.4490 |  |
| Site: UCSD (vs UAB) | -263.1727 | 498.9457 | ±997.8913 | -0.527 | 0.5979 |  |
| Site: UW (vs UAB) | -805.4139 | 456.2218 | ±912.4436 | -1.765 | 0.0775 | . |
| **Age (years)** | **-110.8326** | 18.9795 | ±37.9590 | **-5.840** | **5.23e-09** | *** |
| **BMI (kg/m2)** | **-58.2699** | 24.2480 | ±48.4959 | **-2.403** | **0.0163** | * |
| Hypertension | +744.2866 | 451.8445 | ±903.6891 | +1.647 | 0.0995 | . |
| High cholesterol | -401.6299 | 389.6080 | ±779.2160 | -1.031 | 0.3026 |  |
| Kidney disease | -528.4706 | 760.9188 | ±1521.8376 | -0.695 | 0.4874 |  |
| Circulatory disease | -1026.4918 | 652.0686 | ±1304.1372 | -1.574 | 0.1154 |  |
| Time 54-250, pooled (%) | -4701.8495 | 4156.0896 | ±8312.1791 | -1.131 | 0.2579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1553**, Adj R² = **0.1314**, F-statistic = **6.50** (p = **5.85e-10**), Residual SE = **3603.653** on **389** df, AIC = **7717.9**, BIC = **7765.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +621597.1703 | 601635.8357 | ±1203271.6714 | +1.033 | 0.3015 |  |
| **Education: graduate level (vs college)** | **-813.4146** | 370.4072 | ±740.8144 | **-2.196** | **0.0281** | * |
| Education: high school or below (vs college) | +610.5498 | 857.0470 | ±1714.0940 | +0.712 | 0.4762 |  |
| Site: UCSD (vs UAB) | -308.2692 | 495.7689 | ±991.5378 | -0.622 | 0.5341 |  |
| Site: UW (vs UAB) | -840.5928 | 458.1122 | ±916.2244 | -1.835 | 0.0665 | . |
| **Age (years)** | **-112.0689** | 19.0272 | ±38.0545 | **-5.890** | **3.86e-09** | *** |
| **BMI (kg/m2)** | **-56.5988** | 24.6199 | ±49.2397 | **-2.299** | **0.0215** | * |
| Hypertension | +788.0062 | 452.1567 | ±904.3134 | +1.743 | 0.0814 | . |
| High cholesterol | -418.3292 | 389.2886 | ±778.5772 | -1.075 | 0.2826 |  |
| Kidney disease | -546.5896 | 762.0080 | ±1524.0161 | -0.717 | 0.4732 |  |
| Circulatory disease | -1053.9707 | 653.8853 | ±1307.7707 | -1.612 | 0.1070 |  |
| Avg. daily time 54-250 (%) | -6026.0377 | 6017.6552 | ±12035.3105 | -1.001 | 0.3166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **401**, R² = **0.1572**, Adj R² = **0.1333**, F-statistic = **6.60** (p = **4.01e-10**), Residual SE = **3599.683** on **389** df, AIC = **7717.1**, BIC = **7765.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18716.3526** | 1500.4408 | ±3000.8817 | **+12.474** | **1.04e-35** | *** |
| **Education: graduate level (vs college)** | **-790.8230** | 370.1401 | ±740.2801 | **-2.137** | **0.0326** | * |
| Education: high school or below (vs college) | +647.2725 | 856.6858 | ±1713.3715 | +0.756 | 0.4499 |  |
| Site: UCSD (vs UAB) | -349.1387 | 494.5726 | ±989.1451 | -0.706 | 0.4802 |  |
| Site: UW (vs UAB) | -857.4955 | 453.4844 | ±906.9688 | -1.891 | 0.0586 | . |
| **Age (years)** | **-112.7424** | 19.0514 | ±38.1029 | **-5.918** | **3.26e-09** | *** |
| **BMI (kg/m2)** | **-54.4772** | 25.6472 | ±51.2943 | **-2.124** | **0.0337** | * |
| Hypertension | +760.9780 | 446.9573 | ±893.9146 | +1.703 | 0.0886 | . |
| High cholesterol | -393.0546 | 388.9976 | ±777.9952 | -1.010 | 0.3123 |  |
| Kidney disease | -726.1030 | 806.1166 | ±1612.2331 | -0.901 | 0.3677 |  |
| Circulatory disease | -975.2885 | 639.2231 | ±1278.4461 | -1.526 | 0.1271 |  |
| Time 181-250, pooled (%) | +1110.6310 | 668.8404 | ±1337.6807 | +1.661 | 0.0968 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **401**, R² = **0.1587**, Adj R² = **0.1349**, F-statistic = **6.67** (p = **2.97e-10**), Residual SE = **3596.543** on **389** df, AIC = **7716.4**, BIC = **7764.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18693.7474** | 1478.0890 | ±2956.1781 | **+12.647** | **1.16e-36** | *** |
| **Education: graduate level (vs college)** | **-785.9559** | 369.9662 | ±739.9324 | **-2.124** | **0.0336** | * |
| Education: high school or below (vs college) | +674.0882 | 856.4493 | ±1712.8987 | +0.787 | 0.4312 |  |
| Site: UCSD (vs UAB) | -339.2838 | 494.5095 | ±989.0190 | -0.686 | 0.4926 |  |
| Site: UW (vs UAB) | -861.4895 | 452.3940 | ±904.7880 | -1.904 | 0.0569 | . |
| **Age (years)** | **-111.7654** | 19.0445 | ±38.0891 | **-5.869** | **4.39e-09** | *** |
| **BMI (kg/m2)** | **-55.4824** | 24.8246 | ±49.6492 | **-2.235** | **0.0254** | * |
| Hypertension | +763.7092 | 446.4831 | ±892.9663 | +1.710 | 0.0872 | . |
| High cholesterol | -409.0603 | 388.1647 | ±776.3295 | -1.054 | 0.2920 |  |
| Kidney disease | -683.0541 | 794.9912 | ±1589.9824 | -0.859 | 0.3902 |  |
| Circulatory disease | -977.4040 | 637.2678 | ±1274.5356 | -1.534 | 0.1251 |  |
| Avg. daily time 181-250 (%) | +1210.5512 | 663.2355 | ±1326.4709 | +1.825 | 0.0680 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **401**, R² = **0.1571**, Adj R² = **0.1333**, F-statistic = **6.59** (p = **4.07e-10**), Residual SE = **3599.828** on **389** df, AIC = **7717.1**, BIC = **7765.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18710.6284** | 1502.1901 | ±3004.3803 | **+12.456** | **1.30e-35** | *** |
| **Education: graduate level (vs college)** | **-790.9565** | 370.1712 | ±740.3424 | **-2.137** | **0.0326** | * |
| Education: high school or below (vs college) | +647.4617 | 856.6974 | ±1713.3948 | +0.756 | 0.4498 |  |
| Site: UCSD (vs UAB) | -347.6615 | 494.6294 | ±989.2588 | -0.703 | 0.4821 |  |
| Site: UW (vs UAB) | -856.2280 | 453.5679 | ±907.1358 | -1.888 | 0.0591 | . |
| **Age (years)** | **-112.6682** | 19.0541 | ±38.1082 | **-5.913** | **3.36e-09** | *** |
| **BMI (kg/m2)** | **-54.4087** | 25.6536 | ±51.3071 | **-2.121** | **0.0339** | * |
| Hypertension | +761.9677 | 447.0148 | ±894.0295 | +1.705 | 0.0883 | . |
| High cholesterol | -393.6305 | 389.0112 | ±778.0223 | -1.012 | 0.3116 |  |
| Kidney disease | -725.2263 | 805.8678 | ±1611.7356 | -0.900 | 0.3682 |  |
| Circulatory disease | -975.3937 | 639.2849 | ±1278.5698 | -1.526 | 0.1271 |  |
| Time > 180 (%) | +1102.4641 | 666.4012 | ±1332.8024 | +1.654 | 0.0981 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1586**, Adj R² = **0.1348**, F-statistic = **6.66** (p = **3.03e-10**), Residual SE = **3596.742** on **389** df, AIC = **7716.4**, BIC = **7764.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18687.0379** | 1480.0788 | ±2960.1577 | **+12.626** | **1.52e-36** | *** |
| **Education: graduate level (vs college)** | **-786.1439** | 370.0041 | ±740.0081 | **-2.125** | **0.0336** | * |
| Education: high school or below (vs college) | +674.0953 | 856.4624 | ±1712.9248 | +0.787 | 0.4312 |  |
| Site: UCSD (vs UAB) | -337.6075 | 494.5501 | ±989.1003 | -0.683 | 0.4948 |  |
| Site: UW (vs UAB) | -859.9521 | 452.4877 | ±904.9754 | -1.900 | 0.0574 | . |
| **Age (years)** | **-111.6850** | 19.0510 | ±38.1021 | **-5.862** | **4.56e-09** | *** |
| **BMI (kg/m2)** | **-55.3912** | 24.8343 | ±49.6686 | **-2.230** | **0.0257** | * |
| Hypertension | +764.8669 | 446.5700 | ±893.1399 | +1.713 | 0.0868 | . |
| High cholesterol | -409.6178 | 388.2044 | ±776.4087 | -1.055 | 0.2914 |  |
| Kidney disease | -682.3938 | 794.7392 | ±1589.4785 | -0.859 | 0.3905 |  |
| Circulatory disease | -977.5104 | 637.3538 | ±1274.7076 | -1.534 | 0.1251 |  |
| Avg. daily time > 180 (%) | +1200.0358 | 659.9183 | ±1319.8366 | +1.818 | 0.0690 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1661**, Adj R² = **0.1425**, F-statistic = **7.04** (p = **6.49e-11**), Residual SE = **3580.674** on **389** df, AIC = **7712.8**, BIC = **7760.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18668.2938** | 1488.8503 | ±2977.7006 | **+12.539** | **4.58e-36** | *** |
| Education: graduate level (vs college) | -739.7890 | 378.3184 | ±756.6367 | -1.955 | 0.0505 | . |
| Education: high school or below (vs college) | +593.6335 | 842.6476 | ±1685.2951 | +0.704 | 0.4811 |  |
| Site: UCSD (vs UAB) | -393.7234 | 489.0143 | ±978.0286 | -0.805 | 0.4207 |  |
| **Site: UW (vs UAB)** | **-907.0915** | 442.1234 | ±884.2467 | **-2.052** | **0.0402** | * |
| **Age (years)** | **-105.2058** | 20.3606 | ±40.7211 | **-5.167** | **2.38e-07** | *** |
| **BMI (kg/m2)** | **-60.5997** | 23.8158 | ±47.6316 | **-2.545** | **0.0109** | * |
| Hypertension | +692.0867 | 425.9979 | ±851.9957 | +1.625 | 0.1042 |  |
| High cholesterol | -454.5851 | 391.0667 | ±782.1333 | -1.162 | 0.2451 |  |
| Kidney disease | -655.0001 | 795.4809 | ±1590.9617 | -0.823 | 0.4103 |  |
| Circulatory disease | -910.6137 | 651.0573 | ±1302.1147 | -1.399 | 0.1619 |  |
| Nocturnal time > 180 (%) | +1304.9622 | 922.5774 | ±1845.1548 | +1.414 | 0.1572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 401; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1516**, F-statistic = **8.15** (p = **5.40e-12**), Residual SE = **11.595** on **390** df, AIC = **3114.2**, BIC = **3158.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8490** | 4.6965 | ±9.3930 | **+11.040** | **2.45e-28** | *** |
| Education: graduate level (vs college) | -2.3269 | 1.1940 | ±2.3879 | -1.949 | 0.0513 | . |
| Education: high school or below (vs college) | +1.5104 | 2.6985 | ±5.3970 | +0.560 | 0.5757 |  |
| Site: UCSD (vs UAB) | -1.6998 | 1.5772 | ±3.1544 | -1.078 | 0.2811 |  |
| Site: UW (vs UAB) | -2.8682 | 1.4851 | ±2.9702 | -1.931 | 0.0534 | . |
| **Age (years)** | **-0.4123** | 0.0567 | ±0.1134 | **-7.271** | **3.57e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0836 | ±0.1671 | -0.128 | 0.8984 |  |
| Hypertension | +1.8324 | 1.3874 | ±2.7747 | +1.321 | 0.1866 |  |
| High cholesterol | -0.7472 | 1.2253 | ±2.4505 | -0.610 | 0.5420 |  |
| Kidney disease | -1.4715 | 2.3974 | ±4.7947 | -0.614 | 0.5393 |  |
| Circulatory disease | -2.7913 | 1.9547 | ±3.9094 | -1.428 | 0.1533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **401**, R² = **0.1740**, Adj R² = **0.1506**, F-statistic = **7.45** (p = **1.25e-11**), Residual SE = **11.602** on **389** df, AIC = **3115.6**, BIC = **3163.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.1148** | 11.6776 | ±23.3553 | **+3.778** | **1.58e-04** | *** |
| Education: graduate level (vs college) | -2.2805 | 1.1957 | ±2.3914 | -1.907 | 0.0565 | . |
| Education: high school or below (vs college) | +1.4227 | 2.6962 | ±5.3925 | +0.528 | 0.5977 |  |
| Site: UCSD (vs UAB) | -1.6343 | 1.5725 | ±3.1451 | -1.039 | 0.2987 |  |
| Site: UW (vs UAB) | -2.7935 | 1.4838 | ±2.9677 | -1.883 | 0.0597 | . |
| **Age (years)** | **-0.4166** | 0.0572 | ±0.1144 | **-7.282** | **3.28e-13** | *** |
| BMI (kg/m2) | -0.0177 | 0.0824 | ±0.1648 | -0.215 | 0.8296 |  |
| Hypertension | +1.7501 | 1.3912 | ±2.7824 | +1.258 | 0.2084 |  |
| High cholesterol | -0.9705 | 1.2592 | ±2.5183 | -0.771 | 0.4408 |  |
| Kidney disease | -1.3462 | 2.4099 | ±4.8197 | -0.559 | 0.5764 |  |
| Circulatory disease | -2.7352 | 1.9681 | ±3.9362 | -1.390 | 0.1646 |  |
| HbA1c (%) | +1.4891 | 2.0406 | ±4.0812 | +0.730 | 0.4656 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1494**, F-statistic = **7.39** (p = **1.60e-11**), Residual SE = **11.610** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1707** | 10.6550 | ±21.3099 | **+4.803** | **1.57e-06** | *** |
| Education: graduate level (vs college) | -2.3239 | 1.1955 | ±2.3909 | -1.944 | 0.0519 | . |
| Education: high school or below (vs college) | +1.5188 | 2.6955 | ±5.3910 | +0.563 | 0.5731 |  |
| Site: UCSD (vs UAB) | -1.7053 | 1.5892 | ±3.1785 | -1.073 | 0.2833 |  |
| Site: UW (vs UAB) | -2.8744 | 1.4982 | ±2.9963 | -1.919 | 0.0550 | . |
| **Age (years)** | **-0.4121** | 0.0567 | ±0.1135 | **-7.264** | **3.77e-13** | *** |
| BMI (kg/m2) | -0.0111 | 0.0839 | ±0.1679 | -0.132 | 0.8948 |  |
| Hypertension | +1.8245 | 1.3914 | ±2.7828 | +1.311 | 0.1898 |  |
| High cholesterol | -0.7441 | 1.2367 | ±2.4734 | -0.602 | 0.5474 |  |
| Kidney disease | -1.4719 | 2.4085 | ±4.8169 | -0.611 | 0.5411 |  |
| Circulatory disease | -2.7935 | 1.9610 | ±3.9219 | -1.425 | 0.1543 |  |
| Mean glucose (mg/dL) | +0.0060 | 0.0864 | ±0.1728 | +0.069 | 0.9447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1494**, F-statistic = **7.39** (p = **1.60e-11**), Residual SE = **11.610** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3419** | 22.0223 | ±44.0446 | **+2.286** | **0.0223** | * |
| Education: graduate level (vs college) | -2.3239 | 1.1955 | ±2.3909 | -1.944 | 0.0519 | . |
| Education: high school or below (vs college) | +1.5188 | 2.6955 | ±5.3910 | +0.563 | 0.5731 |  |
| Site: UCSD (vs UAB) | -1.7053 | 1.5892 | ±3.1785 | -1.073 | 0.2833 |  |
| Site: UW (vs UAB) | -2.8744 | 1.4982 | ±2.9963 | -1.919 | 0.0550 | . |
| **Age (years)** | **-0.4121** | 0.0567 | ±0.1135 | **-7.264** | **3.77e-13** | *** |
| BMI (kg/m2) | -0.0111 | 0.0839 | ±0.1679 | -0.132 | 0.8948 |  |
| Hypertension | +1.8245 | 1.3914 | ±2.7828 | +1.311 | 0.1898 |  |
| High cholesterol | -0.7441 | 1.2367 | ±2.4734 | -0.602 | 0.5474 |  |
| Kidney disease | -1.4719 | 2.4085 | ±4.8169 | -0.611 | 0.5411 |  |
| Circulatory disease | -2.7935 | 1.9610 | ±3.9219 | -1.425 | 0.1543 |  |
| GMI (%) | +0.2504 | 3.6113 | ±7.2226 | +0.069 | 0.9447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **401**, R² = **0.1744**, Adj R² = **0.1511**, F-statistic = **7.47** (p = **1.13e-11**), Residual SE = **11.598** on **389** df, AIC = **3115.4**, BIC = **3163.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.4474** | 8.6205 | ±17.2409 | **+5.272** | **1.35e-07** | *** |
| Education: graduate level (vs college) | -2.2613 | 1.1968 | ±2.3936 | -1.889 | 0.0588 | . |
| Education: high school or below (vs college) | +1.5998 | 2.7006 | ±5.4013 | +0.592 | 0.5536 |  |
| Site: UCSD (vs UAB) | -1.8368 | 1.5843 | ±3.1687 | -1.159 | 0.2463 |  |
| **Site: UW (vs UAB)** | **-2.9741** | 1.4908 | ±2.9816 | **-1.995** | **0.0460** | * |
| **Age (years)** | **-0.4042** | 0.0571 | ±0.1142 | **-7.079** | **1.45e-12** | *** |
| BMI (kg/m2) | -0.0220 | 0.0831 | ±0.1662 | -0.265 | 0.7912 |  |
| Hypertension | +1.7361 | 1.3803 | ±2.7607 | +1.258 | 0.2085 |  |
| High cholesterol | -0.7421 | 1.2267 | ±2.4535 | -0.605 | 0.5452 |  |
| Kidney disease | -1.3538 | 2.4316 | ±4.8632 | -0.557 | 0.5777 |  |
| Circulatory disease | -2.7671 | 1.9641 | ±3.9283 | -1.409 | 0.1589 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0550 | 0.0640 | ±0.1280 | +0.859 | 0.3904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1729**, Adj R² = **0.1495**, F-statistic = **7.39** (p = **1.57e-11**), Residual SE = **11.609** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7804** | 6.1423 | ±12.2846 | **+8.593** | **8.48e-18** | *** |
| **Education: graduate level (vs college)** | **-2.3507** | 1.1946 | ±2.3892 | **-1.968** | **0.0491** | * |
| Education: high school or below (vs college) | +1.4971 | 2.7024 | ±5.4048 | +0.554 | 0.5796 |  |
| Site: UCSD (vs UAB) | -1.7192 | 1.5783 | ±3.1566 | -1.089 | 0.2760 |  |
| Site: UW (vs UAB) | -2.8920 | 1.4983 | ±2.9965 | -1.930 | 0.0536 | . |
| **Age (years)** | **-0.4120** | 0.0570 | ±0.1140 | **-7.229** | **4.86e-13** | *** |
| BMI (kg/m2) | -0.0098 | 0.0841 | ±0.1683 | -0.117 | 0.9068 |  |
| Hypertension | +1.8514 | 1.3816 | ±2.7632 | +1.340 | 0.1802 |  |
| High cholesterol | -0.7670 | 1.2394 | ±2.4789 | -0.619 | 0.5360 |  |
| Kidney disease | -1.4066 | 2.4177 | ±4.8354 | -0.582 | 0.5607 |  |
| Circulatory disease | -2.7785 | 1.9597 | ±3.9194 | -1.418 | 0.1562 |  |
| Glucose SD, pooled (mg/dL) | -0.0564 | 0.2597 | ±0.5193 | -0.217 | 0.8279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1735**, Adj R² = **0.1501**, F-statistic = **7.42** (p = **1.38e-11**), Residual SE = **11.605** on **389** df, AIC = **3115.9**, BIC = **3163.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.9780** | 5.7893 | ±11.5785 | **+9.324** | **1.12e-20** | *** |
| **Education: graduate level (vs college)** | **-2.3944** | 1.1995 | ±2.3989 | **-1.996** | **0.0459** | * |
| Education: high school or below (vs college) | +1.4603 | 2.7043 | ±5.4087 | +0.540 | 0.5892 |  |
| Site: UCSD (vs UAB) | -1.7435 | 1.5764 | ±3.1528 | -1.106 | 0.2687 |  |
| Site: UW (vs UAB) | -2.9261 | 1.4965 | ±2.9931 | -1.955 | 0.0506 | . |
| **Age (years)** | **-0.4113** | 0.0571 | ±0.1142 | **-7.201** | **5.98e-13** | *** |
| BMI (kg/m2) | -0.0076 | 0.0845 | ±0.1689 | -0.090 | 0.9285 |  |
| Hypertension | +1.8613 | 1.3841 | ±2.7681 | +1.345 | 0.1787 |  |
| High cholesterol | -0.7930 | 1.2359 | ±2.4719 | -0.642 | 0.5211 |  |
| Kidney disease | -1.3136 | 2.4014 | ±4.8028 | -0.547 | 0.5844 |  |
| Circulatory disease | -2.7848 | 1.9670 | ±3.9339 | -1.416 | 0.1568 |  |
| Avg. daily SD (mg/dL) | -0.1432 | 0.2483 | ±0.4965 | -0.577 | 0.5642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **401**, R² = **0.1731**, Adj R² = **0.1497**, F-statistic = **7.40** (p = **1.50e-11**), Residual SE = **11.608** on **389** df, AIC = **3116.1**, BIC = **3164.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.3819** | 5.9485 | ±11.8970 | **+8.974** | **2.86e-19** | *** |
| **Education: graduate level (vs college)** | **-2.3596** | 1.1967 | ±2.3935 | **-1.972** | **0.0486** | * |
| Education: high school or below (vs college) | +1.5061 | 2.7080 | ±5.4159 | +0.556 | 0.5781 |  |
| Site: UCSD (vs UAB) | -1.7430 | 1.5804 | ±3.1607 | -1.103 | 0.2701 |  |
| Site: UW (vs UAB) | -2.9207 | 1.5056 | ±3.0112 | -1.940 | 0.0524 | . |
| **Age (years)** | **-0.4115** | 0.0570 | ±0.1140 | **-7.218** | **5.27e-13** | *** |
| BMI (kg/m2) | -0.0103 | 0.0837 | ±0.1675 | -0.123 | 0.9021 |  |
| Hypertension | +1.8450 | 1.3873 | ±2.7747 | +1.330 | 0.1835 |  |
| High cholesterol | -0.7740 | 1.2303 | ±2.4606 | -0.629 | 0.5293 |  |
| Kidney disease | -1.3677 | 2.4099 | ±4.8199 | -0.568 | 0.5704 |  |
| Circulatory disease | -2.7739 | 1.9620 | ±3.9239 | -1.414 | 0.1574 |  |
| CV (%) | -0.1046 | 0.2607 | ±0.5214 | -0.401 | 0.6881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **401**, R² = **0.1731**, Adj R² = **0.1497**, F-statistic = **7.40** (p = **1.51e-11**), Residual SE = **11.608** on **389** df, AIC = **3116.1**, BIC = **3164.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.4058** | 6.1173 | ±12.2346 | **+8.240** | **1.72e-16** | *** |
| **Education: graduate level (vs college)** | **-2.3626** | 1.1971 | ±2.3942 | **-1.974** | **0.0484** | * |
| Education: high school or below (vs college) | +1.5139 | 2.7087 | ±5.4173 | +0.559 | 0.5762 |  |
| Site: UCSD (vs UAB) | -1.7365 | 1.5788 | ±3.1575 | -1.100 | 0.2714 |  |
| Site: UW (vs UAB) | -2.9138 | 1.5030 | ±3.0059 | -1.939 | 0.0525 | . |
| **Age (years)** | **-0.4116** | 0.0570 | ±0.1139 | **-7.225** | **5.02e-13** | *** |
| BMI (kg/m2) | -0.0104 | 0.0837 | ±0.1673 | -0.124 | 0.9014 |  |
| Hypertension | +1.8440 | 1.3871 | ±2.7741 | +1.329 | 0.1837 |  |
| High cholesterol | -0.7758 | 1.2312 | ±2.4624 | -0.630 | 0.5286 |  |
| Kidney disease | -1.3948 | 2.4006 | ±4.8012 | -0.581 | 0.5612 |  |
| Circulatory disease | -2.7832 | 1.9620 | ±3.9240 | -1.419 | 0.1560 |  |
| Mean / SD ratio | +0.2079 | 0.5319 | ±1.0639 | +0.391 | 0.6959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1738**, Adj R² = **0.1504**, F-statistic = **7.44** (p = **1.29e-11**), Residual SE = **11.603** on **389** df, AIC = **3115.7**, BIC = **3163.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4293** | 5.8394 | ±11.6788 | **+8.465** | **2.57e-17** | *** |
| **Education: graduate level (vs college)** | **-2.3986** | 1.1996 | ±2.3993 | **-1.999** | **0.0456** | * |
| Education: high school or below (vs college) | +1.5071 | 2.7134 | ±5.4268 | +0.555 | 0.5786 |  |
| Site: UCSD (vs UAB) | -1.7585 | 1.5742 | ±3.1485 | -1.117 | 0.2640 |  |
| **Site: UW (vs UAB)** | **-2.9497** | 1.4967 | ±2.9934 | **-1.971** | **0.0488** | * |
| **Age (years)** | **-0.4106** | 0.0571 | ±0.1142 | **-7.189** | **6.54e-13** | *** |
| BMI (kg/m2) | -0.0087 | 0.0839 | ±0.1677 | -0.104 | 0.9169 |  |
| Hypertension | +1.8349 | 1.3899 | ±2.7798 | +1.320 | 0.1868 |  |
| High cholesterol | -0.7850 | 1.2285 | ±2.4570 | -0.639 | 0.5228 |  |
| Kidney disease | -1.3267 | 2.3996 | ±4.7993 | -0.553 | 0.5803 |  |
| Circulatory disease | -2.8189 | 1.9706 | ±3.9412 | -1.430 | 0.1526 |  |
| Avg. daily mean/SD | +0.3002 | 0.3900 | ±0.7799 | +0.770 | 0.4415 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **401**, R² = **0.1805**, Adj R² = **0.1574**, F-statistic = **7.79** (p = **3.10e-12**), Residual SE = **11.555** on **389** df, AIC = **3112.4**, BIC = **3160.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.4446** | 5.8474 | ±11.6949 | **+7.601** | **2.95e-14** | *** |
| Education: graduate level (vs college) | -2.3022 | 1.1943 | ±2.3886 | -1.928 | 0.0539 | . |
| Education: high school or below (vs college) | +1.2044 | 2.6653 | ±5.3305 | +0.452 | 0.6513 |  |
| Site: UCSD (vs UAB) | -1.5804 | 1.5669 | ±3.1339 | -1.009 | 0.3132 |  |
| Site: UW (vs UAB) | -2.5847 | 1.4851 | ±2.9702 | -1.740 | 0.0818 | . |
| **Age (years)** | **-0.4026** | 0.0559 | ±0.1118 | **-7.202** | **5.94e-13** | *** |
| BMI (kg/m2) | -0.0034 | 0.0828 | ±0.1657 | -0.041 | 0.9671 |  |
| Hypertension | +1.9305 | 1.3834 | ±2.7668 | +1.395 | 0.1629 |  |
| High cholesterol | -0.8228 | 1.2250 | ±2.4500 | -0.672 | 0.5018 |  |
| Kidney disease | -1.8570 | 2.3865 | ±4.7729 | -0.778 | 0.4365 |  |
| Circulatory disease | -2.7493 | 1.9503 | ±3.9005 | -1.410 | 0.1586 |  |
| MAG (mg/dL/h) | +0.1907 | 0.1055 | ±0.2110 | +1.808 | 0.0706 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1494**, F-statistic = **7.39** (p = **1.60e-11**), Residual SE = **11.610** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7028** | 6.4218 | ±12.8435 | **+8.051** | **8.20e-16** | *** |
| Education: graduate level (vs college) | -2.3247 | 1.2001 | ±2.4001 | -1.937 | 0.0527 | . |
| Education: high school or below (vs college) | +1.5110 | 2.7040 | ±5.4080 | +0.559 | 0.5763 |  |
| Site: UCSD (vs UAB) | -1.6976 | 1.5764 | ±3.1527 | -1.077 | 0.2815 |  |
| Site: UW (vs UAB) | -2.8651 | 1.4977 | ±2.9955 | -1.913 | 0.0558 | . |
| **Age (years)** | **-0.4123** | 0.0570 | ±0.1139 | **-7.237** | **4.58e-13** | *** |
| BMI (kg/m2) | -0.0105 | 0.0838 | ±0.1676 | -0.125 | 0.9005 |  |
| Hypertension | +1.8341 | 1.3985 | ±2.7970 | +1.311 | 0.1897 |  |
| High cholesterol | -0.7464 | 1.2313 | ±2.4627 | -0.606 | 0.5444 |  |
| Kidney disease | -1.4780 | 2.4031 | ±4.8062 | -0.615 | 0.5385 |  |
| Circulatory disease | -2.7921 | 1.9567 | ±3.9134 | -1.427 | 0.1536 |  |
| Avg. daily range (mg/dL) | +0.0017 | 0.0564 | ±0.1127 | +0.031 | 0.9754 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **401**, R² = **0.1742**, Adj R² = **0.1509**, F-statistic = **7.46** (p = **1.18e-11**), Residual SE = **11.600** on **389** df, AIC = **3115.5**, BIC = **3163.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6068** | 4.9629 | ±9.9259 | **+10.197** | **2.05e-24** | *** |
| **Education: graduate level (vs college)** | **-2.3568** | 1.2010 | ±2.4020 | **-1.962** | **0.0497** | * |
| Education: high school or below (vs college) | +1.4274 | 2.7289 | ±5.4579 | +0.523 | 0.6009 |  |
| Site: UCSD (vs UAB) | -1.6497 | 1.5754 | ±3.1508 | -1.047 | 0.2950 |  |
| Site: UW (vs UAB) | -2.8841 | 1.4854 | ±2.9709 | -1.942 | 0.0522 | . |
| **Age (years)** | **-0.4120** | 0.0569 | ±0.1138 | **-7.243** | **4.37e-13** | *** |
| BMI (kg/m2) | -0.0118 | 0.0838 | ±0.1677 | -0.141 | 0.8881 |  |
| Hypertension | +1.7403 | 1.3942 | ±2.7884 | +1.248 | 0.2119 |  |
| High cholesterol | -0.7647 | 1.2252 | ±2.4503 | -0.624 | 0.5325 |  |
| Kidney disease | -1.4826 | 2.4027 | ±4.8053 | -0.617 | 0.5372 |  |
| Circulatory disease | -2.8843 | 1.9706 | ±3.9412 | -1.464 | 0.1433 |  |
| SD of daily means (mg/dL) | +0.2559 | 0.3566 | ±0.7133 | +0.718 | 0.4730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **401**, R² = **0.1893**, Adj R² = **0.1664**, F-statistic = **8.26** (p = **4.67e-13**), Residual SE = **11.493** on **389** df, AIC = **3108.1**, BIC = **3156.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+594.3739** | 186.8112 | ±373.6224 | **+3.182** | **0.0015** | ** |
| Education: graduate level (vs college) | -2.1546 | 1.1933 | ±2.3867 | -1.806 | 0.0710 | . |
| Education: high school or below (vs college) | +1.7077 | 2.6471 | ±5.2943 | +0.645 | 0.5188 |  |
| Site: UCSD (vs UAB) | -1.4528 | 1.5587 | ±3.1173 | -0.932 | 0.3513 |  |
| Site: UW (vs UAB) | -2.7145 | 1.4618 | ±2.9236 | -1.857 | 0.0633 | . |
| **Age (years)** | **-0.4073** | 0.0560 | ±0.1121 | **-7.269** | **3.63e-13** | *** |
| BMI (kg/m2) | -0.0060 | 0.0904 | ±0.1809 | -0.066 | 0.9472 |  |
| Hypertension | +1.7794 | 1.3716 | ±2.7433 | +1.297 | 0.1945 |  |
| High cholesterol | -0.7872 | 1.2207 | ±2.4414 | -0.645 | 0.5190 |  |
| Kidney disease | -1.9653 | 2.4871 | ±4.9741 | -0.790 | 0.4294 |  |
| Circulatory disease | -2.7643 | 1.9249 | ±3.8497 | -1.436 | 0.1510 |  |
| **Time in range 70-180, pooled (%)** | **-5.4562** | 1.8760 | ±3.7520 | **-2.908** | **0.0036** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **401**, R² = **0.1875**, Adj R² = **0.1645**, F-statistic = **8.16** (p = **6.98e-13**), Residual SE = **11.506** on **389** df, AIC = **3109.0**, BIC = **3156.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+545.0446** | 181.5752 | ±363.1504 | **+3.002** | **0.0027** | ** |
| Education: graduate level (vs college) | -2.1175 | 1.1912 | ±2.3825 | -1.778 | 0.0755 | . |
| Education: high school or below (vs college) | +1.7452 | 2.6557 | ±5.3114 | +0.657 | 0.5111 |  |
| Site: UCSD (vs UAB) | -1.5570 | 1.5580 | ±3.1160 | -0.999 | 0.3176 |  |
| **Site: UW (vs UAB)** | **-2.8678** | 1.4627 | ±2.9253 | **-1.961** | **0.0499** | * |
| **Age (years)** | **-0.4072** | 0.0557 | ±0.1115 | **-7.305** | **2.76e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0852 | ±0.1703 | -0.125 | 0.9004 |  |
| Hypertension | +1.9912 | 1.3832 | ±2.7663 | +1.440 | 0.1500 |  |
| High cholesterol | -0.8507 | 1.2178 | ±2.4356 | -0.699 | 0.4848 |  |
| Kidney disease | -1.7476 | 2.4615 | ±4.9231 | -0.710 | 0.4777 |  |
| Circulatory disease | -2.9030 | 1.9161 | ±3.8321 | -1.515 | 0.1297 |  |
| **Avg. daily time in range 70-180 (%)** | **-4.9560** | 1.8203 | ±3.6406 | **-2.723** | **0.0065** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1731**, Adj R² = **0.1497**, F-statistic = **7.40** (p = **1.49e-11**), Residual SE = **11.608** on **389** df, AIC = **3116.0**, BIC = **3164.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6570** | 4.7498 | ±9.4996 | **+10.876** | **1.51e-27** | *** |
| Education: graduate level (vs college) | -2.3216 | 1.1982 | ±2.3965 | -1.938 | 0.0527 | . |
| Education: high school or below (vs college) | +1.5424 | 2.7069 | ±5.4138 | +0.570 | 0.5688 |  |
| Site: UCSD (vs UAB) | -1.6068 | 1.5888 | ±3.1775 | -1.011 | 0.3118 |  |
| Site: UW (vs UAB) | -2.8187 | 1.4899 | ±2.9798 | -1.892 | 0.0585 | . |
| **Age (years)** | **-0.4118** | 0.0568 | ±0.1136 | **-7.251** | **4.14e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0836 | ±0.1673 | -0.128 | 0.8984 |  |
| Hypertension | +1.8020 | 1.3975 | ±2.7950 | +1.289 | 0.1972 |  |
| High cholesterol | -0.7420 | 1.2285 | ±2.4570 | -0.604 | 0.5459 |  |
| Kidney disease | -1.4026 | 2.4160 | ±4.8320 | -0.581 | 0.5615 |  |
| Circulatory disease | -2.8190 | 1.9642 | ±3.9283 | -1.435 | 0.1512 |  |
| Any reading < 54 during wear (0/1) | +0.6340 | 1.4860 | ±2.9720 | +0.427 | 0.6696 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1797**, Adj R² = **0.1566**, F-statistic = **7.75** (p = **3.67e-12**), Residual SE = **11.561** on **389** df, AIC = **3112.8**, BIC = **3160.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2328** | 4.6963 | ±9.3926 | **+10.909** | **1.04e-27** | *** |
| Education: graduate level (vs college) | -2.3108 | 1.1939 | ±2.3878 | -1.936 | 0.0529 | . |
| Education: high school or below (vs college) | +1.7919 | 2.7046 | ±5.4092 | +0.663 | 0.5076 |  |
| Site: UCSD (vs UAB) | -1.3786 | 1.5842 | ±3.1685 | -0.870 | 0.3842 |  |
| Site: UW (vs UAB) | -2.7247 | 1.4806 | ±2.9613 | -1.840 | 0.0657 | . |
| **Age (years)** | **-0.4045** | 0.0563 | ±0.1126 | **-7.185** | **6.71e-13** | *** |
| BMI (kg/m2) | -0.0226 | 0.0812 | ±0.1624 | -0.278 | 0.7807 |  |
| Hypertension | +1.6102 | 1.3921 | ±2.7843 | +1.157 | 0.2474 |  |
| High cholesterol | -0.6617 | 1.2240 | ±2.4481 | -0.541 | 0.5888 |  |
| Kidney disease | -1.2492 | 2.4128 | ±4.8257 | -0.518 | 0.6047 |  |
| Circulatory disease | -2.9755 | 2.0001 | ±4.0003 | -1.488 | 0.1368 |  |
| Time < 54 (%) | +19.2074 | 13.8891 | ±27.7781 | +1.383 | 0.1667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1794**, Adj R² = **0.1562**, F-statistic = **7.73** (p = **3.92e-12**), Residual SE = **11.563** on **389** df, AIC = **3113.0**, BIC = **3160.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6176** | 4.6898 | ±9.3796 | **+11.006** | **3.56e-28** | *** |
| Education: graduate level (vs college) | -2.3327 | 1.1954 | ±2.3907 | -1.951 | 0.0510 | . |
| Education: high school or below (vs college) | +1.6220 | 2.6872 | ±5.3744 | +0.604 | 0.5461 |  |
| Site: UCSD (vs UAB) | -1.5730 | 1.5731 | ±3.1462 | -1.000 | 0.3174 |  |
| Site: UW (vs UAB) | -2.8766 | 1.4913 | ±2.9827 | -1.929 | 0.0537 | . |
| **Age (years)** | **-0.4101** | 0.0564 | ±0.1127 | **-7.276** | **3.43e-13** | *** |
| BMI (kg/m2) | -0.0163 | 0.0828 | ±0.1656 | -0.197 | 0.8435 |  |
| Hypertension | +1.7835 | 1.3896 | ±2.7792 | +1.283 | 0.1993 |  |
| High cholesterol | -0.7271 | 1.2238 | ±2.4476 | -0.594 | 0.5525 |  |
| Kidney disease | -1.3217 | 2.4130 | ±4.8261 | -0.548 | 0.5839 |  |
| Circulatory disease | -3.0878 | 2.0112 | ±4.0225 | -1.535 | 0.1247 |  |
| Avg. daily time < 54 (%) | +24.6560 | 21.4509 | ±42.9017 | +1.149 | 0.2504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1745**, Adj R² = **0.1512**, F-statistic = **7.48** (p = **1.11e-11**), Residual SE = **11.598** on **389** df, AIC = **3115.4**, BIC = **3163.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3274** | 4.7507 | ±9.5013 | **+10.804** | **3.29e-27** | *** |
| Education: graduate level (vs college) | -2.2937 | 1.1998 | ±2.3995 | -1.912 | 0.0559 | . |
| Education: high school or below (vs college) | +1.3932 | 2.7014 | ±5.4029 | +0.516 | 0.6060 |  |
| Site: UCSD (vs UAB) | -1.6183 | 1.5723 | ±3.1447 | -1.029 | 0.3034 |  |
| Site: UW (vs UAB) | -2.7803 | 1.4831 | ±2.9663 | -1.875 | 0.0608 | . |
| **Age (years)** | **-0.4119** | 0.0566 | ±0.1133 | **-7.273** | **3.51e-13** | *** |
| BMI (kg/m2) | -0.0097 | 0.0838 | ±0.1675 | -0.116 | 0.9075 |  |
| Hypertension | +1.9259 | 1.3865 | ±2.7730 | +1.389 | 0.1648 |  |
| High cholesterol | -0.8530 | 1.2460 | ±2.4920 | -0.685 | 0.4936 |  |
| Kidney disease | -1.3913 | 2.3878 | ±4.7755 | -0.583 | 0.5601 |  |
| Circulatory disease | -2.7642 | 1.9573 | ±3.9145 | -1.412 | 0.1579 |  |
| Time 54-69, pooled (%) | +2.8938 | 3.1263 | ±6.2526 | +0.926 | 0.3546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **401**, R² = **0.1733**, Adj R² = **0.1499**, F-statistic = **7.41** (p = **1.43e-11**), Residual SE = **11.606** on **389** df, AIC = **3115.9**, BIC = **3163.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6284** | 4.7215 | ±9.4429 | **+10.935** | **7.86e-28** | *** |
| Education: graduate level (vs college) | -2.2920 | 1.2011 | ±2.4022 | -1.908 | 0.0564 | . |
| Education: high school or below (vs college) | +1.4494 | 2.7093 | ±5.4187 | +0.535 | 0.5927 |  |
| Site: UCSD (vs UAB) | -1.6747 | 1.5751 | ±3.1503 | -1.063 | 0.2877 |  |
| Site: UW (vs UAB) | -2.8474 | 1.4858 | ±2.9717 | -1.916 | 0.0553 | . |
| **Age (years)** | **-0.4127** | 0.0567 | ±0.1133 | **-7.283** | **3.27e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0837 | ±0.1675 | -0.128 | 0.8984 |  |
| Hypertension | +1.9326 | 1.3982 | ±2.7964 | +1.382 | 0.1669 |  |
| High cholesterol | -0.7995 | 1.2466 | ±2.4931 | -0.641 | 0.5213 |  |
| Kidney disease | -1.4349 | 2.3992 | ±4.7983 | -0.598 | 0.5498 |  |
| Circulatory disease | -2.8140 | 1.9613 | ±3.9227 | -1.435 | 0.1514 |  |
| Avg. daily time 54-69 (%) | +1.6802 | 3.2212 | ±6.4424 | +0.522 | 0.6019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **401**, R² = **0.1763**, Adj R² = **0.1530**, F-statistic = **7.57** (p = **7.69e-12**), Residual SE = **11.586** on **389** df, AIC = **3114.5**, BIC = **3162.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0801** | 4.7528 | ±9.5056 | **+10.747** | **6.10e-27** | *** |
| Education: graduate level (vs college) | -2.2823 | 1.1999 | ±2.3998 | -1.902 | 0.0572 | . |
| Education: high school or below (vs college) | +1.4168 | 2.6936 | ±5.3871 | +0.526 | 0.5989 |  |
| Site: UCSD (vs UAB) | -1.5372 | 1.5703 | ±3.1407 | -0.979 | 0.3276 |  |
| Site: UW (vs UAB) | -2.7312 | 1.4804 | ±2.9607 | -1.845 | 0.0650 | . |
| **Age (years)** | **-0.4103** | 0.0565 | ±0.1130 | **-7.262** | **3.82e-13** | *** |
| BMI (kg/m2) | -0.0117 | 0.0833 | ±0.1666 | -0.141 | 0.8879 |  |
| Hypertension | +1.9075 | 1.3886 | ±2.7771 | +1.374 | 0.1695 |  |
| High cholesterol | -0.8635 | 1.2424 | ±2.4848 | -0.695 | 0.4870 |  |
| Kidney disease | -1.3292 | 2.3867 | ±4.7734 | -0.557 | 0.5776 |  |
| Circulatory disease | -2.7921 | 1.9680 | ±3.9360 | -1.419 | 0.1560 |  |
| Time < 70 (%) | +3.6209 | 3.0107 | ±6.0214 | +1.203 | 0.2291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **401**, R² = **0.1743**, Adj R² = **0.1509**, F-statistic = **7.46** (p = **1.17e-11**), Residual SE = **11.600** on **389** df, AIC = **3115.5**, BIC = **3163.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4958** | 4.7157 | ±9.4313 | **+10.920** | **9.23e-28** | *** |
| Education: graduate level (vs college) | -2.2753 | 1.2043 | ±2.4087 | -1.889 | 0.0589 | . |
| Education: high school or below (vs college) | +1.4306 | 2.7030 | ±5.4059 | +0.529 | 0.5966 |  |
| Site: UCSD (vs UAB) | -1.6494 | 1.5732 | ±3.1464 | -1.048 | 0.2944 |  |
| Site: UW (vs UAB) | -2.8379 | 1.4850 | ±2.9700 | -1.911 | 0.0560 | . |
| **Age (years)** | **-0.4126** | 0.0566 | ±0.1132 | **-7.293** | **3.04e-13** | *** |
| BMI (kg/m2) | -0.0113 | 0.0837 | ±0.1673 | -0.135 | 0.8928 |  |
| Hypertension | +1.9771 | 1.4029 | ±2.8058 | +1.409 | 0.1587 |  |
| High cholesterol | -0.8234 | 1.2447 | ±2.4895 | -0.661 | 0.5083 |  |
| Kidney disease | -1.4016 | 2.3990 | ±4.7979 | -0.584 | 0.5591 |  |
| Circulatory disease | -2.8554 | 1.9687 | ±3.9374 | -1.450 | 0.1469 |  |
| Avg. daily time < 70 (%) | +2.5112 | 3.1656 | ±6.3311 | +0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1800**, Adj R² = **0.1568**, F-statistic = **7.76** (p = **3.49e-12**), Residual SE = **11.559** on **389** df, AIC = **3112.7**, BIC = **3160.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1956.8131 | 1317.4937 | ±2634.9875 | +1.485 | 0.1375 |  |
| Education: graduate level (vs college) | -2.3105 | 1.1934 | ±2.3867 | -1.936 | 0.0529 | . |
| Education: high school or below (vs college) | +1.8016 | 2.7050 | ±5.4099 | +0.666 | 0.5054 |  |
| Site: UCSD (vs UAB) | -1.3557 | 1.5868 | ±3.1735 | -0.854 | 0.3929 |  |
| Site: UW (vs UAB) | -2.7055 | 1.4808 | ±2.9615 | -1.827 | 0.0677 | . |
| **Age (years)** | **-0.4032** | 0.0564 | ±0.1128 | **-7.152** | **8.54e-13** | *** |
| BMI (kg/m2) | -0.0212 | 0.0814 | ±0.1628 | -0.260 | 0.7948 |  |
| Hypertension | +1.6246 | 1.3908 | ±2.7817 | +1.168 | 0.2428 |  |
| High cholesterol | -0.6688 | 1.2239 | ±2.4479 | -0.546 | 0.5848 |  |
| Kidney disease | -1.2540 | 2.4123 | ±4.8245 | -0.520 | 0.6032 |  |
| Circulatory disease | -2.9752 | 2.0002 | ±4.0004 | -1.487 | 0.1369 |  |
| Time 54-250, pooled (%) | -19.0572 | 13.1816 | ±26.3633 | -1.446 | 0.1482 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1799**, Adj R² = **0.1568**, F-statistic = **7.76** (p = **3.52e-12**), Residual SE = **11.560** on **389** df, AIC = **3112.7**, BIC = **3160.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2553.9345 | 1998.0592 | ±3996.1183 | +1.278 | 0.2012 |  |
| Education: graduate level (vs college) | -2.3319 | 1.1943 | ±2.3885 | -1.953 | 0.0509 | . |
| Education: high school or below (vs college) | +1.6411 | 2.6875 | ±5.3751 | +0.611 | 0.5414 |  |
| Site: UCSD (vs UAB) | -1.5345 | 1.5735 | ±3.1469 | -0.975 | 0.3294 |  |
| Site: UW (vs UAB) | -2.8475 | 1.4869 | ±2.9738 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.4082** | 0.0563 | ±0.1127 | **-7.246** | **4.30e-13** | *** |
| BMI (kg/m2) | -0.0145 | 0.0832 | ±0.1663 | -0.174 | 0.8617 |  |
| Hypertension | +1.8011 | 1.3898 | ±2.7796 | +1.296 | 0.1950 |  |
| High cholesterol | -0.7362 | 1.2239 | ±2.4478 | -0.602 | 0.5475 |  |
| Kidney disease | -1.3239 | 2.4131 | ±4.8261 | -0.549 | 0.5832 |  |
| Circulatory disease | -3.0938 | 2.0109 | ±4.0218 | -1.539 | 0.1239 |  |
| Avg. daily time 54-250 (%) | -25.0253 | 19.9850 | ±39.9699 | -1.252 | 0.2105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **401**, R² = **0.1816**, Adj R² = **0.1585**, F-statistic = **7.85** (p = **2.46e-12**), Residual SE = **11.548** on **389** df, AIC = **3111.9**, BIC = **3159.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3593** | 4.9131 | ±9.8261 | **+10.250** | **1.18e-24** | *** |
| Education: graduate level (vs college) | -2.2442 | 1.1935 | ±2.3870 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | +1.7742 | 2.6757 | ±5.3514 | +0.663 | 0.5073 |  |
| Site: UCSD (vs UAB) | -1.7039 | 1.5734 | ±3.1468 | -1.083 | 0.2788 |  |
| **Site: UW (vs UAB)** | **-2.9143** | 1.4735 | ±2.9469 | **-1.978** | **0.0479** | * |
| **Age (years)** | **-0.4110** | 0.0568 | ±0.1135 | **-7.241** | **4.47e-13** | *** |
| BMI (kg/m2) | -0.0060 | 0.0898 | ±0.1796 | -0.067 | 0.9465 |  |
| Hypertension | +1.6987 | 1.3747 | ±2.7493 | +1.236 | 0.2166 |  |
| High cholesterol | -0.6392 | 1.2325 | ±2.4651 | -0.519 | 0.6040 |  |
| Kidney disease | -2.0285 | 2.5014 | ±5.0027 | -0.811 | 0.4174 |  |
| Circulatory disease | -2.7687 | 1.9192 | ±3.8384 | -1.443 | 0.1491 |  |
| **Time 181-250, pooled (%)** | **+4.2965** | 2.1129 | ±4.2258 | **+2.033** | **0.0420** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **401**, R² = **0.1839**, Adj R² = **0.1608**, F-statistic = **7.97** (p = **1.52e-12**), Residual SE = **11.532** on **389** df, AIC = **3110.8**, BIC = **3158.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2582** | 4.7409 | ±9.4818 | **+10.601** | **2.95e-26** | *** |
| Education: graduate level (vs college) | -2.2245 | 1.1891 | ±2.3782 | -1.871 | 0.0614 | . |
| Education: high school or below (vs college) | +1.8811 | 2.6716 | ±5.3431 | +0.704 | 0.4814 |  |
| Site: UCSD (vs UAB) | -1.6655 | 1.5676 | ±3.1352 | -1.062 | 0.2880 |  |
| **Site: UW (vs UAB)** | **-2.9303** | 1.4685 | ±2.9371 | **-1.995** | **0.0460** | * |
| **Age (years)** | **-0.4072** | 0.0563 | ±0.1126 | **-7.230** | **4.83e-13** | *** |
| BMI (kg/m2) | -0.0099 | 0.0853 | ±0.1705 | -0.116 | 0.9075 |  |
| Hypertension | +1.7082 | 1.3749 | ±2.7498 | +1.242 | 0.2141 |  |
| High cholesterol | -0.7007 | 1.2259 | ±2.4518 | -0.572 | 0.5676 |  |
| Kidney disease | -1.8653 | 2.4668 | ±4.9337 | -0.756 | 0.4495 |  |
| Circulatory disease | -2.7768 | 1.9107 | ±3.8214 | -1.453 | 0.1461 |  |
| **Avg. daily time 181-250 (%)** | **+4.7236** | 2.0625 | ±4.1251 | **+2.290** | **0.0220** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **401**, R² = **0.1817**, Adj R² = **0.1586**, F-statistic = **7.85** (p = **2.41e-12**), Residual SE = **11.547** on **389** df, AIC = **3111.9**, BIC = **3159.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3211** | 4.9199 | ±9.8398 | **+10.228** | **1.48e-24** | *** |
| Education: graduate level (vs college) | -2.2438 | 1.1935 | ±2.3870 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | +1.7777 | 2.6757 | ±5.3513 | +0.664 | 0.5064 |  |
| Site: UCSD (vs UAB) | -1.6982 | 1.5732 | ±3.1464 | -1.079 | 0.2804 |  |
| **Site: UW (vs UAB)** | **-2.9099** | 1.4732 | ±2.9464 | **-1.975** | **0.0482** | * |
| **Age (years)** | **-0.4107** | 0.0568 | ±0.1135 | **-7.236** | **4.62e-13** | *** |
| BMI (kg/m2) | -0.0057 | 0.0899 | ±0.1797 | -0.063 | 0.9494 |  |
| Hypertension | +1.7011 | 1.3748 | ±2.7495 | +1.237 | 0.2159 |  |
| High cholesterol | -0.6403 | 1.2323 | ±2.4647 | -0.520 | 0.6034 |  |
| Kidney disease | -2.0310 | 2.5018 | ±5.0036 | -0.812 | 0.4169 |  |
| Circulatory disease | -2.7689 | 1.9192 | ±3.8385 | -1.443 | 0.1491 |  |
| **Time > 180 (%)** | **+4.3103** | 2.1049 | ±4.2097 | **+2.048** | **0.0406** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1840**, Adj R² = **0.1609**, F-statistic = **7.97** (p = **1.49e-12**), Residual SE = **11.531** on **389** df, AIC = **3110.7**, BIC = **3158.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2155** | 4.7461 | ±9.4923 | **+10.580** | **3.68e-26** | *** |
| Education: graduate level (vs college) | -2.2242 | 1.1890 | ±2.3781 | -1.871 | 0.0614 | . |
| Education: high school or below (vs college) | +1.8849 | 2.6716 | ±5.3432 | +0.706 | 0.4805 |  |
| Site: UCSD (vs UAB) | -1.6586 | 1.5673 | ±3.1345 | -1.058 | 0.2899 |  |
| **Site: UW (vs UAB)** | **-2.9249** | 1.4682 | ±2.9363 | **-1.992** | **0.0463** | * |
| **Age (years)** | **-0.4069** | 0.0563 | ±0.1126 | **-7.224** | **5.06e-13** | *** |
| BMI (kg/m2) | -0.0095 | 0.0853 | ±0.1706 | -0.112 | 0.9110 |  |
| Hypertension | +1.7115 | 1.3750 | ±2.7501 | +1.245 | 0.2133 |  |
| High cholesterol | -0.7024 | 1.2257 | ±2.4514 | -0.573 | 0.5666 |  |
| Kidney disease | -1.8668 | 2.4670 | ±4.9341 | -0.757 | 0.4492 |  |
| Circulatory disease | -2.7771 | 1.9108 | ±3.8216 | -1.453 | 0.1461 |  |
| **Avg. daily time > 180 (%)** | **+4.7306** | 2.0511 | ±4.1022 | **+2.306** | **0.0211** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1819**, Adj R² = **0.1588**, F-statistic = **7.86** (p = **2.32e-12**), Residual SE = **11.546** on **389** df, AIC = **3111.8**, BIC = **3159.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7546** | 4.6041 | ±9.2082 | **+11.024** | **2.93e-28** | *** |
| Education: graduate level (vs college) | -2.1439 | 1.1939 | ±2.3878 | -1.796 | 0.0725 | . |
| Education: high school or below (vs college) | +1.5472 | 2.6471 | ±5.2942 | +0.584 | 0.5589 |  |
| Site: UCSD (vs UAB) | -1.8152 | 1.5649 | ±3.1299 | -1.160 | 0.2461 |  |
| **Site: UW (vs UAB)** | **-3.0237** | 1.4703 | ±2.9406 | **-2.056** | **0.0397** | * |
| **Age (years)** | **-0.3924** | 0.0562 | ±0.1124 | **-6.985** | **2.85e-12** | *** |
| BMI (kg/m2) | -0.0231 | 0.0819 | ±0.1637 | -0.282 | 0.7778 |  |
| Hypertension | +1.5710 | 1.3572 | ±2.7144 | +1.158 | 0.2471 |  |
| High cholesterol | -0.8321 | 1.2169 | ±2.4338 | -0.684 | 0.4941 |  |
| Kidney disease | -1.6556 | 2.4416 | ±4.8832 | -0.678 | 0.4977 |  |
| Circulatory disease | -2.6131 | 1.9786 | ±3.9573 | -1.321 | 0.1866 |  |
| Nocturnal time > 180 (%) | +3.2972 | 2.0228 | ±4.0455 | +1.630 | 0.1031 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 403; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1824**, F-statistic = **9.97** (p = **6.09e-15**), Residual SE = **6.960** on **392** df, AIC = **2718.3**, BIC = **2762.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9407** | 3.8694 | ±7.7387 | **+16.525** | **2.43e-61** | *** |
| **Education: graduate level (vs college)** | **-1.9757** | 0.7628 | ±1.5255 | **-2.590** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.8025** | 1.2822 | ±2.5644 | **-2.186** | **0.0288** | * |
| **Site: UCSD (vs UAB)** | **-1.9532** | 0.9505 | ±1.9009 | **-2.055** | **0.0399** | * |
| **Site: UW (vs UAB)** | **-2.7252** | 0.8541 | ±1.7081 | **-3.191** | **0.0014** | ** |
| **Age (years)** | **-0.1448** | 0.0361 | ±0.0722 | **-4.008** | **6.11e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0761 | ±0.1521 | **+3.389** | **7.02e-04** | *** |
| **Hypertension** | **+2.0570** | 0.8072 | ±1.6144 | **+2.548** | **0.0108** | * |
| High cholesterol | -0.3663 | 0.7573 | ±1.5146 | -0.484 | 0.6286 |  |
| Kidney disease | -0.3222 | 2.0209 | ±4.0418 | -0.159 | 0.8733 |  |
| Circulatory disease | -1.7166 | 0.9110 | ±1.8220 | -1.884 | 0.0595 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.5952** | 6.9779 | ±13.9557 | **+9.114** | **7.95e-20** | *** |
| **Education: graduate level (vs college)** | **-1.9734** | 0.7621 | ±1.5242 | **-2.589** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.8062** | 1.2860 | ±2.5720 | **-2.182** | **0.0291** | * |
| **Site: UCSD (vs UAB)** | **-1.9507** | 0.9490 | ±1.8980 | **-2.055** | **0.0398** | * |
| **Site: UW (vs UAB)** | **-2.7220** | 0.8541 | ±1.7082 | **-3.187** | **0.0014** | ** |
| **Age (years)** | **-0.1449** | 0.0368 | ±0.0737 | **-3.933** | **8.38e-05** | *** |
| **BMI (kg/m2)** | **+0.2574** | 0.0778 | ±0.1556 | **+3.309** | **9.35e-04** | *** |
| **Hypertension** | **+2.0534** | 0.8132 | ±1.6264 | **+2.525** | **0.0116** | * |
| High cholesterol | -0.3762 | 0.7727 | ±1.5454 | -0.487 | 0.6264 |  |
| Kidney disease | -0.3166 | 2.0203 | ±4.0406 | -0.157 | 0.8755 |  |
| Circulatory disease | -1.7141 | 0.9174 | ±1.8349 | -1.868 | 0.0617 | . |
| HbA1c (%) | +0.0665 | 1.2603 | ±2.5206 | +0.053 | 0.9579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **403**, R² = **0.2030**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.87e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.9736** | 7.0046 | ±14.0092 | **+8.848** | **8.94e-19** | *** |
| **Education: graduate level (vs college)** | **-1.9676** | 0.7626 | ±1.5252 | **-2.580** | **0.0099** | ** |
| **Education: high school or below (vs college)** | **-2.7790** | 1.2865 | ±2.5731 | **-2.160** | **0.0308** | * |
| **Site: UCSD (vs UAB)** | **-1.9680** | 0.9546 | ±1.9093 | **-2.062** | **0.0393** | * |
| **Site: UW (vs UAB)** | **-2.7431** | 0.8583 | ±1.7166 | **-3.196** | **0.0014** | ** |
| **Age (years)** | **-0.1443** | 0.0363 | ±0.0727 | **-3.969** | **7.20e-05** | *** |
| **BMI (kg/m2)** | **+0.2566** | 0.0762 | ±0.1523 | **+3.369** | **7.55e-04** | *** |
| **Hypertension** | **+2.0336** | 0.8061 | ±1.6123 | **+2.523** | **0.0116** | * |
| High cholesterol | -0.3575 | 0.7650 | ±1.5300 | -0.467 | 0.6403 |  |
| Kidney disease | -0.3238 | 2.0431 | ±4.0862 | -0.158 | 0.8741 |  |
| Circulatory disease | -1.7232 | 0.9132 | ±1.8263 | -1.887 | 0.0592 | . |
| Mean glucose (mg/dL) | +0.0174 | 0.0493 | ±0.0986 | +0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **403**, R² = **0.2030**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.87e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.5701** | 13.2421 | ±26.4841 | **+4.499** | **6.84e-06** | *** |
| **Education: graduate level (vs college)** | **-1.9676** | 0.7626 | ±1.5252 | **-2.580** | **0.0099** | ** |
| **Education: high school or below (vs college)** | **-2.7790** | 1.2865 | ±2.5731 | **-2.160** | **0.0308** | * |
| **Site: UCSD (vs UAB)** | **-1.9680** | 0.9546 | ±1.9093 | **-2.062** | **0.0393** | * |
| **Site: UW (vs UAB)** | **-2.7431** | 0.8583 | ±1.7166 | **-3.196** | **0.0014** | ** |
| **Age (years)** | **-0.1443** | 0.0363 | ±0.0727 | **-3.969** | **7.20e-05** | *** |
| **BMI (kg/m2)** | **+0.2566** | 0.0762 | ±0.1523 | **+3.369** | **7.55e-04** | *** |
| **Hypertension** | **+2.0336** | 0.8061 | ±1.6123 | **+2.523** | **0.0116** | * |
| High cholesterol | -0.3575 | 0.7650 | ±1.5300 | -0.467 | 0.6403 |  |
| Kidney disease | -0.3238 | 2.0431 | ±4.0862 | -0.158 | 0.8741 |  |
| Circulatory disease | -1.7232 | 0.9132 | ±1.8263 | -1.887 | 0.0592 | . |
| GMI (%) | +0.7261 | 2.0616 | ±4.1233 | +0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **403**, R² = **0.2051**, Adj R² = **0.1827**, F-statistic = **9.17** (p = **1.18e-14**), Residual SE = **6.958** on **391** df, AIC = **2719.1**, BIC = **2767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3044** | 5.5368 | ±11.0736 | **+10.711** | **9.04e-27** | *** |
| **Education: graduate level (vs college)** | **-1.9307** | 0.7543 | ±1.5086 | **-2.560** | **0.0105** | * |
| **Education: high school or below (vs college)** | **-2.7401** | 1.2816 | ±2.5633 | **-2.138** | **0.0325** | * |
| **Site: UCSD (vs UAB)** | **-2.0473** | 0.9574 | ±1.9148 | **-2.138** | **0.0325** | * |
| **Site: UW (vs UAB)** | **-2.8005** | 0.8604 | ±1.7207 | **-3.255** | **0.0011** | ** |
| **Age (years)** | **-0.1390** | 0.0365 | ±0.0730 | **-3.810** | **1.39e-04** | *** |
| **BMI (kg/m2)** | **+0.2499** | 0.0756 | ±0.1511 | **+3.307** | **9.43e-04** | *** |
| **Hypertension** | **+1.9866** | 0.8041 | ±1.6082 | **+2.470** | **0.0135** | * |
| High cholesterol | -0.3642 | 0.7609 | ±1.5219 | -0.479 | 0.6322 |  |
| Kidney disease | -0.2376 | 2.0312 | ±4.0624 | -0.117 | 0.9069 |  |
| Circulatory disease | -1.6989 | 0.9102 | ±1.8204 | -1.867 | 0.0620 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0398 | 0.0375 | ±0.0749 | +1.062 | 0.2881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0050** | 4.4760 | ±8.9520 | **+14.300** | **2.20e-46** | *** |
| **Education: graduate level (vs college)** | **-1.9774** | 0.7620 | ±1.5240 | **-2.595** | **0.0095** | ** |
| **Education: high school or below (vs college)** | **-2.8034** | 1.2855 | ±2.5710 | **-2.181** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9544** | 0.9523 | ±1.9045 | **-2.052** | **0.0401** | * |
| **Site: UW (vs UAB)** | **-2.7267** | 0.8534 | ±1.7067 | **-3.195** | **0.0014** | ** |
| **Age (years)** | **-0.1447** | 0.0362 | ±0.0725 | **-3.994** | **6.50e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0763 | ±0.1527 | **+3.378** | **7.31e-04** | *** |
| **Hypertension** | **+2.0585** | 0.8054 | ±1.6109 | **+2.556** | **0.0106** | * |
| High cholesterol | -0.3678 | 0.7723 | ±1.5446 | -0.476 | 0.6339 |  |
| Kidney disease | -0.3177 | 2.1061 | ±4.2122 | -0.151 | 0.8801 |  |
| Circulatory disease | -1.7156 | 0.9091 | ±1.8183 | -1.887 | 0.0592 | . |
| Glucose SD, pooled (mg/dL) | -0.0039 | 0.1518 | ±0.3036 | -0.026 | 0.9795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0552** | 4.2939 | ±8.5877 | **+14.918** | **2.52e-50** | *** |
| **Education: graduate level (vs college)** | **-1.9794** | 0.7620 | ±1.5240 | **-2.598** | **0.0094** | ** |
| **Education: high school or below (vs college)** | **-2.8051** | 1.2857 | ±2.5715 | **-2.182** | **0.0291** | * |
| **Site: UCSD (vs UAB)** | **-1.9552** | 0.9510 | ±1.9021 | **-2.056** | **0.0398** | * |
| **Site: UW (vs UAB)** | **-2.7279** | 0.8526 | ±1.7052 | **-3.200** | **0.0014** | ** |
| **Age (years)** | **-0.1447** | 0.0363 | ±0.0725 | **-3.990** | **6.61e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0767 | ±0.1534 | **+3.363** | **7.71e-04** | *** |
| **Hypertension** | **+2.0590** | 0.8060 | ±1.6120 | **+2.555** | **0.0106** | * |
| High cholesterol | -0.3690 | 0.7692 | ±1.5383 | -0.480 | 0.6314 |  |
| Kidney disease | -0.3135 | 2.0937 | ±4.1874 | -0.150 | 0.8810 |  |
| Circulatory disease | -1.7160 | 0.9117 | ±1.8235 | -1.882 | 0.0598 | . |
| Avg. daily SD (mg/dL) | -0.0077 | 0.1497 | ±0.2995 | -0.051 | 0.9590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **403**, R² = **0.2029**, Adj R² = **0.1805**, F-statistic = **9.05** (p = **1.93e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.5642** | 4.2849 | ±8.5697 | **+15.068** | **2.63e-51** | *** |
| **Education: graduate level (vs college)** | **-1.9896** | 0.7643 | ±1.5286 | **-2.603** | **0.0092** | ** |
| **Education: high school or below (vs college)** | **-2.8040** | 1.2858 | ±2.5716 | **-2.181** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9693** | 0.9532 | ±1.9065 | **-2.066** | **0.0388** | * |
| **Site: UW (vs UAB)** | **-2.7446** | 0.8535 | ±1.7070 | **-3.216** | **0.0013** | ** |
| **Age (years)** | **-0.1445** | 0.0363 | ±0.0727 | **-3.977** | **6.99e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0763 | ±0.1526 | **+3.379** | **7.27e-04** | *** |
| **Hypertension** | **+2.0638** | 0.8075 | ±1.6149 | **+2.556** | **0.0106** | * |
| High cholesterol | -0.3783 | 0.7656 | ±1.5313 | -0.494 | 0.6213 |  |
| Kidney disease | -0.2792 | 2.0803 | ±4.1605 | -0.134 | 0.8932 |  |
| Circulatory disease | -1.7087 | 0.9092 | ±1.8185 | -1.879 | 0.0602 | . |
| CV (%) | -0.0425 | 0.1520 | ±0.3040 | -0.280 | 0.7797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **403**, R² = **0.2030**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.88e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.1212** | 4.5283 | ±9.0566 | **+13.939** | **3.66e-44** | *** |
| **Education: graduate level (vs college)** | **-1.9975** | 0.7654 | ±1.5307 | **-2.610** | **0.0091** | ** |
| **Education: high school or below (vs college)** | **-2.8004** | 1.2872 | ±2.5744 | **-2.176** | **0.0296** | * |
| **Site: UCSD (vs UAB)** | **-1.9707** | 0.9534 | ±1.9069 | **-2.067** | **0.0387** | * |
| **Site: UW (vs UAB)** | **-2.7474** | 0.8540 | ±1.7079 | **-3.217** | **0.0013** | ** |
| **Age (years)** | **-0.1445** | 0.0363 | ±0.0725 | **-3.983** | **6.81e-05** | *** |
| **BMI (kg/m2)** | **+0.2580** | 0.0763 | ±0.1525 | **+3.383** | **7.18e-04** | *** |
| **Hypertension** | **+2.0665** | 0.8071 | ±1.6142 | **+2.560** | **0.0105** | * |
| High cholesterol | -0.3847 | 0.7663 | ±1.5326 | -0.502 | 0.6157 |  |
| Kidney disease | -0.2772 | 2.0652 | ±4.1304 | -0.134 | 0.8932 |  |
| Circulatory disease | -1.7105 | 0.9116 | ±1.8232 | -1.876 | 0.0606 | . |
| Mean / SD ratio | +0.1182 | 0.3001 | ±0.6002 | +0.394 | 0.6936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **403**, R² = **0.2029**, Adj R² = **0.1805**, F-statistic = **9.05** (p = **1.92e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3668** | 4.4440 | ±8.8879 | **+14.259** | **3.94e-46** | *** |
| **Education: graduate level (vs college)** | **-1.9942** | 0.7651 | ±1.5303 | **-2.606** | **0.0092** | ** |
| **Education: high school or below (vs college)** | **-2.8033** | 1.2873 | ±2.5746 | **-2.178** | **0.0294** | * |
| **Site: UCSD (vs UAB)** | **-1.9639** | 0.9518 | ±1.9037 | **-2.063** | **0.0391** | * |
| **Site: UW (vs UAB)** | **-2.7412** | 0.8517 | ±1.7035 | **-3.218** | **0.0013** | ** |
| **Age (years)** | **-0.1444** | 0.0363 | ±0.0725 | **-3.982** | **6.85e-05** | *** |
| **BMI (kg/m2)** | **+0.2583** | 0.0765 | ±0.1529 | **+3.378** | **7.31e-04** | *** |
| **Hypertension** | **+2.0601** | 0.8080 | ±1.6159 | **+2.550** | **0.0108** | * |
| High cholesterol | -0.3772 | 0.7628 | ±1.5256 | -0.495 | 0.6209 |  |
| Kidney disease | -0.2866 | 2.0578 | ±4.1156 | -0.139 | 0.8892 |  |
| Circulatory disease | -1.7218 | 0.9151 | ±1.8302 | -1.882 | 0.0599 | . |
| Avg. daily mean/SD | +0.0713 | 0.2279 | ±0.4558 | +0.313 | 0.7543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **403**, R² = **0.2106**, Adj R² = **0.1883**, F-statistic = **9.48** (p = **3.46e-15**), Residual SE = **6.934** on **391** df, AIC = **2716.3**, BIC = **2764.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3990** | 4.2820 | ±8.5640 | **+13.872** | **9.39e-44** | *** |
| **Education: graduate level (vs college)** | **-1.9596** | 0.7619 | ±1.5238 | **-2.572** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.9910** | 1.2484 | ±2.4968 | **-2.396** | **0.0166** | * |
| **Site: UCSD (vs UAB)** | **-1.8823** | 0.9409 | ±1.8818 | **-2.001** | **0.0454** | * |
| **Site: UW (vs UAB)** | **-2.5553** | 0.8580 | ±1.7160 | **-2.978** | **0.0029** | ** |
| **Age (years)** | **-0.1388** | 0.0359 | ±0.0717 | **-3.868** | **1.10e-04** | *** |
| **BMI (kg/m2)** | **+0.2623** | 0.0738 | ±0.1476 | **+3.555** | **3.78e-04** | *** |
| **Hypertension** | **+2.1136** | 0.8011 | ±1.6022 | **+2.638** | **0.0083** | ** |
| High cholesterol | -0.4108 | 0.7541 | ±1.5083 | -0.545 | 0.5860 |  |
| Kidney disease | -0.5605 | 2.0231 | ±4.0462 | -0.277 | 0.7818 |  |
| Circulatory disease | -1.6926 | 0.9013 | ±1.8027 | -1.878 | 0.0604 | . |
| MAG (mg/dL/h) | +0.1170 | 0.0614 | ±0.1228 | +1.905 | 0.0568 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1804**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7273** | 4.8079 | ±9.6157 | **+13.255** | **4.23e-40** | *** |
| **Education: graduate level (vs college)** | **-1.9723** | 0.7659 | ±1.5317 | **-2.575** | **0.0100** | * |
| **Education: high school or below (vs college)** | **-2.8018** | 1.2844 | ±2.5687 | **-2.181** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9504** | 0.9541 | ±1.9083 | **-2.044** | **0.0409** | * |
| **Site: UW (vs UAB)** | **-2.7213** | 0.8584 | ±1.7168 | **-3.170** | **0.0015** | ** |
| **Age (years)** | **-0.1448** | 0.0362 | ±0.0724 | **-3.997** | **6.41e-05** | *** |
| **BMI (kg/m2)** | **+0.2581** | 0.0767 | ±0.1534 | **+3.365** | **7.65e-04** | *** |
| **Hypertension** | **+2.0589** | 0.8121 | ±1.6242 | **+2.535** | **0.0112** | * |
| High cholesterol | -0.3648 | 0.7619 | ±1.5239 | -0.479 | 0.6321 |  |
| Kidney disease | -0.3320 | 2.0647 | ±4.1293 | -0.161 | 0.8723 |  |
| Circulatory disease | -1.7180 | 0.9113 | ±1.8226 | -1.885 | 0.0594 | . |
| Avg. daily range (mg/dL) | +0.0025 | 0.0318 | ±0.0636 | +0.080 | 0.9364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **403**, R² = **0.2075**, Adj R² = **0.1853**, F-statistic = **9.31** (p = **6.82e-15**), Residual SE = **6.948** on **391** df, AIC = **2717.8**, BIC = **2765.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5688** | 3.8786 | ±7.7573 | **+16.132** | **1.53e-58** | *** |
| **Education: graduate level (vs college)** | **-2.0121** | 0.7622 | ±1.5245 | **-2.640** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **-2.8976** | 1.3003 | ±2.6006 | **-2.228** | **0.0259** | * |
| **Site: UCSD (vs UAB)** | **-1.8912** | 0.9464 | ±1.8929 | **-1.998** | **0.0457** | * |
| **Site: UW (vs UAB)** | **-2.7414** | 0.8479 | ±1.6958 | **-3.233** | **0.0012** | ** |
| **Age (years)** | **-0.1446** | 0.0358 | ±0.0716 | **-4.042** | **5.30e-05** | *** |
| **BMI (kg/m2)** | **+0.2569** | 0.0756 | ±0.1513 | **+3.397** | **6.81e-04** | *** |
| **Hypertension** | **+1.9538** | 0.8140 | ±1.6280 | **+2.400** | **0.0164** | * |
| High cholesterol | -0.3875 | 0.7543 | ±1.5086 | -0.514 | 0.6074 |  |
| Kidney disease | -0.3357 | 2.0036 | ±4.0072 | -0.168 | 0.8669 |  |
| **Circulatory disease** | **-1.8194** | 0.9253 | ±1.8505 | **-1.966** | **0.0493** | * |
| SD of daily means (mg/dL) | +0.2828 | 0.1934 | ±0.3868 | +1.462 | 0.1437 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **403**, R² = **0.2032**, Adj R² = **0.1808**, F-statistic = **9.07** (p = **1.80e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.0**, BIC = **2768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +119.5255 | 119.1548 | ±238.3096 | +1.003 | 0.3158 |  |
| **Education: graduate level (vs college)** | **-1.9576** | 0.7718 | ±1.5436 | **-2.536** | **0.0112** | * |
| **Education: high school or below (vs college)** | **-2.7830** | 1.2792 | ±2.5584 | **-2.176** | **0.0296** | * |
| **Site: UCSD (vs UAB)** | **-1.9288** | 0.9583 | ±1.9166 | **-2.013** | **0.0441** | * |
| **Site: UW (vs UAB)** | **-2.7117** | 0.8570 | ±1.7141 | **-3.164** | **0.0016** | ** |
| **Age (years)** | **-0.1442** | 0.0363 | ±0.0726 | **-3.974** | **7.05e-05** | *** |
| **BMI (kg/m2)** | **+0.2583** | 0.0780 | ±0.1560 | **+3.311** | **9.29e-04** | *** |
| **Hypertension** | **+2.0494** | 0.8069 | ±1.6139 | **+2.540** | **0.0111** | * |
| High cholesterol | -0.3694 | 0.7576 | ±1.5152 | -0.488 | 0.6258 |  |
| Kidney disease | -0.3740 | 2.0566 | ±4.1131 | -0.182 | 0.8557 |  |
| Circulatory disease | -1.7148 | 0.9101 | ±1.8201 | -1.884 | 0.0595 | . |
| Time in range 70-180, pooled (%) | -0.5590 | 1.2020 | ±2.4041 | -0.465 | 0.6419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **403**, R² = **0.2034**, Adj R² = **0.1810**, F-statistic = **9.08** (p = **1.73e-14**), Residual SE = **6.966** on **391** df, AIC = **2719.9**, BIC = **2767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +125.9651 | 107.3670 | ±214.7339 | +1.173 | 0.2407 |  |
| **Education: graduate level (vs college)** | **-1.9494** | 0.7650 | ±1.5301 | **-2.548** | **0.0108** | * |
| **Education: high school or below (vs college)** | **-2.7742** | 1.2752 | ±2.5504 | **-2.176** | **0.0296** | * |
| **Site: UCSD (vs UAB)** | **-1.9352** | 0.9486 | ±1.8972 | **-2.040** | **0.0413** | * |
| **Site: UW (vs UAB)** | **-2.7272** | 0.8548 | ±1.7096 | **-3.190** | **0.0014** | ** |
| **Age (years)** | **-0.1441** | 0.0361 | ±0.0722 | **-3.992** | **6.55e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0763 | ±0.1527 | **+3.379** | **7.28e-04** | *** |
| **Hypertension** | **+2.0746** | 0.8096 | ±1.6192 | **+2.562** | **0.0104** | * |
| High cholesterol | -0.3786 | 0.7545 | ±1.5091 | -0.502 | 0.6159 |  |
| Kidney disease | -0.3583 | 2.0352 | ±4.0703 | -0.176 | 0.8603 |  |
| Circulatory disease | -1.7317 | 0.9066 | ±1.8133 | -1.910 | 0.0561 | . |
| Avg. daily time in range 70-180 (%) | -0.6233 | 1.0769 | ±2.1539 | -0.579 | 0.5628 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.2041**, Adj R² = **0.1817**, F-statistic = **9.12** (p = **1.47e-14**), Residual SE = **6.963** on **391** df, AIC = **2719.6**, BIC = **2767.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7110** | 3.8556 | ±7.7112 | **+16.524** | **2.45e-61** | *** |
| **Education: graduate level (vs college)** | **-1.9691** | 0.7640 | ±1.5280 | **-2.577** | **0.0100** | ** |
| **Education: high school or below (vs college)** | **-2.7647** | 1.2874 | ±2.5749 | **-2.147** | **0.0318** | * |
| Site: UCSD (vs UAB) | -1.8429 | 0.9593 | ±1.9186 | -1.921 | 0.0547 | . |
| **Site: UW (vs UAB)** | **-2.6675** | 0.8632 | ±1.7265 | **-3.090** | **0.0020** | ** |
| **Age (years)** | **-0.1441** | 0.0360 | ±0.0720 | **-4.002** | **6.28e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0757 | ±0.1514 | **+3.405** | **6.61e-04** | *** |
| **Hypertension** | **+2.0193** | 0.8074 | ±1.6148 | **+2.501** | **0.0124** | * |
| High cholesterol | -0.3594 | 0.7583 | ±1.5167 | -0.474 | 0.6356 |  |
| Kidney disease | -0.2406 | 2.0287 | ±4.0574 | -0.119 | 0.9056 |  |
| Circulatory disease | -1.7503 | 0.9113 | ±1.8227 | -1.921 | 0.0548 | . |
| Any reading < 54 during wear (0/1) | +0.7574 | 0.8861 | ±1.7722 | +0.855 | 0.3927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.2110**, Adj R² = **0.1888**, F-statistic = **9.50** (p = **3.15e-15**), Residual SE = **6.933** on **391** df, AIC = **2716.1**, BIC = **2764.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.5314** | 3.7673 | ±7.5346 | **+16.864** | **8.29e-64** | *** |
| **Education: graduate level (vs college)** | **-1.9659** | 0.7587 | ±1.5175 | **-2.591** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.6174** | 1.2865 | ±2.5731 | **-2.034** | **0.0419** | * |
| Site: UCSD (vs UAB) | -1.7383 | 0.9523 | ±1.9047 | -1.825 | 0.0680 | . |
| **Site: UW (vs UAB)** | **-2.6311** | 0.8505 | ±1.7011 | **-3.093** | **0.0020** | ** |
| **Age (years)** | **-0.1396** | 0.0357 | ±0.0714 | **-3.913** | **9.12e-05** | *** |
| **BMI (kg/m2)** | **+0.2501** | 0.0741 | ±0.1482 | **+3.375** | **7.38e-04** | *** |
| **Hypertension** | **+1.9074** | 0.8084 | ±1.6168 | **+2.360** | **0.0183** | * |
| High cholesterol | -0.3095 | 0.7560 | ±1.5120 | -0.409 | 0.6822 |  |
| Kidney disease | -0.1759 | 2.0255 | ±4.0509 | -0.087 | 0.9308 |  |
| **Circulatory disease** | **-1.8396** | 0.9132 | ±1.8263 | **-2.015** | **0.0439** | * |
| **Time < 54 (%)** | **+12.7485** | 4.9881 | ±9.9763 | **+2.556** | **0.0106** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.2035**, Adj R² = **0.1811**, F-statistic = **9.08** (p = **1.71e-14**), Residual SE = **6.965** on **391** df, AIC = **2719.9**, BIC = **2767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8948** | 3.8558 | ±7.7116 | **+16.571** | **1.13e-61** | *** |
| **Education: graduate level (vs college)** | **-1.9769** | 0.7646 | ±1.5293 | **-2.585** | **0.0097** | ** |
| **Education: high school or below (vs college)** | **-2.7806** | 1.2799 | ±2.5598 | **-2.173** | **0.0298** | * |
| **Site: UCSD (vs UAB)** | **-1.9279** | 0.9516 | ±1.9033 | **-2.026** | **0.0428** | * |
| **Site: UW (vs UAB)** | **-2.7272** | 0.8557 | ±1.7114 | **-3.187** | **0.0014** | ** |
| **Age (years)** | **-0.1443** | 0.0361 | ±0.0721 | **-4.001** | **6.31e-05** | *** |
| **BMI (kg/m2)** | **+0.2567** | 0.0758 | ±0.1517 | **+3.384** | **7.14e-04** | *** |
| **Hypertension** | **+2.0469** | 0.8084 | ±1.6168 | **+2.532** | **0.0113** | * |
| High cholesterol | -0.3622 | 0.7590 | ±1.5181 | -0.477 | 0.6332 |  |
| Kidney disease | -0.2927 | 2.0233 | ±4.0467 | -0.145 | 0.8850 |  |
| Circulatory disease | -1.7756 | 0.9190 | ±1.8380 | -1.932 | 0.0534 | . |
| Avg. daily time < 54 (%) | +4.8921 | 8.0373 | ±16.0745 | +0.609 | 0.5427 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9269** | 3.8473 | ±7.6946 | **+16.616** | **5.34e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9747** | 0.7676 | ±1.5352 | **-2.573** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.8056** | 1.2868 | ±2.5736 | **-2.180** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9512** | 0.9499 | ±1.8999 | **-2.054** | **0.0400** | * |
| **Site: UW (vs UAB)** | **-2.7230** | 0.8587 | ±1.7174 | **-3.171** | **0.0015** | ** |
| **Age (years)** | **-0.1447** | 0.0361 | ±0.0723 | **-4.006** | **6.17e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0761 | ±0.1521 | **+3.389** | **7.00e-04** | *** |
| **Hypertension** | **+2.0594** | 0.8125 | ±1.6251 | **+2.535** | **0.0113** | * |
| High cholesterol | -0.3690 | 0.7630 | ±1.5261 | -0.484 | 0.6286 |  |
| Kidney disease | -0.3201 | 2.0263 | ±4.0526 | -0.158 | 0.8745 |  |
| Circulatory disease | -1.7159 | 0.9143 | ±1.8285 | -1.877 | 0.0605 | . |
| Time 54-69, pooled (%) | +0.0763 | 1.8066 | ±3.6132 | +0.042 | 0.9663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **403**, R² = **0.2031**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.87e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0404** | 3.8583 | ±7.7167 | **+16.598** | **7.22e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9915** | 0.7661 | ±1.5322 | **-2.600** | **0.0093** | ** |
| **Education: high school or below (vs college)** | **-2.7746** | 1.2936 | ±2.5871 | **-2.145** | **0.0320** | * |
| **Site: UCSD (vs UAB)** | **-1.9642** | 0.9495 | ±1.8989 | **-2.069** | **0.0386** | * |
| **Site: UW (vs UAB)** | **-2.7336** | 0.8560 | ±1.7121 | **-3.193** | **0.0014** | ** |
| **Age (years)** | **-0.1446** | 0.0362 | ±0.0725 | **-3.990** | **6.62e-05** | *** |
| **BMI (kg/m2)** | **+0.2577** | 0.0763 | ±0.1526 | **+3.379** | **7.29e-04** | *** |
| **Hypertension** | **+2.0130** | 0.8153 | ±1.6307 | **+2.469** | **0.0136** | * |
| High cholesterol | -0.3432 | 0.7629 | ±1.5258 | -0.450 | 0.6528 |  |
| Kidney disease | -0.3381 | 2.0350 | ±4.0700 | -0.166 | 0.8680 |  |
| Circulatory disease | -1.7059 | 0.9100 | ±1.8201 | -1.875 | 0.0609 | . |
| Avg. daily time 54-69 (%) | -0.7573 | 1.7484 | ±3.4968 | -0.433 | 0.6649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **403**, R² = **0.2034**, Adj R² = **0.1810**, F-statistic = **9.08** (p = **1.72e-14**), Residual SE = **6.966** on **391** df, AIC = **2719.9**, BIC = **2767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7355** | 3.8239 | ±7.6478 | **+16.668** | **2.25e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9630** | 0.7669 | ±1.5337 | **-2.560** | **0.0105** | * |
| **Education: high school or below (vs college)** | **-2.8273** | 1.2818 | ±2.5636 | **-2.206** | **0.0274** | * |
| **Site: UCSD (vs UAB)** | **-1.9117** | 0.9489 | ±1.8978 | **-2.015** | **0.0439** | * |
| **Site: UW (vs UAB)** | **-2.6904** | 0.8574 | ±1.7148 | **-3.138** | **0.0017** | ** |
| **Age (years)** | **-0.1442** | 0.0359 | ±0.0719 | **-4.011** | **6.04e-05** | *** |
| **BMI (kg/m2)** | **+0.2575** | 0.0757 | ±0.1514 | **+3.401** | **6.72e-04** | *** |
| **Hypertension** | **+2.0759** | 0.8089 | ±1.6178 | **+2.566** | **0.0103** | * |
| High cholesterol | -0.3963 | 0.7607 | ±1.5214 | -0.521 | 0.6024 |  |
| Kidney disease | -0.2849 | 2.0208 | ±4.0416 | -0.141 | 0.8879 |  |
| Circulatory disease | -1.7174 | 0.9118 | ±1.8235 | -1.884 | 0.0596 | . |
| Time < 70 (%) | +0.9646 | 1.5908 | ±3.1815 | +0.606 | 0.5443 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **403**, R² = **0.2029**, Adj R² = **0.1804**, F-statistic = **9.05** (p = **1.95e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9968** | 3.8559 | ±7.7117 | **+16.597** | **7.30e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9839** | 0.7658 | ±1.5315 | **-2.591** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.7897** | 1.2908 | ±2.5816 | **-2.161** | **0.0307** | * |
| **Site: UCSD (vs UAB)** | **-1.9610** | 0.9488 | ±1.8976 | **-2.067** | **0.0387** | * |
| **Site: UW (vs UAB)** | **-2.7295** | 0.8562 | ±1.7124 | **-3.188** | **0.0014** | ** |
| **Age (years)** | **-0.1447** | 0.0362 | ±0.0724 | **-3.996** | **6.44e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0763 | ±0.1526 | **+3.380** | **7.24e-04** | *** |
| **Hypertension** | **+2.0347** | 0.8143 | ±1.6285 | **+2.499** | **0.0125** | * |
| High cholesterol | -0.3545 | 0.7615 | ±1.5231 | -0.466 | 0.6416 |  |
| Kidney disease | -0.3330 | 2.0315 | ±4.0630 | -0.164 | 0.8698 |  |
| Circulatory disease | -1.7062 | 0.9086 | ±1.8173 | -1.878 | 0.0604 | . |
| Avg. daily time < 70 (%) | -0.3972 | 1.5732 | ±3.1463 | -0.252 | 0.8007 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.2100**, Adj R² = **0.1878**, F-statistic = **9.45** (p = **3.89e-15**), Residual SE = **6.937** on **391** df, AIC = **2716.6**, BIC = **2764.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1235.7093** | 488.5746 | ±977.1491 | **+2.529** | **0.0114** | * |
| **Education: graduate level (vs college)** | **-1.9664** | 0.7600 | ±1.5200 | **-2.587** | **0.0097** | ** |
| **Education: high school or below (vs college)** | **-2.6250** | 1.2865 | ±2.5729 | **-2.040** | **0.0413** | * |
| Site: UCSD (vs UAB) | -1.7401 | 0.9536 | ±1.9072 | -1.825 | 0.0680 | . |
| **Site: UW (vs UAB)** | **-2.6262** | 0.8521 | ±1.7043 | **-3.082** | **0.0021** | ** |
| **Age (years)** | **-0.1392** | 0.0358 | ±0.0715 | **-3.893** | **9.89e-05** | *** |
| **BMI (kg/m2)** | **+0.2515** | 0.0745 | ±0.1489 | **+3.377** | **7.32e-04** | *** |
| **Hypertension** | **+1.9272** | 0.8084 | ±1.6169 | **+2.384** | **0.0171** | * |
| High cholesterol | -0.3179 | 0.7579 | ±1.5159 | -0.419 | 0.6749 |  |
| Kidney disease | -0.1897 | 2.0263 | ±4.0526 | -0.094 | 0.9254 |  |
| **Circulatory disease** | **-1.8304** | 0.9133 | ±1.8266 | **-2.004** | **0.0451** | * |
| **Time 54-250, pooled (%)** | **-11.7224** | 4.8841 | ±9.7681 | **-2.400** | **0.0164** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.2032**, Adj R² = **0.1808**, F-statistic = **9.07** (p = **1.80e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.0**, BIC = **2768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +448.1619 | 823.8648 | ±1647.7296 | +0.544 | 0.5865 |  |
| **Education: graduate level (vs college)** | **-1.9765** | 0.7653 | ±1.5307 | **-2.583** | **0.0098** | ** |
| **Education: high school or below (vs college)** | **-2.7827** | 1.2806 | ±2.5611 | **-2.173** | **0.0298** | * |
| **Site: UCSD (vs UAB)** | **-1.9278** | 0.9522 | ±1.9045 | **-2.024** | **0.0429** | * |
| **Site: UW (vs UAB)** | **-2.7223** | 0.8562 | ±1.7124 | **-3.179** | **0.0015** | ** |
| **Age (years)** | **-0.1441** | 0.0361 | ±0.0722 | **-3.995** | **6.47e-05** | *** |
| **BMI (kg/m2)** | **+0.2572** | 0.0760 | ±0.1520 | **+3.385** | **7.11e-04** | *** |
| **Hypertension** | **+2.0519** | 0.8088 | ±1.6176 | **+2.537** | **0.0112** | * |
| High cholesterol | -0.3645 | 0.7597 | ±1.5194 | -0.480 | 0.6313 |  |
| Kidney disease | -0.2998 | 2.0234 | ±4.0467 | -0.148 | 0.8822 |  |
| Circulatory disease | -1.7632 | 0.9201 | ±1.8401 | -1.916 | 0.0553 | . |
| Avg. daily time 54-250 (%) | -3.8429 | 8.2378 | ±16.4756 | -0.466 | 0.6409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1804**, F-statistic = **9.04** (p = **1.98e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8937** | 4.0447 | ±8.0893 | **+15.797** | **3.26e-56** | *** |
| **Education: graduate level (vs college)** | **-1.9731** | 0.7675 | ±1.5350 | **-2.571** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.7944** | 1.2905 | ±2.5811 | **-2.165** | **0.0304** | * |
| **Site: UCSD (vs UAB)** | **-1.9533** | 0.9540 | ±1.9079 | **-2.048** | **0.0406** | * |
| **Site: UW (vs UAB)** | **-2.7270** | 0.8567 | ±1.7134 | **-3.183** | **0.0015** | ** |
| **Age (years)** | **-0.1447** | 0.0363 | ±0.0727 | **-3.982** | **6.84e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0778 | ±0.1557 | **+3.314** | **9.19e-04** | *** |
| **Hypertension** | **+2.0525** | 0.8101 | ±1.6201 | **+2.534** | **0.0113** | * |
| High cholesterol | -0.3628 | 0.7680 | ±1.5360 | -0.472 | 0.6366 |  |
| Kidney disease | -0.3400 | 2.0877 | ±4.1755 | -0.163 | 0.8706 |  |
| Circulatory disease | -1.7160 | 0.9128 | ±1.8255 | -1.880 | 0.0601 | . |
| Time 181-250, pooled (%) | +0.1355 | 1.3650 | ±2.7299 | +0.099 | 0.9209 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **403**, R² = **0.2040**, Adj R² = **0.1816**, F-statistic = **9.11** (p = **1.51e-14**), Residual SE = **6.963** on **391** df, AIC = **2719.6**, BIC = **2767.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.6162** | 3.9353 | ±7.8706 | **+16.165** | **8.83e-59** | *** |
| **Education: graduate level (vs college)** | **-1.9551** | 0.7646 | ±1.5291 | **-2.557** | **0.0106** | * |
| **Education: high school or below (vs college)** | **-2.7283** | 1.2783 | ±2.5565 | **-2.134** | **0.0328** | * |
| **Site: UCSD (vs UAB)** | **-1.9458** | 0.9514 | ±1.9027 | **-2.045** | **0.0408** | * |
| **Site: UW (vs UAB)** | **-2.7397** | 0.8558 | ±1.7117 | **-3.201** | **0.0014** | ** |
| **Age (years)** | **-0.1437** | 0.0362 | ±0.0725 | **-3.967** | **7.29e-05** | *** |
| **BMI (kg/m2)** | **+0.2581** | 0.0768 | ±0.1536 | **+3.361** | **7.76e-04** | *** |
| **Hypertension** | **+2.0294** | 0.8075 | ±1.6149 | **+2.513** | **0.0120** | * |
| High cholesterol | -0.3562 | 0.7615 | ±1.5231 | -0.468 | 0.6399 |  |
| Kidney disease | -0.4038 | 2.0612 | ±4.1224 | -0.196 | 0.8447 |  |
| Circulatory disease | -1.7146 | 0.9076 | ±1.8152 | -1.889 | 0.0589 | . |
| Avg. daily time 181-250 (%) | +0.9622 | 1.2802 | ±2.5603 | +0.752 | 0.4523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1804**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8991** | 4.0466 | ±8.0933 | **+15.791** | **3.61e-56** | *** |
| **Education: graduate level (vs college)** | **-1.9734** | 0.7674 | ±1.5349 | **-2.571** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.7954** | 1.2908 | ±2.5816 | **-2.166** | **0.0303** | * |
| **Site: UCSD (vs UAB)** | **-1.9531** | 0.9541 | ±1.9083 | **-2.047** | **0.0407** | * |
| **Site: UW (vs UAB)** | **-2.7266** | 0.8567 | ±1.7133 | **-3.183** | **0.0015** | ** |
| **Age (years)** | **-0.1447** | 0.0364 | ±0.0727 | **-3.981** | **6.86e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0778 | ±0.1556 | **+3.314** | **9.19e-04** | *** |
| **Hypertension** | **+2.0531** | 0.8101 | ±1.6202 | **+2.534** | **0.0113** | * |
| High cholesterol | -0.3633 | 0.7680 | ±1.5359 | -0.473 | 0.6361 |  |
| Kidney disease | -0.3376 | 2.0875 | ±4.1750 | -0.162 | 0.8715 |  |
| Circulatory disease | -1.7161 | 0.9129 | ±1.8257 | -1.880 | 0.0601 | . |
| Time > 180 (%) | +0.1172 | 1.3645 | ±2.7290 | +0.086 | 0.9315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **403**, R² = **0.2039**, Adj R² = **0.1816**, F-statistic = **9.11** (p = **1.53e-14**), Residual SE = **6.963** on **391** df, AIC = **2719.7**, BIC = **2767.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.6164** | 3.9378 | ±7.8756 | **+16.155** | **1.04e-58** | *** |
| **Education: graduate level (vs college)** | **-1.9556** | 0.7646 | ±1.5292 | **-2.558** | **0.0105** | * |
| **Education: high school or below (vs college)** | **-2.7295** | 1.2786 | ±2.5572 | **-2.135** | **0.0328** | * |
| **Site: UCSD (vs UAB)** | **-1.9447** | 0.9513 | ±1.9026 | **-2.044** | **0.0409** | * |
| **Site: UW (vs UAB)** | **-2.7382** | 0.8556 | ±1.7113 | **-3.200** | **0.0014** | ** |
| **Age (years)** | **-0.1437** | 0.0362 | ±0.0725 | **-3.964** | **7.37e-05** | *** |
| **BMI (kg/m2)** | **+0.2581** | 0.0768 | ±0.1536 | **+3.361** | **7.76e-04** | *** |
| **Hypertension** | **+2.0308** | 0.8076 | ±1.6151 | **+2.515** | **0.0119** | * |
| High cholesterol | -0.3568 | 0.7616 | ±1.5232 | -0.469 | 0.6394 |  |
| Kidney disease | -0.4019 | 2.0610 | ±4.1220 | -0.195 | 0.8454 |  |
| Circulatory disease | -1.7147 | 0.9078 | ±1.8155 | -1.889 | 0.0589 | . |
| Avg. daily time > 180 (%) | +0.9379 | 1.2791 | ±2.5582 | +0.733 | 0.4634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **403**, R² = **0.2099**, Adj R² = **0.1876**, F-statistic = **9.44** (p = **4.05e-15**), Residual SE = **6.938** on **391** df, AIC = **2716.7**, BIC = **2764.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3503** | 3.7715 | ±7.5429 | **+16.797** | **2.55e-63** | *** |
| **Education: graduate level (vs college)** | **-1.8798** | 0.7559 | ±1.5118 | **-2.487** | **0.0129** | * |
| **Education: high school or below (vs college)** | **-2.7856** | 1.2628 | ±2.5256 | **-2.206** | **0.0274** | * |
| **Site: UCSD (vs UAB)** | **-2.0097** | 0.9432 | ±1.8864 | **-2.131** | **0.0331** | * |
| **Site: UW (vs UAB)** | **-2.8081** | 0.8584 | ±1.7168 | **-3.271** | **0.0011** | ** |
| **Age (years)** | **-0.1342** | 0.0354 | ±0.0709 | **-3.787** | **1.53e-04** | *** |
| **BMI (kg/m2)** | **+0.2514** | 0.0750 | ±0.1499 | **+3.354** | **7.96e-04** | *** |
| **Hypertension** | **+1.9145** | 0.8018 | ±1.6037 | **+2.388** | **0.0170** | * |
| High cholesterol | -0.4137 | 0.7583 | ±1.5165 | -0.546 | 0.5854 |  |
| Kidney disease | -0.4227 | 1.9953 | ±3.9907 | -0.212 | 0.8322 |  |
| Circulatory disease | -1.6205 | 0.9101 | ±1.8202 | -1.781 | 0.0750 | . |
| Nocturnal time > 180 (%) | +1.7799 | 1.0782 | ±2.1563 | +1.651 | 0.0988 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 409; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **409**, R² = **0.0820**, Adj R² = **0.0590**, F-statistic = **3.56** (p = **1.58e-04**), Residual SE = **64.885** on **398** df, AIC = **4584.7**, BIC = **4628.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.9589** | 26.5970 | ±53.1940 | **+15.075** | **2.35e-51** | *** |
| Education: graduate level (vs college) | +7.2130 | 6.6967 | ±13.3934 | +1.077 | 0.2814 |  |
| Education: high school or below (vs college) | -3.1173 | 14.6166 | ±29.2333 | -0.213 | 0.8311 |  |
| Site: UCSD (vs UAB) | -10.9041 | 8.4979 | ±16.9959 | -1.283 | 0.1994 |  |
| Site: UW (vs UAB) | -5.9147 | 7.9186 | ±15.8371 | -0.747 | 0.4551 |  |
| Age (years) | +0.2558 | 0.3261 | ±0.6522 | +0.784 | 0.4328 |  |
| **BMI (kg/m2)** | **-1.1942** | 0.4800 | ±0.9599 | **-2.488** | **0.0128** | * |
| **Hypertension** | **-23.6810** | 7.3750 | ±14.7501 | **-3.211** | **0.0013** | ** |
| High cholesterol | -0.4049 | 6.7928 | ±13.5855 | -0.060 | 0.9525 |  |
| **Kidney disease** | **-36.9225** | 18.7213 | ±37.4427 | **-1.972** | **0.0486** | * |
| Circulatory disease | +10.6704 | 12.0313 | ±24.0627 | +0.887 | 0.3751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **409**, R² = **0.1036**, Adj R² = **0.0787**, F-statistic = **4.17** (p = **7.57e-06**), Residual SE = **64.199** on **397** df, AIC = **4577.0**, BIC = **4625.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+575.5814** | 58.9663 | ±117.9325 | **+9.761** | **1.65e-22** | *** |
| Education: graduate level (vs college) | +5.8111 | 6.6544 | ±13.3088 | +0.873 | 0.3825 |  |
| Education: high school or below (vs college) | -1.3205 | 14.4665 | ±28.9330 | -0.091 | 0.9273 |  |
| Site: UCSD (vs UAB) | -12.2613 | 8.4295 | ±16.8589 | -1.455 | 0.1458 |  |
| Site: UW (vs UAB) | -7.5798 | 7.8358 | ±15.6715 | -0.967 | 0.3334 |  |
| Age (years) | +0.3488 | 0.3243 | ±0.6485 | +1.076 | 0.2821 |  |
| **BMI (kg/m2)** | **-1.0583** | 0.4461 | ±0.8922 | **-2.372** | **0.0177** | * |
| **Hypertension** | **-21.5882** | 7.3824 | ±14.7647 | **-2.924** | **0.0035** | ** |
| High cholesterol | +4.5570 | 6.8286 | ±13.6572 | +0.667 | 0.5046 |  |
| **Kidney disease** | **-38.9595** | 17.8352 | ±35.6704 | **-2.184** | **0.0289** | * |
| Circulatory disease | +9.2986 | 11.5178 | ±23.0356 | +0.807 | 0.4195 |  |
| **HbA1c (%)** | **-33.4365** | 10.3429 | ±20.6858 | **-3.233** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **409**, R² = **0.0917**, Adj R² = **0.0665**, F-statistic = **3.64** (p = **6.15e-05**), Residual SE = **64.623** on **397** df, AIC = **4582.4**, BIC = **4630.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+502.3269** | 53.6770 | ±107.3540 | **+9.358** | **8.10e-21** | *** |
| Education: graduate level (vs college) | +6.9460 | 6.6742 | ±13.3484 | +1.041 | 0.2980 |  |
| Education: high school or below (vs college) | -4.5567 | 14.8940 | ±29.7881 | -0.306 | 0.7597 |  |
| Site: UCSD (vs UAB) | -10.2376 | 8.4206 | ±16.8412 | -1.216 | 0.2241 |  |
| Site: UW (vs UAB) | -5.0624 | 7.8910 | ±15.7819 | -0.642 | 0.5212 |  |
| Age (years) | +0.2280 | 0.3218 | ±0.6436 | +0.708 | 0.4787 |  |
| **BMI (kg/m2)** | **-1.1358** | 0.4768 | ±0.9536 | **-2.382** | **0.0172** | * |
| **Hypertension** | **-22.6211** | 7.3650 | ±14.7301 | **-3.071** | **0.0021** | ** |
| High cholesterol | -0.9597 | 6.7658 | ±13.5316 | -0.142 | 0.8872 |  |
| **Kidney disease** | **-36.8159** | 18.6439 | ±37.2878 | **-1.975** | **0.0483** | * |
| Circulatory disease | +10.7409 | 11.9756 | ±23.9512 | +0.897 | 0.3698 |  |
| **Mean glucose (mg/dL)** | **-0.8919** | 0.4252 | ±0.8503 | **-2.098** | **0.0359** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **409**, R² = **0.0917**, Adj R² = **0.0665**, F-statistic = **3.64** (p = **6.15e-05**), Residual SE = **64.623** on **397** df, AIC = **4582.4**, BIC = **4630.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+625.7418** | 108.8455 | ±217.6911 | **+5.749** | **8.98e-09** | *** |
| Education: graduate level (vs college) | +6.9460 | 6.6742 | ±13.3484 | +1.041 | 0.2980 |  |
| Education: high school or below (vs college) | -4.5567 | 14.8940 | ±29.7881 | -0.306 | 0.7597 |  |
| Site: UCSD (vs UAB) | -10.2376 | 8.4206 | ±16.8412 | -1.216 | 0.2241 |  |
| Site: UW (vs UAB) | -5.0624 | 7.8910 | ±15.7819 | -0.642 | 0.5212 |  |
| Age (years) | +0.2280 | 0.3218 | ±0.6436 | +0.708 | 0.4787 |  |
| **BMI (kg/m2)** | **-1.1358** | 0.4768 | ±0.9536 | **-2.382** | **0.0172** | * |
| **Hypertension** | **-22.6211** | 7.3650 | ±14.7301 | **-3.071** | **0.0021** | ** |
| High cholesterol | -0.9597 | 6.7658 | ±13.5316 | -0.142 | 0.8872 |  |
| **Kidney disease** | **-36.8159** | 18.6439 | ±37.2878 | **-1.975** | **0.0483** | * |
| Circulatory disease | +10.7409 | 11.9756 | ±23.9512 | +0.897 | 0.3698 |  |
| **GMI (%)** | **-37.2855** | 17.7746 | ±35.5491 | **-2.098** | **0.0359** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **409**, R² = **0.0946**, Adj R² = **0.0695**, F-statistic = **3.77** (p = **3.71e-05**), Residual SE = **64.519** on **397** df, AIC = **4581.1**, BIC = **4629.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+494.5796** | 45.7576 | ±91.5153 | **+10.809** | **3.13e-27** | *** |
| Education: graduate level (vs college) | +6.4574 | 6.6974 | ±13.3948 | +0.964 | 0.3350 |  |
| Education: high school or below (vs college) | -4.6226 | 14.7669 | ±29.5337 | -0.313 | 0.7543 |  |
| Site: UCSD (vs UAB) | -9.1104 | 8.4328 | ±16.8655 | -1.080 | 0.2800 |  |
| Site: UW (vs UAB) | -4.3834 | 7.9184 | ±15.8369 | -0.554 | 0.5799 |  |
| Age (years) | +0.1363 | 0.3186 | ±0.6372 | +0.428 | 0.6689 |  |
| **BMI (kg/m2)** | **-1.0239** | 0.4574 | ±0.9149 | **-2.238** | **0.0252** | * |
| **Hypertension** | **-22.2357** | 7.3657 | ±14.7314 | **-3.019** | **0.0025** | ** |
| High cholesterol | -0.5549 | 6.7810 | ±13.5620 | -0.082 | 0.9348 |  |
| **Kidney disease** | **-38.9327** | 18.8320 | ±37.6640 | **-2.067** | **0.0387** | * |
| Circulatory disease | +9.9938 | 12.0296 | ±24.0592 | +0.831 | 0.4061 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.8042** | 0.3465 | ±0.6929 | **-2.321** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0566**, F-statistic = **3.23** (p = **3.14e-04**), Residual SE = **64.965** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0020** | 34.8858 | ±69.7717 | **+11.581** | **5.16e-31** | *** |
| Education: graduate level (vs college) | +7.1320 | 6.8646 | ±13.7292 | +1.039 | 0.2988 |  |
| Education: high school or below (vs college) | -3.1180 | 14.6374 | ±29.2749 | -0.213 | 0.8313 |  |
| Site: UCSD (vs UAB) | -10.9688 | 8.4671 | ±16.9341 | -1.295 | 0.1952 |  |
| Site: UW (vs UAB) | -5.9921 | 7.9899 | ±15.9799 | -0.750 | 0.4533 |  |
| Age (years) | +0.2566 | 0.3284 | ±0.6567 | +0.782 | 0.4345 |  |
| **BMI (kg/m2)** | **-1.1919** | 0.4803 | ±0.9606 | **-2.482** | **0.0131** | * |
| **Hypertension** | **-23.6226** | 7.3469 | ±14.6937 | **-3.215** | **0.0013** | ** |
| High cholesterol | -0.4624 | 6.8043 | ±13.6086 | -0.068 | 0.9458 |  |
| Kidney disease | -36.7146 | 18.7827 | ±37.5654 | -1.955 | 0.0506 | . |
| Circulatory disease | +10.6941 | 12.0259 | ±24.0518 | +0.889 | 0.3739 |  |
| Glucose SD, pooled (mg/dL) | -0.1834 | 1.4635 | ±2.9270 | -0.125 | 0.9003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0566**, F-statistic = **3.23** (p = **3.14e-04**), Residual SE = **64.965** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.7727** | 32.8701 | ±65.7402 | **+12.284** | **1.11e-34** | *** |
| Education: graduate level (vs college) | +7.1207 | 6.8744 | ±13.7488 | +1.036 | 0.3003 |  |
| Education: high school or below (vs college) | -3.1476 | 14.6261 | ±29.2522 | -0.215 | 0.8296 |  |
| Site: UCSD (vs UAB) | -10.9636 | 8.4738 | ±16.9475 | -1.294 | 0.1957 |  |
| Site: UW (vs UAB) | -5.9889 | 7.9627 | ±15.9255 | -0.752 | 0.4520 |  |
| Age (years) | +0.2571 | 0.3288 | ±0.6577 | +0.782 | 0.4343 |  |
| **BMI (kg/m2)** | **-1.1903** | 0.4805 | ±0.9610 | **-2.477** | **0.0132** | * |
| **Hypertension** | **-23.6502** | 7.3666 | ±14.7333 | **-3.210** | **0.0013** | ** |
| High cholesterol | -0.4525 | 6.8111 | ±13.6222 | -0.066 | 0.9470 |  |
| Kidney disease | -36.6947 | 18.8098 | ±37.6197 | -1.951 | 0.0511 | . |
| Circulatory disease | +10.6656 | 12.0530 | ±24.1060 | +0.885 | 0.3762 |  |
| Avg. daily SD (mg/dL) | -0.1891 | 1.4339 | ±2.8677 | -0.132 | 0.8951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **409**, R² = **0.0833**, Adj R² = **0.0579**, F-statistic = **3.28** (p = **2.56e-04**), Residual SE = **64.922** on **397** df, AIC = **4586.2**, BIC = **4634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+384.6354** | 34.4013 | ±68.8026 | **+11.181** | **5.06e-29** | *** |
| Education: graduate level (vs college) | +7.6092 | 6.8124 | ±13.6248 | +1.117 | 0.2640 |  |
| Education: high school or below (vs college) | -3.3340 | 14.7134 | ±29.4269 | -0.227 | 0.8207 |  |
| Site: UCSD (vs UAB) | -10.4627 | 8.4603 | ±16.9206 | -1.237 | 0.2162 |  |
| Site: UW (vs UAB) | -5.3712 | 8.0329 | ±16.0658 | -0.669 | 0.5037 |  |
| Age (years) | +0.2472 | 0.3274 | ±0.6549 | +0.755 | 0.4503 |  |
| **BMI (kg/m2)** | **-1.1967** | 0.4824 | ±0.9647 | **-2.481** | **0.0131** | * |
| **Hypertension** | **-23.8118** | 7.3813 | ±14.7626 | **-3.226** | **0.0013** | ** |
| High cholesterol | -0.1688 | 6.8070 | ±13.6139 | -0.025 | 0.9802 |  |
| **Kidney disease** | **-38.0100** | 18.8914 | ±37.7828 | **-2.012** | **0.0442** | * |
| Circulatory disease | +10.5381 | 12.1051 | ±24.2103 | +0.871 | 0.3840 |  |
| CV (%) | +1.1124 | 1.5570 | ±3.1140 | +0.714 | 0.4749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **409**, R² = **0.0833**, Adj R² = **0.0579**, F-statistic = **3.28** (p = **2.54e-04**), Residual SE = **64.920** on **397** df, AIC = **4586.2**, BIC = **4634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+417.0004** | 35.4017 | ±70.8033 | **+11.779** | **5.00e-32** | *** |
| Education: graduate level (vs college) | +7.6569 | 6.8240 | ±13.6480 | +1.122 | 0.2618 |  |
| Education: high school or below (vs college) | -3.3789 | 14.7219 | ±29.4438 | -0.230 | 0.8185 |  |
| Site: UCSD (vs UAB) | -10.5004 | 8.4529 | ±16.9058 | -1.242 | 0.2142 |  |
| Site: UW (vs UAB) | -5.4146 | 8.0157 | ±16.0313 | -0.676 | 0.4994 |  |
| Age (years) | +0.2483 | 0.3272 | ±0.6544 | +0.759 | 0.4479 |  |
| **BMI (kg/m2)** | **-1.1963** | 0.4817 | ±0.9633 | **-2.484** | **0.0130** | * |
| **Hypertension** | **-23.8214** | 7.3795 | ±14.7590 | **-3.228** | **0.0012** | ** |
| High cholesterol | -0.1407 | 6.8153 | ±13.6306 | -0.021 | 0.9835 |  |
| **Kidney disease** | **-37.7068** | 18.8152 | ±37.6304 | **-2.004** | **0.0451** | * |
| Circulatory disease | +10.6262 | 12.1140 | ±24.2280 | +0.877 | 0.3804 |  |
| Mean / SD ratio | -2.3162 | 3.1876 | ±6.3752 | -0.727 | 0.4675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **409**, R² = **0.0823**, Adj R² = **0.0569**, F-statistic = **3.24** (p = **3.03e-04**), Residual SE = **64.957** on **397** df, AIC = **4586.6**, BIC = **4634.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.4599** | 34.0927 | ±68.1854 | **+11.952** | **6.37e-33** | *** |
| Education: graduate level (vs college) | +7.4248 | 6.8254 | ±13.6509 | +1.088 | 0.2767 |  |
| Education: high school or below (vs college) | -3.1826 | 14.6892 | ±29.3785 | -0.217 | 0.8285 |  |
| Site: UCSD (vs UAB) | -10.7505 | 8.4752 | ±16.9504 | -1.268 | 0.2046 |  |
| Site: UW (vs UAB) | -5.7050 | 7.9958 | ±15.9916 | -0.714 | 0.4755 |  |
| Age (years) | +0.2512 | 0.3286 | ±0.6572 | +0.765 | 0.4445 |  |
| **BMI (kg/m2)** | **-1.1996** | 0.4823 | ±0.9646 | **-2.487** | **0.0129** | * |
| **Hypertension** | **-23.6823** | 7.3932 | ±14.7865 | **-3.203** | **0.0014** | ** |
| High cholesterol | -0.3416 | 6.8145 | ±13.6289 | -0.050 | 0.9600 |  |
| **Kidney disease** | **-37.3377** | 18.7542 | ±37.5084 | **-1.991** | **0.0465** | * |
| Circulatory disease | +10.7557 | 12.1018 | ±24.2037 | +0.889 | 0.3741 |  |
| Avg. daily mean/SD | -0.8044 | 2.4194 | ±4.8388 | -0.332 | 0.7395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **409**, R² = **0.0947**, Adj R² = **0.0697**, F-statistic = **3.78** (p = **3.64e-05**), Residual SE = **64.515** on **397** df, AIC = **4581.0**, BIC = **4629.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+450.8336** | 34.0157 | ±68.0314 | **+13.254** | **4.30e-40** | *** |
| Education: graduate level (vs college) | +7.1015 | 6.6611 | ±13.3223 | +1.066 | 0.2864 |  |
| Education: high school or below (vs college) | -0.5440 | 14.2306 | ±28.4612 | -0.038 | 0.9695 |  |
| Site: UCSD (vs UAB) | -11.6596 | 8.4376 | ±16.8753 | -1.382 | 0.1670 |  |
| Site: UW (vs UAB) | -7.8184 | 7.9167 | ±15.8334 | -0.988 | 0.3234 |  |
| Age (years) | +0.1929 | 0.3247 | ±0.6494 | +0.594 | 0.5525 |  |
| **BMI (kg/m2)** | **-1.2391** | 0.4671 | ±0.9342 | **-2.653** | **0.0080** | ** |
| **Hypertension** | **-24.3127** | 7.3947 | ±14.7894 | **-3.288** | **0.0010** | ** |
| High cholesterol | +0.3318 | 6.7390 | ±13.4780 | +0.049 | 0.9607 |  |
| Kidney disease | -34.1588 | 18.8238 | ±37.6475 | -1.815 | 0.0696 | . |
| Circulatory disease | +10.0733 | 11.9085 | ±23.8169 | +0.846 | 0.3976 |  |
| **MAG (mg/dL/h)** | **-1.2941** | 0.5594 | ±1.1187 | **-2.314** | **0.0207** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0567**, F-statistic = **3.23** (p = **3.13e-04**), Residual SE = **64.964** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.9038** | 37.6347 | ±75.2694 | **+10.546** | **5.29e-26** | *** |
| Education: graduate level (vs college) | +7.2735 | 6.8045 | ±13.6091 | +1.069 | 0.2851 |  |
| Education: high school or below (vs college) | -3.1419 | 14.6676 | ±29.3352 | -0.214 | 0.8304 |  |
| Site: UCSD (vs UAB) | -10.8297 | 8.5146 | ±17.0292 | -1.272 | 0.2034 |  |
| Site: UW (vs UAB) | -5.8211 | 8.0000 | ±16.0000 | -0.728 | 0.4668 |  |
| Age (years) | +0.2546 | 0.3281 | ±0.6561 | +0.776 | 0.4377 |  |
| **BMI (kg/m2)** | **-1.1884** | 0.4840 | ±0.9680 | **-2.455** | **0.0141** | * |
| **Hypertension** | **-23.6264** | 7.4701 | ±14.9401 | **-3.163** | **0.0016** | ** |
| High cholesterol | -0.3948 | 6.8152 | ±13.6304 | -0.058 | 0.9538 |  |
| **Kidney disease** | **-37.1259** | 18.8351 | ±37.6703 | **-1.971** | **0.0487** | * |
| Circulatory disease | +10.6703 | 12.0707 | ±24.1413 | +0.884 | 0.3767 |  |
| Avg. daily range (mg/dL) | +0.0483 | 0.3252 | ±0.6505 | +0.149 | 0.8819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **409**, R² = **0.0820**, Adj R² = **0.0566**, F-statistic = **3.22** (p = **3.16e-04**), Residual SE = **64.967** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.6042** | 27.6921 | ±55.3842 | **+14.466** | **1.98e-47** | *** |
| Education: graduate level (vs college) | +7.2081 | 6.7091 | ±13.4181 | +1.074 | 0.2827 |  |
| Education: high school or below (vs college) | -3.1461 | 14.7058 | ±29.4116 | -0.214 | 0.8306 |  |
| Site: UCSD (vs UAB) | -10.8846 | 8.4902 | ±16.9804 | -1.282 | 0.1998 |  |
| Site: UW (vs UAB) | -5.9184 | 7.9399 | ±15.8798 | -0.745 | 0.4560 |  |
| Age (years) | +0.2561 | 0.3268 | ±0.6536 | +0.784 | 0.4333 |  |
| **BMI (kg/m2)** | **-1.1945** | 0.4812 | ±0.9623 | **-2.483** | **0.0130** | * |
| **Hypertension** | **-23.7075** | 7.4115 | ±14.8229 | **-3.199** | **0.0014** | ** |
| High cholesterol | -0.4136 | 6.8336 | ±13.6673 | -0.061 | 0.9517 |  |
| **Kidney disease** | **-36.9173** | 18.7782 | ±37.5563 | **-1.966** | **0.0493** | * |
| Circulatory disease | +10.6418 | 12.0861 | ±24.1723 | +0.880 | 0.3786 |  |
| SD of daily means (mg/dL) | +0.0704 | 1.6248 | ±3.2496 | +0.043 | 0.9654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **409**, R² = **0.0829**, Adj R² = **0.0575**, F-statistic = **3.26** (p = **2.74e-04**), Residual SE = **64.936** on **397** df, AIC = **4586.4**, BIC = **4634.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1062.0916 | 1150.7598 | ±2301.5195 | +0.923 | 0.3560 |  |
| Education: graduate level (vs college) | +7.4185 | 6.7988 | ±13.5976 | +1.091 | 0.2752 |  |
| Education: high school or below (vs college) | -3.0488 | 14.6731 | ±29.3462 | -0.208 | 0.8354 |  |
| Site: UCSD (vs UAB) | -10.6574 | 8.4674 | ±16.9348 | -1.259 | 0.2082 |  |
| Site: UW (vs UAB) | -5.7381 | 7.9483 | ±15.8966 | -0.722 | 0.4703 |  |
| Age (years) | +0.2599 | 0.3252 | ±0.6503 | +0.799 | 0.4241 |  |
| **BMI (kg/m2)** | **-1.1852** | 0.4753 | ±0.9507 | **-2.494** | **0.0126** | * |
| **Hypertension** | **-23.7306** | 7.3860 | ±14.7720 | **-3.213** | **0.0013** | ** |
| High cholesterol | -0.4338 | 6.8098 | ±13.6196 | -0.064 | 0.9492 |  |
| **Kidney disease** | **-37.3901** | 18.8019 | ±37.6038 | **-1.989** | **0.0467** | * |
| Circulatory disease | +10.7962 | 12.1528 | ±24.3056 | +0.888 | 0.3743 |  |
| Time in range 70-180, pooled (%) | -6.6490 | 11.5672 | ±23.1344 | -0.575 | 0.5654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **409**, R² = **0.0833**, Adj R² = **0.0579**, F-statistic = **3.28** (p = **2.56e-04**), Residual SE = **64.921** on **397** df, AIC = **4586.2**, BIC = **4634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1176.2689 | 1087.3562 | ±2174.7123 | +1.082 | 0.2794 |  |
| Education: graduate level (vs college) | +7.5541 | 6.8262 | ±13.6525 | +1.107 | 0.2685 |  |
| Education: high school or below (vs college) | -2.9217 | 14.6717 | ±29.3434 | -0.199 | 0.8422 |  |
| Site: UCSD (vs UAB) | -10.7359 | 8.4872 | ±16.9744 | -1.265 | 0.2059 |  |
| Site: UW (vs UAB) | -5.9179 | 7.9553 | ±15.9107 | -0.744 | 0.4569 |  |
| Age (years) | +0.2627 | 0.3258 | ±0.6516 | +0.806 | 0.4202 |  |
| **BMI (kg/m2)** | **-1.1897** | 0.4796 | ±0.9591 | **-2.481** | **0.0131** | * |
| **Hypertension** | **-23.3985** | 7.4549 | ±14.9097 | **-3.139** | **0.0017** | ** |
| High cholesterol | -0.5823 | 6.7995 | ±13.5990 | -0.086 | 0.9318 |  |
| **Kidney disease** | **-37.4094** | 18.7974 | ±37.5949 | **-1.990** | **0.0466** | * |
| Circulatory disease | +10.5156 | 12.1452 | ±24.2904 | +0.866 | 0.3866 |  |
| Avg. daily time in range 70-180 (%) | -7.7917 | 10.9199 | ±21.8398 | -0.714 | 0.4755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **409**, R² = **0.0824**, Adj R² = **0.0570**, F-statistic = **3.24** (p = **2.97e-04**), Residual SE = **64.953** on **397** df, AIC = **4586.6**, BIC = **4634.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.9777** | 26.9082 | ±53.8165 | **+14.865** | **5.60e-50** | *** |
| Education: graduate level (vs college) | +7.2182 | 6.7106 | ±13.4213 | +1.076 | 0.2821 |  |
| Education: high school or below (vs college) | -2.9679 | 14.6708 | ±29.3416 | -0.202 | 0.8397 |  |
| Site: UCSD (vs UAB) | -10.3446 | 8.6834 | ±17.3667 | -1.191 | 0.2335 |  |
| Site: UW (vs UAB) | -5.6149 | 7.9897 | ±15.9795 | -0.703 | 0.4822 |  |
| Age (years) | +0.2577 | 0.3264 | ±0.6528 | +0.790 | 0.4298 |  |
| **BMI (kg/m2)** | **-1.1953** | 0.4816 | ±0.9631 | **-2.482** | **0.0131** | * |
| **Hypertension** | **-23.8356** | 7.3961 | ±14.7923 | **-3.223** | **0.0013** | ** |
| High cholesterol | -0.3847 | 6.8045 | ±13.6090 | -0.057 | 0.9549 |  |
| Kidney disease | -36.5334 | 18.8353 | ±37.6705 | -1.940 | 0.0524 | . |
| Circulatory disease | +10.5587 | 12.0622 | ±24.1243 | +0.875 | 0.3814 |  |
| Any reading < 54 during wear (0/1) | +3.4669 | 7.4397 | ±14.8795 | +0.466 | 0.6412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0567**, F-statistic = **3.23** (p = **3.11e-04**), Residual SE = **64.963** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.5646** | 26.8211 | ±53.6422 | **+14.935** | **1.96e-50** | *** |
| Education: graduate level (vs college) | +7.2141 | 6.7123 | ±13.4246 | +1.075 | 0.2825 |  |
| Education: high school or below (vs college) | -2.9474 | 14.6460 | ±29.2920 | -0.201 | 0.8405 |  |
| Site: UCSD (vs UAB) | -10.6678 | 8.6345 | ±17.2691 | -1.235 | 0.2167 |  |
| Site: UW (vs UAB) | -5.8096 | 7.9711 | ±15.9421 | -0.729 | 0.4661 |  |
| Age (years) | +0.2606 | 0.3275 | ±0.6550 | +0.796 | 0.4262 |  |
| **BMI (kg/m2)** | **-1.2022** | 0.4835 | ±0.9669 | **-2.487** | **0.0129** | * |
| **Hypertension** | **-23.8195** | 7.4057 | ±14.8115 | **-3.216** | **0.0013** | ** |
| High cholesterol | -0.3464 | 6.8039 | ±13.6078 | -0.051 | 0.9594 |  |
| Kidney disease | -36.7636 | 18.7680 | ±37.5360 | -1.959 | 0.0501 | . |
| Circulatory disease | +10.5616 | 12.0572 | ±24.1144 | +0.876 | 0.3811 |  |
| Time < 54 (%) | +12.7256 | 52.9914 | ±105.9829 | +0.240 | 0.8102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **409**, R² = **0.0836**, Adj R² = **0.0582**, F-statistic = **3.29** (p = **2.42e-04**), Residual SE = **64.909** on **397** df, AIC = **4586.0**, BIC = **4634.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.3898** | 26.7431 | ±53.4863 | **+14.972** | **1.12e-50** | *** |
| Education: graduate level (vs college) | +7.1874 | 6.7045 | ±13.4090 | +1.072 | 0.2837 |  |
| Education: high school or below (vs college) | -2.8365 | 14.6359 | ±29.2718 | -0.194 | 0.8463 |  |
| Site: UCSD (vs UAB) | -10.4951 | 8.5207 | ±17.0414 | -1.232 | 0.2181 |  |
| Site: UW (vs UAB) | -5.8945 | 7.9213 | ±15.8427 | -0.744 | 0.4568 |  |
| Age (years) | +0.2599 | 0.3262 | ±0.6524 | +0.797 | 0.4255 |  |
| **BMI (kg/m2)** | **-1.2093** | 0.4846 | ±0.9691 | **-2.496** | **0.0126** | * |
| **Hypertension** | **-23.7823** | 7.3809 | ±14.7619 | **-3.222** | **0.0013** | ** |
| High cholesterol | -0.3453 | 6.8061 | ±13.6121 | -0.051 | 0.9595 |  |
| Kidney disease | -36.5471 | 18.7888 | ±37.5775 | -1.945 | 0.0518 | . |
| Circulatory disease | +9.9452 | 12.0700 | ±24.1400 | +0.824 | 0.4100 |  |
| Avg. daily time < 54 (%) | +64.9196 | 62.5331 | ±125.0661 | +1.038 | 0.2992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **409**, R² = **0.1004**, Adj R² = **0.0754**, F-statistic = **4.03** (p = **1.35e-05**), Residual SE = **64.314** on **397** df, AIC = **4578.5**, BIC = **4626.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.9195** | 27.1176 | ±54.2352 | **+14.489** | **1.41e-47** | *** |
| Education: graduate level (vs college) | +7.9489 | 6.6737 | ±13.3473 | +1.191 | 0.2336 |  |
| Education: high school or below (vs college) | -6.1101 | 14.7562 | ±29.5125 | -0.414 | 0.6788 |  |
| Site: UCSD (vs UAB) | -10.1144 | 8.4316 | ±16.8632 | -1.200 | 0.2303 |  |
| Site: UW (vs UAB) | -4.7305 | 7.9000 | ±15.8001 | -0.599 | 0.5493 |  |
| Age (years) | +0.2550 | 0.3240 | ±0.6481 | +0.787 | 0.4313 |  |
| **BMI (kg/m2)** | **-1.1840** | 0.4865 | ±0.9729 | **-2.434** | **0.0149** | * |
| **Hypertension** | **-22.2120** | 7.3470 | ±14.6939 | **-3.023** | **0.0025** | ** |
| High cholesterol | -2.3640 | 6.6943 | ±13.3887 | -0.353 | 0.7240 |  |
| Kidney disease | -35.3093 | 19.0061 | ±38.0121 | -1.858 | 0.0632 | . |
| Circulatory disease | +11.1881 | 12.0568 | ±24.1136 | +0.928 | 0.3534 |  |
| **Time 54-69, pooled (%)** | **+50.0786** | 17.2263 | ±34.4526 | **+2.907** | **0.0036** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **409**, R² = **0.0987**, Adj R² = **0.0737**, F-statistic = **3.95** (p = **1.81e-05**), Residual SE = **64.373** on **397** df, AIC = **4579.2**, BIC = **4627.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.0703** | 26.9885 | ±53.9770 | **+14.638** | **1.60e-48** | *** |
| Education: graduate level (vs college) | +8.3527 | 6.6881 | ±13.3761 | +1.249 | 0.2117 |  |
| Education: high school or below (vs college) | -5.8212 | 14.8233 | ±29.6466 | -0.393 | 0.6945 |  |
| Site: UCSD (vs UAB) | -10.7798 | 8.4386 | ±16.8772 | -1.277 | 0.2014 |  |
| Site: UW (vs UAB) | -5.5393 | 7.8719 | ±15.7437 | -0.704 | 0.4816 |  |
| Age (years) | +0.2403 | 0.3259 | ±0.6518 | +0.737 | 0.4610 |  |
| **BMI (kg/m2)** | **-1.1932** | 0.4843 | ±0.9687 | **-2.463** | **0.0138** | * |
| **Hypertension** | **-20.9835** | 7.4710 | ±14.9420 | **-2.809** | **0.0050** | ** |
| High cholesterol | -1.9334 | 6.6986 | ±13.3971 | -0.289 | 0.7729 |  |
| Kidney disease | -35.6575 | 19.0144 | ±38.0289 | -1.875 | 0.0608 | . |
| Circulatory disease | +10.1970 | 12.0726 | ±24.1453 | +0.845 | 0.3983 |  |
| **Avg. daily time 54-69 (%)** | **+48.4532** | 17.9374 | ±35.8748 | **+2.701** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **409**, R² = **0.0970**, Adj R² = **0.0720**, F-statistic = **3.88** (p = **2.45e-05**), Residual SE = **64.434** on **397** df, AIC = **4580.0**, BIC = **4628.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.2998** | 27.2650 | ±54.5300 | **+14.425** | **3.60e-47** | *** |
| Education: graduate level (vs college) | +7.8043 | 6.6753 | ±13.3507 | +1.169 | 0.2424 |  |
| Education: high school or below (vs college) | -4.9735 | 14.7379 | ±29.4759 | -0.337 | 0.7358 |  |
| Site: UCSD (vs UAB) | -9.5311 | 8.4240 | ±16.8480 | -1.131 | 0.2579 |  |
| Site: UW (vs UAB) | -4.6389 | 7.9292 | ±15.8583 | -0.585 | 0.5585 |  |
| Age (years) | +0.2703 | 0.3248 | ±0.6495 | +0.832 | 0.4052 |  |
| **BMI (kg/m2)** | **-1.2113** | 0.4906 | ±0.9811 | **-2.469** | **0.0135** | * |
| **Hypertension** | **-22.9432** | 7.3382 | ±14.6765 | **-3.127** | **0.0018** | ** |
| High cholesterol | -1.7855 | 6.7106 | ±13.4212 | -0.266 | 0.7902 |  |
| Kidney disease | -35.1349 | 18.9855 | ±37.9711 | -1.851 | 0.0642 | . |
| Circulatory disease | +10.7417 | 12.0260 | ±24.0520 | +0.893 | 0.3717 |  |
| **Time < 70 (%)** | **+39.9914** | 14.8149 | ±29.6298 | **+2.699** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **409**, R² = **0.0979**, Adj R² = **0.0729**, F-statistic = **3.92** (p = **2.10e-05**), Residual SE = **64.403** on **397** df, AIC = **4579.6**, BIC = **4627.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.3686** | 27.0182 | ±54.0363 | **+14.633** | **1.72e-48** | *** |
| Education: graduate level (vs college) | +8.2053 | 6.6798 | ±13.3597 | +1.228 | 0.2193 |  |
| Education: high school or below (vs college) | -5.3260 | 14.8101 | ±29.6201 | -0.360 | 0.7191 |  |
| Site: UCSD (vs UAB) | -10.5238 | 8.4206 | ±16.8413 | -1.250 | 0.2114 |  |
| Site: UW (vs UAB) | -5.5690 | 7.8748 | ±15.7495 | -0.707 | 0.4794 |  |
| Age (years) | +0.2448 | 0.3257 | ±0.6514 | +0.752 | 0.4523 |  |
| **BMI (kg/m2)** | **-1.2033** | 0.4860 | ±0.9720 | **-2.476** | **0.0133** | * |
| **Hypertension** | **-21.3593** | 7.4558 | ±14.9115 | **-2.865** | **0.0042** | ** |
| High cholesterol | -1.7190 | 6.7095 | ±13.4190 | -0.256 | 0.7978 |  |
| Kidney disease | -35.5543 | 19.0155 | ±38.0310 | -1.870 | 0.0615 | . |
| Circulatory disease | +9.7720 | 12.0603 | ±24.1206 | +0.810 | 0.4178 |  |
| **Avg. daily time < 70 (%)** | **+42.9042** | 15.8537 | ±31.7075 | **+2.706** | **0.0068** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **409**, R² = **0.0820**, Adj R² = **0.0566**, F-statistic = **3.23** (p = **3.16e-04**), Residual SE = **64.966** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +754.0243 | 5140.7960 | ±10281.5920 | +0.147 | 0.8834 |  |
| Education: graduate level (vs college) | +7.2132 | 6.7135 | ±13.4270 | +1.074 | 0.2826 |  |
| Education: high school or below (vs college) | -3.0679 | 14.6414 | ±29.2829 | -0.210 | 0.8340 |  |
| Site: UCSD (vs UAB) | -10.8337 | 8.6499 | ±17.2998 | -1.252 | 0.2104 |  |
| Site: UW (vs UAB) | -5.8817 | 7.9772 | ±15.9543 | -0.737 | 0.4609 |  |
| Age (years) | +0.2573 | 0.3278 | ±0.6555 | +0.785 | 0.4324 |  |
| **BMI (kg/m2)** | **-1.1962** | 0.4818 | ±0.9636 | **-2.483** | **0.0130** | * |
| **Hypertension** | **-23.7172** | 7.4025 | ±14.8049 | **-3.204** | **0.0014** | ** |
| High cholesterol | -0.3899 | 6.8049 | ±13.6098 | -0.057 | 0.9543 |  |
| **Kidney disease** | **-36.8791** | 18.7567 | ±37.5133 | **-1.966** | **0.0493** | * |
| Circulatory disease | +10.6401 | 12.0631 | ±24.1261 | +0.882 | 0.3778 |  |
| Time 54-250, pooled (%) | -3.5320 | 51.4408 | ±102.8816 | -0.069 | 0.9453 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **409**, R² = **0.0829**, Adj R² = **0.0575**, F-statistic = **3.26** (p = **2.75e-04**), Residual SE = **64.937** on **397** df, AIC = **4586.4**, BIC = **4634.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4986.3337 | 6558.4641 | ±13116.9281 | +0.760 | 0.4471 |  |
| Education: graduate level (vs college) | +7.1935 | 6.7111 | ±13.4222 | +1.072 | 0.2838 |  |
| Education: high school or below (vs college) | -2.8865 | 14.6290 | ±29.2580 | -0.197 | 0.8436 |  |
| Site: UCSD (vs UAB) | -10.5471 | 8.5420 | ±17.0839 | -1.235 | 0.2169 |  |
| Site: UW (vs UAB) | -5.8469 | 7.9327 | ±15.8654 | -0.737 | 0.4611 |  |
| Age (years) | +0.2622 | 0.3267 | ±0.6535 | +0.802 | 0.4223 |  |
| **BMI (kg/m2)** | **-1.2013** | 0.4825 | ±0.9650 | **-2.490** | **0.0128** | * |
| **Hypertension** | **-23.7201** | 7.3844 | ±14.7687 | **-3.212** | **0.0013** | ** |
| High cholesterol | -0.3804 | 6.8082 | ±13.6165 | -0.056 | 0.9554 |  |
| Kidney disease | -36.6678 | 18.7704 | ±37.5409 | -1.953 | 0.0508 | . |
| Circulatory disease | +10.1572 | 12.0776 | ±24.1551 | +0.841 | 0.4004 |  |
| Avg. daily time 54-250 (%) | -45.8616 | 65.6045 | ±131.2091 | -0.699 | 0.4845 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **409**, R² = **0.0853**, Adj R² = **0.0599**, F-statistic = **3.36** (p = **1.84e-04**), Residual SE = **64.851** on **397** df, AIC = **4585.3**, BIC = **4633.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.0233** | 27.7277 | ±55.4554 | **+14.643** | **1.49e-48** | *** |
| Education: graduate level (vs college) | +6.9906 | 6.7506 | ±13.5012 | +1.036 | 0.3004 |  |
| Education: high school or below (vs college) | -3.8894 | 14.6370 | ±29.2739 | -0.266 | 0.7905 |  |
| Site: UCSD (vs UAB) | -10.9235 | 8.4935 | ±16.9870 | -1.286 | 0.1984 |  |
| Site: UW (vs UAB) | -5.8264 | 7.9097 | ±15.8194 | -0.737 | 0.4614 |  |
| Age (years) | +0.2531 | 0.3281 | ±0.6563 | +0.771 | 0.4405 |  |
| **BMI (kg/m2)** | **-1.2176** | 0.5081 | ±1.0162 | **-2.396** | **0.0166** | * |
| **Hypertension** | **-23.3154** | 7.3434 | ±14.6868 | **-3.175** | **0.0015** | ** |
| High cholesterol | -0.8252 | 6.7877 | ±13.5754 | -0.122 | 0.9032 |  |
| Kidney disease | -35.3413 | 19.1266 | ±38.2533 | -1.848 | 0.0646 | . |
| Circulatory disease | +10.4342 | 11.9359 | ±23.8717 | +0.874 | 0.3820 |  |
| Time 181-250, pooled (%) | -13.7714 | 12.1082 | ±24.2163 | -1.137 | 0.2554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **409**, R² = **0.0843**, Adj R² = **0.0589**, F-statistic = **3.32** (p = **2.18e-04**), Residual SE = **64.888** on **397** df, AIC = **4585.7**, BIC = **4633.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.9866** | 26.8518 | ±53.7036 | **+15.082** | **2.12e-51** | *** |
| Education: graduate level (vs college) | +6.9798 | 6.7452 | ±13.4903 | +1.035 | 0.3008 |  |
| Education: high school or below (vs college) | -3.9725 | 14.6294 | ±29.2589 | -0.272 | 0.7860 |  |
| Site: UCSD (vs UAB) | -11.0307 | 8.4706 | ±16.9413 | -1.302 | 0.1928 |  |
| Site: UW (vs UAB) | -5.8061 | 7.9191 | ±15.8383 | -0.733 | 0.4635 |  |
| Age (years) | +0.2438 | 0.3253 | ±0.6506 | +0.749 | 0.4537 |  |
| **BMI (kg/m2)** | **-1.2022** | 0.4853 | ±0.9706 | **-2.477** | **0.0132** | * |
| **Hypertension** | **-23.4718** | 7.3597 | ±14.7194 | **-3.189** | **0.0014** | ** |
| High cholesterol | -0.4979 | 6.7902 | ±13.5805 | -0.073 | 0.9415 |  |
| Kidney disease | -35.8612 | 18.9601 | ±37.9203 | -1.891 | 0.0586 | . |
| Circulatory disease | +10.6582 | 11.9546 | ±23.9092 | +0.892 | 0.3726 |  |
| Avg. daily time 181-250 (%) | -11.2727 | 11.3024 | ±22.6048 | -0.997 | 0.3186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **409**, R² = **0.0854**, Adj R² = **0.0601**, F-statistic = **3.37** (p = **1.79e-04**), Residual SE = **64.846** on **397** df, AIC = **4585.2**, BIC = **4633.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.2391** | 27.7716 | ±55.5432 | **+14.628** | **1.87e-48** | *** |
| Education: graduate level (vs college) | +6.9863 | 6.7495 | ±13.4991 | +1.035 | 0.3006 |  |
| Education: high school or below (vs college) | -3.9149 | 14.6361 | ±29.2722 | -0.267 | 0.7891 |  |
| Site: UCSD (vs UAB) | -10.9430 | 8.4916 | ±16.9833 | -1.289 | 0.1975 |  |
| Site: UW (vs UAB) | -5.8396 | 7.9071 | ±15.8142 | -0.739 | 0.4602 |  |
| Age (years) | +0.2521 | 0.3280 | ±0.6561 | +0.769 | 0.4422 |  |
| **BMI (kg/m2)** | **-1.2191** | 0.5090 | ±1.0180 | **-2.395** | **0.0166** | * |
| **Hypertension** | **-23.3166** | 7.3436 | ±14.6872 | **-3.175** | **0.0015** | ** |
| High cholesterol | -0.8293 | 6.7865 | ±13.5730 | -0.122 | 0.9027 |  |
| Kidney disease | -35.3046 | 19.1324 | ±38.2648 | -1.845 | 0.0650 | . |
| Circulatory disease | +10.4294 | 11.9331 | ±23.8661 | +0.874 | 0.3821 |  |
| Time > 180 (%) | -14.0650 | 12.0728 | ±24.1456 | -1.165 | 0.2440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **409**, R² = **0.0844**, Adj R² = **0.0590**, F-statistic = **3.33** (p = **2.13e-04**), Residual SE = **64.883** on **397** df, AIC = **4585.7**, BIC = **4633.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.1964** | 26.8735 | ±53.7469 | **+15.078** | **2.26e-51** | *** |
| Education: graduate level (vs college) | +6.9737 | 6.7435 | ±13.4871 | +1.034 | 0.3011 |  |
| Education: high school or below (vs college) | -4.0045 | 14.6283 | ±29.2566 | -0.274 | 0.7843 |  |
| Site: UCSD (vs UAB) | -11.0514 | 8.4683 | ±16.9366 | -1.305 | 0.1919 |  |
| Site: UW (vs UAB) | -5.8166 | 7.9153 | ±15.8306 | -0.735 | 0.4624 |  |
| Age (years) | +0.2426 | 0.3252 | ±0.6504 | +0.746 | 0.4558 |  |
| **BMI (kg/m2)** | **-1.2033** | 0.4857 | ±0.9714 | **-2.477** | **0.0132** | * |
| **Hypertension** | **-23.4742** | 7.3600 | ±14.7200 | **-3.189** | **0.0014** | ** |
| High cholesterol | -0.4961 | 6.7893 | ±13.5785 | -0.073 | 0.9418 |  |
| Kidney disease | -35.8290 | 18.9644 | ±37.9287 | -1.889 | 0.0589 | . |
| Circulatory disease | +10.6581 | 11.9516 | ±23.9032 | +0.892 | 0.3725 |  |
| Avg. daily time > 180 (%) | -11.5864 | 11.2535 | ±22.5070 | -1.030 | 0.3032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **409**, R² = **0.0875**, Adj R² = **0.0623**, F-statistic = **3.46** (p = **1.25e-04**), Residual SE = **64.771** on **397** df, AIC = **4584.3**, BIC = **4632.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.2824** | 26.6286 | ±53.2572 | **+15.220** | **2.61e-52** | *** |
| Education: graduate level (vs college) | +6.5304 | 6.7511 | ±13.5021 | +0.967 | 0.3334 |  |
| Education: high school or below (vs college) | -3.1994 | 14.5703 | ±29.1406 | -0.220 | 0.8262 |  |
| Site: UCSD (vs UAB) | -10.6232 | 8.4448 | ±16.8897 | -1.258 | 0.2084 |  |
| Site: UW (vs UAB) | -5.2888 | 7.9295 | ±15.8591 | -0.667 | 0.5048 |  |
| Age (years) | +0.1770 | 0.3327 | ±0.6654 | +0.532 | 0.5947 |  |
| **BMI (kg/m2)** | **-1.1418** | 0.4712 | ±0.9424 | **-2.423** | **0.0154** | * |
| **Hypertension** | **-22.6884** | 7.3480 | ±14.6960 | **-3.088** | **0.0020** | ** |
| High cholesterol | -0.0578 | 6.8106 | ±13.6212 | -0.008 | 0.9932 |  |
| Kidney disease | -35.9514 | 18.4632 | ±36.9263 | -1.947 | 0.0515 | . |
| Circulatory disease | +9.9102 | 12.0542 | ±24.1084 | +0.822 | 0.4110 |  |
| Nocturnal time > 180 (%) | -13.7339 | 9.9101 | ±19.8202 | -1.386 | 0.1658 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 403; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **403**, R² = **0.1408**, Adj R² = **0.1189**, F-statistic = **6.43** (p = **3.47e-09**), Residual SE = **16.382** on **392** df, AIC = **3408.2**, BIC = **3452.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6403** | 7.8668 | ±15.7337 | **+7.454** | **9.05e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7783** | 1.7654 | ±3.5307 | **-2.707** | **0.0068** | ** |
| Education: high school or below (vs college) | -1.6751 | 3.1922 | ±6.3844 | -0.525 | 0.5998 |  |
| Site: UCSD (vs UAB) | -0.9144 | 2.1951 | ±4.3902 | -0.417 | 0.6770 |  |
| **Site: UW (vs UAB)** | **-4.2796** | 2.0120 | ±4.0240 | **-2.127** | **0.0334** | * |
| **Age (years)** | **-0.3240** | 0.0822 | ±0.1643 | **-3.944** | **8.03e-05** | *** |
| **BMI (kg/m2)** | **+0.4654** | 0.1472 | ±0.2944 | **+3.162** | **0.0016** | ** |
| Hypertension | +2.0906 | 1.9211 | ±3.8422 | +1.088 | 0.2765 |  |
| High cholesterol | -0.9807 | 1.7797 | ±3.5594 | -0.551 | 0.5816 |  |
| Kidney disease | -2.1739 | 4.8814 | ±9.7627 | -0.445 | 0.6561 |  |
| Circulatory disease | -3.0018 | 2.2729 | ±4.5457 | -1.321 | 0.1866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.09e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.5056** | 17.0337 | ±34.0673 | **+3.317** | **9.09e-04** | *** |
| **Education: graduate level (vs college)** | **-4.7642** | 1.7746 | ±3.5492 | **-2.685** | **0.0073** | ** |
| Education: high school or below (vs college) | -1.6980 | 3.1877 | ±6.3755 | -0.533 | 0.5943 |  |
| Site: UCSD (vs UAB) | -0.8989 | 2.1993 | ±4.3987 | -0.409 | 0.6827 |  |
| **Site: UW (vs UAB)** | **-4.2595** | 2.0171 | ±4.0342 | **-2.112** | **0.0347** | * |
| **Age (years)** | **-0.3251** | 0.0826 | ±0.1653 | **-3.935** | **8.33e-05** | *** |
| **BMI (kg/m2)** | **+0.4633** | 0.1487 | ±0.2973 | **+3.117** | **0.0018** | ** |
| Hypertension | +2.0684 | 1.9421 | ±3.8842 | +1.065 | 0.2869 |  |
| High cholesterol | -1.0416 | 1.8710 | ±3.7420 | -0.557 | 0.5777 |  |
| Kidney disease | -2.1388 | 4.9039 | ±9.8079 | -0.436 | 0.6627 |  |
| Circulatory disease | -2.9863 | 2.2806 | ±4.5613 | -1.309 | 0.1904 |  |
| HbA1c (%) | +0.4110 | 2.9489 | ±5.8979 | +0.139 | 0.8892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **403**, R² = **0.1439**, Adj R² = **0.1198**, F-statistic = **5.98** (p = **4.99e-09**), Residual SE = **16.373** on **391** df, AIC = **3408.8**, BIC = **3456.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7676** | 15.3355 | ±30.6710 | **+2.854** | **0.0043** | ** |
| **Education: graduate level (vs college)** | **-4.7175** | 1.7638 | ±3.5276 | **-2.675** | **0.0075** | ** |
| Education: high school or below (vs college) | -1.4970 | 3.2026 | ±6.4052 | -0.467 | 0.6402 |  |
| Site: UCSD (vs UAB) | -1.0263 | 2.1955 | ±4.3909 | -0.467 | 0.6402 |  |
| **Site: UW (vs UAB)** | **-4.4149** | 2.0060 | ±4.0120 | **-2.201** | **0.0277** | * |
| **Age (years)** | **-0.3203** | 0.0826 | ±0.1651 | **-3.880** | **1.05e-04** | *** |
| **BMI (kg/m2)** | **+0.4566** | 0.1471 | ±0.2941 | **+3.104** | **0.0019** | ** |
| Hypertension | +1.9132 | 1.9092 | ±3.8184 | +1.002 | 0.3163 |  |
| High cholesterol | -0.9140 | 1.7900 | ±3.5800 | -0.511 | 0.6096 |  |
| Kidney disease | -2.1854 | 4.9367 | ±9.8735 | -0.443 | 0.6580 |  |
| Circulatory disease | -3.0519 | 2.2843 | ±4.5686 | -1.336 | 0.1815 |  |
| Mean glucose (mg/dL) | +0.1313 | 0.1136 | ±0.2272 | +1.156 | 0.2477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **403**, R² = **0.1439**, Adj R² = **0.1198**, F-statistic = **5.98** (p = **4.99e-09**), Residual SE = **16.373** on **391** df, AIC = **3408.8**, BIC = **3456.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +25.5966 | 29.9369 | ±59.8738 | +0.855 | 0.3925 |  |
| **Education: graduate level (vs college)** | **-4.7175** | 1.7638 | ±3.5276 | **-2.675** | **0.0075** | ** |
| Education: high school or below (vs college) | -1.4970 | 3.2026 | ±6.4052 | -0.467 | 0.6402 |  |
| Site: UCSD (vs UAB) | -1.0263 | 2.1955 | ±4.3909 | -0.467 | 0.6402 |  |
| **Site: UW (vs UAB)** | **-4.4149** | 2.0060 | ±4.0120 | **-2.201** | **0.0277** | * |
| **Age (years)** | **-0.3203** | 0.0826 | ±0.1651 | **-3.880** | **1.05e-04** | *** |
| **BMI (kg/m2)** | **+0.4566** | 0.1471 | ±0.2941 | **+3.104** | **0.0019** | ** |
| Hypertension | +1.9132 | 1.9092 | ±3.8184 | +1.002 | 0.3163 |  |
| High cholesterol | -0.9140 | 1.7900 | ±3.5800 | -0.511 | 0.6096 |  |
| Kidney disease | -2.1854 | 4.9367 | ±9.8735 | -0.443 | 0.6580 |  |
| Circulatory disease | -3.0519 | 2.2843 | ±4.5686 | -1.336 | 0.1815 |  |
| GMI (%) | +5.4897 | 4.7495 | ±9.4991 | +1.156 | 0.2477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **403**, R² = **0.1449**, Adj R² = **0.1209**, F-statistic = **6.02** (p = **4.10e-09**), Residual SE = **16.364** on **391** df, AIC = **3408.3**, BIC = **3456.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.7279** | 12.6288 | ±25.2576 | **+3.542** | **3.97e-04** | *** |
| **Education: graduate level (vs college)** | **-4.6434** | 1.7548 | ±3.5096 | **-2.646** | **0.0081** | ** |
| Education: high school or below (vs college) | -1.4878 | 3.2104 | ±6.4209 | -0.463 | 0.6431 |  |
| Site: UCSD (vs UAB) | -1.1967 | 2.1883 | ±4.3766 | -0.547 | 0.5845 |  |
| **Site: UW (vs UAB)** | **-4.5054** | 2.0106 | ±4.0211 | **-2.241** | **0.0250** | * |
| **Age (years)** | **-0.3069** | 0.0828 | ±0.1656 | **-3.705** | **2.11e-04** | *** |
| **BMI (kg/m2)** | **+0.4417** | 0.1439 | ±0.2877 | **+3.070** | **0.0021** | ** |
| Hypertension | +1.8791 | 1.9119 | ±3.8238 | +0.983 | 0.3257 |  |
| High cholesterol | -0.9743 | 1.7832 | ±3.5664 | -0.546 | 0.5848 |  |
| Kidney disease | -1.9200 | 4.9048 | ±9.8096 | -0.391 | 0.6955 |  |
| Circulatory disease | -2.9488 | 2.2787 | ±4.5574 | -1.294 | 0.1956 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.1194 | 0.0896 | ±0.1792 | +1.333 | 0.1824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **403**, R² = **0.1433**, Adj R² = **0.1192**, F-statistic = **5.95** (p = **5.65e-09**), Residual SE = **16.379** on **391** df, AIC = **3409.1**, BIC = **3457.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.6327** | 9.8766 | ±19.7532 | **+5.329** | **9.87e-08** | *** |
| **Education: graduate level (vs college)** | **-4.6197** | 1.7685 | ±3.5369 | **-2.612** | **0.0090** | ** |
| Education: high school or below (vs college) | -1.5933 | 3.1640 | ±6.3279 | -0.504 | 0.6146 |  |
| Site: UCSD (vs UAB) | -0.8012 | 2.1927 | ±4.3854 | -0.365 | 0.7148 |  |
| **Site: UW (vs UAB)** | **-4.1449** | 2.0085 | ±4.0171 | **-2.064** | **0.0391** | * |
| **Age (years)** | **-0.3255** | 0.0822 | ±0.1645 | **-3.959** | **7.54e-05** | *** |
| **BMI (kg/m2)** | **+0.4604** | 0.1465 | ±0.2930 | **+3.143** | **0.0017** | ** |
| Hypertension | +1.9515 | 1.9151 | ±3.8302 | +1.019 | 0.3082 |  |
| High cholesterol | -0.8435 | 1.7927 | ±3.5854 | -0.471 | 0.6380 |  |
| Kidney disease | -2.6008 | 4.9886 | ±9.9771 | -0.521 | 0.6021 |  |
| Circulatory disease | -3.0922 | 2.2580 | ±4.5159 | -1.369 | 0.1709 |  |
| Glucose SD, pooled (mg/dL) | +0.3637 | 0.3634 | ±0.7268 | +1.001 | 0.3169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **403**, R² = **0.1435**, Adj R² = **0.1194**, F-statistic = **5.96** (p = **5.40e-09**), Residual SE = **16.377** on **391** df, AIC = **3409.0**, BIC = **3456.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0094** | 9.3960 | ±18.7919 | **+5.642** | **1.68e-08** | *** |
| **Education: graduate level (vs college)** | **-4.5934** | 1.7708 | ±3.5416 | **-2.594** | **0.0095** | ** |
| Education: high school or below (vs college) | -1.5463 | 3.1563 | ±6.3127 | -0.490 | 0.6242 |  |
| Site: UCSD (vs UAB) | -0.8134 | 2.1882 | ±4.3763 | -0.372 | 0.7101 |  |
| **Site: UW (vs UAB)** | **-4.1480** | 2.0097 | ±4.0193 | **-2.064** | **0.0390** | * |
| **Age (years)** | **-0.3263** | 0.0823 | ±0.1646 | **-3.964** | **7.37e-05** | *** |
| **BMI (kg/m2)** | **+0.4575** | 0.1457 | ±0.2914 | **+3.140** | **0.0017** | ** |
| Hypertension | +1.9957 | 1.9141 | ±3.8283 | +1.043 | 0.2971 |  |
| High cholesterol | -0.8488 | 1.7905 | ±3.5809 | -0.474 | 0.6355 |  |
| Kidney disease | -2.6006 | 4.9762 | ±9.9525 | -0.523 | 0.6012 |  |
| Circulatory disease | -3.0281 | 2.2655 | ±4.5309 | -1.337 | 0.1813 |  |
| Avg. daily SD (mg/dL) | +0.3782 | 0.3626 | ±0.7251 | +1.043 | 0.2969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **403**, R² = **0.1414**, Adj R² = **0.1173**, F-statistic = **5.85** (p = **8.17e-09**), Residual SE = **16.397** on **391** df, AIC = **3409.9**, BIC = **3457.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.7559** | 9.5509 | ±19.1019 | **+5.838** | **5.29e-09** | *** |
| **Education: graduate level (vs college)** | **-4.7137** | 1.7726 | ±3.5451 | **-2.659** | **0.0078** | ** |
| Education: high school or below (vs college) | -1.6681 | 3.1809 | ±6.3618 | -0.524 | 0.6000 |  |
| Site: UCSD (vs UAB) | -0.8401 | 2.1969 | ±4.3937 | -0.382 | 0.7022 |  |
| **Site: UW (vs UAB)** | **-4.1900** | 2.0108 | ±4.0216 | **-2.084** | **0.0372** | * |
| **Age (years)** | **-0.3253** | 0.0823 | ±0.1647 | **-3.952** | **7.76e-05** | *** |
| **BMI (kg/m2)** | **+0.4648** | 0.1470 | ±0.2941 | **+3.161** | **0.0016** | ** |
| Hypertension | +2.0592 | 1.9225 | ±3.8450 | +1.071 | 0.2841 |  |
| High cholesterol | -0.9254 | 1.7848 | ±3.5696 | -0.518 | 0.6041 |  |
| Kidney disease | -2.3729 | 4.9620 | ±9.9241 | -0.478 | 0.6325 |  |
| Circulatory disease | -3.0383 | 2.2640 | ±4.5280 | -1.342 | 0.1796 |  |
| CV (%) | +0.1967 | 0.3804 | ±0.7608 | +0.517 | 0.6051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **403**, R² = **0.1413**, Adj R² = **0.1171**, F-statistic = **5.85** (p = **8.36e-09**), Residual SE = **16.398** on **391** df, AIC = **3410.0**, BIC = **3458.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.1085** | 9.4925 | ±18.9850 | **+6.438** | **1.21e-10** | *** |
| **Education: graduate level (vs college)** | **-4.7125** | 1.7716 | ±3.5433 | **-2.660** | **0.0078** | ** |
| Education: high school or below (vs college) | -1.6815 | 3.1820 | ±6.3641 | -0.528 | 0.5972 |  |
| Site: UCSD (vs UAB) | -0.8616 | 2.1979 | ±4.3958 | -0.392 | 0.6951 |  |
| **Site: UW (vs UAB)** | **-4.2129** | 2.0135 | ±4.0269 | **-2.092** | **0.0364** | * |
| **Age (years)** | **-0.3249** | 0.0823 | ±0.1646 | **-3.949** | **7.85e-05** | *** |
| **BMI (kg/m2)** | **+0.4648** | 0.1472 | ±0.2944 | **+3.158** | **0.0016** | ** |
| Hypertension | +2.0619 | 1.9221 | ±3.8441 | +1.073 | 0.2834 |  |
| High cholesterol | -0.9255 | 1.7870 | ±3.5740 | -0.518 | 0.6045 |  |
| Kidney disease | -2.3096 | 4.9334 | ±9.8669 | -0.468 | 0.6397 |  |
| Circulatory disease | -3.0202 | 2.2653 | ±4.5306 | -1.333 | 0.1825 |  |
| Mean / SD ratio | -0.3561 | 0.7613 | ±1.5225 | -0.468 | 0.6399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **403**, R² = **0.1417**, Adj R² = **0.1176**, F-statistic = **5.87** (p = **7.73e-09**), Residual SE = **16.394** on **391** df, AIC = **3409.8**, BIC = **3457.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6679** | 9.2442 | ±18.4884 | **+6.671** | **2.54e-11** | *** |
| **Education: graduate level (vs college)** | **-4.6805** | 1.7734 | ±3.5469 | **-2.639** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.6709 | 3.1726 | ±6.3452 | -0.527 | 0.5984 |  |
| Site: UCSD (vs UAB) | -0.8579 | 2.1938 | ±4.3876 | -0.391 | 0.6958 |  |
| **Site: UW (vs UAB)** | **-4.1952** | 2.0134 | ±4.0268 | **-2.084** | **0.0372** | * |
| **Age (years)** | **-0.3258** | 0.0824 | ±0.1647 | **-3.955** | **7.65e-05** | *** |
| **BMI (kg/m2)** | **+0.4628** | 0.1469 | ±0.2937 | **+3.151** | **0.0016** | ** |
| Hypertension | +2.0745 | 1.9225 | ±3.8450 | +1.079 | 0.2806 |  |
| High cholesterol | -0.9233 | 1.7831 | ±3.5662 | -0.518 | 0.6046 |  |
| Kidney disease | -2.3617 | 4.9194 | ±9.8388 | -0.480 | 0.6312 |  |
| Circulatory disease | -2.9742 | 2.2733 | ±4.5466 | -1.308 | 0.1908 |  |
| Avg. daily mean/SD | -0.3762 | 0.5834 | ±1.1669 | -0.645 | 0.5190 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **403**, R² = **0.1423**, Adj R² = **0.1181**, F-statistic = **5.90** (p = **6.92e-09**), Residual SE = **16.389** on **391** df, AIC = **3409.5**, BIC = **3457.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.2177** | 9.5294 | ±19.0589 | **+5.689** | **1.27e-08** | *** |
| **Education: graduate level (vs college)** | **-4.7626** | 1.7682 | ±3.5363 | **-2.694** | **0.0071** | ** |
| Education: high school or below (vs college) | -1.8586 | 3.2115 | ±6.4231 | -0.579 | 0.5628 |  |
| Site: UCSD (vs UAB) | -0.8454 | 2.1986 | ±4.3973 | -0.385 | 0.7006 |  |
| **Site: UW (vs UAB)** | **-4.1141** | 2.0364 | ±4.0727 | **-2.020** | **0.0433** | * |
| **Age (years)** | **-0.3182** | 0.0826 | ±0.1652 | **-3.851** | **1.18e-04** | *** |
| **BMI (kg/m2)** | **+0.4698** | 0.1457 | ±0.2914 | **+3.224** | **0.0013** | ** |
| Hypertension | +2.1456 | 1.9249 | ±3.8498 | +1.115 | 0.2650 |  |
| High cholesterol | -1.0239 | 1.7839 | ±3.5679 | -0.574 | 0.5660 |  |
| Kidney disease | -2.4059 | 4.8960 | ±9.7920 | -0.491 | 0.6231 |  |
| Circulatory disease | -2.9784 | 2.2765 | ±4.5530 | -1.308 | 0.1908 |  |
| MAG (mg/dL/h) | +0.1139 | 0.1424 | ±0.2848 | +0.800 | 0.4238 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **403**, R² = **0.1429**, Adj R² = **0.1188**, F-statistic = **5.92** (p = **6.14e-09**), Residual SE = **16.383** on **391** df, AIC = **3409.3**, BIC = **3457.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.8026** | 10.4895 | ±20.9791 | **+5.034** | **4.81e-07** | *** |
| **Education: graduate level (vs college)** | **-4.6853** | 1.7760 | ±3.5520 | **-2.638** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.6538 | 3.1691 | ±6.3382 | -0.522 | 0.6018 |  |
| Site: UCSD (vs UAB) | -0.8380 | 2.2008 | ±4.4016 | -0.381 | 0.7034 |  |
| **Site: UW (vs UAB)** | **-4.1725** | 2.0272 | ±4.0544 | **-2.058** | **0.0396** | * |
| **Age (years)** | **-0.3248** | 0.0826 | ±0.1653 | **-3.931** | **8.47e-05** | *** |
| **BMI (kg/m2)** | **+0.4733** | 0.1509 | ±0.3017 | **+3.137** | **0.0017** | ** |
| Hypertension | +2.1414 | 1.9266 | ±3.8531 | +1.112 | 0.2663 |  |
| High cholesterol | -0.9392 | 1.7816 | ±3.5633 | -0.527 | 0.5981 |  |
| Kidney disease | -2.4404 | 4.9388 | ±9.8777 | -0.494 | 0.6212 |  |
| Circulatory disease | -3.0411 | 2.2737 | ±4.5474 | -1.338 | 0.1811 |  |
| Avg. daily range (mg/dL) | +0.0694 | 0.0754 | ±0.1508 | +0.921 | 0.3571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **403**, R² = **0.1447**, Adj R² = **0.1207**, F-statistic = **6.02** (p = **4.23e-09**), Residual SE = **16.365** on **391** df, AIC = **3408.4**, BIC = **3456.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8251** | 8.0951 | ±16.1901 | **+6.896** | **5.34e-12** | *** |
| **Education: graduate level (vs college)** | **-4.8529** | 1.7668 | ±3.5336 | **-2.747** | **0.0060** | ** |
| Education: high school or below (vs college) | -1.8701 | 3.1895 | ±6.3791 | -0.586 | 0.5577 |  |
| Site: UCSD (vs UAB) | -0.7871 | 2.1892 | ±4.3784 | -0.360 | 0.7192 |  |
| **Site: UW (vs UAB)** | **-4.3128** | 2.0032 | ±4.0065 | **-2.153** | **0.0313** | * |
| **Age (years)** | **-0.3238** | 0.0816 | ±0.1631 | **-3.969** | **7.21e-05** | *** |
| **BMI (kg/m2)** | **+0.4637** | 0.1466 | ±0.2932 | **+3.164** | **0.0016** | ** |
| Hypertension | +1.8787 | 1.9409 | ±3.8818 | +0.968 | 0.3331 |  |
| High cholesterol | -1.0241 | 1.7784 | ±3.5568 | -0.576 | 0.5647 |  |
| Kidney disease | -2.2015 | 4.8476 | ±9.6952 | -0.454 | 0.6497 |  |
| Circulatory disease | -3.2128 | 2.2663 | ±4.5326 | -1.418 | 0.1563 |  |
| SD of daily means (mg/dL) | +0.5802 | 0.4265 | ±0.8530 | +1.360 | 0.1737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **403**, R² = **0.1447**, Adj R² = **0.1206**, F-statistic = **6.01** (p = **4.28e-09**), Residual SE = **16.366** on **391** df, AIC = **3408.4**, BIC = **3456.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +420.8882 | 274.6157 | ±549.2315 | +1.533 | 0.1254 |  |
| **Education: graduate level (vs college)** | **-4.6607** | 1.7792 | ±3.5583 | **-2.620** | **0.0088** | ** |
| Education: high school or below (vs college) | -1.5478 | 3.1455 | ±6.2911 | -0.492 | 0.6227 |  |
| Site: UCSD (vs UAB) | -0.7557 | 2.2075 | ±4.4150 | -0.342 | 0.7321 |  |
| **Site: UW (vs UAB)** | **-4.1912** | 2.0124 | ±4.0248 | **-2.083** | **0.0373** | * |
| **Age (years)** | **-0.3205** | 0.0829 | ±0.1657 | **-3.868** | **1.10e-04** | *** |
| **BMI (kg/m2)** | **+0.4689** | 0.1551 | ±0.3102 | **+3.023** | **0.0025** | ** |
| Hypertension | +2.0411 | 1.9121 | ±3.8242 | +1.067 | 0.2858 |  |
| High cholesterol | -1.0007 | 1.7767 | ±3.5534 | -0.563 | 0.5733 |  |
| Kidney disease | -2.5110 | 4.9360 | ±9.8720 | -0.509 | 0.6110 |  |
| Circulatory disease | -2.9902 | 2.2396 | ±4.4791 | -1.335 | 0.1818 |  |
| Time in range 70-180, pooled (%) | -3.6432 | 2.7666 | ±5.5331 | -1.317 | 0.1879 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **403**, R² = **0.1452**, Adj R² = **0.1211**, F-statistic = **6.04** (p = **3.90e-09**), Residual SE = **16.361** on **391** df, AIC = **3408.2**, BIC = **3456.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +428.9533 | 260.4543 | ±520.9086 | +1.647 | 0.0996 | . |
| **Education: graduate level (vs college)** | **-4.6216** | 1.7700 | ±3.5401 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | -1.5059 | 3.1425 | ±6.2850 | -0.479 | 0.6318 |  |
| Site: UCSD (vs UAB) | -0.8072 | 2.1909 | ±4.3819 | -0.368 | 0.7126 |  |
| **Site: UW (vs UAB)** | **-4.2915** | 2.0076 | ±4.0152 | **-2.138** | **0.0325** | * |
| **Age (years)** | **-0.3202** | 0.0824 | ±0.1647 | **-3.888** | **1.01e-04** | *** |
| **BMI (kg/m2)** | **+0.4662** | 0.1486 | ±0.2973 | **+3.136** | **0.0017** | ** |
| Hypertension | +2.1953 | 1.9261 | ±3.8523 | +1.140 | 0.2544 |  |
| High cholesterol | -1.0536 | 1.7743 | ±3.5487 | -0.594 | 0.5526 |  |
| Kidney disease | -2.3892 | 4.9476 | ±9.8952 | -0.483 | 0.6292 |  |
| Circulatory disease | -3.0919 | 2.2514 | ±4.5027 | -1.373 | 0.1696 |  |
| Avg. daily time in range 70-180 (%) | -3.7212 | 2.6176 | ±5.2351 | -1.422 | 0.1551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.1410**, Adj R² = **0.1168**, F-statistic = **5.83** (p = **8.88e-09**), Residual SE = **16.401** on **391** df, AIC = **3410.1**, BIC = **3458.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4568** | 7.9135 | ±15.8270 | **+7.387** | **1.50e-13** | *** |
| **Education: graduate level (vs college)** | **-4.7730** | 1.7705 | ±3.5411 | **-2.696** | **0.0070** | ** |
| Education: high school or below (vs college) | -1.6448 | 3.2041 | ±6.4081 | -0.513 | 0.6077 |  |
| Site: UCSD (vs UAB) | -0.8263 | 2.2238 | ±4.4475 | -0.372 | 0.7102 |  |
| **Site: UW (vs UAB)** | **-4.2335** | 2.0318 | ±4.0636 | **-2.084** | **0.0372** | * |
| **Age (years)** | **-0.3235** | 0.0823 | ±0.1645 | **-3.932** | **8.44e-05** | *** |
| **BMI (kg/m2)** | **+0.4654** | 0.1472 | ±0.2944 | **+3.162** | **0.0016** | ** |
| Hypertension | +2.0605 | 1.9257 | ±3.8515 | +1.070 | 0.2846 |  |
| High cholesterol | -0.9751 | 1.7825 | ±3.5650 | -0.547 | 0.5843 |  |
| Kidney disease | -2.1087 | 4.9164 | ±9.8328 | -0.429 | 0.6680 |  |
| Circulatory disease | -3.0287 | 2.2791 | ±4.5582 | -1.329 | 0.1839 |  |
| Any reading < 54 during wear (0/1) | +0.6049 | 2.0390 | ±4.0780 | +0.297 | 0.7667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.1419**, Adj R² = **0.1177**, F-statistic = **5.88** (p = **7.51e-09**), Residual SE = **16.393** on **391** df, AIC = **3409.7**, BIC = **3457.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3126** | 7.8224 | ±15.6447 | **+7.455** | **9.01e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7705** | 1.7674 | ±3.5347 | **-2.699** | **0.0070** | ** |
| Education: high school or below (vs college) | -1.5269 | 3.2054 | ±6.4107 | -0.476 | 0.6338 |  |
| Site: UCSD (vs UAB) | -0.7424 | 2.2088 | ±4.4176 | -0.336 | 0.7368 |  |
| **Site: UW (vs UAB)** | **-4.2042** | 2.0219 | ±4.0438 | **-2.079** | **0.0376** | * |
| **Age (years)** | **-0.3199** | 0.0821 | ±0.1643 | **-3.895** | **9.84e-05** | *** |
| **BMI (kg/m2)** | **+0.4592** | 0.1466 | ±0.2933 | **+3.132** | **0.0017** | ** |
| Hypertension | +1.9708 | 1.9360 | ±3.8720 | +1.018 | 0.3087 |  |
| High cholesterol | -0.9352 | 1.7859 | ±3.5718 | -0.524 | 0.6005 |  |
| Kidney disease | -2.0567 | 4.8980 | ±9.7959 | -0.420 | 0.6746 |  |
| Circulatory disease | -3.1003 | 2.2889 | ±4.5778 | -1.355 | 0.1756 |  |
| Time < 54 (%) | +10.2072 | 12.2748 | ±24.5496 | +0.832 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.1408**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.17e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6324** | 7.8769 | ±15.7538 | **+7.444** | **9.80e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7785** | 1.7701 | ±3.5401 | **-2.700** | **0.0069** | ** |
| Education: high school or below (vs college) | -1.6713 | 3.1994 | ±6.3988 | -0.522 | 0.6014 |  |
| Site: UCSD (vs UAB) | -0.9101 | 2.1994 | ±4.3988 | -0.414 | 0.6790 |  |
| **Site: UW (vs UAB)** | **-4.2799** | 2.0175 | ±4.0351 | **-2.121** | **0.0339** | * |
| **Age (years)** | **-0.3239** | 0.0823 | ±0.1646 | **-3.936** | **8.27e-05** | *** |
| **BMI (kg/m2)** | **+0.4652** | 0.1475 | ±0.2950 | **+3.154** | **0.0016** | ** |
| Hypertension | +2.0888 | 1.9263 | ±3.8526 | +1.084 | 0.2782 |  |
| High cholesterol | -0.9800 | 1.7864 | ±3.5728 | -0.549 | 0.5833 |  |
| Kidney disease | -2.1688 | 4.8886 | ±9.7773 | -0.444 | 0.6573 |  |
| Circulatory disease | -3.0119 | 2.2949 | ±4.5898 | -1.312 | 0.1894 |  |
| Avg. daily time < 54 (%) | +0.8371 | 19.3271 | ±38.6543 | +0.043 | 0.9655 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.14e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7246** | 7.8882 | ±15.7764 | **+7.445** | **9.72e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7841** | 1.7762 | ±3.5525 | **-2.693** | **0.0071** | ** |
| Education: high school or below (vs college) | -1.6563 | 3.1998 | ±6.3995 | -0.518 | 0.6047 |  |
| Site: UCSD (vs UAB) | -0.9266 | 2.1988 | ±4.3976 | -0.421 | 0.6734 |  |
| **Site: UW (vs UAB)** | **-4.2930** | 2.0219 | ±4.0439 | **-2.123** | **0.0337** | * |
| **Age (years)** | **-0.3241** | 0.0824 | ±0.1649 | **-3.931** | **8.46e-05** | *** |
| **BMI (kg/m2)** | **+0.4653** | 0.1475 | ±0.2949 | **+3.155** | **0.0016** | ** |
| Hypertension | +2.0760 | 1.9291 | ±3.8582 | +1.076 | 0.2819 |  |
| High cholesterol | -0.9641 | 1.8082 | ±3.6163 | -0.533 | 0.5939 |  |
| Kidney disease | -2.1866 | 4.8967 | ±9.7933 | -0.447 | 0.6552 |  |
| Circulatory disease | -3.0059 | 2.2780 | ±4.5560 | -1.320 | 0.1870 |  |
| Time 54-69, pooled (%) | -0.4664 | 4.4718 | ±8.9436 | -0.104 | 0.9169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **403**, R² = **0.1421**, Adj R² = **0.1180**, F-statistic = **5.89** (p = **7.17e-09**), Residual SE = **16.391** on **391** df, AIC = **3409.6**, BIC = **3457.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.1024** | 7.9102 | ±15.8204 | **+7.472** | **7.92e-14** | *** |
| **Education: graduate level (vs college)** | **-4.8517** | 1.7744 | ±3.5488 | **-2.734** | **0.0063** | ** |
| Education: high school or below (vs college) | -1.5457 | 3.2444 | ±6.4889 | -0.476 | 0.6338 |  |
| Site: UCSD (vs UAB) | -0.9655 | 2.2008 | ±4.4015 | -0.439 | 0.6609 |  |
| **Site: UW (vs UAB)** | **-4.3184** | 2.0144 | ±4.0289 | **-2.144** | **0.0321** | * |
| **Age (years)** | **-0.3233** | 0.0827 | ±0.1654 | **-3.910** | **9.22e-05** | *** |
| **BMI (kg/m2)** | **+0.4653** | 0.1479 | ±0.2958 | **+3.146** | **0.0017** | ** |
| Hypertension | +1.8863 | 1.9315 | ±3.8629 | +0.977 | 0.3288 |  |
| High cholesterol | -0.8734 | 1.8047 | ±3.6093 | -0.484 | 0.6284 |  |
| Kidney disease | -2.2476 | 4.8994 | ±9.7989 | -0.459 | 0.6464 |  |
| Circulatory disease | -2.9521 | 2.2731 | ±4.5462 | -1.299 | 0.1940 |  |
| Avg. daily time 54-69 (%) | -3.5106 | 4.5069 | ±9.0137 | -0.779 | 0.4360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.15e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5635** | 7.8772 | ±15.7543 | **+7.435** | **1.05e-13** | *** |
| **Education: graduate level (vs college)** | **-4.7735** | 1.7758 | ±3.5517 | **-2.688** | **0.0072** | ** |
| Education: high school or below (vs college) | -1.6844 | 3.1927 | ±6.3855 | -0.528 | 0.5978 |  |
| Site: UCSD (vs UAB) | -0.8989 | 2.1992 | ±4.3984 | -0.409 | 0.6827 |  |
| **Site: UW (vs UAB)** | **-4.2666** | 2.0240 | ±4.0480 | **-2.108** | **0.0350** | * |
| **Age (years)** | **-0.3238** | 0.0823 | ±0.1646 | **-3.934** | **8.35e-05** | *** |
| **BMI (kg/m2)** | **+0.4653** | 0.1474 | ±0.2947 | **+3.157** | **0.0016** | ** |
| Hypertension | +2.0976 | 1.9258 | ±3.8516 | +1.089 | 0.2761 |  |
| High cholesterol | -0.9919 | 1.7975 | ±3.5950 | -0.552 | 0.5811 |  |
| Kidney disease | -2.1599 | 4.8959 | ±9.7919 | -0.441 | 0.6591 |  |
| Circulatory disease | -3.0021 | 2.2771 | ±4.5543 | -1.318 | 0.1874 |  |
| Time < 70 (%) | +0.3610 | 3.8696 | ±7.7392 | +0.093 | 0.9257 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **403**, R² = **0.1418**, Adj R² = **0.1177**, F-statistic = **5.87** (p = **7.53e-09**), Residual SE = **16.393** on **391** df, AIC = **3409.7**, BIC = **3457.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.0412** | 7.9121 | ±15.8241 | **+7.462** | **8.51e-14** | *** |
| **Education: graduate level (vs college)** | **-4.8370** | 1.7733 | ±3.5466 | **-2.728** | **0.0064** | ** |
| Education: high school or below (vs college) | -1.5830 | 3.2403 | ±6.4806 | -0.489 | 0.6252 |  |
| Site: UCSD (vs UAB) | -0.9705 | 2.1996 | ±4.3993 | -0.441 | 0.6591 |  |
| **Site: UW (vs UAB)** | **-4.3099** | 2.0156 | ±4.0312 | **-2.138** | **0.0325** | * |
| **Age (years)** | **-0.3237** | 0.0827 | ±0.1653 | **-3.916** | **9.01e-05** | *** |
| **BMI (kg/m2)** | **+0.4659** | 0.1480 | ±0.2960 | **+3.148** | **0.0016** | ** |
| Hypertension | +1.9311 | 1.9294 | ±3.8588 | +1.001 | 0.3169 |  |
| High cholesterol | -0.8962 | 1.7986 | ±3.5972 | -0.498 | 0.6183 |  |
| Kidney disease | -2.2507 | 4.8959 | ±9.7917 | -0.460 | 0.6457 |  |
| Circulatory disease | -2.9273 | 2.2724 | ±4.5448 | -1.288 | 0.1977 |  |
| Avg. daily time < 70 (%) | -2.8422 | 4.0433 | ±8.0867 | -0.703 | 0.4821 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.1420**, Adj R² = **0.1179**, F-statistic = **5.88** (p = **7.24e-09**), Residual SE = **16.391** on **391** df, AIC = **3409.6**, BIC = **3457.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1140.7157 | 1187.2124 | ±2374.4247 | +0.961 | 0.3366 |  |
| **Education: graduate level (vs college)** | **-4.7697** | 1.7673 | ±3.5346 | **-2.699** | **0.0070** | ** |
| Education: high school or below (vs college) | -1.5111 | 3.2056 | ±6.4111 | -0.471 | 0.6374 |  |
| Site: UCSD (vs UAB) | -0.7176 | 2.2109 | ±4.4219 | -0.325 | 0.7455 |  |
| **Site: UW (vs UAB)** | **-4.1882** | 2.0224 | ±4.0449 | **-2.071** | **0.0384** | * |
| **Age (years)** | **-0.3189** | 0.0823 | ±0.1645 | **-3.877** | **1.06e-04** | *** |
| **BMI (kg/m2)** | **+0.4596** | 0.1465 | ±0.2930 | **+3.138** | **0.0017** | ** |
| Hypertension | +1.9707 | 1.9342 | ±3.8684 | +1.019 | 0.3083 |  |
| High cholesterol | -0.9360 | 1.7851 | ±3.5703 | -0.524 | 0.6001 |  |
| Kidney disease | -2.0514 | 4.8992 | ±9.7983 | -0.419 | 0.6754 |  |
| Circulatory disease | -3.1070 | 2.2899 | ±4.5797 | -1.357 | 0.1748 |  |
| Time 54-250, pooled (%) | -10.8251 | 11.8765 | ±23.7530 | -0.911 | 0.3620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.09e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +345.1921 | 1813.2162 | ±3626.4324 | +0.190 | 0.8490 |  |
| **Education: graduate level (vs college)** | **-4.7789** | 1.7699 | ±3.5397 | **-2.700** | **0.0069** | ** |
| Education: high school or below (vs college) | -1.6603 | 3.1984 | ±6.3968 | -0.519 | 0.6037 |  |
| Site: UCSD (vs UAB) | -0.8954 | 2.2012 | ±4.4025 | -0.407 | 0.6842 |  |
| **Site: UW (vs UAB)** | **-4.2774** | 2.0189 | ±4.0378 | **-2.119** | **0.0341** | * |
| **Age (years)** | **-0.3235** | 0.0824 | ±0.1647 | **-3.929** | **8.54e-05** | *** |
| **BMI (kg/m2)** | **+0.4650** | 0.1473 | ±0.2946 | **+3.157** | **0.0016** | ** |
| Hypertension | +2.0867 | 1.9258 | ±3.8516 | +1.084 | 0.2786 |  |
| High cholesterol | -0.9794 | 1.7853 | ±3.5705 | -0.549 | 0.5833 |  |
| Kidney disease | -2.1571 | 4.8910 | ±9.7820 | -0.441 | 0.6592 |  |
| Circulatory disease | -3.0366 | 2.2948 | ±4.5896 | -1.323 | 0.1858 |  |
| Avg. daily time 54-250 (%) | -2.8660 | 18.1378 | ±36.2756 | -0.158 | 0.8744 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **403**, R² = **0.1448**, Adj R² = **0.1208**, F-statistic = **6.02** (p = **4.17e-09**), Residual SE = **16.364** on **391** df, AIC = **3408.3**, BIC = **3456.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2506** | 8.4644 | ±16.9288 | **+6.764** | **1.35e-11** | *** |
| **Education: graduate level (vs college)** | **-4.7020** | 1.7703 | ±3.5406 | **-2.656** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.4349 | 3.1819 | ±6.3637 | -0.451 | 0.6520 |  |
| Site: UCSD (vs UAB) | -0.9177 | 2.2058 | ±4.4117 | -0.416 | 0.6774 |  |
| **Site: UW (vs UAB)** | **-4.3312** | 2.0110 | ±4.0219 | **-2.154** | **0.0313** | * |
| **Age (years)** | **-0.3229** | 0.0834 | ±0.1669 | **-3.870** | **1.09e-04** | *** |
| **BMI (kg/m2)** | **+0.4703** | 0.1585 | ±0.3170 | **+2.967** | **0.0030** | ** |
| Hypertension | +1.9554 | 1.9114 | ±3.8228 | +1.023 | 0.3063 |  |
| High cholesterol | -0.8769 | 1.7928 | ±3.5856 | -0.489 | 0.6248 |  |
| Kidney disease | -2.6984 | 4.9952 | ±9.9905 | -0.540 | 0.5891 |  |
| Circulatory disease | -2.9852 | 2.2234 | ±4.4467 | -1.343 | 0.1794 |  |
| Time 181-250, pooled (%) | +4.0009 | 3.1265 | ±6.2529 | +1.280 | 0.2006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **403**, R² = **0.1496**, Adj R² = **0.1256**, F-statistic = **6.25** (p = **1.62e-09**), Residual SE = **16.319** on **391** df, AIC = **3406.1**, BIC = **3454.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6813** | 8.0865 | ±16.1730 | **+7.009** | **2.39e-12** | *** |
| **Education: graduate level (vs college)** | **-4.6540** | 1.7581 | ±3.5163 | **-2.647** | **0.0081** | ** |
| Education: high school or below (vs college) | -1.2270 | 3.1720 | ±6.3441 | -0.387 | 0.6989 |  |
| Site: UCSD (vs UAB) | -0.8700 | 2.1932 | ±4.3865 | -0.397 | 0.6916 |  |
| **Site: UW (vs UAB)** | **-4.3668** | 2.0022 | ±4.0043 | **-2.181** | **0.0292** | * |
| **Age (years)** | **-0.3178** | 0.0827 | ±0.1654 | **-3.842** | **1.22e-04** | *** |
| **BMI (kg/m2)** | **+0.4672** | 0.1506 | ±0.3011 | **+3.103** | **0.0019** | ** |
| Hypertension | +1.9238 | 1.9090 | ±3.8179 | +1.008 | 0.3135 |  |
| High cholesterol | -0.9197 | 1.7789 | ±3.5577 | -0.517 | 0.6051 |  |
| Kidney disease | -2.6660 | 4.9992 | ±9.9984 | -0.533 | 0.5938 |  |
| Circulatory disease | -2.9897 | 2.2186 | ±4.4372 | -1.348 | 0.1778 |  |
| Avg. daily time 181-250 (%) | +5.8078 | 2.9850 | ±5.9700 | +1.946 | 0.0517 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **403**, R² = **0.1449**, Adj R² = **0.1208**, F-statistic = **6.02** (p = **4.11e-09**), Residual SE = **16.364** on **391** df, AIC = **3408.3**, BIC = **3456.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2092** | 8.4795 | ±16.9590 | **+6.747** | **1.51e-11** | *** |
| **Education: graduate level (vs college)** | **-4.7013** | 1.7704 | ±3.5408 | **-2.655** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.4306 | 3.1819 | ±6.3638 | -0.450 | 0.6530 |  |
| Site: UCSD (vs UAB) | -0.9124 | 2.2061 | ±4.4122 | -0.414 | 0.6792 |  |
| **Site: UW (vs UAB)** | **-4.3273** | 2.0107 | ±4.0213 | **-2.152** | **0.0314** | * |
| **Age (years)** | **-0.3226** | 0.0835 | ±0.1669 | **-3.865** | **1.11e-04** | *** |
| **BMI (kg/m2)** | **+0.4706** | 0.1588 | ±0.3175 | **+2.964** | **0.0030** | ** |
| Hypertension | +1.9571 | 1.9114 | ±3.8228 | +1.024 | 0.3059 |  |
| High cholesterol | -0.8774 | 1.7925 | ±3.5851 | -0.489 | 0.6245 |  |
| Kidney disease | -2.7029 | 4.9957 | ±9.9915 | -0.541 | 0.5885 |  |
| Circulatory disease | -2.9854 | 2.2232 | ±4.4464 | -1.343 | 0.1793 |  |
| Time > 180 (%) | +4.0300 | 3.1184 | ±6.2368 | +1.292 | 0.1962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **403**, R² = **0.1497**, Adj R² = **0.1257**, F-statistic = **6.26** (p = **1.59e-09**), Residual SE = **16.318** on **391** df, AIC = **3406.1**, BIC = **3454.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6261** | 8.0981 | ±16.1961 | **+6.993** | **2.70e-12** | *** |
| **Education: graduate level (vs college)** | **-4.6534** | 1.7582 | ±3.5164 | **-2.647** | **0.0081** | ** |
| Education: high school or below (vs college) | -1.2217 | 3.1721 | ±6.3442 | -0.385 | 0.7001 |  |
| Site: UCSD (vs UAB) | -0.8615 | 2.1932 | ±4.3863 | -0.393 | 0.6945 |  |
| **Site: UW (vs UAB)** | **-4.3603** | 2.0014 | ±4.0028 | **-2.179** | **0.0294** | * |
| **Age (years)** | **-0.3174** | 0.0827 | ±0.1655 | **-3.836** | **1.25e-04** | *** |
| **BMI (kg/m2)** | **+0.4676** | 0.1507 | ±0.3015 | **+3.102** | **0.0019** | ** |
| Hypertension | +1.9276 | 1.9091 | ±3.8182 | +1.010 | 0.3126 |  |
| High cholesterol | -0.9217 | 1.7788 | ±3.5576 | -0.518 | 0.6043 |  |
| Kidney disease | -2.6684 | 5.0000 | ±10.0000 | -0.534 | 0.5936 |  |
| Circulatory disease | -2.9901 | 2.2188 | ±4.4376 | -1.348 | 0.1778 |  |
| Avg. daily time > 180 (%) | +5.8238 | 2.9728 | ±5.9456 | +1.959 | 0.0501 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **403**, R² = **0.1523**, Adj R² = **0.1284**, F-statistic = **6.39** (p = **9.33e-10**), Residual SE = **16.293** on **391** df, AIC = **3404.8**, BIC = **3452.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9379** | 7.7197 | ±15.4395 | **+7.376** | **1.64e-13** | *** |
| **Education: graduate level (vs college)** | **-4.5018** | 1.7463 | ±3.4926 | **-2.578** | **0.0099** | ** |
| Education: high school or below (vs college) | -1.6262 | 3.1751 | ±6.3502 | -0.512 | 0.6085 |  |
| Site: UCSD (vs UAB) | -1.0774 | 2.1593 | ±4.3187 | -0.499 | 0.6178 |  |
| **Site: UW (vs UAB)** | **-4.5184** | 2.0041 | ±4.0082 | **-2.255** | **0.0242** | * |
| **Age (years)** | **-0.2935** | 0.0836 | ±0.1672 | **-3.512** | **4.45e-04** | *** |
| **BMI (kg/m2)** | **+0.4471** | 0.1437 | ±0.2873 | **+3.112** | **0.0019** | ** |
| Hypertension | +1.6796 | 1.8998 | ±3.7996 | +0.884 | 0.3766 |  |
| High cholesterol | -1.1172 | 1.7771 | ±3.5543 | -0.629 | 0.5296 |  |
| Kidney disease | -2.4636 | 4.8013 | ±9.6027 | -0.513 | 0.6079 |  |
| Circulatory disease | -2.7249 | 2.2549 | ±4.5098 | -1.208 | 0.2269 |  |
| **Nocturnal time > 180 (%)** | **+5.1317** | 2.4878 | ±4.9756 | **+2.063** | **0.0391** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 140 single-predictor tests; 18 with raw p < 0.05 (about 7 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 401): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.079 vs 0.079 for covariates alone, gain -0.001; +309 per SD, p = 0.097). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 401): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.109 vs 0.100 for covariates alone, gain +0.009; -1.63 per SD, p = 0.004). Raw p < 0.05 (FDR not applicable here): TIR 70-180 (pooled) (p = 0.004), TIR 70-180 (daily avg) (p = 0.006), %>180 (daily avg) (p = 0.021), %181-250 (daily avg) (p = 0.022), %>180 (pooled) (p = 0.041).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 403): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.138 vs 0.133 for covariates alone, gain +0.006; +0.717 per SD, p = 0.011). Raw p < 0.05 (FDR not applicable here): %<54 (pooled) (p = 0.011), %54-250 (pooled) (p = 0.016).
- **Total sleep time per night (min)** (n = 409): best single predictor out of sample is **HbA1c** (CV R² 0.028 vs 0.002 for covariates alone, gain +0.027; -10.5 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): HbA1c (p = 0.001), %54-69 (pooled) (p = 0.004), %<70 (daily avg) (p = 0.007), %54-69 (daily avg) (p = 0.007), %<70 (pooled) (p = 0.007).
- **Garmin stress score, mean (0-100)** (n = 403): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.068 vs 0.056 for covariates alone, gain +0.012; +1.93 per SD, p = 0.039). Raw p < 0.05 (FDR not applicable here): %>180 nocturnal (p = 0.039).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.027, via HbA1c); Garmin stress score, mean (0-100) (+0.012, via %>180 nocturnal); Brisk-cadence minutes per day (>= 100 steps/min) (+0.009, via TIR 70-180 (pooled)); Resting heart-rate proxy (daily 5th pct, bpm) (+0.006, via %<54 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM level (0 FDR-significant / 3 raw-significant of 15); Band > 180 (0 FDR-significant / 3 raw-significant of 15); Range 70-180 (0 FDR-significant / 2 raw-significant of 10).
Level metrics: 0 FDR-significant (3 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Steps per wear-day (%>180 nocturnal, ΔAIC -5.8); Brisk-cadence minutes per day (TIR 70-180 (pooled), ΔAIC -7.5); Resting heart-rate proxy (%<54 (pooled), ΔAIC -4.2); Garmin stress score, mean (%>180 nocturnal, ΔAIC -5.4).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
