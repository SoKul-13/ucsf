# AI-READI Cognitive Impairment Analysis: Replication, Econometrics, & Glycemic Dynamics

This repository contains a modular Python research pipeline and comprehensive documentation for analyzing the relationship between **diabetes severity**, **continuous glucose monitoring (CGM) dynamics**, **social determinants of health (SDOH)**, and **cognitive function (MoCA scores)** across the AI-READI cohort ($N = 2,226$).

---

## 1. Executive Summary & Research Framework

The analytical pipeline is structured into **5 distinct sequential phases**, each addressing specific methodological questions:

```
                          [ AI-READI Raw EHR & Dexcom G6 Data ]
                                           │
                                           ▼
            ┌──────────────────────────────┴──────────────────────────────┐
            ▼                                                             ▼
┌───────────────────────────────────────┐     ┌───────────────────────────────────────┐
│   Phase 1: Baseline Replication       │     │   Phase 2: Advanced Econometrics      │
│   ├── GMI vs. HbA1c side-by-side      │ ──► │   ├── 10,000-iter survey bootstrap    │
│   ├── MoCA construct validity         │     │   ├── FWL partialling out & PSM       │
│   └── ML predictive benchmarks        │     │   └── Instrumental Variables (2SLS)   │
└───────────────────────────────────────┘     └───────────────────────────────────────┘
                                                           │
                                                           ▼
┌───────────────────────────────────────┐     ┌───────────────────────────────────────┐
│   Phase 4: Personalized Spike ML      │     │   Phase 3: Spikes & Stratifications   │
│   ├── Patient Z-score standardization ├───◄─│   ├── Continuous CGM glucose surges   │
│   ├── 15m, 30m, 60m ML forecasting    │     │   ├── 3x4 Age x Diabetes Grid         │
│   └── Diurnal & 168-hr weekly grid    │     │   ├── Item-level PAID-5 distress      │
└───────────────────────────────────────┘     └───────────────────────────────────────┘
                                                           │
                                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│   Phase 5: Multimodal CGM Outcome Prediction & Comorbidity Evaluation               │
│   ├── 4 Domain Pillars: Cognition, Depression, Indoor Environment, Wearable Activity│
│   ├── HbA1c vs. CGM Metrics (Mean, SD, Mean/SD, TIR 70-180) vs. Combined Models     │
│   └── Likelihood Ratio Tests (LRT) for incremental value & redundancy testing       │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### Purpose of Each Phase:

* **Phase 1: Baseline Statistical Replication & Validation (`1_baseline_replication`)**
  * **Objective**: Evaluate whether continuous glucose monitoring metrics—specifically Glucose Management Indicator (GMI) and Time in Range (TIR)—provide equivalent or superior predictive power over traditional lab HbA1c in detecting MoCA cognitive impairment ($\text{MoCA} < 26$).
  * **Key Outputs**: Baseline multivariable regressions, cohort definition validation, and machine learning gridsearches.

* **Phase 2: Advanced Econometric, Survey, & Causal Inference (`2_advanced_causal_and_survey`)**
  * **Objective**: Control for confounding variables, selection bias, and lifestyle factors. Applies Frisch-Waugh-Lovell (FWL) partialling out, Propensity Score Matching (PSM), Instrumental Variables (2SLS), and 10,000-iteration permutation bootstrap tests on SDOH survey responses (depression, diet, smoking, vision care).
  * **Key Outputs**: Causal effect bounds, non-parametric permutation p-values, and Spearman/Pearson correlation matrices.

* **Phase 3: High-Frequency Spikes, Stratifications, & Interaction Econometrics (`3_spikes_surveys_and_interactions`)**
  * **Objective**: Move beyond static population averages to model high-frequency glucose surge dynamics ($>180 \text{ mg/dL}$ spikes), $3 \times 4$ demographic/questionnaire grid stratifications, item-level PAID-5 diabetes distress, Welch's t-tests with exact Standard Errors ($\text{SE}$), and non-linear interaction terms ($\text{Age}_{>65} \times \text{Diabetic}$).
  * **Key Outputs**: Dynamic surge predictive models, stratified subgroup matrices, and 4-quadrant linear models.

* **Phase 4: Personalized Spike Modeling, Machine Learning Forecasting, & Weekly Management (`4_personalized_spike_analysis`)**
  * **Objective**: Standardize individual patient baselines via Z-score transformation ($Z_{i,t} \ge 2.0$, $>2\text{ SD}$ surges) to address coverage equity across disease severity, build GroupKFold machine learning models forecasting spikes across 15, 30, and 60-minute horizons, evaluate cognitive/psychological correlations (MoCA and CESD-10 depression), and infer diurnal meal patterns and weekday vs. weekend management variability across a 168-hour grid.
  * **Key Outputs**: Patient baseline standardization pipeline, 15m/30m/60m ML forecasting models, paired weekday vs. weekend statistical tests, and 168-hour weekly glycemic heatmaps.

* **Phase 5: CGM vs HbA1c for Comorbidity Prediction (`5_multimodal_cgm_analysis`)**
  * **Objective**: Test whether four pre-specified CGM metrics (mean glucose, mean/SD ratio, average daily TIR 70-180, average daily SD; glucose categories < 54 / 54-69 / 70-180 / 181-250 / > 250 mg/dL) predict **cognition** (MoCA total, MoCA < 26, memory index), **depression** (CES-D-10 total and ≥ 10), the **home environment** (LeeLab Anura: PM2.5, temperature, humidity, VOC) and **wearable physiology** (Garmin: steps, brisk minutes, resting heart rate, sleep, stress) better than laboratory HbA1c. For every outcome, covariate-only, HbA1c-only, single-CGM-metric, four-CGM-metric and combined models are fitted on one identical complete-case sample (age, BMI, education, site, four comorbidities, season for environmental outcomes). Slopes are tested with HC3-robust t-tests (OLS) or Wald z-tests (logistic); incremental information with nested F / likelihood-ratio tests; out-of-sample value with 5 × 10-fold cross-validation, DeLong and bootstrap; multiplicity with Benjamini-Hochberg FDR; robustness with diabetes-stratified, quadratic, ≥ 7-day CGM, insulin-excluded and rank-based analyses, plus an FDR-controlled exploratory sweep of 11 further CGM metrics.
  * **Key Outputs**: `data/master_multimodal_dataset.csv` (2,280 × 163), `reports/5_multimodal_cgm_analysis/research_report_01..04*.md`, result CSVs in `reports/5_multimodal_cgm_analysis/data/`, six figures in `reports/5_multimodal_cgm_analysis/figures/`.
  * **Headline**: CGM (mean glucose, daily SD) adds to HbA1c for cognition and resting heart rate and makes HbA1c redundant there; HbA1c retains unique information for activity, sleep duration and indoor PM2.5; depression is unrelated to glycaemic level after adjustment.
  * **Follow-ups (report 05)**: a two-metric CGM pair (mean glucose + daily SD) reproduces the four-metric block with VIF ≤ 3.8; the non-glucose component of HbA1c (haemoglobin glycation index) carries the activity / sleep / PM2.5 signal and is not explained by red-cell indices; between-day glucose variability → CES-D-10 ≥ 10 replicates in the AI-READI hold-out split (OR 1.25 per SD); the cognition gradient is confined to the non-diabetic range; 10-day CGM metrics have split-half ICC 0.87-0.92.

---

## 2. Repository Structure

```
new research/
├── README.md                              # Root project index & execution guide
├── docs/                                  # Analytical synthesis & methodology guides
│   ├── comprehensive_replication_guide.md # End-to-end cleaning & statistical guide
│   ├── stratification_details.md          # Cohort grouping & covariate adjustment logic
│   ├── cgm_vs_hba1c_holistic_comparison.md# Deep dive: CGM metrics vs. lab HbA1c
│   └── analysis_implications_summary.md   # Scientific summary of findings
├── src/                                   # Python scripts organized by phase
│   ├── 1_baseline_replication/            # Phase 1: Baseline replication scripts
│   │   ├── extract_data.py                # Raw clinical & Dexcom JSON parser
│   │   ├── analyze_data.py                # Baseline GMI regression model
│   │   ├── analyze_side_by_side.py        # GMI vs HbA1c side-by-side comparison
│   │   ├── moca_validity.py               # MoCA permutation bootstrap test
│   │   ├── export_exact_results.py        # Unrounded regression outputs & CIs
│   │   ├── gridsearch.py                  # Statistical model gridsearch
│   │   └── gridsearch_ml.py               # Machine Learning predictive benchmark
│   ├── 2_advanced_causal_and_survey/      # Phase 2: Advanced econometrics scripts
│   │   ├── extract_extended_data.py       # Extended survey feature extractor
│   │   ├── survey_bootstrap.py            # 10,000-iteration permutation bootstrap
│   │   ├── causal_inference.py            # FWL, PSM, IV-2SLS & Fixed Effects
│   │   └── correlation_analysis.py        # Pearson & Spearman correlation matrices
│   ├── 3_spikes_surveys_and_interactions/ # Phase 3: Spikes & stratifications scripts
│   │   ├── cgm_spike_extraction.py        # Continuous 5-min glucose surge parser
│   │   ├── model_moca_spikes.py           # Spike duration & frequency logit models
│   │   ├── aireadi_survey_stratified.py   # 3x4 Age x Diabetes stratification grid
│   │   ├── moca_dummies_ttests.py         # Welch's t-tests (SE) & dummy regressions
│   │   ├── paid_moca_analysis.py          # Item-level PAID-5 distress vs MoCA
│   │   └── interaction_stratified_models.py# Non-linear interaction & 4-quadrant OLS
│   └── 4_personalized_spike_analysis/    # Phase 4: Personalized spike ML & weekly dynamics
│       ├── 01_personalized_spike_evaluation.py # Patient z-score standardization & clinical correlations
│       ├── 02_extract_sliding_windows.py  # 805k parallel time-series sliding window extractor
│       ├── 03_predictive_spike_models.py  # GroupKFold ML forecasting (15m, 30m, 60m horizons)
│       └── 04_diurnal_weekly_management.py# Meal pattern inference, weekday/weekend tests & 168h grid
│   └── 5_multimodal_cgm_analysis/         # Phase 5: CGM vs HbA1c comorbidity prediction
│       ├── extract_multimodal_dataset.py  # Full-file extraction: CGM day-level metrics, OMOP, Anura sensor, Garmin (site-local time)
│       ├── run_multimodal_cgm_models.py   # Nested HbA1c / CGM / combined models, CV, DeLong, bootstrap, FDR, figures
│       ├── generate_reports.py            # Markdown tables: research_report_02..04
│       ├── run_phase5_followups.py        # Follow-ups (report 05): CGM pair, HGI discordance, replication, splines, split-half ICC
│       ├── generate_head_to_head_report.py# (companion) head-to-head summary generator
│       └── generate_phase4_style_report.py# (companion) Phase-4-style table generator
├── data/                                  # Master CSV & Parquet datasets
│   ├── master_cgm_moca_dataset.csv        # Phase 1 baseline dataset
│   ├── master_extended_dataset.csv        # Phase 2 extended survey dataset
│   ├── master_cgm_spikes_dataset.csv      # Phase 3 high-frequency spike dataset
│   ├── personalized_spike_metrics.csv     # Phase 4 master personalized spike dataset
│   └── master_multimodal_dataset.csv      # Phase 5 master multimodal dataset
└── reports/                               # Output markdown reports organized by phase
    ├── 1_baseline_replication/            # Phase 1 markdown reports & CSV exports
    ├── 2_advanced_causal_and_survey/      # Phase 2 econometric & survey reports
    ├── 3_spikes_surveys_and_interactions/ # Phase 3 surge dynamic & interaction reports
    ├── 4_personalized_spike_analysis/    # Phase 4 personalized spike reports, figures & data
    │   ├── INDEPTH_EXPLANATION_AND_RESULTS.md # In-depth research report & executive synthesis
    │   ├── personalized_spike_analysis.md # Comprehensive Phase 4 analytical report
    │   ├── data/                          # Phase 4 output summary CSVs & window parquet
    │   └── figures/                       # High-resolution PNG visualizations (Fig 1 - Fig 6)
    └── 5_multimodal_cgm_analysis/         # Phase 5 reports, result CSVs & figures
        ├── research_report_01_cgm_vs_hba1c_comorbidity_prediction.md   # Main narrative research report
        ├── research_report_02_full_regression_tables.md                # All specifications, all outcomes
        ├── research_report_03_sensitivity_and_exploratory_tables.md    # Sensitivity samples & exploratory sweeps
        ├── research_report_04_data_dictionary_and_methods_log.md       # Variable definitions & procedures
        ├── research_report_05_followups_parsimony_discordance_replication.md # Follow-up analyses (pair, HGI, replication, splines, stability)
        ├── data/                          # Result CSVs (slopes, nested tests, CV, FDR, stratified, Table 1)
        └── figures/                       # fig1-fig10 PNG
