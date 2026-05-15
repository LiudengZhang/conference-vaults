# Reading TEA Leaves for de novo Protein Design — Pantolini & Durairaj (Basel)

**One-line description** — A protein-language-model-derived 20-letter "TEA" alphabet enables fast Monte-Carlo de-novo protein design without invoking expensive structure-prediction oracles inside the inner loop, expanding the functional protein design space at a fraction of prior compute cost.

- **Authors:** Lorenzo Pantolini, Janani Durairaj
- **Affiliation(s):** SIB Swiss Institute of Bioinformatics / University of Basel (Schwede lab adjacent)
- **Track / workshop:** ICLR 2026 — **LMRL workshop oral talk** (Apr 27, 2026; 16:13 oral slot)
- **OpenReview:** TBD — workshop PDF not yet directly linked
- **bioRxiv:** [10.64898/2026.02.09.704813v2](https://www.biorxiv.org/content/10.64898/2026.02.09.704813v2)
- **Code:** TBD — Durairaj lab github
- **Status at ICLR 2026:** LMRL workshop **Oral** (12-min slot)

## What it does

The paper attacks the Monte-Carlo bottleneck in de novo protein design: classical MCMC over sequence space is under-explored because each step either requires a slow structure-prediction oracle (AlphaFold/Boltz/ESMFold-class) or a noisy proxy. The contribution is **TEA**, a learned 20-letter alphabet derived from contrastive training over protein-language-model embeddings, which captures functional equivalence classes well enough to substitute for full structure prediction inside the MCMC inner loop.

## How it works

**Core idea.** Discretise protein-language-model embeddings into a learned 20-letter "TEA" alphabet — sized to match the natural amino-acid alphabet but indexing *functional / fold-class equivalence* — so MCMC de novo protein design can score proposals in TEA-space at sequence-comparison cost instead of running a structure-prediction oracle inside the inner loop.

**Inputs / outputs.** Inputs are a design target (functional motif, fold class, or homology reference) and an initial sequence; the MCMC sampler outputs candidate sequences scored in TEA-space. Final candidates are verified with full structure prediction (AlphaFold / Boltz / ESMFold-class) outside the loop.

**Key innovation.** Prior de novo MCMC pipelines (trDesign, ProteinMPNN-coupled hallucination, RFdiffusion-driven sampling) call a structure oracle at every step — the dominant compute cost. TEA replaces the oracle with a learned discrete projection trained contrastively from protein-LM embeddings, which Durairaj's earlier work (*Nature* 2023, "Uncovering new families and folds in the natural protein universe") had already shown to capture functional equivalence well enough for large-scale homology search.

**Parameters / training details.** Alphabet size: 20 letters (matching amino-acid cardinality). Training objective: contrastive on protein-LM embeddings against functional / fold-class anchors. Base protein-LM: ESM-class (TBD-verify from bioRxiv v2). MCMC inner-loop scoring: TEA-space sequence comparison; structure prediction reserved for end-of-run verification only.

**Canonical experiment.** The bioRxiv v2 preprint demonstrates Monte-Carlo de novo design over functional targets at compute cost far below structure-oracle-in-the-loop baselines, and reuses the TEA alphabet's earlier "highly efficient large-scale protein homology search" performance as the validation that TEA-space comparison is biologically meaningful (TBD — exact wall-clock and success-rate numbers from bioRxiv v2 PDF).

## Headline benchmarks

The bioRxiv preprint reports "highly efficient large-scale protein homology search" performance for the TEA alphabet, and demonstrates Monte-Carlo de-novo design over functional targets at compute cost far below structure-oracle-in-the-loop baselines (TBD — exact wall-clock and success-rate numbers from bioRxiv v2 PDF).

## Where it fits in the corpus

- **AACR 2026:** drug-discovery axis — design of small protein binders for cancer targets without full Boltz inside the loop.
- **GEM workshop sibling:** the GEM RBX-1 binder competition is the natural benchmark for TEA-driven design pipelines.
- **NeurIPS 2026 MLSB:** likely follow-on with experimental validation.
- **ESHG / ASHG 2026:** protein-variant effect prediction is the diagnostic adaptation.

## Notes

Janani Durairaj's TEA-alphabet line of work bridges the protein-LM-embeddings and protein-design communities — the same alphabet that enabled efficient homology search (Nature 2023, "Uncovering new families and folds in the natural protein universe") is being repurposed for generative inner loops. The ICLR 2026 LMRL oral slot signals the community sees this as the next step beyond RFdiffusion / Boltz-driven design for the "design-at-scale" regime where the structure-oracle cost dominates. Pair with Proteina-Complexa (NVIDIA, this vault) as the two methodological poles of 2026 protein design — one scales by atomistic generative pretraining + test-time compute, the other scales by sidestepping the oracle entirely.
