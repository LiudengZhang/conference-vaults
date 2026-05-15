# Single-Cell Genomics 2026 — Program Notes

Pre-meeting prep covering the GRC Single-Cell Genomics (May 10–15, Les Diablerets) and Wellcome Single Cell Biology (Jun 10–12, Hinxton). Written mid-GRC (May 11, 2026) when the GRC is in-session but closed-door and Wellcome is a month out with the speaker list public since Apr 22.

## Dates and venues — at-a-glance

| Meeting | Dates | Venue | Format | Capacity | Status |
|---|---|---|---|---|---|
| **GRC SCG (GRS)** | Sat–Sun May 9–10, 2026 | Les Diablerets Conference Center, Eurotel Victoria, Switzerland | In-person, single-track | ~50 | Closed (application deadline was Apr 11) |
| **GRC SCG (main)** | Sun May 10 – Fri May 15, 2026 | Les Diablerets, same venue | In-person, single-track, closed-door | ~200 | **In-session this week; oversubscribed** |
| **Wellcome SCB** | Wed–Fri Jun 10–12, 2026 | Wellcome Genome Campus, Hinxton, UK | Hybrid (in-person + virtual) | ~250 in-person | In-person reg closes May 11; virtual closes Jun 1 |

Travel: GRC participants typically fly into Geneva (GVA) or Zurich (ZRH), then 90-min rail to Aigle → cogwheel to Les Diablerets. Wellcome attendees fly into LHR/STN/LTN, then ~50 min by car/bus to Hinxton. Same-week back-to-back attendance is unusual but plausible for senior PIs; expect the same ~20–30 people at both meetings.

## Chair / committee

- **GRC SCG 2026 chair:** Angela Oliveira Pisco (CZ Biohub formerly; current role per LinkedIn — Insitro). Co-organizer of GRC SCG 2024 with Zhuang, Fan, and Xie. Chair-elect for the GRS strand is not publicly named but historically a rising-PI from the same network.
- **Wellcome SCB 2026 organizing committee:** Leeat Keren (Weizmann — spatial proteomics / MIBI), Cole Trapnell (UW — Monocle / sci-RNA-seq lineage), Roser Vento-Tormo (Sanger — tissue atlases / CellPhoneDB / spatial). All three have AACR-axis publications. Trapnell + Vento-Tormo are recurring committee members across years; Keren is new for 2026.

## Anticipated top-5 themes for the 2026 SCG cohort

Cross-cutting between the two meetings, ranked by expected oral-talk count + AACR overlap:

