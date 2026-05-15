# GBCC2025 — Program Extracted (working notes)

**Internal-use working file.** Source for the bulk tool-page generation pass. Not for end-reader consumption — formatting is utilitarian. Sources: `gbcc2025.bioconductor.org/program/scientific_program/`, `gbcc2025.bioconductor.org/program/glance/`, Galaxy June 2025 newsletter meeting report, Bioconductor "Bringing Bioconductor to Galaxy" CoFest recap.

**Tag legend:**
- `[BIOC]` — clearly a Bioconductor R package (has or will have a Bioconductor page)
- `[GALAXY]` — Galaxy tool / workflow / platform feature (XML wrapper or platform-side software)
- `[INTEGRATION]` — cross-platform scaffolding (Bioc-in-Galaxy, MCP protocols, auto-wrapping)
- `[METHOD]` — methods talk; package not clearly named in title (recheck against full abstract)
- `[COMMUNITY]` — community / training / global-access talk; no tool anchor
- `[?]` — unclear from title alone; needs abstract-book lookup

**Sparse-coverage flags:**
- `gbcc25_AbstractBook.pdf` (CSHL-hosted) returned 404 at fetch time → full abstracts not yet ingested; tool/package mentions hidden in abstract bodies are missed
- GBCC2025 YouTube playlist URL referenced in the meeting report but not surfaced in our crawl → video-link column will stay TBD until the playlist is found
- Slide DOIs (Zenodo) typically posted 2–4 weeks post-conference; recheck after Aug 2025

---

## Day 1 — Mon Jun 23, 2025 (arrival)

- 5–7 PM Dinner
- 7–8 PM Opening Ceremony [no talks indexed]
- 8–9 PM "GBCC2025 LIVE!" — special evening session

---

## Day 2 — Tue Jun 24, 2025

### Keynote 1 (9:00–10:00, Grace Auditorium)
- **Sergei L. Kosakovsky Pond** (Temple University) — "Interactive Genomic Analytics with responsive notebooks, in-the-browser computation, and AI-assisted development" — `[METHOD]` (Pond is the HyPhy developer; HyPhy is implicit ecosystem context, not necessarily a launch artifact)

### Oral Session 1 (10:30–12:00, Grace Auditorium; chair Sehyun Oh)
1. **Junhao Qiu, Jeremy Goecks** — "Galaxy All-in-One Agent: A Unified Natural Language Interface for Cross-Galaxy Data Analysis" — Tool: **GAIA** — `[GALAXY]` `[INTEGRATION]`
2. **Dannon Baker, Junhao Qiu, Jeremy Goecks, Mike Schatz** — "Introducing GalaxyMCP: Integrating AI Assistants with Galaxy Through the Model Context Protocol" — Tool: **GalaxyMCP** — `[GALAXY]` `[INTEGRATION]`
3. **Jayadev Joshi, Fabio Cumbo, Daniel Blankenberg** — "Automated integration of R/Bioconductor tools into Galaxy" — `[INTEGRATION]` (no single package name — auto-wrapping pipeline)
4. **Marius van den Beek** — "User-Defined, Safe, and Rapidly Deployable Galaxy Tools with Embedded Type-Safe Editing" — `[GALAXY]` (YAML tool authoring system)
5. **Aysam Guerler, Ahmed Awan, Alireza Heidari, Bjoern Gruening, et al.** — "Bringing Data to Life: Galaxy's New Visualization Framework" — `[GALAXY]`
6. **Leandro Liborio, Subindev Devadasan, et al.** — "Managing materials science workflows with Galaxy at STFC" — `[GALAXY]` `[COMMUNITY]` (domain transfer; case study)
7. **Vincent J Carey** — "Language-agnostic strategies for genomic data representation in Bioconductor" — `[BIOC]` `[METHOD]` (no specific package; framework talk)
8. **Leonid Kostrykin, Beatriz Serrano-Solano, Riccardo Massei, Karl Rohr** — "Streamlining the User Experience for Reproducible Image Analysis in Galaxy" — `[GALAXY]`
9. **Stephen L Mosher, Michael C Schatz, Jonathan Lawson, Robert Carroll** — "Enabling Genomic Research at Scale with NHGRI AnVIL: A Cloud Platform for Genomic Data Analysis" — Tool: **AnVIL** — `[GALAXY]` `[INTEGRATION]` (cloud platform)

