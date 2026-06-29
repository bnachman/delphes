# Audit — `cards/delphes_card_ATLAS.tcl`

Phase-0 inventory of every physics parameterization in the ATLAS Run-2 card.
Columns:

- **Loc** — line(s) in the card.
- **Type** — `measured` (needs value+uncertainty+source) or `choice`/`geometry` (document only).
- **Current value / form** — exactly what the card hard-codes today.
- **Ref in card?** — reference already present in the `.tcl` (verbatim), or — if none.
- **Source status** — what Phase-1/2 must still supply.

> "Ref in card?" reflects only the existing comment; it is not a check that the
> value actually matches that reference.

## 1. Detector geometry / magnetic field

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 72–78 | `ParticlePropagator` Radius / HalfLength / Bz | geometry | R=1.15 m, L=3.51 m, Bz=2.0 T | — | Cite ATLAS detector paper (JINST 3 S08003). |

## 2. Tracking / reconstruction efficiency (η, pᴛ step functions)

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 91–96 | ChargedHadron tracking eff | measured | |η|≤1.5: 0.70 (0.1<pᴛ≤1), 0.95 (pᴛ>1); 1.5<|η|≤2.5: 0.60 / 0.85; |η|>2.5: 0 | — | Source needed (ATLAS tracking performance, Run 2). |
| 110–117 | Electron tracking eff | measured | |η|≤1.5: 0.73 / 0.95 / 0.99; 1.5<|η|≤2.5: 0.50 / 0.83 / 0.90 | — | Source needed (ATLAS e reco/ID performance). |
| 131–136 | Muon tracking eff | measured | |η|≤1.5: 0.75 / 0.99; 1.5<|η|≤2.5: 0.70 / 0.98 | — | Source needed (ATLAS muon reco performance). |
| 432–435 | Photon efficiency | measured | 0.95 (|η|≤1.5), 0.85 (1.5<|η|≤2.5), pᴛ>10 | — | Source needed (ATLAS photon ID). |
| 467–470 | Electron efficiency | measured | 0.95 / 0.85, pᴛ>10 | — | Source needed (ATLAS e ID working point). |
| 501–504 | Muon efficiency | measured | 0.95 (|η|≤1.5), 0.85 (1.5<|η|≤2.7), pᴛ>10 | — | Source needed (ATLAS muon ID). |

## 3. Track momentum resolution — `sqrt(a² + (b·pᴛ)²)`

| Loc | η region | Type | a (const term) | b (·pᴛ term, GeV⁻¹) | Ref in card? | Source status |
|-----|----------|------|----------------|---------------------|--------------|---------------|
| 150–152 | charged hadron, |η|≤0.5 | measured | 0.06 | 1.3e-3 | — | Source needed (ID resolution). |
| | 0.5<|η|≤1.5 | measured | 0.10 | 1.7e-3 | — | " |
| | 1.5<|η|≤2.5 | measured | 0.25 | 3.1e-3 | — | " |
| 166–168 | electron, |η|≤0.5 | measured | 0.03 | 1.3e-3 | — | Source needed. |
| | 0.5<|η|≤1.5 | measured | 0.05 | 1.7e-3 | — | " |
| | 1.5<|η|≤2.5 | measured | 0.15 | 3.1e-3 | — | " |
| 181–183 | muon, |η|≤0.5 | measured | 0.01 | 1.0e-4 | — | Source needed (combined muon pᴛ resolution). |
| | 0.5<|η|≤1.5 | measured | 0.015 | 1.5e-4 | — | " |
| | 1.5<|η|≤2.5 | measured | 0.025 | 3.5e-4 | — | " |

## 4. Calorimeter energy resolution — `sqrt(E²·C² + E·S² + N²)`

