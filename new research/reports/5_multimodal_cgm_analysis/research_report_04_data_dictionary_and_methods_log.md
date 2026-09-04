# Phase 5 - Data dictionary, extraction rules and execution log

## 1. Execution

```bash
source "new research/.venv/bin/activate"
python3 "new research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py"   # ~5 min, 8 workers
python3 "new research/src/5_multimodal_cgm_analysis/run_multimodal_cgm_models.py"     # ~10 min
python3 "new research/src/5_multimodal_cgm_analysis/generate_reports.py"
```

Inputs: `dataset/` (AI-READI v3.0.0 flagship release). Output dataset: `new research/data/master_multimodal_dataset.csv` (one row per participant, 2,280 rows). Result CSVs: `reports/5_multimodal_cgm_analysis/data/`; figures: `.../figures/`.

## 2. Glucose category cut-offs (mg/dL)

| Category | Rule |
| :--- | :--- |
| Severe hypoglycaemia | < 54 (strict) |
| Moderate hypoglycaemia | 54-69 inclusive |
| Normal / time in range (TIR) | 70-180 inclusive |
| Moderate hyperglycaemia | 181-250 inclusive |
| Severe hyperglycaemia | > 250 (strict) |

## 3. CGM variables (Dexcom G6, 5-min sampling, converted to site-local time)

| Variable | Definition |
| :--- | :--- |
| `mean_glucose` | Mean of all valid readings (39-401 mg/dL) over the wear period |
| `glucose_sd` | Sample SD (ddof = 1) of all readings |
| `mean_to_sd_ratio` | `mean_glucose / glucose_sd` (inverse of the coefficient of variation) |
| `glucose_cv` | 100 x SD / mean |
| `gmi` | Glucose management indicator = 3.31 + 0.02392 x mean glucose |
| `tir_overall`, `tar_above_180`, `tbr_below_70`, `pct_severe_hypo`, `pct_mod_hypo`, `pct_mod_hyper`, `pct_severe_hyper` | Percentage of all readings in each category |
| `cgm_valid_days` | Number of local calendar days with >= 70% of the expected 288 readings |
| `avg_daily_tir` | Mean over valid days of the daily % of readings in 70-180 |
| `avg_daily_sd` | Mean over valid days of the within-day sample SD |
| `avg_daily_mean`, `avg_daily_tar`, `avg_daily_tbr`, `avg_daily_range`, `avg_daily_mean_to_sd` | Analogous day-level averages |
| `sd_of_daily_means` | Between-day SD of the daily means |
| `mag_mg_dl_per_h` | Mean absolute glucose change per hour (consecutive readings <= 30 min apart) |
| `nocturnal_mean`, `nocturnal_tar` | Mean and % > 180 between 00:00 and 05:59 local time |

Inclusion: >= 3 valid days (sensitivity: >= 7).

## 4. Clinical / survey variables (OMOP tables)

| Variable | Source | Rule |
| :--- | :--- | :--- |
| `hba1c` | `measurement.csv` `import_hba1c` | mean of laboratory values |
| `moca_total`, `moca_memory_index`, `moca_delayed_recall`, ... | `measurement.csv` `moca_*` | max per participant |
| `cognitive_impairment` | derived | MoCA total < 26 |
| `cesd10_total`, `cesd_item1..10` | `observation.csv` `cestl`, `ces1..ces10` | CES-D-10 total (0-30) |
| `cesd10_ge10` | derived | CES-D-10 >= 10 (standard screening threshold) |
| `paid5_total` | `observation.csv` `paidscore` | PAID-5 diabetes distress (0-20) |
| `years_of_education`, `education_level` | `observation.csv` | <= 12 y = high school or below; 13-16 = college; > 16 = graduate |
| `hypertension`, `high_cholesterol`, `kidney_disease`, `circulatory_problems` (circulation, stroke, MI), `pulmonary_disease`, ... | `condition_occurrence.csv` `mhoccur_*` | self-reported medical history |
| `insulin_use`, `oral_glucose_meds` | `observation.csv` `cmtrt_insln`, `cmtrt_a1c` | 0 for participants not asked (non-diabetic) |
| `current_smoker`, `ever_alcohol`, `sleeping_pills_2wk`, `food_insecure`, `fell_last_12mo` | `observation.csv` | sentinel codes 555/777/888/999 treated as missing |
| `diabetes_status`, `any_diabetes` | `participants.tsv` `study_group` | T2D = oral/non-insulin or insulin-dependent groups |
| `clinical_site`, `visit_season` | `participants.tsv` | UW, UCSD, UAB; season of study visit |

Sex and race/ethnicity are not released at the individual level in this dataset version and could not be adjusted for.

## 5. Home environmental sensor (LeeLab Anura, 5-s sampling, full file)

Physical-plausibility filters: temperature -10 to 50 C, humidity 0-100 %, PM < 5,000 ug/m3 (uint16 sentinel removed), VOC/NOx index 1-500 (0 = warm-up). Readings averaged to 1-minute bins before summarising.

