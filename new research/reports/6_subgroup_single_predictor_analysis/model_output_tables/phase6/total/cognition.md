# Phase 6 model output tables - All (analysis base) - Total analysis base - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 2,138; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2138**, R² = **0.1044**, Adj R² = **0.1002**, F-statistic = **24.80** (p = **7.63e-45**), Residual SE = **2.981** on **2127** df, AIC = **10748.6**, BIC = **10810.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3540** | 0.5238 | ±1.0477 | **+56.037** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8076** | 0.1350 | ±0.2700 | **+5.983** | **2.19e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6636** | 0.2786 | ±0.5572 | **-5.972** | **2.35e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4553** | 0.1714 | ±0.3428 | **-2.656** | **0.0079** | ** |
| Site: UW (vs UAB) | -0.2152 | 0.1631 | ±0.3262 | -1.319 | 0.1871 |  |
| **Age (years)** | **-0.0515** | 0.0065 | ±0.0129 | **-7.959** | **1.73e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0182 | -1.220 | 0.2223 |  |
| **Hypertension** | **-0.4966** | 0.1447 | ±0.2894 | **-3.432** | **6.00e-04** | *** |
| High cholesterol | +0.2659 | 0.1380 | ±0.2759 | +1.927 | 0.0540 | . |
| Kidney disease | +0.0360 | 0.2352 | ±0.4704 | +0.153 | 0.8782 |  |
| Circulatory disease | -0.1698 | 0.1840 | ±0.3679 | -0.923 | 0.3559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2138**, R² = **0.1155**, Adj R² = **0.1109**, F-statistic = **25.24** (p = **1.09e-49**), Residual SE = **2.963** on **2126** df, AIC = **10723.9**, BIC = **10791.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.0366** | 0.6439 | ±1.2878 | **+48.200** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7663** | 0.1346 | ±0.2692 | **+5.693** | **1.25e-08** | *** |
| **Education: high school or below (vs college)** | **-1.5356** | 0.2772 | ±0.5544 | **-5.540** | **3.02e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.4860** | 0.1709 | ±0.3417 | **-2.845** | **0.0044** | ** |
| Site: UW (vs UAB) | -0.2572 | 0.1626 | ±0.3252 | -1.582 | 0.1137 |  |
| **Age (years)** | **-0.0497** | 0.0064 | ±0.0128 | **-7.761** | **8.43e-15** | *** |
| BMI (kg/m2) | -0.0052 | 0.0093 | ±0.0185 | -0.565 | 0.5722 |  |
| **Hypertension** | **-0.4262** | 0.1439 | ±0.2878 | **-2.962** | **0.0031** | ** |
| **High cholesterol** | **+0.3269** | 0.1385 | ±0.2769 | **+2.361** | **0.0182** | * |
| Kidney disease | +0.0935 | 0.2343 | ±0.4686 | +0.399 | 0.6899 |  |
| Circulatory disease | -0.1400 | 0.1834 | ±0.3668 | -0.763 | 0.4454 |  |
| **HbA1c (%)** | **-0.3310** | 0.0705 | ±0.1410 | **-4.693** | **2.69e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2138**, R² = **0.1202**, Adj R² = **0.1156**, F-statistic = **26.40** (p = **4.61e-52**), Residual SE = **2.955** on **2126** df, AIC = **10712.6**, BIC = **10780.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.6664** | 0.5708 | ±1.1415 | **+53.729** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7799** | 0.1339 | ±0.2678 | **+5.824** | **5.74e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5238** | 0.2761 | ±0.5522 | **-5.519** | **3.41e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5071** | 0.1701 | ±0.3402 | **-2.981** | **0.0029** | ** |
| Site: UW (vs UAB) | -0.2442 | 0.1614 | ±0.3229 | -1.512 | 0.1304 |  |
| **Age (years)** | **-0.0497** | 0.0064 | ±0.0129 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | -0.0065 | 0.0092 | ±0.0184 | -0.703 | 0.4822 |  |
| **Hypertension** | **-0.4150** | 0.1439 | ±0.2877 | **-2.885** | **0.0039** | ** |
| **High cholesterol** | **+0.3153** | 0.1380 | ±0.2761 | **+2.284** | **0.0223** | * |
| Kidney disease | +0.1691 | 0.2353 | ±0.4706 | +0.719 | 0.4723 |  |
| Circulatory disease | -0.1326 | 0.1818 | ±0.3636 | -0.729 | 0.4659 |  |
| **Mean glucose (mg/dL)** | **-0.0121** | 0.0022 | ±0.0044 | **-5.441** | **5.30e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2138**, R² = **0.1202**, Adj R² = **0.1156**, F-statistic = **26.40** (p = **4.61e-52**), Residual SE = **2.955** on **2126** df, AIC = **10712.6**, BIC = **10780.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.3392** | 0.7491 | ±1.4983 | **+43.169** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7799** | 0.1339 | ±0.2678 | **+5.824** | **5.74e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5238** | 0.2761 | ±0.5522 | **-5.519** | **3.41e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5071** | 0.1701 | ±0.3402 | **-2.981** | **0.0029** | ** |
| Site: UW (vs UAB) | -0.2442 | 0.1614 | ±0.3229 | -1.512 | 0.1304 |  |
| **Age (years)** | **-0.0497** | 0.0064 | ±0.0129 | **-7.725** | **1.12e-14** | *** |
| BMI (kg/m2) | -0.0065 | 0.0092 | ±0.0184 | -0.703 | 0.4822 |  |
| **Hypertension** | **-0.4150** | 0.1439 | ±0.2877 | **-2.885** | **0.0039** | ** |
| **High cholesterol** | **+0.3153** | 0.1380 | ±0.2761 | **+2.284** | **0.0223** | * |
| Kidney disease | +0.1691 | 0.2353 | ±0.4706 | +0.719 | 0.4723 |  |
| Circulatory disease | -0.1326 | 0.1818 | ±0.3636 | -0.729 | 0.4659 |  |
| **GMI (%)** | **-0.5054** | 0.0929 | ±0.1858 | **-5.441** | **5.30e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2138**, R² = **0.1184**, Adj R² = **0.1138**, F-statistic = **25.95** (p = **3.95e-51**), Residual SE = **2.958** on **2126** df, AIC = **10717.0**, BIC = **10785.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.5899** | 0.5743 | ±1.1485 | **+53.268** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7783** | 0.1339 | ±0.2679 | **+5.810** | **6.24e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5385** | 0.2758 | ±0.5517 | **-5.577** | **2.44e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.4910** | 0.1703 | ±0.3407 | **-2.882** | **0.0039** | ** |
| Site: UW (vs UAB) | -0.2304 | 0.1617 | ±0.3235 | -1.424 | 0.1543 |  |
| **Age (years)** | **-0.0514** | 0.0065 | ±0.0129 | **-7.968** | **1.61e-15** | *** |
| BMI (kg/m2) | -0.0042 | 0.0093 | ±0.0186 | -0.450 | 0.6530 |  |
| **Hypertension** | **-0.4363** | 0.1440 | ±0.2880 | **-3.030** | **0.0024** | ** |
| **High cholesterol** | **+0.3157** | 0.1382 | ±0.2765 | **+2.284** | **0.0224** | * |
| Kidney disease | +0.1221 | 0.2338 | ±0.4676 | +0.522 | 0.6014 |  |
| Circulatory disease | -0.1416 | 0.1815 | ±0.3630 | -0.780 | 0.4354 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0114** | 0.0023 | ±0.0045 | **-5.033** | **4.83e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2138**, R² = **0.1187**, Adj R² = **0.1142**, F-statistic = **26.04** (p = **2.52e-51**), Residual SE = **2.958** on **2126** df, AIC = **10716.1**, BIC = **10784.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9210** | 0.5321 | ±1.0641 | **+56.237** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7628** | 0.1339 | ±0.2678 | **+5.696** | **1.23e-08** | *** |
| **Education: high school or below (vs college)** | **-1.5439** | 0.2753 | ±0.5506 | **-5.608** | **2.04e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5206** | 0.1708 | ±0.3415 | **-3.049** | **0.0023** | ** |
| Site: UW (vs UAB) | -0.2718 | 0.1625 | ±0.3250 | -1.672 | 0.0945 | . |
| **Age (years)** | **-0.0484** | 0.0065 | ±0.0129 | **-7.484** | **7.21e-14** | *** |
| BMI (kg/m2) | -0.0080 | 0.0092 | ±0.0185 | -0.870 | 0.3845 |  |
| **Hypertension** | **-0.4068** | 0.1432 | ±0.2865 | **-2.840** | **0.0045** | ** |
| **High cholesterol** | **+0.3007** | 0.1375 | ±0.2749 | **+2.187** | **0.0287** | * |
| Kidney disease | +0.2501 | 0.2346 | ±0.4692 | +1.066 | 0.2864 |  |
| Circulatory disease | -0.1304 | 0.1831 | ±0.3662 | -0.712 | 0.4763 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0331** | 0.0061 | ±0.0122 | **-5.433** | **5.53e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2138**, R² = **0.1181**, Adj R² = **0.1136**, F-statistic = **25.89** (p = **5.17e-51**), Residual SE = **2.959** on **2126** df, AIC = **10717.6**, BIC = **10785.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9135** | 0.5305 | ±1.0610 | **+56.389** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7684** | 0.1340 | ±0.2681 | **+5.733** | **9.86e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5422** | 0.2759 | ±0.5518 | **-5.590** | **2.27e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5154** | 0.1706 | ±0.3411 | **-3.021** | **0.0025** | ** |
| Site: UW (vs UAB) | -0.2638 | 0.1625 | ±0.3249 | -1.624 | 0.1044 |  |
| **Age (years)** | **-0.0481** | 0.0065 | ±0.0130 | **-7.423** | **1.14e-13** | *** |
| BMI (kg/m2) | -0.0087 | 0.0092 | ±0.0184 | -0.943 | 0.3459 |  |
| **Hypertension** | **-0.4101** | 0.1434 | ±0.2868 | **-2.860** | **0.0042** | ** |
| **High cholesterol** | **+0.3007** | 0.1376 | ±0.2752 | **+2.185** | **0.0289** | * |
| Kidney disease | +0.2500 | 0.2351 | ±0.4702 | +1.063 | 0.2876 |  |
| Circulatory disease | -0.1371 | 0.1833 | ±0.3667 | -0.748 | 0.4547 |  |
| **Avg. daily SD (mg/dL)** | **-0.0365** | 0.0069 | ±0.0137 | **-5.324** | **1.01e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2138**, R² = **0.1092**, Adj R² = **0.1046**, F-statistic = **23.70** (p = **1.55e-46**), Residual SE = **2.973** on **2126** df, AIC = **10739.0**, BIC = **10807.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.0365** | 0.5595 | ±1.1190 | **+53.684** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7823** | 0.1344 | ±0.2689 | **+5.819** | **5.92e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6242** | 0.2776 | ±0.5552 | **-5.851** | **4.88e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4929** | 0.1720 | ±0.3439 | **-2.866** | **0.0042** | ** |
| Site: UW (vs UAB) | -0.2508 | 0.1638 | ±0.3277 | -1.530 | 0.1259 |  |
| **Age (years)** | **-0.0494** | 0.0065 | ±0.0130 | **-7.595** | **3.08e-14** | *** |
| BMI (kg/m2) | -0.0106 | 0.0091 | ±0.0183 | -1.157 | 0.2471 |  |
| **Hypertension** | **-0.4525** | 0.1438 | ±0.2876 | **-3.147** | **0.0016** | ** |
| **High cholesterol** | **+0.2710** | 0.1377 | ±0.2754 | **+1.968** | **0.0491** | * |
| Kidney disease | +0.1533 | 0.2343 | ±0.4685 | +0.654 | 0.5129 |  |
| Circulatory disease | -0.1525 | 0.1846 | ±0.3692 | -0.826 | 0.4089 |  |
| **CV (%)** | **-0.0425** | 0.0129 | ±0.0258 | **-3.296** | **9.82e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2138**, R² = **0.1091**, Adj R² = **0.1045**, F-statistic = **23.68** (p = **1.73e-46**), Residual SE = **2.974** on **2126** df, AIC = **10739.3**, BIC = **10807.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.3054** | 0.6198 | ±1.2397 | **+45.666** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7826** | 0.1345 | ±0.2689 | **+5.821** | **5.87e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6215** | 0.2773 | ±0.5547 | **-5.846** | **5.02e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4870** | 0.1717 | ±0.3433 | **-2.837** | **0.0046** | ** |
| Site: UW (vs UAB) | -0.2394 | 0.1635 | ±0.3270 | -1.464 | 0.1432 |  |
| **Age (years)** | **-0.0494** | 0.0065 | ±0.0130 | **-7.615** | **2.64e-14** | *** |
| BMI (kg/m2) | -0.0106 | 0.0091 | ±0.0183 | -1.160 | 0.2459 |  |
| **Hypertension** | **-0.4517** | 0.1437 | ±0.2875 | **-3.142** | **0.0017** | ** |
| **High cholesterol** | **+0.2734** | 0.1377 | ±0.2754 | **+1.986** | **0.0471** | * |
| Kidney disease | +0.1262 | 0.2339 | ±0.4678 | +0.539 | 0.5895 |  |
| Circulatory disease | -0.1522 | 0.1843 | ±0.3687 | -0.826 | 0.4090 |  |
| **Mean / SD ratio** | **+0.1638** | 0.0506 | ±0.1013 | **+3.234** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2138**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.39** (p = **6.67e-46**), Residual SE = **2.976** on **2126** df, AIC = **10742.1**, BIC = **10810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4535** | 0.6197 | ±1.2393 | **+45.918** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7893** | 0.1347 | ±0.2694 | **+5.859** | **4.66e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6261** | 0.2780 | ±0.5560 | **-5.849** | **4.93e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4740** | 0.1713 | ±0.3426 | **-2.767** | **0.0057** | ** |
| Site: UW (vs UAB) | -0.2309 | 0.1633 | ±0.3267 | -1.414 | 0.1574 |  |
| **Age (years)** | **-0.0494** | 0.0065 | ±0.0130 | **-7.594** | **3.11e-14** | *** |
| BMI (kg/m2) | -0.0107 | 0.0091 | ±0.0183 | -1.172 | 0.2412 |  |
| **Hypertension** | **-0.4622** | 0.1441 | ±0.2882 | **-3.208** | **0.0013** | ** |
| **High cholesterol** | **+0.2707** | 0.1378 | ±0.2756 | **+1.965** | **0.0494** | * |
| Kidney disease | +0.1106 | 0.2343 | ±0.4686 | +0.472 | 0.6370 |  |
| Circulatory disease | -0.1635 | 0.1842 | ±0.3685 | -0.887 | 0.3750 |  |
| **Avg. daily mean/SD** | **+0.1192** | 0.0423 | ±0.0847 | **+2.814** | **0.0049** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2138**, R² = **0.1095**, Adj R² = **0.1049**, F-statistic = **23.76** (p = **1.16e-46**), Residual SE = **2.973** on **2126** df, AIC = **10738.4**, BIC = **10806.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3854** | 0.5956 | ±1.1912 | **+51.016** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7811** | 0.1351 | ±0.2703 | **+5.781** | **7.45e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6189** | 0.2753 | ±0.5507 | **-5.880** | **4.11e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4931** | 0.1714 | ±0.3429 | **-2.876** | **0.0040** | ** |
| Site: UW (vs UAB) | -0.2732 | 0.1634 | ±0.3268 | -1.672 | 0.0945 | . |
| **Age (years)** | **-0.0519** | 0.0065 | ±0.0129 | **-8.030** | **9.75e-16** | *** |
| BMI (kg/m2) | -0.0099 | 0.0092 | ±0.0183 | -1.081 | 0.2797 |  |
| **Hypertension** | **-0.4838** | 0.1442 | ±0.2885 | **-3.354** | **7.96e-04** | *** |
| High cholesterol | +0.2629 | 0.1378 | ±0.2757 | +1.908 | 0.0564 | . |
| Kidney disease | +0.0999 | 0.2384 | ±0.4768 | +0.419 | 0.6751 |  |
| Circulatory disease | -0.1618 | 0.1836 | ±0.3672 | -0.881 | 0.3783 |  |
| **MAG (mg/dL/h)** | **-0.0253** | 0.0077 | ±0.0154 | **-3.300** | **9.67e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2138**, R² = **0.1159**, Adj R² = **0.1113**, F-statistic = **25.33** (p = **7.21e-50**), Residual SE = **2.962** on **2126** df, AIC = **10723.1**, BIC = **10791.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1746** | 0.5430 | ±1.0861 | **+55.566** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7729** | 0.1342 | ±0.2684 | **+5.759** | **8.45e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5572** | 0.2760 | ±0.5520 | **-5.642** | **1.68e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5144** | 0.1707 | ±0.3414 | **-3.013** | **0.0026** | ** |
| Site: UW (vs UAB) | -0.2619 | 0.1626 | ±0.3251 | -1.611 | 0.1071 |  |
| **Age (years)** | **-0.0489** | 0.0065 | ±0.0130 | **-7.533** | **4.98e-14** | *** |
| BMI (kg/m2) | -0.0105 | 0.0092 | ±0.0183 | -1.149 | 0.2508 |  |
| **Hypertension** | **-0.4307** | 0.1435 | ±0.2871 | **-3.001** | **0.0027** | ** |
| **High cholesterol** | **+0.2937** | 0.1377 | ±0.2753 | **+2.133** | **0.0329** | * |
| Kidney disease | +0.2191 | 0.2352 | ±0.4704 | +0.932 | 0.3516 |  |
| Circulatory disease | -0.1365 | 0.1839 | ±0.3678 | -0.742 | 0.4579 |  |
| **Avg. daily range (mg/dL)** | **-0.0090** | 0.0019 | ±0.0037 | **-4.825** | **1.40e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2138**, R² = **0.1131**, Adj R² = **0.1086**, F-statistic = **24.66** (p = **1.71e-48**), Residual SE = **2.967** on **2126** df, AIC = **10729.6**, BIC = **10797.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6218** | 0.5294 | ±1.0588 | **+55.952** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7662** | 0.1341 | ±0.2682 | **+5.714** | **1.11e-08** | *** |
| **Education: high school or below (vs college)** | **-1.6048** | 0.2742 | ±0.5485 | **-5.852** | **4.86e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4987** | 0.1719 | ±0.3438 | **-2.901** | **0.0037** | ** |
| Site: UW (vs UAB) | -0.2578 | 0.1636 | ±0.3272 | -1.576 | 0.1150 |  |
| **Age (years)** | **-0.0512** | 0.0065 | ±0.0129 | **-7.923** | **2.31e-15** | *** |
| BMI (kg/m2) | -0.0071 | 0.0092 | ±0.0184 | -0.774 | 0.4388 |  |
| **Hypertension** | **-0.4484** | 0.1437 | ±0.2874 | **-3.120** | **0.0018** | ** |
| **High cholesterol** | **+0.2938** | 0.1378 | ±0.2757 | **+2.132** | **0.0330** | * |
| Kidney disease | +0.1402 | 0.2334 | ±0.4668 | +0.601 | 0.5479 |  |
| Circulatory disease | -0.1194 | 0.1834 | ±0.3668 | -0.651 | 0.5151 |  |
| **SD of daily means (mg/dL)** | **-0.0479** | 0.0117 | ±0.0233 | **-4.108** | **3.99e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2138**, R² = **0.1162**, Adj R² = **0.1117**, F-statistic = **25.42** (p = **4.73e-50**), Residual SE = **2.962** on **2126** df, AIC = **10722.2**, BIC = **10790.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5663** | 0.6486 | ±1.2972 | **+42.501** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7721** | 0.1342 | ±0.2684 | **+5.754** | **8.70e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5489** | 0.2763 | ±0.5526 | **-5.606** | **2.07e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5229** | 0.1715 | ±0.3430 | **-3.049** | **0.0023** | ** |
| Site: UW (vs UAB) | -0.2644 | 0.1625 | ±0.3249 | -1.627 | 0.1037 |  |
| **Age (years)** | **-0.0498** | 0.0064 | ±0.0129 | **-7.736** | **1.02e-14** | *** |
| BMI (kg/m2) | -0.0072 | 0.0092 | ±0.0184 | -0.784 | 0.4333 |  |
| **Hypertension** | **-0.4449** | 0.1438 | ±0.2876 | **-3.094** | **0.0020** | ** |
| **High cholesterol** | **+0.2970** | 0.1378 | ±0.2756 | **+2.155** | **0.0311** | * |
| Kidney disease | +0.1673 | 0.2351 | ±0.4702 | +0.712 | 0.4767 |  |
| Circulatory disease | -0.1356 | 0.1823 | ±0.3646 | -0.744 | 0.4569 |  |
| **Time in range 70-180, pooled (%)** | **+0.0177** | 0.0037 | ±0.0075 | **+4.729** | **2.26e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2138**, R² = **0.1158**, Adj R² = **0.1113**, F-statistic = **25.32** (p = **7.45e-50**), Residual SE = **2.962** on **2126** df, AIC = **10723.1**, BIC = **10791.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.5922** | 0.6502 | ±1.3004 | **+42.438** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7738** | 0.1342 | ±0.2684 | **+5.765** | **8.17e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5497** | 0.2764 | ±0.5529 | **-5.606** | **2.07e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5226** | 0.1716 | ±0.3432 | **-3.045** | **0.0023** | ** |
| Site: UW (vs UAB) | -0.2637 | 0.1626 | ±0.3251 | -1.622 | 0.1047 |  |
| **Age (years)** | **-0.0498** | 0.0064 | ±0.0129 | **-7.726** | **1.11e-14** | *** |
| BMI (kg/m2) | -0.0072 | 0.0092 | ±0.0185 | -0.782 | 0.4340 |  |
| **Hypertension** | **-0.4468** | 0.1438 | ±0.2876 | **-3.107** | **0.0019** | ** |
| **High cholesterol** | **+0.2973** | 0.1379 | ±0.2757 | **+2.156** | **0.0311** | * |
| Kidney disease | +0.1675 | 0.2351 | ±0.4702 | +0.713 | 0.4760 |  |
| Circulatory disease | -0.1362 | 0.1823 | ±0.3647 | -0.747 | 0.4550 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0173** | 0.0037 | ±0.0075 | **+4.635** | **3.58e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2138**, R² = **0.1062**, Adj R² = **0.1016**, F-statistic = **22.97** (p = **4.93e-45**), Residual SE = **2.978** on **2126** df, AIC = **10746.2**, BIC = **10814.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2088** | 0.5324 | ±1.0649 | **+54.858** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8151** | 0.1349 | ±0.2698 | **+6.042** | **1.53e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6363** | 0.2801 | ±0.5602 | **-5.841** | **5.17e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4202** | 0.1741 | ±0.3483 | **-2.413** | **0.0158** | * |
| Site: UW (vs UAB) | -0.1960 | 0.1648 | ±0.3296 | -1.189 | 0.2343 |  |
| **Age (years)** | **-0.0507** | 0.0065 | ±0.0130 | **-7.814** | **5.53e-15** | *** |
| BMI (kg/m2) | -0.0118 | 0.0091 | ±0.0181 | -1.306 | 0.1916 |  |
| **Hypertension** | **-0.4993** | 0.1447 | ±0.2894 | **-3.451** | **5.58e-04** | *** |
| **High cholesterol** | **+0.2839** | 0.1383 | ±0.2765 | **+2.054** | **0.0400** | * |
| Kidney disease | +0.0454 | 0.2350 | ±0.4699 | +0.193 | 0.8469 |  |
| Circulatory disease | -0.1923 | 0.1846 | ±0.3691 | -1.042 | 0.2975 |  |
| **Any reading < 54 during wear (0/1)** | **+0.2967** | 0.1422 | ±0.2844 | **+2.086** | **0.0370** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2138**, R² = **0.1046**, Adj R² = **0.0999**, F-statistic = **22.57** (p = **3.30e-44**), Residual SE = **2.981** on **2126** df, AIC = **10750.2**, BIC = **10818.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3292** | 0.5273 | ±1.0546 | **+55.621** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8092** | 0.1351 | ±0.2702 | **+5.989** | **2.11e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6575** | 0.2788 | ±0.5577 | **-5.944** | **2.78e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4442** | 0.1731 | ±0.3462 | **-2.566** | **0.0103** | * |
| Site: UW (vs UAB) | -0.2063 | 0.1644 | ±0.3289 | -1.254 | 0.2097 |  |
| **Age (years)** | **-0.0514** | 0.0065 | ±0.0129 | **-7.942** | **1.99e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0182 | -1.221 | 0.2222 |  |
| **Hypertension** | **-0.4950** | 0.1448 | ±0.2896 | **-3.419** | **6.29e-04** | *** |
| High cholesterol | +0.2705 | 0.1384 | ±0.2767 | +1.955 | 0.0506 | . |
| Kidney disease | +0.0365 | 0.2355 | ±0.4709 | +0.155 | 0.8768 |  |
| Circulatory disease | -0.1725 | 0.1840 | ±0.3680 | -0.938 | 0.3485 |  |
| Time < 54 (%) | +0.0754 | 0.1199 | ±0.2398 | +0.629 | 0.5295 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2138**, R² = **0.1045**, Adj R² = **0.0998**, F-statistic = **22.55** (p = **3.68e-44**), Residual SE = **2.981** on **2126** df, AIC = **10750.4**, BIC = **10818.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3445** | 0.5253 | ±1.0506 | **+55.861** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8091** | 0.1351 | ±0.2702 | **+5.990** | **2.10e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6602** | 0.2789 | ±0.5578 | **-5.953** | **2.64e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4496** | 0.1727 | ±0.3455 | **-2.603** | **0.0093** | ** |
| Site: UW (vs UAB) | -0.2096 | 0.1644 | ±0.3288 | -1.275 | 0.2024 |  |
| **Age (years)** | **-0.0515** | 0.0065 | ±0.0129 | **-7.961** | **1.71e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0182 | -1.221 | 0.2221 |  |
| **Hypertension** | **-0.4955** | 0.1448 | ±0.2896 | **-3.422** | **6.21e-04** | *** |
| High cholesterol | +0.2683 | 0.1383 | ±0.2766 | +1.940 | 0.0523 | . |
| Kidney disease | +0.0359 | 0.2353 | ±0.4706 | +0.153 | 0.8788 |  |
| Circulatory disease | -0.1715 | 0.1840 | ±0.3680 | -0.932 | 0.3514 |  |
| Avg. daily time < 54 (%) | +0.0542 | 0.1529 | ±0.3059 | +0.354 | 0.7231 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2138**, R² = **0.1045**, Adj R² = **0.0998**, F-statistic = **22.55** (p = **3.71e-44**), Residual SE = **2.981** on **2126** df, AIC = **10750.5**, BIC = **10818.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3412** | 0.5285 | ±1.0570 | **+55.516** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8096** | 0.1353 | ±0.2707 | **+5.982** | **2.20e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6609** | 0.2792 | ±0.5583 | **-5.949** | **2.69e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4509** | 0.1730 | ±0.3461 | **-2.606** | **0.0092** | ** |
| Site: UW (vs UAB) | -0.2109 | 0.1644 | ±0.3287 | -1.283 | 0.1994 |  |
| **Age (years)** | **-0.0515** | 0.0065 | ±0.0130 | **-7.949** | **1.88e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0181 | -1.227 | 0.2197 |  |
| **Hypertension** | **-0.4953** | 0.1447 | ±0.2894 | **-3.423** | **6.20e-04** | *** |
| High cholesterol | +0.2676 | 0.1382 | ±0.2763 | +1.937 | 0.0528 | . |
| Kidney disease | +0.0361 | 0.2352 | ±0.4705 | +0.153 | 0.8780 |  |
| Circulatory disease | -0.1707 | 0.1840 | ±0.3679 | -0.928 | 0.3534 |  |
| Time 54-69, pooled (%) | +0.0149 | 0.0434 | ±0.0867 | +0.343 | 0.7314 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2138**, R² = **0.1044**, Adj R² = **0.0998**, F-statistic = **22.54** (p = **3.83e-44**), Residual SE = **2.981** on **2126** df, AIC = **10750.5**, BIC = **10818.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3477** | 0.5274 | ±1.0548 | **+55.644** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8090** | 0.1354 | ±0.2709 | **+5.974** | **2.32e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6620** | 0.2792 | ±0.5583 | **-5.954** | **2.62e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4529** | 0.1727 | ±0.3455 | **-2.622** | **0.0087** | ** |
| Site: UW (vs UAB) | -0.2125 | 0.1644 | ±0.3288 | -1.293 | 0.1962 |  |
| **Age (years)** | **-0.0515** | 0.0065 | ±0.0129 | **-7.959** | **1.74e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0182 | -1.225 | 0.2206 |  |
| **Hypertension** | **-0.4958** | 0.1447 | ±0.2894 | **-3.426** | **6.14e-04** | *** |
| High cholesterol | +0.2668 | 0.1381 | ±0.2762 | +1.932 | 0.0534 | . |
| Kidney disease | +0.0361 | 0.2352 | ±0.4704 | +0.154 | 0.8779 |  |
| Circulatory disease | -0.1703 | 0.1840 | ±0.3680 | -0.926 | 0.3547 |  |
| Avg. daily time 54-69 (%) | +0.0094 | 0.0441 | ±0.0883 | +0.212 | 0.8321 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2138**, R² = **0.1045**, Adj R² = **0.0999**, F-statistic = **22.55** (p = **3.57e-44**), Residual SE = **2.981** on **2126** df, AIC = **10750.4**, BIC = **10818.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3349** | 0.5290 | ±1.0580 | **+55.453** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8101** | 0.1353 | ±0.2706 | **+5.987** | **2.13e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6594** | 0.2792 | ±0.5584 | **-5.944** | **2.79e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4482** | 0.1734 | ±0.3468 | **-2.585** | **0.0098** | ** |
| Site: UW (vs UAB) | -0.2087 | 0.1646 | ±0.3293 | -1.268 | 0.2049 |  |
| **Age (years)** | **-0.0515** | 0.0065 | ±0.0130 | **-7.945** | **1.93e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0181 | -1.228 | 0.2195 |  |
| **Hypertension** | **-0.4949** | 0.1447 | ±0.2894 | **-3.419** | **6.28e-04** | *** |
| High cholesterol | +0.2687 | 0.1383 | ±0.2765 | +1.944 | 0.0519 | . |
| Kidney disease | +0.0362 | 0.2353 | ±0.4706 | +0.154 | 0.8777 |  |
| Circulatory disease | -0.1714 | 0.1840 | ±0.3679 | -0.931 | 0.3516 |  |
| Time < 70 (%) | +0.0160 | 0.0350 | ±0.0700 | +0.458 | 0.6467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2138**, R² = **0.1044**, Adj R² = **0.0998**, F-statistic = **22.54** (p = **3.79e-44**), Residual SE = **2.981** on **2126** df, AIC = **10750.5**, BIC = **10818.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3458** | 0.5273 | ±1.0547 | **+55.649** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8094** | 0.1354 | ±0.2708 | **+5.979** | **2.25e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6613** | 0.2792 | ±0.5583 | **-5.951** | **2.67e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4518** | 0.1730 | ±0.3459 | **-2.612** | **0.0090** | ** |
| Site: UW (vs UAB) | -0.2114 | 0.1646 | ±0.3292 | -1.284 | 0.1991 |  |
| **Age (years)** | **-0.0515** | 0.0065 | ±0.0129 | **-7.960** | **1.72e-15** | *** |
| BMI (kg/m2) | -0.0111 | 0.0091 | ±0.0182 | -1.225 | 0.2205 |  |
| **Hypertension** | **-0.4955** | 0.1447 | ±0.2895 | **-3.424** | **6.18e-04** | *** |
| High cholesterol | +0.2673 | 0.1382 | ±0.2763 | +1.935 | 0.0530 | . |
| Kidney disease | +0.0361 | 0.2352 | ±0.4705 | +0.154 | 0.8779 |  |
| Circulatory disease | -0.1706 | 0.1840 | ±0.3679 | -0.927 | 0.3538 |  |
| Avg. daily time < 70 (%) | +0.0098 | 0.0364 | ±0.0727 | +0.268 | 0.7886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2138**, R² = **0.1114**, Adj R² = **0.1068**, F-statistic = **24.22** (p = **1.33e-47**), Residual SE = **2.970** on **2126** df, AIC = **10733.9**, BIC = **10801.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.9763** | 0.8749 | ±1.7497 | **+30.835** | **9.02e-209** | *** |
| **Education: graduate level (vs college)** | **+0.7766** | 0.1347 | ±0.2695 | **+5.764** | **8.23e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5831** | 0.2772 | ±0.5545 | **-5.710** | **1.13e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.4976** | 0.1713 | ±0.3426 | **-2.904** | **0.0037** | ** |
| Site: UW (vs UAB) | -0.2606 | 0.1630 | ±0.3260 | -1.599 | 0.1099 |  |
| **Age (years)** | **-0.0519** | 0.0065 | ±0.0129 | **-8.039** | **9.03e-16** | *** |
| BMI (kg/m2) | -0.0095 | 0.0092 | ±0.0183 | -1.033 | 0.3016 |  |
| **Hypertension** | **-0.4688** | 0.1443 | ±0.2886 | **-3.248** | **0.0012** | ** |
| **High cholesterol** | **+0.2737** | 0.1377 | ±0.2753 | **+1.988** | **0.0468** | * |
| Kidney disease | +0.0983 | 0.2360 | ±0.4719 | +0.416 | 0.6771 |  |
| Circulatory disease | -0.1447 | 0.1822 | ±0.3644 | -0.794 | 0.4269 |  |
| **Time 54-250, pooled (%)** | **+0.0244** | 0.0073 | ±0.0146 | **+3.344** | **8.25e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2138**, R² = **0.1112**, Adj R² = **0.1066**, F-statistic = **24.17** (p = **1.68e-47**), Residual SE = **2.970** on **2126** df, AIC = **10734.4**, BIC = **10802.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.9685** | 0.8949 | ±1.7898 | **+30.136** | **1.62e-199** | *** |
| **Education: graduate level (vs college)** | **+0.7773** | 0.1348 | ±0.2695 | **+5.768** | **8.04e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5841** | 0.2772 | ±0.5543 | **-5.716** | **1.09e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.4965** | 0.1714 | ±0.3427 | **-2.897** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.2585 | 0.1630 | ±0.3260 | -1.586 | 0.1128 |  |
| **Age (years)** | **-0.0518** | 0.0065 | ±0.0129 | **-8.016** | **1.09e-15** | *** |
| BMI (kg/m2) | -0.0095 | 0.0092 | ±0.0184 | -1.032 | 0.3022 |  |
| **Hypertension** | **-0.4703** | 0.1443 | ±0.2886 | **-3.259** | **0.0011** | ** |
| **High cholesterol** | **+0.2737** | 0.1377 | ±0.2754 | **+1.988** | **0.0468** | * |
| Kidney disease | +0.1003 | 0.2361 | ±0.4722 | +0.425 | 0.6709 |  |
| Circulatory disease | -0.1437 | 0.1822 | ±0.3644 | -0.789 | 0.4302 |  |
| **Avg. daily time 54-250 (%)** | **+0.0243** | 0.0075 | ±0.0150 | **+3.241** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2138**, R² = **0.1141**, Adj R² = **0.1095**, F-statistic = **24.89** (p = **5.64e-49**), Residual SE = **2.965** on **2126** df, AIC = **10727.3**, BIC = **10795.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2426** | 0.5248 | ±1.0497 | **+55.718** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7926** | 0.1342 | ±0.2683 | **+5.908** | **3.46e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5794** | 0.2775 | ±0.5550 | **-5.692** | **1.26e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5004** | 0.1713 | ±0.3427 | **-2.920** | **0.0035** | ** |
| Site: UW (vs UAB) | -0.2311 | 0.1623 | ±0.3246 | -1.424 | 0.1545 |  |
| **Age (years)** | **-0.0486** | 0.0065 | ±0.0129 | **-7.524** | **5.31e-14** | *** |
| BMI (kg/m2) | -0.0074 | 0.0092 | ±0.0184 | -0.801 | 0.4232 |  |
| **Hypertension** | **-0.4498** | 0.1439 | ±0.2878 | **-3.126** | **0.0018** | ** |
| **High cholesterol** | **+0.3048** | 0.1381 | ±0.2763 | **+2.207** | **0.0273** | * |
| Kidney disease | +0.1582 | 0.2342 | ±0.4683 | +0.676 | 0.4992 |  |
| Circulatory disease | -0.1486 | 0.1835 | ±0.3670 | -0.810 | 0.4180 |  |
| **Time 181-250, pooled (%)** | **-0.0250** | 0.0058 | ±0.0115 | **-4.351** | **1.36e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2138**, R² = **0.1138**, Adj R² = **0.1092**, F-statistic = **24.81** (p = **8.28e-49**), Residual SE = **2.966** on **2126** df, AIC = **10728.1**, BIC = **10796.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2473** | 0.5252 | ±1.0504 | **+55.689** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7941** | 0.1342 | ±0.2684 | **+5.917** | **3.27e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5788** | 0.2777 | ±0.5555 | **-5.685** | **1.31e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5026** | 0.1714 | ±0.3428 | **-2.932** | **0.0034** | ** |
| Site: UW (vs UAB) | -0.2331 | 0.1624 | ±0.3248 | -1.435 | 0.1513 |  |
| **Age (years)** | **-0.0488** | 0.0065 | ±0.0129 | **-7.551** | **4.31e-14** | *** |
| BMI (kg/m2) | -0.0074 | 0.0092 | ±0.0184 | -0.801 | 0.4232 |  |
| **Hypertension** | **-0.4509** | 0.1439 | ±0.2878 | **-3.133** | **0.0017** | ** |
| **High cholesterol** | **+0.3046** | 0.1382 | ±0.2764 | **+2.205** | **0.0275** | * |
| Kidney disease | +0.1568 | 0.2340 | ±0.4681 | +0.670 | 0.5028 |  |
| Circulatory disease | -0.1499 | 0.1835 | ±0.3670 | -0.817 | 0.4141 |  |
| **Avg. daily time 181-250 (%)** | **-0.0243** | 0.0057 | ±0.0114 | **-4.270** | **1.95e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2138**, R² = **0.1162**, Adj R² = **0.1116**, F-statistic = **25.41** (p = **4.94e-50**), Residual SE = **2.962** on **2126** df, AIC = **10722.3**, BIC = **10790.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3123** | 0.5240 | ±1.0480 | **+55.941** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7752** | 0.1342 | ±0.2683 | **+5.778** | **7.54e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5456** | 0.2765 | ±0.5531 | **-5.589** | **2.28e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5145** | 0.1712 | ±0.3424 | **-3.005** | **0.0027** | ** |
| Site: UW (vs UAB) | -0.2568 | 0.1623 | ±0.3246 | -1.582 | 0.1136 |  |
| **Age (years)** | **-0.0498** | 0.0064 | ±0.0129 | **-7.732** | **1.06e-14** | *** |
| BMI (kg/m2) | -0.0073 | 0.0092 | ±0.0184 | -0.796 | 0.4261 |  |
| **Hypertension** | **-0.4436** | 0.1438 | ±0.2877 | **-3.084** | **0.0020** | ** |
| **High cholesterol** | **+0.2997** | 0.1379 | ±0.2758 | **+2.174** | **0.0297** | * |
| Kidney disease | +0.1661 | 0.2351 | ±0.4702 | +0.706 | 0.4799 |  |
| Circulatory disease | -0.1376 | 0.1823 | ±0.3646 | -0.755 | 0.4502 |  |
| **Time > 180 (%)** | **-0.0175** | 0.0037 | ±0.0074 | **-4.714** | **2.43e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2138**, R² = **0.1158**, Adj R² = **0.1112**, F-statistic = **25.30** (p = **8.02e-50**), Residual SE = **2.963** on **2126** df, AIC = **10723.3**, BIC = **10791.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3078** | 0.5244 | ±1.0489 | **+55.886** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7772** | 0.1342 | ±0.2684 | **+5.791** | **6.98e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5468** | 0.2767 | ±0.5534 | **-5.590** | **2.27e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5159** | 0.1713 | ±0.3426 | **-3.011** | **0.0026** | ** |
| Site: UW (vs UAB) | -0.2565 | 0.1624 | ±0.3248 | -1.580 | 0.1142 |  |
| **Age (years)** | **-0.0498** | 0.0064 | ±0.0129 | **-7.730** | **1.07e-14** | *** |
| BMI (kg/m2) | -0.0073 | 0.0092 | ±0.0184 | -0.795 | 0.4267 |  |
| **Hypertension** | **-0.4455** | 0.1438 | ±0.2877 | **-3.097** | **0.0020** | ** |
| **High cholesterol** | **+0.2995** | 0.1380 | ±0.2759 | **+2.171** | **0.0299** | * |
| Kidney disease | +0.1664 | 0.2351 | ±0.4701 | +0.708 | 0.4791 |  |
| Circulatory disease | -0.1379 | 0.1823 | ±0.3647 | -0.756 | 0.4495 |  |
| **Avg. daily time > 180 (%)** | **-0.0171** | 0.0037 | ±0.0074 | **-4.613** | **3.97e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2138**, R² = **0.1139**, Adj R² = **0.1093**, F-statistic = **24.84** (p = **7.21e-49**), Residual SE = **2.966** on **2126** df, AIC = **10727.9**, BIC = **10795.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3107** | 0.5244 | ±1.0488 | **+55.896** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7684** | 0.1340 | ±0.2680 | **+5.733** | **9.85e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5656** | 0.2763 | ±0.5526 | **-5.666** | **1.46e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.5098** | 0.1717 | ±0.3434 | **-2.969** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.2477 | 0.1627 | ±0.3253 | -1.523 | 0.1277 |  |
| **Age (years)** | **-0.0511** | 0.0065 | ±0.0129 | **-7.915** | **2.47e-15** | *** |
| BMI (kg/m2) | -0.0061 | 0.0093 | ±0.0185 | -0.662 | 0.5082 |  |
| **Hypertension** | **-0.4662** | 0.1441 | ±0.2882 | **-3.236** | **0.0012** | ** |
| **High cholesterol** | **+0.2912** | 0.1379 | ±0.2757 | **+2.112** | **0.0347** | * |
| Kidney disease | +0.1266 | 0.2336 | ±0.4672 | +0.542 | 0.5879 |  |
| Circulatory disease | -0.1448 | 0.1820 | ±0.3640 | -0.795 | 0.4264 |  |
| **Nocturnal time > 180 (%)** | **-0.0157** | 0.0038 | ±0.0076 | **-4.150** | **3.32e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2138**, R² = **0.1130**, Adj R² = **0.1084**, F-statistic = **24.61** (p = **2.12e-48**), Residual SE = **2.967** on **2126** df, AIC = **10730.1**, BIC = **10798.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4072** | 0.5224 | ±1.0447 | **+56.296** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7729** | 0.1341 | ±0.2682 | **+5.763** | **8.29e-09** | *** |
| **Education: high school or below (vs college)** | **-1.6168** | 0.2778 | ±0.5557 | **-5.819** | **5.91e-09** | *** |
| **Site: UCSD (vs UAB)** | **-0.4848** | 0.1704 | ±0.3407 | **-2.846** | **0.0044** | ** |
| Site: UW (vs UAB) | -0.2269 | 0.1621 | ±0.3241 | -1.400 | 0.1615 |  |
| **Age (years)** | **-0.0490** | 0.0065 | ±0.0130 | **-7.545** | **4.51e-14** | *** |
| BMI (kg/m2) | -0.0115 | 0.0091 | ±0.0182 | -1.267 | 0.2052 |  |
| **Hypertension** | **-0.4383** | 0.1436 | ±0.2871 | **-3.053** | **0.0023** | ** |
| **High cholesterol** | **+0.3024** | 0.1379 | ±0.2758 | **+2.193** | **0.0283** | * |
| Kidney disease | +0.1311 | 0.2366 | ±0.4731 | +0.554 | 0.5794 |  |
| Circulatory disease | -0.1679 | 0.1844 | ±0.3689 | -0.910 | 0.3627 |  |
| **Any reading > 250 during wear (0/1)** | **-0.6184** | 0.1433 | ±0.2866 | **-4.315** | **1.59e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2138**, R² = **0.1115**, Adj R² = **0.1069**, F-statistic = **24.24** (p = **1.21e-47**), Residual SE = **2.970** on **2126** df, AIC = **10733.7**, BIC = **10801.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4045** | 0.5250 | ±1.0499 | **+56.013** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7769** | 0.1347 | ±0.2694 | **+5.767** | **8.07e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5807** | 0.2773 | ±0.5546 | **-5.700** | **1.20e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.4942** | 0.1712 | ±0.3424 | **-2.887** | **0.0039** | ** |
| Site: UW (vs UAB) | -0.2579 | 0.1629 | ±0.3258 | -1.583 | 0.1134 |  |
| **Age (years)** | **-0.0519** | 0.0065 | ±0.0129 | **-8.037** | **9.20e-16** | *** |
| BMI (kg/m2) | -0.0095 | 0.0092 | ±0.0183 | -1.032 | 0.3019 |  |
| **Hypertension** | **-0.4681** | 0.1443 | ±0.2887 | **-3.243** | **0.0012** | ** |
| **High cholesterol** | **+0.2752** | 0.1377 | ±0.2754 | **+1.999** | **0.0457** | * |
| Kidney disease | +0.0987 | 0.2360 | ±0.4720 | +0.418 | 0.6757 |  |
| Circulatory disease | -0.1455 | 0.1822 | ±0.3643 | -0.799 | 0.4246 |  |
| **Time > 250 (%)** | **-0.0245** | 0.0073 | ±0.0146 | **-3.359** | **7.83e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2138**, R² = **0.1112**, Adj R² = **0.1066**, F-statistic = **24.18** (p = **1.59e-47**), Residual SE = **2.970** on **2126** df, AIC = **10734.3**, BIC = **10802.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3954** | 0.5251 | ±1.0502 | **+55.979** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.7778** | 0.1347 | ±0.2695 | **+5.773** | **7.80e-09** | *** |
| **Education: high school or below (vs college)** | **-1.5824** | 0.2772 | ±0.5545 | **-5.708** | **1.14e-08** | *** |
| **Site: UCSD (vs UAB)** | **-0.4941** | 0.1713 | ±0.3425 | **-2.885** | **0.0039** | ** |
| Site: UW (vs UAB) | -0.2561 | 0.1629 | ±0.3258 | -1.572 | 0.1160 |  |
| **Age (years)** | **-0.0518** | 0.0065 | ±0.0129 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -0.0095 | 0.0092 | ±0.0183 | -1.032 | 0.3022 |  |
| **Hypertension** | **-0.4697** | 0.1443 | ±0.2886 | **-3.254** | **0.0011** | ** |
| **High cholesterol** | **+0.2749** | 0.1377 | ±0.2755 | **+1.996** | **0.0460** | * |
| Kidney disease | +0.1004 | 0.2361 | ±0.4722 | +0.425 | 0.6705 |  |
| Circulatory disease | -0.1444 | 0.1822 | ±0.3644 | -0.792 | 0.4281 |  |
| **Avg. daily time > 250 (%)** | **-0.0244** | 0.0075 | ±0.0150 | **-3.247** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 2,138; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0617**, LLR χ² = **177.60** (p = **7.39e-33**), AUC = **0.6678**, AIC = **2723.7**, BIC = **2786.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8080** | 0.3849 | ±0.7699 | **-7.295** | **2.99e-13** | 0.0603 | *** |
| **Education: graduate level (vs college)** | **-0.6196** | 0.1015 | ±0.2030 | **-6.106** | **1.02e-09** | 0.5382 | *** |
| **Education: high school or below (vs college)** | **+0.7820** | 0.1508 | ±0.3015 | **+5.187** | **2.14e-07** | 2.1858 | *** |
| **Site: UCSD (vs UAB)** | **+0.3346** | 0.1181 | ±0.2363 | **+2.832** | **0.0046** | 1.3973 | ** |
| Site: UW (vs UAB) | +0.0488 | 0.1145 | ±0.2291 | +0.426 | 0.6701 | 1.0500 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.018** | **2.25e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0067 | ±0.0134 | **+2.179** | **0.0293** | 1.0147 | * |
| Hypertension | +0.1940 | 0.1014 | ±0.2028 | +1.913 | 0.0557 | 1.2141 | . |
| High cholesterol | -0.0524 | 0.0967 | ±0.1933 | -0.542 | 0.5880 | 0.9490 |  |
| Kidney disease | -0.1759 | 0.1509 | ±0.3018 | -1.166 | 0.2437 | 0.8387 |  |
| Circulatory disease | +0.1104 | 0.1265 | ±0.2529 | +0.873 | 0.3829 | 1.1167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0671**, LLR χ² = **193.22** (p = **1.89e-35**), AUC = **0.6747**, AIC = **2710.0**, BIC = **2778.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.7482** | 0.4580 | ±0.9160 | **-8.184** | **2.74e-16** | 0.0236 | *** |
| **Education: graduate level (vs college)** | **-0.6015** | 0.1020 | ±0.2039 | **-5.900** | **3.65e-09** | 0.5480 | *** |
| **Education: high school or below (vs college)** | **+0.7211** | 0.1521 | ±0.3043 | **+4.740** | **2.14e-06** | 2.0567 | *** |
| **Site: UCSD (vs UAB)** | **+0.3531** | 0.1187 | ±0.2374 | **+2.975** | **0.0029** | 1.4235 | ** |
| Site: UW (vs UAB) | +0.0741 | 0.1153 | ±0.2306 | +0.643 | 0.5205 | 1.0769 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.831** | **8.43e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0115 | 0.0068 | ±0.0136 | +1.694 | 0.0903 | 1.0116 | . |
| Hypertension | +0.1560 | 0.1022 | ±0.2044 | +1.526 | 0.1269 | 1.1688 |  |
| High cholesterol | -0.0863 | 0.0975 | ±0.1949 | -0.885 | 0.3761 | 0.9173 |  |
| Kidney disease | -0.2097 | 0.1520 | ±0.3041 | -1.379 | 0.1679 | 0.8108 |  |
| Circulatory disease | +0.0951 | 0.1271 | ±0.2541 | +0.748 | 0.4543 | 1.0997 |  |
| **HbA1c (%)** | **+0.1809** | 0.0468 | ±0.0936 | **+3.865** | **1.11e-04** | 1.1983 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0690**, LLR χ² = **198.81** (p = **1.31e-36**), AUC = **0.6767**, AIC = **2704.4**, BIC = **2772.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5321** | 0.4199 | ±0.8398 | **-8.412** | **4.05e-17** | 0.0292 | *** |
| **Education: graduate level (vs college)** | **-0.6100** | 0.1019 | ±0.2039 | **-5.984** | **2.18e-09** | 0.5433 | *** |
| **Education: high school or below (vs college)** | **+0.7189** | 0.1522 | ±0.3044 | **+4.724** | **2.32e-06** | 2.0521 | *** |
| **Site: UCSD (vs UAB)** | **+0.3648** | 0.1189 | ±0.2378 | **+3.067** | **0.0022** | 1.4402 | ** |
| Site: UW (vs UAB) | +0.0651 | 0.1153 | ±0.2305 | +0.565 | 0.5720 | 1.0673 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.830** | **8.49e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0123 | 0.0068 | ±0.0135 | +1.816 | 0.0694 | 1.0124 | . |
| Hypertension | +0.1509 | 0.1023 | ±0.2047 | +1.474 | 0.1404 | 1.1628 |  |
| High cholesterol | -0.0786 | 0.0974 | ±0.1947 | -0.807 | 0.4196 | 0.9244 |  |
| Kidney disease | -0.2521 | 0.1531 | ±0.3063 | -1.646 | 0.0997 | 0.7772 | . |
| Circulatory disease | +0.0915 | 0.1273 | ±0.2547 | +0.719 | 0.4724 | 1.0958 |  |
| **Mean glucose (mg/dL)** | **+0.0065** | 0.0014 | ±0.0029 | **+4.522** | **6.12e-06** | 1.0065 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0690**, LLR χ² = **198.81** (p = **1.31e-36**), AUC = **0.6767**, AIC = **2704.4**, BIC = **2772.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4271** | 0.5293 | ±1.0587 | **-8.363** | **6.10e-17** | 0.0119 | *** |
| **Education: graduate level (vs college)** | **-0.6100** | 0.1019 | ±0.2039 | **-5.984** | **2.18e-09** | 0.5433 | *** |
| **Education: high school or below (vs college)** | **+0.7189** | 0.1522 | ±0.3044 | **+4.724** | **2.32e-06** | 2.0521 | *** |
| **Site: UCSD (vs UAB)** | **+0.3648** | 0.1189 | ±0.2378 | **+3.067** | **0.0022** | 1.4402 | ** |
| Site: UW (vs UAB) | +0.0651 | 0.1153 | ±0.2305 | +0.565 | 0.5720 | 1.0673 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.830** | **8.49e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0123 | 0.0068 | ±0.0135 | +1.816 | 0.0694 | 1.0124 | . |
| Hypertension | +0.1509 | 0.1023 | ±0.2047 | +1.474 | 0.1404 | 1.1628 |  |
| High cholesterol | -0.0786 | 0.0974 | ±0.1947 | -0.807 | 0.4196 | 0.9244 |  |
| Kidney disease | -0.2521 | 0.1531 | ±0.3063 | -1.646 | 0.0997 | 0.7772 | . |
| Circulatory disease | +0.0915 | 0.1273 | ±0.2547 | +0.719 | 0.4724 | 1.0958 |  |
| **GMI (%)** | **+0.2704** | 0.0598 | ±0.1196 | **+4.522** | **6.12e-06** | 1.3105 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0678**, LLR χ² = **195.23** (p = **7.25e-36**), AUC = **0.6756**, AIC = **2708.0**, BIC = **2776.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4715** | 0.4198 | ±0.8396 | **-8.270** | **1.34e-16** | 0.0311 | *** |
| **Education: graduate level (vs college)** | **-0.6088** | 0.1019 | ±0.2037 | **-5.976** | **2.28e-09** | 0.5440 | *** |
| **Education: high school or below (vs college)** | **+0.7266** | 0.1520 | ±0.3039 | **+4.782** | **1.74e-06** | 2.0680 | *** |
| **Site: UCSD (vs UAB)** | **+0.3551** | 0.1187 | ±0.2374 | **+2.991** | **0.0028** | 1.4263 | ** |
| Site: UW (vs UAB) | +0.0571 | 0.1151 | ±0.2302 | +0.496 | 0.6197 | 1.0588 |  |
| **Age (years)** | **+0.0318** | 0.0045 | ±0.0090 | **+7.037** | **1.97e-12** | 1.0323 | *** |
| BMI (kg/m2) | +0.0112 | 0.0068 | ±0.0136 | +1.652 | 0.0986 | 1.0113 | . |
| Hypertension | +0.1628 | 0.1021 | ±0.2042 | +1.595 | 0.1107 | 1.1768 |  |
| High cholesterol | -0.0780 | 0.0973 | ±0.1946 | -0.801 | 0.4229 | 0.9250 |  |
| Kidney disease | -0.2256 | 0.1524 | ±0.3048 | -1.480 | 0.1389 | 0.7980 |  |
| Circulatory disease | +0.0963 | 0.1272 | ±0.2545 | +0.757 | 0.4493 | 1.1010 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0059** | 0.0014 | ±0.0029 | **+4.125** | **3.70e-05** | 1.0059 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0684**, LLR χ² = **196.80** (p = **3.43e-36**), AUC = **0.6761**, AIC = **2706.4**, BIC = **2774.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1323** | 0.3945 | ±0.7891 | **-7.939** | **2.03e-15** | 0.0436 | *** |
| **Education: graduate level (vs college)** | **-0.6014** | 0.1020 | ±0.2040 | **-5.896** | **3.72e-09** | 0.5480 | *** |
| **Education: high school or below (vs college)** | **+0.7262** | 0.1519 | ±0.3038 | **+4.781** | **1.74e-06** | 2.0672 | *** |
| **Site: UCSD (vs UAB)** | **+0.3724** | 0.1191 | ±0.2381 | **+3.128** | **0.0018** | 1.4513 | ** |
| Site: UW (vs UAB) | +0.0819 | 0.1154 | ±0.2308 | +0.710 | 0.4777 | 1.0854 |  |
| **Age (years)** | **+0.0303** | 0.0045 | ±0.0091 | **+6.682** | **2.36e-11** | 1.0307 | *** |
| BMI (kg/m2) | +0.0131 | 0.0068 | ±0.0135 | +1.946 | 0.0516 | 1.0132 | . |
| Hypertension | +0.1462 | 0.1024 | ±0.2049 | +1.427 | 0.1536 | 1.1574 |  |
| High cholesterol | -0.0713 | 0.0973 | ±0.1946 | -0.733 | 0.4638 | 0.9312 |  |
| Kidney disease | -0.2951 | 0.1547 | ±0.3094 | -1.908 | 0.0564 | 0.7444 | . |
| Circulatory disease | +0.0903 | 0.1272 | ±0.2544 | +0.710 | 0.4774 | 1.0946 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0176** | 0.0040 | ±0.0081 | **+4.344** | **1.40e-05** | 1.0177 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0681**, LLR χ² = **196.12** (p = **4.74e-36**), AUC = **0.6763**, AIC = **2707.1**, BIC = **2775.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1280** | 0.3944 | ±0.7888 | **-7.931** | **2.17e-15** | 0.0438 | *** |
| **Education: graduate level (vs college)** | **-0.6044** | 0.1020 | ±0.2039 | **-5.927** | **3.09e-09** | 0.5464 | *** |
| **Education: high school or below (vs college)** | **+0.7248** | 0.1519 | ±0.3037 | **+4.773** | **1.82e-06** | 2.0644 | *** |
| **Site: UCSD (vs UAB)** | **+0.3699** | 0.1190 | ±0.2380 | **+3.108** | **0.0019** | 1.4475 | ** |
| Site: UW (vs UAB) | +0.0772 | 0.1153 | ±0.2307 | +0.670 | 0.5031 | 1.0803 |  |
| **Age (years)** | **+0.0301** | 0.0045 | ±0.0091 | **+6.638** | **3.18e-11** | 1.0305 | *** |
| **BMI (kg/m2)** | **+0.0135** | 0.0067 | ±0.0135 | **+1.995** | **0.0460** | 1.0135 | * |
| Hypertension | +0.1477 | 0.1024 | ±0.2048 | +1.442 | 0.1493 | 1.1591 |  |
| High cholesterol | -0.0710 | 0.0972 | ±0.1945 | -0.730 | 0.4653 | 0.9315 |  |
| Kidney disease | -0.2948 | 0.1547 | ±0.3094 | -1.906 | 0.0567 | 0.7447 | . |
| Circulatory disease | +0.0942 | 0.1271 | ±0.2542 | +0.742 | 0.4584 | 1.0988 |  |
| **Avg. daily SD (mg/dL)** | **+0.0194** | 0.0046 | ±0.0091 | **+4.268** | **1.97e-05** | 1.0196 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0642**, LLR χ² = **184.85** (p = **1.02e-33**), AUC = **0.6719**, AIC = **2718.4**, BIC = **2786.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2016** | 0.4134 | ±0.8268 | **-7.744** | **9.61e-15** | 0.0407 | *** |
| **Education: graduate level (vs college)** | **-0.6080** | 0.1017 | ±0.2035 | **-5.976** | **2.29e-09** | 0.5445 | *** |
| **Education: high school or below (vs college)** | **+0.7627** | 0.1511 | ±0.3023 | **+5.046** | **4.50e-07** | 2.1441 | *** |
| **Site: UCSD (vs UAB)** | **+0.3569** | 0.1187 | ±0.2373 | **+3.007** | **0.0026** | 1.4289 | ** |
| Site: UW (vs UAB) | +0.0708 | 0.1151 | ±0.2302 | +0.616 | 0.5382 | 1.0734 |  |
| **Age (years)** | **+0.0306** | 0.0045 | ±0.0090 | **+6.758** | **1.40e-11** | 1.0310 | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0067 | ±0.0134 | **+2.136** | **0.0327** | 1.0145 | * |
| Hypertension | +0.1687 | 0.1020 | ±0.2040 | +1.654 | 0.0981 | 1.1838 | . |
| High cholesterol | -0.0552 | 0.0969 | ±0.1937 | -0.570 | 0.5688 | 0.9463 |  |
| Kidney disease | -0.2439 | 0.1534 | ±0.3069 | -1.590 | 0.1119 | 0.7835 |  |
| Circulatory disease | +0.1013 | 0.1267 | ±0.2534 | +0.799 | 0.4241 | 1.1066 |  |
| **CV (%)** | **+0.0240** | 0.0089 | ±0.0178 | **+2.689** | **0.0072** | 1.0243 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0639**, LLR χ² = **183.94** (p = **1.57e-33**), AUC = **0.6714**, AIC = **2719.3**, BIC = **2787.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2497** | 0.4429 | ±0.8859 | **-5.079** | **3.79e-07** | 0.1054 | *** |
| **Education: graduate level (vs college)** | **-0.6090** | 0.1017 | ±0.2034 | **-5.988** | **2.12e-09** | 0.5439 | *** |
| **Education: high school or below (vs college)** | **+0.7617** | 0.1511 | ±0.3023 | **+5.040** | **4.66e-07** | 2.1420 | *** |
| **Site: UCSD (vs UAB)** | **+0.3525** | 0.1185 | ±0.2371 | **+2.974** | **0.0029** | 1.4226 | ** |
| Site: UW (vs UAB) | +0.0632 | 0.1149 | ±0.2298 | +0.550 | 0.5822 | 1.0653 |  |
| **Age (years)** | **+0.0306** | 0.0045 | ±0.0090 | **+6.771** | **1.28e-11** | 1.0311 | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0067 | ±0.0134 | **+2.140** | **0.0323** | 1.0145 | * |
| Hypertension | +0.1697 | 0.1020 | ±0.2040 | +1.664 | 0.0962 | 1.1849 | . |
| High cholesterol | -0.0570 | 0.0969 | ±0.1937 | -0.589 | 0.5560 | 0.9446 |  |
| Kidney disease | -0.2255 | 0.1524 | ±0.3048 | -1.480 | 0.1389 | 0.7981 |  |
| Circulatory disease | +0.1016 | 0.1267 | ±0.2534 | +0.802 | 0.4225 | 1.1070 |  |
| **Mean / SD ratio** | **-0.0886** | 0.0353 | ±0.0706 | **-2.509** | **0.0121** | 0.9152 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0637**, LLR χ² = **183.38** (p = **2.05e-33**), AUC = **0.6712**, AIC = **2719.9**, BIC = **2787.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2796** | 0.4422 | ±0.8844 | **-5.155** | **2.53e-07** | 0.1023 | *** |
| **Education: graduate level (vs college)** | **-0.6115** | 0.1017 | ±0.2033 | **-6.015** | **1.80e-09** | 0.5426 | *** |
| **Education: high school or below (vs college)** | **+0.7619** | 0.1511 | ±0.3022 | **+5.042** | **4.60e-07** | 2.1424 | *** |
| **Site: UCSD (vs UAB)** | **+0.3465** | 0.1184 | ±0.2368 | **+2.927** | **0.0034** | 1.4141 | ** |
| Site: UW (vs UAB) | +0.0589 | 0.1148 | ±0.2297 | +0.513 | 0.6078 | 1.0607 |  |
| **Age (years)** | **+0.0305** | 0.0045 | ±0.0091 | **+6.739** | **1.60e-11** | 1.0310 | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0067 | ±0.0134 | **+2.143** | **0.0321** | 1.0145 | * |
| Hypertension | +0.1732 | 0.1019 | ±0.2038 | +1.700 | 0.0892 | 1.1891 | . |
| High cholesterol | -0.0559 | 0.0968 | ±0.1937 | -0.577 | 0.5638 | 0.9456 |  |
| Kidney disease | -0.2209 | 0.1522 | ±0.3044 | -1.451 | 0.1468 | 0.8018 |  |
| Circulatory disease | +0.1078 | 0.1266 | ±0.2532 | +0.851 | 0.3946 | 1.1138 |  |
| **Avg. daily mean/SD** | **-0.0711** | 0.0297 | ±0.0594 | **-2.393** | **0.0167** | 0.9313 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0642**, LLR χ² = **184.99** (p = **9.56e-34**), AUC = **0.6705**, AIC = **2718.3**, BIC = **2786.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3960** | 0.4439 | ±0.8877 | **-7.651** | **2.00e-14** | 0.0335 | *** |
| **Education: graduate level (vs college)** | **-0.6078** | 0.1018 | ±0.2035 | **-5.973** | **2.33e-09** | 0.5446 | *** |
| **Education: high school or below (vs college)** | **+0.7584** | 0.1510 | ±0.3020 | **+5.023** | **5.09e-07** | 2.1348 | *** |
| **Site: UCSD (vs UAB)** | **+0.3575** | 0.1187 | ±0.2374 | **+3.012** | **0.0026** | 1.4297 | ** |
| Site: UW (vs UAB) | +0.0823 | 0.1154 | ±0.2309 | +0.713 | 0.4760 | 1.0858 |  |
| **Age (years)** | **+0.0320** | 0.0045 | ±0.0090 | **+7.090** | **1.34e-12** | 1.0325 | *** |
| **BMI (kg/m2)** | **+0.0140** | 0.0067 | ±0.0134 | **+2.089** | **0.0367** | 1.0141 | * |
| Hypertension | +0.1871 | 0.1016 | ±0.2032 | +1.842 | 0.0655 | 1.2058 | . |
| High cholesterol | -0.0515 | 0.0969 | ±0.1937 | -0.532 | 0.5950 | 0.9498 |  |
| Kidney disease | -0.2109 | 0.1518 | ±0.3037 | -1.389 | 0.1647 | 0.8098 |  |
| Circulatory disease | +0.1069 | 0.1267 | ±0.2534 | +0.844 | 0.3987 | 1.1128 |  |
| **MAG (mg/dL/h)** | **+0.0141** | 0.0052 | ±0.0104 | **+2.708** | **0.0068** | 1.0142 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0670**, LLR χ² = **193.03** (p = **2.07e-35**), AUC = **0.6754**, AIC = **2710.2**, BIC = **2778.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2655** | 0.4048 | ±0.8095 | **-8.068** | **7.16e-16** | 0.0382 | *** |
| **Education: graduate level (vs college)** | **-0.6061** | 0.1019 | ±0.2038 | **-5.947** | **2.73e-09** | 0.5455 | *** |
| **Education: high school or below (vs college)** | **+0.7313** | 0.1517 | ±0.3033 | **+4.822** | **1.42e-06** | 2.0777 | *** |
| **Site: UCSD (vs UAB)** | **+0.3689** | 0.1189 | ±0.2379 | **+3.102** | **0.0019** | 1.4461 | ** |
| Site: UW (vs UAB) | +0.0758 | 0.1153 | ±0.2305 | +0.657 | 0.5110 | 1.0787 |  |
| **Age (years)** | **+0.0305** | 0.0045 | ±0.0090 | **+6.735** | **1.64e-11** | 1.0309 | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0067 | ±0.0135 | **+2.139** | **0.0325** | 1.0145 | * |
| Hypertension | +0.1586 | 0.1022 | ±0.2043 | +1.553 | 0.1205 | 1.1719 |  |
| High cholesterol | -0.0674 | 0.0971 | ±0.1943 | -0.694 | 0.4879 | 0.9348 |  |
| Kidney disease | -0.2768 | 0.1540 | ±0.3081 | -1.797 | 0.0724 | 0.7582 | . |
| Circulatory disease | +0.0942 | 0.1270 | ±0.2540 | +0.742 | 0.4582 | 1.0988 |  |
| **Avg. daily range (mg/dL)** | **+0.0048** | 0.0012 | ±0.0024 | **+3.912** | **9.16e-05** | 1.0048 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0663**, LLR χ² = **190.82** (p = **5.93e-35**), AUC = **0.6725**, AIC = **2712.4**, BIC = **2780.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9774** | 0.3893 | ±0.7787 | **-7.647** | **2.05e-14** | 0.0509 | *** |
| **Education: graduate level (vs college)** | **-0.6004** | 0.1019 | ±0.2038 | **-5.891** | **3.84e-09** | 0.5486 | *** |
| **Education: high school or below (vs college)** | **+0.7526** | 0.1514 | ±0.3028 | **+4.970** | **6.68e-07** | 2.1224 | *** |
| **Site: UCSD (vs UAB)** | **+0.3615** | 0.1189 | ±0.2377 | **+3.041** | **0.0024** | 1.4355 | ** |
| Site: UW (vs UAB) | +0.0763 | 0.1152 | ±0.2304 | +0.662 | 0.5079 | 1.0793 |  |
| **Age (years)** | **+0.0317** | 0.0045 | ±0.0090 | **+7.009** | **2.41e-12** | 1.0322 | *** |
| BMI (kg/m2) | +0.0124 | 0.0068 | ±0.0135 | +1.842 | 0.0654 | 1.0125 | . |
| Hypertension | +0.1669 | 0.1020 | ±0.2040 | +1.637 | 0.1017 | 1.1816 |  |
| High cholesterol | -0.0702 | 0.0972 | ±0.1944 | -0.722 | 0.4703 | 0.9322 |  |
| Kidney disease | -0.2385 | 0.1528 | ±0.3055 | -1.561 | 0.1185 | 0.7878 |  |
| Circulatory disease | +0.0821 | 0.1273 | ±0.2545 | +0.645 | 0.5187 | 1.0856 |  |
| **SD of daily means (mg/dL)** | **+0.0274** | 0.0077 | ±0.0153 | **+3.577** | **3.47e-04** | 1.0278 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0673**, LLR χ² = **193.83** (p = **1.41e-35**), AUC = **0.6738**, AIC = **2709.4**, BIC = **2777.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8701** | 0.4502 | ±0.9004 | **-4.154** | **3.27e-05** | 0.1541 | *** |
| **Education: graduate level (vs college)** | **-0.6051** | 0.1019 | ±0.2038 | **-5.938** | **2.89e-09** | 0.5460 | *** |
| **Education: high school or below (vs college)** | **+0.7291** | 0.1519 | ±0.3039 | **+4.799** | **1.60e-06** | 2.0733 | *** |
| **Site: UCSD (vs UAB)** | **+0.3726** | 0.1190 | ±0.2379 | **+3.132** | **0.0017** | 1.4515 | ** |
| Site: UW (vs UAB) | +0.0772 | 0.1153 | ±0.2307 | +0.670 | 0.5031 | 1.0803 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.841** | **7.87e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0126 | 0.0068 | ±0.0135 | +1.870 | 0.0614 | 1.0127 | . |
| Hypertension | +0.1659 | 0.1020 | ±0.2041 | +1.625 | 0.1041 | 1.1804 |  |
| High cholesterol | -0.0694 | 0.0972 | ±0.1943 | -0.714 | 0.4754 | 0.9330 |  |
| Kidney disease | -0.2504 | 0.1531 | ±0.3062 | -1.636 | 0.1019 | 0.7785 |  |
| Circulatory disease | +0.0930 | 0.1271 | ±0.2542 | +0.732 | 0.4644 | 1.0975 |  |
| **Time in range 70-180, pooled (%)** | **-0.0094** | 0.0024 | ±0.0047 | **-3.997** | **6.43e-05** | 0.9906 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0672**, LLR χ² = **193.56** (p = **1.61e-35**), AUC = **0.6737**, AIC = **2709.7**, BIC = **2777.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8756** | 0.4505 | ±0.9009 | **-4.164** | **3.13e-05** | 0.1533 | *** |
| **Education: graduate level (vs college)** | **-0.6059** | 0.1019 | ±0.2038 | **-5.946** | **2.75e-09** | 0.5456 | *** |
| **Education: high school or below (vs college)** | **+0.7289** | 0.1519 | ±0.3039 | **+4.797** | **1.61e-06** | 2.0727 | *** |
| **Site: UCSD (vs UAB)** | **+0.3727** | 0.1190 | ±0.2379 | **+3.133** | **0.0017** | 1.4517 | ** |
| Site: UW (vs UAB) | +0.0770 | 0.1153 | ±0.2307 | +0.668 | 0.5042 | 1.0801 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.834** | **8.26e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0126 | 0.0068 | ±0.0135 | +1.867 | 0.0618 | 1.0127 | . |
| Hypertension | +0.1666 | 0.1020 | ±0.2040 | +1.633 | 0.1024 | 1.1813 |  |
| High cholesterol | -0.0697 | 0.0972 | ±0.1943 | -0.717 | 0.4733 | 0.9327 |  |
| Kidney disease | -0.2513 | 0.1531 | ±0.3063 | -1.641 | 0.1008 | 0.7778 |  |
| Circulatory disease | +0.0931 | 0.1271 | ±0.2542 | +0.732 | 0.4639 | 1.0976 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0093** | 0.0024 | ±0.0047 | **-3.964** | **7.37e-05** | 0.9907 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0634**, LLR χ² = **182.61** (p = **2.96e-33**), AUC = **0.6704**, AIC = **2720.6**, BIC = **2788.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7024** | 0.3882 | ±0.7764 | **-6.961** | **3.38e-12** | 0.0670 | *** |
| **Education: graduate level (vs college)** | **-0.6271** | 0.1017 | ±0.2033 | **-6.168** | **6.94e-10** | 0.5342 | *** |
| **Education: high school or below (vs college)** | **+0.7616** | 0.1511 | ±0.3022 | **+5.041** | **4.64e-07** | 2.1418 | *** |
| **Site: UCSD (vs UAB)** | **+0.3095** | 0.1188 | ±0.2376 | **+2.605** | **0.0092** | 1.3627 | ** |
| Site: UW (vs UAB) | +0.0342 | 0.1149 | ±0.2298 | +0.297 | 0.7661 | 1.0348 |  |
| **Age (years)** | **+0.0310** | 0.0045 | ±0.0090 | **+6.872** | **6.33e-12** | 1.0315 | *** |
| **BMI (kg/m2)** | **+0.0153** | 0.0067 | ±0.0135 | **+2.268** | **0.0233** | 1.0154 | * |
| Hypertension | +0.1969 | 0.1015 | ±0.2030 | +1.940 | 0.0524 | 1.2176 | . |
| High cholesterol | -0.0664 | 0.0970 | ±0.1940 | -0.685 | 0.4934 | 0.9357 |  |
| Kidney disease | -0.1842 | 0.1513 | ±0.3025 | -1.218 | 0.2234 | 0.8318 |  |
| Circulatory disease | +0.1282 | 0.1268 | ±0.2537 | +1.011 | 0.3120 | 1.1368 |  |
| **Any reading < 54 during wear (0/1)** | **-0.2310** | 0.1035 | ±0.2070 | **-2.231** | **0.0256** | 0.7938 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0617**, LLR χ² = **177.60** (p = **3.20e-32**), AUC = **0.6678**, AIC = **2725.6**, BIC = **2793.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8108** | 0.3861 | ±0.7723 | **-7.279** | **3.36e-13** | 0.0602 | *** |
| **Education: graduate level (vs college)** | **-0.6194** | 0.1015 | ±0.2030 | **-6.103** | **1.04e-09** | 0.5382 | *** |
| **Education: high school or below (vs college)** | **+0.7827** | 0.1510 | ±0.3019 | **+5.185** | **2.16e-07** | 2.1873 | *** |
| **Site: UCSD (vs UAB)** | **+0.3358** | 0.1189 | ±0.2378 | **+2.825** | **0.0047** | 1.3991 | ** |
| Site: UW (vs UAB) | +0.0498 | 0.1151 | ±0.2302 | +0.433 | 0.6650 | 1.0511 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.018** | **2.24e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0067 | ±0.0134 | **+2.179** | **0.0293** | 1.0147 | * |
| Hypertension | +0.1941 | 0.1014 | ±0.2028 | +1.915 | 0.0555 | 1.2143 | . |
| High cholesterol | -0.0519 | 0.0968 | ±0.1936 | -0.536 | 0.5921 | 0.9495 |  |
| Kidney disease | -0.1758 | 0.1509 | ±0.3018 | -1.165 | 0.2439 | 0.8388 |  |
| Circulatory disease | +0.1101 | 0.1265 | ±0.2530 | +0.870 | 0.3843 | 1.1163 |  |
| Time < 54 (%) | +0.0082 | 0.0893 | ±0.1787 | +0.092 | 0.9265 | 1.0083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0617**, LLR χ² = **177.78** (p = **2.94e-32**), AUC = **0.6679**, AIC = **2725.5**, BIC = **2793.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8165** | 0.3855 | ±0.7709 | **-7.307** | **2.73e-13** | 0.0598 | *** |
| **Education: graduate level (vs college)** | **-0.6184** | 0.1015 | ±0.2031 | **-6.091** | **1.12e-09** | 0.5388 | *** |
| **Education: high school or below (vs college)** | **+0.7849** | 0.1509 | ±0.3019 | **+5.200** | **1.99e-07** | 2.1923 | *** |
| **Site: UCSD (vs UAB)** | **+0.3395** | 0.1187 | ±0.2374 | **+2.860** | **0.0042** | 1.4042 | ** |
| Site: UW (vs UAB) | +0.0539 | 0.1152 | ±0.2303 | +0.468 | 0.6399 | 1.0554 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.016** | **2.28e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0067 | ±0.0134 | **+2.178** | **0.0294** | 1.0147 | * |
| Hypertension | +0.1949 | 0.1014 | ±0.2028 | +1.922 | 0.0546 | 1.2152 | . |
| High cholesterol | -0.0502 | 0.0968 | ±0.1936 | -0.519 | 0.6038 | 0.9510 |  |
| Kidney disease | -0.1760 | 0.1509 | ±0.3018 | -1.166 | 0.2435 | 0.8386 |  |
| Circulatory disease | +0.1090 | 0.1265 | ±0.2530 | +0.862 | 0.3888 | 1.1152 |  |
| Avg. daily time < 54 (%) | +0.0455 | 0.1054 | ±0.2108 | +0.432 | 0.6658 | 1.0466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0620**, LLR χ² = **178.53** (p = **2.06e-32**), AUC = **0.6684**, AIC = **2724.7**, BIC = **2792.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8344** | 0.3860 | ±0.7719 | **-7.344** | **2.08e-13** | 0.0588 | *** |
| **Education: graduate level (vs college)** | **-0.6154** | 0.1016 | ±0.2032 | **-6.057** | **1.39e-09** | 0.5404 | *** |
| **Education: high school or below (vs college)** | **+0.7883** | 0.1510 | ±0.3020 | **+5.221** | **1.78e-07** | 2.1996 | *** |
| **Site: UCSD (vs UAB)** | **+0.3438** | 0.1186 | ±0.2371 | **+2.899** | **0.0037** | 1.4102 | ** |
| Site: UW (vs UAB) | +0.0588 | 0.1151 | ±0.2301 | +0.511 | 0.6092 | 1.0606 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.024** | **2.16e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0067 | ±0.0134 | **+2.156** | **0.0311** | 1.0146 | * |
| Hypertension | +0.1967 | 0.1014 | ±0.2029 | +1.939 | 0.0525 | 1.2174 | . |
| High cholesterol | -0.0488 | 0.0968 | ±0.1935 | -0.504 | 0.6142 | 0.9524 |  |
| Kidney disease | -0.1757 | 0.1508 | ±0.3017 | -1.165 | 0.2441 | 0.8389 |  |
| Circulatory disease | +0.1089 | 0.1265 | ±0.2530 | +0.861 | 0.3892 | 1.1151 |  |
| Time 54-69, pooled (%) | +0.0312 | 0.0322 | ±0.0644 | +0.969 | 0.3324 | 1.0317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0622**, LLR χ² = **178.99** (p = **1.65e-32**), AUC = **0.6686**, AIC = **2724.3**, BIC = **2792.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8331** | 0.3856 | ±0.7712 | **-7.347** | **2.02e-13** | 0.0588 | *** |
| **Education: graduate level (vs college)** | **-0.6140** | 0.1016 | ±0.2032 | **-6.042** | **1.52e-09** | 0.5412 | *** |
| **Education: high school or below (vs college)** | **+0.7895** | 0.1510 | ±0.3020 | **+5.228** | **1.71e-07** | 2.2022 | *** |
| **Site: UCSD (vs UAB)** | **+0.3440** | 0.1185 | ±0.2370 | **+2.904** | **0.0037** | 1.4106 | ** |
| Site: UW (vs UAB) | +0.0611 | 0.1151 | ±0.2302 | +0.531 | 0.5957 | 1.0630 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.009** | **2.40e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0067 | ±0.0134 | **+2.150** | **0.0315** | 1.0145 | * |
| Hypertension | +0.1974 | 0.1015 | ±0.2029 | +1.946 | 0.0517 | 1.2183 | . |
| High cholesterol | -0.0484 | 0.0968 | ±0.1935 | -0.500 | 0.6173 | 0.9528 |  |
| Kidney disease | -0.1755 | 0.1509 | ±0.3017 | -1.163 | 0.2447 | 0.8390 |  |
| Circulatory disease | +0.1092 | 0.1265 | ±0.2530 | +0.863 | 0.3882 | 1.1153 |  |
| Avg. daily time 54-69 (%) | +0.0376 | 0.0317 | ±0.0633 | +1.186 | 0.2356 | 1.0383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0619**, LLR χ² = **178.25** (p = **2.36e-32**), AUC = **0.6683**, AIC = **2725.0**, BIC = **2793.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8329** | 0.3862 | ±0.7725 | **-7.335** | **2.22e-13** | 0.0588 | *** |
| **Education: graduate level (vs college)** | **-0.6163** | 0.1016 | ±0.2032 | **-6.067** | **1.30e-09** | 0.5399 | *** |
| **Education: high school or below (vs college)** | **+0.7880** | 0.1510 | ±0.3020 | **+5.218** | **1.81e-07** | 2.1990 | *** |
| **Site: UCSD (vs UAB)** | **+0.3439** | 0.1187 | ±0.2375 | **+2.896** | **0.0038** | 1.4105 | ** |
| Site: UW (vs UAB) | +0.0583 | 0.1152 | ±0.2304 | +0.506 | 0.6130 | 1.0600 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.026** | **2.12e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0067 | ±0.0134 | **+2.164** | **0.0305** | 1.0146 | * |
| Hypertension | +0.1963 | 0.1014 | ±0.2029 | +1.935 | 0.0530 | 1.2169 | . |
| High cholesterol | -0.0487 | 0.0968 | ±0.1936 | -0.503 | 0.6152 | 0.9525 |  |
| Kidney disease | -0.1756 | 0.1508 | ±0.3017 | -1.164 | 0.2445 | 0.8390 |  |
| Circulatory disease | +0.1087 | 0.1265 | ±0.2530 | +0.859 | 0.3904 | 1.1148 |  |
| Time < 70 (%) | +0.0211 | 0.0260 | ±0.0520 | +0.809 | 0.4182 | 1.0213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0621**, LLR χ² = **178.78** (p = **1.83e-32**), AUC = **0.6686**, AIC = **2724.5**, BIC = **2792.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8325** | 0.3857 | ±0.7713 | **-7.345** | **2.06e-13** | 0.0589 | *** |
| **Education: graduate level (vs college)** | **-0.6146** | 0.1016 | ±0.2032 | **-6.048** | **1.46e-09** | 0.5409 | *** |
| **Education: high school or below (vs college)** | **+0.7896** | 0.1510 | ±0.3020 | **+5.228** | **1.71e-07** | 2.2024 | *** |
| **Site: UCSD (vs UAB)** | **+0.3449** | 0.1186 | ±0.2372 | **+2.909** | **0.0036** | 1.4119 | ** |
| Site: UW (vs UAB) | +0.0614 | 0.1152 | ±0.2304 | +0.533 | 0.5940 | 1.0633 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+7.010** | **2.39e-12** | 1.0321 | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0067 | ±0.0134 | **+2.157** | **0.0310** | 1.0146 | * |
| Hypertension | +0.1972 | 0.1015 | ±0.2029 | +1.944 | 0.0519 | 1.2180 | . |
| High cholesterol | -0.0479 | 0.0968 | ±0.1936 | -0.495 | 0.6204 | 0.9532 |  |
| Kidney disease | -0.1756 | 0.1509 | ±0.3017 | -1.164 | 0.2443 | 0.8389 |  |
| Circulatory disease | +0.1086 | 0.1265 | ±0.2530 | +0.859 | 0.3906 | 1.1147 |  |
| Avg. daily time < 70 (%) | +0.0287 | 0.0263 | ±0.0526 | +1.092 | 0.2750 | 1.0291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0648**, LLR χ² = **186.49** (p = **4.68e-34**), AUC = **0.6705**, AIC = **2716.8**, BIC = **2784.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.5680** | 0.5759 | ±1.1519 | **-2.723** | **0.0065** | 0.2085 | ** |
| **Education: graduate level (vs college)** | **-0.6047** | 0.1018 | ±0.2036 | **-5.941** | **2.83e-09** | 0.5463 | *** |
| **Education: high school or below (vs college)** | **+0.7452** | 0.1516 | ±0.3032 | **+4.916** | **8.83e-07** | 2.1068 | *** |
| **Site: UCSD (vs UAB)** | **+0.3557** | 0.1186 | ±0.2371 | **+3.000** | **0.0027** | 1.4272 | ** |
| Site: UW (vs UAB) | +0.0721 | 0.1151 | ±0.2302 | +0.627 | 0.5309 | 1.0748 |  |
| **Age (years)** | **+0.0319** | 0.0045 | ±0.0090 | **+7.072** | **1.52e-12** | 1.0324 | *** |
| **BMI (kg/m2)** | **+0.0138** | 0.0067 | ±0.0135 | **+2.051** | **0.0403** | 1.0139 | * |
| Hypertension | +0.1791 | 0.1017 | ±0.2034 | +1.761 | 0.0782 | 1.1962 | . |
| High cholesterol | -0.0563 | 0.0969 | ±0.1938 | -0.581 | 0.5610 | 0.9452 |  |
| Kidney disease | -0.2096 | 0.1520 | ±0.3040 | -1.379 | 0.1679 | 0.8109 |  |
| Circulatory disease | +0.0975 | 0.1269 | ±0.2538 | +0.768 | 0.4422 | 1.1024 |  |
| **Time 54-250, pooled (%)** | **-0.0128** | 0.0044 | ±0.0088 | **-2.891** | **0.0038** | 0.9873 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0646**, LLR χ² = **186.01** (p = **5.87e-34**), AUC = **0.6704**, AIC = **2717.2**, BIC = **2785.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.5793** | 0.5815 | ±1.1629 | **-2.716** | **0.0066** | 0.2061 | ** |
| **Education: graduate level (vs college)** | **-0.6052** | 0.1018 | ±0.2035 | **-5.947** | **2.73e-09** | 0.5460 | *** |
| **Education: high school or below (vs college)** | **+0.7458** | 0.1516 | ±0.3031 | **+4.921** | **8.63e-07** | 2.1080 | *** |
| **Site: UCSD (vs UAB)** | **+0.3550** | 0.1185 | ±0.2371 | **+2.994** | **0.0028** | 1.4261 | ** |
| Site: UW (vs UAB) | +0.0707 | 0.1151 | ±0.2301 | +0.614 | 0.5391 | 1.0732 |  |
| **Age (years)** | **+0.0318** | 0.0045 | ±0.0090 | **+7.056** | **1.71e-12** | 1.0323 | *** |
| **BMI (kg/m2)** | **+0.0138** | 0.0067 | ±0.0135 | **+2.051** | **0.0402** | 1.0139 | * |
| Hypertension | +0.1801 | 0.1017 | ±0.2034 | +1.771 | 0.0765 | 1.1974 | . |
| High cholesterol | -0.0564 | 0.0969 | ±0.1937 | -0.582 | 0.5605 | 0.9452 |  |
| Kidney disease | -0.2103 | 0.1520 | ±0.3041 | -1.383 | 0.1667 | 0.8104 |  |
| Circulatory disease | +0.0972 | 0.1269 | ±0.2538 | +0.766 | 0.4438 | 1.1021 |  |
| **Avg. daily time 54-250 (%)** | **-0.0126** | 0.0045 | ±0.0089 | **-2.814** | **0.0049** | 0.9875 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0662**, LLR χ² = **190.68** (p = **6.36e-35**), AUC = **0.6739**, AIC = **2712.6**, BIC = **2780.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7664** | 0.3860 | ±0.7721 | **-7.166** | **7.70e-13** | 0.0629 | *** |
| **Education: graduate level (vs college)** | **-0.6164** | 0.1018 | ±0.2036 | **-6.055** | **1.40e-09** | 0.5399 | *** |
| **Education: high school or below (vs college)** | **+0.7446** | 0.1516 | ±0.3032 | **+4.912** | **9.02e-07** | 2.1057 | *** |
| **Site: UCSD (vs UAB)** | **+0.3612** | 0.1187 | ±0.2375 | **+3.042** | **0.0023** | 1.4351 | ** |
| Site: UW (vs UAB) | +0.0595 | 0.1151 | ±0.2301 | +0.518 | 0.6048 | 1.0614 |  |
| **Age (years)** | **+0.0303** | 0.0045 | ±0.0090 | **+6.694** | **2.17e-11** | 1.0308 | *** |
| BMI (kg/m2) | +0.0128 | 0.0068 | ±0.0135 | +1.891 | 0.0587 | 1.0129 | . |
| Hypertension | +0.1689 | 0.1020 | ±0.2039 | +1.656 | 0.0976 | 1.1840 | . |
| High cholesterol | -0.0735 | 0.0972 | ±0.1944 | -0.756 | 0.4496 | 0.9292 |  |
| Kidney disease | -0.2456 | 0.1529 | ±0.3058 | -1.606 | 0.1083 | 0.7823 |  |
| Circulatory disease | +0.0998 | 0.1269 | ±0.2538 | +0.786 | 0.4318 | 1.1049 |  |
| **Time 181-250, pooled (%)** | **+0.0133** | 0.0037 | ±0.0073 | **+3.610** | **3.06e-04** | 1.0133 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0662**, LLR χ² = **190.70** (p = **6.31e-35**), AUC = **0.6739**, AIC = **2712.6**, BIC = **2780.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7684** | 0.3861 | ±0.7722 | **-7.170** | **7.49e-13** | 0.0628 | *** |
| **Education: graduate level (vs college)** | **-0.6172** | 0.1018 | ±0.2036 | **-6.062** | **1.34e-09** | 0.5395 | *** |
| **Education: high school or below (vs college)** | **+0.7435** | 0.1516 | ±0.3032 | **+4.904** | **9.38e-07** | 2.1032 | *** |
| **Site: UCSD (vs UAB)** | **+0.3630** | 0.1188 | ±0.2375 | **+3.056** | **0.0022** | 1.4376 | ** |
| Site: UW (vs UAB) | +0.0609 | 0.1151 | ±0.2302 | +0.529 | 0.5968 | 1.0628 |  |
| **Age (years)** | **+0.0304** | 0.0045 | ±0.0090 | **+6.710** | **1.94e-11** | 1.0308 | *** |
| BMI (kg/m2) | +0.0128 | 0.0068 | ±0.0135 | +1.887 | 0.0591 | 1.0128 | . |
| Hypertension | +0.1690 | 0.1020 | ±0.2039 | +1.657 | 0.0975 | 1.1841 | . |
| High cholesterol | -0.0738 | 0.0972 | ±0.1944 | -0.759 | 0.4476 | 0.9288 |  |
| Kidney disease | -0.2460 | 0.1529 | ±0.3059 | -1.608 | 0.1078 | 0.7819 |  |
| Circulatory disease | +0.1002 | 0.1269 | ±0.2537 | +0.789 | 0.4299 | 1.1053 |  |
| **Avg. daily time 181-250 (%)** | **+0.0131** | 0.0036 | ±0.0073 | **+3.613** | **3.03e-04** | 1.0132 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0670**, LLR χ² = **192.97** (p = **2.13e-35**), AUC = **0.6732**, AIC = **2710.3**, BIC = **2778.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8028** | 0.3863 | ±0.7725 | **-7.256** | **3.98e-13** | 0.0606 | *** |
| **Education: graduate level (vs college)** | **-0.6071** | 0.1019 | ±0.2038 | **-5.959** | **2.54e-09** | 0.5449 | *** |
| **Education: high school or below (vs college)** | **+0.7284** | 0.1519 | ±0.3039 | **+4.795** | **1.63e-06** | 2.0719 | *** |
| **Site: UCSD (vs UAB)** | **+0.3672** | 0.1189 | ±0.2377 | **+3.090** | **0.0020** | 1.4437 | ** |
| Site: UW (vs UAB) | +0.0722 | 0.1152 | ±0.2305 | +0.626 | 0.5310 | 1.0749 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.844** | **7.71e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0128 | 0.0068 | ±0.0135 | +1.888 | 0.0591 | 1.0128 | . |
| Hypertension | +0.1660 | 0.1020 | ±0.2041 | +1.627 | 0.1038 | 1.1805 |  |
| High cholesterol | -0.0703 | 0.0972 | ±0.1943 | -0.723 | 0.4694 | 0.9321 |  |
| Kidney disease | -0.2479 | 0.1530 | ±0.3061 | -1.620 | 0.1052 | 0.7804 |  |
| Circulatory disease | +0.0944 | 0.1271 | ±0.2542 | +0.742 | 0.4578 | 1.0990 |  |
| **Time > 180 (%)** | **+0.0091** | 0.0023 | ±0.0047 | **+3.892** | **9.94e-05** | 1.0091 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0669**, LLR χ² = **192.59** (p = **2.56e-35**), AUC = **0.6731**, AIC = **2710.7**, BIC = **2778.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8000** | 0.3862 | ±0.7725 | **-7.249** | **4.19e-13** | 0.0608 | *** |
| **Education: graduate level (vs college)** | **-0.6080** | 0.1019 | ±0.2037 | **-5.968** | **2.40e-09** | 0.5445 | *** |
| **Education: high school or below (vs college)** | **+0.7285** | 0.1519 | ±0.3038 | **+4.796** | **1.62e-06** | 2.0720 | *** |
| **Site: UCSD (vs UAB)** | **+0.3681** | 0.1189 | ±0.2377 | **+3.097** | **0.0020** | 1.4450 | ** |
| Site: UW (vs UAB) | +0.0721 | 0.1152 | ±0.2305 | +0.626 | 0.5316 | 1.0747 |  |
| **Age (years)** | **+0.0309** | 0.0045 | ±0.0090 | **+6.844** | **7.69e-12** | 1.0314 | *** |
| BMI (kg/m2) | +0.0128 | 0.0068 | ±0.0135 | +1.886 | 0.0593 | 1.0128 | . |
| Hypertension | +0.1668 | 0.1020 | ±0.2040 | +1.635 | 0.1021 | 1.1815 |  |
| High cholesterol | -0.0703 | 0.0972 | ±0.1943 | -0.724 | 0.4692 | 0.9321 |  |
| Kidney disease | -0.2485 | 0.1531 | ±0.3062 | -1.623 | 0.1045 | 0.7799 |  |
| Circulatory disease | +0.0943 | 0.1271 | ±0.2541 | +0.742 | 0.4581 | 1.0989 |  |
| **Avg. daily time > 180 (%)** | **+0.0090** | 0.0023 | ±0.0047 | **+3.844** | **1.21e-04** | 1.0090 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0655**, LLR χ² = **188.70** (p = **1.63e-34**), AUC = **0.6718**, AIC = **2714.5**, BIC = **2782.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7997** | 0.3860 | ±0.7719 | **-7.254** | **4.06e-13** | 0.0608 | *** |
| **Education: graduate level (vs college)** | **-0.6032** | 0.1018 | ±0.2037 | **-5.923** | **3.16e-09** | 0.5471 | *** |
| **Education: high school or below (vs college)** | **+0.7392** | 0.1517 | ±0.3033 | **+4.874** | **1.09e-06** | 2.0943 | *** |
| **Site: UCSD (vs UAB)** | **+0.3627** | 0.1187 | ±0.2375 | **+3.054** | **0.0023** | 1.4372 | ** |
| Site: UW (vs UAB) | +0.0661 | 0.1151 | ±0.2301 | +0.575 | 0.5655 | 1.0684 |  |
| **Age (years)** | **+0.0316** | 0.0045 | ±0.0090 | **+6.996** | **2.64e-12** | 1.0321 | *** |
| BMI (kg/m2) | +0.0122 | 0.0068 | ±0.0135 | +1.807 | 0.0707 | 1.0123 | . |
| Hypertension | +0.1782 | 0.1018 | ±0.2036 | +1.751 | 0.0799 | 1.1951 | . |
| High cholesterol | -0.0646 | 0.0970 | ±0.1940 | -0.666 | 0.5057 | 0.9375 |  |
| Kidney disease | -0.2241 | 0.1524 | ±0.3047 | -1.471 | 0.1414 | 0.7993 |  |
| Circulatory disease | +0.0981 | 0.1270 | ±0.2540 | +0.772 | 0.4400 | 1.1030 |  |
| **Nocturnal time > 180 (%)** | **+0.0077** | 0.0023 | ±0.0047 | **+3.312** | **9.28e-04** | 1.0078 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0648**, LLR χ² = **186.51** (p = **4.63e-34**), AUC = **0.6735**, AIC = **2716.7**, BIC = **2784.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8443** | 0.3859 | ±0.7719 | **-7.370** | **1.71e-13** | 0.0582 | *** |
| **Education: graduate level (vs college)** | **-0.6062** | 0.1018 | ±0.2035 | **-5.958** | **2.56e-09** | 0.5454 | *** |
| **Education: high school or below (vs college)** | **+0.7647** | 0.1512 | ±0.3024 | **+5.057** | **4.26e-07** | 2.1483 | *** |
| **Site: UCSD (vs UAB)** | **+0.3501** | 0.1185 | ±0.2370 | **+2.955** | **0.0031** | 1.4192 | ** |
| Site: UW (vs UAB) | +0.0551 | 0.1148 | ±0.2297 | +0.480 | 0.6314 | 1.0566 |  |
| **Age (years)** | **+0.0305** | 0.0045 | ±0.0090 | **+6.757** | **1.41e-11** | 1.0310 | *** |
| **BMI (kg/m2)** | **+0.0149** | 0.0067 | ±0.0135 | **+2.212** | **0.0270** | 1.0150 | * |
| Hypertension | +0.1664 | 0.1020 | ±0.2041 | +1.630 | 0.1030 | 1.1810 |  |
| High cholesterol | -0.0704 | 0.0971 | ±0.1942 | -0.725 | 0.4687 | 0.9321 |  |
| Kidney disease | -0.2229 | 0.1522 | ±0.3044 | -1.465 | 0.1430 | 0.8002 |  |
| Circulatory disease | +0.1111 | 0.1267 | ±0.2534 | +0.877 | 0.3805 | 1.1175 |  |
| **Any reading > 250 during wear (0/1)** | **+0.2899** | 0.0970 | ±0.1939 | **+2.990** | **0.0028** | 1.3363 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0648**, LLR χ² = **186.45** (p = **4.77e-34**), AUC = **0.6706**, AIC = **2716.8**, BIC = **2784.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8401** | 0.3860 | ±0.7720 | **-7.358** | **1.87e-13** | 0.0584 | *** |
| **Education: graduate level (vs college)** | **-0.6050** | 0.1018 | ±0.2035 | **-5.944** | **2.77e-09** | 0.5461 | *** |
| **Education: high school or below (vs college)** | **+0.7442** | 0.1516 | ±0.3032 | **+4.909** | **9.15e-07** | 2.1048 | *** |
| **Site: UCSD (vs UAB)** | **+0.3538** | 0.1185 | ±0.2371 | **+2.985** | **0.0028** | 1.4244 | ** |
| Site: UW (vs UAB) | +0.0704 | 0.1151 | ±0.2301 | +0.612 | 0.5404 | 1.0730 |  |
| **Age (years)** | **+0.0319** | 0.0045 | ±0.0090 | **+7.069** | **1.56e-12** | 1.0324 | *** |
| **BMI (kg/m2)** | **+0.0138** | 0.0067 | ±0.0135 | **+2.050** | **0.0403** | 1.0139 | * |
| Hypertension | +0.1789 | 0.1017 | ±0.2034 | +1.759 | 0.0785 | 1.1959 | . |
| High cholesterol | -0.0571 | 0.0969 | ±0.1938 | -0.589 | 0.5557 | 0.9445 |  |
| Kidney disease | -0.2096 | 0.1520 | ±0.3040 | -1.379 | 0.1679 | 0.8109 |  |
| Circulatory disease | +0.0980 | 0.1269 | ±0.2538 | +0.772 | 0.4399 | 1.1030 |  |
| **Time > 250 (%)** | **+0.0127** | 0.0044 | ±0.0088 | **+2.885** | **0.0039** | 1.0128 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,138)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2138**, events = **857**, McFadden pseudo-R² = **0.0646**, LLR χ² = **185.91** (p = **6.16e-34**), AUC = **0.6703**, AIC = **2717.3**, BIC = **2785.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8346** | 0.3859 | ±0.7718 | **-7.346** | **2.05e-13** | 0.0587 | *** |
| **Education: graduate level (vs college)** | **-0.6056** | 0.1018 | ±0.2035 | **-5.952** | **2.66e-09** | 0.5457 | *** |
| **Education: high school or below (vs college)** | **+0.7452** | 0.1516 | ±0.3031 | **+4.916** | **8.83e-07** | 2.1068 | *** |
| **Site: UCSD (vs UAB)** | **+0.3535** | 0.1185 | ±0.2370 | **+2.983** | **0.0029** | 1.4240 | ** |
| Site: UW (vs UAB) | +0.0691 | 0.1150 | ±0.2300 | +0.601 | 0.5477 | 1.0716 |  |
| **Age (years)** | **+0.0318** | 0.0045 | ±0.0090 | **+7.057** | **1.71e-12** | 1.0323 | *** |
| **BMI (kg/m2)** | **+0.0138** | 0.0067 | ±0.0135 | **+2.052** | **0.0402** | 1.0139 | * |
| Hypertension | +0.1800 | 0.1017 | ±0.2034 | +1.770 | 0.0767 | 1.1972 | . |
| High cholesterol | -0.0569 | 0.0969 | ±0.1937 | -0.588 | 0.5566 | 0.9446 |  |
| Kidney disease | -0.2100 | 0.1520 | ±0.3041 | -1.382 | 0.1671 | 0.8106 |  |
| Circulatory disease | +0.0977 | 0.1269 | ±0.2538 | +0.769 | 0.4416 | 1.1026 |  |
| **Avg. daily time > 250 (%)** | **+0.0125** | 0.0045 | ±0.0089 | **+2.797** | **0.0052** | 1.0126 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 2,138; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2138**, R² = **0.0762**, Adj R² = **0.0719**, F-statistic = **17.56** (p = **4.46e-31**), Residual SE = **2.624** on **2127** df, AIC = **10204.1**, BIC = **10266.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1125** | 0.4706 | ±0.9412 | **+34.239** | **6.35e-257** | *** |
| **Education: graduate level (vs college)** | **+0.2530** | 0.1221 | ±0.2441 | **+2.073** | **0.0382** | * |
| **Education: high school or below (vs college)** | **-1.1206** | 0.2280 | ±0.4560 | **-4.915** | **8.87e-07** | *** |
| Site: UCSD (vs UAB) | +0.1003 | 0.1543 | ±0.3087 | +0.650 | 0.5156 |  |
| Site: UW (vs UAB) | +0.0377 | 0.1460 | ±0.2921 | +0.258 | 0.7964 |  |
| **Age (years)** | **-0.0515** | 0.0059 | ±0.0118 | **-8.759** | **1.97e-18** | *** |
| BMI (kg/m2) | -0.0103 | 0.0081 | ±0.0162 | -1.273 | 0.2031 |  |
| **Hypertension** | **-0.4192** | 0.1250 | ±0.2501 | **-3.352** | **8.02e-04** | *** |
| High cholesterol | +0.1843 | 0.1222 | ±0.2444 | +1.509 | 0.1314 |  |
| Kidney disease | -0.0777 | 0.2061 | ±0.4121 | -0.377 | 0.7061 |  |
| Circulatory disease | +0.1221 | 0.1592 | ±0.3184 | +0.767 | 0.4432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2138**, R² = **0.0794**, Adj R² = **0.0747**, F-statistic = **16.68** (p = **5.91e-32**), Residual SE = **2.621** on **2126** df, AIC = **10198.8**, BIC = **10266.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8937** | 0.5557 | ±1.1114 | **+30.402** | **5.23e-203** | *** |
| Education: graduate level (vs college) | +0.2338 | 0.1220 | ±0.2441 | +1.916 | 0.0553 | . |
| **Education: high school or below (vs college)** | **-1.0612** | 0.2293 | ±0.4586 | **-4.628** | **3.70e-06** | *** |
| Site: UCSD (vs UAB) | +0.0860 | 0.1543 | ±0.3087 | +0.558 | 0.5772 |  |
| Site: UW (vs UAB) | +0.0181 | 0.1461 | ±0.2921 | +0.124 | 0.9011 |  |
| **Age (years)** | **-0.0506** | 0.0059 | ±0.0117 | **-8.645** | **5.37e-18** | *** |
| BMI (kg/m2) | -0.0076 | 0.0082 | ±0.0164 | -0.924 | 0.3556 |  |
| **Hypertension** | **-0.3865** | 0.1244 | ±0.2489 | **-3.106** | **0.0019** | ** |
| High cholesterol | +0.2127 | 0.1224 | ±0.2448 | +1.738 | 0.0822 | . |
| Kidney disease | -0.0511 | 0.2068 | ±0.4137 | -0.247 | 0.8050 |  |
| Circulatory disease | +0.1360 | 0.1589 | ±0.3177 | +0.856 | 0.3921 |  |
| **HbA1c (%)** | **-0.1537** | 0.0557 | ±0.1115 | **-2.757** | **0.0058** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2138**, R² = **0.0812**, Adj R² = **0.0764**, F-statistic = **17.07** (p = **8.81e-33**), Residual SE = **2.618** on **2126** df, AIC = **10194.8**, BIC = **10262.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7473** | 0.5001 | ±1.0001 | **+33.491** | **6.52e-246** | *** |
| **Education: graduate level (vs college)** | **+0.2396** | 0.1219 | ±0.2439 | **+1.965** | **0.0494** | * |
| **Education: high school or below (vs college)** | **-1.0530** | 0.2274 | ±0.4548 | **-4.630** | **3.65e-06** | *** |
| Site: UCSD (vs UAB) | +0.0753 | 0.1537 | ±0.3075 | +0.489 | 0.6245 |  |
| Site: UW (vs UAB) | +0.0237 | 0.1455 | ±0.2910 | +0.163 | 0.8709 |  |
| **Age (years)** | **-0.0506** | 0.0059 | ±0.0117 | **-8.625** | **6.40e-18** | *** |
| BMI (kg/m2) | -0.0081 | 0.0082 | ±0.0164 | -0.984 | 0.3249 |  |
| **Hypertension** | **-0.3797** | 0.1250 | ±0.2500 | **-3.038** | **0.0024** | ** |
| High cholesterol | +0.2083 | 0.1223 | ±0.2447 | +1.702 | 0.0887 | . |
| Kidney disease | -0.0133 | 0.2086 | ±0.4173 | -0.064 | 0.9490 |  |
| Circulatory disease | +0.1401 | 0.1587 | ±0.3173 | +0.883 | 0.3772 |  |
| **Mean glucose (mg/dL)** | **-0.0058** | 0.0017 | ±0.0034 | **-3.431** | **6.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2138**, R² = **0.0812**, Adj R² = **0.0764**, F-statistic = **17.07** (p = **8.81e-33**), Residual SE = **2.618** on **2126** df, AIC = **10194.8**, BIC = **10262.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.5564** | 0.6199 | ±1.2397 | **+28.324** | **1.77e-176** | *** |
| **Education: graduate level (vs college)** | **+0.2396** | 0.1219 | ±0.2439 | **+1.965** | **0.0494** | * |
| **Education: high school or below (vs college)** | **-1.0530** | 0.2274 | ±0.4548 | **-4.630** | **3.65e-06** | *** |
| Site: UCSD (vs UAB) | +0.0753 | 0.1537 | ±0.3075 | +0.489 | 0.6245 |  |
| Site: UW (vs UAB) | +0.0237 | 0.1455 | ±0.2910 | +0.163 | 0.8709 |  |
| **Age (years)** | **-0.0506** | 0.0059 | ±0.0117 | **-8.625** | **6.40e-18** | *** |
| BMI (kg/m2) | -0.0081 | 0.0082 | ±0.0164 | -0.984 | 0.3249 |  |
| **Hypertension** | **-0.3797** | 0.1250 | ±0.2500 | **-3.038** | **0.0024** | ** |
| High cholesterol | +0.2083 | 0.1223 | ±0.2447 | +1.702 | 0.0887 | . |
| Kidney disease | -0.0133 | 0.2086 | ±0.4173 | -0.064 | 0.9490 |  |
| Circulatory disease | +0.1401 | 0.1587 | ±0.3173 | +0.883 | 0.3772 |  |
| **GMI (%)** | **-0.2445** | 0.0712 | ±0.1425 | **-3.431** | **6.01e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2138**, R² = **0.0820**, Adj R² = **0.0772**, F-statistic = **17.26** (p = **3.56e-33**), Residual SE = **2.617** on **2126** df, AIC = **10192.8**, BIC = **10260.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7996** | 0.4965 | ±0.9930 | **+33.836** | **5.88e-251** | *** |
| Education: graduate level (vs college) | +0.2367 | 0.1218 | ±0.2437 | +1.943 | 0.0520 | . |
| **Education: high school or below (vs college)** | **-1.0510** | 0.2273 | ±0.4545 | **-4.625** | **3.75e-06** | *** |
| Site: UCSD (vs UAB) | +0.0805 | 0.1537 | ±0.3074 | +0.524 | 0.6004 |  |
| Site: UW (vs UAB) | +0.0292 | 0.1456 | ±0.2913 | +0.201 | 0.8409 |  |
| **Age (years)** | **-0.0514** | 0.0059 | ±0.0117 | **-8.763** | **1.91e-18** | *** |
| BMI (kg/m2) | -0.0065 | 0.0083 | ±0.0166 | -0.780 | 0.4352 |  |
| **Hypertension** | **-0.3857** | 0.1248 | ±0.2496 | **-3.091** | **0.0020** | ** |
| High cholesterol | +0.2120 | 0.1224 | ±0.2448 | +1.732 | 0.0832 | . |
| Kidney disease | -0.0298 | 0.2077 | ±0.4154 | -0.144 | 0.8857 |  |
| Circulatory disease | +0.1378 | 0.1582 | ±0.3165 | +0.871 | 0.3839 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0063** | 0.0017 | ±0.0034 | **-3.703** | **2.13e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2138**, R² = **0.0800**, Adj R² = **0.0752**, F-statistic = **16.80** (p = **3.21e-32**), Residual SE = **2.620** on **2126** df, AIC = **10197.5**, BIC = **10265.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3635** | 0.4803 | ±0.9605 | **+34.072** | **1.90e-254** | *** |
| Education: graduate level (vs college) | +0.2332 | 0.1220 | ±0.2440 | +1.911 | 0.0559 | . |
| **Education: high school or below (vs college)** | **-1.0676** | 0.2288 | ±0.4575 | **-4.667** | **3.06e-06** | *** |
| Site: UCSD (vs UAB) | +0.0714 | 0.1541 | ±0.3083 | +0.463 | 0.6431 |  |
| Site: UW (vs UAB) | +0.0126 | 0.1458 | ±0.2916 | +0.087 | 0.9311 |  |
| **Age (years)** | **-0.0501** | 0.0059 | ±0.0117 | **-8.539** | **1.35e-17** | *** |
| BMI (kg/m2) | -0.0089 | 0.0082 | ±0.0163 | -1.096 | 0.2730 |  |
| **Hypertension** | **-0.3794** | 0.1246 | ±0.2492 | **-3.045** | **0.0023** | ** |
| High cholesterol | +0.1998 | 0.1221 | ±0.2443 | +1.636 | 0.1019 |  |
| Kidney disease | +0.0171 | 0.2115 | ±0.4229 | +0.081 | 0.9357 |  |
| Circulatory disease | +0.1395 | 0.1588 | ±0.3177 | +0.879 | 0.3796 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0147** | 0.0051 | ±0.0102 | **-2.870** | **0.0041** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2138**, R² = **0.0801**, Adj R² = **0.0753**, F-statistic = **16.82** (p = **2.95e-32**), Residual SE = **2.620** on **2126** df, AIC = **10197.3**, BIC = **10265.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3683** | 0.4803 | ±0.9606 | **+34.080** | **1.45e-254** | *** |
| Education: graduate level (vs college) | +0.2351 | 0.1221 | ±0.2441 | +1.926 | 0.0541 | . |
| **Education: high school or below (vs college)** | **-1.0651** | 0.2286 | ±0.4573 | **-4.659** | **3.18e-06** | *** |
| Site: UCSD (vs UAB) | +0.0729 | 0.1538 | ±0.3076 | +0.474 | 0.6357 |  |
| Site: UW (vs UAB) | +0.0154 | 0.1457 | ±0.2914 | +0.106 | 0.9156 |  |
| **Age (years)** | **-0.0499** | 0.0059 | ±0.0117 | **-8.508** | **1.76e-17** | *** |
| BMI (kg/m2) | -0.0092 | 0.0082 | ±0.0163 | -1.128 | 0.2595 |  |
| **Hypertension** | **-0.3796** | 0.1248 | ±0.2496 | **-3.041** | **0.0024** | ** |
| High cholesterol | +0.2002 | 0.1222 | ±0.2443 | +1.639 | 0.1012 |  |
| Kidney disease | +0.0201 | 0.2112 | ±0.4224 | +0.095 | 0.9241 |  |
| Circulatory disease | +0.1371 | 0.1590 | ±0.3180 | +0.862 | 0.3887 |  |
| **Avg. daily SD (mg/dL)** | **-0.0167** | 0.0057 | ±0.0113 | **-2.951** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2138**, R² = **0.0771**, Adj R² = **0.0724**, F-statistic = **16.15** (p = **7.28e-31**), Residual SE = **2.624** on **2126** df, AIC = **10204.1**, BIC = **10272.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3667** | 0.5125 | ±1.0250 | **+31.937** | **8.31e-224** | *** |
| **Education: graduate level (vs college)** | **+0.2436** | 0.1221 | ±0.2441 | **+1.996** | **0.0460** | * |
| **Education: high school or below (vs college)** | **-1.1059** | 0.2291 | ±0.4581 | **-4.828** | **1.38e-06** | *** |
| Site: UCSD (vs UAB) | +0.0863 | 0.1547 | ±0.3093 | +0.558 | 0.5767 |  |
| Site: UW (vs UAB) | +0.0244 | 0.1464 | ±0.2928 | +0.167 | 0.8676 |  |
| **Age (years)** | **-0.0507** | 0.0059 | ±0.0117 | **-8.633** | **5.95e-18** | *** |
| BMI (kg/m2) | -0.0101 | 0.0081 | ±0.0162 | -1.248 | 0.2122 |  |
| **Hypertension** | **-0.4027** | 0.1246 | ±0.2491 | **-3.233** | **0.0012** | ** |
| High cholesterol | +0.1862 | 0.1221 | ±0.2443 | +1.525 | 0.1273 |  |
| Kidney disease | -0.0340 | 0.2101 | ±0.4203 | -0.162 | 0.8713 |  |
| Circulatory disease | +0.1286 | 0.1593 | ±0.3185 | +0.807 | 0.4196 |  |
| CV (%) | -0.0158 | 0.0113 | ±0.0227 | -1.399 | 0.1618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2138**, R² = **0.0765**, Adj R² = **0.0717**, F-statistic = **16.01** (p = **1.49e-30**), Residual SE = **2.625** on **2126** df, AIC = **10205.6**, BIC = **10273.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9088** | 0.5343 | ±1.0687 | **+29.774** | **8.59e-195** | *** |
| **Education: graduate level (vs college)** | **+0.2482** | 0.1220 | ±0.2439 | **+2.035** | **0.0419** | * |
| **Education: high school or below (vs college)** | **-1.1124** | 0.2289 | ±0.4578 | **-4.859** | **1.18e-06** | *** |
| Site: UCSD (vs UAB) | +0.0942 | 0.1548 | ±0.3097 | +0.608 | 0.5431 |  |
| Site: UW (vs UAB) | +0.0330 | 0.1465 | ±0.2930 | +0.225 | 0.8220 |  |
| **Age (years)** | **-0.0511** | 0.0059 | ±0.0117 | **-8.714** | **2.94e-18** | *** |
| BMI (kg/m2) | -0.0102 | 0.0081 | ±0.0162 | -1.259 | 0.2079 |  |
| **Hypertension** | **-0.4104** | 0.1245 | ±0.2489 | **-3.298** | **9.75e-04** | *** |
| High cholesterol | +0.1858 | 0.1222 | ±0.2444 | +1.521 | 0.1283 |  |
| Kidney disease | -0.0602 | 0.2089 | ±0.4178 | -0.288 | 0.7732 |  |
| Circulatory disease | +0.1255 | 0.1592 | ±0.3184 | +0.788 | 0.4305 |  |
| Mean / SD ratio | +0.0318 | 0.0452 | ±0.0905 | +0.703 | 0.4818 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2138**, R² = **0.0767**, Adj R² = **0.0719**, F-statistic = **16.05** (p = **1.22e-30**), Residual SE = **2.624** on **2126** df, AIC = **10205.2**, BIC = **10273.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8440** | 0.5286 | ±1.0573 | **+29.971** | **2.36e-197** | *** |
| **Education: graduate level (vs college)** | **+0.2476** | 0.1221 | ±0.2441 | **+2.028** | **0.0426** | * |
| **Education: high school or below (vs college)** | **-1.1094** | 0.2288 | ±0.4575 | **-4.850** | **1.24e-06** | *** |
| Site: UCSD (vs UAB) | +0.0948 | 0.1544 | ±0.3089 | +0.614 | 0.5394 |  |
| Site: UW (vs UAB) | +0.0330 | 0.1463 | ±0.2926 | +0.225 | 0.8217 |  |
| **Age (years)** | **-0.0509** | 0.0059 | ±0.0117 | **-8.680** | **3.95e-18** | *** |
| BMI (kg/m2) | -0.0102 | 0.0081 | ±0.0162 | -1.256 | 0.2090 |  |
| **Hypertension** | **-0.4089** | 0.1247 | ±0.2494 | **-3.279** | **0.0010** | ** |
| High cholesterol | +0.1858 | 0.1222 | ±0.2443 | +1.521 | 0.1283 |  |
| Kidney disease | -0.0555 | 0.2083 | ±0.4166 | -0.266 | 0.7899 |  |
| Circulatory disease | +0.1240 | 0.1592 | ±0.3185 | +0.779 | 0.4362 |  |
| Avg. daily mean/SD | +0.0355 | 0.0367 | ±0.0735 | +0.967 | 0.3336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2138**, R² = **0.0779**, Adj R² = **0.0732**, F-statistic = **16.33** (p = **3.06e-31**), Residual SE = **2.623** on **2126** df, AIC = **10202.3**, BIC = **10270.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.6274** | 0.5396 | ±1.0792 | **+30.813** | **1.73e-208** | *** |
| Education: graduate level (vs college) | +0.2398 | 0.1226 | ±0.2452 | +1.956 | 0.0504 | . |
| **Education: high school or below (vs college)** | **-1.0983** | 0.2270 | ±0.4539 | **-4.839** | **1.30e-06** | *** |
| Site: UCSD (vs UAB) | +0.0815 | 0.1537 | ±0.3074 | +0.530 | 0.5961 |  |
| Site: UW (vs UAB) | +0.0087 | 0.1456 | ±0.2913 | +0.060 | 0.9524 |  |
| **Age (years)** | **-0.0517** | 0.0059 | ±0.0118 | **-8.793** | **1.45e-18** | *** |
| BMI (kg/m2) | -0.0097 | 0.0081 | ±0.0162 | -1.196 | 0.2319 |  |
| **Hypertension** | **-0.4128** | 0.1250 | ±0.2501 | **-3.301** | **9.62e-04** | *** |
| High cholesterol | +0.1829 | 0.1222 | ±0.2443 | +1.497 | 0.1344 |  |
| Kidney disease | -0.0458 | 0.2092 | ±0.4184 | -0.219 | 0.8266 |  |
| Circulatory disease | +0.1261 | 0.1598 | ±0.3197 | +0.789 | 0.4301 |  |
| MAG (mg/dL/h) | -0.0127 | 0.0065 | ±0.0130 | -1.940 | 0.0524 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2138**, R² = **0.0793**, Adj R² = **0.0746**, F-statistic = **16.65** (p = **6.55e-32**), Residual SE = **2.621** on **2126** df, AIC = **10199.0**, BIC = **10267.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4819** | 0.4916 | ±0.9832 | **+33.528** | **1.91e-246** | *** |
| Education: graduate level (vs college) | +0.2374 | 0.1222 | ±0.2444 | +1.943 | 0.0520 | . |
| **Education: high school or below (vs college)** | **-1.0727** | 0.2283 | ±0.4566 | **-4.699** | **2.62e-06** | *** |
| Site: UCSD (vs UAB) | +0.0737 | 0.1537 | ±0.3075 | +0.480 | 0.6316 |  |
| Site: UW (vs UAB) | +0.0166 | 0.1456 | ±0.2912 | +0.114 | 0.9091 |  |
| **Age (years)** | **-0.0503** | 0.0059 | ±0.0118 | **-8.552** | **1.21e-17** | *** |
| BMI (kg/m2) | -0.0100 | 0.0081 | ±0.0163 | -1.235 | 0.2167 |  |
| **Hypertension** | **-0.3895** | 0.1249 | ±0.2498 | **-3.119** | **0.0018** | ** |
| High cholesterol | +0.1969 | 0.1222 | ±0.2444 | +1.611 | 0.1071 |  |
| Kidney disease | +0.0047 | 0.2106 | ±0.4211 | +0.022 | 0.9822 |  |
| Circulatory disease | +0.1371 | 0.1592 | ±0.3184 | +0.861 | 0.3892 |  |
| **Avg. daily range (mg/dL)** | **-0.0041** | 0.0015 | ±0.0031 | **-2.621** | **0.0088** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2138**, R² = **0.0784**, Adj R² = **0.0736**, F-statistic = **16.44** (p = **1.85e-31**), Residual SE = **2.622** on **2126** df, AIC = **10201.2**, BIC = **10269.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2275** | 0.4733 | ±0.9466 | **+34.285** | **1.31e-257** | *** |
| Education: graduate level (vs college) | +0.2352 | 0.1220 | ±0.2439 | +1.928 | 0.0538 | . |
| **Education: high school or below (vs college)** | **-1.0954** | 0.2284 | ±0.4568 | **-4.796** | **1.62e-06** | *** |
| Site: UCSD (vs UAB) | +0.0817 | 0.1551 | ±0.3101 | +0.527 | 0.5983 |  |
| Site: UW (vs UAB) | +0.0194 | 0.1464 | ±0.2928 | +0.132 | 0.8948 |  |
| **Age (years)** | **-0.0514** | 0.0059 | ±0.0117 | **-8.746** | **2.22e-18** | *** |
| BMI (kg/m2) | -0.0086 | 0.0081 | ±0.0163 | -1.056 | 0.2910 |  |
| **Hypertension** | **-0.3984** | 0.1244 | ±0.2488 | **-3.203** | **0.0014** | ** |
| High cholesterol | +0.1963 | 0.1223 | ±0.2447 | +1.605 | 0.1085 |  |
| Kidney disease | -0.0330 | 0.2088 | ±0.4176 | -0.158 | 0.8746 |  |
| Circulatory disease | +0.1438 | 0.1584 | ±0.3168 | +0.908 | 0.3641 |  |
| **SD of daily means (mg/dL)** | **-0.0206** | 0.0103 | ±0.0206 | **-1.996** | **0.0459** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2138**, R² = **0.0797**, Adj R² = **0.0749**, F-statistic = **16.74** (p = **4.38e-32**), Residual SE = **2.620** on **2126** df, AIC = **10198.1**, BIC = **10266.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2743** | 0.5566 | ±1.1133 | **+27.440** | **9.19e-166** | *** |
| Education: graduate level (vs college) | +0.2364 | 0.1220 | ±0.2440 | +1.937 | 0.0527 | . |
| **Education: high school or below (vs college)** | **-1.0669** | 0.2276 | ±0.4552 | **-4.687** | **2.77e-06** | *** |
| Site: UCSD (vs UAB) | +0.0686 | 0.1544 | ±0.3088 | +0.445 | 0.6567 |  |
| Site: UW (vs UAB) | +0.0146 | 0.1458 | ±0.2916 | +0.100 | 0.9202 |  |
| **Age (years)** | **-0.0507** | 0.0059 | ±0.0117 | **-8.646** | **5.31e-18** | *** |
| BMI (kg/m2) | -0.0085 | 0.0082 | ±0.0164 | -1.037 | 0.2995 |  |
| **Hypertension** | **-0.3950** | 0.1246 | ±0.2491 | **-3.171** | **0.0015** | ** |
| High cholesterol | +0.1989 | 0.1222 | ±0.2444 | +1.628 | 0.1035 |  |
| Kidney disease | -0.0162 | 0.2090 | ±0.4179 | -0.077 | 0.9383 |  |
| Circulatory disease | +0.1381 | 0.1588 | ±0.3177 | +0.870 | 0.3845 |  |
| **Time in range 70-180, pooled (%)** | **+0.0083** | 0.0029 | ±0.0058 | **+2.872** | **0.0041** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2138**, R² = **0.0797**, Adj R² = **0.0749**, F-statistic = **16.74** (p = **4.37e-32**), Residual SE = **2.620** on **2126** df, AIC = **10198.1**, BIC = **10266.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2721** | 0.5576 | ±1.1151 | **+27.391** | **3.54e-165** | *** |
| Education: graduate level (vs college) | +0.2369 | 0.1220 | ±0.2440 | +1.941 | 0.0522 | . |
| **Education: high school or below (vs college)** | **-1.0663** | 0.2276 | ±0.4553 | **-4.684** | **2.81e-06** | *** |
| Site: UCSD (vs UAB) | +0.0682 | 0.1544 | ±0.3088 | +0.442 | 0.6585 |  |
| Site: UW (vs UAB) | +0.0145 | 0.1458 | ±0.2916 | +0.100 | 0.9207 |  |
| **Age (years)** | **-0.0506** | 0.0059 | ±0.0117 | **-8.640** | **5.64e-18** | *** |
| BMI (kg/m2) | -0.0085 | 0.0082 | ±0.0164 | -1.032 | 0.3018 |  |
| **Hypertension** | **-0.3954** | 0.1246 | ±0.2491 | **-3.175** | **0.0015** | ** |
| High cholesterol | +0.1993 | 0.1222 | ±0.2444 | +1.631 | 0.1029 |  |
| Kidney disease | -0.0150 | 0.2089 | ±0.4178 | -0.072 | 0.9428 |  |
| Circulatory disease | +0.1381 | 0.1588 | ±0.3176 | +0.870 | 0.3845 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0083** | 0.0029 | ±0.0058 | **+2.867** | **0.0041** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2138**, R² = **0.0774**, Adj R² = **0.0726**, F-statistic = **16.21** (p = **5.57e-31**), Residual SE = **2.623** on **2126** df, AIC = **10203.5**, BIC = **10271.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0128** | 0.4766 | ±0.9532 | **+33.598** | **1.77e-247** | *** |
| **Education: graduate level (vs college)** | **+0.2582** | 0.1218 | ±0.2437 | **+2.119** | **0.0341** | * |
| **Education: high school or below (vs college)** | **-1.1019** | 0.2277 | ±0.4554 | **-4.839** | **1.30e-06** | *** |
| Site: UCSD (vs UAB) | +0.1244 | 0.1555 | ±0.3109 | +0.800 | 0.4235 |  |
| Site: UW (vs UAB) | +0.0508 | 0.1467 | ±0.2934 | +0.346 | 0.7291 |  |
| **Age (years)** | **-0.0509** | 0.0059 | ±0.0118 | **-8.643** | **5.49e-18** | *** |
| BMI (kg/m2) | -0.0108 | 0.0081 | ±0.0162 | -1.336 | 0.1817 |  |
| **Hypertension** | **-0.4211** | 0.1250 | ±0.2501 | **-3.368** | **7.58e-04** | *** |
| High cholesterol | +0.1968 | 0.1220 | ±0.2439 | +1.613 | 0.1067 |  |
| Kidney disease | -0.0713 | 0.2062 | ±0.4125 | -0.346 | 0.7295 |  |
| Circulatory disease | +0.1067 | 0.1593 | ±0.3186 | +0.670 | 0.5031 |  |
| Any reading < 54 during wear (0/1) | +0.2038 | 0.1226 | ±0.2452 | +1.662 | 0.0965 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2138**, R² = **0.0767**, Adj R² = **0.0719**, F-statistic = **16.05** (p = **1.23e-30**), Residual SE = **2.624** on **2126** df, AIC = **10205.2**, BIC = **10273.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0766** | 0.4732 | ±0.9464 | **+33.975** | **5.27e-253** | *** |
| **Education: graduate level (vs college)** | **+0.2552** | 0.1220 | ±0.2439 | **+2.093** | **0.0364** | * |
| **Education: high school or below (vs college)** | **-1.1118** | 0.2281 | ±0.4562 | **-4.874** | **1.09e-06** | *** |
| Site: UCSD (vs UAB) | +0.1164 | 0.1558 | ±0.3116 | +0.747 | 0.4551 |  |
| Site: UW (vs UAB) | +0.0506 | 0.1471 | ±0.2943 | +0.344 | 0.7311 |  |
| **Age (years)** | **-0.0514** | 0.0059 | ±0.0118 | **-8.738** | **2.37e-18** | *** |
| BMI (kg/m2) | -0.0103 | 0.0081 | ±0.0162 | -1.271 | 0.2037 |  |
| **Hypertension** | **-0.4169** | 0.1251 | ±0.2502 | **-3.332** | **8.62e-04** | *** |
| High cholesterol | +0.1910 | 0.1224 | ±0.2449 | +1.560 | 0.1188 |  |
| Kidney disease | -0.0771 | 0.2060 | ±0.4120 | -0.374 | 0.7084 |  |
| Circulatory disease | +0.1182 | 0.1593 | ±0.3186 | +0.742 | 0.4580 |  |
| Time < 54 (%) | +0.1089 | 0.0981 | ±0.1963 | +1.109 | 0.2673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2138**, R² = **0.0762**, Adj R² = **0.0715**, F-statistic = **15.95** (p = **1.93e-30**), Residual SE = **2.625** on **2126** df, AIC = **10206.1**, BIC = **10274.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1124** | 0.4723 | ±0.9447 | **+34.111** | **5.02e-255** | *** |
| **Education: graduate level (vs college)** | **+0.2530** | 0.1221 | ±0.2442 | **+2.072** | **0.0382** | * |
| **Education: high school or below (vs college)** | **-1.1206** | 0.2281 | ±0.4561 | **-4.913** | **8.95e-07** | *** |
| Site: UCSD (vs UAB) | +0.1004 | 0.1554 | ±0.3109 | +0.646 | 0.5183 |  |
| Site: UW (vs UAB) | +0.0377 | 0.1473 | ±0.2945 | +0.256 | 0.7978 |  |
| **Age (years)** | **-0.0515** | 0.0059 | ±0.0118 | **-8.758** | **2.00e-18** | *** |
| BMI (kg/m2) | -0.0103 | 0.0081 | ±0.0162 | -1.272 | 0.2032 |  |
| **Hypertension** | **-0.4192** | 0.1252 | ±0.2504 | **-3.348** | **8.15e-04** | *** |
| High cholesterol | +0.1844 | 0.1224 | ±0.2447 | +1.507 | 0.1319 |  |
| Kidney disease | -0.0777 | 0.2061 | ±0.4122 | -0.377 | 0.7061 |  |
| Circulatory disease | +0.1221 | 0.1594 | ±0.3187 | +0.766 | 0.4437 |  |
| Avg. daily time < 54 (%) | +0.0006 | 0.1068 | ±0.2137 | +0.006 | 0.9952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2138**, R² = **0.0763**, Adj R² = **0.0715**, F-statistic = **15.95** (p = **1.91e-30**), Residual SE = **2.625** on **2126** df, AIC = **10206.1**, BIC = **10274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1084** | 0.4737 | ±0.9474 | **+34.007** | **1.75e-253** | *** |
| **Education: graduate level (vs college)** | **+0.2537** | 0.1221 | ±0.2443 | **+2.077** | **0.0378** | * |
| **Education: high school or below (vs college)** | **-1.1198** | 0.2281 | ±0.4562 | **-4.910** | **9.13e-07** | *** |
| Site: UCSD (vs UAB) | +0.1017 | 0.1551 | ±0.3101 | +0.656 | 0.5117 |  |
| Site: UW (vs UAB) | +0.0390 | 0.1468 | ±0.2935 | +0.266 | 0.7903 |  |
| **Age (years)** | **-0.0515** | 0.0059 | ±0.0118 | **-8.751** | **2.12e-18** | *** |
| BMI (kg/m2) | -0.0103 | 0.0081 | ±0.0162 | -1.275 | 0.2023 |  |
| **Hypertension** | **-0.4188** | 0.1252 | ±0.2505 | **-3.344** | **8.27e-04** | *** |
| High cholesterol | +0.1849 | 0.1222 | ±0.2444 | +1.513 | 0.1303 |  |
| Kidney disease | -0.0777 | 0.2061 | ±0.4123 | -0.377 | 0.7062 |  |
| Circulatory disease | +0.1218 | 0.1592 | ±0.3185 | +0.765 | 0.4444 |  |
| Time 54-69, pooled (%) | +0.0048 | 0.0361 | ±0.0722 | +0.133 | 0.8944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2138**, R² = **0.0763**, Adj R² = **0.0715**, F-statistic = **15.97** (p = **1.80e-30**), Residual SE = **2.625** on **2126** df, AIC = **10206.0**, BIC = **10274.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1227** | 0.4728 | ±0.9457 | **+34.098** | **7.94e-255** | *** |
| **Education: graduate level (vs college)** | **+0.2507** | 0.1222 | ±0.2444 | **+2.052** | **0.0402** | * |
| **Education: high school or below (vs college)** | **-1.1232** | 0.2280 | ±0.4560 | **-4.927** | **8.36e-07** | *** |
| Site: UCSD (vs UAB) | +0.0966 | 0.1549 | ±0.3097 | +0.624 | 0.5328 |  |
| Site: UW (vs UAB) | +0.0333 | 0.1468 | ±0.2936 | +0.227 | 0.8205 |  |
| **Age (years)** | **-0.0515** | 0.0059 | ±0.0118 | **-8.756** | **2.03e-18** | *** |
| BMI (kg/m2) | -0.0102 | 0.0081 | ±0.0162 | -1.265 | 0.2057 |  |
| **Hypertension** | **-0.4205** | 0.1252 | ±0.2505 | **-3.358** | **7.85e-04** | *** |
| High cholesterol | +0.1828 | 0.1222 | ±0.2444 | +1.496 | 0.1347 |  |
| Kidney disease | -0.0779 | 0.2061 | ±0.4122 | -0.378 | 0.7055 |  |
| Circulatory disease | +0.1228 | 0.1593 | ±0.3185 | +0.771 | 0.4407 |  |
| Avg. daily time 54-69 (%) | -0.0151 | 0.0370 | ±0.0740 | -0.408 | 0.6830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2138**, R² = **0.0763**, Adj R² = **0.0715**, F-statistic = **15.97** (p = **1.80e-30**), Residual SE = **2.625** on **2126** df, AIC = **10206.0**, BIC = **10274.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0979** | 0.4742 | ±0.9484 | **+33.948** | **1.29e-252** | *** |
| **Education: graduate level (vs college)** | **+0.2549** | 0.1221 | ±0.2441 | **+2.088** | **0.0368** | * |
| **Education: high school or below (vs college)** | **-1.1174** | 0.2281 | ±0.4562 | **-4.898** | **9.66e-07** | *** |
| Site: UCSD (vs UAB) | +0.1057 | 0.1554 | ±0.3109 | +0.680 | 0.4963 |  |
| Site: UW (vs UAB) | +0.0426 | 0.1470 | ±0.2941 | +0.290 | 0.7720 |  |
| **Age (years)** | **-0.0514** | 0.0059 | ±0.0118 | **-8.747** | **2.20e-18** | *** |
| BMI (kg/m2) | -0.0103 | 0.0081 | ±0.0162 | -1.279 | 0.2011 |  |
| **Hypertension** | **-0.4179** | 0.1252 | ±0.2505 | **-3.336** | **8.49e-04** | *** |
| High cholesterol | +0.1865 | 0.1223 | ±0.2446 | +1.525 | 0.1272 |  |
| Kidney disease | -0.0776 | 0.2061 | ±0.4123 | -0.376 | 0.7066 |  |
| Circulatory disease | +0.1209 | 0.1592 | ±0.3185 | +0.759 | 0.4476 |  |
| Time < 70 (%) | +0.0123 | 0.0272 | ±0.0543 | +0.451 | 0.6517 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2138**, R² = **0.0763**, Adj R² = **0.0715**, F-statistic = **15.96** (p = **1.84e-30**), Residual SE = **2.625** on **2126** df, AIC = **10206.0**, BIC = **10274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1214** | 0.4730 | ±0.9461 | **+34.081** | **1.42e-254** | *** |
| **Education: graduate level (vs college)** | **+0.2512** | 0.1222 | ±0.2444 | **+2.055** | **0.0398** | * |
| **Education: high school or below (vs college)** | **-1.1230** | 0.2280 | ±0.4560 | **-4.926** | **8.41e-07** | *** |
| Site: UCSD (vs UAB) | +0.0967 | 0.1551 | ±0.3101 | +0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +0.0336 | 0.1470 | ±0.2940 | +0.228 | 0.8193 |  |
| **Age (years)** | **-0.0515** | 0.0059 | ±0.0118 | **-8.756** | **2.03e-18** | *** |
| BMI (kg/m2) | -0.0103 | 0.0081 | ±0.0162 | -1.268 | 0.2048 |  |
| **Hypertension** | **-0.4203** | 0.1252 | ±0.2505 | **-3.356** | **7.91e-04** | *** |
| High cholesterol | +0.1828 | 0.1222 | ±0.2444 | +1.495 | 0.1348 |  |
| Kidney disease | -0.0778 | 0.2061 | ±0.4122 | -0.377 | 0.7058 |  |
| Circulatory disease | +0.1229 | 0.1593 | ±0.3185 | +0.772 | 0.4404 |  |
| Avg. daily time < 70 (%) | -0.0104 | 0.0295 | ±0.0590 | -0.354 | 0.7235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2138**, R² = **0.0782**, Adj R² = **0.0734**, F-statistic = **16.39** (p = **2.30e-31**), Residual SE = **2.622** on **2126** df, AIC = **10201.6**, BIC = **10269.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0227** | 0.6815 | ±1.3630 | **+22.043** | **1.11e-107** | *** |
| Education: graduate level (vs college) | +0.2388 | 0.1221 | ±0.2443 | +1.955 | 0.0506 | . |
| **Education: high school or below (vs college)** | **-1.0837** | 0.2279 | ±0.4558 | **-4.756** | **1.98e-06** | *** |
| Site: UCSD (vs UAB) | +0.0810 | 0.1546 | ±0.3091 | +0.524 | 0.6005 |  |
| Site: UW (vs UAB) | +0.0169 | 0.1462 | ±0.2924 | +0.115 | 0.9082 |  |
| **Age (years)** | **-0.0517** | 0.0059 | ±0.0117 | **-8.802** | **1.34e-18** | *** |
| BMI (kg/m2) | -0.0096 | 0.0081 | ±0.0163 | -1.175 | 0.2401 |  |
| **Hypertension** | **-0.4064** | 0.1248 | ±0.2495 | **-3.258** | **0.0011** | ** |
| High cholesterol | +0.1879 | 0.1221 | ±0.2441 | +1.540 | 0.1237 |  |
| Kidney disease | -0.0492 | 0.2076 | ±0.4152 | -0.237 | 0.8127 |  |
| Circulatory disease | +0.1336 | 0.1590 | ±0.3181 | +0.840 | 0.4009 |  |
| **Time 54-250, pooled (%)** | **+0.0112** | 0.0051 | ±0.0102 | **+2.195** | **0.0281** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2138**, R² = **0.0781**, Adj R² = **0.0733**, F-statistic = **16.37** (p = **2.55e-31**), Residual SE = **2.622** on **2126** df, AIC = **10201.9**, BIC = **10269.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0299** | 0.6865 | ±1.3729 | **+21.895** | **2.90e-106** | *** |
| Education: graduate level (vs college) | +0.2392 | 0.1222 | ±0.2443 | +1.958 | 0.0502 | . |
| **Education: high school or below (vs college)** | **-1.0845** | 0.2278 | ±0.4557 | **-4.760** | **1.93e-06** | *** |
| Site: UCSD (vs UAB) | +0.0816 | 0.1546 | ±0.3091 | +0.528 | 0.5974 |  |
| Site: UW (vs UAB) | +0.0180 | 0.1462 | ±0.2923 | +0.123 | 0.9019 |  |
| **Age (years)** | **-0.0516** | 0.0059 | ±0.0117 | **-8.792** | **1.47e-18** | *** |
| BMI (kg/m2) | -0.0096 | 0.0081 | ±0.0163 | -1.175 | 0.2401 |  |
| **Hypertension** | **-0.4072** | 0.1248 | ±0.2495 | **-3.264** | **0.0011** | ** |
| High cholesterol | +0.1879 | 0.1221 | ±0.2441 | +1.539 | 0.1237 |  |
| Kidney disease | -0.0485 | 0.2077 | ±0.4153 | -0.234 | 0.8151 |  |
| Circulatory disease | +0.1339 | 0.1591 | ±0.3181 | +0.842 | 0.3998 |  |
| **Avg. daily time 54-250 (%)** | **+0.0110** | 0.0051 | ±0.0103 | **+2.151** | **0.0315** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2138**, R² = **0.0792**, Adj R² = **0.0744**, F-statistic = **16.61** (p = **7.95e-32**), Residual SE = **2.621** on **2126** df, AIC = **10199.4**, BIC = **10267.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0595** | 0.4725 | ±0.9451 | **+33.985** | **3.67e-253** | *** |
| **Education: graduate level (vs college)** | **+0.2459** | 0.1219 | ±0.2437 | **+2.018** | **0.0436** | * |
| **Education: high school or below (vs college)** | **-1.0806** | 0.2280 | ±0.4560 | **-4.740** | **2.14e-06** | *** |
| Site: UCSD (vs UAB) | +0.0789 | 0.1542 | ±0.3083 | +0.512 | 0.6088 |  |
| Site: UW (vs UAB) | +0.0301 | 0.1458 | ±0.2916 | +0.206 | 0.8365 |  |
| **Age (years)** | **-0.0501** | 0.0059 | ±0.0118 | **-8.526** | **1.51e-17** | *** |
| BMI (kg/m2) | -0.0085 | 0.0082 | ±0.0164 | -1.043 | 0.2970 |  |
| **Hypertension** | **-0.3969** | 0.1247 | ±0.2494 | **-3.183** | **0.0015** | ** |
| High cholesterol | +0.2029 | 0.1224 | ±0.2448 | +1.657 | 0.0974 | . |
| Kidney disease | -0.0196 | 0.2087 | ±0.4174 | -0.094 | 0.9251 |  |
| Circulatory disease | +0.1322 | 0.1589 | ±0.3178 | +0.832 | 0.4056 |  |
| **Time 181-250, pooled (%)** | **-0.0119** | 0.0046 | ±0.0092 | **-2.603** | **0.0093** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2138**, R² = **0.0791**, Adj R² = **0.0744**, F-statistic = **16.61** (p = **8.03e-32**), Residual SE = **2.621** on **2126** df, AIC = **10199.4**, BIC = **10267.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0609** | 0.4727 | ±0.9455 | **+33.974** | **5.45e-253** | *** |
| **Education: graduate level (vs college)** | **+0.2465** | 0.1219 | ±0.2437 | **+2.023** | **0.0431** | * |
| **Education: high school or below (vs college)** | **-1.0797** | 0.2281 | ±0.4561 | **-4.734** | **2.20e-06** | *** |
| Site: UCSD (vs UAB) | +0.0775 | 0.1542 | ±0.3083 | +0.503 | 0.6152 |  |
| Site: UW (vs UAB) | +0.0290 | 0.1458 | ±0.2916 | +0.199 | 0.8422 |  |
| **Age (years)** | **-0.0502** | 0.0059 | ±0.0118 | **-8.537** | **1.38e-17** | *** |
| BMI (kg/m2) | -0.0085 | 0.0082 | ±0.0164 | -1.039 | 0.2989 |  |
| **Hypertension** | **-0.3971** | 0.1247 | ±0.2494 | **-3.184** | **0.0015** | ** |
| High cholesterol | +0.2031 | 0.1224 | ±0.2448 | +1.659 | 0.0972 | . |
| Kidney disease | -0.0194 | 0.2085 | ±0.4171 | -0.093 | 0.9260 |  |
| Circulatory disease | +0.1317 | 0.1589 | ±0.3178 | +0.829 | 0.4071 |  |
| **Avg. daily time 181-250 (%)** | **-0.0117** | 0.0045 | ±0.0091 | **-2.589** | **0.0096** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2138**, R² = **0.0797**, Adj R² = **0.0750**, F-statistic = **16.74** (p = **4.28e-32**), Residual SE = **2.620** on **2126** df, AIC = **10198.1**, BIC = **10266.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0928** | 0.4721 | ±0.9442 | **+34.087** | **1.14e-254** | *** |
| Education: graduate level (vs college) | +0.2378 | 0.1220 | ±0.2439 | +1.949 | 0.0513 | . |
| **Education: high school or below (vs college)** | **-1.0650** | 0.2277 | ±0.4553 | **-4.678** | **2.90e-06** | *** |
| Site: UCSD (vs UAB) | +0.0724 | 0.1543 | ±0.3085 | +0.470 | 0.6387 |  |
| Site: UW (vs UAB) | +0.0181 | 0.1458 | ±0.2915 | +0.124 | 0.9014 |  |
| **Age (years)** | **-0.0507** | 0.0059 | ±0.0117 | **-8.642** | **5.51e-18** | *** |
| BMI (kg/m2) | -0.0085 | 0.0082 | ±0.0164 | -1.043 | 0.2971 |  |
| **Hypertension** | **-0.3942** | 0.1246 | ±0.2492 | **-3.164** | **0.0016** | ** |
| High cholesterol | +0.2003 | 0.1222 | ±0.2445 | +1.639 | 0.1013 |  |
| Kidney disease | -0.0165 | 0.2089 | ±0.4179 | -0.079 | 0.9372 |  |
| Circulatory disease | +0.1372 | 0.1588 | ±0.3176 | +0.864 | 0.3875 |  |
| **Time > 180 (%)** | **-0.0082** | 0.0029 | ±0.0057 | **-2.880** | **0.0040** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2138**, R² = **0.0796**, Adj R² = **0.0748**, F-statistic = **16.71** (p = **4.97e-32**), Residual SE = **2.620** on **2126** df, AIC = **10198.4**, BIC = **10266.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0908** | 0.4723 | ±0.9445 | **+34.072** | **1.95e-254** | *** |
| Education: graduate level (vs college) | +0.2387 | 0.1220 | ±0.2440 | +1.957 | 0.0504 | . |
| **Education: high school or below (vs college)** | **-1.0657** | 0.2277 | ±0.4555 | **-4.680** | **2.87e-06** | *** |
| Site: UCSD (vs UAB) | +0.0719 | 0.1543 | ±0.3086 | +0.466 | 0.6414 |  |
| Site: UW (vs UAB) | +0.0182 | 0.1458 | ±0.2916 | +0.125 | 0.9005 |  |
| **Age (years)** | **-0.0507** | 0.0059 | ±0.0117 | **-8.642** | **5.51e-18** | *** |
| BMI (kg/m2) | -0.0085 | 0.0082 | ±0.0164 | -1.042 | 0.2974 |  |
| **Hypertension** | **-0.3951** | 0.1246 | ±0.2492 | **-3.171** | **0.0015** | ** |
| High cholesterol | +0.2002 | 0.1223 | ±0.2445 | +1.637 | 0.1016 |  |
| Kidney disease | -0.0164 | 0.2089 | ±0.4178 | -0.079 | 0.9373 |  |
| Circulatory disease | +0.1371 | 0.1588 | ±0.3177 | +0.863 | 0.3880 |  |
| **Avg. daily time > 180 (%)** | **-0.0081** | 0.0029 | ±0.0057 | **-2.817** | **0.0049** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2138**, R² = **0.0792**, Adj R² = **0.0744**, F-statistic = **16.62** (p = **7.59e-32**), Residual SE = **2.621** on **2126** df, AIC = **10199.3**, BIC = **10267.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0915** | 0.4724 | ±0.9448 | **+34.064** | **2.52e-254** | *** |
| Education: graduate level (vs college) | +0.2340 | 0.1218 | ±0.2437 | +1.921 | 0.0547 | . |
| **Education: high school or below (vs college)** | **-1.0731** | 0.2277 | ±0.4554 | **-4.712** | **2.45e-06** | *** |
| Site: UCSD (vs UAB) | +0.0740 | 0.1546 | ±0.3092 | +0.478 | 0.6324 |  |
| Site: UW (vs UAB) | +0.0219 | 0.1460 | ±0.2920 | +0.150 | 0.8808 |  |
| **Age (years)** | **-0.0513** | 0.0059 | ±0.0117 | **-8.737** | **2.40e-18** | *** |
| BMI (kg/m2) | -0.0079 | 0.0082 | ±0.0165 | -0.960 | 0.3372 |  |
| **Hypertension** | **-0.4044** | 0.1246 | ±0.2491 | **-3.247** | **0.0012** | ** |
| High cholesterol | +0.1966 | 0.1222 | ±0.2445 | +1.608 | 0.1078 |  |
| Kidney disease | -0.0339 | 0.2079 | ±0.4157 | -0.163 | 0.8705 |  |
| Circulatory disease | +0.1342 | 0.1585 | ±0.3171 | +0.847 | 0.3972 |  |
| **Nocturnal time > 180 (%)** | **-0.0076** | 0.0029 | ±0.0057 | **-2.657** | **0.0079** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2138**, R² = **0.0786**, Adj R² = **0.0738**, F-statistic = **16.48** (p = **1.50e-31**), Residual SE = **2.622** on **2126** df, AIC = **10200.7**, BIC = **10268.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1366** | 0.4714 | ±0.9427 | **+34.234** | **7.54e-257** | *** |
| Education: graduate level (vs college) | +0.2373 | 0.1221 | ±0.2441 | +1.944 | 0.0519 | . |
| **Education: high school or below (vs college)** | **-1.0994** | 0.2281 | ±0.4562 | **-4.820** | **1.43e-06** | *** |
| Site: UCSD (vs UAB) | +0.0869 | 0.1538 | ±0.3076 | +0.565 | 0.5719 |  |
| Site: UW (vs UAB) | +0.0324 | 0.1457 | ±0.2913 | +0.222 | 0.8241 |  |
| **Age (years)** | **-0.0503** | 0.0059 | ±0.0118 | **-8.547** | **1.26e-17** | *** |
| BMI (kg/m2) | -0.0105 | 0.0081 | ±0.0162 | -1.294 | 0.1958 |  |
| **Hypertension** | **-0.3927** | 0.1248 | ±0.2496 | **-3.147** | **0.0016** | ** |
| High cholesterol | +0.2009 | 0.1223 | ±0.2445 | +1.643 | 0.1004 |  |
| Kidney disease | -0.0346 | 0.2097 | ±0.4194 | -0.165 | 0.8689 |  |
| Circulatory disease | +0.1230 | 0.1592 | ±0.3184 | +0.772 | 0.4398 |  |
| **Any reading > 250 during wear (0/1)** | **-0.2804** | 0.1247 | ±0.2495 | **-2.248** | **0.0246** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2138**, R² = **0.0783**, Adj R² = **0.0735**, F-statistic = **16.41** (p = **2.10e-31**), Residual SE = **2.622** on **2126** df, AIC = **10201.5**, BIC = **10269.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1360** | 0.4717 | ±0.9435 | **+34.205** | **2.06e-256** | *** |
| Education: graduate level (vs college) | +0.2387 | 0.1221 | ±0.2442 | +1.955 | 0.0506 | . |
| **Education: high school or below (vs college)** | **-1.0820** | 0.2279 | ±0.4558 | **-4.748** | **2.06e-06** | *** |
| Site: UCSD (vs UAB) | +0.0822 | 0.1545 | ±0.3090 | +0.532 | 0.5945 |  |
| Site: UW (vs UAB) | +0.0178 | 0.1461 | ±0.2923 | +0.122 | 0.9031 |  |
| **Age (years)** | **-0.0517** | 0.0059 | ±0.0117 | **-8.802** | **1.35e-18** | *** |
| BMI (kg/m2) | -0.0095 | 0.0081 | ±0.0163 | -1.173 | 0.2410 |  |
| **Hypertension** | **-0.4059** | 0.1248 | ±0.2495 | **-3.254** | **0.0011** | ** |
| High cholesterol | +0.1887 | 0.1221 | ±0.2441 | +1.546 | 0.1222 |  |
| Kidney disease | -0.0486 | 0.2076 | ±0.4152 | -0.234 | 0.8151 |  |
| Circulatory disease | +0.1334 | 0.1590 | ±0.3180 | +0.839 | 0.4015 |  |
| **Time > 250 (%)** | **-0.0114** | 0.0051 | ±0.0102 | **-2.241** | **0.0250** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,138)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2138**, R² = **0.0781**, Adj R² = **0.0733**, F-statistic = **16.37** (p = **2.55e-31**), Residual SE = **2.622** on **2126** df, AIC = **10201.9**, BIC = **10269.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1312** | 0.4717 | ±0.9434 | **+34.199** | **2.53e-256** | *** |
| **Education: graduate level (vs college)** | **+0.2395** | 0.1221 | ±0.2443 | **+1.961** | **0.0499** | * |
| **Education: high school or below (vs college)** | **-1.0839** | 0.2279 | ±0.4558 | **-4.756** | **1.97e-06** | *** |
| Site: UCSD (vs UAB) | +0.0828 | 0.1545 | ±0.3090 | +0.536 | 0.5921 |  |
| Site: UW (vs UAB) | +0.0192 | 0.1461 | ±0.2922 | +0.131 | 0.8956 |  |
| **Age (years)** | **-0.0516** | 0.0059 | ±0.0117 | **-8.792** | **1.47e-18** | *** |
| BMI (kg/m2) | -0.0096 | 0.0081 | ±0.0163 | -1.175 | 0.2401 |  |
| **Hypertension** | **-0.4070** | 0.1248 | ±0.2495 | **-3.262** | **0.0011** | ** |
| High cholesterol | +0.1884 | 0.1221 | ±0.2442 | +1.543 | 0.1228 |  |
| Kidney disease | -0.0486 | 0.2077 | ±0.4153 | -0.234 | 0.8150 |  |
| Circulatory disease | +0.1336 | 0.1591 | ±0.3181 | +0.840 | 0.4010 |  |
| **Avg. daily time > 250 (%)** | **-0.0110** | 0.0051 | ±0.0103 | **-2.152** | **0.0314** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 93 single-predictor tests; 70 with raw p < 0.05 (about 5 expected by chance); FDR rule applied to 93 tests (samples with n >= 500), of which **61** are significant at BH q < 0.05 in the all-tests family and 66 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 2,138): best single predictor out of sample is **Mean glucose** (CV R² 0.106 vs 0.092 for covariates alone, gain +0.015; -0.411 per SD, p = 5.3e-08, q = 6.4e-07). FDR-robust associations (24): Mean glucose (lower outcome, -0.411 per SD, q = 6.4e-07); GMI (lower outcome, -0.411 per SD, q = 6.4e-07); SD (pooled) (lower outcome, -0.399 per SD, q = 6.5e-07); SD (daily avg) (lower outcome, -0.39 per SD, q = 1.2e-06); Nocturnal mean (lower outcome, -0.385 per SD, q = 5.2e-06); Daily range (lower outcome, -0.352 per SD, q = 1.4e-05); ....
- **Cognitive impairment (MoCA < 26)** (n = 2,138): best single predictor out of sample is **GMI** (CV AUC 0.669 vs 0.660 for covariates alone, gain +0.009; OR 1.25 per SD, p = 6.1e-06, q = 5.1e-05). FDR-robust associations (23): Mean glucose (higher outcome, OR 1.25 per SD, q = 5.1e-05); GMI (higher outcome, OR 1.25 per SD, q = 5.1e-05); SD (pooled) (higher outcome, OR 1.24 per SD, q = 1.1e-04); SD (daily avg) (higher outcome, OR 1.23 per SD, q = 1.4e-04); Nocturnal mean (higher outcome, OR 1.22 per SD, q = 2.5e-04); TIR 70-180 (pooled) (lower outcome, OR 0.83 per SD, q = 4.2e-04); ....
- **MoCA memory index score (0-15)** (n = 2,138): best single predictor out of sample is **Nocturnal mean** (CV R² 0.068 vs 0.063 for covariates alone, gain +0.005; -0.214 per SD, p = 2.1e-04, q = 0.001). FDR-robust associations (14): Nocturnal mean (lower outcome, -0.214 per SD, q = 0.001); Mean glucose (lower outcome, -0.199 per SD, q = 0.003); GMI (lower outcome, -0.199 per SD, q = 0.003); SD (daily avg) (lower outcome, -0.178 per SD, q = 0.014); %>180 (pooled) (lower outcome, -0.167 per SD, q = 0.017); TIR 70-180 (pooled) (higher outcome, +0.167 per SD, q = 0.017); ....

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA total score (0-30) (+0.015, via Mean glucose); Cognitive impairment (MoCA < 26) (+0.009, via GMI); MoCA memory index score (0-15) (+0.005, via Nocturnal mean). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (18 FDR-significant / 20 raw-significant of 24); CGM level (9 FDR-significant / 9 raw-significant of 9); Band > 180 (9 FDR-significant / 9 raw-significant of 9).
Level metrics: 9 FDR-significant (9 raw); variability metrics: 18 FDR-significant (20 raw); HbA1c alone: 3 FDR-significant (3 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (Mean glucose, ΔAIC -11.3); Cognitive impairment (Mean glucose, ΔAIC -5.6); MoCA memory index score (Nocturnal mean, ΔAIC -5.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
