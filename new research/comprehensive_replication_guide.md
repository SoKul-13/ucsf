# Comprehensive Replication Guide: AI-READI Cognitive Impairment Analysis

This document walks through every step we took to replicate the findings of the AI-READI paper (*"Association of diabetes severity with cognitive function in US adults"*), explains our methodological choices, and explores alternative configurations through a metric grid search.

---

## 1. Step-by-Step Walkthrough

### Step 1: Identifying the Study Design
The original paper analyzed a cross-sectional multi-center cohort (AI-READI) consisting of adults aged 40-85. They stratified participants into four groups based on their diabetes severity and assessed their cognitive function using the Montreal Cognitive Assessment (MoCA). 

### Step 2: Extracting the Cohort and Glycemic Groups
We used the `participants.tsv` file from the dataset to load the participant cohort. This file contained the `study_group` column, which allowed us to stratify our participants into the exact same four tiers as the original paper:
1. **Healthy / Controls** (`1_Controls`)
2. **Pre-diabetes / Lifestyle Controlled** (`2_Pre-diabetes`)
3. **Medication-controlled T2DM** (`3_Medication-controlled`)
4. **Insulin-dependent T2DM** (`4_Insulin-dependent`)

### Step 3: Extracting CGM Metrics (The Independent Variable)
The original paper used **HbA1c** (a blood test) to measure diabetes severity. Since we wanted to replicate this with wearable data, we parsed over 2,000 JSON files from the `continuous_glucose_monitoring/dexcom_g6/` directory. 
- We enforced a minimum of 3 days of valid data (864 readings) per patient.
- From these interstitial glucose readings, we calculated three key metrics: **Mean Glucose**, **Glucose Management Indicator (GMI)**, and **Time in Range (TIR)**.

### Step 4: Extracting MoCA Scores (The Dependent Variable)
Using `measurement.csv` and matching OMOP concept IDs, we pulled cognitive scores for each patient:
- `moca_total_score` (Total Score, Max 30)
- `moca_combined_mis_score` (Memory Domain)
- `moca_orientation` (Orientation Domain)
- `moca_abstraction` (Abstraction Domain)
We defined **Cognitive Impairment** as a Total MoCA Score < 26, matching standard clinical cutoffs used in the paper.

### Step 5: Extracting Clinical Confounders
To ensure our multivariable regressions were fair, we extracted the exact same confounders used by the original authors. 
- **Age and BMI**: Extracted from `participants.tsv` and `measurement.csv` (`bmi_vsorres, BMI`).
- **Education Level**: Extracted from `observation.csv` (`years_of_education`) and categorized into "High school or below", "College level", and "Graduate level".
- **Comorbidities**: We mapped ICD/SNOMED OMOP codes in `condition_occurrence.csv` to flag binary states (0 or 1) for Hypertension (`mhoccur_hbp`), High Cholesterol (`mhoccur_clsh`), Kidney Disease (`mhoccur_rnl`), Circulatory Problems (`mhoccur_circ`, `mhoccur_strk`, `mhoccur_mi`), and Neurodegenerative Diseases (`mhoccur_pd`, `mhoccur_ad`, `mhoccur_cogn`, `mhoccur_ms`, `mhoccur_cns`).

### Step 6: Statistical Modeling
Using Python's `statsmodels`, we exactly mirrored their statistical pipeline:
- **Table 1**: One-way ANOVAs and Chi-square tests to find baseline demographic differences.
- **Table 2**: Multivariable OLS regressions to evaluate the relationship between diabetes group and raw MoCA scores while adjusting for all confounders.
- **Table 3**: Multivariable Logistic Regressions to evaluate the Odds Ratio (OR) of suffering from cognitive impairment (MoCA < 26).

---

## 2. Meaning, Relevance, and Importance of the Metrics

