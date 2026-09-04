# Folder 5: Multimodal CGM Regression & Comparative Analysis Reports

This directory contains the full suite of multimodal continuous glucose monitoring (CGM) regression analyses, head-to-head biomarker evaluations against static HbA1c, econometric prediction tables, and methodological execution logs across $N = 1,743$ participants in the UCSF / AI-READI cohort.

---

## 📂 File Layout & Directory Navigation

```
new research/reports/5_multimodal_cgm_analysis/
├── README.md                                                 <- [This file] Directory navigation & summary index
├── 01_executive_summary_multimodal_cgm_comorbidity_analysis.md <- Executive summary report of multimodal CGM relationships
├── 02_cgm_vs_hba1c_head_to_head_comparative_analysis.md       <- Dedicated head-to-head comparison: CGM vs. HbA1c performance & collinearity
├── 03_full_econometric_regression_prediction_tables.md         <- Complete 17-outcome econometric regression tables & detailed 3-part breakdowns
├── 04_execution_and_methodology_detailed_log.md               <- Technical execution log, dataset schema, and methodology audit
└── data/                                                      <- Clean machine-readable CSV datasets
    ├── master_multimodal_cgm_head_to_head_summary.csv        <- Head-to-head performance matrix CSV
    └── multimodal_regression_results_detailed.csv             <- Full regression parameter CSV (all terms, SEs, p-values)
```

---

## 📑 File Summaries & Key Research Questions Answered

### 1. [`01_executive_summary_multimodal_cgm_comorbidity_analysis.md`](./01_executive_summary_multimodal_cgm_comorbidity_analysis.md)
- **Purpose**: High-level executive synthesis of CGM metric predictive performance across Cognition, Depression, Indoor Environment Sensors, and Wearable Activity.
- **Key Focus**: Summary of statistical significance, forest plot key takeaways, and clinical implications.

### 2. [`02_cgm_vs_hba1c_head_to_head_comparative_analysis.md`](./02_cgm_vs_hba1c_head_to_head_comparative_analysis.md)
- **Purpose**: Dedicated scientific evaluation answering: *"Since HbA1c and CGM mean glucose are collinear, how do they compare under identical conditions? Which biomarker is superior for each outcome, and why?"*
- **Key Findings**:
  - **CGM Dominates Cognition & Autonomic Wearables**: For `moca_total`, `cognitive_impairment`, `wearable_stress_mean`, `wearable_hr_mean`, and `env_pm25_mean`, CGM continuous features outcompete and absorb static HbA1c completely (HbA1c becomes non-significant at $p > 0.53$, while CGM remains $p < 0.0001$).
  - **HbA1c Dominates Active Calories**: For `wearable_active_calories`, HbA1c outcompetes CGM ($p = 0.0090$ vs CGM $p = 0.6693$).
  - **Dual Complementary**: For `env_hum_mean`, both are complementary ($p < 0.05$).
  - **Neither Significant**: For `depression_score` and `high_depression`, neither glycemic metric adds incremental value beyond demographic factors and SDOH ($p > 0.31$).

### 3. [`03_full_econometric_regression_prediction_tables.md`](./03_full_econometric_regression_prediction_tables.md)
- **Purpose**: Comprehensive statistical report formatted in Phase 4 style. Includes equations, full regression tables (Estimates, SE, 95% CIs, $t/z$-statistics, $p$-values, $R^2$, AUC, F1, Brier, AIC), 3-part detailed analytical commentary under **every table**, and a Master Synthesis & Citation Matrix.

### 4. [`04_execution_and_methodology_detailed_log.md`](./04_execution_and_methodology_detailed_log.md)
- **Purpose**: Step-by-step pipeline audit detailing data cleaning, demographic balance, missing value handling, regression specifications, and Python script generation logs.

---

## 📊 Data Directory

- [`data/master_multimodal_cgm_head_to_head_summary.csv`](./data/master_multimodal_cgm_head_to_head_summary.csv): Machine-readable CSV table containing model fit metrics ($R^2$ / AUC) for Model 1A (HbA1c Only), Model 1B (CGM Features Only), and Model 1C (Combined Model), along with Likelihood Ratio Test $p$-values and head-to-head winners for all 17 targets.
- [`data/multimodal_regression_results_detailed.csv`](./data/multimodal_regression_results_detailed.csv): Un-aggregated CSV containing every regression term, coefficient, standard error, $z/t$-statistic, and $p$-value across all 51 fitted models (17 outcomes $\times$ 3 model specifications).


---

## 🔬 Research report series (`research_report_*.md`)

A second, fully re-derived analysis lives alongside the files above. It rebuilds the master dataset from the full raw files (all environmental-sensor rows, site-local time, wear-day filtering, duplicate-interval removal), uses the four pre-specified CGM metrics (mean glucose, mean/SD, average daily TIR 70-180, average daily SD) with the 54/70/180/250 mg/dL categories, and fits every specification on one identical sample per outcome.

| File | Contents |
| :--- | :--- |
| [`research_report_01_cgm_vs_hba1c_comorbidity_prediction.md`](./research_report_01_cgm_vs_hba1c_comorbidity_prediction.md) | Main narrative report (abstract, background, methods, results by domain, discussion, limitations, references) |
| [`research_report_02_full_regression_tables.md`](./research_report_02_full_regression_tables.md) | Table 1, predictor correlations, FDR-controlled families, every specification for every primary outcome |
| [`research_report_03_sensitivity_and_exploratory_tables.md`](./research_report_03_sensitivity_and_exploratory_tables.md) | Sensitivity samples, exploratory outcomes, 11-metric CGM sweep |
| [`research_report_04_data_dictionary_and_methods_log.md`](./research_report_04_data_dictionary_and_methods_log.md) | Variable dictionary, extraction rules, statistical procedures, commands |
| [`research_report_05_followups_parsimony_discordance_replication.md`](./research_report_05_followups_parsimony_discordance_replication.md) | Follow-ups: parsimonious CGM pair, HbA1c-CGM discordance (HGI), split-sample depression replication, splines, split-half stability (`data/followup_*.csv`, `figures/fig7-fig10`) |
| `data/*.csv` | `primary_slope_tests_with_fdr.csv`, `primary_incremental_tests_with_fdr.csv`, `primary_single_cgm_beyond_hba1c_with_fdr.csv`, `model_fit_all_specs.csv`, `slope_tests_all_specs.csv`, `nested_tests_all.csv`, `head_to_head_hba1c_vs_cgm.csv`, `diabetes_stratified_slopes.csv`, `nonlinearity_quadratic_tests.csv`, `partial_spearman_correlations.csv`, `vif_combined_model.csv`, `exploratory_cgm_metric_sweep_with_fdr.csv`, `table1_descriptives_by_diabetes_status.csv`, `analysis_base_sample.csv`, `coverage.json` |
| `figures/fig1-fig6` | Forest plot, nested-test heatmap, cross-validated performance, predictor correlations, diabetes-stratified slopes, sample flow |

Generated by `src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py` → `run_multimodal_cgm_models.py` → `generate_reports.py` → `run_phase5_followups.py`.
