# Day 4 — Thursday Jun 26, 2025

The closing day is short — one keynote, one oral session, lunch, departure — but it's where several through-lines of the meeting land. Jason Williams (CSHL) gives the morning training-and-equity keynote on home turf; Scott Cain chairs the eight-talk Oral Session 5, which is a deliberate mix of the Bioconductor (plyxp, mia/miaverse, mitology) and Galaxy (FAIR-EASE, Galaxy-E, credential handling, database reliability) sides under a single roof. The post-conference CoFest then runs separately on Friday and Saturday at the Sandra and Edward Meyer building.

## Morning

[Jason Williams (Cold Spring Harbor Laboratory)](../keynotes/williams.md) closed the keynote arc with *Conquest of Abundance: Genomics in a Time of Plenty* — a training / equity / access talk rather than a tool launch, complementing the Day 3 community session under Mike Love's chairing. Williams runs CSHL's training operation, so this is essentially the host-institution closing remarks for a meeting CSHL hosted.

Oral Session 5 (10:30–12:00, chaired by Scott Cain) ran eight talks across both ecosystems. [plyxp](../tools/plyxp.md) (Justin Landis, Michael Love) opened — *reimagining dplyr syntax for SummarizedExperiment objects* — the canonical "tidyverse-for-Bioc" artifact of the meeting, paired with Mangiola's [Tidyomics](../tools/tidyomics.md) talk on Day 3. Tuomas Borman / Leo Lahti followed with the oral version of *Orchestrating Microbiome Analysis with Bioconductor* — the [mia](../tools/mia.md) / miaverse update, pairing the workshop the day before with a 12-minute talk that emphasizes new functionality. Stephen Salerno presented *Inference with predicted data* — the methodological complement to his Day 2 workshop on AI-predicted-outcomes inference (likely the IPD R package, though the package name is not in the title). John Davis on simple and secure credential handling in Galaxy. Marie Jossé / Jérôme Detoc / Erwan Bodéré on [FAIR-EASE](../tools/fair-ease.md) — two years of bridging Earth-system science to Galaxy. [mitology](../tools/mitology.md) (Stefania Pirrotta, Massimo Bonora, Enrica Calura) — dissecting mitochondrial activity from transcriptome data — completes the Pirrotta double-bill ([signifinder](../tools/signifinder.md) on Day 2). Coline Royaux / Marie Jossé on Galaxy-E, the ecology-oriented Galaxy initiative (a 2025 update). John Davis returned to close — *Little errors at big scale* — on data efficiency, consistency, and reliability in the Galaxy database.

## Afternoon

12:00–1:00 lunch and departure. No afternoon program.

The post-conference CoFest ran Friday Jun 27 – Saturday Jun 28 at the Sandra and Edward Meyer building (separate registration). The headline deliverable was [GSVA→Galaxy](../tools/gsva-galaxy.md) — the Bioconductor GSVA package wrapped as a Galaxy tool with an open PR — produced by Fabio Cumbo, Jayadev Joshi, Bryan Raubenolt, and Daniel Blankenberg, with on-site contributions from Maria Doyle, Gretta Yagudayeva, Charlotte Soneson, and Marcel Ramos Pérez (and remote support from Robert Castelo). This is the artifact that connects the Day 2 [bioc-to-galaxy](../tools/bioc-to-galaxy.md) auto-wrapping pipeline talk and the Day 3 Blankenberg workshop into a concrete shipped wrapper.

## What to chase

- The Salerno *inference with predicted data* talk and his Day 2 workshop together — confirm whether the underlying R package is `ipd`, an IPD-derivative, or a new artifact; this is a methods axis that AACR / RECOMB methods circuits also touch and worth a cross-vault link.
- The two John Davis talks (credential handling + database reliability) bookend the session and are infrastructure work that doesn't get its own tool page, but together they describe the operational state of the Galaxy backend in mid-2025.
- The CoFest output beyond [GSVA→Galaxy](../tools/gsva-galaxy.md) — the Bioconductor blog recap mentions a future maintainer field in Galaxy tool XML and embedded Shiny apps as in-progress directions; track whether either ships before EuroBioC 2025 in September.