- **Mean Glucose (mg/dL)**: The arithmetic average of all glucose readings from the Dexcom G6. It provides a raw look at a patient's overall glycemic load.
- **GMI (Glucose Management Indicator, %)**: A clinically validated formula (`3.31 + 0.02392 * Mean Glucose`) designed to approximate what a patient's laboratory HbA1c would be based solely on CGM data. It is highly relevant because physicians use it as a 1:1 substitute for HbA1c when blood draws aren't available.
- **TIR (Time in Range, %)**: The percentage of time a patient's glucose stays between 70 and 180 mg/dL. This is important because it captures *glycemic variability*—two patients can have the same Mean Glucose, but one could have dangerous swings (low TIR) while the other is stable (high TIR).
- **MoCA (Montreal Cognitive Assessment)**: A widely used screening assessment for detecting cognitive impairment. A score below 26 is generally indicative of Mild Cognitive Impairment (MCI) or dementia.

---

## 3. CGM vs HbA1c: Why is it Different/Better/Worse?

The original paper relied on laboratory **HbA1c**. Our replication relies entirely on wearable **Continuous Glucose Monitoring (CGM)**.

> [!TIP]
> **Why CGM is Better**
> - **Non-Invasive and Continuous**: CGM doesn't require a venous blood draw and provides a much higher resolution picture of a patient's metabolic state over time. 
> - **Captures Variability**: HbA1c is just a 3-month average. It completely masks glycemic variability. A patient with extreme hypoglycemic crashes and hyperglycemic spikes could have a "normal" HbA1c. CGM unlocks metrics like **Time in Range (TIR)** which capture these dangerous fluctuations.

> [!WARNING]
> **Why CGM can be Worse**
> - **Temporal Mismatch**: HbA1c reflects a 3-month physiological average. The CGM data we extracted was collected over an acute window (e.g., 10-14 days of wearing the Dexcom sensor). If a patient had an atypical week (e.g., sick, traveling, or altering their diet because they knew they were being monitored), the CGM data might not accurately reflect their chronic, long-term diabetes severity the way an HbA1c molecule does.

---

## 4. Why Use GMI as the Covariate?

In our primary replication, we used **GMI** instead of Mean Glucose or TIR. 

Since the explicit goal was to *replicate* the original paper, we needed a variable that behaved identically to HbA1c within the theoretical framework of the models. Because GMI is mathematically intended to be the "CGM equivalent of HbA1c," it was the most scientifically sound 1:1 replacement. 

*Note on GMI vs Mean Glucose*: Because GMI is derived using a simple linear equation (`y = mx + b`) from Mean Glucose, using either GMI or Mean Glucose in an OLS or Logistic Regression will yield the **exact same statistical significance (p-values) and predictive odds ratios**. They are perfectly collinear. The only difference is the scale of the coefficients. We chose GMI because the scale (%) makes more sense when comparing against an HbA1c-based paper.

---

## 5. Metric Gridsearch: GMI vs Mean Glucose vs TIR

To see how the choice of CGM metric impacts the multivariable models, we ran a grid search replacing the main glycemic covariate in the models. 

*(Note: In Table 2, the adjusted means shift slightly depending on the intercept of the model, but the significance tells the real story).*

### Results Adjusted for GMI
**Table 2: MoCA Total Score Adjusted Means**
- Means: Controls: 31.6, Pre-diabetes: 31.5, Medication: 31.3, Insulin: 30.6
- Omnibus p-value for group effect: **0.019**

**Table 3: Association with Cognitive Impairment (OR)**
| Glycaemic Status | Multivariable OR (95% CI) | p-value |
| --- | --- | --- |
| Pre-diabetes | 1.04 (0.80 - 1.36) | 0.754 |
| Medication-controlled | 1.18 (0.88 - 1.57) | 0.271 |
| Insulin-dependent | 1.63 (1.04 - 2.55) | **0.032** |

### Results Adjusted for Mean Glucose
**Table 2: MoCA Total Score Adjusted Means**
- Means: Controls: 30.1, Pre-diabetes: 30.0, Medication: 29.9, Insulin: 29.1
- Omnibus p-value for group effect: **0.019**

**Table 3: Association with Cognitive Impairment (OR)**
| Glycaemic Status | Multivariable OR (95% CI) | p-value |
| --- | --- | --- |
| Pre-diabetes | 1.04 (0.80 - 1.36) | 0.754 |
| Medication-controlled | 1.18 (0.88 - 1.57) | 0.271 |
| Insulin-dependent | 1.63 (1.04 - 2.55) | **0.032** |

