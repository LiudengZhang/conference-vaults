# Synthesis — AT02 vs the 57-poster corpus

AACR 2026 session **AT02 ("Agentic AI as the Cancer Researcher: Autonomous Discovery in Oncology,"** Tue 4/21 2:30 PM PT, ~12,831 words) is the only dedicated AACR plenary-format session this year on agentic AI. Three speakers set the agenda from stage, each covering a different slice of the agent stack:

- **Danielle Bitterman** (Dana-Farber / Brigham and Women's) — agentic AI for late-stage clinical development and real-world-data curation; adverse-event monitoring as the worked example.
- **Sebastian Foersch** (University Medical Center Mainz) — AI agents in clinical tissue medicine, with a modular pathology-orchestrator system (diagnostic agent + IHC agent + reporting agent) as the worked example.
- **Marinka Zitnik** (Harvard) — open AI co-scientists via Tool Universe (a 2,000-tool scientific environment) and the MedEA agent; prospective EHR-based hypothesis generation as the worked example.

This page takes each speaker's 2-3 load-bearing claims from the AT02 transcript and asks the same question of each: **does the 57-poster AACR 2026 agentic-AI corpus support, contradict, or not address it?** The goal is to locate the gap between what leaders are saying from stage and what the rest of the field is actually shipping in posters.

*Name note: the auto-captioner renders Bitterman as "Bittermann" / "Peterman", Foersch as "Firsch" / "Forster" / "Forscht", and Zitnik as "zitnick" / "Sitnik". Silently corrected here per `docs/notes/caveats.md`. MedEA is also auto-rendered as "Medea" / "media" in the transcript.*

*Quotation note: quotes are lightly cleaned transcript fragments (paragraphing, filler, obvious ASR noise removed). Ellipses "[…]" mark joins.*

---

## Danielle Bitterman — agentic AI for clinical development

Bitterman opened the session by framing agentic AI against the ~10% phase-1-to-approval success rate of oncology drug development, arguing that most of the field's bottleneck is in multi-step, multi-system workflow coordination rather than single-model performance. Her group's published adverse-event pipeline achieves macro-F1 of 0.93 on immune-related adverse-event extraction from clinical notes at ~$0.02 per note, with a randomized user study showing 40% curator-time reduction at matched accuracy.

### Thesis 1 — The bottleneck in agentic clinical AI is no longer model performance; it is data integration, governance, and monitoring

> "The challenge with agentic systems is not the performance of the models, in my opinion. It's all the other work that has to go into making agentic systems a reality. Data integration with agentic systems is super important. […] You need to ensure value to demonstrate the need and return on investment of building the agentic workflows and its surrounding governance approach. Monitoring model drift and data drift […] is really important for any highly regulated setting, and governance bodies need to be set up to ensure that the ethical approach and safety are being governed in a responsible way. […] This requires a lot, currently the lion's share of effort for implementing agentic AI in clinical systems."

**Corpus verdict: partially supported — one governance-oriented poster, essentially no drift-monitoring or infrastructure posters.**

- **Supports (prospective implementation science)**: **#1393** (Jacob Rosenthal, a *prospective implementation study* design for an AI-assisted breast-trial-accrual workflow) is the single poster in the 57 that centers the deployment question Bitterman flags. **#34** (Haddad, AR-LA-TX veteran survey) and **#35** (Blenman, "Humans cannot live by AI alone") are the human-factors posters that address the governance / trust side without being technical papers.
- **Partially addresses**: **#30** (Theodorou, adaptive LLM-based cohort extraction for trial feasibility) and **#LB450** (Van Alsten, AI-assisted pathology-report abstraction for breast cancer) do describe production data-integration work at institutional scale but do not foreground governance or drift monitoring.
- **Not addressed**: zero posters in the 57 report on model-drift monitoring, post-deployment auditing, or the "lion's share" of plumbing effort Bitterman describes. The corpus is biased toward method posters at the capability frontier, not deployment-science posters behind it.

### Thesis 2 — Current benchmarks (multi-choice QA) do not reflect real-world agentic use; we need stepwise, auditable evaluation

> "Our current standard approaches for evaluating the performance of these large language models largely relies on types of multi-choice question answer exams […]. The challenge is this does not necessarily reflect the type of real-world applications that we would really want to use these agentic AI systems in. […] Real-world applications […] have generative output and rely on faithful reasoning steps across agentic systems and reliable extraction from the correct evidence base. […] Sound scientific judgment and multi-step reasoning abilities are currently not covered by our evaluation strategy."

**Corpus verdict: not addressed.**

- No poster in the 57 presents a stepwise agentic-reasoning benchmark. **#2739** (Desai, "Evaluation of LLMs for automated clinical trial matching") and **#3** (Thiriveedi, evaluation of an agentic LLM chatbot on GENIE BPC data) are the two *evaluation* posters, but both report task-level accuracy on end outputs — not the faithful-reasoning-step audit Bitterman describes.
- **#2747** (Palumbo) benchmarks guideline-anchored LLM decision support against Open Evidence — a pairwise system comparison rather than stepwise reasoning evaluation.
- Bitterman's Q&A response reinforces the gap: *"As they become more performant, we are going to increasingly run into an issue that they may be doing tasks that we don't have human experts who can oversee it, and that's where I think it's going to become even more important to evaluate the stepwise breakdown of the agentic workflows."* Zero posters in the 57 address this stepwise-breakdown evaluation question.

### Thesis 3 — Real-world multi-step clinical workflows (adverse-event monitoring, patient matching, outcome monitoring) are the right near-term target; one-shot tasks are not

> "Why is agentic AI particularly exciting for the clinical development workflow? […] Our challenges [are] not just […] with our ability to access data or collect data, but really there are multi-step workflow challenges that require really deep coordination and iteration across many different fragmented systems. […] Insights to clinical development are not a one-stop kind of, we found this finding, and this is the answer, but it actually triggers timely action."

**Corpus verdict: strongly supported — this is the densest stage-to-poster alignment on the page.**

- **Adverse events and toxicity**: **#32** (Fort, real-world immune-related AE exploration), **#2755** (Lazar, LLM extraction of AEs at scale), **#2762** (Lu, LLM-extracted immunotherapy toxicities with severity-stratified OS).
- **Trial matching / eligibility / cohort extraction**: **#29** (Krawczuk, reasoning-guided retrieval for trial eligibility), **#2739** (Desai, LLM-based trial matching), **#30** (Theodorou, adaptive agentic cohort extraction), **#4** (Velazquez-Villarreal, multi-agent CRC precision-oncology ecosystem).
- **Diagnosis / staging curation from unstructured notes**: **#20** (Kang, agentic AI for cancer diagnosis + staging curation), **#2744** (Mohammed, automated clinical + pathological staging), **#2738** (Gyorffy, CIDER clinical-data extraction), **#2750** (Levy, on-site petabyte-scale LM for colon MSI curation).
- **Patient triage / clinical workflow**: **#2741** (Nguyen, LLM triage of hem/onc patient messages).
- This is effectively the entire "LLM-as-classifier / extractor" family plus half the "workflow automation" family. The AACR 2026 corpus is doing exactly what Bitterman says near-term agentic AI should do.

---

## Sebastian Foersch — AI agents for clinical tissue medicine

Foersch's talk argued that pathology is both uniquely well-suited to agentic orchestration (it's a step-by-step, multi-tool discipline — H&E, then IHC, then NGS, then reporting) and uniquely vulnerable to emergent AI risks (prompt injection via slide scribbling, watermark-bias attacks on vision models). His prototype is a minimum-viable-product system: an orchestrator LLM routes between a diagnostic microscopy agent (pathology FM), a textbook-RAG LLM, an IHC agent, an NGS agent, and a reporting agent, with a reasoning trace surfaced for quality management.

