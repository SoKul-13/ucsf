"""
Phase 6 - Single-predictor glycaemic models by diabetes subgroup, with explicit FDR policy
=========================================================================================

Same data pipeline, covariates, outcome definitions and complete-case rules as Phase 5
(`master_multimodal_dataset.csv` from `5_multimodal_cgm_analysis/extract_multimodal_dataset.py`).

What is new
  1. Three analysis populations: TOTAL, HEALTHY (no diabetes + pre-diabetes / lifestyle),
     NON-HEALTHY (type 2 diabetes on oral / non-insulin injectables + insulin-treated).
  2. Every glycaemic measure is entered ALONE (covariates + one predictor): HbA1c, and every
     CGM metric (level, variability, time-in-range 70-180, and the glucose bands < 54, 54-69,
     < 70, 181-250, > 250, > 180, 54-250; pooled and day-averaged).
  3. p-values are reported raw AND Benjamini-Hochberg adjusted; the BH adjustment is applied
     only when the sample behind the test is large (n >= FDR_MIN_N participants).
  4. Feasibility check of the glucose bands outside 54-250 and the band-specific analyses.

Outputs: reports/6_subgroup_single_predictor_analysis/data/*.csv, figures/*.png
"""

import os
import sys
import json
import warnings

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
from sklearn.model_selection import RepeatedKFold, RepeatedStratifiedKFold
from sklearn.metrics import roc_auc_score, r2_score

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src", "5_multimodal_cgm_analysis"))
from run_multimodal_cgm_models import (fit, fit_ml, slope_row, COV_FORMULA, BASE_COVS, OUTCOMES, HBA1C)  # noqa: E402

warnings.filterwarnings("ignore")
np.random.seed(20260907)

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORT_DIR = os.path.join(PROJECT_ROOT, "reports", "6_subgroup_single_predictor_analysis")
OUT_DATA = os.path.join(REPORT_DIR, "data")
OUT_FIG = os.path.join(REPORT_DIR, "figures")
for d in (OUT_DATA, OUT_FIG):
    os.makedirs(d, exist_ok=True)

FDR_MIN_N = 1000          # BH-FDR applied only when the test's sample has at least this many participants
CV_SPLITS, CV_REPEATS = 10, 3

GROUPS = {
    "total": ("Total analysis base", lambda d: d),
    "healthy": ("Healthy group (no diabetes + pre-diabetes / lifestyle)", lambda d: d[d["any_diabetes"] == 0]),
    "non_healthy": ("Non-healthy group (T2D non-insulin + T2D insulin)", lambda d: d[d["any_diabetes"] == 1]),
}

