# Per-parameter provenance record schema

Each `measured` parameter from the audit gets one record. Records are the raw
material for both the new cards and the JINST tables. Proposed storage:
`provenance.yaml` (one list entry per record). Schema:

```yaml
- param_id: ATLAS.MuonMomentumSmearing.eta0_05.a   # stable unique key
  card: delphes_card_ATLAS.tcl
  module: MuonMomentumSmearing
  quantity: track_momentum_resolution_const_term     # controlled vocabulary
  object: muon
  eta_min: 0.0
  eta_max: 0.5
  pt_range: ">0.1 GeV"
  functional_form: "sqrt(a^2 + (b*pt)^2)"
  role: a                          # which coefficient in the form this record is
  current_value: 0.01              # value hard-coded in the card today
  current_uncertainty: null        # none recorded in card

  # --- filled in Phase 1 (source mapping) ---
  source:
    collaboration: ATLAS
    title: "..."
    arxiv: "..."
    doi: "..."
    report_number: "..."           # e.g. ATL-PHYS-PUB-...
    year: 0
    locator: "Fig. 5(b), |eta|<0.5 curve"   # EXACT table/figure/eqn

  # --- filled in Phase 2 (extraction + verification) ---
  extracted_value: null
  extracted_uncertainty: null      # +/- ; or asymmetric [lo, hi]
  uncertainty_type: null           # stat | syst | total | spread
  extraction_method: null          # e.g. "read off Fig.5 at pt=10,100 GeV; refit a,b"
  matches_current: null            # true/false vs current_value (flag if false)
  verification:
    verified_by_independent_agent: false
    verifier_locator_agrees: false
    notes: ""
  status: audited                  # audited -> sourced -> extracted -> verified -> applied
```

## Controlled vocabulary for `quantity`

- `tracking_efficiency`, `reco_efficiency`
- `track_momentum_resolution_const_term` (a), `track_momentum_resolution_pt_term` (b)
- `ecal_resolution_stochastic` (S), `ecal_resolution_const` (C), `ecal_resolution_noise` (N), `ecal_eta_prefactor`
- `hcal_resolution_stochastic`, `hcal_resolution_const`, `hcal_resolution_noise`
- `jet_energy_scale`
- `btag_efficiency`, `btag_c_mistag`, `btag_light_mistag`
- `tau_efficiency`, `tau_mistag`

## Status flow

`audited` (Phase 0, done) → `sourced` (Phase 1) → `extracted` (Phase 2) →
`verified` (Phase 2, independent agent agrees) → `applied` (Phase 3, written to
baseline/uncertainty card).

A record may only advance to `applied` once `verification.verified_by_independent_agent`
is `true`. Records where `matches_current` is `false` are surfaced for your
review before any card value changes.
