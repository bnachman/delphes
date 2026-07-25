# Reviewer sign-off — Delphes card provenance

**Goal:** every hard-coded coefficient in the ATLAS and CMS Delphes cards should
trace to a citable Run-2 measurement (value + uncertainty + exact locator).
Phase 0–2 did the source-mapping, extraction, and an *automated* adversarial
verification. **This file is the human sign-off layer**: two named reviewers per
experiment independently confirm each block before we consider it done.

- Reviewers: **ATLAS** — Ben, Elham · **CMS** — Gregor, Michele
- Every block has a **Lead** (does the deep check, writes the verdict) and a
  **2nd** (independent confirm). A block is `DONE` only when **both** sign.
- Michele is a Delphes author/maintainer → the convention-heavy CMS blocks
  (ECAL prefactor, HCAL, JES, and the Delphes functional forms) are led by him.

---

## What a reviewer does — per block (≈10–20 min each)

For each block you are **Lead** on:

1. **Open the source at the locator** given in the block's row of
   `findings_summary.md`. Confirm the *measured* value and its uncertainty match
   what we extracted. (The locator is exact — figure/table/section/page.)
2. **Look at the overlay** (if the block has one — see the Overlay column and
   `manuscript/` Appendix A). Does our card curve + band actually sit on the
   published data points? Flag if not.
3. **Judge the proposed revision** in `review_highly_discrepant.md` /
   `findings_summary.md`. Do you agree with the new value, the "keep current"
   call, or the functional-form change?
4. **Record your verdict** in the table below — replace `⬜ pending` in your
   column with one of:
   - `✅ agree` — extraction, source, and proposed revision all check out.
   - `✏️ revise: <value/reason>` — you'd use a different number/form (say what).
   - `❓ needs-more: <what>` — can't sign yet; name the missing input.
   Add your initials + date, e.g. `✅ agree — BPN 2026-07-28`.

For each block you are **2nd** on: independently repeat step 1 (and 2 if there's
an overlay). You don't have to re-derive the revision from scratch — you're
confirming the Lead's verdict is defensible against the source. Same notation.

**Where the material lives**
- Per-coefficient tables, sources, uncertainties, proposed values:
  `findings_summary.md` (search the block name, e.g. `## ATLAS.ElectronMomRes`).
- The big discrepancies, triaged with locators and Tier-1/2 status:
  `review_highly_discrepant.md`.
- Overlays (our curve on the real figure): `manuscript/` Appendix A, manifest in
  `validation_overlays.md`.
- Generated cards showing what's applied:
  `cards/delphes_card_{ATLAS,CMS}_{baseline,uncertainty}.tcl` (stock cards are
  untouched; every change carries an inline `# stock value was:` comment).

**Priority** — start at 🔴, then 🟠, then 🟢:
🔴 applied revision / functional-form change (biggest physics impact) ·
🟠 notable discrepancy, documented but not yet applied (needs your call) ·
🟢 verified consistent / "keep current" (a confirmation pass).

---

## ATLAS blocks — Lead/2nd: Ben & Elham

| Block | Lead | 2nd | Pri | Source locator (see findings_summary.md) | Overlay | Ben | Elham |
|-------|------|-----|-----|------------------------------------------|---------|-----|-------|
| ChargedHadronMomRes | Ben | Elham | 🔴 | **arXiv:2605.07585 Fig.15(c)** (Run 2+3; a(η)≈1.9%→4.6%); slope b from 1404.4562 | ⬜ todo (2605.07585 Fig.15c) | ✏️ source→2605.07585 (BPN) | ⬜ pending |
| ChargedHadronTrackingEff | Ben | Elham | 🔴 | **arXiv:2605.07585 Fig.16(a,b)** (Run 2+3, Loose WP; 0.85 central) + Fig.17 syst | ⬜ todo (2605.07585 Fig.16) | ✏️ source→2605.07585 (BPN) | ⬜ pending |
| MuonTrackingEff | Ben | Elham | 🟢 | 1603.05598 / 2012.00578 (reco eff ~99% Loose) | — (consistency) | ⬜ pending | ⬜ pending |
| MuonIDEff | Ben | Elham | 🟠 | 1603.05598 / 2012.00578 — card 0.95 vs Medium-WP 0.98 (WP-dependent) | — | ⬜ pending | ⬜ pending |
| BTagging | Ben | Elham | 🟠 | 1907.05120 Table 4 + Fig.8/10 (70% MV2 WP); high-pT falloff 0.086 | ✅ atlasbtag | ⬜ pending | ⬜ pending |
| JES | Ben | Elham | 🟠 | 1703.09665 / 2007.02645 — coeffs (3.0,0.2) unsupported, needs JER form | — | ⬜ pending | ⬜ pending |
| TauTagging | Ben | Elham | 🟠 | ATL-PHYS-PUB-2019-033 Table 2 (RNN Medium) — card consistent/conservative | — | ⬜ pending | ⬜ pending |
| ElectronMomRes | Elham | Ben | 🔴 | 2309.05471 §5.1/§7 Fig.16(b) — form → √(S²/pt+C²), S=0.101, C=0.010/0.012/0.018 | ✅ atlasel | ⬜ pending | ⬜ pending |
| ElectronIDEff | Elham | Ben | 🟠 | 1902.04655 §6.3, Fig.8 — card 0.95/0.85 vs Loose 0.93 / endcap ~0.90 | ✅ atlaseid | ⬜ pending | ⬜ pending |
| ElectronTrackingEff | Elham | Ben | 🟢 | 1902.04655 Fig.2/Fig.4 (εreco 96–99% for ET>15 GeV) | — | ⬜ pending | ⬜ pending |
| PhotonEff | Elham | Ben | 🟢 | 1810.05087 — tight photon ID; card 0.95/0.85 consistent | — (ID-vs-ET not isolated) | ⬜ pending | ⬜ pending |
| ECalRes | Elham | Ben | 🟢 | physics/0608012 Fig.19 + 2109.02551 Table 4 (EM 10.1%/0.2%, FCal 28.5%/3.5%) | — (formula, cross-check) | ⬜ pending | ⬜ pending |
| HCalRes | Elham | Ben | 🟠 | AtlFast3 / TileCal — check S/N/C vs published; card is effective not test-beam | — | ⬜ pending | ⬜ pending |