# predictor -> (label, family, band)
PREDICTORS = {
    HBA1C: ("HbA1c (%)", "HbA1c", "-"),
    "mean_glucose": ("Mean glucose (mg/dL)", "CGM level", "-"),
    "gmi": ("GMI (%)", "CGM level", "-"),
    "nocturnal_mean": ("Nocturnal mean 00-06h (mg/dL)", "CGM level", "-"),
    "glucose_sd": ("Glucose SD, pooled (mg/dL)", "CGM variability", "-"),
    "avg_daily_sd": ("Avg. daily SD (mg/dL)", "CGM variability", "-"),
    "glucose_cv": ("CV (%)", "CGM variability", "-"),
    "mean_to_sd_ratio": ("Mean / SD ratio", "CGM variability", "-"),
    "avg_daily_mean_to_sd": ("Avg. daily mean / SD", "CGM variability", "-"),
    "mag_mg_dl_per_h": ("MAG (mg/dL/h)", "CGM variability", "-"),
    "avg_daily_range": ("Avg. daily range (mg/dL)", "CGM variability", "-"),
    "sd_of_daily_means": ("SD of daily means (mg/dL)", "CGM variability", "-"),
    "tir_overall": ("Time in range 70-180, pooled (%)", "Range 70-180", "70-180"),
    "avg_daily_tir": ("Avg. daily time in range 70-180 (%)", "Range 70-180", "70-180"),
    "any_below_54": ("Any reading < 54 during wear (0/1)", "Band < 54", "<54"),
    "pct_severe_hypo": ("Time < 54, pooled (%)", "Band < 54", "<54"),
    "avg_daily_pct_below_54": ("Avg. daily time < 54 (%)", "Band < 54", "<54"),
    "pct_mod_hypo": ("Time 54-69, pooled (%)", "Band 54-69", "54-69"),
    "avg_daily_pct_54_69": ("Avg. daily time 54-69 (%)", "Band 54-69", "54-69"),
    "tbr_below_70": ("Time < 70, pooled (%)", "Band < 70", "<70"),
    "avg_daily_tbr": ("Avg. daily time < 70 (%)", "Band < 70", "<70"),
    "pct_54_250": ("Time 54-250, pooled (%)", "Band 54-250", "54-250"),
    "avg_daily_pct_54_250": ("Avg. daily time 54-250 (%)", "Band 54-250", "54-250"),
    "pct_mod_hyper": ("Time 181-250, pooled (%)", "Band 181-250", "181-250"),
    "avg_daily_pct_181_250": ("Avg. daily time 181-250 (%)", "Band 181-250", "181-250"),
    "tar_above_180": ("Time > 180, pooled (%)", "Band > 180", ">180"),
    "avg_daily_tar": ("Avg. daily time > 180 (%)", "Band > 180", ">180"),
    "nocturnal_tar": ("Nocturnal time > 180 (%)", "Band > 180", ">180"),
    "any_above_250": ("Any reading > 250 during wear (0/1)", "Band > 250", ">250"),
    "pct_severe_hyper": ("Time > 250, pooled (%)", "Band > 250", ">250"),
    "avg_daily_pct_above_250": ("Avg. daily time > 250 (%)", "Band > 250", ">250"),
}
BANDS = ["<54", "54-69", "<70", "70-180", "181-250", ">180", ">250", "54-250"]
BAND_POOLED = {"<54": "pct_severe_hypo", "54-69": "pct_mod_hypo", "<70": "tbr_below_70", "70-180": "tir_overall",
               "181-250": "pct_mod_hyper", ">180": "tar_above_180", ">250": "pct_severe_hyper", "54-250": "pct_54_250"}


def cross_validate(formula, df, y, kind):
    if kind == "ols":
        it = RepeatedKFold(n_splits=CV_SPLITS, n_repeats=CV_REPEATS, random_state=7).split(df)
    else:
        it = RepeatedStratifiedKFold(n_splits=CV_SPLITS, n_repeats=CV_REPEATS, random_state=7).split(df, df[y])
    scores = []
    for tr, te in it:
        try:
            m = fit_ml(formula, df.iloc[tr], kind)
            pred = np.asarray(m.predict(df.iloc[te]))
            if kind == "ols":
                scores.append(r2_score(df.iloc[te][y], pred))
            elif df.iloc[te][y].nunique() == 2:
                scores.append(roc_auc_score(df.iloc[te][y], pred))
        except Exception:
            pass
    return float(np.mean(scores)) if scores else np.nan


def band_feasibility(base):
    rows = []
    for gkey, (glabel, gsel) in GROUPS.items():
        d = gsel(base)
        for band in BANDS:
            col = BAND_POOLED[band]
            v = d[col].dropna()
            rows.append({"group": gkey, "group_label": glabel, "band": band, "metric": col, "n": len(v),
                         "n_any_time": int((v > 0).sum()), "pct_any_time": float((v > 0).mean() * 100),
                         "n_ge_1pct": int((v >= 1).sum()), "n_ge_5pct": int((v >= 5).sum()), "n_ge_10pct": int((v >= 10).sum()),
                         "mean_pct_time": float(v.mean()), "median_pct_time": float(v.median()),
                         "p90_pct_time": float(v.quantile(0.90)), "max_pct_time": float(v.max()),
                         "median_pct_time_among_exposed": float(v[v > 0].median()) if (v > 0).any() else np.nan,
                         "n_readings_below_54_total": int(d["n_readings_below_54"].sum()) if band == "<54" else np.nan,
                         "n_readings_above_250_total": int(d["n_readings_above_250"].sum()) if band == ">250" else np.nan})
    fe = pd.DataFrame(rows)
    fe["enough_for_regression"] = np.where(fe["n_ge_1pct"] >= 100, "yes (>= 100 participants with >= 1% time)",
                                           np.where(fe["n_any_time"] >= 100, "marginal (>= 100 with any time, < 100 with >= 1%)", "no"))
    fe.to_csv(os.path.join(OUT_DATA, "band_feasibility.csv"), index=False)
    return fe


