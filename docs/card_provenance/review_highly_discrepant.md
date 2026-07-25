# Highly-discrepant numbers — review checklist

These are the card values that disagree most with their verified source (factor
≳1.5, or a functional-form problem). Each row gives the stock card value, the
proposed source-faithful value, the exact source locator to check, and whether
it is **applied** in the generated `*_baseline.tcl` cards or only **documented**
(left at the stock value pending your review).

Verify against the locator; if you disagree, the stock value is preserved in an
inline `# stock value was:` comment in the baseline card for easy revert.
Full per-coefficient detail: `findings_summary.md` / `run1_provenance.json`.
**Sources standardized to Run-2 (13 TeV)** — see `run2_resourcing.md` for the
per-block re-sourcing (and the blocks where no Run-2 paper exists, kept Run-1
with a caveat).

## Tier 1 — applied in the baseline cards (resolution; biggest, cleanest)

| # | Quantity | Region | Card | Proposed | Source — locator | Why |
|---|----------|--------|------|----------|------------------|-----|
| 1 | Charged-hadron mom. res. **CMS** ($a$) | 0.5 / 1.5 / 2.5 | 0.06 / 0.10 / 0.25 | 0.009 / 0.015 / 0.023 | 1405.6569 (7 TeV; tracker unchanged), Run-2 corrob. 1712.07158 (~1.5% central) | ~3× too pessimistic |
| 2 | Charged-hadron mom. res. **CMS** ($b$, GeV⁻¹) | 0.5 / 1.5 / 2.5 | 1.3e-3 / 1.7e-3 / 3.1e-3 | 2.3e-4 / 4.2e-4 / 9.5e-4 | same | ~3–6× too large |
| 3 | Charged-hadron mom. res. **ATLAS** ($a$,$b$) | all | 0.06–0.25 / 1.3–3.1e-3 | **shipped:** $\sqrt{0.019^2+(3.6\!\times\!10^{-4}p_T)^2}\times\eta$-shape ($a$: 0.019/0.022/0.028/0.037/0.046) | **arXiv:2605.07585 Fig. 15(c)** (Run 2+3, Final Tracks, tt̄) | **UPDATED 2026-07 (Ben):** $a(\eta)$ now from the Run-2+3 ID paper Fig. 15(c) relative $q/p_T$ resolution (~1.9% central → ~4.6% at $|\eta|$=2.5). $p_T$-averaged fig → fixes $a$; slope $b$=3.6e-4 kept from ID form (1404.4562). Supersedes the muon-ID $a$=0.013 (PERF-2015-10) — hadrons resolve worse. In `apply_user_tracking.py`. |
| 4 | Electron mom. res. **ATLAS** | all | $a$=0.03/0.05/0.15, $b$≠0 | $a$=0.010/0.012/0.018, **$b$=0** | **Run-2:** arXiv:2309.05471 (JINST 19 (2024) P02009) §5.1/§7/Fig. 16(b) | Wrong form: $b\,p_T$ is a tracker artefact; electrons are ECAL-dominated (flat vs $p_T$) |
| 5 | Electron mom. res. **CMS** | all | $a$=0.03/0.05/0.15, $b$≠0 | $a$=0.020/0.025/0.050, **$b$=0** | **Run-2:** arXiv:2012.06888 (JINST 16 (2021) P05014) Fig. 11 | Wrong form (same); $b$ was byte-identical to the tracker block |
| 6 | Muon mom. res. **ATLAS** central floor $a$ | \|η\|≤0.5 | 0.010 | 0.017 | arXiv:1603.05598 §8.2 (1.7% J/ψ, 2.3% Z) | Optimistic ~2×. Note: combined-muon anchor vs ID-only form |
| 7 | Muon mom. res. **CMS** endcap floor $a$ | 1.5–2.5 | 0.025 | 0.030 | arXiv:1804.04528 §7.1 (endcap ~3%) | Mildly optimistic |

## Tier 2 — documented only (stock value kept; needs your call before applying)

