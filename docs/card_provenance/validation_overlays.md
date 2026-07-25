# Validation overlays — manifest & progress

For each figure-read parameterization we overlay our Delphes curve (+ band) on the
source figure (method in `overlay_method.md`). Status of the per-block overlays:

Legend: ✅ done (real-figure overlay) · 🔸 digitized re-plot (fallback) · ⬜ todo (arXiv, can do) · 🔒 blocked (need file from you, see NEEDS_FROM_USER.md)

## Momentum / energy resolution
| Block | Source figure | Status | File |
|-------|---------------|--------|------|
| CMS muon (barrel) | 1804.04528 Fig. 9 | ✅ | aux_overlay_onfigure_muon.pdf |
| ATLAS muon (barrel) | 2012.00578 Fig. 2 | ✅ | aux_overlay_onfigure_atlasmu.pdf |
| CMS electron | 2012.06888 Fig. 11 | ✅ | aux_overlay_onfigure_cmsel.pdf |
| ATLAS electron | 2309.05471 Fig. 16(b) | ✅ | aux_overlay_onfigure_atlasel.pdf |
| CMS charged-hadron | 1405.6569 (no isolated res-vs-eta fig) | n/a — detector-intrinsic, validated via CMS muon Fig. 9 (same tracker) |
| ATLAS charged-hadron | **arXiv:2605.07585 Fig. 15(c)** (Run 2+3) | ⬜ todo (arXiv, doable) | supersedes PERF-2015-10; a(η)≈1.9%→4.6% |

## Tracking / ID efficiency
| Block | Source figure | Status |
|-------|---------------|--------|
| ATLAS charged-hadron tracking | **arXiv:2605.07585 Fig. 16(a,b)** (Run 2+3, Loose WP) | ⬜ todo (arXiv; supersedes PUB-2015-051 overlay, plateau 0.91→0.85) |
| CMS charged-hadron tracking | 1405.6569 Fig. 11 | ✅ (aux_overlay_onfigure_cmstrkeff.pdf) |
| ATLAS muon eff | 2012.00578 | ▫ no overlay; consistency argument only (measured reco eff ~99% Loose / 95-99% Tight makes the card's flat 0.95 conservative) |
| CMS muon eff | 1804.04528 | ▫ no overlay; consistency argument only (Loose >99% / Tight 95-99% makes the card's flat 0.95 conservative) |
| ATLAS electron ID | 1902.04655 Fig. 8 | ✅ aux_overlay_onfigure_atlaseid.pdf |
| CMS electron ID | 2012.06888 Fig. 26 | ✅ aux_overlay_onfigure_cmseid.pdf |
| ATLAS photon ID | 1810.05087 | ▫ ID-vs-ET fig not cleanly isolated; card 0.95/0.85 consistent w/ tight photon ID |
| CMS photon ID | 2012.06888 Fig. 27 | ✅ aux_overlay_onfigure_cmsphot.pdf |

## Flavour tagging
| Block | Source figure | Status |
|-------|---------------|--------|
| ATLAS b-tag | 1907.05120 Fig. 8a | ✅ aux_overlay_onfigure_atlasbtag.pdf |
| CMS b-tag | 1712.07158 Fig. 17 | ⬜ todo (page render failed here) — DeepCSV WP; NOT covered by the ATLAS MV2 overlay |
| CMS tau | 1809.02816 Fig. 3 (ROC) | ✅ aux_overlay_onfigure_cmstau.pdf |

## Calorimeter
Calo blocks are formula (S/N/C) rather than a single curve; validated by the
effective-resolution cross-check (CMS: 2012.06888 Fig. 33; ATLAS: AtlFast3 Table 4)
documented in findings — overlay optional.

Work proceeds in batches; this file is updated as each overlay lands.
