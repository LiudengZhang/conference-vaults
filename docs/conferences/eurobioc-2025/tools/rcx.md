# RCX (RCX2 update)

**Cytoscape Exchange (CX) format for R** — creates, validates, visualizes, and converts biological networks in the Cytoscape CX format to standard R graph objects (igraph, graphNEL). The EuroBioC2025 talk covered the package's v2 (RCX2) updates.

- **Maintainer:** Florian Auer (University of Augsburg) — `florian.auer@informatik.uni-augsburg.de`
- **Bioconductor:** [RCX v1.16.0](https://bioconductor.org/packages/release/bioc/html/RCX.html)
- **Source:** [git.bioconductor.org/packages/RCX](https://git.bioconductor.org/packages/RCX)
- **Vignettes:** [RCX implementing the Cytoscape Exchange format](https://bioconductor.org/packages/release/bioc/vignettes/RCX/inst/doc/RCX_an_R_package_implementing_the_Cytoscape_Exchange_format.html)
- **License:** MIT
- **Status at EuroBioC2025:** methods talk on the v2 update (talk title referenced as "RCX2")

## Talk at EuroBioC2025

- **Speaker:** Florian Auer (University of Augsburg)
- **Day / session:** Day 1 (Wed Sep 17, 2025) — morning short-talk session, after the Crowell keynote
- **Talk title:** "RCX2 package for biological network exchange formats"
- **Slides (Zenodo DOI):** *to verify after publish*
- **Video:** not recorded
- **Abstract / schedule:** [eurobioc2025 schedule](https://eurobioc2025.bioconductor.org/pages/schedule.html)

## What it does

RCX is the canonical R reader/writer for the Cytoscape Exchange (CX) network format used by NDEx and Cytoscape itself. It validates network structure, round-trips to igraph/graphNEL for downstream analysis, and provides a visualization layer. The "RCX2" talk title points to a v2 upgrade — the released Bioconductor package is named `RCX` (currently v1.16.0); the v2 changes likely shipped under the same package name.

## How it works

**Core idea.** The CX format is a JSON document split into aspect-modules (nodes, edges, nodeAttributes, edgeAttributes, networkAttributes, cartesianLayout, cyVisualProperties, metaData), each with its own schema and cross-references by integer IDs. RCX mirrors that as an R `RCX` object whose slots are aspects, and validates referential integrity (every edge's source/target must resolve to a node ID, attribute aspects reference valid node/edge IDs, etc.) on import.

**Inputs / outputs.** Input: a CX JSON file (from NDEx, Cytoscape, or another producer). Output: an `RCX` R object; round-trippable to `igraph` via `toIgraph()` and to Bioconductor's `graphNEL` for downstream graph algorithms; serializable back to CX with `writeCX()`.

**Key innovation.** Native R support for the full aspect model — including Cytoscape visual properties and metaData — so a CX file edited in R is still a valid CX file when opened in Cytoscape or pushed to NDEx. Earlier R network packages strip presentation when converting to igraph; RCX preserves it.

**Parameters worth knowing.** `readCX(file)` for full-file read; the lower-level `readJSON` / `parseJSON` / `processCX` triple for incremental parsing when a CX file has deprecated or unknown aspects. `toIgraph(rcx)` for graph-library export. `$metaData` accessor to inventory which aspects an object actually carries.

**Canonical example.** Vignette walks through the bundled "Imatinib-Inhibition-of-BCR-ABL" pathway (an NDEx network): load with `readCX()`, inspect aspects with `summary()` and `$metaData`, modify node or edge attributes, then write back with `writeCX()` for re-upload to NDEx.

## Where it fits in the corpus

- **AACR 2026:** no current dossier; relevant axis is bioinfo / AI methods (network-based analyses, gene-regulatory inference)
- **GBCC 2025:** queued
- **Nextflow Summit 2026:** not mentioned

## Notes

Naming oddity: talk announced as "RCX2" but the released Bioconductor package is `RCX`. Verify after slides land whether RCX2 was a project nickname for the v2 update or a separate fork.
