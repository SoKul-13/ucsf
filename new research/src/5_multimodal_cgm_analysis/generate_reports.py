"""
Phase 5 - report generator
==========================
Turns the CSV outputs of `run_multimodal_cgm_models.py` into Markdown tables:

  reports/5_multimodal_cgm_analysis/research_report_02_full_regression_tables.md   (all specifications, all outcomes)
  reports/5_multimodal_cgm_analysis/research_report_03_sensitivity_and_exploratory_tables.md
  reports/5_multimodal_cgm_analysis/research_report_04_data_dictionary_and_methods_log.md

The narrative research report (research_report_01_*.md) is written separately and cites these tables.
"""

import os
import json
import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
REPORT_DIR = os.path.join(PROJECT_ROOT, "reports", "5_multimodal_cgm_analysis")
D = os.path.join(REPORT_DIR, "data")

from run_multimodal_cgm_models import CORE_CGM, EXPLORATORY_CGM, HBA1C, PRED_LABEL, OUTCOMES, EXPLORATORY_OUTCOMES  # noqa: E402

SPEC_LABEL = {"M0": "M0: covariates only", "M1": "M1: + HbA1c", "M2": "M2: + 4 CGM metrics",
              "M3": "M3: + HbA1c + 4 CGM metrics"}
for k, lab in CORE_CGM.items():
    SPEC_LABEL[f"M2_{k}"] = f"M2[{lab}]: + {lab}"
    SPEC_LABEL[f"M3_{k}"] = f"M3[{lab}]: + HbA1c + {lab}"
SAMPLE_LABEL = {"primary": "Primary analysis sample", "cgm_ge7_days": "Sensitivity: >= 7 valid CGM days",
                "no_insulin": "Sensitivity: insulin users excluded", "diabetes_only": "Sensitivity: type 2 diabetes only",
                "no_diabetes_only": "Sensitivity: no diabetes / pre-diabetes only",
                "exploratory_outcome": "Exploratory outcome"}


def fmt_p(p):
    if pd.isna(p):
        return "-"
    if p < 0.001:
        return f"{p:.1e}"
    return f"{p:.3f}"


def stars(p):
    return "" if pd.isna(p) else ("***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "")


def md_table(df, cols, headers=None, align=None):
    headers = headers or cols
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join(align or [":---"] + [":---:"] * (len(cols) - 1)) + " |"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(str(r[c]) for c in cols) + " |")
    return "\n".join(out)


def load():
    g = lambda n: pd.read_csv(os.path.join(D, n)) if os.path.exists(os.path.join(D, n)) else pd.DataFrame()
    return {
        "fit": g("model_fit_all_specs.csv"), "slopes": g("slope_tests_all_specs.csv"),
        "nested": g("nested_tests_all.csv"), "h2h": g("head_to_head_hba1c_vs_cgm.csv"),
        "vif": g("vif_combined_model.csv"), "partial": g("partial_spearman_correlations.csv"),
        "nonlin": g("nonlinearity_quadratic_tests.csv"), "strat": g("diabetes_stratified_slopes.csv"),
        "fam": g("primary_slope_tests_with_fdr.csv"), "fam2": g("primary_incremental_tests_with_fdr.csv"),
        "fam3": g("primary_single_cgm_beyond_hba1c_with_fdr.csv"), "expl": g("exploratory_cgm_metric_sweep_with_fdr.csv"),
        "t1": g("table1_descriptives_by_diabetes_status.csv"), "corr": pd.read_csv(os.path.join(D, "predictor_spearman_correlations.csv"), index_col=0),
        "cov": json.load(open(os.path.join(D, "coverage.json"))), "summary": g("outcome_summary.csv"),
    }


