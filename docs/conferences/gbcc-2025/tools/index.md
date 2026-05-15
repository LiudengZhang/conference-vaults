# GBCC 2025 — Tools

GBCC2025 ran 3 keynotes + 53 oral talks across 5 sessions + 11 lightning talks + 10 hands-on workshops + 50+ posters. A substantial fraction of the oral and lightning talks introduce or update a named Bioconductor package, a Galaxy tool, or a cross-platform integration artifact — that's what this directory captures. Each entry below corresponds to **one tool presented at GBCC2025** (Bioconductor package, Galaxy tool, or integration scaffolding).

> **Status:** Active — bulk extraction complete (24 tool entries across Bioconductor packages, Galaxy tools, and cross-platform integration). Talks-with-packages source list at [../program-notes.md](../program-notes.md). Slide DOIs (Zenodo) and YouTube playlist links TBD pending Bioconductor community deposits.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure:

````markdown
# <PackageName>

**One-line description** — what the package does in plain language.

- **Maintainer:** <name> (<institution>)
- **Ecosystem:** Bioconductor / Galaxy / cross-platform
- **Bioconductor:** [package page] *(if applicable)*
- **Galaxy ToolShed:** [tool page] *(if applicable)*
- **Source:** [GitHub link]
- **Vignette / docs:** [link]
- **Status at GBCC2025:** new release / major update / methods talk / case study / workshop / integration demo

## Talk at GBCC2025

- **Speaker:** ...
- **Day / session:** Day X — Oral Session N / Lightning / Workshop
- **Slides:** [Zenodo DOI]
- **Video:** [GBCC2025 YouTube playlist link if recorded]
- **Abstract / talk page:** [scientific-program link or CSHL abstract-book page]

## What it does

2–3 sentences: the problem it solves, key methodological idea, what it consumes/produces.

## Where it fits in the corpus

- AACR 2026: [link if mentioned]
- ISMB 2026: [link if mentioned]
- RECOMB 2026: [link if mentioned]
- Nextflow Summit 2026: [link if mentioned]
- EuroBioC 2025: [link if also presented at sister event]

## Notes

Free-form impressions, benchmarks claimed, comparisons to alternatives. For Galaxy-wrapped Bioconductor tools: link the wrapper PR or the `tools-iuc` shed entry.
````

## Tool index

24 entries from oral sessions, lightning talks, workshops, and the post-conference CoFest deliverable, ordered by day/session. Three keynotes deferred to the keynotes/ subdirectory and day digests.

Skipped (not in this table): community / training / non-tool talks (Doyle on Bioconductor in Africa; Gauthier on UseGalaxy Canada; Santana on sertão research; Kucher on AnVIL training); methods talks without a clearly named package anchor (Hansen on allele-specific methylation; Nanda on viral-infection signaling networks; Lakshman on orthology-at-scale; Eagles on Visium HD; Moses on LUAD spatial; Campillo on differential transcript usage — flagged for follow-up after the abstract book is retrieved).

