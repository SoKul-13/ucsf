# Phase 6 model output tables - All (analysis base) - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 1,125; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1253**, F-statistic = **17.10** (p = **3.89e-29**), Residual SE = **3758.368** on **1114** df, AIC = **21725.0**, BIC = **21780.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18042.5887** | 869.6609 | ±1739.3219 | **+20.747** | **1.31e-95** | *** |
| **Education: graduate level (vs college)** | **-533.0111** | 230.0878 | ±460.1757 | **-2.317** | **0.0205** | * |
| **Education: high school or below (vs college)** | **+1602.2738** | 598.8933 | ±1197.7867 | **+2.675** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.8789 | 308.9740 | ±617.9480 | +0.359 | 0.7197 |  |
| Site: UW (vs UAB) | -206.5139 | 274.3920 | ±548.7840 | -0.753 | 0.4517 |  |
| **Age (years)** | **-115.6421** | 10.5083 | ±21.0166 | **-11.005** | **3.62e-28** | *** |
| BMI (kg/m2) | -31.7766 | 17.8849 | ±35.7697 | -1.777 | 0.0756 | . |
| Hypertension | -106.7198 | 266.2986 | ±532.5973 | -0.401 | 0.6886 |  |
| High cholesterol | -76.1910 | 230.7635 | ±461.5269 | -0.330 | 0.7413 |  |
| Kidney disease | -337.5699 | 532.4419 | ±1064.8838 | -0.634 | 0.5261 |  |
| Circulatory disease | -651.5480 | 357.0262 | ±714.0525 | -1.825 | 0.0680 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1125**, R² = **0.1371**, Adj R² = **0.1286**, F-statistic = **16.08** (p = **1.38e-29**), Residual SE = **3751.207** on **1113** df, AIC = **21721.7**, BIC = **21782.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15537.1814** | 1331.5770 | ±2663.1539 | **+11.668** | **1.85e-31** | *** |
| **Education: graduate level (vs college)** | **-532.8054** | 229.5647 | ±459.1294 | **-2.321** | **0.0203** | * |
| **Education: high school or below (vs college)** | **+1547.2254** | 600.2836 | ±1200.5671 | **+2.577** | **0.0100** | ** |
| Site: UCSD (vs UAB) | +87.6834 | 309.1081 | ±618.2162 | +0.284 | 0.7767 |  |
| Site: UW (vs UAB) | -228.9389 | 273.8332 | ±547.6663 | -0.836 | 0.4031 |  |
| **Age (years)** | **-117.6473** | 10.4852 | ±20.9703 | **-11.220** | **3.24e-29** | *** |
| **BMI (kg/m2)** | **-35.2503** | 17.9424 | ±35.8848 | **-1.965** | **0.0495** | * |
| Hypertension | -130.4308 | 265.4728 | ±530.9456 | -0.491 | 0.6232 |  |
| High cholesterol | -147.4812 | 233.0321 | ±466.0643 | -0.633 | 0.5268 |  |
| Kidney disease | -335.8216 | 530.0786 | ±1060.1572 | -0.634 | 0.5264 |  |
| Circulatory disease | -679.7218 | 355.0559 | ±710.1118 | -1.914 | 0.0556 | . |
| **HbA1c (%)** | **+493.1986** | 196.9678 | ±393.9356 | **+2.504** | **0.0123** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.66e-28**), Residual SE = **3760.056** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18036.1630** | 1074.4248 | ±2148.8496 | **+16.787** | **3.05e-63** | *** |
| **Education: graduate level (vs college)** | **-533.1193** | 230.7736 | ±461.5472 | **-2.310** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+1602.0796** | 599.4959 | ±1198.9919 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.8304 | 309.4384 | ±618.8769 | +0.358 | 0.7202 |  |
| Site: UW (vs UAB) | -206.7266 | 275.4543 | ±550.9085 | -0.750 | 0.4530 |  |
| **Age (years)** | **-115.6452** | 10.5217 | ±21.0434 | **-10.991** | **4.22e-28** | *** |
| BMI (kg/m2) | -31.7849 | 17.9996 | ±35.9992 | -1.766 | 0.0774 | . |
| Hypertension | -106.9141 | 267.4302 | ±534.8603 | -0.400 | 0.6893 |  |
| High cholesterol | -76.3787 | 230.9019 | ±461.8038 | -0.331 | 0.7408 |  |
| Kidney disease | -337.8195 | 532.5187 | ±1065.0375 | -0.634 | 0.5258 |  |
| Circulatory disease | -651.6431 | 357.0931 | ±714.1861 | -1.825 | 0.0680 | . |
| Mean glucose (mg/dL) | +0.0596 | 6.1728 | ±12.3456 | +0.010 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.66e-28**), Residual SE = **3760.056** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18027.9208** | 1721.0387 | ±3442.0773 | **+10.475** | **1.13e-25** | *** |
| **Education: graduate level (vs college)** | **-533.1193** | 230.7736 | ±461.5472 | **-2.310** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+1602.0796** | 599.4959 | ±1198.9919 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.8304 | 309.4384 | ±618.8769 | +0.358 | 0.7202 |  |
| Site: UW (vs UAB) | -206.7266 | 275.4543 | ±550.9085 | -0.750 | 0.4530 |  |
| **Age (years)** | **-115.6452** | 10.5217 | ±21.0434 | **-10.991** | **4.22e-28** | *** |
| BMI (kg/m2) | -31.7849 | 17.9996 | ±35.9992 | -1.766 | 0.0774 | . |
| Hypertension | -106.9141 | 267.4302 | ±534.8603 | -0.400 | 0.6893 |  |
| High cholesterol | -76.3787 | 230.9019 | ±461.8038 | -0.331 | 0.7408 |  |
| Kidney disease | -337.8195 | 532.5187 | ±1065.0375 | -0.634 | 0.5258 |  |
| Circulatory disease | -651.6431 | 357.0931 | ±714.1861 | -1.825 | 0.0680 | . |
| GMI (%) | +2.4901 | 258.0605 | ±516.1211 | +0.010 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.53e-28**), Residual SE = **3759.777** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17792.1541** | 1042.2984 | ±2084.5967 | **+17.070** | **2.48e-65** | *** |
| **Education: graduate level (vs college)** | **-535.4184** | 230.3199 | ±460.6398 | **-2.325** | **0.0201** | * |
| **Education: high school or below (vs college)** | **+1594.0897** | 599.2489 | ±1198.4978 | **+2.660** | **0.0078** | ** |
| Site: UCSD (vs UAB) | +105.9055 | 309.6337 | ±619.2674 | +0.342 | 0.7323 |  |
| Site: UW (vs UAB) | -214.8009 | 274.3782 | ±548.7563 | -0.783 | 0.4337 |  |
| **Age (years)** | **-115.5412** | 10.5160 | ±21.0320 | **-10.987** | **4.41e-28** | *** |
| BMI (kg/m2) | -32.7004 | 18.1648 | ±36.3297 | -1.800 | 0.0718 | . |
| Hypertension | -112.9959 | 266.8552 | ±533.7104 | -0.423 | 0.6720 |  |
| High cholesterol | -85.5867 | 231.7794 | ±463.5588 | -0.369 | 0.7119 |  |
| Kidney disease | -340.7841 | 532.3796 | ±1064.7592 | -0.640 | 0.5221 |  |
| Circulatory disease | -653.2739 | 356.9776 | ±713.9552 | -1.830 | 0.0672 | . |
| Nocturnal mean 00-06h (mg/dL) | +2.3740 | 5.8350 | ±11.6699 | +0.407 | 0.6841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.65e-28**), Residual SE = **3760.027** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18088.4039** | 920.6278 | ±1841.2557 | **+19.648** | **6.03e-86** | *** |
| **Education: graduate level (vs college)** | **-532.6974** | 230.4218 | ±460.8437 | **-2.312** | **0.0208** | * |
| **Education: high school or below (vs college)** | **+1602.5657** | 599.4784 | ±1198.9568 | **+2.673** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +109.4137 | 310.2195 | ±620.4390 | +0.353 | 0.7243 |  |
| Site: UW (vs UAB) | -205.0697 | 274.4960 | ±548.9920 | -0.747 | 0.4550 |  |
| **Age (years)** | **-115.5775** | 10.5307 | ±21.0615 | **-10.975** | **5.03e-28** | *** |
| BMI (kg/m2) | -31.8212 | 17.8684 | ±35.7368 | -1.781 | 0.0749 | . |
| Hypertension | -103.8317 | 266.9518 | ±533.9036 | -0.389 | 0.6973 |  |
| High cholesterol | -75.3228 | 230.7358 | ±461.4716 | -0.326 | 0.7441 |  |
| Kidney disease | -331.9697 | 533.7892 | ±1067.5783 | -0.622 | 0.5340 |  |
| Circulatory disease | -650.2989 | 356.9960 | ±713.9920 | -1.822 | 0.0685 | . |
| Glucose SD, pooled (mg/dL) | -2.3466 | 17.7812 | ±35.5624 | -0.132 | 0.8950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.60e-28**), Residual SE = **3759.914** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18133.3085** | 910.9309 | ±1821.8617 | **+19.906** | **3.59e-88** | *** |
| **Education: graduate level (vs college)** | **-531.8678** | 230.4564 | ±460.9129 | **-2.308** | **0.0210** | * |
| **Education: high school or below (vs college)** | **+1603.4192** | 599.5374 | ±1199.0748 | **+2.674** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +108.4044 | 309.7441 | ±619.4883 | +0.350 | 0.7264 |  |
| Site: UW (vs UAB) | -202.7288 | 274.7589 | ±549.5178 | -0.738 | 0.4606 |  |
| **Age (years)** | **-115.4582** | 10.5412 | ±21.0825 | **-10.953** | **6.43e-28** | *** |
| BMI (kg/m2) | -31.7953 | 17.9041 | ±35.8082 | -1.776 | 0.0758 | . |
| Hypertension | -100.4268 | 266.7625 | ±533.5250 | -0.376 | 0.7066 |  |
| High cholesterol | -74.2244 | 230.8250 | ±461.6500 | -0.322 | 0.7478 |  |
| Kidney disease | -325.6053 | 533.5591 | ±1067.1183 | -0.610 | 0.5417 |  |
| Circulatory disease | -648.8405 | 357.0461 | ±714.0922 | -1.817 | 0.0692 | . |
| Avg. daily SD (mg/dL) | -5.4417 | 18.8882 | ±37.7764 | -0.288 | 0.7733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.63e-28**), Residual SE = **3759.999** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18136.0180** | 998.2492 | ±1996.4984 | **+18.168** | **9.28e-74** | *** |
| **Education: graduate level (vs college)** | **-533.9678** | 230.0846 | ±460.1693 | **-2.321** | **0.0203** | * |
| **Education: high school or below (vs college)** | **+1600.4212** | 600.7456 | ±1201.4912 | **+2.664** | **0.0077** | ** |
| Site: UCSD (vs UAB) | +107.2043 | 311.6562 | ±623.3123 | +0.344 | 0.7309 |  |
| Site: UW (vs UAB) | -207.0085 | 274.6546 | ±549.3092 | -0.754 | 0.4510 |  |
| **Age (years)** | **-115.5552** | 10.5286 | ±21.0572 | **-10.975** | **5.02e-28** | *** |
| BMI (kg/m2) | -31.9608 | 17.8550 | ±35.7100 | -1.790 | 0.0735 | . |
| Hypertension | -104.2041 | 266.4931 | ±532.9862 | -0.391 | 0.6958 |  |
| High cholesterol | -77.4133 | 231.3502 | ±462.7004 | -0.335 | 0.7379 |  |
| Kidney disease | -331.4434 | 534.0917 | ±1068.1834 | -0.621 | 0.5349 |  |
| Circulatory disease | -650.8747 | 357.3452 | ±714.6905 | -1.821 | 0.0685 | . |
| CV (%) | -5.1921 | 28.7356 | ±57.4711 | -0.181 | 0.8566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.60e-28**), Residual SE = **3759.931** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18193.2533** | 1045.9340 | ±2091.8679 | **+17.394** | **9.12e-68** | *** |
| **Education: graduate level (vs college)** | **-531.3316** | 229.9776 | ±459.9552 | **-2.310** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+1603.2058** | 599.2856 | ±1198.5713 | **+2.675** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +116.2072 | 310.9079 | ±621.8158 | +0.374 | 0.7086 |  |
| Site: UW (vs UAB) | -207.1548 | 274.5064 | ±549.0128 | -0.755 | 0.4505 |  |
| **Age (years)** | **-115.7823** | 10.5325 | ±21.0650 | **-10.993** | **4.14e-28** | *** |
| BMI (kg/m2) | -31.5480 | 17.8580 | ±35.7161 | -1.767 | 0.0773 | . |
| Hypertension | -110.9964 | 266.2361 | ±532.4723 | -0.417 | 0.6767 |  |
| High cholesterol | -75.1039 | 231.1485 | ±462.2969 | -0.325 | 0.7452 |  |
| Kidney disease | -344.0027 | 533.8871 | ±1067.7741 | -0.644 | 0.5194 |  |
| Circulatory disease | -652.2786 | 357.1356 | ±714.2711 | -1.826 | 0.0678 | . |
| Mean / SD ratio | -25.3926 | 91.5093 | ±183.0186 | -0.277 | 0.7814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.50e-28**), Residual SE = **3759.703** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18299.1497** | 1049.2592 | ±2098.5184 | **+17.440** | **4.10e-68** | *** |
| **Education: graduate level (vs college)** | **-532.1095** | 230.2177 | ±460.4354 | **-2.311** | **0.0208** | * |
| **Education: high school or below (vs college)** | **+1600.8183** | 598.5698 | ±1197.1396 | **+2.674** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +118.0230 | 309.8545 | ±619.7090 | +0.381 | 0.7033 |  |
| Site: UW (vs UAB) | -208.8094 | 274.4620 | ±548.9240 | -0.761 | 0.4468 |  |
| **Age (years)** | **-115.9923** | 10.5548 | ±21.1097 | **-10.989** | **4.29e-28** | *** |
| BMI (kg/m2) | -31.6184 | 17.8716 | ±35.7433 | -1.769 | 0.0769 | . |
| Hypertension | -112.0004 | 266.0356 | ±532.0712 | -0.421 | 0.6738 |  |
| High cholesterol | -74.6548 | 231.0001 | ±462.0003 | -0.323 | 0.7466 |  |
| Kidney disease | -350.4720 | 534.1571 | ±1068.3142 | -0.656 | 0.5117 |  |
| Circulatory disease | -652.1797 | 357.2171 | ±714.4341 | -1.826 | 0.0679 | . |
| Avg. daily mean/SD | -35.4788 | 76.3933 | ±152.7867 | -0.464 | 0.6423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1125**, R² = **0.1445**, Adj R² = **0.1360**, F-statistic = **17.09** (p = **1.48e-31**), Residual SE = **3735.169** on **1113** df, AIC = **21712.0**, BIC = **21772.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15724.4790** | 1042.7579 | ±2085.5158 | **+15.080** | **2.20e-51** | *** |
| **Education: graduate level (vs college)** | **-515.5912** | 229.0025 | ±458.0049 | **-2.251** | **0.0244** | * |
| **Education: high school or below (vs college)** | **+1568.7427** | 593.6309 | ±1187.2619 | **+2.643** | **0.0082** | ** |
| Site: UCSD (vs UAB) | +168.8285 | 307.9783 | ±615.9566 | +0.548 | 0.5836 |  |
| Site: UW (vs UAB) | -142.6833 | 275.7380 | ±551.4759 | -0.517 | 0.6048 |  |
| **Age (years)** | **-113.9293** | 10.3839 | ±20.7677 | **-10.972** | **5.22e-28** | *** |
| BMI (kg/m2) | -30.7829 | 17.6526 | ±35.3053 | -1.744 | 0.0812 | . |
| Hypertension | -95.8597 | 264.9230 | ±529.8461 | -0.362 | 0.7175 |  |
| High cholesterol | -44.0260 | 227.9099 | ±455.8199 | -0.193 | 0.8468 |  |
| Kidney disease | -408.2573 | 529.4294 | ±1058.8588 | -0.771 | 0.4406 |  |
| Circulatory disease | -618.7274 | 354.8170 | ±709.6340 | -1.744 | 0.0812 | . |
| **MAG (mg/dL/h)** | **+55.6816** | 15.1237 | ±30.2475 | **+3.682** | **2.32e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.826** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17884.7512** | 960.0665 | ±1920.1329 | **+18.629** | **1.88e-77** | *** |
| **Education: graduate level (vs college)** | **-534.6141** | 230.3203 | ±460.6407 | **-2.321** | **0.0203** | * |
| **Education: high school or below (vs college)** | **+1599.2347** | 598.4772 | ±1196.9543 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +114.0933 | 309.8660 | ±619.7319 | +0.368 | 0.7127 |  |
| Site: UW (vs UAB) | -209.6170 | 274.6882 | ±549.3764 | -0.763 | 0.4454 |  |
| **Age (years)** | **-115.8203** | 10.5251 | ±21.0502 | **-11.004** | **3.65e-28** | *** |
| BMI (kg/m2) | -31.3400 | 17.8463 | ±35.6925 | -1.756 | 0.0791 | . |
| Hypertension | -112.2415 | 266.7652 | ±533.5305 | -0.421 | 0.6739 |  |
| High cholesterol | -76.5830 | 230.9166 | ±461.8332 | -0.332 | 0.7402 |  |
| Kidney disease | -349.3725 | 532.9941 | ±1065.9881 | -0.655 | 0.5122 |  |
| Circulatory disease | -654.2223 | 357.1102 | ±714.2205 | -1.832 | 0.0670 | . |
| Avg. daily range (mg/dL) | +1.6278 | 4.4326 | ±8.8653 | +0.367 | 0.7135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1125**, R² = **0.1341**, Adj R² = **0.1255**, F-statistic = **15.67** (p = **8.86e-29**), Residual SE = **3757.821** on **1113** df, AIC = **21725.6**, BIC = **21785.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17783.0807** | 883.3959 | ±1766.7919 | **+20.130** | **4.00e-90** | *** |
| **Education: graduate level (vs college)** | **-534.9954** | 230.2931 | ±460.5861 | **-2.323** | **0.0202** | * |
| **Education: high school or below (vs college)** | **+1611.1013** | 597.8978 | ±1195.7957 | **+2.695** | **0.0070** | ** |
| Site: UCSD (vs UAB) | +130.8299 | 309.5766 | ±619.1532 | +0.423 | 0.6726 |  |
| Site: UW (vs UAB) | -209.7674 | 274.0395 | ±548.0791 | -0.765 | 0.4440 |  |
| **Age (years)** | **-115.3787** | 10.5033 | ±21.0066 | **-10.985** | **4.51e-28** | *** |
| BMI (kg/m2) | -32.6570 | 18.0037 | ±36.0074 | -1.814 | 0.0697 | . |
| Hypertension | -112.8385 | 265.9140 | ±531.8279 | -0.424 | 0.6713 |  |
| High cholesterol | -88.6128 | 231.1491 | ±462.2982 | -0.383 | 0.7015 |  |
| Kidney disease | -351.2047 | 533.8276 | ±1067.6553 | -0.658 | 0.5106 |  |
| Circulatory disease | -659.3186 | 356.5715 | ±713.1430 | -1.849 | 0.0645 | . |
| SD of daily means (mg/dL) | +41.5497 | 36.8219 | ±73.6439 | +1.128 | 0.2592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.54e-28**), Residual SE = **3759.794** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17536.3244** | 1652.7554 | ±3305.5107 | **+10.610** | **2.67e-26** | *** |
| **Education: graduate level (vs college)** | **-531.5959** | 230.2530 | ±460.5060 | **-2.309** | **0.0210** | * |
| **Education: high school or below (vs college)** | **+1604.5192** | 600.3775 | ±1200.7550 | **+2.673** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +107.8338 | 309.7306 | ±619.4613 | +0.348 | 0.7277 |  |
| Site: UW (vs UAB) | -204.8959 | 274.8225 | ±549.6450 | -0.746 | 0.4559 |  |
| **Age (years)** | **-115.6795** | 10.5170 | ±21.0340 | **-10.999** | **3.85e-28** | *** |
| BMI (kg/m2) | -31.6014 | 17.9661 | ±35.9323 | -1.759 | 0.0786 | . |
| Hypertension | -101.7437 | 267.4045 | ±534.8089 | -0.380 | 0.7036 |  |
| High cholesterol | -71.3242 | 230.7065 | ±461.4130 | -0.309 | 0.7572 |  |
| Kidney disease | -326.0376 | 532.5405 | ±1065.0809 | -0.612 | 0.5404 |  |
| Circulatory disease | -647.1084 | 357.4703 | ±714.9406 | -1.810 | 0.0703 | . |
| Time in range 70-180, pooled (%) | +5.2073 | 14.1701 | ±28.3402 | +0.367 | 0.7133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.52e-28**), Residual SE = **3759.742** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17487.2968** | 1659.4358 | ±3318.8716 | **+10.538** | **5.77e-26** | *** |
| **Education: graduate level (vs college)** | **-531.3875** | 230.2744 | ±460.5488 | **-2.308** | **0.0210** | * |
| **Education: high school or below (vs college)** | **+1604.0654** | 600.4921 | ±1200.9841 | **+2.671** | **0.0076** | ** |
| Site: UCSD (vs UAB) | +107.7455 | 309.7049 | ±619.4097 | +0.348 | 0.7279 |  |
| Site: UW (vs UAB) | -204.8528 | 274.8039 | ±549.6079 | -0.745 | 0.4560 |  |
| **Age (years)** | **-115.6664** | 10.5156 | ±21.0312 | **-11.000** | **3.84e-28** | *** |
| BMI (kg/m2) | -31.5504 | 17.9786 | ±35.9573 | -1.755 | 0.0793 | . |
| Hypertension | -101.3386 | 267.3718 | ±534.7436 | -0.379 | 0.7047 |  |
| High cholesterol | -70.5253 | 230.8207 | ±461.6414 | -0.306 | 0.7600 |  |
| Kidney disease | -325.1354 | 532.7017 | ±1065.4035 | -0.610 | 0.5416 |  |
| Circulatory disease | -646.7315 | 357.4873 | ±714.9745 | -1.809 | 0.0704 | . |
| Avg. daily time in range 70-180 (%) | +5.6761 | 14.1169 | ±28.2337 | +0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.65e-28**), Residual SE = **3760.028** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18060.6762** | 891.1692 | ±1782.3383 | **+20.266** | **2.55e-91** | *** |
| **Education: graduate level (vs college)** | **-533.9451** | 230.8992 | ±461.7983 | **-2.312** | **0.0208** | * |
| **Education: high school or below (vs college)** | **+1598.8816** | 597.8636 | ±1195.7272 | **+2.674** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +105.9574 | 310.4141 | ±620.8282 | +0.341 | 0.7328 |  |
| Site: UW (vs UAB) | -208.6379 | 275.1269 | ±550.2538 | -0.758 | 0.4483 |  |
| **Age (years)** | **-115.7418** | 10.5973 | ±21.1946 | **-10.922** | **9.06e-28** | *** |
| BMI (kg/m2) | -31.7211 | 17.8837 | ±35.7673 | -1.774 | 0.0761 | . |
| Hypertension | -106.3525 | 266.7766 | ±533.5533 | -0.399 | 0.6901 |  |
| High cholesterol | -78.1774 | 230.9408 | ±461.8815 | -0.339 | 0.7350 |  |
| Kidney disease | -338.4214 | 533.3407 | ±1066.6814 | -0.635 | 0.5257 |  |
| Circulatory disease | -647.8504 | 357.2582 | ±714.5165 | -1.813 | 0.0698 | . |
| Any reading < 54 during wear (0/1) | -31.5991 | 242.4173 | ±484.8347 | -0.130 | 0.8963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1333**, Adj R² = **0.1247**, F-statistic = **15.56** (p = **1.45e-28**), Residual SE = **3759.574** on **1113** df, AIC = **21726.7**, BIC = **21787.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18087.6088** | 877.3417 | ±1754.6835 | **+20.616** | **1.96e-94** | *** |
| **Education: graduate level (vs college)** | **-535.2651** | 230.3365 | ±460.6731 | **-2.324** | **0.0201** | * |
| **Education: high school or below (vs college)** | **+1592.6177** | 599.8072 | ±1199.6145 | **+2.655** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +91.0565 | 310.8824 | ±621.7647 | +0.293 | 0.7696 |  |
| Site: UW (vs UAB) | -221.5373 | 274.3675 | ±548.7349 | -0.807 | 0.4194 |  |
| **Age (years)** | **-115.7600** | 10.5153 | ±21.0307 | **-11.009** | **3.47e-28** | *** |
| BMI (kg/m2) | -31.9148 | 17.9106 | ±35.8213 | -1.782 | 0.0748 | . |
| Hypertension | -111.1918 | 266.1753 | ±532.3506 | -0.418 | 0.6761 |  |
| High cholesterol | -85.2060 | 231.5071 | ±463.0142 | -0.368 | 0.7128 |  |
| Kidney disease | -333.2488 | 532.1154 | ±1064.2307 | -0.626 | 0.5311 |  |
| Circulatory disease | -651.5353 | 357.1507 | ±714.3014 | -1.824 | 0.0681 | . |
| Time < 54 (%) | -101.5489 | 142.4474 | ±284.8948 | -0.713 | 0.4759 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.61e-28**), Residual SE = **3759.949** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18057.9889** | 875.5171 | ±1751.0342 | **+20.626** | **1.62e-94** | *** |
| **Education: graduate level (vs college)** | **-534.5645** | 230.4510 | ±460.9020 | **-2.320** | **0.0204** | * |
| **Education: high school or below (vs college)** | **+1597.7786** | 599.4535 | ±1198.9071 | **+2.665** | **0.0077** | ** |
| Site: UCSD (vs UAB) | +102.5453 | 310.7326 | ±621.4652 | +0.330 | 0.7414 |  |
| Site: UW (vs UAB) | -214.3682 | 274.7618 | ±549.5236 | -0.780 | 0.4353 |  |
| **Age (years)** | **-115.6250** | 10.5131 | ±21.0263 | **-10.998** | **3.90e-28** | *** |
| BMI (kg/m2) | -31.8232 | 17.9316 | ±35.8632 | -1.775 | 0.0759 | . |
| Hypertension | -109.6120 | 266.1674 | ±532.3348 | -0.412 | 0.6805 |  |
| High cholesterol | -80.2281 | 231.2077 | ±462.4153 | -0.347 | 0.7286 |  |
| Kidney disease | -335.7177 | 532.3659 | ±1064.7319 | -0.631 | 0.5283 |  |
| Circulatory disease | -652.3369 | 356.9709 | ±713.9418 | -1.827 | 0.0676 | . |
| Avg. daily time < 54 (%) | -64.1694 | 225.5860 | ±451.1720 | -0.284 | 0.7761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.52e-28**), Residual SE = **3759.742** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18086.3039** | 886.0161 | ±1772.0322 | **+20.413** | **1.28e-92** | *** |
| **Education: graduate level (vs college)** | **-537.9523** | 230.6103 | ±461.2206 | **-2.333** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+1589.8651** | 598.9022 | ±1197.8043 | **+2.655** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +99.6940 | 308.5371 | ±617.0743 | +0.323 | 0.7466 |  |
| Site: UW (vs UAB) | -218.2815 | 272.8285 | ±545.6570 | -0.800 | 0.4237 |  |
| **Age (years)** | **-115.8278** | 10.5475 | ±21.0950 | **-10.982** | **4.69e-28** | *** |
| BMI (kg/m2) | -31.6446 | 17.9118 | ±35.8236 | -1.767 | 0.0773 | . |
| Hypertension | -110.8634 | 266.2872 | ±532.5744 | -0.416 | 0.6772 |  |
| High cholesterol | -82.6320 | 231.6347 | ±463.2693 | -0.357 | 0.7213 |  |
| Kidney disease | -338.2275 | 532.8798 | ±1065.7597 | -0.635 | 0.5256 |  |
| Circulatory disease | -651.5544 | 357.0067 | ±714.0134 | -1.825 | 0.0680 | . |
| Time 54-69, pooled (%) | -33.5920 | 87.7037 | ±175.4074 | -0.383 | 0.7017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.828** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18074.3324** | 882.8468 | ±1765.6937 | **+20.473** | **3.76e-93** | *** |
| **Education: graduate level (vs college)** | **-537.7639** | 230.5860 | ±461.1720 | **-2.332** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+1590.8842** | 599.0536 | ±1198.1073 | **+2.656** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +103.1152 | 308.5115 | ±617.0229 | +0.334 | 0.7382 |  |
| Site: UW (vs UAB) | -216.5089 | 273.1347 | ±546.2695 | -0.793 | 0.4280 |  |
| **Age (years)** | **-115.7420** | 10.5318 | ±21.0635 | **-10.990** | **4.28e-28** | *** |
| BMI (kg/m2) | -31.6711 | 17.9136 | ±35.8271 | -1.768 | 0.0771 | . |
| Hypertension | -110.6750 | 266.4153 | ±532.8306 | -0.415 | 0.6778 |  |
| High cholesterol | -81.2787 | 231.5164 | ±463.0328 | -0.351 | 0.7255 |  |
| Kidney disease | -338.5354 | 532.7158 | ±1065.4316 | -0.635 | 0.5251 |  |
| Circulatory disease | -651.9887 | 356.9664 | ±713.9328 | -1.826 | 0.0678 | . |
| Avg. daily time 54-69 (%) | -28.6122 | 89.9583 | ±179.9166 | -0.318 | 0.7504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1125**, R² = **0.1333**, Adj R² = **0.1247**, F-statistic = **15.56** (p = **1.46e-28**), Residual SE = **3759.607** on **1113** df, AIC = **21726.7**, BIC = **21787.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18098.1311** | 886.7924 | ±1773.5848 | **+20.409** | **1.40e-92** | *** |
| **Education: graduate level (vs college)** | **-538.4005** | 230.6231 | ±461.2463 | **-2.335** | **0.0196** | * |
| **Education: high school or below (vs college)** | **+1587.4869** | 599.3106 | ±1198.6212 | **+2.649** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +94.0648 | 309.1857 | ±618.3713 | +0.304 | 0.7609 |  |
| Site: UW (vs UAB) | -222.3757 | 273.0154 | ±546.0308 | -0.815 | 0.4153 |  |
| **Age (years)** | **-115.8550** | 10.5409 | ±21.0819 | **-10.991** | **4.22e-28** | *** |
| BMI (kg/m2) | -31.6948 | 17.9195 | ±35.8391 | -1.769 | 0.0769 | . |
| Hypertension | -112.0486 | 266.2067 | ±532.4134 | -0.421 | 0.6738 |  |
| High cholesterol | -85.1213 | 231.8256 | ±463.6512 | -0.367 | 0.7135 |  |
| Kidney disease | -336.8385 | 532.6262 | ±1065.2524 | -0.632 | 0.5271 |  |
| Circulatory disease | -651.5501 | 357.0020 | ±714.0041 | -1.825 | 0.0680 | . |
| Time < 70 (%) | -31.8351 | 65.3727 | ±130.7454 | -0.487 | 0.6263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.824** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18075.1126** | 883.0421 | ±1766.0842 | **+20.469** | **4.06e-93** | *** |
| **Education: graduate level (vs college)** | **-537.5982** | 230.6316 | ±461.2633 | **-2.331** | **0.0198** | * |
| **Education: high school or below (vs college)** | **+1590.9912** | 599.2472 | ±1198.4944 | **+2.655** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +101.2090 | 308.8957 | ±617.7914 | +0.328 | 0.7432 |  |
| Site: UW (vs UAB) | -217.8834 | 273.3682 | ±546.7364 | -0.797 | 0.4254 |  |
| **Age (years)** | **-115.7198** | 10.5251 | ±21.0502 | **-10.995** | **4.06e-28** | *** |
| BMI (kg/m2) | -31.7052 | 17.9184 | ±35.8367 | -1.769 | 0.0768 | . |
| Hypertension | -111.1378 | 266.3473 | ±532.6947 | -0.417 | 0.6765 |  |
| High cholesterol | -81.9930 | 231.5935 | ±463.1870 | -0.354 | 0.7233 |  |
| Kidney disease | -337.6875 | 532.6355 | ±1065.2710 | -0.634 | 0.5261 |  |
| Circulatory disease | -652.2155 | 356.9261 | ±713.8521 | -1.827 | 0.0677 | . |
| Avg. daily time < 70 (%) | -24.1019 | 72.5433 | ±145.0865 | -0.332 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1334**, Adj R² = **0.1249**, F-statistic = **15.58** (p = **1.33e-28**), Residual SE = **3759.254** on **1113** df, AIC = **21726.5**, BIC = **21786.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19743.0251** | 2850.0124 | ±5700.0248 | **+6.927** | **4.29e-12** | *** |
| **Education: graduate level (vs college)** | **-532.3636** | 230.1762 | ±460.3523 | **-2.313** | **0.0207** | * |
| **Education: high school or below (vs college)** | **+1591.1064** | 599.7883 | ±1199.5766 | **+2.653** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +113.1586 | 309.0736 | ±618.1472 | +0.366 | 0.7143 |  |
| Site: UW (vs UAB) | -204.9401 | 274.5374 | ±549.0749 | -0.746 | 0.4554 |  |
| **Age (years)** | **-115.4495** | 10.5337 | ±21.0675 | **-10.960** | **5.95e-28** | *** |
| BMI (kg/m2) | -31.8309 | 17.8995 | ±35.7989 | -1.778 | 0.0754 | . |
| Hypertension | -105.3746 | 266.3218 | ±532.6437 | -0.396 | 0.6924 |  |
| High cholesterol | -77.1971 | 230.9067 | ±461.8135 | -0.334 | 0.7381 |  |
| Kidney disease | -344.0772 | 533.1014 | ±1066.2029 | -0.645 | 0.5187 |  |
| Circulatory disease | -661.1243 | 358.5694 | ±717.1387 | -1.844 | 0.0652 | . |
| Time 54-250, pooled (%) | -17.2021 | 27.3454 | ±54.6907 | -0.629 | 0.5293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1335**, Adj R² = **0.1249**, F-statistic = **15.58** (p = **1.29e-28**), Residual SE = **3759.155** on **1113** df, AIC = **21726.4**, BIC = **21786.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19918.8972** | 2855.4540 | ±5710.9080 | **+6.976** | **3.04e-12** | *** |
| **Education: graduate level (vs college)** | **-532.3128** | 230.1650 | ±460.3299 | **-2.313** | **0.0207** | * |
| **Education: high school or below (vs college)** | **+1590.1870** | 599.8053 | ±1199.6105 | **+2.651** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +112.1751 | 309.0326 | ±618.0652 | +0.363 | 0.7166 |  |
| Site: UW (vs UAB) | -205.6667 | 274.5495 | ±549.0990 | -0.749 | 0.4538 |  |
| **Age (years)** | **-115.4683** | 10.5290 | ±21.0581 | **-10.967** | **5.53e-28** | *** |
| BMI (kg/m2) | -31.8911 | 17.8979 | ±35.7957 | -1.782 | 0.0748 | . |
| Hypertension | -105.1168 | 266.2842 | ±532.5684 | -0.395 | 0.6930 |  |
| High cholesterol | -77.7281 | 230.8515 | ±461.7031 | -0.337 | 0.7363 |  |
| Kidney disease | -343.9654 | 533.0610 | ±1066.1220 | -0.645 | 0.5188 |  |
| Circulatory disease | -661.4605 | 358.5108 | ±717.0215 | -1.845 | 0.0650 | . |
| Avg. daily time 54-250 (%) | -18.9191 | 27.2973 | ±54.5945 | -0.693 | 0.4883 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1338**, Adj R² = **0.1253**, F-statistic = **15.63** (p = **1.04e-28**), Residual SE = **3758.408** on **1113** df, AIC = **21726.0**, BIC = **21786.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18048.7218** | 871.5550 | ±1743.1099 | **+20.709** | **2.89e-95** | *** |
| **Education: graduate level (vs college)** | **-524.4371** | 230.4655 | ±460.9311 | **-2.276** | **0.0229** | * |
| **Education: high school or below (vs college)** | **+1605.1174** | 598.8983 | ±1197.7967 | **+2.680** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +108.6383 | 309.3623 | ±618.7247 | +0.351 | 0.7255 |  |
| Site: UW (vs UAB) | -192.3803 | 274.3239 | ±548.6477 | -0.701 | 0.4831 |  |
| **Age (years)** | **-115.4629** | 10.5115 | ±21.0231 | **-10.984** | **4.54e-28** | *** |
| BMI (kg/m2) | -31.2778 | 17.9996 | ±35.9993 | -1.738 | 0.0823 | . |
| Hypertension | -84.9865 | 267.3958 | ±534.7917 | -0.318 | 0.7506 |  |
| High cholesterol | -56.1342 | 230.7860 | ±461.5721 | -0.243 | 0.8078 |  |
| Kidney disease | -302.7118 | 533.4592 | ±1066.9183 | -0.567 | 0.5704 |  |
| Circulatory disease | -645.9874 | 356.9643 | ±713.9286 | -1.810 | 0.0703 | . |
| Time 181-250, pooled (%) | -18.7818 | 17.1953 | ±34.3907 | -1.092 | 0.2747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1339**, Adj R² = **0.1254**, F-statistic = **15.65** (p = **9.77e-29**), Residual SE = **3758.169** on **1113** df, AIC = **21725.8**, BIC = **21786.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18047.2767** | 871.6776 | ±1743.3551 | **+20.704** | **3.18e-95** | *** |
| **Education: graduate level (vs college)** | **-523.3003** | 230.5309 | ±461.0618 | **-2.270** | **0.0232** | * |
| **Education: high school or below (vs college)** | **+1603.7599** | 599.0353 | ±1198.0706 | **+2.677** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +106.6658 | 309.4540 | ±618.9080 | +0.345 | 0.7303 |  |
| Site: UW (vs UAB) | -192.8774 | 274.2815 | ±548.5631 | -0.703 | 0.4819 |  |
| **Age (years)** | **-115.4756** | 10.5095 | ±21.0190 | **-10.988** | **4.38e-28** | *** |
| BMI (kg/m2) | -31.1788 | 18.0095 | ±36.0191 | -1.731 | 0.0834 | . |
| Hypertension | -83.4682 | 267.4305 | ±534.8610 | -0.312 | 0.7550 |  |
| High cholesterol | -54.4536 | 230.9089 | ±461.8178 | -0.236 | 0.8136 |  |
| Kidney disease | -300.1132 | 533.5369 | ±1067.0738 | -0.562 | 0.5738 |  |
| Circulatory disease | -644.7967 | 356.8703 | ±713.7405 | -1.807 | 0.0708 | . |
| Avg. daily time 181-250 (%) | -19.8563 | 16.8791 | ±33.7583 | -1.176 | 0.2394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.60e-28**), Residual SE = **3759.920** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18046.4783** | 870.0757 | ±1740.1513 | **+20.741** | **1.47e-95** | *** |
| **Education: graduate level (vs college)** | **-531.3500** | 230.3214 | ±460.6428 | **-2.307** | **0.0211** | * |
| **Education: high school or below (vs college)** | **+1605.6470** | 599.9767 | ±1199.9534 | **+2.676** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +110.6657 | 309.5165 | ±619.0330 | +0.358 | 0.7207 |  |
| Site: UW (vs UAB) | -203.4672 | 275.0416 | ±550.0832 | -0.740 | 0.4594 |  |
| **Age (years)** | **-115.6439** | 10.5168 | ±21.0336 | **-10.996** | **3.99e-28** | *** |
| BMI (kg/m2) | -31.6595 | 17.9664 | ±35.9328 | -1.762 | 0.0780 | . |
| Hypertension | -102.4905 | 267.3777 | ±534.7553 | -0.383 | 0.7015 |  |
| High cholesterol | -71.6147 | 230.7450 | ±461.4900 | -0.310 | 0.7563 |  |
| Kidney disease | -329.3159 | 532.9084 | ±1065.8167 | -0.618 | 0.5366 |  |
| Circulatory disease | -648.3369 | 357.4065 | ±714.8130 | -1.814 | 0.0697 | . |
| Time > 180 (%) | -3.7661 | 14.0663 | ±28.1327 | -0.268 | 0.7889 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.841** on **1113** df, AIC = **21726.8**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18046.4586** | 870.1750 | ±1740.3501 | **+20.739** | **1.54e-95** | *** |
| **Education: graduate level (vs college)** | **-530.7650** | 230.3485 | ±460.6969 | **-2.304** | **0.0212** | * |
| **Education: high school or below (vs college)** | **+1605.9694** | 600.1378 | ±1200.2756 | **+2.676** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.1678 | 309.5696 | ±619.1392 | +0.356 | 0.7219 |  |
| Site: UW (vs UAB) | -202.9097 | 275.0044 | ±550.0088 | -0.738 | 0.4606 |  |
| **Age (years)** | **-115.6471** | 10.5158 | ±21.0316 | **-10.997** | **3.93e-28** | *** |
| BMI (kg/m2) | -31.6027 | 17.9800 | ±35.9599 | -1.758 | 0.0788 | . |
| Hypertension | -101.3853 | 267.4143 | ±534.8285 | -0.379 | 0.7046 |  |
| High cholesterol | -70.3495 | 230.8702 | ±461.7405 | -0.305 | 0.7606 |  |
| Kidney disease | -327.2175 | 532.9578 | ±1065.9156 | -0.614 | 0.5392 |  |
| Circulatory disease | -647.4163 | 357.4190 | ±714.8380 | -1.811 | 0.0701 | . |
| Avg. daily time > 180 (%) | -4.7151 | 14.0562 | ±28.1124 | -0.335 | 0.7373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.61e-28**), Residual SE = **3759.948** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18040.4306** | 871.2717 | ±1742.5434 | **+20.706** | **3.07e-95** | *** |
| **Education: graduate level (vs college)** | **-533.4263** | 230.2573 | ±460.5146 | **-2.317** | **0.0205** | * |
| **Education: high school or below (vs college)** | **+1604.4117** | 600.3573 | ±1200.7147 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.6851 | 309.5281 | ±619.0563 | +0.358 | 0.7206 |  |
| Site: UW (vs UAB) | -204.5911 | 274.9345 | ±549.8690 | -0.744 | 0.4568 |  |
| **Age (years)** | **-115.7219** | 10.5164 | ±21.0328 | **-11.004** | **3.66e-28** | *** |
| BMI (kg/m2) | -31.4089 | 18.1446 | ±36.2892 | -1.731 | 0.0834 | . |
| Hypertension | -105.1008 | 266.9591 | ±533.9182 | -0.394 | 0.6938 |  |
| High cholesterol | -71.0423 | 231.3975 | ±462.7950 | -0.307 | 0.7588 |  |
| Kidney disease | -336.6388 | 532.6442 | ±1065.2884 | -0.632 | 0.5274 |  |
| Circulatory disease | -650.8688 | 357.2705 | ±714.5409 | -1.822 | 0.0685 | . |
| Nocturnal time > 180 (%) | -3.5454 | 14.9577 | ±29.9154 | -0.237 | 0.8126 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1333**, Adj R² = **0.1247**, F-statistic = **15.56** (p = **1.47e-28**), Residual SE = **3759.616** on **1113** df, AIC = **21726.7**, BIC = **21787.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18000.8648** | 876.6736 | ±1753.3473 | **+20.533** | **1.09e-93** | *** |
| **Education: graduate level (vs college)** | **-533.2133** | 230.2952 | ±460.5904 | **-2.315** | **0.0206** | * |
| **Education: high school or below (vs college)** | **+1600.5037** | 598.3156 | ±1196.6312 | **+2.675** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.3232 | 309.0496 | ±618.0991 | +0.357 | 0.7211 |  |
| Site: UW (vs UAB) | -209.8143 | 274.8981 | ±549.7962 | -0.763 | 0.4453 |  |
| **Age (years)** | **-115.6524** | 10.5240 | ±21.0480 | **-10.989** | **4.30e-28** | *** |
| BMI (kg/m2) | -31.0196 | 17.8417 | ±35.6834 | -1.739 | 0.0821 | . |
| Hypertension | -115.8408 | 267.3927 | ±534.7855 | -0.433 | 0.6649 |  |
| High cholesterol | -81.8241 | 229.7035 | ±459.4071 | -0.356 | 0.7217 |  |
| Kidney disease | -342.8691 | 532.3086 | ±1064.6172 | -0.644 | 0.5195 |  |
| Circulatory disease | -650.1322 | 357.3663 | ±714.7326 | -1.819 | 0.0689 | . |
| Any reading > 250 during wear (0/1) | +146.0163 | 285.8194 | ±571.6389 | +0.511 | 0.6094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1335**, Adj R² = **0.1249**, F-statistic = **15.59** (p = **1.26e-28**), Residual SE = **3759.067** on **1113** df, AIC = **21726.4**, BIC = **21786.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18029.0032** | 870.0381 | ±1740.0762 | **+20.722** | **2.19e-95** | *** |
| **Education: graduate level (vs college)** | **-532.7140** | 230.1420 | ±460.2840 | **-2.315** | **0.0206** | * |
| **Education: high school or below (vs college)** | **+1587.9570** | 599.7959 | ±1199.5917 | **+2.647** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +109.6733 | 309.1106 | ±618.2212 | +0.355 | 0.7227 |  |
| Site: UW (vs UAB) | -207.5998 | 274.6402 | ±549.2803 | -0.756 | 0.4497 |  |
| **Age (years)** | **-115.4490** | 10.5309 | ±21.0619 | **-10.963** | **5.77e-28** | *** |
| BMI (kg/m2) | -31.8635 | 17.8970 | ±35.7940 | -1.780 | 0.0750 | . |
| Hypertension | -106.0626 | 266.2953 | ±532.5907 | -0.398 | 0.6904 |  |
| High cholesterol | -79.0237 | 230.7626 | ±461.5252 | -0.342 | 0.7320 |  |
| Kidney disease | -344.0280 | 533.1075 | ±1066.2151 | -0.645 | 0.5187 |  |
| Circulatory disease | -662.2541 | 358.5623 | ±717.1247 | -1.847 | 0.0648 | . |
| Time > 250 (%) | +19.2358 | 26.7857 | ±53.5715 | +0.718 | 0.4727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1335**, Adj R² = **0.1249**, F-statistic = **15.59** (p = **1.26e-28**), Residual SE = **3759.082** on **1113** df, AIC = **21726.4**, BIC = **21786.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18031.0331** | 869.9435 | ±1739.8870 | **+20.727** | **1.99e-95** | *** |
| **Education: graduate level (vs college)** | **-532.7601** | 230.1395 | ±460.2790 | **-2.315** | **0.0206** | * |
| **Education: high school or below (vs college)** | **+1588.2616** | 599.8734 | ±1199.7467 | **+2.648** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +109.6661 | 309.0954 | ±618.1908 | +0.355 | 0.7227 |  |
| Site: UW (vs UAB) | -208.0480 | 274.6631 | ±549.3263 | -0.757 | 0.4488 |  |
| **Age (years)** | **-115.4552** | 10.5294 | ±21.0588 | **-10.965** | **5.63e-28** | *** |
| BMI (kg/m2) | -31.9106 | 17.8995 | ±35.7989 | -1.783 | 0.0746 | . |
| Hypertension | -105.9360 | 266.2971 | ±532.5941 | -0.398 | 0.6908 |  |
| High cholesterol | -79.0403 | 230.7705 | ±461.5409 | -0.343 | 0.7320 |  |
| Kidney disease | -343.6810 | 533.0538 | ±1066.1076 | -0.645 | 0.5191 |  |
| Circulatory disease | -662.1470 | 358.4961 | ±716.9921 | -1.847 | 0.0647 | . |
| Avg. daily time > 250 (%) | +19.7656 | 27.1968 | ±54.3937 | +0.727 | 0.4674 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 1,125; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1394**, F-statistic = **19.21** (p = **6.57e-33**), Residual SE = **11.849** on **1114** df, AIC = **8766.2**, BIC = **8821.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8701** | 2.8500 | ±5.7001 | **+16.796** | **2.60e-63** | *** |
| Education: graduate level (vs college) | -1.4338 | 0.7423 | ±1.4846 | -1.932 | 0.0534 | . |
| **Education: high school or below (vs college)** | **+3.8401** | 1.7412 | ±3.4824 | **+2.205** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.6799 | 0.9956 | ±1.9913 | +0.683 | 0.4947 |  |
| Site: UW (vs UAB) | -0.0767 | 0.8585 | ±1.7170 | -0.089 | 0.9288 |  |
| **Age (years)** | **-0.3980** | 0.0328 | ±0.0656 | **-12.125** | **7.83e-34** | *** |
| BMI (kg/m2) | +0.0264 | 0.0569 | ±0.1139 | +0.464 | 0.6426 |  |
| Hypertension | -0.3428 | 0.8154 | ±1.6308 | -0.420 | 0.6742 |  |
| High cholesterol | -0.1133 | 0.7294 | ±1.4588 | -0.155 | 0.8766 |  |
| Kidney disease | -0.3528 | 1.6981 | ±3.3961 | -0.208 | 0.8354 |  |
| Circulatory disease | -1.9672 | 1.0698 | ±2.1396 | -1.839 | 0.0659 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1125**, R² = **0.1512**, Adj R² = **0.1428**, F-statistic = **18.02** (p = **2.26e-33**), Residual SE = **11.826** on **1113** df, AIC = **8762.7**, BIC = **8823.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.8581** | 4.4285 | ±8.8570 | **+9.000** | **2.25e-19** | *** |
| Education: graduate level (vs college) | -1.4331 | 0.7404 | ±1.4807 | -1.936 | 0.0529 | . |
| **Education: high school or below (vs college)** | **+3.6640** | 1.7510 | ±3.5021 | **+2.092** | **0.0364** | * |
| Site: UCSD (vs UAB) | +0.6057 | 0.9955 | ±1.9911 | +0.608 | 0.5429 |  |
| Site: UW (vs UAB) | -0.1484 | 0.8576 | ±1.7153 | -0.173 | 0.8626 |  |
| **Age (years)** | **-0.4044** | 0.0327 | ±0.0655 | **-12.355** | **4.60e-35** | *** |
| BMI (kg/m2) | +0.0153 | 0.0573 | ±0.1145 | +0.267 | 0.7892 |  |
| Hypertension | -0.4187 | 0.8135 | ±1.6269 | -0.515 | 0.6068 |  |
| High cholesterol | -0.3413 | 0.7400 | ±1.4801 | -0.461 | 0.6447 |  |
| Kidney disease | -0.3472 | 1.6840 | ±3.3681 | -0.206 | 0.8366 |  |
| Circulatory disease | -2.0573 | 1.0672 | ±2.1343 | -1.928 | 0.0539 | . |
| **HbA1c (%)** | **+1.5772** | 0.6799 | ±1.3598 | **+2.320** | **0.0204** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1125**, R² = **0.1475**, Adj R² = **0.1391**, F-statistic = **17.51** (p = **2.29e-32**), Residual SE = **11.852** on **1113** df, AIC = **8767.6**, BIC = **8827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.3350** | 3.4451 | ±6.8901 | **+13.450** | **3.09e-41** | *** |
| **Education: graduate level (vs college)** | **-1.4596** | 0.7444 | ±1.4889 | **-1.961** | **0.0499** | * |
| **Education: high school or below (vs college)** | **+3.7937** | 1.7416 | ±3.4833 | **+2.178** | **0.0294** | * |
| Site: UCSD (vs UAB) | +0.6683 | 0.9959 | ±1.9918 | +0.671 | 0.5022 |  |
| Site: UW (vs UAB) | -0.1275 | 0.8632 | ±1.7264 | -0.148 | 0.8825 |  |
| **Age (years)** | **-0.3987** | 0.0329 | ±0.0658 | **-12.116** | **8.70e-34** | *** |
| BMI (kg/m2) | +0.0244 | 0.0572 | ±0.1144 | +0.427 | 0.6693 |  |
| Hypertension | -0.3892 | 0.8172 | ±1.6343 | -0.476 | 0.6338 |  |
| High cholesterol | -0.1581 | 0.7295 | ±1.4589 | -0.217 | 0.8284 |  |
| Kidney disease | -0.4124 | 1.6891 | ±3.3782 | -0.244 | 0.8071 |  |
| Circulatory disease | -1.9899 | 1.0722 | ±2.1445 | -1.856 | 0.0635 | . |
| Mean glucose (mg/dL) | +0.0142 | 0.0197 | ±0.0394 | +0.723 | 0.4698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1125**, R² = **0.1475**, Adj R² = **0.1391**, F-statistic = **17.51** (p = **2.29e-32**), Residual SE = **11.852** on **1113** df, AIC = **8767.6**, BIC = **8827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.3661** | 5.4669 | ±10.9338 | **+8.115** | **4.84e-16** | *** |
| **Education: graduate level (vs college)** | **-1.4596** | 0.7444 | ±1.4889 | **-1.961** | **0.0499** | * |
| **Education: high school or below (vs college)** | **+3.7937** | 1.7416 | ±3.4833 | **+2.178** | **0.0294** | * |
| Site: UCSD (vs UAB) | +0.6683 | 0.9959 | ±1.9918 | +0.671 | 0.5022 |  |
| Site: UW (vs UAB) | -0.1275 | 0.8632 | ±1.7264 | -0.148 | 0.8825 |  |
| **Age (years)** | **-0.3987** | 0.0329 | ±0.0658 | **-12.116** | **8.70e-34** | *** |
| BMI (kg/m2) | +0.0244 | 0.0572 | ±0.1144 | +0.427 | 0.6693 |  |
| Hypertension | -0.3892 | 0.8172 | ±1.6343 | -0.476 | 0.6338 |  |
| High cholesterol | -0.1581 | 0.7295 | ±1.4589 | -0.217 | 0.8284 |  |
| Kidney disease | -0.4124 | 1.6891 | ±3.3782 | -0.244 | 0.8071 |  |
| Circulatory disease | -1.9899 | 1.0722 | ±2.1445 | -1.856 | 0.0635 | . |
| GMI (%) | +0.5949 | 0.8231 | ±1.6461 | +0.723 | 0.4698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1125**, R² = **0.1474**, Adj R² = **0.1390**, F-statistic = **17.50** (p = **2.36e-32**), Residual SE = **11.852** on **1113** df, AIC = **8767.7**, BIC = **8828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5203** | 3.3931 | ±6.7861 | **+13.710** | **8.80e-43** | *** |
| Education: graduate level (vs college) | -1.4468 | 0.7430 | ±1.4861 | -1.947 | 0.0515 | . |
| **Education: high school or below (vs college)** | **+3.7960** | 1.7418 | ±3.4835 | **+2.179** | **0.0293** | * |
| Site: UCSD (vs UAB) | +0.6531 | 0.9968 | ±1.9935 | +0.655 | 0.5123 |  |
| Site: UW (vs UAB) | -0.1214 | 0.8620 | ±1.7241 | -0.141 | 0.8880 |  |
| **Age (years)** | **-0.3974** | 0.0328 | ±0.0657 | **-12.099** | **1.06e-33** | *** |
| BMI (kg/m2) | +0.0214 | 0.0578 | ±0.1157 | +0.371 | 0.7108 |  |
| Hypertension | -0.3767 | 0.8165 | ±1.6331 | -0.461 | 0.6446 |  |
| High cholesterol | -0.1639 | 0.7304 | ±1.4608 | -0.224 | 0.8224 |  |
| Kidney disease | -0.3701 | 1.6933 | ±3.3867 | -0.219 | 0.8270 |  |
| Circulatory disease | -1.9765 | 1.0709 | ±2.1419 | -1.846 | 0.0650 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0128 | 0.0190 | ±0.0381 | +0.672 | 0.5014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1479**, Adj R² = **0.1395**, F-statistic = **17.56** (p = **1.77e-32**), Residual SE = **11.849** on **1113** df, AIC = **8767.1**, BIC = **8827.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.7362** | 3.0109 | ±6.0219 | **+15.522** | **2.46e-54** | *** |
| Education: graduate level (vs college) | -1.4416 | 0.7433 | ±1.4865 | -1.939 | 0.0524 | . |
| **Education: high school or below (vs college)** | **+3.8329** | 1.7375 | ±3.4749 | **+2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.7161 | 0.9997 | ±1.9994 | +0.716 | 0.4738 |  |
| Site: UW (vs UAB) | -0.1125 | 0.8600 | ±1.7201 | -0.131 | 0.8960 |  |
| **Age (years)** | **-0.3996** | 0.0329 | ±0.0658 | **-12.151** | **5.65e-34** | *** |
| BMI (kg/m2) | +0.0275 | 0.0569 | ±0.1138 | +0.484 | 0.6285 |  |
| Hypertension | -0.4143 | 0.8170 | ±1.6339 | -0.507 | 0.6121 |  |
| High cholesterol | -0.1348 | 0.7294 | ±1.4588 | -0.185 | 0.8534 |  |
| Kidney disease | -0.4914 | 1.7000 | ±3.4000 | -0.289 | 0.7725 |  |
| Circulatory disease | -1.9981 | 1.0707 | ±2.1414 | -1.866 | 0.0620 | . |
| Glucose SD, pooled (mg/dL) | +0.0581 | 0.0580 | ±0.1160 | +1.002 | 0.3166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1476**, Adj R² = **0.1392**, F-statistic = **17.52** (p = **2.09e-32**), Residual SE = **11.851** on **1113** df, AIC = **8767.4**, BIC = **8827.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.0262** | 2.9790 | ±5.9580 | **+15.786** | **3.89e-56** | *** |
| Education: graduate level (vs college) | -1.4444 | 0.7438 | ±1.4875 | -1.942 | 0.0521 | . |
| **Education: high school or below (vs college)** | **+3.8294** | 1.7393 | ±3.4787 | **+2.202** | **0.0277** | * |
| Site: UCSD (vs UAB) | +0.7029 | 0.9985 | ±1.9971 | +0.704 | 0.4815 |  |
| Site: UW (vs UAB) | -0.1119 | 0.8608 | ±1.7216 | -0.130 | 0.8965 |  |
| **Age (years)** | **-0.3997** | 0.0329 | ±0.0658 | **-12.142** | **6.36e-34** | *** |
| BMI (kg/m2) | +0.0266 | 0.0569 | ±0.1138 | +0.467 | 0.6402 |  |
| Hypertension | -0.4014 | 0.8168 | ±1.6336 | -0.491 | 0.6231 |  |
| High cholesterol | -0.1316 | 0.7298 | ±1.4596 | -0.180 | 0.8569 |  |
| Kidney disease | -0.4641 | 1.6972 | ±3.3945 | -0.273 | 0.7845 |  |
| Circulatory disease | -1.9924 | 1.0716 | ±2.1432 | -1.859 | 0.0630 | . |
| Avg. daily SD (mg/dL) | +0.0506 | 0.0617 | ±0.1235 | +0.820 | 0.4123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1125**, R² = **0.1476**, Adj R² = **0.1391**, F-statistic = **17.51** (p = **2.20e-32**), Residual SE = **11.851** on **1113** df, AIC = **8767.5**, BIC = **8827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6013** | 3.3082 | ±6.6164 | **+14.087** | **4.60e-45** | *** |
| Education: graduate level (vs college) | -1.4208 | 0.7419 | ±1.4837 | -1.915 | 0.0555 | . |
| **Education: high school or below (vs college)** | **+3.8652** | 1.7401 | ±3.4801 | **+2.221** | **0.0263** | * |
| Site: UCSD (vs UAB) | +0.7298 | 1.0047 | ±2.0093 | +0.726 | 0.4676 |  |
| Site: UW (vs UAB) | -0.0700 | 0.8605 | ±1.7209 | -0.081 | 0.9352 |  |
| **Age (years)** | **-0.3992** | 0.0328 | ±0.0657 | **-12.158** | **5.21e-34** | *** |
| BMI (kg/m2) | +0.0289 | 0.0570 | ±0.1140 | +0.507 | 0.6118 |  |
| Hypertension | -0.3770 | 0.8167 | ±1.6335 | -0.462 | 0.6444 |  |
| High cholesterol | -0.0967 | 0.7300 | ±1.4601 | -0.132 | 0.8946 |  |
| Kidney disease | -0.4360 | 1.7088 | ±3.4176 | -0.255 | 0.7986 |  |
| Circulatory disease | -1.9763 | 1.0696 | ±2.1393 | -1.848 | 0.0647 | . |
| CV (%) | +0.0705 | 0.0957 | ±0.1914 | +0.737 | 0.4612 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1125**, R² = **0.1485**, Adj R² = **0.1401**, F-statistic = **17.65** (p = **1.19e-32**), Residual SE = **11.845** on **1113** df, AIC = **8766.3**, BIC = **8826.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2736** | 3.3979 | ±6.7957 | **+14.796** | **1.56e-49** | *** |
| Education: graduate level (vs college) | -1.4070 | 0.7410 | ±1.4820 | -1.899 | 0.0576 | . |
| **Education: high school or below (vs college)** | **+3.8549** | 1.7358 | ±3.4716 | **+2.221** | **0.0264** | * |
| Site: UCSD (vs UAB) | +0.7649 | 1.0012 | ±2.0025 | +0.764 | 0.4449 |  |
| Site: UW (vs UAB) | -0.0869 | 0.8594 | ±1.7188 | -0.101 | 0.9194 |  |
| **Age (years)** | **-0.4002** | 0.0328 | ±0.0656 | **-12.193** | **3.39e-34** | *** |
| BMI (kg/m2) | +0.0301 | 0.0570 | ±0.1139 | +0.528 | 0.5975 |  |
| Hypertension | -0.4111 | 0.8160 | ±1.6320 | -0.504 | 0.6144 |  |
| High cholesterol | -0.0959 | 0.7296 | ±1.4593 | -0.131 | 0.8954 |  |
| Kidney disease | -0.4554 | 1.7043 | ±3.4086 | -0.267 | 0.7893 |  |
| Circulatory disease | -1.9789 | 1.0675 | ±2.1349 | -1.854 | 0.0638 | . |
| Mean / SD ratio | -0.4051 | 0.3009 | ±0.6018 | -1.346 | 0.1782 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1486**, Adj R² = **0.1402**, F-statistic = **17.66** (p = **1.14e-32**), Residual SE = **11.844** on **1113** df, AIC = **8766.1**, BIC = **8826.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3789** | 3.4077 | ±6.8154 | **+14.784** | **1.86e-49** | *** |
| Education: graduate level (vs college) | -1.4250 | 0.7418 | ±1.4836 | -1.921 | 0.0547 | . |
| **Education: high school or below (vs college)** | **+3.8258** | 1.7365 | ±3.4730 | **+2.203** | **0.0276** | * |
| Site: UCSD (vs UAB) | +0.7497 | 0.9985 | ±1.9970 | +0.751 | 0.4527 |  |
| Site: UW (vs UAB) | -0.0992 | 0.8592 | ±1.7184 | -0.115 | 0.9081 |  |
| **Age (years)** | **-0.4014** | 0.0329 | ±0.0658 | **-12.209** | **2.78e-34** | *** |
| BMI (kg/m2) | +0.0280 | 0.0568 | ±0.1136 | +0.492 | 0.6225 |  |
| Hypertension | -0.3945 | 0.8153 | ±1.6306 | -0.484 | 0.6285 |  |
| High cholesterol | -0.0983 | 0.7295 | ±1.4590 | -0.135 | 0.8929 |  |
| Kidney disease | -0.4790 | 1.7012 | ±3.4024 | -0.282 | 0.7783 |  |
| Circulatory disease | -1.9734 | 1.0683 | ±2.1366 | -1.847 | 0.0647 | . |
| Avg. daily mean/SD | -0.3469 | 0.2499 | ±0.4997 | -1.388 | 0.1650 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1125**, R² = **0.1613**, Adj R² = **0.1530**, F-statistic = **19.46** (p = **3.89e-36**), Residual SE = **11.756** on **1113** df, AIC = **8749.3**, BIC = **8809.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.6564** | 3.4381 | ±6.8763 | **+11.534** | **8.87e-31** | *** |
| Education: graduate level (vs college) | -1.3721 | 0.7377 | ±1.4754 | -1.860 | 0.0629 | . |
| **Education: high school or below (vs college)** | **+3.7213** | 1.7112 | ±3.4225 | **+2.175** | **0.0297** | * |
| Site: UCSD (vs UAB) | +0.8852 | 0.9890 | ±1.9780 | +0.895 | 0.3708 |  |
| Site: UW (vs UAB) | +0.1494 | 0.8586 | ±1.7172 | +0.174 | 0.8618 |  |
| **Age (years)** | **-0.3919** | 0.0325 | ±0.0650 | **-12.059** | **1.74e-33** | *** |
| BMI (kg/m2) | +0.0299 | 0.0559 | ±0.1118 | +0.536 | 0.5921 |  |
| Hypertension | -0.3043 | 0.8105 | ±1.6209 | -0.376 | 0.7073 |  |
| High cholesterol | +0.0007 | 0.7207 | ±1.4414 | +0.001 | 0.9992 |  |
| Kidney disease | -0.6033 | 1.6796 | ±3.3592 | -0.359 | 0.7195 |  |
| Circulatory disease | -1.8509 | 1.0552 | ±2.1105 | -1.754 | 0.0794 | . |
| **MAG (mg/dL/h)** | **+0.1973** | 0.0490 | ±0.0981 | **+4.024** | **5.72e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1125**, R² = **0.1486**, Adj R² = **0.1402**, F-statistic = **17.66** (p = **1.15e-32**), Residual SE = **11.844** on **1113** df, AIC = **8766.2**, BIC = **8826.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.9687** | 3.1504 | ±6.3008 | **+14.591** | **3.19e-48** | *** |
| Education: graduate level (vs college) | -1.4531 | 0.7430 | ±1.4861 | -1.956 | 0.0505 | . |
| **Education: high school or below (vs college)** | **+3.8035** | 1.7360 | ±3.4720 | **+2.191** | **0.0285** | * |
| Site: UCSD (vs UAB) | +0.7186 | 0.9974 | ±1.9948 | +0.720 | 0.4712 |  |
| Site: UW (vs UAB) | -0.1141 | 0.8609 | ±1.7219 | -0.133 | 0.8946 |  |
| **Age (years)** | **-0.4001** | 0.0328 | ±0.0656 | **-12.192** | **3.41e-34** | *** |
| BMI (kg/m2) | +0.0317 | 0.0570 | ±0.1139 | +0.556 | 0.5782 |  |
| Hypertension | -0.4093 | 0.8167 | ±1.6334 | -0.501 | 0.6162 |  |
| High cholesterol | -0.1180 | 0.7292 | ±1.4583 | -0.162 | 0.8714 |  |
| Kidney disease | -0.4950 | 1.6944 | ±3.3888 | -0.292 | 0.7702 |  |
| Circulatory disease | -1.9994 | 1.0699 | ±2.1398 | -1.869 | 0.0617 | . |
| Avg. daily range (mg/dL) | +0.0196 | 0.0146 | ±0.0292 | +1.344 | 0.1789 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1125**, R² = **0.1494**, Adj R² = **0.1410**, F-statistic = **17.78** (p = **6.82e-33**), Residual SE = **11.838** on **1113** df, AIC = **8765.1**, BIC = **8825.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6215** | 2.9011 | ±5.8023 | **+16.070** | **4.14e-58** | *** |
| Education: graduate level (vs college) | -1.4433 | 0.7423 | ±1.4846 | -1.944 | 0.0518 | . |
| **Education: high school or below (vs college)** | **+3.8826** | 1.7315 | ±3.4631 | **+2.242** | **0.0249** | * |
| Site: UCSD (vs UAB) | +0.7759 | 0.9973 | ±1.9946 | +0.778 | 0.4366 |  |
| Site: UW (vs UAB) | -0.0924 | 0.8578 | ±1.7155 | -0.108 | 0.9142 |  |
| **Age (years)** | **-0.3967** | 0.0328 | ±0.0656 | **-12.101** | **1.04e-33** | *** |
| BMI (kg/m2) | +0.0222 | 0.0573 | ±0.1147 | +0.387 | 0.6989 |  |
| Hypertension | -0.3723 | 0.8153 | ±1.6307 | -0.457 | 0.6480 |  |
| High cholesterol | -0.1730 | 0.7293 | ±1.4587 | -0.237 | 0.8125 |  |
| Kidney disease | -0.4184 | 1.7028 | ±3.4057 | -0.246 | 0.8059 |  |
| Circulatory disease | -2.0046 | 1.0666 | ±2.1331 | -1.880 | 0.0602 | . |
| SD of daily means (mg/dL) | +0.1999 | 0.1188 | ±0.2377 | +1.682 | 0.0925 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1125**, R² = **0.1473**, Adj R² = **0.1389**, F-statistic = **17.48** (p = **2.56e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.9**, BIC = **8828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1251** | 5.3799 | ±10.7597 | **+9.317** | **1.19e-20** | *** |
| Education: graduate level (vs college) | -1.4401 | 0.7430 | ±1.4860 | -1.938 | 0.0526 | . |
| **Education: high school or below (vs college)** | **+3.8301** | 1.7429 | ±3.4858 | **+2.198** | **0.0280** | * |
| Site: UCSD (vs UAB) | +0.6934 | 0.9974 | ±1.9948 | +0.695 | 0.4869 |  |
| Site: UW (vs UAB) | -0.0839 | 0.8601 | ±1.7203 | -0.098 | 0.9223 |  |
| **Age (years)** | **-0.3978** | 0.0329 | ±0.0657 | **-12.105** | **9.99e-34** | *** |
| BMI (kg/m2) | +0.0256 | 0.0571 | ±0.1142 | +0.449 | 0.6535 |  |
| Hypertension | -0.3650 | 0.8165 | ±1.6330 | -0.447 | 0.6549 |  |
| High cholesterol | -0.1350 | 0.7296 | ±1.4593 | -0.185 | 0.8533 |  |
| Kidney disease | -0.4042 | 1.6938 | ±3.3877 | -0.239 | 0.8114 |  |
| Circulatory disease | -1.9870 | 1.0736 | ±2.1472 | -1.851 | 0.0642 | . |
| Time in range 70-180, pooled (%) | -0.0232 | 0.0452 | ±0.0904 | -0.513 | 0.6079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1125**, R² = **0.1473**, Adj R² = **0.1388**, F-statistic = **17.47** (p = **2.64e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.9**, BIC = **8828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8944** | 5.4060 | ±10.8121 | **+9.229** | **2.72e-20** | *** |
| Education: graduate level (vs college) | -1.4397 | 0.7431 | ±1.4862 | -1.937 | 0.0527 | . |
| **Education: high school or below (vs college)** | **+3.8335** | 1.7432 | ±3.4864 | **+2.199** | **0.0279** | * |
| Site: UCSD (vs UAB) | +0.6913 | 0.9974 | ±1.9948 | +0.693 | 0.4882 |  |
| Site: UW (vs UAB) | -0.0828 | 0.8600 | ±1.7201 | -0.096 | 0.9233 |  |
| **Age (years)** | **-0.3979** | 0.0329 | ±0.0657 | **-12.106** | **9.85e-34** | *** |
| BMI (kg/m2) | +0.0256 | 0.0571 | ±0.1143 | +0.448 | 0.6542 |  |
| Hypertension | -0.3624 | 0.8168 | ±1.6335 | -0.444 | 0.6572 |  |
| High cholesterol | -0.1339 | 0.7300 | ±1.4600 | -0.183 | 0.8544 |  |
| Kidney disease | -0.3982 | 1.6940 | ±3.3880 | -0.235 | 0.8142 |  |
| Circulatory disease | -1.9848 | 1.0736 | ±2.1472 | -1.849 | 0.0645 | . |
| Avg. daily time in range 70-180 (%) | -0.0207 | 0.0452 | ±0.0903 | -0.458 | 0.6467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.45** (p = **2.89e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7644** | 2.9169 | ±5.8339 | **+16.375** | **2.89e-60** | *** |
| Education: graduate level (vs college) | -1.4283 | 0.7427 | ±1.4855 | -1.923 | 0.0545 | . |
| **Education: high school or below (vs college)** | **+3.8599** | 1.7400 | ±3.4799 | **+2.218** | **0.0265** | * |
| Site: UCSD (vs UAB) | +0.7086 | 1.0014 | ±2.0028 | +0.708 | 0.4792 |  |
| Site: UW (vs UAB) | -0.0643 | 0.8621 | ±1.7242 | -0.075 | 0.9405 |  |
| **Age (years)** | **-0.3974** | 0.0332 | ±0.0664 | **-11.978** | **4.64e-33** | *** |
| BMI (kg/m2) | +0.0261 | 0.0570 | ±0.1139 | +0.458 | 0.6468 |  |
| Hypertension | -0.3450 | 0.8171 | ±1.6342 | -0.422 | 0.6729 |  |
| High cholesterol | -0.1017 | 0.7298 | ±1.4596 | -0.139 | 0.8892 |  |
| Kidney disease | -0.3479 | 1.7002 | ±3.4005 | -0.205 | 0.8379 |  |
| Circulatory disease | -1.9888 | 1.0724 | ±2.1448 | -1.855 | 0.0637 | . |
| Any reading < 54 during wear (0/1) | +0.1846 | 0.7708 | ±1.5416 | +0.239 | 0.8108 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.45** (p = **2.91e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9271** | 2.8769 | ±5.7538 | **+16.659** | **2.60e-62** | *** |
| Education: graduate level (vs college) | -1.4366 | 0.7434 | ±1.4868 | -1.933 | 0.0533 | . |
| **Education: high school or below (vs college)** | **+3.8279** | 1.7430 | ±3.4860 | **+2.196** | **0.0281** | * |
| Site: UCSD (vs UAB) | +0.6548 | 1.0049 | ±2.0097 | +0.652 | 0.5146 |  |
| Site: UW (vs UAB) | -0.0957 | 0.8613 | ±1.7226 | -0.111 | 0.9115 |  |
| **Age (years)** | **-0.3981** | 0.0329 | ±0.0658 | **-12.108** | **9.61e-34** | *** |
| BMI (kg/m2) | +0.0262 | 0.0570 | ±0.1141 | +0.460 | 0.6455 |  |
| Hypertension | -0.3485 | 0.8154 | ±1.6308 | -0.427 | 0.6691 |  |
| High cholesterol | -0.1247 | 0.7312 | ±1.4624 | -0.171 | 0.8646 |  |
| Kidney disease | -0.3474 | 1.6990 | ±3.3980 | -0.204 | 0.8380 |  |
| Circulatory disease | -1.9672 | 1.0702 | ±2.1405 | -1.838 | 0.0660 | . |
| Time < 54 (%) | -0.1286 | 0.6136 | ±1.2272 | -0.210 | 0.8340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.45** (p = **2.91e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9097** | 2.8701 | ±5.7401 | **+16.693** | **1.48e-62** | *** |
| Education: graduate level (vs college) | -1.4378 | 0.7437 | ±1.4875 | -1.933 | 0.0532 | . |
| **Education: high school or below (vs college)** | **+3.8285** | 1.7423 | ±3.4845 | **+2.197** | **0.0280** | * |
| Site: UCSD (vs UAB) | +0.6585 | 1.0042 | ±2.0083 | +0.656 | 0.5120 |  |
| Site: UW (vs UAB) | -0.0969 | 0.8615 | ±1.7230 | -0.112 | 0.9104 |  |
| **Age (years)** | **-0.3979** | 0.0328 | ±0.0657 | **-12.117** | **8.58e-34** | *** |
| BMI (kg/m2) | +0.0263 | 0.0571 | ±0.1141 | +0.461 | 0.6449 |  |
| Hypertension | -0.3503 | 0.8153 | ±1.6305 | -0.430 | 0.6675 |  |
| High cholesterol | -0.1237 | 0.7303 | ±1.4606 | -0.169 | 0.8655 |  |
| Kidney disease | -0.3481 | 1.6988 | ±3.3976 | -0.205 | 0.8377 |  |
| Circulatory disease | -1.9692 | 1.0697 | ±2.1394 | -1.841 | 0.0656 | . |
| Avg. daily time < 54 (%) | -0.1650 | 0.8196 | ±1.6392 | -0.201 | 0.8405 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.85e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9643** | 2.9022 | ±5.8044 | **+16.527** | **2.35e-61** | *** |
| Education: graduate level (vs college) | -1.4444 | 0.7438 | ±1.4876 | -1.942 | 0.0521 | . |
| **Education: high school or below (vs college)** | **+3.8133** | 1.7427 | ±3.4853 | **+2.188** | **0.0287** | * |
| Site: UCSD (vs UAB) | +0.6558 | 0.9975 | ±1.9949 | +0.657 | 0.5109 |  |
| Site: UW (vs UAB) | -0.1021 | 0.8576 | ±1.7152 | -0.119 | 0.9052 |  |
| **Age (years)** | **-0.3984** | 0.0330 | ±0.0659 | **-12.090** | **1.20e-33** | *** |
| BMI (kg/m2) | +0.0267 | 0.0570 | ±0.1140 | +0.469 | 0.6393 |  |
| Hypertension | -0.3518 | 0.8155 | ±1.6310 | -0.431 | 0.6662 |  |
| High cholesterol | -0.1272 | 0.7324 | ±1.4647 | -0.174 | 0.8622 |  |
| Kidney disease | -0.3542 | 1.6985 | ±3.3971 | -0.209 | 0.8348 |  |
| Circulatory disease | -1.9672 | 1.0699 | ±2.1399 | -1.839 | 0.0660 | . |
| Time 54-69, pooled (%) | -0.0724 | 0.2708 | ±0.5416 | -0.267 | 0.7892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1125**, R² = **0.1472**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.81e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9629** | 2.8930 | ±5.7859 | **+16.579** | **9.86e-62** | *** |
| Education: graduate level (vs college) | -1.4477 | 0.7438 | ±1.4876 | -1.946 | 0.0516 | . |
| **Education: high school or below (vs college)** | **+3.8068** | 1.7435 | ±3.4869 | **+2.183** | **0.0290** | * |
| Site: UCSD (vs UAB) | +0.6572 | 0.9967 | ±1.9933 | +0.659 | 0.5097 |  |
| Site: UW (vs UAB) | -0.1060 | 0.8578 | ±1.7156 | -0.124 | 0.9017 |  |
| **Age (years)** | **-0.3983** | 0.0329 | ±0.0658 | **-12.104** | **1.00e-33** | *** |
| BMI (kg/m2) | +0.0267 | 0.0570 | ±0.1140 | +0.469 | 0.6392 |  |
| Hypertension | -0.3544 | 0.8155 | ±1.6311 | -0.435 | 0.6639 |  |
| High cholesterol | -0.1282 | 0.7319 | ±1.4638 | -0.175 | 0.8610 |  |
| Kidney disease | -0.3556 | 1.6980 | ±3.3959 | -0.209 | 0.8341 |  |
| Circulatory disease | -1.9685 | 1.0697 | ±2.1394 | -1.840 | 0.0657 | . |
| Avg. daily time 54-69 (%) | -0.0837 | 0.2766 | ±0.5532 | -0.303 | 0.7622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.84e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9732** | 2.9047 | ±5.8094 | **+16.516** | **2.83e-61** | *** |
| Education: graduate level (vs college) | -1.4438 | 0.7440 | ±1.4880 | -1.941 | 0.0523 | . |
| **Education: high school or below (vs college)** | **+3.8126** | 1.7432 | ±3.4864 | **+2.187** | **0.0287** | * |
| Site: UCSD (vs UAB) | +0.6487 | 1.0003 | ±2.0005 | +0.649 | 0.5167 |  |
| Site: UW (vs UAB) | -0.1062 | 0.8588 | ±1.7175 | -0.124 | 0.9016 |  |
| **Age (years)** | **-0.3984** | 0.0329 | ±0.0659 | **-12.094** | **1.13e-33** | *** |
| BMI (kg/m2) | +0.0266 | 0.0570 | ±0.1140 | +0.466 | 0.6411 |  |
| Hypertension | -0.3527 | 0.8154 | ±1.6307 | -0.433 | 0.6653 |  |
| High cholesterol | -0.1299 | 0.7327 | ±1.4654 | -0.177 | 0.8593 |  |
| Kidney disease | -0.3515 | 1.6986 | ±3.3972 | -0.207 | 0.8361 |  |
| Circulatory disease | -1.9672 | 1.0700 | ±2.1400 | -1.839 | 0.0660 | . |
| Time < 70 (%) | -0.0591 | 0.2055 | ±0.4110 | -0.288 | 0.7737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1125**, R² = **0.1472**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.81e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9632** | 2.8939 | ±5.7877 | **+16.574** | **1.07e-61** | *** |
| Education: graduate level (vs college) | -1.4469 | 0.7441 | ±1.4882 | -1.945 | 0.0518 | . |
| **Education: high school or below (vs college)** | **+3.8078** | 1.7435 | ±3.4870 | **+2.184** | **0.0290** | * |
| Site: UCSD (vs UAB) | +0.6522 | 0.9985 | ±1.9970 | +0.653 | 0.5136 |  |
| Site: UW (vs UAB) | -0.1093 | 0.8587 | ±1.7175 | -0.127 | 0.8987 |  |
| **Age (years)** | **-0.3982** | 0.0329 | ±0.0658 | **-12.108** | **9.58e-34** | *** |
| BMI (kg/m2) | +0.0266 | 0.0570 | ±0.1140 | +0.467 | 0.6405 |  |
| Hypertension | -0.3555 | 0.8154 | ±1.6308 | -0.436 | 0.6629 |  |
| High cholesterol | -0.1299 | 0.7320 | ±1.4639 | -0.177 | 0.8591 |  |
| Kidney disease | -0.3532 | 1.6981 | ±3.3961 | -0.208 | 0.8352 |  |
| Circulatory disease | -1.9691 | 1.0696 | ±2.1393 | -1.841 | 0.0656 | . |
| Avg. daily time < 70 (%) | -0.0690 | 0.2263 | ±0.4527 | -0.305 | 0.7604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1396**, F-statistic = **17.59** (p = **1.60e-32**), Residual SE = **11.848** on **1113** df, AIC = **8766.9**, BIC = **8827.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7288** | 9.7908 | ±19.5817 | **+5.794** | **6.87e-09** | *** |
| Education: graduate level (vs college) | -1.4304 | 0.7425 | ±1.4849 | -1.927 | 0.0540 | . |
| **Education: high school or below (vs college)** | **+3.7819** | 1.7405 | ±3.4809 | **+2.173** | **0.0298** | * |
| Site: UCSD (vs UAB) | +0.6918 | 0.9948 | ±1.9897 | +0.695 | 0.4868 |  |
| Site: UW (vs UAB) | -0.0685 | 0.8592 | ±1.7184 | -0.080 | 0.9364 |  |
| **Age (years)** | **-0.3970** | 0.0329 | ±0.0658 | **-12.070** | **1.52e-33** | *** |
| BMI (kg/m2) | +0.0261 | 0.0570 | ±0.1140 | +0.459 | 0.6465 |  |
| Hypertension | -0.3358 | 0.8147 | ±1.6294 | -0.412 | 0.6802 |  |
| High cholesterol | -0.1185 | 0.7295 | ±1.4589 | -0.162 | 0.8709 |  |
| Kidney disease | -0.3867 | 1.7001 | ±3.4001 | -0.227 | 0.8201 |  |
| Circulatory disease | -2.0171 | 1.0767 | ±2.1535 | -1.873 | 0.0610 | . |
| Time 54-250, pooled (%) | -0.0896 | 0.0942 | ±0.1885 | -0.951 | 0.3416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.59** (p = **1.59e-32**), Residual SE = **11.848** on **1113** df, AIC = **8766.9**, BIC = **8827.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.1212** | 10.1068 | ±20.2136 | **+5.652** | **1.59e-08** | *** |
| Education: graduate level (vs college) | -1.4304 | 0.7425 | ±1.4849 | -1.926 | 0.0540 | . |
| **Education: high school or below (vs college)** | **+3.7805** | 1.7408 | ±3.4815 | **+2.172** | **0.0299** | * |
| Site: UCSD (vs UAB) | +0.6863 | 0.9947 | ±1.9895 | +0.690 | 0.4903 |  |
| Site: UW (vs UAB) | -0.0725 | 0.8592 | ±1.7184 | -0.084 | 0.9327 |  |
| **Age (years)** | **-0.3971** | 0.0329 | ±0.0658 | **-12.078** | **1.38e-33** | *** |
| BMI (kg/m2) | +0.0259 | 0.0570 | ±0.1140 | +0.454 | 0.6500 |  |
| Hypertension | -0.3349 | 0.8147 | ±1.6294 | -0.411 | 0.6810 |  |
| High cholesterol | -0.1209 | 0.7294 | ±1.4588 | -0.166 | 0.8684 |  |
| Kidney disease | -0.3844 | 1.6997 | ±3.3995 | -0.226 | 0.8211 |  |
| Circulatory disease | -2.0161 | 1.0767 | ±2.1534 | -1.872 | 0.0611 | . |
| Avg. daily time 54-250 (%) | -0.0933 | 0.0972 | ±0.1944 | -0.960 | 0.3372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1386**, F-statistic = **17.45** (p = **2.97e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.2**, BIC = **8828.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8699** | 2.8529 | ±5.7058 | **+16.779** | **3.46e-63** | *** |
| Education: graduate level (vs college) | -1.4340 | 0.7449 | ±1.4898 | -1.925 | 0.0542 | . |
| **Education: high school or below (vs college)** | **+3.8400** | 1.7426 | ±3.4852 | **+2.204** | **0.0276** | * |
| Site: UCSD (vs UAB) | +0.6799 | 0.9972 | ±1.9944 | +0.682 | 0.4953 |  |
| Site: UW (vs UAB) | -0.0770 | 0.8593 | ±1.7187 | -0.090 | 0.9286 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0659 | **-12.084** | **1.29e-33** | *** |
| BMI (kg/m2) | +0.0264 | 0.0572 | ±0.1144 | +0.462 | 0.6443 |  |
| Hypertension | -0.3433 | 0.8155 | ±1.6311 | -0.421 | 0.6738 |  |
| High cholesterol | -0.1137 | 0.7310 | ±1.4619 | -0.156 | 0.8763 |  |
| Kidney disease | -0.3536 | 1.6927 | ±3.3854 | -0.209 | 0.8345 |  |
| Circulatory disease | -1.9673 | 1.0710 | ±2.1419 | -1.837 | 0.0662 | . |
| Time 181-250, pooled (%) | +0.0004 | 0.0576 | ±0.1153 | +0.007 | 0.9940 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1386**, F-statistic = **17.45** (p = **2.97e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.2**, BIC = **8828.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8706** | 2.8537 | ±5.7074 | **+16.775** | **3.73e-63** | *** |
| Education: graduate level (vs college) | -1.4328 | 0.7452 | ±1.4904 | -1.923 | 0.0545 | . |
| **Education: high school or below (vs college)** | **+3.8402** | 1.7425 | ±3.4850 | **+2.204** | **0.0275** | * |
| Site: UCSD (vs UAB) | +0.6795 | 0.9978 | ±1.9955 | +0.681 | 0.4959 |  |
| Site: UW (vs UAB) | -0.0753 | 0.8591 | ±1.7183 | -0.088 | 0.9301 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0659 | **-12.086** | **1.25e-33** | *** |
| BMI (kg/m2) | +0.0265 | 0.0572 | ±0.1145 | +0.463 | 0.6436 |  |
| Hypertension | -0.3405 | 0.8162 | ±1.6323 | -0.417 | 0.6765 |  |
| High cholesterol | -0.1111 | 0.7313 | ±1.4625 | -0.152 | 0.8793 |  |
| Kidney disease | -0.3490 | 1.6927 | ±3.3854 | -0.206 | 0.8366 |  |
| Circulatory disease | -1.9665 | 1.0711 | ±2.1421 | -1.836 | 0.0663 | . |
| Avg. daily time 181-250 (%) | -0.0020 | 0.0570 | ±0.1140 | -0.035 | 0.9720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1125**, R² = **0.1474**, Adj R² = **0.1389**, F-statistic = **17.49** (p = **2.47e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.8**, BIC = **8828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8432** | 2.8483 | ±5.6965 | **+16.797** | **2.55e-63** | *** |
| Education: graduate level (vs college) | -1.4453 | 0.7433 | ±1.4866 | -1.944 | 0.0518 | . |
| **Education: high school or below (vs college)** | **+3.8168** | 1.7427 | ±3.4855 | **+2.190** | **0.0285** | * |
| Site: UCSD (vs UAB) | +0.6814 | 0.9959 | ±1.9918 | +0.684 | 0.4939 |  |
| Site: UW (vs UAB) | -0.0978 | 0.8609 | ±1.7218 | -0.114 | 0.9096 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0657 | **-12.106** | **9.79e-34** | *** |
| BMI (kg/m2) | +0.0256 | 0.0571 | ±0.1143 | +0.448 | 0.6540 |  |
| Hypertension | -0.3720 | 0.8163 | ±1.6325 | -0.456 | 0.6485 |  |
| High cholesterol | -0.1449 | 0.7299 | ±1.4597 | -0.199 | 0.8426 |  |
| Kidney disease | -0.4098 | 1.6932 | ±3.3864 | -0.242 | 0.8087 |  |
| Circulatory disease | -1.9894 | 1.0733 | ±2.1466 | -1.853 | 0.0638 | . |
| Time > 180 (%) | +0.0260 | 0.0450 | ±0.0900 | +0.578 | 0.5634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1473**, Adj R² = **0.1389**, F-statistic = **17.48** (p = **2.55e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.9**, BIC = **8828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8507** | 2.8489 | ±5.6978 | **+16.796** | **2.60e-63** | *** |
| Education: graduate level (vs college) | -1.4451 | 0.7434 | ±1.4869 | -1.944 | 0.0519 | . |
| **Education: high school or below (vs college)** | **+3.8215** | 1.7429 | ±3.4859 | **+2.193** | **0.0283** | * |
| Site: UCSD (vs UAB) | +0.6835 | 0.9962 | ±1.9925 | +0.686 | 0.4927 |  |
| Site: UW (vs UAB) | -0.0948 | 0.8608 | ±1.7215 | -0.110 | 0.9123 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0657 | **-12.106** | **9.80e-34** | *** |
| BMI (kg/m2) | +0.0255 | 0.0572 | ±0.1144 | +0.447 | 0.6550 |  |
| Hypertension | -0.3696 | 0.8166 | ±1.6333 | -0.453 | 0.6509 |  |
| High cholesterol | -0.1426 | 0.7302 | ±1.4604 | -0.195 | 0.8452 |  |
| Kidney disease | -0.4048 | 1.6932 | ±3.3864 | -0.239 | 0.8111 |  |
| Circulatory disease | -1.9879 | 1.0734 | ±2.1467 | -1.852 | 0.0640 | . |
| Avg. daily time > 180 (%) | +0.0237 | 0.0450 | ±0.0899 | +0.526 | 0.5987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1386**, F-statistic = **17.45** (p = **2.97e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.2**, BIC = **8828.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8716** | 2.8542 | ±5.7084 | **+16.772** | **3.90e-63** | *** |
| Education: graduate level (vs college) | -1.4335 | 0.7429 | ±1.4858 | -1.930 | 0.0537 | . |
| **Education: high school or below (vs college)** | **+3.8386** | 1.7449 | ±3.4898 | **+2.200** | **0.0278** | * |
| Site: UCSD (vs UAB) | +0.6800 | 0.9973 | ±1.9946 | +0.682 | 0.4953 |  |
| Site: UW (vs UAB) | -0.0781 | 0.8610 | ±1.7219 | -0.091 | 0.9277 |  |
| **Age (years)** | **-0.3979** | 0.0329 | ±0.0657 | **-12.111** | **9.27e-34** | *** |
| BMI (kg/m2) | +0.0262 | 0.0578 | ±0.1156 | +0.453 | 0.6508 |  |
| Hypertension | -0.3440 | 0.8169 | ±1.6338 | -0.421 | 0.6737 |  |
| High cholesterol | -0.1170 | 0.7319 | ±1.4639 | -0.160 | 0.8730 |  |
| Kidney disease | -0.3535 | 1.6989 | ±3.3979 | -0.208 | 0.8352 |  |
| Circulatory disease | -1.9677 | 1.0709 | ±2.1417 | -1.837 | 0.0661 | . |
| Nocturnal time > 180 (%) | +0.0025 | 0.0488 | ±0.0976 | +0.052 | 0.9586 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1483**, Adj R² = **0.1399**, F-statistic = **17.62** (p = **1.39e-32**), Residual SE = **11.846** on **1113** df, AIC = **8766.6**, BIC = **8826.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5446** | 2.8702 | ±5.7403 | **+16.565** | **1.25e-61** | *** |
| Education: graduate level (vs college) | -1.4354 | 0.7426 | ±1.4853 | -1.933 | 0.0533 | . |
| **Education: high school or below (vs college)** | **+3.8263** | 1.7370 | ±3.4739 | **+2.203** | **0.0276** | * |
| Site: UCSD (vs UAB) | +0.6755 | 0.9951 | ±1.9903 | +0.679 | 0.4972 |  |
| Site: UW (vs UAB) | -0.1025 | 0.8609 | ±1.7218 | -0.119 | 0.9053 |  |
| **Age (years)** | **-0.3981** | 0.0329 | ±0.0657 | **-12.109** | **9.41e-34** | *** |
| BMI (kg/m2) | +0.0323 | 0.0572 | ±0.1144 | +0.565 | 0.5718 |  |
| Hypertension | -0.4140 | 0.8152 | ±1.6303 | -0.508 | 0.6116 |  |
| High cholesterol | -0.1572 | 0.7281 | ±1.4561 | -0.216 | 0.8290 |  |
| Kidney disease | -0.3942 | 1.6931 | ±3.3863 | -0.233 | 0.8159 |  |
| Circulatory disease | -1.9562 | 1.0706 | ±2.1411 | -1.827 | 0.0677 | . |
| Any reading > 250 during wear (0/1) | +1.1391 | 0.9316 | ±1.8632 | +1.223 | 0.2214 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.59** (p = **1.54e-32**), Residual SE = **11.847** on **1113** df, AIC = **8766.8**, BIC = **8827.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8043** | 2.8513 | ±5.7027 | **+16.766** | **4.36e-63** | *** |
| Education: graduate level (vs college) | -1.4324 | 0.7424 | ±1.4847 | -1.929 | 0.0537 | . |
| **Education: high school or below (vs college)** | **+3.7707** | 1.7408 | ±3.4816 | **+2.166** | **0.0303** | * |
| Site: UCSD (vs UAB) | +0.6740 | 0.9948 | ±1.9896 | +0.678 | 0.4981 |  |
| Site: UW (vs UAB) | -0.0820 | 0.8593 | ±1.7185 | -0.095 | 0.9240 |  |
| **Age (years)** | **-0.3970** | 0.0329 | ±0.0658 | **-12.075** | **1.43e-33** | *** |
| BMI (kg/m2) | +0.0260 | 0.0570 | ±0.1139 | +0.456 | 0.6481 |  |
| Hypertension | -0.3396 | 0.8147 | ±1.6293 | -0.417 | 0.6767 |  |
| High cholesterol | -0.1270 | 0.7293 | ±1.4586 | -0.174 | 0.8618 |  |
| Kidney disease | -0.3841 | 1.6996 | ±3.3992 | -0.226 | 0.8212 |  |
| Circulatory disease | -2.0191 | 1.0769 | ±2.1537 | -1.875 | 0.0608 | . |
| Time > 250 (%) | +0.0932 | 0.0947 | ±0.1895 | +0.984 | 0.3252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.59** (p = **1.55e-32**), Residual SE = **11.847** on **1113** df, AIC = **8766.8**, BIC = **8827.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8140** | 2.8511 | ±5.7022 | **+16.770** | **4.02e-63** | *** |
| Education: graduate level (vs college) | -1.4326 | 0.7424 | ±1.4848 | -1.930 | 0.0536 | . |
| **Education: high school or below (vs college)** | **+3.7721** | 1.7410 | ±3.4820 | **+2.167** | **0.0303** | * |
| Site: UCSD (vs UAB) | +0.6740 | 0.9948 | ±1.9895 | +0.678 | 0.4981 |  |
| Site: UW (vs UAB) | -0.0842 | 0.8594 | ±1.7187 | -0.098 | 0.9220 |  |
| **Age (years)** | **-0.3971** | 0.0329 | ±0.0658 | **-12.077** | **1.39e-33** | *** |
| BMI (kg/m2) | +0.0258 | 0.0570 | ±0.1140 | +0.452 | 0.6511 |  |
| Hypertension | -0.3390 | 0.8147 | ±1.6294 | -0.416 | 0.6773 |  |
| High cholesterol | -0.1271 | 0.7293 | ±1.4586 | -0.174 | 0.8617 |  |
| Kidney disease | -0.3825 | 1.6994 | ±3.3989 | -0.225 | 0.8219 |  |
| Circulatory disease | -2.0186 | 1.0767 | ±2.1534 | -1.875 | 0.0608 | . |
| Avg. daily time > 250 (%) | +0.0959 | 0.0975 | ±0.1950 | +0.983 | 0.3254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 1,128; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1128**, R² = **0.1380**, Adj R² = **0.1303**, F-statistic = **17.89** (p = **1.47e-30**), Residual SE = **7.415** on **1117** df, AIC = **7732.0**, BIC = **7787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6111** | 2.0009 | ±4.0018 | **+31.292** | **6.04e-215** | *** |
| Education: graduate level (vs college) | -0.8967 | 0.4744 | ±0.9487 | -1.890 | 0.0587 | . |
| Education: high school or below (vs college) | -0.1804 | 0.9266 | ±1.8533 | -0.195 | 0.8456 |  |
| **Site: UCSD (vs UAB)** | **-1.9665** | 0.6187 | ±1.2375 | **-3.178** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3272** | 0.5477 | ±1.0954 | **-4.249** | **2.15e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.039** | **1.55e-09** | *** |
| **BMI (kg/m2)** | **+0.2547** | 0.0394 | ±0.0789 | **+6.458** | **1.06e-10** | *** |
| Hypertension | +0.5130 | 0.5143 | ±1.0287 | +0.997 | 0.3185 |  |
| High cholesterol | -0.3462 | 0.4651 | ±0.9302 | -0.744 | 0.4567 |  |
| Kidney disease | +0.8191 | 1.0332 | ±2.0664 | +0.793 | 0.4279 |  |
| Circulatory disease | +0.3881 | 0.6883 | ±1.3767 | +0.564 | 0.5729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1128**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.63** (p = **1.26e-32**), Residual SE = **7.375** on **1116** df, AIC = **7720.7**, BIC = **7781.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8216** | 2.7690 | ±5.5379 | **+19.799** | **3.06e-87** | *** |
| Education: graduate level (vs college) | -0.8949 | 0.4717 | ±0.9435 | -1.897 | 0.0578 | . |
| Education: high school or below (vs college) | -0.3540 | 0.9115 | ±1.8230 | -0.388 | 0.6977 |  |
| **Site: UCSD (vs UAB)** | **-2.0459** | 0.6184 | ±1.2368 | **-3.308** | **9.38e-04** | *** |
| **Site: UW (vs UAB)** | **-2.3954** | 0.5430 | ±1.0860 | **-4.411** | **1.03e-05** | *** |
| **Age (years)** | **-0.1365** | 0.0215 | ±0.0431 | **-6.338** | **2.32e-10** | *** |
| **BMI (kg/m2)** | **+0.2437** | 0.0387 | ±0.0774 | **+6.294** | **3.09e-10** | *** |
| Hypertension | +0.4398 | 0.5117 | ±1.0233 | +0.860 | 0.3900 |  |
| High cholesterol | -0.5650 | 0.4606 | ±0.9211 | -1.227 | 0.2199 |  |
| Kidney disease | +0.8213 | 1.0210 | ±2.0419 | +0.804 | 0.4212 |  |
| Circulatory disease | +0.3031 | 0.6654 | ±1.3309 | +0.455 | 0.6488 |  |
| **HbA1c (%)** | **+1.5335** | 0.4072 | ±0.8144 | **+3.766** | **1.66e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1128**, R² = **0.1478**, Adj R² = **0.1394**, F-statistic = **17.60** (p = **1.48e-32**), Residual SE = **7.376** on **1116** df, AIC = **7721.1**, BIC = **7781.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.0003** | 2.4051 | ±4.8101 | **+24.116** | **1.70e-128** | *** |
| **Education: graduate level (vs college)** | **-0.9726** | 0.4731 | ±0.9463 | **-2.056** | **0.0398** | * |
| Education: high school or below (vs college) | -0.3197 | 0.9066 | ±1.8131 | -0.353 | 0.7244 |  |
| **Site: UCSD (vs UAB)** | **-2.0043** | 0.6180 | ±1.2360 | **-3.243** | **0.0012** | ** |
| **Site: UW (vs UAB)** | **-2.4817** | 0.5463 | ±1.0927 | **-4.542** | **5.56e-06** | *** |
| **Age (years)** | **-0.1325** | 0.0214 | ±0.0428 | **-6.190** | **6.03e-10** | *** |
| **BMI (kg/m2)** | **+0.2486** | 0.0392 | ±0.0784 | **+6.344** | **2.23e-10** | *** |
| Hypertension | +0.3703 | 0.5148 | ±1.0295 | +0.719 | 0.4719 |  |
| High cholesterol | -0.4799 | 0.4612 | ±0.9225 | -1.040 | 0.2982 |  |
| Kidney disease | +0.6393 | 1.0174 | ±2.0348 | +0.628 | 0.5298 |  |
| Circulatory disease | +0.3185 | 0.6682 | ±1.3364 | +0.477 | 0.6336 |  |
| **Mean glucose (mg/dL)** | **+0.0428** | 0.0133 | ±0.0267 | **+3.207** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1128**, R² = **0.1478**, Adj R² = **0.1394**, F-statistic = **17.60** (p = **1.48e-32**), Residual SE = **7.376** on **1116** df, AIC = **7721.1**, BIC = **7781.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0832** | 3.7783 | ±7.5566 | **+13.785** | **3.15e-43** | *** |
| **Education: graduate level (vs college)** | **-0.9726** | 0.4731 | ±0.9463 | **-2.056** | **0.0398** | * |
| Education: high school or below (vs college) | -0.3197 | 0.9066 | ±1.8131 | -0.353 | 0.7244 |  |
| **Site: UCSD (vs UAB)** | **-2.0043** | 0.6180 | ±1.2360 | **-3.243** | **0.0012** | ** |
| **Site: UW (vs UAB)** | **-2.4817** | 0.5463 | ±1.0927 | **-4.542** | **5.56e-06** | *** |
| **Age (years)** | **-0.1325** | 0.0214 | ±0.0428 | **-6.190** | **6.03e-10** | *** |
| **BMI (kg/m2)** | **+0.2486** | 0.0392 | ±0.0784 | **+6.344** | **2.23e-10** | *** |
| Hypertension | +0.3703 | 0.5148 | ±1.0295 | +0.719 | 0.4719 |  |
| High cholesterol | -0.4799 | 0.4612 | ±0.9225 | -1.040 | 0.2982 |  |
| Kidney disease | +0.6393 | 1.0174 | ±2.0348 | +0.628 | 0.5298 |  |
| Circulatory disease | +0.3185 | 0.6682 | ±1.3364 | +0.477 | 0.6336 |  |
| **GMI (%)** | **+1.7876** | 0.5573 | ±1.1147 | **+3.207** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1128**, R² = **0.1466**, Adj R² = **0.1382**, F-statistic = **17.43** (p = **3.13e-32**), Residual SE = **7.381** on **1116** df, AIC = **7722.7**, BIC = **7783.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5668** | 2.3312 | ±4.6623 | **+25.123** | **2.76e-139** | *** |
| **Education: graduate level (vs college)** | **-0.9331** | 0.4727 | ±0.9454 | **-1.974** | **0.0484** | * |
| Education: high school or below (vs college) | -0.3110 | 0.9089 | ±1.8178 | -0.342 | 0.7322 |  |
| **Site: UCSD (vs UAB)** | **-2.0509** | 0.6192 | ±1.2383 | **-3.312** | **9.25e-04** | *** |
| **Site: UW (vs UAB)** | **-2.4617** | 0.5456 | ±1.0912 | **-4.512** | **6.43e-06** | *** |
| **Age (years)** | **-0.1287** | 0.0214 | ±0.0428 | **-6.008** | **1.87e-09** | *** |
| **BMI (kg/m2)** | **+0.2395** | 0.0391 | ±0.0782 | **+6.124** | **9.11e-10** | *** |
| Hypertension | +0.4073 | 0.5141 | ±1.0281 | +0.792 | 0.4282 |  |
| High cholesterol | -0.4976 | 0.4625 | ±0.9249 | -1.076 | 0.2819 |  |
| Kidney disease | +0.7682 | 1.0159 | ±2.0319 | +0.756 | 0.4496 |  |
| Circulatory disease | +0.3595 | 0.6699 | ±1.3398 | +0.537 | 0.5916 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0384** | 0.0128 | ±0.0256 | **+3.004** | **0.0027** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1128**, R² = **0.1480**, Adj R² = **0.1397**, F-statistic = **17.63** (p = **1.29e-32**), Residual SE = **7.375** on **1116** df, AIC = **7720.8**, BIC = **7781.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1552** | 2.0610 | ±4.1220 | **+29.188** | **2.78e-187** | *** |
| Education: graduate level (vs college) | -0.9105 | 0.4706 | ±0.9412 | -1.935 | 0.0530 | . |
| Education: high school or below (vs college) | -0.2003 | 0.9060 | ±1.8121 | -0.221 | 0.8250 |  |
| **Site: UCSD (vs UAB)** | **-1.8946** | 0.6162 | ±1.2324 | **-3.075** | **0.0021** | ** |
| **Site: UW (vs UAB)** | **-2.4054** | 0.5448 | ±1.0897 | **-4.415** | **1.01e-05** | *** |
| **Age (years)** | **-0.1338** | 0.0214 | ±0.0428 | **-6.246** | **4.22e-10** | *** |
| **BMI (kg/m2)** | **+0.2571** | 0.0392 | ±0.0785 | **+6.552** | **5.68e-11** | *** |
| Hypertension | +0.3531 | 0.5150 | ±1.0301 | +0.686 | 0.4929 |  |
| High cholesterol | -0.3889 | 0.4617 | ±0.9235 | -0.842 | 0.3996 |  |
| Kidney disease | +0.5135 | 1.0325 | ±2.0651 | +0.497 | 0.6190 |  |
| Circulatory disease | +0.3235 | 0.6671 | ±1.3343 | +0.485 | 0.6278 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1259** | 0.0371 | ±0.0742 | **+3.392** | **6.93e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1128**, R² = **0.1469**, Adj R² = **0.1384**, F-statistic = **17.46** (p = **2.71e-32**), Residual SE = **7.380** on **1116** df, AIC = **7722.4**, BIC = **7782.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5294** | 2.0357 | ±4.0713 | **+29.735** | **2.75e-194** | *** |
| Education: graduate level (vs college) | -0.9197 | 0.4714 | ±0.9428 | -1.951 | 0.0511 | . |
| Education: high school or below (vs college) | -0.2103 | 0.9074 | ±1.8148 | -0.232 | 0.8167 |  |
| **Site: UCSD (vs UAB)** | **-1.9161** | 0.6159 | ±1.2317 | **-3.111** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.4157** | 0.5463 | ±1.0926 | **-4.422** | **9.78e-06** | *** |
| **Age (years)** | **-0.1345** | 0.0215 | ±0.0429 | **-6.264** | **3.75e-10** | *** |
| **BMI (kg/m2)** | **+0.2551** | 0.0391 | ±0.0781 | **+6.530** | **6.59e-11** | *** |
| Hypertension | +0.3634 | 0.5169 | ±1.0338 | +0.703 | 0.4820 |  |
| High cholesterol | -0.3875 | 0.4621 | ±0.9243 | -0.839 | 0.4017 |  |
| Kidney disease | +0.5395 | 1.0295 | ±2.0589 | +0.524 | 0.6002 |  |
| Circulatory disease | +0.3282 | 0.6686 | ±1.3372 | +0.491 | 0.6236 |  |
| **Avg. daily SD (mg/dL)** | **+0.1250** | 0.0393 | ±0.0787 | **+3.178** | **0.0015** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1128**, R² = **0.1419**, Adj R² = **0.1335**, F-statistic = **16.78** (p = **5.84e-31**), Residual SE = **7.402** on **1116** df, AIC = **7728.9**, BIC = **7789.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3685** | 2.1660 | ±4.3320 | **+27.871** | **6.01e-171** | *** |
| Education: graduate level (vs college) | -0.8719 | 0.4723 | ±0.9446 | -1.846 | 0.0649 | . |
| Education: high school or below (vs college) | -0.1391 | 0.9197 | ±1.8393 | -0.151 | 0.8798 |  |
| **Site: UCSD (vs UAB)** | **-1.8826** | 0.6170 | ±1.2341 | **-3.051** | **0.0023** | ** |
| **Site: UW (vs UAB)** | **-2.3156** | 0.5464 | ±1.0928 | **-4.238** | **2.25e-05** | *** |
| **Age (years)** | **-0.1324** | 0.0216 | ±0.0432 | **-6.134** | **8.55e-10** | *** |
| **BMI (kg/m2)** | **+0.2591** | 0.0395 | ±0.0790 | **+6.560** | **5.38e-11** | *** |
| Hypertension | +0.4497 | 0.5139 | ±1.0277 | +0.875 | 0.3815 |  |
| High cholesterol | -0.3141 | 0.4654 | ±0.9307 | -0.675 | 0.4997 |  |
| Kidney disease | +0.6686 | 1.0411 | ±2.0822 | +0.642 | 0.5208 |  |
| Circulatory disease | +0.3741 | 0.6809 | ±1.3617 | +0.549 | 0.5827 |  |
| **CV (%)** | **+0.1246** | 0.0538 | ±0.1077 | **+2.316** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1128**, R² = **0.1422**, Adj R² = **0.1337**, F-statistic = **16.82** (p = **4.92e-31**), Residual SE = **7.400** on **1116** df, AIC = **7728.5**, BIC = **7788.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.1189** | 2.2941 | ±4.5883 | **+28.385** | **3.10e-177** | *** |
| Education: graduate level (vs college) | -0.8661 | 0.4720 | ±0.9440 | -1.835 | 0.0665 | . |
| Education: high school or below (vs college) | -0.1669 | 0.9195 | ±1.8391 | -0.182 | 0.8560 |  |
| **Site: UCSD (vs UAB)** | **-1.8853** | 0.6169 | ±1.2337 | **-3.056** | **0.0022** | ** |
| **Site: UW (vs UAB)** | **-2.3416** | 0.5465 | ±1.0929 | **-4.285** | **1.83e-05** | *** |
| **Age (years)** | **-0.1326** | 0.0216 | ±0.0432 | **-6.141** | **8.20e-10** | *** |
| **BMI (kg/m2)** | **+0.2585** | 0.0394 | ±0.0788 | **+6.562** | **5.32e-11** | *** |
| Hypertension | +0.4368 | 0.5138 | ±1.0276 | +0.850 | 0.3953 |  |
| High cholesterol | -0.3230 | 0.4650 | ±0.9299 | -0.695 | 0.4873 |  |
| Kidney disease | +0.7096 | 1.0388 | ±2.0775 | +0.683 | 0.4946 |  |
| Circulatory disease | +0.3788 | 0.6803 | ±1.3606 | +0.557 | 0.5777 |  |
| **Mean / SD ratio** | **-0.4227** | 0.1740 | ±0.3480 | **-2.429** | **0.0151** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1128**, R² = **0.1420**, Adj R² = **0.1335**, F-statistic = **16.79** (p = **5.59e-31**), Residual SE = **7.401** on **1116** df, AIC = **7728.8**, BIC = **7789.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.0911** | 2.3024 | ±4.6049 | **+28.270** | **8.00e-176** | *** |
| Education: graduate level (vs college) | -0.8843 | 0.4724 | ±0.9447 | -1.872 | 0.0612 | . |
| Education: high school or below (vs college) | -0.1961 | 0.9192 | ±1.8385 | -0.213 | 0.8311 |  |
| **Site: UCSD (vs UAB)** | **-1.9065** | 0.6167 | ±1.2333 | **-3.092** | **0.0020** | ** |
| **Site: UW (vs UAB)** | **-2.3545** | 0.5472 | ±1.0944 | **-4.303** | **1.69e-05** | *** |
| **Age (years)** | **-0.1336** | 0.0217 | ±0.0433 | **-6.166** | **6.99e-10** | *** |
| **BMI (kg/m2)** | **+0.2561** | 0.0392 | ±0.0783 | **+6.537** | **6.27e-11** | *** |
| Hypertension | +0.4561 | 0.5151 | ±1.0302 | +0.886 | 0.3759 |  |
| High cholesterol | -0.3256 | 0.4652 | ±0.9304 | -0.700 | 0.4840 |  |
| Kidney disease | +0.6915 | 1.0358 | ±2.0716 | +0.668 | 0.5044 |  |
| Circulatory disease | +0.3842 | 0.6814 | ±1.3627 | +0.564 | 0.5728 |  |
| **Avg. daily mean/SD** | **-0.3429** | 0.1454 | ±0.2908 | **-2.358** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1128**, R² = **0.1477**, Adj R² = **0.1393**, F-statistic = **17.59** (p = **1.56e-32**), Residual SE = **7.376** on **1116** df, AIC = **7721.2**, BIC = **7781.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3888** | 2.2798 | ±4.5597 | **+25.611** | **1.15e-144** | *** |
| Education: graduate level (vs college) | -0.8587 | 0.4700 | ±0.9400 | -1.827 | 0.0677 | . |
| Education: high school or below (vs college) | -0.2433 | 0.9137 | ±1.8273 | -0.266 | 0.7900 |  |
| **Site: UCSD (vs UAB)** | **-1.8593** | 0.6156 | ±1.2313 | **-3.020** | **0.0025** | ** |
| **Site: UW (vs UAB)** | **-2.2175** | 0.5491 | ±1.0982 | **-4.039** | **5.38e-05** | *** |
| **Age (years)** | **-0.1272** | 0.0214 | ±0.0428 | **-5.950** | **2.68e-09** | *** |
| **BMI (kg/m2)** | **+0.2569** | 0.0388 | ±0.0775 | **+6.628** | **3.40e-11** | *** |
| Hypertension | +0.5257 | 0.5142 | ±1.0285 | +1.022 | 0.3066 |  |
| High cholesterol | -0.2921 | 0.4636 | ±0.9272 | -0.630 | 0.5286 |  |
| Kidney disease | +0.6851 | 1.0235 | ±2.0469 | +0.669 | 0.5032 |  |
| Circulatory disease | +0.4285 | 0.6780 | ±1.3560 | +0.632 | 0.5274 |  |
| **MAG (mg/dL/h)** | **+0.1013** | 0.0304 | ±0.0609 | **+3.329** | **8.71e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1128**, R² = **0.1450**, Adj R² = **0.1365**, F-statistic = **17.20** (p = **8.85e-32**), Residual SE = **7.388** on **1116** df, AIC = **7724.9**, BIC = **7785.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.0904** | 2.1233 | ±4.2466 | **+28.301** | **3.38e-176** | *** |
| Education: graduate level (vs college) | -0.9188 | 0.4722 | ±0.9443 | -1.946 | 0.0517 | . |
| Education: high school or below (vs college) | -0.2297 | 0.9111 | ±1.8223 | -0.252 | 0.8010 |  |
| **Site: UCSD (vs UAB)** | **-1.9209** | 0.6160 | ±1.2319 | **-3.119** | **0.0018** | ** |
| **Site: UW (vs UAB)** | **-2.3794** | 0.5465 | ±1.0930 | **-4.354** | **1.34e-05** | *** |
| **Age (years)** | **-0.1331** | 0.0215 | ±0.0430 | **-6.189** | **6.07e-10** | *** |
| **BMI (kg/m2)** | **+0.2616** | 0.0395 | ±0.0790 | **+6.618** | **3.64e-11** | *** |
| Hypertension | +0.4196 | 0.5168 | ±1.0337 | +0.812 | 0.4168 |  |
| High cholesterol | -0.3497 | 0.4638 | ±0.9275 | -0.754 | 0.4508 |  |
| Kidney disease | +0.6286 | 1.0318 | ±2.0636 | +0.609 | 0.5424 |  |
| Circulatory disease | +0.3459 | 0.6733 | ±1.3466 | +0.514 | 0.6074 |  |
| **Avg. daily range (mg/dL)** | **+0.0260** | 0.0088 | ±0.0176 | **+2.965** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1128**, R² = **0.1516**, Adj R² = **0.1432**, F-statistic = **18.12** (p = **1.41e-33**), Residual SE = **7.360** on **1116** df, AIC = **7716.1**, BIC = **7776.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.7469** | 2.0032 | ±4.0064 | **+30.325** | **5.34e-202** | *** |
| Education: graduate level (vs college) | -0.9071 | 0.4698 | ±0.9395 | -1.931 | 0.0535 | . |
| Education: high school or below (vs college) | -0.1098 | 0.9051 | ±1.8103 | -0.121 | 0.9034 |  |
| **Site: UCSD (vs UAB)** | **-1.8198** | 0.6149 | ±1.2298 | **-2.960** | **0.0031** | ** |
| **Site: UW (vs UAB)** | **-2.3464** | 0.5402 | ±1.0805 | **-4.343** | **1.40e-05** | *** |
| **Age (years)** | **-0.1286** | 0.0213 | ±0.0426 | **-6.039** | **1.56e-09** | *** |
| **BMI (kg/m2)** | **+0.2485** | 0.0393 | ±0.0787 | **+6.316** | **2.69e-10** | *** |
| Hypertension | +0.4652 | 0.5084 | ±1.0169 | +0.915 | 0.3602 |  |
| High cholesterol | -0.4404 | 0.4614 | ±0.9227 | -0.955 | 0.3398 |  |
| Kidney disease | +0.7289 | 1.0283 | ±2.0566 | +0.709 | 0.4784 |  |
| Circulatory disease | +0.3345 | 0.6707 | ±1.3414 | +0.499 | 0.6180 |  |
| **SD of daily means (mg/dL)** | **+0.2998** | 0.0759 | ±0.1518 | **+3.950** | **7.81e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1128**, R² = **0.1463**, Adj R² = **0.1378**, F-statistic = **17.38** (p = **3.92e-32**), Residual SE = **7.383** on **1116** df, AIC = **7723.1**, BIC = **7783.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8747** | 3.9915 | ±7.9830 | **+17.756** | **1.54e-70** | *** |
| Education: graduate level (vs college) | -0.9193 | 0.4716 | ±0.9433 | -1.949 | 0.0513 | . |
| Education: high school or below (vs college) | -0.2230 | 0.9094 | ±1.8187 | -0.245 | 0.8062 |  |
| **Site: UCSD (vs UAB)** | **-1.9181** | 0.6187 | ±1.2374 | **-3.100** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.3534** | 0.5434 | ±1.0869 | **-4.330** | **1.49e-05** | *** |
| **Age (years)** | **-0.1297** | 0.0214 | ±0.0427 | **-6.072** | **1.26e-09** | *** |
| **BMI (kg/m2)** | **+0.2519** | 0.0393 | ±0.0787 | **+6.405** | **1.50e-10** | *** |
| Hypertension | +0.4303 | 0.5140 | ±1.0280 | +0.837 | 0.4025 |  |
| High cholesterol | -0.4239 | 0.4623 | ±0.9246 | -0.917 | 0.3592 |  |
| Kidney disease | +0.6241 | 1.0250 | ±2.0499 | +0.609 | 0.5426 |  |
| Circulatory disease | +0.3156 | 0.6719 | ±1.3438 | +0.470 | 0.6385 |  |
| **Time in range 70-180, pooled (%)** | **-0.0850** | 0.0347 | ±0.0693 | **-2.453** | **0.0142** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1128**, R² = **0.1459**, Adj R² = **0.1375**, F-statistic = **17.33** (p = **4.90e-32**), Residual SE = **7.384** on **1116** df, AIC = **7723.6**, BIC = **7783.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7173** | 4.0101 | ±8.0202 | **+17.635** | **1.33e-69** | *** |
| Education: graduate level (vs college) | -0.9198 | 0.4718 | ±0.9436 | -1.949 | 0.0512 | . |
| Education: high school or below (vs college) | -0.2118 | 0.9094 | ±1.8189 | -0.233 | 0.8158 |  |
| **Site: UCSD (vs UAB)** | **-1.9219** | 0.6186 | ±1.2371 | **-3.107** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.3512** | 0.5436 | ±1.0872 | **-4.325** | **1.52e-05** | *** |
| **Age (years)** | **-0.1300** | 0.0214 | ±0.0428 | **-6.079** | **1.21e-09** | *** |
| **BMI (kg/m2)** | **+0.2515** | 0.0393 | ±0.0786 | **+6.401** | **1.55e-10** | *** |
| Hypertension | +0.4330 | 0.5140 | ±1.0281 | +0.842 | 0.3996 |  |
| High cholesterol | -0.4274 | 0.4624 | ±0.9248 | -0.924 | 0.3553 |  |
| Kidney disease | +0.6315 | 1.0250 | ±2.0500 | +0.616 | 0.5378 |  |
| Circulatory disease | +0.3179 | 0.6724 | ±1.3447 | +0.473 | 0.6363 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0829** | 0.0346 | ±0.0691 | **-2.397** | **0.0165** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1128**, R² = **0.1387**, Adj R² = **0.1302**, F-statistic = **16.33** (p = **4.32e-30**), Residual SE = **7.415** on **1116** df, AIC = **7733.1**, BIC = **7793.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3606** | 2.0120 | ±4.0239 | **+30.995** | **6.34e-211** | *** |
| Education: graduate level (vs college) | -0.8836 | 0.4751 | ±0.9503 | -1.860 | 0.0629 | . |
| Education: high school or below (vs college) | -0.1358 | 0.9340 | ±1.8679 | -0.145 | 0.8844 |  |
| **Site: UCSD (vs UAB)** | **-1.8975** | 0.6227 | ±1.2454 | **-3.047** | **0.0023** | ** |
| **Site: UW (vs UAB)** | **-2.2973** | 0.5490 | ±1.0980 | **-4.185** | **2.86e-05** | *** |
| **Age (years)** | **-0.1290** | 0.0216 | ±0.0432 | **-5.976** | **2.28e-09** | *** |
| **BMI (kg/m2)** | **+0.2540** | 0.0394 | ±0.0788 | **+6.446** | **1.15e-10** | *** |
| Hypertension | +0.5078 | 0.5155 | ±1.0309 | +0.985 | 0.3246 |  |
| High cholesterol | -0.3188 | 0.4660 | ±0.9321 | -0.684 | 0.4940 |  |
| Kidney disease | +0.8285 | 1.0360 | ±2.0721 | +0.800 | 0.4239 |  |
| Circulatory disease | +0.3372 | 0.6914 | ±1.3829 | +0.488 | 0.6257 |  |
| Any reading < 54 during wear (0/1) | +0.4364 | 0.4846 | ±0.9693 | +0.900 | 0.3679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1128**, R² = **0.1385**, Adj R² = **0.1300**, F-statistic = **16.31** (p = **4.84e-30**), Residual SE = **7.416** on **1116** df, AIC = **7733.4**, BIC = **7793.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.4834** | 2.0133 | ±4.0267 | **+31.035** | **1.84e-211** | *** |
| Education: graduate level (vs college) | -0.8901 | 0.4745 | ±0.9490 | -1.876 | 0.0607 | . |
| Education: high school or below (vs college) | -0.1533 | 0.9282 | ±1.8563 | -0.165 | 0.8688 |  |
| **Site: UCSD (vs UAB)** | **-1.9102** | 0.6231 | ±1.2462 | **-3.066** | **0.0022** | ** |
| **Site: UW (vs UAB)** | **-2.2847** | 0.5507 | ±1.1014 | **-4.149** | **3.34e-05** | *** |
| **Age (years)** | **-0.1300** | 0.0216 | ±0.0432 | **-6.018** | **1.77e-09** | *** |
| **BMI (kg/m2)** | **+0.2551** | 0.0395 | ±0.0790 | **+6.459** | **1.06e-10** | *** |
| Hypertension | +0.5255 | 0.5148 | ±1.0297 | +1.021 | 0.3074 |  |
| High cholesterol | -0.3206 | 0.4659 | ±0.9317 | -0.688 | 0.4913 |  |
| Kidney disease | +0.8065 | 1.0346 | ±2.0692 | +0.780 | 0.4357 |  |
| Circulatory disease | +0.3879 | 0.6889 | ±1.3778 | +0.563 | 0.5734 |  |
| Time < 54 (%) | +0.2878 | 0.2594 | ±0.5189 | +1.109 | 0.2673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1128**, R² = **0.1383**, Adj R² = **0.1298**, F-statistic = **16.28** (p = **5.54e-30**), Residual SE = **7.417** on **1116** df, AIC = **7733.6**, BIC = **7794.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5443** | 2.0091 | ±4.0183 | **+31.130** | **9.44e-213** | *** |
| Education: graduate level (vs college) | -0.8898 | 0.4748 | ±0.9495 | -1.874 | 0.0609 | . |
| Education: high school or below (vs college) | -0.1610 | 0.9280 | ±1.8560 | -0.174 | 0.8623 |  |
| **Site: UCSD (vs UAB)** | **-1.9303** | 0.6222 | ±1.2443 | **-3.103** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.2933** | 0.5511 | ±1.1022 | **-4.161** | **3.16e-05** | *** |
| **Age (years)** | **-0.1304** | 0.0216 | ±0.0432 | **-6.037** | **1.57e-09** | *** |
| **BMI (kg/m2)** | **+0.2549** | 0.0395 | ±0.0790 | **+6.456** | **1.08e-10** | *** |
| Hypertension | +0.5254 | 0.5153 | ±1.0306 | +1.020 | 0.3079 |  |
| High cholesterol | -0.3287 | 0.4663 | ±0.9326 | -0.705 | 0.4809 |  |
| Kidney disease | +0.8109 | 1.0340 | ±2.0680 | +0.784 | 0.4329 |  |
| Circulatory disease | +0.3913 | 0.6889 | ±1.3778 | +0.568 | 0.5700 |  |
| Avg. daily time < 54 (%) | +0.2783 | 0.3599 | ±0.7198 | +0.773 | 0.4393 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1128**, R² = **0.1380**, Adj R² = **0.1295**, F-statistic = **16.25** (p = **6.41e-30**), Residual SE = **7.418** on **1116** df, AIC = **7734.0**, BIC = **7794.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6064** | 2.0152 | ±4.0304 | **+31.067** | **6.72e-212** | *** |
| Education: graduate level (vs college) | -0.8962 | 0.4760 | ±0.9520 | -1.883 | 0.0597 | . |
| Education: high school or below (vs college) | -0.1791 | 0.9300 | ±1.8599 | -0.193 | 0.8473 |  |
| **Site: UCSD (vs UAB)** | **-1.9653** | 0.6221 | ±1.2441 | **-3.159** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3260** | 0.5514 | ±1.1029 | **-4.218** | **2.47e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.029** | **1.65e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0395 | ±0.0789 | **+6.454** | **1.09e-10** | *** |
| Hypertension | +0.5135 | 0.5153 | ±1.0305 | +0.997 | 0.3190 |  |
| High cholesterol | -0.3455 | 0.4659 | ±0.9318 | -0.742 | 0.4584 |  |
| Kidney disease | +0.8192 | 1.0339 | ±2.0678 | +0.792 | 0.4282 |  |
| Circulatory disease | +0.3881 | 0.6887 | ±1.3773 | +0.563 | 0.5731 |  |
| Time 54-69, pooled (%) | +0.0036 | 0.1461 | ±0.2922 | +0.025 | 0.9803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1128**, R² = **0.1380**, Adj R² = **0.1295**, F-statistic = **16.25** (p = **6.40e-30**), Residual SE = **7.418** on **1116** df, AIC = **7734.0**, BIC = **7794.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6051** | 2.0120 | ±4.0240 | **+31.116** | **1.48e-212** | *** |
| Education: graduate level (vs college) | -0.8958 | 0.4765 | ±0.9529 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | -0.1783 | 0.9308 | ±1.8616 | -0.192 | 0.8481 |  |
| **Site: UCSD (vs UAB)** | **-1.9650** | 0.6209 | ±1.2419 | **-3.165** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3253** | 0.5511 | ±1.1021 | **-4.220** | **2.45e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.033** | **1.61e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0395 | ±0.0789 | **+6.454** | **1.09e-10** | *** |
| Hypertension | +0.5138 | 0.5155 | ±1.0311 | +0.997 | 0.3190 |  |
| High cholesterol | -0.3452 | 0.4659 | ±0.9317 | -0.741 | 0.4587 |  |
| Kidney disease | +0.8193 | 1.0338 | ±2.0676 | +0.793 | 0.4281 |  |
| Circulatory disease | +0.3881 | 0.6886 | ±1.3773 | +0.564 | 0.5730 |  |
| Avg. daily time 54-69 (%) | +0.0054 | 0.1491 | ±0.2983 | +0.036 | 0.9711 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1128**, R² = **0.1381**, Adj R² = **0.1296**, F-statistic = **16.25** (p = **6.19e-30**), Residual SE = **7.418** on **1116** df, AIC = **7733.9**, BIC = **7794.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5540** | 2.0172 | ±4.0344 | **+31.011** | **3.89e-211** | *** |
| Education: graduate level (vs college) | -0.8911 | 0.4757 | ±0.9514 | -1.873 | 0.0610 | . |
| Education: high school or below (vs college) | -0.1655 | 0.9300 | ±1.8600 | -0.178 | 0.8588 |  |
| **Site: UCSD (vs UAB)** | **-1.9491** | 0.6236 | ±1.2472 | **-3.126** | **0.0018** | ** |
| **Site: UW (vs UAB)** | **-2.3110** | 0.5523 | ±1.1045 | **-4.184** | **2.86e-05** | *** |
| **Age (years)** | **-0.1301** | 0.0216 | ±0.0432 | **-6.020** | **1.75e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0394 | ±0.0789 | **+6.457** | **1.07e-10** | *** |
| Hypertension | +0.5184 | 0.5153 | ±1.0307 | +1.006 | 0.3144 |  |
| High cholesterol | -0.3371 | 0.4662 | ±0.9323 | -0.723 | 0.4697 |  |
| Kidney disease | +0.8181 | 1.0343 | ±2.0685 | +0.791 | 0.4289 |  |
| Circulatory disease | +0.3880 | 0.6888 | ±1.3776 | +0.563 | 0.5732 |  |
| Time < 70 (%) | +0.0326 | 0.1075 | ±0.2149 | +0.304 | 0.7614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1128**, R² = **0.1381**, Adj R² = **0.1296**, F-statistic = **16.25** (p = **6.32e-30**), Residual SE = **7.418** on **1116** df, AIC = **7733.9**, BIC = **7794.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5815** | 2.0127 | ±4.0254 | **+31.093** | **3.00e-212** | *** |
| Education: graduate level (vs college) | -0.8925 | 0.4762 | ±0.9525 | -1.874 | 0.0609 | . |
| Education: high school or below (vs college) | -0.1703 | 0.9308 | ±1.8617 | -0.183 | 0.8548 |  |
| **Site: UCSD (vs UAB)** | **-1.9576** | 0.6219 | ±1.2437 | **-3.148** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3169** | 0.5519 | ±1.1037 | **-4.198** | **2.69e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.032** | **1.62e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0394 | ±0.0789 | **+6.455** | **1.08e-10** | *** |
| Hypertension | +0.5170 | 0.5157 | ±1.0314 | +1.003 | 0.3161 |  |
| High cholesterol | -0.3409 | 0.4662 | ±0.9323 | -0.731 | 0.4645 |  |
| Kidney disease | +0.8191 | 1.0340 | ±2.0679 | +0.792 | 0.4282 |  |
| Circulatory disease | +0.3886 | 0.6887 | ±1.3775 | +0.564 | 0.5726 |  |
| Avg. daily time < 70 (%) | +0.0219 | 0.1197 | ±0.2394 | +0.183 | 0.8551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1421**, Adj R² = **0.1337**, F-statistic = **16.81** (p = **5.14e-31**), Residual SE = **7.401** on **1116** df, AIC = **7728.6**, BIC = **7788.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8098** | 7.2491 | ±14.4981 | **+10.182** | **2.39e-24** | *** |
| Education: graduate level (vs college) | -0.8927 | 0.4748 | ±0.9496 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | -0.2564 | 0.9158 | ±1.8316 | -0.280 | 0.7795 |  |
| **Site: UCSD (vs UAB)** | **-1.9515** | 0.6207 | ±1.2414 | **-3.144** | **0.0017** | ** |
| **Site: UW (vs UAB)** | **-2.3168** | 0.5457 | ±1.0914 | **-4.246** | **2.18e-05** | *** |
| **Age (years)** | **-0.1291** | 0.0216 | ±0.0431 | **-5.990** | **2.10e-09** | *** |
| **BMI (kg/m2)** | **+0.2544** | 0.0395 | ±0.0790 | **+6.439** | **1.20e-10** | *** |
| Hypertension | +0.5217 | 0.5153 | ±1.0305 | +1.013 | 0.3113 |  |
| High cholesterol | -0.3522 | 0.4650 | ±0.9301 | -0.757 | 0.4488 |  |
| Kidney disease | +0.7736 | 1.0361 | ±2.0722 | +0.747 | 0.4553 |  |
| Circulatory disease | +0.3246 | 0.6783 | ±1.3566 | +0.479 | 0.6322 |  |
| Time 54-250, pooled (%) | -0.1133 | 0.0704 | ±0.1407 | -1.610 | 0.1073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1420**, Adj R² = **0.1335**, F-statistic = **16.79** (p = **5.60e-31**), Residual SE = **7.401** on **1116** df, AIC = **7728.8**, BIC = **7789.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.0715** | 7.7352 | ±15.4704 | **+9.576** | **1.01e-21** | *** |
| Education: graduate level (vs college) | -0.8927 | 0.4750 | ±0.9499 | -1.879 | 0.0602 | . |
| Education: high school or below (vs college) | -0.2565 | 0.9160 | ±1.8320 | -0.280 | 0.7795 |  |
| **Site: UCSD (vs UAB)** | **-1.9585** | 0.6206 | ±1.2411 | **-3.156** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3220** | 0.5458 | ±1.0916 | **-4.254** | **2.10e-05** | *** |
| **Age (years)** | **-0.1293** | 0.0216 | ±0.0431 | **-5.997** | **2.00e-09** | *** |
| **BMI (kg/m2)** | **+0.2540** | 0.0395 | ±0.0790 | **+6.432** | **1.26e-10** | *** |
| Hypertension | +0.5227 | 0.5154 | ±1.0308 | +1.014 | 0.3105 |  |
| High cholesterol | -0.3551 | 0.4652 | ±0.9305 | -0.763 | 0.4453 |  |
| Kidney disease | +0.7776 | 1.0361 | ±2.0721 | +0.751 | 0.4529 |  |
| Circulatory disease | +0.3272 | 0.6783 | ±1.3566 | +0.482 | 0.6296 |  |
| Avg. daily time 54-250 (%) | -0.1156 | 0.0752 | ±0.1503 | -1.537 | 0.1242 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1128**, R² = **0.1447**, Adj R² = **0.1363**, F-statistic = **17.17** (p = **1.02e-31**), Residual SE = **7.389** on **1116** df, AIC = **7725.2**, BIC = **7785.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5750** | 1.9719 | ±3.9437 | **+31.734** | **5.29e-221** | *** |
| **Education: graduate level (vs college)** | **-0.9463** | 0.4720 | ±0.9439 | **-2.005** | **0.0450** | * |
| Education: high school or below (vs college) | -0.2019 | 0.9212 | ±1.8424 | -0.219 | 0.8265 |  |
| **Site: UCSD (vs UAB)** | **-1.9555** | 0.6168 | ±1.2336 | **-3.171** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.4100** | 0.5476 | ±1.0952 | **-4.401** | **1.08e-05** | *** |
| **Age (years)** | **-0.1314** | 0.0214 | ±0.0428 | **-6.140** | **8.26e-10** | *** |
| **BMI (kg/m2)** | **+0.2518** | 0.0393 | ±0.0787 | **+6.399** | **1.56e-10** | *** |
| Hypertension | +0.3836 | 0.5156 | ±1.0311 | +0.744 | 0.4568 |  |
| High cholesterol | -0.4623 | 0.4602 | ±0.9205 | -1.004 | 0.3152 |  |
| Kidney disease | +0.6086 | 1.0166 | ±2.0332 | +0.599 | 0.5494 |  |
| Circulatory disease | +0.3560 | 0.6779 | ±1.3558 | +0.525 | 0.5995 |  |
| **Time 181-250, pooled (%)** | **+0.1104** | 0.0449 | ±0.0899 | **+2.457** | **0.0140** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1446**, Adj R² = **0.1361**, F-statistic = **17.15** (p = **1.12e-31**), Residual SE = **7.390** on **1116** df, AIC = **7725.4**, BIC = **7785.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5860** | 1.9709 | ±3.9418 | **+31.755** | **2.70e-221** | *** |
| **Education: graduate level (vs college)** | **-0.9484** | 0.4722 | ±0.9443 | **-2.009** | **0.0446** | * |
| Education: high school or below (vs college) | -0.1927 | 0.9205 | ±1.8410 | -0.209 | 0.8342 |  |
| **Site: UCSD (vs UAB)** | **-1.9458** | 0.6168 | ±1.2337 | **-3.154** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.4009** | 0.5472 | ±1.0944 | **-4.388** | **1.15e-05** | *** |
| **Age (years)** | **-0.1312** | 0.0214 | ±0.0428 | **-6.134** | **8.56e-10** | *** |
| **BMI (kg/m2)** | **+0.2514** | 0.0393 | ±0.0786 | **+6.400** | **1.56e-10** | *** |
| Hypertension | +0.3851 | 0.5156 | ±1.0312 | +0.747 | 0.4552 |  |
| High cholesterol | -0.4626 | 0.4602 | ±0.9204 | -1.005 | 0.3148 |  |
| Kidney disease | +0.6105 | 1.0169 | ±2.0338 | +0.600 | 0.5483 |  |
| Circulatory disease | +0.3521 | 0.6781 | ±1.3562 | +0.519 | 0.6036 |  |
| **Avg. daily time 181-250 (%)** | **+0.1079** | 0.0449 | ±0.0898 | **+2.404** | **0.0162** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1128**, R² = **0.1460**, Adj R² = **0.1376**, F-statistic = **17.35** (p = **4.59e-32**), Residual SE = **7.384** on **1116** df, AIC = **7723.5**, BIC = **7783.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5237** | 1.9770 | ±3.9539 | **+31.626** | **1.62e-219** | *** |
| **Education: graduate level (vs college)** | **-0.9333** | 0.4721 | ±0.9442 | **-1.977** | **0.0480** | * |
| Education: high school or below (vs college) | -0.2609 | 0.9115 | ±1.8229 | -0.286 | 0.7747 |  |
| **Site: UCSD (vs UAB)** | **-1.9635** | 0.6177 | ±1.2354 | **-3.179** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3948** | 0.5450 | ±1.0900 | **-4.394** | **1.11e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0214 | ±0.0428 | **-6.093** | **1.11e-09** | *** |
| **BMI (kg/m2)** | **+0.2521** | 0.0394 | ±0.0788 | **+6.398** | **1.57e-10** | *** |
| Hypertension | +0.4176 | 0.5145 | ±1.0290 | +0.812 | 0.4170 |  |
| High cholesterol | -0.4463 | 0.4624 | ±0.9247 | -0.965 | 0.3344 |  |
| Kidney disease | +0.6292 | 1.0240 | ±2.0480 | +0.614 | 0.5389 |  |
| Circulatory disease | +0.3168 | 0.6718 | ±1.3436 | +0.472 | 0.6373 |  |
| **Time > 180 (%)** | **+0.0839** | 0.0351 | ±0.0701 | **+2.392** | **0.0168** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1128**, R² = **0.1458**, Adj R² = **0.1374**, F-statistic = **17.31** (p = **5.29e-32**), Residual SE = **7.385** on **1116** df, AIC = **7723.8**, BIC = **7784.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5430** | 1.9761 | ±3.9522 | **+31.650** | **7.63e-220** | *** |
| **Education: graduate level (vs college)** | **-0.9354** | 0.4722 | ±0.9444 | **-1.981** | **0.0476** | * |
| Education: high school or below (vs college) | -0.2498 | 0.9116 | ±1.8233 | -0.274 | 0.7840 |  |
| **Site: UCSD (vs UAB)** | **-1.9557** | 0.6178 | ±1.2357 | **-3.165** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3899** | 0.5450 | ±1.0900 | **-4.385** | **1.16e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0214 | ±0.0428 | **-6.090** | **1.13e-09** | *** |
| **BMI (kg/m2)** | **+0.2517** | 0.0394 | ±0.0787 | **+6.394** | **1.61e-10** | *** |
| Hypertension | +0.4184 | 0.5146 | ±1.0292 | +0.813 | 0.4161 |  |
| High cholesterol | -0.4467 | 0.4624 | ±0.9249 | -0.966 | 0.3340 |  |
| Kidney disease | +0.6325 | 1.0241 | ±2.0481 | +0.618 | 0.5368 |  |
| Circulatory disease | +0.3162 | 0.6722 | ±1.3444 | +0.470 | 0.6381 |  |
| **Avg. daily time > 180 (%)** | **+0.0824** | 0.0350 | ±0.0700 | **+2.357** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1128**, R² = **0.1396**, Adj R² = **0.1312**, F-statistic = **16.47** (p = **2.39e-30**), Residual SE = **7.411** on **1116** df, AIC = **7731.9**, BIC = **7792.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6375** | 1.9971 | ±3.9942 | **+31.364** | **6.29e-216** | *** |
| Education: graduate level (vs college) | -0.8910 | 0.4741 | ±0.9482 | -1.880 | 0.0602 | . |
| Education: high school or below (vs college) | -0.2048 | 0.9219 | ±1.8438 | -0.222 | 0.8242 |  |
| **Site: UCSD (vs UAB)** | **-1.9658** | 0.6197 | ±1.2394 | **-3.172** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3483** | 0.5478 | ±1.0957 | **-4.287** | **1.81e-05** | *** |
| **Age (years)** | **-0.1295** | 0.0215 | ±0.0430 | **-6.014** | **1.81e-09** | *** |
| **BMI (kg/m2)** | **+0.2505** | 0.0399 | ±0.0797 | **+6.285** | **3.28e-10** | *** |
| Hypertension | +0.4935 | 0.5160 | ±1.0321 | +0.956 | 0.3389 |  |
| High cholesterol | -0.4036 | 0.4664 | ±0.9327 | -0.865 | 0.3868 |  |
| Kidney disease | +0.8078 | 1.0340 | ±2.0680 | +0.781 | 0.4346 |  |
| Circulatory disease | +0.3812 | 0.6845 | ±1.3690 | +0.557 | 0.5776 |  |
| Nocturnal time > 180 (%) | +0.0398 | 0.0388 | ±0.0776 | +1.027 | 0.3045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1398**, Adj R² = **0.1313**, F-statistic = **16.48** (p = **2.22e-30**), Residual SE = **7.411** on **1116** df, AIC = **7731.7**, BIC = **7792.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3709** | 2.0047 | ±4.0094 | **+31.112** | **1.64e-212** | *** |
| Education: graduate level (vs college) | -0.8998 | 0.4741 | ±0.9481 | -1.898 | 0.0577 | . |
| Education: high school or below (vs college) | -0.1852 | 0.9220 | ±1.8440 | -0.201 | 0.8408 |  |
| **Site: UCSD (vs UAB)** | **-1.9697** | 0.6185 | ±1.2370 | **-3.185** | **0.0014** | ** |
| **Site: UW (vs UAB)** | **-2.3454** | 0.5488 | ±1.0976 | **-4.274** | **1.92e-05** | *** |
| **Age (years)** | **-0.1304** | 0.0216 | ±0.0432 | **-6.045** | **1.50e-09** | *** |
| **BMI (kg/m2)** | **+0.2590** | 0.0397 | ±0.0795 | **+6.517** | **7.19e-11** | *** |
| Hypertension | +0.4623 | 0.5161 | ±1.0321 | +0.896 | 0.3704 |  |
| High cholesterol | -0.3784 | 0.4643 | ±0.9287 | -0.815 | 0.4151 |  |
| Kidney disease | +0.7964 | 1.0314 | ±2.0628 | +0.772 | 0.4400 |  |
| Circulatory disease | +0.4013 | 0.6834 | ±1.3669 | +0.587 | 0.5571 |  |
| Any reading > 250 during wear (0/1) | +0.8428 | 0.5614 | ±1.1227 | +1.501 | 0.1333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1128**, R² = **0.1418**, Adj R² = **0.1334**, F-statistic = **16.77** (p = **6.17e-31**), Residual SE = **7.402** on **1116** df, AIC = **7729.0**, BIC = **7789.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5325** | 1.9997 | ±3.9994 | **+31.271** | **1.15e-214** | *** |
| Education: graduate level (vs college) | -0.8953 | 0.4749 | ±0.9497 | -1.885 | 0.0594 | . |
| Education: high school or below (vs college) | -0.2645 | 0.9175 | ±1.8349 | -0.288 | 0.7731 |  |
| **Site: UCSD (vs UAB)** | **-1.9735** | 0.6199 | ±1.2399 | **-3.183** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3333** | 0.5457 | ±1.0914 | **-4.276** | **1.90e-05** | *** |
| **Age (years)** | **-0.1292** | 0.0216 | ±0.0431 | **-5.997** | **2.01e-09** | *** |
| **BMI (kg/m2)** | **+0.2542** | 0.0395 | ±0.0790 | **+6.436** | **1.23e-10** | *** |
| Hypertension | +0.5167 | 0.5152 | ±1.0303 | +1.003 | 0.3158 |  |
| High cholesterol | -0.3618 | 0.4654 | ±0.9308 | -0.777 | 0.4369 |  |
| Kidney disease | +0.7798 | 1.0358 | ±2.0717 | +0.753 | 0.4515 |  |
| Circulatory disease | +0.3266 | 0.6786 | ±1.3573 | +0.481 | 0.6304 |  |
| Time > 250 (%) | +0.1099 | 0.0729 | ±0.1459 | +1.507 | 0.1317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1418**, Adj R² = **0.1334**, F-statistic = **16.77** (p = **6.18e-31**), Residual SE = **7.402** on **1116** df, AIC = **7729.0**, BIC = **7789.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5437** | 1.9995 | ±3.9990 | **+31.280** | **8.82e-215** | *** |
| Education: graduate level (vs college) | -0.8955 | 0.4749 | ±0.9498 | -1.886 | 0.0593 | . |
| Education: high school or below (vs college) | -0.2632 | 0.9175 | ±1.8350 | -0.287 | 0.7742 |  |
| **Site: UCSD (vs UAB)** | **-1.9734** | 0.6200 | ±1.2400 | **-3.183** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3359** | 0.5458 | ±1.0915 | **-4.280** | **1.87e-05** | *** |
| **Age (years)** | **-0.1293** | 0.0216 | ±0.0431 | **-5.997** | **2.01e-09** | *** |
| **BMI (kg/m2)** | **+0.2539** | 0.0395 | ±0.0790 | **+6.430** | **1.28e-10** | *** |
| Hypertension | +0.5175 | 0.5153 | ±1.0306 | +1.004 | 0.3153 |  |
| High cholesterol | -0.3621 | 0.4655 | ±0.9310 | -0.778 | 0.4366 |  |
| Kidney disease | +0.7816 | 1.0359 | ±2.0718 | +0.755 | 0.4505 |  |
| Circulatory disease | +0.3268 | 0.6785 | ±1.3570 | +0.482 | 0.6300 |  |
| Avg. daily time > 250 (%) | +0.1137 | 0.0767 | ±0.1534 | +1.483 | 0.1381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 1,137; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0214**, F-statistic = **3.48** (p = **1.57e-04**), Residual SE = **65.505** on **1126** df, AIC = **12747.8**, BIC = **12803.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.1684** | 16.4040 | ±32.8079 | **+24.638** | **4.89e-134** | *** |
| Education: graduate level (vs college) | +0.6486 | 4.0966 | ±8.1931 | +0.158 | 0.8742 |  |
| Education: high school or below (vs college) | -15.7250 | 8.7895 | ±17.5789 | -1.789 | 0.0736 | . |
| Site: UCSD (vs UAB) | -6.2682 | 5.4287 | ±10.8574 | -1.155 | 0.2482 |  |
| Site: UW (vs UAB) | -1.3074 | 4.7771 | ±9.5542 | -0.274 | 0.7843 |  |
| Age (years) | -0.0578 | 0.1879 | ±0.3758 | -0.307 | 0.7585 |  |
| **BMI (kg/m2)** | **-0.9238** | 0.3274 | ±0.6549 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.6117 | 4.4007 | ±8.8014 | -1.730 | 0.0837 | . |
| High cholesterol | -2.5058 | 4.0275 | ±8.0550 | -0.622 | 0.5338 |  |
| Kidney disease | -18.6810 | 10.5899 | ±21.1797 | -1.764 | 0.0777 | . |
| Circulatory disease | +13.1569 | 6.9529 | ±13.9058 | +1.892 | 0.0585 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1137**, R² = **0.0334**, Adj R² = **0.0240**, F-statistic = **3.54** (p = **6.74e-05**), Residual SE = **65.418** on **1125** df, AIC = **12745.7**, BIC = **12806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+443.0237** | 25.0012 | ±50.0024 | **+17.720** | **2.93e-70** | *** |
| Education: graduate level (vs college) | +0.5503 | 4.0897 | ±8.1795 | +0.135 | 0.8930 |  |
| Education: high school or below (vs college) | -14.8085 | 8.8127 | ±17.6254 | -1.680 | 0.0929 | . |
| Site: UCSD (vs UAB) | -6.1220 | 5.4198 | ±10.8395 | -1.130 | 0.2587 |  |
| Site: UW (vs UAB) | -0.9734 | 4.7742 | ±9.5483 | -0.204 | 0.8384 |  |
| Age (years) | -0.0229 | 0.1893 | ±0.3786 | -0.121 | 0.9039 |  |
| **BMI (kg/m2)** | **-0.8745** | 0.3274 | ±0.6547 | **-2.671** | **0.0076** | ** |
| Hypertension | -7.3771 | 4.3900 | ±8.7800 | -1.680 | 0.0929 | . |
| High cholesterol | -1.3317 | 4.0806 | ±8.1613 | -0.326 | 0.7442 |  |
| Kidney disease | -18.4698 | 10.5454 | ±21.0907 | -1.751 | 0.0799 | . |
| Circulatory disease | +13.6068 | 6.9872 | ±13.9743 | +1.947 | 0.0515 | . |
| **HbA1c (%)** | **-7.6546** | 3.6342 | ±7.2684 | **-2.106** | **0.0352** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **2.99e-04**), Residual SE = **65.531** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.8771** | 19.7053 | ±39.4106 | **+20.699** | **3.55e-95** | *** |
| Education: graduate level (vs college) | +0.7053 | 4.1194 | ±8.2388 | +0.171 | 0.8641 |  |
| Education: high school or below (vs college) | -15.5941 | 8.8359 | ±17.6718 | -1.765 | 0.0776 | . |
| Site: UCSD (vs UAB) | -6.2687 | 5.4332 | ±10.8664 | -1.154 | 0.2486 |  |
| Site: UW (vs UAB) | -1.1882 | 4.8206 | ±9.6412 | -0.246 | 0.8053 |  |
| Age (years) | -0.0556 | 0.1883 | ±0.3767 | -0.295 | 0.7678 |  |
| **BMI (kg/m2)** | **-0.9196** | 0.3283 | ±0.6565 | **-2.801** | **0.0051** | ** |
| Hypertension | -7.5167 | 4.3970 | ±8.7941 | -1.709 | 0.0874 | . |
| High cholesterol | -2.3831 | 4.0483 | ±8.0966 | -0.589 | 0.5561 |  |
| Kidney disease | -18.5231 | 10.6118 | ±21.2237 | -1.746 | 0.0809 | . |
| Circulatory disease | +13.2069 | 6.9750 | ±13.9499 | +1.893 | 0.0583 | . |
| Mean glucose (mg/dL) | -0.0344 | 0.1071 | ±0.2143 | -0.321 | 0.7483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **2.99e-04**), Residual SE = **65.531** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.6348** | 30.5247 | ±61.0494 | **+13.518** | **1.22e-41** | *** |
| Education: graduate level (vs college) | +0.7053 | 4.1194 | ±8.2388 | +0.171 | 0.8641 |  |
| Education: high school or below (vs college) | -15.5941 | 8.8359 | ±17.6718 | -1.765 | 0.0776 | . |
| Site: UCSD (vs UAB) | -6.2687 | 5.4332 | ±10.8664 | -1.154 | 0.2486 |  |
| Site: UW (vs UAB) | -1.1882 | 4.8206 | ±9.6412 | -0.246 | 0.8053 |  |
| Age (years) | -0.0556 | 0.1883 | ±0.3767 | -0.295 | 0.7678 |  |
| **BMI (kg/m2)** | **-0.9196** | 0.3283 | ±0.6565 | **-2.801** | **0.0051** | ** |
| Hypertension | -7.5167 | 4.3970 | ±8.7941 | -1.709 | 0.0874 | . |
| High cholesterol | -2.3831 | 4.0483 | ±8.0966 | -0.589 | 0.5561 |  |
| Kidney disease | -18.5231 | 10.6118 | ±21.2237 | -1.746 | 0.0809 | . |
| Circulatory disease | +13.2069 | 6.9750 | ±13.9499 | +1.893 | 0.0583 | . |
| GMI (%) | -1.4374 | 4.4789 | ±8.9578 | -0.321 | 0.7483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1137**, R² = **0.0308**, Adj R² = **0.0213**, F-statistic = **3.25** (p = **2.16e-04**), Residual SE = **65.506** on **1125** df, AIC = **12748.8**, BIC = **12809.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+415.0928** | 19.4244 | ±38.8488 | **+21.370** | **2.56e-101** | *** |
| Education: graduate level (vs college) | +0.7410 | 4.1007 | ±8.2014 | +0.181 | 0.8566 |  |
| Education: high school or below (vs college) | -15.3077 | 8.8402 | ±17.6805 | -1.732 | 0.0833 | . |
| Site: UCSD (vs UAB) | -6.1568 | 5.4301 | ±10.8601 | -1.134 | 0.2569 |  |
| Site: UW (vs UAB) | -0.9679 | 4.8119 | ±9.6239 | -0.201 | 0.8406 |  |
| Age (years) | -0.0610 | 0.1882 | ±0.3763 | -0.324 | 0.7459 |  |
| **BMI (kg/m2)** | **-0.8849** | 0.3287 | ±0.6575 | **-2.692** | **0.0071** | ** |
| Hypertension | -7.3879 | 4.4058 | ±8.8116 | -1.677 | 0.0936 | . |
| High cholesterol | -2.0390 | 4.0551 | ±8.1102 | -0.503 | 0.6151 |  |
| Kidney disease | -18.5058 | 10.5784 | ±21.1569 | -1.749 | 0.0802 | . |
| Circulatory disease | +13.2147 | 6.9716 | ±13.9431 | +1.896 | 0.0580 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.1038 | 0.0998 | ±0.1995 | -1.040 | 0.2982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.20** (p = **2.72e-04**), Residual SE = **65.523** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.7394** | 17.1091 | ±34.2183 | **+23.832** | **1.57e-125** | *** |
| Education: graduate level (vs college) | +0.6672 | 4.1035 | ±8.2071 | +0.163 | 0.8708 |  |
| Education: high school or below (vs college) | -15.6686 | 8.8044 | ±17.6087 | -1.780 | 0.0751 | . |
| Site: UCSD (vs UAB) | -6.4091 | 5.4539 | ±10.9079 | -1.175 | 0.2399 |  |
| Site: UW (vs UAB) | -1.1991 | 4.7881 | ±9.5762 | -0.250 | 0.8023 |  |
| Age (years) | -0.0517 | 0.1890 | ±0.3780 | -0.273 | 0.7845 |  |
| **BMI (kg/m2)** | **-0.9279** | 0.3274 | ±0.6547 | **-2.834** | **0.0046** | ** |
| Hypertension | -7.4126 | 4.3898 | ±8.7797 | -1.689 | 0.0913 | . |
| High cholesterol | -2.4088 | 4.0334 | ±8.0667 | -0.597 | 0.5504 |  |
| Kidney disease | -18.1948 | 10.6208 | ±21.2416 | -1.713 | 0.0867 | . |
| Circulatory disease | +13.2524 | 6.9651 | ±13.9302 | +1.903 | 0.0571 | . |
| Glucose SD, pooled (mg/dL) | -0.1852 | 0.3136 | ±0.6272 | -0.591 | 0.5548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1137**, R² = **0.0304**, Adj R² = **0.0209**, F-statistic = **3.20** (p = **2.65e-04**), Residual SE = **65.522** on **1125** df, AIC = **12749.3**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.6832** | 16.8667 | ±33.7334 | **+24.171** | **4.51e-129** | *** |
| Education: graduate level (vs college) | +0.6888 | 4.1082 | ±8.2164 | +0.168 | 0.8668 |  |
| Education: high school or below (vs college) | -15.6328 | 8.8105 | ±17.6210 | -1.774 | 0.0760 | . |
| Site: UCSD (vs UAB) | -6.3939 | 5.4550 | ±10.9099 | -1.172 | 0.2411 |  |
| Site: UW (vs UAB) | -1.1631 | 4.7910 | ±9.5821 | -0.243 | 0.8082 |  |
| Age (years) | -0.0495 | 0.1894 | ±0.3787 | -0.262 | 0.7937 |  |
| **BMI (kg/m2)** | **-0.9253** | 0.3274 | ±0.6548 | **-2.826** | **0.0047** | ** |
| Hypertension | -7.4023 | 4.3888 | ±8.7775 | -1.687 | 0.0917 | . |
| High cholesterol | -2.3953 | 4.0345 | ±8.0691 | -0.594 | 0.5527 |  |
| Kidney disease | -18.1511 | 10.6407 | ±21.2813 | -1.706 | 0.0880 | . |
| Circulatory disease | +13.2640 | 6.9684 | ±13.9368 | +1.903 | 0.0570 | . |
| Avg. daily SD (mg/dL) | -0.2134 | 0.3333 | ±0.6666 | -0.640 | 0.5219 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.19** (p = **2.76e-04**), Residual SE = **65.525** on **1125** df, AIC = **12749.4**, BIC = **12809.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+409.0816** | 18.0731 | ±36.1462 | **+22.635** | **1.97e-113** | *** |
| Education: graduate level (vs college) | +0.5943 | 4.0947 | ±8.1893 | +0.145 | 0.8846 |  |
| Education: high school or below (vs college) | -15.8043 | 8.7820 | ±17.5641 | -1.800 | 0.0719 | . |
| Site: UCSD (vs UAB) | -6.4563 | 5.4666 | ±10.9332 | -1.181 | 0.2376 |  |
| Site: UW (vs UAB) | -1.3320 | 4.7827 | ±9.5655 | -0.279 | 0.7806 |  |
| Age (years) | -0.0523 | 0.1889 | ±0.3778 | -0.277 | 0.7820 |  |
| **BMI (kg/m2)** | **-0.9335** | 0.3274 | ±0.6548 | **-2.851** | **0.0044** | ** |
| Hypertension | -7.4963 | 4.3934 | ±8.7868 | -1.706 | 0.0880 | . |
| High cholesterol | -2.5489 | 4.0334 | ±8.0669 | -0.632 | 0.5274 |  |
| Kidney disease | -18.3140 | 10.6110 | ±21.2220 | -1.726 | 0.0844 | . |
| Circulatory disease | +13.1972 | 6.9585 | ±13.9170 | +1.897 | 0.0579 | . |
| CV (%) | -0.2765 | 0.4802 | ±0.9604 | -0.576 | 0.5647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **2.97e-04**), Residual SE = **65.530** on **1125** df, AIC = **12749.6**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.8681** | 19.3354 | ±38.6708 | **+20.732** | **1.77e-95** | *** |
| Education: graduate level (vs college) | +0.6118 | 4.0942 | ±8.1884 | +0.149 | 0.8812 |  |
| Education: high school or below (vs college) | -15.7300 | 8.7903 | ±17.5805 | -1.789 | 0.0735 | . |
| Site: UCSD (vs UAB) | -6.3813 | 5.4577 | ±10.9155 | -1.169 | 0.2423 |  |
| Site: UW (vs UAB) | -1.2972 | 4.7804 | ±9.5607 | -0.271 | 0.7861 |  |
| Age (years) | -0.0543 | 0.1890 | ±0.3780 | -0.287 | 0.7739 |  |
| **BMI (kg/m2)** | **-0.9289** | 0.3277 | ±0.6555 | **-2.834** | **0.0046** | ** |
| Hypertension | -7.5349 | 4.3977 | ±8.7953 | -1.713 | 0.0866 | . |
| High cholesterol | -2.5132 | 4.0312 | ±8.0625 | -0.623 | 0.5330 |  |
| Kidney disease | -18.5181 | 10.5943 | ±21.1887 | -1.748 | 0.0805 | . |
| Circulatory disease | +13.1762 | 6.9550 | ±13.9101 | +1.894 | 0.0582 | . |
| Mean / SD ratio | +0.5526 | 1.5517 | ±3.1034 | +0.356 | 0.7217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1137**, R² = **0.0305**, Adj R² = **0.0211**, F-statistic = **3.22** (p = **2.46e-04**), Residual SE = **65.516** on **1125** df, AIC = **12749.1**, BIC = **12809.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.4354** | 19.6561 | ±39.3122 | **+20.169** | **1.85e-90** | *** |
| Education: graduate level (vs college) | +0.6295 | 4.0995 | ±8.1990 | +0.154 | 0.8780 |  |
| Education: high school or below (vs college) | -15.6313 | 8.7936 | ±17.5871 | -1.778 | 0.0755 | . |
| Site: UCSD (vs UAB) | -6.4709 | 5.4642 | ±10.9284 | -1.184 | 0.2363 |  |
| Site: UW (vs UAB) | -1.2417 | 4.7802 | ±9.5604 | -0.260 | 0.7950 |  |
| Age (years) | -0.0465 | 0.1896 | ±0.3792 | -0.245 | 0.8062 |  |
| **BMI (kg/m2)** | **-0.9288** | 0.3273 | ±0.6546 | **-2.838** | **0.0045** | ** |
| Hypertension | -7.4994 | 4.3970 | ±8.7939 | -1.706 | 0.0881 | . |
| High cholesterol | -2.5068 | 4.0319 | ±8.0638 | -0.622 | 0.5341 |  |
| Kidney disease | -18.2165 | 10.6274 | ±21.2549 | -1.714 | 0.0865 | . |
| Circulatory disease | +13.2047 | 6.9615 | ±13.9230 | +1.897 | 0.0579 | . |
| Avg. daily mean/SD | +1.0618 | 1.3161 | ±2.6322 | +0.807 | 0.4198 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1137**, R² = **0.0455**, Adj R² = **0.0361**, F-statistic = **4.87** (p = **2.16e-07**), Residual SE = **65.009** on **1125** df, AIC = **12731.5**, BIC = **12791.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+448.3426** | 18.5820 | ±37.1640 | **+24.128** | **1.28e-128** | *** |
| Education: graduate level (vs college) | +0.4202 | 4.0747 | ±8.1494 | +0.103 | 0.9179 |  |
| Education: high school or below (vs college) | -14.7301 | 8.6353 | ±17.2707 | -1.706 | 0.0880 | . |
| Site: UCSD (vs UAB) | -7.3409 | 5.4441 | ±10.8883 | -1.348 | 0.1775 |  |
| Site: UW (vs UAB) | -2.5141 | 4.7531 | ±9.5063 | -0.529 | 0.5968 |  |
| Age (years) | -0.0854 | 0.1864 | ±0.3728 | -0.458 | 0.6470 |  |
| **BMI (kg/m2)** | **-0.9437** | 0.3197 | ±0.6394 | **-2.952** | **0.0032** | ** |
| Hypertension | -7.8758 | 4.3711 | ±8.7421 | -1.802 | 0.0716 | . |
| High cholesterol | -2.9081 | 3.9994 | ±7.9988 | -0.727 | 0.4672 |  |
| Kidney disease | -17.1316 | 10.5369 | ±21.0738 | -1.626 | 0.1040 |  |
| Circulatory disease | +12.5144 | 6.9195 | ±13.8391 | +1.809 | 0.0705 | . |
| **MAG (mg/dL/h)** | **-1.0731** | 0.2601 | ±0.5203 | **-4.125** | **3.70e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1137**, R² = **0.0305**, Adj R² = **0.0210**, F-statistic = **3.22** (p = **2.49e-04**), Residual SE = **65.517** on **1125** df, AIC = **12749.2**, BIC = **12809.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+409.7936** | 17.6025 | ±35.2050 | **+23.280** | **7.00e-120** | *** |
| Education: graduate level (vs college) | +0.7155 | 4.1094 | ±8.2188 | +0.174 | 0.8618 |  |
| Education: high school or below (vs college) | -15.5720 | 8.8091 | ±17.6183 | -1.768 | 0.0771 | . |
| Site: UCSD (vs UAB) | -6.4129 | 5.4570 | ±10.9141 | -1.175 | 0.2399 |  |
| Site: UW (vs UAB) | -1.2077 | 4.7846 | ±9.5693 | -0.252 | 0.8007 |  |
| Age (years) | -0.0501 | 0.1889 | ±0.3778 | -0.265 | 0.7909 |  |
| **BMI (kg/m2)** | **-0.9400** | 0.3280 | ±0.6560 | **-2.866** | **0.0042** | ** |
| Hypertension | -7.4439 | 4.3938 | ±8.7876 | -1.694 | 0.0902 | . |
| High cholesterol | -2.4609 | 4.0345 | ±8.0690 | -0.610 | 0.5419 |  |
| Kidney disease | -18.1862 | 10.6349 | ±21.2699 | -1.710 | 0.0873 | . |
| Circulatory disease | +13.2387 | 6.9676 | ±13.9351 | +1.900 | 0.0574 | . |
| Avg. daily range (mg/dL) | -0.0587 | 0.0766 | ±0.1533 | -0.766 | 0.4439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.19** (p = **2.77e-04**), Residual SE = **65.525** on **1125** df, AIC = **12749.5**, BIC = **12809.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.2835** | 16.8166 | ±33.6332 | **+24.160** | **5.91e-129** | *** |
| Education: graduate level (vs college) | +0.6604 | 4.0981 | ±8.1962 | +0.161 | 0.8720 |  |
| Education: high school or below (vs college) | -15.8003 | 8.7898 | ±17.5796 | -1.798 | 0.0722 | . |
| Site: UCSD (vs UAB) | -6.4269 | 5.4234 | ±10.8469 | -1.185 | 0.2360 |  |
| Site: UW (vs UAB) | -1.2902 | 4.7805 | ±9.5610 | -0.270 | 0.7872 |  |
| Age (years) | -0.0597 | 0.1881 | ±0.3762 | -0.317 | 0.7511 |  |
| **BMI (kg/m2)** | **-0.9162** | 0.3271 | ±0.6542 | **-2.801** | **0.0051** | ** |
| Hypertension | -7.5825 | 4.4025 | ±8.8050 | -1.722 | 0.0850 | . |
| High cholesterol | -2.3708 | 4.0236 | ±8.0472 | -0.589 | 0.5557 |  |
| Kidney disease | -18.5838 | 10.5966 | ±21.1932 | -1.754 | 0.0795 | . |
| Circulatory disease | +13.2332 | 6.9536 | ±13.9073 | +1.903 | 0.0570 | . |
| SD of daily means (mg/dL) | -0.3435 | 0.5681 | ±1.1361 | -0.605 | 0.5454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.20** (p = **2.73e-04**), Residual SE = **65.524** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+418.1650** | 30.7562 | ±61.5125 | **+13.596** | **4.22e-42** | *** |
| Education: graduate level (vs college) | +0.6392 | 4.1012 | ±8.2023 | +0.156 | 0.8762 |  |
| Education: high school or below (vs college) | -15.8219 | 8.8230 | ±17.6459 | -1.793 | 0.0729 | . |
| Site: UCSD (vs UAB) | -6.1195 | 5.4499 | ±10.8997 | -1.123 | 0.2615 |  |
| Site: UW (vs UAB) | -1.3509 | 4.7824 | ±9.5648 | -0.282 | 0.7776 |  |
| Age (years) | -0.0581 | 0.1880 | ±0.3759 | -0.309 | 0.7574 |  |
| **BMI (kg/m2)** | **-0.9267** | 0.3285 | ±0.6570 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.7013 | 4.3957 | ±8.7914 | -1.752 | 0.0798 | . |
| High cholesterol | -2.6758 | 4.0236 | ±8.0472 | -0.665 | 0.5060 |  |
| Kidney disease | -19.0530 | 10.6110 | ±21.2220 | -1.796 | 0.0726 | . |
| Circulatory disease | +13.0281 | 6.9716 | ±13.9432 | +1.869 | 0.0617 | . |
| Time in range 70-180, pooled (%) | -0.1438 | 0.2544 | ±0.5088 | -0.565 | 0.5718 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0209**, F-statistic = **3.20** (p = **2.68e-04**), Residual SE = **65.523** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+419.0122** | 30.8392 | ±61.6784 | **+13.587** | **4.78e-42** | *** |
| Education: graduate level (vs college) | +0.6367 | 4.1014 | ±8.2028 | +0.155 | 0.8766 |  |
| Education: high school or below (vs college) | -15.8104 | 8.8215 | ±17.6429 | -1.792 | 0.0731 | . |
| Site: UCSD (vs UAB) | -6.1183 | 5.4473 | ±10.8945 | -1.123 | 0.2614 |  |
| Site: UW (vs UAB) | -1.3501 | 4.7821 | ±9.5642 | -0.282 | 0.7777 |  |
| Age (years) | -0.0584 | 0.1880 | ±0.3760 | -0.311 | 0.7559 |  |
| **BMI (kg/m2)** | **-0.9278** | 0.3287 | ±0.6574 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.7034 | 4.3958 | ±8.7916 | -1.752 | 0.0797 | . |
| High cholesterol | -2.6953 | 4.0223 | ±8.0447 | -0.670 | 0.5028 |  |
| Kidney disease | -19.0703 | 10.6133 | ±21.2266 | -1.797 | 0.0724 | . |
| Circulatory disease | +13.0201 | 6.9713 | ±13.9425 | +1.868 | 0.0618 | . |
| Avg. daily time in range 70-180 (%) | -0.1516 | 0.2538 | ±0.5075 | -0.598 | 0.5501 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.17** (p = **3.06e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.7145** | 16.7357 | ±33.4714 | **+24.123** | **1.44e-128** | *** |
| Education: graduate level (vs college) | +0.6756 | 4.1145 | ±8.2290 | +0.164 | 0.8696 |  |
| Education: high school or below (vs college) | -15.6309 | 8.8444 | ±17.6888 | -1.767 | 0.0772 | . |
| Site: UCSD (vs UAB) | -6.1498 | 5.4750 | ±10.9500 | -1.123 | 0.2613 |  |
| Site: UW (vs UAB) | -1.2505 | 4.7954 | ±9.5908 | -0.261 | 0.7943 |  |
| Age (years) | -0.0554 | 0.1882 | ±0.3763 | -0.294 | 0.7685 |  |
| **BMI (kg/m2)** | **-0.9255** | 0.3271 | ±0.6543 | **-2.829** | **0.0047** | ** |
| Hypertension | -7.6181 | 4.4039 | ±8.8079 | -1.730 | 0.0837 | . |
| High cholesterol | -2.4580 | 4.0611 | ±8.1223 | -0.605 | 0.5450 |  |
| Kidney disease | -18.6762 | 10.5909 | ±21.1817 | -1.763 | 0.0778 | . |
| Circulatory disease | +13.0605 | 6.9512 | ±13.9025 | +1.879 | 0.0603 | . |
| Any reading < 54 during wear (0/1) | +0.8253 | 4.1765 | ±8.3530 | +0.198 | 0.8433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1137**, R² = **0.0305**, Adj R² = **0.0211**, F-statistic = **3.22** (p = **2.44e-04**), Residual SE = **65.515** on **1125** df, AIC = **12749.1**, BIC = **12809.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.3574** | 16.4550 | ±32.9100 | **+24.634** | **5.42e-134** | *** |
| Education: graduate level (vs college) | +0.5846 | 4.1000 | ±8.2001 | +0.143 | 0.8866 |  |
| Education: high school or below (vs college) | -15.9904 | 8.7851 | ±17.5701 | -1.820 | 0.0687 | . |
| Site: UCSD (vs UAB) | -6.7783 | 5.4708 | ±10.9416 | -1.239 | 0.2153 |  |
| Site: UW (vs UAB) | -1.7054 | 4.8139 | ±9.6278 | -0.354 | 0.7231 |  |
| Age (years) | -0.0609 | 0.1877 | ±0.3755 | -0.324 | 0.7456 |  |
| **BMI (kg/m2)** | **-0.9276** | 0.3274 | ±0.6548 | **-2.833** | **0.0046** | ** |
| Hypertension | -7.7306 | 4.4038 | ±8.8075 | -1.755 | 0.0792 | . |
| High cholesterol | -2.7301 | 4.0508 | ±8.1016 | -0.674 | 0.5003 |  |
| Kidney disease | -18.5706 | 10.6023 | ±21.2047 | -1.752 | 0.0799 | . |
| Circulatory disease | +13.1806 | 6.9492 | ±13.8984 | +1.897 | 0.0579 | . |
| Time < 54 (%) | -2.6405 | 1.9578 | ±3.9155 | -1.349 | 0.1774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1137**, R² = **0.0307**, Adj R² = **0.0212**, F-statistic = **3.24** (p = **2.27e-04**), Residual SE = **65.510** on **1125** df, AIC = **12748.9**, BIC = **12809.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.1553** | 16.4304 | ±32.8608 | **+24.659** | **2.96e-134** | *** |
| Education: graduate level (vs college) | +0.5434 | 4.1035 | ±8.2070 | +0.132 | 0.8946 |  |
| Education: high school or below (vs college) | -16.0241 | 8.7855 | ±17.5710 | -1.824 | 0.0682 | . |
| Site: UCSD (vs UAB) | -6.7727 | 5.4556 | ±10.9113 | -1.241 | 0.2145 |  |
| Site: UW (vs UAB) | -1.8045 | 4.8106 | ±9.6213 | -0.375 | 0.7076 |  |
| Age (years) | -0.0569 | 0.1879 | ±0.3758 | -0.303 | 0.7621 |  |
| **BMI (kg/m2)** | **-0.9270** | 0.3271 | ±0.6541 | **-2.834** | **0.0046** | ** |
| Hypertension | -7.7979 | 4.4090 | ±8.8179 | -1.769 | 0.0770 | . |
| High cholesterol | -2.7429 | 4.0482 | ±8.0963 | -0.678 | 0.4981 |  |
| Kidney disease | -18.5685 | 10.6041 | ±21.2083 | -1.751 | 0.0799 | . |
| Circulatory disease | +13.1461 | 6.9521 | ±13.9042 | +1.891 | 0.0586 | . |
| Avg. daily time < 54 (%) | -4.0111 | 2.5181 | ±5.0361 | -1.593 | 0.1112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0207**, F-statistic = **3.18** (p = **2.92e-04**), Residual SE = **65.529** on **1125** df, AIC = **12749.6**, BIC = **12810.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.4709** | 16.4968 | ±32.9937 | **+24.457** | **4.19e-132** | *** |
| Education: graduate level (vs college) | +0.7238 | 4.1095 | ±8.2190 | +0.176 | 0.8602 |  |
| Education: high school or below (vs college) | -15.5279 | 8.8123 | ±17.6246 | -1.762 | 0.0781 | . |
| Site: UCSD (vs UAB) | -6.0973 | 5.4484 | ±10.8968 | -1.119 | 0.2631 |  |
| Site: UW (vs UAB) | -1.1234 | 4.8113 | ±9.6226 | -0.233 | 0.8154 |  |
| Age (years) | -0.0548 | 0.1880 | ±0.3760 | -0.292 | 0.7705 |  |
| **BMI (kg/m2)** | **-0.9260** | 0.3280 | ±0.6560 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.5322 | 4.4142 | ±8.8284 | -1.706 | 0.0879 | . |
| High cholesterol | -2.4087 | 4.0440 | ±8.0879 | -0.596 | 0.5514 |  |
| Kidney disease | -18.6769 | 10.5822 | ±21.1643 | -1.765 | 0.0776 | . |
| Circulatory disease | +13.1348 | 6.9574 | ±13.9147 | +1.888 | 0.0590 | . |
| Time 54-69, pooled (%) | +0.5538 | 1.0905 | ±2.1811 | +0.508 | 0.6116 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.18** (p = **2.93e-04**), Residual SE = **65.529** on **1125** df, AIC = **12749.6**, BIC = **12810.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.6011** | 16.4568 | ±32.9136 | **+24.525** | **8.01e-133** | *** |
| Education: graduate level (vs college) | +0.7296 | 4.1127 | ±8.2255 | +0.177 | 0.8592 |  |
| Education: high school or below (vs college) | -15.5226 | 8.8111 | ±17.6222 | -1.762 | 0.0781 | . |
| Site: UCSD (vs UAB) | -6.1385 | 5.4424 | ±10.8849 | -1.128 | 0.2594 |  |
| Site: UW (vs UAB) | -1.1323 | 4.8055 | ±9.6110 | -0.236 | 0.8137 |  |
| Age (years) | -0.0560 | 0.1879 | ±0.3759 | -0.298 | 0.7658 |  |
| **BMI (kg/m2)** | **-0.9257** | 0.3282 | ±0.6563 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.5269 | 4.4192 | ±8.8384 | -1.703 | 0.0885 | . |
| High cholesterol | -2.4209 | 4.0418 | ±8.0837 | -0.599 | 0.5492 |  |
| Kidney disease | -18.6699 | 10.5821 | ±21.1643 | -1.764 | 0.0777 | . |
| Circulatory disease | +13.1421 | 6.9589 | ±13.9178 | +1.889 | 0.0590 | . |
| Avg. daily time 54-69 (%) | +0.5286 | 1.0890 | ±2.1780 | +0.485 | 0.6274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.10e-04**), Residual SE = **65.534** on **1125** df, AIC = **12749.8**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0522** | 16.5080 | ±33.0160 | **+24.476** | **2.65e-132** | *** |
| Education: graduate level (vs college) | +0.6595 | 4.1089 | ±8.2178 | +0.161 | 0.8725 |  |
| Education: high school or below (vs college) | -15.6940 | 8.8067 | ±17.6134 | -1.782 | 0.0747 | . |
| Site: UCSD (vs UAB) | -6.2341 | 5.4597 | ±10.9194 | -1.142 | 0.2535 |  |
| Site: UW (vs UAB) | -1.2746 | 4.8205 | ±9.6410 | -0.264 | 0.7915 |  |
| Age (years) | -0.0573 | 0.1880 | ±0.3759 | -0.305 | 0.7604 |  |
| **BMI (kg/m2)** | **-0.9240** | 0.3277 | ±0.6554 | **-2.820** | **0.0048** | ** |
| Hypertension | -7.5989 | 4.4128 | ±8.8255 | -1.722 | 0.0851 | . |
| High cholesterol | -2.4881 | 4.0513 | ±8.1026 | -0.614 | 0.5391 |  |
| Kidney disease | -18.6833 | 10.5925 | ±21.1851 | -1.764 | 0.0778 | . |
| Circulatory disease | +13.1536 | 6.9550 | ±13.9099 | +1.891 | 0.0586 | . |
| Time < 70 (%) | +0.0680 | 0.8445 | ±1.6890 | +0.080 | 0.9359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.10e-04**), Residual SE = **65.534** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0293** | 16.4621 | ±32.9242 | **+24.543** | **5.14e-133** | *** |
| Education: graduate level (vs college) | +0.6675 | 4.1132 | ±8.2263 | +0.162 | 0.8711 |  |
| Education: high school or below (vs college) | -15.6768 | 8.8077 | ±17.6154 | -1.780 | 0.0751 | . |
| Site: UCSD (vs UAB) | -6.2291 | 5.4477 | ±10.8954 | -1.143 | 0.2529 |  |
| Site: UW (vs UAB) | -1.2594 | 4.8122 | ±9.6244 | -0.262 | 0.7935 |  |
| Age (years) | -0.0574 | 0.1879 | ±0.3759 | -0.306 | 0.7599 |  |
| **BMI (kg/m2)** | **-0.9241** | 0.3278 | ±0.6556 | **-2.819** | **0.0048** | ** |
| Hypertension | -7.5899 | 4.4192 | ±8.8384 | -1.717 | 0.0859 | . |
| High cholesterol | -2.4826 | 4.0471 | ±8.0941 | -0.613 | 0.5396 |  |
| Kidney disease | -18.6817 | 10.5904 | ±21.1807 | -1.764 | 0.0777 | . |
| Circulatory disease | +13.1543 | 6.9566 | ±13.9133 | +1.891 | 0.0586 | . |
| Avg. daily time < 70 (%) | +0.1054 | 0.8810 | ±1.7620 | +0.120 | 0.9047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **3.04e-04**), Residual SE = **65.532** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.5692** | 44.8398 | ±89.6796 | **+8.755** | **2.04e-18** | *** |
| Education: graduate level (vs college) | +0.6253 | 4.0973 | ±8.1946 | +0.153 | 0.8787 |  |
| Education: high school or below (vs college) | -15.6428 | 8.8217 | ±17.6434 | -1.773 | 0.0762 | . |
| Site: UCSD (vs UAB) | -6.3216 | 5.4384 | ±10.8768 | -1.162 | 0.2451 |  |
| Site: UW (vs UAB) | -1.3206 | 4.7792 | ±9.5585 | -0.276 | 0.7823 |  |
| Age (years) | -0.0584 | 0.1880 | ±0.3759 | -0.311 | 0.7561 |  |
| **BMI (kg/m2)** | **-0.9247** | 0.3274 | ±0.6549 | **-2.824** | **0.0047** | ** |
| Hypertension | -7.6487 | 4.4095 | ±8.8190 | -1.735 | 0.0828 | . |
| High cholesterol | -2.4820 | 4.0273 | ±8.0547 | -0.616 | 0.5377 |  |
| Kidney disease | -18.6140 | 10.5971 | ±21.1941 | -1.757 | 0.0790 | . |
| Circulatory disease | +13.2281 | 6.9768 | ±13.9536 | +1.896 | 0.0580 | . |
| Time 54-250, pooled (%) | +0.1174 | 0.4156 | ±0.8313 | +0.283 | 0.7776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **3.05e-04**), Residual SE = **65.532** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.8137** | 46.1902 | ±92.3805 | **+8.504** | **1.83e-17** | *** |
| Education: graduate level (vs college) | +0.6263 | 4.0974 | ±8.1948 | +0.153 | 0.8785 |  |
| Education: high school or below (vs college) | -15.6455 | 8.8207 | ±17.6415 | -1.774 | 0.0761 | . |
| Site: UCSD (vs UAB) | -6.3117 | 5.4365 | ±10.8731 | -1.161 | 0.2456 |  |
| Site: UW (vs UAB) | -1.3147 | 4.7793 | ±9.5587 | -0.275 | 0.7832 |  |
| Age (years) | -0.0582 | 0.1880 | ±0.3759 | -0.309 | 0.7570 |  |
| **BMI (kg/m2)** | **-0.9243** | 0.3275 | ±0.6549 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.6481 | 4.4105 | ±8.8210 | -1.734 | 0.0829 | . |
| High cholesterol | -2.4801 | 4.0269 | ±8.0538 | -0.616 | 0.5380 |  |
| Kidney disease | -18.6209 | 10.5986 | ±21.1972 | -1.757 | 0.0789 | . |
| Circulatory disease | +13.2224 | 6.9763 | ±13.9527 | +1.895 | 0.0580 | . |
| Avg. daily time 54-250 (%) | +0.1146 | 0.4281 | ±0.8562 | +0.268 | 0.7890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1137**, R² = **0.0306**, Adj R² = **0.0212**, F-statistic = **3.23** (p = **2.33e-04**), Residual SE = **65.512** on **1125** df, AIC = **12749.0**, BIC = **12809.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.1092** | 16.4427 | ±32.8854 | **+24.577** | **2.24e-133** | *** |
| Education: graduate level (vs college) | +0.5320 | 4.1212 | ±8.2424 | +0.129 | 0.8973 |  |
| Education: high school or below (vs college) | -15.8211 | 8.8023 | ±17.6047 | -1.797 | 0.0723 | . |
| Site: UCSD (vs UAB) | -6.1894 | 5.4376 | ±10.8752 | -1.138 | 0.2550 |  |
| Site: UW (vs UAB) | -1.5251 | 4.7917 | ±9.5833 | -0.318 | 0.7503 |  |
| Age (years) | -0.0615 | 0.1882 | ±0.3764 | -0.327 | 0.7440 |  |
| **BMI (kg/m2)** | **-0.9307** | 0.3289 | ±0.6578 | **-2.830** | **0.0047** | ** |
| Hypertension | -7.9268 | 4.3924 | ±8.7848 | -1.805 | 0.0711 | . |
| High cholesterol | -2.8424 | 4.0351 | ±8.0703 | -0.704 | 0.4812 |  |
| Kidney disease | -19.2707 | 10.6293 | ±21.2586 | -1.813 | 0.0698 | . |
| Circulatory disease | +13.0842 | 6.9569 | ±13.9138 | +1.881 | 0.0600 | . |
| Time 181-250, pooled (%) | +0.2915 | 0.3730 | ±0.7460 | +0.781 | 0.4346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0307**, Adj R² = **0.0212**, F-statistic = **3.24** (p = **2.29e-04**), Residual SE = **65.510** on **1125** df, AIC = **12748.9**, BIC = **12809.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.1246** | 16.4457 | ±32.8915 | **+24.573** | **2.44e-133** | *** |
| Education: graduate level (vs college) | +0.5218 | 4.1222 | ±8.2445 | +0.127 | 0.8993 |  |
| Education: high school or below (vs college) | -15.8001 | 8.8010 | ±17.6021 | -1.795 | 0.0726 | . |
| Site: UCSD (vs UAB) | -6.1602 | 5.4391 | ±10.8782 | -1.133 | 0.2574 |  |
| Site: UW (vs UAB) | -1.5084 | 4.7886 | ±9.5772 | -0.315 | 0.7528 |  |
| Age (years) | -0.0611 | 0.1882 | ±0.3763 | -0.325 | 0.7454 |  |
| **BMI (kg/m2)** | **-0.9318** | 0.3289 | ±0.6579 | **-2.833** | **0.0046** | ** |
| Hypertension | -7.9334 | 4.3940 | ±8.7880 | -1.806 | 0.0710 | . |
| High cholesterol | -2.8583 | 4.0328 | ±8.0656 | -0.709 | 0.4785 |  |
| Kidney disease | -19.2943 | 10.6339 | ±21.2678 | -1.814 | 0.0696 | . |
| Circulatory disease | +13.0669 | 6.9572 | ±13.9144 | +1.878 | 0.0604 | . |
| Avg. daily time 181-250 (%) | +0.2971 | 0.3686 | ±0.7372 | +0.806 | 0.4202 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.19** (p = **2.74e-04**), Residual SE = **65.524** on **1125** df, AIC = **12749.4**, BIC = **12809.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0319** | 16.4117 | ±32.8234 | **+24.618** | **8.01e-134** | *** |
| Education: graduate level (vs college) | +0.6167 | 4.1056 | ±8.2112 | +0.150 | 0.8806 |  |
| Education: high school or below (vs college) | -15.8847 | 8.8290 | ±17.6579 | -1.799 | 0.0720 | . |
| Site: UCSD (vs UAB) | -6.1930 | 5.4398 | ±10.8797 | -1.138 | 0.2549 |  |
| Site: UW (vs UAB) | -1.4183 | 4.7918 | ±9.5836 | -0.296 | 0.7672 |  |
| Age (years) | -0.0590 | 0.1881 | ±0.3762 | -0.314 | 0.7538 |  |
| **BMI (kg/m2)** | **-0.9263** | 0.3283 | ±0.6567 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.7264 | 4.3956 | ±8.7913 | -1.758 | 0.0788 | . |
| High cholesterol | -2.7096 | 4.0303 | ±8.0606 | -0.672 | 0.5014 |  |
| Kidney disease | -19.0416 | 10.6123 | ±21.2246 | -1.794 | 0.0728 | . |
| Circulatory disease | +13.0373 | 6.9713 | ±13.9425 | +1.870 | 0.0615 | . |
| Time > 180 (%) | +0.1413 | 0.2584 | ±0.5168 | +0.547 | 0.5844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.20** (p = **2.70e-04**), Residual SE = **65.523** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0515** | 16.4166 | ±32.8331 | **+24.612** | **9.30e-134** | *** |
| Education: graduate level (vs college) | +0.6104 | 4.1065 | ±8.2130 | +0.149 | 0.8818 |  |
| Education: high school or below (vs college) | -15.8761 | 8.8264 | ±17.6527 | -1.799 | 0.0721 | . |
| Site: UCSD (vs UAB) | -6.1768 | 5.4404 | ±10.8807 | -1.135 | 0.2562 |  |
| Site: UW (vs UAB) | -1.4164 | 4.7907 | ±9.5814 | -0.296 | 0.7675 |  |
| Age (years) | -0.0589 | 0.1881 | ±0.3761 | -0.313 | 0.7542 |  |
| **BMI (kg/m2)** | **-0.9273** | 0.3285 | ±0.6569 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.7318 | 4.3963 | ±8.7925 | -1.759 | 0.0786 | . |
| High cholesterol | -2.7233 | 4.0283 | ±8.0566 | -0.676 | 0.4990 |  |
| Kidney disease | -19.0599 | 10.6172 | ±21.2344 | -1.795 | 0.0726 | . |
| Circulatory disease | +13.0271 | 6.9710 | ±13.9420 | +1.869 | 0.0617 | . |
| Avg. daily time > 180 (%) | +0.1480 | 0.2578 | ±0.5157 | +0.574 | 0.5660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1137**, R² = **0.0304**, Adj R² = **0.0210**, F-statistic = **3.21** (p = **2.55e-04**), Residual SE = **65.519** on **1125** df, AIC = **12749.2**, BIC = **12809.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2483** | 16.4385 | ±32.8769 | **+24.592** | **1.55e-133** | *** |
| Education: graduate level (vs college) | +0.7098 | 4.0936 | ±8.1872 | +0.173 | 0.8623 |  |
| Education: high school or below (vs college) | -15.8767 | 8.8357 | ±17.6715 | -1.797 | 0.0724 | . |
| Site: UCSD (vs UAB) | -6.1622 | 5.4361 | ±10.8722 | -1.134 | 0.2570 |  |
| Site: UW (vs UAB) | -1.3895 | 4.7860 | ±9.5719 | -0.290 | 0.7716 |  |
| Age (years) | -0.0548 | 0.1879 | ±0.3759 | -0.292 | 0.7704 |  |
| **BMI (kg/m2)** | **-0.9403** | 0.3306 | ±0.6611 | **-2.845** | **0.0044** | ** |
| Hypertension | -7.6417 | 4.4042 | ±8.8084 | -1.735 | 0.0827 | . |
| High cholesterol | -2.8256 | 4.0410 | ±8.0820 | -0.699 | 0.4844 |  |
| Kidney disease | -18.7860 | 10.5874 | ±21.1748 | -1.774 | 0.0760 | . |
| Circulatory disease | +13.1223 | 6.9600 | ±13.9199 | +1.885 | 0.0594 | . |
| Nocturnal time > 180 (%) | +0.1896 | 0.2587 | ±0.5173 | +0.733 | 0.4636 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.10e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2996** | 16.4876 | ±32.9753 | **+24.521** | **8.74e-133** | *** |
| Education: graduate level (vs college) | +0.6494 | 4.1005 | ±8.2010 | +0.158 | 0.8742 |  |
| Education: high school or below (vs college) | -15.7257 | 8.7997 | ±17.5995 | -1.787 | 0.0739 | . |
| Site: UCSD (vs UAB) | -6.2749 | 5.4312 | ±10.8624 | -1.155 | 0.2480 |  |
| Site: UW (vs UAB) | -1.2974 | 4.7856 | ±9.5712 | -0.271 | 0.7863 |  |
| Age (years) | -0.0577 | 0.1881 | ±0.3763 | -0.307 | 0.7591 |  |
| **BMI (kg/m2)** | **-0.9262** | 0.3294 | ±0.6588 | **-2.812** | **0.0049** | ** |
| Hypertension | -7.5810 | 4.3996 | ±8.7991 | -1.723 | 0.0849 | . |
| High cholesterol | -2.4868 | 4.0281 | ±8.0561 | -0.617 | 0.5370 |  |
| Kidney disease | -18.6653 | 10.5943 | ±21.1887 | -1.762 | 0.0781 | . |
| Circulatory disease | +13.1481 | 6.9656 | ±13.9312 | +1.888 | 0.0591 | . |
| Any reading > 250 during wear (0/1) | -0.4700 | 5.0070 | ±10.0140 | -0.094 | 0.9252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.09e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2141** | 16.3987 | ±32.7973 | **+24.649** | **3.75e-134** | *** |
| Education: graduate level (vs college) | +0.6381 | 4.0969 | ±8.1937 | +0.156 | 0.8762 |  |
| Education: high school or below (vs college) | -15.6770 | 8.8292 | ±17.6585 | -1.776 | 0.0758 | . |
| Site: UCSD (vs UAB) | -6.2839 | 5.4348 | ±10.8696 | -1.156 | 0.2476 |  |
| Site: UW (vs UAB) | -1.3051 | 4.7823 | ±9.5646 | -0.273 | 0.7849 |  |
| Age (years) | -0.0580 | 0.1880 | ±0.3760 | -0.309 | 0.7577 |  |
| **BMI (kg/m2)** | **-0.9242** | 0.3275 | ±0.6550 | **-2.822** | **0.0048** | ** |
| Hypertension | -7.6279 | 4.4086 | ±8.8172 | -1.730 | 0.0836 | . |
| High cholesterol | -2.4885 | 4.0273 | ±8.0547 | -0.618 | 0.5366 |  |
| Kidney disease | -18.6492 | 10.5939 | ±21.1878 | -1.760 | 0.0783 | . |
| Circulatory disease | +13.1928 | 6.9801 | ±13.9601 | +1.890 | 0.0587 | . |
| Time > 250 (%) | -0.0600 | 0.4703 | ±0.9406 | -0.128 | 0.8984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.09e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2078** | 16.3983 | ±32.7967 | **+24.649** | **3.74e-134** | *** |
| Education: graduate level (vs college) | +0.6383 | 4.0968 | ±8.1936 | +0.156 | 0.8762 |  |
| Education: high school or below (vs college) | -15.6778 | 8.8271 | ±17.6541 | -1.776 | 0.0757 | . |
| Site: UCSD (vs UAB) | -6.2838 | 5.4346 | ±10.8692 | -1.156 | 0.2476 |  |
| Site: UW (vs UAB) | -1.3037 | 4.7825 | ±9.5651 | -0.273 | 0.7852 |  |
| Age (years) | -0.0580 | 0.1880 | ±0.3760 | -0.308 | 0.7577 |  |
| **BMI (kg/m2)** | **-0.9240** | 0.3275 | ±0.6551 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.6284 | 4.4090 | ±8.8181 | -1.730 | 0.0836 | . |
| High cholesterol | -2.4884 | 4.0270 | ±8.0540 | -0.618 | 0.5366 |  |
| Kidney disease | -18.6505 | 10.5959 | ±21.1917 | -1.760 | 0.0784 | . |
| Circulatory disease | +13.1922 | 6.9795 | ±13.9589 | +1.890 | 0.0587 | . |
| Avg. daily time > 250 (%) | -0.0614 | 0.4728 | ±0.9456 | -0.130 | 0.8967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 1,130; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0734**, F-statistic = **9.94** (p = **4.16e-16**), Residual SE = **16.661** on **1119** df, AIC = **9575.3**, BIC = **9630.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4909** | 4.4214 | ±8.8428 | **+11.872** | **1.65e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6726** | 1.0675 | ±2.1350 | **-2.504** | **0.0123** | * |
| Education: high school or below (vs college) | +0.5387 | 1.9678 | ±3.9356 | +0.274 | 0.7843 |  |
| Site: UCSD (vs UAB) | +0.3648 | 1.3705 | ±2.7409 | +0.266 | 0.7901 |  |
| Site: UW (vs UAB) | -2.2583 | 1.2008 | ±2.4016 | -1.881 | 0.0600 | . |
| **Age (years)** | **-0.2430** | 0.0487 | ±0.0975 | **-4.985** | **6.20e-07** | *** |
| **BMI (kg/m2)** | **+0.4354** | 0.0855 | ±0.1709 | **+5.094** | **3.51e-07** | *** |
| Hypertension | +0.0423 | 1.1464 | ±2.2929 | +0.037 | 0.9706 |  |
| High cholesterol | -0.0244 | 1.0575 | ±2.1150 | -0.023 | 0.9816 |  |
| Kidney disease | +1.2632 | 2.2584 | ±4.5168 | +0.559 | 0.5759 |  |
| Circulatory disease | -0.1758 | 1.5643 | ±3.1286 | -0.112 | 0.9105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1130**, R² = **0.0895**, Adj R² = **0.0806**, F-statistic = **9.99** (p = **1.62e-17**), Residual SE = **16.596** on **1118** df, AIC = **9567.5**, BIC = **9627.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.4757** | 6.4930 | ±12.9860 | **+5.772** | **7.85e-09** | *** |
| **Education: graduate level (vs college)** | **-2.6709** | 1.0659 | ±2.1317 | **-2.506** | **0.0122** | * |
| Education: high school or below (vs college) | +0.2032 | 1.9322 | ±3.8644 | +0.105 | 0.9162 |  |
| Site: UCSD (vs UAB) | +0.2278 | 1.3676 | ±2.7352 | +0.167 | 0.8677 |  |
| **Site: UW (vs UAB)** | **-2.3901** | 1.1919 | ±2.3837 | **-2.005** | **0.0449** | * |
| **Age (years)** | **-0.2554** | 0.0487 | ±0.0974 | **-5.244** | **1.57e-07** | *** |
| **BMI (kg/m2)** | **+0.4140** | 0.0838 | ±0.1675 | **+4.942** | **7.74e-07** | *** |
| Hypertension | -0.0939 | 1.1429 | ±2.2858 | -0.082 | 0.9345 |  |
| High cholesterol | -0.4475 | 1.0572 | ±2.1145 | -0.423 | 0.6721 |  |
| Kidney disease | +1.2716 | 2.2427 | ±4.4854 | +0.567 | 0.5707 |  |
| Circulatory disease | -0.3354 | 1.5297 | ±3.0594 | -0.219 | 0.8264 |  |
| **HbA1c (%)** | **+2.9623** | 0.9302 | ±1.8604 | **+3.185** | **0.0014** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1130**, R² = **0.0857**, Adj R² = **0.0767**, F-statistic = **9.53** (p = **1.35e-16**), Residual SE = **16.631** on **1118** df, AIC = **9572.2**, BIC = **9632.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.9724** | 5.6176 | ±11.2351 | **+8.184** | **2.75e-16** | *** |
| **Education: graduate level (vs college)** | **-2.7848** | 1.0665 | ±2.1330 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | +0.3351 | 1.9544 | ±3.9088 | +0.171 | 0.8639 |  |
| Site: UCSD (vs UAB) | +0.3172 | 1.3734 | ±2.7468 | +0.231 | 0.8173 |  |
| **Site: UW (vs UAB)** | **-2.4758** | 1.2044 | ±2.4089 | **-2.056** | **0.0398** | * |
| **Age (years)** | **-0.2462** | 0.0487 | ±0.0975 | **-5.052** | **4.37e-07** | *** |
| **BMI (kg/m2)** | **+0.4268** | 0.0852 | ±0.1703 | **+5.012** | **5.39e-07** | *** |
| Hypertension | -0.1539 | 1.1489 | ±2.2979 | -0.134 | 0.8935 |  |
| High cholesterol | -0.2104 | 1.0582 | ±2.1164 | -0.199 | 0.8424 |  |
| Kidney disease | +1.0083 | 2.2524 | ±4.5048 | +0.448 | 0.6544 |  |
| Circulatory disease | -0.2747 | 1.5504 | ±3.1008 | -0.177 | 0.8594 |  |
| Mean glucose (mg/dL) | +0.0605 | 0.0328 | ±0.0656 | +1.845 | 0.0651 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1130**, R² = **0.0857**, Adj R² = **0.0767**, F-statistic = **9.53** (p = **1.35e-16**), Residual SE = **16.631** on **1118** df, AIC = **9572.2**, BIC = **9632.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.6006** | 9.1631 | ±18.3263 | **+4.103** | **4.07e-05** | *** |
| **Education: graduate level (vs college)** | **-2.7848** | 1.0665 | ±2.1330 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | +0.3351 | 1.9544 | ±3.9088 | +0.171 | 0.8639 |  |
| Site: UCSD (vs UAB) | +0.3172 | 1.3734 | ±2.7468 | +0.231 | 0.8173 |  |
| **Site: UW (vs UAB)** | **-2.4758** | 1.2044 | ±2.4089 | **-2.056** | **0.0398** | * |
| **Age (years)** | **-0.2462** | 0.0487 | ±0.0975 | **-5.052** | **4.37e-07** | *** |
| **BMI (kg/m2)** | **+0.4268** | 0.0852 | ±0.1703 | **+5.012** | **5.39e-07** | *** |
| Hypertension | -0.1539 | 1.1489 | ±2.2979 | -0.134 | 0.8935 |  |
| High cholesterol | -0.2104 | 1.0582 | ±2.1164 | -0.199 | 0.8424 |  |
| Kidney disease | +1.0083 | 2.2524 | ±4.5048 | +0.448 | 0.6544 |  |
| Circulatory disease | -0.2747 | 1.5504 | ±3.1008 | -0.177 | 0.8594 |  |
| GMI (%) | +2.5292 | 1.3711 | ±2.7421 | +1.845 | 0.0651 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1130**, R² = **0.0847**, Adj R² = **0.0757**, F-statistic = **9.41** (p = **2.40e-16**), Residual SE = **16.640** on **1118** df, AIC = **9573.4**, BIC = **9633.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1952** | 5.4751 | ±10.9501 | **+8.620** | **6.69e-18** | *** |
| **Education: graduate level (vs college)** | **-2.7240** | 1.0666 | ±2.1333 | **-2.554** | **0.0107** | * |
| Education: high school or below (vs college) | +0.3592 | 1.9560 | ±3.9120 | +0.184 | 0.8543 |  |
| Site: UCSD (vs UAB) | +0.2582 | 1.3728 | ±2.7456 | +0.188 | 0.8508 |  |
| **Site: UW (vs UAB)** | **-2.4338** | 1.2045 | ±2.4090 | **-2.021** | **0.0433** | * |
| **Age (years)** | **-0.2409** | 0.0486 | ±0.0973 | **-4.953** | **7.30e-07** | *** |
| **BMI (kg/m2)** | **+0.4157** | 0.0855 | ±0.1710 | **+4.861** | **1.17e-06** | *** |
| Hypertension | -0.0918 | 1.1487 | ±2.2975 | -0.080 | 0.9363 |  |
| High cholesterol | -0.2211 | 1.0598 | ±2.1196 | -0.209 | 0.8347 |  |
| Kidney disease | +1.1970 | 2.2479 | ±4.4959 | +0.533 | 0.5944 |  |
| Circulatory disease | -0.2118 | 1.5509 | ±3.1018 | -0.137 | 0.8914 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0503 | 0.0318 | ±0.0636 | +1.582 | 0.1136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1130**, R² = **0.0879**, Adj R² = **0.0789**, F-statistic = **9.79** (p = **4.12e-17**), Residual SE = **16.611** on **1118** df, AIC = **9569.5**, BIC = **9629.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2746** | 4.7285 | ±9.4569 | **+10.209** | **1.80e-24** | *** |
| **Education: graduate level (vs college)** | **-2.7063** | 1.0619 | ±2.1238 | **-2.549** | **0.0108** | * |
| Education: high school or below (vs college) | +0.5144 | 1.9507 | ±3.9015 | +0.264 | 0.7920 |  |
| Site: UCSD (vs UAB) | +0.4993 | 1.3724 | ±2.7447 | +0.364 | 0.7160 |  |
| **Site: UW (vs UAB)** | **-2.3948** | 1.2009 | ±2.4019 | **-1.994** | **0.0461** | * |
| **Age (years)** | **-0.2488** | 0.0487 | ±0.0973 | **-5.114** | **3.15e-07** | *** |
| **BMI (kg/m2)** | **+0.4393** | 0.0857 | ±0.1714 | **+5.127** | **2.94e-07** | *** |
| Hypertension | -0.2271 | 1.1516 | ±2.3031 | -0.197 | 0.8437 |  |
| High cholesterol | -0.0896 | 1.0551 | ±2.1103 | -0.085 | 0.9323 |  |
| Kidney disease | +0.7412 | 2.2741 | ±4.5482 | +0.326 | 0.7445 |  |
| Circulatory disease | -0.2881 | 1.5494 | ±3.0988 | -0.186 | 0.8525 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.2162** | 0.0876 | ±0.1752 | **+2.469** | **0.0136** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1130**, R² = **0.0868**, Adj R² = **0.0778**, F-statistic = **9.66** (p = **7.56e-17**), Residual SE = **16.621** on **1118** df, AIC = **9570.9**, BIC = **9631.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0248** | 4.6627 | ±9.3255 | **+10.514** | **7.43e-26** | *** |
| **Education: graduate level (vs college)** | **-2.7194** | 1.0632 | ±2.1265 | **-2.558** | **0.0105** | * |
| Education: high school or below (vs college) | +0.4908 | 1.9542 | ±3.9084 | +0.251 | 0.8017 |  |
| Site: UCSD (vs UAB) | +0.4560 | 1.3711 | ±2.7422 | +0.333 | 0.7394 |  |
| **Site: UW (vs UAB)** | **-2.4073** | 1.2026 | ±2.4052 | **-2.002** | **0.0453** | * |
| **Age (years)** | **-0.2499** | 0.0488 | ±0.0975 | **-5.126** | **2.97e-07** | *** |
| **BMI (kg/m2)** | **+0.4359** | 0.0853 | ±0.1707 | **+5.108** | **3.26e-07** | *** |
| Hypertension | -0.2008 | 1.1530 | ±2.3061 | -0.174 | 0.8618 |  |
| High cholesterol | -0.0873 | 1.0563 | ±2.1125 | -0.083 | 0.9341 |  |
| Kidney disease | +0.8005 | 2.2759 | ±4.5518 | +0.352 | 0.7250 |  |
| Circulatory disease | -0.2758 | 1.5514 | ±3.1029 | -0.178 | 0.8589 |  |
| **Avg. daily SD (mg/dL)** | **+0.2081** | 0.0925 | ±0.1851 | **+2.249** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1130**, R² = **0.0857**, Adj R² = **0.0767**, F-statistic = **9.53** (p = **1.35e-16**), Residual SE = **16.631** on **1118** df, AIC = **9572.2**, BIC = **9632.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4507** | 4.9923 | ±9.9846 | **+9.505** | **2.01e-21** | *** |
| **Education: graduate level (vs college)** | **-2.6248** | 1.0623 | ±2.1245 | **-2.471** | **0.0135** | * |
| Education: high school or below (vs college) | +0.6463 | 1.9591 | ±3.9183 | +0.330 | 0.7415 |  |
| Site: UCSD (vs UAB) | +0.5618 | 1.3692 | ±2.7384 | +0.410 | 0.6816 |  |
| Site: UW (vs UAB) | -2.2352 | 1.2010 | ±2.4021 | -1.861 | 0.0627 | . |
| **Age (years)** | **-0.2475** | 0.0487 | ±0.0975 | **-5.079** | **3.79e-07** | *** |
| **BMI (kg/m2)** | **+0.4451** | 0.0861 | ±0.1722 | **+5.170** | **2.34e-07** | *** |
| Hypertension | -0.0982 | 1.1487 | ±2.2975 | -0.086 | 0.9319 |  |
| High cholesterol | +0.0550 | 1.0580 | ±2.1160 | +0.052 | 0.9586 |  |
| Kidney disease | +0.9269 | 2.2805 | ±4.5610 | +0.406 | 0.6844 |  |
| Circulatory disease | -0.2093 | 1.5582 | ±3.1163 | -0.134 | 0.8931 |  |
| **CV (%)** | **+0.2801** | 0.1299 | ±0.2597 | **+2.157** | **0.0310** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1130**, R² = **0.0872**, Adj R² = **0.0782**, F-statistic = **9.71** (p = **5.92e-17**), Residual SE = **16.617** on **1118** df, AIC = **9570.3**, BIC = **9630.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8240** | 5.0035 | ±10.0071 | **+11.756** | **6.54e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6044** | 1.0609 | ±2.1218 | **-2.455** | **0.0141** | * |
| Education: high school or below (vs college) | +0.5863 | 1.9557 | ±3.9114 | +0.300 | 0.7643 |  |
| Site: UCSD (vs UAB) | +0.5776 | 1.3675 | ±2.7351 | +0.422 | 0.6727 |  |
| Site: UW (vs UAB) | -2.2974 | 1.1999 | ±2.3998 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.2484** | 0.0487 | ±0.0974 | **-5.099** | **3.41e-07** | *** |
| **BMI (kg/m2)** | **+0.4447** | 0.0859 | ±0.1718 | **+5.177** | **2.26e-07** | *** |
| Hypertension | -0.1486 | 1.1499 | ±2.2998 | -0.129 | 0.8972 |  |
| High cholesterol | +0.0440 | 1.0566 | ±2.1132 | +0.042 | 0.9668 |  |
| Kidney disease | +0.9838 | 2.2696 | ±4.5392 | +0.433 | 0.6647 |  |
| Circulatory disease | -0.2047 | 1.5556 | ±3.1112 | -0.132 | 0.8953 |  |
| **Mean / SD ratio** | **-1.0683** | 0.4090 | ±0.8180 | **-2.612** | **0.0090** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1130**, R² = **0.0860**, Adj R² = **0.0770**, F-statistic = **9.56** (p = **1.16e-16**), Residual SE = **16.628** on **1118** df, AIC = **9571.8**, BIC = **9632.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.1931** | 5.0365 | ±10.0729 | **+11.554** | **7.02e-31** | *** |
| **Education: graduate level (vs college)** | **-2.6513** | 1.0628 | ±2.1255 | **-2.495** | **0.0126** | * |
| Education: high school or below (vs college) | +0.5070 | 1.9585 | ±3.9170 | +0.259 | 0.7957 |  |
| Site: UCSD (vs UAB) | +0.5065 | 1.3677 | ±2.7355 | +0.370 | 0.7111 |  |
| Site: UW (vs UAB) | -2.3240 | 1.2018 | ±2.4036 | -1.934 | 0.0531 | . |
| **Age (years)** | **-0.2503** | 0.0489 | ±0.0977 | **-5.123** | **3.00e-07** | *** |
| **BMI (kg/m2)** | **+0.4385** | 0.0853 | ±0.1706 | **+5.140** | **2.75e-07** | *** |
| Hypertension | -0.0854 | 1.1505 | ±2.3009 | -0.074 | 0.9409 |  |
| High cholesterol | +0.0295 | 1.0581 | ±2.1162 | +0.028 | 0.9778 |  |
| Kidney disease | +0.9689 | 2.2741 | ±4.5482 | +0.426 | 0.6701 |  |
| Circulatory disease | -0.1877 | 1.5599 | ±3.1198 | -0.120 | 0.9042 |  |
| **Avg. daily mean/SD** | **-0.7891** | 0.3420 | ±0.6840 | **-2.307** | **0.0210** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1130**, R² = **0.0861**, Adj R² = **0.0771**, F-statistic = **9.58** (p = **1.08e-16**), Residual SE = **16.627** on **1118** df, AIC = **9571.7**, BIC = **9632.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2161** | 5.1036 | ±10.2072 | **+9.056** | **1.36e-19** | *** |
| **Education: graduate level (vs college)** | **-2.6219** | 1.0621 | ±2.1242 | **-2.469** | **0.0136** | * |
| Education: high school or below (vs college) | +0.4461 | 1.9604 | ±3.9209 | +0.228 | 0.8200 |  |
| Site: UCSD (vs UAB) | +0.5306 | 1.3713 | ±2.7425 | +0.387 | 0.6988 |  |
| Site: UW (vs UAB) | -2.0977 | 1.2009 | ±2.4018 | -1.747 | 0.0807 | . |
| **Age (years)** | **-0.2384** | 0.0485 | ±0.0971 | **-4.912** | **9.03e-07** | *** |
| **BMI (kg/m2)** | **+0.4385** | 0.0850 | ±0.1700 | **+5.159** | **2.48e-07** | *** |
| Hypertension | +0.0676 | 1.1493 | ±2.2985 | +0.059 | 0.9531 |  |
| High cholesterol | +0.0587 | 1.0583 | ±2.1165 | +0.055 | 0.9558 |  |
| Kidney disease | +1.0704 | 2.2471 | ±4.4942 | +0.476 | 0.6338 |  |
| Circulatory disease | -0.1133 | 1.5567 | ±3.1134 | -0.073 | 0.9420 |  |
| **MAG (mg/dL/h)** | **+0.1508** | 0.0671 | ±0.1342 | **+2.247** | **0.0246** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1130**, R² = **0.0870**, Adj R² = **0.0780**, F-statistic = **9.69** (p = **6.58e-17**), Residual SE = **16.619** on **1118** df, AIC = **9570.6**, BIC = **9630.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6468** | 4.8534 | ±9.7067 | **+9.817** | **9.49e-23** | *** |
| **Education: graduate level (vs college)** | **-2.7231** | 1.0629 | ±2.1257 | **-2.562** | **0.0104** | * |
| Education: high school or below (vs college) | +0.4461 | 1.9567 | ±3.9134 | +0.228 | 0.8197 |  |
| Site: UCSD (vs UAB) | +0.4638 | 1.3698 | ±2.7396 | +0.339 | 0.7349 |  |
| **Site: UW (vs UAB)** | **-2.3590** | 1.2011 | ±2.4021 | **-1.964** | **0.0495** | * |
| **Age (years)** | **-0.2484** | 0.0488 | ±0.0975 | **-5.095** | **3.49e-07** | *** |
| **BMI (kg/m2)** | **+0.4485** | 0.0863 | ±0.1726 | **+5.198** | **2.02e-07** | *** |
| Hypertension | -0.1322 | 1.1517 | ±2.3034 | -0.115 | 0.9086 |  |
| High cholesterol | -0.0243 | 1.0567 | ±2.1134 | -0.023 | 0.9816 |  |
| Kidney disease | +0.8957 | 2.2691 | ±4.5381 | +0.395 | 0.6930 |  |
| Circulatory disease | -0.2586 | 1.5550 | ±3.1101 | -0.166 | 0.8679 |  |
| **Avg. daily range (mg/dL)** | **+0.0501** | 0.0206 | ±0.0412 | **+2.433** | **0.0150** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1130**, R² = **0.0885**, Adj R² = **0.0796**, F-statistic = **9.87** (p = **2.81e-17**), Residual SE = **16.605** on **1118** df, AIC = **9568.7**, BIC = **9629.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5982** | 4.5335 | ±9.0670 | **+10.940** | **7.38e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7013** | 1.0635 | ±2.1270 | **-2.540** | **0.0111** | * |
| Education: high school or below (vs college) | +0.6332 | 1.9341 | ±3.8682 | +0.327 | 0.7434 |  |
| Site: UCSD (vs UAB) | +0.5939 | 1.3671 | ±2.7342 | +0.434 | 0.6640 |  |
| Site: UW (vs UAB) | -2.2992 | 1.1958 | ±2.3915 | -1.923 | 0.0545 | . |
| **Age (years)** | **-0.2401** | 0.0484 | ±0.0969 | **-4.957** | **7.17e-07** | *** |
| **BMI (kg/m2)** | **+0.4257** | 0.0858 | ±0.1715 | **+4.963** | **6.95e-07** | *** |
| Hypertension | -0.0259 | 1.1415 | ±2.2829 | -0.023 | 0.9819 |  |
| High cholesterol | -0.1572 | 1.0541 | ±2.1083 | -0.149 | 0.8814 |  |
| Kidney disease | +1.1062 | 2.2489 | ±4.4977 | +0.492 | 0.6228 |  |
| Circulatory disease | -0.2699 | 1.5476 | ±3.0952 | -0.174 | 0.8616 |  |
| **SD of daily means (mg/dL)** | **+0.4649** | 0.1707 | ±0.3414 | **+2.723** | **0.0065** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1130**, R² = **0.0837**, Adj R² = **0.0746**, F-statistic = **9.28** (p = **4.31e-16**), Residual SE = **16.650** on **1118** df, AIC = **9574.7**, BIC = **9635.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.5103** | 9.0936 | ±18.1873 | **+6.764** | **1.34e-11** | *** |
| **Education: graduate level (vs college)** | **-2.6980** | 1.0675 | ±2.1349 | **-2.528** | **0.0115** | * |
| Education: high school or below (vs college) | +0.4962 | 1.9549 | ±3.9099 | +0.254 | 0.7997 |  |
| Site: UCSD (vs UAB) | +0.4205 | 1.3792 | ±2.7584 | +0.305 | 0.7604 |  |
| Site: UW (vs UAB) | -2.2865 | 1.1999 | ±2.3998 | -1.906 | 0.0567 | . |
| **Age (years)** | **-0.2423** | 0.0487 | ±0.0973 | **-4.980** | **6.35e-07** | *** |
| **BMI (kg/m2)** | **+0.4323** | 0.0855 | ±0.1711 | **+5.054** | **4.32e-07** | *** |
| Hypertension | -0.0466 | 1.1503 | ±2.3005 | -0.041 | 0.9677 |  |
| High cholesterol | -0.1100 | 1.0594 | ±2.1188 | -0.104 | 0.9173 |  |
| Kidney disease | +1.0564 | 2.2675 | ±4.5350 | +0.466 | 0.6413 |  |
| Circulatory disease | -0.2515 | 1.5575 | ±3.1150 | -0.161 | 0.8717 |  |
| Time in range 70-180, pooled (%) | -0.0927 | 0.0824 | ±0.1648 | -1.126 | 0.2602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1130**, R² = **0.0834**, Adj R² = **0.0743**, F-statistic = **9.24** (p = **5.09e-16**), Residual SE = **16.652** on **1118** df, AIC = **9575.1**, BIC = **9635.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.8604** | 9.1049 | ±18.2099 | **+6.684** | **2.32e-11** | *** |
| **Education: graduate level (vs college)** | **-2.6972** | 1.0677 | ±2.1354 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | +0.5091 | 1.9565 | ±3.9131 | +0.260 | 0.7947 |  |
| Site: UCSD (vs UAB) | +0.4129 | 1.3784 | ±2.7567 | +0.300 | 0.7645 |  |
| Site: UW (vs UAB) | -2.2829 | 1.2003 | ±2.4005 | -1.902 | 0.0572 | . |
| **Age (years)** | **-0.2426** | 0.0487 | ±0.0974 | **-4.984** | **6.22e-07** | *** |
| **BMI (kg/m2)** | **+0.4320** | 0.0855 | ±0.1710 | **+5.054** | **4.32e-07** | *** |
| Hypertension | -0.0391 | 1.1503 | ±2.3006 | -0.034 | 0.9729 |  |
| High cholesterol | -0.1090 | 1.0598 | ±2.1196 | -0.103 | 0.9181 |  |
| Kidney disease | +1.0747 | 2.2677 | ±4.5355 | +0.474 | 0.6356 |  |
| Circulatory disease | -0.2454 | 1.5585 | ±3.1169 | -0.157 | 0.8749 |  |
| Avg. daily time in range 70-180 (%) | -0.0855 | 0.0818 | ±0.1636 | -1.045 | 0.2958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1130**, R² = **0.0820**, Adj R² = **0.0730**, F-statistic = **9.08** (p = **1.07e-15**), Residual SE = **16.664** on **1118** df, AIC = **9576.7**, BIC = **9637.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0475** | 4.4862 | ±8.9725 | **+11.602** | **4.05e-31** | *** |
| **Education: graduate level (vs college)** | **-2.6498** | 1.0689 | ±2.1378 | **-2.479** | **0.0132** | * |
| Education: high school or below (vs college) | +0.6201 | 1.9820 | ±3.9640 | +0.313 | 0.7544 |  |
| Site: UCSD (vs UAB) | +0.4910 | 1.3775 | ±2.7550 | +0.356 | 0.7215 |  |
| Site: UW (vs UAB) | -2.2049 | 1.2037 | ±2.4073 | -1.832 | 0.0670 | . |
| **Age (years)** | **-0.2406** | 0.0490 | ±0.0979 | **-4.914** | **8.94e-07** | *** |
| **BMI (kg/m2)** | **+0.4341** | 0.0855 | ±0.1710 | **+5.078** | **3.81e-07** | *** |
| Hypertension | +0.0337 | 1.1480 | ±2.2960 | +0.029 | 0.9766 |  |
| High cholesterol | +0.0244 | 1.0598 | ±2.1197 | +0.023 | 0.9817 |  |
| Kidney disease | +1.2823 | 2.2680 | ±4.5360 | +0.565 | 0.5718 |  |
| Circulatory disease | -0.2651 | 1.5721 | ±3.1442 | -0.169 | 0.8661 |  |
| Any reading < 54 during wear (0/1) | +0.7802 | 1.0759 | ±2.1519 | +0.725 | 0.4683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.36e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.3**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4636** | 4.4479 | ±8.8957 | **+11.795** | **4.13e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6712** | 1.0677 | ±2.1355 | **-2.502** | **0.0124** | * |
| Education: high school or below (vs college) | +0.5446 | 1.9705 | ±3.9409 | +0.276 | 0.7823 |  |
| Site: UCSD (vs UAB) | +0.3770 | 1.3790 | ±2.7580 | +0.273 | 0.7846 |  |
| Site: UW (vs UAB) | -2.2491 | 1.2055 | ±2.4110 | -1.866 | 0.0621 | . |
| **Age (years)** | **-0.2429** | 0.0488 | ±0.0977 | **-4.975** | **6.54e-07** | *** |
| **BMI (kg/m2)** | **+0.4355** | 0.0856 | ±0.1713 | **+5.085** | **3.68e-07** | *** |
| Hypertension | +0.0449 | 1.1475 | ±2.2951 | +0.039 | 0.9688 |  |
| High cholesterol | -0.0189 | 1.0586 | ±2.1172 | -0.018 | 0.9858 |  |
| Kidney disease | +1.2605 | 2.2599 | ±4.5198 | +0.558 | 0.5770 |  |
| Circulatory disease | -0.1758 | 1.5649 | ±3.1297 | -0.112 | 0.9106 |  |
| Time < 54 (%) | +0.0618 | 0.8855 | ±1.7709 | +0.070 | 0.9444 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.04** (p = **1.32e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.2**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5557** | 4.4353 | ±8.8707 | **+11.849** | **2.17e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6793** | 1.0678 | ±2.1357 | **-2.509** | **0.0121** | * |
| Education: high school or below (vs college) | +0.5197 | 1.9724 | ±3.9448 | +0.263 | 0.7922 |  |
| Site: UCSD (vs UAB) | +0.3293 | 1.3754 | ±2.7509 | +0.239 | 0.8108 |  |
| Site: UW (vs UAB) | -2.2913 | 1.2051 | ±2.4103 | -1.901 | 0.0573 | . |
| **Age (years)** | **-0.2429** | 0.0488 | ±0.0975 | **-4.980** | **6.36e-07** | *** |
| **BMI (kg/m2)** | **+0.4352** | 0.0856 | ±0.1712 | **+5.085** | **3.68e-07** | *** |
| Hypertension | +0.0302 | 1.1490 | ±2.2981 | +0.026 | 0.9790 |  |
| High cholesterol | -0.0414 | 1.0581 | ±2.1162 | -0.039 | 0.9688 |  |
| Kidney disease | +1.2711 | 2.2602 | ±4.5205 | +0.562 | 0.5739 |  |
| Circulatory disease | -0.1791 | 1.5647 | ±3.1294 | -0.114 | 0.9089 |  |
| Avg. daily time < 54 (%) | -0.2710 | 1.1803 | ±2.3605 | -0.230 | 0.8184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.33e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.2**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5928** | 4.4673 | ±8.9345 | **+11.773** | **5.38e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6843** | 1.0674 | ±2.1349 | **-2.515** | **0.0119** | * |
| Education: high school or below (vs college) | +0.5102 | 1.9742 | ±3.9484 | +0.258 | 0.7961 |  |
| Site: UCSD (vs UAB) | +0.3394 | 1.3750 | ±2.7500 | +0.247 | 0.8050 |  |
| Site: UW (vs UAB) | -2.2850 | 1.2049 | ±2.4098 | -1.896 | 0.0579 | . |
| **Age (years)** | **-0.2434** | 0.0489 | ±0.0978 | **-4.979** | **6.40e-07** | *** |
| **BMI (kg/m2)** | **+0.4357** | 0.0855 | ±0.1711 | **+5.094** | **3.51e-07** | *** |
| Hypertension | +0.0331 | 1.1479 | ±2.2958 | +0.029 | 0.9770 |  |
| High cholesterol | -0.0389 | 1.0585 | ±2.1170 | -0.037 | 0.9707 |  |
| Kidney disease | +1.2618 | 2.2587 | ±4.5174 | +0.559 | 0.5764 |  |
| Circulatory disease | -0.1758 | 1.5654 | ±3.1308 | -0.112 | 0.9106 |  |
| Time 54-69, pooled (%) | -0.0776 | 0.3633 | ±0.7266 | -0.214 | 0.8309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1130**, R² = **0.0817**, Adj R² = **0.0727**, F-statistic = **9.04** (p = **1.28e-15**), Residual SE = **16.667** on **1118** df, AIC = **9577.1**, BIC = **9637.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.6292** | 4.4566 | ±8.9131 | **+11.809** | **3.49e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6935** | 1.0681 | ±2.1362 | **-2.522** | **0.0117** | * |
| Education: high school or below (vs college) | +0.4899 | 1.9762 | ±3.9525 | +0.248 | 0.8042 |  |
| Site: UCSD (vs UAB) | +0.3323 | 1.3725 | ±2.7450 | +0.242 | 0.8087 |  |
| Site: UW (vs UAB) | -2.3005 | 1.2031 | ±2.4063 | -1.912 | 0.0559 | . |
| **Age (years)** | **-0.2434** | 0.0488 | ±0.0976 | **-4.986** | **6.17e-07** | *** |
| **BMI (kg/m2)** | **+0.4358** | 0.0856 | ±0.1711 | **+5.093** | **3.52e-07** | *** |
| Hypertension | +0.0259 | 1.1484 | ±2.2968 | +0.023 | 0.9820 |  |
| High cholesterol | -0.0457 | 1.0580 | ±2.1159 | -0.043 | 0.9656 |  |
| Kidney disease | +1.2591 | 2.2578 | ±4.5155 | +0.558 | 0.5771 |  |
| Circulatory disease | -0.1776 | 1.5656 | ±3.1312 | -0.113 | 0.9097 |  |
| Avg. daily time 54-69 (%) | -0.1230 | 0.3839 | ±0.7677 | -0.321 | 0.7486 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.34e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.2**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5652** | 4.4709 | ±8.9418 | **+11.757** | **6.49e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6800** | 1.0674 | ±2.1347 | **-2.511** | **0.0120** | * |
| Education: high school or below (vs college) | +0.5191 | 1.9742 | ±3.9484 | +0.263 | 0.7926 |  |
| Site: UCSD (vs UAB) | +0.3426 | 1.3778 | ±2.7556 | +0.249 | 0.8036 |  |
| Site: UW (vs UAB) | -2.2791 | 1.2065 | ±2.4130 | -1.889 | 0.0589 | . |
| **Age (years)** | **-0.2432** | 0.0489 | ±0.0978 | **-4.977** | **6.47e-07** | *** |
| **BMI (kg/m2)** | **+0.4355** | 0.0855 | ±0.1711 | **+5.091** | **3.56e-07** | *** |
| Hypertension | +0.0354 | 1.1481 | ±2.2961 | +0.031 | 0.9754 |  |
| High cholesterol | -0.0360 | 1.0588 | ±2.1177 | -0.034 | 0.9728 |  |
| Kidney disease | +1.2643 | 2.2592 | ±4.5184 | +0.560 | 0.5758 |  |
| Circulatory disease | -0.1758 | 1.5652 | ±3.1303 | -0.112 | 0.9106 |  |
| Time < 70 (%) | -0.0423 | 0.2782 | ±0.5563 | -0.152 | 0.8791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1130**, R² = **0.0817**, Adj R² = **0.0727**, F-statistic = **9.04** (p = **1.28e-15**), Residual SE = **16.667** on **1118** df, AIC = **9577.1**, BIC = **9637.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.6318** | 4.4571 | ±8.9143 | **+11.808** | **3.53e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6927** | 1.0681 | ±2.1361 | **-2.521** | **0.0117** | * |
| Education: high school or below (vs college) | +0.4905 | 1.9769 | ±3.9538 | +0.248 | 0.8040 |  |
| Site: UCSD (vs UAB) | +0.3240 | 1.3737 | ±2.7475 | +0.236 | 0.8135 |  |
| Site: UW (vs UAB) | -2.3063 | 1.2045 | ±2.4091 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.2433** | 0.0488 | ±0.0976 | **-4.986** | **6.17e-07** | *** |
| **BMI (kg/m2)** | **+0.4356** | 0.0856 | ±0.1711 | **+5.091** | **3.55e-07** | *** |
| Hypertension | +0.0240 | 1.1489 | ±2.2978 | +0.021 | 0.9834 |  |
| High cholesterol | -0.0487 | 1.0582 | ±2.1163 | -0.046 | 0.9633 |  |
| Kidney disease | +1.2628 | 2.2581 | ±4.5161 | +0.559 | 0.5760 |  |
| Circulatory disease | -0.1786 | 1.5654 | ±3.1308 | -0.114 | 0.9092 |  |
| Avg. daily time < 70 (%) | -0.1033 | 0.3251 | ±0.6502 | -0.318 | 0.7506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0738**, F-statistic = **9.17** (p = **6.99e-16**), Residual SE = **16.657** on **1118** df, AIC = **9575.8**, BIC = **9636.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.7009** | 21.2201 | ±42.4402 | **+3.096** | **0.0020** | ** |
| **Education: graduate level (vs college)** | **-2.6678** | 1.0710 | ±2.1420 | **-2.491** | **0.0127** | * |
| Education: high school or below (vs college) | +0.4504 | 1.9629 | ±3.9257 | +0.229 | 0.8185 |  |
| Site: UCSD (vs UAB) | +0.3836 | 1.3807 | ±2.7614 | +0.278 | 0.7812 |  |
| Site: UW (vs UAB) | -2.2457 | 1.2010 | ±2.4020 | -1.870 | 0.0615 | . |
| **Age (years)** | **-0.2415** | 0.0488 | ±0.0977 | **-4.946** | **7.57e-07** | *** |
| **BMI (kg/m2)** | **+0.4350** | 0.0858 | ±0.1715 | **+5.073** | **3.92e-07** | *** |
| Hypertension | +0.0531 | 1.1530 | ±2.3060 | +0.046 | 0.9632 |  |
| High cholesterol | -0.0323 | 1.0605 | ±2.1211 | -0.030 | 0.9757 |  |
| Kidney disease | +1.2121 | 2.2701 | ±4.5401 | +0.534 | 0.5934 |  |
| Circulatory disease | -0.2492 | 1.5657 | ±3.1314 | -0.159 | 0.8735 |  |
| Time 54-250, pooled (%) | -0.1336 | 0.2101 | ±0.4202 | -0.636 | 0.5248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0827**, Adj R² = **0.0737**, F-statistic = **9.16** (p = **7.36e-16**), Residual SE = **16.658** on **1118** df, AIC = **9575.9**, BIC = **9636.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.6913** | 22.3930 | ±44.7859 | **+2.934** | **0.0034** | ** |
| **Education: graduate level (vs college)** | **-2.6678** | 1.0712 | ±2.1423 | **-2.491** | **0.0128** | * |
| Education: high school or below (vs college) | +0.4515 | 1.9638 | ±3.9276 | +0.230 | 0.8181 |  |
| Site: UCSD (vs UAB) | +0.3748 | 1.3800 | ±2.7600 | +0.272 | 0.7859 |  |
| Site: UW (vs UAB) | -2.2520 | 1.2014 | ±2.4027 | -1.875 | 0.0609 | . |
| **Age (years)** | **-0.2418** | 0.0488 | ±0.0976 | **-4.953** | **7.32e-07** | *** |
| **BMI (kg/m2)** | **+0.4346** | 0.0857 | ±0.1715 | **+5.069** | **4.00e-07** | *** |
| Hypertension | +0.0541 | 1.1533 | ±2.3066 | +0.047 | 0.9626 |  |
| High cholesterol | -0.0355 | 1.0609 | ±2.1217 | -0.033 | 0.9733 |  |
| Kidney disease | +1.2177 | 2.2699 | ±4.5398 | +0.536 | 0.5916 |  |
| Circulatory disease | -0.2445 | 1.5659 | ±3.1317 | -0.156 | 0.8759 |  |
| Avg. daily time 54-250 (%) | -0.1331 | 0.2214 | ±0.4429 | -0.601 | 0.5478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1130**, R² = **0.0832**, Adj R² = **0.0742**, F-statistic = **9.23** (p = **5.42e-16**), Residual SE = **16.653** on **1118** df, AIC = **9575.2**, BIC = **9635.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4550** | 4.4040 | ±8.8080 | **+11.911** | **1.04e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7277** | 1.0672 | ±2.1343 | **-2.556** | **0.0106** | * |
| Education: high school or below (vs college) | +0.5189 | 1.9688 | ±3.9376 | +0.264 | 0.7921 |  |
| Site: UCSD (vs UAB) | +0.3807 | 1.3730 | ±2.7459 | +0.277 | 0.7816 |  |
| Site: UW (vs UAB) | -2.3471 | 1.2030 | ±2.4061 | -1.951 | 0.0511 | . |
| **Age (years)** | **-0.2442** | 0.0487 | ±0.0974 | **-5.016** | **5.28e-07** | *** |
| **BMI (kg/m2)** | **+0.4322** | 0.0855 | ±0.1710 | **+5.055** | **4.31e-07** | *** |
| Hypertension | -0.0961 | 1.1522 | ±2.3043 | -0.083 | 0.9335 |  |
| High cholesterol | -0.1501 | 1.0574 | ±2.1148 | -0.142 | 0.8871 |  |
| Kidney disease | +1.0402 | 2.2566 | ±4.5133 | +0.461 | 0.6448 |  |
| Circulatory disease | -0.2078 | 1.5615 | ±3.1230 | -0.133 | 0.8941 |  |
| Time 181-250, pooled (%) | +0.1195 | 0.0974 | ±0.1949 | +1.227 | 0.2199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0831**, Adj R² = **0.0740**, F-statistic = **9.21** (p = **5.99e-16**), Residual SE = **16.655** on **1118** df, AIC = **9575.5**, BIC = **9635.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4675** | 4.4036 | ±8.8072 | **+11.915** | **9.93e-33** | *** |
| **Education: graduate level (vs college)** | **-2.7276** | 1.0676 | ±2.1352 | **-2.555** | **0.0106** | * |
| Education: high school or below (vs college) | +0.5289 | 1.9681 | ±3.9362 | +0.269 | 0.7881 |  |
| Site: UCSD (vs UAB) | +0.3898 | 1.3735 | ±2.7469 | +0.284 | 0.7766 |  |
| Site: UW (vs UAB) | -2.3339 | 1.2029 | ±2.4057 | -1.940 | 0.0523 | . |
| **Age (years)** | **-0.2439** | 0.0487 | ±0.0974 | **-5.011** | **5.40e-07** | *** |
| **BMI (kg/m2)** | **+0.4320** | 0.0854 | ±0.1709 | **+5.057** | **4.26e-07** | *** |
| Hypertension | -0.0886 | 1.1519 | ±2.3038 | -0.077 | 0.9387 |  |
| High cholesterol | -0.1447 | 1.0574 | ±2.1149 | -0.137 | 0.8912 |  |
| Kidney disease | +1.0518 | 2.2573 | ±4.5145 | +0.466 | 0.6413 |  |
| Circulatory disease | -0.2106 | 1.5620 | ±3.1239 | -0.135 | 0.8927 |  |
| Avg. daily time 181-250 (%) | +0.1116 | 0.0957 | ±0.1915 | +1.165 | 0.2439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1130**, R² = **0.0838**, Adj R² = **0.0747**, F-statistic = **9.29** (p = **4.09e-16**), Residual SE = **16.649** on **1118** df, AIC = **9574.6**, BIC = **9635.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3958** | 4.4080 | ±8.8161 | **+11.886** | **1.39e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7152** | 1.0675 | ±2.1350 | **-2.544** | **0.0110** | * |
| Education: high school or below (vs college) | +0.4511 | 1.9565 | ±3.9129 | +0.231 | 0.8177 |  |
| Site: UCSD (vs UAB) | +0.3721 | 1.3755 | ±2.7510 | +0.271 | 0.7868 |  |
| Site: UW (vs UAB) | -2.3340 | 1.2016 | ±2.4032 | -1.942 | 0.0521 | . |
| **Age (years)** | **-0.2430** | 0.0487 | ±0.0973 | **-4.993** | **5.94e-07** | *** |
| **BMI (kg/m2)** | **+0.4324** | 0.0856 | ±0.1712 | **+5.053** | **4.36e-07** | *** |
| Hypertension | -0.0642 | 1.1510 | ±2.3019 | -0.056 | 0.9555 |  |
| High cholesterol | -0.1384 | 1.0605 | ±2.1209 | -0.131 | 0.8961 |  |
| Kidney disease | +1.0536 | 2.2669 | ±4.5337 | +0.465 | 0.6421 |  |
| Circulatory disease | -0.2535 | 1.5577 | ±3.1154 | -0.163 | 0.8707 |  |
| Time > 180 (%) | +0.0951 | 0.0831 | ±0.1661 | +1.145 | 0.2523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1130**, R² = **0.0836**, Adj R² = **0.0745**, F-statistic = **9.27** (p = **4.57e-16**), Residual SE = **16.651** on **1118** df, AIC = **9574.9**, BIC = **9635.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4197** | 4.4072 | ±8.8144 | **+11.894** | **1.27e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7161** | 1.0677 | ±2.1354 | **-2.544** | **0.0110** | * |
| Education: high school or below (vs college) | +0.4653 | 1.9573 | ±3.9147 | +0.238 | 0.8121 |  |
| Site: UCSD (vs UAB) | +0.3800 | 1.3759 | ±2.7517 | +0.276 | 0.7824 |  |
| Site: UW (vs UAB) | -2.3263 | 1.2017 | ±2.4035 | -1.936 | 0.0529 | . |
| **Age (years)** | **-0.2429** | 0.0487 | ±0.0973 | **-4.991** | **6.00e-07** | *** |
| **BMI (kg/m2)** | **+0.4321** | 0.0855 | ±0.1710 | **+5.052** | **4.37e-07** | *** |
| Hypertension | -0.0596 | 1.1511 | ±2.3021 | -0.052 | 0.9587 |  |
| High cholesterol | -0.1349 | 1.0605 | ±2.1211 | -0.127 | 0.8987 |  |
| Kidney disease | +1.0638 | 2.2669 | ±4.5338 | +0.469 | 0.6389 |  |
| Circulatory disease | -0.2517 | 1.5584 | ±3.1168 | -0.162 | 0.8717 |  |
| Avg. daily time > 180 (%) | +0.0903 | 0.0824 | ±0.1649 | +1.095 | 0.2733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.36e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.3**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4937** | 4.4287 | ±8.8574 | **+11.853** | **2.08e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6721** | 1.0687 | ±2.1375 | **-2.500** | **0.0124** | * |
| Education: high school or below (vs college) | +0.5362 | 1.9768 | ±3.9535 | +0.271 | 0.7862 |  |
| Site: UCSD (vs UAB) | +0.3650 | 1.3741 | ±2.7481 | +0.266 | 0.7905 |  |
| Site: UW (vs UAB) | -2.2605 | 1.2052 | ±2.4104 | -1.876 | 0.0607 | . |
| **Age (years)** | **-0.2429** | 0.0488 | ±0.0976 | **-4.977** | **6.47e-07** | *** |
| **BMI (kg/m2)** | **+0.4349** | 0.0864 | ±0.1728 | **+5.034** | **4.81e-07** | *** |
| Hypertension | +0.0403 | 1.1517 | ±2.3033 | +0.035 | 0.9721 |  |
| High cholesterol | -0.0302 | 1.0628 | ±2.1256 | -0.028 | 0.9773 |  |
| Kidney disease | +1.2621 | 2.2627 | ±4.5254 | +0.558 | 0.5770 |  |
| Circulatory disease | -0.1764 | 1.5705 | ±3.1410 | -0.112 | 0.9106 |  |
| Nocturnal time > 180 (%) | +0.0041 | 0.0931 | ±0.1863 | +0.044 | 0.9651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0738**, F-statistic = **9.18** (p = **6.90e-16**), Residual SE = **16.657** on **1118** df, AIC = **9575.8**, BIC = **9636.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0525** | 4.4441 | ±8.8882 | **+11.713** | **1.10e-31** | *** |
| **Education: graduate level (vs college)** | **-2.6781** | 1.0665 | ±2.1329 | **-2.511** | **0.0120** | * |
| Education: high school or below (vs college) | +0.5320 | 1.9704 | ±3.9408 | +0.270 | 0.7872 |  |
| Site: UCSD (vs UAB) | +0.3623 | 1.3719 | ±2.7438 | +0.264 | 0.7917 |  |
| Site: UW (vs UAB) | -2.2913 | 1.2037 | ±2.4074 | -1.904 | 0.0570 | . |
| **Age (years)** | **-0.2431** | 0.0488 | ±0.0975 | **-4.985** | **6.19e-07** | *** |
| **BMI (kg/m2)** | **+0.4432** | 0.0863 | ±0.1725 | **+5.138** | **2.78e-07** | *** |
| Hypertension | -0.0552 | 1.1511 | ±2.3022 | -0.048 | 0.9618 |  |
| High cholesterol | -0.0784 | 1.0581 | ±2.1162 | -0.074 | 0.9409 |  |
| Kidney disease | +1.2058 | 2.2585 | ±4.5171 | +0.534 | 0.5934 |  |
| Circulatory disease | -0.1605 | 1.5647 | ±3.1294 | -0.103 | 0.9183 |  |
| Any reading > 250 during wear (0/1) | +1.5444 | 1.2728 | ±2.5456 | +1.213 | 0.2250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0738**, F-statistic = **9.17** (p = **6.99e-16**), Residual SE = **16.657** on **1118** df, AIC = **9575.8**, BIC = **9636.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3968** | 4.4249 | ±8.8499 | **+11.841** | **2.39e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6709** | 1.0709 | ±2.1417 | **-2.494** | **0.0126** | * |
| Education: high school or below (vs college) | +0.4370 | 1.9638 | ±3.9277 | +0.223 | 0.8239 |  |
| Site: UCSD (vs UAB) | +0.3572 | 1.3785 | ±2.7571 | +0.259 | 0.7955 |  |
| Site: UW (vs UAB) | -2.2655 | 1.2014 | ±2.4029 | -1.886 | 0.0593 | . |
| **Age (years)** | **-0.2416** | 0.0488 | ±0.0976 | **-4.950** | **7.41e-07** | *** |
| **BMI (kg/m2)** | **+0.4348** | 0.0857 | ±0.1715 | **+5.072** | **3.94e-07** | *** |
| Hypertension | +0.0474 | 1.1528 | ±2.3057 | +0.041 | 0.9672 |  |
| High cholesterol | -0.0442 | 1.0611 | ±2.1222 | -0.042 | 0.9668 |  |
| Kidney disease | +1.2176 | 2.2702 | ±4.5404 | +0.536 | 0.5917 |  |
| Circulatory disease | -0.2497 | 1.5659 | ±3.1317 | -0.159 | 0.8733 |  |
| Time > 250 (%) | +0.1345 | 0.2143 | ±0.4287 | +0.628 | 0.5303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0737**, F-statistic = **9.17** (p = **7.13e-16**), Residual SE = **16.658** on **1118** df, AIC = **9575.8**, BIC = **9636.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4116** | 4.4245 | ±8.8491 | **+11.846** | **2.27e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6711** | 1.0710 | ±2.1419 | **-2.494** | **0.0126** | * |
| Education: high school or below (vs college) | +0.4392 | 1.9641 | ±3.9282 | +0.224 | 0.8230 |  |
| Site: UCSD (vs UAB) | +0.3572 | 1.3786 | ±2.7571 | +0.259 | 0.7956 |  |
| Site: UW (vs UAB) | -2.2685 | 1.2017 | ±2.4034 | -1.888 | 0.0591 | . |
| **Age (years)** | **-0.2417** | 0.0488 | ±0.0976 | **-4.952** | **7.36e-07** | *** |
| **BMI (kg/m2)** | **+0.4345** | 0.0857 | ±0.1715 | **+5.068** | **4.02e-07** | *** |
| Hypertension | +0.0483 | 1.1531 | ±2.3062 | +0.042 | 0.9666 |  |
| High cholesterol | -0.0444 | 1.0613 | ±2.1225 | -0.042 | 0.9666 |  |
| Kidney disease | +1.2203 | 2.2700 | ±4.5399 | +0.538 | 0.5909 |  |
| Circulatory disease | -0.2483 | 1.5658 | ±3.1315 | -0.159 | 0.8740 |  |
| Avg. daily time > 250 (%) | +0.1372 | 0.2230 | ±0.4459 | +0.615 | 0.5384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Wearable activity

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 155 single-predictor tests; 33 with raw p < 0.05 (about 8 expected by chance); FDR rule applied to 155 tests (samples with n >= 500), of which **11** are significant at BH q < 0.05 in the all-tests family and 22 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Steps per wear-day** (n = 1,125): best single predictor out of sample is **MAG** (CV R² 0.116 vs 0.108 for covariates alone, gain +0.008; +432 per SD, p = 2.3e-04, q = 0.013). FDR-robust associations (1): MAG (higher outcome, +432 per SD, q = 0.013).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 1,125): best single predictor out of sample is **MAG** (CV R² 0.136 vs 0.124 for covariates alone, gain +0.011; +1.53 per SD, p = 5.7e-05, q = 0.007). FDR-robust associations (1): MAG (higher outcome, +1.53 per SD, q = 0.007).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 1,128): best single predictor out of sample is **SD of daily means** (CV R² 0.113 vs 0.104 for covariates alone, gain +0.009; +0.932 per SD, p = 7.8e-05, q = 0.007). FDR-robust associations (7): SD of daily means (higher outcome, +0.932 per SD, q = 0.007); HbA1c (higher outcome, +0.818 per SD, q = 0.010); SD (pooled) (higher outcome, +0.809 per SD, q = 0.025); MAG (higher outcome, +0.787 per SD, q = 0.029); Mean glucose (higher outcome, +0.802 per SD, q = 0.036); GMI (higher outcome, +0.802 per SD, q = 0.036); ....
- **Total sleep time per night (min)** (n = 1,137): best single predictor out of sample is **MAG** (CV R² 0.010 vs -0.005 for covariates alone, gain +0.015; -8.28 per SD, p = 3.7e-05, q = 0.007). FDR-robust associations (1): MAG (lower outcome, -8.28 per SD, q = 0.007).
- **Garmin stress score, mean (0-100)** (n = 1,130): best single predictor out of sample is **HbA1c** (CV R² 0.056 vs 0.051 for covariates alone, gain +0.006; +1.58 per SD, p = 0.001, q = 0.036). FDR-robust associations (1): HbA1c (higher outcome, +1.58 per SD, q = 0.036).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Total sleep time per night (min) (+0.015, via MAG); Brisk-cadence minutes per day (>= 100 steps/min) (+0.011, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.009, via SD of daily means); Steps per wear-day (+0.008, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (7 FDR-significant / 19 raw-significant of 40); HbA1c (2 FDR-significant / 5 raw-significant of 5); CGM level (2 FDR-significant / 3 raw-significant of 15).
Level metrics: 2 FDR-significant (3 raw); variability metrics: 7 FDR-significant (19 raw); HbA1c alone: 2 FDR-significant (5 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Steps per wear-day (MAG, ΔAIC -9.6); Brisk-cadence minutes per day (MAG, ΔAIC -13.5); Resting heart-rate proxy (SD of daily means, ΔAIC -4.6); Total sleep time per night (MAG, ΔAIC -14.3).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
