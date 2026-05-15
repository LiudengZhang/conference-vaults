# ESM-3 — Hayes et al. (EvolutionaryScale)

**One-line description** — A frontier multimodal generative protein language model that reasons jointly over sequence, structure, and function as three parallel token tracks; trained at 98B parameters on 2.78 billion proteins, ESM-3 generated esmGFP, a novel green fluorescent protein with only 36% identity to avGFP — equivalent, by the authors' phylogenetic argument, to ~500 million years of natural evolution.

- **Authors:** Thomas Hayes, Roshan Rao, Halil Akin, Nicholas J. Sofroniew, Deniz Oktay, Zeming Lin, Robert Verkuil, Vincent Q. Tran, Jonathan Deaton, Marius Wiggert, Rohil Badkundri, Irhum Shafkat, Jun Gong, Alexander Derry, Raul S. Molina, Neil Thomas, Yousuf A. Khan, Chetan Mishra, Carolyn Kim, Liam J. Bartie, Matthew Nemeth, Patrick D. Hsu, Tom Sercu, Salvatore Candido, Alexander Rives
- **Affiliation(s):** EvolutionaryScale (with Arc Institute collaboration for the esmGFP wet-lab work)
- **Track / workshop:** Not an ICLR 2026 paper per se — included in this vault as a **load-bearing foundation-model dependency** for several ICLR 2026 protein-design entries (e.g. TEA-alphabet's ESM-class backbone, GEM workshop binder pipelines that score in ESM-3 latent space)
- **Science:** [10.1126/science.ads0018](https://www.science.org/doi/10.1126/science.ads0018) (Hayes et al., *Science* 2025; PubMed [39818825](https://pubmed.ncbi.nlm.nih.gov/39818825/))
- **bioRxiv (preprint):** [2024.07.01.600583v1](https://www.biorxiv.org/content/10.1101/2024.07.01.600583v1)
- **Blog / technical report:** [evolutionaryscale.ai/blog/esm3-release](https://www.evolutionaryscale.ai/blog/esm3-release)
- **Code / SDK:** [github.com/evolutionaryscale/esm](https://github.com/evolutionaryscale/esm) (`pip install esm`)
- **Weights:** ESM3-small-open (1.4B) on Hugging Face under Cambrian Non-Commercial License; ESM3-medium (7B) and ESM3-large (98B) gated via EvolutionaryScale Forge API
- **CZI Virtual Cells Platform mirror:** [virtualcellmodels.cziscience.com/model/esm3](https://virtualcellmodels.cziscience.com/model/esm3)

## What it does

ESM-3 is a generative masked language model over proteins that, unlike its predecessor ESM-2, treats sequence, three-dimensional structure, and function as three jointly-modelled discrete token streams rather than a sequence-only input. You can prompt it with any combination of the three (e.g. "give me the sequence for this active-site geometry plus this InterPro keyword") and iteratively decode the missing tracks — making it a single model for structure prediction, inverse folding, function annotation, and de novo design.

## How it works

**Architecture.** ESM-3 is a bidirectional transformer trunk that processes seven input tracks fused in a single latent space: (a) amino-acid sequence tokens, (b) raw structure coordinates, (c) discrete structure tokens, (d) 8-class secondary-structure labels (SS8), (e) quantized solvent-accessible surface area (SASA), (f) function-keyword tokens, and (g) per-residue InterPro annotation binary features. **Geometric attention** in the first transformer block lets the model condition directly on atomic coordinates when they are provided.

**Tokenization — the three-track core.** The headline architectural move is collapsing structure and function into discrete alphabets so the same masked-LM machinery that worked on sequence in ESM-2 can be applied across modalities:

- **Sequence track:** standard amino-acid vocabulary.
- **Structure track:** local 3D neighbourhoods around each residue are encoded by an **attentive VQ-VAE** into a vocabulary of 4,096 discrete structure tokens, one per residue, with an iterative-decoding scheme for generation.
- **Function track:** function-keyword tokens (drawn from controlled vocabularies including InterPro) plus binary residue-annotation features.

This lets a single forward pass take any subset of tracks as input and decode any other subset as output.

**Pretraining corpus.** Approximately **2.78 billion natural protein sequences** from UniRef, MGnify, JGI metagenomics, and PDB, augmented with synthetic data from predicted structures (AlphaFold-DB / ESMFold) and inverse-folded predicted sequences. Cluster-based sampling controls redundancy.

**Pretraining objective.** Generative masked-language modelling jointly across all token tracks (sequence, structure, SS8, SASA, function, residue annotations) under a **variable-rate masking schedule** — the noise rate is sampled per example so the model learns to predict tokens from arbitrary masking fractions and conditioning combinations. This is what enables the same checkpoint to do conditional generation, inverse folding, structure prediction, and function annotation at inference.

**Parameter scales.** Three checkpoints were trained: **1.4B (ESM3-small)**, **7B (ESM3-medium)**, and **98B (ESM3-large)**. The 98B variant produces the most biologically realistic proteins and is the configuration reported in the *Science* headline results.

**Compute.** The 98B model was trained with **~1.07 × 10²⁴ FLOPs** on **771 billion unique tokens** — described in the technical report as the most compute applied to any biological model at time of release.

**Fine-tuning recipe.** The released SDK supports two routes: (a) low-rank adaptation / supervised fine-tuning of the open 1.4B checkpoint locally for downstream classification or generation tasks; (b) prompted iterative decoding without any weight updates, using the variable-masking pretraining objective to do conditional design at inference (this is the recipe used for esmGFP). For atomic-coordination prompting in the *Science* paper, no extra fine-tuning is required — atomic positions are passed directly into the geometric-attention first block.

## Headline results

- **esmGFP** — a de novo green fluorescent protein with **36% sequence identity to avGFP** and **58% sequence identity to its closest known fluorescent-protein neighbour (tagRFP)**. esmGFP folds and produces the chromophore. By comparing the identity gap to evolutionary distances between naturally occurring GFPs, the authors estimate esmGFP corresponds to **>500 million years of equivalent natural evolution** — the marketing line of the paper but supported by the phylogenetic argument in the supplement.
- **Atomic-coordination scaffolding.** When prompted with atomic positions of residues distant in sequence but close in space (e.g. metal-binding sites, catalytic triads), ESM-3 produces designs with **pTM > 0.8 and scTM ≈ 0.96 ± 0.04**, with success rate scaling cleanly with model size — the 98B model substantially outperforms 7B and 1.4B on the hardest motif-scaffolding prompts.
- **Multimodal prompting.** End-to-end design of a PETase-active-site scaffold using a combined prompt of (active-site structure + active-site amino acids + α/β-hydrolase function keyword) — a task that no single ESM-2-class or RFdiffusion-class model can solve in one shot.
- **Function-conditional generation.** Function-keyword conditioning lets ESM-3 generate sequences enriched for arbitrary InterPro annotations, providing a controllable design knob absent from sequence-only PLMs.

## Why it matters — versus ESM-2

ESM-2 was sequence-only and discriminative: you got embeddings, contact predictions, and (via ESMFold) structure prediction, but generation was awkward and structure was an output, not an input. ESM-3 changes three things at once:

1. **Multimodal in both directions** — structure and function are first-class inputs *and* outputs, so the same checkpoint does conditional design, inverse folding, structure prediction, and function annotation without separate heads.
2. **Order-of-magnitude scale** — 98B parameters and 10²⁴ FLOPs is roughly 60× the parameter count of ESM-2-15B and decisively in the regime where compute-optimal scaling laws for proteins start to look like those for language.
3. **Generative-native** — variable-rate masked pretraining means iterative decoding is the natural inference mode, so design pipelines (RFdiffusion-class hallucination loops, MCMC samplers, Proteina-Complexa-style flow models) can plug ESM-3 in as a generator rather than as a scoring oracle.

The downstream effect across ICLR 2026's protein-design track is large: ESM-3 (or ESM-C, its open-weights successor) is the default backbone for embedding-space MCMC (TEA alphabet), the default scoring oracle for binder hallucination, and the default starting point for any "design with function constraints" recipe.

## Known limitations

- **Licensing — load-bearing.** Only the **1.4B (ESM3-small-open)** checkpoint is publicly downloadable, and it sits under the **Cambrian Non-Commercial License** (an EvolutionaryScale custom license, not OSI-approved; the original ESM3 Community License was revised to remove the drug-development restriction and add a naming requirement, with "Derivative Work" extended to allow training on model outputs). The **7B and 98B checkpoints are gated** behind the EvolutionaryScale Forge API (authentication-token access) or AWS SageMaker commercial agreements — you cannot just download the 98B weights. Academic use of the open 1.4B model is permitted; commercial use of the larger frontier models requires a partnership. This is a material constraint for any downstream method that wants to claim "scales with frontier compute" — most public reproductions are bounded by the 1.4B checkpoint or by the more permissive ESM-C 300M / 600M follow-on.
- **"500 million years" framing is an estimate, not a measurement.** The number is derived from extrapolating natural-GFP phylogenetic distance to sequence identity; it is not a calibrated evolutionary timescale.
- **Binding prediction is uneven.** Subsequent third-party evaluations have reported that ESM-3's binding predictions can underperform simpler baselines on specific tasks — gaining structure tokens does not automatically improve every downstream readout (see Sgarbossa et al., "More Structures, Less Accuracy: ESM3's Binding Prediction Paradox", 2024).
- **Compute footprint.** Training at 98B / 10²⁴ FLOPs is not reproducible by academic labs; the open scientific record is therefore the technical report plus the 1.4B reference checkpoint, not a fully open frontier model.
- **Bias inherited from PDB / UniRef.** Structure tokens are trained on PDB, which is over-represented for soluble, well-folded, easy-to-crystallise proteins; membrane proteins, intrinsically disordered regions, and large complexes are under-represented and ESM-3's structure-track quality degrades there.

## Where it fits in the corpus

- **ICLR 2026 protein-design papers (this vault):** Proteina-Complexa (NVIDIA) uses ESM-class embeddings as inputs; TEA-alphabet (Pantolini & Durairaj) builds its 20-letter alphabet on ESM-class embeddings; GEM workshop binder pipelines use ESM-3 as a scoring oracle.
- **AACR 2026:** any oncology-target binder design demo on the AACR program is downstream of an ESM-class PLM — ESM-3 is the current frontier checkpoint.
- **NeurIPS 2026 MLSB / ICML 2026 GenBio:** expect ESM-C (the open-weights successor) to be the default backbone for the 2026 workshop submissions; ESM-3 remains the headline benchmark for "what frontier-scale buys you."

## Sources

- Hayes T. et al., "Simulating 500 million years of evolution with a language model," *Science* 387, eads0018 (2025) — [DOI](https://www.science.org/doi/10.1126/science.ads0018) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/39818825/)
- bioRxiv preprint: [10.1101/2024.07.01.600583v1](https://www.biorxiv.org/content/10.1101/2024.07.01.600583v1)
- EvolutionaryScale technical-report blog: [esm3-release](https://www.evolutionaryscale.ai/blog/esm3-release)
- Code / SDK: [github.com/evolutionaryscale/esm](https://github.com/evolutionaryscale/esm)
- Cambrian Non-Commercial License: [evolutionaryscale.ai/policies/cambrian-non-commercial-license-agreement](https://www.evolutionaryscale.ai/policies/cambrian-non-commercial-license-agreement)
- Cambrian Open License (covers ESM-C 300M and the codebase): [evolutionaryscale.ai/policies/cambrian-open-license-agreement](https://www.evolutionaryscale.ai/policies/cambrian-open-license-agreement)
- ESM-C successor blog: [esm-cambrian](https://www.evolutionaryscale.ai/blog/esm-cambrian)
- CZI Virtual Cells Platform listing: [virtualcellmodels.cziscience.com/model/esm3](https://virtualcellmodels.cziscience.com/model/esm3)
- Independent architecture write-up: Eric J. Ma, "Dissecting the ESM3 Model Architecture" (2024) — [link](https://ericmjl.github.io/blog/2024/8/25/dissecting-the-esm3-model-architecture/)
- Wikipedia summary of esmGFP: [en.wikipedia.org/wiki/EsmGFP](https://en.wikipedia.org/wiki/EsmGFP)
