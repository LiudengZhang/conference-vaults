# Day 2 — Thursday Sep 18, 2025

Day 2 was the spatial-omics day, the AI-protein-design day, and — by design — the hands-on day. Two keynotes (Sharpe in the morning, Ferruz in the early afternoon) bracketed a short-talk block dominated by spatial methods, and the afternoon dissolved into five parallel workshops covering OSTA, microbiome (mia), proteomics (msqrob2), the Workshop Platform itself, and iSEE. It was the densest day of the meeting and the one most likely to translate into adopted tooling for attendees' next projects.

## Morning

James Sharpe opened with [C3PO: Cell 3D Positioning by Optical encoding](../keynotes/sharpe.md). The talk title implies a hardware + computational pipeline for 3D spatial encoding of cells; this sits adjacent to (but methodologically distinct from) the imaging-based spatial transcriptomics that anchored Day 1's Crowell keynote and would dominate the morning's short talks.

The first short-talk block was epigenomics-leaning. [footprintR](../tools/footprintr.md) (Charlotte Soneson) — TF-footprinting from ATAC / DNase data, with Soneson's usual emphasis on careful benchmarking. [decemedip](../tools/decemedip.md) (Ning Shen) — methylation-based cell-type deconvolution, a problem space where Bioconductor has historically been thin.

The late-morning block pivoted hard into spatial. [SpatialData](../tools/spatialdata.md) (Luca Marconato) is the most consequential entry: a Python-primary framework for spatial-omics data that the Bioconductor side is now actively building an R interop layer against. [DESpace](../tools/despace.md) (Peiying Cai) tackles spatially variable / spatially DE genes on top of edgeR's NB framework — a direct bridge between the spatial talk track and Day 1's edgeR update. [spatialFDA](../tools/spatialfda.md) (Martin Emons) extends spatial inference to the multi-sample regime, which is where the field is heading clinically. [consICA](../tools/consica.md) (Maryna Chepeleva) brought independent-component analysis into the dimensionality-reduction conversation, complementary to omicsGMF from Day 1. [barbieQ](../tools/barbieq.md) (Liyang Fei) covered clonal barcode tracking — a niche but high-leverage tool for lineage-tracing experiments.

## Afternoon

Noelia Ferruz's [Controllable protein design with language models](../keynotes/ferruz.md) was the meeting's main brush with the AI-for-biology zeitgeist. The talk title emphasizes *controllable* — i.e., conditional generation rather than free generation — which is the active frontier in protein LMs.

The 14:45 workshop block was the meeting's most concretely useful afternoon: five parallel hands-on sessions. [OSTA](../tools/osta.md) (Stephanie Hicks et al., delivered by Dong & Patrick) — the orchestrating-spatial-transcriptomics-analysis book made workshop. [mia](../tools/mia.md) (Tuomas Borman) — microbiome data analysis, the umbrella framework miaTime extends. [msqrob2](../tools/msqrob2.md) (Christophe Vanderaa) — robust statistical proteomics from the Clement group, complementary to omicsGMF from Day 1. [Workshop Platform](../tools/workshop-platform.md) (Alexandru Mahmoud) — the meta-infrastructure underneath every other workshop in the room, which would echo into Serizay's Day 3 keynote on community-driven flexible software. [iSEE](../tools/isee.md) (Federico Marini) — the visualization workhorse; pairs naturally with DeeDeeExperiment from Day 1.

## Posters & social

The 16:30 poster session was the second and final poster block — the last shot at face-to-face cross-pollination before the more formal Day 3 close.

## What to chase

- Marconato's SpatialData slides — confirm the current state of the R interop layer (the tools index notes it's still in development).
- Ferruz's slides — which controllable-design objectives were demoed, and on what protein families.
- Workshop Platform GitHub — Mahmoud's repo is a likely Day 3 callback when Serizay closes; useful to read in advance.