1. **Foundation models for single-cell omics.** scGPT-v2 and Geneformer-v2 successor work, perturbation-prediction foundation models (Bunne's CellFlow lineage at EPFL), Universal Cell Embeddings + scPRINT updates. The GRC subtitle ("Accelerating Medical Discovery With Single Cell Omics and Machine Learning") and the GRS topic ("AI and ML for Single-Cell and Spatial Omics") both center this. AACR overlap: AACR 2026 agentic-AI dossier + foundation-model sessions.
2. **Spatial transcriptomics at scale.** Visium HD analysis tooling, Xenium-native pipelines, CosMx integration, MERSCOPE/MERFISH analysis, ISS (Nilsson). The Wellcome "spatial technologies" session and the GRC "Spatial and Proteomics Analysis" session both anchor this. AACR overlap: the AACR single-cell-spatial topic has 8 strong-fit sessions cross-listed.
3. **Multimodal single-cell + integration.** CITE-seq successors, Multiome + methylation + RNA, ATAC+RNA at scale, proteo-genomics. The Wellcome "beyond transcriptomics" session and the GRC "Epigenomics" + "3D Genomics" sessions. AACR overlap: AACR 2026 hematology + multimodal sessions.
4. **Lineage tracing and perturbation atlases.** Recording-based lineage (Loveless at Rice, Gagnon at Utah), Perturb-seq successors, drug-response atlases. Wellcome speakers center this; the GRC "Single-Cell Modeling" session will cover the analytical side. Crosses with the EMBO Lineage Tracing 2026 meeting (Mar 2026, separate).
5. **Cancer single-cell with clinical translation.** Single-cell atlases of disease states, biomarker discovery from scRNA / spatial, clinical-trial-adjacent applications. The GRC "Applications in Medicine" session is explicitly this. Direct AACR overlap: AACR 2026 has 8 single-cell + spatial sessions and 1,015 poster abstracts in this topic.

## Cross-vault overlap watch

Authors and tools known or strongly expected to appear at both SCG-2026 and elsewhere in the corpus:

### High-confidence cross-links (Wellcome speakers, public)

| Person | SCG-2026 role | Other corpus appearances |
|---|---|---|
| Cole Trapnell | Wellcome organizer + talk | AACR 2026 (single-cell-spatial topic Sun 4/19 + Mon 4/20 sessions cite Monocle pseudotime); EuroBioC indirectly (Monocle has a Bioc wrapper); CSHL BDS 2026 (spatial session likely cites sci-Space) |
| Roser Vento-Tormo | Wellcome organizer + talk | AACR 2026 (CellPhoneDB used in 20+ poster abstracts in single-cell-spatial topic); HCA / HuBMAP infrastructure axis |
| Leeat Keren | Wellcome organizer + large-scale | AACR 2026 (MIBI + spatial-proteomics — Mapping Neural-Immune Circuits session 4/18, Spatial Biomarkers session 4/21); ESMO 2026 (clinical spatial-proteomics) |
| Charlotte Bunne | Wellcome computational | RECOMB 2026 (ML for biology); ISMB 2026 MLCSB; AACR 2026 agentic-AI dossier (foundation-model adjacency); ICML 2026 (likely) |
| Mats Nilsson | Wellcome spatial | AGBT 2026 (ISS platform reference); AACR 2026 spatial sessions |
| Sizun Jiang | Wellcome spatial | AACR 2026 (3D Tissue Imaging + Spatial Biomarkers); SITC 2026 (immune spatial) |
| Céline Vallot | Wellcome beyond-transcriptomics | AACR 2026 (epigenetics + cancer single-cell sessions); HTAN |
| Ido Amit | Wellcome keynote | AACR 2026 (MARS-seq + immune atlases cited in multiple sessions); ASH 2026 (clinical hematology atlases) |

### Anticipated cross-links (GRC, will confirm post-meeting)

GRC speaker list is closed. Based on the published session structure + the AI/ML subtitle + Pisco's network at Insitro / CZ Biohub, expected speakers include some subset of: Aviv Regev (Genentech), Dana Pe'er (MSKCC), Fabian Theis (Helmholtz Munich — scGen / scVI line), Bo Wang (Toronto — scGPT), Christina Leslie (MSKCC — chromatin), Rahul Satija (NYGC — Seurat), Caleb Lareau (MSK — scATAC), Jeffrey Janes / Anjali Tarun / Yan Wang (CELLxGENE-adjacent), and a Sanger contingent (Vento-Tormo crossover, plus Sarah Teichmann's lab line). Confirm post-meeting from preprint signals and Bluesky.

### Tool / package cross-links to watch

Tools where SCG-2026 talks could plausibly mention or update them, with the corresponding AACR / EuroBioC / sibling-vault entry:

- **scGPT / Geneformer / scFoundation** ↔ AACR 2026 agentic-AI dossier (foundation-models surface)
- **CellPhoneDB / CellChat / NicheNet** (cell-cell communication) ↔ AACR 2026 single-cell-spatial topic (heavy use in TME sessions: Macrophages 4/18, Neural-Immune Circuits 4/18, Fibroblast Dynamics 4/18)
- **SpatialData / DESpace / OSTA / spatialFDA** ↔ EuroBioC 2025 (Marconato, Cai, Dong+Patrick, Emons)
- **Voyager / Visium-HD analysis** ↔ CSHL BDS 2026 spatial session (anticipated)
- **scVI / scANVI / scArches** ↔ ICML / NeurIPS appearances + AACR sessions using batch-corrected atlases
- **CellTypist** ↔ AACR 2026 atlas-annotation poster pipelines (Vento-Tormo)
- **Monocle3 / sci-RNA-seq / sci-Space** ↔ AACR 2026 trajectory analyses (Trapnell)
- **cell2location / Tangram / CytoSPACE** ↔ AACR 2026 spatial-deconvolution methods
- **CELLxGENE Census / HCA / Tabula Sapiens / HTAN** ↔ atlas-infrastructure cross-cutting

## Information-extraction strategy

- **GRC (May 10–15, off-the-record):** wait 2–6 weeks post-meeting, then scrape bioRxiv for "Gordon Research Conference" or "GRC" or "Single-Cell Genomics" in acknowledgements/funding sections. Cross-reference with Pisco's lab Bluesky / X feed for any blessed sharing. Most reliable signal: preprints that drop May 20 – Jul 5 from labs known to have attended.
- **Wellcome (Jun 10–12, hybrid):** scrape Wellcome event page on Jun 5 for finalized schedule + abstract titles (typically posted ~1 week before). Tune #SingleCell26 on Bluesky/X during the meeting. Wellcome keynotes go to YouTube channel `@WellcomeGenomeCampus` post-meeting; selected short talks sometimes too. Speaker slides occasionally to Zenodo or lab sites.
- **Post-meeting bulk extraction (Jul 2026):** one pass after both meetings + 4 weeks of preprint drops, building ~30–40 tool pages. Use the EuroBioC 2025 / CSHL BDS 2026 pattern — codex-driven extraction once the template is locked.

## What is and isn't covered

- **Covered:** GRC Single-Cell Genomics 2026 + GRS, Wellcome Single Cell Biology 2026.
- **Not covered (separate vaults or out-of-scope):**
  - **EMBO Lineage Tracing 2026** (Mar 2026, Heidelberg) — separate EMBO meeting, captured as side-reference in tools/lineage pages but not a vault yet.
  - **3rd Probing Human Disease using Single-Cell Technologies** (Fusion Conferences, Mar 1–4, 2026, Playa Mujeres) — industry-leaning, AACR-cancer-axis overlap exists but small attendance + low public-record makes a vault not worth the effort.
  - **EMBL Brain (epi)genome Symposium** (Apr 21–24, 2026, Heidelberg) — neuro-focused, captured as side-reference in any neuro-overlap tool pages but not a vault.
  - **Advances in Single Cell and Spatial Biology 2026** (commercial conference series) — sponsor-heavy, low signal-to-noise, not in scope.
  - **CSHL Single Cell Analyses** — does not run in 2026 (CSHL BDS 2026 occupies the methods slot; see [`cshl-bds-2026/`](../cshl-bds-2026/)).
  - **Joint ASCB-EMBO 2026** (Dec 2026, San Diego) — broad cell biology, single-cell is a small fraction; possible separate vault if a single-cell track is announced.
  - **Keystone single-cell symposia** — none in 2026 with a single-cell-anchor title; the 2026 Keystone calendar has spatial-biology-adjacent meetings but no SCG-flagship slot.

## Calibration: what could go wrong

- **Pisco / GRC discretion is tighter than expected.** If no preprints surface with "GRC SCG 2026" acknowledgement and Bluesky stays quiet, the GRC half of this vault stays sparse. Fallback: build the Wellcome half thoroughly and treat the GRC half as a watch-list rather than a tool index.
- **Wellcome program changes between Apr 22 and Jun 10.** Some speaker drops always happen; final session-to-day mapping isn't finalized until ~1 week pre-meeting. Pre-scaffolded tool pages should reference "Day TBD" until Jun 5 schedule scrape.
- **Foundation-model hype peaking.** If GRC and Wellcome both end up being 50%+ foundation-model talks, the tool index becomes lopsided. Counter-axis: make sure spatial / multimodal / lineage / non-model entries get equal extraction effort.
- **Industry talks invisible.** Neither meeting has a paid sponsor track, so 10x / Vizgen / Curio / Singleron / Element / Parse Biosciences platform updates won't appear in talks. Those are captured in [`agbt-2026/`](../agbt-2026/) and trade-press writeups; cross-link from SCG tool pages where relevant rather than re-extracting.

## Sources

See [`index.md` → Sources](index.md#sources). Additionally, post-meeting:

- bioRxiv search filter: `("Gordon Research Conference" OR "GRC") AND ("single-cell" OR "single cell" OR "scRNA")` for May 15 – Jul 15, 2026 window.
- bioRxiv search filter: `"Wellcome Single Cell Biology" OR #SingleCell26` for Jun 10 – Jul 31, 2026 window.
- Bluesky search: `#SingleCellGenomics #SingleCell26 #SCG2026` from May 10 onward.
- Pisco lab site / X / Bluesky: track for any blessed-sharing posts.
- Wellcome YouTube channel: `@WellcomeGenomeCampus` for post-meeting keynote uploads.
