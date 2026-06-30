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
| ATLAS charged-hadron | PERF-2015-10 figaux_11a | 🔒 / 🔸 | aux_momres_overlay.pdf (digitized) |

## Tracking / ID efficiency
| Block | Source figure | Status |
|-------|---------------|--------|
| ATLAS charged-hadron tracking | PUB-2015-051 Fig. 1a (user-supplied) | ✅ aux_overlay_onfigure_atlastrkeff.pdf |
| CMS charged-hadron tracking | 1405.6569 Fig. 11 | ✅ (aux_overlay_onfigure_cmstrkeff.pdf) |
| ATLAS muon eff | 2012.00578 (eff figs) | ⬜ |
| CMS muon eff | 1804.04528 Fig. 7 | ⬜ |
| ATLAS electron ID | 1902.04655 Fig. 8 | ✅ aux_overlay_onfigure_atlaseid.pdf |
| CMS electron ID | 2012.06888 Fig. 26 | ✅ aux_overlay_onfigure_cmseid.pdf |
| ATLAS photon ID | 1810.05087 | ⬜ |
| CMS photon ID | 2012.06888 | ⬜ |

## Flavour tagging
| Block | Source figure | Status |
|-------|---------------|--------|
| ATLAS b-tag | 1907.05120 Fig. 8a | ✅ aux_overlay_onfigure_atlasbtag.pdf |
| CMS b-tag | 1712.07158 Fig. 17 | ⬜ |
| CMS tau | 1809.02816 Fig. 3 (ROC) | ✅ aux_overlay_onfigure_cmstau.pdf |

## Calorimeter
Calo blocks are formula (S/N/C) rather than a single curve; validated by the
effective-resolution cross-check (CMS: 2012.06888 Fig. 33; ATLAS: AtlFast3 Table 4)
documented in findings — overlay optional.

Work proceeds in batches; this file is updated as each overlay lands.