### Workshops (1:00–2:30, concurrent)
- Marius van den Beek — "Exploring Galaxy Workflows" — `[GALAXY]` workshop
- Stephen Salerno — "Inference Challenges and Corrections for AI-Predicted Outcomes" — `[METHOD]` workshop (post-prediction inference)
- John Davis, Ahmed Awan — "Galaxy Backend Architecture and Software Development" — `[GALAXY]` workshop
- Greg Watson — "Deploying Autonomous Galaxy Workflows for Materials Laboratories" — `[GALAXY]` workshop
- Ellis Patrick — "Making Space Count - Strategies for Analysing Spatial Omics Data" — `[BIOC]` workshop (Patrick's spatial-omics ecosystem)

### Oral Session 2A (3:00–5:00, Bush Hall; chair Jenny Drnevich)
1. **Ahmed H Awan, Dannon Baker, et al.** — "From Upload to Execution: A Unified Galaxy Workflow Run Interface" — `[GALAXY]`
2. **John Chilton, Marius van den Beek, Ahmed Awan** — "More Usable and More Powerful Galaxy Dataset Collections" — `[GALAXY]`
3. **Junhao Qiu, Jeremy Goecks** — "AI-augmented data analyses in Galaxy" — `[GALAXY]` `[INTEGRATION]` (likely GAIA-adjacent; recheck)
4. **Bryan Raubenolt, Akhil Mohan, et al.** — "Benchmarking Quantum Machine Learning Models in Galaxy" — `[GALAXY]` `[METHOD]`
5. **Jamie Park** — "Leveraging Deep Learning with torch in R for Next-Generation Epigenetic Clock Development" — Tool: **torch (R)** — `[BIOC]` `[METHOD]` (epigenetic clock case study)
6. **Paulo Cilas Morais Lyra Junior, Junhao Qiu, et al.** — "The Galaxy-ML2 tool suite: Using Galaxy to promote best practices in machine learning for biomedical data science" — Tool: **Galaxy-ML2** — `[GALAXY]`
7. **Gregory R Watson** — "NOVA: Leveraging Galaxy for Neutrons Scattering Data Analysis and Visualization" — Tool: **NOVA** — `[GALAXY]` (cross-domain)
8. **Fabio Cumbo, Jayadev Joshi, Daniel Blankenberg** — "Towards the automatic integration of tools in Galaxy: the anvi'o suite and a new AI-driven automation pipeline" — Tool: **anvi'o (auto-wrapped)** — `[INTEGRATION]`
9. **Paul De Geest, Sanjay Srikakulam, et al.** — "Dynamic meta-scheduling in Galaxy with TPV Broker for smarter workload distribution" — Tool: **TPV Broker** — `[GALAXY]`
10. **Marisa J Loach, Daniel M Johnson, Wendi Bacon** — "One Million Heart Cells: Integrating Public Data on Galaxy to Explore How Cardiomyocytes Change in Atrial Fibrillation" — `[GALAXY]` `[COMMUNITY]` (case study; single-cell + Galaxy)
11. **Angelo Velle, Francesco Patanè, Chiara Romualdi** — "gINTomics, a powerful Bioconductor package for multiomics data integration and visualization" — Package: **gINTomics** — `[BIOC]`
12. **Pavankumar Videm, Paul Zierep, et al.** — "Bioconductor-R-Shiny Applications on Galaxy" — `[INTEGRATION]` (Shiny-on-Galaxy)

### Oral Session 2B (3:00–5:00, Grace Auditorium; chair Vincent Carey)
1. **Pascal Belleau, Xintong Li, Astrid Deschênes, et al.** — "Robust ancestry inference from challenging human molecular data with RAIDS" — Package: **RAIDS** — `[BIOC]`
2. **Katherine T Do, Subina Mehta, et al.** — "Meta-iPep: A metaimmunopeptidomics pipeline implemented within Galaxy platform to characterize HLA-bound microbial peptides for immunotherapy" — Tool: **Meta-iPep** — `[GALAXY]` (pipeline)
3. **Kasper D Hansen** — "Analyzing allele-specific methylation using Oxford Nanopore long-read DNA sequencing" — `[BIOC]` `[METHOD]` (no clear package name in title; check abstract — Hansen maintains several methylation packages)
4. **Stefania Pirrotta, Laura Masatti, et al.** — "Public gene expression cancer signatures across bulk, single-cell and spatial transcriptomics data with signifinder Bioconductor package" — Package: **signifinder** — `[BIOC]`
5. **Pariksheet Nanda, Jason E Shoemaker** — "Host cell signaling during viral infection network perturbation analysis" — `[METHOD]` (no clear package — recheck abstract)
6. **Grace E Kenney, Rintsen N Sherpa, Alan P Boyle, Douglas H Phanstiel** — "SEMplR: An R package for predicting the effects of genetic variation on transcription factor binding" — Package: **SEMplR** — `[BIOC]`
7. **Xiuwen Zheng, Raven Chen** — "Enhancing rare variant analysis in biobanks: whole-genome annotation using GDS files" — `[BIOC]` (Zheng maintains the GDS / SeqArray ecosystem; check abstract for specific package)
8. **Aidan H Lakshman, Erik S Wright** — "Orthology Detection at the Scale of Modern Genomics" — `[BIOC]` `[METHOD]` (Wright maintains DECIPHER + SynExtend; check abstract)
9. **Lambda Moses, Bianca Dumitrascu** — "Multiscale analysis of lung adenocarcinoma spatial transcriptomics data" — `[BIOC]` `[METHOD]` (Moses is Voyager / SpatialFeatureExperiment maintainer; check abstract)
10. **Pascal Belleau, Astrid Deschênes, et al.** — "Deciphering CLEC12A Negative Regulation of Neutrophil Activation by Network and Functional Enrichment Analyses" — `[METHOD]` (case study)
11. **Tyler Collins, Alex Ostrovsky, Michael Schatz** — "Broadening Metagenomic Horizons in Galaxy: Introducing the HiFi-MAG Pipeline, New Profilers, and Insights from BioDIGS" — Tool: **HiFi-MAG Pipeline** — `[GALAXY]`
12. **Beatriz Campillo, Michael Love** — "Visualizing and analyzing differential transcript usage" — `[BIOC]` `[METHOD]` (Love maintains DESeq2/tximeta/fishpond; check abstract for specific package — likely fishpond or new tool)

### Evening
- 5–6 PM wine-and-cheese networking
- 6–7 PM dinner
- 7:30–9:30 PM Poster Session 1 — `[POSTERS]` 25+ posters (out of 50+ total); not enumerated here

---

## Day 3 — Wed Jun 25, 2025

### Keynote 2 (9:00–10:00, Grace Auditorium)
- **Charlotte Soneson** (Friedrich Miescher Institute) — "From classes to community — How Bioconductor has advanced my research" — `[BIOC]` (career-arc keynote; Soneson is a prolific Bioc maintainer — also speaks at EuroBioC2025 footprintR talk)

### Lightning Talks (10:30–11:15) — 11 speakers
Per the Galaxy newsletter recap:
- **Ali Imami** — Kinome analysis R package — Package: **(name TBD)** — `[BIOC]`
- **James Eapen** (Van Andel Institute) — "iscream: fast and efficient BED file queries" — Package: **iscream** (Rcpp + htslib) — `[BIOC]`
- **Sunita Sharma** — Ciliary gene regulation — `[METHOD]` `[?]`
- **Stefano Mangiola** (Adelaide University) — Tidyomics package — Package: **Tidyomics** — `[BIOC]` (also gives Oral Session 4 talk; lightning was likely a teaser)
- **Robert Castelo** (Pompeu Fabra) — atena (transposable element analysis) — Package: **atena** — `[BIOC]`
- Plus 6 more covering: tidy-style interfaces for SummarizedExperiment objects (Landis/Love-adjacent? plyxp gets a full Oral Session 5 slot — distinct talk?), Bioconductor microbiome tools, ML interpretation, credential security in Galaxy, FAIR-EASE Earth-system workflows, Galaxy-E ecology extensions
- **`[?]`** — full lineup of all 11 names not surfaced in current crawl; flagged for follow-up via the abstract-book PDF

### BoF Session 1 (11:15–12:00) — `[COMMUNITY]` self-organized; topics not all indexed (workflow reproducibility, ML integration mentioned as examples)

### Oral Session 3 (1:00–2:00, Grace Auditorium; chair Lambda Moses)
1. **Marius van den Beek** — "The Intergalactic Workflow Commission: Standardizing, Testing, and Distributing Reproducible Galaxy Workflows" — Tool: **Intergalactic Workflow Commission (IWC)** — `[GALAXY]`
2. **Ilaria Billato, Marcel Ramos Perez, et al.** — "A standardized R/Bioconductor framework for integrative analysis of histopathological images with multi-omics data" — `[BIOC]` `[METHOD]` (Ramos Perez maintains MultiAssayExperiment / curatedTCGAData; recheck abstract for specific package — Billato also presents at EuroBioC2025)
3. **Cameron Watson, Luke Sargent, Allison L Creason** — "Advancing digital pathology with Galaxy: Tools for histological imaging foundation models" — `[GALAXY]` `[METHOD]`
4. **Nicholas J Eagles, Sarah E Maguire, et al.** — "Computational considerations for analysis of Visium HD: A Bioconductor user's perspective" — `[BIOC]` `[METHOD]` (Eagles is from LIBD; check abstract for specific package — likely SpatialExperiment-extended)
5. **Samuel Gunz, Mark D Robinson** — "sosta: a framework to analyze anatomical structures from spatial omics data" — Package: **sosta** — `[BIOC]`
6. **Delphine Lariviere, Erick Duarte, et al.** — "Universally accessible interactive curation workflows for large genome assembly" — `[GALAXY]`

### Workshops (2:00–3:30, concurrent)
- Daniel Blankenberg — "Streamlining Bioinformatics: Adding Bioconductor Tools in Galaxy" — `[INTEGRATION]` workshop (links to GSVA wrapper + auto-integration)
- Tuomas Borman — "Orchestrating Microbiome Analysis with Bioconductor" — Package: **mia** (and miaverse) — `[BIOC]` workshop (Borman also runs the analogous EuroBioC2025 workshop)
- Pratik Jagtap — "Immunopeptidogenomics Pipeline in Galaxy for MHC-Bound Neoantigens" — `[GALAXY]` workshop
- Frederick Tan — "AnVIL: Secure, scalable computing for controlled access data" — `[GALAXY]` `[INTEGRATION]` workshop
- Ann Loraine — "Galaxy History Based Alignment Comparison in IGB" — Tool: **IGB (Integrated Genome Browser)** — `[GALAXY]` workshop

### Oral Session 4 (4:00–5:00, Grace Auditorium; chair Mike Love)
1. **Maria Doyle, Umar Ahmad, et al.** — "Empowering Bioinformatics in Africa through Bioconductor: Expanding Training and Community Engagement" — `[COMMUNITY]`
2. **Carol Gauthier, Charles Coulombe, et al.** — "Building UseGalaxy Capability in Canada" — `[COMMUNITY]` `[GALAXY]`
3. **Subina Mehta, Katherine Do, et al.** — "Mass Spectrometry-Centered Multi-Omics: Advancing Galaxy Training Materials for Integrated Analysis and Community Adoption" — `[COMMUNITY]` `[GALAXY]`
4. **Natalie Kucher, Michael C Schatz, et al.** — "Training and education in the cloud with the NHGRI AnVIL" — `[COMMUNITY]` `[GALAXY]`
5. **Carolina O Santana, Pieter Spealman, Gabriel Perron** — "Molecular ecology at the sertão - Using Galaxy to empower research in developing communities" — `[COMMUNITY]` `[GALAXY]`
6. **Stefano Mangiola** — "Democratising the Analysis of the Human Cell Atlas with Bioconductor" — Package: **Tidyomics ecosystem (tidySingleCellExperiment etc.)** — `[BIOC]` (community + tool talk)

### BoF Session 2 (5:00–6:00) — `[COMMUNITY]` self-organized

### Evening
- 6–8 PM Banquet
- 8–11 PM DJ Party + Galaxy 20th Anniversary Celebration

---

## Day 4 — Thu Jun 26, 2025

### Keynote 3 (9:00–10:00, Grace Auditorium)
- **Jason Williams** (Cold Spring Harbor Laboratory) — "Conquest of Abundance: Genomics in a Time of Plenty" — `[COMMUNITY]` (training equity, access — not a tool talk)

### Oral Session 5 (10:30–12:00, Grace Auditorium; chair Scott Cain)
1. **Justin T Landis, Michael I Love** — "plyxp: reimagining dplyr syntax for SummarizedExperiment objects" — Package: **plyxp** — `[BIOC]`
2. **Tuomas Borman, Leo Lahti** — "Orchestrating Microbiome Analysis with Bioconductor" — Package: **mia / miaverse** — `[BIOC]` (oral version of the workshop)
3. **Stephen Salerno, Jiacheng Miao, et al.** — "Inference with predicted data – what do we do after we have machine learned everything?" — `[METHOD]` (likely IPD / ipd-R; check abstract — Salerno also runs the Day-2 workshop)
4. **John Davis, Alireza Heidari, et al.** — "Simple and Secure Credential Handling for Tools in Galaxy" — `[GALAXY]`
5. **Marie Jossé, Jérôme Detoc, Erwan Bodéré** — "Bridging Earth System Sciences with Galaxy: Two Years of FAIR-EASE" — Tool: **FAIR-EASE** — `[GALAXY]` `[COMMUNITY]`
6. **Stefania Pirrotta, Massimo Bonora, Enrica Calura** — "Dissect mitochondrial activity by transcriptome data with mitology R package" — Package: **mitology** — `[BIOC]` (Pirrotta also presents signifinder in 2B)
7. **Coline Royaux, Marie Jossé, et al.** — "Galaxy-E: Ecology oriented Galaxy initiative, a 2025 update!" — Tool: **Galaxy-E** — `[GALAXY]` `[COMMUNITY]`
8. **John Davis** — "Little errors at big scale: towards efficiency, consistency, and reliability of data in the Galaxy database" — `[GALAXY]` (infrastructure)

### 12:00–1:00 lunch + departure

---

## CoFest — Jun 27–28, 2025 (post-conference, separate registration)

Not part of the main 4-day program but produces concrete tool artifacts that belong in the GBCC vault:
- **GSVA** (Gene Set Variation Analysis) — Bioconductor package wrapped as a Galaxy tool; draft PR open. Speakers: Fabio Cumbo, Jayadev Joshi, Bryan Raubenolt, Daniel Blankenberg. On-site team: Maria Doyle, Gretta Yagudayeva, Charlotte Soneson, Marcel Ramos Pérez. Remote: Robert Castelo. — `[INTEGRATION]`
- Future direction: developer guide for wrapping Bioconductor tools; embedding Shiny apps in Galaxy; "maintainer" field in Galaxy tool XML.

---

## Tool/package shortlist for the bulk extraction pass

Confirmed package/tool name in title (clear `[BIOC]` or `[GALAXY]` candidates for tool pages):

**Bioconductor packages — strong candidates:**
1. **gINTomics** — multi-omics integration (Velle/Romualdi, Day 2 / Oral 2A #11)
2. **RAIDS** — ancestry inference (Belleau, Day 2 / Oral 2B #1)
3. **signifinder** — cancer signatures across bulk/SC/spatial (Pirrotta, Day 2 / Oral 2B #4)
4. **SEMplR** — TF-binding variant effects (Kenney, Day 2 / Oral 2B #6)
5. **sosta** — spatial anatomical structures (Gunz/Robinson, Day 3 / Oral 3 #5)
6. **plyxp** — dplyr for SummarizedExperiment (Landis/Love, Day 4 / Oral 5 #1)
7. **mitology** — mitochondrial activity from transcriptome (Pirrotta, Day 4 / Oral 5 #6)
8. **Tidyomics** (and tidySingleCellExperiment family) — Mangiola, Day 3 lightning + Day 3 / Oral 4 #6
9. **atena** — transposable elements (Castelo, Day 3 lightning)
10. **iscream** — BED file queries via Rcpp+htslib (Eapen, Day 3 lightning)
11. **mia / miaverse** — microbiome (Borman/Lahti, Day 4 / Oral 5 #2 + Day 3 workshop)
12. **torch (in R)** — epigenetic clock case study (Park, Day 2 / Oral 2A #5) — note: torch is established; this is a methods-talk anchor
13. **(Imami's kinome package)** — `[?]` name TBD from abstract book

**Galaxy tools / platforms:**
14. **GAIA** — natural-language Galaxy agent (Qiu/Goecks, Day 2 / Oral 1 #1)
15. **GalaxyMCP** — MCP protocol for Galaxy (Baker/Qiu/Goecks/Schatz, Day 2 / Oral 1 #2)
16. **Galaxy-ML2** — ML tool suite (Lyra Junior, Day 2 / Oral 2A #6)
17. **NOVA** — neutron-scattering on Galaxy (Watson, Day 2 / Oral 2A #7)
18. **TPV Broker** — meta-scheduling (De Geest, Day 2 / Oral 2A #9)
19. **HiFi-MAG Pipeline** — long-read metagenomics (Collins/Schatz, Day 2 / Oral 2B #11)
20. **AnVIL** — cloud platform (Mosher et al., Day 2 / Oral 1 #9 — and Day 3 workshop)
21. **Intergalactic Workflow Commission (IWC)** — workflow standardization (van den Beek, Day 3 / Oral 3 #1)
22. **Meta-iPep** — metaimmunopeptidomics pipeline (Do/Mehta, Day 2 / Oral 2B #2)
23. **FAIR-EASE** — Earth-system workflows on Galaxy (Jossé, Day 4 / Oral 5 #5)
24. **Galaxy-E** — ecology-oriented Galaxy (Royaux/Jossé, Day 4 / Oral 5 #7)
25. **IGB** — Integrated Genome Browser (Loraine, Day 3 workshop)

**Cross-platform / integration scaffolding:**
26. Auto-wrapping pipeline for R/Bioc → Galaxy (Joshi/Cumbo/Blankenberg, Day 2 / Oral 1 #3)
27. anvi'o auto-wrapped suite + AI-driven automation (Cumbo/Joshi/Blankenberg, Day 2 / Oral 2A #8)
28. Bioconductor-R-Shiny-on-Galaxy (Videm/Zierep, Day 2 / Oral 2A #12)
29. **GSVA Galaxy wrapper** (CoFest deliverable — Cumbo/Joshi/Raubenolt/Blankenberg)

**Methods talks worth a tool page once specific package is confirmed via abstract book:**
30. Hansen — allele-specific methylation, ONT long-read (`[?]`)
31. Eagles — Visium HD analysis (`[?]` — Bioc package likely from LIBD's spatialLIBD ecosystem)
32. Moses — multiscale spatial-transcriptomics LUAD (`[?]` — likely Voyager / SpatialFeatureExperiment update)
33. Lakshman/Wright — orthology at scale (`[?]` — likely SynExtend update)
34. Campillo/Love — differential transcript usage (`[?]` — likely fishpond / DRIMSeq-adjacent or new)

**Excluded from tool pages (community / training / case-study only, no clear tool anchor):**
- Doyle (Africa training); Gauthier (UseGalaxy Canada); Mehta (MS multi-omics training); Kucher (AnVIL training); Santana (sertão); Liborio (STFC materials science); Loach (heart-cell case study); Belleau-#10 (CLEC12A case study); Nanda (viral signaling); Williams keynote; Pond keynote (HyPhy implicit); Soneson keynote (career arc, not a launch)

---

## Open follow-ups before bulk extraction

1. **Fetch CSHL `gbcc25_AbstractBook.pdf`** — try alternate paths or contact organizers; needed for the 11 lightning-talk full lineup, the `[?]`-tagged methods talks, and the missing Bioconductor package names in case-study abstracts.
2. **Locate the GBCC2025 YouTube playlist** — meeting report mentions it but URL not surfaced; needed for video links across all tool pages.
3. **Confirm Zenodo DOI deposits** — Bioconductor speakers typically deposit slides 2–4 weeks post-conference; recheck after Aug 2025.
4. **Cross-walk EuroBioC2025 ↔ GBCC2025 talks by same speaker** — Soneson, Mangiola, Castelo, Pirrotta, Borman, Billato, Ramos Pérez at minimum overlap. Cross-link wired both directions in the per-tool pages.
5. **Sponsors / organizers list** — captured in index.md but full sponsor table (Silver: CZI, BMS; Bronze: Limagrain, GalaxyWorks, R Consortium) goes in a footer of the digest if/when written.
