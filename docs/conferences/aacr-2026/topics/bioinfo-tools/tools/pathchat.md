# PathChat / PathChat-2

**Family:** path-fm (vision-language)
**Modality:** H&E and IHC histology images (tile / ROI level) + free-text clinical context; outputs natural-language answers, diagnoses, and rationale
**Released:** PathChat: Nature, June 2024 (Lu et al., Mahmood Lab); PathChat+ / PathChat-2: 2024 follow-up; PathChat DX: FDA Breakthrough Device Designation, January 2025 (Modella AI)
**License:** PathChat weights are not openly redistributed — academic access via Mahmood Lab request; clinical "PathChat DX" version is commercial via Modella AI. The Nature 2024 paper is open access
**Code/checkpoint:** [comp-path.bwh.harvard.edu/pathchat](https://comp-path.bwh.harvard.edu/pathchat/) (access request); [modella.ai/pathchat](https://www.modella.ai/pathchat) (commercial)
**Also surfaced in:** agentic-ai, virtual-cells

> PathChat is a multimodal vision-language assistant for pathology
> from the Mahmood Lab (Mass General Brigham / Harvard) — a histology
> "copilot" that accepts an H&E or IHC region of interest plus
> free-text clinical context and returns natural-language answers,
> differential diagnoses, and explanations. It is built by pairing a
> pathology-tuned vision encoder (UNI, further aligned to text on 1.18M
> pathology image-caption pairs) with a 13B-parameter Llama-2 LLM via
> a LLaVA-style multimodal projector, then instruction-tuning the
> stack on 456,916 visual-language instruction pairs covering 999,202
> question-answer turns. The clinical-grade follow-up, PathChat DX,
> was granted FDA Breakthrough Device Designation in January 2025 —
> one of the first generative-AI pathology tools to receive the
> designation.

## Architecture & training

**Vision encoder.** PathChat re-uses the **UNI** ViT-L/16 backbone
from the same lab, pretrained on ~100M H&E tiles from ~100K slides via
DINOv2 self-supervision. A vision-language alignment stage further
trains this encoder on **1.18 million pathology image-caption pairs**
(curated from textbooks, PubMed Central figures, and lab-internal
sources) — this stage is conceptually equivalent to CONCH-style
contrastive alignment and produces a text-aware vision encoder.

**LLM backbone.** A **13B-parameter Llama-2** chat model. The vision
encoder feeds the LLM through a multimodal projector module in the
LLaVA-1.5 style: image tokens are concatenated to the text token
stream before the first transformer layer.

**Instruction tuning.** The full stack is fine-tuned end-to-end (or
LoRA-style — the paper uses full-MLLM tuning) on **456,916 unique
visual-language instructions covering 999,202 question-answer turns**.
The earlier arXiv preprint (2312.07814) reports a smaller 257K
instruction set; the published Nature version expanded to the 456K
figure. Instructions span tumor identification, grading,
differential diagnosis, biomarker reasoning, and IHC interpretation.

**PathChat+ / PathChat-2.** A follow-up MLLM trained on **>1 million
pathology-specific instruction samples and ~5.5M Q-A turns**, with
upgraded vision encoder and instruction curation. PathChat+ reports
**80.0% accuracy on a held-out differential-diagnosis benchmark**, a
+8 absolute-point lift over PathChat-1. PathChat DX is the
clinically-validated derivative carrying the FDA Breakthrough
Designation.

## Headline benchmarks

**Multiple-choice diagnostic accuracy (Nature 2024, image only):**
- **PathChat: 78.1%** image-only; **89.5%** when patient clinical
  context (age, sex, history, radiology) is added.
- The arXiv preprint reports 70.8% image-only / 81.2% with context for
  an earlier checkpoint — the +50%-pt and +52%-pt gaps vs. LLaVA-1.5
  and LLaVA-Med in the preprint reflect that earlier checkpoint.

**Head-to-head pairwise win rates (Nature 2024 evaluation by
board-certified pathologists, open-ended responses):**

| Comparator   | PathChat median win rate |
|--------------|--------------------------|
| GPT-4V       | 56.5%                    |
| LLaVA-1.5    | 67.7%                    |
| LLaVA-Med    | 74.2%                    |

PathChat beats GPT-4V on pathologist preference even though GPT-4V
operates with a vastly larger underlying LLM — the gap is driven by
the pathology-tuned vision encoder.

**vs. UNI / Virchow / Prov-GigaPath.** These are vision-only feature
extractors and are not directly comparable on the QA / chat tasks
PathChat is benchmarked on. The closest analogue is CONCH, also from
the Mahmood Lab; PathChat re-uses CONCH-class alignment data but adds
the generative LLM head, so it competes with LLaVA-Med rather than
with UNI.

## Why it matters for AACR / clinical pathology

- **First MLLM pathology copilot with FDA Breakthrough Designation.**
  PathChat DX (Modella AI, January 2025) is among the first generative
  AI tools for pathology to receive Breakthrough Device Designation,
  making PathChat the most regulatorily mature item in this catalog.
- **Closes the loop with clinical context.** The +11.4-pt accuracy
  gain from adding text-based clinical context (78.1% → 89.5%) is a
  direct experimental answer to a question AACR sessions repeatedly
  pose: how much does multimodal context actually move the needle on
  diagnostic accuracy?
- **Agentic AI substrate.** Several AACR 2026 agentic-AI sessions
  describe pathologist-in-the-loop AI; PathChat is the canonical
  example of the underlying primitive (image + text → reasoning).

## Known limitations

- **Closed weights.** PathChat is not redistributed under an
  open-source license; academic users must request access through
  the Mahmood Lab portal, and commercial use is mediated through
  Modella AI.
- **ROI-level, not WSI-native.** PathChat operates on
  pathologist-selected regions of interest, not whole gigapixel
  slides — the system does not include a slide-level aggregator and
  therefore depends on upstream ROI selection (manual or via a
  separate WSI model).
- **Llama-2 backbone is aging.** The 13B Llama-2 LLM was
  state-of-the-art in 2023 but trails Llama-3.x and Qwen-2.x on
  general reasoning by 2026; PathChat-2 / DX is presumed to update
  the backbone but details are not fully public.
- **English-only.** All instruction tuning and clinical context is
  English-language; multilingual deployment is not evaluated.
- **Hallucination risk on rare entities.** The Nature paper documents
  cases where PathChat fabricates plausible-but-wrong differential
  diagnoses for tumor entities under-represented in the
  instruction-tuning corpus — a generic MLLM failure mode that is
  load-bearing here because outputs look authoritative.

## Sources

- Lu M.Y., Chen B., Williamson D.F.K., Chen R.J., Zhao M., Chow A.K.,
  Ikemura K., Kim A., Pouli D., Patel A., Soliman A., Chen C., Ding T.,
  Wang J.J., Gerber G., Liang I., Le L.P., Parwani A.V., Weishaupt L.L.,
  Mahmood F. (2024). *A multimodal generative AI copilot for human
  pathology.* Nature 634, 466-473. [doi:10.1038/s41586-024-07618-3](https://doi.org/10.1038/s41586-024-07618-3) — open access.
- Lu M.Y. et al. (2023). *A Foundational Multimodal Vision Language AI
  Assistant for Human Pathology.* [arXiv:2312.07814](https://arxiv.org/abs/2312.07814) — preprint with the earlier 257K instruction set and 70.8% benchmark.
- Mahmood Lab landing page: [comp-path.bwh.harvard.edu/pathchat](https://comp-path.bwh.harvard.edu/pathchat/).
- Modella AI commercial site and FDA Breakthrough announcement (Jan
  2025): [modella.ai/pathchat-fda-breakthrough-designation](https://www.modella.ai/pathchat-fda-breakthrough-designation).
- Nature Biotechnology research-highlight commentary: *Vision-language
  AI assistance in human pathology.* [nature.com/articles/s41587-024-02326-9](https://www.nature.com/articles/s41587-024-02326-9).
- License: Nature paper is open access (CC-BY); model weights are not
  openly redistributed.

## Use in the AACR 2026 corpus

<!-- mentions:start -->

_Mention scan pending — populated by the alias-matching pipeline used
for UNI, CHIEF, and Prov-GigaPath._

<!-- mentions:end -->
