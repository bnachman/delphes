#!/usr/bin/env python3
"""Generate Phase-3 baseline and uncertainty Delphes cards.

v1 scope: applies the verified momentum-resolution revisions (charged hadron,
electron, muon) for ATLAS and CMS -- the most discrepant, cleanest-to-revise
blocks. Every change keeps the original value in an inline comment and is tagged
REVIEW where the change is large (factor >~1.5 or a functional-form change).
Other measured blocks are left at their current values (the baseline card equals
the stock card for those); their proposed revisions are documented in
findings_summary.md / review_highly_discrepant.md and applied in a later pass
after review.

The uncertainty card is the +1 sigma "pessimistic detector" variant: each
revised resolution coefficient is scaled up by the block's relative uncertainty
(plot-read terms default to 15%, calibration-level constant terms to 5%). Run
baseline vs uncertainty to get a one-sided resolution systematic; mirror for the
down side.
"""
import re, os

CARDS = "/home/user/delphes/cards"

def fmt(x):
    """Compact number formatting matching the card style."""
    if x == 0:
        return "0.0"
    s = f"{x:.6g}"
    return s

def formula(coeffs):
    """Build a Delphes ResolutionFormula string from 3 (eta_lo,eta_hi,a,b) rows."""
    lines = []
    pad = " " * 25
    for i, (elo, ehi, a, b) in enumerate(coeffs):
        if elo == 0.0:
            cond = f"(abs(eta) <= {fmt(ehi)})"
        else:
            cond = f"(abs(eta) > {fmt(elo)} && abs(eta) <= {fmt(ehi)})"
        term = f"{cond} * (pt > 0.1) * sqrt({fmt(a)}^2 + pt^2*{fmt(b)}^2)"
        prefix = "                  " if i == 0 else pad
        suffix = " +" if i < len(coeffs) - 1 else ""
        lines.append(prefix + term + suffix)
    return "set ResolutionFormula {" + "\n".join(lines).lstrip() if False else \
           "set ResolutionFormula {" + "\n".join(
               (l if i else l) for i, l in enumerate(lines)) + "}"

# Each entry: card, module, current (eta_lo,eta_hi,a,b) rows, baseline rows,
# rel_unc, review flag, multiline source/comment.
BLOCKS = [
  # ---------------- ATLAS ----------------
  dict(card="ATLAS", module="ChargedHadronMomentumSmearing", review=True, runc=0.15,
       source=["ATLAS inner-detector track momentum resolution, sigma_ID/pt = a(eta) (+) b(eta)*pt.",
               "Source: arXiv:1404.4562 (EPJC 74 (2014) 3130) Eq.(2), Figs. 17-18 (plot-read, muon-ID tracks)."],
       cur=[(0,0.5,0.06,1.3e-3),(0.5,1.5,0.10,1.7e-3),(1.5,2.5,0.25,3.1e-3)],
       new=[(0,0.5,0.015,3.9e-4),(0.5,1.5,0.025,6.1e-4),(1.5,2.5,0.040,9.0e-4)],
       note="REVIEW: ~3x reduction vs stock. Measured anchors are muon-ID tracks; confirm intended hadron-specific term before adopting."),
  dict(card="ATLAS", module="ElectronMomentumSmearing", review=True, runc=0.15,
       source=["Electron resolution is ECAL-dominated -> ~flat vs pt; the stock b*pt term is a tracker artefact (removed).",
               "Source: arXiv:1902.04655 / 1407.5063 (ATLAS e/gamma); effective resolution ~0.7-1.5% (barrel-endcap)."],
       cur=[(0,0.5,0.03,1.3e-3),(0.5,1.5,0.05,1.7e-3),(1.5,2.5,0.15,3.1e-3)],
       new=[(0,0.5,0.007,0.0),(0.5,1.5,0.012,0.0),(1.5,2.5,0.015,0.0)],
       note="REVIEW: functional-form change (b set to 0; constant term lowered). Calorimeter resolution, not tracker."),
  dict(card="ATLAS", module="MuonMomentumSmearing", review=True, runc=0.05,
       source=["Combined-muon pt resolution. Source: arXiv:1603.05598 (EPJC 76 (2016) 292) Sec. 8.2; form arXiv:1404.4562 Eq.(2).",
               "Central floor raised 0.010 -> 0.017 to match measured 1.7% (J/psi) / 2.3% (Z); mid/endcap unchanged."],
       cur=[(0,0.5,0.010,1.0e-4),(0.5,1.5,0.015,1.5e-4),(1.5,2.5,0.025,3.5e-4)],
       new=[(0,0.5,0.017,1.0e-4),(0.5,1.5,0.015,1.5e-4),(1.5,2.5,0.025,3.5e-4)],
       note="REVIEW: central floor change only (combined-muon vs ID-only ambiguity; see provenance)."),
  # ---------------- CMS ----------------
  dict(card="CMS", module="ChargedHadronMomentumSmearing", review=True, runc=0.15,
       source=["CMS tracker track momentum resolution. Source: arXiv:1405.6569 (JINST 9 (2014) P10009).",
               "Proposed source-faithful a,b per eta region (verified Phase 2)."],
       cur=[(0,0.5,0.06,1.3e-3),(0.5,1.5,0.10,1.7e-3),(1.5,2.5,0.25,3.1e-3)],
       new=[(0,0.5,0.009,2.3e-4),(0.5,1.5,0.015,4.2e-4),(1.5,2.5,0.023,9.5e-4)],
       note="REVIEW: ~3x reduction vs stock (constant terms ~1-2.3%, slopes ~2-10e-4/GeV)."),
  dict(card="CMS", module="ElectronMomentumSmearing", review=True, runc=0.15,
       source=["Electron resolution is ECAL-dominated -> ~flat vs pt; stock b*pt term is a tracker artefact (removed).",
               "Source: arXiv:1502.02701 (JINST 10 (2015) P06005) Sec. 4.8; effective resolution ~1.6-1.7% (barrel) to ~4.5% (endcap)."],
       cur=[(0,0.5,0.03,1.3e-3),(0.5,1.5,0.05,1.7e-3),(1.5,2.5,0.15,3.1e-3)],
       new=[(0,0.5,0.017,0.0),(0.5,1.5,0.025,0.0),(1.5,2.5,0.045,0.0)],
       note="REVIEW: functional-form change (b set to 0; constant term lowered to measured effective resolution)."),
  dict(card="CMS", module="MuonMomentumSmearing", review=True, runc=0.05,
       source=["CMS muon resolution. Source: arXiv:1804.04528 (JINST 13 (2018) P06015) Sec. 7.",
               "Barrel floor 1% exact (kept); endcap floor 0.025 -> 0.030 to match measured ~3%."],
       cur=[(0,0.5,0.010,1.0e-4),(0.5,1.5,0.015,1.5e-4),(1.5,2.5,0.025,3.5e-4)],
       new=[(0,0.5,0.010,1.0e-4),(0.5,1.5,0.015,1.5e-4),(1.5,2.5,0.030,3.5e-4)],
       note="REVIEW: endcap floor change only (2.5% -> 3.0%)."),
]

