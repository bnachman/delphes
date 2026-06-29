# Highly-discrepant numbers — review checklist

These are the card values that disagree most with their verified source (factor
≳1.5, or a functional-form problem). Each row gives the stock card value, the
proposed source-faithful value, the exact source locator to check, and whether
it is **applied** in the generated `*_baseline.tcl` cards or only **documented**
(left at the stock value pending your review).

Verify against the locator; if you disagree, the stock value is preserved in an
inline `# stock value was:` comment in the baseline card for easy revert.
Full per-coefficient detail: `findings_summary.md` / `run1_provenance.json`.

## Tier 1 — applied in the baseline cards (resolution; biggest, cleanest)

| # | Quantity | Region | Card | Proposed | Source — locator | Why |
|---|----------|--------|------|----------|------------------|-----|
| 1 | Charged-hadron mom. res. **CMS** ($a$) | 0.5 / 1.5 / 2.5 | 0.06 / 0.10 / 0.25 | 0.009 / 0.015 / 0.023 | arXiv:1405.6569 (JINST 9 (2014) P10009), tracker resolution | ~3× too pessimistic |
| 2 | Charged-hadron mom. res. **CMS** ($b$, GeV⁻¹) | 0.5 / 1.5 / 2.5 | 1.3e-3 / 1.7e-3 / 3.1e-3 | 2.3e-4 / 4.2e-4 / 9.5e-4 | same | ~3–6× too large |
| 3 | Charged-hadron mom. res. **ATLAS** ($a$,$b$) | all | 0.06–0.25 / 1.3–3.1e-3 | 0.015–0.040 / 3.9–9.0e-4 | arXiv:1404.4562 Eq.(2), Figs. 17–18 | ~3× pessimistic. **Anchors are muon-ID tracks** — confirm the card term is not deliberately hadron-specific |
| 4 | Electron mom. res. **ATLAS** | all | $a$=0.03/0.05/0.15, $b$≠0 | $a$=0.007/0.012/0.015, **$b$=0** | arXiv:1902.04655 / 1407.5063 | Wrong form: $b\,p_T$ is a tracker artefact; electrons are ECAL-dominated (flat vs $p_T$) |
| 5 | Electron mom. res. **CMS** | all | $a$=0.03/0.05/0.15, $b$≠0 | $a$=0.017/0.025/0.045, **$b$=0** | arXiv:1502.02701 (JINST 10 (2015) P06005) §4.8 | Wrong form (same); $b$ is byte-identical to the tracker block |
| 6 | Muon mom. res. **ATLAS** central floor $a$ | \|η\|≤0.5 | 0.010 | 0.017 | arXiv:1603.05598 §8.2 (1.7% J/ψ, 2.3% Z) | Optimistic ~2×. Note: combined-muon anchor vs ID-only form |
| 7 | Muon mom. res. **CMS** endcap floor $a$ | 1.5–2.5 | 0.025 | 0.030 | arXiv:1804.04528 §7.1 (endcap ~3%) | Mildly optimistic |

## Tier 2 — documented only (stock value kept; needs your call before applying)

| # | Quantity | Region | Card | Proposed | Source — locator | Note |
|---|----------|--------|------|----------|------------------|------|
| 8 | **CMS ECal** energy-shape $S$ / $C$ / $N$ | barrel+endcap | 0.11 / 0.008 / 0.40 | 0.028 / 0.003 / 0.12 | arXiv:1502.02701 / 1306.2016 | **Subtle:** the card multiplies these by an η-prefactor (1+0.64η²); the apparent ~3–4× gap may partly be a convention difference. Reconcile the prefactor before changing. |
| 9 | **CMS HCal** stochastic $S$ | \|η\|≤3.0 | 1.50 | 1.10 (with $C$=0.09) | CMS HCAL / PF (arXiv:1706.04965) | combined-calo measured term |
| 10 | **ATLAS ch-had tracking eff** plateau | central / forward | 0.95 / 0.85 | 0.86 / 0.73 | arXiv:1602.01633 Fig. 2(c,d) | optimistic by 5–12% absolute |
| 11 | **ATLAS muon ID eff** | \|η\|≤1.5 | 0.95 | 0.98 (Medium WP) | arXiv:1603.05598 / 2012.00578 | pessimistic; depends on intended WP |
| 12 | **ATLAS τ eff** (1-prong / 3-prong) | — | 0.70 / 0.60 | 0.55 / 0.40 | ATL-PHYS-PUB-2015-045 (Medium WP) | card optimistic vs the WP it names |
| 13 | **CMS τ→jet mistag** | — | 0.01 | 0.003 | arXiv:1809.02816 §5.2 (tight WP 0.21%→0.07%) | card ~3–10× too high at the matched efficiency |
| 14 | **ATLAS JES** `ScaleFormula` coeffs | — | 3.0, 0.2 | (no clean drop-in) | arXiv:1703.09665 / 2007.02645 | verifier: coefficients unsupported; needs a proper JER parameterization, not a single linear η slope |

## Suggested order to check
Start with **#3 and #1/#2** (the ~3× track-resolution change is the single
biggest physics effect and the muon-ID-vs-hadron caveat is the one genuine
judgement call), then **#4/#5** (electron form — straightforward once you accept
ECAL-dominance), then **#8** (the CMS ECal prefactor convention, which needs a
human to untangle before any change).