| Variable | Definition |
| :--- | :--- |
| `env_pm25_mean`, `env_pm25_median`, `env_pm25_p95`, `env_pm25_daily_max` | PM2.5 (ug/m3) summaries |
| `env_pm25_pct_gt15`, `env_pm25_pct_gt35` | % of minutes above the WHO 2021 24-h guideline (15) and US EPA 24-h standard (35) |
| `log_pm25_mean` | log(1 + mean PM2.5) - primary environment outcome |
| `env_pm10_mean`, `env_pm1_mean` | PM10 / PM1 means |
| `env_temp_mean`, `env_temp_sd`, `env_temp_night_mean` (22:00-05:59), `env_temp_pct_lt18`, `env_temp_pct_gt26` | Temperature (C) |
| `env_hum_mean`, `env_hum_sd`, `env_hum_pct_gt60`, `env_hum_pct_lt30` | Relative humidity (%) |
| `env_voc_mean`, `env_voc_median`, `env_voc_pct_gt250` | Sensirion VOC index (100 = typical baseline) |
| `env_nox_mean`, `env_nox_median`, `env_nox_pct_gt20` | Sensirion NOx index |
| `env_days` | hours of valid data / 24; inclusion >= 3 days |

## 6. Wearable (Garmin Vivosmart 5)

| Variable | Definition |
| :--- | :--- |
| `wear_days_hr` | Calendar days (excluding first and last) with >= 10 distinct hours containing a valid heart-rate sample (30-220 bpm) |
| `hr_mean`, `hr_resting_proxy` (mean of the daily 5th percentile), `hr_night_mean` (00:00-04:59) | Heart rate (bpm) on wear-days |
| `steps_per_day` | Mean daily step total over wear-days with > 0 steps |
| `mvpa_min_per_day` | Minutes/day in non-sedentary epochs with cadence >= 100 steps/min (moderate-intensity proxy) |
| `active_min_per_day`, `sedentary_pct` | Non-sedentary minutes/day; % of labelled minutes labelled sedentary |
| `active_kcal_per_day` | Daily maximum of the cumulative active-kcal counter |
| `stress_mean`, `stress_pct_high` (> 50), `stress_pct_rest` (<= 25) | Garmin HRV-based stress index, valid samples 0-100 only (-1 / -2 removed) |
| `sleep_tst_min`, `sleep_efficiency_pct`, `sleep_deep_pct`, `sleep_rem_pct`, `sleep_tst_sd_min` | Per night (interval assigned to the date 12 h before its start); duplicate/overlapping intervals removed; nights between 2 h and 16 h |
| `spo2_mean`, `spo2_pct_lt90` | Pulse-oximetry samples 70-100 % |
| `resp_rate_mean` | Respiratory-rate samples 4-40 breaths/min |

## 7. Follow-up variables (report 05, `run_phase5_followups.py`)

| Variable | Definition |
| :--- | :--- |
| `hemoglobin_g_dl`, `mcv_fl`, `rdw_pct`, `hematocrit_pct`, `c_peptide` | `measurement.csv` `lbscat_a1c` (haemoglobin, g/dL - not HbA1c), `lbscat_mcv`, `lbscat_rdw`, `lbscat_hct`, `import_c_peptide` |
| `recommended_split` | `participants.tsv` train / val / test; train = discovery, val + test = hold-out |
| `sleep_onset_mean_h`, `sleep_midpoint_mean_h` | Mean clock time of sleep onset / midpoint, in hours after local noon of the night date (15 = 03:00) |
| `sleep_onset_sd_h`, `sleep_midpoint_sd_h`, `sleep_tst_sd_min` | Night-to-night SD of onset, midpoint and total sleep time (sleep regularity) |
| `hgi` | Haemoglobin glycation index = HbA1c minus its cohort-regression prediction from mean glucose (computed inside the follow-up script) |
| `glycation_gap` | HbA1c minus GMI |
| Split-half metrics (`followup_E_*`) | Mean glucose, daily SD and TIR computed separately for the first and second half of each participant's wear; ICC(2,1) |

## 8. Statistical procedures

- Continuous outcomes: OLS, HC3 heteroskedasticity-robust standard errors and t-tests; nested F-tests on the ML fit and HC3 block Wald tests.
- Binary outcomes: logistic regression (Newton-Raphson), Wald z-tests, likelihood-ratio tests, McFadden and Nagelkerke R2, DeLong test for paired AUC differences.
- Effects reported per 1 SD of the predictor (SD computed in the complete-case sample of that outcome) and in raw units.
- Out-of-sample performance: 5 x repeated 10-fold cross-validation (stratified for binary outcomes); R2 / AUC / Brier.
- Bootstrap (400 resamples) 95% percentile CI for the difference in adjusted R2 between CGM-only and HbA1c-only models.
- Multiplicity: Benjamini-Hochberg FDR within the primary slope family (14 outcomes x 5 predictors), the incremental-test family (14 x 2) and the single-metric-beyond-HbA1c family (14 x 4); exploratory sweeps FDR-controlled separately.
- Robustness: rank-based partial Spearman correlations, quadratic terms, diabetes-stratified slopes with interaction tests, >= 7-day CGM, insulin exclusion, diabetes-only and non-diabetes-only samples.
- Follow-ups (report 05): nested tests for the two-metric pair; HGI models with and without red-cell indices; discovery/hold-out replication with one-sided hold-out tests in the pre-specified direction; bootstrap (500) mediation; 4-group interaction tests and natural cubic splines (`cr(x, df=4)`); split-half ICC(2,1).
- Software: Python 3.14, pandas 3.0, statsmodels 0.14.6, scikit-learn 1.9, SciPy.