# GSVA Galaxy wrapper

**Gene Set Variation Analysis (GSVA) wrapped as a Galaxy tool** — a CoFest deliverable from GBCC2025 that takes one of the most-cited Bioconductor packages and packages it as a Galaxy tool, serving as the proof-of-concept for the auto-integration pipeline that automatically wraps Bioconductor packages for Galaxy.

- **Bioconductor source package:** [GSVA](https://bioconductor.org/packages/release/bioc/html/GSVA.html)
- **Galaxy wrapper PR:** see [github.com/galaxyproject/tools-iuc](https://github.com/galaxyproject/tools-iuc) (draft as of GBCC2025 CoFest)
- **Source (upstream):** [github.com/rcastelo/GSVA](https://github.com/rcastelo/GSVA)
- **Documentation / training:** [GSVA vignette](https://bioconductor.org/packages/release/bioc/vignettes/GSVA/inst/doc/GSVA.html); Galaxy tool docs TBD on merge
- **CoFest authors:** Fabio Cumbo, Jayadev Joshi, Bryan Raubenolt, Daniel Blankenberg (lead); on-site team Maria Doyle, Gretta Yagudayeva, Charlotte Soneson, Marcel Ramos Pérez; remote — Robert Castelo (GSVA maintainer, UPF)
- **Status at GBCC2025:** CoFest deliverable / proof-of-concept for the auto-wrap pipeline

## CoFest output at GBCC2025

- **Format:** GBCC2025 Community Fest (CoFest) deliverable, not a session talk
- **Day / session:** GBCC2025 CoFest, Jun 27-28, 2025 (post-conference, CSHL)
- **Title:** "GSVA Galaxy wrapper"
- **Slides / output:** PR on `galaxyproject/tools-iuc` (link to be added on merge)
- **Video:** not recorded
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

GSVA computes per-sample gene-set enrichment scores from an expression matrix — turning a genes-by-samples matrix into a gene-sets-by-samples matrix that downstream tools can treat as features. The Galaxy wrapper exposes this as a tool with the same arguments (method = `gsva` / `ssgsea` / `plage` / `zscore`, kernel choice, min/max set size) so a Galaxy user can run GSVA on a workflow output without writing R. The deeper goal is the auto-wrap pipeline behind it: GSVA is the visible test case demonstrating that the Bioconductor-to-Galaxy pipeline works end-to-end on a non-trivial package.

## How it works

**Core idea.** The Galaxy tool is a thin XML wrapper around the upstream `GSVA::gsva()` Bioconductor entry point. The wrapper declares the tool's parameters, points the Galaxy job runner at a Conda environment with R + Bioc + GSVA installed, runs an R driver script that loads the user's expression matrix and gene sets, and surfaces the resulting matrix as a Galaxy dataset.

**Inputs / outputs.** Input: an expression matrix (genes × samples, microarray or RNA-seq) and a gene-set collection (e.g. MSigDB GMT). Output: a gene-sets × samples score matrix that downstream Galaxy tools (clustering, differential analysis, survival modelling) treat as features.

**Key innovation.** GSVA performs a non-parametric coordinate-system change from genes to gene sets — preserving per-sample resolution while collapsing thousands of genes into hundreds of pathway scores, unsupervised and reference-free. As a Galaxy wrapper, the innovation is the auto-wrap pipeline: the initial wrapper was drafted by an LLM (Gemini) from the GSVA package's R-side metadata, then refined by humans — the CoFest deliverable proves the LLM-assisted bioc-to-galaxy path works on a real, widely-cited package.

**Parameters / API surface worth knowing.**
- `method` — one of `gsva`, `ssgsea`, `plage`, `zscore` (algorithm choice).
- `kernel` — controls the ranking approach for the non-parametric enrichment calculation.
- `min.sz` / `max.sz` — gene-set size filters (drop sets outside the range).
- Conda dependency — R + `bioconductor-gsva` pinned in the wrapper's `<requirements>` block.

**Canonical example.** From the GSVA vignette: load an `ExpressionSet` (e.g. a TCGA RNA-seq subset), pass MSigDB Hallmark gene sets, call `gsva(expr, gene_sets, method = "gsva")`, get a Hallmark-by-sample matrix. The Galaxy wrapper exposes exactly this call as a form: upload matrix, upload GMT, pick method, click run, download the score matrix.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo-tools (gene-set enrichment is a default feature-engineering step for any cancer-omics analysis)
- **bioc-to-galaxy** ([entry](bioc-to-galaxy.md)) — GSVA is the proof-of-concept test case; success here unblocks a long tail of Bioc packages
- **atena** ([entry](atena.md)) — also Castelo's package; the GSVA wrapper closes the loop with the package maintainer remotely
- **Workshop Platform** ([cross-vault](../../eurobioc-2025/tools/workshop-platform.md)) — wrapped tools are easier to slot into hands-on tutorial environments

## Notes

GSVA being one of the most-cited Bioconductor packages makes it a high-visibility test case — a successful wrap is broadly useful and gives the auto-pipeline an immediate poster child. Castelo's remote participation is the maintainer-loop closure: an auto-wrap that the upstream maintainer endorses is qualitatively different from one done over the maintainer's head.
