# Citable, uncertainty-aware Delphes cards for ATLAS & CMS (Run 2)

Goal: produce **new baseline + uncertainty Delphes cards** for the ATLAS and CMS
Run-2 detectors in which every hard-coded parameterization (resolutions,
efficiencies, tagging rates, scale factors) is traceable to a public,
peer-reviewed or collaboration-endorsed source, carries an **uncertainty**, and
is documented well enough to support an accompanying instrumentation paper
(target: *JINST*).

This directory holds the **provenance layer** that sits between the published
literature and the `.tcl` cards:

| File | Purpose |
|------|---------|
| `README.md` | This file — scope, methodology, schema, workflow. |
| `audit_ATLAS.md` | Inventory of every parameterization in `cards/delphes_card_ATLAS.tcl`, its current value, and any reference already present. |
| `audit_CMS.md` | Same for `cards/delphes_card_CMS.tcl`. |
| `provenance_schema.md` | The per-parameter record schema agents fill in (value, uncertainty, source, locator, verification). |
| `sources.bib` | BibTeX for every source cited (to be grown as sourcing proceeds). |

Scope for this pass (per project decision): **ATLAS + CMS Run-2 only**
(`delphes_card_ATLAS.tcl`, `delphes_card_CMS.tcl`). PileUp / HL-LHC / Phase-II
variants are explicitly out of scope for now.

## Why this is a good agentic task

The work is a tight, repeatable loop per parameter:

1. Identify the authoritative public measurement (performance paper, PUB/DP note, TDR).
2. Locate the exact table/figure giving the fitted value + uncertainty.
3. Extract value and uncertainty; reconcile units/definition with the Delphes formula.
4. **Adversarially verify** the extracted number against the source (independent agent re-reads the cited table and must agree, or the entry is rejected).
5. Record the result in the provenance schema; update the card comment.

Steps 1–4 fan out across hundreds of parameters and parallelize cleanly. Step 4
(independent verification) is mandatory — it is what keeps a language model from
inventing a plausible-but-wrong resolution number.

## Workflow / phases

- **Phase 0 — Audit (this commit).** Enumerate every parameterization in both
  cards, record current value + functional form + any existing in-card reference.
  Output: `audit_ATLAS.md`, `audit_CMS.md`. **No new physics numbers are
  invented here.**
- **Phase 1 — Source mapping.** For each audited parameter, identify the
  best public source and the exact locator (table/figure/eqn). Reviewed by you
  before extraction.
- **Phase 2 — Extraction + verification.** Pull value + uncertainty; a second
  independent agent re-verifies each against the source. Discrepancies with the
  current card value are flagged, not silently overwritten.
- **Phase 3 — New cards + paper.** Emit `delphes_card_ATLAS_baseline.tcl` /
  `..._uncertainty.tcl` (and CMS) with cited values + uncertainty handles, and
  draft the JINST manuscript from the provenance tables.

## Card categories that need citable values

From the Phase-0 audit, the parameterizations group into:

1. **Detector geometry / B-field** — `Radius`, `HalfLength`, `Bz` (TDR facts; no resolution uncertainty, but cite).
2. **Tracking / reconstruction efficiency** — η,pᴛ step functions for charged hadrons, electrons, muons, photons.
3. **Track momentum resolution** — `sqrt(a² + (b·pᴛ)²)` per η bin (charged hadron, electron, muon).
4. **Calorimeter energy resolution** — ECal/HCal `sqrt((S/√E)² + (N/E)² + C²)`-type stochastic / noise / constant terms per η region.
5. **Calorimeter granularity** — `EtaPhiBins` tower maps (geometry; cite TDR).
6. **Isolation working points** — `DeltaRMax`, `PTRatioMax`, `PTMin`.
7. **Jet energy scale** — `ScaleFormula` coefficients.
8. **Flavor tagging** — b-tag efficiency + c/light mistag, τ-tag efficiency + mistag, all pᴛ-dependent.

## Conventions

- A parameter that is a *choice* (jet radius `ParameterR`, algorithm, `JetPTMin`,
  isolation cone) is tagged `choice` — documented, but not "measured", so no
  uncertainty is assigned.
- A parameter that is a *measured detector property* is tagged `measured` and
  must carry a value, an uncertainty, and a verified source before it enters a
  baseline card.
- "Current ref in card" records only what the existing `.tcl` already says — it
  is **not** an endorsement that the value matches that reference. Verifying that
  match is Phase 2 work.
