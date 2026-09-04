# Comprehensive Multimodal CGM Outcome Prediction Report
## Evaluation of CGM Features vs. HbA1c across Cognition, Depression, Environment, and Wearable Activity

### Executive Summary
This analysis evaluates whether Continuous Glucose Monitoring (CGM) derived metrics predict outcomes across four major domain pillars:
1. **Cognition**: MoCA Total Score, MoCA domain scores (Memory, Orientation, Abstraction), and Cognitive Impairment (`MoCA < 26`).
2. **Depression**: CESD-10 Total Score and High Depression Risk (`CESD-10 >= 10`).
3. **Environment**: Ambient Temperature, Relative Humidity, Indoor PM2.5, PM10, VOC, and NOx levels.
4. **Wearable Activity**: Daily Steps, Active Calories, Stress Levels, and Heart Rate.

For every outcome, three nested regression specifications were estimated (adjusting for age, BMI, education, hypertension, cholesterol, kidney disease, and circulatory disease):
- **Model 1 (HbA1c Only)**: Outcome ~ Covariates + `HbA1c`
- **Model 2 (CGM Features Only)**: Outcome ~ Covariates + `Mean Glucose` + `Glucose SD` + `Mean/SD Ratio` + `TIR (70-180)`
- **Model 3 (Combined)**: Outcome ~ Covariates + `HbA1c` + `Mean Glucose` + `Glucose SD` + `Mean/SD Ratio` + `TIR (70-180)`


---
## Domain: Cognition

### Target: MoCA Total Score (N = 1691, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.1010 | 0.0962 | -4221.59 | 8463.17 |
| **Model 2** | CGM Features Only | 0.1131 | 0.1069 | -4328.89 | 8683.79 |
| **Model 3** | Combined (HbA1c + CGM) | **0.1131** | **0.1062** | **-4210.15** | **8448.30** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -0.0906 | 0.1452 | -0.624 | 0.5326 | [-0.3754, 0.1941] |
| `mean_glucose` | -0.0347 | 0.0085 | -4.108 | **0.0000** ⭐ | [-0.0513, -0.0181] |
| `glucose_sd` | -0.0014 | 0.0261 | -0.054 | 0.9570 | [-0.0526, 0.0497] |
| `mean_to_sd_ratio` | 0.0709 | 0.1272 | 0.557 | 0.5773 | [-0.1786, 0.3204] |
| `tir` | -0.0430 | 0.0125 | -3.438 | **0.0006** ⭐ | [-0.0675, -0.0185] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 22.875$, $p = **1.3414e-04**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 237.493$, $p = **1.3849e-53**$


### Target: MoCA Memory Domain (N = 1691, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0703 | 0.0653 | -4058.45 | 8136.90 |
| **Model 2** | CGM Features Only | 0.0740 | 0.0675 | -4163.15 | 8352.31 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0735** | **0.0664** | **-4055.47** | **8138.94** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 0.0395 | 0.1325 | 0.298 | 0.7659 | [-0.2204, 0.2993] |
| `mean_glucose` | -0.0124 | 0.0077 | -1.609 | 0.1077 | [-0.0275, 0.0027] |
| `glucose_sd` | -0.0104 | 0.0238 | -0.435 | 0.6636 | [-0.0570, 0.0363] |
| `mean_to_sd_ratio` | -0.0411 | 0.1161 | -0.354 | 0.7234 | [-0.2688, 0.1866] |
| `tir` | -0.0117 | 0.0114 | -1.025 | 0.3053 | [-0.0341, 0.0107] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 5.967$, $p = 0.2016$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 215.369$, $p = **9.2586e-49**$


### Target: MoCA Orientation Domain (N = 1691, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0202 | 0.0150 | -672.92 | 1365.85 |
| **Model 2** | CGM Features Only | 0.0226 | 0.0158 | -702.97 | 1431.94 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0231** | **0.0155** | **-670.49** | **1368.98** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -0.0311 | 0.0179 | -1.739 | 0.0823 | [-0.0662, 0.0040] |
| `mean_glucose` | 0.0012 | 0.0010 | 1.179 | 0.2387 | [-0.0008, 0.0033] |
| `glucose_sd` | -0.0030 | 0.0032 | -0.922 | 0.3569 | [-0.0093, 0.0033] |
| `mean_to_sd_ratio` | 0.0004 | 0.0157 | 0.024 | 0.9807 | [-0.0304, 0.0311] |
| `tir` | 0.0002 | 0.0015 | 0.110 | 0.9126 | [-0.0029, 0.0032] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 4.864$, $p = 0.3015$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 64.963$, $p = **7.6299e-16**$


