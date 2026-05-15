# FAIBI 2nd Edition — Foundation AI models in Biomedical Imaging (Workshop)

**Closing-day workshop on foundation models in biomedical imaging, co-organized by Jia Wu (MD Anderson Cancer Center) — direct cancer-center authorship signal among the workshop slate, with explicit oncology-imaging FM emphasis.**

- **Speaker(s) / Authors:** Co-organizers: Sharib Ali (Stirling), Rashid Qureshi (Salim Habib University), Islem Rekik (Imperial College London), **Jia Wu (MD Anderson Cancer Center)**, Mohsin Bilal (Birmingham City)
- **Affiliation(s):** Stirling · Salim Habib · Imperial · **MD Anderson Cancer Center** · Birmingham City
- **Anchor type:** workshop / synthesis
- **Track / day:** Sat Apr 11 PM (closing day, satellite track)
- **IEEE Xplore:** TBD (workshop papers indexed separately from main proceedings; some FAIBI papers may appear as Xplore workshop volumes)
- **Status:** post-meeting

## What it does

FAIBI 2nd edition consolidates foundation-model methods for biomedical imaging across pathology, radiology, microscopy, and multimodal — the same author pool that populates MICCAI's COMPAY / DGM4MICCAI workshops and CVPR's FMV / MMFM-BIOMED. The cancer-relevance hook is Jia Wu's co-organizer slot: Wu's MD Anderson group focuses on radiomics, radiogenomics, and FM-based oncology imaging biomarkers, which biases the program toward cancer-axis FM applications relative to FAIBI 1st edition.

## How it works / methodology

Workshop-format: invited talks + short oral / poster papers (typical FAIBI 2026 format ~10–20 papers across pathology / radiology / multimodal tracks). Methods center on (a) pretraining recipes for medical image encoders (SSL on H&E, CT, MR, US), (b) downstream task adaptation (segmentation, classification, generation), (c) evaluation protocols including fairness / robustness / OOD generalization, (d) clinical translation pathways.

## Headline benchmarks

TBD — workshop-level synthesis; named-tool papers from the program will get individual tool pages where artifacts are released. Targeted: any oncology-imaging FM update, any pathology FM evaluation paper, any radiology FM with a cancer subgroup analysis.

## How it works

**Core idea.** FAIBI is a curation venue, not a single methodology — but the workshop's structure operationalizes a shared methodological program across pathology, radiology, microscopy, and multimodal foundation models: SSL pretraining at scale, downstream task adaptation with minimal labels, and clinical-translation-aware evaluation (fairness, OOD robustness, regulatory pathway).

**Inputs / outputs.** Inputs (across the program): H&E whole-slide images, CT / MR / US volumes, microscopy stacks, and paired text / molecular labels. Outputs span the full medical-imaging task surface — classification, segmentation, generation, retrieval, captioning, agentic workflows — with a common emphasis on **transfer to oncology-imaging endpoints** under the Jia Wu co-organizer steering.

**Key innovation.** The cancer-center-organized workshop slot is the load-bearing methodological framing: FAIBI 2nd edition explicitly biases toward FM evaluations that include cancer-relevant cohorts and outcomes (lung CT screening cohorts, breast mammography reader studies, pathology survival prediction, radiogenomics) rather than generic medical-imaging benchmarks. The implicit hypothesis tested across the program is that domain-pretrained FMs + cancer-specific adaptation outperform generalist medical FMs on oncology tasks.

**Parameters.** Workshop-level — papers span small (single-modality, sub-10M parameter) adaptations to large (>1B-parameter foundation-model) updates. Typical FAIBI 2026 program likely contains ~10–20 short oral / poster papers across pathology / radiology / multimodal tracks.

**Canonical example.** A representative FAIBI 2nd-edition paper type: take a published pathology FM (UNI, CHIEF) or radiology FM (Med-PaLM-class, BiomedCLIP), apply minimal adaptation (linear probe, LoRA, few-shot prompting) to a cancer-axis downstream task (lung-CT nodule malignancy, breast-MRI lesion classification, pathology-based survival prediction), and report performance with fairness / OOD / radiologist-reader-study comparison. Named-tool releases from the workshop graduate to individual tool pages.

## Where it fits in the corpus

- **AACR 2026:** indirect via Jia Wu / MD Anderson radiomics line; pathology FM updates cross-link to [CHIEF](../../aacr-2026/topics/bioinfo-tools/tools/chief.md), [UNI](../../aacr-2026/topics/bioinfo-tools/tools/uni.md), [Prov-GigaPath](../../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md)
- **MICCAI 2026:** direct sibling — COMPAY (Sep 27–Oct 1) is the methodologically-nearest workshop; same author pool, fuller papers
- **CVPR 2026:** FMV / MMFM-BIOMED workshops are the upstream architecture-feeder venues
- **RSNA 2026:** if any radiology FM presented here reaches deployment, RSNA tool index gets the clinical-counterpart entry

## Notes

FAIBI 2nd edition's MD Anderson co-organizer slot is the direct cancer-center authorship signal that elevates this workshop above the other ISBI 2026 satellite events for the cancer-relevance filter. Watch for the workshop's accepted-paper list (typically posted ~1 week post-meeting) and pick named-tool papers for individual tool pages.
