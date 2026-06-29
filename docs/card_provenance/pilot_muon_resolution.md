# Pilot — muon momentum resolution (Phases 1+2 run end-to-end)

This is the first parameterization block taken through the full
source -> extract -> **independently verify** -> record loop. It validates the
methodology before fanning out over the rest of the audit.

## Loop as executed

1. **Source mapping + extraction** — two independent agents (one per experiment)
   read the actual performance papers and extracted sigma(pt)/pt vs pt with
   exact figure/table locators.
2. **Adversarial verification** — two *separate* agents re-read each cited source
   cold and confirmed or refuted every numeric claim (default: reject if not
   found). **Both returned ACCEPT**; all anchor numbers confirmed verbatim.
3. **Record** — `provenance.yaml` (12 coefficient records, status `verified`),
   `sources.bib` (5 verified references), and cited comments added to both cards.
   Live card values were **not** changed (no silent overwrites).

## What the pilot found

Both cards hard-code the *same* muon resolution, which is itself questionable
(the ATLAS and CMS muon systems differ). Form: `sqrt(a^2 + (b*pt)^2)`.

| Region | a, b (both cards) | Verified verdict |
|--------|-------------------|------------------|
| \|η\|≤0.5 | 0.010, 1.0e-4 | **CMS:** barrel floor ~1% exact (1804.04528 §7.1). **ATLAS:** a=0.010 → ~1.0% is **too optimistic** vs measured 1.7–2.3% combined-muon (1603.05598 §8.2). b-term high-pt (~10% @1 TeV) consistent. |
| 0.5–1.5 | 0.015, 1.5e-4 | No matching bin in either experiment (boundaries are a Delphes choice). Interpolation; not directly measured. |
| 1.5–2.5 | 0.025, 3.5e-4 | **ATLAS:** matches endcap 2.3%/2.9% (J/ψ,Z) well. **CMS:** a=0.025 → 2.5% mildly **optimistic** vs CMS-quoted 3% endcap. Endcap high-pt term unvalidated (CMS Fig. 9 is barrel-only). |

## Key citable sources (verified)

- **ATLAS form + curve:** arXiv:1404.4562 (EPJC 74 (2014) 3130) Eq. (2), Figs. 17–18.
- **ATLAS 13 TeV anchors:** arXiv:1603.05598 (EPJC 76 (2016) 292) §8.2.
- **ATLAS high-pt:** arXiv:2012.00578 (EPJC 81 (2021) 578) Fig. 2.
- **CMS floors + high-pt barrel:** arXiv:1804.04528 (JINST 13 (2018) P06015) §7.1, §7.2/Fig. 9.

## Open items surfaced for human review (Phase 3)

1. ATLAS central floor a=0.010 → revise upward toward ~0.017 (1.7%)? (combined-muon
   anchor; Delphes' single smearing maps most directly to ID-only Eq. 2 — decide
   which the card should represent).
2. CMS endcap floor a=0.025 → revise toward 0.030 (3%)?
3. ATLAS/CMS sharing identical coefficients — should they diverge?
4. Eta binning (0.5/1.5/2.5) matches neither detector; keep for backward
   compatibility or re-bin to detector boundaries in the new baseline card?

## Cost / scaling note

This block (6 coefficients × 2 cards) used 4 agents (2 extract + 2 verify),
~150k subagent tokens total. The remaining audit is ~50 measured parameters;
many share a source already named in the card, so per-parameter cost drops once
a source PDF is in hand. Recommend fanning out by source-paper (one agent reads
one paper, extracts all parameters it backs) rather than by single parameter.
