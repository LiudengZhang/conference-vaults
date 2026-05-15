# Vince Carey — "A coherent ecosystem for genomic data science: 25 years of Bioconductor"

**Affiliation:** Harvard Medical School / Channing Division of Network Medicine, Brigham and Women's Hospital
**Day / session:** Day 1 (Wed Sep 17, 2025) — opening keynote
**Talk title:** "A coherent ecosystem for genomic data science: 25 years of Bioconductor"
**Slides (Zenodo DOI):** *to verify after publish — Bioconductor speakers typically deposit within ~2 weeks of the meeting*
**Video:** [Bioconductor YouTube — plenaries playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7) (keynotes recorded)
**Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## Thesis

A retrospective + prospective on Bioconductor as an *ecosystem* — not just a package repository, but a coherent set of S4 classes (`SummarizedExperiment`, `SingleCellExperiment`, `SpatialExperiment`), release discipline, and review culture that has held together across 25 years of changing assays. The argument is almost certainly that the coherence — shared data structures, semiannual releases, mandatory vignettes — is what compounded into the present-day ecosystem, and that the same discipline is what will absorb the next wave (cloud-native, foundation-model integrations, multimodal single-cell-spatial).

## Speaker context

Vince Carey is one of the original Bioconductor co-founders (with Robert Gentleman et al., 2001) and has been on the project's core team continuously since. His Channing Division work centers on statistical genomics, cloud-scale genomic data access (`restfulSE`, `BiocFileCache`, `AnVIL`-adjacent tooling), and integrative methods for asthma / respiratory disease cohorts. He is a co-author on *Orchestrating Spatially Resolved Transcriptomics Analysis with Bioconductor* (OSTA), which makes him a natural anchor for the keynote — both backwards-looking (25 years) and forward (spatial / multimodal). Inviting him to open the European leg of the conference frames the meeting as ecosystem-stewardship rather than topical methods.

## Connections to the corpus

- [OSTA](../tools/osta.md) — Carey is a co-author; the book is a present-tense exemplar of the "coherent ecosystem" thesis applied to spatial omics
- [Workshop Platform](../tools/workshop-platform.md) — the runtime / Docker side of the same coherence argument (every Bioconductor release ships a reproducible compute substrate)
- [SpatialData](../tools/spatialdata.md), [SingleCellExperiment-shaped tools](../tools/index.md) — the S4 class lineage Carey would be reflecting on
- AACR axis: bioinfo-tools (ecosystem-level rather than single-tool)

## Open questions

- How explicitly does Carey address the *non*-R parts of the ecosystem (Python / scverse interop, Zarr-backed `SpatialData`)? The 25-year framing could either be insular or actively bridge-building — the recording will tell.
- Any forward-looking commitments on cloud-native infrastructure (AnVIL, Terra, BiocFileCache at scale) vs. AI-driven analysis (foundation models trained on `SummarizedExperiment`-shaped data)?
- Concrete metrics — package count, download trajectory, contributor geography — vs. narrative-only framing? Carey tends toward the quantitative.
