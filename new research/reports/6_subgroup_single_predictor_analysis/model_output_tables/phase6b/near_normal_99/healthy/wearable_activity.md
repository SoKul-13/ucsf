# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 344; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **344**, R² = **0.1714**, Adj R² = **0.1465**, F-statistic = **6.89** (p = **8.38e-10**), Residual SE = **3359.536** on **333** df, AIC = **6573.3**, BIC = **6615.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18737.1654** | 1352.8715 | ±2705.7429 | **+13.850** | **1.27e-43** | *** |
| Education: graduate level (vs college) | -608.4617 | 372.7710 | ±745.5420 | -1.632 | 0.1026 |  |
| Education: high school or below (vs college) | +1206.0004 | 903.7020 | ±1807.4039 | +1.335 | 0.1820 |  |
| Site: UCSD (vs UAB) | -228.1382 | 496.6439 | ±993.2878 | -0.459 | 0.6460 |  |
| **Site: UW (vs UAB)** | **-932.5830** | 457.6689 | ±915.3378 | **-2.038** | **0.0416** | * |
| **Age (years)** | **-114.6485** | 17.6928 | ±35.3856 | **-6.480** | **9.17e-11** | *** |
| BMI (kg/m2) | -48.3669 | 25.1795 | ±50.3590 | -1.921 | 0.0547 | . |
| Hypertension | +139.4417 | 428.9198 | ±857.8396 | +0.325 | 0.7451 |  |
| High cholesterol | -78.7601 | 381.6871 | ±763.3742 | -0.206 | 0.8365 |  |
| Kidney disease | -494.6464 | 812.3045 | ±1624.6090 | -0.609 | 0.5426 |  |
| Circulatory disease | -716.8285 | 697.5878 | ±1395.1756 | -1.028 | 0.3041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **344**, R² = **0.1753**, Adj R² = **0.1479**, F-statistic = **6.41** (p = **1.16e-09**), Residual SE = **3356.744** on **332** df, AIC = **6573.7**, BIC = **6619.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14648.5954** | 3659.3022 | ±7318.6043 | **+4.003** | **6.25e-05** | *** |
| Education: graduate level (vs college) | -594.5043 | 372.0039 | ±744.0078 | -1.598 | 0.1100 |  |
| Education: high school or below (vs college) | +1184.7587 | 900.8461 | ±1801.6922 | +1.315 | 0.1885 |  |
| Site: UCSD (vs UAB) | -185.0097 | 493.6141 | ±987.2282 | -0.375 | 0.7078 |  |
| Site: UW (vs UAB) | -886.6190 | 456.2231 | ±912.4463 | -1.943 | 0.0520 | . |
| **Age (years)** | **-117.1549** | 17.8917 | ±35.7835 | **-6.548** | **5.83e-11** | *** |
| **BMI (kg/m2)** | **-51.7722** | 24.5478 | ±49.0956 | **-2.109** | **0.0349** | * |
| Hypertension | +95.9523 | 428.7355 | ±857.4710 | +0.224 | 0.8229 |  |
| High cholesterol | -187.1493 | 391.2889 | ±782.5778 | -0.478 | 0.6324 |  |
| Kidney disease | -454.7819 | 824.9006 | ±1649.8013 | -0.551 | 0.5814 |  |
| Circulatory disease | -684.2582 | 698.1701 | ±1396.3402 | -0.980 | 0.3270 |  |
| HbA1c (%) | +788.7293 | 651.2510 | ±1302.5019 | +1.211 | 0.2259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.20e-09**), Residual SE = **3364.124** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19582.1597** | 3449.5143 | ±6899.0285 | **+5.677** | **1.37e-08** | *** |
| Education: graduate level (vs college) | -611.4817 | 373.7285 | ±747.4569 | -1.636 | 0.1018 |  |
| Education: high school or below (vs college) | +1197.8873 | 907.0025 | ±1814.0051 | +1.321 | 0.1866 |  |
| Site: UCSD (vs UAB) | -219.7096 | 502.3937 | ±1004.7873 | -0.437 | 0.6619 |  |
| **Site: UW (vs UAB)** | **-924.1300** | 461.8649 | ±923.7298 | **-2.001** | **0.0454** | * |
| **Age (years)** | **-114.9381** | 17.7693 | ±35.5386 | **-6.468** | **9.91e-11** | *** |
| BMI (kg/m2) | -47.6756 | 25.4558 | ±50.9117 | -1.873 | 0.0611 | . |
| Hypertension | +151.2524 | 433.9657 | ±867.9314 | +0.349 | 0.7274 |  |
| High cholesterol | -83.8997 | 385.4173 | ±770.8345 | -0.218 | 0.8277 |  |
| Kidney disease | -492.5171 | 812.6969 | ±1625.3939 | -0.606 | 0.5445 |  |
| Circulatory disease | -717.2150 | 699.0036 | ±1398.0072 | -1.026 | 0.3049 |  |
| Mean glucose (mg/dL) | -7.4751 | 28.0072 | ±56.0144 | -0.267 | 0.7895 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.20e-09**), Residual SE = **3364.124** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20616.5541** | 7176.0672 | ±14352.1343 | **+2.873** | **0.0041** | ** |
| Education: graduate level (vs college) | -611.4817 | 373.7285 | ±747.4569 | -1.636 | 0.1018 |  |
| Education: high school or below (vs college) | +1197.8873 | 907.0025 | ±1814.0051 | +1.321 | 0.1866 |  |
| Site: UCSD (vs UAB) | -219.7096 | 502.3937 | ±1004.7873 | -0.437 | 0.6619 |  |
| **Site: UW (vs UAB)** | **-924.1300** | 461.8649 | ±923.7298 | **-2.001** | **0.0454** | * |
| **Age (years)** | **-114.9381** | 17.7693 | ±35.5386 | **-6.468** | **9.91e-11** | *** |
| BMI (kg/m2) | -47.6756 | 25.4558 | ±50.9117 | -1.873 | 0.0611 | . |
| Hypertension | +151.2524 | 433.9657 | ±867.9314 | +0.349 | 0.7274 |  |
| High cholesterol | -83.8997 | 385.4173 | ±770.8345 | -0.218 | 0.8277 |  |
| Kidney disease | -492.5171 | 812.6969 | ±1625.3939 | -0.606 | 0.5445 |  |
| Circulatory disease | -717.2150 | 699.0036 | ±1398.0072 | -1.026 | 0.3049 |  |
| GMI (%) | -312.5059 | 1170.8688 | ±2341.7377 | -0.267 | 0.7895 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **344**, R² = **0.1715**, Adj R² = **0.1440**, F-statistic = **6.25** (p = **2.26e-09**), Residual SE = **3364.397** on **332** df, AIC = **6575.3**, BIC = **6621.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18286.7580** | 2705.1759 | ±5410.3517 | **+6.760** | **1.38e-11** | *** |
| Education: graduate level (vs college) | -602.4163 | 376.2088 | ±752.4175 | -1.601 | 0.1093 |  |
| Education: high school or below (vs college) | +1212.1415 | 906.2013 | ±1812.4027 | +1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | -239.4538 | 503.0218 | ±1006.0436 | -0.476 | 0.6341 |  |
| **Site: UW (vs UAB)** | **-940.6941** | 460.7530 | ±921.5059 | **-2.042** | **0.0412** | * |
| **Age (years)** | **-114.0664** | 17.9873 | ±35.9747 | **-6.341** | **2.28e-10** | *** |
| BMI (kg/m2) | -49.2783 | 25.7930 | ±51.5860 | -1.911 | 0.0561 | . |
| Hypertension | +134.0156 | 430.8638 | ±861.7276 | +0.311 | 0.7558 |  |
| High cholesterol | -78.6250 | 382.8061 | ±765.6121 | -0.205 | 0.8373 |  |
| Kidney disease | -489.3042 | 814.8305 | ±1629.6610 | -0.600 | 0.5482 |  |
| Circulatory disease | -713.6510 | 699.3265 | ±1398.6530 | -1.020 | 0.3075 |  |
| Nocturnal mean 00-06h (mg/dL) | +3.8864 | 20.3793 | ±40.7586 | +0.191 | 0.8488 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1769**, Adj R² = **0.1496**, F-statistic = **6.49** (p = **8.69e-10**), Residual SE = **3353.383** on **332** df, AIC = **6573.0**, BIC = **6619.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20785.6273** | 1919.5157 | ±3839.0314 | **+10.829** | **2.52e-27** | *** |
| Education: graduate level (vs college) | -661.8320 | 371.9292 | ±743.8585 | -1.779 | 0.0752 | . |
| Education: high school or below (vs college) | +1165.5124 | 909.3013 | ±1818.6026 | +1.282 | 0.1999 |  |
| Site: UCSD (vs UAB) | -294.6967 | 496.4653 | ±992.9306 | -0.594 | 0.5528 |  |
| **Site: UW (vs UAB)** | **-980.1542** | 464.8356 | ±929.6713 | **-2.109** | **0.0350** | * |
| **Age (years)** | **-114.4057** | 17.7661 | ±35.5322 | **-6.440** | **1.20e-10** | *** |
| BMI (kg/m2) | -46.4564 | 25.2874 | ±50.5747 | -1.837 | 0.0662 | . |
| Hypertension | +152.4517 | 428.2380 | ±856.4760 | +0.356 | 0.7218 |  |
| High cholesterol | -116.3891 | 383.4187 | ±766.8375 | -0.304 | 0.7615 |  |
| Kidney disease | -400.1377 | 776.6371 | ±1553.2742 | -0.515 | 0.6064 |  |
| Circulatory disease | -702.5254 | 699.8377 | ±1399.6754 | -1.004 | 0.3155 |  |
| Glucose SD, pooled (mg/dL) | -121.6274 | 90.1999 | ±180.3998 | -1.348 | 0.1775 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1788**, Adj R² = **0.1516**, F-statistic = **6.57** (p = **6.23e-10**), Residual SE = **3349.560** on **332** df, AIC = **6572.2**, BIC = **6618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20914.4973** | 1819.3771 | ±3638.7543 | **+11.495** | **1.39e-30** | *** |
| Education: graduate level (vs college) | -673.3168 | 373.8955 | ±747.7911 | -1.801 | 0.0717 | . |
| Education: high school or below (vs college) | +1147.0393 | 911.0270 | ±1822.0540 | +1.259 | 0.2080 |  |
| Site: UCSD (vs UAB) | -315.4106 | 495.7594 | ±991.5189 | -0.636 | 0.5246 |  |
| **Site: UW (vs UAB)** | **-995.4199** | 463.7502 | ±927.5003 | **-2.146** | **0.0318** | * |
| **Age (years)** | **-114.6894** | 17.7096 | ±35.4192 | **-6.476** | **9.41e-11** | *** |
| BMI (kg/m2) | -44.9812 | 25.5712 | ±51.1423 | -1.759 | 0.0786 | . |
| Hypertension | +138.5167 | 427.7728 | ±855.5457 | +0.324 | 0.7461 |  |
| High cholesterol | -114.1637 | 381.4099 | ±762.8198 | -0.299 | 0.7647 |  |
| Kidney disease | -389.6207 | 774.5108 | ±1549.0215 | -0.503 | 0.6149 |  |
| Circulatory disease | -715.0196 | 700.8412 | ±1401.6825 | -1.020 | 0.3076 |  |
| Avg. daily SD (mg/dL) | -140.7542 | 86.5289 | ±173.0579 | -1.627 | 0.1038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **344**, R² = **0.1762**, Adj R² = **0.1489**, F-statistic = **6.45** (p = **9.93e-10**), Residual SE = **3354.923** on **332** df, AIC = **6573.3**, BIC = **6619.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20582.4999** | 1815.4154 | ±3630.8308 | **+11.338** | **8.54e-30** | *** |
| Education: graduate level (vs college) | -650.4361 | 372.7479 | ±745.4957 | -1.745 | 0.0810 | . |
| Education: high school or below (vs college) | +1186.1211 | 909.2882 | ±1818.5764 | +1.304 | 0.1921 |  |
| Site: UCSD (vs UAB) | -304.1582 | 497.9874 | ±995.9749 | -0.611 | 0.5413 |  |
| **Site: UW (vs UAB)** | **-993.2339** | 466.1710 | ±932.3421 | **-2.131** | **0.0331** | * |
| **Age (years)** | **-113.8891** | 17.7950 | ±35.5901 | **-6.400** | **1.55e-10** | *** |
| BMI (kg/m2) | -48.0661 | 24.9141 | ±49.8281 | -1.929 | 0.0537 | . |
| Hypertension | +127.1536 | 430.8039 | ±861.6078 | +0.295 | 0.7679 |  |
| High cholesterol | -104.0905 | 381.0229 | ±762.0458 | -0.273 | 0.7847 |  |
| Kidney disease | -417.3190 | 785.4450 | ±1570.8900 | -0.531 | 0.5952 |  |
| Circulatory disease | -701.6015 | 701.4036 | ±1402.8072 | -1.000 | 0.3172 |  |
| CV (%) | -123.3208 | 89.5213 | ±179.0427 | -1.378 | 0.1683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **344**, R² = **0.1764**, Adj R² = **0.1491**, F-statistic = **6.46** (p = **9.50e-10**), Residual SE = **3354.412** on **332** df, AIC = **6573.2**, BIC = **6619.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16966.1817** | 1956.0064 | ±3912.0128 | **+8.674** | **4.18e-18** | *** |
| Education: graduate level (vs college) | -655.3913 | 373.3058 | ±746.6117 | -1.756 | 0.0791 | . |
| Education: high school or below (vs college) | +1191.3727 | 910.6285 | ±1821.2570 | +1.308 | 0.1908 |  |
| Site: UCSD (vs UAB) | -294.4740 | 497.8000 | ±995.6000 | -0.592 | 0.5542 |  |
| **Site: UW (vs UAB)** | **-983.3622** | 465.4183 | ±930.8366 | **-2.113** | **0.0346** | * |
| **Age (years)** | **-114.0105** | 17.7883 | ±35.5767 | **-6.409** | **1.46e-10** | *** |
| BMI (kg/m2) | -48.1649 | 24.8545 | ±49.7089 | -1.938 | 0.0526 | . |
| Hypertension | +134.8162 | 429.7449 | ±859.4899 | +0.314 | 0.7537 |  |
| High cholesterol | -106.9865 | 380.6027 | ±761.2055 | -0.281 | 0.7786 |  |
| Kidney disease | -437.1366 | 787.3809 | ±1574.7618 | -0.555 | 0.5788 |  |
| Circulatory disease | -704.7957 | 701.4233 | ±1402.8465 | -1.005 | 0.3150 |  |
| Mean / SD ratio | +260.6185 | 189.1556 | ±378.3111 | +1.378 | 0.1683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1780**, Adj R² = **0.1508**, F-statistic = **6.54** (p = **7.12e-10**), Residual SE = **3351.101** on **332** df, AIC = **6572.5**, BIC = **6618.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16842.2368** | 1872.7416 | ±3745.4833 | **+8.993** | **2.40e-19** | *** |
| Education: graduate level (vs college) | -665.1039 | 375.0919 | ±750.1838 | -1.773 | 0.0762 | . |
| Education: high school or below (vs college) | +1179.1688 | 912.3134 | ±1824.6267 | +1.293 | 0.1962 |  |
| Site: UCSD (vs UAB) | -317.7922 | 496.6461 | ±993.2922 | -0.640 | 0.5223 |  |
| **Site: UW (vs UAB)** | **-996.9237** | 463.8357 | ±927.6714 | **-2.149** | **0.0316** | * |
| **Age (years)** | **-114.2045** | 17.7365 | ±35.4730 | **-6.439** | **1.20e-10** | *** |
| BMI (kg/m2) | -46.3378 | 25.1329 | ±50.2658 | -1.844 | 0.0652 | . |
| Hypertension | +113.6677 | 430.6570 | ±861.3140 | +0.264 | 0.7918 |  |
| High cholesterol | -97.8498 | 379.6652 | ±759.3303 | -0.258 | 0.7966 |  |
| Kidney disease | -418.1708 | 789.1847 | ±1578.3693 | -0.530 | 0.5962 |  |
| Circulatory disease | -715.7875 | 702.4189 | ±1404.8379 | -1.019 | 0.3082 |  |
| Avg. daily mean/SD | +244.6903 | 151.6154 | ±303.2307 | +1.614 | 0.1066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **344**, R² = **0.1718**, Adj R² = **0.1444**, F-statistic = **6.26** (p = **2.13e-09**), Residual SE = **3363.726** on **332** df, AIC = **6575.1**, BIC = **6621.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18196.7105** | 1831.7983 | ±3663.5965 | **+9.934** | **2.97e-23** | *** |
| Education: graduate level (vs college) | -608.3817 | 373.9138 | ±747.8275 | -1.627 | 0.1037 |  |
| Education: high school or below (vs college) | +1186.1692 | 907.5205 | ±1815.0409 | +1.307 | 0.1912 |  |
| Site: UCSD (vs UAB) | -211.3568 | 495.8400 | ±991.6800 | -0.426 | 0.6699 |  |
| Site: UW (vs UAB) | -907.5477 | 467.3633 | ±934.7265 | -1.942 | 0.0522 | . |
| **Age (years)** | **-113.6816** | 17.6062 | ±35.2123 | **-6.457** | **1.07e-10** | *** |
| BMI (kg/m2) | -47.5728 | 25.0858 | ±50.1715 | -1.896 | 0.0579 | . |
| Hypertension | +150.0064 | 433.0157 | ±866.0314 | +0.346 | 0.7290 |  |
| High cholesterol | -89.6989 | 386.4008 | ±772.8016 | -0.232 | 0.8164 |  |
| Kidney disease | -521.7510 | 816.0054 | ±1632.0108 | -0.639 | 0.5226 |  |
| Circulatory disease | -722.9547 | 699.6959 | ±1399.3919 | -1.033 | 0.3015 |  |
| MAG (mg/dL/h) | +13.1549 | 35.3276 | ±70.6553 | +0.372 | 0.7096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **344**, R² = **0.1738**, Adj R² = **0.1465**, F-statistic = **6.35** (p = **1.50e-09**), Residual SE = **3359.640** on **332** df, AIC = **6574.3**, BIC = **6620.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20185.0616** | 2062.3884 | ±4124.7768 | **+9.787** | **1.28e-22** | *** |
| Education: graduate level (vs college) | -624.3918 | 375.2091 | ±750.4183 | -1.664 | 0.0961 | . |
| Education: high school or below (vs college) | +1188.8025 | 905.4840 | ±1810.9680 | +1.313 | 0.1892 |  |
| Site: UCSD (vs UAB) | -269.3213 | 495.6429 | ±991.2858 | -0.543 | 0.5869 |  |
| **Site: UW (vs UAB)** | **-967.2025** | 464.8228 | ±929.6456 | **-2.081** | **0.0375** | * |
| **Age (years)** | **-115.1116** | 17.7248 | ±35.4497 | **-6.494** | **8.34e-11** | *** |
| **BMI (kg/m2)** | **-50.3044** | 24.5310 | ±49.0620 | **-2.051** | **0.0403** | * |
| Hypertension | +116.4170 | 433.0267 | ±866.0534 | +0.269 | 0.7880 |  |
| High cholesterol | -79.8803 | 382.0912 | ±764.1824 | -0.209 | 0.8344 |  |
| Kidney disease | -453.9153 | 800.5830 | ±1601.1660 | -0.567 | 0.5707 |  |
| Circulatory disease | -699.0845 | 702.3528 | ±1404.7055 | -0.995 | 0.3196 |  |
| Avg. daily range (mg/dL) | -16.5423 | 19.4258 | ±38.8517 | -0.852 | 0.3945 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **344**, R² = **0.1714**, Adj R² = **0.1440**, F-statistic = **6.24** (p = **2.28e-09**), Residual SE = **3364.526** on **332** df, AIC = **6575.3**, BIC = **6621.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18686.4726** | 1445.3196 | ±2890.6391 | **+12.929** | **3.09e-38** | *** |
| Education: graduate level (vs college) | -609.8053 | 377.0339 | ±754.0678 | -1.617 | 0.1058 |  |
| Education: high school or below (vs college) | +1203.1084 | 912.0263 | ±1824.0527 | +1.319 | 0.1871 |  |
| Site: UCSD (vs UAB) | -227.1350 | 497.8397 | ±995.6794 | -0.456 | 0.6482 |  |
| **Site: UW (vs UAB)** | **-935.0471** | 460.1976 | ±920.3952 | **-2.032** | **0.0422** | * |
| **Age (years)** | **-114.7285** | 17.7710 | ±35.5419 | **-6.456** | **1.08e-10** | *** |
| BMI (kg/m2) | -48.4353 | 25.3718 | ±50.7436 | -1.909 | 0.0563 | . |
| Hypertension | +136.1128 | 430.2899 | ±860.5798 | +0.316 | 0.7518 |  |
| High cholesterol | -78.6710 | 383.5433 | ±767.0866 | -0.205 | 0.8375 |  |
| Kidney disease | -491.9725 | 815.0094 | ±1630.0188 | -0.604 | 0.5461 |  |
| Circulatory disease | -718.4509 | 701.8098 | ±1403.6197 | -1.024 | 0.3060 |  |
| SD of daily means (mg/dL) | +11.7644 | 127.0225 | ±254.0451 | +0.093 | 0.9262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **344**, R² = **0.1776**, Adj R² = **0.1504**, F-statistic = **6.52** (p = **7.64e-10**), Residual SE = **3351.913** on **332** df, AIC = **6572.7**, BIC = **6618.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +115961.9523 | 59974.0515 | ±119948.1029 | +1.934 | 0.0532 | . |
| Education: graduate level (vs college) | -582.6748 | 373.3987 | ±746.7975 | -1.560 | 0.1187 |  |
| Education: high school or below (vs college) | +1242.0377 | 906.3637 | ±1812.7274 | +1.370 | 0.1706 |  |
| Site: UCSD (vs UAB) | -176.2299 | 492.8097 | ±985.6194 | -0.358 | 0.7206 |  |
| **Site: UW (vs UAB)** | **-894.4077** | 454.9862 | ±909.9724 | **-1.966** | **0.0493** | * |
| **Age (years)** | **-113.2784** | 17.6636 | ±35.3272 | **-6.413** | **1.43e-10** | *** |
| BMI (kg/m2) | -46.7964 | 26.3720 | ±52.7440 | -1.774 | 0.0760 | . |
| Hypertension | +132.1466 | 427.1050 | ±854.2100 | +0.309 | 0.7570 |  |
| High cholesterol | -100.2281 | 383.7860 | ±767.5721 | -0.261 | 0.7940 |  |
| Kidney disease | -543.2520 | 844.9977 | ±1689.9954 | -0.643 | 0.5203 |  |
| Circulatory disease | -732.3732 | 700.7281 | ±1401.4562 | -1.045 | 0.2959 |  |
| Time in range 70-180, pooled (%) | -978.3127 | 602.0608 | ±1204.1217 | -1.625 | 0.1042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **344**, R² = **0.1786**, Adj R² = **0.1514**, F-statistic = **6.56** (p = **6.42e-10**), Residual SE = **3349.916** on **332** df, AIC = **6572.3**, BIC = **6618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120237.8992** | 58662.0420 | ±117324.0840 | **+2.050** | **0.0404** | * |
| Education: graduate level (vs college) | -578.0479 | 373.0336 | ±746.0673 | -1.550 | 0.1212 |  |
| Education: high school or below (vs college) | +1262.0507 | 903.9902 | ±1807.9805 | +1.396 | 0.1627 |  |
| Site: UCSD (vs UAB) | -181.6504 | 491.1659 | ±982.3317 | -0.370 | 0.7115 |  |
| **Site: UW (vs UAB)** | **-923.7989** | 454.2565 | ±908.5130 | **-2.034** | **0.0420** | * |
| **Age (years)** | **-112.1763** | 17.5763 | ±35.1526 | **-6.382** | **1.75e-10** | *** |
| BMI (kg/m2) | -47.8915 | 25.6226 | ±51.2453 | -1.869 | 0.0616 | . |
| Hypertension | +168.4396 | 430.4289 | ±860.8578 | +0.391 | 0.6956 |  |
| High cholesterol | -111.2399 | 383.5633 | ±767.1267 | -0.290 | 0.7718 |  |
| Kidney disease | -502.2864 | 838.8868 | ±1677.7736 | -0.599 | 0.5493 |  |
| Circulatory disease | -762.3623 | 697.8074 | ±1395.6148 | -1.093 | 0.2746 |  |
| Avg. daily time in range 70-180 (%) | -1020.9705 | 588.4638 | ±1176.9275 | -1.735 | 0.0827 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.21e-09**), Residual SE = **3364.158** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18702.6629** | 1366.1516 | ±2732.3031 | **+13.690** | **1.16e-42** | *** |
| Education: graduate level (vs college) | -606.6034 | 374.8048 | ±749.6097 | -1.618 | 0.1056 |  |
| Education: high school or below (vs college) | +1210.4444 | 905.4979 | ±1810.9958 | +1.337 | 0.1813 |  |
| Site: UCSD (vs UAB) | -206.5460 | 504.1584 | ±1008.3168 | -0.410 | 0.6820 |  |
| **Site: UW (vs UAB)** | **-919.7681** | 460.7663 | ±921.5325 | **-1.996** | **0.0459** | * |
| **Age (years)** | **-114.6765** | 17.7481 | ±35.4963 | **-6.461** | **1.04e-10** | *** |
| BMI (kg/m2) | -48.3633 | 25.2311 | ±50.4622 | -1.917 | 0.0553 | . |
| Hypertension | +131.9833 | 429.9526 | ±859.9051 | +0.307 | 0.7589 |  |
| High cholesterol | -77.4115 | 382.7726 | ±765.5451 | -0.202 | 0.8397 |  |
| Kidney disease | -479.7449 | 819.2997 | ±1638.5993 | -0.586 | 0.5582 |  |
| Circulatory disease | -725.7353 | 699.2793 | ±1398.5586 | -1.038 | 0.2993 |  |
| Any reading < 54 during wear (0/1) | +142.8272 | 460.0967 | ±920.1933 | +0.310 | 0.7562 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1758**, Adj R² = **0.1485**, F-statistic = **6.44** (p = **1.05e-09**), Residual SE = **3355.578** on **332** df, AIC = **6573.5**, BIC = **6619.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18638.5748** | 1355.1619 | ±2710.3238 | **+13.754** | **4.83e-43** | *** |
| Education: graduate level (vs college) | -601.7974 | 375.1891 | ±750.3782 | -1.604 | 0.1087 |  |
| Education: high school or below (vs college) | +1260.9596 | 907.6630 | ±1815.3260 | +1.389 | 0.1648 |  |
| Site: UCSD (vs UAB) | -155.2007 | 501.1661 | ±1002.3321 | -0.310 | 0.7568 |  |
| Site: UW (vs UAB) | -896.0089 | 459.1868 | ±918.3737 | -1.951 | 0.0510 | . |
| **Age (years)** | **-113.6394** | 17.6768 | ±35.3535 | **-6.429** | **1.29e-10** | *** |
| **BMI (kg/m2)** | **-50.9346** | 24.8998 | ±49.7996 | **-2.046** | **0.0408** | * |
| Hypertension | +98.5600 | 426.1703 | ±852.3406 | +0.231 | 0.8171 |  |
| High cholesterol | -70.2225 | 382.2795 | ±764.5590 | -0.184 | 0.8543 |  |
| Kidney disease | -442.5028 | 815.9602 | ±1631.9204 | -0.542 | 0.5876 |  |
| Circulatory disease | -783.0479 | 710.6022 | ±1421.2044 | -1.102 | 0.2705 |  |
| Time < 54 (%) | +4645.6067 | 5234.6682 | ±10469.3363 | +0.887 | 0.3748 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1810**, Adj R² = **0.1538**, F-statistic = **6.67** (p = **4.22e-10**), Residual SE = **3345.102** on **332** df, AIC = **6571.3**, BIC = **6617.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18667.5462** | 1349.7046 | ±2699.4093 | **+13.831** | **1.66e-43** | *** |
| Education: graduate level (vs college) | -626.7449 | 371.4647 | ±742.9293 | -1.687 | 0.0916 | . |
| Education: high school or below (vs college) | +1233.8384 | 905.1374 | ±1810.2747 | +1.363 | 0.1728 |  |
| Site: UCSD (vs UAB) | -172.2521 | 493.5083 | ±987.0166 | -0.349 | 0.7271 |  |
| **Site: UW (vs UAB)** | **-920.1367** | 458.3822 | ±916.7644 | **-2.007** | **0.0447** | * |
| **Age (years)** | **-113.7225** | 17.5751 | ±35.1502 | **-6.471** | **9.76e-11** | *** |
| **BMI (kg/m2)** | **-50.9503** | 25.0405 | ±50.0811 | **-2.035** | **0.0419** | * |
| Hypertension | +116.0736 | 426.9673 | ±853.9346 | +0.272 | 0.7857 |  |
| High cholesterol | -61.8489 | 380.9724 | ±761.9448 | -0.162 | 0.8710 |  |
| Kidney disease | -449.1402 | 817.6182 | ±1635.2363 | -0.549 | 0.5828 |  |
| Circulatory disease | -855.8216 | 718.6641 | ±1437.3283 | -1.191 | 0.2337 |  |
| Avg. daily time < 54 (%) | +8155.5683 | 6335.8486 | ±12671.6973 | +1.287 | 0.1980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.21e-09**), Residual SE = **3364.151** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18681.2917** | 1366.7369 | ±2733.4738 | **+13.669** | **1.57e-42** | *** |
| Education: graduate level (vs college) | -603.1738 | 375.2516 | ±750.5033 | -1.607 | 0.1080 |  |
| Education: high school or below (vs college) | +1198.9707 | 910.6560 | ±1821.3120 | +1.317 | 0.1880 |  |
| Site: UCSD (vs UAB) | -218.2468 | 495.5146 | ±991.0292 | -0.440 | 0.6596 |  |
| **Site: UW (vs UAB)** | **-921.5160** | 459.0608 | ±918.1216 | **-2.007** | **0.0447** | * |
| **Age (years)** | **-114.6753** | 17.7446 | ±35.4893 | **-6.463** | **1.03e-10** | *** |
| BMI (kg/m2) | -48.1311 | 25.2919 | ±50.5838 | -1.903 | 0.0570 | . |
| Hypertension | +152.4473 | 433.2053 | ±866.4106 | +0.352 | 0.7249 |  |
| High cholesterol | -93.3002 | 392.6287 | ±785.2574 | -0.238 | 0.8122 |  |
| Kidney disease | -483.4568 | 816.9220 | ±1633.8440 | -0.592 | 0.5540 |  |
| Circulatory disease | -715.9170 | 699.5365 | ±1399.0729 | -1.023 | 0.3061 |  |
| Time 54-69, pooled (%) | +300.2638 | 981.8964 | ±1963.7929 | +0.306 | 0.7598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **344**, R² = **0.1715**, Adj R² = **0.1440**, F-statistic = **6.25** (p = **2.27e-09**), Residual SE = **3364.469** on **332** df, AIC = **6575.3**, BIC = **6621.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18712.9267** | 1357.0624 | ±2714.1248 | **+13.789** | **2.96e-43** | *** |
| Education: graduate level (vs college) | -604.4449 | 374.7519 | ±749.5038 | -1.613 | 0.1068 |  |
| Education: high school or below (vs college) | +1202.6015 | 909.7291 | ±1819.4583 | +1.322 | 0.1862 |  |
| Site: UCSD (vs UAB) | -225.3172 | 495.5556 | ±991.1112 | -0.455 | 0.6493 |  |
| **Site: UW (vs UAB)** | **-930.5723** | 458.5391 | ±917.0783 | **-2.029** | **0.0424** | * |
| **Age (years)** | **-114.6742** | 17.7341 | ±35.4683 | **-6.466** | **1.00e-10** | *** |
| BMI (kg/m2) | -48.3014 | 25.2655 | ±50.5311 | -1.912 | 0.0559 | . |
| Hypertension | +150.7294 | 440.5055 | ±881.0111 | +0.342 | 0.7322 |  |
| High cholesterol | -84.4423 | 390.1379 | ±780.2758 | -0.216 | 0.8286 |  |
| Kidney disease | -489.5009 | 817.5062 | ±1635.0123 | -0.599 | 0.5493 |  |
| Circulatory disease | -720.0313 | 700.8109 | ±1401.6219 | -1.027 | 0.3042 |  |
| Avg. daily time 54-69 (%) | +160.5898 | 1003.1227 | ±2006.2454 | +0.160 | 0.8728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **344**, R² = **0.1723**, Adj R² = **0.1449**, F-statistic = **6.28** (p = **1.95e-09**), Residual SE = **3362.726** on **332** df, AIC = **6574.9**, BIC = **6621.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18623.6104** | 1370.6398 | ±2741.2795 | **+13.588** | **4.75e-42** | *** |
| Education: graduate level (vs college) | -598.0292 | 376.3856 | ±752.7713 | -1.589 | 0.1121 |  |
| Education: high school or below (vs college) | +1199.6566 | 909.4485 | ±1818.8971 | +1.319 | 0.1871 |  |
| Site: UCSD (vs UAB) | -201.4932 | 495.4680 | ±990.9360 | -0.407 | 0.6842 |  |
| **Site: UW (vs UAB)** | **-908.0811** | 459.0997 | ±918.1994 | **-1.978** | **0.0479** | * |
| **Age (years)** | **-114.5785** | 17.7604 | ±35.5208 | **-6.451** | **1.11e-10** | *** |
| BMI (kg/m2) | -48.2395 | 25.3316 | ±50.6633 | -1.904 | 0.0569 | . |
| Hypertension | +158.3473 | 433.7404 | ±867.4808 | +0.365 | 0.7151 |  |
| High cholesterol | -104.2788 | 391.9273 | ±783.8546 | -0.266 | 0.7902 |  |
| Kidney disease | -468.0850 | 816.7750 | ±1633.5500 | -0.573 | 0.5666 |  |
| Circulatory disease | -722.9737 | 702.3785 | ±1404.7571 | -1.029 | 0.3033 |  |
| Time < 70 (%) | +547.7692 | 973.3642 | ±1946.7283 | +0.563 | 0.5736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **344**, R² = **0.1722**, Adj R² = **0.1448**, F-statistic = **6.28** (p = **1.98e-09**), Residual SE = **3362.908** on **332** df, AIC = **6575.0**, BIC = **6621.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18651.7288** | 1358.4484 | ±2716.8968 | **+13.730** | **6.70e-43** | *** |
| Education: graduate level (vs college) | -596.2620 | 376.1917 | ±752.3834 | -1.585 | 0.1130 |  |
| Education: high school or below (vs college) | +1196.4899 | 909.8164 | ±1819.6327 | +1.315 | 0.1885 |  |
| Site: UCSD (vs UAB) | -215.0557 | 494.5150 | ±989.0300 | -0.435 | 0.6636 |  |
| **Site: UW (vs UAB)** | **-925.0574** | 458.4348 | ±916.8696 | **-2.018** | **0.0436** | * |
| **Age (years)** | **-114.6734** | 17.7338 | ±35.4676 | **-6.466** | **1.00e-10** | *** |
| BMI (kg/m2) | -48.3179 | 25.3532 | ±50.7065 | -1.906 | 0.0567 | . |
| Hypertension | +175.5638 | 443.1039 | ±886.2079 | +0.396 | 0.6919 |  |
| High cholesterol | -96.6056 | 389.5020 | ±779.0039 | -0.248 | 0.8041 |  |
| Kidney disease | -474.4912 | 817.0366 | ±1634.0732 | -0.581 | 0.5614 |  |
| Circulatory disease | -736.6441 | 703.9270 | ±1407.8539 | -1.046 | 0.2953 |  |
| Avg. daily time < 70 (%) | +535.7469 | 1016.9479 | ±2033.8958 | +0.527 | 0.5983 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1756**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.10e-09**), Residual SE = **3356.118** on **332** df, AIC = **6573.6**, BIC = **6619.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +467196.3580 | 523788.8656 | ±1047577.7312 | +0.892 | 0.3724 |  |
| Education: graduate level (vs college) | -597.9257 | 376.4560 | ±752.9119 | -1.588 | 0.1122 |  |
| Education: high school or below (vs college) | +1262.1010 | 907.6685 | ±1815.3370 | +1.390 | 0.1644 |  |
| Site: UCSD (vs UAB) | -157.4380 | 501.3149 | ±1002.6298 | -0.314 | 0.7535 |  |
| Site: UW (vs UAB) | -899.8982 | 459.1530 | ±918.3059 | -1.960 | 0.0500 | . |
| **Age (years)** | **-113.5062** | 17.6828 | ±35.3657 | **-6.419** | **1.37e-10** | *** |
| **BMI (kg/m2)** | **-50.6516** | 24.9268 | ±49.8535 | **-2.032** | **0.0422** | * |
| Hypertension | +101.4236 | 426.3395 | ±852.6790 | +0.238 | 0.8120 |  |
| High cholesterol | -75.1943 | 382.7615 | ±765.5230 | -0.196 | 0.8443 |  |
| Kidney disease | -443.7339 | 816.0561 | ±1632.1123 | -0.544 | 0.5866 |  |
| Circulatory disease | -780.4535 | 710.5279 | ±1421.0557 | -1.098 | 0.2720 |  |
| Time 54-250, pooled (%) | -4485.7146 | 5239.1118 | ±10478.2235 | -0.856 | 0.3919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1804**, Adj R² = **0.1532**, F-statistic = **6.64** (p = **4.70e-10**), Residual SE = **3346.343** on **332** df, AIC = **6571.6**, BIC = **6617.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +800955.0706 | 635699.9652 | ±1271399.9304 | +1.260 | 0.2077 |  |
| Education: graduate level (vs college) | -618.0804 | 372.2763 | ±744.5526 | -1.660 | 0.0969 | . |
| Education: high school or below (vs college) | +1238.5605 | 904.9366 | ±1809.8733 | +1.369 | 0.1711 |  |
| Site: UCSD (vs UAB) | -174.0026 | 493.6892 | ±987.3784 | -0.352 | 0.7245 |  |
| **Site: UW (vs UAB)** | **-925.7235** | 458.7654 | ±917.5307 | **-2.018** | **0.0436** | * |
| **Age (years)** | **-113.4360** | 17.5931 | ±35.1862 | **-6.448** | **1.14e-10** | *** |
| **BMI (kg/m2)** | **-50.4691** | 25.1017 | ±50.2035 | **-2.011** | **0.0444** | * |
| Hypertension | +119.8387 | 427.4094 | ±854.8188 | +0.280 | 0.7792 |  |
| High cholesterol | -71.5712 | 381.5631 | ±763.1263 | -0.188 | 0.8512 |  |
| Kidney disease | -449.9066 | 817.6047 | ±1635.2095 | -0.550 | 0.5821 |  |
| Circulatory disease | -849.5480 | 718.5549 | ±1437.1099 | -1.182 | 0.2371 |  |
| Avg. daily time 54-250 (%) | -7823.1765 | 6357.8014 | ±12715.6028 | -1.230 | 0.2185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **344**, R² = **0.1753**, Adj R² = **0.1479**, F-statistic = **6.41** (p = **1.16e-09**), Residual SE = **3356.760** on **332** df, AIC = **6573.7**, BIC = **6619.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18403.4322** | 1389.1424 | ±2778.2847 | **+13.248** | **4.63e-40** | *** |
| Education: graduate level (vs college) | -603.2380 | 373.3772 | ±746.7544 | -1.616 | 0.1062 |  |
| Education: high school or below (vs college) | +1244.9737 | 905.0022 | ±1810.0045 | +1.376 | 0.1689 |  |
| Site: UCSD (vs UAB) | -224.5828 | 497.1124 | ±994.2248 | -0.452 | 0.6514 |  |
| **Site: UW (vs UAB)** | **-936.7647** | 456.1395 | ±912.2789 | **-2.054** | **0.0400** | * |
| **Age (years)** | **-113.6402** | 17.6685 | ±35.3369 | **-6.432** | **1.26e-10** | *** |
| BMI (kg/m2) | -47.2818 | 26.1495 | ±52.2991 | -1.808 | 0.0706 | . |
| Hypertension | +104.9141 | 429.1116 | ±858.2232 | +0.244 | 0.8069 |  |
| High cholesterol | -57.7917 | 384.2220 | ±768.4440 | -0.150 | 0.8804 |  |
| Kidney disease | -574.8923 | 847.7857 | ±1695.5714 | -0.678 | 0.4977 |  |
| Circulatory disease | -720.6989 | 697.0071 | ±1394.0141 | -1.034 | 0.3011 |  |
| Time 181-250, pooled (%) | +816.3458 | 669.6591 | ±1339.3183 | +1.219 | 0.2228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **344**, R² = **0.1766**, Adj R² = **0.1493**, F-statistic = **6.47** (p = **9.24e-10**), Residual SE = **3354.086** on **332** df, AIC = **6573.2**, BIC = **6619.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18345.4732** | 1369.9396 | ±2739.8791 | **+13.391** | **6.78e-41** | *** |
| Education: graduate level (vs college) | -602.8662 | 372.8705 | ±745.7409 | -1.617 | 0.1059 |  |
| Education: high school or below (vs college) | +1272.9950 | 904.9189 | ±1809.8378 | +1.407 | 0.1595 |  |
| Site: UCSD (vs UAB) | -208.5283 | 496.0308 | ±992.0616 | -0.420 | 0.6742 |  |
| **Site: UW (vs UAB)** | **-937.0499** | 455.7060 | ±911.4120 | **-2.056** | **0.0398** | * |
| **Age (years)** | **-112.3878** | 17.6612 | ±35.3224 | **-6.364** | **1.97e-10** | *** |
| BMI (kg/m2) | -48.0631 | 25.4720 | ±50.9439 | -1.887 | 0.0592 | . |
| Hypertension | +102.7486 | 429.3369 | ±858.6738 | +0.239 | 0.8109 |  |
| High cholesterol | -76.2895 | 382.4208 | ±764.8415 | -0.199 | 0.8419 |  |
| Kidney disease | -536.8013 | 839.0482 | ±1678.0964 | -0.640 | 0.5223 |  |
| Circulatory disease | -723.9933 | 694.6965 | ±1389.3929 | -1.042 | 0.2973 |  |
| Avg. daily time 181-250 (%) | +931.7457 | 655.2929 | ±1310.5857 | +1.422 | 0.1551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **344**, R² = **0.1752**, Adj R² = **0.1479**, F-statistic = **6.41** (p = **1.17e-09**), Residual SE = **3356.857** on **332** df, AIC = **6573.7**, BIC = **6619.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18402.7495** | 1389.8959 | ±2779.7919 | **+13.240** | **5.13e-40** | *** |
| Education: graduate level (vs college) | -602.5346 | 373.4020 | ±746.8040 | -1.614 | 0.1066 |  |
| Education: high school or below (vs college) | +1245.2413 | 904.9953 | ±1809.9906 | +1.376 | 0.1688 |  |
| Site: UCSD (vs UAB) | -224.5590 | 497.1155 | ±994.2311 | -0.452 | 0.6515 |  |
| **Site: UW (vs UAB)** | **-937.2099** | 456.1509 | ±912.3017 | **-2.055** | **0.0399** | * |
| **Age (years)** | **-113.6171** | 17.6700 | ±35.3399 | **-6.430** | **1.28e-10** | *** |
| BMI (kg/m2) | -47.2544 | 26.1511 | ±52.3022 | -1.807 | 0.0708 | . |
| Hypertension | +105.4257 | 429.1017 | ±858.2035 | +0.246 | 0.8059 |  |
| High cholesterol | -58.7878 | 384.1489 | ±768.2978 | -0.153 | 0.8784 |  |
| Kidney disease | -574.2131 | 847.5244 | ±1695.0489 | -0.678 | 0.4981 |  |
| Circulatory disease | -720.6141 | 697.0516 | ±1394.1032 | -1.034 | 0.3012 |  |
| Time > 180 (%) | +810.4722 | 668.2730 | ±1336.5460 | +1.213 | 0.2252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1765**, Adj R² = **0.1492**, F-statistic = **6.47** (p = **9.34e-10**), Residual SE = **3354.217** on **332** df, AIC = **6573.2**, BIC = **6619.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18344.5048** | 1370.8939 | ±2741.7878 | **+13.381** | **7.77e-41** | *** |
| Education: graduate level (vs college) | -601.9719 | 372.9253 | ±745.8505 | -1.614 | 0.1065 |  |
| Education: high school or below (vs college) | +1273.1866 | 904.9157 | ±1809.8314 | +1.407 | 0.1594 |  |
| Site: UCSD (vs UAB) | -208.6125 | 496.0384 | ±992.0769 | -0.421 | 0.6741 |  |
| **Site: UW (vs UAB)** | **-937.6169** | 455.7314 | ±911.4627 | **-2.057** | **0.0396** | * |
| **Age (years)** | **-112.3663** | 17.6646 | ±35.3293 | **-6.361** | **2.00e-10** | *** |
| BMI (kg/m2) | -48.0209 | 25.4774 | ±50.9548 | -1.885 | 0.0595 | . |
| Hypertension | +103.3554 | 429.3273 | ±858.6545 | +0.241 | 0.8098 |  |
| High cholesterol | -77.3757 | 382.3926 | ±764.7851 | -0.202 | 0.8396 |  |
| Kidney disease | -536.3576 | 838.8368 | ±1677.6735 | -0.639 | 0.5226 |  |
| Circulatory disease | -723.8677 | 694.7661 | ±1389.5322 | -1.042 | 0.2975 |  |
| Avg. daily time > 180 (%) | +924.7811 | 653.6312 | ±1307.2624 | +1.415 | 0.1571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1727**, Adj R² = **0.1453**, F-statistic = **6.30** (p = **1.82e-09**), Residual SE = **3361.904** on **332** df, AIC = **6574.8**, BIC = **6620.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18604.2241** | 1360.0921 | ±2720.1842 | **+13.679** | **1.36e-42** | *** |
| Education: graduate level (vs college) | -586.3072 | 375.3223 | ±750.6446 | -1.562 | 0.1183 |  |
| Education: high school or below (vs college) | +1204.7133 | 901.0546 | ±1802.1092 | +1.337 | 0.1812 |  |
| Site: UCSD (vs UAB) | -221.2556 | 496.3169 | ±992.6339 | -0.446 | 0.6557 |  |
| **Site: UW (vs UAB)** | **-945.1835** | 457.2677 | ±914.5354 | **-2.067** | **0.0387** | * |
| **Age (years)** | **-112.0033** | 18.0760 | ±36.1521 | **-6.196** | **5.78e-10** | *** |
| **BMI (kg/m2)** | **-50.4995** | 25.0427 | ±50.0854 | **-2.017** | **0.0437** | * |
| Hypertension | +121.0911 | 428.0730 | ±856.1460 | +0.283 | 0.7773 |  |
| High cholesterol | -97.6340 | 380.7022 | ±761.4045 | -0.256 | 0.7976 |  |
| Kidney disease | -524.7631 | 825.4026 | ±1650.8052 | -0.636 | 0.5249 |  |
| Circulatory disease | -712.6061 | 704.3712 | ±1408.7424 | -1.012 | 0.3117 |  |
| Nocturnal time > 180 (%) | +387.5554 | 642.6237 | ±1285.2473 | +0.603 | 0.5465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 344; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **344**, R² = **0.1751**, Adj R² = **0.1503**, F-statistic = **7.07** (p = **4.34e-10**), Residual SE = **11.394** on **333** df, AIC = **2661.0**, BIC = **2703.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2786** | 4.9053 | ±9.8106 | **+10.250** | **1.19e-24** | *** |
| Education: graduate level (vs college) | -1.6660 | 1.2709 | ±2.5419 | -1.311 | 0.1899 |  |
| Education: high school or below (vs college) | +3.0126 | 2.8710 | ±5.7420 | +1.049 | 0.2940 |  |
| Site: UCSD (vs UAB) | -1.2002 | 1.6694 | ±3.3388 | -0.719 | 0.4722 |  |
| Site: UW (vs UAB) | -2.6139 | 1.5944 | ±3.1889 | -1.639 | 0.1011 |  |
| **Age (years)** | **-0.4087** | 0.0599 | ±0.1198 | **-6.821** | **9.01e-12** | *** |
| BMI (kg/m2) | +0.0039 | 0.0892 | ±0.1784 | +0.044 | 0.9651 |  |
| Hypertension | +0.4195 | 1.4913 | ±2.9826 | +0.281 | 0.7785 |  |
| High cholesterol | -0.3162 | 1.3006 | ±2.6013 | -0.243 | 0.8079 |  |
| Kidney disease | -1.5600 | 2.6180 | ±5.2359 | -0.596 | 0.5512 |  |
| Circulatory disease | -1.8889 | 2.1948 | ±4.3897 | -0.861 | 0.3894 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **344**, R² = **0.1767**, Adj R² = **0.1494**, F-statistic = **6.48** (p = **9.00e-10**), Residual SE = **11.399** on **332** df, AIC = **2662.3**, BIC = **2708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.2250** | 12.7113 | ±25.4226 | **+3.243** | **0.0012** | ** |
| Education: graduate level (vs college) | -1.6350 | 1.2721 | ±2.5442 | -1.285 | 0.1987 |  |
| Education: high school or below (vs college) | +2.9656 | 2.8578 | ±5.7155 | +1.038 | 0.2994 |  |
| Site: UCSD (vs UAB) | -1.1047 | 1.6585 | ±3.3170 | -0.666 | 0.5053 |  |
| Site: UW (vs UAB) | -2.5121 | 1.5902 | ±3.1804 | -1.580 | 0.1142 |  |
| **Age (years)** | **-0.4142** | 0.0603 | ±0.1206 | **-6.868** | **6.49e-12** | *** |
| BMI (kg/m2) | -0.0036 | 0.0879 | ±0.1758 | -0.041 | 0.9670 |  |
| Hypertension | +0.3232 | 1.4944 | ±2.9888 | +0.216 | 0.8288 |  |
| High cholesterol | -0.5562 | 1.3401 | ±2.6802 | -0.415 | 0.6781 |  |
| Kidney disease | -1.4718 | 2.6327 | ±5.2654 | -0.559 | 0.5761 |  |
| Circulatory disease | -1.8168 | 2.2038 | ±4.4075 | -0.824 | 0.4097 |  |
| HbA1c (%) | +1.7465 | 2.2513 | ±4.5026 | +0.776 | 0.4379 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **344**, R² = **0.1756**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.09e-09**), Residual SE = **11.407** on **332** df, AIC = **2662.8**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8070** | 11.4773 | ±22.9547 | **+4.775** | **1.79e-06** | *** |
| Education: graduate level (vs college) | -1.6821 | 1.2734 | ±2.5468 | -1.321 | 0.1865 |  |
| Education: high school or below (vs college) | +2.9691 | 2.8692 | ±5.7385 | +1.035 | 0.3008 |  |
| Site: UCSD (vs UAB) | -1.1551 | 1.6890 | ±3.3780 | -0.684 | 0.4941 |  |
| Site: UW (vs UAB) | -2.5686 | 1.6120 | ±3.2241 | -1.593 | 0.1111 |  |
| **Age (years)** | **-0.4102** | 0.0600 | ±0.1200 | **-6.837** | **8.10e-12** | *** |
| BMI (kg/m2) | +0.0076 | 0.0906 | ±0.1812 | +0.084 | 0.9331 |  |
| Hypertension | +0.4828 | 1.5061 | ±3.0121 | +0.321 | 0.7486 |  |
| High cholesterol | -0.3438 | 1.3162 | ±2.6323 | -0.261 | 0.7940 |  |
| Kidney disease | -1.5486 | 2.6075 | ±5.2149 | -0.594 | 0.5526 |  |
| Circulatory disease | -1.8910 | 2.1974 | ±4.3948 | -0.861 | 0.3895 |  |
| Mean glucose (mg/dL) | -0.0401 | 0.0944 | ±0.1887 | -0.425 | 0.6712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **344**, R² = **0.1756**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.09e-09**), Residual SE = **11.407** on **332** df, AIC = **2662.8**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3504** | 23.9371 | ±47.8741 | **+2.521** | **0.0117** | * |
| Education: graduate level (vs college) | -1.6821 | 1.2734 | ±2.5468 | -1.321 | 0.1865 |  |
| Education: high school or below (vs college) | +2.9691 | 2.8692 | ±5.7385 | +1.035 | 0.3008 |  |
| Site: UCSD (vs UAB) | -1.1551 | 1.6890 | ±3.3780 | -0.684 | 0.4941 |  |
| Site: UW (vs UAB) | -2.5686 | 1.6120 | ±3.2241 | -1.593 | 0.1111 |  |
| **Age (years)** | **-0.4102** | 0.0600 | ±0.1200 | **-6.837** | **8.10e-12** | *** |
| BMI (kg/m2) | +0.0076 | 0.0906 | ±0.1812 | +0.084 | 0.9331 |  |
| Hypertension | +0.4828 | 1.5061 | ±3.0121 | +0.321 | 0.7486 |  |
| High cholesterol | -0.3438 | 1.3162 | ±2.6323 | -0.261 | 0.7940 |  |
| Kidney disease | -1.5486 | 2.6075 | ±5.2149 | -0.594 | 0.5526 |  |
| Circulatory disease | -1.8910 | 2.1974 | ±4.3948 | -0.861 | 0.3895 |  |
| GMI (%) | -1.6747 | 3.9449 | ±7.8897 | -0.425 | 0.6712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **344**, R² = **0.1751**, Adj R² = **0.1477**, F-statistic = **6.41** (p = **1.20e-09**), Residual SE = **11.411** on **332** df, AIC = **2663.0**, BIC = **2709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1423** | 9.3159 | ±18.6318 | **+5.382** | **7.35e-08** | *** |
| Education: graduate level (vs college) | -1.6641 | 1.2822 | ±2.5644 | -1.298 | 0.1943 |  |
| Education: high school or below (vs college) | +3.0145 | 2.8722 | ±5.7443 | +1.050 | 0.2939 |  |
| Site: UCSD (vs UAB) | -1.2037 | 1.6977 | ±3.3954 | -0.709 | 0.4783 |  |
| Site: UW (vs UAB) | -2.6163 | 1.6116 | ±3.2233 | -1.623 | 0.1045 |  |
| **Age (years)** | **-0.4085** | 0.0602 | ±0.1204 | **-6.783** | **1.17e-11** | *** |
| BMI (kg/m2) | +0.0036 | 0.0922 | ±0.1845 | +0.039 | 0.9687 |  |
| Hypertension | +0.4178 | 1.4967 | ±2.9934 | +0.279 | 0.7801 |  |
| High cholesterol | -0.3162 | 1.3060 | ±2.6121 | -0.242 | 0.8087 |  |
| Kidney disease | -1.5584 | 2.6225 | ±5.2450 | -0.594 | 0.5523 |  |
| Circulatory disease | -1.8880 | 2.1987 | ±4.3975 | -0.859 | 0.3905 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0012 | 0.0719 | ±0.1438 | +0.016 | 0.9870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1757**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.09e-09**), Residual SE = **11.407** on **332** df, AIC = **2662.7**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5353** | 6.6192 | ±13.2383 | **+7.937** | **2.07e-15** | *** |
| Education: graduate level (vs college) | -1.7247 | 1.2668 | ±2.5335 | -1.362 | 0.1733 |  |
| Education: high school or below (vs college) | +2.9680 | 2.8833 | ±5.7667 | +1.029 | 0.3033 |  |
| Site: UCSD (vs UAB) | -1.2736 | 1.6606 | ±3.3213 | -0.767 | 0.4431 |  |
| Site: UW (vs UAB) | -2.6663 | 1.6077 | ±3.2153 | -1.658 | 0.0972 | . |
| **Age (years)** | **-0.4084** | 0.0602 | ±0.1204 | **-6.785** | **1.16e-11** | *** |
| BMI (kg/m2) | +0.0060 | 0.0902 | ±0.1804 | +0.067 | 0.9469 |  |
| Hypertension | +0.4338 | 1.4924 | ±2.9849 | +0.291 | 0.7713 |  |
| High cholesterol | -0.3577 | 1.3176 | ±2.6351 | -0.271 | 0.7860 |  |
| Kidney disease | -1.4559 | 2.6014 | ±5.2029 | -0.560 | 0.5757 |  |
| Circulatory disease | -1.8732 | 2.2012 | ±4.4025 | -0.851 | 0.3948 |  |
| Glucose SD, pooled (mg/dL) | -0.1340 | 0.3048 | ±0.6097 | -0.440 | 0.6603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1773**, Adj R² = **0.1500**, F-statistic = **6.50** (p = **8.12e-10**), Residual SE = **11.395** on **332** df, AIC = **2662.1**, BIC = **2708.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3329** | 6.2184 | ±12.4367 | **+8.737** | **2.38e-18** | *** |
| Education: graduate level (vs college) | -1.7867 | 1.2733 | ±2.5465 | -1.403 | 0.1605 |  |
| Education: high school or below (vs college) | +2.9028 | 2.8895 | ±5.7789 | +1.005 | 0.3151 |  |
| Site: UCSD (vs UAB) | -1.3627 | 1.6568 | ±3.3136 | -0.823 | 0.4108 |  |
| Site: UW (vs UAB) | -2.7309 | 1.6085 | ±3.2169 | -1.698 | 0.0895 | . |
| **Age (years)** | **-0.4087** | 0.0601 | ±0.1201 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | +0.0102 | 0.0910 | ±0.1821 | +0.112 | 0.9108 |  |
| Hypertension | +0.4177 | 1.4933 | ±2.9867 | +0.280 | 0.7797 |  |
| High cholesterol | -0.3821 | 1.3095 | ±2.6191 | -0.292 | 0.7704 |  |
| Kidney disease | -1.3645 | 2.5818 | ±5.1635 | -0.529 | 0.5972 |  |
| Circulatory disease | -1.8856 | 2.2052 | ±4.4105 | -0.855 | 0.3925 |  |
| Avg. daily SD (mg/dL) | -0.2621 | 0.2852 | ±0.5704 | -0.919 | 0.3581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **344**, R² = **0.1754**, Adj R² = **0.1481**, F-statistic = **6.42** (p = **1.13e-09**), Residual SE = **11.408** on **332** df, AIC = **2662.8**, BIC = **2708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.9520** | 6.3313 | ±12.6626 | **+8.206** | **2.30e-16** | *** |
| Education: graduate level (vs college) | -1.7040 | 1.2696 | ±2.5393 | -1.342 | 0.1796 |  |
| Education: high school or below (vs college) | +2.9946 | 2.8858 | ±5.7716 | +1.038 | 0.2994 |  |
| Site: UCSD (vs UAB) | -1.2692 | 1.6656 | ±3.3313 | -0.762 | 0.4461 |  |
| Site: UW (vs UAB) | -2.6689 | 1.6112 | ±3.2223 | -1.656 | 0.0976 | . |
| **Age (years)** | **-0.4080** | 0.0602 | ±0.1205 | **-6.774** | **1.26e-11** | *** |
| BMI (kg/m2) | +0.0042 | 0.0894 | ±0.1787 | +0.047 | 0.9628 |  |
| Hypertension | +0.4083 | 1.5002 | ±3.0004 | +0.272 | 0.7855 |  |
| High cholesterol | -0.3392 | 1.3073 | ±2.6147 | -0.259 | 0.7953 |  |
| Kidney disease | -1.4899 | 2.6074 | ±5.2149 | -0.571 | 0.5677 |  |
| Circulatory disease | -1.8751 | 2.2012 | ±4.4024 | -0.852 | 0.3943 |  |
| CV (%) | -0.1118 | 0.2995 | ±0.5990 | -0.373 | 0.7088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **344**, R² = **0.1755**, Adj R² = **0.1482**, F-statistic = **6.43** (p = **1.11e-09**), Residual SE = **11.408** on **332** df, AIC = **2662.8**, BIC = **2708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4894** | 6.8458 | ±13.6915 | **+7.083** | **1.41e-12** | *** |
| Education: graduate level (vs college) | -1.7134 | 1.2713 | ±2.5426 | -1.348 | 0.1777 |  |
| Education: high school or below (vs college) | +2.9978 | 2.8881 | ±5.7761 | +1.038 | 0.2993 |  |
| Site: UCSD (vs UAB) | -1.2673 | 1.6656 | ±3.3313 | -0.761 | 0.4468 |  |
| Site: UW (vs UAB) | -2.6652 | 1.6099 | ±3.2198 | -1.655 | 0.0978 | . |
| **Age (years)** | **-0.4080** | 0.0602 | ±0.1204 | **-6.779** | **1.21e-11** | *** |
| BMI (kg/m2) | +0.0041 | 0.0892 | ±0.1785 | +0.046 | 0.9633 |  |
| Hypertension | +0.4148 | 1.4968 | ±2.9936 | +0.277 | 0.7817 |  |
| High cholesterol | -0.3447 | 1.3070 | ±2.6141 | -0.264 | 0.7920 |  |
| Kidney disease | -1.5019 | 2.6059 | ±5.2118 | -0.576 | 0.5644 |  |
| Circulatory disease | -1.8768 | 2.2017 | ±4.4034 | -0.852 | 0.3940 |  |
| Mean / SD ratio | +0.2633 | 0.6371 | ±1.2743 | +0.413 | 0.6794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1772**, Adj R² = **0.1499**, F-statistic = **6.50** (p = **8.26e-10**), Residual SE = **11.396** on **332** df, AIC = **2662.1**, BIC = **2708.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6350** | 6.5295 | ±13.0591 | **+7.142** | **9.19e-13** | *** |
| Education: graduate level (vs college) | -1.7749 | 1.2772 | ±2.5545 | -1.390 | 0.1646 |  |
| Education: high school or below (vs college) | +2.9610 | 2.8975 | ±5.7949 | +1.022 | 0.3068 |  |
| Site: UCSD (vs UAB) | -1.3726 | 1.6592 | ±3.3184 | -0.827 | 0.4081 |  |
| Site: UW (vs UAB) | -2.7376 | 1.6074 | ±3.2148 | -1.703 | 0.0885 | . |
| **Age (years)** | **-0.4078** | 0.0601 | ±0.1202 | **-6.788** | **1.14e-11** | *** |
| BMI (kg/m2) | +0.0078 | 0.0898 | ±0.1797 | +0.087 | 0.9308 |  |
| Hypertension | +0.3699 | 1.5016 | ±3.0032 | +0.246 | 0.8054 |  |
| High cholesterol | -0.3529 | 1.3022 | ±2.6043 | -0.271 | 0.7864 |  |
| Kidney disease | -1.4130 | 2.6024 | ±5.2049 | -0.543 | 0.5872 |  |
| Circulatory disease | -1.8869 | 2.2066 | ±4.4132 | -0.855 | 0.3925 |  |
| Avg. daily mean/SD | +0.4705 | 0.4949 | ±0.9897 | +0.951 | 0.3417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **344**, R² = **0.1820**, Adj R² = **0.1549**, F-statistic = **6.71** (p = **3.52e-10**), Residual SE = **11.363** on **332** df, AIC = **2660.1**, BIC = **2706.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.8820** | 6.4364 | ±12.8729 | **+6.662** | **2.69e-11** | *** |
| Education: graduate level (vs college) | -1.6649 | 1.2725 | ±2.5451 | -1.308 | 0.1908 |  |
| Education: high school or below (vs college) | +2.7412 | 2.8325 | ±5.6650 | +0.968 | 0.3332 |  |
| Site: UCSD (vs UAB) | -0.9706 | 1.6503 | ±3.3006 | -0.588 | 0.5565 |  |
| Site: UW (vs UAB) | -2.2712 | 1.6032 | ±3.2065 | -1.417 | 0.1566 |  |
| **Age (years)** | **-0.3954** | 0.0595 | ±0.1190 | **-6.648** | **2.97e-11** | *** |
| BMI (kg/m2) | +0.0148 | 0.0887 | ±0.1773 | +0.167 | 0.8677 |  |
| Hypertension | +0.5640 | 1.4931 | ±2.9861 | +0.378 | 0.7056 |  |
| High cholesterol | -0.4659 | 1.3067 | ±2.6134 | -0.357 | 0.7214 |  |
| Kidney disease | -1.9310 | 2.6004 | ±5.2008 | -0.743 | 0.4577 |  |
| Circulatory disease | -1.9728 | 2.2110 | ±4.4220 | -0.892 | 0.3723 |  |
| MAG (mg/dL/h) | +0.1800 | 0.1184 | ±0.2368 | +1.521 | 0.1284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **344**, R² = **0.1752**, Adj R² = **0.1478**, F-statistic = **6.41** (p = **1.18e-09**), Residual SE = **11.410** on **332** df, AIC = **2663.0**, BIC = **2709.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2185** | 7.0022 | ±14.0044 | **+7.315** | **2.58e-13** | *** |
| Education: graduate level (vs college) | -1.6763 | 1.2770 | ±2.5541 | -1.313 | 0.1893 |  |
| Education: high school or below (vs college) | +3.0014 | 2.8818 | ±5.7636 | +1.042 | 0.2976 |  |
| Site: UCSD (vs UAB) | -1.2270 | 1.6547 | ±3.3095 | -0.741 | 0.4584 |  |
| Site: UW (vs UAB) | -2.6363 | 1.6092 | ±3.2184 | -1.638 | 0.1014 |  |
| **Age (years)** | **-0.4090** | 0.0599 | ±0.1198 | **-6.826** | **8.76e-12** | *** |
| BMI (kg/m2) | +0.0026 | 0.0885 | ±0.1770 | +0.030 | 0.9762 |  |
| Hypertension | +0.4045 | 1.5057 | ±3.0113 | +0.269 | 0.7882 |  |
| High cholesterol | -0.3169 | 1.3054 | ±2.6108 | -0.243 | 0.8082 |  |
| Kidney disease | -1.5336 | 2.6125 | ±5.2250 | -0.587 | 0.5572 |  |
| Circulatory disease | -1.8774 | 2.2005 | ±4.4011 | -0.853 | 0.3936 |  |
| Avg. daily range (mg/dL) | -0.0107 | 0.0635 | ±0.1271 | -0.169 | 0.8658 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **344**, R² = **0.1778**, Adj R² = **0.1506**, F-statistic = **6.53** (p = **7.40e-10**), Residual SE = **11.392** on **332** df, AIC = **2661.8**, BIC = **2707.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6935** | 5.1252 | ±10.2503 | **+9.501** | **2.08e-21** | *** |
| Education: graduate level (vs college) | -1.7080 | 1.2827 | ±2.5654 | -1.332 | 0.1830 |  |
| Education: high school or below (vs college) | +2.9222 | 2.8899 | ±5.7798 | +1.011 | 0.3119 |  |
| Site: UCSD (vs UAB) | -1.1689 | 1.6667 | ±3.3334 | -0.701 | 0.4831 |  |
| Site: UW (vs UAB) | -2.6909 | 1.5964 | ±3.1928 | -1.686 | 0.0919 | . |
| **Age (years)** | **-0.4112** | 0.0599 | ±0.1198 | **-6.861** | **6.82e-12** | *** |
| BMI (kg/m2) | +0.0018 | 0.0895 | ±0.1791 | +0.020 | 0.9843 |  |
| Hypertension | +0.3154 | 1.4884 | ±2.9768 | +0.212 | 0.8322 |  |
| High cholesterol | -0.3134 | 1.3026 | ±2.6052 | -0.241 | 0.8098 |  |
| Kidney disease | -1.4764 | 2.6334 | ±5.2667 | -0.561 | 0.5750 |  |
| Circulatory disease | -1.9397 | 2.1981 | ±4.3962 | -0.882 | 0.3775 |  |
| SD of daily means (mg/dL) | +0.3679 | 0.4303 | ±0.8606 | +0.855 | 0.3926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **344**, R² = **0.1956**, Adj R² = **0.1690**, F-statistic = **7.34** (p = **2.95e-11**), Residual SE = **11.268** on **332** df, AIC = **2654.3**, BIC = **2700.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+650.4218** | 202.0902 | ±404.1803 | **+3.218** | **0.0013** | ** |
| Education: graduate level (vs college) | -1.5068 | 1.2634 | ±2.5269 | -1.193 | 0.2330 |  |
| Education: high school or below (vs college) | +3.2351 | 2.8155 | ±5.6309 | +1.149 | 0.2505 |  |
| Site: UCSD (vs UAB) | -0.8798 | 1.6383 | ±3.2765 | -0.537 | 0.5912 |  |
| Site: UW (vs UAB) | -2.3782 | 1.5623 | ±3.1247 | -1.522 | 0.1280 |  |
| **Age (years)** | **-0.4002** | 0.0593 | ±0.1186 | **-6.747** | **1.51e-11** | *** |
| BMI (kg/m2) | +0.0136 | 0.0997 | ±0.1994 | +0.136 | 0.8916 |  |
| Hypertension | +0.3744 | 1.4648 | ±2.9296 | +0.256 | 0.7982 |  |
| High cholesterol | -0.4487 | 1.2964 | ±2.5927 | -0.346 | 0.7292 |  |
| Kidney disease | -1.8601 | 2.7308 | ±5.4616 | -0.681 | 0.4958 |  |
| Circulatory disease | -1.9849 | 2.1837 | ±4.3674 | -0.909 | 0.3634 |  |
| **Time in range 70-180, pooled (%)** | **-6.0389** | 2.0288 | ±4.0576 | **-2.977** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **344**, R² = **0.1961**, Adj R² = **0.1695**, F-statistic = **7.36** (p = **2.69e-11**), Residual SE = **11.264** on **332** df, AIC = **2654.1**, BIC = **2700.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+639.9514** | 196.1649 | ±392.3299 | **+3.262** | **0.0011** | ** |
| Education: graduate level (vs college) | -1.4893 | 1.2575 | ±2.5149 | -1.184 | 0.2363 |  |
| Education: high school or below (vs college) | +3.3382 | 2.8133 | ±5.6265 | +1.187 | 0.2354 |  |
| Site: UCSD (vs UAB) | -0.9302 | 1.6286 | ±3.2572 | -0.571 | 0.5679 |  |
| Site: UW (vs UAB) | -2.5628 | 1.5603 | ±3.1206 | -1.643 | 0.1005 |  |
| **Age (years)** | **-0.3943** | 0.0586 | ±0.1172 | **-6.726** | **1.75e-11** | *** |
| BMI (kg/m2) | +0.0067 | 0.0918 | ±0.1836 | +0.073 | 0.9422 |  |
| Hypertension | +0.5879 | 1.4779 | ±2.9558 | +0.398 | 0.6908 |  |
| High cholesterol | -0.5049 | 1.2935 | ±2.5870 | -0.390 | 0.6963 |  |
| Kidney disease | -1.6044 | 2.7121 | ±5.4243 | -0.592 | 0.5541 |  |
| Circulatory disease | -2.1535 | 2.1688 | ±4.3376 | -0.993 | 0.3207 |  |
| **Avg. daily time in range 70-180 (%)** | **-5.9314** | 1.9659 | ±3.9317 | **-3.017** | **0.0026** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1757**, Adj R² = **0.1484**, F-statistic = **6.43** (p = **1.08e-09**), Residual SE = **11.406** on **332** df, AIC = **2662.7**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0795** | 4.9586 | ±9.9171 | **+10.100** | **5.55e-24** | *** |
| Education: graduate level (vs college) | -1.6552 | 1.2772 | ±2.5543 | -1.296 | 0.1950 |  |
| Education: high school or below (vs college) | +3.0383 | 2.8792 | ±5.7584 | +1.055 | 0.2913 |  |
| Site: UCSD (vs UAB) | -1.0756 | 1.6771 | ±3.3543 | -0.641 | 0.5213 |  |
| Site: UW (vs UAB) | -2.5399 | 1.5982 | ±3.1964 | -1.589 | 0.1120 |  |
| **Age (years)** | **-0.4088** | 0.0601 | ±0.1202 | **-6.800** | **1.04e-11** | *** |
| BMI (kg/m2) | +0.0039 | 0.0892 | ±0.1784 | +0.044 | 0.9649 |  |
| Hypertension | +0.3764 | 1.4995 | ±2.9990 | +0.251 | 0.8018 |  |
| High cholesterol | -0.3084 | 1.3046 | ±2.6091 | -0.236 | 0.8131 |  |
| Kidney disease | -1.4740 | 2.6383 | ±5.2767 | -0.559 | 0.5764 |  |
| Circulatory disease | -1.9403 | 2.2091 | ±4.4182 | -0.878 | 0.3798 |  |
| Any reading < 54 during wear (0/1) | +0.8244 | 1.6050 | ±3.2100 | +0.514 | 0.6075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1816**, Adj R² = **0.1545**, F-statistic = **6.70** (p = **3.78e-10**), Residual SE = **11.366** on **332** df, AIC = **2660.3**, BIC = **2706.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8725** | 4.8976 | ±9.7953 | **+10.183** | **2.36e-24** | *** |
| Education: graduate level (vs college) | -1.6385 | 1.2769 | ±2.5538 | -1.283 | 0.1994 |  |
| Education: high school or below (vs college) | +3.2390 | 2.8818 | ±5.7637 | +1.124 | 0.2610 |  |
| Site: UCSD (vs UAB) | -0.8998 | 1.6759 | ±3.3518 | -0.537 | 0.5913 |  |
| Site: UW (vs UAB) | -2.4632 | 1.5921 | ±3.1841 | -1.547 | 0.1218 |  |
| **Age (years)** | **-0.4045** | 0.0597 | ±0.1194 | **-6.774** | **1.26e-11** | *** |
| BMI (kg/m2) | -0.0067 | 0.0866 | ±0.1733 | -0.077 | 0.9386 |  |
| Hypertension | +0.2511 | 1.4869 | ±2.9738 | +0.169 | 0.8659 |  |
| High cholesterol | -0.2811 | 1.3005 | ±2.6011 | -0.216 | 0.8289 |  |
| Kidney disease | -1.3453 | 2.6319 | ±5.2638 | -0.511 | 0.6093 |  |
| Circulatory disease | -2.1617 | 2.2610 | ±4.5220 | -0.956 | 0.3390 |  |
| Time < 54 (%) | +19.1344 | 17.7204 | ±35.4407 | +1.080 | 0.2802 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1865**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.58e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0206** | 4.8767 | ±9.7534 | **+10.257** | **1.10e-24** | *** |
| Education: graduate level (vs college) | -1.7337 | 1.2632 | ±2.5264 | -1.373 | 0.1699 |  |
| Education: high school or below (vs college) | +3.1158 | 2.8578 | ±5.7157 | +1.090 | 0.2756 |  |
| Site: UCSD (vs UAB) | -0.9931 | 1.6562 | ±3.3123 | -0.600 | 0.5487 |  |
| Site: UW (vs UAB) | -2.5677 | 1.5919 | ±3.1839 | -1.613 | 0.1068 |  |
| **Age (years)** | **-0.4052** | 0.0593 | ±0.1185 | **-6.837** | **8.11e-12** | *** |
| BMI (kg/m2) | -0.0057 | 0.0875 | ±0.1750 | -0.065 | 0.9483 |  |
| Hypertension | +0.3329 | 1.4812 | ±2.9625 | +0.225 | 0.8222 |  |
| High cholesterol | -0.2535 | 1.2940 | ±2.5880 | -0.196 | 0.8447 |  |
| Kidney disease | -1.3914 | 2.6332 | ±5.2663 | -0.528 | 0.5972 |  |
| Circulatory disease | -2.4041 | 2.2917 | ±4.5833 | -1.049 | 0.2942 |  |
| Avg. daily time < 54 (%) | +30.2267 | 21.7597 | ±43.5193 | +1.389 | 0.1648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1796**, Adj R² = **0.1524**, F-statistic = **6.61** (p = **5.36e-10**), Residual SE = **11.379** on **332** df, AIC = **2661.1**, BIC = **2707.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4081** | 4.9530 | ±9.9059 | **+9.975** | **1.95e-23** | *** |
| Education: graduate level (vs college) | -1.5836 | 1.2754 | ±2.5507 | -1.242 | 0.2144 |  |
| Education: high school or below (vs college) | +2.9031 | 2.8625 | ±5.7250 | +1.014 | 0.3105 |  |
| Site: UCSD (vs UAB) | -1.0461 | 1.6505 | ±3.3011 | -0.634 | 0.5262 |  |
| Site: UW (vs UAB) | -2.4415 | 1.5896 | ±3.1792 | -1.536 | 0.1246 |  |
| **Age (years)** | **-0.4091** | 0.0598 | ±0.1197 | **-6.835** | **8.19e-12** | *** |
| BMI (kg/m2) | +0.0076 | 0.0897 | ±0.1794 | +0.084 | 0.9327 |  |
| Hypertension | +0.6221 | 1.4911 | ±2.9823 | +0.417 | 0.6765 |  |
| High cholesterol | -0.5427 | 1.3355 | ±2.6709 | -0.406 | 0.6844 |  |
| Kidney disease | -1.3857 | 2.5984 | ±5.1969 | -0.533 | 0.5938 |  |
| Circulatory disease | -1.8747 | 2.2103 | ±4.4206 | -0.848 | 0.3963 |  |
| Time 54-69, pooled (%) | +4.6779 | 3.4353 | ±6.8706 | +1.362 | 0.1733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **344**, R² = **0.1779**, Adj R² = **0.1506**, F-statistic = **6.53** (p = **7.34e-10**), Residual SE = **11.391** on **332** df, AIC = **2661.8**, BIC = **2707.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7169** | 4.9136 | ±9.8273 | **+10.118** | **4.59e-24** | *** |
| Education: graduate level (vs college) | -1.5729 | 1.2737 | ±2.5474 | -1.235 | 0.2169 |  |
| Education: high school or below (vs college) | +2.9338 | 2.8711 | ±5.7423 | +1.022 | 0.3069 |  |
| Site: UCSD (vs UAB) | -1.1349 | 1.6572 | ±3.3143 | -0.685 | 0.4935 |  |
| Site: UW (vs UAB) | -2.5673 | 1.5937 | ±3.1874 | -1.611 | 0.1072 |  |
| **Age (years)** | **-0.4092** | 0.0598 | ±0.1196 | **-6.842** | **7.78e-12** | *** |
| BMI (kg/m2) | +0.0054 | 0.0896 | ±0.1793 | +0.060 | 0.9518 |  |
| Hypertension | +0.6810 | 1.5159 | ±3.0318 | +0.449 | 0.6532 |  |
| High cholesterol | -0.4479 | 1.3310 | ±2.6620 | -0.337 | 0.7365 |  |
| Kidney disease | -1.4408 | 2.6193 | ±5.2386 | -0.550 | 0.5823 |  |
| Circulatory disease | -1.9631 | 2.2109 | ±4.4219 | -0.888 | 0.3746 |  |
| Avg. daily time 54-69 (%) | +3.7211 | 3.5306 | ±7.0613 | +1.054 | 0.2919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **344**, R² = **0.1816**, Adj R² = **0.1545**, F-statistic = **6.70** (p = **3.78e-10**), Residual SE = **11.366** on **332** df, AIC = **2660.3**, BIC = **2706.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2503** | 4.9549 | ±9.9098 | **+9.940** | **2.80e-23** | *** |
| Education: graduate level (vs college) | -1.5715 | 1.2768 | ±2.5535 | -1.231 | 0.2184 |  |
| Education: high school or below (vs college) | +2.9552 | 2.8582 | ±5.7164 | +1.034 | 0.3012 |  |
| Site: UCSD (vs UAB) | -0.9590 | 1.6480 | ±3.2959 | -0.582 | 0.5606 |  |
| Site: UW (vs UAB) | -2.3920 | 1.5871 | ±3.1742 | -1.507 | 0.1318 |  |
| **Age (years)** | **-0.4080** | 0.0598 | ±0.1195 | **-6.826** | **8.71e-12** | *** |
| BMI (kg/m2) | +0.0051 | 0.0891 | ±0.1783 | +0.057 | 0.9548 |  |
| Hypertension | +0.5907 | 1.4906 | ±2.9812 | +0.396 | 0.6919 |  |
| High cholesterol | -0.5473 | 1.3323 | ±2.6645 | -0.411 | 0.6812 |  |
| Kidney disease | -1.3195 | 2.5997 | ±5.1994 | -0.508 | 0.6118 |  |
| Circulatory disease | -1.9446 | 2.2277 | ±4.4554 | -0.873 | 0.3827 |  |
| Time < 70 (%) | +4.9604 | 3.3134 | ±6.6269 | +1.497 | 0.1344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **344**, R² = **0.1801**, Adj R² = **0.1530**, F-statistic = **6.63** (p = **4.89e-10**), Residual SE = **11.376** on **332** df, AIC = **2660.9**, BIC = **2707.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5601** | 4.9078 | ±9.8155 | **+10.098** | **5.62e-24** | *** |
| Education: graduate level (vs college) | -1.5634 | 1.2764 | ±2.5528 | -1.225 | 0.2206 |  |
| Education: high school or below (vs college) | +2.9326 | 2.8646 | ±5.7293 | +1.024 | 0.3060 |  |
| Site: UCSD (vs UAB) | -1.0902 | 1.6515 | ±3.3030 | -0.660 | 0.5092 |  |
| Site: UW (vs UAB) | -2.5506 | 1.5913 | ±3.1826 | -1.603 | 0.1090 |  |
| **Age (years)** | **-0.4089** | 0.0597 | ±0.1193 | **-6.853** | **7.23e-12** | *** |
| BMI (kg/m2) | +0.0043 | 0.0895 | ±0.1790 | +0.048 | 0.9616 |  |
| Hypertension | +0.7232 | 1.5182 | ±3.0363 | +0.476 | 0.6338 |  |
| High cholesterol | -0.4663 | 1.3266 | ±2.6531 | -0.352 | 0.7252 |  |
| Kidney disease | -1.3905 | 2.6195 | ±5.2391 | -0.531 | 0.5955 |  |
| Circulatory disease | -2.0556 | 2.2276 | ±4.4552 | -0.923 | 0.3561 |  |
| Avg. daily time < 70 (%) | +4.5053 | 3.4745 | ±6.9489 | +1.297 | 0.1947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1816**, Adj R² = **0.1545**, F-statistic = **6.70** (p = **3.75e-10**), Residual SE = **11.365** on **332** df, AIC = **2660.2**, BIC = **2706.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1961.2092 | 1757.3670 | ±3514.7339 | +1.116 | 0.2644 |  |
| Education: graduate level (vs college) | -1.6211 | 1.2802 | ±2.5605 | -1.266 | 0.2054 |  |
| Education: high school or below (vs college) | +3.2517 | 2.8828 | ±5.7656 | +1.128 | 0.2593 |  |
| Site: UCSD (vs UAB) | -0.8990 | 1.6768 | ±3.3535 | -0.536 | 0.5919 |  |
| Site: UW (vs UAB) | -2.4746 | 1.5922 | ±3.1845 | -1.554 | 0.1201 |  |
| **Age (years)** | **-0.4038** | 0.0597 | ±0.1195 | **-6.760** | **1.38e-11** | *** |
| BMI (kg/m2) | -0.0058 | 0.0868 | ±0.1736 | -0.067 | 0.9464 |  |
| Hypertension | +0.2575 | 1.4872 | ±2.9743 | +0.173 | 0.8626 |  |
| High cholesterol | -0.3010 | 1.3020 | ±2.6040 | -0.231 | 0.8172 |  |
| Kidney disease | -1.3431 | 2.6320 | ±5.2640 | -0.510 | 0.6098 |  |
| Circulatory disease | -2.1600 | 2.2618 | ±4.5236 | -0.955 | 0.3396 |  |
| Time 54-250, pooled (%) | -19.1141 | 17.5785 | ±35.1571 | -1.087 | 0.2769 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1864**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.58e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3041.5028 | 2140.6400 | ±4281.2800 | +1.421 | 0.1554 |  |
| Education: graduate level (vs college) | -1.7027 | 1.2653 | ±2.5305 | -1.346 | 0.1784 |  |
| Education: high school or below (vs college) | +3.1371 | 2.8581 | ±5.7162 | +1.098 | 0.2724 |  |
| Site: UCSD (vs UAB) | -0.9932 | 1.6570 | ±3.3139 | -0.599 | 0.5489 |  |
| Site: UW (vs UAB) | -2.5876 | 1.5935 | ±3.1869 | -1.624 | 0.1044 |  |
| **Age (years)** | **-0.4040** | 0.0593 | ±0.1186 | **-6.815** | **9.45e-12** | *** |
| BMI (kg/m2) | -0.0041 | 0.0878 | ±0.1757 | -0.047 | 0.9624 |  |
| Hypertension | +0.3445 | 1.4820 | ±2.9639 | +0.232 | 0.8162 |  |
| High cholesterol | -0.2887 | 1.2956 | ±2.5912 | -0.223 | 0.8237 |  |
| Kidney disease | -1.3889 | 2.6331 | ±5.2662 | -0.527 | 0.5979 |  |
| Circulatory disease | -2.3965 | 2.2920 | ±4.5839 | -1.046 | 0.2958 |  |
| Avg. daily time 54-250 (%) | -29.9161 | 21.4091 | ±42.8181 | -1.397 | 0.1623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **344**, R² = **0.1838**, Adj R² = **0.1567**, F-statistic = **6.80** (p = **2.55e-10**), Residual SE = **11.350** on **332** df, AIC = **2659.3**, BIC = **2705.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5733** | 5.1450 | ±10.2900 | **+9.441** | **3.70e-21** | *** |
| Education: graduate level (vs college) | -1.6393 | 1.2712 | ±2.5424 | -1.290 | 0.1972 |  |
| Education: high school or below (vs college) | +3.2118 | 2.8535 | ±5.7070 | +1.126 | 0.2604 |  |
| Site: UCSD (vs UAB) | -1.1821 | 1.6712 | ±3.3425 | -0.707 | 0.4794 |  |
| Site: UW (vs UAB) | -2.6352 | 1.5808 | ±3.1616 | -1.667 | 0.0955 | . |
| **Age (years)** | **-0.4035** | 0.0598 | ±0.1196 | **-6.746** | **1.52e-11** | *** |
| BMI (kg/m2) | +0.0094 | 0.0969 | ±0.1939 | +0.097 | 0.9224 |  |
| Hypertension | +0.2430 | 1.4801 | ±2.9602 | +0.164 | 0.8696 |  |
| High cholesterol | -0.2091 | 1.3089 | ±2.6179 | -0.160 | 0.8731 |  |
| Kidney disease | -1.9701 | 2.7240 | ±5.4481 | -0.723 | 0.4695 |  |
| Circulatory disease | -1.9087 | 2.1657 | ±4.3315 | -0.881 | 0.3781 |  |
| Time 181-250, pooled (%) | +4.1714 | 2.2280 | ±4.4560 | +1.872 | 0.0612 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **344**, R² = **0.1865**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.57e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3009** | 4.9413 | ±9.8826 | **+9.775** | **1.44e-22** | *** |
| Education: graduate level (vs college) | -1.6377 | 1.2668 | ±2.5336 | -1.293 | 0.1961 |  |
| Education: high school or below (vs college) | +3.3509 | 2.8483 | ±5.6966 | +1.176 | 0.2394 |  |
| Site: UCSD (vs UAB) | -1.1012 | 1.6607 | ±3.3213 | -0.663 | 0.5072 |  |
| Site: UW (vs UAB) | -2.6364 | 1.5754 | ±3.1508 | -1.673 | 0.0942 | . |
| **Age (years)** | **-0.3972** | 0.0594 | ±0.1188 | **-6.685** | **2.30e-11** | *** |
| BMI (kg/m2) | +0.0054 | 0.0913 | ±0.1827 | +0.059 | 0.9526 |  |
| Hypertension | +0.2342 | 1.4821 | ±2.9643 | +0.158 | 0.8744 |  |
| High cholesterol | -0.3037 | 1.2987 | ±2.5974 | -0.234 | 0.8151 |  |
| Kidney disease | -1.7729 | 2.6920 | ±5.3840 | -0.659 | 0.5102 |  |
| Circulatory disease | -1.9251 | 2.1541 | ±4.3081 | -0.894 | 0.3715 |  |
| **Avg. daily time 181-250 (%)** | **+4.7044** | 2.1745 | ±4.3490 | **+2.163** | **0.0305** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **344**, R² = **0.1838**, Adj R² = **0.1567**, F-statistic = **6.80** (p = **2.55e-10**), Residual SE = **11.350** on **332** df, AIC = **2659.3**, BIC = **2705.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5586** | 5.1497 | ±10.2993 | **+9.429** | **4.12e-21** | *** |
| Education: graduate level (vs college) | -1.6355 | 1.2712 | ±2.5423 | -1.287 | 0.1982 |  |
| Education: high school or below (vs college) | +3.2144 | 2.8534 | ±5.7069 | +1.127 | 0.2599 |  |
| Site: UCSD (vs UAB) | -1.1818 | 1.6713 | ±3.3426 | -0.707 | 0.4795 |  |
| Site: UW (vs UAB) | -2.6377 | 1.5808 | ±3.1616 | -1.669 | 0.0952 | . |
| **Age (years)** | **-0.4033** | 0.0598 | ±0.1196 | **-6.743** | **1.55e-11** | *** |
| BMI (kg/m2) | +0.0096 | 0.0970 | ±0.1940 | +0.099 | 0.9210 |  |
| Hypertension | +0.2445 | 1.4801 | ±2.9602 | +0.165 | 0.8688 |  |
| High cholesterol | -0.2135 | 1.3085 | ±2.6169 | -0.163 | 0.8704 |  |
| Kidney disease | -1.9693 | 2.7239 | ±5.4477 | -0.723 | 0.4697 |  |
| Circulatory disease | -1.9084 | 2.1660 | ±4.3319 | -0.881 | 0.3783 |  |
| Time > 180 (%) | +4.1685 | 2.2229 | ±4.4458 | +1.875 | 0.0608 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1865**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.57e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2838** | 4.9456 | ±9.8911 | **+9.763** | **1.62e-22** | *** |
| Education: graduate level (vs college) | -1.6330 | 1.2667 | ±2.5335 | -1.289 | 0.1974 |  |
| Education: high school or below (vs college) | +3.3539 | 2.8482 | ±5.6965 | +1.178 | 0.2390 |  |
| Site: UCSD (vs UAB) | -1.1010 | 1.6607 | ±3.3215 | -0.663 | 0.5073 |  |
| Site: UW (vs UAB) | -2.6394 | 1.5754 | ±3.1509 | -1.675 | 0.0939 | . |
| **Age (years)** | **-0.3971** | 0.0594 | ±0.1189 | **-6.681** | **2.37e-11** | *** |
| BMI (kg/m2) | +0.0057 | 0.0914 | ±0.1828 | +0.062 | 0.9506 |  |
| Hypertension | +0.2361 | 1.4822 | ±2.9643 | +0.159 | 0.8734 |  |
| High cholesterol | -0.3092 | 1.2983 | ±2.5967 | -0.238 | 0.8118 |  |
| Kidney disease | -1.7719 | 2.6918 | ±5.3836 | -0.658 | 0.5104 |  |
| Circulatory disease | -1.9247 | 2.1543 | ±4.3087 | -0.893 | 0.3716 |  |
| **Avg. daily time > 180 (%)** | **+4.6981** | 2.1679 | ±4.3359 | **+2.167** | **0.0302** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1786**, Adj R² = **0.1514**, F-statistic = **6.56** (p = **6.45e-10**), Residual SE = **11.386** on **332** df, AIC = **2661.5**, BIC = **2707.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5422** | 4.8325 | ±9.6650 | **+10.252** | **1.16e-24** | *** |
| Education: graduate level (vs college) | -1.5432 | 1.2713 | ±2.5425 | -1.214 | 0.2248 |  |
| Education: high school or below (vs college) | +3.0055 | 2.8396 | ±5.6792 | +1.058 | 0.2899 |  |
| Site: UCSD (vs UAB) | -1.1621 | 1.6660 | ±3.3320 | -0.698 | 0.4855 |  |
| Site: UW (vs UAB) | -2.6837 | 1.5912 | ±3.1823 | -1.687 | 0.0917 | . |
| **Age (years)** | **-0.3940** | 0.0603 | ±0.1207 | **-6.530** | **6.57e-11** | *** |
| BMI (kg/m2) | -0.0079 | 0.0888 | ±0.1776 | -0.089 | 0.9290 |  |
| Hypertension | +0.3178 | 1.4795 | ±2.9590 | +0.215 | 0.8299 |  |
| High cholesterol | -0.4208 | 1.2909 | ±2.5817 | -0.326 | 0.7445 |  |
| Kidney disease | -1.7269 | 2.6441 | ±5.2883 | -0.653 | 0.5137 |  |
| Circulatory disease | -1.8655 | 2.2206 | ±4.4412 | -0.840 | 0.4008 |  |
| Nocturnal time > 180 (%) | +2.1469 | 2.1711 | ±4.3422 | +0.989 | 0.3227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 346; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1548**, F-statistic = **7.32** (p = **1.70e-10**), Residual SE = **6.667** on **335** df, AIC = **2305.5**, BIC = **2347.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8265** | 3.9998 | ±7.9996 | **+15.707** | **1.35e-55** | *** |
| **Education: graduate level (vs college)** | **-1.7812** | 0.7764 | ±1.5528 | **-2.294** | **0.0218** | * |
| Education: high school or below (vs college) | -1.8761 | 1.3420 | ±2.6841 | -1.398 | 0.1621 |  |
| **Site: UCSD (vs UAB)** | **-1.9760** | 0.9762 | ±1.9524 | **-2.024** | **0.0430** | * |
| **Site: UW (vs UAB)** | **-2.5729** | 0.8831 | ±1.7662 | **-2.913** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0368 | ±0.0736 | **-3.624** | **2.91e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0812 | ±0.1624 | **+3.159** | **0.0016** | ** |
| Hypertension | +0.9457 | 0.8421 | ±1.6841 | +1.123 | 0.2614 |  |
| High cholesterol | -0.2784 | 0.8174 | ±1.6347 | -0.341 | 0.7334 |  |
| Kidney disease | +0.0608 | 2.1902 | ±4.3805 | +0.028 | 0.9779 |  |
| Circulatory disease | -0.6757 | 1.0045 | ±2.0091 | -0.673 | 0.5012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **346**, R² = **0.1795**, Adj R² = **0.1525**, F-statistic = **6.64** (p = **4.64e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.0521** | 7.4315 | ±14.8629 | **+8.215** | **2.12e-16** | *** |
| **Education: graduate level (vs college)** | **-1.7737** | 0.7754 | ±1.5508 | **-2.288** | **0.0222** | * |
| Education: high school or below (vs college) | -1.8839 | 1.3441 | ±2.6882 | -1.402 | 0.1610 |  |
| **Site: UCSD (vs UAB)** | **-1.9599** | 0.9729 | ±1.9458 | **-2.015** | **0.0440** | * |
| **Site: UW (vs UAB)** | **-2.5534** | 0.8841 | ±1.7682 | **-2.888** | **0.0039** | ** |
| **Age (years)** | **-0.1343** | 0.0375 | ±0.0750 | **-3.584** | **3.39e-04** | *** |
| **BMI (kg/m2)** | **+0.2548** | 0.0825 | ±0.1650 | **+3.089** | **0.0020** | ** |
| Hypertension | +0.9273 | 0.8464 | ±1.6928 | +1.096 | 0.2732 |  |
| High cholesterol | -0.3247 | 0.8222 | ±1.6443 | -0.395 | 0.6929 |  |
| Kidney disease | +0.0786 | 2.1899 | ±4.3798 | +0.036 | 0.9714 |  |
| Circulatory disease | -0.6616 | 1.0059 | ±2.0118 | -0.658 | 0.5107 |  |
| HbA1c (%) | +0.3423 | 1.3523 | ±2.7046 | +0.253 | 0.8002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8864** | 7.3543 | ±14.7085 | **+8.551** | **1.22e-17** | *** |
| **Education: graduate level (vs college)** | **-1.7814** | 0.7777 | ±1.5554 | **-2.291** | **0.0220** | * |
| Education: high school or below (vs college) | -1.8767 | 1.3525 | ±2.7050 | -1.388 | 0.1653 |  |
| **Site: UCSD (vs UAB)** | **-1.9754** | 0.9822 | ±1.9643 | **-2.011** | **0.0443** | * |
| **Site: UW (vs UAB)** | **-2.5723** | 0.8834 | ±1.7668 | **-2.912** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0372 | ±0.0743 | **-3.588** | **3.34e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0815 | ±0.1630 | **+3.147** | **0.0016** | ** |
| Hypertension | +0.9466 | 0.8443 | ±1.6886 | +1.121 | 0.2622 |  |
| High cholesterol | -0.2787 | 0.8264 | ±1.6528 | -0.337 | 0.7359 |  |
| Kidney disease | +0.0609 | 2.2101 | ±4.4202 | +0.028 | 0.9780 |  |
| Circulatory disease | -0.6757 | 1.0061 | ±2.0122 | -0.672 | 0.5018 |  |
| Mean glucose (mg/dL) | -0.0005 | 0.0521 | ±0.1042 | -0.010 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9596** | 13.9642 | ±27.9285 | **+4.509** | **6.52e-06** | *** |
| **Education: graduate level (vs college)** | **-1.7814** | 0.7777 | ±1.5554 | **-2.291** | **0.0220** | * |
| Education: high school or below (vs college) | -1.8767 | 1.3525 | ±2.7050 | -1.388 | 0.1653 |  |
| **Site: UCSD (vs UAB)** | **-1.9754** | 0.9822 | ±1.9643 | **-2.011** | **0.0443** | * |
| **Site: UW (vs UAB)** | **-2.5723** | 0.8834 | ±1.7668 | **-2.912** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0372 | ±0.0743 | **-3.588** | **3.34e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0815 | ±0.1630 | **+3.147** | **0.0016** | ** |
| Hypertension | +0.9466 | 0.8443 | ±1.6886 | +1.121 | 0.2622 |  |
| High cholesterol | -0.2787 | 0.8264 | ±1.6528 | -0.337 | 0.7359 |  |
| Kidney disease | +0.0609 | 2.2101 | ±4.4202 | +0.028 | 0.9780 |  |
| Circulatory disease | -0.6757 | 1.0061 | ±2.0122 | -0.672 | 0.5018 |  |
| GMI (%) | -0.0221 | 2.1772 | ±4.3544 | -0.010 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **346**, R² = **0.1805**, Adj R² = **0.1536**, F-statistic = **6.69** (p = **3.83e-10**), Residual SE = **6.672** on **334** df, AIC = **2307.0**, BIC = **2353.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.5751** | 5.8841 | ±11.7681 | **+10.125** | **4.29e-24** | *** |
| **Education: graduate level (vs college)** | **-1.7401** | 0.7709 | ±1.5418 | **-2.257** | **0.0240** | * |
| Education: high school or below (vs college) | -1.8341 | 1.3428 | ±2.6856 | -1.366 | 0.1720 |  |
| **Site: UCSD (vs UAB)** | **-2.0530** | 0.9932 | ±1.9865 | **-2.067** | **0.0387** | * |
| **Site: UW (vs UAB)** | **-2.6303** | 0.8877 | ±1.7753 | **-2.963** | **0.0030** | ** |
| **Age (years)** | **-0.1292** | 0.0375 | ±0.0749 | **-3.449** | **5.62e-04** | *** |
| **BMI (kg/m2)** | **+0.2502** | 0.0821 | ±0.1642 | **+3.047** | **0.0023** | ** |
| Hypertension | +0.9062 | 0.8372 | ±1.6743 | +1.082 | 0.2791 |  |
| High cholesterol | -0.2789 | 0.8211 | ±1.6421 | -0.340 | 0.7341 |  |
| Kidney disease | +0.0988 | 2.2025 | ±4.4050 | +0.045 | 0.9642 |  |
| Circulatory disease | -0.6525 | 1.0022 | ±2.0045 | -0.651 | 0.5150 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0281 | 0.0410 | ±0.0820 | +0.684 | 0.4937 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1794**, Adj R² = **0.1523**, F-statistic = **6.64** (p = **4.73e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3639** | 4.9353 | ±9.8707 | **+12.636** | **1.33e-36** | *** |
| **Education: graduate level (vs college)** | **-1.7688** | 0.7762 | ±1.5525 | **-2.279** | **0.0227** | * |
| Education: high school or below (vs college) | -1.8673 | 1.3444 | ±2.6889 | -1.389 | 0.1649 |  |
| **Site: UCSD (vs UAB)** | **-1.9620** | 0.9779 | ±1.9558 | **-2.006** | **0.0448** | * |
| **Site: UW (vs UAB)** | **-2.5638** | 0.8849 | ±1.7697 | **-2.897** | **0.0038** | ** |
| **Age (years)** | **-0.1334** | 0.0369 | ±0.0738 | **-3.616** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2561** | 0.0814 | ±0.1628 | **+3.146** | **0.0017** | ** |
| Hypertension | +0.9414 | 0.8427 | ±1.6854 | +1.117 | 0.2640 |  |
| High cholesterol | -0.2689 | 0.8378 | ±1.6756 | -0.321 | 0.7482 |  |
| Kidney disease | +0.0386 | 2.2679 | ±4.5359 | +0.017 | 0.9864 |  |
| Circulatory disease | -0.6797 | 1.0037 | ±2.0073 | -0.677 | 0.4983 |  |
| Glucose SD, pooled (mg/dL) | +0.0274 | 0.1776 | ±0.3552 | +0.154 | 0.8772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1794**, Adj R² = **0.1523**, F-statistic = **6.64** (p = **4.72e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3702** | 4.6800 | ±9.3599 | **+13.327** | **1.61e-40** | *** |
| **Education: graduate level (vs college)** | **-1.7672** | 0.7760 | ±1.5520 | **-2.277** | **0.0228** | * |
| Education: high school or below (vs college) | -1.8641 | 1.3445 | ±2.6891 | -1.386 | 0.1656 |  |
| **Site: UCSD (vs UAB)** | **-1.9590** | 0.9761 | ±1.9523 | **-2.007** | **0.0448** | * |
| **Site: UW (vs UAB)** | **-2.5617** | 0.8848 | ±1.7695 | **-2.895** | **0.0038** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.613** | **3.03e-04** | *** |
| **BMI (kg/m2)** | **+0.2558** | 0.0817 | ±0.1634 | **+3.132** | **0.0017** | ** |
| Hypertension | +0.9443 | 0.8440 | ±1.6880 | +1.119 | 0.2632 |  |
| High cholesterol | -0.2698 | 0.8325 | ±1.6651 | -0.324 | 0.7459 |  |
| Kidney disease | +0.0378 | 2.2562 | ±4.5125 | +0.017 | 0.9866 |  |
| Circulatory disease | -0.6769 | 1.0051 | ±2.0102 | -0.673 | 0.5006 |  |
| Avg. daily SD (mg/dL) | +0.0295 | 0.1719 | ±0.3438 | +0.171 | 0.8639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.78e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5812** | 4.6178 | ±9.2356 | **+13.552** | **7.69e-42** | *** |
| **Education: graduate level (vs college)** | **-1.7754** | 0.7769 | ±1.5539 | **-2.285** | **0.0223** | * |
| Education: high school or below (vs college) | -1.8736 | 1.3430 | ±2.6861 | -1.395 | 0.1630 |  |
| **Site: UCSD (vs UAB)** | **-1.9666** | 0.9782 | ±1.9564 | **-2.010** | **0.0444** | * |
| **Site: UW (vs UAB)** | **-2.5657** | 0.8824 | ±1.7647 | **-2.908** | **0.0036** | ** |
| **Age (years)** | **-0.1334** | 0.0369 | ±0.0739 | **-3.611** | **3.05e-04** | *** |
| **BMI (kg/m2)** | **+0.2564** | 0.0812 | ±0.1625 | **+3.156** | **0.0016** | ** |
| Hypertension | +0.9467 | 0.8452 | ±1.6904 | +1.120 | 0.2627 |  |
| High cholesterol | -0.2744 | 0.8284 | ±1.6568 | -0.331 | 0.7404 |  |
| Kidney disease | +0.0501 | 2.2350 | ±4.4700 | +0.022 | 0.9821 |  |
| Circulatory disease | -0.6781 | 1.0037 | ±2.0073 | -0.676 | 0.4993 |  |
| CV (%) | +0.0164 | 0.1712 | ±0.3423 | +0.096 | 0.9238 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7889** | 4.6964 | ±9.3928 | **+13.370** | **9.11e-41** | *** |
| **Education: graduate level (vs college)** | **-1.7823** | 0.7788 | ±1.5575 | **-2.289** | **0.0221** | * |
| Education: high school or below (vs college) | -1.8765 | 1.3446 | ±2.6892 | -1.396 | 0.1628 |  |
| **Site: UCSD (vs UAB)** | **-1.9772** | 0.9793 | ±1.9586 | **-2.019** | **0.0435** | * |
| **Site: UW (vs UAB)** | **-2.5738** | 0.8836 | ±1.7673 | **-2.913** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.613** | **3.02e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0813 | ±0.1625 | **+3.156** | **0.0016** | ** |
| Hypertension | +0.9458 | 0.8440 | ±1.6881 | +1.121 | 0.2625 |  |
| High cholesterol | -0.2791 | 0.8295 | ±1.6590 | -0.336 | 0.7365 |  |
| Kidney disease | +0.0621 | 2.2236 | ±4.4472 | +0.028 | 0.9777 |  |
| Circulatory disease | -0.6754 | 1.0044 | ±2.0088 | -0.672 | 0.5013 |  |
| Mean / SD ratio | +0.0055 | 0.3430 | ±0.6859 | +0.016 | 0.9871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9665** | 4.6440 | ±9.2879 | **+13.559** | **7.03e-42** | *** |
| **Education: graduate level (vs college)** | **-1.7766** | 0.7785 | ±1.5569 | **-2.282** | **0.0225** | * |
| Education: high school or below (vs college) | -1.8741 | 1.3438 | ±2.6877 | -1.395 | 0.1631 |  |
| **Site: UCSD (vs UAB)** | **-1.9703** | 0.9781 | ±1.9562 | **-2.014** | **0.0440** | * |
| **Site: UW (vs UAB)** | **-2.5691** | 0.8819 | ±1.7639 | **-2.913** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.615** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2563** | 0.0815 | ±0.1630 | **+3.145** | **0.0017** | ** |
| Hypertension | +0.9469 | 0.8465 | ±1.6931 | +1.119 | 0.2633 |  |
| High cholesterol | -0.2763 | 0.8249 | ±1.6498 | -0.335 | 0.7377 |  |
| Kidney disease | +0.0547 | 2.2209 | ±4.4418 | +0.025 | 0.9803 |  |
| Circulatory disease | -0.6762 | 1.0056 | ±2.0112 | -0.672 | 0.5013 |  |
| Avg. daily mean/SD | -0.0181 | 0.2705 | ±0.5410 | -0.067 | 0.9466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **346**, R² = **0.1862**, Adj R² = **0.1594**, F-statistic = **6.95** (p = **1.37e-10**), Residual SE = **6.648** on **334** df, AIC = **2304.6**, BIC = **2350.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4647** | 4.7913 | ±9.5826 | **+12.202** | **3.02e-34** | *** |
| **Education: graduate level (vs college)** | **-1.7791** | 0.7790 | ±1.5580 | **-2.284** | **0.0224** | * |
| Education: high school or below (vs college) | -2.0366 | 1.3003 | ±2.6007 | -1.566 | 0.1173 |  |
| Site: UCSD (vs UAB) | -1.8442 | 0.9719 | ±1.9438 | -1.898 | 0.0578 | . |
| **Site: UW (vs UAB)** | **-2.3756** | 0.8973 | ±1.7947 | **-2.647** | **0.0081** | ** |
| **Age (years)** | **-0.1254** | 0.0372 | ±0.0743 | **-3.375** | **7.38e-04** | *** |
| **BMI (kg/m2)** | **+0.2629** | 0.0797 | ±0.1594 | **+3.299** | **9.72e-04** | *** |
| Hypertension | +1.0271 | 0.8392 | ±1.6783 | +1.224 | 0.2210 |  |
| High cholesterol | -0.3637 | 0.8160 | ±1.6321 | -0.446 | 0.6559 |  |
| Kidney disease | -0.1601 | 2.2028 | ±4.4056 | -0.073 | 0.9420 |  |
| Circulatory disease | -0.7272 | 1.0048 | ±2.0096 | -0.724 | 0.4693 |  |
| MAG (mg/dL/h) | +0.1061 | 0.0692 | ±0.1384 | +1.534 | 0.1251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.76e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.1829** | 5.3169 | ±10.6338 | **+11.883** | **1.44e-32** | *** |
| **Education: graduate level (vs college)** | **-1.7855** | 0.7801 | ±1.5602 | **-2.289** | **0.0221** | * |
| Education: high school or below (vs college) | -1.8803 | 1.3496 | ±2.6991 | -1.393 | 0.1635 |  |
| **Site: UCSD (vs UAB)** | **-1.9851** | 0.9823 | ±1.9646 | **-2.021** | **0.0433** | * |
| **Site: UW (vs UAB)** | **-2.5802** | 0.8915 | ±1.7831 | **-2.894** | **0.0038** | ** |
| **Age (years)** | **-0.1335** | 0.0370 | ±0.0739 | **-3.610** | **3.06e-04** | *** |
| **BMI (kg/m2)** | **+0.2560** | 0.0817 | ±0.1635 | **+3.132** | **0.0017** | ** |
| Hypertension | +0.9411 | 0.8504 | ±1.7008 | +1.107 | 0.2684 |  |
| High cholesterol | -0.2794 | 0.8221 | ±1.6442 | -0.340 | 0.7339 |  |
| Kidney disease | +0.0714 | 2.2241 | ±4.4483 | +0.032 | 0.9744 |  |
| Circulatory disease | -0.6708 | 1.0045 | ±2.0089 | -0.668 | 0.5042 |  |
| Avg. daily range (mg/dL) | -0.0041 | 0.0359 | ±0.0718 | -0.113 | 0.9098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **346**, R² = **0.1888**, Adj R² = **0.1621**, F-statistic = **7.07** (p = **8.50e-11**), Residual SE = **6.638** on **334** df, AIC = **2303.5**, BIC = **2349.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.0891** | 3.9770 | ±7.9539 | **+15.361** | **3.00e-53** | *** |
| **Education: graduate level (vs college)** | **-1.8332** | 0.7729 | ±1.5457 | **-2.372** | **0.0177** | * |
| Education: high school or below (vs college) | -1.9812 | 1.3507 | ±2.7014 | -1.467 | 0.1424 |  |
| **Site: UCSD (vs UAB)** | **-1.9305** | 0.9694 | ±1.9387 | **-1.992** | **0.0464** | * |
| **Site: UW (vs UAB)** | **-2.6553** | 0.8718 | ±1.7437 | **-3.046** | **0.0023** | ** |
| **Age (years)** | **-0.1364** | 0.0361 | ±0.0722 | **-3.776** | **1.59e-04** | *** |
| **BMI (kg/m2)** | **+0.2548** | 0.0801 | ±0.1602 | **+3.181** | **0.0015** | ** |
| Hypertension | +0.8299 | 0.8447 | ±1.6894 | +0.982 | 0.3259 |  |
| High cholesterol | -0.2784 | 0.8120 | ±1.6241 | -0.343 | 0.7317 |  |
| Kidney disease | +0.1506 | 2.1573 | ±4.3146 | +0.070 | 0.9444 |  |
| Circulatory disease | -0.7310 | 1.0149 | ±2.0299 | -0.720 | 0.4714 |  |
| SD of daily means (mg/dL) | +0.4033 | 0.2205 | ±0.4411 | +1.829 | 0.0674 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **346**, R² = **0.1802**, Adj R² = **0.1532**, F-statistic = **6.67** (p = **4.06e-10**), Residual SE = **6.673** on **334** df, AIC = **2307.2**, BIC = **2353.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +137.2208 | 128.5758 | ±257.1516 | +1.067 | 0.2859 |  |
| **Education: graduate level (vs college)** | **-1.7610** | 0.7861 | ±1.5723 | **-2.240** | **0.0251** | * |
| Education: high school or below (vs college) | -1.8495 | 1.3379 | ±2.6759 | -1.382 | 0.1669 |  |
| Site: UCSD (vs UAB) | -1.9380 | 0.9896 | ±1.9793 | -1.958 | 0.0502 | . |
| **Site: UW (vs UAB)** | **-2.5471** | 0.8881 | ±1.7761 | **-2.868** | **0.0041** | ** |
| **Age (years)** | **-0.1322** | 0.0372 | ±0.0744 | **-3.556** | **3.76e-04** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0846 | ±0.1693 | **+3.045** | **0.0023** | ** |
| Hypertension | +0.9369 | 0.8402 | ±1.6805 | +1.115 | 0.2648 |  |
| High cholesterol | -0.2928 | 0.8140 | ±1.6280 | -0.360 | 0.7191 |  |
| Kidney disease | +0.0216 | 2.2176 | ±4.4352 | +0.010 | 0.9922 |  |
| Circulatory disease | -0.6892 | 1.0016 | ±2.0032 | -0.688 | 0.4914 |  |
| Time in range 70-180, pooled (%) | -0.7486 | 1.3000 | ±2.5999 | -0.576 | 0.5647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **346**, R² = **0.1822**, Adj R² = **0.1552**, F-statistic = **6.76** (p = **2.85e-10**), Residual SE = **6.665** on **334** df, AIC = **2306.3**, BIC = **2352.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +190.5311 | 116.3264 | ±232.6528 | +1.638 | 0.1014 |  |
| **Education: graduate level (vs college)** | **-1.7436** | 0.7800 | ±1.5599 | **-2.235** | **0.0254** | * |
| Education: high school or below (vs college) | -1.8086 | 1.3252 | ±2.6504 | -1.365 | 0.1723 |  |
| **Site: UCSD (vs UAB)** | **-1.9175** | 0.9739 | ±1.9477 | **-1.969** | **0.0490** | * |
| **Site: UW (vs UAB)** | **-2.5668** | 0.8822 | ±1.7644 | **-2.909** | **0.0036** | ** |
| **Age (years)** | **-0.1302** | 0.0368 | ±0.0737 | **-3.535** | **4.08e-04** | *** |
| **BMI (kg/m2)** | **+0.2574** | 0.0821 | ±0.1641 | **+3.136** | **0.0017** | ** |
| Hypertension | +0.9768 | 0.8419 | ±1.6837 | +1.160 | 0.2460 |  |
| High cholesterol | -0.3168 | 0.8111 | ±1.6223 | -0.391 | 0.6961 |  |
| Kidney disease | +0.0477 | 2.1982 | ±4.3964 | +0.022 | 0.9827 |  |
| Circulatory disease | -0.7354 | 0.9944 | ±1.9887 | -0.740 | 0.4596 |  |
| Avg. daily time in range 70-180 (%) | -1.2846 | 1.1693 | ±2.3387 | -1.099 | 0.2720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1796**, Adj R² = **0.1525**, F-statistic = **6.64** (p = **4.58e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.4**, BIC = **2353.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7505** | 3.9932 | ±7.9865 | **+15.714** | **1.21e-55** | *** |
| **Education: graduate level (vs college)** | **-1.7769** | 0.7790 | ±1.5580 | **-2.281** | **0.0225** | * |
| Education: high school or below (vs college) | -1.8665 | 1.3472 | ±2.6944 | -1.385 | 0.1659 |  |
| **Site: UCSD (vs UAB)** | **-1.9291** | 0.9818 | ±1.9637 | **-1.965** | **0.0494** | * |
| **Site: UW (vs UAB)** | **-2.5455** | 0.8894 | ±1.7787 | **-2.862** | **0.0042** | ** |
| **Age (years)** | **-0.1334** | 0.0368 | ±0.0737 | **-3.620** | **2.94e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0810 | ±0.1621 | **+3.165** | **0.0016** | ** |
| Hypertension | +0.9288 | 0.8469 | ±1.6939 | +1.097 | 0.2728 |  |
| High cholesterol | -0.2750 | 0.8188 | ±1.6375 | -0.336 | 0.7370 |  |
| Kidney disease | +0.0932 | 2.1961 | ±4.3923 | +0.042 | 0.9662 |  |
| Circulatory disease | -0.6956 | 1.0093 | ±2.0187 | -0.689 | 0.4907 |  |
| Any reading < 54 during wear (0/1) | +0.3138 | 0.8932 | ±1.7864 | +0.351 | 0.7254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1862**, Adj R² = **0.1594**, F-statistic = **6.95** (p = **1.37e-10**), Residual SE = **6.648** on **334** df, AIC = **2304.6**, BIC = **2350.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5794** | 3.9144 | ±7.8288 | **+15.987** | **1.58e-57** | *** |
| **Education: graduate level (vs college)** | **-1.7652** | 0.7736 | ±1.5473 | **-2.282** | **0.0225** | * |
| Education: high school or below (vs college) | -1.7401 | 1.3498 | ±2.6996 | -1.289 | 0.1973 |  |
| Site: UCSD (vs UAB) | -1.7928 | 0.9778 | ±1.9557 | -1.833 | 0.0667 | . |
| **Site: UW (vs UAB)** | **-2.4830** | 0.8770 | ±1.7539 | **-2.831** | **0.0046** | ** |
| **Age (years)** | **-0.1308** | 0.0366 | ±0.0731 | **-3.579** | **3.45e-04** | *** |
| **BMI (kg/m2)** | **+0.2502** | 0.0793 | ±0.1586 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.8414 | 0.8461 | ±1.6922 | +0.994 | 0.3200 |  |
| High cholesterol | -0.2564 | 0.8157 | ±1.6314 | -0.314 | 0.7533 |  |
| Kidney disease | +0.1899 | 2.1957 | ±4.3914 | +0.086 | 0.9311 |  |
| Circulatory disease | -0.8422 | 1.0181 | ±2.0361 | -0.827 | 0.4081 |  |
| **Time < 54 (%)** | **+11.6204** | 5.7971 | ±11.5942 | **+2.005** | **0.0450** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1811**, Adj R² = **0.1541**, F-statistic = **6.71** (p = **3.49e-10**), Residual SE = **6.670** on **334** df, AIC = **2306.8**, BIC = **2353.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7666** | 3.9720 | ±7.9440 | **+15.802** | **3.00e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7971** | 0.7782 | ±1.5563 | **-2.309** | **0.0209** | * |
| Education: high school or below (vs college) | -1.8527 | 1.3384 | ±2.6769 | -1.384 | 0.1663 |  |
| **Site: UCSD (vs UAB)** | **-1.9277** | 0.9781 | ±1.9562 | **-1.971** | **0.0487** | * |
| **Site: UW (vs UAB)** | **-2.5627** | 0.8838 | ±1.7675 | **-2.900** | **0.0037** | ** |
| **Age (years)** | **-0.1325** | 0.0367 | ±0.0734 | **-3.610** | **3.07e-04** | *** |
| **BMI (kg/m2)** | **+0.2543** | 0.0806 | ±0.1612 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.9250 | 0.8428 | ±1.6857 | +1.098 | 0.2724 |  |
| High cholesterol | -0.2636 | 0.8190 | ±1.6380 | -0.322 | 0.7475 |  |
| Kidney disease | +0.0994 | 2.1938 | ±4.3876 | +0.045 | 0.9638 |  |
| Circulatory disease | -0.7953 | 1.0216 | ±2.0433 | -0.778 | 0.4363 |  |
| Avg. daily time < 54 (%) | +7.0047 | 8.5989 | ±17.1978 | +0.815 | 0.4153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8465** | 3.9892 | ±7.9785 | **+15.754** | **6.45e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7832** | 0.7834 | ±1.5668 | **-2.276** | **0.0228** | * |
| Education: high school or below (vs college) | -1.8737 | 1.3466 | ±2.6933 | -1.391 | 0.1641 |  |
| **Site: UCSD (vs UAB)** | **-1.9792** | 0.9772 | ±1.9545 | **-2.025** | **0.0428** | * |
| **Site: UW (vs UAB)** | **-2.5767** | 0.8865 | ±1.7730 | **-2.907** | **0.0037** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.615** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2564** | 0.0812 | ±0.1624 | **+3.158** | **0.0016** | ** |
| Hypertension | +0.9412 | 0.8495 | ±1.6990 | +1.108 | 0.2679 |  |
| High cholesterol | -0.2733 | 0.8255 | ±1.6511 | -0.331 | 0.7406 |  |
| Kidney disease | +0.0569 | 2.2012 | ±4.4023 | +0.026 | 0.9794 |  |
| Circulatory disease | -0.6759 | 1.0070 | ±2.0141 | -0.671 | 0.5021 |  |
| Time 54-69, pooled (%) | -0.1069 | 1.8678 | ±3.7356 | -0.057 | 0.9544 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **346**, R² = **0.1794**, Adj R² = **0.1523**, F-statistic = **6.64** (p = **4.73e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8807** | 3.9834 | ±7.9669 | **+15.785** | **3.92e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7902** | 0.7812 | ±1.5625 | **-2.292** | **0.0219** | * |
| Education: high school or below (vs college) | -1.8684 | 1.3506 | ±2.7012 | -1.383 | 0.1666 |  |
| **Site: UCSD (vs UAB)** | **-1.9821** | 0.9755 | ±1.9510 | **-2.032** | **0.0422** | * |
| **Site: UW (vs UAB)** | **-2.5768** | 0.8855 | ±1.7711 | **-2.910** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.610** | **3.06e-04** | *** |
| **BMI (kg/m2)** | **+0.2563** | 0.0812 | ±0.1625 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.9212 | 0.8640 | ±1.7281 | +1.066 | 0.2864 |  |
| High cholesterol | -0.2660 | 0.8267 | ±1.6535 | -0.322 | 0.7476 |  |
| Kidney disease | +0.0497 | 2.2050 | ±4.4100 | +0.023 | 0.9820 |  |
| Circulatory disease | -0.6683 | 1.0015 | ±2.0030 | -0.667 | 0.5046 |  |
| Avg. daily time 54-69 (%) | -0.3576 | 1.9303 | ±3.8605 | -0.185 | 0.8530 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **346**, R² = **0.1797**, Adj R² = **0.1526**, F-statistic = **6.65** (p = **4.49e-10**), Residual SE = **6.675** on **334** df, AIC = **2307.4**, BIC = **2353.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6823** | 3.9710 | ±7.9420 | **+15.785** | **3.94e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7672** | 0.7833 | ±1.5665 | **-2.256** | **0.0241** | * |
| Education: high school or below (vs college) | -1.8839 | 1.3430 | ±2.6860 | -1.403 | 0.1607 |  |
| **Site: UCSD (vs UAB)** | **-1.9440** | 0.9753 | ±1.9505 | **-1.993** | **0.0462** | * |
| **Site: UW (vs UAB)** | **-2.5434** | 0.8839 | ±1.7677 | **-2.878** | **0.0040** | ** |
| **Age (years)** | **-0.1332** | 0.0368 | ±0.0736 | **-3.621** | **2.93e-04** | *** |
| **BMI (kg/m2)** | **+0.2566** | 0.0809 | ±0.1619 | **+3.171** | **0.0015** | ** |
| Hypertension | +0.9687 | 0.8459 | ±1.6918 | +1.145 | 0.2522 |  |
| High cholesterol | -0.3096 | 0.8247 | ±1.6495 | -0.375 | 0.7073 |  |
| Kidney disease | +0.0939 | 2.1964 | ±4.3929 | +0.043 | 0.9659 |  |
| Circulatory disease | -0.6841 | 1.0060 | ±2.0119 | -0.680 | 0.4965 |  |
| Time < 70 (%) | +0.6938 | 1.6553 | ±3.3107 | +0.419 | 0.6751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8170** | 3.9797 | ±7.9594 | **+15.784** | **3.98e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7799** | 0.7810 | ±1.5619 | **-2.279** | **0.0227** | * |
| Education: high school or below (vs college) | -1.8772 | 1.3480 | ±2.6961 | -1.393 | 0.1637 |  |
| **Site: UCSD (vs UAB)** | **-1.9746** | 0.9745 | ±1.9490 | **-2.026** | **0.0427** | * |
| **Site: UW (vs UAB)** | **-2.5722** | 0.8854 | ±1.7708 | **-2.905** | **0.0037** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.615** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0812 | ±0.1624 | **+3.158** | **0.0016** | ** |
| Hypertension | +0.9497 | 0.8596 | ±1.7192 | +1.105 | 0.2693 |  |
| High cholesterol | -0.2803 | 0.8247 | ±1.6493 | -0.340 | 0.7339 |  |
| Kidney disease | +0.0630 | 2.2006 | ±4.4012 | +0.029 | 0.9772 |  |
| Circulatory disease | -0.6780 | 1.0002 | ±2.0004 | -0.678 | 0.4979 |  |
| Avg. daily time < 70 (%) | +0.0595 | 1.7262 | ±3.4524 | +0.034 | 0.9725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1847**, Adj R² = **0.1578**, F-statistic = **6.88** (p = **1.82e-10**), Residual SE = **6.655** on **334** df, AIC = **2305.3**, BIC = **2351.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1081.7476 | 607.7249 | ±1215.4498 | +1.780 | 0.0751 | . |
| **Education: graduate level (vs college)** | **-1.7578** | 0.7755 | ±1.5510 | **-2.267** | **0.0234** | * |
| Education: high school or below (vs college) | -1.7499 | 1.3500 | ±2.7000 | -1.296 | 0.1949 |  |
| Site: UCSD (vs UAB) | -1.8147 | 0.9782 | ±1.9563 | -1.855 | 0.0636 | . |
| **Site: UW (vs UAB)** | **-2.5001** | 0.8785 | ±1.7571 | **-2.846** | **0.0044** | ** |
| **Age (years)** | **-0.1308** | 0.0366 | ±0.0732 | **-3.570** | **3.57e-04** | *** |
| **BMI (kg/m2)** | **+0.2514** | 0.0798 | ±0.1596 | **+3.151** | **0.0016** | ** |
| Hypertension | +0.8576 | 0.8464 | ±1.6928 | +1.013 | 0.3110 |  |
| High cholesterol | -0.2697 | 0.8181 | ±1.6362 | -0.330 | 0.7417 |  |
| Kidney disease | +0.1753 | 2.1964 | ±4.3927 | +0.080 | 0.9364 |  |
| Circulatory disease | -0.8210 | 1.0175 | ±2.0349 | -0.807 | 0.4197 |  |
| Time 54-250, pooled (%) | -10.1918 | 6.0748 | ±12.1497 | -1.678 | 0.0934 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1801**, Adj R² = **0.1531**, F-statistic = **6.67** (p = **4.12e-10**), Residual SE = **6.673** on **334** df, AIC = **2307.2**, BIC = **2353.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +542.3622 | 966.3427 | ±1932.6855 | +0.561 | 0.5746 |  |
| **Education: graduate level (vs college)** | **-1.7873** | 0.7799 | ±1.5598 | **-2.292** | **0.0219** | * |
| Education: high school or below (vs college) | -1.8565 | 1.3401 | ±2.6803 | -1.385 | 0.1660 |  |
| **Site: UCSD (vs UAB)** | **-1.9426** | 0.9781 | ±1.9562 | **-1.986** | **0.0470** | * |
| **Site: UW (vs UAB)** | **-2.5691** | 0.8860 | ±1.7720 | **-2.900** | **0.0037** | ** |
| **Age (years)** | **-0.1326** | 0.0368 | ±0.0735 | **-3.607** | **3.10e-04** | *** |
| **BMI (kg/m2)** | **+0.2552** | 0.0810 | ±0.1619 | **+3.152** | **0.0016** | ** |
| Hypertension | +0.9333 | 0.8445 | ±1.6890 | +1.105 | 0.2691 |  |
| High cholesterol | -0.2738 | 0.8206 | ±1.6411 | -0.334 | 0.7386 |  |
| Kidney disease | +0.0879 | 2.1936 | ±4.3871 | +0.040 | 0.9680 |  |
| Circulatory disease | -0.7572 | 1.0250 | ±2.0499 | -0.739 | 0.4600 |  |
| Avg. daily time 54-250 (%) | -4.7960 | 9.6614 | ±19.3229 | -0.496 | 0.6196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **346**, R² = **0.1797**, Adj R² = **0.1527**, F-statistic = **6.65** (p = **4.46e-10**), Residual SE = **6.675** on **334** df, AIC = **2307.4**, BIC = **2353.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6102** | 4.2918 | ±8.5836 | **+14.588** | **3.34e-48** | *** |
| **Education: graduate level (vs college)** | **-1.7781** | 0.7814 | ±1.5628 | **-2.275** | **0.0229** | * |
| Education: high school or below (vs college) | -1.8518 | 1.3452 | ±2.6905 | -1.377 | 0.1686 |  |
| **Site: UCSD (vs UAB)** | **-1.9735** | 0.9835 | ±1.9670 | **-2.007** | **0.0448** | * |
| **Site: UW (vs UAB)** | **-2.5769** | 0.8860 | ±1.7721 | **-2.908** | **0.0036** | ** |
| **Age (years)** | **-0.1327** | 0.0374 | ±0.0747 | **-3.552** | **3.83e-04** | *** |
| **BMI (kg/m2)** | **+0.2573** | 0.0848 | ±0.1696 | **+3.034** | **0.0024** | ** |
| Hypertension | +0.9219 | 0.8431 | ±1.6861 | +1.093 | 0.2742 |  |
| High cholesterol | -0.2642 | 0.8315 | ±1.6631 | -0.318 | 0.7507 |  |
| Kidney disease | +0.0079 | 2.2539 | ±4.5077 | +0.003 | 0.9972 |  |
| Circulatory disease | -0.6789 | 1.0033 | ±2.0065 | -0.677 | 0.4986 |  |
| Time 181-250, pooled (%) | +0.5283 | 1.4455 | ±2.8910 | +0.365 | 0.7148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **346**, R² = **0.1828**, Adj R² = **0.1559**, F-statistic = **6.79** (p = **2.57e-10**), Residual SE = **6.663** on **334** df, AIC = **2306.1**, BIC = **2352.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.1848** | 4.1234 | ±8.2469 | **+15.081** | **2.17e-51** | *** |
| **Education: graduate level (vs college)** | **-1.7729** | 0.7797 | ±1.5593 | **-2.274** | **0.0230** | * |
| Education: high school or below (vs college) | -1.7690 | 1.3305 | ±2.6610 | -1.330 | 0.1837 |  |
| **Site: UCSD (vs UAB)** | **-1.9431** | 0.9780 | ±1.9561 | **-1.987** | **0.0469** | * |
| **Site: UW (vs UAB)** | **-2.5835** | 0.8830 | ±1.7661 | **-2.926** | **0.0034** | ** |
| **Age (years)** | **-0.1297** | 0.0372 | ±0.0744 | **-3.484** | **4.94e-04** | *** |
| **BMI (kg/m2)** | **+0.2572** | 0.0826 | ±0.1652 | **+3.115** | **0.0018** | ** |
| Hypertension | +0.8818 | 0.8397 | ±1.6794 | +1.050 | 0.2937 |  |
| High cholesterol | -0.2729 | 0.8201 | ±1.6402 | -0.333 | 0.7393 |  |
| Kidney disease | -0.0108 | 2.2261 | ±4.4521 | -0.005 | 0.9961 |  |
| Circulatory disease | -0.6891 | 0.9958 | ±1.9916 | -0.692 | 0.4889 |  |
| Avg. daily time 181-250 (%) | +1.5242 | 1.3514 | ±2.7028 | +1.128 | 0.2594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **346**, R² = **0.1796**, Adj R² = **0.1526**, F-statistic = **6.65** (p = **4.51e-10**), Residual SE = **6.675** on **334** df, AIC = **2307.4**, BIC = **2353.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6282** | 4.2885 | ±8.5770 | **+14.604** | **2.66e-48** | *** |
| **Education: graduate level (vs college)** | **-1.7779** | 0.7814 | ±1.5629 | **-2.275** | **0.0229** | * |
| Education: high school or below (vs college) | -1.8537 | 1.3460 | ±2.6920 | -1.377 | 0.1684 |  |
| **Site: UCSD (vs UAB)** | **-1.9737** | 0.9834 | ±1.9667 | **-2.007** | **0.0447** | * |
| **Site: UW (vs UAB)** | **-2.5768** | 0.8860 | ±1.7719 | **-2.908** | **0.0036** | ** |
| **Age (years)** | **-0.1327** | 0.0374 | ±0.0747 | **-3.553** | **3.81e-04** | *** |
| **BMI (kg/m2)** | **+0.2572** | 0.0847 | ±0.1694 | **+3.037** | **0.0024** | ** |
| Hypertension | +0.9242 | 0.8433 | ±1.6866 | +1.096 | 0.2731 |  |
| High cholesterol | -0.2660 | 0.8313 | ±1.6625 | -0.320 | 0.7490 |  |
| Kidney disease | +0.0128 | 2.2531 | ±4.5063 | +0.006 | 0.9955 |  |
| Circulatory disease | -0.6785 | 1.0037 | ±2.0073 | -0.676 | 0.4990 |  |
| Time > 180 (%) | +0.4799 | 1.4467 | ±2.8935 | +0.332 | 0.7401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1825**, Adj R² = **0.1556**, F-statistic = **6.78** (p = **2.68e-10**), Residual SE = **6.664** on **334** df, AIC = **2306.2**, BIC = **2352.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.2017** | 4.1246 | ±8.2493 | **+15.080** | **2.18e-51** | *** |
| **Education: graduate level (vs college)** | **-1.7717** | 0.7798 | ±1.5595 | **-2.272** | **0.0231** | * |
| Education: high school or below (vs college) | -1.7718 | 1.3314 | ±2.6629 | -1.331 | 0.1833 |  |
| **Site: UCSD (vs UAB)** | **-1.9442** | 0.9781 | ±1.9561 | **-1.988** | **0.0468** | * |
| **Site: UW (vs UAB)** | **-2.5841** | 0.8832 | ±1.7663 | **-2.926** | **0.0034** | ** |
| **Age (years)** | **-0.1297** | 0.0372 | ±0.0745 | **-3.485** | **4.93e-04** | *** |
| **BMI (kg/m2)** | **+0.2573** | 0.0826 | ±0.1652 | **+3.115** | **0.0018** | ** |
| Hypertension | +0.8846 | 0.8400 | ±1.6799 | +1.053 | 0.2923 |  |
| High cholesterol | -0.2748 | 0.8200 | ±1.6401 | -0.335 | 0.7376 |  |
| Kidney disease | -0.0080 | 2.2254 | ±4.4508 | -0.004 | 0.9971 |  |
| Circulatory disease | -0.6885 | 0.9962 | ±1.9923 | -0.691 | 0.4895 |  |
| Avg. daily time > 180 (%) | +1.4694 | 1.3537 | ±2.7073 | +1.086 | 0.2777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1879**, Adj R² = **0.1611**, F-statistic = **7.02** (p = **1.02e-10**), Residual SE = **6.642** on **334** df, AIC = **2303.9**, BIC = **2350.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.1511** | 3.8724 | ±7.7448 | **+16.050** | **5.75e-58** | *** |
| **Education: graduate level (vs college)** | **-1.6725** | 0.7704 | ±1.5409 | **-2.171** | **0.0299** | * |
| Education: high school or below (vs college) | -1.8868 | 1.3200 | ±2.6401 | -1.429 | 0.1529 |  |
| **Site: UCSD (vs UAB)** | **-1.9339** | 0.9723 | ±1.9446 | **-1.989** | **0.0467** | * |
| **Site: UW (vs UAB)** | **-2.6360** | 0.8853 | ±1.7705 | **-2.978** | **0.0029** | ** |
| **Age (years)** | **-0.1201** | 0.0366 | ±0.0733 | **-3.278** | **0.0010** | ** |
| **BMI (kg/m2)** | **+0.2461** | 0.0802 | ±0.1604 | **+3.068** | **0.0022** | ** |
| Hypertension | +0.8509 | 0.8313 | ±1.6626 | +1.024 | 0.3060 |  |
| High cholesterol | -0.3761 | 0.8165 | ±1.6330 | -0.461 | 0.6451 |  |
| Kidney disease | -0.0938 | 2.1656 | ±4.3312 | -0.043 | 0.9655 |  |
| Circulatory disease | -0.6542 | 1.0038 | ±2.0077 | -0.652 | 0.5146 |  |
| Nocturnal time > 180 (%) | +1.9696 | 1.1673 | ±2.3345 | +1.687 | 0.0915 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 349; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **349**, R² = **0.0654**, Adj R² = **0.0377**, F-statistic = **2.36** (p = **0.0103**), Residual SE = **61.297** on **338** df, AIC = **3874.0**, BIC = **3916.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.5655** | 26.4944 | ±52.9889 | **+15.232** | **2.17e-52** | *** |
| Education: graduate level (vs college) | +4.9608 | 6.7860 | ±13.5720 | +0.731 | 0.4648 |  |
| Education: high school or below (vs college) | -7.2421 | 15.1168 | ±30.2336 | -0.479 | 0.6319 |  |
| Site: UCSD (vs UAB) | -10.3084 | 8.3718 | ±16.7436 | -1.231 | 0.2182 |  |
| Site: UW (vs UAB) | -5.2393 | 8.2818 | ±16.5636 | -0.633 | 0.5270 |  |
| Age (years) | +0.1741 | 0.3266 | ±0.6532 | +0.533 | 0.5939 |  |
| **BMI (kg/m2)** | **-1.1462** | 0.4868 | ±0.9735 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-15.4435** | 7.7635 | ±15.5270 | **-1.989** | **0.0467** | * |
| High cholesterol | -1.4694 | 6.9827 | ±13.9653 | -0.210 | 0.8333 |  |
| Kidney disease | -33.4101 | 20.2134 | ±40.4268 | -1.653 | 0.0984 | . |
| Circulatory disease | +10.1124 | 13.3644 | ±26.7287 | +0.757 | 0.4492 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **349**, R² = **0.0952**, Adj R² = **0.0656**, F-statistic = **3.22** (p = **3.42e-04**), Residual SE = **60.401** on **337** df, AIC = **3864.7**, BIC = **3911.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+600.2638** | 62.8621 | ±125.7243 | **+9.549** | **1.31e-21** | *** |
| Education: graduate level (vs college) | +3.8604 | 6.7077 | ±13.4154 | +0.576 | 0.5649 |  |
| Education: high school or below (vs college) | -6.2891 | 14.9340 | ±29.8681 | -0.421 | 0.6737 |  |
| Site: UCSD (vs UAB) | -12.5410 | 8.2591 | ±16.5182 | -1.518 | 0.1289 |  |
| Site: UW (vs UAB) | -7.4743 | 8.1685 | ±16.3370 | -0.915 | 0.3602 |  |
| Age (years) | +0.2905 | 0.3257 | ±0.6514 | +0.892 | 0.3725 |  |
| **BMI (kg/m2)** | **-1.0099** | 0.4436 | ±0.8872 | **-2.276** | **0.0228** | * |
| Hypertension | -13.4699 | 7.7195 | ±15.4391 | -1.745 | 0.0810 | . |
| High cholesterol | +3.6242 | 6.8839 | ±13.7677 | +0.526 | 0.5986 |  |
| Kidney disease | -34.0634 | 18.7868 | ±37.5737 | -1.813 | 0.0698 | . |
| Circulatory disease | +8.6785 | 12.7431 | ±25.4862 | +0.681 | 0.4958 |  |
| **HbA1c (%)** | **-37.7074** | 11.4252 | ±22.8504 | **-3.300** | **9.66e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **349**, R² = **0.0708**, Adj R² = **0.0405**, F-statistic = **2.33** (p = **0.0089**), Residual SE = **61.209** on **337** df, AIC = **3874.0**, BIC = **3920.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+474.4049** | 52.4029 | ±104.8058 | **+9.053** | **1.39e-19** | *** |
| Education: graduate level (vs college) | +4.8245 | 6.7684 | ±13.5368 | +0.713 | 0.4760 |  |
| Education: high school or below (vs college) | -8.0787 | 15.3416 | ±30.6833 | -0.527 | 0.5985 |  |
| Site: UCSD (vs UAB) | -9.7231 | 8.3638 | ±16.7277 | -1.163 | 0.2450 |  |
| Site: UW (vs UAB) | -4.5730 | 8.3035 | ±16.6070 | -0.551 | 0.5818 |  |
| Age (years) | +0.1491 | 0.3247 | ±0.6493 | +0.459 | 0.6461 |  |
| **BMI (kg/m2)** | **-1.0935** | 0.4825 | ±0.9651 | **-2.266** | **0.0234** | * |
| Hypertension | -14.5683 | 7.8244 | ±15.6488 | -1.862 | 0.0626 | . |
| High cholesterol | -1.9568 | 6.9642 | ±13.9283 | -0.281 | 0.7787 |  |
| Kidney disease | -33.2367 | 20.1190 | ±40.2381 | -1.652 | 0.0985 | . |
| Circulatory disease | +9.8547 | 13.3440 | ±26.6880 | +0.739 | 0.4602 |  |
| Mean glucose (mg/dL) | -0.6242 | 0.4121 | ±0.8242 | -1.514 | 0.1299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **349**, R² = **0.0708**, Adj R² = **0.0405**, F-statistic = **2.33** (p = **0.0089**), Residual SE = **61.209** on **337** df, AIC = **3874.0**, BIC = **3920.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+560.7743** | 105.7091 | ±211.4182 | **+5.305** | **1.13e-07** | *** |
| Education: graduate level (vs college) | +4.8245 | 6.7684 | ±13.5368 | +0.713 | 0.4760 |  |
| Education: high school or below (vs college) | -8.0787 | 15.3416 | ±30.6833 | -0.527 | 0.5985 |  |
| Site: UCSD (vs UAB) | -9.7231 | 8.3638 | ±16.7277 | -1.163 | 0.2450 |  |
| Site: UW (vs UAB) | -4.5730 | 8.3035 | ±16.6070 | -0.551 | 0.5818 |  |
| Age (years) | +0.1491 | 0.3247 | ±0.6493 | +0.459 | 0.6461 |  |
| **BMI (kg/m2)** | **-1.0935** | 0.4825 | ±0.9651 | **-2.266** | **0.0234** | * |
| Hypertension | -14.5683 | 7.8244 | ±15.6488 | -1.862 | 0.0626 | . |
| High cholesterol | -1.9568 | 6.9642 | ±13.9283 | -0.281 | 0.7787 |  |
| Kidney disease | -33.2367 | 20.1190 | ±40.2381 | -1.652 | 0.0985 | . |
| Circulatory disease | +9.8547 | 13.3440 | ±26.6880 | +0.739 | 0.4602 |  |
| GMI (%) | -26.0935 | 17.2292 | ±34.4583 | -1.514 | 0.1299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **349**, R² = **0.0735**, Adj R² = **0.0432**, F-statistic = **2.43** (p = **0.0064**), Residual SE = **61.122** on **337** df, AIC = **3873.0**, BIC = **3919.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+474.4693** | 45.8950 | ±91.7899 | **+10.338** | **4.74e-25** | *** |
| Education: graduate level (vs college) | +4.1878 | 6.7933 | ±13.5867 | +0.616 | 0.5376 |  |
| Education: high school or below (vs college) | -8.3824 | 15.2378 | ±30.4756 | -0.550 | 0.5822 |  |
| Site: UCSD (vs UAB) | -8.7395 | 8.3584 | ±16.7167 | -1.046 | 0.2957 |  |
| Site: UW (vs UAB) | -3.9692 | 8.3341 | ±16.6682 | -0.476 | 0.6339 |  |
| Age (years) | +0.0821 | 0.3232 | ±0.6465 | +0.254 | 0.7994 |  |
| **BMI (kg/m2)** | **-1.0003** | 0.4657 | ±0.9314 | **-2.148** | **0.0317** | * |
| Hypertension | -14.5908 | 7.8106 | ±15.6212 | -1.868 | 0.0617 | . |
| High cholesterol | -1.5693 | 6.9856 | ±13.9711 | -0.225 | 0.8222 |  |
| Kidney disease | -34.4176 | 20.2110 | ±40.4219 | -1.703 | 0.0886 | . |
| Circulatory disease | +9.3443 | 13.3602 | ±26.7204 | +0.699 | 0.4843 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.6121 | 0.3457 | ±0.6913 | -1.771 | 0.0766 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **349**, R² = **0.0667**, Adj R² = **0.0363**, F-statistic = **2.19** (p = **0.0146**), Residual SE = **61.343** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.8456** | 37.1624 | ±74.3247 | **+10.383** | **2.97e-25** | *** |
| Education: graduate level (vs college) | +5.4285 | 6.8820 | ±13.7640 | +0.789 | 0.4302 |  |
| Education: high school or below (vs college) | -7.1972 | 15.1695 | ±30.3389 | -0.474 | 0.6352 |  |
| Site: UCSD (vs UAB) | -9.6870 | 8.3469 | ±16.6938 | -1.161 | 0.2458 |  |
| Site: UW (vs UAB) | -4.8305 | 8.3567 | ±16.7135 | -0.578 | 0.5632 |  |
| Age (years) | +0.1722 | 0.3269 | ±0.6538 | +0.527 | 0.5985 |  |
| **BMI (kg/m2)** | **-1.1600** | 0.4885 | ±0.9771 | **-2.375** | **0.0176** | * |
| **Hypertension** | **-15.4983** | 7.7875 | ±15.5749 | **-1.990** | **0.0466** | * |
| High cholesterol | -1.1962 | 6.9911 | ±13.9822 | -0.171 | 0.8641 |  |
| Kidney disease | -34.1688 | 20.3139 | ±40.6277 | -1.682 | 0.0926 | . |
| Circulatory disease | +10.0936 | 13.4142 | ±26.8284 | +0.752 | 0.4518 |  |
| Glucose SD, pooled (mg/dL) | +1.0470 | 1.5009 | ±3.0018 | +0.698 | 0.4854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **349**, R² = **0.0667**, Adj R² = **0.0363**, F-statistic = **2.19** (p = **0.0146**), Residual SE = **61.343** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.5376** | 35.4502 | ±70.9005 | **+10.932** | **8.12e-28** | *** |
| Education: graduate level (vs college) | +5.4462 | 6.8977 | ±13.7955 | +0.790 | 0.4298 |  |
| Education: high school or below (vs college) | -7.0707 | 15.1468 | ±30.2936 | -0.467 | 0.6406 |  |
| Site: UCSD (vs UAB) | -9.6083 | 8.3649 | ±16.7298 | -1.149 | 0.2507 |  |
| Site: UW (vs UAB) | -4.7893 | 8.3255 | ±16.6509 | -0.575 | 0.5651 |  |
| Age (years) | +0.1739 | 0.3275 | ±0.6550 | +0.531 | 0.5954 |  |
| **BMI (kg/m2)** | **-1.1701** | 0.4923 | ±0.9847 | **-2.377** | **0.0175** | * |
| **Hypertension** | **-15.3433** | 7.7942 | ±15.5885 | **-1.969** | **0.0490** | * |
| High cholesterol | -1.2995 | 6.9938 | ±13.9875 | -0.186 | 0.8526 |  |
| Kidney disease | -34.2635 | 20.2836 | ±40.5671 | -1.689 | 0.0912 | . |
| Circulatory disease | +10.1686 | 13.3933 | ±26.7865 | +0.759 | 0.4477 |  |
| Avg. daily SD (mg/dL) | +1.0374 | 1.5346 | ±3.0692 | +0.676 | 0.4991 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **349**, R² = **0.0700**, Adj R² = **0.0396**, F-statistic = **2.30** (p = **0.0099**), Residual SE = **61.237** on **337** df, AIC = **3874.3**, BIC = **3920.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.4843** | 36.7878 | ±73.5755 | **+10.125** | **4.27e-24** | *** |
| Education: graduate level (vs college) | +5.7359 | 6.8482 | ±13.6964 | +0.838 | 0.4023 |  |
| Education: high school or below (vs college) | -7.5126 | 15.2811 | ±30.5622 | -0.492 | 0.6230 |  |
| Site: UCSD (vs UAB) | -9.0098 | 8.3380 | ±16.6759 | -1.081 | 0.2799 |  |
| Site: UW (vs UAB) | -4.2460 | 8.4131 | ±16.8263 | -0.505 | 0.6138 |  |
| Age (years) | +0.1610 | 0.3253 | ±0.6506 | +0.495 | 0.6205 |  |
| **BMI (kg/m2)** | **-1.1488** | 0.4886 | ±0.9771 | **-2.351** | **0.0187** | * |
| Hypertension | -15.1746 | 7.8102 | ±15.6205 | -1.943 | 0.0520 | . |
| High cholesterol | -1.1507 | 6.9873 | ±13.9746 | -0.165 | 0.8692 |  |
| Kidney disease | -34.6262 | 20.3126 | ±40.6252 | -1.705 | 0.0883 | . |
| Circulatory disease | +9.9455 | 13.4133 | ±26.8266 | +0.741 | 0.4584 |  |
| CV (%) | +2.0755 | 1.6257 | ±3.2515 | +1.277 | 0.2017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **349**, R² = **0.0697**, Adj R² = **0.0393**, F-statistic = **2.30** (p = **0.0102**), Residual SE = **61.245** on **337** df, AIC = **3874.4**, BIC = **3920.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+431.8984** | 34.2161 | ±68.4323 | **+12.623** | **1.58e-36** | *** |
| Education: graduate level (vs college) | +5.7771 | 6.8468 | ±13.6936 | +0.844 | 0.3988 |  |
| Education: high school or below (vs college) | -7.5131 | 15.2983 | ±30.5966 | -0.491 | 0.6234 |  |
| Site: UCSD (vs UAB) | -9.1885 | 8.3306 | ±16.6612 | -1.103 | 0.2700 |  |
| Site: UW (vs UAB) | -4.4377 | 8.3858 | ±16.7715 | -0.529 | 0.5967 |  |
| Age (years) | +0.1638 | 0.3252 | ±0.6504 | +0.504 | 0.6144 |  |
| **BMI (kg/m2)** | **-1.1475** | 0.4872 | ±0.9744 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-15.3288** | 7.8025 | ±15.6050 | **-1.965** | **0.0495** | * |
| High cholesterol | -1.1346 | 6.9890 | ±13.9781 | -0.162 | 0.8710 |  |
| Kidney disease | -34.1706 | 20.3005 | ±40.6010 | -1.683 | 0.0923 | . |
| Circulatory disease | +9.9919 | 13.4074 | ±26.8147 | +0.745 | 0.4561 |  |
| Mean / SD ratio | -4.1736 | 3.3293 | ±6.6585 | -1.254 | 0.2100 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **349**, R² = **0.0678**, Adj R² = **0.0374**, F-statistic = **2.23** (p = **0.0128**), Residual SE = **61.307** on **337** df, AIC = **3875.1**, BIC = **3921.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+423.4098** | 34.1544 | ±68.3089 | **+12.397** | **2.72e-35** | *** |
| Education: graduate level (vs college) | +5.6038 | 6.8603 | ±13.7206 | +0.817 | 0.4140 |  |
| Education: high school or below (vs college) | -7.2771 | 15.2783 | ±30.5567 | -0.476 | 0.6339 |  |
| Site: UCSD (vs UAB) | -9.3300 | 8.3950 | ±16.7899 | -1.111 | 0.2664 |  |
| Site: UW (vs UAB) | -4.5946 | 8.3666 | ±16.7333 | -0.549 | 0.5829 |  |
| Age (years) | +0.1695 | 0.3267 | ±0.6534 | +0.519 | 0.6040 |  |
| **BMI (kg/m2)** | **-1.1688** | 0.4904 | ±0.9809 | **-2.383** | **0.0172** | * |
| Hypertension | -15.0993 | 7.8184 | ±15.6369 | -1.931 | 0.0535 | . |
| High cholesterol | -1.4174 | 6.9937 | ±13.9875 | -0.203 | 0.8394 |  |
| Kidney disease | -34.2836 | 20.2185 | ±40.4371 | -1.696 | 0.0900 | . |
| Circulatory disease | +10.1271 | 13.3558 | ±26.7116 | +0.758 | 0.4483 |  |
| Avg. daily mean/SD | -2.5499 | 2.7486 | ±5.4972 | -0.928 | 0.3536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **349**, R² = **0.0713**, Adj R² = **0.0410**, F-statistic = **2.35** (p = **0.0084**), Residual SE = **61.193** on **337** df, AIC = **3873.8**, BIC = **3920.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+437.8260** | 36.3674 | ±72.7349 | **+12.039** | **2.22e-33** | *** |
| Education: graduate level (vs college) | +4.9246 | 6.7819 | ±13.5638 | +0.726 | 0.4678 |  |
| Education: high school or below (vs college) | -5.6621 | 14.8191 | ±29.6382 | -0.382 | 0.7024 |  |
| Site: UCSD (vs UAB) | -11.3004 | 8.3850 | ±16.7701 | -1.348 | 0.1778 |  |
| Site: UW (vs UAB) | -6.8147 | 8.3349 | ±16.6697 | -0.818 | 0.4136 |  |
| Age (years) | +0.1144 | 0.3302 | ±0.6605 | +0.346 | 0.7290 |  |
| **BMI (kg/m2)** | **-1.1929** | 0.4826 | ±0.9652 | **-2.472** | **0.0134** | * |
| **Hypertension** | **-16.0576** | 7.8262 | ±15.6525 | **-2.052** | **0.0402** | * |
| High cholesterol | -0.5133 | 6.9302 | ±13.8603 | -0.074 | 0.9410 |  |
| Kidney disease | -31.5833 | 20.3110 | ±40.6220 | -1.555 | 0.1199 |  |
| Circulatory disease | +10.2201 | 13.3358 | ±26.6716 | +0.766 | 0.4435 |  |
| MAG (mg/dL/h) | -0.8410 | 0.5881 | ±1.1761 | -1.430 | 0.1527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **349**, R² = **0.0696**, Adj R² = **0.0392**, F-statistic = **2.29** (p = **0.0103**), Residual SE = **61.249** on **337** df, AIC = **3874.4**, BIC = **3920.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+371.0028** | 39.5014 | ±79.0027 | **+9.392** | **5.88e-21** | *** |
| Education: graduate level (vs college) | +5.3148 | 6.8237 | ±13.6474 | +0.779 | 0.4361 |  |
| Education: high school or below (vs college) | -7.2508 | 15.3048 | ±30.6096 | -0.474 | 0.6357 |  |
| Site: UCSD (vs UAB) | -9.2426 | 8.3818 | ±16.7636 | -1.103 | 0.2702 |  |
| Site: UW (vs UAB) | -4.4077 | 8.3608 | ±16.7217 | -0.527 | 0.5981 |  |
| Age (years) | +0.1812 | 0.3264 | ±0.6528 | +0.555 | 0.5787 |  |
| **BMI (kg/m2)** | **-1.0998** | 0.4814 | ±0.9628 | **-2.285** | **0.0223** | * |
| Hypertension | -14.8075 | 7.8521 | ±15.7043 | -1.886 | 0.0593 | . |
| High cholesterol | -1.5693 | 7.0066 | ±14.0133 | -0.224 | 0.8228 |  |
| Kidney disease | -34.4741 | 20.2161 | ±40.4322 | -1.705 | 0.0881 | . |
| Circulatory disease | +9.9149 | 13.3506 | ±26.7012 | +0.743 | 0.4577 |  |
| Avg. daily range (mg/dL) | +0.3728 | 0.3398 | ±0.6795 | +1.097 | 0.2725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **349**, R² = **0.0655**, Adj R² = **0.0350**, F-statistic = **2.15** (p = **0.0170**), Residual SE = **61.384** on **337** df, AIC = **3876.0**, BIC = **3922.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.8047** | 28.2906 | ±56.5812 | **+14.203** | **8.81e-46** | *** |
| Education: graduate level (vs college) | +4.9229 | 6.8090 | ±13.6181 | +0.723 | 0.4697 |  |
| Education: high school or below (vs college) | -7.3847 | 15.1492 | ±30.2983 | -0.487 | 0.6259 |  |
| Site: UCSD (vs UAB) | -10.2321 | 8.3715 | ±16.7431 | -1.222 | 0.2216 |  |
| Site: UW (vs UAB) | -5.3135 | 8.2992 | ±16.5984 | -0.640 | 0.5220 |  |
| Age (years) | +0.1730 | 0.3272 | ±0.6545 | +0.529 | 0.5971 |  |
| **BMI (kg/m2)** | **-1.1487** | 0.4881 | ±0.9762 | **-2.353** | **0.0186** | * |
| **Hypertension** | **-15.5589** | 7.8301 | ±15.6601 | **-1.987** | **0.0469** | * |
| High cholesterol | -1.4791 | 7.0034 | ±14.0068 | -0.211 | 0.8327 |  |
| Kidney disease | -33.2622 | 20.3963 | ±40.7927 | -1.631 | 0.1029 |  |
| Circulatory disease | +10.0305 | 13.4388 | ±26.8775 | +0.746 | 0.4554 |  |
| SD of daily means (mg/dL) | +0.3901 | 1.8296 | ±3.6593 | +0.213 | 0.8312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **349**, R² = **0.0678**, Adj R² = **0.0374**, F-statistic = **2.23** (p = **0.0128**), Residual SE = **61.308** on **337** df, AIC = **3875.1**, BIC = **3921.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1450.2171 | 1177.7835 | ±2355.5671 | +1.231 | 0.2182 |  |
| Education: graduate level (vs college) | +5.1935 | 6.8251 | ±13.6502 | +0.761 | 0.4467 |  |
| Education: high school or below (vs college) | -7.1870 | 15.2083 | ±30.4166 | -0.473 | 0.6365 |  |
| Site: UCSD (vs UAB) | -9.8249 | 8.3577 | ±16.7154 | -1.176 | 0.2398 |  |
| Site: UW (vs UAB) | -4.8503 | 8.3266 | ±16.6533 | -0.583 | 0.5602 |  |
| Age (years) | +0.1852 | 0.3262 | ±0.6524 | +0.568 | 0.5701 |  |
| **BMI (kg/m2)** | **-1.1227** | 0.4767 | ±0.9534 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-15.4841** | 7.7925 | ±15.5850 | **-1.987** | **0.0469** | * |
| High cholesterol | -1.6426 | 7.0069 | ±14.0137 | -0.234 | 0.8146 |  |
| Kidney disease | -33.6806 | 20.2022 | ±40.4045 | -1.667 | 0.0955 | . |
| Circulatory disease | +10.1337 | 13.4865 | ±26.9730 | +0.751 | 0.4524 |  |
| Time in range 70-180, pooled (%) | -10.5319 | 11.8666 | ±23.7332 | -0.888 | 0.3748 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **349**, R² = **0.0690**, Adj R² = **0.0386**, F-statistic = **2.27** (p = **0.0111**), Residual SE = **61.268** on **337** df, AIC = **3874.7**, BIC = **3920.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1646.6510 | 1146.0906 | ±2292.1811 | +1.437 | 0.1508 |  |
| Education: graduate level (vs college) | +5.2889 | 6.8428 | ±13.6856 | +0.773 | 0.4396 |  |
| Education: high school or below (vs college) | -6.9444 | 15.2098 | ±30.4196 | -0.457 | 0.6480 |  |
| Site: UCSD (vs UAB) | -9.7638 | 8.3520 | ±16.7040 | -1.169 | 0.2424 |  |
| Site: UW (vs UAB) | -5.1308 | 8.3282 | ±16.6563 | -0.616 | 0.5378 |  |
| Age (years) | +0.2017 | 0.3284 | ±0.6567 | +0.614 | 0.5391 |  |
| **BMI (kg/m2)** | **-1.1322** | 0.4845 | ±0.9691 | **-2.337** | **0.0195** | * |
| Hypertension | -14.9707 | 7.8336 | ±15.6671 | -1.911 | 0.0560 | . |
| High cholesterol | -1.8598 | 7.0122 | ±14.0244 | -0.265 | 0.7908 |  |
| Kidney disease | -33.5595 | 20.1916 | ±40.3833 | -1.662 | 0.0965 | . |
| Circulatory disease | +9.5862 | 13.5112 | ±27.0223 | +0.710 | 0.4780 |  |
| Avg. daily time in range 70-180 (%) | -12.5049 | 11.5396 | ±23.0791 | -1.084 | 0.2785 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **349**, R² = **0.0664**, Adj R² = **0.0359**, F-statistic = **2.18** (p = **0.0153**), Residual SE = **61.355** on **337** df, AIC = **3875.7**, BIC = **3921.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.3791** | 26.8132 | ±53.6264 | **+15.007** | **6.63e-51** | *** |
| Education: graduate level (vs college) | +5.0000 | 6.8070 | ±13.6140 | +0.735 | 0.4626 |  |
| Education: high school or below (vs college) | -7.1130 | 15.2118 | ±30.4237 | -0.468 | 0.6401 |  |
| Site: UCSD (vs UAB) | -9.4409 | 8.5805 | ±17.1610 | -1.100 | 0.2712 |  |
| Site: UW (vs UAB) | -4.7158 | 8.3441 | ±16.6882 | -0.565 | 0.5720 |  |
| Age (years) | +0.1716 | 0.3264 | ±0.6529 | +0.526 | 0.5991 |  |
| **BMI (kg/m2)** | **-1.1475** | 0.4903 | ±0.9805 | **-2.341** | **0.0193** | * |
| **Hypertension** | **-15.7207** | 7.8213 | ±15.6427 | **-2.010** | **0.0444** | * |
| High cholesterol | -1.4445 | 7.0018 | ±14.0035 | -0.206 | 0.8366 |  |
| Kidney disease | -32.8374 | 20.4036 | ±40.8072 | -1.609 | 0.1075 |  |
| Circulatory disease | +9.8634 | 13.4490 | ±26.8980 | +0.733 | 0.4633 |  |
| Any reading < 54 during wear (0/1) | +5.2781 | 7.9305 | ±15.8609 | +0.666 | 0.5057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **349**, R² = **0.0660**, Adj R² = **0.0355**, F-statistic = **2.16** (p = **0.0160**), Residual SE = **61.368** on **337** df, AIC = **3875.8**, BIC = **3922.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.9475** | 26.7842 | ±53.5684 | **+15.044** | **3.77e-51** | *** |
| Education: graduate level (vs college) | +4.9866 | 6.8036 | ±13.6072 | +0.733 | 0.4636 |  |
| Education: high school or below (vs college) | -6.9207 | 15.1378 | ±30.2757 | -0.457 | 0.6475 |  |
| Site: UCSD (vs UAB) | -9.7843 | 8.5303 | ±17.0605 | -1.147 | 0.2514 |  |
| Site: UW (vs UAB) | -4.9773 | 8.3549 | ±16.7098 | -0.596 | 0.5514 |  |
| Age (years) | +0.1799 | 0.3277 | ±0.6554 | +0.549 | 0.5830 |  |
| **BMI (kg/m2)** | **-1.1629** | 0.4944 | ±0.9889 | **-2.352** | **0.0187** | * |
| **Hypertension** | **-15.6966** | 7.8022 | ±15.6045 | **-2.012** | **0.0442** | * |
| High cholesterol | -1.4124 | 6.9971 | ±13.9941 | -0.202 | 0.8400 |  |
| Kidney disease | -33.0589 | 20.2874 | ±40.5747 | -1.630 | 0.1032 |  |
| Circulatory disease | +9.7252 | 13.4378 | ±26.8756 | +0.724 | 0.4692 |  |
| Time < 54 (%) | +30.2259 | 56.4323 | ±112.8646 | +0.536 | 0.5922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **349**, R² = **0.0686**, Adj R² = **0.0382**, F-statistic = **2.26** (p = **0.0116**), Residual SE = **61.281** on **337** df, AIC = **3874.8**, BIC = **3921.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.9034** | 26.7291 | ±53.4581 | **+15.074** | **2.42e-51** | *** |
| Education: graduate level (vs college) | +4.7646 | 6.8038 | ±13.6076 | +0.700 | 0.4837 |  |
| Education: high school or below (vs college) | -6.9802 | 15.1381 | ±30.2762 | -0.461 | 0.6447 |  |
| Site: UCSD (vs UAB) | -9.6475 | 8.3939 | ±16.7878 | -1.149 | 0.2504 |  |
| Site: UW (vs UAB) | -5.0512 | 8.2805 | ±16.5610 | -0.610 | 0.5419 |  |
| Age (years) | +0.1813 | 0.3266 | ±0.6532 | +0.555 | 0.5788 |  |
| **BMI (kg/m2)** | **-1.1721** | 0.4962 | ±0.9925 | **-2.362** | **0.0182** | * |
| **Hypertension** | **-15.6524** | 7.7568 | ±15.5136 | **-2.018** | **0.0436** | * |
| High cholesterol | -1.2936 | 7.0138 | ±14.0275 | -0.184 | 0.8537 |  |
| Kidney disease | -32.9638 | 20.3267 | ±40.6534 | -1.622 | 0.1049 |  |
| Circulatory disease | +8.8135 | 13.4496 | ±26.8991 | +0.655 | 0.5123 |  |
| Avg. daily time < 54 (%) | +82.1411 | 60.9515 | ±121.9029 | +1.348 | 0.1778 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **349**, R² = **0.0833**, Adj R² = **0.0534**, F-statistic = **2.78** (p = **0.0018**), Residual SE = **60.796** on **337** df, AIC = **3869.3**, BIC = **3915.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7782** | 27.2990 | ±54.5980 | **+14.498** | **1.25e-47** | *** |
| Education: graduate level (vs college) | +5.8491 | 6.7634 | ±13.5268 | +0.865 | 0.3871 |  |
| Education: high school or below (vs college) | -9.4947 | 15.4006 | ±30.8013 | -0.617 | 0.5376 |  |
| Site: UCSD (vs UAB) | -9.2692 | 8.3501 | ±16.7002 | -1.110 | 0.2670 |  |
| Site: UW (vs UAB) | -3.8297 | 8.3158 | ±16.6316 | -0.461 | 0.6451 |  |
| Age (years) | +0.1608 | 0.3236 | ±0.6472 | +0.497 | 0.6192 |  |
| **BMI (kg/m2)** | **-1.1142** | 0.4922 | ±0.9844 | **-2.264** | **0.0236** | * |
| Hypertension | -13.4055 | 7.8050 | ±15.6100 | -1.718 | 0.0859 | . |
| High cholesterol | -3.8069 | 6.9477 | ±13.8954 | -0.548 | 0.5837 |  |
| Kidney disease | -31.6168 | 20.4979 | ±40.9958 | -1.542 | 0.1230 |  |
| Circulatory disease | +10.2020 | 13.3119 | ±26.6238 | +0.766 | 0.4435 |  |
| **Time 54-69, pooled (%)** | **+47.2703** | 17.5737 | ±35.1475 | **+2.690** | **0.0071** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **349**, R² = **0.0838**, Adj R² = **0.0539**, F-statistic = **2.80** (p = **0.0017**), Residual SE = **60.780** on **337** df, AIC = **3869.1**, BIC = **3915.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.8980** | 27.1147 | ±54.2294 | **+14.638** | **1.61e-48** | *** |
| Education: graduate level (vs college) | +6.1474 | 6.7671 | ±13.5343 | +0.908 | 0.3637 |  |
| Education: high school or below (vs college) | -9.4665 | 15.5199 | ±31.0397 | -0.610 | 0.5419 |  |
| Site: UCSD (vs UAB) | -9.9138 | 8.3325 | ±16.6651 | -1.190 | 0.2341 |  |
| Site: UW (vs UAB) | -4.8630 | 8.2523 | ±16.5046 | -0.589 | 0.5557 |  |
| Age (years) | +0.1592 | 0.3257 | ±0.6514 | +0.489 | 0.6249 |  |
| **BMI (kg/m2)** | **-1.1250** | 0.4897 | ±0.9795 | **-2.297** | **0.0216** | * |
| Hypertension | -12.0598 | 7.9534 | ±15.9067 | -1.516 | 0.1294 |  |
| High cholesterol | -3.0755 | 6.9312 | ±13.8625 | -0.444 | 0.6572 |  |
| Kidney disease | -31.8140 | 20.4587 | ±40.9175 | -1.555 | 0.1199 |  |
| Circulatory disease | +9.2263 | 13.3194 | ±26.6388 | +0.693 | 0.4885 |  |
| **Avg. daily time 54-69 (%)** | **+48.0658** | 18.3528 | ±36.7056 | **+2.619** | **0.0088** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **349**, R² = **0.0810**, Adj R² = **0.0510**, F-statistic = **2.70** (p = **0.0024**), Residual SE = **60.872** on **337** df, AIC = **3870.1**, BIC = **3916.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.3240** | 27.4157 | ±54.8315 | **+14.456** | **2.30e-47** | *** |
| Education: graduate level (vs college) | +5.7290 | 6.7624 | ±13.5247 | +0.847 | 0.3969 |  |
| Education: high school or below (vs college) | -8.6898 | 15.3548 | ±30.7095 | -0.566 | 0.5714 |  |
| Site: UCSD (vs UAB) | -8.7707 | 8.3629 | ±16.7257 | -1.049 | 0.2943 |  |
| Site: UW (vs UAB) | -3.7343 | 8.3472 | ±16.6945 | -0.447 | 0.6546 |  |
| Age (years) | +0.1706 | 0.3240 | ±0.6479 | +0.526 | 0.5986 |  |
| **BMI (kg/m2)** | **-1.1414** | 0.4969 | ±0.9938 | **-2.297** | **0.0216** | * |
| Hypertension | -14.0850 | 7.7735 | ±15.5470 | -1.812 | 0.0700 | . |
| High cholesterol | -3.3293 | 6.9427 | ±13.8854 | -0.480 | 0.6316 |  |
| Kidney disease | -31.4722 | 20.5045 | ±41.0089 | -1.535 | 0.1248 |  |
| Circulatory disease | +9.6856 | 13.3225 | ±26.6450 | +0.727 | 0.4672 |  |
| **Time < 70 (%)** | **+39.1046** | 15.1458 | ±30.2917 | **+2.582** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **349**, R² = **0.0835**, Adj R² = **0.0536**, F-statistic = **2.79** (p = **0.0017**), Residual SE = **60.789** on **337** df, AIC = **3869.2**, BIC = **3915.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+397.2696** | 27.1380 | ±54.2761 | **+14.639** | **1.59e-48** | *** |
| Education: graduate level (vs college) | +5.9173 | 6.7503 | ±13.5006 | +0.877 | 0.3807 |  |
| Education: high school or below (vs college) | -9.0904 | 15.4847 | ±30.9693 | -0.587 | 0.5572 |  |
| Site: UCSD (vs UAB) | -9.6111 | 8.3180 | ±16.6360 | -1.155 | 0.2479 |  |
| Site: UW (vs UAB) | -4.8052 | 8.2528 | ±16.5056 | -0.582 | 0.5604 |  |
| Age (years) | +0.1646 | 0.3256 | ±0.6512 | +0.505 | 0.6132 |  |
| **BMI (kg/m2)** | **-1.1409** | 0.4926 | ±0.9851 | **-2.316** | **0.0205** | * |
| Hypertension | -12.5329 | 7.9121 | ±15.8242 | -1.584 | 0.1132 |  |
| High cholesterol | -2.8109 | 6.9323 | ±13.8645 | -0.405 | 0.6851 |  |
| Kidney disease | -31.7527 | 20.4872 | ±40.9743 | -1.550 | 0.1212 |  |
| Circulatory disease | +8.6434 | 13.3287 | ±26.6575 | +0.648 | 0.5167 |  |
| **Avg. daily time < 70 (%)** | **+42.8943** | 16.2583 | ±32.5167 | **+2.638** | **0.0083** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **349**, R² = **0.0657**, Adj R² = **0.0352**, F-statistic = **2.15** (p = **0.0165**), Residual SE = **61.376** on **337** df, AIC = **3875.9**, BIC = **3922.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2677.7952 | 5708.8243 | ±11417.6485 | +0.469 | 0.6390 |  |
| Education: graduate level (vs college) | +5.0003 | 6.8061 | ±13.6122 | +0.735 | 0.4625 |  |
| Education: high school or below (vs college) | -6.9847 | 15.1326 | ±30.2651 | -0.462 | 0.6444 |  |
| Site: UCSD (vs UAB) | -9.9122 | 8.5293 | ±17.0585 | -1.162 | 0.2452 |  |
| Site: UW (vs UAB) | -5.0559 | 8.3482 | ±16.6964 | -0.606 | 0.5448 |  |
| Age (years) | +0.1793 | 0.3280 | ±0.6559 | +0.547 | 0.5846 |  |
| **BMI (kg/m2)** | **-1.1578** | 0.4928 | ±0.9856 | **-2.350** | **0.0188** | * |
| **Hypertension** | **-15.6267** | 7.8008 | ±15.6017 | **-2.003** | **0.0452** | * |
| High cholesterol | -1.4502 | 6.9976 | ±13.9952 | -0.207 | 0.8358 |  |
| Kidney disease | -33.1456 | 20.2772 | ±40.5544 | -1.635 | 0.1021 |  |
| Circulatory disease | +9.8235 | 13.4400 | ±26.8801 | +0.731 | 0.4648 |  |
| Time 54-250, pooled (%) | -22.7478 | 57.1185 | ±114.2371 | -0.398 | 0.6904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **349**, R² = **0.0677**, Adj R² = **0.0373**, F-statistic = **2.23** (p = **0.0129**), Residual SE = **61.310** on **337** df, AIC = **3875.1**, BIC = **3921.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7348.7961 | 6215.6607 | ±12431.3214 | +1.182 | 0.2371 |  |
| Education: graduate level (vs college) | +4.8630 | 6.8045 | ±13.6089 | +0.715 | 0.4748 |  |
| Education: high school or below (vs college) | -6.9683 | 15.1306 | ±30.2611 | -0.461 | 0.6451 |  |
| Site: UCSD (vs UAB) | -9.7438 | 8.3973 | ±16.7946 | -1.160 | 0.2459 |  |
| Site: UW (vs UAB) | -5.1266 | 8.2806 | ±16.5611 | -0.619 | 0.5358 |  |
| Age (years) | +0.1829 | 0.3270 | ±0.6540 | +0.559 | 0.5759 |  |
| **BMI (kg/m2)** | **-1.1648** | 0.4938 | ±0.9875 | **-2.359** | **0.0183** | * |
| **Hypertension** | **-15.5956** | 7.7585 | ±15.5171 | **-2.010** | **0.0444** | * |
| High cholesterol | -1.4008 | 7.0129 | ±14.0259 | -0.200 | 0.8417 |  |
| Kidney disease | -33.0322 | 20.3075 | ±40.6150 | -1.627 | 0.1038 |  |
| Circulatory disease | +9.0225 | 13.4533 | ±26.9066 | +0.671 | 0.5024 |  |
| Avg. daily time 54-250 (%) | -69.4607 | 62.1673 | ±124.3347 | -1.117 | 0.2639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **349**, R² = **0.0667**, Adj R² = **0.0362**, F-statistic = **2.19** (p = **0.0147**), Residual SE = **61.345** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.0707** | 27.6692 | ±55.3384 | **+14.712** | **5.39e-49** | *** |
| Education: graduate level (vs college) | +4.9481 | 6.8135 | ±13.6271 | +0.726 | 0.4677 |  |
| Education: high school or below (vs college) | -7.5794 | 15.1492 | ±30.2985 | -0.500 | 0.6169 |  |
| Site: UCSD (vs UAB) | -10.3612 | 8.3904 | ±16.7807 | -1.235 | 0.2169 |  |
| Site: UW (vs UAB) | -5.2316 | 8.2840 | ±16.5680 | -0.632 | 0.5277 |  |
| Age (years) | +0.1651 | 0.3278 | ±0.6556 | +0.504 | 0.6144 |  |
| **BMI (kg/m2)** | **-1.1629** | 0.5109 | ±1.0219 | **-2.276** | **0.0228** | * |
| Hypertension | -15.1278 | 7.7747 | ±15.5494 | -1.946 | 0.0517 | . |
| High cholesterol | -1.7303 | 6.9960 | ±13.9921 | -0.247 | 0.8047 |  |
| Kidney disease | -32.7995 | 20.5414 | ±41.0828 | -1.597 | 0.1103 |  |
| Circulatory disease | +10.0082 | 13.3345 | ±26.6690 | +0.751 | 0.4529 |  |
| Time 181-250, pooled (%) | -8.1147 | 12.4197 | ±24.8394 | -0.653 | 0.5135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **349**, R² = **0.0661**, Adj R² = **0.0357**, F-statistic = **2.17** (p = **0.0157**), Residual SE = **61.362** on **337** df, AIC = **3875.7**, BIC = **3922.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.3196** | 27.0066 | ±54.0132 | **+15.045** | **3.71e-51** | *** |
| Education: graduate level (vs college) | +4.9423 | 6.8052 | ±13.6103 | +0.726 | 0.4677 |  |
| Education: high school or below (vs college) | -7.6548 | 15.1466 | ±30.2933 | -0.505 | 0.6133 |  |
| Site: UCSD (vs UAB) | -10.4781 | 8.3546 | ±16.7093 | -1.254 | 0.2098 |  |
| Site: UW (vs UAB) | -5.2344 | 8.2888 | ±16.5776 | -0.632 | 0.5277 |  |
| Age (years) | +0.1592 | 0.3266 | ±0.6532 | +0.488 | 0.6258 |  |
| **BMI (kg/m2)** | **-1.1520** | 0.4925 | ±0.9849 | **-2.339** | **0.0193** | * |
| Hypertension | -15.2538 | 7.7846 | ±15.5692 | -1.959 | 0.0501 | . |
| High cholesterol | -1.4769 | 6.9928 | ±13.9856 | -0.211 | 0.8327 |  |
| Kidney disease | -33.0944 | 20.4082 | ±40.8165 | -1.622 | 0.1049 |  |
| Circulatory disease | +10.1620 | 13.3569 | ±26.7137 | +0.761 | 0.4468 |  |
| Avg. daily time 181-250 (%) | -6.2396 | 11.7937 | ±23.5874 | -0.529 | 0.5968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **349**, R² = **0.0668**, Adj R² = **0.0363**, F-statistic = **2.19** (p = **0.0146**), Residual SE = **61.342** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.2031** | 27.6988 | ±55.3976 | **+14.701** | **6.34e-49** | *** |
| Education: graduate level (vs college) | +4.9403 | 6.8140 | ±13.6280 | +0.725 | 0.4684 |  |
| Education: high school or below (vs college) | -7.5949 | 15.1488 | ±30.2975 | -0.501 | 0.6161 |  |
| Site: UCSD (vs UAB) | -10.3633 | 8.3905 | ±16.7810 | -1.235 | 0.2168 |  |
| Site: UW (vs UAB) | -5.2263 | 8.2840 | ±16.5680 | -0.631 | 0.5281 |  |
| Age (years) | +0.1646 | 0.3278 | ±0.6556 | +0.502 | 0.6156 |  |
| **BMI (kg/m2)** | **-1.1638** | 0.5117 | ±1.0234 | **-2.274** | **0.0229** | * |
| Hypertension | -15.1213 | 7.7745 | ±15.5490 | -1.945 | 0.0518 | . |
| High cholesterol | -1.7292 | 6.9947 | ±13.9893 | -0.247 | 0.8047 |  |
| Kidney disease | -32.7818 | 20.5469 | ±41.0937 | -1.595 | 0.1106 |  |
| Circulatory disease | +10.0043 | 13.3323 | ±26.6646 | +0.750 | 0.4530 |  |
| Time > 180 (%) | -8.3502 | 12.4108 | ±24.8215 | -0.673 | 0.5011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **349**, R² = **0.0662**, Adj R² = **0.0357**, F-statistic = **2.17** (p = **0.0156**), Residual SE = **61.360** on **337** df, AIC = **3875.7**, BIC = **3922.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.4606** | 27.0188 | ±54.0377 | **+15.044** | **3.80e-51** | *** |
| Education: graduate level (vs college) | +4.9352 | 6.8056 | ±13.6112 | +0.725 | 0.4684 |  |
| Education: high school or below (vs college) | -7.6769 | 15.1459 | ±30.2918 | -0.507 | 0.6123 |  |
| Site: UCSD (vs UAB) | -10.4857 | 8.3542 | ±16.7085 | -1.255 | 0.2094 |  |
| Site: UW (vs UAB) | -5.2299 | 8.2894 | ±16.5788 | -0.631 | 0.5281 |  |
| Age (years) | +0.1584 | 0.3266 | ±0.6531 | +0.485 | 0.6277 |  |
| **BMI (kg/m2)** | **-1.1526** | 0.4928 | ±0.9855 | **-2.339** | **0.0193** | * |
| Hypertension | -15.2483 | 7.7845 | ±15.5690 | -1.959 | 0.0501 | . |
| High cholesterol | -1.4698 | 6.9923 | ±13.9847 | -0.210 | 0.8335 |  |
| Kidney disease | -33.0813 | 20.4130 | ±40.8260 | -1.621 | 0.1051 |  |
| Circulatory disease | +10.1632 | 13.3546 | ±26.7091 | +0.761 | 0.4466 |  |
| Avg. daily time > 180 (%) | -6.4991 | 11.7822 | ±23.5644 | -0.552 | 0.5812 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **349**, R² = **0.0740**, Adj R² = **0.0438**, F-statistic = **2.45** (p = **0.0059**), Residual SE = **61.103** on **337** df, AIC = **3872.8**, BIC = **3919.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+409.2278** | 26.1377 | ±52.2754 | **+15.657** | **2.99e-55** | *** |
| Education: graduate level (vs college) | +4.0669 | 6.8381 | ±13.6761 | +0.595 | 0.5520 |  |
| Education: high school or below (vs college) | -7.1154 | 15.0949 | ±30.1899 | -0.471 | 0.6374 |  |
| Site: UCSD (vs UAB) | -10.7691 | 8.3637 | ±16.7273 | -1.288 | 0.1979 |  |
| Site: UW (vs UAB) | -4.7032 | 8.2794 | ±16.5589 | -0.568 | 0.5700 |  |
| Age (years) | +0.0624 | 0.3280 | ±0.6561 | +0.190 | 0.8491 |  |
| **BMI (kg/m2)** | **-1.0548** | 0.4770 | ±0.9540 | **-2.211** | **0.0270** | * |
| Hypertension | -14.6620 | 7.7016 | ±15.4032 | -1.904 | 0.0569 | . |
| High cholesterol | -0.6365 | 6.9586 | ±13.9172 | -0.091 | 0.9271 |  |
| Kidney disease | -31.8496 | 19.9102 | ±39.8204 | -1.600 | 0.1097 |  |
| Circulatory disease | +9.8390 | 13.4057 | ±26.8113 | +0.734 | 0.4630 |  |
| Nocturnal time > 180 (%) | -17.1428 | 10.8986 | ±21.7971 | -1.573 | 0.1157 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 346; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0987**, F-statistic = **4.78** (p = **2.01e-06**), Residual SE = **16.037** on **335** df, AIC = **2913.0**, BIC = **2955.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0937** | 8.3045 | ±16.6091 | **+6.755** | **1.43e-11** | *** |
| Education: graduate level (vs college) | -3.5493 | 1.8441 | ±3.6882 | -1.925 | 0.0543 | . |
| Education: high school or below (vs college) | +0.3223 | 3.3631 | ±6.7262 | +0.096 | 0.9237 |  |
| Site: UCSD (vs UAB) | -1.8928 | 2.3291 | ±4.6582 | -0.813 | 0.4164 |  |
| **Site: UW (vs UAB)** | **-4.4324** | 2.1258 | ±4.2516 | **-2.085** | **0.0371** | * |
| **Age (years)** | **-0.2951** | 0.0873 | ±0.1747 | **-3.378** | **7.29e-04** | *** |
| **BMI (kg/m2)** | **+0.4696** | 0.1583 | ±0.3167 | **+2.966** | **0.0030** | ** |
| Hypertension | -0.0692 | 2.1014 | ±4.2029 | -0.033 | 0.9737 |  |
| High cholesterol | -0.6058 | 1.9248 | ±3.8496 | -0.315 | 0.7530 |  |
| Kidney disease | -2.1559 | 5.2242 | ±10.4483 | -0.413 | 0.6798 |  |
| Circulatory disease | -1.7947 | 2.5443 | ±5.0885 | -0.705 | 0.4806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **346**, R² = **0.1256**, Adj R² = **0.0968**, F-statistic = **4.36** (p = **4.12e-06**), Residual SE = **16.055** on **334** df, AIC = **2914.7**, BIC = **2960.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9108** | 18.3902 | ±36.7804 | **+2.605** | **0.0092** | ** |
| Education: graduate level (vs college) | -3.5149 | 1.8496 | ±3.6993 | -1.900 | 0.0574 | . |
| Education: high school or below (vs college) | +0.2863 | 3.3539 | ±6.7078 | +0.085 | 0.9320 |  |
| Site: UCSD (vs UAB) | -1.8186 | 2.3287 | ±4.6573 | -0.781 | 0.4348 |  |
| **Site: UW (vs UAB)** | **-4.3425** | 2.1275 | ±4.2551 | **-2.041** | **0.0412** | * |
| **Age (years)** | **-0.2998** | 0.0877 | ±0.1754 | **-3.417** | **6.32e-04** | *** |
| **BMI (kg/m2)** | **+0.4620** | 0.1578 | ±0.3156 | **+2.928** | **0.0034** | ** |
| Hypertension | -0.1541 | 2.1110 | ±4.2221 | -0.073 | 0.9418 |  |
| High cholesterol | -0.8194 | 1.9993 | ±3.9987 | -0.410 | 0.6819 |  |
| Kidney disease | -2.0739 | 5.2332 | ±10.4664 | -0.396 | 0.6919 |  |
| Circulatory disease | -1.7298 | 2.5455 | ±5.0909 | -0.680 | 0.4968 |  |
| HbA1c (%) | +1.5785 | 3.2405 | ±6.4811 | +0.487 | 0.6262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **346**, R² = **0.1277**, Adj R² = **0.0990**, F-statistic = **4.44** (p = **2.94e-06**), Residual SE = **16.035** on **334** df, AIC = **2913.8**, BIC = **2960.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2412** | 16.1941 | ±32.3881 | **+2.608** | **0.0091** | ** |
| Education: graduate level (vs college) | -3.5050 | 1.8456 | ±3.6913 | -1.899 | 0.0576 | . |
| Education: high school or below (vs college) | +0.4495 | 3.3702 | ±6.7404 | +0.133 | 0.8939 |  |
| Site: UCSD (vs UAB) | -2.0217 | 2.3353 | ±4.6706 | -0.866 | 0.3867 |  |
| **Site: UW (vs UAB)** | **-4.5705** | 2.1136 | ±4.2272 | **-2.162** | **0.0306** | * |
| **Age (years)** | **-0.2906** | 0.0879 | ±0.1757 | **-3.307** | **9.42e-04** | *** |
| **BMI (kg/m2)** | **+0.4589** | 0.1576 | ±0.3152 | **+2.912** | **0.0036** | ** |
| Hypertension | -0.2658 | 2.0827 | ±4.1655 | -0.128 | 0.8985 |  |
| High cholesterol | -0.5235 | 1.9386 | ±3.8773 | -0.270 | 0.7871 |  |
| Kidney disease | -2.1933 | 5.2799 | ±10.5599 | -0.415 | 0.6778 |  |
| Circulatory disease | -1.7888 | 2.5442 | ±5.0883 | -0.703 | 0.4820 |  |
| Mean glucose (mg/dL) | +0.1225 | 0.1208 | ±0.2415 | +1.015 | 0.3103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **346**, R² = **0.1277**, Adj R² = **0.0990**, F-statistic = **4.44** (p = **2.94e-06**), Residual SE = **16.035** on **334** df, AIC = **2913.8**, BIC = **2960.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +25.2838 | 31.7292 | ±63.4584 | +0.797 | 0.4255 |  |
| Education: graduate level (vs college) | -3.5050 | 1.8456 | ±3.6913 | -1.899 | 0.0576 | . |
| Education: high school or below (vs college) | +0.4495 | 3.3702 | ±6.7404 | +0.133 | 0.8939 |  |
| Site: UCSD (vs UAB) | -2.0217 | 2.3353 | ±4.6706 | -0.866 | 0.3867 |  |
| **Site: UW (vs UAB)** | **-4.5705** | 2.1136 | ±4.2272 | **-2.162** | **0.0306** | * |
| **Age (years)** | **-0.2906** | 0.0879 | ±0.1757 | **-3.307** | **9.42e-04** | *** |
| **BMI (kg/m2)** | **+0.4589** | 0.1576 | ±0.3152 | **+2.912** | **0.0036** | ** |
| Hypertension | -0.2658 | 2.0827 | ±4.1655 | -0.128 | 0.8985 |  |
| High cholesterol | -0.5235 | 1.9386 | ±3.8773 | -0.270 | 0.7871 |  |
| Kidney disease | -2.1933 | 5.2799 | ±10.5599 | -0.415 | 0.6778 |  |
| Circulatory disease | -1.7888 | 2.5442 | ±5.0883 | -0.703 | 0.4820 |  |
| GMI (%) | +5.1231 | 5.0490 | ±10.0979 | +1.015 | 0.3103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **346**, R² = **0.1300**, Adj R² = **0.1014**, F-statistic = **4.54** (p = **2.03e-06**), Residual SE = **16.014** on **334** df, AIC = **2912.9**, BIC = **2959.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.6737** | 13.2113 | ±26.4226 | **+3.079** | **0.0021** | ** |
| Education: graduate level (vs college) | -3.3541 | 1.8373 | ±3.6746 | -1.826 | 0.0679 | . |
| Education: high school or below (vs college) | +0.5215 | 3.3742 | ±6.7485 | +0.155 | 0.8772 |  |
| Site: UCSD (vs UAB) | -2.2580 | 2.3351 | ±4.6703 | -0.967 | 0.3336 |  |
| **Site: UW (vs UAB)** | **-4.7044** | 2.1162 | ±4.2324 | **-2.223** | **0.0262** | * |
| **Age (years)** | **-0.2757** | 0.0879 | ±0.1757 | **-3.138** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.4397** | 0.1539 | ±0.3078 | **+2.857** | **0.0043** | ** |
| Hypertension | -0.2568 | 2.0775 | ±4.1551 | -0.124 | 0.9016 |  |
| High cholesterol | -0.6081 | 1.9259 | ±3.8517 | -0.316 | 0.7522 |  |
| Kidney disease | -1.9757 | 5.2188 | ±10.4375 | -0.379 | 0.7050 |  |
| Circulatory disease | -1.6846 | 2.5228 | ±5.0456 | -0.668 | 0.5043 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.1331 | 0.0960 | ±0.1919 | +1.387 | 0.1656 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1292**, Adj R² = **0.1006**, F-statistic = **4.51** (p = **2.30e-06**), Residual SE = **16.021** on **334** df, AIC = **2913.2**, BIC = **2959.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6581** | 10.9625 | ±21.9249 | **+4.347** | **1.38e-05** | *** |
| Education: graduate level (vs college) | -3.3233 | 1.8527 | ±3.7053 | -1.794 | 0.0729 | . |
| Education: high school or below (vs college) | +0.4831 | 3.3058 | ±6.6116 | +0.146 | 0.8838 |  |
| Site: UCSD (vs UAB) | -1.6374 | 2.3278 | ±4.6555 | -0.703 | 0.4818 |  |
| **Site: UW (vs UAB)** | **-4.2661** | 2.1173 | ±4.2346 | **-2.015** | **0.0439** | * |
| **Age (years)** | **-0.2956** | 0.0873 | ±0.1747 | **-3.385** | **7.12e-04** | *** |
| **BMI (kg/m2)** | **+0.4622** | 0.1573 | ±0.3147 | **+2.938** | **0.0033** | ** |
| Hypertension | -0.1489 | 2.0956 | ±4.1912 | -0.071 | 0.9433 |  |
| High cholesterol | -0.4331 | 1.9414 | ±3.8827 | -0.223 | 0.8235 |  |
| Kidney disease | -2.5602 | 5.3362 | ±10.6724 | -0.480 | 0.6314 |  |
| Circulatory disease | -1.8669 | 2.5278 | ±5.0556 | -0.739 | 0.4602 |  |
| Glucose SD, pooled (mg/dL) | +0.5004 | 0.4248 | ±0.8496 | +1.178 | 0.2388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1288**, Adj R² = **0.1001**, F-statistic = **4.49** (p = **2.48e-06**), Residual SE = **16.025** on **334** df, AIC = **2913.4**, BIC = **2959.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7962** | 10.3726 | ±20.7452 | **+4.704** | **2.55e-06** | *** |
| Education: graduate level (vs college) | -3.3244 | 1.8548 | ±3.7096 | -1.792 | 0.0731 | . |
| Education: high school or below (vs college) | +0.5149 | 3.3095 | ±6.6190 | +0.156 | 0.8763 |  |
| Site: UCSD (vs UAB) | -1.6216 | 2.3274 | ±4.6549 | -0.697 | 0.4860 |  |
| **Site: UW (vs UAB)** | **-4.2525** | 2.1220 | ±4.2440 | **-2.004** | **0.0451** | * |
| **Age (years)** | **-0.2944** | 0.0874 | ±0.1748 | **-3.370** | **7.53e-04** | *** |
| **BMI (kg/m2)** | **+0.4586** | 0.1561 | ±0.3123 | **+2.937** | **0.0033** | ** |
| Hypertension | -0.0925 | 2.1009 | ±4.2019 | -0.044 | 0.9649 |  |
| High cholesterol | -0.4684 | 1.9363 | ±3.8727 | -0.242 | 0.8089 |  |
| Kidney disease | -2.5229 | 5.3272 | ±10.6544 | -0.474 | 0.6358 |  |
| Circulatory disease | -1.8144 | 2.5493 | ±5.0987 | -0.712 | 0.4766 |  |
| Avg. daily SD (mg/dL) | +0.4712 | 0.4183 | ±0.8367 | +1.126 | 0.2600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **346**, R² = **0.1264**, Adj R² = **0.0976**, F-statistic = **4.39** (p = **3.60e-06**), Residual SE = **16.047** on **334** df, AIC = **2914.3**, BIC = **2960.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2074** | 10.5237 | ±21.0473 | **+4.866** | **1.14e-06** | *** |
| Education: graduate level (vs college) | -3.4329 | 1.8558 | ±3.7115 | -1.850 | 0.0643 | . |
| Education: high school or below (vs college) | +0.3733 | 3.3330 | ±6.6659 | +0.112 | 0.9108 |  |
| Site: UCSD (vs UAB) | -1.7054 | 2.3319 | ±4.6638 | -0.731 | 0.4646 |  |
| **Site: UW (vs UAB)** | **-4.2893** | 2.1212 | ±4.2425 | **-2.022** | **0.0432** | * |
| **Age (years)** | **-0.2968** | 0.0875 | ±0.1750 | **-3.392** | **6.93e-04** | *** |
| **BMI (kg/m2)** | **+0.4689** | 0.1582 | ±0.3165 | **+2.963** | **0.0030** | ** |
| Hypertension | -0.0511 | 2.1089 | ±4.2178 | -0.024 | 0.9807 |  |
| High cholesterol | -0.5277 | 1.9326 | ±3.8653 | -0.273 | 0.7848 |  |
| Kidney disease | -2.3687 | 5.2901 | ±10.5802 | -0.448 | 0.6543 |  |
| Circulatory disease | -1.8427 | 2.5366 | ±5.0733 | -0.726 | 0.4676 |  |
| CV (%) | +0.3262 | 0.4402 | ±0.8804 | +0.741 | 0.4587 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **346**, R² = **0.1263**, Adj R² = **0.0975**, F-statistic = **4.39** (p = **3.66e-06**), Residual SE = **16.048** on **334** df, AIC = **2914.4**, BIC = **2960.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4632** | 10.3065 | ±20.6130 | **+5.867** | **4.45e-09** | *** |
| Education: graduate level (vs college) | -3.4244 | 1.8548 | ±3.7097 | -1.846 | 0.0649 | . |
| Education: high school or below (vs college) | +0.3582 | 3.3307 | ±6.6613 | +0.108 | 0.9144 |  |
| Site: UCSD (vs UAB) | -1.7502 | 2.3329 | ±4.6658 | -0.750 | 0.4531 |  |
| **Site: UW (vs UAB)** | **-4.3302** | 2.1251 | ±4.2502 | **-2.038** | **0.0416** | * |
| **Age (years)** | **-0.2961** | 0.0874 | ±0.1748 | **-3.388** | **7.05e-04** | *** |
| **BMI (kg/m2)** | **+0.4690** | 0.1585 | ±0.3170 | **+2.959** | **0.0031** | ** |
| Hypertension | -0.0760 | 2.1066 | ±4.2133 | -0.036 | 0.9712 |  |
| High cholesterol | -0.5206 | 1.9353 | ±3.8706 | -0.269 | 0.7879 |  |
| Kidney disease | -2.3082 | 5.2611 | ±10.5222 | -0.439 | 0.6609 |  |
| Circulatory disease | -1.8346 | 2.5353 | ±5.0706 | -0.724 | 0.4693 |  |
| Mean / SD ratio | -0.6440 | 0.9006 | ±1.8013 | -0.715 | 0.4746 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1267**, Adj R² = **0.0980**, F-statistic = **4.41** (p = **3.41e-06**), Residual SE = **16.044** on **334** df, AIC = **2914.2**, BIC = **2960.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.6903** | 10.1321 | ±20.2641 | **+5.990** | **2.10e-09** | *** |
| Education: graduate level (vs college) | -3.3982 | 1.8569 | ±3.7137 | -1.830 | 0.0672 | . |
| Education: high school or below (vs college) | +0.3888 | 3.3249 | ±6.6498 | +0.117 | 0.9069 |  |
| Site: UCSD (vs UAB) | -1.7061 | 2.3350 | ±4.6700 | -0.731 | 0.4650 |  |
| **Site: UW (vs UAB)** | **-4.3076** | 2.1269 | ±4.2537 | **-2.025** | **0.0428** | * |
| **Age (years)** | **-0.2954** | 0.0874 | ±0.1749 | **-3.378** | **7.30e-04** | *** |
| **BMI (kg/m2)** | **+0.4643** | 0.1577 | ±0.3154 | **+2.945** | **0.0032** | ** |
| Hypertension | -0.0304 | 2.1142 | ±4.2285 | -0.014 | 0.9885 |  |
| High cholesterol | -0.5381 | 1.9299 | ±3.8598 | -0.279 | 0.7804 |  |
| Kidney disease | -2.3549 | 5.2576 | ±10.5152 | -0.448 | 0.6542 |  |
| Circulatory disease | -1.8108 | 2.5510 | ±5.1020 | -0.710 | 0.4778 |  |
| Avg. daily mean/SD | -0.5947 | 0.7337 | ±1.4675 | -0.811 | 0.4176 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **346**, R² = **0.1258**, Adj R² = **0.0970**, F-statistic = **4.37** (p = **3.98e-06**), Residual SE = **16.053** on **334** df, AIC = **2914.6**, BIC = **2960.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3806** | 10.7306 | ±21.4611 | **+4.881** | **1.05e-06** | *** |
| Education: graduate level (vs college) | -3.5475 | 1.8505 | ±3.7010 | -1.917 | 0.0552 | . |
| Education: high school or below (vs college) | +0.1857 | 3.3903 | ±6.7805 | +0.055 | 0.9563 |  |
| Site: UCSD (vs UAB) | -1.7807 | 2.3560 | ±4.7120 | -0.756 | 0.4498 |  |
| **Site: UW (vs UAB)** | **-4.2644** | 2.1704 | ±4.3408 | **-1.965** | **0.0494** | * |
| **Age (years)** | **-0.2884** | 0.0885 | ±0.1770 | **-3.259** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.4751** | 0.1580 | ±0.3160 | **+3.007** | **0.0026** | ** |
| Hypertension | +0.0001 | 2.1182 | ±4.2364 | +0.000 | 1.0000 |  |
| High cholesterol | -0.6784 | 1.9376 | ±3.8753 | -0.350 | 0.7263 |  |
| Kidney disease | -2.3439 | 5.2429 | ±10.4858 | -0.447 | 0.6548 |  |
| Circulatory disease | -1.8385 | 2.5640 | ±5.1280 | -0.717 | 0.4733 |  |
| MAG (mg/dL/h) | +0.0904 | 0.1620 | ±0.3240 | +0.558 | 0.5770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **346**, R² = **0.1263**, Adj R² = **0.0975**, F-statistic = **4.39** (p = **3.69e-06**), Residual SE = **16.048** on **334** df, AIC = **2914.4**, BIC = **2960.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0011** | 11.7394 | ±23.4787 | **+4.344** | **1.40e-05** | *** |
| Education: graduate level (vs college) | -3.4875 | 1.8581 | ±3.7161 | -1.877 | 0.0605 | . |
| Education: high school or below (vs college) | +0.3815 | 3.3381 | ±6.6762 | +0.114 | 0.9090 |  |
| Site: UCSD (vs UAB) | -1.7626 | 2.3488 | ±4.6976 | -0.750 | 0.4530 |  |
| **Site: UW (vs UAB)** | **-4.3284** | 2.1499 | ±4.2998 | **-2.013** | **0.0441** | * |
| **Age (years)** | **-0.2931** | 0.0879 | ±0.1758 | **-3.335** | **8.53e-04** | *** |
| **BMI (kg/m2)** | **+0.4765** | 0.1628 | ±0.3255 | **+2.928** | **0.0034** | ** |
| Hypertension | -0.0028 | 2.1184 | ±4.2369 | -0.001 | 0.9990 |  |
| High cholesterol | -0.5904 | 1.9276 | ±3.8551 | -0.306 | 0.7594 |  |
| Kidney disease | -2.3073 | 5.2754 | ±10.5509 | -0.437 | 0.6618 |  |
| Circulatory disease | -1.8649 | 2.5571 | ±5.1142 | -0.729 | 0.4658 |  |
| Avg. daily range (mg/dL) | +0.0581 | 0.0859 | ±0.1719 | +0.676 | 0.4988 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **346**, R² = **0.1351**, Adj R² = **0.1067**, F-statistic = **4.74** (p = **8.95e-07**), Residual SE = **15.966** on **334** df, AIC = **2910.9**, BIC = **2957.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8900** | 8.4446 | ±16.8891 | **+6.145** | **8.01e-10** | *** |
| **Education: graduate level (vs college)** | **-3.6752** | 1.8409 | ±3.6818 | **-1.996** | **0.0459** | * |
| Education: high school or below (vs college) | +0.0680 | 3.2913 | ±6.5825 | +0.021 | 0.9835 |  |
| Site: UCSD (vs UAB) | -1.7829 | 2.3144 | ±4.6287 | -0.770 | 0.4411 |  |
| **Site: UW (vs UAB)** | **-4.6317** | 2.1008 | ±4.2017 | **-2.205** | **0.0275** | * |
| **Age (years)** | **-0.3024** | 0.0859 | ±0.1718 | **-3.520** | **4.31e-04** | *** |
| **BMI (kg/m2)** | **+0.4656** | 0.1562 | ±0.3124 | **+2.981** | **0.0029** | ** |
| Hypertension | -0.3496 | 2.1094 | ±4.2187 | -0.166 | 0.8684 |  |
| High cholesterol | -0.6059 | 1.9125 | ±3.8249 | -0.317 | 0.7514 |  |
| Kidney disease | -1.9387 | 5.1677 | ±10.3353 | -0.375 | 0.7075 |  |
| Circulatory disease | -1.9286 | 2.4983 | ±4.9966 | -0.772 | 0.4401 |  |
| **SD of daily means (mg/dL)** | **+0.9758** | 0.4941 | ±0.9881 | **+1.975** | **0.0483** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **346**, R² = **0.1329**, Adj R² = **0.1043**, F-statistic = **4.65** (p = **1.29e-06**), Residual SE = **15.987** on **334** df, AIC = **2911.8**, BIC = **2957.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +567.4436 | 302.4155 | ±604.8309 | +1.876 | 0.0606 | . |
| Education: graduate level (vs college) | -3.4102 | 1.8565 | ±3.7131 | -1.837 | 0.0662 | . |
| Education: high school or below (vs college) | +0.5052 | 3.2861 | ±6.5723 | +0.154 | 0.8778 |  |
| Site: UCSD (vs UAB) | -1.6315 | 2.3478 | ±4.6956 | -0.695 | 0.4871 |  |
| **Site: UW (vs UAB)** | **-4.2551** | 2.1266 | ±4.2532 | **-2.001** | **0.0454** | * |
| **Age (years)** | **-0.2876** | 0.0887 | ±0.1775 | **-3.241** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.4785** | 0.1729 | ±0.3458 | **+2.767** | **0.0057** | ** |
| Hypertension | -0.1297 | 2.0782 | ±4.1564 | -0.062 | 0.9503 |  |
| High cholesterol | -0.7050 | 1.9156 | ±3.8312 | -0.368 | 0.7129 |  |
| Kidney disease | -2.4249 | 5.2929 | ±10.5858 | -0.458 | 0.6469 |  |
| Circulatory disease | -1.8873 | 2.5100 | ±5.0200 | -0.752 | 0.4521 |  |
| Time in range 70-180, pooled (%) | -5.1455 | 3.0508 | ±6.1015 | -1.687 | 0.0917 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **346**, R² = **0.1371**, Adj R² = **0.1086**, F-statistic = **4.82** (p = **6.55e-07**), Residual SE = **15.949** on **334** df, AIC = **2910.1**, BIC = **2956.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+668.8642** | 286.2631 | ±572.5262 | **+2.337** | **0.0195** | * |
| Education: graduate level (vs college) | -3.3687 | 1.8464 | ±3.6929 | -1.824 | 0.0681 | . |
| Education: high school or below (vs college) | +0.6466 | 3.2589 | ±6.5178 | +0.198 | 0.8427 |  |
| Site: UCSD (vs UAB) | -1.6122 | 2.3207 | ±4.6414 | -0.695 | 0.4872 |  |
| **Site: UW (vs UAB)** | **-4.4027** | 2.1096 | ±4.2192 | **-2.087** | **0.0369** | * |
| **Age (years)** | **-0.2802** | 0.0878 | ±0.1756 | **-3.192** | **0.0014** | ** |
| **BMI (kg/m2)** | **+0.4739** | 0.1618 | ±0.3237 | **+2.929** | **0.0034** | ** |
| Hypertension | +0.0797 | 2.0907 | ±4.1813 | +0.038 | 0.9696 |  |
| High cholesterol | -0.7904 | 1.9092 | ±3.8183 | -0.414 | 0.6789 |  |
| Kidney disease | -2.2188 | 5.3517 | ±10.7033 | -0.415 | 0.6784 |  |
| Circulatory disease | -2.0811 | 2.5379 | ±5.0759 | -0.820 | 0.4122 |  |
| **Avg. daily time in range 70-180 (%)** | **-6.1638** | 2.8804 | ±5.7608 | **-2.140** | **0.0324** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0960**, F-statistic = **4.33** (p = **4.61e-06**), Residual SE = **16.061** on **334** df, AIC = **2915.0**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0935** | 8.3547 | ±16.7094 | **+6.714** | **1.89e-11** | *** |
| Education: graduate level (vs college) | -3.5493 | 1.8521 | ±3.7041 | -1.916 | 0.0553 | . |
| Education: high school or below (vs college) | +0.3223 | 3.3797 | ±6.7594 | +0.095 | 0.9240 |  |
| Site: UCSD (vs UAB) | -1.8927 | 2.3581 | ±4.7161 | -0.803 | 0.4222 |  |
| **Site: UW (vs UAB)** | **-4.4323** | 2.1438 | ±4.2877 | **-2.067** | **0.0387** | * |
| **Age (years)** | **-0.2951** | 0.0876 | ±0.1751 | **-3.370** | **7.51e-04** | *** |
| **BMI (kg/m2)** | **+0.4696** | 0.1586 | ±0.3171 | **+2.962** | **0.0031** | ** |
| Hypertension | -0.0692 | 2.1145 | ±4.2291 | -0.033 | 0.9739 |  |
| High cholesterol | -0.6058 | 1.9281 | ±3.8562 | -0.314 | 0.7534 |  |
| Kidney disease | -2.1558 | 5.2526 | ±10.5052 | -0.410 | 0.6815 |  |
| Circulatory disease | -1.7948 | 2.5510 | ±5.1020 | -0.704 | 0.4817 |  |
| Any reading < 54 during wear (0/1) | +0.0010 | 2.1553 | ±4.3107 | +0.000 | 0.9996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1252**, Adj R² = **0.0964**, F-statistic = **4.35** (p = **4.35e-06**), Residual SE = **16.058** on **334** df, AIC = **2914.8**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.9622** | 8.2921 | ±16.5843 | **+6.749** | **1.49e-11** | *** |
| Education: graduate level (vs college) | -3.5408 | 1.8495 | ±3.6990 | -1.914 | 0.0556 | . |
| Education: high school or below (vs college) | +0.3946 | 3.3814 | ±6.7628 | +0.117 | 0.9071 |  |
| Site: UCSD (vs UAB) | -1.7954 | 2.3411 | ±4.6823 | -0.767 | 0.4432 |  |
| **Site: UW (vs UAB)** | **-4.3845** | 2.1340 | ±4.2679 | **-2.055** | **0.0399** | * |
| **Age (years)** | **-0.2937** | 0.0875 | ±0.1751 | **-3.356** | **7.91e-04** | *** |
| **BMI (kg/m2)** | **+0.4663** | 0.1584 | ±0.3168 | **+2.944** | **0.0032** | ** |
| Hypertension | -0.1247 | 2.1220 | ±4.2440 | -0.059 | 0.9532 |  |
| High cholesterol | -0.5941 | 1.9296 | ±3.8593 | -0.308 | 0.7582 |  |
| Kidney disease | -2.0872 | 5.2386 | ±10.4773 | -0.398 | 0.6903 |  |
| Circulatory disease | -1.8833 | 2.5699 | ±5.1399 | -0.733 | 0.4637 |  |
| Time < 54 (%) | +6.1824 | 14.2542 | ±28.5084 | +0.434 | 0.6645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1251**, Adj R² = **0.0963**, F-statistic = **4.34** (p = **4.43e-06**), Residual SE = **16.059** on **334** df, AIC = **2914.9**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0411** | 8.3011 | ±16.6023 | **+6.751** | **1.47e-11** | *** |
| Education: graduate level (vs college) | -3.5633 | 1.8481 | ±3.6961 | -1.928 | 0.0538 | . |
| Education: high school or below (vs college) | +0.3429 | 3.3671 | ±6.7341 | +0.102 | 0.9189 |  |
| Site: UCSD (vs UAB) | -1.8505 | 2.3347 | ±4.6694 | -0.793 | 0.4280 |  |
| **Site: UW (vs UAB)** | **-4.4234** | 2.1336 | ±4.2671 | **-2.073** | **0.0381** | * |
| **Age (years)** | **-0.2944** | 0.0875 | ±0.1750 | **-3.365** | **7.66e-04** | *** |
| **BMI (kg/m2)** | **+0.4677** | 0.1584 | ±0.3168 | **+2.953** | **0.0031** | ** |
| Hypertension | -0.0874 | 2.1101 | ±4.2203 | -0.041 | 0.9670 |  |
| High cholesterol | -0.5929 | 1.9340 | ±3.8681 | -0.307 | 0.7592 |  |
| Kidney disease | -2.1219 | 5.2368 | ±10.4736 | -0.405 | 0.6853 |  |
| Circulatory disease | -1.8997 | 2.5855 | ±5.1710 | -0.735 | 0.4625 |  |
| Avg. daily time < 54 (%) | +6.1488 | 18.7229 | ±37.4457 | +0.328 | 0.7426 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1250**, Adj R² = **0.0962**, F-statistic = **4.34** (p = **4.48e-06**), Residual SE = **16.060** on **334** df, AIC = **2914.9**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8586** | 8.3449 | ±16.6898 | **+6.694** | **2.18e-11** | *** |
| Education: graduate level (vs college) | -3.5256 | 1.8632 | ±3.7264 | -1.892 | 0.0585 | . |
| Education: high school or below (vs college) | +0.2934 | 3.3573 | ±6.7145 | +0.087 | 0.9304 |  |
| Site: UCSD (vs UAB) | -1.8546 | 2.3358 | ±4.6716 | -0.794 | 0.4272 |  |
| **Site: UW (vs UAB)** | **-4.3885** | 2.1381 | ±4.2761 | **-2.053** | **0.0401** | * |
| **Age (years)** | **-0.2951** | 0.0876 | ±0.1753 | **-3.368** | **7.58e-04** | *** |
| **BMI (kg/m2)** | **+0.4705** | 0.1583 | ±0.3166 | **+2.972** | **0.0030** | ** |
| Hypertension | -0.0162 | 2.1145 | ±4.2289 | -0.008 | 0.9939 |  |
| High cholesterol | -0.6649 | 1.9696 | ±3.9392 | -0.338 | 0.7357 |  |
| Kidney disease | -2.1097 | 5.2458 | ±10.4916 | -0.402 | 0.6876 |  |
| Circulatory disease | -1.7919 | 2.5549 | ±5.1099 | -0.701 | 0.4831 |  |
| Time 54-69, pooled (%) | +1.2595 | 4.8590 | ±9.7181 | +0.259 | 0.7955 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0960**, F-statistic = **4.33** (p = **4.60e-06**), Residual SE = **16.061** on **334** df, AIC = **2915.0**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.1534** | 8.3434 | ±16.6868 | **+6.730** | **1.69e-11** | *** |
| Education: graduate level (vs college) | -3.5592 | 1.8632 | ±3.7264 | -1.910 | 0.0561 | . |
| Education: high school or below (vs college) | +0.3308 | 3.3878 | ±6.7756 | +0.098 | 0.9222 |  |
| Site: UCSD (vs UAB) | -1.8995 | 2.3354 | ±4.6709 | -0.813 | 0.4160 |  |
| **Site: UW (vs UAB)** | **-4.4367** | 2.1322 | ±4.2643 | **-2.081** | **0.0374** | * |
| **Age (years)** | **-0.2950** | 0.0878 | ±0.1755 | **-3.362** | **7.74e-04** | *** |
| **BMI (kg/m2)** | **+0.4694** | 0.1585 | ±0.3170 | **+2.962** | **0.0031** | ** |
| Hypertension | -0.0963 | 2.1347 | ±4.2694 | -0.045 | 0.9640 |  |
| High cholesterol | -0.5922 | 1.9592 | ±3.9185 | -0.302 | 0.7625 |  |
| Kidney disease | -2.1681 | 5.2494 | ±10.4988 | -0.413 | 0.6796 |  |
| Circulatory disease | -1.7866 | 2.5473 | ±5.0946 | -0.701 | 0.4831 |  |
| Avg. daily time 54-69 (%) | -0.3944 | 4.9736 | ±9.9473 | -0.079 | 0.9368 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **346**, R² = **0.1251**, Adj R² = **0.0963**, F-statistic = **4.34** (p = **4.41e-06**), Residual SE = **16.059** on **334** df, AIC = **2914.9**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8018** | 8.3335 | ±16.6671 | **+6.696** | **2.14e-11** | *** |
| Education: graduate level (vs college) | -3.5210 | 1.8625 | ±3.7251 | -1.890 | 0.0587 | . |
| Education: high school or below (vs college) | +0.3065 | 3.3569 | ±6.7137 | +0.091 | 0.9272 |  |
| Site: UCSD (vs UAB) | -1.8281 | 2.3371 | ±4.6742 | -0.782 | 0.4341 |  |
| **Site: UW (vs UAB)** | **-4.3726** | 2.1383 | ±4.2766 | **-2.045** | **0.0409** | * |
| **Age (years)** | **-0.2948** | 0.0876 | ±0.1751 | **-3.367** | **7.60e-04** | *** |
| **BMI (kg/m2)** | **+0.4699** | 0.1581 | ±0.3161 | **+2.973** | **0.0030** | ** |
| Hypertension | -0.0227 | 2.1069 | ±4.2138 | -0.011 | 0.9914 |  |
| High cholesterol | -0.6691 | 1.9567 | ±3.9133 | -0.342 | 0.7324 |  |
| Kidney disease | -2.0888 | 5.2480 | ±10.4960 | -0.398 | 0.6906 |  |
| Circulatory disease | -1.8117 | 2.5554 | ±5.1108 | -0.709 | 0.4783 |  |
| Time < 70 (%) | +1.4040 | 4.1883 | ±8.3766 | +0.335 | 0.7375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0960**, F-statistic = **4.33** (p = **4.61e-06**), Residual SE = **16.061** on **334** df, AIC = **2915.0**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0957** | 8.3405 | ±16.6810 | **+6.726** | **1.75e-11** | *** |
| Education: graduate level (vs college) | -3.5496 | 1.8597 | ±3.7195 | -1.909 | 0.0563 | . |
| Education: high school or below (vs college) | +0.3225 | 3.3822 | ±6.7644 | +0.095 | 0.9240 |  |
| Site: UCSD (vs UAB) | -1.8931 | 2.3341 | ±4.6683 | -0.811 | 0.4173 |  |
| **Site: UW (vs UAB)** | **-4.4325** | 2.1327 | ±4.2653 | **-2.078** | **0.0377** | * |
| **Age (years)** | **-0.2951** | 0.0877 | ±0.1754 | **-3.365** | **7.67e-04** | *** |
| **BMI (kg/m2)** | **+0.4696** | 0.1585 | ±0.3170 | **+2.963** | **0.0030** | ** |
| Hypertension | -0.0700 | 2.1236 | ±4.2471 | -0.033 | 0.9737 |  |
| High cholesterol | -0.6054 | 1.9493 | ±3.8986 | -0.311 | 0.7561 |  |
| Kidney disease | -2.1563 | 5.2482 | ±10.4964 | -0.411 | 0.6812 |  |
| Circulatory disease | -1.7942 | 2.5506 | ±5.1012 | -0.703 | 0.4818 |  |
| Avg. daily time < 70 (%) | -0.0127 | 4.3614 | ±8.7228 | -0.003 | 0.9977 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1251**, Adj R² = **0.0963**, F-statistic = **4.34** (p = **4.40e-06**), Residual SE = **16.059** on **334** df, AIC = **2914.9**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +612.0238 | 1422.0578 | ±2844.1156 | +0.430 | 0.6669 |  |
| Education: graduate level (vs college) | -3.5366 | 1.8513 | ±3.7026 | -1.910 | 0.0561 | . |
| Education: high school or below (vs college) | +0.3911 | 3.3834 | ±6.7668 | +0.116 | 0.9080 |  |
| Site: UCSD (vs UAB) | -1.8048 | 2.3416 | ±4.6833 | -0.771 | 0.4408 |  |
| **Site: UW (vs UAB)** | **-4.3926** | 2.1333 | ±4.2666 | **-2.059** | **0.0395** | * |
| **Age (years)** | **-0.2937** | 0.0876 | ±0.1752 | **-3.352** | **8.02e-04** | *** |
| **BMI (kg/m2)** | **+0.4668** | 0.1584 | ±0.3168 | **+2.947** | **0.0032** | ** |
| Hypertension | -0.1173 | 2.1208 | ±4.2416 | -0.055 | 0.9559 |  |
| High cholesterol | -0.6011 | 1.9290 | ±3.8579 | -0.312 | 0.7553 |  |
| Kidney disease | -2.0934 | 5.2392 | ±10.4783 | -0.400 | 0.6895 |  |
| Circulatory disease | -1.8740 | 2.5694 | ±5.1388 | -0.729 | 0.4658 |  |
| Time 54-250, pooled (%) | -5.5607 | 14.2245 | ±28.4491 | -0.391 | 0.6959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1250**, Adj R² = **0.0962**, F-statistic = **4.34** (p = **4.48e-06**), Residual SE = **16.060** on **334** df, AIC = **2914.9**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +570.8282 | 1863.9847 | ±3727.9694 | +0.306 | 0.7594 |  |
| Education: graduate level (vs college) | -3.5558 | 1.8482 | ±3.6965 | -1.924 | 0.0544 | . |
| Education: high school or below (vs college) | +0.3434 | 3.3692 | ±6.7383 | +0.102 | 0.9188 |  |
| Site: UCSD (vs UAB) | -1.8570 | 2.3350 | ±4.6700 | -0.795 | 0.4264 |  |
| **Site: UW (vs UAB)** | **-4.4282** | 2.1329 | ±4.2659 | **-2.076** | **0.0379** | * |
| **Age (years)** | **-0.2943** | 0.0876 | ±0.1752 | **-3.360** | **7.80e-04** | *** |
| **BMI (kg/m2)** | **+0.4683** | 0.1584 | ±0.3168 | **+2.956** | **0.0031** | ** |
| Hypertension | -0.0826 | 2.1096 | ±4.2193 | -0.039 | 0.9688 |  |
| High cholesterol | -0.6009 | 1.9320 | ±3.8639 | -0.311 | 0.7558 |  |
| Kidney disease | -2.1268 | 5.2367 | ±10.4733 | -0.406 | 0.6846 |  |
| Circulatory disease | -1.8823 | 2.5846 | ±5.1692 | -0.728 | 0.4665 |  |
| Avg. daily time 54-250 (%) | -5.1480 | 18.6447 | ±37.2894 | -0.276 | 0.7825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **346**, R² = **0.1318**, Adj R² = **0.1032**, F-statistic = **4.61** (p = **1.53e-06**), Residual SE = **15.997** on **334** df, AIC = **2912.2**, BIC = **2958.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.0040** | 9.1593 | ±18.3186 | **+5.896** | **3.72e-09** | *** |
| Education: graduate level (vs college) | -3.5191 | 1.8481 | ±3.6962 | -1.904 | 0.0569 | . |
| Education: high school or below (vs college) | +0.5574 | 3.3548 | ±6.7097 | +0.166 | 0.8680 |  |
| Site: UCSD (vs UAB) | -1.8692 | 2.3518 | ±4.7036 | -0.795 | 0.4267 |  |
| **Site: UW (vs UAB)** | **-4.4710** | 2.1224 | ±4.2447 | **-2.107** | **0.0352** | * |
| **Age (years)** | **-0.2888** | 0.0892 | ±0.1783 | **-3.239** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.4773** | 0.1755 | ±0.3510 | **+2.720** | **0.0065** | ** |
| Hypertension | -0.2995 | 2.0711 | ±4.1423 | -0.145 | 0.8850 |  |
| High cholesterol | -0.4689 | 1.9370 | ±3.8740 | -0.242 | 0.8087 |  |
| Kidney disease | -2.6668 | 5.3587 | ±10.7174 | -0.498 | 0.6187 |  |
| Circulatory disease | -1.8252 | 2.4788 | ±4.9575 | -0.736 | 0.4615 |  |
| Time 181-250, pooled (%) | +5.1023 | 3.3254 | ±6.6508 | +1.534 | 0.1249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **346**, R² = **0.1393**, Adj R² = **0.1109**, F-statistic = **4.91** (p = **4.59e-07**), Residual SE = **15.928** on **334** df, AIC = **2909.2**, BIC = **2955.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0476** | 8.6212 | ±17.2424 | **+6.153** | **7.60e-10** | *** |
| Education: graduate level (vs college) | -3.5100 | 1.8373 | ±3.6746 | -1.910 | 0.0561 | . |
| Education: high school or below (vs college) | +0.8307 | 3.3395 | ±6.6790 | +0.249 | 0.8036 |  |
| Site: UCSD (vs UAB) | -1.7369 | 2.3334 | ±4.6667 | -0.744 | 0.4566 |  |
| **Site: UW (vs UAB)** | **-4.4826** | 2.1066 | ±4.2132 | **-2.128** | **0.0333** | * |
| **Age (years)** | **-0.2777** | 0.0883 | ±0.1766 | **-3.145** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.4732** | 0.1634 | ±0.3267 | **+2.896** | **0.0038** | ** |
| Hypertension | -0.3729 | 2.0710 | ±4.1419 | -0.180 | 0.8571 |  |
| High cholesterol | -0.5797 | 1.9134 | ±3.8267 | -0.303 | 0.7619 |  |
| Kidney disease | -2.4955 | 5.3892 | ±10.7784 | -0.463 | 0.6433 |  |
| Circulatory disease | -1.8583 | 2.4900 | ±4.9800 | -0.746 | 0.4555 |  |
| **Avg. daily time 181-250 (%)** | **+7.2347** | 3.1483 | ±6.2965 | **+2.298** | **0.0216** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **346**, R² = **0.1317**, Adj R² = **0.1031**, F-statistic = **4.61** (p = **1.55e-06**), Residual SE = **15.998** on **334** df, AIC = **2912.2**, BIC = **2958.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.9970** | 9.1671 | ±18.3343 | **+5.890** | **3.86e-09** | *** |
| Education: graduate level (vs college) | -3.5147 | 1.8483 | ±3.6965 | -1.902 | 0.0572 | . |
| Education: high school or below (vs college) | +0.5594 | 3.3547 | ±6.7094 | +0.167 | 0.8676 |  |
| Site: UCSD (vs UAB) | -1.8690 | 2.3519 | ±4.7037 | -0.795 | 0.4268 |  |
| **Site: UW (vs UAB)** | **-4.4737** | 2.1223 | ±4.2446 | **-2.108** | **0.0350** | * |
| **Age (years)** | **-0.2887** | 0.0892 | ±0.1784 | **-3.237** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.4775** | 0.1756 | ±0.3511 | **+2.719** | **0.0065** | ** |
| Hypertension | -0.2965 | 2.0713 | ±4.1427 | -0.143 | 0.8862 |  |
| High cholesterol | -0.4750 | 1.9364 | ±3.8727 | -0.245 | 0.8062 |  |
| Kidney disease | -2.6632 | 5.3585 | ±10.7170 | -0.497 | 0.6192 |  |
| Circulatory disease | -1.8246 | 2.4793 | ±4.9587 | -0.736 | 0.4618 |  |
| Time > 180 (%) | +5.0724 | 3.3199 | ±6.6397 | +1.528 | 0.1265 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1391**, Adj R² = **0.1108**, F-statistic = **4.91** (p = **4.68e-07**), Residual SE = **15.930** on **334** df, AIC = **2909.3**, BIC = **2955.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0340** | 8.6313 | ±17.2626 | **+6.144** | **8.03e-10** | *** |
| Education: graduate level (vs college) | -3.5029 | 1.8374 | ±3.6749 | -1.906 | 0.0566 | . |
| Education: high school or below (vs college) | +0.8333 | 3.3395 | ±6.6789 | +0.250 | 0.8030 |  |
| Site: UCSD (vs UAB) | -1.7373 | 2.3335 | ±4.6670 | -0.744 | 0.4566 |  |
| **Site: UW (vs UAB)** | **-4.4870** | 2.1068 | ±4.2135 | **-2.130** | **0.0332** | * |
| **Age (years)** | **-0.2775** | 0.0883 | ±0.1766 | **-3.142** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.4735** | 0.1635 | ±0.3271 | **+2.896** | **0.0038** | ** |
| Hypertension | -0.3686 | 2.0712 | ±4.1424 | -0.178 | 0.8587 |  |
| High cholesterol | -0.5881 | 1.9133 | ±3.8265 | -0.307 | 0.7586 |  |
| Kidney disease | -2.4927 | 5.3890 | ±10.7781 | -0.463 | 0.6437 |  |
| Circulatory disease | -1.8574 | 2.4906 | ±4.9811 | -0.746 | 0.4558 |  |
| **Avg. daily time > 180 (%)** | **+7.1950** | 3.1410 | ±6.2821 | **+2.291** | **0.0220** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1380**, Adj R² = **0.1096**, F-statistic = **4.86** (p = **5.60e-07**), Residual SE = **15.940** on **334** df, AIC = **2909.7**, BIC = **2955.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.1399** | 8.0033 | ±16.0066 | **+6.765** | **1.34e-11** | *** |
| Education: graduate level (vs college) | -3.2349 | 1.8208 | ±3.6416 | -1.777 | 0.0756 | . |
| Education: high school or below (vs college) | +0.2916 | 3.3576 | ±6.7151 | +0.087 | 0.9308 |  |
| Site: UCSD (vs UAB) | -1.7710 | 2.3043 | ±4.6086 | -0.769 | 0.4421 |  |
| **Site: UW (vs UAB)** | **-4.6148** | 2.1009 | ±4.2017 | **-2.197** | **0.0280** | * |
| **Age (years)** | **-0.2567** | 0.0873 | ±0.1745 | **-2.943** | **0.0033** | ** |
| **BMI (kg/m2)** | **+0.4396** | 0.1546 | ±0.3092 | **+2.843** | **0.0045** | ** |
| Hypertension | -0.3435 | 2.0753 | ±4.1506 | -0.165 | 0.8686 |  |
| High cholesterol | -0.8885 | 1.9052 | ±3.8104 | -0.466 | 0.6410 |  |
| Kidney disease | -2.6029 | 5.1433 | ±10.2865 | -0.506 | 0.6128 |  |
| Circulatory disease | -1.7326 | 2.5294 | ±5.0588 | -0.685 | 0.4933 |  |
| **Nocturnal time > 180 (%)** | **+5.6971** | 2.4600 | ±4.9199 | **+2.316** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
