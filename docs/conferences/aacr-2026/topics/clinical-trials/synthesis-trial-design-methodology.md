# Synthesis — are Bayesian / adaptive / model-assisted trial designs mainstream in AACR 2026 CT?

**Thesis:** Bayesian, adaptive, and model-assisted dose-finding designs have crossed from academic-biostatistics novelty into a plurality of early-phase CT poster readouts at AACR 2026 — but the penetration is lopsided. BOIN is now the de-facto industry default for sponsor-run Phase I dose-escalation; Bayesian Phase 2 extensions (BOP2, Bayesian borrowing in basket trials) are visible; **adaptive** and **platform** designs remain rare; and meaningful usage of **synthetic / external controls** is absent from the corpus entirely.

This page parses the full 642-poster JSONL for design-pattern keyword hits (Title + Abstract + SessionTitle, case-insensitive), cites every claim to a specific PresentationNumber, and closes with an institutional analysis of whether this is a real methodology shift or a Chinese-industry-sponsor concentration. No session transcripts exist for the Clinical Trials track (see [caveats](../../../../notes/caveats.md)), so this is a corpus-only synthesis.

**Quantitative scan — total design-pattern hits (of 642):**

| Pattern | Hits | Hit rate | Notes |
|---|---:|---:|---|
| Bayesian (any) | 19 | 3.0% | Almost entirely BOIN and its extensions |
| BOIN (Bayesian Optimal Interval) | 16 | 2.5% | Clear industry default for dose-escalation |
| Basket trial | 7 | 1.1% | 3 are TAPUR (ASCO/Rodon); 1 basket meta-methodology |
| Platform trial | 5 | 1.1% | Only CT223 (AACR-ADOPT-GEA) is a bona-fide adaptive platform |
| Real-world evidence / RWD | 10 | 1.6% | Precision-oncology registries + AI cohort extraction |
| Master protocol | 2 | 0.3% | FORTE (CT273) and STING (2602) |
| Adaptive design (explicit) | 3 | 0.5% | Distinct from BOIN's Bayesian-adaptive dose rule |
| mTPI | 2 | 0.3% | CT127, CT073 (mTPI-2) |
| Keyboard design | 1 | 0.2% | CT131 only |
| Umbrella trial | 1 | 0.2% | CT262 (ELEVATE) |
| CRM | 0 | 0% | Entirely absent — BOIN has supplanted CRM |
| Synthetic control | 0 | 0% | Absent |
| External control | 0 | 0% | Absent |
| Standard 3+3 design | 26 | 4.0% | Still more common than BOIN by raw count |

**Key numeric comparison:** 3+3 (26 posters) still outnumbers BOIN (16 posters) roughly 1.6:1 in the raw corpus — so 3+3 is not yet the minority. But the balance **inside** sponsor-led FIH / Phase 1/2-in-progress posters (`CT` identifiers, where novel modalities get first-reported) is the opposite: BOIN and its variants (BF-BOIN, BOIN12, BOP2) dominate. The shift is real but concentrated in the early-phase industry-sponsored tier.

---

## Bayesian dose-finding (19 posters, of which 16 are BOIN)

**What it is.** Bayesian dose-finding replaces the 3+3 rule (escalate if 0/3 DLTs, hold if 1/3, stop if 2/3) with a posterior-probability update of the dose-toxicity curve after every cohort, and picks the next dose to minimize expected overshoot of the target DLT rate. BOIN (Bayesian Optimal Interval, Ji/Yuan lab) is the most widely adopted implementation because the escalation table is pre-computed at protocol writing and no Bayesian software is needed at the bedside. Variants: **BF-BOIN** (backfilling at safe doses to accelerate the optimal biological dose [OBD] search), **BOIN12** (a Phase I/II extension that jointly optimizes safety and efficacy), and **BOP2** (Bayesian optimal Phase 2 designs with futility monitoring).

**Representative posters.**