def run_models(base, out_name="single_predictor_results_all_groups.csv", cohort="all", cohort_label="All (analysis base)",
               cv_splits=None, cv_repeats=None, verbose=True):
    global CV_SPLITS, CV_REPEATS
    if cv_splits:
        CV_SPLITS, CV_REPEATS = cv_splits, cv_repeats or 1
    rows = []
    for gkey, (glabel, gsel) in GROUPS.items():
        dg = gsel(base)
        for dom, y, kind, lab, ef, ec in OUTCOMES:
            covf = COV_FORMULA + ef
            d_out = dg.dropna(subset=[y] + BASE_COVS + ec).copy()
            if kind == "logit":
                d_out[y] = d_out[y].astype(int)
            if len(d_out) < 60 or (kind == "logit" and d_out[y].nunique() < 2):
                continue
            if verbose:
                print(f"  {cohort:18s} {gkey:12s} {lab[:45]:45s} n={len(d_out)}")
            # covariates-only and HbA1c-only references computed once on the full outcome sample and reused
            # whenever a predictor has no additional missingness (the usual case)
            try:
                m0_full = fit_ml(f"{y} ~ {covf}", d_out, kind)
                mh_full = fit_ml(f"{y} ~ {covf} + {HBA1C}", d_out, kind)
                cv0_full = cross_validate(f"{y} ~ {covf}", d_out, y, kind)
            except Exception as e:      # e.g. separation / singular design in a small cohort
                rows.append({"cohort": cohort, "cohort_label": cohort_label, "group": gkey, "group_label": glabel, "domain": dom, "outcome": y,
                             "label": lab, "kind": kind, "predictor": "(all)", "predictor_label": "(all)", "family": "-", "band": "-", "n": len(d_out),
                             "skipped_reason": f"reference model failed in this cohort: {type(e).__name__}"})
                continue
            for pr, (plab, fam, band) in PREDICTORS.items():
                if pr not in d_out.columns:
                    continue
                d = d_out.dropna(subset=[pr])
                if len(d) < 60 or (kind == "logit" and d[y].sum() < 15):
                    rows.append({"cohort": cohort, "cohort_label": cohort_label, "group": gkey, "group_label": glabel, "domain": dom, "outcome": y, "label": lab, "kind": kind,
                                 "predictor": pr, "predictor_label": plab, "family": fam, "band": band, "n": len(d),
                                 "skipped_reason": "sample too small (< 60 participants or < 15 events)"})
                    continue
                if d[pr].std(ddof=1) == 0:
                    rows.append({"cohort": cohort, "cohort_label": cohort_label, "group": gkey, "group_label": glabel, "domain": dom, "outcome": y, "label": lab, "kind": kind,
                                 "predictor": pr, "predictor_label": plab, "family": fam, "band": band, "n": len(d),
                                 "skipped_reason": "predictor constant in this cohort"})
                    continue
                if band != "-" and (d[pr] > 0).sum() < 30:       # band with almost no exposure -> skip, recorded in feasibility
                    rows.append({"cohort": cohort, "cohort_label": cohort_label, "group": gkey, "group_label": glabel, "domain": dom, "outcome": y, "label": lab, "kind": kind,
                                 "predictor": pr, "predictor_label": plab, "family": fam, "band": band, "n": len(d),
                                 "skipped_reason": "fewer than 30 participants with any time in band"})
                    continue
                try:
                    m = fit(f"{y} ~ {covf} + {pr}", d, kind)
                    mml = fit_ml(f"{y} ~ {covf} + {pr}", d, kind)
                    if len(d) == len(d_out):
                        m0, mh, cv0 = m0_full, mh_full, cv0_full
                    else:
                        m0 = fit_ml(f"{y} ~ {covf}", d, kind)
                        mh = fit_ml(f"{y} ~ {covf} + {HBA1C}", d, kind)
                        cv0 = cross_validate(f"{y} ~ {covf}", d, y, kind)
                    if pr == HBA1C:
                        mh = mml
                except Exception as e:
                    rows.append({"cohort": cohort, "cohort_label": cohort_label, "group": gkey, "group_label": glabel, "domain": dom, "outcome": y, "label": lab, "kind": kind,
                                 "predictor": pr, "predictor_label": plab, "family": fam, "band": band, "n": len(d), "skipped_reason": f"fit error: {e!r}"[:80]})
                    continue
                sd_x = float(d[pr].std(ddof=1))
                r = slope_row(m, pr, sd_x, kind)
                r.update({"cohort": cohort, "cohort_label": cohort_label, "group": gkey, "group_label": glabel, "domain": dom, "outcome": y, "label": lab, "kind": kind,
                          "predictor": pr, "predictor_label": plab, "family": fam, "band": band, "n": len(d),
                          "events": int(d[y].sum()) if kind == "logit" else np.nan, "sd_x": sd_x,
                          "n_exposed_gt0": int((d[pr] > 0).sum()) if band != "-" else np.nan,
                          "test": "HC3 t" if kind == "ols" else "Wald z",
                          "aic": float(mml.aic), "delta_aic_vs_covariates": float(mml.aic - m0.aic),
                          "delta_aic_vs_hba1c_model": float(mml.aic - mh.aic) if len(d.dropna(subset=[HBA1C])) == len(d) else np.nan,
                          "adj_r2": float(mml.rsquared_adj) if kind == "ols" else np.nan,
                          "adj_r2_covariates_only": float(m0.rsquared_adj) if kind == "ols" else np.nan,
                          "auc_in_sample": float(roc_auc_score(d[y], mml.predict(d))) if kind == "logit" else np.nan,
                          "cv_score": cross_validate(f"{y} ~ {covf} + {pr}", d, y, kind),
                          "cv_score_covariates_only": cv0,
                          "skipped_reason": ""})
                rows.append(r)
    res = pd.DataFrame(rows)
    ok = res["skipped_reason"].fillna("") == ""
    res["fdr_applied"] = ok & (res["n"] >= FDR_MIN_N)
    for fam_name, keys in (("q_bh_group_all_tests", ["group"]),
                           ("q_bh_group_outcome", ["group", "outcome"]),
                           ("q_bh_group_predictor", ["group", "predictor"]),
                           ("q_bh_group_band", ["group", "band"])):
        res[fam_name] = np.nan
        sub = res[res["fdr_applied"]]
        for _, idx in sub.groupby(keys).groups.items():
            idx = list(idx)
            if len(idx) >= 2:
                res.loc[idx, fam_name] = multipletests(res.loc[idx, "p"], method="fdr_bh")[1]
            elif len(idx) == 1:
                res.loc[idx, fam_name] = res.loc[idx, "p"]
    # informational BH q over all valid tests in each population, computed regardless of the n >= FDR_MIN_N rule
    res["q_bh_informational_group_all"] = np.nan
    for _, idx in res[ok].groupby("group").groups.items():
        idx = list(idx)
        if len(idx) >= 2:
            res.loc[idx, "q_bh_informational_group_all"] = multipletests(res.loc[idx, "p"], method="fdr_bh")[1]
    res["sig_raw_05"] = ok & (res["p"] < 0.05)
    res["sig_fdr_05_group_all"] = res["q_bh_group_all_tests"] < 0.05
    res["sig_fdr_05_group_outcome"] = res["q_bh_group_outcome"] < 0.05
    res.to_csv(os.path.join(OUT_DATA, out_name), index=False)
    return res


