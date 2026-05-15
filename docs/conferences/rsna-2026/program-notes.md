# RSNA 2026 — Program notes (pre-meeting)

Pre-meeting working file. What's verified, what's anticipated, where to look as the program goes live.

> **Updated:** May 2026 (~7 months pre-meeting). Will be updated again when (a) registration opens late July, (b) the searchable program goes live late summer, (c) RSNAI Monthly press releases drop Sep–Nov, and (d) the AI Showcase exhibitor list is finalized.

## Verified facts

- **Meeting:** 112th RSNA Scientific Assembly and Annual Meeting
- **Dates:** **Sunday Nov 29 – Thursday Dec 3, 2026** (5 days)
- **Venue:** McCormick Place, Chicago, IL
- **Technical Exhibits hours:** Nov 29 – Dec 2, 10:00–17:00 CT daily (closed Dec 3)
- **Theme:** "At the Center of Care" — radiology as the hub of modern medicine, with diverse perspectives and new discoveries advancing the patient's journey
- **Abstract submission:** closed earlier in the spring; acceptance notifications rolling out (RSNA in Brief, Apr 2026)
- **Registration:** opens late July 2026
- **AI Challenge 2026:** **Knee MRI AI Challenge** — RSNA's first musculoskeletal AI challenge; winners announced at the meeting

## AI track structure

The RSNA AI program has three load-bearing components:

### 1. AI Showcase — South Hall A (exhibit floor)

- **Booth block:** South Hall A, ~Booth 4700s (exact starting booth published with exhibitor list)
- **100+ AI vendor exhibitors** in 2025; expected similar or larger in 2026 (2025 hit 111 registered exhibitors and 228 booths total demonstrating AI/ML tools)
- **AI Theater** (separate booth, ~5500-block in 2025) — 30+ companies delivering 20-minute presentations Sun–Wed
- **Format:** vendor-led product demonstrations, FDA-cleared device announcements, deployment case studies
- **Cross-link:** vendor products that wrap a public foundation model get tracked on that model's page in [`tools/`](tools/index.md); vendor-only products that don't reference an open FM get a roll-up paragraph here (not individual pages — too many to be useful)

### 2. "Radiology Reimagined: AI, innovation and interoperability in practice"

- **Format:** live demonstration of standards-based AI integration into the diagnostic radiology workflow
- **Location:** AI Showcase, South Hall A (2025 was Booth 5104; 2026 booth TBD)
- **Cadence:** every half hour, Mon–Wed during the meeting
- **What it is:** the successor to the older "Imaging AI in Practice" (IAIP) demonstration. Uses real-world clinical scenarios + interoperability standards (DICOM, HL7 FHIR, IHE AI profiles) to demonstrate how AI tools plug into the PACS / reporting workflow without bespoke integration
- **Why it matters:** the technical-deployment story for AI. Models that exist at AACR / NeurIPS / arxiv mostly *don't* show up in the live diagnostic workflow. This demo is where the standards story lives

### 3. Deep-learning lecture series + AI scientific sessions

- **Format:** refresher courses (multi-session series across the meeting) + dedicated AI scientific paper sessions across the body-system tracks
- **Recurring topics (anticipated):** AI fundamentals, validation and prospective study design, governance and regulation, fairness and bias auditing, foundation models, multimodal LLMs, federated learning, generative AI in reporting
- **Cross-cutting AI sessions in each body-system track:** breast AI, chest AI / lung screening, neuro AI, MSK AI (boosted in 2026 thanks to the Knee MRI Challenge focus), cardiac AI (CCTA), abdominal AI (opportunistic screening)
- **Hot-topic / controversy sessions:** typically a few AI-themed slots (e.g., "Generative AI in radiology — practice-changing or hype?") — exact slate published with the program

## Expected foundation-model updates at RSNA 2026

Conservative list — pathology FMs cross-linked to AACR; radiology-native FMs flagged as candidates pending program confirmation.

### Pathology foundation models (AACR vault cross-links)

These are unlikely to have major *new* checkpoint releases at RSNA (their home venue is AACR / Nature / arxiv), but they may surface in **radiology-pathology cross-modality** talks or refresher-course material on multimodal FMs. The AACR vault holds the canonical dossier.

| Model | AACR dossier | Anticipated RSNA 2026 surface area |
|---|---|---|
| **CHIEF** | [chief.md](../aacr-2026/topics/bioinfo-tools/tools/chief.md) | Mahmood Lab — possible cross-modality talk if a radiology-pathology bridge from the same lab surfaces. AACR corpus shows zero genuine mentions (all hits were false positives on "Chief AI / Scientific Officer"); RSNA 2026 may be the better venue if any |
| **Prov-GigaPath** | [prov-gigapath.md](../aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md) | Microsoft + Providence — Microsoft Research has multiple radiology FMs at RSNA each year (RadDino, MAIRA, LLaVA-Rad); expect joint pathology-radiology framing in informatics sessions |
| **UNI / UNI2** | [uni.md](../aacr-2026/topics/bioinfo-tools/tools/uni.md) | Mahmood Lab — UNI2 (Jan 2025 release) is likely benchmark backbone in 2026 multimodal-FM comparisons; watch for embedding-export-based downstream tasks in pathology-radiology integration talks |

