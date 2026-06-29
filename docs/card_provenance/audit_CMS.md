# Audit — `cards/delphes_card_CMS.tcl`

Phase-0 inventory of every physics parameterization in the CMS Run-2 card.
Same column conventions as `audit_ATLAS.md`. "Ref in card?" reflects only the
existing comment; matching the value to that reference is Phase-2 work.

## 1. Detector geometry / magnetic field

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 72–78 | `ParticlePropagator` Radius / HalfLength / Bz | geometry | R=1.29 m, L=3.00 m, Bz=3.8 T | — | Cite CMS detector paper (JINST 3 S08004) / tracker TDR. |

## 2. Tracking / reconstruction efficiency (η, pᴛ step functions)

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 92–97 | ChargedHadron tracking eff | measured | |η|≤1.5: 0.70 / 0.95; 1.5<|η|≤2.5: 0.60 / 0.85 | — | Source needed (CMS tracking performance, e.g. 1405.6569). |
| 111–118 | Electron tracking eff | measured | |η|≤1.5: 0.73 / 0.95 / 0.99; 1.5<|η|≤2.5: 0.50 / 0.83 / 0.90 | — | Source needed (CMS e reco). |
| 132–140 | Muon tracking eff | measured | |η|≤1.5: 0.75 / 0.99 / 0.99·exp(...); 1.5<|η|≤2.5: 0.70 / 0.98 / 0.98·exp(...) | — | Source needed (CMS muon reco); note high-pᴛ exp() roll-off. |
| 445–448 | Photon efficiency | measured | 0.95 (|η|≤1.5), 0.85 (1.5<|η|≤2.5), pᴛ>10 | — | Source needed (CMS photon ID). |
| 480–483 | Electron efficiency | measured | 0.95 / 0.85, pᴛ>10 | — | Source needed (CMS e ID WP). |
| 514–517 | Muon efficiency | measured | 0.95 (|η|≤1.5), 0.95 (1.5<|η|≤2.4), pᴛ>10 | — | Source needed (CMS muon ID). |

## 3. Track momentum resolution — `sqrt(a² + (b·pᴛ)²)`

| Loc | η region | Type | a (const) | b (·pᴛ, GeV⁻¹) | Ref in card? | Source status |
|-----|----------|------|-----------|----------------|--------------|---------------|
| 155–157 | charged hadron, |η|≤0.5 | measured | 0.06 | 1.3e-3 | "based on arXiv:1405.6569" (line 154) | Confirm value↔source; add uncertainty. |
| | 0.5<|η|≤1.5 | measured | 0.10 | 1.7e-3 | as above | Confirm. |
| | 1.5<|η|≤2.5 | measured | 0.25 | 3.1e-3 | as above | Confirm. |
| 172–174 | electron, |η|≤0.5 | measured | 0.03 | 1.3e-3 | "based on arXiv:1502.02701" (line 171) | Confirm. |
| | 0.5<|η|≤1.5 | measured | 0.05 | 1.7e-3 | as above | Confirm. |
| | 1.5<|η|≤2.5 | measured | 0.15 | 3.1e-3 | as above | Confirm. |
| 188–190 | muon, |η|≤0.5 | measured | 0.01 | 1.0e-4 | — | Source needed (CMS muon pᴛ resolution, e.g. 1804.04528). |
| | 0.5<|η|≤1.5 | measured | 0.015 | 1.5e-4 | — | " |
| | 1.5<|η|≤2.5 | measured | 0.025 | 3.5e-4 | — | " |

## 4. Calorimeter energy resolution

ECal carries η-dependent prefactors multiplying the `sqrt(E²·C² + E·S² + N²)` core.

