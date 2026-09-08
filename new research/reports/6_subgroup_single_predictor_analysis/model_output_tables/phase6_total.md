# Phase 6 model output tables - All (analysis base) - Total analysis base

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 2,135; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1032**, F-statistic = **25.55** (p = **3.02e-46**), Residual SE = **4.715** on **2124** df, AIC = **12691.3**, BIC = **12753.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5053** | 0.8327 | ±1.6653 | **+10.215** | **1.71e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8470** | 0.2143 | ±0.4285 | **-3.953** | **7.72e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2921** | 0.4056 | ±0.8112 | **+3.186** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.0775 | 0.2740 | ±0.5480 | +0.283 | 0.7772 |  |
| Site: UW (vs UAB) | +0.0731 | 0.2537 | ±0.5073 | +0.288 | 0.7734 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.909** | **3.79e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.737** | **2.17e-06** | *** |
| Hypertension | +0.2910 | 0.2264 | ±0.4527 | +1.285 | 0.1986 |  |
| **High cholesterol** | **+0.6623** | 0.2123 | ±0.4246 | **+3.120** | **0.0018** | ** |
| **Kidney disease** | **+0.9434** | 0.3768 | ±0.7536 | **+2.504** | **0.0123** | * |
| **Circulatory disease** | **+1.1324** | 0.3188 | ±0.6375 | **+3.553** | **3.81e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2135**, R² = **0.1083**, Adj R² = **0.1037**, F-statistic = **23.44** (p = **5.34e-46**), Residual SE = **4.713** on **2123** df, AIC = **12691.1**, BIC = **12759.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7300** | 1.0312 | ±2.0623 | **+7.496** | **6.56e-14** | *** |
| **Education: graduate level (vs college)** | **-0.8280** | 0.2142 | ±0.4283 | **-3.866** | **1.11e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2328** | 0.4045 | ±0.8091 | **+3.047** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.0916 | 0.2743 | ±0.5486 | +0.334 | 0.7383 |  |
| Site: UW (vs UAB) | +0.0923 | 0.2547 | ±0.5095 | +0.363 | 0.7170 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0191 | **-9.943** | **2.70e-23** | *** |
| **BMI (kg/m2)** | **+0.0750** | 0.0165 | ±0.0331 | **+4.534** | **5.78e-06** | *** |
| Hypertension | +0.2586 | 0.2275 | ±0.4550 | +1.137 | 0.2557 |  |
| **High cholesterol** | **+0.6341** | 0.2123 | ±0.4247 | **+2.986** | **0.0028** | ** |
| **Kidney disease** | **+0.9170** | 0.3780 | ±0.7560 | **+2.426** | **0.0153** | * |
| **Circulatory disease** | **+1.1185** | 0.3179 | ±0.6359 | **+3.518** | **4.35e-04** | *** |
| HbA1c (%) | +0.1526 | 0.1196 | ±0.2392 | +1.276 | 0.2020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.26** (p = **1.24e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.8**, BIC = **12760.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2669** | 0.9142 | ±1.8283 | **+9.043** | **1.52e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8420** | 0.2144 | ±0.4287 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2668** | 0.4071 | ±0.8143 | **+3.112** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0869 | 0.2746 | ±0.5492 | +0.316 | 0.7516 |  |
| Site: UW (vs UAB) | +0.0784 | 0.2541 | ±0.5082 | +0.308 | 0.7577 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0191 | **-9.902** | **4.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0329 | **+4.667** | **3.06e-06** | *** |
| Hypertension | +0.2763 | 0.2269 | ±0.4538 | +1.218 | 0.2234 |  |
| **High cholesterol** | **+0.6531** | 0.2124 | ±0.4248 | **+3.075** | **0.0021** | ** |
| **Kidney disease** | **+0.9192** | 0.3805 | ±0.7611 | **+2.416** | **0.0157** | * |
| **Circulatory disease** | **+1.1255** | 0.3185 | ±0.6370 | **+3.533** | **4.10e-04** | *** |
| Mean glucose (mg/dL) | +0.0022 | 0.0035 | ±0.0071 | +0.623 | 0.5335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.26** (p = **1.24e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.8**, BIC = **12760.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9625** | 1.2006 | ±2.4013 | **+6.632** | **3.31e-11** | *** |
| **Education: graduate level (vs college)** | **-0.8420** | 0.2144 | ±0.4287 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2668** | 0.4071 | ±0.8143 | **+3.112** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0869 | 0.2746 | ±0.5492 | +0.316 | 0.7516 |  |
| Site: UW (vs UAB) | +0.0784 | 0.2541 | ±0.5082 | +0.308 | 0.7577 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0191 | **-9.902** | **4.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0329 | **+4.667** | **3.06e-06** | *** |
| Hypertension | +0.2763 | 0.2269 | ±0.4538 | +1.218 | 0.2234 |  |
| **High cholesterol** | **+0.6531** | 0.2124 | ±0.4248 | **+3.075** | **0.0021** | ** |
| **Kidney disease** | **+0.9192** | 0.3805 | ±0.7611 | **+2.416** | **0.0157** | * |
| **Circulatory disease** | **+1.1255** | 0.3185 | ±0.6370 | **+3.533** | **4.10e-04** | *** |
| GMI (%) | +0.0919 | 0.1476 | ±0.2953 | +0.623 | 0.5335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.39e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.7**, BIC = **12759.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0806** | 0.9171 | ±1.8341 | **+8.811** | **1.24e-18** | *** |
| **Education: graduate level (vs college)** | **-0.8369** | 0.2144 | ±0.4288 | **-3.903** | **9.48e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2491** | 0.4068 | ±0.8137 | **+3.070** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.0897 | 0.2742 | ±0.5483 | +0.327 | 0.7434 |  |
| Site: UW (vs UAB) | +0.0783 | 0.2540 | ±0.5080 | +0.308 | 0.7579 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.898** | **4.26e-23** | *** |
| **BMI (kg/m2)** | **+0.0753** | 0.0165 | ±0.0331 | **+4.556** | **5.22e-06** | *** |
| Hypertension | +0.2704 | 0.2264 | ±0.4528 | +1.194 | 0.2323 |  |
| **High cholesterol** | **+0.6450** | 0.2124 | ±0.4247 | **+3.037** | **0.0024** | ** |
| **Kidney disease** | **+0.9138** | 0.3800 | ±0.7600 | **+2.405** | **0.0162** | * |
| **Circulatory disease** | **+1.1225** | 0.3185 | ±0.6370 | **+3.524** | **4.25e-04** | *** |
| Nocturnal mean 00-06h (mg/dL) | +0.0039 | 0.0036 | ±0.0071 | +1.104 | 0.2695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.40** (p = **6.58e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.5**, BIC = **12759.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2980** | 0.8500 | ±1.7000 | **+9.762** | **1.64e-22** | *** |
| **Education: graduate level (vs college)** | **-0.8307** | 0.2145 | ±0.4289 | **-3.873** | **1.07e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2492** | 0.4063 | ±0.8125 | **+3.075** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1014 | 0.2747 | ±0.5494 | +0.369 | 0.7121 |  |
| Site: UW (vs UAB) | +0.0940 | 0.2542 | ±0.5084 | +0.370 | 0.7114 |  |
| **Age (years)** | **-0.0951** | 0.0095 | ±0.0191 | **-9.968** | **2.10e-23** | *** |
| **BMI (kg/m2)** | **+0.0766** | 0.0165 | ±0.0329 | **+4.654** | **3.25e-06** | *** |
| Hypertension | +0.2585 | 0.2275 | ±0.4550 | +1.136 | 0.2559 |  |
| **High cholesterol** | **+0.6494** | 0.2121 | ±0.4243 | **+3.062** | **0.0022** | ** |
| **Kidney disease** | **+0.8652** | 0.3830 | ±0.7660 | **+2.259** | **0.0239** | * |
| **Circulatory disease** | **+1.1181** | 0.3188 | ±0.6376 | **+3.507** | **4.53e-04** | *** |
| Glucose SD, pooled (mg/dL) | +0.0121 | 0.0095 | ±0.0191 | +1.265 | 0.2059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1030**, F-statistic = **23.29** (p = **1.12e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3750** | 0.8483 | ±1.6966 | **+9.873** | **5.47e-23** | *** |
| **Education: graduate level (vs college)** | **-0.8379** | 0.2143 | ±0.4286 | **-3.910** | **9.24e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2646** | 0.4068 | ±0.8135 | **+3.109** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0915 | 0.2748 | ±0.5496 | +0.333 | 0.7392 |  |
| Site: UW (vs UAB) | +0.0846 | 0.2540 | ±0.5081 | +0.333 | 0.7390 |  |
| **Age (years)** | **-0.0948** | 0.0096 | ±0.0191 | **-9.916** | **3.53e-23** | *** |
| **BMI (kg/m2)** | **+0.0771** | 0.0164 | ±0.0329 | **+4.694** | **2.68e-06** | *** |
| Hypertension | +0.2711 | 0.2277 | ±0.4554 | +1.191 | 0.2338 |  |
| **High cholesterol** | **+0.6541** | 0.2123 | ±0.4246 | **+3.081** | **0.0021** | ** |
| **Kidney disease** | **+0.8937** | 0.3833 | ±0.7665 | **+2.332** | **0.0197** | * |
| **Circulatory disease** | **+1.1248** | 0.3189 | ±0.6378 | **+3.527** | **4.20e-04** | *** |
| Avg. daily SD (mg/dL) | +0.0085 | 0.0107 | ±0.0214 | +0.794 | 0.4273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1031**, F-statistic = **23.29** (p = **1.10e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2281** | 0.8967 | ±1.7934 | **+9.176** | **4.48e-20** | *** |
| **Education: graduate level (vs college)** | **-0.8368** | 0.2145 | ±0.4290 | **-3.901** | **9.57e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2769** | 0.4059 | ±0.8117 | **+3.146** | **0.0017** | ** |
| Site: UCSD (vs UAB) | +0.0928 | 0.2747 | ±0.5494 | +0.338 | 0.7354 |  |
| Site: UW (vs UAB) | +0.0878 | 0.2538 | ±0.5075 | +0.346 | 0.7294 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0190 | **-9.962** | **2.24e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.721** | **2.35e-06** | *** |
| Hypertension | +0.2732 | 0.2273 | ±0.4545 | +1.202 | 0.2293 |  |
| **High cholesterol** | **+0.6603** | 0.2123 | ±0.4245 | **+3.111** | **0.0019** | ** |
| **Kidney disease** | **+0.8958** | 0.3795 | ±0.7590 | **+2.361** | **0.0182** | * |
| **Circulatory disease** | **+1.1257** | 0.3193 | ±0.6385 | **+3.526** | **4.22e-04** | *** |
| CV (%) | +0.0172 | 0.0197 | ±0.0395 | +0.872 | 0.3832 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1031**, F-statistic = **23.31** (p = **1.02e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.4**, BIC = **12760.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.9759** | 0.9561 | ±1.9121 | **+9.388** | **6.09e-21** | *** |
| **Education: graduate level (vs college)** | **-0.8358** | 0.2147 | ±0.4293 | **-3.894** | **9.88e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2740** | 0.4057 | ±0.8114 | **+3.140** | **0.0017** | ** |
| Site: UCSD (vs UAB) | +0.0919 | 0.2746 | ±0.5491 | +0.335 | 0.7377 |  |
| Site: UW (vs UAB) | +0.0842 | 0.2536 | ±0.5072 | +0.332 | 0.7398 |  |
| **Age (years)** | **-0.0949** | 0.0095 | ±0.0191 | **-9.961** | **2.26e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.724** | **2.31e-06** | *** |
| Hypertension | +0.2708 | 0.2273 | ±0.4547 | +1.191 | 0.2336 |  |
| **High cholesterol** | **+0.6590** | 0.2123 | ±0.4246 | **+3.104** | **0.0019** | ** |
| **Kidney disease** | **+0.9027** | 0.3780 | ±0.7559 | **+2.388** | **0.0169** | * |
| **Circulatory disease** | **+1.1247** | 0.3191 | ±0.6381 | **+3.525** | **4.24e-04** | *** |
| Mean / SD ratio | -0.0737 | 0.0750 | ±0.1501 | -0.982 | 0.3263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1028**, F-statistic = **23.22** (p = **1.54e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.3**, BIC = **12761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6053** | 0.9642 | ±1.9283 | **+8.925** | **4.45e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8450** | 0.2144 | ±0.4288 | **-3.941** | **8.12e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2882** | 0.4060 | ±0.8119 | **+3.173** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0796 | 0.2743 | ±0.5487 | +0.290 | 0.7716 |  |
| Site: UW (vs UAB) | +0.0749 | 0.2535 | ±0.5071 | +0.295 | 0.7677 |  |
| **Age (years)** | **-0.0942** | 0.0095 | ±0.0191 | **-9.869** | **5.67e-23** | *** |
| **BMI (kg/m2)** | **+0.0776** | 0.0164 | ±0.0328 | **+4.733** | **2.21e-06** | *** |
| Hypertension | +0.2872 | 0.2276 | ±0.4553 | +1.261 | 0.2071 |  |
| **High cholesterol** | **+0.6618** | 0.2124 | ±0.4248 | **+3.116** | **0.0018** | ** |
| **Kidney disease** | **+0.9351** | 0.3782 | ±0.7565 | **+2.472** | **0.0134** | * |
| **Circulatory disease** | **+1.1318** | 0.3190 | ±0.6380 | **+3.548** | **3.89e-04** | *** |
| Avg. daily mean/SD | -0.0133 | 0.0641 | ±0.1281 | -0.207 | 0.8359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2135**, R² = **0.1096**, Adj R² = **0.1049**, F-statistic = **23.75** (p = **1.27e-46**), Residual SE = **4.710** on **2123** df, AIC = **12688.1**, BIC = **12756.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4335** | 0.9517 | ±1.9035 | **+7.810** | **5.70e-15** | *** |
| **Education: graduate level (vs college)** | **-0.8195** | 0.2144 | ±0.4288 | **-3.822** | **1.32e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2457** | 0.4046 | ±0.8092 | **+3.079** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1169 | 0.2740 | ±0.5480 | +0.427 | 0.6696 |  |
| Site: UW (vs UAB) | +0.1333 | 0.2551 | ±0.5102 | +0.523 | 0.6013 |  |
| **Age (years)** | **-0.0936** | 0.0095 | ±0.0190 | **-9.876** | **5.27e-23** | *** |
| **BMI (kg/m2)** | **+0.0765** | 0.0164 | ±0.0329 | **+4.653** | **3.27e-06** | *** |
| Hypertension | +0.2777 | 0.2265 | ±0.4530 | +1.226 | 0.2201 |  |
| **High cholesterol** | **+0.6652** | 0.2121 | ±0.4242 | **+3.136** | **0.0017** | ** |
| **Kidney disease** | **+0.8771** | 0.3781 | ±0.7562 | **+2.320** | **0.0204** | * |
| **Circulatory disease** | **+1.1234** | 0.3193 | ±0.6385 | **+3.519** | **4.34e-04** | *** |
| **MAG (mg/dL/h)** | **+0.0264** | 0.0122 | ±0.0245 | **+2.155** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.27** (p = **1.19e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.7**, BIC = **12760.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3150** | 0.8713 | ±1.7426 | **+9.543** | **1.39e-21** | *** |
| **Education: graduate level (vs college)** | **-0.8390** | 0.2143 | ±0.4286 | **-3.915** | **9.06e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2680** | 0.4066 | ±0.8133 | **+3.118** | **0.0018** | ** |
| Site: UCSD (vs UAB) | +0.0912 | 0.2748 | ±0.5496 | +0.332 | 0.7399 |  |
| Site: UW (vs UAB) | +0.0841 | 0.2539 | ±0.5078 | +0.331 | 0.7405 |  |
| **Age (years)** | **-0.0946** | 0.0095 | ±0.0191 | **-9.917** | **3.51e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.723** | **2.33e-06** | *** |
| Hypertension | +0.2759 | 0.2274 | ±0.4547 | +1.214 | 0.2249 |  |
| **High cholesterol** | **+0.6557** | 0.2124 | ±0.4248 | **+3.087** | **0.0020** | ** |
| **Kidney disease** | **+0.9010** | 0.3818 | ±0.7637 | **+2.360** | **0.0183** | * |
| **Circulatory disease** | **+1.1247** | 0.3190 | ±0.6380 | **+3.526** | **4.22e-04** | *** |
| Avg. daily range (mg/dL) | +0.0021 | 0.0028 | ±0.0056 | +0.739 | 0.4599 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2135**, R² = **0.1122**, Adj R² = **0.1076**, F-statistic = **24.39** (p = **6.18e-48**), Residual SE = **4.703** on **2123** df, AIC = **12681.8**, BIC = **12749.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1921** | 0.8360 | ±1.6720 | **+9.799** | **1.14e-22** | *** |
| **Education: graduate level (vs college)** | **-0.7982** | 0.2144 | ±0.4288 | **-3.723** | **1.97e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2217** | 0.4038 | ±0.8077 | **+3.025** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +0.1284 | 0.2732 | ±0.5465 | +0.470 | 0.6384 |  |
| Site: UW (vs UAB) | +0.1226 | 0.2537 | ±0.5073 | +0.484 | 0.6287 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0190 | **-9.929** | **3.13e-23** | *** |
| **BMI (kg/m2)** | **+0.0730** | 0.0165 | ±0.0329 | **+4.434** | **9.26e-06** | *** |
| Hypertension | +0.2341 | 0.2264 | ±0.4529 | +1.034 | 0.3012 |  |
| **High cholesterol** | **+0.6295** | 0.2113 | ±0.4226 | **+2.979** | **0.0029** | ** |
| **Kidney disease** | **+0.8212** | 0.3791 | ±0.7582 | **+2.166** | **0.0303** | * |
| **Circulatory disease** | **+1.0728** | 0.3171 | ±0.6343 | **+3.383** | **7.17e-04** | *** |
| **SD of daily means (mg/dL)** | **+0.0564** | 0.0175 | ±0.0349 | **+3.227** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.40** (p = **6.52e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.5**, BIC = **12759.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2275** | 1.0242 | ±2.0484 | **+9.009** | **2.07e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8327** | 0.2145 | ±0.4290 | **-3.882** | **1.04e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2461** | 0.4068 | ±0.8137 | **+3.063** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1047 | 0.2751 | ±0.5502 | +0.381 | 0.7036 |  |
| Site: UW (vs UAB) | +0.0931 | 0.2547 | ±0.5094 | +0.365 | 0.7148 |  |
| **Age (years)** | **-0.0947** | 0.0095 | ±0.0190 | **-9.946** | **2.62e-23** | *** |
| **BMI (kg/m2)** | **+0.0761** | 0.0165 | ±0.0329 | **+4.621** | **3.83e-06** | *** |
| Hypertension | +0.2705 | 0.2265 | ±0.4531 | +1.194 | 0.2324 |  |
| **High cholesterol** | **+0.6494** | 0.2122 | ±0.4245 | **+3.060** | **0.0022** | ** |
| **Kidney disease** | **+0.8904** | 0.3821 | ±0.7642 | **+2.330** | **0.0198** | * |
| **Circulatory disease** | **+1.1183** | 0.3185 | ±0.6370 | **+3.511** | **4.46e-04** | *** |
| Time in range 70-180, pooled (%) | -0.0071 | 0.0059 | ±0.0119 | -1.199 | 0.2305 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.39** (p = **6.93e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.6**, BIC = **12759.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2039** | 1.0265 | ±2.0530 | **+8.966** | **3.07e-19** | *** |
| **Education: graduate level (vs college)** | **-0.8336** | 0.2145 | ±0.4290 | **-3.887** | **1.02e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2472** | 0.4069 | ±0.8138 | **+3.065** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1040 | 0.2751 | ±0.5501 | +0.378 | 0.7053 |  |
| Site: UW (vs UAB) | +0.0924 | 0.2547 | ±0.5093 | +0.363 | 0.7167 |  |
| **Age (years)** | **-0.0947** | 0.0095 | ±0.0190 | **-9.944** | **2.67e-23** | *** |
| **BMI (kg/m2)** | **+0.0761** | 0.0165 | ±0.0330 | **+4.621** | **3.82e-06** | *** |
| Hypertension | +0.2717 | 0.2265 | ±0.4530 | +1.199 | 0.2304 |  |
| **High cholesterol** | **+0.6495** | 0.2123 | ±0.4245 | **+3.060** | **0.0022** | ** |
| **Kidney disease** | **+0.8913** | 0.3820 | ±0.7640 | **+2.333** | **0.0196** | * |
| **Circulatory disease** | **+1.1188** | 0.3185 | ±0.6371 | **+3.512** | **4.44e-04** | *** |
| Avg. daily time in range 70-180 (%) | -0.0069 | 0.0059 | ±0.0119 | -1.156 | 0.2476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2135**, R² = **0.1075**, Adj R² = **0.1029**, F-statistic = **23.26** (p = **1.29e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.9**, BIC = **12760.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4340** | 0.8443 | ±1.6887 | **+9.989** | **1.70e-23** | *** |
| **Education: graduate level (vs college)** | **-0.8434** | 0.2146 | ±0.4292 | **-3.929** | **8.51e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3056** | 0.4057 | ±0.8114 | **+3.218** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0946 | 0.2747 | ±0.5493 | +0.344 | 0.7307 |  |
| Site: UW (vs UAB) | +0.0825 | 0.2538 | ±0.5076 | +0.325 | 0.7450 |  |
| **Age (years)** | **-0.0936** | 0.0095 | ±0.0191 | **-9.806** | **1.06e-22** | *** |
| **BMI (kg/m2)** | **+0.0773** | 0.0164 | ±0.0327 | **+4.723** | **2.32e-06** | *** |
| Hypertension | +0.2897 | 0.2266 | ±0.4532 | +1.278 | 0.2012 |  |
| **High cholesterol** | **+0.6712** | 0.2123 | ±0.4247 | **+3.161** | **0.0016** | ** |
| **Kidney disease** | **+0.9479** | 0.3768 | ±0.7537 | **+2.515** | **0.0119** | * |
| **Circulatory disease** | **+1.1218** | 0.3205 | ±0.6411 | **+3.500** | **4.66e-04** | *** |
| Any reading < 54 during wear (0/1) | +0.1443 | 0.2281 | ±0.4562 | +0.632 | 0.5271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2135**, R² = **0.1075**, Adj R² = **0.1029**, F-statistic = **23.24** (p = **1.38e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.1**, BIC = **12761.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5394** | 0.8377 | ±1.6754 | **+10.194** | **2.11e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8491** | 0.2144 | ±0.4288 | **-3.960** | **7.50e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2838** | 0.4063 | ±0.8126 | **+3.160** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.0623 | 0.2754 | ±0.5508 | +0.226 | 0.8210 |  |
| Site: UW (vs UAB) | +0.0608 | 0.2547 | ±0.5094 | +0.239 | 0.8113 |  |
| **Age (years)** | **-0.0941** | 0.0095 | ±0.0190 | **-9.917** | **3.52e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.736** | **2.18e-06** | *** |
| Hypertension | +0.2888 | 0.2264 | ±0.4529 | +1.276 | 0.2021 |  |
| **High cholesterol** | **+0.6560** | 0.2125 | ±0.4251 | **+3.087** | **0.0020** | ** |
| **Kidney disease** | **+0.9428** | 0.3767 | ±0.7534 | **+2.503** | **0.0123** | * |
| **Circulatory disease** | **+1.1361** | 0.3191 | ±0.6383 | **+3.560** | **3.71e-04** | *** |
| Time < 54 (%) | -0.1034 | 0.1729 | ±0.3459 | -0.598 | 0.5500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1027**, F-statistic = **23.22** (p = **1.57e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.3**, BIC = **12761.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5095** | 0.8355 | ±1.6710 | **+10.185** | **2.32e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8476** | 0.2145 | ±0.4290 | **-3.952** | **7.75e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2907** | 0.4064 | ±0.8127 | **+3.176** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0751 | 0.2747 | ±0.5495 | +0.273 | 0.7847 |  |
| Site: UW (vs UAB) | +0.0706 | 0.2545 | ±0.5089 | +0.278 | 0.7814 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.907** | **3.90e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.736** | **2.18e-06** | *** |
| Hypertension | +0.2905 | 0.2266 | ±0.4532 | +1.282 | 0.1999 |  |
| **High cholesterol** | **+0.6613** | 0.2124 | ±0.4247 | **+3.114** | **0.0018** | ** |
| **Kidney disease** | **+0.9435** | 0.3769 | ±0.7537 | **+2.504** | **0.0123** | * |
| **Circulatory disease** | **+1.1332** | 0.3194 | ±0.6387 | **+3.548** | **3.88e-04** | *** |
| Avg. daily time < 54 (%) | -0.0234 | 0.2390 | ±0.4780 | -0.098 | 0.9219 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.27** (p = **1.21e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.8**, BIC = **12760.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4591** | 0.8357 | ±1.6714 | **+10.122** | **4.40e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8398** | 0.2146 | ±0.4292 | **-3.914** | **9.09e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3017** | 0.4055 | ±0.8111 | **+3.210** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0930 | 0.2739 | ±0.5477 | +0.340 | 0.7341 |  |
| Site: UW (vs UAB) | +0.0883 | 0.2534 | ±0.5068 | +0.348 | 0.7276 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.893** | **4.45e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.723** | **2.32e-06** | *** |
| Hypertension | +0.2956 | 0.2263 | ±0.4527 | +1.306 | 0.1916 |  |
| **High cholesterol** | **+0.6686** | 0.2124 | ±0.4248 | **+3.147** | **0.0016** | ** |
| **Kidney disease** | **+0.9435** | 0.3768 | ±0.7535 | **+2.504** | **0.0123** | * |
| **Circulatory disease** | **+1.1295** | 0.3194 | ±0.6388 | **+3.536** | **4.06e-04** | *** |
| Time 54-69, pooled (%) | +0.0530 | 0.0717 | ±0.1433 | +0.740 | 0.4596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2135**, R² = **0.1078**, Adj R² = **0.1031**, F-statistic = **23.31** (p = **1.01e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.4**, BIC = **12760.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4588** | 0.8343 | ±1.6686 | **+10.139** | **3.72e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8368** | 0.2146 | ±0.4291 | **-3.900** | **9.63e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3041** | 0.4055 | ±0.8110 | **+3.216** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0944 | 0.2737 | ±0.5475 | +0.345 | 0.7303 |  |
| Site: UW (vs UAB) | +0.0929 | 0.2534 | ±0.5068 | +0.367 | 0.7139 |  |
| **Age (years)** | **-0.0941** | 0.0095 | ±0.0190 | **-9.909** | **3.80e-23** | *** |
| **BMI (kg/m2)** | **+0.0774** | 0.0164 | ±0.0328 | **+4.720** | **2.36e-06** | *** |
| Hypertension | +0.2970 | 0.2264 | ±0.4527 | +1.312 | 0.1895 |  |
| **High cholesterol** | **+0.6695** | 0.2123 | ±0.4246 | **+3.154** | **0.0016** | ** |
| **Kidney disease** | **+0.9441** | 0.3766 | ±0.7531 | **+2.507** | **0.0122** | * |
| **Circulatory disease** | **+1.1295** | 0.3194 | ±0.6387 | **+3.537** | **4.05e-04** | *** |
| Avg. daily time 54-69 (%) | +0.0680 | 0.0709 | ±0.1418 | +0.959 | 0.3374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2135**, R² = **0.1075**, Adj R² = **0.1028**, F-statistic = **23.23** (p = **1.43e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.1**, BIC = **12761.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4742** | 0.8372 | ±1.6743 | **+10.123** | **4.39e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8430** | 0.2146 | ±0.4292 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2989** | 0.4058 | ±0.8115 | **+3.201** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.0889 | 0.2743 | ±0.5487 | +0.324 | 0.7458 |  |
| Site: UW (vs UAB) | +0.0836 | 0.2538 | ±0.5076 | +0.329 | 0.7419 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.894** | **4.41e-23** | *** |
| **BMI (kg/m2)** | **+0.0776** | 0.0164 | ±0.0328 | **+4.730** | **2.25e-06** | *** |
| Hypertension | +0.2938 | 0.2264 | ±0.4528 | +1.298 | 0.1944 |  |
| **High cholesterol** | **+0.6670** | 0.2125 | ±0.4251 | **+3.138** | **0.0017** | ** |
| **Kidney disease** | **+0.9436** | 0.3769 | ±0.7539 | **+2.503** | **0.0123** | * |
| **Circulatory disease** | **+1.1301** | 0.3195 | ±0.6389 | **+3.538** | **4.04e-04** | *** |
| Time < 70 (%) | +0.0259 | 0.0576 | ±0.1151 | +0.450 | 0.6524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2135**, R² = **0.1076**, Adj R² = **0.1030**, F-statistic = **23.28** (p = **1.18e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.7**, BIC = **12760.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4660** | 0.8350 | ±1.6699 | **+10.139** | **3.70e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8389** | 0.2146 | ±0.4292 | **-3.909** | **9.27e-05** | *** |
| **Education: high school or below (vs college)** | **+1.3030** | 0.4057 | ±0.8114 | **+3.212** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.0936 | 0.2739 | ±0.5479 | +0.342 | 0.7325 |  |
| Site: UW (vs UAB) | +0.0911 | 0.2536 | ±0.5073 | +0.359 | 0.7194 |  |
| **Age (years)** | **-0.0940** | 0.0095 | ±0.0190 | **-9.910** | **3.78e-23** | *** |
| **BMI (kg/m2)** | **+0.0775** | 0.0164 | ±0.0328 | **+4.725** | **2.30e-06** | *** |
| Hypertension | +0.2960 | 0.2264 | ±0.4529 | +1.307 | 0.1912 |  |
| **High cholesterol** | **+0.6692** | 0.2123 | ±0.4247 | **+3.152** | **0.0016** | ** |
| **Kidney disease** | **+0.9437** | 0.3767 | ±0.7534 | **+2.505** | **0.0122** | * |
| **Circulatory disease** | **+1.1291** | 0.3194 | ±0.6389 | **+3.535** | **4.08e-04** | *** |
| Avg. daily time < 70 (%) | +0.0457 | 0.0593 | ±0.1185 | +0.771 | 0.4406 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1082**, Adj R² = **0.1035**, F-statistic = **23.41** (p = **6.32e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.4**, BIC = **12759.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.7792** | 1.4342 | ±2.8684 | **+6.819** | **9.20e-12** | *** |
| **Education: graduate level (vs college)** | **-0.8304** | 0.2146 | ±0.4292 | **-3.869** | **1.09e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2487** | 0.4056 | ±0.8111 | **+3.079** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1000 | 0.2746 | ±0.5492 | +0.364 | 0.7157 |  |
| Site: UW (vs UAB) | +0.0973 | 0.2554 | ±0.5107 | +0.381 | 0.7032 |  |
| **Age (years)** | **-0.0938** | 0.0095 | ±0.0190 | **-9.880** | **5.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0329 | **+4.662** | **3.12e-06** | *** |
| Hypertension | +0.2763 | 0.2263 | ±0.4526 | +1.221 | 0.2221 |  |
| **High cholesterol** | **+0.6579** | 0.2121 | ±0.4242 | **+3.102** | **0.0019** | ** |
| **Kidney disease** | **+0.9102** | 0.3792 | ±0.7584 | **+2.400** | **0.0164** | * |
| **Circulatory disease** | **+1.1188** | 0.3190 | ±0.6380 | **+3.507** | **4.53e-04** | *** |
| Time 54-250, pooled (%) | -0.0130 | 0.0120 | ±0.0241 | -1.085 | 0.2781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.41e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.8**, BIC = **12759.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.6843** | 1.4604 | ±2.9208 | **+6.631** | **3.33e-11** | *** |
| **Education: graduate level (vs college)** | **-0.8320** | 0.2146 | ±0.4292 | **-3.877** | **1.06e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2526** | 0.4057 | ±0.8113 | **+3.088** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.0977 | 0.2747 | ±0.5493 | +0.356 | 0.7219 |  |
| Site: UW (vs UAB) | +0.0944 | 0.2553 | ±0.5105 | +0.370 | 0.7116 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.889** | **4.65e-23** | *** |
| **BMI (kg/m2)** | **+0.0769** | 0.0165 | ±0.0330 | **+4.666** | **3.07e-06** | *** |
| Hypertension | +0.2782 | 0.2263 | ±0.4525 | +1.229 | 0.2189 |  |
| **High cholesterol** | **+0.6582** | 0.2121 | ±0.4243 | **+3.103** | **0.0019** | ** |
| **Kidney disease** | **+0.9118** | 0.3792 | ±0.7584 | **+2.404** | **0.0162** | * |
| **Circulatory disease** | **+1.1193** | 0.3191 | ±0.6381 | **+3.508** | **4.51e-04** | *** |
| Avg. daily time 54-250 (%) | -0.0120 | 0.0123 | ±0.0245 | -0.979 | 0.3274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1030**, F-statistic = **23.28** (p = **1.13e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5361** | 0.8339 | ±1.6679 | **+10.236** | **1.37e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8429** | 0.2144 | ±0.4287 | **-3.932** | **8.41e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2694** | 0.4076 | ±0.8152 | **+3.114** | **0.0018** | ** |
| Site: UCSD (vs UAB) | +0.0899 | 0.2749 | ±0.5498 | +0.327 | 0.7438 |  |
| Site: UW (vs UAB) | +0.0776 | 0.2540 | ±0.5081 | +0.306 | 0.7599 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0191 | **-9.927** | **3.17e-23** | *** |
| **BMI (kg/m2)** | **+0.0766** | 0.0164 | ±0.0329 | **+4.661** | **3.15e-06** | *** |
| Hypertension | +0.2784 | 0.2267 | ±0.4534 | +1.228 | 0.2194 |  |
| **High cholesterol** | **+0.6513** | 0.2127 | ±0.4254 | **+3.062** | **0.0022** | ** |
| **Kidney disease** | **+0.9098** | 0.3822 | ±0.7645 | **+2.380** | **0.0173** | * |
| **Circulatory disease** | **+1.1264** | 0.3184 | ±0.6368 | **+3.538** | **4.03e-04** | *** |
| Time 181-250, pooled (%) | +0.0069 | 0.0088 | ±0.0176 | +0.781 | 0.4350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1077**, Adj R² = **0.1030**, F-statistic = **23.29** (p = **1.11e-45**), Residual SE = **4.715** on **2123** df, AIC = **12692.6**, BIC = **12760.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5361** | 0.8340 | ±1.6681 | **+10.235** | **1.39e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8432** | 0.2143 | ±0.4287 | **-3.934** | **8.37e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2682** | 0.4077 | ±0.8154 | **+3.110** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.0910 | 0.2749 | ±0.5498 | +0.331 | 0.7406 |  |
| Site: UW (vs UAB) | +0.0783 | 0.2540 | ±0.5081 | +0.308 | 0.7578 |  |
| **Age (years)** | **-0.0948** | 0.0095 | ±0.0191 | **-9.931** | **3.07e-23** | *** |
| **BMI (kg/m2)** | **+0.0766** | 0.0164 | ±0.0329 | **+4.657** | **3.20e-06** | *** |
| Hypertension | +0.2782 | 0.2267 | ±0.4535 | +1.227 | 0.2199 |  |
| **High cholesterol** | **+0.6509** | 0.2127 | ±0.4254 | **+3.060** | **0.0022** | ** |
| **Kidney disease** | **+0.9088** | 0.3822 | ±0.7644 | **+2.378** | **0.0174** | * |
| **Circulatory disease** | **+1.1265** | 0.3184 | ±0.6369 | **+3.538** | **4.04e-04** | *** |
| Avg. daily time 181-250 (%) | +0.0070 | 0.0087 | ±0.0174 | +0.799 | 0.4243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2135**, R² = **0.1081**, Adj R² = **0.1035**, F-statistic = **23.39** (p = **6.97e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.6**, BIC = **12759.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5221** | 0.8339 | ±1.6678 | **+10.220** | **1.62e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8344** | 0.2145 | ±0.4289 | **-3.891** | **1.00e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2465** | 0.4069 | ±0.8139 | **+3.063** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1004 | 0.2749 | ±0.5498 | +0.365 | 0.7149 |  |
| Site: UW (vs UAB) | +0.0894 | 0.2546 | ±0.5091 | +0.351 | 0.7255 |  |
| **Age (years)** | **-0.0947** | 0.0095 | ±0.0190 | **-9.944** | **2.69e-23** | *** |
| **BMI (kg/m2)** | **+0.0762** | 0.0165 | ±0.0329 | **+4.627** | **3.71e-06** | *** |
| Hypertension | +0.2708 | 0.2265 | ±0.4531 | +1.195 | 0.2320 |  |
| **High cholesterol** | **+0.6488** | 0.2123 | ±0.4246 | **+3.056** | **0.0022** | ** |
| **Kidney disease** | **+0.8929** | 0.3820 | ±0.7640 | **+2.337** | **0.0194** | * |
| **Circulatory disease** | **+1.1196** | 0.3184 | ±0.6368 | **+3.517** | **4.37e-04** | *** |
| Time > 180 (%) | +0.0068 | 0.0059 | ±0.0118 | +1.152 | 0.2494 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.62e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.8**, BIC = **12759.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5232** | 0.8340 | ±1.6680 | **+10.220** | **1.62e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8357** | 0.2145 | ±0.4289 | **-3.897** | **9.75e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2486** | 0.4070 | ±0.8141 | **+3.068** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1000 | 0.2749 | ±0.5499 | +0.364 | 0.7161 |  |
| Site: UW (vs UAB) | +0.0886 | 0.2545 | ±0.5091 | +0.348 | 0.7277 |  |
| **Age (years)** | **-0.0946** | 0.0095 | ±0.0190 | **-9.940** | **2.80e-23** | *** |
| **BMI (kg/m2)** | **+0.0763** | 0.0165 | ±0.0330 | **+4.629** | **3.68e-06** | *** |
| Hypertension | +0.2723 | 0.2265 | ±0.4531 | +1.202 | 0.2294 |  |
| **High cholesterol** | **+0.6494** | 0.2123 | ±0.4246 | **+3.059** | **0.0022** | ** |
| **Kidney disease** | **+0.8948** | 0.3820 | ±0.7639 | **+2.343** | **0.0192** | * |
| **Circulatory disease** | **+1.1202** | 0.3185 | ±0.6369 | **+3.518** | **4.35e-04** | *** |
| Avg. daily time > 180 (%) | +0.0064 | 0.0059 | ±0.0118 | +1.087 | 0.2771 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2135**, R² = **0.1092**, Adj R² = **0.1046**, F-statistic = **23.66** (p = **1.88e-46**), Residual SE = **4.711** on **2123** df, AIC = **12688.9**, BIC = **12756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5369** | 0.8345 | ±1.6690 | **+10.230** | **1.46e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8195** | 0.2147 | ±0.4294 | **-3.817** | **1.35e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2225** | 0.4062 | ±0.8123 | **+3.010** | **0.0026** | ** |
| Site: UCSD (vs UAB) | +0.1154 | 0.2743 | ±0.5486 | +0.421 | 0.6739 |  |
| Site: UW (vs UAB) | +0.0955 | 0.2544 | ±0.5088 | +0.375 | 0.7074 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0190 | **-9.918** | **3.49e-23** | *** |
| **BMI (kg/m2)** | **+0.0742** | 0.0165 | ±0.0331 | **+4.485** | **7.30e-06** | *** |
| Hypertension | +0.2698 | 0.2262 | ±0.4523 | +1.193 | 0.2330 |  |
| **High cholesterol** | **+0.6445** | 0.2120 | ±0.4240 | **+3.041** | **0.0024** | ** |
| **Kidney disease** | **+0.8803** | 0.3818 | ±0.7637 | **+2.305** | **0.0211** | * |
| **Circulatory disease** | **+1.1148** | 0.3185 | ±0.6369 | **+3.500** | **4.65e-04** | *** |
| Nocturnal time > 180 (%) | +0.0110 | 0.0060 | ±0.0120 | +1.821 | 0.0686 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1074**, Adj R² = **0.1028**, F-statistic = **23.23** (p = **1.49e-45**), Residual SE = **4.716** on **2123** df, AIC = **12693.2**, BIC = **12761.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4989** | 0.8333 | ±1.6667 | **+10.199** | **2.01e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8429** | 0.2148 | ±0.4296 | **-3.924** | **8.70e-05** | *** |
| **Education: high school or below (vs college)** | **+1.2868** | 0.4058 | ±0.8117 | **+3.171** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.0810 | 0.2743 | ±0.5487 | +0.295 | 0.7679 |  |
| Site: UW (vs UAB) | +0.0745 | 0.2537 | ±0.5073 | +0.294 | 0.7689 |  |
| **Age (years)** | **-0.0943** | 0.0095 | ±0.0191 | **-9.883** | **4.95e-23** | *** |
| **BMI (kg/m2)** | **+0.0777** | 0.0164 | ±0.0328 | **+4.736** | **2.17e-06** | *** |
| Hypertension | +0.2842 | 0.2263 | ±0.4527 | +1.256 | 0.2092 |  |
| **High cholesterol** | **+0.6580** | 0.2130 | ±0.4260 | **+3.089** | **0.0020** | ** |
| **Kidney disease** | **+0.9322** | 0.3781 | ±0.7563 | **+2.465** | **0.0137** | * |
| **Circulatory disease** | **+1.1323** | 0.3188 | ±0.6376 | **+3.552** | **3.83e-04** | *** |
| Any reading > 250 during wear (0/1) | +0.0729 | 0.2174 | ±0.4348 | +0.335 | 0.7375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2135**, R² = **0.1082**, Adj R² = **0.1036**, F-statistic = **23.41** (p = **6.13e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.4**, BIC = **12759.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4789** | 0.8345 | ±1.6690 | **+10.160** | **2.99e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8304** | 0.2146 | ±0.4292 | **-3.870** | **1.09e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2469** | 0.4057 | ±0.8113 | **+3.074** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.0984 | 0.2745 | ±0.5489 | +0.359 | 0.7199 |  |
| Site: UW (vs UAB) | +0.0961 | 0.2552 | ±0.5104 | +0.377 | 0.7065 |  |
| **Age (years)** | **-0.0938** | 0.0095 | ±0.0190 | **-9.882** | **5.00e-23** | *** |
| **BMI (kg/m2)** | **+0.0768** | 0.0165 | ±0.0330 | **+4.661** | **3.15e-06** | *** |
| Hypertension | +0.2758 | 0.2263 | ±0.4526 | +1.219 | 0.2229 |  |
| **High cholesterol** | **+0.6570** | 0.2121 | ±0.4242 | **+3.098** | **0.0020** | ** |
| **Kidney disease** | **+0.9096** | 0.3792 | ±0.7584 | **+2.399** | **0.0164** | * |
| **Circulatory disease** | **+1.1190** | 0.3190 | ±0.6379 | **+3.508** | **4.51e-04** | *** |
| Time > 250 (%) | +0.0133 | 0.0120 | ±0.0240 | +1.102 | 0.2704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2135**, R² = **0.1080**, Adj R² = **0.1034**, F-statistic = **23.37** (p = **7.37e-46**), Residual SE = **4.714** on **2123** df, AIC = **12691.7**, BIC = **12759.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4857** | 0.8344 | ±1.6688 | **+10.170** | **2.70e-24** | *** |
| **Education: graduate level (vs college)** | **-0.8323** | 0.2146 | ±0.4291 | **-3.879** | **1.05e-04** | *** |
| **Education: high school or below (vs college)** | **+1.2517** | 0.4057 | ±0.8115 | **+3.085** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.0965 | 0.2746 | ±0.5491 | +0.352 | 0.7251 |  |
| Site: UW (vs UAB) | +0.0932 | 0.2551 | ±0.5103 | +0.365 | 0.7150 |  |
| **Age (years)** | **-0.0939** | 0.0095 | ±0.0190 | **-9.889** | **4.66e-23** | *** |
| **BMI (kg/m2)** | **+0.0769** | 0.0165 | ±0.0330 | **+4.665** | **3.08e-06** | *** |
| Hypertension | +0.2779 | 0.2263 | ±0.4526 | +1.228 | 0.2194 |  |
| **High cholesterol** | **+0.6577** | 0.2121 | ±0.4243 | **+3.100** | **0.0019** | ** |
| **Kidney disease** | **+0.9117** | 0.3792 | ±0.7584 | **+2.404** | **0.0162** | * |
| **Circulatory disease** | **+1.1197** | 0.3190 | ±0.6380 | **+3.510** | **4.48e-04** | *** |
| Avg. daily time > 250 (%) | +0.0120 | 0.0123 | ±0.0245 | +0.982 | 0.3260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 2,135; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0669**, LLR χ² = **138.37** (p = **9.08e-25**), AUC = **0.6799**, AIC = **1952.1**, BIC = **2014.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4584 | 0.4537 | ±0.9075 | -1.010 | 0.3124 | 0.6323 |  |
| Education: graduate level (vs college) | -0.2185 | 0.1297 | ±0.2594 | -1.684 | 0.0921 | 0.8037 | . |
| Education: high school or below (vs college) | +0.2867 | 0.1712 | ±0.3425 | +1.674 | 0.0940 | 1.3321 | . |
| Site: UCSD (vs UAB) | -0.0662 | 0.1505 | ±0.3010 | -0.440 | 0.6602 | 0.9360 |  |
| Site: UW (vs UAB) | +0.0149 | 0.1389 | ±0.2779 | +0.107 | 0.9148 | 1.0150 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.881** | **5.93e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.285** | **1.83e-05** | 1.0331 | *** |
| Hypertension | +0.1669 | 0.1283 | ±0.2566 | +1.301 | 0.1933 | 1.1817 |  |
| **High cholesterol** | **+0.3597** | 0.1221 | ±0.2441 | **+2.947** | **0.0032** | 1.4330 | ** |
| **Kidney disease** | **+0.4941** | 0.1716 | ±0.3433 | **+2.878** | **0.0040** | 1.6390 | ** |
| **Circulatory disease** | **+0.5014** | 0.1487 | ±0.2975 | **+3.371** | **7.49e-04** | 1.6511 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0692**, LLR χ² = **143.07** (p = **3.86e-25**), AUC = **0.6826**, AIC = **1949.4**, BIC = **2017.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.0296** | 0.5244 | ±1.0489 | **-1.963** | **0.0496** | 0.3572 | * |
| Education: graduate level (vs college) | -0.1991 | 0.1302 | ±0.2604 | -1.529 | 0.1261 | 0.8195 |  |
| Education: high school or below (vs college) | +0.2429 | 0.1730 | ±0.3460 | +1.404 | 0.1604 | 1.2749 |  |
| Site: UCSD (vs UAB) | -0.0505 | 0.1510 | ±0.3020 | -0.335 | 0.7380 | 0.9507 |  |
| Site: UW (vs UAB) | +0.0353 | 0.1397 | ±0.2794 | +0.253 | 0.8004 | 1.0360 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.951** | **3.62e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0307** | 0.0077 | ±0.0154 | **+4.000** | **6.33e-05** | 1.0312 | *** |
| Hypertension | +0.1405 | 0.1292 | ±0.2584 | +1.088 | 0.2768 | 1.1508 |  |
| **High cholesterol** | **+0.3368** | 0.1226 | ±0.2452 | **+2.747** | **0.0060** | 1.4004 | ** |
| **Kidney disease** | **+0.4788** | 0.1721 | ±0.3442 | **+2.782** | **0.0054** | 1.6141 | ** |
| **Circulatory disease** | **+0.4950** | 0.1489 | ±0.2979 | **+3.324** | **8.88e-04** | 1.6405 | *** |
| **HbA1c (%)** | **+0.1095** | 0.0497 | ±0.0994 | **+2.203** | **0.0276** | 1.1157 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0684**, LLR χ² = **141.38** (p = **8.53e-25**), AUC = **0.6821**, AIC = **1951.1**, BIC = **2019.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7684 | 0.4879 | ±0.9757 | -1.575 | 0.1152 | 0.4637 |  |
| Education: graduate level (vs college) | -0.2080 | 0.1300 | ±0.2599 | -1.600 | 0.1096 | 0.8122 |  |
| Education: high school or below (vs college) | +0.2553 | 0.1724 | ±0.3448 | +1.481 | 0.1387 | 1.2908 |  |
| Site: UCSD (vs UAB) | -0.0522 | 0.1509 | ±0.3018 | -0.346 | 0.7291 | 0.9491 |  |
| Site: UW (vs UAB) | +0.0252 | 0.1393 | ±0.2786 | +0.181 | 0.8564 | 1.0255 |  |
| **Age (years)** | **-0.0403** | 0.0058 | ±0.0116 | **-6.937** | **4.02e-12** | 0.9605 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0076 | ±0.0153 | **+4.140** | **3.48e-05** | 1.0322 | *** |
| Hypertension | +0.1471 | 0.1290 | ±0.2580 | +1.140 | 0.2542 | 1.1585 |  |
| **High cholesterol** | **+0.3455** | 0.1224 | ±0.2448 | **+2.823** | **0.0048** | 1.4126 | ** |
| **Kidney disease** | **+0.4655** | 0.1726 | ±0.3453 | **+2.696** | **0.0070** | 1.5927 | ** |
| **Circulatory disease** | **+0.4954** | 0.1488 | ±0.2977 | **+3.328** | **8.74e-04** | 1.6411 | *** |
| Mean glucose (mg/dL) | +0.0028 | 0.0016 | ±0.0031 | +1.754 | 0.0794 | 1.0028 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0684**, LLR χ² = **141.38** (p = **8.53e-25**), AUC = **0.6821**, AIC = **1951.1**, BIC = **2019.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1507 | 0.6023 | ±1.2046 | -1.911 | 0.0561 | 0.3164 | . |
| Education: graduate level (vs college) | -0.2080 | 0.1300 | ±0.2599 | -1.600 | 0.1096 | 0.8122 |  |
| Education: high school or below (vs college) | +0.2553 | 0.1724 | ±0.3448 | +1.481 | 0.1387 | 1.2908 |  |
| Site: UCSD (vs UAB) | -0.0522 | 0.1509 | ±0.3018 | -0.346 | 0.7291 | 0.9491 |  |
| Site: UW (vs UAB) | +0.0252 | 0.1393 | ±0.2786 | +0.181 | 0.8564 | 1.0255 |  |
| **Age (years)** | **-0.0403** | 0.0058 | ±0.0116 | **-6.937** | **4.02e-12** | 0.9605 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0076 | ±0.0153 | **+4.140** | **3.48e-05** | 1.0322 | *** |
| Hypertension | +0.1471 | 0.1290 | ±0.2580 | +1.140 | 0.2542 | 1.1585 |  |
| **High cholesterol** | **+0.3455** | 0.1224 | ±0.2448 | **+2.823** | **0.0048** | 1.4126 | ** |
| **Kidney disease** | **+0.4655** | 0.1726 | ±0.3453 | **+2.696** | **0.0070** | 1.5927 | ** |
| **Circulatory disease** | **+0.4954** | 0.1488 | ±0.2977 | **+3.328** | **8.74e-04** | 1.6411 | *** |
| GMI (%) | +0.1155 | 0.0658 | ±0.1317 | +1.754 | 0.0794 | 1.1224 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0704**, LLR χ² = **145.57** (p = **1.20e-25**), AUC = **0.6855**, AIC = **1946.9**, BIC = **2014.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9315 | 0.4876 | ±0.9752 | -1.910 | 0.0561 | 0.3940 | . |
| Education: graduate level (vs college) | -0.1999 | 0.1301 | ±0.2603 | -1.536 | 0.1246 | 0.8189 |  |
| Education: high school or below (vs college) | +0.2406 | 0.1727 | ±0.3454 | +1.394 | 0.1635 | 1.2720 |  |
| Site: UCSD (vs UAB) | -0.0482 | 0.1510 | ±0.3020 | -0.319 | 0.7494 | 0.9529 |  |
| Site: UW (vs UAB) | +0.0248 | 0.1394 | ±0.2788 | +0.178 | 0.8588 | 1.0251 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.884** | **5.81e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0304** | 0.0077 | ±0.0154 | **+3.954** | **7.68e-05** | 1.0309 | *** |
| Hypertension | +0.1428 | 0.1289 | ±0.2579 | +1.107 | 0.2681 | 1.1535 |  |
| **High cholesterol** | **+0.3385** | 0.1225 | ±0.2450 | **+2.763** | **0.0057** | 1.4028 | ** |
| **Kidney disease** | **+0.4662** | 0.1724 | ±0.3448 | **+2.705** | **0.0068** | 1.5940 | ** |
| **Circulatory disease** | **+0.4964** | 0.1489 | ±0.2979 | **+3.333** | **8.59e-04** | 1.6427 | *** |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0042** | 0.0015 | ±0.0031 | **+2.723** | **0.0065** | 1.0042 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0691**, LLR χ² = **142.95** (p = **4.09e-25**), AUC = **0.6830**, AIC = **1949.5**, BIC = **2017.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6382 | 0.4624 | ±0.9248 | -1.380 | 0.1675 | 0.5282 |  |
| Education: graduate level (vs college) | -0.2002 | 0.1302 | ±0.2604 | -1.538 | 0.1240 | 0.8185 |  |
| Education: high school or below (vs college) | +0.2509 | 0.1724 | ±0.3448 | +1.456 | 0.1455 | 1.2852 |  |
| Site: UCSD (vs UAB) | -0.0470 | 0.1509 | ±0.3019 | -0.311 | 0.7554 | 0.9541 |  |
| Site: UW (vs UAB) | +0.0361 | 0.1396 | ±0.2792 | +0.258 | 0.7961 | 1.0367 |  |
| **Age (years)** | **-0.0409** | 0.0058 | ±0.0117 | **-7.010** | **2.38e-12** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0317** | 0.0076 | ±0.0153 | **+4.147** | **3.37e-05** | 1.0322 | *** |
| Hypertension | +0.1391 | 0.1293 | ±0.2586 | +1.076 | 0.2820 | 1.1492 |  |
| **High cholesterol** | **+0.3468** | 0.1224 | ±0.2447 | **+2.834** | **0.0046** | 1.4145 | ** |
| **Kidney disease** | **+0.4262** | 0.1751 | ±0.3501 | **+2.435** | **0.0149** | 1.5314 | * |
| **Circulatory disease** | **+0.4932** | 0.1490 | ±0.2979 | **+3.311** | **9.29e-04** | 1.6376 | *** |
| **Glucose SD, pooled (mg/dL)** | **+0.0101** | 0.0047 | ±0.0094 | **+2.160** | **0.0307** | 1.0102 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0681**, LLR χ² = **140.96** (p = **1.04e-24**), AUC = **0.6818**, AIC = **1951.5**, BIC = **2019.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5971 | 0.4625 | ±0.9250 | -1.291 | 0.1967 | 0.5504 |  |
| Education: graduate level (vs college) | -0.2056 | 0.1301 | ±0.2601 | -1.581 | 0.1139 | 0.8141 |  |
| Education: high school or below (vs college) | +0.2585 | 0.1723 | ±0.3446 | +1.500 | 0.1335 | 1.2950 |  |
| Site: UCSD (vs UAB) | -0.0529 | 0.1508 | ±0.3016 | -0.351 | 0.7258 | 0.9485 |  |
| Site: UW (vs UAB) | +0.0288 | 0.1394 | ±0.2788 | +0.207 | 0.8363 | 1.0292 |  |
| **Age (years)** | **-0.0407** | 0.0058 | ±0.0117 | **-6.985** | **2.85e-12** | 0.9601 | *** |
| **BMI (kg/m2)** | **+0.0321** | 0.0076 | ±0.0153 | **+4.204** | **2.62e-05** | 1.0326 | *** |
| Hypertension | +0.1466 | 0.1291 | ±0.2582 | +1.136 | 0.2562 | 1.1579 |  |
| **High cholesterol** | **+0.3502** | 0.1223 | ±0.2446 | **+2.863** | **0.0042** | 1.4193 | ** |
| **Kidney disease** | **+0.4412** | 0.1751 | ±0.3501 | **+2.520** | **0.0117** | 1.5546 | * |
| **Circulatory disease** | **+0.4965** | 0.1488 | ±0.2977 | **+3.336** | **8.50e-04** | 1.6430 | *** |
| Avg. daily SD (mg/dL) | +0.0087 | 0.0053 | ±0.0107 | +1.622 | 0.1048 | 1.0087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0674**, LLR χ² = **139.37** (p = **2.19e-24**), AUC = **0.6809**, AIC = **1953.1**, BIC = **2021.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6328 | 0.4863 | ±0.9725 | -1.301 | 0.1932 | 0.5311 |  |
| Education: graduate level (vs college) | -0.2114 | 0.1300 | ±0.2599 | -1.627 | 0.1038 | 0.8095 |  |
| Education: high school or below (vs college) | +0.2767 | 0.1716 | ±0.3432 | +1.612 | 0.1069 | 1.3187 |  |
| Site: UCSD (vs UAB) | -0.0573 | 0.1508 | ±0.3015 | -0.380 | 0.7037 | 0.9443 |  |
| Site: UW (vs UAB) | +0.0249 | 0.1394 | ±0.2788 | +0.179 | 0.8581 | 1.0252 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0117 | **-6.938** | **3.97e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0324** | 0.0076 | ±0.0152 | **+4.259** | **2.05e-05** | 1.0330 | *** |
| Hypertension | +0.1557 | 0.1289 | ±0.2578 | +1.208 | 0.2270 | 1.1685 |  |
| **High cholesterol** | **+0.3581** | 0.1221 | ±0.2443 | **+2.932** | **0.0034** | 1.4307 | ** |
| **Kidney disease** | **+0.4619** | 0.1748 | ±0.3496 | **+2.642** | **0.0082** | 1.5870 | ** |
| **Circulatory disease** | **+0.4979** | 0.1488 | ±0.2977 | **+3.345** | **8.24e-04** | 1.6452 | *** |
| CV (%) | +0.0109 | 0.0109 | ±0.0218 | +1.001 | 0.3167 | 1.0110 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0672**, LLR χ² = **139.07** (p = **2.52e-24**), AUC = **0.6806**, AIC = **1953.4**, BIC = **2021.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2245 | 0.5338 | ±1.0676 | -0.421 | 0.6741 | 0.7989 |  |
| Education: graduate level (vs college) | -0.2126 | 0.1299 | ±0.2599 | -1.636 | 0.1018 | 0.8085 |  |
| Education: high school or below (vs college) | +0.2775 | 0.1716 | ±0.3433 | +1.617 | 0.1059 | 1.3198 |  |
| Site: UCSD (vs UAB) | -0.0593 | 0.1507 | ±0.3015 | -0.394 | 0.6939 | 0.9424 |  |
| Site: UW (vs UAB) | +0.0217 | 0.1392 | ±0.2785 | +0.156 | 0.8762 | 1.0219 |  |
| **Age (years)** | **-0.0404** | 0.0058 | ±0.0117 | **-6.925** | **4.37e-12** | 0.9604 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.265** | **2.00e-05** | 1.0330 | *** |
| Hypertension | +0.1575 | 0.1289 | ±0.2578 | +1.222 | 0.2216 | 1.1706 |  |
| **High cholesterol** | **+0.3572** | 0.1221 | ±0.2443 | **+2.925** | **0.0034** | 1.4294 | ** |
| **Kidney disease** | **+0.4735** | 0.1735 | ±0.3469 | **+2.729** | **0.0063** | 1.6056 | ** |
| **Circulatory disease** | **+0.4980** | 0.1489 | ±0.2977 | **+3.345** | **8.22e-04** | 1.6454 | *** |
| Mean / SD ratio | -0.0364 | 0.0439 | ±0.0877 | -0.831 | 0.4061 | 0.9642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0669**, LLR χ² = **138.39** (p = **3.46e-24**), AUC = **0.6800**, AIC = **1954.1**, BIC = **2022.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4231 | 0.5309 | ±1.0617 | -0.797 | 0.4254 | 0.6550 |  |
| Education: graduate level (vs college) | -0.2176 | 0.1299 | ±0.2598 | -1.676 | 0.0938 | 0.8044 | . |
| Education: high school or below (vs college) | +0.2853 | 0.1716 | ±0.3432 | +1.662 | 0.0965 | 1.3301 | . |
| Site: UCSD (vs UAB) | -0.0656 | 0.1506 | ±0.3011 | -0.435 | 0.6632 | 0.9365 |  |
| Site: UW (vs UAB) | +0.0157 | 0.1391 | ±0.2782 | +0.113 | 0.9104 | 1.0158 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0117 | **-6.854** | **7.16e-12** | 0.9607 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.282** | **1.85e-05** | 1.0331 | *** |
| Hypertension | +0.1657 | 0.1287 | ±0.2573 | +1.288 | 0.1977 | 1.1803 |  |
| **High cholesterol** | **+0.3595** | 0.1221 | ±0.2441 | **+2.945** | **0.0032** | 1.4326 | ** |
| **Kidney disease** | **+0.4910** | 0.1733 | ±0.3465 | **+2.834** | **0.0046** | 1.6340 | ** |
| **Circulatory disease** | **+0.5012** | 0.1488 | ±0.2975 | **+3.369** | **7.54e-04** | 1.6507 | *** |
| Avg. daily mean/SD | -0.0047 | 0.0366 | ±0.0731 | -0.128 | 0.8983 | 0.9953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0692**, LLR χ² = **143.22** (p = **3.59e-25**), AUC = **0.6830**, AIC = **1949.2**, BIC = **2017.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0216 | 0.5219 | ±1.0438 | -1.958 | 0.0503 | 0.3600 | . |
| Education: graduate level (vs college) | -0.2010 | 0.1302 | ±0.2603 | -1.544 | 0.1225 | 0.8179 |  |
| Education: high school or below (vs college) | +0.2591 | 0.1722 | ±0.3443 | +1.505 | 0.1323 | 1.2958 |  |
| Site: UCSD (vs UAB) | -0.0440 | 0.1511 | ±0.3022 | -0.292 | 0.7706 | 0.9569 |  |
| Site: UW (vs UAB) | +0.0508 | 0.1402 | ±0.2804 | +0.362 | 0.7173 | 1.0521 |  |
| **Age (years)** | **-0.0398** | 0.0058 | ±0.0116 | **-6.832** | **8.36e-12** | 0.9610 | *** |
| **BMI (kg/m2)** | **+0.0320** | 0.0076 | ±0.0153 | **+4.182** | **2.89e-05** | 1.0325 | *** |
| Hypertension | +0.1597 | 0.1287 | ±0.2574 | +1.241 | 0.2146 | 1.1732 |  |
| **High cholesterol** | **+0.3632** | 0.1224 | ±0.2447 | **+2.968** | **0.0030** | 1.4379 | ** |
| **Kidney disease** | **+0.4620** | 0.1725 | ±0.3450 | **+2.678** | **0.0074** | 1.5872 | ** |
| **Circulatory disease** | **+0.4976** | 0.1490 | ±0.2981 | **+3.339** | **8.41e-04** | 1.6448 | *** |
| **MAG (mg/dL/h)** | **+0.0137** | 0.0062 | ±0.0124 | **+2.216** | **0.0267** | 1.0138 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0679**, LLR χ² = **140.44** (p = **1.32e-24**), AUC = **0.6814**, AIC = **1952.0**, BIC = **2020.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6522 | 0.4738 | ±0.9476 | -1.376 | 0.1687 | 0.5209 |  |
| Education: graduate level (vs college) | -0.2070 | 0.1300 | ±0.2601 | -1.592 | 0.1113 | 0.8130 |  |
| Education: high school or below (vs college) | +0.2617 | 0.1723 | ±0.3446 | +1.519 | 0.1288 | 1.2991 |  |
| Site: UCSD (vs UAB) | -0.0524 | 0.1509 | ±0.3017 | -0.347 | 0.7282 | 0.9489 |  |
| Site: UW (vs UAB) | +0.0277 | 0.1394 | ±0.2787 | +0.199 | 0.8425 | 1.0281 |  |
| **Age (years)** | **-0.0406** | 0.0058 | ±0.0117 | **-6.962** | **3.36e-12** | 0.9602 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.259** | **2.05e-05** | 1.0330 | *** |
| Hypertension | +0.1521 | 0.1289 | ±0.2578 | +1.180 | 0.2379 | 1.1643 |  |
| **High cholesterol** | **+0.3522** | 0.1223 | ±0.2445 | **+2.880** | **0.0040** | 1.4221 | ** |
| **Kidney disease** | **+0.4487** | 0.1748 | ±0.3496 | **+2.567** | **0.0103** | 1.5663 | * |
| **Circulatory disease** | **+0.4951** | 0.1489 | ±0.2978 | **+3.325** | **8.85e-04** | 1.6406 | *** |
| Avg. daily range (mg/dL) | +0.0021 | 0.0015 | ±0.0029 | +1.448 | 0.1477 | 1.0021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0741**, LLR χ² = **153.32** (p = **3.12e-27**), AUC = **0.6891**, AIC = **1939.1**, BIC = **2007.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6570 | 0.4578 | ±0.9155 | -1.435 | 0.1512 | 0.5184 |  |
| Education: graduate level (vs college) | -0.1819 | 0.1307 | ±0.2614 | -1.392 | 0.1640 | 0.8337 |  |
| Education: high school or below (vs college) | +0.2495 | 0.1726 | ±0.3451 | +1.446 | 0.1482 | 1.2834 |  |
| Site: UCSD (vs UAB) | -0.0368 | 0.1515 | ±0.3029 | -0.243 | 0.8082 | 0.9639 |  |
| Site: UW (vs UAB) | +0.0527 | 0.1401 | ±0.2803 | +0.376 | 0.7069 | 1.0541 |  |
| **Age (years)** | **-0.0402** | 0.0058 | ±0.0116 | **-6.913** | **4.74e-12** | 0.9606 | *** |
| **BMI (kg/m2)** | **+0.0303** | 0.0077 | ±0.0154 | **+3.938** | **8.21e-05** | 1.0307 | *** |
| Hypertension | +0.1285 | 0.1296 | ±0.2592 | +0.992 | 0.3214 | 1.1371 |  |
| **High cholesterol** | **+0.3375** | 0.1227 | ±0.2454 | **+2.751** | **0.0059** | 1.4015 | ** |
| **Kidney disease** | **+0.4246** | 0.1740 | ±0.3479 | **+2.441** | **0.0146** | 1.5290 | * |
| **Circulatory disease** | **+0.4735** | 0.1498 | ±0.2996 | **+3.161** | **0.0016** | 1.6056 | ** |
| **SD of daily means (mg/dL)** | **+0.0322** | 0.0082 | ±0.0164 | **+3.926** | **8.65e-05** | 1.0327 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0689**, LLR χ² = **142.54** (p = **4.96e-25**), AUC = **0.6827**, AIC = **1949.9**, BIC = **2017.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0868 | 0.5256 | ±1.0511 | +0.165 | 0.8688 | 1.0907 |  |
| Education: graduate level (vs college) | -0.2021 | 0.1301 | ±0.2603 | -1.553 | 0.1205 | 0.8170 |  |
| Education: high school or below (vs college) | +0.2520 | 0.1724 | ±0.3448 | +1.462 | 0.1438 | 1.2866 |  |
| Site: UCSD (vs UAB) | -0.0422 | 0.1512 | ±0.3023 | -0.279 | 0.7800 | 0.9587 |  |
| Site: UW (vs UAB) | +0.0349 | 0.1396 | ±0.2792 | +0.250 | 0.8023 | 1.0356 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.957** | **3.49e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0077 | ±0.0153 | **+4.112** | **3.92e-05** | 1.0320 | *** |
| Hypertension | +0.1493 | 0.1289 | ±0.2577 | +1.159 | 0.2466 | 1.1610 |  |
| **High cholesterol** | **+0.3470** | 0.1223 | ±0.2447 | **+2.836** | **0.0046** | 1.4148 | ** |
| **Kidney disease** | **+0.4549** | 0.1730 | ±0.3461 | **+2.629** | **0.0086** | 1.5760 | ** |
| **Circulatory disease** | **+0.4939** | 0.1489 | ±0.2978 | **+3.317** | **9.10e-04** | 1.6387 | *** |
| **Time in range 70-180, pooled (%)** | **-0.0055** | 0.0026 | ±0.0053 | **-2.071** | **0.0384** | 0.9945 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0688**, LLR χ² = **142.21** (p = **5.77e-25**), AUC = **0.6826**, AIC = **1950.3**, BIC = **2018.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.0681 | 0.5263 | ±1.0526 | +0.129 | 0.8971 | 1.0704 |  |
| Education: graduate level (vs college) | -0.2031 | 0.1301 | ±0.2602 | -1.561 | 0.1186 | 0.8162 |  |
| Education: high school or below (vs college) | +0.2528 | 0.1724 | ±0.3448 | +1.466 | 0.1426 | 1.2876 |  |
| Site: UCSD (vs UAB) | -0.0429 | 0.1512 | ±0.3023 | -0.284 | 0.7767 | 0.9580 |  |
| Site: UW (vs UAB) | +0.0341 | 0.1396 | ±0.2791 | +0.244 | 0.8071 | 1.0347 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.958** | **3.46e-12** | 0.9603 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0077 | ±0.0153 | **+4.115** | **3.88e-05** | 1.0320 | *** |
| Hypertension | +0.1504 | 0.1288 | ±0.2577 | +1.167 | 0.2431 | 1.1623 |  |
| **High cholesterol** | **+0.3473** | 0.1223 | ±0.2447 | **+2.839** | **0.0045** | 1.4152 | ** |
| **Kidney disease** | **+0.4556** | 0.1731 | ±0.3461 | **+2.633** | **0.0085** | 1.5772 | ** |
| **Circulatory disease** | **+0.4943** | 0.1489 | ±0.2977 | **+3.320** | **8.99e-04** | 1.6394 | *** |
| **Avg. daily time in range 70-180 (%)** | **-0.0053** | 0.0026 | ±0.0053 | **-1.989** | **0.0467** | 0.9948 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0674**, LLR χ² = **139.42** (p = **2.14e-24**), AUC = **0.6797**, AIC = **1953.0**, BIC = **2021.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5226 | 0.4581 | ±0.9162 | -1.141 | 0.2540 | 0.5930 |  |
| Education: graduate level (vs college) | -0.2157 | 0.1298 | ±0.2596 | -1.662 | 0.0965 | 0.8059 | . |
| Education: high school or below (vs college) | +0.2992 | 0.1718 | ±0.3435 | +1.742 | 0.0815 | 1.3488 | . |
| Site: UCSD (vs UAB) | -0.0504 | 0.1513 | ±0.3027 | -0.333 | 0.7393 | 0.9509 |  |
| Site: UW (vs UAB) | +0.0244 | 0.1393 | ±0.2786 | +0.175 | 0.8612 | 1.0247 |  |
| **Age (years)** | **-0.0396** | 0.0058 | ±0.0116 | **-6.800** | **1.05e-11** | 0.9612 | *** |
| **BMI (kg/m2)** | **+0.0323** | 0.0076 | ±0.0152 | **+4.231** | **2.32e-05** | 1.0328 | *** |
| Hypertension | +0.1651 | 0.1284 | ±0.2568 | +1.286 | 0.1985 | 1.1795 |  |
| **High cholesterol** | **+0.3680** | 0.1224 | ±0.2447 | **+3.007** | **0.0026** | 1.4448 | ** |
| **Kidney disease** | **+0.4967** | 0.1718 | ±0.3435 | **+2.892** | **0.0038** | 1.6434 | ** |
| **Circulatory disease** | **+0.4912** | 0.1491 | ±0.2983 | **+3.293** | **9.90e-04** | 1.6342 | *** |
| Any reading < 54 during wear (0/1) | +0.1280 | 0.1245 | ±0.2490 | +1.028 | 0.3039 | 1.1366 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.55** (p = **3.21e-24**), AUC = **0.6800**, AIC = **1953.9**, BIC = **2021.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4440 | 0.4550 | ±0.9100 | -0.976 | 0.3291 | 0.6415 |  |
| Education: graduate level (vs college) | -0.2188 | 0.1297 | ±0.2594 | -1.687 | 0.0916 | 0.8035 | . |
| Education: high school or below (vs college) | +0.2827 | 0.1715 | ±0.3430 | +1.649 | 0.0992 | 1.3267 | . |
| Site: UCSD (vs UAB) | -0.0738 | 0.1515 | ±0.3031 | -0.487 | 0.6263 | 0.9289 |  |
| Site: UW (vs UAB) | +0.0089 | 0.1396 | ±0.2792 | +0.064 | 0.9492 | 1.0089 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.890** | **5.58e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0327** | 0.0076 | ±0.0152 | **+4.294** | **1.75e-05** | 1.0332 | *** |
| Hypertension | +0.1660 | 0.1283 | ±0.2567 | +1.294 | 0.1958 | 1.1806 |  |
| **High cholesterol** | **+0.3567** | 0.1223 | ±0.2445 | **+2.917** | **0.0035** | 1.4286 | ** |
| **Kidney disease** | **+0.4935** | 0.1717 | ±0.3434 | **+2.874** | **0.0040** | 1.6380 | ** |
| **Circulatory disease** | **+0.5035** | 0.1488 | ±0.2977 | **+3.383** | **7.16e-04** | 1.6546 | *** |
| Time < 54 (%) | -0.0547 | 0.1338 | ±0.2677 | -0.409 | 0.6827 | 0.9468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0669**, LLR χ² = **138.42** (p = **3.41e-24**), AUC = **0.6800**, AIC = **1954.0**, BIC = **2022.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4541 | 0.4541 | ±0.9083 | -1.000 | 0.3174 | 0.6350 |  |
| Education: graduate level (vs college) | -0.2191 | 0.1297 | ±0.2595 | -1.689 | 0.0912 | 0.8032 | . |
| Education: high school or below (vs college) | +0.2849 | 0.1714 | ±0.3429 | +1.662 | 0.0965 | 1.3296 | . |
| Site: UCSD (vs UAB) | -0.0694 | 0.1512 | ±0.3024 | -0.459 | 0.6463 | 0.9330 |  |
| Site: UW (vs UAB) | +0.0118 | 0.1396 | ±0.2792 | +0.085 | 0.9325 | 1.0119 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.880** | **5.97e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.288** | **1.80e-05** | 1.0332 | *** |
| Hypertension | +0.1664 | 0.1283 | ±0.2567 | +1.297 | 0.1948 | 1.1810 |  |
| **High cholesterol** | **+0.3583** | 0.1222 | ±0.2444 | **+2.932** | **0.0034** | 1.4309 | ** |
| **Kidney disease** | **+0.4940** | 0.1717 | ±0.3433 | **+2.878** | **0.0040** | 1.6389 | ** |
| **Circulatory disease** | **+0.5024** | 0.1488 | ±0.2976 | **+3.376** | **7.35e-04** | 1.6527 | *** |
| Avg. daily time < 54 (%) | -0.0312 | 0.1447 | ±0.2894 | -0.216 | 0.8290 | 0.9692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.68** (p = **3.03e-24**), AUC = **0.6802**, AIC = **1953.8**, BIC = **2021.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4761 | 0.4549 | ±0.9098 | -1.047 | 0.2953 | 0.6212 |  |
| Education: graduate level (vs college) | -0.2156 | 0.1299 | ±0.2597 | -1.661 | 0.0968 | 0.8060 | . |
| Education: high school or below (vs college) | +0.2903 | 0.1714 | ±0.3428 | +1.694 | 0.0903 | 1.3369 | . |
| Site: UCSD (vs UAB) | -0.0589 | 0.1511 | ±0.3022 | -0.390 | 0.6966 | 0.9428 |  |
| Site: UW (vs UAB) | +0.0210 | 0.1394 | ±0.2789 | +0.151 | 0.8803 | 1.0212 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.881** | **5.95e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.273** | **1.93e-05** | 1.0331 | *** |
| Hypertension | +0.1689 | 0.1284 | ±0.2568 | +1.316 | 0.1883 | 1.1840 |  |
| **High cholesterol** | **+0.3625** | 0.1222 | ±0.2444 | **+2.967** | **0.0030** | 1.4369 | ** |
| **Kidney disease** | **+0.4940** | 0.1716 | ±0.3433 | **+2.878** | **0.0040** | 1.6389 | ** |
| **Circulatory disease** | **+0.5006** | 0.1488 | ±0.2975 | **+3.365** | **7.65e-04** | 1.6497 | *** |
| Time 54-69, pooled (%) | +0.0211 | 0.0377 | ±0.0754 | +0.559 | 0.5763 | 1.0213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0671**, LLR χ² = **138.70** (p = **2.99e-24**), AUC = **0.6802**, AIC = **1953.8**, BIC = **2021.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4729 | 0.4545 | ±0.9090 | -1.041 | 0.2981 | 0.6232 |  |
| Education: graduate level (vs college) | -0.2151 | 0.1299 | ±0.2598 | -1.656 | 0.0977 | 0.8065 | . |
| Education: high school or below (vs college) | +0.2903 | 0.1714 | ±0.3428 | +1.694 | 0.0903 | 1.3368 | . |
| Site: UCSD (vs UAB) | -0.0598 | 0.1509 | ±0.3019 | -0.396 | 0.6919 | 0.9419 |  |
| Site: UW (vs UAB) | +0.0211 | 0.1394 | ±0.2789 | +0.152 | 0.8795 | 1.0214 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.887** | **5.70e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0325** | 0.0076 | ±0.0152 | **+4.273** | **1.93e-05** | 1.0331 | *** |
| Hypertension | +0.1689 | 0.1284 | ±0.2568 | +1.315 | 0.1884 | 1.1840 |  |
| **High cholesterol** | **+0.3624** | 0.1222 | ±0.2443 | **+2.966** | **0.0030** | 1.4367 | ** |
| **Kidney disease** | **+0.4943** | 0.1716 | ±0.3433 | **+2.880** | **0.0040** | 1.6393 | ** |
| **Circulatory disease** | **+0.5010** | 0.1487 | ±0.2975 | **+3.368** | **7.57e-04** | 1.6503 | *** |
| Avg. daily time 54-69 (%) | +0.0216 | 0.0372 | ±0.0743 | +0.581 | 0.5610 | 1.0218 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.49** (p = **3.30e-24**), AUC = **0.6800**, AIC = **1954.0**, BIC = **2022.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4704 | 0.4551 | ±0.9102 | -1.034 | 0.3013 | 0.6248 |  |
| Education: graduate level (vs college) | -0.2169 | 0.1298 | ±0.2596 | -1.671 | 0.0947 | 0.8050 | . |
| Education: high school or below (vs college) | +0.2894 | 0.1714 | ±0.3429 | +1.688 | 0.0914 | 1.3356 | . |
| Site: UCSD (vs UAB) | -0.0609 | 0.1513 | ±0.3026 | -0.402 | 0.6875 | 0.9410 |  |
| Site: UW (vs UAB) | +0.0193 | 0.1396 | ±0.2791 | +0.138 | 0.8901 | 1.0195 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.879** | **6.03e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.277** | **1.90e-05** | 1.0331 | *** |
| Hypertension | +0.1681 | 0.1284 | ±0.2568 | +1.310 | 0.1903 | 1.1831 |  |
| **High cholesterol** | **+0.3618** | 0.1222 | ±0.2444 | **+2.960** | **0.0031** | 1.4359 | ** |
| **Kidney disease** | **+0.4941** | 0.1716 | ±0.3433 | **+2.879** | **0.0040** | 1.6391 | ** |
| **Circulatory disease** | **+0.5006** | 0.1488 | ±0.2975 | **+3.365** | **7.66e-04** | 1.6496 | *** |
| Time < 70 (%) | +0.0108 | 0.0311 | ±0.0622 | +0.347 | 0.7284 | 1.0109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0670**, LLR χ² = **138.55** (p = **3.20e-24**), AUC = **0.6801**, AIC = **1953.9**, BIC = **2021.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4694 | 0.4545 | ±0.9090 | -1.033 | 0.3017 | 0.6254 |  |
| Education: graduate level (vs college) | -0.2161 | 0.1299 | ±0.2597 | -1.664 | 0.0962 | 0.8057 | . |
| Education: high school or below (vs college) | +0.2898 | 0.1714 | ±0.3428 | +1.691 | 0.0909 | 1.3362 | . |
| Site: UCSD (vs UAB) | -0.0608 | 0.1511 | ±0.3021 | -0.402 | 0.6876 | 0.9411 |  |
| Site: UW (vs UAB) | +0.0202 | 0.1395 | ±0.2791 | +0.145 | 0.8851 | 1.0204 |  |
| **Age (years)** | **-0.0400** | 0.0058 | ±0.0116 | **-6.885** | **5.78e-12** | 0.9608 | *** |
| **BMI (kg/m2)** | **+0.0326** | 0.0076 | ±0.0152 | **+4.276** | **1.90e-05** | 1.0331 | *** |
| Hypertension | +0.1684 | 0.1284 | ±0.2568 | +1.311 | 0.1897 | 1.1834 |  |
| **High cholesterol** | **+0.3620** | 0.1222 | ±0.2444 | **+2.963** | **0.0030** | 1.4362 | ** |
| **Kidney disease** | **+0.4942** | 0.1716 | ±0.3433 | **+2.880** | **0.0040** | 1.6392 | ** |
| **Circulatory disease** | **+0.5007** | 0.1487 | ±0.2975 | **+3.366** | **7.63e-04** | 1.6498 | *** |
| Avg. daily time < 70 (%) | +0.0135 | 0.0311 | ±0.0623 | +0.432 | 0.6654 | 1.0136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0679**, LLR χ² = **140.54** (p = **1.27e-24**), AUC = **0.6819**, AIC = **1951.9**, BIC = **2019.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1827 | 0.6236 | ±1.2473 | +0.293 | 0.7696 | 1.2004 |  |
| Education: graduate level (vs college) | -0.2066 | 0.1301 | ±0.2601 | -1.589 | 0.1121 | 0.8133 |  |
| Education: high school or below (vs college) | +0.2624 | 0.1724 | ±0.3447 | +1.522 | 0.1280 | 1.3000 |  |
| Site: UCSD (vs UAB) | -0.0514 | 0.1510 | ±0.3019 | -0.341 | 0.7334 | 0.9499 |  |
| Site: UW (vs UAB) | +0.0310 | 0.1396 | ±0.2792 | +0.222 | 0.8242 | 1.0315 |  |
| **Age (years)** | **-0.0398** | 0.0058 | ±0.0116 | **-6.849** | **7.42e-12** | 0.9610 | *** |
| **BMI (kg/m2)** | **+0.0322** | 0.0076 | ±0.0153 | **+4.224** | **2.40e-05** | 1.0327 | *** |
| Hypertension | +0.1571 | 0.1286 | ±0.2572 | +1.222 | 0.2219 | 1.1701 |  |
| **High cholesterol** | **+0.3554** | 0.1221 | ±0.2442 | **+2.911** | **0.0036** | 1.4268 | ** |
| **Kidney disease** | **+0.4784** | 0.1722 | ±0.3444 | **+2.778** | **0.0055** | 1.6134 | ** |
| **Circulatory disease** | **+0.4981** | 0.1487 | ±0.2975 | **+3.349** | **8.11e-04** | 1.6455 | *** |
| Time 54-250, pooled (%) | -0.0066 | 0.0044 | ±0.0089 | -1.496 | 0.1345 | 0.9934 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0677**, LLR χ² = **140.03** (p = **1.60e-24**), AUC = **0.6817**, AIC = **1952.4**, BIC = **2020.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1181 | 0.6317 | ±1.2634 | +0.187 | 0.8516 | 1.1254 |  |
| Education: graduate level (vs college) | -0.2082 | 0.1300 | ±0.2601 | -1.602 | 0.1093 | 0.8120 |  |
| Education: high school or below (vs college) | +0.2653 | 0.1723 | ±0.3446 | +1.540 | 0.1236 | 1.3038 |  |
| Site: UCSD (vs UAB) | -0.0532 | 0.1509 | ±0.3019 | -0.353 | 0.7244 | 0.9482 |  |
| Site: UW (vs UAB) | +0.0286 | 0.1395 | ±0.2790 | +0.205 | 0.8375 | 1.0290 |  |
| **Age (years)** | **-0.0399** | 0.0058 | ±0.0116 | **-6.861** | **6.82e-12** | 0.9609 | *** |
| **BMI (kg/m2)** | **+0.0322** | 0.0076 | ±0.0152 | **+4.230** | **2.34e-05** | 1.0328 | *** |
| Hypertension | +0.1587 | 0.1286 | ±0.2571 | +1.234 | 0.2170 | 1.1720 |  |
| **High cholesterol** | **+0.3560** | 0.1221 | ±0.2442 | **+2.915** | **0.0036** | 1.4276 | ** |
| **Kidney disease** | **+0.4794** | 0.1722 | ±0.3444 | **+2.784** | **0.0054** | 1.6152 | ** |
| **Circulatory disease** | **+0.4982** | 0.1487 | ±0.2974 | **+3.350** | **8.08e-04** | 1.6458 | *** |
| Avg. daily time 54-250 (%) | -0.0059 | 0.0045 | ±0.0091 | -1.310 | 0.1901 | 0.9941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0685**, LLR χ² = **141.76** (p = **7.14e-25**), AUC = **0.6816**, AIC = **1950.7**, BIC = **2018.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4272 | 0.4547 | ±0.9093 | -0.940 | 0.3474 | 0.6523 |  |
| Education: graduate level (vs college) | -0.2098 | 0.1299 | ±0.2598 | -1.615 | 0.1064 | 0.8107 |  |
| Education: high school or below (vs college) | +0.2636 | 0.1718 | ±0.3435 | +1.534 | 0.1249 | 1.3016 |  |
| Site: UCSD (vs UAB) | -0.0514 | 0.1508 | ±0.3017 | -0.341 | 0.7334 | 0.9499 |  |
| Site: UW (vs UAB) | +0.0224 | 0.1392 | ±0.2784 | +0.161 | 0.8724 | 1.0226 |  |
| **Age (years)** | **-0.0409** | 0.0058 | ±0.0117 | **-7.009** | **2.39e-12** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0314** | 0.0077 | ±0.0153 | **+4.106** | **4.03e-05** | 1.0319 | *** |
| Hypertension | +0.1523 | 0.1288 | ±0.2576 | +1.183 | 0.2370 | 1.1645 |  |
| **High cholesterol** | **+0.3449** | 0.1225 | ±0.2449 | **+2.816** | **0.0049** | 1.4118 | ** |
| **Kidney disease** | **+0.4555** | 0.1731 | ±0.3463 | **+2.631** | **0.0085** | 1.5770 | ** |
| **Circulatory disease** | **+0.4947** | 0.1490 | ±0.2980 | **+3.320** | **8.99e-04** | 1.6400 | *** |
| Time 181-250, pooled (%) | +0.0081 | 0.0043 | ±0.0087 | +1.865 | 0.0622 | 1.0081 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0686**, LLR χ² = **141.93** (p = **6.61e-25**), AUC = **0.6817**, AIC = **1950.5**, BIC = **2018.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4272 | 0.4547 | ±0.9094 | -0.939 | 0.3475 | 0.6523 |  |
| Education: graduate level (vs college) | -0.2100 | 0.1299 | ±0.2598 | -1.617 | 0.1060 | 0.8106 |  |
| Education: high school or below (vs college) | +0.2620 | 0.1718 | ±0.3437 | +1.525 | 0.1273 | 1.2996 |  |
| Site: UCSD (vs UAB) | -0.0500 | 0.1509 | ±0.3018 | -0.332 | 0.7401 | 0.9512 |  |
| Site: UW (vs UAB) | +0.0232 | 0.1392 | ±0.2784 | +0.167 | 0.8675 | 1.0235 |  |
| **Age (years)** | **-0.0409** | 0.0058 | ±0.0117 | **-7.009** | **2.41e-12** | 0.9599 | *** |
| **BMI (kg/m2)** | **+0.0314** | 0.0077 | ±0.0153 | **+4.098** | **4.16e-05** | 1.0319 | *** |
| Hypertension | +0.1520 | 0.1288 | ±0.2576 | +1.180 | 0.2379 | 1.1642 |  |
| **High cholesterol** | **+0.3444** | 0.1225 | ±0.2450 | **+2.812** | **0.0049** | 1.4111 | ** |
| **Kidney disease** | **+0.4545** | 0.1732 | ±0.3463 | **+2.625** | **0.0087** | 1.5753 | ** |
| **Circulatory disease** | **+0.4950** | 0.1490 | ±0.2979 | **+3.323** | **8.91e-04** | 1.6405 | *** |
| Avg. daily time 181-250 (%) | +0.0081 | 0.0043 | ±0.0085 | +1.910 | 0.0561 | 1.0082 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0688**, LLR χ² = **142.34** (p = **5.44e-25**), AUC = **0.6824**, AIC = **1950.1**, BIC = **2018.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4553 | 0.4545 | ±0.9091 | -1.002 | 0.3165 | 0.6343 |  |
| Education: graduate level (vs college) | -0.2033 | 0.1301 | ±0.2602 | -1.563 | 0.1181 | 0.8160 |  |
| Education: high school or below (vs college) | +0.2519 | 0.1724 | ±0.3449 | +1.461 | 0.1441 | 1.2864 |  |
| Site: UCSD (vs UAB) | -0.0455 | 0.1511 | ±0.3021 | -0.302 | 0.7630 | 0.9555 |  |
| Site: UW (vs UAB) | +0.0322 | 0.1395 | ±0.2790 | +0.231 | 0.8176 | 1.0327 |  |
| **Age (years)** | **-0.0405** | 0.0058 | ±0.0116 | **-6.955** | **3.52e-12** | 0.9604 | *** |
| **BMI (kg/m2)** | **+0.0315** | 0.0077 | ±0.0153 | **+4.122** | **3.76e-05** | 1.0320 | *** |
| Hypertension | +0.1493 | 0.1289 | ±0.2577 | +1.159 | 0.2465 | 1.1611 |  |
| **High cholesterol** | **+0.3464** | 0.1223 | ±0.2447 | **+2.831** | **0.0046** | 1.4139 | ** |
| **Kidney disease** | **+0.4561** | 0.1730 | ±0.3460 | **+2.636** | **0.0084** | 1.5780 | ** |
| **Circulatory disease** | **+0.4945** | 0.1489 | ±0.2978 | **+3.322** | **8.95e-04** | 1.6397 | *** |
| **Time > 180 (%)** | **+0.0053** | 0.0026 | ±0.0052 | **+2.022** | **0.0432** | 1.0053 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0687**, LLR χ² = **142.02** (p = **6.32e-25**), AUC = **0.6824**, AIC = **1950.4**, BIC = **2018.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4529 | 0.4545 | ±0.9090 | -0.997 | 0.3190 | 0.6358 |  |
| Education: graduate level (vs college) | -0.2045 | 0.1301 | ±0.2601 | -1.572 | 0.1159 | 0.8151 |  |
| Education: high school or below (vs college) | +0.2527 | 0.1724 | ±0.3449 | +1.466 | 0.1428 | 1.2875 |  |
| Site: UCSD (vs UAB) | -0.0456 | 0.1511 | ±0.3021 | -0.302 | 0.7626 | 0.9554 |  |
| Site: UW (vs UAB) | +0.0315 | 0.1395 | ±0.2790 | +0.226 | 0.8213 | 1.0320 |  |
| **Age (years)** | **-0.0404** | 0.0058 | ±0.0116 | **-6.954** | **3.56e-12** | 0.9604 | *** |
| **BMI (kg/m2)** | **+0.0316** | 0.0077 | ±0.0153 | **+4.124** | **3.73e-05** | 1.0321 | *** |
| Hypertension | +0.1504 | 0.1288 | ±0.2577 | +1.168 | 0.2429 | 1.1623 |  |
| **High cholesterol** | **+0.3468** | 0.1223 | ±0.2447 | **+2.835** | **0.0046** | 1.4146 | ** |
| **Kidney disease** | **+0.4568** | 0.1730 | ±0.3461 | **+2.640** | **0.0083** | 1.5791 | ** |
| **Circulatory disease** | **+0.4948** | 0.1489 | ±0.2977 | **+3.324** | **8.88e-04** | 1.6402 | *** |
| Avg. daily time > 180 (%) | +0.0051 | 0.0026 | ±0.0052 | +1.937 | 0.0527 | 1.0051 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0710**, LLR χ² = **146.95** (p = **6.25e-26**), AUC = **0.6860**, AIC = **1945.5**, BIC = **2013.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4481 | 0.4553 | ±0.9106 | -0.984 | 0.3251 | 0.6388 |  |
| Education: graduate level (vs college) | -0.1901 | 0.1304 | ±0.2608 | -1.458 | 0.1449 | 0.8269 |  |
| Education: high school or below (vs college) | +0.2402 | 0.1726 | ±0.3453 | +1.391 | 0.1642 | 1.2714 |  |
| Site: UCSD (vs UAB) | -0.0329 | 0.1513 | ±0.3027 | -0.217 | 0.8279 | 0.9676 |  |
| Site: UW (vs UAB) | +0.0373 | 0.1397 | ±0.2795 | +0.267 | 0.7893 | 1.0380 |  |
| **Age (years)** | **-0.0403** | 0.0058 | ±0.0116 | **-6.923** | **4.42e-12** | 0.9605 | *** |
| **BMI (kg/m2)** | **+0.0304** | 0.0077 | ±0.0154 | **+3.950** | **7.81e-05** | 1.0309 | *** |
| Hypertension | +0.1496 | 0.1289 | ±0.2578 | +1.161 | 0.2457 | 1.1614 |  |
| **High cholesterol** | **+0.3446** | 0.1224 | ±0.2448 | **+2.815** | **0.0049** | 1.4114 | ** |
| **Kidney disease** | **+0.4540** | 0.1728 | ±0.3456 | **+2.627** | **0.0086** | 1.5745 | ** |
| **Circulatory disease** | **+0.4947** | 0.1491 | ±0.2981 | **+3.318** | **9.06e-04** | 1.6399 | *** |
| **Nocturnal time > 180 (%)** | **+0.0076** | 0.0025 | ±0.0051 | **+2.991** | **0.0028** | 1.0076 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0676**, LLR χ² = **139.84** (p = **1.75e-24**), AUC = **0.6795**, AIC = **1952.6**, BIC = **2020.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4663 | 0.4543 | ±0.9085 | -1.026 | 0.3047 | 0.6273 |  |
| Education: graduate level (vs college) | -0.2088 | 0.1300 | ±0.2600 | -1.606 | 0.1083 | 0.8116 |  |
| Education: high school or below (vs college) | +0.2767 | 0.1715 | ±0.3430 | +1.614 | 0.1066 | 1.3188 |  |
| Site: UCSD (vs UAB) | -0.0603 | 0.1506 | ±0.3012 | -0.400 | 0.6891 | 0.9415 |  |
| Site: UW (vs UAB) | +0.0175 | 0.1390 | ±0.2780 | +0.126 | 0.8997 | 1.0177 |  |
| **Age (years)** | **-0.0407** | 0.0058 | ±0.0117 | **-6.957** | **3.47e-12** | 0.9602 | *** |
| **BMI (kg/m2)** | **+0.0327** | 0.0076 | ±0.0152 | **+4.291** | **1.78e-05** | 1.0332 | *** |
| Hypertension | +0.1530 | 0.1290 | ±0.2579 | +1.187 | 0.2354 | 1.1654 |  |
| **High cholesterol** | **+0.3511** | 0.1224 | ±0.2447 | **+2.869** | **0.0041** | 1.4206 | ** |
| **Kidney disease** | **+0.4709** | 0.1728 | ±0.3456 | **+2.725** | **0.0064** | 1.6014 | ** |
| **Circulatory disease** | **+0.5012** | 0.1488 | ±0.2976 | **+3.368** | **7.56e-04** | 1.6508 | *** |
| Any reading > 250 during wear (0/1) | +0.1474 | 0.1212 | ±0.2424 | +1.216 | 0.2240 | 1.1588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0680**, LLR χ² = **140.58** (p = **1.24e-24**), AUC = **0.6820**, AIC = **1951.9**, BIC = **2019.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4800 | 0.4546 | ±0.9092 | -1.056 | 0.2910 | 0.6188 |  |
| Education: graduate level (vs college) | -0.2066 | 0.1300 | ±0.2601 | -1.589 | 0.1121 | 0.8133 |  |
| Education: high school or below (vs college) | +0.2617 | 0.1724 | ±0.3448 | +1.518 | 0.1291 | 1.2991 |  |
| Site: UCSD (vs UAB) | -0.0523 | 0.1509 | ±0.3019 | -0.347 | 0.7289 | 0.9490 |  |
| Site: UW (vs UAB) | +0.0304 | 0.1395 | ±0.2791 | +0.218 | 0.8277 | 1.0308 |  |
| **Age (years)** | **-0.0398** | 0.0058 | ±0.0116 | **-6.850** | **7.36e-12** | 0.9610 | *** |
| **BMI (kg/m2)** | **+0.0322** | 0.0076 | ±0.0153 | **+4.225** | **2.39e-05** | 1.0327 | *** |
| Hypertension | +0.1569 | 0.1286 | ±0.2572 | +1.220 | 0.2225 | 1.1699 |  |
| **High cholesterol** | **+0.3550** | 0.1221 | ±0.2442 | **+2.907** | **0.0036** | 1.4262 | ** |
| **Kidney disease** | **+0.4782** | 0.1722 | ±0.3444 | **+2.777** | **0.0055** | 1.6131 | ** |
| **Circulatory disease** | **+0.4983** | 0.1487 | ±0.2974 | **+3.350** | **8.07e-04** | 1.6459 | *** |
| Time > 250 (%) | +0.0067 | 0.0044 | ±0.0089 | +1.510 | 0.1310 | 1.0067 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,135)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2135**, events = **403**, McFadden pseudo-R² = **0.0677**, LLR χ² = **140.05** (p = **1.59e-24**), AUC = **0.6817**, AIC = **1952.4**, BIC = **2020.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4743 | 0.4544 | ±0.9088 | -1.044 | 0.2966 | 0.6224 |  |
| Education: graduate level (vs college) | -0.2083 | 0.1300 | ±0.2600 | -1.602 | 0.1091 | 0.8119 |  |
| Education: high school or below (vs college) | +0.2648 | 0.1723 | ±0.3447 | +1.537 | 0.1244 | 1.3032 |  |
| Site: UCSD (vs UAB) | -0.0538 | 0.1509 | ±0.3018 | -0.357 | 0.7215 | 0.9476 |  |
| Site: UW (vs UAB) | +0.0281 | 0.1395 | ±0.2790 | +0.201 | 0.8405 | 1.0285 |  |
| **Age (years)** | **-0.0399** | 0.0058 | ±0.0116 | **-6.861** | **6.83e-12** | 0.9609 | *** |
| **BMI (kg/m2)** | **+0.0323** | 0.0076 | ±0.0152 | **+4.230** | **2.33e-05** | 1.0328 | *** |
| Hypertension | +0.1586 | 0.1286 | ±0.2571 | +1.233 | 0.2174 | 1.1718 |  |
| **High cholesterol** | **+0.3557** | 0.1221 | ±0.2442 | **+2.913** | **0.0036** | 1.4271 | ** |
| **Kidney disease** | **+0.4794** | 0.1722 | ±0.3444 | **+2.784** | **0.0054** | 1.6150 | ** |
| **Circulatory disease** | **+0.4984** | 0.1487 | ±0.2974 | **+3.351** | **8.05e-04** | 1.6460 | *** |
| Avg. daily time > 250 (%) | +0.0060 | 0.0045 | ±0.0090 | +1.317 | 0.1877 | 1.0060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.1564**, Adj R² = **0.1512**, F-statistic = **29.76** (p = **4.62e-68**), Residual SE = **0.887** on **2086** df, AIC = **5469.4**, BIC = **5548.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5351** | 0.1632 | ±0.3264 | **+15.532** | **2.10e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1093** | 0.0397 | ±0.0794 | **-2.751** | **0.0059** | ** |
| **Education: high school or below (vs college)** | **+0.4907** | 0.0817 | ±0.1633 | **+6.008** | **1.88e-09** | *** |
| Site: UCSD (vs UAB) | +0.0353 | 0.0490 | ±0.0980 | +0.721 | 0.4712 |  |
| **Site: UW (vs UAB)** | **-0.3550** | 0.0504 | ±0.1008 | **-7.043** | **1.88e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1664** | 0.0530 | ±0.1061 | **-3.137** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0083 | 0.0564 | ±0.1129 | +0.147 | 0.8827 |  |
| Season: winter (vs autumn) | -0.0301 | 0.0564 | ±0.1128 | -0.534 | 0.5934 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.719** | **2.81e-18** | *** |
| **BMI (kg/m2)** | **+0.0147** | 0.0031 | ±0.0062 | **+4.711** | **2.46e-06** | *** |
| **Hypertension** | **+0.1158** | 0.0418 | ±0.0837 | **+2.768** | **0.0056** | ** |
| High cholesterol | -0.0450 | 0.0393 | ±0.0786 | -1.145 | 0.2522 |  |
| Kidney disease | -0.0587 | 0.0587 | ±0.1174 | -1.000 | 0.3175 |  |
| Circulatory disease | +0.1159 | 0.0593 | ±0.1185 | +1.956 | 0.0504 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.1616**, Adj R² = **0.1560**, F-statistic = **28.71** (p = **5.13e-70**), Residual SE = **0.884** on **2085** df, AIC = **5458.5**, BIC = **5543.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1789** | 0.1990 | ±0.3980 | **+10.949** | **6.73e-28** | *** |
| **Education: graduate level (vs college)** | **-0.1011** | 0.0398 | ±0.0796 | **-2.540** | **0.0111** | * |
| **Education: high school or below (vs college)** | **+0.4620** | 0.0806 | ±0.1612 | **+5.731** | **1.00e-08** | *** |
| Site: UCSD (vs UAB) | +0.0429 | 0.0490 | ±0.0979 | +0.876 | 0.3813 |  |
| **Site: UW (vs UAB)** | **-0.3459** | 0.0502 | ±0.1004 | **-6.890** | **5.57e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0529 | ±0.1058 | **-2.965** | **0.0030** | ** |
| Season: summer (vs autumn) | +0.0121 | 0.0563 | ±0.1126 | +0.215 | 0.8298 |  |
| Season: winter (vs autumn) | -0.0255 | 0.0562 | ±0.1125 | -0.453 | 0.6507 |  |
| **Age (years)** | **-0.0162** | 0.0018 | ±0.0036 | **-8.930** | **4.28e-19** | *** |
| **BMI (kg/m2)** | **+0.0134** | 0.0032 | ±0.0064 | **+4.201** | **2.66e-05** | *** |
| **Hypertension** | **+0.1012** | 0.0418 | ±0.0837 | **+2.419** | **0.0156** | * |
| High cholesterol | -0.0579 | 0.0392 | ±0.0784 | -1.475 | 0.1401 |  |
| Kidney disease | -0.0712 | 0.0585 | ±0.1169 | -1.217 | 0.2235 |  |
| Circulatory disease | +0.1096 | 0.0595 | ±0.1190 | +1.841 | 0.0656 | . |
| **HbA1c (%)** | **+0.0693** | 0.0236 | ±0.0473 | **+2.933** | **0.0034** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.1570**, Adj R² = **0.1514**, F-statistic = **27.75** (p = **1.27e-67**), Residual SE = **0.887** on **2085** df, AIC = **5470.0**, BIC = **5554.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4567** | 0.1790 | ±0.3581 | **+13.722** | **7.54e-43** | *** |
| **Education: graduate level (vs college)** | **-0.1076** | 0.0398 | ±0.0796 | **-2.703** | **0.0069** | ** |
| **Education: high school or below (vs college)** | **+0.4819** | 0.0813 | ±0.1625 | **+5.930** | **3.03e-09** | *** |
| Site: UCSD (vs UAB) | +0.0389 | 0.0490 | ±0.0979 | +0.794 | 0.4274 |  |
| **Site: UW (vs UAB)** | **-0.3531** | 0.0504 | ±0.1007 | **-7.010** | **2.39e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1658** | 0.0531 | ±0.1062 | **-3.123** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0097 | 0.0565 | ±0.1129 | +0.171 | 0.8639 |  |
| Season: winter (vs autumn) | -0.0289 | 0.0564 | ±0.1129 | -0.512 | 0.6089 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.762** | **1.91e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.571** | **4.85e-06** | *** |
| **Hypertension** | **+0.1109** | 0.0424 | ±0.0847 | **+2.618** | **0.0089** | ** |
| High cholesterol | -0.0479 | 0.0393 | ±0.0785 | -1.219 | 0.2228 |  |
| Kidney disease | -0.0667 | 0.0587 | ±0.1175 | -1.136 | 0.2560 |  |
| Circulatory disease | +0.1138 | 0.0596 | ±0.1192 | +1.910 | 0.0561 | . |
| Mean glucose (mg/dL) | +0.0007 | 0.0007 | ±0.0014 | +1.011 | 0.3121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.1570**, Adj R² = **0.1514**, F-statistic = **27.75** (p = **1.27e-67**), Residual SE = **0.887** on **2085** df, AIC = **5470.0**, BIC = **5554.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3573** | 0.2369 | ±0.4739 | **+9.949** | **2.56e-23** | *** |
| **Education: graduate level (vs college)** | **-0.1076** | 0.0398 | ±0.0796 | **-2.703** | **0.0069** | ** |
| **Education: high school or below (vs college)** | **+0.4819** | 0.0813 | ±0.1625 | **+5.930** | **3.03e-09** | *** |
| Site: UCSD (vs UAB) | +0.0389 | 0.0490 | ±0.0979 | +0.794 | 0.4274 |  |
| **Site: UW (vs UAB)** | **-0.3531** | 0.0504 | ±0.1007 | **-7.010** | **2.39e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1658** | 0.0531 | ±0.1062 | **-3.123** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0097 | 0.0565 | ±0.1129 | +0.171 | 0.8639 |  |
| Season: winter (vs autumn) | -0.0289 | 0.0564 | ±0.1129 | -0.512 | 0.6089 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.762** | **1.91e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.571** | **4.85e-06** | *** |
| **Hypertension** | **+0.1109** | 0.0424 | ±0.0847 | **+2.618** | **0.0089** | ** |
| High cholesterol | -0.0479 | 0.0393 | ±0.0785 | -1.219 | 0.2228 |  |
| Kidney disease | -0.0667 | 0.0587 | ±0.1175 | -1.136 | 0.2560 |  |
| Circulatory disease | +0.1138 | 0.0596 | ±0.1192 | +1.910 | 0.0561 | . |
| GMI (%) | +0.0300 | 0.0297 | ±0.0594 | +1.011 | 0.3121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.1575**, Adj R² = **0.1518**, F-statistic = **27.84** (p = **7.31e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.8**, BIC = **5553.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4309** | 0.1781 | ±0.3562 | **+13.649** | **2.05e-42** | *** |
| **Education: graduate level (vs college)** | **-0.1067** | 0.0398 | ±0.0796 | **-2.681** | **0.0073** | ** |
| **Education: high school or below (vs college)** | **+0.4796** | 0.0811 | ±0.1623 | **+5.910** | **3.41e-09** | *** |
| Site: UCSD (vs UAB) | +0.0389 | 0.0489 | ±0.0979 | +0.794 | 0.4271 |  |
| **Site: UW (vs UAB)** | **-0.3535** | 0.0504 | ±0.1008 | **-7.016** | **2.28e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1670** | 0.0531 | ±0.1061 | **-3.148** | **0.0016** | ** |
| Season: summer (vs autumn) | +0.0101 | 0.0564 | ±0.1128 | +0.178 | 0.8584 |  |
| Season: winter (vs autumn) | -0.0299 | 0.0564 | ±0.1128 | -0.530 | 0.5960 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.726** | **2.64e-18** | *** |
| **BMI (kg/m2)** | **+0.0141** | 0.0032 | ±0.0064 | **+4.420** | **9.87e-06** | *** |
| **Hypertension** | **+0.1105** | 0.0422 | ±0.0845 | **+2.617** | **0.0089** | ** |
| High cholesterol | -0.0491 | 0.0393 | ±0.0786 | -1.249 | 0.2115 |  |
| Kidney disease | -0.0659 | 0.0583 | ±0.1167 | -1.129 | 0.2587 |  |
| Circulatory disease | +0.1137 | 0.0595 | ±0.1190 | +1.912 | 0.0559 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0010 | 0.0007 | ±0.0014 | +1.328 | 0.1841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.1577**, Adj R² = **0.1520**, F-statistic = **27.88** (p = **5.92e-68**), Residual SE = **0.886** on **2085** df, AIC = **5468.4**, BIC = **5553.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4836** | 0.1650 | ±0.3299 | **+15.054** | **3.23e-51** | *** |
| **Education: graduate level (vs college)** | **-0.1052** | 0.0398 | ±0.0796 | **-2.641** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.4794** | 0.0816 | ±0.1633 | **+5.872** | **4.30e-09** | *** |
| Site: UCSD (vs UAB) | +0.0420 | 0.0490 | ±0.0980 | +0.858 | 0.3908 |  |
| **Site: UW (vs UAB)** | **-0.3495** | 0.0503 | ±0.1006 | **-6.950** | **3.65e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0531 | ±0.1062 | **-3.108** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0098 | 0.0564 | ±0.1128 | +0.174 | 0.8620 |  |
| Season: winter (vs autumn) | -0.0283 | 0.0564 | ±0.1128 | -0.502 | 0.6158 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.813** | **1.21e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.593** | **4.37e-06** | *** |
| **Hypertension** | **+0.1077** | 0.0422 | ±0.0844 | **+2.554** | **0.0107** | * |
| High cholesterol | -0.0480 | 0.0393 | ±0.0786 | -1.222 | 0.2216 |  |
| Kidney disease | -0.0780 | 0.0584 | ±0.1168 | -1.335 | 0.1818 |  |
| Circulatory disease | +0.1125 | 0.0596 | ±0.1192 | +1.887 | 0.0592 | . |
| Glucose SD, pooled (mg/dL) | +0.0030 | 0.0018 | ±0.0036 | +1.654 | 0.0981 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.1572**, Adj R² = **0.1515**, F-statistic = **27.78** (p = **1.04e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.6**, BIC = **5554.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4940** | 0.1652 | ±0.3303 | **+15.101** | **1.60e-51** | *** |
| **Education: graduate level (vs college)** | **-0.1064** | 0.0398 | ±0.0796 | **-2.673** | **0.0075** | ** |
| **Education: high school or below (vs college)** | **+0.4815** | 0.0818 | ±0.1637 | **+5.883** | **4.02e-09** | *** |
| Site: UCSD (vs UAB) | +0.0403 | 0.0490 | ±0.0980 | +0.823 | 0.4105 |  |
| **Site: UW (vs UAB)** | **-0.3512** | 0.0503 | ±0.1007 | **-6.978** | **3.00e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0531 | ±0.1062 | **-3.108** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0100 | 0.0565 | ±0.1129 | +0.178 | 0.8588 |  |
| Season: winter (vs autumn) | -0.0281 | 0.0565 | ±0.1129 | -0.498 | 0.6186 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.795** | **1.43e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0063 | **+4.630** | **3.66e-06** | *** |
| **Hypertension** | **+0.1095** | 0.0422 | ±0.0844 | **+2.594** | **0.0095** | ** |
| High cholesterol | -0.0474 | 0.0393 | ±0.0786 | -1.206 | 0.2277 |  |
| Kidney disease | -0.0741 | 0.0584 | ±0.1168 | -1.269 | 0.2043 |  |
| Circulatory disease | +0.1137 | 0.0596 | ±0.1191 | +1.909 | 0.0563 | . |
| Avg. daily SD (mg/dL) | +0.0026 | 0.0020 | ±0.0040 | +1.328 | 0.1840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.1576**, Adj R² = **0.1519**, F-statistic = **27.86** (p = **6.45e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.6**, BIC = **5553.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4324** | 0.1727 | ±0.3455 | **+14.081** | **4.94e-45** | *** |
| **Education: graduate level (vs college)** | **-0.1054** | 0.0398 | ±0.0795 | **-2.650** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4847** | 0.0819 | ±0.1637 | **+5.921** | **3.19e-09** | *** |
| Site: UCSD (vs UAB) | +0.0416 | 0.0491 | ±0.0981 | +0.848 | 0.3966 |  |
| **Site: UW (vs UAB)** | **-0.3494** | 0.0503 | ±0.1006 | **-6.942** | **3.86e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1646** | 0.0531 | ±0.1062 | **-3.099** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0084 | 0.0564 | ±0.1128 | +0.148 | 0.8821 |  |
| Season: winter (vs autumn) | -0.0289 | 0.0564 | ±0.1128 | -0.513 | 0.6081 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.810** | **1.25e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.686** | **2.79e-06** | *** |
| **Hypertension** | **+0.1094** | 0.0418 | ±0.0836 | **+2.615** | **0.0089** | ** |
| High cholesterol | -0.0457 | 0.0393 | ±0.0786 | -1.164 | 0.2444 |  |
| Kidney disease | -0.0761 | 0.0586 | ±0.1171 | -1.300 | 0.1936 |  |
| Circulatory disease | +0.1134 | 0.0595 | ±0.1189 | +1.906 | 0.0566 | . |
| CV (%) | +0.0064 | 0.0039 | ±0.0078 | +1.642 | 0.1005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.1576**, Adj R² = **0.1520**, F-statistic = **27.86** (p = **6.40e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.5**, BIC = **5553.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6947** | 0.1916 | ±0.3831 | **+14.066** | **6.12e-45** | *** |
| **Education: graduate level (vs college)** | **-0.1054** | 0.0398 | ±0.0795 | **-2.651** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4844** | 0.0818 | ±0.1636 | **+5.923** | **3.17e-09** | *** |
| Site: UCSD (vs UAB) | +0.0408 | 0.0491 | ±0.0982 | +0.830 | 0.4065 |  |
| **Site: UW (vs UAB)** | **-0.3511** | 0.0504 | ±0.1007 | **-6.970** | **3.16e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1655** | 0.0531 | ±0.1061 | **-3.120** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0076 | 0.0564 | ±0.1128 | +0.134 | 0.8934 |  |
| Season: winter (vs autumn) | -0.0301 | 0.0564 | ±0.1128 | -0.534 | 0.5935 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.806** | **1.29e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.681** | **2.85e-06** | *** |
| **Hypertension** | **+0.1092** | 0.0418 | ±0.0836 | **+2.612** | **0.0090** | ** |
| High cholesterol | -0.0462 | 0.0393 | ±0.0786 | -1.176 | 0.2394 |  |
| Kidney disease | -0.0721 | 0.0586 | ±0.1173 | -1.230 | 0.2186 |  |
| Circulatory disease | +0.1133 | 0.0594 | ±0.1189 | +1.906 | 0.0567 | . |
| Mean / SD ratio | -0.0249 | 0.0143 | ±0.0285 | -1.747 | 0.0807 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.1575**, Adj R² = **0.1519**, F-statistic = **27.85** (p = **7.11e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.8**, BIC = **5553.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6863** | 0.1894 | ±0.3788 | **+14.181** | **1.20e-45** | *** |
| **Education: graduate level (vs college)** | **-0.1061** | 0.0398 | ±0.0795 | **-2.667** | **0.0076** | ** |
| **Education: high school or below (vs college)** | **+0.4843** | 0.0819 | ±0.1638 | **+5.913** | **3.35e-09** | *** |
| Site: UCSD (vs UAB) | +0.0390 | 0.0490 | ±0.0981 | +0.795 | 0.4269 |  |
| **Site: UW (vs UAB)** | **-0.3521** | 0.0504 | ±0.1008 | **-6.988** | **2.79e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1650** | 0.0531 | ±0.1061 | **-3.110** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0090 | 0.0564 | ±0.1128 | +0.159 | 0.8738 |  |
| Season: winter (vs autumn) | -0.0292 | 0.0564 | ±0.1128 | -0.518 | 0.6043 |  |
| **Age (years)** | **-0.0162** | 0.0018 | ±0.0037 | **-8.816** | **1.18e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.687** | **2.77e-06** | *** |
| **Hypertension** | **+0.1102** | 0.0419 | ±0.0837 | **+2.631** | **0.0085** | ** |
| High cholesterol | -0.0459 | 0.0393 | ±0.0786 | -1.167 | 0.2431 |  |
| Kidney disease | -0.0710 | 0.0587 | ±0.1174 | -1.210 | 0.2261 |  |
| Circulatory disease | +0.1150 | 0.0594 | ±0.1187 | +1.937 | 0.0527 | . |
| Avg. daily mean/SD | -0.0201 | 0.0119 | ±0.0238 | -1.685 | 0.0919 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.1583**, Adj R² = **0.1527**, F-statistic = **28.01** (p = **2.76e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.8**, BIC = **5551.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3412** | 0.1796 | ±0.3592 | **+13.036** | **7.68e-39** | *** |
| **Education: graduate level (vs college)** | **-0.1043** | 0.0397 | ±0.0795 | **-2.625** | **0.0087** | ** |
| **Education: high school or below (vs college)** | **+0.4820** | 0.0814 | ±0.1627 | **+5.923** | **3.16e-09** | *** |
| Site: UCSD (vs UAB) | +0.0432 | 0.0489 | ±0.0978 | +0.883 | 0.3771 |  |
| **Site: UW (vs UAB)** | **-0.3438** | 0.0506 | ±0.1011 | **-6.800** | **1.05e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1647** | 0.0530 | ±0.1059 | **-3.110** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0125 | 0.0562 | ±0.1125 | +0.223 | 0.8237 |  |
| Season: winter (vs autumn) | -0.0268 | 0.0562 | ±0.1125 | -0.477 | 0.6332 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.701** | **3.28e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.617** | **3.89e-06** | *** |
| **Hypertension** | **+0.1132** | 0.0418 | ±0.0836 | **+2.709** | **0.0068** | ** |
| High cholesterol | -0.0443 | 0.0393 | ±0.0787 | -1.127 | 0.2597 |  |
| Kidney disease | -0.0706 | 0.0591 | ±0.1182 | -1.195 | 0.2319 |  |
| Circulatory disease | +0.1148 | 0.0592 | ±0.1185 | +1.937 | 0.0527 | . |
| **MAG (mg/dL/h)** | **+0.0047** | 0.0022 | ±0.0044 | **+2.148** | **0.0317** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.1571**, Adj R² = **0.1515**, F-statistic = **27.76** (p = **1.16e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.8**, BIC = **5554.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4736** | 0.1690 | ±0.3381 | **+14.633** | **1.74e-48** | *** |
| **Education: graduate level (vs college)** | **-0.1066** | 0.0398 | ±0.0796 | **-2.679** | **0.0074** | ** |
| **Education: high school or below (vs college)** | **+0.4824** | 0.0818 | ±0.1635 | **+5.900** | **3.64e-09** | *** |
| Site: UCSD (vs UAB) | +0.0403 | 0.0490 | ±0.0979 | +0.823 | 0.4103 |  |
| **Site: UW (vs UAB)** | **-0.3513** | 0.0503 | ±0.1006 | **-6.981** | **2.94e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1655** | 0.0531 | ±0.1062 | **-3.117** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0094 | 0.0564 | ±0.1129 | +0.167 | 0.8670 |  |
| Season: winter (vs autumn) | -0.0284 | 0.0564 | ±0.1129 | -0.503 | 0.6148 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.796** | **1.42e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.684** | **2.82e-06** | *** |
| **Hypertension** | **+0.1109** | 0.0421 | ±0.0843 | **+2.632** | **0.0085** | ** |
| High cholesterol | -0.0470 | 0.0393 | ±0.0786 | -1.196 | 0.2317 |  |
| Kidney disease | -0.0723 | 0.0583 | ±0.1166 | -1.239 | 0.2153 |  |
| Circulatory disease | +0.1135 | 0.0596 | ±0.1192 | +1.905 | 0.0568 | . |
| Avg. daily range (mg/dL) | +0.0007 | 0.0005 | ±0.0011 | +1.256 | 0.2092 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.1603**, Adj R² = **0.1547**, F-statistic = **28.43** (p = **2.55e-69**), Residual SE = **0.885** on **2085** df, AIC = **5461.8**, BIC = **5546.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4832** | 0.1621 | ±0.3243 | **+15.315** | **6.11e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1008** | 0.0398 | ±0.0796 | **-2.533** | **0.0113** | * |
| **Education: high school or below (vs college)** | **+0.4782** | 0.0808 | ±0.1616 | **+5.917** | **3.27e-09** | *** |
| Site: UCSD (vs UAB) | +0.0454 | 0.0487 | ±0.0974 | +0.933 | 0.3510 |  |
| **Site: UW (vs UAB)** | **-0.3458** | 0.0501 | ±0.1002 | **-6.905** | **5.03e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1680** | 0.0531 | ±0.1061 | **-3.167** | **0.0015** | ** |
| Season: summer (vs autumn) | +0.0043 | 0.0565 | ±0.1130 | +0.076 | 0.9395 |  |
| Season: winter (vs autumn) | -0.0322 | 0.0563 | ±0.1125 | -0.572 | 0.5674 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.758** | **1.98e-18** | *** |
| **BMI (kg/m2)** | **+0.0138** | 0.0031 | ±0.0063 | **+4.401** | **1.08e-05** | *** |
| **Hypertension** | **+0.1059** | 0.0419 | ±0.0838 | **+2.527** | **0.0115** | * |
| High cholesterol | -0.0503 | 0.0392 | ±0.0784 | -1.284 | 0.1990 |  |
| Kidney disease | -0.0797 | 0.0579 | ±0.1159 | -1.376 | 0.1690 |  |
| Circulatory disease | +0.1054 | 0.0595 | ±0.1191 | +1.770 | 0.0768 | . |
| **SD of daily means (mg/dL)** | **+0.0098** | 0.0036 | ±0.0072 | **+2.702** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.1584**, Adj R² = **0.1528**, F-statistic = **28.04** (p = **2.41e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.5**, BIC = **5551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7585** | 0.2060 | ±0.4120 | **+13.391** | **6.80e-41** | *** |
| **Education: graduate level (vs college)** | **-0.1048** | 0.0398 | ±0.0796 | **-2.634** | **0.0084** | ** |
| **Education: high school or below (vs college)** | **+0.4755** | 0.0810 | ±0.1621 | **+5.868** | **4.41e-09** | *** |
| Site: UCSD (vs UAB) | +0.0446 | 0.0489 | ±0.0979 | +0.912 | 0.3619 |  |
| **Site: UW (vs UAB)** | **-0.3484** | 0.0503 | ±0.1007 | **-6.923** | **4.42e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1650** | 0.0530 | ±0.1061 | **-3.111** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0109 | 0.0563 | ±0.1127 | +0.194 | 0.8464 |  |
| Season: winter (vs autumn) | -0.0290 | 0.0563 | ±0.1126 | -0.515 | 0.6063 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.817** | **1.18e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.490** | **7.12e-06** | *** |
| **Hypertension** | **+0.1092** | 0.0420 | ±0.0840 | **+2.600** | **0.0093** | ** |
| High cholesterol | -0.0488 | 0.0392 | ±0.0785 | -1.244 | 0.2135 |  |
| Kidney disease | -0.0753 | 0.0587 | ±0.1173 | -1.284 | 0.1993 |  |
| Circulatory disease | +0.1118 | 0.0596 | ±0.1191 | +1.877 | 0.0606 | . |
| Time in range 70-180, pooled (%) | -0.0022 | 0.0012 | ±0.0023 | -1.914 | 0.0556 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.1584**, Adj R² = **0.1528**, F-statistic = **28.03** (p = **2.45e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.5**, BIC = **5551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7584** | 0.2064 | ±0.4128 | **+13.365** | **9.73e-41** | *** |
| **Education: graduate level (vs college)** | **-0.1050** | 0.0398 | ±0.0796 | **-2.638** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.4754** | 0.0810 | ±0.1621 | **+5.868** | **4.42e-09** | *** |
| Site: UCSD (vs UAB) | +0.0447 | 0.0489 | ±0.0979 | +0.913 | 0.3610 |  |
| **Site: UW (vs UAB)** | **-0.3484** | 0.0503 | ±0.1007 | **-6.923** | **4.43e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1653** | 0.0530 | ±0.1061 | **-3.116** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0106 | 0.0563 | ±0.1126 | +0.189 | 0.8502 |  |
| Season: winter (vs autumn) | -0.0294 | 0.0563 | ±0.1126 | -0.522 | 0.6017 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.819** | **1.16e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.485** | **7.28e-06** | *** |
| **Hypertension** | **+0.1094** | 0.0420 | ±0.0840 | **+2.605** | **0.0092** | ** |
| High cholesterol | -0.0489 | 0.0392 | ±0.0785 | -1.246 | 0.2127 |  |
| Kidney disease | -0.0755 | 0.0586 | ±0.1172 | -1.288 | 0.1976 |  |
| Circulatory disease | +0.1118 | 0.0596 | ±0.1191 | +1.877 | 0.0605 | . |
| Avg. daily time in range 70-180 (%) | -0.0022 | 0.0012 | ±0.0023 | -1.907 | 0.0565 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.1568**, Adj R² = **0.1512**, F-statistic = **27.70** (p = **1.66e-67**), Residual SE = **0.887** on **2085** df, AIC = **5470.5**, BIC = **5555.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5139** | 0.1625 | ±0.3249 | **+15.473** | **5.28e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1084** | 0.0397 | ±0.0793 | **-2.732** | **0.0063** | ** |
| **Education: high school or below (vs college)** | **+0.4947** | 0.0819 | ±0.1638 | **+6.042** | **1.52e-09** | *** |
| Site: UCSD (vs UAB) | +0.0401 | 0.0491 | ±0.0982 | +0.817 | 0.4140 |  |
| **Site: UW (vs UAB)** | **-0.3523** | 0.0503 | ±0.1006 | **-7.007** | **2.43e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1662** | 0.0531 | ±0.1061 | **-3.133** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0094 | 0.0564 | ±0.1127 | +0.167 | 0.8673 |  |
| Season: winter (vs autumn) | -0.0287 | 0.0563 | ±0.1127 | -0.509 | 0.6106 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.643** | **5.47e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.663** | **3.11e-06** | *** |
| **Hypertension** | **+0.1155** | 0.0418 | ±0.0836 | **+2.762** | **0.0058** | ** |
| High cholesterol | -0.0426 | 0.0395 | ±0.0789 | -1.079 | 0.2804 |  |
| Kidney disease | -0.0577 | 0.0588 | ±0.1175 | -0.981 | 0.3265 |  |
| Circulatory disease | +0.1129 | 0.0593 | ±0.1186 | +1.905 | 0.0568 | . |
| Any reading < 54 during wear (0/1) | +0.0410 | 0.0456 | ±0.0912 | +0.899 | 0.3685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.1572**, Adj R² = **0.1515**, F-statistic = **27.78** (p = **1.05e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.6**, BIC = **5554.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5174** | 0.1639 | ±0.3279 | **+15.355** | **3.28e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1083** | 0.0397 | ±0.0793 | **-2.730** | **0.0063** | ** |
| **Education: high school or below (vs college)** | **+0.4952** | 0.0816 | ±0.1633 | **+6.066** | **1.31e-09** | *** |
| Site: UCSD (vs UAB) | +0.0431 | 0.0492 | ±0.0984 | +0.877 | 0.3807 |  |
| **Site: UW (vs UAB)** | **-0.3486** | 0.0504 | ±0.1009 | **-6.912** | **4.80e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0530 | ±0.1060 | **-3.115** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0077 | 0.0564 | ±0.1129 | +0.136 | 0.8915 |  |
| Season: winter (vs autumn) | -0.0300 | 0.0564 | ±0.1127 | -0.533 | 0.5939 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.669** | **4.35e-18** | *** |
| **BMI (kg/m2)** | **+0.0147** | 0.0031 | ±0.0062 | **+4.715** | **2.42e-06** | *** |
| **Hypertension** | **+0.1170** | 0.0419 | ±0.0838 | **+2.792** | **0.0052** | ** |
| High cholesterol | -0.0419 | 0.0396 | ±0.0792 | -1.059 | 0.2897 |  |
| Kidney disease | -0.0585 | 0.0586 | ±0.1173 | -0.998 | 0.3181 |  |
| Circulatory disease | +0.1142 | 0.0591 | ±0.1183 | +1.930 | 0.0535 | . |
| Time < 54 (%) | +0.0516 | 0.0538 | ±0.1076 | +0.960 | 0.3373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.1582**, Adj R² = **0.1526**, F-statistic = **27.99** (p = **3.04e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.0**, BIC = **5551.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5177** | 0.1631 | ±0.3262 | **+15.435** | **9.51e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1068** | 0.0396 | ±0.0793 | **-2.694** | **0.0070** | ** |
| **Education: high school or below (vs college)** | **+0.4971** | 0.0816 | ±0.1633 | **+6.090** | **1.13e-09** | *** |
| Site: UCSD (vs UAB) | +0.0456 | 0.0490 | ±0.0980 | +0.930 | 0.3523 |  |
| **Site: UW (vs UAB)** | **-0.3447** | 0.0505 | ±0.1009 | **-6.832** | **8.37e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1641** | 0.0530 | ±0.1060 | **-3.094** | **0.0020** | ** |
| Season: summer (vs autumn) | +0.0074 | 0.0564 | ±0.1128 | +0.131 | 0.8957 |  |
| Season: winter (vs autumn) | -0.0310 | 0.0563 | ±0.1126 | -0.550 | 0.5820 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.718** | **2.84e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.719** | **2.37e-06** | *** |
| **Hypertension** | **+0.1180** | 0.0420 | ±0.0839 | **+2.811** | **0.0049** | ** |
| High cholesterol | -0.0408 | 0.0395 | ±0.0789 | -1.033 | 0.3017 |  |
| Kidney disease | -0.0593 | 0.0585 | ±0.1170 | -1.013 | 0.3108 |  |
| Circulatory disease | +0.1132 | 0.0590 | ±0.1181 | +1.918 | 0.0552 | . |
| Avg. daily time < 54 (%) | +0.0953 | 0.0712 | ±0.1424 | +1.339 | 0.1806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.1591**, Adj R² = **0.1535**, F-statistic = **28.18** (p = **1.06e-68**), Residual SE = **0.886** on **2085** df, AIC = **5464.8**, BIC = **5549.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5043** | 0.1629 | ±0.3258 | **+15.373** | **2.50e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1045** | 0.0396 | ±0.0792 | **-2.638** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.4974** | 0.0818 | ±0.1636 | **+6.081** | **1.20e-09** | *** |
| Site: UCSD (vs UAB) | +0.0456 | 0.0490 | ±0.0980 | +0.929 | 0.3527 |  |
| **Site: UW (vs UAB)** | **-0.3448** | 0.0506 | ±0.1011 | **-6.819** | **9.17e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1643** | 0.0529 | ±0.1059 | **-3.105** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0092 | 0.0562 | ±0.1124 | +0.163 | 0.8702 |  |
| Season: winter (vs autumn) | -0.0313 | 0.0562 | ±0.1125 | -0.557 | 0.5778 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.691** | **3.59e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0062 | **+4.683** | **2.83e-06** | *** |
| **Hypertension** | **+0.1189** | 0.0420 | ±0.0839 | **+2.833** | **0.0046** | ** |
| High cholesterol | -0.0409 | 0.0393 | ±0.0787 | -1.040 | 0.2982 |  |
| Kidney disease | -0.0589 | 0.0585 | ±0.1171 | -1.006 | 0.3145 |  |
| Circulatory disease | +0.1141 | 0.0591 | ±0.1182 | +1.931 | 0.0535 | . |
| Time 54-69, pooled (%) | +0.0348 | 0.0191 | ±0.0382 | +1.826 | 0.0678 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.1594**, Adj R² = **0.1538**, F-statistic = **28.25** (p = **7.18e-69**), Residual SE = **0.886** on **2085** df, AIC = **5464.0**, BIC = **5548.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5103** | 0.1627 | ±0.3254 | **+15.427** | **1.08e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1036** | 0.0396 | ±0.0792 | **-2.617** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+0.4973** | 0.0818 | ±0.1636 | **+6.079** | **1.21e-09** | *** |
| Site: UCSD (vs UAB) | +0.0444 | 0.0490 | ±0.0979 | +0.907 | 0.3646 |  |
| **Site: UW (vs UAB)** | **-0.3442** | 0.0506 | ±0.1012 | **-6.801** | **1.04e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1643** | 0.0529 | ±0.1058 | **-3.106** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0094 | 0.0562 | ±0.1123 | +0.168 | 0.8665 |  |
| Season: winter (vs autumn) | -0.0322 | 0.0562 | ±0.1125 | -0.573 | 0.5667 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.731** | **2.52e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0062 | **+4.680** | **2.87e-06** | *** |
| **Hypertension** | **+0.1191** | 0.0420 | ±0.0839 | **+2.837** | **0.0046** | ** |
| High cholesterol | -0.0412 | 0.0393 | ±0.0786 | -1.047 | 0.2950 |  |
| Kidney disease | -0.0587 | 0.0584 | ±0.1169 | -1.004 | 0.3155 |  |
| Circulatory disease | +0.1145 | 0.0591 | ±0.1182 | +1.938 | 0.0527 | . |
| Avg. daily time 54-69 (%) | +0.0364 | 0.0195 | ±0.0389 | +1.871 | 0.0613 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.1589**, Adj R² = **0.1533**, F-statistic = **28.14** (p = **1.34e-68**), Residual SE = **0.886** on **2085** df, AIC = **5465.3**, BIC = **5550.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5019** | 0.1632 | ±0.3263 | **+15.333** | **4.62e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1051** | 0.0396 | ±0.0792 | **-2.653** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4983** | 0.0818 | ±0.1636 | **+6.090** | **1.13e-09** | *** |
| Site: UCSD (vs UAB) | +0.0474 | 0.0491 | ±0.0982 | +0.965 | 0.3347 |  |
| **Site: UW (vs UAB)** | **-0.3437** | 0.0506 | ±0.1012 | **-6.793** | **1.10e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1641** | 0.0529 | ±0.1059 | **-3.101** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0087 | 0.0563 | ±0.1125 | +0.154 | 0.8776 |  |
| Season: winter (vs autumn) | -0.0310 | 0.0562 | ±0.1125 | -0.551 | 0.5814 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.677** | **4.07e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.695** | **2.67e-06** | *** |
| **Hypertension** | **+0.1188** | 0.0420 | ±0.0839 | **+2.831** | **0.0046** | ** |
| High cholesterol | -0.0402 | 0.0394 | ±0.0788 | -1.020 | 0.3076 |  |
| Kidney disease | -0.0588 | 0.0585 | ±0.1171 | -1.004 | 0.3154 |  |
| Circulatory disease | +0.1136 | 0.0591 | ±0.1181 | +1.923 | 0.0545 | . |
| Time < 70 (%) | +0.0271 | 0.0152 | ±0.0304 | +1.779 | 0.0753 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.1596**, Adj R² = **0.1539**, F-statistic = **28.28** (p = **6.10e-69**), Residual SE = **0.885** on **2085** df, AIC = **5463.7**, BIC = **5548.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5083** | 0.1627 | ±0.3255 | **+15.412** | **1.35e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1037** | 0.0396 | ±0.0792 | **-2.619** | **0.0088** | ** |
| **Education: high school or below (vs college)** | **+0.4984** | 0.0818 | ±0.1636 | **+6.093** | **1.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0464 | 0.0490 | ±0.0979 | +0.947 | 0.3436 |  |
| **Site: UW (vs UAB)** | **-0.3424** | 0.0506 | ±0.1012 | **-6.765** | **1.33e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1639** | 0.0529 | ±0.1058 | **-3.097** | **0.0020** | ** |
| Season: summer (vs autumn) | +0.0090 | 0.0562 | ±0.1124 | +0.160 | 0.8731 |  |
| Season: winter (vs autumn) | -0.0322 | 0.0562 | ±0.1124 | -0.573 | 0.5669 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.730** | **2.55e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0062 | **+4.691** | **2.72e-06** | *** |
| **Hypertension** | **+0.1193** | 0.0420 | ±0.0840 | **+2.841** | **0.0045** | ** |
| High cholesterol | -0.0404 | 0.0393 | ±0.0787 | -1.026 | 0.3049 |  |
| Kidney disease | -0.0589 | 0.0584 | ±0.1168 | -1.008 | 0.3135 |  |
| Circulatory disease | +0.1138 | 0.0590 | ±0.1181 | +1.928 | 0.0539 | . |
| Avg. daily time < 70 (%) | +0.0310 | 0.0163 | ±0.0326 | +1.905 | 0.0568 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1583**, Adj R² = **0.1527**, F-statistic = **28.01** (p = **2.76e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.8**, BIC = **5551.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9112** | 0.2838 | ±0.5676 | **+10.258** | **1.09e-24** | *** |
| **Education: graduate level (vs college)** | **-0.1043** | 0.0399 | ±0.0798 | **-2.612** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+0.4773** | 0.0806 | ±0.1612 | **+5.923** | **3.16e-09** | *** |
| Site: UCSD (vs UAB) | +0.0426 | 0.0489 | ±0.0978 | +0.872 | 0.3833 |  |
| **Site: UW (vs UAB)** | **-0.3475** | 0.0503 | ±0.1005 | **-6.913** | **4.76e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1649** | 0.0531 | ±0.1062 | **-3.106** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0142 | 0.0564 | ±0.1127 | +0.252 | 0.8007 |  |
| Season: winter (vs autumn) | -0.0291 | 0.0563 | ±0.1127 | -0.516 | 0.6059 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.690** | **3.61e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.585** | **4.53e-06** | *** |
| **Hypertension** | **+0.1112** | 0.0418 | ±0.0837 | **+2.656** | **0.0079** | ** |
| High cholesterol | -0.0460 | 0.0393 | ±0.0786 | -1.172 | 0.2411 |  |
| Kidney disease | -0.0689 | 0.0588 | ±0.1177 | -1.171 | 0.2414 |  |
| Circulatory disease | +0.1120 | 0.0596 | ±0.1191 | +1.880 | 0.0601 | . |
| Time 54-250, pooled (%) | -0.0039 | 0.0023 | ±0.0047 | -1.645 | 0.1000 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1583**, Adj R² = **0.1527**, F-statistic = **28.02** (p = **2.67e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.7**, BIC = **5551.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9211** | 0.2867 | ±0.5734 | **+10.189** | **2.23e-24** | *** |
| **Education: graduate level (vs college)** | **-0.1043** | 0.0399 | ±0.0798 | **-2.612** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+0.4772** | 0.0806 | ±0.1612 | **+5.921** | **3.19e-09** | *** |
| Site: UCSD (vs UAB) | +0.0426 | 0.0489 | ±0.0978 | +0.872 | 0.3833 |  |
| **Site: UW (vs UAB)** | **-0.3476** | 0.0503 | ±0.1005 | **-6.917** | **4.61e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0531 | ±0.1062 | **-3.111** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0139 | 0.0563 | ±0.1127 | +0.247 | 0.8049 |  |
| Season: winter (vs autumn) | -0.0293 | 0.0563 | ±0.1127 | -0.520 | 0.6028 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.703** | **3.22e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.581** | **4.62e-06** | *** |
| **Hypertension** | **+0.1113** | 0.0418 | ±0.0837 | **+2.660** | **0.0078** | ** |
| High cholesterol | -0.0461 | 0.0393 | ±0.0786 | -1.173 | 0.2408 |  |
| Kidney disease | -0.0695 | 0.0588 | ±0.1176 | -1.181 | 0.2375 |  |
| Circulatory disease | +0.1117 | 0.0596 | ±0.1192 | +1.874 | 0.0609 | . |
| Avg. daily time 54-250 (%) | -0.0039 | 0.0024 | ±0.0047 | -1.661 | 0.0967 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.1571**, Adj R² = **0.1515**, F-statistic = **27.76** (p = **1.14e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.7**, BIC = **5554.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5441** | 0.1639 | ±0.3278 | **+15.522** | **2.45e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1081** | 0.0397 | ±0.0794 | **-2.721** | **0.0065** | ** |
| **Education: high school or below (vs college)** | **+0.4834** | 0.0819 | ±0.1638 | **+5.901** | **3.60e-09** | *** |
| Site: UCSD (vs UAB) | +0.0394 | 0.0490 | ±0.0981 | +0.803 | 0.4217 |  |
| **Site: UW (vs UAB)** | **-0.3535** | 0.0504 | ±0.1009 | **-7.009** | **2.40e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1660** | 0.0530 | ±0.1061 | **-3.130** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0075 | 0.0565 | ±0.1129 | +0.134 | 0.8936 |  |
| Season: winter (vs autumn) | -0.0296 | 0.0564 | ±0.1128 | -0.525 | 0.5997 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0037 | **-8.773** | **1.74e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.564** | **5.02e-06** | *** |
| **Hypertension** | **+0.1121** | 0.0422 | ±0.0843 | **+2.658** | **0.0079** | ** |
| High cholesterol | -0.0482 | 0.0393 | ±0.0787 | -1.225 | 0.2208 |  |
| Kidney disease | -0.0685 | 0.0585 | ±0.1171 | -1.171 | 0.2418 |  |
| Circulatory disease | +0.1143 | 0.0594 | ±0.1188 | +1.924 | 0.0544 | . |
| Time 181-250, pooled (%) | +0.0020 | 0.0017 | ±0.0033 | +1.221 | 0.2221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1571**, Adj R² = **0.1514**, F-statistic = **27.76** (p = **1.18e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.8**, BIC = **5554.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5438** | 0.1639 | ±0.3278 | **+15.518** | **2.61e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1082** | 0.0397 | ±0.0794 | **-2.724** | **0.0064** | ** |
| **Education: high school or below (vs college)** | **+0.4834** | 0.0819 | ±0.1638 | **+5.903** | **3.56e-09** | *** |
| Site: UCSD (vs UAB) | +0.0396 | 0.0490 | ±0.0981 | +0.807 | 0.4197 |  |
| **Site: UW (vs UAB)** | **-0.3534** | 0.0504 | ±0.1009 | **-7.006** | **2.45e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1662** | 0.0530 | ±0.1061 | **-3.132** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0075 | 0.0565 | ±0.1129 | +0.134 | 0.8937 |  |
| Season: winter (vs autumn) | -0.0297 | 0.0564 | ±0.1128 | -0.528 | 0.5978 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0037 | **-8.769** | **1.80e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.562** | **5.08e-06** | *** |
| **Hypertension** | **+0.1122** | 0.0422 | ±0.0843 | **+2.661** | **0.0078** | ** |
| High cholesterol | -0.0481 | 0.0393 | ±0.0787 | -1.224 | 0.2209 |  |
| Kidney disease | -0.0684 | 0.0585 | ±0.1170 | -1.168 | 0.2426 |  |
| Circulatory disease | +0.1144 | 0.0594 | ±0.1188 | +1.926 | 0.0541 | . |
| Avg. daily time 181-250 (%) | +0.0020 | 0.0016 | ±0.0033 | +1.200 | 0.2302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.1580**, Adj R² = **0.1524**, F-statistic = **27.95** (p = **3.94e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.5**, BIC = **5552.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5393** | 0.1634 | ±0.3269 | **+15.536** | **1.97e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1056** | 0.0398 | ±0.0796 | **-2.654** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4768** | 0.0811 | ±0.1622 | **+5.878** | **4.14e-09** | *** |
| Site: UCSD (vs UAB) | +0.0427 | 0.0490 | ±0.0979 | +0.871 | 0.3836 |  |
| **Site: UW (vs UAB)** | **-0.3500** | 0.0503 | ±0.1007 | **-6.952** | **3.60e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1653** | 0.0531 | ±0.1061 | **-3.116** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0106 | 0.0564 | ±0.1127 | +0.188 | 0.8511 |  |
| Season: winter (vs autumn) | -0.0291 | 0.0563 | ±0.1127 | -0.516 | 0.6057 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.803** | **1.33e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.515** | **6.34e-06** | *** |
| **Hypertension** | **+0.1098** | 0.0421 | ±0.0841 | **+2.610** | **0.0090** | ** |
| High cholesterol | -0.0487 | 0.0392 | ±0.0785 | -1.241 | 0.2147 |  |
| Kidney disease | -0.0733 | 0.0587 | ±0.1174 | -1.249 | 0.2115 |  |
| Circulatory disease | +0.1124 | 0.0596 | ±0.1191 | +1.887 | 0.0591 | . |
| Time > 180 (%) | +0.0020 | 0.0012 | ±0.0023 | +1.697 | 0.0898 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.1580**, Adj R² = **0.1523**, F-statistic = **27.94** (p = **4.15e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.6**, BIC = **5552.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5400** | 0.1635 | ±0.3270 | **+15.535** | **2.00e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1058** | 0.0398 | ±0.0796 | **-2.660** | **0.0078** | ** |
| **Education: high school or below (vs college)** | **+0.4769** | 0.0811 | ±0.1622 | **+5.880** | **4.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0428 | 0.0490 | ±0.0979 | +0.875 | 0.3816 |  |
| **Site: UW (vs UAB)** | **-0.3500** | 0.0503 | ±0.1007 | **-6.953** | **3.59e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1656** | 0.0531 | ±0.1061 | **-3.121** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0103 | 0.0564 | ±0.1127 | +0.183 | 0.8549 |  |
| Season: winter (vs autumn) | -0.0294 | 0.0563 | ±0.1127 | -0.521 | 0.6024 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.802** | **1.35e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.512** | **6.43e-06** | *** |
| **Hypertension** | **+0.1100** | 0.0421 | ±0.0841 | **+2.615** | **0.0089** | ** |
| High cholesterol | -0.0487 | 0.0392 | ±0.0785 | -1.241 | 0.2148 |  |
| Kidney disease | -0.0734 | 0.0587 | ±0.1173 | -1.251 | 0.2108 |  |
| Circulatory disease | +0.1124 | 0.0596 | ±0.1191 | +1.887 | 0.0591 | . |
| Avg. daily time > 180 (%) | +0.0019 | 0.0011 | ±0.0023 | +1.672 | 0.0944 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.1586**, Adj R² = **0.1530**, F-statistic = **28.08** (p = **1.87e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.0**, BIC = **5550.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5418** | 0.1636 | ±0.3271 | **+15.539** | **1.89e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1034** | 0.0398 | ±0.0797 | **-2.596** | **0.0094** | ** |
| **Education: high school or below (vs college)** | **+0.4754** | 0.0809 | ±0.1618 | **+5.875** | **4.22e-09** | *** |
| Site: UCSD (vs UAB) | +0.0441 | 0.0489 | ±0.0978 | +0.901 | 0.3674 |  |
| **Site: UW (vs UAB)** | **-0.3498** | 0.0503 | ±0.1006 | **-6.955** | **3.52e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1671** | 0.0531 | ±0.1061 | **-3.149** | **0.0016** | ** |
| Season: summer (vs autumn) | +0.0113 | 0.0563 | ±0.1126 | +0.200 | 0.8414 |  |
| Season: winter (vs autumn) | -0.0310 | 0.0563 | ±0.1126 | -0.550 | 0.5826 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.753** | **2.07e-18** | *** |
| **BMI (kg/m2)** | **+0.0139** | 0.0032 | ±0.0064 | **+4.378** | **1.20e-05** | *** |
| **Hypertension** | **+0.1111** | 0.0419 | ±0.0838 | **+2.650** | **0.0080** | ** |
| High cholesterol | -0.0487 | 0.0392 | ±0.0784 | -1.241 | 0.2147 |  |
| Kidney disease | -0.0719 | 0.0584 | ±0.1169 | -1.230 | 0.2185 |  |
| Circulatory disease | +0.1124 | 0.0595 | ±0.1190 | +1.890 | 0.0588 | . |
| **Nocturnal time > 180 (%)** | **+0.0023** | 0.0012 | ±0.0023 | **+1.979** | **0.0478** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1565**, Adj R² = **0.1508**, F-statistic = **27.63** (p = **2.45e-67**), Residual SE = **0.887** on **2085** df, AIC = **5471.3**, BIC = **5556.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5336** | 0.1633 | ±0.3266 | **+15.513** | **2.84e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1085** | 0.0398 | ±0.0796 | **-2.725** | **0.0064** | ** |
| **Education: high school or below (vs college)** | **+0.4896** | 0.0818 | ±0.1636 | **+5.986** | **2.15e-09** | *** |
| Site: UCSD (vs UAB) | +0.0360 | 0.0490 | ±0.0980 | +0.735 | 0.4625 |  |
| **Site: UW (vs UAB)** | **-0.3547** | 0.0504 | ±0.1008 | **-7.037** | **1.97e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1656** | 0.0531 | ±0.1062 | **-3.119** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0084 | 0.0565 | ±0.1129 | +0.149 | 0.8812 |  |
| Season: winter (vs autumn) | -0.0293 | 0.0565 | ±0.1130 | -0.519 | 0.6035 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.713** | **2.95e-18** | *** |
| **BMI (kg/m2)** | **+0.0147** | 0.0031 | ±0.0062 | **+4.709** | **2.49e-06** | *** |
| **Hypertension** | **+0.1146** | 0.0423 | ±0.0846 | **+2.711** | **0.0067** | ** |
| High cholesterol | -0.0458 | 0.0393 | ±0.0787 | -1.164 | 0.2444 |  |
| Kidney disease | -0.0607 | 0.0587 | ±0.1174 | -1.034 | 0.3011 |  |
| Circulatory disease | +0.1159 | 0.0593 | ±0.1186 | +1.954 | 0.0507 | . |
| Any reading > 250 during wear (0/1) | +0.0134 | 0.0419 | ±0.0838 | +0.321 | 0.7484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.1582**, Adj R² = **0.1525**, F-statistic = **27.99** (p = **3.17e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.1**, BIC = **5551.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5265** | 0.1635 | ±0.3269 | **+15.456** | **6.85e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1045** | 0.0399 | ±0.0799 | **-2.617** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+0.4774** | 0.0806 | ±0.1611 | **+5.926** | **3.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0419 | 0.0489 | ±0.0978 | +0.855 | 0.3923 |  |
| **Site: UW (vs UAB)** | **-0.3482** | 0.0503 | ±0.1005 | **-6.925** | **4.35e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1650** | 0.0531 | ±0.1062 | **-3.109** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0141 | 0.0564 | ±0.1127 | +0.250 | 0.8027 |  |
| Season: winter (vs autumn) | -0.0291 | 0.0564 | ±0.1127 | -0.517 | 0.6055 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.694** | **3.50e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.588** | **4.48e-06** | *** |
| **Hypertension** | **+0.1112** | 0.0419 | ±0.0837 | **+2.657** | **0.0079** | ** |
| High cholesterol | -0.0462 | 0.0393 | ±0.0786 | -1.177 | 0.2391 |  |
| Kidney disease | -0.0686 | 0.0588 | ±0.1177 | -1.166 | 0.2437 |  |
| Circulatory disease | +0.1122 | 0.0596 | ±0.1192 | +1.884 | 0.0596 | . |
| Time > 250 (%) | +0.0037 | 0.0023 | ±0.0047 | +1.592 | 0.1114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1582**, Adj R² = **0.1525**, F-statistic = **27.99** (p = **3.18e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.1**, BIC = **5551.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5280** | 0.1635 | ±0.3270 | **+15.464** | **6.06e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1046** | 0.0399 | ±0.0798 | **-2.619** | **0.0088** | ** |
| **Education: high school or below (vs college)** | **+0.4775** | 0.0806 | ±0.1611 | **+5.926** | **3.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0419 | 0.0489 | ±0.0978 | +0.857 | 0.3912 |  |
| **Site: UW (vs UAB)** | **-0.3483** | 0.0503 | ±0.1005 | **-6.930** | **4.22e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1653** | 0.0531 | ±0.1062 | **-3.114** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0137 | 0.0564 | ±0.1127 | +0.244 | 0.8074 |  |
| Season: winter (vs autumn) | -0.0293 | 0.0564 | ±0.1127 | -0.520 | 0.6029 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.703** | **3.22e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.585** | **4.54e-06** | *** |
| **Hypertension** | **+0.1114** | 0.0419 | ±0.0837 | **+2.662** | **0.0078** | ** |
| High cholesterol | -0.0462 | 0.0393 | ±0.0786 | -1.176 | 0.2395 |  |
| Kidney disease | -0.0690 | 0.0588 | ±0.1176 | -1.173 | 0.2407 |  |
| Circulatory disease | +0.1120 | 0.0596 | ±0.1192 | +1.879 | 0.0603 | . |
| Avg. daily time > 250 (%) | +0.0038 | 0.0024 | ±0.0047 | +1.594 | 0.1109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2982**, F-statistic = **69.61** (p = **1.22e-152**), Residual SE = **1.986** on **2086** df, AIC = **8854.6**, BIC = **8933.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9397** | 0.3610 | ±0.7219 | **+66.323** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1210 | 0.0921 | ±0.1842 | -1.314 | 0.1888 |  |
| Education: high school or below (vs college) | +0.1977 | 0.1564 | ±0.3127 | +1.264 | 0.2062 |  |
| Site: UCSD (vs UAB) | -0.1209 | 0.1103 | ±0.2207 | -1.096 | 0.2731 |  |
| **Site: UW (vs UAB)** | **-1.1222** | 0.1075 | ±0.2149 | **-10.444** | **1.56e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3635** | 0.1199 | ±0.2397 | **-3.033** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1384 | ±0.2768 | **+13.677** | **1.38e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3136** | 0.1231 | ±0.2463 | **-10.668** | **1.44e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.501** | **0.0124** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.595 | 0.1106 |  |
| **Hypertension** | **+0.2913** | 0.0962 | ±0.1923 | **+3.030** | **0.0024** | ** |
| High cholesterol | -0.0858 | 0.0920 | ±0.1840 | -0.933 | 0.3509 |  |
| Kidney disease | +0.1246 | 0.1379 | ±0.2758 | +0.903 | 0.3664 |  |
| **Circulatory disease** | **+0.2754** | 0.1290 | ±0.2579 | **+2.136** | **0.0327** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.65** (p = **8.18e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.1**, BIC = **8940.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7855** | 0.4509 | ±0.9018 | **+52.751** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1175 | 0.0924 | ±0.1849 | -1.271 | 0.2039 |  |
| Education: high school or below (vs college) | +0.1853 | 0.1576 | ±0.3151 | +1.176 | 0.2397 |  |
| Site: UCSD (vs UAB) | -0.1177 | 0.1108 | ±0.2215 | -1.062 | 0.2881 |  |
| **Site: UW (vs UAB)** | **-1.1183** | 0.1077 | ±0.2154 | **-10.383** | **2.95e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3594** | 0.1205 | ±0.2411 | **-2.981** | **0.0029** | ** |
| **Season: summer (vs autumn)** | **+1.8943** | 0.1386 | ±0.2772 | **+13.668** | **1.57e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3116** | 0.1232 | ±0.2463 | **-10.649** | **1.76e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.451** | **0.0143** | * |
| BMI (kg/m2) | +0.0099 | 0.0067 | ±0.0133 | +1.491 | 0.1361 |  |
| **Hypertension** | **+0.2850** | 0.0960 | ±0.1921 | **+2.968** | **0.0030** | ** |
| High cholesterol | -0.0914 | 0.0929 | ±0.1858 | -0.984 | 0.3251 |  |
| Kidney disease | +0.1192 | 0.1383 | ±0.2767 | +0.861 | 0.3891 |  |
| **Circulatory disease** | **+0.2727** | 0.1293 | ±0.2587 | **+2.108** | **0.0350** | * |
| HbA1c (%) | +0.0300 | 0.0548 | ±0.1096 | +0.548 | 0.5840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.00e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9020** | 0.3893 | ±0.7786 | **+61.400** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1202 | 0.0922 | ±0.1843 | -1.304 | 0.1921 |  |
| Education: high school or below (vs college) | +0.1935 | 0.1574 | ±0.3148 | +1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | -0.1192 | 0.1108 | ±0.2215 | -1.076 | 0.2818 |  |
| **Site: UW (vs UAB)** | **-1.1213** | 0.1077 | ±0.2155 | **-10.407** | **2.30e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3632** | 0.1200 | ±0.2399 | **-3.028** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8933** | 0.1385 | ±0.2771 | **+13.666** | **1.61e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2463 | **-10.662** | **1.53e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.479** | **0.0132** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.565 | 0.1177 |  |
| **Hypertension** | **+0.2890** | 0.0958 | ±0.1917 | **+3.015** | **0.0026** | ** |
| High cholesterol | -0.0872 | 0.0920 | ±0.1840 | -0.948 | 0.3432 |  |
| Kidney disease | +0.1207 | 0.1384 | ±0.2767 | +0.872 | 0.3829 |  |
| **Circulatory disease** | **+0.2744** | 0.1292 | ±0.2585 | **+2.123** | **0.0337** | * |
| Mean glucose (mg/dL) | +0.0003 | 0.0014 | ±0.0028 | +0.244 | 0.8073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.00e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8543** | 0.4968 | ±0.9937 | **+48.013** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1202 | 0.0922 | ±0.1843 | -1.304 | 0.1921 |  |
| Education: high school or below (vs college) | +0.1935 | 0.1574 | ±0.3148 | +1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | -0.1192 | 0.1108 | ±0.2215 | -1.076 | 0.2818 |  |
| **Site: UW (vs UAB)** | **-1.1213** | 0.1077 | ±0.2155 | **-10.407** | **2.30e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3632** | 0.1200 | ±0.2399 | **-3.028** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8933** | 0.1385 | ±0.2771 | **+13.666** | **1.61e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2463 | **-10.662** | **1.53e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.479** | **0.0132** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.565 | 0.1177 |  |
| **Hypertension** | **+0.2890** | 0.0958 | ±0.1917 | **+3.015** | **0.0026** | ** |
| High cholesterol | -0.0872 | 0.0920 | ±0.1840 | -0.948 | 0.3432 |  |
| Kidney disease | +0.1207 | 0.1384 | ±0.2767 | +0.872 | 0.3829 |  |
| **Circulatory disease** | **+0.2744** | 0.1292 | ±0.2585 | **+2.123** | **0.0337** | * |
| GMI (%) | +0.0144 | 0.0591 | ±0.1181 | +0.244 | 0.8073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.04e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9361** | 0.3887 | ±0.7775 | **+61.574** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1209 | 0.0922 | ±0.1844 | -1.311 | 0.1898 |  |
| Education: high school or below (vs college) | +0.1973 | 0.1573 | ±0.3145 | +1.255 | 0.2097 |  |
| Site: UCSD (vs UAB) | -0.1208 | 0.1106 | ±0.2213 | -1.092 | 0.2749 |  |
| **Site: UW (vs UAB)** | **-1.1222** | 0.1077 | ±0.2154 | **-10.422** | **1.97e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3635** | 0.1199 | ±0.2398 | **-3.031** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8927** | 0.1385 | ±0.2770 | **+13.664** | **1.66e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3136** | 0.1232 | ±0.2464 | **-10.662** | **1.53e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.500** | **0.0124** | * |
| BMI (kg/m2) | +0.0105 | 0.0067 | ±0.0134 | +1.566 | 0.1174 |  |
| **Hypertension** | **+0.2912** | 0.0958 | ±0.1916 | **+3.039** | **0.0024** | ** |
| High cholesterol | -0.0860 | 0.0920 | ±0.1841 | -0.934 | 0.3503 |  |
| Kidney disease | +0.1243 | 0.1379 | ±0.2759 | +0.901 | 0.3675 |  |
| **Circulatory disease** | **+0.2753** | 0.1292 | ±0.2584 | **+2.131** | **0.0331** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0000 | 0.0014 | ±0.0028 | +0.023 | 0.9817 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.01e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9237** | 0.3680 | ±0.7359 | **+65.016** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1197 | 0.0923 | ±0.1845 | -1.298 | 0.1943 |  |
| Education: high school or below (vs college) | +0.1942 | 0.1572 | ±0.3145 | +1.235 | 0.2169 |  |
| Site: UCSD (vs UAB) | -0.1188 | 0.1108 | ±0.2216 | -1.072 | 0.2835 |  |
| **Site: UW (vs UAB)** | **-1.1205** | 0.1079 | ±0.2157 | **-10.390** | **2.76e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3631** | 0.1200 | ±0.2400 | **-3.026** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8931** | 0.1385 | ±0.2771 | **+13.665** | **1.65e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3131** | 0.1233 | ±0.2465 | **-10.654** | **1.68e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.467** | **0.0136** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.578 | 0.1146 |  |
| **Hypertension** | **+0.2888** | 0.0964 | ±0.1927 | **+2.997** | **0.0027** | ** |
| High cholesterol | -0.0868 | 0.0921 | ±0.1841 | -0.943 | 0.3459 |  |
| Kidney disease | +0.1186 | 0.1403 | ±0.2805 | +0.845 | 0.3979 |  |
| **Circulatory disease** | **+0.2743** | 0.1291 | ±0.2582 | **+2.125** | **0.0336** | * |
| Glucose SD, pooled (mg/dL) | +0.0009 | 0.0041 | ±0.0082 | +0.226 | 0.8211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.04e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9377** | 0.3683 | ±0.7366 | **+64.992** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1209 | 0.0923 | ±0.1846 | -1.310 | 0.1903 |  |
| Education: high school or below (vs college) | +0.1972 | 0.1571 | ±0.3143 | +1.255 | 0.2094 |  |
| Site: UCSD (vs UAB) | -0.1207 | 0.1107 | ±0.2213 | -1.090 | 0.2755 |  |
| **Site: UW (vs UAB)** | **-1.1221** | 0.1077 | ±0.2154 | **-10.417** | **2.06e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3634** | 0.1200 | ±0.2399 | **-3.029** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8927** | 0.1386 | ±0.2771 | **+13.660** | **1.75e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3135** | 0.1232 | ±0.2465 | **-10.660** | **1.57e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.485** | **0.0130** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0132 | +1.591 | 0.1116 |  |
| **Hypertension** | **+0.2910** | 0.0965 | ±0.1929 | **+3.017** | **0.0026** | ** |
| High cholesterol | -0.0859 | 0.0920 | ±0.1840 | -0.934 | 0.3503 |  |
| Kidney disease | +0.1238 | 0.1401 | ±0.2802 | +0.884 | 0.3767 |  |
| **Circulatory disease** | **+0.2753** | 0.1291 | ±0.2582 | **+2.133** | **0.0329** | * |
| Avg. daily SD (mg/dL) | +0.0001 | 0.0045 | ±0.0089 | +0.028 | 0.9779 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **9.89e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8981** | 0.3896 | ±0.7791 | **+61.346** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1194 | 0.0922 | ±0.1844 | -1.295 | 0.1952 |  |
| Education: high school or below (vs college) | +0.1953 | 0.1567 | ±0.3133 | +1.246 | 0.2126 |  |
| Site: UCSD (vs UAB) | -0.1184 | 0.1105 | ±0.2210 | -1.071 | 0.2840 |  |
| **Site: UW (vs UAB)** | **-1.1200** | 0.1076 | ±0.2152 | **-10.408** | **2.28e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3628** | 0.1200 | ±0.2400 | **-3.023** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1385 | ±0.2769 | **+13.669** | **1.55e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3132** | 0.1233 | ±0.2466 | **-10.652** | **1.72e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.464** | **0.0137** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0131 | +1.590 | 0.1118 |  |
| **Hypertension** | **+0.2887** | 0.0967 | ±0.1935 | **+2.984** | **0.0028** | ** |
| High cholesterol | -0.0861 | 0.0921 | ±0.1841 | -0.936 | 0.3494 |  |
| Kidney disease | +0.1175 | 0.1404 | ±0.2808 | +0.837 | 0.4027 |  |
| **Circulatory disease** | **+0.2744** | 0.1290 | ±0.2579 | **+2.128** | **0.0334** | * |
| CV (%) | +0.0026 | 0.0086 | ±0.0171 | +0.301 | 0.7633 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.03e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9643** | 0.4125 | ±0.8250 | **+58.096** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1204 | 0.0922 | ±0.1845 | -1.305 | 0.1918 |  |
| Education: high school or below (vs college) | +0.1967 | 0.1564 | ±0.3129 | +1.257 | 0.2087 |  |
| Site: UCSD (vs UAB) | -0.1201 | 0.1104 | ±0.2208 | -1.088 | 0.2768 |  |
| **Site: UW (vs UAB)** | **-1.1216** | 0.1075 | ±0.2149 | **-10.437** | **1.69e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3634** | 0.1200 | ±0.2399 | **-3.029** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8925** | 0.1384 | ±0.2769 | **+13.671** | **1.50e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3136** | 0.1232 | ±0.2464 | **-10.661** | **1.54e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.485** | **0.0130** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.593 | 0.1112 |  |
| **Hypertension** | **+0.2903** | 0.0966 | ±0.1933 | **+3.004** | **0.0027** | ** |
| High cholesterol | -0.0860 | 0.0921 | ±0.1842 | -0.934 | 0.3502 |  |
| Kidney disease | +0.1225 | 0.1395 | ±0.2790 | +0.878 | 0.3799 |  |
| **Circulatory disease** | **+0.2750** | 0.1290 | ±0.2579 | **+2.133** | **0.0330** | * |
| Mean / SD ratio | -0.0039 | 0.0331 | ±0.0662 | -0.116 | 0.9074 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.03e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9217** | 0.4124 | ±0.8248 | **+58.005** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1214 | 0.0924 | ±0.1847 | -1.314 | 0.1888 |  |
| Education: high school or below (vs college) | +0.1984 | 0.1564 | ±0.3127 | +1.269 | 0.2045 |  |
| Site: UCSD (vs UAB) | -0.1214 | 0.1103 | ±0.2207 | -1.100 | 0.2714 |  |
| **Site: UW (vs UAB)** | **-1.1226** | 0.1074 | ±0.2147 | **-10.455** | **1.38e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1200 | ±0.2400 | **-3.030** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1385 | ±0.2770 | **+13.666** | **1.62e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3137** | 0.1232 | ±0.2465 | **-10.659** | **1.58e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.504** | **0.0123** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.596 | 0.1105 |  |
| **Hypertension** | **+0.2920** | 0.0966 | ±0.1933 | **+3.021** | **0.0025** | ** |
| High cholesterol | -0.0857 | 0.0921 | ±0.1842 | -0.931 | 0.3519 |  |
| Kidney disease | +0.1260 | 0.1394 | ±0.2788 | +0.904 | 0.3660 |  |
| **Circulatory disease** | **+0.2755** | 0.1290 | ±0.2580 | **+2.136** | **0.0327** | * |
| Avg. daily mean/SD | +0.0024 | 0.0284 | ±0.0568 | +0.084 | 0.9331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.03e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9667** | 0.4138 | ±0.8276 | **+57.915** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1217 | 0.0924 | ±0.1847 | -1.318 | 0.1876 |  |
| Education: high school or below (vs college) | +0.1989 | 0.1565 | ±0.3130 | +1.271 | 0.2038 |  |
| Site: UCSD (vs UAB) | -0.1220 | 0.1105 | ±0.2210 | -1.104 | 0.2696 |  |
| **Site: UW (vs UAB)** | **-1.1238** | 0.1080 | ±0.2160 | **-10.408** | **2.28e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1200 | ±0.2400 | **-3.031** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8920** | 0.1387 | ±0.2774 | **+13.641** | **2.29e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3141** | 0.1233 | ±0.2466 | **-10.659** | **1.58e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.499** | **0.0125** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0132 | +1.596 | 0.1104 |  |
| **Hypertension** | **+0.2917** | 0.0961 | ±0.1922 | **+3.035** | **0.0024** | ** |
| High cholesterol | -0.0859 | 0.0921 | ±0.1841 | -0.933 | 0.3506 |  |
| Kidney disease | +0.1262 | 0.1389 | ±0.2779 | +0.908 | 0.3636 |  |
| **Circulatory disease** | **+0.2756** | 0.1290 | ±0.2580 | **+2.137** | **0.0326** | * |
| MAG (mg/dL/h) | -0.0007 | 0.0051 | ±0.0102 | -0.129 | 0.8972 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.04e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9422** | 0.3772 | ±0.7545 | **+63.469** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1211 | 0.0922 | ±0.1844 | -1.313 | 0.1891 |  |
| Education: high school or below (vs college) | +0.1980 | 0.1570 | ±0.3139 | +1.262 | 0.2071 |  |
| Site: UCSD (vs UAB) | -0.1211 | 0.1106 | ±0.2212 | -1.095 | 0.2734 |  |
| **Site: UW (vs UAB)** | **-1.1224** | 0.1077 | ±0.2153 | **-10.424** | **1.93e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3635** | 0.1200 | ±0.2399 | **-3.031** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1385 | ±0.2770 | **+13.665** | **1.65e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3137** | 0.1232 | ±0.2464 | **-10.663** | **1.52e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.492** | **0.0127** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.594 | 0.1109 |  |
| **Hypertension** | **+0.2915** | 0.0964 | ±0.1928 | **+3.025** | **0.0025** | ** |
| High cholesterol | -0.0857 | 0.0920 | ±0.1840 | -0.932 | 0.3512 |  |
| Kidney disease | +0.1251 | 0.1401 | ±0.2803 | +0.893 | 0.3719 |  |
| **Circulatory disease** | **+0.2755** | 0.1291 | ±0.2581 | **+2.135** | **0.0328** | * |
| Avg. daily range (mg/dL) | -0.0000 | 0.0012 | ±0.0024 | -0.024 | 0.9811 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.64** (p = **8.67e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9171** | 0.3635 | ±0.7270 | **+65.796** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1173 | 0.0921 | ±0.1843 | -1.273 | 0.2030 |  |
| Education: high school or below (vs college) | +0.1922 | 0.1571 | ±0.3142 | +1.224 | 0.2211 |  |
| Site: UCSD (vs UAB) | -0.1165 | 0.1111 | ±0.2221 | -1.049 | 0.2941 |  |
| **Site: UW (vs UAB)** | **-1.1182** | 0.1082 | ±0.2165 | **-10.332** | **5.04e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3642** | 0.1200 | ±0.2401 | **-3.034** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8909** | 0.1385 | ±0.2769 | **+13.657** | **1.84e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3145** | 0.1232 | ±0.2464 | **-10.669** | **1.42e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.491** | **0.0127** | * |
| BMI (kg/m2) | +0.0101 | 0.0066 | ±0.0132 | +1.531 | 0.1258 |  |
| **Hypertension** | **+0.2870** | 0.0963 | ±0.1925 | **+2.981** | **0.0029** | ** |
| High cholesterol | -0.0882 | 0.0921 | ±0.1841 | -0.958 | 0.3383 |  |
| Kidney disease | +0.1154 | 0.1393 | ±0.2785 | +0.829 | 0.4073 |  |
| **Circulatory disease** | **+0.2708** | 0.1291 | ±0.2581 | **+2.098** | **0.0359** | * |
| SD of daily means (mg/dL) | +0.0043 | 0.0086 | ±0.0171 | +0.497 | 0.6193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.64** (p = **8.77e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0712** | 0.4384 | ±0.8769 | **+54.904** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1184 | 0.0922 | ±0.1844 | -1.284 | 0.1991 |  |
| Education: high school or below (vs college) | +0.1888 | 0.1576 | ±0.3153 | +1.197 | 0.2312 |  |
| Site: UCSD (vs UAB) | -0.1154 | 0.1110 | ±0.2219 | -1.040 | 0.2982 |  |
| **Site: UW (vs UAB)** | **-1.1184** | 0.1080 | ±0.2160 | **-10.357** | **3.87e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3627** | 0.1200 | ±0.2400 | **-3.022** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8942** | 0.1386 | ±0.2773 | **+13.662** | **1.71e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2463 | **-10.661** | **1.55e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.459** | **0.0139** | * |
| BMI (kg/m2) | +0.0102 | 0.0066 | ±0.0132 | +1.545 | 0.1224 |  |
| **Hypertension** | **+0.2874** | 0.0960 | ±0.1920 | **+2.995** | **0.0027** | ** |
| High cholesterol | -0.0881 | 0.0920 | ±0.1839 | -0.958 | 0.3381 |  |
| Kidney disease | +0.1148 | 0.1383 | ±0.2766 | +0.830 | 0.4066 |  |
| **Circulatory disease** | **+0.2730** | 0.1292 | ±0.2583 | **+2.114** | **0.0346** | * |
| Time in range 70-180, pooled (%) | -0.0013 | 0.0024 | ±0.0048 | -0.542 | 0.5881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2980**, F-statistic = **64.63** (p = **9.08e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0567** | 0.4388 | ±0.8775 | **+54.830** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1188 | 0.0922 | ±0.1844 | -1.288 | 0.1977 |  |
| Education: high school or below (vs college) | +0.1897 | 0.1577 | ±0.3153 | +1.203 | 0.2290 |  |
| Site: UCSD (vs UAB) | -0.1160 | 0.1110 | ±0.2220 | -1.045 | 0.2959 |  |
| **Site: UW (vs UAB)** | **-1.1188** | 0.1080 | ±0.2160 | **-10.361** | **3.75e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3629** | 0.1200 | ±0.2400 | **-3.025** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8938** | 0.1386 | ±0.2772 | **+13.662** | **1.72e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3133** | 0.1232 | ±0.2463 | **-10.663** | **1.51e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.461** | **0.0138** | * |
| BMI (kg/m2) | +0.0102 | 0.0066 | ±0.0132 | +1.549 | 0.1215 |  |
| **Hypertension** | **+0.2880** | 0.0960 | ±0.1920 | **+2.999** | **0.0027** | ** |
| High cholesterol | -0.0879 | 0.0920 | ±0.1839 | -0.956 | 0.3392 |  |
| Kidney disease | +0.1157 | 0.1383 | ±0.2765 | +0.837 | 0.4025 |  |
| **Circulatory disease** | **+0.2732** | 0.1291 | ±0.2583 | **+2.116** | **0.0344** | * |
| Avg. daily time in range 70-180 (%) | -0.0012 | 0.0024 | ±0.0048 | -0.479 | 0.6318 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.64** (p = **8.87e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9676** | 0.3651 | ±0.7301 | **+65.652** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1222 | 0.0920 | ±0.1840 | -1.328 | 0.1843 |  |
| Education: high school or below (vs college) | +0.1923 | 0.1561 | ±0.3122 | +1.232 | 0.2178 |  |
| Site: UCSD (vs UAB) | -0.1272 | 0.1113 | ±0.2226 | -1.143 | 0.2531 |  |
| **Site: UW (vs UAB)** | **-1.1258** | 0.1080 | ±0.2160 | **-10.424** | **1.93e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1199 | ±0.2397 | **-3.035** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8912** | 0.1386 | ±0.2771 | **+13.648** | **2.07e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3155** | 0.1232 | ±0.2465 | **-10.675** | **1.34e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.455** | **0.0141** | * |
| BMI (kg/m2) | +0.0106 | 0.0066 | ±0.0131 | +1.618 | 0.1057 |  |
| **Hypertension** | **+0.2918** | 0.0962 | ±0.1924 | **+3.033** | **0.0024** | ** |
| High cholesterol | -0.0890 | 0.0918 | ±0.1837 | -0.969 | 0.3325 |  |
| Kidney disease | +0.1232 | 0.1380 | ±0.2761 | +0.892 | 0.3721 |  |
| **Circulatory disease** | **+0.2794** | 0.1289 | ±0.2579 | **+2.167** | **0.0303** | * |
| Any reading < 54 during wear (0/1) | -0.0540 | 0.0972 | ±0.1945 | -0.555 | 0.5786 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.3037**, Adj R² = **0.2990**, F-statistic = **64.95** (p = **1.96e-152**), Residual SE = **1.985** on **2085** df, AIC = **8853.2**, BIC = **8938.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8864** | 0.3622 | ±0.7244 | **+65.944** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1182 | 0.0920 | ±0.1841 | -1.284 | 0.1990 |  |
| Education: high school or below (vs college) | +0.2113 | 0.1564 | ±0.3127 | +1.352 | 0.1765 |  |
| Site: UCSD (vs UAB) | -0.0975 | 0.1111 | ±0.2222 | -0.877 | 0.3804 |  |
| **Site: UW (vs UAB)** | **-1.1030** | 0.1079 | ±0.2158 | **-10.225** | **1.53e-24** | *** |
| **Season: spring (vs autumn)** | **-0.3597** | 0.1200 | ±0.2401 | **-2.997** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8907** | 0.1384 | ±0.2769 | **+13.658** | **1.80e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3135** | 0.1231 | ±0.2462 | **-10.668** | **1.44e-26** | *** |
| **Age (years)** | **+0.0106** | 0.0042 | ±0.0084 | **+2.545** | **0.0109** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0132 | +1.589 | 0.1121 |  |
| **Hypertension** | **+0.2949** | 0.0961 | ±0.1921 | **+3.070** | **0.0021** | ** |
| High cholesterol | -0.0765 | 0.0920 | ±0.1839 | -0.832 | 0.4052 |  |
| Kidney disease | +0.1250 | 0.1379 | ±0.2757 | +0.907 | 0.3646 |  |
| **Circulatory disease** | **+0.2701** | 0.1288 | ±0.2576 | **+2.097** | **0.0360** | * |
| Time < 54 (%) | +0.1554 | 0.0954 | ±0.1908 | +1.629 | 0.1033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.3034**, Adj R² = **0.2987**, F-statistic = **64.87** (p = **2.88e-152**), Residual SE = **1.985** on **2085** df, AIC = **8854.0**, BIC = **8938.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9097** | 0.3612 | ±0.7225 | **+66.190** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1168 | 0.0920 | ±0.1840 | -1.269 | 0.2044 |  |
| Education: high school or below (vs college) | +0.2087 | 0.1562 | ±0.3125 | +1.336 | 0.1816 |  |
| Site: UCSD (vs UAB) | -0.1033 | 0.1109 | ±0.2218 | -0.932 | 0.3515 |  |
| **Site: UW (vs UAB)** | **-1.1045** | 0.1078 | ±0.2156 | **-10.244** | **1.25e-24** | *** |
| **Season: spring (vs autumn)** | **-0.3595** | 0.1200 | ±0.2400 | **-2.995** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8910** | 0.1385 | ±0.2771 | **+13.649** | **2.04e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3152** | 0.1231 | ±0.2462 | **-10.683** | **1.22e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.494** | **0.0126** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0131 | +1.590 | 0.1119 |  |
| **Hypertension** | **+0.2950** | 0.0961 | ±0.1921 | **+3.071** | **0.0021** | ** |
| High cholesterol | -0.0786 | 0.0919 | ±0.1838 | -0.855 | 0.3926 |  |
| Kidney disease | +0.1235 | 0.1378 | ±0.2756 | +0.896 | 0.3702 |  |
| **Circulatory disease** | **+0.2707** | 0.1288 | ±0.2576 | **+2.102** | **0.0355** | * |
| Avg. daily time < 54 (%) | +0.1638 | 0.1283 | ±0.2566 | +1.277 | 0.2017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.3031**, Adj R² = **0.2984**, F-statistic = **64.77** (p = **4.74e-152**), Residual SE = **1.985** on **2085** df, AIC = **8855.0**, BIC = **8939.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9058** | 0.3630 | ±0.7259 | **+65.864** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1158 | 0.0922 | ±0.1843 | -1.256 | 0.2091 |  |
| Education: high school or below (vs college) | +0.2051 | 0.1561 | ±0.3123 | +1.314 | 0.1889 |  |
| Site: UCSD (vs UAB) | -0.1097 | 0.1108 | ±0.2216 | -0.990 | 0.3223 |  |
| **Site: UW (vs UAB)** | **-1.1110** | 0.1077 | ±0.2154 | **-10.314** | **6.08e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3612** | 0.1199 | ±0.2398 | **-3.012** | **0.0026** | ** |
| **Season: summer (vs autumn)** | **+1.8936** | 0.1383 | ±0.2765 | **+13.696** | **1.07e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3149** | 0.1232 | ±0.2464 | **-10.674** | **1.35e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.513** | **0.0120** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.570 | 0.1165 |  |
| **Hypertension** | **+0.2946** | 0.0960 | ±0.1921 | **+3.068** | **0.0022** | ** |
| High cholesterol | -0.0814 | 0.0921 | ±0.1842 | -0.884 | 0.3769 |  |
| Kidney disease | +0.1243 | 0.1379 | ±0.2757 | +0.902 | 0.3671 |  |
| **Circulatory disease** | **+0.2734** | 0.1290 | ±0.2580 | **+2.120** | **0.0340** | * |
| Time 54-69, pooled (%) | +0.0383 | 0.0277 | ±0.0554 | +1.383 | 0.1668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.3034**, Adj R² = **0.2987**, F-statistic = **64.86** (p = **3.06e-152**), Residual SE = **1.985** on **2085** df, AIC = **8854.1**, BIC = **8938.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9075** | 0.3620 | ±0.7241 | **+66.034** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1137 | 0.0921 | ±0.1843 | -1.234 | 0.2172 |  |
| Education: high school or below (vs college) | +0.2063 | 0.1561 | ±0.3122 | +1.321 | 0.1863 |  |
| Site: UCSD (vs UAB) | -0.1092 | 0.1107 | ±0.2214 | -0.986 | 0.3241 |  |
| **Site: UW (vs UAB)** | **-1.1082** | 0.1076 | ±0.2153 | **-10.295** | **7.39e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3608** | 0.1199 | ±0.2398 | **-3.010** | **0.0026** | ** |
| **Season: summer (vs autumn)** | **+1.8941** | 0.1382 | ±0.2764 | **+13.704** | **9.57e-43** | *** |
| **Season: winter (vs autumn)** | **-1.3164** | 0.1231 | ±0.2463 | **-10.689** | **1.14e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.493** | **0.0127** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.563 | 0.1181 |  |
| **Hypertension** | **+0.2955** | 0.0960 | ±0.1920 | **+3.078** | **0.0021** | ** |
| High cholesterol | -0.0809 | 0.0920 | ±0.1841 | -0.879 | 0.3796 |  |
| Kidney disease | +0.1246 | 0.1378 | ±0.2756 | +0.904 | 0.3659 |  |
| **Circulatory disease** | **+0.2735** | 0.1289 | ±0.2579 | **+2.122** | **0.0339** | * |
| Avg. daily time 54-69 (%) | +0.0472 | 0.0274 | ±0.0548 | +1.725 | 0.0845 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.3033**, Adj R² = **0.2987**, F-statistic = **64.85** (p = **3.17e-152**), Residual SE = **1.985** on **2085** df, AIC = **8854.2**, BIC = **8938.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8929** | 0.3630 | ±0.7259 | **+65.829** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1151 | 0.0921 | ±0.1842 | -1.250 | 0.2113 |  |
| Education: high school or below (vs college) | +0.2084 | 0.1561 | ±0.3122 | +1.335 | 0.1819 |  |
| Site: UCSD (vs UAB) | -0.1040 | 0.1109 | ±0.2218 | -0.938 | 0.3483 |  |
| **Site: UW (vs UAB)** | **-1.1064** | 0.1077 | ±0.2154 | **-10.271** | **9.53e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3603** | 0.1200 | ±0.2399 | **-3.004** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8931** | 0.1383 | ±0.2765 | **+13.691** | **1.14e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3149** | 0.1232 | ±0.2463 | **-10.677** | **1.31e-26** | *** |
| **Age (years)** | **+0.0106** | 0.0042 | ±0.0084 | **+2.524** | **0.0116** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.568 | 0.1169 |  |
| **Hypertension** | **+0.2955** | 0.0960 | ±0.1921 | **+3.077** | **0.0021** | ** |
| High cholesterol | -0.0791 | 0.0921 | ±0.1841 | -0.860 | 0.3900 |  |
| Kidney disease | +0.1245 | 0.1379 | ±0.2757 | +0.903 | 0.3666 |  |
| **Circulatory disease** | **+0.2721** | 0.1289 | ±0.2579 | **+2.110** | **0.0348** | * |
| Time < 70 (%) | +0.0381 | 0.0234 | ±0.0467 | +1.629 | 0.1032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.3035**, Adj R² = **0.2988**, F-statistic = **64.90** (p = **2.47e-152**), Residual SE = **1.985** on **2085** df, AIC = **8853.7**, BIC = **8938.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9028** | 0.3619 | ±0.7238 | **+66.047** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1133 | 0.0921 | ±0.1842 | -1.231 | 0.2185 |  |
| Education: high school or below (vs college) | +0.2083 | 0.1561 | ±0.3122 | +1.335 | 0.1820 |  |
| Site: UCSD (vs UAB) | -0.1057 | 0.1107 | ±0.2215 | -0.955 | 0.3397 |  |
| **Site: UW (vs UAB)** | **-1.1050** | 0.1076 | ±0.2153 | **-10.265** | **1.01e-24** | *** |
| **Season: spring (vs autumn)** | **-0.3601** | 0.1199 | ±0.2398 | **-3.003** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8935** | 0.1383 | ±0.2765 | **+13.695** | **1.08e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3165** | 0.1231 | ±0.2462 | **-10.694** | **1.09e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.492** | **0.0127** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.565 | 0.1177 |  |
| **Hypertension** | **+0.2961** | 0.0960 | ±0.1920 | **+3.084** | **0.0020** | ** |
| High cholesterol | -0.0795 | 0.0920 | ±0.1840 | -0.864 | 0.3877 |  |
| Kidney disease | +0.1243 | 0.1378 | ±0.2755 | +0.902 | 0.3669 |  |
| **Circulatory disease** | **+0.2725** | 0.1289 | ±0.2578 | **+2.114** | **0.0345** | * |
| Avg. daily time < 70 (%) | +0.0426 | 0.0240 | ±0.0481 | +1.774 | 0.0760 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2980**, F-statistic = **64.63** (p = **8.93e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1548** | 0.5764 | ±1.1527 | **+41.910** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1182 | 0.0922 | ±0.1844 | -1.281 | 0.2001 |  |
| Education: high school or below (vs college) | +0.1900 | 0.1574 | ±0.3149 | +1.207 | 0.2275 |  |
| Site: UCSD (vs UAB) | -0.1167 | 0.1110 | ±0.2219 | -1.052 | 0.2928 |  |
| **Site: UW (vs UAB)** | **-1.1179** | 0.1081 | ±0.2163 | **-10.338** | **4.74e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3626** | 0.1200 | ±0.2401 | **-3.021** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8960** | 0.1388 | ±0.2775 | **+13.663** | **1.69e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2464 | **-10.657** | **1.62e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.508** | **0.0121** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.567 | 0.1171 |  |
| **Hypertension** | **+0.2887** | 0.0960 | ±0.1919 | **+3.008** | **0.0026** | ** |
| High cholesterol | -0.0864 | 0.0920 | ±0.1841 | -0.939 | 0.3477 |  |
| Kidney disease | +0.1187 | 0.1383 | ±0.2766 | +0.858 | 0.3907 |  |
| **Circulatory disease** | **+0.2732** | 0.1292 | ±0.2584 | **+2.114** | **0.0345** | * |
| Time 54-250, pooled (%) | -0.0022 | 0.0045 | ±0.0091 | -0.488 | 0.6253 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.63** (p = **9.29e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1273** | 0.5849 | ±1.1699 | **+41.249** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1186 | 0.0922 | ±0.1845 | -1.286 | 0.1985 |  |
| Education: high school or below (vs college) | +0.1911 | 0.1574 | ±0.3149 | +1.214 | 0.2248 |  |
| Site: UCSD (vs UAB) | -0.1174 | 0.1110 | ±0.2219 | -1.058 | 0.2902 |  |
| **Site: UW (vs UAB)** | **-1.1187** | 0.1081 | ±0.2162 | **-10.346** | **4.35e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3629** | 0.1200 | ±0.2400 | **-3.023** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8953** | 0.1388 | ±0.2775 | **+13.659** | **1.78e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3132** | 0.1232 | ±0.2464 | **-10.658** | **1.59e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.504** | **0.0123** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.569 | 0.1166 |  |
| **Hypertension** | **+0.2891** | 0.0960 | ±0.1919 | **+3.013** | **0.0026** | ** |
| High cholesterol | -0.0864 | 0.0920 | ±0.1841 | -0.938 | 0.3481 |  |
| Kidney disease | +0.1193 | 0.1383 | ±0.2766 | +0.863 | 0.3883 |  |
| **Circulatory disease** | **+0.2734** | 0.1292 | ±0.2584 | **+2.116** | **0.0344** | * |
| Avg. daily time 54-250 (%) | -0.0019 | 0.0046 | ±0.0092 | -0.416 | 0.6772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **9.94e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9441** | 0.3615 | ±0.7230 | **+66.237** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1204 | 0.0921 | ±0.1843 | -1.307 | 0.1912 |  |
| Education: high school or below (vs college) | +0.1941 | 0.1572 | ±0.3144 | +1.235 | 0.2169 |  |
| Site: UCSD (vs UAB) | -0.1189 | 0.1106 | ±0.2211 | -1.075 | 0.2822 |  |
| **Site: UW (vs UAB)** | **-1.1215** | 0.1076 | ±0.2152 | **-10.421** | **1.98e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3633** | 0.1199 | ±0.2398 | **-3.030** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8922** | 0.1384 | ±0.2768 | **+13.673** | **1.48e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3134** | 0.1232 | ±0.2463 | **-10.665** | **1.49e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.451** | **0.0142** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.567 | 0.1171 |  |
| **Hypertension** | **+0.2895** | 0.0961 | ±0.1922 | **+3.013** | **0.0026** | ** |
| High cholesterol | -0.0874 | 0.0920 | ±0.1839 | -0.951 | 0.3418 |  |
| Kidney disease | +0.1197 | 0.1381 | ±0.2762 | +0.867 | 0.3861 |  |
| **Circulatory disease** | **+0.2746** | 0.1291 | ±0.2581 | **+2.128** | **0.0334** | * |
| Time 181-250, pooled (%) | +0.0010 | 0.0036 | ±0.0072 | +0.281 | 0.7785 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.01e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9430** | 0.3614 | ±0.7228 | **+66.247** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1206 | 0.0921 | ±0.1843 | -1.309 | 0.1905 |  |
| Education: high school or below (vs college) | +0.1948 | 0.1572 | ±0.3145 | +1.239 | 0.2153 |  |
| Site: UCSD (vs UAB) | -0.1193 | 0.1106 | ±0.2212 | -1.079 | 0.2808 |  |
| **Site: UW (vs UAB)** | **-1.1216** | 0.1076 | ±0.2153 | **-10.420** | **2.01e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3634** | 0.1199 | ±0.2398 | **-3.030** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8923** | 0.1384 | ±0.2768 | **+13.674** | **1.45e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3135** | 0.1232 | ±0.2463 | **-10.665** | **1.48e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.461** | **0.0139** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.572 | 0.1158 |  |
| **Hypertension** | **+0.2899** | 0.0961 | ±0.1922 | **+3.016** | **0.0026** | ** |
| High cholesterol | -0.0871 | 0.0919 | ±0.1839 | -0.947 | 0.3437 |  |
| Kidney disease | +0.1208 | 0.1380 | ±0.2760 | +0.875 | 0.3813 |  |
| **Circulatory disease** | **+0.2748** | 0.1291 | ±0.2581 | **+2.129** | **0.0332** | * |
| Avg. daily time 181-250 (%) | +0.0008 | 0.0035 | ±0.0071 | +0.215 | 0.8299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.43e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9418** | 0.3610 | ±0.7220 | **+66.322** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1192 | 0.0922 | ±0.1844 | -1.293 | 0.1959 |  |
| Education: high school or below (vs college) | +0.1908 | 0.1576 | ±0.3153 | +1.210 | 0.2262 |  |
| Site: UCSD (vs UAB) | -0.1173 | 0.1109 | ±0.2217 | -1.058 | 0.2901 |  |
| **Site: UW (vs UAB)** | **-1.1198** | 0.1079 | ±0.2158 | **-10.378** | **3.11e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3630** | 0.1200 | ±0.2400 | **-3.025** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8937** | 0.1386 | ±0.2773 | **+13.659** | **1.78e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3131** | 0.1232 | ±0.2463 | **-10.661** | **1.54e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.466** | **0.0137** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.556 | 0.1197 |  |
| **Hypertension** | **+0.2883** | 0.0960 | ±0.1919 | **+3.005** | **0.0027** | ** |
| High cholesterol | -0.0877 | 0.0920 | ±0.1839 | -0.953 | 0.3403 |  |
| Kidney disease | +0.1173 | 0.1383 | ±0.2766 | +0.848 | 0.3964 |  |
| **Circulatory disease** | **+0.2737** | 0.1292 | ±0.2583 | **+2.119** | **0.0341** | * |
| Time > 180 (%) | +0.0010 | 0.0024 | ±0.0048 | +0.406 | 0.6845 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.71e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9417** | 0.3611 | ±0.7221 | **+66.310** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1196 | 0.0922 | ±0.1844 | -1.297 | 0.1945 |  |
| Education: high school or below (vs college) | +0.1919 | 0.1577 | ±0.3153 | +1.217 | 0.2235 |  |
| Site: UCSD (vs UAB) | -0.1178 | 0.1109 | ±0.2218 | -1.062 | 0.2881 |  |
| **Site: UW (vs UAB)** | **-1.1202** | 0.1079 | ±0.2158 | **-10.381** | **3.02e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3632** | 0.1200 | ±0.2399 | **-3.027** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8935** | 0.1386 | ±0.2772 | **+13.659** | **1.78e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3133** | 0.1232 | ±0.2463 | **-10.663** | **1.52e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.470** | **0.0135** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.561 | 0.1186 |  |
| **Hypertension** | **+0.2889** | 0.0960 | ±0.1919 | **+3.010** | **0.0026** | ** |
| High cholesterol | -0.0874 | 0.0919 | ±0.1839 | -0.950 | 0.3420 |  |
| Kidney disease | +0.1184 | 0.1383 | ±0.2765 | +0.857 | 0.3917 |  |
| **Circulatory disease** | **+0.2740** | 0.1292 | ±0.2583 | **+2.121** | **0.0339** | * |
| Avg. daily time > 180 (%) | +0.0008 | 0.0024 | ±0.0048 | +0.336 | 0.7372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **9.96e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9415** | 0.3612 | ±0.7223 | **+66.289** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1194 | 0.0923 | ±0.1846 | -1.294 | 0.1958 |  |
| Education: high school or below (vs college) | +0.1935 | 0.1574 | ±0.3149 | +1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | -0.1185 | 0.1109 | ±0.2218 | -1.069 | 0.2852 |  |
| **Site: UW (vs UAB)** | **-1.1208** | 0.1079 | ±0.2159 | **-10.384** | **2.94e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1200 | ±0.2399 | **-3.032** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8934** | 0.1386 | ±0.2772 | **+13.659** | **1.77e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3139** | 0.1232 | ±0.2464 | **-10.665** | **1.49e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.495** | **0.0126** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0133 | +1.546 | 0.1222 |  |
| **Hypertension** | **+0.2900** | 0.0960 | ±0.1919 | **+3.023** | **0.0025** | ** |
| High cholesterol | -0.0868 | 0.0920 | ±0.1840 | -0.944 | 0.3453 |  |
| Kidney disease | +0.1210 | 0.1378 | ±0.2756 | +0.878 | 0.3801 |  |
| **Circulatory disease** | **+0.2745** | 0.1291 | ±0.2583 | **+2.125** | **0.0336** | * |
| Nocturnal time > 180 (%) | +0.0006 | 0.0024 | ±0.0049 | +0.260 | 0.7952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.65** (p = **8.39e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.2**, BIC = **8940.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9464** | 0.3617 | ±0.7233 | **+66.213** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1245 | 0.0924 | ±0.1848 | -1.347 | 0.1779 |  |
| Education: high school or below (vs college) | +0.2025 | 0.1565 | ±0.3130 | +1.294 | 0.1955 |  |
| Site: UCSD (vs UAB) | -0.1240 | 0.1106 | ±0.2212 | -1.122 | 0.2621 |  |
| **Site: UW (vs UAB)** | **-1.1234** | 0.1075 | ±0.2150 | **-10.448** | **1.49e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3668** | 0.1201 | ±0.2402 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.8921** | 0.1384 | ±0.2769 | **+13.668** | **1.57e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3171** | 0.1233 | ±0.2467 | **-10.678** | **1.29e-26** | *** |
| **Age (years)** | **+0.0107** | 0.0042 | ±0.0084 | **+2.555** | **0.0106** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.586 | 0.1127 |  |
| **Hypertension** | **+0.2968** | 0.0962 | ±0.1925 | **+3.084** | **0.0020** | ** |
| High cholesterol | -0.0822 | 0.0920 | ±0.1841 | -0.894 | 0.3715 |  |
| Kidney disease | +0.1336 | 0.1388 | ±0.2775 | +0.963 | 0.3357 |  |
| **Circulatory disease** | **+0.2755** | 0.1290 | ±0.2579 | **+2.136** | **0.0327** | * |
| Any reading > 250 during wear (0/1) | -0.0604 | 0.0923 | ±0.1847 | -0.654 | 0.5133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.33e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9354** | 0.3609 | ±0.7217 | **+66.328** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1186 | 0.0922 | ±0.1844 | -1.287 | 0.1983 |  |
| Education: high school or below (vs college) | +0.1911 | 0.1575 | ±0.3150 | +1.213 | 0.2250 |  |
| Site: UCSD (vs UAB) | -0.1177 | 0.1109 | ±0.2218 | -1.061 | 0.2886 |  |
| **Site: UW (vs UAB)** | **-1.1188** | 0.1081 | ±0.2162 | **-10.350** | **4.17e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3628** | 0.1200 | ±0.2401 | **-3.023** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8955** | 0.1388 | ±0.2776 | **+13.658** | **1.81e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3131** | 0.1232 | ±0.2464 | **-10.657** | **1.61e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.507** | **0.0122** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.571 | 0.1162 |  |
| **Hypertension** | **+0.2890** | 0.0960 | ±0.1919 | **+3.012** | **0.0026** | ** |
| High cholesterol | -0.0865 | 0.0920 | ±0.1841 | -0.939 | 0.3475 |  |
| Kidney disease | +0.1196 | 0.1383 | ±0.2765 | +0.865 | 0.3869 |  |
| **Circulatory disease** | **+0.2736** | 0.1292 | ±0.2584 | **+2.117** | **0.0342** | * |
| Time > 250 (%) | +0.0019 | 0.0045 | ±0.0090 | +0.411 | 0.6814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.55e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9366** | 0.3609 | ±0.7217 | **+66.330** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1190 | 0.0922 | ±0.1845 | -1.290 | 0.1971 |  |
| Education: high school or below (vs college) | +0.1919 | 0.1574 | ±0.3149 | +1.219 | 0.2229 |  |
| Site: UCSD (vs UAB) | -0.1180 | 0.1109 | ±0.2218 | -1.064 | 0.2873 |  |
| **Site: UW (vs UAB)** | **-1.1193** | 0.1081 | ±0.2162 | **-10.356** | **3.93e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3630** | 0.1200 | ±0.2400 | **-3.025** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8950** | 0.1388 | ±0.2775 | **+13.656** | **1.87e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3133** | 0.1232 | ±0.2464 | **-10.659** | **1.59e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.504** | **0.0123** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.572 | 0.1159 |  |
| **Hypertension** | **+0.2894** | 0.0960 | ±0.1919 | **+3.016** | **0.0026** | ** |
| High cholesterol | -0.0864 | 0.0920 | ±0.1841 | -0.938 | 0.3481 |  |
| Kidney disease | +0.1200 | 0.1383 | ±0.2766 | +0.868 | 0.3854 |  |
| **Circulatory disease** | **+0.2737** | 0.1292 | ±0.2584 | **+2.118** | **0.0342** | * |
| Avg. daily time > 250 (%) | +0.0017 | 0.0046 | ±0.0092 | +0.359 | 0.7195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2414**, F-statistic = **52.38** (p = **7.12e-118**), Residual SE = **5.971** on **2086** df, AIC = **13478.5**, BIC = **13557.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4444** | 1.0674 | ±2.1347 | **+46.324** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6180** | 0.2811 | ±0.5622 | **+2.198** | **0.0279** | * |
| Education: high school or below (vs college) | +0.5496 | 0.4554 | ±0.9107 | +1.207 | 0.2274 |  |
| **Site: UCSD (vs UAB)** | **+3.1579** | 0.3410 | ±0.6821 | **+9.260** | **2.05e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3227** | 0.3159 | ±0.6319 | **-4.186** | **2.84e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7771** | 0.3672 | ±0.7344 | **-4.840** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8522** | 0.3805 | ±0.7609 | **+4.868** | **1.13e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7086** | 0.3910 | ±0.7819 | **-14.602** | **2.74e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.882** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0199 | ±0.0398 | -0.924 | 0.3553 |  |
| Hypertension | -0.0452 | 0.2938 | ±0.5876 | -0.154 | 0.8777 |  |
| **High cholesterol** | **-0.7535** | 0.2746 | ±0.5491 | **-2.744** | **0.0061** | ** |
| Kidney disease | +0.6620 | 0.4192 | ±0.8383 | +1.579 | 0.1143 |  |
| Circulatory disease | +0.1963 | 0.3675 | ±0.7351 | +0.534 | 0.5933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.90e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1895** | 1.2571 | ±2.5142 | **+39.129** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6238** | 0.2814 | ±0.5628 | **+2.217** | **0.0266** | * |
| Education: high school or below (vs college) | +0.5291 | 0.4593 | ±0.9185 | +1.152 | 0.2493 |  |
| **Site: UCSD (vs UAB)** | **+3.1633** | 0.3421 | ±0.6842 | **+9.247** | **2.31e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3161** | 0.3171 | ±0.6343 | **-4.150** | **3.33e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7703** | 0.3682 | ±0.7365 | **-4.807** | **1.53e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8549** | 0.3805 | ±0.7610 | **+4.875** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7053** | 0.3910 | ±0.7820 | **-14.592** | **3.16e-48** | *** |
| **Age (years)** | **-0.0487** | 0.0125 | ±0.0250 | **-3.891** | **9.97e-05** | *** |
| BMI (kg/m2) | -0.0193 | 0.0201 | ±0.0403 | -0.958 | 0.3380 |  |
| Hypertension | -0.0557 | 0.2941 | ±0.5882 | -0.189 | 0.8498 |  |
| **High cholesterol** | **-0.7627** | 0.2760 | ±0.5520 | **-2.763** | **0.0057** | ** |
| Kidney disease | +0.6531 | 0.4199 | ±0.8397 | +1.555 | 0.1198 |  |
| Circulatory disease | +0.1918 | 0.3680 | ±0.7361 | +0.521 | 0.6024 |  |
| HbA1c (%) | +0.0496 | 0.1329 | ±0.2658 | +0.373 | 0.7090 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.62** (p = **5.00e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3036** | 1.1416 | ±2.2831 | **+43.190** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6209** | 0.2813 | ±0.5626 | **+2.207** | **0.0273** | * |
| Education: high school or below (vs college) | +0.5339 | 0.4588 | ±0.9177 | +1.164 | 0.2446 |  |
| **Site: UCSD (vs UAB)** | **+3.1642** | 0.3428 | ±0.6857 | **+9.230** | **2.72e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3192** | 0.3169 | ±0.6337 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7760** | 0.3676 | ±0.7352 | **-4.831** | **1.36e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8546** | 0.3805 | ±0.7610 | **+4.874** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7064** | 0.3909 | ±0.7817 | **-14.600** | **2.82e-48** | *** |
| **Age (years)** | **-0.0486** | 0.0125 | ±0.0250 | **-3.889** | **1.01e-04** | *** |
| BMI (kg/m2) | -0.0189 | 0.0201 | ±0.0402 | -0.941 | 0.3469 |  |
| Hypertension | -0.0541 | 0.2943 | ±0.5887 | -0.184 | 0.8541 |  |
| **High cholesterol** | **-0.7587** | 0.2752 | ±0.5504 | **-2.757** | **0.0058** | ** |
| Kidney disease | +0.6476 | 0.4206 | ±0.8411 | +1.540 | 0.1236 |  |
| Circulatory disease | +0.1925 | 0.3680 | ±0.7360 | +0.523 | 0.6009 |  |
| Mean glucose (mg/dL) | +0.0013 | 0.0041 | ±0.0081 | +0.316 | 0.7517 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.62** (p = **5.00e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1252** | 1.4414 | ±2.8827 | **+34.082** | **1.35e-254** | *** |
| **Education: graduate level (vs college)** | **+0.6209** | 0.2813 | ±0.5626 | **+2.207** | **0.0273** | * |
| Education: high school or below (vs college) | +0.5339 | 0.4588 | ±0.9177 | +1.164 | 0.2446 |  |
| **Site: UCSD (vs UAB)** | **+3.1642** | 0.3428 | ±0.6857 | **+9.230** | **2.72e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3192** | 0.3169 | ±0.6337 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7760** | 0.3676 | ±0.7352 | **-4.831** | **1.36e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8546** | 0.3805 | ±0.7610 | **+4.874** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7064** | 0.3909 | ±0.7817 | **-14.600** | **2.82e-48** | *** |
| **Age (years)** | **-0.0486** | 0.0125 | ±0.0250 | **-3.889** | **1.01e-04** | *** |
| BMI (kg/m2) | -0.0189 | 0.0201 | ±0.0402 | -0.941 | 0.3469 |  |
| Hypertension | -0.0541 | 0.2943 | ±0.5887 | -0.184 | 0.8541 |  |
| **High cholesterol** | **-0.7587** | 0.2752 | ±0.5504 | **-2.757** | **0.0058** | ** |
| Kidney disease | +0.6476 | 0.4206 | ±0.8411 | +1.540 | 0.1236 |  |
| Circulatory disease | +0.1925 | 0.3680 | ±0.7360 | +0.523 | 0.6009 |  |
| GMI (%) | +0.0539 | 0.1703 | ±0.3406 | +0.316 | 0.7517 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.84e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2662** | 1.1368 | ±2.2736 | **+43.337** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6223** | 0.2813 | ±0.5626 | **+2.212** | **0.0270** | * |
| Education: high school or below (vs college) | +0.5306 | 0.4583 | ±0.9165 | +1.158 | 0.2469 |  |
| **Site: UCSD (vs UAB)** | **+3.1639** | 0.3424 | ±0.6847 | **+9.241** | **2.43e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3200** | 0.3165 | ±0.6330 | **-4.171** | **3.04e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7782** | 0.3674 | ±0.7348 | **-4.840** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8551** | 0.3805 | ±0.7611 | **+4.875** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7083** | 0.3911 | ±0.7821 | **-14.597** | **2.94e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.882** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0194 | 0.0203 | ±0.0406 | -0.957 | 0.3386 |  |
| Hypertension | -0.0543 | 0.2939 | ±0.5878 | -0.185 | 0.8533 |  |
| **High cholesterol** | **-0.7605** | 0.2753 | ±0.5507 | **-2.762** | **0.0057** | ** |
| Kidney disease | +0.6497 | 0.4195 | ±0.8390 | +1.549 | 0.1214 |  |
| Circulatory disease | +0.1925 | 0.3680 | ±0.7361 | +0.523 | 0.6009 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0016 | 0.0040 | ±0.0081 | +0.407 | 0.6842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.2463**, Adj R² = **0.2412**, F-statistic = **48.66** (p = **4.12e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.0**, BIC = **13564.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5845** | 1.0871 | ±2.1742 | **+45.612** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6068** | 0.2822 | ±0.5644 | **+2.150** | **0.0315** | * |
| Education: high school or below (vs college) | +0.5802 | 0.4571 | ±0.9142 | +1.269 | 0.2043 |  |
| **Site: UCSD (vs UAB)** | **+3.1396** | 0.3435 | ±0.6869 | **+9.141** | **6.18e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3376** | 0.3177 | ±0.6355 | **-4.210** | **2.56e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7807** | 0.3674 | ±0.7347 | **-4.847** | **1.25e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8481** | 0.3806 | ±0.7611 | **+4.856** | **1.20e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7135** | 0.3912 | ±0.7824 | **-14.606** | **2.58e-48** | *** |
| **Age (years)** | **-0.0476** | 0.0125 | ±0.0250 | **-3.806** | **1.41e-04** | *** |
| BMI (kg/m2) | -0.0176 | 0.0199 | ±0.0399 | -0.883 | 0.3770 |  |
| Hypertension | -0.0231 | 0.2942 | ±0.5883 | -0.079 | 0.9374 |  |
| **High cholesterol** | **-0.7453** | 0.2749 | ±0.5498 | **-2.711** | **0.0067** | ** |
| Kidney disease | +0.7145 | 0.4253 | ±0.8506 | +1.680 | 0.0930 | . |
| Circulatory disease | +0.2057 | 0.3676 | ±0.7352 | +0.560 | 0.5758 |  |
| Glucose SD, pooled (mg/dL) | -0.0081 | 0.0113 | ±0.0227 | -0.715 | 0.4747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.76e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5356** | 1.0874 | ±2.1749 | **+45.553** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6116** | 0.2821 | ±0.5642 | **+2.168** | **0.0302** | * |
| Education: high school or below (vs college) | +0.5700 | 0.4574 | ±0.9147 | +1.246 | 0.2127 |  |
| **Site: UCSD (vs UAB)** | **+3.1468** | 0.3433 | ±0.6866 | **+9.166** | **4.89e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3312** | 0.3175 | ±0.6351 | **-4.192** | **2.76e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7799** | 0.3675 | ±0.7349 | **-4.844** | **1.27e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8483** | 0.3807 | ±0.7613 | **+4.856** | **1.20e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7130** | 0.3913 | ±0.7825 | **-14.602** | **2.73e-48** | *** |
| **Age (years)** | **-0.0478** | 0.0125 | ±0.0250 | **-3.821** | **1.33e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0399 | -0.902 | 0.3671 |  |
| Hypertension | -0.0312 | 0.2941 | ±0.5882 | -0.106 | 0.9154 |  |
| **High cholesterol** | **-0.7481** | 0.2750 | ±0.5500 | **-2.720** | **0.0065** | ** |
| Kidney disease | +0.6963 | 0.4253 | ±0.8506 | +1.637 | 0.1016 |  |
| Circulatory disease | +0.2012 | 0.3676 | ±0.7351 | +0.548 | 0.5840 |  |
| Avg. daily SD (mg/dL) | -0.0058 | 0.0128 | ±0.0256 | -0.456 | 0.6482 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.2467**, Adj R² = **0.2417**, F-statistic = **48.78** (p = **2.17e-117**), Residual SE = **5.970** on **2085** df, AIC = **13478.7**, BIC = **13563.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9935** | 1.1531 | ±2.3061 | **+43.357** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.5972** | 0.2823 | ±0.5647 | **+2.115** | **0.0344** | * |
| Education: high school or below (vs college) | +0.5814 | 0.4558 | ±0.9115 | +1.276 | 0.2021 |  |
| **Site: UCSD (vs UAB)** | **+3.1243** | 0.3428 | ±0.6856 | **+9.114** | **7.96e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3529** | 0.3173 | ±0.6346 | **-4.264** | **2.01e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7868** | 0.3672 | ±0.7344 | **-4.866** | **1.14e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8519** | 0.3807 | ±0.7613 | **+4.865** | **1.14e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7150** | 0.3913 | ±0.7826 | **-14.605** | **2.60e-48** | *** |
| **Age (years)** | **-0.0467** | 0.0125 | ±0.0250 | **-3.731** | **1.91e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0199 | ±0.0397 | -0.903 | 0.3663 |  |
| Hypertension | -0.0106 | 0.2942 | ±0.5884 | -0.036 | 0.9712 |  |
| **High cholesterol** | **-0.7494** | 0.2746 | ±0.5492 | **-2.729** | **0.0063** | ** |
| Kidney disease | +0.7553 | 0.4261 | ±0.8521 | +1.773 | 0.0763 | . |
| Circulatory disease | +0.2100 | 0.3673 | ±0.7347 | +0.572 | 0.5675 |  |
| CV (%) | -0.0341 | 0.0252 | ±0.0505 | -1.351 | 0.1767 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.2466**, Adj R² = **0.2415**, F-statistic = **48.74** (p = **2.72e-117**), Residual SE = **5.970** on **2085** df, AIC = **13479.1**, BIC = **13563.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7093** | 1.2304 | ±2.4609 | **+39.587** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6003** | 0.2822 | ±0.5644 | **+2.127** | **0.0334** | * |
| Education: high school or below (vs college) | +0.5787 | 0.4562 | ±0.9124 | +1.269 | 0.2046 |  |
| **Site: UCSD (vs UAB)** | **+3.1328** | 0.3424 | ±0.6847 | **+9.150** | **5.67e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3409** | 0.3166 | ±0.6333 | **-4.235** | **2.29e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7811** | 0.3672 | ±0.7345 | **-4.850** | **1.23e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8557** | 0.3808 | ±0.7616 | **+4.873** | **1.10e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7087** | 0.3912 | ±0.7823 | **-14.594** | **3.06e-48** | *** |
| **Age (years)** | **-0.0469** | 0.0125 | ±0.0251 | **-3.743** | **1.81e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0398 | -0.906 | 0.3649 |  |
| Hypertension | -0.0145 | 0.2947 | ±0.5894 | -0.049 | 0.9607 |  |
| **High cholesterol** | **-0.7478** | 0.2746 | ±0.5492 | **-2.723** | **0.0065** | ** |
| Kidney disease | +0.7239 | 0.4232 | ±0.8464 | +1.710 | 0.0872 | . |
| Circulatory disease | +0.2085 | 0.3675 | ±0.7351 | +0.567 | 0.5705 |  |
| Mean / SD ratio | +0.1146 | 0.0979 | ±0.1958 | +1.171 | 0.2415 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.64** (p = **4.66e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.2**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1350** | 1.2355 | ±2.4711 | **+39.768** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6114** | 0.2821 | ±0.5642 | **+2.167** | **0.0302** | * |
| Education: high school or below (vs college) | +0.5626 | 0.4563 | ±0.9127 | +1.233 | 0.2177 |  |
| **Site: UCSD (vs UAB)** | **+3.1504** | 0.3418 | ±0.6835 | **+9.218** | **3.01e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3285** | 0.3163 | ±0.6326 | **-4.200** | **2.67e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7799** | 0.3674 | ±0.7349 | **-4.844** | **1.27e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8509** | 0.3808 | ±0.7616 | **+4.861** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7104** | 0.3913 | ±0.7825 | **-14.595** | **3.03e-48** | *** |
| **Age (years)** | **-0.0477** | 0.0126 | ±0.0251 | **-3.796** | **1.47e-04** | *** |
| BMI (kg/m2) | -0.0182 | 0.0199 | ±0.0398 | -0.917 | 0.3591 |  |
| Hypertension | -0.0336 | 0.2947 | ±0.5895 | -0.114 | 0.9092 |  |
| **High cholesterol** | **-0.7517** | 0.2747 | ±0.5494 | **-2.736** | **0.0062** | ** |
| Kidney disease | +0.6873 | 0.4223 | ±0.8446 | +1.627 | 0.1037 |  |
| Circulatory disease | +0.1982 | 0.3676 | ±0.7351 | +0.539 | 0.5897 |  |
| Avg. daily mean/SD | +0.0411 | 0.0842 | ±0.1684 | +0.488 | 0.6259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.62** (p = **5.17e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5594** | 1.2129 | ±2.4258 | **+40.861** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6150** | 0.2820 | ±0.5640 | **+2.181** | **0.0292** | * |
| Education: high school or below (vs college) | +0.5548 | 0.4573 | ±0.9147 | +1.213 | 0.2251 |  |
| **Site: UCSD (vs UAB)** | **+3.1532** | 0.3434 | ±0.6868 | **+9.182** | **4.23e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3293** | 0.3193 | ±0.6386 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7781** | 0.3674 | ±0.7349 | **-4.839** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8497** | 0.3804 | ±0.7608 | **+4.863** | **1.16e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7106** | 0.3908 | ±0.7815 | **-14.614** | **2.29e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.888** | **1.01e-04** | *** |
| BMI (kg/m2) | -0.0183 | 0.0199 | ±0.0398 | -0.917 | 0.3590 |  |
| Hypertension | -0.0437 | 0.2938 | ±0.5877 | -0.149 | 0.8818 |  |
| **High cholesterol** | **-0.7539** | 0.2747 | ±0.5494 | **-2.744** | **0.0061** | ** |
| Kidney disease | +0.6691 | 0.4222 | ±0.8445 | +1.585 | 0.1131 |  |
| Circulatory disease | +0.1970 | 0.3675 | ±0.7350 | +0.536 | 0.5919 |  |
| MAG (mg/dL/h) | -0.0028 | 0.0145 | ±0.0290 | -0.192 | 0.8476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2412**, F-statistic = **48.65** (p = **4.42e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.1**, BIC = **13564.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6357** | 1.1119 | ±2.2238 | **+44.640** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6098** | 0.2821 | ±0.5641 | **+2.162** | **0.0306** | * |
| Education: high school or below (vs college) | +0.5753 | 0.4579 | ±0.9158 | +1.256 | 0.2090 |  |
| **Site: UCSD (vs UAB)** | **+3.1423** | 0.3433 | ±0.6867 | **+9.153** | **5.55e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3343** | 0.3175 | ±0.6350 | **-4.203** | **2.64e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7799** | 0.3674 | ±0.7348 | **-4.844** | **1.27e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8487** | 0.3806 | ±0.7613 | **+4.857** | **1.19e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7139** | 0.3911 | ±0.7822 | **-14.609** | **2.46e-48** | *** |
| **Age (years)** | **-0.0478** | 0.0125 | ±0.0250 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | -0.0182 | 0.0199 | ±0.0398 | -0.916 | 0.3594 |  |
| Hypertension | -0.0299 | 0.2940 | ±0.5880 | -0.102 | 0.9189 |  |
| **High cholesterol** | **-0.7472** | 0.2748 | ±0.5497 | **-2.719** | **0.0066** | ** |
| Kidney disease | +0.7042 | 0.4250 | ±0.8499 | +1.657 | 0.0975 | . |
| Circulatory disease | +0.2037 | 0.3674 | ±0.7347 | +0.555 | 0.5792 |  |
| Avg. daily range (mg/dL) | -0.0021 | 0.0034 | ±0.0068 | -0.611 | 0.5411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.2463**, Adj R² = **0.2412**, F-statistic = **48.67** (p = **3.91e-117**), Residual SE = **5.971** on **2085** df, AIC = **13479.9**, BIC = **13564.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5325** | 1.0739 | ±2.1479 | **+46.122** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6035** | 0.2822 | ±0.5644 | **+2.139** | **0.0325** | * |
| Education: high school or below (vs college) | +0.5708 | 0.4562 | ±0.9123 | +1.251 | 0.2108 |  |
| **Site: UCSD (vs UAB)** | **+3.1407** | 0.3430 | ±0.6860 | **+9.157** | **5.35e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3383** | 0.3175 | ±0.6350 | **-4.215** | **2.50e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7743** | 0.3671 | ±0.7343 | **-4.833** | **1.35e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8590** | 0.3810 | ±0.7619 | **+4.880** | **1.06e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7051** | 0.3915 | ±0.7829 | **-14.574** | **4.12e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0125 | ±0.0249 | **-3.871** | **1.08e-04** | *** |
| BMI (kg/m2) | -0.0170 | 0.0200 | ±0.0399 | -0.850 | 0.3951 |  |
| Hypertension | -0.0283 | 0.2943 | ±0.5886 | -0.096 | 0.9233 |  |
| **High cholesterol** | **-0.7444** | 0.2748 | ±0.5495 | **-2.709** | **0.0067** | ** |
| Kidney disease | +0.6976 | 0.4216 | ±0.8432 | +1.655 | 0.0980 | . |
| Circulatory disease | +0.2142 | 0.3689 | ±0.7378 | +0.581 | 0.5614 |  |
| SD of daily means (mg/dL) | -0.0166 | 0.0214 | ±0.0429 | -0.774 | 0.4389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.64** (p = **4.65e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.2**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1038** | 1.2958 | ±2.5916 | **+37.894** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6112** | 0.2814 | ±0.5627 | **+2.172** | **0.0298** | * |
| Education: high school or below (vs college) | +0.5727 | 0.4589 | ±0.9177 | +1.248 | 0.2120 |  |
| **Site: UCSD (vs UAB)** | **+3.1437** | 0.3442 | ±0.6884 | **+9.133** | **6.65e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3327** | 0.3176 | ±0.6353 | **-4.196** | **2.72e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7792** | 0.3674 | ±0.7349 | **-4.842** | **1.28e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8482** | 0.3806 | ±0.7613 | **+4.856** | **1.20e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7103** | 0.3911 | ±0.7822 | **-14.600** | **2.81e-48** | *** |
| **Age (years)** | **-0.0481** | 0.0125 | ±0.0250 | **-3.845** | **1.21e-04** | *** |
| BMI (kg/m2) | -0.0176 | 0.0200 | ±0.0401 | -0.880 | 0.3790 |  |
| Hypertension | -0.0351 | 0.2941 | ±0.5881 | -0.120 | 0.9049 |  |
| **High cholesterol** | **-0.7477** | 0.2749 | ±0.5499 | **-2.719** | **0.0065** | ** |
| Kidney disease | +0.6873 | 0.4223 | ±0.8445 | +1.628 | 0.1036 |  |
| Circulatory disease | +0.2026 | 0.3677 | ±0.7354 | +0.551 | 0.5815 |  |
| Time in range 70-180, pooled (%) | +0.0034 | 0.0070 | ±0.0141 | +0.480 | 0.6315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.73e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1279** | 1.2979 | ±2.5958 | **+37.852** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6119** | 0.2814 | ±0.5628 | **+2.175** | **0.0297** | * |
| Education: high school or below (vs college) | +0.5712 | 0.4589 | ±0.9177 | +1.245 | 0.2132 |  |
| **Site: UCSD (vs UAB)** | **+3.1446** | 0.3443 | ±0.6886 | **+9.133** | **6.67e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3320** | 0.3177 | ±0.6354 | **-4.193** | **2.75e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7786** | 0.3674 | ±0.7348 | **-4.841** | **1.29e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8489** | 0.3806 | ±0.7613 | **+4.857** | **1.19e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7096** | 0.3911 | ±0.7823 | **-14.598** | **2.90e-48** | *** |
| **Age (years)** | **-0.0481** | 0.0125 | ±0.0250 | **-3.845** | **1.20e-04** | *** |
| BMI (kg/m2) | -0.0177 | 0.0201 | ±0.0401 | -0.882 | 0.3779 |  |
| Hypertension | -0.0361 | 0.2940 | ±0.5881 | -0.123 | 0.9024 |  |
| **High cholesterol** | **-0.7480** | 0.2750 | ±0.5500 | **-2.720** | **0.0065** | ** |
| Kidney disease | +0.6858 | 0.4222 | ±0.8445 | +1.624 | 0.1043 |  |
| Circulatory disease | +0.2021 | 0.3677 | ±0.7354 | +0.550 | 0.5825 |  |
| Avg. daily time in range 70-180 (%) | +0.0031 | 0.0070 | ±0.0140 | +0.443 | 0.6574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.2465**, Adj R² = **0.2414**, F-statistic = **48.71** (p = **3.21e-117**), Residual SE = **5.971** on **2085** df, AIC = **13479.5**, BIC = **13564.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5949** | 1.0751 | ±2.1503 | **+46.129** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6117** | 0.2814 | ±0.5628 | **+2.174** | **0.0297** | * |
| Education: high school or below (vs college) | +0.5210 | 0.4568 | ±0.9136 | +1.140 | 0.2541 |  |
| **Site: UCSD (vs UAB)** | **+3.1240** | 0.3429 | ±0.6857 | **+9.112** | **8.11e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3418** | 0.3156 | ±0.6313 | **-4.251** | **2.13e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7782** | 0.3673 | ±0.7345 | **-4.842** | **1.29e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8444** | 0.3807 | ±0.7613 | **+4.845** | **1.27e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7187** | 0.3913 | ±0.7825 | **-14.616** | **2.22e-48** | *** |
| **Age (years)** | **-0.0493** | 0.0125 | ±0.0249 | **-3.958** | **7.55e-05** | *** |
| BMI (kg/m2) | -0.0177 | 0.0199 | ±0.0399 | -0.886 | 0.3756 |  |
| Hypertension | -0.0426 | 0.2940 | ±0.5881 | -0.145 | 0.8847 |  |
| **High cholesterol** | **-0.7706** | 0.2749 | ±0.5498 | **-2.803** | **0.0051** | ** |
| Kidney disease | +0.6546 | 0.4194 | ±0.8388 | +1.561 | 0.1185 |  |
| Circulatory disease | +0.2177 | 0.3686 | ±0.7372 | +0.591 | 0.5548 |  |
| Any reading < 54 during wear (0/1) | -0.2906 | 0.2931 | ±0.5861 | -0.992 | 0.3213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.2473**, Adj R² = **0.2422**, F-statistic = **48.92** (p = **1.06e-117**), Residual SE = **5.968** on **2085** df, AIC = **13477.2**, BIC = **13561.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6020** | 1.0705 | ±2.1409 | **+46.337** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6097** | 0.2809 | ±0.5618 | **+2.170** | **0.0300** | * |
| Education: high school or below (vs college) | +0.5091 | 0.4557 | ±0.9113 | +1.117 | 0.2638 |  |
| **Site: UCSD (vs UAB)** | **+3.0885** | 0.3432 | ±0.6864 | **+8.999** | **2.27e-19** | *** |
| **Site: UW (vs UAB)** | **-1.3795** | 0.3165 | ±0.6330 | **-4.359** | **1.31e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7882** | 0.3672 | ±0.7344 | **-4.870** | **1.12e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8578** | 0.3807 | ±0.7614 | **+4.880** | **1.06e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7091** | 0.3911 | ±0.7823 | **-14.596** | **2.96e-48** | *** |
| **Age (years)** | **-0.0489** | 0.0124 | ±0.0249 | **-3.932** | **8.44e-05** | *** |
| BMI (kg/m2) | -0.0183 | 0.0199 | ±0.0399 | -0.920 | 0.3577 |  |
| Hypertension | -0.0556 | 0.2939 | ±0.5878 | -0.189 | 0.8499 |  |
| **High cholesterol** | **-0.7810** | 0.2753 | ±0.5507 | **-2.836** | **0.0046** | ** |
| Kidney disease | +0.6606 | 0.4190 | ±0.8380 | +1.577 | 0.1149 |  |
| Circulatory disease | +0.2121 | 0.3679 | ±0.7358 | +0.576 | 0.5643 |  |
| **Time < 54 (%)** | **-0.4596** | 0.2117 | ±0.4233 | **-2.171** | **0.0299** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.2475**, Adj R² = **0.2425**, F-statistic = **48.99** (p = **7.41e-118**), Residual SE = **5.967** on **2085** df, AIC = **13476.5**, BIC = **13561.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5560** | 1.0660 | ±2.1321 | **+46.487** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6021** | 0.2810 | ±0.5620 | **+2.143** | **0.0321** | * |
| Education: high school or below (vs college) | +0.5085 | 0.4550 | ±0.9100 | +1.118 | 0.2637 |  |
| **Site: UCSD (vs UAB)** | **+3.0922** | 0.3426 | ±0.6851 | **+9.027** | **1.77e-19** | *** |
| **Site: UW (vs UAB)** | **-1.3886** | 0.3169 | ±0.6339 | **-4.381** | **1.18e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7920** | 0.3671 | ±0.7342 | **-4.882** | **1.05e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8581** | 0.3809 | ±0.7618 | **+4.878** | **1.07e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7029** | 0.3910 | ±0.7819 | **-14.587** | **3.40e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0124 | ±0.0249 | **-3.880** | **1.05e-04** | *** |
| BMI (kg/m2) | -0.0183 | 0.0199 | ±0.0397 | -0.921 | 0.3569 |  |
| Hypertension | -0.0589 | 0.2938 | ±0.5876 | -0.200 | 0.8412 |  |
| **High cholesterol** | **-0.7806** | 0.2751 | ±0.5502 | **-2.837** | **0.0045** | ** |
| Kidney disease | +0.6659 | 0.4192 | ±0.8384 | +1.588 | 0.1122 |  |
| Circulatory disease | +0.2137 | 0.3673 | ±0.7345 | +0.582 | 0.5606 |  |
| **Avg. daily time < 54 (%)** | **-0.6104** | 0.3041 | ±0.6081 | **-2.007** | **0.0447** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.2465**, Adj R² = **0.2415**, F-statistic = **48.73** (p = **2.86e-117**), Residual SE = **5.971** on **2085** df, AIC = **13479.2**, BIC = **13564.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5344** | 1.0721 | ±2.1442 | **+46.204** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6040** | 0.2813 | ±0.5625 | **+2.147** | **0.0318** | * |
| Education: high school or below (vs college) | +0.5298 | 0.4551 | ±0.9103 | +1.164 | 0.2444 |  |
| **Site: UCSD (vs UAB)** | **+3.1280** | 0.3432 | ±0.6864 | **+9.114** | **7.95e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3524** | 0.3163 | ±0.6327 | **-4.275** | **1.91e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7831** | 0.3673 | ±0.7347 | **-4.854** | **1.21e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8496** | 0.3806 | ±0.7612 | **+4.860** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7051** | 0.3912 | ±0.7824 | **-14.584** | **3.57e-48** | *** |
| **Age (years)** | **-0.0485** | 0.0125 | ±0.0249 | **-3.896** | **9.77e-05** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0399 | -0.903 | 0.3665 |  |
| Hypertension | -0.0540 | 0.2939 | ±0.5878 | -0.184 | 0.8542 |  |
| **High cholesterol** | **-0.7653** | 0.2753 | ±0.5505 | **-2.781** | **0.0054** | ** |
| Kidney disease | +0.6626 | 0.4195 | ±0.8390 | +1.579 | 0.1142 |  |
| Circulatory disease | +0.2016 | 0.3678 | ±0.7356 | +0.548 | 0.5835 |  |
| Time 54-69, pooled (%) | -0.1018 | 0.0923 | ±0.1847 | -1.102 | 0.2703 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.2466**, Adj R² = **0.2415**, F-statistic = **48.75** (p = **2.64e-117**), Residual SE = **5.970** on **2085** df, AIC = **13479.1**, BIC = **13563.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5173** | 1.0695 | ±2.1390 | **+46.300** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6014** | 0.2814 | ±0.5627 | **+2.138** | **0.0325** | * |
| Education: high school or below (vs college) | +0.5300 | 0.4550 | ±0.9099 | +1.165 | 0.2440 |  |
| **Site: UCSD (vs UAB)** | **+3.1312** | 0.3428 | ±0.6856 | **+9.135** | **6.55e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3545** | 0.3164 | ±0.6328 | **-4.281** | **1.86e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7831** | 0.3674 | ±0.7347 | **-4.854** | **1.21e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8489** | 0.3806 | ±0.7612 | **+4.858** | **1.19e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7024** | 0.3911 | ±0.7822 | **-14.580** | **3.75e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0124 | ±0.0249 | **-3.879** | **1.05e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0398 | -0.902 | 0.3672 |  |
| Hypertension | -0.0547 | 0.2938 | ±0.5876 | -0.186 | 0.8524 |  |
| **High cholesterol** | **-0.7647** | 0.2751 | ±0.5503 | **-2.779** | **0.0054** | ** |
| Kidney disease | +0.6619 | 0.4194 | ±0.8388 | +1.578 | 0.1145 |  |
| Circulatory disease | +0.2005 | 0.3677 | ±0.7355 | +0.545 | 0.5856 |  |
| Avg. daily time 54-69 (%) | -0.1070 | 0.0908 | ±0.1816 | -1.179 | 0.2384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.2468**, Adj R² = **0.2418**, F-statistic = **48.80** (p = **1.95e-117**), Residual SE = **5.969** on **2085** df, AIC = **13478.4**, BIC = **13563.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5734** | 1.0725 | ±2.1449 | **+46.224** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6017** | 0.2811 | ±0.5623 | **+2.140** | **0.0323** | * |
| Education: high school or below (vs college) | +0.5199 | 0.4552 | ±0.9104 | +1.142 | 0.2534 |  |
| **Site: UCSD (vs UAB)** | **+3.1111** | 0.3437 | ±0.6873 | **+9.053** | **1.40e-19** | *** |
| **Site: UW (vs UAB)** | **-1.3664** | 0.3164 | ±0.6329 | **-4.318** | **1.57e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7859** | 0.3673 | ±0.7347 | **-4.862** | **1.16e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8508** | 0.3806 | ±0.7612 | **+4.863** | **1.16e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7051** | 0.3912 | ±0.7825 | **-14.583** | **3.63e-48** | *** |
| **Age (years)** | **-0.0486** | 0.0124 | ±0.0249 | **-3.908** | **9.31e-05** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0399 | -0.901 | 0.3674 |  |
| Hypertension | -0.0567 | 0.2939 | ±0.5879 | -0.193 | 0.8471 |  |
| **High cholesterol** | **-0.7720** | 0.2754 | ±0.5508 | **-2.803** | **0.0051** | ** |
| Kidney disease | +0.6623 | 0.4194 | ±0.8389 | +1.579 | 0.1143 |  |
| Circulatory disease | +0.2054 | 0.3679 | ±0.7357 | +0.558 | 0.5766 |  |
| Time < 70 (%) | -0.1051 | 0.0746 | ±0.1492 | -1.409 | 0.1588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.2469**, Adj R² = **0.2418**, F-statistic = **48.82** (p = **1.80e-117**), Residual SE = **5.969** on **2085** df, AIC = **13478.3**, BIC = **13563.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5403** | 1.0687 | ±2.1374 | **+46.355** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.5979** | 0.2813 | ±0.5625 | **+2.126** | **0.0335** | * |
| Education: high school or below (vs college) | +0.5218 | 0.4549 | ±0.9098 | +1.147 | 0.2513 |  |
| **Site: UCSD (vs UAB)** | **+3.1183** | 0.3430 | ±0.6860 | **+9.092** | **9.75e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3677** | 0.3165 | ±0.6330 | **-4.321** | **1.55e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7860** | 0.3673 | ±0.7347 | **-4.862** | **1.16e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8498** | 0.3806 | ±0.7612 | **+4.861** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7011** | 0.3911 | ±0.7822 | **-14.578** | **3.89e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0124 | ±0.0249 | **-3.879** | **1.05e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0199 | ±0.0398 | -0.900 | 0.3679 |  |
| Hypertension | -0.0575 | 0.2938 | ±0.5876 | -0.196 | 0.8448 |  |
| **High cholesterol** | **-0.7701** | 0.2752 | ±0.5504 | **-2.798** | **0.0051** | ** |
| Kidney disease | +0.6626 | 0.4194 | ±0.8388 | +1.580 | 0.1141 |  |
| Circulatory disease | +0.2038 | 0.3676 | ±0.7353 | +0.554 | 0.5792 |  |
| Avg. daily time < 70 (%) | -0.1111 | 0.0755 | ±0.1510 | -1.471 | 0.1413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.26e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4065** | 1.6600 | ±3.3200 | **+29.763** | **1.18e-194** | *** |
| **Education: graduate level (vs college)** | **+0.6175** | 0.2812 | ±0.5624 | **+2.196** | **0.0281** | * |
| Education: high school or below (vs college) | +0.5510 | 0.4594 | ±0.9189 | +1.199 | 0.2305 |  |
| **Site: UCSD (vs UAB)** | **+3.1571** | 0.3432 | ±0.6864 | **+9.199** | **3.63e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3234** | 0.3181 | ±0.6361 | **-4.161** | **3.17e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7773** | 0.3676 | ±0.7353 | **-4.834** | **1.34e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8516** | 0.3808 | ±0.7617 | **+4.862** | **1.16e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7087** | 0.3911 | ±0.7821 | **-14.598** | **2.91e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.882** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0200 | ±0.0400 | -0.919 | 0.3581 |  |
| Hypertension | -0.0447 | 0.2939 | ±0.5878 | -0.152 | 0.8790 |  |
| **High cholesterol** | **-0.7534** | 0.2747 | ±0.5494 | **-2.742** | **0.0061** | ** |
| Kidney disease | +0.6630 | 0.4207 | ±0.8415 | +1.576 | 0.1151 |  |
| Circulatory disease | +0.1967 | 0.3675 | ±0.7351 | +0.535 | 0.5926 |  |
| Time 54-250, pooled (%) | +0.0004 | 0.0126 | ±0.0251 | +0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.26e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4322** | 1.6953 | ±3.3906 | **+29.159** | **6.52e-187** | *** |
| **Education: graduate level (vs college)** | **+0.6178** | 0.2812 | ±0.5625 | **+2.197** | **0.0280** | * |
| Education: high school or below (vs college) | +0.5500 | 0.4596 | ±0.9192 | +1.197 | 0.2314 |  |
| **Site: UCSD (vs UAB)** | **+3.1576** | 0.3432 | ±0.6864 | **+9.200** | **3.58e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3229** | 0.3180 | ±0.6360 | **-4.160** | **3.19e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7771** | 0.3676 | ±0.7352 | **-4.835** | **1.33e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8520** | 0.3808 | ±0.7615 | **+4.864** | **1.15e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7086** | 0.3911 | ±0.7822 | **-14.597** | **2.94e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.881** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0200 | ±0.0400 | -0.920 | 0.3578 |  |
| Hypertension | -0.0451 | 0.2939 | ±0.5877 | -0.153 | 0.8781 |  |
| **High cholesterol** | **-0.7535** | 0.2747 | ±0.5495 | **-2.742** | **0.0061** | ** |
| Kidney disease | +0.6623 | 0.4209 | ±0.8417 | +1.574 | 0.1156 |  |
| Circulatory disease | +0.1964 | 0.3675 | ±0.7351 | +0.534 | 0.5931 |  |
| Avg. daily time 54-250 (%) | +0.0001 | 0.0129 | ±0.0258 | +0.010 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2412**, F-statistic = **48.65** (p = **4.34e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.1**, BIC = **13564.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4149** | 1.0687 | ±2.1375 | **+46.236** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6141** | 0.2813 | ±0.5626 | **+2.183** | **0.0290** | * |
| Education: high school or below (vs college) | +0.5732 | 0.4566 | ±0.9132 | +1.255 | 0.2094 |  |
| **Site: UCSD (vs UAB)** | **+3.1446** | 0.3429 | ±0.6858 | **+9.171** | **4.69e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3275** | 0.3164 | ±0.6327 | **-4.196** | **2.71e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7782** | 0.3672 | ±0.7344 | **-4.842** | **1.28e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8547** | 0.3808 | ±0.7616 | **+4.871** | **1.11e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7103** | 0.3911 | ±0.7822 | **-14.600** | **2.79e-48** | *** |
| **Age (years)** | **-0.0476** | 0.0125 | ±0.0251 | **-3.803** | **1.43e-04** | *** |
| BMI (kg/m2) | -0.0174 | 0.0200 | ±0.0400 | -0.869 | 0.3848 |  |
| Hypertension | -0.0330 | 0.2942 | ±0.5883 | -0.112 | 0.9108 |  |
| **High cholesterol** | **-0.7431** | 0.2752 | ±0.5504 | **-2.700** | **0.0069** | ** |
| Kidney disease | +0.6940 | 0.4217 | ±0.8435 | +1.646 | 0.0999 | . |
| Circulatory disease | +0.2016 | 0.3677 | ±0.7354 | +0.548 | 0.5835 |  |
| Time 181-250, pooled (%) | -0.0066 | 0.0108 | ±0.0217 | -0.609 | 0.5423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.64** (p = **4.48e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.1**, BIC = **13564.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4180** | 1.0685 | ±2.1370 | **+46.249** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6147** | 0.2813 | ±0.5626 | **+2.186** | **0.0289** | * |
| Education: high school or below (vs college) | +0.5717 | 0.4565 | ±0.9130 | +1.252 | 0.2105 |  |
| **Site: UCSD (vs UAB)** | **+3.1449** | 0.3431 | ±0.6862 | **+9.166** | **4.89e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3277** | 0.3165 | ±0.6329 | **-4.196** | **2.72e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7778** | 0.3672 | ±0.7344 | **-4.841** | **1.29e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8545** | 0.3808 | ±0.7616 | **+4.870** | **1.11e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7097** | 0.3911 | ±0.7822 | **-14.598** | **2.88e-48** | *** |
| **Age (years)** | **-0.0477** | 0.0125 | ±0.0250 | **-3.813** | **1.37e-04** | *** |
| BMI (kg/m2) | -0.0175 | 0.0200 | ±0.0400 | -0.873 | 0.3828 |  |
| Hypertension | -0.0340 | 0.2941 | ±0.5883 | -0.116 | 0.9080 |  |
| **High cholesterol** | **-0.7439** | 0.2752 | ±0.5505 | **-2.703** | **0.0069** | ** |
| Kidney disease | +0.6914 | 0.4216 | ±0.8432 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.2009 | 0.3678 | ±0.7355 | +0.546 | 0.5849 |  |
| Avg. daily time 181-250 (%) | -0.0060 | 0.0107 | ±0.0213 | -0.559 | 0.5758 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.92e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4391** | 1.0682 | ±2.1363 | **+46.285** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6134** | 0.2813 | ±0.5627 | **+2.180** | **0.0292** | * |
| Education: high school or below (vs college) | +0.5671 | 0.4589 | ±0.9177 | +1.236 | 0.2165 |  |
| **Site: UCSD (vs UAB)** | **+3.1486** | 0.3437 | ±0.6873 | **+9.162** | **5.10e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3290** | 0.3174 | ±0.6348 | **-4.187** | **2.83e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7784** | 0.3674 | ±0.7349 | **-4.840** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8493** | 0.3806 | ±0.7613 | **+4.859** | **1.18e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7099** | 0.3911 | ±0.7822 | **-14.600** | **2.81e-48** | *** |
| **Age (years)** | **-0.0482** | 0.0125 | ±0.0250 | **-3.851** | **1.17e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0201 | ±0.0401 | -0.890 | 0.3733 |  |
| Hypertension | -0.0376 | 0.2941 | ±0.5882 | -0.128 | 0.8982 |  |
| **High cholesterol** | **-0.7488** | 0.2750 | ±0.5501 | **-2.723** | **0.0065** | ** |
| Kidney disease | +0.6804 | 0.4220 | ±0.8440 | +1.612 | 0.1069 |  |
| Circulatory disease | +0.2007 | 0.3678 | ±0.7355 | +0.546 | 0.5853 |  |
| Time > 180 (%) | -0.0025 | 0.0070 | ±0.0139 | -0.352 | 0.7249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.62** (p = **4.99e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4388** | 1.0683 | ±2.1366 | **+46.278** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6141** | 0.2813 | ±0.5627 | **+2.183** | **0.0291** | * |
| Education: high school or below (vs college) | +0.5654 | 0.4588 | ±0.9177 | +1.232 | 0.2179 |  |
| **Site: UCSD (vs UAB)** | **+3.1493** | 0.3438 | ±0.6877 | **+9.159** | **5.24e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3284** | 0.3174 | ±0.6349 | **-4.185** | **2.86e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7780** | 0.3674 | ±0.7348 | **-4.839** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8499** | 0.3806 | ±0.7612 | **+4.860** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7095** | 0.3911 | ±0.7822 | **-14.598** | **2.87e-48** | *** |
| **Age (years)** | **-0.0482** | 0.0125 | ±0.0250 | **-3.853** | **1.16e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0201 | ±0.0401 | -0.893 | 0.3721 |  |
| Hypertension | -0.0385 | 0.2940 | ±0.5881 | -0.131 | 0.8958 |  |
| **High cholesterol** | **-0.7493** | 0.2751 | ±0.5502 | **-2.724** | **0.0065** | ** |
| Kidney disease | +0.6788 | 0.4220 | ±0.8440 | +1.608 | 0.1077 |  |
| Circulatory disease | +0.2003 | 0.3678 | ±0.7356 | +0.545 | 0.5861 |  |
| Avg. daily time > 180 (%) | -0.0022 | 0.0070 | ±0.0139 | -0.315 | 0.7528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2412**, F-statistic = **48.65** (p = **4.28e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.0**, BIC = **13564.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4319** | 1.0680 | ±2.1360 | **+46.285** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6070** | 0.2814 | ±0.5629 | **+2.157** | **0.0310** | * |
| Education: high school or below (vs college) | +0.5783 | 0.4586 | ±0.9172 | +1.261 | 0.2073 |  |
| **Site: UCSD (vs UAB)** | **+3.1414** | 0.3437 | ±0.6873 | **+9.141** | **6.20e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3324** | 0.3171 | ±0.6343 | **-4.201** | **2.65e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7757** | 0.3672 | ±0.7343 | **-4.836** | **1.32e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8466** | 0.3806 | ±0.7613 | **+4.851** | **1.23e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7070** | 0.3912 | ±0.7825 | **-14.587** | **3.39e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0125 | ±0.0250 | **-3.869** | **1.09e-04** | *** |
| BMI (kg/m2) | -0.0170 | 0.0201 | ±0.0403 | -0.844 | 0.3985 |  |
| Hypertension | -0.0363 | 0.2940 | ±0.5880 | -0.123 | 0.9018 |  |
| **High cholesterol** | **-0.7466** | 0.2751 | ±0.5501 | **-2.714** | **0.0066** | ** |
| Kidney disease | +0.6868 | 0.4212 | ±0.8423 | +1.631 | 0.1030 |  |
| Circulatory disease | +0.2029 | 0.3675 | ±0.7350 | +0.552 | 0.5809 |  |
| Nocturnal time > 180 (%) | -0.0043 | 0.0069 | ±0.0138 | -0.628 | 0.5303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2470**, Adj R² = **0.2419**, F-statistic = **48.85** (p = **1.53e-117**), Residual SE = **5.969** on **2085** df, AIC = **13477.9**, BIC = **13562.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4935** | 1.0660 | ±2.1320 | **+46.430** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.5927** | 0.2813 | ±0.5627 | **+2.107** | **0.0351** | * |
| Education: high school or below (vs college) | +0.5852 | 0.4572 | ±0.9143 | +1.280 | 0.2005 |  |
| **Site: UCSD (vs UAB)** | **+3.1351** | 0.3413 | ±0.6826 | **+9.186** | **4.10e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3312** | 0.3160 | ±0.6321 | **-4.212** | **2.53e-05** | *** |
| **Season: spring (vs autumn)** | **-1.8011** | 0.3668 | ±0.7336 | **-4.910** | **9.10e-07** | *** |
| **Season: summer (vs autumn)** | **+1.8485** | 0.3803 | ±0.7607 | **+4.860** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7336** | 0.3909 | ±0.7818 | **-14.667** | **1.04e-48** | *** |
| **Age (years)** | **-0.0465** | 0.0125 | ±0.0250 | **-3.716** | **2.03e-04** | *** |
| BMI (kg/m2) | -0.0187 | 0.0198 | ±0.0397 | -0.942 | 0.3461 |  |
| Hypertension | -0.0055 | 0.2937 | ±0.5874 | -0.019 | 0.9852 |  |
| **High cholesterol** | **-0.7273** | 0.2749 | ±0.5497 | **-2.646** | **0.0081** | ** |
| Kidney disease | +0.7278 | 0.4219 | ±0.8438 | +1.725 | 0.0845 | . |
| Circulatory disease | +0.1968 | 0.3675 | ±0.7349 | +0.536 | 0.5923 |  |
| Any reading > 250 during wear (0/1) | -0.4405 | 0.2793 | ±0.5587 | -1.577 | 0.1148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.25e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4429** | 1.0671 | ±2.1343 | **+46.332** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6188** | 0.2812 | ±0.5624 | **+2.200** | **0.0278** | * |
| Education: high school or below (vs college) | +0.5473 | 0.4595 | ±0.9191 | +1.191 | 0.2337 |  |
| **Site: UCSD (vs UAB)** | **+3.1590** | 0.3430 | ±0.6860 | **+9.210** | **3.27e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3215** | 0.3179 | ±0.6359 | **-4.156** | **3.23e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7769** | 0.3676 | ±0.7353 | **-4.833** | **1.34e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8532** | 0.3809 | ±0.7617 | **+4.866** | **1.14e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7084** | 0.3911 | ±0.7821 | **-14.597** | **2.92e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.880** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0200 | ±0.0400 | -0.923 | 0.3563 |  |
| Hypertension | -0.0460 | 0.2939 | ±0.5878 | -0.157 | 0.8756 |  |
| **High cholesterol** | **-0.7537** | 0.2747 | ±0.5495 | **-2.743** | **0.0061** | ** |
| Kidney disease | +0.6603 | 0.4206 | ±0.8413 | +1.570 | 0.1165 |  |
| Circulatory disease | +0.1956 | 0.3676 | ±0.7352 | +0.532 | 0.5946 |  |
| Time > 250 (%) | +0.0007 | 0.0125 | ±0.0251 | +0.052 | 0.9586 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.25e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4428** | 1.0671 | ±2.1343 | **+46.332** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6190** | 0.2812 | ±0.5624 | **+2.201** | **0.0277** | * |
| Education: high school or below (vs college) | +0.5466 | 0.4597 | ±0.9193 | +1.189 | 0.2344 |  |
| **Site: UCSD (vs UAB)** | **+3.1594** | 0.3431 | ±0.6861 | **+9.209** | **3.28e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3211** | 0.3179 | ±0.6358 | **-4.156** | **3.24e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7769** | 0.3676 | ±0.7352 | **-4.834** | **1.34e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8534** | 0.3808 | ±0.7616 | **+4.867** | **1.13e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7084** | 0.3911 | ±0.7821 | **-14.597** | **2.93e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.880** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0185 | 0.0200 | ±0.0400 | -0.923 | 0.3560 |  |
| Hypertension | -0.0462 | 0.2939 | ±0.5877 | -0.157 | 0.8750 |  |
| **High cholesterol** | **-0.7538** | 0.2748 | ±0.5495 | **-2.743** | **0.0061** | ** |
| Kidney disease | +0.6596 | 0.4208 | ±0.8416 | +1.568 | 0.1170 |  |
| Circulatory disease | +0.1954 | 0.3676 | ±0.7352 | +0.532 | 0.5950 |  |
| Avg. daily time > 250 (%) | +0.0009 | 0.0129 | ±0.0258 | +0.067 | 0.9469 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0430**, F-statistic = **8.26** (p = **1.76e-16**), Residual SE = **16.020** on **2086** df, AIC = **17623.6**, BIC = **17702.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2419** | 3.2063 | ±6.4126 | **+39.061** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6093** | 0.7264 | ±1.4529 | **-2.215** | **0.0267** | * |
| **Education: high school or below (vs college)** | **+5.0469** | 1.3740 | ±2.7481 | **+3.673** | **2.40e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1622** | 0.9550 | ±1.9099 | **+2.264** | **0.0236** | * |
| Site: UW (vs UAB) | -0.9890 | 0.8558 | ±1.7117 | -1.156 | 0.2479 |  |
| **Season: spring (vs autumn)** | **+2.7791** | 0.9194 | ±1.8387 | **+3.023** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9774 | 1.0279 | ±2.0558 | +1.924 | 0.0544 | . |
| **Season: winter (vs autumn)** | **+4.2719** | 1.0344 | ±2.0687 | **+4.130** | **3.63e-05** | *** |
| **Age (years)** | **-0.1118** | 0.0356 | ±0.0713 | **-3.137** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1778** | 0.0541 | ±0.1083 | **+3.284** | **0.0010** | ** |
| Hypertension | +1.0969 | 0.7963 | ±1.5926 | +1.377 | 0.1684 |  |
| High cholesterol | -0.0469 | 0.7479 | ±1.4958 | -0.063 | 0.9500 |  |
| Kidney disease | -1.5921 | 1.1144 | ±2.2287 | -1.429 | 0.1531 |  |
| Circulatory disease | +0.1221 | 1.0355 | ±2.0711 | +0.118 | 0.9061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.0499**, Adj R² = **0.0435**, F-statistic = **7.82** (p = **2.17e-16**), Residual SE = **16.016** on **2085** df, AIC = **17623.7**, BIC = **17708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7616** | 3.8103 | ±7.6206 | **+33.531** | **1.72e-246** | *** |
| **Education: graduate level (vs college)** | **-1.6673** | 0.7221 | ±1.4443 | **-2.309** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+5.2497** | 1.3811 | ±2.7621 | **+3.801** | **1.44e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1089** | 0.9543 | ±1.9087 | **+2.210** | **0.0271** | * |
| Site: UW (vs UAB) | -1.0538 | 0.8530 | ±1.7059 | -1.235 | 0.2167 |  |
| **Season: spring (vs autumn)** | **+2.7118** | 0.9214 | ±1.8428 | **+2.943** | **0.0032** | ** |
| Season: summer (vs autumn) | +1.9507 | 1.0288 | ±2.0576 | +1.896 | 0.0579 | . |
| **Season: winter (vs autumn)** | **+4.2391** | 1.0382 | ±2.0765 | **+4.083** | **4.44e-05** | *** |
| **Age (years)** | **-0.1091** | 0.0358 | ±0.0716 | **-3.047** | **0.0023** | ** |
| **BMI (kg/m2)** | **+0.1866** | 0.0542 | ±0.1085 | **+3.439** | **5.83e-04** | *** |
| Hypertension | +1.2006 | 0.8069 | ±1.6137 | +1.488 | 0.1368 |  |
| High cholesterol | +0.0441 | 0.7539 | ±1.5078 | +0.058 | 0.9534 |  |
| Kidney disease | -1.5040 | 1.1098 | ±2.2196 | -1.355 | 0.1754 |  |
| Circulatory disease | +0.1669 | 1.0354 | ±2.0707 | +0.161 | 0.8719 |  |
| HbA1c (%) | -0.4903 | 0.4122 | ±0.8244 | -1.190 | 0.2342 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.0495**, Adj R² = **0.0431**, F-statistic = **7.75** (p = **3.15e-16**), Residual SE = **16.020** on **2085** df, AIC = **17624.5**, BIC = **17709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4837** | 3.5747 | ±7.1494 | **+35.383** | **3.12e-274** | *** |
| **Education: graduate level (vs college)** | **-1.6354** | 0.7238 | ±1.4475 | **-2.260** | **0.0239** | * |
| **Education: high school or below (vs college)** | **+5.1856** | 1.3791 | ±2.7581 | **+3.760** | **1.70e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1061** | 0.9588 | ±1.9177 | **+2.197** | **0.0281** | * |
| Site: UW (vs UAB) | -1.0197 | 0.8553 | ±1.7105 | -1.192 | 0.2332 |  |
| **Season: spring (vs autumn)** | **+2.7692** | 0.9203 | ±1.8407 | **+3.009** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9561 | 1.0296 | ±2.0592 | +1.900 | 0.0575 | . |
| **Season: winter (vs autumn)** | **+4.2525** | 1.0381 | ±2.0761 | **+4.097** | **4.19e-05** | *** |
| **Age (years)** | **-0.1100** | 0.0357 | ±0.0714 | **-3.084** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1077 | **+3.385** | **7.11e-04** | *** |
| Hypertension | +1.1754 | 0.8088 | ±1.6176 | +1.453 | 0.1461 |  |
| High cholesterol | -0.0012 | 0.7527 | ±1.5055 | -0.002 | 0.9987 |  |
| Kidney disease | -1.4654 | 1.1164 | ±2.2327 | -1.313 | 0.1893 |  |
| Circulatory disease | +0.1556 | 1.0352 | ±2.0703 | +0.150 | 0.8805 |  |
| Mean glucose (mg/dL) | -0.0114 | 0.0125 | ±0.0250 | -0.910 | 0.3629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.0495**, Adj R² = **0.0431**, F-statistic = **7.75** (p = **3.15e-16**), Residual SE = **16.020** on **2085** df, AIC = **17624.5**, BIC = **17709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0563** | 4.6099 | ±9.2199 | **+27.778** | **7.93e-170** | *** |
| **Education: graduate level (vs college)** | **-1.6354** | 0.7238 | ±1.4475 | **-2.260** | **0.0239** | * |
| **Education: high school or below (vs college)** | **+5.1856** | 1.3791 | ±2.7581 | **+3.760** | **1.70e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1061** | 0.9588 | ±1.9177 | **+2.197** | **0.0281** | * |
| Site: UW (vs UAB) | -1.0197 | 0.8553 | ±1.7105 | -1.192 | 0.2332 |  |
| **Season: spring (vs autumn)** | **+2.7692** | 0.9203 | ±1.8407 | **+3.009** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9561 | 1.0296 | ±2.0592 | +1.900 | 0.0575 | . |
| **Season: winter (vs autumn)** | **+4.2525** | 1.0381 | ±2.0761 | **+4.097** | **4.19e-05** | *** |
| **Age (years)** | **-0.1100** | 0.0357 | ±0.0714 | **-3.084** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1077 | **+3.385** | **7.11e-04** | *** |
| Hypertension | +1.1754 | 0.8088 | ±1.6176 | +1.453 | 0.1461 |  |
| High cholesterol | -0.0012 | 0.7527 | ±1.5055 | -0.002 | 0.9987 |  |
| Kidney disease | -1.4654 | 1.1164 | ±2.2327 | -1.313 | 0.1893 |  |
| Circulatory disease | +0.1556 | 1.0352 | ±2.0703 | +0.150 | 0.8805 |  |
| GMI (%) | -0.4751 | 0.5222 | ±1.0443 | -0.910 | 0.3629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.0497**, Adj R² = **0.0433**, F-statistic = **7.78** (p = **2.66e-16**), Residual SE = **16.018** on **2085** df, AIC = **17624.1**, BIC = **17708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6730** | 3.6717 | ±7.3435 | **+34.500** | **8.15e-261** | *** |
| **Education: graduate level (vs college)** | **-1.6439** | 0.7238 | ±1.4477 | **-2.271** | **0.0231** | * |
| **Education: high school or below (vs college)** | **+5.1996** | 1.3706 | ±2.7411 | **+3.794** | **1.48e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1135** | 0.9581 | ±1.9161 | **+2.206** | **0.0274** | * |
| Site: UW (vs UAB) | -1.0103 | 0.8553 | ±1.7106 | -1.181 | 0.2375 |  |
| **Season: spring (vs autumn)** | **+2.7879** | 0.9195 | ±1.8390 | **+3.032** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9535 | 1.0294 | ±2.0588 | +1.898 | 0.0577 | . |
| **Season: winter (vs autumn)** | **+4.2691** | 1.0344 | ±2.0687 | **+4.127** | **3.67e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0357 | ±0.0714 | **-3.126** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1859** | 0.0537 | ±0.1074 | **+3.462** | **5.37e-04** | *** |
| Hypertension | +1.1700 | 0.8080 | ±1.6160 | +1.448 | 0.1476 |  |
| High cholesterol | +0.0094 | 0.7555 | ±1.5110 | +0.012 | 0.9901 |  |
| Kidney disease | -1.4933 | 1.1165 | ±2.2329 | -1.338 | 0.1810 |  |
| Circulatory disease | +0.1522 | 1.0345 | ±2.0689 | +0.147 | 0.8830 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0132 | 0.0137 | ±0.0274 | -0.966 | 0.3341 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.13e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3356** | 3.2433 | ±6.4867 | **+38.644** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6168** | 0.7234 | ±1.4468 | **-2.235** | **0.0254** | * |
| **Education: high school or below (vs college)** | **+5.0673** | 1.3758 | ±2.7517 | **+3.683** | **2.30e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1500** | 0.9622 | ±1.9244 | **+2.235** | **0.0254** | * |
| Site: UW (vs UAB) | -0.9989 | 0.8552 | ±1.7104 | -1.168 | 0.2428 |  |
| **Season: spring (vs autumn)** | **+2.7767** | 0.9198 | ±1.8396 | **+3.019** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9747 | 1.0288 | ±2.0577 | +1.919 | 0.0549 | . |
| **Season: winter (vs autumn)** | **+4.2687** | 1.0376 | ±2.0753 | **+4.114** | **3.89e-05** | *** |
| **Age (years)** | **-0.1113** | 0.0360 | ±0.0721 | **-3.089** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1783** | 0.0542 | ±0.1084 | **+3.291** | **9.97e-04** | *** |
| Hypertension | +1.1117 | 0.8054 | ±1.6108 | +1.380 | 0.1675 |  |
| High cholesterol | -0.0414 | 0.7526 | ±1.5051 | -0.055 | 0.9561 |  |
| Kidney disease | -1.5571 | 1.1199 | ±2.2398 | -1.390 | 0.1644 |  |
| Circulatory disease | +0.1284 | 1.0339 | ±2.0677 | +0.124 | 0.9011 |  |
| Glucose SD, pooled (mg/dL) | -0.0054 | 0.0361 | ±0.0722 | -0.150 | 0.8808 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.11e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1318** | 3.2468 | ±6.4937 | **+38.540** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6017** | 0.7245 | ±1.4491 | **-2.211** | **0.0271** | * |
| **Education: high school or below (vs college)** | **+5.0223** | 1.3738 | ±2.7475 | **+3.656** | **2.56e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1756** | 0.9590 | ±1.9180 | **+2.269** | **0.0233** | * |
| Site: UW (vs UAB) | -0.9787 | 0.8558 | ±1.7116 | -1.144 | 0.2528 |  |
| **Season: spring (vs autumn)** | **+2.7825** | 0.9198 | ±1.8396 | **+3.025** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9820 | 1.0290 | ±2.0580 | +1.926 | 0.0541 | . |
| **Season: winter (vs autumn)** | **+4.2773** | 1.0378 | ±2.0757 | **+4.121** | **3.77e-05** | *** |
| **Age (years)** | **-0.1125** | 0.0360 | ±0.0719 | **-3.127** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1773** | 0.0541 | ±0.1083 | **+3.276** | **0.0011** | ** |
| Hypertension | +1.0800 | 0.8054 | ±1.6109 | +1.341 | 0.1799 |  |
| High cholesterol | -0.0534 | 0.7512 | ±1.5024 | -0.071 | 0.9433 |  |
| Kidney disease | -1.6335 | 1.1205 | ±2.2409 | -1.458 | 0.1449 |  |
| Circulatory disease | +0.1162 | 1.0348 | ±2.0695 | +0.112 | 0.9106 |  |
| Avg. daily SD (mg/dL) | +0.0070 | 0.0366 | ±0.0732 | +0.193 | 0.8473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.51e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.3**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6218** | 3.2492 | ±6.4985 | **+38.354** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5859** | 0.7265 | ±1.4530 | **-2.183** | **0.0290** | * |
| **Education: high school or below (vs college)** | **+5.0110** | 1.3734 | ±2.7469 | **+3.649** | **2.64e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2001** | 0.9598 | ±1.9196 | **+2.292** | **0.0219** | * |
| Site: UW (vs UAB) | -0.9548 | 0.8555 | ±1.7110 | -1.116 | 0.2644 |  |
| **Season: spring (vs autumn)** | **+2.7900** | 0.9189 | ±1.8378 | **+3.036** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9776 | 1.0282 | ±2.0564 | +1.923 | 0.0544 | . |
| **Season: winter (vs autumn)** | **+4.2791** | 1.0353 | ±2.0706 | **+4.133** | **3.58e-05** | *** |
| **Age (years)** | **-0.1137** | 0.0363 | ±0.0726 | **-3.132** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1773** | 0.0542 | ±0.1085 | **+3.269** | **0.0011** | ** |
| Hypertension | +1.0578 | 0.7980 | ±1.5961 | +1.326 | 0.1850 |  |
| High cholesterol | -0.0515 | 0.7490 | ±1.4979 | -0.069 | 0.9452 |  |
| Kidney disease | -1.6975 | 1.1143 | ±2.2286 | -1.523 | 0.1277 |  |
| Circulatory disease | +0.1066 | 1.0347 | ±2.0694 | +0.103 | 0.9179 |  |
| CV (%) | +0.0385 | 0.0689 | ±0.1379 | +0.558 | 0.5766 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.96e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.5**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7960** | 3.8070 | ±7.6140 | **+33.043** | **1.95e-239** | *** |
| **Education: graduate level (vs college)** | **-1.5960** | 0.7264 | ±1.4528 | **-2.197** | **0.0280** | * |
| **Education: high school or below (vs college)** | **+5.0249** | 1.3728 | ±2.7456 | **+3.660** | **2.52e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1811** | 0.9593 | ±1.9186 | **+2.274** | **0.0230** | * |
| Site: UW (vs UAB) | -0.9752 | 0.8558 | ±1.7117 | -1.139 | 0.2545 |  |
| **Season: spring (vs autumn)** | **+2.7821** | 0.9193 | ±1.8385 | **+3.026** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9747 | 1.0284 | ±2.0569 | +1.920 | 0.0548 | . |
| **Season: winter (vs autumn)** | **+4.2720** | 1.0352 | ±2.0703 | **+4.127** | **3.68e-05** | *** |
| **Age (years)** | **-0.1129** | 0.0363 | ±0.0726 | **-3.110** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.0737 | 0.8000 | ±1.6000 | +1.342 | 0.1795 |  |
| High cholesterol | -0.0512 | 0.7492 | ±1.4984 | -0.068 | 0.9455 |  |
| Kidney disease | -1.6388 | 1.1145 | ±2.2289 | -1.470 | 0.1414 |  |
| Circulatory disease | +0.1129 | 1.0350 | ±2.0700 | +0.109 | 0.9131 |  |
| Mean / SD ratio | -0.0864 | 0.2655 | ±0.5310 | -0.326 | 0.7448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.0492**, Adj R² = **0.0428**, F-statistic = **7.71** (p = **4.09e-16**), Residual SE = **16.022** on **2085** df, AIC = **17625.1**, BIC = **17709.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4757** | 3.7615 | ±7.5230 | **+33.624** | **7.55e-248** | *** |
| **Education: graduate level (vs college)** | **-1.5832** | 0.7273 | ±1.4546 | **-2.177** | **0.0295** | * |
| **Education: high school or below (vs college)** | **+4.9952** | 1.3720 | ±2.7439 | **+3.641** | **2.72e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1920** | 0.9565 | ±1.9130 | **+2.292** | **0.0219** | * |
| Site: UW (vs UAB) | -0.9655 | 0.8565 | ±1.7130 | -1.127 | 0.2596 |  |
| **Season: spring (vs autumn)** | **+2.7904** | 0.9187 | ±1.8375 | **+3.037** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9826 | 1.0279 | ±2.0559 | +1.929 | 0.0538 | . |
| **Season: winter (vs autumn)** | **+4.2792** | 1.0350 | ±2.0700 | **+4.134** | **3.56e-05** | *** |
| **Age (years)** | **-0.1147** | 0.0364 | ±0.0727 | **-3.153** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1772** | 0.0542 | ±0.1084 | **+3.270** | **0.0011** | ** |
| Hypertension | +1.0506 | 0.7981 | ±1.5962 | +1.316 | 0.1881 |  |
| High cholesterol | -0.0542 | 0.7487 | ±1.4974 | -0.072 | 0.9423 |  |
| Kidney disease | -1.6929 | 1.1177 | ±2.2353 | -1.515 | 0.1299 |  |
| Circulatory disease | +0.1144 | 1.0355 | ±2.0711 | +0.110 | 0.9120 |  |
| Avg. daily mean/SD | -0.1637 | 0.2180 | ±0.4360 | -0.751 | 0.4526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.0492**, Adj R² = **0.0429**, F-statistic = **7.71** (p = **4.01e-16**), Residual SE = **16.022** on **2085** df, AIC = **17625.0**, BIC = **17709.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.9920** | 3.4503 | ±6.9005 | **+35.937** | **8.06e-283** | *** |
| **Education: graduate level (vs college)** | **-1.5774** | 0.7243 | ±1.4485 | **-2.178** | **0.0294** | * |
| **Education: high school or below (vs college)** | **+4.9908** | 1.3826 | ±2.7651 | **+3.610** | **3.06e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2130** | 0.9527 | ±1.9054 | **+2.323** | **0.0202** | * |
| Site: UW (vs UAB) | -0.9165 | 0.8525 | ±1.7049 | -1.075 | 0.2823 |  |
| **Season: spring (vs autumn)** | **+2.7898** | 0.9190 | ±1.8381 | **+3.036** | **0.0024** | ** |
| Season: summer (vs autumn) | +2.0045 | 1.0262 | ±2.0524 | +1.953 | 0.0508 | . |
| **Season: winter (vs autumn)** | **+4.2930** | 1.0352 | ±2.0704 | **+4.147** | **3.37e-05** | *** |
| **Age (years)** | **-0.1113** | 0.0356 | ±0.0711 | **-3.131** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1763** | 0.0543 | ±0.1087 | **+3.246** | **0.0012** | ** |
| Hypertension | +1.0801 | 0.7970 | ±1.5941 | +1.355 | 0.1754 |  |
| High cholesterol | -0.0426 | 0.7488 | ±1.4976 | -0.057 | 0.9546 |  |
| Kidney disease | -1.6691 | 1.1101 | ±2.2203 | -1.504 | 0.1327 |  |
| Circulatory disease | +0.1146 | 1.0365 | ±2.0730 | +0.111 | 0.9120 |  |
| MAG (mg/dL/h) | +0.0303 | 0.0426 | ±0.0851 | +0.712 | 0.4762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.68** (p = **4.78e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8675** | 3.3013 | ±6.6026 | **+37.823** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5934** | 0.7246 | ±1.4491 | **-2.199** | **0.0279** | * |
| **Education: high school or below (vs college)** | **+4.9966** | 1.3730 | ±2.7459 | **+3.639** | **2.73e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1926** | 0.9580 | ±1.9159 | **+2.289** | **0.0221** | * |
| Site: UW (vs UAB) | -0.9662 | 0.8548 | ±1.7096 | -1.130 | 0.2583 |  |
| **Season: spring (vs autumn)** | **+2.7845** | 0.9195 | ±1.8389 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9842 | 1.0283 | ±2.0565 | +1.930 | 0.0536 | . |
| **Season: winter (vs autumn)** | **+4.2823** | 1.0373 | ±2.0746 | **+4.128** | **3.65e-05** | *** |
| **Age (years)** | **-0.1130** | 0.0359 | ±0.0718 | **-3.148** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0541 | ±0.1083 | **+3.277** | **0.0010** | ** |
| Hypertension | +1.0670 | 0.8042 | ±1.6084 | +1.327 | 0.1846 |  |
| High cholesterol | -0.0593 | 0.7504 | ±1.5009 | -0.079 | 0.9370 |  |
| Kidney disease | -1.6748 | 1.1171 | ±2.2342 | -1.499 | 0.1338 |  |
| Circulatory disease | +0.1075 | 1.0351 | ±2.0703 | +0.104 | 0.9173 |  |
| Avg. daily range (mg/dL) | +0.0041 | 0.0099 | ±0.0198 | +0.411 | 0.6809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.0499**, Adj R² = **0.0435**, F-statistic = **7.81** (p = **2.19e-16**), Residual SE = **16.016** on **2085** df, AIC = **17623.7**, BIC = **17708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6651** | 3.2216 | ±6.4433 | **+39.007** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6786** | 0.7226 | ±1.4453 | **-2.323** | **0.0202** | * |
| **Education: high school or below (vs college)** | **+5.1487** | 1.3745 | ±2.7490 | **+3.746** | **1.80e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0797** | 0.9674 | ±1.9348 | **+2.150** | **0.0316** | * |
| Site: UW (vs UAB) | -1.0642 | 0.8550 | ±1.7100 | -1.245 | 0.2133 |  |
| **Season: spring (vs autumn)** | **+2.7926** | 0.9204 | ±1.8409 | **+3.034** | **0.0024** | ** |
| Season: summer (vs autumn) | +2.0104 | 1.0289 | ±2.0578 | +1.954 | 0.0507 | . |
| **Season: winter (vs autumn)** | **+4.2888** | 1.0311 | ±2.0623 | **+4.159** | **3.19e-05** | *** |
| **Age (years)** | **-0.1112** | 0.0358 | ±0.0715 | **-3.110** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1846** | 0.0548 | ±0.1097 | **+3.366** | **7.64e-04** | *** |
| Hypertension | +1.1780 | 0.8039 | ±1.6078 | +1.465 | 0.1428 |  |
| High cholesterol | -0.0035 | 0.7561 | ±1.5121 | -0.005 | 0.9963 |  |
| Kidney disease | -1.4209 | 1.1230 | ±2.2460 | -1.265 | 0.2058 |  |
| Circulatory disease | +0.2083 | 1.0295 | ±2.0590 | +0.202 | 0.8396 |  |
| SD of daily means (mg/dL) | -0.0796 | 0.0968 | ±0.1935 | -0.823 | 0.4104 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.70e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.3696** | 3.8105 | ±7.6209 | **+32.639** | **1.15e-233** | *** |
| **Education: graduate level (vs college)** | **-1.6267** | 0.7222 | ±1.4444 | **-2.252** | **0.0243** | * |
| **Education: high school or below (vs college)** | **+5.1060** | 1.3795 | ±2.7590 | **+3.701** | **2.15e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1259** | 0.9602 | ±1.9204 | **+2.214** | **0.0268** | * |
| Site: UW (vs UAB) | -1.0147 | 0.8536 | ±1.7071 | -1.189 | 0.2345 |  |
| **Season: spring (vs autumn)** | **+2.7738** | 0.9203 | ±1.8407 | **+3.014** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9673 | 1.0299 | ±2.0599 | +1.910 | 0.0561 | . |
| **Season: winter (vs autumn)** | **+4.2677** | 1.0371 | ±2.0742 | **+4.115** | **3.87e-05** | *** |
| **Age (years)** | **-0.1109** | 0.0357 | ±0.0714 | **-3.109** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1798** | 0.0538 | ±0.1077 | **+3.338** | **8.43e-04** | *** |
| Hypertension | +1.1227 | 0.8079 | ±1.6158 | +1.390 | 0.1646 |  |
| High cholesterol | -0.0320 | 0.7506 | ±1.5011 | -0.043 | 0.9660 |  |
| Kidney disease | -1.5273 | 1.1205 | ±2.2411 | -1.363 | 0.1729 |  |
| Circulatory disease | +0.1384 | 1.0352 | ±2.0704 | +0.134 | 0.8936 |  |
| Time in range 70-180, pooled (%) | +0.0086 | 0.0222 | ±0.0444 | +0.390 | 0.6968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.56e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.3**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.2480** | 3.8124 | ±7.6247 | **+32.591** | **5.53e-233** | *** |
| **Education: graduate level (vs college)** | **-1.6284** | 0.7224 | ±1.4448 | **-2.254** | **0.0242** | * |
| **Education: high school or below (vs college)** | **+5.1147** | 1.3787 | ±2.7574 | **+3.710** | **2.07e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1205** | 0.9604 | ±1.9209 | **+2.208** | **0.0273** | * |
| Site: UW (vs UAB) | -1.0184 | 0.8536 | ±1.7072 | -1.193 | 0.2329 |  |
| **Season: spring (vs autumn)** | **+2.7743** | 0.9202 | ±1.8404 | **+3.015** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9671 | 1.0297 | ±2.0594 | +1.910 | 0.0561 | . |
| **Season: winter (vs autumn)** | **+4.2688** | 1.0362 | ±2.0724 | **+4.120** | **3.79e-05** | *** |
| **Age (years)** | **-0.1108** | 0.0357 | ±0.0714 | **-3.104** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1801** | 0.0538 | ±0.1076 | **+3.346** | **8.21e-04** | *** |
| Hypertension | +1.1257 | 0.8077 | ±1.6155 | +1.394 | 0.1634 |  |
| High cholesterol | -0.0296 | 0.7508 | ±1.5016 | -0.039 | 0.9686 |  |
| Kidney disease | -1.5173 | 1.1198 | ±2.2396 | -1.355 | 0.1754 |  |
| Circulatory disease | +0.1406 | 1.0353 | ±2.0705 | +0.136 | 0.8920 |  |
| Avg. daily time in range 70-180 (%) | +0.0098 | 0.0222 | ±0.0443 | +0.441 | 0.6593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.0494**, Adj R² = **0.0431**, F-statistic = **7.75** (p = **3.30e-16**), Residual SE = **16.020** on **2085** df, AIC = **17624.6**, BIC = **17709.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6484** | 3.1386 | ±6.2772 | **+40.033** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6263** | 0.7272 | ±1.4543 | **-2.236** | **0.0253** | * |
| **Education: high school or below (vs college)** | **+4.9695** | 1.3718 | ±2.7436 | **+3.623** | **2.92e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0707** | 0.9571 | ±1.9142 | **+2.164** | **0.0305** | * |
| Site: UW (vs UAB) | -1.0406 | 0.8499 | ±1.6998 | -1.224 | 0.2208 |  |
| **Season: spring (vs autumn)** | **+2.7762** | 0.9194 | ±1.8387 | **+3.020** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9565 | 1.0275 | ±2.0551 | +1.904 | 0.0569 | . |
| **Season: winter (vs autumn)** | **+4.2448** | 1.0362 | ±2.0724 | **+4.096** | **4.20e-05** | *** |
| **Age (years)** | **-0.1142** | 0.0352 | ±0.0704 | **-3.244** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.1798** | 0.0545 | ±0.1089 | **+3.302** | **9.60e-04** | *** |
| Hypertension | +1.1039 | 0.7956 | ±1.5912 | +1.387 | 0.1653 |  |
| High cholesterol | -0.0930 | 0.7494 | ±1.4988 | -0.124 | 0.9012 |  |
| Kidney disease | -1.6120 | 1.1175 | ±2.2349 | -1.443 | 0.1491 |  |
| Circulatory disease | +0.1800 | 1.0329 | ±2.0658 | +0.174 | 0.8617 |  |
| Any reading < 54 during wear (0/1) | -0.7848 | 0.7883 | ±1.5766 | -0.996 | 0.3195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.19e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2262** | 3.2086 | ±6.4172 | **+39.028** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6085** | 0.7271 | ±1.4541 | **-2.212** | **0.0269** | * |
| **Education: high school or below (vs college)** | **+5.0509** | 1.3729 | ±2.7457 | **+3.679** | **2.34e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1692** | 0.9596 | ±1.9192 | **+2.261** | **0.0238** | * |
| Site: UW (vs UAB) | -0.9833 | 0.8583 | ±1.7165 | -1.146 | 0.2519 |  |
| **Season: spring (vs autumn)** | **+2.7802** | 0.9199 | ±1.8398 | **+3.022** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9768 | 1.0281 | ±2.0563 | +1.923 | 0.0545 | . |
| **Season: winter (vs autumn)** | **+4.2720** | 1.0348 | ±2.0695 | **+4.129** | **3.65e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0356 | ±0.0713 | **-3.136** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1778** | 0.0542 | ±0.1084 | **+3.281** | **0.0010** | ** |
| Hypertension | +1.0979 | 0.7968 | ±1.5936 | +1.378 | 0.1682 |  |
| High cholesterol | -0.0442 | 0.7486 | ±1.4973 | -0.059 | 0.9530 |  |
| Kidney disease | -1.5920 | 1.1150 | ±2.2301 | -1.428 | 0.1534 |  |
| Circulatory disease | +0.1206 | 1.0358 | ±2.0717 | +0.116 | 0.9073 |  |
| Time < 54 (%) | +0.0459 | 0.6379 | ±1.2757 | +0.072 | 0.9426 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.68** (p = **4.79e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1772** | 3.2053 | ±6.4106 | **+39.053** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6002** | 0.7269 | ±1.4538 | **-2.201** | **0.0277** | * |
| **Education: high school or below (vs college)** | **+5.0707** | 1.3735 | ±2.7469 | **+3.692** | **2.23e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2003** | 0.9594 | ±1.9187 | **+2.293** | **0.0218** | * |
| Site: UW (vs UAB) | -0.9507 | 0.8594 | ±1.7188 | -1.106 | 0.2686 |  |
| **Season: spring (vs autumn)** | **+2.7877** | 0.9200 | ±1.8399 | **+3.030** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9739 | 1.0278 | ±2.0556 | +1.921 | 0.0548 | . |
| **Season: winter (vs autumn)** | **+4.2686** | 1.0349 | ±2.0698 | **+4.125** | **3.71e-05** | *** |
| **Age (years)** | **-0.1119** | 0.0357 | ±0.0713 | **-3.138** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1777** | 0.0542 | ±0.1084 | **+3.280** | **0.0010** | ** |
| Hypertension | +1.1048 | 0.7965 | ±1.5931 | +1.387 | 0.1654 |  |
| High cholesterol | -0.0312 | 0.7485 | ±1.4969 | -0.042 | 0.9667 |  |
| Kidney disease | -1.5944 | 1.1137 | ±2.2275 | -1.432 | 0.1523 |  |
| Circulatory disease | +0.1120 | 1.0360 | ±2.0720 | +0.108 | 0.9139 |  |
| Avg. daily time < 54 (%) | +0.3536 | 0.7188 | ±1.4375 | +0.492 | 0.6227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.90e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.5**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1617** | 3.2007 | ±6.4014 | **+39.105** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5969** | 0.7287 | ±1.4575 | **-2.191** | **0.0284** | * |
| **Education: high school or below (vs college)** | **+5.0645** | 1.3735 | ±2.7469 | **+3.687** | **2.27e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1889** | 0.9590 | ±1.9179 | **+2.283** | **0.0225** | * |
| Site: UW (vs UAB) | -0.9624 | 0.8562 | ±1.7124 | -1.124 | 0.2610 |  |
| **Season: spring (vs autumn)** | **+2.7845** | 0.9195 | ±1.8390 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9796 | 1.0279 | ±2.0559 | +1.926 | 0.0541 | . |
| **Season: winter (vs autumn)** | **+4.2688** | 1.0349 | ±2.0699 | **+4.125** | **3.71e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0356 | ±0.0713 | **-3.134** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1774** | 0.0542 | ±0.1084 | **+3.272** | **0.0011** | ** |
| Hypertension | +1.1047 | 0.7969 | ±1.5938 | +1.386 | 0.1657 |  |
| High cholesterol | -0.0363 | 0.7494 | ±1.4988 | -0.048 | 0.9613 |  |
| Kidney disease | -1.5926 | 1.1141 | ±2.2282 | -1.430 | 0.1528 |  |
| Circulatory disease | +0.1174 | 1.0362 | ±2.0725 | +0.113 | 0.9098 |  |
| Time 54-69, pooled (%) | +0.0907 | 0.2487 | ±0.4974 | +0.365 | 0.7152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.05e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1994** | 3.2009 | ±6.4018 | **+39.114** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5997** | 0.7292 | ±1.4584 | **-2.194** | **0.0282** | * |
| **Education: high school or below (vs college)** | **+5.0583** | 1.3739 | ±2.7478 | **+3.682** | **2.32e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1778** | 0.9586 | ±1.9172 | **+2.272** | **0.0231** | * |
| Site: UW (vs UAB) | -0.9704 | 0.8567 | ±1.7134 | -1.133 | 0.2573 |  |
| **Season: spring (vs autumn)** | **+2.7826** | 0.9195 | ±1.8391 | **+3.026** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9793 | 1.0279 | ±2.0559 | +1.926 | 0.0542 | . |
| **Season: winter (vs autumn)** | **+4.2683** | 1.0350 | ±2.0701 | **+4.124** | **3.73e-05** | *** |
| **Age (years)** | **-0.1119** | 0.0357 | ±0.0713 | **-3.136** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.1024 | 0.7968 | ±1.5935 | +1.384 | 0.1665 |  |
| High cholesterol | -0.0404 | 0.7493 | ±1.4986 | -0.054 | 0.9570 |  |
| Kidney disease | -1.5921 | 1.1144 | ±2.2288 | -1.429 | 0.1531 |  |
| Circulatory disease | +0.1197 | 1.0362 | ±2.0725 | +0.115 | 0.9081 |  |
| Avg. daily time 54-69 (%) | +0.0625 | 0.2448 | ±0.4896 | +0.255 | 0.7985 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.97e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.5**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1645** | 3.2015 | ±6.4030 | **+39.096** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5996** | 0.7284 | ±1.4568 | **-2.196** | **0.0281** | * |
| **Education: high school or below (vs college)** | **+5.0647** | 1.3730 | ±2.7459 | **+3.689** | **2.25e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1903** | 0.9601 | ±1.9202 | **+2.281** | **0.0225** | * |
| Site: UW (vs UAB) | -0.9627 | 0.8568 | ±1.7136 | -1.124 | 0.2612 |  |
| **Season: spring (vs autumn)** | **+2.7844** | 0.9196 | ±1.8391 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9782 | 1.0281 | ±2.0561 | +1.924 | 0.0543 | . |
| **Season: winter (vs autumn)** | **+4.2699** | 1.0349 | ±2.0699 | **+4.126** | **3.70e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0356 | ±0.0712 | **-3.134** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.1038 | 0.7969 | ±1.5938 | +1.385 | 0.1660 |  |
| High cholesterol | -0.0358 | 0.7495 | ±1.4990 | -0.048 | 0.9619 |  |
| Kidney disease | -1.5923 | 1.1142 | ±2.2283 | -1.429 | 0.1530 |  |
| Circulatory disease | +0.1167 | 1.0362 | ±2.0724 | +0.113 | 0.9104 |  |
| Time < 70 (%) | +0.0631 | 0.1945 | ±0.3889 | +0.324 | 0.7457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.97e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.5**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1860** | 3.2013 | ±6.4026 | **+39.105** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5977** | 0.7288 | ±1.4575 | **-2.192** | **0.0284** | * |
| **Education: high school or below (vs college)** | **+5.0631** | 1.3737 | ±2.7474 | **+3.686** | **2.28e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1853** | 0.9595 | ±1.9189 | **+2.278** | **0.0228** | * |
| Site: UW (vs UAB) | -0.9627 | 0.8575 | ±1.7149 | -1.123 | 0.2615 |  |
| **Season: spring (vs autumn)** | **+2.7843** | 0.9196 | ±1.8392 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9788 | 1.0280 | ±2.0559 | +1.925 | 0.0542 | . |
| **Season: winter (vs autumn)** | **+4.2676** | 1.0350 | ±2.0700 | **+4.123** | **3.73e-05** | *** |
| **Age (years)** | **-0.1119** | 0.0357 | ±0.0713 | **-3.136** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.1040 | 0.7967 | ±1.5935 | +1.386 | 0.1658 |  |
| High cholesterol | -0.0373 | 0.7494 | ±1.4987 | -0.050 | 0.9603 |  |
| Kidney disease | -1.5925 | 1.1141 | ±2.2282 | -1.429 | 0.1529 |  |
| Circulatory disease | +0.1177 | 1.0363 | ±2.0725 | +0.114 | 0.9095 |  |
| Avg. daily time < 70 (%) | +0.0647 | 0.1957 | ±0.3913 | +0.331 | 0.7409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0507**, Adj R² = **0.0443**, F-statistic = **7.95** (p = **9.76e-17**), Residual SE = **16.009** on **2085** df, AIC = **17621.9**, BIC = **17706.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.1125** | 4.6084 | ±9.2168 | **+25.847** | **2.65e-147** | *** |
| **Education: graduate level (vs college)** | **-1.6906** | 0.7247 | ±1.4495 | **-2.333** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+5.2648** | 1.3786 | ±2.7573 | **+3.819** | **1.34e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0428** | 0.9619 | ±1.9239 | **+2.124** | **0.0337** | * |
| Site: UW (vs UAB) | -1.1121 | 0.8582 | ±1.7164 | -1.296 | 0.1950 |  |
| **Season: spring (vs autumn)** | **+2.7546** | 0.9217 | ±1.8434 | **+2.989** | **0.0028** | ** |
| Season: summer (vs autumn) | +1.8813 | 1.0329 | ±2.0659 | +1.821 | 0.0686 | . |
| **Season: winter (vs autumn)** | **+4.2551** | 1.0337 | ±2.0673 | **+4.117** | **3.85e-05** | *** |
| **Age (years)** | **-0.1127** | 0.0357 | ±0.0714 | **-3.155** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1076 | **+3.387** | **7.07e-04** | *** |
| Hypertension | +1.1734 | 0.7979 | ±1.5957 | +1.471 | 0.1414 |  |
| High cholesterol | -0.0298 | 0.7488 | ±1.4977 | -0.040 | 0.9683 |  |
| Kidney disease | -1.4254 | 1.1103 | ±2.2205 | -1.284 | 0.1992 |  |
| Circulatory disease | +0.1865 | 1.0343 | ±2.0686 | +0.180 | 0.8569 |  |
| Time 54-250, pooled (%) | +0.0630 | 0.0366 | ±0.0733 | +1.719 | 0.0857 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0508**, Adj R² = **0.0445**, F-statistic = **7.98** (p = **8.38e-17**), Residual SE = **16.008** on **2085** df, AIC = **17621.5**, BIC = **17706.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+118.7211** | 4.6817 | ±9.3634 | **+25.358** | **7.26e-142** | *** |
| **Education: graduate level (vs college)** | **-1.6935** | 0.7247 | ±1.4495 | **-2.337** | **0.0195** | * |
| **Education: high school or below (vs college)** | **+5.2748** | 1.3776 | ±2.7551 | **+3.829** | **1.29e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0387** | 0.9616 | ±1.9233 | **+2.120** | **0.0340** | * |
| Site: UW (vs UAB) | -1.1134 | 0.8579 | ±1.7157 | -1.298 | 0.1943 |  |
| **Season: spring (vs autumn)** | **+2.7580** | 0.9215 | ±1.8431 | **+2.993** | **0.0028** | ** |
| Season: summer (vs autumn) | +1.8829 | 1.0325 | ±2.0650 | +1.824 | 0.0682 | . |
| **Season: winter (vs autumn)** | **+4.2587** | 1.0332 | ±2.0664 | **+4.122** | **3.76e-05** | *** |
| **Age (years)** | **-0.1124** | 0.0357 | ±0.0714 | **-3.146** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1826** | 0.0538 | ±0.1075 | **+3.396** | **6.84e-04** | *** |
| Hypertension | +1.1737 | 0.7979 | ±1.5958 | +1.471 | 0.1413 |  |
| High cholesterol | -0.0287 | 0.7489 | ±1.4978 | -0.038 | 0.9694 |  |
| Kidney disease | -1.4102 | 1.1090 | ±2.2180 | -1.272 | 0.2035 |  |
| Circulatory disease | +0.1934 | 1.0349 | ±2.0697 | +0.187 | 0.8518 |  |
| Avg. daily time 54-250 (%) | +0.0666 | 0.0378 | ±0.0756 | +1.762 | 0.0780 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.0493**, Adj R² = **0.0430**, F-statistic = **7.73** (p = **3.65e-16**), Residual SE = **16.021** on **2085** df, AIC = **17624.8**, BIC = **17709.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3546** | 3.2063 | ±6.4127 | **+39.096** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5947** | 0.7242 | ±1.4483 | **-2.202** | **0.0277** | * |
| **Education: high school or below (vs college)** | **+4.9567** | 1.3745 | ±2.7489 | **+3.606** | **3.11e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2131** | 0.9549 | ±1.9099 | **+2.318** | **0.0205** | * |
| Site: UW (vs UAB) | -0.9703 | 0.8543 | ±1.7087 | -1.136 | 0.2561 |  |
| **Season: spring (vs autumn)** | **+2.7833** | 0.9201 | ±1.8401 | **+3.025** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9677 | 1.0282 | ±2.0564 | +1.914 | 0.0557 | . |
| **Season: winter (vs autumn)** | **+4.2784** | 1.0376 | ±2.0753 | **+4.123** | **3.74e-05** | *** |
| **Age (years)** | **-0.1147** | 0.0358 | ±0.0715 | **-3.207** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.1739** | 0.0540 | ±0.1080 | **+3.221** | **0.0013** | ** |
| Hypertension | +1.0500 | 0.8112 | ±1.6225 | +1.294 | 0.1956 |  |
| High cholesterol | -0.0865 | 0.7494 | ±1.4988 | -0.115 | 0.9081 |  |
| Kidney disease | -1.7146 | 1.1327 | ±2.2655 | -1.514 | 0.1301 |  |
| Circulatory disease | +0.1017 | 1.0352 | ±2.0703 | +0.098 | 0.9217 |  |
| Time 181-250, pooled (%) | +0.0253 | 0.0378 | ±0.0756 | +0.669 | 0.5036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0493**, Adj R² = **0.0429**, F-statistic = **7.72** (p = **3.79e-16**), Residual SE = **16.021** on **2085** df, AIC = **17624.9**, BIC = **17709.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3459** | 3.2067 | ±6.4134 | **+39.088** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5967** | 0.7244 | ±1.4489 | **-2.204** | **0.0275** | * |
| **Education: high school or below (vs college)** | **+4.9599** | 1.3743 | ±2.7486 | **+3.609** | **3.07e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2132** | 0.9556 | ±1.9113 | **+2.316** | **0.0206** | * |
| Site: UW (vs UAB) | -0.9691 | 0.8542 | ±1.7083 | -1.135 | 0.2566 |  |
| **Season: spring (vs autumn)** | **+2.7818** | 0.9200 | ±1.8401 | **+3.024** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9680 | 1.0282 | ±2.0564 | +1.914 | 0.0556 | . |
| **Season: winter (vs autumn)** | **+4.2763** | 1.0370 | ±2.0741 | **+4.124** | **3.73e-05** | *** |
| **Age (years)** | **-0.1144** | 0.0358 | ±0.0715 | **-3.200** | **0.0014** | ** |
| **BMI (kg/m2)** | **+0.1741** | 0.0540 | ±0.1080 | **+3.223** | **0.0013** | ** |
| Hypertension | +1.0527 | 0.8107 | ±1.6215 | +1.298 | 0.1941 |  |
| High cholesterol | -0.0847 | 0.7498 | ±1.4996 | -0.113 | 0.9100 |  |
| Kidney disease | -1.7081 | 1.1327 | ±2.2654 | -1.508 | 0.1316 |  |
| Circulatory disease | +0.1039 | 1.0350 | ±2.0700 | +0.100 | 0.9200 |  |
| Avg. daily time 181-250 (%) | +0.0235 | 0.0369 | ±0.0739 | +0.637 | 0.5241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.65e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2225** | 3.2088 | ±6.4176 | **+39.024** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6260** | 0.7224 | ±1.4449 | **-2.251** | **0.0244** | * |
| **Education: high school or below (vs college)** | **+5.1110** | 1.3795 | ±2.7590 | **+3.705** | **2.11e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1284** | 0.9592 | ±1.9184 | **+2.219** | **0.0265** | * |
| Site: UW (vs UAB) | -1.0121 | 0.8538 | ±1.7077 | -1.185 | 0.2359 |  |
| **Season: spring (vs autumn)** | **+2.7743** | 0.9203 | ±1.8405 | **+3.015** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9670 | 1.0299 | ±2.0599 | +1.910 | 0.0562 | . |
| **Season: winter (vs autumn)** | **+4.2673** | 1.0372 | ±2.0745 | **+4.114** | **3.89e-05** | *** |
| **Age (years)** | **-0.1109** | 0.0357 | ±0.0714 | **-3.108** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1798** | 0.0539 | ±0.1077 | **+3.339** | **8.41e-04** | *** |
| Hypertension | +1.1248 | 0.8082 | ±1.6164 | +1.392 | 0.1640 |  |
| High cholesterol | -0.0298 | 0.7509 | ±1.5018 | -0.040 | 0.9683 |  |
| Kidney disease | -1.5246 | 1.1207 | ±2.2413 | -1.360 | 0.1737 |  |
| Circulatory disease | +0.1383 | 1.0352 | ±2.0705 | +0.134 | 0.8937 |  |
| Time > 180 (%) | -0.0090 | 0.0220 | ±0.0441 | -0.408 | 0.6829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.51e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.3**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2161** | 3.2084 | ±6.4169 | **+39.027** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6273** | 0.7227 | ±1.4453 | **-2.252** | **0.0243** | * |
| **Education: high school or below (vs college)** | **+5.1198** | 1.3788 | ±2.7576 | **+3.713** | **2.05e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1225** | 0.9595 | ±1.9191 | **+2.212** | **0.0270** | * |
| Site: UW (vs UAB) | -1.0154 | 0.8538 | ±1.7077 | -1.189 | 0.2344 |  |
| **Season: spring (vs autumn)** | **+2.7750** | 0.9201 | ±1.8402 | **+3.016** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9669 | 1.0297 | ±2.0593 | +1.910 | 0.0561 | . |
| **Season: winter (vs autumn)** | **+4.2680** | 1.0365 | ±2.0730 | **+4.118** | **3.83e-05** | *** |
| **Age (years)** | **-0.1108** | 0.0357 | ±0.0714 | **-3.105** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1801** | 0.0538 | ±0.1076 | **+3.346** | **8.19e-04** | *** |
| Hypertension | +1.1279 | 0.8081 | ±1.6161 | +1.396 | 0.1628 |  |
| High cholesterol | -0.0274 | 0.7511 | ±1.5022 | -0.036 | 0.9709 |  |
| Kidney disease | -1.5145 | 1.1200 | ±2.2399 | -1.352 | 0.1763 |  |
| Circulatory disease | +0.1406 | 1.0352 | ±2.0705 | +0.136 | 0.8920 |  |
| Avg. daily time > 180 (%) | -0.0101 | 0.0221 | ±0.0442 | -0.459 | 0.6460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.68** (p = **4.81e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.5**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2202** | 3.2072 | ±6.4145 | **+39.043** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6284** | 0.7212 | ±1.4424 | **-2.258** | **0.0240** | * |
| **Education: high school or below (vs college)** | **+5.0970** | 1.3771 | ±2.7542 | **+3.701** | **2.15e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1335** | 0.9609 | ±1.9217 | **+2.220** | **0.0264** | * |
| Site: UW (vs UAB) | -1.0060 | 0.8535 | ±1.7070 | -1.179 | 0.2385 |  |
| **Season: spring (vs autumn)** | **+2.7815** | 0.9193 | ±1.8386 | **+3.026** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9678 | 1.0305 | ±2.0611 | +1.909 | 0.0562 | . |
| **Season: winter (vs autumn)** | **+4.2747** | 1.0328 | ±2.0657 | **+4.139** | **3.49e-05** | *** |
| **Age (years)** | **-0.1116** | 0.0357 | ±0.0713 | **-3.128** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1803** | 0.0538 | ±0.1076 | **+3.351** | **8.04e-04** | *** |
| Hypertension | +1.1125 | 0.8045 | ±1.6091 | +1.383 | 0.1667 |  |
| High cholesterol | -0.0349 | 0.7509 | ±1.5018 | -0.046 | 0.9630 |  |
| Kidney disease | -1.5489 | 1.1219 | ±2.2438 | -1.381 | 0.1674 |  |
| Circulatory disease | +0.1337 | 1.0346 | ±2.0693 | +0.129 | 0.8972 |  |
| Nocturnal time > 180 (%) | -0.0076 | 0.0244 | ±0.0487 | -0.311 | 0.7560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0499**, Adj R² = **0.0435**, F-statistic = **7.82** (p = **2.10e-16**), Residual SE = **16.016** on **2085** df, AIC = **17623.6**, BIC = **17708.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1232** | 3.2061 | ±6.4121 | **+39.027** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5483** | 0.7234 | ±1.4468 | **-2.140** | **0.0323** | * |
| **Education: high school or below (vs college)** | **+4.9608** | 1.3697 | ±2.7393 | **+3.622** | **2.92e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2171** | 0.9543 | ±1.9086 | **+2.323** | **0.0202** | * |
| Site: UW (vs UAB) | -0.9683 | 0.8551 | ±1.7101 | -1.132 | 0.2575 |  |
| **Season: spring (vs autumn)** | **+2.8372** | 0.9201 | ±1.8402 | **+3.084** | **0.0020** | ** |
| Season: summer (vs autumn) | +1.9863 | 1.0274 | ±2.0547 | +1.933 | 0.0532 | . |
| **Season: winter (vs autumn)** | **+4.3324** | 1.0419 | ±2.0837 | **+4.158** | **3.21e-05** | *** |
| **Age (years)** | **-0.1163** | 0.0357 | ±0.0715 | **-3.256** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1785** | 0.0542 | ±0.1084 | **+3.292** | **9.95e-04** | *** |
| Hypertension | +1.0008 | 0.8072 | ±1.6144 | +1.240 | 0.2150 |  |
| High cholesterol | -0.1103 | 0.7511 | ±1.5022 | -0.147 | 0.8833 |  |
| Kidney disease | -1.7512 | 1.1147 | ±2.2293 | -1.571 | 0.1162 |  |
| Circulatory disease | +0.1210 | 1.0352 | ±2.0704 | +0.117 | 0.9070 |  |
| Any reading > 250 during wear (0/1) | +1.0645 | 0.7661 | ±1.5322 | +1.389 | 0.1647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.0507**, Adj R² = **0.0443**, F-statistic = **7.95** (p = **9.73e-17**), Residual SE = **16.009** on **2085** df, AIC = **17621.8**, BIC = **17706.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3866** | 3.2113 | ±6.4226 | **+39.045** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6895** | 0.7247 | ±1.4494 | **-2.331** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+5.2703** | 1.3788 | ±2.7576 | **+3.822** | **1.32e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0523** | 0.9612 | ±1.9224 | **+2.135** | **0.0327** | * |
| Site: UW (vs UAB) | -1.1043 | 0.8579 | ±1.7158 | -1.287 | 0.1980 |  |
| **Season: spring (vs autumn)** | **+2.7561** | 0.9216 | ±1.8433 | **+2.990** | **0.0028** | ** |
| Season: summer (vs autumn) | +1.8805 | 1.0329 | ±2.0658 | +1.821 | 0.0687 | . |
| **Season: winter (vs autumn)** | **+4.2552** | 1.0337 | ±2.0674 | **+4.116** | **3.85e-05** | *** |
| **Age (years)** | **-0.1126** | 0.0357 | ±0.0714 | **-3.153** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1077 | **+3.386** | **7.09e-04** | *** |
| Hypertension | +1.1748 | 0.7979 | ±1.5959 | +1.472 | 0.1409 |  |
| High cholesterol | -0.0260 | 0.7491 | ±1.4981 | -0.035 | 0.9723 |  |
| Kidney disease | -1.4252 | 1.1101 | ±2.2201 | -1.284 | 0.1992 |  |
| Circulatory disease | +0.1844 | 1.0343 | ±2.0687 | +0.178 | 0.8585 |  |
| Time > 250 (%) | -0.0630 | 0.0366 | ±0.0733 | -1.718 | 0.0858 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0509**, Adj R² = **0.0445**, F-statistic = **7.98** (p = **8.13e-17**), Residual SE = **16.008** on **2085** df, AIC = **17621.4**, BIC = **17706.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3680** | 3.2097 | ±6.4193 | **+39.060** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6924** | 0.7248 | ±1.4495 | **-2.335** | **0.0195** | * |
| **Education: high school or below (vs college)** | **+5.2813** | 1.3777 | ±2.7554 | **+3.833** | **1.26e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0449** | 0.9611 | ±1.9221 | **+2.128** | **0.0334** | * |
| Site: UW (vs UAB) | -1.1072 | 0.8575 | ±1.7150 | -1.291 | 0.1967 |  |
| **Season: spring (vs autumn)** | **+2.7595** | 0.9215 | ±1.8430 | **+2.995** | **0.0027** | ** |
| Season: summer (vs autumn) | +1.8814 | 1.0324 | ±2.0649 | +1.822 | 0.0684 | . |
| **Season: winter (vs autumn)** | **+4.2579** | 1.0333 | ±2.0665 | **+4.121** | **3.77e-05** | *** |
| **Age (years)** | **-0.1124** | 0.0357 | ±0.0714 | **-3.147** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1826** | 0.0538 | ±0.1075 | **+3.397** | **6.82e-04** | *** |
| Hypertension | +1.1759 | 0.7980 | ±1.5960 | +1.474 | 0.1406 |  |
| High cholesterol | -0.0256 | 0.7491 | ±1.4981 | -0.034 | 0.9727 |  |
| Kidney disease | -1.4091 | 1.1089 | ±2.2178 | -1.271 | 0.2038 |  |
| Circulatory disease | +0.1920 | 1.0348 | ±2.0696 | +0.186 | 0.8528 |  |
| Avg. daily time > 250 (%) | -0.0671 | 0.0378 | ±0.0757 | -1.775 | 0.0760 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 1,872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1872**, R² = **0.1399**, Adj R² = **0.1353**, F-statistic = **30.27** (p = **1.55e-54**), Residual SE = **4234.002** on **1861** df, AIC = **36589.3**, BIC = **36650.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19510.1838** | 800.4881 | ±1600.9761 | **+24.373** | **3.32e-131** | *** |
| **Education: graduate level (vs college)** | **-652.0416** | 205.9530 | ±411.9059 | **-3.166** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **+1044.3055** | 395.7683 | ±791.5367 | **+2.639** | **0.0083** | ** |
| Site: UCSD (vs UAB) | +220.5205 | 264.2687 | ±528.5374 | +0.834 | 0.4040 |  |
| Site: UW (vs UAB) | -114.2527 | 239.3035 | ±478.6069 | -0.477 | 0.6330 |  |
| **Age (years)** | **-136.6472** | 9.2496 | ±18.4993 | **-14.773** | **2.18e-49** | *** |
| **BMI (kg/m2)** | **-32.5698** | 15.5362 | ±31.0725 | **-2.096** | **0.0360** | * |
| Hypertension | +164.7856 | 219.9282 | ±439.8564 | +0.749 | 0.4537 |  |
| High cholesterol | -23.9662 | 200.4288 | ±400.8576 | -0.120 | 0.9048 |  |
| **Kidney disease** | **-874.7082** | 336.4518 | ±672.9037 | **-2.600** | **0.0093** | ** |
| **Circulatory disease** | **-1035.7741** | 261.2555 | ±522.5110 | **-3.965** | **7.35e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1872**, R² = **0.1445**, Adj R² = **0.1394**, F-statistic = **28.55** (p = **7.18e-56**), Residual SE = **4223.881** on **1860** df, AIC = **36581.3**, BIC = **36647.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17975.7073** | 1011.9075 | ±2023.8149 | **+17.764** | **1.34e-70** | *** |
| **Education: graduate level (vs college)** | **-615.5171** | 207.2243 | ±414.4485 | **-2.970** | **0.0030** | ** |
| **Education: high school or below (vs college)** | **+927.5768** | 394.6376 | ±789.2751 | **+2.350** | **0.0188** | * |
| Site: UCSD (vs UAB) | +241.2269 | 263.4004 | ±526.8007 | +0.916 | 0.3598 |  |
| Site: UW (vs UAB) | -74.4809 | 238.2917 | ±476.5835 | -0.313 | 0.7546 |  |
| **Age (years)** | **-138.3614** | 9.2889 | ±18.5778 | **-14.895** | **3.53e-50** | *** |
| **BMI (kg/m2)** | **-38.3996** | 15.6212 | ±31.2424 | **-2.458** | **0.0140** | * |
| Hypertension | +95.9893 | 221.9263 | ±443.8525 | +0.433 | 0.6654 |  |
| High cholesterol | -80.6809 | 201.4855 | ±402.9711 | -0.400 | 0.6888 |  |
| **Kidney disease** | **-911.3369** | 336.4417 | ±672.8834 | **-2.709** | **0.0068** | ** |
| **Circulatory disease** | **-1051.1544** | 261.6542 | ±523.3083 | **-4.017** | **5.89e-05** | *** |
| **HbA1c (%)** | **+306.2488** | 123.4453 | ±246.8905 | **+2.481** | **0.0131** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1872**, R² = **0.1412**, Adj R² = **0.1361**, F-statistic = **27.81** (p = **2.20e-54**), Residual SE = **4231.888** on **1860** df, AIC = **36588.4**, BIC = **36654.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18969.6429** | 886.6421 | ±1773.2842 | **+21.395** | **1.49e-101** | *** |
| **Education: graduate level (vs college)** | **-641.0668** | 206.7556 | ±413.5113 | **-3.101** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **+987.6687** | 392.6064 | ±785.2127 | **+2.516** | **0.0119** | * |
| Site: UCSD (vs UAB) | +234.9159 | 263.7996 | ±527.5992 | +0.891 | 0.3732 |  |
| Site: UW (vs UAB) | -103.1282 | 238.8436 | ±477.6872 | -0.432 | 0.6659 |  |
| **Age (years)** | **-137.3984** | 9.3117 | ±18.6234 | **-14.755** | **2.84e-49** | *** |
| **BMI (kg/m2)** | **-34.7286** | 15.5670 | ±31.1339 | **-2.231** | **0.0257** | * |
| Hypertension | +129.9201 | 221.7464 | ±443.4927 | +0.586 | 0.5579 |  |
| High cholesterol | -43.8542 | 200.8024 | ±401.6049 | -0.218 | 0.8271 |  |
| **Kidney disease** | **-931.3680** | 341.9741 | ±683.9482 | **-2.724** | **0.0065** | ** |
| **Circulatory disease** | **-1051.0816** | 261.9858 | ±523.9716 | **-4.012** | **6.02e-05** | *** |
| Mean glucose (mg/dL) | +5.0814 | 3.7656 | ±7.5312 | +1.349 | 0.1772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1872**, R² = **0.1412**, Adj R² = **0.1361**, F-statistic = **27.81** (p = **2.20e-54**), Residual SE = **4231.888** on **1860** df, AIC = **36588.4**, BIC = **36654.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18266.4880** | 1206.0570 | ±2412.1141 | **+15.146** | **8.10e-52** | *** |
| **Education: graduate level (vs college)** | **-641.0668** | 206.7556 | ±413.5113 | **-3.101** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **+987.6687** | 392.6064 | ±785.2127 | **+2.516** | **0.0119** | * |
| Site: UCSD (vs UAB) | +234.9159 | 263.7996 | ±527.5992 | +0.891 | 0.3732 |  |
| Site: UW (vs UAB) | -103.1282 | 238.8436 | ±477.6872 | -0.432 | 0.6659 |  |
| **Age (years)** | **-137.3984** | 9.3117 | ±18.6234 | **-14.755** | **2.84e-49** | *** |
| **BMI (kg/m2)** | **-34.7286** | 15.5670 | ±31.1339 | **-2.231** | **0.0257** | * |
| Hypertension | +129.9201 | 221.7464 | ±443.4927 | +0.586 | 0.5579 |  |
| High cholesterol | -43.8542 | 200.8024 | ±401.6049 | -0.218 | 0.8271 |  |
| **Kidney disease** | **-931.3680** | 341.9741 | ±683.9482 | **-2.724** | **0.0065** | ** |
| **Circulatory disease** | **-1051.0816** | 261.9858 | ±523.9716 | **-4.012** | **6.02e-05** | *** |
| GMI (%) | +212.4335 | 157.4253 | ±314.8506 | +1.349 | 0.1772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1872**, R² = **0.1423**, Adj R² = **0.1373**, F-statistic = **28.06** (p = **6.75e-55**), Residual SE = **4229.125** on **1860** df, AIC = **36585.9**, BIC = **36652.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18774.4585** | 896.4256 | ±1792.8511 | **+20.944** | **2.14e-97** | *** |
| **Education: graduate level (vs college)** | **-634.5379** | 206.9590 | ±413.9181 | **-3.066** | **0.0022** | ** |
| **Education: high school or below (vs college)** | **+967.8067** | 392.0147 | ±784.0295 | **+2.469** | **0.0136** | * |
| Site: UCSD (vs UAB) | +232.3202 | 263.5852 | ±527.1705 | +0.881 | 0.3781 |  |
| Site: UW (vs UAB) | -106.8664 | 238.7319 | ±477.4638 | -0.448 | 0.6544 |  |
| **Age (years)** | **-136.7332** | 9.2693 | ±18.5387 | **-14.751** | **3.03e-49** | *** |
| **BMI (kg/m2)** | **-37.0350** | 15.6229 | ±31.2457 | **-2.371** | **0.0178** | * |
| Hypertension | +125.3967 | 221.1295 | ±442.2590 | +0.567 | 0.5707 |  |
| High cholesterol | -50.6814 | 200.8881 | ±401.7762 | -0.252 | 0.8008 |  |
| **Kidney disease** | **-922.9960** | 339.6153 | ±679.2306 | **-2.718** | **0.0066** | ** |
| **Circulatory disease** | **-1053.1239** | 261.6799 | ±523.3598 | **-4.024** | **5.71e-05** | *** |
| Nocturnal mean 00-06h (mg/dL) | +6.9457 | 3.9253 | ±7.8506 | +1.769 | 0.0768 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1872**, R² = **0.1405**, Adj R² = **0.1354**, F-statistic = **27.64** (p = **4.68e-54**), Residual SE = **4233.662** on **1860** df, AIC = **36589.9**, BIC = **36656.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19336.5341** | 815.3342 | ±1630.6684 | **+23.716** | **2.46e-124** | *** |
| **Education: graduate level (vs college)** | **-641.0836** | 207.5201 | ±415.0402 | **-3.089** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **+1006.0079** | 393.6997 | ±787.3994 | **+2.555** | **0.0106** | * |
| Site: UCSD (vs UAB) | +240.1745 | 263.8555 | ±527.7111 | +0.910 | 0.3627 |  |
| Site: UW (vs UAB) | -94.9875 | 238.5271 | ±477.0542 | -0.398 | 0.6905 |  |
| **Age (years)** | **-137.5420** | 9.3591 | ±18.7182 | **-14.696** | **6.83e-49** | *** |
| **BMI (kg/m2)** | **-33.3480** | 15.5530 | ±31.1060 | **-2.144** | **0.0320** | * |
| Hypertension | +137.1163 | 222.4953 | ±444.9905 | +0.616 | 0.5377 |  |
| High cholesterol | -34.0098 | 200.8399 | ±401.6797 | -0.169 | 0.8655 |  |
| **Kidney disease** | **-939.5959** | 348.8978 | ±697.7956 | **-2.693** | **0.0071** | ** |
| **Circulatory disease** | **-1046.0442** | 262.0140 | ±524.0280 | **-3.992** | **6.54e-05** | *** |
| Glucose SD, pooled (mg/dL) | +9.9625 | 10.4149 | ±20.8298 | +0.957 | 0.3388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1872**, R² = **0.1403**, Adj R² = **0.1353**, F-statistic = **27.61** (p = **5.53e-54**), Residual SE = **4234.050** on **1860** df, AIC = **36590.3**, BIC = **36656.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19359.7807** | 814.0717 | ±1628.1433 | **+23.781** | **5.20e-125** | *** |
| **Education: graduate level (vs college)** | **-643.6321** | 207.1545 | ±414.3089 | **-3.107** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **+1010.2655** | 394.7386 | ±789.4772 | **+2.559** | **0.0105** | * |
| Site: UCSD (vs UAB) | +236.5026 | 263.8200 | ±527.6400 | +0.896 | 0.3700 |  |
| Site: UW (vs UAB) | -99.6020 | 238.5575 | ±477.1150 | -0.418 | 0.6763 |  |
| **Age (years)** | **-137.5279** | 9.3671 | ±18.7342 | **-14.682** | **8.40e-49** | *** |
| **BMI (kg/m2)** | **-33.0613** | 15.5445 | ±31.0890 | **-2.127** | **0.0334** | * |
| Hypertension | +141.2186 | 222.3222 | ±444.6444 | +0.635 | 0.5253 |  |
| High cholesterol | -32.9601 | 201.0172 | ±402.0345 | -0.164 | 0.8698 |  |
| **Kidney disease** | **-931.6363** | 348.1125 | ±696.2251 | **-2.676** | **0.0074** | ** |
| **Circulatory disease** | **-1043.5526** | 261.8757 | ±523.7513 | **-3.985** | **6.75e-05** | *** |
| Avg. daily SD (mg/dL) | +9.6551 | 11.2995 | ±22.5990 | +0.854 | 0.3928 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1872**, R² = **0.1399**, Adj R² = **0.1348**, F-statistic = **27.50** (p = **8.75e-54**), Residual SE = **4235.129** on **1860** df, AIC = **36591.2**, BIC = **36657.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19479.6951** | 857.7270 | ±1715.4539 | **+22.711** | **3.50e-114** | *** |
| **Education: graduate level (vs college)** | **-651.2214** | 206.9075 | ±413.8150 | **-3.147** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **+1042.2425** | 396.0568 | ±792.1137 | **+2.632** | **0.0085** | ** |
| Site: UCSD (vs UAB) | +222.4584 | 264.6340 | ±529.2681 | +0.841 | 0.4006 |  |
| Site: UW (vs UAB) | -112.4252 | 239.2849 | ±478.5697 | -0.470 | 0.6385 |  |
| **Age (years)** | **-136.7302** | 9.3176 | ±18.6352 | **-14.674** | **9.40e-49** | *** |
| **BMI (kg/m2)** | **-32.5590** | 15.5494 | ±31.0989 | **-2.094** | **0.0363** | * |
| Hypertension | +162.8296 | 221.4679 | ±442.9358 | +0.735 | 0.4622 |  |
| High cholesterol | -24.2242 | 200.6049 | ±401.2097 | -0.121 | 0.9039 |  |
| **Kidney disease** | **-879.7571** | 344.1248 | ±688.2496 | **-2.557** | **0.0106** | * |
| **Circulatory disease** | **-1036.2908** | 261.5422 | ±523.0844 | **-3.962** | **7.43e-05** | *** |
| CV (%) | +1.8256 | 19.4802 | ±38.9604 | +0.094 | 0.9253 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1872**, R² = **0.1405**, Adj R² = **0.1355**, F-statistic = **27.65** (p = **4.46e-54**), Residual SE = **4233.548** on **1860** df, AIC = **36589.8**, BIC = **36656.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20061.9509** | 934.5325 | ±1869.0649 | **+21.467** | **3.14e-102** | *** |
| **Education: graduate level (vs college)** | **-642.0642** | 206.6417 | ±413.2833 | **-3.107** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **+1018.5593** | 395.8808 | ±791.7615 | **+2.573** | **0.0101** | * |
| Site: UCSD (vs UAB) | +242.0763 | 264.4567 | ±528.9135 | +0.915 | 0.3600 |  |
| Site: UW (vs UAB) | -97.8970 | 239.2213 | ±478.4426 | -0.409 | 0.6824 |  |
| **Age (years)** | **-137.6701** | 9.3244 | ±18.6489 | **-14.764** | **2.48e-49** | *** |
| **BMI (kg/m2)** | **-32.4831** | 15.5472 | ±31.0944 | **-2.089** | **0.0367** | * |
| Hypertension | +139.1136 | 221.2599 | ±442.5198 | +0.629 | 0.5295 |  |
| High cholesterol | -28.4539 | 200.5719 | ±401.1438 | -0.142 | 0.8872 |  |
| **Kidney disease** | **-924.0587** | 342.1072 | ±684.2144 | **-2.701** | **0.0069** | ** |
| **Circulatory disease** | **-1043.6811** | 261.5968 | ±523.1937 | **-3.990** | **6.62e-05** | *** |
| Mean / SD ratio | -88.4048 | 72.7083 | ±145.4167 | -1.216 | 0.2240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1872**, R² = **0.1411**, Adj R² = **0.1360**, F-statistic = **27.77** (p = **2.56e-54**), Residual SE = **4232.250** on **1860** df, AIC = **36588.7**, BIC = **36655.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20250.1890** | 930.5660 | ±1861.1320 | **+21.761** | **5.42e-105** | *** |
| **Education: graduate level (vs college)** | **-641.5947** | 206.1613 | ±412.3227 | **-3.112** | **0.0019** | ** |
| **Education: high school or below (vs college)** | **+1008.7378** | 396.5166 | ±793.0332 | **+2.544** | **0.0110** | * |
| Site: UCSD (vs UAB) | +242.1864 | 264.2332 | ±528.4664 | +0.917 | 0.3594 |  |
| Site: UW (vs UAB) | -97.4369 | 239.0080 | ±478.0159 | -0.408 | 0.6835 |  |
| **Age (years)** | **-138.3069** | 9.3486 | ±18.6973 | **-14.794** | **1.59e-49** | *** |
| **BMI (kg/m2)** | **-32.3785** | 15.5272 | ±31.0545 | **-2.085** | **0.0370** | * |
| Hypertension | +134.3729 | 220.3708 | ±440.7416 | +0.610 | 0.5420 |  |
| High cholesterol | -29.2080 | 200.5547 | ±401.1094 | -0.146 | 0.8842 |  |
| **Kidney disease** | **-937.1796** | 340.7550 | ±681.5099 | **-2.750** | **0.0060** | ** |
| **Circulatory disease** | **-1040.5715** | 261.5468 | ±523.0935 | **-3.979** | **6.93e-05** | *** |
| Avg. daily mean/SD | -100.3027 | 59.3982 | ±118.7963 | -1.689 | 0.0913 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1872**, R² = **0.1484**, Adj R² = **0.1434**, F-statistic = **29.47** (p = **1.12e-57**), Residual SE = **4214.173** on **1860** df, AIC = **36572.7**, BIC = **36639.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17563.3720** | 933.6800 | ±1867.3600 | **+18.811** | **6.15e-79** | *** |
| **Education: graduate level (vs college)** | **-608.6267** | 205.9241 | ±411.8481 | **-2.956** | **0.0031** | ** |
| **Education: high school or below (vs college)** | **+952.6463** | 392.6989 | ±785.3978 | **+2.426** | **0.0153** | * |
| Site: UCSD (vs UAB) | +296.9684 | 263.1957 | ±526.3913 | +1.128 | 0.2592 |  |
| Site: UW (vs UAB) | -7.1972 | 238.6797 | ±477.3593 | -0.030 | 0.9759 |  |
| **Age (years)** | **-136.0224** | 9.1914 | ±18.3829 | **-14.799** | **1.49e-49** | *** |
| **BMI (kg/m2)** | **-33.9435** | 15.4746 | ±30.9492 | **-2.193** | **0.0283** | * |
| Hypertension | +142.9441 | 219.1830 | ±438.3660 | +0.652 | 0.5143 |  |
| High cholesterol | -21.4877 | 199.5804 | ±399.1608 | -0.108 | 0.9143 |  |
| **Kidney disease** | **-1004.7085** | 340.7466 | ±681.4933 | **-2.949** | **0.0032** | ** |
| **Circulatory disease** | **-1033.3899** | 261.0869 | ±522.1738 | **-3.958** | **7.56e-05** | *** |
| **MAG (mg/dL/h)** | **+47.6392** | 12.8502 | ±25.7004 | **+3.707** | **2.09e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1872**, R² = **0.1409**, Adj R² = **0.1358**, F-statistic = **27.73** (p = **3.10e-54**), Residual SE = **4232.692** on **1860** df, AIC = **36589.1**, BIC = **36655.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19148.5940** | 842.5602 | ±1685.1204 | **+22.727** | **2.44e-114** | *** |
| **Education: graduate level (vs college)** | **-640.2729** | 206.9633 | ±413.9265 | **-3.094** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **+993.6691** | 395.0663 | ±790.1327 | **+2.515** | **0.0119** | * |
| Site: UCSD (vs UAB) | +246.0781 | 263.9660 | ±527.9319 | +0.932 | 0.3512 |  |
| Site: UW (vs UAB) | -91.6714 | 238.6381 | ±477.2762 | -0.384 | 0.7009 |  |
| **Age (years)** | **-137.7747** | 9.3363 | ±18.6726 | **-14.757** | **2.78e-49** | *** |
| **BMI (kg/m2)** | **-32.5424** | 15.5599 | ±31.1197 | **-2.091** | **0.0365** | * |
| Hypertension | +135.9458 | 222.0325 | ±444.0651 | +0.612 | 0.5404 |  |
| High cholesterol | -35.8445 | 200.9037 | ±401.8074 | -0.178 | 0.8584 |  |
| **Kidney disease** | **-955.0493** | 345.6950 | ±691.3899 | **-2.763** | **0.0057** | ** |
| **Circulatory disease** | **-1047.5015** | 261.8787 | ±523.7575 | **-4.000** | **6.34e-05** | *** |
| Avg. daily range (mg/dL) | +3.9104 | 3.0146 | ±6.0292 | +1.297 | 0.1946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1872**, R² = **0.1418**, Adj R² = **0.1367**, F-statistic = **27.94** (p = **1.21e-54**), Residual SE = **4230.490** on **1860** df, AIC = **36587.1**, BIC = **36653.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19324.0301** | 805.7981 | ±1611.5963 | **+23.981** | **4.37e-127** | *** |
| **Education: graduate level (vs college)** | **-629.1356** | 208.0856 | ±416.1712 | **-3.023** | **0.0025** | ** |
| **Education: high school or below (vs college)** | **+1002.1110** | 392.8884 | ±785.7768 | **+2.551** | **0.0108** | * |
| Site: UCSD (vs UAB) | +249.2707 | 263.6658 | ±527.3316 | +0.945 | 0.3445 |  |
| Site: UW (vs UAB) | -82.4695 | 238.7494 | ±477.4987 | -0.345 | 0.7298 |  |
| **Age (years)** | **-136.7883** | 9.2706 | ±18.5413 | **-14.755** | **2.86e-49** | *** |
| **BMI (kg/m2)** | **-35.1667** | 15.5685 | ±31.1369 | **-2.259** | **0.0239** | * |
| Hypertension | +128.2901 | 220.8963 | ±441.7926 | +0.581 | 0.5614 |  |
| High cholesterol | -39.1276 | 200.3297 | ±400.6593 | -0.195 | 0.8451 |  |
| **Kidney disease** | **-938.7102** | 343.8360 | ±687.6720 | **-2.730** | **0.0063** | ** |
| **Circulatory disease** | **-1065.8739** | 262.4906 | ±524.9811 | **-4.061** | **4.89e-05** | *** |
| SD of daily means (mg/dL) | +32.7873 | 20.7575 | ±41.5151 | +1.580 | 0.1142 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1872**, R² = **0.1406**, Adj R² = **0.1355**, F-statistic = **27.66** (p = **4.22e-54**), Residual SE = **4233.421** on **1860** df, AIC = **36589.7**, BIC = **36656.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20152.9610** | 1045.1863 | ±2090.3725 | **+19.282** | **7.65e-83** | *** |
| **Education: graduate level (vs college)** | **-641.2755** | 207.6001 | ±415.2003 | **-3.089** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **+1003.1638** | 392.6871 | ±785.3742 | **+2.555** | **0.0106** | * |
| Site: UCSD (vs UAB) | +240.8158 | 263.7615 | ±527.5230 | +0.913 | 0.3612 |  |
| Site: UW (vs UAB) | -96.8626 | 238.7965 | ±477.5930 | -0.406 | 0.6850 |  |
| **Age (years)** | **-137.2343** | 9.3122 | ±18.6243 | **-14.737** | **3.72e-49** | *** |
| **BMI (kg/m2)** | **-34.0865** | 15.5061 | ±31.0122 | **-2.198** | **0.0279** | * |
| Hypertension | +145.4327 | 221.5230 | ±443.0459 | +0.657 | 0.5115 |  |
| High cholesterol | -32.9484 | 200.8592 | ±401.7183 | -0.164 | 0.8697 |  |
| **Kidney disease** | **-919.6081** | 344.0256 | ±688.0513 | **-2.673** | **0.0075** | ** |
| **Circulatory disease** | **-1049.2429** | 261.9309 | ±523.8618 | **-4.006** | **6.18e-05** | *** |
| Time in range 70-180, pooled (%) | -6.2902 | 6.5778 | ±13.1557 | -0.956 | 0.3389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1872**, R² = **0.1406**, Adj R² = **0.1355**, F-statistic = **27.66** (p = **4.27e-54**), Residual SE = **4233.445** on **1860** df, AIC = **36589.8**, BIC = **36656.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20150.6157** | 1047.3485 | ±2094.6969 | **+19.240** | **1.72e-82** | *** |
| **Education: graduate level (vs college)** | **-641.7708** | 207.5244 | ±415.0488 | **-3.093** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **+1002.9313** | 392.6310 | ±785.2620 | **+2.554** | **0.0106** | * |
| Site: UCSD (vs UAB) | +241.1393 | 263.6993 | ±527.3985 | +0.914 | 0.3605 |  |
| Site: UW (vs UAB) | -96.9829 | 238.7717 | ±477.5434 | -0.406 | 0.6846 |  |
| **Age (years)** | **-137.2688** | 9.3166 | ±18.6333 | **-14.734** | **3.91e-49** | *** |
| **BMI (kg/m2)** | **-34.1004** | 15.5146 | ±31.0291 | **-2.198** | **0.0280** | * |
| Hypertension | +145.9860 | 221.4039 | ±442.8078 | +0.659 | 0.5097 |  |
| High cholesterol | -33.1940 | 200.8652 | ±401.7305 | -0.165 | 0.8687 |  |
| **Kidney disease** | **-920.1474** | 344.1623 | ±688.3246 | **-2.674** | **0.0075** | ** |
| **Circulatory disease** | **-1048.9950** | 262.0174 | ±524.0348 | **-4.004** | **6.24e-05** | *** |
| Avg. daily time in range 70-180 (%) | -6.2187 | 6.5452 | ±13.0905 | -0.950 | 0.3421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1872**, R² = **0.1422**, Adj R² = **0.1371**, F-statistic = **28.02** (p = **8.08e-55**), Residual SE = **4229.544** on **1860** df, AIC = **36586.3**, BIC = **36652.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19772.8228** | 811.3007 | ±1622.6015 | **+24.372** | **3.41e-131** | *** |
| **Education: graduate level (vs college)** | **-657.4335** | 205.9035 | ±411.8070 | **-3.193** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **+999.4727** | 394.3889 | ±788.7777 | **+2.534** | **0.0113** | * |
| Site: UCSD (vs UAB) | +155.9013 | 264.7554 | ±529.5107 | +0.589 | 0.5560 |  |
| Site: UW (vs UAB) | -145.8384 | 239.5047 | ±479.0094 | -0.609 | 0.5426 |  |
| **Age (years)** | **-138.2077** | 9.2891 | ±18.5783 | **-14.878** | **4.55e-50** | *** |
| **BMI (kg/m2)** | **-31.7777** | 15.5465 | ±31.0931 | **-2.044** | **0.0410** | * |
| Hypertension | +169.5908 | 219.8863 | ±439.7727 | +0.771 | 0.4405 |  |
| High cholesterol | -55.1003 | 200.5368 | ±401.0736 | -0.275 | 0.7835 |  |
| **Kidney disease** | **-894.0547** | 336.3466 | ±672.6931 | **-2.658** | **0.0079** | ** |
| **Circulatory disease** | **-993.8106** | 261.3536 | ±522.7071 | **-3.803** | **1.43e-04** | *** |
| **Any reading < 54 during wear (0/1)** | **-479.0493** | 212.4569 | ±424.9139 | **-2.255** | **0.0241** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1872**, R² = **0.1416**, Adj R² = **0.1365**, F-statistic = **27.89** (p = **1.49e-54**), Residual SE = **4230.972** on **1860** df, AIC = **36587.6**, BIC = **36654.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19636.5759** | 805.0049 | ±1610.0099 | **+24.393** | **2.02e-131** | *** |
| **Education: graduate level (vs college)** | **-658.5961** | 205.7470 | ±411.4940 | **-3.201** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **+1014.8558** | 395.8149 | ±791.6298 | **+2.564** | **0.0103** | * |
| Site: UCSD (vs UAB) | +165.7682 | 266.1003 | ±532.2006 | +0.623 | 0.5333 |  |
| Site: UW (vs UAB) | -158.6598 | 239.8600 | ±479.7201 | -0.661 | 0.5083 |  |
| **Age (years)** | **-137.0931** | 9.2495 | ±18.4990 | **-14.822** | **1.06e-49** | *** |
| **BMI (kg/m2)** | **-32.6285** | 15.5693 | ±31.1386 | **-2.096** | **0.0361** | * |
| Hypertension | +157.6917 | 219.6327 | ±439.2654 | +0.718 | 0.4728 |  |
| High cholesterol | -47.1120 | 200.7440 | ±401.4881 | -0.235 | 0.8145 |  |
| **Kidney disease** | **-875.5653** | 335.9009 | ±671.8018 | **-2.607** | **0.0091** | ** |
| **Circulatory disease** | **-1022.2249** | 261.2230 | ±522.4460 | **-3.913** | **9.11e-05** | *** |
| **Time < 54 (%)** | **-348.5918** | 151.9798 | ±303.9597 | **-2.294** | **0.0218** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1872**, R² = **0.1415**, Adj R² = **0.1365**, F-statistic = **27.88** (p = **1.56e-54**), Residual SE = **4231.086** on **1860** df, AIC = **36587.7**, BIC = **36654.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19589.8418** | 802.5381 | ±1605.0761 | **+24.410** | **1.34e-131** | *** |
| **Education: graduate level (vs college)** | **-663.3500** | 205.9930 | ±411.9861 | **-3.220** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **+1017.3028** | 395.8753 | ±791.7507 | **+2.570** | **0.0102** | * |
| Site: UCSD (vs UAB) | +174.2309 | 265.8985 | ±531.7971 | +0.655 | 0.5123 |  |
| Site: UW (vs UAB) | -159.3448 | 240.1430 | ±480.2860 | -0.664 | 0.5070 |  |
| **Age (years)** | **-136.5557** | 9.2460 | ±18.4921 | **-14.769** | **2.32e-49** | *** |
| **BMI (kg/m2)** | **-32.5936** | 15.5458 | ±31.0917 | **-2.097** | **0.0360** | * |
| Hypertension | +157.4061 | 219.7365 | ±439.4730 | +0.716 | 0.4738 |  |
| High cholesterol | -45.5025 | 200.4942 | ±400.9884 | -0.227 | 0.8205 |  |
| **Kidney disease** | **-873.8506** | 335.9366 | ±671.8732 | **-2.601** | **0.0093** | ** |
| **Circulatory disease** | **-1023.0510** | 260.9774 | ±521.9548 | **-3.920** | **8.85e-05** | *** |
| **Avg. daily time < 54 (%)** | **-410.0104** | 153.2418 | ±306.4836 | **-2.676** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1872**, R² = **0.1421**, Adj R² = **0.1371**, F-statistic = **28.02** (p = **8.32e-55**), Residual SE = **4229.614** on **1860** df, AIC = **36586.4**, BIC = **36652.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19659.6330** | 805.0546 | ±1610.1093 | **+24.420** | **1.04e-131** | *** |
| **Education: graduate level (vs college)** | **-672.0860** | 205.4566 | ±410.9131 | **-3.271** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **+1019.0466** | 395.6047 | ±791.2094 | **+2.576** | **0.0100** | ** |
| Site: UCSD (vs UAB) | +171.6295 | 263.5367 | ±527.0734 | +0.651 | 0.5149 |  |
| Site: UW (vs UAB) | -159.3003 | 238.4631 | ±476.9261 | -0.668 | 0.5041 |  |
| **Age (years)** | **-136.9198** | 9.2395 | ±18.4790 | **-14.819** | **1.10e-49** | *** |
| **BMI (kg/m2)** | **-32.2678** | 15.6252 | ±31.2504 | **-2.065** | **0.0389** | * |
| Hypertension | +153.3877 | 220.0989 | ±440.1978 | +0.697 | 0.4859 |  |
| High cholesterol | -45.8605 | 200.5527 | ±401.1055 | -0.229 | 0.8191 |  |
| **Kidney disease** | **-880.2539** | 335.5008 | ±671.0016 | **-2.624** | **0.0087** | ** |
| **Circulatory disease** | **-1027.5040** | 261.2849 | ±522.5699 | **-3.933** | **8.41e-05** | *** |
| **Time 54-69, pooled (%)** | **-146.5658** | 62.7299 | ±125.4599 | **-2.336** | **0.0195** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1872**, R² = **0.1422**, Adj R² = **0.1372**, F-statistic = **28.04** (p = **7.65e-55**), Residual SE = **4229.415** on **1860** df, AIC = **36586.2**, BIC = **36652.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19629.0820** | 803.3523 | ±1606.7046 | **+24.434** | **7.45e-132** | *** |
| **Education: graduate level (vs college)** | **-674.1569** | 205.4752 | ±410.9505 | **-3.281** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **+1020.0662** | 395.4125 | ±790.8250 | **+2.580** | **0.0099** | ** |
| Site: UCSD (vs UAB) | +178.0260 | 263.5619 | ±527.1238 | +0.675 | 0.4994 |  |
| Site: UW (vs UAB) | -159.6630 | 238.7044 | ±477.4087 | -0.669 | 0.5036 |  |
| **Age (years)** | **-136.5781** | 9.2375 | ±18.4750 | **-14.785** | **1.83e-49** | *** |
| **BMI (kg/m2)** | **-32.2565** | 15.6169 | ±31.2338 | **-2.065** | **0.0389** | * |
| Hypertension | +153.5373 | 220.1838 | ±440.3676 | +0.697 | 0.4856 |  |
| High cholesterol | -43.9739 | 200.3642 | ±400.7285 | -0.219 | 0.8263 |  |
| **Kidney disease** | **-880.9209** | 335.4581 | ±670.9162 | **-2.626** | **0.0086** | ** |
| **Circulatory disease** | **-1028.7422** | 261.2163 | ±522.4326 | **-3.938** | **8.21e-05** | *** |
| **Avg. daily time 54-69 (%)** | **-146.6125** | 61.8471 | ±123.6943 | **-2.371** | **0.0178** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1872**, R² = **0.1424**, Adj R² = **0.1373**, F-statistic = **28.08** (p = **6.26e-55**), Residual SE = **4228.948** on **1860** df, AIC = **36585.8**, BIC = **36652.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19682.5114** | 806.0864 | ±1612.1728 | **+24.417** | **1.12e-131** | *** |
| **Education: graduate level (vs college)** | **-671.4359** | 205.4635 | ±410.9269 | **-3.268** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **+1012.2873** | 395.5824 | ±791.1648 | **+2.559** | **0.0105** | * |
| Site: UCSD (vs UAB) | +159.3511 | 264.1429 | ±528.2857 | +0.603 | 0.5463 |  |
| Site: UW (vs UAB) | -168.4529 | 238.7113 | ±477.4225 | -0.706 | 0.4804 |  |
| **Age (years)** | **-137.0385** | 9.2395 | ±18.4790 | **-14.832** | **9.13e-50** | *** |
| **BMI (kg/m2)** | **-32.3339** | 15.6182 | ±31.2364 | **-2.070** | **0.0384** | * |
| Hypertension | +152.5533 | 219.9541 | ±439.9082 | +0.694 | 0.4880 |  |
| High cholesterol | -50.8678 | 200.6398 | ±401.2796 | -0.254 | 0.7999 |  |
| **Kidney disease** | **-879.7320** | 335.4398 | ±670.8796 | **-2.623** | **0.0087** | ** |
| **Circulatory disease** | **-1023.8936** | 261.3157 | ±522.6313 | **-3.918** | **8.92e-05** | *** |
| **Time < 70 (%)** | **-124.6716** | 47.8648 | ±95.7297 | **-2.605** | **0.0092** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1872**, R² = **0.1424**, Adj R² = **0.1373**, F-statistic = **28.08** (p = **6.30e-55**), Residual SE = **4228.962** on **1860** df, AIC = **36585.8**, BIC = **36652.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19637.0766** | 803.6078 | ±1607.2157 | **+24.436** | **7.07e-132** | *** |
| **Education: graduate level (vs college)** | **-674.5639** | 205.5599 | ±411.1197 | **-3.282** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **+1015.1228** | 395.4172 | ±790.8345 | **+2.567** | **0.0103** | * |
| Site: UCSD (vs UAB) | +169.6826 | 264.0071 | ±528.0143 | +0.643 | 0.5204 |  |
| Site: UW (vs UAB) | -167.2324 | 238.9510 | ±477.9020 | -0.700 | 0.4840 |  |
| **Age (years)** | **-136.5596** | 9.2377 | ±18.4754 | **-14.783** | **1.89e-49** | *** |
| **BMI (kg/m2)** | **-32.3074** | 15.6056 | ±31.2112 | **-2.070** | **0.0384** | * |
| Hypertension | +152.8292 | 220.0731 | ±440.1463 | +0.694 | 0.4874 |  |
| High cholesterol | -47.8227 | 200.3808 | ±400.7616 | -0.239 | 0.8114 |  |
| **Kidney disease** | **-879.7932** | 335.4342 | ±670.8683 | **-2.623** | **0.0087** | ** |
| **Circulatory disease** | **-1025.8027** | 261.1634 | ±522.3268 | **-3.928** | **8.57e-05** | *** |
| **Avg. daily time < 70 (%)** | **-126.2298** | 48.9734 | ±97.9469 | **-2.578** | **0.0100** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1399**, Adj R² = **0.1348**, F-statistic = **27.50** (p = **8.76e-54**), Residual SE = **4235.133** on **1860** df, AIC = **36591.2**, BIC = **36657.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19580.4623** | 1464.1909 | ±2928.3818 | **+13.373** | **8.71e-41** | *** |
| **Education: graduate level (vs college)** | **-651.0922** | 208.2561 | ±416.5123 | **-3.126** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **+1042.0843** | 391.4437 | ±782.8875 | **+2.662** | **0.0078** | ** |
| Site: UCSD (vs UAB) | +221.4390 | 263.4883 | ±526.9766 | +0.840 | 0.4007 |  |
| Site: UW (vs UAB) | -113.0002 | 238.5524 | ±477.1048 | -0.474 | 0.6357 |  |
| **Age (years)** | **-136.6333** | 9.2448 | ±18.4896 | **-14.779** | **1.99e-49** | *** |
| **BMI (kg/m2)** | **-32.6314** | 15.5536 | ±31.1072 | **-2.098** | **0.0359** | * |
| Hypertension | +164.0234 | 220.2188 | ±440.4375 | +0.745 | 0.4564 |  |
| High cholesterol | -24.0967 | 200.5221 | ±401.0441 | -0.120 | 0.9043 |  |
| **Kidney disease** | **-876.4843** | 339.9736 | ±679.9473 | **-2.578** | **0.0099** | ** |
| **Circulatory disease** | **-1036.4138** | 262.0045 | ±524.0091 | **-3.956** | **7.63e-05** | *** |
| Time 54-250, pooled (%) | -0.7160 | 12.1972 | ±24.3944 | -0.059 | 0.9532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1399**, Adj R² = **0.1348**, F-statistic = **27.51** (p = **8.73e-54**), Residual SE = **4235.125** on **1860** df, AIC = **36591.2**, BIC = **36657.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19615.8198** | 1452.7296 | ±2905.4592 | **+13.503** | **1.51e-41** | *** |
| **Education: graduate level (vs college)** | **-650.6614** | 208.2638 | ±416.5277 | **-3.124** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **+1041.0585** | 391.7804 | ±783.5608 | **+2.657** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +221.8557 | 263.5187 | ±527.0375 | +0.842 | 0.3998 |  |
| Site: UW (vs UAB) | -112.4784 | 238.5962 | ±477.1924 | -0.471 | 0.6373 |  |
| **Age (years)** | **-136.6336** | 9.2490 | ±18.4980 | **-14.773** | **2.19e-49** | *** |
| **BMI (kg/m2)** | **-32.6629** | 15.5470 | ±31.0940 | **-2.101** | **0.0356** | * |
| Hypertension | +163.7217 | 220.2270 | ±440.4539 | +0.743 | 0.4572 |  |
| High cholesterol | -24.1615 | 200.5174 | ±401.0349 | -0.120 | 0.9041 |  |
| **Kidney disease** | **-877.4708** | 340.1310 | ±680.2621 | **-2.580** | **0.0099** | ** |
| **Circulatory disease** | **-1036.7749** | 262.0039 | ±524.0078 | **-3.957** | **7.59e-05** | *** |
| Avg. daily time 54-250 (%) | -1.0698 | 12.0412 | ±24.0825 | -0.089 | 0.9292 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1872**, R² = **0.1420**, Adj R² = **0.1369**, F-statistic = **27.98** (p = **1.00e-54**), Residual SE = **4230.050** on **1860** df, AIC = **36586.8**, BIC = **36653.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19595.5892** | 800.9629 | ±1601.9259 | **+24.465** | **3.48e-132** | *** |
| **Education: graduate level (vs college)** | **-647.8382** | 205.8940 | ±411.7880 | **-3.146** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **+983.3248** | 395.6189 | ±791.2379 | **+2.486** | **0.0129** | * |
| Site: UCSD (vs UAB) | +247.7118 | 264.2474 | ±528.4947 | +0.937 | 0.3485 |  |
| Site: UW (vs UAB) | -102.2929 | 239.1932 | ±478.3863 | -0.428 | 0.6689 |  |
| **Age (years)** | **-138.5830** | 9.3420 | ±18.6841 | **-14.834** | **8.79e-50** | *** |
| **BMI (kg/m2)** | **-35.1538** | 15.4763 | ±30.9526 | **-2.271** | **0.0231** | * |
| Hypertension | +129.4885 | 222.0862 | ±444.1724 | +0.583 | 0.5599 |  |
| High cholesterol | -47.5270 | 201.5273 | ±403.0546 | -0.236 | 0.8136 |  |
| **Kidney disease** | **-954.0064** | 343.1485 | ±686.2969 | **-2.780** | **0.0054** | ** |
| **Circulatory disease** | **-1055.8958** | 261.7464 | ±523.4928 | **-4.034** | **5.48e-05** | *** |
| Time 181-250, pooled (%) | +16.8881 | 9.5197 | ±19.0395 | +1.774 | 0.0761 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1419**, Adj R² = **0.1368**, F-statistic = **27.95** (p = **1.12e-54**), Residual SE = **4230.312** on **1860** df, AIC = **36587.0**, BIC = **36653.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19592.0594** | 801.6290 | ±1603.2581 | **+24.440** | **6.38e-132** | *** |
| **Education: graduate level (vs college)** | **-648.6275** | 205.8852 | ±411.7704 | **-3.150** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **+982.9452** | 394.8976 | ±789.7952 | **+2.489** | **0.0128** | * |
| Site: UCSD (vs UAB) | +249.3524 | 264.1790 | ±528.3580 | +0.944 | 0.3452 |  |
| Site: UW (vs UAB) | -101.1348 | 239.1499 | ±478.2998 | -0.423 | 0.6724 |  |
| **Age (years)** | **-138.4676** | 9.3456 | ±18.6912 | **-14.816** | **1.15e-49** | *** |
| **BMI (kg/m2)** | **-35.1158** | 15.4992 | ±30.9984 | **-2.266** | **0.0235** | * |
| Hypertension | +130.6395 | 221.8991 | ±443.7982 | +0.589 | 0.5560 |  |
| High cholesterol | -47.2868 | 201.4786 | ±402.9572 | -0.235 | 0.8144 |  |
| **Kidney disease** | **-952.0215** | 343.1741 | ±686.3482 | **-2.774** | **0.0055** | ** |
| **Circulatory disease** | **-1054.3056** | 261.9100 | ±523.8200 | **-4.025** | **5.69e-05** | *** |
| Avg. daily time 181-250 (%) | +16.2192 | 9.4294 | ±18.8589 | +1.720 | 0.0854 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1872**, R² = **0.1409**, Adj R² = **0.1358**, F-statistic = **27.72** (p = **3.22e-54**), Residual SE = **4232.783** on **1860** df, AIC = **36589.2**, BIC = **36655.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19536.2397** | 801.6137 | ±1603.2274 | **+24.371** | **3.46e-131** | *** |
| **Education: graduate level (vs college)** | **-640.6850** | 207.3270 | ±414.6540 | **-3.090** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **+994.6941** | 392.5453 | ±785.0906 | **+2.534** | **0.0113** | * |
| Site: UCSD (vs UAB) | +240.4883 | 263.7331 | ±527.4663 | +0.912 | 0.3618 |  |
| Site: UW (vs UAB) | -97.2478 | 238.8346 | ±477.6692 | -0.407 | 0.6839 |  |
| **Age (years)** | **-137.3513** | 9.3144 | ±18.6289 | **-14.746** | **3.26e-49** | *** |
| **BMI (kg/m2)** | **-34.3159** | 15.5184 | ±31.0367 | **-2.211** | **0.0270** | * |
| Hypertension | +141.6142 | 221.5607 | ±443.1214 | +0.639 | 0.5227 |  |
| High cholesterol | -35.9632 | 200.9099 | ±401.8199 | -0.179 | 0.8579 |  |
| **Kidney disease** | **-927.0999** | 344.0667 | ±688.1335 | **-2.695** | **0.0070** | ** |
| **Circulatory disease** | **-1050.7065** | 261.9266 | ±523.8532 | **-4.011** | **6.03e-05** | *** |
| Time > 180 (%) | +7.2985 | 6.5229 | ±13.0459 | +1.119 | 0.2632 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1872**, R² = **0.1408**, Adj R² = **0.1358**, F-statistic = **27.72** (p = **3.26e-54**), Residual SE = **4232.815** on **1860** df, AIC = **36589.2**, BIC = **36655.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19539.0315** | 801.8209 | ±1603.6417 | **+24.368** | **3.71e-131** | *** |
| **Education: graduate level (vs college)** | **-641.3901** | 207.2432 | ±414.4864 | **-3.095** | **0.0020** | ** |
| **Education: high school or below (vs college)** | **+994.5292** | 392.4512 | ±784.9025 | **+2.534** | **0.0113** | * |
| Site: UCSD (vs UAB) | +241.5815 | 263.6803 | ±527.3606 | +0.916 | 0.3596 |  |
| Site: UW (vs UAB) | -97.2082 | 238.8136 | ±477.6271 | -0.407 | 0.6840 |  |
| **Age (years)** | **-137.3649** | 9.3160 | ±18.6321 | **-14.745** | **3.31e-49** | *** |
| **BMI (kg/m2)** | **-34.3343** | 15.5259 | ±31.0519 | **-2.211** | **0.0270** | * |
| Hypertension | +142.2429 | 221.4676 | ±442.9353 | +0.642 | 0.5207 |  |
| High cholesterol | -36.0616 | 200.8901 | ±401.7801 | -0.180 | 0.8575 |  |
| **Kidney disease** | **-927.8305** | 344.2053 | ±688.4107 | **-2.696** | **0.0070** | ** |
| **Circulatory disease** | **-1050.5745** | 261.9975 | ±523.9950 | **-4.010** | **6.08e-05** | *** |
| Avg. daily time > 180 (%) | +7.2304 | 6.5046 | ±13.0091 | +1.112 | 0.2663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1872**, R² = **0.1409**, Adj R² = **0.1358**, F-statistic = **27.73** (p = **3.12e-54**), Residual SE = **4232.714** on **1860** df, AIC = **36589.1**, BIC = **36655.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19540.5977** | 801.5648 | ±1603.1296 | **+24.378** | **2.92e-131** | *** |
| **Education: graduate level (vs college)** | **-635.7160** | 208.4368 | ±416.8735 | **-3.050** | **0.0023** | ** |
| **Education: high school or below (vs college)** | **+996.9223** | 391.6242 | ±783.2483 | **+2.546** | **0.0109** | * |
| Site: UCSD (vs UAB) | +241.5889 | 263.1756 | ±526.3511 | +0.918 | 0.3586 |  |
| Site: UW (vs UAB) | -98.9624 | 238.7466 | ±477.4933 | -0.415 | 0.6785 |  |
| **Age (years)** | **-136.8464** | 9.2748 | ±18.5496 | **-14.755** | **2.87e-49** | *** |
| **BMI (kg/m2)** | **-35.1210** | 15.5167 | ±31.0335 | **-2.263** | **0.0236** | * |
| Hypertension | +147.9316 | 221.1113 | ±442.2227 | +0.669 | 0.5035 |  |
| High cholesterol | -32.0045 | 200.7595 | ±401.5189 | -0.159 | 0.8733 |  |
| **Kidney disease** | **-912.7001** | 342.0654 | ±684.1309 | **-2.668** | **0.0076** | ** |
| **Circulatory disease** | **-1049.8163** | 261.6707 | ±523.3414 | **-4.012** | **6.02e-05** | *** |
| Nocturnal time > 180 (%) | +7.4056 | 6.7412 | ±13.4823 | +1.099 | 0.2720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1418**, Adj R² = **0.1367**, F-statistic = **27.94** (p = **1.19e-54**), Residual SE = **4230.447** on **1860** df, AIC = **36587.1**, BIC = **36653.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19463.6874** | 802.4695 | ±1604.9391 | **+24.255** | **5.89e-130** | *** |
| **Education: graduate level (vs college)** | **-635.0167** | 206.6892 | ±413.3784 | **-3.072** | **0.0021** | ** |
| **Education: high school or below (vs college)** | **+1004.4713** | 395.0422 | ±790.0843 | **+2.543** | **0.0110** | * |
| Site: UCSD (vs UAB) | +236.1869 | 264.2907 | ±528.5814 | +0.894 | 0.3715 |  |
| Site: UW (vs UAB) | -104.1274 | 239.0584 | ±478.1168 | -0.436 | 0.6631 |  |
| **Age (years)** | **-138.2232** | 9.3203 | ±18.6406 | **-14.830** | **9.33e-50** | *** |
| **BMI (kg/m2)** | **-31.9988** | 15.5857 | ±31.1714 | **-2.053** | **0.0401** | * |
| Hypertension | +122.5708 | 221.9937 | ±443.9874 | +0.552 | 0.5809 |  |
| High cholesterol | -50.9783 | 200.8255 | ±401.6509 | -0.254 | 0.7996 |  |
| **Kidney disease** | **-943.7438** | 341.4032 | ±682.8063 | **-2.764** | **0.0057** | ** |
| **Circulatory disease** | **-1034.9672** | 262.1660 | ±524.3320 | **-3.948** | **7.89e-05** | *** |
| Any reading > 250 during wear (0/1) | +424.6565 | 221.2580 | ±442.5160 | +1.919 | 0.0549 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1872**, R² = **0.1399**, Adj R² = **0.1348**, F-statistic = **27.51** (p = **8.66e-54**), Residual SE = **4235.105** on **1860** df, AIC = **36591.2**, BIC = **36657.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19507.8136** | 800.9312 | ±1601.8623 | **+24.356** | **4.96e-131** | *** |
| **Education: graduate level (vs college)** | **-649.9583** | 208.1899 | ±416.3798 | **-3.122** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **+1039.2267** | 391.3359 | ±782.6719 | **+2.656** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +222.3148 | 263.5403 | ±527.0805 | +0.844 | 0.3989 |  |
| Site: UW (vs UAB) | -111.6679 | 238.5633 | ±477.1266 | -0.468 | 0.6397 |  |
| **Age (years)** | **-136.6183** | 9.2459 | ±18.4918 | **-14.776** | **2.09e-49** | *** |
| **BMI (kg/m2)** | **-32.7072** | 15.5569 | ±31.1139 | **-2.102** | **0.0355** | * |
| Hypertension | +163.0567 | 220.2177 | ±440.4355 | +0.740 | 0.4590 |  |
| High cholesterol | -24.3625 | 200.5021 | ±401.0042 | -0.122 | 0.9033 |  |
| **Kidney disease** | **-878.6655** | 340.0581 | ±680.1162 | **-2.584** | **0.0098** | ** |
| **Circulatory disease** | **-1037.1360** | 261.9798 | ±523.9596 | **-3.959** | **7.53e-05** | *** |
| Time > 250 (%) | +1.5938 | 12.2231 | ±24.4463 | +0.130 | 0.8963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,872)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1399**, Adj R² = **0.1348**, F-statistic = **27.51** (p = **8.63e-54**), Residual SE = **4235.096** on **1860** df, AIC = **36591.2**, BIC = **36657.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19508.2560** | 801.0619 | ±1602.1239 | **+24.353** | **5.39e-131** | *** |
| **Education: graduate level (vs college)** | **-649.7415** | 208.1810 | ±416.3620 | **-3.121** | **0.0018** | ** |
| **Education: high school or below (vs college)** | **+1038.6563** | 391.7034 | ±783.4068 | **+2.652** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +222.5885 | 263.5485 | ±527.0969 | +0.845 | 0.3983 |  |
| Site: UW (vs UAB) | -111.4317 | 238.6051 | ±477.2101 | -0.467 | 0.6405 |  |
| **Age (years)** | **-136.6236** | 9.2492 | ±18.4985 | **-14.771** | **2.24e-49** | *** |
| **BMI (kg/m2)** | **-32.7284** | 15.5496 | ±31.0992 | **-2.105** | **0.0353** | * |
| Hypertension | +162.9411 | 220.2297 | ±440.4594 | +0.740 | 0.4594 |  |
| High cholesterol | -24.3944 | 200.4993 | ±400.9986 | -0.122 | 0.9032 |  |
| **Kidney disease** | **-879.4087** | 340.1922 | ±680.3845 | **-2.585** | **0.0097** | ** |
| **Circulatory disease** | **-1037.4217** | 261.9765 | ±523.9530 | **-3.960** | **7.50e-05** | *** |
| Avg. daily time > 250 (%) | +1.8217 | 12.0703 | ±24.1405 | +0.151 | 0.8800 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 1,872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1872**, R² = **0.1606**, Adj R² = **0.1561**, F-statistic = **35.61** (p = **3.74e-64**), Residual SE = **12.699** on **1861** df, AIC = **14839.0**, BIC = **14899.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6103** | 2.4204 | ±4.8407 | **+21.323** | **6.88e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8683** | 0.6301 | ±1.2602 | **-2.965** | **0.0030** | ** |
| **Education: high school or below (vs college)** | **+2.9592** | 1.1560 | ±2.3119 | **+2.560** | **0.0105** | * |
| Site: UCSD (vs UAB) | +0.7218 | 0.8027 | ±1.6055 | +0.899 | 0.3685 |  |
| Site: UW (vs UAB) | +0.0237 | 0.7112 | ±1.4225 | +0.033 | 0.9734 |  |
| **Age (years)** | **-0.4494** | 0.0272 | ±0.0544 | **-16.524** | **2.44e-61** | *** |
| BMI (kg/m2) | +0.0263 | 0.0472 | ±0.0943 | +0.557 | 0.5773 |  |
| Hypertension | +0.2884 | 0.6508 | ±1.3017 | +0.443 | 0.6576 |  |
| High cholesterol | +0.0810 | 0.5959 | ±1.1918 | +0.136 | 0.8919 |  |
| Kidney disease | -1.5789 | 1.0076 | ±2.0153 | -1.567 | 0.1171 |  |
| **Circulatory disease** | **-2.7942** | 0.7684 | ±1.5368 | **-3.636** | **2.77e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1872**, R² = **0.1652**, Adj R² = **0.1602**, F-statistic = **33.46** (p = **1.65e-65**), Residual SE = **12.668** on **1860** df, AIC = **14830.8**, BIC = **14897.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.9579** | 2.9255 | ±5.8510 | **+16.051** | **5.60e-58** | *** |
| **Education: graduate level (vs college)** | **-1.7576** | 0.6317 | ±1.2633 | **-2.782** | **0.0054** | ** |
| **Education: high school or below (vs college)** | **+2.6053** | 1.1583 | ±2.3167 | **+2.249** | **0.0245** | * |
| Site: UCSD (vs UAB) | +0.7846 | 0.7988 | ±1.5975 | +0.982 | 0.3260 |  |
| Site: UW (vs UAB) | +0.1443 | 0.7075 | ±1.4150 | +0.204 | 0.8384 |  |
| **Age (years)** | **-0.4546** | 0.0273 | ±0.0546 | **-16.653** | **2.90e-62** | *** |
| BMI (kg/m2) | +0.0086 | 0.0475 | ±0.0950 | +0.181 | 0.8562 |  |
| Hypertension | +0.0798 | 0.6575 | ±1.3149 | +0.121 | 0.9033 |  |
| High cholesterol | -0.0910 | 0.5983 | ±1.1966 | -0.152 | 0.8792 |  |
| Kidney disease | -1.6900 | 1.0024 | ±2.0048 | -1.686 | 0.0918 | . |
| **Circulatory disease** | **-2.8408** | 0.7685 | ±1.5369 | **-3.697** | **2.18e-04** | *** |
| **HbA1c (%)** | **+0.9285** | 0.3437 | ±0.6874 | **+2.702** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1872**, R² = **0.1619**, Adj R² = **0.1570**, F-statistic = **32.67** (p = **5.57e-64**), Residual SE = **12.693** on **1860** df, AIC = **14838.1**, BIC = **14904.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9749** | 2.6043 | ±5.2087 | **+19.189** | **4.57e-82** | *** |
| **Education: graduate level (vs college)** | **-1.8351** | 0.6320 | ±1.2640 | **-2.904** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+2.7878** | 1.1519 | ±2.3037 | **+2.420** | **0.0155** | * |
| Site: UCSD (vs UAB) | +0.7654 | 0.8001 | ±1.6002 | +0.957 | 0.3388 |  |
| Site: UW (vs UAB) | +0.0574 | 0.7089 | ±1.4178 | +0.081 | 0.9355 |  |
| **Age (years)** | **-0.4517** | 0.0274 | ±0.0548 | **-16.481** | **4.99e-61** | *** |
| BMI (kg/m2) | +0.0198 | 0.0473 | ±0.0947 | +0.417 | 0.6766 |  |
| Hypertension | +0.1829 | 0.6576 | ±1.3153 | +0.278 | 0.7809 |  |
| High cholesterol | +0.0208 | 0.5971 | ±1.1942 | +0.035 | 0.9722 |  |
| Kidney disease | -1.7503 | 1.0184 | ±2.0368 | -1.719 | 0.0857 | . |
| **Circulatory disease** | **-2.8405** | 0.7700 | ±1.5400 | **-3.689** | **2.25e-04** | *** |
| Mean glucose (mg/dL) | +0.0154 | 0.0107 | ±0.0215 | +1.431 | 0.1526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1872**, R² = **0.1619**, Adj R² = **0.1570**, F-statistic = **32.67** (p = **5.57e-64**), Residual SE = **12.693** on **1860** df, AIC = **14838.1**, BIC = **14904.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8475** | 3.4478 | ±6.8955 | **+13.878** | **8.63e-44** | *** |
| **Education: graduate level (vs college)** | **-1.8351** | 0.6320 | ±1.2640 | **-2.904** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+2.7878** | 1.1519 | ±2.3037 | **+2.420** | **0.0155** | * |
| Site: UCSD (vs UAB) | +0.7654 | 0.8001 | ±1.6002 | +0.957 | 0.3388 |  |
| Site: UW (vs UAB) | +0.0574 | 0.7089 | ±1.4178 | +0.081 | 0.9355 |  |
| **Age (years)** | **-0.4517** | 0.0274 | ±0.0548 | **-16.481** | **4.99e-61** | *** |
| BMI (kg/m2) | +0.0198 | 0.0473 | ±0.0947 | +0.417 | 0.6766 |  |
| Hypertension | +0.1829 | 0.6576 | ±1.3153 | +0.278 | 0.7809 |  |
| High cholesterol | +0.0208 | 0.5971 | ±1.1942 | +0.035 | 0.9722 |  |
| Kidney disease | -1.7503 | 1.0184 | ±2.0368 | -1.719 | 0.0857 | . |
| **Circulatory disease** | **-2.8405** | 0.7700 | ±1.5400 | **-3.689** | **2.25e-04** | *** |
| GMI (%) | +0.6427 | 0.4493 | ±0.8986 | +1.431 | 0.1526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1872**, R² = **0.1626**, Adj R² = **0.1576**, F-statistic = **32.83** (p = **2.76e-64**), Residual SE = **12.688** on **1860** df, AIC = **14836.6**, BIC = **14903.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6090** | 2.6328 | ±5.2655 | **+18.843** | **3.35e-79** | *** |
| **Education: graduate level (vs college)** | **-1.8207** | 0.6326 | ±1.2652 | **-2.878** | **0.0040** | ** |
| **Education: high school or below (vs college)** | **+2.7511** | 1.1512 | ±2.3025 | **+2.390** | **0.0169** | * |
| Site: UCSD (vs UAB) | +0.7539 | 0.7999 | ±1.5998 | +0.942 | 0.3459 |  |
| Site: UW (vs UAB) | +0.0438 | 0.7095 | ±1.4190 | +0.062 | 0.9507 |  |
| **Age (years)** | **-0.4496** | 0.0273 | ±0.0545 | **-16.500** | **3.66e-61** | *** |
| BMI (kg/m2) | +0.0141 | 0.0475 | ±0.0950 | +0.298 | 0.7660 |  |
| Hypertension | +0.1813 | 0.6559 | ±1.3118 | +0.276 | 0.7822 |  |
| High cholesterol | +0.0083 | 0.5969 | ±1.1939 | +0.014 | 0.9889 |  |
| Kidney disease | -1.7103 | 1.0124 | ±2.0249 | -1.689 | 0.0912 | . |
| **Circulatory disease** | **-2.8414** | 0.7693 | ±1.5387 | **-3.693** | **2.21e-04** | *** |
| Nocturnal mean 00-06h (mg/dL) | +0.0189 | 0.0112 | ±0.0225 | +1.680 | 0.0929 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1872**, R² = **0.1620**, Adj R² = **0.1570**, F-statistic = **32.68** (p = **5.33e-64**), Residual SE = **12.692** on **1860** df, AIC = **14838.0**, BIC = **14904.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.8190** | 2.4489 | ±4.8978 | **+20.752** | **1.18e-95** | *** |
| **Education: graduate level (vs college)** | **-1.8184** | 0.6334 | ±1.2669 | **-2.871** | **0.0041** | ** |
| **Education: high school or below (vs college)** | **+2.7847** | 1.1538 | ±2.3075 | **+2.414** | **0.0158** | * |
| Site: UCSD (vs UAB) | +0.8114 | 0.8000 | ±1.6001 | +1.014 | 0.3105 |  |
| Site: UW (vs UAB) | +0.1115 | 0.7065 | ±1.4131 | +0.158 | 0.8746 |  |
| **Age (years)** | **-0.4535** | 0.0275 | ±0.0551 | **-16.461** | **6.98e-61** | *** |
| BMI (kg/m2) | +0.0227 | 0.0472 | ±0.0944 | +0.482 | 0.6300 |  |
| Hypertension | +0.1624 | 0.6608 | ±1.3215 | +0.246 | 0.8059 |  |
| High cholesterol | +0.0352 | 0.5973 | ±1.1946 | +0.059 | 0.9530 |  |
| Kidney disease | -1.8746 | 1.0410 | ±2.0820 | -1.801 | 0.0717 | . |
| **Circulatory disease** | **-2.8410** | 0.7695 | ±1.5390 | **-3.692** | **2.22e-04** | *** |
| Glucose SD, pooled (mg/dL) | +0.0454 | 0.0305 | ±0.0611 | +1.486 | 0.1373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1872**, R² = **0.1617**, Adj R² = **0.1567**, F-statistic = **32.61** (p = **7.34e-64**), Residual SE = **12.695** on **1860** df, AIC = **14838.7**, BIC = **14905.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9049** | 2.4484 | ±4.8969 | **+20.791** | **5.24e-96** | *** |
| **Education: graduate level (vs college)** | **-1.8289** | 0.6327 | ±1.2653 | **-2.891** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+2.7996** | 1.1570 | ±2.3139 | **+2.420** | **0.0155** | * |
| Site: UCSD (vs UAB) | +0.7968 | 0.8005 | ±1.6010 | +0.995 | 0.3196 |  |
| Site: UW (vs UAB) | +0.0924 | 0.7069 | ±1.4138 | +0.131 | 0.8960 |  |
| **Age (years)** | **-0.4535** | 0.0276 | ±0.0552 | **-16.439** | **1.01e-60** | *** |
| BMI (kg/m2) | +0.0240 | 0.0472 | ±0.0943 | +0.508 | 0.6111 |  |
| Hypertension | +0.1779 | 0.6604 | ±1.3208 | +0.269 | 0.7876 |  |
| High cholesterol | +0.0388 | 0.5978 | ±1.1956 | +0.065 | 0.9482 |  |
| Kidney disease | -1.8459 | 1.0384 | ±2.0769 | -1.778 | 0.0755 | . |
| **Circulatory disease** | **-2.8307** | 0.7696 | ±1.5392 | **-3.678** | **2.35e-04** | *** |
| Avg. daily SD (mg/dL) | +0.0453 | 0.0336 | ±0.0671 | +1.349 | 0.1774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1872**, R² = **0.1610**, Adj R² = **0.1560**, F-statistic = **32.45** (p = **1.55e-63**), Residual SE = **12.700** on **1860** df, AIC = **14840.2**, BIC = **14906.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7411** | 2.5966 | ±5.1933 | **+19.541** | **4.92e-85** | *** |
| **Education: graduate level (vs college)** | **-1.8450** | 0.6319 | ±1.2639 | **-2.920** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+2.9004** | 1.1580 | ±2.3161 | **+2.505** | **0.0123** | * |
| Site: UCSD (vs UAB) | +0.7771 | 0.8039 | ±1.6078 | +0.967 | 0.3338 |  |
| Site: UW (vs UAB) | +0.0758 | 0.7104 | ±1.4208 | +0.107 | 0.9150 |  |
| **Age (years)** | **-0.4518** | 0.0274 | ±0.0548 | **-16.488** | **4.50e-61** | *** |
| BMI (kg/m2) | +0.0266 | 0.0472 | ±0.0944 | +0.563 | 0.5732 |  |
| Hypertension | +0.2327 | 0.6570 | ±1.3140 | +0.354 | 0.7232 |  |
| High cholesterol | +0.0736 | 0.5964 | ±1.1928 | +0.123 | 0.9017 |  |
| Kidney disease | -1.7229 | 1.0323 | ±2.0646 | -1.669 | 0.0951 | . |
| **Circulatory disease** | **-2.8089** | 0.7689 | ±1.5379 | **-3.653** | **2.59e-04** | *** |
| CV (%) | +0.0520 | 0.0588 | ±0.1176 | +0.885 | 0.3759 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1872**, R² = **0.1624**, Adj R² = **0.1575**, F-statistic = **32.79** (p = **3.28e-64**), Residual SE = **12.689** on **1860** df, AIC = **14837.0**, BIC = **14903.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.4067** | 2.8255 | ±5.6509 | **+19.256** | **1.26e-82** | *** |
| **Education: graduate level (vs college)** | **-1.8178** | 0.6310 | ±1.2620 | **-2.881** | **0.0040** | ** |
| **Education: high school or below (vs college)** | **+2.8287** | 1.1561 | ±2.3121 | **+2.447** | **0.0144** | * |
| Site: UCSD (vs UAB) | +0.8311 | 0.8026 | ±1.6053 | +1.035 | 0.3005 |  |
| Site: UW (vs UAB) | +0.1066 | 0.7098 | ±1.4196 | +0.150 | 0.8806 |  |
| **Age (years)** | **-0.4546** | 0.0274 | ±0.0548 | **-16.579** | **9.87e-62** | *** |
| BMI (kg/m2) | +0.0267 | 0.0472 | ±0.0943 | +0.567 | 0.5709 |  |
| Hypertension | +0.1583 | 0.6565 | ±1.3129 | +0.241 | 0.8094 |  |
| High cholesterol | +0.0582 | 0.5959 | ±1.1919 | +0.098 | 0.9221 |  |
| Kidney disease | -1.8290 | 1.0242 | ±2.0483 | -1.786 | 0.0741 | . |
| **Circulatory disease** | **-2.8343** | 0.7684 | ±1.5368 | **-3.688** | **2.26e-04** | *** |
| **Mean / SD ratio** | **-0.4481** | 0.2226 | ±0.4452 | **-2.013** | **0.0441** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1872**, R² = **0.1629**, Adj R² = **0.1579**, F-statistic = **32.90** (p = **2.00e-64**), Residual SE = **12.686** on **1860** df, AIC = **14836.0**, BIC = **14902.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.7277** | 2.8101 | ±5.6203 | **+19.475** | **1.79e-84** | *** |
| **Education: graduate level (vs college)** | **-1.8243** | 0.6298 | ±1.2596 | **-2.897** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+2.8093** | 1.1576 | ±2.3152 | **+2.427** | **0.0152** | * |
| Site: UCSD (vs UAB) | +0.8131 | 0.8021 | ±1.6041 | +1.014 | 0.3107 |  |
| Site: UW (vs UAB) | +0.0946 | 0.7093 | ±1.4186 | +0.133 | 0.8939 |  |
| **Age (years)** | **-0.4564** | 0.0275 | ±0.0550 | **-16.605** | **6.39e-62** | *** |
| BMI (kg/m2) | +0.0271 | 0.0471 | ±0.0941 | +0.576 | 0.5649 |  |
| Hypertension | +0.1603 | 0.6537 | ±1.3075 | +0.245 | 0.8063 |  |
| High cholesterol | +0.0589 | 0.5958 | ±1.1916 | +0.099 | 0.9212 |  |
| Kidney disease | -1.8421 | 1.0183 | ±2.0366 | -1.809 | 0.0705 | . |
| **Circulatory disease** | **-2.8144** | 0.7684 | ±1.5369 | **-3.662** | **2.50e-04** | *** |
| **Avg. daily mean/SD** | **-0.4225** | 0.1822 | ±0.3644 | **-2.319** | **0.0204** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1872**, R² = **0.1703**, Adj R² = **0.1654**, F-statistic = **34.71** (p = **5.98e-68**), Residual SE = **12.629** on **1860** df, AIC = **14819.2**, BIC = **14885.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.2916** | 2.7626 | ±5.5253 | **+16.394** | **2.10e-60** | *** |
| **Education: graduate level (vs college)** | **-1.7274** | 0.6290 | ±1.2579 | **-2.746** | **0.0060** | ** |
| **Education: high school or below (vs college)** | **+2.6617** | 1.1443 | ±2.2885 | **+2.326** | **0.0200** | * |
| Site: UCSD (vs UAB) | +0.9699 | 0.7974 | ±1.5947 | +1.216 | 0.2238 |  |
| Site: UW (vs UAB) | +0.3712 | 0.7043 | ±1.4086 | +0.527 | 0.5982 |  |
| **Age (years)** | **-0.4474** | 0.0270 | ±0.0540 | **-16.569** | **1.16e-61** | *** |
| BMI (kg/m2) | +0.0218 | 0.0470 | ±0.0940 | +0.464 | 0.6423 |  |
| Hypertension | +0.2175 | 0.6492 | ±1.2984 | +0.335 | 0.7376 |  |
| High cholesterol | +0.0890 | 0.5930 | ±1.1860 | +0.150 | 0.8807 |  |
| **Kidney disease** | **-2.0009** | 1.0156 | ±2.0312 | **-1.970** | **0.0488** | * |
| **Circulatory disease** | **-2.7864** | 0.7650 | ±1.5301 | **-3.642** | **2.70e-04** | *** |
| **MAG (mg/dL/h)** | **+0.1546** | 0.0377 | ±0.0755 | **+4.096** | **4.20e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1872**, R² = **0.1625**, Adj R² = **0.1575**, F-statistic = **32.81** (p = **3.03e-64**), Residual SE = **12.689** on **1860** df, AIC = **14836.8**, BIC = **14903.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1033** | 2.5287 | ±5.0574 | **+19.814** | **2.26e-87** | *** |
| **Education: graduate level (vs college)** | **-1.8193** | 0.6319 | ±1.2639 | **-2.879** | **0.0040** | ** |
| **Education: high school or below (vs college)** | **+2.7482** | 1.1579 | ±2.3158 | **+2.373** | **0.0176** | * |
| Site: UCSD (vs UAB) | +0.8283 | 0.8006 | ±1.6011 | +1.035 | 0.3008 |  |
| Site: UW (vs UAB) | +0.1178 | 0.7073 | ±1.4145 | +0.167 | 0.8677 |  |
| **Age (years)** | **-0.4541** | 0.0275 | ±0.0550 | **-16.527** | **2.36e-61** | *** |
| BMI (kg/m2) | +0.0264 | 0.0472 | ±0.0944 | +0.559 | 0.5761 |  |
| Hypertension | +0.1682 | 0.6586 | ±1.3171 | +0.255 | 0.7984 |  |
| High cholesterol | +0.0315 | 0.5973 | ±1.1947 | +0.053 | 0.9580 |  |
| Kidney disease | -1.9138 | 1.0324 | ±2.0647 | -1.854 | 0.0638 | . |
| **Circulatory disease** | **-2.8431** | 0.7694 | ±1.5388 | **-3.695** | **2.20e-04** | *** |
| Avg. daily range (mg/dL) | +0.0163 | 0.0090 | ±0.0180 | +1.808 | 0.0705 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1872**, R² = **0.1629**, Adj R² = **0.1580**, F-statistic = **32.92** (p = **1.87e-64**), Residual SE = **12.685** on **1860** df, AIC = **14835.8**, BIC = **14902.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9836** | 2.4244 | ±4.8487 | **+21.030** | **3.51e-98** | *** |
| **Education: graduate level (vs college)** | **-1.7912** | 0.6348 | ±1.2695 | **-2.822** | **0.0048** | ** |
| **Education: high school or below (vs college)** | **+2.8171** | 1.1481 | ±2.2963 | **+2.454** | **0.0141** | * |
| Site: UCSD (vs UAB) | +0.8186 | 0.7987 | ±1.5974 | +1.025 | 0.3054 |  |
| Site: UW (vs UAB) | +0.1307 | 0.7080 | ±1.4161 | +0.185 | 0.8535 |  |
| **Age (years)** | **-0.4499** | 0.0272 | ±0.0545 | **-16.523** | **2.50e-61** | *** |
| BMI (kg/m2) | +0.0175 | 0.0472 | ±0.0945 | +0.371 | 0.7105 |  |
| Hypertension | +0.1656 | 0.6562 | ±1.3125 | +0.252 | 0.8008 |  |
| High cholesterol | +0.0299 | 0.5955 | ±1.1910 | +0.050 | 0.9599 |  |
| Kidney disease | -1.7944 | 1.0266 | ±2.0531 | -1.748 | 0.0805 | . |
| **Circulatory disease** | **-2.8955** | 0.7683 | ±1.5366 | **-3.769** | **1.64e-04** | *** |
| SD of daily means (mg/dL) | +0.1104 | 0.0573 | ±0.1145 | +1.928 | 0.0539 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1872**, R² = **0.1614**, Adj R² = **0.1564**, F-statistic = **32.54** (p = **9.96e-64**), Residual SE = **12.697** on **1860** df, AIC = **14839.3**, BIC = **14905.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.6652** | 3.1725 | ±6.3450 | **+16.916** | **3.44e-64** | *** |
| **Education: graduate level (vs college)** | **-1.8339** | 0.6341 | ±1.2681 | **-2.892** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+2.8277** | 1.1534 | ±2.3068 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | +0.7867 | 0.7989 | ±1.5978 | +0.985 | 0.3248 |  |
| Site: UW (vs UAB) | +0.0793 | 0.7063 | ±1.4126 | +0.112 | 0.9106 |  |
| **Age (years)** | **-0.4513** | 0.0274 | ±0.0549 | **-16.453** | **7.95e-61** | *** |
| BMI (kg/m2) | +0.0214 | 0.0472 | ±0.0945 | +0.454 | 0.6500 |  |
| Hypertension | +0.2266 | 0.6572 | ±1.3143 | +0.345 | 0.7303 |  |
| High cholesterol | +0.0523 | 0.5971 | ±1.1941 | +0.088 | 0.9302 |  |
| Kidney disease | -1.7225 | 1.0249 | ±2.0498 | -1.681 | 0.0928 | . |
| **Circulatory disease** | **-2.8372** | 0.7704 | ±1.5408 | **-3.683** | **2.31e-04** | *** |
| Time in range 70-180, pooled (%) | -0.0201 | 0.0186 | ±0.0372 | -1.081 | 0.2798 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1872**, R² = **0.1614**, Adj R² = **0.1564**, F-statistic = **32.54** (p = **1.00e-63**), Residual SE = **12.697** on **1860** df, AIC = **14839.3**, BIC = **14905.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.6614** | 3.1793 | ±6.3585 | **+16.879** | **6.47e-64** | *** |
| **Education: graduate level (vs college)** | **-1.8355** | 0.6339 | ±1.2678 | **-2.895** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+2.8267** | 1.1532 | ±2.3063 | **+2.451** | **0.0142** | * |
| Site: UCSD (vs UAB) | +0.7878 | 0.7987 | ±1.5974 | +0.986 | 0.3239 |  |
| Site: UW (vs UAB) | +0.0790 | 0.7062 | ±1.4124 | +0.112 | 0.9109 |  |
| **Age (years)** | **-0.4514** | 0.0274 | ±0.0549 | **-16.448** | **8.63e-61** | *** |
| BMI (kg/m2) | +0.0214 | 0.0473 | ±0.0945 | +0.452 | 0.6510 |  |
| Hypertension | +0.2282 | 0.6569 | ±1.3139 | +0.347 | 0.7283 |  |
| High cholesterol | +0.0514 | 0.5971 | ±1.1942 | +0.086 | 0.9314 |  |
| Kidney disease | -1.7245 | 1.0252 | ±2.0504 | -1.682 | 0.0926 | . |
| **Circulatory disease** | **-2.8365** | 0.7706 | ±1.5412 | **-3.681** | **2.32e-04** | *** |
| Avg. daily time in range 70-180 (%) | -0.0199 | 0.0185 | ±0.0371 | -1.074 | 0.2829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1872**, R² = **0.1615**, Adj R² = **0.1565**, F-statistic = **32.57** (p = **8.98e-64**), Residual SE = **12.696** on **1860** df, AIC = **14839.1**, BIC = **14905.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.1036** | 2.4560 | ±4.9120 | **+21.215** | **6.94e-100** | *** |
| **Education: graduate level (vs college)** | **-1.8785** | 0.6300 | ±1.2600 | **-2.982** | **0.0029** | ** |
| **Education: high school or below (vs college)** | **+2.8750** | 1.1551 | ±2.3102 | **+2.489** | **0.0128** | * |
| Site: UCSD (vs UAB) | +0.6004 | 0.8067 | ±1.6135 | +0.744 | 0.4567 |  |
| Site: UW (vs UAB) | -0.0356 | 0.7142 | ±1.4283 | -0.050 | 0.9602 |  |
| **Age (years)** | **-0.4523** | 0.0274 | ±0.0548 | **-16.506** | **3.31e-61** | *** |
| BMI (kg/m2) | +0.0278 | 0.0472 | ±0.0944 | +0.589 | 0.5561 |  |
| Hypertension | +0.2975 | 0.6511 | ±1.3022 | +0.457 | 0.6478 |  |
| High cholesterol | +0.0225 | 0.5955 | ±1.1910 | +0.038 | 0.9699 |  |
| Kidney disease | -1.6153 | 1.0070 | ±2.0140 | -1.604 | 0.1087 |  |
| **Circulatory disease** | **-2.7154** | 0.7697 | ±1.5395 | **-3.528** | **4.19e-04** | *** |
| Any reading < 54 during wear (0/1) | -0.8998 | 0.6428 | ±1.2855 | -1.400 | 0.1615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1872**, R² = **0.1614**, Adj R² = **0.1564**, F-statistic = **32.54** (p = **9.96e-64**), Residual SE = **12.697** on **1860** df, AIC = **14839.3**, BIC = **14905.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8698** | 2.4340 | ±4.8681 | **+21.310** | **9.14e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8818** | 0.6299 | ±1.2598 | **-2.988** | **0.0028** | ** |
| **Education: high school or below (vs college)** | **+2.8987** | 1.1566 | ±2.3131 | **+2.506** | **0.0122** | * |
| Site: UCSD (vs UAB) | +0.6094 | 0.8093 | ±1.6187 | +0.753 | 0.4515 |  |
| Site: UW (vs UAB) | -0.0675 | 0.7149 | ±1.4297 | -0.094 | 0.9248 |  |
| **Age (years)** | **-0.4503** | 0.0272 | ±0.0544 | **-16.550** | **1.60e-61** | *** |
| BMI (kg/m2) | +0.0262 | 0.0472 | ±0.0943 | +0.555 | 0.5790 |  |
| Hypertension | +0.2739 | 0.6504 | ±1.3009 | +0.421 | 0.6737 |  |
| High cholesterol | +0.0335 | 0.5965 | ±1.1930 | +0.056 | 0.9553 |  |
| Kidney disease | -1.5807 | 1.0065 | ±2.0129 | -1.571 | 0.1163 |  |
| **Circulatory disease** | **-2.7664** | 0.7689 | ±1.5378 | **-3.598** | **3.21e-04** | *** |
| Time < 54 (%) | -0.7158 | 0.3662 | ±0.7324 | -1.955 | 0.0506 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1872**, R² = **0.1616**, Adj R² = **0.1567**, F-statistic = **32.59** (p = **7.91e-64**), Residual SE = **12.695** on **1860** df, AIC = **14838.8**, BIC = **14905.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7976** | 2.4277 | ±4.8554 | **+21.336** | **5.26e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8949** | 0.6304 | ±1.2608 | **-3.006** | **0.0026** | ** |
| **Education: high school or below (vs college)** | **+2.8957** | 1.1565 | ±2.3130 | **+2.504** | **0.0123** | * |
| Site: UCSD (vs UAB) | +0.6130 | 0.8088 | ±1.6175 | +0.758 | 0.4485 |  |
| Site: UW (vs UAB) | -0.0823 | 0.7151 | ±1.4301 | -0.115 | 0.9084 |  |
| **Age (years)** | **-0.4492** | 0.0272 | ±0.0544 | **-16.517** | **2.77e-61** | *** |
| BMI (kg/m2) | +0.0262 | 0.0472 | ±0.0943 | +0.556 | 0.5781 |  |
| Hypertension | +0.2711 | 0.6506 | ±1.3011 | +0.417 | 0.6769 |  |
| High cholesterol | +0.0303 | 0.5960 | ±1.1920 | +0.051 | 0.9594 |  |
| Kidney disease | -1.5769 | 1.0064 | ±2.0128 | -1.567 | 0.1171 |  |
| **Circulatory disease** | **-2.7643** | 0.7686 | ±1.5373 | **-3.596** | **3.23e-04** | *** |
| Avg. daily time < 54 (%) | -0.9642 | 0.4963 | ±0.9925 | -1.943 | 0.0520 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1872**, R² = **0.1616**, Adj R² = **0.1567**, F-statistic = **32.60** (p = **7.83e-64**), Residual SE = **12.695** on **1860** df, AIC = **14838.8**, BIC = **14905.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.9127** | 2.4353 | ±4.8706 | **+21.317** | **7.94e-101** | *** |
| **Education: graduate level (vs college)** | **-1.9089** | 0.6292 | ±1.2584 | **-3.034** | **0.0024** | ** |
| **Education: high school or below (vs college)** | **+2.9081** | 1.1570 | ±2.3140 | **+2.513** | **0.0120** | * |
| Site: UCSD (vs UAB) | +0.6229 | 0.8030 | ±1.6060 | +0.776 | 0.4379 |  |
| Site: UW (vs UAB) | -0.0674 | 0.7118 | ±1.4236 | -0.095 | 0.9245 |  |
| **Age (years)** | **-0.4500** | 0.0272 | ±0.0544 | **-16.541** | **1.86e-61** | *** |
| BMI (kg/m2) | +0.0269 | 0.0473 | ±0.0946 | +0.568 | 0.5697 |  |
| Hypertension | +0.2654 | 0.6516 | ±1.3032 | +0.407 | 0.6838 |  |
| High cholesterol | +0.0367 | 0.5964 | ±1.1928 | +0.062 | 0.9510 |  |
| Kidney disease | -1.5901 | 1.0057 | ±2.0114 | -1.581 | 0.1138 |  |
| **Circulatory disease** | **-2.7775** | 0.7690 | ±1.5380 | **-3.612** | **3.04e-04** | *** |
| Time 54-69, pooled (%) | -0.2966 | 0.1833 | ±0.3665 | -1.618 | 0.1056 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1872**, R² = **0.1618**, Adj R² = **0.1568**, F-statistic = **32.64** (p = **6.55e-64**), Residual SE = **12.694** on **1860** df, AIC = **14838.4**, BIC = **14904.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8655** | 2.4308 | ±4.8615 | **+21.337** | **5.13e-101** | *** |
| **Education: graduate level (vs college)** | **-1.9158** | 0.6291 | ±1.2583 | **-3.045** | **0.0023** | ** |
| **Education: high school or below (vs college)** | **+2.9072** | 1.1566 | ±2.3132 | **+2.514** | **0.0120** | * |
| Site: UCSD (vs UAB) | +0.6306 | 0.8027 | ±1.6054 | +0.786 | 0.4321 |  |
| Site: UW (vs UAB) | -0.0737 | 0.7122 | ±1.4245 | -0.104 | 0.9175 |  |
| **Age (years)** | **-0.4493** | 0.0272 | ±0.0544 | **-16.522** | **2.53e-61** | *** |
| BMI (kg/m2) | +0.0270 | 0.0473 | ±0.0946 | +0.570 | 0.5689 |  |
| Hypertension | +0.2643 | 0.6517 | ±1.3035 | +0.406 | 0.6851 |  |
| High cholesterol | +0.0380 | 0.5959 | ±1.1918 | +0.064 | 0.9491 |  |
| Kidney disease | -1.5923 | 1.0055 | ±2.0109 | -1.584 | 0.1133 |  |
| **Circulatory disease** | **-2.7791** | 0.7689 | ±1.5379 | **-3.614** | **3.01e-04** | *** |
| Avg. daily time 54-69 (%) | -0.3147 | 0.1826 | ±0.3651 | -1.724 | 0.0847 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1872**, R² = **0.1617**, Adj R² = **0.1568**, F-statistic = **32.63** (p = **6.82e-64**), Residual SE = **12.694** on **1860** df, AIC = **14838.5**, BIC = **14904.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.9602** | 2.4381 | ±4.8762 | **+21.312** | **8.87e-101** | *** |
| **Education: graduate level (vs college)** | **-1.9077** | 0.6293 | ±1.2586 | **-3.032** | **0.0024** | ** |
| **Education: high school or below (vs college)** | **+2.8942** | 1.1569 | ±2.3139 | **+2.502** | **0.0124** | * |
| Site: UCSD (vs UAB) | +0.5976 | 0.8050 | ±1.6099 | +0.742 | 0.4579 |  |
| Site: UW (vs UAB) | -0.0863 | 0.7128 | ±1.4257 | -0.121 | 0.9036 |  |
| **Age (years)** | **-0.4502** | 0.0272 | ±0.0544 | **-16.548** | **1.66e-61** | *** |
| BMI (kg/m2) | +0.0268 | 0.0473 | ±0.0946 | +0.566 | 0.5714 |  |
| Hypertension | +0.2636 | 0.6513 | ±1.3026 | +0.405 | 0.6857 |  |
| High cholesterol | +0.0264 | 0.5966 | ±1.1932 | +0.044 | 0.9648 |  |
| Kidney disease | -1.5891 | 1.0055 | ±2.0111 | -1.580 | 0.1140 |  |
| **Circulatory disease** | **-2.7701** | 0.7692 | ±1.5384 | **-3.601** | **3.17e-04** | *** |
| Time < 70 (%) | -0.2532 | 0.1421 | ±0.2842 | -1.782 | 0.0748 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1872**, R² = **0.1619**, Adj R² = **0.1570**, F-statistic = **32.67** (p = **5.62e-64**), Residual SE = **12.693** on **1860** df, AIC = **14838.1**, BIC = **14904.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8879** | 2.4316 | ±4.8633 | **+21.339** | **4.97e-101** | *** |
| **Education: graduate level (vs college)** | **-1.9176** | 0.6294 | ±1.2588 | **-3.047** | **0.0023** | ** |
| **Education: high school or below (vs college)** | **+2.8953** | 1.1565 | ±2.3130 | **+2.503** | **0.0123** | * |
| Site: UCSD (vs UAB) | +0.6106 | 0.8041 | ±1.6082 | +0.759 | 0.4476 |  |
| Site: UW (vs UAB) | -0.0922 | 0.7130 | ±1.4261 | -0.129 | 0.8971 |  |
| **Age (years)** | **-0.4492** | 0.0272 | ±0.0544 | **-16.521** | **2.58e-61** | *** |
| BMI (kg/m2) | +0.0269 | 0.0473 | ±0.0946 | +0.568 | 0.5701 |  |
| Hypertension | +0.2623 | 0.6515 | ±1.3030 | +0.403 | 0.6873 |  |
| High cholesterol | +0.0288 | 0.5959 | ±1.1918 | +0.048 | 0.9615 |  |
| Kidney disease | -1.5900 | 1.0054 | ±2.0107 | -1.582 | 0.1138 |  |
| **Circulatory disease** | **-2.7724** | 0.7690 | ±1.5380 | **-3.605** | **3.12e-04** | *** |
| Avg. daily time < 70 (%) | -0.2762 | 0.1481 | ±0.2963 | -1.865 | 0.0622 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1607**, Adj R² = **0.1557**, F-statistic = **32.37** (p = **2.22e-63**), Residual SE = **12.702** on **1860** df, AIC = **14840.9**, BIC = **14907.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3432** | 4.2872 | ±8.5744 | **+12.209** | **2.78e-34** | *** |
| **Education: graduate level (vs college)** | **-1.8584** | 0.6366 | ±1.2731 | **-2.920** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+2.9360** | 1.1476 | ±2.2952 | **+2.558** | **0.0105** | * |
| Site: UCSD (vs UAB) | +0.7314 | 0.7992 | ±1.5984 | +0.915 | 0.3601 |  |
| Site: UW (vs UAB) | +0.0368 | 0.7060 | ±1.4119 | +0.052 | 0.9584 |  |
| **Age (years)** | **-0.4493** | 0.0272 | ±0.0543 | **-16.534** | **2.09e-61** | *** |
| BMI (kg/m2) | +0.0256 | 0.0473 | ±0.0945 | +0.542 | 0.5875 |  |
| Hypertension | +0.2805 | 0.6529 | ±1.3057 | +0.430 | 0.6675 |  |
| High cholesterol | +0.0796 | 0.5962 | ±1.1923 | +0.134 | 0.8937 |  |
| Kidney disease | -1.5974 | 1.0177 | ±2.0353 | -1.570 | 0.1165 |  |
| **Circulatory disease** | **-2.8009** | 0.7705 | ±1.5410 | **-3.635** | **2.78e-04** | *** |
| Time 54-250, pooled (%) | -0.0075 | 0.0343 | ±0.0686 | -0.218 | 0.8277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1607**, Adj R² = **0.1557**, F-statistic = **32.37** (p = **2.20e-63**), Residual SE = **12.702** on **1860** df, AIC = **14840.9**, BIC = **14907.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4355** | 4.2546 | ±8.5092 | **+12.324** | **6.69e-35** | *** |
| **Education: graduate level (vs college)** | **-1.8576** | 0.6366 | ±1.2732 | **-2.918** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+2.9338** | 1.1483 | ±2.2965 | **+2.555** | **0.0106** | * |
| Site: UCSD (vs UAB) | +0.7322 | 0.7993 | ±1.5986 | +0.916 | 0.3596 |  |
| Site: UW (vs UAB) | +0.0376 | 0.7062 | ±1.4124 | +0.053 | 0.9575 |  |
| **Age (years)** | **-0.4493** | 0.0272 | ±0.0544 | **-16.526** | **2.39e-61** | *** |
| BMI (kg/m2) | +0.0256 | 0.0473 | ±0.0945 | +0.541 | 0.5886 |  |
| Hypertension | +0.2801 | 0.6529 | ±1.3057 | +0.429 | 0.6679 |  |
| High cholesterol | +0.0795 | 0.5961 | ±1.1923 | +0.133 | 0.8940 |  |
| Kidney disease | -1.6005 | 1.0181 | ±2.0363 | -1.572 | 0.1160 |  |
| **Circulatory disease** | **-2.8020** | 0.7705 | ±1.5409 | **-3.637** | **2.76e-04** | *** |
| Avg. daily time 54-250 (%) | -0.0084 | 0.0339 | ±0.0678 | -0.247 | 0.8052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1872**, R² = **0.1624**, Adj R² = **0.1574**, F-statistic = **32.79** (p = **3.36e-64**), Residual SE = **12.689** on **1860** df, AIC = **14837.1**, BIC = **14903.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8508** | 2.4313 | ±4.8626 | **+21.326** | **6.46e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8565** | 0.6298 | ±1.2597 | **-2.948** | **0.0032** | ** |
| **Education: high school or below (vs college)** | **+2.7874** | 1.1605 | ±2.3210 | **+2.402** | **0.0163** | * |
| Site: UCSD (vs UAB) | +0.7984 | 0.8011 | ±1.6022 | +0.997 | 0.3190 |  |
| Site: UW (vs UAB) | +0.0574 | 0.7099 | ±1.4198 | +0.081 | 0.9355 |  |
| **Age (years)** | **-0.4549** | 0.0276 | ±0.0552 | **-16.484** | **4.80e-61** | *** |
| BMI (kg/m2) | +0.0190 | 0.0472 | ±0.0943 | +0.403 | 0.6869 |  |
| Hypertension | +0.1890 | 0.6583 | ±1.3165 | +0.287 | 0.7740 |  |
| High cholesterol | +0.0146 | 0.5989 | ±1.1977 | +0.024 | 0.9805 |  |
| Kidney disease | -1.8023 | 1.0198 | ±2.0397 | -1.767 | 0.0772 | . |
| **Circulatory disease** | **-2.8509** | 0.7699 | ±1.5397 | **-3.703** | **2.13e-04** | *** |
| Time 181-250, pooled (%) | +0.0476 | 0.0274 | ±0.0548 | +1.735 | 0.0827 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1623**, Adj R² = **0.1574**, F-statistic = **32.77** (p = **3.57e-64**), Residual SE = **12.690** on **1860** df, AIC = **14837.2**, BIC = **14903.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8433** | 2.4329 | ±4.8658 | **+21.309** | **9.32e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8586** | 0.6298 | ±1.2597 | **-2.951** | **0.0032** | ** |
| **Education: high school or below (vs college)** | **+2.7845** | 1.1587 | ±2.3174 | **+2.403** | **0.0163** | * |
| Site: UCSD (vs UAB) | +0.8039 | 0.8008 | ±1.6015 | +1.004 | 0.3154 |  |
| Site: UW (vs UAB) | +0.0611 | 0.7096 | ±1.4191 | +0.086 | 0.9314 |  |
| **Age (years)** | **-0.4546** | 0.0276 | ±0.0552 | **-16.475** | **5.55e-61** | *** |
| BMI (kg/m2) | +0.0190 | 0.0472 | ±0.0944 | +0.403 | 0.6868 |  |
| Hypertension | +0.1912 | 0.6579 | ±1.3158 | +0.291 | 0.7713 |  |
| High cholesterol | +0.0146 | 0.5988 | ±1.1976 | +0.024 | 0.9805 |  |
| Kidney disease | -1.7990 | 1.0199 | ±2.0398 | -1.764 | 0.0778 | . |
| **Circulatory disease** | **-2.8469** | 0.7703 | ±1.5406 | **-3.696** | **2.19e-04** | *** |
| Avg. daily time 181-250 (%) | +0.0462 | 0.0272 | ±0.0544 | +1.697 | 0.0896 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1872**, R² = **0.1616**, Adj R² = **0.1566**, F-statistic = **32.58** (p = **8.27e-64**), Residual SE = **12.696** on **1860** df, AIC = **14838.9**, BIC = **14905.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6889** | 2.4277 | ±4.8554 | **+21.291** | **1.37e-100** | *** |
| **Education: graduate level (vs college)** | **-1.8341** | 0.6334 | ±1.2668 | **-2.896** | **0.0038** | ** |
| **Education: high school or below (vs college)** | **+2.8095** | 1.1534 | ±2.3067 | **+2.436** | **0.0149** | * |
| Site: UCSD (vs UAB) | +0.7821 | 0.7990 | ±1.5981 | +0.979 | 0.3277 |  |
| Site: UW (vs UAB) | +0.0750 | 0.7070 | ±1.4140 | +0.106 | 0.9155 |  |
| **Age (years)** | **-0.4515** | 0.0274 | ±0.0549 | **-16.458** | **7.40e-61** | *** |
| BMI (kg/m2) | +0.0210 | 0.0473 | ±0.0945 | +0.445 | 0.6566 |  |
| Hypertension | +0.2185 | 0.6573 | ±1.3146 | +0.332 | 0.7396 |  |
| High cholesterol | +0.0448 | 0.5972 | ±1.1944 | +0.075 | 0.9402 |  |
| Kidney disease | -1.7370 | 1.0245 | ±2.0490 | -1.695 | 0.0900 | . |
| **Circulatory disease** | **-2.8392** | 0.7703 | ±1.5406 | **-3.686** | **2.28e-04** | *** |
| Time > 180 (%) | +0.0220 | 0.0184 | ±0.0369 | +1.194 | 0.2324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1872**, R² = **0.1616**, Adj R² = **0.1566**, F-statistic = **32.59** (p = **8.22e-64**), Residual SE = **12.695** on **1860** df, AIC = **14838.9**, BIC = **14905.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6982** | 2.4287 | ±4.8575 | **+21.286** | **1.53e-100** | *** |
| **Education: graduate level (vs college)** | **-1.8359** | 0.6332 | ±1.2665 | **-2.899** | **0.0037** | ** |
| **Education: high school or below (vs college)** | **+2.8075** | 1.1530 | ±2.3060 | **+2.435** | **0.0149** | * |
| Site: UCSD (vs UAB) | +0.7860 | 0.7988 | ±1.5976 | +0.984 | 0.3251 |  |
| Site: UW (vs UAB) | +0.0757 | 0.7069 | ±1.4138 | +0.107 | 0.9147 |  |
| **Age (years)** | **-0.4516** | 0.0274 | ±0.0549 | **-16.457** | **7.44e-61** | *** |
| BMI (kg/m2) | +0.0209 | 0.0473 | ±0.0946 | +0.442 | 0.6584 |  |
| Hypertension | +0.2197 | 0.6571 | ±1.3143 | +0.334 | 0.7381 |  |
| High cholesterol | +0.0441 | 0.5972 | ±1.1943 | +0.074 | 0.9411 |  |
| Kidney disease | -1.7409 | 1.0249 | ±2.0497 | -1.699 | 0.0894 | . |
| **Circulatory disease** | **-2.8393** | 0.7705 | ±1.5409 | **-3.685** | **2.28e-04** | *** |
| Avg. daily time > 180 (%) | +0.0220 | 0.0184 | ±0.0368 | +1.196 | 0.2316 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1872**, R² = **0.1614**, Adj R² = **0.1564**, F-statistic = **32.54** (p = **9.92e-64**), Residual SE = **12.697** on **1860** df, AIC = **14839.3**, BIC = **14905.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6923** | 2.4287 | ±4.8573 | **+21.284** | **1.59e-100** | *** |
| **Education: graduate level (vs college)** | **-1.8243** | 0.6364 | ±1.2727 | **-2.867** | **0.0041** | ** |
| **Education: high school or below (vs college)** | **+2.8314** | 1.1517 | ±2.3035 | **+2.458** | **0.0140** | * |
| Site: UCSD (vs UAB) | +0.7786 | 0.7979 | ±1.5958 | +0.976 | 0.3291 |  |
| Site: UW (vs UAB) | +0.0650 | 0.7069 | ±1.4138 | +0.092 | 0.9268 |  |
| **Age (years)** | **-0.4499** | 0.0273 | ±0.0546 | **-16.493** | **4.14e-61** | *** |
| BMI (kg/m2) | +0.0194 | 0.0473 | ±0.0946 | +0.410 | 0.6817 |  |
| Hypertension | +0.2430 | 0.6554 | ±1.3108 | +0.371 | 0.7108 |  |
| High cholesterol | +0.0593 | 0.5967 | ±1.1934 | +0.099 | 0.9208 |  |
| Kidney disease | -1.6814 | 1.0207 | ±2.0414 | -1.647 | 0.0995 | . |
| **Circulatory disease** | **-2.8321** | 0.7697 | ±1.5394 | **-3.679** | **2.34e-04** | *** |
| Nocturnal time > 180 (%) | +0.0200 | 0.0191 | ±0.0381 | +1.048 | 0.2947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1626**, Adj R² = **0.1577**, F-statistic = **32.84** (p = **2.64e-64**), Residual SE = **12.688** on **1860** df, AIC = **14836.6**, BIC = **14903.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4656** | 2.4225 | ±4.8450 | **+21.245** | **3.68e-100** | *** |
| **Education: graduate level (vs college)** | **-1.8154** | 0.6313 | ±1.2626 | **-2.876** | **0.0040** | ** |
| **Education: high school or below (vs college)** | **+2.8352** | 1.1577 | ±2.3154 | **+2.449** | **0.0143** | * |
| Site: UCSD (vs UAB) | +0.7706 | 0.8025 | ±1.6051 | +0.960 | 0.3370 |  |
| Site: UW (vs UAB) | +0.0552 | 0.7104 | ±1.4209 | +0.078 | 0.9380 |  |
| **Age (years)** | **-0.4543** | 0.0275 | ±0.0549 | **-16.541** | **1.87e-61** | *** |
| BMI (kg/m2) | +0.0281 | 0.0473 | ±0.0946 | +0.593 | 0.5530 |  |
| Hypertension | +0.1570 | 0.6558 | ±1.3116 | +0.239 | 0.8107 |  |
| High cholesterol | -0.0031 | 0.5981 | ±1.1963 | -0.005 | 0.9959 |  |
| Kidney disease | -1.7938 | 1.0190 | ±2.0381 | -1.760 | 0.0784 | . |
| **Circulatory disease** | **-2.7917** | 0.7711 | ±1.5422 | **-3.620** | **2.94e-04** | *** |
| **Any reading > 250 during wear (0/1)** | **+1.3216** | 0.6608 | ±1.3216 | **+2.000** | **0.0455** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1872**, R² = **0.1607**, Adj R² = **0.1557**, F-statistic = **32.37** (p = **2.17e-63**), Residual SE = **12.702** on **1860** df, AIC = **14840.9**, BIC = **14907.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.5965** | 2.4195 | ±4.8390 | **+21.325** | **6.63e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8562** | 0.6364 | ±1.2728 | **-2.917** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+2.9297** | 1.1474 | ±2.2948 | **+2.553** | **0.0107** | * |
| Site: UCSD (vs UAB) | +0.7322 | 0.7995 | ±1.5989 | +0.916 | 0.3597 |  |
| Site: UW (vs UAB) | +0.0388 | 0.7062 | ±1.4123 | +0.055 | 0.9562 |  |
| **Age (years)** | **-0.4492** | 0.0272 | ±0.0543 | **-16.531** | **2.18e-61** | *** |
| BMI (kg/m2) | +0.0255 | 0.0473 | ±0.0946 | +0.539 | 0.5899 |  |
| Hypertension | +0.2784 | 0.6529 | ±1.3058 | +0.426 | 0.6698 |  |
| High cholesterol | +0.0787 | 0.5961 | ±1.1922 | +0.132 | 0.8950 |  |
| Kidney disease | -1.6019 | 1.0177 | ±2.0355 | -1.574 | 0.1155 |  |
| **Circulatory disease** | **-2.8021** | 0.7704 | ±1.5408 | **-3.637** | **2.76e-04** | *** |
| Time > 250 (%) | +0.0093 | 0.0344 | ±0.0687 | +0.270 | 0.7875 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,872)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1872**, R² = **0.1607**, Adj R² = **0.1557**, F-statistic = **32.37** (p = **2.16e-63**), Residual SE = **12.702** on **1860** df, AIC = **14840.9**, BIC = **14907.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.5995** | 2.4205 | ±4.8411 | **+21.317** | **7.82e-101** | *** |
| **Education: graduate level (vs college)** | **-1.8556** | 0.6364 | ±1.2728 | **-2.916** | **0.0035** | ** |
| **Education: high school or below (vs college)** | **+2.9278** | 1.1481 | ±2.2963 | **+2.550** | **0.0108** | * |
| Site: UCSD (vs UAB) | +0.7333 | 0.7995 | ±1.5989 | +0.917 | 0.3590 |  |
| Site: UW (vs UAB) | +0.0394 | 0.7064 | ±1.4128 | +0.056 | 0.9555 |  |
| **Age (years)** | **-0.4493** | 0.0272 | ±0.0544 | **-16.525** | **2.43e-61** | *** |
| BMI (kg/m2) | +0.0254 | 0.0473 | ±0.0945 | +0.538 | 0.5909 |  |
| Hypertension | +0.2782 | 0.6529 | ±1.3058 | +0.426 | 0.6701 |  |
| High cholesterol | +0.0786 | 0.5961 | ±1.1922 | +0.132 | 0.8951 |  |
| Kidney disease | -1.6051 | 1.0182 | ±2.0363 | -1.576 | 0.1149 |  |
| **Circulatory disease** | **-2.8033** | 0.7703 | ±1.5407 | **-3.639** | **2.74e-04** | *** |
| Avg. daily time > 250 (%) | +0.0101 | 0.0339 | ±0.0679 | +0.298 | 0.7654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 1,877; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1877**, R² = **0.1647**, Adj R² = **0.1602**, F-statistic = **36.78** (p = **3.03e-66**), Residual SE = **8.122** on **1866** df, AIC = **13200.8**, BIC = **13261.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1352** | 1.6301 | ±3.2602 | **+40.571** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5560** | 0.4109 | ±0.8218 | **-3.787** | **1.53e-04** | *** |
| Education: high school or below (vs college) | +0.5018 | 0.6419 | ±1.2838 | +0.782 | 0.4344 |  |
| **Site: UCSD (vs UAB)** | **-1.9957** | 0.5099 | ±1.0198 | **-3.914** | **9.08e-05** | *** |
| **Site: UW (vs UAB)** | **-2.1941** | 0.4658 | ±0.9315 | **-4.711** | **2.47e-06** | *** |
| **Age (years)** | **-0.1650** | 0.0183 | ±0.0366 | **-9.014** | **1.98e-19** | *** |
| **BMI (kg/m2)** | **+0.2467** | 0.0297 | ±0.0594 | **+8.298** | **1.06e-16** | *** |
| **Hypertension** | **+1.5608** | 0.4223 | ±0.8446 | **+3.696** | **2.19e-04** | *** |
| High cholesterol | +0.2041 | 0.3939 | ±0.7878 | +0.518 | 0.6044 |  |
| **Kidney disease** | **+1.3304** | 0.6761 | ±1.3523 | **+1.968** | **0.0491** | * |
| Circulatory disease | -0.2649 | 0.5350 | ±1.0701 | -0.495 | 0.6205 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1877**, R² = **0.1966**, Adj R² = **0.1919**, F-statistic = **41.49** (p = **6.66e-81**), Residual SE = **7.967** on **1865** df, AIC = **13129.6**, BIC = **13196.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2266** | 1.9132 | ±3.8264 | **+30.434** | **1.95e-203** | *** |
| **Education: graduate level (vs college)** | **-1.3690** | 0.4054 | ±0.8108 | **-3.377** | **7.33e-04** | *** |
| Education: high school or below (vs college) | -0.1258 | 0.6179 | ±1.2357 | -0.204 | 0.8387 |  |
| **Site: UCSD (vs UAB)** | **-1.8995** | 0.5004 | ±1.0008 | **-3.796** | **1.47e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9890** | 0.4574 | ±0.9148 | **-4.349** | **1.37e-05** | *** |
| **Age (years)** | **-0.1737** | 0.0179 | ±0.0358 | **-9.716** | **2.57e-22** | *** |
| **BMI (kg/m2)** | **+0.2168** | 0.0292 | ±0.0584 | **+7.428** | **1.10e-13** | *** |
| **Hypertension** | **+1.2001** | 0.4184 | ±0.8367 | **+2.868** | **0.0041** | ** |
| High cholesterol | -0.0790 | 0.3905 | ±0.7810 | -0.202 | 0.8396 |  |
| Kidney disease | +1.1276 | 0.6772 | ±1.3545 | +1.665 | 0.0959 | . |
| Circulatory disease | -0.3428 | 0.5254 | ±1.0508 | -0.652 | 0.5141 |  |
| **HbA1c (%)** | **+1.5767** | 0.2034 | ±0.4068 | **+7.751** | **9.10e-15** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1877**, R² = **0.1990**, Adj R² = **0.1943**, F-statistic = **42.13** (p = **4.28e-82**), Residual SE = **7.955** on **1865** df, AIC = **13123.9**, BIC = **13190.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.7489** | 1.7588 | ±3.5175 | **+34.541** | **1.97e-261** | *** |
| **Education: graduate level (vs college)** | **-1.4451** | 0.4028 | ±0.8056 | **-3.587** | **3.34e-04** | *** |
| Education: high school or below (vs college) | -0.0893 | 0.6122 | ±1.2244 | -0.146 | 0.8841 |  |
| **Site: UCSD (vs UAB)** | **-1.8621** | 0.5009 | ±1.0018 | **-3.718** | **2.01e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0850** | 0.4548 | ±0.9097 | **-4.584** | **4.56e-06** | *** |
| **Age (years)** | **-0.1722** | 0.0179 | ±0.0357 | **-9.635** | **5.70e-22** | *** |
| **BMI (kg/m2)** | **+0.2256** | 0.0292 | ±0.0584 | **+7.722** | **1.14e-14** | *** |
| **Hypertension** | **+1.2075** | 0.4185 | ±0.8370 | **+2.885** | **0.0039** | ** |
| High cholesterol | +0.0128 | 0.3878 | ±0.7757 | +0.033 | 0.9737 |  |
| Kidney disease | +0.7657 | 0.6732 | ±1.3464 | +1.137 | 0.2554 |  |
| Circulatory disease | -0.4159 | 0.5264 | ±1.0528 | -0.790 | 0.4295 |  |
| **Mean glucose (mg/dL)** | **+0.0504** | 0.0064 | ±0.0128 | **+7.877** | **3.34e-15** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1877**, R² = **0.1990**, Adj R² = **0.1943**, F-statistic = **42.13** (p = **4.28e-82**), Residual SE = **7.955** on **1865** df, AIC = **13123.9**, BIC = **13190.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.7688** | 2.2885 | ±4.5769 | **+23.496** | **4.51e-122** | *** |
| **Education: graduate level (vs college)** | **-1.4451** | 0.4028 | ±0.8056 | **-3.587** | **3.34e-04** | *** |
| Education: high school or below (vs college) | -0.0893 | 0.6122 | ±1.2244 | -0.146 | 0.8841 |  |
| **Site: UCSD (vs UAB)** | **-1.8621** | 0.5009 | ±1.0018 | **-3.718** | **2.01e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0850** | 0.4548 | ±0.9097 | **-4.584** | **4.56e-06** | *** |
| **Age (years)** | **-0.1722** | 0.0179 | ±0.0357 | **-9.635** | **5.70e-22** | *** |
| **BMI (kg/m2)** | **+0.2256** | 0.0292 | ±0.0584 | **+7.722** | **1.14e-14** | *** |
| **Hypertension** | **+1.2075** | 0.4185 | ±0.8370 | **+2.885** | **0.0039** | ** |
| High cholesterol | +0.0128 | 0.3878 | ±0.7757 | +0.033 | 0.9737 |  |
| Kidney disease | +0.7657 | 0.6732 | ±1.3464 | +1.137 | 0.2554 |  |
| Circulatory disease | -0.4159 | 0.5264 | ±1.0528 | -0.790 | 0.4295 |  |
| **GMI (%)** | **+2.1088** | 0.2677 | ±0.5354 | **+7.877** | **3.34e-15** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1877**, R² = **0.1942**, Adj R² = **0.1894**, F-statistic = **40.86** (p = **1.06e-79**), Residual SE = **7.979** on **1865** df, AIC = **13135.2**, BIC = **13201.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.1400** | 1.7561 | ±3.5123 | **+34.815** | **1.45e-265** | *** |
| **Education: graduate level (vs college)** | **-1.4348** | 0.4049 | ±0.8099 | **-3.543** | **3.95e-04** | *** |
| Education: high school or below (vs college) | -0.0352 | 0.6129 | ±1.2258 | -0.057 | 0.9541 |  |
| **Site: UCSD (vs UAB)** | **-1.9226** | 0.5037 | ±1.0073 | **-3.817** | **1.35e-04** | *** |
| **Site: UW (vs UAB)** | **-2.1442** | 0.4558 | ±0.9115 | **-4.705** | **2.54e-06** | *** |
| **Age (years)** | **-0.1654** | 0.0180 | ±0.0359 | **-9.209** | **3.30e-20** | *** |
| **BMI (kg/m2)** | **+0.2167** | 0.0291 | ±0.0582 | **+7.443** | **9.88e-14** | *** |
| **Hypertension** | **+1.2884** | 0.4190 | ±0.8381 | **+3.075** | **0.0021** | ** |
| High cholesterol | +0.0267 | 0.3897 | ±0.7793 | +0.069 | 0.9454 |  |
| Kidney disease | +1.0018 | 0.6702 | ±1.3403 | +1.495 | 0.1350 |  |
| Circulatory disease | -0.3822 | 0.5264 | ±1.0528 | -0.726 | 0.4678 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0470** | 0.0064 | ±0.0128 | **+7.328** | **2.34e-13** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1877**, R² = **0.1926**, Adj R² = **0.1878**, F-statistic = **40.44** (p = **6.37e-79**), Residual SE = **7.987** on **1865** df, AIC = **13138.9**, BIC = **13205.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8222** | 1.6205 | ±3.2409 | **+39.385** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4081** | 0.4042 | ±0.8084 | **-3.484** | **4.94e-04** | *** |
| Education: high school or below (vs college) | -0.0455 | 0.6213 | ±1.2425 | -0.073 | 0.9417 |  |
| **Site: UCSD (vs UAB)** | **-1.7533** | 0.5022 | ±1.0044 | **-3.491** | **4.81e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9418** | 0.4564 | ±0.9128 | **-4.254** | **2.10e-05** | *** |
| **Age (years)** | **-0.1766** | 0.0180 | ±0.0359 | **-9.825** | **8.79e-23** | *** |
| **BMI (kg/m2)** | **+0.2366** | 0.0292 | ±0.0585 | **+8.090** | **5.99e-16** | *** |
| **Hypertension** | **+1.1812** | 0.4213 | ±0.8426 | **+2.804** | **0.0051** | ** |
| High cholesterol | +0.0829 | 0.3888 | ±0.7776 | +0.213 | 0.8312 |  |
| Kidney disease | +0.4586 | 0.6834 | ±1.3668 | +0.671 | 0.5022 |  |
| Circulatory disease | -0.3992 | 0.5265 | ±1.0530 | -0.758 | 0.4483 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1319** | 0.0183 | ±0.0366 | **+7.202** | **5.92e-13** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1877**, R² = **0.1911**, Adj R² = **0.1863**, F-statistic = **40.05** (p = **3.50e-78**), Residual SE = **7.995** on **1865** df, AIC = **13142.4**, BIC = **13208.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8704** | 1.6177 | ±3.2355 | **+39.481** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4260** | 0.4040 | ±0.8080 | **-3.530** | **4.16e-04** | *** |
| Education: high school or below (vs college) | -0.0456 | 0.6233 | ±1.2466 | -0.073 | 0.9417 |  |
| **Site: UCSD (vs UAB)** | **-1.7741** | 0.5025 | ±1.0050 | **-3.530** | **4.15e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9790** | 0.4570 | ±0.9140 | **-4.330** | **1.49e-05** | *** |
| **Age (years)** | **-0.1779** | 0.0180 | ±0.0360 | **-9.878** | **5.21e-23** | *** |
| **BMI (kg/m2)** | **+0.2394** | 0.0292 | ±0.0584 | **+8.195** | **2.51e-16** | *** |
| **Hypertension** | **+1.1943** | 0.4216 | ±0.8431 | **+2.833** | **0.0046** | ** |
| High cholesterol | +0.0803 | 0.3889 | ±0.7778 | +0.207 | 0.8364 |  |
| Kidney disease | +0.4628 | 0.6849 | ±1.3698 | +0.676 | 0.4992 |  |
| Circulatory disease | -0.3813 | 0.5260 | ±1.0519 | -0.725 | 0.4684 |  |
| **Avg. daily SD (mg/dL)** | **+0.1448** | 0.0206 | ±0.0411 | **+7.047** | **1.82e-12** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1877**, R² = **0.1740**, Adj R² = **0.1691**, F-statistic = **35.71** (p = **7.02e-70**), Residual SE = **8.079** on **1865** df, AIC = **13181.7**, BIC = **13248.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3264** | 1.6990 | ±3.3981 | **+37.272** | **4.70e-304** | *** |
| **Education: graduate level (vs college)** | **-1.4782** | 0.4084 | ±0.8167 | **-3.620** | **2.95e-04** | *** |
| Education: high school or below (vs college) | +0.2953 | 0.6399 | ±1.2797 | +0.461 | 0.6444 |  |
| **Site: UCSD (vs UAB)** | **-1.8259** | 0.5080 | ±1.0161 | **-3.594** | **3.26e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0277** | 0.4634 | ±0.9269 | **-4.375** | **1.21e-05** | *** |
| **Age (years)** | **-0.1725** | 0.0183 | ±0.0366 | **-9.434** | **3.94e-21** | *** |
| **BMI (kg/m2)** | **+0.2477** | 0.0295 | ±0.0590 | **+8.400** | **4.46e-17** | *** |
| **Hypertension** | **+1.3737** | 0.4237 | ±0.8474 | **+3.242** | **0.0012** | ** |
| High cholesterol | +0.1861 | 0.3917 | ±0.7834 | +0.475 | 0.6346 |  |
| Kidney disease | +0.8543 | 0.6843 | ±1.3686 | +1.248 | 0.2119 |  |
| Circulatory disease | -0.3129 | 0.5312 | ±1.0624 | -0.589 | 0.5559 |  |
| **CV (%)** | **+0.1681** | 0.0365 | ±0.0730 | **+4.605** | **4.12e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1877**, R² = **0.1757**, Adj R² = **0.1708**, F-statistic = **36.13** (p = **1.05e-70**), Residual SE = **8.071** on **1865** df, AIC = **13177.8**, BIC = **13244.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.5520** | 1.8549 | ±3.7097 | **+38.036** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4721** | 0.4078 | ±0.8156 | **-3.610** | **3.06e-04** | *** |
| Education: high school or below (vs college) | +0.2823 | 0.6379 | ±1.2759 | +0.442 | 0.6581 |  |
| **Site: UCSD (vs UAB)** | **-1.8342** | 0.5063 | ±1.0127 | **-3.622** | **2.92e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0683** | 0.4621 | ±0.9241 | **-4.476** | **7.60e-06** | *** |
| **Age (years)** | **-0.1730** | 0.0183 | ±0.0365 | **-9.480** | **2.54e-21** | *** |
| **BMI (kg/m2)** | **+0.2473** | 0.0294 | ±0.0588 | **+8.407** | **4.22e-17** | *** |
| **Hypertension** | **+1.3465** | 0.4234 | ±0.8467 | **+3.180** | **0.0015** | ** |
| High cholesterol | +0.1752 | 0.3914 | ±0.7828 | +0.448 | 0.6545 |  |
| Kidney disease | +0.9255 | 0.6781 | ±1.3562 | +1.365 | 0.1723 |  |
| Circulatory disease | -0.3284 | 0.5301 | ±1.0603 | -0.619 | 0.5356 |  |
| **Mean / SD ratio** | **-0.7076** | 0.1355 | ±0.2709 | **-5.223** | **1.76e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1877**, R² = **0.1741**, Adj R² = **0.1692**, F-statistic = **35.73** (p = **6.18e-70**), Residual SE = **8.078** on **1865** df, AIC = **13181.5**, BIC = **13247.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.2003** | 1.8552 | ±3.7104 | **+37.840** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4936** | 0.4080 | ±0.8159 | **-3.661** | **2.51e-04** | *** |
| Education: high school or below (vs college) | +0.2962 | 0.6395 | ±1.2790 | +0.463 | 0.6433 |  |
| **Site: UCSD (vs UAB)** | **-1.8889** | 0.5067 | ±1.0135 | **-3.728** | **1.93e-04** | *** |
| **Site: UW (vs UAB)** | **-2.1086** | 0.4630 | ±0.9260 | **-4.554** | **5.26e-06** | *** |
| **Age (years)** | **-0.1739** | 0.0183 | ±0.0367 | **-9.483** | **2.47e-21** | *** |
| **BMI (kg/m2)** | **+0.2475** | 0.0294 | ±0.0588 | **+8.423** | **3.66e-17** | *** |
| **Hypertension** | **+1.3850** | 0.4227 | ±0.8455 | **+3.276** | **0.0011** | ** |
| High cholesterol | +0.1822 | 0.3917 | ±0.7833 | +0.465 | 0.6418 |  |
| Kidney disease | +0.9785 | 0.6771 | ±1.3542 | +1.445 | 0.1484 |  |
| Circulatory disease | -0.2921 | 0.5309 | ±1.0618 | -0.550 | 0.5822 |  |
| **Avg. daily mean/SD** | **-0.5505** | 0.1121 | ±0.2242 | **-4.911** | **9.05e-07** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1877**, R² = **0.1832**, Adj R² = **0.1783**, F-statistic = **38.02** (p = **2.59e-74**), Residual SE = **8.034** on **1865** df, AIC = **13160.7**, BIC = **13227.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5423** | 1.8184 | ±3.6367 | **+33.295** | **4.60e-243** | *** |
| **Education: graduate level (vs college)** | **-1.4283** | 0.4066 | ±0.8133 | **-3.512** | **4.44e-04** | *** |
| Education: high school or below (vs college) | +0.2157 | 0.6267 | ±1.2533 | +0.344 | 0.7307 |  |
| **Site: UCSD (vs UAB)** | **-1.7847** | 0.5046 | ±1.0092 | **-3.537** | **4.05e-04** | *** |
| **Site: UW (vs UAB)** | **-1.8917** | 0.4643 | ±0.9285 | **-4.075** | **4.61e-05** | *** |
| **Age (years)** | **-0.1631** | 0.0180 | ±0.0360 | **-9.058** | **1.33e-19** | *** |
| **BMI (kg/m2)** | **+0.2432** | 0.0292 | ±0.0585 | **+8.321** | **8.74e-17** | *** |
| **Hypertension** | **+1.4851** | 0.4189 | ±0.8377 | **+3.546** | **3.92e-04** | *** |
| High cholesterol | +0.2158 | 0.3901 | ±0.7803 | +0.553 | 0.5802 |  |
| Kidney disease | +0.9560 | 0.6838 | ±1.3675 | +1.398 | 0.1621 |  |
| Circulatory disease | -0.2660 | 0.5277 | ±1.0554 | -0.504 | 0.6142 |  |
| **MAG (mg/dL/h)** | **+0.1365** | 0.0222 | ±0.0444 | **+6.147** | **7.91e-10** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1877**, R² = **0.1898**, Adj R² = **0.1850**, F-statistic = **39.71** (p = **1.52e-77**), Residual SE = **8.001** on **1865** df, AIC = **13145.4**, BIC = **13211.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5970** | 1.6590 | ±3.3180 | **+37.732** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4370** | 0.4046 | ±0.8091 | **-3.552** | **3.82e-04** | *** |
| Education: high school or below (vs college) | -0.0230 | 0.6234 | ±1.2469 | -0.037 | 0.9705 |  |
| **Site: UCSD (vs UAB)** | **-1.7620** | 0.5023 | ±1.0047 | **-3.508** | **4.52e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9783** | 0.4579 | ±0.9158 | **-4.320** | **1.56e-05** | *** |
| **Age (years)** | **-0.1758** | 0.0180 | ±0.0361 | **-9.740** | **2.03e-22** | *** |
| **BMI (kg/m2)** | **+0.2470** | 0.0293 | ±0.0587 | **+8.419** | **3.78e-17** | *** |
| **Hypertension** | **+1.2663** | 0.4211 | ±0.8421 | **+3.007** | **0.0026** | ** |
| High cholesterol | +0.0981 | 0.3889 | ±0.7779 | +0.252 | 0.8008 |  |
| Kidney disease | +0.5330 | 0.6845 | ±1.3690 | +0.779 | 0.4362 |  |
| Circulatory disease | -0.3799 | 0.5255 | ±1.0510 | -0.723 | 0.4698 |  |
| **Avg. daily range (mg/dL)** | **+0.0382** | 0.0052 | ±0.0105 | **+7.303** | **2.81e-13** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1877**, R² = **0.1903**, Adj R² = **0.1856**, F-statistic = **39.86** (p = **8.21e-78**), Residual SE = **7.998** on **1865** df, AIC = **13144.2**, BIC = **13210.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.7887** | 1.6068 | ±3.2136 | **+40.322** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.3912** | 0.4066 | ±0.8131 | **-3.422** | **6.22e-04** | *** |
| Education: high school or below (vs college) | +0.1619 | 0.6197 | ±1.2395 | +0.261 | 0.7939 |  |
| **Site: UCSD (vs UAB)** | **-1.8031** | 0.5039 | ±1.0077 | **-3.578** | **3.46e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9646** | 0.4575 | ±0.9150 | **-4.294** | **1.75e-05** | *** |
| **Age (years)** | **-0.1658** | 0.0180 | ±0.0360 | **-9.212** | **3.20e-20** | *** |
| **BMI (kg/m2)** | **+0.2285** | 0.0292 | ±0.0584 | **+7.822** | **5.19e-15** | *** |
| **Hypertension** | **+1.2874** | 0.4181 | ±0.8361 | **+3.080** | **0.0021** | ** |
| High cholesterol | +0.1038 | 0.3911 | ±0.7821 | +0.266 | 0.7906 |  |
| Kidney disease | +0.8710 | 0.6728 | ±1.3456 | +1.295 | 0.1955 |  |
| Circulatory disease | -0.4744 | 0.5308 | ±1.0615 | -0.894 | 0.3714 |  |
| **SD of daily means (mg/dL)** | **+0.2345** | 0.0355 | ±0.0710 | **+6.605** | **3.97e-11** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1877**, R² = **0.1976**, Adj R² = **0.1929**, F-statistic = **41.75** (p = **2.18e-81**), Residual SE = **7.963** on **1865** df, AIC = **13127.3**, BIC = **13193.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.7048** | 1.9006 | ±3.8012 | **+39.306** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4126** | 0.4039 | ±0.8079 | **-3.497** | **4.70e-04** | *** |
| Education: high school or below (vs college) | -0.0822 | 0.6127 | ±1.2253 | -0.134 | 0.8932 |  |
| **Site: UCSD (vs UAB)** | **-1.7354** | 0.5018 | ±1.0036 | **-3.458** | **5.43e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9615** | 0.4548 | ±0.9095 | **-4.313** | **1.61e-05** | *** |
| **Age (years)** | **-0.1726** | 0.0179 | ±0.0359 | **-9.629** | **6.01e-22** | *** |
| **BMI (kg/m2)** | **+0.2268** | 0.0291 | ±0.0583 | **+7.783** | **7.09e-15** | *** |
| **Hypertension** | **+1.2940** | 0.4188 | ±0.8376 | **+3.090** | **0.0020** | ** |
| High cholesterol | +0.0931 | 0.3883 | ±0.7766 | +0.240 | 0.8106 |  |
| Kidney disease | +0.7239 | 0.6767 | ±1.3534 | +1.070 | 0.2847 |  |
| Circulatory disease | -0.4426 | 0.5264 | ±1.0528 | -0.841 | 0.4004 |  |
| **Time in range 70-180, pooled (%)** | **-0.0841** | 0.0109 | ±0.0218 | **-7.725** | **1.12e-14** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1877**, R² = **0.1971**, Adj R² = **0.1923**, F-statistic = **41.61** (p = **3.95e-81**), Residual SE = **7.965** on **1865** df, AIC = **13128.5**, BIC = **13194.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.6657** | 1.9018 | ±3.8036 | **+39.261** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4190** | 0.4042 | ±0.8083 | **-3.511** | **4.46e-04** | *** |
| Education: high school or below (vs college) | -0.0843 | 0.6128 | ±1.2256 | -0.138 | 0.8905 |  |
| **Site: UCSD (vs UAB)** | **-1.7316** | 0.5020 | ±1.0039 | **-3.450** | **5.61e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9635** | 0.4549 | ±0.9098 | **-4.316** | **1.59e-05** | *** |
| **Age (years)** | **-0.1731** | 0.0179 | ±0.0359 | **-9.647** | **5.08e-22** | *** |
| **BMI (kg/m2)** | **+0.2266** | 0.0292 | ±0.0584 | **+7.766** | **8.10e-15** | *** |
| **Hypertension** | **+1.3016** | 0.4188 | ±0.8376 | **+3.108** | **0.0019** | ** |
| High cholesterol | +0.0897 | 0.3884 | ±0.7767 | +0.231 | 0.8173 |  |
| Kidney disease | +0.7176 | 0.6772 | ±1.3545 | +1.060 | 0.2893 |  |
| Circulatory disease | -0.4393 | 0.5269 | ±1.0538 | -0.834 | 0.4044 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0830** | 0.0108 | ±0.0216 | **-7.671** | **1.71e-14** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1877**, R² = **0.1647**, Adj R² = **0.1598**, F-statistic = **33.43** (p = **1.82e-65**), Residual SE = **8.124** on **1865** df, AIC = **13202.7**, BIC = **13269.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1969** | 1.6458 | ±3.2916 | **+40.222** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5571** | 0.4112 | ±0.8224 | **-3.787** | **1.53e-04** | *** |
| Education: high school or below (vs college) | +0.4919 | 0.6432 | ±1.2865 | +0.765 | 0.4444 |  |
| **Site: UCSD (vs UAB)** | **-2.0107** | 0.5139 | ±1.0277 | **-3.913** | **9.12e-05** | *** |
| **Site: UW (vs UAB)** | **-2.2017** | 0.4675 | ±0.9349 | **-4.710** | **2.48e-06** | *** |
| **Age (years)** | **-0.1653** | 0.0183 | ±0.0367 | **-9.017** | **1.93e-19** | *** |
| **BMI (kg/m2)** | **+0.2468** | 0.0298 | ±0.0595 | **+8.294** | **1.10e-16** | *** |
| **Hypertension** | **+1.5623** | 0.4226 | ±0.8452 | **+3.697** | **2.18e-04** | *** |
| High cholesterol | +0.1964 | 0.3960 | ±0.7920 | +0.496 | 0.6198 |  |
| Kidney disease | +1.3260 | 0.6768 | ±1.3536 | +1.959 | 0.0501 | . |
| Circulatory disease | -0.2553 | 0.5362 | ±1.0724 | -0.476 | 0.6339 |  |
| Any reading < 54 during wear (0/1) | -0.1124 | 0.4106 | ±0.8212 | -0.274 | 0.7842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1877**, R² = **0.1647**, Adj R² = **0.1598**, F-statistic = **33.44** (p = **1.72e-65**), Residual SE = **8.124** on **1865** df, AIC = **13202.6**, BIC = **13269.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0797** | 1.6357 | ±3.2714 | **+40.399** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5532** | 0.4110 | ±0.8219 | **-3.779** | **1.57e-04** | *** |
| Education: high school or below (vs college) | +0.5145 | 0.6426 | ±1.2853 | +0.801 | 0.4233 |  |
| **Site: UCSD (vs UAB)** | **-1.9716** | 0.5137 | ±1.0275 | **-3.838** | **1.24e-04** | *** |
| **Site: UW (vs UAB)** | **-2.1745** | 0.4682 | ±0.9363 | **-4.645** | **3.41e-06** | *** |
| **Age (years)** | **-0.1648** | 0.0183 | ±0.0366 | **-9.002** | **2.22e-19** | *** |
| **BMI (kg/m2)** | **+0.2467** | 0.0297 | ±0.0594 | **+8.299** | **1.05e-16** | *** |
| **Hypertension** | **+1.5637** | 0.4225 | ±0.8449 | **+3.701** | **2.14e-04** | *** |
| High cholesterol | +0.2143 | 0.3943 | ±0.7886 | +0.544 | 0.5868 |  |
| **Kidney disease** | **+1.3306** | 0.6764 | ±1.3528 | **+1.967** | **0.0492** | * |
| Circulatory disease | -0.2707 | 0.5346 | ±1.0691 | -0.506 | 0.6125 |  |
| Time < 54 (%) | +0.1529 | 0.2423 | ±0.4846 | +0.631 | 0.5280 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1877**, R² = **0.1647**, Adj R² = **0.1597**, F-statistic = **33.42** (p = **1.88e-65**), Residual SE = **8.124** on **1865** df, AIC = **13202.8**, BIC = **13269.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1255** | 1.6327 | ±3.2654 | **+40.501** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5546** | 0.4110 | ±0.8221 | **-3.782** | **1.55e-04** | *** |
| Education: high school or below (vs college) | +0.5050 | 0.6423 | ±1.2847 | +0.786 | 0.4318 |  |
| **Site: UCSD (vs UAB)** | **-1.9900** | 0.5134 | ±1.0268 | **-3.876** | **1.06e-04** | *** |
| **Site: UW (vs UAB)** | **-2.1886** | 0.4684 | ±0.9368 | **-4.673** | **2.97e-06** | *** |
| **Age (years)** | **-0.1650** | 0.0183 | ±0.0366 | **-9.010** | **2.06e-19** | *** |
| **BMI (kg/m2)** | **+0.2467** | 0.0297 | ±0.0595 | **+8.295** | **1.08e-16** | *** |
| **Hypertension** | **+1.5616** | 0.4226 | ±0.8452 | **+3.695** | **2.20e-04** | *** |
| High cholesterol | +0.2067 | 0.3944 | ±0.7888 | +0.524 | 0.6002 |  |
| **Kidney disease** | **+1.3303** | 0.6763 | ±1.3526 | **+1.967** | **0.0492** | * |
| Circulatory disease | -0.2664 | 0.5351 | ±1.0701 | -0.498 | 0.6185 |  |
| Avg. daily time < 54 (%) | +0.0497 | 0.3941 | ±0.7882 | +0.126 | 0.8997 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1877**, R² = **0.1650**, Adj R² = **0.1601**, F-statistic = **33.51** (p = **1.25e-65**), Residual SE = **8.122** on **1865** df, AIC = **13201.9**, BIC = **13268.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.2554** | 1.6380 | ±3.2760 | **+40.449** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5720** | 0.4117 | ±0.8234 | **-3.819** | **1.34e-04** | *** |
| Education: high school or below (vs college) | +0.4817 | 0.6419 | ±1.2839 | +0.750 | 0.4531 |  |
| **Site: UCSD (vs UAB)** | **-2.0354** | 0.5134 | ±1.0268 | **-3.965** | **7.35e-05** | *** |
| **Site: UW (vs UAB)** | **-2.2304** | 0.4682 | ±0.9364 | **-4.764** | **1.90e-06** | *** |
| **Age (years)** | **-0.1652** | 0.0183 | ±0.0366 | **-9.020** | **1.88e-19** | *** |
| **BMI (kg/m2)** | **+0.2469** | 0.0298 | ±0.0596 | **+8.289** | **1.14e-16** | *** |
| **Hypertension** | **+1.5518** | 0.4224 | ±0.8448 | **+3.674** | **2.39e-04** | *** |
| High cholesterol | +0.1863 | 0.3939 | ±0.7879 | +0.473 | 0.6363 |  |
| **Kidney disease** | **+1.3269** | 0.6757 | ±1.3514 | **+1.964** | **0.0496** | * |
| Circulatory disease | -0.2581 | 0.5358 | ±1.0715 | -0.482 | 0.6300 |  |
| Time 54-69, pooled (%) | -0.1179 | 0.1164 | ±0.2327 | -1.013 | 0.3109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1877**, R² = **0.1651**, Adj R² = **0.1601**, F-statistic = **33.52** (p = **1.21e-65**), Residual SE = **8.122** on **1865** df, AIC = **13201.9**, BIC = **13268.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.2323** | 1.6353 | ±3.2707 | **+40.501** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5740** | 0.4119 | ±0.8238 | **-3.822** | **1.33e-04** | *** |
| Education: high school or below (vs college) | +0.4822 | 0.6418 | ±1.2837 | +0.751 | 0.4525 |  |
| **Site: UCSD (vs UAB)** | **-2.0308** | 0.5126 | ±1.0252 | **-3.962** | **7.44e-05** | *** |
| **Site: UW (vs UAB)** | **-2.2312** | 0.4679 | ±0.9357 | **-4.769** | **1.85e-06** | *** |
| **Age (years)** | **-0.1649** | 0.0183 | ±0.0366 | **-9.004** | **2.17e-19** | *** |
| **BMI (kg/m2)** | **+0.2469** | 0.0298 | ±0.0596 | **+8.290** | **1.13e-16** | *** |
| **Hypertension** | **+1.5518** | 0.4225 | ±0.8449 | **+3.673** | **2.40e-04** | *** |
| High cholesterol | +0.1876 | 0.3938 | ±0.7876 | +0.477 | 0.6337 |  |
| **Kidney disease** | **+1.3263** | 0.6757 | ±1.3514 | **+1.963** | **0.0497** | * |
| Circulatory disease | -0.2589 | 0.5358 | ±1.0716 | -0.483 | 0.6290 |  |
| Avg. daily time 54-69 (%) | -0.1198 | 0.1178 | ±0.2356 | -1.017 | 0.3092 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1877**, R² = **0.1648**, Adj R² = **0.1599**, F-statistic = **33.46** (p = **1.57e-65**), Residual SE = **8.124** on **1865** df, AIC = **13202.4**, BIC = **13268.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.2223** | 1.6387 | ±3.2773 | **+40.412** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5657** | 0.4115 | ±0.8230 | **-3.805** | **1.42e-04** | *** |
| Education: high school or below (vs college) | +0.4857 | 0.6422 | ±1.2843 | +0.756 | 0.4494 |  |
| **Site: UCSD (vs UAB)** | **-2.0268** | 0.5145 | ±1.0289 | **-3.940** | **8.16e-05** | *** |
| **Site: UW (vs UAB)** | **-2.2216** | 0.4688 | ±0.9376 | **-4.739** | **2.15e-06** | *** |
| **Age (years)** | **-0.1652** | 0.0183 | ±0.0366 | **-9.020** | **1.88e-19** | *** |
| **BMI (kg/m2)** | **+0.2468** | 0.0298 | ±0.0595 | **+8.290** | **1.13e-16** | *** |
| **Hypertension** | **+1.5548** | 0.4224 | ±0.8449 | **+3.681** | **2.33e-04** | *** |
| High cholesterol | +0.1903 | 0.3942 | ±0.7884 | +0.483 | 0.6292 |  |
| **Kidney disease** | **+1.3285** | 0.6759 | ±1.3518 | **+1.965** | **0.0494** | * |
| Circulatory disease | -0.2588 | 0.5356 | ±1.0711 | -0.483 | 0.6289 |  |
| Time < 70 (%) | -0.0630 | 0.0909 | ±0.1818 | -0.693 | 0.4884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1877**, R² = **0.1649**, Adj R² = **0.1600**, F-statistic = **33.48** (p = **1.42e-65**), Residual SE = **8.123** on **1865** df, AIC = **13202.2**, BIC = **13268.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.2149** | 1.6351 | ±3.2703 | **+40.495** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5701** | 0.4117 | ±0.8235 | **-3.813** | **1.37e-04** | *** |
| Education: high school or below (vs college) | +0.4836 | 0.6420 | ±1.2840 | +0.753 | 0.4513 |  |
| **Site: UCSD (vs UAB)** | **-2.0279** | 0.5133 | ±1.0266 | **-3.951** | **7.79e-05** | *** |
| **Site: UW (vs UAB)** | **-2.2274** | 0.4684 | ±0.9368 | **-4.755** | **1.98e-06** | *** |
| **Age (years)** | **-0.1649** | 0.0183 | ±0.0366 | **-9.005** | **2.15e-19** | *** |
| **BMI (kg/m2)** | **+0.2468** | 0.0298 | ±0.0595 | **+8.290** | **1.13e-16** | *** |
| **Hypertension** | **+1.5535** | 0.4225 | ±0.8450 | **+3.677** | **2.36e-04** | *** |
| High cholesterol | +0.1890 | 0.3940 | ±0.7880 | +0.480 | 0.6314 |  |
| **Kidney disease** | **+1.3280** | 0.6758 | ±1.3516 | **+1.965** | **0.0494** | * |
| Circulatory disease | -0.2585 | 0.5358 | ±1.0715 | -0.482 | 0.6295 |  |
| Avg. daily time < 70 (%) | -0.0792 | 0.0987 | ±0.1973 | -0.803 | 0.4221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1877**, R² = **0.1769**, Adj R² = **0.1721**, F-statistic = **36.44** (p = **2.70e-71**), Residual SE = **8.065** on **1865** df, AIC = **13175.0**, BIC = **13241.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.1274** | 2.5023 | ±5.0045 | **+30.024** | **4.82e-198** | *** |
| **Education: graduate level (vs college)** | **-1.4363** | 0.4101 | ±0.8202 | **-3.503** | **4.61e-04** | *** |
| Education: high school or below (vs college) | +0.2002 | 0.6247 | ±1.2493 | +0.321 | 0.7486 |  |
| **Site: UCSD (vs UAB)** | **-1.8825** | 0.5068 | ±1.0136 | **-3.715** | **2.04e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0320** | 0.4634 | ±0.9267 | **-4.385** | **1.16e-05** | *** |
| **Age (years)** | **-0.1631** | 0.0181 | ±0.0362 | **-9.003** | **2.20e-19** | *** |
| **BMI (kg/m2)** | **+0.2390** | 0.0297 | ±0.0595 | **+8.037** | **9.23e-16** | *** |
| **Hypertension** | **+1.4586** | 0.4214 | ±0.8428 | **+3.461** | **5.38e-04** | *** |
| High cholesterol | +0.1928 | 0.3918 | ±0.7836 | +0.492 | 0.6228 |  |
| Kidney disease | +1.1001 | 0.6800 | ±1.3601 | +1.618 | 0.1057 |  |
| Circulatory disease | -0.3443 | 0.5302 | ±1.0605 | -0.649 | 0.5161 |  |
| **Time 54-250, pooled (%)** | **-0.0917** | 0.0207 | ±0.0415 | **-4.421** | **9.81e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1877**, R² = **0.1768**, Adj R² = **0.1719**, F-statistic = **36.41** (p = **3.03e-71**), Residual SE = **8.065** on **1865** df, AIC = **13175.3**, BIC = **13241.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.2887** | 2.5583 | ±5.1167 | **+29.429** | **2.36e-190** | *** |
| **Education: graduate level (vs college)** | **-1.4382** | 0.4101 | ±0.8201 | **-3.507** | **4.53e-04** | *** |
| Education: high school or below (vs college) | +0.2022 | 0.6252 | ±1.2503 | +0.323 | 0.7464 |  |
| **Site: UCSD (vs UAB)** | **-1.8849** | 0.5069 | ±1.0137 | **-3.719** | **2.00e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0386** | 0.4634 | ±0.9268 | **-4.399** | **1.09e-05** | *** |
| **Age (years)** | **-0.1637** | 0.0181 | ±0.0362 | **-9.033** | **1.68e-19** | *** |
| **BMI (kg/m2)** | **+0.2388** | 0.0298 | ±0.0596 | **+8.019** | **1.06e-15** | *** |
| **Hypertension** | **+1.4636** | 0.4213 | ±0.8427 | **+3.474** | **5.14e-04** | *** |
| High cholesterol | +0.1928 | 0.3918 | ±0.7836 | +0.492 | 0.6226 |  |
| Kidney disease | +1.0881 | 0.6804 | ±1.3608 | +1.599 | 0.1098 |  |
| Circulatory disease | -0.3489 | 0.5305 | ±1.0609 | -0.658 | 0.5107 |  |
| **Avg. daily time 54-250 (%)** | **-0.0928** | 0.0214 | ±0.0429 | **-4.331** | **1.49e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1877**, R² = **0.2004**, Adj R² = **0.1957**, F-statistic = **42.50** (p = **8.45e-83**), Residual SE = **7.948** on **1865** df, AIC = **13120.6**, BIC = **13187.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.8118** | 1.5786 | ±3.1572 | **+42.324** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5196** | 0.4014 | ±0.8028 | **-3.786** | **1.53e-04** | *** |
| Education: high school or below (vs college) | -0.0224 | 0.6219 | ±1.2438 | -0.036 | 0.9713 |  |
| **Site: UCSD (vs UAB)** | **-1.7869** | 0.5002 | ±1.0005 | **-3.572** | **3.54e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0994** | 0.4532 | ±0.9064 | **-4.633** | **3.61e-06** | *** |
| **Age (years)** | **-0.1805** | 0.0181 | ±0.0361 | **-9.996** | **1.58e-23** | *** |
| **BMI (kg/m2)** | **+0.2260** | 0.0288 | ±0.0577 | **+7.840** | **4.52e-15** | *** |
| **Hypertension** | **+1.2686** | 0.4180 | ±0.8360 | **+3.035** | **0.0024** | ** |
| High cholesterol | +0.0197 | 0.3879 | ±0.7757 | +0.051 | 0.9596 |  |
| Kidney disease | +0.6827 | 0.6700 | ±1.3399 | +1.019 | 0.3082 |  |
| Circulatory disease | -0.4279 | 0.5285 | ±1.0569 | -0.810 | 0.4181 |  |
| **Time 181-250, pooled (%)** | **+0.1368** | 0.0166 | ±0.0332 | **+8.245** | **1.64e-16** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1877**, R² = **0.1999**, Adj R² = **0.1951**, F-statistic = **42.35** (p = **1.65e-82**), Residual SE = **7.951** on **1865** df, AIC = **13122.0**, BIC = **13188.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.7968** | 1.5791 | ±3.1583 | **+42.299** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5253** | 0.4018 | ±0.8037 | **-3.796** | **1.47e-04** | *** |
| Education: high school or below (vs college) | -0.0330 | 0.6204 | ±1.2408 | -0.053 | 0.9576 |  |
| **Site: UCSD (vs UAB)** | **-1.7689** | 0.5003 | ±1.0006 | **-3.536** | **4.07e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0881** | 0.4534 | ±0.9069 | **-4.605** | **4.12e-06** | *** |
| **Age (years)** | **-0.1798** | 0.0180 | ±0.0361 | **-9.963** | **2.21e-23** | *** |
| **BMI (kg/m2)** | **+0.2259** | 0.0289 | ±0.0577 | **+7.827** | **4.98e-15** | *** |
| **Hypertension** | **+1.2731** | 0.4182 | ±0.8363 | **+3.045** | **0.0023** | ** |
| High cholesterol | +0.0176 | 0.3879 | ±0.7759 | +0.045 | 0.9638 |  |
| Kidney disease | +0.6873 | 0.6707 | ±1.3414 | +1.025 | 0.3055 |  |
| Circulatory disease | -0.4181 | 0.5292 | ±1.0584 | -0.790 | 0.4295 |  |
| **Avg. daily time 181-250 (%)** | **+0.1338** | 0.0164 | ±0.0328 | **+8.154** | **3.52e-16** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1877**, R² = **0.1974**, Adj R² = **0.1927**, F-statistic = **41.71** (p = **2.58e-81**), Residual SE = **7.963** on **1865** df, AIC = **13127.6**, BIC = **13194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.4121** | 1.5841 | ±3.1681 | **+41.925** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4270** | 0.4037 | ±0.8075 | **-3.534** | **4.09e-04** | *** |
| Education: high school or below (vs college) | -0.0968 | 0.6134 | ±1.2267 | -0.158 | 0.8747 |  |
| **Site: UCSD (vs UAB)** | **-1.7794** | 0.5016 | ±1.0031 | **-3.548** | **3.88e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0004** | 0.4546 | ±0.9092 | **-4.400** | **1.08e-05** | *** |
| **Age (years)** | **-0.1728** | 0.0179 | ±0.0359 | **-9.636** | **5.61e-22** | *** |
| **BMI (kg/m2)** | **+0.2272** | 0.0292 | ±0.0584 | **+7.780** | **7.23e-15** | *** |
| **Hypertension** | **+1.2891** | 0.4189 | ±0.8379 | **+3.077** | **0.0021** | ** |
| High cholesterol | +0.0762 | 0.3884 | ±0.7769 | +0.196 | 0.8444 |  |
| Kidney disease | +0.7282 | 0.6760 | ±1.3521 | +1.077 | 0.2814 |  |
| Circulatory disease | -0.4327 | 0.5273 | ±1.0546 | -0.821 | 0.4119 |  |
| **Time > 180 (%)** | **+0.0831** | 0.0108 | ±0.0215 | **+7.720** | **1.17e-14** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1877**, R² = **0.1971**, Adj R² = **0.1924**, F-statistic = **41.63** (p = **3.61e-81**), Residual SE = **7.965** on **1865** df, AIC = **13128.3**, BIC = **13194.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.4455** | 1.5853 | ±3.1706 | **+41.914** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4345** | 0.4039 | ±0.8078 | **-3.552** | **3.83e-04** | *** |
| Education: high school or below (vs college) | -0.0998 | 0.6134 | ±1.2267 | -0.163 | 0.8708 |  |
| **Site: UCSD (vs UAB)** | **-1.7667** | 0.5017 | ±1.0034 | **-3.521** | **4.29e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9996** | 0.4547 | ±0.9095 | **-4.397** | **1.10e-05** | *** |
| **Age (years)** | **-0.1730** | 0.0179 | ±0.0359 | **-9.641** | **5.35e-22** | *** |
| **BMI (kg/m2)** | **+0.2269** | 0.0292 | ±0.0585 | **+7.762** | **8.37e-15** | *** |
| **Hypertension** | **+1.2955** | 0.4190 | ±0.8379 | **+3.092** | **0.0020** | ** |
| High cholesterol | +0.0747 | 0.3884 | ±0.7767 | +0.192 | 0.8474 |  |
| Kidney disease | +0.7186 | 0.6766 | ±1.3532 | +1.062 | 0.2882 |  |
| Circulatory disease | -0.4316 | 0.5277 | ±1.0555 | -0.818 | 0.4135 |  |
| **Avg. daily time > 180 (%)** | **+0.0825** | 0.0107 | ±0.0214 | **+7.696** | **1.41e-14** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1877**, R² = **0.1868**, Adj R² = **0.1820**, F-statistic = **38.94** (p = **4.57e-76**), Residual SE = **8.016** on **1865** df, AIC = **13152.4**, BIC = **13218.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.4050** | 1.5967 | ±3.1934 | **+41.589** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4057** | 0.4084 | ±0.8169 | **-3.442** | **5.78e-04** | *** |
| Education: high school or below (vs college) | +0.0447 | 0.6147 | ±1.2295 | +0.073 | 0.9421 |  |
| **Site: UCSD (vs UAB)** | **-1.8076** | 0.5054 | ±1.0107 | **-3.577** | **3.48e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0514** | 0.4577 | ±0.9154 | **-4.482** | **7.38e-06** | *** |
| **Age (years)** | **-0.1667** | 0.0181 | ±0.0362 | **-9.215** | **3.12e-20** | *** |
| **BMI (kg/m2)** | **+0.2234** | 0.0294 | ±0.0587 | **+7.610** | **2.74e-14** | *** |
| **Hypertension** | **+1.3997** | 0.4211 | ±0.8423 | **+3.324** | **8.88e-04** | *** |
| High cholesterol | +0.1355 | 0.3915 | ±0.7831 | +0.346 | 0.7293 |  |
| Kidney disease | +0.9753 | 0.6742 | ±1.3483 | +1.447 | 0.1480 |  |
| Circulatory disease | -0.3926 | 0.5289 | ±1.0579 | -0.742 | 0.4580 |  |
| **Nocturnal time > 180 (%)** | **+0.0683** | 0.0109 | ±0.0217 | **+6.283** | **3.32e-10** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1877**, R² = **0.1844**, Adj R² = **0.1795**, F-statistic = **38.32** (p = **6.76e-75**), Residual SE = **8.028** on **1865** df, AIC = **13158.0**, BIC = **13224.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.8409** | 1.6087 | ±3.2174 | **+40.928** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4535** | 0.4068 | ±0.8136 | **-3.573** | **3.53e-04** | *** |
| Education: high school or below (vs college) | +0.2475 | 0.6224 | ±1.2447 | +0.398 | 0.6909 |  |
| **Site: UCSD (vs UAB)** | **-1.8972** | 0.5034 | ±1.0069 | **-3.769** | **1.64e-04** | *** |
| **Site: UW (vs UAB)** | **-2.1297** | 0.4589 | ±0.9178 | **-4.641** | **3.47e-06** | *** |
| **Age (years)** | **-0.1748** | 0.0182 | ±0.0364 | **-9.597** | **8.26e-22** | *** |
| **BMI (kg/m2)** | **+0.2502** | 0.0294 | ±0.0588 | **+8.510** | **1.74e-17** | *** |
| **Hypertension** | **+1.2966** | 0.4215 | ±0.8429 | **+3.076** | **0.0021** | ** |
| High cholesterol | +0.0390 | 0.3914 | ±0.7827 | +0.100 | 0.9206 |  |
| Kidney disease | +0.8889 | 0.6788 | ±1.3577 | +1.309 | 0.1904 |  |
| Circulatory disease | -0.2547 | 0.5312 | ±1.0624 | -0.479 | 0.6316 |  |
| **Any reading > 250 during wear (0/1)** | **+2.6579** | 0.4056 | ±0.8112 | **+6.553** | **5.64e-11** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1877**, R² = **0.1768**, Adj R² = **0.1719**, F-statistic = **36.41** (p = **3.08e-71**), Residual SE = **8.065** on **1865** df, AIC = **13175.3**, BIC = **13241.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.9881** | 1.6209 | ±3.2419 | **+40.710** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4387** | 0.4101 | ±0.8202 | **-3.508** | **4.51e-04** | *** |
| Education: high school or below (vs college) | +0.1942 | 0.6250 | ±1.2499 | +0.311 | 0.7560 |  |
| **Site: UCSD (vs UAB)** | **-1.8975** | 0.5067 | ±1.0135 | **-3.745** | **1.81e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0446** | 0.4631 | ±0.9263 | **-4.415** | **1.01e-05** | *** |
| **Age (years)** | **-0.1632** | 0.0181 | ±0.0362 | **-9.009** | **2.07e-19** | *** |
| **BMI (kg/m2)** | **+0.2390** | 0.0298 | ±0.0595 | **+8.035** | **9.36e-16** | *** |
| **Hypertension** | **+1.4574** | 0.4214 | ±0.8429 | **+3.458** | **5.44e-04** | *** |
| High cholesterol | +0.1867 | 0.3919 | ±0.7838 | +0.476 | 0.6338 |  |
| Kidney disease | +1.1012 | 0.6799 | ±1.3597 | +1.620 | 0.1053 |  |
| Circulatory disease | -0.3404 | 0.5305 | ±1.0610 | -0.642 | 0.5211 |  |
| **Time > 250 (%)** | **+0.0912** | 0.0207 | ±0.0414 | **+4.411** | **1.03e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,877)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1877**, R² = **0.1768**, Adj R² = **0.1719**, F-statistic = **36.41** (p = **3.11e-71**), Residual SE = **8.065** on **1865** df, AIC = **13175.3**, BIC = **13241.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.0254** | 1.6222 | ±3.2444 | **+40.701** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.4408** | 0.4100 | ±0.8200 | **-3.514** | **4.41e-04** | *** |
| Education: high school or below (vs college) | +0.1964 | 0.6254 | ±1.2508 | +0.314 | 0.7535 |  |
| **Site: UCSD (vs UAB)** | **-1.8955** | 0.5068 | ±1.0136 | **-3.740** | **1.84e-04** | *** |
| **Site: UW (vs UAB)** | **-2.0490** | 0.4632 | ±0.9264 | **-4.424** | **9.70e-06** | *** |
| **Age (years)** | **-0.1637** | 0.0181 | ±0.0362 | **-9.031** | **1.70e-19** | *** |
| **BMI (kg/m2)** | **+0.2388** | 0.0298 | ±0.0596 | **+8.017** | **1.08e-15** | *** |
| **Hypertension** | **+1.4621** | 0.4214 | ±0.8428 | **+3.470** | **5.21e-04** | *** |
| High cholesterol | +0.1879 | 0.3918 | ±0.7836 | +0.480 | 0.6315 |  |
| Kidney disease | +1.0886 | 0.6803 | ±1.3605 | +1.600 | 0.1095 |  |
| Circulatory disease | -0.3460 | 0.5307 | ±1.0614 | -0.652 | 0.5144 |  |
| **Avg. daily time > 250 (%)** | **+0.0927** | 0.0214 | ±0.0428 | **+4.330** | **1.49e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 1,893; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1893**, R² = **0.0389**, Adj R² = **0.0338**, F-statistic = **7.61** (p = **5.23e-12**), Residual SE = **66.792** on **1882** df, AIC = **21290.3**, BIC = **21351.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.1270** | 12.6616 | ±25.3232 | **+31.049** | **1.19e-211** | *** |
| Education: graduate level (vs college) | +2.3687 | 3.3329 | ±6.6657 | +0.711 | 0.4773 |  |
| **Education: high school or below (vs college)** | **-15.5398** | 5.3530 | ±10.7060 | **-2.903** | **0.0037** | ** |
| **Site: UCSD (vs UAB)** | **-11.1114** | 4.0828 | ±8.1656 | **-2.722** | **0.0065** | ** |
| Site: UW (vs UAB) | -1.8345 | 3.8215 | ±7.6430 | -0.480 | 0.6312 |  |
| Age (years) | +0.1322 | 0.1500 | ±0.2999 | +0.882 | 0.3780 |  |
| **BMI (kg/m2)** | **-0.9272** | 0.2319 | ±0.4638 | **-3.998** | **6.39e-05** | *** |
| **Hypertension** | **-14.1514** | 3.3781 | ±6.7563 | **-4.189** | **2.80e-05** | *** |
| High cholesterol | -0.8364 | 3.1432 | ±6.2864 | -0.266 | 0.7902 |  |
| Kidney disease | -5.5903 | 6.0722 | ±12.1443 | -0.921 | 0.3572 |  |
| **Circulatory disease** | **+10.9711** | 4.7027 | ±9.4054 | **+2.333** | **0.0197** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1893**, R² = **0.0444**, Adj R² = **0.0388**, F-statistic = **7.94** (p = **1.19e-13**), Residual SE = **66.617** on **1881** df, AIC = **21281.3**, BIC = **21347.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+418.6476** | 14.2592 | ±28.5185 | **+29.360** | **1.79e-189** | *** |
| Education: graduate level (vs college) | +1.6999 | 3.3412 | ±6.6824 | +0.509 | 0.6109 |  |
| **Education: high school or below (vs college)** | **-13.5787** | 5.3676 | ±10.7352 | **-2.530** | **0.0114** | * |
| **Site: UCSD (vs UAB)** | **-11.4793** | 4.0629 | ±8.1257 | **-2.825** | **0.0047** | ** |
| Site: UW (vs UAB) | -2.4417 | 3.8202 | ±7.6404 | -0.639 | 0.5227 |  |
| Age (years) | +0.1615 | 0.1497 | ±0.2993 | +1.079 | 0.2805 |  |
| **BMI (kg/m2)** | **-0.8322** | 0.2330 | ±0.4660 | **-3.572** | **3.55e-04** | *** |
| **Hypertension** | **-13.0072** | 3.3794 | ±6.7587 | **-3.849** | **1.19e-04** | *** |
| High cholesterol | +0.0828 | 3.1419 | ±6.2837 | +0.026 | 0.9790 |  |
| Kidney disease | -4.8286 | 6.0816 | ±12.1632 | -0.794 | 0.4272 |  |
| **Circulatory disease** | **+11.2062** | 4.6866 | ±9.3733 | **+2.391** | **0.0168** | * |
| **HbA1c (%)** | **-5.0930** | 1.3570 | ±2.7139 | **-3.753** | **1.75e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1893**, R² = **0.0403**, Adj R² = **0.0347**, F-statistic = **7.17** (p = **4.49e-12**), Residual SE = **66.761** on **1881** df, AIC = **21289.5**, BIC = **21356.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.5249** | 13.4300 | ±26.8601 | **+29.898** | **2.12e-196** | *** |
| Education: graduate level (vs college) | +2.1601 | 3.3356 | ±6.6713 | +0.648 | 0.5173 |  |
| **Education: high school or below (vs college)** | **-14.6718** | 5.3905 | ±10.7810 | **-2.722** | **0.0065** | ** |
| **Site: UCSD (vs UAB)** | **-11.3457** | 4.0668 | ±8.1337 | **-2.790** | **0.0053** | ** |
| Site: UW (vs UAB) | -1.9719 | 3.8235 | ±7.6470 | -0.516 | 0.6060 |  |
| Age (years) | +0.1447 | 0.1504 | ±0.3008 | +0.962 | 0.3360 |  |
| **BMI (kg/m2)** | **-0.8946** | 0.2330 | ±0.4659 | **-3.840** | **1.23e-04** | *** |
| **Hypertension** | **-13.6063** | 3.3799 | ±6.7598 | **-4.026** | **5.68e-05** | *** |
| High cholesterol | -0.5206 | 3.1507 | ±6.3013 | -0.165 | 0.8688 |  |
| Kidney disease | -4.6185 | 6.1564 | ±12.3128 | -0.750 | 0.4531 |  |
| **Circulatory disease** | **+11.1906** | 4.7057 | ±9.4114 | **+2.378** | **0.0174** | * |
| Mean glucose (mg/dL) | -0.0793 | 0.0478 | ±0.0956 | -1.658 | 0.0973 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1893**, R² = **0.0403**, Adj R² = **0.0347**, F-statistic = **7.17** (p = **4.49e-12**), Residual SE = **66.761** on **1881** df, AIC = **21289.5**, BIC = **21356.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.4958** | 16.8508 | ±33.7015 | **+24.479** | **2.45e-132** | *** |
| Education: graduate level (vs college) | +2.1601 | 3.3356 | ±6.6713 | +0.648 | 0.5173 |  |
| **Education: high school or below (vs college)** | **-14.6718** | 5.3905 | ±10.7810 | **-2.722** | **0.0065** | ** |
| **Site: UCSD (vs UAB)** | **-11.3457** | 4.0668 | ±8.1337 | **-2.790** | **0.0053** | ** |
| Site: UW (vs UAB) | -1.9719 | 3.8235 | ±7.6470 | -0.516 | 0.6060 |  |
| Age (years) | +0.1447 | 0.1504 | ±0.3008 | +0.962 | 0.3360 |  |
| **BMI (kg/m2)** | **-0.8946** | 0.2330 | ±0.4659 | **-3.840** | **1.23e-04** | *** |
| **Hypertension** | **-13.6063** | 3.3799 | ±6.7598 | **-4.026** | **5.68e-05** | *** |
| High cholesterol | -0.5206 | 3.1507 | ±6.3013 | -0.165 | 0.8688 |  |
| Kidney disease | -4.6185 | 6.1564 | ±12.3128 | -0.750 | 0.4531 |  |
| **Circulatory disease** | **+11.1906** | 4.7057 | ±9.4114 | **+2.378** | **0.0174** | * |
| GMI (%) | -3.3145 | 1.9988 | ±3.9977 | -1.658 | 0.0973 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1893**, R² = **0.0401**, Adj R² = **0.0344**, F-statistic = **7.13** (p = **5.41e-12**), Residual SE = **66.769** on **1881** df, AIC = **21289.9**, BIC = **21356.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.8651** | 13.4971 | ±26.9941 | **+29.700** | **7.64e-194** | *** |
| Education: graduate level (vs college) | +2.1540 | 3.3384 | ±6.6768 | +0.645 | 0.5188 |  |
| **Education: high school or below (vs college)** | **-14.7581** | 5.3853 | ±10.7707 | **-2.740** | **0.0061** | ** |
| **Site: UCSD (vs UAB)** | **-11.2575** | 4.0686 | ±8.1372 | **-2.767** | **0.0057** | ** |
| Site: UW (vs UAB) | -1.8864 | 3.8254 | ±7.6508 | -0.493 | 0.6219 |  |
| Age (years) | +0.1340 | 0.1501 | ±0.3002 | +0.893 | 0.3720 |  |
| **BMI (kg/m2)** | **-0.8811** | 0.2340 | ±0.4680 | **-3.765** | **1.67e-04** | *** |
| **Hypertension** | **-13.7466** | 3.3812 | ±6.7624 | **-4.066** | **4.79e-05** | *** |
| High cholesterol | -0.5342 | 3.1494 | ±6.2987 | -0.170 | 0.8653 |  |
| Kidney disease | -4.9837 | 6.1259 | ±12.2519 | -0.814 | 0.4159 |  |
| **Circulatory disease** | **+11.1405** | 4.7059 | ±9.4118 | **+2.367** | **0.0179** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0734 | 0.0487 | ±0.0974 | -1.508 | 0.1317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1893**, R² = **0.0419**, Adj R² = **0.0363**, F-statistic = **7.48** (p = **1.08e-12**), Residual SE = **66.705** on **1881** df, AIC = **21286.3**, BIC = **21352.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.8017** | 12.7949 | ±25.5898 | **+31.169** | **2.82e-213** | *** |
| Education: graduate level (vs college) | +1.9441 | 3.3382 | ±6.6765 | +0.582 | 0.5603 |  |
| **Education: high school or below (vs college)** | **-14.1638** | 5.4021 | ±10.8042 | **-2.622** | **0.0087** | ** |
| **Site: UCSD (vs UAB)** | **-11.7334** | 4.0606 | ±8.1212 | **-2.890** | **0.0039** | ** |
| Site: UW (vs UAB) | -2.4354 | 3.8292 | ±7.6584 | -0.636 | 0.5248 |  |
| Age (years) | +0.1632 | 0.1505 | ±0.3011 | +1.084 | 0.2782 |  |
| **BMI (kg/m2)** | **-0.8991** | 0.2322 | ±0.4644 | **-3.872** | **1.08e-04** | *** |
| **Hypertension** | **-13.2118** | 3.3863 | ±6.7726 | **-3.902** | **9.56e-05** | *** |
| High cholesterol | -0.4985 | 3.1413 | ±6.2826 | -0.159 | 0.8739 |  |
| Kidney disease | -3.2841 | 6.2669 | ±12.5338 | -0.524 | 0.6003 |  |
| **Circulatory disease** | **+11.2728** | 4.6916 | ±9.3831 | **+2.403** | **0.0163** | * |
| **Glucose SD, pooled (mg/dL)** | **-0.3338** | 0.1333 | ±0.2666 | **-2.504** | **0.0123** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1893**, R² = **0.0418**, Adj R² = **0.0362**, F-statistic = **7.46** (p = **1.20e-12**), Residual SE = **66.709** on **1881** df, AIC = **21286.5**, BIC = **21353.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.7345** | 12.7912 | ±25.5824 | **+31.173** | **2.51e-213** | *** |
| Education: graduate level (vs college) | +1.9912 | 3.3340 | ±6.6681 | +0.597 | 0.5503 |  |
| **Education: high school or below (vs college)** | **-14.1461** | 5.4110 | ±10.8221 | **-2.614** | **0.0089** | ** |
| **Site: UCSD (vs UAB)** | **-11.6805** | 4.0646 | ±8.1292 | **-2.874** | **0.0041** | ** |
| Site: UW (vs UAB) | -2.3449 | 3.8286 | ±7.6571 | -0.612 | 0.5402 |  |
| Age (years) | +0.1670 | 0.1507 | ±0.3014 | +1.108 | 0.2679 |  |
| **BMI (kg/m2)** | **-0.9064** | 0.2320 | ±0.4640 | **-3.907** | **9.36e-05** | *** |
| **Hypertension** | **-13.2429** | 3.3857 | ±6.7715 | **-3.911** | **9.18e-05** | *** |
| High cholesterol | -0.4837 | 3.1431 | ±6.2863 | -0.154 | 0.8777 |  |
| Kidney disease | -3.2621 | 6.2703 | ±12.5405 | -0.520 | 0.6029 |  |
| **Circulatory disease** | **+11.2384** | 4.6958 | ±9.3917 | **+2.393** | **0.0167** | * |
| **Avg. daily SD (mg/dL)** | **-0.3697** | 0.1496 | ±0.2993 | **-2.471** | **0.0135** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1893**, R² = **0.0407**, Adj R² = **0.0351**, F-statistic = **7.26** (p = **2.97e-12**), Residual SE = **66.745** on **1881** df, AIC = **21288.6**, BIC = **21355.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.6543** | 13.4521 | ±26.9042 | **+29.932** | **7.46e-197** | *** |
| Education: graduate level (vs college) | +2.0730 | 3.3374 | ±6.6748 | +0.621 | 0.5345 |  |
| **Education: high school or below (vs college)** | **-14.7898** | 5.3870 | ±10.7740 | **-2.745** | **0.0060** | ** |
| **Site: UCSD (vs UAB)** | **-11.6825** | 4.0760 | ±8.1520 | **-2.866** | **0.0042** | ** |
| Site: UW (vs UAB) | -2.3922 | 3.8341 | ±7.6683 | -0.624 | 0.5327 |  |
| Age (years) | +0.1591 | 0.1509 | ±0.3017 | +1.055 | 0.2915 |  |
| **BMI (kg/m2)** | **-0.9279** | 0.2319 | ±0.4638 | **-4.001** | **6.30e-05** | *** |
| **Hypertension** | **-13.5373** | 3.3821 | ±6.7641 | **-4.003** | **6.26e-05** | *** |
| High cholesterol | -0.7466 | 3.1399 | ±6.2797 | -0.238 | 0.8120 |  |
| Kidney disease | -3.9125 | 6.2240 | ±12.4480 | -0.629 | 0.5296 |  |
| **Circulatory disease** | **+11.1213** | 4.6943 | ±9.3885 | **+2.369** | **0.0178** | * |
| CV (%) | -0.5779 | 0.2953 | ±0.5907 | -1.957 | 0.0504 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1893**, R² = **0.0404**, Adj R² = **0.0348**, F-statistic = **7.20** (p = **3.97e-12**), Residual SE = **66.756** on **1881** df, AIC = **21289.2**, BIC = **21355.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.2901** | 14.8948 | ±29.7896 | **+25.532** | **8.77e-144** | *** |
| Education: graduate level (vs college) | +2.1121 | 3.3382 | ±6.6764 | +0.633 | 0.5269 |  |
| **Education: high school or below (vs college)** | **-14.8578** | 5.3864 | ±10.7728 | **-2.758** | **0.0058** | ** |
| **Site: UCSD (vs UAB)** | **-11.5887** | 4.0739 | ±8.1478 | **-2.845** | **0.0044** | ** |
| Site: UW (vs UAB) | -2.2103 | 3.8318 | ±7.6636 | -0.577 | 0.5640 |  |
| Age (years) | +0.1568 | 0.1514 | ±0.3028 | +1.035 | 0.3005 |  |
| **BMI (kg/m2)** | **-0.9280** | 0.2319 | ±0.4638 | **-4.002** | **6.28e-05** | *** |
| **Hypertension** | **-13.5845** | 3.3824 | ±6.7648 | **-4.016** | **5.91e-05** | *** |
| High cholesterol | -0.7065 | 3.1417 | ±6.2834 | -0.225 | 0.8221 |  |
| Kidney disease | -4.3798 | 6.1574 | ±12.3148 | -0.711 | 0.4769 |  |
| **Circulatory disease** | **+11.1497** | 4.6946 | ±9.3892 | **+2.375** | **0.0175** | * |
| Mean / SD ratio | +2.0433 | 1.1730 | ±2.3459 | +1.742 | 0.0815 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1893**, R² = **0.0412**, Adj R² = **0.0356**, F-statistic = **7.35** (p = **1.96e-12**), Residual SE = **66.728** on **1881** df, AIC = **21287.6**, BIC = **21354.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+377.3430** | 14.8166 | ±29.6332 | **+25.468** | **4.51e-143** | *** |
| Education: graduate level (vs college) | +2.1266 | 3.3326 | ±6.6651 | +0.638 | 0.5234 |  |
| **Education: high school or below (vs college)** | **-14.6822** | 5.3824 | ±10.7648 | **-2.728** | **0.0064** | ** |
| **Site: UCSD (vs UAB)** | **-11.5270** | 4.0777 | ±8.1555 | **-2.827** | **0.0047** | ** |
| Site: UW (vs UAB) | -2.1791 | 3.8275 | ±7.6550 | -0.569 | 0.5691 |  |
| Age (years) | +0.1682 | 0.1515 | ±0.3031 | +1.110 | 0.2669 |  |
| **BMI (kg/m2)** | **-0.9296** | 0.2318 | ±0.4635 | **-4.011** | **6.05e-05** | *** |
| **Hypertension** | **-13.5479** | 3.3795 | ±6.7590 | **-4.009** | **6.10e-05** | *** |
| High cholesterol | -0.6803 | 3.1408 | ±6.2816 | -0.217 | 0.8285 |  |
| Kidney disease | -4.1604 | 6.1535 | ±12.3070 | -0.676 | 0.4990 |  |
| **Circulatory disease** | **+11.0930** | 4.6994 | ±9.3989 | **+2.361** | **0.0183** | * |
| **Avg. daily mean/SD** | **+2.1229** | 0.9720 | ±1.9441 | **+2.184** | **0.0290** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1893**, R² = **0.0556**, Adj R² = **0.0501**, F-statistic = **10.07** (p = **4.78e-18**), Residual SE = **66.225** on **1881** df, AIC = **21259.0**, BIC = **21325.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+433.5949** | 14.1595 | ±28.3189 | **+30.622** | **6.19e-206** | *** |
| Education: graduate level (vs college) | +1.4497 | 3.3134 | ±6.6268 | +0.438 | 0.6617 |  |
| **Education: high school or below (vs college)** | **-13.3023** | 5.2883 | ±10.5766 | **-2.515** | **0.0119** | * |
| **Site: UCSD (vs UAB)** | **-12.5386** | 4.0592 | ±8.1184 | **-3.089** | **0.0020** | ** |
| Site: UW (vs UAB) | -3.9906 | 3.8040 | ±7.6079 | -1.049 | 0.2942 |  |
| Age (years) | +0.1229 | 0.1487 | ±0.2973 | +0.827 | 0.4082 |  |
| **BMI (kg/m2)** | **-0.8968** | 0.2291 | ±0.4583 | **-3.914** | **9.09e-05** | *** |
| **Hypertension** | **-13.6474** | 3.3480 | ±6.6960 | **-4.076** | **4.58e-05** | *** |
| High cholesterol | -0.7729 | 3.1221 | ±6.2441 | -0.248 | 0.8045 |  |
| Kidney disease | -2.7430 | 6.1339 | ±12.2677 | -0.447 | 0.6547 |  |
| **Circulatory disease** | **+10.8544** | 4.6617 | ±9.3233 | **+2.328** | **0.0199** | * |
| **MAG (mg/dL/h)** | **-1.0019** | 0.1770 | ±0.3539 | **-5.662** | **1.50e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1893**, R² = **0.0417**, Adj R² = **0.0361**, F-statistic = **7.43** (p = **1.33e-12**), Residual SE = **66.713** on **1881** df, AIC = **21286.8**, BIC = **21353.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.0280** | 13.1179 | ±26.2358 | **+30.647** | **2.88e-206** | *** |
| Education: graduate level (vs college) | +2.0442 | 3.3349 | ±6.6698 | +0.613 | 0.5399 |  |
| **Education: high school or below (vs college)** | **-14.1807** | 5.4073 | ±10.8147 | **-2.622** | **0.0087** | ** |
| **Site: UCSD (vs UAB)** | **-11.7110** | 4.0693 | ±8.1385 | **-2.878** | **0.0040** | ** |
| Site: UW (vs UAB) | -2.3664 | 3.8292 | ±7.6584 | -0.618 | 0.5366 |  |
| Age (years) | +0.1620 | 0.1506 | ±0.3012 | +1.076 | 0.2822 |  |
| **BMI (kg/m2)** | **-0.9264** | 0.2319 | ±0.4639 | **-3.994** | **6.49e-05** | *** |
| **Hypertension** | **-13.4160** | 3.3813 | ±6.7627 | **-3.968** | **7.26e-05** | *** |
| High cholesterol | -0.5313 | 3.1441 | ±6.2882 | -0.169 | 0.8658 |  |
| Kidney disease | -3.4408 | 6.2433 | ±12.4865 | -0.551 | 0.5815 |  |
| **Circulatory disease** | **+11.2293** | 4.6984 | ±9.3968 | **+2.390** | **0.0168** | * |
| **Avg. daily range (mg/dL)** | **-0.0980** | 0.0407 | ±0.0814 | **-2.409** | **0.0160** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1893**, R² = **0.0414**, Adj R² = **0.0358**, F-statistic = **7.39** (p = **1.63e-12**), Residual SE = **66.721** on **1881** df, AIC = **21287.2**, BIC = **21353.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.2359** | 12.7094 | ±25.4189 | **+31.177** | **2.22e-213** | *** |
| Education: graduate level (vs college) | +1.9421 | 3.3502 | ±6.7003 | +0.580 | 0.5621 |  |
| **Education: high school or below (vs college)** | **-14.7357** | 5.3482 | ±10.6964 | **-2.755** | **0.0059** | ** |
| **Site: UCSD (vs UAB)** | **-11.5845** | 4.0591 | ±8.1182 | **-2.854** | **0.0043** | ** |
| Site: UW (vs UAB) | -2.3706 | 3.8288 | ±7.6576 | -0.619 | 0.5358 |  |
| Age (years) | +0.1351 | 0.1500 | ±0.3000 | +0.901 | 0.3676 |  |
| **BMI (kg/m2)** | **-0.8800** | 0.2320 | ±0.4639 | **-3.794** | **1.48e-04** | *** |
| **Hypertension** | **-13.5139** | 3.3840 | ±6.7679 | **-3.994** | **6.51e-05** | *** |
| High cholesterol | -0.5648 | 3.1396 | ±6.2792 | -0.180 | 0.8572 |  |
| Kidney disease | -4.4139 | 6.1846 | ±12.3691 | -0.714 | 0.4754 |  |
| **Circulatory disease** | **+11.4497** | 4.6835 | ±9.3671 | **+2.445** | **0.0145** | * |
| **SD of daily means (mg/dL)** | **-0.5678** | 0.2532 | ±0.5063 | **-2.243** | **0.0249** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1893**, R² = **0.0396**, Adj R² = **0.0340**, F-statistic = **7.05** (p = **8.00e-12**), Residual SE = **66.784** on **1881** df, AIC = **21290.8**, BIC = **21357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+383.1612** | 15.4444 | ±30.8888 | **+24.809** | **7.15e-136** | *** |
| Education: graduate level (vs college) | +2.1635 | 3.3411 | ±6.6822 | +0.648 | 0.5173 |  |
| **Education: high school or below (vs college)** | **-14.9060** | 5.3928 | ±10.7856 | **-2.764** | **0.0057** | ** |
| **Site: UCSD (vs UAB)** | **-11.4262** | 4.0713 | ±8.1426 | **-2.807** | **0.0050** | ** |
| Site: UW (vs UAB) | -2.0774 | 3.8283 | ±7.6566 | -0.543 | 0.5874 |  |
| Age (years) | +0.1419 | 0.1505 | ±0.3010 | +0.943 | 0.3457 |  |
| **BMI (kg/m2)** | **-0.9044** | 0.2331 | ±0.4661 | **-3.881** | **1.04e-04** | *** |
| **Hypertension** | **-13.8537** | 3.3778 | ±6.7555 | **-4.101** | **4.11e-05** | *** |
| High cholesterol | -0.6934 | 3.1447 | ±6.2895 | -0.221 | 0.8255 |  |
| Kidney disease | -4.8238 | 6.1684 | ±12.3369 | -0.782 | 0.4342 |  |
| **Circulatory disease** | **+11.1629** | 4.7017 | ±9.4034 | **+2.374** | **0.0176** | * |
| Time in range 70-180, pooled (%) | +0.0973 | 0.0818 | ±0.1636 | +1.189 | 0.2344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1893**, R² = **0.0396**, Adj R² = **0.0340**, F-statistic = **7.05** (p = **8.23e-12**), Residual SE = **66.785** on **1881** df, AIC = **21290.9**, BIC = **21357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+383.3653** | 15.4837 | ±30.9674 | **+24.759** | **2.47e-135** | *** |
| Education: graduate level (vs college) | +2.1747 | 3.3411 | ±6.6822 | +0.651 | 0.5151 |  |
| **Education: high school or below (vs college)** | **-14.9108** | 5.3939 | ±10.7878 | **-2.764** | **0.0057** | ** |
| **Site: UCSD (vs UAB)** | **-11.4259** | 4.0728 | ±8.1456 | **-2.805** | **0.0050** | ** |
| Site: UW (vs UAB) | -2.0724 | 3.8286 | ±7.6572 | -0.541 | 0.5883 |  |
| Age (years) | +0.1422 | 0.1506 | ±0.3011 | +0.945 | 0.3449 |  |
| **BMI (kg/m2)** | **-0.9046** | 0.2331 | ±0.4662 | **-3.881** | **1.04e-04** | *** |
| **Hypertension** | **-13.8675** | 3.3775 | ±6.7551 | **-4.106** | **4.03e-05** | *** |
| High cholesterol | -0.6919 | 3.1451 | ±6.2902 | -0.220 | 0.8259 |  |
| Kidney disease | -4.8284 | 6.1755 | ±12.3511 | -0.782 | 0.4343 |  |
| **Circulatory disease** | **+11.1571** | 4.7018 | ±9.4035 | **+2.373** | **0.0176** | * |
| Avg. daily time in range 70-180 (%) | +0.0946 | 0.0817 | ±0.1634 | +1.158 | 0.2470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1893**, R² = **0.0393**, Adj R² = **0.0337**, F-statistic = **7.00** (p = **1.01e-11**), Residual SE = **66.794** on **1881** df, AIC = **21291.4**, BIC = **21357.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+391.3944** | 12.9434 | ±25.8869 | **+30.239** | **7.31e-201** | *** |
| Education: graduate level (vs college) | +2.4132 | 3.3377 | ±6.6754 | +0.723 | 0.4697 |  |
| **Education: high school or below (vs college)** | **-15.2652** | 5.3796 | ±10.7592 | **-2.838** | **0.0045** | ** |
| **Site: UCSD (vs UAB)** | **-10.7154** | 4.1100 | ±8.2200 | **-2.607** | **0.0091** | ** |
| Site: UW (vs UAB) | -1.6208 | 3.8294 | ±7.6587 | -0.423 | 0.6721 |  |
| Age (years) | +0.1426 | 0.1505 | ±0.3010 | +0.948 | 0.3433 |  |
| **BMI (kg/m2)** | **-0.9334** | 0.2315 | ±0.4630 | **-4.032** | **5.53e-05** | *** |
| **Hypertension** | **-14.1696** | 3.3787 | ±6.7573 | **-4.194** | **2.74e-05** | *** |
| High cholesterol | -0.6352 | 3.1632 | ±6.3264 | -0.201 | 0.8408 |  |
| Kidney disease | -5.4761 | 6.0678 | ±12.1357 | -0.902 | 0.3668 |  |
| **Circulatory disease** | **+10.7053** | 4.7130 | ±9.4260 | **+2.271** | **0.0231** | * |
| Any reading < 54 during wear (0/1) | +3.1872 | 3.3588 | ±6.7176 | +0.949 | 0.3427 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1893**, R² = **0.0389**, Adj R² = **0.0333**, F-statistic = **6.92** (p = **1.49e-11**), Residual SE = **66.809** on **1881** df, AIC = **21292.2**, BIC = **21358.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.9643** | 12.7083 | ±25.4166 | **+30.922** | **6.08e-210** | *** |
| Education: graduate level (vs college) | +2.3775 | 3.3360 | ±6.6720 | +0.713 | 0.4760 |  |
| **Education: high school or below (vs college)** | **-15.5035** | 5.3581 | ±10.7163 | **-2.893** | **0.0038** | ** |
| **Site: UCSD (vs UAB)** | **-11.0434** | 4.1130 | ±8.2261 | **-2.685** | **0.0073** | ** |
| Site: UW (vs UAB) | -1.7780 | 3.8455 | ±7.6909 | -0.462 | 0.6438 |  |
| Age (years) | +0.1328 | 0.1499 | ±0.2999 | +0.886 | 0.3757 |  |
| **BMI (kg/m2)** | **-0.9271** | 0.2321 | ±0.4642 | **-3.994** | **6.50e-05** | *** |
| **Hypertension** | **-14.1411** | 3.3802 | ±6.7604 | **-4.183** | **2.87e-05** | *** |
| High cholesterol | -0.8089 | 3.1527 | ±6.3054 | -0.257 | 0.7975 |  |
| Kidney disease | -5.5885 | 6.0733 | ±12.1466 | -0.920 | 0.3575 |  |
| **Circulatory disease** | **+10.9523** | 4.7039 | ±9.4077 | **+2.328** | **0.0199** | * |
| Time < 54 (%) | +0.4300 | 2.6481 | ±5.2961 | +0.162 | 0.8710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1893**, R² = **0.0389**, Adj R² = **0.0333**, F-statistic = **6.92** (p = **1.50e-11**), Residual SE = **66.810** on **1881** df, AIC = **21292.2**, BIC = **21358.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.1077** | 12.6848 | ±25.3695 | **+30.991** | **7.23e-211** | *** |
| Education: graduate level (vs college) | +2.3714 | 3.3383 | ±6.6765 | +0.710 | 0.4775 |  |
| **Education: high school or below (vs college)** | **-15.5337** | 5.3571 | ±10.7141 | **-2.900** | **0.0037** | ** |
| **Site: UCSD (vs UAB)** | **-11.1009** | 4.1035 | ±8.2071 | **-2.705** | **0.0068** | ** |
| Site: UW (vs UAB) | -1.8239 | 3.8431 | ±7.6861 | -0.475 | 0.6351 |  |
| Age (years) | +0.1322 | 0.1500 | ±0.3000 | +0.881 | 0.3781 |  |
| **BMI (kg/m2)** | **-0.9272** | 0.2320 | ±0.4641 | **-3.996** | **6.45e-05** | *** |
| **Hypertension** | **-14.1494** | 3.3809 | ±6.7618 | **-4.185** | **2.85e-05** | *** |
| High cholesterol | -0.8317 | 3.1520 | ±6.3040 | -0.264 | 0.7919 |  |
| Kidney disease | -5.5903 | 6.0730 | ±12.1461 | -0.921 | 0.3573 |  |
| **Circulatory disease** | **+10.9678** | 4.7028 | ±9.4055 | **+2.332** | **0.0197** | * |
| Avg. daily time < 54 (%) | +0.0939 | 2.7318 | ±5.4636 | +0.034 | 0.9726 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1893**, R² = **0.0393**, Adj R² = **0.0337**, F-statistic = **7.00** (p = **1.02e-11**), Residual SE = **66.794** on **1881** df, AIC = **21291.4**, BIC = **21357.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.1375** | 12.7239 | ±25.4478 | **+30.819** | **1.46e-208** | *** |
| Education: graduate level (vs college) | +2.4975 | 3.3404 | ±6.6809 | +0.748 | 0.4547 |  |
| **Education: high school or below (vs college)** | **-15.3918** | 5.3592 | ±10.7184 | **-2.872** | **0.0041** | ** |
| **Site: UCSD (vs UAB)** | **-10.7967** | 4.0929 | ±8.1859 | **-2.638** | **0.0083** | ** |
| Site: UW (vs UAB) | -1.5395 | 3.8381 | ±7.6763 | -0.401 | 0.6884 |  |
| Age (years) | +0.1342 | 0.1500 | ±0.3001 | +0.894 | 0.3712 |  |
| **BMI (kg/m2)** | **-0.9296** | 0.2319 | ±0.4638 | **-4.008** | **6.12e-05** | *** |
| **Hypertension** | **-14.0604** | 3.3844 | ±6.7688 | **-4.154** | **3.26e-05** | *** |
| High cholesterol | -0.7002 | 3.1533 | ±6.3067 | -0.222 | 0.8243 |  |
| Kidney disease | -5.5586 | 6.0727 | ±12.1453 | -0.915 | 0.3600 |  |
| **Circulatory disease** | **+10.9039** | 4.7060 | ±9.4119 | **+2.317** | **0.0205** | * |
| Time 54-69, pooled (%) | +0.9811 | 0.9567 | ±1.9134 | +1.025 | 0.3051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1893**, R² = **0.0392**, Adj R² = **0.0336**, F-statistic = **6.97** (p = **1.15e-11**), Residual SE = **66.799** on **1881** df, AIC = **21291.6**, BIC = **21358.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.4853** | 12.6984 | ±25.3968 | **+30.908** | **9.27e-210** | *** |
| Education: graduate level (vs college) | +2.4850 | 3.3422 | ±6.6844 | +0.744 | 0.4572 |  |
| **Education: high school or below (vs college)** | **-15.4243** | 5.3579 | ±10.7158 | **-2.879** | **0.0040** | ** |
| **Site: UCSD (vs UAB)** | **-10.8909** | 4.0905 | ±8.1809 | **-2.663** | **0.0078** | ** |
| Site: UW (vs UAB) | -1.5919 | 3.8357 | ±7.6715 | -0.415 | 0.6781 |  |
| Age (years) | +0.1320 | 0.1500 | ±0.3000 | +0.880 | 0.3790 |  |
| **BMI (kg/m2)** | **-0.9292** | 0.2321 | ±0.4641 | **-4.004** | **6.22e-05** | *** |
| **Hypertension** | **-14.0770** | 3.3848 | ±6.7696 | **-4.159** | **3.20e-05** | *** |
| High cholesterol | -0.7360 | 3.1526 | ±6.3052 | -0.233 | 0.8154 |  |
| Kidney disease | -5.5619 | 6.0724 | ±12.1448 | -0.916 | 0.3597 |  |
| **Circulatory disease** | **+10.9218** | 4.7068 | ±9.4135 | **+2.320** | **0.0203** | * |
| Avg. daily time 54-69 (%) | +0.8015 | 0.9291 | ±1.8582 | +0.863 | 0.3883 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1893**, R² = **0.0392**, Adj R² = **0.0336**, F-statistic = **6.98** (p = **1.14e-11**), Residual SE = **66.798** on **1881** df, AIC = **21291.6**, BIC = **21358.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.1981** | 12.7300 | ±25.4601 | **+30.809** | **1.99e-208** | *** |
| Education: graduate level (vs college) | +2.4703 | 3.3403 | ±6.6806 | +0.740 | 0.4596 |  |
| **Education: high school or below (vs college)** | **-15.3823** | 5.3591 | ±10.7182 | **-2.870** | **0.0041** | ** |
| **Site: UCSD (vs UAB)** | **-10.7907** | 4.1001 | ±8.2002 | **-2.632** | **0.0085** | ** |
| Site: UW (vs UAB) | -1.5451 | 3.8428 | ±7.6855 | -0.402 | 0.6876 |  |
| Age (years) | +0.1345 | 0.1500 | ±0.3001 | +0.897 | 0.3700 |  |
| **BMI (kg/m2)** | **-0.9286** | 0.2319 | ±0.4639 | **-4.004** | **6.23e-05** | *** |
| **Hypertension** | **-14.0732** | 3.3838 | ±6.7675 | **-4.159** | **3.20e-05** | *** |
| High cholesterol | -0.7005 | 3.1549 | ±6.3098 | -0.222 | 0.8243 |  |
| Kidney disease | -5.5659 | 6.0729 | ±12.1458 | -0.917 | 0.3594 |  |
| **Circulatory disease** | **+10.8958** | 4.7047 | ±9.4094 | **+2.316** | **0.0206** | * |
| Time < 70 (%) | +0.6698 | 0.7371 | ±1.4743 | +0.909 | 0.3636 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1893**, R² = **0.0391**, Adj R² = **0.0335**, F-statistic = **6.96** (p = **1.25e-11**), Residual SE = **66.802** on **1881** df, AIC = **21291.8**, BIC = **21358.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.5676** | 12.6997 | ±25.3994 | **+30.912** | **8.35e-210** | *** |
| Education: graduate level (vs college) | +2.4656 | 3.3425 | ±6.6851 | +0.738 | 0.4607 |  |
| **Education: high school or below (vs college)** | **-15.4234** | 5.3575 | ±10.7151 | **-2.879** | **0.0040** | ** |
| **Site: UCSD (vs UAB)** | **-10.8965** | 4.0946 | ±8.1893 | **-2.661** | **0.0078** | ** |
| Site: UW (vs UAB) | -1.6036 | 3.8391 | ±7.6782 | -0.418 | 0.6762 |  |
| Age (years) | +0.1320 | 0.1500 | ±0.3000 | +0.880 | 0.3789 |  |
| **BMI (kg/m2)** | **-0.9285** | 0.2321 | ±0.4641 | **-4.001** | **6.30e-05** | *** |
| **Hypertension** | **-14.0880** | 3.3844 | ±6.7688 | **-4.163** | **3.15e-05** | *** |
| High cholesterol | -0.7386 | 3.1538 | ±6.3076 | -0.234 | 0.8148 |  |
| Kidney disease | -5.5710 | 6.0725 | ±12.1450 | -0.917 | 0.3589 |  |
| **Circulatory disease** | **+10.9175** | 4.7053 | ±9.4106 | **+2.320** | **0.0203** | * |
| Avg. daily time < 70 (%) | +0.5559 | 0.7302 | ±1.4604 | +0.761 | 0.4465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1893**, R² = **0.0391**, Adj R² = **0.0335**, F-statistic = **6.96** (p = **1.24e-11**), Residual SE = **66.802** on **1881** df, AIC = **21291.8**, BIC = **21358.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+383.4590** | 19.2461 | ±38.4922 | **+19.924** | **2.52e-88** | *** |
| Education: graduate level (vs college) | +2.2241 | 3.3540 | ±6.7080 | +0.663 | 0.5073 |  |
| **Education: high school or below (vs college)** | **-15.2698** | 5.3553 | ±10.7105 | **-2.851** | **0.0044** | ** |
| **Site: UCSD (vs UAB)** | **-11.2415** | 4.0780 | ±8.1560 | **-2.757** | **0.0058** | ** |
| Site: UW (vs UAB) | -1.9934 | 3.8181 | ±7.6362 | -0.522 | 0.6016 |  |
| Age (years) | +0.1306 | 0.1499 | ±0.2999 | +0.871 | 0.3836 |  |
| **BMI (kg/m2)** | **-0.9194** | 0.2327 | ±0.4653 | **-3.952** | **7.76e-05** | *** |
| **Hypertension** | **-14.0545** | 3.3778 | ±6.7555 | **-4.161** | **3.17e-05** | *** |
| High cholesterol | -0.8182 | 3.1445 | ±6.2890 | -0.260 | 0.7947 |  |
| Kidney disease | -5.3208 | 6.1225 | ±12.2451 | -0.869 | 0.3848 |  |
| **Circulatory disease** | **+11.0628** | 4.7070 | ±9.4141 | **+2.350** | **0.0188** | * |
| Time 54-250, pooled (%) | +0.0985 | 0.1422 | ±0.2843 | +0.693 | 0.4884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1893**, R² = **0.0391**, Adj R² = **0.0334**, F-statistic = **6.95** (p = **1.27e-11**), Residual SE = **66.803** on **1881** df, AIC = **21291.9**, BIC = **21358.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+384.0074** | 19.5616 | ±39.1232 | **+19.631** | **8.46e-86** | *** |
| Education: graduate level (vs college) | +2.2366 | 3.3541 | ±6.7082 | +0.667 | 0.5049 |  |
| **Education: high school or below (vs college)** | **-15.2911** | 5.3550 | ±10.7100 | **-2.855** | **0.0043** | ** |
| **Site: UCSD (vs UAB)** | **-11.2294** | 4.0786 | ±8.1571 | **-2.753** | **0.0059** | ** |
| Site: UW (vs UAB) | -1.9752 | 3.8175 | ±7.6350 | -0.517 | 0.6049 |  |
| Age (years) | +0.1313 | 0.1500 | ±0.3000 | +0.876 | 0.3812 |  |
| **BMI (kg/m2)** | **-0.9198** | 0.2327 | ±0.4654 | **-3.953** | **7.71e-05** | *** |
| **Hypertension** | **-14.0671** | 3.3775 | ±6.7550 | **-4.165** | **3.11e-05** | *** |
| High cholesterol | -0.8196 | 3.1447 | ±6.2893 | -0.261 | 0.7944 |  |
| Kidney disease | -5.3280 | 6.1288 | ±12.2576 | -0.869 | 0.3847 |  |
| **Circulatory disease** | **+11.0608** | 4.7076 | ±9.4151 | **+2.350** | **0.0188** | * |
| Avg. daily time 54-250 (%) | +0.0924 | 0.1456 | ±0.2911 | +0.634 | 0.5258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1893**, R² = **0.0399**, Adj R² = **0.0343**, F-statistic = **7.10** (p = **6.33e-12**), Residual SE = **66.775** on **1881** df, AIC = **21290.3**, BIC = **21356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.1973** | 12.6896 | ±25.3792 | **+30.907** | **9.62e-210** | *** |
| Education: graduate level (vs college) | +2.2790 | 3.3343 | ±6.6686 | +0.684 | 0.4943 |  |
| **Education: high school or below (vs college)** | **-14.8500** | 5.4107 | ±10.8214 | **-2.745** | **0.0061** | ** |
| **Site: UCSD (vs UAB)** | **-11.3917** | 4.0712 | ±8.1425 | **-2.798** | **0.0051** | ** |
| Site: UW (vs UAB) | -1.9370 | 3.8308 | ±7.6616 | -0.506 | 0.6131 |  |
| Age (years) | +0.1529 | 0.1512 | ±0.3023 | +1.011 | 0.3118 |  |
| **BMI (kg/m2)** | **-0.9002** | 0.2327 | ±0.4653 | **-3.869** | **1.09e-04** | *** |
| **Hypertension** | **-13.7701** | 3.3806 | ±6.7611 | **-4.073** | **4.63e-05** | *** |
| High cholesterol | -0.5862 | 3.1480 | ±6.2960 | -0.186 | 0.8523 |  |
| Kidney disease | -4.6805 | 6.1616 | ±12.3232 | -0.760 | 0.4475 |  |
| **Circulatory disease** | **+11.1420** | 4.7015 | ±9.4029 | **+2.370** | **0.0178** | * |
| Time 181-250, pooled (%) | -0.1758 | 0.1328 | ±0.2657 | -1.323 | 0.1857 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1893**, R² = **0.0398**, Adj R² = **0.0342**, F-statistic = **7.10** (p = **6.48e-12**), Residual SE = **66.776** on **1881** df, AIC = **21290.3**, BIC = **21356.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.2297** | 12.6905 | ±25.3811 | **+30.907** | **9.55e-210** | *** |
| Education: graduate level (vs college) | +2.2874 | 3.3346 | ±6.6692 | +0.686 | 0.4927 |  |
| **Education: high school or below (vs college)** | **-14.8384** | 5.4123 | ±10.8246 | **-2.742** | **0.0061** | ** |
| **Site: UCSD (vs UAB)** | **-11.4145** | 4.0725 | ±8.1451 | **-2.803** | **0.0051** | ** |
| Site: UW (vs UAB) | -1.9522 | 3.8318 | ±7.6636 | -0.509 | 0.6104 |  |
| Age (years) | +0.1519 | 0.1512 | ±0.3023 | +1.005 | 0.3150 |  |
| **BMI (kg/m2)** | **-0.9004** | 0.2327 | ±0.4654 | **-3.869** | **1.09e-04** | *** |
| **Hypertension** | **-13.7782** | 3.3810 | ±6.7621 | **-4.075** | **4.60e-05** | *** |
| High cholesterol | -0.5848 | 3.1483 | ±6.2966 | -0.186 | 0.8526 |  |
| Kidney disease | -4.6923 | 6.1659 | ±12.3318 | -0.761 | 0.4466 |  |
| **Circulatory disease** | **+11.1308** | 4.7024 | ±9.4047 | **+2.367** | **0.0179** | * |
| Avg. daily time 181-250 (%) | -0.1711 | 0.1311 | ±0.2622 | -1.305 | 0.1920 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1893**, R² = **0.0397**, Adj R² = **0.0341**, F-statistic = **7.07** (p = **7.45e-12**), Residual SE = **66.781** on **1881** df, AIC = **21290.7**, BIC = **21357.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.7376** | 12.6759 | ±25.3518 | **+30.983** | **9.13e-211** | *** |
| Education: graduate level (vs college) | +2.1696 | 3.3398 | ±6.6796 | +0.650 | 0.5159 |  |
| **Education: high school or below (vs college)** | **-14.8535** | 5.3945 | ±10.7889 | **-2.753** | **0.0059** | ** |
| **Site: UCSD (vs UAB)** | **-11.3918** | 4.0705 | ±8.1410 | **-2.799** | **0.0051** | ** |
| Site: UW (vs UAB) | -2.0445 | 3.8272 | ±7.6543 | -0.534 | 0.5932 |  |
| Age (years) | +0.1427 | 0.1505 | ±0.3010 | +0.948 | 0.3431 |  |
| **BMI (kg/m2)** | **-0.9036** | 0.2330 | ±0.4660 | **-3.878** | **1.05e-04** | *** |
| **Hypertension** | **-13.8284** | 3.3788 | ±6.7576 | **-4.093** | **4.26e-05** | *** |
| High cholesterol | -0.6663 | 3.1458 | ±6.2915 | -0.212 | 0.8322 |  |
| Kidney disease | -4.7854 | 6.1678 | ±12.3356 | -0.776 | 0.4378 |  |
| **Circulatory disease** | **+11.1601** | 4.7017 | ±9.4034 | **+2.374** | **0.0176** | * |
| Time > 180 (%) | -0.1017 | 0.0812 | ±0.1625 | -1.252 | 0.2107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1893**, R² = **0.0396**, Adj R² = **0.0340**, F-statistic = **7.06** (p = **7.78e-12**), Residual SE = **66.783** on **1881** df, AIC = **21290.8**, BIC = **21357.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.7151** | 12.6793 | ±25.3587 | **+30.973** | **1.25e-210** | *** |
| Education: graduate level (vs college) | +2.1844 | 3.3396 | ±6.6792 | +0.654 | 0.5131 |  |
| **Education: high school or below (vs college)** | **-14.8663** | 5.3954 | ±10.7907 | **-2.755** | **0.0059** | ** |
| **Site: UCSD (vs UAB)** | **-11.3999** | 4.0718 | ±8.1437 | **-2.800** | **0.0051** | ** |
| Site: UW (vs UAB) | -2.0407 | 3.8276 | ±7.6551 | -0.533 | 0.5939 |  |
| Age (years) | +0.1426 | 0.1506 | ±0.3011 | +0.947 | 0.3437 |  |
| **BMI (kg/m2)** | **-0.9040** | 0.2330 | ±0.4661 | **-3.879** | **1.05e-04** | *** |
| **Hypertension** | **-13.8454** | 3.3788 | ±6.7576 | **-4.098** | **4.17e-05** | *** |
| High cholesterol | -0.6691 | 3.1461 | ±6.2922 | -0.213 | 0.8316 |  |
| Kidney disease | -4.7959 | 6.1752 | ±12.3504 | -0.777 | 0.4374 |  |
| **Circulatory disease** | **+11.1547** | 4.7019 | ±9.4038 | **+2.372** | **0.0177** | * |
| Avg. daily time > 180 (%) | -0.0982 | 0.0814 | ±0.1627 | -1.207 | 0.2273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1893**, R² = **0.0390**, Adj R² = **0.0333**, F-statistic = **6.93** (p = **1.39e-11**), Residual SE = **66.806** on **1881** df, AIC = **21292.1**, BIC = **21358.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.9833** | 12.6815 | ±25.3631 | **+30.989** | **7.67e-211** | *** |
| Education: graduate level (vs college) | +2.2838 | 3.3462 | ±6.6924 | +0.683 | 0.4949 |  |
| **Education: high school or below (vs college)** | **-15.3282** | 5.3872 | ±10.7745 | **-2.845** | **0.0044** | ** |
| **Site: UCSD (vs UAB)** | **-11.2141** | 4.0802 | ±8.1604 | **-2.748** | **0.0060** | ** |
| Site: UW (vs UAB) | -1.8994 | 3.8281 | ±7.6562 | -0.496 | 0.6198 |  |
| Age (years) | +0.1333 | 0.1502 | ±0.3003 | +0.888 | 0.3745 |  |
| **BMI (kg/m2)** | **-0.9158** | 0.2343 | ±0.4685 | **-3.909** | **9.25e-05** | *** |
| **Hypertension** | **-14.0779** | 3.3796 | ±6.7592 | **-4.166** | **3.11e-05** | *** |
| High cholesterol | -0.7966 | 3.1447 | ±6.2895 | -0.253 | 0.8000 |  |
| Kidney disease | -5.3901 | 6.1344 | ±12.2687 | -0.879 | 0.3796 |  |
| **Circulatory disease** | **+11.0318** | 4.7028 | ±9.4055 | **+2.346** | **0.0190** | * |
| Nocturnal time > 180 (%) | -0.0341 | 0.0804 | ±0.1609 | -0.424 | 0.6719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1893**, R² = **0.0412**, Adj R² = **0.0356**, F-statistic = **7.35** (p = **1.94e-12**), Residual SE = **66.728** on **1881** df, AIC = **21287.6**, BIC = **21354.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.8598** | 12.6631 | ±25.3262 | **+31.103** | **2.19e-212** | *** |
| Education: graduate level (vs college) | +2.0571 | 3.3370 | ±6.6739 | +0.616 | 0.5376 |  |
| **Education: high school or below (vs college)** | **-14.8699** | 5.3787 | ±10.7574 | **-2.765** | **0.0057** | ** |
| **Site: UCSD (vs UAB)** | **-11.4235** | 4.0601 | ±8.1203 | **-2.814** | **0.0049** | ** |
| Site: UW (vs UAB) | -1.9555 | 3.8267 | ±7.6535 | -0.511 | 0.6093 |  |
| Age (years) | +0.1585 | 0.1511 | ±0.3021 | +1.050 | 0.2939 |  |
| **BMI (kg/m2)** | **-0.9366** | 0.2315 | ±0.4629 | **-4.047** | **5.20e-05** | *** |
| **Hypertension** | **-13.3933** | 3.3803 | ±6.7607 | **-3.962** | **7.43e-05** | *** |
| High cholesterol | -0.3921 | 3.1419 | ±6.2838 | -0.125 | 0.9007 |  |
| Kidney disease | -4.3399 | 6.1334 | ±12.2668 | -0.708 | 0.4792 |  |
| **Circulatory disease** | **+10.9109** | 4.7122 | ±9.4243 | **+2.315** | **0.0206** | * |
| **Any reading > 250 during wear (0/1)** | **-7.0631** | 3.2888 | ±6.5775 | **-2.148** | **0.0317** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1893**, R² = **0.0391**, Adj R² = **0.0335**, F-statistic = **6.96** (p = **1.23e-11**), Residual SE = **66.802** on **1881** df, AIC = **21291.8**, BIC = **21358.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.2722** | 12.6622 | ±25.3244 | **+31.059** | **8.69e-212** | *** |
| Education: graduate level (vs college) | +2.2246 | 3.3533 | ±6.7067 | +0.663 | 0.5071 |  |
| **Education: high school or below (vs college)** | **-15.2585** | 5.3557 | ±10.7115 | **-2.849** | **0.0044** | ** |
| **Site: UCSD (vs UAB)** | **-11.2271** | 4.0776 | ±8.1552 | **-2.753** | **0.0059** | ** |
| Site: UW (vs UAB) | -1.9820 | 3.8177 | ±7.6354 | -0.519 | 0.6036 |  |
| Age (years) | +0.1308 | 0.1499 | ±0.2999 | +0.872 | 0.3832 |  |
| **BMI (kg/m2)** | **-0.9193** | 0.2327 | ±0.4654 | **-3.951** | **7.79e-05** | *** |
| **Hypertension** | **-14.0511** | 3.3779 | ±6.7559 | **-4.160** | **3.19e-05** | *** |
| High cholesterol | -0.8116 | 3.1446 | ±6.2893 | -0.258 | 0.7963 |  |
| Kidney disease | -5.3176 | 6.1221 | ±12.2442 | -0.869 | 0.3851 |  |
| **Circulatory disease** | **+11.0594** | 4.7066 | ±9.4133 | **+2.350** | **0.0188** | * |
| Time > 250 (%) | -0.0995 | 0.1422 | ±0.2845 | -0.700 | 0.4841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,893)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1893**, R² = **0.0391**, Adj R² = **0.0334**, F-statistic = **6.95** (p = **1.27e-11**), Residual SE = **66.803** on **1881** df, AIC = **21291.9**, BIC = **21358.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.2243** | 12.6643 | ±25.3285 | **+31.050** | **1.14e-211** | *** |
| Education: graduate level (vs college) | +2.2390 | 3.3532 | ±6.7064 | +0.668 | 0.5043 |  |
| **Education: high school or below (vs college)** | **-15.2845** | 5.3555 | ±10.7109 | **-2.854** | **0.0043** | ** |
| **Site: UCSD (vs UAB)** | **-11.2193** | 4.0782 | ±8.1565 | **-2.751** | **0.0059** | ** |
| Site: UW (vs UAB) | -1.9651 | 3.8172 | ±7.6345 | -0.515 | 0.6067 |  |
| Age (years) | +0.1313 | 0.1500 | ±0.3000 | +0.876 | 0.3812 |  |
| **BMI (kg/m2)** | **-0.9198** | 0.2327 | ±0.4654 | **-3.953** | **7.72e-05** | *** |
| **Hypertension** | **-14.0649** | 3.3777 | ±6.7554 | **-4.164** | **3.13e-05** | *** |
| High cholesterol | -0.8149 | 3.1448 | ±6.2895 | -0.259 | 0.7955 |  |
| Kidney disease | -5.3275 | 6.1284 | ±12.2569 | -0.869 | 0.3847 |  |
| **Circulatory disease** | **+11.0577** | 4.7073 | ±9.4146 | **+2.349** | **0.0188** | * |
| Avg. daily time > 250 (%) | -0.0926 | 0.1458 | ±0.2915 | -0.635 | 0.5255 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 1,879; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1879**, R² = **0.1103**, Adj R² = **0.1055**, F-statistic = **23.15** (p = **1.98e-41**), Residual SE = **17.352** on **1868** df, AIC = **16067.5**, BIC = **16128.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7177** | 3.4762 | ±6.9524 | **+16.604** | **6.55e-62** | *** |
| **Education: graduate level (vs college)** | **-3.9358** | 0.8837 | ±1.7674 | **-4.454** | **8.44e-06** | *** |
| Education: high school or below (vs college) | +0.9478 | 1.3115 | ±2.6231 | +0.723 | 0.4699 |  |
| Site: UCSD (vs UAB) | +1.5898 | 1.0854 | ±2.1708 | +1.465 | 0.1430 |  |
| Site: UW (vs UAB) | -1.5643 | 0.9685 | ±1.9369 | -1.615 | 0.1063 |  |
| **Age (years)** | **-0.3088** | 0.0394 | ±0.0788 | **-7.841** | **4.47e-15** | *** |
| **BMI (kg/m2)** | **+0.4470** | 0.0627 | ±0.1253 | **+7.132** | **9.86e-13** | *** |
| **Hypertension** | **+1.8785** | 0.9086 | ±1.8173 | **+2.067** | **0.0387** | * |
| High cholesterol | +0.6371 | 0.8480 | ±1.6960 | +0.751 | 0.4525 |  |
| Kidney disease | +1.5605 | 1.4128 | ±2.8256 | +1.105 | 0.2693 |  |
| Circulatory disease | -1.6304 | 1.1380 | ±2.2760 | -1.433 | 0.1519 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1879**, R² = **0.1393**, Adj R² = **0.1343**, F-statistic = **27.48** (p = **9.64e-54**), Residual SE = **17.071** on **1867** df, AIC = **16007.2**, BIC = **16073.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1420** | 3.9474 | ±7.8948 | **+10.676** | **1.32e-26** | *** |
| **Education: graduate level (vs college)** | **-3.5662** | 0.8737 | ±1.7474 | **-4.082** | **4.47e-05** | *** |
| Education: high school or below (vs college) | -0.2859 | 1.2764 | ±2.5529 | -0.224 | 0.8228 |  |
| Site: UCSD (vs UAB) | +1.7979 | 1.0659 | ±2.1318 | +1.687 | 0.0916 | . |
| Site: UW (vs UAB) | -1.1570 | 0.9523 | ±1.9046 | -1.215 | 0.2244 |  |
| **Age (years)** | **-0.3266** | 0.0386 | ±0.0772 | **-8.462** | **2.62e-17** | *** |
| **BMI (kg/m2)** | **+0.3879** | 0.0609 | ±0.1219 | **+6.366** | **1.94e-10** | *** |
| Hypertension | +1.1710 | 0.9003 | ±1.8007 | +1.301 | 0.1934 |  |
| High cholesterol | +0.0731 | 0.8381 | ±1.6761 | +0.087 | 0.9305 |  |
| Kidney disease | +1.1758 | 1.3966 | ±2.7932 | +0.842 | 0.3998 |  |
| Circulatory disease | -1.7719 | 1.1206 | ±2.2412 | -1.581 | 0.1138 |  |
| **HbA1c (%)** | **+3.1128** | 0.3958 | ±0.7915 | **+7.865** | **3.68e-15** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1879**, R² = **0.1371**, Adj R² = **0.1320**, F-statistic = **26.97** (p = **1.00e-52**), Residual SE = **17.093** on **1867** df, AIC = **16012.0**, BIC = **16078.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8850** | 3.7116 | ±7.4231 | **+12.902** | **4.41e-38** | *** |
| **Education: graduate level (vs college)** | **-3.7344** | 0.8716 | ±1.7431 | **-4.285** | **1.83e-05** | *** |
| Education: high school or below (vs college) | -0.1317 | 1.2721 | ±2.5442 | -0.104 | 0.9175 |  |
| Site: UCSD (vs UAB) | +1.8445 | 1.0726 | ±2.1451 | +1.720 | 0.0855 | . |
| Site: UW (vs UAB) | -1.3610 | 0.9513 | ±1.9025 | -1.431 | 0.1525 |  |
| **Age (years)** | **-0.3224** | 0.0388 | ±0.0776 | **-8.312** | **9.40e-17** | *** |
| **BMI (kg/m2)** | **+0.4085** | 0.0614 | ±0.1227 | **+6.656** | **2.82e-11** | *** |
| Hypertension | +1.2381 | 0.9037 | ±1.8074 | +1.370 | 0.1707 |  |
| High cholesterol | +0.2858 | 0.8387 | ±1.6774 | +0.341 | 0.7333 |  |
| Kidney disease | +0.5419 | 1.4061 | ±2.8122 | +0.385 | 0.6999 |  |
| Circulatory disease | -1.8961 | 1.1233 | ±2.2466 | -1.688 | 0.0914 | . |
| **Mean glucose (mg/dL)** | **+0.0923** | 0.0135 | ±0.0271 | **+6.821** | **9.04e-12** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1879**, R² = **0.1371**, Adj R² = **0.1320**, F-statistic = **26.97** (p = **1.00e-52**), Residual SE = **17.093** on **1867** df, AIC = **16012.0**, BIC = **16078.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+35.1171** | 4.7917 | ±9.5834 | **+7.329** | **2.32e-13** | *** |
| **Education: graduate level (vs college)** | **-3.7344** | 0.8716 | ±1.7431 | **-4.285** | **1.83e-05** | *** |
| Education: high school or below (vs college) | -0.1317 | 1.2721 | ±2.5442 | -0.104 | 0.9175 |  |
| Site: UCSD (vs UAB) | +1.8445 | 1.0726 | ±2.1451 | +1.720 | 0.0855 | . |
| Site: UW (vs UAB) | -1.3610 | 0.9513 | ±1.9025 | -1.431 | 0.1525 |  |
| **Age (years)** | **-0.3224** | 0.0388 | ±0.0776 | **-8.312** | **9.40e-17** | *** |
| **BMI (kg/m2)** | **+0.4085** | 0.0614 | ±0.1227 | **+6.656** | **2.82e-11** | *** |
| Hypertension | +1.2381 | 0.9037 | ±1.8074 | +1.370 | 0.1707 |  |
| High cholesterol | +0.2858 | 0.8387 | ±1.6774 | +0.341 | 0.7333 |  |
| Kidney disease | +0.5419 | 1.4061 | ±2.8122 | +0.385 | 0.6999 |  |
| Circulatory disease | -1.8961 | 1.1233 | ±2.2466 | -1.688 | 0.0914 | . |
| **GMI (%)** | **+3.8573** | 0.5655 | ±1.1310 | **+6.821** | **9.04e-12** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1879**, R² = **0.1324**, Adj R² = **0.1272**, F-statistic = **25.89** (p = **1.43e-50**), Residual SE = **17.140** on **1867** df, AIC = **16022.3**, BIC = **16088.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7816** | 3.7203 | ±7.4407 | **+13.112** | **2.81e-39** | *** |
| **Education: graduate level (vs college)** | **-3.7211** | 0.8757 | ±1.7514 | **-4.249** | **2.14e-05** | *** |
| Education: high school or below (vs college) | -0.0154 | 1.2728 | ±2.5456 | -0.012 | 0.9903 |  |
| Site: UCSD (vs UAB) | +1.7300 | 1.0766 | ±2.1533 | +1.607 | 0.1081 |  |
| Site: UW (vs UAB) | -1.4725 | 0.9536 | ±1.9071 | -1.544 | 0.1225 |  |
| **Age (years)** | **-0.3099** | 0.0389 | ±0.0778 | **-7.971** | **1.58e-15** | *** |
| **BMI (kg/m2)** | **+0.3935** | 0.0614 | ±0.1228 | **+6.407** | **1.48e-10** | *** |
| Hypertension | +1.3930 | 0.9042 | ±1.8085 | +1.541 | 0.1234 |  |
| High cholesterol | +0.3182 | 0.8411 | ±1.6821 | +0.378 | 0.7052 |  |
| Kidney disease | +0.9844 | 1.4020 | ±2.8040 | +0.702 | 0.4826 |  |
| Circulatory disease | -1.8309 | 1.1228 | ±2.2456 | -1.631 | 0.1030 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0842** | 0.0137 | ±0.0274 | **+6.148** | **7.86e-10** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1879**, R² = **0.1316**, Adj R² = **0.1265**, F-statistic = **25.73** (p = **3.04e-50**), Residual SE = **17.147** on **1867** df, AIC = **16023.9**, BIC = **16090.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.5545** | 3.4717 | ±6.9435 | **+15.426** | **1.10e-53** | *** |
| **Education: graduate level (vs college)** | **-3.6714** | 0.8739 | ±1.7477 | **-4.201** | **2.65e-05** | *** |
| Education: high school or below (vs college) | -0.0290 | 1.2893 | ±2.5786 | -0.023 | 0.9820 |  |
| Site: UCSD (vs UAB) | +2.0391 | 1.0740 | ±2.1481 | +1.898 | 0.0576 | . |
| Site: UW (vs UAB) | -1.1068 | 0.9569 | ±1.9138 | -1.157 | 0.2474 |  |
| **Age (years)** | **-0.3300** | 0.0389 | ±0.0779 | **-8.475** | **2.36e-17** | *** |
| **BMI (kg/m2)** | **+0.4282** | 0.0616 | ±0.1232 | **+6.951** | **3.63e-12** | *** |
| Hypertension | +1.2031 | 0.9082 | ±1.8165 | +1.325 | 0.1853 |  |
| High cholesterol | +0.4170 | 0.8422 | ±1.6843 | +0.495 | 0.6205 |  |
| Kidney disease | +0.0014 | 1.4331 | ±2.8661 | +0.001 | 0.9992 |  |
| Circulatory disease | -1.8608 | 1.1281 | ±2.2563 | -1.649 | 0.0991 | . |
| **Glucose SD, pooled (mg/dL)** | **+0.2386** | 0.0379 | ±0.0757 | **+6.302** | **2.95e-10** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1879**, R² = **0.1308**, Adj R² = **0.1256**, F-statistic = **25.53** (p = **7.49e-50**), Residual SE = **17.156** on **1867** df, AIC = **16025.8**, BIC = **16092.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.6130** | 3.4745 | ±6.9490 | **+15.430** | **1.02e-53** | *** |
| **Education: graduate level (vs college)** | **-3.7005** | 0.8733 | ±1.7466 | **-4.237** | **2.26e-05** | *** |
| Education: high school or below (vs college) | -0.0393 | 1.2932 | ±2.5865 | -0.030 | 0.9758 |  |
| Site: UCSD (vs UAB) | +1.9996 | 1.0739 | ±2.1478 | +1.862 | 0.0626 | . |
| Site: UW (vs UAB) | -1.1714 | 0.9584 | ±1.9168 | -1.222 | 0.2216 |  |
| **Age (years)** | **-0.3326** | 0.0390 | ±0.0781 | **-8.523** | **1.55e-17** | *** |
| **BMI (kg/m2)** | **+0.4332** | 0.0616 | ±0.1233 | **+7.029** | **2.09e-12** | *** |
| Hypertension | +1.2239 | 0.9095 | ±1.8190 | +1.346 | 0.1784 |  |
| High cholesterol | +0.4109 | 0.8429 | ±1.6858 | +0.487 | 0.6259 |  |
| Kidney disease | -0.0013 | 1.4382 | ±2.8764 | -0.001 | 0.9993 |  |
| Circulatory disease | -1.8290 | 1.1279 | ±2.2557 | -1.622 | 0.1049 |  |
| **Avg. daily SD (mg/dL)** | **+0.2638** | 0.0435 | ±0.0869 | **+6.069** | **1.29e-09** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1879**, R² = **0.1170**, Adj R² = **0.1118**, F-statistic = **22.49** (p = **1.05e-43**), Residual SE = **17.291** on **1867** df, AIC = **16055.2**, BIC = **16121.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7840** | 3.6853 | ±7.3705 | **+14.323** | **1.57e-46** | *** |
| **Education: graduate level (vs college)** | **-3.8020** | 0.8804 | ±1.7607 | **-4.319** | **1.57e-05** | *** |
| Education: high school or below (vs college) | +0.5950 | 1.3141 | ±2.6282 | +0.453 | 0.6507 |  |
| Site: UCSD (vs UAB) | +1.8943 | 1.0823 | ±2.1646 | +1.750 | 0.0801 | . |
| Site: UW (vs UAB) | -1.2723 | 0.9664 | ±1.9328 | -1.317 | 0.1880 |  |
| **Age (years)** | **-0.3221** | 0.0394 | ±0.0788 | **-8.179** | **2.86e-16** | *** |
| **BMI (kg/m2)** | **+0.4483** | 0.0623 | ±0.1246 | **+7.196** | **6.21e-13** | *** |
| Hypertension | +1.5576 | 0.9108 | ±1.8216 | +1.710 | 0.0872 | . |
| High cholesterol | +0.6067 | 0.8458 | ±1.6915 | +0.717 | 0.4732 |  |
| Kidney disease | +0.7303 | 1.4356 | ±2.8712 | +0.509 | 0.6110 |  |
| Circulatory disease | -1.7097 | 1.1363 | ±2.2725 | -1.505 | 0.1324 |  |
| **CV (%)** | **+0.2959** | 0.0788 | ±0.1575 | **+3.756** | **1.73e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1879**, R² = **0.1198**, Adj R² = **0.1146**, F-statistic = **23.10** (p = **6.14e-45**), Residual SE = **17.263** on **1867** df, AIC = **16049.3**, BIC = **16115.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.2106** | 3.8983 | ±7.7966 | **+16.985** | **1.07e-64** | *** |
| **Education: graduate level (vs college)** | **-3.7802** | 0.8783 | ±1.7567 | **-4.304** | **1.68e-05** | *** |
| Education: high school or below (vs college) | +0.5364 | 1.3090 | ±2.6180 | +0.410 | 0.6820 |  |
| Site: UCSD (vs UAB) | +1.9072 | 1.0788 | ±2.1576 | +1.768 | 0.0771 | . |
| Site: UW (vs UAB) | -1.3236 | 0.9644 | ±1.9289 | -1.372 | 0.1699 |  |
| **Age (years)** | **-0.3242** | 0.0393 | ±0.0785 | **-8.256** | **1.50e-16** | *** |
| **BMI (kg/m2)** | **+0.4477** | 0.0622 | ±0.1245 | **+7.195** | **6.26e-13** | *** |
| Hypertension | +1.4765 | 0.9111 | ±1.8222 | +1.621 | 0.1051 |  |
| High cholesterol | +0.5849 | 0.8443 | ±1.6885 | +0.693 | 0.4885 |  |
| Kidney disease | +0.7872 | 1.4224 | ±2.8448 | +0.553 | 0.5800 |  |
| Circulatory disease | -1.7497 | 1.1358 | ±2.2716 | -1.541 | 0.1234 |  |
| **Mean / SD ratio** | **-1.3596** | 0.2957 | ±0.5914 | **-4.598** | **4.27e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1879**, R² = **0.1180**, Adj R² = **0.1128**, F-statistic = **22.71** (p = **3.74e-44**), Residual SE = **17.281** on **1867** df, AIC = **16053.1**, BIC = **16119.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.3473** | 3.9006 | ±7.8011 | **+16.753** | **5.36e-63** | *** |
| **Education: graduate level (vs college)** | **-3.8225** | 0.8789 | ±1.7577 | **-4.349** | **1.37e-05** | *** |
| Education: high school or below (vs college) | +0.5672 | 1.3119 | ±2.6238 | +0.432 | 0.6655 |  |
| Site: UCSD (vs UAB) | +1.7927 | 1.0793 | ±2.1585 | +1.661 | 0.0967 | . |
| Site: UW (vs UAB) | -1.4053 | 0.9666 | ±1.9332 | -1.454 | 0.1460 |  |
| **Age (years)** | **-0.3255** | 0.0394 | ±0.0788 | **-8.258** | **1.48e-16** | *** |
| **BMI (kg/m2)** | **+0.4482** | 0.0622 | ±0.1245 | **+7.201** | **6.00e-13** | *** |
| Hypertension | +1.5588 | 0.9104 | ±1.8209 | +1.712 | 0.0869 | . |
| High cholesterol | +0.5984 | 0.8455 | ±1.6910 | +0.708 | 0.4791 |  |
| Kidney disease | +0.9050 | 1.4236 | ±2.8472 | +0.636 | 0.5250 |  |
| Circulatory disease | -1.6782 | 1.1371 | ±2.2743 | -1.476 | 0.1400 |  |
| **Avg. daily mean/SD** | **-1.0324** | 0.2475 | ±0.4950 | **-4.171** | **3.03e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1879**, R² = **0.1211**, Adj R² = **0.1159**, F-statistic = **23.38** (p = **1.68e-45**), Residual SE = **17.251** on **1867** df, AIC = **16046.6**, BIC = **16113.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9149** | 3.9013 | ±7.8026 | **+12.538** | **4.62e-36** | *** |
| **Education: graduate level (vs college)** | **-3.7333** | 0.8777 | ±1.7555 | **-4.253** | **2.11e-05** | *** |
| Education: high school or below (vs college) | +0.5042 | 1.3012 | ±2.6023 | +0.388 | 0.6984 |  |
| Site: UCSD (vs UAB) | +1.9196 | 1.0814 | ±2.1628 | +1.775 | 0.0759 | . |
| Site: UW (vs UAB) | -1.0897 | 0.9665 | ±1.9331 | -1.127 | 0.2596 |  |
| **Age (years)** | **-0.3059** | 0.0390 | ±0.0780 | **-7.840** | **4.49e-15** | *** |
| **BMI (kg/m2)** | **+0.4409** | 0.0621 | ±0.1242 | **+7.099** | **1.26e-12** | *** |
| Hypertension | +1.7711 | 0.9068 | ±1.8136 | +1.953 | 0.0508 | . |
| High cholesterol | +0.6586 | 0.8454 | ±1.6909 | +0.779 | 0.4360 |  |
| Kidney disease | +0.9804 | 1.4275 | ±2.8549 | +0.687 | 0.4922 |  |
| Circulatory disease | -1.6236 | 1.1301 | ±2.2603 | -1.437 | 0.1508 |  |
| **MAG (mg/dL/h)** | **+0.2154** | 0.0468 | ±0.0936 | **+4.601** | **4.20e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1879**, R² = **0.1293**, Adj R² = **0.1242**, F-statistic = **25.21** (p = **3.30e-49**), Residual SE = **17.170** on **1867** df, AIC = **16028.8**, BIC = **16095.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3731** | 3.5696 | ±7.1391 | **+14.392** | **5.81e-47** | *** |
| **Education: graduate level (vs college)** | **-3.7213** | 0.8739 | ±1.7478 | **-4.258** | **2.06e-05** | *** |
| Education: high school or below (vs college) | +0.0143 | 1.2954 | ±2.5908 | +0.011 | 0.9912 |  |
| Site: UCSD (vs UAB) | +2.0151 | 1.0751 | ±2.1502 | +1.874 | 0.0609 | . |
| Site: UW (vs UAB) | -1.1746 | 0.9595 | ±1.9190 | -1.224 | 0.2209 |  |
| **Age (years)** | **-0.3285** | 0.0391 | ±0.0782 | **-8.405** | **4.29e-17** | *** |
| **BMI (kg/m2)** | **+0.4468** | 0.0619 | ±0.1238 | **+7.219** | **5.24e-13** | *** |
| Hypertension | +1.3618 | 0.9088 | ±1.8177 | +1.498 | 0.1340 |  |
| High cholesterol | +0.4490 | 0.8425 | ±1.6849 | +0.533 | 0.5940 |  |
| Kidney disease | +0.1402 | 1.4383 | ±2.8767 | +0.097 | 0.9224 |  |
| Circulatory disease | -1.8251 | 1.1289 | ±2.2577 | -1.617 | 0.1059 |  |
| **Avg. daily range (mg/dL)** | **+0.0688** | 0.0113 | ±0.0227 | **+6.060** | **1.36e-09** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1879**, R² = **0.1266**, Adj R² = **0.1214**, F-statistic = **24.60** (p = **5.66e-48**), Residual SE = **17.197** on **1867** df, AIC = **16034.8**, BIC = **16101.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.5034** | 3.4492 | ±6.8984 | **+16.092** | **2.92e-58** | *** |
| **Education: graduate level (vs college)** | **-3.6713** | 0.8803 | ±1.7607 | **-4.170** | **3.04e-05** | *** |
| Education: high school or below (vs college) | +0.3862 | 1.2800 | ±2.5600 | +0.302 | 0.7629 |  |
| Site: UCSD (vs UAB) | +1.9177 | 1.0766 | ±2.1533 | +1.781 | 0.0749 | . |
| Site: UW (vs UAB) | -1.1890 | 0.9571 | ±1.9142 | -1.242 | 0.2141 |  |
| **Age (years)** | **-0.3103** | 0.0390 | ±0.0779 | **-7.965** | **1.66e-15** | *** |
| **BMI (kg/m2)** | **+0.4170** | 0.0617 | ±0.1235 | **+6.755** | **1.43e-11** | *** |
| Hypertension | +1.4325 | 0.9039 | ±1.8077 | +1.585 | 0.1130 |  |
| High cholesterol | +0.4735 | 0.8444 | ±1.6888 | +0.561 | 0.5750 |  |
| Kidney disease | +0.8083 | 1.4110 | ±2.8221 | +0.573 | 0.5667 |  |
| Circulatory disease | -1.9725 | 1.1343 | ±2.2687 | -1.739 | 0.0821 | . |
| **SD of daily means (mg/dL)** | **+0.3867** | 0.0679 | ±0.1358 | **+5.693** | **1.25e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1879**, R² = **0.1348**, Adj R² = **0.1297**, F-statistic = **26.43** (p = **1.17e-51**), Residual SE = **17.116** on **1867** df, AIC = **16017.1**, BIC = **16083.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.0336** | 4.0511 | ±8.1023 | **+18.028** | **1.18e-72** | *** |
| **Education: graduate level (vs college)** | **-3.6781** | 0.8744 | ±1.7488 | **-4.206** | **2.59e-05** | *** |
| Education: high school or below (vs college) | -0.0846 | 1.2705 | ±2.5410 | -0.067 | 0.9469 |  |
| Site: UCSD (vs UAB) | +2.0627 | 1.0757 | ±2.1513 | +1.918 | 0.0552 | . |
| Site: UW (vs UAB) | -1.1459 | 0.9530 | ±1.9060 | -1.202 | 0.2292 |  |
| **Age (years)** | **-0.3227** | 0.0388 | ±0.0777 | **-8.308** | **9.70e-17** | *** |
| **BMI (kg/m2)** | **+0.4114** | 0.0614 | ±0.1229 | **+6.696** | **2.14e-11** | *** |
| Hypertension | +1.4067 | 0.9043 | ±1.8086 | +1.556 | 0.1198 |  |
| High cholesterol | +0.4322 | 0.8404 | ±1.6808 | +0.514 | 0.6071 |  |
| Kidney disease | +0.4977 | 1.4132 | ±2.8263 | +0.352 | 0.7247 |  |
| Circulatory disease | -1.9335 | 1.1256 | ±2.2511 | -1.718 | 0.0858 | . |
| **Time in range 70-180, pooled (%)** | **-0.1501** | 0.0224 | ±0.0448 | **-6.697** | **2.12e-11** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1879**, R² = **0.1341**, Adj R² = **0.1290**, F-statistic = **26.29** (p = **2.24e-51**), Residual SE = **17.122** on **1867** df, AIC = **16018.5**, BIC = **16084.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.8887** | 4.0561 | ±8.1122 | **+17.970** | **3.33e-72** | *** |
| **Education: graduate level (vs college)** | **-3.6908** | 0.8749 | ±1.7498 | **-4.219** | **2.46e-05** | *** |
| Education: high school or below (vs college) | -0.0839 | 1.2710 | ±2.5419 | -0.066 | 0.9474 |  |
| Site: UCSD (vs UAB) | +2.0662 | 1.0760 | ±2.1521 | +1.920 | 0.0548 | . |
| Site: UW (vs UAB) | -1.1518 | 0.9533 | ±1.9067 | -1.208 | 0.2270 |  |
| **Age (years)** | **-0.3235** | 0.0389 | ±0.0777 | **-8.321** | **8.74e-17** | *** |
| **BMI (kg/m2)** | **+0.4113** | 0.0615 | ±0.1230 | **+6.685** | **2.30e-11** | *** |
| Hypertension | +1.4227 | 0.9044 | ±1.8087 | +1.573 | 0.1157 |  |
| High cholesterol | +0.4274 | 0.8406 | ±1.6812 | +0.508 | 0.6111 |  |
| Kidney disease | +0.4913 | 1.4143 | ±2.8285 | +0.347 | 0.7283 |  |
| Circulatory disease | -1.9262 | 1.1263 | ±2.2526 | -1.710 | 0.0872 | . |
| **Avg. daily time in range 70-180 (%)** | **-0.1475** | 0.0223 | ±0.0446 | **-6.620** | **3.59e-11** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1879**, R² = **0.1104**, Adj R² = **0.1052**, F-statistic = **21.07** (p = **8.31e-41**), Residual SE = **17.355** on **1867** df, AIC = **16069.2**, BIC = **16135.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.9982** | 3.5350 | ±7.0699 | **+16.407** | **1.70e-60** | *** |
| **Education: graduate level (vs college)** | **-3.9406** | 0.8844 | ±1.7688 | **-4.456** | **8.36e-06** | *** |
| Education: high school or below (vs college) | +0.9025 | 1.3163 | ±2.6327 | +0.686 | 0.4930 |  |
| Site: UCSD (vs UAB) | +1.5199 | 1.0930 | ±2.1860 | +1.391 | 0.1643 |  |
| Site: UW (vs UAB) | -1.5991 | 0.9721 | ±1.9443 | -1.645 | 0.1000 | . |
| **Age (years)** | **-0.3104** | 0.0396 | ±0.0792 | **-7.841** | **4.48e-15** | *** |
| **BMI (kg/m2)** | **+0.4479** | 0.0627 | ±0.1254 | **+7.145** | **9.00e-13** | *** |
| **Hypertension** | **+1.8841** | 0.9092 | ±1.8184 | **+2.072** | **0.0382** | * |
| High cholesterol | +0.6025 | 0.8507 | ±1.7014 | +0.708 | 0.4788 |  |
| Kidney disease | +1.5399 | 1.4148 | ±2.8296 | +1.088 | 0.2764 |  |
| Circulatory disease | -1.5869 | 1.1395 | ±2.2790 | -1.393 | 0.1637 |  |
| Any reading < 54 during wear (0/1) | -0.5158 | 0.8771 | ±1.7541 | -0.588 | 0.5565 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1879**, R² = **0.1103**, Adj R² = **0.1050**, F-statistic = **21.04** (p = **9.79e-41**), Residual SE = **17.357** on **1867** df, AIC = **16069.5**, BIC = **16136.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7103** | 3.4889 | ±6.9777 | **+16.541** | **1.85e-61** | *** |
| **Education: graduate level (vs college)** | **-3.9355** | 0.8837 | ±1.7673 | **-4.454** | **8.44e-06** | *** |
| Education: high school or below (vs college) | +0.9495 | 1.3134 | ±2.6269 | +0.723 | 0.4697 |  |
| Site: UCSD (vs UAB) | +1.5930 | 1.0921 | ±2.1843 | +1.459 | 0.1447 |  |
| Site: UW (vs UAB) | -1.5617 | 0.9728 | ±1.9456 | -1.605 | 0.1084 |  |
| **Age (years)** | **-0.3087** | 0.0394 | ±0.0788 | **-7.833** | **4.78e-15** | *** |
| **BMI (kg/m2)** | **+0.4470** | 0.0627 | ±0.1254 | **+7.127** | **1.02e-12** | *** |
| **Hypertension** | **+1.8789** | 0.9090 | ±1.8181 | **+2.067** | **0.0387** | * |
| High cholesterol | +0.6384 | 0.8488 | ±1.6977 | +0.752 | 0.4520 |  |
| Kidney disease | +1.5606 | 1.4129 | ±2.8259 | +1.104 | 0.2694 |  |
| Circulatory disease | -1.6312 | 1.1387 | ±2.2775 | -1.432 | 0.1520 |  |
| Time < 54 (%) | +0.0202 | 0.6936 | ±1.3871 | +0.029 | 0.9767 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1879**, R² = **0.1103**, Adj R² = **0.1051**, F-statistic = **21.04** (p = **9.44e-41**), Residual SE = **17.356** on **1867** df, AIC = **16069.5**, BIC = **16135.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7651** | 3.4810 | ±6.9620 | **+16.594** | **7.64e-62** | *** |
| **Education: graduate level (vs college)** | **-3.9425** | 0.8838 | ±1.7677 | **-4.461** | **8.17e-06** | *** |
| Education: high school or below (vs college) | +0.9318 | 1.3131 | ±2.6262 | +0.710 | 0.4779 |  |
| Site: UCSD (vs UAB) | +1.5619 | 1.0908 | ±2.1815 | +1.432 | 0.1522 |  |
| Site: UW (vs UAB) | -1.5913 | 0.9726 | ±1.9452 | -1.636 | 0.1018 |  |
| **Age (years)** | **-0.3087** | 0.0394 | ±0.0788 | **-7.836** | **4.64e-15** | *** |
| **BMI (kg/m2)** | **+0.4470** | 0.0627 | ±0.1254 | **+7.127** | **1.02e-12** | *** |
| **Hypertension** | **+1.8742** | 0.9091 | ±1.8182 | **+2.062** | **0.0393** | * |
| High cholesterol | +0.6242 | 0.8492 | ±1.6983 | +0.735 | 0.4623 |  |
| Kidney disease | +1.5612 | 1.4131 | ±2.8261 | +1.105 | 0.2692 |  |
| Circulatory disease | -1.6230 | 1.1393 | ±2.2787 | -1.424 | 0.1543 |  |
| Avg. daily time < 54 (%) | -0.2446 | 0.9200 | ±1.8401 | -0.266 | 0.7904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1879**, R² = **0.1111**, Adj R² = **0.1058**, F-statistic = **21.21** (p = **4.40e-41**), Residual SE = **17.349** on **1867** df, AIC = **16067.9**, BIC = **16134.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.0780** | 3.4998 | ±6.9997 | **+16.594** | **7.65e-62** | *** |
| **Education: graduate level (vs college)** | **-3.9840** | 0.8843 | ±1.7686 | **-4.505** | **6.63e-06** | *** |
| Education: high school or below (vs college) | +0.8874 | 1.3111 | ±2.6222 | +0.677 | 0.4985 |  |
| Site: UCSD (vs UAB) | +1.4734 | 1.0910 | ±2.1819 | +1.351 | 0.1768 |  |
| Site: UW (vs UAB) | -1.6717 | 0.9711 | ±1.9421 | -1.721 | 0.0852 | . |
| **Age (years)** | **-0.3095** | 0.0394 | ±0.0789 | **-7.847** | **4.25e-15** | *** |
| **BMI (kg/m2)** | **+0.4477** | 0.0628 | ±0.1255 | **+7.133** | **9.84e-13** | *** |
| **Hypertension** | **+1.8522** | 0.9091 | ±1.8182 | **+2.037** | **0.0416** | * |
| High cholesterol | +0.5855 | 0.8480 | ±1.6959 | +0.690 | 0.4899 |  |
| Kidney disease | +1.5490 | 1.4115 | ±2.8230 | +1.097 | 0.2725 |  |
| Circulatory disease | -1.6108 | 1.1398 | ±2.2797 | -1.413 | 0.1576 |  |
| Time 54-69, pooled (%) | -0.3514 | 0.2818 | ±0.5636 | -1.247 | 0.2124 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1879**, R² = **0.1112**, Adj R² = **0.1059**, F-statistic = **21.23** (p = **3.94e-41**), Residual SE = **17.348** on **1867** df, AIC = **16067.6**, BIC = **16134.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.0195** | 3.4922 | ±6.9845 | **+16.614** | **5.53e-62** | *** |
| **Education: graduate level (vs college)** | **-3.9917** | 0.8848 | ±1.7697 | **-4.511** | **6.44e-06** | *** |
| Education: high school or below (vs college) | +0.8871 | 1.3107 | ±2.6214 | +0.677 | 0.4985 |  |
| Site: UCSD (vs UAB) | +1.4839 | 1.0896 | ±2.1792 | +1.362 | 0.1732 |  |
| Site: UW (vs UAB) | -1.6775 | 0.9703 | ±1.9406 | -1.729 | 0.0838 | . |
| **Age (years)** | **-0.3086** | 0.0394 | ±0.0788 | **-7.832** | **4.79e-15** | *** |
| **BMI (kg/m2)** | **+0.4477** | 0.0628 | ±0.1255 | **+7.134** | **9.76e-13** | *** |
| **Hypertension** | **+1.8511** | 0.9091 | ±1.8182 | **+2.036** | **0.0417** | * |
| High cholesterol | +0.5880 | 0.8476 | ±1.6952 | +0.694 | 0.4878 |  |
| Kidney disease | +1.5469 | 1.4111 | ±2.8222 | +1.096 | 0.2730 |  |
| Circulatory disease | -1.6126 | 1.1401 | ±2.2802 | -1.414 | 0.1572 |  |
| Avg. daily time 54-69 (%) | -0.3685 | 0.2883 | ±0.5767 | -1.278 | 0.2012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1879**, R² = **0.1108**, Adj R² = **0.1055**, F-statistic = **21.14** (p = **5.89e-41**), Residual SE = **17.352** on **1867** df, AIC = **16068.5**, BIC = **16134.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.0301** | 3.5009 | ±7.0017 | **+16.576** | **1.04e-61** | *** |
| **Education: graduate level (vs college)** | **-3.9708** | 0.8840 | ±1.7681 | **-4.492** | **7.06e-06** | *** |
| Education: high school or below (vs college) | +0.8902 | 1.3119 | ±2.6238 | +0.679 | 0.4974 |  |
| Site: UCSD (vs UAB) | +1.4794 | 1.0928 | ±2.1857 | +1.354 | 0.1758 |  |
| Site: UW (vs UAB) | -1.6620 | 0.9725 | ±1.9451 | -1.709 | 0.0875 | . |
| **Age (years)** | **-0.3095** | 0.0394 | ±0.0789 | **-7.849** | **4.19e-15** | *** |
| **BMI (kg/m2)** | **+0.4474** | 0.0627 | ±0.1255 | **+7.131** | **1.00e-12** | *** |
| **Hypertension** | **+1.8572** | 0.9091 | ±1.8183 | **+2.043** | **0.0411** | * |
| High cholesterol | +0.5889 | 0.8485 | ±1.6970 | +0.694 | 0.4877 |  |
| Kidney disease | +1.5528 | 1.4122 | ±2.8244 | +1.100 | 0.2715 |  |
| Circulatory disease | -1.6092 | 1.1399 | ±2.2798 | -1.412 | 0.1580 |  |
| Time < 70 (%) | -0.2253 | 0.2222 | ±0.4444 | -1.014 | 0.3106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1879**, R² = **0.1110**, Adj R² = **0.1057**, F-statistic = **21.19** (p = **4.85e-41**), Residual SE = **17.350** on **1867** df, AIC = **16068.1**, BIC = **16134.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.9897** | 3.4908 | ±6.9816 | **+16.612** | **5.68e-62** | *** |
| **Education: graduate level (vs college)** | **-3.9839** | 0.8846 | ±1.7692 | **-4.504** | **6.68e-06** | *** |
| Education: high school or below (vs college) | +0.8860 | 1.3113 | ±2.6227 | +0.676 | 0.4992 |  |
| Site: UCSD (vs UAB) | +1.4820 | 1.0907 | ±2.1814 | +1.359 | 0.1742 |  |
| Site: UW (vs UAB) | -1.6764 | 0.9714 | ±1.9429 | -1.726 | 0.0844 | . |
| **Age (years)** | **-0.3086** | 0.0394 | ±0.0788 | **-7.833** | **4.75e-15** | *** |
| **BMI (kg/m2)** | **+0.4475** | 0.0628 | ±0.1255 | **+7.132** | **9.91e-13** | *** |
| **Hypertension** | **+1.8539** | 0.9091 | ±1.8183 | **+2.039** | **0.0414** | * |
| High cholesterol | +0.5872 | 0.8481 | ±1.6961 | +0.692 | 0.4887 |  |
| Kidney disease | +1.5514 | 1.4116 | ±2.8233 | +1.099 | 0.2718 |  |
| Circulatory disease | -1.6092 | 1.1403 | ±2.2807 | -1.411 | 0.1582 |  |
| Avg. daily time < 70 (%) | -0.2685 | 0.2412 | ±0.4825 | -1.113 | 0.2657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1879**, R² = **0.1208**, Adj R² = **0.1156**, F-statistic = **23.32** (p = **2.19e-45**), Residual SE = **17.254** on **1867** df, AIC = **16047.2**, BIC = **16113.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.9873** | 5.5652 | ±11.1303 | **+13.474** | **2.21e-41** | *** |
| **Education: graduate level (vs college)** | **-3.7057** | 0.8842 | ±1.7683 | **-4.191** | **2.77e-05** | *** |
| Education: high school or below (vs college) | +0.3733 | 1.2835 | ±2.5670 | +0.291 | 0.7712 |  |
| Site: UCSD (vs UAB) | +1.8115 | 1.0813 | ±2.1627 | +1.675 | 0.0939 | . |
| Site: UW (vs UAB) | -1.2518 | 0.9647 | ±1.9294 | -1.298 | 0.1944 |  |
| **Age (years)** | **-0.3053** | 0.0390 | ±0.0780 | **-7.825** | **5.07e-15** | *** |
| **BMI (kg/m2)** | **+0.4323** | 0.0623 | ±0.1246 | **+6.938** | **3.98e-12** | *** |
| Hypertension | +1.6839 | 0.9056 | ±1.8111 | +1.860 | 0.0630 | . |
| High cholesterol | +0.6123 | 0.8452 | ±1.6903 | +0.724 | 0.4688 |  |
| Kidney disease | +1.1265 | 1.4155 | ±2.8311 | +0.796 | 0.4261 |  |
| Circulatory disease | -1.7772 | 1.1296 | ±2.2592 | -1.573 | 0.1156 |  |
| **Time 54-250, pooled (%)** | **-0.1761** | 0.0455 | ±0.0911 | **-3.868** | **1.10e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1879**, R² = **0.1207**, Adj R² = **0.1155**, F-statistic = **23.30** (p = **2.39e-45**), Residual SE = **17.254** on **1867** df, AIC = **16047.4**, BIC = **16113.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.3014** | 5.6852 | ±11.3704 | **+13.245** | **4.81e-40** | *** |
| **Education: graduate level (vs college)** | **-3.7091** | 0.8842 | ±1.7684 | **-4.195** | **2.73e-05** | *** |
| Education: high school or below (vs college) | +0.3766 | 1.2836 | ±2.5672 | +0.293 | 0.7692 |  |
| Site: UCSD (vs UAB) | +1.8066 | 1.0813 | ±2.1626 | +1.671 | 0.0948 | . |
| Site: UW (vs UAB) | -1.2644 | 0.9645 | ±1.9290 | -1.311 | 0.1899 |  |
| **Age (years)** | **-0.3065** | 0.0390 | ±0.0781 | **-7.851** | **4.11e-15** | *** |
| **BMI (kg/m2)** | **+0.4319** | 0.0624 | ±0.1248 | **+6.924** | **4.39e-12** | *** |
| Hypertension | +1.6936 | 0.9055 | ±1.8109 | +1.870 | 0.0614 | . |
| High cholesterol | +0.6122 | 0.8451 | ±1.6901 | +0.724 | 0.4688 |  |
| Kidney disease | +1.1034 | 1.4161 | ±2.8323 | +0.779 | 0.4359 |  |
| Circulatory disease | -1.7862 | 1.1298 | ±2.2596 | -1.581 | 0.1139 |  |
| **Avg. daily time 54-250 (%)** | **-0.1782** | 0.0469 | ±0.0937 | **-3.804** | **1.43e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1879**, R² = **0.1353**, Adj R² = **0.1302**, F-statistic = **26.56** (p = **6.64e-52**), Residual SE = **17.111** on **1867** df, AIC = **16015.9**, BIC = **16082.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.9084** | 3.3982 | ±6.7964 | **+17.335** | **2.56e-67** | *** |
| **Education: graduate level (vs college)** | **-3.8710** | 0.8702 | ±1.7404 | **-4.448** | **8.65e-06** | *** |
| Education: high school or below (vs college) | +0.0499 | 1.2859 | ±2.5717 | +0.039 | 0.9690 |  |
| Site: UCSD (vs UAB) | +1.9597 | 1.0742 | ±2.1485 | +1.824 | 0.0681 | . |
| Site: UW (vs UAB) | -1.3966 | 0.9516 | ±1.9031 | -1.468 | 0.1422 |  |
| **Age (years)** | **-0.3359** | 0.0390 | ±0.0781 | **-8.607** | **7.50e-18** | *** |
| **BMI (kg/m2)** | **+0.4111** | 0.0614 | ±0.1227 | **+6.700** | **2.08e-11** | *** |
| Hypertension | +1.3777 | 0.9065 | ±1.8130 | +1.520 | 0.1286 |  |
| High cholesterol | +0.3121 | 0.8405 | ±1.6809 | +0.371 | 0.7103 |  |
| Kidney disease | +0.4585 | 1.4080 | ±2.8160 | +0.326 | 0.7447 |  |
| Circulatory disease | -1.8982 | 1.1308 | ±2.2616 | -1.679 | 0.0932 | . |
| **Time 181-250, pooled (%)** | **+0.2369** | 0.0339 | ±0.0679 | **+6.980** | **2.96e-12** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1879**, R² = **0.1346**, Adj R² = **0.1295**, F-statistic = **26.40** (p = **1.35e-51**), Residual SE = **17.117** on **1867** df, AIC = **16017.4**, BIC = **16083.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8752** | 3.4000 | ±6.8000 | **+17.316** | **3.55e-67** | *** |
| **Education: graduate level (vs college)** | **-3.8810** | 0.8710 | ±1.7421 | **-4.456** | **8.37e-06** | *** |
| Education: high school or below (vs college) | +0.0363 | 1.2840 | ±2.5680 | +0.028 | 0.9775 |  |
| Site: UCSD (vs UAB) | +1.9877 | 1.0746 | ±2.1492 | +1.850 | 0.0644 | . |
| Site: UW (vs UAB) | -1.3784 | 0.9522 | ±1.9043 | -1.448 | 0.1477 |  |
| **Age (years)** | **-0.3347** | 0.0390 | ±0.0781 | **-8.575** | **9.92e-18** | *** |
| **BMI (kg/m2)** | **+0.4111** | 0.0614 | ±0.1228 | **+6.696** | **2.15e-11** | *** |
| Hypertension | +1.3882 | 0.9067 | ±1.8133 | +1.531 | 0.1257 |  |
| High cholesterol | +0.3109 | 0.8408 | ±1.6817 | +0.370 | 0.7116 |  |
| Kidney disease | +0.4722 | 1.4093 | ±2.8185 | +0.335 | 0.7376 |  |
| Circulatory disease | -1.8800 | 1.1321 | ±2.2643 | -1.661 | 0.0968 | . |
| **Avg. daily time 181-250 (%)** | **+0.2305** | 0.0335 | ±0.0670 | **+6.879** | **6.03e-12** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1879**, R² = **0.1350**, Adj R² = **0.1299**, F-statistic = **26.48** (p = **9.26e-52**), Residual SE = **17.114** on **1867** df, AIC = **16016.6**, BIC = **16083.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2342** | 3.3946 | ±6.7892 | **+17.155** | **5.76e-66** | *** |
| **Education: graduate level (vs college)** | **-3.7025** | 0.8739 | ±1.7479 | **-4.237** | **2.27e-05** | *** |
| Education: high school or below (vs college) | -0.1182 | 1.2710 | ±2.5420 | -0.093 | 0.9259 |  |
| Site: UCSD (vs UAB) | +1.9874 | 1.0749 | ±2.1498 | +1.849 | 0.0645 | . |
| Site: UW (vs UAB) | -1.2126 | 0.9523 | ±1.9047 | -1.273 | 0.2029 |  |
| **Age (years)** | **-0.3232** | 0.0389 | ±0.0777 | **-8.318** | **8.97e-17** | *** |
| **BMI (kg/m2)** | **+0.4119** | 0.0615 | ±0.1230 | **+6.698** | **2.12e-11** | *** |
| Hypertension | +1.3948 | 0.9046 | ±1.8091 | +1.542 | 0.1231 |  |
| High cholesterol | +0.4012 | 0.8403 | ±1.6807 | +0.477 | 0.6331 |  |
| Kidney disease | +0.4973 | 1.4123 | ±2.8247 | +0.352 | 0.7247 |  |
| Circulatory disease | -1.9181 | 1.1266 | ±2.2531 | -1.703 | 0.0886 | . |
| **Time > 180 (%)** | **+0.1494** | 0.0222 | ±0.0444 | **+6.734** | **1.65e-11** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1879**, R² = **0.1346**, Adj R² = **0.1295**, F-statistic = **26.39** (p = **1.44e-51**), Residual SE = **17.118** on **1867** df, AIC = **16017.6**, BIC = **16084.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2910** | 3.3974 | ±6.7948 | **+17.157** | **5.53e-66** | *** |
| **Education: graduate level (vs college)** | **-3.7168** | 0.8743 | ±1.7486 | **-4.251** | **2.13e-05** | *** |
| Education: high school or below (vs college) | -0.1196 | 1.2711 | ±2.5422 | -0.094 | 0.9250 |  |
| Site: UCSD (vs UAB) | +2.0077 | 1.0754 | ±2.1507 | +1.867 | 0.0619 | . |
| Site: UW (vs UAB) | -1.2128 | 0.9527 | ±1.9054 | -1.273 | 0.2030 |  |
| **Age (years)** | **-0.3234** | 0.0389 | ±0.0777 | **-8.320** | **8.81e-17** | *** |
| **BMI (kg/m2)** | **+0.4115** | 0.0616 | ±0.1231 | **+6.685** | **2.31e-11** | *** |
| Hypertension | +1.4084 | 0.9046 | ±1.8093 | +1.557 | 0.1195 |  |
| High cholesterol | +0.3996 | 0.8403 | ±1.6807 | +0.476 | 0.6344 |  |
| Kidney disease | +0.4845 | 1.4133 | ±2.8266 | +0.343 | 0.7317 |  |
| Circulatory disease | -1.9150 | 1.1272 | ±2.2544 | -1.699 | 0.0893 | . |
| **Avg. daily time > 180 (%)** | **+0.1477** | 0.0221 | ±0.0442 | **+6.684** | **2.32e-11** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1879**, R² = **0.1263**, Adj R² = **0.1212**, F-statistic = **24.54** (p = **7.43e-48**), Residual SE = **17.199** on **1867** df, AIC = **16035.3**, BIC = **16101.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.2030** | 3.4251 | ±6.8503 | **+16.993** | **9.27e-65** | *** |
| **Education: graduate level (vs college)** | **-3.6715** | 0.8814 | ±1.7627 | **-4.166** | **3.10e-05** | *** |
| Education: high school or below (vs college) | +0.1466 | 1.2721 | ±2.5443 | +0.115 | 0.9083 |  |
| Site: UCSD (vs UAB) | +1.9291 | 1.0804 | ±2.1608 | +1.786 | 0.0742 | . |
| Site: UW (vs UAB) | -1.3113 | 0.9570 | ±1.9140 | -1.370 | 0.1706 |  |
| **Age (years)** | **-0.3121** | 0.0391 | ±0.0782 | **-7.980** | **1.46e-15** | *** |
| **BMI (kg/m2)** | **+0.4059** | 0.0621 | ±0.1241 | **+6.541** | **6.10e-11** | *** |
| Hypertension | +1.5967 | 0.9069 | ±1.8138 | +1.761 | 0.0783 | . |
| High cholesterol | +0.5123 | 0.8447 | ±1.6893 | +0.607 | 0.5442 |  |
| Kidney disease | +0.9461 | 1.4122 | ±2.8244 | +0.670 | 0.5029 |  |
| Circulatory disease | -1.8471 | 1.1279 | ±2.2559 | -1.638 | 0.1015 |  |
| **Nocturnal time > 180 (%)** | **+0.1206** | 0.0222 | ±0.0443 | **+5.441** | **5.30e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1879**, R² = **0.1247**, Adj R² = **0.1195**, F-statistic = **24.17** (p = **4.11e-47**), Residual SE = **17.216** on **1867** df, AIC = **16038.9**, BIC = **16105.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2165** | 3.4374 | ±6.8749 | **+16.645** | **3.28e-62** | *** |
| **Education: graduate level (vs college)** | **-3.7532** | 0.8762 | ±1.7525 | **-4.283** | **1.84e-05** | *** |
| Education: high school or below (vs college) | +0.5038 | 1.2955 | ±2.5911 | +0.389 | 0.6974 |  |
| Site: UCSD (vs UAB) | +1.7727 | 1.0776 | ±2.1553 | +1.645 | 0.1000 | . |
| Site: UW (vs UAB) | -1.4470 | 0.9581 | ±1.9163 | -1.510 | 0.1310 |  |
| **Age (years)** | **-0.3263** | 0.0393 | ±0.0786 | **-8.301** | **1.03e-16** | *** |
| **BMI (kg/m2)** | **+0.4528** | 0.0618 | ±0.1237 | **+7.320** | **2.47e-13** | *** |
| Hypertension | +1.4146 | 0.9067 | ±1.8134 | +1.560 | 0.1187 |  |
| High cholesterol | +0.3484 | 0.8449 | ±1.6898 | +0.412 | 0.6801 |  |
| Kidney disease | +0.7684 | 1.4286 | ±2.8573 | +0.538 | 0.5907 |  |
| Circulatory disease | -1.6188 | 1.1380 | ±2.2759 | -1.423 | 0.1549 |  |
| **Any reading > 250 during wear (0/1)** | **+4.7059** | 0.8561 | ±1.7123 | **+5.497** | **3.87e-08** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1879**, R² = **0.1208**, Adj R² = **0.1156**, F-statistic = **23.32** (p = **2.24e-45**), Residual SE = **17.254** on **1867** df, AIC = **16047.2**, BIC = **16113.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.4421** | 3.4457 | ±6.8914 | **+16.671** | **2.15e-62** | *** |
| **Education: graduate level (vs college)** | **-3.7093** | 0.8841 | ±1.7683 | **-4.195** | **2.72e-05** | *** |
| Education: high school or below (vs college) | +0.3594 | 1.2839 | ±2.5677 | +0.280 | 0.7795 |  |
| Site: UCSD (vs UAB) | +1.7833 | 1.0809 | ±2.1619 | +1.650 | 0.0990 | . |
| Site: UW (vs UAB) | -1.2747 | 0.9641 | ±1.9282 | -1.322 | 0.1861 |  |
| **Age (years)** | **-0.3056** | 0.0390 | ±0.0780 | **-7.831** | **4.83e-15** | *** |
| **BMI (kg/m2)** | **+0.4323** | 0.0623 | ±0.1246 | **+6.937** | **3.99e-12** | *** |
| Hypertension | +1.6808 | 0.9056 | ±1.8113 | +1.856 | 0.0635 | . |
| High cholesterol | +0.6005 | 0.8451 | ±1.6903 | +0.711 | 0.4774 |  |
| Kidney disease | +1.1269 | 1.4156 | ±2.8311 | +0.796 | 0.4260 |  |
| Circulatory disease | -1.7703 | 1.1299 | ±2.2597 | -1.567 | 0.1172 |  |
| **Time > 250 (%)** | **+0.1758** | 0.0455 | ±0.0909 | **+3.868** | **1.10e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,879)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1879**, R² = **0.1208**, Adj R² = **0.1156**, F-statistic = **23.31** (p = **2.27e-45**), Residual SE = **17.254** on **1867** df, AIC = **16047.2**, BIC = **16113.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.5138** | 3.4480 | ±6.8960 | **+16.680** | **1.82e-62** | *** |
| **Education: graduate level (vs college)** | **-3.7134** | 0.8841 | ±1.7682 | **-4.200** | **2.67e-05** | *** |
| Education: high school or below (vs college) | +0.3634 | 1.2838 | ±2.5676 | +0.283 | 0.7771 |  |
| Site: UCSD (vs UAB) | +1.7868 | 1.0810 | ±2.1620 | +1.653 | 0.0983 | . |
| Site: UW (vs UAB) | -1.2834 | 0.9640 | ±1.9280 | -1.331 | 0.1831 |  |
| **Age (years)** | **-0.3064** | 0.0390 | ±0.0781 | **-7.851** | **4.13e-15** | *** |
| **BMI (kg/m2)** | **+0.4319** | 0.0624 | ±0.1248 | **+6.923** | **4.42e-12** | *** |
| Hypertension | +1.6900 | 0.9055 | ±1.8110 | +1.866 | 0.0620 | . |
| High cholesterol | +0.6027 | 0.8450 | ±1.6899 | +0.713 | 0.4756 |  |
| Kidney disease | +1.1028 | 1.4161 | ±2.8322 | +0.779 | 0.4361 |  |
| Circulatory disease | -1.7811 | 1.1300 | ±2.2600 | -1.576 | 0.1150 |  |
| **Avg. daily time > 250 (%)** | **+0.1787** | 0.0469 | ±0.0937 | **+3.812** | **1.38e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
