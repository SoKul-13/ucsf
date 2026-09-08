"""
Phase 6b - Actual-value glucose cohorts
=======================================
Repeats the Phase 6 single-predictor grid (31 measures x 14 outcomes x total / healthy / non-healthy)
inside cohorts defined by each participant's OWN CGM readings:

  normal_70_180   every valid reading within 70-180 mg/dL            (n = 39  -> too small, reported as not possible)
  near_normal     >= 99 % of readings within 70-180 (substitute)     (n = 454)
  within_54_250   no reading < 54 and none > 250                     (n = 890)
  hypo_below_54   at least one reading < 54 (hypoglycaemia exposure)  (n = 638)
  hyper_above_250 at least one reading > 250 (hyperglycaemia exposure)(n = 795)

Inside every cohort the standard 70-180 time-in-range metrics remain part of the predictor set.
FDR rule from Phase 6 (BH only when n >= 1,000) is applied; no cohort reaches it, so an
informational BH q is also stored (`q_bh_informational_group_all`) and labelled as such.
"""

import os
import sys
import json
import numpy as np
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import run_phase6_analysis as P  # noqa: E402

MIN_COHORT_N = 100         # below this the cohort is reported as "not possible"

COHORTS = {
    "normal_70_180": ("Normal range only: every reading within 70-180", lambda d: d[d["tir_overall"] >= 100 - 1e-9]),
    "near_normal_99": ("Near-normal substitute: >= 99% of readings within 70-180", lambda d: d[d["tir_overall"] >= 99]),
    "within_54_250": ("Within 54-250: no reading < 54 and none > 250", lambda d: d[(d["any_below_54"] == 0) & (d["any_above_250"] == 0)]),
    "hypo_below_54": ("Hypoglycaemia exposure: at least one reading < 54", lambda d: d[d["any_below_54"] == 1]),
    "hyper_above_250": ("Hyperglycaemia exposure: at least one reading > 250", lambda d: d[d["any_above_250"] == 1]),
}


def cohort_sizes(base):
    rows = []
    for ck, (clabel, csel) in COHORTS.items():
        d = csel(base)
        rows.append({"cohort": ck, "cohort_label": clabel, "n_total": len(d), "n_healthy": int((d.any_diabetes == 0).sum()),
                     "n_non_healthy": int((d.any_diabetes == 1).sum()), "n_moca": int(d.moca_total.notna().sum()),
                     "cesd_ge10_events": int(d.cesd10_ge10.sum()), "moca_lt26_events": int(d.cognitive_impairment.sum()),
                     "n_env": int(d.env_pm25_mean.notna().sum()), "n_steps": int(d.steps_per_day.notna().sum()),
                     "n_resting_hr": int(d.hr_resting_proxy.notna().sum()), "n_sleep": int(d.sleep_tst_min.notna().sum()),
                     "feasible": "yes" if len(d) >= MIN_COHORT_N else f"no - fewer than {MIN_COHORT_N} participants"})
    # overlaps
    hypo = base["any_below_54"] == 1; hyper = base["any_above_250"] == 1
    overlap = {"hypo_only": int((hypo & ~hyper).sum()), "hyper_only": int((hyper & ~hypo).sum()), "both": int((hypo & hyper).sum()),
               "neither (within 54-250)": int((~hypo & ~hyper).sum())}
    cs = pd.DataFrame(rows)
    cs.to_csv(os.path.join(P.OUT_DATA, "cohort_sizes.csv"), index=False)
    with open(os.path.join(P.OUT_DATA, "cohort_overlap.json"), "w") as f:
        json.dump(overlap, f, indent=1)
    return cs, overlap


