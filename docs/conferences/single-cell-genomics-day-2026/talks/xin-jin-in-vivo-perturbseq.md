# Xin Jin (keynote ★) — in vivo Perturb-seq, from a pilot screen to a whole-brain genome-scale CRISPR screen

**Speaker:** **Xin Jin**, Scripps Research (confirmed via [SCGD26 speaker list](https://satijalab.org/scgd26/))
**Talk title (official):** "Towards a functional brain genome"
**Bio (as introduced):** grad student finishing in **Cory Bargmann's** lab (Rockefeller) → **Harvard Junior Fellow** → co-developed in vivo Perturb-seq with **Feng Zhang** and **Paola Arlotta** (first prototype: [Jin et al., *Science* 2020](https://www.science.org/doi/10.1126/science.aaz6063)). Co-founder of **PerturbAI**.
**Slot:** SCGD26, Jun 12, 2026 (11:00–11:40 AM EDT)
**Recording:** SCGD26 livestream (YouTube) — verify archived link
**Status:** Captured from session transcript

## Thesis

Human genetics has handed neuroscience a long list of large-effect, **haploinsufficient (loss-of-function)** risk genes for autism / neurodevelopmental disorders / schizophrenia — far more than can be studied one gene at a time. The answer is to scale **functional genomics directly in the mammalian brain** at single-cell resolution: in vivo Perturb-seq pairs pooled CRISPR perturbation (delivered in utero) with single-cell read-out postnatally, with built-in internal controls that regress out animal-level and library-prep confounds.

## Methods & technical advances

- **AAV-CH9 for fast embryonic expression.** Lentivirus was the in vivo bottleneck. A repurposed-screen across 86 barcoded AAV serotypes (collaboration, UC Irvine) found **AAV-CH9** (originally a Schaffer-lab DNA-shuffling variant from UC Berkeley) expresses fast and early enough for corticogenesis — ~10× less work than the 2020 approach, more cells recovered.
- **Single-nucleus multiomic guide capture.** Moving from single-cell to single-**nucleus** (for ATAC + RNA multiome, adult tissue) broke guide-RNA recovery; ~2 years of optimization (student "Xinhe"). Fix: barcoded, polyadenylated guide transcript + **MS2 or PP7 RNA-hairpin** capture by a nuclear-anchored binding-protein fusion — both anchoring vectors improved gRNA assignment ~3.8× vs. non-anchoring, without significantly compromising editing. Preprint: [*In vivo multiomic Perturb-seq with enhanced nuclear gRNA capture*, bioRxiv 2026](https://www.biorxiv.org/content/10.64898/2026.03.15.711739v1) (vector deposited to Addgene — specific plasmid ID not confirmed, see below).
- **Whole-brain genome-scale screen.** With Broad / Allen / "Ox" / **Pertrip AI** collaborators (leads incl. "Tuo," **Maria Kushchenova**, **Soo Young Kim**): **1,947 disease-associated genes**, **8,588 sgRNAs**, **>7.7M cells** after QC (per-hemisphere/mouse/litter barcoding). Preprint: [*Genome-scale functional mapping of the mammalian whole brain with in vivo Perturb-seq*, bioRxiv 2026](https://www.biorxiv.org/content/10.64898/2026.03.16.711480v1) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13108593/)). Atlas openly on Hugging Face: [**perturbai/wholebrain_crispr_atlas**](https://huggingface.co/datasets/perturbai/wholebrain_crispr_atlas) (CC-BY-4.0), also released via PerturbAI + the NVIDIA AI Blueprint for single-cell analysis. MOI/cell-number titration keeps ≈1 guide/cell; CRISPR knockout (not CRISPRi) often yields in-frame deletions → nonfunctional protein even when transcript is detectable.

## Key results

- **Pilot (Fox g1 / Foxg1):** (cortical-development pilot screen — [Jin et al., *Cell* 2024](https://www.cell.com/cell/fulltext/S0092-8674(24)00476-8)) two independent guides give highly correlated log-fold-change → two-allele LoF support. In **layer-6 corticothalamic neurons**, knockout de-represses a transcription-factor network (ectopic Bcl11b, Rorb, etc.) → failed fate maintenance / hybrid fate — and this is **layer-6-specific** (layer-5 IT neurons, same lineage, respond completely differently). Bulk would have missed it.
- **Whole-brain:** ~20–30% of perturbation×subtype pairs have a significant effect. Top-vulnerable programs are **proteostasis/proteasome** (post-mitotic neurons can't dilute proteotoxic stress), RNA splicing, epigenetic regulation. The four top PSMC hits are physically interacting 26S proteasome components — biochemical partners rediscovered genetically.
- **GRIN2A vs GRIN2B vignette:** Grin2b perturbs more cell types (cortical + subcortical; severe/early NDD) than Grin2a (cortical, milder/later schizophrenia) — consistent with clinical onset. "Phenocopy" sharing with clathrin-mediated endocytosis genes; some "**phen-opposite**" cell types where Grin2a and Grin2b drive *opposite* DE.
- **Perturb-Clear** (postdoc "Boli"): tissue clearing + light-sheet + sparse perturbation → manual reconstruction of dendritic cytoarchitecture + long-range connectivity, paired with Perturb-seq. ADNP knockout → basal-branch-specific complexity loss in layer-4 (not oblique/tuft, not layer-2/3), with concordant large DE only in layer-4. Morphology + RNA are **concordant overall** and more interpretable jointly.

## Q&A highlights

- **"Sequencing cost is no longer the blocker."** The next bottleneck is *which* cell-type × perturbation combinations to sample — the space is **sparse** (some cell types matter far more), so the move is computation-guided iterative sampling of high-effect-size genes, not brute force.
- On polygenic disease: start with large-effect de novo (haploinsufficient) variants because CRISPR knockout models them well; polygenic effects may still **converge** on a smaller set of conserved large-effect nodes (cites Jonathan Pritchard).

## Connections to the corpus

- [Aviv Regev — virtual cell / lab-in-the-loop](aviv-regev-virtual-cell.md) (in vivo Perturb-seq for ASD genes; convergence onto few programs) and [Alex — VIP Perturb-seq](alex-vip-perturbseq.md) (scalable Flex-based perturb screens).
- AACR axis: [virtual-cells](../../aacr-2026/topics/virtual-cells/), [single-cell-spatial-omics](../../aacr-2026/topics/single-cell-spatial-omics/).

## Sources

- SCGD26 speaker list (confirms Xin Jin, Scripps Research; title "Towards a functional brain genome"): https://satijalab.org/scgd26/
- Jin et al., *Science* 2020 (first in vivo Perturb-seq / ASD genes): https://www.science.org/doi/10.1126/science.aaz6063
- Jin et al., *Cell* 2024 (massively parallel in vivo Perturb-seq, cortical development pilot): https://www.cell.com/cell/fulltext/S0092-8674(24)00476-8
- Whole-brain atlas preprint, bioRxiv 2026: https://www.biorxiv.org/content/10.64898/2026.03.16.711480v1 — https://pmc.ncbi.nlm.nih.gov/articles/PMC13108593/
- Whole-brain CRISPR atlas on Hugging Face: https://huggingface.co/datasets/perturbai/wholebrain_crispr_atlas
- Nuclear guide-capture (MS2/PP7) preprint, bioRxiv 2026: https://www.biorxiv.org/content/10.64898/2026.03.15.711739v1

## Still unverified

- Exact lab-member name spellings ("Xinhe," "Tuo," "Maria Kushchenova," "Soo Young Kim," postdoc "Boli"): not confirmed against an authoritative author list (bioRxiv full-text returned 403; searched Google Scholar/bioRxiv abstracts, names not individually verified).
- Specific **Addgene plasmid ID** for the nuclear guide-capture/anchoring vector: searched Addgene + the preprint listing; candidate Multiome Perturb-seq sgRNA vectors exist (e.g., pEM040) but could not be confirmed as the exact deposit from this preprint.