### Radiology-native foundation models (RSNA-primary)

These are the models RSNA is the natural home for. The 2026 cycle will reveal which of them have new checkpoints, prospective deployment data, or named-trial readouts.

- **RadFM** (Shanghai Jiao Tong + collaborators) — generalist radiology FM trained on 2D + 3D imaging + reports. Refresher-course / multimodal-FM material likely.
- **Med-PaLM-M** (Google DeepMind) — multimodal Gemini-era successor expected. Generative-AI-in-radiology slot.
- **Merlin** (Stanford) — abdominal CT + EHR. Strong opportunistic-screening / body-composition story; the May 2026 RSNA press release on "AI model analyses body composition to predict health risks" is in this family.
- **RadDino** (Microsoft Research) — DINOv2-based chest X-ray FM. Chest-AI sessions; likely benchmark backbone.
- **MAIRA-2 / MAIRA-3** (Microsoft Research) — chest X-ray report-generation FM. Generative-AI / governance sessions; MAIRA family has had RSNA presence in 2024-2025.
- **CheXagent** (Stanford AIMI) — chest X-ray multimodal LLM. Chest-AI / informatics.
- **LLaVA-Med / LLaVA-Rad** (Microsoft + Stanford) — vision-language radiology. Generative-AI sessions; benchmark backbone.

### Segmentation FMs

- **MedSAM** (Wang Lab, UToronto) — universal medical segmentation. Refresher-course staple.
- **SegVol** (BAAI / Tsinghua) — 3D volumetric segmentation.
- **Universal-MedSeg variants** — derivative work; watch for prompt-tuned / federated variants.

### Methods / governance topics likely to recur

- **AI bias / fairness auditing** — recurring refresher-course track
- **FDA-cleared AI device list updates** — separate session each year; tracked here as an annual snapshot
- **Reimbursement (NTAP, CPT codes for AI) updates** — ACR / RSNA joint session typical
- **ACR DSI standards** + the **IAIP / "Radiology Reimagined" demo** — interoperability story
- **Synthetic data + privacy-preserving evaluation** — recurring; expect more in 2026 given the multi-institution prospective-trial pressure

## Anticipated imaging-trial readouts

Trials likely to surface at RSNA 2026 (or with companion publications in Radiology / Radiology: AI timed to the meeting). All flagged *expected* until confirmed by program release.

### Breast screening AI

- **Post-AI-STREAM analyses** — AI-STREAM (the Korean prospective AI-CAD trial) published headline results in Radiology: AI in early 2026; follow-on subgroup / cost-effectiveness / interval-cancer analyses are likely at RSNA 2026
- **BreastScreen Norway prospective deployment** — ongoing real-world readouts; multi-year cohort updates typical
- **MIRAI-MRI (NCT05968157)** — AI-triggered supplemental screening MRI; first interim readout possible at RSNA 2026 depending on accrual
- **Hologic / Lunit / ScreenPoint / DeepHealth / Volpara** — vendor-sponsored prospective audits routinely surface at RSNA
- **NCCN guideline tie-in** — NCCN updated breast cancer guidelines to include AI-based risk assessment in 2025; RSNA 2026 will likely have the implementation-data session

### Lung-cancer screening AI

- **NLST / NELSON-replay AI readouts** — multiple groups have AI-on-screening-CT retrospective cohorts; expect prospective USPSTF-aligned cohort updates
- **Volume-doubling-time AI** for lung-nodule follow-up
- **Aidoc / Riverain ClearRead / RadAI / RadLogics** — vendor-led real-world audits

### Prostate MRI

- **PI-RADS AI requirements (v1.0, Radiology 2024)** — implementation-and-validation studies should mature into prospective readouts by RSNA 2026
- **bpMRI vs mpMRI AI head-to-heads** — recurring topic; whatever lands in Radiology in 2026 will surface here
- **TransPerC / PROMIS-style AI-triage cohorts** — biopsy-deferral signals

### Opportunistic / body-composition AI

- **Whole-body MRI body-composition AI** — the May 2026 RSNA press release flagged this as a 2026 highlight ("AI model analyses body composition to predict health risks"); abstract / talk likely at RSNA 2026
- **Abdominal-CT opportunistic screening** (Merlin / Stanford) — sarcopenia, hepatic steatosis, osteoporosis, atherosclerosis from routine CT
- **Cardiovascular risk from CT** — CAC scoring AI, perivascular fat AI

### Stroke / neuro AI

- **LVO detection AI** (Viz.ai, Aidoc, RapidAI, etc.) — deployment-outcome studies, door-to-needle / door-to-puncture impact
- **Glioma / brain-tumor segmentation** — BraTS-style FM segmentation deployed prospectively

## Where to look (source priorities)