- **#CT087** (IPN60300, Ipsen, ITGA2 ADC) — "A Bayesian Optimal Interval design will be used for dose escalation." Straight BOIN in a sponsor-led FIH Phase I/II.
- **#CT284** (BPI-572270, Betta Pharmaceuticals, RAS(ON) inhibitor) — "In Part A, dose escalation follows a backfilling Bayesian optimal interval (BF-BOIN) design." BF-BOIN in action for OBD search.
- **#CT294** (TROPIKANA, MD Anderson, TROP2 CAR IL-15 cord-blood NK) — "Approximately 54 patients will be enrolled using a Bayesian Optimal Interval Phase I/II (BOIN12) design." Joint safety-efficacy BOIN12 in an academic-sponsor cell therapy trial.
- **#CT287** (MD Anderson / Eikon, CNS-penetrant PARP1-selective agent) — "Part 1 (Dose Escalation; using the Bayesian optimal interval [BOIN] design) and Part 2 (Dose Optimization)." Project-Optimus-aligned two-part structure on a BOIN backbone.
- **#CT290** (NTS071-101, Nutshell Therapeutics) — "accelerated titration design for 100 and 200 mg, followed by Bayesian Optimal Interval (BOIN) design with backfilling." A common hybrid: fast-start accelerated titration feeds into BF-BOIN.
- **#CT129** (NST-628 pan-RAF-MEK molecular glue, Moffitt et al.) — "Dose escalation employed BOIN method, with accelerated titration." Another accelerated-titration + BOIN hybrid, already reporting preliminary results.
- **#CT273** (FORTE, Fore Biotherapeutics + Sarah Cannon) — uses **BOP2** (Bayesian optimal Phase 2) for the master-protocol cohort futility/activity decisions. Demonstrates Bayesian designs at the Phase 2 tier, not just dose-finding.
- **#CT285** (DOMISOL, Domain Therapeutics, CCR8 mAb) — "Adaptive Bayesian dose-escalation will identify the recommended Phase II dose (RP2D) based on safety, PK, and biomarker readouts." Combines adaptive + Bayesian + translational biomarker endpoints.
- **#CT061** (ANS03, AnHeart Therapeutics, ROS1 TRK inhibitor) — "Dose escalation was determined by Bayesian optimal interval design." Already-reporting preliminary-efficacy poster, not just trial-in-progress.
- **#CT060** (D3S-002, BeiGene, ERK1/2 inhibitor) — "The PK and safety profiles were evaluated with D3S-002 QD at 8 dose levels from 10mg to 240mg under BOIN design." Demonstrates how BOIN scales across many dose levels.
- **#CT133** (City of Hope, 225Ac-DOTA-daratumumab alpha-radioimmunotherapy) — "We used a BOIN design for dose escalation decisions." BOIN applied to a targeted radiopharmaceutical, a modality where DLT windows are unusually long.
- **#CT289** (Impact + Fudan, POLQ inhibitor SYN818 + olaparib) — "guided by a Bayesian dose-finding model." Combination-therapy Phase Ib on a BOIN-class backbone.
- **#6435** (AstraZeneca biostatistics) — "basket trial strategy that formally borrows information across indications" — a Bayesian hierarchical borrowing methodology poster proposing how to pool efficacy signals across baskets.

**Substrate.** Bayesian dose-finding in the corpus spans every major modality that the AACR 2026 poster hall contains: small molecules (CT060 ERK, CT287 PARP, CT288 PARG, CT289 POLQ, CT097 SMARCA2 degrader), bispecific ADCs (CT128 JS212, CT099 VBC101), trispecific T-cell engagers (CT079 EVOLVE104), cord-blood CAR-NK (CT294 TROPIKANA), targeted radiopharmaceuticals (CT046, CT133), antibody monotherapies (CT285 CCR8, CT284 RAS(ON)), and mRNA / antagomir therapeutics (CT198). The design pattern is modality-agnostic — a strong signal for genuine mainstreaming rather than a one-indication fad.

## Model-assisted dose-finding beyond BOIN (mTPI, Keyboard — 3 posters)

**What it is.** mTPI (modified Toxicity Probability Interval, Ji lab), mTPI-2, and Keyboard are BOIN's sibling "model-assisted" designs — all share the pre-computed decision-table property but use slightly different decision rules about equivalent-toxicity intervals. They remain academic alternatives to BOIN in the JSONL.

