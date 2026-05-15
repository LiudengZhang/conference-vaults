# Segmentation Foundation Models at ISBI 2026 — Synthesis

**Synthesis dossier covering SAM-3 / MedSAM / SegVol successor models surfacing across ISBI 2026 main proceedings and the FAIBI + Exploring-FM-in-Medical-Image-Analysis workshops — the segmentation-FM axis that bridges CVPR architectures to MICCAI medical adaptation.**

- **Speaker(s) / Authors:** Multiple — main-proceedings authors + workshop presenters across FAIBI 2nd ed. and Exploring FM in Medical Image Analysis (organizers Gu / Chen / Yang / Zheng / Zhou / Shen)
- **Affiliation(s):** Multi-institutional — Tohoku, Sheffield, Emory/GT, Liverpool, UCL, ShanghaiTech, plus Stirling/MD Anderson/Imperial (FAIBI co-organizers)
- **Anchor type:** synthesis / methods
- **Track / day:** ISBI 2026 main proceedings (Thu Apr 9 – Fri Apr 10) + Fri Apr 10 PM workshop + Sat Apr 11 PM workshop
- **IEEE Xplore:** TBD (multiple Xplore DOIs across main proceedings + workshop volumes — individual papers get their own tool pages where artifacts released)
- **Status:** post-meeting

## What it does

This synthesis tracks the SAM-3 / MedSAM / SegVol successor line at ISBI 2026 — promptable segmentation foundation models adapted for medical imaging. The axis covers (a) SAM-3 medical adaptations (continued from SAM / SAM-2 lineage), (b) MedSAM successors with expanded modality coverage (CT, MR, US, microscopy, pathology), (c) SegVol-style volumetric promptable segmenters, (d) text-promptable medical segmentation models. Cancer-relevance is via tumor segmentation across modalities — the backbone use case for radiotherapy planning, radiomics, treatment-response measurement.

## How it works / methodology

The shared recipe: pretrain a large image encoder (often initialized from SAM / DINOv2 / a medical FM checkpoint), pair with a prompt encoder (points / boxes / masks / text), train on large multi-modal medical segmentation corpora (often >1M masks across CT / MR / US / pathology), evaluate on held-out tumor / organ / lesion segmentation benchmarks. Variations cover prompt modality (interactive vs text vs auto), 2D vs 3D, supervised vs self-supervised pretraining, generalist vs modality-specific specialization.

## Headline benchmarks

TBD — synthesis-level. Anchor benchmarks across the SAM-medical line: BraTS (brain tumor MR), KiTS (kidney CT), LiTS (liver CT), TotalSegmentator (multi-organ CT), MSD (Medical Segmentation Decathlon), AMOS (abdominal multi-organ). Specific ISBI 2026 paper-level deltas extracted into per-tool pages once IEEE Xplore indexes proceedings (~early May 2026).

## How it works

**Core idea.** Promptable segmentation foundation models replace per-task / per-dataset segmentation training with a single large model that produces segmentation masks **conditional on a prompt** (point, box, mask, or text). Medical adaptations (MedSAM, SegVol, SAM-3-medical successors) port this promptable paradigm to CT / MR / US / pathology / microscopy, where the prompt encodes clinician intent (point at a tumor, click on an organ, describe an anatomical structure).

**Inputs / outputs.** Inputs: an image (2D slice or 3D volume) plus one or more prompts (points with positive/negative polarity, bounding boxes, coarse masks, or natural-language descriptions like "left kidney"). Outputs: a binary or multi-class segmentation mask aligned with the prompt; for some variants, ranked candidate masks with quality scores.

**Key innovation.** Three shifts from per-dataset U-Nets: (1) pretraining on >1M masks across heterogeneous medical modalities so the same model handles CT, MR, US, and pathology, (2) prompt conditioning that decouples model capability from task specification, (3) zero-shot generalization to anatomical structures never explicitly labeled in training. SegVol-line models extend this to native 3D promptable volumetric segmentation, closing the 2D-to-3D gap that hampered earlier SAM-medical adaptations.

**Parameters.** SAM-3 / MedSAM scale: ViT-H/16 image encoder (~600M parameters), small prompt encoder (<10M), mask decoder (~10M). SegVol-class 3D: typically 100–300M parameters with patch-based volumetric processing. Training compute: thousands of GPU-days on multi-million-mask corpora.

**Canonical example.** Tumor segmentation on a 3D liver CT: clinician places a single positive point inside the tumor and an optional negative point on adjacent vessel; SegVol returns a 3D tumor mask in seconds; mask quality measured against the LiTS / KiTS held-out annotation. BraTS brain-tumor canonical example: text prompt "enhancing tumor" applied to a 3D MRI → segmentation mask scored against BraTS multi-region ground truth.

## Where it fits in the corpus

- **AACR 2026:** indirect — tumor segmentation feeds radiomics and treatment-response endpoints; no direct pathology-FM crosswalk but cross-modal generalist medical FMs may overlap
- **MICCAI 2026:** strong sibling — most ISBI 2026 segmentation-FM papers will have MICCAI cousin papers (Sep 27–Oct 1); BraTS / KiTS / AMOS challenge results land at MICCAI
- **RSNA 2026:** clinical-deployment counterpart — radiotherapy / treatment-planning systems use these segmenters; RSNA tool index gets the deployed-product entries
- **CVPR 2026:** architecture upstream — SAM-3 line originates at CVPR / NeurIPS, ISBI adapts ~6 months later

## Notes

This is a synthesis page, not a single-tool page — individual named-model papers (specific SAM-3 medical successors, specific MedSAM v3 / SegVol v2 releases) get their own tool pages once IEEE Xplore indexes the proceedings. The synthesis exists as a navigation anchor in the vault for the broader segmentation-FM axis that spans ISBI main proceedings, both relevant workshops (FAIBI Sat Apr 11 PM, Exploring FM in Medical Image Analysis Fri Apr 10 PM), and the MICCAI 2026 cousin-paper pattern.