```

---

## 3. Order of Execution

To fully replicate the setup and run the validation scripts, execute the scripts sequentially by phase:

### Environment Setup
```bash
# Navigate to the workspace root
cd ucsf

# Activate the Python Virtual Environment
source "new research/.venv/bin/activate"
```

### Phase 1: Baseline Replication & Validation
```bash
# 1. Parse raw clinical data & Dexcom G6 CGM streams into master dataset
python3 "new research/src/1_baseline_replication/extract_data.py"

# 2. Run side-by-side multivariable comparison of GMI vs HbA1c
python3 "new research/src/1_baseline_replication/analyze_side_by_side.py"

# 3. Evaluate MoCA construct validity using permutation bootstrap tests
python3 "new research/src/1_baseline_replication/moca_validity.py"

# 4. Execute Machine Learning GridSearch comparing model predictive power
python3 "new research/src/1_baseline_replication/gridsearch_ml.py"

# 5. Export exact unrounded regression coefficients, standard errors, and 95% CIs
python3 "new research/src/1_baseline_replication/export_exact_results.py"
```

### Phase 2: Advanced Econometrics, Causal Inference, & Survey Analysis
```bash
# 6. Extract lifestyle, SDOH, and survey data into master extended dataset
python3 "new research/src/2_advanced_causal_and_survey/extract_extended_data.py"