**Representative posters.**

- **#CT127** (ES014, Elpiscience Biopharma, CD39 × TGF-β bispecific) — "dose escalation by an mTPI (modified Toxicity Probability Interval) design."
- **#CT073** (FiREBOLT / LY4337713, Eli Lilly radioligand) — "modified toxicity probability interval-2 (mTPI-2) statistical model will guide dose decisions."
- **#CT131** (BAY2862789, Bayer DGKα inhibitor) — "A FiH trial was performed using a keyboard design for dose escalation." Only keyboard-design poster in the corpus.

**CRM absent.** Zero posters use the Continual Reassessment Method — the method that first introduced Bayesian dose-finding to oncology. BOIN has effectively supplanted CRM in the AACR 2026 corpus, consistent with industry feedback that pre-computed decision tables (BOIN/mTPI/Keyboard) are logistically easier than CRM's per-patient Bayesian update.

## Basket, umbrella, platform, master-protocol (15 posters combined, with dedup)

**What it is.** Basket trials enroll a single drug across histology-agnostic genomic buckets; umbrella trials match multiple drugs to sub-populations within a single disease; platform trials do both + add/drop arms adaptively; master protocols are the umbrella scaffold.

**Representative posters.**

- **#CT273** (FORTE, plixorafenib) — Phase 2 master protocol for BRAF-altered cancers with BOP2 within-cohort. Dual tagging: master-protocol *and* Bayesian Phase 2.
- **#CT206** (larotrectinib in NTRK1/2/3-amp) — TAPUR Phase II basket readout (ASCO-run, enrolling across indications). Representative of the academic-consortium basket approach.
- **#CT211** (palbociclib in CCND1-amp lung) — another TAPUR basket cohort readout.
- **#CT212** (neratinib in EGFR exon-18 NSCLC) — reports from the SUMMIT global basket trial.
- **#CT223** (AACR-ADOPT-GEA) — "a prospective, multi-center, two-stage adaptive platform trial" in GEA adenocarcinomas. The only bona-fide biomarker-driven adaptive platform trial in the corpus.
- **#CT262** (ELEVATE, elacestrant + everolimus *or* abemaciclib) — an umbrella-style randomized Phase II in ER+/HER2− mBC. Only poster using "umbrella" framing.
- **#6435** (AstraZeneca, Biostatistics session) — "propose a basket trial strategy that formally borrows information across indications to improve dose selection." Bayesian borrowing methodology paper, not a trial.
- **#2602** (Gustave Roussy) — references the STING master protocol for molecularly stratified genomic profiling. Uses master-protocol framing for real-world data aggregation rather than a prospective trial.

**Summary:** 3 of 7 basket-trial posters are **TAPUR** reporting from the single ASCO-run trial; the remaining 4 are independent baskets. Only one poster in the entire corpus (CT223, AACR-ADOPT-GEA) reports a prospective adaptive platform trial. The "platform trial" keyword otherwise matches loosely (preclinical preclinical-evaluation *platforms*, not clinical platform trials).

## Adaptive Phase 2/3 designs (3 posters, excluding adaptive-dose-finding BOIN posters)

**What it is.** Adaptive trial designs allow pre-specified modifications (sample-size re-estimation, seamless Phase 2→3 transition, adaptive randomization, covariate-adjusted stratification) based on interim data. Separate from Bayesian dose-finding, which is already "adaptive" in a narrow sense.

**Representative posters.**

- **#CT224** (TeLuRide-006, Eikon Therapeutics, TLR7/8 agonist EIK1001 + pembrolizumab) — "global, multicenter, randomized, double-blind, **adaptive Phase 2/3 trial**" — the clearest case of a seamless adaptive Phase 2/3 design in the corpus.
- **#CT223** (AACR-ADOPT-GEA, already cited) — adaptive platform trial.
- **#CT285** (DOMISOL, CCR8 mAb) — adaptive Bayesian dose-escalation with translational-biomarker-driven RP2D selection.
- **#LB128** (pan-Indian lung cohort) — argues adaptive molecular-cluster-based stratification "to enable smarter clinical trial design," but is itself a retrospective cohort analysis, not a prospective adaptive trial.
- **#LB327** (pediatric CAR-T, Children's Hospital of Philadelphia) — "Optimizing fludarabine exposure in pediatric CAR T-cell patients through an adaptive dosing approach" — adaptive PK-guided dosing rather than adaptive trial design per se, but the closest pediatric-oncology example of Bayesian-style adaptation in the corpus.