### Target: MoCA Abstraction Domain (N = 1691, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0726 | 0.0676 | -588.33 | 1196.66 |
| **Model 2** | CGM Features Only | 0.0793 | 0.0729 | -607.30 | 1240.59 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0764** | **0.0693** | **-584.83** | **1197.67** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -0.0182 | 0.0170 | -1.071 | 0.2841 | [-0.0516, 0.0151] |
| `mean_glucose` | -0.0011 | 0.0010 | -1.068 | 0.2858 | [-0.0030, 0.0009] |
| `glucose_sd` | -0.0025 | 0.0031 | -0.815 | 0.4153 | [-0.0085, 0.0035] |
| `mean_to_sd_ratio` | -0.0006 | 0.0149 | -0.043 | 0.9657 | [-0.0299, 0.0286] |
| `tir` | -0.0036 | 0.0015 | -2.446 | **0.0146** ⭐ | [-0.0065, -0.0007] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 6.992$, $p = 0.1363$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 44.924$, $p = **2.0481e-11**$


### Target: Cognitive Impairment (MoCA < 26) (N = 1691, Model = GLM)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | ROC-AUC | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.6688 | -1067.31 | 2154.61 |
| **Model 2** | CGM Features Only | 0.6796 | -1085.94 | 2197.87 |
| **Model 3** | Combined (HbA1c + CGM) | **0.6807** | **-1057.96** | **2143.92** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Odds Ratio (OR) | Std Error | $z$-stat | $p$-value | 95% CI (OR) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 0.0312 | 1.0317 | 0.1035 | 0.301 | 0.7631 | [0.8422, 1.2638] |
| `mean_glucose` | 0.0218 | 1.0221 | 0.0063 | 3.450 | **0.0006** ⭐ | [1.0095, 1.0348] |
| `glucose_sd` | 0.0094 | 1.0095 | 0.0189 | 0.497 | 0.6189 | [0.9727, 1.0476] |
| `mean_to_sd_ratio` | -0.0045 | 0.9955 | 0.0943 | -0.048 | 0.9616 | [0.8274, 1.1976] |
| `tir` | 0.0283 | 1.0287 | 0.0093 | 3.046 | **0.0023** ⭐ | [1.0101, 1.0477] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 18.693$, $p = **9.0282e-04**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 55.951$, $p = **7.4318e-14**$



---
## Domain: Depression

### Target: CESD-10 Depression Score (N = 1688, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.1047 | 0.0998 | -5003.00 | 10026.00 |
| **Model 2** | CGM Features Only | 0.1018 | 0.0955 | -5157.51 | 10341.02 |
| **Model 3** | Combined (HbA1c + CGM) | **0.1072** | **0.1002** | **-5000.63** | **10029.27** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 0.2046 | 0.2331 | 0.878 | 0.3802 | [-0.2526, 0.6619] |
| `mean_glucose` | -0.0257 | 0.0136 | -1.897 | 0.0580 | [-0.0524, 0.0009] |
| `glucose_sd` | 0.0071 | 0.0419 | 0.170 | 0.8647 | [-0.0750, 0.0892] |
| `mean_to_sd_ratio` | -0.0134 | 0.2041 | -0.066 | 0.9477 | [-0.4137, 0.3870] |
| `tir` | -0.0321 | 0.0201 | -1.598 | 0.1101 | [-0.0714, 0.0073] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 4.735$, $p = 0.3156$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 313.747$, $p = **3.3334e-70**$