| Loc | Subdetector / η region | Type | Prefactor | C | S | N | Ref in card? | Source status |
|-----|------------------------|------|-----------|---|---|---|--------------|---------------|
| 291 | ECal, |η|≤1.5 | measured | (1+0.64·η²) | 0.008 | 0.11 | 0.40 | "Eta shape arXiv:1306.2016, Energy shape arXiv:1502.02701" (line 290) | Confirm value↔source. |
| 292 | ECal, 1.5<|η|≤2.5 | measured | (2.16+5.6(|η|−2)²) | 0.008 | 0.11 | 0.40 | as above | Confirm. |
| 293 | ECal, 2.5<|η|≤5.0 (HF) | measured | 1 | 0.107 | 2.08 | — | as above | Confirm / find HF source. |
| 361 | HCal, |η|≤3.0 | measured | 1 | 0.050 | 1.50 | — | — | Source needed (CMS HCAL resolution / combined calo). |
| 362 | HCal, 3.0<|η|≤5.0 | measured | 1 | 0.130 | 2.70 | — | — | Source needed (HF). |

## 5. Calorimeter granularity (tower η/φ maps)

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 233–263 | ECal EtaPhiBins | geometry | 0.0174 Δη barrel/endcap; HF coarse | — | Cite ECAL/HGCAL granularity. |
| 322–338 | HCal EtaPhiBins | geometry | 72/36/18 φ-bins by region | — | Cite HCAL granularity. |

## 6. Isolation working points

| Loc | Object | Type | DeltaRMax | PTMin | PTRatioMax | Ref in card? | Source status |
|-----|--------|------|-----------|-------|------------|--------------|---------------|
| 461–465 | Photon | choice | 0.5 | 0.5 | 0.12 | — | Document WP. |
| 496–500 | Electron | choice | 0.5 | 0.5 | 0.12 | — | " |
| 530–534 | Muon | choice | 0.5 | 0.5 | 0.25 | — | " |

## 7. Jet energy scale

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 673 | `ScaleFormula` | measured | `sqrt((2.5 - 0.15·|η|)²/pᴛ + 1.0)` | — | Source needed (CMS JES, JINST 12 P02014). |

## 8. Flavor tagging

| Loc | Channel | Type | Current value | Ref in card? | Source status |
|-----|---------|------|---------------|--------------|---------------|
| 709 | b-tag light mistag (PDG 0) | measured | `0.01 + 0.000038·pᴛ` | "based on arXiv:1211.4462" (line 706) | Confirm value↔source; add uncertainty. |
| 712 | b-tag c mistag (PDG 4) | measured | `0.25·tanh(0.018·pᴛ)/(1+0.0013·pᴛ)` | as above | Confirm. |
| 715 | b-tag b eff (PDG 5) | measured | `0.85·tanh(0.0025·pᴛ)·25/(1+0.063·pᴛ)` | as above | Confirm WP; add uncertainty. |
| 736–738 | τ-tag mistag / eff | measured | mistag 0.01, τ eff 0.6 | — | Source needed (CMS τ ID WP). |

## 9. Object-finding choices (document only, no uncertainty)

| Loc | Parameter | Current value |
|-----|-----------|---------------|
| 593, 622 | GenJet / Jet `ParameterR` | 0.5 (anti-kᴛ) |
| 638 | FatJet `ParameterR` + grooming | R=0.8; SoftDrop β=0, zcut=0.1; trim/prune params |
| 595, 624, 658 | `JetPTMin` | 20 / 20 / 200 GeV |
| 687–689 | JetFlavorAssociation DeltaR / PartonEtaMax | 0.5 / 2.5 |
| 727–731 | TauTagging DeltaR / TauEtaMax | 0.5 / 2.5 |

---

**Counts (parameters needing a verified source + uncertainty):**
tracking/reco eff ≈ 6 blocks, momentum resolution = 9 coefficients,
calo resolution = 5 η-regions (≈ 13 coefficients incl. ECal prefactors),
JES = 1 formula, flavor tagging = 4 channels. Several CMS blocks already cite a
source (1405.6569, 1502.02701, 1306.2016, 1211.4462) — these need value↔source
confirmation + uncertainties rather than fresh sourcing.
