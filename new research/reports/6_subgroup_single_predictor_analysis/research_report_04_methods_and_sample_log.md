# Phase 6 - Methods, sample construction and execution log

## Execution

```bash
source "new research/.venv/bin/activate"
python3 "new research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py"       # shared with Phase 5 (adds the band metrics)
python3 "new research/src/6_subgroup_single_predictor_analysis/run_phase6_analysis.py"     # ~10 min
python3 "new research/src/6_subgroup_single_predictor_analysis/generate_phase6_reports.py"
```

## Sample construction (identical to Phase 5)

1. `master_multimodal_dataset.csv` (2,280 rows) from the shared extractor; CGM readings 39-401 mg/dL, site-local time, valid day = >= 70 % of 288 readings, no truncation of the wear period.
2. Analysis base = >= 3 valid CGM days, laboratory HbA1c present, four core CGM metrics present, complete covariates -> N = 2,138.
3. Populations: total (2,138); healthy = study groups `healthy` + `pre_diabetes_lifestyle_controlled` (1,271); non-healthy = `oral_medication_and_or_non_insulin_injectable_medication_controlled` + `insulin_dependent` (867).
4. For each population and outcome: complete cases on the outcome and covariates (season for environmental outcomes). For each predictor: the outcome sample minus participants missing that predictor (day-level band metrics can be missing only for very short wear). Every predictor for a given population x outcome is therefore fitted on the same rows except for those rare predictor-specific losses, which are visible in the `n` column.
5. Band predictors are skipped when fewer than 30 participants in the sample have any time in the band (recorded in the tables as 'skipped').

## Models and tests

