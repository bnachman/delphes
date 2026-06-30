# Validation overlays — method & access notes

To convince the reader that a figure-read parameterization is faithful, we overlay
our extracted Delphes curve (+ per-bin uncertainty band) on the source figure and
put it in the auxiliary material, citing the figure. Two implementations:

1. **Overlay on the actual published figure (preferred / gold standard).**
   Download the arXiv PDF, render the figure page (`pdftoppm`), calibrate
   pixel<->data from the axes, and draw our curve on top. No intermediate
   digitization to trust — the reader sees the real figure. Worked example:
   `manuscript/aux_overlay_onfigure_muon.pdf` (Delphes muon barrel resolution on
   CMS Fig. 9, arXiv:1804.04528). The curve tracks the inner-tracker points: ~1%
   floor, ~10% at 1 TeV.

2. **Re-plot with digitized points (fallback).** Our curve + the values we read
   off the figure, as points with the band. Worked examples:
   `manuscript/aux_trkeff_overlay.pdf`, `manuscript/aux_momres_overlay.pdf`.

## Access constraints in this environment

- **arXiv is reachable** -> for any source figure published *in* the arXiv paper,
  method (1) works (download PDF, render, overlay).
- **`atlas.web.cern.ch` (ATLAS public figaux) and `www.hepdata.net` are BLOCKED**
  by the session egress policy (403 org denial; not routed around per policy).
  So: the two ATLAS tracking blocks (ATL-PHYS-PUB-2015-051, PERF-2015-10 figaux)
  and any HEPData table cannot be fetched here. For those, either (a) the figure
  image is added to the repo and we overlay locally, or (b) we use method (2) with
  the digitized values and cite the figure.

## Pipeline (method 1)
`curl arxiv.org/pdf/<id>` -> `pdftoppm -png -r150 -f <pg> -l <pg>` -> crop to the
axis box (PIL) -> read axis tick pixels -> matplotlib `imshow` + plot curve in the
calibrated mapping -> save PDF for the aux. Calibration is per-figure (axis tick
pixel positions); precise versions detect ticks programmatically.