### Thesis 1 — Modular multi-agent pathology systems are the right architecture, because pathology is a step-by-step iterative diagnostic workflow

> "We have an orchestrating agent that is sort of steering the whole workflow. And then we start out with a diagnostic AI agent […] a pathology foundation model that has been fine-tuned on just sort of describing the microscopy of, for example, a whole slide image. […] It will then compare the microscopic description with the textbook knowledge and say, 'Okay, this is my initial diagnosis, and you have to do these couple of tests to confirm.' […] We think that this particular approach could be really valuable for rare tumor entities where pathological diagnosis is actually reliant on a step-by-step workflow […] such as hematopathology, sarcoma pathology, or salivary gland tumors."

**Corpus verdict: partially supported — strong in spatial biology, essentially empty in pathology orchestration itself.**

- **Supports (multi-agent composition, other domains)**: **#22** (Ni, multi-agent CAR-T system composing target-discovery + toxicity + molecular-design agents) and **#4** (Velazquez-Villarreal, multi-agent CRC clinico-genomic-SDOH ecosystem) implement the modular-orchestration pattern Foersch argues for — but in therapeutic design and precision-oncology ecosystems rather than pathology.
- **Supports (spatial-biology orchestration, adjacent)**: **#21** (Rognoni, end-to-end spatial-biology agent for MERSCOPE), **#28** (Seong, PortrAIgent co-scientist for spatial transcriptomics) — both implement the orchestrator-plus-specialist pattern inside the tissue-omics pipeline Foersch points to in his "spatial agent" slide.
- **Not addressed**: no poster in the 57 implements a *modular multi-agent pathology workflow* of the kind Foersch demonstrated on stage. The closest is **#LB450** (Van Alsten, AI-assisted pathology report abstraction) and **#2763** (Fried, LLM classification of pathology reports into ontological hierarchies) — both text-level, single-LLM extractors, not orchestrated multi-agent systems. His rare-tumor application (hematopathology, sarcoma, salivary gland) has zero direct analogues in the corpus.

