# Phase 6b - Single-predictor tables inside the actual-value glucose cohorts

Cohorts are defined by each participant's own CGM readings over the wear period; inside every cohort the full Phase 6 predictor set (HbA1c, CGM level and variability, time in range 70-180, and the glucose bands) is entered one measure at a time with the Phase 5 covariates, in the total, healthy (no diabetes + pre-diabetes) and non-healthy (T2D oral + insulin) populations.

**Table layout.** Per outcome: (A) model output on the raw scale, one row per single-predictor model (coefficient, HC3 SE, 95% CI, t/z, p, stars); (B) effect per 1 SD, BH q (rule and informational), adjusted R²/AUC, AIC differences, CV. Complete term-by-term output for every model is in `model_output_tables/phase6b/<cohort>/<population>/<domain>.md` (index: `model_output_tables/README.md`) and `phase6b_model_outputs.csv`.

## Cohort sizes and feasibility

| Cohort | Definition | N | Healthy | Non-healthy | MoCA | MoCA<26 events | CES-D>=10 events | Environment | Steps | Resting HR | Sleep | Feasible? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| normal_70_180 | Normal range only: every reading within 70-180 | 39 | 30 | 9 | 39 | 10 | 6 | 37 | 35 | 36 | 34 | no - fewer than 100 participants |
| near_normal_99 | Near-normal substitute: >= 99% of readings within 70-180 | 454 | 393 | 61 | 454 | 148 | 82 | 443 | 401 | 403 | 409 | yes |
| within_54_250 | Within 54-250: no reading < 54 and none > 250 | 890 | 685 | 205 | 890 | 336 | 155 | 872 | 771 | 774 | 779 | yes |
| hypo_below_54 | Hypoglycaemia exposure: at least one reading < 54 | 638 | 408 | 230 | 638 | 228 | 137 | 628 | 575 | 576 | 588 | yes |
| hyper_above_250 | Hyperglycaemia exposure: at least one reading > 250 | 795 | 244 | 551 | 795 | 371 | 165 | 783 | 690 | 692 | 694 | yes |

Overlap of the exposure cohorts (total): hypoglycaemia only 453, hyperglycaemia only 610, both 185, neither (within 54-250) 890.

