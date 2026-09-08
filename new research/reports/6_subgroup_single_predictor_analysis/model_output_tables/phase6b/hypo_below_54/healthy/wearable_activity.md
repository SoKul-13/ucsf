# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 374; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **374**, R² = **0.1420**, Adj R² = **0.1183**, F-statistic = **6.01** (p = **1.90e-08**), Residual SE = **3795.242** on **363** df, AIC = **7236.8**, BIC = **7280.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19637.7130** | 1571.6648 | ±3143.3297 | **+12.495** | **7.96e-36** | *** |
| Education: graduate level (vs college) | -439.5686 | 469.7341 | ±939.4682 | -0.936 | 0.3494 |  |
| Education: high school or below (vs college) | +786.7877 | 884.9350 | ±1769.8700 | +0.889 | 0.3740 |  |
| Site: UCSD (vs UAB) | +108.1039 | 555.0899 | ±1110.1798 | +0.195 | 0.8456 |  |
| Site: UW (vs UAB) | -54.9328 | 462.0779 | ±924.1557 | -0.119 | 0.9054 |  |
| **Age (years)** | **-131.8077** | 17.7977 | ±35.5954 | **-7.406** | **1.30e-13** | *** |
| BMI (kg/m2) | -55.4633 | 33.6683 | ±67.3366 | -1.647 | 0.0995 | . |
| Hypertension | -400.4022 | 476.5264 | ±953.0529 | -0.840 | 0.4008 |  |
| High cholesterol | -162.6440 | 409.6427 | ±819.2855 | -0.397 | 0.6913 |  |
| Kidney disease | -172.4596 | 1218.9239 | ±2437.8477 | -0.141 | 0.8875 |  |
| Circulatory disease | +76.7883 | 603.1413 | ±1206.2827 | +0.127 | 0.8987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **374**, R² = **0.1454**, Adj R² = **0.1195**, F-statistic = **5.60** (p = **2.59e-08**), Residual SE = **3792.785** on **362** df, AIC = **7237.3**, BIC = **7284.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16792.1466** | 2928.6647 | ±5857.3295 | **+5.734** | **9.83e-09** | *** |
| Education: graduate level (vs college) | -408.1919 | 469.4962 | ±938.9924 | -0.869 | 0.3846 |  |
| Education: high school or below (vs college) | +725.3074 | 886.4524 | ±1772.9048 | +0.818 | 0.4132 |  |
| Site: UCSD (vs UAB) | +5.9181 | 546.1608 | ±1092.3217 | +0.011 | 0.9914 |  |
| Site: UW (vs UAB) | -74.3025 | 458.4688 | ±916.9375 | -0.162 | 0.8713 |  |
| **Age (years)** | **-135.5981** | 17.7360 | ±35.4720 | **-7.645** | **2.08e-14** | *** |
| BMI (kg/m2) | -59.9847 | 34.0277 | ±68.0554 | -1.763 | 0.0779 | . |
| Hypertension | -390.2353 | 479.0451 | ±958.0902 | -0.815 | 0.4153 |  |
| High cholesterol | -247.8549 | 421.8144 | ±843.6288 | -0.588 | 0.5568 |  |
| Kidney disease | -207.0788 | 1217.1797 | ±2434.3594 | -0.170 | 0.8649 |  |
| Circulatory disease | +115.2588 | 607.6348 | ±1215.2695 | +0.190 | 0.8496 |  |
| HbA1c (%) | +577.3046 | 453.1047 | ±906.2094 | +1.274 | 0.2026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1160**, F-statistic = **5.45** (p = **4.75e-08**), Residual SE = **3800.176** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19988.4516** | 2036.7419 | ±4073.4839 | **+9.814** | **9.81e-23** | *** |
| Education: graduate level (vs college) | -434.0277 | 473.8073 | ±947.6146 | -0.916 | 0.3596 |  |
| Education: high school or below (vs college) | +797.3027 | 886.5809 | ±1773.1618 | +0.899 | 0.3685 |  |
| Site: UCSD (vs UAB) | +114.6154 | 553.3022 | ±1106.6043 | +0.207 | 0.8359 |  |
| Site: UW (vs UAB) | -42.3941 | 460.7248 | ±921.4496 | -0.092 | 0.9267 |  |
| **Age (years)** | **-131.5914** | 17.8523 | ±35.7045 | **-7.371** | **1.69e-13** | *** |
| BMI (kg/m2) | -55.0889 | 34.0508 | ±68.1015 | -1.618 | 0.1057 |  |
| Hypertension | -390.9048 | 479.2807 | ±958.5613 | -0.816 | 0.4147 |  |
| High cholesterol | -151.1031 | 414.6667 | ±829.3334 | -0.364 | 0.7156 |  |
| Kidney disease | -148.5705 | 1233.9465 | ±2467.8930 | -0.120 | 0.9042 |  |
| Circulatory disease | +75.9005 | 605.4628 | ±1210.9257 | +0.125 | 0.9002 |  |
| Mean glucose (mg/dL) | -3.4484 | 13.9762 | ±27.9523 | -0.247 | 0.8051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1160**, F-statistic = **5.45** (p = **4.75e-08**), Residual SE = **3800.176** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20465.6327** | 3591.2714 | ±7182.5428 | **+5.699** | **1.21e-08** | *** |
| Education: graduate level (vs college) | -434.0277 | 473.8073 | ±947.6146 | -0.916 | 0.3596 |  |
| Education: high school or below (vs college) | +797.3027 | 886.5809 | ±1773.1618 | +0.899 | 0.3685 |  |
| Site: UCSD (vs UAB) | +114.6154 | 553.3022 | ±1106.6043 | +0.207 | 0.8359 |  |
| Site: UW (vs UAB) | -42.3941 | 460.7248 | ±921.4496 | -0.092 | 0.9267 |  |
| **Age (years)** | **-131.5914** | 17.8523 | ±35.7045 | **-7.371** | **1.69e-13** | *** |
| BMI (kg/m2) | -55.0889 | 34.0508 | ±68.1015 | -1.618 | 0.1057 |  |
| Hypertension | -390.9048 | 479.2807 | ±958.5613 | -0.816 | 0.4147 |  |
| High cholesterol | -151.1031 | 414.6667 | ±829.3334 | -0.364 | 0.7156 |  |
| Kidney disease | -148.5705 | 1233.9465 | ±2467.8930 | -0.120 | 0.9042 |  |
| Circulatory disease | +75.9005 | 605.4628 | ±1210.9257 | +0.125 | 0.9002 |  |
| GMI (%) | -144.1635 | 584.2879 | ±1168.5759 | -0.247 | 0.8051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **374**, R² = **0.1424**, Adj R² = **0.1163**, F-statistic = **5.46** (p = **4.52e-08**), Residual SE = **3799.579** on **362** df, AIC = **7238.7**, BIC = **7285.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19081.8428** | 2060.0304 | ±4120.0608 | **+9.263** | **1.99e-20** | *** |
| Education: graduate level (vs college) | -442.9478 | 470.9230 | ±941.8460 | -0.941 | 0.3469 |  |
| Education: high school or below (vs college) | +766.5636 | 891.0257 | ±1782.0515 | +0.860 | 0.3896 |  |
| Site: UCSD (vs UAB) | +94.8726 | 552.9125 | ±1105.8251 | +0.172 | 0.8638 |  |
| Site: UW (vs UAB) | -72.1259 | 456.8311 | ±913.6621 | -0.158 | 0.8745 |  |
| **Age (years)** | **-131.6108** | 17.8623 | ±35.7245 | **-7.368** | **1.73e-13** | *** |
| BMI (kg/m2) | -57.1289 | 34.4259 | ±68.8518 | -1.659 | 0.0970 | . |
| Hypertension | -416.4904 | 480.3165 | ±960.6330 | -0.867 | 0.3859 |  |
| High cholesterol | -186.5254 | 415.8636 | ±831.7273 | -0.449 | 0.6538 |  |
| Kidney disease | -183.8490 | 1223.9617 | ±2447.9235 | -0.150 | 0.8806 |  |
| Circulatory disease | +85.9153 | 607.3600 | ±1214.7201 | +0.141 | 0.8875 |  |
| Nocturnal mean 00-06h (mg/dL) | +5.4838 | 13.5043 | ±27.0086 | +0.406 | 0.6847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1440**, Adj R² = **0.1179**, F-statistic = **5.53** (p = **3.39e-08**), Residual SE = **3796.067** on **362** df, AIC = **7238.0**, BIC = **7285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20142.1630** | 1680.2724 | ±3360.5449 | **+11.987** | **4.13e-33** | *** |
| Education: graduate level (vs college) | -423.8342 | 472.6225 | ±945.2450 | -0.897 | 0.3698 |  |
| Education: high school or below (vs college) | +798.7368 | 890.7300 | ±1781.4600 | +0.897 | 0.3699 |  |
| Site: UCSD (vs UAB) | +133.4205 | 551.6675 | ±1103.3349 | +0.242 | 0.8089 |  |
| Site: UW (vs UAB) | -46.8622 | 461.9808 | ±923.9615 | -0.101 | 0.9192 |  |
| **Age (years)** | **-129.6904** | 17.8845 | ±35.7690 | **-7.252** | **4.12e-13** | *** |
| BMI (kg/m2) | -55.8857 | 33.6587 | ±67.3174 | -1.660 | 0.0968 | . |
| Hypertension | -380.4672 | 476.1147 | ±952.2294 | -0.799 | 0.4242 |  |
| High cholesterol | -166.7985 | 410.1849 | ±820.3698 | -0.407 | 0.6843 |  |
| Kidney disease | -35.8553 | 1232.1015 | ±2464.2029 | -0.029 | 0.9768 |  |
| Circulatory disease | +68.7626 | 606.5286 | ±1213.0572 | +0.113 | 0.9097 |  |
| Glucose SD, pooled (mg/dL) | -29.5040 | 34.0908 | ±68.1816 | -0.865 | 0.3868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1438**, Adj R² = **0.1178**, F-statistic = **5.53** (p = **3.49e-08**), Residual SE = **3796.406** on **362** df, AIC = **7238.0**, BIC = **7285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20057.1862** | 1661.7055 | ±3323.4109 | **+12.070** | **1.52e-33** | *** |
| Education: graduate level (vs college) | -430.0140 | 471.8466 | ±943.6933 | -0.911 | 0.3621 |  |
| Education: high school or below (vs college) | +806.9718 | 892.2601 | ±1784.5202 | +0.904 | 0.3658 |  |
| Site: UCSD (vs UAB) | +144.7697 | 549.3903 | ±1098.7805 | +0.264 | 0.7922 |  |
| Site: UW (vs UAB) | -41.3687 | 461.8934 | ±923.7869 | -0.090 | 0.9286 |  |
| **Age (years)** | **-129.3328** | 17.9346 | ±35.8693 | **-7.211** | **5.54e-13** | *** |
| BMI (kg/m2) | -55.4118 | 33.7989 | ±67.5977 | -1.639 | 0.1011 |  |
| Hypertension | -381.8848 | 475.9933 | ±951.9866 | -0.802 | 0.4224 |  |
| High cholesterol | -164.8192 | 410.4248 | ±820.8496 | -0.402 | 0.6880 |  |
| Kidney disease | -41.0323 | 1233.8820 | ±2467.7640 | -0.033 | 0.9735 |  |
| Circulatory disease | +64.9375 | 605.4677 | ±1210.9354 | +0.107 | 0.9146 |  |
| Avg. daily SD (mg/dL) | -30.4706 | 38.1187 | ±76.2375 | -0.799 | 0.4241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **374**, R² = **0.1443**, Adj R² = **0.1183**, F-statistic = **5.55** (p = **3.18e-08**), Residual SE = **3795.275** on **362** df, AIC = **7237.8**, BIC = **7284.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20395.6953** | 1793.4665 | ±3586.9331 | **+11.372** | **5.75e-30** | *** |
| Education: graduate level (vs college) | -431.8728 | 470.1330 | ±940.2661 | -0.919 | 0.3583 |  |
| Education: high school or below (vs college) | +779.0683 | 894.4274 | ±1788.8547 | +0.871 | 0.3837 |  |
| Site: UCSD (vs UAB) | +127.5768 | 554.5406 | ±1109.0812 | +0.230 | 0.8180 |  |
| Site: UW (vs UAB) | -73.9795 | 463.8344 | ±927.6687 | -0.159 | 0.8733 |  |
| **Age (years)** | **-129.5711** | 17.8820 | ±35.7639 | **-7.246** | **4.30e-13** | *** |
| BMI (kg/m2) | -56.6971 | 33.7120 | ±67.4240 | -1.682 | 0.0926 | . |
| Hypertension | -395.2634 | 475.4048 | ±950.8096 | -0.831 | 0.4057 |  |
| High cholesterol | -193.8143 | 409.0566 | ±818.1132 | -0.474 | 0.6356 |  |
| Kidney disease | -52.8285 | 1217.9532 | ±2435.9065 | -0.043 | 0.9654 |  |
| Circulatory disease | +66.8132 | 605.7790 | ±1211.5581 | +0.110 | 0.9122 |  |
| CV (%) | -44.4031 | 46.1632 | ±92.3263 | -0.962 | 0.3361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **374**, R² = **0.1422**, Adj R² = **0.1161**, F-statistic = **5.45** (p = **4.70e-08**), Residual SE = **3800.053** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19312.2666** | 1947.4500 | ±3894.9000 | **+9.917** | **3.52e-23** | *** |
| Education: graduate level (vs college) | -432.4010 | 474.1575 | ±948.3150 | -0.912 | 0.3618 |  |
| Education: high school or below (vs college) | +789.7459 | 888.5272 | ±1777.0545 | +0.889 | 0.3741 |  |
| Site: UCSD (vs UAB) | +113.9513 | 555.8801 | ±1111.7602 | +0.205 | 0.8376 |  |
| Site: UW (vs UAB) | -55.5749 | 463.1909 | ±926.3817 | -0.120 | 0.9045 |  |
| **Age (years)** | **-131.0972** | 17.7892 | ±35.5784 | **-7.369** | **1.71e-13** | *** |
| BMI (kg/m2) | -55.5582 | 33.7330 | ±67.4660 | -1.647 | 0.0996 | . |
| Hypertension | -398.2877 | 477.3439 | ±954.6877 | -0.834 | 0.4041 |  |
| High cholesterol | -167.9585 | 409.3196 | ±818.6392 | -0.410 | 0.6816 |  |
| Kidney disease | -143.9780 | 1226.6747 | ±2453.3494 | -0.117 | 0.9066 |  |
| Circulatory disease | +74.2881 | 605.0679 | ±1210.1358 | +0.123 | 0.9023 |  |
| Mean / SD ratio | +51.3773 | 182.5333 | ±365.0666 | +0.281 | 0.7784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1160**, F-statistic = **5.45** (p = **4.76e-08**), Residual SE = **3800.209** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19896.9241** | 1931.1138 | ±3862.2276 | **+10.303** | **6.81e-25** | *** |
| Education: graduate level (vs college) | -445.1474 | 473.8056 | ±947.6112 | -0.940 | 0.3475 |  |
| Education: high school or below (vs college) | +778.9847 | 886.2456 | ±1772.4911 | +0.879 | 0.3794 |  |
| Site: UCSD (vs UAB) | +98.7277 | 555.5181 | ±1111.0361 | +0.178 | 0.8589 |  |
| Site: UW (vs UAB) | -56.0859 | 462.7508 | ±925.5016 | -0.121 | 0.9035 |  |
| **Age (years)** | **-132.4910** | 17.6869 | ±35.3737 | **-7.491** | **6.84e-14** | *** |
| BMI (kg/m2) | -55.5820 | 33.7504 | ±67.5008 | -1.647 | 0.0996 | . |
| Hypertension | -400.7473 | 478.1959 | ±956.3917 | -0.838 | 0.4020 |  |
| High cholesterol | -159.5473 | 409.3474 | ±818.6949 | -0.390 | 0.6967 |  |
| Kidney disease | -198.6499 | 1236.2273 | ±2472.4546 | -0.161 | 0.8723 |  |
| Circulatory disease | +80.1554 | 603.7335 | ±1207.4670 | +0.133 | 0.8944 |  |
| Avg. daily mean/SD | -32.7562 | 147.8300 | ±295.6601 | -0.222 | 0.8246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **374**, R² = **0.1450**, Adj R² = **0.1190**, F-statistic = **5.58** (p = **2.82e-08**), Residual SE = **3793.818** on **362** df, AIC = **7237.5**, BIC = **7284.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18378.4464** | 1900.0000 | ±3800.0001 | **+9.673** | **3.93e-22** | *** |
| Education: graduate level (vs college) | -438.4008 | 471.1726 | ±942.3452 | -0.930 | 0.3521 |  |
| Education: high school or below (vs college) | +821.4831 | 879.5040 | ±1759.0080 | +0.934 | 0.3503 |  |
| Site: UCSD (vs UAB) | +75.3853 | 552.1306 | ±1104.2612 | +0.137 | 0.8914 |  |
| Site: UW (vs UAB) | -2.9418 | 472.4036 | ±944.8072 | -0.006 | 0.9950 |  |
| **Age (years)** | **-130.6933** | 17.7046 | ±35.4093 | **-7.382** | **1.56e-13** | *** |
| BMI (kg/m2) | -54.1097 | 33.4185 | ±66.8370 | -1.619 | 0.1054 |  |
| Hypertension | -426.3099 | 476.3767 | ±952.7535 | -0.895 | 0.3708 |  |
| High cholesterol | -115.8703 | 404.1122 | ±808.2244 | -0.287 | 0.7743 |  |
| Kidney disease | -188.6395 | 1230.7121 | ±2461.4242 | -0.153 | 0.8782 |  |
| Circulatory disease | +82.5520 | 602.4795 | ±1204.9591 | +0.137 | 0.8910 |  |
| MAG (mg/dL/h) | +28.3679 | 25.3966 | ±50.7932 | +1.117 | 0.2640 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **374**, R² = **0.1426**, Adj R² = **0.1165**, F-statistic = **5.47** (p = **4.36e-08**), Residual SE = **3799.121** on **362** df, AIC = **7238.6**, BIC = **7285.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19984.2460** | 1736.0239 | ±3472.0479 | **+11.512** | **1.15e-30** | *** |
| Education: graduate level (vs college) | -438.7616 | 471.0214 | ±942.0427 | -0.932 | 0.3516 |  |
| Education: high school or below (vs college) | +795.5060 | 891.8471 | ±1783.6942 | +0.892 | 0.3724 |  |
| Site: UCSD (vs UAB) | +127.4136 | 550.8953 | ±1101.7905 | +0.231 | 0.8171 |  |
| Site: UW (vs UAB) | -52.9213 | 462.6319 | ±925.2638 | -0.114 | 0.9089 |  |
| **Age (years)** | **-130.5983** | 17.9580 | ±35.9160 | **-7.272** | **3.53e-13** | *** |
| BMI (kg/m2) | -56.7041 | 33.6527 | ±67.3055 | -1.685 | 0.0920 | . |
| Hypertension | -391.8444 | 476.2460 | ±952.4921 | -0.823 | 0.4106 |  |
| High cholesterol | -170.6107 | 408.9602 | ±817.9204 | -0.417 | 0.6765 |  |
| Kidney disease | -118.5109 | 1225.9777 | ±2451.9555 | -0.097 | 0.9230 |  |
| Circulatory disease | +71.6905 | 605.5124 | ±1211.0248 | +0.118 | 0.9058 |  |
| Avg. daily range (mg/dL) | -3.8860 | 8.3217 | ±16.6434 | -0.467 | 0.6405 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **374**, R² = **0.1422**, Adj R² = **0.1162**, F-statistic = **5.46** (p = **4.63e-08**), Residual SE = **3799.875** on **362** df, AIC = **7238.7**, BIC = **7285.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19766.1760** | 1634.0460 | ±3268.0920 | **+12.096** | **1.10e-33** | *** |
| Education: graduate level (vs college) | -429.3031 | 473.9677 | ±947.9354 | -0.906 | 0.3651 |  |
| Education: high school or below (vs college) | +774.4583 | 885.3411 | ±1770.6821 | +0.875 | 0.3817 |  |
| Site: UCSD (vs UAB) | +94.8656 | 557.8754 | ±1115.7509 | +0.170 | 0.8650 |  |
| Site: UW (vs UAB) | -55.9352 | 463.8959 | ±927.7918 | -0.121 | 0.9040 |  |
| **Age (years)** | **-131.8604** | 17.8661 | ±35.7323 | **-7.380** | **1.58e-13** | *** |
| BMI (kg/m2) | -55.2024 | 33.6861 | ±67.3721 | -1.639 | 0.1013 |  |
| Hypertension | -398.8921 | 477.7570 | ±955.5140 | -0.835 | 0.4038 |  |
| High cholesterol | -157.3098 | 412.4301 | ±824.8602 | -0.381 | 0.7029 |  |
| Kidney disease | -157.3143 | 1226.2581 | ±2452.5163 | -0.128 | 0.8979 |  |
| Circulatory disease | +79.1136 | 607.1075 | ±1214.2150 | +0.130 | 0.8963 |  |
| SD of daily means (mg/dL) | -18.9763 | 58.3586 | ±116.7173 | -0.325 | 0.7451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **374**, R² = **0.1436**, Adj R² = **0.1176**, F-statistic = **5.52** (p = **3.61e-08**), Residual SE = **3796.821** on **362** df, AIC = **7238.1**, BIC = **7285.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16540.5068** | 3236.4575 | ±6472.9151 | **+5.111** | **3.21e-07** | *** |
| Education: graduate level (vs college) | -442.3024 | 469.0305 | ±938.0610 | -0.943 | 0.3457 |  |
| Education: high school or below (vs college) | +787.0818 | 889.0668 | ±1778.1336 | +0.885 | 0.3760 |  |
| Site: UCSD (vs UAB) | +91.6656 | 557.3456 | ±1114.6913 | +0.164 | 0.8694 |  |
| Site: UW (vs UAB) | -75.9219 | 461.4604 | ±922.9208 | -0.165 | 0.8693 |  |
| **Age (years)** | **-130.8191** | 17.8095 | ±35.6191 | **-7.345** | **2.05e-13** | *** |
| BMI (kg/m2) | -55.5747 | 33.8054 | ±67.6107 | -1.644 | 0.1002 |  |
| Hypertension | -396.8083 | 476.7044 | ±953.4087 | -0.832 | 0.4052 |  |
| High cholesterol | -169.6930 | 409.3302 | ±818.6604 | -0.415 | 0.6785 |  |
| Kidney disease | -50.1184 | 1228.0507 | ±2456.1014 | -0.041 | 0.9674 |  |
| Circulatory disease | +43.8576 | 602.5938 | ±1205.1877 | +0.073 | 0.9420 |  |
| Time in range 70-180, pooled (%) | +31.9140 | 29.5089 | ±59.0177 | +1.082 | 0.2795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **374**, R² = **0.1432**, Adj R² = **0.1172**, F-statistic = **5.50** (p = **3.87e-08**), Residual SE = **3797.655** on **362** df, AIC = **7238.3**, BIC = **7285.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16981.7675** | 3217.4270 | ±6434.8540 | **+5.278** | **1.31e-07** | *** |
| Education: graduate level (vs college) | -443.4125 | 469.1638 | ±938.3276 | -0.945 | 0.3446 |  |
| Education: high school or below (vs college) | +782.9851 | 889.8345 | ±1779.6689 | +0.880 | 0.3789 |  |
| Site: UCSD (vs UAB) | +97.9868 | 556.9023 | ±1113.8045 | +0.176 | 0.8603 |  |
| Site: UW (vs UAB) | -72.5173 | 462.1525 | ±924.3050 | -0.157 | 0.8753 |  |
| **Age (years)** | **-130.7524** | 17.8134 | ±35.6268 | **-7.340** | **2.13e-13** | *** |
| BMI (kg/m2) | -55.2710 | 33.8189 | ±67.6379 | -1.634 | 0.1022 |  |
| Hypertension | -396.5118 | 477.0569 | ±954.1138 | -0.831 | 0.4059 |  |
| High cholesterol | -165.6638 | 409.5800 | ±819.1600 | -0.404 | 0.6859 |  |
| Kidney disease | -69.6265 | 1231.0156 | ±2462.0313 | -0.057 | 0.9549 |  |
| Circulatory disease | +48.3560 | 602.2401 | ±1204.4802 | +0.080 | 0.9360 |  |
| Avg. daily time in range 70-180 (%) | +27.0254 | 28.8850 | ±57.7701 | +0.936 | 0.3495 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **374**, R² = **0.1428**, Adj R² = **0.1167**, F-statistic = **5.48** (p = **4.19e-08**), Residual SE = **3798.640** on **362** df, AIC = **7238.5**, BIC = **7285.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19750.7516** | 1597.3444 | ±3194.6887 | **+12.365** | **4.06e-35** | *** |
| Education: graduate level (vs college) | -445.6441 | 470.2393 | ±940.4786 | -0.948 | 0.3433 |  |
| Education: high school or below (vs college) | +773.6018 | 889.1089 | ±1778.2178 | +0.870 | 0.3843 |  |
| Site: UCSD (vs UAB) | +61.0881 | 562.1640 | ±1124.3280 | +0.109 | 0.9135 |  |
| Site: UW (vs UAB) | -93.1648 | 460.6593 | ±921.3187 | -0.202 | 0.8397 |  |
| **Age (years)** | **-131.6248** | 17.8233 | ±35.6466 | **-7.385** | **1.52e-13** | *** |
| BMI (kg/m2) | -56.2107 | 33.8478 | ±67.6956 | -1.661 | 0.0968 | . |
| Hypertension | -418.7480 | 477.9488 | ±955.8976 | -0.876 | 0.3810 |  |
| High cholesterol | -187.5059 | 412.6958 | ±825.3916 | -0.454 | 0.6496 |  |
| Kidney disease | -152.7861 | 1216.4584 | ±2432.9167 | -0.126 | 0.9000 |  |
| Circulatory disease | +62.6915 | 601.9737 | ±1203.9473 | +0.104 | 0.9171 |  |
| Time < 54 (%) | -122.8686 | 149.2111 | ±298.4221 | -0.823 | 0.4102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1160**, F-statistic = **5.45** (p = **4.75e-08**), Residual SE = **3800.192** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19665.9114** | 1592.0481 | ±3184.0961 | **+12.353** | **4.72e-35** | *** |
| Education: graduate level (vs college) | -443.9392 | 471.7620 | ±943.5240 | -0.941 | 0.3467 |  |
| Education: high school or below (vs college) | +780.7689 | 887.8981 | ±1775.7961 | +0.879 | 0.3792 |  |
| Site: UCSD (vs UAB) | +91.9289 | 560.8956 | ±1121.7912 | +0.164 | 0.8698 |  |
| Site: UW (vs UAB) | -72.9514 | 462.1753 | ±924.3507 | -0.158 | 0.8746 |  |
| **Age (years)** | **-131.5347** | 17.8353 | ±35.6707 | **-7.375** | **1.64e-13** | *** |
| BMI (kg/m2) | -55.6721 | 33.9593 | ±67.9187 | -1.639 | 0.1011 |  |
| Hypertension | -409.6503 | 477.8662 | ±955.7324 | -0.857 | 0.3913 |  |
| High cholesterol | -172.8385 | 411.5827 | ±823.1653 | -0.420 | 0.6745 |  |
| Kidney disease | -165.1530 | 1218.8510 | ±2437.7020 | -0.135 | 0.8922 |  |
| Circulatory disease | +69.8939 | 600.9184 | ±1201.8368 | +0.116 | 0.9074 |  |
| Avg. daily time < 54 (%) | -63.8507 | 248.6794 | ±497.3588 | -0.257 | 0.7974 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **374**, R² = **0.1423**, Adj R² = **0.1162**, F-statistic = **5.46** (p = **4.60e-08**), Residual SE = **3799.783** on **362** df, AIC = **7238.7**, BIC = **7285.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19710.4252** | 1617.9837 | ±3235.9673 | **+12.182** | **3.87e-34** | *** |
| Education: graduate level (vs college) | -444.3983 | 470.0253 | ±940.0506 | -0.945 | 0.3444 |  |
| Education: high school or below (vs college) | +772.1811 | 888.2463 | ±1776.4927 | +0.869 | 0.3847 |  |
| Site: UCSD (vs UAB) | +91.9115 | 553.4128 | ±1106.8257 | +0.166 | 0.8681 |  |
| Site: UW (vs UAB) | -76.3124 | 456.8327 | ±913.6653 | -0.167 | 0.8673 |  |
| **Age (years)** | **-131.8590** | 17.8483 | ±35.6966 | **-7.388** | **1.49e-13** | *** |
| BMI (kg/m2) | -55.2559 | 33.8843 | ±67.7686 | -1.631 | 0.1029 |  |
| Hypertension | -413.6865 | 477.5557 | ±955.1113 | -0.866 | 0.3863 |  |
| High cholesterol | -174.8041 | 411.9592 | ±823.9184 | -0.424 | 0.6713 |  |
| Kidney disease | -169.5212 | 1219.6069 | ±2439.2138 | -0.139 | 0.8895 |  |
| Circulatory disease | +66.9875 | 601.0215 | ±1202.0430 | +0.111 | 0.9113 |  |
| Time 54-69, pooled (%) | -33.2855 | 106.1571 | ±212.3142 | -0.314 | 0.7539 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1160**, F-statistic = **5.45** (p = **4.74e-08**), Residual SE = **3800.142** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19677.8060** | 1607.0791 | ±3214.1581 | **+12.244** | **1.80e-34** | *** |
| Education: graduate level (vs college) | -444.1485 | 470.5154 | ±941.0307 | -0.944 | 0.3452 |  |
| Education: high school or below (vs college) | +774.2962 | 888.0061 | ±1776.0122 | +0.872 | 0.3832 |  |
| Site: UCSD (vs UAB) | +98.7765 | 553.2119 | ±1106.4239 | +0.179 | 0.8583 |  |
| Site: UW (vs UAB) | -70.5186 | 458.6291 | ±917.2581 | -0.154 | 0.8778 |  |
| **Age (years)** | **-131.7474** | 17.8337 | ±35.6674 | **-7.388** | **1.50e-13** | *** |
| BMI (kg/m2) | -55.3091 | 33.8482 | ±67.6965 | -1.634 | 0.1023 |  |
| Hypertension | -410.0276 | 477.8079 | ±955.6158 | -0.858 | 0.3908 |  |
| High cholesterol | -170.8773 | 411.4541 | ±822.9081 | -0.415 | 0.6779 |  |
| Kidney disease | -171.8398 | 1219.4312 | ±2438.8624 | -0.141 | 0.8879 |  |
| Circulatory disease | +70.7310 | 601.4238 | ±1202.8476 | +0.118 | 0.9064 |  |
| Avg. daily time 54-69 (%) | -22.6141 | 106.5692 | ±213.1385 | -0.212 | 0.8319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **374**, R² = **0.1425**, Adj R² = **0.1165**, F-statistic = **5.47** (p = **4.38e-08**), Residual SE = **3799.189** on **362** df, AIC = **7238.6**, BIC = **7285.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19749.3255** | 1624.1069 | ±3248.2138 | **+12.160** | **5.07e-34** | *** |
| Education: graduate level (vs college) | -446.5629 | 469.9838 | ±939.9677 | -0.950 | 0.3420 |  |
| Education: high school or below (vs college) | +767.1528 | 889.8358 | ±1779.6715 | +0.862 | 0.3886 |  |
| Site: UCSD (vs UAB) | +76.8574 | 555.2665 | ±1110.5330 | +0.138 | 0.8899 |  |
| Site: UW (vs UAB) | -89.2119 | 456.5234 | ±913.0468 | -0.195 | 0.8451 |  |
| **Age (years)** | **-131.8096** | 17.8328 | ±35.6655 | **-7.391** | **1.45e-13** | *** |
| BMI (kg/m2) | -55.4580 | 33.9570 | ±67.9140 | -1.633 | 0.1024 |  |
| Hypertension | -420.1187 | 477.8679 | ±955.7358 | -0.879 | 0.3793 |  |
| High cholesterol | -183.0529 | 412.8122 | ±825.6244 | -0.443 | 0.6575 |  |
| Kidney disease | -163.5293 | 1217.9218 | ±2435.8437 | -0.134 | 0.8932 |  |
| Circulatory disease | +62.0776 | 600.3899 | ±1200.7797 | +0.103 | 0.9176 |  |
| Time < 70 (%) | -35.9519 | 78.0267 | ±156.0534 | -0.461 | 0.6450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1161**, F-statistic = **5.45** (p = **4.71e-08**), Residual SE = **3800.086** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19682.5512** | 1609.4063 | ±3218.8125 | **+12.230** | **2.16e-34** | *** |
| Education: graduate level (vs college) | -445.0551 | 470.8730 | ±941.7460 | -0.945 | 0.3446 |  |
| Education: high school or below (vs college) | +773.6951 | 888.6497 | ±1777.2994 | +0.871 | 0.3840 |  |
| Site: UCSD (vs UAB) | +94.6237 | 554.1117 | ±1108.2233 | +0.171 | 0.8644 |  |
| Site: UW (vs UAB) | -74.6009 | 458.9655 | ±917.9310 | -0.163 | 0.8709 |  |
| **Age (years)** | **-131.6671** | 17.8275 | ±35.6550 | **-7.386** | **1.52e-13** | *** |
| BMI (kg/m2) | -55.3914 | 33.8923 | ±67.7846 | -1.634 | 0.1022 |  |
| Hypertension | -411.9527 | 477.9145 | ±955.8289 | -0.862 | 0.3887 |  |
| High cholesterol | -173.2482 | 411.8383 | ±823.6765 | -0.421 | 0.6740 |  |
| Kidney disease | -169.5877 | 1218.9799 | ±2437.9598 | -0.139 | 0.8894 |  |
| Circulatory disease | +69.1788 | 600.8016 | ±1201.6032 | +0.115 | 0.9083 |  |
| Avg. daily time < 70 (%) | -20.2471 | 84.6717 | ±169.3434 | -0.239 | 0.8110 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **374**, R² = **0.1431**, Adj R² = **0.1170**, F-statistic = **5.49** (p = **3.99e-08**), Residual SE = **3798.055** on **362** df, AIC = **7238.4**, BIC = **7285.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +8484.7506 | 11737.6305 | ±23475.2610 | +0.723 | 0.4698 |  |
| Education: graduate level (vs college) | -446.5495 | 469.8646 | ±939.7292 | -0.950 | 0.3419 |  |
| Education: high school or below (vs college) | +775.7385 | 889.6124 | ±1779.2248 | +0.872 | 0.3832 |  |
| Site: UCSD (vs UAB) | +61.4256 | 569.8854 | ±1139.7708 | +0.108 | 0.9142 |  |
| Site: UW (vs UAB) | -97.3839 | 462.7202 | ±925.4405 | -0.210 | 0.8333 |  |
| **Age (years)** | **-131.1322** | 17.8135 | ±35.6270 | **-7.361** | **1.82e-13** | *** |
| BMI (kg/m2) | -56.5276 | 33.7878 | ±67.5757 | -1.673 | 0.0943 | . |
| Hypertension | -415.6860 | 477.2218 | ±954.4435 | -0.871 | 0.3837 |  |
| High cholesterol | -189.6045 | 410.8350 | ±821.6700 | -0.462 | 0.6444 |  |
| Kidney disease | -87.2042 | 1227.0216 | ±2454.0432 | -0.071 | 0.9433 |  |
| Circulatory disease | +55.3773 | 602.5462 | ±1205.0924 | +0.092 | 0.9268 |  |
| Time 54-250, pooled (%) | +112.5757 | 119.6286 | ±239.2573 | +0.941 | 0.3467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **374**, R² = **0.1423**, Adj R² = **0.1162**, F-statistic = **5.46** (p = **4.62e-08**), Residual SE = **3799.834** on **362** df, AIC = **7238.7**, BIC = **7285.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +13035.5924 | 14449.4021 | ±28898.8043 | +0.902 | 0.3670 |  |
| Education: graduate level (vs college) | -445.4713 | 470.7673 | ±941.5347 | -0.946 | 0.3440 |  |
| Education: high school or below (vs college) | +780.2912 | 888.6960 | ±1777.3919 | +0.878 | 0.3799 |  |
| Site: UCSD (vs UAB) | +87.5026 | 568.3702 | ±1136.7403 | +0.154 | 0.8776 |  |
| Site: UW (vs UAB) | -77.4017 | 463.5306 | ±927.0612 | -0.167 | 0.8674 |  |
| **Age (years)** | **-131.1931** | 17.7840 | ±35.5680 | **-7.377** | **1.62e-13** | *** |
| BMI (kg/m2) | -55.8348 | 33.8417 | ±67.6835 | -1.650 | 0.0990 | . |
| Hypertension | -409.7777 | 477.1586 | ±954.3173 | -0.859 | 0.3905 |  |
| High cholesterol | -174.0556 | 409.4399 | ±818.8798 | -0.425 | 0.6708 |  |
| Kidney disease | -122.5999 | 1240.4056 | ±2480.8112 | -0.099 | 0.9213 |  |
| Circulatory disease | +64.1524 | 602.3372 | ±1204.6743 | +0.107 | 0.9152 |  |
| Avg. daily time 54-250 (%) | +66.2768 | 146.3602 | ±292.7204 | +0.453 | 0.6507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **374**, R² = **0.1430**, Adj R² = **0.1169**, F-statistic = **5.49** (p = **4.06e-08**), Residual SE = **3798.268** on **362** df, AIC = **7238.4**, BIC = **7285.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19632.7332** | 1577.8499 | ±3155.6998 | **+12.443** | **1.53e-35** | *** |
| Education: graduate level (vs college) | -435.8425 | 470.4897 | ±940.9794 | -0.926 | 0.3543 |  |
| Education: high school or below (vs college) | +803.5450 | 885.9861 | ±1771.9722 | +0.907 | 0.3644 |  |
| Site: UCSD (vs UAB) | +119.9472 | 553.3390 | ±1106.6779 | +0.217 | 0.8284 |  |
| Site: UW (vs UAB) | -43.8351 | 462.4233 | ±924.8466 | -0.095 | 0.9245 |  |
| **Age (years)** | **-130.9942** | 17.8487 | ±35.6975 | **-7.339** | **2.15e-13** | *** |
| BMI (kg/m2) | -55.4714 | 33.6977 | ±67.3954 | -1.646 | 0.0997 | . |
| Hypertension | -380.5375 | 477.5656 | ±955.1312 | -0.797 | 0.4256 |  |
| High cholesterol | -150.8647 | 411.3313 | ±822.6626 | -0.367 | 0.7138 |  |
| Kidney disease | -80.7911 | 1232.4047 | ±2464.8093 | -0.066 | 0.9477 |  |
| Circulatory disease | +59.9995 | 605.1490 | ±1210.2980 | +0.099 | 0.9210 |  |
| Time 181-250, pooled (%) | -30.6802 | 33.0272 | ±66.0544 | -0.929 | 0.3529 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **374**, R² = **0.1431**, Adj R² = **0.1170**, F-statistic = **5.49** (p = **3.98e-08**), Residual SE = **3798.002** on **362** df, AIC = **7238.4**, BIC = **7285.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19624.2206** | 1579.1718 | ±3158.3436 | **+12.427** | **1.87e-35** | *** |
| Education: graduate level (vs college) | -434.9307 | 470.6095 | ±941.2189 | -0.924 | 0.3554 |  |
| Education: high school or below (vs college) | +802.6148 | 886.4190 | ±1772.8380 | +0.905 | 0.3652 |  |
| Site: UCSD (vs UAB) | +118.9393 | 553.5645 | ±1107.1290 | +0.215 | 0.8299 |  |
| Site: UW (vs UAB) | -43.2088 | 462.3021 | ±924.6043 | -0.093 | 0.9255 |  |
| **Age (years)** | **-130.9659** | 17.8496 | ±35.6992 | **-7.337** | **2.18e-13** | *** |
| BMI (kg/m2) | -55.2800 | 33.7282 | ±67.4564 | -1.639 | 0.1012 |  |
| Hypertension | -378.3224 | 477.7790 | ±955.5580 | -0.792 | 0.4285 |  |
| High cholesterol | -149.4617 | 411.5926 | ±823.1853 | -0.363 | 0.7165 |  |
| Kidney disease | -78.5146 | 1232.8956 | ±2465.7913 | -0.064 | 0.9492 |  |
| Circulatory disease | +58.3570 | 604.8786 | ±1209.7572 | +0.096 | 0.9231 |  |
| Avg. daily time 181-250 (%) | -31.0526 | 32.2155 | ±64.4311 | -0.964 | 0.3351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **374**, R² = **0.1429**, Adj R² = **0.1168**, F-statistic = **5.49** (p = **4.11e-08**), Residual SE = **3798.408** on **362** df, AIC = **7238.4**, BIC = **7285.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19633.6809** | 1577.3890 | ±3154.7781 | **+12.447** | **1.45e-35** | *** |
| Education: graduate level (vs college) | -436.7006 | 470.4104 | ±940.8207 | -0.928 | 0.3532 |  |
| Education: high school or below (vs college) | +801.4156 | 886.2867 | ±1772.5733 | +0.904 | 0.3659 |  |
| Site: UCSD (vs UAB) | +117.4291 | 553.5562 | ±1107.1124 | +0.212 | 0.8320 |  |
| Site: UW (vs UAB) | -47.1417 | 462.4795 | ±924.9589 | -0.102 | 0.9188 |  |
| **Age (years)** | **-130.9904** | 17.8355 | ±35.6710 | **-7.344** | **2.07e-13** | *** |
| BMI (kg/m2) | -55.5591 | 33.6787 | ±67.3574 | -1.650 | 0.0990 | . |
| Hypertension | -382.9911 | 477.3276 | ±954.6551 | -0.802 | 0.4223 |  |
| High cholesterol | -153.5096 | 411.0832 | ±822.1664 | -0.373 | 0.7088 |  |
| Kidney disease | -78.0306 | 1234.8878 | ±2469.7755 | -0.063 | 0.9496 |  |
| Circulatory disease | +60.3872 | 605.0034 | ±1210.0069 | +0.100 | 0.9205 |  |
| Time > 180 (%) | -26.3395 | 29.3131 | ±58.6261 | -0.899 | 0.3689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **374**, R² = **0.1430**, Adj R² = **0.1169**, F-statistic = **5.49** (p = **4.07e-08**), Residual SE = **3798.282** on **362** df, AIC = **7238.4**, BIC = **7285.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19625.0378** | 1578.4909 | ±3156.9818 | **+12.433** | **1.73e-35** | *** |
| Education: graduate level (vs college) | -436.2416 | 470.4796 | ±940.9593 | -0.927 | 0.3538 |  |
| Education: high school or below (vs college) | +799.8621 | 886.7365 | ±1773.4730 | +0.902 | 0.3670 |  |
| Site: UCSD (vs UAB) | +115.6350 | 554.0497 | ±1108.0994 | +0.209 | 0.8347 |  |
| Site: UW (vs UAB) | -46.6442 | 462.3976 | ±924.7951 | -0.101 | 0.9196 |  |
| **Age (years)** | **-130.9780** | 17.8357 | ±35.6713 | **-7.344** | **2.08e-13** | *** |
| BMI (kg/m2) | -55.3711 | 33.7098 | ±67.4195 | -1.643 | 0.1005 |  |
| Hypertension | -381.9398 | 477.4819 | ±954.9639 | -0.800 | 0.4238 |  |
| High cholesterol | -151.9971 | 411.3567 | ±822.7134 | -0.370 | 0.7118 |  |
| Kidney disease | -77.7937 | 1235.8498 | ±2471.6995 | -0.063 | 0.9498 |  |
| Circulatory disease | +59.3130 | 604.7095 | ±1209.4191 | +0.098 | 0.9219 |  |
| Avg. daily time > 180 (%) | -25.8423 | 28.3566 | ±56.7133 | -0.911 | 0.3621 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **374**, R² = **0.1431**, Adj R² = **0.1171**, F-statistic = **5.50** (p = **3.94e-08**), Residual SE = **3797.883** on **362** df, AIC = **7238.3**, BIC = **7285.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19603.0416** | 1581.1195 | ±3162.2390 | **+12.398** | **2.67e-35** | *** |
| Education: graduate level (vs college) | -452.7614 | 469.1112 | ±938.2223 | -0.965 | 0.3345 |  |
| Education: high school or below (vs college) | +806.0593 | 888.9124 | ±1777.8247 | +0.907 | 0.3645 |  |
| Site: UCSD (vs UAB) | +98.9177 | 557.4994 | ±1114.9989 | +0.177 | 0.8592 |  |
| Site: UW (vs UAB) | -52.0839 | 462.5803 | ±925.1607 | -0.113 | 0.9104 |  |
| **Age (years)** | **-131.1124** | 17.8631 | ±35.7262 | **-7.340** | **2.14e-13** | *** |
| BMI (kg/m2) | -54.4113 | 33.8583 | ±67.7166 | -1.607 | 0.1080 |  |
| Hypertension | -378.4501 | 480.2470 | ±960.4941 | -0.788 | 0.4307 |  |
| High cholesterol | -160.5341 | 410.1012 | ±820.2024 | -0.391 | 0.6955 |  |
| Kidney disease | -163.7646 | 1217.8570 | ±2435.7139 | -0.134 | 0.8930 |  |
| Circulatory disease | +41.9080 | 605.5439 | ±1211.0877 | +0.069 | 0.9448 |  |
| Nocturnal time > 180 (%) | -30.1699 | 30.3553 | ±60.7106 | -0.994 | 0.3203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **374**, R² = **0.1420**, Adj R² = **0.1159**, F-statistic = **5.45** (p = **4.82e-08**), Residual SE = **3800.360** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19644.4942** | 1580.8523 | ±3161.7046 | **+12.427** | **1.88e-35** | *** |
| Education: graduate level (vs college) | -441.7057 | 470.2366 | ±940.4733 | -0.939 | 0.3476 |  |
| Education: high school or below (vs college) | +787.3521 | 887.9390 | ±1775.8781 | +0.887 | 0.3752 |  |
| Site: UCSD (vs UAB) | +114.0025 | 550.7385 | ±1101.4769 | +0.207 | 0.8360 |  |
| Site: UW (vs UAB) | -55.4452 | 462.8628 | ±925.7256 | -0.120 | 0.9047 |  |
| **Age (years)** | **-131.6209** | 17.7211 | ±35.4423 | **-7.427** | **1.11e-13** | *** |
| BMI (kg/m2) | -55.6692 | 33.6924 | ±67.3848 | -1.652 | 0.0985 | . |
| Hypertension | -397.2940 | 478.1653 | ±956.3305 | -0.831 | 0.4060 |  |
| High cholesterol | -161.6249 | 410.7078 | ±821.4155 | -0.394 | 0.6939 |  |
| Kidney disease | -162.8203 | 1229.0146 | ±2458.0292 | -0.132 | 0.8946 |  |
| Circulatory disease | +73.4936 | 603.0713 | ±1206.1426 | +0.122 | 0.9030 |  |
| Any reading > 250 during wear (0/1) | -82.1227 | 513.4018 | ±1026.8035 | -0.160 | 0.8729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **374**, R² = **0.1423**, Adj R² = **0.1162**, F-statistic = **5.46** (p = **4.59e-08**), Residual SE = **3799.763** on **362** df, AIC = **7238.7**, BIC = **7285.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19638.7236** | 1575.4270 | ±3150.8540 | **+12.466** | **1.15e-35** | *** |
| Education: graduate level (vs college) | -440.9437 | 470.4832 | ±940.9663 | -0.937 | 0.3486 |  |
| Education: high school or below (vs college) | +787.7911 | 887.3382 | ±1774.6764 | +0.888 | 0.3746 |  |
| Site: UCSD (vs UAB) | +104.6027 | 559.8916 | ±1119.7833 | +0.187 | 0.8518 |  |
| Site: UW (vs UAB) | -62.1488 | 463.5017 | ±927.0035 | -0.134 | 0.8933 |  |
| **Age (years)** | **-131.3139** | 17.7621 | ±35.5243 | **-7.393** | **1.44e-13** | *** |
| BMI (kg/m2) | -55.8322 | 33.6531 | ±67.3061 | -1.659 | 0.0971 | . |
| Hypertension | -398.9193 | 476.8750 | ±953.7499 | -0.837 | 0.4029 |  |
| High cholesterol | -166.7094 | 409.7381 | ±819.4762 | -0.407 | 0.6841 |  |
| Kidney disease | -107.0940 | 1257.1532 | ±2514.3065 | -0.085 | 0.9321 |  |
| Circulatory disease | +68.5288 | 605.5274 | ±1211.0548 | +0.113 | 0.9099 |  |
| Time > 250 (%) | -109.4537 | 246.4580 | ±492.9161 | -0.444 | 0.6570 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 374)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **374**, R² = **0.1421**, Adj R² = **0.1161**, F-statistic = **5.45** (p = **4.72e-08**), Residual SE = **3800.090** on **362** df, AIC = **7238.8**, BIC = **7285.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19633.5318** | 1574.4060 | ±3148.8119 | **+12.470** | **1.08e-35** | *** |
| Education: graduate level (vs college) | -441.1081 | 470.2947 | ±940.5895 | -0.938 | 0.3483 |  |
| Education: high school or below (vs college) | +786.5071 | 887.3166 | ±1774.6332 | +0.886 | 0.3754 |  |
| Site: UCSD (vs UAB) | +103.8084 | 560.4434 | ±1120.8869 | +0.185 | 0.8531 |  |
| Site: UW (vs UAB) | -59.1764 | 462.9975 | ±925.9950 | -0.128 | 0.8983 |  |
| **Age (years)** | **-131.4344** | 17.7581 | ±35.5163 | **-7.401** | **1.35e-13** | *** |
| BMI (kg/m2) | -55.6376 | 33.6690 | ±67.3380 | -1.652 | 0.0984 | . |
| Hypertension | -400.1498 | 476.8090 | ±953.6181 | -0.839 | 0.4013 |  |
| High cholesterol | -163.5792 | 410.0165 | ±820.0330 | -0.399 | 0.6899 |  |
| Kidney disease | -124.8183 | 1259.4552 | ±2518.9104 | -0.099 | 0.9211 |  |
| Circulatory disease | +70.6133 | 604.6856 | ±1209.3712 | +0.117 | 0.9070 |  |
| Avg. daily time > 250 (%) | -74.6889 | 200.0858 | ±400.1715 | -0.373 | 0.7089 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 374; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1375**, F-statistic = **6.95** (p = **5.65e-10**), Residual SE = **12.102** on **363** df, AIC = **2937.2**, BIC = **2980.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0164** | 5.0643 | ±10.1287 | **+10.863** | **1.72e-27** | *** |
| Education: graduate level (vs college) | -1.4780 | 1.5008 | ±3.0015 | -0.985 | 0.3247 |  |
| Education: high school or below (vs college) | +1.3566 | 2.7547 | ±5.5093 | +0.492 | 0.6224 |  |
| Site: UCSD (vs UAB) | +0.2374 | 1.8345 | ±3.6689 | +0.129 | 0.8970 |  |
| Site: UW (vs UAB) | +0.0045 | 1.4813 | ±2.9626 | +0.003 | 0.9976 |  |
| **Age (years)** | **-0.4613** | 0.0597 | ±0.1193 | **-7.731** | **1.07e-14** | *** |
| BMI (kg/m2) | -0.0735 | 0.1049 | ±0.2098 | -0.701 | 0.4834 |  |
| Hypertension | -0.9923 | 1.4722 | ±2.9444 | -0.674 | 0.5003 |  |
| High cholesterol | -0.5241 | 1.3182 | ±2.6365 | -0.398 | 0.6910 |  |
| Kidney disease | -1.1120 | 3.4241 | ±6.8482 | -0.325 | 0.7454 |  |
| Circulatory disease | +0.0466 | 1.8563 | ±3.7127 | +0.025 | 0.9800 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **374**, R² = **0.1633**, Adj R² = **0.1379**, F-statistic = **6.42** (p = **9.27e-10**), Residual SE = **12.099** on **362** df, AIC = **2938.0**, BIC = **2985.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.8930** | 9.0316 | ±18.0632 | **+5.192** | **2.08e-07** | *** |
| Education: graduate level (vs college) | -1.3884 | 1.4951 | ±2.9902 | -0.929 | 0.3531 |  |
| Education: high school or below (vs college) | +1.1811 | 2.7797 | ±5.5595 | +0.425 | 0.6709 |  |
| Site: UCSD (vs UAB) | -0.0543 | 1.8083 | ±3.6166 | -0.030 | 0.9761 |  |
| Site: UW (vs UAB) | -0.0508 | 1.4733 | ±2.9467 | -0.034 | 0.9725 |  |
| **Age (years)** | **-0.4721** | 0.0593 | ±0.1185 | **-7.968** | **1.62e-15** | *** |
| BMI (kg/m2) | -0.0864 | 0.1066 | ±0.2133 | -0.810 | 0.4177 |  |
| Hypertension | -0.9632 | 1.4773 | ±2.9547 | -0.652 | 0.5144 |  |
| High cholesterol | -0.7673 | 1.3489 | ±2.6978 | -0.569 | 0.5695 |  |
| Kidney disease | -1.2109 | 3.4088 | ±6.8177 | -0.355 | 0.7224 |  |
| Circulatory disease | +0.1564 | 1.8697 | ±3.7393 | +0.084 | 0.9333 |  |
| HbA1c (%) | +1.6480 | 1.3932 | ±2.7863 | +1.183 | 0.2368 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1351**, F-statistic = **6.30** (p = **1.55e-09**), Residual SE = **12.119** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1775** | 6.3846 | ±12.7692 | **+8.642** | **5.51e-18** | *** |
| Education: graduate level (vs college) | -1.4755 | 1.5134 | ±3.0268 | -0.975 | 0.3296 |  |
| Education: high school or below (vs college) | +1.3614 | 2.7685 | ±5.5370 | +0.492 | 0.6229 |  |
| Site: UCSD (vs UAB) | +0.2404 | 1.8272 | ±3.6543 | +0.132 | 0.8953 |  |
| Site: UW (vs UAB) | +0.0102 | 1.4806 | ±2.9612 | +0.007 | 0.9945 |  |
| **Age (years)** | **-0.4612** | 0.0599 | ±0.1199 | **-7.694** | **1.42e-14** | *** |
| BMI (kg/m2) | -0.0734 | 0.1059 | ±0.2117 | -0.693 | 0.4884 |  |
| Hypertension | -0.9879 | 1.4852 | ±2.9704 | -0.665 | 0.5059 |  |
| High cholesterol | -0.5188 | 1.3329 | ±2.6658 | -0.389 | 0.6971 |  |
| Kidney disease | -1.1011 | 3.4431 | ±6.8861 | -0.320 | 0.7491 |  |
| Circulatory disease | +0.0462 | 1.8612 | ±3.7224 | +0.025 | 0.9802 |  |
| Mean glucose (mg/dL) | -0.0016 | 0.0429 | ±0.0857 | -0.037 | 0.9705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1351**, F-statistic = **6.30** (p = **1.55e-09**), Residual SE = **12.119** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.3966** | 11.0531 | ±22.1061 | **+5.012** | **5.39e-07** | *** |
| Education: graduate level (vs college) | -1.4755 | 1.5134 | ±3.0268 | -0.975 | 0.3296 |  |
| Education: high school or below (vs college) | +1.3614 | 2.7685 | ±5.5370 | +0.492 | 0.6229 |  |
| Site: UCSD (vs UAB) | +0.2404 | 1.8272 | ±3.6543 | +0.132 | 0.8953 |  |
| Site: UW (vs UAB) | +0.0102 | 1.4806 | ±2.9612 | +0.007 | 0.9945 |  |
| **Age (years)** | **-0.4612** | 0.0599 | ±0.1199 | **-7.694** | **1.42e-14** | *** |
| BMI (kg/m2) | -0.0734 | 0.1059 | ±0.2117 | -0.693 | 0.4884 |  |
| Hypertension | -0.9879 | 1.4852 | ±2.9704 | -0.665 | 0.5059 |  |
| High cholesterol | -0.5188 | 1.3329 | ±2.6658 | -0.389 | 0.6971 |  |
| Kidney disease | -1.1011 | 3.4431 | ±6.8861 | -0.320 | 0.7491 |  |
| Circulatory disease | +0.0462 | 1.8612 | ±3.7224 | +0.025 | 0.9802 |  |
| GMI (%) | -0.0662 | 1.7918 | ±3.5836 | -0.037 | 0.9705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **374**, R² = **0.1612**, Adj R² = **0.1357**, F-statistic = **6.32** (p = **1.40e-09**), Residual SE = **12.115** on **362** df, AIC = **2939.0**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.9403** | 6.4960 | ±12.9919 | **+8.150** | **3.65e-16** | *** |
| Education: graduate level (vs college) | -1.4906 | 1.5046 | ±3.0092 | -0.991 | 0.3218 |  |
| Education: high school or below (vs college) | +1.2810 | 2.7921 | ±5.5843 | +0.459 | 0.6464 |  |
| Site: UCSD (vs UAB) | +0.1880 | 1.8270 | ±3.6540 | +0.103 | 0.9180 |  |
| Site: UW (vs UAB) | -0.0597 | 1.4726 | ±2.9452 | -0.041 | 0.9676 |  |
| **Age (years)** | **-0.4606** | 0.0599 | ±0.1198 | **-7.686** | **1.52e-14** | *** |
| BMI (kg/m2) | -0.0797 | 0.1069 | ±0.2137 | -0.746 | 0.4555 |  |
| Hypertension | -1.0523 | 1.4881 | ±2.9763 | -0.707 | 0.4795 |  |
| High cholesterol | -0.6133 | 1.3290 | ±2.6581 | -0.461 | 0.6445 |  |
| Kidney disease | -1.1546 | 3.4253 | ±6.8505 | -0.337 | 0.7361 |  |
| Circulatory disease | +0.0807 | 1.8676 | ±3.7352 | +0.043 | 0.9656 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0205 | 0.0419 | ±0.0837 | +0.489 | 0.6246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1613**, Adj R² = **0.1358**, F-statistic = **6.33** (p = **1.36e-09**), Residual SE = **12.114** on **362** df, AIC = **2938.9**, BIC = **2986.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.9732** | 5.4652 | ±10.9304 | **+10.242** | **1.29e-24** | *** |
| Education: graduate level (vs college) | -1.4482 | 1.5138 | ±3.0277 | -0.957 | 0.3388 |  |
| Education: high school or below (vs college) | +1.3792 | 2.7569 | ±5.5139 | +0.500 | 0.6169 |  |
| Site: UCSD (vs UAB) | +0.2855 | 1.8192 | ±3.6383 | +0.157 | 0.8753 |  |
| Site: UW (vs UAB) | +0.0198 | 1.4795 | ±2.9589 | +0.013 | 0.9893 |  |
| **Age (years)** | **-0.4573** | 0.0596 | ±0.1191 | **-7.679** | **1.60e-14** | *** |
| BMI (kg/m2) | -0.0743 | 0.1049 | ±0.2099 | -0.708 | 0.4787 |  |
| Hypertension | -0.9544 | 1.4790 | ±2.9580 | -0.645 | 0.5187 |  |
| High cholesterol | -0.5319 | 1.3199 | ±2.6398 | -0.403 | 0.6869 |  |
| Kidney disease | -0.8529 | 3.4866 | ±6.9732 | -0.245 | 0.8067 |  |
| Circulatory disease | +0.0313 | 1.8638 | ±3.7276 | +0.017 | 0.9866 |  |
| Glucose SD, pooled (mg/dL) | -0.0560 | 0.1074 | ±0.2147 | -0.521 | 0.6022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1614**, Adj R² = **0.1359**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **12.113** on **362** df, AIC = **2938.9**, BIC = **2986.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8945** | 5.4041 | ±10.8083 | **+10.343** | **4.51e-25** | *** |
| Education: graduate level (vs college) | -1.4580 | 1.5112 | ±3.0224 | -0.965 | 0.3346 |  |
| Education: high school or below (vs college) | +1.3988 | 2.7603 | ±5.5206 | +0.507 | 0.6123 |  |
| Site: UCSD (vs UAB) | +0.3142 | 1.8071 | ±3.6142 | +0.174 | 0.8620 |  |
| Site: UW (vs UAB) | +0.0329 | 1.4791 | ±2.9581 | +0.022 | 0.9823 |  |
| **Age (years)** | **-0.4561** | 0.0596 | ±0.1191 | **-7.657** | **1.90e-14** | *** |
| BMI (kg/m2) | -0.0734 | 0.1052 | ±0.2104 | -0.698 | 0.4852 |  |
| Hypertension | -0.9535 | 1.4787 | ±2.9573 | -0.645 | 0.5190 |  |
| High cholesterol | -0.5286 | 1.3210 | ±2.6420 | -0.400 | 0.6890 |  |
| Kidney disease | -0.8369 | 3.4896 | ±6.9792 | -0.240 | 0.8105 |  |
| Circulatory disease | +0.0218 | 1.8604 | ±3.7207 | +0.012 | 0.9907 |  |
| Avg. daily SD (mg/dL) | -0.0638 | 0.1213 | ±0.2426 | -0.526 | 0.5990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **374**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.35** (p = **1.25e-09**), Residual SE = **12.110** on **362** df, AIC = **2938.7**, BIC = **2985.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7272** | 5.8733 | ±11.7466 | **+9.659** | **4.52e-22** | *** |
| Education: graduate level (vs college) | -1.4606 | 1.5054 | ±3.0107 | -0.970 | 0.3319 |  |
| Education: high school or below (vs college) | +1.3391 | 2.7579 | ±5.5158 | +0.486 | 0.6273 |  |
| Site: UCSD (vs UAB) | +0.2814 | 1.8314 | ±3.6628 | +0.154 | 0.8779 |  |
| Site: UW (vs UAB) | -0.0385 | 1.4880 | ±2.9760 | -0.026 | 0.9794 |  |
| **Age (years)** | **-0.4563** | 0.0595 | ±0.1189 | **-7.673** | **1.68e-14** | *** |
| BMI (kg/m2) | -0.0763 | 0.1051 | ±0.2102 | -0.726 | 0.4678 |  |
| Hypertension | -0.9807 | 1.4723 | ±2.9446 | -0.666 | 0.5054 |  |
| High cholesterol | -0.5944 | 1.3141 | ±2.6283 | -0.452 | 0.6510 |  |
| Kidney disease | -0.8420 | 3.4550 | ±6.9100 | -0.244 | 0.8075 |  |
| Circulatory disease | +0.0241 | 1.8632 | ±3.7264 | +0.013 | 0.9897 |  |
| CV (%) | -0.1002 | 0.1485 | ±0.2970 | -0.675 | 0.4998 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1351**, F-statistic = **6.30** (p = **1.55e-09**), Residual SE = **12.119** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2761** | 6.1549 | ±12.3098 | **+8.981** | **2.69e-19** | *** |
| Education: graduate level (vs college) | -1.4837 | 1.5205 | ±3.0410 | -0.976 | 0.3292 |  |
| Education: high school or below (vs college) | +1.3542 | 2.7630 | ±5.5261 | +0.490 | 0.6241 |  |
| Site: UCSD (vs UAB) | +0.2328 | 1.8271 | ±3.6541 | +0.127 | 0.8986 |  |
| Site: UW (vs UAB) | +0.0050 | 1.4859 | ±2.9719 | +0.003 | 0.9973 |  |
| **Age (years)** | **-0.4619** | 0.0589 | ±0.1179 | **-7.836** | **4.65e-15** | *** |
| BMI (kg/m2) | -0.0735 | 0.1051 | ±0.2102 | -0.699 | 0.4846 |  |
| Hypertension | -0.9939 | 1.4788 | ±2.9577 | -0.672 | 0.5015 |  |
| High cholesterol | -0.5198 | 1.3144 | ±2.6288 | -0.395 | 0.6925 |  |
| Kidney disease | -1.1348 | 3.4687 | ±6.9374 | -0.327 | 0.7436 |  |
| Circulatory disease | +0.0486 | 1.8595 | ±3.7190 | +0.026 | 0.9792 |  |
| Mean / SD ratio | -0.0410 | 0.6016 | ±1.2032 | -0.068 | 0.9457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1611**, Adj R² = **0.1357**, F-statistic = **6.32** (p = **1.41e-09**), Residual SE = **12.115** on **362** df, AIC = **2939.0**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7397** | 6.1226 | ±12.2453 | **+9.267** | **1.91e-20** | *** |
| Education: graduate level (vs college) | -1.5151 | 1.5187 | ±3.0375 | -0.998 | 0.3185 |  |
| Education: high school or below (vs college) | +1.3047 | 2.7689 | ±5.5378 | +0.471 | 0.6375 |  |
| Site: UCSD (vs UAB) | +0.1751 | 1.8162 | ±3.6325 | +0.096 | 0.9232 |  |
| Site: UW (vs UAB) | -0.0032 | 1.4842 | ±2.9683 | -0.002 | 0.9983 |  |
| **Age (years)** | **-0.4659** | 0.0585 | ±0.1171 | **-7.959** | **1.73e-15** | *** |
| BMI (kg/m2) | -0.0743 | 0.1050 | ±0.2100 | -0.708 | 0.4791 |  |
| Hypertension | -0.9945 | 1.4787 | ±2.9575 | -0.673 | 0.5012 |  |
| High cholesterol | -0.5035 | 1.3153 | ±2.6306 | -0.383 | 0.7019 |  |
| Kidney disease | -1.2862 | 3.4933 | ±6.9866 | -0.368 | 0.7127 |  |
| Circulatory disease | +0.0690 | 1.8548 | ±3.7096 | +0.037 | 0.9703 |  |
| Avg. daily mean/SD | -0.2178 | 0.4775 | ±0.9550 | -0.456 | 0.6483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **374**, R² = **0.1630**, Adj R² = **0.1376**, F-statistic = **6.41** (p = **9.89e-10**), Residual SE = **12.101** on **362** df, AIC = **2938.2**, BIC = **2985.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4003** | 6.1618 | ±12.3237 | **+8.342** | **7.32e-17** | *** |
| Education: graduate level (vs college) | -1.4747 | 1.5036 | ±3.0072 | -0.981 | 0.3267 |  |
| Education: high school or below (vs college) | +1.4562 | 2.7383 | ±5.4766 | +0.532 | 0.5949 |  |
| Site: UCSD (vs UAB) | +0.1435 | 1.8153 | ±3.6307 | +0.079 | 0.9370 |  |
| Site: UW (vs UAB) | +0.1538 | 1.5048 | ±3.0096 | +0.102 | 0.9186 |  |
| **Age (years)** | **-0.4581** | 0.0597 | ±0.1194 | **-7.674** | **1.66e-14** | *** |
| BMI (kg/m2) | -0.0696 | 0.1043 | ±0.2085 | -0.668 | 0.5041 |  |
| Hypertension | -1.0666 | 1.4772 | ±2.9544 | -0.722 | 0.4703 |  |
| High cholesterol | -0.3898 | 1.2977 | ±2.5955 | -0.300 | 0.7639 |  |
| Kidney disease | -1.1585 | 3.4552 | ±6.9103 | -0.335 | 0.7374 |  |
| Circulatory disease | +0.0631 | 1.8518 | ±3.7035 | +0.034 | 0.9728 |  |
| MAG (mg/dL/h) | +0.0815 | 0.0816 | ±0.1632 | +0.998 | 0.3181 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **374**, R² = **0.1612**, Adj R² = **0.1357**, F-statistic = **6.32** (p = **1.40e-09**), Residual SE = **12.115** on **362** df, AIC = **2939.0**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0776** | 5.6548 | ±11.3096 | **+9.917** | **3.52e-23** | *** |
| Education: graduate level (vs college) | -1.4755 | 1.5059 | ±3.0119 | -0.980 | 0.3272 |  |
| Education: high school or below (vs college) | +1.3833 | 2.7655 | ±5.5311 | +0.500 | 0.6170 |  |
| Site: UCSD (vs UAB) | +0.2966 | 1.8134 | ±3.6269 | +0.164 | 0.8701 |  |
| Site: UW (vs UAB) | +0.0106 | 1.4812 | ±2.9624 | +0.007 | 0.9943 |  |
| **Age (years)** | **-0.4576** | 0.0599 | ±0.1197 | **-7.646** | **2.08e-14** | *** |
| BMI (kg/m2) | -0.0773 | 0.1051 | ±0.2103 | -0.736 | 0.4620 |  |
| Hypertension | -0.9660 | 1.4757 | ±2.9515 | -0.655 | 0.5127 |  |
| High cholesterol | -0.5485 | 1.3148 | ±2.6296 | -0.417 | 0.6766 |  |
| Kidney disease | -0.9468 | 3.4494 | ±6.8988 | -0.274 | 0.7837 |  |
| Circulatory disease | +0.0310 | 1.8619 | ±3.7238 | +0.017 | 0.9867 |  |
| Avg. daily range (mg/dL) | -0.0119 | 0.0266 | ±0.0531 | -0.448 | 0.6543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1351**, F-statistic = **6.30** (p = **1.54e-09**), Residual SE = **12.119** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8857** | 5.2843 | ±10.5686 | **+10.387** | **2.85e-25** | *** |
| Education: graduate level (vs college) | -1.4885 | 1.5140 | ±3.0279 | -0.983 | 0.3255 |  |
| Education: high school or below (vs college) | +1.3691 | 2.7554 | ±5.5108 | +0.497 | 0.6193 |  |
| Site: UCSD (vs UAB) | +0.2509 | 1.8482 | ±3.6965 | +0.136 | 0.8920 |  |
| Site: UW (vs UAB) | +0.0055 | 1.4877 | ±2.9753 | +0.004 | 0.9970 |  |
| **Age (years)** | **-0.4613** | 0.0598 | ±0.1196 | **-7.713** | **1.23e-14** | *** |
| BMI (kg/m2) | -0.0738 | 0.1053 | ±0.2106 | -0.701 | 0.4834 |  |
| Hypertension | -0.9938 | 1.4773 | ±2.9546 | -0.673 | 0.5011 |  |
| High cholesterol | -0.5295 | 1.3297 | ±2.6594 | -0.398 | 0.6905 |  |
| Kidney disease | -1.1274 | 3.4535 | ±6.9070 | -0.326 | 0.7441 |  |
| Circulatory disease | +0.0442 | 1.8640 | ±3.7280 | +0.024 | 0.9811 |  |
| SD of daily means (mg/dL) | +0.0193 | 0.1862 | ±0.3724 | +0.104 | 0.9175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **374**, R² = **0.1613**, Adj R² = **0.1359**, F-statistic = **6.33** (p = **1.35e-09**), Residual SE = **12.113** on **362** df, AIC = **2938.9**, BIC = **2986.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3823** | 10.3510 | ±20.7021 | **+4.674** | **2.95e-06** | *** |
| Education: graduate level (vs college) | -1.4839 | 1.5005 | ±3.0011 | -0.989 | 0.3227 |  |
| Education: high school or below (vs college) | +1.3572 | 2.7561 | ±5.5121 | +0.492 | 0.6224 |  |
| Site: UCSD (vs UAB) | +0.2022 | 1.8490 | ±3.6980 | +0.109 | 0.9129 |  |
| Site: UW (vs UAB) | -0.0405 | 1.4821 | ±2.9643 | -0.027 | 0.9782 |  |
| **Age (years)** | **-0.4592** | 0.0597 | ±0.1193 | **-7.695** | **1.41e-14** | *** |
| BMI (kg/m2) | -0.0738 | 0.1052 | ±0.2104 | -0.701 | 0.4832 |  |
| Hypertension | -0.9846 | 1.4739 | ±2.9477 | -0.668 | 0.5041 |  |
| High cholesterol | -0.5392 | 1.3174 | ±2.6348 | -0.409 | 0.6823 |  |
| Kidney disease | -0.8500 | 3.4688 | ±6.9377 | -0.245 | 0.8064 |  |
| Circulatory disease | -0.0240 | 1.8526 | ±3.7052 | -0.013 | 0.9897 |  |
| Time in range 70-180, pooled (%) | +0.0684 | 0.0961 | ±0.1921 | +0.712 | 0.4767 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **374**, R² = **0.1613**, Adj R² = **0.1358**, F-statistic = **6.33** (p = **1.38e-09**), Residual SE = **12.114** on **362** df, AIC = **2939.0**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9749** | 10.1687 | ±20.3375 | **+4.816** | **1.46e-06** | *** |
| Education: graduate level (vs college) | -1.4868 | 1.5004 | ±3.0007 | -0.991 | 0.3217 |  |
| Education: high school or below (vs college) | +1.3479 | 2.7585 | ±5.5170 | +0.489 | 0.6251 |  |
| Site: UCSD (vs UAB) | +0.2144 | 1.8458 | ±3.6916 | +0.116 | 0.9075 |  |
| Site: UW (vs UAB) | -0.0355 | 1.4830 | ±2.9661 | -0.024 | 0.9809 |  |
| **Age (years)** | **-0.4589** | 0.0596 | ±0.1192 | **-7.698** | **1.39e-14** | *** |
| BMI (kg/m2) | -0.0731 | 0.1052 | ±0.2105 | -0.695 | 0.4873 |  |
| Hypertension | -0.9834 | 1.4748 | ±2.9496 | -0.667 | 0.5049 |  |
| High cholesterol | -0.5309 | 1.3181 | ±2.6362 | -0.403 | 0.6871 |  |
| Kidney disease | -0.8781 | 3.4737 | ±6.9474 | -0.253 | 0.8004 |  |
| Circulatory disease | -0.0181 | 1.8515 | ±3.7030 | -0.010 | 0.9922 |  |
| Avg. daily time in range 70-180 (%) | +0.0615 | 0.0929 | ±0.1859 | +0.662 | 0.5083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **374**, R² = **0.1611**, Adj R² = **0.1356**, F-statistic = **6.32** (p = **1.43e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.0**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2834** | 5.1417 | ±10.2833 | **+10.752** | **5.80e-27** | *** |
| Education: graduate level (vs college) | -1.4924 | 1.5047 | ±3.0095 | -0.992 | 0.3213 |  |
| Education: high school or below (vs college) | +1.3254 | 2.7587 | ±5.5174 | +0.480 | 0.6309 |  |
| Site: UCSD (vs UAB) | +0.1264 | 1.8653 | ±3.7305 | +0.068 | 0.9460 |  |
| Site: UW (vs UAB) | -0.0858 | 1.4848 | ±2.9695 | -0.058 | 0.9539 |  |
| **Age (years)** | **-0.4609** | 0.0598 | ±0.1196 | **-7.710** | **1.26e-14** | *** |
| BMI (kg/m2) | -0.0753 | 0.1054 | ±0.2108 | -0.714 | 0.4751 |  |
| Hypertension | -1.0356 | 1.4784 | ±2.9569 | -0.700 | 0.4836 |  |
| High cholesterol | -0.5828 | 1.3267 | ±2.6533 | -0.439 | 0.6604 |  |
| Kidney disease | -1.0656 | 3.4244 | ±6.8489 | -0.311 | 0.7557 |  |
| Circulatory disease | +0.0133 | 1.8544 | ±3.7089 | +0.007 | 0.9943 |  |
| Time < 54 (%) | -0.2903 | 0.6431 | ±1.2861 | -0.451 | 0.6517 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **374**, R² = **0.1609**, Adj R² = **0.1354**, F-statistic = **6.31** (p = **1.47e-09**), Residual SE = **12.117** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1471** | 5.1289 | ±10.2577 | **+10.752** | **5.78e-27** | *** |
| Education: graduate level (vs college) | -1.4983 | 1.5088 | ±3.0177 | -0.993 | 0.3207 |  |
| Education: high school or below (vs college) | +1.3287 | 2.7563 | ±5.5126 | +0.482 | 0.6298 |  |
| Site: UCSD (vs UAB) | +0.1625 | 1.8631 | ±3.7263 | +0.087 | 0.9305 |  |
| Site: UW (vs UAB) | -0.0791 | 1.4861 | ±2.9722 | -0.053 | 0.9576 |  |
| **Age (years)** | **-0.4601** | 0.0597 | ±0.1195 | **-7.701** | **1.35e-14** | *** |
| BMI (kg/m2) | -0.0745 | 0.1057 | ±0.2114 | -0.705 | 0.4810 |  |
| Hypertension | -1.0351 | 1.4775 | ±2.9550 | -0.701 | 0.4836 |  |
| High cholesterol | -0.5713 | 1.3234 | ±2.6467 | -0.432 | 0.6659 |  |
| Kidney disease | -1.0782 | 3.4267 | ±6.8534 | -0.315 | 0.7530 |  |
| Circulatory disease | +0.0146 | 1.8518 | ±3.7035 | +0.008 | 0.9937 |  |
| Avg. daily time < 54 (%) | -0.2960 | 0.8870 | ±1.7740 | -0.334 | 0.7386 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **374**, R² = **0.1608**, Adj R² = **0.1353**, F-statistic = **6.31** (p = **1.49e-09**), Residual SE = **12.117** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2091** | 5.2265 | ±10.4531 | **+10.563** | **4.41e-26** | *** |
| Education: graduate level (vs college) | -1.4908 | 1.5026 | ±3.0053 | -0.992 | 0.3211 |  |
| Education: high school or below (vs college) | +1.3178 | 2.7639 | ±5.5277 | +0.477 | 0.6335 |  |
| Site: UCSD (vs UAB) | +0.1945 | 1.8350 | ±3.6701 | +0.106 | 0.9156 |  |
| Site: UW (vs UAB) | -0.0522 | 1.4727 | ±2.9453 | -0.035 | 0.9717 |  |
| **Age (years)** | **-0.4615** | 0.0599 | ±0.1197 | **-7.710** | **1.26e-14** | *** |
| BMI (kg/m2) | -0.0730 | 0.1055 | ±0.2110 | -0.692 | 0.4892 |  |
| Hypertension | -1.0275 | 1.4780 | ±2.9560 | -0.695 | 0.4870 |  |
| High cholesterol | -0.5563 | 1.3310 | ±2.6620 | -0.418 | 0.6760 |  |
| Kidney disease | -1.1042 | 3.4254 | ±6.8509 | -0.322 | 0.7472 |  |
| Circulatory disease | +0.0206 | 1.8507 | ±3.7014 | +0.011 | 0.9911 |  |
| Time 54-69, pooled (%) | -0.0882 | 0.3328 | ±0.6657 | -0.265 | 0.7909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **374**, R² = **0.1608**, Adj R² = **0.1353**, F-statistic = **6.31** (p = **1.49e-09**), Residual SE = **12.117** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1690** | 5.1927 | ±10.3853 | **+10.624** | **2.29e-26** | *** |
| Education: graduate level (vs college) | -1.4955 | 1.5033 | ±3.0066 | -0.995 | 0.3198 |  |
| Education: high school or below (vs college) | +1.3090 | 2.7660 | ±5.5319 | +0.473 | 0.6360 |  |
| Site: UCSD (vs UAB) | +0.2019 | 1.8333 | ±3.6666 | +0.110 | 0.9123 |  |
| Site: UW (vs UAB) | -0.0549 | 1.4742 | ±2.9484 | -0.037 | 0.9703 |  |
| **Age (years)** | **-0.4611** | 0.0598 | ±0.1195 | **-7.715** | **1.21e-14** | *** |
| BMI (kg/m2) | -0.0729 | 0.1055 | ±0.2111 | -0.691 | 0.4895 |  |
| Hypertension | -1.0289 | 1.4771 | ±2.9542 | -0.697 | 0.4861 |  |
| High cholesterol | -0.5554 | 1.3287 | ±2.6574 | -0.418 | 0.6759 |  |
| Kidney disease | -1.1097 | 3.4233 | ±6.8465 | -0.324 | 0.7458 |  |
| Circulatory disease | +0.0235 | 1.8509 | ±3.7019 | +0.013 | 0.9899 |  |
| Avg. daily time 54-69 (%) | -0.0861 | 0.3313 | ±0.6626 | -0.260 | 0.7949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **374**, R² = **0.1610**, Adj R² = **0.1355**, F-statistic = **6.31** (p = **1.45e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2988** | 5.2398 | ±10.4795 | **+10.554** | **4.88e-26** | *** |
| Education: graduate level (vs college) | -1.4957 | 1.5032 | ±3.0064 | -0.995 | 0.3197 |  |
| Education: high school or below (vs college) | +1.3069 | 2.7647 | ±5.5294 | +0.473 | 0.6364 |  |
| Site: UCSD (vs UAB) | +0.1584 | 1.8436 | ±3.6873 | +0.086 | 0.9315 |  |
| Site: UW (vs UAB) | -0.0823 | 1.4742 | ±2.9485 | -0.056 | 0.9555 |  |
| **Age (years)** | **-0.4613** | 0.0598 | ±0.1196 | **-7.714** | **1.22e-14** | *** |
| BMI (kg/m2) | -0.0735 | 0.1057 | ±0.2114 | -0.695 | 0.4867 |  |
| Hypertension | -1.0422 | 1.4793 | ±2.9586 | -0.705 | 0.4811 |  |
| High cholesterol | -0.5757 | 1.3329 | ±2.6659 | -0.432 | 0.6658 |  |
| Kidney disease | -1.0894 | 3.4236 | ±6.8472 | -0.318 | 0.7503 |  |
| Circulatory disease | +0.0093 | 1.8499 | ±3.6999 | +0.005 | 0.9960 |  |
| Time < 70 (%) | -0.0910 | 0.2487 | ±0.4974 | -0.366 | 0.7145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **374**, R² = **0.1609**, Adj R² = **0.1354**, F-statistic = **6.31** (p = **1.47e-09**), Residual SE = **12.117** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1957** | 5.1976 | ±10.3952 | **+10.619** | **2.42e-26** | *** |
| Education: graduate level (vs college) | -1.5000 | 1.5048 | ±3.0096 | -0.997 | 0.3189 |  |
| Education: high school or below (vs college) | +1.3042 | 2.7647 | ±5.5295 | +0.472 | 0.6371 |  |
| Site: UCSD (vs UAB) | +0.1835 | 1.8383 | ±3.6766 | +0.100 | 0.9205 |  |
| Site: UW (vs UAB) | -0.0742 | 1.4758 | ±2.9516 | -0.050 | 0.9599 |  |
| **Age (years)** | **-0.4608** | 0.0597 | ±0.1194 | **-7.715** | **1.21e-14** | *** |
| BMI (kg/m2) | -0.0732 | 0.1057 | ±0.2113 | -0.693 | 0.4882 |  |
| Hypertension | -1.0385 | 1.4776 | ±2.9552 | -0.703 | 0.4822 |  |
| High cholesterol | -0.5665 | 1.3295 | ±2.6589 | -0.426 | 0.6700 |  |
| Kidney disease | -1.1005 | 3.4228 | ±6.8456 | -0.322 | 0.7478 |  |
| Circulatory disease | +0.0161 | 1.8497 | ±3.6994 | +0.009 | 0.9930 |  |
| Avg. daily time < 70 (%) | -0.0810 | 0.2667 | ±0.5334 | -0.304 | 0.7614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **374**, R² = **0.1611**, Adj R² = **0.1356**, F-statistic = **6.32** (p = **1.42e-09**), Residual SE = **12.115** on **362** df, AIC = **2939.0**, BIC = **2986.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +31.3398 | 44.7935 | ±89.5869 | +0.700 | 0.4841 |  |
| Education: graduate level (vs college) | -1.4928 | 1.5033 | ±3.0067 | -0.993 | 0.3207 |  |
| Education: high school or below (vs college) | +1.3331 | 2.7584 | ±5.5167 | +0.483 | 0.6289 |  |
| Site: UCSD (vs UAB) | +0.1384 | 1.8887 | ±3.7775 | +0.073 | 0.9416 |  |
| Site: UW (vs UAB) | -0.0856 | 1.4891 | ±2.9782 | -0.058 | 0.9541 |  |
| **Age (years)** | **-0.4599** | 0.0597 | ±0.1193 | **-7.708** | **1.27e-14** | *** |
| BMI (kg/m2) | -0.0758 | 0.1054 | ±0.2108 | -0.719 | 0.4721 |  |
| Hypertension | -1.0247 | 1.4737 | ±2.9475 | -0.695 | 0.4869 |  |
| High cholesterol | -0.5813 | 1.3195 | ±2.6389 | -0.441 | 0.6595 |  |
| Kidney disease | -0.9310 | 3.4850 | ±6.9700 | -0.267 | 0.7893 |  |
| Circulatory disease | +0.0011 | 1.8528 | ±3.7056 | +0.001 | 0.9995 |  |
| Time 54-250, pooled (%) | +0.2390 | 0.4549 | ±0.9098 | +0.525 | 0.5993 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **374**, R² = **0.1608**, Adj R² = **0.1353**, F-statistic = **6.31** (p = **1.50e-09**), Residual SE = **12.117** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +38.1738 | 50.6918 | ±101.3835 | +0.753 | 0.4514 |  |
| Education: graduate level (vs college) | -1.4931 | 1.5050 | ±3.0099 | -0.992 | 0.3212 |  |
| Education: high school or below (vs college) | +1.3400 | 2.7581 | ±5.5162 | +0.486 | 0.6271 |  |
| Site: UCSD (vs UAB) | +0.1849 | 1.8837 | ±3.7674 | +0.098 | 0.9218 |  |
| Site: UW (vs UAB) | -0.0528 | 1.4879 | ±2.9758 | -0.036 | 0.9717 |  |
| **Age (years)** | **-0.4598** | 0.0595 | ±0.1190 | **-7.729** | **1.09e-14** | *** |
| BMI (kg/m2) | -0.0745 | 0.1055 | ±0.2110 | -0.706 | 0.4802 |  |
| Hypertension | -1.0162 | 1.4719 | ±2.9438 | -0.690 | 0.4900 |  |
| High cholesterol | -0.5532 | 1.3148 | ±2.6295 | -0.421 | 0.6739 |  |
| Kidney disease | -0.9848 | 3.5213 | ±7.0426 | -0.280 | 0.7797 |  |
| Circulatory disease | +0.0143 | 1.8511 | ±3.7022 | +0.008 | 0.9938 |  |
| Avg. daily time 54-250 (%) | +0.1691 | 0.5132 | ±1.0264 | +0.329 | 0.7418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **374**, R² = **0.1610**, Adj R² = **0.1355**, F-statistic = **6.32** (p = **1.44e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0064** | 5.0778 | ±10.1557 | **+10.833** | **2.41e-27** | *** |
| Education: graduate level (vs college) | -1.4706 | 1.5042 | ±3.0084 | -0.978 | 0.3282 |  |
| Education: high school or below (vs college) | +1.3901 | 2.7539 | ±5.5078 | +0.505 | 0.6137 |  |
| Site: UCSD (vs UAB) | +0.2611 | 1.8272 | ±3.6543 | +0.143 | 0.8864 |  |
| Site: UW (vs UAB) | +0.0267 | 1.4805 | ±2.9611 | +0.018 | 0.9856 |  |
| **Age (years)** | **-0.4597** | 0.0598 | ±0.1196 | **-7.687** | **1.50e-14** | *** |
| BMI (kg/m2) | -0.0735 | 0.1050 | ±0.2099 | -0.701 | 0.4835 |  |
| Hypertension | -0.9525 | 1.4782 | ±2.9563 | -0.644 | 0.5193 |  |
| High cholesterol | -0.5005 | 1.3263 | ±2.6526 | -0.377 | 0.7059 |  |
| Kidney disease | -0.9287 | 3.4591 | ±6.9181 | -0.268 | 0.7883 |  |
| Circulatory disease | +0.0130 | 1.8593 | ±3.7187 | +0.007 | 0.9944 |  |
| Time 181-250, pooled (%) | -0.0614 | 0.1043 | ±0.2086 | -0.588 | 0.5564 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **374**, R² = **0.1610**, Adj R² = **0.1355**, F-statistic = **6.32** (p = **1.44e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9900** | 5.0800 | ±10.1600 | **+10.825** | **2.63e-27** | *** |
| Education: graduate level (vs college) | -1.4690 | 1.5047 | ±3.0095 | -0.976 | 0.3290 |  |
| Education: high school or below (vs college) | +1.3875 | 2.7541 | ±5.5083 | +0.504 | 0.6144 |  |
| Site: UCSD (vs UAB) | +0.2586 | 1.8284 | ±3.6568 | +0.141 | 0.8875 |  |
| Site: UW (vs UAB) | +0.0274 | 1.4801 | ±2.9602 | +0.019 | 0.9852 |  |
| **Age (years)** | **-0.4597** | 0.0598 | ±0.1195 | **-7.690** | **1.47e-14** | *** |
| BMI (kg/m2) | -0.0732 | 0.1050 | ±0.2101 | -0.697 | 0.4860 |  |
| Hypertension | -0.9491 | 1.4795 | ±2.9590 | -0.642 | 0.5212 |  |
| High cholesterol | -0.4983 | 1.3275 | ±2.6550 | -0.375 | 0.7074 |  |
| Kidney disease | -0.9285 | 3.4616 | ±6.9231 | -0.268 | 0.7885 |  |
| Circulatory disease | +0.0106 | 1.8585 | ±3.7171 | +0.006 | 0.9955 |  |
| Avg. daily time 181-250 (%) | -0.0607 | 0.1010 | ±0.2019 | -0.601 | 0.5479 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **374**, R² = **0.1610**, Adj R² = **0.1355**, F-statistic = **6.31** (p = **1.45e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0084** | 5.0764 | ±10.1528 | **+10.836** | **2.32e-27** | *** |
| Education: graduate level (vs college) | -1.4724 | 1.5039 | ±3.0078 | -0.979 | 0.3276 |  |
| Education: high school or below (vs college) | +1.3853 | 2.7546 | ±5.5091 | +0.503 | 0.6150 |  |
| Site: UCSD (vs UAB) | +0.2558 | 1.8286 | ±3.6572 | +0.140 | 0.8888 |  |
| Site: UW (vs UAB) | +0.0198 | 1.4810 | ±2.9619 | +0.013 | 0.9893 |  |
| **Age (years)** | **-0.4597** | 0.0597 | ±0.1195 | **-7.694** | **1.42e-14** | *** |
| BMI (kg/m2) | -0.0737 | 0.1049 | ±0.2099 | -0.702 | 0.4824 |  |
| Hypertension | -0.9581 | 1.4776 | ±2.9552 | -0.648 | 0.5167 |  |
| High cholesterol | -0.5061 | 1.3248 | ±2.6497 | -0.382 | 0.7024 |  |
| Kidney disease | -0.9265 | 3.4709 | ±6.9418 | -0.267 | 0.7895 |  |
| Circulatory disease | +0.0144 | 1.8586 | ±3.7171 | +0.008 | 0.9938 |  |
| Time > 180 (%) | -0.0517 | 0.0919 | ±0.1838 | -0.563 | 0.5735 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **374**, R² = **0.1610**, Adj R² = **0.1355**, F-statistic = **6.31** (p = **1.46e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9925** | 5.0778 | ±10.1555 | **+10.830** | **2.48e-27** | *** |
| Education: graduate level (vs college) | -1.4718 | 1.5042 | ±3.0084 | -0.978 | 0.3279 |  |
| Education: high school or below (vs college) | +1.3811 | 2.7551 | ±5.5102 | +0.501 | 0.6162 |  |
| Site: UCSD (vs UAB) | +0.2516 | 1.8307 | ±3.6614 | +0.137 | 0.8907 |  |
| Site: UW (vs UAB) | +0.0201 | 1.4806 | ±2.9613 | +0.014 | 0.9892 |  |
| **Age (years)** | **-0.4598** | 0.0597 | ±0.1194 | **-7.698** | **1.38e-14** | *** |
| BMI (kg/m2) | -0.0734 | 0.1050 | ±0.2100 | -0.699 | 0.4848 |  |
| Hypertension | -0.9576 | 1.4786 | ±2.9572 | -0.648 | 0.5172 |  |
| High cholesterol | -0.5041 | 1.3262 | ±2.6524 | -0.380 | 0.7039 |  |
| Kidney disease | -0.9341 | 3.4740 | ±6.9479 | -0.269 | 0.7880 |  |
| Circulatory disease | +0.0137 | 1.8578 | ±3.7155 | +0.007 | 0.9941 |  |
| Avg. daily time > 180 (%) | -0.0486 | 0.0881 | ±0.1763 | -0.551 | 0.5816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **374**, R² = **0.1610**, Adj R² = **0.1355**, F-statistic = **6.31** (p = **1.45e-09**), Residual SE = **12.116** on **362** df, AIC = **2939.1**, BIC = **2986.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9542** | 5.0824 | ±10.1648 | **+10.813** | **3.00e-27** | *** |
| Education: graduate level (vs college) | -1.5017 | 1.4995 | ±2.9990 | -1.001 | 0.3166 |  |
| Education: high school or below (vs college) | +1.3911 | 2.7590 | ±5.5180 | +0.504 | 0.6141 |  |
| Site: UCSD (vs UAB) | +0.2210 | 1.8452 | ±3.6903 | +0.120 | 0.9047 |  |
| Site: UW (vs UAB) | +0.0096 | 1.4822 | ±2.9645 | +0.006 | 0.9948 |  |
| **Age (years)** | **-0.4601** | 0.0598 | ±0.1195 | **-7.699** | **1.37e-14** | *** |
| BMI (kg/m2) | -0.0716 | 0.1053 | ±0.2107 | -0.680 | 0.4964 |  |
| Hypertension | -0.9529 | 1.4845 | ±2.9690 | -0.642 | 0.5209 |  |
| High cholesterol | -0.5203 | 1.3202 | ±2.6404 | -0.394 | 0.6935 |  |
| Kidney disease | -1.0964 | 3.4240 | ±6.8480 | -0.320 | 0.7488 |  |
| Circulatory disease | -0.0160 | 1.8620 | ±3.7240 | -0.009 | 0.9931 |  |
| Nocturnal time > 180 (%) | -0.0541 | 0.0969 | ±0.1938 | -0.559 | 0.5764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1351**, F-statistic = **6.30** (p = **1.55e-09**), Residual SE = **12.119** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0279** | 5.1012 | ±10.2024 | **+10.787** | **3.95e-27** | *** |
| Education: graduate level (vs college) | -1.4817 | 1.5016 | ±3.0032 | -0.987 | 0.3238 |  |
| Education: high school or below (vs college) | +1.3575 | 2.7615 | ±5.5230 | +0.492 | 0.6230 |  |
| Site: UCSD (vs UAB) | +0.2475 | 1.8064 | ±3.6128 | +0.137 | 0.8910 |  |
| Site: UW (vs UAB) | +0.0036 | 1.4839 | ±2.9678 | +0.002 | 0.9981 |  |
| **Age (years)** | **-0.4610** | 0.0592 | ±0.1185 | **-7.781** | **7.21e-15** | *** |
| BMI (kg/m2) | -0.0739 | 0.1053 | ±0.2106 | -0.702 | 0.4829 |  |
| Hypertension | -0.9869 | 1.4786 | ±2.9571 | -0.668 | 0.5044 |  |
| High cholesterol | -0.5223 | 1.3230 | ±2.6460 | -0.395 | 0.6930 |  |
| Kidney disease | -1.0956 | 3.4620 | ±6.9241 | -0.316 | 0.7517 |  |
| Circulatory disease | +0.0409 | 1.8500 | ±3.7000 | +0.022 | 0.9823 |  |
| Any reading > 250 during wear (0/1) | -0.1403 | 1.7330 | ±3.4659 | -0.081 | 0.9355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **374**, R² = **0.1607**, Adj R² = **0.1352**, F-statistic = **6.30** (p = **1.53e-09**), Residual SE = **12.118** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0179** | 5.0717 | ±10.1435 | **+10.848** | **2.04e-27** | *** |
| Education: graduate level (vs college) | -1.4802 | 1.5027 | ±3.0054 | -0.985 | 0.3246 |  |
| Education: high school or below (vs college) | +1.3581 | 2.7576 | ±5.5152 | +0.493 | 0.6224 |  |
| Site: UCSD (vs UAB) | +0.2319 | 1.8488 | ±3.6977 | +0.125 | 0.9002 |  |
| Site: UW (vs UAB) | -0.0069 | 1.4853 | ±2.9706 | -0.005 | 0.9963 |  |
| **Age (years)** | **-0.4605** | 0.0594 | ±0.1189 | **-7.748** | **9.34e-15** | *** |
| BMI (kg/m2) | -0.0741 | 0.1050 | ±0.2101 | -0.705 | 0.4805 |  |
| Hypertension | -0.9899 | 1.4739 | ±2.9478 | -0.672 | 0.5018 |  |
| High cholesterol | -0.5305 | 1.3171 | ±2.6342 | -0.403 | 0.6871 |  |
| Kidney disease | -1.0091 | 3.5642 | ±7.1284 | -0.283 | 0.7771 |  |
| Circulatory disease | +0.0336 | 1.8578 | ±3.7156 | +0.018 | 0.9856 |  |
| Time > 250 (%) | -0.1724 | 0.6917 | ±1.3834 | -0.249 | 0.8032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 374)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **374**, R² = **0.1606**, Adj R² = **0.1351**, F-statistic = **6.30** (p = **1.55e-09**), Residual SE = **12.119** on **362** df, AIC = **2939.2**, BIC = **2986.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0132** | 5.0669 | ±10.1339 | **+10.857** | **1.84e-27** | *** |
| Education: graduate level (vs college) | -1.4792 | 1.5020 | ±3.0040 | -0.985 | 0.3247 |  |
| Education: high school or below (vs college) | +1.3564 | 2.7574 | ±5.5148 | +0.492 | 0.6228 |  |
| Site: UCSD (vs UAB) | +0.2342 | 1.8519 | ±3.7038 | +0.126 | 0.8994 |  |
| Site: UW (vs UAB) | +0.0013 | 1.4840 | ±2.9681 | +0.001 | 0.9993 |  |
| **Age (years)** | **-0.4610** | 0.0594 | ±0.1189 | **-7.756** | **8.77e-15** | *** |
| BMI (kg/m2) | -0.0737 | 0.1050 | ±0.2100 | -0.701 | 0.4831 |  |
| Hypertension | -0.9921 | 1.4734 | ±2.9469 | -0.673 | 0.5008 |  |
| High cholesterol | -0.5248 | 1.3186 | ±2.6372 | -0.398 | 0.6906 |  |
| Kidney disease | -1.0763 | 3.5666 | ±7.1332 | -0.302 | 0.7628 |  |
| Circulatory disease | +0.0419 | 1.8568 | ±3.7135 | +0.023 | 0.9820 |  |
| Avg. daily time > 250 (%) | -0.0560 | 0.5714 | ±1.1428 | -0.098 | 0.9219 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 373; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1386**, F-statistic = **6.99** (p = **4.87e-10**), Residual SE = **7.530** on **362** df, AIC = **2575.5**, BIC = **2618.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0144** | 3.1060 | ±6.2119 | **+21.898** | **2.71e-106** | *** |
| Education: graduate level (vs college) | -0.2289 | 0.8765 | ±1.7529 | -0.261 | 0.7939 |  |
| Education: high school or below (vs college) | -1.4328 | 1.8767 | ±3.7534 | -0.763 | 0.4452 |  |
| **Site: UCSD (vs UAB)** | **-2.8131** | 1.1512 | ±2.3024 | **-2.444** | **0.0145** | * |
| **Site: UW (vs UAB)** | **-3.4383** | 0.9210 | ±1.8420 | **-3.733** | **1.89e-04** | *** |
| **Age (years)** | **-0.1762** | 0.0356 | ±0.0713 | **-4.945** | **7.62e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0661 | ±0.1322 | **+2.961** | **0.0031** | ** |
| Hypertension | -0.1064 | 0.8986 | ±1.7972 | -0.118 | 0.9058 |  |
| High cholesterol | -0.3792 | 0.8610 | ±1.7221 | -0.440 | 0.6596 |  |
| Kidney disease | -0.0416 | 2.0732 | ±4.1464 | -0.020 | 0.9840 |  |
| Circulatory disease | +0.6953 | 1.1884 | ±2.3767 | +0.585 | 0.5585 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **373**, R² = **0.1628**, Adj R² = **0.1373**, F-statistic = **6.38** (p = **1.10e-09**), Residual SE = **7.536** on **361** df, AIC = **2577.0**, BIC = **2624.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.8628** | 5.3962 | ±10.7923 | **+12.020** | **2.78e-33** | *** |
| Education: graduate level (vs college) | -0.1920 | 0.8816 | ±1.7632 | -0.218 | 0.8276 |  |
| Education: high school or below (vs college) | -1.5010 | 1.8640 | ±3.7281 | -0.805 | 0.4207 |  |
| **Site: UCSD (vs UAB)** | **-2.9266** | 1.1520 | ±2.3039 | **-2.541** | **0.0111** | * |
| **Site: UW (vs UAB)** | **-3.4578** | 0.9206 | ±1.8411 | **-3.756** | **1.73e-04** | *** |
| **Age (years)** | **-0.1805** | 0.0359 | ±0.0718 | **-5.025** | **5.02e-07** | *** |
| **BMI (kg/m2)** | **+0.1907** | 0.0668 | ±0.1336 | **+2.855** | **0.0043** | ** |
| Hypertension | -0.0959 | 0.9008 | ±1.8016 | -0.106 | 0.9152 |  |
| High cholesterol | -0.4747 | 0.8534 | ±1.7068 | -0.556 | 0.5781 |  |
| Kidney disease | -0.0809 | 2.0694 | ±4.1389 | -0.039 | 0.9688 |  |
| Circulatory disease | +0.7380 | 1.1832 | ±2.3664 | +0.624 | 0.5328 |  |
| HbA1c (%) | +0.6397 | 0.8644 | ±1.7288 | +0.740 | 0.4593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **373**, R² = **0.1626**, Adj R² = **0.1371**, F-statistic = **6.37** (p = **1.14e-09**), Residual SE = **7.537** on **361** df, AIC = **2577.1**, BIC = **2624.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.2639** | 4.2521 | ±8.5042 | **+15.584** | **9.37e-55** | *** |
| Education: graduate level (vs college) | -0.2554 | 0.8801 | ±1.7602 | -0.290 | 0.7717 |  |
| Education: high school or below (vs college) | -1.4854 | 1.8827 | ±3.7655 | -0.789 | 0.4301 |  |
| **Site: UCSD (vs UAB)** | **-2.8457** | 1.1548 | ±2.3095 | **-2.464** | **0.0137** | * |
| **Site: UW (vs UAB)** | **-3.4998** | 0.9398 | ±1.8795 | **-3.724** | **1.96e-04** | *** |
| **Age (years)** | **-0.1773** | 0.0358 | ±0.0716 | **-4.951** | **7.39e-07** | *** |
| **BMI (kg/m2)** | **+0.1938** | 0.0665 | ±0.1330 | **+2.914** | **0.0036** | ** |
| Hypertension | -0.1542 | 0.9073 | ±1.8146 | -0.170 | 0.8650 |  |
| High cholesterol | -0.4374 | 0.8526 | ±1.7053 | -0.513 | 0.6079 |  |
| Kidney disease | -0.1614 | 2.0766 | ±4.1532 | -0.078 | 0.9380 |  |
| Circulatory disease | +0.6998 | 1.1871 | ±2.3742 | +0.589 | 0.5555 |  |
| Mean glucose (mg/dL) | +0.0172 | 0.0298 | ±0.0595 | +0.578 | 0.5630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **373**, R² = **0.1626**, Adj R² = **0.1371**, F-statistic = **6.37** (p = **1.14e-09**), Residual SE = **7.537** on **361** df, AIC = **2577.1**, BIC = **2624.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8812** | 7.6774 | ±15.3548 | **+8.321** | **8.74e-17** | *** |
| Education: graduate level (vs college) | -0.2554 | 0.8801 | ±1.7602 | -0.290 | 0.7717 |  |
| Education: high school or below (vs college) | -1.4854 | 1.8827 | ±3.7655 | -0.789 | 0.4301 |  |
| **Site: UCSD (vs UAB)** | **-2.8457** | 1.1548 | ±2.3095 | **-2.464** | **0.0137** | * |
| **Site: UW (vs UAB)** | **-3.4998** | 0.9398 | ±1.8795 | **-3.724** | **1.96e-04** | *** |
| **Age (years)** | **-0.1773** | 0.0358 | ±0.0716 | **-4.951** | **7.39e-07** | *** |
| **BMI (kg/m2)** | **+0.1938** | 0.0665 | ±0.1330 | **+2.914** | **0.0036** | ** |
| Hypertension | -0.1542 | 0.9073 | ±1.8146 | -0.170 | 0.8650 |  |
| High cholesterol | -0.4374 | 0.8526 | ±1.7053 | -0.513 | 0.6079 |  |
| Kidney disease | -0.1614 | 2.0766 | ±4.1532 | -0.078 | 0.9380 |  |
| Circulatory disease | +0.6998 | 1.1871 | ±2.3742 | +0.589 | 0.5555 |  |
| GMI (%) | +0.7199 | 1.2445 | ±2.4889 | +0.578 | 0.5630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **373**, R² = **0.1623**, Adj R² = **0.1368**, F-statistic = **6.36** (p = **1.22e-09**), Residual SE = **7.538** on **361** df, AIC = **2577.2**, BIC = **2624.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.7836** | 4.0824 | ±8.1648 | **+16.359** | **3.75e-60** | *** |
| Education: graduate level (vs college) | -0.2344 | 0.8784 | ±1.7569 | -0.267 | 0.7896 |  |
| Education: high school or below (vs college) | -1.4777 | 1.8742 | ±3.7484 | -0.788 | 0.4304 |  |
| **Site: UCSD (vs UAB)** | **-2.8427** | 1.1510 | ±2.3019 | **-2.470** | **0.0135** | * |
| **Site: UW (vs UAB)** | **-3.4746** | 0.9310 | ±1.8621 | **-3.732** | **1.90e-04** | *** |
| **Age (years)** | **-0.1758** | 0.0358 | ±0.0715 | **-4.918** | **8.73e-07** | *** |
| **BMI (kg/m2)** | **+0.1920** | 0.0672 | ±0.1344 | **+2.857** | **0.0043** | ** |
| Hypertension | -0.1428 | 0.9055 | ±1.8109 | -0.158 | 0.8747 |  |
| High cholesterol | -0.4331 | 0.8577 | ±1.7155 | -0.505 | 0.6136 |  |
| Kidney disease | -0.0677 | 2.0740 | ±4.1481 | -0.033 | 0.9740 |  |
| Circulatory disease | +0.7156 | 1.1841 | ±2.3683 | +0.604 | 0.5456 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0122 | 0.0270 | ±0.0540 | +0.450 | 0.6526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **373**, R² = **0.1661**, Adj R² = **0.1407**, F-statistic = **6.54** (p = **5.90e-10**), Residual SE = **7.521** on **361** df, AIC = **2575.5**, BIC = **2622.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.5172** | 3.2247 | ±6.4493 | **+20.628** | **1.55e-94** | *** |
| Education: graduate level (vs college) | -0.2696 | 0.8761 | ±1.7522 | -0.308 | 0.7583 |  |
| Education: high school or below (vs college) | -1.4686 | 1.8744 | ±3.7489 | -0.783 | 0.4333 |  |
| **Site: UCSD (vs UAB)** | **-2.8892** | 1.1515 | ±2.3030 | **-2.509** | **0.0121** | * |
| **Site: UW (vs UAB)** | **-3.4568** | 0.9240 | ±1.8480 | **-3.741** | **1.83e-04** | *** |
| **Age (years)** | **-0.1827** | 0.0359 | ±0.0718 | **-5.087** | **3.64e-07** | *** |
| **BMI (kg/m2)** | **+0.1971** | 0.0663 | ±0.1326 | **+2.972** | **0.0030** | ** |
| Hypertension | -0.1680 | 0.9028 | ±1.8057 | -0.186 | 0.8524 |  |
| High cholesterol | -0.3697 | 0.8613 | ±1.7226 | -0.429 | 0.6677 |  |
| Kidney disease | -0.4509 | 2.1093 | ±4.2187 | -0.214 | 0.8307 |  |
| Circulatory disease | +0.7193 | 1.1794 | ±2.3588 | +0.610 | 0.5419 |  |
| Glucose SD, pooled (mg/dL) | +0.0878 | 0.0601 | ±0.1202 | +1.461 | 0.1439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **373**, R² = **0.1654**, Adj R² = **0.1399**, F-statistic = **6.50** (p = **6.83e-10**), Residual SE = **7.524** on **361** df, AIC = **2575.9**, BIC = **2622.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8400** | 3.1713 | ±6.3427 | **+21.076** | **1.31e-98** | *** |
| Education: graduate level (vs college) | -0.2506 | 0.8765 | ±1.7530 | -0.286 | 0.7749 |  |
| Education: high school or below (vs college) | -1.4897 | 1.8667 | ±3.7335 | -0.798 | 0.4249 |  |
| **Site: UCSD (vs UAB)** | **-2.9167** | 1.1548 | ±2.3095 | **-2.526** | **0.0115** | * |
| **Site: UW (vs UAB)** | **-3.4718** | 0.9263 | ±1.8527 | **-3.748** | **1.78e-04** | *** |
| **Age (years)** | **-0.1833** | 0.0361 | ±0.0722 | **-5.077** | **3.84e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0661 | ±0.1322 | **+2.960** | **0.0031** | ** |
| Hypertension | -0.1603 | 0.9039 | ±1.8078 | -0.177 | 0.8592 |  |
| High cholesterol | -0.3755 | 0.8615 | ±1.7230 | -0.436 | 0.6629 |  |
| Kidney disease | -0.4129 | 2.1032 | ±4.2064 | -0.196 | 0.8444 |  |
| Circulatory disease | +0.7287 | 1.1806 | ±2.3613 | +0.617 | 0.5371 |  |
| Avg. daily SD (mg/dL) | +0.0856 | 0.0650 | ±0.1299 | +1.317 | 0.1878 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **373**, R² = **0.1655**, Adj R² = **0.1401**, F-statistic = **6.51** (p = **6.61e-10**), Residual SE = **7.524** on **361** df, AIC = **2575.8**, BIC = **2622.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0901** | 3.3626 | ±6.7253 | **+19.654** | **5.32e-86** | *** |
| Education: graduate level (vs college) | -0.2434 | 0.8767 | ±1.7533 | -0.278 | 0.7813 |  |
| Education: high school or below (vs college) | -1.4134 | 1.8657 | ±3.7313 | -0.758 | 0.4487 |  |
| **Site: UCSD (vs UAB)** | **-2.8632** | 1.1507 | ±2.3015 | **-2.488** | **0.0128** | * |
| **Site: UW (vs UAB)** | **-3.3853** | 0.9206 | ±1.8413 | **-3.677** | **2.36e-04** | *** |
| **Age (years)** | **-0.1820** | 0.0359 | ±0.0718 | **-5.070** | **3.98e-07** | *** |
| **BMI (kg/m2)** | **+0.1989** | 0.0664 | ±0.1327 | **+2.998** | **0.0027** | ** |
| Hypertension | -0.1214 | 0.9025 | ±1.8050 | -0.134 | 0.8930 |  |
| High cholesterol | -0.3023 | 0.8643 | ±1.7287 | -0.350 | 0.7265 |  |
| Kidney disease | -0.3481 | 2.1234 | ±4.2468 | -0.164 | 0.8698 |  |
| Circulatory disease | +0.7208 | 1.1831 | ±2.3662 | +0.609 | 0.5424 |  |
| CV (%) | +0.1129 | 0.0821 | ±0.1642 | +1.375 | 0.1691 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **373**, R² = **0.1685**, Adj R² = **0.1432**, F-statistic = **6.65** (p = **3.73e-10**), Residual SE = **7.510** on **361** df, AIC = **2574.4**, BIC = **2621.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.8886** | 3.8218 | ±7.6437 | **+18.810** | **6.26e-79** | *** |
| Education: graduate level (vs college) | -0.3081 | 0.8782 | ±1.7564 | -0.351 | 0.7257 |  |
| Education: high school or below (vs college) | -1.4682 | 1.8619 | ±3.7238 | -0.789 | 0.4304 |  |
| **Site: UCSD (vs UAB)** | **-2.8834** | 1.1449 | ±2.2899 | **-2.518** | **0.0118** | * |
| **Site: UW (vs UAB)** | **-3.4252** | 0.9223 | ±1.8447 | **-3.714** | **2.04e-04** | *** |
| **Age (years)** | **-0.1848** | 0.0358 | ±0.0716 | **-5.160** | **2.47e-07** | *** |
| **BMI (kg/m2)** | **+0.1970** | 0.0663 | ±0.1326 | **+2.971** | **0.0030** | ** |
| Hypertension | -0.1338 | 0.9021 | ±1.8043 | -0.148 | 0.8821 |  |
| High cholesterol | -0.3189 | 0.8599 | ±1.7198 | -0.371 | 0.7108 |  |
| Kidney disease | -0.3830 | 2.1194 | ±4.2389 | -0.181 | 0.8566 |  |
| Circulatory disease | +0.7252 | 1.1790 | ±2.3579 | +0.615 | 0.5385 |  |
| Mean / SD ratio | -0.6110 | 0.3401 | ±0.6803 | -1.796 | 0.0725 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **373**, R² = **0.1683**, Adj R² = **0.1429**, F-statistic = **6.64** (p = **3.94e-10**), Residual SE = **7.511** on **361** df, AIC = **2574.6**, BIC = **2621.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.7985** | 3.8146 | ±7.6292 | **+18.822** | **4.99e-79** | *** |
| Education: graduate level (vs college) | -0.3047 | 0.8784 | ±1.7568 | -0.347 | 0.7287 |  |
| Education: high school or below (vs college) | -1.5468 | 1.8564 | ±3.7129 | -0.833 | 0.4047 |  |
| **Site: UCSD (vs UAB)** | **-2.9505** | 1.1493 | ±2.2987 | **-2.567** | **0.0103** | * |
| **Site: UW (vs UAB)** | **-3.4501** | 0.9241 | ±1.8483 | **-3.733** | **1.89e-04** | *** |
| **Age (years)** | **-0.1863** | 0.0360 | ±0.0721 | **-5.172** | **2.32e-07** | *** |
| **BMI (kg/m2)** | **+0.1941** | 0.0659 | ±0.1317 | **+2.946** | **0.0032** | ** |
| Hypertension | -0.1135 | 0.9047 | ±1.8094 | -0.125 | 0.9001 |  |
| High cholesterol | -0.3367 | 0.8609 | ±1.7218 | -0.391 | 0.6957 |  |
| Kidney disease | -0.4260 | 2.1069 | ±4.2139 | -0.202 | 0.8398 |  |
| Circulatory disease | +0.7445 | 1.1795 | ±2.3590 | +0.631 | 0.5279 |  |
| Avg. daily mean/SD | -0.4777 | 0.2775 | ±0.5550 | -1.721 | 0.0852 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **373**, R² = **0.1659**, Adj R² = **0.1405**, F-statistic = **6.53** (p = **6.11e-10**), Residual SE = **7.522** on **361** df, AIC = **2575.6**, BIC = **2622.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.0423** | 3.7689 | ±7.5378 | **+17.258** | **9.82e-67** | *** |
| Education: graduate level (vs college) | -0.2223 | 0.8737 | ±1.7474 | -0.254 | 0.7992 |  |
| Education: high school or below (vs college) | -1.3510 | 1.8850 | ±3.7699 | -0.717 | 0.4735 |  |
| **Site: UCSD (vs UAB)** | **-2.8908** | 1.1446 | ±2.2891 | **-2.526** | **0.0115** | * |
| **Site: UW (vs UAB)** | **-3.3120** | 0.9330 | ±1.8660 | **-3.550** | **3.85e-04** | *** |
| **Age (years)** | **-0.1737** | 0.0356 | ±0.0712 | **-4.882** | **1.05e-06** | *** |
| **BMI (kg/m2)** | **+0.1990** | 0.0662 | ±0.1324 | **+3.005** | **0.0027** | ** |
| Hypertension | -0.1690 | 0.9025 | ±1.8050 | -0.187 | 0.8514 |  |
| High cholesterol | -0.2706 | 0.8674 | ±1.7347 | -0.312 | 0.7551 |  |
| Kidney disease | -0.0815 | 2.0774 | ±4.1548 | -0.039 | 0.9687 |  |
| Circulatory disease | +0.7090 | 1.1850 | ±2.3700 | +0.598 | 0.5496 |  |
| MAG (mg/dL/h) | +0.0670 | 0.0499 | ±0.0998 | +1.343 | 0.1794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **373**, R² = **0.1641**, Adj R² = **0.1387**, F-statistic = **6.44** (p = **8.63e-10**), Residual SE = **7.530** on **361** df, AIC = **2576.4**, BIC = **2623.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.6554** | 3.2555 | ±6.5109 | **+20.475** | **3.60e-93** | *** |
| Education: graduate level (vs college) | -0.2285 | 0.8758 | ±1.7517 | -0.261 | 0.7942 |  |
| Education: high school or below (vs college) | -1.4672 | 1.8744 | ±3.7489 | -0.783 | 0.4338 |  |
| **Site: UCSD (vs UAB)** | **-2.8894** | 1.1539 | ±2.3078 | **-2.504** | **0.0123** | * |
| **Site: UW (vs UAB)** | **-3.4429** | 0.9243 | ±1.8486 | **-3.725** | **1.95e-04** | *** |
| **Age (years)** | **-0.1811** | 0.0362 | ±0.0724 | **-4.999** | **5.77e-07** | *** |
| **BMI (kg/m2)** | **+0.2006** | 0.0661 | ±0.1323 | **+3.033** | **0.0024** | ** |
| Hypertension | -0.1414 | 0.9041 | ±1.8081 | -0.156 | 0.8758 |  |
| High cholesterol | -0.3496 | 0.8649 | ±1.7298 | -0.404 | 0.6860 |  |
| Kidney disease | -0.2551 | 2.1017 | ±4.2035 | -0.121 | 0.9034 |  |
| Circulatory disease | +0.7154 | 1.1822 | ±2.3644 | +0.605 | 0.5451 |  |
| Avg. daily range (mg/dL) | +0.0153 | 0.0144 | ±0.0289 | +1.057 | 0.2905 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **373**, R² = **0.1676**, Adj R² = **0.1423**, F-statistic = **6.61** (p = **4.44e-10**), Residual SE = **7.514** on **361** df, AIC = **2574.9**, BIC = **2621.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8182** | 3.2668 | ±6.5335 | **+20.454** | **5.55e-93** | *** |
| Education: graduate level (vs college) | -0.3157 | 0.8748 | ±1.7497 | -0.361 | 0.7182 |  |
| Education: high school or below (vs college) | -1.3178 | 1.8906 | ±3.7812 | -0.697 | 0.4858 |  |
| **Site: UCSD (vs UAB)** | **-2.6903** | 1.1406 | ±2.2812 | **-2.359** | **0.0183** | * |
| **Site: UW (vs UAB)** | **-3.4206** | 0.9189 | ±1.8378 | **-3.722** | **1.97e-04** | *** |
| **Age (years)** | **-0.1760** | 0.0356 | ±0.0713 | **-4.938** | **7.89e-07** | *** |
| **BMI (kg/m2)** | **+0.1935** | 0.0672 | ±0.1343 | **+2.880** | **0.0040** | ** |
| Hypertension | -0.1240 | 0.8954 | ±1.7909 | -0.139 | 0.8898 |  |
| High cholesterol | -0.4335 | 0.8544 | ±1.7088 | -0.507 | 0.6119 |  |
| Kidney disease | -0.1875 | 2.0738 | ±4.1476 | -0.090 | 0.9280 |  |
| Circulatory disease | +0.6737 | 1.1783 | ±2.3565 | +0.572 | 0.5675 |  |
| SD of daily means (mg/dL) | +0.1776 | 0.1179 | ±0.2359 | +1.506 | 0.1320 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **373**, R² = **0.1626**, Adj R² = **0.1371**, F-statistic = **6.37** (p = **1.15e-09**), Residual SE = **7.537** on **361** df, AIC = **2577.1**, BIC = **2624.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.3521** | 8.2114 | ±16.4227 | **+8.811** | **1.24e-18** | *** |
| Education: graduate level (vs college) | -0.2239 | 0.8792 | ±1.7585 | -0.255 | 0.7990 |  |
| Education: high school or below (vs college) | -1.4333 | 1.8945 | ±3.7889 | -0.757 | 0.4493 |  |
| **Site: UCSD (vs UAB)** | **-2.7902** | 1.1603 | ±2.3206 | **-2.405** | **0.0162** | * |
| **Site: UW (vs UAB)** | **-3.4078** | 0.9171 | ±1.8343 | **-3.716** | **2.03e-04** | *** |
| **Age (years)** | **-0.1777** | 0.0359 | ±0.0718 | **-4.951** | **7.39e-07** | *** |
| **BMI (kg/m2)** | **+0.1959** | 0.0660 | ±0.1320 | **+2.968** | **0.0030** | ** |
| Hypertension | -0.1119 | 0.9000 | ±1.7999 | -0.124 | 0.9011 |  |
| High cholesterol | -0.3699 | 0.8660 | ±1.7319 | -0.427 | 0.6692 |  |
| Kidney disease | -0.2134 | 2.0714 | ±4.1429 | -0.103 | 0.9179 |  |
| Circulatory disease | +0.7414 | 1.1888 | ±2.3777 | +0.624 | 0.5328 |  |
| Time in range 70-180, pooled (%) | -0.0447 | 0.0779 | ±0.1559 | -0.573 | 0.5665 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **373**, R² = **0.1626**, Adj R² = **0.1370**, F-statistic = **6.37** (p = **1.16e-09**), Residual SE = **7.537** on **361** df, AIC = **2577.1**, BIC = **2624.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.1364** | 8.2665 | ±16.5331 | **+8.726** | **2.63e-18** | *** |
| Education: graduate level (vs college) | -0.2216 | 0.8806 | ±1.7611 | -0.252 | 0.8013 |  |
| Education: high school or below (vs college) | -1.4270 | 1.8936 | ±3.7871 | -0.754 | 0.4511 |  |
| **Site: UCSD (vs UAB)** | **-2.7975** | 1.1579 | ±2.3157 | **-2.416** | **0.0157** | * |
| **Site: UW (vs UAB)** | **-3.4098** | 0.9172 | ±1.8345 | **-3.717** | **2.01e-04** | *** |
| **Age (years)** | **-0.1779** | 0.0360 | ±0.0719 | **-4.948** | **7.49e-07** | *** |
| **BMI (kg/m2)** | **+0.1954** | 0.0660 | ±0.1321 | **+2.959** | **0.0031** | ** |
| Hypertension | -0.1129 | 0.8997 | ±1.7993 | -0.125 | 0.9001 |  |
| High cholesterol | -0.3752 | 0.8646 | ±1.7291 | -0.434 | 0.6643 |  |
| Kidney disease | -0.2017 | 2.0734 | ±4.1469 | -0.097 | 0.9225 |  |
| Circulatory disease | +0.7394 | 1.1892 | ±2.3784 | +0.622 | 0.5341 |  |
| Avg. daily time in range 70-180 (%) | -0.0419 | 0.0777 | ±0.1555 | -0.539 | 0.5896 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **373**, R² = **0.1619**, Adj R² = **0.1363**, F-statistic = **6.34** (p = **1.32e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.4**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.9483** | 3.1547 | ±6.3094 | **+21.539** | **6.77e-103** | *** |
| Education: graduate level (vs college) | -0.2254 | 0.8775 | ±1.7549 | -0.257 | 0.7973 |  |
| Education: high school or below (vs college) | -1.4251 | 1.8816 | ±3.7632 | -0.757 | 0.4488 |  |
| **Site: UCSD (vs UAB)** | **-2.7856** | 1.1640 | ±2.3280 | **-2.393** | **0.0167** | * |
| **Site: UW (vs UAB)** | **-3.4159** | 0.9322 | ±1.8644 | **-3.664** | **2.48e-04** | *** |
| **Age (years)** | **-0.1763** | 0.0357 | ±0.0713 | **-4.944** | **7.64e-07** | *** |
| **BMI (kg/m2)** | **+0.1961** | 0.0663 | ±0.1326 | **+2.958** | **0.0031** | ** |
| Hypertension | -0.0956 | 0.9038 | ±1.8075 | -0.106 | 0.9158 |  |
| High cholesterol | -0.3647 | 0.8635 | ±1.7270 | -0.422 | 0.6728 |  |
| Kidney disease | -0.0531 | 2.0807 | ±4.1614 | -0.026 | 0.9797 |  |
| Circulatory disease | +0.7035 | 1.1906 | ±2.3811 | +0.591 | 0.5546 |  |
| Time < 54 (%) | +0.0719 | 0.2395 | ±0.4790 | +0.300 | 0.7639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0001** | 3.1376 | ±6.2752 | **+21.673** | **3.70e-104** | *** |
| Education: graduate level (vs college) | -0.2267 | 0.8787 | ±1.7574 | -0.258 | 0.7964 |  |
| Education: high school or below (vs college) | -1.4298 | 1.8859 | ±3.7718 | -0.758 | 0.4484 |  |
| **Site: UCSD (vs UAB)** | **-2.8049** | 1.1599 | ±2.3199 | **-2.418** | **0.0156** | * |
| **Site: UW (vs UAB)** | **-3.4291** | 0.9352 | ±1.8703 | **-3.667** | **2.46e-04** | *** |
| **Age (years)** | **-0.1764** | 0.0358 | ±0.0716 | **-4.930** | **8.23e-07** | *** |
| **BMI (kg/m2)** | **+0.1958** | 0.0663 | ±0.1327 | **+2.951** | **0.0032** | ** |
| Hypertension | -0.1017 | 0.9065 | ±1.8130 | -0.112 | 0.9107 |  |
| High cholesterol | -0.3740 | 0.8658 | ±1.7316 | -0.432 | 0.6657 |  |
| Kidney disease | -0.0453 | 2.0785 | ±4.1570 | -0.022 | 0.9826 |  |
| Circulatory disease | +0.6988 | 1.1917 | ±2.3834 | +0.586 | 0.5576 |  |
| Avg. daily time < 54 (%) | +0.0324 | 0.4052 | ±0.8104 | +0.080 | 0.9362 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0334** | 3.1528 | ±6.3056 | **+21.579** | **2.84e-103** | *** |
| Education: graduate level (vs college) | -0.2302 | 0.8789 | ±1.7577 | -0.262 | 0.7934 |  |
| Education: high school or below (vs college) | -1.4366 | 1.8868 | ±3.7737 | -0.761 | 0.4464 |  |
| **Site: UCSD (vs UAB)** | **-2.8173** | 1.1572 | ±2.3144 | **-2.435** | **0.0149** | * |
| **Site: UW (vs UAB)** | **-3.4438** | 0.9333 | ±1.8666 | **-3.690** | **2.24e-04** | *** |
| **Age (years)** | **-0.1763** | 0.0357 | ±0.0715 | **-4.933** | **8.08e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0663 | ±0.1326 | **+2.953** | **0.0031** | ** |
| Hypertension | -0.1098 | 0.9063 | ±1.8126 | -0.121 | 0.9036 |  |
| High cholesterol | -0.3824 | 0.8628 | ±1.7257 | -0.443 | 0.6576 |  |
| Kidney disease | -0.0408 | 2.0762 | ±4.1524 | -0.020 | 0.9843 |  |
| Circulatory disease | +0.6927 | 1.1909 | ±2.3818 | +0.582 | 0.5608 |  |
| Time 54-69, pooled (%) | -0.0087 | 0.1725 | ±0.3450 | -0.050 | 0.9600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0188** | 3.1411 | ±6.2822 | **+21.654** | **5.52e-104** | *** |
| Education: graduate level (vs college) | -0.2294 | 0.8804 | ±1.7609 | -0.261 | 0.7944 |  |
| Education: high school or below (vs college) | -1.4342 | 1.8905 | ±3.7810 | -0.759 | 0.4481 |  |
| **Site: UCSD (vs UAB)** | **-2.8141** | 1.1554 | ±2.3107 | **-2.436** | **0.0149** | * |
| **Site: UW (vs UAB)** | **-3.4400** | 0.9338 | ±1.8676 | **-3.684** | **2.30e-04** | *** |
| **Age (years)** | **-0.1762** | 0.0357 | ±0.0714 | **-4.934** | **8.04e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0663 | ±0.1325 | **+2.954** | **0.0031** | ** |
| Hypertension | -0.1074 | 0.9068 | ±1.8135 | -0.118 | 0.9057 |  |
| High cholesterol | -0.3801 | 0.8632 | ±1.7264 | -0.440 | 0.6597 |  |
| Kidney disease | -0.0415 | 2.0754 | ±4.1509 | -0.020 | 0.9840 |  |
| Circulatory disease | +0.6946 | 1.1909 | ±2.3819 | +0.583 | 0.5597 |  |
| Avg. daily time 54-69 (%) | -0.0025 | 0.1731 | ±0.3463 | -0.014 | 0.9885 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0041** | 3.1673 | ±6.3346 | **+21.471** | **2.94e-102** | *** |
| Education: graduate level (vs college) | -0.2283 | 0.8788 | ±1.7576 | -0.260 | 0.7950 |  |
| Education: high school or below (vs college) | -1.4310 | 1.8870 | ±3.7741 | -0.758 | 0.4482 |  |
| **Site: UCSD (vs UAB)** | **-2.8102** | 1.1620 | ±2.3240 | **-2.418** | **0.0156** | * |
| **Site: UW (vs UAB)** | **-3.4351** | 0.9371 | ±1.8743 | **-3.666** | **2.47e-04** | *** |
| **Age (years)** | **-0.1762** | 0.0357 | ±0.0714 | **-4.934** | **8.04e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0662 | ±0.1325 | **+2.954** | **0.0031** | ** |
| Hypertension | -0.1045 | 0.9075 | ±1.8149 | -0.115 | 0.9083 |  |
| High cholesterol | -0.3773 | 0.8638 | ±1.7276 | -0.437 | 0.6622 |  |
| Kidney disease | -0.0424 | 2.0774 | ±4.1549 | -0.020 | 0.9837 |  |
| Circulatory disease | +0.6967 | 1.1914 | ±2.3828 | +0.585 | 0.5587 |  |
| Time < 70 (%) | +0.0033 | 0.1278 | ±0.2557 | +0.026 | 0.9793 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0129** | 3.1465 | ±6.2931 | **+21.615** | **1.29e-103** | *** |
| Education: graduate level (vs college) | -0.2288 | 0.8806 | ±1.7612 | -0.260 | 0.7950 |  |
| Education: high school or below (vs college) | -1.4324 | 1.8921 | ±3.7841 | -0.757 | 0.4490 |  |
| **Site: UCSD (vs UAB)** | **-2.8126** | 1.1575 | ±2.3149 | **-2.430** | **0.0151** | * |
| **Site: UW (vs UAB)** | **-3.4376** | 0.9375 | ±1.8751 | **-3.667** | **2.46e-04** | *** |
| **Age (years)** | **-0.1762** | 0.0357 | ±0.0714 | **-4.934** | **8.05e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0663 | ±0.1325 | **+2.954** | **0.0031** | ** |
| Hypertension | -0.1060 | 0.9084 | ±1.8168 | -0.117 | 0.9071 |  |
| High cholesterol | -0.3789 | 0.8644 | ±1.7288 | -0.438 | 0.6612 |  |
| Kidney disease | -0.0417 | 2.0757 | ±4.1515 | -0.020 | 0.9840 |  |
| Circulatory disease | +0.6956 | 1.1916 | ±2.3832 | +0.584 | 0.5594 |  |
| Avg. daily time < 70 (%) | +0.0007 | 0.1401 | ±0.2803 | +0.005 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.33** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3286** | 22.2939 | ±44.5877 | **+3.110** | **0.0019** | ** |
| Education: graduate level (vs college) | -0.2281 | 0.8794 | ±1.7589 | -0.259 | 0.7953 |  |
| Education: high school or below (vs college) | -1.4315 | 1.8821 | ±3.7641 | -0.761 | 0.4469 |  |
| **Site: UCSD (vs UAB)** | **-2.8076** | 1.1581 | ±2.3161 | **-2.424** | **0.0153** | * |
| **Site: UW (vs UAB)** | **-3.4333** | 0.9242 | ±1.8483 | **-3.715** | **2.03e-04** | *** |
| **Age (years)** | **-0.1763** | 0.0357 | ±0.0713 | **-4.945** | **7.60e-07** | *** |
| **BMI (kg/m2)** | **+0.1958** | 0.0663 | ±0.1326 | **+2.953** | **0.0031** | ** |
| Hypertension | -0.1045 | 0.9027 | ±1.8054 | -0.116 | 0.9078 |  |
| High cholesterol | -0.3760 | 0.8686 | ±1.7371 | -0.433 | 0.6651 |  |
| Kidney disease | -0.0516 | 2.1052 | ±4.2104 | -0.025 | 0.9804 |  |
| Circulatory disease | +0.6978 | 1.1910 | ±2.3821 | +0.586 | 0.5579 |  |
| Time 54-250, pooled (%) | -0.0133 | 0.2266 | ±0.4531 | -0.059 | 0.9533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.34** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.5**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.4154** | 31.7249 | ±63.4498 | **+2.062** | **0.0392** | * |
| Education: graduate level (vs college) | -0.2313 | 0.8827 | ±1.7654 | -0.262 | 0.7933 |  |
| Education: high school or below (vs college) | -1.4354 | 1.8840 | ±3.7680 | -0.762 | 0.4461 |  |
| **Site: UCSD (vs UAB)** | **-2.8212** | 1.1519 | ±2.3038 | **-2.449** | **0.0143** | * |
| **Site: UW (vs UAB)** | **-3.4471** | 0.9227 | ±1.8453 | **-3.736** | **1.87e-04** | *** |
| **Age (years)** | **-0.1760** | 0.0357 | ±0.0715 | **-4.925** | **8.44e-07** | *** |
| **BMI (kg/m2)** | **+0.1955** | 0.0663 | ±0.1326 | **+2.949** | **0.0032** | ** |
| Hypertension | -0.1100 | 0.9034 | ±1.8067 | -0.122 | 0.9030 |  |
| High cholesterol | -0.3837 | 0.8685 | ±1.7370 | -0.442 | 0.6586 |  |
| Kidney disease | -0.0219 | 2.1079 | ±4.2159 | -0.010 | 0.9917 |  |
| Circulatory disease | +0.6903 | 1.1933 | ±2.3865 | +0.579 | 0.5629 |  |
| Avg. daily time 54-250 (%) | +0.0261 | 0.3197 | ±0.6395 | +0.082 | 0.9350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **373**, R² = **0.1631**, Adj R² = **0.1376**, F-statistic = **6.39** (p = **1.05e-09**), Residual SE = **7.535** on **361** df, AIC = **2576.9**, BIC = **2623.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0272** | 3.1049 | ±6.2097 | **+21.910** | **2.09e-106** | *** |
| Education: graduate level (vs college) | -0.2353 | 0.8767 | ±1.7534 | -0.268 | 0.7884 |  |
| Education: high school or below (vs college) | -1.4710 | 1.8955 | ±3.7911 | -0.776 | 0.4377 |  |
| **Site: UCSD (vs UAB)** | **-2.8402** | 1.1575 | ±2.3151 | **-2.454** | **0.0141** | * |
| **Site: UW (vs UAB)** | **-3.4616** | 0.9291 | ±1.8582 | **-3.726** | **1.95e-04** | *** |
| **Age (years)** | **-0.1781** | 0.0359 | ±0.0719 | **-4.958** | **7.13e-07** | *** |
| **BMI (kg/m2)** | **+0.1957** | 0.0661 | ±0.1322 | **+2.962** | **0.0031** | ** |
| Hypertension | -0.1523 | 0.9007 | ±1.8014 | -0.169 | 0.8658 |  |
| High cholesterol | -0.4070 | 0.8568 | ±1.7135 | -0.475 | 0.6348 |  |
| Kidney disease | -0.2507 | 2.0628 | ±4.1257 | -0.122 | 0.9033 |  |
| Circulatory disease | +0.7335 | 1.1877 | ±2.3754 | +0.618 | 0.5369 |  |
| Time 181-250, pooled (%) | +0.0697 | 0.1064 | ±0.2129 | +0.655 | 0.5127 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **373**, R² = **0.1630**, Adj R² = **0.1375**, F-statistic = **6.39** (p = **1.06e-09**), Residual SE = **7.535** on **361** df, AIC = **2576.9**, BIC = **2624.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0443** | 3.1080 | ±6.2159 | **+21.894** | **2.99e-106** | *** |
| Education: graduate level (vs college) | -0.2365 | 0.8770 | ±1.7541 | -0.270 | 0.7874 |  |
| Education: high school or below (vs college) | -1.4662 | 1.8937 | ±3.7875 | -0.774 | 0.4388 |  |
| **Site: UCSD (vs UAB)** | **-2.8362** | 1.1573 | ±2.3146 | **-2.451** | **0.0143** | * |
| **Site: UW (vs UAB)** | **-3.4610** | 0.9294 | ±1.8588 | **-3.724** | **1.96e-04** | *** |
| **Age (years)** | **-0.1781** | 0.0359 | ±0.0718 | **-4.961** | **7.01e-07** | *** |
| **BMI (kg/m2)** | **+0.1953** | 0.0661 | ±0.1322 | **+2.955** | **0.0031** | ** |
| Hypertension | -0.1537 | 0.9010 | ±1.8020 | -0.171 | 0.8646 |  |
| High cholesterol | -0.4080 | 0.8566 | ±1.7131 | -0.476 | 0.6338 |  |
| Kidney disease | -0.2404 | 2.0656 | ±4.1313 | -0.116 | 0.9074 |  |
| Circulatory disease | +0.7342 | 1.1875 | ±2.3751 | +0.618 | 0.5364 |  |
| Avg. daily time 181-250 (%) | +0.0654 | 0.1021 | ±0.2042 | +0.640 | 0.5219 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **373**, R² = **0.1627**, Adj R² = **0.1372**, F-statistic = **6.38** (p = **1.13e-09**), Residual SE = **7.536** on **361** df, AIC = **2577.0**, BIC = **2624.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0236** | 3.1091 | ±6.2181 | **+21.879** | **4.11e-106** | *** |
| Education: graduate level (vs college) | -0.2331 | 0.8778 | ±1.7555 | -0.266 | 0.7906 |  |
| Education: high school or below (vs college) | -1.4621 | 1.8917 | ±3.7835 | -0.773 | 0.4396 |  |
| **Site: UCSD (vs UAB)** | **-2.8319** | 1.1578 | ±2.3155 | **-2.446** | **0.0144** | * |
| **Site: UW (vs UAB)** | **-3.4524** | 0.9280 | ±1.8559 | **-3.720** | **1.99e-04** | *** |
| **Age (years)** | **-0.1779** | 0.0359 | ±0.0719 | **-4.950** | **7.42e-07** | *** |
| **BMI (kg/m2)** | **+0.1959** | 0.0661 | ±0.1322 | **+2.964** | **0.0030** | ** |
| Hypertension | -0.1418 | 0.9004 | ±1.8009 | -0.157 | 0.8749 |  |
| High cholesterol | -0.3982 | 0.8582 | ±1.7163 | -0.464 | 0.6426 |  |
| Kidney disease | -0.2311 | 2.0686 | ±4.1372 | -0.112 | 0.9110 |  |
| Circulatory disease | +0.7281 | 1.1886 | ±2.3772 | +0.613 | 0.5401 |  |
| Time > 180 (%) | +0.0527 | 0.0961 | ±0.1923 | +0.548 | 0.5838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **373**, R² = **0.1627**, Adj R² = **0.1372**, F-statistic = **6.38** (p = **1.13e-09**), Residual SE = **7.536** on **361** df, AIC = **2577.1**, BIC = **2624.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0396** | 3.1119 | ±6.2238 | **+21.864** | **5.69e-106** | *** |
| Education: graduate level (vs college) | -0.2336 | 0.8783 | ±1.7565 | -0.266 | 0.7902 |  |
| Education: high school or below (vs college) | -1.4578 | 1.8893 | ±3.7786 | -0.772 | 0.4404 |  |
| **Site: UCSD (vs UAB)** | **-2.8276** | 1.1573 | ±2.3145 | **-2.443** | **0.0146** | * |
| **Site: UW (vs UAB)** | **-3.4526** | 0.9287 | ±1.8574 | **-3.718** | **2.01e-04** | *** |
| **Age (years)** | **-0.1779** | 0.0359 | ±0.0718 | **-4.955** | **7.22e-07** | *** |
| **BMI (kg/m2)** | **+0.1955** | 0.0661 | ±0.1322 | **+2.957** | **0.0031** | ** |
| Hypertension | -0.1421 | 0.9007 | ±1.8015 | -0.158 | 0.8747 |  |
| High cholesterol | -0.4002 | 0.8577 | ±1.7154 | -0.467 | 0.6408 |  |
| Kidney disease | -0.2223 | 2.0705 | ±4.1410 | -0.107 | 0.9145 |  |
| Circulatory disease | +0.7286 | 1.1884 | ±2.3768 | +0.613 | 0.5398 |  |
| Avg. daily time > 180 (%) | +0.0491 | 0.0936 | ±0.1872 | +0.525 | 0.5996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **373**, R² = **0.1621**, Adj R² = **0.1365**, F-statistic = **6.35** (p = **1.28e-09**), Residual SE = **7.539** on **361** df, AIC = **2577.3**, BIC = **2624.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.9792** | 3.1358 | ±6.2715 | **+21.679** | **3.26e-104** | *** |
| Education: graduate level (vs college) | -0.2439 | 0.8801 | ±1.7603 | -0.277 | 0.7817 |  |
| Education: high school or below (vs college) | -1.4140 | 1.8717 | ±3.7433 | -0.755 | 0.4500 |  |
| **Site: UCSD (vs UAB)** | **-2.8218** | 1.1591 | ±2.3181 | **-2.435** | **0.0149** | * |
| **Site: UW (vs UAB)** | **-3.4373** | 0.9242 | ±1.8483 | **-3.719** | **2.00e-04** | *** |
| **Age (years)** | **-0.1755** | 0.0361 | ±0.0721 | **-4.868** | **1.13e-06** | *** |
| **BMI (kg/m2)** | **+0.1967** | 0.0667 | ±0.1333 | **+2.951** | **0.0032** | ** |
| Hypertension | -0.0842 | 0.9006 | ±1.8011 | -0.093 | 0.9255 |  |
| High cholesterol | -0.3762 | 0.8612 | ±1.7224 | -0.437 | 0.6622 |  |
| Kidney disease | -0.0322 | 2.0748 | ±4.1496 | -0.016 | 0.9876 |  |
| Circulatory disease | +0.6612 | 1.1805 | ±2.3610 | +0.560 | 0.5754 |  |
| Nocturnal time > 180 (%) | -0.0294 | 0.0848 | ±0.1696 | -0.347 | 0.7286 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **373**, R² = **0.1618**, Adj R² = **0.1363**, F-statistic = **6.34** (p = **1.34e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.4**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0063** | 3.1067 | ±6.2135 | **+21.890** | **3.24e-106** | *** |
| Education: graduate level (vs college) | -0.2264 | 0.8781 | ±1.7563 | -0.258 | 0.7965 |  |
| Education: high school or below (vs college) | -1.4335 | 1.8887 | ±3.7773 | -0.759 | 0.4478 |  |
| **Site: UCSD (vs UAB)** | **-2.8201** | 1.1565 | ±2.3130 | **-2.438** | **0.0147** | * |
| **Site: UW (vs UAB)** | **-3.4377** | 0.9231 | ±1.8462 | **-3.724** | **1.96e-04** | *** |
| **Age (years)** | **-0.1765** | 0.0361 | ±0.0722 | **-4.890** | **1.01e-06** | *** |
| **BMI (kg/m2)** | **+0.1959** | 0.0661 | ±0.1323 | **+2.963** | **0.0030** | ** |
| Hypertension | -0.1100 | 0.8979 | ±1.7959 | -0.123 | 0.9025 |  |
| High cholesterol | -0.3804 | 0.8624 | ±1.7249 | -0.441 | 0.6591 |  |
| Kidney disease | -0.0530 | 2.0677 | ±4.1353 | -0.026 | 0.9795 |  |
| Circulatory disease | +0.6992 | 1.1878 | ±2.3755 | +0.589 | 0.5561 |  |
| Any reading > 250 during wear (0/1) | +0.0980 | 1.1155 | ±2.2310 | +0.088 | 0.9300 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **373**, R² = **0.1619**, Adj R² = **0.1363**, F-statistic = **6.34** (p = **1.32e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.4**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0154** | 3.1239 | ±6.2477 | **+21.773** | **4.20e-105** | *** |
| Education: graduate level (vs college) | -0.2302 | 0.8824 | ±1.7649 | -0.261 | 0.7942 |  |
| Education: high school or below (vs college) | -1.4319 | 1.8783 | ±3.7565 | -0.762 | 0.4459 |  |
| **Site: UCSD (vs UAB)** | **-2.8164** | 1.1528 | ±2.3057 | **-2.443** | **0.0146** | * |
| **Site: UW (vs UAB)** | **-3.4451** | 0.9201 | ±1.8402 | **-3.744** | **1.81e-04** | *** |
| **Age (years)** | **-0.1758** | 0.0358 | ±0.0717 | **-4.906** | **9.31e-07** | *** |
| **BMI (kg/m2)** | **+0.1953** | 0.0663 | ±0.1325 | **+2.948** | **0.0032** | ** |
| Hypertension | -0.1050 | 0.8986 | ±1.7973 | -0.117 | 0.9070 |  |
| High cholesterol | -0.3831 | 0.8663 | ±1.7326 | -0.442 | 0.6583 |  |
| Kidney disease | +0.0205 | 2.1159 | ±4.2318 | +0.010 | 0.9923 |  |
| Circulatory disease | +0.6874 | 1.1906 | ±2.3813 | +0.577 | 0.5637 |  |
| Time > 250 (%) | -0.1040 | 0.7159 | ±1.4319 | -0.145 | 0.8845 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 373)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **373**, R² = **0.1619**, Adj R² = **0.1363**, F-statistic = **6.34** (p = **1.33e-09**), Residual SE = **7.540** on **361** df, AIC = **2577.4**, BIC = **2624.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0096** | 3.1248 | ±6.2496 | **+21.764** | **5.05e-105** | *** |
| Education: graduate level (vs college) | -0.2307 | 0.8855 | ±1.7710 | -0.261 | 0.7944 |  |
| Education: high school or below (vs college) | -1.4332 | 1.8800 | ±3.7600 | -0.762 | 0.4459 |  |
| **Site: UCSD (vs UAB)** | **-2.8181** | 1.1514 | ±2.3027 | **-2.448** | **0.0144** | * |
| **Site: UW (vs UAB)** | **-3.4432** | 0.9210 | ±1.8420 | **-3.738** | **1.85e-04** | *** |
| **Age (years)** | **-0.1758** | 0.0357 | ±0.0715 | **-4.919** | **8.70e-07** | *** |
| **BMI (kg/m2)** | **+0.1955** | 0.0663 | ±0.1326 | **+2.949** | **0.0032** | ** |
| Hypertension | -0.1061 | 0.8989 | ±1.7977 | -0.118 | 0.9061 |  |
| High cholesterol | -0.3803 | 0.8649 | ±1.7299 | -0.440 | 0.6601 |  |
| Kidney disease | +0.0143 | 2.1124 | ±4.2248 | +0.007 | 0.9946 |  |
| Circulatory disease | +0.6881 | 1.1924 | ±2.3848 | +0.577 | 0.5639 |  |
| Avg. daily time > 250 (%) | -0.0876 | 0.7852 | ±1.5704 | -0.112 | 0.9112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 383; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **383**, R² = **0.0318**, Adj R² = **0.0058**, F-statistic = **1.22** (p = **0.2739**), Residual SE = **64.246** on **372** df, AIC = **4286.4**, BIC = **4329.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.7584** | 28.7322 | ±57.4644 | **+13.565** | **6.44e-42** | *** |
| Education: graduate level (vs college) | +3.7658 | 7.1714 | ±14.3427 | +0.525 | 0.5995 |  |
| Education: high school or below (vs college) | -27.0364 | 18.0823 | ±36.1646 | -1.495 | 0.1349 |  |
| Site: UCSD (vs UAB) | +4.7076 | 10.2337 | ±20.4673 | +0.460 | 0.6455 |  |
| Site: UW (vs UAB) | +4.1044 | 7.7963 | ±15.5926 | +0.526 | 0.5986 |  |
| Age (years) | -0.0326 | 0.3245 | ±0.6490 | -0.100 | 0.9200 |  |
| BMI (kg/m2) | -0.7317 | 0.6258 | ±1.2515 | -1.169 | 0.2423 |  |
| Hypertension | -5.6399 | 7.5929 | ±15.1857 | -0.743 | 0.4576 |  |
| High cholesterol | +3.7235 | 7.1997 | ±14.3993 | +0.517 | 0.6050 |  |
| Kidney disease | -8.1931 | 16.7644 | ±33.5287 | -0.489 | 0.6250 |  |
| Circulatory disease | +5.6051 | 11.2433 | ±22.4866 | +0.499 | 0.6181 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **383**, R² = **0.0327**, Adj R² = **0.0040**, F-statistic = **1.14** (p = **0.3277**), Residual SE = **64.303** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.6889** | 59.4390 | ±118.8780 | **+6.943** | **3.84e-12** | *** |
| Education: graduate level (vs college) | +3.5432 | 7.1697 | ±14.3393 | +0.494 | 0.6212 |  |
| Education: high school or below (vs college) | -26.5142 | 18.3908 | ±36.7816 | -1.442 | 0.1494 |  |
| Site: UCSD (vs UAB) | +5.5002 | 10.0647 | ±20.1294 | +0.546 | 0.5847 |  |
| Site: UW (vs UAB) | +4.2598 | 7.7936 | ±15.5872 | +0.547 | 0.5847 |  |
| Age (years) | -0.0008 | 0.3286 | ±0.6572 | -0.003 | 0.9979 |  |
| BMI (kg/m2) | -0.6930 | 0.6231 | ±1.2461 | -1.112 | 0.2661 |  |
| Hypertension | -5.7089 | 7.6277 | ±15.2554 | -0.748 | 0.4542 |  |
| High cholesterol | +4.4402 | 7.6135 | ±15.2270 | +0.583 | 0.5598 |  |
| Kidney disease | -7.9274 | 16.8619 | ±33.7238 | -0.470 | 0.6383 |  |
| Circulatory disease | +5.3008 | 11.5064 | ±23.0128 | +0.461 | 0.6450 |  |
| HbA1c (%) | -4.6852 | 9.4852 | ±18.9704 | -0.494 | 0.6213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **383**, R² = **0.0327**, Adj R² = **0.0040**, F-statistic = **1.14** (p = **0.3279**), Residual SE = **64.304** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.8885** | 40.4882 | ±80.9765 | **+9.975** | **1.95e-23** | *** |
| Education: graduate level (vs college) | +3.9952 | 7.2225 | ±14.4450 | +0.553 | 0.5802 |  |
| Education: high school or below (vs college) | -26.6165 | 18.1374 | ±36.2748 | -1.467 | 0.1422 |  |
| Site: UCSD (vs UAB) | +4.9495 | 10.3206 | ±20.6413 | +0.480 | 0.6315 |  |
| Site: UW (vs UAB) | +4.5876 | 7.9589 | ±15.9178 | +0.576 | 0.5643 |  |
| Age (years) | -0.0222 | 0.3229 | ±0.6459 | -0.069 | 0.9451 |  |
| BMI (kg/m2) | -0.7165 | 0.6266 | ±1.2532 | -1.143 | 0.2529 |  |
| Hypertension | -5.2433 | 7.7438 | ±15.4876 | -0.677 | 0.4983 |  |
| High cholesterol | +4.1777 | 7.2376 | ±14.4752 | +0.577 | 0.5638 |  |
| Kidney disease | -7.3440 | 17.0208 | ±34.0417 | -0.431 | 0.6661 |  |
| Circulatory disease | +5.5652 | 11.2850 | ±22.5700 | +0.493 | 0.6219 |  |
| Mean glucose (mg/dL) | -0.1397 | 0.2434 | ±0.4869 | -0.574 | 0.5661 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **383**, R² = **0.0327**, Adj R² = **0.0040**, F-statistic = **1.14** (p = **0.3279**), Residual SE = **64.304** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+423.2173** | 68.6262 | ±137.2524 | **+6.167** | **6.96e-10** | *** |
| Education: graduate level (vs college) | +3.9952 | 7.2225 | ±14.4450 | +0.553 | 0.5802 |  |
| Education: high school or below (vs college) | -26.6165 | 18.1374 | ±36.2748 | -1.467 | 0.1422 |  |
| Site: UCSD (vs UAB) | +4.9495 | 10.3206 | ±20.6413 | +0.480 | 0.6315 |  |
| Site: UW (vs UAB) | +4.5876 | 7.9589 | ±15.9178 | +0.576 | 0.5643 |  |
| Age (years) | -0.0222 | 0.3229 | ±0.6459 | -0.069 | 0.9451 |  |
| BMI (kg/m2) | -0.7165 | 0.6266 | ±1.2532 | -1.143 | 0.2529 |  |
| Hypertension | -5.2433 | 7.7438 | ±15.4876 | -0.677 | 0.4983 |  |
| High cholesterol | +4.1777 | 7.2376 | ±14.4752 | +0.577 | 0.5638 |  |
| Kidney disease | -7.3440 | 17.0208 | ±34.0417 | -0.431 | 0.6661 |  |
| Circulatory disease | +5.5652 | 11.2850 | ±22.5700 | +0.493 | 0.6219 |  |
| GMI (%) | -5.8395 | 10.1774 | ±20.3549 | -0.574 | 0.5661 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **383**, R² = **0.0348**, Adj R² = **0.0061**, F-statistic = **1.21** (p = **0.2752**), Residual SE = **64.236** on **371** df, AIC = **4287.2**, BIC = **4334.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+413.4796** | 39.2717 | ±78.5435 | **+10.529** | **6.37e-26** | *** |
| Education: graduate level (vs college) | +3.9669 | 7.1764 | ±14.3528 | +0.553 | 0.5804 |  |
| Education: high school or below (vs college) | -26.1524 | 18.1757 | ±36.3514 | -1.439 | 0.1502 |  |
| Site: UCSD (vs UAB) | +5.2626 | 10.3865 | ±20.7729 | +0.507 | 0.6124 |  |
| Site: UW (vs UAB) | +4.7871 | 7.9178 | ±15.8355 | +0.605 | 0.5454 |  |
| Age (years) | -0.0393 | 0.3250 | ±0.6500 | -0.121 | 0.9037 |  |
| BMI (kg/m2) | -0.6553 | 0.6288 | ±1.2576 | -1.042 | 0.2973 |  |
| Hypertension | -4.9859 | 7.7362 | ±15.4725 | -0.644 | 0.5193 |  |
| High cholesterol | +4.7649 | 7.2491 | ±14.4982 | +0.657 | 0.5110 |  |
| Kidney disease | -7.7948 | 16.7667 | ±33.5333 | -0.465 | 0.6420 |  |
| Circulatory disease | +5.2313 | 11.2490 | ±22.4981 | +0.465 | 0.6419 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.2364 | 0.2357 | ±0.4715 | -1.003 | 0.3160 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **383**, R² = **0.0318**, Adj R² = **0.0031**, F-statistic = **1.11** (p = **0.3523**), Residual SE = **64.332** on **371** df, AIC = **4288.4**, BIC = **4335.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.6929** | 30.1400 | ±60.2800 | **+12.929** | **3.07e-38** | *** |
| Education: graduate level (vs college) | +3.7637 | 7.2339 | ±14.4678 | +0.520 | 0.6029 |  |
| Education: high school or below (vs college) | -27.0380 | 18.1029 | ±36.2057 | -1.494 | 0.1353 |  |
| Site: UCSD (vs UAB) | +4.7036 | 10.2602 | ±20.5205 | +0.458 | 0.6466 |  |
| Site: UW (vs UAB) | +4.1033 | 7.8178 | ±15.6357 | +0.525 | 0.5997 |  |
| Age (years) | -0.0329 | 0.3304 | ±0.6608 | -0.100 | 0.9206 |  |
| BMI (kg/m2) | -0.7317 | 0.6270 | ±1.2539 | -1.167 | 0.2432 |  |
| Hypertension | -5.6429 | 7.5983 | ±15.1965 | -0.743 | 0.4577 |  |
| High cholesterol | +3.7239 | 7.2240 | ±14.4480 | +0.515 | 0.6062 |  |
| Kidney disease | -8.2100 | 17.1006 | ±34.2013 | -0.480 | 0.6312 |  |
| Circulatory disease | +5.6060 | 11.2871 | ±22.5742 | +0.497 | 0.6194 |  |
| Glucose SD, pooled (mg/dL) | +0.0040 | 0.5719 | ±1.1438 | +0.007 | 0.9945 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **383**, R² = **0.0319**, Adj R² = **0.0031**, F-statistic = **1.11** (p = **0.3522**), Residual SE = **64.332** on **371** df, AIC = **4288.4**, BIC = **4335.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.0685** | 29.7183 | ±59.4365 | **+13.126** | **2.35e-39** | *** |
| Education: graduate level (vs college) | +3.7731 | 7.2200 | ±14.4399 | +0.523 | 0.6013 |  |
| Education: high school or below (vs college) | -27.0206 | 18.0938 | ±36.1877 | -1.493 | 0.1353 |  |
| Site: UCSD (vs UAB) | +4.7396 | 10.2561 | ±20.5122 | +0.462 | 0.6440 |  |
| Site: UW (vs UAB) | +4.1152 | 7.8159 | ±15.6318 | +0.527 | 0.5985 |  |
| Age (years) | -0.0306 | 0.3319 | ±0.6637 | -0.092 | 0.9266 |  |
| BMI (kg/m2) | -0.7317 | 0.6269 | ±1.2537 | -1.167 | 0.2431 |  |
| Hypertension | -5.6251 | 7.6048 | ±15.2097 | -0.740 | 0.4595 |  |
| High cholesterol | +3.7233 | 7.2225 | ±14.4450 | +0.516 | 0.6062 |  |
| Kidney disease | -8.0985 | 17.0449 | ±34.0897 | -0.475 | 0.6347 |  |
| Circulatory disease | +5.5970 | 11.2952 | ±22.5903 | +0.496 | 0.6202 |  |
| Avg. daily SD (mg/dL) | -0.0233 | 0.6172 | ±1.2344 | -0.038 | 0.9699 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **383**, R² = **0.0320**, Adj R² = **0.0033**, F-statistic = **1.11** (p = **0.3487**), Residual SE = **64.328** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+386.9762** | 30.3476 | ±60.6952 | **+12.751** | **3.06e-37** | *** |
| Education: graduate level (vs college) | +3.7375 | 7.2015 | ±14.4030 | +0.519 | 0.6038 |  |
| Education: high school or below (vs college) | -27.0091 | 18.1219 | ±36.2438 | -1.490 | 0.1361 |  |
| Site: UCSD (vs UAB) | +4.6052 | 10.2256 | ±20.4511 | +0.450 | 0.6524 |  |
| Site: UW (vs UAB) | +4.1690 | 7.8318 | ±15.6637 | +0.532 | 0.5945 |  |
| Age (years) | -0.0419 | 0.3325 | ±0.6651 | -0.126 | 0.8998 |  |
| BMI (kg/m2) | -0.7270 | 0.6262 | ±1.2524 | -1.161 | 0.2457 |  |
| Hypertension | -5.6657 | 7.5912 | ±15.1825 | -0.746 | 0.4555 |  |
| High cholesterol | +3.8295 | 7.2590 | ±14.5180 | +0.528 | 0.5978 |  |
| Kidney disease | -8.6143 | 16.8334 | ±33.6668 | -0.512 | 0.6088 |  |
| Circulatory disease | +5.6323 | 11.2781 | ±22.5563 | +0.499 | 0.6175 |  |
| CV (%) | +0.1670 | 0.7431 | ±1.4861 | +0.225 | 0.8222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **383**, R² = **0.0319**, Adj R² = **0.0032**, F-statistic = **1.11** (p = **0.3511**), Residual SE = **64.331** on **371** df, AIC = **4288.4**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.2193** | 35.3159 | ±70.6318 | **+11.106** | **1.17e-28** | *** |
| Education: graduate level (vs college) | +3.7161 | 7.2226 | ±14.4452 | +0.515 | 0.6069 |  |
| Education: high school or below (vs college) | -27.0566 | 18.0990 | ±36.1980 | -1.495 | 0.1349 |  |
| Site: UCSD (vs UAB) | +4.6344 | 10.2216 | ±20.4432 | +0.453 | 0.6503 |  |
| Site: UW (vs UAB) | +4.1035 | 7.8119 | ±15.6239 | +0.525 | 0.5994 |  |
| Age (years) | -0.0383 | 0.3335 | ±0.6670 | -0.115 | 0.9085 |  |
| BMI (kg/m2) | -0.7308 | 0.6266 | ±1.2532 | -1.166 | 0.2435 |  |
| Hypertension | -5.6528 | 7.5925 | ±15.1851 | -0.745 | 0.4566 |  |
| High cholesterol | +3.7543 | 7.2376 | ±14.4752 | +0.519 | 0.6040 |  |
| Kidney disease | -8.4043 | 16.8709 | ±33.7419 | -0.498 | 0.6184 |  |
| Circulatory disease | +5.6115 | 11.2683 | ±22.5366 | +0.498 | 0.6185 |  |
| Mean / SD ratio | -0.3841 | 2.8306 | ±5.6611 | -0.136 | 0.8921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **383**, R² = **0.0323**, Adj R² = **0.0036**, F-statistic = **1.12** (p = **0.3403**), Residual SE = **64.318** on **371** df, AIC = **4288.2**, BIC = **4335.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+381.8080** | 35.3519 | ±70.7038 | **+10.800** | **3.43e-27** | *** |
| Education: graduate level (vs college) | +3.9379 | 7.2321 | ±14.4642 | +0.545 | 0.5861 |  |
| Education: high school or below (vs college) | -26.8070 | 18.0845 | ±36.1691 | -1.482 | 0.1383 |  |
| Site: UCSD (vs UAB) | +5.0998 | 10.2078 | ±20.4157 | +0.500 | 0.6174 |  |
| Site: UW (vs UAB) | +4.1572 | 7.8098 | ±15.6196 | +0.532 | 0.5945 |  |
| Age (years) | -0.0109 | 0.3342 | ±0.6684 | -0.033 | 0.9741 |  |
| BMI (kg/m2) | -0.7285 | 0.6261 | ±1.2523 | -1.163 | 0.2447 |  |
| Hypertension | -5.6575 | 7.6153 | ±15.2305 | -0.743 | 0.4575 |  |
| High cholesterol | +3.6754 | 7.2281 | ±14.4563 | +0.508 | 0.6111 |  |
| Kidney disease | -7.3882 | 16.9944 | ±33.9888 | -0.435 | 0.6638 |  |
| Circulatory disease | +5.5660 | 11.2766 | ±22.5531 | +0.494 | 0.6216 |  |
| Avg. daily mean/SD | +0.9926 | 2.2142 | ±4.4284 | +0.448 | 0.6540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **383**, R² = **0.0647**, Adj R² = **0.0370**, F-statistic = **2.33** (p = **0.0088**), Residual SE = **63.232** on **371** df, AIC = **4275.2**, BIC = **4322.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+456.1350** | 32.4454 | ±64.8908 | **+14.059** | **6.83e-45** | *** |
| Education: graduate level (vs college) | +3.8602 | 7.0866 | ±14.1732 | +0.545 | 0.5859 |  |
| Education: high school or below (vs college) | -28.7638 | 17.6651 | ±35.3301 | -1.628 | 0.1035 |  |
| Site: UCSD (vs UAB) | +6.9496 | 10.1154 | ±20.2307 | +0.687 | 0.4921 |  |
| Site: UW (vs UAB) | +1.5296 | 7.5842 | ±15.1684 | +0.202 | 0.8402 |  |
| Age (years) | -0.0857 | 0.3180 | ±0.6360 | -0.270 | 0.7875 |  |
| BMI (kg/m2) | -0.8003 | 0.5857 | ±1.1715 | -1.366 | 0.1719 |  |
| Hypertension | -4.1816 | 7.4257 | ±14.8513 | -0.563 | 0.5733 |  |
| High cholesterol | +1.5340 | 7.2147 | ±14.4293 | +0.213 | 0.8316 |  |
| Kidney disease | -7.9073 | 16.9310 | ±33.8620 | -0.467 | 0.6405 |  |
| Circulatory disease | +5.4063 | 11.1625 | ±22.3250 | +0.484 | 0.6282 |  |
| **MAG (mg/dL/h)** | **-1.5175** | 0.4233 | ±0.8466 | **-3.585** | **3.37e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **383**, R² = **0.0321**, Adj R² = **0.0034**, F-statistic = **1.12** (p = **0.3446**), Residual SE = **64.323** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.4288** | 31.2084 | ±62.4168 | **+12.607** | **1.94e-36** | *** |
| Education: graduate level (vs college) | +3.7696 | 7.1959 | ±14.3918 | +0.524 | 0.6004 |  |
| Education: high school or below (vs college) | -26.9359 | 18.1147 | ±36.2293 | -1.487 | 0.1370 |  |
| Site: UCSD (vs UAB) | +4.9497 | 10.2552 | ±20.5105 | +0.483 | 0.6293 |  |
| Site: UW (vs UAB) | +4.1287 | 7.8124 | ±15.6249 | +0.528 | 0.5972 |  |
| Age (years) | -0.0187 | 0.3283 | ±0.6566 | -0.057 | 0.9546 |  |
| BMI (kg/m2) | -0.7452 | 0.6299 | ±1.2598 | -1.183 | 0.2368 |  |
| Hypertension | -5.5456 | 7.6038 | ±15.2077 | -0.729 | 0.4658 |  |
| High cholesterol | +3.6450 | 7.2398 | ±14.4796 | +0.503 | 0.6146 |  |
| Kidney disease | -7.6290 | 16.9675 | ±33.9349 | -0.450 | 0.6530 |  |
| Circulatory disease | +5.5441 | 11.3105 | ±22.6211 | +0.490 | 0.6240 |  |
| Avg. daily range (mg/dL) | -0.0419 | 0.1335 | ±0.2670 | -0.314 | 0.7538 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **383**, R² = **0.0320**, Adj R² = **0.0033**, F-statistic = **1.12** (p = **0.3474**), Residual SE = **64.327** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.1813** | 29.2913 | ±58.5827 | **+13.252** | **4.37e-40** | *** |
| Education: graduate level (vs college) | +3.6252 | 7.2606 | ±14.5213 | +0.499 | 0.6176 |  |
| Education: high school or below (vs college) | -26.8731 | 18.1106 | ±36.2212 | -1.484 | 0.1379 |  |
| Site: UCSD (vs UAB) | +4.8551 | 10.2509 | ±20.5018 | +0.474 | 0.6358 |  |
| Site: UW (vs UAB) | +4.1316 | 7.8091 | ±15.6183 | +0.529 | 0.5968 |  |
| Age (years) | -0.0328 | 0.3250 | ±0.6501 | -0.101 | 0.9196 |  |
| BMI (kg/m2) | -0.7351 | 0.6252 | ±1.2504 | -1.176 | 0.2397 |  |
| Hypertension | -5.6591 | 7.6036 | ±15.2071 | -0.744 | 0.4567 |  |
| High cholesterol | +3.6407 | 7.2135 | ±14.4270 | +0.505 | 0.6138 |  |
| Kidney disease | -8.3448 | 16.8707 | ±33.7415 | -0.495 | 0.6209 |  |
| Circulatory disease | +5.5494 | 11.2826 | ±22.5652 | +0.492 | 0.6228 |  |
| SD of daily means (mg/dL) | +0.2421 | 0.8952 | ±1.7904 | +0.270 | 0.7869 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **383**, R² = **0.0329**, Adj R² = **0.0042**, F-statistic = **1.15** (p = **0.3230**), Residual SE = **64.297** on **371** df, AIC = **4288.0**, BIC = **4335.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+429.5163** | 75.4559 | ±150.9118 | **+5.692** | **1.25e-08** | *** |
| Education: graduate level (vs college) | +3.7852 | 7.1953 | ±14.3906 | +0.526 | 0.5988 |  |
| Education: high school or below (vs college) | -27.0366 | 18.1066 | ±36.2132 | -1.493 | 0.1354 |  |
| Site: UCSD (vs UAB) | +4.9558 | 10.2491 | ±20.4983 | +0.484 | 0.6287 |  |
| Site: UW (vs UAB) | +4.3687 | 7.8195 | ±15.6390 | +0.559 | 0.5764 |  |
| Age (years) | -0.0464 | 0.3269 | ±0.6537 | -0.142 | 0.8872 |  |
| BMI (kg/m2) | -0.7295 | 0.6259 | ±1.2517 | -1.166 | 0.2438 |  |
| Hypertension | -5.7223 | 7.5917 | ±15.1833 | -0.754 | 0.4510 |  |
| High cholesterol | +3.8041 | 7.2028 | ±14.4057 | +0.528 | 0.5974 |  |
| Kidney disease | -9.5681 | 17.0928 | ±34.1856 | -0.560 | 0.5756 |  |
| Circulatory disease | +5.9760 | 11.2620 | ±22.5240 | +0.531 | 0.5957 |  |
| Time in range 70-180, pooled (%) | -0.4089 | 0.6939 | ±1.3878 | -0.589 | 0.5557 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **383**, R² = **0.0332**, Adj R² = **0.0045**, F-statistic = **1.16** (p = **0.3161**), Residual SE = **64.289** on **371** df, AIC = **4287.9**, BIC = **4335.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+433.0823** | 73.8825 | ±147.7650 | **+5.862** | **4.58e-09** | *** |
| Education: graduate level (vs college) | +3.8132 | 7.1900 | ±14.3800 | +0.530 | 0.5959 |  |
| Education: high school or below (vs college) | -26.9726 | 18.1197 | ±36.2395 | -1.489 | 0.1366 |  |
| Site: UCSD (vs UAB) | +4.9122 | 10.2413 | ±20.4825 | +0.480 | 0.6315 |  |
| Site: UW (vs UAB) | +4.3883 | 7.8140 | ±15.6281 | +0.562 | 0.5744 |  |
| Age (years) | -0.0506 | 0.3272 | ±0.6545 | -0.154 | 0.8772 |  |
| BMI (kg/m2) | -0.7337 | 0.6264 | ±1.2528 | -1.171 | 0.2415 |  |
| Hypertension | -5.7355 | 7.5880 | ±15.1760 | -0.756 | 0.4497 |  |
| High cholesterol | +3.7588 | 7.1960 | ±14.3919 | +0.522 | 0.6014 |  |
| Kidney disease | -9.6813 | 17.0463 | ±34.0926 | -0.568 | 0.5701 |  |
| Circulatory disease | +6.0095 | 11.2630 | ±22.5260 | +0.534 | 0.5936 |  |
| Avg. daily time in range 70-180 (%) | -0.4403 | 0.6685 | ±1.3370 | -0.659 | 0.5101 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **383**, R² = **0.0332**, Adj R² = **0.0045**, F-statistic = **1.16** (p = **0.3148**), Residual SE = **64.287** on **371** df, AIC = **4287.9**, BIC = **4335.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.1162** | 28.8121 | ±57.6242 | **+13.609** | **3.52e-42** | *** |
| Education: graduate level (vs college) | +3.6449 | 7.1766 | ±14.3532 | +0.508 | 0.6115 |  |
| Education: high school or below (vs college) | -27.3430 | 18.0698 | ±36.1396 | -1.513 | 0.1302 |  |
| Site: UCSD (vs UAB) | +3.7466 | 10.3449 | ±20.6897 | +0.362 | 0.7172 |  |
| Site: UW (vs UAB) | +3.3192 | 7.9202 | ±15.8404 | +0.419 | 0.6752 |  |
| Age (years) | -0.0294 | 0.3247 | ±0.6495 | -0.090 | 0.9279 |  |
| BMI (kg/m2) | -0.7478 | 0.6264 | ±1.2529 | -1.194 | 0.2326 |  |
| Hypertension | -6.0045 | 7.6006 | ±15.2012 | -0.790 | 0.4295 |  |
| High cholesterol | +3.2396 | 7.2564 | ±14.5128 | +0.446 | 0.6553 |  |
| Kidney disease | -7.8677 | 16.7993 | ±33.5986 | -0.468 | 0.6395 |  |
| Circulatory disease | +5.3964 | 11.2706 | ±22.5412 | +0.479 | 0.6321 |  |
| Time < 54 (%) | -2.5274 | 2.2043 | ±4.4086 | -1.147 | 0.2515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **383**, R² = **0.0336**, Adj R² = **0.0049**, F-statistic = **1.17** (p = **0.3048**), Residual SE = **64.275** on **371** df, AIC = **4287.7**, BIC = **4335.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+391.4714** | 28.7678 | ±57.5357 | **+13.608** | **3.59e-42** | *** |
| Education: graduate level (vs college) | +3.5116 | 7.1951 | ±14.3903 | +0.488 | 0.6255 |  |
| Education: high school or below (vs college) | -27.4400 | 18.0623 | ±36.1247 | -1.519 | 0.1287 |  |
| Site: UCSD (vs UAB) | +3.7927 | 10.2883 | ±20.5766 | +0.369 | 0.7124 |  |
| Site: UW (vs UAB) | +3.0511 | 7.9115 | ±15.8230 | +0.386 | 0.6998 |  |
| Age (years) | -0.0176 | 0.3256 | ±0.6511 | -0.054 | 0.9568 |  |
| BMI (kg/m2) | -0.7449 | 0.6249 | ±1.2498 | -1.192 | 0.2333 |  |
| Hypertension | -6.1734 | 7.6300 | ±15.2599 | -0.809 | 0.4185 |  |
| High cholesterol | +3.1696 | 7.2654 | ±14.5307 | +0.436 | 0.6626 |  |
| Kidney disease | -7.8466 | 16.8186 | ±33.6372 | -0.467 | 0.6408 |  |
| Circulatory disease | +5.3158 | 11.2768 | ±22.5537 | +0.471 | 0.6374 |  |
| Avg. daily time < 54 (%) | -3.7494 | 2.8108 | ±5.6217 | -1.334 | 0.1822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **383**, R² = **0.0327**, Adj R² = **0.0040**, F-statistic = **1.14** (p = **0.3281**), Residual SE = **64.304** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.8256** | 28.5050 | ±57.0101 | **+13.606** | **3.71e-42** | *** |
| Education: graduate level (vs college) | +3.8590 | 7.1836 | ±14.3671 | +0.537 | 0.5911 |  |
| Education: high school or below (vs college) | -26.6402 | 18.1100 | ±36.2200 | -1.471 | 0.1413 |  |
| Site: UCSD (vs UAB) | +5.1258 | 10.2853 | ±20.5706 | +0.498 | 0.6182 |  |
| Site: UW (vs UAB) | +4.6389 | 7.8453 | ±15.6906 | +0.591 | 0.5543 |  |
| Age (years) | -0.0302 | 0.3242 | ±0.6484 | -0.093 | 0.9258 |  |
| BMI (kg/m2) | -0.7372 | 0.6301 | ±1.2602 | -1.170 | 0.2420 |  |
| Hypertension | -5.2727 | 7.7239 | ±15.4478 | -0.683 | 0.4948 |  |
| High cholesterol | +3.9968 | 7.2077 | ±14.4154 | +0.555 | 0.5792 |  |
| Kidney disease | -8.2104 | 16.7327 | ±33.4655 | -0.491 | 0.6237 |  |
| Circulatory disease | +5.7539 | 11.2547 | ±22.5094 | +0.511 | 0.6092 |  |
| Time 54-69, pooled (%) | +0.8894 | 1.1929 | ±2.3859 | +0.746 | 0.4559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **383**, R² = **0.0328**, Adj R² = **0.0042**, F-statistic = **1.14** (p = **0.3249**), Residual SE = **64.300** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.1361** | 28.5266 | ±57.0533 | **+13.606** | **3.68e-42** | *** |
| Education: graduate level (vs college) | +3.9120 | 7.1887 | ±14.3774 | +0.544 | 0.5863 |  |
| Education: high school or below (vs college) | -26.5195 | 18.1103 | ±36.2207 | -1.464 | 0.1431 |  |
| Site: UCSD (vs UAB) | +5.0629 | 10.2761 | ±20.5522 | +0.493 | 0.6222 |  |
| Site: UW (vs UAB) | +4.7018 | 7.8370 | ±15.6740 | +0.600 | 0.5485 |  |
| Age (years) | -0.0339 | 0.3242 | ±0.6484 | -0.104 | 0.9168 |  |
| BMI (kg/m2) | -0.7380 | 0.6308 | ±1.2615 | -1.170 | 0.2420 |  |
| Hypertension | -5.2284 | 7.7394 | ±15.4788 | -0.676 | 0.4993 |  |
| High cholesterol | +3.9965 | 7.2029 | ±14.4057 | +0.555 | 0.5790 |  |
| Kidney disease | -8.1649 | 16.7170 | ±33.4339 | -0.488 | 0.6253 |  |
| Circulatory disease | +5.7251 | 11.2582 | ±22.5164 | +0.509 | 0.6111 |  |
| Avg. daily time 54-69 (%) | +0.9231 | 1.1764 | ±2.3529 | +0.785 | 0.4327 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **383**, R² = **0.0320**, Adj R² = **0.0033**, F-statistic = **1.11** (p = **0.3492**), Residual SE = **64.329** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.9791** | 28.5994 | ±57.1987 | **+13.601** | **3.95e-42** | *** |
| Education: graduate level (vs college) | +3.8041 | 7.1858 | ±14.3716 | +0.529 | 0.5965 |  |
| Education: high school or below (vs college) | -26.8942 | 18.0913 | ±36.1827 | -1.487 | 0.1371 |  |
| Site: UCSD (vs UAB) | +4.9209 | 10.3178 | ±20.6356 | +0.477 | 0.6334 |  |
| Site: UW (vs UAB) | +4.3331 | 7.8849 | ±15.7699 | +0.550 | 0.5826 |  |
| Age (years) | -0.0322 | 0.3247 | ±0.6494 | -0.099 | 0.9209 |  |
| BMI (kg/m2) | -0.7317 | 0.6272 | ±1.2543 | -1.167 | 0.2434 |  |
| Hypertension | -5.5001 | 7.7038 | ±15.4075 | -0.714 | 0.4753 |  |
| High cholesterol | +3.8486 | 7.2331 | ±14.4663 | +0.532 | 0.5947 |  |
| Kidney disease | -8.2303 | 16.7752 | ±33.5504 | -0.491 | 0.6237 |  |
| Circulatory disease | +5.6677 | 11.2564 | ±22.5129 | +0.504 | 0.6146 |  |
| Time < 70 (%) | +0.2509 | 0.9208 | ±1.8417 | +0.272 | 0.7853 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **383**, R² = **0.0321**, Adj R² = **0.0034**, F-statistic = **1.12** (p = **0.3462**), Residual SE = **64.325** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.9673** | 28.5984 | ±57.1968 | **+13.601** | **3.95e-42** | *** |
| Education: graduate level (vs college) | +3.8466 | 7.1945 | ±14.3891 | +0.535 | 0.5929 |  |
| Education: high school or below (vs college) | -26.7979 | 18.0989 | ±36.1978 | -1.481 | 0.1387 |  |
| Site: UCSD (vs UAB) | +4.9323 | 10.2898 | ±20.5795 | +0.479 | 0.6317 |  |
| Site: UW (vs UAB) | +4.4360 | 7.8634 | ±15.7267 | +0.564 | 0.5727 |  |
| Age (years) | -0.0345 | 0.3249 | ±0.6498 | -0.106 | 0.9154 |  |
| BMI (kg/m2) | -0.7329 | 0.6283 | ±1.2566 | -1.167 | 0.2434 |  |
| Hypertension | -5.4298 | 7.7328 | ±15.4657 | -0.702 | 0.4826 |  |
| High cholesterol | +3.8819 | 7.2255 | ±14.4510 | +0.537 | 0.5911 |  |
| Kidney disease | -8.2152 | 16.7508 | ±33.5016 | -0.490 | 0.6238 |  |
| Circulatory disease | +5.6791 | 11.2582 | ±22.5165 | +0.504 | 0.6140 |  |
| Avg. daily time < 70 (%) | +0.3573 | 0.9352 | ±1.8705 | +0.382 | 0.7025 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **383**, R² = **0.0323**, Adj R² = **0.0036**, F-statistic = **1.12** (p = **0.3406**), Residual SE = **64.319** on **371** df, AIC = **4288.2**, BIC = **4335.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +279.3739 | 234.4217 | ±468.8434 | +1.192 | 0.2334 |  |
| Education: graduate level (vs college) | +3.7078 | 7.1827 | ±14.3653 | +0.516 | 0.6057 |  |
| Education: high school or below (vs college) | -27.1562 | 18.0677 | ±36.1354 | -1.503 | 0.1328 |  |
| Site: UCSD (vs UAB) | +4.2200 | 10.3811 | ±20.7622 | +0.407 | 0.6844 |  |
| Site: UW (vs UAB) | +3.6835 | 7.9087 | ±15.8174 | +0.466 | 0.6414 |  |
| Age (years) | -0.0260 | 0.3258 | ±0.6516 | -0.080 | 0.9364 |  |
| BMI (kg/m2) | -0.7425 | 0.6269 | ±1.2539 | -1.184 | 0.2363 |  |
| Hypertension | -5.7763 | 7.6063 | ±15.2125 | -0.759 | 0.4476 |  |
| High cholesterol | +3.4633 | 7.2576 | ±14.5152 | +0.477 | 0.6332 |  |
| Kidney disease | -7.4482 | 17.1442 | ±34.2884 | -0.434 | 0.6640 |  |
| Circulatory disease | +5.4231 | 11.3184 | ±22.6367 | +0.479 | 0.6318 |  |
| Time 54-250, pooled (%) | +1.1142 | 2.3424 | ±4.6849 | +0.476 | 0.6343 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **383**, R² = **0.0322**, Adj R² = **0.0035**, F-statistic = **1.12** (p = **0.3422**), Residual SE = **64.321** on **371** df, AIC = **4288.2**, BIC = **4335.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +272.5027 | 302.9185 | ±605.8371 | +0.900 | 0.3683 |  |
| Education: graduate level (vs college) | +3.6726 | 7.1984 | ±14.3968 | +0.510 | 0.6099 |  |
| Education: high school or below (vs college) | -27.1599 | 18.0765 | ±36.1530 | -1.502 | 0.1330 |  |
| Site: UCSD (vs UAB) | +4.3224 | 10.3343 | ±20.6686 | +0.418 | 0.6758 |  |
| Site: UW (vs UAB) | +3.7054 | 7.8868 | ±15.7737 | +0.470 | 0.6385 |  |
| Age (years) | -0.0219 | 0.3269 | ±0.6538 | -0.067 | 0.9466 |  |
| BMI (kg/m2) | -0.7385 | 0.6263 | ±1.2526 | -1.179 | 0.2384 |  |
| Hypertension | -5.7952 | 7.6234 | ±15.2468 | -0.760 | 0.4471 |  |
| High cholesterol | +3.5287 | 7.2638 | ±14.5276 | +0.486 | 0.6271 |  |
| Kidney disease | -7.4007 | 17.2226 | ±34.4453 | -0.430 | 0.6674 |  |
| Circulatory disease | +5.4062 | 11.3266 | ±22.6533 | +0.477 | 0.6331 |  |
| Avg. daily time 54-250 (%) | +1.1772 | 3.0257 | ±6.0514 | +0.389 | 0.6972 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **383**, R² = **0.0328**, Adj R² = **0.0041**, F-statistic = **1.14** (p = **0.3258**), Residual SE = **64.301** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.9213** | 28.8059 | ±57.6118 | **+13.536** | **9.57e-42** | *** |
| Education: graduate level (vs college) | +3.7132 | 7.2187 | ±14.4373 | +0.514 | 0.6070 |  |
| Education: high school or below (vs college) | -27.3026 | 18.0753 | ±36.1506 | -1.510 | 0.1309 |  |
| Site: UCSD (vs UAB) | +4.5630 | 10.2585 | ±20.5170 | +0.445 | 0.6565 |  |
| Site: UW (vs UAB) | +3.9446 | 7.8310 | ±15.6621 | +0.504 | 0.6145 |  |
| Age (years) | -0.0473 | 0.3272 | ±0.6544 | -0.144 | 0.8852 |  |
| BMI (kg/m2) | -0.7308 | 0.6251 | ±1.2502 | -1.169 | 0.2424 |  |
| Hypertension | -5.9942 | 7.6403 | ±15.2807 | -0.785 | 0.4327 |  |
| High cholesterol | +3.5583 | 7.2034 | ±14.4067 | +0.494 | 0.6213 |  |
| Kidney disease | -9.4795 | 17.1610 | ±34.3220 | -0.552 | 0.5807 |  |
| Circulatory disease | +5.8823 | 11.2593 | ±22.5185 | +0.522 | 0.6014 |  |
| Time 181-250, pooled (%) | +0.4809 | 0.9440 | ±1.8880 | +0.509 | 0.6104 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **383**, R² = **0.0329**, Adj R² = **0.0043**, F-statistic = **1.15** (p = **0.3218**), Residual SE = **64.296** on **371** df, AIC = **4288.0**, BIC = **4335.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.0243** | 28.8155 | ±57.6310 | **+13.535** | **9.69e-42** | *** |
| Education: graduate level (vs college) | +3.7015 | 7.2209 | ±14.4418 | +0.513 | 0.6082 |  |
| Education: high school or below (vs college) | -27.2940 | 18.0738 | ±36.1476 | -1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +4.5850 | 10.2536 | ±20.5073 | +0.447 | 0.6548 |  |
| Site: UW (vs UAB) | +3.9352 | 7.8285 | ±15.6570 | +0.503 | 0.6152 |  |
| Age (years) | -0.0476 | 0.3272 | ±0.6544 | -0.146 | 0.8843 |  |
| BMI (kg/m2) | -0.7334 | 0.6250 | ±1.2499 | -1.174 | 0.2406 |  |
| Hypertension | -6.0337 | 7.6458 | ±15.2916 | -0.789 | 0.4300 |  |
| High cholesterol | +3.5347 | 7.1994 | ±14.3987 | +0.491 | 0.6234 |  |
| Kidney disease | -9.5491 | 17.1476 | ±34.2952 | -0.557 | 0.5776 |  |
| Circulatory disease | +5.9120 | 11.2637 | ±22.5275 | +0.525 | 0.5997 |  |
| Avg. daily time 181-250 (%) | +0.4954 | 0.9038 | ±1.8076 | +0.548 | 0.5836 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **383**, R² = **0.0327**, Adj R² = **0.0040**, F-statistic = **1.14** (p = **0.3278**), Residual SE = **64.303** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.8974** | 28.8106 | ±57.6212 | **+13.533** | **9.97e-42** | *** |
| Education: graduate level (vs college) | +3.7227 | 7.2192 | ±14.4383 | +0.516 | 0.6061 |  |
| Education: high school or below (vs college) | -27.2689 | 18.0855 | ±36.1710 | -1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | +4.6079 | 10.2515 | ±20.5031 | +0.449 | 0.6531 |  |
| Site: UW (vs UAB) | +3.9957 | 7.8245 | ±15.6490 | +0.511 | 0.6096 |  |
| Age (years) | -0.0470 | 0.3275 | ±0.6550 | -0.144 | 0.8859 |  |
| BMI (kg/m2) | -0.7296 | 0.6252 | ±1.2504 | -1.167 | 0.2432 |  |
| Hypertension | -5.9509 | 7.6361 | ±15.2722 | -0.779 | 0.4358 |  |
| High cholesterol | +3.5999 | 7.2051 | ±14.4102 | +0.500 | 0.6173 |  |
| Kidney disease | -9.5109 | 17.2064 | ±34.4127 | -0.553 | 0.5804 |  |
| Circulatory disease | +5.8745 | 11.2599 | ±22.5198 | +0.522 | 0.6019 |  |
| Time > 180 (%) | +0.4100 | 0.8520 | ±1.7040 | +0.481 | 0.6304 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **383**, R² = **0.0328**, Adj R² = **0.0042**, F-statistic = **1.14** (p = **0.3248**), Residual SE = **64.300** on **371** df, AIC = **4288.0**, BIC = **4335.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.0079** | 28.8233 | ±57.6467 | **+13.531** | **1.03e-41** | *** |
| Education: graduate level (vs college) | +3.7166 | 7.2204 | ±14.4407 | +0.515 | 0.6067 |  |
| Education: high school or below (vs college) | -27.2533 | 18.0838 | ±36.1676 | -1.507 | 0.1318 |  |
| Site: UCSD (vs UAB) | +4.6394 | 10.2463 | ±20.4927 | +0.453 | 0.6507 |  |
| Site: UW (vs UAB) | +3.9868 | 7.8227 | ±15.6454 | +0.510 | 0.6103 |  |
| Age (years) | -0.0473 | 0.3275 | ±0.6549 | -0.144 | 0.8852 |  |
| BMI (kg/m2) | -0.7322 | 0.6251 | ±1.2503 | -1.171 | 0.2415 |  |
| Hypertension | -5.9739 | 7.6392 | ±15.2785 | -0.782 | 0.4342 |  |
| High cholesterol | +3.5728 | 7.2023 | ±14.4045 | +0.496 | 0.6198 |  |
| Kidney disease | -9.5693 | 17.2045 | ±34.4089 | -0.556 | 0.5781 |  |
| Circulatory disease | +5.9001 | 11.2640 | ±22.5280 | +0.524 | 0.6004 |  |
| Avg. daily time > 180 (%) | +0.4148 | 0.8119 | ±1.6237 | +0.511 | 0.6094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **383**, R² = **0.0324**, Adj R² = **0.0037**, F-statistic = **1.13** (p = **0.3366**), Residual SE = **64.314** on **371** df, AIC = **4288.2**, BIC = **4335.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.0995** | 28.9009 | ±57.8017 | **+13.498** | **1.61e-41** | *** |
| Education: graduate level (vs college) | +3.9367 | 7.1529 | ±14.3058 | +0.550 | 0.5821 |  |
| Education: high school or below (vs college) | -27.2578 | 18.2256 | ±36.4512 | -1.496 | 0.1348 |  |
| Site: UCSD (vs UAB) | +4.8251 | 10.2455 | ±20.4910 | +0.471 | 0.6377 |  |
| Site: UW (vs UAB) | +4.0988 | 7.8388 | ±15.6777 | +0.523 | 0.6011 |  |
| Age (years) | -0.0402 | 0.3262 | ±0.6524 | -0.123 | 0.9020 |  |
| BMI (kg/m2) | -0.7428 | 0.6279 | ±1.2558 | -1.183 | 0.2368 |  |
| Hypertension | -5.8912 | 7.6672 | ±15.3344 | -0.768 | 0.4423 |  |
| High cholesterol | +3.7012 | 7.2167 | ±14.4333 | +0.513 | 0.6080 |  |
| Kidney disease | -8.2946 | 16.7547 | ±33.5093 | -0.495 | 0.6206 |  |
| Circulatory disease | +6.0039 | 11.2342 | ±22.4685 | +0.534 | 0.5930 |  |
| Nocturnal time > 180 (%) | +0.3387 | 1.1309 | ±2.2619 | +0.299 | 0.7646 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **383**, R² = **0.0387**, Adj R² = **0.0102**, F-statistic = **1.36** (p = **0.1905**), Residual SE = **64.104** on **371** df, AIC = **4285.7**, BIC = **4333.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.4636** | 28.8412 | ±57.6823 | **+13.469** | **2.38e-41** | *** |
| Education: graduate level (vs college) | +4.2573 | 7.1516 | ±14.3033 | +0.595 | 0.5516 |  |
| Education: high school or below (vs college) | -27.1789 | 18.1075 | ±36.2150 | -1.501 | 0.1334 |  |
| Site: UCSD (vs UAB) | +3.5161 | 10.3755 | ±20.7510 | +0.339 | 0.7347 |  |
| Site: UW (vs UAB) | +4.1109 | 7.8018 | ±15.6037 | +0.527 | 0.5983 |  |
| Age (years) | -0.0697 | 0.3298 | ±0.6596 | -0.211 | 0.8327 |  |
| BMI (kg/m2) | -0.6842 | 0.6284 | ±1.2568 | -1.089 | 0.2763 |  |
| Hypertension | -6.4725 | 7.5700 | ±15.1400 | -0.855 | 0.3925 |  |
| High cholesterol | +3.6863 | 7.1674 | ±14.3347 | +0.514 | 0.6070 |  |
| Kidney disease | -9.5005 | 16.4249 | ±32.8498 | -0.578 | 0.5630 |  |
| Circulatory disease | +6.4528 | 11.2543 | ±22.5086 | +0.573 | 0.5664 |  |
| Any reading > 250 during wear (0/1) | +14.7217 | 10.0037 | ±20.0075 | +1.472 | 0.1411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **383**, R² = **0.0321**, Adj R² = **0.0034**, F-statistic = **1.12** (p = **0.3449**), Residual SE = **64.324** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.7587** | 28.8184 | ±57.6368 | **+13.525** | **1.12e-41** | *** |
| Education: graduate level (vs college) | +3.7725 | 7.2113 | ±14.4226 | +0.523 | 0.6009 |  |
| Education: high school or below (vs college) | -27.0580 | 18.1170 | ±36.2339 | -1.494 | 0.1353 |  |
| Site: UCSD (vs UAB) | +4.7979 | 10.2734 | ±20.5468 | +0.467 | 0.6405 |  |
| Site: UW (vs UAB) | +4.2100 | 7.8385 | ±15.6770 | +0.537 | 0.5912 |  |
| Age (years) | -0.0399 | 0.3276 | ±0.6552 | -0.122 | 0.9030 |  |
| BMI (kg/m2) | -0.7265 | 0.6259 | ±1.2519 | -1.161 | 0.2458 |  |
| Hypertension | -5.6743 | 7.6018 | ±15.2036 | -0.746 | 0.4554 |  |
| High cholesterol | +3.7897 | 7.2087 | ±14.4173 | +0.526 | 0.5991 |  |
| Kidney disease | -9.0422 | 17.3096 | ±34.6192 | -0.522 | 0.6014 |  |
| Circulatory disease | +5.7321 | 11.2818 | ±22.5637 | +0.508 | 0.6114 |  |
| Time > 250 (%) | +1.5730 | 6.3964 | ±12.7928 | +0.246 | 0.8057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 383)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **383**, R² = **0.0321**, Adj R² = **0.0034**, F-statistic = **1.12** (p = **0.3463**), Residual SE = **64.325** on **371** df, AIC = **4288.3**, BIC = **4335.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.8437** | 28.8494 | ±57.6988 | **+13.513** | **1.31e-41** | *** |
| Education: graduate level (vs college) | +3.7807 | 7.2119 | ±14.4238 | +0.524 | 0.6001 |  |
| Education: high school or below (vs college) | -27.0400 | 18.1107 | ±36.2213 | -1.493 | 0.1354 |  |
| Site: UCSD (vs UAB) | +4.8170 | 10.2700 | ±20.5401 | +0.469 | 0.6390 |  |
| Site: UW (vs UAB) | +4.1808 | 7.8324 | ±15.6649 | +0.534 | 0.5935 |  |
| Age (years) | -0.0393 | 0.3275 | ±0.6551 | -0.120 | 0.9045 |  |
| BMI (kg/m2) | -0.7288 | 0.6262 | ±1.2523 | -1.164 | 0.2445 |  |
| Hypertension | -5.6536 | 7.5992 | ±15.1984 | -0.744 | 0.4569 |  |
| High cholesterol | +3.7469 | 7.2119 | ±14.4237 | +0.520 | 0.6034 |  |
| Kidney disease | -8.9571 | 17.3430 | ±34.6860 | -0.516 | 0.6055 |  |
| Circulatory disease | +5.7258 | 11.2751 | ±22.5503 | +0.508 | 0.6116 |  |
| Avg. daily time > 250 (%) | +1.3156 | 6.0840 | ±12.1681 | +0.216 | 0.8288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 374; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **374**, R² = **0.1088**, Adj R² = **0.0843**, F-statistic = **4.43** (p = **6.69e-06**), Residual SE = **16.423** on **363** df, AIC = **3165.6**, BIC = **3208.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6521** | 7.3802 | ±14.7605 | **+9.302** | **1.38e-20** | *** |
| Education: graduate level (vs college) | -2.0457 | 1.8567 | ±3.7133 | -1.102 | 0.2705 |  |
| Education: high school or below (vs college) | +0.3959 | 4.3309 | ±8.6618 | +0.091 | 0.9272 |  |
| Site: UCSD (vs UAB) | +0.5381 | 2.5692 | ±5.1384 | +0.209 | 0.8341 |  |
| **Site: UW (vs UAB)** | **-4.0032** | 2.0001 | ±4.0002 | **-2.001** | **0.0453** | * |
| **Age (years)** | **-0.4004** | 0.0851 | ±0.1702 | **-4.704** | **2.55e-06** | *** |
| BMI (kg/m2) | +0.2411 | 0.1458 | ±0.2915 | +1.654 | 0.0982 | . |
| Hypertension | -1.1499 | 1.9739 | ±3.9479 | -0.583 | 0.5602 |  |
| High cholesterol | +1.0254 | 1.9188 | ±3.8376 | +0.534 | 0.5931 |  |
| Kidney disease | -2.2992 | 4.3954 | ±8.7908 | -0.523 | 0.6009 |  |
| Circulatory disease | +0.1622 | 2.5627 | ±5.1254 | +0.063 | 0.9495 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **374**, R² = **0.1131**, Adj R² = **0.0862**, F-statistic = **4.20** (p = **7.30e-06**), Residual SE = **16.406** on **362** df, AIC = **3165.8**, BIC = **3212.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2192** | 11.7568 | ±23.5137 | **+4.697** | **2.64e-06** | *** |
| Education: graduate level (vs college) | -1.8976 | 1.8582 | ±3.7165 | -1.021 | 0.3072 |  |
| Education: high school or below (vs college) | +0.1057 | 4.3162 | ±8.6324 | +0.024 | 0.9805 |  |
| Site: UCSD (vs UAB) | +0.0557 | 2.5904 | ±5.1807 | +0.022 | 0.9828 |  |
| **Site: UW (vs UAB)** | **-4.0946** | 1.9910 | ±3.9821 | **-2.057** | **0.0397** | * |
| **Age (years)** | **-0.4183** | 0.0863 | ±0.1727 | **-4.844** | **1.27e-06** | *** |
| BMI (kg/m2) | +0.2197 | 0.1454 | ±0.2908 | +1.511 | 0.1307 |  |
| Hypertension | -1.1019 | 1.9777 | ±3.9553 | -0.557 | 0.5774 |  |
| High cholesterol | +0.6231 | 1.8951 | ±3.7903 | +0.329 | 0.7423 |  |
| Kidney disease | -2.4626 | 4.3415 | ±8.6830 | -0.567 | 0.5706 |  |
| Circulatory disease | +0.3438 | 2.5443 | ±5.0887 | +0.135 | 0.8925 |  |
| HbA1c (%) | +2.7252 | 1.8568 | ±3.7137 | +1.468 | 0.1422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **374**, R² = **0.1093**, Adj R² = **0.0822**, F-statistic = **4.04** (p = **1.37e-05**), Residual SE = **16.441** on **362** df, AIC = **3167.4**, BIC = **3214.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.8823** | 9.2474 | ±18.4948 | **+7.124** | **1.05e-12** | *** |
| Education: graduate level (vs college) | -2.0895 | 1.8596 | ±3.7191 | -1.124 | 0.2612 |  |
| Education: high school or below (vs college) | +0.3129 | 4.3654 | ±8.7308 | +0.072 | 0.9429 |  |
| Site: UCSD (vs UAB) | +0.4867 | 2.5839 | ±5.1678 | +0.188 | 0.8506 |  |
| **Site: UW (vs UAB)** | **-4.1022** | 2.0359 | ±4.0718 | **-2.015** | **0.0439** | * |
| **Age (years)** | **-0.4021** | 0.0861 | ±0.1722 | **-4.671** | **3.00e-06** | *** |
| BMI (kg/m2) | +0.2381 | 0.1467 | ±0.2935 | +1.623 | 0.1047 |  |
| Hypertension | -1.2249 | 1.9737 | ±3.9475 | -0.621 | 0.5349 |  |
| High cholesterol | +0.9342 | 1.9075 | ±3.8150 | +0.490 | 0.6243 |  |
| Kidney disease | -2.4878 | 4.4047 | ±8.8093 | -0.565 | 0.5722 |  |
| Circulatory disease | +0.1692 | 2.5710 | ±5.1420 | +0.066 | 0.9475 |  |
| Mean glucose (mg/dL) | +0.0272 | 0.0637 | ±0.1275 | +0.427 | 0.6692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **374**, R² = **0.1093**, Adj R² = **0.0822**, F-statistic = **4.04** (p = **1.37e-05**), Residual SE = **16.441** on **362** df, AIC = **3167.4**, BIC = **3214.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.1140** | 16.1981 | ±32.3963 | **+3.835** | **1.26e-04** | *** |
| Education: graduate level (vs college) | -2.0895 | 1.8596 | ±3.7191 | -1.124 | 0.2612 |  |
| Education: high school or below (vs college) | +0.3129 | 4.3654 | ±8.7308 | +0.072 | 0.9429 |  |
| Site: UCSD (vs UAB) | +0.4867 | 2.5839 | ±5.1678 | +0.188 | 0.8506 |  |
| **Site: UW (vs UAB)** | **-4.1022** | 2.0359 | ±4.0718 | **-2.015** | **0.0439** | * |
| **Age (years)** | **-0.4021** | 0.0861 | ±0.1722 | **-4.671** | **3.00e-06** | *** |
| BMI (kg/m2) | +0.2381 | 0.1467 | ±0.2935 | +1.623 | 0.1047 |  |
| Hypertension | -1.2249 | 1.9737 | ±3.9475 | -0.621 | 0.5349 |  |
| High cholesterol | +0.9342 | 1.9075 | ±3.8150 | +0.490 | 0.6243 |  |
| Kidney disease | -2.4878 | 4.4047 | ±8.8093 | -0.565 | 0.5722 |  |
| Circulatory disease | +0.1692 | 2.5710 | ±5.1420 | +0.066 | 0.9475 |  |
| GMI (%) | +1.1385 | 2.6647 | ±5.3293 | +0.427 | 0.6692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **374**, R² = **0.1088**, Adj R² = **0.0818**, F-statistic = **4.02** (p = **1.48e-05**), Residual SE = **16.446** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.0598** | 9.1774 | ±18.3549 | **+7.525** | **5.27e-14** | *** |
| Education: graduate level (vs college) | -2.0433 | 1.8618 | ±3.7236 | -1.097 | 0.2724 |  |
| Education: high school or below (vs college) | +0.4107 | 4.3248 | ±8.6495 | +0.095 | 0.9243 |  |
| Site: UCSD (vs UAB) | +0.5478 | 2.5732 | ±5.1465 | +0.213 | 0.8314 |  |
| **Site: UW (vs UAB)** | **-3.9906** | 2.0213 | ±4.0425 | **-1.974** | **0.0483** | * |
| **Age (years)** | **-0.4005** | 0.0851 | ±0.1703 | **-4.704** | **2.55e-06** | *** |
| BMI (kg/m2) | +0.2423 | 0.1489 | ±0.2977 | +1.627 | 0.1036 |  |
| Hypertension | -1.1380 | 1.9757 | ±3.9514 | -0.576 | 0.5646 |  |
| High cholesterol | +1.0429 | 1.9116 | ±3.8232 | +0.546 | 0.5854 |  |
| Kidney disease | -2.2908 | 4.4198 | ±8.8396 | -0.518 | 0.6042 |  |
| Circulatory disease | +0.1555 | 2.5706 | ±5.1411 | +0.061 | 0.9518 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0040 | 0.0610 | ±0.1220 | -0.066 | 0.9474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1135**, Adj R² = **0.0865**, F-statistic = **4.21** (p = **6.86e-06**), Residual SE = **16.403** on **362** df, AIC = **3165.7**, BIC = **3212.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.3763** | 7.6389 | ±15.2778 | **+8.558** | **1.15e-17** | *** |
| Education: graduate level (vs college) | -2.1479 | 1.8569 | ±3.7138 | -1.157 | 0.2474 |  |
| Education: high school or below (vs college) | +0.3183 | 4.3721 | ±8.7442 | +0.073 | 0.9420 |  |
| Site: UCSD (vs UAB) | +0.3737 | 2.5775 | ±5.1549 | +0.145 | 0.8847 |  |
| **Site: UW (vs UAB)** | **-4.0556** | 2.0132 | ±4.0264 | **-2.014** | **0.0440** | * |
| **Age (years)** | **-0.4141** | 0.0859 | ±0.1717 | **-4.823** | **1.42e-06** | *** |
| BMI (kg/m2) | +0.2438 | 0.1463 | ±0.2926 | +1.667 | 0.0956 | . |
| Hypertension | -1.2793 | 1.9743 | ±3.9486 | -0.648 | 0.5170 |  |
| High cholesterol | +1.0524 | 1.9206 | ±3.8413 | +0.548 | 0.5837 |  |
| Kidney disease | -3.1862 | 4.5099 | ±9.0198 | -0.707 | 0.4799 |  |
| Circulatory disease | +0.2143 | 2.5615 | ±5.1229 | +0.084 | 0.9333 |  |
| Glucose SD, pooled (mg/dL) | +0.1916 | 0.1401 | ±0.2801 | +1.368 | 0.1713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1123**, Adj R² = **0.0854**, F-statistic = **4.16** (p = **8.32e-06**), Residual SE = **16.414** on **362** df, AIC = **3166.2**, BIC = **3213.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1938** | 7.5652 | ±15.1305 | **+8.750** | **2.14e-18** | *** |
| Education: graduate level (vs college) | -2.1017 | 1.8551 | ±3.7103 | -1.133 | 0.2572 |  |
| Education: high school or below (vs college) | +0.2776 | 4.3691 | ±8.7383 | +0.064 | 0.9493 |  |
| Site: UCSD (vs UAB) | +0.3232 | 2.5834 | ±5.1667 | +0.125 | 0.9004 |  |
| **Site: UW (vs UAB)** | **-4.0827** | 2.0171 | ±4.0342 | **-2.024** | **0.0430** | * |
| **Age (years)** | **-0.4149** | 0.0862 | ±0.1725 | **-4.811** | **1.50e-06** | *** |
| BMI (kg/m2) | +0.2407 | 0.1457 | ±0.2915 | +1.652 | 0.0986 | . |
| Hypertension | -1.2584 | 1.9777 | ±3.9555 | -0.636 | 0.5246 |  |
| High cholesterol | +1.0381 | 1.9221 | ±3.8443 | +0.540 | 0.5891 |  |
| Kidney disease | -3.0694 | 4.5223 | ±9.0446 | -0.679 | 0.4973 |  |
| Circulatory disease | +0.2317 | 2.5627 | ±5.1254 | +0.090 | 0.9280 |  |
| Avg. daily SD (mg/dL) | +0.1786 | 0.1522 | ±0.3045 | +1.173 | 0.2408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **374**, R² = **0.1138**, Adj R² = **0.0869**, F-statistic = **4.23** (p = **6.48e-06**), Residual SE = **16.400** on **362** df, AIC = **3165.5**, BIC = **3212.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9529** | 8.1690 | ±16.3380 | **+7.829** | **4.93e-15** | *** |
| Education: graduate level (vs college) | -2.0934 | 1.8590 | ±3.7180 | -1.126 | 0.2601 |  |
| Education: high school or below (vs college) | +0.4438 | 4.3305 | ±8.6611 | +0.102 | 0.9184 |  |
| Site: UCSD (vs UAB) | +0.4174 | 2.5724 | ±5.1447 | +0.162 | 0.8711 |  |
| Site: UW (vs UAB) | -3.8851 | 2.0004 | ±4.0007 | -1.942 | 0.0521 | . |
| **Age (years)** | **-0.4142** | 0.0852 | ±0.1704 | **-4.863** | **1.15e-06** | *** |
| BMI (kg/m2) | +0.2487 | 0.1469 | ±0.2937 | +1.693 | 0.0904 | . |
| Hypertension | -1.1817 | 1.9795 | ±3.9589 | -0.597 | 0.5505 |  |
| High cholesterol | +1.2186 | 1.9161 | ±3.8323 | +0.636 | 0.5248 |  |
| Kidney disease | -3.0408 | 4.5464 | ±9.0928 | -0.669 | 0.5036 |  |
| Circulatory disease | +0.2241 | 2.5570 | ±5.1139 | +0.088 | 0.9302 |  |
| CV (%) | +0.2753 | 0.2156 | ±0.4311 | +1.277 | 0.2016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **374**, R² = **0.1185**, Adj R² = **0.0917**, F-statistic = **4.42** (p = **2.97e-06**), Residual SE = **16.357** on **362** df, AIC = **3163.6**, BIC = **3210.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.4168** | 8.9442 | ±17.8883 | **+8.767** | **1.83e-18** | *** |
| Education: graduate level (vs college) | -2.2608 | 1.8647 | ±3.7293 | -1.212 | 0.2253 |  |
| Education: high school or below (vs college) | +0.3072 | 4.3304 | ±8.6607 | +0.071 | 0.9435 |  |
| Site: UCSD (vs UAB) | +0.3626 | 2.5555 | ±5.1110 | +0.142 | 0.8872 |  |
| **Site: UW (vs UAB)** | **-3.9839** | 2.0046 | ±4.0091 | **-1.987** | **0.0469** | * |
| **Age (years)** | **-0.4217** | 0.0847 | ±0.1694 | **-4.980** | **6.37e-07** | *** |
| BMI (kg/m2) | +0.2439 | 0.1465 | ±0.2930 | +1.665 | 0.0960 | . |
| Hypertension | -1.2133 | 1.9750 | ±3.9500 | -0.614 | 0.5390 |  |
| High cholesterol | +1.1848 | 1.9114 | ±3.8227 | +0.620 | 0.5353 |  |
| Kidney disease | -3.1537 | 4.5023 | ±9.0046 | -0.700 | 0.4836 |  |
| Circulatory disease | +0.2372 | 2.5497 | ±5.0994 | +0.093 | 0.9259 |  |
| Mean / SD ratio | -1.5415 | 0.7889 | ±1.5778 | -1.954 | 0.0507 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **374**, R² = **0.1162**, Adj R² = **0.0894**, F-statistic = **4.33** (p = **4.32e-06**), Residual SE = **16.377** on **362** df, AIC = **3164.5**, BIC = **3211.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.2036** | 8.8671 | ±17.7343 | **+8.707** | **3.13e-18** | *** |
| Education: graduate level (vs college) | -2.2298 | 1.8618 | ±3.7235 | -1.198 | 0.2310 |  |
| Education: high school or below (vs college) | +0.1385 | 4.3420 | ±8.6841 | +0.032 | 0.9746 |  |
| Site: UCSD (vs UAB) | +0.2288 | 2.5625 | ±5.1250 | +0.089 | 0.9289 |  |
| **Site: UW (vs UAB)** | **-4.0412** | 2.0099 | ±4.0198 | **-2.011** | **0.0444** | * |
| **Age (years)** | **-0.4229** | 0.0852 | ±0.1704 | **-4.964** | **6.92e-07** | *** |
| BMI (kg/m2) | +0.2371 | 0.1454 | ±0.2907 | +1.631 | 0.1028 |  |
| Hypertension | -1.1612 | 1.9841 | ±3.9683 | -0.585 | 0.5584 |  |
| High cholesterol | +1.1275 | 1.9173 | ±3.8346 | +0.588 | 0.5565 |  |
| Kidney disease | -3.1632 | 4.4977 | ±8.9953 | -0.703 | 0.4819 |  |
| Circulatory disease | +0.2733 | 2.5544 | ±5.1088 | +0.107 | 0.9148 |  |
| Avg. daily mean/SD | -1.0807 | 0.6299 | ±1.2597 | -1.716 | 0.0862 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **374**, R² = **0.1139**, Adj R² = **0.0870**, F-statistic = **4.23** (p = **6.36e-06**), Residual SE = **16.399** on **362** df, AIC = **3165.5**, BIC = **3212.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6747** | 8.4417 | ±16.8835 | **+7.306** | **2.75e-13** | *** |
| Education: graduate level (vs college) | -2.0393 | 1.8498 | ±3.6996 | -1.102 | 0.2703 |  |
| Education: high school or below (vs college) | +0.5882 | 4.3422 | ±8.6844 | +0.135 | 0.8923 |  |
| Site: UCSD (vs UAB) | +0.3568 | 2.5637 | ±5.1275 | +0.139 | 0.8893 |  |
| Site: UW (vs UAB) | -3.7151 | 2.0116 | ±4.0232 | -1.847 | 0.0648 | . |
| **Age (years)** | **-0.3942** | 0.0844 | ±0.1689 | **-4.669** | **3.03e-06** | *** |
| BMI (kg/m2) | +0.2486 | 0.1459 | ±0.2917 | +1.704 | 0.0884 | . |
| Hypertension | -1.2934 | 1.9821 | ±3.9643 | -0.653 | 0.5141 |  |
| High cholesterol | +1.2845 | 1.9291 | ±3.8581 | +0.666 | 0.5055 |  |
| Kidney disease | -2.3888 | 4.3633 | ±8.7267 | -0.547 | 0.5841 |  |
| Circulatory disease | +0.1942 | 2.5647 | ±5.1293 | +0.076 | 0.9397 |  |
| MAG (mg/dL/h) | +0.1572 | 0.1126 | ±0.2251 | +1.396 | 0.1626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **374**, R² = **0.1122**, Adj R² = **0.0852**, F-statistic = **4.16** (p = **8.56e-06**), Residual SE = **16.415** on **362** df, AIC = **3166.2**, BIC = **3213.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.2256** | 7.7928 | ±15.5856 | **+8.370** | **5.76e-17** | *** |
| Education: graduate level (vs college) | -2.0537 | 1.8517 | ±3.7034 | -1.109 | 0.2674 |  |
| Education: high school or below (vs college) | +0.3097 | 4.3727 | ±8.7455 | +0.071 | 0.9435 |  |
| Site: UCSD (vs UAB) | +0.3472 | 2.5807 | ±5.1615 | +0.135 | 0.8930 |  |
| **Site: UW (vs UAB)** | **-4.0231** | 2.0118 | ±4.0237 | **-2.000** | **0.0455** | * |
| **Age (years)** | **-0.4123** | 0.0864 | ±0.1728 | **-4.772** | **1.82e-06** | *** |
| BMI (kg/m2) | +0.2533 | 0.1463 | ±0.2927 | +1.731 | 0.0834 | . |
| Hypertension | -1.2345 | 1.9785 | ±3.9570 | -0.624 | 0.5327 |  |
| High cholesterol | +1.1042 | 1.9249 | ±3.8498 | +0.574 | 0.5662 |  |
| Kidney disease | -2.8326 | 4.4861 | ±8.9722 | -0.631 | 0.5278 |  |
| Circulatory disease | +0.2126 | 2.5620 | ±5.1240 | +0.083 | 0.9339 |  |
| Avg. daily range (mg/dL) | +0.0384 | 0.0341 | ±0.0682 | +1.127 | 0.2596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **374**, R² = **0.1149**, Adj R² = **0.0880**, F-statistic = **4.27** (p = **5.40e-06**), Residual SE = **16.390** on **362** df, AIC = **3165.1**, BIC = **3212.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0756** | 7.6104 | ±15.2209 | **+8.682** | **3.88e-18** | *** |
| Education: graduate level (vs college) | -2.2516 | 1.8690 | ±3.7380 | -1.205 | 0.2283 |  |
| Education: high school or below (vs college) | +0.6432 | 4.3204 | ±8.6408 | +0.149 | 0.8817 |  |
| Site: UCSD (vs UAB) | +0.8036 | 2.5356 | ±5.0712 | +0.317 | 0.7513 |  |
| **Site: UW (vs UAB)** | **-3.9831** | 2.0039 | ±4.0078 | **-1.988** | **0.0468** | * |
| **Age (years)** | **-0.3993** | 0.0850 | ±0.1700 | **-4.698** | **2.63e-06** | *** |
| BMI (kg/m2) | +0.2358 | 0.1488 | ±0.2977 | +1.585 | 0.1131 |  |
| Hypertension | -1.1801 | 1.9629 | ±3.9259 | -0.601 | 0.5477 |  |
| High cholesterol | +0.9184 | 1.9182 | ±3.8365 | +0.479 | 0.6321 |  |
| Kidney disease | -2.6029 | 4.3838 | ±8.7676 | -0.594 | 0.5527 |  |
| Circulatory disease | +0.1156 | 2.5567 | ±5.1134 | +0.045 | 0.9639 |  |
| SD of daily means (mg/dL) | +0.3806 | 0.2592 | ±0.5185 | +1.468 | 0.1421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **374**, R² = **0.1088**, Adj R² = **0.0818**, F-statistic = **4.02** (p = **1.48e-05**), Residual SE = **16.446** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.6703** | 19.0916 | ±38.1831 | **+3.649** | **2.63e-04** | *** |
| Education: graduate level (vs college) | -2.0448 | 1.8628 | ±3.7256 | -1.098 | 0.2723 |  |
| Education: high school or below (vs college) | +0.3958 | 4.3488 | ±8.6975 | +0.091 | 0.9275 |  |
| Site: UCSD (vs UAB) | +0.5435 | 2.5752 | ±5.1505 | +0.211 | 0.8329 |  |
| **Site: UW (vs UAB)** | **-3.9963** | 1.9945 | ±3.9889 | **-2.004** | **0.0451** | * |
| **Age (years)** | **-0.4007** | 0.0857 | ±0.1715 | **-4.673** | **2.97e-06** | *** |
| BMI (kg/m2) | +0.2411 | 0.1460 | ±0.2920 | +1.651 | 0.0987 | . |
| Hypertension | -1.1510 | 1.9768 | ±3.9535 | -0.582 | 0.5604 |  |
| High cholesterol | +1.0277 | 1.9262 | ±3.8524 | +0.534 | 0.5937 |  |
| Kidney disease | -2.3394 | 4.4596 | ±8.9191 | -0.525 | 0.5999 |  |
| Circulatory disease | +0.1730 | 2.5746 | ±5.1492 | +0.067 | 0.9464 |  |
| Time in range 70-180, pooled (%) | -0.0105 | 0.1783 | ±0.3566 | -0.059 | 0.9531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **374**, R² = **0.1088**, Adj R² = **0.0818**, F-statistic = **4.02** (p = **1.48e-05**), Residual SE = **16.446** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.7789** | 18.9301 | ±37.8601 | **+3.580** | **3.43e-04** | *** |
| Education: graduate level (vs college) | -2.0470 | 1.8638 | ±3.7276 | -1.098 | 0.2721 |  |
| Education: high school or below (vs college) | +0.3947 | 4.3446 | ±8.6893 | +0.091 | 0.9276 |  |
| Site: UCSD (vs UAB) | +0.5348 | 2.5742 | ±5.1484 | +0.208 | 0.8354 |  |
| **Site: UW (vs UAB)** | **-4.0089** | 1.9933 | ±3.9867 | **-2.011** | **0.0443** | * |
| **Age (years)** | **-0.4000** | 0.0859 | ±0.1717 | **-4.658** | **3.19e-06** | *** |
| BMI (kg/m2) | +0.2411 | 0.1461 | ±0.2921 | +1.651 | 0.0988 | . |
| Hypertension | -1.1486 | 1.9763 | ±3.9526 | -0.581 | 0.5611 |  |
| High cholesterol | +1.0244 | 1.9245 | ±3.8489 | +0.532 | 0.5945 |  |
| Kidney disease | -2.2654 | 4.4619 | ±8.9239 | -0.508 | 0.6117 |  |
| Circulatory disease | +0.1529 | 2.5728 | ±5.1456 | +0.059 | 0.9526 |  |
| Avg. daily time in range 70-180 (%) | +0.0089 | 0.1738 | ±0.3476 | +0.051 | 0.9592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **374**, R² = **0.1091**, Adj R² = **0.0820**, F-statistic = **4.03** (p = **1.42e-05**), Residual SE = **16.443** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.9216** | 7.4446 | ±14.8892 | **+9.258** | **2.08e-20** | *** |
| Education: graduate level (vs college) | -2.0602 | 1.8570 | ±3.7139 | -1.109 | 0.2672 |  |
| Education: high school or below (vs college) | +0.3645 | 4.3374 | ±8.6748 | +0.084 | 0.9330 |  |
| Site: UCSD (vs UAB) | +0.4260 | 2.5857 | ±5.1714 | +0.165 | 0.8691 |  |
| **Site: UW (vs UAB)** | **-4.0943** | 2.0113 | ±4.0227 | **-2.036** | **0.0418** | * |
| **Age (years)** | **-0.3999** | 0.0852 | ±0.1704 | **-4.694** | **2.68e-06** | *** |
| BMI (kg/m2) | +0.2393 | 0.1464 | ±0.2927 | +1.635 | 0.1021 |  |
| Hypertension | -1.1936 | 1.9819 | ±3.9639 | -0.602 | 0.5470 |  |
| High cholesterol | +0.9661 | 1.9170 | ±3.8340 | +0.504 | 0.6143 |  |
| Kidney disease | -2.2523 | 4.4235 | ±8.8469 | -0.509 | 0.6106 |  |
| Circulatory disease | +0.1286 | 2.5630 | ±5.1261 | +0.050 | 0.9600 |  |
| Time < 54 (%) | -0.2930 | 0.8954 | ±1.7908 | -0.327 | 0.7435 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **374**, R² = **0.1096**, Adj R² = **0.0825**, F-statistic = **4.05** (p = **1.32e-05**), Residual SE = **16.439** on **362** df, AIC = **3167.3**, BIC = **3214.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.9353** | 7.4024 | ±14.8048 | **+9.313** | **1.25e-20** | *** |
| Education: graduate level (vs college) | -2.0896 | 1.8549 | ±3.7097 | -1.127 | 0.2599 |  |
| Education: high school or below (vs college) | +0.3355 | 4.3513 | ±8.7025 | +0.077 | 0.9385 |  |
| Site: UCSD (vs UAB) | +0.3756 | 2.5764 | ±5.1527 | +0.146 | 0.8841 |  |
| **Site: UW (vs UAB)** | **-4.1842** | 2.0136 | ±4.0273 | **-2.078** | **0.0377** | * |
| **Age (years)** | **-0.3976** | 0.0854 | ±0.1709 | **-4.654** | **3.25e-06** | *** |
| BMI (kg/m2) | +0.2390 | 0.1462 | ±0.2925 | +1.634 | 0.1022 |  |
| Hypertension | -1.2428 | 1.9900 | ±3.9800 | -0.625 | 0.5323 |  |
| High cholesterol | +0.9230 | 1.9182 | ±3.8364 | +0.481 | 0.6304 |  |
| Kidney disease | -2.2258 | 4.4195 | ±8.8391 | -0.504 | 0.6145 |  |
| Circulatory disease | +0.0930 | 2.5636 | ±5.1273 | +0.036 | 0.9711 |  |
| Avg. daily time < 54 (%) | -0.6414 | 1.2839 | ±2.5677 | -0.500 | 0.6174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **374**, R² = **0.1089**, Adj R² = **0.0819**, F-statistic = **4.02** (p = **1.45e-05**), Residual SE = **16.445** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.8392** | 7.4992 | ±14.9984 | **+9.180** | **4.33e-20** | *** |
| Education: graduate level (vs college) | -2.0582 | 1.8541 | ±3.7082 | -1.110 | 0.2670 |  |
| Education: high school or below (vs college) | +0.3583 | 4.3452 | ±8.6903 | +0.082 | 0.9343 |  |
| Site: UCSD (vs UAB) | +0.4964 | 2.5761 | ±5.1523 | +0.193 | 0.8472 |  |
| **Site: UW (vs UAB)** | **-4.0582** | 2.0113 | ±4.0226 | **-2.018** | **0.0436** | * |
| **Age (years)** | **-0.4005** | 0.0853 | ±0.1706 | **-4.694** | **2.68e-06** | *** |
| BMI (kg/m2) | +0.2416 | 0.1462 | ±0.2924 | +1.652 | 0.0985 | . |
| Hypertension | -1.1840 | 1.9783 | ±3.9566 | -0.599 | 0.5495 |  |
| High cholesterol | +0.9941 | 1.9189 | ±3.8377 | +0.518 | 0.6044 |  |
| Kidney disease | -2.2916 | 4.4030 | ±8.8061 | -0.520 | 0.6027 |  |
| Circulatory disease | +0.1370 | 2.5722 | ±5.1443 | +0.053 | 0.9575 |  |
| Time 54-69, pooled (%) | -0.0857 | 0.4500 | ±0.9000 | -0.190 | 0.8490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **374**, R² = **0.1090**, Adj R² = **0.0820**, F-statistic = **4.03** (p = **1.43e-05**), Residual SE = **16.444** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.8514** | 7.4596 | ±14.9192 | **+9.230** | **2.71e-20** | *** |
| Education: graduate level (vs college) | -2.0685 | 1.8539 | ±3.7078 | -1.116 | 0.2645 |  |
| Education: high school or below (vs college) | +0.3338 | 4.3530 | ±8.7059 | +0.077 | 0.9389 |  |
| Site: UCSD (vs UAB) | +0.4917 | 2.5715 | ±5.1431 | +0.191 | 0.8484 |  |
| **Site: UW (vs UAB)** | **-4.0806** | 2.0070 | ±4.0140 | **-2.033** | **0.0420** | * |
| **Age (years)** | **-0.4001** | 0.0852 | ±0.1704 | **-4.697** | **2.64e-06** | *** |
| BMI (kg/m2) | +0.2418 | 0.1462 | ±0.2925 | +1.654 | 0.0982 | . |
| Hypertension | -1.1977 | 1.9805 | ±3.9609 | -0.605 | 0.5453 |  |
| High cholesterol | +0.9845 | 1.9173 | ±3.8346 | +0.513 | 0.6076 |  |
| Kidney disease | -2.2961 | 4.3968 | ±8.7935 | -0.522 | 0.6015 |  |
| Circulatory disease | +0.1321 | 2.5711 | ±5.1422 | +0.051 | 0.9590 |  |
| Avg. daily time 54-69 (%) | -0.1124 | 0.4620 | ±0.9239 | -0.243 | 0.8077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **374**, R² = **0.1090**, Adj R² = **0.0820**, F-statistic = **4.03** (p = **1.43e-05**), Residual SE = **16.444** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.9305** | 7.5160 | ±15.0319 | **+9.171** | **4.68e-20** | *** |
| Education: graduate level (vs college) | -2.0632 | 1.8531 | ±3.7062 | -1.113 | 0.2656 |  |
| Education: high school or below (vs college) | +0.3469 | 4.3467 | ±8.6935 | +0.080 | 0.9364 |  |
| Site: UCSD (vs UAB) | +0.4601 | 2.5812 | ±5.1625 | +0.178 | 0.8585 |  |
| **Site: UW (vs UAB)** | **-4.0887** | 2.0151 | ±4.0303 | **-2.029** | **0.0425** | * |
| **Age (years)** | **-0.4004** | 0.0852 | ±0.1705 | **-4.697** | **2.64e-06** | *** |
| BMI (kg/m2) | +0.2411 | 0.1463 | ±0.2926 | +1.648 | 0.0994 | . |
| Hypertension | -1.1990 | 1.9809 | ±3.9618 | -0.605 | 0.5450 |  |
| High cholesterol | +0.9745 | 1.9178 | ±3.8356 | +0.508 | 0.6114 |  |
| Kidney disease | -2.2769 | 4.4098 | ±8.8197 | -0.516 | 0.6056 |  |
| Circulatory disease | +0.1255 | 2.5708 | ±5.1417 | +0.049 | 0.9611 |  |
| Time < 70 (%) | -0.0897 | 0.3451 | ±0.6902 | -0.260 | 0.7949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **374**, R² = **0.1092**, Adj R² = **0.0821**, F-statistic = **4.03** (p = **1.39e-05**), Residual SE = **16.442** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.9278** | 7.4585 | ±14.9170 | **+9.241** | **2.43e-20** | *** |
| Education: graduate level (vs college) | -2.0795 | 1.8525 | ±3.7049 | -1.123 | 0.2616 |  |
| Education: high school or below (vs college) | +0.3154 | 4.3582 | ±8.7164 | +0.072 | 0.9423 |  |
| Site: UCSD (vs UAB) | +0.4552 | 2.5717 | ±5.1433 | +0.177 | 0.8595 |  |
| **Site: UW (vs UAB)** | **-4.1241** | 2.0107 | ±4.0213 | **-2.051** | **0.0403** | * |
| **Age (years)** | **-0.3995** | 0.0851 | ±0.1702 | **-4.693** | **2.69e-06** | *** |
| BMI (kg/m2) | +0.2415 | 0.1463 | ±0.2927 | +1.650 | 0.0989 | . |
| Hypertension | -1.2209 | 1.9845 | ±3.9691 | -0.615 | 0.5384 |  |
| High cholesterol | +0.9602 | 1.9168 | ±3.8335 | +0.501 | 0.6164 |  |
| Kidney disease | -2.2815 | 4.4000 | ±8.8000 | -0.519 | 0.6041 |  |
| Circulatory disease | +0.1154 | 2.5708 | ±5.1416 | +0.045 | 0.9642 |  |
| Avg. daily time < 70 (%) | -0.1245 | 0.3905 | ±0.7811 | -0.319 | 0.7499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **374**, R² = **0.1092**, Adj R² = **0.0821**, F-statistic = **4.03** (p = **1.39e-05**), Residual SE = **16.442** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +41.0374 | 64.0045 | ±128.0090 | +0.641 | 0.5214 |  |
| Education: graduate level (vs college) | -2.0630 | 1.8597 | ±3.7194 | -1.109 | 0.2673 |  |
| Education: high school or below (vs college) | +0.3686 | 4.3342 | ±8.6684 | +0.085 | 0.9322 |  |
| Site: UCSD (vs UAB) | +0.4225 | 2.5736 | ±5.1473 | +0.164 | 0.8696 |  |
| **Site: UW (vs UAB)** | **-4.1083** | 1.9966 | ±3.9932 | **-2.058** | **0.0396** | * |
| **Age (years)** | **-0.3987** | 0.0852 | ±0.1704 | **-4.681** | **2.86e-06** | *** |
| BMI (kg/m2) | +0.2384 | 0.1463 | ±0.2926 | +1.629 | 0.1032 |  |
| Hypertension | -1.1877 | 1.9791 | ±3.9581 | -0.600 | 0.5484 |  |
| High cholesterol | +0.9586 | 1.9230 | ±3.8459 | +0.499 | 0.6181 |  |
| Kidney disease | -2.0881 | 4.4891 | ±8.9783 | -0.465 | 0.6418 |  |
| Circulatory disease | +0.1092 | 2.5602 | ±5.1203 | +0.043 | 0.9660 |  |
| Time 54-250, pooled (%) | +0.2787 | 0.6436 | ±1.2872 | +0.433 | 0.6649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **374**, R² = **0.1097**, Adj R² = **0.0827**, F-statistic = **4.06** (p = **1.28e-05**), Residual SE = **16.437** on **362** df, AIC = **3167.2**, BIC = **3214.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +19.1153 | 78.0080 | ±156.0160 | +0.245 | 0.8064 |  |
| Education: graduate level (vs college) | -2.0900 | 1.8602 | ±3.7205 | -1.124 | 0.2612 |  |
| Education: high school or below (vs college) | +0.3472 | 4.3429 | ±8.6859 | +0.080 | 0.9363 |  |
| Site: UCSD (vs UAB) | +0.3835 | 2.5664 | ±5.1327 | +0.149 | 0.8812 |  |
| **Site: UW (vs UAB)** | **-4.1718** | 1.9916 | ±3.9832 | **-2.095** | **0.0362** | * |
| **Age (years)** | **-0.3958** | 0.0855 | ±0.1709 | **-4.630** | **3.65e-06** | *** |
| BMI (kg/m2) | +0.2383 | 0.1460 | ±0.2921 | +1.632 | 0.1028 |  |
| Hypertension | -1.2202 | 1.9809 | ±3.9618 | -0.616 | 0.5379 |  |
| High cholesterol | +0.9398 | 1.9213 | ±3.8427 | +0.489 | 0.6248 |  |
| Kidney disease | -1.9251 | 4.5067 | ±9.0135 | -0.427 | 0.6693 |  |
| Circulatory disease | +0.0674 | 2.5623 | ±5.1246 | +0.026 | 0.9790 |  |
| Avg. daily time 54-250 (%) | +0.4973 | 0.7793 | ±1.5587 | +0.638 | 0.5234 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **374**, R² = **0.1091**, Adj R² = **0.0820**, F-statistic = **4.03** (p = **1.43e-05**), Residual SE = **16.444** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6621** | 7.3998 | ±14.7996 | **+9.279** | **1.71e-20** | *** |
| Education: graduate level (vs college) | -2.0532 | 1.8595 | ±3.7191 | -1.104 | 0.2695 |  |
| Education: high school or below (vs college) | +0.3622 | 4.3608 | ±8.7216 | +0.083 | 0.9338 |  |
| Site: UCSD (vs UAB) | +0.5143 | 2.5852 | ±5.1704 | +0.199 | 0.8423 |  |
| **Site: UW (vs UAB)** | **-4.0255** | 2.0195 | ±4.0391 | **-1.993** | **0.0462** | * |
| **Age (years)** | **-0.4020** | 0.0861 | ±0.1721 | **-4.671** | **2.99e-06** | *** |
| BMI (kg/m2) | +0.2411 | 0.1459 | ±0.2917 | +1.653 | 0.0984 | . |
| Hypertension | -1.1898 | 1.9715 | ±3.9431 | -0.603 | 0.5462 |  |
| High cholesterol | +1.0017 | 1.9167 | ±3.8334 | +0.523 | 0.6012 |  |
| Kidney disease | -2.4834 | 4.4340 | ±8.8679 | -0.560 | 0.5754 |  |
| Circulatory disease | +0.1960 | 2.5758 | ±5.1516 | +0.076 | 0.9394 |  |
| Time 181-250, pooled (%) | +0.0617 | 0.2269 | ±0.4539 | +0.272 | 0.7858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **374**, R² = **0.1090**, Adj R² = **0.0819**, F-statistic = **4.02** (p = **1.45e-05**), Residual SE = **16.445** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6712** | 7.4063 | ±14.8126 | **+9.272** | **1.83e-20** | *** |
| Education: graduate level (vs college) | -2.0523 | 1.8605 | ±3.7210 | -1.103 | 0.2700 |  |
| Education: high school or below (vs college) | +0.3735 | 4.3546 | ±8.7092 | +0.086 | 0.9317 |  |
| Site: UCSD (vs UAB) | +0.5227 | 2.5838 | ±5.1675 | +0.202 | 0.8397 |  |
| **Site: UW (vs UAB)** | **-4.0198** | 2.0195 | ±4.0391 | **-1.990** | **0.0465** | * |
| **Age (years)** | **-0.4016** | 0.0860 | ±0.1719 | **-4.671** | **2.99e-06** | *** |
| BMI (kg/m2) | +0.2408 | 0.1459 | ±0.2919 | +1.650 | 0.0990 | . |
| Hypertension | -1.1812 | 1.9718 | ±3.9435 | -0.599 | 0.5491 |  |
| High cholesterol | +1.0067 | 1.9169 | ±3.8338 | +0.525 | 0.5995 |  |
| Kidney disease | -2.4325 | 4.4383 | ±8.8767 | -0.548 | 0.5836 |  |
| Circulatory disease | +0.1884 | 2.5742 | ±5.1484 | +0.073 | 0.9417 |  |
| Avg. daily time 181-250 (%) | +0.0441 | 0.2162 | ±0.4325 | +0.204 | 0.8385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **374**, R² = **0.1090**, Adj R² = **0.0819**, F-statistic = **4.02** (p = **1.45e-05**), Residual SE = **16.445** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6586** | 7.4032 | ±14.8065 | **+9.274** | **1.79e-20** | *** |
| Education: graduate level (vs college) | -2.0504 | 1.8610 | ±3.7220 | -1.102 | 0.2706 |  |
| Education: high school or below (vs college) | +0.3722 | 4.3541 | ±8.7082 | +0.085 | 0.9319 |  |
| Site: UCSD (vs UAB) | +0.5230 | 2.5842 | ±5.1684 | +0.202 | 0.8396 |  |
| **Site: UW (vs UAB)** | **-4.0158** | 2.0167 | ±4.0334 | **-1.991** | **0.0465** | * |
| **Age (years)** | **-0.4017** | 0.0860 | ±0.1721 | **-4.670** | **3.02e-06** | *** |
| BMI (kg/m2) | +0.2412 | 0.1459 | ±0.2918 | +1.653 | 0.0983 | . |
| Hypertension | -1.1780 | 1.9724 | ±3.9448 | -0.597 | 0.5503 |  |
| High cholesterol | +1.0106 | 1.9181 | ±3.8361 | +0.527 | 0.5983 |  |
| Kidney disease | -2.4520 | 4.4508 | ±8.9016 | -0.551 | 0.5817 |  |
| Circulatory disease | +0.1888 | 2.5740 | ±5.1479 | +0.073 | 0.9415 |  |
| Time > 180 (%) | +0.0426 | 0.2037 | ±0.4073 | +0.209 | 0.8342 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **374**, R² = **0.1089**, Adj R² = **0.0818**, F-statistic = **4.02** (p = **1.47e-05**), Residual SE = **16.445** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6648** | 7.4087 | ±14.8175 | **+9.268** | **1.90e-20** | *** |
| Education: graduate level (vs college) | -2.0491 | 1.8620 | ±3.7241 | -1.100 | 0.2711 |  |
| Education: high school or below (vs college) | +0.3828 | 4.3473 | ±8.6947 | +0.088 | 0.9298 |  |
| Site: UCSD (vs UAB) | +0.5305 | 2.5823 | ±5.1646 | +0.205 | 0.8372 |  |
| **Site: UW (vs UAB)** | **-4.0115** | 2.0171 | ±4.0342 | **-1.989** | **0.0467** | * |
| **Age (years)** | **-0.4012** | 0.0859 | ±0.1718 | **-4.670** | **3.02e-06** | *** |
| BMI (kg/m2) | +0.2410 | 0.1460 | ±0.2919 | +1.651 | 0.0988 | . |
| Hypertension | -1.1684 | 1.9726 | ±3.9452 | -0.592 | 0.5536 |  |
| High cholesterol | +1.0147 | 1.9178 | ±3.8357 | +0.529 | 0.5968 |  |
| Kidney disease | -2.3943 | 4.4527 | ±8.9055 | -0.538 | 0.5908 |  |
| Circulatory disease | +0.1798 | 2.5724 | ±5.1448 | +0.070 | 0.9443 |  |
| Avg. daily time > 180 (%) | +0.0260 | 0.1946 | ±0.3891 | +0.133 | 0.8938 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **374**, R² = **0.1107**, Adj R² = **0.0837**, F-statistic = **4.10** (p = **1.09e-05**), Residual SE = **16.428** on **362** df, AIC = **3166.8**, BIC = **3213.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.4655** | 7.4356 | ±14.8712 | **+9.208** | **3.33e-20** | *** |
| Education: graduate level (vs college) | -2.1167 | 1.8678 | ±3.7356 | -1.133 | 0.2571 |  |
| Education: high school or below (vs college) | +0.4996 | 4.3058 | ±8.6116 | +0.116 | 0.9076 |  |
| Site: UCSD (vs UAB) | +0.4887 | 2.5729 | ±5.1459 | +0.190 | 0.8494 |  |
| **Site: UW (vs UAB)** | **-3.9878** | 2.0062 | ±4.0124 | **-1.988** | **0.0468** | * |
| **Age (years)** | **-0.3966** | 0.0857 | ±0.1715 | **-4.627** | **3.71e-06** | *** |
| BMI (kg/m2) | +0.2467 | 0.1470 | ±0.2940 | +1.678 | 0.0933 | . |
| Hypertension | -1.0318 | 1.9750 | ±3.9499 | -0.522 | 0.6014 |  |
| High cholesterol | +1.0367 | 1.9153 | ±3.8305 | +0.541 | 0.5883 |  |
| Kidney disease | -2.2524 | 4.3828 | ±8.7657 | -0.514 | 0.6073 |  |
| Circulatory disease | -0.0254 | 2.5512 | ±5.1023 | -0.010 | 0.9920 |  |
| Nocturnal time > 180 (%) | -0.1623 | 0.1954 | ±0.3907 | -0.831 | 0.4061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **374**, R² = **0.1090**, Adj R² = **0.0819**, F-statistic = **4.03** (p = **1.45e-05**), Residual SE = **16.444** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6039** | 7.3821 | ±14.7643 | **+9.293** | **1.50e-20** | *** |
| Education: graduate level (vs college) | -2.0305 | 1.8575 | ±3.7151 | -1.093 | 0.2743 |  |
| Education: high school or below (vs college) | +0.3919 | 4.3684 | ±8.7368 | +0.090 | 0.9285 |  |
| Site: UCSD (vs UAB) | +0.4962 | 2.5964 | ±5.1928 | +0.191 | 0.8484 |  |
| **Site: UW (vs UAB)** | **-3.9995** | 2.0051 | ±4.0102 | **-1.995** | **0.0461** | * |
| **Age (years)** | **-0.4017** | 0.0858 | ±0.1715 | **-4.684** | **2.82e-06** | *** |
| BMI (kg/m2) | +0.2425 | 0.1459 | ±0.2918 | +1.662 | 0.0965 | . |
| Hypertension | -1.1719 | 1.9704 | ±3.9408 | -0.595 | 0.5520 |  |
| High cholesterol | +1.0181 | 1.9239 | ±3.8478 | +0.529 | 0.5967 |  |
| Kidney disease | -2.3677 | 4.4105 | ±8.8209 | -0.537 | 0.5914 |  |
| Circulatory disease | +0.1856 | 2.5750 | ±5.1500 | +0.072 | 0.9425 |  |
| Any reading > 250 during wear (0/1) | +0.5834 | 2.5005 | ±5.0011 | +0.233 | 0.8155 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **374**, R² = **0.1090**, Adj R² = **0.0819**, F-statistic = **4.02** (p = **1.45e-05**), Residual SE = **16.445** on **362** df, AIC = **3167.6**, BIC = **3214.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6548** | 7.4178 | ±14.8356 | **+9.255** | **2.13e-20** | *** |
| Education: graduate level (vs college) | -2.0494 | 1.8704 | ±3.7408 | -1.096 | 0.2732 |  |
| Education: high school or below (vs college) | +0.3986 | 4.3304 | ±8.6609 | +0.092 | 0.9267 |  |
| Site: UCSD (vs UAB) | +0.5287 | 2.5732 | ±5.1465 | +0.205 | 0.8372 |  |
| **Site: UW (vs UAB)** | **-4.0225** | 1.9976 | ±3.9951 | **-2.014** | **0.0440** | * |
| **Age (years)** | **-0.3991** | 0.0855 | ±0.1709 | **-4.669** | **3.03e-06** | *** |
| BMI (kg/m2) | +0.2401 | 0.1463 | ±0.2926 | +1.641 | 0.1008 |  |
| Hypertension | -1.1459 | 1.9741 | ±3.9482 | -0.580 | 0.5616 |  |
| High cholesterol | +1.0145 | 1.9282 | ±3.8564 | +0.526 | 0.5988 |  |
| Kidney disease | -2.1237 | 4.5434 | ±9.0867 | -0.467 | 0.6402 |  |
| Circulatory disease | +0.1400 | 2.5628 | ±5.1255 | +0.055 | 0.9564 |  |
| Time > 250 (%) | -0.2938 | 1.6052 | ±3.2104 | -0.183 | 0.8548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 374)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **374**, R² = **0.1091**, Adj R² = **0.0820**, F-statistic = **4.03** (p = **1.42e-05**), Residual SE = **16.443** on **362** df, AIC = **3167.5**, BIC = **3214.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.6299** | 7.4137 | ±14.8274 | **+9.257** | **2.10e-20** | *** |
| Education: graduate level (vs college) | -2.0539 | 1.8735 | ±3.7469 | -1.096 | 0.2729 |  |
| Education: high school or below (vs college) | +0.3944 | 4.3330 | ±8.6659 | +0.091 | 0.9275 |  |
| Site: UCSD (vs UAB) | +0.5153 | 2.5718 | ±5.1437 | +0.200 | 0.8412 |  |
| **Site: UW (vs UAB)** | **-4.0257** | 1.9992 | ±3.9985 | **-2.014** | **0.0440** | * |
| **Age (years)** | **-0.3984** | 0.0854 | ±0.1707 | **-4.667** | **3.05e-06** | *** |
| BMI (kg/m2) | +0.2401 | 0.1462 | ±0.2924 | +1.643 | 0.1005 |  |
| Hypertension | -1.1485 | 1.9738 | ±3.9476 | -0.582 | 0.5606 |  |
| High cholesterol | +1.0204 | 1.9253 | ±3.8505 | +0.530 | 0.5961 |  |
| Kidney disease | -2.0463 | 4.5285 | ±9.0569 | -0.452 | 0.6514 |  |
| Circulatory disease | +0.1294 | 2.5649 | ±5.1298 | +0.050 | 0.9597 |  |
| Avg. daily time > 250 (%) | -0.3964 | 1.6086 | ±3.2171 | -0.246 | 0.8054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 150 single-predictor tests; 1 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 374): best single predictor out of sample is **CV** (CV R² 0.054 vs 0.055 for covariates alone, gain -0.000; -201 per SD, p = 0.336). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 374): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.076 vs 0.078 for covariates alone, gain -0.002; -0.252 per SD, p = 0.576). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 373): best single predictor out of sample is **Mean/SD** (CV R² 0.105 vs 0.100 for covariates alone, gain +0.006; -0.681 per SD, p = 0.072). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Total sleep time per night (min)** (n = 383): best single predictor out of sample is **MAG** (CV R² -0.021 vs -0.051 for covariates alone, gain +0.030; -11.9 per SD, p = 3.4e-04). Raw p < 0.05 (FDR not applicable here): MAG (p = 3.4e-04).
- **Garmin stress score, mean (0-100)** (n = 374): best single predictor out of sample is **Mean/SD** (CV R² 0.046 vs 0.043 for covariates alone, gain +0.003; -1.72 per SD, p = 0.051). No glycaemic measure is associated with this outcome (all p > 0.05).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.030, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.006, via Mean/SD); Garmin stress score, mean (0-100) (+0.003, via Mean/SD); Steps per wear-day (-0.000, via CV). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 1 raw-significant of 40); HbA1c (0 FDR-significant / 0 raw-significant of 5); CGM level (0 FDR-significant / 0 raw-significant of 15).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Resting heart-rate proxy (Mean/SD, ΔAIC -2.5); Total sleep time per night (MAG, ΔAIC -12.9); Garmin stress score, mean (Mean/SD, ΔAIC -2.3).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