### Target: High Depression Risk (CESD-10 >= 10) (N = 1688, Model = GLM)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | ROC-AUC | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.6806 | -728.34 | 1476.68 |
| **Model 2** | CGM Features Only | 0.6757 | -764.75 | 1555.49 |
| **Model 3** | Combined (HbA1c + CGM) | **0.6803** | **-727.73** | **1483.46** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Odds Ratio (OR) | Std Error | $z$-stat | $p$-value | 95% CI (OR) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 0.0950 | 1.0996 | 0.1217 | 0.780 | 0.4353 | [0.8662, 1.3960] |
| `mean_glucose` | -0.0043 | 0.9958 | 0.0078 | -0.544 | 0.5867 | [0.9806, 1.0111] |
| `glucose_sd` | -0.0039 | 0.9961 | 0.0234 | -0.168 | 0.8665 | [0.9515, 1.0428] |
| `mean_to_sd_ratio` | 0.0076 | 1.0076 | 0.1185 | 0.064 | 0.9489 | [0.7988, 1.2710] |
| `tir` | -0.0116 | 0.9884 | 0.0110 | -1.055 | 0.2913 | [0.9673, 1.0100] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 1.217$, $p = 0.8752$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 74.031$, $p = **7.6898e-18**$



---
## Domain: Environment

### Target: Mean Ambient Temperature (°C/F) (N = 1665, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0074 | 0.0020 | -30135.65 | 60291.31 |
| **Model 2** | CGM Features Only | 0.0074 | 0.0003 | -30874.63 | 61775.26 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0079** | **0.0001** | **-30135.24** | **60298.48** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -611479.2874 | 876897.7588 | -0.697 | 0.4857 | [-2331428.2087, 1108469.6338] |
| `mean_glucose` | 83.6561 | 51290.7618 | 0.002 | 0.9987 | [-100518.1410, 100685.4532] |
| `glucose_sd` | -66620.5526 | 157762.4025 | -0.422 | 0.6729 | [-376056.0271, 242814.9219] |
| `mean_to_sd_ratio` | -563162.1685 | 772515.2888 | -0.729 | 0.4661 | [-2078375.1159, 952050.7789] |
| `tir` | -15398.2002 | 75573.6714 | -0.204 | 0.8386 | [-163628.5422, 132832.1417] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 0.825$, $p = 0.9350$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 1478.782$, $p = **0.0000e+00**$


### Target: Mean Relative Humidity (%) (N = 1665, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0124 | 0.0070 | -5685.94 | 11391.88 |
| **Model 2** | CGM Features Only | 0.0164 | 0.0095 | -5827.50 | 11681.00 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0216** | **0.0139** | **-5678.10** | **11384.20** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 0.8976 | 0.3661 | 2.452 | **0.0143** ⭐ | [0.1796, 1.6157] |
| `mean_glucose` | 0.0255 | 0.0214 | 1.192 | 0.2335 | [-0.0165, 0.0675] |
| `glucose_sd` | 0.1128 | 0.0659 | 1.713 | 0.0869 | [-0.0164, 0.2420] |
| `mean_to_sd_ratio` | 0.6924 | 0.3225 | 2.147 | **0.0320** ⭐ | [0.0598, 1.3250] |
| `tir` | 0.1012 | 0.0316 | 3.206 | **0.0014** ⭐ | [0.0393, 0.1630] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 15.686$, $p = **3.4715e-03**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 298.802$, $p = **6.0081e-67**$


### Target: Mean Indoor PM2.5 (µg/m³) (N = 1665, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0453 | 0.0401 | -8273.82 | 16567.63 |
| **Model 2** | CGM Features Only | 0.0537 | 0.0470 | -8509.86 | 17045.73 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0522** | **0.0447** | **-8267.78** | **16563.56** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 3.2595 | 1.7342 | 1.880 | 0.0603 | [-0.1419, 6.6609] |
| `mean_glucose` | -0.2730 | 0.1014 | -2.691 | **0.0072** ⭐ | [-0.4720, -0.0741] |
| `glucose_sd` | 0.2023 | 0.3120 | 0.649 | 0.5167 | [-0.4096, 0.8143] |
| `mean_to_sd_ratio` | -0.3646 | 1.5278 | -0.239 | 0.8114 | [-3.3611, 2.6320] |
| `tir` | -0.2048 | 0.1495 | -1.370 | 0.1708 | [-0.4979, 0.0884] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 12.066$, $p = **1.6867e-02**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 484.162$, $p = **2.6551e-107**$


