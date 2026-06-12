# Anshul Kundaje — sequence-to-accessibility models (ChromBPNet) on fibroblast reprogramming

**Speaker:** **Anshul Kundaje** — Associate Professor of Computer Science & Genetics, Stanford University. Graduate students **Surag Nair** and **Mohamed Ameen** ("Moe") — co-first authors of the reprogramming paper. Collaboration with Ionis; "Kevin"/Helen.
**Talk title (SCGD26):** "Deep learning the regulatory code of fetal development and cellular reprogramming from single cell chromatin accessibility"
**Slot:** SCGD26, Jun 12, 2026
**Method:** **ChromBPNet** — base-resolution sequence→ATAC-seq deep-learning models + interpretation (DeepLIFT/DeepSHAP, TF-MoDISco)
**Recording:** SCGD26 livestream — paper, data, and interactive browser at the [reprogramming browser](https://kundajelab.github.io/reprogramming-browser/home.html)
**Status:** Captured from session transcript

## Thesis

How is one fixed genome read differently across cell states? Using **Yamanaka (OSKM) reprogramming** of human dermal fibroblasts → iPSCs (Sendai delivery, 14-point time course, scRNA + scATAC), sequence-to-accessibility models give **mechanistic** insight — not just predictions — about how DNA sequence, TF concentration, and motif **affinity** drive chromatin dynamics.

## Setup & models

- ~15 cell states from fibroblast → "high-OSK" → pre-iPSC → iPSC, with off-target trajectories (keratinocyte-like, partially reprogrammed). Endogenous vs. exogenous OSKM separable by isoform structure → the **high-OSK** state has supraphysiological OSKM; iPSC has physiological levels.
- A separate **ChromBPNet** (small bias-corrected seq→profile model) trained per pseudobulk cell state (Pearson ~0.75–0.875). Interpreted with DeepLIFT/DeepSHAP contribution scores + **TF-MoDISco** to track per-nucleotide, per-state motif activity in individual enhancers (e.g. the NanoG locus, with CTCF insulators bookmarking dynamic enhancers).

## Key findings

- **~50–60k transient peaks** open then close, are **out-of-distribution** (absent from ENCODE/Roadmap and beginning/end states), and map to genes with no obvious enrichment — invisible without dense time-sampling.
- **Affinity × concentration trade-off.** At supraphysiological OSKM, OCT4/SOX2 bind **low-affinity, non-canonical** motifs (e.g. POU "CAT→AAT") that physiological levels can't. Transient peaks with the *weakest* OCT-SOX motifs close *first* as TF concentration drops — explaining the temporal decay. ChromBPNet, trained only on sequence + accessibility, **reproduces footprint changes as a function of both concentration and affinity** despite never being told either (synthetic-motif insertion experiments for KLF, SOX2).
- **"Repression by theft" model.** Transient low-affinity OCT-SOX peaks also carry **AP-1** sites. The flood of new peaks **sponges AP-1 away** from fibroblast enhancers → rapid (~5×, within 2 days) shutdown of fibroblast genes. Confirmed by single-cell multiome (day 1–2): per-cell accessibility at newly opened AP-1 peaks **anti-correlates** with fibroblast-program expression.

## Q&A highlights (with Rahul Satija)

- **Low-affinity motifs are pervasive, not a reprogramming artifact** — standard motif-calling/binarization (ChromVAR-style thresholds) hides them; collectively many weak sites rival a single strong one (cites Julia/related work; Mars/Barkai-style low-affinity work).
- **One model for promoters + enhancers** is fine — they're ends of a continuous spectrum; fine-tune sampling/learning rates for subtleties (vs. a separate-models view).
- **Gene-expression (RNA) prediction is a *data* problem, not architecture** — only ~20k genes, each enhancer seen once in native context; needs perturbation data (enhancer hopping, deletions, inversions) to learn enhancer→gene syntax.
- **What a "virtual cell" should be:** not just accurate prediction but **mechanistically anchored** internals — interpret the model and show predictions arise through real causal biology.

## Connections to the corpus

- Squarely the **virtual-cells / sequence-to-function FM** thread — see [Aviv Regev — virtual cell / lab-in-the-loop](aviv-regev-virtual-cell.md); AACR [virtual-cells](../../aacr-2026/topics/virtual-cells/) and [bioinfo-tools](../../aacr-2026/topics/bioinfo-tools/) (Geneformer/scGPT-line FMs).
- Reprogramming-dynamics + scATAC overlaps the GRC "Single-Cell Modeling / Epigenomics" sessions in [`single-cell-genomics-2026/`](../../single-cell-genomics-2026/).

## Sources

- SCGD26 event + speaker list: <https://satijalab.org/scgd26/>
- Paper (published): Nair, Ameen, et al. "Transcription factor stoichiometry, motif affinity and syntax regulate single-cell chromatin dynamics during fibroblast reprogramming to pluripotency." — <https://pmc.ncbi.nlm.nih.gov/articles/PMC10592962/>
- Preprint (bioRxiv): <https://doi.org/10.1101/2023.10.04.560808>
- Interactive browser (scRNA + scATAC, data, ChromBPNet models): <https://kundajelab.github.io/reprogramming-browser/home.html>
- Analysis code: <https://github.com/kundajelab/scATAC-reprog>
- ChromBPNet (maintained tool): <https://github.com/kundajelab/chrombpnet>
