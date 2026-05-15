# splicelogic

**Translate differential-transcript-usage (DTU) results into interpretable exon-level splice events** — a Bioconductor package from the Love lab that takes DTU output (transcript-level effect sizes between conditions) and recasts the per-transcript signal as concrete pairwise splice events (cassette exon, alt-5'/3' SS, intron retention, etc.) so an analyst can see *what splicing change* drives the DTU call rather than just *which transcripts shifted*.

- **Maintainer:** Beatriz Campillo Miñano (Love lab, UNC-Chapel Hill) — `beatrizcampillo29@gmail.com`
- **Bioconductor:** [splicelogic](https://bioconductor.org/packages/release/bioc/html/splicelogic.html) (submitted Mar 2026, released in subsequent Bioc cycle)
- **Source:** [github.com/thelovelab/splicelogic](https://github.com/thelovelab/splicelogic)
- **Vignette:** [splicelogic vignette](https://bioconductor.org/packages/release/bioc/vignettes/splicelogic/inst/doc/splicelogic.html)
- **License:** MIT + file LICENSE
- **Status at GBCC2025:** preview talk (the package was submitted to Bioconductor in March 2026; the June 2025 talk was a prototype demo of the DTU-to-splice-event interpretation)

## Talk at GBCC2025

- **Speakers:** Beatriz Campillo Miñano, Michael Love (UNC-Chapel Hill)
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2B, Grace Auditorium (chair: Vincent Carey)
- **Talk title:** "Visualizing and analyzing differential transcript usage"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

splicelogic takes the output of a DTU analysis (e.g. from DRIMSeq, fishpond, or another transcript-level test) and resolves the transcript-level effect into pairwise exon-level comparisons. For each pair of transcripts that shift in relative abundance, it classifies the structural difference as a discrete splicing event class (cassette exon, alt-5' SS, alt-3' SS, intron retention, mutually exclusive exons, alt-first/last exon) and produces visualizations that make the underlying splice change inspectable. The aim is to bridge the gap between "transcript X went up while transcript Y went down" and "exon E is being included more often in condition A".

## How it works

**Core idea.** Rather than operate on splice junctions, splicelogic works on whole transcript structures — each transcript and all its exons carry the DTU effect estimate forward, and pairwise up-vs-down transcript comparisons are decomposed into the discrete splicing event that distinguishes them.

**Inputs / outputs.** Input is a `TxDb` object (transcript annotation) plus a DTU result table with a per-transcript effect-size column. Output is a per-event table classifying each detected change as skipped exon, included exon, mutually exclusive exons, retained intron, or alternative splice site, stored as `GRanges` objects.

**Key innovation.** Method-agnostic upstream coupling: splicelogic accepts transcript-level effect estimates from any DTU tester — DRIMSeq, DEXSeq, satuRn, edgeR-diffSplice — so the interpretation layer is decoupled from the statistical-testing layer. Preserving full isoform context (rather than junction-level evidence) keeps the event call grounded in the annotated transcript model.

**Parameters / API surface worth knowing.**
- `prepare_exons(txdb, dtu_table, coef_col)` — joins exon annotation to DTU results; `coef_col` names the effect-size column.
- `preprocess()` — prepares exons for event detection.
- `find_se()` — detects skipped exons specifically.
- `find_all_events()` — runs the full event-classification sweep.

**Canonical example.** From the README workflow: load a `TxDb`, run DRIMSeq (or another DTU tester), pass its coefficient table through `prepare_exons()` → `preprocess()` → `find_all_events()` to get a per-event classification table tying each annotated transcript-pair shift to a specific splicing event class.

## Where it fits in the corpus

- **AACR 2026:** axis = bioinfo / AI methods; DTU interpretation matters for any cancer-splicing dossier (oncogene isoform switching, neoantigen-from-cryptic-splice work)
- **EuroBioC 2025:** no direct counterpart on splicing interpretation
- **fishpond / DRIMSeq:** the upstream DTU testers — splicelogic consumes their output rather than replacing them
- **ISMB 2026:** scaffold; splicing methods overlap likely
- **Nextflow Summit 2026:** not mentioned

## Notes

The package was submitted to Bioconductor in March 2026, so the GBCC2025 talk was effectively a preview of work-in-progress. The release timeline matters for citation accuracy: if a user references the package from GBCC slides, point them at the github repo (`thelovelab/splicelogic`) rather than the not-yet-existing Bioconductor URL for the talk date. Campillo joined the Love lab as a BCB PhD candidate in June 2025; this was an early-PhD presentation.