### Target: Mean Indoor PM10 (µg/m³) (N = 1665, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0444 | 0.0392 | -8335.24 | 16690.48 |
| **Model 2** | CGM Features Only | 0.0528 | 0.0460 | -8570.17 | 17166.34 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0511** | **0.0436** | **-8329.41** | **16686.82** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 3.2709 | 1.7996 | 1.818 | 0.0693 | [-0.2588, 6.8006] |
| `mean_glucose` | -0.2787 | 0.1053 | -2.648 | **0.0082** ⭐ | [-0.4852, -0.0723] |
| `glucose_sd` | 0.2181 | 0.3238 | 0.674 | 0.5006 | [-0.4169, 0.8532] |
| `mean_to_sd_ratio` | -0.3264 | 1.5854 | -0.206 | 0.8369 | [-3.4359, 2.7831] |
| `tir` | -0.2042 | 0.1551 | -1.317 | 0.1881 | [-0.5084, 0.1000] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 11.657$, $p = **2.0095e-02**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 481.521$, $p = **9.9695e-107**$


### Target: Mean Indoor VOC Index (N = 1665, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0160 | 0.0106 | -8656.29 | 17332.58 |
| **Model 2** | CGM Features Only | 0.0193 | 0.0124 | -8874.49 | 17774.99 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0174** | **0.0097** | **-8655.08** | **17338.15** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -0.7136 | 2.1883 | -0.326 | 0.7444 | [-5.0059, 3.5786] |
| `mean_glucose` | -0.1944 | 0.1280 | -1.519 | 0.1290 | [-0.4455, 0.0566] |
| `glucose_sd` | 0.3292 | 0.3937 | 0.836 | 0.4032 | [-0.4430, 1.1014] |
| `mean_to_sd_ratio` | 1.2856 | 1.9279 | 0.667 | 0.5050 | [-2.4957, 5.0669] |
| `tir` | -0.1406 | 0.1886 | -0.746 | 0.4560 | [-0.5105, 0.2293] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 2.427$, $p = 0.6578$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 438.838$, $p = **1.9380e-97**$


### Target: Mean Indoor NOx Index (N = 1665, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0059 | 0.0005 | -1910.64 | 3841.27 |
| **Model 2** | CGM Features Only | 0.0083 | 0.0012 | -1937.23 | 3900.46 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0084** | **0.0006** | **-1908.55** | **3845.11** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 0.0157 | 0.0381 | 0.414 | 0.6790 | [-0.0589, 0.0904] |
| `mean_glucose` | 0.0044 | 0.0022 | 1.976 | **0.0483** ⭐ | [0.0000, 0.0088] |
| `glucose_sd` | -0.0085 | 0.0068 | -1.236 | 0.2166 | [-0.0219, 0.0050] |
| `mean_to_sd_ratio` | -0.0439 | 0.0335 | -1.311 | 0.1900 | [-0.1097, 0.0218] |
| `tir` | 0.0035 | 0.0033 | 1.079 | 0.2807 | [-0.0029, 0.0100] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 4.167$, $p = 0.3839$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 57.356$, $p = **3.6362e-14**$



---
## Domain: Wearable Activity

### Target: Average Daily Steps (N = 257, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0366 | 0.0015 | -2432.94 | 4885.89 |
| **Model 2** | CGM Features Only | 0.0619 | 0.0177 | -2531.97 | 5089.94 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0633** | **0.0132** | **-2429.33** | **4886.67** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -26.2340 | 416.0563 | -0.063 | 0.9498 | [-845.7709, 793.3030] |
| `mean_glucose` | 41.3179 | 25.5018 | 1.620 | 0.1065 | [-8.9150, 91.5508] |
| `glucose_sd` | -193.0289 | 80.6966 | -2.392 | **0.0175** ⭐ | [-351.9830, -34.0748] |
| `mean_to_sd_ratio` | -830.9030 | 358.3031 | -2.319 | **0.0212** ⭐ | [-1536.6792, -125.1268] |
| `tir` | -25.7007 | 43.2232 | -0.595 | 0.5527 | [-110.8407, 59.4394] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 7.217$, $p = 0.1248$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 205.268$, $p = **1.4800e-46**$


