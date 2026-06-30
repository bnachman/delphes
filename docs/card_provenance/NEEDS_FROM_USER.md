# Files needed from you (blocked by session egress policy)

The session can reach **arXiv** but the egress policy blocks **`atlas.web.cern.ch`**
(ATLAS public figaux) and **`www.hepdata.net`**. For sources not in an arXiv paper,
drop the figure image/PDF into `docs/card_provenance/figures/` and I'll overlay
locally.

## Status

| # | File | For which block | Status |
|---|------|-----------------|--------|
| 1 | ATL-PHYS-PUB-2015-051 (Fig. 1a) | ATLAS charged-hadron **tracking efficiency** | ✅ **received** → real overlay done (`aux_overlay_onfigure_atlastrkeff.pdf`) |
| 2 | "PERF-2015-10 figaux\_11a" (rel. $p_T$ resolution vs $\eta$) | ATLAS charged-hadron **momentum resolution** | ⏳ still needed (see note) — currently digitized re-plot |

## Note on PERF-2015-10 (#2)
The bare code `PERF-2015-10` does not resolve cleanly and `atlas.web.cern.ch` is
blocked here, so I can't fetch `figaux_11a.png`. The "relative $p_T$ resolution vs
$|\eta|$" content is, however, available in the **ATLAS muon performance papers on
arXiv** (1603.05598 Figs.~11--12; 2012.00578 Fig.~2 — the latter already overlaid),
which is what the charged-hadron resolution is anchored to anyway. So #2 is
**optional**: if you can paste `figaux_11a.png` I'll overlay on it directly;
otherwise the digitized re-plot + the arXiv muon-paper citation stands.
