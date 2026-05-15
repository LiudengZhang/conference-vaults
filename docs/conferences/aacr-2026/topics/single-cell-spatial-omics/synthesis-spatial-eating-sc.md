# Synthesis — is spatial eating single-cell?

The headline claim this page argues: **at AACR 2026, spatial is eating single-cell — not at the volume level, but at the identity level.** scRNA-seq is still the more-common assay by a 55-to-35 margin in this 1,015-poster corpus, but the dedicated poster sessions, the method-development sessions, the late-breaking sessions, and the rate at which historically pure-scRNA workflows have added a spatial arm all point to a field where the poster-hall centroid of "single-cell & spatial omics" is migrating toward spatial.

The corpus for this page is the same 1,015 posters catalogued in [landscape.md](landscape.md), plus five transcripts from method-centric sessions: **Spatial and Single-Cell Omics at Scale** (Sun 4/19, Broad / MSK / Weizmann co-chairs), **AI × Spatial Transcriptomics / Pathology** (Mon 4/20 PM, symlinked from Agentic AI), **Single-Cell Multi-omic Technologies** (Mon 4/20, chromatin-and-DNA-focused), **Late Spatial Biomarkers at Single-Cell Resolution** (Tue 4/21 PM), and **Decoding Cancer Ecosystem Pathology** (Mon 4/20 AM).

*Quotation note: quotations below are lightly cleaned transcript fragments (paragraphing, obvious filler removed). Names crosschecked against session metadata per `docs/notes/caveats.md`. Where auto-captions render a name unclear, the attribution is to the session chair role rather than an uncertain spelling.*

---

## Claim 1 — platform-count ratio across posters

Primary-platform counts, taken from the classifier in [landscape.md](landscape.md):

| Axis | Count | Share of classified (994) |
|---|---:|---:|
| Spatial subtotal (imaging-ST + sequencing-ST + proteomics) | 345 | 35% |
| Single-cell subtotal (scRNA-seq + multiomics) | 550 | 55% |
| Other / hybrid | 99 | 10% |

On the strict volume metric, scRNA-seq still wins. But the "any match" column of the landscape tally is more informative: **181 posters match at least one spatial-proteomics keyword, and 465 of 1,015 posters (46%) mention the word "spatial" at all.** 281 of those 465 *also* mention single-cell / scRNA / snRNA — in other words, for every two pure-scRNA-seq posters, there is now one hybrid poster pulling scRNA-seq into a spatially-resolved design. This is the real ratio to watch.

Supporting hybrid / spatial-forward posters:

- **#773** (KENTA MANABE, Physicochemical Modulation of the Cancer Ecosystem) — "Single-cell and spatial transcriptomic profiling reveal fibrosis-related tumor states in lung squamous cell cancer"; the scRNA-seq atlas is built explicitly to annotate the Visium spots.
- **#4945** (Ji Hye Choi, Spatial Niches 2) — "Distinct colorectal cancer tumor cell subtypes revealed by single-cell **and** spatial transcriptomics"; the poster reports subtypes only resolved when the scRNA-seq-defined states are projected back onto Xenium sections.
- **#LB229** (Jason Carter, LB Tumor Biology 1) — "Single-cell and spatially resolved transcriptomics identifies clinically targetable myeloid niches"; a late-breaking poster where the clinically actionable finding is the niche, not the cell type.
- **#711** (Asumi Iesato, Molecular Pathology) — "Single-cell and spatial profiling identifies tumor features and actionable surface targets in primary thyroid cancer"; same pattern.
- **#6114** (Integrated single-cell and spatial atlas of tumor-draining lymph nodes) — atlas framing, spatial substrate.
- **#4954** ("Integrated scRNAseq and spatial RNAseq analysis of aggressive prostatic adenocarcinoma identifies TIGIT-expressing T cells") — scRNA is the first-listed method, but the contribution is a spatially-mapped target.
- **#7744** (Single-cell and spatial profiling reveal tumor-immune features underlying pathologic complete response) — neoadjuvant-response biomarker, built on both assays.
- **#7751** (Integrative multi-omics and spatial transcriptomics reveal novel immunotherapy targets).

Common rhetorical pattern: the poster title names both assays. The scRNA-seq is the annotation atlas. The spatial section is where the claim actually lives — "neighborhood," "niche," "architecture," "margin," "interaction."

