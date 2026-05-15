# Conference Vaults

Per-conference vaults for biomedical, bioinformatics, and AI/ML meetings — built dossiers, day digests, themes, and program-notes templates. **Successor to [conference-corpus](https://github.com/LiudengZhang/conference-corpus)** (archived).

The FM → Virtual Cells talk-prep and knowledge-base content moved to [fm-to-virtual-cells](https://github.com/LiudengZhang/fm-to-virtual-cells), which is password-gated. This repo holds only the per-conference vault content.

## Coverage

- **37 conferences** scaffolded across 2025–2026
- **13 vaults content-complete** · 24 scaffolded for live coverage at each meeting window
- **~109 deep dossiers** built (tools / trials / launches / talks / keynotes)

## Site

Built and deployed via `mkdocs gh-deploy`. The deployed site is password-gated client-side using [mkdocs-encryptcontent-plugin](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin). Pass the password via the `SITE_PASSWORD` env var at build time:

```bash
SITE_PASSWORD='your-password' mkdocs build --strict
SITE_PASSWORD='your-password' mkdocs gh-deploy --force
```

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
SITE_PASSWORD='your-password' mkdocs serve -a 127.0.0.1:8000
```

## Build scripts

- `scripts/build_site.py` — renders per-conference session pages and poster JSON from the per-meeting transcript dirs (`aacr-2026/`, `jpm-2026/`, `nextflow-2026/`).
- `scripts/conferences.py` — config for which conferences are wired through the builder.
- `scripts/test_build_tool_pages.py` — guardrail tests for the tool-page renderer.

## Per-conference data dirs

- `aacr-2026/` — raw transcripts + extracted poster data
- `jpm-2026/` — raw research notes
- `nextflow-2026/` — raw session transcripts
