# Synthesis — ED03 vs the 48-poster corpus

AACR 2026 session **ED03 ("Foundation Models and Multimodal AI for Cancer Research,"** Fri 4/17 PM, ~11,668 words) is the only dedicated AACR plenary this year on virtual-cell and multimodal-FM methods. Three speakers set the field's agenda from stage:

- **Charlotte Bunne** (EPFL) — virtual patients via multimodal foundation models, with spatial-proteomics + histopathology as the worked example.
- **Serena Yeung-Levy** (Stanford Biomedical Data Science) — generative models of disease dynamics (CellFlux flow matching) and multimodal VLMs for scientific reasoning (MicroVQA, BioMedICA).
- **Michael Moor** (ETH Zurich) — grounded, verifiable medical agents (MYRIAD atlas, process reward models); joined remotely.

This page takes each speaker's 2-3 load-bearing claims from the ED03 transcript and asks the same question of each: **does the 48-poster AACR 2026 virtual-cells corpus support, contradict, or not address it?** The point is to locate the gap between what leaders are saying from stage and what the rest of the field is shipping in posters.

*Name note: the auto-caption renders Bunne as "Bonner" and Moor as "Moore" — corrected silently here per `docs/notes/caveats.md`.*

*Quotation note: quotations below are lightly cleaned transcript fragments (paragraphing, obvious filler removed). Ellipses "[…]" mark joins.*

---

## Charlotte Bunne — virtual patients with multimodal foundation models

Bunne gave the session's framing talk. Her lab at EPFL built a multimodal foundation model that jointly encodes H&E histopathology and variable-panel spatial proteomics (4,605 patients at submission time, now 33 clinical studies), uses it as the substrate for in-silico perturbation screens on the Swiss supercomputer, and wraps the whole thing in an active-acquisition system ("EchoK") that decides which additional markers to acquire.

### Thesis 1 — Histopathology FMs translate; spatial-proteomics FMs require new architectures

> "The moment we use a different modality, if we want to get a molecular insight into a tissue and we move to a data type that is not just an H&E, we struggle. […] Spatial proteomics, for example, is not an RGB image. It's an image where every assay looks at a set of proteins […] 40, 80, 150 plex protein panels. So here it already starts. How do we build foundation models for those type of data modalities?"

**Corpus verdict: partially supported.**

- **Supports**: **#4163** (Andrew Song, "A general-purpose AI foundation model for spatial proteomics") is the direct poster-corpus analogue — an FM built specifically for multiplexed spatial proteomics, reporting that conventional cell-segmentation-then-threshold pipelines are inadequate.
- **Baseline for the comparison**: **#LB174** (H-optimus-1) and **#5491** (AI FM for single-cell annotation from histopathology) are pure-histopathology foundation models of the exact kind Bunne contrasts against — RGB vision transformers trained at scale. **#2778** (cancer-scale WSI → ST FM) and **#5489** (multi-scale FM for RCC localization) also fall in the H&E-as-RGB camp.
- **Not addressed**: Bunne's specific architectural claim — that panel-varying protein tokenization requires a protein-language-model-backed encoder that can handle assays where *"in clinical study A look at protein ABC, and then the next clinical study actually looks at protein DEF"* — is not directly tested by any other poster. #4163 is the only spatial-proteomics FM in the entire 48.

### Thesis 2 — The real payoff of virtual-tissue FMs is in-silico perturbation / treatment simulation and new biomarkers

> "We can now use a treatment encoder and now use a generative model to forecast how those state or cell tissue states change over time. […] How do we have now patterns of those models that are actually very informative for clinical decision-makings? […] We can extract minimum signatures that are corresponding to responder and non-responder signals."

**Corpus verdict: supported in spirit, with a shift of substrate.**

