"""
Auto-generated interpretation sections for Phase 6 / 6b files.

`interpret(rows, heading)` takes any subset of the single-predictor result rows (Phase 6 or 6b CSV
columns) and writes a data-driven summary: what predicts each outcome best out of sample, which
associations survive the FDR rule, which are only nominal, and which predictor families carry the
signal.  Every statement is computed from the rows passed in, so the same function serves the
population files, the band files, the cohort files and the term-by-term model-output files.
"""

import numpy as np
import pandas as pd

FAMILY_ORDER = ["HbA1c", "CGM level", "CGM variability", "Range 70-180", "Band < 54", "Band 54-69", "Band < 70",
                "Band 54-250", "Band 181-250", "Band > 180", "Band > 250"]


def _fmt_p(p):
    return f"{p:.1e}" if p < 0.001 else f"{p:.3f}"


def _effect(r):
    if r["kind"] == "logit":
        return f"OR {r['or_per_sd']:.2f} per SD"
    return f"{r['beta_per_sd']:+.3g} per SD"


def _direction(r):
    return "higher" if r["beta_raw"] > 0 else "lower"


def interpret(rows, heading="Interpretation", context=None, short=None):
    """rows: DataFrame of result rows (skipped rows are ignored). Returns markdown."""
    short = short or {}
    ok = rows[rows["skipped_reason"].fillna("") == ""].copy()
    if len(ok) == 0:
        return f"\n## {heading}\n\n_No models could be fitted for this selection._\n"
    ok["gain"] = ok["cv_score"] - ok["cv_score_covariates_only"]
    ok["fdr_sig"] = ok["fdr_applied"] & (ok["q_bh_group_all_tests"] < 0.05)
    ok["fdr_sig_outcome"] = ok["fdr_applied"] & (ok["q_bh_group_outcome"] < 0.05)
    ok["pl"] = ok["predictor"].map(lambda p: short.get(p, ok.loc[ok.predictor == p, "predictor_label"].iloc[0] if (ok.predictor == p).any() else p))
    n_tests = len(ok); n_raw = int((ok["p"] < 0.05).sum()); n_fdr_applied = int(ok["fdr_applied"].sum()); n_fdr = int(ok["fdr_sig"].sum())
    L = [f"\n## {heading}", ""]
    if context:
        L += [context, ""]
    L.append(f"**Scope.** {n_tests} single-predictor tests; {n_raw} with raw p < 0.05 (about {round(0.05 * n_tests)} expected by chance); "
             f"FDR rule applied to {n_fdr_applied} tests (samples with n >= 500), of which **{n_fdr}** are significant at BH q < 0.05 in the all-tests family"
             + (f" and {int(ok['fdr_sig_outcome'].sum())} in the within-outcome family." if n_fdr_applied else "; no test met the FDR rule, so only raw p-values are available."))
    L.append("")
    # ---- per outcome ----
    L.append("**By outcome (best out-of-sample predictor, then the associations that survive FDR):**")
    L.append("")
    outcomes = list(dict.fromkeys(ok["outcome"]))
    rank = []
    for y in outcomes:
        s = ok[ok.outcome == y]
        lab = s["label"].iloc[0]
        best = s.sort_values("gain", ascending=False).iloc[0]
        gain = best["gain"]
        metric = "AUC" if best["kind"] == "logit" else "R²"
        rank.append((lab, gain, best["pl"]))
        line = f"- **{lab}** (n = {int(s['n'].max()):,}): best single predictor out of sample is **{best['pl']}** "
        line += f"(CV {metric} {best['cv_score']:.3f} vs {best['cv_score_covariates_only']:.3f} for covariates alone, gain {gain:+.3f}; "
        line += f"{_effect(best)}, p = {_fmt_p(best['p'])}"
        if best["fdr_applied"]:
            line += f", q = {_fmt_p(best['q_bh_group_all_tests'])}"
        line += ")."
        sig = s[s["fdr_sig"]].sort_values("p")
        if len(sig):
            items = [f"{r['pl']} ({_direction(r)} outcome, {_effect(r)}, q = {_fmt_p(r['q_bh_group_all_tests'])})" for _, r in sig.head(6).iterrows()]
            line += f" FDR-robust associations ({len(sig)}): " + "; ".join(items) + ("; ..." if len(sig) > 6 else "") + "."
        else:
            nom = s[s["p"] < 0.05].sort_values("p")
            if len(nom) and n_fdr_applied:
                line += f" No association survives FDR; nominal only: " + ", ".join(f"{r['pl']} (p = {_fmt_p(r['p'])})" for _, r in nom.head(4).iterrows()) + "."
            elif len(nom):
                line += f" Raw p < 0.05 (FDR not applicable here): " + ", ".join(f"{r['pl']} (p = {_fmt_p(r['p'])})" for _, r in nom.head(5).iterrows()) + "."
            else:
                line += " No glycaemic measure is associated with this outcome (all p > 0.05)."
        if gain <= 0.002 and len(sig) == 0:
            line += " Not predictable from glycaemia in this sample."
        L.append(line)
    L.append("")
    # ---- ranking for prediction ----
    rank.sort(key=lambda t: -t[1])
    L.append("**Most predictable outcomes (largest out-of-sample gain over covariates):** " +
             "; ".join(f"{lab} ({g:+.3f}, via {pl})" for lab, g, pl in rank[:4]) +
             ". Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.")
    L.append("")
    # ---- predictor families ----
    fam = ok.groupby("family").agg(tests=("p", "size"), fdr=("fdr_sig", "sum"), raw=("p", lambda s: int((s < 0.05).sum())),
                                   mean_gain=("gain", "mean")).reindex([f for f in FAMILY_ORDER if f in ok["family"].unique()])
    fam = fam.dropna(subset=["tests"])
    top = fam.sort_values(["fdr", "raw"], ascending=False).head(3)
    L.append("**Predictor families carrying the signal:** " +
             "; ".join(f"{f} ({int(r['fdr'])} FDR-significant / {int(r['raw'])} raw-significant of {int(r['tests'])})" for f, r in top.iterrows()) + ".")
    # level vs variability contrast
    lvl = ok[ok["family"] == "CGM level"]; var = ok[ok["family"] == "CGM variability"]; h = ok[ok["family"] == "HbA1c"]
    if len(lvl) and len(var):
        L.append(f"Level metrics: {int(lvl['fdr_sig'].sum())} FDR-significant ({int((lvl['p'] < 0.05).sum())} raw); variability metrics: "
                 f"{int(var['fdr_sig'].sum())} FDR-significant ({int((var['p'] < 0.05).sum())} raw); HbA1c alone: {int(h['fdr_sig'].sum())} FDR-significant ({int((h['p'] < 0.05).sum())} raw) across the outcomes in this file.")
    # HbA1c vs best CGM per outcome
    better = []
    for y in outcomes:
        s = ok[ok.outcome == y]
        hh = s[s.predictor == "hba1c"]; cg = s[s.predictor != "hba1c"]
        if len(hh) and len(cg):
            d = cg["delta_aic_vs_hba1c_model"].min()
            if pd.notna(d) and d < -2:
                b = cg.sort_values("delta_aic_vs_hba1c_model").iloc[0]
                better.append(f"{s['label'].iloc[0].split(' (')[0]} ({b['pl']}, ΔAIC {d:+.1f})")
    if better:
        L.append("")
        L.append("**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** " + "; ".join(better) + ".")
    L.append("")
    L.append("_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). "
             "Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._")
    return "\n".join(L) + "\n"
