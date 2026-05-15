# EuroBioC 2025 — Tools

EuroBioC2025 ran 5 keynotes + ~25 short talks + 5 hands-on workshops + posters. Most short talks introduce or update a Bioconductor package — that's what this directory captures. Each entry below corresponds to **one package presented at EuroBioC2025**.

> **Status:** Template stub. We're proposing the per-tool format here for review before bulk extraction. Once locked, ~30 entries get populated from the talk + workshop list.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure:

````markdown
# <PackageName>

**One-line description** — what the package does in plain language.

- **Maintainer:** <name> (<institution>)
- **Bioconductor:** [package page]
- **Source:** [GitHub link]
- **Vignette:** [vignette link]
- **Status at EuroBioC2025:** new release / major update / methods talk / case study / workshop

## Talk at EuroBioC2025

- **Speaker:** ...
- **Day / session:** ...
- **Slides:** [Zenodo DOI]
- **Video:** [YouTube link if recorded]
- **Abstract / talk page:** [conf-site link]

## What it does

2–3 sentences: the problem it solves, key methodological idea, what it consumes/produces.

## Where it fits in the corpus

- AACR 2026: [link if mentioned]
- ISMB 2026: [link if mentioned]
- RECOMB 2026: [link if mentioned]
- Nextflow Summit 2026: [link if mentioned]
- GBCC 2025: [link if mentioned]

## Notes

Free-form impressions, benchmarks claimed, comparisons to alternatives.
````

## Tool index

23 entries covering EuroBioC2025 short talks + workshops, ordered by day and session. Three were drafted by hand to set the template (DESpace, DeeDeeExperiment, iSEE); the remaining 20 came from a single bulk pass after the format was validated. Slide DOIs are TBD — the Bioconductor community typically deposits to Zenodo within a few weeks of the meeting.

Skipped (not in this table): community / non-package talks (Laurah Ondari on Bioconductor training in Africa; Katharina F. Heil on ELIXIR resources), three short talks without a clear package anchor (Lucas Beerland — distributional inference single-cell proteomics; Jiayi Wang — ATAC-seq bias correction; Ilaria Billato — histopathological image integration). Six keynotes are deferred to a separate digest pass.

