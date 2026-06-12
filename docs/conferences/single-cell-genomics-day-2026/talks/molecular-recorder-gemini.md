# GEMINI — a genetically encoded protein-assembly molecular recorder

**Speaker:** **Dingchang Lin** (Johns Hopkins University) — hiring PhDs + postdocs; collaboration with the **David Baker Lab (University of Washington, Institute for Protein Design)**
**Talk title:** "Genetically encoded assembly recorder temporally resolves cellular history"
**Slot:** SCGD26, Jun 12, 2026 — first talk after the host's opening (10:40–11:00 AM EDT)
**Method:** **GEMINI** ("Granularly Expanding Memory for Intracellular Narrative Integration")
**Recording:** SCGD26 livestream (YouTube) — verify archived link
**Status:** Captured from session transcript

## Thesis

A recorder smaller than a "TrueRing"-style device that fits *inside* a cell, is **genetically encoded** (so it can be expressed in arbitrarily many cells), and self-assembles into a protein particle whose growth predictably encodes the cell's signaling history for later optical read-out. Analog, not digital: the *intensity* of each band carries signal amplitude, and band *position* carries timing.

## How it works

Three subunit types co-assemble into a particle (shown growing as a hexagonal structure in live cells):

1. **Blank subunit** — drives constant, predictable particle growth (the "ruler" for later temporal decoding).
2. **Reporter subunit** — carries a fluorophore; its expression/incorporation is driven by a cell signal (e.g. an **NF-κB** promoter driving GFP-tagged subunit), so a hyperactive cell deposits a bright band.
3. **Timestamp subunit** — incorporation is gated by an external stimulus, correlating wall-clock time to band position.

- The particle is a **computationally designed self-assembling protein particle** (Baker Lab collaboration); the best of many screened variants grows with near-perfect predictability, fit by a simple mathematical growth model.
- **Timestamping uses HaloTag chemistry** — switching small-molecule dye colors creates a color-transition band marking a known time; an earlier *linear* recorder required fibers to lie parallel to the imaging plane, whereas the **isotropic** particle reads out identically at any orientation (enables high-throughput tissue read-out).

## Key results

- **In vitro decoding:** two timestamps 11 h apart bracket a signal; decoded onset shifts with addition time. Temporal **accuracy and precision both sub-hour**.
- **NF-κB dynamics:** decoded TNF-α-driven activation (≈2 h delay vs. timestamp, from transcription/translation lag) and **deactivation** (TNF-α washout); resolved **multiple on/off cycles** as distinct bands in single particles.
- **In vivo — tumor xenograft:** clonal line injected into immunodeficient mice; LPS-induced systemic inflammation read out via tumor particles; dose-dependent GFP; co-stained CD31 vasculature → higher vascular density correlated with **earlier NF-κB peak time** and higher intensity. **Blood-brain-barrier-permeable dye** enabled systemic in vivo timestamping (retro-orbital injection); LPS injected at different days produced cleanly separable onset bands across a 48 h window.
- **Native brain:** AAV-delivered particles expressed in cortex/hippocampus with minimal impact on neuronal density, GFAP, calcium dynamics (running-wheel + GCaMP), or behavior (open field, short-term memory). Cellular-resolution pipeline registers each particle to its neuron and scales to whole-brain. Recorded **transcription history** (tet-on / doxycycline timing) and **seizure-induced neural activity**; in-brain precision is lower than in vitro/xenograft, attributed to heterogeneity from local AAV injection.

## Connections to the corpus

- **Recording-based lineage/temporal tracing** — sibling to the DNA/RNA "molecular tape recorder" thread; see [Kevin Chao — TimeVault](kevin-chao-timevault.md) (RNA time-capsule) and [Amanda Urke — SynapseSeq](amanda-urke-synapseseq.md) (barcode recording of connectivity).
- **Designed proteins** — Baker-Lab computationally designed assembly intersects the protein-design axis (cf. EuroBioC 2025 Ferruz keynote on protein design with language models).
- AACR axis: single-cell + spatial (in situ temporal read-out).

## Sources

- SCGD26 schedule (speaker, affiliation, talk title): <https://satijalab.org/scgd26/>
- Preprint — Yan, Lu, Li et al., "Genetically encoded assembly recorder temporally resolves cellular histories *in cellulo* and *in vivo*," bioRxiv 2025.07.16.664392: <https://www.biorxiv.org/content/10.1101/2025.07.16.664392v1>
- Journal — "Genetically encoded assembly recorder temporally resolves cellular history," *Nature* (2026), DOI [10.1038/s41586-026-10323-y](https://www.nature.com/articles/s41586-026-10323-y) (author list includes David Baker, UW Institute for Protein Design, confirming the protein-design collaboration)