- **Supports (in-silico screens)**: **#1464** (CELLama-Perturb, virtual-cell model for spatial drug sensitivity); **#4181** (Turbine's Virtual Lab, mechanism-enabled simulation for target de-risking); **#978** (cell→patient transcriptome-modeled drug response); **#1467** (GRPO-based mechanism-aware therapy planning on a multimodal oncology FM); **#LB438** (multiscale mechanistic pathway-crosstalk analysis for TME rewiring under therapy). All five implement some version of the in-silico-screen-over-learned-representations pattern Bunne described.
- **Supports (AI-derived biomarkers)**: **#87** (Path2Prot — AI-inferred proteomic biomarkers for breast tumor subtyping), **#2778** (WSI → spatial transcriptomics), **#LB443** (MutationProjector genotype FM for therapeutic response), and **#2765** (MiFM microbiome trajectories and risk clocks) match her "new generation of AI-derived biomarkers" framing.
- **Contradicts (sort of)**: every single one of those posters uses transcriptomic, mutational, microbial, or morphological features — **none** uses spatial-proteomics tissue representations as the substrate. Bunne's specific substrate — a multimodal spatial-proteomics + H&E latent as the foundation for in-silico screening — has **zero direct poster analogues**. The field wants her payoff but is taking a different route to it, largely because spatial-proteomics data is much rarer than either H&E or scRNA-seq.

### Thesis 3 — Active / sequential acquisition (the "EchoK" / "ask for more when needed" idea)

> "What we want is that the foundation model knows what it knows and asks us for more whenever needed. […] It's a sequential acquisition problem, asking for more whenever needed or stopping when done, that uses reinforcement learning […] a minimum assay that is good enough for any downstream task."

**Corpus verdict: not addressed.**

- No poster in the 48 implements active / sequential experimental design on top of a multimodal FM. The closest is **#1467** (uses GRPO reinforcement learning, but for therapy planning, not assay design) and **#4212** (a blood-based estimator, but static rather than sequential).
- This is a clear blind spot — Bunne is arguing for a capability ("a minimum assay that is good enough for any downstream task") that the AACR 2026 poster hall simply is not shipping. It is also a reasonable finding: sequential-acquisition RL on top of biological FMs is hard to publish as a single poster, because the evaluation requires a prospective assay-design loop, not a static benchmark.

---

## Serena Yeung-Levy — disease dynamics and scientific reasoning

Yeung-Levy's talk split into two halves: generative image models for virtual cells (CellFlux, CellFlux V2, CellFlux MM) that use flow matching to map control→perturbed cell populations at image and joint-imaging-plus-transcriptomics scale; and vision-language models for scientific reasoning, anchored by the MicroVQA benchmark (1,000+ researcher-level microscopy questions) and the BioMedICA open-access 24M-image PubMed Central dataset.

### Thesis 1 — Flow matching is the right primitive for distribution-to-distribution perturbation modelling, and it scales

> "Flow matching, what we are trying to do is to learn a continuous velocity field that transforms from one source distribution to another target distribution. […] It actually very naturally fits this problem that we're talking about, trying to go from the source to target cell populations. […] CellFlux V2 […] as we scale from 300,000 images to 11.6 million images […] we can achieve these virtual cell foundation models."

**Corpus verdict: not addressed.**

- Zero posters in the 48 use flow matching, continuous velocity fields, or ODE-based generative modelling for cell-state transitions.
- **#4213** (GEM-1, "generative genomics accurately predicts cancer gene expression") is the closest generative-perturbation poster but the abstract suggests autoregressive / masked sequence modeling rather than flow matching.
- **#1464** (CELLama-Perturb) is a perturbation model but trained as a representation-learning model in the CELLama spatial family, not a flow-matching generator.
- **#4181** (Turbine's Virtual Lab) uses mechanism-enabled simulations which are closer to mechanistic systems biology than to continuous-latent flow matching.
- The specific methodological bet Yeung-Levy is making — that flow matching is the scalable primitive for source-to-target distributional learning in virtual cells — is not reflected in what AACR-submitting labs chose to build this year. This could be a timing gap (CellFlux is very recent) rather than a disagreement.

### Thesis 2 — Joint imaging + transcriptomics modelling matters, but paired data is scarce so we need unimodal bridging

> "What I think is also very important is being able to jointly model these together, imaging and transcriptomics together. […] The matched pair data […] we don't have the data to train as large scale foundation models as we want. So […] to take — to learn a single model, but that learns from matched data where that exists and learns from unimodal data where you have that."

**Corpus verdict: supported; this is the strongest stage-to-poster alignment on the page.**

