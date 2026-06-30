## ATLAS.ChargedHadronTrackingEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 11
- **Source:** ATL-PHYS-PUB-2015-051 (CDS 2110140) — Figure 1(a) Loose track selection (efficiency vs eta, pt>5 GeV plateau); anchored by Table 1 (|eta|<=0.1: 91% +-0.4%; 2.3<=|eta|<=2.5: 73% +
- **Verifier corrections:** 1) LOCATOR/PLATEAU MISATTRIBUTION (significant): The Table 1 anchor values (91% at |eta|<=0.1; 73% at 2.3-2.5) are NOT pt>5 GeV plateau values. Table 1 caption explicitly states 'results shown are obtained by integrating over pT in the range [0.4,20] GeV.' The block labels these bins as 'plateau pt>5 GeV' and builds the whole etaplateau step-function on that premise — this is a mis-read. The true pt>5 GeV plateau is only quoted as overall ~90% (Loose), not per-eta. 2) FABRICATED PRECISION on int

## ATLAS.ElectronTrackingEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 14
- **Source:** arXiv:1902.04655, Eur. Phys. J. C 79 (2019) 639 (ATLAS EGAM-2018-01) — Fig. 4 (epsilon_reco vs eta in ET bins 15-20/25-30/40-45/80-150 GeV) and Fig. 2 (total reco eff vs true ET, top; epsilon_reco vs ET, bottom)
- **Verifier corrections:** (1) REPRESENTATION MISLABEL at low ET: the pt 3-15 GeV bins are read from Figure 2 TOP, which is the TOTAL reconstruction efficiency (EMclus x e_reco), NOT e_reco "relative to reconstructed clusters." This is acceptable for a Delphes total-reco card, but the bin notes citing "e_reco" / "epsilon_reco data points" for the turn-on region are technically wrong -- those are total-efficiency reads. The high-ET bins (>15 GeV) correctly use e_reco from Fig.4. (2) HIGH-ET PER-ETA FINE STRUCTURE UNVERIFIA

## ATLAS.MuonTrackingEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 8
- **Source:** arXiv:2012.00578 (Eur. Phys. J. C 81 (2021) 578), 139 fb^-1 — Fig. 17 (Medium efficiency vs eta, pt>10 GeV) and Table 1 (Medium prompt-muon efficiency vs pt, |eta|<2.5); eta=0 dip and 1.0<|eta|<1.3 dip 
- **Verifier corrections:** Bin VALUES and uncertainties are accepted (70%/97% exact from Table 1; central plateau values consistent with text 'exceeds 98% for 0.1<|eta|<2.5' and the documented 1.0-1.3 MDT dip; forward 0.94 consistent with Fig 17). Corrections to SOURCE/LOCATOR metadata: (1) LOCATOR MISATTRIBUTION: the main 'Medium efficiency vs eta, pt>10 GeV' plot for |eta|<2.5 is FIGURE 12 (right panel), NOT Figure 17. Figure 17 is specifically the forward 2.5<|eta|<2.7 double-ratio extension (with tag-and-probe |eta|<2

## ATLAS.ChargedHadronMomRes

- **Verdict:** REJECT  | Run-2: true | dedicated figure: true | bins: 5
- **Source:** ATLAS-CONF/PERF-2015-10 = arXiv:1704.07983 (figaux_11a, expected relative pT resolution vs eta, 13 TeV); base (a,b) from ATLAS ID design/Run-2 resolution sigma(pT)/pT = 0.05% x pT(GeV) (+) 1% — PERF-2015-10 figaux_11a (expected sigma(pT)/pT vs |eta|); base a=0.013, b=3.6e-4 from ID pT-resolution formula sigma(pT)/pT ~ 0.05% pT (+) 1
- **Verifier corrections:** DEDICATED FIGURE FALSE: figaux_11a / Figure 11 of PERF-2015-10 is a reconstructable-EFFICIENCY plot for rho/3-prong-tau decays, not an "expected sigma(pT)/pT vs |eta|" plot. No such resolution-vs-eta figure exists anywhere in arXiv:1704.07983. LOCATOR FABRICATED: the paper contains no momentum-resolution parametrization, no "0.05% x pT (+) 1%" formula, and no etashape normalization numbers ("4.16 vs 1.73 in figaux_11a units" are invented). SOURCE MISMATCH: the cited Run-2 dense-environment track

## ATLAS.ElectronMomRes

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 6
- **Source:** arXiv:2309.05471 (JINST 19 (2024) P02009), ATLAS EGAM-2021-02 — Sec 7 + Fig 16(b) (additional constant term c_i vs eta, 24 eta intervals); eta binning from Sec 5.1/Sec 10.1: 0,0.6,1.0,1.37,1.55,1.82,2.47;
- **Verifier corrections:** Bin structure, source, locator, eta binning, and per-bin uncertainty band are all correctly read. But the central VALUES and formula_terms are partly unsourced and must be flagged:
1) The paper's Fig 16(b) c_i is the ADDITIONAL (residual data-MC) constant term, which the text says is "less than 1% in most of the barrel." The extraction instead reports an "effective" c built by adding an UNSTATED "~0.7% MC-intrinsic constant term in quadrature" -> c~1.0%. That ~0.7% intrinsic value appears NOWHER

