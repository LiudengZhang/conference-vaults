export const meta = {
  name: 'asco-2026-vault-build',
  description: 'Build out ASCO 2026 trial pages, day digests, and themes with verified post-meeting results',
  phases: [
    { title: 'Discover', detail: 'per-track agents surface real reported ASCO 2026 trials' },
    { title: 'Build trials', detail: 'research→write one verified page per trial' },
    { title: 'Synthesize', detail: '5 day digests + themes.md' },
  ],
}

const BASE = '/Users/lzhang34/Desktop/conference-vaults/docs/conferences/asco-2026'

// Already built by hand (Plenary tier) — do not rebuild.
const ALREADY = new Set(['proteus', 'sarc041', 'libretto-432', 'harmoni-6', 'rasolute-302'])

// Curated, well-sourced seed list (acronym + filename + research hint + day).
const SEED = [
  // Lung
  { file: 'wu-kong28', acronym: 'WU-KONG28 (LBA8500)', day: 'Fri May 29', hint: 'sunvozertinib vs platinum chemo, 1L EGFR exon20ins NSCLC, Dizal, PFS' },
  { file: 'alchemist-ea5142', acronym: 'ALCHEMIST EA5142 (Abstract 8000)', day: 'Mon Jun 1', hint: 'adjuvant nivolumab after chemo in resected NSCLC, ECOG-ACRIN/NCI, DFS/OS' },
  { file: 'crown-7yr', acronym: 'CROWN (Abstract 8502)', day: 'unknown', hint: 'lorlatinib 1L ALK+ NSCLC 7-year update, Pfizer, PFS and CNS' },
  { file: 'triton', acronym: 'TRITON (Abstract 8515)', day: 'unknown', hint: 'AstraZeneca dual checkpoint in STK11/KEAP1/KRAS-mut nonsquamous NSCLC, ORR/PFS' },
  { file: 'triplex', acronym: 'TRIPLEX (LBA8005)', day: 'Tue Jun 2', hint: 'thoracic radiotherapy + chemo-immunotherapy 1L ES-SCLC, French cooperative, OS' },
  { file: 'dareon-5', acronym: 'DAREON-5', day: 'unknown', hint: 'obrixtamig DLL3 bispecific in SCLC/neuroendocrine, Boehringer Ingelheim' },
  // GI
  { file: 'herizon-gea-01', acronym: 'HERIZON-GEA-01', day: 'unknown', hint: 'zanidatamab + chemo +/- tislelizumab vs trastuzumab+chemo 1L HER2+ gastric/GEJ, Jazz/BeiGene, PFS/OS' },
  { file: 'breakwater', acronym: 'BREAKWATER', day: 'unknown', hint: 'encorafenib + cetuximab + FOLFIRI 1L BRAF V600E mCRC, Pfizer, OS/PFS' },
  { file: 'origami-1', acronym: 'OrigAMI-1', day: 'unknown', hint: 'amivantamab + chemo in mCRC, J&J, durability/ORR' },
  { file: 'rmc-9805', acronym: 'RMC-9805 (KRAS G12D)', day: 'unknown', hint: 'RMC-9805 oral KRAS G12D(ON) inhibitor early-phase PDAC/CRC, Revolution Medicines' },
  // GU
  { file: 'keynote-b15', acronym: 'KEYNOTE-B15 / EV-304', day: 'unknown', hint: 'perioperative enfortumab vedotin + pembro vs chemo in MIBC, Pfizer/Astellas/Merck, EFS' },
  { file: 'litespark-022', acronym: 'LITESPARK-022', day: 'unknown', hint: 'adjuvant pembrolizumab + belzutifan in ccRCC, Merck, DFS' },
  { file: 'litespark-011', acronym: 'LITESPARK-011', day: 'unknown', hint: 'belzutifan + lenvatinib vs cabozantinib 2L+ RCC, Merck, PFS' },
  { file: 'peace-3', acronym: 'PEACE-3', day: 'unknown', hint: 'enzalutamide + radium-223 vs enzalutamide mCRPC, OS/rPFS' },
  { file: 'psma-ac225', acronym: 'Actinium-225 PSMA', day: 'unknown', hint: '225Ac-PSMA targeted alpha radioligand mCRPC dose escalation, Fred Saad' },
  // Breast
  { file: 'ascent-04', acronym: 'ASCENT-04 (LBA1000/LBA1013)', day: 'Sun May 31', hint: 'sacituzumab govitecan + pembro vs chemo+pembro 1L PD-L1+ metastatic TNBC, Gilead, PFS / biomarker subgroups' },
  { file: 'perservera', acronym: 'persevERA (LBA1006)', day: 'unknown', hint: 'giredestrant + palbociclib 1L ER+/HER2- metastatic BC, Roche, PFS — primary missed' },
  { file: 'serena-6', acronym: 'SERENA-6 PFS2 (LBA1007)', day: 'unknown', hint: 'camizestrant ctDNA-guided switch ESR1-mut 1L ER+ MBC, AstraZeneca, PFS2' },
  { file: 'kn026-004', acronym: 'KN026-004 (LBA660)', day: 'unknown', hint: 'anbenitamab + nab-paclitaxel neoadjuvant HER2+ breast, Akeso/Hansoh, pCR' },
  // Heme
  { file: 'frontmind', acronym: 'frontMIND (LBA7000)', day: 'Sat May 30', hint: 'tafasitamab + lenalidomide + R-CHOP 1L DLBCL high IPI, Incyte, PFS HR ~0.75' },
  { file: 'majestec-3', acronym: 'MajesTEC-3', day: 'unknown', hint: 'teclistamab + daratumumab vs SOC in 1-3 prior line multiple myeloma, J&J, PFS' },
  { file: 'redirectt-1', acronym: 'RedirecTT-1', day: 'unknown', hint: 'talquetamab + teclistamab in extramedullary multiple myeloma, J&J, ORR/PFS' },
  { file: 'revumenib-aml', acronym: 'Revumenib (menin)', day: 'unknown', hint: 'revumenib menin inhibitor in KMT2A-r / NPM1-mut AML, Syndax, combination data' },
  { file: 'ziftomenib-aml', acronym: 'Ziftomenib (menin)', day: 'unknown', hint: 'ziftomenib menin inhibitor NPM1-mut AML, Kura Oncology' },
  // Melanoma / Other
  { file: 'optimum-02', acronym: 'OptimUM-02 (LBA9503)', day: 'Mon Jun 1', hint: 'darovasertib + crizotinib 1L HLA-A2-neg metastatic uveal melanoma, IDEAYA/Servier, PFS 6.9 vs 3.1 HR 0.42, ORR 37 vs 6%' },
]

