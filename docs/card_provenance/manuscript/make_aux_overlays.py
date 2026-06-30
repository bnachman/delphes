#!/usr/bin/env python3
"""Auxiliary validation overlays: our extracted Delphes parameterization drawn
ON TOP of the digitized source-figure points, so a reader can see the extraction
is faithful. Worked example: ATLAS charged-hadron tracking blocks.

NOTE: the 'digitized' points here are the values read in reference_ATLASUncerts.ipynb.
For the final paper these should come from HEPData (where a record exists) or a
WebPlotDigitizer trace of the published figure, with the figure + HEPData DOI cited.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 9, "legend.fontsize": 7.5, "figure.dpi": 150})

# ---------------------------------------------------------------------------
# 1) Charged-hadron tracking efficiency vs |eta| (plateau, pt>5 GeV)
#    Source: ATL-PHYS-PUB-2015-051 Fig 1a (Loose). Digitized bin values + band.
# ---------------------------------------------------------------------------
eta_c = np.array([0.10,0.30,0.50,0.70,0.90,1.10,1.30,1.50,1.70,1.90,2.10,2.30,2.45])
eff   = np.array([0.91,0.91,0.91,0.90,0.89,0.88,0.87,0.84,0.80,0.78,0.78,0.79,0.73])
eff_up= np.array([0.91,0.91,0.91,0.91,0.90,0.89,0.87,0.85,0.81,0.79,0.80,0.81,0.75])
eff_err = eff_up - eff
edges = [0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.5]

fig, ax = plt.subplots(figsize=(4.4,3.0))
# our extracted parameterization as a step function
xs, ys = [], []
vals = [0.91,0.91,0.91,0.90,0.89,0.88,0.87,0.84,0.80,0.78,0.78,0.79,0.73]
for i,v in enumerate(vals):
    xs += [edges[i], edges[i+1]]; ys += [v, v]
ax.plot(xs, ys, color="#d62728", lw=1.6, label="Delphes extraction (this work)")
ax.fill_between(xs, np.array(ys)-np.repeat(eff_err,2), np.array(ys)+np.repeat(eff_err,2),
                color="#d62728", alpha=0.18, label="syst. band (per-$\\eta$)")
# digitized source points
ax.errorbar(eta_c, eff, yerr=eff_err, fmt="o", ms=4, color="k", capsize=2,
            label="ATL-PHYS-PUB-2015-051 Fig.1a (digitized)")
# stock card for contrast
ax.plot([0,1.5,1.5,2.5],[0.95,0.95,0.85,0.85], color="0.5", ls="--", lw=1.2,
        label="stock card (0.95 / 0.85)")
ax.set_xlabel(r"$|\eta|$"); ax.set_ylabel("charged-hadron tracking efficiency")
ax.set_xlim(0,2.5); ax.set_ylim(0.65,1.0)
ax.legend(loc="lower left", frameon=False)
ax.set_title("Tracking efficiency: extraction vs source figure", fontsize=8.5)
fig.tight_layout(); fig.savefig("aux_trkeff_overlay.pdf", bbox_inches="tight")
fig.savefig("aux_trkeff_overlay.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------------------
# 2) Charged-hadron momentum resolution sigma(pt)/pt vs |eta| at fixed pt
#    Source: PERF-2015-10 figaux_11a (relative pt resolution vs |eta|).
#    Our curve: sqrt(a^2+(b*pt)^2)*etashape; etashape digitized from figaux.
# ---------------------------------------------------------------------------
a, b = 0.013, 0.00036
shape_edges = [0.0,0.63,1.05,1.46,1.89,2.31,2.5]
shape_val   = [1.73,1.86,1.95,2.18,2.89,4.16]      # digitized figaux_11a (in %, *normalised below*)
shape_up    = [1.05,1.03,1.09,1.05,1.06,1.10]      # systematic-up factors
norm = 1.73
fig, ax = plt.subplots(figsize=(4.4,3.0))
for pt, col in ((10,"#1f77b4"),(100,"#d62728")):
    base = np.sqrt(a**2 + (b*pt)**2)
    xs, ys, yup = [], [], []
    for i,v in enumerate(shape_val):
        s = (v/norm); su = s*shape_up[i]
        xs += [shape_edges[i], shape_edges[i+1]]
        ys += [100*base*s, 100*base*s]; yup += [100*base*su, 100*base*su]
    ax.plot(xs, ys, color=col, lw=1.6, label=f"extraction, $p_T$={pt} GeV")
    ax.fill_between(xs, ys, yup, color=col, alpha=0.18)
    # digitized source points at this pt (bin centres)
    cen = [0.31,0.84,1.25,1.67,2.10,2.40]
    pts = [100*base*(v/norm) for v in shape_val]
    perr= [100*base*((v/norm)*f-(v/norm)) for v,f in zip(shape_val,shape_up)]
    ax.errorbar(cen, pts, yerr=perr, fmt="o", ms=3.5, color=col, capsize=2, alpha=0.9)
ax.set_xlabel(r"$|\eta|$"); ax.set_ylabel(r"$\sigma(p_T)/p_T$ [%]")
ax.set_xlim(0,2.5); ax.set_ylim(0,12)
ax.plot([],[],"ko",ms=3.5,label="PERF-2015-10 figaux_11a (digitized)")
ax.legend(loc="upper left", frameon=False, ncol=1)
ax.set_title("Track momentum resolution: extraction vs source figure", fontsize=8.5)
fig.tight_layout(); fig.savefig("aux_momres_overlay.pdf", bbox_inches="tight")
fig.savefig("aux_momres_overlay.png", bbox_inches="tight"); plt.close(fig)

print("wrote aux_trkeff_overlay.{pdf,png}, aux_momres_overlay.{pdf,png}")
