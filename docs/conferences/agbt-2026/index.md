# AGBT 2026

Per-launch dossiers and program notes from the **Advances in Genome Biology and Technology General Meeting** (Marco Island, FL, **February 22–25, 2026**) — the sequencing-platform and spatial-genomics showcase of the year.

> **Status:** Concluded. Build-out is queued from public coverage. AGBT runs under a **closed-ish abstract policy** (concurrent-session abstracts are visible to attendees but not posted publicly), so this vault uses a **JPM-style "one degree removed" build**: every claim is sourced to a vendor press release, GenomeWeb post, Bio-IT World story, C&EN recap, or substack/blog summary. No primary transcripts.

## Why this is in the vault

AGBT is upstream of every downstream tool dossier across the vault:

- **AACR 2026 posters** that report Visium HD, Xenium, CosMx, or MERSCOPE data are running on platforms that were either *first announced* or *roadmap-updated* at AGBT.
- **[EuroBioC 2025](../eurobioc-2025/index.md) Bioconductor packages** ([SpatialExperiment](../eurobioc-2025/tools/spatialdata.md), SpatialFeatureExperiment, DESpace) consume output from these instruments — their relevance scales with whichever platform wins shelf space at AGBT.
- **[GBCC 2025](../gbcc-2025/index.md) tools** (Voyager, spatialLIBD, SOSTA) likewise depend on the spatial-platform output formats announced here.
- **Long-read methods** (PacBio HiFi/Revio, ONT PromethION) feed into structural-variant and haplotype-resolved assembly tracks at every downstream meeting.

So while AGBT itself isn't a Bioconductor or pharma-deal conference, its launches set the substrate for everything else.

## Start here

- **[Per-launch dossiers](launches/index.md)** — one page per vendor announcement: chemistry, throughput, accuracy, cost-per-Gb, availability, headline benchmarks, competitive context.
- **[Program notes](program-notes.md)** — confirmed sessions, organizing committee, vendor PR index, post-event recap aggregator, cross-vault links.

## At a glance (top platform headlines)