| # | Quantity | Region | Card | Proposed | Source — locator | Note |
|---|----------|--------|------|----------|------------------|------|
| 8 | **CMS ECal** energy-shape $S$ / $C$ / $N$ | barrel+endcap | 0.11 / 0.008 / 0.40 | **keep (do not change)** | effective values; cross-check arXiv:2012.06888 Fig. 33 (1–3.4% low-brem, 2–5% all-brem) | **Resolved (re-exam):** the card S/N/C are *effective* (tuned to in-situ), NOT test-beam; the (1+0.64η²) prefactor is a Delphes construct; no Run-2 S/N/C exists. The card reproduces measured performance — **keep + caveat**. (The earlier 0.028 figure is the test-beam $S$, which would *underestimate* Run-2.) |
| 8b | **CMS b-tag** c-mistag amplitude | — | 0.25 | ~0.15 | **Run-2:** arXiv:1712.07158 (DeepCSV Medium, Table 2/App. A) | card c-mistag ~40–75% too high above ~60 GeV (b-eff and light-mistag are fine) |
| 9 | **CMS HCal** stochastic $S$ | \|η\|≤3.0 | 1.50 | 1.10 (with $C$=0.09) | PF arXiv:1706.04965 Eq.(2) (110%/√E⊕9%) + Run-2 corrob. 1910.00079 | detector-intrinsic; card 150%/5% ≠ published 110%/9% |
| 10 | **ATLAS ch-had tracking eff** plateau | central / forward | 0.95 / 0.85 | **0.85 / ~0.70** (Loose WP) | **arXiv:2605.07585 Fig. 16(a,b)** (Run 2+3, min-bias sim) | **UPDATED 2026-07 (Ben):** now sourced from the Run-2+3 ID paper (Loose WP): central $|\eta|$<1.5 ≈ 0.85, forward ~0.67–0.72; $p_T$ plateau by ~1 GeV. Supersedes both the stock 0.95 and the earlier 1602.01633 (0.86) / PUB-2015-051 (0.91) reads. Applied via `apply_user_tracking.py`. |
| 11 | **ATLAS muon ID eff** | \|η\|≤1.5 | 0.95 | 0.98 (Medium WP) | arXiv:1603.05598 / 2012.00578 | pessimistic; depends on intended WP |
| 12 | **ATLAS τ eff** (1-prong / 3-prong) | — | 0.70 / 0.60 | **keep** (0.75 / 0.60) | **Run-2:** ATL-PHYS-PUB-2019-033 (RNN Medium WP, Table 2) | **Corrected:** card is consistent/slightly conservative, NOT optimistic — the earlier "0.55/0.40" used the superseded 2015 BDT note. Card multi-prong mistag 0.01 is ~2× the RNN value (0.0042) → conservative. |
| 13 | **CMS τ→jet mistag** | — | 0.01 | 0.003 | arXiv:1809.02816 §5.2 (tight WP 0.21%→0.07%) | card ~3–10× too high at the matched efficiency |
| 14 | **ATLAS JES** `ScaleFormula` coeffs | — | 3.0, 0.2 | (no clean drop-in) | arXiv:1703.09665 / 2007.02645 | verifier: coefficients unsupported; needs a proper JER parameterization, not a single linear η slope |
| 15 | **CMS JES** `ScaleFormula` stochastic | — | ~2.5 | ~0.9 (with $C$≈0.04) | **No Run-2 paper;** best = CMS-DP-2021-033 (Run-2 legacy) | card-implied σ/p_T ~3× measured Run-2 JER; no constant term. DP-note only |

## Suggested order to check
Start with **#3 and #1/#2** (the ~3× track-resolution change is the single
biggest physics effect and the muon-ID-vs-hadron caveat is the one genuine
judgement call), then **#4/#5** (electron form — straightforward once you accept
ECAL-dominance), then **#8** (the CMS ECal prefactor convention, which needs a
human to untangle before any change).