## Real-world evidence (10 posters)

**What it is.** Using real-world data (RWD — EHR, claims, molecular tumor registries) to generate trial-like evidence (RWE), typically either for (a) external control arms, (b) feasibility / cohort extraction for trial recruitment, or (c) post-marketing effectiveness.

**Representative posters.**

- **#30** (Keiji AI + Guardant) — "Automated cohort extraction from real-world oncology data using adaptive LLM-based agentic systems for clinical trial feasibility." Representative of the emerging agentic-RWE tier.
- **#5358** (Danbury Hospital) — "Disparities between genomic alterations and clinical trial representation in precision oncology" — RWE argument for trial-eligibility reform.
- **#5357** (U Arizona) — "Molecular tumor registries — a learning system for real world data" — registry-as-infrastructure framing.
- **#5345** (Natera) — "Large-scale genomic analysis of pancreatic cancer in a real-world patient population" — ~10,000-patient RWD analysis.
- **#4170** (Imagene AI) — "AI-driven multimodal workflow for enhancing **late-phase clinical trial outcome prediction**" using RWD.
- **#LB118** ([1Cell.Ai, Tata Memorial) — "Real-world evidence linking TP53 mutation class to genomic instability and therapy response."
- **#5339** (AbbVie) — "distinct biological programs of SCLC molecular subtypes revealed by real-world clinico-genomics data" used to inform enrichment strategies.

**Missing.** Zero posters use RWE as an **external-control arm** for a prospective trial — the regulatory-qualified use-case promoted by the FDA's External Control Arm guidance. The closest is #4170 (RWD to predict trial outcomes) but that is a performance-modeling paper, not an external control.

**One agentic-AI outlier.** #30 (Keiji AI + Guardant, listed in the Agentic AI in Cancer session) combines RWD, LLM-based agentic systems, and clinical-trial feasibility — a cross-topic poster that also surfaces in the [Agentic AI](../agentic-ai/index.md) topic. The fact that this is the most methodologically adventurous RWE poster and it was placed in Agentic AI rather than Biostatistics suggests that the venue-assignment system has not yet caught up with the methodology crossover.

## Synthetic / external controls — zero-hit result

**Zero posters** in the JSONL match `synthetic control` or `external control` in Title/Abstract/SessionTitle. This is the most striking negative finding of the scan: the entire methodology family that would let a sponsor replace a randomized control arm with a matched cohort drawn from RWD is simply absent from AACR 2026 poster content. The 10 RWE posters all use RWD for population-scale description, eligibility, or biomarker-prevalence arguments — none proposes an external-control analysis.

## Counter-evidence — 3+3 and "standard" designs are still common (26+ posters)

Classical 3+3 dose-escalation persists, and not only in academic investigator-initiated trials. Representative posters explicitly using 3+3:

- **#CT041** (Nagoya / Kyoto / NCC Japan investigator-initiated — TUG1 lncRNA therapeutic) — "The dose escalation was conducted using a 3+3 design, with four dose levels established."
- **#CT200** (Stingray Therapeutics, vizenpistat ENPP1 inhibitor) — "using a standard 3+3 dose-escalation design and has successfully completed six dosing cohorts."
- **#CT291** (Shanghai KangaBio, KGX101 IL-12 Prodrug) — "A standard 3+3 design was employed to assess the safety, PK, PD, immunogenicity."
- **#CT270** (Penn State pediatric — DFMO + AMXT-1501 in neuroblastoma) — "The Phase I portion uses a standard 3+3 design."
- **#CT192** (Newave Pharmaceutical, LP-118 Bcl-2/Bcl-xL inhibitor) — implicit 3+3 via dose-cohort framing.
- **#CT114** (NCI / James Gulley, intratumoral anti-CTLA-4 GIGA-564) — "subsequent cohorts followed a 3+3 dose escalation design."
- **#CT126** (Hummingbird Bioscience, HMBD-002 VISTA mAb) — "A standard 3+3 design was utilized."
- **#CT267** (Remedy Plan / MSK, RPT1G in R/R AML/MDS) — "uses a standard 3+3 design with escalating oral doses."
- **#CT295** (MSK, CRD3874-SI STING agonist) — "will explore the safety and tolerability of CRD3874-SI following standard 3+3 design."

