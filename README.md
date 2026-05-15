# Conference Vaults

Per-conference vaults for biomedical, bioinformatics, and AI/ML meetings — built dossiers, day digests, themes, and program-notes templates. **Successor to [conference-corpus](https://github.com/LiudengZhang/conference-corpus)** (archived).

The FM → Virtual Cells talk-prep and knowledge-base content moved to [fm-to-virtual-cells](https://github.com/LiudengZhang/fm-to-virtual-cells), which is password-gated. This repo holds only the per-conference vault content.

## Coverage

- **37 conferences** scaffolded across 2025–2026
- **13 vaults content-complete** · 24 scaffolded for live coverage at each meeting window
- **~109 deep dossiers** built (tools / trials / launches / talks / keynotes)

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve -a 127.0.0.1:8000
```

## Build + deploy

```bash
mkdocs build --strict
mkdocs gh-deploy --force
```

## Build scripts

- `scripts/build_site.py` — renders per-conference session pages and poster JSON from the per-meeting transcript dirs (`aacr-2026/`, `jpm-2026/`, `nextflow-2026/`).
- `scripts/conferences.py` — config for which conferences are wired through the builder.
- `scripts/test_build_tool_pages.py` — guardrail tests for the tool-page renderer.

## Per-conference data dirs

- `aacr-2026/` — raw transcripts + extracted poster data
- `jpm-2026/` — raw research notes
- `nextflow-2026/` — raw session transcripts