*Muon momentum resolution:* revised in `generate_cards.py` (MuonMomentumSmearing;
barrel floor 0.010→0.017 from 1603.05598 §8.2, review_highly_discrepant #6/#7).
Ben to sign it together with MuonIDEff.

## CMS blocks — Lead/2nd: Gregor & Michele

| Block | Lead | 2nd | Pri | Source locator (see findings_summary.md) | Overlay | Gregor | Michele |
|-------|------|-----|-----|------------------------------------------|---------|--------|---------|
| ChargedHadronTrackingEff | Gregor | Michele | 🟢 | 1405.6569 Fig.11 (tracking eff vs pT/η) | ✅ cmstrkeff | ⬜ pending | ⬜ pending |
| ElectronMomRes | Gregor | Michele | 🔴 | 2012.06888 Fig.11 — form → √(S²/pt+C²), S=0.028, C=0.020/0.025/0.050 | ✅ cmsel | ⬜ pending | ⬜ pending |
| ElectronIDEff | Gregor | Michele | 🟠 | 2012.06888 Fig.26 | ✅ cmseid | ⬜ pending | ⬜ pending |
| ElectronTrackingEff | Gregor | Michele | 🟢 | 2012.06888 (reco eff) | — | ⬜ pending | ⬜ pending |
| MuonIDEff | Gregor | Michele | 🟢 | 1804.04528 §7 (Loose >99% / Tight 95–99%) | — (consistency) | ⬜ pending | ⬜ pending |
| MuonTrackingEff | Gregor | Michele | 🟢 | 1804.04528 | — (consistency) | ⬜ pending | ⬜ pending |
| PhotonEff | Gregor | Michele | 🟢 | 2012.06888 Fig.27 | ✅ cmsphot | ⬜ pending | ⬜ pending |
| ChargedHadronMomRes | Michele | Gregor | 🔴 | 1405.6569 (7 TeV, tracker unchanged); Run-2 corrob. 1712.07158 (~1.5% central). CAVEAT: 68% vs 90% interval on slopes | 🔸 (muon Fig.9, same tracker) | ⬜ pending | ⬜ pending |
| ECalRes | Michele | Gregor | 🟠 | 2012.06888 Fig.33 — S/N/C are **effective**, (1+0.64η²) is a Delphes construct; no Run-2 S/N/C exists | — (formula) | ⬜ pending | ⬜ pending |
| HCalRes | Michele | Gregor | 🟠 | PF 1706.04965 Eq.(2) (110%/√E⊕9%) — card 150%/5%; no peer-reviewed Run-2 per-η source | — | ⬜ pending | ⬜ pending |
| JES | Michele | Gregor | 🟠 | No Run-2 paper; best = CMS-DP-2021-033 (DP-note). Card-implied JER ~3× measured | — | ⬜ pending | ⬜ pending |
| BTagging | Michele | Gregor | 🟠 | 1712.07158 (DeepCSV Medium, Table 2/App.A) — c-mistag amplitude 0.25 vs ~0.15 | ⬜ todo (DeepCSV) | ⬜ pending | ⬜ pending |
| TauTagging | Michele | Gregor | 🟠 | 1809.02816 §5.2 — τ→jet mistag 0.01 vs 0.003 (tight WP) | ✅ cmstau | ⬜ pending | ⬜ pending |

---

## Progress

- ATLAS: 0 / 13 fully signed (both reviewers)
- CMS: 0 / 13 fully signed

Update the counts as blocks close. When a block is `✅ agree` by both reviewers,
mark it **DONE** in both columns. Disagreements (`✏️`/`❓`) stay open and get
discussed — escalate a contentious block to its own GitHub issue if the thread
gets long.

## Open inputs still needed (don't block review)
- ~~ATLAS PERF-2015-10 figaux_11a~~ — **no longer needed**: the ATLAS charged-hadron
  momentum-resolution and tracking-efficiency blocks are now sourced from
  arXiv:2605.07585 (Figs. 15c / 16), which is on arXiv and fully accessible. The
  overlays can be produced here from that paper (todo).
- CMS b-tag DeepCSV overlay (1712.07158 Fig.17) — page render to retry.
