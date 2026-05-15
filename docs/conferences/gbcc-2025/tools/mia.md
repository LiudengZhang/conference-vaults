# mia

GBCC2025 workshop / oral pair on the Bioconductor microbiome ecosystem. See [EuroBioC 2025 entry](../../eurobioc-2025/tools/mia.md) for the same package's parallel coverage at the European event.

**Microbiome Analysis with Bioconductor** — a `TreeSummarizedExperiment`-based framework for microbiome data, providing diversity, ordination, differential abundance, and community-ecology analyses on a single canonical S4 container. The substrate for the OMA (Orchestrating Microbiome Analysis) book and the mia* family of helper packages.

- **Maintainer:** Tuomas Borman (University of Turku) — `tuomas.vesa.borman@utu.fi`
- **Authors include:** Felix G.M. Ernst, Tuomas Borman, Leo Lahti (PI), and broader microbiome community
- **Bioconductor:** [mia v1.20.0](https://bioconductor.org/packages/release/bioc/html/mia.html)
- **Source:** [github.com/microbiome/mia](https://github.com/microbiome/mia)
- **Companion book:** [Orchestrating Microbiome Analysis (OMA)](https://microbiome.github.io/OMA/)
- **License:** Artistic-2.0
- **Status at GBCC2025:** mature package; workshop + Oral Session 5 talk

## Workshop + talk at GBCC2025

- **Workshop presenter:** Tuomas Borman (University of Turku)
- **Workshop session:** Day 3 — afternoon workshop slot (2-3:30 PM)
- **Workshop title:** "Orchestrating Microbiome Analysis with Bioconductor"
- **Oral speaker:** Leo Lahti (University of Turku)
- **Oral session:** Day 4 — Oral Session 5
- **Format:** hands-on workshop drawing on the OMA book; companion oral talk on ecosystem direction
- **Slides / materials:** *to verify after publish — typically a per-event GitHub repo under [github.com/microbiome](https://github.com/microbiome)*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

mia gives microbiome data a `TreeSummarizedExperiment` home — abundances, taxonomy, phylogenetic tree, and per-sample metadata in one S4 object — and supplies the standard analysis vocabulary (alpha/beta diversity, ordination, agglomeration to taxonomic ranks, differential abundance via several backends, transformation utilities). The mia* family extends this with time-series (miaTime), visualization (miaViz), simulation (miaSim), and Shiny GUIs (iSEEtree). The OMA book is the curated walkthrough.

## How it works

**Core idea.** mia treats the microbiome as a single `TreeSummarizedExperiment` object that keeps abundance assays, taxonomy `rowData` (Kingdom → Species), phylogeny in `rowTree`, and sample metadata in `colData` synchronized — so subsetting and analysis propagate through every layer at once.

**Inputs / outputs.** Inputs are imported from BIOM files, QIIME2 output, DADA2 objects, or phyloseq objects via the mia importers. Outputs include alpha- and beta-diversity values (Shannon, Simpson, JSD, UniFrac, …), agglomerated assays at a chosen taxonomic rank, transformed assays (log, rarefaction), differential-abundance results, and tidy data frames for downstream plotting.

**Key innovation.** A single S4 container that unifies microbiome operations — abundance, taxonomy, and phylogeny stay aligned under the standard SummarizedExperiment idioms — which makes mia the substrate for the OMA book and the broader mia* family (miaTime, miaViz, miaSim, iSEEtree).

**Parameters worth knowing.**
- `agglomerateByRank()` — collapse features to a taxonomic rank (e.g. `rank = "Family"`).
- `addAlpha()` — compute and attach alpha-diversity indices (`index = "shannon"`, etc.) to `colData`.
- `transformAssay()` — apply a transformation (log, relative abundance, CLR, …) and store it as a new assay.
- `rarefyAssay()` — equalize sequencing depth across samples.

**Canonical example.** The vignette loads the bundled `GlobalPatterns` dataset and agglomerates 19,216 OTUs down to 341 families, then attaches Shannon diversity in one step:
```r
data(GlobalPatterns, package = "mia")
tse <- agglomerateByRank(GlobalPatterns, rank = "Family")
tse <- addAlpha(tse, index = "shannon")
```

## Where it fits in the corpus

- **AACR 2026:** axes = bioinfo-tools (microbiome–cancer interfaces appear in immune-microenvironment and cancer-prevention dossiers)
- **miaTime** ([entry](../../eurobioc-2025/tools/miatime.md)) — same UTU group; longitudinal extension built on mia's containers
- **Bioc-to-Galaxy** ([entry](bioc-to-galaxy.md)) — Borman is core to both the microbiome ecosystem AND the Galaxy-bridge CoFest; mia is a flagship candidate for auto-integration
- **EuroBioC 2025 mia entry** ([entry](../../eurobioc-2025/tools/mia.md)) — the European twin
- **Nextflow Summit 2026:** not mentioned

## Notes

The GBCC angle on mia emphasizes Galaxy / cross-platform integration — the joint Galaxy-Bioconductor framing of the event makes "how do non-R users get at this" a first-class question. The EuroBioC version was Bioc-internal (S4 design, OMA book curation, mia* family extensions); GBCC is the cross-ecosystem export. Both tracks share the same package and team — the framing is what differs.