## ATLAS.MuonMomRes

- **Verdict:** ACCEPT  | Run-2: true | dedicated figure: true | bins: 4
- **Source:** arXiv:2212.07338 (Eur. Phys. J. C 83 (2023) 686) — Eq.(9) sigma(pT)/pT = r0/pT (+) r1 (+) r2*pT; Fig.4 (resolution vs p, barrel/endcap, 1 TeV anchors); Fig.7 and text Sec.6 (pT resolution vs 
- _no corrections_

## ATLAS.ECalRes

- **Verdict:** ACCEPT  | Run-2: false | dedicated figure: true | bins: 0
- **Source:** arXiv:physics/0608012 (NIM A568 (2006) 601) — Eq. (8): sigma/E = a/sqrt(E) (+) b, a=10.1+/-0.1 %.sqrt(GeV), b=0.17+/-0.04 %
- **Verifier corrections:** none. Minor non-blocking observations: (1) The card's energy descriptor "90-180 GeV electrons" is narrower than the paper's actual fitted range (10-245 GeV available; 15-180 GeV linearity); this does not affect the Eq.(8) coefficients. (2) The forward FCal sampling value "28.5%/sqrt(GeV)" is presented as approximate and could not be confirmed against an exact published figure in open text, but it is appropriately hedged (unc_rel=0.1) and the companion constant term ~3.5% is corroborated as ~4% b

## ATLAS.HCalRes

- **Verdict:** ACCEPT  | Run-2: true | dedicated figure: true | bins: 0
- **Source:** arXiv:2109.02551 (Comput. Softw. Big Sci. 6 (2022) 7) — Table 4 (Stochastic term a and Constant term c for Tile, LAr Hadronic Endcap (HEC), FCal); Eq.(3) sigma_E/E = a/sqrt(E/GeV) (+) c; hadron et
- **Verifier corrections:** none. All Table 4 values (Tile 56.4%/5.5%, HEC 76.2%/0, FCal 28.5%/3.5%), the Eq.(3) form, and the eta-slice uncertainty bands match the source verbatim. Only nit: locator cites "text p.18" for the eta-slice ranges, but in the PDF the eta-slice text sits on the page after Table 4 (the running page marker shows "17" just above it), so the page reference may be off by one between PDF/journal pagination — immaterial, the content is correct and unambiguous.

## ATLAS.PhotonEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 15
- **Source:** arXiv:1810.05087, Eur. Phys. J. C 79 (2019) 205 — Figs. 9-12 (Tight ID efficiency vs ET, unconverted/converted, 4 eta bins); Sec. 10 binning; conclusion p.34 (eff 45-60% at ET=10 GeV -> 95-9
- **Verifier corrections:** Locator errors (minor, do not affect bins/values):
1. "Sec. 10 binning" is WRONG — there is no Section 10 in this paper. The conclusion is Section 8 (not 10), and the ET bin boundaries (8,15,20,25,30,40,50,60,80,100,250,1000 GeV) appear in the methods text (~PDF p.10), not a Section 10. Correct the section reference.
2. "conclusion p.34" is acceptable/correct (the conclusion's quoted sentence is on printed page 34->35; arXiv PDF p.34 carries the page number).
3. Value nuance (not an error, flagg

## ATLAS.ElectronIDEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 11
- **Source:** arXiv:1902.04655 (Eur. Phys. J. C 79 (2019) 639) — Figure 8 (bottom panel: eps_id vs eta, Z->ee, ET>4.5 GeV; top panel: eps_id vs ET) for Loose/Medium/Tight LH WPs; eta bin edges from Sec.7.3
- **Verifier corrections:** (1) FABRICATED ETA EDGE: The locator lists eta edges "0, 0.1, 0.6, 0.8, ...". The source Table 2 has NO 0.1 boundary; the nine official bins are {0, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47}. The extra 0.1 edge and the resulting 0-0.1 (0.945) vs 0.1-0.6 (0.96) split are invented. The eta~0 efficiency dip IS visible in Fig 8, but it is NOT a tabulated bin boundary and falls inside the first official bin; representing it as a discrete 0-0.1 bin is the extractor's modeling, not source-tab

## ATLAS.MuonIDEff

- **Verdict:** ACCEPT  | Run-2: true | dedicated figure: true | bins: 8
- **Source:** arXiv:1603.05598 (EPJC 76 (2016) 292), Table-1 from arXiv:2012.00578 (EPJC 81 (2021) 578) — arXiv:1603.05598 Fig.3 (Medium eff vs eta, Z->mumu, pT>10 GeV) + Sec.6.2 high-eta (2.5<|eta|<2.7, SF~0.9); crack |eta|<0.1 Medium drops (Loo
- **Verifier corrections:** none. All numerically load-bearing claims are directly supported by the cited locators: Table 1 Medium 70%/97% (exact), Section 6.2 high-eta SF~0.9 +/-3-5% (exact), Fig 3 crack drop to 0.6-0.65 with Loose recovery (figure+text), Fig 6 ~99% plateau pT>6 GeV (exact text). The finer per-eta sub-bin central values (e.g. 0.985 for 1.05-1.3 and 2.0-2.5 vs 0.990 for barrel/endcap) are eyeballed interpolations within the paper's stated ">98%" / "~99%" band rather than tabulated numbers, but they are phy

## ATLAS.JES

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 6
- **Source:** arXiv:2007.02645, Eur. Phys. J. C 81 (2021) 689 — Eq.(4) JER form sigma/pt=sqrt((N/pt)^2+(S/sqrt(pt))^2+C^2); Fig.29-30 (PFlow+JES anti-kt R=0.4, 0.2<=|eta|<0.7); Fig.28 noise term N vs eta;
- **Verifier corrections:** The six per-eta (N,S,C) triplets [(3.5,0.71,0.042),(3.8,0.74,0.045),(4.5,0.80,0.050),(5.5,0.85,0.055),(9.0,0.95,0.060),(6.5,1.10,0.070)] are NOT in the paper - the paper gives only Eq.(4)'s functional FORM, never tabulated fit parameters per eta bin. These triplets and the derived per-bin central sigma/pt values (0.179, 0.191, 0.215, 0.246, 0.352, 0.304 at a "reference pt=30 GeV" that the paper never specifies) are the extractor's own fabricated fits/extrapolations, not source values. Only the 0

## ATLAS.BTagging

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 0
- **Source:** arXiv:1907.05120, Eur. Phys. J. C 79 (2019) 970 (BTAG-2018-01) — Table 4 (MV2 single-cut OP rejections: 70% WP cut>0.83, c-rej 8.9, tau-rej 36, light-rej 300); Fig 8(a) b-eff vs pT at 70% MV2 OP; Table 5 (
- **Verifier corrections:** Two minor imprecisions, neither in the extracted source (Table-4/Table-5/Fig-8a) values themselves:

(1) eff_b_peak note overstates the high-pT falloff: it says b-eff 'falls to ~0.55-0.60 at 20-30 GeV AND at very high pT.' Fig 8(a) shows ~0.54 only at the lowest (20-30 GeV) bin; at the highest bin (250-600 GeV) the measured efficiency falls only to ~0.70, not 0.55-0.60. The low-pT value is right; the very-high-pT value is wrong (should be ~0.70).

(2) Internal inconsistency between the stated pe

## ATLAS.TauTagging

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 0
- **Source:** ATL-PHYS-PUB-2019-033 (CDS 2688062) — Table 2 (WP eff + rejection, pT>20 GeV); Figure 7 (Medium WP rejection vs pT/|eta|/mu); Figure 6 (eff vs pT/|eta|/mu, flattened)
- **Verifier corrections:** All Table 2 values (efficiencies and pT-integrated rejections) are EXACT and clean. Two minor figure-reading caveats on the delphes pT-binned formula (do not change the headline numbers):
1) mistag_1prong middle bin (50-100 GeV) uses the pT-INTEGRATED value 0.0286 (=1/35), not the bin-specific value. Figure 7a RNN in 50-100 GeV reads rejection ~38-54 (avg ~45 -> ~0.022). Using 0.0286 here slightly OVERESTIMATES mistag (conservative), so it is an approximation rather than the bin reading.
2) mist

## CMS.ElectronTrackingEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 9
- **Source:** arXiv:2012.06888, CMS-EGM-17-001, JINST 16 (2021) P05014 — Fig. 4 (reco eff vs eta, pT bins 20-45/45-75/75-100/100-500 GeV) and Fig. 30 (reco eff vs eta, 45<pT<75 GeV); summary text Sec. 4.7/9: 'reco
- **Verifier corrections:** Two minor note-level inaccuracies (do not affect bin values or the Run-2 anchoring): (1) The note on the endcap 10-20 GeV bin claims "~0.92-0.94 from Fig.4 lowest pT bin" — INCORRECT attribution: Fig. 4's lowest pT bin is 20-45 GeV, not 10-20 GeV. Fig. 4 contains NO bin below 20 GeV. The 10 GeV anchor comes solely from the Sec. 4.7/Sec. 9 summary text ("better than 95% over E_T 10-500 GeV", "down to E_T as low as 10 GeV"), not from a Fig. 4 marker. The 10-20 GeV central values (0.95 barrel, 0.93

## CMS.MuonTrackingEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 5
- **Source:** arXiv:1804.04528 (JINST 13 (2018) P06015), CMS-MUO-16-001 — Fig. 7 (reco+ID eff. vs eta, loose & tight) and Table 3 (eff. for pT>20 GeV, by |eta| region); plateau statement p.17 line 'about 99% of muo
- **Verifier corrections:** Locator imprecision (not a value error): the extraction cites 'Table 3' but the efficiency table is labeled tab:TPplateau (it is the muon-ID/isolation efficiency table, Table 5 in the published JINST numbering, not Table 3). The Figure 7 and plateau-statement locators are correct. Content/value notes: (a) Bins [0,0.3] and [0.3,0.9] both use 0.9975, and bins [0.9,1.2] and [1.2,2.4] both use 0.9977 — the table gives only ONE value per coarse region (0.0-0.9 and 0.9-2.4), so the four bins are faith

## CMS.ChargedHadronMomRes

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 4
- **Source:** arXiv:1405.6569 (JINST 9 (2014) P10009), Run-2 corrob. arXiv:1804.04528 (JINST 13 (2018) P06015) — Sec. 5.2.1, Fig. 14 (bottom panel: (Resolution in p_T)/p_T (%) vs eta for mu+- at p_T=1,10,100 GeV) and Fig. 15; abstract p.1; Run-2: 1804.0
- **Verifier corrections:** MISATTRIBUTED RUN-2 NUMBERS (appear in notes of bins 0-0.9 and 1.6-2.1, and in formula_terms b_slope_barrel and b_slope_endcap notes): The block repeatedly cites 1804.04528 as saying "1.3-2.0% barrel for 20<pt<100 GeV" and "better than 6% in the endcaps". These exact phrases/numbers DO NOT appear anywhere in arXiv:1804.04528. A COLD grep of the full text finds no "1.3", no "better than 6", no "20<pT<100" resolution statement. What the paper ACTUALLY states (Sec 7.1, verbatim): "The resolution fo

## CMS.ElectronMomRes

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 4
- **Source:** arXiv:2012.06888 (JINST 16 (2021) P05014), CDS record 2747266 — Fig. 11 (relative electron energy resolution vs pT, E-p combination, barrel & endcap); eta categories on p.27 text (|eta|<1.0, 1.0-1.44, 1.5
- **Verifier corrections:** (A) FABRICATED per-bin central values: 0.0102, 0.0144, 0.0215, 0.0295 sigma/E are NOT printed anywhere in the paper — they are eyeballed off the Fig.11 curve. The paper tabulates no numeric resolution value for any eta×pT bin; the only quantitative statement is the qualitative '2 to 5%' range. (B) FABRICATED per-bin uncertainties: unc_rel 0.10/0.12/0.15/0.18 have no basis — the paper's only stated resolution-related uncertainties are the fit-procedure error bars on Fig.11 markers (not quantified

## CMS.MuonMomRes

- **Verdict:** ACCEPT  | Run-2: true | dedicated figure: true | bins: 4
- **Source:** arXiv:1804.04528 (JINST 13 (2018) P06015) — Sec. 7.1 (floors: 1% barrel / 3% endcap, ~5% uncertainty); Sec. 7.2 + Fig. 9 (high-pt RMS of R(q/pT) vs pT, Tune-P, |eta|<0.9)
- **Verifier corrections:** Substantive claims all confirmed; verdict ACCEPT. One minor internal-consistency nit (does NOT change any bin value or uncertainty, so not a correction to the extracted fields): the barrel Tune-P slope b_barrel_TuneP=6.3e-5 does not reproduce the stated 1 TeV anchor of 0.058 -- sqrt(0.010^2+(6.3e-5*1000)^2)=0.0638 (~0.064), whereas exact anchoring to 0.058 requires b~5.7e-5. The 6.3e-5 value over-predicts the top bin by ~10%, but it is presented as a least-squares fit to all Fig 9 Tune-P points 

## CMS.HCalRes

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: false | bins: 0
- **Source:** arXiv:1706.04965 (CMS-PRF-14-001), JINST 12 (2017) P10003 — Eq.(2), Section 2.4 (HCAL); combined ECAL+HCAL pion test-beam resolution. Test-beam source = ref [24] EPJC 60 (2009) 359. Forward HF: EPJC 5
- **Verifier corrections:** Values, per-bin formula terms, sources, and the primary locator (Eq.(2)) are all correct and verified. One locator clarification (not a value error): the PF paper arXiv:1706.04965 Section 2.4 does NOT quote any forward/HF stochastic+constant resolution formula — its HF subsection only describes the detector. The forward 280%/11% comes solely from EPJC 53 (2008) 139. The top-level "locator" string blends the PF-paper Eq.(2) (which covers only the barrel/combined ECAL+HCAL) with the separate HF re

## CMS.PhotonEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 21
- **Source:** arXiv:2012.06888 (JINST 16 (2021) P05014), CMS-EGM-17-001 — Figure 27 (left panel): cut-based Loose photon ID efficiency vs E_T in 4 |eta| bins
- **Verifier corrections:** One central value is off: eta 0.80-1.44 (grey squares), ET 200-500 GeV bin. Extraction has central=0.905, but in the figure the grey square in the last ET bin sits at the same low level as the black circle, measured at eff ~ 0.878-0.885 (re-confirmed by row scan: grey pixels at y~771-785 -> eff ~0.873-0.885). Correct value is approximately 0.88, not 0.905 (off by ~0.025). The corresponding delphes_fragment line "(abs(eta) > 0.80 && abs(eta) <= 1.44) * (pt > 200.0) * (0.905)" should be ~0.88. All

## CMS.ElectronIDEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 9
- **Source:** arXiv:2012.06888; JINST 16 (2021) P05014; CMS-EGM-17-001 — Sec. 7.3.1 + Sec. 7.4, Fig. 26 (left: cut-based Veto WP electron ID efficiency vs ET in 4 eta bins, with data/MC ratio panel); WP target eff
- **Verifier corrections:** The structural metadata (source, locator, WP, four eta bins, crack exclusion, ET threshold, uncertainty magnitude, Run-2 status, dedicated-figure flag) is all correct and directly confirmed. CAVEAT on numeric central values: the per-bin central efficiencies (turn-on 10-20 GeV bins ~0.82-0.90; plateau >20 GeV bins ~0.91-0.965) are NOT stated numerically anywhere in the text — they are eyeball reads of the Fig.26 curves. The CMS public figure image (cms-results EGM-17-001) returned HTTP 403 and co

## CMS.MuonIDEff

- **Verdict:** ACCEPT_WITH_CORRECTIONS  | Run-2: true | dedicated figure: true | bins: 9
- **Source:** arXiv:1804.04528, JINST 13 (2018) P06015 — Fig. 7 (ereco+ID vs eta, Loose & Tight ID, pT>=20 GeV) and text p.18 (lines 1244-1254)
- **Verifier corrections:** CRITICAL: bin eta 0.2-0.4 central=0.955 is WRONG. This is the |eta|=0.3 dip bin; the measured DATA efficiency plunges to ~0.87 (MC ~0.89), not 0.955. The extraction names the dip in its note but uses a value ~0.085 too high, missing the dip depth entirely. Correct central ~0.87 (unc_rel ~0.02 covering data/MC ~2%). SHAPE ERROR: bin eta 1.2-1.6 central=0.960 with note "lower tight-ID eff" is wrong sign — this region is a local PEAK at ~0.989 in data, not a low; should be ~0.985-0.99. SHAPE ERROR:

## CMS.JES

- **Verdict:** REJECT  | Run-2: true | dedicated figure: true | bins: 0
- **Source:** arXiv:2301.02175 (proceedings); underlying NSC parameterization and per-eta fits from CMS JINST 12 (2017) P02014, arXiv:1607.03663 — arXiv:2301.02175 Fig.6 left (JER vs pt, anti-kT R=0.4 PF+CHS, 0.0<|eta|<0.5); NSC fit form Eq.38 and Fig.37/38 of arXiv:1607.03663 (C_quark=
- **Verifier corrections:** Major fabrication: the entire 21-value per-eta-bin NSC table (N=3.4/3.6/4.2/4.0/3.6/3.0/3.5 GeV; S=0.83/0.85/0.90/0.95/1.05/1.20/1.10; C=0.043/0.046/0.050/0.045/0.040/0.050/0.055) for the 7 eta bins 0-0.5...3.0-5.0 appears NOWHERE in either cited source. Neither paper tabulates per-eta N, S, C fit parameters; the proceedings (2301.02175) gives no NSC fit at all, and the 8 TeV JINST paper gives only global |eta|<1.3 fits for R=0.5/0.7. These per-bin numbers and their unc_rel bands (0.05-0.25) are

## CMS.BTagging

- **Verdict:** ACCEPT  | Run-2: true | dedicated figure: true | bins: 0
- **Source:** arXiv:1712.07158 (JINST 13 (2018) P05011), CMS Collaboration — Table 2 (integrated WP eff, pt>20 GeV) + Appendix A Table 6 and Fig. 63 (pt parameterization of SF*efficiency); DeepCSV P(b)+P(bb) Medium wo
- **Verifier corrections:** none. All extracted bins, central values, source, and locator (Table 2 + Appendix A Table 6 + Fig 63, DeepCSV P(b)+P(bb) Medium WP, 13 TeV 35.9 fb-1 2016) are confirmed exactly. Minor non-blocking note: the per-bin unc_rel values (2-6% on b-eff, 15-25% on c, 15-25% on udsg) are not tabulated as such in Table 6 — they are the extractor's stated approximate SF-uncertainty-band estimates (explicitly flagged "illustrative" / drawn from the SF figures Fig.36/44/48), so they are not contradicted by th

