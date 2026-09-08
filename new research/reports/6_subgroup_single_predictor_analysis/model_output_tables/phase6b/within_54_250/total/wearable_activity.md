# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Total analysis base - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 771; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1189**, F-statistic = **11.39** (p = **2.50e-18**), Residual SE = **3970.187** on **760** df, AIC = **14976.8**, BIC = **15027.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17610.0497** | 1219.3992 | ±2438.7985 | **+14.442** | **2.83e-47** | *** |
| **Education: graduate level (vs college)** | **-1006.4026** | 295.4820 | ±590.9639 | **-3.406** | **6.59e-04** | *** |
| Education: high school or below (vs college) | +872.5576 | 631.1397 | ±1262.2794 | +1.383 | 0.1668 |  |
| Site: UCSD (vs UAB) | -10.3326 | 389.3921 | ±778.7842 | -0.027 | 0.9788 |  |
| Site: UW (vs UAB) | -206.8318 | 366.8178 | ±733.6357 | -0.564 | 0.5729 |  |
| **Age (years)** | **-117.2839** | 14.6500 | ±29.3000 | **-8.006** | **1.19e-15** | *** |
| BMI (kg/m2) | -4.7599 | 24.0314 | ±48.0629 | -0.198 | 0.8430 |  |
| Hypertension | +529.2261 | 346.9041 | ±693.8082 | +1.526 | 0.1271 |  |
| High cholesterol | -189.2004 | 291.6013 | ±583.2026 | -0.649 | 0.5164 |  |
| Kidney disease | -236.0257 | 575.1219 | ±1150.2439 | -0.410 | 0.6815 |  |
| **Circulatory disease** | **-1010.8211** | 427.9700 | ±855.9400 | **-2.362** | **0.0182** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **771**, R² = **0.1368**, Adj R² = **0.1243**, F-statistic = **10.94** (p = **6.33e-19**), Residual SE = **3957.981** on **759** df, AIC = **14973.0**, BIC = **15028.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13191.2392** | 2251.2250 | ±4502.4500 | **+5.860** | **4.64e-09** | *** |
| **Education: graduate level (vs college)** | **-1003.3865** | 294.1974 | ±588.3948 | **-3.411** | **6.48e-04** | *** |
| Education: high school or below (vs college) | +834.1189 | 632.0873 | ±1264.1747 | +1.320 | 0.1870 |  |
| Site: UCSD (vs UAB) | +2.3077 | 387.8319 | ±775.6638 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | -191.8740 | 366.4044 | ±732.8088 | -0.524 | 0.6005 |  |
| **Age (years)** | **-118.9088** | 14.5423 | ±29.0846 | **-8.177** | **2.92e-16** | *** |
| BMI (kg/m2) | -13.7654 | 23.3873 | ±46.7747 | -0.589 | 0.5561 |  |
| Hypertension | +424.3186 | 351.1922 | ±702.3843 | +1.208 | 0.2270 |  |
| High cholesterol | -312.4384 | 291.7150 | ±583.4299 | -1.071 | 0.2842 |  |
| Kidney disease | -195.7569 | 566.6824 | ±1133.3648 | -0.345 | 0.7298 |  |
| **Circulatory disease** | **-1083.7265** | 424.3187 | ±848.6374 | **-2.554** | **0.0106** | * |
| **HbA1c (%)** | **+861.6379** | 366.2845 | ±732.5691 | **+2.352** | **0.0187** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **771**, R² = **0.1314**, Adj R² = **0.1188**, F-statistic = **10.44** (p = **5.59e-18**), Residual SE = **3970.280** on **759** df, AIC = **14977.8**, BIC = **15033.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16286.5468** | 1830.6397 | ±3661.2794 | **+8.897** | **5.76e-19** | *** |
| **Education: graduate level (vs college)** | **-1011.4824** | 295.8027 | ±591.6053 | **-3.419** | **6.27e-04** | *** |
| Education: high school or below (vs college) | +878.5146 | 629.8647 | ±1259.7294 | +1.395 | 0.1631 |  |
| Site: UCSD (vs UAB) | +3.1448 | 389.3408 | ±778.6816 | +0.008 | 0.9936 |  |
| Site: UW (vs UAB) | -218.6530 | 366.6914 | ±733.3829 | -0.596 | 0.5510 |  |
| **Age (years)** | **-117.5271** | 14.6443 | ±29.2886 | **-8.025** | **1.01e-15** | *** |
| BMI (kg/m2) | -7.3783 | 24.1427 | ±48.2853 | -0.306 | 0.7599 |  |
| Hypertension | +497.3796 | 348.7981 | ±697.5961 | +1.426 | 0.1539 |  |
| High cholesterol | -202.2161 | 291.5210 | ±583.0421 | -0.694 | 0.4879 |  |
| Kidney disease | -275.0000 | 574.3330 | ±1148.6659 | -0.479 | 0.6321 |  |
| **Circulatory disease** | **-1038.6310** | 429.1437 | ±858.2873 | **-2.420** | **0.0155** | * |
| Mean glucose (mg/dL) | +11.9534 | 12.5761 | ±25.1521 | +0.950 | 0.3419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **771**, R² = **0.1314**, Adj R² = **0.1188**, F-statistic = **10.44** (p = **5.59e-18**), Residual SE = **3970.280** on **759** df, AIC = **14977.8**, BIC = **15033.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14632.4665** | 3338.7737 | ±6677.5474 | **+4.383** | **1.17e-05** | *** |
| **Education: graduate level (vs college)** | **-1011.4824** | 295.8027 | ±591.6053 | **-3.419** | **6.27e-04** | *** |
| Education: high school or below (vs college) | +878.5146 | 629.8647 | ±1259.7294 | +1.395 | 0.1631 |  |
| Site: UCSD (vs UAB) | +3.1448 | 389.3408 | ±778.6816 | +0.008 | 0.9936 |  |
| Site: UW (vs UAB) | -218.6530 | 366.6914 | ±733.3829 | -0.596 | 0.5510 |  |
| **Age (years)** | **-117.5271** | 14.6443 | ±29.2886 | **-8.025** | **1.01e-15** | *** |
| BMI (kg/m2) | -7.3783 | 24.1427 | ±48.2853 | -0.306 | 0.7599 |  |
| Hypertension | +497.3796 | 348.7981 | ±697.5961 | +1.426 | 0.1539 |  |
| High cholesterol | -202.2161 | 291.5210 | ±583.0421 | -0.694 | 0.4879 |  |
| Kidney disease | -275.0000 | 574.3330 | ±1148.6659 | -0.479 | 0.6321 |  |
| **Circulatory disease** | **-1038.6310** | 429.1437 | ±858.2873 | **-2.420** | **0.0155** | * |
| GMI (%) | +499.7221 | 525.7552 | ±1051.5103 | +0.950 | 0.3419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **771**, R² = **0.1324**, Adj R² = **0.1198**, F-statistic = **10.53** (p = **3.81e-18**), Residual SE = **3968.112** on **759** df, AIC = **14977.0**, BIC = **15032.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16007.8691** | 1695.2478 | ±3390.4955 | **+9.443** | **3.63e-21** | *** |
| **Education: graduate level (vs college)** | **-1010.7375** | 295.4789 | ±590.9578 | **-3.421** | **6.25e-04** | *** |
| Education: high school or below (vs college) | +868.8320 | 627.8369 | ±1255.6737 | +1.384 | 0.1664 |  |
| Site: UCSD (vs UAB) | -10.8978 | 390.0592 | ±780.1183 | -0.028 | 0.9777 |  |
| Site: UW (vs UAB) | -229.3775 | 365.2990 | ±730.5979 | -0.628 | 0.5301 |  |
| **Age (years)** | **-116.1730** | 14.6330 | ±29.2661 | **-7.939** | **2.04e-15** | *** |
| BMI (kg/m2) | -10.5018 | 24.2185 | ±48.4370 | -0.434 | 0.6646 |  |
| Hypertension | +497.8018 | 345.7354 | ±691.4709 | +1.440 | 0.1499 |  |
| High cholesterol | -218.2128 | 292.8423 | ±585.6845 | -0.745 | 0.4562 |  |
| Kidney disease | -253.3978 | 570.6908 | ±1141.3817 | -0.444 | 0.6570 |  |
| **Circulatory disease** | **-1044.2782** | 426.9985 | ±853.9971 | **-2.446** | **0.0145** | * |
| Nocturnal mean 00-06h (mg/dL) | +14.4976 | 11.3476 | ±22.6952 | +1.278 | 0.2014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1307**, Adj R² = **0.1181**, F-statistic = **10.38** (p = **7.35e-18**), Residual SE = **3971.834** on **759** df, AIC = **14978.4**, BIC = **15034.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17238.9455** | 1342.6847 | ±2685.3695 | **+12.839** | **9.89e-38** | *** |
| **Education: graduate level (vs college)** | **-999.6664** | 296.4148 | ±592.8296 | **-3.373** | **7.45e-04** | *** |
| Education: high school or below (vs college) | +858.7495 | 631.0954 | ±1262.1908 | +1.361 | 0.1736 |  |
| Site: UCSD (vs UAB) | +7.7202 | 391.3920 | ±782.7839 | +0.020 | 0.9843 |  |
| Site: UW (vs UAB) | -204.4671 | 367.4409 | ±734.8817 | -0.556 | 0.5779 |  |
| **Age (years)** | **-117.8059** | 14.7150 | ±29.4299 | **-8.006** | **1.19e-15** | *** |
| BMI (kg/m2) | -5.3727 | 23.9761 | ±47.9522 | -0.224 | 0.8227 |  |
| Hypertension | +503.4278 | 345.4408 | ±690.8816 | +1.457 | 0.1450 |  |
| High cholesterol | -195.9615 | 292.1943 | ±584.3885 | -0.671 | 0.5024 |  |
| Kidney disease | -262.3628 | 577.0757 | ±1154.1515 | -0.455 | 0.6494 |  |
| **Circulatory disease** | **-1021.7959** | 428.1085 | ±856.2169 | **-2.387** | **0.0170** | * |
| Glucose SD, pooled (mg/dL) | +21.6542 | 35.0162 | ±70.0325 | +0.618 | 0.5363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1306**, Adj R² = **0.1180**, F-statistic = **10.37** (p = **7.80e-18**), Residual SE = **3972.166** on **759** df, AIC = **14978.6**, BIC = **15034.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17334.5214** | 1325.2230 | ±2650.4460 | **+13.080** | **4.26e-39** | *** |
| **Education: graduate level (vs college)** | **-1002.7668** | 296.3871 | ±592.7741 | **-3.383** | **7.16e-04** | *** |
| Education: high school or below (vs college) | +863.6958 | 631.2738 | ±1262.5475 | +1.368 | 0.1713 |  |
| Site: UCSD (vs UAB) | +3.9156 | 391.1858 | ±782.3717 | +0.010 | 0.9920 |  |
| Site: UW (vs UAB) | -206.8037 | 367.1158 | ±734.2316 | -0.563 | 0.5732 |  |
| **Age (years)** | **-117.7425** | 14.7357 | ±29.4714 | **-7.990** | **1.35e-15** | *** |
| BMI (kg/m2) | -5.3039 | 23.9958 | ±47.9916 | -0.221 | 0.8251 |  |
| Hypertension | +508.1861 | 345.0372 | ±690.0743 | +1.473 | 0.1408 |  |
| High cholesterol | -193.4399 | 292.1020 | ±584.2040 | -0.662 | 0.5078 |  |
| Kidney disease | -254.6733 | 575.8516 | ±1151.7031 | -0.442 | 0.6583 |  |
| **Circulatory disease** | **-1017.9826** | 428.2802 | ±856.5603 | **-2.377** | **0.0175** | * |
| Avg. daily SD (mg/dL) | +17.9414 | 36.0940 | ±72.1881 | +0.497 | 0.6191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.69e-18**), Residual SE = **3972.779** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17683.1280** | 1411.0172 | ±2822.0343 | **+12.532** | **4.98e-36** | *** |
| **Education: graduate level (vs college)** | **-1008.0691** | 296.9832 | ±593.9665 | **-3.394** | **6.88e-04** | *** |
| Education: high school or below (vs college) | +875.2858 | 633.9647 | ±1267.9295 | +1.381 | 0.1674 |  |
| Site: UCSD (vs UAB) | -12.8925 | 391.6692 | ±783.3383 | -0.033 | 0.9737 |  |
| Site: UW (vs UAB) | -207.8250 | 368.5577 | ±737.1154 | -0.564 | 0.5728 |  |
| **Age (years)** | **-117.2046** | 14.7405 | ±29.4811 | **-7.951** | **1.85e-15** | *** |
| BMI (kg/m2) | -4.7930 | 24.0924 | ±48.1848 | -0.199 | 0.8423 |  |
| Hypertension | +532.2061 | 344.9495 | ±689.8990 | +1.543 | 0.1229 |  |
| High cholesterol | -188.8473 | 292.0065 | ±584.0131 | -0.647 | 0.5178 |  |
| Kidney disease | -233.4142 | 575.4874 | ±1150.9748 | -0.406 | 0.6850 |  |
| **Circulatory disease** | **-1010.5649** | 428.5001 | ±857.0001 | **-2.358** | **0.0184** | * |
| CV (%) | -4.6801 | 46.0240 | ±92.0480 | -0.102 | 0.9190 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.67e-18**), Residual SE = **3972.766** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17707.3330** | 1457.4139 | ±2914.8278 | **+12.150** | **5.75e-34** | *** |
| **Education: graduate level (vs college)** | **-1003.9938** | 296.8013 | ±593.6026 | **-3.383** | **7.18e-04** | *** |
| Education: high school or below (vs college) | +869.4888 | 633.0436 | ±1266.0873 | +1.374 | 0.1696 |  |
| Site: UCSD (vs UAB) | -7.5694 | 391.3189 | ±782.6378 | -0.019 | 0.9846 |  |
| Site: UW (vs UAB) | -206.1680 | 367.8989 | ±735.7977 | -0.560 | 0.5752 |  |
| **Age (years)** | **-117.3780** | 14.7366 | ±29.4731 | **-7.965** | **1.65e-15** | *** |
| BMI (kg/m2) | -4.7383 | 24.0541 | ±48.1083 | -0.197 | 0.8438 |  |
| Hypertension | +525.7958 | 344.4699 | ±688.9398 | +1.526 | 0.1269 |  |
| High cholesterol | -189.5784 | 292.0339 | ±584.0678 | -0.649 | 0.5162 |  |
| Kidney disease | -239.1864 | 575.7931 | ±1151.5861 | -0.415 | 0.6778 |  |
| **Circulatory disease** | **-1010.5974** | 428.3434 | ±856.6867 | **-2.359** | **0.0183** | * |
| Mean / SD ratio | -14.6775 | 115.8816 | ±231.7632 | -0.127 | 0.8992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.41e-18**), Residual SE = **3972.594** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17831.5306** | 1438.4045 | ±2876.8090 | **+12.397** | **2.72e-35** | *** |
| **Education: graduate level (vs college)** | **-1001.9083** | 296.7393 | ±593.4786 | **-3.376** | **7.34e-04** | *** |
| Education: high school or below (vs college) | +866.3589 | 632.3502 | ±1264.7004 | +1.370 | 0.1707 |  |
| Site: UCSD (vs UAB) | -4.1109 | 390.8036 | ±781.6073 | -0.011 | 0.9916 |  |
| Site: UW (vs UAB) | -206.4232 | 367.2695 | ±734.5390 | -0.562 | 0.5741 |  |
| **Age (years)** | **-117.5556** | 14.7665 | ±29.5330 | **-7.961** | **1.71e-15** | *** |
| BMI (kg/m2) | -4.8167 | 24.0243 | ±48.0486 | -0.200 | 0.8411 |  |
| Hypertension | +522.0778 | 344.1729 | ±688.3459 | +1.517 | 0.1293 |  |
| High cholesterol | -189.7497 | 292.0280 | ±584.0559 | -0.650 | 0.5158 |  |
| Kidney disease | -243.0993 | 575.7435 | ±1151.4871 | -0.422 | 0.6729 |  |
| **Circulatory disease** | **-1008.7573** | 428.3430 | ±856.6860 | **-2.355** | **0.0185** | * |
| Avg. daily mean/SD | -28.5461 | 93.4416 | ±186.8831 | -0.305 | 0.7600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **771**, R² = **0.1475**, Adj R² = **0.1351**, F-statistic = **11.93** (p = **7.89e-21**), Residual SE = **3933.467** on **759** df, AIC = **14963.5**, BIC = **15019.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14593.5632** | 1359.1509 | ±2718.3019 | **+10.737** | **6.80e-27** | *** |
| **Education: graduate level (vs college)** | **-999.0177** | 291.8603 | ±583.7206 | **-3.423** | **6.19e-04** | *** |
| Education: high school or below (vs college) | +716.6220 | 635.1659 | ±1270.3318 | +1.128 | 0.2592 |  |
| Site: UCSD (vs UAB) | +30.0858 | 386.8635 | ±773.7270 | +0.078 | 0.9380 |  |
| Site: UW (vs UAB) | -175.9872 | 363.6320 | ±727.2641 | -0.484 | 0.6284 |  |
| **Age (years)** | **-116.7408** | 14.3536 | ±28.7073 | **-8.133** | **4.18e-16** | *** |
| BMI (kg/m2) | -5.9086 | 23.4180 | ±46.8359 | -0.252 | 0.8008 |  |
| Hypertension | +570.0378 | 344.6883 | ±689.3767 | +1.654 | 0.0982 | . |
| High cholesterol | -201.2569 | 289.0770 | ±578.1540 | -0.696 | 0.4863 |  |
| Kidney disease | -320.5200 | 578.6985 | ±1157.3971 | -0.554 | 0.5797 |  |
| **Circulatory disease** | **-943.9558** | 427.6507 | ±855.3014 | **-2.207** | **0.0273** | * |
| **MAG (mg/dL/h)** | **+83.1868** | 22.1221 | ±44.2442 | **+3.760** | **1.70e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **771**, R² = **0.1314**, Adj R² = **0.1188**, F-statistic = **10.44** (p = **5.58e-18**), Residual SE = **3970.266** on **759** df, AIC = **14977.8**, BIC = **15033.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16879.6476** | 1408.8083 | ±2817.6167 | **+11.982** | **4.44e-33** | *** |
| **Education: graduate level (vs college)** | **-1003.7187** | 296.0146 | ±592.0292 | **-3.391** | **6.97e-04** | *** |
| Education: high school or below (vs college) | +845.9686 | 632.3558 | ±1264.7116 | +1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | +11.5295 | 390.6775 | ±781.3550 | +0.030 | 0.9765 |  |
| Site: UW (vs UAB) | -207.5140 | 367.0629 | ±734.1258 | -0.565 | 0.5718 |  |
| **Age (years)** | **-118.1017** | 14.7205 | ±29.4410 | **-8.023** | **1.03e-15** | *** |
| BMI (kg/m2) | -4.0296 | 23.9870 | ±47.9740 | -0.168 | 0.8666 |  |
| Hypertension | +503.4938 | 346.6643 | ±693.3286 | +1.452 | 0.1464 |  |
| High cholesterol | -193.1856 | 291.7775 | ±583.5549 | -0.662 | 0.5079 |  |
| Kidney disease | -269.0876 | 574.2643 | ±1148.5286 | -0.469 | 0.6394 |  |
| **Circulatory disease** | **-1024.5368** | 427.2470 | ±854.4940 | **-2.398** | **0.0165** | * |
| Avg. daily range (mg/dL) | +8.4632 | 8.3724 | ±16.7448 | +1.011 | 0.3121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **771**, R² = **0.1337**, Adj R² = **0.1211**, F-statistic = **10.65** (p = **2.23e-18**), Residual SE = **3965.075** on **759** df, AIC = **14975.8**, BIC = **15031.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17076.8749** | 1236.2965 | ±2472.5929 | **+13.813** | **2.13e-43** | *** |
| **Education: graduate level (vs college)** | **-1006.0308** | 295.1535 | ±590.3069 | **-3.409** | **6.53e-04** | *** |
| Education: high school or below (vs college) | +824.8035 | 625.3992 | ±1250.7983 | +1.319 | 0.1872 |  |
| Site: UCSD (vs UAB) | +29.0789 | 386.7803 | ±773.5605 | +0.075 | 0.9401 |  |
| Site: UW (vs UAB) | -182.7376 | 366.5247 | ±733.0495 | -0.499 | 0.6181 |  |
| **Age (years)** | **-117.0502** | 14.6522 | ±29.3043 | **-7.989** | **1.36e-15** | *** |
| BMI (kg/m2) | -8.3503 | 23.9786 | ±47.9573 | -0.348 | 0.7277 |  |
| Hypertension | +520.8110 | 345.7292 | ±691.4583 | +1.506 | 0.1320 |  |
| High cholesterol | -230.5732 | 292.9403 | ±585.8807 | -0.787 | 0.4312 |  |
| Kidney disease | -288.0180 | 583.8003 | ±1167.6005 | -0.493 | 0.6218 |  |
| **Circulatory disease** | **-1058.3233** | 430.8422 | ±861.6844 | **-2.456** | **0.0140** | * |
| SD of daily means (mg/dL) | +106.8370 | 68.1413 | ±136.2826 | +1.568 | 0.1169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.70e-18**), Residual SE = **3972.786** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17281.4269** | 4824.2241 | ±9648.4481 | **+3.582** | **3.41e-04** | *** |
| **Education: graduate level (vs college)** | **-1006.0870** | 295.9075 | ±591.8150 | **-3.400** | **6.74e-04** | *** |
| Education: high school or below (vs college) | +872.7966 | 632.2352 | ±1264.4703 | +1.380 | 0.1674 |  |
| Site: UCSD (vs UAB) | -11.9035 | 390.0906 | ±780.1813 | -0.031 | 0.9757 |  |
| Site: UW (vs UAB) | -206.9160 | 367.5587 | ±735.1173 | -0.563 | 0.5735 |  |
| **Age (years)** | **-117.2318** | 14.6314 | ±29.2628 | **-8.012** | **1.13e-15** | *** |
| BMI (kg/m2) | -4.6555 | 24.2362 | ±48.4724 | -0.192 | 0.8477 |  |
| Hypertension | +530.7296 | 347.7066 | ±695.4132 | +1.526 | 0.1269 |  |
| High cholesterol | -187.8531 | 293.4749 | ±586.9498 | -0.640 | 0.5221 |  |
| Kidney disease | -232.1184 | 581.7870 | ±1163.5740 | -0.399 | 0.6899 |  |
| **Circulatory disease** | **-1007.7303** | 430.6498 | ±861.2996 | **-2.340** | **0.0193** | * |
| Time in range 70-180, pooled (%) | +3.2874 | 46.8566 | ±93.7131 | +0.070 | 0.9441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.71e-18**), Residual SE = **3972.796** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17809.7059** | 5006.0042 | ±10012.0084 | **+3.558** | **3.74e-04** | *** |
| **Education: graduate level (vs college)** | **-1006.5651** | 296.0100 | ±592.0201 | **-3.400** | **6.73e-04** | *** |
| Education: high school or below (vs college) | +872.6438 | 632.2922 | ±1264.5844 | +1.380 | 0.1675 |  |
| Site: UCSD (vs UAB) | -9.3317 | 390.1811 | ±780.3622 | -0.024 | 0.9809 |  |
| Site: UW (vs UAB) | -206.7768 | 367.5601 | ±735.1203 | -0.563 | 0.5737 |  |
| **Age (years)** | **-117.3141** | 14.6320 | ±29.2641 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -4.8262 | 24.2431 | ±48.4862 | -0.199 | 0.8422 |  |
| Hypertension | +528.3033 | 347.4475 | ±694.8951 | +1.521 | 0.1284 |  |
| High cholesterol | -189.9991 | 293.5637 | ±587.1274 | -0.647 | 0.5175 |  |
| Kidney disease | -238.4461 | 582.0271 | ±1164.0542 | -0.410 | 0.6820 |  |
| **Circulatory disease** | **-1012.7703** | 431.4971 | ±862.9942 | **-2.347** | **0.0189** | * |
| Avg. daily time in range 70-180 (%) | -1.9952 | 48.6250 | ±97.2501 | -0.041 | 0.9673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **771**, R² = **0.1319**, Adj R² = **0.1193**, F-statistic = **10.48** (p = **4.67e-18**), Residual SE = **3969.256** on **759** df, AIC = **14977.4**, BIC = **15033.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17699.3778** | 1228.1322 | ±2456.2644 | **+14.412** | **4.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1034.3858** | 297.0233 | ±594.0466 | **-3.483** | **4.97e-04** | *** |
| Education: high school or below (vs college) | +850.0044 | 629.7035 | ±1259.4071 | +1.350 | 0.1771 |  |
| Site: UCSD (vs UAB) | +5.4817 | 390.8660 | ±781.7319 | +0.014 | 0.9888 |  |
| Site: UW (vs UAB) | -211.6061 | 366.6459 | ±733.2918 | -0.577 | 0.5638 |  |
| **Age (years)** | **-117.1154** | 14.6437 | ±29.2875 | **-7.998** | **1.27e-15** | *** |
| BMI (kg/m2) | -5.3945 | 24.0557 | ±48.1114 | -0.224 | 0.8226 |  |
| Hypertension | +523.7435 | 346.7773 | ±693.5546 | +1.510 | 0.1310 |  |
| High cholesterol | -183.6749 | 291.3118 | ±582.6236 | -0.631 | 0.5284 |  |
| Kidney disease | -255.2149 | 573.1379 | ±1146.2758 | -0.445 | 0.6561 |  |
| **Circulatory disease** | **-1015.1774** | 429.0496 | ±858.0992 | **-2.366** | **0.0180** | * |
| Time 54-69, pooled (%) | -338.2375 | 278.8362 | ±557.6723 | -1.213 | 0.2251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **771**, R² = **0.1325**, Adj R² = **0.1199**, F-statistic = **10.54** (p = **3.63e-18**), Residual SE = **3967.838** on **759** df, AIC = **14976.9**, BIC = **15032.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17698.1285** | 1226.3368 | ±2452.6737 | **+14.432** | **3.27e-47** | *** |
| **Education: graduate level (vs college)** | **-1041.5631** | 296.9051 | ±593.8101 | **-3.508** | **4.51e-04** | *** |
| Education: high school or below (vs college) | +841.1424 | 628.9052 | ±1257.8105 | +1.337 | 0.1811 |  |
| Site: UCSD (vs UAB) | +17.5322 | 391.7386 | ±783.4772 | +0.045 | 0.9643 |  |
| Site: UW (vs UAB) | -209.4153 | 366.7465 | ±733.4929 | -0.571 | 0.5680 |  |
| **Age (years)** | **-116.9488** | 14.6327 | ±29.2654 | **-7.992** | **1.32e-15** | *** |
| BMI (kg/m2) | -5.4617 | 24.0690 | ±48.1381 | -0.227 | 0.8205 |  |
| Hypertension | +522.3078 | 346.7481 | ±693.4962 | +1.506 | 0.1320 |  |
| High cholesterol | -184.0787 | 291.2551 | ±582.5101 | -0.632 | 0.5274 |  |
| Kidney disease | -261.0457 | 572.2711 | ±1144.5423 | -0.456 | 0.6483 |  |
| **Circulatory disease** | **-1022.0227** | 428.8456 | ±857.6911 | **-2.383** | **0.0172** | * |
| Avg. daily time 54-69 (%) | -388.3808 | 264.6760 | ±529.3519 | -1.467 | 0.1423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **771**, R² = **0.1319**, Adj R² = **0.1193**, F-statistic = **10.48** (p = **4.67e-18**), Residual SE = **3969.256** on **759** df, AIC = **14977.4**, BIC = **15033.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17699.3778** | 1228.1322 | ±2456.2644 | **+14.412** | **4.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1034.3858** | 297.0233 | ±594.0466 | **-3.483** | **4.97e-04** | *** |
| Education: high school or below (vs college) | +850.0044 | 629.7035 | ±1259.4071 | +1.350 | 0.1771 |  |
| Site: UCSD (vs UAB) | +5.4817 | 390.8660 | ±781.7319 | +0.014 | 0.9888 |  |
| Site: UW (vs UAB) | -211.6061 | 366.6459 | ±733.2918 | -0.577 | 0.5638 |  |
| **Age (years)** | **-117.1154** | 14.6437 | ±29.2875 | **-7.998** | **1.27e-15** | *** |
| BMI (kg/m2) | -5.3945 | 24.0557 | ±48.1114 | -0.224 | 0.8226 |  |
| Hypertension | +523.7435 | 346.7773 | ±693.5546 | +1.510 | 0.1310 |  |
| High cholesterol | -183.6749 | 291.3118 | ±582.6236 | -0.631 | 0.5284 |  |
| Kidney disease | -255.2149 | 573.1379 | ±1146.2758 | -0.445 | 0.6561 |  |
| **Circulatory disease** | **-1015.1774** | 429.0496 | ±858.0992 | **-2.366** | **0.0180** | * |
| Time < 70 (%) | -338.2375 | 278.8362 | ±557.6723 | -1.213 | 0.2251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **771**, R² = **0.1325**, Adj R² = **0.1199**, F-statistic = **10.54** (p = **3.63e-18**), Residual SE = **3967.838** on **759** df, AIC = **14976.9**, BIC = **15032.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17698.1285** | 1226.3368 | ±2452.6737 | **+14.432** | **3.27e-47** | *** |
| **Education: graduate level (vs college)** | **-1041.5631** | 296.9051 | ±593.8101 | **-3.508** | **4.51e-04** | *** |
| Education: high school or below (vs college) | +841.1424 | 628.9052 | ±1257.8105 | +1.337 | 0.1811 |  |
| Site: UCSD (vs UAB) | +17.5322 | 391.7386 | ±783.4772 | +0.045 | 0.9643 |  |
| Site: UW (vs UAB) | -209.4153 | 366.7465 | ±733.4929 | -0.571 | 0.5680 |  |
| **Age (years)** | **-116.9488** | 14.6327 | ±29.2654 | **-7.992** | **1.32e-15** | *** |
| BMI (kg/m2) | -5.4617 | 24.0690 | ±48.1381 | -0.227 | 0.8205 |  |
| Hypertension | +522.3078 | 346.7481 | ±693.4962 | +1.506 | 0.1320 |  |
| High cholesterol | -184.0787 | 291.2551 | ±582.5101 | -0.632 | 0.5274 |  |
| Kidney disease | -261.0457 | 572.2711 | ±1144.5423 | -0.456 | 0.6483 |  |
| **Circulatory disease** | **-1022.0227** | 428.8456 | ±857.6911 | **-2.383** | **0.0172** | * |
| Avg. daily time < 70 (%) | -388.3808 | 264.6760 | ±529.3519 | -1.467 | 0.1423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.69e-18**), Residual SE = **3972.780** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17610.9161** | 1220.4782 | ±2440.9564 | **+14.430** | **3.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1007.0814** | 295.8880 | ±591.7761 | **-3.404** | **6.65e-04** | *** |
| Education: high school or below (vs college) | +872.0283 | 631.6914 | ±1263.3827 | +1.380 | 0.1674 |  |
| Site: UCSD (vs UAB) | -8.3402 | 390.5150 | ±781.0300 | -0.021 | 0.9830 |  |
| Site: UW (vs UAB) | -206.7881 | 367.4306 | ±734.8612 | -0.563 | 0.5736 |  |
| **Age (years)** | **-117.3421** | 14.6458 | ±29.2917 | **-8.012** | **1.13e-15** | *** |
| BMI (kg/m2) | -4.8877 | 24.2104 | ±48.4208 | -0.202 | 0.8400 |  |
| Hypertension | +527.4277 | 347.9137 | ±695.8273 | +1.516 | 0.1295 |  |
| High cholesterol | -190.6948 | 293.4910 | ±586.9821 | -0.650 | 0.5159 |  |
| Kidney disease | -240.7551 | 581.4883 | ±1162.9766 | -0.414 | 0.6789 |  |
| **Circulatory disease** | **-1014.4408** | 430.3092 | ±860.6183 | **-2.357** | **0.0184** | * |
| Time 181-250, pooled (%) | +3.7978 | 46.5758 | ±93.1516 | +0.082 | 0.9350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.46e-18**), Residual SE = **3972.631** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17613.2951** | 1219.8898 | ±2439.7797 | **+14.438** | **2.97e-47** | *** |
| **Education: graduate level (vs college)** | **-1008.2845** | 296.0144 | ±592.0287 | **-3.406** | **6.59e-04** | *** |
| Education: high school or below (vs college) | +872.1454 | 631.6000 | ±1263.1999 | +1.381 | 0.1673 |  |
| Site: UCSD (vs UAB) | -4.0581 | 390.7121 | ±781.4241 | -0.010 | 0.9917 |  |
| Site: UW (vs UAB) | -206.6028 | 367.4427 | ±734.8855 | -0.562 | 0.5739 |  |
| **Age (years)** | **-117.4402** | 14.6473 | ±29.2945 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -5.1436 | 24.2056 | ±48.4112 | -0.212 | 0.8317 |  |
| Hypertension | +523.9697 | 347.7092 | ±695.4184 | +1.507 | 0.1318 |  |
| High cholesterol | -193.4368 | 293.5701 | ±587.1402 | -0.659 | 0.5100 |  |
| Kidney disease | -250.0058 | 581.5296 | ±1163.0593 | -0.430 | 0.6673 |  |
| **Circulatory disease** | **-1021.8272** | 431.1495 | ±862.2991 | **-2.370** | **0.0178** | * |
| Avg. daily time 181-250 (%) | +10.9431 | 48.3900 | ±96.7800 | +0.226 | 0.8211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.69e-18**), Residual SE = **3972.780** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17610.9161** | 1220.4782 | ±2440.9564 | **+14.430** | **3.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1007.0814** | 295.8880 | ±591.7761 | **-3.404** | **6.65e-04** | *** |
| Education: high school or below (vs college) | +872.0283 | 631.6914 | ±1263.3827 | +1.380 | 0.1674 |  |
| Site: UCSD (vs UAB) | -8.3402 | 390.5150 | ±781.0300 | -0.021 | 0.9830 |  |
| Site: UW (vs UAB) | -206.7881 | 367.4306 | ±734.8612 | -0.563 | 0.5736 |  |
| **Age (years)** | **-117.3421** | 14.6458 | ±29.2917 | **-8.012** | **1.13e-15** | *** |
| BMI (kg/m2) | -4.8877 | 24.2104 | ±48.4208 | -0.202 | 0.8400 |  |
| Hypertension | +527.4277 | 347.9137 | ±695.8273 | +1.516 | 0.1295 |  |
| High cholesterol | -190.6948 | 293.4910 | ±586.9821 | -0.650 | 0.5159 |  |
| Kidney disease | -240.7551 | 581.4883 | ±1162.9766 | -0.414 | 0.6789 |  |
| **Circulatory disease** | **-1014.4408** | 430.3092 | ±860.6183 | **-2.357** | **0.0184** | * |
| Time > 180 (%) | +3.7978 | 46.5758 | ±93.1516 | +0.082 | 0.9350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.46e-18**), Residual SE = **3972.631** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17613.2951** | 1219.8898 | ±2439.7797 | **+14.438** | **2.97e-47** | *** |
| **Education: graduate level (vs college)** | **-1008.2845** | 296.0144 | ±592.0287 | **-3.406** | **6.59e-04** | *** |
| Education: high school or below (vs college) | +872.1454 | 631.6000 | ±1263.1999 | +1.381 | 0.1673 |  |
| Site: UCSD (vs UAB) | -4.0581 | 390.7121 | ±781.4241 | -0.010 | 0.9917 |  |
| Site: UW (vs UAB) | -206.6028 | 367.4427 | ±734.8855 | -0.562 | 0.5739 |  |
| **Age (years)** | **-117.4402** | 14.6473 | ±29.2945 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -5.1436 | 24.2056 | ±48.4112 | -0.212 | 0.8317 |  |
| Hypertension | +523.9697 | 347.7092 | ±695.4184 | +1.507 | 0.1318 |  |
| High cholesterol | -193.4368 | 293.5701 | ±587.1402 | -0.659 | 0.5100 |  |
| Kidney disease | -250.0058 | 581.5296 | ±1163.0593 | -0.430 | 0.6673 |  |
| **Circulatory disease** | **-1021.8272** | 431.1495 | ±862.2991 | **-2.370** | **0.0178** | * |
| Avg. daily time > 180 (%) | +10.9431 | 48.3900 | ±96.7800 | +0.226 | 0.8211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.38e-18**), Residual SE = **3972.576** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17615.9151** | 1220.3691 | ±2440.7381 | **+14.435** | **3.12e-47** | *** |
| **Education: graduate level (vs college)** | **-1005.8770** | 295.7997 | ±591.5995 | **-3.401** | **6.73e-04** | *** |
| Education: high school or below (vs college) | +863.2764 | 631.7881 | ±1263.5763 | +1.366 | 0.1718 |  |
| Site: UCSD (vs UAB) | -3.1566 | 389.6780 | ±779.3559 | -0.008 | 0.9935 |  |
| Site: UW (vs UAB) | -205.6088 | 367.4153 | ±734.8305 | -0.560 | 0.5757 |  |
| **Age (years)** | **-117.1856** | 14.6789 | ±29.3577 | **-7.983** | **1.42e-15** | *** |
| BMI (kg/m2) | -5.5363 | 24.2818 | ±48.5636 | -0.228 | 0.8196 |  |
| Hypertension | +529.9980 | 347.6357 | ±695.2714 | +1.525 | 0.1274 |  |
| High cholesterol | -198.3199 | 295.6271 | ±591.2542 | -0.671 | 0.5023 |  |
| Kidney disease | -247.2590 | 578.3474 | ±1156.6947 | -0.428 | 0.6690 |  |
| **Circulatory disease** | **-1019.8399** | 428.6705 | ±857.3410 | **-2.379** | **0.0174** | * |
| Nocturnal time > 180 (%) | +11.4315 | 45.4388 | ±90.8776 | +0.252 | 0.8014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 771; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **771**, R² = **0.1526**, Adj R² = **0.1414**, F-statistic = **13.68** (p = **2.46e-22**), Residual SE = **12.051** on **760** df, AIC = **6037.2**, BIC = **6088.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6581** | 3.9688 | ±7.9377 | **+11.000** | **3.81e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7257** | 0.9004 | ±1.8007 | **-3.027** | **0.0025** | ** |
| Education: high school or below (vs college) | +2.1540 | 1.9303 | ±3.8606 | +1.116 | 0.2645 |  |
| Site: UCSD (vs UAB) | -0.1785 | 1.1876 | ±2.3752 | -0.150 | 0.8805 |  |
| Site: UW (vs UAB) | -0.5365 | 1.0983 | ±2.1965 | -0.489 | 0.6252 |  |
| **Age (years)** | **-0.3794** | 0.0418 | ±0.0836 | **-9.077** | **1.12e-19** | *** |
| BMI (kg/m2) | +0.1613 | 0.0840 | ±0.1681 | +1.919 | 0.0550 | . |
| Hypertension | +1.1026 | 1.0004 | ±2.0007 | +1.102 | 0.2704 |  |
| High cholesterol | -0.1747 | 0.8817 | ±1.7633 | -0.198 | 0.8429 |  |
| Kidney disease | -0.1166 | 1.7255 | ±3.4509 | -0.068 | 0.9461 |  |
| **Circulatory disease** | **-2.9641** | 1.2665 | ±2.5329 | **-2.340** | **0.0193** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **771**, R² = **0.1598**, Adj R² = **0.1477**, F-statistic = **13.13** (p = **4.38e-23**), Residual SE = **12.007** on **759** df, AIC = **6032.5**, BIC = **6088.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2536** | 7.1982 | ±14.3963 | **+4.064** | **4.82e-05** | *** |
| **Education: graduate level (vs college)** | **-2.7159** | 0.8940 | ±1.7880 | **-3.038** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.0287 | 1.9388 | ±3.8776 | +1.046 | 0.2954 |  |
| Site: UCSD (vs UAB) | -0.1373 | 1.1788 | ±2.3576 | -0.116 | 0.9073 |  |
| Site: UW (vs UAB) | -0.4878 | 1.0948 | ±2.1896 | -0.446 | 0.6559 |  |
| **Age (years)** | **-0.3847** | 0.0413 | ±0.0825 | **-9.326** | **1.09e-20** | *** |
| BMI (kg/m2) | +0.1319 | 0.0809 | ±0.1617 | +1.631 | 0.1029 |  |
| Hypertension | +0.7606 | 1.0088 | ±2.0175 | +0.754 | 0.4508 |  |
| High cholesterol | -0.5764 | 0.8868 | ±1.7736 | -0.650 | 0.5157 |  |
| Kidney disease | +0.0147 | 1.6876 | ±3.3752 | +0.009 | 0.9930 |  |
| **Circulatory disease** | **-3.2017** | 1.2583 | ±2.5166 | **-2.545** | **0.0109** | * |
| **HbA1c (%)** | **+2.8088** | 1.1499 | ±2.2999 | **+2.443** | **0.0146** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **771**, R² = **0.1545**, Adj R² = **0.1422**, F-statistic = **12.60** (p = **4.24e-22**), Residual SE = **12.045** on **759** df, AIC = **6037.4**, BIC = **6093.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.3211** | 5.7068 | ±11.4136 | **+6.715** | **1.88e-11** | *** |
| **Education: graduate level (vs college)** | **-2.7462** | 0.9007 | ±1.8014 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1780 | 1.9244 | ±3.8488 | +1.132 | 0.2577 |  |
| Site: UCSD (vs UAB) | -0.1241 | 1.1866 | ±2.3733 | -0.105 | 0.9167 |  |
| Site: UW (vs UAB) | -0.5842 | 1.0977 | ±2.1953 | -0.532 | 0.5946 |  |
| **Age (years)** | **-0.3804** | 0.0417 | ±0.0833 | **-9.132** | **6.74e-20** | *** |
| BMI (kg/m2) | +0.1507 | 0.0839 | ±0.1679 | +1.796 | 0.0725 | . |
| Hypertension | +0.9742 | 1.0013 | ±2.0025 | +0.973 | 0.3306 |  |
| High cholesterol | -0.2272 | 0.8809 | ±1.7618 | -0.258 | 0.7965 |  |
| Kidney disease | -0.2737 | 1.7176 | ±3.4352 | -0.159 | 0.8734 |  |
| **Circulatory disease** | **-3.0762** | 1.2759 | ±2.5517 | **-2.411** | **0.0159** | * |
| Mean glucose (mg/dL) | +0.0482 | 0.0372 | ±0.0744 | +1.295 | 0.1952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **771**, R² = **0.1545**, Adj R² = **0.1422**, F-statistic = **12.60** (p = **4.24e-22**), Residual SE = **12.045** on **759** df, AIC = **6037.4**, BIC = **6093.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6510** | 10.0800 | ±20.1601 | **+3.140** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-2.7462** | 0.9007 | ±1.8014 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1780 | 1.9244 | ±3.8488 | +1.132 | 0.2577 |  |
| Site: UCSD (vs UAB) | -0.1241 | 1.1866 | ±2.3733 | -0.105 | 0.9167 |  |
| Site: UW (vs UAB) | -0.5842 | 1.0977 | ±2.1953 | -0.532 | 0.5946 |  |
| **Age (years)** | **-0.3804** | 0.0417 | ±0.0833 | **-9.132** | **6.74e-20** | *** |
| BMI (kg/m2) | +0.1507 | 0.0839 | ±0.1679 | +1.796 | 0.0725 | . |
| Hypertension | +0.9742 | 1.0013 | ±2.0025 | +0.973 | 0.3306 |  |
| High cholesterol | -0.2272 | 0.8809 | ±1.7618 | -0.258 | 0.7965 |  |
| Kidney disease | -0.2737 | 1.7176 | ±3.4352 | -0.159 | 0.8734 |  |
| **Circulatory disease** | **-3.0762** | 1.2759 | ±2.5517 | **-2.411** | **0.0159** | * |
| GMI (%) | +2.0151 | 1.5556 | ±3.1111 | +1.295 | 0.1952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **771**, R² = **0.1543**, Adj R² = **0.1421**, F-statistic = **12.59** (p = **4.48e-22**), Residual SE = **12.046** on **759** df, AIC = **6037.5**, BIC = **6093.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.0816** | 5.2305 | ±10.4609 | **+7.472** | **7.90e-14** | *** |
| **Education: graduate level (vs college)** | **-2.7381** | 0.9004 | ±1.8008 | **-3.041** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.1433 | 1.9228 | ±3.8457 | +1.115 | 0.2650 |  |
| Site: UCSD (vs UAB) | -0.1801 | 1.1885 | ±2.3770 | -0.152 | 0.8796 |  |
| Site: UW (vs UAB) | -0.6009 | 1.0974 | ±2.1947 | -0.548 | 0.5840 |  |
| **Age (years)** | **-0.3763** | 0.0418 | ±0.0836 | **-9.003** | **2.19e-19** | *** |
| BMI (kg/m2) | +0.1449 | 0.0847 | ±0.1694 | +1.710 | 0.0873 | . |
| Hypertension | +1.0128 | 0.9955 | ±1.9910 | +1.017 | 0.3090 |  |
| High cholesterol | -0.2576 | 0.8822 | ±1.7644 | -0.292 | 0.7703 |  |
| Kidney disease | -0.1662 | 1.7098 | ±3.4196 | -0.097 | 0.9226 |  |
| **Circulatory disease** | **-3.0596** | 1.2720 | ±2.5441 | **-2.405** | **0.0162** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0414 | 0.0335 | ±0.0671 | +1.234 | 0.2170 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1545**, Adj R² = **0.1422**, F-statistic = **12.61** (p = **4.23e-22**), Residual SE = **12.045** on **759** df, AIC = **6037.4**, BIC = **6093.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.2391** | 4.4162 | ±8.8323 | **+9.338** | **9.80e-21** | *** |
| **Education: graduate level (vs college)** | **-2.6818** | 0.9018 | ±1.8036 | **-2.974** | **0.0029** | ** |
| Education: high school or below (vs college) | +2.0639 | 1.9246 | ±3.8492 | +1.072 | 0.2835 |  |
| Site: UCSD (vs UAB) | -0.0608 | 1.1873 | ±2.3745 | -0.051 | 0.9592 |  |
| Site: UW (vs UAB) | -0.5211 | 1.0977 | ±2.1953 | -0.475 | 0.6350 |  |
| **Age (years)** | **-0.3828** | 0.0418 | ±0.0836 | **-9.160** | **5.21e-20** | *** |
| BMI (kg/m2) | +0.1573 | 0.0829 | ±0.1658 | +1.897 | 0.0578 | . |
| Hypertension | +0.9344 | 1.0025 | ±2.0051 | +0.932 | 0.3513 |  |
| High cholesterol | -0.2188 | 0.8807 | ±1.7613 | -0.248 | 0.8038 |  |
| Kidney disease | -0.2882 | 1.7280 | ±3.4561 | -0.167 | 0.8675 |  |
| **Circulatory disease** | **-3.0356** | 1.2685 | ±2.5369 | **-2.393** | **0.0167** | * |
| Glucose SD, pooled (mg/dL) | +0.1412 | 0.1077 | ±0.2155 | +1.310 | 0.1901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1542**, Adj R² = **0.1419**, F-statistic = **12.58** (p = **4.81e-22**), Residual SE = **12.047** on **759** df, AIC = **6037.7**, BIC = **6093.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.6266** | 4.3430 | ±8.6860 | **+9.585** | **9.27e-22** | *** |
| **Education: graduate level (vs college)** | **-2.6989** | 0.9015 | ±1.8029 | **-2.994** | **0.0028** | ** |
| Education: high school or below (vs college) | +2.0886 | 1.9263 | ±3.8526 | +1.084 | 0.2782 |  |
| Site: UCSD (vs UAB) | -0.0734 | 1.1872 | ±2.3744 | -0.062 | 0.9507 |  |
| Site: UW (vs UAB) | -0.5363 | 1.0980 | ±2.1959 | -0.488 | 0.6252 |  |
| **Age (years)** | **-0.3828** | 0.0419 | ±0.0837 | **-9.143** | **6.07e-20** | *** |
| BMI (kg/m2) | +0.1573 | 0.0829 | ±0.1659 | +1.896 | 0.0579 | . |
| Hypertension | +0.9475 | 1.0017 | ±2.0034 | +0.946 | 0.3442 |  |
| High cholesterol | -0.2060 | 0.8814 | ±1.7627 | -0.234 | 0.8152 |  |
| Kidney disease | -0.2541 | 1.7230 | ±3.4459 | -0.147 | 0.8828 |  |
| **Circulatory disease** | **-3.0169** | 1.2688 | ±2.5376 | **-2.378** | **0.0174** | * |
| Avg. daily SD (mg/dL) | +0.1323 | 0.1101 | ±0.2203 | +1.201 | 0.2297 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **771**, R² = **0.1529**, Adj R² = **0.1406**, F-statistic = **12.45** (p = **8.31e-22**), Residual SE = **12.057** on **759** df, AIC = **6038.9**, BIC = **6094.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.4369** | 4.6752 | ±9.3503 | **+9.077** | **1.12e-19** | *** |
| **Education: graduate level (vs college)** | **-2.6979** | 0.9049 | ±1.8097 | **-2.982** | **0.0029** | ** |
| Education: high school or below (vs college) | +2.1084 | 1.9357 | ±3.8714 | +1.089 | 0.2761 |  |
| Site: UCSD (vs UAB) | -0.1357 | 1.1894 | ±2.3789 | -0.114 | 0.9092 |  |
| Site: UW (vs UAB) | -0.5199 | 1.1003 | ±2.2005 | -0.473 | 0.6365 |  |
| **Age (years)** | **-0.3808** | 0.0420 | ±0.0839 | **-9.072** | **1.17e-19** | *** |
| BMI (kg/m2) | +0.1618 | 0.0840 | ±0.1680 | +1.927 | 0.0540 | . |
| Hypertension | +1.0528 | 1.0027 | ±2.0054 | +1.050 | 0.2937 |  |
| High cholesterol | -0.1806 | 0.8822 | ±1.7644 | -0.205 | 0.8378 |  |
| Kidney disease | -0.1602 | 1.7301 | ±3.4601 | -0.093 | 0.9262 |  |
| **Circulatory disease** | **-2.9684** | 1.2665 | ±2.5331 | **-2.344** | **0.0191** | * |
| CV (%) | +0.0782 | 0.1464 | ±0.2928 | +0.534 | 0.5932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.55e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.3921** | 4.5900 | ±9.1801 | **+9.889** | **4.63e-23** | *** |
| **Education: graduate level (vs college)** | **-2.6828** | 0.9042 | ±1.8085 | **-2.967** | **0.0030** | ** |
| Education: high school or below (vs college) | +2.0993 | 1.9317 | ±3.8634 | +1.087 | 0.2772 |  |
| Site: UCSD (vs UAB) | -0.1292 | 1.1884 | ±2.3767 | -0.109 | 0.9134 |  |
| Site: UW (vs UAB) | -0.5247 | 1.0994 | ±2.1988 | -0.477 | 0.6332 |  |
| **Age (years)** | **-0.3811** | 0.0420 | ±0.0840 | **-9.078** | **1.10e-19** | *** |
| BMI (kg/m2) | +0.1617 | 0.0839 | ±0.1677 | +1.928 | 0.0539 | . |
| Hypertension | +1.0415 | 1.0008 | ±2.0015 | +1.041 | 0.2980 |  |
| High cholesterol | -0.1814 | 0.8823 | ±1.7646 | -0.206 | 0.8371 |  |
| Kidney disease | -0.1729 | 1.7289 | ±3.4578 | -0.100 | 0.9203 |  |
| **Circulatory disease** | **-2.9601** | 1.2657 | ±2.5314 | **-2.339** | **0.0194** | * |
| Mean / SD ratio | -0.2616 | 0.3642 | ±0.7285 | -0.718 | 0.4726 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1532**, Adj R² = **0.1409**, F-statistic = **12.48** (p = **7.27e-22**), Residual SE = **12.054** on **759** df, AIC = **6038.6**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.4332** | 4.5251 | ±9.0502 | **+10.040** | **1.01e-23** | *** |
| **Education: graduate level (vs college)** | **-2.6897** | 0.9036 | ±1.8072 | **-2.977** | **0.0029** | ** |
| Education: high school or below (vs college) | +2.1043 | 1.9309 | ±3.8618 | +1.090 | 0.2758 |  |
| Site: UCSD (vs UAB) | -0.1286 | 1.1869 | ±2.3738 | -0.108 | 0.9137 |  |
| Site: UW (vs UAB) | -0.5333 | 1.0988 | ±2.1975 | -0.485 | 0.6274 |  |
| **Age (years)** | **-0.3816** | 0.0421 | ±0.0842 | **-9.070** | **1.19e-19** | *** |
| BMI (kg/m2) | +0.1608 | 0.0837 | ±0.1674 | +1.921 | 0.0547 | . |
| Hypertension | +1.0453 | 0.9990 | ±1.9979 | +1.046 | 0.2954 |  |
| High cholesterol | -0.1791 | 0.8826 | ±1.7651 | -0.203 | 0.8392 |  |
| Kidney disease | -0.1733 | 1.7261 | ±3.4522 | -0.100 | 0.9200 |  |
| **Circulatory disease** | **-2.9475** | 1.2654 | ±2.5308 | **-2.329** | **0.0198** | * |
| Avg. daily mean/SD | -0.2288 | 0.2888 | ±0.5777 | -0.792 | 0.4283 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **771**, R² = **0.1725**, Adj R² = **0.1605**, F-statistic = **14.38** (p = **1.95e-25**), Residual SE = **11.916** on **759** df, AIC = **6020.8**, BIC = **6076.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.6576** | 4.1993 | ±8.3986 | **+8.015** | **1.10e-15** | *** |
| **Education: graduate level (vs college)** | **-2.7013** | 0.8889 | ±1.7778 | **-3.039** | **0.0024** | ** |
| Education: high school or below (vs college) | +1.6370 | 1.9209 | ±3.8419 | +0.852 | 0.3941 |  |
| Site: UCSD (vs UAB) | -0.0445 | 1.1736 | ±2.3471 | -0.038 | 0.9698 |  |
| Site: UW (vs UAB) | -0.4343 | 1.0796 | ±2.1592 | -0.402 | 0.6875 |  |
| **Age (years)** | **-0.3776** | 0.0410 | ±0.0820 | **-9.216** | **3.08e-20** | *** |
| BMI (kg/m2) | +0.1575 | 0.0810 | ±0.1621 | +1.943 | 0.0520 | . |
| Hypertension | +1.2379 | 0.9878 | ±1.9757 | +1.253 | 0.2101 |  |
| High cholesterol | -0.2147 | 0.8727 | ±1.7453 | -0.246 | 0.8057 |  |
| Kidney disease | -0.3967 | 1.7374 | ±3.4747 | -0.228 | 0.8194 |  |
| **Circulatory disease** | **-2.7424** | 1.2541 | ±2.5082 | **-2.187** | **0.0288** | * |
| **MAG (mg/dL/h)** | **+0.2758** | 0.0646 | ±0.1292 | **+4.269** | **1.96e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **771**, R² = **0.1565**, Adj R² = **0.1443**, F-statistic = **12.80** (p = **1.80e-22**), Residual SE = **12.031** on **759** df, AIC = **6035.6**, BIC = **6091.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.4304** | 4.6890 | ±9.3780 | **+8.409** | **4.13e-17** | *** |
| **Education: graduate level (vs college)** | **-2.7102** | 0.8996 | ±1.7992 | **-3.013** | **0.0026** | ** |
| Education: high school or below (vs college) | +2.0001 | 1.9303 | ±3.8606 | +1.036 | 0.3001 |  |
| Site: UCSD (vs UAB) | -0.0519 | 1.1840 | ±2.3681 | -0.044 | 0.9650 |  |
| Site: UW (vs UAB) | -0.5405 | 1.0975 | ±2.1950 | -0.492 | 0.6224 |  |
| **Age (years)** | **-0.3842** | 0.0417 | ±0.0834 | **-9.209** | **3.28e-20** | *** |
| **BMI (kg/m2)** | **+0.1655** | 0.0835 | ±0.1670 | **+1.982** | **0.0474** | * |
| Hypertension | +0.9537 | 1.0026 | ±2.0053 | +0.951 | 0.3415 |  |
| High cholesterol | -0.1978 | 0.8807 | ±1.7615 | -0.225 | 0.8223 |  |
| Kidney disease | -0.3079 | 1.7159 | ±3.4319 | -0.179 | 0.8576 |  |
| **Circulatory disease** | **-3.0435** | 1.2636 | ±2.5271 | **-2.409** | **0.0160** | * |
| Avg. daily range (mg/dL) | +0.0490 | 0.0266 | ±0.0532 | +1.840 | 0.0657 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **771**, R² = **0.1560**, Adj R² = **0.1438**, F-statistic = **12.76** (p = **2.18e-22**), Residual SE = **12.034** on **759** df, AIC = **6036.0**, BIC = **6091.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9934** | 4.0303 | ±8.0606 | **+10.419** | **2.02e-25** | *** |
| **Education: graduate level (vs college)** | **-2.7246** | 0.8991 | ±1.7982 | **-3.030** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.0049 | 1.9060 | ±3.8121 | +1.052 | 0.2929 |  |
| Site: UCSD (vs UAB) | -0.0554 | 1.1776 | ±2.3552 | -0.047 | 0.9625 |  |
| Site: UW (vs UAB) | -0.4613 | 1.0954 | ±2.1909 | -0.421 | 0.6737 |  |
| **Age (years)** | **-0.3787** | 0.0418 | ±0.0835 | **-9.068** | **1.21e-19** | *** |
| BMI (kg/m2) | +0.1501 | 0.0833 | ±0.1667 | +1.800 | 0.0718 | . |
| Hypertension | +1.0763 | 0.9976 | ±1.9951 | +1.079 | 0.2806 |  |
| High cholesterol | -0.3039 | 0.8798 | ±1.7596 | -0.345 | 0.7298 |  |
| Kidney disease | -0.2789 | 1.7451 | ±3.4901 | -0.160 | 0.8730 |  |
| **Circulatory disease** | **-3.1124** | 1.2693 | ±2.5386 | **-2.452** | **0.0142** | * |
| SD of daily means (mg/dL) | +0.3336 | 0.2003 | ±0.4006 | +1.665 | 0.0959 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **771**, R² = **0.1528**, Adj R² = **0.1406**, F-statistic = **12.45** (p = **8.37e-22**), Residual SE = **12.057** on **759** df, AIC = **6038.9**, BIC = **6094.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0799** | 13.1700 | ±26.3399 | **+3.803** | **1.43e-04** | *** |
| **Education: graduate level (vs college)** | **-2.7319** | 0.9005 | ±1.8010 | **-3.034** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.1493 | 1.9308 | ±3.8617 | +1.113 | 0.2657 |  |
| Site: UCSD (vs UAB) | -0.1478 | 1.1893 | ±2.3785 | -0.124 | 0.9011 |  |
| Site: UW (vs UAB) | -0.5349 | 1.0990 | ±2.1980 | -0.487 | 0.6265 |  |
| **Age (years)** | **-0.3805** | 0.0417 | ±0.0834 | **-9.125** | **7.20e-20** | *** |
| BMI (kg/m2) | +0.1592 | 0.0839 | ±0.1678 | +1.898 | 0.0577 | . |
| Hypertension | +1.0732 | 1.0030 | ±2.0060 | +1.070 | 0.2846 |  |
| High cholesterol | -0.2010 | 0.8832 | ±1.7664 | -0.228 | 0.8199 |  |
| Kidney disease | -0.1929 | 1.7366 | ±3.4732 | -0.111 | 0.9115 |  |
| **Circulatory disease** | **-3.0245** | 1.2808 | ±2.5616 | **-2.361** | **0.0182** | * |
| Time in range 70-180, pooled (%) | -0.0642 | 0.1282 | ±0.2563 | -0.501 | 0.6162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.58e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5997** | 13.6074 | ±27.2148 | **+3.866** | **1.11e-04** | *** |
| **Education: graduate level (vs college)** | **-2.7330** | 0.9005 | ±1.8009 | **-3.035** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.1578 | 1.9304 | ±3.8608 | +1.118 | 0.2637 |  |
| Site: UCSD (vs UAB) | -0.1337 | 1.1893 | ±2.3785 | -0.112 | 0.9105 |  |
| Site: UW (vs UAB) | -0.5341 | 1.0988 | ±2.1976 | -0.486 | 0.6269 |  |
| **Age (years)** | **-0.3808** | 0.0417 | ±0.0834 | **-9.133** | **6.68e-20** | *** |
| BMI (kg/m2) | +0.1583 | 0.0838 | ±0.1676 | +1.889 | 0.0589 | . |
| Hypertension | +1.0613 | 1.0027 | ±2.0055 | +1.058 | 0.2899 |  |
| High cholesterol | -0.2105 | 0.8833 | ±1.7665 | -0.238 | 0.8117 |  |
| Kidney disease | -0.2250 | 1.7349 | ±3.4698 | -0.130 | 0.8968 |  |
| **Circulatory disease** | **-3.0514** | 1.2819 | ±2.5638 | **-2.380** | **0.0173** | * |
| Avg. daily time in range 70-180 (%) | -0.0894 | 0.1323 | ±0.2646 | -0.675 | 0.4995 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **771**, R² = **0.1548**, Adj R² = **0.1426**, F-statistic = **12.64** (p = **3.63e-22**), Residual SE = **12.043** on **759** df, AIC = **6037.1**, BIC = **6092.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9901** | 3.9806 | ±7.9612 | **+11.051** | **2.16e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8298** | 0.9075 | ±1.8149 | **-3.118** | **0.0018** | ** |
| Education: high school or below (vs college) | +2.0701 | 1.9268 | ±3.8536 | +1.074 | 0.2826 |  |
| Site: UCSD (vs UAB) | -0.1197 | 1.1891 | ±2.3781 | -0.101 | 0.9198 |  |
| Site: UW (vs UAB) | -0.5543 | 1.0975 | ±2.1949 | -0.505 | 0.6135 |  |
| **Age (years)** | **-0.3788** | 0.0418 | ±0.0836 | **-9.062** | **1.28e-19** | *** |
| BMI (kg/m2) | +0.1589 | 0.0842 | ±0.1684 | +1.887 | 0.0591 | . |
| Hypertension | +1.0822 | 0.9994 | ±1.9987 | +1.083 | 0.2788 |  |
| High cholesterol | -0.1542 | 0.8806 | ±1.7612 | -0.175 | 0.8610 |  |
| Kidney disease | -0.1879 | 1.7222 | ±3.4443 | -0.109 | 0.9131 |  |
| **Circulatory disease** | **-2.9803** | 1.2684 | ±2.5367 | **-2.350** | **0.0188** | * |
| Time 54-69, pooled (%) | -1.2573 | 0.6545 | ±1.3089 | -1.921 | 0.0547 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **771**, R² = **0.1555**, Adj R² = **0.1432**, F-statistic = **12.70** (p = **2.79e-22**), Residual SE = **12.038** on **759** df, AIC = **6036.5**, BIC = **6092.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9709** | 3.9776 | ±7.9551 | **+11.055** | **2.08e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8506** | 0.9076 | ±1.8153 | **-3.141** | **0.0017** | ** |
| Education: high school or below (vs college) | +2.0424 | 1.9251 | ±3.8501 | +1.061 | 0.2887 |  |
| Site: UCSD (vs UAB) | -0.0795 | 1.1896 | ±2.3793 | -0.067 | 0.9467 |  |
| Site: UW (vs UAB) | -0.5457 | 1.0975 | ±2.1950 | -0.497 | 0.6190 |  |
| **Age (years)** | **-0.3782** | 0.0418 | ±0.0836 | **-9.051** | **1.42e-19** | *** |
| BMI (kg/m2) | +0.1588 | 0.0843 | ±0.1685 | +1.884 | 0.0596 | . |
| Hypertension | +1.0780 | 0.9992 | ±1.9983 | +1.079 | 0.2806 |  |
| High cholesterol | -0.1565 | 0.8804 | ±1.7608 | -0.178 | 0.8589 |  |
| Kidney disease | -0.2054 | 1.7186 | ±3.4372 | -0.120 | 0.9049 |  |
| **Circulatory disease** | **-3.0039** | 1.2687 | ±2.5374 | **-2.368** | **0.0179** | * |
| **Avg. daily time 54-69 (%)** | **-1.3795** | 0.6041 | ±1.2081 | **-2.284** | **0.0224** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **771**, R² = **0.1548**, Adj R² = **0.1426**, F-statistic = **12.64** (p = **3.63e-22**), Residual SE = **12.043** on **759** df, AIC = **6037.1**, BIC = **6092.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9901** | 3.9806 | ±7.9612 | **+11.051** | **2.16e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8298** | 0.9075 | ±1.8149 | **-3.118** | **0.0018** | ** |
| Education: high school or below (vs college) | +2.0701 | 1.9268 | ±3.8536 | +1.074 | 0.2826 |  |
| Site: UCSD (vs UAB) | -0.1197 | 1.1891 | ±2.3781 | -0.101 | 0.9198 |  |
| Site: UW (vs UAB) | -0.5543 | 1.0975 | ±2.1949 | -0.505 | 0.6135 |  |
| **Age (years)** | **-0.3788** | 0.0418 | ±0.0836 | **-9.062** | **1.28e-19** | *** |
| BMI (kg/m2) | +0.1589 | 0.0842 | ±0.1684 | +1.887 | 0.0591 | . |
| Hypertension | +1.0822 | 0.9994 | ±1.9987 | +1.083 | 0.2788 |  |
| High cholesterol | -0.1542 | 0.8806 | ±1.7612 | -0.175 | 0.8610 |  |
| Kidney disease | -0.1879 | 1.7222 | ±3.4443 | -0.109 | 0.9131 |  |
| **Circulatory disease** | **-2.9803** | 1.2684 | ±2.5367 | **-2.350** | **0.0188** | * |
| Time < 70 (%) | -1.2573 | 0.6545 | ±1.3089 | -1.921 | 0.0547 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **771**, R² = **0.1555**, Adj R² = **0.1432**, F-statistic = **12.70** (p = **2.79e-22**), Residual SE = **12.038** on **759** df, AIC = **6036.5**, BIC = **6092.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9709** | 3.9776 | ±7.9551 | **+11.055** | **2.08e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8506** | 0.9076 | ±1.8153 | **-3.141** | **0.0017** | ** |
| Education: high school or below (vs college) | +2.0424 | 1.9251 | ±3.8501 | +1.061 | 0.2887 |  |
| Site: UCSD (vs UAB) | -0.0795 | 1.1896 | ±2.3793 | -0.067 | 0.9467 |  |
| Site: UW (vs UAB) | -0.5457 | 1.0975 | ±2.1950 | -0.497 | 0.6190 |  |
| **Age (years)** | **-0.3782** | 0.0418 | ±0.0836 | **-9.051** | **1.42e-19** | *** |
| BMI (kg/m2) | +0.1588 | 0.0843 | ±0.1685 | +1.884 | 0.0596 | . |
| Hypertension | +1.0780 | 0.9992 | ±1.9983 | +1.079 | 0.2806 |  |
| High cholesterol | -0.1565 | 0.8804 | ±1.7608 | -0.178 | 0.8589 |  |
| Kidney disease | -0.2054 | 1.7186 | ±3.4372 | -0.120 | 0.9049 |  |
| **Circulatory disease** | **-3.0039** | 1.2687 | ±2.5374 | **-2.368** | **0.0179** | * |
| **Avg. daily time < 70 (%)** | **-1.3795** | 0.6041 | ±1.2081 | **-2.284** | **0.0224** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.47e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6785** | 3.9595 | ±7.9190 | **+11.031** | **2.70e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7417** | 0.9000 | ±1.8000 | **-3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1415 | 1.9296 | ±3.8592 | +1.110 | 0.2671 |  |
| Site: UCSD (vs UAB) | -0.1315 | 1.1897 | ±2.3794 | -0.111 | 0.9120 |  |
| Site: UW (vs UAB) | -0.5355 | 1.0987 | ±2.1974 | -0.487 | 0.6260 |  |
| **Age (years)** | **-0.3808** | 0.0417 | ±0.0834 | **-9.133** | **6.66e-20** | *** |
| BMI (kg/m2) | +0.1583 | 0.0838 | ±0.1675 | +1.889 | 0.0589 | . |
| Hypertension | +1.0602 | 1.0034 | ±2.0069 | +1.057 | 0.2907 |  |
| High cholesterol | -0.2099 | 0.8831 | ±1.7662 | -0.238 | 0.8121 |  |
| Kidney disease | -0.2280 | 1.7353 | ±3.4705 | -0.131 | 0.8955 |  |
| **Circulatory disease** | **-3.0493** | 1.2810 | ±2.5619 | **-2.380** | **0.0173** | * |
| Time 181-250, pooled (%) | +0.0895 | 0.1276 | ±0.2553 | +0.701 | 0.4834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **771**, R² = **0.1535**, Adj R² = **0.1412**, F-statistic = **12.51** (p = **6.33e-22**), Residual SE = **12.052** on **759** df, AIC = **6038.3**, BIC = **6094.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6936** | 3.9539 | ±7.9077 | **+11.051** | **2.17e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7463** | 0.8998 | ±1.7997 | **-3.052** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1494 | 1.9286 | ±3.8571 | +1.115 | 0.2651 |  |
| Site: UCSD (vs UAB) | -0.1098 | 1.1897 | ±2.3794 | -0.092 | 0.9265 |  |
| Site: UW (vs UAB) | -0.5340 | 1.0985 | ±2.1970 | -0.486 | 0.6269 |  |
| **Age (years)** | **-0.3812** | 0.0417 | ±0.0834 | **-9.142** | **6.14e-20** | *** |
| BMI (kg/m2) | +0.1571 | 0.0836 | ±0.1673 | +1.878 | 0.0604 | . |
| Hypertension | +1.0450 | 1.0032 | ±2.0065 | +1.042 | 0.2976 |  |
| High cholesterol | -0.2211 | 0.8830 | ±1.7660 | -0.250 | 0.8023 |  |
| Kidney disease | -0.2697 | 1.7327 | ±3.4653 | -0.156 | 0.8763 |  |
| **Circulatory disease** | **-3.0846** | 1.2824 | ±2.5648 | **-2.405** | **0.0162** | * |
| Avg. daily time 181-250 (%) | +0.1198 | 0.1318 | ±0.2636 | +0.909 | 0.3632 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.47e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6785** | 3.9595 | ±7.9190 | **+11.031** | **2.70e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7417** | 0.9000 | ±1.8000 | **-3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1415 | 1.9296 | ±3.8592 | +1.110 | 0.2671 |  |
| Site: UCSD (vs UAB) | -0.1315 | 1.1897 | ±2.3794 | -0.111 | 0.9120 |  |
| Site: UW (vs UAB) | -0.5355 | 1.0987 | ±2.1974 | -0.487 | 0.6260 |  |
| **Age (years)** | **-0.3808** | 0.0417 | ±0.0834 | **-9.133** | **6.66e-20** | *** |
| BMI (kg/m2) | +0.1583 | 0.0838 | ±0.1675 | +1.889 | 0.0589 | . |
| Hypertension | +1.0602 | 1.0034 | ±2.0069 | +1.057 | 0.2907 |  |
| High cholesterol | -0.2099 | 0.8831 | ±1.7662 | -0.238 | 0.8121 |  |
| Kidney disease | -0.2280 | 1.7353 | ±3.4705 | -0.131 | 0.8955 |  |
| **Circulatory disease** | **-3.0493** | 1.2810 | ±2.5619 | **-2.380** | **0.0173** | * |
| Time > 180 (%) | +0.0895 | 0.1276 | ±0.2553 | +0.701 | 0.4834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1535**, Adj R² = **0.1412**, F-statistic = **12.51** (p = **6.33e-22**), Residual SE = **12.052** on **759** df, AIC = **6038.3**, BIC = **6094.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6936** | 3.9539 | ±7.9077 | **+11.051** | **2.17e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7463** | 0.8998 | ±1.7997 | **-3.052** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1494 | 1.9286 | ±3.8571 | +1.115 | 0.2651 |  |
| Site: UCSD (vs UAB) | -0.1098 | 1.1897 | ±2.3794 | -0.092 | 0.9265 |  |
| Site: UW (vs UAB) | -0.5340 | 1.0985 | ±2.1970 | -0.486 | 0.6269 |  |
| **Age (years)** | **-0.3812** | 0.0417 | ±0.0834 | **-9.142** | **6.14e-20** | *** |
| BMI (kg/m2) | +0.1571 | 0.0836 | ±0.1673 | +1.878 | 0.0604 | . |
| Hypertension | +1.0450 | 1.0032 | ±2.0065 | +1.042 | 0.2976 |  |
| High cholesterol | -0.2211 | 0.8830 | ±1.7660 | -0.250 | 0.8023 |  |
| Kidney disease | -0.2697 | 1.7327 | ±3.4653 | -0.156 | 0.8763 |  |
| **Circulatory disease** | **-3.0846** | 1.2824 | ±2.5648 | **-2.405** | **0.0162** | * |
| Avg. daily time > 180 (%) | +0.1198 | 0.1318 | ±0.2636 | +0.909 | 0.3632 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.52e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7000** | 3.9621 | ±7.9243 | **+11.029** | **2.76e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7220** | 0.9007 | ±1.8013 | **-3.022** | **0.0025** | ** |
| Education: high school or below (vs college) | +2.0876 | 1.9356 | ±3.8711 | +1.079 | 0.2808 |  |
| Site: UCSD (vs UAB) | -0.1271 | 1.1869 | ±2.3739 | -0.107 | 0.9147 |  |
| Site: UW (vs UAB) | -0.5278 | 1.0980 | ±2.1960 | -0.481 | 0.6307 |  |
| **Age (years)** | **-0.3787** | 0.0419 | ±0.0838 | **-9.039** | **1.58e-19** | *** |
| BMI (kg/m2) | +0.1557 | 0.0845 | ±0.1690 | +1.843 | 0.0653 | . |
| Hypertension | +1.1081 | 1.0032 | ±2.0063 | +1.105 | 0.2693 |  |
| High cholesterol | -0.2399 | 0.8860 | ±1.7720 | -0.271 | 0.7865 |  |
| Kidney disease | -0.1969 | 1.7254 | ±3.4508 | -0.114 | 0.9091 |  |
| **Circulatory disease** | **-3.0286** | 1.2738 | ±2.5475 | **-2.378** | **0.0174** | * |
| Nocturnal time > 180 (%) | +0.0818 | 0.1329 | ±0.2657 | +0.615 | 0.5383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 774; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **774**, R² = **0.1846**, Adj R² = **0.1739**, F-statistic = **17.28** (p = **1.67e-28**), Residual SE = **7.747** on **763** df, AIC = **5376.6**, BIC = **5427.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5124** | 2.8548 | ±5.7095 | **+21.898** | **2.73e-106** | *** |
| **Education: graduate level (vs college)** | **-2.2952** | 0.6151 | ±1.2303 | **-3.731** | **1.91e-04** | *** |
| Education: high school or below (vs college) | -1.7599 | 0.9955 | ±1.9910 | -1.768 | 0.0771 | . |
| **Site: UCSD (vs UAB)** | **-1.6295** | 0.7479 | ±1.4958 | **-2.179** | **0.0293** | * |
| **Site: UW (vs UAB)** | **-1.8219** | 0.7189 | ±1.4378 | **-2.534** | **0.0113** | * |
| **Age (years)** | **-0.1506** | 0.0295 | ±0.0590 | **-5.107** | **3.27e-07** | *** |
| **BMI (kg/m2)** | **+0.3064** | 0.0552 | ±0.1104 | **+5.552** | **2.83e-08** | *** |
| **Hypertension** | **+1.7532** | 0.6636 | ±1.3272 | **+2.642** | **0.0082** | ** |
| High cholesterol | +0.0066 | 0.5805 | ±1.1611 | +0.011 | 0.9909 |  |
| **Kidney disease** | **+2.8922** | 1.1299 | ±2.2598 | **+2.560** | **0.0105** | * |
| Circulatory disease | -0.0491 | 0.8952 | ±1.7904 | -0.055 | 0.9563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **774**, R² = **0.1971**, Adj R² = **0.1855**, F-statistic = **17.00** (p = **2.72e-30**), Residual SE = **7.692** on **762** df, AIC = **5366.7**, BIC = **5422.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1542** | 4.2788 | ±8.5576 | **+11.722** | **9.89e-32** | *** |
| **Education: graduate level (vs college)** | **-2.2868** | 0.6084 | ±1.2168 | **-3.759** | **1.71e-04** | *** |
| Education: high school or below (vs college) | -1.8679 | 0.9992 | ±1.9984 | -1.869 | 0.0616 | . |
| **Site: UCSD (vs UAB)** | **-1.5987** | 0.7349 | ±1.4699 | **-2.175** | **0.0296** | * |
| **Site: UW (vs UAB)** | **-1.7773** | 0.7121 | ±1.4243 | **-2.496** | **0.0126** | * |
| **Age (years)** | **-0.1550** | 0.0290 | ±0.0580 | **-5.343** | **9.12e-08** | *** |
| **BMI (kg/m2)** | **+0.2808** | 0.0534 | ±0.1068 | **+5.259** | **1.45e-07** | *** |
| **Hypertension** | **+1.4631** | 0.6635 | ±1.3270 | **+2.205** | **0.0274** | * |
| High cholesterol | -0.3339 | 0.5734 | ±1.1467 | -0.582 | 0.5603 |  |
| **Kidney disease** | **+3.0027** | 1.0989 | ±2.1979 | **+2.732** | **0.0063** | ** |
| Circulatory disease | -0.2439 | 0.8630 | ±1.7260 | -0.283 | 0.7774 |  |
| **HbA1c (%)** | **+2.4096** | 0.7358 | ±1.4716 | **+3.275** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **774**, R² = **0.2022**, Adj R² = **0.1907**, F-statistic = **17.56** (p = **2.64e-31**), Residual SE = **7.668** on **762** df, AIC = **5361.7**, BIC = **5417.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8437** | 3.5942 | ±7.1884 | **+14.424** | **3.64e-47** | *** |
| **Education: graduate level (vs college)** | **-2.3253** | 0.6078 | ±1.2157 | **-3.826** | **1.30e-04** | *** |
| Education: high school or below (vs college) | -1.7122 | 0.9815 | ±1.9630 | -1.745 | 0.0811 | . |
| **Site: UCSD (vs UAB)** | **-1.5409** | 0.7372 | ±1.4744 | **-2.090** | **0.0366** | * |
| **Site: UW (vs UAB)** | **-1.9361** | 0.7096 | ±1.4192 | **-2.728** | **0.0064** | ** |
| **Age (years)** | **-0.1524** | 0.0290 | ±0.0579 | **-5.264** | **1.41e-07** | *** |
| **BMI (kg/m2)** | **+0.2848** | 0.0532 | ±0.1063 | **+5.357** | **8.47e-08** | *** |
| **Hypertension** | **+1.4925** | 0.6579 | ±1.3157 | **+2.269** | **0.0233** | * |
| High cholesterol | -0.1060 | 0.5737 | ±1.1475 | -0.185 | 0.8535 |  |
| **Kidney disease** | **+2.6195** | 1.1131 | ±2.2263 | **+2.353** | **0.0186** | * |
| Circulatory disease | -0.2817 | 0.8711 | ±1.7422 | -0.323 | 0.7464 |  |
| **Mean glucose (mg/dL)** | **+0.0965** | 0.0227 | ±0.0454 | **+4.256** | **2.08e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **774**, R² = **0.2022**, Adj R² = **0.1907**, F-statistic = **17.56** (p = **2.64e-31**), Residual SE = **7.668** on **762** df, AIC = **5361.7**, BIC = **5417.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.4854** | 6.1119 | ±12.2237 | **+6.297** | **3.04e-10** | *** |
| **Education: graduate level (vs college)** | **-2.3253** | 0.6078 | ±1.2157 | **-3.826** | **1.30e-04** | *** |
| Education: high school or below (vs college) | -1.7122 | 0.9815 | ±1.9630 | -1.745 | 0.0811 | . |
| **Site: UCSD (vs UAB)** | **-1.5409** | 0.7372 | ±1.4744 | **-2.090** | **0.0366** | * |
| **Site: UW (vs UAB)** | **-1.9361** | 0.7096 | ±1.4192 | **-2.728** | **0.0064** | ** |
| **Age (years)** | **-0.1524** | 0.0290 | ±0.0579 | **-5.264** | **1.41e-07** | *** |
| **BMI (kg/m2)** | **+0.2848** | 0.0532 | ±0.1063 | **+5.357** | **8.47e-08** | *** |
| **Hypertension** | **+1.4925** | 0.6579 | ±1.3157 | **+2.269** | **0.0233** | * |
| High cholesterol | -0.1060 | 0.5737 | ±1.1475 | -0.185 | 0.8535 |  |
| **Kidney disease** | **+2.6195** | 1.1131 | ±2.2263 | **+2.353** | **0.0186** | * |
| Circulatory disease | -0.2817 | 0.8711 | ±1.7422 | -0.323 | 0.7464 |  |
| **GMI (%)** | **+4.0358** | 0.9482 | ±1.8964 | **+4.256** | **2.08e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **774**, R² = **0.2015**, Adj R² = **0.1900**, F-statistic = **17.48** (p = **3.64e-31**), Residual SE = **7.671** on **762** df, AIC = **5362.4**, BIC = **5418.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.2659** | 3.2182 | ±6.4364 | **+16.551** | **1.56e-61** | *** |
| **Education: graduate level (vs college)** | **-2.3109** | 0.6067 | ±1.2133 | **-3.809** | **1.39e-04** | *** |
| Education: high school or below (vs college) | -1.7781 | 0.9907 | ±1.9814 | -1.795 | 0.0727 | . |
| **Site: UCSD (vs UAB)** | **-1.6524** | 0.7405 | ±1.4811 | **-2.231** | **0.0257** | * |
| **Site: UW (vs UAB)** | **-1.9670** | 0.7105 | ±1.4209 | **-2.769** | **0.0056** | ** |
| **Age (years)** | **-0.1440** | 0.0289 | ±0.0578 | **-4.982** | **6.29e-07** | *** |
| **BMI (kg/m2)** | **+0.2724** | 0.0525 | ±0.1051 | **+5.186** | **2.15e-07** | *** |
| **Hypertension** | **+1.5639** | 0.6583 | ±1.3166 | **+2.376** | **0.0175** | * |
| High cholesterol | -0.1641 | 0.5743 | ±1.1485 | -0.286 | 0.7750 |  |
| **Kidney disease** | **+2.8243** | 1.1018 | ±2.2036 | **+2.563** | **0.0104** | * |
| Circulatory disease | -0.2468 | 0.8648 | ±1.7295 | -0.285 | 0.7753 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0839** | 0.0198 | ±0.0396 | **+4.241** | **2.22e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **774**, R² = **0.1917**, Adj R² = **0.1800**, F-statistic = **16.43** (p = **3.08e-29**), Residual SE = **7.718** on **762** df, AIC = **5371.9**, BIC = **5427.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4726** | 2.9048 | ±5.8096 | **+20.474** | **3.67e-93** | *** |
| **Education: graduate level (vs college)** | **-2.2318** | 0.6120 | ±1.2239 | **-3.647** | **2.65e-04** | *** |
| Education: high school or below (vs college) | -1.8769 | 0.9917 | ±1.9834 | -1.893 | 0.0584 | . |
| **Site: UCSD (vs UAB)** | **-1.5000** | 0.7434 | ±1.4869 | **-2.018** | **0.0436** | * |
| **Site: UW (vs UAB)** | **-1.8176** | 0.7150 | ±1.4300 | **-2.542** | **0.0110** | * |
| **Age (years)** | **-0.1547** | 0.0296 | ±0.0592 | **-5.229** | **1.71e-07** | *** |
| **BMI (kg/m2)** | **+0.3009** | 0.0540 | ±0.1080 | **+5.574** | **2.49e-08** | *** |
| **Hypertension** | **+1.5360** | 0.6610 | ±1.3220 | **+2.324** | **0.0201** | * |
| High cholesterol | -0.0490 | 0.5773 | ±1.1545 | -0.085 | 0.9323 |  |
| **Kidney disease** | **+2.7013** | 1.1246 | ±2.2492 | **+2.402** | **0.0163** | * |
| Circulatory disease | -0.1379 | 0.8772 | ±1.7545 | -0.157 | 0.8751 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1782** | 0.0708 | ±0.1416 | **+2.516** | **0.0119** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **774**, R² = **0.1921**, Adj R² = **0.1805**, F-statistic = **16.47** (p = **2.54e-29**), Residual SE = **7.716** on **762** df, AIC = **5371.5**, BIC = **5427.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6481** | 2.8677 | ±5.7353 | **+20.800** | **4.31e-96** | *** |
| **Education: graduate level (vs college)** | **-2.2483** | 0.6117 | ±1.2234 | **-3.676** | **2.37e-04** | *** |
| Education: high school or below (vs college) | -1.8554 | 0.9900 | ±1.9799 | -1.874 | 0.0609 | . |
| **Site: UCSD (vs UAB)** | **-1.5018** | 0.7427 | ±1.4853 | **-2.022** | **0.0432** | * |
| **Site: UW (vs UAB)** | **-1.8380** | 0.7153 | ±1.4307 | **-2.569** | **0.0102** | * |
| **Age (years)** | **-0.1551** | 0.0296 | ±0.0592 | **-5.242** | **1.59e-07** | *** |
| **BMI (kg/m2)** | **+0.3002** | 0.0538 | ±0.1076 | **+5.577** | **2.45e-08** | *** |
| **Hypertension** | **+1.5278** | 0.6633 | ±1.3267 | **+2.303** | **0.0213** | * |
| High cholesterol | -0.0371 | 0.5770 | ±1.1540 | -0.064 | 0.9488 |  |
| **Kidney disease** | **+2.7243** | 1.1230 | ±2.2461 | **+2.426** | **0.0153** | * |
| Circulatory disease | -0.1223 | 0.8769 | ±1.7538 | -0.139 | 0.8891 |  |
| **Avg. daily SD (mg/dL)** | **+0.1875** | 0.0733 | ±0.1466 | **+2.559** | **0.0105** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **774**, R² = **0.1850**, Adj R² = **0.1732**, F-statistic = **15.72** (p = **6.18e-28**), Residual SE = **7.750** on **762** df, AIC = **5378.3**, BIC = **5434.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6669** | 3.0977 | ±6.1955 | **+19.907** | **3.53e-88** | *** |
| **Education: graduate level (vs college)** | **-2.2749** | 0.6176 | ±1.2351 | **-3.684** | **2.30e-04** | *** |
| Education: high school or below (vs college) | -1.7923 | 1.0003 | ±2.0007 | -1.792 | 0.0732 | . |
| **Site: UCSD (vs UAB)** | **-1.6028** | 0.7483 | ±1.4966 | **-2.142** | **0.0322** | * |
| **Site: UW (vs UAB)** | **-1.8127** | 0.7198 | ±1.4395 | **-2.518** | **0.0118** | * |
| **Age (years)** | **-0.1515** | 0.0298 | ±0.0596 | **-5.082** | **3.74e-07** | *** |
| **BMI (kg/m2)** | **+0.3067** | 0.0551 | ±0.1102 | **+5.565** | **2.62e-08** | *** |
| **Hypertension** | **+1.7174** | 0.6627 | ±1.3254 | **+2.591** | **0.0096** | ** |
| High cholesterol | +0.0033 | 0.5808 | ±1.1617 | +0.006 | 0.9954 |  |
| **Kidney disease** | **+2.8643** | 1.1348 | ±2.2696 | **+2.524** | **0.0116** | * |
| Circulatory disease | -0.0512 | 0.8934 | ±1.7868 | -0.057 | 0.9543 |  |
| CV (%) | +0.0543 | 0.0980 | ±0.1960 | +0.554 | 0.5799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **774**, R² = **0.1849**, Adj R² = **0.1731**, F-statistic = **15.71** (p = **6.38e-28**), Residual SE = **7.751** on **762** df, AIC = **5378.4**, BIC = **5434.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3112** | 3.3641 | ±6.7282 | **+18.820** | **5.22e-79** | *** |
| **Education: graduate level (vs college)** | **-2.2741** | 0.6180 | ±1.2360 | **-3.680** | **2.33e-04** | *** |
| Education: high school or below (vs college) | -1.7856 | 0.9985 | ±1.9970 | -1.788 | 0.0737 | . |
| **Site: UCSD (vs UAB)** | **-1.6104** | 0.7482 | ±1.4963 | **-2.152** | **0.0314** | * |
| **Site: UW (vs UAB)** | **-1.8195** | 0.7194 | ±1.4387 | **-2.529** | **0.0114** | * |
| **Age (years)** | **-0.1513** | 0.0297 | ±0.0595 | **-5.087** | **3.65e-07** | *** |
| **BMI (kg/m2)** | **+0.3065** | 0.0551 | ±0.1102 | **+5.562** | **2.66e-08** | *** |
| **Hypertension** | **+1.7231** | 0.6622 | ±1.3244 | **+2.602** | **0.0093** | ** |
| High cholesterol | +0.0048 | 0.5809 | ±1.1618 | +0.008 | 0.9934 |  |
| **Kidney disease** | **+2.8678** | 1.1352 | ±2.2703 | **+2.526** | **0.0115** | * |
| Circulatory disease | -0.0468 | 0.8942 | ±1.7885 | -0.052 | 0.9583 |  |
| Mean / SD ratio | -0.1203 | 0.2299 | ±0.4598 | -0.523 | 0.6007 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **774**, R² = **0.1854**, Adj R² = **0.1736**, F-statistic = **15.76** (p = **5.22e-28**), Residual SE = **7.748** on **762** df, AIC = **5377.9**, BIC = **5433.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7548** | 3.3168 | ±6.6337 | **+19.222** | **2.44e-82** | *** |
| **Education: graduate level (vs college)** | **-2.2673** | 0.6171 | ±1.2341 | **-3.674** | **2.38e-04** | *** |
| Education: high school or below (vs college) | -1.7953 | 0.9964 | ±1.9928 | -1.802 | 0.0716 | . |
| **Site: UCSD (vs UAB)** | **-1.6017** | 0.7476 | ±1.4951 | **-2.143** | **0.0321** | * |
| **Site: UW (vs UAB)** | **-1.8253** | 0.7192 | ±1.4384 | **-2.538** | **0.0112** | * |
| **Age (years)** | **-0.1520** | 0.0298 | ±0.0595 | **-5.105** | **3.31e-07** | *** |
| **BMI (kg/m2)** | **+0.3059** | 0.0550 | ±0.1100 | **+5.562** | **2.66e-08** | *** |
| **Hypertension** | **+1.7095** | 0.6626 | ±1.3252 | **+2.580** | **0.0099** | ** |
| High cholesterol | +0.0062 | 0.5809 | ±1.1617 | +0.011 | 0.9915 |  |
| **Kidney disease** | **+2.8549** | 1.1329 | ±2.2659 | **+2.520** | **0.0117** | * |
| Circulatory disease | -0.0369 | 0.8942 | ±1.7884 | -0.041 | 0.9671 |  |
| Avg. daily mean/SD | -0.1598 | 0.1825 | ±0.3650 | -0.876 | 0.3812 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **774**, R² = **0.1966**, Adj R² = **0.1850**, F-statistic = **16.95** (p = **3.38e-30**), Residual SE = **7.695** on **762** df, AIC = **5367.2**, BIC = **5423.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.4565** | 2.9834 | ±5.9668 | **+19.259** | **1.19e-82** | *** |
| **Education: graduate level (vs college)** | **-2.2730** | 0.6090 | ±1.2180 | **-3.732** | **1.90e-04** | *** |
| **Education: high school or below (vs college)** | **-2.0144** | 0.9905 | ±1.9809 | **-2.034** | **0.0420** | * |
| **Site: UCSD (vs UAB)** | **-1.5671** | 0.7426 | ±1.4852 | **-2.110** | **0.0348** | * |
| **Site: UW (vs UAB)** | **-1.7900** | 0.7151 | ±1.4302 | **-2.503** | **0.0123** | * |
| **Age (years)** | **-0.1496** | 0.0291 | ±0.0581 | **-5.148** | **2.63e-07** | *** |
| **BMI (kg/m2)** | **+0.3048** | 0.0529 | ±0.1059 | **+5.759** | **8.46e-09** | *** |
| **Hypertension** | **+1.8119** | 0.6608 | ±1.3215 | **+2.742** | **0.0061** | ** |
| High cholesterol | -0.0216 | 0.5774 | ±1.1548 | -0.037 | 0.9702 |  |
| **Kidney disease** | **+2.7607** | 1.1236 | ±2.2471 | **+2.457** | **0.0140** | * |
| Circulatory disease | +0.0309 | 0.8790 | ±1.7579 | +0.035 | 0.9720 |  |
| **MAG (mg/dL/h)** | **+0.1394** | 0.0438 | ±0.0877 | **+3.179** | **0.0015** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **774**, R² = **0.1917**, Adj R² = **0.1800**, F-statistic = **16.43** (p = **3.07e-29**), Residual SE = **7.718** on **762** df, AIC = **5371.9**, BIC = **5427.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8182** | 3.0528 | ±6.1056 | **+19.267** | **1.02e-82** | *** |
| **Education: graduate level (vs college)** | **-2.2721** | 0.6121 | ±1.2242 | **-3.712** | **2.06e-04** | *** |
| Education: high school or below (vs college) | -1.8947 | 0.9940 | ±1.9881 | -1.906 | 0.0566 | . |
| **Site: UCSD (vs UAB)** | **-1.5392** | 0.7448 | ±1.4896 | **-2.067** | **0.0388** | * |
| **Site: UW (vs UAB)** | **-1.8425** | 0.7158 | ±1.4317 | **-2.574** | **0.0101** | * |
| **Age (years)** | **-0.1544** | 0.0296 | ±0.0591 | **-5.225** | **1.74e-07** | *** |
| **BMI (kg/m2)** | **+0.3095** | 0.0548 | ±0.1095 | **+5.653** | **1.58e-08** | *** |
| **Hypertension** | **+1.6140** | 0.6626 | ±1.3252 | **+2.436** | **0.0149** | * |
| High cholesterol | -0.0117 | 0.5781 | ±1.1562 | -0.020 | 0.9839 |  |
| **Kidney disease** | **+2.7448** | 1.1246 | ±2.2491 | **+2.441** | **0.0147** | * |
| Circulatory disease | -0.1213 | 0.8748 | ±1.7496 | -0.139 | 0.8897 |  |
| **Avg. daily range (mg/dL)** | **+0.0430** | 0.0170 | ±0.0340 | **+2.529** | **0.0114** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **774**, R² = **0.1918**, Adj R² = **0.1801**, F-statistic = **16.43** (p = **3.01e-29**), Residual SE = **7.718** on **762** df, AIC = **5371.8**, BIC = **5427.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.9592** | 2.8063 | ±5.6127 | **+21.722** | **1.27e-104** | *** |
| **Education: graduate level (vs college)** | **-2.2920** | 0.6113 | ±1.2227 | **-3.749** | **1.77e-04** | *** |
| Education: high school or below (vs college) | -1.9006 | 0.9910 | ±1.9820 | -1.918 | 0.0551 | . |
| **Site: UCSD (vs UAB)** | **-1.5170** | 0.7440 | ±1.4879 | **-2.039** | **0.0414** | * |
| **Site: UW (vs UAB)** | **-1.7575** | 0.7144 | ±1.4287 | **-2.460** | **0.0139** | * |
| **Age (years)** | **-0.1499** | 0.0292 | ±0.0584 | **-5.135** | **2.83e-07** | *** |
| **BMI (kg/m2)** | **+0.2960** | 0.0541 | ±0.1083 | **+5.467** | **4.57e-08** | *** |
| **Hypertension** | **+1.7248** | 0.6565 | ±1.3130 | **+2.627** | **0.0086** | ** |
| High cholesterol | -0.1176 | 0.5811 | ±1.1623 | -0.202 | 0.8397 |  |
| **Kidney disease** | **+2.7516** | 1.1123 | ±2.2247 | **+2.474** | **0.0134** | * |
| Circulatory disease | -0.1926 | 0.8894 | ±1.7788 | -0.217 | 0.8286 |  |
| **SD of daily means (mg/dL)** | **+0.3126** | 0.1332 | ±0.2665 | **+2.347** | **0.0190** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **774**, R² = **0.1924**, Adj R² = **0.1807**, F-statistic = **16.50** (p = **2.25e-29**), Residual SE = **7.715** on **762** df, AIC = **5371.2**, BIC = **5427.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.0226** | 8.7041 | ±17.4083 | **+9.768** | **1.54e-22** | *** |
| **Education: graduate level (vs college)** | **-2.3049** | 0.6107 | ±1.2215 | **-3.774** | **1.61e-04** | *** |
| Education: high school or below (vs college) | -1.7803 | 0.9981 | ±1.9963 | -1.784 | 0.0745 | . |
| **Site: UCSD (vs UAB)** | **-1.5465** | 0.7460 | ±1.4920 | **-2.073** | **0.0382** | * |
| **Site: UW (vs UAB)** | **-1.8339** | 0.7132 | ±1.4263 | **-2.571** | **0.0101** | * |
| **Age (years)** | **-0.1540** | 0.0294 | ±0.0588 | **-5.236** | **1.64e-07** | *** |
| **BMI (kg/m2)** | **+0.2987** | 0.0541 | ±0.1083 | **+5.518** | **3.44e-08** | *** |
| **Hypertension** | **+1.6555** | 0.6619 | ±1.3238 | **+2.501** | **0.0124** | * |
| High cholesterol | -0.0963 | 0.5772 | ±1.1545 | -0.167 | 0.8675 |  |
| **Kidney disease** | **+2.6823** | 1.1224 | ±2.2448 | **+2.390** | **0.0169** | * |
| Circulatory disease | -0.2622 | 0.8880 | ±1.7759 | -0.295 | 0.7678 |  |
| **Time in range 70-180, pooled (%)** | **-0.2250** | 0.0806 | ±0.1612 | **-2.791** | **0.0053** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **774**, R² = **0.1933**, Adj R² = **0.1816**, F-statistic = **16.60** (p = **1.51e-29**), Residual SE = **7.711** on **762** df, AIC = **5370.4**, BIC = **5426.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+86.9031** | 8.8506 | ±17.7012 | **+9.819** | **9.34e-23** | *** |
| **Education: graduate level (vs college)** | **-2.3017** | 0.6101 | ±1.2203 | **-3.772** | **1.62e-04** | *** |
| Education: high school or below (vs college) | -1.7536 | 0.9977 | ±1.9954 | -1.758 | 0.0788 | . |
| **Site: UCSD (vs UAB)** | **-1.5347** | 0.7449 | ±1.4897 | **-2.060** | **0.0394** | * |
| **Site: UW (vs UAB)** | **-1.8350** | 0.7127 | ±1.4255 | **-2.575** | **0.0100** | * |
| **Age (years)** | **-0.1541** | 0.0294 | ±0.0588 | **-5.245** | **1.56e-07** | *** |
| **BMI (kg/m2)** | **+0.2976** | 0.0539 | ±0.1078 | **+5.523** | **3.34e-08** | *** |
| **Hypertension** | **+1.6462** | 0.6611 | ±1.3223 | **+2.490** | **0.0128** | * |
| High cholesterol | -0.1029 | 0.5764 | ±1.1529 | -0.179 | 0.8583 |  |
| **Kidney disease** | **+2.6613** | 1.1201 | ±2.2401 | **+2.376** | **0.0175** | * |
| Circulatory disease | -0.2891 | 0.8877 | ±1.7753 | -0.326 | 0.7447 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.2435** | 0.0818 | ±0.1637 | **-2.975** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **774**, R² = **0.1934**, Adj R² = **0.1818**, F-statistic = **16.61** (p = **1.41e-29**), Residual SE = **7.710** on **762** df, AIC = **5370.2**, BIC = **5426.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9450** | 2.8570 | ±5.7140 | **+22.032** | **1.43e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4288** | 0.6175 | ±1.2349 | **-3.933** | **8.38e-05** | *** |
| Education: high school or below (vs college) | -1.8664 | 0.9933 | ±1.9866 | -1.879 | 0.0602 | . |
| **Site: UCSD (vs UAB)** | **-1.5559** | 0.7447 | ±1.4894 | **-2.089** | **0.0367** | * |
| **Site: UW (vs UAB)** | **-1.8447** | 0.7166 | ±1.4333 | **-2.574** | **0.0101** | * |
| **Age (years)** | **-0.1497** | 0.0294 | ±0.0588 | **-5.093** | **3.52e-07** | *** |
| **BMI (kg/m2)** | **+0.3031** | 0.0553 | ±0.1106 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7273** | 0.6608 | ±1.3217 | **+2.614** | **0.0090** | ** |
| High cholesterol | +0.0328 | 0.5804 | ±1.1607 | +0.057 | 0.9549 |  |
| **Kidney disease** | **+2.8039** | 1.1229 | ±2.2458 | **+2.497** | **0.0125** | * |
| Circulatory disease | -0.0696 | 0.8901 | ±1.7802 | -0.078 | 0.9376 |  |
| **Time 54-69, pooled (%)** | **-1.6258** | 0.6836 | ±1.3672 | **-2.378** | **0.0174** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **774**, R² = **0.1923**, Adj R² = **0.1806**, F-statistic = **16.49** (p = **2.35e-29**), Residual SE = **7.715** on **762** df, AIC = **5371.3**, BIC = **5427.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8490** | 2.8548 | ±5.7096 | **+22.015** | **2.05e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4273** | 0.6178 | ±1.2356 | **-3.929** | **8.53e-05** | *** |
| Education: high school or below (vs college) | -1.8767 | 0.9931 | ±1.9862 | -1.890 | 0.0588 | . |
| **Site: UCSD (vs UAB)** | **-1.5271** | 0.7445 | ±1.4890 | **-2.051** | **0.0403** | * |
| **Site: UW (vs UAB)** | **-1.8312** | 0.7169 | ±1.4338 | **-2.554** | **0.0106** | * |
| **Age (years)** | **-0.1492** | 0.0294 | ±0.0588 | **-5.074** | **3.89e-07** | *** |
| **BMI (kg/m2)** | **+0.3035** | 0.0553 | ±0.1107 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7278** | 0.6613 | ±1.3226 | **+2.613** | **0.0090** | ** |
| High cholesterol | +0.0265 | 0.5805 | ±1.1610 | +0.046 | 0.9636 |  |
| **Kidney disease** | **+2.8003** | 1.1241 | ±2.2482 | **+2.491** | **0.0127** | * |
| Circulatory disease | -0.0904 | 0.8902 | ±1.7805 | -0.101 | 0.9192 |  |
| **Avg. daily time 54-69 (%)** | **-1.4725** | 0.6774 | ±1.3548 | **-2.174** | **0.0297** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **774**, R² = **0.1934**, Adj R² = **0.1818**, F-statistic = **16.61** (p = **1.41e-29**), Residual SE = **7.710** on **762** df, AIC = **5370.2**, BIC = **5426.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9450** | 2.8570 | ±5.7140 | **+22.032** | **1.43e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4288** | 0.6175 | ±1.2349 | **-3.933** | **8.38e-05** | *** |
| Education: high school or below (vs college) | -1.8664 | 0.9933 | ±1.9866 | -1.879 | 0.0602 | . |
| **Site: UCSD (vs UAB)** | **-1.5559** | 0.7447 | ±1.4894 | **-2.089** | **0.0367** | * |
| **Site: UW (vs UAB)** | **-1.8447** | 0.7166 | ±1.4333 | **-2.574** | **0.0101** | * |
| **Age (years)** | **-0.1497** | 0.0294 | ±0.0588 | **-5.093** | **3.52e-07** | *** |
| **BMI (kg/m2)** | **+0.3031** | 0.0553 | ±0.1106 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7273** | 0.6608 | ±1.3217 | **+2.614** | **0.0090** | ** |
| High cholesterol | +0.0328 | 0.5804 | ±1.1607 | +0.057 | 0.9549 |  |
| **Kidney disease** | **+2.8039** | 1.1229 | ±2.2458 | **+2.497** | **0.0125** | * |
| Circulatory disease | -0.0696 | 0.8901 | ±1.7802 | -0.078 | 0.9376 |  |
| **Time < 70 (%)** | **-1.6258** | 0.6836 | ±1.3672 | **-2.378** | **0.0174** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **774**, R² = **0.1923**, Adj R² = **0.1806**, F-statistic = **16.49** (p = **2.35e-29**), Residual SE = **7.715** on **762** df, AIC = **5371.3**, BIC = **5427.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8490** | 2.8548 | ±5.7096 | **+22.015** | **2.05e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4273** | 0.6178 | ±1.2356 | **-3.929** | **8.53e-05** | *** |
| Education: high school or below (vs college) | -1.8767 | 0.9931 | ±1.9862 | -1.890 | 0.0588 | . |
| **Site: UCSD (vs UAB)** | **-1.5271** | 0.7445 | ±1.4890 | **-2.051** | **0.0403** | * |
| **Site: UW (vs UAB)** | **-1.8312** | 0.7169 | ±1.4338 | **-2.554** | **0.0106** | * |
| **Age (years)** | **-0.1492** | 0.0294 | ±0.0588 | **-5.074** | **3.89e-07** | *** |
| **BMI (kg/m2)** | **+0.3035** | 0.0553 | ±0.1107 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7278** | 0.6613 | ±1.3226 | **+2.613** | **0.0090** | ** |
| High cholesterol | +0.0265 | 0.5805 | ±1.1610 | +0.046 | 0.9636 |  |
| **Kidney disease** | **+2.8003** | 1.1241 | ±2.2482 | **+2.491** | **0.0127** | * |
| Circulatory disease | -0.0904 | 0.8902 | ±1.7805 | -0.101 | 0.9192 |  |
| **Avg. daily time < 70 (%)** | **-1.4725** | 0.6774 | ±1.3548 | **-2.174** | **0.0297** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **774**, R² = **0.1949**, Adj R² = **0.1833**, F-statistic = **16.77** (p = **7.39e-30**), Residual SE = **7.703** on **762** df, AIC = **5368.8**, BIC = **5424.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5969** | 2.8064 | ±5.6127 | **+22.305** | **3.27e-110** | *** |
| **Education: graduate level (vs college)** | **-2.3274** | 0.6096 | ±1.2191 | **-3.818** | **1.34e-04** | *** |
| Education: high school or below (vs college) | -1.8000 | 0.9981 | ±1.9961 | -1.803 | 0.0713 | . |
| **Site: UCSD (vs UAB)** | **-1.5232** | 0.7454 | ±1.4907 | **-2.044** | **0.0410** | * |
| **Site: UW (vs UAB)** | **-1.8392** | 0.7121 | ±1.4242 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0294 | ±0.0587 | **-5.255** | **1.48e-07** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.0540 | ±0.1079 | **+5.506** | **3.67e-08** | *** |
| **Hypertension** | **+1.6377** | 0.6616 | ±1.3233 | **+2.475** | **0.0133** | * |
| High cholesterol | -0.1065 | 0.5762 | ±1.1525 | -0.185 | 0.8533 |  |
| **Kidney disease** | **+2.6390** | 1.1202 | ±2.2404 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.2952 | 0.8863 | ±1.7725 | -0.333 | 0.7390 |  |
| **Time 181-250, pooled (%)** | **+0.2564** | 0.0819 | ±0.1638 | **+3.132** | **0.0017** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **774**, R² = **0.1958**, Adj R² = **0.1842**, F-statistic = **16.87** (p = **4.81e-30**), Residual SE = **7.698** on **762** df, AIC = **5367.9**, BIC = **5423.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6230** | 2.7958 | ±5.5916 | **+22.399** | **4.02e-111** | *** |
| **Education: graduate level (vs college)** | **-2.3272** | 0.6089 | ±1.2177 | **-3.822** | **1.32e-04** | *** |
| Education: high school or below (vs college) | -1.7746 | 0.9973 | ±1.9946 | -1.779 | 0.0752 | . |
| **Site: UCSD (vs UAB)** | **-1.5035** | 0.7441 | ±1.4881 | **-2.021** | **0.0433** | * |
| **Site: UW (vs UAB)** | **-1.8385** | 0.7117 | ±1.4235 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0293 | ±0.0587 | **-5.261** | **1.43e-07** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.0537 | ±0.1074 | **+5.510** | **3.58e-08** | *** |
| **Hypertension** | **+1.6278** | 0.6608 | ±1.3217 | **+2.463** | **0.0138** | * |
| High cholesterol | -0.1133 | 0.5754 | ±1.1508 | -0.197 | 0.8440 |  |
| **Kidney disease** | **+2.6145** | 1.1179 | ±2.2357 | **+2.339** | **0.0193** | * |
| Circulatory disease | -0.3275 | 0.8861 | ±1.7722 | -0.370 | 0.7117 |  |
| **Avg. daily time 181-250 (%)** | **+0.2747** | 0.0823 | ±0.1646 | **+3.338** | **8.45e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **774**, R² = **0.1949**, Adj R² = **0.1833**, F-statistic = **16.77** (p = **7.39e-30**), Residual SE = **7.703** on **762** df, AIC = **5368.8**, BIC = **5424.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5969** | 2.8064 | ±5.6127 | **+22.305** | **3.27e-110** | *** |
| **Education: graduate level (vs college)** | **-2.3274** | 0.6096 | ±1.2191 | **-3.818** | **1.34e-04** | *** |
| Education: high school or below (vs college) | -1.8000 | 0.9981 | ±1.9961 | -1.803 | 0.0713 | . |
| **Site: UCSD (vs UAB)** | **-1.5232** | 0.7454 | ±1.4907 | **-2.044** | **0.0410** | * |
| **Site: UW (vs UAB)** | **-1.8392** | 0.7121 | ±1.4242 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0294 | ±0.0587 | **-5.255** | **1.48e-07** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.0540 | ±0.1079 | **+5.506** | **3.67e-08** | *** |
| **Hypertension** | **+1.6377** | 0.6616 | ±1.3233 | **+2.475** | **0.0133** | * |
| High cholesterol | -0.1065 | 0.5762 | ±1.1525 | -0.185 | 0.8533 |  |
| **Kidney disease** | **+2.6390** | 1.1202 | ±2.2404 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.2952 | 0.8863 | ±1.7725 | -0.333 | 0.7390 |  |
| **Time > 180 (%)** | **+0.2564** | 0.0819 | ±0.1638 | **+3.132** | **0.0017** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **774**, R² = **0.1958**, Adj R² = **0.1842**, F-statistic = **16.87** (p = **4.81e-30**), Residual SE = **7.698** on **762** df, AIC = **5367.9**, BIC = **5423.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6230** | 2.7958 | ±5.5916 | **+22.399** | **4.02e-111** | *** |
| **Education: graduate level (vs college)** | **-2.3272** | 0.6089 | ±1.2177 | **-3.822** | **1.32e-04** | *** |
| Education: high school or below (vs college) | -1.7746 | 0.9973 | ±1.9946 | -1.779 | 0.0752 | . |
| **Site: UCSD (vs UAB)** | **-1.5035** | 0.7441 | ±1.4881 | **-2.021** | **0.0433** | * |
| **Site: UW (vs UAB)** | **-1.8385** | 0.7117 | ±1.4235 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0293 | ±0.0587 | **-5.261** | **1.43e-07** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.0537 | ±0.1074 | **+5.510** | **3.58e-08** | *** |
| **Hypertension** | **+1.6278** | 0.6608 | ±1.3217 | **+2.463** | **0.0138** | * |
| High cholesterol | -0.1133 | 0.5754 | ±1.1508 | -0.197 | 0.8440 |  |
| **Kidney disease** | **+2.6145** | 1.1179 | ±2.2357 | **+2.339** | **0.0193** | * |
| Circulatory disease | -0.3275 | 0.8861 | ±1.7722 | -0.370 | 0.7117 |  |
| **Avg. daily time > 180 (%)** | **+0.2747** | 0.0823 | ±0.1646 | **+3.338** | **8.45e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **774**, R² = **0.1885**, Adj R² = **0.1768**, F-statistic = **16.09** (p = **1.30e-28**), Residual SE = **7.733** on **762** df, AIC = **5374.9**, BIC = **5430.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6027** | 2.8309 | ±5.6619 | **+22.114** | **2.33e-108** | *** |
| **Education: graduate level (vs college)** | **-2.2823** | 0.6121 | ±1.2242 | **-3.729** | **1.93e-04** | *** |
| Education: high school or below (vs college) | -1.8741 | 0.9997 | ±1.9993 | -1.875 | 0.0608 | . |
| **Site: UCSD (vs UAB)** | **-1.5551** | 0.7466 | ±1.4931 | **-2.083** | **0.0373** | * |
| **Site: UW (vs UAB)** | **-1.8142** | 0.7172 | ±1.4345 | **-2.529** | **0.0114** | * |
| **Age (years)** | **-0.1492** | 0.0295 | ±0.0589 | **-5.061** | **4.17e-07** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.0549 | ±0.1098 | **+5.390** | **7.04e-08** | *** |
| **Hypertension** | **+1.7600** | 0.6636 | ±1.3272 | **+2.652** | **0.0080** | ** |
| High cholesterol | -0.1081 | 0.5841 | ±1.1682 | -0.185 | 0.8532 |  |
| **Kidney disease** | **+2.7727** | 1.1176 | ±2.2352 | **+2.481** | **0.0131** | * |
| Circulatory disease | -0.1601 | 0.8921 | ±1.7841 | -0.179 | 0.8576 |  |
| **Nocturnal time > 180 (%)** | **+0.1439** | 0.0552 | ±0.1103 | **+2.609** | **0.0091** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 779; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0337**, F-statistic = **3.72** (p = **6.96e-05**), Residual SE = **68.144** on **768** df, AIC = **8798.9**, BIC = **8850.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0289** | 20.0650 | ±40.1300 | **+19.737** | **1.03e-86** | *** |
| Education: graduate level (vs college) | +3.7391 | 5.1659 | ±10.3318 | +0.724 | 0.4692 |  |
| Education: high school or below (vs college) | -10.2480 | 9.4268 | ±18.8535 | -1.087 | 0.2770 |  |
| Site: UCSD (vs UAB) | -11.1787 | 6.4849 | ±12.9697 | -1.724 | 0.0847 | . |
| Site: UW (vs UAB) | -2.2734 | 6.2240 | ±12.4480 | -0.365 | 0.7149 |  |
| Age (years) | +0.2656 | 0.2290 | ±0.4580 | +1.160 | 0.2461 |  |
| **BMI (kg/m2)** | **-1.1725** | 0.3805 | ±0.7609 | **-3.082** | **0.0021** | ** |
| **Hypertension** | **-15.6581** | 5.4435 | ±10.8870 | **-2.876** | **0.0040** | ** |
| High cholesterol | -4.4069 | 5.0157 | ±10.0315 | -0.879 | 0.3796 |  |
| Kidney disease | -11.9639 | 11.6264 | ±23.2527 | -1.029 | 0.3035 |  |
| Circulatory disease | +12.0514 | 8.1584 | ±16.3168 | +1.477 | 0.1396 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **779**, R² = **0.0554**, Adj R² = **0.0419**, F-statistic = **4.09** (p = **7.30e-06**), Residual SE = **67.856** on **767** df, AIC = **8793.3**, BIC = **8849.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+482.7682** | 35.8793 | ±71.7585 | **+13.455** | **2.86e-41** | *** |
| Education: graduate level (vs college) | +3.5461 | 5.1616 | ±10.3231 | +0.687 | 0.4921 |  |
| Education: high school or below (vs college) | -9.4689 | 9.3853 | ±18.7706 | -1.009 | 0.3130 |  |
| Site: UCSD (vs UAB) | -11.7142 | 6.4523 | ±12.9047 | -1.815 | 0.0694 | . |
| Site: UW (vs UAB) | -2.6027 | 6.2097 | ±12.4195 | -0.419 | 0.6751 |  |
| Age (years) | +0.3013 | 0.2298 | ±0.4596 | +1.311 | 0.1899 |  |
| **BMI (kg/m2)** | **-0.9994** | 0.3752 | ±0.7503 | **-2.664** | **0.0077** | ** |
| **Hypertension** | **-13.6168** | 5.4973 | ±10.9947 | **-2.477** | **0.0132** | * |
| High cholesterol | -2.0829 | 5.0807 | ±10.1614 | -0.410 | 0.6818 |  |
| Kidney disease | -12.6035 | 11.3992 | ±22.7983 | -1.106 | 0.2689 |  |
| Circulatory disease | +13.3256 | 8.1530 | ±16.3060 | +1.634 | 0.1022 |  |
| **HbA1c (%)** | **-16.8999** | 6.0907 | ±12.1815 | **-2.775** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **779**, R² = **0.0481**, Adj R² = **0.0345**, F-statistic = **3.52** (p = **7.71e-05**), Residual SE = **68.118** on **767** df, AIC = **8799.3**, BIC = **8855.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.0265** | 29.1694 | ±58.3388 | **+14.571** | **4.30e-48** | *** |
| Education: graduate level (vs college) | +3.8692 | 5.1689 | ±10.3378 | +0.749 | 0.4541 |  |
| Education: high school or below (vs college) | -10.3011 | 9.4304 | ±18.8609 | -1.092 | 0.2747 |  |
| Site: UCSD (vs UAB) | -11.4436 | 6.4843 | ±12.9687 | -1.765 | 0.0776 | . |
| Site: UW (vs UAB) | -1.9769 | 6.2589 | ±12.5179 | -0.316 | 0.7521 |  |
| Age (years) | +0.2716 | 0.2296 | ±0.4591 | +1.183 | 0.2368 |  |
| **BMI (kg/m2)** | **-1.1102** | 0.3816 | ±0.7632 | **-2.909** | **0.0036** | ** |
| **Hypertension** | **-14.9631** | 5.4338 | ±10.8676 | **-2.754** | **0.0059** | ** |
| High cholesterol | -4.1019 | 5.0472 | ±10.0944 | -0.813 | 0.4164 |  |
| Kidney disease | -11.0321 | 11.6922 | ±23.3844 | -0.944 | 0.3454 |  |
| Circulatory disease | +12.5722 | 8.2089 | ±16.4177 | +1.532 | 0.1256 |  |
| Mean glucose (mg/dL) | -0.2638 | 0.2102 | ±0.4204 | -1.255 | 0.2095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **779**, R² = **0.0481**, Adj R² = **0.0345**, F-statistic = **3.52** (p = **7.71e-05**), Residual SE = **68.118** on **767** df, AIC = **8799.3**, BIC = **8855.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+461.5341** | 54.1930 | ±108.3861 | **+8.516** | **1.64e-17** | *** |
| Education: graduate level (vs college) | +3.8692 | 5.1689 | ±10.3378 | +0.749 | 0.4541 |  |
| Education: high school or below (vs college) | -10.3011 | 9.4304 | ±18.8609 | -1.092 | 0.2747 |  |
| Site: UCSD (vs UAB) | -11.4436 | 6.4843 | ±12.9687 | -1.765 | 0.0776 | . |
| Site: UW (vs UAB) | -1.9769 | 6.2589 | ±12.5179 | -0.316 | 0.7521 |  |
| Age (years) | +0.2716 | 0.2296 | ±0.4591 | +1.183 | 0.2368 |  |
| **BMI (kg/m2)** | **-1.1102** | 0.3816 | ±0.7632 | **-2.909** | **0.0036** | ** |
| **Hypertension** | **-14.9631** | 5.4338 | ±10.8676 | **-2.754** | **0.0059** | ** |
| High cholesterol | -4.1019 | 5.0472 | ±10.0944 | -0.813 | 0.4164 |  |
| Kidney disease | -11.0321 | 11.6922 | ±23.3844 | -0.944 | 0.3454 |  |
| Circulatory disease | +12.5722 | 8.2089 | ±16.4177 | +1.532 | 0.1256 |  |
| GMI (%) | -11.0295 | 8.7885 | ±17.5771 | -1.255 | 0.2095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **779**, R² = **0.0518**, Adj R² = **0.0382**, F-statistic = **3.81** (p = **2.37e-05**), Residual SE = **67.986** on **767** df, AIC = **8796.3**, BIC = **8852.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+439.6318** | 28.3998 | ±56.7995 | **+15.480** | **4.73e-54** | *** |
| Education: graduate level (vs college) | +3.8390 | 5.1499 | ±10.2999 | +0.745 | 0.4560 |  |
| Education: high school or below (vs college) | -10.0908 | 9.4119 | ±18.8238 | -1.072 | 0.2837 |  |
| Site: UCSD (vs UAB) | -11.1201 | 6.4695 | ±12.9389 | -1.719 | 0.0856 | . |
| Site: UW (vs UAB) | -1.6079 | 6.2510 | ±12.5020 | -0.257 | 0.7970 |  |
| Age (years) | +0.2362 | 0.2278 | ±0.4557 | +1.037 | 0.2999 |  |
| **BMI (kg/m2)** | **-1.0053** | 0.3740 | ±0.7480 | **-2.688** | **0.0072** | ** |
| **Hypertension** | **-14.7319** | 5.4441 | ±10.8883 | **-2.706** | **0.0068** | ** |
| High cholesterol | -3.5412 | 5.0561 | ±10.1122 | -0.700 | 0.4837 |  |
| Kidney disease | -11.3945 | 11.6375 | ±23.2750 | -0.979 | 0.3275 |  |
| Circulatory disease | +12.7781 | 8.2013 | ±16.4026 | +1.558 | 0.1192 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.3983** | 0.1890 | ±0.3780 | **-2.107** | **0.0351** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **779**, R² = **0.0466**, Adj R² = **0.0329**, F-statistic = **3.41** (p = **1.25e-04**), Residual SE = **68.174** on **767** df, AIC = **8800.6**, BIC = **8856.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.9902** | 21.6009 | ±43.2018 | **+18.610** | **2.67e-77** | *** |
| Education: graduate level (vs college) | +3.6322 | 5.1712 | ±10.3423 | +0.702 | 0.4824 |  |
| Education: high school or below (vs college) | -9.9646 | 9.4931 | ±18.9861 | -1.050 | 0.2939 |  |
| Site: UCSD (vs UAB) | -11.4841 | 6.4978 | ±12.9956 | -1.767 | 0.0772 | . |
| Site: UW (vs UAB) | -2.3306 | 6.2342 | ±12.4684 | -0.374 | 0.7085 |  |
| Age (years) | +0.2752 | 0.2317 | ±0.4635 | +1.187 | 0.2351 |  |
| **BMI (kg/m2)** | **-1.1632** | 0.3816 | ±0.7632 | **-3.048** | **0.0023** | ** |
| **Hypertension** | **-15.2816** | 5.4746 | ±10.9492 | **-2.791** | **0.0052** | ** |
| High cholesterol | -4.2797 | 5.0513 | ±10.1025 | -0.847 | 0.3969 |  |
| Kidney disease | -11.4936 | 11.6579 | ±23.3158 | -0.986 | 0.3242 |  |
| Circulatory disease | +12.1904 | 8.1647 | ±16.3294 | +1.493 | 0.1354 |  |
| Glucose SD, pooled (mg/dL) | -0.3496 | 0.6377 | ±1.2754 | -0.548 | 0.5835 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **779**, R² = **0.0466**, Adj R² = **0.0329**, F-statistic = **3.41** (p = **1.23e-04**), Residual SE = **68.172** on **767** df, AIC = **8800.5**, BIC = **8856.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.7971** | 21.2089 | ±42.4178 | **+18.945** | **4.88e-80** | *** |
| Education: graduate level (vs college) | +3.6727 | 5.1699 | ±10.3398 | +0.710 | 0.4775 |  |
| Education: high school or below (vs college) | -9.9956 | 9.4795 | ±18.9589 | -1.054 | 0.2917 |  |
| Site: UCSD (vs UAB) | -11.4903 | 6.5079 | ±13.0157 | -1.766 | 0.0775 | . |
| Site: UW (vs UAB) | -2.2898 | 6.2349 | ±12.4699 | -0.367 | 0.7134 |  |
| Age (years) | +0.2761 | 0.2318 | ±0.4635 | +1.192 | 0.2334 |  |
| **BMI (kg/m2)** | **-1.1618** | 0.3816 | ±0.7632 | **-3.044** | **0.0023** | ** |
| **Hypertension** | **-15.2510** | 5.4846 | ±10.9692 | **-2.781** | **0.0054** | ** |
| High cholesterol | -4.3031 | 5.0434 | ±10.0868 | -0.853 | 0.3935 |  |
| Kidney disease | -11.5060 | 11.6844 | ±23.3688 | -0.985 | 0.3248 |  |
| Circulatory disease | +12.1723 | 8.1655 | ±16.3310 | +1.491 | 0.1360 |  |
| Avg. daily SD (mg/dL) | -0.3773 | 0.6417 | ±1.2835 | -0.588 | 0.5566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.4775** | 23.4000 | ±46.8001 | **+16.901** | **4.45e-64** | *** |
| Education: graduate level (vs college) | +3.7521 | 5.1827 | ±10.3655 | +0.724 | 0.4691 |  |
| Education: high school or below (vs college) | -10.2726 | 9.5336 | ±19.0673 | -1.078 | 0.2813 |  |
| Site: UCSD (vs UAB) | -11.1581 | 6.5015 | ±13.0030 | -1.716 | 0.0861 | . |
| Site: UW (vs UAB) | -2.2643 | 6.2448 | ±12.4896 | -0.363 | 0.7169 |  |
| Age (years) | +0.2649 | 0.2311 | ±0.4621 | +1.147 | 0.2516 |  |
| **BMI (kg/m2)** | **-1.1721** | 0.3803 | ±0.7607 | **-3.082** | **0.0021** | ** |
| **Hypertension** | **-15.6773** | 5.4733 | ±10.9467 | **-2.864** | **0.0042** | ** |
| High cholesterol | -4.4109 | 5.0315 | ±10.0631 | -0.877 | 0.3807 |  |
| Kidney disease | -11.9860 | 11.6153 | ±23.2305 | -1.032 | 0.3021 |  |
| Circulatory disease | +12.0509 | 8.1689 | ±16.3377 | +1.475 | 0.1402 |  |
| CV (%) | +0.0353 | 0.8978 | ±1.7956 | +0.039 | 0.9686 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.40e-04**), Residual SE = **68.187** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.5744** | 26.0137 | ±52.0273 | **+15.322** | **5.47e-53** | *** |
| Education: graduate level (vs college) | +3.8019 | 5.1901 | ±10.3801 | +0.733 | 0.4638 |  |
| Education: high school or below (vs college) | -10.3454 | 9.5230 | ±19.0460 | -1.086 | 0.2773 |  |
| Site: UCSD (vs UAB) | -11.1000 | 6.4899 | ±12.9799 | -1.710 | 0.0872 | . |
| Site: UW (vs UAB) | -2.2450 | 6.2395 | ±12.4789 | -0.360 | 0.7190 |  |
| Age (years) | +0.2628 | 0.2310 | ±0.4621 | +1.138 | 0.2553 |  |
| **BMI (kg/m2)** | **-1.1713** | 0.3806 | ±0.7612 | **-3.078** | **0.0021** | ** |
| **Hypertension** | **-15.7349** | 5.4657 | ±10.9314 | **-2.879** | **0.0040** | ** |
| High cholesterol | -4.4226 | 5.0294 | ±10.0588 | -0.879 | 0.3792 |  |
| Kidney disease | -12.0516 | 11.6067 | ±23.2133 | -1.038 | 0.2991 |  |
| Circulatory disease | +12.0619 | 8.1750 | ±16.3501 | +1.475 | 0.1401 |  |
| Mean / SD ratio | -0.3855 | 2.2462 | ±4.4924 | -0.172 | 0.8637 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.1595** | 25.4373 | ±50.8746 | **+15.574** | **1.09e-54** | *** |
| Education: graduate level (vs college) | +3.7417 | 5.1793 | ±10.3586 | +0.722 | 0.4700 |  |
| Education: high school or below (vs college) | -10.2526 | 9.5055 | ±19.0111 | -1.079 | 0.2808 |  |
| Site: UCSD (vs UAB) | -11.1748 | 6.5004 | ±13.0009 | -1.719 | 0.0856 | . |
| Site: UW (vs UAB) | -2.2727 | 6.2334 | ±12.4668 | -0.365 | 0.7154 |  |
| Age (years) | +0.2654 | 0.2313 | ±0.4626 | +1.147 | 0.2512 |  |
| **BMI (kg/m2)** | **-1.1725** | 0.3810 | ±0.7619 | **-3.078** | **0.0021** | ** |
| **Hypertension** | **-15.6618** | 5.4637 | ±10.9275 | **-2.867** | **0.0042** | ** |
| High cholesterol | -4.4075 | 5.0268 | ±10.0537 | -0.877 | 0.3806 |  |
| Kidney disease | -11.9688 | 11.6357 | ±23.2715 | -1.029 | 0.3037 |  |
| Circulatory disease | +12.0527 | 8.1764 | ±16.3529 | +1.474 | 0.1405 |  |
| Avg. daily mean/SD | -0.0169 | 1.7753 | ±3.5506 | -0.010 | 0.9924 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **779**, R² = **0.0565**, Adj R² = **0.0429**, F-statistic = **4.17** (p = **5.19e-06**), Residual SE = **67.819** on **767** df, AIC = **8792.5**, BIC = **8848.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+434.0392** | 22.9255 | ±45.8510 | **+18.933** | **6.15e-80** | *** |
| Education: graduate level (vs college) | +3.7504 | 5.1557 | ±10.3113 | +0.727 | 0.4670 |  |
| Education: high school or below (vs college) | -7.8805 | 9.3442 | ±18.6884 | -0.843 | 0.3990 |  |
| Site: UCSD (vs UAB) | -11.7337 | 6.5311 | ±13.0622 | -1.797 | 0.0724 | . |
| Site: UW (vs UAB) | -2.6855 | 6.2158 | ±12.4315 | -0.432 | 0.6657 |  |
| Age (years) | +0.2640 | 0.2282 | ±0.4564 | +1.157 | 0.2474 |  |
| **BMI (kg/m2)** | **-1.1593** | 0.3756 | ±0.7512 | **-3.087** | **0.0020** | ** |
| **Hypertension** | **-16.2008** | 5.4105 | ±10.8209 | **-2.994** | **0.0028** | ** |
| High cholesterol | -4.2177 | 4.9869 | ±9.9737 | -0.846 | 0.3977 |  |
| Kidney disease | -10.8620 | 11.5934 | ±23.1868 | -0.937 | 0.3488 |  |
| Circulatory disease | +11.0424 | 8.1311 | ±16.2622 | +1.358 | 0.1745 |  |
| **MAG (mg/dL/h)** | **-1.0574** | 0.4362 | ±0.8725 | **-2.424** | **0.0154** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.9158** | 22.9621 | ±45.9242 | **+17.242** | **1.28e-66** | *** |
| Education: graduate level (vs college) | +3.7391 | 5.1741 | ±10.3482 | +0.723 | 0.4699 |  |
| Education: high school or below (vs college) | -10.2531 | 9.5291 | ±19.0582 | -1.076 | 0.2819 |  |
| Site: UCSD (vs UAB) | -11.1751 | 6.5313 | ±13.0626 | -1.711 | 0.0871 | . |
| Site: UW (vs UAB) | -2.2730 | 6.2328 | ±12.4656 | -0.365 | 0.7154 |  |
| Age (years) | +0.2655 | 0.2323 | ±0.4645 | +1.143 | 0.2531 |  |
| **BMI (kg/m2)** | **-1.1724** | 0.3807 | ±0.7615 | **-3.079** | **0.0021** | ** |
| **Hypertension** | **-15.6617** | 5.4541 | ±10.9082 | **-2.872** | **0.0041** | ** |
| High cholesterol | -4.4075 | 5.0326 | ±10.0652 | -0.876 | 0.3811 |  |
| Kidney disease | -11.9698 | 11.6755 | ±23.3509 | -1.025 | 0.3053 |  |
| Circulatory disease | +12.0499 | 8.1667 | ±16.3335 | +1.475 | 0.1401 |  |
| Avg. daily range (mg/dL) | +0.0013 | 0.1589 | ±0.3178 | +0.008 | 0.9934 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **779**, R² = **0.0467**, Adj R² = **0.0330**, F-statistic = **3.41** (p = **1.20e-04**), Residual SE = **68.169** on **767** df, AIC = **8800.5**, BIC = **8856.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.3971** | 20.4286 | ±40.8572 | **+19.551** | **4.05e-85** | *** |
| Education: graduate level (vs college) | +3.7011 | 5.1712 | ±10.3424 | +0.716 | 0.4742 |  |
| Education: high school or below (vs college) | -9.9381 | 9.4631 | ±18.9262 | -1.050 | 0.2936 |  |
| Site: UCSD (vs UAB) | -11.4337 | 6.4672 | ±12.9344 | -1.768 | 0.0771 | . |
| Site: UW (vs UAB) | -2.4292 | 6.2247 | ±12.4494 | -0.390 | 0.6964 |  |
| Age (years) | +0.2644 | 0.2292 | ±0.4584 | +1.154 | 0.2487 |  |
| **BMI (kg/m2)** | **-1.1483** | 0.3827 | ±0.7654 | **-3.001** | **0.0027** | ** |
| **Hypertension** | **-15.6671** | 5.4430 | ±10.8861 | **-2.878** | **0.0040** | ** |
| High cholesterol | -4.0790 | 5.0559 | ±10.1119 | -0.807 | 0.4198 |  |
| Kidney disease | -11.6395 | 11.6069 | ±23.2139 | -1.003 | 0.3160 |  |
| Circulatory disease | +12.3588 | 8.1883 | ±16.3767 | +1.509 | 0.1312 |  |
| SD of daily means (mg/dL) | -0.6839 | 1.0582 | ±2.1164 | -0.646 | 0.5181 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.41e-04**), Residual SE = **68.187** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.6835** | 71.2653 | ±142.5306 | **+5.693** | **1.25e-08** | *** |
| Education: graduate level (vs college) | +3.7363 | 5.1726 | ±10.3452 | +0.722 | 0.4701 |  |
| Education: high school or below (vs college) | -10.2649 | 9.4519 | ±18.9039 | -1.086 | 0.2775 |  |
| Site: UCSD (vs UAB) | -11.1398 | 6.4846 | ±12.9692 | -1.718 | 0.0858 | . |
| Site: UW (vs UAB) | -2.2798 | 6.2332 | ±12.4665 | -0.366 | 0.7146 |  |
| Age (years) | +0.2638 | 0.2296 | ±0.4593 | +1.149 | 0.2506 |  |
| **BMI (kg/m2)** | **-1.1760** | 0.3821 | ±0.7642 | **-3.078** | **0.0021** | ** |
| **Hypertension** | **-15.6991** | 5.4606 | ±10.9211 | **-2.875** | **0.0040** | ** |
| High cholesterol | -4.4505 | 5.0423 | ±10.0845 | -0.883 | 0.3774 |  |
| Kidney disease | -12.0946 | 11.7464 | ±23.4928 | -1.030 | 0.3032 |  |
| Circulatory disease | +11.9704 | 8.2450 | ±16.4900 | +1.452 | 0.1465 |  |
| Time in range 70-180, pooled (%) | -0.0962 | 0.6737 | ±1.3474 | -0.143 | 0.8864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+394.4073** | 73.0940 | ±146.1880 | **+5.396** | **6.82e-08** | *** |
| Education: graduate level (vs college) | +3.7395 | 5.1720 | ±10.3440 | +0.723 | 0.4697 |  |
| Education: high school or below (vs college) | -10.2470 | 9.4426 | ±18.8852 | -1.085 | 0.2778 |  |
| Site: UCSD (vs UAB) | -11.1855 | 6.4812 | ±12.9624 | -1.726 | 0.0844 | . |
| Site: UW (vs UAB) | -2.2724 | 6.2360 | ±12.4721 | -0.364 | 0.7156 |  |
| Age (years) | +0.2659 | 0.2296 | ±0.4592 | +1.158 | 0.2468 |  |
| **BMI (kg/m2)** | **-1.1719** | 0.3819 | ±0.7638 | **-3.069** | **0.0022** | ** |
| **Hypertension** | **-15.6513** | 5.4647 | ±10.9295 | **-2.864** | **0.0042** | ** |
| High cholesterol | -4.3997 | 5.0378 | ±10.0756 | -0.873 | 0.3825 |  |
| Kidney disease | -11.9415 | 11.7737 | ±23.5474 | -1.014 | 0.3105 |  |
| Circulatory disease | +12.0658 | 8.2618 | ±16.5236 | +1.460 | 0.1442 |  |
| Avg. daily time in range 70-180 (%) | +0.0162 | 0.6937 | ±1.3874 | +0.023 | 0.9814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.39e-04**), Residual SE = **68.186** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7552** | 20.3133 | ±40.6266 | **+19.483** | **1.54e-84** | *** |
| Education: graduate level (vs college) | +3.8311 | 5.1982 | ±10.3963 | +0.737 | 0.4611 |  |
| Education: high school or below (vs college) | -10.1951 | 9.4336 | ±18.8673 | -1.081 | 0.2798 |  |
| Site: UCSD (vs UAB) | -11.2365 | 6.5074 | ±13.0148 | -1.727 | 0.0842 | . |
| Site: UW (vs UAB) | -2.2742 | 6.2288 | ±12.4577 | -0.365 | 0.7150 |  |
| Age (years) | +0.2647 | 0.2288 | ±0.4576 | +1.157 | 0.2473 |  |
| **BMI (kg/m2)** | **-1.1702** | 0.3822 | ±0.7644 | **-3.062** | **0.0022** | ** |
| **Hypertension** | **-15.6291** | 5.4402 | ±10.8804 | **-2.873** | **0.0041** | ** |
| High cholesterol | -4.4214 | 5.0157 | ±10.0314 | -0.882 | 0.3780 |  |
| Kidney disease | -11.9200 | 11.6340 | ±23.2680 | -1.025 | 0.3056 |  |
| Circulatory disease | +12.0635 | 8.1743 | ±16.3486 | +1.476 | 0.1400 |  |
| Time 54-69, pooled (%) | +1.1459 | 4.5203 | ±9.0405 | +0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0414** | 20.2281 | ±40.4563 | **+19.579** | **2.35e-85** | *** |
| Education: graduate level (vs college) | +3.7340 | 5.2102 | ±10.4204 | +0.717 | 0.4736 |  |
| Education: high school or below (vs college) | -10.2516 | 9.4372 | ±18.8744 | -1.086 | 0.2773 |  |
| Site: UCSD (vs UAB) | -11.1744 | 6.5168 | ±13.0337 | -1.715 | 0.0864 | . |
| Site: UW (vs UAB) | -2.2730 | 6.2271 | ±12.4543 | -0.365 | 0.7151 |  |
| Age (years) | +0.2657 | 0.2288 | ±0.4577 | +1.161 | 0.2456 |  |
| **BMI (kg/m2)** | **-1.1726** | 0.3814 | ±0.7629 | **-3.074** | **0.0021** | ** |
| **Hypertension** | **-15.6597** | 5.4437 | ±10.8874 | **-2.877** | **0.0040** | ** |
| High cholesterol | -4.4064 | 5.0167 | ±10.0334 | -0.878 | 0.3797 |  |
| Kidney disease | -11.9666 | 11.6396 | ±23.2792 | -1.028 | 0.3039 |  |
| Circulatory disease | +12.0498 | 8.1694 | ±16.3388 | +1.475 | 0.1402 |  |
| Avg. daily time 54-69 (%) | -0.0589 | 4.2605 | ±8.5210 | -0.014 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.39e-04**), Residual SE = **68.186** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7552** | 20.3133 | ±40.6266 | **+19.483** | **1.54e-84** | *** |
| Education: graduate level (vs college) | +3.8311 | 5.1982 | ±10.3963 | +0.737 | 0.4611 |  |
| Education: high school or below (vs college) | -10.1951 | 9.4336 | ±18.8673 | -1.081 | 0.2798 |  |
| Site: UCSD (vs UAB) | -11.2365 | 6.5074 | ±13.0148 | -1.727 | 0.0842 | . |
| Site: UW (vs UAB) | -2.2742 | 6.2288 | ±12.4577 | -0.365 | 0.7150 |  |
| Age (years) | +0.2647 | 0.2288 | ±0.4576 | +1.157 | 0.2473 |  |
| **BMI (kg/m2)** | **-1.1702** | 0.3822 | ±0.7644 | **-3.062** | **0.0022** | ** |
| **Hypertension** | **-15.6291** | 5.4402 | ±10.8804 | **-2.873** | **0.0041** | ** |
| High cholesterol | -4.4214 | 5.0157 | ±10.0314 | -0.882 | 0.3780 |  |
| Kidney disease | -11.9200 | 11.6340 | ±23.2680 | -1.025 | 0.3056 |  |
| Circulatory disease | +12.0635 | 8.1743 | ±16.3486 | +1.476 | 0.1400 |  |
| Time < 70 (%) | +1.1459 | 4.5203 | ±9.0405 | +0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0414** | 20.2281 | ±40.4563 | **+19.579** | **2.35e-85** | *** |
| Education: graduate level (vs college) | +3.7340 | 5.2102 | ±10.4204 | +0.717 | 0.4736 |  |
| Education: high school or below (vs college) | -10.2516 | 9.4372 | ±18.8744 | -1.086 | 0.2773 |  |
| Site: UCSD (vs UAB) | -11.1744 | 6.5168 | ±13.0337 | -1.715 | 0.0864 | . |
| Site: UW (vs UAB) | -2.2730 | 6.2271 | ±12.4543 | -0.365 | 0.7151 |  |
| Age (years) | +0.2657 | 0.2288 | ±0.4577 | +1.161 | 0.2456 |  |
| **BMI (kg/m2)** | **-1.1726** | 0.3814 | ±0.7629 | **-3.074** | **0.0021** | ** |
| **Hypertension** | **-15.6597** | 5.4437 | ±10.8874 | **-2.877** | **0.0040** | ** |
| High cholesterol | -4.4064 | 5.0167 | ±10.0334 | -0.878 | 0.3797 |  |
| Kidney disease | -11.9666 | 11.6396 | ±23.2792 | -1.028 | 0.3039 |  |
| Circulatory disease | +12.0498 | 8.1694 | ±16.3388 | +1.475 | 0.1402 |  |
| Avg. daily time < 70 (%) | -0.0589 | 4.2605 | ±8.5210 | -0.014 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0690** | 20.1231 | ±40.2462 | **+19.682** | **3.06e-86** | *** |
| Education: graduate level (vs college) | +3.7314 | 5.1776 | ±10.3552 | +0.721 | 0.4711 |  |
| Education: high school or below (vs college) | -10.2637 | 9.4544 | ±18.9087 | -1.086 | 0.2777 |  |
| Site: UCSD (vs UAB) | -11.1465 | 6.4864 | ±12.9728 | -1.718 | 0.0857 | . |
| Site: UW (vs UAB) | -2.2781 | 6.2345 | ±12.4690 | -0.365 | 0.7148 |  |
| Age (years) | +0.2643 | 0.2298 | ±0.4596 | +1.150 | 0.2500 |  |
| **BMI (kg/m2)** | **-1.1752** | 0.3827 | ±0.7654 | **-3.071** | **0.0021** | ** |
| **Hypertension** | **-15.6901** | 5.4584 | ±10.9168 | **-2.874** | **0.0040** | ** |
| High cholesterol | -4.4381 | 5.0453 | ±10.0905 | -0.880 | 0.3790 |  |
| Kidney disease | -12.0629 | 11.7528 | ±23.5057 | -1.026 | 0.3047 |  |
| Circulatory disease | +11.9910 | 8.2519 | ±16.5038 | +1.453 | 0.1462 |  |
| Time 181-250, pooled (%) | +0.0709 | 0.6756 | ±1.3511 | +0.105 | 0.9164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0201** | 20.1193 | ±40.2386 | **+19.684** | **2.98e-86** | *** |
| Education: graduate level (vs college) | +3.7407 | 5.1774 | ±10.3548 | +0.723 | 0.4700 |  |
| Education: high school or below (vs college) | -10.2463 | 9.4467 | ±18.8935 | -1.085 | 0.2781 |  |
| Site: UCSD (vs UAB) | -11.1859 | 6.4839 | ±12.9678 | -1.725 | 0.0845 | . |
| Site: UW (vs UAB) | -2.2726 | 6.2360 | ±12.4721 | -0.364 | 0.7155 |  |
| Age (years) | +0.2659 | 0.2297 | ±0.4594 | +1.157 | 0.2471 |  |
| **BMI (kg/m2)** | **-1.1719** | 0.3824 | ±0.7647 | **-3.065** | **0.0022** | ** |
| **Hypertension** | **-15.6516** | 5.4640 | ±10.9280 | **-2.865** | **0.0042** | ** |
| High cholesterol | -4.4005 | 5.0425 | ±10.0850 | -0.873 | 0.3828 |  |
| Kidney disease | -11.9431 | 11.7799 | ±23.5597 | -1.014 | 0.3106 |  |
| Circulatory disease | +12.0648 | 8.2678 | ±16.5356 | +1.459 | 0.1445 |  |
| Avg. daily time 181-250 (%) | -0.0145 | 0.6958 | ±1.3916 | -0.021 | 0.9833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0690** | 20.1231 | ±40.2462 | **+19.682** | **3.06e-86** | *** |
| Education: graduate level (vs college) | +3.7314 | 5.1776 | ±10.3552 | +0.721 | 0.4711 |  |
| Education: high school or below (vs college) | -10.2637 | 9.4544 | ±18.9087 | -1.086 | 0.2777 |  |
| Site: UCSD (vs UAB) | -11.1465 | 6.4864 | ±12.9728 | -1.718 | 0.0857 | . |
| Site: UW (vs UAB) | -2.2781 | 6.2345 | ±12.4690 | -0.365 | 0.7148 |  |
| Age (years) | +0.2643 | 0.2298 | ±0.4596 | +1.150 | 0.2500 |  |
| **BMI (kg/m2)** | **-1.1752** | 0.3827 | ±0.7654 | **-3.071** | **0.0021** | ** |
| **Hypertension** | **-15.6901** | 5.4584 | ±10.9168 | **-2.874** | **0.0040** | ** |
| High cholesterol | -4.4381 | 5.0453 | ±10.0905 | -0.880 | 0.3790 |  |
| Kidney disease | -12.0629 | 11.7528 | ±23.5057 | -1.026 | 0.3047 |  |
| Circulatory disease | +11.9910 | 8.2519 | ±16.5038 | +1.453 | 0.1462 |  |
| Time > 180 (%) | +0.0709 | 0.6756 | ±1.3511 | +0.105 | 0.9164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0201** | 20.1193 | ±40.2386 | **+19.684** | **2.98e-86** | *** |
| Education: graduate level (vs college) | +3.7407 | 5.1774 | ±10.3548 | +0.723 | 0.4700 |  |
| Education: high school or below (vs college) | -10.2463 | 9.4467 | ±18.8935 | -1.085 | 0.2781 |  |
| Site: UCSD (vs UAB) | -11.1859 | 6.4839 | ±12.9678 | -1.725 | 0.0845 | . |
| Site: UW (vs UAB) | -2.2726 | 6.2360 | ±12.4721 | -0.364 | 0.7155 |  |
| Age (years) | +0.2659 | 0.2297 | ±0.4594 | +1.157 | 0.2471 |  |
| **BMI (kg/m2)** | **-1.1719** | 0.3824 | ±0.7647 | **-3.065** | **0.0022** | ** |
| **Hypertension** | **-15.6516** | 5.4640 | ±10.9280 | **-2.865** | **0.0042** | ** |
| High cholesterol | -4.4005 | 5.0425 | ±10.0850 | -0.873 | 0.3828 |  |
| Kidney disease | -11.9431 | 11.7799 | ±23.5597 | -1.014 | 0.3106 |  |
| Circulatory disease | +12.0648 | 8.2678 | ±16.5356 | +1.459 | 0.1445 |  |
| Avg. daily time > 180 (%) | -0.0145 | 0.6958 | ±1.3916 | -0.021 | 0.9833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.41e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0734** | 20.0872 | ±40.1743 | **+19.718** | **1.52e-86** | *** |
| Education: graduate level (vs college) | +3.7452 | 5.1676 | ±10.3352 | +0.725 | 0.4686 |  |
| Education: high school or below (vs college) | -10.3178 | 9.5389 | ±19.0778 | -1.082 | 0.2794 |  |
| Site: UCSD (vs UAB) | -11.1314 | 6.4692 | ±12.9384 | -1.721 | 0.0853 | . |
| Site: UW (vs UAB) | -2.2637 | 6.2278 | ±12.4556 | -0.363 | 0.7162 |  |
| Age (years) | +0.2662 | 0.2293 | ±0.4586 | +1.161 | 0.2457 |  |
| **BMI (kg/m2)** | **-1.1779** | 0.3807 | ±0.7614 | **-3.094** | **0.0020** | ** |
| **Hypertension** | **-15.6526** | 5.4508 | ±10.9016 | **-2.872** | **0.0041** | ** |
| High cholesterol | -4.4733 | 5.0770 | ±10.1540 | -0.881 | 0.3783 |  |
| Kidney disease | -12.0483 | 11.6687 | ±23.3373 | -1.033 | 0.3018 |  |
| Circulatory disease | +11.9969 | 8.1988 | ±16.3976 | +1.463 | 0.1434 |  |
| Nocturnal time > 180 (%) | +0.0782 | 0.7326 | ±1.4651 | +0.107 | 0.9150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 775; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **775**, R² = **0.1374**, Adj R² = **0.1261**, F-statistic = **12.17** (p = **1.04e-19**), Residual SE = **17.203** on **764** df, AIC = **6620.1**, BIC = **6671.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2532** | 6.0370 | ±12.0740 | **+8.324** | **8.49e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6311** | 1.3655 | ±2.7309 | **-4.124** | **3.72e-05** | *** |
| Education: high school or below (vs college) | -2.6615 | 2.0967 | ±4.1934 | -1.269 | 0.2043 |  |
| Site: UCSD (vs UAB) | +1.5652 | 1.6593 | ±3.3186 | +0.943 | 0.3455 |  |
| Site: UW (vs UAB) | -1.0669 | 1.5497 | ±3.0994 | -0.688 | 0.4912 |  |
| **Age (years)** | **-0.2791** | 0.0637 | ±0.1273 | **-4.383** | **1.17e-05** | *** |
| **BMI (kg/m2)** | **+0.5939** | 0.1161 | ±0.2322 | **+5.115** | **3.13e-07** | *** |
| Hypertension | +2.3802 | 1.4598 | ±2.9196 | +1.630 | 0.1030 |  |
| High cholesterol | -0.2785 | 1.2984 | ±2.5969 | -0.215 | 0.8301 |  |
| **Kidney disease** | **+6.6916** | 2.4056 | ±4.8113 | **+2.782** | **0.0054** | ** |
| Circulatory disease | -0.2829 | 1.9434 | ±3.8867 | -0.146 | 0.8843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **775**, R² = **0.1432**, Adj R² = **0.1308**, F-statistic = **11.59** (p = **3.51e-20**), Residual SE = **17.157** on **763** df, AIC = **6617.0**, BIC = **6672.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.1962** | 9.6462 | ±19.2924 | **+3.338** | **8.45e-04** | *** |
| **Education: graduate level (vs college)** | **-5.6165** | 1.3582 | ±2.7164 | **-4.135** | **3.54e-05** | *** |
| Education: high school or below (vs college) | -2.8226 | 2.1103 | ±4.2205 | -1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | +1.6355 | 1.6450 | ±3.2901 | +0.994 | 0.3201 |  |
| Site: UW (vs UAB) | -0.9980 | 1.5427 | ±3.0855 | -0.647 | 0.5177 |  |
| **Age (years)** | **-0.2865** | 0.0630 | ±0.1260 | **-4.546** | **5.47e-06** | *** |
| **BMI (kg/m2)** | **+0.5560** | 0.1146 | ±0.2291 | **+4.854** | **1.21e-06** | *** |
| Hypertension | +1.9594 | 1.4704 | ±2.9409 | +1.333 | 0.1827 |  |
| High cholesterol | -0.7793 | 1.3059 | ±2.6117 | -0.597 | 0.5506 |  |
| **Kidney disease** | **+6.8492** | 2.3760 | ±4.7520 | **+2.883** | **0.0039** | ** |
| Circulatory disease | -0.5654 | 1.9129 | ±3.8258 | -0.296 | 0.7676 |  |
| **HbA1c (%)** | **+3.5328** | 1.6108 | ±3.2216 | **+2.193** | **0.0283** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **775**, R² = **0.1472**, Adj R² = **0.1349**, F-statistic = **11.97** (p = **6.54e-21**), Residual SE = **17.116** on **763** df, AIC = **6613.3**, BIC = **6669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.1435** | 8.0090 | ±16.0179 | **+4.138** | **3.50e-05** | *** |
| **Education: graduate level (vs college)** | **-5.6966** | 1.3529 | ±2.7058 | **-4.211** | **2.55e-05** | *** |
| Education: high school or below (vs college) | -2.5993 | 2.1075 | ±4.2149 | -1.233 | 0.2174 |  |
| Site: UCSD (vs UAB) | +1.7294 | 1.6505 | ±3.3009 | +1.048 | 0.2947 |  |
| Site: UW (vs UAB) | -1.2427 | 1.5456 | ±3.0913 | -0.804 | 0.4214 |  |
| **Age (years)** | **-0.2824** | 0.0629 | ±0.1259 | **-4.488** | **7.18e-06** | *** |
| **BMI (kg/m2)** | **+0.5593** | 0.1135 | ±0.2270 | **+4.927** | **8.35e-07** | *** |
| Hypertension | +1.9780 | 1.4603 | ±2.9205 | +1.355 | 0.1756 |  |
| High cholesterol | -0.4457 | 1.2935 | ±2.5870 | -0.345 | 0.7304 |  |
| **Kidney disease** | **+6.2431** | 2.3915 | ±4.7830 | **+2.611** | **0.0090** | ** |
| Circulatory disease | -0.6646 | 1.9148 | ±3.8295 | -0.347 | 0.7285 |  |
| **Mean glucose (mg/dL)** | **+0.1550** | 0.0523 | ±0.1045 | **+2.965** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **775**, R² = **0.1472**, Adj R² = **0.1349**, F-statistic = **11.97** (p = **6.54e-21**), Residual SE = **17.116** on **763** df, AIC = **6613.3**, BIC = **6669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +11.7008 | 13.9751 | ±27.9502 | +0.837 | 0.4024 |  |
| **Education: graduate level (vs college)** | **-5.6966** | 1.3529 | ±2.7058 | **-4.211** | **2.55e-05** | *** |
| Education: high school or below (vs college) | -2.5993 | 2.1075 | ±4.2149 | -1.233 | 0.2174 |  |
| Site: UCSD (vs UAB) | +1.7294 | 1.6505 | ±3.3009 | +1.048 | 0.2947 |  |
| Site: UW (vs UAB) | -1.2427 | 1.5456 | ±3.0913 | -0.804 | 0.4214 |  |
| **Age (years)** | **-0.2824** | 0.0629 | ±0.1259 | **-4.488** | **7.18e-06** | *** |
| **BMI (kg/m2)** | **+0.5593** | 0.1135 | ±0.2270 | **+4.927** | **8.35e-07** | *** |
| Hypertension | +1.9780 | 1.4603 | ±2.9205 | +1.355 | 0.1756 |  |
| High cholesterol | -0.4457 | 1.2935 | ±2.5870 | -0.345 | 0.7304 |  |
| **Kidney disease** | **+6.2431** | 2.3915 | ±4.7830 | **+2.611** | **0.0090** | ** |
| Circulatory disease | -0.6646 | 1.9148 | ±3.8295 | -0.347 | 0.7285 |  |
| **GMI (%)** | **+6.4781** | 2.1852 | ±4.3705 | **+2.965** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **775**, R² = **0.1477**, Adj R² = **0.1354**, F-statistic = **12.02** (p = **5.24e-21**), Residual SE = **17.111** on **763** df, AIC = **6612.8**, BIC = **6668.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.6728** | 7.3074 | ±14.6147 | **+4.745** | **2.09e-06** | *** |
| **Education: graduate level (vs college)** | **-5.6666** | 1.3522 | ±2.7045 | **-4.190** | **2.78e-05** | *** |
| Education: high school or below (vs college) | -2.6984 | 2.1167 | ±4.2334 | -1.275 | 0.2024 |  |
| Site: UCSD (vs UAB) | +1.5486 | 1.6516 | ±3.3032 | +0.938 | 0.3484 |  |
| Site: UW (vs UAB) | -1.3009 | 1.5460 | ±3.0921 | -0.841 | 0.4001 |  |
| **Age (years)** | **-0.2685** | 0.0628 | ±0.1255 | **-4.279** | **1.88e-05** | *** |
| **BMI (kg/m2)** | **+0.5367** | 0.1127 | ±0.2255 | **+4.761** | **1.93e-06** | *** |
| Hypertension | +2.0705 | 1.4571 | ±2.9141 | +1.421 | 0.1553 |  |
| High cholesterol | -0.5597 | 1.2936 | ±2.5872 | -0.433 | 0.6653 |  |
| **Kidney disease** | **+6.5726** | 2.3684 | ±4.7368 | **+2.775** | **0.0055** | ** |
| Circulatory disease | -0.6174 | 1.9057 | ±3.8114 | -0.324 | 0.7460 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.1415** | 0.0463 | ±0.0926 | **+3.055** | **0.0022** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **775**, R² = **0.1415**, Adj R² = **0.1291**, F-statistic = **11.43** (p = **7.03e-20**), Residual SE = **17.173** on **763** df, AIC = **6618.5**, BIC = **6674.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.2703** | 6.3919 | ±12.7839 | **+7.082** | **1.42e-12** | *** |
| **Education: graduate level (vs college)** | **-5.5382** | 1.3632 | ±2.7263 | **-4.063** | **4.85e-05** | *** |
| Education: high school or below (vs college) | -2.8608 | 2.0900 | ±4.1800 | -1.369 | 0.1711 |  |
| Site: UCSD (vs UAB) | +1.7834 | 1.6549 | ±3.3099 | +1.078 | 0.2812 |  |
| Site: UW (vs UAB) | -1.0565 | 1.5476 | ±3.0951 | -0.683 | 0.4948 |  |
| **Age (years)** | **-0.2858** | 0.0639 | ±0.1278 | **-4.472** | **7.74e-06** | *** |
| **BMI (kg/m2)** | **+0.5850** | 0.1146 | ±0.2292 | **+5.104** | **3.32e-07** | *** |
| Hypertension | +2.0332 | 1.4695 | ±2.9389 | +1.384 | 0.1665 |  |
| High cholesterol | -0.3611 | 1.2962 | ±2.5923 | -0.279 | 0.7806 |  |
| **Kidney disease** | **+6.3739** | 2.3962 | ±4.7925 | **+2.660** | **0.0078** | ** |
| Circulatory disease | -0.4342 | 1.9195 | ±3.8390 | -0.226 | 0.8210 |  |
| Glucose SD, pooled (mg/dL) | +0.2917 | 0.1561 | ±0.3122 | +1.868 | 0.0617 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **775**, R² = **0.1407**, Adj R² = **0.1283**, F-statistic = **11.36** (p = **9.60e-20**), Residual SE = **17.181** on **763** df, AIC = **6619.2**, BIC = **6675.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.1347** | 6.3078 | ±12.6156 | **+7.314** | **2.59e-13** | *** |
| **Education: graduate level (vs college)** | **-5.5740** | 1.3629 | ±2.7257 | **-4.090** | **4.32e-05** | *** |
| Education: high school or below (vs college) | -2.8057 | 2.0882 | ±4.1765 | -1.344 | 0.1791 |  |
| Site: UCSD (vs UAB) | +1.7534 | 1.6556 | ±3.3113 | +1.059 | 0.2896 |  |
| Site: UW (vs UAB) | -1.0870 | 1.5496 | ±3.0992 | -0.701 | 0.4830 |  |
| **Age (years)** | **-0.2856** | 0.0640 | ±0.1279 | **-4.464** | **8.04e-06** | *** |
| **BMI (kg/m2)** | **+0.5851** | 0.1147 | ±0.2294 | **+5.102** | **3.36e-07** | *** |
| Hypertension | +2.0645 | 1.4705 | ±2.9410 | +1.404 | 0.1603 |  |
| High cholesterol | -0.3334 | 1.2974 | ±2.5948 | -0.257 | 0.7972 |  |
| **Kidney disease** | **+6.4459** | 2.4030 | ±4.8060 | **+2.682** | **0.0073** | ** |
| Circulatory disease | -0.3935 | 1.9232 | ±3.8464 | -0.205 | 0.8379 |  |
| Avg. daily SD (mg/dL) | +0.2691 | 0.1608 | ±0.3215 | +1.674 | 0.0942 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **775**, R² = **0.1377**, Adj R² = **0.1253**, F-statistic = **11.08** (p = **3.27e-19**), Residual SE = **17.211** on **763** df, AIC = **6621.8**, BIC = **6677.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4038** | 6.8371 | ±13.6742 | **+7.080** | **1.45e-12** | *** |
| **Education: graduate level (vs college)** | **-5.5888** | 1.3719 | ±2.7438 | **-4.074** | **4.63e-05** | *** |
| Education: high school or below (vs college) | -2.7337 | 2.1013 | ±4.2026 | -1.301 | 0.1933 |  |
| Site: UCSD (vs UAB) | +1.6237 | 1.6596 | ±3.3192 | +0.978 | 0.3279 |  |
| Site: UW (vs UAB) | -1.0464 | 1.5527 | ±3.1055 | -0.674 | 0.5004 |  |
| **Age (years)** | **-0.2810** | 0.0641 | ±0.1282 | **-4.383** | **1.17e-05** | *** |
| **BMI (kg/m2)** | **+0.5946** | 0.1161 | ±0.2322 | **+5.122** | **3.02e-07** | *** |
| Hypertension | +2.3035 | 1.4664 | ±2.9329 | +1.571 | 0.1162 |  |
| High cholesterol | -0.2841 | 1.2996 | ±2.5992 | -0.219 | 0.8270 |  |
| **Kidney disease** | **+6.6298** | 2.4143 | ±4.8285 | **+2.746** | **0.0060** | ** |
| Circulatory disease | -0.2887 | 1.9406 | ±3.8813 | -0.149 | 0.8818 |  |
| CV (%) | +0.1184 | 0.2181 | ±0.4361 | +0.543 | 0.5870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **775**, R² = **0.1380**, Adj R² = **0.1255**, F-statistic = **11.10** (p = **2.99e-19**), Residual SE = **17.209** on **763** df, AIC = **6621.6**, BIC = **6677.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7695** | 7.0506 | ±14.1013 | **+7.484** | **7.19e-14** | *** |
| **Education: graduate level (vs college)** | **-5.5673** | 1.3716 | ±2.7432 | **-4.059** | **4.93e-05** | *** |
| Education: high school or below (vs college) | -2.7446 | 2.0982 | ±4.1963 | -1.308 | 0.1908 |  |
| Site: UCSD (vs UAB) | +1.6252 | 1.6592 | ±3.3184 | +0.980 | 0.3273 |  |
| Site: UW (vs UAB) | -1.0589 | 1.5515 | ±3.1030 | -0.682 | 0.4949 |  |
| **Age (years)** | **-0.2813** | 0.0640 | ±0.1280 | **-4.395** | **1.11e-05** | *** |
| **BMI (kg/m2)** | **+0.5943** | 0.1160 | ±0.2320 | **+5.124** | **2.99e-07** | *** |
| Hypertension | +2.2870 | 1.4663 | ±2.9327 | +1.560 | 0.1188 |  |
| High cholesterol | -0.2820 | 1.2996 | ±2.5991 | -0.217 | 0.8282 |  |
| **Kidney disease** | **+6.6134** | 2.4123 | ±4.8247 | **+2.742** | **0.0061** | ** |
| Circulatory disease | -0.2773 | 1.9410 | ±3.8819 | -0.143 | 0.8864 |  |
| Mean / SD ratio | -0.3799 | 0.5345 | ±1.0689 | -0.711 | 0.4772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **775**, R² = **0.1379**, Adj R² = **0.1254**, F-statistic = **11.09** (p = **3.12e-19**), Residual SE = **17.210** on **763** df, AIC = **6621.7**, BIC = **6677.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3882** | 6.9730 | ±13.9460 | **+7.513** | **5.78e-14** | *** |
| **Education: graduate level (vs college)** | **-5.5854** | 1.3698 | ±2.7397 | **-4.077** | **4.55e-05** | *** |
| Education: high school or below (vs college) | -2.7241 | 2.0966 | ±4.1933 | -1.299 | 0.1939 |  |
| Site: UCSD (vs UAB) | +1.6128 | 1.6593 | ±3.3187 | +0.972 | 0.3311 |  |
| Site: UW (vs UAB) | -1.0727 | 1.5519 | ±3.1039 | -0.691 | 0.4894 |  |
| **Age (years)** | **-0.2815** | 0.0641 | ±0.1282 | **-4.392** | **1.12e-05** | *** |
| **BMI (kg/m2)** | **+0.5931** | 0.1159 | ±0.2318 | **+5.117** | **3.10e-07** | *** |
| Hypertension | +2.3065 | 1.4638 | ±2.9277 | +1.576 | 0.1151 |  |
| High cholesterol | -0.2774 | 1.3000 | ±2.6000 | -0.213 | 0.8310 |  |
| **Kidney disease** | **+6.6265** | 2.4146 | ±4.8292 | **+2.744** | **0.0061** | ** |
| Circulatory disease | -0.2634 | 1.9447 | ±3.8894 | -0.135 | 0.8923 |  |
| Avg. daily mean/SD | -0.2752 | 0.4258 | ±0.8516 | -0.646 | 0.5180 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **775**, R² = **0.1406**, Adj R² = **0.1282**, F-statistic = **11.34** (p = **1.03e-19**), Residual SE = **17.183** on **763** df, AIC = **6619.3**, BIC = **6675.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.6573** | 6.6734 | ±13.3468 | **+6.692** | **2.20e-11** | *** |
| **Education: graduate level (vs college)** | **-5.6121** | 1.3611 | ±2.7222 | **-4.123** | **3.74e-05** | *** |
| Education: high school or below (vs college) | -2.9483 | 2.1173 | ±4.2347 | -1.392 | 0.1638 |  |
| Site: UCSD (vs UAB) | +1.6353 | 1.6583 | ±3.3166 | +0.986 | 0.3241 |  |
| Site: UW (vs UAB) | -1.0328 | 1.5468 | ±3.0936 | -0.668 | 0.5043 |  |
| **Age (years)** | **-0.2780** | 0.0635 | ±0.1271 | **-4.375** | **1.21e-05** | *** |
| **BMI (kg/m2)** | **+0.5921** | 0.1141 | ±0.2282 | **+5.190** | **2.11e-07** | *** |
| Hypertension | +2.4497 | 1.4626 | ±2.9251 | +1.675 | 0.0939 | . |
| High cholesterol | -0.3053 | 1.2982 | ±2.5964 | -0.235 | 0.8141 |  |
| **Kidney disease** | **+6.5422** | 2.4104 | ±4.8207 | **+2.714** | **0.0066** | ** |
| Circulatory disease | -0.1988 | 1.9368 | ±3.8737 | -0.103 | 0.9183 |  |
| MAG (mg/dL/h) | +0.1543 | 0.0971 | ±0.1943 | +1.588 | 0.1123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **775**, R² = **0.1408**, Adj R² = **0.1284**, F-statistic = **11.36** (p = **9.50e-20**), Residual SE = **17.181** on **763** df, AIC = **6619.1**, BIC = **6675.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.7791** | 6.7752 | ±13.5503 | **+6.609** | **3.86e-11** | *** |
| **Education: graduate level (vs college)** | **-5.6062** | 1.3622 | ±2.7243 | **-4.116** | **3.86e-05** | *** |
| Education: high school or below (vs college) | -2.8679 | 2.0938 | ±4.1876 | -1.370 | 0.1708 |  |
| Site: UCSD (vs UAB) | +1.7096 | 1.6606 | ±3.3213 | +1.029 | 0.3032 |  |
| Site: UW (vs UAB) | -1.0922 | 1.5482 | ±3.0965 | -0.705 | 0.4805 |  |
| **Age (years)** | **-0.2850** | 0.0640 | ±0.1279 | **-4.456** | **8.35e-06** | *** |
| **BMI (kg/m2)** | **+0.5986** | 0.1161 | ±0.2321 | **+5.158** | **2.50e-07** | *** |
| Hypertension | +2.1820 | 1.4650 | ±2.9300 | +1.489 | 0.1364 |  |
| High cholesterol | -0.2985 | 1.2977 | ±2.5955 | -0.230 | 0.8181 |  |
| **Kidney disease** | **+6.4685** | 2.4044 | ±4.8089 | **+2.690** | **0.0071** | ** |
| Circulatory disease | -0.3938 | 1.9242 | ±3.8483 | -0.205 | 0.8378 |  |
| Avg. daily range (mg/dL) | +0.0637 | 0.0379 | ±0.0758 | +1.681 | 0.0928 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **775**, R² = **0.1419**, Adj R² = **0.1296**, F-statistic = **11.47** (p = **5.81e-20**), Residual SE = **17.169** on **763** df, AIC = **6618.1**, BIC = **6673.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5806** | 6.0271 | ±12.0541 | **+7.894** | **2.91e-15** | *** |
| **Education: graduate level (vs college)** | **-5.6348** | 1.3597 | ±2.7194 | **-4.144** | **3.41e-05** | *** |
| Education: high school or below (vs college) | -2.9144 | 2.1062 | ±4.2124 | -1.384 | 0.1664 |  |
| Site: UCSD (vs UAB) | +1.7605 | 1.6528 | ±3.3055 | +1.065 | 0.2868 |  |
| Site: UW (vs UAB) | -0.9605 | 1.5417 | ±3.0835 | -0.623 | 0.5333 |  |
| **Age (years)** | **-0.2780** | 0.0633 | ±0.1267 | **-4.390** | **1.14e-05** | *** |
| **BMI (kg/m2)** | **+0.5758** | 0.1145 | ±0.2291 | **+5.027** | **4.99e-07** | *** |
| Hypertension | +2.3394 | 1.4521 | ±2.9042 | +1.611 | 0.1072 |  |
| High cholesterol | -0.4854 | 1.2985 | ±2.5970 | -0.374 | 0.7085 |  |
| **Kidney disease** | **+6.4408** | 2.3643 | ±4.7286 | **+2.724** | **0.0064** | ** |
| Circulatory disease | -0.5393 | 1.9327 | ±3.8654 | -0.279 | 0.7802 |  |
| **SD of daily means (mg/dL)** | **+0.5397** | 0.2682 | ±0.5365 | **+2.012** | **0.0442** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **775**, R² = **0.1378**, Adj R² = **0.1253**, F-statistic = **11.08** (p = **3.24e-19**), Residual SE = **17.210** on **763** df, AIC = **6621.8**, BIC = **6677.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.8602** | 18.0054 | ±36.0108 | **+3.380** | **7.25e-04** | *** |
| **Education: graduate level (vs college)** | **-5.6357** | 1.3644 | ±2.7288 | **-4.131** | **3.62e-05** | *** |
| Education: high school or below (vs college) | -2.6707 | 2.1038 | ±4.2076 | -1.269 | 0.2043 |  |
| Site: UCSD (vs UAB) | +1.6037 | 1.6608 | ±3.3217 | +0.966 | 0.3342 |  |
| Site: UW (vs UAB) | -1.0722 | 1.5508 | ±3.1017 | -0.691 | 0.4893 |  |
| **Age (years)** | **-0.2807** | 0.0639 | ±0.1278 | **-4.391** | **1.13e-05** | *** |
| **BMI (kg/m2)** | **+0.5903** | 0.1163 | ±0.2326 | **+5.076** | **3.85e-07** | *** |
| Hypertension | +2.3338 | 1.4635 | ±2.9271 | +1.595 | 0.1108 |  |
| High cholesterol | -0.3271 | 1.2994 | ±2.5987 | -0.252 | 0.8013 |  |
| **Kidney disease** | **+6.5931** | 2.4203 | ±4.8406 | **+2.724** | **0.0064** | ** |
| Circulatory disease | -0.3831 | 1.9419 | ±3.8838 | -0.197 | 0.8436 |  |
| Time in range 70-180, pooled (%) | -0.1060 | 0.1648 | ±0.3296 | -0.643 | 0.5199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **775**, R² = **0.1377**, Adj R² = **0.1253**, F-statistic = **11.08** (p = **3.28e-19**), Residual SE = **17.211** on **763** df, AIC = **6621.8**, BIC = **6677.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5881** | 18.2116 | ±36.4232 | **+3.327** | **8.78e-04** | *** |
| **Education: graduate level (vs college)** | **-5.6339** | 1.3645 | ±2.7291 | **-4.129** | **3.65e-05** | *** |
| Education: high school or below (vs college) | -2.6584 | 2.1046 | ±4.2091 | -1.263 | 0.2065 |  |
| Site: UCSD (vs UAB) | +1.6044 | 1.6606 | ±3.3211 | +0.966 | 0.3339 |  |
| Site: UW (vs UAB) | -1.0722 | 1.5510 | ±3.1020 | -0.691 | 0.4894 |  |
| **Age (years)** | **-0.2806** | 0.0639 | ±0.1278 | **-4.390** | **1.13e-05** | *** |
| **BMI (kg/m2)** | **+0.5902** | 0.1163 | ±0.2327 | **+5.073** | **3.92e-07** | *** |
| Hypertension | +2.3345 | 1.4633 | ±2.9266 | +1.595 | 0.1106 |  |
| High cholesterol | -0.3250 | 1.2992 | ±2.5984 | -0.250 | 0.8025 |  |
| **Kidney disease** | **+6.5942** | 2.4216 | ±4.8431 | **+2.723** | **0.0065** | ** |
| Circulatory disease | -0.3844 | 1.9419 | ±3.8838 | -0.198 | 0.8431 |  |
| Avg. daily time in range 70-180 (%) | -0.1032 | 0.1664 | ±0.3328 | -0.620 | 0.5351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1327**, F-statistic = **11.77** (p = **1.61e-20**), Residual SE = **17.138** on **763** df, AIC = **6615.3**, BIC = **6671.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1894** | 6.0308 | ±12.0616 | **+8.488** | **2.10e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9133** | 1.3693 | ±2.7386 | **-4.318** | **1.57e-05** | *** |
| Education: high school or below (vs college) | -2.8874 | 2.0949 | ±4.1897 | -1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +1.7784 | 1.6504 | ±3.3007 | +1.078 | 0.2812 |  |
| Site: UW (vs UAB) | -1.0851 | 1.5457 | ±3.0913 | -0.702 | 0.4827 |  |
| **Age (years)** | **-0.2792** | 0.0634 | ±0.1268 | **-4.404** | **1.06e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1163 | ±0.2325 | **+5.051** | **4.39e-07** | *** |
| Hypertension | +2.3518 | 1.4545 | ±2.9090 | +1.617 | 0.1059 |  |
| High cholesterol | -0.2136 | 1.2986 | ±2.5973 | -0.165 | 0.8693 |  |
| **Kidney disease** | **+6.5041** | 2.4058 | ±4.8116 | **+2.704** | **0.0069** | ** |
| Circulatory disease | -0.3224 | 1.9383 | ±3.8766 | -0.166 | 0.8679 |  |
| **Time 54-69, pooled (%)** | **-3.2322** | 1.5095 | ±3.0190 | **-2.141** | **0.0323** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1326**, F-statistic = **11.76** (p = **1.66e-20**), Residual SE = **17.139** on **763** df, AIC = **6615.3**, BIC = **6671.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0482** | 6.0261 | ±12.0523 | **+8.471** | **2.43e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9277** | 1.3706 | ±2.7412 | **-4.325** | **1.53e-05** | *** |
| Education: high school or below (vs college) | -2.9230 | 2.0950 | ±4.1901 | -1.395 | 0.1630 |  |
| Site: UCSD (vs UAB) | +1.8529 | 1.6500 | ±3.2999 | +1.123 | 0.2614 |  |
| Site: UW (vs UAB) | -1.0579 | 1.5457 | ±3.0914 | -0.684 | 0.4937 |  |
| **Age (years)** | **-0.2781** | 0.0634 | ±0.1268 | **-4.389** | **1.14e-05** | *** |
| **BMI (kg/m2)** | **+0.5875** | 0.1164 | ±0.2327 | **+5.048** | **4.46e-07** | *** |
| Hypertension | +2.3496 | 1.4549 | ±2.9098 | +1.615 | 0.1063 |  |
| High cholesterol | -0.2240 | 1.2986 | ±2.5972 | -0.172 | 0.8631 |  |
| **Kidney disease** | **+6.4848** | 2.4047 | ±4.8095 | **+2.697** | **0.0070** | ** |
| Circulatory disease | -0.3680 | 1.9378 | ±3.8756 | -0.190 | 0.8494 |  |
| **Avg. daily time 54-69 (%)** | **-3.1232** | 1.5891 | ±3.1781 | **-1.965** | **0.0494** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1327**, F-statistic = **11.77** (p = **1.61e-20**), Residual SE = **17.138** on **763** df, AIC = **6615.3**, BIC = **6671.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1894** | 6.0308 | ±12.0616 | **+8.488** | **2.10e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9133** | 1.3693 | ±2.7386 | **-4.318** | **1.57e-05** | *** |
| Education: high school or below (vs college) | -2.8874 | 2.0949 | ±4.1897 | -1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +1.7784 | 1.6504 | ±3.3007 | +1.078 | 0.2812 |  |
| Site: UW (vs UAB) | -1.0851 | 1.5457 | ±3.0913 | -0.702 | 0.4827 |  |
| **Age (years)** | **-0.2792** | 0.0634 | ±0.1268 | **-4.404** | **1.06e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1163 | ±0.2325 | **+5.051** | **4.39e-07** | *** |
| Hypertension | +2.3518 | 1.4545 | ±2.9090 | +1.617 | 0.1059 |  |
| High cholesterol | -0.2136 | 1.2986 | ±2.5973 | -0.165 | 0.8693 |  |
| **Kidney disease** | **+6.5041** | 2.4058 | ±4.8116 | **+2.704** | **0.0069** | ** |
| Circulatory disease | -0.3224 | 1.9383 | ±3.8766 | -0.166 | 0.8679 |  |
| **Time < 70 (%)** | **-3.2322** | 1.5095 | ±3.0190 | **-2.141** | **0.0323** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1326**, F-statistic = **11.76** (p = **1.66e-20**), Residual SE = **17.139** on **763** df, AIC = **6615.3**, BIC = **6671.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0482** | 6.0261 | ±12.0523 | **+8.471** | **2.43e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9277** | 1.3706 | ±2.7412 | **-4.325** | **1.53e-05** | *** |
| Education: high school or below (vs college) | -2.9230 | 2.0950 | ±4.1901 | -1.395 | 0.1630 |  |
| Site: UCSD (vs UAB) | +1.8529 | 1.6500 | ±3.2999 | +1.123 | 0.2614 |  |
| Site: UW (vs UAB) | -1.0579 | 1.5457 | ±3.0914 | -0.684 | 0.4937 |  |
| **Age (years)** | **-0.2781** | 0.0634 | ±0.1268 | **-4.389** | **1.14e-05** | *** |
| **BMI (kg/m2)** | **+0.5875** | 0.1164 | ±0.2327 | **+5.048** | **4.46e-07** | *** |
| Hypertension | +2.3496 | 1.4549 | ±2.9098 | +1.615 | 0.1063 |  |
| High cholesterol | -0.2240 | 1.2986 | ±2.5972 | -0.172 | 0.8631 |  |
| **Kidney disease** | **+6.4848** | 2.4047 | ±4.8095 | **+2.697** | **0.0070** | ** |
| Circulatory disease | -0.3680 | 1.9378 | ±3.8756 | -0.190 | 0.8494 |  |
| **Avg. daily time < 70 (%)** | **-3.1232** | 1.5891 | ±3.1781 | **-1.965** | **0.0494** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.47e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3099** | 6.0175 | ±12.0351 | **+8.361** | **6.24e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6540** | 1.3622 | ±2.7245 | **-4.150** | **3.32e-05** | *** |
| Education: high school or below (vs college) | -2.6890 | 2.1051 | ±4.2103 | -1.277 | 0.2015 |  |
| Site: UCSD (vs UAB) | +1.6404 | 1.6605 | ±3.3210 | +0.988 | 0.3232 |  |
| Site: UW (vs UAB) | -1.0766 | 1.5504 | ±3.1007 | -0.694 | 0.4874 |  |
| **Age (years)** | **-0.2817** | 0.0638 | ±0.1277 | **-4.413** | **1.02e-05** | *** |
| **BMI (kg/m2)** | **+0.5876** | 0.1160 | ±0.2320 | **+5.065** | **4.08e-07** | *** |
| Hypertension | +2.3020 | 1.4656 | ±2.9312 | +1.571 | 0.1163 |  |
| High cholesterol | -0.3552 | 1.2987 | ±2.5975 | -0.274 | 0.7844 |  |
| **Kidney disease** | **+6.5187** | 2.4153 | ±4.8307 | **+2.699** | **0.0070** | ** |
| Circulatory disease | -0.4507 | 1.9389 | ±3.8779 | -0.232 | 0.8162 |  |
| Time 181-250, pooled (%) | +0.1752 | 0.1685 | ±0.3370 | +1.040 | 0.2984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.49e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3231** | 6.0145 | ±12.0290 | **+8.367** | **5.91e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6527** | 1.3621 | ±2.7243 | **-4.150** | **3.33e-05** | *** |
| Education: high school or below (vs college) | -2.6711 | 2.1057 | ±4.2114 | -1.268 | 0.2046 |  |
| Site: UCSD (vs UAB) | +1.6491 | 1.6600 | ±3.3200 | +0.993 | 0.3205 |  |
| Site: UW (vs UAB) | -1.0756 | 1.5504 | ±3.1009 | -0.694 | 0.4879 |  |
| **Age (years)** | **-0.2816** | 0.0638 | ±0.1276 | **-4.412** | **1.03e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1160 | ±0.2319 | **+5.063** | **4.13e-07** | *** |
| Hypertension | +2.2997 | 1.4656 | ±2.9312 | +1.569 | 0.1166 |  |
| High cholesterol | -0.3555 | 1.2987 | ±2.5974 | -0.274 | 0.7843 |  |
| **Kidney disease** | **+6.5120** | 2.4165 | ±4.8330 | **+2.695** | **0.0070** | ** |
| Circulatory disease | -0.4627 | 1.9383 | ±3.8766 | -0.239 | 0.8113 |  |
| Avg. daily time 181-250 (%) | +0.1778 | 0.1690 | ±0.3380 | +1.052 | 0.2927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.47e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3099** | 6.0175 | ±12.0351 | **+8.361** | **6.24e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6540** | 1.3622 | ±2.7245 | **-4.150** | **3.32e-05** | *** |
| Education: high school or below (vs college) | -2.6890 | 2.1051 | ±4.2103 | -1.277 | 0.2015 |  |
| Site: UCSD (vs UAB) | +1.6404 | 1.6605 | ±3.3210 | +0.988 | 0.3232 |  |
| Site: UW (vs UAB) | -1.0766 | 1.5504 | ±3.1007 | -0.694 | 0.4874 |  |
| **Age (years)** | **-0.2817** | 0.0638 | ±0.1277 | **-4.413** | **1.02e-05** | *** |
| **BMI (kg/m2)** | **+0.5876** | 0.1160 | ±0.2320 | **+5.065** | **4.08e-07** | *** |
| Hypertension | +2.3020 | 1.4656 | ±2.9312 | +1.571 | 0.1163 |  |
| High cholesterol | -0.3552 | 1.2987 | ±2.5975 | -0.274 | 0.7844 |  |
| **Kidney disease** | **+6.5187** | 2.4153 | ±4.8307 | **+2.699** | **0.0070** | ** |
| Circulatory disease | -0.4507 | 1.9389 | ±3.8779 | -0.232 | 0.8162 |  |
| Time > 180 (%) | +0.1752 | 0.1685 | ±0.3370 | +1.040 | 0.2984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.49e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3231** | 6.0145 | ±12.0290 | **+8.367** | **5.91e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6527** | 1.3621 | ±2.7243 | **-4.150** | **3.33e-05** | *** |
| Education: high school or below (vs college) | -2.6711 | 2.1057 | ±4.2114 | -1.268 | 0.2046 |  |
| Site: UCSD (vs UAB) | +1.6491 | 1.6600 | ±3.3200 | +0.993 | 0.3205 |  |
| Site: UW (vs UAB) | -1.0756 | 1.5504 | ±3.1009 | -0.694 | 0.4879 |  |
| **Age (years)** | **-0.2816** | 0.0638 | ±0.1276 | **-4.412** | **1.03e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1160 | ±0.2319 | **+5.063** | **4.13e-07** | *** |
| Hypertension | +2.2997 | 1.4656 | ±2.9312 | +1.569 | 0.1166 |  |
| High cholesterol | -0.3555 | 1.2987 | ±2.5974 | -0.274 | 0.7843 |  |
| **Kidney disease** | **+6.5120** | 2.4165 | ±4.8330 | **+2.695** | **0.0070** | ** |
| Circulatory disease | -0.4627 | 1.9383 | ±3.8766 | -0.239 | 0.8113 |  |
| Avg. daily time > 180 (%) | +0.1778 | 0.1690 | ±0.3380 | +1.052 | 0.2927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **775**, R² = **0.1382**, Adj R² = **0.1257**, F-statistic = **11.12** (p = **2.77e-19**), Residual SE = **17.207** on **763** df, AIC = **6621.5**, BIC = **6677.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3416** | 6.0284 | ±12.0568 | **+8.351** | **6.78e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6188** | 1.3636 | ±2.7272 | **-4.121** | **3.78e-05** | *** |
| Education: high school or below (vs college) | -2.7704 | 2.1043 | ±4.2087 | -1.317 | 0.1880 |  |
| Site: UCSD (vs UAB) | +1.6381 | 1.6598 | ±3.3196 | +0.987 | 0.3237 |  |
| Site: UW (vs UAB) | -1.0587 | 1.5485 | ±3.0969 | -0.684 | 0.4942 |  |
| **Age (years)** | **-0.2778** | 0.0637 | ±0.1273 | **-4.365** | **1.27e-05** | *** |
| **BMI (kg/m2)** | **+0.5838** | 0.1172 | ±0.2344 | **+4.982** | **6.28e-07** | *** |
| Hypertension | +2.3869 | 1.4630 | ±2.9259 | +1.632 | 0.1028 |  |
| High cholesterol | -0.3880 | 1.3042 | ±2.6085 | -0.297 | 0.7661 |  |
| **Kidney disease** | **+6.5776** | 2.4038 | ±4.8076 | **+2.736** | **0.0062** | ** |
| Circulatory disease | -0.3883 | 1.9422 | ±3.8844 | -0.200 | 0.8415 |  |
| Nocturnal time > 180 (%) | +0.1373 | 0.1366 | ±0.2732 | +1.005 | 0.3148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