### Thesis 2 — Open-source, on-premise agentic systems matter because hospital data cannot leave the institution

> "The cool thing about this system is that it's based on open-source models. You can actually run this on-premise if you don't want to upload your sensitive medical information to some cloud. This particular system has very low computing requirement, and it's a modular system that you can sort of add additional capabilities to."

**Corpus verdict: supported — with one direct analogue and several implicit.**

- **Direct support**: **#2750** (Levy) is the cleanest match — an **on-site peta-scale language model for MSI classification** from pathology reports, explicitly designed for institutional deployment where data cannot leave.
- **Indirect support**: **#2740** (Contreras Guzman, CAR-T clinical data on Google Cloud) is the *opposite* architecture and serves as a useful counterexample — it shows the cloud route is also being taken. **#30** (Theodorou) notes "adaptive" agentic systems for trial feasibility, suggesting private deployment.
- Zitnik's Q&A during the session echoes the same point: for institutions without private frontier-LLM inference endpoints, she swapped the backbone for an open-weight LLM installed at the hospital. The on-premise-vs-cloud axis is treated as live by every AT02 speaker, and the corpus reflects both choices without taking a side.

### Thesis 3 — Medical agents are vulnerable to prompt-injection and adversarial-image attacks that currently go unmitigated

> "If you have a generalist AI model that has not been hardened towards certain types of attack, you can show it a medical image, for example, a radiology image with a tumor on it, and it will have a certain diagnostic capability. But if you include, for example, a text statement […] but state that it looks completely healthy, then the model will completely forget or ignore better, ignore all the knowledge it has about radiology and state whatever is written in that prompt. […] We in pathology cannot stop ourself from scribbling on our tissue slides, and we have also seen that these incidental prompt injection attacks can highly influence a model's decision."

**Corpus verdict: not addressed.**

