# Day 1 — Wednesday Sep 17, 2025

Day 1 set the tone for the whole meeting: a community looking back on 25 years of Bioconductor while pushing forward into spatial transcriptomics, statistical modeling of heterogeneity, and a long parade of metabolomics / proteomics / multi-omics packages. Two keynotes bookended the day's short-talk blocks — Vince Carey opened with a retrospective + roadmap, and Susan Holmes anchored the afternoon with a methodological argument for latent-variable thinking as the right response to biological heterogeneity. In between came a remarkably dense sequence of short talks — by the end of the day the audience had been introduced to a dozen new or substantially updated R packages.

## Morning

Vince Carey opened the conference with [25 years of Bioconductor](../keynotes/carey.md) — a retrospective on the project's coherent-ecosystem ethos and the data structures (SummarizedExperiment, ExperimentHub, AnnotationHub) that made interoperability tractable. The talk title positions Bioconductor explicitly as an ecosystem, not a package collection — a frame the rest of the meeting would return to.

Helena Crowell followed immediately with [Colorectal cancer through whole-transcriptome imaging](../keynotes/crowell.md), which previewed the spatial-omics thread that would dominate Day 2. The pairing — community retrospective then a working spatial-CRC case — was deliberate.

The morning short-talk block leaned heavily metabolomics + mass spec. [notame](../tools/notame.md) (Vilhelm Suksi) and [Metabonaut](../tools/metabonaut.md) (Philippine Louail) presented a coordinated metabolomics workflow / tutorial pair. [SpectriPy](../tools/spectripy.md) (Johannes Rainer) put the cross-language interop story on stage early — R↔Python mass-spec data exchange as a first-class concern, not an afterthought. Proteomics-adjacent, [omicsGMF](../tools/omicsgmf.md) (Lieven Clement) introduced a generalized matrix-factorization approach to dimensionality reduction; the talk title suggests it's positioned as a single method usable across single-cell and proteomics. Microbiome time-series got a slot with [miaTime](../tools/miatime.md) (Geraldson T. Muluh), extending the mia framework to longitudinal designs. Networks were represented by [RCX](../tools/rcx.md) (Florian Auer) — Cytoscape exchange format support in R.

## Afternoon

Susan Holmes' [Latent variables as the best medicine for heterogeneity](../keynotes/holmes.md) provided the day's methodological centerpiece. The title argues a methodological position — when biology is heterogeneous, the right move is to model latent structure rather than to pre-stratify or average it away. The talk likely connected forward to several afternoon short talks; in particular, the omicsGMF and (Day 2) consICA contributions are squarely in this lineage.

The afternoon short talks ran broader. [MIRit](../tools/mirit.md) (Jacopo Ronchi) covered miRNA–mRNA integration. [DeeDeeExperiment](../tools/deedeeexperiment.md) (Najla Abassi) introduced a new infrastructure / data class — one of the few infra talks of the day, and worth pairing with the iSEE workshop on Day 2. [edgeR](../tools/edger.md) (Lizhong Chen) was the lone classical-RNA-seq DE update, a reminder that the workhorse tools still get major-version work. [MOSClip](../tools/mosclip.md) (Anna C E De Lima Tanada) addressed multi-omics survival analysis, complementary to MIRit. [Rega](../tools/rega.md) (Igor Cervenka) covered EGA submission tooling — the unglamorous but essential plumbing of a regulated data-sharing workflow.

A few talks in the afternoon are not yet captured as tools (Justine Leclerc on conformeR, Koen Van den Berge on transfactor, Katharina Heil on ELIXIR community resources) and remain to verify against the recordings.

## Posters & social

The 16:30 poster session was the first of two — by tradition this is where the next year's short-talk pipeline is sourced. Conference dinner at 20:00 closed Day 1.

## What to chase

- Vince Carey's slides — confirm whether the "25 years" framing was retrospective only or included a forward roadmap.
- Susan Holmes' slides on Zenodo — exact methodological argument and which datasets she used to motivate the latent-variable framing.
- The three afternoon talks deferred from the tools index (conformeR, transfactor, ELIXIR) — recordings may justify adding a fourth category to the corpus.