| Package / Tool | Ecosystem | Domain | Speaker | Day / Session | Slides | Video | Mentioned elsewhere |
|---|---|---|---|---|---|---|---|
| [GAIA](gaia.md) | Galaxy | AI agent / NLI | Qiu, Goecks | Day 2 / Oral 1 | TBD | TBD | [GalaxyMCP](galaxymcp.md) |
| [GalaxyMCP](galaxymcp.md) | Galaxy | AI / MCP | Baker, Qiu, Goecks, Schatz | Day 2 / Oral 1 | TBD | TBD | [GAIA](gaia.md) |
| [AnVIL](anvil.md) | Galaxy + cloud | cloud platform | Mosher, Schatz et al. | Day 2 / Oral 1 + Day 3 workshop | TBD | TBD | [bioc-to-galaxy](bioc-to-galaxy.md) |
| [torch](torch.md) | CRAN / R | DL / epigenetic clock | Jamie Park | Day 2 / Oral 2A | TBD | TBD | — |
| [Galaxy-ML2](galaxy-ml2.md) | Galaxy | ML tool suite | Lyra Junior, Qiu | Day 2 / Oral 2A | TBD | TBD | — |
| [NOVA](nova.md) | Galaxy | neutron scattering | Gregory R Watson | Day 2 / Oral 2A | TBD | TBD | — |
| [TPV Broker](tpv-broker.md) | Galaxy | scheduler | De Geest, Srikakulam et al. | Day 2 / Oral 2A | TBD | TBD | — |
| [gINTomics](gintomics.md) | Bioconductor | multi-omics integration | Velle, Romualdi | Day 2 / Oral 2A | TBD | TBD | [MOSClip ↗ EuroBioC](../../eurobioc-2025/tools/mosclip.md) |
| [RAIDS](raids.md) | Bioconductor | ancestry inference | Belleau, Deschênes et al. | Day 2 / Oral 2B | TBD | TBD | — |
| [signifinder](signifinder.md) | Bioconductor | cancer signatures | Stefania Pirrotta | Day 2 / Oral 2B | TBD | TBD | [mitology](mitology.md) |
| [SEMPLR](semplr.md) | Bioconductor | TF-binding variants | Kenney, Boyle, Phanstiel | Day 2 / Oral 2B | TBD | TBD | — |
| [Meta-iPep](meta-ipep.md) | Galaxy | metaimmunopeptidomics | Do, Mehta | Day 2 / Oral 2B | TBD | TBD | — |
| [HiFi-MAG](hifi-mag.md) | Galaxy | long-read metagenomics | Collins, Schatz | Day 2 / Oral 2B | TBD | TBD | [mia](mia.md) |
| [bsseq](bsseq.md) | Bioconductor | ASM methylation (ONT) | Kasper D Hansen | Day 2 / Oral 2B | TBD | TBD | — |
| [SynExtend](synextend.md) | Bioconductor | orthology / ExoLabel | Lakshman, Wright | Day 2 / Oral 2B | TBD | TBD | — |
| [SeqArray](seqarray.md) | Bioconductor | rare-variant annotation | Xiuwen Zheng | Day 2 / Oral 2B | TBD | TBD | — |
| [Voyager](voyager.md) | Bioconductor | spatial multiscale (LUAD) | Lambda Moses | Day 2 / Oral 2B | TBD | TBD | [SpatialData ↗ EuroBioC](../../eurobioc-2025/tools/spatialdata.md) |
| [splicelogic](splicelogic.md) | Bioconductor | differential transcript usage | Campillo, Love | Day 2 / Oral 2B | TBD | TBD | [plyxp](plyxp.md) |
| [atena](atena.md) | Bioconductor | transposable elements | Robert Castelo | Day 3 / Lightning | TBD | TBD | [GSVA→Galaxy](gsva-galaxy.md) |
| [iscream](iscream.md) | Bioconductor | BED queries (Rcpp) | James Eapen | Day 3 / Lightning | TBD | TBD | — |
| [KRSA](krsa.md) | Bioconductor | kinome analysis | Ali Imami | Day 3 / Lightning | TBD | TBD | — |
| [sosta](sosta.md) | Bioconductor | spatial omics | Gunz, Robinson | Day 3 / Oral 3 | TBD | TBD | [spatialFDA ↗ EuroBioC](../../eurobioc-2025/tools/spatialfda.md), [SpatialData ↗ EuroBioC](../../eurobioc-2025/tools/spatialdata.md) |
| [IWC](iwc.md) | Galaxy | workflow registry | Marius van den Beek | Day 3 / Oral 3 | TBD | TBD | — |
| [spatialLIBD](spatiallibd.md) | Bioconductor | Visium HD | Nicholas Eagles | Day 3 / Oral 3 | TBD | TBD | [Voyager](voyager.md), [SpatialData ↗ EuroBioC](../../eurobioc-2025/tools/spatialdata.md) |
| [mia](mia.md) | Bioconductor | microbiome | Tuomas Borman | Day 3 workshop + Day 4 / Oral 5 | TBD | TBD | [mia ↗ EuroBioC](../../eurobioc-2025/tools/mia.md), [miaTime ↗ EuroBioC](../../eurobioc-2025/tools/miatime.md) |
| [Tidyomics](tidyomics.md) | Bioconductor | tidyverse for omics | Stefano Mangiola | Day 3 / Lightning + Oral 4 | TBD | TBD | [plyxp](plyxp.md) |
| [bioc-to-galaxy](bioc-to-galaxy.md) | Integration | auto-wrap pipeline | Joshi, Cumbo, Blankenberg | Day 2 + Day 3 workshop | TBD | TBD | [GSVA→Galaxy](gsva-galaxy.md), [mia](mia.md) |
| [plyxp](plyxp.md) | Bioconductor | dplyr for SummarizedExperiment | Landis, Love | Day 4 / Oral 5 | TBD | TBD | [Tidyomics](tidyomics.md), [DeeDeeExperiment ↗ EuroBioC](../../eurobioc-2025/tools/deedeeexperiment.md) |
| [mitology](mitology.md) | Bioconductor | mitochondrial activity | Pirrotta, Bonora, Calura | Day 4 / Oral 5 | TBD | TBD | [signifinder](signifinder.md) |
| [FAIR-EASE](fair-ease.md) | Galaxy | Earth-system | Jossé, Detoc, Bodéré | Day 4 / Oral 5 | TBD | TBD | — |
| [ipd](ipd.md) | CRAN / R | post-prediction inference | Stephen Salerno | Day 2 workshop + Day 4 / Oral 5 | TBD | TBD | — |
| [GSVA→Galaxy](gsva-galaxy.md) | Integration | wrapper deliverable | Cumbo, Joshi, Raubenolt, Blankenberg | CoFest (Jun 27-28) | — | — | [bioc-to-galaxy](bioc-to-galaxy.md), [atena](atena.md) |

