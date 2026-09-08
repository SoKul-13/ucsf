"""
Phase 6b report generator: cohort-by-cohort single-predictor tables in the Phase 6 format.
Writes reports/6_subgroup_single_predictor_analysis/research_report_05_glucose_cohort_tables.md
"""

import os
import sys
import json
import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from run_phase6_analysis import PREDICTORS, GROUPS, OUT_DATA, REPORT_DIR, FDR_MIN_N, OUTCOMES  # noqa: E402
from run_phase6b_glucose_cohorts import COHORTS, MIN_COHORT_N  # noqa: E402
from generate_phase6_reports import fmt_p, stars, md_table, eff, SHORT  # noqa: E402


def main():
    res = pd.read_csv(os.path.join(OUT_DATA, "cohort_all_results.csv"))
    cs = pd.read_csv(os.path.join(OUT_DATA, "cohort_sizes.csv"))
    overlap = json.load(open(os.path.join(OUT_DATA, "cohort_overlap.json")))
    counts = pd.read_csv(os.path.join(OUT_DATA, "cohort_significance_counts.csv"))
    ok = res["skipped_reason"].fillna("") == ""
    r = res.copy()
    r.loc[ok, "Effect per 1 SD (95% CI)"] = r[ok].apply(eff, axis=1)
    r.loc[ok, "raw slope"] = r[ok]["beta_raw"].map(lambda v: f"{v:.4g}")
    r.loc[ok, "t / z"] = r[ok]["stat"].map(lambda v: f"{v:.2f}")
    r.loc[ok, "p (raw)"] = r[ok]["p"].map(lambda v: fmt_p(v) + stars(v))
    r.loc[ok, "q rule"] = r[ok].apply(lambda x: (fmt_p(x["q_bh_group_all_tests"]) if x["fdr_applied"] else f"not applied (n < {FDR_MIN_N})"), axis=1)
    r.loc[ok, "q info"] = r[ok]["q_bh_informational_group_all"].map(lambda v: fmt_p(v) + (" (q<0.05)" if v < 0.05 else ""))
    r.loc[ok, "dAIC covs"] = r[ok]["delta_aic_vs_covariates"].map(lambda v: f"{v:+.1f}")
    r.loc[ok, "dAIC HbA1c"] = r[ok]["delta_aic_vs_hba1c_model"].map(lambda v: "-" if pd.isna(v) else f"{v:+.1f}")
    r.loc[ok, "CV"] = r[ok].apply(lambda x: f"{x['cv_score']:.4f} | {x['cv_score_covariates_only']:.4f}", axis=1)
    r.loc[ok, "coef"] = r[ok]["beta_raw"].map(lambda v: f"{v:+.4g}")
    r.loc[ok, "se"] = r[ok]["se_raw"].map(lambda v: f"{v:.4g}")
    r.loc[ok, "ci"] = r[ok].apply(lambda x: f"[{x['ci_low_raw']:.4g}, {x['ci_high_raw']:.4g}]", axis=1)
    r.loc[ok, "sig"] = r[ok]["p"].map(stars)
    r.loc[ok, "fit"] = r[ok].apply(lambda x: f"{x['adj_r2']:.4f}" if x["kind"] == "ols" else f"{x['auc_in_sample']:.4f}", axis=1)
    r["Predictor"] = r["predictor"].map(lambda p: SHORT.get(p, PREDICTORS.get(p, (p,))[0]))
    r["_po"] = r["predictor"].map({p: i for i, p in enumerate(PREDICTORS)}).fillna(999)
    cols_a = ["Predictor", "n", "coef", "se", "ci", "t / z", "p (raw)", "sig"]
    hdr_a = ["Predictor (alone)", "N", "Coef (β)", "Std. Err.", "95% CI", "t / z", "Pr(>\\|t\\|)", "Signif"]
    cols_b = ["Predictor", "Effect per 1 SD (95% CI)", "q rule", "q info", "fit", "dAIC covs", "dAIC HbA1c", "CV"]
    hdr_b = ["Predictor (alone)", "β per 1 SD (95% CI)", f"q (rule: n >= {FDR_MIN_N})", "q (informational)", "Adj R² / AUC", "ΔAIC vs covs", "ΔAIC vs HbA1c", "CV R²/AUC (predictor vs covariates-only)"]

    L = ["# Phase 6b - Single-predictor tables inside the actual-value glucose cohorts", "",
         "Cohorts are defined by each participant's own CGM readings over the wear period; inside every cohort the full Phase 6 predictor set "
         "(HbA1c, CGM level and variability, time in range 70-180, and the glucose bands) is entered one measure at a time with the Phase 5 covariates, "
         "in the total, healthy (no diabetes + pre-diabetes) and non-healthy (T2D oral + insulin) populations.", "",
         "**Table layout.** Per outcome: (A) model output on the raw scale, one row per single-predictor model (coefficient, HC3 SE, 95% CI, t/z, p, stars); (B) effect per 1 SD, BH q (rule and informational), adjusted R²/AUC, AIC differences, CV. Complete term-by-term output for every model is in `model_output_tables/phase6b/<cohort>/<population>/<domain>.md` (index: `model_output_tables/README.md`) and `phase6b_model_outputs.csv`.", "",
         "## Cohort sizes and feasibility", ""]
    L.append(md_table(cs, ["cohort", "cohort_label", "n_total", "n_healthy", "n_non_healthy", "n_moca", "moca_lt26_events", "cesd_ge10_events", "n_env", "n_steps", "n_resting_hr", "n_sleep", "feasible"],
                      ["Cohort", "Definition", "N", "Healthy", "Non-healthy", "MoCA", "MoCA<26 events", "CES-D>=10 events", "Environment", "Steps", "Resting HR", "Sleep", "Feasible?"]))
    L += ["", f"Overlap of the exposure cohorts (total): hypoglycaemia only {overlap['hypo_only']}, hyperglycaemia only {overlap['hyper_only']}, both {overlap['both']}, neither (within 54-250) {overlap['neither (within 54-250)']}.", "",
          f"**FDR.** The Phase 6 rule (BH only when n >= {FDR_MIN_N}) is not met by any cohort, so the rule column reads 'not applied'. An informational BH q over all tests in the population is shown alongside and must be read as such.", "",
          "## Significance counts", ""]
    c = counts.copy(); c["cohort"] = c["cohort"].map(lambda k: COHORTS[k][0]); c["group"] = c["group"].map(lambda g: GROUPS[g][0])
    L.append(md_table(c, ["cohort", "group", "tests", "n_min", "n_max", "sig_raw", "sig_q_informational"], ["Cohort", "Population", "Tests", "n min", "n max", "Raw p < 0.05", "Informational q < 0.05"]))
    index = L + ["", "## Per-cohort table files (one file per cohort so that each renders in GitHub / VS Code)", ""]
    for ck in COHORTS:
        sub_c = r[r.cohort == ck]
        fname = f"research_report_05_cohort_{ck}.md"
        n = int(cs.loc[cs.cohort == ck, "n_total"].iloc[0])
        if len(sub_c) == 0:
            index.append(f"- {COHORTS[ck][0]}: **not analysed** (only {n} participants, fewer than {MIN_COHORT_N})"); continue
        index.append(f"- [{COHORTS[ck][0]}]({fname}) (N = {n:,})")
        C = [f"# Phase 6b cohort tables - {COHORTS[ck][0]} (N = {n:,})", "",
             "Back to the [cohort index](research_report_05_glucose_cohort_tables.md). Per outcome: (A) model output on the raw scale, one row per single-predictor model; "
             "(B) effect per 1 SD, BH q (rule and informational), adjusted R²/AUC, AIC differences, CV. Full term-by-term output: `model_output_tables/phase6b/`.", ""]
        for g, (glabel, _) in GROUPS.items():
            C.append(f"## Population: {glabel}\n")
            for dom in ["Cognition", "Depression", "Home environment", "Wearable activity"]:
                C.append(f"### Domain: {dom}\n")
                for d, y, kind, lab, _, _ in OUTCOMES:
                    if d != dom:
                        continue
                    sub = sub_c[(sub_c.group == g) & (sub_c.outcome == y)].sort_values("_po")
                    okk = sub[sub["skipped_reason"].fillna("") == ""]
                    if len(okk) == 0:
                        why = sub["skipped_reason"].dropna().unique()
                        C.append(f"#### {lab}\n_no models_ ({'; '.join(why[:2]) if len(why) else 'no data'})\n"); continue
                    nn = int(okk["n"].max()); ev = okk["events"].dropna()
                    C.append(f"#### {lab}\n*n = {nn:,}" + (f"; events = {int(ev.iloc[0])}" if len(ev) else "") + f"; {'OLS (HC3)' if kind == 'ols' else 'logistic (Wald)'}*\n")
                    C.append("**(A) Model output, raw scale**\n\n" + md_table(okk, cols_a, hdr_a) + "\n\n**(B) Standardised effect, multiplicity and fit**\n\n" + md_table(okk, cols_b, hdr_b))
                    sk = sub[sub["skipped_reason"].fillna("") != ""]
                    if len(sk):
                        C.append("\nSkipped: " + "; ".join(f"{PREDICTORS.get(p, (p,))[0]} ({why})" for p, why in zip(sk["predictor"], sk["skipped_reason"])))
                    C.append("")
        with open(os.path.join(REPORT_DIR, fname), "w") as f:
            f.write("\n".join(C))
    with open(os.path.join(REPORT_DIR, "research_report_05_glucose_cohort_tables.md"), "w") as f:
        f.write("\n".join(index))
    print("written")


if __name__ == "__main__":
    main()