- Zero posters in the 57 evaluate prompt-injection robustness, adversarial-image resistance, or red-teaming of agentic medical systems.
- **#35** (Blenman, "Humans cannot live by AI alone") and **#34** (Haddad, veteran perception survey) are the only posters even loosely in the "safety" bucket, and both are human-factors rather than technical-attack papers.
- This is a clean stage-vs-corpus gap: an active research threat Foersch and his collaborators (Jan Klusmann / Jakob Nikolas Kather's lab) are publishing against has zero poster representation at AACR 2026. It is — consistent with Moor's Virtual-Cells analog on ED03 — a venue effect: security-of-medical-AI papers typically land at Nature Medicine, Nature Machine Intelligence, or security conferences, not the AACR poster hall.

---

## Marinka Zitnik — open AI co-scientists via Tool Universe

Zitnik framed the session's final talk around a shift from human-only science to human-AI co-science, with the practical claim that the blocker to general-purpose cancer-research agents is neither the LLM nor the data — it is the *tool layer*. Her lab released **Tool Universe** (a shared environment of ~2,000 scientific tools, adopted as an official Anthropic connector, with 200,000+ analyses across 113 countries Nov-25 → Feb-26) and **MedEA**, a co-scientist agent that planned a TME-response-prediction workflow, queried COMPASS (a concept-bottleneck transformer FM for TMEs), and ran causal-inference-adjusted emulated trials against a 5.4M-EHR dataset to generate novel drug-comorbidity-risk hypotheses.

### Thesis 1 — A shared tool environment is the right primitive; prompt engineering and parametric-memory-only LLMs hit a ceiling

> "We have done quite a bit of benchmarking and sensitivity analysis across all frontier models […]. And generally, what we found is that prompt engineering can only get you that far, and beyond that, the biggest gap is that of context generalization. […] Tool Universe specifies an AI tool interaction protocols, novel ways for AIs to communicate with each other in order to connect that LLM to 2,000 scientific tools that allow an LLM to now query experimental data, computational models, and scientific tools."

**Corpus verdict: supported in spirit; only one poster builds at the platform-tool-environment layer rather than the single-agent layer.**

- **Direct support (platform / shared infrastructure)**: **#5451** (Weinstein, Omicology — a comprehensive AI/LLM/NLP web resource for omics-literature navigation) is the corpus's closest analogue to a shared *research infrastructure* layer. It is narrower (literature navigation) and not an execution environment, but the mindset matches.
- **Implicit support (explicit tool-calling agents)**: **#16** (DrBioRight), **#18** (GP CoPilot), **#19** (GenerAItive), **#23** (ImmunoVerse-Chat), **#28** (PortrAIgent), **#31** (CHARLES) all implement LLMs-calling-tools architectures internally — but each is a vertically-owned stack, not a sharable tool environment.
- **Not addressed**: no poster ships an open, shared, cross-institutional tool registry of the Tool-Universe variety. The AACR 2026 corpus is doing Zitnik's Thesis 1 *implementation* pattern (tools + LLM + agent) but none have reached her *ecosystem* conclusion (one shared environment, many agents).

### Thesis 2 — Co-scientists should do real-world-evidence hypothesis generation with causal-inference adjustment on EHR data — not just answer questions

> "We connected this agent with a system of 5.4 million electronic health records and ask it to generate potential novel hypothesis about whether specific patient populations might be a higher or lower risk for adverse events or outcomes. […] We apply the novelty filter to filter out those predictions that correspond to what is already known […] of which we then have another auxiliary arm to the agent that sample hypothesis from that bank and then emulate clinical trials using real world evidence data […] with causal inference adjustments."

**Corpus verdict: partially supported — EHR-mining agents exist; causal-inference-grounded hypothesis generation does not.**

- **Supports (real-world-data mining and hypothesis surfacing)**: **#32** (Fort, real-world immune-related AE exploration), **#33** (Zhang, healthcare-system-scale multimodal whole-patient temporal FM), **#4** (Velazquez-Villarreal, real-time clinical-genomic-SDOH integration for CRC precision oncology), **#26** (Waqas, multi-agent temporal SDOH extraction), **#2762** (Lu, LLM-extracted immunotherapy toxicities with downstream OS analysis). Each of these mines real-world clinical text or structured data at population scale.
- **Not addressed (causal-inference-grounded)**: none of those posters layer causal-inference adjustment on top. **#4940** (Junho Lee, hybrid mathematical model of CAF emergent structures) is the only formal causal-modeling poster in the 57, and it is a wet-lab-adjacent dynamical-systems paper, not an agentic causal-inference system.
- The Zitnik-style combined pattern — **agent + RWD + causal adjustment + novelty filter** — has no single-poster analogue. Individual ingredients are present; the integrated workflow is not.

### Thesis 3 — Evaluation of agents requires blinded arena-style comparison + prospective lab-in-the-loop, not just retrospective benchmarks

> "There are a number of computational academic benchmarks […]. One common strategy for benchmarking these type of agents is with so-called arena style evaluations, where there is a notion of an arena in which there are a handful of agents competing with each other, and then producing, solving task, generating outputs, and then human experts evaluate them, and the identity of those agents who generated the outputs is blinded. […] I think there is beyond that also an opportunity to not only evaluate agents in retrospective manner, but also prospectively with lab-in-the-loop type of approach."

**Corpus verdict: not addressed.**

- Zero posters in the 57 report an arena-style blinded pairwise evaluation. **#3** (Thiriveedi, *evaluation of an agentic LLM chatbot for GENIE BPC*) is the nearest neighbor — but it is a single-system evaluation on a fixed task set, not a blinded arena.
- **#2739** (Desai, trial-matching LLM eval) is likewise single-system accuracy.
- No poster reports prospective lab-in-the-loop or active-learning-style evaluation of an agent.
- This mirrors the Bitterman Thesis-2 gap exactly: stage-side, the speakers agree evaluation is the critical unsolved problem; poster-side, three of 57 posters touch evaluation, none at the agentic-arena or prospective-loop level Zitnik describes.

---

## Cross-speaker convergences

Two themes recur across all three AT02 talks and are worth flagging before the thin-evidence list:

- **Evaluation is the bottleneck, not model performance.** Bitterman argues it explicitly (Thesis 2); Zitnik argues it explicitly (Thesis 3); Foersch argues it implicitly via his adversarial-attack examples (Thesis 3). The corpus ships 3 evaluation posters total (#3, #2739, #2747), none at the stepwise / arena / red-team level all three speakers call for.
- **Hospital-data locality and governance are real engineering constraints.** Bitterman's HIPAA-compliant OpenAI endpoint, Foersch's on-premise open-source stack, and Zitnik's swappable open-weight backbones all converge on the same operational point: production agentic AI must accommodate institutions that cannot send data off-site. The corpus partially addresses this with #2750 (on-site peta-scale LM), but there is no AACR 2026 poster on drift monitoring or post-deployment auditing for these on-premise systems.
- **Human-in-the-loop deferral as a reliability mechanism.** Bitterman's interactive-review UI (where the agent surfaces evidence text for human edit), Foersch's reasoning-trace pathologist-in-the-loop design, and Zitnik's explicit `I don't know` / defer-to-human behavior in MedEA all converge on the same reliability pattern: agents that abstain loudly are more trustworthy than agents that answer confidently. In the corpus, #31 CHARLES ("self-critical") and #35 Blenman ("Humans cannot live by AI alone") are the clearest matches to that framing; the extractor-family posters typically do not foreground abstention behavior.

## Thin-evidence flags — theses where the corpus is too thin to argue either way

Several AT02 claims are not testable against the 57-poster corpus because the relevant poster population is too small or absent. Flagged here rather than invented support:

- **Bitterman Thesis 1 (governance, drift monitoring, deployment infrastructure)**: 1 true deployment-science poster (#1393). Cannot conclude whether the field is closing or widening the gap.
- **Bitterman Thesis 2 (stepwise reasoning evaluation)**: 0 posters. Cannot evaluate.
- **Foersch Thesis 1 — the rare-tumor pathology-orchestration sub-claim (hematopathology, sarcoma, salivary gland)**: 0 posters. Cannot evaluate.
- **Foersch Thesis 3 (prompt injection, adversarial-image attacks, medical-agent red-teaming)**: 0 posters. Cannot evaluate.
- **Zitnik Thesis 1 — the shared-tool-registry sub-claim**: 1 partial-match (#5451 Omicology, literature-only). Too thin.
- **Zitnik Thesis 2 — the causal-inference-on-RWD sub-claim**: 0 direct posters.
- **Zitnik Thesis 3 (arena-style blinded + prospective lab-in-the-loop evaluation)**: 0 posters.

Of 9 theses extracted, **6 have essentially no corpus coverage.** All 6 cluster on the evaluation / governance / security axis, with a seventh (shared infrastructure) at the ecosystem layer.

---

## Closing synthesis — the stage-vs-corpus gap

The three AT02 speakers converge on a shared research program: **agentic AI systems that plan multi-step clinical and research workflows, call shared tools, and are evaluated prospectively through auditable step-by-step reasoning and red-teamed for security and drift**. The AACR 2026 agentic-AI poster corpus strongly supports the first half of that program — the "plan multi-step workflows" half. Roughly 29 of 57 posters (copilots + workflow agents + multi-agent systems) implement some variant of this pattern, with particularly dense clusters on adverse-event monitoring, trial matching, and clinical-note-to-structured-data pipelines that map 1-to-1 onto Bitterman's Thesis 3.

But the second half — **stepwise / arena / prospective evaluation, drift and governance monitoring, adversarial robustness, causal-inference-adjusted hypothesis generation, and shared cross-institutional tool ecosystems** — is almost entirely absent. Only 3 of 57 posters (#3, #2739, #2747) address evaluation at all, all at end-output accuracy level; 1 (#1393) addresses deployment / implementation science; 0 address agent security or drift monitoring.

The three AT02 speakers are 12-18 months ahead of the median AACR 2026 submitter on the evaluation, governance, and security axes. Some of this is venue effect — arena-style benchmarks and security red-teaming typically land at NeurIPS / ACL / Nature Medicine rather than the AACR poster hall — but some of it is substantive: the community is shipping agent *capabilities* (chatbots, extractors, pipelines) faster than it is shipping the *scaffolding* around them (audits, drift detectors, red teams, shared tool registries). Closing that scaffolding gap is the obvious opportunity for AACR 2027.

One way to read the gap more charitably: the AT02 speakers are operating one stack-layer above the poster corpus. Foersch's "modular multi-agent pathology system" is an *orchestrator* built on top of the single-purpose pathology-classification and pathology-report-extraction posters (#2750, #LB450, #2763) that AACR 2026 actually shipped. Zitnik's Tool Universe is a *registry* over exactly the kind of single-domain tools that #16 DrBioRight, #18 GP CoPilot, and #31 CHARLES each ship as vertically-owned stacks. Bitterman's drift-monitored clinical-workflow governance is an *operations layer* on top of the adverse-event / cohort-extraction capability posters (#30, #32, #2755, #2762) that are already in the corpus. The poster hall has the components; the stage has the next-level integration. In that reading, the 2027 move is less "invent new methods" and more "compose the 2026 methods into audited, shared, red-teamed ecosystems" — which is exactly the program all three speakers laid out.