# --------------------------------------------------------------------------------------
def outcome_block(R, y, sample, fdr_lookup=None):
    fit = R["fit"]; fit = fit[(fit["outcome"] == y) & (fit["sample"] == sample)]
    sl = R["slopes"]; sl = sl[(sl["outcome"] == y) & (sl["sample"] == sample)]
    ne = R["nested"]; ne = ne[(ne["outcome"] == y) & (ne["sample"] == sample)]
    h2 = R["h2h"]; h2 = h2[(h2["outcome"] == y) & (h2["sample"] == sample)]
    if len(fit) == 0:
        return ""
    kind = fit["kind"].iloc[0]; label = fit["label"].iloc[0]; n = int(fit["n"].iloc[0])
    lines = [f"### {label}", f"*Sample:* {SAMPLE_LABEL.get(sample, sample)}; N = {n:,}"
             + (f"; events = {int(R['summary'][(R['summary'].outcome == y) & (R['summary']['sample'] == sample)]['events'].iloc[0])}" if kind == "logit" else "")
             + f"; estimator = {'OLS with HC3-robust SEs' if kind == 'ols' else 'logistic regression (Wald z)'}", ""]

    # --- fit table
    lines.append("**Model fit by specification**\n")
    order = ["M0", "M1"] + [f"M2_{k}" for k in CORE_CGM] + ["M2", "M3"]
    f = fit.set_index("spec").reindex(order).reset_index()
    f["Specification"] = f["spec"].map(SPEC_LABEL)
    f["AIC"] = f["aic"].map(lambda v: f"{v:.1f}"); f["BIC"] = f["bic"].map(lambda v: f"{v:.1f}")
    if kind == "ols":
        f["R2"] = f["r2"].map(lambda v: f"{v:.4f}"); f["Adj. R2"] = f["adj_r2"].map(lambda v: f"{v:.4f}")
        f["CV R2 (mean +- SD)"] = f.apply(lambda r: f"{r['cv_r2_mean']:.4f} +- {r['cv_r2_sd']:.3f}" if pd.notna(r.get("cv_r2_mean", np.nan)) else "-", axis=1)
        lines.append(md_table(f, ["Specification", "R2", "Adj. R2", "AIC", "BIC", "CV R2 (mean +- SD)"]))
    else:
        f["McFadden R2"] = f["mcfadden_r2"].map(lambda v: f"{v:.4f}"); f["Nagelkerke R2"] = f["nagelkerke_r2"].map(lambda v: f"{v:.4f}")
        f["AUC (in-sample)"] = f["auc_in_sample"].map(lambda v: f"{v:.4f}")
        f["CV AUC (mean +- SD)"] = f.apply(lambda r: f"{r['cv_auc_mean']:.4f} +- {r['cv_auc_sd']:.3f}" if pd.notna(r.get("cv_auc_mean", np.nan)) else "-", axis=1)
        f["CV Brier"] = f.apply(lambda r: f"{r['cv_brier_mean']:.4f}" if pd.notna(r.get("cv_brier_mean", np.nan)) else "-", axis=1)
        lines.append(md_table(f, ["Specification", "McFadden R2", "Nagelkerke R2", "AIC", "BIC", "AUC (in-sample)", "CV AUC (mean +- SD)", "CV Brier"]))
    lines.append("")

    # --- slope tables
    lines.append("**Slope tests (each row is one predictor in one specification)**\n")
    s = sl.copy()
    s["Specification"] = s["spec"].map(SPEC_LABEL)
    s["Predictor"] = s["predictor"].map(PRED_LABEL)
    s["raw slope (95% CI)"] = s.apply(lambda r: f"{r['beta_raw']:.4g} [{r['ci_low_raw']:.4g}, {r['ci_high_raw']:.4g}]", axis=1)
    if kind == "ols":
        s["per-1-SD effect (95% CI)"] = s.apply(lambda r: f"{r['beta_per_sd']:.3f} [{r['ci_low_per_sd']:.3f}, {r['ci_high_per_sd']:.3f}]", axis=1)
        s["t (HC3)"] = s["stat"].map(lambda v: f"{v:.2f}")
        cols = ["Specification", "Predictor", "raw slope (95% CI)", "per-1-SD effect (95% CI)", "t (HC3)", "p"]
    else:
        s["per-1-SD effect (95% CI)"] = s.apply(lambda r: f"OR {r['or_per_sd']:.3f} [{r['or_ci_low']:.3f}, {r['or_ci_high']:.3f}]", axis=1)
        s["t (HC3)"] = s["stat"].map(lambda v: f"{v:.2f}")
        cols = ["Specification", "Predictor", "raw slope (95% CI)", "per-1-SD effect (95% CI)", "t (HC3)", "p"]
    s["p"] = s["p"].map(lambda v: fmt_p(v) + stars(v))
    s["_o"] = s["spec"].map({k: i for i, k in enumerate(order + [f"M3_{k}" for k in CORE_CGM])})
    s = s.sort_values(["_o", "predictor"])
    hdr = ["Specification", "Predictor", "raw slope (95% CI)", "per-1-SD effect (95% CI)", "z" if kind == "logit" else "t (HC3)", "p"]
    lines.append(md_table(s, cols, hdr)); lines.append("")

    # --- nested tests
    lines.append("**Nested-model tests (incremental information)**\n")
    ne = ne.copy()
    ne["Comparison"] = ne.apply(lambda r: f"{r['full']} vs {r['reduced']}", axis=1)
    ne["Statistic"] = ne.apply(lambda r: f"{r['test']}({r['df']}) = {r['stat']:.2f}", axis=1)
    ne["p"] = ne["p"].map(lambda v: fmt_p(v) + stars(v))
    ne["robust Wald p"] = ne["robust_wald_p"].map(lambda v: fmt_p(v) + stars(v))
    ne["dAIC (full - reduced)"] = ne["delta_aic"].map(lambda v: f"{v:+.1f}")
    ne["dBIC"] = ne["delta_bic"].map(lambda v: f"{v:+.1f}")
    lines.append(md_table(ne, ["question", "Comparison", "Statistic", "p", "robust Wald p", "dAIC (full - reduced)", "dBIC"],
                          ["Question", "Comparison", "Statistic", "p", "Robust Wald p", "dAIC (full - reduced)", "dBIC"]))
    lines.append("")

    # --- head to head
    if len(h2):
        h = h2.iloc[0]
        lines.append("**Head-to-head: HbA1c-only vs CGM-only (non-nested)**\n")
        if kind == "ols":
            lines.append(f"- Adj. R2: M1 (HbA1c) = {h['adj_r2_M1']:.4f}; M2 (4 CGM) = {h['adj_r2_M2']:.4f}; "
                         f"best single CGM metric = {PRED_LABEL[h['best_single_cgm']]} ({h['adj_r2_best_single_cgm']:.4f}); M3 = {h['adj_r2_M3']:.4f}")
            if pd.notna(h.get("boot_dAdjR2_M2_minus_M1_ci_low", np.nan)):
                lines.append(f"- Bootstrap 95% CI for Adj.R2(M2) - Adj.R2(M1): [{h['boot_dAdjR2_M2_minus_M1_ci_low']:+.4f}, {h['boot_dAdjR2_M2_minus_M1_ci_high']:+.4f}]; "
                             f"for best-single-CGM - M1: [{h['boot_dAdjR2_best_minus_M1_ci_low']:+.4f}, {h['boot_dAdjR2_best_minus_M1_ci_high']:+.4f}]")
        else:
            lines.append(f"- AUC: M1 (HbA1c) = {h['auc_M1']:.4f}; M2 (4 CGM) = {h['auc_M2']:.4f} (DeLong z = {h['delong_z_M2_vs_M1']:.2f}, p = {fmt_p(h['delong_p_M2_vs_M1'])}); "
                         f"best single CGM = {PRED_LABEL[h['best_single_cgm']]} ({h['auc_best_single_cgm']:.4f}, DeLong p = {fmt_p(h['delong_p_best_vs_M1'])}); "
                         f"M3 = {h['auc_M3']:.4f} (DeLong p vs M1 = {fmt_p(h['delong_p_M3_vs_M1'])})")
        lines.append(f"- AIC: M1 = {h['aic_M1']:.1f}; M2 = {h['aic_M2']:.1f}; best single CGM = {h['aic_best_single_cgm']:.1f} "
                     f"(difference vs M1 = {h['aic_diff_bestCGM_minus_HbA1c']:+.1f}); M3 = {h['aic_M3']:.1f}")
        lines.append("")

    # --- VIF, partial correlations, non-linearity, stratified
    v = R["vif"]; v = v[(v["outcome"] == y) & (v["sample"] == sample)]
    if len(v):
        lines.append("**Variance inflation factors in M3** (HbA1c + 4 CGM metrics): " +
                     "; ".join(f"{PRED_LABEL[r['predictor']]} = {r['vif']:.1f}" for _, r in v.iterrows()))
        lines.append("")
    pc = R["partial"]; pc = pc[(pc["outcome"] == y) & (pc["sample"] == sample)]
    if len(pc):
        lines.append("**Rank-based partial correlations** (Spearman rho of covariate-residualised outcome and predictor): " +
                     "; ".join(f"{PRED_LABEL[r['predictor']]} rho = {r['partial_spearman_rho']:+.3f} (p = {fmt_p(r['p'])})" for _, r in pc.iterrows()))
        lines.append("")
    nl = R["nonlin"]; nl = nl[(nl["outcome"] == y) & (nl["sample"] == sample)]
    if len(nl):
        lines.append("**Quadratic (non-linearity) checks**, single-predictor models with z-scored predictor: " +
                     "; ".join(f"{PRED_LABEL[r['predictor']]}: beta_quad = {r['beta_quadratic_z']:+.3f}, p = {fmt_p(r['p_quadratic'])}" for _, r in nl.iterrows()))
        lines.append("")
    st = R["strat"]; st = st[(st["outcome"] == y) & (st["sample"] == sample)]
    if len(st):
        lines.append("**Diabetes-stratified single-predictor slopes** (per pooled SD; interaction p from predictor x diabetes term)\n")
        st = st.copy()
        st["Predictor"] = st["predictor"].map(PRED_LABEL)
        st["slope (95% CI)"] = st.apply(lambda r: f"{r['beta_per_pooled_sd']:+.3f} [{r['ci_low']:+.3f}, {r['ci_high']:+.3f}]", axis=1)
        st["p"] = st["p"].map(lambda v: fmt_p(v) + stars(v))
        st["p_int"] = st["p_interaction"].map(fmt_p)
        lines.append(md_table(st, ["Predictor", "stratum", "n", "slope (95% CI)", "p", "p_int"],
                              ["Predictor", "Stratum", "n", "Slope per pooled SD (95% CI)", "p", "Interaction p"]))
        lines.append("")
    return "\n".join(lines)