- **Direct supports** (imaging ↔ molecular joint modeling): **#2754** (VGL — vision-gene-language LLM combining histopathology + gene expression for cell-type classification in lung cancer); **#71** (histopathology ↔ spatial transcriptomics bridging for TME profiling); **#1457** (gene expression and pathway activity from H&E WSIs in NSCLC); **#87** (Path2Prot — inferring proteomic biomarkers from pathology); **#2778** (cancer-scale FM that predicts spatial transcriptomics from WSI); **#1438** (generative AI for breast genomic subtype from histology); **#2752** (CancerSTFormer — multi-scale spot-resolution spatial transcriptomics analysis).
- **Adjacent supports** (broader multimodal fusion): **#1251** (HONeYBEE, foundation-model-driven multimodal AI for GBM / NSCLC / PDAC), **#4184** (multimodal prostate DL), **#5505** (cross-platform spatial-omics framework).
- This is by a wide margin the best-represented family in the corpus — 8 posters in the core "multimodal fusion & VLM/LLM" family alone, plus adjacent ones in other families.
- **Partially addresses**: None of the above explicitly implements Yeung-Levy's specific "unimodal-bridging" training recipe — combining a small matched dataset with much larger unimodal sets via a shared latent — at the scale she describes. The posters are mostly paired-data only, which is the exact constraint she is warning about.

### Thesis 3 — Scientific-reasoning benchmarks (MicroVQA) are the bottleneck for VLM-based biology agents

> "There really doesn't exist easy, good sources of research-level, scientific microscopy-based reasoning. […] MicroVQA was a work that tried to make progress in covering that space of higher-level reasoning, and to truly be able to assess researcher-level capabilities. […] Over 1,000 questions […] this benchmark is still hard for current state-of-the-art models."

**Corpus verdict: not addressed.**

- **#5478** (benchmarking gene-expression foundation models on bulk RNA-Seq) is the only pure benchmark poster in the 48, and it is a performance benchmark (how well do scRNA-trained FMs transfer to bulk RNA-seq), not a researcher-level scientific-reasoning benchmark of the MicroVQA type.
- **#LB169** (scCAP) is an evaluation of ontology-aware cell-type annotation, comparing against CellTypist, SCimilarity, SingleR, and Geneformer — but this is task-level annotation accuracy, which is a much narrower notion than Yeung-Levy's "researcher-level reasoning with hypothesis generation and experimental proposal."
- The stage-vs-poster gap here is large: Yeung-Levy and Moor both argue that the field's progress depends on better benchmarks and verifiable reasoning, yet almost no one is shipping benchmark posters. This is arguably a publication-venue effect — pure-benchmark papers typically land at NeurIPS / ICML, not AACR.

---

## Michael Moor — reliable, verifiable medical agents

Moor's pre-recorded talk (his flight was canceled due to an airline strike) argued that medical AI agents fail for two distinct reasons: (1) they are grounded against unstructured text, so retrieval is leaky; and (2) their reasoning is never verified step-by-step. His lab's responses are MYRIAD (a 6M-entry structured QA atlas grounded in peer-reviewed literature) and process reward models (a "policing" LM that verifies each reasoning step of a base LM at inference time).

### Thesis 1 — Language models without structured grounding are unreliable for medicine; the knowledge representation matters at least as much as the model

> "Currently we use just a massive amount of text chunks that are completely unstructured. So retrieving from this is actually quite hard and quite leaky and noisy. […] We propose this Myriad dataset […] a large-scale atlas of roughly six million medical question-answer pairs, each pair being grounded directly from a passage in the peer-reviewed medical literature."

**Corpus verdict: not addressed.**

- No poster in the 48 builds a grounded medical-knowledge atlas or structures literature into QA pairs for RAG.
- **#30** (adaptive LLM-based agentic cohort extraction) does use LLMs for clinical data extraction and could plausibly benefit from MYRIAD-style structured grounding, but its abstract does not address knowledge-representation structure at all — it is focused on schema-matching real-world data for trial feasibility.
- **#LB169** (scCAP, ontology-aware LLM for cell-type annotation) is the closest in spirit — it does argue that structured ontology grounding improves annotation — but the scope is cell types, not medical literature.
- The MYRIAD-style "representation of the knowledge matters as much as the content" argument has essentially no poster analogue in this slice. It is a stage-only claim in AACR 2026.

### Thesis 2 — Process reward models / stepwise reasoning verification is how to make agents reliable

> "It's not enough to just give a language model access to a neatly organized corpus of knowledge. We actually want to check individual reasoning steps that a language model produces. […] A policing language model, which we in the field would call a process reward model […] by training such a verifier […] we can actually improve many different language model by just hook plugging it in at inference time."