def figures(allres, cs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8.5, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#b5b4b0",
                         "xtick.color": "#52514e", "ytick.color": "#52514e", "figure.facecolor": "white"})
    labs = [l for _, _, _, l, _, _ in P.OUTCOMES]
    preds = list(P.PREDICTORS)
    ok = allres[allres["skipped_reason"].fillna("") == ""].copy()
    ok["signed"] = -np.log10(ok["p"].clip(1e-300)) * np.sign(ok["beta_raw"])
    cohorts = [c for c in COHORTS if c in ok["cohort"].unique()]
    fig, axes = plt.subplots(1, len(cohorts), figsize=(6.5 * len(cohorts), 0.42 * len(preds) + 2.5), sharey=True)
    axes = np.atleast_1d(axes)
    for ax, ck in zip(axes, cohorts):
        sub = ok[(ok.cohort == ck) & (ok.group == "total")]
        piv = sub.pivot_table(index="predictor", columns="label", values="signed").reindex(index=preds, columns=labs)
        pv = sub.pivot_table(index="predictor", columns="label", values="p").reindex(index=preds, columns=labs)
        qq = sub.pivot_table(index="predictor", columns="label", values="q_bh_informational_group_all").reindex(index=preds, columns=labs)
        im = ax.imshow(piv.values.astype(float), cmap="RdBu_r", vmin=-6, vmax=6, aspect="auto")
        for i in range(piv.shape[0]):
            for j in range(piv.shape[1]):
                p = pv.values[i, j]
                if np.isnan(p):
                    ax.text(j, i, "·", ha="center", va="center", fontsize=7, color="#8a8987"); continue
                mark = "**" if (not np.isnan(qq.values[i, j]) and qq.values[i, j] < 0.05) else ("*" if p < 0.05 else "")
                ax.text(j, i, f"{p:.2g}{mark}", ha="center", va="center", fontsize=5.4, color="white" if abs(piv.values[i, j]) > 3.5 else "#0b0b0b")
        ax.set_xticks(range(len(labs))); ax.set_xticklabels([l.split(" (")[0] for l in labs], rotation=60, ha="right", fontsize=7.5)
        n = int(cs.loc[cs.cohort == ck, "n_total"].iloc[0])
        ax.set_title(f"{COHORTS[ck][0]}\n(total population, n = {n:,}; FDR rule not met, ** = informational BH q < 0.05)", fontsize=8, loc="left")
    axes[0].set_yticks(range(len(preds))); axes[0].set_yticklabels([P.PREDICTORS[p][0] for p in preds], fontsize=7.5)
    fig.colorbar(im, ax=axes, fraction=0.012, pad=0.01).set_label("signed -log10 p", fontsize=8)
    fig.suptitle("Fig. 4  Single-predictor tests inside the actual-value glucose cohorts (total population). Cell = raw p; * p < 0.05", fontsize=9.5, x=0.01, ha="left")
    fig.savefig(os.path.join(P.OUT_FIG, "fig4_heatmap_glucose_cohorts.png"), dpi=170, bbox_inches="tight"); plt.close(fig)

    # cohort size chart
    fig, ax = plt.subplots(figsize=(9, 3.6))
    x = np.arange(len(cs)); w = 0.28
    ax.bar(x - w, cs["n_healthy"], width=w, color="#1baf7a", label="healthy")
    ax.bar(x, cs["n_non_healthy"], width=w, color="#eb6834", label="non-healthy")
    ax.bar(x + w, cs["n_total"], width=w, color="#8a8987", label="total")
    ax.axhline(MIN_COHORT_N, color="#e34948", lw=1, ls="--"); ax.text(len(cs) - 0.5, MIN_COHORT_N + 15, f"feasibility line ({MIN_COHORT_N})", fontsize=7.5, ha="right", color="#e34948")
    ax.set_xticks(x); ax.set_xticklabels([c.replace("_", "\n", 1) for c in cs["cohort"]], fontsize=8); ax.set_ylabel("participants")
    ax.legend(fontsize=8, frameon=False)
    ax.set_title("Fig. 5  Size of the actual-value glucose cohorts by population", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(P.OUT_FIG, "fig5_glucose_cohort_sizes.png"), dpi=170); plt.close(fig)


def main():
    base = pd.read_csv(os.path.join(P.OUT_DATA, "analysis_base_sample.csv"), low_memory=False)
    cs, overlap = cohort_sizes(base)
    print(cs.to_string()); print(overlap)
    results = []
    for ck, (clabel, csel) in COHORTS.items():
        d = csel(base)
        if len(d) < MIN_COHORT_N:
            print(f"  cohort {ck}: n = {len(d)} -> not possible, skipped")
            continue
        res = P.run_models(d, out_name=f"cohort_{ck}_results.csv", cohort=ck, cohort_label=clabel, cv_splits=5, cv_repeats=2)
        results.append(res)
    allres = pd.concat(results, ignore_index=True)
    allres.to_csv(os.path.join(P.OUT_DATA, "cohort_all_results.csv"), index=False)
    ok = allres[allres["skipped_reason"].fillna("") == ""]
    counts = ok.groupby(["cohort", "group"]).agg(tests=("p", "size"), sig_raw=("sig_raw_05", "sum"), n_min=("n", "min"), n_max=("n", "max"),
                                                 sig_q_informational=("q_bh_informational_group_all", lambda s: int((s < 0.05).sum()))).reset_index()
    counts.to_csv(os.path.join(P.OUT_DATA, "cohort_significance_counts.csv"), index=False)
    print(counts.to_string())
    figures(allres, cs)
    print("done")


if __name__ == "__main__":
    main()