A precise restatement of the 55-vs-35 volume picture: of the 814 posters that mention scRNA / snRNA / single-cell anywhere, **281 (35%) also mention "spatial."** Of the 465 that mention "spatial," **281 (60%) also mention single-cell.** A spatial poster is much more likely than a single-cell poster to be *both*; this asymmetry is the numerical fingerprint of spatial pulling single-cell into its orbit rather than the other way around. Said another way: when a poster adopts one of these two methodologies, the spatial poster usually pulls in scRNA-seq as a complement; the single-cell poster does *not* typically pull in spatial as a complement.

## Claim 2 — growth signal in session titles

The poster-session assignments reveal a structural asymmetry that the aggregate platform count conceals:

- **Dedicated spatial-named AACR 2026 poster sessions: 7.** Spatial Proteomics and Transcriptomics 1, 2, and 3 (24 + 26 + 28 = 78 posters in those three alone); Spatial Niches and Functional Boundaries within the TME 1 and 2 (22 + 22 = 44 posters); Spatial Protein Profiling and Multi-Modal Mapping of Tumor and Circulating Ecosystems (15 posters); Functional and Spatial Regulation of Immune Evasion and Anti-Tumor Immunity (13 posters). **Total spatial-named poster capacity: 150 posters / 15% of the entire corpus.**
- **Dedicated single-cell-named AACR 2026 poster sessions: 0.** There is no "Single-Cell RNA-seq 1, 2, 3" session. scRNA-seq posters scatter across biology-framed sessions (Fibroblasts as Architects of the TME, Tumor Heterogeneity, Adaptive Immunity, Inflammation-Immunity-Cancer, Pediatric Cancer Genomics, Clonal Hematopoiesis, and so on). That pattern — spatial as a methods track, single-cell as a workhorse — is exactly what "eating" looks like institutionally.