def summarise(res, suffix=""):
    ok = res[res["skipped_reason"].fillna("") == ""]
    counts = ok.groupby("group").agg(tests=("p", "size"), sig_raw=("sig_raw_05", "sum"),
                                     fdr_applied=("fdr_applied", "sum"), sig_fdr_all=("sig_fdr_05_group_all", "sum"),
                                     sig_fdr_outcome=("sig_fdr_05_group_outcome", "sum"), n_min=("n", "min"), n_max=("n", "max")).reset_index()
    counts.to_csv(os.path.join(OUT_DATA, f"significance_counts_by_group{suffix}.csv"), index=False)
    # signed -log10 p matrix per group
    ok = ok.copy()
    ok["signed_log10p"] = -np.log10(ok["p"].clip(1e-300)) * np.sign(ok["beta_raw"])
    ok.to_csv(os.path.join(OUT_DATA, f"single_predictor_results_clean{suffix}.csv"), index=False)
    return counts, ok


def make_figures(ok, fe):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8.5, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#b5b4b0",
                         "xtick.color": "#52514e", "ytick.color": "#52514e", "figure.facecolor": "white"})
    labs = [l for _, _, _, l, _, _ in OUTCOMES]
    preds = list(PREDICTORS)
    # Fig 1: signed -log10 p heatmaps, one per group
    fig, axes = plt.subplots(1, 3, figsize=(20, 0.42 * len(preds) + 2.5), sharey=True)
    for ax, (gkey, (glabel, _)) in zip(axes, GROUPS.items()):
        sub = ok[ok.group == gkey]
        piv = sub.pivot_table(index="predictor", columns="label", values="signed_log10p").reindex(index=preds, columns=labs)
        q = sub.pivot_table(index="predictor", columns="label", values="q_bh_group_all_tests").reindex(index=preds, columns=labs)
        pv = sub.pivot_table(index="predictor", columns="label", values="p").reindex(index=preds, columns=labs)
        im = ax.imshow(piv.values.astype(float), cmap="RdBu_r", vmin=-8, vmax=8, aspect="auto")
        for i in range(piv.shape[0]):
            for j in range(piv.shape[1]):
                p = pv.values[i, j]; qq = q.values[i, j]
                if np.isnan(p):
                    ax.text(j, i, "·", ha="center", va="center", fontsize=7, color="#8a8987")
                    continue
                mark = ("**" if (not np.isnan(qq) and qq < 0.05) else ("*" if p < 0.05 else ""))
                ax.text(j, i, f"{p:.2g}{mark}", ha="center", va="center", fontsize=5.6,
                        color="white" if abs(piv.values[i, j]) > 4.5 else "#0b0b0b")
        ax.set_xticks(range(len(labs))); ax.set_xticklabels([l.split(" (")[0] for l in labs], rotation=60, ha="right", fontsize=7.5)
        ax.set_title(f"{glabel}\n(n = {int(sub['n'].min()):,}-{int(sub['n'].max()):,}; FDR {'applied' if sub['fdr_applied'].any() else 'not applied (n < ' + str(FDR_MIN_N) + ')'})", fontsize=8.5, loc="left")
    axes[0].set_yticks(range(len(preds))); axes[0].set_yticklabels([PREDICTORS[p][0] for p in preds], fontsize=7.5)
    cb = fig.colorbar(im, ax=axes, fraction=0.012, pad=0.01); cb.set_label("signed -log10 p (sign = direction of slope)", fontsize=8)
    fig.suptitle("Fig. 1  Single-predictor covariate-adjusted tests by population. Cell = raw p; * raw p < 0.05; ** BH-FDR q < 0.05 (family = all tests in the population)",
                 fontsize=9.5, x=0.01, ha="left")
    fig.savefig(os.path.join(OUT_FIG, "fig1_heatmap_single_predictor_by_group.png"), dpi=170, bbox_inches="tight"); plt.close(fig)

    # Fig 2: per-SD effects of the six headline predictors across the three groups, per outcome
    head = [HBA1C, "mean_glucose", "glucose_sd", "avg_daily_sd", "tir_overall", "avg_daily_tir"]
    cols = {"total": "#8a8987", "healthy": "#1baf7a", "non_healthy": "#eb6834"}
    fig, axes = plt.subplots(nrows=(len(labs) + 2) // 3, ncols=3, figsize=(14, 3.1 * ((len(labs) + 2) // 3)))
    axes = axes.ravel()
    for ax, lab in zip(axes, labs):
        ys = np.arange(len(head))[::-1]
        for off, gkey in zip((0.25, 0.0, -0.25), ["total", "healthy", "non_healthy"]):
            sub = ok[(ok.label == lab) & (ok.group == gkey)].set_index("predictor").reindex(head)
            kind = ok[ok.label == lab]["kind"].iloc[0]
            if kind == "logit":
                est, lo, hi = np.log(sub["or_per_sd"]), np.log(sub["or_ci_low"]), np.log(sub["or_ci_high"])
            else:
                est, lo, hi = sub["beta_per_sd"], sub["ci_low_per_sd"], sub["ci_high_per_sd"]
            for yv, e, l, h, p in zip(ys, est, lo, hi, sub["p"]):
                if np.isnan(e):
                    continue
                ax.plot([l, h], [yv + off, yv + off], color=cols[gkey], lw=1.6)
                ax.plot(e, yv + off, "o", color=cols[gkey], ms=4, mec="white", mew=0.6)
        ax.axvline(0, color="#b5b4b0", lw=1, ls="--")
        ax.set_yticks(ys); ax.set_yticklabels([PREDICTORS[p][0] for p in head], fontsize=7.5)
        ax.set_title(lab, fontsize=8, loc="left")
        ax.set_xlabel("log-OR per 1 SD" if kind == "logit" else "change per 1 SD of predictor", fontsize=7.5)
    for ax in axes[len(labs):]:
        ax.axis("off")
    from matplotlib.lines import Line2D
    fig.legend(handles=[Line2D([], [], marker="o", ls="", color=c, label=GROUPS[g][0]) for g, c in cols.items()], loc="upper right", fontsize=8, frameon=False)
    fig.suptitle("Fig. 2  Headline predictors entered one at a time: per-SD effects (95% CI) in the total, healthy and non-healthy populations", fontsize=9.5, x=0.01, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.965]); fig.savefig(os.path.join(OUT_FIG, "fig2_forest_headline_predictors_by_group.png"), dpi=170); plt.close(fig)

    # Fig 3: band feasibility
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
    for ax, (gkey, (glabel, _)) in zip(axes, GROUPS.items()):
        sub = fe[fe.group == gkey].set_index("band").reindex(BANDS)
        x = np.arange(len(BANDS)); w = 0.27
        ax.bar(x - w, sub["n_any_time"], width=w, color="#2a78d6", label="any time in band")
        ax.bar(x, sub["n_ge_1pct"], width=w, color="#eb6834", label=">= 1% of time")
        ax.bar(x + w, sub["n_ge_5pct"], width=w, color="#1baf7a", label=">= 5% of time")
        ax.axhline(100, color="#8a8987", lw=1, ls="--")
        ax.set_xticks(x); ax.set_xticklabels(BANDS); ax.set_title(f"{glabel} (n = {int(sub['n'].max()):,})", fontsize=8.5, loc="left")
    axes[0].set_ylabel("participants"); axes[0].legend(fontsize=8, frameon=False)
    fig.suptitle("Fig. 3  How many participants have CGM time in each glucose band (dashed = 100-participant feasibility line)", fontsize=9.5, x=0.01, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.94]); fig.savefig(os.path.join(OUT_FIG, "fig3_band_feasibility.png"), dpi=170); plt.close(fig)


