# FAIR-EASE

**FAIR data infrastructure for Earth-system and environmental sciences on Galaxy** — a multi-year European project bringing FAIR (Findable, Accessible, Interoperable, Reusable) workflows to Earth-system science domains via Galaxy, the climate / ocean / biodiversity counterpart to Galaxy's biomedical use.

- **Galaxy tool / platform:** [fairease.eu](https://fairease.eu/) — uses [earth-system.usegalaxy.eu](https://earth-system.usegalaxy.eu/) as the Galaxy server
- **Source:** [github.com/fair-ease](https://github.com/fair-ease)
- **Documentation / training:** [Galaxy Training Network — climate / ecology](https://training.galaxyproject.org/training-material/topics/climate/); FAIR-EASE-specific tutorials linked from `fairease.eu`
- **Authors at GBCC2025:** Marie Jossé, Jérôme Detoc, Erwan Bodéré
- **Status at GBCC2025:** cross-domain Galaxy deployment — two-year retrospective talk

## Talk at GBCC2025

- **Speakers:** Marie Jossé, Jérôme Detoc, Erwan Bodéré
- **Day / session:** Day 4 (Thu Jun 26, 2025) — Oral Session 5
- **Talk title:** "Bridging Earth System Sciences with Galaxy: Two Years of FAIR-EASE"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

FAIR-EASE deploys Galaxy as the workflow engine for Earth-system science use cases — biodiversity (GBIF / occurrence-record processing), marine (Argo float / ocean-color analysis), and atmospheric / climate workflows. The project couples Galaxy with domain data lakes (e.g., the EOSC and Pangaea archives) and contributes Earth-system tools to the Galaxy ToolShed. The two-year retrospective covers community building, tool contributions, and lessons from running Galaxy outside its biomedical home turf.

## How it works

**Core idea.** FAIR-EASE is described as "the first interdomain digital architecture for integrated use of environmental data" — it stitches Galaxy (workflow engine), an Earth Analytics Lab (interactive analysis), and a set of data-discovery / access services into a stack that operationalises the FAIR principles on Earth-system data rather than biomedical data.

**Inputs / outputs.** Input: heterogeneous environmental datasets (climate, ocean, biodiversity, food-security observation streams) sourced via FAIR-discovery and FAIR-access services. Output: reproducible analyses run on the Earth-System Galaxy instance ([earth-system.usegalaxy.eu](https://earth-system.usegalaxy.eu/)), plus Earth-domain tools and workflows contributed back to the Galaxy ToolShed and Training Network.

**Key innovation.** Treating "Galaxy" as a domain-portable workflow substrate. The project demonstrates the Galaxy patterns — ToolShed, IWC-style workflow curation, GTN training, federation — apply unchanged to climate / ocean / biodiversity, with the EU's Earth-System Galaxy server as the deployment.

**Parameters / API surface worth knowing.**
- Five FAIR-EASE result areas — data-discovery, data-access, analytical frameworks (Earth Analytics Lab), real-world demonstrators, best-practice / FAIR-by-design guidance.
- Earth-System Galaxy instance — `earth-system.usegalaxy.eu`, the deployment target for Earth-domain tools.
- Tool contributions — Earth-system tools land in the Galaxy ToolShed alongside biomedical ones.
- Training material — climate / ecology topics in the Galaxy Training Network.
- EOSC alignment — outputs feed into the European Open Science Cloud ecosystem.

**Canonical example.** *Not specified in the public site at the level of a single canonical workflow.* The two-year retrospective at GBCC2025 frames the canonical use cases as biodiversity (GBIF occurrence-record processing), marine (Argo / ocean-color analyses), and atmospheric / climate workflows run on the Earth-System Galaxy server.

## Where it fits in the corpus

- **AACR 2026:** orthogonal — included for ecosystem-mapping completeness, like NOVA. The cross-domain reach demonstrates Galaxy's scope beyond biomedicine.
- **Galaxy-E** ([usegalaxy.eu](https://usegalaxy.eu/)) — sister deployment effort; FAIR-EASE feeds tools into the European Galaxy ecosystem
- **GBCC2025 ecosystem thread** — alongside AnVIL (US biomedical cloud) and FAIR-EASE (EU Earth-system), the meeting maps how Galaxy spans clouds and domains

## Notes

FAIR-EASE matters here as a counter-example: Galaxy is not a biomedical-only platform, and the patterns (workflow registry, training network, tool-shed contributions) port cleanly to a totally different scientific domain. The two-year mark is the right time for a retrospective — early adoption is over, sustainability is the new question.
