# Kevin Chao — TimeVault: a vault-protein recorder of the cellular transcriptome

**Speaker:** **Kevin (Yu-Kai) Chao** — PhD student, Department of Chemistry, Harvard University / Broad Institute (**Fei Chen Lab**; Broad Cancer Program). Introduced by Nathan Nakatsuka (Satija Lab).
**Talk title (official):** "TimeVault: A genetically encoded device for transcriptome storage in mammalian cells"
**Slot:** SCGD26, Jun 12, 2026 — 3:20–3:40 PM
**Method:** **TimeVault** — engineered **vault** ribonucleoprotein particle that captures + preserves a past transcriptome snapshot in living cells
**Paper:** Chao Y-K, Wu M, Gong Q, Chen F. *Science* (2026), [doi:10.1126/science.adz9353](https://www.science.org/doi/abs/10.1126/science.adz9353) — plasmids deposited on Addgene (e.g. [#242118](https://www.addgene.org/242118/), full set: [article collection](https://www.addgene.org/browse/article/28263789/))
**Status:** Captured from session transcript

## Thesis

To ask *why* a cell survives a drug, you need its **prior** (drug-naive) state — but RNA measurement is destructive and drug selection already alters the cell. **TimeVault** keeps a "time capsule" record of the transcriptome **before** perturbation, carried through to after, linking past state to future fate (cancer persister cells: drug-tolerant "persister" states pre-exist treatment).

## How it works

Built on the **vault** — a large, abundant (3,000–15,000/cell), non-essential ribonucleoprotein whose major vault protein (MVP) self-assembles (78 MVP copies; native cargo = a poly-ADP-ribose polymerase with an "INT" interaction domain). Fusing the **INT domain** to a protein packages it into the vault.

TimeVault fuses INT to a **poly(A)-binding protein** → captures mRNA into the vault particle, isolating it from cytosolic mRNA to preserve a past transcriptome. Recording window is controlled by a **Tet-OFF** promoter (add doxycycline to stop capture).

## Key results

- **Captures RNA:** detectable only when both components (MVP + poly(A)-binding) are present; preserves ~1–3% of housekeeping mRNA (GAPDH, ACTB) and protects it from degradation in lysate.
- **Controllable window:** doxycycline stops capture (MVP mRNA half-life ~5.4 h); 4sU labeling shows vault-captured RNA stays high over multiple days while the lysate transcriptome turns over in <1 day; RNA-seq shows captured transcriptome correlates well with total lysate (comparable gene counts) → ~1–2 transcripts/particle.
- **Records a past state:** heat-shock-then-recover experiment — the **recorded** fraction shows up-regulated heat-shock response only in the heat-shock-past condition, while the **present** transcriptome is normal (cell recovered). Clean separation by GO enrichment.
- **Cancer persisters (PC9, EGFR-mutant NSCLC + osimertinib):** retrieved the **drug-naive** transcriptome of cells that later survived. Persisters pre-show up-regulated **OXPHOS**, reduced division (reduced Warburg), adhesion, detox enzymes, IL-6. Top marker **fibronectin (FN1)** validated by immunostaining (a rare FN1-high subpopulation pre-exists; majority becomes FN1-high after drug). scRNA on drug-naive PC9 confirms a middle population enriched for FN1/PI3 etc. **siRNA against FN1 (and other persister markers) sensitizes** cells to osimertinib (combination kills more than drug alone).

## Connections to the corpus

- A third "molecular recorder" on the day — pairs with [GEMINI](molecular-recorder-gemini.md) (protein-assembly temporal recorder) and [SynapseSeq](amanda-urke-synapseseq.md) (barcode recording); the past↔future framing echoes [Aviv Regev — lab-in-the-loop](aviv-regev-virtual-cell.md).
- Cancer drug-tolerant-persister biology → AACR clinical / single-cell axes.

## Sources

- Schedule — [Single Cell Genomics Day 2026](https://satijalab.org/scgd26/): "Kevin Chao (Harvard University) — TimeVault: A genetically encoded device for transcriptome storage in mammalian cells," 3:20–3:40 PM.
- Paper — [*Science* 2026, doi:10.1126/science.adz9353](https://www.science.org/doi/abs/10.1126/science.adz9353); [Broad listing](https://www.broadinstitute.org/publications/broad1373081) (authors Chao Y-K, Wu M, Gong Q, Chen F → confirms PI = **Fei Chen**, Broad Institute).
- Plasmids — [Addgene #242118 (pKC061_pLVX_TetON_RRM34_TmTP, gift of Fei Chen)](https://www.addgene.org/242118/); [article plasmid collection](https://www.addgene.org/browse/article/28263789/).

## Open questions

- No separate bioRxiv preprint located — the work appears to have been published directly in *Science* (2026). (Note: the 2023 bioRxiv "Molecular Time Capsules," 10.1101/2023.10.12.562053, is a **different** group — Gene-Wei Li lab, MIT — not TimeVault.)
- Introducer (Nathan Nakatsuka) is from the session transcript, not independently confirmed.
