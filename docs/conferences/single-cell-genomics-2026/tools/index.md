# Single-Cell Genomics 2026 — Tools

Per-tool index covering the GRC Single-Cell Genomics 2026 (May 10–15, Les Diablerets, off-the-record) and the Wellcome Single Cell Biology 2026 (Jun 10–12, Hinxton, partially recorded). Both meetings together define the single-cell-methods cohort that AACR 2026 talks will cite for the next 12 months.

> **Status:** Template stub + pre-meeting scaffolding. Wellcome speaker list dropped Apr 22, 2026 — ~15–20 tool pages can be pre-scaffolded from the speaker bios + their lab's most-recent preprint, then enriched post-meeting. GRC pages cannot be scaffolded in advance (talk list is closed); they get populated from preprint signals in the 4–8 weeks after May 15.

## Per-tool entry template

Each tool gets its own page (`tools/<package-slug>.md`) following this structure. The single-cell-flavored extension of the standard EuroBioC / CSHL BDS template:

````markdown
# <PackageName>

**One-line description** — what the package does in plain language.

- **Maintainer:** <name> (<institution>)
- **Modality:** scRNA / scATAC / spatial-transcriptomics / spatial-proteomics / CITE-seq / methylation / multimodal / lineage / atlas-platform
- **Language:** Python / R / both / standalone binary
- **Package:** [PyPI / Bioconductor / CRAN / GitHub-only]
- **Source:** [GitHub link]
- **Docs / vignette:** [link]
- **Preprint:** [bioRxiv DOI]
- **Publication:** [journal link, if any]
- **Status at SCG-2026:** new release / major update / methods talk / case study / atlas drop / preprint pre-announcement
- **Atlas footprint:** which large datasets it's been benchmarked on (HCA, Tabula Sapiens, CELLxGENE corpus, HuBMAP, HTAN, ENCODE-singlecell, MS-style atlases)
- **Foundation-model lineage:** if applicable — scGPT-line / Geneformer-line / scFoundation-line / scBERT-line / Universal Cell Embeddings / scPRINT / independent

## Talk at GRC Single-Cell Genomics 2026 (Les Diablerets, May 10–15)

- **Speaker:** ...
- **Session:** AI for Genomics / TF Regulation / Single-Cell Modeling / Applications in Medicine / Spatial & Proteomics / 3D Genomics / Epigenomics
- **Day:** ...
- **Slides / abstract:** Gordon Conferences are closed-door — no public record (extract from post-meeting preprints + attendee Bluesky/X with chair blessing)
- **Recording:** none (GRC policy)

## Talk at Wellcome Single Cell Biology 2026 (Hinxton, Jun 10–12)

- **Speaker:** ...
- **Session:** large scale / beyond transcriptomics / non-model / tech dev / computational / spatial
- **Day:** Wed 10 / Thu 11 / Fri 12
- **Slides:** [Zenodo or lab site]
- **Video:** [YouTube — Wellcome posts keynotes; selective for short talks]
- **Abstract page:** [Wellcome event page link]

## What it does

2–3 sentences: the problem it solves, key methodological idea, what it consumes/produces.

## Where it fits in the corpus

- AACR 2026 (single-cell + spatial topic): [link if mentioned]
- EuroBioC 2025: [link to SpatialData / DESpace / OSTA / spatialFDA / iSEE if related]
- CSHL BDS 2026 (spatial session): [link]
- RECOMB 2026 (ML for biology): [link]
- ISMB 2026 (MLCSB / RegSys / Sequence Analysis): [link]
- AGBT 2026 (platform-launch reference): [link if uses 10x Visium HD / Xenium / Curio Pixel / etc.]

## Notes

Free-form impressions, claimed benchmarks, head-to-head comparisons to alternatives (scGPT vs Geneformer vs scFoundation; Tangram vs cell2location vs CytoSPACE; etc.).
````

## Tool index — pre-meeting scaffolding (Wellcome speakers only)

The 15 Wellcome speakers each anchor one likely tool/method/atlas. GRC speakers are unknown until on-site, so this table only pre-scaffolds the Wellcome half. The full ~30-tool table fills in post-Jun 12.

