# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 593; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1195**, F-statistic = **9.04** (p = **6.37e-14**), Residual SE = **3709.413** on **582** df, AIC = **11441.1**, BIC = **11489.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17270.8292** | 1250.4427 | ±2500.8853 | **+13.812** | **2.16e-43** | *** |
| Education: graduate level (vs college) | -578.8517 | 310.6041 | ±621.2082 | -1.864 | 0.0624 | . |
| Education: high school or below (vs college) | +1371.0371 | 776.6242 | ±1553.2485 | +1.765 | 0.0775 | . |
| Site: UCSD (vs UAB) | -158.5977 | 416.8466 | ±833.6931 | -0.380 | 0.7036 |  |
| Site: UW (vs UAB) | -476.6411 | 402.3052 | ±804.6103 | -1.185 | 0.2361 |  |
| **Age (years)** | **-106.4262** | 15.0854 | ±30.1708 | **-7.055** | **1.73e-12** | *** |
| BMI (kg/m2) | -18.0475 | 25.1397 | ±50.2793 | -0.718 | 0.4728 |  |
| Hypertension | +267.9617 | 384.8497 | ±769.6995 | +0.696 | 0.4863 |  |
| High cholesterol | -234.4279 | 306.4427 | ±612.8854 | -0.765 | 0.4443 |  |
| Kidney disease | -605.4053 | 565.4140 | ±1130.8280 | -1.071 | 0.2843 |  |
| **Circulatory disease** | **-1008.2603** | 493.1095 | ±986.2191 | **-2.045** | **0.0409** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **593**, R² = **0.1421**, Adj R² = **0.1258**, F-statistic = **8.75** (p = **1.90e-14**), Residual SE = **3696.097** on **581** df, AIC = **11437.8**, BIC = **11490.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11824.8308** | 2781.3840 | ±5562.7679 | **+4.251** | **2.12e-05** | *** |
| Education: graduate level (vs college) | -591.4675 | 308.2507 | ±616.5014 | -1.919 | 0.0550 | . |
| Education: high school or below (vs college) | +1377.4586 | 777.6321 | ±1555.2643 | +1.771 | 0.0765 | . |
| Site: UCSD (vs UAB) | -136.9874 | 414.4365 | ±828.8729 | -0.331 | 0.7410 |  |
| Site: UW (vs UAB) | -480.1261 | 401.3306 | ±802.6612 | -1.196 | 0.2316 |  |
| **Age (years)** | **-110.8054** | 14.9913 | ±29.9825 | **-7.391** | **1.45e-13** | *** |
| BMI (kg/m2) | -25.6574 | 24.3460 | ±48.6921 | -1.054 | 0.2919 |  |
| Hypertension | +209.3878 | 385.3062 | ±770.6124 | +0.543 | 0.5868 |  |
| High cholesterol | -332.9329 | 314.1540 | ±628.3081 | -1.060 | 0.2892 |  |
| Kidney disease | -598.4686 | 560.9389 | ±1121.8778 | -1.067 | 0.2860 |  |
| **Circulatory disease** | **-993.2849** | 486.7873 | ±973.5746 | **-2.040** | **0.0413** | * |
| **HbA1c (%)** | **+1073.7239** | 486.6861 | ±973.3722 | **+2.206** | **0.0274** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.99e-13**), Residual SE = **3712.601** on **581** df, AIC = **11443.1**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17318.0174** | 1982.0237 | ±3964.0475 | **+8.738** | **2.38e-18** | *** |
| Education: graduate level (vs college) | -578.4736 | 310.7475 | ±621.4950 | -1.862 | 0.0627 | . |
| Education: high school or below (vs college) | +1371.0560 | 778.0507 | ±1556.1014 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -159.4493 | 415.8973 | ±831.7946 | -0.383 | 0.7014 |  |
| Site: UW (vs UAB) | -475.9900 | 402.6115 | ±805.2230 | -1.182 | 0.2371 |  |
| **Age (years)** | **-106.4017** | 15.0873 | ±30.1746 | **-7.052** | **1.76e-12** | *** |
| BMI (kg/m2) | -17.9628 | 25.2687 | ±50.5373 | -0.711 | 0.4772 |  |
| Hypertension | +268.5502 | 387.1221 | ±774.2442 | +0.694 | 0.4879 |  |
| High cholesterol | -234.1851 | 307.2667 | ±614.5334 | -0.762 | 0.4460 |  |
| Kidney disease | -604.5071 | 567.1880 | ±1134.3760 | -1.066 | 0.2865 |  |
| **Circulatory disease** | **-1007.6178** | 494.0832 | ±988.1663 | **-2.039** | **0.0414** | * |
| Mean glucose (mg/dL) | -0.4346 | 13.7189 | ±27.4379 | -0.032 | 0.9747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.99e-13**), Residual SE = **3712.601** on **581** df, AIC = **11443.1**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17378.1581** | 3656.1750 | ±7312.3501 | **+4.753** | **2.00e-06** | *** |
| Education: graduate level (vs college) | -578.4736 | 310.7475 | ±621.4950 | -1.862 | 0.0627 | . |
| Education: high school or below (vs college) | +1371.0560 | 778.0507 | ±1556.1014 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -159.4493 | 415.8973 | ±831.7946 | -0.383 | 0.7014 |  |
| Site: UW (vs UAB) | -475.9900 | 402.6115 | ±805.2230 | -1.182 | 0.2371 |  |
| **Age (years)** | **-106.4017** | 15.0873 | ±30.1746 | **-7.052** | **1.76e-12** | *** |
| BMI (kg/m2) | -17.9628 | 25.2687 | ±50.5373 | -0.711 | 0.4772 |  |
| Hypertension | +268.5502 | 387.1221 | ±774.2442 | +0.694 | 0.4879 |  |
| High cholesterol | -234.1851 | 307.2667 | ±614.5334 | -0.762 | 0.4460 |  |
| Kidney disease | -604.5071 | 567.1880 | ±1134.3760 | -1.066 | 0.2865 |  |
| **Circulatory disease** | **-1007.6178** | 494.0832 | ±988.1663 | **-2.039** | **0.0414** | * |
| GMI (%) | -18.1694 | 573.5343 | ±1147.0686 | -0.032 | 0.9747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.594** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17196.9910** | 1836.2690 | ±3672.5380 | **+9.365** | **7.59e-21** | *** |
| Education: graduate level (vs college) | -579.1488 | 310.9962 | ±621.9925 | -1.862 | 0.0626 | . |
| Education: high school or below (vs college) | +1370.4543 | 777.4472 | ±1554.8944 | +1.763 | 0.0779 | . |
| Site: UCSD (vs UAB) | -158.1655 | 417.3283 | ±834.6565 | -0.379 | 0.7047 |  |
| Site: UW (vs UAB) | -478.0631 | 401.4486 | ±802.8971 | -1.191 | 0.2337 |  |
| **Age (years)** | **-106.3949** | 15.1037 | ±30.2075 | **-7.044** | **1.86e-12** | *** |
| BMI (kg/m2) | -18.3354 | 25.7223 | ±51.4446 | -0.713 | 0.4760 |  |
| Hypertension | +267.4091 | 385.9117 | ±771.8235 | +0.693 | 0.4884 |  |
| High cholesterol | -235.5700 | 309.2971 | ±618.5942 | -0.762 | 0.4463 |  |
| Kidney disease | -606.1232 | 566.3759 | ±1132.7519 | -1.070 | 0.2845 |  |
| **Circulatory disease** | **-1008.9203** | 494.1593 | ±988.3187 | **-2.042** | **0.0412** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.6873 | 12.6735 | ±25.3471 | +0.054 | 0.9568 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1347**, Adj R² = **0.1183**, F-statistic = **8.22** (p = **1.82e-13**), Residual SE = **3711.978** on **581** df, AIC = **11442.9**, BIC = **11495.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16970.7182** | 1379.8840 | ±2759.7680 | **+12.299** | **9.21e-35** | *** |
| Education: graduate level (vs college) | -569.2457 | 310.2932 | ±620.5864 | -1.835 | 0.0666 | . |
| Education: high school or below (vs college) | +1372.8445 | 776.4057 | ±1552.8113 | +1.768 | 0.0770 | . |
| Site: UCSD (vs UAB) | -142.1482 | 417.7264 | ±835.4529 | -0.340 | 0.7336 |  |
| Site: UW (vs UAB) | -484.6003 | 400.8034 | ±801.6068 | -1.209 | 0.2266 |  |
| **Age (years)** | **-107.1279** | 15.2627 | ±30.5254 | **-7.019** | **2.24e-12** | *** |
| BMI (kg/m2) | -18.4897 | 25.1697 | ±50.3395 | -0.735 | 0.4626 |  |
| Hypertension | +258.8673 | 384.1161 | ±768.2323 | +0.674 | 0.5004 |  |
| High cholesterol | -237.6574 | 307.3980 | ±614.7959 | -0.773 | 0.4394 |  |
| Kidney disease | -612.9529 | 568.8319 | ±1137.6638 | -1.078 | 0.2812 |  |
| **Circulatory disease** | **-1006.9504** | 494.3676 | ±988.7351 | **-2.037** | **0.0417** | * |
| Glucose SD, pooled (mg/dL) | +18.3482 | 41.2610 | ±82.5220 | +0.445 | 0.6565 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1345**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.95e-13**), Residual SE = **3712.467** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17143.3768** | 1368.5698 | ±2737.1396 | **+12.526** | **5.35e-36** | *** |
| Education: graduate level (vs college) | -575.4764 | 310.9087 | ±621.8174 | -1.851 | 0.0642 | . |
| Education: high school or below (vs college) | +1371.3479 | 777.2740 | ±1554.5479 | +1.764 | 0.0777 | . |
| Site: UCSD (vs UAB) | -149.7948 | 416.7296 | ±833.4592 | -0.359 | 0.7193 |  |
| Site: UW (vs UAB) | -480.2423 | 401.9390 | ±803.8781 | -1.195 | 0.2322 |  |
| **Age (years)** | **-106.7666** | 15.2369 | ±30.4737 | **-7.007** | **2.43e-12** | *** |
| BMI (kg/m2) | -18.3090 | 25.2034 | ±50.4068 | -0.726 | 0.4676 |  |
| Hypertension | +264.4228 | 384.8881 | ±769.7763 | +0.687 | 0.4921 |  |
| High cholesterol | -235.7332 | 307.2173 | ±614.4346 | -0.767 | 0.4429 |  |
| Kidney disease | -609.3386 | 567.5705 | ±1135.1410 | -1.074 | 0.2830 |  |
| **Circulatory disease** | **-1007.9536** | 494.3975 | ±988.7949 | **-2.039** | **0.0415** | * |
| Avg. daily SD (mg/dL) | +8.7525 | 41.6286 | ±83.2571 | +0.210 | 0.8335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **593**, R² = **0.1345**, Adj R² = **0.1181**, F-statistic = **8.21** (p = **1.94e-13**), Residual SE = **3712.425** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17068.7996** | 1426.3352 | ±2852.6705 | **+11.967** | **5.30e-33** | *** |
| Education: graduate level (vs college) | -571.0787 | 309.4186 | ±618.8372 | -1.846 | 0.0649 | . |
| Education: high school or below (vs college) | +1372.6077 | 776.9810 | ±1553.9621 | +1.767 | 0.0773 | . |
| Site: UCSD (vs UAB) | -151.9570 | 418.6475 | ±837.2949 | -0.363 | 0.7166 |  |
| Site: UW (vs UAB) | -478.5918 | 401.8645 | ±803.7290 | -1.191 | 0.2337 |  |
| **Age (years)** | **-106.7306** | 15.2641 | ±30.5283 | **-6.992** | **2.71e-12** | *** |
| BMI (kg/m2) | -17.9515 | 25.1465 | ±50.2929 | -0.714 | 0.4753 |  |
| Hypertension | +264.3268 | 383.5737 | ±767.1473 | +0.689 | 0.4908 |  |
| High cholesterol | -234.7521 | 307.0385 | ±614.0770 | -0.765 | 0.4445 |  |
| Kidney disease | -606.6295 | 567.7556 | ±1135.5112 | -1.068 | 0.2853 |  |
| **Circulatory disease** | **-1004.7199** | 493.6984 | ±987.3968 | **-2.035** | **0.0418** | * |
| CV (%) | +13.1953 | 53.3964 | ±106.7928 | +0.247 | 0.8048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.95e-13**), Residual SE = **3712.478** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17453.7439** | 1606.6735 | ±3213.3471 | **+10.863** | **1.72e-27** | *** |
| Education: graduate level (vs college) | -572.0337 | 309.1143 | ±618.2286 | -1.851 | 0.0642 | . |
| Education: high school or below (vs college) | +1371.6913 | 777.0411 | ±1554.0822 | +1.765 | 0.0775 | . |
| Site: UCSD (vs UAB) | -153.5738 | 418.0013 | ±836.0026 | -0.367 | 0.7133 |  |
| Site: UW (vs UAB) | -478.8689 | 401.5890 | ±803.1780 | -1.192 | 0.2331 |  |
| **Age (years)** | **-106.6565** | 15.2477 | ±30.4954 | **-6.995** | **2.65e-12** | *** |
| BMI (kg/m2) | -17.9705 | 25.1580 | ±50.3159 | -0.714 | 0.4750 |  |
| Hypertension | +265.0034 | 383.4396 | ±766.8792 | +0.691 | 0.4895 |  |
| High cholesterol | -234.4712 | 307.0252 | ±614.0503 | -0.764 | 0.4451 |  |
| Kidney disease | -606.6047 | 567.3671 | ±1134.7342 | -1.069 | 0.2850 |  |
| **Circulatory disease** | **-1004.9895** | 493.7249 | ±987.4498 | **-2.036** | **0.0418** | * |
| Mean / SD ratio | -27.4057 | 133.5297 | ±267.0595 | -0.205 | 0.8374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.97e-13**), Residual SE = **3712.552** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17384.1088** | 1578.3248 | ±3156.6495 | **+11.014** | **3.26e-28** | *** |
| Education: graduate level (vs college) | -575.3383 | 310.0980 | ±620.1960 | -1.855 | 0.0635 | . |
| Education: high school or below (vs college) | +1370.9144 | 777.2976 | ±1554.5953 | +1.764 | 0.0778 | . |
| Site: UCSD (vs UAB) | -154.6045 | 417.0325 | ±834.0650 | -0.371 | 0.7108 |  |
| Site: UW (vs UAB) | -478.2784 | 402.0413 | ±804.0825 | -1.190 | 0.2342 |  |
| **Age (years)** | **-106.5931** | 15.2686 | ±30.5371 | **-6.981** | **2.93e-12** | *** |
| BMI (kg/m2) | -18.0800 | 25.1802 | ±50.3603 | -0.718 | 0.4727 |  |
| Hypertension | +267.2443 | 384.7144 | ±769.4288 | +0.695 | 0.4873 |  |
| High cholesterol | -234.3819 | 306.9951 | ±613.9901 | -0.763 | 0.4452 |  |
| Kidney disease | -606.5828 | 566.8410 | ±1133.6819 | -1.070 | 0.2846 |  |
| **Circulatory disease** | **-1006.3671** | 493.5028 | ±987.0056 | **-2.039** | **0.0414** | * |
| Avg. daily mean/SD | -14.4739 | 109.6830 | ±219.3660 | -0.132 | 0.8950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **593**, R² = **0.1577**, Adj R² = **0.1418**, F-statistic = **9.89** (p = **1.43e-16**), Residual SE = **3662.222** on **581** df, AIC = **11426.8**, BIC = **11479.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13951.1236** | 1384.9433 | ±2769.8867 | **+10.073** | **7.24e-24** | *** |
| Education: graduate level (vs college) | -554.3693 | 304.0557 | ±608.1114 | -1.823 | 0.0683 | . |
| Education: high school or below (vs college) | +1193.7531 | 779.2668 | ±1558.5335 | +1.532 | 0.1255 |  |
| Site: UCSD (vs UAB) | -90.6408 | 410.7545 | ±821.5091 | -0.221 | 0.8254 |  |
| Site: UW (vs UAB) | -456.9627 | 397.3790 | ±794.7581 | -1.150 | 0.2502 |  |
| **Age (years)** | **-106.4514** | 14.8268 | ±29.6535 | **-7.180** | **6.99e-13** | *** |
| BMI (kg/m2) | -17.7222 | 24.1081 | ±48.2161 | -0.735 | 0.4623 |  |
| Hypertension | +348.8348 | 383.3914 | ±766.7827 | +0.910 | 0.3629 |  |
| High cholesterol | -232.6933 | 301.6073 | ±603.2146 | -0.772 | 0.4404 |  |
| Kidney disease | -725.2339 | 571.5479 | ±1143.0959 | -1.269 | 0.2045 |  |
| Circulatory disease | -893.0417 | 497.0552 | ±994.1104 | -1.797 | 0.0724 | . |
| **MAG (mg/dL/h)** | **+90.8297** | 25.7177 | ±51.4355 | **+3.532** | **4.13e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **593**, R² = **0.1356**, Adj R² = **0.1192**, F-statistic = **8.29** (p = **1.37e-13**), Residual SE = **3709.994** on **581** df, AIC = **11442.2**, BIC = **11494.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16544.6304** | 1453.8668 | ±2907.7337 | **+11.380** | **5.28e-30** | *** |
| Education: graduate level (vs college) | -572.9932 | 311.1507 | ±622.3013 | -1.842 | 0.0655 | . |
| Education: high school or below (vs college) | +1356.1676 | 776.8371 | ±1553.6741 | +1.746 | 0.0809 | . |
| Site: UCSD (vs UAB) | -135.1396 | 416.0419 | ±832.0838 | -0.325 | 0.7453 |  |
| Site: UW (vs UAB) | -492.5178 | 401.8603 | ±803.7205 | -1.226 | 0.2204 |  |
| **Age (years)** | **-107.6523** | 15.1872 | ±30.3744 | **-7.088** | **1.36e-12** | *** |
| BMI (kg/m2) | -17.1775 | 25.1938 | ±50.3875 | -0.682 | 0.4954 |  |
| Hypertension | +264.0079 | 385.4670 | ±770.9340 | +0.685 | 0.4934 |  |
| High cholesterol | -233.5913 | 306.6018 | ±613.2037 | -0.762 | 0.4461 |  |
| Kidney disease | -626.4669 | 568.2137 | ±1136.4274 | -1.103 | 0.2702 |  |
| **Circulatory disease** | **-1010.5797** | 494.0420 | ±988.0840 | **-2.046** | **0.0408** | * |
| Avg. daily range (mg/dL) | +8.6931 | 9.3253 | ±18.6505 | +0.932 | 0.3512 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **593**, R² = **0.1438**, Adj R² = **0.1276**, F-statistic = **8.87** (p = **1.10e-14**), Residual SE = **3692.279** on **581** df, AIC = **11436.5**, BIC = **11489.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16433.4853** | 1238.9385 | ±2477.8771 | **+13.264** | **3.74e-40** | *** |
| Education: graduate level (vs college) | -573.8199 | 308.1882 | ±616.3764 | -1.862 | 0.0626 | . |
| Education: high school or below (vs college) | +1385.6472 | 766.5799 | ±1533.1597 | +1.808 | 0.0707 | . |
| Site: UCSD (vs UAB) | -125.8880 | 415.5236 | ±831.0472 | -0.303 | 0.7619 |  |
| Site: UW (vs UAB) | -488.5381 | 397.3297 | ±794.6594 | -1.230 | 0.2189 |  |
| **Age (years)** | **-106.1058** | 15.0601 | ±30.1203 | **-7.045** | **1.85e-12** | *** |
| BMI (kg/m2) | -24.4950 | 25.0147 | ±50.0293 | -0.979 | 0.3275 |  |
| Hypertension | +267.2084 | 380.1556 | ±760.3112 | +0.703 | 0.4821 |  |
| High cholesterol | -284.0465 | 307.9535 | ±615.9070 | -0.922 | 0.3563 |  |
| Kidney disease | -590.6265 | 561.1517 | ±1122.3033 | -1.053 | 0.2926 |  |
| **Circulatory disease** | **-1006.8727** | 493.0741 | ±986.1482 | **-2.042** | **0.0411** | * |
| **SD of daily means (mg/dL)** | **+175.1072** | 77.0978 | ±154.1957 | **+2.271** | **0.0231** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.99e-13**), Residual SE = **3712.602** on **581** df, AIC = **11443.1**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17431.5894** | 5952.4245 | ±11904.8490 | **+2.928** | **0.0034** | ** |
| Education: graduate level (vs college) | -578.7877 | 311.1963 | ±622.3926 | -1.860 | 0.0629 | . |
| Education: high school or below (vs college) | +1371.4197 | 780.4041 | ±1560.8081 | +1.757 | 0.0789 | . |
| Site: UCSD (vs UAB) | -157.7589 | 419.3374 | ±838.6749 | -0.376 | 0.7068 |  |
| Site: UW (vs UAB) | -477.0293 | 401.7645 | ±803.5290 | -1.187 | 0.2351 |  |
| **Age (years)** | **-106.4573** | 15.0786 | ±30.1573 | **-7.060** | **1.66e-12** | *** |
| BMI (kg/m2) | -18.0768 | 25.2158 | ±50.4317 | -0.717 | 0.4734 |  |
| Hypertension | +267.9819 | 385.2821 | ±770.5641 | +0.696 | 0.4867 |  |
| High cholesterol | -235.0346 | 308.1483 | ±616.2966 | -0.763 | 0.4456 |  |
| Kidney disease | -605.8635 | 566.3937 | ±1132.7875 | -1.070 | 0.2848 |  |
| **Circulatory disease** | **-1009.0474** | 493.7708 | ±987.5415 | **-2.044** | **0.0410** | * |
| Time in range 70-180, pooled (%) | -1.6095 | 58.8774 | ±117.7548 | -0.027 | 0.9782 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.583** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17738.6654** | 6007.4487 | ±12014.8975 | **+2.953** | **0.0031** | ** |
| Education: graduate level (vs college) | -578.7190 | 311.1141 | ±622.2282 | -1.860 | 0.0629 | . |
| Education: high school or below (vs college) | +1372.4222 | 780.2959 | ±1560.5919 | +1.759 | 0.0786 | . |
| Site: UCSD (vs UAB) | -156.0382 | 419.3391 | ±838.6782 | -0.372 | 0.7098 |  |
| Site: UW (vs UAB) | -477.5417 | 402.0067 | ±804.0135 | -1.188 | 0.2349 |  |
| **Age (years)** | **-106.5098** | 15.0776 | ±30.1551 | **-7.064** | **1.62e-12** | *** |
| BMI (kg/m2) | -18.1550 | 25.2354 | ±50.4708 | -0.719 | 0.4719 |  |
| Hypertension | +268.1563 | 385.2156 | ±770.4311 | +0.696 | 0.4864 |  |
| High cholesterol | -236.2019 | 308.0162 | ±616.0324 | -0.767 | 0.4432 |  |
| Kidney disease | -606.8048 | 566.3888 | ±1132.7777 | -1.071 | 0.2840 |  |
| **Circulatory disease** | **-1010.7979** | 494.0180 | ±988.0361 | **-2.046** | **0.0407** | * |
| Avg. daily time in range 70-180 (%) | -4.6772 | 59.2992 | ±118.5984 | -0.079 | 0.9371 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **593**, R² = **0.1346**, Adj R² = **0.1182**, F-statistic = **8.22** (p = **1.86e-13**), Residual SE = **3712.126** on **581** df, AIC = **11442.9**, BIC = **11495.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17310.8127** | 1260.8379 | ±2521.6759 | **+13.730** | **6.75e-43** | *** |
| Education: graduate level (vs college) | -593.2115 | 313.1815 | ±626.3630 | -1.894 | 0.0582 | . |
| Education: high school or below (vs college) | +1355.1262 | 776.1060 | ±1552.2119 | +1.746 | 0.0808 | . |
| Site: UCSD (vs UAB) | -150.8911 | 419.4364 | ±838.8728 | -0.360 | 0.7190 |  |
| Site: UW (vs UAB) | -478.4559 | 402.3708 | ±804.7416 | -1.189 | 0.2344 |  |
| **Age (years)** | **-106.5054** | 15.1299 | ±30.2597 | **-7.039** | **1.93e-12** | *** |
| BMI (kg/m2) | -18.2068 | 25.1447 | ±50.2893 | -0.724 | 0.4690 |  |
| Hypertension | +268.7329 | 385.1777 | ±770.3555 | +0.698 | 0.4854 |  |
| High cholesterol | -232.7983 | 306.6463 | ±613.2926 | -0.759 | 0.4477 |  |
| Kidney disease | -610.8263 | 564.5797 | ±1129.1594 | -1.082 | 0.2793 |  |
| **Circulatory disease** | **-1013.4199** | 493.4754 | ±986.9508 | **-2.054** | **0.0400** | * |
| Time 54-69, pooled (%) | -110.8416 | 370.7164 | ±741.4328 | -0.299 | 0.7649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **593**, R² = **0.1348**, Adj R² = **0.1184**, F-statistic = **8.23** (p = **1.76e-13**), Residual SE = **3711.768** on **581** df, AIC = **11442.8**, BIC = **11495.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17316.7396** | 1258.9383 | ±2517.8766 | **+13.755** | **4.75e-43** | *** |
| Education: graduate level (vs college) | -598.6666 | 312.8213 | ±625.6426 | -1.914 | 0.0557 | . |
| Education: high school or below (vs college) | +1348.2542 | 776.0834 | ±1552.1668 | +1.737 | 0.0823 | . |
| Site: UCSD (vs UAB) | -145.2398 | 420.6501 | ±841.3002 | -0.345 | 0.7299 |  |
| Site: UW (vs UAB) | -478.1780 | 402.5600 | ±805.1199 | -1.188 | 0.2349 |  |
| **Age (years)** | **-106.4717** | 15.1188 | ±30.2376 | **-7.042** | **1.89e-12** | *** |
| BMI (kg/m2) | -18.2344 | 25.1544 | ±50.3087 | -0.725 | 0.4685 |  |
| Hypertension | +268.0523 | 385.2641 | ±770.5281 | +0.696 | 0.4866 |  |
| High cholesterol | -232.9887 | 306.7647 | ±613.5294 | -0.760 | 0.4476 |  |
| Kidney disease | -612.3782 | 564.3677 | ±1128.7353 | -1.085 | 0.2779 |  |
| **Circulatory disease** | **-1017.4472** | 493.3926 | ±986.7852 | **-2.062** | **0.0392** | * |
| Avg. daily time 54-69 (%) | -142.2810 | 368.4577 | ±736.9155 | -0.386 | 0.6994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **593**, R² = **0.1346**, Adj R² = **0.1182**, F-statistic = **8.22** (p = **1.86e-13**), Residual SE = **3712.126** on **581** df, AIC = **11442.9**, BIC = **11495.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17310.8127** | 1260.8379 | ±2521.6759 | **+13.730** | **6.75e-43** | *** |
| Education: graduate level (vs college) | -593.2115 | 313.1815 | ±626.3630 | -1.894 | 0.0582 | . |
| Education: high school or below (vs college) | +1355.1262 | 776.1060 | ±1552.2119 | +1.746 | 0.0808 | . |
| Site: UCSD (vs UAB) | -150.8911 | 419.4364 | ±838.8728 | -0.360 | 0.7190 |  |
| Site: UW (vs UAB) | -478.4559 | 402.3708 | ±804.7416 | -1.189 | 0.2344 |  |
| **Age (years)** | **-106.5054** | 15.1299 | ±30.2597 | **-7.039** | **1.93e-12** | *** |
| BMI (kg/m2) | -18.2068 | 25.1447 | ±50.2893 | -0.724 | 0.4690 |  |
| Hypertension | +268.7329 | 385.1777 | ±770.3555 | +0.698 | 0.4854 |  |
| High cholesterol | -232.7983 | 306.6463 | ±613.2926 | -0.759 | 0.4477 |  |
| Kidney disease | -610.8263 | 564.5797 | ±1129.1594 | -1.082 | 0.2793 |  |
| **Circulatory disease** | **-1013.4199** | 493.4754 | ±986.9508 | **-2.054** | **0.0400** | * |
| Time < 70 (%) | -110.8416 | 370.7164 | ±741.4328 | -0.299 | 0.7649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **593**, R² = **0.1348**, Adj R² = **0.1184**, F-statistic = **8.23** (p = **1.76e-13**), Residual SE = **3711.768** on **581** df, AIC = **11442.8**, BIC = **11495.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17316.7396** | 1258.9383 | ±2517.8766 | **+13.755** | **4.75e-43** | *** |
| Education: graduate level (vs college) | -598.6666 | 312.8213 | ±625.6426 | -1.914 | 0.0557 | . |
| Education: high school or below (vs college) | +1348.2542 | 776.0834 | ±1552.1668 | +1.737 | 0.0823 | . |
| Site: UCSD (vs UAB) | -145.2398 | 420.6501 | ±841.3002 | -0.345 | 0.7299 |  |
| Site: UW (vs UAB) | -478.1780 | 402.5600 | ±805.1199 | -1.188 | 0.2349 |  |
| **Age (years)** | **-106.4717** | 15.1188 | ±30.2376 | **-7.042** | **1.89e-12** | *** |
| BMI (kg/m2) | -18.2344 | 25.1544 | ±50.3087 | -0.725 | 0.4685 |  |
| Hypertension | +268.0523 | 385.2641 | ±770.5281 | +0.696 | 0.4866 |  |
| High cholesterol | -232.9887 | 306.7647 | ±613.5294 | -0.760 | 0.4476 |  |
| Kidney disease | -612.3782 | 564.3677 | ±1128.7353 | -1.085 | 0.2779 |  |
| **Circulatory disease** | **-1017.4472** | 493.3926 | ±986.7852 | **-2.062** | **0.0392** | * |
| Avg. daily time < 70 (%) | -142.2810 | 368.4577 | ±736.9155 | -0.386 | 0.6994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.570** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17272.2210** | 1250.7640 | ±2501.5280 | **+13.809** | **2.24e-43** | *** |
| Education: graduate level (vs college) | -579.3718 | 310.5592 | ±621.1185 | -1.866 | 0.0621 | . |
| Education: high school or below (vs college) | +1371.5824 | 779.0508 | ±1558.1016 | +1.761 | 0.0783 | . |
| Site: UCSD (vs UAB) | -155.1773 | 419.8789 | ±839.7577 | -0.370 | 0.7117 |  |
| Site: UW (vs UAB) | -478.1327 | 401.4145 | ±802.8290 | -1.191 | 0.2336 |  |
| **Age (years)** | **-106.5422** | 15.1010 | ±30.2021 | **-7.055** | **1.72e-12** | *** |
| BMI (kg/m2) | -18.1611 | 25.1980 | ±50.3961 | -0.721 | 0.4711 |  |
| Hypertension | +268.0746 | 385.2573 | ±770.5145 | +0.696 | 0.4865 |  |
| High cholesterol | -236.5256 | 308.5074 | ±617.0149 | -0.767 | 0.4433 |  |
| Kidney disease | -607.3370 | 566.1693 | ±1132.3387 | -1.073 | 0.2834 |  |
| **Circulatory disease** | **-1011.3613** | 493.2596 | ±986.5192 | **-2.050** | **0.0403** | * |
| Time 181-250, pooled (%) | +5.7904 | 58.1144 | ±116.2287 | +0.100 | 0.9206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.96e-13**), Residual SE = **3712.493** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17274.5278** | 1250.3118 | ±2500.6237 | **+13.816** | **2.04e-43** | *** |
| Education: graduate level (vs college) | -580.0356 | 310.5496 | ±621.0991 | -1.868 | 0.0618 | . |
| Education: high school or below (vs college) | +1372.4891 | 778.7394 | ±1557.4787 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -151.7535 | 420.1025 | ±840.2050 | -0.361 | 0.7179 |  |
| Site: UW (vs UAB) | -478.8121 | 401.7026 | ±803.4053 | -1.192 | 0.2333 |  |
| **Age (years)** | **-106.6204** | 15.0999 | ±30.1998 | **-7.061** | **1.65e-12** | *** |
| BMI (kg/m2) | -18.3068 | 25.2044 | ±50.4088 | -0.726 | 0.4676 |  |
| Hypertension | +268.4126 | 385.1995 | ±770.3990 | +0.697 | 0.4859 |  |
| High cholesterol | -238.3689 | 308.4745 | ±616.9490 | -0.773 | 0.4397 |  |
| Kidney disease | -609.1227 | 565.9292 | ±1131.8585 | -1.076 | 0.2818 |  |
| **Circulatory disease** | **-1014.7416** | 493.4852 | ±986.9704 | **-2.056** | **0.0398** | * |
| Avg. daily time 181-250 (%) | +10.6755 | 58.7609 | ±117.5217 | +0.182 | 0.8558 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1180**, F-statistic = **8.20** (p = **1.98e-13**), Residual SE = **3712.570** on **581** df, AIC = **11443.0**, BIC = **11495.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17272.2210** | 1250.7640 | ±2501.5280 | **+13.809** | **2.24e-43** | *** |
| Education: graduate level (vs college) | -579.3718 | 310.5592 | ±621.1185 | -1.866 | 0.0621 | . |
| Education: high school or below (vs college) | +1371.5824 | 779.0508 | ±1558.1016 | +1.761 | 0.0783 | . |
| Site: UCSD (vs UAB) | -155.1773 | 419.8789 | ±839.7577 | -0.370 | 0.7117 |  |
| Site: UW (vs UAB) | -478.1327 | 401.4145 | ±802.8290 | -1.191 | 0.2336 |  |
| **Age (years)** | **-106.5422** | 15.1010 | ±30.2021 | **-7.055** | **1.72e-12** | *** |
| BMI (kg/m2) | -18.1611 | 25.1980 | ±50.3961 | -0.721 | 0.4711 |  |
| Hypertension | +268.0746 | 385.2573 | ±770.5145 | +0.696 | 0.4865 |  |
| High cholesterol | -236.5256 | 308.5074 | ±617.0149 | -0.767 | 0.4433 |  |
| Kidney disease | -607.3370 | 566.1693 | ±1132.3387 | -1.073 | 0.2834 |  |
| **Circulatory disease** | **-1011.3613** | 493.2596 | ±986.5192 | **-2.050** | **0.0403** | * |
| Time > 180 (%) | +5.7904 | 58.1144 | ±116.2287 | +0.100 | 0.9206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.96e-13**), Residual SE = **3712.493** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17274.5278** | 1250.3118 | ±2500.6237 | **+13.816** | **2.04e-43** | *** |
| Education: graduate level (vs college) | -580.0356 | 310.5496 | ±621.0991 | -1.868 | 0.0618 | . |
| Education: high school or below (vs college) | +1372.4891 | 778.7394 | ±1557.4787 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -151.7535 | 420.1025 | ±840.2050 | -0.361 | 0.7179 |  |
| Site: UW (vs UAB) | -478.8121 | 401.7026 | ±803.4053 | -1.192 | 0.2333 |  |
| **Age (years)** | **-106.6204** | 15.0999 | ±30.1998 | **-7.061** | **1.65e-12** | *** |
| BMI (kg/m2) | -18.3068 | 25.2044 | ±50.4088 | -0.726 | 0.4676 |  |
| Hypertension | +268.4126 | 385.1995 | ±770.3990 | +0.697 | 0.4859 |  |
| High cholesterol | -238.3689 | 308.4745 | ±616.9490 | -0.773 | 0.4397 |  |
| Kidney disease | -609.1227 | 565.9292 | ±1131.8585 | -1.076 | 0.2818 |  |
| **Circulatory disease** | **-1014.7416** | 493.4852 | ±986.9704 | **-2.056** | **0.0398** | * |
| Avg. daily time > 180 (%) | +10.6755 | 58.7609 | ±117.5217 | +0.182 | 0.8558 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 593)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1344**, Adj R² = **0.1181**, F-statistic = **8.20** (p = **1.95e-13**), Residual SE = **3712.486** on **581** df, AIC = **11443.0**, BIC = **11495.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17268.7687** | 1253.3686 | ±2506.7372 | **+13.778** | **3.46e-43** | *** |
| Education: graduate level (vs college) | -579.6555 | 311.0459 | ±622.0917 | -1.864 | 0.0624 | . |
| Education: high school or below (vs college) | +1375.3347 | 780.4009 | ±1560.8017 | +1.762 | 0.0780 | . |
| Site: UCSD (vs UAB) | -162.6604 | 418.6330 | ±837.2660 | -0.389 | 0.6976 |  |
| Site: UW (vs UAB) | -474.1198 | 401.7627 | ±803.5253 | -1.180 | 0.2380 |  |
| **Age (years)** | **-106.5137** | 15.0772 | ±30.1543 | **-7.065** | **1.61e-12** | *** |
| BMI (kg/m2) | -17.5626 | 25.3574 | ±50.7149 | -0.693 | 0.4886 |  |
| Hypertension | +265.7215 | 385.5192 | ±771.0385 | +0.689 | 0.4907 |  |
| High cholesterol | -227.0618 | 313.6168 | ±627.2336 | -0.724 | 0.4691 |  |
| Kidney disease | -605.9547 | 566.2521 | ±1132.5041 | -1.070 | 0.2846 |  |
| **Circulatory disease** | **-1007.5507** | 498.0312 | ±996.0624 | **-2.023** | **0.0431** | * |
| Nocturnal time > 180 (%) | -9.3573 | 62.4517 | ±124.9034 | -0.150 | 0.8809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 593; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **593**, R² = **0.1461**, Adj R² = **0.1315**, F-statistic = **9.96** (p = **1.66e-15**), Residual SE = **11.523** on **582** df, AIC = **4592.7**, BIC = **4640.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7177** | 4.1331 | ±8.2662 | **+10.577** | **3.79e-26** | *** |
| Education: graduate level (vs college) | -1.5582 | 0.9653 | ±1.9306 | -1.614 | 0.1065 |  |
| Education: high school or below (vs college) | +3.0935 | 2.3519 | ±4.7038 | +1.315 | 0.1884 |  |
| Site: UCSD (vs UAB) | -0.4355 | 1.3278 | ±2.6555 | -0.328 | 0.7429 |  |
| Site: UW (vs UAB) | -1.0831 | 1.2291 | ±2.4583 | -0.881 | 0.3782 |  |
| **Age (years)** | **-0.3515** | 0.0455 | ±0.0910 | **-7.725** | **1.11e-14** | *** |
| BMI (kg/m2) | +0.0909 | 0.0839 | ±0.1678 | +1.083 | 0.2787 |  |
| Hypertension | +0.4547 | 1.1391 | ±2.2783 | +0.399 | 0.6898 |  |
| High cholesterol | -0.5058 | 0.9706 | ±1.9412 | -0.521 | 0.6023 |  |
| Kidney disease | -1.3642 | 1.8727 | ±3.7453 | -0.728 | 0.4663 |  |
| **Circulatory disease** | **-3.0418** | 1.4901 | ±2.9803 | **-2.041** | **0.0412** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **593**, R² = **0.1514**, Adj R² = **0.1353**, F-statistic = **9.42** (p = **1.06e-15**), Residual SE = **11.497** on **581** df, AIC = **4591.1**, BIC = **4643.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6503** | 8.8068 | ±17.6136 | **+3.367** | **7.61e-04** | *** |
| Education: graduate level (vs college) | -1.5907 | 0.9592 | ±1.9183 | -1.658 | 0.0972 | . |
| Education: high school or below (vs college) | +3.1101 | 2.3679 | ±4.7358 | +1.313 | 0.1890 |  |
| Site: UCSD (vs UAB) | -0.3797 | 1.3167 | ±2.6334 | -0.288 | 0.7731 |  |
| Site: UW (vs UAB) | -1.0921 | 1.2261 | ±2.4523 | -0.891 | 0.3731 |  |
| **Age (years)** | **-0.3629** | 0.0453 | ±0.0906 | **-8.012** | **1.12e-15** | *** |
| BMI (kg/m2) | +0.0712 | 0.0821 | ±0.1643 | +0.867 | 0.3860 |  |
| Hypertension | +0.3034 | 1.1361 | ±2.2722 | +0.267 | 0.7894 |  |
| High cholesterol | -0.7602 | 0.9979 | ±1.9958 | -0.762 | 0.4462 |  |
| Kidney disease | -1.3463 | 1.8517 | ±3.7033 | -0.727 | 0.4672 |  |
| **Circulatory disease** | **-3.0031** | 1.4772 | ±2.9544 | **-2.033** | **0.0421** | * |
| HbA1c (%) | +2.7735 | 1.5711 | ±3.1422 | +1.765 | 0.0775 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **593**, R² = **0.1463**, Adj R² = **0.1301**, F-statistic = **9.05** (p = **5.19e-15**), Residual SE = **11.531** on **581** df, AIC = **4594.6**, BIC = **4647.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2485** | 6.2202 | ±12.4404 | **+6.792** | **1.10e-11** | *** |
| Education: graduate level (vs college) | -1.5699 | 0.9663 | ±1.9327 | -1.625 | 0.1042 |  |
| Education: high school or below (vs college) | +3.0929 | 2.3526 | ±4.7052 | +1.315 | 0.1886 |  |
| Site: UCSD (vs UAB) | -0.4090 | 1.3252 | ±2.6503 | -0.309 | 0.7576 |  |
| Site: UW (vs UAB) | -1.1034 | 1.2322 | ±2.4643 | -0.896 | 0.3705 |  |
| **Age (years)** | **-0.3523** | 0.0454 | ±0.0909 | **-7.754** | **8.93e-15** | *** |
| BMI (kg/m2) | +0.0882 | 0.0842 | ±0.1683 | +1.048 | 0.2945 |  |
| Hypertension | +0.4364 | 1.1418 | ±2.2835 | +0.382 | 0.7023 |  |
| High cholesterol | -0.5133 | 0.9724 | ±1.9448 | -0.528 | 0.5976 |  |
| Kidney disease | -1.3922 | 1.8701 | ±3.7403 | -0.744 | 0.4566 |  |
| **Circulatory disease** | **-3.0618** | 1.5027 | ±3.0055 | **-2.037** | **0.0416** | * |
| Mean glucose (mg/dL) | +0.0135 | 0.0419 | ±0.0838 | +0.323 | 0.7466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **593**, R² = **0.1463**, Adj R² = **0.1301**, F-statistic = **9.05** (p = **5.19e-15**), Residual SE = **11.531** on **581** df, AIC = **4594.6**, BIC = **4647.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.3761** | 11.2351 | ±22.4701 | **+3.594** | **3.26e-04** | *** |
| Education: graduate level (vs college) | -1.5699 | 0.9663 | ±1.9327 | -1.625 | 0.1042 |  |
| Education: high school or below (vs college) | +3.0929 | 2.3526 | ±4.7052 | +1.315 | 0.1886 |  |
| Site: UCSD (vs UAB) | -0.4090 | 1.3252 | ±2.6503 | -0.309 | 0.7576 |  |
| Site: UW (vs UAB) | -1.1034 | 1.2322 | ±2.4643 | -0.896 | 0.3705 |  |
| **Age (years)** | **-0.3523** | 0.0454 | ±0.0909 | **-7.754** | **8.93e-15** | *** |
| BMI (kg/m2) | +0.0882 | 0.0842 | ±0.1683 | +1.048 | 0.2945 |  |
| Hypertension | +0.4364 | 1.1418 | ±2.2835 | +0.382 | 0.7023 |  |
| High cholesterol | -0.5133 | 0.9724 | ±1.9448 | -0.528 | 0.5976 |  |
| Kidney disease | -1.3922 | 1.8701 | ±3.7403 | -0.744 | 0.4566 |  |
| **Circulatory disease** | **-3.0618** | 1.5027 | ±3.0055 | **-2.037** | **0.0416** | * |
| GMI (%) | +0.5657 | 1.7507 | ±3.5014 | +0.323 | 0.7466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **593**, R² = **0.1461**, Adj R² = **0.1300**, F-statistic = **9.04** (p = **5.43e-15**), Residual SE = **11.532** on **581** df, AIC = **4594.7**, BIC = **4647.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6840** | 5.6141 | ±11.2281 | **+7.781** | **7.19e-15** | *** |
| Education: graduate level (vs college) | -1.5583 | 0.9667 | ±1.9333 | -1.612 | 0.1070 |  |
| Education: high school or below (vs college) | +3.0932 | 2.3552 | ±4.7103 | +1.313 | 0.1891 |  |
| Site: UCSD (vs UAB) | -0.4353 | 1.3287 | ±2.6573 | -0.328 | 0.7432 |  |
| Site: UW (vs UAB) | -1.0838 | 1.2324 | ±2.4649 | -0.879 | 0.3792 |  |
| **Age (years)** | **-0.3515** | 0.0456 | ±0.0912 | **-7.706** | **1.30e-14** | *** |
| BMI (kg/m2) | +0.0907 | 0.0868 | ±0.1737 | +1.045 | 0.2961 |  |
| Hypertension | +0.4545 | 1.1395 | ±2.2790 | +0.399 | 0.6900 |  |
| High cholesterol | -0.5063 | 0.9754 | ±1.9507 | -0.519 | 0.6037 |  |
| Kidney disease | -1.3645 | 1.8748 | ±3.7496 | -0.728 | 0.4667 |  |
| **Circulatory disease** | **-3.0421** | 1.4964 | ±2.9928 | **-2.033** | **0.0421** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0003 | 0.0370 | ±0.0740 | +0.008 | 0.9932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1486**, Adj R² = **0.1325**, F-statistic = **9.22** (p = **2.54e-15**), Residual SE = **11.516** on **581** df, AIC = **4593.0**, BIC = **4645.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.0011** | 4.5486 | ±9.0971 | **+9.014** | **1.99e-19** | *** |
| Education: graduate level (vs college) | -1.4712 | 0.9636 | ±1.9273 | -1.527 | 0.1268 |  |
| Education: high school or below (vs college) | +3.1099 | 2.3404 | ±4.6808 | +1.329 | 0.1839 |  |
| Site: UCSD (vs UAB) | -0.2866 | 1.3211 | ±2.6423 | -0.217 | 0.8282 |  |
| Site: UW (vs UAB) | -1.1552 | 1.2262 | ±2.4524 | -0.942 | 0.3461 |  |
| **Age (years)** | **-0.3579** | 0.0457 | ±0.0915 | **-7.826** | **5.05e-15** | *** |
| BMI (kg/m2) | +0.0869 | 0.0832 | ±0.1665 | +1.043 | 0.2968 |  |
| Hypertension | +0.3724 | 1.1371 | ±2.2741 | +0.328 | 0.7433 |  |
| High cholesterol | -0.5350 | 0.9708 | ±1.9416 | -0.551 | 0.5816 |  |
| Kidney disease | -1.4325 | 1.8778 | ±3.7555 | -0.763 | 0.4455 |  |
| **Circulatory disease** | **-3.0299** | 1.4921 | ±2.9841 | **-2.031** | **0.0423** | * |
| Glucose SD, pooled (mg/dL) | +0.1661 | 0.1274 | ±0.2547 | +1.304 | 0.1922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1481**, Adj R² = **0.1320**, F-statistic = **9.18** (p = **2.92e-15**), Residual SE = **11.519** on **581** df, AIC = **4593.3**, BIC = **4645.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.4922** | 4.5186 | ±9.0372 | **+9.182** | **4.21e-20** | *** |
| Education: graduate level (vs college) | -1.4992 | 0.9652 | ±1.9304 | -1.553 | 0.1204 |  |
| Education: high school or below (vs college) | +3.0989 | 2.3430 | ±4.6861 | +1.323 | 0.1860 |  |
| Site: UCSD (vs UAB) | -0.2818 | 1.3196 | ±2.6392 | -0.214 | 0.8309 |  |
| Site: UW (vs UAB) | -1.1460 | 1.2283 | ±2.4565 | -0.933 | 0.3508 |  |
| **Age (years)** | **-0.3575** | 0.0457 | ±0.0914 | **-7.820** | **5.29e-15** | *** |
| BMI (kg/m2) | +0.0863 | 0.0831 | ±0.1662 | +1.038 | 0.2992 |  |
| Hypertension | +0.3929 | 1.1392 | ±2.2784 | +0.345 | 0.7302 |  |
| High cholesterol | -0.5285 | 0.9712 | ±1.9425 | -0.544 | 0.5863 |  |
| Kidney disease | -1.4329 | 1.8728 | ±3.7457 | -0.765 | 0.4442 |  |
| **Circulatory disease** | **-3.0364** | 1.4926 | ±2.9851 | **-2.034** | **0.0419** | * |
| Avg. daily SD (mg/dL) | +0.1528 | 0.1310 | ±0.2619 | +1.167 | 0.2432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **593**, R² = **0.1477**, Adj R² = **0.1315**, F-statistic = **9.15** (p = **3.36e-15**), Residual SE = **11.522** on **581** df, AIC = **4593.6**, BIC = **4646.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.0011** | 4.7690 | ±9.5380 | **+8.597** | **8.15e-18** | *** |
| Education: graduate level (vs college) | -1.4536 | 0.9625 | ±1.9249 | -1.510 | 0.1310 |  |
| Education: high school or below (vs college) | +3.1146 | 2.3459 | ±4.6918 | +1.328 | 0.1843 |  |
| Site: UCSD (vs UAB) | -0.3462 | 1.3263 | ±2.6527 | -0.261 | 0.7941 |  |
| Site: UW (vs UAB) | -1.1094 | 1.2276 | ±2.4552 | -0.904 | 0.3662 |  |
| **Age (years)** | **-0.3556** | 0.0459 | ±0.0917 | **-7.754** | **8.90e-15** | *** |
| BMI (kg/m2) | +0.0922 | 0.0838 | ±0.1675 | +1.100 | 0.2712 |  |
| Hypertension | +0.4058 | 1.1377 | ±2.2755 | +0.357 | 0.7213 |  |
| High cholesterol | -0.5101 | 0.9718 | ±1.9436 | -0.525 | 0.5997 |  |
| Kidney disease | -1.3807 | 1.8834 | ±3.7669 | -0.733 | 0.4635 |  |
| **Circulatory disease** | **-2.9942** | 1.4875 | ±2.9750 | **-2.013** | **0.0441** | * |
| CV (%) | +0.1774 | 0.1694 | ±0.3388 | +1.047 | 0.2949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **593**, R² = **0.1475**, Adj R² = **0.1314**, F-statistic = **9.14** (p = **3.52e-15**), Residual SE = **11.523** on **581** df, AIC = **4593.7**, BIC = **4646.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5024** | 5.1409 | ±10.2818 | **+9.046** | **1.49e-19** | *** |
| Education: graduate level (vs college) | -1.4544 | 0.9621 | ±1.9243 | -1.512 | 0.1306 |  |
| Education: high school or below (vs college) | +3.1035 | 2.3445 | ±4.6890 | +1.324 | 0.1856 |  |
| Site: UCSD (vs UAB) | -0.3590 | 1.3253 | ±2.6506 | -0.271 | 0.7865 |  |
| Site: UW (vs UAB) | -1.1171 | 1.2270 | ±2.4541 | -0.910 | 0.3626 |  |
| **Age (years)** | **-0.3551** | 0.0459 | ±0.0917 | **-7.743** | **9.75e-15** | *** |
| BMI (kg/m2) | +0.0920 | 0.0838 | ±0.1677 | +1.098 | 0.2724 |  |
| Hypertension | +0.4097 | 1.1368 | ±2.2736 | +0.360 | 0.7186 |  |
| High cholesterol | -0.5064 | 0.9721 | ±1.9442 | -0.521 | 0.6024 |  |
| Kidney disease | -1.3825 | 1.8815 | ±3.7630 | -0.735 | 0.4625 |  |
| **Circulatory disease** | **-2.9920** | 1.4888 | ±2.9775 | **-2.010** | **0.0445** | * |
| Mean / SD ratio | -0.4172 | 0.4259 | ±0.8517 | -0.980 | 0.3272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **593**, R² = **0.1472**, Adj R² = **0.1310**, F-statistic = **9.12** (p = **3.90e-15**), Residual SE = **11.525** on **581** df, AIC = **4594.0**, BIC = **4646.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.0591** | 5.0506 | ±10.1012 | **+9.120** | **7.54e-20** | *** |
| Education: graduate level (vs college) | -1.4855 | 0.9646 | ±1.9292 | -1.540 | 0.1235 |  |
| Education: high school or below (vs college) | +3.0910 | 2.3466 | ±4.6933 | +1.317 | 0.1878 |  |
| Site: UCSD (vs UAB) | -0.3530 | 1.3229 | ±2.6457 | -0.267 | 0.7896 |  |
| Site: UW (vs UAB) | -1.1170 | 1.2288 | ±2.4576 | -0.909 | 0.3633 |  |
| **Age (years)** | **-0.3550** | 0.0459 | ±0.0919 | **-7.729** | **1.08e-14** | *** |
| BMI (kg/m2) | +0.0902 | 0.0838 | ±0.1675 | +1.077 | 0.2816 |  |
| Hypertension | +0.4399 | 1.1397 | ±2.2794 | +0.386 | 0.6995 |  |
| High cholesterol | -0.5048 | 0.9723 | ±1.9447 | -0.519 | 0.6036 |  |
| Kidney disease | -1.3885 | 1.8766 | ±3.7532 | -0.740 | 0.4593 |  |
| **Circulatory disease** | **-3.0026** | 1.4881 | ±2.9762 | **-2.018** | **0.0436** | * |
| Avg. daily mean/SD | -0.2992 | 0.3497 | ±0.6993 | -0.856 | 0.3922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **593**, R² = **0.1758**, Adj R² = **0.1602**, F-statistic = **11.27** (p = **4.22e-19**), Residual SE = **11.330** on **581** df, AIC = **4573.7**, BIC = **4626.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.0089** | 4.4636 | ±8.9272 | **+7.171** | **7.44e-13** | *** |
| Education: graduate level (vs college) | -1.4718 | 0.9443 | ±1.8886 | -1.559 | 0.1191 |  |
| Education: high school or below (vs college) | +2.4682 | 2.3244 | ±4.6487 | +1.062 | 0.2883 |  |
| Site: UCSD (vs UAB) | -0.1958 | 1.2995 | ±2.5989 | -0.151 | 0.8802 |  |
| Site: UW (vs UAB) | -1.0137 | 1.2034 | ±2.4068 | -0.842 | 0.3996 |  |
| **Age (years)** | **-0.3516** | 0.0448 | ±0.0897 | **-7.842** | **4.44e-15** | *** |
| BMI (kg/m2) | +0.0920 | 0.0787 | ±0.1574 | +1.169 | 0.2424 |  |
| Hypertension | +0.7400 | 1.1237 | ±2.2474 | +0.659 | 0.5102 |  |
| High cholesterol | -0.4996 | 0.9520 | ±1.9039 | -0.525 | 0.5997 |  |
| Kidney disease | -1.7868 | 1.8738 | ±3.7477 | -0.954 | 0.3403 |  |
| Circulatory disease | -2.6354 | 1.4796 | ±2.9593 | -1.781 | 0.0749 | . |
| **MAG (mg/dL/h)** | **+0.3204** | 0.0757 | ±0.1514 | **+4.232** | **2.31e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **593**, R² = **0.1524**, Adj R² = **0.1363**, F-statistic = **9.49** (p = **7.77e-16**), Residual SE = **11.490** on **581** df, AIC = **4590.4**, BIC = **4643.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.5776** | 4.8435 | ±9.6871 | **+7.965** | **1.66e-15** | *** |
| Education: graduate level (vs college) | -1.5167 | 0.9637 | ±1.9274 | -1.574 | 0.1155 |  |
| Education: high school or below (vs college) | +2.9882 | 2.3426 | ±4.6852 | +1.276 | 0.2021 |  |
| Site: UCSD (vs UAB) | -0.2695 | 1.3143 | ±2.6287 | -0.205 | 0.8375 |  |
| Site: UW (vs UAB) | -1.1955 | 1.2261 | ±2.4522 | -0.975 | 0.3295 |  |
| **Age (years)** | **-0.3602** | 0.0455 | ±0.0910 | **-7.918** | **2.41e-15** | *** |
| BMI (kg/m2) | +0.0970 | 0.0839 | ±0.1678 | +1.156 | 0.2476 |  |
| Hypertension | +0.4267 | 1.1402 | ±2.2804 | +0.374 | 0.7082 |  |
| High cholesterol | -0.4998 | 0.9683 | ±1.9366 | -0.516 | 0.6057 |  |
| Kidney disease | -1.5133 | 1.8597 | ±3.7194 | -0.814 | 0.4158 |  |
| **Circulatory disease** | **-3.0582** | 1.4872 | ±2.9744 | **-2.056** | **0.0398** | * |
| **Avg. daily range (mg/dL)** | **+0.0615** | 0.0304 | ±0.0608 | **+2.023** | **0.0431** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **593**, R² = **0.1533**, Adj R² = **0.1372**, F-statistic = **9.56** (p = **5.83e-16**), Residual SE = **11.484** on **581** df, AIC = **4589.7**, BIC = **4642.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.4404** | 4.0741 | ±8.1482 | **+10.172** | **2.65e-24** | *** |
| Education: graduate level (vs college) | -1.5445 | 0.9602 | ±1.9203 | -1.609 | 0.1077 |  |
| Education: high school or below (vs college) | +3.1332 | 2.3170 | ±4.6340 | +1.352 | 0.1763 |  |
| Site: UCSD (vs UAB) | -0.3466 | 1.3215 | ±2.6431 | -0.262 | 0.7931 |  |
| Site: UW (vs UAB) | -1.1155 | 1.2189 | ±2.4378 | -0.915 | 0.3601 |  |
| **Age (years)** | **-0.3507** | 0.0454 | ±0.0908 | **-7.724** | **1.13e-14** | *** |
| BMI (kg/m2) | +0.0733 | 0.0834 | ±0.1668 | +0.879 | 0.3794 |  |
| Hypertension | +0.4527 | 1.1287 | ±2.2575 | +0.401 | 0.6884 |  |
| High cholesterol | -0.6407 | 0.9669 | ±1.9338 | -0.663 | 0.5076 |  |
| Kidney disease | -1.3240 | 1.8573 | ±3.7145 | -0.713 | 0.4759 |  |
| **Circulatory disease** | **-3.0380** | 1.4915 | ±2.9831 | **-2.037** | **0.0417** | * |
| **SD of daily means (mg/dL)** | **+0.4762** | 0.2245 | ±0.4490 | **+2.121** | **0.0339** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **593**, R² = **0.1464**, Adj R² = **0.1303**, F-statistic = **9.06** (p = **4.93e-15**), Residual SE = **11.530** on **581** df, AIC = **4594.5**, BIC = **4647.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7413** | 15.9517 | ±31.9034 | **+3.244** | **0.0012** | ** |
| Education: graduate level (vs college) | -1.5550 | 0.9666 | ±1.9331 | -1.609 | 0.1077 |  |
| Education: high school or below (vs college) | +3.1126 | 2.3520 | ±4.7040 | +1.323 | 0.1857 |  |
| Site: UCSD (vs UAB) | -0.3937 | 1.3309 | ±2.6618 | -0.296 | 0.7674 |  |
| Site: UW (vs UAB) | -1.1025 | 1.2296 | ±2.4592 | -0.897 | 0.3699 |  |
| **Age (years)** | **-0.3531** | 0.0453 | ±0.0906 | **-7.792** | **6.58e-15** | *** |
| BMI (kg/m2) | +0.0894 | 0.0838 | ±0.1677 | +1.066 | 0.2862 |  |
| Hypertension | +0.4557 | 1.1407 | ±2.2815 | +0.400 | 0.6895 |  |
| High cholesterol | -0.5360 | 0.9730 | ±1.9460 | -0.551 | 0.5817 |  |
| Kidney disease | -1.3871 | 1.8667 | ±3.7334 | -0.743 | 0.4574 |  |
| **Circulatory disease** | **-3.0811** | 1.5027 | ±3.0054 | **-2.050** | **0.0403** | * |
| Time in range 70-180, pooled (%) | -0.0803 | 0.1569 | ±0.3138 | -0.512 | 0.6087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **593**, R² = **0.1467**, Adj R² = **0.1305**, F-statistic = **9.08** (p = **4.59e-15**), Residual SE = **11.529** on **581** df, AIC = **4594.3**, BIC = **4646.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6006** | 16.6998 | ±33.3996 | **+3.270** | **0.0011** | ** |
| Education: graduate level (vs college) | -1.5551 | 0.9662 | ±1.9324 | -1.609 | 0.1075 |  |
| Education: high school or below (vs college) | +3.1257 | 2.3518 | ±4.7035 | +1.329 | 0.1838 |  |
| Site: UCSD (vs UAB) | -0.3760 | 1.3309 | ±2.6618 | -0.283 | 0.7776 |  |
| Site: UW (vs UAB) | -1.1041 | 1.2294 | ±2.4587 | -0.898 | 0.3691 |  |
| **Age (years)** | **-0.3535** | 0.0453 | ±0.0907 | **-7.798** | **6.29e-15** | *** |
| BMI (kg/m2) | +0.0884 | 0.0837 | ±0.1674 | +1.056 | 0.2912 |  |
| Hypertension | +0.4593 | 1.1408 | ±2.2816 | +0.403 | 0.6873 |  |
| High cholesterol | -0.5470 | 0.9727 | ±1.9454 | -0.562 | 0.5739 |  |
| Kidney disease | -1.3968 | 1.8624 | ±3.7248 | -0.750 | 0.4533 |  |
| **Circulatory disease** | **-3.1008** | 1.5049 | ±3.0098 | **-2.060** | **0.0394** | * |
| Avg. daily time in range 70-180 (%) | -0.1088 | 0.1644 | ±0.3287 | -0.662 | 0.5080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **593**, R² = **0.1469**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.26e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.2**, BIC = **4646.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9517** | 4.1482 | ±8.2965 | **+10.595** | **3.13e-26** | *** |
| Education: graduate level (vs college) | -1.6422 | 0.9786 | ±1.9571 | -1.678 | 0.0933 | . |
| Education: high school or below (vs college) | +3.0004 | 2.3498 | ±4.6997 | +1.277 | 0.2017 |  |
| Site: UCSD (vs UAB) | -0.3904 | 1.3296 | ±2.6593 | -0.294 | 0.7690 |  |
| Site: UW (vs UAB) | -1.0938 | 1.2294 | ±2.4588 | -0.890 | 0.3737 |  |
| **Age (years)** | **-0.3520** | 0.0455 | ±0.0911 | **-7.729** | **1.09e-14** | *** |
| BMI (kg/m2) | +0.0899 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4592 | 1.1396 | ±2.2791 | +0.403 | 0.6870 |  |
| High cholesterol | -0.4962 | 0.9710 | ±1.9420 | -0.511 | 0.6093 |  |
| Kidney disease | -1.3959 | 1.8725 | ±3.7450 | -0.745 | 0.4560 |  |
| **Circulatory disease** | **-3.0720** | 1.4917 | ±2.9833 | **-2.059** | **0.0395** | * |
| Time 54-69, pooled (%) | -0.6485 | 0.8699 | ±1.7399 | -0.745 | 0.4560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1309**, F-statistic = **9.10** (p = **4.13e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9337** | 4.1444 | ±8.2887 | **+10.601** | **2.95e-26** | *** |
| Education: graduate level (vs college) | -1.6514 | 0.9783 | ±1.9567 | -1.688 | 0.0914 | . |
| Education: high school or below (vs college) | +2.9863 | 2.3521 | ±4.7043 | +1.270 | 0.2042 |  |
| Site: UCSD (vs UAB) | -0.3727 | 1.3304 | ±2.6608 | -0.280 | 0.7794 |  |
| Site: UW (vs UAB) | -1.0904 | 1.2296 | ±2.4592 | -0.887 | 0.3752 |  |
| **Age (years)** | **-0.3518** | 0.0455 | ±0.0911 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | +0.0900 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4552 | 1.1397 | ±2.2794 | +0.399 | 0.6896 |  |
| High cholesterol | -0.4990 | 0.9712 | ±1.9424 | -0.514 | 0.6074 |  |
| Kidney disease | -1.3970 | 1.8716 | ±3.7432 | -0.746 | 0.4554 |  |
| **Circulatory disease** | **-3.0850** | 1.4942 | ±2.9884 | **-2.065** | **0.0390** | * |
| Avg. daily time 54-69 (%) | -0.6693 | 0.8640 | ±1.7280 | -0.775 | 0.4385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **593**, R² = **0.1469**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.26e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.2**, BIC = **4646.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9517** | 4.1482 | ±8.2965 | **+10.595** | **3.13e-26** | *** |
| Education: graduate level (vs college) | -1.6422 | 0.9786 | ±1.9571 | -1.678 | 0.0933 | . |
| Education: high school or below (vs college) | +3.0004 | 2.3498 | ±4.6997 | +1.277 | 0.2017 |  |
| Site: UCSD (vs UAB) | -0.3904 | 1.3296 | ±2.6593 | -0.294 | 0.7690 |  |
| Site: UW (vs UAB) | -1.0938 | 1.2294 | ±2.4588 | -0.890 | 0.3737 |  |
| **Age (years)** | **-0.3520** | 0.0455 | ±0.0911 | **-7.729** | **1.09e-14** | *** |
| BMI (kg/m2) | +0.0899 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4592 | 1.1396 | ±2.2791 | +0.403 | 0.6870 |  |
| High cholesterol | -0.4962 | 0.9710 | ±1.9420 | -0.511 | 0.6093 |  |
| Kidney disease | -1.3959 | 1.8725 | ±3.7450 | -0.745 | 0.4560 |  |
| **Circulatory disease** | **-3.0720** | 1.4917 | ±2.9833 | **-2.059** | **0.0395** | * |
| Time < 70 (%) | -0.6485 | 0.8699 | ±1.7399 | -0.745 | 0.4560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1309**, F-statistic = **9.10** (p = **4.13e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9337** | 4.1444 | ±8.2887 | **+10.601** | **2.95e-26** | *** |
| Education: graduate level (vs college) | -1.6514 | 0.9783 | ±1.9567 | -1.688 | 0.0914 | . |
| Education: high school or below (vs college) | +2.9863 | 2.3521 | ±4.7043 | +1.270 | 0.2042 |  |
| Site: UCSD (vs UAB) | -0.3727 | 1.3304 | ±2.6608 | -0.280 | 0.7794 |  |
| Site: UW (vs UAB) | -1.0904 | 1.2296 | ±2.4592 | -0.887 | 0.3752 |  |
| **Age (years)** | **-0.3518** | 0.0455 | ±0.0911 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | +0.0900 | 0.0840 | ±0.1680 | +1.071 | 0.2842 |  |
| Hypertension | +0.4552 | 1.1397 | ±2.2794 | +0.399 | 0.6896 |  |
| High cholesterol | -0.4990 | 0.9712 | ±1.9424 | -0.514 | 0.6074 |  |
| Kidney disease | -1.3970 | 1.8716 | ±3.7432 | -0.746 | 0.4554 |  |
| **Circulatory disease** | **-3.0850** | 1.4942 | ±2.9884 | **-2.065** | **0.0390** | * |
| Avg. daily time < 70 (%) | -0.6693 | 0.8640 | ±1.7280 | -0.775 | 0.4385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **593**, R² = **0.1467**, Adj R² = **0.1305**, F-statistic = **9.08** (p = **4.60e-15**), Residual SE = **11.529** on **581** df, AIC = **4594.3**, BIC = **4647.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7427** | 4.1239 | ±8.2478 | **+10.607** | **2.76e-26** | *** |
| Education: graduate level (vs college) | -1.5675 | 0.9652 | ±1.9304 | -1.624 | 0.1044 |  |
| Education: high school or below (vs college) | +3.1033 | 2.3504 | ±4.7009 | +1.320 | 0.1867 |  |
| Site: UCSD (vs UAB) | -0.3740 | 1.3304 | ±2.6607 | -0.281 | 0.7786 |  |
| Site: UW (vs UAB) | -1.1100 | 1.2294 | ±2.4588 | -0.903 | 0.3666 |  |
| **Age (years)** | **-0.3536** | 0.0453 | ±0.0906 | **-7.806** | **5.91e-15** | *** |
| BMI (kg/m2) | +0.0888 | 0.0838 | ±0.1675 | +1.060 | 0.2889 |  |
| Hypertension | +0.4568 | 1.1408 | ±2.2815 | +0.400 | 0.6889 |  |
| High cholesterol | -0.5435 | 0.9732 | ±1.9464 | -0.558 | 0.5766 |  |
| Kidney disease | -1.3989 | 1.8644 | ±3.7287 | -0.750 | 0.4530 |  |
| **Circulatory disease** | **-3.0975** | 1.5043 | ±3.0087 | **-2.059** | **0.0395** | * |
| Time 181-250, pooled (%) | +0.1041 | 0.1562 | ±0.3124 | +0.667 | 0.5051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.16e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7649** | 4.1168 | ±8.2336 | **+10.631** | **2.14e-26** | *** |
| Education: graduate level (vs college) | -1.5733 | 0.9649 | ±1.9298 | -1.630 | 0.1030 |  |
| Education: high school or below (vs college) | +3.1120 | 2.3490 | ±4.6980 | +1.325 | 0.1852 |  |
| Site: UCSD (vs UAB) | -0.3481 | 1.3304 | ±2.6609 | -0.262 | 0.7936 |  |
| Site: UW (vs UAB) | -1.1109 | 1.2292 | ±2.4584 | -0.904 | 0.3661 |  |
| **Age (years)** | **-0.3540** | 0.0453 | ±0.0906 | **-7.812** | **5.61e-15** | *** |
| BMI (kg/m2) | +0.0876 | 0.0836 | ±0.1672 | +1.047 | 0.2950 |  |
| Hypertension | +0.4605 | 1.1407 | ±2.2815 | +0.404 | 0.6865 |  |
| High cholesterol | -0.5561 | 0.9728 | ±1.9456 | -0.572 | 0.5676 |  |
| Kidney disease | -1.4117 | 1.8590 | ±3.7180 | -0.759 | 0.4476 |  |
| **Circulatory disease** | **-3.1245** | 1.5077 | ±3.0153 | **-2.072** | **0.0382** | * |
| Avg. daily time 181-250 (%) | +0.1363 | 0.1636 | ±0.3272 | +0.833 | 0.4047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **593**, R² = **0.1467**, Adj R² = **0.1305**, F-statistic = **9.08** (p = **4.60e-15**), Residual SE = **11.529** on **581** df, AIC = **4594.3**, BIC = **4647.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7427** | 4.1239 | ±8.2478 | **+10.607** | **2.76e-26** | *** |
| Education: graduate level (vs college) | -1.5675 | 0.9652 | ±1.9304 | -1.624 | 0.1044 |  |
| Education: high school or below (vs college) | +3.1033 | 2.3504 | ±4.7009 | +1.320 | 0.1867 |  |
| Site: UCSD (vs UAB) | -0.3740 | 1.3304 | ±2.6607 | -0.281 | 0.7786 |  |
| Site: UW (vs UAB) | -1.1100 | 1.2294 | ±2.4588 | -0.903 | 0.3666 |  |
| **Age (years)** | **-0.3536** | 0.0453 | ±0.0906 | **-7.806** | **5.91e-15** | *** |
| BMI (kg/m2) | +0.0888 | 0.0838 | ±0.1675 | +1.060 | 0.2889 |  |
| Hypertension | +0.4568 | 1.1408 | ±2.2815 | +0.400 | 0.6889 |  |
| High cholesterol | -0.5435 | 0.9732 | ±1.9464 | -0.558 | 0.5766 |  |
| Kidney disease | -1.3989 | 1.8644 | ±3.7287 | -0.750 | 0.4530 |  |
| **Circulatory disease** | **-3.0975** | 1.5043 | ±3.0087 | **-2.059** | **0.0395** | * |
| Time > 180 (%) | +0.1041 | 0.1562 | ±0.3124 | +0.667 | 0.5051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1470**, Adj R² = **0.1308**, F-statistic = **9.10** (p = **4.16e-15**), Residual SE = **11.527** on **581** df, AIC = **4594.1**, BIC = **4646.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7649** | 4.1168 | ±8.2336 | **+10.631** | **2.14e-26** | *** |
| Education: graduate level (vs college) | -1.5733 | 0.9649 | ±1.9298 | -1.630 | 0.1030 |  |
| Education: high school or below (vs college) | +3.1120 | 2.3490 | ±4.6980 | +1.325 | 0.1852 |  |
| Site: UCSD (vs UAB) | -0.3481 | 1.3304 | ±2.6609 | -0.262 | 0.7936 |  |
| Site: UW (vs UAB) | -1.1109 | 1.2292 | ±2.4584 | -0.904 | 0.3661 |  |
| **Age (years)** | **-0.3540** | 0.0453 | ±0.0906 | **-7.812** | **5.61e-15** | *** |
| BMI (kg/m2) | +0.0876 | 0.0836 | ±0.1672 | +1.047 | 0.2950 |  |
| Hypertension | +0.4605 | 1.1407 | ±2.2815 | +0.404 | 0.6865 |  |
| High cholesterol | -0.5561 | 0.9728 | ±1.9456 | -0.572 | 0.5676 |  |
| Kidney disease | -1.4117 | 1.8590 | ±3.7180 | -0.759 | 0.4476 |  |
| **Circulatory disease** | **-3.1245** | 1.5077 | ±3.0153 | **-2.072** | **0.0382** | * |
| Avg. daily time > 180 (%) | +0.1363 | 0.1636 | ±0.3272 | +0.833 | 0.4047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 593)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **593**, R² = **0.1463**, Adj R² = **0.1301**, F-statistic = **9.05** (p = **5.21e-15**), Residual SE = **11.532** on **581** df, AIC = **4594.6**, BIC = **4647.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7077** | 4.1456 | ±8.2912 | **+10.543** | **5.46e-26** | *** |
| Education: graduate level (vs college) | -1.5621 | 0.9667 | ±1.9334 | -1.616 | 0.1061 |  |
| Education: high school or below (vs college) | +3.1144 | 2.3587 | ±4.7174 | +1.320 | 0.1867 |  |
| Site: UCSD (vs UAB) | -0.4553 | 1.3289 | ±2.6577 | -0.343 | 0.7319 |  |
| Site: UW (vs UAB) | -1.0709 | 1.2308 | ±2.4615 | -0.870 | 0.3842 |  |
| **Age (years)** | **-0.3520** | 0.0456 | ±0.0911 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | +0.0932 | 0.0850 | ±0.1699 | +1.097 | 0.2726 |  |
| Hypertension | +0.4438 | 1.1429 | ±2.2859 | +0.388 | 0.6978 |  |
| High cholesterol | -0.4700 | 0.9777 | ±1.9555 | -0.481 | 0.6307 |  |
| Kidney disease | -1.3669 | 1.8773 | ±3.7547 | -0.728 | 0.4666 |  |
| **Circulatory disease** | **-3.0383** | 1.4910 | ±2.9820 | **-2.038** | **0.0416** | * |
| Nocturnal time > 180 (%) | -0.0454 | 0.1410 | ±0.2821 | -0.322 | 0.7474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 597; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **597**, R² = **0.1491**, Adj R² = **0.1345**, F-statistic = **10.26** (p = **4.91e-16**), Residual SE = **7.427** on **586** df, AIC = **4099.2**, BIC = **4147.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3247** | 3.3385 | ±6.6770 | **+17.770** | **1.21e-70** | *** |
| **Education: graduate level (vs college)** | **-1.7318** | 0.6709 | ±1.3418 | **-2.581** | **0.0098** | ** |
| Education: high school or below (vs college) | -1.1250 | 1.1380 | ±2.2760 | -0.989 | 0.3229 |  |
| Site: UCSD (vs UAB) | -1.5464 | 0.8355 | ±1.6710 | -1.851 | 0.0642 | . |
| **Site: UW (vs UAB)** | **-1.7085** | 0.7873 | ±1.5747 | **-2.170** | **0.0300** | * |
| **Age (years)** | **-0.1047** | 0.0310 | ±0.0620 | **-3.375** | **7.39e-04** | *** |
| **BMI (kg/m2)** | **+0.3104** | 0.0681 | ±0.1362 | **+4.559** | **5.13e-06** | *** |
| Hypertension | +0.7130 | 0.7483 | ±1.4967 | +0.953 | 0.3407 |  |
| High cholesterol | -0.7516 | 0.6361 | ±1.2723 | -1.182 | 0.2374 |  |
| Kidney disease | +0.7480 | 1.2321 | ±2.4642 | +0.607 | 0.5438 |  |
| Circulatory disease | -0.4494 | 0.9357 | ±1.8714 | -0.480 | 0.6310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **597**, R² = **0.1562**, Adj R² = **0.1403**, F-statistic = **9.84** (p = **1.72e-16**), Residual SE = **7.402** on **585** df, AIC = **4096.2**, BIC = **4148.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7437** | 5.3637 | ±10.7275 | **+9.088** | **1.01e-19** | *** |
| **Education: graduate level (vs college)** | **-1.7530** | 0.6644 | ±1.3289 | **-2.638** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.1086 | 1.1457 | ±2.2914 | -0.968 | 0.3332 |  |
| Site: UCSD (vs UAB) | -1.5159 | 0.8245 | ±1.6490 | -1.839 | 0.0660 | . |
| **Site: UW (vs UAB)** | **-1.7166** | 0.7823 | ±1.5645 | **-2.194** | **0.0282** | * |
| **Age (years)** | **-0.1129** | 0.0314 | ±0.0627 | **-3.600** | **3.18e-04** | *** |
| **BMI (kg/m2)** | **+0.2949** | 0.0664 | ±0.1328 | **+4.440** | **8.99e-06** | *** |
| Hypertension | +0.6001 | 0.7490 | ±1.4980 | +0.801 | 0.4230 |  |
| High cholesterol | -0.9383 | 0.6282 | ±1.2564 | -1.494 | 0.1353 |  |
| Kidney disease | +0.7623 | 1.1958 | ±2.3917 | +0.637 | 0.5238 |  |
| Circulatory disease | -0.4145 | 0.9214 | ±1.8428 | -0.450 | 0.6528 |  |
| **HbA1c (%)** | **+2.0870** | 0.9855 | ±1.9711 | **+2.118** | **0.0342** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **597**, R² = **0.1595**, Adj R² = **0.1437**, F-statistic = **10.09** (p = **5.91e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.8**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2431** | 4.0523 | ±8.1046 | **+12.645** | **1.19e-36** | *** |
| **Education: graduate level (vs college)** | **-1.7918** | 0.6673 | ±1.3346 | **-2.685** | **0.0073** | ** |
| Education: high school or below (vs college) | -1.1240 | 1.1155 | ±2.2310 | -1.008 | 0.3137 |  |
| Site: UCSD (vs UAB) | -1.4097 | 0.8242 | ±1.6484 | -1.710 | 0.0872 | . |
| **Site: UW (vs UAB)** | **-1.8287** | 0.7809 | ±1.5617 | **-2.342** | **0.0192** | * |
| **Age (years)** | **-0.1087** | 0.0307 | ±0.0614 | **-3.538** | **4.03e-04** | *** |
| **BMI (kg/m2)** | **+0.2955** | 0.0665 | ±0.1330 | **+4.445** | **8.80e-06** | *** |
| Hypertension | +0.6009 | 0.7466 | ±1.4933 | +0.805 | 0.4209 |  |
| High cholesterol | -0.7904 | 0.6341 | ±1.2682 | -1.246 | 0.2126 |  |
| Kidney disease | +0.5959 | 1.2256 | ±2.4513 | +0.486 | 0.6268 |  |
| Circulatory disease | -0.5664 | 0.9291 | ±1.8583 | -0.610 | 0.5421 |  |
| **Mean glucose (mg/dL)** | **+0.0745** | 0.0254 | ±0.0508 | **+2.934** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **597**, R² = **0.1595**, Adj R² = **0.1437**, F-statistic = **10.09** (p = **5.91e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.8**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9339** | 6.7861 | ±13.5721 | **+6.032** | **1.62e-09** | *** |
| **Education: graduate level (vs college)** | **-1.7918** | 0.6673 | ±1.3346 | **-2.685** | **0.0073** | ** |
| Education: high school or below (vs college) | -1.1240 | 1.1155 | ±2.2310 | -1.008 | 0.3137 |  |
| Site: UCSD (vs UAB) | -1.4097 | 0.8242 | ±1.6484 | -1.710 | 0.0872 | . |
| **Site: UW (vs UAB)** | **-1.8287** | 0.7809 | ±1.5617 | **-2.342** | **0.0192** | * |
| **Age (years)** | **-0.1087** | 0.0307 | ±0.0614 | **-3.538** | **4.03e-04** | *** |
| **BMI (kg/m2)** | **+0.2955** | 0.0665 | ±0.1330 | **+4.445** | **8.80e-06** | *** |
| Hypertension | +0.6009 | 0.7466 | ±1.4933 | +0.805 | 0.4209 |  |
| High cholesterol | -0.7904 | 0.6341 | ±1.2682 | -1.246 | 0.2126 |  |
| Kidney disease | +0.5959 | 1.2256 | ±2.4513 | +0.486 | 0.6268 |  |
| Circulatory disease | -0.5664 | 0.9291 | ±1.8583 | -0.610 | 0.5421 |  |
| **GMI (%)** | **+3.1146** | 1.0615 | ±2.1230 | **+2.934** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **597**, R² = **0.1629**, Adj R² = **0.1472**, F-statistic = **10.35** (p = **1.98e-17**), Residual SE = **7.372** on **585** df, AIC = **4091.4**, BIC = **4144.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2844** | 3.5806 | ±7.1612 | **+14.323** | **1.57e-46** | *** |
| **Education: graduate level (vs college)** | **-1.7586** | 0.6631 | ±1.3261 | **-2.652** | **0.0080** | ** |
| Education: high school or below (vs college) | -1.1810 | 1.1170 | ±2.2340 | -1.057 | 0.2904 |  |
| Site: UCSD (vs UAB) | -1.5122 | 0.8248 | ±1.6496 | -1.833 | 0.0667 | . |
| **Site: UW (vs UAB)** | **-1.8720** | 0.7789 | ±1.5578 | **-2.403** | **0.0162** | * |
| **Age (years)** | **-0.1010** | 0.0305 | ±0.0610 | **-3.312** | **9.27e-04** | *** |
| **BMI (kg/m2)** | **+0.2782** | 0.0651 | ±0.1301 | **+4.276** | **1.90e-05** | *** |
| Hypertension | +0.6371 | 0.7429 | ±1.4858 | +0.858 | 0.3911 |  |
| High cholesterol | -0.8721 | 0.6329 | ±1.2658 | -1.378 | 0.1682 |  |
| Kidney disease | +0.6744 | 1.2073 | ±2.4146 | +0.559 | 0.5764 |  |
| Circulatory disease | -0.5266 | 0.9248 | ±1.8496 | -0.569 | 0.5691 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0750** | 0.0223 | ±0.0445 | **+3.368** | **7.58e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **597**, R² = **0.1538**, Adj R² = **0.1379**, F-statistic = **9.66** (p = **3.66e-16**), Residual SE = **7.412** on **585** df, AIC = **4097.9**, BIC = **4150.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9026** | 3.3928 | ±6.7856 | **+16.772** | **3.93e-63** | *** |
| **Education: graduate level (vs college)** | **-1.6506** | 0.6671 | ±1.3343 | **-2.474** | **0.0134** | * |
| Education: high school or below (vs college) | -1.1108 | 1.1299 | ±2.2597 | -0.983 | 0.3256 |  |
| Site: UCSD (vs UAB) | -1.4250 | 0.8304 | ±1.6608 | -1.716 | 0.0862 | . |
| **Site: UW (vs UAB)** | **-1.7819** | 0.7860 | ±1.5719 | **-2.267** | **0.0234** | * |
| **Age (years)** | **-0.1101** | 0.0316 | ±0.0633 | **-3.482** | **4.98e-04** | *** |
| **BMI (kg/m2)** | **+0.3065** | 0.0669 | ±0.1339 | **+4.579** | **4.67e-06** | *** |
| Hypertension | +0.6297 | 0.7477 | ±1.4953 | +0.842 | 0.3997 |  |
| High cholesterol | -0.7699 | 0.6356 | ±1.2711 | -1.211 | 0.2258 |  |
| Kidney disease | +0.6850 | 1.2377 | ±2.4755 | +0.553 | 0.5800 |  |
| Circulatory disease | -0.4345 | 0.9247 | ±1.8494 | -0.470 | 0.6384 |  |
| Glucose SD, pooled (mg/dL) | +0.1485 | 0.0876 | ±0.1752 | +1.695 | 0.0901 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **597**, R² = **0.1540**, Adj R² = **0.1381**, F-statistic = **9.68** (p = **3.40e-16**), Residual SE = **7.411** on **585** df, AIC = **4097.7**, BIC = **4150.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.0770** | 3.3594 | ±6.7188 | **+16.990** | **9.69e-65** | *** |
| **Education: graduate level (vs college)** | **-1.6678** | 0.6678 | ±1.3356 | **-2.497** | **0.0125** | * |
| Education: high school or below (vs college) | -1.1192 | 1.1289 | ±2.2578 | -0.991 | 0.3215 |  |
| Site: UCSD (vs UAB) | -1.4046 | 0.8278 | ±1.6555 | -1.697 | 0.0897 | . |
| **Site: UW (vs UAB)** | **-1.7823** | 0.7878 | ±1.5757 | **-2.262** | **0.0237** | * |
| **Age (years)** | **-0.1104** | 0.0316 | ±0.0631 | **-3.498** | **4.69e-04** | *** |
| **BMI (kg/m2)** | **+0.3053** | 0.0667 | ±0.1335 | **+4.574** | **4.78e-06** | *** |
| Hypertension | +0.6397 | 0.7514 | ±1.5029 | +0.851 | 0.3946 |  |
| High cholesterol | -0.7659 | 0.6355 | ±1.2709 | -1.205 | 0.2281 |  |
| Kidney disease | +0.6766 | 1.2378 | ±2.4757 | +0.547 | 0.5847 |  |
| Circulatory disease | -0.4394 | 0.9261 | ±1.8522 | -0.475 | 0.6351 |  |
| Avg. daily SD (mg/dL) | +0.1549 | 0.0898 | ±0.1796 | +1.725 | 0.0846 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **597**, R² = **0.1493**, Adj R² = **0.1333**, F-statistic = **9.33** (p = **1.50e-15**), Residual SE = **7.432** on **585** df, AIC = **4101.0**, BIC = **4153.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6069** | 3.6218 | ±7.2437 | **+16.182** | **6.80e-59** | *** |
| **Education: graduate level (vs college)** | **-1.7036** | 0.6729 | ±1.3458 | **-2.532** | **0.0114** | * |
| Education: high school or below (vs college) | -1.1200 | 1.1384 | ±2.2769 | -0.984 | 0.3252 |  |
| Site: UCSD (vs UAB) | -1.5250 | 0.8362 | ±1.6724 | -1.824 | 0.0682 | . |
| **Site: UW (vs UAB)** | **-1.7173** | 0.7889 | ±1.5777 | **-2.177** | **0.0295** | * |
| **Age (years)** | **-0.1057** | 0.0316 | ±0.0632 | **-3.344** | **8.25e-04** | *** |
| **BMI (kg/m2)** | **+0.3107** | 0.0680 | ±0.1360 | **+4.569** | **4.91e-06** | *** |
| Hypertension | +0.6984 | 0.7471 | ±1.4941 | +0.935 | 0.3499 |  |
| High cholesterol | -0.7509 | 0.6375 | ±1.2749 | -1.178 | 0.2388 |  |
| Kidney disease | +0.7430 | 1.2372 | ±2.4744 | +0.601 | 0.5482 |  |
| Circulatory disease | -0.4353 | 0.9358 | ±1.8716 | -0.465 | 0.6418 |  |
| CV (%) | +0.0470 | 0.1178 | ±0.2355 | +0.399 | 0.6901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **597**, R² = **0.1492**, Adj R² = **0.1332**, F-statistic = **9.32** (p = **1.57e-15**), Residual SE = **7.433** on **585** df, AIC = **4101.1**, BIC = **4153.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.8266** | 3.9176 | ±7.8353 | **+15.271** | **1.19e-52** | *** |
| **Education: graduate level (vs college)** | **-1.7123** | 0.6732 | ±1.3465 | **-2.543** | **0.0110** | * |
| Education: high school or below (vs college) | -1.1235 | 1.1385 | ±2.2769 | -0.987 | 0.3237 |  |
| Site: UCSD (vs UAB) | -1.5349 | 0.8364 | ±1.6728 | -1.835 | 0.0665 | . |
| **Site: UW (vs UAB)** | **-1.7167** | 0.7893 | ±1.5787 | **-2.175** | **0.0296** | * |
| **Age (years)** | **-0.1052** | 0.0314 | ±0.0628 | **-3.351** | **8.05e-04** | *** |
| **BMI (kg/m2)** | **+0.3106** | 0.0681 | ±0.1361 | **+4.564** | **5.03e-06** | *** |
| Hypertension | +0.7032 | 0.7470 | ±1.4940 | +0.941 | 0.3465 |  |
| High cholesterol | -0.7501 | 0.6377 | ±1.2753 | -1.176 | 0.2394 |  |
| Kidney disease | +0.7441 | 1.2372 | ±2.4744 | +0.601 | 0.5476 |  |
| Circulatory disease | -0.4398 | 0.9372 | ±1.8744 | -0.469 | 0.6388 |  |
| Mean / SD ratio | -0.0751 | 0.2663 | ±0.5327 | -0.282 | 0.7780 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **597**, R² = **0.1495**, Adj R² = **0.1335**, F-statistic = **9.35** (p = **1.42e-15**), Residual SE = **7.431** on **585** df, AIC = **4100.9**, BIC = **4153.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.2754** | 3.8717 | ±7.7434 | **+15.568** | **1.20e-54** | *** |
| **Education: graduate level (vs college)** | **-1.7003** | 0.6733 | ±1.3466 | **-2.525** | **0.0116** | * |
| Education: high school or below (vs college) | -1.1264 | 1.1374 | ±2.2748 | -0.990 | 0.3220 |  |
| Site: UCSD (vs UAB) | -1.5189 | 0.8356 | ±1.6712 | -1.818 | 0.0691 | . |
| **Site: UW (vs UAB)** | **-1.7271** | 0.7907 | ±1.5814 | **-2.184** | **0.0289** | * |
| **Age (years)** | **-0.1059** | 0.0314 | ±0.0628 | **-3.376** | **7.36e-04** | *** |
| **BMI (kg/m2)** | **+0.3100** | 0.0679 | ±0.1359 | **+4.563** | **5.03e-06** | *** |
| Hypertension | +0.7032 | 0.7495 | ±1.4990 | +0.938 | 0.3482 |  |
| High cholesterol | -0.7475 | 0.6379 | ±1.2757 | -1.172 | 0.2412 |  |
| Kidney disease | +0.7368 | 1.2373 | ±2.4745 | +0.595 | 0.5515 |  |
| Circulatory disease | -0.4324 | 0.9358 | ±1.8716 | -0.462 | 0.6440 |  |
| Avg. daily mean/SD | -0.1212 | 0.2163 | ±0.4326 | -0.561 | 0.5751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **597**, R² = **0.1635**, Adj R² = **0.1478**, F-statistic = **10.39** (p = **1.64e-17**), Residual SE = **7.370** on **585** df, AIC = **4091.0**, BIC = **4143.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.0784** | 3.4842 | ±6.9683 | **+15.521** | **2.49e-54** | *** |
| **Education: graduate level (vs college)** | **-1.6808** | 0.6602 | ±1.3204 | **-2.546** | **0.0109** | * |
| Education: high school or below (vs college) | -1.3960 | 1.1350 | ±2.2700 | -1.230 | 0.2187 |  |
| Site: UCSD (vs UAB) | -1.4430 | 0.8290 | ±1.6580 | -1.741 | 0.0817 | . |
| **Site: UW (vs UAB)** | **-1.7003** | 0.7829 | ±1.5658 | **-2.172** | **0.0299** | * |
| **Age (years)** | **-0.1044** | 0.0307 | ±0.0613 | **-3.405** | **6.62e-04** | *** |
| **BMI (kg/m2)** | **+0.3113** | 0.0650 | ±0.1301 | **+4.786** | **1.70e-06** | *** |
| Hypertension | +0.8244 | 0.7494 | ±1.4988 | +1.100 | 0.2713 |  |
| High cholesterol | -0.7584 | 0.6320 | ±1.2641 | -1.200 | 0.2302 |  |
| Kidney disease | +0.5613 | 1.2219 | ±2.4439 | +0.459 | 0.6460 |  |
| Circulatory disease | -0.3181 | 0.9224 | ±1.8448 | -0.345 | 0.7302 |  |
| **MAG (mg/dL/h)** | **+0.1433** | 0.0515 | ±0.1030 | **+2.781** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **597**, R² = **0.1532**, Adj R² = **0.1373**, F-statistic = **9.62** (p = **4.36e-16**), Residual SE = **7.415** on **585** df, AIC = **4098.2**, BIC = **4150.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6292** | 3.6302 | ±7.2604 | **+15.599** | **7.34e-55** | *** |
| **Education: graduate level (vs college)** | **-1.7043** | 0.6692 | ±1.3385 | **-2.547** | **0.0109** | * |
| Education: high school or below (vs college) | -1.1781 | 1.1349 | ±2.2697 | -1.038 | 0.2992 |  |
| Site: UCSD (vs UAB) | -1.4733 | 0.8334 | ±1.6668 | -1.768 | 0.0771 | . |
| **Site: UW (vs UAB)** | **-1.7792** | 0.7882 | ±1.5764 | **-2.257** | **0.0240** | * |
| **Age (years)** | **-0.1089** | 0.0313 | ±0.0627 | **-3.477** | **5.08e-04** | *** |
| **BMI (kg/m2)** | **+0.3132** | 0.0679 | ±0.1357 | **+4.615** | **3.94e-06** | *** |
| Hypertension | +0.6866 | 0.7515 | ±1.5030 | +0.914 | 0.3609 |  |
| High cholesterol | -0.7415 | 0.6368 | ±1.2736 | -1.164 | 0.2443 |  |
| Kidney disease | +0.6689 | 1.2390 | ±2.4779 | +0.540 | 0.5893 |  |
| Circulatory disease | -0.4598 | 0.9258 | ±1.8517 | -0.497 | 0.6195 |  |
| Avg. daily range (mg/dL) | +0.0324 | 0.0199 | ±0.0398 | +1.626 | 0.1040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **597**, R² = **0.1600**, Adj R² = **0.1442**, F-statistic = **10.13** (p = **5.12e-17**), Residual SE = **7.385** on **585** df, AIC = **4093.5**, BIC = **4146.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.5097** | 3.1894 | ±6.3787 | **+18.032** | **1.10e-72** | *** |
| **Education: graduate level (vs college)** | **-1.7206** | 0.6642 | ±1.3283 | **-2.591** | **0.0096** | ** |
| Education: high school or below (vs college) | -1.0935 | 1.1155 | ±2.2311 | -0.980 | 0.3269 |  |
| Site: UCSD (vs UAB) | -1.4722 | 0.8320 | ±1.6640 | -1.769 | 0.0768 | . |
| **Site: UW (vs UAB)** | **-1.7386** | 0.7742 | ±1.5485 | **-2.246** | **0.0247** | * |
| **Age (years)** | **-0.1041** | 0.0306 | ±0.0612 | **-3.402** | **6.68e-04** | *** |
| **BMI (kg/m2)** | **+0.2968** | 0.0663 | ±0.1325 | **+4.479** | **7.49e-06** | *** |
| Hypertension | +0.7027 | 0.7374 | ±1.4748 | +0.953 | 0.3406 |  |
| High cholesterol | -0.8611 | 0.6357 | ±1.2714 | -1.355 | 0.1755 |  |
| Kidney disease | +0.7810 | 1.2054 | ±2.4108 | +0.648 | 0.5171 |  |
| Circulatory disease | -0.4548 | 0.9226 | ±1.8452 | -0.493 | 0.6220 |  |
| **SD of daily means (mg/dL)** | **+0.3800** | 0.1574 | ±0.3148 | **+2.414** | **0.0158** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **597**, R² = **0.1571**, Adj R² = **0.1412**, F-statistic = **9.91** (p = **1.28e-16**), Residual SE = **7.398** on **585** df, AIC = **4095.5**, BIC = **4148.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.5745** | 8.5960 | ±17.1921 | **+9.955** | **2.40e-23** | *** |
| **Education: graduate level (vs college)** | **-1.7194** | 0.6663 | ±1.3325 | **-2.581** | **0.0099** | ** |
| Education: high school or below (vs college) | -1.0615 | 1.1295 | ±2.2590 | -0.940 | 0.3473 |  |
| Site: UCSD (vs UAB) | -1.4184 | 0.8296 | ±1.6592 | -1.710 | 0.0873 | . |
| **Site: UW (vs UAB)** | **-1.7757** | 0.7820 | ±1.5639 | **-2.271** | **0.0232** | * |
| **Age (years)** | **-0.1096** | 0.0311 | ±0.0621 | **-3.527** | **4.20e-04** | *** |
| **BMI (kg/m2)** | **+0.3052** | 0.0668 | ±0.1336 | **+4.568** | **4.93e-06** | *** |
| Hypertension | +0.7104 | 0.7480 | ±1.4960 | +0.950 | 0.3422 |  |
| High cholesterol | -0.8447 | 0.6331 | ±1.2662 | -1.334 | 0.1821 |  |
| Kidney disease | +0.6732 | 1.2229 | ±2.4459 | +0.550 | 0.5820 |  |
| Circulatory disease | -0.5715 | 0.9271 | ±1.8542 | -0.616 | 0.5376 |  |
| **Time in range 70-180, pooled (%)** | **-0.2627** | 0.0746 | ±0.1492 | **-3.523** | **4.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **597**, R² = **0.1578**, Adj R² = **0.1420**, F-statistic = **9.97** (p = **1.01e-16**), Residual SE = **7.395** on **585** df, AIC = **4095.0**, BIC = **4147.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+87.5673** | 9.0612 | ±18.1224 | **+9.664** | **4.29e-22** | *** |
| **Education: graduate level (vs college)** | **-1.7216** | 0.6656 | ±1.3311 | **-2.587** | **0.0097** | ** |
| Education: high school or below (vs college) | -1.0400 | 1.1277 | ±2.2554 | -0.922 | 0.3564 |  |
| Site: UCSD (vs UAB) | -1.4016 | 0.8276 | ±1.6552 | -1.694 | 0.0903 | . |
| **Site: UW (vs UAB)** | **-1.7670** | 0.7808 | ±1.5616 | **-2.263** | **0.0236** | * |
| **Age (years)** | **-0.1095** | 0.0310 | ±0.0621 | **-3.530** | **4.16e-04** | *** |
| **BMI (kg/m2)** | **+0.3035** | 0.0664 | ±0.1329 | **+4.568** | **4.92e-06** | *** |
| Hypertension | +0.7179 | 0.7478 | ±1.4955 | +0.960 | 0.3370 |  |
| High cholesterol | -0.8525 | 0.6322 | ±1.2645 | -1.348 | 0.1775 |  |
| Kidney disease | +0.6638 | 1.2217 | ±2.4435 | +0.543 | 0.5869 |  |
| Circulatory disease | -0.5962 | 0.9269 | ±1.8538 | -0.643 | 0.5201 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.2823** | 0.0790 | ±0.1581 | **-3.571** | **3.56e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **597**, R² = **0.1539**, Adj R² = **0.1380**, F-statistic = **9.67** (p = **3.55e-16**), Residual SE = **7.412** on **585** df, AIC = **4097.8**, BIC = **4150.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.7043** | 3.3543 | ±6.7087 | **+17.799** | **7.18e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8659** | 0.6808 | ±1.3616 | **-2.741** | **0.0061** | ** |
| Education: high school or below (vs college) | -1.2724 | 1.1427 | ±2.2853 | -1.114 | 0.2655 |  |
| Site: UCSD (vs UAB) | -1.4769 | 0.8327 | ±1.6654 | -1.774 | 0.0761 | . |
| **Site: UW (vs UAB)** | **-1.7255** | 0.7865 | ±1.5730 | **-2.194** | **0.0282** | * |
| **Age (years)** | **-0.1053** | 0.0310 | ±0.0621 | **-3.393** | **6.93e-04** | *** |
| **BMI (kg/m2)** | **+0.3087** | 0.0683 | ±0.1367 | **+4.517** | **6.27e-06** | *** |
| Hypertension | +0.7195 | 0.7475 | ±1.4950 | +0.963 | 0.3358 |  |
| High cholesterol | -0.7357 | 0.6366 | ±1.2733 | -1.156 | 0.2479 |  |
| Kidney disease | +0.6985 | 1.2285 | ±2.4570 | +0.569 | 0.5696 |  |
| Circulatory disease | -0.4978 | 0.9354 | ±1.8708 | -0.532 | 0.5946 |  |
| Time 54-69, pooled (%) | -1.0440 | 0.5645 | ±1.1289 | -1.850 | 0.0644 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **597**, R² = **0.1530**, Adj R² = **0.1371**, F-statistic = **9.61** (p = **4.71e-16**), Residual SE = **7.416** on **585** df, AIC = **4098.4**, BIC = **4151.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6230** | 3.3498 | ±6.6996 | **+17.799** | **7.21e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8580** | 0.6808 | ±1.3615 | **-2.729** | **0.0063** | ** |
| Education: high school or below (vs college) | -1.2690 | 1.1424 | ±2.2848 | -1.111 | 0.2666 |  |
| Site: UCSD (vs UAB) | -1.4643 | 0.8325 | ±1.6650 | -1.759 | 0.0786 | . |
| **Site: UW (vs UAB)** | **-1.7183** | 0.7866 | ±1.5731 | **-2.185** | **0.0289** | * |
| **Age (years)** | **-0.1049** | 0.0310 | ±0.0620 | **-3.380** | **7.25e-04** | *** |
| **BMI (kg/m2)** | **+0.3089** | 0.0684 | ±0.1367 | **+4.519** | **6.22e-06** | *** |
| Hypertension | +0.7133 | 0.7479 | ±1.4957 | +0.954 | 0.3402 |  |
| High cholesterol | -0.7414 | 0.6368 | ±1.2735 | -1.164 | 0.2443 |  |
| Kidney disease | +0.7046 | 1.2301 | ±2.4601 | +0.573 | 0.5668 |  |
| Circulatory disease | -0.5076 | 0.9361 | ±1.8722 | -0.542 | 0.5877 |  |
| Avg. daily time 54-69 (%) | -0.9156 | 0.5291 | ±1.0583 | -1.730 | 0.0836 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **597**, R² = **0.1539**, Adj R² = **0.1380**, F-statistic = **9.67** (p = **3.55e-16**), Residual SE = **7.412** on **585** df, AIC = **4097.8**, BIC = **4150.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.7043** | 3.3543 | ±6.7087 | **+17.799** | **7.18e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8659** | 0.6808 | ±1.3616 | **-2.741** | **0.0061** | ** |
| Education: high school or below (vs college) | -1.2724 | 1.1427 | ±2.2853 | -1.114 | 0.2655 |  |
| Site: UCSD (vs UAB) | -1.4769 | 0.8327 | ±1.6654 | -1.774 | 0.0761 | . |
| **Site: UW (vs UAB)** | **-1.7255** | 0.7865 | ±1.5730 | **-2.194** | **0.0282** | * |
| **Age (years)** | **-0.1053** | 0.0310 | ±0.0621 | **-3.393** | **6.93e-04** | *** |
| **BMI (kg/m2)** | **+0.3087** | 0.0683 | ±0.1367 | **+4.517** | **6.27e-06** | *** |
| Hypertension | +0.7195 | 0.7475 | ±1.4950 | +0.963 | 0.3358 |  |
| High cholesterol | -0.7357 | 0.6366 | ±1.2733 | -1.156 | 0.2479 |  |
| Kidney disease | +0.6985 | 1.2285 | ±2.4570 | +0.569 | 0.5696 |  |
| Circulatory disease | -0.4978 | 0.9354 | ±1.8708 | -0.532 | 0.5946 |  |
| Time < 70 (%) | -1.0440 | 0.5645 | ±1.1289 | -1.850 | 0.0644 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **597**, R² = **0.1530**, Adj R² = **0.1371**, F-statistic = **9.61** (p = **4.71e-16**), Residual SE = **7.416** on **585** df, AIC = **4098.4**, BIC = **4151.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6230** | 3.3498 | ±6.6996 | **+17.799** | **7.21e-71** | *** |
| **Education: graduate level (vs college)** | **-1.8580** | 0.6808 | ±1.3615 | **-2.729** | **0.0063** | ** |
| Education: high school or below (vs college) | -1.2690 | 1.1424 | ±2.2848 | -1.111 | 0.2666 |  |
| Site: UCSD (vs UAB) | -1.4643 | 0.8325 | ±1.6650 | -1.759 | 0.0786 | . |
| **Site: UW (vs UAB)** | **-1.7183** | 0.7866 | ±1.5731 | **-2.185** | **0.0289** | * |
| **Age (years)** | **-0.1049** | 0.0310 | ±0.0620 | **-3.380** | **7.25e-04** | *** |
| **BMI (kg/m2)** | **+0.3089** | 0.0684 | ±0.1367 | **+4.519** | **6.22e-06** | *** |
| Hypertension | +0.7133 | 0.7479 | ±1.4957 | +0.954 | 0.3402 |  |
| High cholesterol | -0.7414 | 0.6368 | ±1.2735 | -1.164 | 0.2443 |  |
| Kidney disease | +0.7046 | 1.2301 | ±2.4601 | +0.573 | 0.5668 |  |
| Circulatory disease | -0.5076 | 0.9361 | ±1.8722 | -0.542 | 0.5877 |  |
| Avg. daily time < 70 (%) | -0.9156 | 0.5291 | ±1.0583 | -1.730 | 0.0836 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **597**, R² = **0.1596**, Adj R² = **0.1438**, F-statistic = **10.10** (p = **5.76e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.7**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4061** | 3.2745 | ±6.5490 | **+18.142** | **1.48e-73** | *** |
| **Education: graduate level (vs college)** | **-1.7562** | 0.6650 | ±1.3300 | **-2.641** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.0949 | 1.1286 | ±2.2571 | -0.970 | 0.3320 |  |
| Site: UCSD (vs UAB) | -1.3806 | 0.8272 | ±1.6544 | -1.669 | 0.0951 | . |
| **Site: UW (vs UAB)** | **-1.7899** | 0.7811 | ±1.5621 | **-2.292** | **0.0219** | * |
| **Age (years)** | **-0.1105** | 0.0311 | ±0.0621 | **-3.557** | **3.75e-04** | *** |
| **BMI (kg/m2)** | **+0.3040** | 0.0667 | ±0.1334 | **+4.558** | **5.16e-06** | *** |
| Hypertension | +0.7119 | 0.7476 | ±1.4951 | +0.952 | 0.3409 |  |
| High cholesterol | -0.8532 | 0.6328 | ±1.2655 | -1.348 | 0.1775 |  |
| Kidney disease | +0.6485 | 1.2208 | ±2.4416 | +0.531 | 0.5953 |  |
| Circulatory disease | -0.6025 | 0.9262 | ±1.8524 | -0.650 | 0.5154 |  |
| **Time 181-250, pooled (%)** | **+0.2996** | 0.0750 | ±0.1500 | **+3.995** | **6.47e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **597**, R² = **0.1603**, Adj R² = **0.1445**, F-statistic = **10.16** (p = **4.53e-17**), Residual SE = **7.384** on **585** df, AIC = **4093.2**, BIC = **4145.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4457** | 3.2565 | ±6.5129 | **+18.255** | **1.90e-74** | *** |
| **Education: graduate level (vs college)** | **-1.7642** | 0.6642 | ±1.3285 | **-2.656** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.0792 | 1.1264 | ±2.2528 | -0.958 | 0.3380 |  |
| Site: UCSD (vs UAB) | -1.3544 | 0.8247 | ±1.6495 | -1.642 | 0.1005 |  |
| **Site: UW (vs UAB)** | **-1.7780** | 0.7797 | ±1.5595 | **-2.280** | **0.0226** | * |
| **Age (years)** | **-0.1102** | 0.0310 | ±0.0620 | **-3.556** | **3.77e-04** | *** |
| **BMI (kg/m2)** | **+0.3020** | 0.0663 | ±0.1325 | **+4.558** | **5.17e-06** | *** |
| Hypertension | +0.7187 | 0.7472 | ±1.4944 | +0.962 | 0.3361 |  |
| High cholesterol | -0.8619 | 0.6319 | ±1.2639 | -1.364 | 0.1726 |  |
| Kidney disease | +0.6378 | 1.2199 | ±2.4399 | +0.523 | 0.6011 |  |
| Circulatory disease | -0.6353 | 0.9263 | ±1.8527 | -0.686 | 0.4928 |  |
| **Avg. daily time 181-250 (%)** | **+0.3186** | 0.0785 | ±0.1570 | **+4.059** | **4.92e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **597**, R² = **0.1596**, Adj R² = **0.1438**, F-statistic = **10.10** (p = **5.76e-17**), Residual SE = **7.387** on **585** df, AIC = **4093.7**, BIC = **4146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4061** | 3.2745 | ±6.5490 | **+18.142** | **1.48e-73** | *** |
| **Education: graduate level (vs college)** | **-1.7562** | 0.6650 | ±1.3300 | **-2.641** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.0949 | 1.1286 | ±2.2571 | -0.970 | 0.3320 |  |
| Site: UCSD (vs UAB) | -1.3806 | 0.8272 | ±1.6544 | -1.669 | 0.0951 | . |
| **Site: UW (vs UAB)** | **-1.7899** | 0.7811 | ±1.5621 | **-2.292** | **0.0219** | * |
| **Age (years)** | **-0.1105** | 0.0311 | ±0.0621 | **-3.557** | **3.75e-04** | *** |
| **BMI (kg/m2)** | **+0.3040** | 0.0667 | ±0.1334 | **+4.558** | **5.16e-06** | *** |
| Hypertension | +0.7119 | 0.7476 | ±1.4951 | +0.952 | 0.3409 |  |
| High cholesterol | -0.8532 | 0.6328 | ±1.2655 | -1.348 | 0.1775 |  |
| Kidney disease | +0.6485 | 1.2208 | ±2.4416 | +0.531 | 0.5953 |  |
| Circulatory disease | -0.6025 | 0.9262 | ±1.8524 | -0.650 | 0.5154 |  |
| **Time > 180 (%)** | **+0.2996** | 0.0750 | ±0.1500 | **+3.995** | **6.47e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **597**, R² = **0.1603**, Adj R² = **0.1445**, F-statistic = **10.16** (p = **4.53e-17**), Residual SE = **7.384** on **585** df, AIC = **4093.2**, BIC = **4145.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4457** | 3.2565 | ±6.5129 | **+18.255** | **1.90e-74** | *** |
| **Education: graduate level (vs college)** | **-1.7642** | 0.6642 | ±1.3285 | **-2.656** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.0792 | 1.1264 | ±2.2528 | -0.958 | 0.3380 |  |
| Site: UCSD (vs UAB) | -1.3544 | 0.8247 | ±1.6495 | -1.642 | 0.1005 |  |
| **Site: UW (vs UAB)** | **-1.7780** | 0.7797 | ±1.5595 | **-2.280** | **0.0226** | * |
| **Age (years)** | **-0.1102** | 0.0310 | ±0.0620 | **-3.556** | **3.77e-04** | *** |
| **BMI (kg/m2)** | **+0.3020** | 0.0663 | ±0.1325 | **+4.558** | **5.17e-06** | *** |
| Hypertension | +0.7187 | 0.7472 | ±1.4944 | +0.962 | 0.3361 |  |
| High cholesterol | -0.8619 | 0.6319 | ±1.2639 | -1.364 | 0.1726 |  |
| Kidney disease | +0.6378 | 1.2199 | ±2.4399 | +0.523 | 0.6011 |  |
| Circulatory disease | -0.6353 | 0.9263 | ±1.8527 | -0.686 | 0.4928 |  |
| **Avg. daily time > 180 (%)** | **+0.3186** | 0.0785 | ±0.1570 | **+4.059** | **4.92e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 597)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **597**, R² = **0.1541**, Adj R² = **0.1382**, F-statistic = **9.69** (p = **3.26e-16**), Residual SE = **7.411** on **585** df, AIC = **4097.6**, BIC = **4150.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3811** | 3.2900 | ±6.5800 | **+18.049** | **8.02e-73** | *** |
| **Education: graduate level (vs college)** | **-1.7118** | 0.6667 | ±1.3333 | **-2.568** | **0.0102** | * |
| Education: high school or below (vs college) | -1.2008 | 1.1362 | ±2.2723 | -1.057 | 0.2906 |  |
| Site: UCSD (vs UAB) | -1.4840 | 0.8317 | ±1.6635 | -1.784 | 0.0744 | . |
| **Site: UW (vs UAB)** | **-1.7615** | 0.7865 | ±1.5729 | **-2.240** | **0.0251** | * |
| **Age (years)** | **-0.1027** | 0.0309 | ±0.0617 | **-3.327** | **8.77e-04** | *** |
| **BMI (kg/m2)** | **+0.3000** | 0.0673 | ±0.1345 | **+4.460** | **8.18e-06** | *** |
| Hypertension | +0.7455 | 0.7469 | ±1.4938 | +0.998 | 0.3182 |  |
| High cholesterol | -0.8865 | 0.6407 | ±1.2814 | -1.384 | 0.1665 |  |
| Kidney disease | +0.7628 | 1.2233 | ±2.4466 | +0.624 | 0.5329 |  |
| Circulatory disease | -0.4571 | 0.9311 | ±1.8623 | -0.491 | 0.6235 |  |
| **Nocturnal time > 180 (%)** | **+0.1805** | 0.0538 | ±0.1075 | **+3.358** | **7.85e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 601; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **601**, R² = **0.0357**, Adj R² = **0.0194**, F-statistic = **2.18** (p = **0.0173**), Residual SE = **67.165** on **590** df, AIC = **6773.5**, BIC = **6821.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.5812** | 22.4075 | ±44.8149 | **+18.145** | **1.41e-73** | *** |
| Education: graduate level (vs college) | +0.9673 | 5.8196 | ±11.6392 | +0.166 | 0.8680 |  |
| Education: high school or below (vs college) | -12.5058 | 11.7747 | ±23.5494 | -1.062 | 0.2882 |  |
| Site: UCSD (vs UAB) | -7.8422 | 7.3562 | ±14.7123 | -1.066 | 0.2864 |  |
| Site: UW (vs UAB) | -1.9034 | 7.0625 | ±14.1250 | -0.270 | 0.7875 |  |
| Age (years) | +0.0086 | 0.2512 | ±0.5024 | +0.034 | 0.9725 |  |
| **BMI (kg/m2)** | **-1.0542** | 0.4471 | ±0.8942 | **-2.358** | **0.0184** | * |
| Hypertension | -9.7792 | 6.3759 | ±12.7519 | -1.534 | 0.1251 |  |
| High cholesterol | -5.1673 | 5.6392 | ±11.2783 | -0.916 | 0.3595 |  |
| Kidney disease | -15.7725 | 14.8422 | ±29.6845 | -1.063 | 0.2879 |  |
| Circulatory disease | +18.6708 | 10.2935 | ±20.5869 | +1.814 | 0.0697 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **601**, R² = **0.0478**, Adj R² = **0.0300**, F-statistic = **2.69** (p = **0.0022**), Residual SE = **66.798** on **589** df, AIC = **6767.9**, BIC = **6820.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+524.4715** | 50.6896 | ±101.3791 | **+10.347** | **4.33e-25** | *** |
| Education: graduate level (vs college) | +0.9927 | 5.7959 | ±11.5918 | +0.171 | 0.8640 |  |
| Education: high school or below (vs college) | -12.6057 | 11.6249 | ±23.2499 | -1.084 | 0.2782 |  |
| Site: UCSD (vs UAB) | -8.6214 | 7.3417 | ±14.6834 | -1.174 | 0.2403 |  |
| Site: UW (vs UAB) | -1.8786 | 7.0394 | ±14.0788 | -0.267 | 0.7896 |  |
| Age (years) | +0.1040 | 0.2585 | ±0.5170 | +0.402 | 0.6875 |  |
| **BMI (kg/m2)** | **-0.9014** | 0.4377 | ±0.8754 | **-2.059** | **0.0395** | * |
| Hypertension | -8.6751 | 6.3612 | ±12.7225 | -1.364 | 0.1726 |  |
| High cholesterol | -3.1121 | 5.6342 | ±11.2685 | -0.552 | 0.5807 |  |
| Kidney disease | -15.4265 | 14.5327 | ±29.0653 | -1.062 | 0.2885 |  |
| Circulatory disease | +18.3476 | 10.1483 | ±20.2966 | +1.808 | 0.0706 | . |
| **HbA1c (%)** | **-23.1400** | 9.2898 | ±18.5796 | **-2.491** | **0.0127** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0274**), Residual SE = **67.219** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.9977** | 33.6749 | ±67.3499 | **+12.264** | **1.41e-34** | *** |
| Education: graduate level (vs college) | +1.0250 | 5.8528 | ±11.7056 | +0.175 | 0.8610 |  |
| Education: high school or below (vs college) | -12.4817 | 11.7998 | ±23.5995 | -1.058 | 0.2901 |  |
| Site: UCSD (vs UAB) | -7.9334 | 7.3850 | ±14.7700 | -1.074 | 0.2827 |  |
| Site: UW (vs UAB) | -1.8031 | 7.1417 | ±14.2833 | -0.252 | 0.8007 |  |
| Age (years) | +0.0117 | 0.2529 | ±0.5057 | +0.046 | 0.9630 |  |
| **BMI (kg/m2)** | **-1.0419** | 0.4523 | ±0.9047 | **-2.303** | **0.0213** | * |
| Hypertension | -9.6990 | 6.3736 | ±12.7473 | -1.522 | 0.1281 |  |
| High cholesterol | -5.1274 | 5.6641 | ±11.3281 | -0.905 | 0.3653 |  |
| Kidney disease | -15.6439 | 14.8945 | ±29.7889 | -1.050 | 0.2936 |  |
| Circulatory disease | +18.7344 | 10.3550 | ±20.7101 | +1.809 | 0.0704 | . |
| Mean glucose (mg/dL) | -0.0593 | 0.2564 | ±0.5128 | -0.231 | 0.8172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0274**), Residual SE = **67.219** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+421.2006** | 64.6912 | ±129.3824 | **+6.511** | **7.47e-11** | *** |
| Education: graduate level (vs college) | +1.0250 | 5.8528 | ±11.7056 | +0.175 | 0.8610 |  |
| Education: high school or below (vs college) | -12.4817 | 11.7998 | ±23.5995 | -1.058 | 0.2901 |  |
| Site: UCSD (vs UAB) | -7.9334 | 7.3850 | ±14.7700 | -1.074 | 0.2827 |  |
| Site: UW (vs UAB) | -1.8031 | 7.1417 | ±14.2833 | -0.252 | 0.8007 |  |
| Age (years) | +0.0117 | 0.2529 | ±0.5057 | +0.046 | 0.9630 |  |
| **BMI (kg/m2)** | **-1.0419** | 0.4523 | ±0.9047 | **-2.303** | **0.0213** | * |
| Hypertension | -9.6990 | 6.3736 | ±12.7473 | -1.522 | 0.1281 |  |
| High cholesterol | -5.1274 | 5.6641 | ±11.3281 | -0.905 | 0.3653 |  |
| Kidney disease | -15.6439 | 14.8945 | ±29.7889 | -1.050 | 0.2936 |  |
| Circulatory disease | +18.7344 | 10.3550 | ±20.7101 | +1.809 | 0.0704 | . |
| GMI (%) | -2.4782 | 10.7200 | ±21.4401 | -0.231 | 0.8172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **601**, R² = **0.0394**, Adj R² = **0.0214**, F-statistic = **2.19** (p = **0.0135**), Residual SE = **67.094** on **589** df, AIC = **6773.2**, BIC = **6826.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+441.9977** | 32.1447 | ±64.2895 | **+13.750** | **5.08e-43** | *** |
| Education: graduate level (vs college) | +1.1106 | 5.8074 | ±11.6148 | +0.191 | 0.8483 |  |
| Education: high school or below (vs college) | -12.1833 | 11.7777 | ±23.5554 | -1.034 | 0.3009 |  |
| Site: UCSD (vs UAB) | -7.9886 | 7.3524 | ±14.7047 | -1.087 | 0.2772 |  |
| Site: UW (vs UAB) | -1.1986 | 7.1284 | ±14.2569 | -0.168 | 0.8665 |  |
| Age (years) | -0.0070 | 0.2510 | ±0.5020 | -0.028 | 0.9778 |  |
| **BMI (kg/m2)** | **-0.9115** | 0.4404 | ±0.8807 | **-2.070** | **0.0385** | * |
| Hypertension | -9.4446 | 6.3954 | ±12.7908 | -1.477 | 0.1397 |  |
| High cholesterol | -4.5683 | 5.6749 | ±11.3499 | -0.805 | 0.4208 |  |
| Kidney disease | -15.4473 | 14.7538 | ±29.5075 | -1.047 | 0.2951 |  |
| Circulatory disease | +18.7839 | 10.3313 | ±20.6626 | +1.818 | 0.0690 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.3309 | 0.2211 | ±0.4421 | -1.497 | 0.1345 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0272**), Residual SE = **67.217** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.0485** | 24.1111 | ±48.2222 | **+16.716** | **9.97e-63** | *** |
| Education: graduate level (vs college) | +1.0757 | 5.7874 | ±11.5747 | +0.186 | 0.8526 |  |
| Education: high school or below (vs college) | -12.5504 | 11.8400 | ±23.6799 | -1.060 | 0.2891 |  |
| Site: UCSD (vs UAB) | -7.6569 | 7.4280 | ±14.8559 | -1.031 | 0.3026 |  |
| Site: UW (vs UAB) | -1.9927 | 7.0816 | ±14.1631 | -0.281 | 0.7784 |  |
| Age (years) | +0.0000 | 0.2553 | ±0.5105 | +0.000 | 0.9999 |  |
| **BMI (kg/m2)** | **-1.0587** | 0.4500 | ±0.8999 | **-2.353** | **0.0186** | * |
| Hypertension | -9.8582 | 6.3942 | ±12.7884 | -1.542 | 0.1231 |  |
| High cholesterol | -5.2236 | 5.6782 | ±11.3563 | -0.920 | 0.3576 |  |
| Kidney disease | -15.8720 | 14.8584 | ±29.7168 | -1.068 | 0.2854 |  |
| Circulatory disease | +18.7129 | 10.3043 | ±20.6085 | +1.816 | 0.0694 | . |
| Glucose SD, pooled (mg/dL) | +0.2160 | 0.7827 | ±1.5655 | +0.276 | 0.7826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **601**, R² = **0.0361**, Adj R² = **0.0181**, F-statistic = **2.01** (p = **0.0256**), Residual SE = **67.207** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.8667** | 23.7550 | ±47.5101 | **+16.875** | **6.87e-64** | *** |
| Education: graduate level (vs college) | +1.0966 | 5.7952 | ±11.5904 | +0.189 | 0.8499 |  |
| Education: high school or below (vs college) | -12.6150 | 11.8717 | ±23.7435 | -1.063 | 0.2880 |  |
| Site: UCSD (vs UAB) | -7.4609 | 7.4565 | ±14.9130 | -1.001 | 0.3170 |  |
| Site: UW (vs UAB) | -2.0582 | 7.0795 | ±14.1589 | -0.291 | 0.7713 |  |
| Age (years) | -0.0070 | 0.2555 | ±0.5111 | -0.027 | 0.9783 |  |
| **BMI (kg/m2)** | **-1.0647** | 0.4511 | ±0.9021 | **-2.361** | **0.0182** | * |
| Hypertension | -9.8910 | 6.3913 | ±12.7827 | -1.548 | 0.1217 |  |
| High cholesterol | -5.2522 | 5.6754 | ±11.3508 | -0.925 | 0.3547 |  |
| Kidney disease | -15.9867 | 14.8728 | ±29.7455 | -1.075 | 0.2824 |  |
| Circulatory disease | +18.7128 | 10.3022 | ±20.6045 | +1.816 | 0.0693 | . |
| Avg. daily SD (mg/dL) | +0.3923 | 0.8150 | ±1.6301 | +0.481 | 0.6303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **601**, R² = **0.0360**, Adj R² = **0.0180**, F-statistic = **2.00** (p = **0.0262**), Residual SE = **67.211** on **589** df, AIC = **6775.3**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.7697** | 25.8376 | ±51.6753 | **+15.472** | **5.33e-54** | *** |
| Education: graduate level (vs college) | +1.2337 | 5.7871 | ±11.5743 | +0.213 | 0.8312 |  |
| Education: high school or below (vs college) | -12.5485 | 11.8384 | ±23.6768 | -1.060 | 0.2892 |  |
| Site: UCSD (vs UAB) | -7.6162 | 7.4041 | ±14.8083 | -1.029 | 0.3037 |  |
| Site: UW (vs UAB) | -1.9612 | 7.0647 | ±14.1294 | -0.278 | 0.7813 |  |
| Age (years) | -0.0027 | 0.2536 | ±0.5072 | -0.011 | 0.9916 |  |
| **BMI (kg/m2)** | **-1.0492** | 0.4465 | ±0.8930 | **-2.350** | **0.0188** | * |
| Hypertension | -9.8513 | 6.3967 | ±12.7935 | -1.540 | 0.1235 |  |
| High cholesterol | -5.2064 | 5.6564 | ±11.3129 | -0.920 | 0.3573 |  |
| Kidney disease | -15.8288 | 14.8376 | ±29.6751 | -1.067 | 0.2861 |  |
| Circulatory disease | +18.8125 | 10.3329 | ±20.6657 | +1.821 | 0.0687 | . |
| CV (%) | +0.4452 | 1.0163 | ±2.0326 | +0.438 | 0.6614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **601**, R² = **0.0362**, Adj R² = **0.0182**, F-statistic = **2.01** (p = **0.0252**), Residual SE = **67.203** on **589** df, AIC = **6775.1**, BIC = **6827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+416.0311** | 29.0629 | ±58.1258 | **+14.315** | **1.77e-46** | *** |
| Education: graduate level (vs college) | +1.3166 | 5.7907 | ±11.5814 | +0.227 | 0.8201 |  |
| Education: high school or below (vs college) | -12.5943 | 11.8591 | ±23.7182 | -1.062 | 0.2882 |  |
| Site: UCSD (vs UAB) | -7.5673 | 7.3893 | ±14.7785 | -1.024 | 0.3058 |  |
| Site: UW (vs UAB) | -1.9893 | 7.0645 | ±14.1290 | -0.282 | 0.7783 |  |
| Age (years) | -0.0042 | 0.2532 | ±0.5065 | -0.016 | 0.9869 |  |
| **BMI (kg/m2)** | **-1.0476** | 0.4464 | ±0.8929 | **-2.346** | **0.0190** | * |
| Hypertension | -9.8763 | 6.3952 | ±12.7904 | -1.544 | 0.1225 |  |
| High cholesterol | -5.2057 | 5.6527 | ±11.3053 | -0.921 | 0.3571 |  |
| Kidney disease | -15.8330 | 14.8365 | ±29.6730 | -1.067 | 0.2859 |  |
| Circulatory disease | +18.8675 | 10.3365 | ±20.6730 | +1.825 | 0.0680 | . |
| Mean / SD ratio | -1.4231 | 2.4679 | ±4.9358 | -0.577 | 0.5642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **601**, R² = **0.0366**, Adj R² = **0.0186**, F-statistic = **2.04** (p = **0.0233**), Residual SE = **67.189** on **589** df, AIC = **6774.9**, BIC = **6827.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+418.5574** | 29.1474 | ±58.2947 | **+14.360** | **9.22e-47** | *** |
| Education: graduate level (vs college) | +1.3164 | 5.7902 | ±11.5805 | +0.227 | 0.8201 |  |
| Education: high school or below (vs college) | -12.6814 | 11.9033 | ±23.8067 | -1.065 | 0.2867 |  |
| Site: UCSD (vs UAB) | -7.4000 | 7.4169 | ±14.8339 | -0.998 | 0.3184 |  |
| Site: UW (vs UAB) | -2.0503 | 7.0631 | ±14.1261 | -0.290 | 0.7716 |  |
| Age (years) | -0.0096 | 0.2538 | ±0.5076 | -0.038 | 0.9699 |  |
| **BMI (kg/m2)** | **-1.0549** | 0.4472 | ±0.8945 | **-2.359** | **0.0183** | * |
| Hypertension | -9.7889 | 6.3894 | ±12.7789 | -1.532 | 0.1255 |  |
| High cholesterol | -5.2053 | 5.6510 | ±11.3019 | -0.921 | 0.3570 |  |
| Kidney disease | -15.9454 | 14.8172 | ±29.6345 | -1.076 | 0.2819 |  |
| Circulatory disease | +18.8788 | 10.3122 | ±20.6244 | +1.831 | 0.0671 | . |
| Avg. daily mean/SD | -1.5363 | 2.0809 | ±4.1618 | -0.738 | 0.4603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **601**, R² = **0.0403**, Adj R² = **0.0224**, F-statistic = **2.25** (p = **0.0111**), Residual SE = **67.061** on **589** df, AIC = **6772.6**, BIC = **6825.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+431.7476** | 26.6199 | ±53.2397 | **+16.219** | **3.70e-59** | *** |
| Education: graduate level (vs college) | +0.8530 | 5.8154 | ±11.6309 | +0.147 | 0.8834 |  |
| Education: high school or below (vs college) | -10.9079 | 11.8308 | ±23.6615 | -0.922 | 0.3565 |  |
| Site: UCSD (vs UAB) | -8.3286 | 7.4708 | ±14.9415 | -1.115 | 0.2649 |  |
| Site: UW (vs UAB) | -2.0411 | 7.0782 | ±14.1565 | -0.288 | 0.7731 |  |
| Age (years) | +0.0113 | 0.2513 | ±0.5026 | +0.045 | 0.9642 |  |
| **BMI (kg/m2)** | **-1.0578** | 0.4436 | ±0.8873 | **-2.384** | **0.0171** | * |
| Hypertension | -10.4292 | 6.3641 | ±12.7281 | -1.639 | 0.1013 |  |
| High cholesterol | -5.1074 | 5.6242 | ±11.2485 | -0.908 | 0.3638 |  |
| Kidney disease | -14.7942 | 14.8764 | ±29.7528 | -0.994 | 0.3200 |  |
| Circulatory disease | +17.7045 | 10.3263 | ±20.6527 | +1.715 | 0.0864 | . |
| MAG (mg/dL/h) | -0.6933 | 0.5220 | ±1.0440 | -1.328 | 0.1841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **601**, R² = **0.0370**, Adj R² = **0.0190**, F-statistic = **2.06** (p = **0.0216**), Residual SE = **67.177** on **589** df, AIC = **6774.6**, BIC = **6827.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8318** | 25.7203 | ±51.4406 | **+15.312** | **6.35e-53** | *** |
| Education: graduate level (vs college) | +0.9863 | 5.8225 | ±11.6450 | +0.169 | 0.8655 |  |
| Education: high school or below (vs college) | -12.9612 | 11.9913 | ±23.9825 | -1.081 | 0.2797 |  |
| Site: UCSD (vs UAB) | -7.4314 | 7.4288 | ±14.8576 | -1.000 | 0.3171 |  |
| Site: UW (vs UAB) | -2.1449 | 7.0639 | ±14.1278 | -0.304 | 0.7614 |  |
| Age (years) | -0.0151 | 0.2560 | ±0.5119 | -0.059 | 0.9531 |  |
| **BMI (kg/m2)** | **-1.0367** | 0.4460 | ±0.8920 | **-2.324** | **0.0201** | * |
| Hypertension | -9.7846 | 6.3810 | ±12.7620 | -1.533 | 0.1252 |  |
| High cholesterol | -5.1820 | 5.6511 | ±11.3023 | -0.917 | 0.3592 |  |
| Kidney disease | -16.1997 | 14.9136 | ±29.8271 | -1.086 | 0.2774 |  |
| Circulatory disease | +18.7174 | 10.2827 | ±20.5654 | +1.820 | 0.0687 | . |
| Avg. daily range (mg/dL) | +0.1534 | 0.1937 | ±0.3874 | +0.792 | 0.4282 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **601**, R² = **0.0372**, Adj R² = **0.0193**, F-statistic = **2.07** (p = **0.0206**), Residual SE = **67.168** on **589** df, AIC = **6774.5**, BIC = **6827.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.2534** | 22.9962 | ±45.9924 | **+17.927** | **7.26e-72** | *** |
| Education: graduate level (vs college) | +0.8521 | 5.8161 | ±11.6323 | +0.146 | 0.8835 |  |
| Education: high school or below (vs college) | -12.5636 | 11.7787 | ±23.5575 | -1.067 | 0.2861 |  |
| Site: UCSD (vs UAB) | -8.0165 | 7.3518 | ±14.7036 | -1.090 | 0.2755 |  |
| Site: UW (vs UAB) | -1.7853 | 7.0645 | ±14.1290 | -0.253 | 0.8005 |  |
| Age (years) | +0.0064 | 0.2522 | ±0.5043 | +0.025 | 0.9798 |  |
| **BMI (kg/m2)** | **-1.0100** | 0.4474 | ±0.8949 | **-2.257** | **0.0240** | * |
| Hypertension | -9.8696 | 6.3694 | ±12.7387 | -1.550 | 0.1212 |  |
| High cholesterol | -4.7162 | 5.6538 | ±11.3076 | -0.834 | 0.4042 |  |
| Kidney disease | -15.9004 | 14.7742 | ±29.5483 | -1.076 | 0.2818 |  |
| Circulatory disease | +18.6714 | 10.2417 | ±20.4835 | +1.823 | 0.0683 | . |
| SD of daily means (mg/dL) | -1.1885 | 1.2298 | ±2.4596 | -0.966 | 0.3338 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **601**, R² = **0.0363**, Adj R² = **0.0183**, F-statistic = **2.01** (p = **0.0250**), Residual SE = **67.202** on **589** df, AIC = **6775.1**, BIC = **6827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+467.5277** | 102.3630 | ±204.7261 | **+4.567** | **4.94e-06** | *** |
| Education: graduate level (vs college) | +1.0186 | 5.8155 | ±11.6310 | +0.175 | 0.8610 |  |
| Education: high school or below (vs college) | -12.4527 | 11.7885 | ±23.5770 | -1.056 | 0.2908 |  |
| Site: UCSD (vs UAB) | -7.6192 | 7.3765 | ±14.7531 | -1.033 | 0.3017 |  |
| Site: UW (vs UAB) | -2.1298 | 7.1106 | ±14.2212 | -0.300 | 0.7645 |  |
| Age (years) | -0.0047 | 0.2515 | ±0.5030 | -0.019 | 0.9852 |  |
| **BMI (kg/m2)** | **-1.0676** | 0.4505 | ±0.9011 | **-2.370** | **0.0178** | * |
| Hypertension | -9.7429 | 6.3845 | ±12.7690 | -1.526 | 0.1270 |  |
| High cholesterol | -5.4242 | 5.6925 | ±11.3849 | -0.953 | 0.3407 |  |
| Kidney disease | -15.9943 | 14.8839 | ±29.7678 | -1.075 | 0.2826 |  |
| Circulatory disease | +18.4192 | 10.3985 | ±20.7970 | +1.771 | 0.0765 | . |
| Time in range 70-180, pooled (%) | -0.6079 | 0.9784 | ±1.9568 | -0.621 | 0.5344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **601**, R² = **0.0360**, Adj R² = **0.0180**, F-statistic = **2.00** (p = **0.0263**), Residual SE = **67.211** on **589** df, AIC = **6775.3**, BIC = **6828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+452.1977** | 106.3993 | ±212.7986 | **+4.250** | **2.14e-05** | *** |
| Education: graduate level (vs college) | +0.9991 | 5.8185 | ±11.6370 | +0.172 | 0.8637 |  |
| Education: high school or below (vs college) | -12.4407 | 11.7722 | ±23.5445 | -1.057 | 0.2906 |  |
| Site: UCSD (vs UAB) | -7.6684 | 7.3707 | ±14.7415 | -1.040 | 0.2982 |  |
| Site: UW (vs UAB) | -2.0490 | 7.1131 | ±14.2262 | -0.288 | 0.7733 |  |
| Age (years) | -0.0004 | 0.2515 | ±0.5029 | -0.002 | 0.9986 |  |
| **BMI (kg/m2)** | **-1.0664** | 0.4513 | ±0.9027 | **-2.363** | **0.0181** | * |
| Hypertension | -9.7354 | 6.3870 | ±12.7740 | -1.524 | 0.1274 |  |
| High cholesterol | -5.3603 | 5.6890 | ±11.3779 | -0.942 | 0.3461 |  |
| Kidney disease | -15.9479 | 14.8990 | ±29.7980 | -1.070 | 0.2844 |  |
| Circulatory disease | +18.4495 | 10.4290 | ±20.8580 | +1.769 | 0.0769 | . |
| Avg. daily time in range 70-180 (%) | -0.4545 | 1.0201 | ±2.0401 | -0.446 | 0.6559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **601**, R² = **0.0359**, Adj R² = **0.0179**, F-statistic = **1.99** (p = **0.0270**), Residual SE = **67.216** on **589** df, AIC = **6775.4**, BIC = **6828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.1039** | 22.7729 | ±45.5459 | **+17.877** | **1.79e-71** | *** |
| Education: graduate level (vs college) | +0.7638 | 5.8667 | ±11.7334 | +0.130 | 0.8964 |  |
| Education: high school or below (vs college) | -12.7021 | 11.7846 | ±23.5692 | -1.078 | 0.2811 |  |
| Site: UCSD (vs UAB) | -7.7223 | 7.3755 | ±14.7510 | -1.047 | 0.2951 |  |
| Site: UW (vs UAB) | -1.9002 | 7.0667 | ±14.1335 | -0.269 | 0.7880 |  |
| Age (years) | +0.0085 | 0.2516 | ±0.5031 | +0.034 | 0.9732 |  |
| **BMI (kg/m2)** | **-1.0569** | 0.4490 | ±0.8979 | **-2.354** | **0.0186** | * |
| Hypertension | -9.7972 | 6.3754 | ±12.7507 | -1.537 | 0.1244 |  |
| High cholesterol | -5.1569 | 5.6432 | ±11.2865 | -0.914 | 0.3608 |  |
| Kidney disease | -15.8186 | 14.8850 | ±29.7700 | -1.063 | 0.2879 |  |
| Circulatory disease | +18.6034 | 10.3189 | ±20.6379 | +1.803 | 0.0714 | . |
| Time 54-69, pooled (%) | -1.6483 | 4.7405 | ±9.4810 | -0.348 | 0.7281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **601**, R² = **0.0361**, Adj R² = **0.0181**, F-statistic = **2.01** (p = **0.0257**), Residual SE = **67.207** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.3302** | 22.6344 | ±45.2687 | **+17.996** | **2.09e-72** | *** |
| Education: graduate level (vs college) | +0.6290 | 5.8808 | ±11.7617 | +0.107 | 0.9148 |  |
| Education: high school or below (vs college) | -12.8507 | 11.7906 | ±23.5813 | -1.090 | 0.2758 |  |
| Site: UCSD (vs UAB) | -7.5994 | 7.3862 | ±14.7724 | -1.029 | 0.3035 |  |
| Site: UW (vs UAB) | -1.8897 | 7.0622 | ±14.1244 | -0.268 | 0.7890 |  |
| Age (years) | +0.0091 | 0.2513 | ±0.5027 | +0.036 | 0.9713 |  |
| **BMI (kg/m2)** | **-1.0584** | 0.4477 | ±0.8954 | **-2.364** | **0.0181** | * |
| Hypertension | -9.8233 | 6.3719 | ±12.7438 | -1.542 | 0.1232 |  |
| High cholesterol | -5.1718 | 5.6443 | ±11.2885 | -0.916 | 0.3595 |  |
| Kidney disease | -15.8430 | 14.8903 | ±29.7806 | -1.064 | 0.2873 |  |
| Circulatory disease | +18.5128 | 10.3025 | ±20.6051 | +1.797 | 0.0723 | . |
| Avg. daily time 54-69 (%) | -2.5589 | 4.7620 | ±9.5240 | -0.537 | 0.5910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **601**, R² = **0.0359**, Adj R² = **0.0179**, F-statistic = **1.99** (p = **0.0270**), Residual SE = **67.216** on **589** df, AIC = **6775.4**, BIC = **6828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.1039** | 22.7729 | ±45.5459 | **+17.877** | **1.79e-71** | *** |
| Education: graduate level (vs college) | +0.7638 | 5.8667 | ±11.7334 | +0.130 | 0.8964 |  |
| Education: high school or below (vs college) | -12.7021 | 11.7846 | ±23.5692 | -1.078 | 0.2811 |  |
| Site: UCSD (vs UAB) | -7.7223 | 7.3755 | ±14.7510 | -1.047 | 0.2951 |  |
| Site: UW (vs UAB) | -1.9002 | 7.0667 | ±14.1335 | -0.269 | 0.7880 |  |
| Age (years) | +0.0085 | 0.2516 | ±0.5031 | +0.034 | 0.9732 |  |
| **BMI (kg/m2)** | **-1.0569** | 0.4490 | ±0.8979 | **-2.354** | **0.0186** | * |
| Hypertension | -9.7972 | 6.3754 | ±12.7507 | -1.537 | 0.1244 |  |
| High cholesterol | -5.1569 | 5.6432 | ±11.2865 | -0.914 | 0.3608 |  |
| Kidney disease | -15.8186 | 14.8850 | ±29.7700 | -1.063 | 0.2879 |  |
| Circulatory disease | +18.6034 | 10.3189 | ±20.6379 | +1.803 | 0.0714 | . |
| Time < 70 (%) | -1.6483 | 4.7405 | ±9.4810 | -0.348 | 0.7281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **601**, R² = **0.0361**, Adj R² = **0.0181**, F-statistic = **2.01** (p = **0.0257**), Residual SE = **67.207** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.3302** | 22.6344 | ±45.2687 | **+17.996** | **2.09e-72** | *** |
| Education: graduate level (vs college) | +0.6290 | 5.8808 | ±11.7617 | +0.107 | 0.9148 |  |
| Education: high school or below (vs college) | -12.8507 | 11.7906 | ±23.5813 | -1.090 | 0.2758 |  |
| Site: UCSD (vs UAB) | -7.5994 | 7.3862 | ±14.7724 | -1.029 | 0.3035 |  |
| Site: UW (vs UAB) | -1.8897 | 7.0622 | ±14.1244 | -0.268 | 0.7890 |  |
| Age (years) | +0.0091 | 0.2513 | ±0.5027 | +0.036 | 0.9713 |  |
| **BMI (kg/m2)** | **-1.0584** | 0.4477 | ±0.8954 | **-2.364** | **0.0181** | * |
| Hypertension | -9.8233 | 6.3719 | ±12.7438 | -1.542 | 0.1232 |  |
| High cholesterol | -5.1718 | 5.6443 | ±11.2885 | -0.916 | 0.3595 |  |
| Kidney disease | -15.8430 | 14.8903 | ±29.7806 | -1.064 | 0.2873 |  |
| Circulatory disease | +18.5128 | 10.3025 | ±20.6051 | +1.797 | 0.0723 | . |
| Avg. daily time < 70 (%) | -2.5589 | 4.7620 | ±9.5240 | -0.537 | 0.5910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **601**, R² = **0.0364**, Adj R² = **0.0184**, F-statistic = **2.02** (p = **0.0244**), Residual SE = **67.198** on **589** df, AIC = **6775.0**, BIC = **6827.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9618** | 22.5197 | ±45.0394 | **+18.071** | **5.36e-73** | *** |
| Education: graduate level (vs college) | +0.9413 | 5.8327 | ±11.6655 | +0.161 | 0.8718 |  |
| Education: high school or below (vs college) | -12.5269 | 11.8040 | ±23.6079 | -1.061 | 0.2886 |  |
| Site: UCSD (vs UAB) | -7.5495 | 7.3821 | ±14.7641 | -1.023 | 0.3065 |  |
| Site: UW (vs UAB) | -2.1501 | 7.1163 | ±14.2327 | -0.302 | 0.7625 |  |
| Age (years) | -0.0060 | 0.2521 | ±0.5042 | -0.024 | 0.9810 |  |
| **BMI (kg/m2)** | **-1.0700** | 0.4517 | ±0.9034 | **-2.369** | **0.0178** | * |
| Hypertension | -9.7467 | 6.3847 | ±12.7694 | -1.527 | 0.1269 |  |
| High cholesterol | -5.4444 | 5.6963 | ±11.3925 | -0.956 | 0.3392 |  |
| Kidney disease | -16.0340 | 14.8967 | ±29.7933 | -1.076 | 0.2818 |  |
| Circulatory disease | +18.3680 | 10.4159 | ±20.8318 | +1.763 | 0.0778 | . |
| Time 181-250, pooled (%) | +0.6658 | 1.0030 | ±2.0059 | +0.664 | 0.5068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **601**, R² = **0.0362**, Adj R² = **0.0182**, F-statistic = **2.01** (p = **0.0255**), Residual SE = **67.206** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9511** | 22.5426 | ±45.0851 | **+18.053** | **7.53e-73** | *** |
| Education: graduate level (vs college) | +0.9323 | 5.8376 | ±11.6752 | +0.160 | 0.8731 |  |
| Education: high school or below (vs college) | -12.5011 | 11.7925 | ±23.5850 | -1.060 | 0.2891 |  |
| Site: UCSD (vs UAB) | -7.5741 | 7.3793 | ±14.7585 | -1.026 | 0.3047 |  |
| Site: UW (vs UAB) | -2.0803 | 7.1138 | ±14.2276 | -0.292 | 0.7700 |  |
| Age (years) | -0.0025 | 0.2518 | ±0.5037 | -0.010 | 0.9921 |  |
| **BMI (kg/m2)** | **-1.0702** | 0.4524 | ±0.9047 | **-2.366** | **0.0180** | * |
| Hypertension | -9.7347 | 6.3869 | ±12.7737 | -1.524 | 0.1275 |  |
| High cholesterol | -5.4068 | 5.6970 | ±11.3939 | -0.949 | 0.3426 |  |
| Kidney disease | -16.0047 | 14.9128 | ±29.8257 | -1.073 | 0.2832 |  |
| Circulatory disease | +18.3627 | 10.4489 | ±20.8979 | +1.757 | 0.0789 | . |
| Avg. daily time 181-250 (%) | +0.5617 | 1.0422 | ±2.0845 | +0.539 | 0.5899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **601**, R² = **0.0364**, Adj R² = **0.0184**, F-statistic = **2.02** (p = **0.0244**), Residual SE = **67.198** on **589** df, AIC = **6775.0**, BIC = **6827.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9618** | 22.5197 | ±45.0394 | **+18.071** | **5.36e-73** | *** |
| Education: graduate level (vs college) | +0.9413 | 5.8327 | ±11.6655 | +0.161 | 0.8718 |  |
| Education: high school or below (vs college) | -12.5269 | 11.8040 | ±23.6079 | -1.061 | 0.2886 |  |
| Site: UCSD (vs UAB) | -7.5495 | 7.3821 | ±14.7641 | -1.023 | 0.3065 |  |
| Site: UW (vs UAB) | -2.1501 | 7.1163 | ±14.2327 | -0.302 | 0.7625 |  |
| Age (years) | -0.0060 | 0.2521 | ±0.5042 | -0.024 | 0.9810 |  |
| **BMI (kg/m2)** | **-1.0700** | 0.4517 | ±0.9034 | **-2.369** | **0.0178** | * |
| Hypertension | -9.7467 | 6.3847 | ±12.7694 | -1.527 | 0.1269 |  |
| High cholesterol | -5.4444 | 5.6963 | ±11.3925 | -0.956 | 0.3392 |  |
| Kidney disease | -16.0340 | 14.8967 | ±29.7933 | -1.076 | 0.2818 |  |
| Circulatory disease | +18.3680 | 10.4159 | ±20.8318 | +1.763 | 0.0778 | . |
| Time > 180 (%) | +0.6658 | 1.0030 | ±2.0059 | +0.664 | 0.5068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **601**, R² = **0.0362**, Adj R² = **0.0182**, F-statistic = **2.01** (p = **0.0255**), Residual SE = **67.206** on **589** df, AIC = **6775.2**, BIC = **6828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.9511** | 22.5426 | ±45.0851 | **+18.053** | **7.53e-73** | *** |
| Education: graduate level (vs college) | +0.9323 | 5.8376 | ±11.6752 | +0.160 | 0.8731 |  |
| Education: high school or below (vs college) | -12.5011 | 11.7925 | ±23.5850 | -1.060 | 0.2891 |  |
| Site: UCSD (vs UAB) | -7.5741 | 7.3793 | ±14.7585 | -1.026 | 0.3047 |  |
| Site: UW (vs UAB) | -2.0803 | 7.1138 | ±14.2276 | -0.292 | 0.7700 |  |
| Age (years) | -0.0025 | 0.2518 | ±0.5037 | -0.010 | 0.9921 |  |
| **BMI (kg/m2)** | **-1.0702** | 0.4524 | ±0.9047 | **-2.366** | **0.0180** | * |
| Hypertension | -9.7347 | 6.3869 | ±12.7737 | -1.524 | 0.1275 |  |
| High cholesterol | -5.4068 | 5.6970 | ±11.3939 | -0.949 | 0.3426 |  |
| Kidney disease | -16.0047 | 14.9128 | ±29.8257 | -1.073 | 0.2832 |  |
| Circulatory disease | +18.3627 | 10.4489 | ±20.8979 | +1.757 | 0.0789 | . |
| Avg. daily time > 180 (%) | +0.5617 | 1.0422 | ±2.0845 | +0.539 | 0.5899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 601)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **601**, R² = **0.0358**, Adj R² = **0.0178**, F-statistic = **1.99** (p = **0.0273**), Residual SE = **67.218** on **589** df, AIC = **6775.4**, BIC = **6828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.5318** | 22.4085 | ±44.8170 | **+18.142** | **1.49e-73** | *** |
| Education: graduate level (vs college) | +0.9437 | 5.8170 | ±11.6341 | +0.162 | 0.8711 |  |
| Education: high school or below (vs college) | -12.3804 | 11.8300 | ±23.6600 | -1.047 | 0.2953 |  |
| Site: UCSD (vs UAB) | -7.9370 | 7.3512 | ±14.7023 | -1.080 | 0.2803 |  |
| Site: UW (vs UAB) | -1.8487 | 7.0866 | ±14.1731 | -0.261 | 0.7942 |  |
| Age (years) | +0.0066 | 0.2518 | ±0.5036 | +0.026 | 0.9792 |  |
| **BMI (kg/m2)** | **-1.0421** | 0.4470 | ±0.8940 | **-2.331** | **0.0197** | * |
| Hypertension | -9.8351 | 6.3953 | ±12.7907 | -1.538 | 0.1241 |  |
| High cholesterol | -4.9709 | 5.7395 | ±11.4791 | -0.866 | 0.3864 |  |
| Kidney disease | -15.7879 | 14.8386 | ±29.6772 | -1.064 | 0.2873 |  |
| Circulatory disease | +18.6651 | 10.2979 | ±20.5957 | +1.813 | 0.0699 | . |
| Nocturnal time > 180 (%) | -0.2364 | 0.7004 | ±1.4007 | -0.337 | 0.7358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 598; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **598**, R² = **0.1019**, Adj R² = **0.0866**, F-statistic = **6.66** (p = **7.87e-10**), Residual SE = **16.942** on **587** df, AIC = **5092.4**, BIC = **5140.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7537** | 7.2671 | ±14.5341 | **+6.021** | **1.74e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7145** | 1.5343 | ±3.0687 | **-2.421** | **0.0155** | * |
| Education: high school or below (vs college) | -0.9505 | 2.4632 | ±4.9264 | -0.386 | 0.6996 |  |
| Site: UCSD (vs UAB) | +0.7626 | 1.9042 | ±3.8084 | +0.400 | 0.6888 |  |
| Site: UW (vs UAB) | -1.5617 | 1.7548 | ±3.5097 | -0.890 | 0.3735 |  |
| **Age (years)** | **-0.1833** | 0.0709 | ±0.1417 | **-2.588** | **0.0097** | ** |
| **BMI (kg/m2)** | **+0.6030** | 0.1463 | ±0.2925 | **+4.123** | **3.74e-05** | *** |
| Hypertension | +0.7734 | 1.6866 | ±3.3732 | +0.459 | 0.6465 |  |
| High cholesterol | -1.4749 | 1.4733 | ±2.9465 | -1.001 | 0.3168 |  |
| Kidney disease | +3.1862 | 3.0158 | ±6.0316 | +1.057 | 0.2907 |  |
| Circulatory disease | -0.0732 | 2.2723 | ±4.5446 | -0.032 | 0.9743 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **598**, R² = **0.1063**, Adj R² = **0.0895**, F-statistic = **6.34** (p = **5.99e-10**), Residual SE = **16.914** on **586** df, AIC = **5091.4**, BIC = **5144.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.2972** | 12.5339 | ±25.0678 | **+2.018** | **0.0436** | * |
| **Education: graduate level (vs college)** | **-3.7474** | 1.5269 | ±3.0539 | **-2.454** | **0.0141** | * |
| Education: high school or below (vs college) | -0.9235 | 2.4746 | ±4.9491 | -0.373 | 0.7090 |  |
| Site: UCSD (vs UAB) | +0.8435 | 1.8865 | ±3.7729 | +0.447 | 0.6548 |  |
| Site: UW (vs UAB) | -1.5727 | 1.7501 | ±3.5002 | -0.899 | 0.3689 |  |
| **Age (years)** | **-0.1988** | 0.0717 | ±0.1434 | **-2.772** | **0.0056** | ** |
| **BMI (kg/m2)** | **+0.5754** | 0.1435 | ±0.2870 | **+4.009** | **6.10e-05** | *** |
| Hypertension | +0.5809 | 1.6920 | ±3.3840 | +0.343 | 0.7314 |  |
| High cholesterol | -1.8041 | 1.4757 | ±2.9514 | -1.223 | 0.2215 |  |
| Kidney disease | +3.2054 | 2.9611 | ±5.9221 | +1.083 | 0.2790 |  |
| Circulatory disease | -0.0085 | 2.2406 | ±4.4812 | -0.004 | 0.9970 |  |
| HbA1c (%) | +3.6531 | 2.2405 | ±4.4811 | +1.630 | 0.1030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **598**, R² = **0.1100**, Adj R² = **0.0933**, F-statistic = **6.59** (p = **2.04e-10**), Residual SE = **16.879** on **586** df, AIC = **5088.9**, BIC = **5141.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.9775** | 9.2414 | ±18.4828 | **+3.027** | **0.0025** | ** |
| **Education: graduate level (vs college)** | **-3.8518** | 1.5247 | ±3.0494 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | -0.9630 | 2.4459 | ±4.8917 | -0.394 | 0.6938 |  |
| Site: UCSD (vs UAB) | +1.0483 | 1.8941 | ±3.7882 | +0.553 | 0.5799 |  |
| Site: UW (vs UAB) | -1.7898 | 1.7544 | ±3.5088 | -1.020 | 0.3076 |  |
| **Age (years)** | **-0.1915** | 0.0706 | ±0.1412 | **-2.713** | **0.0067** | ** |
| **BMI (kg/m2)** | **+0.5740** | 0.1435 | ±0.2870 | **+4.000** | **6.34e-05** | *** |
| Hypertension | +0.5744 | 1.6813 | ±3.3625 | +0.342 | 0.7326 |  |
| High cholesterol | -1.5338 | 1.4710 | ±2.9419 | -1.043 | 0.2971 |  |
| Kidney disease | +2.8807 | 3.0038 | ±6.0076 | +0.959 | 0.3376 |  |
| Circulatory disease | -0.3116 | 2.2574 | ±4.5148 | -0.138 | 0.8902 |  |
| **Mean glucose (mg/dL)** | **+0.1455** | 0.0613 | ±0.1226 | **+2.374** | **0.0176** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **598**, R² = **0.1100**, Adj R² = **0.0933**, F-statistic = **6.59** (p = **2.04e-10**), Residual SE = **16.879** on **586** df, AIC = **5088.9**, BIC = **5141.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.8402 | 16.0838 | ±32.1677 | +0.487 | 0.6259 |  |
| **Education: graduate level (vs college)** | **-3.8518** | 1.5247 | ±3.0494 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | -0.9630 | 2.4459 | ±4.8917 | -0.394 | 0.6938 |  |
| Site: UCSD (vs UAB) | +1.0483 | 1.8941 | ±3.7882 | +0.553 | 0.5799 |  |
| Site: UW (vs UAB) | -1.7898 | 1.7544 | ±3.5088 | -1.020 | 0.3076 |  |
| **Age (years)** | **-0.1915** | 0.0706 | ±0.1412 | **-2.713** | **0.0067** | ** |
| **BMI (kg/m2)** | **+0.5740** | 0.1435 | ±0.2870 | **+4.000** | **6.34e-05** | *** |
| Hypertension | +0.5744 | 1.6813 | ±3.3625 | +0.342 | 0.7326 |  |
| High cholesterol | -1.5338 | 1.4710 | ±2.9419 | -1.043 | 0.2971 |  |
| Kidney disease | +2.8807 | 3.0038 | ±6.0076 | +0.959 | 0.3376 |  |
| Circulatory disease | -0.3116 | 2.2574 | ±4.5148 | -0.138 | 0.8902 |  |
| **GMI (%)** | **+6.0838** | 2.5629 | ±5.1258 | **+2.374** | **0.0176** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **598**, R² = **0.1144**, Adj R² = **0.0978**, F-statistic = **6.88** (p = **5.68e-11**), Residual SE = **16.837** on **586** df, AIC = **5085.9**, BIC = **5138.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.7830** | 8.1681 | ±16.3362 | **+3.279** | **0.0010** | ** |
| **Education: graduate level (vs college)** | **-3.7834** | 1.5175 | ±3.0349 | **-2.493** | **0.0127** | * |
| Education: high school or below (vs college) | -1.0742 | 2.4497 | ±4.8994 | -0.438 | 0.6610 |  |
| Site: UCSD (vs UAB) | +0.8602 | 1.8849 | ±3.7699 | +0.456 | 0.6481 |  |
| Site: UW (vs UAB) | -1.8925 | 1.7514 | ±3.5028 | -1.081 | 0.2799 |  |
| **Age (years)** | **-0.1761** | 0.0697 | ±0.1394 | **-2.527** | **0.0115** | * |
| **BMI (kg/m2)** | **+0.5353** | 0.1405 | ±0.2811 | **+3.809** | **1.40e-04** | *** |
| Hypertension | +0.6255 | 1.6746 | ±3.3493 | +0.374 | 0.7088 |  |
| High cholesterol | -1.7193 | 1.4679 | ±2.9359 | -1.171 | 0.2415 |  |
| Kidney disease | +3.0276 | 2.9643 | ±5.9285 | +1.021 | 0.3071 |  |
| Circulatory disease | -0.2374 | 2.2370 | ±4.4739 | -0.106 | 0.9155 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.1583** | 0.0539 | ±0.1078 | **+2.938** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **598**, R² = **0.1062**, Adj R² = **0.0895**, F-statistic = **6.33** (p = **6.07e-10**), Residual SE = **16.915** on **586** df, AIC = **5091.4**, BIC = **5144.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.5765** | 7.6601 | ±15.3203 | **+5.036** | **4.75e-07** | *** |
| **Education: graduate level (vs college)** | **-3.5566** | 1.5325 | ±3.0649 | **-2.321** | **0.0203** | * |
| Education: high school or below (vs college) | -0.9298 | 2.4494 | ±4.8988 | -0.380 | 0.7042 |  |
| Site: UCSD (vs UAB) | +1.0244 | 1.8989 | ±3.7979 | +0.539 | 0.5896 |  |
| Site: UW (vs UAB) | -1.7153 | 1.7534 | ±3.5067 | -0.978 | 0.3279 |  |
| **Age (years)** | **-0.1949** | 0.0719 | ±0.1439 | **-2.710** | **0.0067** | ** |
| **BMI (kg/m2)** | **+0.5949** | 0.1442 | ±0.2883 | **+4.127** | **3.68e-05** | *** |
| Hypertension | +0.6077 | 1.6935 | ±3.3869 | +0.359 | 0.7197 |  |
| High cholesterol | -1.5014 | 1.4727 | ±2.9454 | -1.019 | 0.3080 |  |
| Kidney disease | +3.0478 | 3.0014 | ±6.0028 | +1.015 | 0.3099 |  |
| Circulatory disease | -0.0498 | 2.2551 | ±4.5102 | -0.022 | 0.9824 |  |
| Glucose SD, pooled (mg/dL) | +0.3166 | 0.1955 | ±0.3911 | +1.619 | 0.1055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **598**, R² = **0.1050**, Adj R² = **0.0882**, F-statistic = **6.25** (p = **8.58e-10**), Residual SE = **16.926** on **586** df, AIC = **5092.2**, BIC = **5145.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.7573** | 7.5597 | ±15.1194 | **+5.259** | **1.45e-07** | *** |
| **Education: graduate level (vs college)** | **-3.6144** | 1.5327 | ±3.0653 | **-2.358** | **0.0184** | * |
| Education: high school or below (vs college) | -0.9485 | 2.4504 | ±4.9008 | -0.387 | 0.6987 |  |
| Site: UCSD (vs UAB) | +1.0152 | 1.9016 | ±3.8031 | +0.534 | 0.5934 |  |
| Site: UW (vs UAB) | -1.6900 | 1.7570 | ±3.5140 | -0.962 | 0.3361 |  |
| **Age (years)** | **-0.1934** | 0.0719 | ±0.1438 | **-2.690** | **0.0071** | ** |
| **BMI (kg/m2)** | **+0.5942** | 0.1443 | ±0.2887 | **+4.117** | **3.84e-05** | *** |
| Hypertension | +0.6536 | 1.6960 | ±3.3919 | +0.385 | 0.6999 |  |
| High cholesterol | -1.4894 | 1.4748 | ±2.9495 | -1.010 | 0.3125 |  |
| Kidney disease | +3.0564 | 3.0181 | ±6.0363 | +1.013 | 0.3112 |  |
| Circulatory disease | -0.0628 | 2.2635 | ±4.5271 | -0.028 | 0.9779 |  |
| Avg. daily SD (mg/dL) | +0.2744 | 0.2003 | ±0.4005 | +1.370 | 0.1707 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **598**, R² = **0.1025**, Adj R² = **0.0856**, F-statistic = **6.08** (p = **1.79e-09**), Residual SE = **16.951** on **586** df, AIC = **5094.0**, BIC = **5146.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.3289** | 8.2345 | ±16.4690 | **+5.019** | **5.19e-07** | *** |
| **Education: graduate level (vs college)** | **-3.6232** | 1.5454 | ±3.0908 | **-2.345** | **0.0191** | * |
| Education: high school or below (vs college) | -0.9358 | 2.4621 | ±4.9242 | -0.380 | 0.7039 |  |
| Site: UCSD (vs UAB) | +0.8337 | 1.9065 | ±3.8131 | +0.437 | 0.6619 |  |
| Site: UW (vs UAB) | -1.5908 | 1.7565 | ±3.5129 | -0.906 | 0.3651 |  |
| **Age (years)** | **-0.1868** | 0.0717 | ±0.1434 | **-2.606** | **0.0092** | ** |
| **BMI (kg/m2)** | **+0.6041** | 0.1461 | ±0.2923 | **+4.134** | **3.57e-05** | *** |
| Hypertension | +0.7266 | 1.6922 | ±3.3845 | +0.429 | 0.6677 |  |
| High cholesterol | -1.4696 | 1.4761 | ±2.9523 | -0.996 | 0.3194 |  |
| Kidney disease | +3.1683 | 3.0173 | ±6.0345 | +1.050 | 0.2937 |  |
| Circulatory disease | -0.0279 | 2.2730 | ±4.5461 | -0.012 | 0.9902 |  |
| CV (%) | +0.1582 | 0.2654 | ±0.5307 | +0.596 | 0.5511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **598**, R² = **0.1030**, Adj R² = **0.0861**, F-statistic = **6.12** (p = **1.54e-09**), Residual SE = **16.946** on **586** df, AIC = **5093.6**, BIC = **5146.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2823** | 8.4354 | ±16.8708 | **+5.605** | **2.08e-08** | *** |
| **Education: graduate level (vs college)** | **-3.5827** | 1.5434 | ±3.0867 | **-2.321** | **0.0203** | * |
| Education: high school or below (vs college) | -0.9431 | 2.4568 | ±4.9135 | -0.384 | 0.7011 |  |
| Site: UCSD (vs UAB) | +0.8412 | 1.9058 | ±3.8116 | +0.441 | 0.6589 |  |
| Site: UW (vs UAB) | -1.6188 | 1.7562 | ±3.5124 | -0.922 | 0.3566 |  |
| **Age (years)** | **-0.1874** | 0.0715 | ±0.1429 | **-2.622** | **0.0088** | ** |
| **BMI (kg/m2)** | **+0.6043** | 0.1461 | ±0.2921 | **+4.137** | **3.52e-05** | *** |
| Hypertension | +0.7076 | 1.6927 | ±3.3853 | +0.418 | 0.6759 |  |
| High cholesterol | -1.4604 | 1.4760 | ±2.9519 | -0.989 | 0.3225 |  |
| Kidney disease | +3.1574 | 3.0102 | ±6.0203 | +1.049 | 0.2942 |  |
| Circulatory disease | -0.0087 | 2.2727 | ±4.5455 | -0.004 | 0.9970 |  |
| Mean / SD ratio | -0.5294 | 0.6328 | ±1.2656 | -0.837 | 0.4028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **598**, R² = **0.1025**, Adj R² = **0.0857**, F-statistic = **6.08** (p = **1.76e-09**), Residual SE = **16.950** on **586** df, AIC = **5093.9**, BIC = **5146.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.3275** | 8.4171 | ±16.8341 | **+5.504** | **3.71e-08** | *** |
| **Education: graduate level (vs college)** | **-3.6328** | 1.5413 | ±3.0827 | **-2.357** | **0.0184** | * |
| Education: high school or below (vs college) | -0.9566 | 2.4596 | ±4.9192 | -0.389 | 0.6973 |  |
| Site: UCSD (vs UAB) | +0.8353 | 1.9082 | ±3.8164 | +0.438 | 0.6616 |  |
| Site: UW (vs UAB) | -1.6124 | 1.7590 | ±3.5180 | -0.917 | 0.3593 |  |
| **Age (years)** | **-0.1867** | 0.0715 | ±0.1430 | **-2.612** | **0.0090** | ** |
| **BMI (kg/m2)** | **+0.6019** | 0.1459 | ±0.2918 | **+4.125** | **3.70e-05** | *** |
| Hypertension | +0.7491 | 1.6925 | ±3.3849 | +0.443 | 0.6581 |  |
| High cholesterol | -1.4608 | 1.4766 | ±2.9532 | -0.989 | 0.3225 |  |
| Kidney disease | +3.1549 | 3.0212 | ±6.0424 | +1.044 | 0.2964 |  |
| Circulatory disease | -0.0294 | 2.2772 | ±4.5544 | -0.013 | 0.9897 |  |
| Avg. daily mean/SD | -0.3291 | 0.5221 | ±1.0442 | -0.630 | 0.5284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **598**, R² = **0.1063**, Adj R² = **0.0896**, F-statistic = **6.34** (p = **5.91e-10**), Residual SE = **16.914** on **586** df, AIC = **5091.4**, BIC = **5144.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.2653** | 7.9535 | ±15.9070 | **+4.685** | **2.79e-06** | *** |
| **Education: graduate level (vs college)** | **-3.6596** | 1.5266 | ±3.0532 | **-2.397** | **0.0165** | * |
| Education: high school or below (vs college) | -1.2932 | 2.4911 | ±4.9822 | -0.519 | 0.6037 |  |
| Site: UCSD (vs UAB) | +0.8896 | 1.9052 | ±3.8103 | +0.467 | 0.6406 |  |
| Site: UW (vs UAB) | -1.5543 | 1.7508 | ±3.5015 | -0.888 | 0.3747 |  |
| **Age (years)** | **-0.1830** | 0.0709 | ±0.1419 | **-2.580** | **0.0099** | ** |
| **BMI (kg/m2)** | **+0.6041** | 0.1432 | ±0.2865 | **+4.217** | **2.47e-05** | *** |
| Hypertension | +0.9187 | 1.6938 | ±3.3877 | +0.542 | 0.5875 |  |
| High cholesterol | -1.4763 | 1.4709 | ±2.9418 | -1.004 | 0.3155 |  |
| Kidney disease | +2.9511 | 3.0194 | ±6.0388 | +0.977 | 0.3284 |  |
| Circulatory disease | +0.0826 | 2.2772 | ±4.5544 | +0.036 | 0.9711 |  |
| MAG (mg/dL/h) | +0.1772 | 0.1128 | ±0.2256 | +1.571 | 0.1161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **598**, R² = **0.1054**, Adj R² = **0.0886**, F-statistic = **6.28** (p = **7.75e-10**), Residual SE = **16.923** on **586** df, AIC = **5092.0**, BIC = **5144.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.2665** | 8.1535 | ±16.3070 | **+4.693** | **2.69e-06** | *** |
| **Education: graduate level (vs college)** | **-3.6707** | 1.5314 | ±3.0629 | **-2.397** | **0.0165** | * |
| Education: high school or below (vs college) | -1.0660 | 2.4564 | ±4.9129 | -0.434 | 0.6643 |  |
| Site: UCSD (vs UAB) | +0.9210 | 1.9089 | ±3.8177 | +0.482 | 0.6295 |  |
| Site: UW (vs UAB) | -1.7000 | 1.7528 | ±3.5056 | -0.970 | 0.3321 |  |
| **Age (years)** | **-0.1922** | 0.0716 | ±0.1433 | **-2.683** | **0.0073** | ** |
| **BMI (kg/m2)** | **+0.6088** | 0.1464 | ±0.2927 | **+4.159** | **3.19e-05** | *** |
| Hypertension | +0.7305 | 1.6969 | ±3.3937 | +0.430 | 0.6668 |  |
| High cholesterol | -1.4443 | 1.4754 | ±2.9509 | -0.979 | 0.3276 |  |
| Kidney disease | +3.0215 | 3.0178 | ±6.0355 | +1.001 | 0.3167 |  |
| Circulatory disease | -0.0995 | 2.2672 | ±4.5344 | -0.044 | 0.9650 |  |
| Avg. daily range (mg/dL) | +0.0658 | 0.0448 | ±0.0897 | +1.468 | 0.1421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **598**, R² = **0.1094**, Adj R² = **0.0927**, F-statistic = **6.54** (p = **2.47e-10**), Residual SE = **16.885** on **586** df, AIC = **5089.3**, BIC = **5142.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.4232** | 7.1385 | ±14.2771 | **+5.663** | **1.49e-08** | *** |
| **Education: graduate level (vs college)** | **-3.7098** | 1.5250 | ±3.0501 | **-2.433** | **0.0150** | * |
| Education: high school or below (vs college) | -0.9104 | 2.4456 | ±4.8911 | -0.372 | 0.7097 |  |
| Site: UCSD (vs UAB) | +0.8978 | 1.8944 | ±3.7889 | +0.474 | 0.6356 |  |
| Site: UW (vs UAB) | -1.6281 | 1.7386 | ±3.4772 | -0.936 | 0.3491 |  |
| **Age (years)** | **-0.1822** | 0.0704 | ±0.1409 | **-2.587** | **0.0097** | ** |
| **BMI (kg/m2)** | **+0.5776** | 0.1431 | ±0.2861 | **+4.037** | **5.41e-05** | *** |
| Hypertension | +0.7716 | 1.6729 | ±3.3457 | +0.461 | 0.6446 |  |
| High cholesterol | -1.6631 | 1.4656 | ±2.9312 | -1.135 | 0.2565 |  |
| Kidney disease | +3.2357 | 2.9368 | ±5.8736 | +1.102 | 0.2706 |  |
| Circulatory disease | -0.0987 | 2.2419 | ±4.4838 | -0.044 | 0.9649 |  |
| **SD of daily means (mg/dL)** | **+0.7015** | 0.3317 | ±0.6633 | **+2.115** | **0.0344** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **598**, R² = **0.1027**, Adj R² = **0.0859**, F-statistic = **6.10** (p = **1.65e-09**), Residual SE = **16.948** on **586** df, AIC = **5093.8**, BIC = **5146.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0354** | 22.8572 | ±45.7144 | **+2.758** | **0.0058** | ** |
| **Education: graduate level (vs college)** | **-3.7053** | 1.5338 | ±3.0676 | **-2.416** | **0.0157** | * |
| Education: high school or below (vs college) | -0.9027 | 2.4616 | ±4.9232 | -0.367 | 0.7138 |  |
| Site: UCSD (vs UAB) | +0.8534 | 1.9064 | ±3.8127 | +0.448 | 0.6544 |  |
| Site: UW (vs UAB) | -1.6105 | 1.7602 | ±3.5204 | -0.915 | 0.3602 |  |
| **Age (years)** | **-0.1868** | 0.0714 | ±0.1428 | **-2.617** | **0.0089** | ** |
| **BMI (kg/m2)** | **+0.5993** | 0.1459 | ±0.2919 | **+4.106** | **4.02e-05** | *** |
| Hypertension | +0.7701 | 1.6893 | ±3.3786 | +0.456 | 0.6485 |  |
| High cholesterol | -1.5436 | 1.4761 | ±2.9521 | -1.046 | 0.2957 |  |
| Kidney disease | +3.1326 | 3.0132 | ±6.0264 | +1.040 | 0.2985 |  |
| Circulatory disease | -0.1625 | 2.2661 | ±4.5322 | -0.072 | 0.9428 |  |
| Time in range 70-180, pooled (%) | -0.1931 | 0.2090 | ±0.4180 | -0.924 | 0.3556 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **598**, R² = **0.1025**, Adj R² = **0.0857**, F-statistic = **6.09** (p = **1.75e-09**), Residual SE = **16.950** on **586** df, AIC = **5093.9**, BIC = **5146.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.2265** | 23.6192 | ±47.2384 | **+2.592** | **0.0095** | ** |
| **Education: graduate level (vs college)** | **-3.7082** | 1.5339 | ±3.0677 | **-2.418** | **0.0156** | * |
| Education: high school or below (vs college) | -0.8969 | 2.4627 | ±4.9255 | -0.364 | 0.7157 |  |
| Site: UCSD (vs UAB) | +0.8485 | 1.9064 | ±3.8128 | +0.445 | 0.6563 |  |
| Site: UW (vs UAB) | -1.5978 | 1.7593 | ±3.5186 | -0.908 | 0.3638 |  |
| **Age (years)** | **-0.1862** | 0.0714 | ±0.1427 | **-2.610** | **0.0091** | ** |
| **BMI (kg/m2)** | **+0.5988** | 0.1461 | ±0.2922 | **+4.099** | **4.16e-05** | *** |
| Hypertension | +0.7751 | 1.6898 | ±3.3796 | +0.459 | 0.6465 |  |
| High cholesterol | -1.5375 | 1.4762 | ±2.9523 | -1.042 | 0.2976 |  |
| Kidney disease | +3.1353 | 3.0162 | ±6.0325 | +1.039 | 0.2986 |  |
| Circulatory disease | -0.1639 | 2.2694 | ±4.5387 | -0.072 | 0.9424 |  |
| Avg. daily time in range 70-180 (%) | -0.1747 | 0.2160 | ±0.4319 | -0.809 | 0.4184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.94e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.5064** | 7.2961 | ±14.5923 | **+6.100** | **1.06e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9748** | 1.5514 | ±3.1027 | **-2.562** | **0.0104** | * |
| Education: high school or below (vs college) | -1.2306 | 2.4697 | ±4.9393 | -0.498 | 0.6183 |  |
| Site: UCSD (vs UAB) | +0.9415 | 1.8982 | ±3.7964 | +0.496 | 0.6199 |  |
| Site: UW (vs UAB) | -1.5723 | 1.7537 | ±3.5074 | -0.897 | 0.3700 |  |
| **Age (years)** | **-0.1858** | 0.0708 | ±0.1416 | **-2.625** | **0.0087** | ** |
| **BMI (kg/m2)** | **+0.5997** | 0.1467 | ±0.2934 | **+4.088** | **4.35e-05** | *** |
| Hypertension | +0.8033 | 1.6844 | ±3.3689 | +0.477 | 0.6335 |  |
| High cholesterol | -1.4351 | 1.4751 | ±2.9503 | -0.973 | 0.3306 |  |
| Kidney disease | +3.0873 | 3.0220 | ±6.0441 | +1.022 | 0.3070 |  |
| Circulatory disease | -0.1611 | 2.2759 | ±4.5517 | -0.071 | 0.9436 |  |
| Time 54-69, pooled (%) | -1.9359 | 1.2716 | ±2.5432 | -1.522 | 0.1279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.97e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.4174** | 7.2873 | ±14.5747 | **+6.095** | **1.09e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9844** | 1.5540 | ±3.1080 | **-2.564** | **0.0103** | * |
| Education: high school or below (vs college) | -1.2521 | 2.4719 | ±4.9438 | -0.507 | 0.6125 |  |
| Site: UCSD (vs UAB) | +0.9841 | 1.8977 | ±3.7954 | +0.519 | 0.6040 |  |
| Site: UW (vs UAB) | -1.5592 | 1.7535 | ±3.5070 | -0.889 | 0.3739 |  |
| **Age (years)** | **-0.1851** | 0.0707 | ±0.1415 | **-2.617** | **0.0089** | ** |
| **BMI (kg/m2)** | **+0.5999** | 0.1468 | ±0.2936 | **+4.087** | **4.38e-05** | *** |
| Hypertension | +0.7921 | 1.6848 | ±3.3696 | +0.470 | 0.6382 |  |
| High cholesterol | -1.4439 | 1.4750 | ±2.9500 | -0.979 | 0.3276 |  |
| Kidney disease | +3.0901 | 3.0222 | ±6.0445 | +1.022 | 0.3066 |  |
| Circulatory disease | -0.1897 | 2.2758 | ±4.5517 | -0.083 | 0.9336 |  |
| Avg. daily time 54-69 (%) | -1.8763 | 1.2846 | ±2.5691 | -1.461 | 0.1441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.94e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.5064** | 7.2961 | ±14.5923 | **+6.100** | **1.06e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9748** | 1.5514 | ±3.1027 | **-2.562** | **0.0104** | * |
| Education: high school or below (vs college) | -1.2306 | 2.4697 | ±4.9393 | -0.498 | 0.6183 |  |
| Site: UCSD (vs UAB) | +0.9415 | 1.8982 | ±3.7964 | +0.496 | 0.6199 |  |
| Site: UW (vs UAB) | -1.5723 | 1.7537 | ±3.5074 | -0.897 | 0.3700 |  |
| **Age (years)** | **-0.1858** | 0.0708 | ±0.1416 | **-2.625** | **0.0087** | ** |
| **BMI (kg/m2)** | **+0.5997** | 0.1467 | ±0.2934 | **+4.088** | **4.35e-05** | *** |
| Hypertension | +0.8033 | 1.6844 | ±3.3689 | +0.477 | 0.6335 |  |
| High cholesterol | -1.4351 | 1.4751 | ±2.9503 | -0.973 | 0.3306 |  |
| Kidney disease | +3.0873 | 3.0220 | ±6.0441 | +1.022 | 0.3070 |  |
| Circulatory disease | -0.1611 | 2.2759 | ±4.5517 | -0.071 | 0.9436 |  |
| Time < 70 (%) | -1.9359 | 1.2716 | ±2.5432 | -1.522 | 0.1279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **598**, R² = **0.1053**, Adj R² = **0.0885**, F-statistic = **6.27** (p = **7.97e-10**), Residual SE = **16.924** on **586** df, AIC = **5092.1**, BIC = **5144.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.4174** | 7.2873 | ±14.5747 | **+6.095** | **1.09e-09** | *** |
| **Education: graduate level (vs college)** | **-3.9844** | 1.5540 | ±3.1080 | **-2.564** | **0.0103** | * |
| Education: high school or below (vs college) | -1.2521 | 2.4719 | ±4.9438 | -0.507 | 0.6125 |  |
| Site: UCSD (vs UAB) | +0.9841 | 1.8977 | ±3.7954 | +0.519 | 0.6040 |  |
| Site: UW (vs UAB) | -1.5592 | 1.7535 | ±3.5070 | -0.889 | 0.3739 |  |
| **Age (years)** | **-0.1851** | 0.0707 | ±0.1415 | **-2.617** | **0.0089** | ** |
| **BMI (kg/m2)** | **+0.5999** | 0.1468 | ±0.2936 | **+4.087** | **4.38e-05** | *** |
| Hypertension | +0.7921 | 1.6848 | ±3.3696 | +0.470 | 0.6382 |  |
| High cholesterol | -1.4439 | 1.4750 | ±2.9500 | -0.979 | 0.3276 |  |
| Kidney disease | +3.0901 | 3.0222 | ±6.0445 | +1.022 | 0.3066 |  |
| Circulatory disease | -0.1897 | 2.2758 | ±4.5517 | -0.083 | 0.9336 |  |
| Avg. daily time < 70 (%) | -1.8763 | 1.2846 | ±2.5691 | -1.461 | 0.1441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **598**, R² = **0.1036**, Adj R² = **0.0867**, F-statistic = **6.15** (p = **1.31e-09**), Residual SE = **16.940** on **586** df, AIC = **5093.2**, BIC = **5146.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8191** | 7.2316 | ±14.4631 | **+6.059** | **1.37e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7377** | 1.5307 | ±3.0614 | **-2.442** | **0.0146** | * |
| Education: high school or below (vs college) | -0.9232 | 2.4592 | ±4.9183 | -0.375 | 0.7074 |  |
| Site: UCSD (vs UAB) | +0.9124 | 1.9037 | ±3.8075 | +0.479 | 0.6317 |  |
| Site: UW (vs UAB) | -1.6304 | 1.7609 | ±3.5219 | -0.926 | 0.3545 |  |
| **Age (years)** | **-0.1885** | 0.0714 | ±0.1427 | **-2.642** | **0.0083** | ** |
| **BMI (kg/m2)** | **+0.5974** | 0.1457 | ±0.2914 | **+4.100** | **4.14e-05** | *** |
| Hypertension | +0.7729 | 1.6896 | ±3.3792 | +0.457 | 0.6474 |  |
| High cholesterol | -1.5641 | 1.4758 | ±2.9517 | -1.060 | 0.2892 |  |
| Kidney disease | +3.0987 | 3.0109 | ±6.0217 | +1.029 | 0.3034 |  |
| Circulatory disease | -0.2084 | 2.2633 | ±4.5266 | -0.092 | 0.9266 |  |
| Time 181-250, pooled (%) | +0.2662 | 0.2140 | ±0.4280 | +1.244 | 0.2136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **598**, R² = **0.1033**, Adj R² = **0.0865**, F-statistic = **6.14** (p = **1.40e-09**), Residual SE = **16.942** on **586** df, AIC = **5093.4**, BIC = **5146.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8431** | 7.2278 | ±14.4556 | **+6.066** | **1.31e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7419** | 1.5306 | ±3.0611 | **-2.445** | **0.0145** | * |
| Education: high school or below (vs college) | -0.9133 | 2.4591 | ±4.9182 | -0.371 | 0.7103 |  |
| Site: UCSD (vs UAB) | +0.9179 | 1.9034 | ±3.8069 | +0.482 | 0.6297 |  |
| Site: UW (vs UAB) | -1.6140 | 1.7596 | ±3.5192 | -0.917 | 0.3590 |  |
| **Age (years)** | **-0.1878** | 0.0713 | ±0.1426 | **-2.633** | **0.0085** | ** |
| **BMI (kg/m2)** | **+0.5964** | 0.1457 | ±0.2915 | **+4.093** | **4.26e-05** | *** |
| Hypertension | +0.7784 | 1.6900 | ±3.3801 | +0.461 | 0.6451 |  |
| High cholesterol | -1.5620 | 1.4762 | ±2.9524 | -1.058 | 0.2900 |  |
| Kidney disease | +3.0990 | 3.0141 | ±6.0282 | +1.028 | 0.3039 |  |
| Circulatory disease | -0.2212 | 2.2661 | ±4.5322 | -0.098 | 0.9222 |  |
| Avg. daily time 181-250 (%) | +0.2547 | 0.2197 | ±0.4394 | +1.159 | 0.2463 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **598**, R² = **0.1036**, Adj R² = **0.0867**, F-statistic = **6.15** (p = **1.31e-09**), Residual SE = **16.940** on **586** df, AIC = **5093.2**, BIC = **5146.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8191** | 7.2316 | ±14.4631 | **+6.059** | **1.37e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7377** | 1.5307 | ±3.0614 | **-2.442** | **0.0146** | * |
| Education: high school or below (vs college) | -0.9232 | 2.4592 | ±4.9183 | -0.375 | 0.7074 |  |
| Site: UCSD (vs UAB) | +0.9124 | 1.9037 | ±3.8075 | +0.479 | 0.6317 |  |
| Site: UW (vs UAB) | -1.6304 | 1.7609 | ±3.5219 | -0.926 | 0.3545 |  |
| **Age (years)** | **-0.1885** | 0.0714 | ±0.1427 | **-2.642** | **0.0083** | ** |
| **BMI (kg/m2)** | **+0.5974** | 0.1457 | ±0.2914 | **+4.100** | **4.14e-05** | *** |
| Hypertension | +0.7729 | 1.6896 | ±3.3792 | +0.457 | 0.6474 |  |
| High cholesterol | -1.5641 | 1.4758 | ±2.9517 | -1.060 | 0.2892 |  |
| Kidney disease | +3.0987 | 3.0109 | ±6.0217 | +1.029 | 0.3034 |  |
| Circulatory disease | -0.2084 | 2.2633 | ±4.5266 | -0.092 | 0.9266 |  |
| Time > 180 (%) | +0.2662 | 0.2140 | ±0.4280 | +1.244 | 0.2136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **598**, R² = **0.1033**, Adj R² = **0.0865**, F-statistic = **6.14** (p = **1.40e-09**), Residual SE = **16.942** on **586** df, AIC = **5093.4**, BIC = **5146.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8431** | 7.2278 | ±14.4556 | **+6.066** | **1.31e-09** | *** |
| **Education: graduate level (vs college)** | **-3.7419** | 1.5306 | ±3.0611 | **-2.445** | **0.0145** | * |
| Education: high school or below (vs college) | -0.9133 | 2.4591 | ±4.9182 | -0.371 | 0.7103 |  |
| Site: UCSD (vs UAB) | +0.9179 | 1.9034 | ±3.8069 | +0.482 | 0.6297 |  |
| Site: UW (vs UAB) | -1.6140 | 1.7596 | ±3.5192 | -0.917 | 0.3590 |  |
| **Age (years)** | **-0.1878** | 0.0713 | ±0.1426 | **-2.633** | **0.0085** | ** |
| **BMI (kg/m2)** | **+0.5964** | 0.1457 | ±0.2915 | **+4.093** | **4.26e-05** | *** |
| Hypertension | +0.7784 | 1.6900 | ±3.3801 | +0.461 | 0.6451 |  |
| High cholesterol | -1.5620 | 1.4762 | ±2.9524 | -1.058 | 0.2900 |  |
| Kidney disease | +3.0990 | 3.0141 | ±6.0282 | +1.028 | 0.3039 |  |
| Circulatory disease | -0.2212 | 2.2661 | ±4.5322 | -0.098 | 0.9222 |  |
| Avg. daily time > 180 (%) | +0.2547 | 0.2197 | ±0.4394 | +1.159 | 0.2463 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 598)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **598**, R² = **0.1035**, Adj R² = **0.0867**, F-statistic = **6.15** (p = **1.33e-09**), Residual SE = **16.941** on **586** df, AIC = **5093.3**, BIC = **5146.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.8282** | 7.2185 | ±14.4370 | **+6.072** | **1.27e-09** | *** |
| **Education: graduate level (vs college)** | **-3.6894** | 1.5306 | ±3.0613 | **-2.410** | **0.0159** | * |
| Education: high school or below (vs college) | -1.0457 | 2.4612 | ±4.9224 | -0.425 | 0.6709 |  |
| Site: UCSD (vs UAB) | +0.8445 | 1.8973 | ±3.7946 | +0.445 | 0.6563 |  |
| Site: UW (vs UAB) | -1.6268 | 1.7560 | ±3.5120 | -0.926 | 0.3542 |  |
| **Age (years)** | **-0.1810** | 0.0707 | ±0.1413 | **-2.561** | **0.0104** | * |
| **BMI (kg/m2)** | **+0.5899** | 0.1464 | ±0.2928 | **+4.029** | **5.60e-05** | *** |
| Hypertension | +0.8148 | 1.6872 | ±3.3743 | +0.483 | 0.6292 |  |
| High cholesterol | -1.6446 | 1.4794 | ±2.9588 | -1.112 | 0.2663 |  |
| Kidney disease | +3.2047 | 3.0076 | ±6.0152 | +1.066 | 0.2866 |  |
| Circulatory disease | -0.0822 | 2.2608 | ±4.5216 | -0.036 | 0.9710 |  |
| Nocturnal time > 180 (%) | +0.2272 | 0.1646 | ±0.3292 | +1.380 | 0.1676 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 115 single-predictor tests; 24 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 115 tests (samples with n >= 500), of which **10** are significant at BH q < 0.05 in the all-tests family and 14 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 593): best single predictor out of sample is **MAG** (CV R² 0.087 vs 0.068 for covariates alone, gain +0.019; +610 per SD, p = 4.1e-04, q = 0.017). FDR-robust associations (1): MAG (higher outcome, +610 per SD, q = 0.017).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 593): best single predictor out of sample is **MAG** (CV R² 0.114 vs 0.089 for covariates alone, gain +0.025; +2.15 per SD, p = 2.3e-05, q = 0.004). FDR-robust associations (1): MAG (higher outcome, +2.15 per SD, q = 0.004).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 597): best single predictor out of sample is **Nocturnal mean** (CV R² 0.117 vs 0.104 for covariates alone, gain +0.013; +0.975 per SD, p = 7.6e-04, q = 0.025). FDR-robust associations (8): %181-250 (daily avg) (higher outcome, +0.863 per SD, q = 0.004); %>180 (daily avg) (higher outcome, +0.863 per SD, q = 0.004); %181-250 (pooled) (higher outcome, +0.833 per SD, q = 0.004); %>180 (pooled) (higher outcome, +0.833 per SD, q = 0.004); TIR 70-180 (daily avg) (lower outcome, -0.76 per SD, q = 0.017); TIR 70-180 (pooled) (lower outcome, -0.725 per SD, q = 0.017); ....
- **Total sleep time per night (min)** (n = 601): best single predictor out of sample is **HbA1c** (CV R² -0.014 vs -0.025 for covariates alone, gain +0.011; -7.77 per SD, p = 0.013, q = 0.254). No association survives FDR; nominal only: HbA1c (p = 0.013).
- **Garmin stress score, mean (0-100)** (n = 598): best single predictor out of sample is **Nocturnal mean** (CV R² 0.068 vs 0.060 for covariates alone, gain +0.008; +2.06 per SD, p = 0.003, q = 0.083). No association survives FDR; nominal only: Nocturnal mean (p = 0.003), GMI (p = 0.018), Mean glucose (p = 0.018), SD of daily means (p = 0.034).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Brisk-cadence minutes per day (>= 100 steps/min) (+0.025, via MAG); Steps per wear-day (+0.019, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.013, via Nocturnal mean); Total sleep time per night (min) (+0.011, via HbA1c). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band > 180 (3 FDR-significant / 3 raw-significant of 15); CGM variability (2 FDR-significant / 8 raw-significant of 40); Range 70-180 (2 FDR-significant / 2 raw-significant of 10).
Level metrics: 1 FDR-significant (6 raw); variability metrics: 2 FDR-significant (8 raw); HbA1c alone: 0 FDR-significant (3 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Steps per wear-day (MAG, ΔAIC -10.9); Brisk-cadence minutes per day (MAG, ΔAIC -17.3); Resting heart-rate proxy (MAG, ΔAIC -5.2); Garmin stress score, mean (Nocturnal mean, ΔAIC -5.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