## Why this format

- **Cross-vault links matter** — same as EuroBioC2025: tool released here, used in cancer-research talk X, benchmarked in methods paper Y, all one click apart
- **Slides + video + vignette + Bioconductor-or-Galaxy page** in one place
- **Ecosystem field** is GBCC-specific — separates R packages from Galaxy tools from cross-platform scaffolding without forcing them into separate directories
- **Status field** distinguishes a v1.0 announcement from a 4-year-old package's annual update from a methods talk from an integration demo
- **Mentioned-elsewhere** points the reader at the EuroBioC2025 vault when the same package was presented at both events (Soneson, Mangiola, Castelo, Pirrotta, Borman, and others appear in both lineups)

## Open questions for the pilot

1. **Granularity** — ✅ inherited from EuroBioC2025: one page per tool
2. **AACR dossier mirroring** — ✅ inherited: full entry in both vaults, cross-linked
3. **Sample tools to draft first** — *open*: candidate set is GAIA + GalaxyMCP (Galaxy AI scaffolding pair, exercises the ecosystem-field variant) and RAIDS / signifinder / sosta (canonical Bioconductor methods talks). plyxp is also a strong template-validation pick because it's a tidyverse-for-SummarizedExperiment package — exactly the cross-cutting kind of tool we want to make sure renders well
4. **Edge case: non-Bioconductor tools** — *open*: GBCC's edge case is GAIA / GalaxyMCP / NOVA — Galaxy-side tools with no Bioconductor page at all. Proposed: same template, swap "Bioconductor" line for "Galaxy ToolShed" and use a "Galaxy" ecosystem badge
5. **Galaxy workflows vs. Bioconductor packages — same template, or split?** — *open*: a Galaxy tool/workflow has different surface (XML wrapper, ToolShed entry, training material) than a Bioconductor package (DESCRIPTION, vignette, BiocCheck). The template above tries to unify them with the "Ecosystem" field plus optional Bioconductor/Galaxy-ToolShed lines. Decision deferred until 3 sample entries (1 Bioconductor, 1 Galaxy-only, 1 integration scaffold) are drafted by hand. If the unified shape is awkward, fall back to two templates and add a third for "integration scaffolding" (Bioc-in-Galaxy wrappers, GalaxyMCP-style protocols, automatic-wrapping pipelines).
