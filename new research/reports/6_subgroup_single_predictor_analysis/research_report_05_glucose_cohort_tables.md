# Phase 6b - Single-predictor tables inside the actual-value glucose cohorts

Cohorts are defined by each participant's own CGM readings over the wear period; inside every cohort the full Phase 6 predictor set (HbA1c, CGM level and variability, time in range 70-180, and the glucose bands) is entered one measure at a time with the Phase 5 covariates, in the total, healthy (no diabetes + pre-diabetes) and non-healthy (T2D oral + insulin) populations.

**Table layout.** Per outcome: (A) model output on the raw scale, one row per single-predictor model (coefficient, HC3 SE, 95% CI, t/z, p, stars); (B) effect per 1 SD, BH q (rule and informational), adjusted R²/AUC, AIC differences, CV. Complete term-by-term output for every model is in `model_output_tables/phase6b_<cohort>_<population>.md` and `phase6b_model_outputs.csv`.

## Cohort sizes and feasibility

| Cohort | Definition | N | Healthy | Non-healthy | MoCA | MoCA<26 events | CES-D>=10 events | Environment | Steps | Resting HR | Sleep | Feasible? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| normal_70_180 | Normal range only: every reading within 70-180 | 39 | 30 | 9 | 39 | 10 | 6 | 37 | 35 | 36 | 34 | no - fewer than 100 participants |
| near_normal_99 | Near-normal substitute: >= 99% of readings within 70-180 | 454 | 393 | 61 | 454 | 148 | 82 | 443 | 401 | 403 | 409 | yes |
| within_54_250 | Within 54-250: no reading < 54 and none > 250 | 890 | 685 | 205 | 890 | 336 | 155 | 872 | 771 | 774 | 779 | yes |
| hypo_below_54 | Hypoglycaemia exposure: at least one reading < 54 | 638 | 408 | 230 | 638 | 228 | 137 | 628 | 575 | 576 | 588 | yes |
| hyper_above_250 | Hyperglycaemia exposure: at least one reading > 250 | 795 | 244 | 551 | 795 | 371 | 165 | 783 | 690 | 692 | 694 | yes |

Overlap of the exposure cohorts (total): hypoglycaemia only 453, hyperglycaemia only 610, both 185, neither (within 54-250) 890.

**FDR.** The Phase 6 rule (BH only when n >= 1000) is not met by any cohort, so the rule column reads 'not applied'. An informational BH q over all tests in the population is shown alongside and must be read as such.

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