const TRACKS = [
  { key: 'GI', q: 'colorectal, pancreatic, gastric/GEJ, hepatobiliary' },
  { key: 'GU', q: 'prostate, kidney/RCC, bladder/urothelial' },
  { key: 'Lung', q: 'NSCLC, SCLC, mesothelioma' },
  { key: 'Breast', q: 'HR+/HER2-, TNBC, HER2+' },
  { key: 'Heme', q: 'lymphoma, myeloma, leukemia/AML/MDS' },
  { key: 'Other', q: 'melanoma, sarcoma, gynecologic, head & neck, GLP-1/symptom science' },
]

const DISCOVER_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    trials: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          acronym: { type: 'string' },
          file: { type: 'string', description: 'kebab-case filename slug, no extension' },
          drug: { type: 'string' },
          indication: { type: 'string' },
          headline: { type: 'string', description: 'one-line reported result with numbers if available' },
          sources: { type: 'array', items: { type: 'string' } },
        },
        required: ['acronym', 'file', 'headline', 'sources'],
      },
    },
  },
  required: ['trials'],
}

const TRIAL_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    file: { type: 'string' },
    acronym: { type: 'string' },
    track: { type: 'string' },
    day: { type: 'string' },
    oneLineResult: { type: 'string' },
    practiceChanging: { type: 'string' },
    verified: { type: 'boolean' },
    wrote: { type: 'boolean' },
  },
  required: ['file', 'acronym', 'track', 'oneLineResult', 'verified', 'wrote'],
}

const PAGE_TEMPLATE = `# <Acronym> — <Drug regimen, indication, line>

> **Abstract:** <#> · **Session:** <name, date, time CT> · **Presenter:** <name, institution> · **Embargo:** <date>

## At a glance
- **Sponsor:** ...
- **PI / presenter:** ...
- **NCT ID:** ...
- **Phase:** ...
- **Design:** ...
- **N:** ...
- **Primary endpoint(s):** ...
- **Comparator:** ...
- **Indication:** ...
- **Line:** ...

## Headline result
<One paragraph. Numbers + HR + p-value. Cite real ASCO 2026 reported data.>

## Mechanism / class
<Drug class, target, prior approvals.>

## Discussant takeaway
<Named discussant + framing if reported; else omit.>

## Practice-changing?
<Yes / no / pending, with rationale.>

## Cross-links
- **AACR 2026:** <if applicable, ../../aacr-2026/index.md>
- **Other ASCO 2026 trials:** <same class/indication, ./<file>.md>
- **JPM 2026:** <sponsor deal if applicable, ../../jpm-2026/index.md>

## Sources
- ASCO Meeting Library: <url>
- Company / trade-press: <urls>`