**FDR.** The Phase 6 rule (BH only when the test's sample has n >= 500) is applied test by test: it is met in the total population of the within-54-250, hypoglycaemia and hyperglycaemia cohorts, in the healthy stratum of the within-54-250 cohort and in part of the non-healthy hyperglycaemia stratum; elsewhere the rule column reads 'not applied' and an informational BH q over all tests in that population is shown alongside. Bold in table (A) = raw p < 0.05; bold in table (B) = q < 0.05.

## Significance counts

| Cohort | Population | Tests | n min | n max | Raw p < 0.05 | Informational q < 0.05 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Hyperglycaemia exposure: at least one reading > 250 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 420 | 215 | 244 | 49 | 10 |
| Hyperglycaemia exposure: at least one reading > 250 | Non-healthy group (T2D non-insulin + T2D insulin) | 420 | 472 | 551 | 70 | 4 |
| Hyperglycaemia exposure: at least one reading > 250 | Total analysis base | 420 | 690 | 795 | 117 | 50 |
| Hypoglycaemia exposure: at least one reading < 54 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 420 | 373 | 408 | 31 | 0 |
| Hypoglycaemia exposure: at least one reading < 54 | Non-healthy group (T2D non-insulin + T2D insulin) | 420 | 201 | 230 | 81 | 10 |
| Hypoglycaemia exposure: at least one reading < 54 | Total analysis base | 420 | 575 | 638 | 144 | 66 |
| Near-normal substitute: >= 99% of readings within 70-180 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 392 | 344 | 393 | 26 | 0 |
| Near-normal substitute: >= 99% of readings within 70-180 | Non-healthy group (T2D non-insulin + T2D insulin) | 96 | 60 | 61 | 0 | 0 |
| Near-normal substitute: >= 99% of readings within 70-180 | Total analysis base | 392 | 401 | 454 | 26 | 0 |
| Within 54-250: no reading < 54 and none > 250 | Healthy group (no diabetes + pre-diabetes / lifestyle) | 322 | 593 | 685 | 38 | 10 |
| Within 54-250: no reading < 54 and none > 250 | Non-healthy group (T2D non-insulin + T2D insulin) | 322 | 177 | 205 | 30 | 0 |
| Within 54-250: no reading < 54 and none > 250 | Total analysis base | 322 | 771 | 890 | 73 | 22 |

## Per-cohort table files (one file per cohort so that each renders in GitHub / VS Code)

- Normal range only: every reading within 70-180: **not analysed** (only 39 participants, fewer than 100)
- [Near-normal substitute: >= 99% of readings within 70-180](research_report_05_cohort_near_normal_99.md) (N = 454)
- [Within 54-250: no reading < 54 and none > 250](research_report_05_cohort_within_54_250.md) (N = 890)
- [Hypoglycaemia exposure: at least one reading < 54](research_report_05_cohort_hypo_below_54.md) (N = 638)
- [Hyperglycaemia exposure: at least one reading > 250](research_report_05_cohort_hyper_above_250.md) (N = 795)

---

# Interpretation across cohorts (total population of each cohort)


## Interpretation - Near-normal substitute: >= 99% of readings within 70-180 - total population

**Scope.** 392 single-predictor tests; 26 with raw p < 0.05 (about 20 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 454): best single predictor out of sample is **GMI** (CV R² 0.070 vs 0.063 for covariates alone, gain +0.006; -0.222 per SD, p = 0.086). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Cognitive impairment (MoCA < 26)** (n = 454): best single predictor out of sample is **%54-69 (daily avg)** (CV AUC 0.643 vs 0.638 for covariates alone, gain +0.005; OR 0.82 per SD, p = 0.085). No glycaemic measure is associated with this outcome (all p > 0.05).
- **MoCA memory index score (0-15)** (n = 454): best single predictor out of sample is **SD of daily means** (CV R² 0.037 vs 0.029 for covariates alone, gain +0.008; -0.337 per SD, p = 0.007). Raw p < 0.05 (FDR not applicable here): SD of daily means (p = 0.007).
- **CES-D-10 depressive symptoms (0-30)** (n = 454): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.017 vs -0.001 for covariates alone, gain +0.018; +0.661 per SD, p = 0.019). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.005), %>180 nocturnal (p = 0.019), %54-250 (pooled) (p = 0.030), %<54 (pooled) (p = 0.031).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 454): best single predictor out of sample is **MAG** (CV AUC 0.644 vs 0.607 for covariates alone, gain +0.037; OR 1.53 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.001).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 443): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.079 vs 0.075 for covariates alone, gain +0.004; -0.0811 per SD, p = 0.076). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor temperature, mean (deg C)** (n = 443): best single predictor out of sample is **Daily range** (CV R² 0.300 vs 0.292 for covariates alone, gain +0.008; -0.239 per SD, p = 0.012). Raw p < 0.05 (FDR not applicable here): Daily range (p = 0.012).
- **Indoor relative humidity, mean (%)** (n = 443): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.223 vs 0.220 for covariates alone, gain +0.003; -0.39 per SD, p = 0.194). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor VOC index, mean** (n = 443): best single predictor out of sample is **%<54 (daily avg)** (CV R² -0.028 vs -0.037 for covariates alone, gain +0.009; +1.12 per SD, p = 0.061). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.043).
- **Steps per wear-day** (n = 401): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.079 vs 0.079 for covariates alone, gain -0.001; +309 per SD, p = 0.097). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 401): best single predictor out of sample is **TIR 70-180 (pooled)** (CV R² 0.109 vs 0.100 for covariates alone, gain +0.009; -1.63 per SD, p = 0.004). Raw p < 0.05 (FDR not applicable here): TIR 70-180 (pooled) (p = 0.004), TIR 70-180 (daily avg) (p = 0.006), %>180 (daily avg) (p = 0.021), %181-250 (daily avg) (p = 0.022), %>180 (pooled) (p = 0.041).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 403): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.138 vs 0.133 for covariates alone, gain +0.006; +0.717 per SD, p = 0.011). Raw p < 0.05 (FDR not applicable here): %<54 (pooled) (p = 0.011), %54-250 (pooled) (p = 0.016).
- **Total sleep time per night (min)** (n = 409): best single predictor out of sample is **HbA1c** (CV R² 0.028 vs 0.002 for covariates alone, gain +0.027; -10.5 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): HbA1c (p = 0.001), %54-69 (pooled) (p = 0.004), %<70 (daily avg) (p = 0.007), %54-69 (daily avg) (p = 0.007), %<70 (pooled) (p = 0.007).
- **Garmin stress score, mean (0-100)** (n = 403): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.068 vs 0.056 for covariates alone, gain +0.012; +1.93 per SD, p = 0.039). Raw p < 0.05 (FDR not applicable here): %>180 nocturnal (p = 0.039).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.037, via MAG); Total sleep time per night (min) (+0.027, via HbA1c); CES-D-10 depressive symptoms (0-30) (+0.018, via %>180 nocturnal); Garmin stress score, mean (0-100) (+0.012, via %>180 nocturnal). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 6 raw-significant of 112); Band > 180 (0 FDR-significant / 4 raw-significant of 42); CGM level (0 FDR-significant / 3 raw-significant of 42).
Level metrics: 0 FDR-significant (3 raw); variability metrics: 0 FDR-significant (6 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (SD of daily means, ΔAIC -4.8); Cognitive impairment (%<70 (daily avg), ΔAIC -3.1); MoCA memory index score (SD of daily means, ΔAIC -7.8); CES-D-10 depressive symptoms (%>180 nocturnal, ΔAIC -9.2); Clinically relevant depressive symptoms (MAG, ΔAIC -10.9); Indoor PM2.5, log(1 + mean ug/m3) (%<54 (daily avg), ΔAIC -4.1); Indoor temperature, mean (Daily range, ΔAIC -6.7); Indoor VOC index, mean (MAG, ΔAIC -3.9); Steps per wear-day (%>180 nocturnal, ΔAIC -5.8); Brisk-cadence minutes per day (TIR 70-180 (pooled), ΔAIC -7.5); Resting heart-rate proxy (%<54 (pooled), ΔAIC -4.2); Garmin stress score, mean (%>180 nocturnal, ΔAIC -5.4).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - Within 54-250: no reading < 54 and none > 250 - total population

**Scope.** 322 single-predictor tests; 73 with raw p < 0.05 (about 16 expected by chance); FDR rule applied to 322 tests (samples with n >= 500), of which **22** are significant at BH q < 0.05 in the all-tests family and 34 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 890): best single predictor out of sample is **GMI** (CV R² 0.094 vs 0.079 for covariates alone, gain +0.015; -0.378 per SD, p = 3.1e-04, q = 0.011). FDR-robust associations (3): Mean glucose (lower outcome, -0.378 per SD, q = 0.011); GMI (lower outcome, -0.378 per SD, q = 0.011); Nocturnal mean (lower outcome, -0.368 per SD, q = 0.013).
- **Cognitive impairment (MoCA < 26)** (n = 890): best single predictor out of sample is **Nocturnal mean** (CV AUC 0.668 vs 0.656 for covariates alone, gain +0.012; OR 1.33 per SD, p = 2.1e-04, q = 0.011). FDR-robust associations (3): Nocturnal mean (higher outcome, OR 1.33 per SD, q = 0.011); GMI (higher outcome, OR 1.31 per SD, q = 0.011); Mean glucose (higher outcome, OR 1.31 per SD, q = 0.011).
- **MoCA memory index score (0-15)** (n = 890): best single predictor out of sample is **Nocturnal mean** (CV R² 0.039 vs 0.033 for covariates alone, gain +0.006; -0.259 per SD, p = 0.016, q = 0.148). No association survives FDR; nominal only: Nocturnal mean (p = 0.016).
- **CES-D-10 depressive symptoms (0-30)** (n = 889): best single predictor out of sample is **GMI** (CV R² 0.050 vs 0.049 for covariates alone, gain +0.001; -0.167 per SD, p = 0.300, q = 0.630). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 889): best single predictor out of sample is **Nocturnal mean** (CV AUC 0.651 vs 0.643 for covariates alone, gain +0.008; OR 1.20 per SD, p = 0.041, q = 0.199). No association survives FDR; nominal only: %>180 nocturnal (p = 0.023), Nocturnal mean (p = 0.041).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 872): best single predictor out of sample is **SD of daily means** (CV R² 0.115 vs 0.115 for covariates alone, gain -0.000; +0.0339 per SD, p = 0.272, q = 0.604). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 872): best single predictor out of sample is **SD of daily means** (CV R² 0.301 vs 0.301 for covariates alone, gain -0.000; -0.0598 per SD, p = 0.404, q = 0.731). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 872): best single predictor out of sample is **SD (pooled)** (CV R² 0.242 vs 0.236 for covariates alone, gain +0.006; +0.587 per SD, p = 0.003, q = 0.048). FDR-robust associations (1): SD (pooled) (higher outcome, +0.587 per SD, q = 0.048).
- **Indoor VOC index, mean** (n = 872): best single predictor out of sample is **SD (pooled)** (CV R² 0.016 vs 0.015 for covariates alone, gain +0.002; -0.805 per SD, p = 0.168, q = 0.484). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 771): best single predictor out of sample is **MAG** (CV R² 0.097 vs 0.080 for covariates alone, gain +0.016; +557 per SD, p = 1.7e-04, q = 0.011). FDR-robust associations (1): MAG (higher outcome, +557 per SD, q = 0.011).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 771): best single predictor out of sample is **MAG** (CV R² 0.131 vs 0.111 for covariates alone, gain +0.020; +1.85 per SD, p = 2.0e-05, q = 0.002). FDR-robust associations (1): MAG (higher outcome, +1.85 per SD, q = 0.002).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 774): best single predictor out of sample is **GMI** (CV R² 0.171 vs 0.153 for covariates alone, gain +0.018; +1.16 per SD, p = 2.1e-05, q = 0.002). FDR-robust associations (10): Mean glucose (higher outcome, +1.16 per SD, q = 0.002); GMI (higher outcome, +1.16 per SD, q = 0.002); Nocturnal mean (higher outcome, +1.15 per SD, q = 0.002); %181-250 (daily avg) (higher outcome, +0.926 per SD, q = 0.021); %>180 (daily avg) (higher outcome, +0.926 per SD, q = 0.021); HbA1c (higher outcome, +1.02 per SD, q = 0.024); ....
- **Total sleep time per night (min)** (n = 779): best single predictor out of sample is **MAG** (CV R² 0.015 vs 0.010 for covariates alone, gain +0.006; -7.09 per SD, p = 0.015, q = 0.148). No association survives FDR; nominal only: HbA1c (p = 0.006), MAG (p = 0.015), Nocturnal mean (p = 0.035).
- **Garmin stress score, mean (0-100)** (n = 775): best single predictor out of sample is **Mean glucose** (CV R² 0.116 vs 0.107 for covariates alone, gain +0.008; +1.88 per SD, p = 0.003, q = 0.046). FDR-robust associations (3): Nocturnal mean (higher outcome, +1.94 per SD, q = 0.040); Mean glucose (higher outcome, +1.88 per SD, q = 0.046); GMI (higher outcome, +1.88 per SD, q = 0.046).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Brisk-cadence minutes per day (>= 100 steps/min) (+0.020, via MAG); Resting heart-rate proxy (daily 5th pct, bpm) (+0.018, via GMI); Steps per wear-day (+0.016, via MAG); MoCA total score (0-30) (+0.015, via GMI). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM level (12 FDR-significant / 15 raw-significant of 42); CGM variability (4 FDR-significant / 17 raw-significant of 112); Band > 180 (2 FDR-significant / 11 raw-significant of 42).
Level metrics: 12 FDR-significant (15 raw); variability metrics: 4 FDR-significant (17 raw); HbA1c alone: 1 FDR-significant (7 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (GMI, ΔAIC -8.1); Cognitive impairment (Nocturnal mean, ΔAIC -9.6); MoCA memory index score (Nocturnal mean, ΔAIC -8.7); Clinically relevant depressive symptoms (%>180 nocturnal, ΔAIC -5.0); Indoor relative humidity, mean (SD (pooled), ΔAIC -7.8); Indoor VOC index, mean (SD (pooled), ΔAIC -2.0); Steps per wear-day (MAG, ΔAIC -9.6); Brisk-cadence minutes per day (MAG, ΔAIC -11.7); Resting heart-rate proxy (Mean glucose, ΔAIC -5.0); Garmin stress score, mean (Nocturnal mean, ΔAIC -4.1).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - Hypoglycaemia exposure: at least one reading < 54 - total population

**Scope.** 420 single-predictor tests; 144 with raw p < 0.05 (about 21 expected by chance); FDR rule applied to 420 tests (samples with n >= 500), of which **66** are significant at BH q < 0.05 in the all-tests family and 102 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 638): best single predictor out of sample is **HbA1c** (CV R² 0.091 vs 0.067 for covariates alone, gain +0.024; -0.523 per SD, p = 1.7e-05, q = 0.002). FDR-robust associations (19): HbA1c (lower outcome, -0.523 per SD, q = 0.002); TIR 70-180 (pooled) (higher outcome, +0.475 per SD, q = 0.010); TIR 70-180 (daily avg) (higher outcome, +0.466 per SD, q = 0.013); Mean glucose (lower outcome, -0.435 per SD, q = 0.017); GMI (lower outcome, -0.435 per SD, q = 0.017); SD (pooled) (lower outcome, -0.442 per SD, q = 0.017); ....
- **Cognitive impairment (MoCA < 26)** (n = 638): best single predictor out of sample is **HbA1c** (CV AUC 0.663 vs 0.641 for covariates alone, gain +0.021; OR 1.43 per SD, p = 2.7e-04, q = 0.008). FDR-robust associations (4): HbA1c (higher outcome, OR 1.43 per SD, q = 0.008); TIR 70-180 (pooled) (lower outcome, OR 0.75 per SD, q = 0.026); TIR 70-180 (daily avg) (lower outcome, OR 0.76 per SD, q = 0.028); SD (pooled) (higher outcome, OR 1.30 per SD, q = 0.037).
- **MoCA memory index score (0-15)** (n = 638): best single predictor out of sample is **HbA1c** (CV R² 0.053 vs 0.043 for covariates alone, gain +0.010; -0.288 per SD, p = 0.005, q = 0.038). FDR-robust associations (1): HbA1c (lower outcome, -0.288 per SD, q = 0.038).
- **CES-D-10 depressive symptoms (0-30)** (n = 637): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.102 vs 0.083 for covariates alone, gain +0.019; +0.744 per SD, p = 4.2e-05, q = 0.003). FDR-robust associations (11): %>250 (pooled) (higher outcome, +0.638 per SD, q = 0.001); %54-250 (pooled) (lower outcome, -0.611 per SD, q = 0.001); %>180 nocturnal (higher outcome, +0.744 per SD, q = 0.003); %54-250 (daily avg) (lower outcome, -0.614 per SD, q = 0.008); %>250 (daily avg) (higher outcome, +0.63 per SD, q = 0.008); TIR 70-180 (daily avg) (lower outcome, -0.57 per SD, q = 0.028); ....
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 637): best single predictor out of sample is **%>180 nocturnal** (CV AUC 0.685 vs 0.659 for covariates alone, gain +0.027; OR 1.54 per SD, p = 1.0e-05, q = 0.001). FDR-robust associations (19): %>180 nocturnal (higher outcome, OR 1.54 per SD, q = 0.001); Nocturnal mean (higher outcome, OR 1.44 per SD, q = 0.008); SD of daily means (higher outcome, OR 1.43 per SD, q = 0.008); TIR 70-180 (daily avg) (lower outcome, OR 0.71 per SD, q = 0.008); %>180 (daily avg) (higher outcome, OR 1.40 per SD, q = 0.008); TIR 70-180 (pooled) (lower outcome, OR 0.71 per SD, q = 0.008); ....
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 628): best single predictor out of sample is **HbA1c** (CV R² 0.120 vs 0.114 for covariates alone, gain +0.006; +0.108 per SD, p = 0.024, q = 0.093). No association survives FDR; nominal only: HbA1c (p = 0.024).
- **Indoor temperature, mean (deg C)** (n = 628): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.239 vs 0.233 for covariates alone, gain +0.006; +0.182 per SD, p = 0.020, q = 0.087). No association survives FDR; nominal only: %<70 (pooled) (p = 0.020), %54-69 (daily avg) (p = 0.020), %<70 (daily avg) (p = 0.020), %<54 (pooled) (p = 0.023).
- **Indoor relative humidity, mean (%)** (n = 628): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.193 vs 0.190 for covariates alone, gain +0.003; -0.462 per SD, p = 0.040, q = 0.125). No association survives FDR; nominal only: %<54 (pooled) (p = 0.036), %<54 (daily avg) (p = 0.040).
- **Indoor VOC index, mean** (n = 628): best single predictor out of sample is **MAG** (CV R² 0.011 vs 0.011 for covariates alone, gain +0.000; +0.963 per SD, p = 0.224, q = 0.432). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Steps per wear-day** (n = 575): best single predictor out of sample is **HbA1c** (CV R² 0.126 vs 0.124 for covariates alone, gain +0.001; +312 per SD, p = 0.217, q = 0.425). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 575): best single predictor out of sample is **HbA1c** (CV R² 0.147 vs 0.141 for covariates alone, gain +0.006; +1.24 per SD, p = 0.096, q = 0.233). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 576): best single predictor out of sample is **Mean/SD** (CV R² 0.155 vs 0.144 for covariates alone, gain +0.010; -1.07 per SD, p = 0.001, q = 0.023). FDR-robust associations (5): Mean/SD (lower outcome, -1.07 per SD, q = 0.023); %181-250 (pooled) (higher outcome, +1.19 per SD, q = 0.028); SD of daily means (higher outcome, +0.979 per SD, q = 0.029); Mean/SD (daily avg) (lower outcome, -0.962 per SD, q = 0.032); %181-250 (daily avg) (higher outcome, +1.11 per SD, q = 0.042).
- **Total sleep time per night (min)** (n = 588): best single predictor out of sample is **MAG** (CV R² 0.004 vs -0.017 for covariates alone, gain +0.021; -12.1 per SD, p = 2.3e-05, q = 0.002). FDR-robust associations (4): MAG (lower outcome, -12.1 per SD, q = 0.002); HbA1c (lower outcome, -8.46 per SD, q = 0.023); %54-250 (daily avg) (higher outcome, +7.03 per SD, q = 0.036); %>250 (daily avg) (lower outcome, -7.14 per SD, q = 0.036).
- **Garmin stress score, mean (0-100)** (n = 577): best single predictor out of sample is **HbA1c** (CV R² 0.095 vs 0.086 for covariates alone, gain +0.009; +2.28 per SD, p = 0.014, q = 0.071). FDR-robust associations (3): Mean/SD (lower outcome, -2.11 per SD, q = 0.029); SD of daily means (higher outcome, +1.87 per SD, q = 0.047); %181-250 (pooled) (higher outcome, +2.17 per SD, q = 0.047).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.027, via %>180 nocturnal); MoCA total score (0-30) (+0.024, via HbA1c); Cognitive impairment (MoCA < 26) (+0.021, via HbA1c); Total sleep time per night (min) (+0.021, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (16 FDR-significant / 40 raw-significant of 112); Band > 180 (9 FDR-significant / 19 raw-significant of 42); Range 70-180 (8 FDR-significant / 15 raw-significant of 28).
Level metrics: 6 FDR-significant (17 raw); variability metrics: 16 FDR-significant (40 raw); HbA1c alone: 5 FDR-significant (8 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (%>180 nocturnal, ΔAIC -11.9); Clinically relevant depressive symptoms (%>180 nocturnal, ΔAIC -14.4); Indoor temperature, mean (%<70 (daily avg), ΔAIC -4.8); Indoor VOC index, mean (%>250 (daily avg), ΔAIC -5.3); Total sleep time per night (MAG, ΔAIC -10.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._


## Interpretation - Hyperglycaemia exposure: at least one reading > 250 - total population

**Scope.** 420 single-predictor tests; 117 with raw p < 0.05 (about 21 expected by chance); FDR rule applied to 420 tests (samples with n >= 500), of which **50** are significant at BH q < 0.05 in the all-tests family and 71 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 795): best single predictor out of sample is **SD (pooled)** (CV R² 0.055 vs 0.047 for covariates alone, gain +0.007; -0.36 per SD, p = 0.004, q = 0.041). FDR-robust associations (5): SD (pooled) (lower outcome, -0.36 per SD, q = 0.041); GMI (lower outcome, -0.365 per SD, q = 0.045); Mean glucose (lower outcome, -0.365 per SD, q = 0.045); %>180 (pooled) (lower outcome, -0.362 per SD, q = 0.046); TIR 70-180 (pooled) (higher outcome, +0.36 per SD, q = 0.046).
- **Cognitive impairment (MoCA < 26)** (n = 795): best single predictor out of sample is **SD (pooled)** (CV AUC 0.626 vs 0.621 for covariates alone, gain +0.005; OR 1.24 per SD, p = 0.008, q = 0.056). FDR-robust associations (3): TIR 70-180 (pooled) (lower outcome, OR 0.80 per SD, q = 0.046); %>180 (pooled) (higher outcome, OR 1.24 per SD, q = 0.046); TIR 70-180 (daily avg) (lower outcome, OR 0.80 per SD, q = 0.046).
- **MoCA memory index score (0-15)** (n = 795): best single predictor out of sample is **Nocturnal mean** (CV R² 0.040 vs 0.035 for covariates alone, gain +0.005; -0.214 per SD, p = 0.026, q = 0.115). No association survives FDR; nominal only: SD (pooled) (p = 0.017), SD (daily avg) (p = 0.018), Nocturnal mean (p = 0.026), GMI (p = 0.043).
- **CES-D-10 depressive symptoms (0-30)** (n = 793): best single predictor out of sample is **SD of daily means** (CV R² 0.115 vs 0.105 for covariates alone, gain +0.010; +0.552 per SD, p = 0.003, q = 0.034). FDR-robust associations (1): SD of daily means (higher outcome, +0.552 per SD, q = 0.034).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 793): best single predictor out of sample is **SD of daily means** (CV AUC 0.704 vs 0.685 for covariates alone, gain +0.019; OR 1.36 per SD, p = 4.7e-04, q = 0.007). FDR-robust associations (1): SD of daily means (higher outcome, OR 1.36 per SD, q = 0.007).
- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 783): best single predictor out of sample is **HbA1c** (CV R² 0.164 vs 0.152 for covariates alone, gain +0.012; +0.122 per SD, p = 0.004, q = 0.044). FDR-robust associations (2): SD of daily means (higher outcome, +0.119 per SD, q = 0.017); HbA1c (higher outcome, +0.122 per SD, q = 0.044).
- **Indoor temperature, mean (deg C)** (n = 783): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.281 vs 0.279 for covariates alone, gain +0.001; +0.128 per SD, p = 0.220, q = 0.482). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 783): best single predictor out of sample is **MAG** (CV R² 0.212 vs 0.213 for covariates alone, gain -0.001; +0.125 per SD, p = 0.564, q = 0.741). No association survives FDR; nominal only: %<54 (pooled) (p = 0.044). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 783): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.030 vs 0.024 for covariates alone, gain +0.005; +1.78 per SD, p = 0.010, q = 0.063). No association survives FDR; nominal only: HbA1c (p = 0.010), %54-250 (daily avg) (p = 0.010), %>250 (daily avg) (p = 0.011), %54-250 (pooled) (p = 0.011).
- **Steps per wear-day** (n = 690): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.131 vs 0.128 for covariates alone, gain +0.003; -362 per SD, p = 0.006, q = 0.050). No association survives FDR; nominal only: %<70 (daily avg) (p = 0.006), %<70 (pooled) (p = 0.014), %54-69 (daily avg) (p = 0.026), %54-69 (pooled) (p = 0.040).
- **Brisk-cadence minutes per day (>= 100 steps/min)** (n = 690): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.150 vs 0.148 for covariates alone, gain +0.003; -0.983 per SD, p = 0.017, q = 0.087). No association survives FDR; nominal only: %<70 (daily avg) (p = 0.017), %<70 (pooled) (p = 0.032), %54-69 (daily avg) (p = 0.040).
- **Resting heart-rate proxy (daily 5th pct, bpm)** (n = 692): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.150 vs 0.111 for covariates alone, gain +0.039; +1.88 per SD, p = 4.2e-08, q = 8.8e-06). FDR-robust associations (19): %181-250 (pooled) (higher outcome, +1.88 per SD, q = 8.8e-06); %181-250 (daily avg) (higher outcome, +1.84 per SD, q = 9.1e-06); %>180 (pooled) (higher outcome, +1.89 per SD, q = 9.1e-06); TIR 70-180 (pooled) (lower outcome, -1.9 per SD, q = 9.1e-06); HbA1c (higher outcome, +1.73 per SD, q = 9.1e-06); %>180 (daily avg) (higher outcome, +1.88 per SD, q = 9.1e-06); ....
- **Total sleep time per night (min)** (n = 694): best single predictor out of sample is **MAG** (CV R² 0.014 vs -0.005 for covariates alone, gain +0.019; -10 per SD, p = 7.5e-05, q = 0.001). FDR-robust associations (1): MAG (lower outcome, -10 per SD, q = 0.001).
- **Garmin stress score, mean (0-100)** (n = 692): best single predictor out of sample is **HbA1c** (CV R² 0.111 vs 0.069 for covariates alone, gain +0.042; +3.98 per SD, p = 2.3e-09, q = 9.5e-07). FDR-robust associations (18): HbA1c (higher outcome, +3.98 per SD, q = 9.5e-07); TIR 70-180 (pooled) (lower outcome, -3.81 per SD, q = 1.4e-05); %>180 (pooled) (higher outcome, +3.8 per SD, q = 1.4e-05); %>180 (daily avg) (higher outcome, +3.75 per SD, q = 1.7e-05); TIR 70-180 (daily avg) (lower outcome, -3.75 per SD, q = 1.7e-05); %181-250 (pooled) (higher outcome, +3.54 per SD, q = 1.7e-05); ....

**Most predictable outcomes (largest out-of-sample gain over covariates):** Garmin stress score, mean (0-100) (+0.042, via HbA1c); Resting heart-rate proxy (daily 5th pct, bpm) (+0.039, via %181-250 (pooled)); Total sleep time per night (min) (+0.019, via MAG); Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.019, via SD of daily means). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (12 FDR-significant / 29 raw-significant of 112); CGM level (8 FDR-significant / 19 raw-significant of 42); Band > 180 (8 FDR-significant / 16 raw-significant of 42).
Level metrics: 8 FDR-significant (19 raw); variability metrics: 12 FDR-significant (29 raw); HbA1c alone: 3 FDR-significant (7 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (Mean glucose, ΔAIC -3.0); Cognitive impairment (TIR 70-180 (pooled), ΔAIC -3.1); MoCA memory index score (SD (pooled), ΔAIC -2.0); CES-D-10 depressive symptoms (SD of daily means, ΔAIC -7.6); Clinically relevant depressive symptoms (SD of daily means, ΔAIC -9.4); Indoor temperature, mean (%<54 (pooled), ΔAIC -2.5); Resting heart-rate proxy (%181-250 (pooled), ΔAIC -6.4); Total sleep time per night (MAG, ΔAIC -9.8).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
