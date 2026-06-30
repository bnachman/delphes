# Re-examination — 3 re-run blocks (CMS)

These three CMS blocks failed the high-fidelity workflow on API overload and were
re-run separately. Summaries below; same standard (dedicated Run-2 figure, finest
binning, per-bin uncertainty, text-anchored vs figure-estimated flagged).

## CMS.ChargedHadronTrackingEff
- **Source:** arXiv:1405.6569 (JINST 9 (2014) P10009), §5.1, Fig. 10 (top) / Fig. 8 (middle). Detector-intrinsic, unchanged Run-1→Run-2.
- **Text-anchored:** 0.94 for |η|<0.9; 0.85 for 0.9<|η|<2.5 (pt>0.9 GeV). Inefficiency dominated by nuclear interactions in tracker material. Plateau flat 1<pt<80 GeV; fast turn-on below ~0.7 GeV.
- **Figure-estimated (softer):** finer split 0.90 (0.9–1.4) / 0.85 (1.4–2.0) / 0.82 (2.0–2.5); per-bin unc ~2–5%; low-pt magnitudes.
- **Proposed:** keep the card's two-region plateau (0.94/0.85, near the current 0.95/0.85), optionally adopt the paper's η-boundaries (0.9/1.4/2.5 rather than 1.5). Low-pt 0.70/0.60 retained as figure-estimates.

## CMS.ECalRes
- **Sources:** S/N/C test-beam = JINST 2 (2007) P04004 (S=2.8%, N≈0.12 GeV, C=0.3% — directly measured). η-shape = arXiv:1306.2016 (7/8 TeV). Run-2 cross-check = arXiv:2012.06888 Fig. 11 (vs pt) and Fig. 33 (σ(m_ee)/m_ee vs η; per-electron ~0.7–0.9% barrel-centre to ~1.5–2.4% endcap; text "1–3.4%" low-brem, abstract "2–5%" all-brem).
- **Key findings:** (a) the card's S=11%/N=0.40/C=0.8% are **effective** values tuned to in-situ performance, NOT a published S/N/C and NOT the test-beam numbers; (b) the `(1+0.64η²)` and `(2.16+5.6(|η|−2)²)` prefactors are **Delphes interpolation envelopes**, not in any paper; (c) **no Run-2 S/N/C decomposition exists.**
- **Proposed:** **KEEP the card numbers** + add a caveat (effective values; prefactor is a Delphes construct; test-beam S/N/C is P04004; Run-2 cross-check is 2012.06888 Fig. 33). **Do NOT** substitute the test-beam S=2.8% — it would *underestimate* the in-situ Run-2 effective resolution. (This corrects the earlier Tier-2 review note that suggested S→0.028.)

## CMS.TauTagging
- **Source:** arXiv:1809.02816 (JINST 13 (2018) P10005), §5.2.2 / Figs. 3–4 / Table 3. DeepTau supplement arXiv:2201.08458.
- **Findings:** card τ-eff 0.6 ≈ **Medium** MVA WP (WPs span 40–90% in 10% steps); Tight WP = 49% eff with jet→τ mistag 0.21% (low/med pt) → 0.07% (high pt). Measured acceptance **|η|<2.3, pt>20 GeV**; SF 0.92–0.99 ±5% per WP.
- **Proposed:** make pt/η-aware — `TauEtaMax 2.3`, `TauPTMin 20`; jet→τ mistag 0.21%→0.07% (pt-stepped) rather than flat 0.01; τ-eff ~0.58 (Medium, incl. SF) or ~0.47 (Tight). Flat 0.6 below ~20 GeV and to |η|=2.5 are unsupported.