| Vendor | Launch | Headline number | Availability | Source |
|---|---|---|---|---|
| Roche | **Axelios 1** sequencer | **$150 30× human genome (duplex)**; instrument $750k | Pre-order post-AGBT; formal launch summer 2026 | [GenomeWeb](https://www.genomeweb.com/sequencing/promising-150-genome-roche-reveals-more-details-axelios-sequencer-agbt) |
| Element Biosciences | **VITARI** benchtop sequencer | **$100 genome**, 10B reads/run, 3 TB output, $689k list | Pre-orders open; ships H2 2026 | [Element PR](https://www.elementbiosciences.com/news/element-biosciences-introduces-vitari-redefining-what-high-throughput-sequencing-makes-possible) |
| Ultima Genomics | **UG200 / UG200 Ultra** | Q60 ppmSeq duplex; 162 Tb/wk (UG200 Ultra); $850k / $1.25M | At AGBT | [Vilella substack](https://albertvilella.substack.com/p/illumina-announcements-and-ultima) |
| Complete Genomics (→ Swiss Rockets) | **DNBSEQ-T7+** | **48B reads/24h**, Q40, $100 genome, $800k US list | Shipping in US/Canada now | [Complete Genomics PR](https://www.completegenomics.com/complete-genomics-highlights-dnbseq-t7-at-agbt-2026-expanding-high-throughput-sequencing-capability/) |
| Illumina | **TruPath** synthetic-long-read + Q70 duplex roadmap | $395 / genome on TruPath; Q70 duplex kits H2 2026 early access | Mixed (TruPath shipping; Q70 EA H2 2026) | [Vilella substack](https://albertvilella.substack.com/p/illumina-announcements-and-ultima) |
| PacBio | **CiFi** (long-read 3C) + SPRQ-Hq + SMRT cell reuse | Chromosome-scale assemblies from a single SMRT cell | Shipping (CiFi); SMRT reuse early access | [PacBio PR](https://www.pacb.com/press_releases/pacbio-and-uc-davis-researchers-introduce-cifi-a-new-long-read-3c-method-that-enables-chromosome-scale-assemblies-from-a-single-smrt-cell/) |
| Oxford Nanopore | PromethION cfDNA/cfRNA + Q38 duplex talks | Joint cfDNA+cfRNA nanopore multiomic cancer monitoring | Roadmap | [ONT AGBT page](https://nanoporetech.com/about/events/conferences/agbt-2026) |
| Singular Genomics | **G4X Spatial Sequencer** (official release) | 500-plex RNA + 18-plex protein + H&E equivalent, ~$100s/sample | Officially released week of AGBT | [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) |
| 10x Genomics | Xenium **RNA+Protein** multiomics; **Atera** spatial preview | Xenium: 28-plex protein + 500-plex RNA, FFPE-compatible | Xenium RNA+Protein mid-2026; Atera formal launch at AACR (April) | [GenomeWeb](https://www.genomeweb.com/business-news/agbt-showcases-diversity-spatial-genomics-technologies) |
| Bruker Spatial Biology | **CellScape** spatial proteomics + **PaintScape** 3D + CosMx mouse WT | CosMx mouse whole-transcriptome + 64 proteins | Roadmap updates | [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) |
| Stellaromics | **Pyxa** (first 3D spatial imager) | 3D spatial imaging — AGBT debut | Newcomer launch | [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) |
| Vizgen | **MERSCOPE Ultra** + MERFISH 2.0 + proteomics | Expanded panels, organoid support | Roadmap | [GEN recap](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/) |

> All numbers above are **vendor PR figures, not validated benchmarks**. Reagent costs exclude library prep, instrument depreciation, and labor in most cases. See per-launch pages for source citations and caveats.

## Program shape

AGBT 2026 ran four days at Marco Island with the customary structure:

- **Plenary sessions** (mornings) — invited speakers in Genomics / AI in Genomics / Genetics & Technology / Evolutionary Genomics tracks.
- **Concurrent sessions** (Tue/Wed evenings) — abstract-selected talks across Cancer, Computational Biology, Technology, and Biology tracks. Abstracts visible to attendees only.
- **Sponsor workshops** — Illumina (Gold), Ultima/Bruker Spatial/Roche (Silver), plus nine Bronze workshops.
- **Poster sessions** — closed (no public abstract book).

See [program notes](program-notes.md) for the confirmed plenary speaker list and organizing-committee co-chairs.

## Source aggregators

Front pages and post-event recaps that index AGBT 2026 coverage:

- [C&EN — Genomics, multiomics, and spatial biology at AGBT 2026](https://cen.acs.org/analytical-chemistry/sequencing/agbt-2026-dna-sequencing-multiomics-spatial/104/web/2026/03)
- [GEN — AGBT 2026 Recap: NGS Big Bets and Spatial's Rising Momentum](https://www.genengnews.com/topics/omics/agbt-2026-recap-ngs-big-bets-and-spatials-rising-momentum/)
- [GenomeWeb — AGBT Sequencing Tech Updates (Battle Royale)](https://www.genomeweb.com/sequencing/agbt-sequencing-tech-updates-portend-battle-royale-high-throughput-clinical-applications) *(paywall — headlines accessible)*
- [GenomeWeb — Spatial Omics roadmaps at AGBT](https://www.genomeweb.com/sequencing/spatial-omics-single-cell-companies-provide-updates-roadmaps-agbt)
- [Albert Vilella — Illumina + Ultima (Part 1)](https://albertvilella.substack.com/p/illumina-announcements-and-ultima)
- [Albert Vilella — Roche Axelios (Part 2)](https://albertvilella.substack.com/p/roche-unveils-the-150-genome-with)
- [Omics! Omics! — AGBT 2026 Preview](http://omicsomics.blogspot.com/2026/02/agbt-2026-preview.html)
- [Omics! Omics! — Axelios run pricing analysis](https://omicsomics.blogspot.com/2026/03/roche-axelios1-run-pricing-not-knockout.html)
- Twitter/Bluesky `#AGBT26` — real-time photo/quote firehose from attendees; not archived.

## Caveats

- AGBT abstracts are **closed-ish** (visible to attendees but not posted to a public abstract server like AACR). Every claim in this vault is reconstructed from third-party coverage and vendor PR.
- **Vendor specs are routinely PR-distorted.** Cost-per-genome numbers assume best-case duplex/reagent-only pricing and exclude library prep, instrument amortization, labor, and reanalysis. Treat them as ceiling claims.
- **Date/venue note:** the *agbt.org* agenda page as fetched lists Orlando, Feb 23–26 — this conflicts with the dates/venue confirmed by the build brief and by [10times](https://10times.com/agbt-meeting) and historical record (Marco Island has been the canonical AGBT venue). Flagged on [program notes](program-notes.md) for resolution.
- Roche's **Axelios 1** was announced *the day after* AGBT closed (Feb 26 press release) but its tech reveal happened at the meeting — treated as an AGBT 2026 launch for indexing purposes, with the press date noted.
- **10x Genomics Atera** had a roadmap preview at AGBT but its formal commercial launch happened at **AACR 2026** in April. Dossier lives in the AGBT vault under "roadmap preview" with a cross-link to the AACR launch.
