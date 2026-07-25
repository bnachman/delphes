#!/usr/bin/env python3
"""Fold the measured ATLAS charged-hadron tracking blocks into the generated
ATLAS baseline/uncertainty cards, replacing the coarse versions with the fine
eta-binned forms + per-eta systematic bands.

Run AFTER generate_cards.py. Source (updated 2026-07, reviewer request, Ben):
  ATLAS Collaboration, "Track and Vertex Reconstruction with the ATLAS Inner
  Detector," CERN-EP-2026-096, arXiv:2605.07585 (submitted to JINST), the
  authoritative Run 2 (2015-18) + Run 3 (2022-26) ID performance paper.
  - tracking efficiency: Fig. 16(a) (eff vs eta, Loose WP, minimum-bias sim) x
    Fig. 16(b) (eff vs pt turn-on); systematics from Fig. 17 (material/physics-list).
  - momentum resolution: Fig. 15(c) relative q/pt resolution vs eta (Final Tracks,
    ttbar, <mu> in [0,80], averaged over the full pt spectrum).
This SUPERSEDES the earlier hand-derivation (ATL-PHYS-PUB-2015-051 Fig 1a/1b for
efficiency; ID TDR + PERF-2015-10 figaux_11a for resolution), which was Run-1/early
Run-2 and, for the momentum resolution, based on muon-ID tracks rather than hadrons.
"""
import re

CARD_BASE = "/home/user/delphes/cards/delphes_card_ATLAS_baseline.tcl"
CARD_UNC  = "/home/user/delphes/cards/delphes_card_ATLAS_uncertainty.tcl"

# ---- charged-hadron tracking efficiency: arXiv:2605.07585 Fig. 16 (Loose WP) ----
# eta plateau (high-pt), read from Fig. 16(a) dark squares (Loose, min-bias sim):
# central |eta|<1.5 ~0.85, falling to ~0.67-0.72 forward (local bump near |eta|=2.0).
ETA_EFF_BASE = [(0.00,0.20,0.850),(0.20,0.40,0.855),(0.40,0.60,0.855),(0.60,0.80,0.845),
                (0.80,1.00,0.835),(1.00,1.20,0.820),(1.20,1.40,0.810),(1.40,1.60,0.780),
                (1.60,1.80,0.750),(1.80,2.00,0.700),(2.00,2.20,0.720),(2.20,2.40,0.700),(2.40,2.50,0.670)]
# +1 sigma material/physics-list systematic (Fig. 17): ~0.5% central rising to ~2% forward.
ETA_EFF_UP   = [(0.00,0.20,0.855),(0.20,0.40,0.860),(0.40,0.60,0.860),(0.60,0.80,0.851),
                (0.80,1.00,0.842),(1.00,1.20,0.828),(1.20,1.40,0.819),(1.40,1.60,0.790),
                (1.60,1.80,0.762),(1.80,2.00,0.714),(2.00,2.20,0.735),(2.20,2.40,0.716),(2.40,2.50,0.690)]
# pt turn-on, read from Fig. 16(b) (eta-integrated Loose): rises from ~0.70 at
# 0.5 GeV to the ~0.80 plateau by ~1 GeV. Normalized to the plateau downstream.
PT_EFF_BASE = [(0.40,0.55,0.70),(0.55,0.65,0.75),(0.65,0.75,0.78),(0.75,0.85,0.795),(0.85,0.95,0.80),
               (0.95,1.05,0.805),(1.05,1.15,0.80),(1.15,1.25,0.80),(1.25,1.35,0.80),(1.35,1.45,0.80),
               (1.45,1.75,0.80),(1.75,2.25,0.80),(2.25,2.75,0.80),(2.75,3.25,0.80),(3.25,3.75,0.80),
               (3.75,4.50,0.80)]
PT_EFF_UP   = [(0.40,0.55,0.71),(0.55,0.65,0.76),(0.65,0.75,0.79),(0.75,0.85,0.805),(0.85,0.95,0.81),
               (0.95,1.05,0.815),(1.05,1.15,0.81),(1.15,1.25,0.81),(1.25,1.35,0.81),(1.35,1.45,0.81),
               (1.45,1.75,0.81),(1.75,2.25,0.81),(2.25,2.75,0.81),(2.75,3.25,0.81),(3.25,3.75,0.81),
               (3.75,4.50,0.81)]
PLATEAU_BASE, PLATEAU_UP = 0.80, 0.81

# ---- charged-hadron momentum resolution: arXiv:2605.07585 Fig. 15(c) ----
# Relative q/pt resolution vs eta (Final Tracks, ttbar <mu> in [0,80], pt-averaged).
# Since the ttbar track spectrum is soft, the average ~ the low-pt (constant/
# multiple-scattering) term, so it primarily fixes a(eta); the high-pt slope b is
# NOT constrained by this pt-averaged figure and is carried over from the ATLAS ID
# parametrization (1404.4562 Eq.2). Central ~1.9%, rising to ~4.6% at |eta|=2.5.
RES_A, RES_B = 0.019, 0.00036          # a = Fig.15(c) central; b = ID-form slope (see note)
# eta-shape: (eta_lo, eta_hi, abs_value_of_a, up_factor); normalized to central RES_A.
RES_ETA = [(0.00,0.50,0.019,1.05),(0.50,1.00,0.022,1.05),(1.00,1.50,0.028,1.07),
           (1.50,2.00,0.037,1.08),(2.00,2.50,0.046,1.10)]
RES_NORM = 0.019

