# AlphaGenome — Avsec et al. (Google DeepMind)

**One-line description** — A unified DNA-sequence-to-function model that takes **1 Mb of DNA as input** and emits **5,930 functional-genomics tracks at single-base-pair resolution** across RNA expression, splicing, chromatin accessibility, histone marks, TF binding, and Hi-C contact maps — a U-Net with a transformer bottleneck, ~450M parameters, jointly trained on ENCODE + GTEx + FANTOM5 + 4D Nucleome for human and mouse, and matching or exceeding the strongest external models on **25 of 26 variant-effect-prediction evaluations**.

- **Authors:** Žiga Avsec, Natasha Latysheva, Jun Cheng, Tom Hubbard, Pushmeet Kohli, and the DeepMind genomics team (full author list: 30+)
- **Affiliation(s):** Google DeepMind
- **Venue:**
  - **Preprint:** bioRxiv, **25 June 2025** — coincident with the DeepMind blog announcement
  - **Journal:** *Nature* 649(8099), **January 2026** — peer-reviewed publication (open-access ahead of issue on 28 Jan 2026)
- **bioRxiv preprint:** [10.1101/2025.06.25.661532v1](https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1)
- **Nature paper:** [10.1038/s41586-025-10014-0](https://www.nature.com/articles/s41586-025-10014-0)
- **DeepMind paper PDF:** [storage.googleapis.com/deepmind-media/papers/alphagenome.pdf](https://storage.googleapis.com/deepmind-media/papers/alphagenome.pdf)
- **DeepMind blog (Jun 2025):** [deepmind.google/blog/alphagenome](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/)
- **Code:** [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome) (Python SDK, Apache 2.0) and [github.com/google-deepmind/alphagenome_research](https://github.com/google-deepmind/alphagenome_research) (research code, source released **Jan 2026**)
- **Pretrained weights:** [HF Hub — google/alphagenome-all-folds](https://huggingface.co/google/alphagenome-all-folds) and per-fold checkpoints `google/alphagenome-fold-0` … `fold-3` — **non-commercial license** ([AlphaGenome Model Terms](https://deepmind.google.com/science/alphagenome/model-terms))
- **API:** Free hosted inference at [deepmind.google.com/science/alphagenome](https://deepmind.google.com/science/alphagenome) for non-commercial research

## What it does

AlphaGenome is a **supervised sequence-to-track regressor** — not a self-supervised foundation model like NT / DNABERT-2 / HyenaDNA / Evo. It maps a 1-Mb DNA window to thousands of predicted functional-genomics measurements at single-base resolution, jointly for human and mouse. The headline application is **non-coding variant effect prediction**: take a reference sequence and an alternate sequence carrying a candidate variant, run both through AlphaGenome, and compare the predicted track deltas at the variant locus. Outputs cover the major regulatory readouts that a wet-lab functional genomics core would assay — making the model a "Swiss-army knife for the non-coding 98% of the genome" (per the Trends in Genetics commentary by Spille et al. 2025) — and the first single model to deliver this range in a single inference call (per DeepMind blog).

## How it works

**Architecture.** **U-Net with transformer bottleneck** (per DeepMind blog and architecture commentary in [rewire.it 2025](https://rewire.it/blog/alphagenome-one-model-for-the-other-98-percent-of-your-dna/) and [Hannigan 2025](https://livingbio.substack.com/p/understanding-alphagenome)):
1. **Convolutional encoder** downsamples the 1-Mb input from 1-bp to 128-bp resolution, learning local sequence motifs (TF binding sites, splice signals, promoter elements).
2. **Transformer bottleneck** at the 128-bp resolution propagates information across the full 1-Mb window — modelling long-range enhancer–promoter interactions, isochore context, chromatin domain structure.
3. **U-Net decoder** upsamples back to 1-bp resolution with skip connections from the encoder, producing single-base predictions for the output tracks that need it (splice junctions, TSS coordinates).
4. **Per-modality output heads** emit the 5,930 human / 1,128 mouse functional tracks.

Implementation uses **sequence parallelism across 8 interconnected TPU v3 devices** — the 1-Mb input is partitioned into 131-kb chunks, with each TPU processing one interval, then aggregated for the transformer bottleneck (per Nature paper and the [arxiviq deep-dive](https://arxiviq.substack.com/p/advancing-regulatory-variant-effect)).

**Parameter count.** Approximately **450 million trainable parameters** (per multiple secondary sources including [Wasai Tech 2025](https://www.wasaitech.com/post/google-deepmind-s-alphagenome-a-computational-perspective) — *the Nature paper does not report this in the abstract; the 450M figure traces to the DeepMind blog and is reported consistently across architecture explainer write-ups but is not a peer-reviewed primary number*).

**Tokenisation.** **No tokenisation in the LLM sense** — input is one-hot encoded DNA at single-base resolution (4-channel: A, C, G, T, with N handled as the zero vector). This is the Enformer / Borzoi lineage rather than the NT / DNABERT / HyenaDNA tokenised-LM lineage.

**Training data.**
- **Reference genomes:** human (GRCh38) and mouse (GRCm39) reference sequences.
- **Functional readouts (training targets):** consortium-curated assay tracks grouped by assay type, cell ontology, and target factor:
    - **ENCODE** — RNA-seq, PRO-cap, DNase-seq, ATAC-seq, TF and histone ChIP-seq
    - **GTEx** — bulk-tissue RNA-seq (held out from public release for licensing; used in training)
    - **FANTOM5** — CAGE (transcription start sites)
    - **4D Nucleome** — Hi-C / Micro-C contact maps

**Output modalities.** **5,930 human tracks** (1,128 mouse tracks), spanning: RNA expression, CAGE / PRO-cap (transcription initiation), splice sites + splice usage + splice junction strength, DNase / ATAC accessibility, histone-mark ChIP, TF binding ChIP, and Hi-C contact maps. Resolution: single base for RNA / splicing / chromatin tracks; per-bin (variable) for contact maps.

**Training objective.** Multi-task regression: per-track Poisson / Gaussian loss between predicted and observed coverage / signal, summed across modalities with modality-specific weights. **Knowledge distillation** is then applied — the published `all_folds` checkpoint is a student model distilled from an ensemble of four cross-validation-fold "teacher" models, balancing accuracy against inference cost.

**Context length / input.** **1,000,000 bp** input window (extended internally by 4,096 bp padding — 2,048 bp each side — for boundary handling). Output predictions cover the central ~131 kb of the input at single-base resolution; the flanking sequence provides regulatory context but is not itself predicted. This is **5× Enformer's 196,608-bp context** and **~2× Borzoi's 524-kb context**.

**Pretraining compute.** Not reported precisely in the published paper. Training infrastructure is **TPU v3** with sequence parallelism across 8 chips per replica; the multi-fold teacher-ensemble + distillation pipeline is significantly heavier than single-model training (per DeepMind blog — no peer-reviewed total TPU-hour figure available).

**Downstream / variant scoring.** Inference takes a reference 1-Mb window and an alt-allele 1-Mb window (typically centred on the variant), produces 5,930 tracks each, and reports per-track and aggregated effect scores. The DeepMind hosted API exposes this as a single REST call.

## Headline benchmarks

- **Variant effect prediction:** AlphaGenome matches or exceeds the strongest available external model on **25 of 26 evaluations** spanning eQTL, sQTL, caQTL, MPRA, and clinical / GWAS variant scoring (per Nature paper abstract).
- **vs Enformer (DeepMind 2021):** Direct successor; AlphaGenome ~5× longer context (1 Mb vs 196 kb), adds splicing and Hi-C output heads, unifies human and mouse, adds per-base resolution for splicing tracks. Outperforms Enformer across all comparable RNA-seq and chromatin tasks (per Nature paper).
- **vs Borzoi (Calico 2024):** AlphaGenome's closest peer (Borzoi: 524-kb context, RNA-seq + epigenetic prediction, U-Net architecture). AlphaGenome wins on splicing-specific tasks and contact-map prediction (which Borzoi does not output); the two are comparable on bulk RNA-seq.
- **vs single-task specialists (Pangolin for splicing, SpliceAI for splice prediction, ChromBPNet for chromatin):** AlphaGenome matches or beats the specialists in their own domain with **a single unified model** — the load-bearing methodological argument of the paper.
- **vs genomic FMs (NT, DNABERT-2, HyenaDNA, Evo):** Not a fair comparison — those are self-supervised LMs evaluated by fine-tuning, AlphaGenome is supervised end-to-end. But on functional-track prediction *as a downstream task*, AlphaGenome dominates the genomic-FM fine-tunes because it was trained for it directly.

*(Caveat: the "25 of 26" framing is from the Nature paper's own benchmarking suite, which DeepMind defines. Independent reproduction at this breadth is ongoing — the **alphagenome_research code release in January 2026** [per [STAT News, 28 Jan 2026](https://www.statnews.com/2026/01/28/deepmind-opens-alphagenome-source-code/)] is what enables third-party replication. Per DeepMind blog — no peer-reviewed external validation of the full 26-task suite as of May 2026.)*

## Why it matters

AlphaGenome is the first model to unify the **non-coding regulatory genomics** stack (gene expression, splicing, chromatin, 3D contact) in a single end-to-end inference call at megabase scale — collapsing what was a dozen separate specialist models (Enformer, Pangolin, SpliceAI, ChromBPNet, Akita, Borzoi, …) into one. Three concrete consequences for the 2026 oncology and clinical-genomics translation effort:

1. **One model for non-coding variant interpretation.** Pathogenic non-coding variants in cancer drivers (TERT promoter, MYC enhancers, PVT1) and Mendelian disease can now be scored uniformly across modalities — addressing the "98% of the genome is non-coding and we can't score it" problem that has dogged ACMG variant classification.
2. **Megabase context as the new default.** Enformer's 196 kb was the previous ceiling; AlphaGenome at 1 Mb covers most TADs in a single window. The next generation of clinical variant pipelines is expected to default to 1 Mb context (Borzoi, AlphaGenome, Evo2).
3. **Free hosted API for non-commercial use.** Unlike the prior AlphaFold release pattern (weights public, commercial use restricted), AlphaGenome adds a free hosted API alongside the weights — significantly lowering the integration cost for academic clinical-genomics groups. The non-commercial restriction is the binding constraint for industry uptake (see Limitations).

The model's relationship to the self-supervised FM lineage (NT, DNABERT-2, HyenaDNA, Evo, Evo2) is **complementary, not competitive** — AlphaGenome will not sample novel sequences or do in-context learning, and the FM lineage will not give per-base RNA-seq predictions out of the box. The expected 2026–2027 pattern is hybrid pipelines where Evo2-style FMs do variant discovery / sequence design and AlphaGenome scores the resulting variants for regulatory effect.

## Known limitations

- **Non-commercial license is the binding industry constraint.** The model weights are released under the AlphaGenome Model Terms — strictly non-commercial use, no distillation into derivative models, no commercial fine-tuning. This blocks pharma / biotech integration without a separate commercial agreement (per the [HF model card](https://huggingface.co/google/alphagenome-all-folds/blob/main/README.md)).
- **No generative capability.** AlphaGenome is purely a forward predictor; it cannot sample novel DNA sequences, do in-context learning, or score variants by sequence likelihood. The Evo2 / HyenaDNA lineage is needed for those use cases.
- **Trained on bulk-tissue / cell-line assays, not single-cell.** Output tracks are bulk RNA-seq, bulk ChIP-seq, bulk Hi-C — not scRNA-seq, scATAC-seq, single-cell Hi-C. Cell-type-specific predictions are at the resolution of the input ENCODE/GTEx cell-type ontology (~hundreds of cell types and tissues), not single-cell resolution. This is the binding limitation for tumour-microenvironment applications where intra-tumoural heterogeneity is the question.
- **Human + mouse only.** No fly, yeast, plant, or arbitrary-species support — unlike multispecies FMs (NT-multispecies-2.5B, Evo). Translational genomics outside the mouse-human axis requires either Borzoi-style retraining or a multispecies FM.
- **GTEx training data is held out from public release.** Reproducibility of the GTEx-derived eQTL benchmarks requires GTEx access (which is dbGaP-controlled) — the released `all_folds` checkpoint includes GTEx-trained weights but the training tracks themselves are not redistributable.
- **The 450M-parameter figure is not in the peer-reviewed paper.** It appears consistently in DeepMind blog text and secondary explainer write-ups but is not in the Nature abstract or the main-text architecture description; treat as DeepMind-asserted, not peer-validated.
- **Distillation to a single student model loses some teacher-ensemble accuracy.** The published `all_folds` model is a distilled student; per-fold teacher models (`fold-0` … `fold-3`) are available on HF Hub for users willing to ensemble at inference cost.
- **Context boundary effects.** The 4,096-bp flanking pad helps but variants near the edge of the 1-Mb window have less surrounding regulatory context than variants in the centre.

## Sources

**Primary publications:**
- **Nature paper (Jan 2026):** Avsec et al., "Advancing regulatory variant effect prediction with AlphaGenome," *Nature* 649(8099), 2026. [10.1038/s41586-025-10014-0](https://www.nature.com/articles/s41586-025-10014-0)
- **bioRxiv preprint (Jun 2025):** [10.1101/2025.06.25.661532v1](https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1) — coincident with DeepMind blog release
- **DeepMind paper PDF mirror:** [storage.googleapis.com/deepmind-media/papers/alphagenome.pdf](https://storage.googleapis.com/deepmind-media/papers/alphagenome.pdf)

**DeepMind communications (vendor-only — flagged accordingly above):**
- **Blog (Jun 2025):** [AlphaGenome: AI for better understanding the genome](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/)
- **Hosted API:** [deepmind.google.com/science/alphagenome](https://deepmind.google.com/science/alphagenome)

**Code and weights:**
- **API client (Apache 2.0):** [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome)
- **Research code (Apache 2.0, released Jan 2026):** [github.com/google-deepmind/alphagenome_research](https://github.com/google-deepmind/alphagenome_research)
- **Weights (non-commercial):** [huggingface.co/google/alphagenome-all-folds](https://huggingface.co/google/alphagenome-all-folds) — student model; per-fold teachers at `google/alphagenome-fold-0` … `fold-3`

**Press, commentary, and independent explainers:**
- **STAT News (Jan 2026 source release):** [DeepMind releases AlphaGenome source code](https://www.statnews.com/2026/01/28/deepmind-opens-alphagenome-source-code/)
- **STAT News (Jun 2025 launch):** [DeepMind launches AlphaGenome](https://www.statnews.com/2025/06/25/google-ai-deepmind-launches-alphagenome-new-model-to-predict-dna-encoding-gene-regulation/)
- **Science / AAAS news:** [DeepMind's latest AI tool makes sense of changes in the human genome](https://www.science.org/content/article/deepmind-s-latest-ai-tool-makes-sense-changes-human-genome)
- **Nature News:** [DeepMind's new AlphaGenome AI tackles the 'dark matter' in our DNA](https://www.nature.com/articles/d41586-025-01998-w)
- **C&EN (Jan 2026):** [Google's AlphaGenome predicts the function of a DNA sequence](https://cen.acs.org/biological-chemistry/genomics/Googles-AlphaGenome-predicts-function-DNA/104/web/2026/01)
- **Scientific American:** [DeepMind's AlphaGenome Uses AI to Decipher Noncoding DNA](https://www.scientificamerican.com/article/deepminds-alphagenome-uses-ai-to-decipher-noncoding-dna-for-research/)
- **Alzforum:** [Top Dog: AlphaGenome Predicts How Noncoding Variants Work](https://www.alzforum.org/news/research-news/top-dog-alphagenome-predicts-how-noncoding-variants-work)
- **Trends in Genetics commentary:** [AlphaGenome, a Swiss-army knife for exploring non-coding DNA](https://www.sciencedirect.com/science/article/pii/S0168952525002896)
- **Architecture deep-dives (independent):** [arxiviq.substack.com](https://arxiviq.substack.com/p/advancing-regulatory-variant-effect) — [rewire.it](https://rewire.it/blog/alphagenome-one-model-for-the-other-98-percent-of-your-dna/) — [livingbio.substack.com](https://livingbio.substack.com/p/understanding-alphagenome) — [binaryverseai.com](https://binaryverseai.com/alphagenome-explained/)