| Loc | Subdetector / η region | Type | C (const) | S (stochastic) | N (noise) | Ref in card? | Source status |
|-----|------------------------|------|-----------|----------------|-----------|--------------|---------------|
| 282–283 | ECal, |η|≤3.2 | measured | 0.0017 | 0.101 | — | `physics/0608012` (JINST 3 S08003), Schram proc., Krieger proc. (comment, lines 279–281) | Confirm value↔source. |
| | ECal, 3.2<|η|≤4.9 (FCal) | measured | 0.0350 | 0.285 | — | as above | Confirm. |
| 349–351 | HCal, |η|≤1.7 | measured | 0.0302 | 0.5205 | 1.59 | `hep-ex/0004009`, Schram proc. (comment, lines 346–347) | Confirm value↔source. |
| | HCal, 1.7<|η|≤3.2 | measured | 0.0500 | 0.706 | — | as above | Confirm. |
| | HCal, 3.2<|η|≤4.9 | measured | 0.0942 | 1.00 | — | as above | Confirm. |

## 5. Calorimeter granularity (tower η/φ maps)

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 225–254 | ECal EtaPhiBins (barrel/endcap) | geometry | 0.0174 Δη, 360 φ-bins to |η|≤3 | — | Cite TDR/detector paper granularity. |
| 250–254 | ECal HF bins | geometry | 36 φ-bins, 3<|η|<5 | "present CMS granularity for HF" (comment) | Note: HF map copied from CMS — flag for ATLAS-appropriate source. |
| 315–323 | HCal EtaPhiBins | geometry | 36/18 φ-bins | — | Cite TDR granularity. |

## 6. Isolation working points

| Loc | Object | Type | DeltaRMax | PTMin | PTRatioMax | Ref in card? | Source status |
|-----|--------|------|-----------|-------|------------|--------------|---------------|
| 448–452 | Photon | choice | 0.5 | 0.5 | 0.12 | — | Document WP definition. |
| 483–487 | Electron | choice | 0.5 | 0.5 | 0.12 | — | " |
| 517–521 | Muon | choice | 0.5 | 0.5 | 0.25 | — | " |

## 7. Jet energy scale

| Loc | Parameter | Type | Current value | Ref in card? | Source status |
|-----|-----------|------|---------------|--------------|---------------|
| 622 | `ScaleFormula` | measured | `sqrt((3.0 - 0.2·|η|)²/pᴛ + 1.0)` | — | Source needed (ATLAS JES / in-situ calibration). |

## 8. Flavor tagging

| Loc | Channel | Type | Current value | Ref in card? | Source status |
|-----|---------|------|---------------|--------------|---------------|
| 658 | b-tag light mistag (PDG 0) | measured | `0.002 + 7.3e-6·pᴛ` | "based on ATL-PHYS-PUB-2015-022" (line 655) | Confirm value↔note; add uncertainty. |
| 661 | b-tag c mistag (PDG 4) | measured | `0.20·tanh(0.02·pᴛ)/(1+0.0034·pᴛ)` | as above | Confirm. |
| 664 | b-tag b eff (PDG 5) | measured | `0.80·tanh(0.003·pᴛ)·30/(1+0.086·pᴛ)` | as above | Confirm; this is the 70%-ish WP. |
| 696–699 | τ-tag eff / mistag | measured | 1-prong 0.70, multi 0.60, mistag 0.02 / 0.01 | "ATL-PHYS-PUB-2015-045 (medium WP)" (line 695) | Confirm value↔note; add uncertainty. |

## 9. Object-finding choices (document only, no uncertainty)

| Loc | Parameter | Current value |
|-----|-----------|---------------|
| 579, 609 | GenJet / Jet `ParameterR` | 0.6 (anti-kᴛ) |
| 581, 610 | `JetPTMin` | 20 GeV |
| 636 | JetFlavorAssociation `DeltaR` / PartonEtaMax | 0.5 / 2.5 |
| 678–683 | TauTagging `DeltaR`, TrackPTMin, TauEtaMax | 0.2 / 1.0 / 2.5 |

---

**Counts (parameters needing a verified source + uncertainty):**
tracking/reco eff ≈ 6 blocks, momentum resolution = 9 coefficients (3 objects × 3 η),
calo resolution = 5 η-regions (≈ 12 coefficients), JES = 1 formula,
flavor tagging = 4 channels. Geometry / granularity / isolation / jet-choice
entries are documented but not assigned uncertainties.
