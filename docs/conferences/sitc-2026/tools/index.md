# Tools — SITC 2026

The second primary artifact: **one Markdown file per biomarker / immune-profiling method or pipeline**. SITC programs methods talks adjacent to drug readouts — multiplex IF panels, TCR repertoire pipelines, ctDNA-MRD assays, microbiome sequencing protocols, single-cell + spatial classifiers. Each gets a `tools/<slug>.md` entry. The drug / cell-therapy side lives in [`trials/`](../trials/index.md).

> **Status:** Template stub. We're carrying over the per-tool format from [EuroBioC 2025 tools](../../eurobioc-2025/tools/index.md), with one modification: SITC is **not** a Bioconductor venue — many tools are commercial platforms (Akoya, Standard BioTools / IonPath MIBI, NanoString CosMx, 10x Xenium / Visium HD, Adaptive immunoSEQ), not R packages. The "Status" badge swaps `Bioconductor` for `Platform / vendor / open-source repo / vignette / preprint`. Once the program-at-a-glance posts in September, ~15–20 entries get populated from the methods + immune-monitoring sessions.

## Per-tool entry template

Each tool gets its own page (`tools/<slug>.md`) following this structure:

````markdown
# <Tool / panel / platform name>

**One-line description** — what the assay / pipeline does in plain language.

- **Group / vendor:** <academic lab / commercial vendor>
- **Platform / format:** <multiplex IF / spatial-transcriptomics / TCR-seq / single-cell / ctDNA / 16S+shotgun / image-analysis / classifier>
- **Repo / vendor page:** [link]
- **Vignette / protocol:** [link]
- **Preprint / paper:** [DOI]
- **Status at SITC 2026:** <new release / major update / methods talk / case-study readout / pre-conference workshop>

## Talk at SITC 2026

- **Speaker:** ...
- **Day / session:** ...
- **Slides:** [link if shared]
- **Video:** [SITC virtual link if recorded]
- **Abstract:** [JITC DOI]

## What it does

2–3 sentences: the immune-profiling problem it solves, key methodological idea,
what it consumes / produces. Be explicit about the **IO use case** — biomarker
of response, mechanism-of-resistance characterization, MRD, neoantigen
prediction, TCR-clonotype tracking, immune-cell-state classification.

## Where it fits in the corpus

- **SITC 2026 trials:** [link to any `trials/<x>.md` that used this assay for correlatives]
- **AACR 2026:** [link if mentioned in an AACR talk or poster]
- **EuroBioC 2025:** [link if the same / analogous package was shown]
- **GBCC 2025 / RECOMB 2026 / ISMB 2026:** [link if mentioned]
- **JPM 2026:** [link if commercial vendor presented]

## Notes

Free-form impressions: validation data shown, comparisons to alternatives,
batch / cross-site reproducibility claims, sample-prep requirements,
turnaround time, regulatory status (CDx / CLIA / RUO).
````

## Tool index

Pre-meeting shortlist of the categories we expect to populate. The specific named platforms below are **expected, subject to program release** — derived from SITC 2025 program shape, AACR 2026 method-talk overlap, and active commercial / academic platforms in IO biomarker development. To be replaced with named talks once SITC posts the program-at-a-glance.