| Tool / method | Modality | Anchor speaker | Affiliation | Likely meeting slot | Cross-corpus links (anticipated) |
|---|---|---|---|---|---|
| scPRINT / CellFlow line | foundation model | Charlotte Bunne | EPFL | Wellcome — computational | AACR agentic-AI; RECOMB ML |
| ISS / In Situ Sequencing | spatial transcriptomics | Mats Nilsson | Stockholm | Wellcome — spatial | AACR spatial; AGBT platform |
| Monocle / sci-RNA-seq lineage | scRNA + lineage | Cole Trapnell | UW | Wellcome — organizer talk | AACR single-cell; EuroBioC |
| CellTypist / tissue atlases | atlas-scale annotation | Roser Vento-Tormo | Sanger | Wellcome — organizer + spatial | AACR atlas; HCA |
| CODEX / spatial-proteomics analysis | spatial proteomics | Sizun Jiang | Harvard | Wellcome — spatial | AACR spatial biomarkers |
| MIBI / multiplexed ion beam | spatial proteomics | Leeat Keren | Weizmann | Wellcome — organizer / large-scale | AACR spatial; Vallot Curie |
| Plasmodium atlas / MalariaCellAtlas | non-model scRNA | Mara Lawniczak | Sanger | Wellcome — non-model | none direct |
| DNA Typewriter / lineage barcoding | lineage tracing | James Gagnon | Utah | Wellcome — beyond transcriptomics | EMBO Lineage Tracing 2026 |
| Recording lineage (engineered) | lineage tracing | Theresa Loveless | Rice | Wellcome — tech dev | EMBO Lineage Tracing 2026 |
| novoSpaRc / spatial reconstruction theory | spatial-reconstruction algorithm | Mor Nitzan | Hebrew U | Wellcome — computational | EuroBioC SpatialData |
| Single-cell epigenomics (cancer) | scATAC / methylation in cancer | Céline Vallot | Curie | Wellcome — beyond transcriptomics | AACR epigenetics; HTAN |
| Oligodendrocyte single-cell atlas | scRNA / neuro | Gonçalo Castelo-Branco | Karolinska | Wellcome — large-scale | none direct |
| Lipid single-cell (D'Angelo) | beyond-transcriptomics | Giovanni D'Angelo | EPFL | Wellcome — beyond transcriptomics | none direct |
| Marlow comparative atlases | non-model / evo-devo | Heather Marlow | Chicago | Wellcome — non-model | none direct |
| Amit-line immune atlases / MARS-seq successors | scRNA / immune | Ido Amit | Weizmann | Wellcome — keynote | AACR immune-stromal; HCA |

### Tool index — GRC (post-meeting, May 15+)

The GRC's seven sessions (AI for Genomics, TF Regulation, Single-Cell Modeling, Applications in Medicine, Spatial & Proteomics, 3D Genomics, Epigenomics) will each yield ~5 oral talks → ~30–35 tool candidates. Tool pages get drafted from:

1. Preprints that drop May 15–Jul 15 with "presented at the 2026 Gordon Research Conference on Single-Cell Genomics" in the acknowledgements.
2. Bluesky posts from attendees with the chair's permission (Pisco has historically blessed selective sharing).
3. Selected speakers' lab Bluesky/X feeds announcing their published-by-then work.

Expected dominant lineages at GRC 2026 (based on the AI/ML subtitle and the field's mid-2026 trajectory):

- **Foundation-model successors:** scGPT-v2, Geneformer-v2, scFoundation-clinical, Universal Cell Embeddings updates, scBERT successors, perturbation-foundation models (Bunne's CellFlow class).
- **Atlas-platform layer:** CELLxGENE Discover updates, HCA v2.0, Tabula Sapiens v3, HuBMAP integration, HTAN cancer-atlas drops.
- **Spatial inference:** Visium HD analysis tooling (Voyager, SpatialData, semla, STUtility), Xenium-native pipelines, CosMx integration, MERSCOPE / MERFISH-Vizgen analysis.
- **3D genomics:** scHi-C analysis (Nagano-line, Higashi successors), single-cell 3D contact-map inference, A/B compartment dynamics.
- **Multimodal:** CITE-seq / TEA-seq / Multiome integration, methylation+RNA, proteo-genomics.

## Why this format

- **Cross-vault links matter most at this meeting.** Tools released here cycle through AACR sessions in the same year (talks reference "new methods like X") and AACR posters the next year (posters use X as a default). Single-Cell Genomics → AACR is the densest tool-to-clinical-application link in the corpus.
- **Modality field is critical** for slicing — single-cell is too broad a category for one-axis searching. scRNA-only methods vs spatial-only methods vs multimodal methods don't compete with each other.
- **Atlas footprint** captures the "is this tool already validated at scale?" dimension that distinguishes 2024-style methods (single dataset benchmarks) from 2026-style methods (CELLxGENE-corpus benchmarks expected).
- **Foundation-model lineage** captures the most important methods-evolution axis of 2026 — which transformer family is this descended from, and what does it cite as baseline?
- **Two-meeting Talk fields** are necessary because many tools will be presented at both GRC and Wellcome (slightly different versions/framings to slightly different audiences).

## Open questions for the pilot

1. **GRC scaffolding from non-public sources** — Pisco's discretion. Default policy: only include a GRC tool page if (a) a preprint exists by post-meeting drafting time, (b) the author has publicly acknowledged presenting at GRC, OR (c) we hear the talk content from an attendee with permission to share. No second-hand "I heard X presented Y" without confirmation.
2. **Foundation-model lineage as a free-text vs controlled-vocab field** — leaning controlled (scGPT / Geneformer / scFoundation / scBERT / UCE / scPRINT / independent) so we can do "show me all Geneformer-line tools" filters later. Open.
3. **Atlas-platform tools (CELLxGENE Discover, HCA portal, CZ CELLxGENE Census)** — these are tools but not in the standard "package on Bioc/PyPI" sense. Proposed: separate badge "Status: platform / atlas-infrastructure" that swaps the package row for an "Access" row pointing to a web portal.
4. **Lineage-tracing tools (DNA Typewriter, recording lineage, Gagnon-line)** — these are wet-lab methods primarily, with analytical tooling secondary. Proposed: "Status: experimental method + companion analysis package" — two rows for source links (wet-lab protocol + analysis code).