def write_full_tables(R):
    L = ["# Phase 5 - Full regression tables: CGM-derived metrics vs HbA1c across four outcome domains",
         "",
         "Generated by `src/5_multimodal_cgm_analysis/generate_reports.py` from the CSV outputs of "
         "`run_multimodal_cgm_models.py`. All specifications for a given outcome are fitted on the same "
         "complete-case sample. Covariates in every model: age, BMI, education level (3 categories), "
         "clinical site, hypertension, high cholesterol, kidney disease, circulatory disease; home-environment "
         "outcomes additionally adjust for season of the study visit. Significance stars: * p<0.05, ** p<0.01, *** p<0.001 (unadjusted).",
         "",
         "**Specification key**: M0 covariates only; M1 + HbA1c; M2[x] + one CGM metric x; M2 + all four CGM metrics "
         "(mean glucose, mean/SD ratio, average daily TIR 70-180, average daily SD); M3[x] + HbA1c + one CGM metric; "
         "M3 + HbA1c + all four CGM metrics.",
         "",
         "## Sample construction", ""]
    for k, v in R["cov"].items():
        L.append(f"- {k}: **{v:,}**")
    L += ["", "## Table 1. Cohort characteristics of the analysis base by diabetes status", "",
          "Values are mean (SD) [n] or n (%). p: Kruskal-Wallis (continuous) or chi-square (binary) across the four groups.", ""]
    t1 = R["t1"]
    L.append(md_table(t1, ["variable", "No diabetes", "Pre-diabetes / lifestyle", "T2D non-insulin", "T2D insulin", "All", "p_across_groups"],
                      ["Variable", "No diabetes", "Pre-diabetes / lifestyle", "T2D non-insulin", "T2D insulin", "All", "p"]))
    L += ["", "## Table 2. Spearman correlations among the five candidate predictors (analysis base)", ""]
    c = R["corr"].copy(); c.index = [PRED_LABEL.get(i, i) for i in c.index]; c.columns = [PRED_LABEL.get(i, i) for i in c.columns]
    c = c.round(2).reset_index().rename(columns={"index": "Predictor"})
    L.append(md_table(c, list(c.columns)))
    L += ["", "## Table 3. Primary family of slope tests with Benjamini-Hochberg FDR", "",
          "One test per outcome x predictor: HbA1c from M1, each CGM metric from its own single-metric model M2[x]. "
          "q = BH-adjusted p across the whole family.", ""]
    fam = R["fam"].copy()
    fam["Outcome"] = fam["label"]; fam["Predictor"] = fam["predictor"].map(PRED_LABEL)
    fam["effect per 1 SD (95% CI)"] = fam.apply(lambda r: (f"OR {r['or_per_sd']:.3f} [{r['or_ci_low']:.3f}, {r['or_ci_high']:.3f}]" if r["kind"] == "logit"
                                                            else f"{r['beta_per_sd']:+.3f} [{r['ci_low_per_sd']:+.3f}, {r['ci_high_per_sd']:+.3f}]"), axis=1)
    fam["stat"] = fam["stat"].map(lambda v: f"{v:.2f}")
    fam["p_s"] = fam["p"].map(fmt_p); fam["q_s"] = fam["q_bh"].map(lambda v: fmt_p(v) + (" (FDR<0.05)" if v < 0.05 else ""))
    fam["_o"] = fam["outcome"].map({c: i for i, (_, c, *_) in enumerate(OUTCOMES)})
    fam["_p"] = fam["predictor"].map({p: i for i, p in enumerate([HBA1C] + list(CORE_CGM))})
    fam = fam.sort_values(["_o", "_p"])
    L.append(md_table(fam, ["Outcome", "Predictor", "n", "effect per 1 SD (95% CI)", "stat", "p_s", "q_s"],
                      ["Outcome", "Predictor", "n", "Effect per 1 SD (95% CI)", "t / z", "p", "q (BH)"]))
    L += ["", "## Table 4. Incremental-information tests with FDR (M3 vs M1: CGM beyond HbA1c; M3 vs M2: HbA1c beyond CGM)", ""]
    f2 = R["fam2"].copy(); f2["Outcome"] = f2["label"]
    f2["Statistic"] = f2.apply(lambda r: f"{r['test']}({r['df']}) = {r['stat']:.2f}", axis=1)
    f2["p_s"] = f2["p"].map(fmt_p); f2["q_s"] = f2["q_bh"].map(lambda v: fmt_p(v) + (" (FDR<0.05)" if v < 0.05 else ""))
    f2["dAIC"] = f2["delta_aic"].map(lambda v: f"{v:+.1f}")
    L.append(md_table(f2, ["Outcome", "question", "Statistic", "p_s", "q_s", "dAIC"], ["Outcome", "Question", "Statistic", "p", "q (BH)", "dAIC (full - reduced)"]))
    L += ["", "## Table 5. Does each single CGM metric add information beyond HbA1c? (M3[x] vs M1, FDR-controlled)", ""]
    f3 = R["fam3"].copy(); f3["Outcome"] = f3["label"]; f3["CGM metric"] = f3["full"].str.replace("M3_", "").map(PRED_LABEL)
    f3["Statistic"] = f3.apply(lambda r: f"{r['test']}({r['df']}) = {r['stat']:.2f}", axis=1)
    f3["p_s"] = f3["p"].map(fmt_p); f3["q_s"] = f3["q_bh"].map(lambda v: fmt_p(v) + (" (FDR<0.05)" if v < 0.05 else ""))
    f3["dAIC"] = f3["delta_aic"].map(lambda v: f"{v:+.1f}")
    L.append(md_table(f3, ["Outcome", "CGM metric", "Statistic", "p_s", "q_s", "dAIC"], ["Outcome", "CGM metric", "Statistic", "p", "q (BH)", "dAIC"]))

    L += ["", "---", "", "## Per-outcome detail (primary analysis sample)", ""]
    for dom in ["Cognition", "Depression", "Home environment", "Wearable activity"]:
        L.append(f"## Domain: {dom}\n")
        for d, y, kind, lab, _, _ in OUTCOMES:
            if d == dom:
                L.append(outcome_block(R, y, "primary")); L.append("\n---\n")
    with open(os.path.join(REPORT_DIR, "research_report_02_full_regression_tables.md"), "w") as f:
        f.write("\n".join(L))


