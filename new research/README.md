# AI-READI Cognitive Impairment Analysis: Replication, Econometrics, & Glycemic Dynamics

This repository contains a modular Python research pipeline and comprehensive documentation for analyzing the relationship between **diabetes severity**, **continuous glucose monitoring (CGM) dynamics**, **social determinants of health (SDOH)**, and **cognitive function (MoCA scores)** across the AI-READI cohort ($N = 2,226$).

---

## 1. Executive Summary & Research Framework

The analytical pipeline is structured into **3 distinct sequential phases**, each addressing specific methodological questions:

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
                                              ┌───────────────────────────────────────┐
                                              │   Phase 3: Spikes & Stratifications   │
                                              │   ├── Continuous CGM glucose surges   │
                                              │   ├── 3x4 Age x Diabetes Grid         │
                                              │   ├── Item-level PAID-5 distress      │
                                              │   └── Age x Diabetic Interaction OLS  │
                                              └───────────────────────────────────────┘
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
│   └── 3_spikes_surveys_and_interactions/ # Phase 3: Spikes & stratifications scripts
│       ├── cgm_spike_extraction.py        # Continuous 5-min glucose surge parser
│       ├── model_moca_spikes.py           # Spike duration & frequency logit models
│       ├── aireadi_survey_stratified.py   # 3x4 Age x Diabetes stratification grid
│       ├── moca_dummies_ttests.py         # Welch's t-tests (SE) & dummy regressions
│       ├── paid_moca_analysis.py          # Item-level PAID-5 distress vs MoCA
│       └── interaction_stratified_models.py# Non-linear interaction & 4-quadrant OLS
├── data/                                  # Master CSV datasets
│   ├── master_cgm_moca_dataset.csv        # Phase 1 baseline dataset
│   ├── master_extended_dataset.csv        # Phase 2 extended survey dataset
│   └── master_cgm_spikes_dataset.csv      # Phase 3 high-frequency spike dataset
└── reports/                               # Output markdown reports organized by phase
    ├── 1_baseline_replication/            # Phase 1 markdown reports & CSV exports
    ├── 2_advanced_causal_and_survey/      # Phase 2 econometric & survey reports
    └── 3_spikes_surveys_and_interactions/ # Phase 3 surge dynamic & interaction reports
```

---

## 3. Order of Execution

To fully replicate the setup and run the validation scripts, execute the scripts sequentially by phase:

### Environment Setup
```bash
# Navigate to the workspace root
cd "/Users/guardian/Documents/GitHub/bcc/ucsf"

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
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/aireadi_surveys_age_diabetes_stratification.md`](reports/3_spikes_surveys_and_interactions/aireadi_surveys_age_diabetes_stratification.md)** | `src/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py` | 3x4 grid stratification across age partitions and diabetes types. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/moca_dummies_ttests_results.md`](reports/3_spikes_surveys_and_interactions/moca_dummies_ttests_results.md)** | `src/3_spikes_surveys_and_interactions/moca_dummies_ttests.py` | Welch's t-tests with Standard Errors and multivariable dummy regressions. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/paid_moca_item_analysis.md`](reports/3_spikes_surveys_and_interactions/paid_moca_item_analysis.md)** | `src/3_spikes_surveys_and_interactions/paid_moca_analysis.py` | Item-level PAID-5 diabetes distress questions vs MoCA sub-scores. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md`](reports/3_spikes_surveys_and_interactions/interaction_stratified_models.md)** | `src/3_spikes_surveys_and_interactions/interaction_stratified_models.py` | Non-linear interaction terms (Age x Diabetic) and 4-quadrant OLS models. |

---

## 5. Methodology & Technical Documentation

For complete mathematical derivations and study designs, refer to the documents in `docs/`:

* **[`docs/comprehensive_replication_guide.md`](docs/comprehensive_replication_guide.md)**: End-to-end guide detailing raw AI-READI data parsing, cleaning pipelines, and step-by-step statistical replication.
* **[`docs/stratification_details.md`](docs/stratification_details.md)**: Details precisely how cohorts were grouped, how outcome variables were separated, and how covariates were adjusted.
* **[`docs/cgm_vs_hba1c_holistic_comparison.md`](docs/cgm_vs_hba1c_holistic_comparison.md)**: A ground-up comparison of how CGM (GMI/TIR) compares to HbA1c in predicting cognitive impairment.
* **[`docs/analysis_implications_summary.md`](docs/analysis_implications_summary.md)**: Scientific synthesis of econometric, correlation, and survey permutation test outputs.
