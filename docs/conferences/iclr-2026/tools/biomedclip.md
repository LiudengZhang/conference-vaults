# BioMedCLIP — Zhang, Xu et al. (Microsoft Research)

**One-line description** — A CLIP-style biomedical vision-language foundation model pretrained contrastively on **PMC-15M** (15,282,336 image-caption pairs harvested from 4.4 million PubMed Central Open Access articles) — two orders of magnitude larger than MIMIC-CXR — that pairs a ViT-B/16 image encoder with a PubMedBERT text encoder and beats both general-domain CLIP and domain-specific radiology models (BioViL) across retrieval, zero-shot classification, and visual question answering.

- **Authors:** Sheng Zhang, Yanbo Xu, Naoto Usuyama, Hanwen Xu, Jaspreet Bagga, Robert Tinn, Sam Preston, Rajesh Rao, Mu Wei, Naveen Valluri, Cliff Wong, Andrea Tupini, Yu Wang, Matt Mazzola, Swadheen Shukla, Lars Liden, Jianfeng Gao, Angela Crabtree, Brian Piening, Carlo Bifulco, Matthew P. Lungren, Tristan Naumann, Sheng Wang, Hoifung Poon
- **Affiliation(s):** Microsoft Research; Microsoft Health & Life Sciences; University of Washington; Providence St. Joseph Health; Stanford
- **Track / workshop:** Not an ICLR 2026 paper — included in this vault as a **load-bearing foundation-model dependency** for ICLR 2026 biomedical-imaging and VQA entries (any pathology / radiology zero-shot or retrieval baseline submitted to LMRL or main-track imaging tracks defaults to BioMedCLIP or its derivatives)
- **NEJM AI (2024 publication of record):** Zhang S. et al., *NEJM AI* 2(1): AIoa2400640, January 2025 (received Jun 23 2024; accepted Sep 26 2024) — [10.1056/AIoa2400640](https://ai.nejm.org/doi/abs/10.1056/AIoa2400640)
- **arXiv (preprint, 2023):** [2303.00915](https://arxiv.org/abs/2303.00915) (v3 current)
- **Microsoft Research project page:** [microsoft.com/research/publication/biomedclip](https://www.microsoft.com/en-us/research/publication/biomedclip-a-multimodal-biomedical-foundation-model-pretrained-from-fifteen-million-scientific-image-text-pairs/)
- **Weights:** [huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224) — distributed under the **MIT License** at `aka.ms/biomedclip`
- **Data pipeline code:** [github.com/microsoft/BiomedCLIP_data_pipeline](https://github.com/microsoft/BiomedCLIP_data_pipeline)

## What it does

BioMedCLIP is a dual-encoder contrastive vision-language model that maps biomedical images and the captions that describe them into a shared embedding space. Given a chest X-ray, histopathology tile, gross specimen, fluorescence-microscopy image, gel, or chart, you can retrieve the most-similar caption (or vice versa), zero-shot classify with arbitrary text labels (no fine-tuning per class), or use the visual encoder as a frozen backbone for downstream segmentation, classification, or VQA heads. It is the default open-weights biomedical CLIP for non-radiology imagery — radiology-specific competitors (BioViL, CheXzero) cover chest X-rays well but degrade on histopathology, microscopy, and the long tail of figure-panel images that PMC-15M covers.

## How it works

**Architecture.** Two-tower dual encoder:

- **Image encoder:** Vision Transformer **ViT-B/16** (12 layers, 768-dim, 86M params), with 224×224 input by default and a 448×448 variant for the higher-resolution release. Each image is split into 16×16 patches, linearly projected, and processed by self-attention layers; the [CLS] token output is linearly projected into the joint embedding space.
- **Text encoder:** **PubMedBERT** (Gu et al. 2021) — a BERT pretrained from scratch on biomedical abstracts and full-text articles. This is the key domain swap versus general-domain CLIP, which uses a GPT-2-class encoder trained on web text and has no exposure to medical terminology. The tokenizer is extended to a **256-token context** (vs. CLIP's 77) to accommodate the longer, more technical captions found in figure legends.

Both encoders end in a linear projection to a shared embedding dimension; cosine similarity in that space is the retrieval / classification signal.

**Pretraining corpus — PMC-15M.** The PMC-15M dataset was systematically constructed by parsing **4.4 million scientific articles** from the **PubMed Central Open Access Subset** with scalable cloud infrastructure, extracting and cleaning **15,282,336 image-caption pairs**. This is **roughly 100× larger than MIMIC-CXR** (the previous standard biomedical image-text corpus, ~370k chest-X-ray reports) and covers the full distribution of biomedical figure types — radiology, histopathology, electron microscopy, gross specimens, gels, plots, schematics, charts. Compound figures with sub-panels are handled by a panel-splitting pipeline so a single caption is not naively paired with an unrelated sub-image.

**Pretraining objective.** Standard **CLIP InfoNCE contrastive loss** on image-caption pairs: maximise cosine similarity for true pairs within a batch while minimising similarity to all in-batch negatives, symmetric over both directions. Domain adaptations relative to vanilla CLIP include the PubMedBERT text encoder, the extended 256-token context, batch composition strategies that balance modality coverage, and pretraining-from-scratch rather than continued-pretraining from OpenAI CLIP (which would inherit web-text alignment bias).

**Parameter count.** ViT-B/16 image encoder is **~86M parameters**; PubMedBERT-base text encoder is **~110M parameters**. Total model size is on the order of **~200M parameters** — small enough to run on a single GPU at inference, deliberately, for clinical-deployment plausibility.

**Compute.** Pretraining was run on Microsoft's Azure GPU infrastructure; the paper does not report a single headline FLOP number but documents training-from-scratch on PMC-15M with standard CLIP-class batch sizes. PMC-15M construction itself was a substantial cloud-compute effort separate from model training.

**Fine-tuning recipe.** Three standard downstream routes, all detailed in the NEJM AI paper:

1. **Zero-shot classification** — encode the image, encode each candidate text label ("a histopathology image of breast carcinoma" vs "a histopathology image of normal tissue"), pick the highest cosine similarity. No gradient updates.
2. **Linear probe / frozen-encoder fine-tuning** — freeze the visual backbone, train a logistic-regression or MLP head on labelled data.
3. **Full fine-tuning** — unfreeze the visual encoder for task-specific supervised training (recommended only when labelled data is in the >10k regime).

For VQA, the standard recipe couples the BioMedCLIP visual encoder with a downstream language-model decoder (e.g. PMC-LLaMA, LLaVA-Med); BioMedCLIP itself does not include a generative head.

## Headline results

- **Image-text retrieval (PMC-15M held-out test).** ViT-B/16-224 with the PubMedBERT 256-token text encoder reaches **R@1 ≈ 87.3** on image-to-text retrieval; the higher-resolution **ViT-B/16-448** variant reaches **R@1 ≈ 89.4** — substantially above general-domain CLIP baselines on biomedical text.
- **Visual Question Answering.** On **VQA-RAD** BioMedCLIP-backed VQA reaches **75.8% overall accuracy**; on **SLAKE** it reaches **86.5% overall** — state-of-the-art at publication time, with particularly strong performance on closed-ended (yes/no) questions.
- **Zero-shot classification.** BioMedCLIP sets new state of the art across standard biomedical image classification benchmarks (RSNA pneumonia, multiple histopathology suites) and — notably — **outperforms radiology-specific models like BioViL on radiology tasks**, despite being trained on a broader, non-radiology-centric corpus. This is the paper's headline scaling-law argument: 15M diverse pairs beats domain-purified narrow pretraining.
- **Cross-modality robustness.** Beats general-domain CLIP across all biomedical modalities tested and beats radiology-specific BioViL across radiology + non-radiology averaged.

## Why it matters — versus general CLIP

Three concrete shifts:

1. **Domain text encoder, not domain fine-tuning.** Replacing CLIP's GPT-2-class web-text encoder with PubMedBERT — a model that has seen the actual vocabulary distribution of biomedical figure captions (gene names, anatomical terms, drug names, abbreviations) — is a larger gain than continued-pretraining the standard CLIP text tower on biomedical data. Domain mismatch in the text tower was the dominant bottleneck.
2. **Long captions are first-class.** Biomedical figure legends are 5–10× longer than natural-image captions; the 256-token context (vs. CLIP's 77) avoids truncating the most diagnostically informative half of every legend.
3. **Generalisation across the long tail.** The PMC-15M corpus spans radiology, pathology, microscopy, gels, charts, schematics — the long tail of biomedical figures that narrow datasets (MIMIC-CXR, CheXpert) ignore. This is why BioMedCLIP beats radiology-specific models even on radiology: the cross-modality scale dominates the within-modality purity.

For the ICLR / NeurIPS / AACR vault: BioMedCLIP is the default open-weights starting point for biomedical visual representation learning. Subsequent specialist models (PathCLIP, QuiltNet, PLIP for pathology; CONCH; Med-Flamingo; LLaVA-Med) either ablate against it or continue-pretrain from it.

## Known limitations

- **PMC-15M is harvested from published-figure captions, not clinical reports.** The text style is "figure legend in a published paper" — concise, terminological, often pointing at sub-panels with arrows / colors that the image alone cannot resolve. This is *not* the distribution of either clinical-radiology reports (long, narrative, hedged) or pathology sign-outs.
- **Publication bias.** PMC-OA over-represents diseases that get published (cancer, COVID-era pneumonia, common-radiology findings) and under-represents rare and rural-medicine pathology.
- **Caption-image misalignment in compound figures.** Even with panel-splitting heuristics, sub-panel-to-sub-caption alignment is imperfect; some training pairs are noisy.
- **Modality coverage is not balanced.** Some modalities (chest X-ray, H&E pathology) are over-represented relative to others (echocardiography video, EEG traces, OCT volumes) because of what PMC publishes.
- **Static at the 2024 cutoff.** PMC continues to grow and disease vocabulary continues to evolve (new drug names, new variant nomenclatures); the released checkpoint is not retrained on rolling data.
- **VQA is not native.** BioMedCLIP itself is a dual-encoder retrieval model; VQA requires bolting on a generative decoder (LLaVA-Med, BiomedGPT, etc.) — the reported VQA-RAD / SLAKE numbers are for those derivative pipelines.
- **Demographic bias inherited from PubMed corpus.** Population coverage in PMC is biased toward US / European / East-Asian academic-medicine cohorts; performance on under-represented populations is not separately characterised in the paper.

## Where it fits in the corpus

- **ICLR 2026 main-track imaging entries:** any pathology / radiology zero-shot baseline or frozen-encoder linear-probe result is computed against BioMedCLIP — it is the published baseline.
- **AACR 2026 pathology axis:** the closest commercially-deployable analog of CONCH / PLIP for digital-pathology applications; BioMedCLIP is the natural baseline for any AACR 2026 H&E-foundation-model demo.
- **MICCAI 2026 / RSNA 2026:** continues to be the default biomedical vision-language pretraining baseline.
- **NeurIPS 2026 / ICML 2026:** successor models (BiomedCLIP-V2, CONCH-v2, MedCLIP-class derivatives) ablate against this checkpoint.

## Sources

- Zhang S., Xu Y., Usuyama N. et al., "A Multimodal Biomedical Foundation Model Trained from Fifteen Million Image-Text Pairs," *NEJM AI* 2(1): AIoa2400640 (January 2025) — [DOI](https://ai.nejm.org/doi/abs/10.1056/AIoa2400640)
- arXiv preprint (2023, v3 current): "BiomedCLIP: a multimodal biomedical foundation model pretrained from fifteen million scientific image-text pairs" — [2303.00915](https://arxiv.org/abs/2303.00915)
- Microsoft Research project page: [microsoft.com/research/publication/biomedclip](https://www.microsoft.com/en-us/research/publication/biomedclip-a-multimodal-biomedical-foundation-model-pretrained-from-fifteen-million-scientific-image-text-pairs/)
- Hugging Face weights (MIT-licensed): [microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224)
- Data pipeline code: [github.com/microsoft/BiomedCLIP_data_pipeline](https://github.com/microsoft/BiomedCLIP_data_pipeline)
- Microsoft Foundry Models catalog listing: [ai.azure.com/catalog/models/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224](https://ai.azure.com/catalog/models/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224)
- alphaXiv overview (architecture / training details): [alphaxiv.org/overview/2303.00915](https://www.alphaxiv.org/overview/2303.00915)
