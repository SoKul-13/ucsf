# Phase 6 model output tables - All (analysis base) - Total analysis base - Wearable activity

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


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
