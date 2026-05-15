# Callisto (expanded) — Volta Labs

**Volta Labs' Callisto automated library-prep platform expanded its capability set at AGBT 2026, with partnerships announced for Roche (Axelios SBX workflows) and Watchmaker Genomics (library-chemistry integration) — positioning Callisto as the upstream automation layer for the 2026 sequencer cohort.**

## At a glance

- **Vendor / launch date / availability:** Volta Labs; expansion announced at AGBT 2026 (Marco Island, Feb 22–25); shipping *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Chemistry / modality:** Automated library prep — digital-fluidics-based sample-to-library automation; AGBT 2026 expansion adds capability breadth and new partner-chemistry integrations *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)*.
- **Throughput (PR):** **TBD** — samples/run / libraries/day for the expanded Callisto configuration not enumerated in public AGBT 2026 coverage.
- **Read length:** n/a (Callisto outputs sequencer-ready libraries; read length is determined by the downstream sequencer).
- **Accuracy (PR):** **TBD** — no library-yield CV, no on-target / duplication-rate metrics in public AGBT 2026 coverage.
- **Partnerships announced at AGBT 2026:** **Roche** (Axelios SBX library workflow) and **Watchmaker Genomics** (library-chemistry integration) *per [GEN AGBT 2026 recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) and [AGBT 2026 program-notes](../program-notes.md)*.
- **List price / cost-per-sample:** **TBD** — no public list price surfaced in AGBT 2026 coverage.

> **Source caveat:** AGBT 2026 public coverage names the Roche and Watchmaker partnerships but does not break out the chemistry-integration details or pricing. Most quantitative fields are flagged **TBD**; **(vendor PR — no independent benchmark)** applies to all spec claims.

## What's new vs prior generation

Callisto is already shipping; AGBT 2026 is an *expansion* rather than a new-platform launch. Three vectors of new news:

1. **Roche partnership.** Roche's Axelios SBX chemistry (nanopore sequencing-by-expansion) requires a non-trivial template-expansion library-prep step before nanopore readout. Callisto integration positions Volta as the automation layer for Roche's first sequencer since 454. *See [Roche Axelios 1 dossier](roche-axelios-1.md).*
2. **Watchmaker Genomics partnership.** Watchmaker's library-prep chemistry (and its broader Bronze-sponsor presence at AGBT 2026) plugs into Callisto's automation deck, broadening the chemistry menu for Volta customers.
3. **Capability expansion.** Public coverage references "expanded capabilities" but does not enumerate the specific protocols or sample types added.

## Headline benchmarks

> **TBD** — no published benchmark cohort for the expanded Callisto configuration. The Roche / Watchmaker partnership announcements are partnership news rather than performance claims.

## Reception / competitive context

Library-prep automation is the *upstream* layer for every sequencing platform in the AGBT 2026 lineup. Whichever sequencers win shelf space (Roche Axelios, Element VITARI, Complete DNBSEQ-T7+, Ultima UG200, PacBio Revio, Oxford Nanopore PromethION), the libraries feeding them have to come from somewhere — currently a mix of manual prep, Beckman/Hamilton/Tecan liquid-handlers running off-the-shelf kits, and integrated solutions (Illumina DNA Prep, MGI MGISP, etc.). Callisto's competitive positioning is:

- **vs. generic liquid-handlers (Beckman, Hamilton, Tecan):** purpose-built for library prep, smaller footprint, simpler operator workflow.
- **vs. sequencer-integrated prep (Illumina DNA Prep, MGI MGISP):** platform-agnostic — same instrument feeds Roche, Element, Complete, PacBio, ONT workflows once partner integrations land.
- **vs. other purpose-built library-prep instruments:** the Roche + Watchmaker partnerships at AGBT 2026 are the strategic differentiator — being upstream of Roche's $150 genome is a meaningful moat.

## Cross-links

- **Upstream of every AGBT 2026 sequencer dossier** — Callisto feeds libraries into:
  - [Roche Axelios 1](roche-axelios-1.md) (Volta + Roche partnership).
  - [Element VITARI](element-vitari.md).
  - [Illumina Q70 duplex / TruPath](illumina-q70-duplex.md).
  - Ultima UG200, Complete DNBSEQ-T7+, PacBio Revio, ONT PromethION (dossiers TBD per [index](index.md)).
- **Partner: Watchmaker Genomics** — Bronze sponsor at AGBT 2026; library-prep chemistry partner *per [program-notes sponsors section](../program-notes.md)*.
- **Competitive: other automated library-prep instruments** — Illumina DNA Prep, MGI MGISP, Tecan/Hamilton/Beckman liquid-handler-based workflows.
- **Bioconductor downstream:** Callisto outputs sequencer-ready libraries — Bioconductor relevance is via the downstream sequencer's data path (e.g. [Rsamtools](https://bioconductor.org/packages/Rsamtools/), [VariantAnnotation](https://bioconductor.org/packages/VariantAnnotation/)), not directly through Callisto.

## Sources

- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) — Feb–Mar 2026 (Volta + Roche + Watchmaker partnerships indexed).
- [AGBT 2026 program-notes vendor index](../program-notes.md) — Volta Labs entry: "Callisto expansion + Roche / Watchmaker partnerships".
- [omicsomics AGBT 2026 preview](http://omicsomics.blogspot.com/2026/02/agbt-2026-preview.html) — pre-meeting context for the library / prep / enzyme cohort (NEB, Watchmaker, Volta, Canal, EpiCypher, MicroPure).

> **Open items:** locate primary Volta Labs and Roche/Watchmaker partnership press releases enumerating the specific Callisto modules added, the Axelios SBX automation workflow details, and any pricing changes. Backfill spec table and partnership-detail lines when primary sources are reachable.