# 7. Execute 10,000-iteration permutation bootstrap test on survey covariates
python3 "new research/src/2_advanced_causal_and_survey/survey_bootstrap.py"

# 8. Run econometric causal models (FWL, Fixed Effects, PSM, IV-2SLS)
python3 "new research/src/2_advanced_causal_and_survey/causal_inference.py"

# 9. Compute Pearson (r) and Spearman (ρ) correlation matrices
python3 "new research/src/2_advanced_causal_and_survey/correlation_analysis.py"
```

### Phase 3: High-Frequency Spikes, Stratifications, & Interaction Econometrics
```bash
# 10. Extract continuous 5-minute Dexcom G6 glucose surge events (>180 mg/dL)
python3 "new research/src/3_spikes_surveys_and_interactions/cgm_spike_extraction.py"

# 11. Model glucose spike duration, frequency, and magnitude against MoCA scores
python3 "new research/src/3_spikes_surveys_and_interactions/model_moca_spikes.py"

# 12. Generate 3x4 grid stratification matrix (3 Age Partitions x 4 Diabetes Types)
python3 "new research/src/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py"

# 13. Perform feature-level Welch's t-tests with SEs and multivariable dummy regressions
python3 "new research/src/3_spikes_surveys_and_interactions/moca_dummies_ttests.py"