### Target: Average Daily Active Calories (N = 1485, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0554 | 0.0496 | -21200.48 | 42420.97 |
| **Model 2** | CGM Features Only | 0.0510 | 0.0434 | -21815.56 | 43657.12 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0569** | **0.0485** | **-21199.29** | **42426.58** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 52649.0834 | 20123.1322 | 2.616 | **0.0090** ⭐ | [13175.9903, 92122.1766] |
| `mean_glucose` | 1333.3575 | 1189.7394 | 1.121 | 0.2626 | [-1000.4091, 3667.1242] |
| `glucose_sd` | -4675.9852 | 3748.1888 | -1.248 | 0.2124 | [-12028.3498, 2676.3795] |
| `mean_to_sd_ratio` | -16474.1932 | 17971.4703 | -0.917 | 0.3595 | [-51726.6336, 18778.2473] |
| `tir` | -273.0412 | 1765.9685 | -0.155 | 0.8771 | [-3737.1262, 3191.0437] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 2.384$, $p = 0.6655$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 1232.541$, $p = **5.1684e-270**$


### Target: Average Stress Level (N = 1576, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0727 | 0.0674 | -6353.56 | 12727.12 |
| **Model 2** | CGM Features Only | 0.0794 | 0.0725 | -6524.63 | 13075.25 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0806** | **0.0730** | **-6346.78** | **12721.56** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | 1.0023 | 0.6900 | 1.453 | 0.1465 | [-0.3511, 2.3556] |
| `mean_glucose` | 0.1058 | 0.0408 | 2.591 | **0.0097** ⭐ | [0.0257, 0.1859] |
| `glucose_sd` | -0.3112 | 0.1259 | -2.472 | **0.0136** ⭐ | [-0.5582, -0.0642] |
| `mean_to_sd_ratio` | -1.6115 | 0.6117 | -2.635 | **0.0085** ⭐ | [-2.8112, -0.4117] |
| `tir` | -0.0157 | 0.0606 | -0.259 | 0.7958 | [-0.1347, 0.1033] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 13.551$, $p = **8.8741e-03**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 355.690$, $p = **2.4440e-79**$


### Target: Average Heart Rate (bpm) (N = 1572, Model = OLS)

#### 1. Model Fit & Goodness of Fit Comparison
| Specification | Predictors | $R^2$ | Adj $R^2$ | Log-Likelihood | AIC |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Model 1** | HbA1c Only | 0.0235 | 0.0179 | -6860.74 | 13741.49 |
| **Model 2** | CGM Features Only | 0.0312 | 0.0239 | -7028.23 | 14082.47 |
| **Model 3** | Combined (HbA1c + CGM) | **0.0300** | **0.0219** | **-6855.54** | **13739.08** |

#### 2. Regression Slopes & Significance (Model 3 - Combined)
| Predictor | Slope ($\beta$) | Std Error | $t$-statistic | $p$-value | 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `hba1c` | -0.8403 | 0.9641 | -0.872 | 0.3836 | [-2.7313, 1.0507] |
| `mean_glucose` | 0.0891 | 0.0571 | 1.562 | 0.1185 | [-0.0228, 0.2010] |
| `glucose_sd` | -0.4285 | 0.1762 | -2.432 | **0.0151** ⭐ | [-0.7740, -0.0829] |
| `mean_to_sd_ratio` | -1.9104 | 0.8576 | -2.228 | **0.0260** ⭐ | [-3.5925, -0.2282] |
| `tir` | -0.1067 | 0.0847 | -1.261 | 0.2077 | [-0.2729, 0.0594] |

#### 3. Redundancy & Incremental Value Tests
- **Incremental Value of CGM Features over HbA1c Alone (Model 3 vs. Model 1)**: LRT $\chi^2(4) = 10.412$, $p = **3.4033e-02**$
- **Incremental Value of HbA1c over CGM Features Alone (Model 3 vs. Model 2)**: LRT $\chi^2(1) = 345.392$, $p = **4.2718e-77**$

