# Talks — AACR Brain Cancer 2026

The primary artifact of this vault: **one Markdown file per talk**. AACR Brain Cancer 2026 is a hybrid meeting — some talks are cellular-therapy clinical cohorts, some are targeted-therapy biology / clinical, some are neuroscience-of-glioma mechanism, some are single-cell / spatial methods, some are pediatric-CNS-tumor readouts. The per-talk schema accommodates all of these with one `Anchor type` field.

> **Status:** Template + master index. Per-talk pages will be populated retrospectively from the AACR Brain 26 program page, the *Cancer Research* abstract supplement, AACR session video / slide releases, and trade-press recaps. Stubs flagged `*expected per program page*` are reconstructed from the public program; the AACR-posted speaker list and abstract numbers are the source of truth once the supplement DOIs land.

## Per-talk template

Each talk file (e.g., `monje-keynote.md`, `il13ra2-egfr-bivalent-car-t.md`, `vorasidenib-combinations.md`, `gd2-car-t-dmg-stanford.md`) follows this schema. Copy and fill:

```markdown
# <Talk title — short>

> **Session:** <session name, date, time ET, room> · **Track:** <track / theme> · **Abstract:** <*Cancer Research* abstract #, if assigned>

## At a glance

- **Speaker:** <name, degrees>
- **Affiliation:** <institution, department, lab>
- **Day / session / track:** <Tue Mar 24 / Cellular Therapy for GBM / cell-therapy>
- **Talk title:** <full title as in program>
- **Anchor type:** <cell therapy / trial | targeted therapy / trial | cohort / readout | mechanism / biology talk | tool / pipeline | award lecture | keynote>
- **Anchor:** <trial acronym + NCT | drug + indication | manuscript citation + DOI | tool name + repo / package URL>
- **Co-authors / consortium:** <if applicable — e.g., COG, Children's Brain Tumor Network (CBTN), GLASS Consortium, NCI-CONNECT>
- **Preprint / paper:** <bioRxiv / medRxiv / Nature / NEJM / Cancer Cell / Cancer Discovery DOI, if accompanying>

## Key result

<One paragraph. Numbers + cohort size + response / PFS / OS / molecular endpoints if known.
For mechanism talks: the headline biological finding. If pre-publication, mark
`*expected per <lab page / prior abstract / press release>*` or `*per AACR Brain 26 program*`.>

## Mechanism / approach

<2–4 sentences. What target, what construct (for cell therapy: scFv / hinge / costim / armouring),
what delivery route (IV / intratumoral / intraventricular / ICV / focused-ultrasound BBB-open),
what comparator, what biomarker stratification. For mechanism talks: model system, key
experimental innovation. For tool / methods talks: what it consumes / produces and the
key computational idea.>

## Why it matters for the corpus

<1–2 sentences. The cross-meeting relevance specifically — does it inform the AACR Annual
neuro-onc slot four weeks later, an ASCO trial readout, a SITC cellular-therapy talk,
a SABCS brain-metastases readout, or a SNO 2026 plenary?>

## Discussant / chair takeaway

<Named session chair + framing once known. AACR special conferences use session-level chairs
rather than per-abstract discussants — capture chair framing.>

## Cross-links

- **AACR Brain 26 prior years:** <e.g., Brain 23 / Brain 21 antecedent talks if part of a series>
- **AACR 2026 Annual (San Diego, Apr 17–22):** <related session / poster, if applicable>
- **SITC 2026 (Nov 4–8):** <CAR-T-in-CNS / IO neuro-onc tie-in>
- **ASCO 2026 (May 29 – Jun 2):** <vorasidenib follow-up / brain-mets readout cross-link>
- **SABCS 2026 (Dec 8–11):** <HER2 brain mets / leptomeningeal disease readout>
- **JPM 2026:** <sponsor presentation / pipeline framing>
- **Other Brain 26 talks:** <session-mates, same-platform, same-target>

## Sources

- *Cancer Research* abstract: <DOI or "pending supplement publication">
- Preprint / paper: <bioRxiv / medRxiv / journal DOI>
- Sponsor / institutional press: <URL>
- Trade-press recap: <OncLive / Targeted Oncology / Neurology Live / CancerNetwork URL>
- ClinicalTrials.gov: <NCT URL>
- Lab page: <URL>
- Recording (if released): <AACR On Demand / YouTube URL>
```

