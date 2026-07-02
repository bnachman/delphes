#!/usr/bin/env python3
"""Fold the physicist's hand-derived ATLAS charged-hadron tracking blocks
(reference_ATLASUncerts.ipynb) into the generated ATLAS baseline/uncertainty
cards, replacing the coarse versions with the fine eta-binned forms + per-eta
systematic bands.

Run AFTER generate_cards.py. Sources (from the notebook):
  - tracking efficiency: ATL-PHYS-PUB-2015-051 Fig 1a/1b (loose)
  - momentum resolution: pt-shape from ATLAS ID TDR (via arXiv:1703.10485);
    eta-shape + per-bin uncertainty from ATLAS PERF-2015-10 figaux_11a
"""
import re

CARD_BASE = "/home/user/delphes/cards/delphes_card_ATLAS_baseline.tcl"
CARD_UNC  = "/home/user/delphes/cards/delphes_card_ATLAS_uncertainty.tcl"

# ---- charged-hadron tracking efficiency (notebook EfficiencyFormula_new / _systup) ----
# eta plateau (pt>~5 GeV): (eta_lo, eta_hi, eff)
ETA_EFF_BASE = [(0.00,0.20,0.91),(0.20,0.40,0.91),(0.40,0.60,0.91),(0.60,0.80,0.90),
                (0.80,1.00,0.89),(1.00,1.20,0.88),(1.20,1.40,0.87),(1.40,1.60,0.84),
                (1.60,1.80,0.80),(1.80,2.00,0.78),(2.00,2.20,0.78),(2.20,2.40,0.79),(2.40,2.50,0.73)]
ETA_EFF_UP   = [(0.00,0.20,0.91),(0.20,0.40,0.91),(0.40,0.60,0.91),(0.60,0.80,0.91),
                (0.80,1.00,0.90),(1.00,1.20,0.89),(1.20,1.40,0.87),(1.40,1.60,0.85),
                (1.60,1.80,0.81),(1.80,2.00,0.79),(2.00,2.20,0.80),(2.20,2.40,0.81),(2.40,2.50,0.75)]
# pt turn-on, normalized to the plateau (notebook divides by 0.90 baseline / 0.91 up)
PT_EFF_BASE = [(0.40,0.55,0.78),(0.55,0.65,0.84),(0.65,0.75,0.85),(0.75,0.85,0.86),(0.85,0.95,0.86),
               (0.95,1.05,0.86),(1.05,1.15,0.87),(1.15,1.25,0.87),(1.25,1.35,0.87),(1.35,1.45,0.87),
               (1.45,1.75,0.88),(1.75,2.25,0.88),(2.25,2.75,0.88),(2.75,3.25,0.89),(3.25,3.75,0.89),
               (3.75,4.50,0.89)]
PT_EFF_UP   = [(0.40,0.55,0.79),(0.55,0.65,0.85),(0.65,0.75,0.86),(0.75,0.85,0.87),(0.85,0.95,0.87),
               (0.95,1.05,0.87),(1.05,1.15,0.88),(1.15,1.25,0.88),(1.25,1.35,0.88),(1.35,1.45,0.88),
               (1.45,1.75,0.88),(1.75,2.25,0.89),(2.25,2.75,0.89),(2.75,3.25,0.90),(3.25,3.75,0.90),
               (3.75,4.50,0.90)]
PLATEAU_BASE, PLATEAU_UP = 0.90, 0.91

# ---- charged-hadron momentum resolution (notebook ResolutionFormula_new / _systup) ----
RES_A, RES_B = 0.013, 0.00036          # ID TDR pt-shape
# eta-shape: (eta_lo, eta_hi, value); normalized to central 1.73; up = factor*value
RES_ETA = [(0.00,0.63,1.73,1.05),(0.63,1.05,1.86,1.03),(1.05,1.46,1.95,1.09),
           (1.46,1.89,2.18,1.05),(1.89,2.31,2.89,1.06),(2.31,2.50,4.16,1.10)]
RES_NORM = 1.73

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
  "PROVENANCE (physicist hand-derivation, reference_ATLASUncerts.ipynb):",
  "Charged-hadron tracking efficiency, fine |eta| bins (plateau) x pt turn-on.",
  "Source: ATL-PHYS-PUB-2015-051 (Early ID Tracking Performance, 13 TeV) Fig 1a/1b (Loose).",
  "Dense-environment effects (PERF-2015-08) NOT included. Replaces the stock 2-bin 0.95/0.85.",
]
RES_HDR = [
  "PROVENANCE (physicist hand-derivation, reference_ATLASUncerts.ipynb):",
  "Charged-hadron track momentum resolution = sqrt(a^2+(b*pt)^2) * etashape(eta).",
  "pt-shape a=0.013, b=3.6e-4 from the ATLAS ID TDR (via arXiv:1703.10485 Eq.2);",
  "fine |eta| shape + per-bin uncertainty from ATLAS PERF-2015-10 figaux_11a.",
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