- `outcome ~ covariates + predictor`, one predictor at a time (rule #2). No combined HbA1c + CGM models in this phase.
- OLS with HC3-robust standard errors (t-test) for continuous outcomes; logistic regression with Wald z for binary outcomes.
- Effects per 1 SD of the predictor (SD in that population and outcome sample); raw slope per unit also reported.
- AIC of the predictor model minus AIC of (a) the covariates-only model and (b) the HbA1c-only model on the same rows.
- Out-of-sample R2 / AUC from repeated 3 x 10-fold cross-validation for the predictor model and the covariates-only model.
- FDR (rule #3): Benjamini-Hochberg applied only to tests whose sample has n >= 1000; families = (i) all tests in the population, (ii) all predictors within one outcome, (iii) all outcomes within one predictor, (iv) all tests within one band. Raw p-values are always reported alongside.

## How 'pooled' and 'day-averaged' metrics are calculated

Let g_1 ... g_N be every valid Dexcom reading of a participant over the whole wear (all days concatenated, 5-min sampling, values 39-401 mg/dL, site-local time; N is typically ~2,850 for 10 days). Let D be the set of *valid* calendar days (days holding >= 70 % of the expected 288 readings) and g_{d,1} ... g_{d,n_d} the readings on day d.

- **Pooled** metric = one statistic computed over all N readings at once, ignoring day boundaries. Examples: mean glucose = (1/N) sum g_i; pooled SD = sqrt( sum (g_i - mean)^2 / (N-1) ); pooled time in 70-180 = 100 x #{i : 70 <= g_i <= 180} / N; pooled time > 250 = 100 x #{i : g_i > 250} / N. Every reading counts equally, so days with more readings weigh more, and partial days are included.
- **Day-averaged** metric = compute the statistic separately on each valid day, then take the unweighted mean over valid days: avg. daily SD = (1/|D|) sum_d SD(g_{d,.}); avg. daily time in 70-180 = (1/|D|) sum_d [100 x #{j : 70 <= g_{d,j} <= 180} / n_d]; likewise for every band. Each day counts equally, partial days (< 70 % complete) are excluded, and the within-day SD is not inflated by day-to-day drift in the mean.
- The two versions correlate at rho ~ 0.98-0.99 for TIR and SD in this cohort and give the same conclusions; the day-averaged form is the one the collaborator asked for ('average daily TIR', 'average daily SD'), the pooled form matches Phase 1-4 and the international consensus reporting.
- Related between-day metric: SD of daily means = SD over valid days of the daily mean glucose (captures day-to-day drift rather than within-day swings).
- 'Any reading < 54' / 'any reading > 250' = 1 if at least one valid reading falls in the band during the wear, else 0.

## Predictors

| Column | Label | Family | Band |
| :--- | :--- | :--- | :--- |
| `hba1c` | HbA1c (%) | HbA1c | - |
| `mean_glucose` | Mean glucose (mg/dL) | CGM level | - |
| `gmi` | GMI (%) | CGM level | - |
| `nocturnal_mean` | Nocturnal mean 00-06h (mg/dL) | CGM level | - |
| `glucose_sd` | Glucose SD, pooled (mg/dL) | CGM variability | - |
| `avg_daily_sd` | Avg. daily SD (mg/dL) | CGM variability | - |
| `glucose_cv` | CV (%) | CGM variability | - |
| `mean_to_sd_ratio` | Mean / SD ratio | CGM variability | - |
| `avg_daily_mean_to_sd` | Avg. daily mean / SD | CGM variability | - |
| `mag_mg_dl_per_h` | MAG (mg/dL/h) | CGM variability | - |
| `avg_daily_range` | Avg. daily range (mg/dL) | CGM variability | - |
| `sd_of_daily_means` | SD of daily means (mg/dL) | CGM variability | - |
| `tir_overall` | Time in range 70-180, pooled (%) | Range 70-180 | 70-180 |
| `avg_daily_tir` | Avg. daily time in range 70-180 (%) | Range 70-180 | 70-180 |
| `any_below_54` | Any reading < 54 during wear (0/1) | Band < 54 | <54 |
| `pct_severe_hypo` | Time < 54, pooled (%) | Band < 54 | <54 |
| `avg_daily_pct_below_54` | Avg. daily time < 54 (%) | Band < 54 | <54 |
| `pct_mod_hypo` | Time 54-69, pooled (%) | Band 54-69 | 54-69 |
| `avg_daily_pct_54_69` | Avg. daily time 54-69 (%) | Band 54-69 | 54-69 |
| `tbr_below_70` | Time < 70, pooled (%) | Band < 70 | <70 |
| `avg_daily_tbr` | Avg. daily time < 70 (%) | Band < 70 | <70 |
| `pct_54_250` | Time 54-250, pooled (%) | Band 54-250 | 54-250 |
| `avg_daily_pct_54_250` | Avg. daily time 54-250 (%) | Band 54-250 | 54-250 |
| `pct_mod_hyper` | Time 181-250, pooled (%) | Band 181-250 | 181-250 |
| `avg_daily_pct_181_250` | Avg. daily time 181-250 (%) | Band 181-250 | 181-250 |
| `tar_above_180` | Time > 180, pooled (%) | Band > 180 | >180 |
| `avg_daily_tar` | Avg. daily time > 180 (%) | Band > 180 | >180 |
| `nocturnal_tar` | Nocturnal time > 180 (%) | Band > 180 | >180 |
| `any_above_250` | Any reading > 250 during wear (0/1) | Band > 250 | >250 |
| `pct_severe_hyper` | Time > 250, pooled (%) | Band > 250 | >250 |
| `avg_daily_pct_above_250` | Avg. daily time > 250 (%) | Band > 250 | >250 |

## Outcomes (as in Phase 5)

| Domain | Column | Type | Label |
| :--- | :--- | :--- | :--- |
| Cognition | `moca_total` | OLS | MoCA total score (0-30) |
| Cognition | `cognitive_impairment` | logistic | Cognitive impairment (MoCA < 26) |
| Cognition | `moca_memory_index` | OLS | MoCA memory index score (0-15) |
| Depression | `cesd10_total` | OLS | CES-D-10 depressive symptoms (0-30) |
| Depression | `cesd10_ge10` | logistic | Clinically relevant depressive symptoms (CES-D-10 >= 10) |
| Home environment | `log_pm25_mean` | OLS | Indoor PM2.5, log(1 + mean ug/m3) |
| Home environment | `env_temp_mean` | OLS | Indoor temperature, mean (deg C) |
| Home environment | `env_hum_mean` | OLS | Indoor relative humidity, mean (%) |
| Home environment | `env_voc_mean` | OLS | Indoor VOC index, mean |
| Wearable activity | `steps_per_day` | OLS | Steps per wear-day |
| Wearable activity | `mvpa_min_per_day` | OLS | Brisk-cadence minutes per day (>= 100 steps/min) |
| Wearable activity | `hr_resting_proxy` | OLS | Resting heart-rate proxy (daily 5th pct, bpm) |
| Wearable activity | `sleep_tst_min` | OLS | Total sleep time per night (min) |
| Wearable activity | `stress_mean` | OLS | Garmin stress score, mean (0-100) |