## Master talk index

The shortlist below is for **stub creation** — entries are reconstructed from the AACR Brain 26 program page and chair public statements. Speaker assignments and titles will be reconciled with the official program / *Cancer Research* supplement when DOIs land. Italicized speakers / titles are `*expected per program / chair statements*`.

| Talk | Speaker (expected) | Affiliation | Day | Session / track | Anchor type | Anchor (expected) | Why it matters |
|---|---|---|---|---|---|---|---|
| **Keynote: glioma cell states and lineage** | Mario L. Suva | Harvard / Broad / MGH | Plenary (Mon Mar 23) | Keynote | keynote | *AC-/MES-/OPC-/NPC-like state framework + new perturbation / lineage data* | Defines the cell-state framework underpinning much of the rest of the program |
| **Keynote: The role of injury programs in gliomagenesis** | Simona Parrinello | UCL Cancer Institute | Plenary (Tue Mar 24) | Keynote | keynote | *injury-response / wound-healing programs as gliomagenesis substrate* | Reframes glioma origin in injury-response terms — recurring 2024–26 theme |
| **Neuroscience of glioma — neural-circuit integration and activity-dependent growth** | Michelle Monje | Stanford | Plenary or session-leading | Neuroscience of gliomas | mechanism / biology talk | *neuron-glioma synaptic integration, AMPAR-driven proliferation; latest model* | Anchors the neuroscience-of-cancer thread that distinguishes Brain 26 from other meetings |
| **Cellular therapy for GBM — chair framing** | Stephen J. Bagley | UPenn | Session chair (Mon/Tue) | Cellular therapy for GBM | session chair | *survey of UPenn IL-13Rα2 + EGFR bivalent CAR-T cohort* | UPenn ICV bivalent CAR-T cohort is the most-watched single CAR-T program in GBM |
| **Bicistronic CAR-T targeting EGFR and IL-13Rα2 in recurrent GBM (Ph1 update)** | *Bagley / O'Rourke / June lab* | UPenn | Mon Mar 23 | Cellular therapy for GBM | cell therapy / trial | *ICV bivalent CAR-T Ph1; expanded cohort per Nature Med 2024 + 2025 PMC update* | Lead clinical signal for ICV bivalent CAR-T in adult GBM |
| **Chlorotoxin CAR-T for recurrent high-grade glioma (Ph1)** | *Brown / Badie lab* | City of Hope | Tue Mar 24 | Cellular therapy for GBM | cell therapy / trial | *chlorotoxin-targeted CAR-T; locoregional + intraventricular delivery* | Broad-targeting (MMP-2-dependent) chlorotoxin-CAR; alternative to single-antigen approaches |
| **IL-13Rα2 CAR-T in recurrent HGG — locoregional delivery long-term** | *Brown / Forman lab* | City of Hope | Tue Mar 24 | Cellular therapy for GBM | cell therapy / trial | *IL-13Rα2 single-target CAR-T; updated cohort per Nature Med 2024* | Lineage benchmark for IL-13Rα2 program; cross-link to bivalent / multispecific designs |
| **Interplay between infused and endogenous immune systems in GBM CAR-T** | *Singh / June / Maus-aligned* | UPenn / MGH | Mon/Tue | Cellular therapy for GBM | mechanism / biology talk | *endogenous T-cell rescue / "epitope spreading" in CNS CAR-T responders* | Frames next-generation CAR-T engineering decisions (armouring, cytokine support) |
| **Cell-state-directed CAR-T cell therapies for glioma** | *Suva / Tirosh / Bernstein-aligned* | Broad / MGH | Mon/Tue | Cellular therapy for GBM | mechanism / biology talk | *targeting cell-state-specific surface antigens (e.g., MES-like, OPC-like)* | Integrates single-cell glioma framework with cell-therapy target selection |
| **GD2 CAR-T for DIPG and diffuse midline glioma — Ph1 update** | *Monje / Mackall lab* | Stanford | Tue Mar 24 | Pediatric / DIPG | cell therapy / trial | *GD2-CAR-T (autologous) IV + ICV in H3K27M-mutant DMG; updated cohort* | Practice-defining for pediatric DMG; the strongest CAR-T-in-CNS efficacy signal to date |
| **B7-H3 CAR-T for pediatric CNS tumors — Ph1** | *Vitanza / Park-aligned* | Seattle Children's | Tue Mar 24 | Pediatric / cell therapy | cell therapy / trial | *B7-H3-targeted CAR-T; locoregional CSF delivery; medulloblastoma + ependymoma + ATRT* | Alternative pediatric CAR-T target with broad CNS-tumor expression |
| **EGFRvIII-targeted approaches for GBM in 2026 — what's left** | *O'Rourke / June* or alternate | UPenn / MGH | Mon Mar 23 | Cellular therapy for GBM | mechanism / biology talk | *EGFRvIII single-target lessons + role in bivalent / multispecific constructs* | Frames the field's reckoning with single-target CAR antigen-escape |
| **Vorasidenib in IDH-mutant glioma — post-INDIGO biology and combinations** | *Mellinghoff / Wen / Cloughesy-aligned* | MSK / DFCI / UCLA | Mon Mar 23 | IDH-mutant glioma | targeted therapy / trial | *vorasidenib + TTF / RT / immune combinations; high-grade IDH-mut signal* | First targeted-therapy approval in grade 2 IDH-mut glioma; combinations define the next chapter |
| **Tumor Treating Fields + vorasidenib in IDH-mutant glioma** | *Wang / Novocure-academic collab* | Terasaki Institute / partner sites | Mon Mar 23 | IDH-mutant glioma | targeted therapy / trial | *TTF + vorasidenib resistance-overcoming mechanism; preclinical + Ph1 design* | AACR-Novocure CDA-funded program; cross-link to ongoing-trial poster |
| **IDH-mut neoantigen / peptide vaccine update** | *Platten / Sahm / Schumacher-aligned* | DKFZ / Heidelberg | Mon Mar 23 | IDH-mutant glioma | targeted therapy / trial | *IDH1R132H peptide vaccine; updated cohort per Nature 2021 + follow-up* | Bridges IDH-mut targeted-therapy thread to neuro-IO |
| **2-HG biology and downstream epigenetic targeting in IDH-mut glioma** | *Mellinghoff / Su lab* | MSK | Mon Mar 23 | IDH-mutant glioma | mechanism / biology talk | *D-2-HG signalling, hypermethylation, vulnerability mapping* | Defines combination-partner space for vorasidenib |
| **Medulloblastoma molecular subgroup-specific therapy (Group 3 / 4)** | *Pomeroy / Roussel / Northcott-aligned* | DFCI / St. Jude | Wed Mar 25 | Pediatric / medulloblastoma | mechanism / biology talk | *MYC-amplified Group 3 + heterogeneous Group 4 biology; subgroup-targeted approaches* | Subgroup-tailored therapy is the medulloblastoma practice-shift question |
| **SHH-medulloblastoma — beyond SMO inhibitors** | *Curran / Wechsler-Reya / Robinson* | St. Jude | Wed Mar 25 | Pediatric / medulloblastoma | mechanism / biology talk | *SHH subtype biology, resistance to SMO-i, novel SHH-pathway targeting* | Post-vismodegib / sonidegib era; addresses pediatric SHH-medulloblastoma niche |
| **GD2 expression and CAR-T targeting in medulloblastoma** | *Mackall / Lim / Vitanza-aligned* | Stanford / Seattle Children's | Wed Mar 25 | Pediatric / cell therapy | cell therapy / trial | *GD2 + GPC2 + B7-H3 multi-antigen medulloblastoma CAR-T pipeline* | Pediatric medulloblastoma CAR-T is the next pediatric-CAR inflection after DMG |
| **DAY101 / tovorafenib in pediatric low-grade glioma (post-FIREFLY)** | *Kilburn / Wright / Day One* | DFCI / Day One Biopharmaceuticals | Wed Mar 25 | Pediatric / targeted | targeted therapy / trial | *type-II RAF inhibitor in BRAF-fusion / V600 pediatric LGG; post-FDA-approval data* | Practice-defining for BRAF-altered pediatric LGG |
| **ONC201 / dordaviprone in H3K27M-mutant glioma** | *Arrillaga-Romany / Chi / Chimerix* | MGH / Chimerix | Tue Mar 24 | Pediatric / DIPG / DMG | targeted therapy / trial | *ClpP / DRD2 modulator; H3K27M-mutant DMG efficacy + biomarker* | First targeted-therapy signal in H3K27M DMG; FDA filing-window |
| **Brain metastases — CNS-active ADC penetration (HER2)** | *Lin / Anders / Bardia-aligned* | DFCI / Duke / UCLA | Tue Mar 24 | Brain metastases | cohort / readout | *T-DXd CNS activity in DESTINY-Breast12; tucatinib brain-mets combinations* | Reframes ADCs as CNS-active drugs; bridges to SABCS 2026 |
| **HER2CLIMB and beyond — tucatinib + ADC sequencing in brain mets** | *Lin / Murthy / Hurvitz* | DFCI / MD Anderson / UW | Tue Mar 24 | Brain metastases | cohort / readout | *tucatinib + T-DXd in brain mets; sequencing question* | HER2 brain-mets practice question |
| **CSF ctDNA / cfDNA for response monitoring in CNS tumors** | *Miller / Brastianos / Brennan-aligned* | MGH / MSK | Wed Mar 25 | Diagnostics / biomarkers | tool / pipeline | *CSF liquid biopsy assay; methylation classifier integration* | Liquid biopsy in CNS tumors is the response-assessment unmet need |
| **DKFZ methylation classifier (MNP v13) and pediatric brain-tumor diagnosis** | *Sahm / Pfister / Capper-aligned* | DKFZ / Heidelberg | Wed Mar 25 | Diagnostics / biomarkers | tool / pipeline | *MNP v13 release; expanded subgroup coverage; clinical validation cohort* | Defines pediatric brain-tumor molecular classification standard worldwide |
| **Microglia and tumor-associated microglia / macrophages in glioma** | *Bowman / Joyce / Quail-aligned* | Yale / Lausanne / McGill | Tue Mar 24 | Neuro-immune / TME | mechanism / biology talk | *TAM single-cell + spatial framework; reprogramming as therapeutic target* | The other half of neuro-IO beyond CAR-T |
| **Dopamine signalling and glioma progression** | *Venkatesh / Monje-aligned* | Stanford | Tue Mar 24 | Neuroscience of gliomas | mechanism / biology talk | *dopaminergic input to glioma; behavioral and pharmacological perturbation* | Extension of the neural-circuit-glioma framework |
| **Blood-brain-barrier-aware drug discovery — design principles** | *Sanai / Lim-aligned* | Ivy Brain Tumor Center / academic | Mon Mar 23 | BBB delivery | mechanism / biology talk | *Phase 0 / window-of-opportunity trials; BBB / BTB PK / PD framework* | Reframes CNS-drug-discovery default assumptions |
| **Focused-ultrasound BBB opening for CNS drug delivery** | *Mainprize / Hynynen-aligned* | Sunnybrook / partner sites | Mon Mar 23 | BBB delivery | tool / pipeline | *MR-guided FUS BBB opening for chemotherapy / antibody delivery* | Emerging modality, late-Ph1 / early-Ph2 |
| **Convection-enhanced delivery (CED) for pediatric DIPG / DMG** | *Souweidane / Bander-aligned* | Weill Cornell / partner | Tue Mar 24 | Pediatric / BBB delivery | tool / pipeline | *CED + radiolabeled antibody / small-molecule pediatric DIPG / DMG trial cohort* | Pediatric DMG-specific delivery modality with extant Ph1 / Ph2 data |
| **Spatial transcriptomics in glioma — GLASS / lineage atlas** | *Verhaak / Suva / Bernstein-aligned* | Yale / Broad | Wed Mar 25 | Single-cell / spatial | tool / pipeline + biology | *GLASS Consortium spatial atlas; Visium HD / Xenium application* | Integrates single-cell framework with spatial context |
| **3D-genome organization and chromatin in glioma** | *Bernstein / Marra-aligned* | Broad | Wed Mar 25 | Tumor heterogeneity / spatial | mechanism / biology talk | *3D-genomics-defined regulatory programs in GBM cell states* | Connects cell-state framework to cis-regulatory architecture |
| **Single-cell atlas of pediatric brain tumors — CBTN / OpenPBTA** | *Resnick / Storm / CBTN team* | CHOP / CBTN | Wed Mar 25 | Pediatric / single-cell | tool / pipeline + cohort | *OpenPBTA scRNA + bulk pan-pediatric atlas update* | Foundational resource for pediatric-brain-tumor biology |
| **Closing plenary / synthesis** | *Chairs (Bagley / Monje / Suva)* | UPenn / Stanford / Broad | Wed Mar 25 PM | Closing | award lecture / synthesis | *meeting-wide synthesis + next-step agenda* | Captures the chair-articulated takeaways |