| Category | Representative platforms / packages | Anticipated SITC angle | Cross-vault link |
|---|---|---|---|
| **Multiplex IF / IHC** | Akoya PhenoCycler-Fusion, Standard BioTools / IonPath MIBI, Lunaphore COMET | TME phenotyping panels keyed to cell-therapy / bispecific cohorts | AACR 2026 spatial sessions; [SpatialData](../../eurobioc-2025/tools/spatialdata.md) |
| **Spatial transcriptomics** | 10x Xenium, NanoString CosMx, Curio Seeker, Vizgen MERSCOPE | Pre/post-treatment biopsy spatial-immune profiling | AACR 2026 spatial; [DESpace](../../eurobioc-2025/tools/despace.md), [spatialFDA](../../eurobioc-2025/tools/spatialfda.md) |
| **TCR repertoire** | Adaptive immunoSEQ, MiXCR, Mvision, Repertoire AI | Clonotype tracking pre/post-treatment; neoantigen-vaccine response | EuroBioC 2025 clonal-tracking ([barbieQ](../../eurobioc-2025/tools/barbieq.md)) |
| **scRNA-seq + scTCR** | 10x Chromium, Parse, Scale; downstream Seurat / scanpy | Cell-therapy product profiling + TIL state characterization | AACR 2026 single-cell axis; EuroBioC2025 single-cell short talks |
| **ctDNA-MRD** | Signatera (Natera), RaDaR (NeoGenomics), Guardant Reveal, Tempus xM | Surrogate endpoint for adjuvant IO / vaccine trials | ASCO 2026 trials with ctDNA-defined cohorts |
| **Neoantigen prediction** | NetMHCpan family, MHCflurry, Personalis NeXT, Gritstone EDGE, BioNTech iNeST | The Wu Smalley lecture substrate; vaccine selection pipelines | AACR 2026 bioinfo-tools axis |
| **Microbiome profiling** | Shotgun metagenomics (illumina + nanopore), 16S, metabolomics | Stool + tissue panels in microbiome × IO cohorts | EuroBioC 2025 [mia](../../eurobioc-2025/tools/mia.md), [miaTime](../../eurobioc-2025/tools/miatime.md) |
| **Spatial-immune classifiers** | Lunaphore-derived signatures, NeoGenomics MultiOmyx, academic CODEX/MIBI pipelines | Response / resistance classifiers; biomarker development | AACR 2026 sessions on TME spatial atlases |
| **Cytometry (mass + spectral)** | Cytek Aurora, Standard BioTools Helios (CyTOF), spectral flow standardization | Deep immune-monitoring panels for clinical trial correlatives | Methods workshops |
| **HLA typing + class-I/II profiling** | OptiType, Polysolver, arcasHLA, Personalis ImmunoID | Required upstream of TCR-T and personalized-vaccine trials | Neoantigen / TCR-T trial cross-links |
| **Image-analysis pipelines (digital pathology)** | QuPath, Stardist, HALO (Indica Labs), PathAI | TIL counting, multiplex-IF segmentation, response classifiers | EuroBioC 2025 [HistoImagePlot](../../eurobioc-2025/tools/histoimageplot.md) |
| **Soluble biomarker panels** | Olink, SomaScan, Luminex multiplex | Cytokine release / IO toxicity / pharmacodynamic monitoring | Trial-correlative panel cross-links |

**Additional candidates** once the program lands:

- **Single-cell proteomics** — emerging in cell-therapy product characterization; EuroBioC [scp-distributional](../../eurobioc-2025/tools/scp-distributional.md) cross-link
- **Foundation models for TCR / antigen prediction** — TCRBert-class, ESM-2 derivatives applied to immunogenicity
- **CITE-seq + cell hashing** — high-parameter single-cell for cell-therapy product release testing
- **CTC / cellular MRD** in solid tumors — Bio-Techne, Epic Sciences platforms
- **Imaging mass cytometry** — Hyperion / Standard BioTools, academic IMC pipelines

## Why this format

- **Cross-vault links matter most here** — a multiplex-IF panel from SITC anchors trial correlatives at AACR, biomarker classifiers at RECOMB, and Bioconductor analysis packages at EuroBioC. The tool entry is the join key.
- **Trial ↔ tool linking** is the unique value of the SITC vault: every `tools/<x>.md` should link to the `trials/<y>.md` where it appeared as correlative data, and vice versa.
- **Platform vs package distinction** is explicit. Unlike EuroBioC (all R packages), SITC mixes commercial platforms, academic open-source pipelines, and clinical assays — the Status field surfaces that.

## Open questions for the build

1. **Commercial vendor sessions** — SITC has industry-symposia where vendors (Akoya, 10x, Adaptive, NanoString) present case studies. Treat these as `tools/` entries with `Status: vendor case-study`?
2. **CDx / IVD status** — for assays moving toward companion-diagnostic status (Signatera, Akoya panels in trials), surface FDA / EU regulatory state as a separate field?
3. **Workshops vs talks** — pre-conference workshops on cellular-therapy immune-monitoring and biomarker development warrant fuller treatment than a single talk; consider a workshop-detail subsection in the template.
