# Aviv Regev (keynote ★) — when quantity becomes quality: toward the virtual cell and the lab-in-the-loop

**Speaker:** **Aviv Regev** — Genentech (formerly Broad Institute). (Long-form keynote + extended Q&A with Rahul Satija; the day was framed as a ~15-year retrospective of single-cell genomics.)
**Official title:** "From Cell Atlases to Medicines, with AI"
**Slot:** SCGD26, Jun 12, 2026 — 2:00–2:45 PM EDT keynote
**Recording:** SCGD26 livestream (YouTube) — verify archived link
**Status:** Captured from session transcript

## Thesis

Single-cell genomics began as a **quality** problem (look at everything precisely). Regev's argument: at sufficient **scale, quantity becomes a new quality** — enough noisy data lets AI models systematically infer the rest. The arc runs from atlases → algorithms that find good representations → systematic **perturbation** ("lab in the loop") → **multimodal** generation → **drug discovery / clinic in the loop**, building toward a mechanistically grounded **virtual cell**.

## Atlases + algorithms (find the biology)

- Hundreds of millions of single human cells profiled (NucSeq, DroNc-seq, INTACT-seq lineage). Algorithms turn noisy scale into clusters (cell types), trajectories/optimal transport (dynamics), covariation (gene programs), and spatial/interaction structure.
- **[sc-linker](https://www.nature.com/articles/s41588-022-01187-9)** (Jagadeesh, Dey, … Alkes Price, Regev; *Nat Genet* 2022) links scRNA gene programs to GWAS/heritability across 60 diseases — cell-type, disease-progression, and pathway programs (e.g. Alzheimer's: monocyte program / microglial ApoE-ApoC1-TREM2 progression / apelin-signaling pathway).
- **Gut/ENS atlas:** new dissociation + label-free enrichment recovered ~1,500 enteric neurons; many CNS-disorder risk genes (Hirschsprung, ASD, Parkinson's) are expressed in **enteric** neurons — a more accessible read-out tissue.
- **Aging brain atlas** (Naomi Habib, Phil De Jager): 95 subsets; **causal modeling** orders microglia-12 → Aβ → microglia-13 → tau → astrocyte-10 → cognitive decline; patient-embedding splits a **progressive-AD** axis vs. an **alternative-brain-aging** axis with distinct multicellular communities.
- **[DIALOGUE](https://www.nature.com/articles/s41587-022-01288-0)** (Livnat Jerby-Arnon & Regev; *Nat Biotechnol* 2022): cell-type-specific **multicellular programs** that covary across niches/patients even from single-cell data.
- **Cross-cell-type QTLs** (380k ILCs, 274 outbred mice): >half of trans-QTLs harbor genes expressed in a *different* cell type (NMU in enteric neurons → ILC2; SOX9 in enterocytes → IL-22 program) — causal effects across cells.

## Lab-in-the-loop (perturb → model → design)

- **Random-sequence Oracle:** ~100M random promoters in yeast → transformer (2018) → design extreme high/low expressers (Karl de Boer/Eilon Sharon lineage). **Perturb-seq** circuits for dendritic cells; in vivo Perturb-seq for ASD genes (15/35 converge on 6 programs across 4 cell types); brain-organoid ASD models (Levin/Arlotta) converging on accelerated GABAergic neurogenesis with genetic-background modifiers.
- **Autonomous agents:** **[Biomni](https://biomni.stanford.edu/)** (with Jure Leskovec, Stanford; [preprint](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1)) for autonomous biomedical analysis; a **spatial agent** ([Genentech **SpatialAgent** / STAgent](https://github.com/Genentech/SpatialAgent), [preprint](https://www.biorxiv.org/content/10.1101/2025.04.01.646731)) that beats average human analysts and pairs best with one. *(Phonetic transcripts "CoCo"/"Orion" not separately confirmed — the published spatial agent is SpatialAgent.)*
- **Foundation models for generation across modalities:**
  - **[SCHAF](https://www.biorxiv.org/content/10.1101/2023.03.21.533680v1.full)** (Single-Cell omics from Histology Analysis Framework) — generate spatial transcriptomics / spatially-resolved scRNA from an **H&E** stain (paired/unpaired; metastatic breast, lung cancer) — "translating languages" H&E→RNA, leveraging the millions of existing H&E slides for pretraining.
  - **[PerturbView](https://www.nature.com/articles/s41587-024-02391-0)** + MOSCATO — optical pooled screens (in situ sequencing of perturbations) in primary cells/tissue (cheaper, ~3–10× more perturbations/cells); AI ties imaging morphology to Perturb-seq RNA; **generate unmeasured Perturb-seq from PerturbView**, validated by a held-out secondary screen of 117 never-measured perturbations.
  - **Iterative Perturb-seq** — model-selected ~600 most-informative pairwise combinations per round beat random pairs at equal data (combinatorial space is astronomically large; 5-way over 20k genes = 10²¹ cells).

## Clinic-in-the-loop (drug discovery → patient)

Targets (Recursion collaboration: pathways + small molecules), indications (patient samples for liabilities/specificity), modality (encoder/generative models for small molecules + antibodies), and a **personalized BioNTech cancer vaccine** (neoantigen presentation model; Phase-1 pancreatic — immune responders relapse-free significantly longer). Framing: drug R&D success LI→launch is ~1–2%, so even a 2× improvement is enormous; you're only as strong as your weakest link, so every step merits effort.

## Q&A highlights (with Rahul Satija)

- **How many patients for multicellular communities?** Not as many as feared — **thousands**, scaling with variant rarity / effect size; spatial data adds within-sample reproducibility; and **H&E** gives tens of millions of archival samples for pretraining.
- **Virtual-cell bar:** a model whose internals are **mechanistically anchored** (causal), not just an accurate black box.

## Connections to the corpus

- The corpus's central **virtual-cells** thesis — see AACR [virtual-cells](../../aacr-2026/topics/virtual-cells/) and [Anshul Kundaje — ChromBPNet](anshul-kundaje-chrombpnet.md) (the same "interpret, don't just predict" stance). Perturb-seq overlaps [Xin Jin](xin-jin-in-vivo-perturbseq.md) and [Alex — VIP Perturb-seq](alex-vip-perturbseq.md). H&E→omics overlaps the foundation-models-for-pathology AACR [bioinfo-tools](../../aacr-2026/topics/bioinfo-tools/) thread.

## Verify / open questions

- **MOSCATO** as paired with PerturbView is *not* yet confirmed. A method named MOSCATO exists (supervised feature selection for multi-omic single-cell data, [PMC9351124](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9351124/)) but its identity as the imaging↔Perturb-seq integration layer Regev described is unverified — leave flagged.
- Phonetic agent code-names "CoCo"/"Orion" not separately confirmed (published spatial agent = SpatialAgent/STAgent).
- Exact patient-count framing for multicellular communities; archived YouTube recording link.

## Sources

- Event/schedule (title, affiliation, slot): https://satijalab.org/scgd26/
- sc-linker — *Nat Genet* 2022: https://www.nature.com/articles/s41588-022-01187-9
- DIALOGUE — *Nat Biotechnol* 2022: https://www.nature.com/articles/s41587-022-01288-0
- SCHAF (H&E→omics) — bioRxiv 2023: https://www.biorxiv.org/content/10.1101/2023.03.21.533680v1.full
- PerturbView — *Nat Biotechnol* 2024: https://www.nature.com/articles/s41587-024-02391-0
- Biomni — biomni.stanford.edu / bioRxiv 2025: https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1
- SpatialAgent (STAgent) — Genentech / bioRxiv 2025: https://github.com/Genentech/SpatialAgent · https://www.biorxiv.org/content/10.1101/2025.04.01.646731
