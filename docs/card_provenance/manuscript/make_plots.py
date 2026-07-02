#!/usr/bin/env python3
"""Generate the manuscript figures (saved as PDF for LaTeX inclusion).

All curves use the Delphes functional forms; 'card' values are the current
hard-coded coefficients, 'proposed' values are the source-faithful revisions
recorded in run1_provenance.json / findings_summary.md (Phase-2, verified).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 9, "axes.titlesize": 9, "axes.labelsize": 9,
    "legend.fontsize": 7.5, "figure.dpi": 150, "lines.linewidth": 1.4,
})

def momres(pt, a, b):
    """Track momentum resolution sigma(pt)/pt = sqrt(a^2 + (b*pt)^2)."""
    return np.sqrt(a**2 + (b * pt)**2)

pt = np.logspace(np.log10(1), np.log10(1000), 200)

# ---------------------------------------------------------------------------
# Fig 1: charged-hadron track momentum resolution, card vs proposed (CMS+ATLAS)
# CMS proposed (verified, arXiv:1405.6569): a=0.009/0.015/0.023, b=2.3/4.2/9.5e-4
# ATLAS proposed = the shipped baseline card: sqrt(0.013^2+(3.6e-4 pt)^2) x eta-shape
# (physicist notebook); per-bin effective (a,b) at the bin-representative eta-shape factor.
# ---------------------------------------------------------------------------
regions = [r"$|\eta|\leq0.5$", r"$0.5<|\eta|\leq1.5$", r"$1.5<|\eta|\leq2.5$"]
card = [(0.06, 1.3e-3), (0.10, 1.7e-3), (0.25, 3.1e-3)]
cms_prop = [(0.009, 2.3e-4), (0.015, 4.2e-4), (0.023, 9.5e-4)]
# ATLAS inner-detector (muon-ID) plateau read from Figs 17-18 of 1404.4562
atlas_prop = [(0.013, 3.6e-4), (0.0147, 4.07e-4), (0.0221, 6.12e-4)]

fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.5), sharey=True)
colors = ["#1f77b4", "#d62728", "#2ca02c"]
for ax, reg, (ac, bc), (a1, b1), (a2, b2), col in zip(
        axes, regions, card, cms_prop, atlas_prop, colors):
    ax.plot(pt, 100*momres(pt, ac, bc), color="k", ls="--", label="Delphes card")
    ax.plot(pt, 100*momres(pt, a1, b1), color="#1f77b4", label="CMS proposed (1405.6569)")
    ax.plot(pt, 100*momres(pt, a2, b2), color="#d62728", label="ATLAS proposed (fine $\\eta$-shape)")
    ax.set_xscale("log")
    ax.set_xlabel(r"$p_\mathrm{T}$ [GeV]")
    ax.set_title(reg)
    ax.grid(True, which="both", ls=":", alpha=0.4)
    ax.set_ylim(0, 40)
axes[0].set_ylabel(r"$\sigma(p_\mathrm{T})/p_\mathrm{T}$ [%]")
axes[0].legend(loc="upper left", frameon=False)
fig.suptitle("Charged-hadron track momentum resolution: card is ~3x too pessimistic", y=1.02)
fig.tight_layout()
fig.savefig("fig_momres.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Fig 2: electron resolution — wrong functional form
# Card: tracker form rises with pt (b*pt term). Measured: ECAL-dominated, ~flat/falling.
# CMS measured effective resolution ~1.6-1.7% (barrel) to ~4.5% (endcap), flat vs pt.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4.0, 2.8))
# stock card (tracker form, rising with pt -- WRONG for a calorimeter)
ax.plot(pt, 100*momres(pt, 0.03, 1.3e-3), "k--", label="stock card, barrel (rising, wrong form)")
ax.plot(pt, 100*momres(pt, 0.15, 3.1e-3), color="0.5", ls="--",
        label="stock card, endcap (rising, wrong form)")
# proposed energy-dependent form sqrt(S^2/pt + C^2) -- improves with pt (correct)
def eres(pt, S, C): return np.sqrt(S**2/pt + C**2)
ax.plot(pt, 100*eres(pt, 0.101, 0.010), color="#1f77b4", lw=1.8,
        label=r"proposed ATLAS barrel $\sqrt{0.101^2/p_T+0.010^2}$")
ax.plot(pt, 100*eres(pt, 0.101, 0.018), color="#d62728", lw=1.8,
        label=r"proposed ATLAS endcap $\sqrt{0.101^2/p_T+0.018^2}$")
ax.set_xscale("log")
ax.set_xlabel(r"$p_\mathrm{T}$ [GeV]")
ax.set_ylabel(r"$\sigma(p_\mathrm{T})/p_\mathrm{T}$ [%]")
ax.set_ylim(0, 20)
ax.set_title("Electron resolution: tracker form (stock) vs. calorimeter form (proposed)")
ax.grid(True, which="both", ls=":", alpha=0.4)
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig("fig_eres.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Fig 3: per-block verdict composition (stacked bar of coefficient verdicts)
# Counts taken from the Phase-2 summary (run1).
# ---------------------------------------------------------------------------
blocks = [
    ("ATLAS ch-had trkEff", [1,2,0,0,0,3]),
    ("ATLAS e trkEff",      [1,0,3,0,3,0]),
    ("ATLAS mu trkEff",     [4,0,0,0,2,0]),
    ("ATLAS ch-had momRes", [0,0,6,0,0,0]),
    ("ATLAS e momRes",      [0,0,3,3,0,0]),
    ("ATLAS ECal",          [4,1,0,0,0,0]),
    ("ATLAS HCal",          [1,3,2,0,0,1]),
    ("ATLAS e idEff",       [1,1,1,0,0,1]),
    ("ATLAS mu idEff",      [1,0,3,0,0,0]),
    ("ATLAS JES",           [1,0,0,2,0,0]),
    ("ATLAS b-tag",         [5,0,0,0,0,0]),
    ("ATLAS tau",           [1,2,1,0,0,0]),
    ("CMS ch-had trkEff",   [5,1,0,0,0,0]),
    ("CMS e trkEff",        [3,0,1,0,3,0]),
    ("CMS mu trkEff",       [2,0,1,0,4,0]),
    ("CMS ch-had momRes",   [0,0,6,0,0,0]),
    ("CMS e momRes",        [0,0,3,3,0,0]),
    ("CMS ECal",            [1,0,3,0,6,0]),
    ("CMS HCal",            [1,1,2,0,0,0]),
    ("CMS e idEff",         [3,1,0,0,0,0]),
    ("CMS mu idEff",        [1,0,2,0,0,1]),
    ("CMS JES",             [0,0,0,0,1,0]),
    ("CMS tau",             [2,2,1,0,0,0]),
]
labels = ["consistent", "optimistic", "pessimistic", "wrong form", "no source", "cannot determine"]
cmap = ["#2ca02c", "#ff7f0e", "#1f77b4", "#d62728", "#7f7f7f", "#bcbd22"]
names = [b[0] for b in blocks]
data = np.array([b[1] for b in blocks])
fig, ax = plt.subplots(figsize=(7.2, 5.2))
left = np.zeros(len(blocks))
y = np.arange(len(blocks))[::-1]
for i, (lab, c) in enumerate(zip(labels, cmap)):
    ax.barh(y, data[:, i], left=left, color=c, label=lab, height=0.72)
    left += data[:, i]
ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=7)
ax.set_xlabel("number of coefficients")
ax.set_title("Per-block coefficient verdicts (Phase-2, all verified)")
ax.legend(ncol=3, loc="lower right", frameon=False, fontsize=7)
ax.grid(True, axis="x", ls=":", alpha=0.4)
fig.tight_layout()
fig.savefig("fig_verdicts.pdf", bbox_inches="tight")
plt.close(fig)

print("wrote fig_momres.pdf, fig_eres.pdf, fig_verdicts.pdf")
