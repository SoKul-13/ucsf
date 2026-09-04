# Technical Execution & Methodology Blueprint
## Detailed Step-by-Step Log of Data Sources, Code Architecture, Statistical Derivations, and File Paths

---

## 1. File & Directory Layout — Where Everything Lives

All project scripts, master datasets, reports, and visual plot graphics are organized under the `new research/` module:

```
ucsf/
├── README.md                                    # Root repository index & 5-phase execution guide
└── new research/
    ├── README.md                                # Detailed module index & execution guide
    ├── data/
    │   ├── master_cgm_moca_dataset.csv          # Clinical EHR & CGM baseline dataset (N=2,226)
    │   └── master_multimodal_dataset.csv        # Master merged multimodal dataset (N=1,743, 38 features)
    ├── src/
    │   └── 5_multimodal_cgm_analysis/           # Phase 5 Source Code Directory
    │       ├── extract_multimodal_dataset.py    # Multimodal feature extraction & merging engine
    │       └── run_multimodal_cgm_models.py     # 3-nested specification regression & LRT engine
    └── reports/
        └── 5_multimodal_cgm_analysis/           # Phase 5 Output Reports Directory
            ├── multimodal_cgm_comorbidity_analysis_report.md # Main report in Dylan's format
            └── execution_and_methodology_detailed_log.md    # This technical execution blueprint
```