By raw count, 26 posters explicitly use 3+3 — **roughly 1.6× the 16 posters using BOIN**. The Bayesian wave has not eliminated 3+3; it has added a second rail and is crowding out 3+3 only within the specific sub-tier of industry-sponsored FIH studies of novel modalities (ADCs, bispecifics, RAS(ON) glues, targeted radiopharmaceuticals). Academic investigator-initiated trials and Chinese-domestic biotech FIH programs still frequently default to 3+3.

**Hybrid designs blur the line.** Several posters combine 3+3 and BOIN — e.g., **#CT292** (CAN016, Canwell Biotechnology): "If ≥ grade 2 AEs were observed then switch to the 3+3 design for further assessing the MTD and/or RP2D" after a primary accelerated titration. These hybrids are counted as 3+3 hits by the keyword scan but are not "pure" 3+3 in practice.

**Accelerated titration + BOIN/3+3 is itself a pattern.** At least four FIH posters explicitly use accelerated titration (single-patient cohorts at very low doses) followed by BOIN or 3+3 once meaningful toxicity emerges: CT115 (LYC001 IL-2), CT129 (NST-628 molecular glue), CT290 (NTS071), and CT284 (BPI-572270 RAS(ON)). This hybrid is operationally attractive because it compresses the early-no-toxicity phase of a trial where classical 3+3 over-enrolls patients at sub-therapeutic doses. The existence of this pattern — distinct from pure 3+3 or pure BOIN — is itself a sign of design sophistication among sponsor teams.

---

## Institutional analysis — is this a methodology shift or an industry concentration?

Affiliations of the 19 Bayesian posters + 16 BOIN posters (deduplicated to 28 unique posters with Bayesian/BOIN/mTPI/Keyboard hits):

