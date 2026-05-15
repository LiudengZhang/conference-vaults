# ASCO GU 2026

**2026 ASCO Genitourinary Cancers Symposium** — Moscone West, San Francisco, CA · Feb 26 – 28, 2026. ~3,500 attendees (in-person + virtual hybrid). Co-sponsored by ASCO, ASTRO, and SUO; this is the GU-cancer subspecialty meeting where prostate / RCC / urothelial practice-changers first read out — often months before an ASCO main-meeting update.

> **Status:** Post-meeting scaffold built **10 weeks after** the symposium closed (today: May 11, 2026). The structure mirrors [ASCO 2026](../asco-2026/index.md) — a per-trial vault driven by public coverage (Meeting Library abstracts post-embargo, ASCO Daily News, OncLive, Targeted Oncology, Cancer Therapy Advisor, urology trade press). Some entries flagged `*forward-looking*` for trials whose ASCO GU readout was a preview / interim, with the practice-changing update expected at ASCO 2026 main meeting (May 29 – Jun 2) or ESMO 2026 (Oct 23 – 27).

## Why this is in the vault

ASCO GU is the **GU-cancer subspecialty counterpart** to [ASCO 2026](../asco-2026/index.md) main meeting. Where ASCO main is broad (40,000 attendees, all tumor types), ASCO GU is deep (3,500 attendees, prostate + RCC + urothelial + rare GU only) — and the practice-changing GU data **almost always lands here first**, with ASCO main reserved for OS / follow-up updates and cross-disease themes.

Examples from the 2026 cycle:

- **KEYNOTE-B15 / EV-304** (perioperative EV+pembro vs cis/gem in MIBC) — practice-changing EFS readout (HR 0.53) at ASCO GU Feb 27; an ASCO 2026 main-meeting update is expected with OS-mature data.
- **LITESPARK-022** (adjuvant pembro+belzutifan vs pembro in ccRCC) — DFS positive (HR 0.72) at ASCO GU Feb 26; sNDA already under FDA priority review at time of GU readout.
- **PEACE-3** (enza+Ra-223 vs enza in mCRPC) — OS positive (HR 0.76) at ASCO GU 2026, after the earlier rPFS readout at ESMO 2024. ASCO 2026 main meeting will host the bone-mets subgroup follow-up.

The pattern: **ASCO GU = first reveal; ASCO main / ESMO = mature update**. This vault captures the first-reveal entries; cross-links point to the follow-up vaults.

**Format note:** ASCO GU is **clinical, not tools-focused**. Same design decision as ASCO 2026 main — the per-tool template that fits EuroBioC2025 / GBCC2025 / ISMB 2026 does not apply. Primary artifact is the **per-trial / per-readout** entry. Template at `trials/index.md`.

## What we have to work with

