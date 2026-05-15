# Cell2Location

**Family:** spatial
**Modality:** Spot-resolution spatial transcriptomics (Visium, ST), paired with a scRNA-seq reference
**Released:** 2022 (Nature Biotechnology)
**License:** Apache-2.0
**Code/checkpoint:** [github.com/BayraktarLab/cell2location](https://github.com/BayraktarLab/cell2location) (fitted per dataset; no pretrained weights)
**Also surfaced in:** single-cell-spatial-omics

> Cell2Location is a Bayesian spatial-transcriptomics deconvolution
> method from the Bayraktar Lab at the Sanger Institute that maps
> fine-grained cell types onto Visium / ST spots by integrating a
> single-cell reference with the spatial counts. It first estimates
> reference cell-type expression signatures from annotated scRNA-seq,
> then fits a hierarchical Negative Binomial model per dataset to
> infer the absolute abundance of each cell type at each spot while
> accounting for technical effects. It is a probabilistic model
> rather than a foundation model: there is no pretrained checkpoint —
> users fit it on their own scRNA-seq + spatial pair.

## Architecture & training

Cell2Location is a hierarchical Bayesian Negative Binomial model
implemented in PyTorch / Pyro on top of the scvi-tools framework. It
factorises the observed spot count matrix into per-cell-type
reference signatures (estimated separately from annotated scRNA-seq
via a regression NB model) multiplied by latent per-spot cell-type
abundances, with explicit nuisance terms for slide-level batch
effects, ambient/contaminating RNA, and gene- and location-specific
overdispersion. Inference is done with stochastic variational
inference; informative gamma priors on per-spot total cell count and
per-cell-type abundance provide the regularisation that lets the
model resolve dozens of cell types per spot. There is no pretraining
or shared checkpoint — the model is fit from scratch on each
scRNA-seq + spatial pair, with GPU runtimes of minutes-to-hours per
slide.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

**Posters mentioning Cell2Location (n=3):**

- **1442** — *Spatial transcriptomics informed tumor purity estimation from histology slides for triple negative breast cancer*
  …en TNBC patients using SCANVI. The integrated single-cell data were mapped onto in-house Visium sections with Cell2Location to estimate spot-level tumor cell-type proportions, serving as supervisory labels. A deep learning model (VID…
- **4952** — *Spatial Transcriptomics reveals core resistance niches distinguishing non-MPR from MPR in NSCLC after neoadjuvant chemoimmunotherapy*
  …9;MPR 70-90%). We compared global programs (DEG, GSEA/Reactome, cell&#8209;cycle), inferred cell composition (cell2location), analyzed context&#8209;specific ligand-receptor and metabolic states, and spatially mapped resistance axes…
- **773** — *Single-cell and spatial transcriptomic profiling reveal fibrosis-related tumor states in lung squamous cell carcinoma associated with idiopathic pulmonary fibrosis*
  …v3.8.0). Cellular trajectories were analyzed using scTour (v1.0.0). Spatial deconvolution was performed using Cell2location (v0.9.6), with validation in an external fibrosing ILD spatial dataset. Results: To infer lineage relationshi…

**Sessions mentioning Cell2Location (n=0):**

_No session transcripts in the AACR 2026 corpus mention this tool._

<!-- mentions:end -->

## What's missing / where evidence is weak

- **No comparison against alternative deconvolution methods.** All three posters (1442 TNBC tumor purity, 4952 NSCLC neoadjuvant chemoimmunotherapy resistance niches, 773 lung squamous cell carcinoma fibrosis) use Cell2Location as the chosen tool without benchmarking against RCTD, Tangram, CARD, or stereoscope. There is no AACR 2026 evidence for which spot-resolution deconvolver is preferable for which tissue.
- **No discussion of compute or runtime.** Cell2Location's per-dataset variational fitting can take hours on GPU; none of the posters report runtime, slide count, or convergence diagnostics.
- **Reference-scRNA-seq dependence is unexamined.** The fidelity of Cell2Location output is bounded by the quality and cell-type coverage of the matched single-cell reference, but corpus posters describe their references in passing rather than as a controlled variable.
- **Zero session mentions.** Despite being a workhorse spatial-transcriptomics tool, Cell2Location does not surface in any of the 12 bioinfo-tools session transcripts.

## Takeaway

Cell2Location is the quiet utility of AACR 2026's spatial-transcriptomics work — three posters use it as the primary deconvolution step in real analyses (TNBC tumor-cell proportions as supervisory labels, NSCLC resistance-niche composition, IPF-associated lung-cancer cell-state mapping) and treat the choice as routine. Unlike the pathology and single-cell foundation models in this index, Cell2Location is not being evaluated, benchmarked, or compared; it is simply being *used*. The corpus thus reinforces its status as the default Bayesian deconvolver for Visium/ST data, while highlighting that the community is no longer asking whether to use it but only what to do with its output.

## FM comparison & 2026 status

**Where it sits in the FM landscape.** Cell2Location is the one entry in this dossier set that is **not a foundation model** — it is a hierarchical Bayesian Negative Binomial deconvolver implemented on Pyro / scvi-tools, refit per dataset with no pretrained weights. Its "peers" are therefore other spot-resolution deconvolution methods (RCTD, Tangram, CARD, stereoscope, DestVI) rather than scFMs. Conceptually it occupies the niche newer scFMs are now trying to colonize: scGPT-spatial (Feb 2025) and CellPLM both target the same deconvolution / imputation task with pretrained transformer backbones, threatening Cell2Location's incumbent status by promising zero-shot transfer instead of per-dataset variational fitting.

**Direct peers.**

| Method | Architecture | Reference / training | Public weights | Headline benchmark |
| --- | --- | --- | --- | --- |
| Cell2Location | Bayesian hierarchical NB, Pyro/scvi-tools | Per-dataset fit from scRNA-seq + ST | Apache-2.0, no shared checkpoint | Top RMSE/JSD on heterogeneous Visium (Li et al. 2023 + ATAC generalization 2025) |
| RCTD | NMF-style regression with platform effects | Per-dataset fit | MIT, GitHub | Co-top performer on AUPR/JSD; preferred for sparse ST |
| Tangram | Optimal-transport mapping of scRNA-seq onto spatial | Per-dataset fit | MIT, GitHub | Strong on heterogeneous tissue, sensitive to reference quality |
| CARD | Conditional Autoregressive spatial decomposition | Per-dataset fit | MIT, GitHub | Top method in 2023 Nat Commun benchmark for spatially smooth signal |
| scGPT-spatial | MoE-decoder transformer FM, continual-pretrained | 30M spatial profiles (SpatialHuman30M) | MIT, GitHub | Zero-shot deconvolution + imputation, outperforms baselines (bioRxiv 2025) |

**What changed in 2025-2026.** Cell2Location itself has been incrementally maintained — recent point releases tracked scvi-tools 1.1.x compatibility, added a SpaceJam model for Nanostring CosMx data, introduced memory-efficient posterior quantification, and extended the amortising neural network architecture. The license remains Apache-2.0 and there is no pretrained checkpoint to release. The bigger 2025-2026 story is *competitive*: an Oxford Bioinformatics 2025 benchmark on spatial ATAC-seq showed Cell2Location and RCTD jointly dominating chromatin-modality deconvolution, generalizing the 2023 Li et al. *Nature Communications* finding to a new data type. Simultaneously, scGPT-spatial's bioRxiv release in Feb 2025 directly threatens Cell2Location's monopoly on Visium / ST deconvolution by offering a pretrained alternative that does not require per-dataset variational fitting. No retraction or concern has been issued.

**AACR-relevant use cases.** The corpus uses Cell2Location in exactly the role its design supports: (1) **Generating supervisory labels for downstream ML** — poster 1441 (TNBC tumor purity from histology) uses Cell2Location-derived spot-level tumor-cell proportions on Visium as the ground-truth labels for training a deep learning model on matched H&E, the cleanest "Cell2Location as upstream annotator" pattern; (2) **Compositional analysis in immuno-oncology** — poster 4952 (NSCLC neoadjuvant chemoimmunotherapy resistance niches) uses cell2location to infer composition before running ligand-receptor and metabolic analyses on MPR-vs-non-MPR samples; (3) **Cross-cohort cell-state mapping** — poster 773 (lung squamous fibrosis) pins Cell2Location v0.9.6 in a multi-tool spatial pipeline alongside scTour. The corpus contains zero head-to-head Cell2Location-vs-RCTD-vs-scGPT-spatial benchmarks; the deconvolver choice is invisible-by-convention. No AACR 2026 session transcript mentions Cell2Location, despite three spatial-transcriptomics-themed sessions on April 20-21 — the workflow is too downstream to surface in plenary talks.