// ---------- Phase 1: Discover ----------
phase('Discover')
const discovered = await parallel(TRACKS.map((t) => () =>
  agent(
    `You are researching the **2026 ASCO Annual Meeting** (May 29 – Jun 2, 2026, Chicago), which just concluded. ` +
    `Find the most important **${t.key}** track trials/abstracts (${t.q}) that were actually PRESENTED with reported results. ` +
    `Use web search/fetch (OncLive, ASCO Daily News, The ASCO Post, Targeted Oncology, CancerNetwork, Healio, company press releases, ASCO Meeting Library). ` +
    `Return up to 10 trials. ONLY include trials with real, reported ASCO 2026 results and at least one credible source URL — do NOT invent trials or numbers. ` +
    `Give each a kebab-case filename slug. Prefer well-known trial acronyms.`,
    { label: `discover:${t.key}`, phase: 'Discover', schema: DISCOVER_SCHEMA }
  )
))

const discoveredTrials = discovered.filter(Boolean).flatMap((d) => d.trials || [])

// Merge seed + discovered, dedupe by file slug, drop already-built, cap.
const seen = new Set(ALREADY)
const merged = []
for (const s of SEED) {
  if (seen.has(s.file)) continue
  seen.add(s.file)
  merged.push({ file: s.file, acronym: s.acronym, day: s.day, hint: s.hint })
}
for (const d of discoveredTrials) {
  const slug = (d.file || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
  if (!slug || seen.has(slug)) continue
  seen.add(slug)
  merged.push({ file: slug, acronym: d.acronym, day: 'unknown', hint: `${d.drug || ''} — ${d.indication || ''}. Reported: ${d.headline}. Sources: ${(d.sources || []).join(', ')}` })
}
const trialList = merged.slice(0, 65)
log(`Discover done: ${discoveredTrials.length} discovered, ${trialList.length} unique trials to build (after seed merge + dedupe).`)

// ---------- Phase 2: Build trial pages ----------
phase('Build trials')
const built = await pipeline(
  trialList,
  (t) => agent(
    `Build a verified per-trial page for the **2026 ASCO Annual Meeting** (May 29 – Jun 2, 2026, Chicago).\n\n` +
    `TRIAL: ${t.acronym}\nRESEARCH HINT: ${t.hint}\n\n` +
    `STEP 1 — RESEARCH (web search/fetch): confirm this trial was presented at ASCO 2026 and gather the reported results ` +
    `(endpoints, HR, p-values, median values, N, presenter, session/day, sponsor, NCT). Sources: ASCO Meeting Library (asco.org/abstracts), ` +
    `ASCO Daily News, OncLive, The ASCO Post, Targeted Oncology, CancerNetwork, Healio, company press releases.\n\n` +
    `STEP 2 — DECIDE: If you CANNOT find credible ASCO 2026 results for this trial, set verified=false and wrote=false and DO NOT write a file. ` +
    `Never fabricate numbers, presenters, or sources. If only a pre-meeting company topline exists, you may write it but flag inline as "*per <company> topline, <date>*".\n\n` +
    `STEP 3 — WRITE (only if verified): write the page to "${BASE}/trials/${t.file}.md" using the Write tool, following EXACTLY this schema (fill every field you have; omit a section only if truly N/A):\n\n` +
    PAGE_TEMPLATE + `\n\n` +
    `Style: terse, factual, cite real source URLs. Cross-links are relative (./<file>.md within trials/, ../../aacr-2026/index.md, ../../jpm-2026/index.md). ` +
    `Mark italic any number that is company-topline-only rather than presented.\n\n` +
    `Return the structured summary: file (="${t.file}"), acronym, track (GI/GU/Lung/Breast/Heme/Melanoma/Sarcoma/GYN/Other), ` +
    `day (Fri May 29 / Sat May 30 / Sun May 31 / Mon Jun 1 / Tue Jun 2 / unknown), oneLineResult (with numbers), ` +
    `practiceChanging (yes/no/pending), verified, wrote.`,
    { label: `trial:${t.file}`, phase: 'Build trials', schema: TRIAL_SCHEMA }
  )
)

const okTrials = built.filter(Boolean).filter((t) => t.wrote)
log(`Build done: ${okTrials.length}/${trialList.length} pages written (plus 5 hand-built Plenary pages).`)

// Include the 5 hand-built Plenary pages in the synthesis context.
const PLENARY = [
  { file: 'proteus', acronym: 'PROTEUS (LBA1)', track: 'GU', day: 'Sun May 31', oneLineResult: 'Perioperative apalutamide+ADT: pCR/MRD 8.9% vs 1.0%, MFS HR 0.80 (BICR); new SOC high-risk localized prostate', practiceChanging: 'yes' },
  { file: 'sarc041', acronym: 'SARC041 (LBA2)', track: 'Sarcoma', day: 'Sun May 31', oneLineResult: 'Abemaciclib vs placebo dedifferentiated liposarcoma: mPFS 9.7 vs 1.5 mo (~62% reduction); first positive Ph3', practiceChanging: 'yes' },
  { file: 'libretto-432', acronym: 'LIBRETTO-432 (LBA3)', track: 'Lung', day: 'Sun May 31', oneLineResult: 'Adjuvant selpercatinib RET+ NSCLC: 83% reduction in recurrence/death (EFS); first adjuvant RET TKI', practiceChanging: 'yes' },
  { file: 'harmoni-6', acronym: 'HARMONi-6 (LBA4)', track: 'Lung', day: 'Sun May 31', oneLineResult: 'Ivonescimab+chemo vs tislelizumab+chemo 1L squamous NSCLC: mOS 27.89 vs 23.69 mo; first OS win for PD-1xVEGF', practiceChanging: 'pending' },
  { file: 'rasolute-302', acronym: 'RASolute 302 (LBA5)', track: 'GI', day: 'Sun May 31', oneLineResult: 'Daraxonrasib vs chemo 2L mPDAC: mOS 13.2 vs 6.7 mo (HR 0.40); first pan-RAS Ph3 win in PDAC', practiceChanging: 'yes' },
]
const allTrials = [...PLENARY, ...okTrials]

// ---------- Phase 3: Synthesize (day digests + themes) ----------
phase('Synthesize')
const DAYS = [
  { file: 'day-1-friday', label: 'Day 1 — Friday May 29 (Education Day; first LBAs incl. WU-KONG28)' },
  { file: 'day-2-saturday', label: 'Day 2 — Saturday May 30 (Opening Session, Presidential Address, frontMIND)' },
  { file: 'day-3-sunday', label: 'Day 3 — Sunday May 31 (PLENARY: LBA1–LBA5; the load-bearing day)' },
  { file: 'day-4-monday', label: 'Day 4 — Monday Jun 1 (OptimUM-02, ALCHEMIST, TRIPLEX)' },
  { file: 'day-5-tuesday', label: 'Day 5 — Tuesday Jun 2 (closing oral sessions)' },
]
const trialDigestContext = allTrials.map((t) => `- [${t.acronym}] (${t.track}, ${t.day || 'unknown'}) trials/${t.file}.md — ${t.oneLineResult}`).join('\n')

const synth = await parallel([
  ...DAYS.map((d) => () =>
    agent(
      `Write the day-digest page "${BASE}/digest/${d.file}.md" for the **2026 ASCO Annual Meeting**.\n\n` +
      `THIS DAY: ${d.label}\n\n` +
      `Built trial pages available to link (relative path from digest/ is ../trials/<file>.md):\n${trialDigestContext}\n\n` +
      `Web-search to confirm which of these (and any other notable abstracts) were presented on THIS day, then write a crisp editorial recap (~400–700 words): ` +
      `lead with the day's headline readout, then 3–6 short sections grouped by track, each linking the relevant trial page with [acronym](../trials/<file>.md). ` +
      `Cite real coverage URLs. Start the file with "# <day label>". Only assert a day placement you can support; if unsure, say "reported during the meeting".\n\n` +
      `Use the Write tool to create the file. Return a one-line confirmation.`,
      { label: `digest:${d.file}`, phase: 'Synthesize' }
    )
  ),
  () => agent(
    `Write "${BASE}/themes.md" — the cross-day synthesis for the **2026 ASCO Annual Meeting**.\n\n` +
    `Built trial pages (relative path from themes.md is trials/<file>.md):\n${trialDigestContext}\n\n` +
    `Organize around these threads (drop any unsupported, add any that clearly emerged): ` +
    `(1) RAS-class drugs become real (daraxonrasib + KRAS-G12D); (2) PD-1×VEGF bispecific class (HARMONi-6 OS); ` +
    `(3) perioperative/adjuvant targeting expands (PROTEUS, KEYNOTE-B15, LIBRETTO-432, ALCHEMIST); (4) ADC durability (ASCENT-04); ` +
    `(5) endocrine-backbone resistance (persevERA, SERENA-6); (6) China-origin assets dominate the LBA slate; (7) radioligands to randomized data (PEACE-3, Ac-225 PSMA); ` +
    `(8) biomarker-matched wins in rare tumors (SARC041 CDK4, darovasertib uveal melanoma).\n\n` +
    `For each theme: 1 short paragraph citing the specific trials with [acronym](trials/<file>.md) links and AACR/JPM cross-links where relevant. ` +
    `Start with "# Themes — ASCO 2026". Use the Write tool. Return a one-line confirmation.`,
    { label: 'themes', phase: 'Synthesize' }
  ),
])

return {
  builtPages: okTrials.length,
  trials: allTrials.map((t) => ({ file: t.file, acronym: t.acronym, track: t.track, day: t.day, oneLineResult: t.oneLineResult, practiceChanging: t.practiceChanging })),
  digests: DAYS.map((d) => d.file),
  synthConfirmations: synth.filter(Boolean),
}