def eff_formula(eta_tab, pt_tab, plateau):
    """Delphes EfficiencyFormula = eta_plateau(eta) * pt_turnon(pt)/plateau."""
    eta_terms = ["(abs(eta) > 2.5) * (0.00)"]
    for lo, hi, v in eta_tab:
        cond = f"(abs(eta) <= {hi:.2f})" if lo == 0.0 else f"(abs(eta) > {lo:.2f} && abs(eta) <= {hi:.2f})"
        eta_terms.append(f"{cond} * ({v:.3f})")
    eta_expr = " + \n    ".join(eta_terms)
    pt_terms = ["(pt <= 0.40) * (0.00)"]
    for lo, hi, v in pt_tab:
        pt_terms.append(f"(pt > {lo:.2f} && pt <= {hi:.2f}) * ({v/plateau:.4f})")
    pt_terms.append(f"(pt > 4.50) * (1.0)")
    pt_expr = " + \n    ".join(pt_terms)
    return ("set EfficiencyFormula {\n  ( " + eta_expr + " )\n  *\n  ( " + pt_expr + " )\n  }")

def res_formula(up=False):
    terms = []
    for lo, hi, val, fac in RES_ETA:
        shape = (val / RES_NORM) * (fac if up else 1.0)
        cond = f"(abs(eta) <= {hi:.2f})" if lo == 0.0 else f"(abs(eta) > {lo:.2f} && abs(eta) <= {hi:.2f})"
        terms.append(f"{cond} * ({shape:.4f})")
    shape_expr = " + \n    ".join(terms)
    return (f"set ResolutionFormula {{\n  (pt > 0.1) * sqrt({RES_A}^2 + pt^2*{RES_B}^2)\n  *\n  ( " + shape_expr + " )\n  }")

def header(lines):
    return "".join("  # " + l + "\n" for l in lines)

def replace_block(text, module, formula_kw, new_formula, hdr):
    """Replace `set <formula_kw> { ... }` inside `module ... <module>` (skips commented templates)."""
    mi = text.find(module)
    if mi < 0:
        raise RuntimeError(f"module {module} not found")
    m = re.search(rf"\n([ \t]*)set {formula_kw} \{{", text[mi:])
    if not m:
        raise RuntimeError(f"{formula_kw} not found in {module}")
    fi = mi + m.start() + 1
    close = text.find("}", fi)
    return text[:fi] + hdr + "  " + new_formula + text[close+1:]

EFF_HDR = [
  "PROVENANCE (arXiv:2605.07585, ATLAS ID Track+Vertex Reco, Run 2+3; reviewer: Ben):",
  "Charged-hadron tracking efficiency, fine |eta| bins (plateau) x pt turn-on.",
  "Source: arXiv:2605.07585 Fig. 16(a) (eff vs eta, Loose WP, min-bias sim) x Fig. 16(b)",
  "(eff vs pt turn-on); systematic band from Fig. 17. Central |eta|<1.5 plateau ~0.85,",
  "forward falling to ~0.67-0.72. SUPERSEDES the earlier PUB-2015-051 (0.91) hand-derivation.",
  "Dense-environment losses NOT included. Replaces the stock 2-bin 0.95/0.85.",
]
RES_HDR = [
  "PROVENANCE (arXiv:2605.07585, ATLAS ID Track+Vertex Reco, Run 2+3; reviewer: Ben):",
  "Charged-hadron track momentum resolution = sqrt(a^2+(b*pt)^2) * etashape(eta).",
  "a(eta) from arXiv:2605.07585 Fig. 15(c) (relative q/pt resolution vs eta, Final Tracks,",
  "ttbar <mu> in [0,80], pt-averaged): ~1.9% central rising to ~4.6% at |eta|=2.5.",
  "b=3.6e-4 (high-pt slope) is NOT constrained by that pt-averaged figure; carried over",
  "from the ATLAS ID parametrization 1404.4562 Eq.(2). SUPERSEDES the earlier muon-ID-based",
  "a=0.013 (PERF-2015-10) -- charged hadrons (soft spectrum + pileup) resolve worse than muon-ID tracks.",
]

# ALL-DEGRADE uncertainty convention: the uncertainty card degrades the detector,
# so tracking efficiency is shifted DOWN by 1 sigma (mirror of the figure's up-band),
# while the resolution is scaled UP. This keeps the _uncertainty card a coherent
# one-sided (pessimistic) systematic. Normalise the pt turn-on to PLATEAU_BASE in
# both cards so the shift is applied cleanly.
def _mirror_down(base_tab, up_tab):
    return [(lo, hi, round(2*b - u, 4)) for (lo, hi, b), (_, _, u) in zip(base_tab, up_tab)]
ETA_EFF_DN = _mirror_down(ETA_EFF_BASE, ETA_EFF_UP)
PT_EFF_DN  = _mirror_down(PT_EFF_BASE, PT_EFF_UP)

for card, up in ((CARD_BASE, False), (CARD_UNC, True)):
    with open(card) as f:
        text = f.read()
    eff = eff_formula(ETA_EFF_DN if up else ETA_EFF_BASE, PT_EFF_DN if up else PT_EFF_BASE,
                      PLATEAU_BASE)
    res = res_formula(up=up)
    eh = EFF_HDR + (["this card: -1 sigma per-eta band (efficiency DEGRADED, all-degrade convention)."] if up else [])
    rh = RES_HDR + (["this card: +1 sigma per-eta band (etashape x 1.03-1.10 from the figure band)."] if up else [])
    text = replace_block(text, "module Efficiency ChargedHadronTrackingEfficiency",
                         "EfficiencyFormula", eff, header(eh))
    text = replace_block(text, "module MomentumSmearing ChargedHadronMomentumSmearing",
                         "ResolutionFormula", res, header(rh))
    with open(card, "w") as f:
        f.write(text)
    print(f"updated {card}")
print("done")
