# Alexandra Bradu — VIPerturb-seq + the "GuEST-List" library

**Speaker:** **Alexandra (Alex) Bradu**, Associate Research Scientist — **Satija Lab, New York Genome Center**.
**Slot:** SCGD26, Jun 12, 2026 · 2:45–3:05 PM EDT — *"Genome-wide single-cell perturbation screens with VIPerturb-seq"*
**Method:** **VIPerturb-seq** ("Very Important Perturbations") + the **GuEST-List** genome-wide guide-barcode library (Guides for Enrichment-based Screening of Targets; the transcript's "Guest List" is the spoken acronym)
**Recording:** SCGD26 livestream — [preprint](https://www.biorxiv.org/content/10.64898/2026.02.12.705613v1), [project site + protocols](https://satijalab.org/viperturb-seq/), and [Addgene pooled library](https://www.addgene.org/pooled-library/human-crispri-guest-list/) (#248188/#248189) available
**Status:** Captured from session transcript

## Thesis

Make **genome-wide single-cell CRISPR screens routine and cheap.** Published genome-wide screens needed >1,000 lanes of 10x. VIP Perturb-seq attacks cost on two axes: (1) raw **throughput**, and (2) **phenotypic enrichment** so you only deep-sequence the cells you care about.

## How it works

Marries a genome-wide perturbation library (e.g. Dolcetto CRISPRi, Doench lab) with **10x Flex**:

- **Throughput:** Flex's newest chemistry adds a barcode to subsets of cells **before** GEM formation → pack multiple cells per droplet → genome-scale screen "in a single afternoon."
- **Enrichment:** Flex works on **fixed/permeabilized** cells, so you can FACS-sort on **intracellular** protein / PTM / even RNA (not just surface markers) and only build libraries from enriched cells.
- **The probe problem + "Guest List":** Flex needs a spiked-in probe per transcript; custom probes against every guide protospacer would cost six figures and aren't reusable. Instead, each guide is cloned with a **synthetic barcode** (modified CROP-seq design). The barcode is **split into part-A × part-B** (100 × 100 options → 10,000 constructs) so **<500 probes** read out the whole Dolcetto library. Recombination between protospacer and barcode is kept **<2%** by minimizing distance (<100 bp) and using three low-homology (<20 bp) guide scaffolds. The genome-wide library is **"GuEST-List"** (Guides for Enrichment-based Screening of Targets — every gene invited; only some become VIPs per experiment); its protospacers match the Dolcetto A CRISPRi library (57,050 guides, >18,000 genes), deposited on [Addgene](https://www.addgene.org/pooled-library/human-crispri-guest-list/) (#248188 puro; #248189 puro+eGFP).

## Key results

- Clean, unambiguous guide assignment (e.g. FDFT1: hundreds of UMIs for the assigned guide, single digits for the next) with robust target knockdown; **>500 probes detect the whole Dolcetto library**.
- **Throughput:** a single 10x lane recovers a huge cell count vs. weeks of prior work; improved sensitivity for **lowly expressed** transcripts vs. 3′ capture.
- **Enrichment proof-of-concept (intracellular Vimentin):** sort Vimentin-high K562s, input ~20k cells → clean enrichment of the **Rag-Regulator/Ragulator (mTOR)** complex as VIPs, at ~2% of the genome-wide cell count.
- **RNA-phenotype screens:** integrated with **Caleb LaReau**'s **perf-seq** (RNA flow-FISH isolation of rare types) — pilot CRISPR screen on a non-coding-RNA phenotype with clean positive-control enrichment (postdoc Aaron Cummings).

## Q&A highlights

- **Enrichment threshold** chosen per phenotype via arrayed FACS benchmarking + mixing experiments; multiple sort bins can be sample-indexed in one run.
- **Split-barcode capture generalizes** beyond guides — ORF libraries, lineage cassettes, combinatorial screens. 10x is seeking early-access customers for the commercial version.

## Connections to the corpus

- Scalable Flex-based perturb screening — sibling to [Aviv Regev — lab-in-the-loop](aviv-regev-virtual-cell.md) and [Xin Jin — in vivo Perturb-seq](xin-jin-in-vivo-perturbseq.md); shares Flex chemistry + the LaReau collaboration with [Sydney Blattman — GIFT](sydney-blattman-gift.md).
- AACR axis: [single-cell-spatial-omics](../../aacr-2026/topics/single-cell-spatial-omics/), [virtual-cells](../../aacr-2026/topics/virtual-cells/).

## Sources

- Speaker / title / slot — [SCGD26 schedule](https://satijalab.org/scgd26/): "Alex Bradu, NYGC — Genome-wide single-cell perturbation screens with VIPerturb-seq," 2:45–3:05 PM EDT. Full name **Alexandra (Alex) Bradu**, Associate Research Scientist, confirmed on the [Satija Lab people page](https://satijalab.org/people/).
- Preprint — Bradu, Blair, Grabski, Mascio, Lee, McCormick, Satija. "Genome-wide single-cell perturbation screens with VIPerturb-seq." [bioRxiv, Feb 2026](https://www.biorxiv.org/content/10.64898/2026.02.12.705613v1).
- Project site (protocols, assay schema, tools) — [satijalab.org/viperturb-seq](https://satijalab.org/viperturb-seq/).
- Library — [Addgene CRISPRi GuEST-List pooled library](https://www.addgene.org/pooled-library/human-crispri-guest-list/), IDs #248188 / #248189, depositing lab Rahul Satija.

*Note: the project site frames VIPerturb-seq as openly shared reagents/protocols and reports a ~50-fold throughput gain via combinatorial indexing; it does not mention a 10x commercial product (the "commercial version" claim from the transcript is unconfirmed).*