**Additional shortlist candidates** to stub once the AACR Brain 26 abstract supplement DOIs land:

- **CAR-T armouring:** TGF-β-resistant CAR-T constructs in GBM; IL-7 / IL-15-armoured constructs; "logic-gated" CARs (e.g., dual-signal SynNotch) for CNS solid tumors.
- **Allogeneic / off-the-shelf cell therapy:** allogeneic NK-cell and γδ-T-cell programs in GBM; allogeneic CAR-T platforms entering CNS.
- **Oncolytic virus + cell therapy combinations:** OV delivering CD19 + EGFRvIII antigens (per Nature Comms 2026 reference); OV priming CAR-T responses.
- **Ependymoma and ATRT:** rare-CNS-tumor-specific sessions (often paired with pediatric track).
- **CNS lymphoma (PCNSL):** typically a small adjunct session; cellular therapy + BBB-aware regimens.
- **Pre-meeting / educational tracks:** statistical-trial-design primers, BBB pharmacology primer, single-cell-for-clinicians.
- **Industry-sponsored research presentations:** typically Servier (vorasidenib), Day One (tovorafenib), Chimerix (ONC201), CARGO / Mustang / 2seventy (cell therapy), Novocure (TTF).

## Cross-cutting themes (for `themes.md`, deferred until per-talk pages are populated)

