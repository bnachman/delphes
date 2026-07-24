# Closure test — plan (stock vs revised card vs public full-sim)

**Question this answers:** do the card revisions change a *physics observable*
enough to matter, and does the revised card land closer to public full-simulation
than the stock card? This is the figure that turns "the coefficient was wrong"
into "and here is the observable-level consequence."

**Verdict on whether it's needed:** not required for the paper's provenance thesis
(the source overlays already prove the coefficient gaps). Worth **one** targeted
closure demonstration — not a broad multi-observable campaign.

---

## Recommended observable (primary): Z → μμ invariant-mass resolution

- **Why:** single, clean, calibration-grade observable; dominated by the muon
  momentum-resolution block we revised (ATLAS barrel floor 1.0%→1.7%); every
  experiment publishes the Z→μμ mass lineshape from full sim + data, so a
  **citable public comparison exists** (ATLAS: 1603.05598 / 2012.00578;
  CMS: 1804.04528). Directly exercises `MuonMomentumSmearing`.
- **Metric:** Gaussian (or Crystal-Ball) width of the reconstructed m_μμ peak,
  split by leading-muon |η| (barrel |η|<1.0 vs endcap). Compare:
  stock card · baseline card · published full-sim width.

## Secondary observable: charged-hadron track p_T resolution

- Exercises the biggest revision (`ChargedHadronMomentumSmearing`, ~3×). Cleanest
  as the single-track σ(p_T)/p_T vs p_T curve (what any track-based mass
  resolution inherits) overlaid on the published tracker-resolution figure
  (CMS 1405.6569; ATLAS PERF-2015-10). This is essentially the Appendix-A
  overlay promoted to a card-vs-card comparison.

---

## How to run it for real (Delphes + generator)

Requires ROOT + Delphes built, and a generator (Pythia8) or ready LHE/HepMC.
Not runnable in this session (no ROOT); this is the recipe for a collaborator.

1. **Sample:** ~1e5 Z→μμ events. Either
   - `DelphesPythia8 cards/<card> configs/pythia_z_mumu.cmnd out.root`, or
   - hand a Z→μμ HepMC/LHE to `DelphesHepMC2` / `DelphesLHEF`.
2. **Cards:** run three times — `delphes_card_ATLAS.tcl` (stock),
   `delphes_card_ATLAS_baseline.tcl` (revised), and (for the systematic)
   `delphes_card_ATLAS_uncertainty.tcl`. Repeat for CMS.
3. **Analyse:** from the `Muon` branch build m_μμ (opposite-sign pair), fit the
   peak per |η| region, tabulate the width. `examples/` has ROOT/uproot macros;
   uproot works without ROOT if only reading the output.
4. **Public reference:** overlay the published full-sim Z→μμ width (numbers in
   the muon papers above). Acceptance: **baseline width lands within the
   published full-sim width ± its uncertainty; stock is outside (too narrow).**
   That is the closure claim.
5. **Systematic band:** baseline vs uncertainty card gives the one-sided
   resolution systematic on the width — report it as the card's built-in error.

**Effort:** ~half a day for someone with a Delphes build. Michele's involvement
makes step 1 and the choice of citable full-sim reference low-friction.

---

## Standalone preview (this session, no Delphes)

`manuscript/closure_toy.py` reproduces the exact operation Delphes'
`MomentumSmearing` performs — scale each muon momentum by a Gaussian of relative
width σ/p_T = the card's `ResolutionFormula(pt,eta)` — on a toy Z→μμ sample, for
the stock vs baseline ATLAS card. It is **a preview of the effect size, not a
Delphes run**: no real detector geometry, acceptance, FSR, or backgrounds. Use it
to decide whether the full study above is worth doing. Output:
`manuscript/closure_toy.pdf`.

**Preview result (this session):**
- *Panel A — ATLAS Z→μμ, barrel, mass response (resolution isolated):* stock card
  gives σ(m_reco/m_gen) = **0.97%**, baseline **1.27%**. The baseline lands where
  the measured single-muon 1.7–2.3% (1603.05598) folds to on a pair (~1.2–1.6%);
  the stock card was **~30% too optimistic**. Note the *raw* Z-peak width barely
  moves (~0.1 GeV) because the 2.5 GeV Breit-Wigner dominates — so the muon
  revision matters for the resolution/response, not the visible peak width.
- *Panel B — CMS charged-hadron single-track σ(p_T)/p_T:* the stock vs baseline
  curves differ by the **~3×** headline factor across the spectrum — this is the
  big one, and it propagates into any track-based mass or MET observable.

**Takeaway for the "is a full sim needed?" decision:** the preview confirms the
effects are real and their *sizes* are as the source extraction predicts. A full
Delphes run would add (a) acceptance/efficiency folding and (b) a head-to-head vs
a *citable* public full-sim number — valuable for one figure, but not required to
establish the provenance claim. Recommend: do the single Z→μμ closure (½ day with
a Delphes build), skip a broad campaign.
