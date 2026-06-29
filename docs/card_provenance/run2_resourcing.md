# Run-2 (13 TeV) re-sourcing pass

The first extraction pass returned several blocks sourced to Run-1 (7–8 TeV)
papers. This pass standardizes on **Run-2 (13 TeV)** sources: for each Run-1-sourced
block an agent found the Run-2 equivalent, re-extracted the value + locator, and
— where no peer-reviewed Run-2 source exists — said so explicitly rather than
invent one. Outcomes below; values that feed the baseline cards are marked.

## Summary

| Block | Old (Run-1) source | Run-2 outcome | Card effect |
|-------|--------------------|---------------|-------------|
| ATLAS charged-had. mom. res. | 1404.4562 (7 TeV) | **No Run-2 (a,b) table.** Values corroborated by 1603.05598 (§8.2) + 2012.00578 (Fig. 2). | values unchanged; re-cited + caveat |
| CMS charged-had. mom. res. | 1405.6569 (7 TeV) | **No Run-2 source** (tracker physically unchanged; every Run-2 paper cites 1405.6569). Corroborated by 1712.07158. | values unchanged; re-cited + caveat |
| CMS charged-had. tracking eff. | 1405.6569 (7 TeV) | Same; muon-based Run-2 ~99.9% is not a valid hadron proxy (nuclear-interaction losses). | values unchanged; re-cited + caveat |
| ATLAS electron mom. res. | 1407.5063 (8 TeV) | **→ arXiv:2309.05471** (JINST 19 (2024) P02009, Run-2 calib), §5.1/§7/Fig. 16(b). | **a = 0.010/0.012/0.018, b=0** |
| CMS electron mom. res. | 1502.02701 (8 TeV) | **→ arXiv:2012.06888** (JINST 16 (2021) P05014), Fig. 11/abstract. | **a = 0.020/0.025/0.050, b=0** |
| CMS electron reco/tracking eff. | 1502.02701 (8 TeV) | → 2012.06888 Fig. 4/30: reco >95% for \|η\|<2.5. Endcap tracking 0.83→~0.95. | documented (eff. block, not yet applied) |
| CMS electron ID eff. | 1502.02701 (8 TeV) | → 2012.06888 §7.3.1/Fig. 26: 0.95 EB = cut-based Veto WP; endcap 0.85→~0.90 (WPs are η-flat). | documented |
| CMS ECal S/N/C | 1306.2016 / 1502.02701 | **No peer-reviewed Run-2 S/N/C decomposition.** 2012.06888 gives only the effective 2–5% resolution. Keep Run-1/test-beam + caveat; ECAL/HGCAL TDRs are best Run-2 detector refs. | values unchanged; caveat |
| CMS b-tagging | 1211.4462 (7 TeV) | **→ arXiv:1712.07158** (JINST 13 (2018) P05011), DeepCSV Medium WP, Table 2/App. A. | c-mistag 0.25→~0.15 (documented) |
| CMS JES | 1607.03663 (8 TeV) | **No peer-reviewed Run-2 JES/JER paper.** Best = CMS-DP-2021-033 (Run-2 legacy). Card stochastic ~3× too large. | documented (DP-note caveat) |
| ATLAS HCal | hep-ex/0004009 (test-beam) | Detector-intrinsic. Re-cite AtlFast3 arXiv:2109.02551 Table 4 (Tile/HEC consistent; FCal not a drop-in). | values unchanged; re-cited |
| CMS HCal | 1706.04965 (8 TeV PF) | Detector-intrinsic; no Run-2 S⊕C. Re-cite PF 1706.04965 Eq. (2) + Run-2 corrob. 1910.00079. Note card 150%/5% vs published 110%/9%. | values unchanged; re-cited |

Already Run-2 (no change): ATLAS muon res./eff. (1603.05598, 2012.00578), CMS
muon res./eff. (1804.04528), ATLAS tracking eff. (1602.01633), ATLAS e/photon ID
(1902.04655, 1810.05087), ATLAS b-tag (1907.05120), ATLAS JES (1703.09665,
2007.02645), CMS τ (1809.02816), CMS photon (2012.06888), ATLAS ECal (2109.02551).

## Two judgement calls flagged for review

1. **ATLAS charged-hadron resolution slope `b`.** The Run-2 *combined-muon* papers
   give a small slope (~1e-4/GeV) because the muon spectrometer improves the high-p_T
   resolution. Charged hadrons are reconstructed by the **inner detector only**, so the
   ID-only slope (~3.9–9.0e-4/GeV, from 1404.4562 Figs. 17–18) is the correct proxy and
   is what the baseline card uses. Confirm this is the intended interpretation.

2. **No Run-2 source for several detector-intrinsic blocks** (CMS tracker resolution &
   efficiency, CMS/ATLAS HCal S/N/C, CMS ECal S/N/C, CMS JES). These quantities are
   detector-intrinsic (test-beam / TDR) and essentially unchanged Run-1→Run-2; the cards
   keep the existing values with a Run-2 corroborating citation and an explicit caveat,
   rather than substitute a non-existent Run-2 number.

## New Run-2 references added to sources.bib

2309.05471 (ATLAS e/γ energy calib, JINST 19 (2024) P02009);
2012.06888 (CMS e/γ reco/ID, JINST 16 (2021) P05014);
1712.07158 (CMS heavy-flavour tagging, JINST 13 (2018) P05011);
1910.00079 (CMS HCAL calibration 13 TeV, JINST 15 (2020) P05002);
CMS-DP-2021-033 (CMS Run-2 legacy JES/JER, CDS 2792322).
