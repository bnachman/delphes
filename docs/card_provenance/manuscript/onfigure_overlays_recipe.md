# On-figure overlay recipes (reproducibility)

Each "gold-standard" overlay (`aux_overlay_onfigure_*.pdf`) draws a Delphes curve on
a rendered source figure. Reproduce with `overlay_lib.py` (`overlay(image, out,
title, curves, xcal, ycal, xlog, ylog)`): `xcal`/`ycal` are `(px1,val1,px2,val2)`
pixel↔data anchors read off the axes. Fetch + render:

    curl -L https://arxiv.org/pdf/<ID> -o p.pdf
    pdftoppm -png -r150 -f <PAGE> -l <PAGE> p.pdf pg     # then PIL-crop to CROP

Calibrations used (pixel coords are in the rendered/cropped image at r=150):

| Overlay | arXiv | page | crop (l,t,r,b) | x-cal | y-cal | curve |
|---|---|---|---|---|---|---|
| muon (CMS) | 1804.04528 | 23 | 150,260,1130,1110 | log: px310=10, 248px/dec | lin: py700=0, py80=0.12 | sqrt(0.010²+(1e-4·pt)²) |
| muon (ATLAS) | 2012.00578 | 11 | 130,150,1120,780 | lin: px148=500, px468=3000 | lin: py322=0, py72=0.9 | sqrt(0.017²+(1e-4·pt)²) barrel |
| electron (CMS) | 2012.06888 | 27 | 130,280,1120,820 | B log px180=10/192px-dec; E px660=10 | B py520=0/py158=0.08; E py158=0.45 | flat a=0.02 (B), 0.05 (E) |
| electron (ATLAS) | 2309.05471 | 22 | (full) | X=652+83.75·η | py1190=0, py888=0.03 | step 0.010/0.012/0.018 (total eff. term) |
| tracking eff (ATLAS) | PUB-2015-051 | 5 | (full) | X=395+74·η | py1033=0.6, py803=1.2 | fine |η| step (0.91…0.73) |
| tracking eff (CMS) | 1405.6569 | 35 | (full) | px258=-2.5, px582=2.5 | py610=1.0, py938=0.5 | step 0.95/0.85 + finer |
| b-tag (ATLAS) | 1907.05120 | 24 | (full) | log px375=100, 248px/dec | py318=0.9, py520=0.5 | 0.8·tanh(0.003pt)·30/(1+0.086pt) |
| tau (CMS) | 1809.02816 | 15 | 140,250,1110,640 | px118=0.3, px430=0.7 (eff) | log py30=1, 84px/dec | point (0.60, 0.010) |
| electron ID (ATLAS) | 1902.04655 | 26 | (full) | X=672+96·η | py1175=0.55, py838=1.0 | step 0.95/0.85 |
| electron ID (CMS) | 2012.06888 | 44 | (full) | (flat, span panel) | py1058=0.5, py792=1.0 | flat 0.95/0.85 |
| photon ID (CMS) | 2012.06888 | 45 | (full) | (flat, span panel) | py580=0.5, py312=1.0 | flat 0.95/0.85 |

Calibrations are hand-read to ~1 axis minor-division; the source figure is shown
underneath, so the reader verifies the comparison directly. See `overlay_method.md`
for the two ATLAS auxiliary blocks that use digitized points instead (source host
egress-blocked).

## Figure reuse / licensing
The appendix reproduces published figures with attribution (arXiv ID + figure
number in every caption). arXiv/CC-BY collaboration papers permit reuse with
attribution; journal-version and ATLAS `PUB`/aux figures require checking the
specific license or requesting permission before submission. Flagged here so it is
resolved before the paper is circulated externally.
