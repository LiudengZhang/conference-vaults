# signifinder

**Compute and explore public cancer transcriptional signatures** — a Bioconductor package containing 70+ curated tumor signatures from the literature and applying them as single-sample / single-cell / single-spot scores across bulk RNA-seq, microarray, single-cell, and spatial transcriptomics inputs.

- **Maintainer:** Stefania Pirrotta (University of Padua) — `stefania.pirrotta@phd.unipd.it`
- **Bioconductor:** [signifinder v1.13.0](https://bioconductor.org/packages/release/bioc/html/signifinder.html)
- **Source:** [github.com/CaluraLab/signifinder](https://github.com/CaluraLab/signifinder)
- **Vignettes:** [signifinder intro](https://bioconductor.org/packages/release/bioc/vignettes/signifinder/inst/doc/signifinder.html)
- **License:** AGPL-3
- **Status at GBCC2025:** methods talk on cross-modality cancer signature scoring

## Talk at GBCC2025

- **Speakers:** Stefania Pirrotta, Laura Masatti, et al. (Calura Lab, University of Padua)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "Public gene expression cancer signatures across bulk, single-cell and spatial transcriptomics data with signifinder Bioconductor package"
- **Slides (Zenodo DOI):** *TBD — Zenodo deposits typically 2–4 weeks post-conference*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

signifinder is a curation play: 70+ published cancer signatures (hypoxia, EMT, immune-infiltrate, stemness, and dozens of indication-specific scores) packaged with one consistent scoring API that runs across bulk RNA-seq, microarray, single-cell, and spatial inputs. Instead of every analyst re-implementing each signature from a paper's supplement, signifinder has them in one place with the same input contract — so a user can compute and compare a panel of signatures on the same object.

## How it works

**Core idea.** Each bundled signature is re-implemented in its original published form — some as weighted sums of gene-level coefficients (e.g. `Pyroptosis_Ye` uses per-gene weights in the −0.187 to 0.130 range), others as enrichment scores via `ssGSEA` or `GSVA`, depending on what the source paper specified. The scoring is per-sample (or per cell / per spot), so the same code path runs across modalities.

**Inputs / outputs.** Input is normalized RNA-seq counts or microarray data wrapped in a `SummarizedExperiment`, `SingleCellExperiment`, or `SpatialExperiment`; gene IDs can be symbols, Entrez, or Ensembl. Output is the same object with one column per signature appended to `colData`.

**Key innovation.** A single API spanning bulk, single-cell, and spatial — earlier signature collections targeted bulk only — plus an evaluation layer that reports the fraction of signature genes actually present in the dataset (e.g. "is using 100% of signature genes").

**Parameters worth knowing.**
- `inputType` — `"rnaseq"` or `"microarray"`, switches normalization assumptions.
- `nametype` — gene-ID convention used in the assay.
- `whichSign` / `tissue` / `tumor` / `topic` — filters in `multipleSign()` for computing a batch of signatures at once.
- `whichAssay` — which assay slot to score when the object holds multiple.

**Canonical example.** The vignette loads `ovse`, an ovarian-cancer bulk RNA-seq `SummarizedExperiment`, and calls `ferroptosisSign(dataset = ovse, inputType = "rnaseq")`. The returned object carries the ferroptosis score in `colData`, and the same object is then chained into further signature calls (e.g. `EMTSign`, `ImmunoScore_Hao`) so a panel of scores accumulates on one object. `availableSignatures()` and `evaluationSignPlot()` support browsing and QC.

## Where it fits in the corpus

- **AACR 2026:** axes single-cell-spatial-omics + clinical-trials — cancer signatures are clinically-actionable readouts and the cross-modality coverage matches the AACR spatial / single-cell dossiers
- **mitology** ([entry](mitology.md)) — same speaker (Pirrotta), Day 4; sister package on the same "transcriptome-interpretation" track
- **ISMB 2026:** scaffold
- **Nextflow Summit 2026:** not mentioned

## Notes

Pirrotta presents twice at GBCC2025 — signifinder on Day 2 and mitology on Day 4 — which signals the Calura lab is consolidating a "transcriptome interpretation" suite (signature scoring + pathway / organelle-specific scoring) rather than shipping one-off packages. The cross-modality angle (bulk + sc + spatial) is the key value-add over older signature collections that targeted bulk only.
