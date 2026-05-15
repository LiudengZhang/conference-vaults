# TPV Broker

**Dynamic meta-scheduling for Galaxy** — a metascheduler that sits on top of Total Perspective Vortex (TPV), Galaxy's pluggable rules engine for routing jobs to destinations. The broker ranks short-listed destinations across heterogeneous backends (HPC clusters, cloud, on-prem) and distributes load across the usegalaxy.* federation rather than treating each instance as an island.

- **Authors:** Paul De Geest, Sanjay Srikakulam, et al. (usegalaxy-eu / VIB-UGent)
- **Galaxy tool / platform:** [usegalaxy-eu/tpv-broker](https://github.com/usegalaxy-eu/tpv-broker)
- **Source:** [github.com/usegalaxy-eu/tpv-broker](https://github.com/usegalaxy-eu/tpv-broker); core TPV at [galaxyproject/total-perspective-vortex](https://github.com/galaxyproject/total-perspective-vortex)
- **Documentation / training:** [TPV docs (readthedocs)](https://total-perspective-vortex.readthedocs.io/) · [shared rules database](https://github.com/galaxyproject/tpv-shared-database)
- **Status at GBCC2025:** oral talk on cluster-side scheduling for Galaxy

## Talk at GBCC2025

- **Speakers:** Paul De Geest, Sanjay Srikakulam
- **Day / session:** Day 2 (Tue Jun 24, 2025) — Oral Session 2A, Bush Hall
- **Talk title:** "Dynamic meta-scheduling in Galaxy with TPV Broker for smarter workload distribution"
- **Slides:** TBD
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

Total Perspective Vortex is a YAML-driven rules engine that maps Galaxy entities (Tools, Users, Roles) to destinations with appropriate resources (cores, GPUs, memory, walltime). TPV Broker plugs into TPV's ranking function: after candidate destinations are short-listed for a job, the broker — operating as a network service across the federation — ranks them based on real-time load, queue state, and policy. The result is dynamic load balancing across usegalaxy.org / .eu / .org.au and partner sites instead of static, per-instance routing.

## How it works

**Core idea.** TPV provides the YAML rules layer that maps Galaxy entities (Tools, Users, Roles) to candidate destinations with resource constraints; TPV Broker replaces TPV's static ranking function with a FastAPI network service that ranks those candidates against live infrastructure telemetry.

**Inputs / outputs.** Inputs to the broker are the short-listed candidate destinations (Pulsar, Slurm, local) plus job specs (cores, memory, GPUs, tool ID) and dataset attributes. Output is an ordered list of destinations; TPV submits the job to the top-ranked one.

**Key innovation.** Telemetry-driven, data-aware scheduling across a federation. Telegraf agents on each Galaxy / Pulsar node feed CPU, memory, queue-depth, and tool-timing metrics into InfluxDB; the broker queries that store at scheduling time, so routing decisions reflect *current* load instead of YAML defaults frozen at deploy time.

**Parameters / API surface worth knowing.**
- TPV rules YAML — declarative mappings from entities (Tools / Users / Roles) to destinations with cores / GPUs / memory / walltime hints; the [shared rules database](https://github.com/galaxyproject/tpv-shared-database) ships ready-made profiles.
- Broker HTTP endpoint — TPV calls this via POST during scheduling, passing candidates + job specs, receiving a ranked list back.
- Metrics stack — Telegraf → InfluxDB → broker ranking algorithms (queue length, resource utilization).
- Destinations — heterogeneous mix: HPC (Slurm), cloud, on-prem, Pulsar-attached remote clusters.

**Canonical example.** A federation operator defines TPV rules saying "RNA-seq alignment tools need 32 GB and 8 cores; eligible destinations are Slurm-EU, Slurm-AU, and Pulsar-cloud." When a job hits TPV, the broker is queried, returns rankings reflecting current queue depth at each site, and the job lands wherever queue pressure is lowest rather than always going to the operator's home cluster.

## Where it fits in the corpus

- **AACR 2026:** infrastructure layer — orthogonal to research axes but underpins reproducibility-at-scale arguments
- **EuroBioC 2025:** no direct counterpart (Bioconductor doesn't have a federation in this sense)
- **Nextflow Summit 2026:** parallel to discussions of executor/cloud burst routing

## Notes

TPV = Total Perspective Vortex (the *Hitchhiker's Guide* reference is intentional). The broker's value proposition only materialises at federation scale — included here as a reminder that the Galaxy infra story is increasingly multi-site, which matters when claiming workflow portability for cancer-research pipelines.
