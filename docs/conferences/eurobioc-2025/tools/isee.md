# iSEE

**Interactive SummarizedExperiment Explorer** — a Shiny-based GUI for exploring `SummarizedExperiment` / `SingleCellExperiment` data, with linked panels, code tracking (every plot exports its R code), and S4 extensibility for custom panel types.

- **Maintainer:** Kevin Rue-Albrecht (Oxford / WIMM) — `kevinrue67@gmail.com`
- **Authors include:** Federico Marini (IMBEI Mainz), Charlotte Soneson, Aaron Lun
- **Bioconductor:** [iSEE v2.24.0](https://bioconductor.org/packages/release/bioc/html/iSEE.html)
- **Source:** [github.com/iSEE/iSEE](https://github.com/iSEE/iSEE)
- **Vignettes:** [User's Guide](https://bioconductor.org/packages/release/bioc/vignettes/iSEE/inst/doc/basic.html) · [Linking panels](https://bioconductor.org/packages/release/bioc/vignettes/iSEE/inst/doc/links.html) · [Configuring](https://bioconductor.org/packages/release/bioc/vignettes/iSEE/inst/doc/configure.html) · [Custom panels](https://bioconductor.org/packages/release/bioc/vignettes/iSEE/inst/doc/custom.html) · [Big data](https://bioconductor.org/packages/release/bioc/vignettes/iSEE/inst/doc/bigdata.html)
- **License:** MIT
- **Status at EuroBioC2025:** mature package (since 2018, v2.24.0); 90-min hands-on workshop

## Workshop at EuroBioC2025

- **Presenter:** Federico Marini (IMBEI Mainz)
- **Day / session:** Day 2 (Thu Sep 18, 2025) — afternoon hands-on workshop session (parallel with OSTA, microbiome, msqrob2, Workshop Platform)
- **Format:** hands-on tutorial; attendees follow vignettes in their own R session, often via the Bioconductor Workshop Platform Docker image
- **Workshop materials:** *to verify — typically a per-event GitHub repo under [github.com/iSEE](https://github.com/iSEE)*
- **Video:** workshops not recorded; the Bioconductor YouTube playlist covers plenaries only

## What it does

iSEE turns a `SummarizedExperiment` into a live, multi-panel Shiny app where each panel (reduced-dimension plot, heatmap, gene-feature plot, sample table, …) can be linked: clicking a cell on a UMAP filters the gene heatmap, etc. Every panel exports the underlying R code that produced its current state, so an exploration session converts cleanly to a reproducible script. Custom panel types are added via S4, which is how iSEE has grown an extension ecosystem (iSEEde, iSEEpathways, iSEEtree, …).

## How it works

**Core idea.** iSEE wraps a `SummarizedExperiment` / `SingleCellExperiment` in a Shiny app composed of typed, S4-defined panels; panels publish selections (sending) and subscribe to selections from other panels (receiving), so the app behaves as a reactive graph over a single data object.

**Inputs / outputs.** Input is any `SummarizedExperiment` derivative. Outputs are (a) the live Shiny session and (b) the exact R code that reproduces every panel's current state, retrievable via the "Extract the R code" modal — making interactive exploration convertible to a script.

**Key innovation.** Panel-to-panel selection transmission plus the S4 extension API: third-party packages (iSEEde, iSEEpathways, iSEEtree) plug new panel classes into the same linking graph without forking the core app.

**Parameters / API surface worth knowing.**
- `iSEE(se, initial = list(...))` — top-level launcher; `initial` is a list of `Panel` objects describing the starting layout.
- Built-in panel classes: `ReducedDimensionPlot`, `FeatureAssayPlot`, `ColumnDataPlot`, `RowDataTable`, `ComplexHeatmapPlot`, `ColumnDataTable`, `RowDataPlot`, `SampleAssayPlot`.
- Selection sources — each panel exposes "Selection parameters" naming a transmitting panel; ordering matters because senders must execute before receivers in the exported script.
- Custom panels — quick path via `createCustomPlot()` / `createCustomTable()`; full S4 path subclasses `Panel` / `ColumnDotPlot` / `RowDotPlot` (documented in the iSEE book, not the basic vignette).

**Canonical example.** The minimal invocation is `iSEE(sce)`; from there the user picks panels from the UI. The "Examine panel chart" view renders the send/receive graph so linking can be inspected, and the code-extraction modal returns the syntax-highlighted R block that regenerates every plot.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; iSEE is a tool researchers *use* to explore single-cell results, so it could appear as a runtime component in any AACR talk that ships an SCE
- **DeeDeeExperiment** ([entry](deedeeexperiment.md)) — natural data source; DDE's DEA/FEA slots are exactly the kind of result an iSEE custom panel could surface
- **ISMB 2026:** scaffold
- **GBCC 2025:** queued — iSEE is a regular workshop fixture
- **Nextflow Summit 2026:** not mentioned (different ecosystem)

## Notes

The canonical interactive-viz citizen of the Bioconductor world — at every recent BioC and EuroBioC event. The 2025 workshop almost certainly emphasized the extension API (`registerCustomPanel()` / S4-defined panels), which is the path that lets a new package author (e.g. someone shipping DeeDeeExperiment) get a polished UI without writing Shiny from scratch.
