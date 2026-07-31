# AI-READI Cognitive Impairment Analysis: Replication & Validation

This repository contains scripts and documentation for replicating and validating findings related to diabetes severity (CGM vs. HbA1c) and cognitive function (MoCA scores).

## Project Structure

```
new research/
├── README.md                              # Root project index & execution guide
├── docs/                                  # Analytical synthesis & methodology documentation
│   ├── comprehensive_replication_guide.md
│   ├── stratification_details.md
│   ├── cgm_vs_hba1c_holistic_comparison.md
│  ├── src/                                   # Python scripts organized by output phase
│   ├── 1_baseline_replication/            # Phase 1: Baseline statistical replication scripts
│   │   ├── extract_data.py
│   │   ├── analyze_data.py
│   │   ├── analyze_side_by_side.py
│   │   ├── moca_validity.py
│   │   ├── export_exact_results.py
│   │   ├── gridsearch.py
│   │   └── gridsearch_ml.py
│   ├── 2_advanced_causal_and_survey/      # Phase 2: Advanced econometrics & survey scripts
│   │   ├── extract_extended_data.py
│   │   ├── survey_bootstrap.py
│   │   ├── causal_inference.py
│   │   └── correlation_analysis.py
│   └── 3_spikes_surveys_and_interactions/ # Phase 3: High-frequency spikes & stratification scripts
│       ├── cgm_spike_extraction.py
│       ├── model_moca_spikes.py
│       ├── aireadi_survey_stratified.py
│       ├── moca_dummies_ttests.py
│       ├── paid_moca_analysis.py
│       └── interaction_stratified_models.py
├── data/                                  # Master CSV datasets
│   ├── master_cgm_moca_dataset.csv
│   ├── master_extended_dataset.csv
│   └── master_cgm_spikes_dataset.csv
└── reports/                               # Stratified report outputs by flow & generation phase
    ├── 1_baseline_replication/            # Phase 1: Baseline statistical replication & validation
    │   ├── report.md
    │   ├── report_side_by_side.md
    │   ├── moca_validity_results.md
    │   ├── comparison_results.md
    │   ├── gridsearch_results.txt
    │   ├── regression_results_total_moca.csv
    │   └── regression_results_specific_impairments.csv
    ├── 2_advanced_causal_and_survey/      # Phase 2: Advanced econometrics, survey & correlation
    │   ├── survey_bootstrap_results.md
    │   ├── causal_inference_results.md
    │   ├── correlation_results.md
    │   ├── analysis_implications_summary.md
    │   └── statistical_tests_and_logic_guide.md
    └── 3_spikes_surveys_and_interactions/ # Phase 3: High-frequency spikes, survey stratifications, & interactions
        ├── moca_spike_prediction_results.md
        ├── aireadi_surveys_age_diabetes_stratification.md
        ├── moca_dummies_ttests_results.md
        ├── paid_moca_item_analysis.md
        └── interaction_and_stratified_models.md
```

---

## Order of Execution

To fully replicate the setup and run the validation scripts, run the scripts in `src/` in this order:

### Phase 1: Baseline Statistical Replication

1. **[`src/1_baseline_replication/extract_data.py`](src/1_baseline_replication/extract_data.py)**
   - **What it does**: Parses raw AI-READI clinical data (`participants.tsv`, `measurement.csv`, `condition_occurrence.csv`, `observation.csv`) and Dexcom G6 CGM JSON files.
   - **Expected Output**: [`data/master_cgm_moca_dataset.csv`](data/master_cgm_moca_dataset.csv).

2. **[`src/1_baseline_replication/analyze_side_by_side.py`](src/1_baseline_replication/analyze_side_by_side.py)**
   - **What it does**: Direct side-by-side multivariable comparison of GMI vs HbA1c.
   - **Expected Output**: [`reports/1_baseline_replication/report_side_by_side.md`](reports/1_baseline_replication/report_side_by_side.md).

3. **[`src/1_baseline_replication/moca_validity.py`](src/1_baseline_replication/moca_validity.py)**
   - **What it does**: Evaluates MoCA construct validity using permutation bootstrap tests.
   - **Expected Output**: [`reports/1_baseline_replication/moca_validity_results.md`](reports/1_baseline_replication/moca_validity_results.md).

4. **[`src/1_baseline_replication/export_exact_results.py`](src/1_baseline_replication/export_exact_results.py)**
   - **What it does**: Exports unrounded regression coefficients, standard errors, Odds Ratios, and p-values to CSV.
   - **Expected Outputs (CSVs)**: 
     - [`reports/1_baseline_replication/regression_results_total_moca.csv`](reports/1_baseline_replication/regression_results_total_moca.csv)
     - [`reports/1_baseline_replication/regression_results_specific_impairments.csv`](reports/1_baseline_replication/regression_results_specific_impairments.csv)

### Phase 2: Advanced Econometric, Survey, & Correlation Analysis

5. **[`src/2_advanced_causal_and_survey/extract_extended_data.py`](src/2_advanced_causal_and_survey/extract_extended_data.py)**
   - **What it does**: Extracts survey data (depression, diet, smoking, alcohol, vape, vision care) into master extended dataset.
   - **Expected Output**: [`data/master_extended_dataset.csv`](data/master_extended_dataset.csv).