def scaled(coeffs, runc):
    """+1 sigma: scale a and b up by relative uncertainty (b=0 stays 0)."""
    return [(elo, ehi, round(a*(1+runc), 6), round(b*(1+runc), 7)) for (elo, ehi, a, b) in coeffs]

def replace_formula(text, module, new_formula, header_lines):
    """Replace the ResolutionFormula inside the named module with new_formula,
    prepending header_lines as comments. Raises if the module/formula not found."""
    mi = text.find(f"module MomentumSmearing {module}")
    if mi < 0:
        raise RuntimeError(f"module {module} not found")
    # match the REAL formula (line-start `set ...`), not the commented `# set ...` template
    m = re.search(r"\n([ \t]*)set ResolutionFormula \{", text[mi:])
    if not m:
        raise RuntimeError(f"ResolutionFormula not found in {module}")
    fi = mi + m.start() + 1  # +1 to skip the leading newline
    close = text.find("}", fi)
    if close < 0:
        raise RuntimeError(f"unterminated formula in {module}")
    header = "".join("  # " + h + "\n" for h in header_lines)
    return text[:fi] + header + "  " + new_formula + text[close+1:]

def build(variant):
    assert variant in ("baseline", "uncertainty")
    for card in ("ATLAS", "CMS"):
        src = os.path.join(CARDS, f"delphes_card_{card}.tcl")
        with open(src) as f:
            text = f.read()
        banner = (
            f"# === {card} {variant} card (Phase-3 v1, generated) ===\n"
            f"# Derived from delphes_card_{card}.tcl. Momentum-resolution blocks revised\n"
            f"# from verified provenance (docs/card_provenance/). "
            + ("Central source-faithful values.\n" if variant == "baseline"
               else "+1 sigma 'pessimistic detector' variant (resolutions scaled up).\n")
            + "# Other measured blocks are unchanged here; see findings_summary.md.\n"
            + "# Lines tagged REVIEW are large changes flagged for human check.\n#\n"
        )
        for b in BLOCKS:
            if b["card"] != card:
                continue
            coeffs = b["new"] if variant == "baseline" else scaled(b["new"], b["runc"])
            cur_str = ", ".join(f"a={fmt(a)},b={fmt(bb)}" for (_,_,a,bb) in b["cur"])
            hdr = ["PROVENANCE (run1, independently verified):"] + b["source"]
            hdr.append(f"stock value was: {cur_str}")
            if variant == "uncertainty":
                hdr.append(f"this card: +1 sigma (x{1+b['runc']:.2f}) on the baseline central values.")
            if b["review"]:
                hdr.append(b["note"])
            text = replace_formula(text, b["module"], formula(coeffs), hdr)
        # prepend banner after the first line (keep any shebang/first comment)
        text = banner + text
        out = os.path.join(CARDS, f"delphes_card_{card}_{variant}.tcl")
        with open(out, "w") as f:
            f.write(text)
        print(f"wrote {out}")

build("baseline")
build("uncertainty")
print("done")