# 14. Analyze item-level PAID-5 diabetes distress questions vs. MoCA sub-scores
python3 "new research/src/3_spikes_surveys_and_interactions/paid_moca_analysis.py"

# 15. Fit non-linear interaction terms (Age > 65 x Diabetic) and 4-quadrant OLS models
python3 "new research/src/3_spikes_surveys_and_interactions/interaction_stratified_models.py"
```

### Phase 4: Personalized Spike Modeling, Machine Learning Forecasting, & Weekly Dynamics
```bash
# 16. Standardize patient CGM baselines, evaluate >2 SD coverage equity & MoCA/CESD-10 correlations
python3 "new research/src/4_personalized_spike_analysis/01_personalized_spike_evaluation.py"

# 17. Parallel extract 805,789 sliding time-series window features across all participants
python3 "new research/src/4_personalized_spike_analysis/02_extract_sliding_windows.py"

# 18. Train 5-Fold GroupKFold ML models forecasting spikes 15, 30, and 60 minutes in advance
python3 "new research/src/4_personalized_spike_analysis/03_predictive_spike_models.py"

# 19. Analyze diurnal meal patterns vs diet score, weekday vs weekend volatility & 168-hour grid
python3 "new research/src/4_personalized_spike_analysis/04_diurnal_weekly_management.py"
```

### Phase 5: Multimodal CGM Outcome Prediction & Comorbidity Evaluation
```bash
# 20. Extract master multimodal dataset merging clinical EHR, survey, environmental sensors & wearables
python3 "new research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py"

