# Helena Crowell — "Colorectal cancer through the lens of whole transcriptome imaging"

**Affiliation:** Charité — Universitätsmedizin Berlin; scverse community core developer
**Day / session:** Day 1 (Wed Sep 17, 2025) — morning keynote 2
**Talk title:** "Colorectal cancer through the lens of whole transcriptome imaging"
**Slides:** [Zenodo 10.5281/zenodo.17189967](https://zenodo.org/records/17189967)
**Video:** [Bioconductor YouTube — plenaries playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQS_qvtLJNdDqHL6z5jj5y_7) (keynotes recorded)
**Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## Thesis

Whole-transcriptome imaging platforms (Xenium 5K-plex, MERSCOPE, Stereo-seq, etc.) collapse the long-standing trade-off between gene-panel breadth and subcellular spatial resolution — and colorectal cancer, with its well-mapped niches (tumor epithelium, stromal CAFs, T-cell exclusion zones, mucinous regions), is a productive testbed for what changes when you can ask transcriptome-scale questions *in situ*. The talk almost certainly argues that the bottleneck has shifted from acquisition to analysis tooling that can handle multi-million-cell, multi-modal objects coherently.

## Speaker context

Helena Crowell is a core developer in the scverse / SpatialData community and a methodological voice on differential-state and compositional analysis in single-cell data (`muscat` co-author, several CyTOF / scRNA-seq method papers). Her appointment at Charité Berlin places her at one of Europe's larger spatial-omics groups. She is an author on the SpatialData framework, which is the Python/Zarr substrate now being mirrored by Bioconductor's `SpatialExperiment` / `SpatialData`-R. Inviting her gives the EuroBioC audience a direct line into the scverse interop conversation — which is exactly the bridge Carey's opening keynote is likely setting up.

## Connections to the corpus

- [SpatialData](../tools/spatialdata.md) — Crowell is a co-author of the underlying framework; her talk is the applied motivation
- [OSTA](../tools/osta.md) — the Bioconductor book that codifies the analysis patterns she would be deploying
- [DESpace](../tools/despace.md) — differential-spatial-pattern testing across CRC niches is exactly DESpace's DSP mode
- [spatialFDA](../tools/spatialfda.md) — functional-data approaches to spatial heterogeneity, complementary to image-based whole-transcriptome readouts
- AACR axis: single-cell-spatial-omics — this is the canonical EuroBioC contribution to that axis

## Open questions

- Which platform(s) — Xenium 5K, MERSCOPE, Stereo-seq, Visium HD — and at what scale (cells, samples, patients)? CRC studies range from single-block proof-of-concept to atlas-scale cohorts.
- Does the analysis stack run in Python (SpatialData / squidpy) or R (SpatialExperiment / OSTA), and are the niches called from segmentation-first or transcriptome-first clustering?
- New methodological contribution vs. application paper? The title hints at biology-forward; the EuroBioC audience would want to know which packages were touched.