6. **[`src/2_advanced_causal_and_survey/survey_bootstrap.py`](src/2_advanced_causal_and_survey/survey_bootstrap.py)**
   - **What it does**: 10,000-iteration permutation test evaluating lifestyle factors against MoCA scores.
   - **Expected Output**: [`reports/2_advanced_causal_and_survey/survey_bootstrap_results.md`](reports/2_advanced_causal_and_survey/survey_bootstrap_results.md).

7. **[`src/2_advanced_causal_and_survey/causal_inference.py`](src/2_advanced_causal_and_survey/causal_inference.py)**
   - **What it does**: FWL partialling out, Fixed Effects, Propensity Score Matching (PSM), and Instrumental Variables (2SLS).
   - **Expected Output**: [`reports/2_advanced_causal_and_survey/causal_inference_results.md`](reports/2_advanced_causal_and_survey/causal_inference_results.md).

8. **[`src/2_advanced_causal_and_survey/correlation_analysis.py`](src/2_advanced_causal_and_survey/correlation_analysis.py)**
   - **What it does**: Computes Pearson ($r$) and Spearman ($\rho$) correlations for MoCA vs HbA1c and Mean Glucose.
   - **Expected Output**: [`reports/2_advanced_causal_and_survey/correlation_results.md`](reports/2_advanced_causal_and_survey/correlation_results.md).

### Phase 3: High-Frequency Spikes, Survey Stratification, & Interaction Econometrics

9. **[`src/3_spikes_surveys_and_interactions/cgm_spike_extraction.py`](src/3_spikes_surveys_and_interactions/cgm_spike_extraction.py)** & **[`src/3_spikes_surveys_and_interactions/model_moca_spikes.py`](src/3_spikes_surveys_and_interactions/model_moca_spikes.py)**
   - **What it does**: Parses continuous Dexcom G6 5-minute CGM streams to extract spike metrics and fits logistic regressions against MoCA impairment.
   - **Expected Output**: [`reports/3_spikes_surveys_and_interactions/moca_spike_prediction_results.md`](reports/3_spikes_surveys_and_interactions/moca_spike_prediction_results.md).

10. **[`src/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py`](src/3_spikes_surveys_and_interactions/aireadi_survey_stratified.py)**
    - **What it does**: Cross-tabulates 4 AI-READI questionnaires across a 3x4 grid (3 Age Partitions $\times$ 4 Diabetes Types).
    - **Expected Output**: [`reports/3_spikes_surveys_and_interactions/aireadi_surveys_age_diabetes_stratification.md`](reports/3_spikes_surveys_and_interactions/aireadi_surveys_age_diabetes_stratification.md).

11. **[`src/3_spikes_surveys_and_interactions/moca_dummies_ttests.py`](src/3_spikes_surveys_and_interactions/moca_dummies_ttests.py)**
    - **What it does**: Two-sample Welch's t-tests with Standard Errors ($\text{SE}$) and multivariable dummy regressions.
    - **Expected Output**: [`reports/3_spikes_surveys_and_interactions/moca_dummies_ttests_results.md`](reports/3_spikes_surveys_and_interactions/moca_dummies_ttests_results.md).

12. **[`src/3_spikes_surveys_and_interactions/paid_moca_analysis.py`](src/3_spikes_surveys_and_interactions/paid_moca_analysis.py)**
    - **What it does**: Evaluates item-level PAID-5 diabetes distress questions against MoCA cognitive sub-scores.
    - **Expected Output**: [`reports/3_spikes_surveys_and_interactions/paid_moca_item_analysis.md`](reports/3_spikes_surveys_and_interactions/paid_moca_item_analysis.md).

13. **[`src/3_spikes_surveys_and_interactions/interaction_stratified_models.py`](src/3_spikes_surveys_and_interactions/interaction_stratified_models.py)**
    - **What it does**: Tests main effect and non-linear interaction terms ($\text{Age}_{>65} \times \text{Diabetic}$) and 4-quadrant stratified linear models.
    - **Expected Output**: [`reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md`](reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md).

---

## Generated Reports Summary

| Phase | Report File | Generated By | Primary Purpose |
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
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md`](reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md)** | `src/3_spikes_surveys_and_interactions/interaction_stratified_models.py` | Non-linear interaction terms (Age x Diabetic) and 4-quadrant OLS models. |em-level PAID-5 diabetes distress questions vs MoCA sub-scores. |
| **Phase 3** | **[`reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md`](reports/3_spikes_surveys_and_interactions/interaction_and_stratified_models.md)** | `src/interaction_stratified_models.py` | Non-linear interaction terms (Age x Diabetic) and 4-quadrant OLS models. |

---

## Documentation & Methodology

Refer to the following analytical reports located in `docs/`:

- **[`docs/comprehensive_replication_guide.md`](docs/comprehensive_replication_guide.md)**: End-to-end guide detailing data acquisition, cleaning pipelines, and step-by-step statistical replication.
- **[`docs/stratification_details.md`](docs/stratification_details.md)**: Details precisely how cohorts were grouped, how outcome variables were separated, and how covariates were adjusted.
- **[`docs/cgm_vs_hba1c_holistic_comparison.md`](docs/cgm_vs_hba1c_holistic_comparison.md)**: A comprehensive, ground-up comparison of how CGM (GMI/TIR) compares to HbA1c in predicting cognitive impairment.
- **[`docs/analysis_implications_summary.md`](docs/analysis_implications_summary.md)**: A plain-english summary of analytical outputs from advanced econometric, correlation, and survey permutation tests.