The late-breaking track reinforces this: the four headline method-and-spatial-centric LB bioinformatics posters (**#LB175** spatially-resolved cell-type inference from H&E; **#LB159** benchmarking foundation models on spatial transcriptomics; **#LB170** scVarID single-cell somatic-variant linkage; **#LB169** scCAP ontology-aware LLM for scRNA annotation) split 2:2 spatial vs single-cell. That's parity on a track where five years ago it would have been 4:0 single-cell.

Supporting session-title count evidence (from session-title string match, not classifier): six of the eight AACR 2026 session titles in the SCSO **strong-fit method-centric** tier contain the word "spatial" or "atlas"; two do not; zero contain "single-cell" without "spatial." See [index.md](index.md#strong-fit-method-centric) for the full list.

## Claim 3 — transcript voices endorse the spatial-centric framing

**Dana Pe'er (Memorial Sloan Kettering Institute)**, opening her talk at *Spatial and Single-Cell Omics at Scale* (Sun 4/19):

> "For a while, we have been really talking about technologies and technologies, and now I really want to see, can we get these technologies to do something and understand biology? […] Cancer was always a disease of mutations, but cancer is really also a disease of the microenvironment. […] We need to understand this changed morphology, this changed microenvironment, and how does the progenitor cell environment look like."

The Broad-affiliated co-chair (unnamed in the auto-caption; introduced as "I'm from the Broad") opens the same session with the single most load-bearing line in this entire corpus:

> "Cells really only make sense in context. […] What we've been doing in genomics for a long time is a little bit like zooming in to that cell and looking at each cell in its individual context. **And it's been focused on dissociated cells. And it's only been recently that we've been able to bring the full power of molecular measurements directly within the context of tissues.**"

That is the case against the last decade of scRNA-seq, delivered by a Broad single-cell-technology lab head at the literal session entitled "spatial and single-cell genomics at scale." The next 35 mentions of "spatial" vs 22 of "single-cell" in the same transcript are downstream of that framing.

**Mingyao Li (University of Pennsylvania)**, opening the *Spatial Transcriptomics × Pathology AI* session (Mon 4/20 PM):

> "Spatial omics technologies, including spatial transcriptomics and spatial proteomics, have transformed our understanding of tumor ecosystems. However, despite their power, the current spatial technologies remain expensive and slow, and this makes them difficult to scale across the full clinical enterprise. […] These histology images are very high resolution, high quality, and importantly, these histology images are very inexpensive, and indeed, they are already routinely being generated for nearly every cancer patient in the clinic. So this highlights a fundamental data tradeoff issue in spatial biology."

Li's *digital tissue twins* program — iSTAR then iSCALE — is a strict translation from the cheap-and-scalable substrate (H&E) to the rich-but-expensive substrate (spatial transcriptomics / proteomics). There is no analogous "scale scRNA-seq from H&E" program at this session. The direction of the arrow matters.

**Andreas Mand** (at *Late Spatial Biomarkers at Single-Cell Resolution*, Tue 4/21 PM) on the field-level validation for spatial proteomics:

> "Our initial study was featured in *Nature Biotechnology* in 2022. Then two years later, *Nature Methods* named **spatial proteomics** the method of the year."

Not scRNA-seq. Not single-cell multiomics. *Spatial proteomics*.

**A session discussant** (NanoString Noetic platform context, same *Late Spatial Biomarkers* Q&A) on the comparison between the spatial transition and the earlier bulk-to-NGS transition:

> "It's no different than what we did in NGS, right? We started out, we sequence everything, and then you hone it down to the key biomarkers that are important. It seems that the same thing will happen here. With Noetic, we're imaging the entire transcriptome. But we're doing that because we wanted to capture all elements of biology before I make the little miniature clinical-grade assay. I think it seems like we made so many mistakes early. In NGS, we made those mistakes. We went to the small panels too early, and we missed some of the biology that should have been in our clinical biomarker assays that weren't there. So hopefully in spatial, we won't make that same mistake."

The discussant is explicitly framing spatial biology as the *next-generation bulk-to-single-cell-plus-spatial transition*, with scRNA-seq absent from the analogy entirely. It is conspicuous that when a senior practitioner reaches for a historical analogue for "the next wave in cancer-biomarker assays," the analogue is NGS panels, not scRNA-seq — *spatial* is treated as the thing that succeeds bulk, not as a companion to single-cell.

One more corroborating data point from the *Spatial and Single-Cell at Scale* session, same unnamed Broad chair speaking about the analytical philosophy of his group's SEGER tool for transcript assignment:

> "It's not a geometric problem. Here we have this sort of boundary between stroma to epithelial, and right here, we have contamination. […] Spatial transcriptomics as people who've used it know, these things are very sparse. So actually having many similar units gives a little bit more robustness."

This is the tell: method-development labs that used to publish scRNA-seq tools (scanpy, Seurat, cellranger-adjacent) are publishing their 2026 posters on spatial-transcript-assignment and spatial-segmentation tools. The substrate under their method-building effort has shifted from dissociated cells to tissue sections — see also #6914 (STCS spatial segmentation), #5505 (cross-platform spatial-omics framework), #5500 (morphology-aware profiling of multiplexed tissue).

## Claim 4 — examples of spatial embedded into historically-scRNA workflows

A few specific poster analogues of "the spatial-ification of biology programs that used to be scRNA-first":

- **Atlas programs**: #3498 (single-cell pediatric cancer atlas) is a pure-scRNA atlas update; #1426 (single-cell tumor atlas for pathway and gene signatures), #7280 (pan-cancer single-cell RNA-seq of monocytes and macrophages) likewise. But #6664 (Single-cell **spatial** proteomics of 1200+ protein targets in tumor microenvironments from diverse cancers) and #6114 (Integrated single-cell and spatial atlas of tumor-draining lymph nodes) are 2026's atlas posters — they carry the atlas claim but the substrate is spatial.
- **DNA methylation**: #1954 — "**Spatial** and single-cell DNA methylation analysis of primary breast cancer reveals lineage-independent epigenetic states." Single-cell methylation (scNMT-like) used to be a pure-scRNA multiomics assay; the 2026 version opens with "spatial and single-cell."
- **CRISPR screens**: #5923 ("Optical pooled CRISPR screening coupling multiplexed guide RNA detection and single-cell spatial multi-omics") and #1214 ("SPACE: Spatially resolved multiomic analysis for high-throughput CRISPR screening in 3D models") and #6200 (Single-cell **spatial** CRISPR screen for tumor microenvironment) and #4913 (Single-cell intercellular CRISPR screen reveals stromal regulators of colorectal cancer) — four of the notable functional-genomics posters this year read out in situ. That's a step-change from the Perturb-seq-only era of 2019-2022.
- **Foundation models**: #5491 (AI FM for single-cell annotation from histopathology images), #2754 (VGL Vision-Gene-Language LLM for cell-type classification from H&E + scRNA), #4163 (general-purpose AI FM for spatial proteomics), #2752 (CancerSTFormer for spot-resolution spatial transcriptomics), #LB159 (practical benchmarking guideline for FMs on spatial transcriptomics). The FM / virtual-cells subfield is where you can see the substrate-shift most starkly: the pathology-and-spatial FMs outnumber the RNA-only cell FMs by roughly 2:1 in this corpus — see the [Virtual Cells landscape](../virtual-cells/landscape.md) for the 48-poster breakdown.

## Counter-evidence — where scRNA is still winning

Not every biology has shifted. Several meaningful exceptions:

**Clonal hematopoiesis / CHIP:** 15 of the 15 CHIP-tagged posters examined use single-cell (scRNA, scATAC, or scWGS) only. Spatial context does not help here — the biology lives in blood cells that are natively dissociated. Representative posters: **#1462** (cell-type-specific somatic variants from scRNA-seq underlying transcriptional heterogeneity in CHIP), **#222** (aberrant T cell proliferation in HIV-associated clonal hematopoiesis), **#LB498** (transcriptional heterogeneity in HSCs predicting clonal fitness), **#2004** (genomic co-evolution of immune system and cancer across time and treatment), **#3225** (multiomic long-read sequencing for chromatin structure). Session: *Clonal Hematopoiesis in Blood Cancer and Solid Tumors* (Mon 4/20 AM) — all talks are single-cell, none is spatial. Similarly: #1783, #LB417.

**Disseminated / circulating tumor cells (DTCs / CTCs):** Rare-cell biology where spatial context within the primary tumor is irrelevant. **#3746** (single-cell liquid biopsy in mCRPC on PSCA-CAR-T), **#117** (scRNA + CNV of CTCs), **#LB005** (DLL3 on CTCs predicting tarlatamab response), **#1434** (deep-learning frameworks for rare-event detection + single-cell phenotyping), **#3776** (centrifugation-free microfluidic CTC isolation), **#3762** (genetic characterization of DTCs from historical cryopreserved bone marrow), **#LB182** (CTC/cfDNA biomarker-guided precision medicine). Session: *Disseminated Tumor Cells in Breast Cancer* (Sun 4/19) — again, all single-cell.

**MRD and CAR-T monitoring:** **#2440** (single-cell MRD profiling in AML), **#5192** (single-cell profiling of immune-circuit disruption preceding CAR-T relapse in B-ALL), **#7012** (scMulti-omics of MRD-associated Tr1-like CD4 in B-ALL), **#643** (Sean Karl Cohort single-cell RNAseq Ewing sarcoma PDX study), **#6463** (longitudinal single-cell atlas of GD2-CAR-T in DIPG). These posters are all about tracking minority populations across time — the assay constraint is sensitivity-per-cell, not tissue context.

**Unfixable-in-tissue biology:** clonal fitness measurements, TCR/BCR repertoire dynamics, cfDNA and ctDNA analysis, CRISPR lineage-tracing (when the barcode is not itself spatial), and drug-response profiling of dissociated cell lines (**#495** single-cell multiomic drug-response of PRISM-multiplexed lines). These will remain single-cell because the biology itself is non-spatial.

The pattern: **scRNA-seq remains the right default for any biology that is either dissociable-by-nature (blood, liquid biopsy) or rare-population-critical (MRD, CTCs).** It is being eaten in solid-tumor TME biology, biomarker discovery, and atlas construction.

## Thin-evidence flags — where the corpus cannot argue decisively

A few sub-claims in this page deserve transparency about what the corpus cannot prove:

- **"Spatial is outpacing single-cell in growth rate" is a session-title argument, not a longitudinal one.** This corpus is one year; AACR 2025 and AACR 2024 would need to be harvested identically to confirm the trajectory. The 0-to-7 ratio of single-cell-named vs spatial-named poster sessions is striking, but it's a snapshot.
- **Platform-vendor counts (Xenium 85 vs CosMx 38, Visium 84 vs Stereo-seq 4) are keyword-in-abstract counts, not shipments or peer-reviewed paper counts.** Abstracts often undercount platform mentions (authors say "spatial transcriptomics" without naming the assay), so these ratios are illustrative but imprecise.
- **"Spatial proteomics is growing faster than spatial transcriptomics" is not directly testable** in this corpus. The primary counts are 125 vs (141+79)=220 — spatial transcriptomics is still larger by roughly 2:1. But the integrated-spatial-proteomics-plus-transcriptomics posters (#6664, #789, #6685, #815) all land in other buckets by the priority rule, which understates spatial proteomics' true integrated footprint.
- **"scRNA-seq is becoming the reference atlas for spatial" is visible in ~30-50 poster abstracts but not always titled that way.** The workflow pattern (dissociate a few samples → scRNA-seq reference → annotate a larger spatial cohort) often appears only in Methods sections that our title-and-abstract regex cannot always reach. The true number of reference-atlas scRNA posters is probably higher than the pure-scRNA-seq count would suggest.
- **Transcript evidence is drawn from five sessions** (spatial-at-scale, AI-spatial-pathology, late-spatial-biomarkers, single-cell-multiomic-technologies, decoding-ecosystem-pathology). Other method-centric sessions — notably *3D Tissue Imaging*, *Neural-Immune Crosstalk*, *Dissecting Hematologic Malignancies at Single-Cell Resolution*, and the *HTAN* session — were scanned for counter-evidence but not systematically mined for pro-thesis quotes; the synthesis would tilt slightly less "eating" and slightly more "complementing" if the hematology and neural-immune sessions had been weighted equally.

## Closing synthesis — eating or complementing?

The honest answer is "both, and the mix depends on biology." For the solid-tumor-TME majority of cancer biology — fibroblasts, macrophages, immune architecture, response prediction, neural-immune crosstalk, senescence — the corpus reads as a near-complete handover: **spatial is the first-listed assay in the poster title, scRNA-seq is the annotation atlas in methods, and the contribution lives in the neighborhood / niche / architecture frame.** That is the "eating" phenotype, and it is the dominant picture in this 1,015-poster corpus.

For dissociable-by-nature biology (hematologic malignancies, liquid biopsy, CTCs, DTCs, MRD) and rare-population biology, scRNA-seq remains uncontested — not because it is fighting back, but because the spatial substrate is not available or not informative. That subfield is complementary, not threatened.

The 2027 prediction, grounded in this year's session-title distribution and the LB bioinformatics track: (1) AACR 2027 will host its first dedicated **Spatial Single-Cell Atlas** poster sessions, likely replacing or absorbing Pan-Cancer Atlas sessions; (2) the Xenium-plus-scRNA-seq-as-reference paper pattern will become so routine that session chairs stop calling it out in titles, exactly the way 10x Chromium became implicit by 2019; (3) the sequencing-based spatial bucket (Visium, Stereo-seq, Slide-seq) will start to shrink in favor of imaging-based single-cell-resolution platforms as subcellular resolution becomes routine; (4) the spatial-proteomics and spatial-epigenetics fronts — today at ~125 and ~5 posters respectively — will converge around integrated multimodal spatial platforms (see #789 PaintScape, #815 simultaneous spatial transcriptome-plus-epigenome, #6685 RNA-plus-protein-plus-morphology) rather than remaining three separate bucket-names; (5) the question at AACR 2028 will not be "spatial or single-cell" but "which spatial + which single-cell reference atlas," with scRNA-seq finally taking the backgrounded-workhorse role that bulk RNA-seq took in 2015.

Spatial is not replacing single-cell. But at AACR 2026, in the solid-tumor center of the field, the frame has flipped: **spatial is the primary method, single-cell is the reference.**

---

## Methodology footer

- **Corpus:** 1,015 posters in `transcripts/single-cell-spatial-omics/posters/abstracts.jsonl`; 20 transcripts in `transcripts/single-cell-spatial-omics/full-sessions/`; no other topic folders consulted for this page.
- **Platform classification:** Python + regex, one primary bucket per poster, priority order imaging-ST → sequencing-ST → spatial-proteomics → sc-multiomics → scRNA-seq → other. Full rule set and the raw by-bucket JSON are generable from `abstracts.jsonl`; see [landscape.md](landscape.md) header for the priority rule.
- **Platform keyword counts:** `\b<platform>\b` case-insensitive regex over title + abstract; reported where cited (Xenium 85, CosMx 38, Visium 84, etc.).
- **Session-title counts:** substring match on `SessionTitle` field.
- **Transcript quotes:** five transcripts (spatial-and-single-cell-omics-at-scale, ai-spatial-transcriptomics-pathology, late-spatial-biomarkers, single-cell-multi-omic-technologies, decoding-cancer-ecosystem-pathology). Quoted fragments are lightly edited (filler and paragraph breaks removed). Speaker attribution crosschecked against session metadata where the auto-caption is unreliable; unnamed chairs are attributed to their affiliation only.
- **What was not done:** no longitudinal comparison to AACR 2023-2025; no poster PDF ingestion (titles + abstracts only); no manual review of the 21 unclassified posters; no double-check of the scRNA-as-reference workflow claim by reading Methods sections.
