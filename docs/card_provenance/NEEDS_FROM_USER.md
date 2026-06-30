# Files needed from you (blocked by session egress policy)

The session can reach **arXiv** but the egress policy blocks **`atlas.web.cern.ch`**
(ATLAS public figaux) and **`www.hepdata.net`**. For the validation overlays on
sources that are NOT in an arXiv paper, please drop the figure image into
`docs/card_provenance/figures/` and I'll overlay our curve on it locally.

## Outstanding (blocked) — please supply if you want the real-figure overlay

| # | File to provide | For which block | Where it lives |
|---|-----------------|-----------------|----------------|
| 1 | `PUB-2015-051_fig1a.png` (track reco eff vs η, Loose) and `..._fig1b.png` (vs pT) | ATLAS charged-hadron **tracking efficiency** | ATL-PHYS-PUB-2015-051 (CDS 2110140) |
| 2 | `PERF-2015-10_figaux_11a.png` (rel. pT resolution vs \|η\|) | ATLAS charged-hadron **momentum resolution** | atlas.web.cern.ch/.../PERF-2015-10/figaux_11a.png |

Without these, those two blocks keep the **digitized re-plot** overlays already
made (`aux_trkeff_overlay.pdf`, `aux_momres_overlay.pdf`), which cite the figure.

## Not needed
HEPData is blocked too, but we're not relying on it — every other source figure
is published in its arXiv paper, which I can fetch and overlay directly.