def write_sensitivity(R):
    L = ["# Phase 5 - Sensitivity analyses and exploratory sweeps", "",
         "All sensitivity samples re-fit every specification on the restricted sample. Tables below show the single-predictor "
         "slope tests (HbA1c from M1; each CGM metric from M2[x]) so that estimates can be compared with the primary analysis.", ""]
    sl = R["slopes"]
    single = sl[((sl["spec"] == "M1") & (sl["predictor"] == HBA1C)) | sl.apply(lambda r: r["spec"] == f"M2_{r['predictor']}", axis=1)].copy()
    single["eff"] = single.apply(lambda r: (f"OR {r['or_per_sd']:.3f} [{r['or_ci_low']:.3f}, {r['or_ci_high']:.3f}]" if r["kind"] == "logit"
                                            else f"{r['beta_per_sd']:+.3f} [{r['ci_low_per_sd']:+.3f}, {r['ci_high_per_sd']:+.3f}]"), axis=1)
    single["p_s"] = single["p"].map(lambda v: fmt_p(v) + stars(v))
    single["stat"] = single["stat"].map(lambda v: f"{v:.2f}")
    single["Predictor"] = single["predictor"].map(PRED_LABEL)
    for sample in ["cgm_ge7_days", "no_insulin", "diabetes_only", "no_diabetes_only"]:
        L.append(f"## {SAMPLE_LABEL[sample]}\n")
        sub = single[single["sample"] == sample]
        if len(sub) == 0:
            L.append("_no results_\n"); continue
        for d, y, kind, lab, _, _ in OUTCOMES:
            s = sub[sub["outcome"] == y]
            if len(s) == 0:
                continue
            L.append(f"**{lab}** (N = {int(s['n'].iloc[0]):,})\n")
            L.append(md_table(s, ["Predictor", "eff", "stat", "p_s"], ["Predictor", "Effect per 1 SD (95% CI)", "t / z", "p"]).replace("| stat |", "| t / z |"))
            ne = R["nested"]; ne = ne[(ne["outcome"] == y) & (ne["sample"] == sample) & (ne["full"] == "M3")]
            if len(ne):
                L.append("\n" + "; ".join(f"{r['question']} {r['test']}({r['df']}) = {r['stat']:.2f}, p = {fmt_p(r['p'])}" for _, r in ne.iterrows()))
            L.append("")
    L += ["## Exploratory outcomes (core CGM metrics, primary sample; not part of the FDR family)", ""]
    for d, y, kind, lab, _, _ in EXPLORATORY_OUTCOMES:
        blk = outcome_block(R, y, "exploratory_outcome")
        if blk:
            L.append(blk); L.append("\n---\n")
    L += ["## Exploratory sweep of additional CGM metrics (single-metric models, primary outcomes, BH-FDR within the sweep)", ""]
    e = R["expl"].copy()
    if len(e):
        e["Outcome"] = e["label"]; e["Metric"] = e["predictor_label"]
        e["eff"] = e.apply(lambda r: (f"OR {r['or_per_sd']:.3f} [{r['or_ci_low']:.3f}, {r['or_ci_high']:.3f}]" if r["kind"] == "logit"
                                      else f"{r['beta_per_sd']:+.3f} [{r['ci_low_per_sd']:+.3f}, {r['ci_high_per_sd']:+.3f}]"), axis=1)
        e["p_s"] = e["p"].map(fmt_p); e["q_s"] = e["q_bh"].map(lambda v: fmt_p(v) + (" (FDR<0.05)" if v < 0.05 else ""))
        e["_o"] = e["outcome"].map({c: i for i, (_, c, *_) in enumerate(OUTCOMES)})
        e = e.sort_values(["_o", "q_bh"])
        L.append(md_table(e, ["Outcome", "Metric", "n", "eff", "p_s", "q_s"], ["Outcome", "CGM metric", "n", "Effect per 1 SD (95% CI)", "p", "q (BH)"]))
    with open(os.path.join(REPORT_DIR, "research_report_03_sensitivity_and_exploratory_tables.md"), "w") as f:
        f.write("\n".join(L))