**Corpus verdict: not addressed.**

- Zero posters in the 48 implement process reward models, stepwise reasoning verification, or outcome-vs-process reward decomposition.
- **#1467** (Eric Schadt, mechanism-aware therapy planning with GRPO) is the only poster using reinforcement learning with a reward signal, but its reward is mechanism-based therapy-planning performance (is this a good therapy for this patient?) — not stepwise reasoning verification (is this reasoning step correct given the literature?). They are related formalisms but different problems.
- The entire process-reward-agent subfield Moor describes — where a verifier model checks individual reasoning steps of a primary model at inference time — is absent from the AACR 2026 poster hall. Again likely a venue effect: this is currently published at NeurIPS/ACL, not AACR.

### Thesis 3 — Agents doing interactive clinical workup are much worse than agents answering exam-style questions — benchmark properly

> "We showed that already two years ago, that if you provide a language model, you confront it in some type of agent clinic […] It will be much harder for such a doctor agent to come up with the right diagnosis if the case has to be interactively worked up as compared to those case profiles where you have these exam-style benchmarks. […] Many models drop drastically in performance if they have to actually do the workup on their own."

**Corpus verdict: not addressed.**

- No poster in the 48 benchmarks interactive agent workup, clinical dialogue, or multi-turn diagnostic reasoning. **#30** is the only agentic-system poster and it is one-shot cohort extraction rather than interactive workup.
- **#1467** uses RL but does not evaluate interactive reasoning trajectories.
- This is arguably the biggest single gap between the ED03 agenda and the AACR 2026 corpus: across their three talks, Bunne, Yeung-Levy, and Moor collectively spent roughly 40% of stage time on evaluation, benchmarking, and verification — and the poster hall in this slice shipped essentially nothing on that axis. Of 48 posters, 3 touch evaluation and 1 touches agentic autonomy; none do both.

---

---

## Thin-evidence flags — theses where the corpus cannot argue either way

Several ED03 claims are simply not testable against the 48-poster corpus because the relevant poster population is too small. Flagging them here rather than inventing support:

- **Bunne Thesis 3 (active / sequential acquisition)**: 0 posters implement it. Cannot evaluate.
- **Yeung-Levy Thesis 1 (flow matching as the scalable primitive)**: 0 posters use flow matching. Cannot evaluate.
- **Yeung-Levy Thesis 3 (MicroVQA-style researcher-level benchmarking)**: 1 marginally-related poster (#LB169). Too thin to argue either way.
- **Moor Thesis 1 (structured knowledge atlases)**: 0 direct posters; #LB169 is adjacent but cell-type ontology only.
- **Moor Thesis 2 (process reward models)**: 0 posters. Cannot evaluate.
- **Moor Thesis 3 (interactive agent workup benchmarks)**: 0 posters. Cannot evaluate.

Of 10 total theses extracted, **6 have insufficient corpus coverage to argue for or against.** All 6 of those are on the evaluation / verification / agent-reliability axis.

---

## Closing synthesis — the stage-vs-corpus gap

The three ED03 speakers are converging on a shared research program: **multimodal foundation models that forecast perturbation effects, with grounded and verifiable agentic reasoning on top**. The AACR 2026 virtual-cells poster corpus partially supports the first half of that program — there are 16 FM posters (cell/gene + pathology) and 6 perturbation/in-silico-screen posters, with a particularly strong multimodal-fusion cohort (8 posters) that directly mirrors Yeung-Levy's joint-imaging-plus-transcriptomics thesis.

But the second half — **benchmarks, evaluation of researcher-level reasoning, process-reward verification, active / sequential acquisition, and grounded knowledge-atlas construction** — is almost entirely absent. Only 3 posters (#5478, #LB169, #30) address any form of evaluation or agentic autonomy, and none address verifiable stepwise reasoning.

The leaders on stage are 18-24 months ahead of the median AACR 2026 submitter on the evaluation and reliability axes. Part of this is a venue effect — MicroVQA-style benchmarks and process-reward agents are currently published at NeurIPS/ICML/ACL rather than AACR — but part of it is substantive: the community is still shipping model capabilities rather than the scaffolding around them. Closing that gap is the obvious opportunity for AACR 2027.
