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
│   └── analysis_implications_summary.md
├── src/                                   # Python data processing & statistical modeling scripts
│   ├── extract_data.py
│   ├── extract_extended_data.py
│   ├── analyze_data.py
│   ├── analyze_side_by_side.py
│   ├── moca_validity.py
│   ├── export_exact_results.py
│   ├── gridsearch.py
│   ├── gridsearch_ml.py
│   ├── survey_bootstrap.py
│   ├── causal_inference.py
│   └── correlation_analysis.py
├── data/                                  # Master CSV datasets
│   ├── master_cgm_moca_dataset.csv
│   └── master_extended_dataset.csv
└── reports/                               # Stratified report outputs by flow & generation phase
    ├── 1_baseline_replication/            # Phase 1: Baseline statistical replication & validation
    │   ├── report.md
    │   ├── report_side_by_side.md
    │   ├── moca_validity_results.md
    │   ├── comparison_results.md
    │   ├── gridsearch_results.txt
    │   ├── regression_results_total_moca.csv
    │   └── regression_results_specific_impairments.csv
    └── 2_advanced_causal_and_survey/      # Phase 2: Advanced econometrics, survey & correlation
        ├── survey_bootstrap_results.md
        ├── causal_inference_results.md
        ├── correlation_results.md
        ├── analysis_implications_summary.md
        └── statistical_tests_and_logic_guide.md