To synthesize across `talks/` once populated:

1. **CAR-T-in-CNS readout convergence.** ICV bivalent (UPenn EGFR + IL-13Rα2) vs locoregional single-target (City of Hope IL-13Rα2, chlorotoxin) vs IV + ICV GD2 (Stanford DMG) vs B7-H3 (Seattle Children's) — the 2026 question is which design / route / target combination wins where. Cross-link to [SITC 2026](../../sitc-2026/index.md) solid-tumor cell-therapy track.
2. **Vorasidenib combination signal.** Post-INDIGO, the question is whether IDH-mut targeted-therapy works as monotherapy in higher-grade disease (CURE follow-up suggests safe + tolerable) and which combination (TTF, RT, vaccine, immune) shifts the curve. The 2026 readout shapes the 2027–28 Ph2 / Ph3 design space.
3. **GD2-CAR-T pediatric inflection.** The Stanford DMG signal is the most-watched CAR-T signal across all of pediatric solid-tumor oncology. Brain 26 is where the design + biomarker work feeds forward to expanded multi-site Ph2. Bridges to AACR 2026 Annual pediatric track and SITC 2026.
4. **Single-cell glioma cell-state framework consolidation.** Suva / Tirosh / Bernstein-aligned labs continue to refine the AC-/MES-/OPC-/NPC-like framework; the 2026 update integrates spatial transcriptomics, lineage tracing, and clinically-paired specimens. Cross-link to [AACR 2026 single-cell topic](../../aacr-2026/topics/single-cell-spatial-omics/index.md).
5. **Neuro-immune / microglia framing.** TAM-targeting plus neural-circuit-glioma plus neuro-IO is converging into a single conceptual frame. The 2026 update brings spatial-immune and single-cell-microglia work into clinical-correlation territory.
6. **BBB-aware drug discovery.** Phase-0 / window-of-opportunity trials + FUS BBB opening + CED + BBB-penetrant chemistry. The 2026 reframing of "CNS drug discovery starts with the BBB" reaches mainstream-oncology consciousness via ADC brain-mets data (cross-link to [SABCS 2026 brain-mets section](../../sabcs-2026/index.md#brain-metastases)).
7. **Pediatric brain-tumor molecular classification standard.** DKFZ MNP v13 update + CBTN / OpenPBTA atlas — the diagnostic + research substrate for pediatric brain-tumor work in 2026 onward.
8. **Brain metastases as cross-cancer practice question.** HER2 brain-mets (DESTINY-Breast12, HER2CLIMB-05) and lung / melanoma brain-mets activity from CNS-penetrant targeted therapy is reshaping ADC + small-molecule positioning. Cross-meeting bridge across Brain 26 → AACR 2026 → ASCO 2026 → SABCS 2026.