def write_dictionary(R):
    L = ["# Phase 5 - Data dictionary, extraction rules and execution log", "",
         "## 1. Execution", "",
         "```bash", 'source "new research/.venv/bin/activate"',
         'python3 "new research/src/5_multimodal_cgm_analysis/extract_multimodal_dataset.py"   # ~5 min, 8 workers',
         'python3 "new research/src/5_multimodal_cgm_analysis/run_multimodal_cgm_models.py"     # ~10 min',
         'python3 "new research/src/5_multimodal_cgm_analysis/generate_reports.py"', "```", "",
         "Inputs: `dataset/` (AI-READI v3.0.0 flagship release). Output dataset: `new research/data/master_multimodal_dataset.csv` "
         "(one row per participant, 2,280 rows). Result CSVs: `reports/5_multimodal_cgm_analysis/data/`; figures: `.../figures/`.", "",
         "## 2. Glucose category cut-offs (mg/dL)", "",
         "| Category | Rule |", "| :--- | :--- |",
         "| Severe hypoglycaemia | < 54 (strict) |", "| Moderate hypoglycaemia | 54-69 inclusive |",
         "| Normal / time in range (TIR) | 70-180 inclusive |", "| Moderate hyperglycaemia | 181-250 inclusive |",
         "| Severe hyperglycaemia | > 250 (strict) |", "",
         "## 3. CGM variables (Dexcom G6, 5-min sampling, converted to site-local time)", "",
         "| Variable | Definition |", "| :--- | :--- |",
         "| `mean_glucose` | Mean of all valid readings (39-401 mg/dL) over the wear period |",
         "| `glucose_sd` | Sample SD (ddof = 1) of all readings |",
         "| `mean_to_sd_ratio` | `mean_glucose / glucose_sd` (inverse of the coefficient of variation) |",
         "| `glucose_cv` | 100 x SD / mean |",
         "| `gmi` | Glucose management indicator = 3.31 + 0.02392 x mean glucose |",
         "| `tir_overall`, `tar_above_180`, `tbr_below_70`, `pct_severe_hypo`, `pct_mod_hypo`, `pct_mod_hyper`, `pct_severe_hyper` | Percentage of all readings in each category |",
         "| `cgm_valid_days` | Number of local calendar days with >= 70% of the expected 288 readings |",
         "| `avg_daily_tir` | Mean over valid days of the daily % of readings in 70-180 |",
         "| `avg_daily_sd` | Mean over valid days of the within-day sample SD |",
         "| `avg_daily_mean`, `avg_daily_tar`, `avg_daily_tbr`, `avg_daily_range`, `avg_daily_mean_to_sd` | Analogous day-level averages |",
         "| `sd_of_daily_means` | Between-day SD of the daily means |",
         "| `mag_mg_dl_per_h` | Mean absolute glucose change per hour (consecutive readings <= 30 min apart) |",
         "| `nocturnal_mean`, `nocturnal_tar` | Mean and % > 180 between 00:00 and 05:59 local time |",
         "", "Inclusion: >= 3 valid days (sensitivity: >= 7).", "",
         "## 4. Clinical / survey variables (OMOP tables)", "",
         "| Variable | Source | Rule |", "| :--- | :--- | :--- |",
         "| `hba1c` | `measurement.csv` `import_hba1c` | mean of laboratory values |",
         "| `moca_total`, `moca_memory_index`, `moca_delayed_recall`, ... | `measurement.csv` `moca_*` | max per participant |",
         "| `cognitive_impairment` | derived | MoCA total < 26 |",
         "| `cesd10_total`, `cesd_item1..10` | `observation.csv` `cestl`, `ces1..ces10` | CES-D-10 total (0-30) |",
         "| `cesd10_ge10` | derived | CES-D-10 >= 10 (standard screening threshold) |",
         "| `paid5_total` | `observation.csv` `paidscore` | PAID-5 diabetes distress (0-20) |",
         "| `years_of_education`, `education_level` | `observation.csv` | <= 12 y = high school or below; 13-16 = college; > 16 = graduate |",
         "| `hypertension`, `high_cholesterol`, `kidney_disease`, `circulatory_problems` (circulation, stroke, MI), `pulmonary_disease`, ... | `condition_occurrence.csv` `mhoccur_*` | self-reported medical history |",
         "| `insulin_use`, `oral_glucose_meds` | `observation.csv` `cmtrt_insln`, `cmtrt_a1c` | 0 for participants not asked (non-diabetic) |",
         "| `current_smoker`, `ever_alcohol`, `sleeping_pills_2wk`, `food_insecure`, `fell_last_12mo` | `observation.csv` | sentinel codes 555/777/888/999 treated as missing |",
         "| `diabetes_status`, `any_diabetes` | `participants.tsv` `study_group` | T2D = oral/non-insulin or insulin-dependent groups |",
         "| `clinical_site`, `visit_season` | `participants.tsv` | UW, UCSD, UAB; season of study visit |",
         "", "Sex and race/ethnicity are not released at the individual level in this dataset version and could not be adjusted for.", "",
         "## 5. Home environmental sensor (LeeLab Anura, 5-s sampling, full file)", "",
         "Physical-plausibility filters: temperature -10 to 50 C, humidity 0-100 %, PM < 5,000 ug/m3 (uint16 sentinel removed), "
         "VOC/NOx index 1-500 (0 = warm-up). Readings averaged to 1-minute bins before summarising.", "",
         "| Variable | Definition |", "| :--- | :--- |",
         "| `env_pm25_mean`, `env_pm25_median`, `env_pm25_p95`, `env_pm25_daily_max` | PM2.5 (ug/m3) summaries |",
         "| `env_pm25_pct_gt15`, `env_pm25_pct_gt35` | % of minutes above the WHO 2021 24-h guideline (15) and US EPA 24-h standard (35) |",
         "| `log_pm25_mean` | log(1 + mean PM2.5) - primary environment outcome |",
         "| `env_pm10_mean`, `env_pm1_mean` | PM10 / PM1 means |",
         "| `env_temp_mean`, `env_temp_sd`, `env_temp_night_mean` (22:00-05:59), `env_temp_pct_lt18`, `env_temp_pct_gt26` | Temperature (C) |",
         "| `env_hum_mean`, `env_hum_sd`, `env_hum_pct_gt60`, `env_hum_pct_lt30` | Relative humidity (%) |",
         "| `env_voc_mean`, `env_voc_median`, `env_voc_pct_gt250` | Sensirion VOC index (100 = typical baseline) |",
         "| `env_nox_mean`, `env_nox_median`, `env_nox_pct_gt20` | Sensirion NOx index |",
         "| `env_days` | hours of valid data / 24; inclusion >= 3 days |", "",
         "## 6. Wearable (Garmin Vivosmart 5)", "",
         "| Variable | Definition |", "| :--- | :--- |",
         "| `wear_days_hr` | Calendar days (excluding first and last) with >= 10 distinct hours containing a valid heart-rate sample (30-220 bpm) |",
         "| `hr_mean`, `hr_resting_proxy` (mean of the daily 5th percentile), `hr_night_mean` (00:00-04:59) | Heart rate (bpm) on wear-days |",
         "| `steps_per_day` | Mean daily step total over wear-days with > 0 steps |",
         "| `mvpa_min_per_day` | Minutes/day in non-sedentary epochs with cadence >= 100 steps/min (moderate-intensity proxy) |",
         "| `active_min_per_day`, `sedentary_pct` | Non-sedentary minutes/day; % of labelled minutes labelled sedentary |",
         "| `active_kcal_per_day` | Daily maximum of the cumulative active-kcal counter |",
         "| `stress_mean`, `stress_pct_high` (> 50), `stress_pct_rest` (<= 25) | Garmin HRV-based stress index, valid samples 0-100 only (-1 / -2 removed) |",
         "| `sleep_tst_min`, `sleep_efficiency_pct`, `sleep_deep_pct`, `sleep_rem_pct`, `sleep_tst_sd_min` | Per night (interval assigned to the date 12 h before its start); duplicate/overlapping intervals removed; nights between 2 h and 16 h |",
         "| `spo2_mean`, `spo2_pct_lt90` | Pulse-oximetry samples 70-100 % |",
         "| `resp_rate_mean` | Respiratory-rate samples 4-40 breaths/min |", "",
         "## 7. Follow-up variables (report 05, `run_phase5_followups.py`)", "",
         "| Variable | Definition |", "| :--- | :--- |",
         "| `hemoglobin_g_dl`, `mcv_fl`, `rdw_pct`, `hematocrit_pct`, `c_peptide` | `measurement.csv` `lbscat_a1c` (haemoglobin, g/dL - not HbA1c), `lbscat_mcv`, `lbscat_rdw`, `lbscat_hct`, `import_c_peptide` |",
         "| `recommended_split` | `participants.tsv` train / val / test; train = discovery, val + test = hold-out |",
         "| `sleep_onset_mean_h`, `sleep_midpoint_mean_h` | Mean clock time of sleep onset / midpoint, in hours after local noon of the night date (15 = 03:00) |",
         "| `sleep_onset_sd_h`, `sleep_midpoint_sd_h`, `sleep_tst_sd_min` | Night-to-night SD of onset, midpoint and total sleep time (sleep regularity) |",
         "| `hgi` | Haemoglobin glycation index = HbA1c minus its cohort-regression prediction from mean glucose (computed inside the follow-up script) |",
         "| `glycation_gap` | HbA1c minus GMI |",
         "| Split-half metrics (`followup_E_*`) | Mean glucose, daily SD and TIR computed separately for the first and second half of each participant's wear; ICC(2,1) |",
         "",
         "## 8. Statistical procedures", "",
         "- Continuous outcomes: OLS, HC3 heteroskedasticity-robust standard errors and t-tests; nested F-tests on the ML fit and HC3 block Wald tests.",
         "- Binary outcomes: logistic regression (Newton-Raphson), Wald z-tests, likelihood-ratio tests, McFadden and Nagelkerke R2, DeLong test for paired AUC differences.",
         "- Effects reported per 1 SD of the predictor (SD computed in the complete-case sample of that outcome) and in raw units.",
         "- Out-of-sample performance: 5 x repeated 10-fold cross-validation (stratified for binary outcomes); R2 / AUC / Brier.",
         "- Bootstrap (400 resamples) 95% percentile CI for the difference in adjusted R2 between CGM-only and HbA1c-only models.",
         "- Multiplicity: Benjamini-Hochberg FDR within the primary slope family (14 outcomes x 5 predictors), the incremental-test family (14 x 2) and the single-metric-beyond-HbA1c family (14 x 4); exploratory sweeps FDR-controlled separately.",
         "- Robustness: rank-based partial Spearman correlations, quadratic terms, diabetes-stratified slopes with interaction tests, >= 7-day CGM, insulin exclusion, diabetes-only and non-diabetes-only samples.",
         "- Follow-ups (report 05): nested tests for the two-metric pair; HGI models with and without red-cell indices; discovery/hold-out replication with one-sided hold-out tests in the pre-specified direction; bootstrap (500) mediation; 4-group interaction tests and natural cubic splines (`cr(x, df=4)`); split-half ICC(2,1).",
         "- Software: Python 3.14, pandas 3.0, statsmodels 0.14.6, scikit-learn 1.9, SciPy."]
    with open(os.path.join(REPORT_DIR, "research_report_04_data_dictionary_and_methods_log.md"), "w") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    R = load()
    write_full_tables(R)
    write_sensitivity(R)
    write_dictionary(R)
    print("Reports written to", REPORT_DIR)