1. **RSNA Daily Bulletin** — [dailybulletin.rsna.org](https://dailybulletin.rsna.org/) — first-pass editorial, per-day. Load-bearing during the meeting.
2. **Radiology / Radiology: AI journal** — [pubs.rsna.org](https://pubs.rsna.org/) — companion-publication DOIs for headline talks. Embargoed timed to the meeting.
3. **RSNAI Monthly press releases** — [rsna.org/media/press](https://www.rsna.org/media/press) — Sep / Oct / Nov 2026 previews. Pre-meeting source.
4. **RSNA Meeting Program** — [meeting.rsna.org](https://meeting.rsna.org/) — searchable, goes live late summer.
5. **AI Showcase exhibitor list** — [rsna.org/ai-showcase](https://www.rsna.org/annual-meeting/exhibitors-and-sponsors/exhibit-spaces/ai-showcase) — pre-meeting (Oct-Nov).
6. **Aunt Minnie / RadAI / Health Imaging** — trade-press editorial; useful for vendor stand-ups.
7. **STAT News / HealthTechHotspot** — analyst framing post-meeting.
8. **Company press releases** — wire services; cross-checked against peer-reviewed source.

## Cross-vault wiring checklist

When the tool pages get populated, each one needs:

- [ ] Back-link to the AACR dossier if the model is pathology-FM (CHIEF / GigaPath / UNI) — already wired in [`tools/index.md`](tools/index.md)
- [ ] Forward-link from the AACR dossier to the RSNA addendum if RSNA surfaces a radiology-extension or cross-modality variant (post-meeting update)
- [ ] JPM 2026 cross-link if the sponsor company presented at JPM (Microsoft, Google, Hologic, GE HealthCare, Siemens Healthineers, Philips, etc.) — [JPM 2026 vault](../jpm-2026/index.md)
- [ ] ASCO 2026 cross-link for imaging-driven oncology trials that read out at ASCO before RSNA (e.g., NCCN breast-AI-risk implementation studies, lung-screening AI cohorts tied to USPSTF cohorts) — [ASCO 2026 vault](../asco-2026/index.md)
- [ ] NeurIPS 2026 cross-link for methods papers that anchored the FM at NeurIPS December 2026 (concurrent with RSNA — same week) — [NeurIPS 2026 vault](../neurips-2026/index.md)

## Top 5 things to watch (going in)

1. **Knee MRI AI Challenge results** — the first MSK challenge in the RSNA Challenge series. Winning architectures + dataset details set the MSK-AI agenda for the next 1–2 years.
2. **Radiology-pathology multimodal FMs** — whether any group bridges CHIEF / UNI / GigaPath into a joint radiology-pathology model with a real cohort. The AACR 2026 vault showed strong UNI / GigaPath presence on the pathology side; RSNA is the natural place for the radiology extension to surface.
3. **MIRAI-MRI interim readout** — AI-triggered supplemental MRI is the cleanest "AI changes screening behaviour, not just sensitivity" trial in the field. Any interim signal would be a load-bearing RSNA 2026 story.
4. **Whole-body MRI body-composition AI** — RSNA pre-flagged this in the May 2026 press release; expect a named talk + Radiology / Radiology: AI companion publication.
5. **Generative-AI report generation** — MAIRA / LLaVA-Rad / CheXagent class. Whether any group lands a prospective deployment readout (not just retrospective AUROC) will set the 2027 agenda for generative AI in radiology.

## Sources

- [RSNA Annual Meeting home](https://www.rsna.org/annual-meeting)
- [RSNA AI Showcase](https://www.rsna.org/annual-meeting/exhibitors-and-sponsors/exhibit-spaces/ai-showcase)
- [Radiology Reimagined: AI, innovation and interoperability in practice](https://www.rsna.org/artificial-intelligence/radiology-reimagined-ai)
- [AI at the Annual Meeting](https://www.rsna.org/artificial-intelligence/at-the-meeting)
- [RSNA in Brief — April 2026 (abstract-submission status; AI Challenge announcement)](https://www.rsna.org/media/press/2026/2652)
- [AI Model Analyses Body Composition to Predict Health Risks (RSNA press, May 2026)](https://www.rsna.org/news/2026/may/ai-analyzes-whole-body-mri)
- [Generative AI and Foundation Models in Radiology (Radiology, 2024)](https://pubs.rsna.org/doi/10.1148/radiol.242961)
- [Foundation Models in Radiology: What, How, Why, and Why Not (Radiology, 2024)](https://pubs.rsna.org/doi/10.1148/radiol.240597)
- [PI-RADS Steering Committee AI requirements (Radiology, 2024)](https://pubs.rsna.org/doi/10.1148/radiol.240140)
- [Breast Cancers Detected and Missed by AI-CAD: AI-STREAM (Radiology: AI, 2026)](https://pubs.rsna.org/doi/10.1148/ryai.250281)
- [RSNAI Monthly press archive](https://www.rsna.org/media/press)
- [RSNA Daily Bulletin (prior year)](https://dailybulletin.rsna.org/)
