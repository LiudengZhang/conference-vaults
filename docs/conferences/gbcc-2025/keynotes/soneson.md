# Charlotte Soneson — "From classes to community — How Bioconductor has advanced my research"

**Affiliation:** Friedrich Miescher Institute for Biomedical Research (FMI), Basel
**Day / session:** Day 3 (Wed Jun 25, 2025) — Keynote 2, Grace Auditorium (9:00–10:00)
**Talk title:** "From classes to community — How Bioconductor has advanced my research"
**Slides (Zenodo DOI):** *to verify after publish — Bioconductor speakers typically deposit within ~2 weeks of the meeting*
**Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
**Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## Thesis

A career-arc keynote, not a tool launch. The "classes to community" framing reads as an argument that Bioconductor's S4 data classes (`SummarizedExperiment`, `SingleCellExperiment`, and the spatial / tidy descendants) are not just engineering convenience — they are the *substrate* on which a community of methods authors can compose work without re-litigating data shape every time. Soneson is well placed to make the argument concretely, drawing on a decade-plus of method development that has compounded precisely because everyone agreed on the container.

## Speaker context

Soneson is one of Bioconductor's most prolific maintainers and reviewers. Her published / maintained software spans single-cell quantification benchmarking, differential expression methodology (with edgeR-adjacent contributions), [iSEE](https://bioconductor.org/packages/iSEE) (the interactive SummarizedExperiment explorer, with Federico Marini and Aaron Lun), and most recently [footprintR](https://bioconductor.org/packages/footprintR) for footprinting / single-molecule data. She is also a member of the GBCC CoFest team that wrapped GSVA into Galaxy. The Day-3 keynote slot is a deliberate signal: invite the maintainer-of-many-things to articulate why the *ecosystem* shape, not any single package, is what advances research.

## Connections to the corpus

- [footprintR ↗ EuroBioC2025](../../eurobioc-2025/tools/footprintr.md) — Soneson presented footprintR at EuroBioC2025; the GBCC keynote sits earlier in the calendar but in the same arc
- [iSEE ↗ EuroBioC2025](../../eurobioc-2025/tools/isee.md) — Soneson is a co-author; iSEE is a canonical "S4-class-as-substrate" example
- [GSVA → Galaxy](../tools/gsva-galaxy.md) — Soneson is on the GBCC CoFest team that produced this wrapper; the keynote and the CoFest artifact share authorship
- Cross-link to [Vince Carey's EuroBioC2025 opening keynote](../../eurobioc-2025/keynotes/carey.md) — both are "ecosystem, not packages" arguments, paired naturally as the 2025 Bioconductor keynote diptych
- AACR axis: **bioinfo-tools** — ecosystem-level rather than single-tool

## Open questions

- How much of the talk is autobiographical (specific projects: iSEE, footprintR, benchmarking work) vs. abstract argument about classes and community? Career-arc keynotes can go either way.
- Does Soneson take a position on the Python/scverse boundary — i.e., does "community" stop at R/Bioconductor, or does it extend to interop with `AnnData` / `SpatialData`? Relevant given the GSVA→Galaxy CoFest crosses an even larger boundary.
- Any concrete asks — funding, recognition, citation practice for software authors — or strictly retrospective? The slot accommodates either.