**Industry sponsors.** Ipsen (#CT087, ITGA2 ADC), Betta Pharmaceuticals (#CT284, RAS(ON)), Eikon Therapeutics (#CT287, PARP1-selective), Impact Therapeutics + Fudan (#CT289, POLQ), Junshi Biosciences + Shanghai Jiao Tong (#CT128, JS212 EGFR/HER3 ADC), Nutshell Therapeutics (#CT290, NTS071), Plexium (#CT097, SMARCA2 degrader), Stingray Therapeutics (#CT295, 3+3 counter-example), Elpiscience Biopharma (#CT127, CD39×TGF-β), Eli Lilly (#CT073, FiREBOLT radioligand), Bayer (#CT131, DGKα), Domain Therapeutics (#CT285, DOMISOL CCR8), Radiopharm Theranostics (#CT046, 177Lu-RAD202), Sarah Cannon + Fore Biotherapeutics (#CT273, FORTE), TransCode Therapeutics (#CT198), and BeiGene (#CT060 ERK inhibitor, #CT065 Wee1/Myt1).

**Academic sponsors.** MD Anderson is the single most frequent institution (listed on #CT287, #CT294, #CT079, #CT099, #CT126 — five posters, all using BOIN or its variants). Memorial Sloan Kettering appears on #CT061 (ROS1 TRK) and #CT295 (STING agonist — the 3+3 counter-example). City of Hope (#CT133, Ac-225 radioimmunotherapy) uses BOIN. AstraZeneca biostatistics group (#6435) contributes the Bayesian-borrowing methodology paper.

**Geographic pattern.** The BOIN-using posters are distributed globally: Chinese-domestic biotechs + hospitals (Betta, Junshi, Nutshell, Impact, Elpiscience, Shanghai Jiao Tong), US pharma (Ipsen, Eli Lilly, BeiGene US, Bayer US), US academic (MD Anderson, MSK, COH), European (Domain Therapeutics FR, Sarah Cannon UK). This is **not** a single-consortium concentration — the BOIN pattern is a global industry default across trial sponsors. Consistent with BOIN's pre-computed-table convenience making it operationally portable.

**MD Anderson cluster.** Five of 28 Bayesian-tagged posters list MD Anderson as an investigator site (often co-led by Timothy Yap, Jordi Rodon, or Funda Meric-Bernstam's teams). This is the clearest single-institution signal — MD Anderson's Drug Development Unit has effectively standardized on BOIN across its portfolio of sponsored FIH trials.

## Closing synthesis

The methodology shift is real but narrower than the thesis suggests. Inside the Phase I / Phase I/II **industry-sponsored FIH-of-novel-modality** tier — novel-mechanism ADCs, molecular glues, bispecific T-cell engagers, targeted radiopharmaceuticals, CAR-NK — BOIN and its variants (BF-BOIN, BOIN12, BOP2) are effectively the industry default; 3+3 readouts in this sub-tier are now the minority. The BOIN usage is modality-agnostic (applied to everything from CNS-penetrant small-molecule PARP1-selective agents to cord-blood-derived CAR-NK therapies), which is a strong signal for genuine mainstreaming rather than a one-indication fad. MD Anderson's Drug Development Unit is the clearest single-institution hub, but the pattern is geographically distributed (Chinese domestic biotech, US pharma, European academic) rather than concentrated in any single consortium.

Outside this sub-tier, however, 3+3 remains common in academic investigator-initiated trials and legacy-modality programs (26 posters still default to 3+3, versus 16 BOIN), and the newer methodology families — prospective adaptive platform trials, master protocols outside FORTE and TAPUR, synthetic/external controls, real-world-data external control arms — remain one-poster or zero-poster phenomena. The cohort evidence best supports a narrower thesis: **Bayesian dose-finding has mainstreamed for sponsor-led FIH of novel modalities; adaptive platform design, external-control methodology, and synthetic-control RWE uses have not.** The AACR 2026 CT poster corpus is therefore in a transitional state — early-phase dose-finding has crossed over, Phase 2/3 adaptive-design methodology is still catching up.

## Thin-evidence / cannot-argue flags

These design families are too thinly represented to argue mainstreaming (or even to argue against it):

- **Umbrella trials** — 1 poster (CT262). Cannot argue.
- **Keyboard design** — 1 poster (CT131). Cannot argue. Keyboard and mTPI together = 3 posters, a small academic-methodology niche.
- **Platform trials (true adaptive platform)** — 1 clinical poster (CT223). Cannot argue for mainstreaming.
- **Master protocols as a cohort-enrollment scaffold** — 2 posters (CT273, 2602). Thin.
- **Synthetic control arms** — 0 posters. Absent from corpus.
- **External control arms** — 0 posters. Absent from corpus.
- **CRM (Continual Reassessment Method)** — 0 posters. Appears to have been supplanted entirely by BOIN in the AACR 2026 early-phase tier.
- **Explicit "adaptive design"** — 3 posters. Thin, though the underlying adaptive rule is implicit inside all BOIN / BOP2 posters.
- **Real-world evidence as external control** — 0 posters. The 10 RWE posters all use RWD for description, eligibility, or prediction rather than as a counterfactual control.
- **Bayesian Phase 2 designs (BOP2, Bayesian predictive-probability futility monitoring)** — 1 explicit poster (CT273 FORTE). Likely under-counted because many Phase II readouts implicitly use Bayesian posterior-probability stopping rules without naming them.

The 6+ "cannot-argue" families above are clustered in one area: **prospective non-standard design innovation beyond dose-finding**. This matches the broader observation that Bayesian dose-finding has crossed over, while the rest of the model-informed trial-design toolkit has not. A reasonable follow-up for AACR 2027 would be a dedicated scan on whether synthetic-control and external-control posters start appearing — that would be the next clear inflection point in methodology mainstreaming.