| Package | Domain | Speaker | Day | Slides | Video | Mentioned elsewhere |
|---|---|---|---|---|---|---|
| [notame](notame.md) | metabolomics | Vilhelm Suksi | Day 1 (AM) | TBD | not recorded | [Metabonaut](metabonaut.md) |
| [Metabonaut](metabonaut.md) | metabolomics (tutorial) | Philippine Louail | Day 1 (AM) | TBD | not recorded | [notame](notame.md), [SpectriPy](spectripy.md) |
| [omicsGMF](omicsgmf.md) | dim. reduction | Lieven Clement | Day 1 (AM) | TBD | not recorded | [msqrob2](msqrob2.md), [iSEE](isee.md) |
| [miaTime](miatime.md) | microbiome (time series) | Geraldson T. Muluh | Day 1 (AM) | TBD | not recorded | [mia](mia.md) |
| [SpectriPy](spectripy.md) | mass spec (cross-lang) | Johannes Rainer | Day 1 (AM) | TBD | not recorded | [Metabonaut](metabonaut.md) |
| [RCX](rcx.md) | networks | Florian Auer | Day 1 (AM) | TBD | not recorded | — |
| [scp-distributional](scp-distributional.md) | single-cell proteomics | Lucas Beerland | Day 1 (AM) | TBD | not recorded | [msqrob2](msqrob2.md), [omicsGMF](omicsgmf.md) |
| [MIRit](mirit.md) | miRNA-mRNA | Jacopo Ronchi | Day 1 (PM) | TBD | not recorded | [MOSClip](mosclip.md) |
| [DeeDeeExperiment](deedeeexperiment.md) | infra / data class | Najla Abassi | Day 1 (PM) | TBD | not recorded | [iSEE](isee.md) |
| [edgeR](edger.md) | RNA-seq DE | Lizhong Chen | Day 1 (PM) | TBD | not recorded | [DESpace](despace.md) |
| [MOSClip](mosclip.md) | multi-omics survival | Anna C E De Lima Tanada | Day 1 (PM) | TBD | not recorded | [MIRit](mirit.md) |
| [Rega](rega.md) | EGA submission | Igor Cervenka | Day 1 (PM) | TBD | not recorded | — |
| [footprintR](footprintr.md) | epigenomics | Charlotte Soneson | Day 2 (AM) | TBD | not recorded | — |
| [decemedip](decemedip.md) | methylation deconvolution | Ning Shen | Day 2 (AM) | TBD | not recorded | — |
| [atacseq-biascorrection](atacseq-biascorrection.md) | ATAC-seq bias correction | Jiayi Wang | Day 2 (AM) | TBD | not recorded | — |
| [SpatialData](spatialdata.md) | spatial omics (Python) | Luca Marconato | Day 2 (late AM) | TBD | not recorded | [OSTA](osta.md), [DESpace](despace.md) |
| [DESpace](despace.md) | spatial DE | Peiying Cai | Day 2 (late AM) | TBD | not recorded | [edgeR](edger.md), [spatialFDA](spatialfda.md) |
| [spatialFDA](spatialfda.md) | spatial multi-sample | Martin Emons | Day 2 (late AM) | TBD | not recorded | [DESpace](despace.md) |
| [consICA](consica.md) | ICA / signal decomp. | Maryna Chepeleva | Day 2 (late AM) | TBD | not recorded | [omicsGMF](omicsgmf.md) |
| [barbieQ](barbieq.md) | clonal tracking | Liyang Fei | Day 2 (late AM) | TBD | not recorded | — |
| [HistoImagePlot](histoimageplot.md) | histopath image integration | Ilaria Billato | Day 2 (late AM) | TBD | not recorded | [OSTA](osta.md) |
| [OSTA](osta.md) | spatial omics (book) | Dong & Patrick | Day 2 (workshop) | TBD | not recorded | [DESpace](despace.md), [SpatialData](spatialdata.md) |
| [mia](mia.md) | microbiome | Tuomas Borman | Day 2 (workshop) | TBD | not recorded | [miaTime](miatime.md) |
| [msqrob2](msqrob2.md) | proteomics | Christophe Vanderaa | Day 2 (workshop) | TBD | not recorded | [omicsGMF](omicsgmf.md) |
| [Workshop Platform](workshop-platform.md) | infrastructure | Alexandru Mahmoud | Day 2 (workshop) | TBD | not recorded | [iSEE](isee.md) |
| [iSEE](isee.md) | visualization | Federico Marini | Day 2 (workshop) | TBD | not recorded | [DeeDeeExperiment](deedeeexperiment.md) |

## Why this format

- **Cross-vault links matter** — this is the only place where "tool released here, used in cancer-research talk X, benchmarked in methods paper Y" can be one click apart
- **Slides + video + vignette + Bioconductor page** in one place — none of the other vaults have this complete quartet
- **Domain field** lets the table slice by single-cell / spatial / etc. without duplicating into topic pages
- **Status field** tells a reader at a glance whether they're looking at a v1.0 announcement or a 4-year-old package's annual update

## Open questions for the pilot

1. **Granularity** — ✅ locked: one page per tool
2. **AACR dossier mirroring** — ✅ locked: full entry in both vaults, cross-linked (no canonical/stub asymmetry)
3. **Sample tools to draft first** — ✅ done: DESpace / DeeDeeExperiment / iSEE drafted; the DDE ↔ iSEE pair exercises the cross-vault link mechanic
4. **Edge case: non-Bioconductor tools** — *open*: SpatialData (Marconato Day 2 talk) is Python-primary with R interop in development. The current template assumes a Bioconductor package page. Need a variant for cross-language or pre-release tools — proposed: a "Status: external / pre-release" badge that swaps the Bioconductor field for "(Python-primary; R interop layer in development)" plus a link to the upstream framework