```

---

## Order of Execution

To fully replicate the setup and run the validation scripts, run the scripts in `src/` in this order:

### Phase 1: Baseline Statistical Replication

1. **[`src/extract_data.py`](src/extract_data.py)**
   - **What it does**: Parses raw AI-READI clinical data (`participants.tsv`, `measurement.csv`, `condition_occurrence.csv`, `observation.csv`) and Dexcom G6 CGM JSON files.
   - **Expected Output**: [`data/master_cgm_moca_dataset.csv`](data/master_cgm_moca_dataset.csv).

2. **[`src/analyze_side_by_side.py`](src/analyze_side_by_side.py)**
   - **What it does**: Direct side-by-side multivariable comparison of GMI vs HbA1c.
   - **Expected Output**: [`reports/1_baseline_replication/report_side_by_side.md`](reports/1_baseline_replication/report_side_by_side.md).

3. **[`src/moca_validity.py`](src/moca_validity.py)**
   - **What it does**: Evaluates MoCA construct validity using permutation bootstrap tests.
   - **Expected Output**: [`reports/1_baseline_replication/moca_validity_results.md`](reports/1_baseline_replication/moca_validity_results.md).

4. **[`src/export_exact_results.py`](src/export_exact_results.py)**
   - **What it does**: Exports unrounded regression coefficients, standard errors, Odds Ratios, and p-values to CSV.
   - **Expected Outputs (CSVs)**: 
     - [`reports/1_baseline_replication/regression_results_total_moca.csv`](reports/1_baseline_replication/regression_results_total_moca.csv)
     - [`reports/1_baseline_replication/regression_results_specific_impairments.csv`](reports/1_baseline_replication/regression_results_specific_impairments.csv)

### Phase 2: Advanced Econometric, Survey, & Correlation Analysis

5. **[`src/extract_extended_data.py`](src/extract_extended_data.py)**
   - **What it does**: Extracts survey data (depression, diet, smoking, alcohol, vape, vision care) into master extended dataset.
   - **Expected Output**: [`data/master_extended_dataset.csv`](data/master_extended_dataset.csv).

6. **[`src/survey_bootstrap.py`](src/survey_bootstrap.py)**
   - **What it does**: 10,000-iteration permutation test evaluating lifestyle factors against MoCA scores.
   - **Expected Output**: [`reports/2_advanced_causal_and_survey/survey_bootstrap_results.md`](reports/2_advanced_causal_and_survey/survey_bootstrap_results.md).

7. **[`src/causal_inference.py`](src/causal_inference.py)**
   - **What it does**: FWL partialling out, Fixed Effects, Propensity Score Matching (PSM), and Instrumental Variables (2SLS).
   - **Expected Output**: [`reports/2_advanced_causal_and_survey/causal_inference_results.md`](reports/2_advanced_causal_and_survey/causal_inference_results.md).

8. **[`src/correlation_analysis.py`](src/correlation_analysis.py)**
   - **What it does**: Computes Pearson ($r$) and Spearman ($\rho$) correlations for MoCA vs HbA1c and Mean Glucose.
   - **Expected Output**: [`reports/2_advanced_causal_and_survey/correlation_results.md`](reports/2_advanced_causal_and_survey/correlation_results.md).

---

## Generated Reports Summary

| Phase | Report File | Generated By | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **[`reports/1_baseline_replication/report.md`](reports/1_baseline_replication/report.md)** | `src/analyze_data.py` | Baseline statistical replication using GMI instead of HbA1c. |
| **Phase 1** | **[`reports/1_baseline_replication/report_side_by_side.md`](reports/1_baseline_replication/report_side_by_side.md)** | `src/analyze_side_by_side.py` | Direct multivariable comparison of GMI vs HbA1c side-by-side. |
| **Phase 1** | **[`reports/1_baseline_replication/moca_validity_results.md`](reports/1_baseline_replication/moca_validity_results.md)** | `src/moca_validity.py` | Cohort definition comparison (AI-READI Strings vs Exhaustive OMOP). |
| **Phase 1** | **[`reports/1_baseline_replication/comparison_results.md`](reports/1_baseline_replication/comparison_results.md)** | `src/gridsearch_ml.py` | Machine Learning GridSearch comparing predictive power of all metrics. |
| **Phase 1** | **[`reports/1_baseline_replication/regression_results_total_moca.csv`](reports/1_baseline_replication/regression_results_total_moca.csv)** <br> **[`reports/1_baseline_replication/regression_results_specific_impairments.csv`](reports/1_baseline_replication/regression_results_specific_impairments.csv)** | `src/export_exact_results.py` | Raw regression coefficients, standard errors, p-values, and 95% CIs. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/survey_bootstrap_results.md`](reports/2_advanced_causal_and_survey/survey_bootstrap_results.md)** | `src/survey_bootstrap.py` | 10,000-iter MoCA permutation test for survey factors. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/causal_inference_results.md`](reports/2_advanced_causal_and_survey/causal_inference_results.md)** | `src/causal_inference.py` | FWL, Fixed Effects, PSM, and Instrumental Variables. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/correlation_results.md`](reports/2_advanced_causal_and_survey/correlation_results.md)** | `src/correlation_analysis.py` | Pearson/Spearman correlation for MoCA and Glucose metrics. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/analysis_implications_summary.md`](reports/2_advanced_causal_and_survey/analysis_implications_summary.md)** | Manual synthesis | Scientific summary of Phase 2 findings and implications. |
| **Phase 2** | **[`reports/2_advanced_causal_and_survey/statistical_tests_and_logic_guide.md`](reports/2_advanced_causal_and_survey/statistical_tests_and_logic_guide.md)** | Manual guide | Comprehensive variable definitions, symbol guide, and test logic walkthrough. |

---

## Documentation & Methodology

Refer to the following analytical reports located in `docs/`:

- **[`docs/comprehensive_replication_guide.md`](docs/comprehensive_replication_guide.md)**: End-to-end guide detailing data acquisition, cleaning pipelines, and step-by-step statistical replication.
- **[`docs/stratification_details.md`](docs/stratification_details.md)**: Details precisely how cohorts were grouped, how outcome variables were separated, and how covariates were adjusted.
- **[`docs/cgm_vs_hba1c_holistic_comparison.md`](docs/cgm_vs_hba1c_holistic_comparison.md)**: A comprehensive, ground-up comparison of how CGM (GMI/TIR) compares to HbA1c in predicting cognitive impairment.
- **[`docs/analysis_implications_summary.md`](docs/analysis_implications_summary.md)**: A plain-english summary of analytical outputs from advanced econometric, correlation, and survey permutation tests.