# 21. Run 3-specification nested regressions (HbA1c vs CGM vs Combined) & LRT incremental tests
python3 "new research/src/5_multimodal_cgm_analysis/run_multimodal_cgm_models.py"

# 22. Render the markdown table reports (full regression tables, sensitivity/exploratory tables, data dictionary)
python3 "new research/src/5_multimodal_cgm_analysis/generate_reports.py"

# 23. Follow-up analyses: parsimonious CGM pair, HbA1c-CGM discordance (HGI), split-sample depression replication, splines, split-half stability
python3 "new research/src/5_multimodal_cgm_analysis/run_phase5_followups.py"
```

---

## 4. Generated Reports Summary Table

| Phase | Report Markdown File | Python Generator Script | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **[`reports/1_baseline_replication/report.md`](reports/1_baseline_replication/report.md)** | `src/1_baseline_replication/analyze_data.py` | Baseline statistical replication using GMI instead of HbA1c. |
| **Phase 1** | **[`reports/1_baseline_replication/report_side_by_side.md`](reports/1_baseline_replication/report_side_by_side.md)** | `src/1_baseline_replication/analyze_side_by_side.py` | Direct multivariable comparison of GMI vs HbA1c side-by-side. |
| **Phase 1** | **[`reports/1_baseline_replication/moca_validity_results.md`](reports/1_baseline_replication/moca_validity_results.md)** | `src/1_baseline_replication/moca_validity.py` | Cohort definition comparison (AI-READI Strings vs Exhaustive OMOP). |
| **Phase 1** | **[`reports/1_baseline_replication/comparison_results.md`](reports/1_baseline_replication/comparison_results.md)** | `src/1_baseline_replication/gridsearch_ml.py` | Machine Learning GridSearch comparing predictive power of all metrics. |
| **Phase 1** | **[`reports/1_baseline_replication/regression_results_total_moca.csv`](reports/1_baseline_replication/regression_results_total_moca.csv)** <br> **[`reports/1_baseline_replication/regression_results_specific_impairments.csv`](reports/1_baseline_replication/regression_results_specific_impairments.csv)** | `src/1_baseline_replication/export_exact_results.py` | Raw regression coefficients, standard errors, p-values, and 95% CIs. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/survey_bootstrap_results.md`](reports/2_advanced_causal_and_survey/survey_bootstrap_results.md)** | `src/2_advanced_causal_and_survey/survey_bootstrap.py` | 10,000-iter MoCA permutation test for survey factors. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/causal_inference_results.md`](reports/2_advanced_causal_and_survey/causal_inference_results.md)** | `src/2_advanced_causal_and_survey/causal_inference.py` | FWL, Fixed Effects, PSM, and Instrumental Variables. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/correlation_results.md`](reports/2_advanced_causal_and_survey/correlation_results.md)** | `src/2_advanced_causal_and_survey/correlation_analysis.py` | Pearson/Spearman correlation for MoCA and Glucose metrics. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/analysis_implications_summary.md`](reports/2_advanced_causal_and_survey/analysis_implications_summary.md)** | Manual synthesis | Scientific summary of Phase 2 findings and implications. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/statistical_tests_and_logic_guide.md`](reports/2_advanced_causal_and_survey/statistical_tests_and_logic_guide.md)** | Manual guide | Comprehensive variable definitions, symbol guide, and test logic walkthrough. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/moca_spike_prediction_results.md`](reports/3_spikes_surveys_and_interactions/moca_spike_prediction_results.md)** | `src/3_spikes_surveys_and_interactions/model_moca_spikes.py` | Continuous glucose surge dynamics & logistic regression against MoCA. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/aireadi_surveys_age_diabetes_stratification.md`](reports/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py)** | `src/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py` | 3x4 grid stratification across age partitions and diabetes types. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/moca_dummies_ttests_results.md`](reports/3_spikes_surveys_and_interactions/moca_dummies_ttests_results.md)** | `src/3_spikes_surveys_and_interactions/moca_dummies_ttests.py` | Welch's t-tests with Standard Errors and multivariable dummy regressions. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/paid_moca_item_analysis.md`](reports/3_spikes_surveys_and_interactions/paid_moca_analysis.md)** | `src/3_spikes_surveys_and_interactions/paid_moca_analysis.py` | Item-level PAID-5 diabetes distress questions vs MoCA sub-scores. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md`](reports/3_spikes_surveys_and_interactions/interaction_stratified_models.md)** | `src/3_spikes_surveys_and_interactions/interaction_stratified_models.py` | Non-linear interaction terms (Age x Diabetic) and 4-quadrant OLS models. |
| **Phase 4** | **[`reports/4_personalized_spike_analysis/01_personalized_spike_and_equity_report.md`](reports/4_personalized_spike_analysis/01_personalized_spike_and_equity_report.md)** | `src/4_personalized_spike_analysis/01_personalized_spike_evaluation.py` | Deliverable 1: Z-score baseline standardization, >2 SD population coverage equity, MoCA & CESD-10 regressions. |
| **Phase 4** | **[`reports/4_personalized_spike_analysis/02_predictive_spike_forecasting_report.md`](reports/4_personalized_spike_analysis/02_predictive_spike_forecasting_report.md)** | `src/4_personalized_spike_analysis/03_predictive_spike_models.py` | Deliverable 2: Machine Learning forecasting metrics (ROC-AUC, PR-AUC, F1, Brier) across 15m/30m/60m horizons. |
| **Phase 4** | **[`reports/4_personalized_spike_analysis/03_diurnal_meal_and_snacking_taxonomy_report.md`](reports/4_personalized_spike_analysis/03_diurnal_meal_and_snacking_taxonomy_report.md)** | `src/4_personalized_spike_analysis/04_diurnal_weekly_management.py` | Deliverable 3: Algorithmic peak detection, 3-Meal vs Grazer taxonomy ($K_i$), postprandial clearance ($k$), diet validation. |
| **Phase 4** | **[`reports/4_personalized_spike_analysis/04_weekday_vs_weekend_and_sdoh_report.md`](reports/4_personalized_spike_analysis/04_weekday_vs_weekend_and_sdoh_report.md)** | `src/4_personalized_spike_analysis/04_diurnal_weekly_management.py` | Deliverable 4: 15-metric battery, paired weekday vs weekend tests ($p = 5.56\times 10^{-25}$), work status, multi-survey SDOH. |
| **Phase 5** | **[`reports/5_multimodal_cgm_analysis/research_report_01_cgm_vs_hba1c_comorbidity_prediction.md`](reports/5_multimodal_cgm_analysis/research_report_01_cgm_vs_hba1c_comorbidity_prediction.md)** | Manual synthesis from `run_multimodal_cgm_models.py` outputs | Main research report: abstract, background, methods, results per domain (cognition, depression, home environment, wearables), discussion, limitations, references. |
| **Phase 5** | **[`reports/5_multimodal_cgm_analysis/research_report_02_full_regression_tables.md`](reports/5_multimodal_cgm_analysis/research_report_02_full_regression_tables.md)** | `src/5_multimodal_cgm_analysis/generate_reports.py` | Table 1 descriptives, predictor correlations, FDR-controlled slope and incremental-test families, and every specification for every primary outcome. |
| **Phase 5** | **[`reports/5_multimodal_cgm_analysis/research_report_03_sensitivity_and_exploratory_tables.md`](reports/5_multimodal_cgm_analysis/research_report_03_sensitivity_and_exploratory_tables.md)** | `src/5_multimodal_cgm_analysis/generate_reports.py` | ≥ 7-day CGM, insulin-excluded, diabetes-only and non-diabetes samples; exploratory outcomes; 11-metric CGM sweep with FDR. |
| **Phase 5** | **[`reports/5_multimodal_cgm_analysis/research_report_04_data_dictionary_and_methods_log.md`](reports/5_multimodal_cgm_analysis/research_report_04_data_dictionary_and_methods_log.md)** | `src/5_multimodal_cgm_analysis/generate_reports.py` | Variable dictionary, extraction rules, glucose cut-offs, statistical procedures, execution commands. |
| **Phase 5** | **[`reports/5_multimodal_cgm_analysis/research_report_05_followups_parsimony_discordance_replication.md`](reports/5_multimodal_cgm_analysis/research_report_05_followups_parsimony_discordance_replication.md)** | `src/5_multimodal_cgm_analysis/run_phase5_followups.py` | Follow-ups: two-metric CGM pair vs four-metric block; HbA1c-CGM discordance (HGI) with red-cell adjustment; discovery/hold-out replication of the depression signal with sleep-regularity mediation; 4-group interactions and spline dose-response; split-half reliability. |
| **Phase 5** | [`reports/5_multimodal_cgm_analysis/01_executive_summary_multimodal_cgm_comorbidity_analysis.md`](reports/5_multimodal_cgm_analysis/01_executive_summary_multimodal_cgm_comorbidity_analysis.md), [`02_cgm_vs_hba1c_head_to_head_comparative_analysis.md`](reports/5_multimodal_cgm_analysis/02_cgm_vs_hba1c_head_to_head_comparative_analysis.md), [`03_full_econometric_regression_prediction_tables.md`](reports/5_multimodal_cgm_analysis/03_full_econometric_regression_prediction_tables.md), [`04_execution_and_methodology_detailed_log.md`](reports/5_multimodal_cgm_analysis/04_execution_and_methodology_detailed_log.md) | `generate_head_to_head_report.py`, `generate_phase4_style_report.py` | Companion summaries produced by the earlier Phase 5 pass (three-model comparison in the Phase 4 table style). |

---

## 5. Methodology & Technical Documentation

For complete mathematical derivations and study designs, refer to the documents in `docs/`:

* **[`docs/comprehensive_replication_guide.md`](docs/comprehensive_replication_guide.md)**: End-to-end guide detailing raw AI-READI data parsing, cleaning pipelines, and step-by-step statistical replication.
* **[`docs/stratification_details.md`](docs/stratification_details.md)**: Details precisely how cohorts were grouped, how outcome variables were separated, and how covariates were adjusted.
* **[`docs/cgm_vs_hba1c_holistic_comparison.md`](docs/cgm_vs_hba1c_holistic_comparison.md)**: A ground-up comparison of how CGM (GMI/TIR) compares to HbA1c in predicting cognitive impairment.
* **[`docs/analysis_implications_summary.md`](docs/analysis_implications_summary.md)**: Scientific synthesis of econometric, correlation, and survey permutation test outputs.
