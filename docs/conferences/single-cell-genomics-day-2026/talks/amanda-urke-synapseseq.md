# Amanda Urke — SynapseSeq: sequencing-based synaptic connectomics

**Speaker:** **Amanda Urke** — MD/PhD student, **Macosko Lab**, Broad Institute / Harvard. Senior author: **Evan Z. Macosko**. Part of the **Brain Connects Consortium**.
**Slot:** SCGD26, Jun 12, 2026 (12:20–12:40 PM)
**Talk title:** "Protein-guided RNA barcoding links transcriptomes to synaptic architecture"
**Method:** **SynapseSeq** / **Synapse-seq** — AAV-barcoded synaptic neuroanatomy linked to single-cell gene expression
**Recording:** SCGD26 livestream — preprint: [bioRxiv 10.64898/2026.02.26.705527](https://www.biorxiv.org/content/10.64898/2026.02.26.705527v1) (posted Feb 27, 2026)
**Status:** Captured from session transcript

## Thesis

Pair **synaptic neuroanatomy with the transcriptomically defined neuron it belongs to**. Existing viral tracers (Sindbis/rabies — e.g. MAPseq/BARseq lineage) label connectivity but lose endogenous gene expression and aren't the field's standard for stable expression. **AAVs** (low immunogenicity, cell-type targeting, BBB-crossing engineerable) preserve endogenous expression — so SynapseSeq builds barcoded connectomics on AAV.

## How it works

Two components co-delivered by AAV:

1. **Targeting protein** — an interchangeable subcellular-localization domain fused to GFP + the RNA-binding protein **PCP**.
2. **Barcode transgene** — mScarlet + a UTR with **PP7 stem-loops**, a unique **32-bp barcode**, and poly(A).

PCP binds the PP7 stem-loops, so the barcoded mRNA is trafficked wherever the targeting protein goes:
- **Presynaptic:** synaptophysin → axonal terminals.
- **Postsynaptic:** a nanobody to endogenous **PSD-95** → excitatory postsynapses.

Read-out: single-nucleus / spatial transcriptomics at the soma for source-cell identity; **Slide-seq** (10 µm beads) or bulk RNA-seq at projection/dendrite sites for the trafficked barcodes; then computationally match barcodes back to source cells. **Removing the stem-loops** is the negative control (barcode no longer rides along).

## Key results

- **Presynaptic validation (mouse V1):** ~80% of barcode colocalizes with GFP-synaptophysin at the thalamus (DLGN); **~7×** barcode-density drop in the stem-loop-deleted control; specificity stable over weeks of incubation (relevant for primate timelines).
- **Brain-wide projections:** ~900 layer-specific cells mapped to targets; reproduced known motifs (layer-5 ET widespread projections; layer-5 NP lacking long-range). Slide-seq resolution teased apart **two layer-6 CT subtypes** with different DLGN-vs-LP connectivity. Anterior-cortex injection revealed medial/lateral layer-5 ET topography and **collaterals** (one neuron → medulla + caudoputamen), plus a cadherin-defined layer-5 ET subtype lacking the striatal collateral.
- **Cross-species dopamine (marmoset):** 10×10 mm barcoded bead arrays; >14,000 SynapseSeq barcodes across ~9,000 beads; highest density in ipsilateral caudate-putamen / nucleus accumbens (nigrostriatal) + mesocortical motor-cortex signal.
- **Postsynaptic (PSD-95) in hippocampus:** Slide-seq on serial sections reconstructed 3D dendritic trees; **~250,000 matches / ~18,000 barcodes**, ~8,000 pyramidal + ~2,000 dentate-granule neurons. Recovered stereotyped geometries (CA1 proximal-apical density; DG unidirectional) and a coordinated gene-expression × morphology comparison across CA subfields (CA1 uniquely enriched for postsynaptic GO terms + most pronounced superficial/deep apical-density difference).

## Q&A highlights

- **Cell-type transduction/trafficking bias** (e.g. CA2 high AAV tropism) is largely normalized by dividing barcode read-out by per-cell expression.
- **Main current challenge:** scaling to large primate/human brains on much larger spatial arrays — riding the falling cost/rising scale of sequencing so any lab can run it without specialized equipment.

## Connections to the corpus

- Sequencing-based connectomics / barcode recording — sibling to [GEMINI](molecular-recorder-gemini.md) (in situ recording) and the MAPseq/BARseq lineage; spatial read-out overlaps AACR [single-cell-spatial-omics](../../aacr-2026/topics/single-cell-spatial-omics/).
- Macosko-lab / Slide-seq spatial substrate connects to the spatial-transcriptomics thread in [`single-cell-genomics-2026/`](../../single-cell-genomics-2026/).

## Sources

- SCGD26 schedule (speaker, affiliation, talk title): <https://satijalab.org/scgd26/> — listed as **Amanda Urke (Harvard University)**, "Protein-guided RNA barcoding links transcriptomes to synaptic architecture", 12:20–12:40 PM.
- Preprint: Urke A, Dolan M-J, Silverman J, Kim M, Pineda J, Garcia S, Luu J, Buckley A, Kumar V, Zhao B, Chan K, Nadaf N, Balderrama KS, Arnold DB, Stevens B, Deverman BE, **Macosko EZ**. "Protein-guided RNA barcoding links transcriptomes to synaptic architecture." bioRxiv, posted Feb 27, 2026. DOI [10.64898/2026.02.26.705527](https://www.biorxiv.org/content/10.64898/2026.02.26.705527v1).

## Verify / open questions

- Open-resource links (code/data repos): not yet located — to be released with the preprint; search returned no GitHub/Zenodo link.
