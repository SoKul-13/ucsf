# MoCA Validity Analysis: Comparison of Cohort Definitions

## Understanding This Report
- **Condition N**: Number of unique patients identified as having a cognitive or neurodegenerative disease (e.g., Alzheimer's, Parkinson's).
- **No Condition N**: Number of unique patients without a documented cognitive disease.
- **Mean MoCA**: The average MoCA Total Score (`moca_total`) for the respective group. Lower scores indicate worse cognitive function (Maximum 30, Impairment < 26).
- **Permutation P-value (1-sided)**: We are testing the hypothesis that patients *without* the condition have significantly *higher* MoCA scores than patients *with* the condition. A significant p-value (p < 0.05 ⭐) proves that MoCA accurately reflects cognitive decline in that specific sub-population.

### Cohort Extraction Results
- AI-READI Strings (`has_cog_disease_ai_readi`) identified 242 patients with MoCA data.
- Exhaustive OMOP Concepts (`has_cog_disease_exhaustive`) identified 9 patients with MoCA data.


# Version A: AI-READI Specific (mhoccur strings)

| Stratification | Condition N | Mean MoCA (Cond) | No Condition N | Mean MoCA (No Cond) | P-value (1-sided) | Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Overall** | 242 | 25.14 | 1494 | 25.80 | **0.0015** ⭐ | Significant (Valid MoCA) |
| **By Age** | - | - | - | - | - | - |
| Below Median Age | 104 | 25.06 | 792 | 26.21 | **<0.001** ⭐ | Significant (Valid MoCA) |
| Above Median Age | 138 | 25.20 | 702 | 25.33 | 0.3323 | Not Significant |
| **By Diabetes Status** | - | - | - | - | - | - |
| 1_Controls | 63 | 25.43 | 544 | 26.20 | **0.0212** ⭐ | Significant (Valid MoCA) |
| 2_Pre-diabetes | 46 | 26.00 | 411 | 25.94 | 0.5497 | Not Significant |
| 3_Medication-controlled | 87 | 25.06 | 438 | 25.53 | 0.1096 | Not Significant |
| 4_Insulin-dependent | 46 | 24.02 | 101 | 24.29 | 0.3651 | Not Significant |
| **By Age and Diabetes Status** | - | - | - | - | - | - |
| 1_Controls - Below Median Age | 30 | 25.90 | 306 | 26.67 | 0.0617 | Not Significant |
| 1_Controls - Above Median Age | 33 | 25.00 | 238 | 25.60 | 0.1356 | Not Significant |
| 2_Pre-diabetes - Below Median Age | 21 | 26.19 | 218 | 26.25 | 0.4659 | Not Significant |
| 2_Pre-diabetes - Above Median Age | 25 | 25.84 | 193 | 25.59 | 0.6516 | Not Significant |
| 3_Medication-controlled - Below Median Age | 36 | 24.89 | 216 | 26.06 | **0.0154** ⭐ | Significant (Valid MoCA) |
| 3_Medication-controlled - Above Median Age | 51 | 25.18 | 222 | 25.00 | 0.6325 | Not Significant |
| 4_Insulin-dependent - Below Median Age | 17 | 22.53 | 52 | 24.02 | 0.1385 | Not Significant |
| 4_Insulin-dependent - Above Median Age | 29 | 24.90 | 49 | 24.57 | 0.6599 | Not Significant |

---


# Version B: Exhaustive OMOP Concept IDs

| Stratification | Condition N | Mean MoCA (Cond) | No Condition N | Mean MoCA (No Cond) | P-value (1-sided) | Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Overall** | 9 | 23.44 | 1727 | 25.72 | **0.0231** ⭐ | Significant (Valid MoCA) |
| **By Age** | - | - | - | - | - | - |
| Below Median Age | 2 | 23.50 | 894 | 26.09 | 0.1388 | Not Significant |
| Above Median Age | 7 | 23.43 | 833 | 25.33 | 0.0723 | Not Significant |
| **By Diabetes Status** | - | - | - | - | - | - |
| 1_Controls | 4 | 22.75 | 603 | 26.14 | **0.0173** ⭐ | Significant (Valid MoCA) |
| 2_Pre-diabetes | 0 | N/A | 457 | N/A | NaN | N/A |
| 3_Medication-controlled | 4 | 23.00 | 521 | 25.47 | 0.0797 | Not Significant |
| 4_Insulin-dependent | 1 | N/A | 146 | N/A | NaN | N/A |
| **By Age and Diabetes Status** | - | - | - | - | - | - |
| 1_Controls - Below Median Age | 1 | N/A | 335 | N/A | NaN | N/A |
| 1_Controls - Above Median Age | 3 | 23.67 | 268 | 25.54 | 0.1577 | Not Significant |
| 2_Pre-diabetes - Below Median Age | 0 | N/A | 239 | N/A | NaN | N/A |
| 2_Pre-diabetes - Above Median Age | 0 | N/A | 218 | N/A | NaN | N/A |
| 3_Medication-controlled - Below Median Age | 1 | N/A | 251 | N/A | NaN | N/A |
| 3_Medication-controlled - Above Median Age | 3 | 21.67 | 270 | 25.07 | 0.0575 | Not Significant |
| 4_Insulin-dependent - Below Median Age | 0 | N/A | 69 | N/A | NaN | N/A |
| 4_Insulin-dependent - Above Median Age | 1 | N/A | 77 | N/A | NaN | N/A |