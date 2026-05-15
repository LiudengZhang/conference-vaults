# Nucleotide Transformer — Dalla-Torre et al. (InstaDeep + NVIDIA + TU Munich)

**One-line description** — A family of encoder-only transformer foundation models for human and multispecies genomics (50M–2.5B parameters) trained with masked-language modelling on 6-mer tokenised DNA across 850 species and 3,202 human genomes; the 2.5B Multispecies variant remains the strongest fine-tuning baseline for short-range regulatory and variant tasks as of 2026.

- **Authors:** Hugo Dalla-Torre, Liam Gonzalez, Javier Mendoza-Revilla, Nicolas Lopez Carranza et al.
- **Affiliation(s):** InstaDeep (London/Paris); NVIDIA; Technical University of Munich
- **Venue:** Nature Methods, Volume 22, February 2025 (preprint: bioRxiv Jan 2023)
- **OpenReview:** N/A (journal venue)
- **arXiv / bioRxiv:** [bioRxiv 2023.01.11.523679](https://www.biorxiv.org/content/10.1101/2023.01.11.523679v1)
- **Nature Methods:** [10.1038/s41592-024-02523-z](https://www.nature.com/articles/s41592-024-02523-z)
- **Code:** [github.com/instadeepai/nucleotide-transformer](https://github.com/instadeepai/nucleotide-transformer)
- **Pretrained weights:** [HF Hub — InstaDeepAI collection](https://huggingface.co/InstaDeepAI) (700k+ downloads as of late 2025)

## What it does

Nucleotide Transformer (NT) is a family of encoder-only transformer models that produce contextual embeddings of DNA for downstream supervised tasks: promoter / enhancer / splice-site classification, histone-mark prediction, regulatory-element annotation, and variant effect scoring. It is consumed as a fine-tuning backbone (parameter-efficient LoRA or full fine-tune) rather than a generative model. The headline NT-Multispecies 2.5B variant is the canonical "strong baseline" against which DNABERT-2, HyenaDNA, Caduceus, Evo, and AlphaGenome are routinely compared on the 18-task NT benchmark suite and BEND.

## How it works

**Architecture.** Encoder-only transformer (BERT-style) with learnable positional embeddings, full bidirectional self-attention. The family spans four sizes — 50M, 100M, 250M, 500M, 2.5B parameters — sharing the same architecture but with width and depth scaled. The 2.5B model uses 32 layers and a hidden size of 2,560 (per the Nature Methods supplement). No ALiBi, no RoPE, no FlashAttention in the original release — these arrived in DNABERT-2 and NT-v2 as efficiency upgrades.

**Tokenisation.** 6-mer tokenisation: non-overlapping windows of 6 nucleotides become single tokens. Vocabulary is the 4^6 = 4,096 possible 6-mers plus 5 stand-alone tokens (A, T, C, G, N) and 3 special tokens (PAD, MASK, CLS), totalling 4,104 tokens. 6-mers were chosen as a sequence-length / embedding-size trade-off after sweeping k from 3 to 8.

**Pretraining corpus.** Three corpora releasing four checkpoint families:
- **Human-reference (500M\_human\_ref):** GRCh38 only, ~3.2 Gb.
- **1000 Genomes (2.5B\_1000G):** 3,202 diverse human genomes from the 1000 Genomes Project.
- **Multispecies (2.5B\_multispecies):** 850 species spanning bacteria, fungi, invertebrates, vertebrates, plants — totalling 174 billion nucleotides. This is the highest-performing variant overall.
- **NT-v2 (50M / 100M / 250M / 500M):** later release with RoPE positional encoding, swiglu activations, FlashAttention-style efficiency.

**Pretraining objective.** Masked-language modelling (BERT-style): 15% of 6-mer tokens are masked; the model predicts the original token from bidirectional context. No next-token / causal objective.

**Context length.** 1,000 tokens of positional embedding → up to ~6 kb of DNA per forward pass (6-mer tokenisation × 1,000 tokens). This is the binding constraint that motivated HyenaDNA (1 Mb) and AlphaGenome (1 Mb).

**Pretraining compute.** The 2.5B-multispecies model was trained on 128 NVIDIA A100 80GB GPUs for 28 days — roughly 86,000 GPU-hours (per Nature Methods reporting). NVIDIA's contribution was infrastructure and Megatron-style sharding.

**Downstream tasks.** 18-task benchmark suite assembled by the authors covering: histone-mark prediction (10 tasks), regulatory annotation (enhancer / promoter / splice donor / splice acceptor — 5 tasks), and chromatin-state classification (3 tasks). Sequences range 200 bp – 600 bp. Probed via fine-tuning, with linear-probing and parameter-efficient-tuning comparators reported.

## Headline benchmarks

- **NT-Multispecies 2.5B** achieves the highest mean Matthews correlation coefficient (MCC) across the 18-task suite, outperforming DNABERT-2, HyenaDNA-32kb, and Enformer in head-to-head comparison (Nature Methods Table 2). The Multispecies model **matches or outperforms HyenaDNA on all 18 tasks** despite HyenaDNA having a 32-kb context (vs 6 kb), demonstrating that pretraining-data diversity beats raw context length on short-range regulatory tasks.
- **Variant effect prediction (zero-shot embedding distance):** NT-2.5B-multispecies shows competitive AUROC for ClinVar pathogenic / benign classification but is dominated by AlphaGenome on regulatory-variant tasks where 1 Mb context is decisive.
- **GUE benchmark (DNABERT-2 paper):** NT-2.5B-multispecies is the strongest baseline overall but DNABERT-2 matches its score with **21× fewer parameters and 92× less pretraining GPU-time** — the methodological framing that motivated BPE replacing k-mers.
- **HuggingFace adoption signal:** 700k+ cumulative downloads, 120+ citations as of late 2025 — the most-downloaded genomic FM on HF Hub.

## Why it matters

NT was the first systematic demonstration that the LLM foundation-model recipe (large-scale MLM pretraining → task-agnostic embeddings → cheap fine-tuning) transfers cleanly to genomics. Before NT (Jan 2023 preprint), DNABERT-1 (2021) had shown the recipe at small scale but only on human reference; NT proved that (a) scaling to 2.5B parameters delivers monotonic gains, and (b) **multispecies pretraining beats human-only pretraining even on human downstream tasks** — the canonical "evolutionary regularisation" argument that every subsequent genomic FM (DNABERT-2, HyenaDNA-mouse, Evo, Caduceus) has inherited. The 18-task NT benchmark suite is now the standard fine-tuning evaluation, with BEND and GUE layered on top for breadth.

## Known limitations

- **Context length is the binding bottleneck.** 6 kb of DNA is insufficient for any long-range regulatory task (enhancer–promoter loops average 50–500 kb in the human genome); NT cannot represent these interactions, which is why HyenaDNA (1 Mb), Enformer (200 kb), Borzoi (524 kb), and AlphaGenome (1 Mb) all exist.
- **6-mer tokenisation loses single-base resolution.** Two sequences differing by one nucleotide can produce wildly different token sequences depending on alignment with the 6-mer grid; this hurts SNV-effect prediction and is the explicit motivation for DNABERT-2's BPE and HyenaDNA's single-nucleotide tokenisation.
- **MLM is not generative.** NT cannot sample novel sequences (unlike Evo / Evo2 / HyenaDNA, which are causal LMs). For variant-effect work this is fine; for synthetic-biology design it is not.
- **Multispecies bias toward microbial sequences.** The 850-species corpus is dominated by bacteria and fungi (smaller genomes are over-represented per genome), which may bias representations toward prokaryotic regulatory patterns; the human-only and 1000G variants exist partly to control for this.
- **Compute cost.** 2.5B parameters × 6-mer tokenisation means fine-tuning the headline model requires multi-A100 setups; the 50M / 100M NT-v2 variants exist for low-budget settings but trade ~3–5 MCC points on the 18-task suite.

## Sources

- **Nature Methods paper:** Dalla-Torre et al., "Nucleotide Transformer: building and evaluating robust foundation models for human genomics," Nature Methods 22, February 2025. [10.1038/s41592-024-02523-z](https://www.nature.com/articles/s41592-024-02523-z) — [PubMed 39609566](https://pubmed.ncbi.nlm.nih.gov/39609566/) — [PMC11810778](https://pmc.ncbi.nlm.nih.gov/articles/PMC11810778/)
- **bioRxiv preprint (Jan 2023):** [10.1101/2023.01.11.523679](https://www.biorxiv.org/content/10.1101/2023.01.11.523679v1)
- **InstaDeep blog companion:** [Decoding our Genome with Nucleotide Transformers](https://instadeep.com/2024/12/decoding-our-genome-with-nucleotide-transformers/)
- **Code:** [github.com/instadeepai/nucleotide-transformer](https://github.com/instadeepai/nucleotide-transformer)
- **Weights (HF Hub):** [huggingface.co/InstaDeepAI](https://huggingface.co/InstaDeepAI) — all four variants under Apache 2.0 / CC-BY-NC licenses depending on training corpus
- **Companion editorial:** [Generalized AI models for genomics applications](https://www.nature.com/articles/s41592-024-02524-y) — Nature Methods News & Views, Feb 2025