| Source | Coverage | Notes |
|---|---|---|
| **ASCO Meeting Library** | abstract full-text (regular) post-Feb 24 embargo lift; LBA full-text on day of presentation | [meetings.asco.org](https://meetings.asco.org/) — primary source for per-trial pages |
| **ASCO GU 2026 Program** | session grid, oral abstract sessions, panel discussions | [asco.org/gu](https://www.asco.org/gu) |
| **ASCO Daily News** | post-session recaps, official ASCO editorial | [dailynews.ascopubs.org](https://dailynews.ascopubs.org/) |
| **OncLive / Targeted Oncology / CancerNetwork** | discussant-level depth, expert reaction video stand-ups, post-meeting "experts recount" panels | [onclive.com](https://www.onclive.com/), [targetedonc.com](https://www.targetedonc.com/), [cancernetwork.com](https://www.cancernetwork.com/) |
| **UroToday / Renal & Urology News / Cancer Therapy Advisor** | urology-specialist coverage (deeper on rare GU and surgical perspectives) | [urotoday.com](https://www.urotoday.com/), [renalandurologynews.com](https://www.renalandurologynews.com/) |
| **Roche/Genentech medically.gene.com** | sponsor-curated congress hub with session-by-session summaries | [medically.gene.com](https://medically.gene.com/global/en/oncology/congresses/gu-cancers-symposium-2026.html) |
| **OncoDaily / MedDataX / touchONCOLOGY** | post-meeting synthesis pieces, trial roundups | various |
| **Company press releases** | toplines (often pre-embargo), full presentation decks (post-presentation) | wire-service syndication |

The **ASCO Meeting Library** is the load-bearing primary source. Every accepted abstract has a permalink; per-trial pages should cite the abstract DOI / permalink, not the company press release.

## Program shape

ASCO GU 2026 ran **Thursday Feb 26 – Saturday Feb 28**, three days, Moscone West, San Francisco. The structure:

- **Day 1 (Thu Feb 26) — Renal Cell Carcinoma.** LITESPARK-022 (LBA418, adjuvant pembro+belzutifan, DFS+) and LITESPARK-011 (LBA417, 2L belzutifan+lenva vs cabo) anchored the day. CYTOSHRINK (SBRT + nivo/ipi) in the late-afternoon orals.
- **Day 2 (Fri Feb 27) — Urothelial / Bladder.** KEYNOTE-B15 / EV-304 (LBA630, perioperative EV+pembro vs cis/gem, EFS HR 0.53) was the headliner. SunRISE-2 (gemcitabine intravesical system + cetrelimab) missed BI-EFS but signaled CR rates worth follow-up. IMvigor011 (ctDNA-guided adjuvant atezo) and NIAGARA biomarker analyses flagged the ctDNA-monitoring transition.
- **Day 3 (Sat Feb 28) — Prostate.** PEACE-3 OS positive (HR 0.76) for enza+Ra-223 vs enza in mCRPC. PSMAaddition (1L mHSPC ¹⁷⁷Lu-PSMA-617 + ADT + ARPI). MEVPRO-3 (mevrometostat EZH2i + enza). BRCAAway (PARPi + ARPI in HRR-altered mCRPC). CAPItello-281 (capivasertib + abi in PTEN-deficient mHSPC). First-in-human ²²⁵Ac-PSMA dose escalation.
- **Format:** ~3 oral abstract sessions per day + ~10 rapid-orals + multi-disciplinary panel discussions. ~1,200 abstracts total (orals + posters + online publication). Hybrid attendance: in-person ~2,400 + virtual ~1,100.
- **Tracks dominating the corpus:** Prostate (hormone-sensitive, CRPC, oligo-metastatic, PSMA-targeted RLT), RCC (frontline IO+TKI, adjuvant), urothelial (1L IO+ADC, FGFR), testicular, penile, adrenal. Cross-cutting: **radioligands, perioperative IO, ctDNA-guided adjuvant, ADCs in bladder, HIF-2α in RCC**.

## Organization

```
conferences/asco-gu-2026/
├── index.md             # this page
├── program-notes.md     # pre-meeting prep notes (reconstructed): tracks, expected LBAs, discussant watch list, key dates
└── trials/              # PRIMARY artifact — one entry per trial / readout
    └── index.md         # template + master trial index table
```

No `themes.md` or `digest/` directory at this scaffold stage; the three-day program is short enough that day-by-day digest is folded into the trial-index table. Synthesis themes will land in trial pages' "cross-links" sections, not as standalone pages.

## What's different from ASCO 2026 main

- **GU only.** Three tumor groups (prostate, RCC, urothelial) + rare GU (testicular, penile, adrenal). No GI, lung, breast, heme, melanoma.
- **Subspecialty audience.** Practicing urologic oncologists + med oncs + rad oncs. Discussion is deeper but narrower than ASCO main.
- **Pre-reveal cycle is shorter.** Many ASCO GU readouts are first-disclosure events — no ESMO 2025 preview, no AACR 2026 mechanism backing. So the per-trial pages here often **stand alone** rather than chaining to prior-conference entries.
- **Some readouts are interim / preview for ASCO main.** When a trial's GU readout is rPFS or DFS, the OS / mature update typically lands at ASCO main meeting in May/June or ESMO in October. Flag as `*forward-looking — OS follow-up expected at ASCO 2026 main meeting*` where applicable.

## Cross-vault links

- **[ASCO 2026 main](../asco-2026/index.md)** — same investigator network, broader scope. GU trials that read out at GU 2026 often get a follow-up update at the main meeting. Notably: **PROTEUS** (apalutamide perioperative HRLPC) on the ASCO main Plenary LBA1 slot — sibling to PEACE-3 / CAPItello-281 here.
- **[AACR 2026](../aacr-2026/index.md)** — mechanism / biomarker / preclinical side. HIF-2α belzutifan biology, EZH2 / mevrometostat mechanism work, and PSMA-targeted RLT pharmacology all have AACR 2025/2026 sessions backing the ASCO GU 2026 clinical readouts.
- **[JPM 2026](../jpm-2026/index.md)** — financing / dealmaking layer. Multiple ASCO GU 2026 trial sponsors were on the JPM stage in January (Merck belzutifan / pembro franchise; Pfizer Padcev/enfortumab vedotin; AstraZeneca volrustomig; Bayer radioligand pipeline).
- **[Conferences timeline](../../timeline.md)** — ASCO GU's position in the year's oncology cycle (JPM Jan → ASCO GI Jan → ASCO GU Feb → AACR Apr → ASCO May/Jun → ESMO Oct → ASH Dec).

## Next step

- **Already in-meeting (Feb 26–28):** scaffolded.
- **Now (post-meeting, May 11):** populate per-trial pages from the abstract Meeting Library + post-meeting OncLive / Targeted Oncology / CancerNetwork "experts recount" coverage. ~15 trial entries on the priority shortlist (KEYNOTE-B15, LITESPARK-022, LITESPARK-011, PEACE-3, PSMAaddition, MEVPRO-3, BRCAAway, CAPItello-281, IMvigor011, NIAGARA biomarker, CYTOSHRINK, SunRISE-2, ²²⁵Ac-PSMA first-in-human, plus 2 rare-GU entries).
- **Forward-looking (May 29 – Jun 2):** flag the ASCO 2026 main-meeting follow-up entries (PROTEUS perioperative prostate as the Plenary sibling; OS updates for trials whose rPFS read out at GU).
- **Forward-looking (Oct 23 – 27):** ESMO 2026 typically hosts the OS follow-up for ASCO GU positive PFS / DFS readouts; reconcile post-ESMO.

## Sources

- [ASCO GU Symposium home](https://www.asco.org/gu)
- [ASCO GU Dates to Know](https://www.asco.org/gu/dates-know)
- [Roche/Genentech medical congress hub — ASCO GU 2026](https://medically.gene.com/global/en/oncology/congresses/gu-cancers-symposium-2026.html)
- [ASCO Daily News — Planning Your GU26 Symposium Experience](https://dailynews.ascopubs.org/do/planning-your-gu26-symposium-experience)
- [Targeted Oncology — ASCO GU 2026 Preview](https://www.targetedonc.com/view/asco-gu-2026-preview-highlights-of-key-trials-in-bladder-kidney-prostate-and-rare-cancers)
- [OncoDaily — ASCO GU 2026: 10 Most Promising Trials](https://oncodaily.com/trial-updates/asco-gu-2026)
- [OncLive — Experts Recount the Most Notable Data From the 2026 GU Cancers Symposium](https://www.onclive.com/view/experts-recount-the-most-notable-data-from-the-2026-genitourinary-cancers-symposium)
- [CancerNetwork — How Will Data From ASCO GU 2026 Affect the Treatment Paradigm?](https://www.cancernetwork.com/view/how-will-data-from-asco-gu-2026-impact-the-treatment-paradigm-)
- [Renal & Urology News — ASCO GU 2026: 6 Key Takeaways](https://www.renalandurologynews.com/features/asco-gu-2026-6-takeaways/)
- [Cancer Therapy Advisor — ASCO GU 2026 to Highlight the Latest Developments](https://www.cancertherapyadvisor.com/reports/asco-gu-2026-to-highlight-the-latest-developments-in-genitourinary-cancer/)
- [touchONCOLOGY — ASCO GU26: What's new and what you need to know](https://touchoncology.com/insight/asco-gu26-whats-new/)
- [UroToday — ASCO GU 2026 conference highlights](https://www.urotoday.com/conference-highlights/asco-gu-2026/)