def main():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_multimodal_dataset.csv"), low_memory=False)
    core = ["mean_glucose", "mean_to_sd_ratio", "avg_daily_tir", "avg_daily_sd"]
    base = df[df["has_cgm"] == 1].dropna(subset=[HBA1C] + core + BASE_COVS).copy()      # identical to Phase 5 analysis base
    print(f"analysis base n = {len(base)}; healthy = {(base.any_diabetes == 0).sum()}; non-healthy = {(base.any_diabetes == 1).sum()}")
    base.to_csv(os.path.join(OUT_DATA, "analysis_base_sample.csv"), index=False)
    fe = band_feasibility(base)
    print(fe[["group", "band", "n", "n_any_time", "n_ge_1pct", "n_ge_5pct", "enough_for_regression"]].to_string())
    res = run_models(base)
    counts, ok = summarise(res)
    print(counts.to_string())
    make_figures(ok, fe)
    with open(os.path.join(OUT_DATA, "config.json"), "w") as f:
        json.dump({"FDR_MIN_N": FDR_MIN_N, "cv": f"{CV_REPEATS} x {CV_SPLITS}-fold", "predictors": PREDICTORS, "groups": {k: v[0] for k, v in GROUPS.items()},
                   "n_base": int(len(base)), "n_healthy": int((base.any_diabetes == 0).sum()), "n_non_healthy": int((base.any_diabetes == 1).sum())}, f, indent=1)
    print("done")


if __name__ == "__main__":
    main()