#### Visual Artifacts Location
Generated high-resolution plot PNGs are stored in the active session artifact directory:
- **$R^2$ Model Performance Comparison**: [`cgm_vs_hba1c_r2_comparison.png`](file:///Users/guardian/.gemini/antigravity-ide/brain/bb7fe048-a70e-4c78-b615-b2ae9a610620/cgm_vs_hba1c_r2_comparison.png)
- **Likelihood Ratio Test (LRT) Incremental Value Bar Chart**: [`lrt_incremental_value_heatmap.png`](file:///Users/guardian/.gemini/antigravity-ide/brain/bb7fe048-a70e-4c78-b615-b2ae9a610620/lrt_incremental_value_heatmap.png)
- **Forest Plot of Standardized Effects**: [`cgm_predictor_forest_plot.png`](file:///Users/guardian/.gemini/antigravity-ide/brain/bb7fe048-a70e-4c78-b615-b2ae9a610620/cgm_predictor_forest_plot.png)

---

## 2. Data Sources & Extraction Logic — How Data Was Processed

### 2a. Dexcom G6 Continuous Glucose Monitoring (CGM) Streams
- **Source**: `dataset/wearable_blood_glucose/continuous_glucose_monitoring/dexcom_g6/`
- **Parsing Engine**: [`extract_data.py`](file:///Users/guardian/Documents/GitHub/bcc/ucsf/new%20research/src/1_baseline_replication/extract_data.py)
- **Quality Filtering**: Minimum 3 days of valid 5-minute readings ($\ge 864$ readings per participant).
- **5 Standardized Glucose Level Cutoffs**:
  1. **Severe Hypoglycaemia (`<54` mg/dL strict)**:
     $$\text{pct\_severe\_hypo} = \frac{\sum \mathbb{I}(v_i < 54.0)}{N_{\text{total}}} \times 100$$
  2. **Moderate Hypoglycaemia (`54–69` mg/dL inclusive)**:
     $$\text{pct\_mod\_hypo} = \frac{\sum \mathbb{I}(54.0 \le v_i \le 69.0)}{N_{\text{total}}} \times 100$$
  3. **Normal / Time in Range (`70–180` mg/dL inclusive)**:
     $$\text{tir} = \frac{\sum \mathbb{I}(70.0 \le v_i \le 180.0)}{N_{\text{total}}} \times 100$$
     *Note: Shifted to 180 mg/dL threshold from earlier 140 mg/dL cutoff.*
  4. **Moderate Hyperglycaemia (`181–250` mg/dL inclusive)**:
     $$\text{pct\_mod\_hyper} = \frac{\sum \mathbb{I}(181.0 \le v_i \le 250.0)}{N_{\text{total}}} \times 100$$
  5. **Severe Hyperglycaemia (`>250` mg/dL strict)**:
     $$\text{pct\_severe\_hyper} = \frac{\sum \mathbb{I}(v_i > 250.0)}{N_{\text{total}}} \times 100$$
- **Core Summary Metrics**:
  - `mean_glucose`: $\bar{v} = \frac{1}{N} \sum_{i=1}^N v_i$
  - `glucose_sd`: $\sigma_v = \sqrt{\frac{1}{N} \sum_{i=1}^N (v_i - \bar{v})^2}$
  - `mean_to_sd_ratio`: $\frac{\bar{v}}{\sigma_v}$

### 2b. Indoor Environmental Sensor Streams (LeeLab Anura)
- **Source**: `dataset/environment/environmental_sensor/leelab_anura/`
- **Parsing Engine**: [`extract_multimodal_dataset.py`](file:///Users/guardian/Documents/GitHub/bcc/ucsf/new%20research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py) (`parse_single_env_folder`)
- **Methodology**: Multiprocessing pool (`ProcessPoolExecutor(max_workers=8)`). Reads up to 20,000 intraday readings per participant to aggregate 14-day mean exposure levels:
  - `env_temp_mean` & `env_hum_mean`: Ambient temperature (°C/F) and relative humidity (%).
  - `env_pm25_mean` & `env_pm10_mean`: Fine (PM2.5) and coarse (PM10) particulate matter concentration (µg/m³).
  - `env_voc_mean` & `env_nox_mean`: Volatile Organic Compounds and Nitrogen Oxides sensor indices.

### 2c. Wearable Activity Tracker (Garmin Vivosmart 5)
- **Source**: `dataset/wearable_activity_monitor/` (`physical_activity`, `physical_activity_calorie`, `stress`, `heart_rate`)
- **Parsing Engine**: [`extract_multimodal_dataset.py`](file:///Users/guardian/Documents/GitHub/bcc/ucsf/new%20research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py) (`parse_single_wearable_pid`)
- **Metrics Extracted**:
  - `wearable_daily_steps`: Total base movement quantity scaled to daily step averages ($\text{total\_steps} / (\text{readings\_count} / 288.0)$).
  - `wearable_active_calories`: Sum of caloric expenditure.
  - `wearable_stress_mean`: Mean Garmin stress score (range 0–100).
  - `wearable_hr_mean`: Mean resting/active heart rate (bpm).

### 2d. Clinical EHR & Survey Observation Data
- **Source**: `dataset/clinical_data/observation.csv` & `measurement.csv`
- **Extraction Engine**: [`extract_multimodal_dataset.py`](file:///Users/guardian/Documents/GitHub/bcc/ucsf/new%20research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py) (`extract_survey_metrics`)
- **Extracted Fields**:
  - `moca_total`, `moca_memory`, `moca_orientation`, `moca_abstraction`: MoCA sub-scores.
  - `cognitive_impairment`: Binary indicator $\mathbb{I}(\text{MoCA} < 26)$.
  - `depression_score`: CES-D-10 sum score (`cestl` observation source value).
  - `high_depression`: Binary indicator $\mathbb{I}(\text{CESD-10} \ge 10)$.
  - `hba1c`: Laboratory HbA1c percentage (%) (OMOP concept ID `4184637`).

---

## 3. Mathematical & Statistical Methodology — How Models Were Evaluated

For every outcome $Y_i$, three nested regression models were estimated adjusting for standard covariates:
$$\mathbf{X}_{\text{cov}} = \text{Age} + \text{BMI} + \text{Education Level} + \text{Hypertension} + \text{High Cholesterol} + \text{Kidney Disease} + \text{Circulatory Problems}$$

### 3a. Model Specifications
1. **Model 1 (HbA1c Only)**:
   $$Y_i = \beta_0 + \beta_1 \cdot \text{HbA1c}_i + \boldsymbol{\gamma}' \mathbf{X}_{\text{cov},i} + \epsilon_i$$
2. **Model 2 (CGM Features Only)**:
   $$Y_i = \beta_0 + \beta_2 \cdot \text{Mean}_i + \beta_3 \cdot \text{SD}_i + \beta_4 \cdot \left(\frac{\text{Mean}}{\text{SD}}\right)_i + \beta_5 \cdot \text{TIR}_{70\text{--}180, i} + \boldsymbol{\gamma}' \mathbf{X}_{\text{cov},i} + \epsilon_i$$
3. **Model 3 (Combined Model)**:
   $$Y_i = \beta_0 + \beta_1 \cdot \text{HbA1c}_i + \beta_2 \cdot \text{Mean}_i + \beta_3 \cdot \text{SD}_i + \beta_4 \cdot \left(\frac{\text{Mean}}{\text{SD}}\right)_i + \beta_5 \cdot \text{TIR}_{70\text{--}180, i} + \boldsymbol{\gamma}' \mathbf{X}_{\text{cov},i} + \epsilon_i$$

### 3b. Linear Regression (OLS) for Continuous Targets
Fitted using `statsmodels.formula.api.ols`.
- **Parameter Slopes ($\beta_j$)**: $\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1} \mathbf{X}' \mathbf{y}$
- **Standard Errors ($\text{SE}(\hat{\beta}_j)$)**: $\sqrt{s^2 (\mathbf{X}'\mathbf{X})^{-1}_{jj}}$
- **Test Statistic ($t$-score)**: $t = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)} \sim t_{N - K}$
- **Model Fit ($R^2$ & Adj $R^2$)**:
  $$R^2 = 1 - \frac{\text{SSR}}{\text{SST}}, \quad R^2_{\text{adj}} = 1 - (1 - R^2) \frac{N - 1}{N - K}$$
- **Akaike Information Criterion (AIC)**: $\text{AIC} = 2K - 2\ell(\hat{\boldsymbol{\beta}})$

### 3c. Logistic Regression (GLM Binomial) for Binary Targets
Fitted using `statsmodels.formula.api.glm` with `family=sm.families.Binomial()`.
- **Log-Odds Model**: $\ln \left( \frac{P(Y_i = 1)}{1 - P(Y_i = 1)} \right) = \beta_0 + \mathbf{x}_i' \boldsymbol{\beta}$
- **Odds Ratio ($\text{OR}$)**: $\text{OR}_j = e^{\hat{\beta}_j}$
- **95% Confidence Interval for $\text{OR}$**: $[ e^{\hat{\beta}_j - 1.96 \cdot \text{SE}}, \; e^{\hat{\beta}_j + 1.96 \cdot \text{SE}} ]$
- **Wald Test Statistic ($z$-score)**: $z = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)} \sim \mathcal{N}(0, 1)$
- **Discriminative Power**: Receiver Operating Characteristic Area Under Curve (ROC-AUC) evaluated via `sklearn.metrics.roc_auc_score`.

### 3d. Likelihood Ratio Tests (LRT) for Incremental Value & Redundancy
To evaluate whether Model 3 (full) significantly improves model fit over Model 1 or Model 2 (reduced):
- **LRT Test Statistic ($\chi^2$)**:
  $$\text{LRT} = 2 \left( \ell_{\text{full}} - \ell_{\text{reduced}} \right)$$
  where $\ell$ is the unconstrained log-likelihood of the model.
- **Degrees of Freedom ($\Delta k$)**:
  - Incremental Value of CGM over HbA1c (Model 3 vs Model 1): $\Delta k = 4$ (`mean_glucose`, `glucose_sd`, `mean_to_sd_ratio`, `tir`).
  - Redundancy of HbA1c given CGM (Model 3 vs Model 2): $\Delta k = 1$ (`hba1c`).
- **$p$-value Calculation**: $p = \text{SF}_{\chi^2}(\text{LRT}, \Delta k) = 1 - F_{\chi^2}(\text{LRT}, \Delta k)$.

---

## 4. Execution Sequence & Commands Run

To reproduce the analysis from scratch, execute the following commands in order:

```bash
# 1. Activate python environment
source "new research/.venv/bin/activate"

# 2. Extract multimodal dataset (merging EHR, Dexcom G6, LeeLab Anura, Garmin Vivosmart 5)
python3 "new research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py"
# Output: new research/data/master_multimodal_dataset.csv (1,743 rows x 38 columns)

# 3. Fit 3-nested regression specifications & compute LRT likelihood ratio tests
python3 "new research/src/5_multimodal_cgm_analysis/run_multimodal_cgm_models.py"
# Output: new research/reports/5_multimodal_cgm_analysis/multimodal_cgm_comorbidity_analysis_report.md

# 4. Generate visual summary plots (R^2 comparison, forest plots, LRT heatmap)
python3 "/Users/guardian/.gemini/antigravity-ide/brain/bb7fe048-a70e-4c78-b615-b2ae9a610620/scratch/generate_visual_plots.py"
# Outputs:
# - cgm_vs_hba1c_r2_comparison.png
# - cgm_predictor_forest_plot.png
# - lrt_incremental_value_heatmap.png
```

---

## 5. Summary of Outputs & Verification Status

- **`multimodal_cgm_comorbidity_analysis_report.md`**: Main outcome prediction report formatted in Dylan's exact structure, detailing all empirical statistics, 5 glucose cutoff bands, and domain findings.
- **`execution_and_methodology_detailed_log.md`**: Complete technical execution log (this document) detailing file paths, data sources, code architecture, mathematical formulas, and command lines.
- **Visual Plots**: 3 high-resolution publication-quality PNG charts generated and embedded into project artifacts.