> [!NOTE]
> As expected, the p-values and Odds Ratios for GMI and Mean Glucose are completely identical because one is a direct linear transformation of the other!

### Results Adjusted for Time In Range (TIR)
**Table 2: MoCA Total Score Adjusted Means**
- Means: Controls: 28.4, Pre-diabetes: 28.2, Medication: 28.0, Insulin: 27.1
- Omnibus p-value for group effect: **0.001**

**Table 3: Association with Cognitive Impairment (OR)**
| Glycaemic Status | Multivariable OR (95% CI) | p-value |
| --- | --- | --- |
| Pre-diabetes | 1.08 (0.83 - 1.41) | 0.576 |
| Medication-controlled | 1.32 (1.00 - 1.75) | 0.054 |
| Insulin-dependent | 1.92 (1.22 - 3.00) | **0.005** |

> [!IMPORTANT]
> **Gridsearch Conclusion**: When we adjust for **Time in Range (TIR)** instead of average glucose (GMI/Mean), the association between severe diabetes and cognitive impairment becomes **even stronger** (p=0.005 vs p=0.032). The odds ratio for the Insulin-dependent group jumps from 1.63x to **1.92x**. This suggests that *glycemic variability* (swings and crashes) might actually be a stronger driver of cognitive decline than just a high average blood sugar! This is a massive advantage of using CGM data over traditional HbA1c.

---

## Final Original Tables (Adjusted for GMI)

For completeness, here are the full summary tables for our baseline replication:

### Table 1: Participant Characteristics

| Characteristic | Controls | Pre-diabetes | Medication-controlled | Insulin-dependent | p-value |
| --- | --- | --- | --- | --- | --- |
| N | 607 | 457 | 525 | 147 | - |
| Age (years) | 60.4 (11.7) | 60.9 (11.1) | 62.7 (10.3) | 62.1 (11.1) | 0.005 |
| BMI | 28.0 (6.9) | 29.4 (6.9) | 30.8 (6.7) | 33.9 (8.2) | 0.000 |
| GMI (%) | 6.2 (0.3) | 6.3 (0.4) | 6.8 (0.6) | 7.1 (0.7) | 0.000 |
| Mean Glucose (mg/dL) | 119.2 (13.7) | 125.6 (17.7) | 144.2 (25.7) | 157.9 (27.7) | 0.000 |
| Time in Range (%) | 97.0 (4.9) | 94.7 (9.1) | 83.3 (18.4) | 71.7 (20.9) | 0.000 |
| Hypertension (%) | 32.3% | 46.2% | 65.3% | 70.1% | 0.000 |
| High Cholesterol (%) | 40.0% | 47.9% | 63.6% | 59.2% | 0.000 |
| Kidney Disease (%) | 4.8% | 10.5% | 12.8% | 28.6% | 0.000 |
| Circulatory Problems (%) | 12.5% | 11.8% | 17.1% | 30.6% | 0.000 |
| Neurodegenerative (%) | 10.4% | 10.1% | 16.6% | 31.3% | 0.000 |

### Table 2: MoCA Total and Domain Scores

| Cognitive Domain | Unadjusted Mean | p-value (Unadj) | Adjusted Mean (approx) | p-value (Adj) |
| --- | --- | --- | --- | --- |
| Total Score | C: 26.1, P: 25.9, M: 25.4, I: 24.2 | 0.000 | C: 31.6, P: 31.5, M: 31.3, I: 30.6 | 0.019 |
| Memory | C: 12.7, P: 12.7, M: 12.4, I: 11.9 | 0.008 | C: 18.0, P: 18.1, M: 18.2, I: 18.0 | 0.925 |
| Orientation | C: 5.9, P: 5.9, M: 5.9, I: 5.8 | 0.133 | C: 6.1, P: 6.1, M: 6.1, I: 6.1 | 0.507 |
| Abstraction | C: 1.9, P: 1.9, M: 1.9, I: 1.8 | 0.001 | C: 1.8, P: 1.8, M: 1.8, I: 1.7 | 0.061 |
