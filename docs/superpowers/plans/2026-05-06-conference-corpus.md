# Conference Corpus Refactor — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the single-conference `aacr-2026` repo into a multi-conference monorepo (`conference-corpus`) hosting AACR 2026, Nextflow Summit 2026, and a JPM 2026 placeholder, served as one MkDocs Material site with per-conference top-level tabs.

**Architecture:** Introduce `scripts/conferences.py` as the single source of truth, generalize `build_site.py` to iterate per-conference, move AACR data + docs under `aacr-2026/` and `docs/conferences/aacr-2026/` respectively, add Nextflow Summit + JPM siblings, rewrite the home page as a 3-card grid. Cloudflare Pages, Basic Auth, Hypothesis annotation, Tabulator wiring all unchanged.

**Tech Stack:** Python 3 (build), MkDocs Material, Tabulator.js, Hypothes.is, Cloudflare Pages.

**Spec:** `docs/superpowers/specs/2026-05-06-conference-corpus-design.md`

**Branch:** `refactor/conference-corpus` (already created, off `tools/dossiers`)

**Validation harness:** This refactor has no `tests/` directory. Validation per task is:
1. `python scripts/build_site.py && mkdocs build --strict` succeeds (modulo the ~49 pre-existing strict warnings captured in Task 1's baseline).
2. SHA-256 of regenerated assets match baseline (where the task asserts "no behavior change") OR diff matches the expected new layout (where the task is intentionally moving things).
3. Visual smoke check: open the local preview (`mkdocs serve`) and click 3 representative pages.

**Git identity for commits:** Use `git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit ...` for every commit step in this plan.

---

## File structure

**New files:**
- `scripts/conferences.py` — `CONFERENCES` list (single source of truth)
- `aacr-2026/transcripts/...` — moved from `transcripts/`
- `aacr-2026/raw/...` — moved from `raw/`
- `nextflow-2026/transcripts/sessions/2026-04-30-nextflow-summit-day-1-am.md` — moved from `_Extra/Nextflow/transcript_day_1_before_lunch.md`
- `nextflow-2026/transcripts/sessions/2026-04-30-nextflow-summit-day-1-pm.md` — moved from `_Extra/Nextflow/transcript_day_1_after_lunch.md`
- `nextflow-2026/transcripts/sessions/2026-05-01-nextflow-summit-day-2.md` — moved from `_Extra/Nextflow/transcript_day_2.md`
- `jpm-2026/README.md` — placeholder
- `docs/conferences/aacr-2026/index.md` — moved from current `docs/index.md` content
- `docs/conferences/aacr-2026/topics/...` — moved from `docs/topics/`
- `docs/conferences/aacr-2026/sessions/...` — moved from `docs/sessions/`
- `docs/conferences/nextflow-2026/index.md` — new conference overview
- `docs/conferences/nextflow-2026/sessions/<slug>.md` — generated copies of the 3 Nextflow transcripts with admonition wrapper
- `docs/conferences/nextflow-2026/sessions/index.md` — generated index of the 3
- `docs/conferences/jpm-2026/index.md` — new placeholder page
- `docs/index.md` — rewritten as 3-card home

**Modified files:**
- `scripts/build_site.py` — generalized to accept `conf` per function
- `mkdocs.yml` — nav restructured with one tab per conference
- `README.md` — rewritten as `conference-corpus` overview
- `docs/topics/*/index.md` (after move) — relative paths re-depthed for `data-src` and `../sessions/...` links
- `docs/topics/bioinfo-tools/index.md` (after move) — same depth fix on session-list links

**Unchanged:**
- `functions/_middleware.js` (Basic Auth)
- `docs/javascripts/*.js` (Tabulator wiring; data-src URLs come from page HTML, not from JS)
- `docs/stylesheets/*.css`
- `docs/notes/extraction.md`, `docs/notes/caveats.md`
- `requirements.txt`, `.gitignore`

---

## Task 1: Pre-flight baseline

**Why:** Capture the current build's warning count, the list of generated files, and SHA-256 checksums so later tasks can prove "no behavior change" precisely. Without a baseline, "the build still works" is unfalsifiable.

**Files:**
- Create: `_baseline/warnings.txt`, `_baseline/checksums.txt`, `_baseline/file-list.txt` (gitignored — see step below)
- Modify: `.gitignore` — add `_baseline/`

- [ ] **Step 1: Add `_baseline/` to .gitignore**

Append to `/Users/lzhang34/Desktop/AACR/.gitignore`:

```
_baseline/
```

- [ ] **Step 2: Run the current build and capture warnings**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdir -p _baseline
python scripts/build_site.py 2>&1 | tee _baseline/build.log
mkdocs build --strict 2>&1 | tee _baseline/mkdocs.log; true
grep -cE "WARNING|ERROR" _baseline/mkdocs.log > _baseline/warnings.txt || true
cat _baseline/warnings.txt
```

Expected: ~49 (per spec). Record the exact number. `mkdocs build --strict` may exit non-zero if there are warnings under `--strict`; that's why we use `; true` and grep separately.

- [ ] **Step 3: Capture file list + checksums of generated assets**

```bash
cd /Users/lzhang34/Desktop/AACR
find docs/assets docs/sessions docs/javascripts/tabulator.min.js docs/stylesheets/tabulator.min.css \
  -type f 2>/dev/null | sort > _baseline/file-list.txt
xargs -a _baseline/file-list.txt shasum -a 256 > _baseline/checksums.txt
wc -l _baseline/file-list.txt _baseline/checksums.txt
```

Expected: file-list and checksums both have N lines where N is the number of generated files (~30-50).

- [ ] **Step 4: Verify branch state**

```bash
cd /Users/lzhang34/Desktop/AACR
git status
git log --oneline -5
git rev-parse --abbrev-ref HEAD
```

Expected: branch is `refactor/conference-corpus`, `_baseline/` is untracked, recent commits include `715077b spec: resolve 4 open questions ...`.

- [ ] **Step 5: Commit the .gitignore update**

```bash
cd /Users/lzhang34/Desktop/AACR
git add .gitignore
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "chore: ignore _baseline/ snapshot dir for refactor validation

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Add `scripts/conferences.py` config (no behavior change)

**Why:** Create the single source of truth for conference metadata. AACR entry uses empty `data_dir` and `docs_dir="docs"` so existing path resolution still works; this lets later tasks flip the strings to migrate paths without touching code structure.

**Files:**
- Create: `scripts/conferences.py`
- Modify: `scripts/build_site.py:1-30` (import the config; do not iterate yet)

- [ ] **Step 1: Create `scripts/conferences.py`**

Write this file at `/Users/lzhang34/Desktop/AACR/scripts/conferences.py`:

```python
"""Conference registry — single source of truth for the multi-conference build.

Each entry describes one conference. `build_site.py` iterates this list and
dispatches per-conference work. Path fields are repo-relative.

Initial AACR `data_dir` and `docs_dir` mirror the pre-refactor layout
(`transcripts/` at repo root, `docs/topics/...`); they flip to
`aacr-2026/` and `docs/conferences/aacr-2026/` in later tasks of the
refactor when the actual files move.
"""

CONFERENCES = [
    {
        "slug": "aacr-2026",
        "label": "AACR 2026",
        "data_dir": "",                              # repo root; becomes "aacr-2026" in Task 4
        "docs_dir": "docs",                          # becomes "docs/conferences/aacr-2026" in Task 5
        "topics": [
            ("agentic-ai", "Agentic AI"),
            ("single-cell-spatial-omics", "Single-Cell & Spatial Omics"),
            ("virtual-cells", "Virtual Cells"),
            ("bioinfo-tools", "Bioinfo / Comp Bio / AI Methods"),
            ("clinical-trials", "Clinical Trials"),
        ],
        "has_posters": True,
        "has_tools_index": True,
        "session_source": "txt-transcripts",          # build_session_pages reads .txt from full-sessions/
    },
    {
        "slug": "nextflow-2026",
        "label": "Nextflow Summit 2026",
        "data_dir": "nextflow-2026",
        "docs_dir": "docs/conferences/nextflow-2026",
        "topics": [],
        "has_posters": False,
        "has_tools_index": False,
        "session_source": "md-transcripts",           # session .md files copied with admonition wrapper
    },
    {
        "slug": "jpm-2026",
        "label": "JPM 2026",
        "data_dir": "jpm-2026",
        "docs_dir": "docs/conferences/jpm-2026",
        "topics": [],
        "has_posters": False,
        "has_tools_index": False,
        "placeholder_only": True,
    },
]
```

- [ ] **Step 2: Import `CONFERENCES` in `build_site.py`**

Edit `/Users/lzhang34/Desktop/AACR/scripts/build_site.py`. After the existing `from collections import defaultdict` line (line 23), add:

```python
from conferences import CONFERENCES
```

(Note: `scripts/` doesn't have an `__init__.py`; Python finds sibling modules because `build_site.py` is run directly with `python scripts/build_site.py`, which adds `scripts/` to sys.path implicitly when invoked as `python -m` would — but for `python scripts/build_site.py`, the script's directory is added to sys.path, so a sibling import works.)

- [ ] **Step 3: Verify the import works without breaking the build**

```bash
cd /Users/lzhang34/Desktop/AACR
python scripts/build_site.py > /tmp/build2.log 2>&1
diff <(grep -E "→|warning|error" _baseline/build.log) <(grep -E "→|warning|error" /tmp/build2.log)
```

Expected: empty diff (build output unchanged).

- [ ] **Step 4: Verify generated asset checksums unchanged**

```bash
cd /Users/lzhang34/Desktop/AACR
xargs -a _baseline/file-list.txt shasum -a 256 > /tmp/checksums2.txt
diff _baseline/checksums.txt /tmp/checksums2.txt
```

Expected: empty diff.

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add scripts/conferences.py scripts/build_site.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "build: add CONFERENCES registry (no behavior change yet)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: Thread `conf` through build_site.py functions

**Why:** Make every path computation in `build_site.py` go through the `conf` dict so that flipping `data_dir`/`docs_dir` in later tasks is sufficient to migrate paths without touching function bodies. AACR entry's empty `data_dir="" ` plus `docs_dir="docs"` keeps the resolved paths bit-identical to the current hardcoded layout.

**Files:**
- Modify: `scripts/build_site.py` (most functions gain a `conf` parameter)

- [ ] **Step 1: Add path-resolution helpers near the top of `build_site.py`**

In `/Users/lzhang34/Desktop/AACR/scripts/build_site.py`, after the `ROOT = Path(...)` line (line 25) and before the existing `TRANSCRIPTS = ROOT / "transcripts"` line, insert these helpers and remove the four hardcoded constants. Replace lines 25-30 with:

```python
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
JS_DIR = DOCS / "javascripts"


def data_path(conf: dict, *parts: str) -> Path:
    """Resolve a path under a conference's data_dir (transcripts/, raw/)."""
    base = ROOT / conf["data_dir"] if conf["data_dir"] else ROOT
    return base.joinpath(*parts)


def docs_path(conf: dict, *parts: str) -> Path:
    """Resolve a path under a conference's docs_dir (topics/, sessions/)."""
    return ROOT.joinpath(conf["docs_dir"], *parts)


def conf_assets_path(conf: dict, *parts: str) -> Path:
    """Resolve a path under docs/assets/<conf>/ with optional sub-parts."""
    base = DOCS / "assets" / conf["slug"]
    return base.joinpath(*parts) if parts else base


def legacy_assets_path(*parts: str) -> Path:
    """Pre-refactor flat docs/assets/ layout. AACR uses this until Task 5
    flips poster JSON output to the slug-namespaced layout. Removed then."""
    base = DOCS / "assets"
    return base.joinpath(*parts) if parts else base
```

(Remove the old `TRANSCRIPTS = ROOT / "transcripts"`, `ASSETS = DOCS / "assets"`, `SESSIONS = DOCS / "sessions"` constants — they're replaced by the helpers above.)

- [ ] **Step 2: Refactor `load_corpus()` → `load_corpus(conf)`**

Replace the existing `load_corpus` function body (lines 86-134 of pre-edit `build_site.py`) with:

```python
def load_corpus(conf: dict) -> dict:
    """Load every poster JSONL and unique session .txt for the given conference.

    Returns: {"posters": [{"Id","Title","Abstract","_topic"}, ...],
              "sessions": [{"stem","text","_topics":[...]}, ...]}
    """
    posters_by_id: dict[str, dict] = {}
    for topic_slug, _ in conf["topics"]:
        jsonl = data_path(conf, "transcripts", topic_slug, "posters", "abstracts.jsonl")
        if not jsonl.exists():
            continue
        with jsonl.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                p = json.loads(line)
                pid = p.get("Id")
                if not pid:
                    continue
                if pid in posters_by_id:
                    posters_by_id[pid].setdefault("_topics", []).append(topic_slug)
                else:
                    p["_topic"] = topic_slug
                    p["_topics"] = [topic_slug]
                    posters_by_id[pid] = p

    sessions_by_stem: dict[str, dict] = {}
    for topic_slug, _ in conf["topics"]:
        fs_dir = data_path(conf, "transcripts", topic_slug, "full-sessions")
        if not fs_dir.exists():
            continue
        for txt in sorted(fs_dir.glob("*.txt")):
            stem = txt.stem
            if stem in sessions_by_stem:
                sessions_by_stem[stem]["_topics"].append(topic_slug)
                continue
            text = resolve_symlink(txt).read_text()
            sessions_by_stem[stem] = {
                "stem": stem,
                "text": text,
                "_topics": [topic_slug],
            }

    return {
        "posters": list(posters_by_id.values()),
        "sessions": list(sessions_by_stem.values()),
    }
```

- [ ] **Step 3: Refactor `survey_tools()` → `survey_tools(conf)`**

Update the function signature and the call to `load_corpus`:

```python
def survey_tools(conf: dict) -> dict:
    """Compute mention counts for every tool in TOOLS and report which pass the gate."""
    corpus = load_corpus(conf)
    survivors, dropped = [], []
    for name, slug, family, aliases in TOOLS:
        hits = scan_mentions(corpus, aliases)
        np_, ns_ = len(hits["posters"]), len(hits["sessions"])
        total = np_ + ns_
        row = {"name": name, "slug": slug, "family": family,
               "n_posters": np_, "n_sessions": ns_, "total": total,
               "hits": hits}
        (survivors if total >= INCLUSION_GATE else dropped).append(row)

    print(f"\n{'Tool':<24} {'Family':<14} {'Posters':>8} {'Sessions':>9} {'Total':>6}")
    print("-" * 65)
    for r in sorted(survivors, key=lambda x: -x["total"]):
        print(f"{r['name']:<24} {r['family']:<14} {r['n_posters']:>8} {r['n_sessions']:>9} {r['total']:>6}  ✓")
    for r in sorted(dropped, key=lambda x: -x["total"]):
        print(f"{r['name']:<24} {r['family']:<14} {r['n_posters']:>8} {r['n_sessions']:>9} {r['total']:>6}  dropped")
    print(f"\n{len(survivors)} survivors, {len(dropped)} dropped (gate={INCLUSION_GATE})")
    return {"survivors": survivors, "dropped": dropped}
```

- [ ] **Step 4: Refactor `build_tool_pages()` → `build_tool_pages(conf)`**

Replace the function body to take `conf` and resolve paths through the helpers. The tools dossier dir lives under each conference's `docs_dir`:

```python
def build_tool_pages(conf: dict):
    """Survey the corpus, gate, then write/refresh dossier mention blocks
    and emit the matrix + mentions JSON for the index page."""
    if not conf.get("has_tools_index"):
        return
    tools_dir = docs_path(conf, "topics", "bioinfo-tools", "tools")
    tools_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = legacy_assets_path("bioinfo-tools")  # flipped to conf_assets_path in Task 5
    assets_dir.mkdir(parents=True, exist_ok=True)

    survey = survey_tools(conf)
    survivors = survey["survivors"]
    dropped = survey["dropped"]

    matrix_rows = []
    mentions_dump = {}
    metadata_re = re.compile(r"^\*\*([\w/ ]+?):\*\*\s*(.+)$", re.MULTILINE)

    for r in survivors:
        slug, name, family, hits = r["slug"], r["name"], r["family"], r["hits"]
        page = tools_dir / f"{slug}.md"

        topics_for_tool = set()
        for h in hits["posters"]:
            topics_for_tool.update(h["_topics"])
        for h in hits["sessions"]:
            topics_for_tool.update(h["_topics"])
        topics_for_tool.discard("bioinfo-tools")
        also_in = sorted(topics_for_tool)

        if not page.exists():
            page.write_text(stub_dossier(name, slug, family, also_in))
            print(f"→ scaffolded {page.relative_to(ROOT)}")

        md = page.read_text()
        new_block = render_mentions_block(name, hits)
        md = inject_mentions_block(md, new_block)
        page.write_text(md)

        meta = dict(metadata_re.findall(md))
        matrix_rows.append({
            "tool": name,
            "slug": slug,
            "family": family,
            "modality": meta.get("Modality", "").strip(),
            "released": meta.get("Released", "").strip(),
            "license": meta.get("License", "").strip(),
            "n_posters": r["n_posters"],
            "n_sessions": r["n_sessions"],
            "also_in": also_in,
        })
        mentions_dump[slug] = hits

    (assets_dir / "tool-matrix.json").write_text(
        json.dumps(matrix_rows, ensure_ascii=False, indent=2)
    )
    (assets_dir / "tool-mentions.json").write_text(
        json.dumps(mentions_dump, ensure_ascii=False)
    )
    print(f"→ {len(survivors)} dossiers + tool-matrix.json + tool-mentions.json")
    if dropped:
        print(f"  dropped (n<{INCLUSION_GATE}): " + ", ".join(
            f"{d['name']} (n={d['total']})" for d in dropped
        ))
```

- [ ] **Step 5: Refactor `build_poster_json` and `build_session_pages` to take `conf`**

Replace `build_poster_json(topic_slug)` with:

```python
def build_poster_json(conf: dict, topic_slug: str) -> int:
    src = data_path(conf, "transcripts", topic_slug, "posters", "abstracts.jsonl")
    if not src.exists():
        return 0
    out = legacy_assets_path(f"{topic_slug}-posters.json")  # flipped to conf_assets_path in Task 5
    rows = []
    with src.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = json.loads(line)
            start = (p.get("Start") or "").strip()
            day = start.split(" ")[0] if start else ""
            rows.append({
                "num": p.get("PresentationNumber") or p.get("Id") or "",
                "title": p.get("Title", "") or "",
                "session": p.get("SessionTitle", "") or "",
                "day": day,
                "presenter": p.get("PresenterDisplayName", "") or "",
                "activity": p.get("Activity", "") or "",
                "authors": p.get("AuthorBlock", "") or "",
                "abstract": p.get("Abstract", "") or "",
                "start": start,
                "player_url": p.get("PlayerUrl", "") or "",
            })
    out.write_text(json.dumps(rows, ensure_ascii=False))
    print(f"→ {out.relative_to(ROOT)}: {len(rows)} posters")
    return len(rows)
```

Replace `build_session_pages()` with:

```python
def build_session_pages(conf: dict):
    """Create one MD page per unique transcript file, tracking which topics link to it."""
    if conf.get("session_source") != "txt-transcripts":
        return 0
    sessions_out = docs_path(conf, "sessions")
    sessions_out.mkdir(parents=True, exist_ok=True)

    by_resolved = defaultdict(list)
    for topic_slug, _ in conf["topics"]:
        fs_dir = data_path(conf, "transcripts", topic_slug, "full-sessions")
        if not fs_dir.exists():
            continue
        for txt in sorted(fs_dir.glob("*.txt")):
            resolved = resolve_symlink(txt)
            by_resolved[(resolved, txt.stem)].append(topic_slug)

    written = 0
    index_entries_by_topic = defaultdict(list)

    for (resolved, stem), topics_in in sorted(by_resolved.items(), key=lambda x: x[0][1]):
        body = read_transcript_text(resolved)
        word_count = len(body.split())

        primary_topic = None
        for ts in topics_in:
            candidate = data_path(conf, "transcripts", ts, "full-sessions", f"{stem}.txt")
            if candidate.exists() and not candidate.is_symlink():
                primary_topic = ts
                break
        if not primary_topic:
            primary_topic = topics_in[0]

        cross_topics = ", ".join(sorted(set(topics_in)))
        md = f"""# {stem}

**Date:** {stem.split('-')[0]}-{stem.split('-')[1]}-{stem.split('-')[2]}
**Primary topic:** `{primary_topic}`
**Cross-referenced from:** {cross_topics}
**Word count:** ~{word_count:,}

!!! note "Auto-generated captions"
    This transcript is Vimeo auto-generated English. Expect misheard names and technical terms. Use the ripgrep/search approach for exact quotes.

<div class="transcript-body">

{body}

</div>
"""
        (sessions_out / f"{stem}.md").write_text(md)
        written += 1
        for ts in topics_in:
            index_entries_by_topic[ts].append((stem, word_count, primary_topic))

    idx_lines = [
        "# Session Transcripts",
        "",
        f"All {written} unique session transcripts from {conf['label']}, grouped by topic. Cross-topic symlinks mean the same video may appear under multiple topics — each transcript has one canonical page here.",
        "",
    ]
    for topic_slug, topic_label in conf["topics"]:
        entries = index_entries_by_topic.get(topic_slug, [])
        if not entries:
            continue
        idx_lines.append(f"## {topic_label}")
        idx_lines.append("")
        idx_lines.append("| Session | Words | Primary |")
        idx_lines.append("|---|---|---|")
        for stem, wc, primary in sorted(entries):
            is_primary = "✓" if primary == topic_slug else ""
            idx_lines.append(f"| [{stem}]({stem}.md) | ~{wc:,} | {is_primary} |")
        idx_lines.append("")
    (sessions_out / "index.md").write_text("\n".join(idx_lines))
    print(f"→ {written} session pages + sessions/index.md for {conf['slug']}")
    return written
```

- [ ] **Step 6: Refactor `ensure_dirs()` and `main()` to iterate CONFERENCES**

Replace `ensure_dirs()`:

```python
def ensure_dirs(conf: dict):
    legacy_assets_path().mkdir(parents=True, exist_ok=True)
    docs_path(conf, "sessions").mkdir(parents=True, exist_ok=True)
    JS_DIR.mkdir(parents=True, exist_ok=True)
```

Replace `main()`:

```python
def main():
    if "--survey" in sys.argv:
        # --survey only makes sense for conferences with tools indices
        for conf in CONFERENCES:
            if conf.get("has_tools_index"):
                survey_tools(conf)
        return
    vendor_tabulator()
    total_posters = 0
    total_sessions = 0
    for conf in CONFERENCES:
        if conf.get("placeholder_only"):
            continue
        ensure_dirs(conf)
        if conf.get("has_posters"):
            for topic_slug, _ in conf["topics"]:
                total_posters += build_poster_json(conf, topic_slug)
        if conf.get("session_source") == "txt-transcripts":
            total_sessions += build_session_pages(conf)
        if conf.get("has_tools_index"):
            build_tool_pages(conf)
    print(f"\nBuild preprocessing complete.")
    print(f"  Posters  : {total_posters:>5} total")
    print(f"  Sessions : {total_sessions:>5} unique transcript pages")
```

- [ ] **Step 7: Run the build, compare to baseline**

```bash
cd /Users/lzhang34/Desktop/AACR
python scripts/build_site.py > /tmp/build3.log 2>&1
xargs -a _baseline/file-list.txt shasum -a 256 > /tmp/checksums3.txt
diff _baseline/checksums.txt /tmp/checksums3.txt
mkdocs build --strict 2>&1 | tee /tmp/mkdocs3.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs3.log
```

Expected: empty diff on checksums; warning count matches baseline.

- [ ] **Step 8: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add scripts/build_site.py
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "build: thread conf dict through build_site.py path resolution

Output paths and behavior unchanged. Sets up conf-driven path migration
in subsequent tasks.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: Move AACR data into `aacr-2026/`

**Why:** Physically relocate `transcripts/` and `raw/` under `aacr-2026/` so the AACR conference owns its data dir. Done as `git mv` so history is preserved. The conf flip from `data_dir=""` to `data_dir="aacr-2026"` is the only code change.

**Files:**
- Move (git): `transcripts/` → `aacr-2026/transcripts/`
- Move (git): `raw/` → `aacr-2026/raw/`
- Modify: `scripts/conferences.py` (one line change to AACR `data_dir`)

- [ ] **Step 1: Move `transcripts/` and `raw/`**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdir -p aacr-2026
git mv transcripts aacr-2026/transcripts
git mv raw aacr-2026/raw
git status
```

Expected: Lots of "renamed" entries under `aacr-2026/`.

- [ ] **Step 2: Update CONFERENCES AACR `data_dir`**

In `/Users/lzhang34/Desktop/AACR/scripts/conferences.py`, change the AACR entry:

```python
        "data_dir": "aacr-2026",                     # was: ""
```

- [ ] **Step 3: Run build, verify checksums match baseline**

```bash
cd /Users/lzhang34/Desktop/AACR
python scripts/build_site.py > /tmp/build4.log 2>&1
xargs -a _baseline/file-list.txt shasum -a 256 > /tmp/checksums4.txt
diff _baseline/checksums.txt /tmp/checksums4.txt
```

Expected: empty diff. The data move is invisible to generated output because resolution flows through `data_path(conf, ...)`.

- [ ] **Step 4: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add scripts/conferences.py aacr-2026
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "refactor: move transcripts/ and raw/ under aacr-2026/

Generated output is bit-identical (verified against pre-refactor checksums).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: Move AACR docs into `docs/conferences/aacr-2026/` and switch poster JSON layout

**Why:** Physical move of `docs/topics/`, `docs/sessions/`, and content of `docs/index.md` to the conference subtree. Simultaneously flip poster-JSON output from `docs/assets/<topic>-posters.json` to `docs/assets/aacr-2026/posters/<topic>.json` (spec calls for slug-namespaced assets), and re-depth all relative paths inside topic indexes and the bioinfo-tools session list to match the deeper location. These are bundled into one task because the relative-path math only resolves consistently if move + path-flip happen together.

**Files:**
- Move (git): `docs/topics/` → `docs/conferences/aacr-2026/topics/`
- Move (git): `docs/sessions/` → `docs/conferences/aacr-2026/sessions/`
- Modify: `docs/index.md` — content moved to `docs/conferences/aacr-2026/index.md`; root `index.md` becomes a temporary one-line stub (rewritten in Task 11)
- Modify: `scripts/conferences.py` (AACR `docs_dir`)
- Modify: `scripts/build_site.py` — flip `legacy_assets_path` calls to `conf_assets_path("posters", ...)` and `conf_assets_path("bioinfo-tools", ...)`
- Modify: `docs/conferences/aacr-2026/topics/<topic>/index.md` — re-depth `data-src` and `../sessions/` URLs (5 files: agentic-ai, single-cell-spatial-omics, virtual-cells, bioinfo-tools, clinical-trials)
- Modify: `docs/conferences/aacr-2026/topics/bioinfo-tools/index.md` — re-depth session-list `../sessions/` links (12 entries)
- Modify: `mkdocs.yml` — re-prefix every nav path with `conferences/aacr-2026/`
- Update: `_baseline/checksums.txt` (paths/contents have shifted by design; will re-baseline after this task)

- [ ] **Step 1: Move docs subdirectories**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdir -p docs/conferences/aacr-2026
git mv docs/topics docs/conferences/aacr-2026/topics
git mv docs/sessions docs/conferences/aacr-2026/sessions
git status
```

Expected: many "renamed" entries.

- [ ] **Step 2: Move `docs/index.md` content into `docs/conferences/aacr-2026/index.md`**

```bash
cd /Users/lzhang34/Desktop/AACR
git mv docs/index.md docs/conferences/aacr-2026/index.md
```

- [ ] **Step 3: Add a temporary root `docs/index.md` stub**

Write to `/Users/lzhang34/Desktop/AACR/docs/index.md`:

```markdown
# Conference Corpus

Site is being restructured for multi-conference hosting. See:

- [AACR 2026](conferences/aacr-2026/)

(Home page rewrite is Task 11 of the conference-corpus refactor.)
```

This stub keeps `mkdocs build` from failing while the real home page is deferred to Task 11.

- [ ] **Step 4: Update CONFERENCES AACR `docs_dir`**

In `/Users/lzhang34/Desktop/AACR/scripts/conferences.py`, change the AACR entry:

```python
        "docs_dir": "docs/conferences/aacr-2026",    # was: "docs"
```

- [ ] **Step 5: Switch poster JSON output to slug-namespaced layout**

In `/Users/lzhang34/Desktop/AACR/scripts/build_site.py`:

Replace the line in `build_poster_json` that reads:

```python
    out = legacy_assets_path(f"{topic_slug}-posters.json")  # flipped to conf_assets_path in Task 5
```

with:

```python
    out = conf_assets_path(conf, "posters", f"{topic_slug}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
```

In `build_tool_pages`, replace:

```python
    assets_dir = legacy_assets_path("bioinfo-tools")  # flipped to conf_assets_path in Task 5
```

with:

```python
    assets_dir = conf_assets_path(conf, "bioinfo-tools")
```

Delete the `legacy_assets_path` helper from `build_site.py` — nothing references it after this task.

- [ ] **Step 6: Re-depth `data-src` and `../sessions/` URLs in topic indexes**

For each of the 5 topic index files (`agentic-ai`, `single-cell-spatial-omics`, `virtual-cells`, `bioinfo-tools`, `clinical-trials`), the relative paths shift like this:

- `data-src="../../assets/<topic>-posters.json"` → `data-src="../../../../assets/aacr-2026/posters/<topic>.json"`
- session links of the form `../sessions/<slug>.md` → `../../sessions/<slug>.md`

Run this sed-style update via individual Edit tool calls (one per file, exact strings). Concrete edits:

For `/Users/lzhang34/Desktop/AACR/docs/conferences/aacr-2026/topics/agentic-ai/index.md`:
- Replace every `(../sessions/` with `(../../sessions/`
- Replace `data-src="../../assets/agentic-ai-posters.json"` with `data-src="../../../../assets/aacr-2026/posters/agentic-ai.json"`

For `/Users/lzhang34/Desktop/AACR/docs/conferences/aacr-2026/topics/single-cell-spatial-omics/index.md`:
- Replace every `(../sessions/` with `(../../sessions/`
- Replace `data-src="../../assets/single-cell-spatial-omics-posters.json"` with `data-src="../../../../assets/aacr-2026/posters/single-cell-spatial-omics.json"`

For `/Users/lzhang34/Desktop/AACR/docs/conferences/aacr-2026/topics/virtual-cells/index.md`:
- Replace every `(../sessions/` with `(../../sessions/`
- Replace `data-src="../../assets/virtual-cells-posters.json"` with `data-src="../../../../assets/aacr-2026/posters/virtual-cells.json"`

For `/Users/lzhang34/Desktop/AACR/docs/conferences/aacr-2026/topics/bioinfo-tools/index.md`:
- Replace every `(../sessions/` with `(../../sessions/`
- Replace `data-src="../../assets/bioinfo-tools-posters.json"` with `data-src="../../../../assets/aacr-2026/posters/bioinfo-tools.json"`

For `/Users/lzhang34/Desktop/AACR/docs/conferences/aacr-2026/topics/clinical-trials/index.md`:
- Replace every `(../sessions/` with `(../../sessions/`
- Replace `data-src="../../assets/clinical-trials-posters.json"` with `data-src="../../../../assets/aacr-2026/posters/clinical-trials.json"`

(Tool dossier pages under `docs/conferences/aacr-2026/topics/bioinfo-tools/tools/<tool>.md` use `../../../sessions/` which already resolves correctly after the move because the depth from a tool page to its conference's `sessions/` is preserved. **No edit needed** for tool pages, but verify by spot-checking one: `docs/conferences/aacr-2026/topics/bioinfo-tools/tools/cell2location.md` should still link via `../../../sessions/`.)

- [ ] **Step 7: Update `mkdocs.yml` nav to re-prefix all AACR paths**

Replace the existing nav block in `/Users/lzhang34/Desktop/AACR/mkdocs.yml` (lines 63-99) with:

```yaml
nav:
  - Home: index.md
  - AACR 2026:
    - Overview: conferences/aacr-2026/index.md
    - Agentic AI:
      - Overview: conferences/aacr-2026/topics/agentic-ai/index.md
      - Landscape: conferences/aacr-2026/topics/agentic-ai/landscape.md
      - Synthesis — AT02 vs corpus: conferences/aacr-2026/topics/agentic-ai/synthesis-at02-vs-corpus.md
    - Single-Cell & Spatial Omics:
      - Overview: conferences/aacr-2026/topics/single-cell-spatial-omics/index.md
      - Landscape: conferences/aacr-2026/topics/single-cell-spatial-omics/landscape.md
      - Synthesis — spatial eating scRNA: conferences/aacr-2026/topics/single-cell-spatial-omics/synthesis-spatial-eating-sc.md
    - Virtual Cells:
      - Overview: conferences/aacr-2026/topics/virtual-cells/index.md
      - Landscape: conferences/aacr-2026/topics/virtual-cells/landscape.md
      - Synthesis — ED03 vs corpus: conferences/aacr-2026/topics/virtual-cells/synthesis-ed03-vs-corpus.md
    - Bioinfo / Comp Bio / AI Methods:
      - Overview: conferences/aacr-2026/topics/bioinfo-tools/index.md
      - Landscape: conferences/aacr-2026/topics/bioinfo-tools/landscape.md
      - Synthesis — FM pathology traction: conferences/aacr-2026/topics/bioinfo-tools/synthesis-fm-pathology-traction.md
      - Tools:
        - Index: conferences/aacr-2026/topics/bioinfo-tools/tools/index.md
        - CHIEF: conferences/aacr-2026/topics/bioinfo-tools/tools/chief.md
        - Prov-GigaPath: conferences/aacr-2026/topics/bioinfo-tools/tools/prov-gigapath.md
        - UNI / UNI2: conferences/aacr-2026/topics/bioinfo-tools/tools/uni.md
        - Geneformer: conferences/aacr-2026/topics/bioinfo-tools/tools/geneformer.md
        - scGPT: conferences/aacr-2026/topics/bioinfo-tools/tools/scgpt.md
        - Cell2Location: conferences/aacr-2026/topics/bioinfo-tools/tools/cell2location.md
    - Clinical Trials:
      - Overview: conferences/aacr-2026/topics/clinical-trials/index.md
      - Landscape: conferences/aacr-2026/topics/clinical-trials/landscape.md
      - Synthesis — trial-design methodology: conferences/aacr-2026/topics/clinical-trials/synthesis-trial-design-methodology.md
    - All AACR sessions: conferences/aacr-2026/sessions/index.md
  - Notes:
    - Extraction method: notes/extraction.md
    - Caveats: notes/caveats.md
```

(Nextflow and JPM tabs come in Tasks 8 and 9.)

- [ ] **Step 8: Build and verify**

```bash
cd /Users/lzhang34/Desktop/AACR
# Remove stale flat-layout poster JSONs from before the slug-namespaced switch
rm -f docs/assets/agentic-ai-posters.json docs/assets/single-cell-spatial-omics-posters.json \
      docs/assets/virtual-cells-posters.json docs/assets/bioinfo-tools-posters.json \
      docs/assets/clinical-trials-posters.json
python scripts/build_site.py > /tmp/build5.log 2>&1
ls docs/assets/aacr-2026/posters/
mkdocs build --strict 2>&1 | tee /tmp/mkdocs5.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs5.log
```

Expected:
- 5 poster JSONs at `docs/assets/aacr-2026/posters/{agentic-ai,single-cell-spatial-omics,virtual-cells,bioinfo-tools,clinical-trials}.json`
- Warning count is the baseline ±1-2 (the docs-tree relocation may shift a few cross-link warnings, which is fine; substantial regression would mean a path is wrong)

- [ ] **Step 9: Smoke check via local preview**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdocs serve -a 127.0.0.1:8765 &
SERVE_PID=$!
sleep 3
curl -s http://127.0.0.1:8765/conferences/aacr-2026/topics/agentic-ai/ | grep -c "poster-table"
curl -s http://127.0.0.1:8765/conferences/aacr-2026/sessions/2026-04-20-am-ai-revolution-in-cancer-research/ | head -c 200
curl -s http://127.0.0.1:8765/assets/aacr-2026/posters/agentic-ai.json | head -c 200
kill $SERVE_PID
```

Expected: poster-table div present, session content non-empty, JSON returns array of poster objects.

- [ ] **Step 10: Re-baseline checksums (the move was intentional, so checksums shift)**

```bash
cd /Users/lzhang34/Desktop/AACR
find docs/assets docs/conferences/aacr-2026/sessions docs/javascripts/tabulator.min.js docs/stylesheets/tabulator.min.css \
  -type f 2>/dev/null | sort > _baseline/file-list.txt
xargs -a _baseline/file-list.txt shasum -a 256 > _baseline/checksums.txt
```

This refreshed baseline is what later tasks compare against.

- [ ] **Step 11: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add -A
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "refactor: move docs/topics, docs/sessions, docs/index.md under conferences/aacr-2026/

Switches poster-JSON output to docs/assets/aacr-2026/posters/<topic>.json
and re-depths relative paths in topic indexes (data-src, sessions links).
Stub root docs/index.md is rewritten in a later task.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: Move Nextflow Summit transcripts into `nextflow-2026/`

**Why:** Physically relocate the three transcripts from `_Extra/Nextflow/` into the new conference's data dir, with the slug names confirmed in the spec. `_Extra/Nextflow/` is removed (it was a holding area).

**Files:**
- Create: `nextflow-2026/transcripts/sessions/`
- Move (git): `_Extra/Nextflow/transcript_day_1_before_lunch.md` → `nextflow-2026/transcripts/sessions/2026-04-30-nextflow-summit-day-1-am.md`
- Move (git): `_Extra/Nextflow/transcript_day_1_after_lunch.md` → `nextflow-2026/transcripts/sessions/2026-04-30-nextflow-summit-day-1-pm.md`
- Move (git): `_Extra/Nextflow/transcript_day_2.md` → `nextflow-2026/transcripts/sessions/2026-05-01-nextflow-summit-day-2.md`
- Remove: `_Extra/Nextflow/` (empty after moves; the `_Extra/JPM26/` sibling stays for now)

- [ ] **Step 1: Confirm `_Extra/Nextflow/` is currently untracked (per initial git status)**

```bash
cd /Users/lzhang34/Desktop/AACR
git status _Extra/Nextflow
```

If `_Extra/` is untracked (matches initial git state), `git mv` won't work; use plain `mv` and `git add` the destination. If tracked, use `git mv`.

- [ ] **Step 2: Move and rename the three transcripts**

If untracked:

```bash
cd /Users/lzhang34/Desktop/AACR
mkdir -p nextflow-2026/transcripts/sessions
mv _Extra/Nextflow/transcript_day_1_before_lunch.md nextflow-2026/transcripts/sessions/2026-04-30-nextflow-summit-day-1-am.md
mv _Extra/Nextflow/transcript_day_1_after_lunch.md nextflow-2026/transcripts/sessions/2026-04-30-nextflow-summit-day-1-pm.md
mv _Extra/Nextflow/transcript_day_2.md nextflow-2026/transcripts/sessions/2026-05-01-nextflow-summit-day-2.md
rmdir _Extra/Nextflow
```

If tracked, swap each `mv` for `git mv`.

- [ ] **Step 3: Verify file sizes match the pre-move state**

```bash
cd /Users/lzhang34/Desktop/AACR
ls -la nextflow-2026/transcripts/sessions/
```

Expected: 3 files, sizes ~108 KB, ~121 KB, ~142 KB respectively (matching the spec's disk-layout block).

- [ ] **Step 4: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add nextflow-2026 _Extra
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "data: move Nextflow Summit 2026 transcripts under nextflow-2026/

3 transcripts (~370 KB total) renamed to date-prefixed slugs:
- 2026-04-30-nextflow-summit-day-1-am
- 2026-04-30-nextflow-summit-day-1-pm
- 2026-05-01-nextflow-summit-day-2

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 7: Render Nextflow session pages from `build_site.py`

**Why:** The Nextflow transcripts are already markdown (unlike AACR's `.txt` captions), so the build step is a thin copy with an admonition wrapper. Generates one `<slug>.md` per transcript under `docs/conferences/nextflow-2026/sessions/` plus an `index.md` listing them, plus a one-page conference overview at `docs/conferences/nextflow-2026/index.md`.

**Files:**
- Create: `docs/conferences/nextflow-2026/index.md`
- Modify: `scripts/build_site.py` — add `build_md_session_pages(conf)` and dispatch to it for `session_source == "md-transcripts"`

- [ ] **Step 1: Add `build_md_session_pages` to `build_site.py`**

In `/Users/lzhang34/Desktop/AACR/scripts/build_site.py`, before `def main():`, add:

```python
def build_md_session_pages(conf: dict) -> int:
    """Copy each .md transcript from data_dir/transcripts/sessions/ into
    docs_dir/sessions/, wrapped with a header admonition. Generates an
    index.md listing all sessions for the conference.

    Suitable for conferences whose transcripts are already markdown
    (e.g., Nextflow Summit), as opposed to AACR's plain-text captions.
    """
    if conf.get("session_source") != "md-transcripts":
        return 0
    src_dir = data_path(conf, "transcripts", "sessions")
    if not src_dir.exists():
        return 0
    out_dir = docs_path(conf, "sessions")
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    entries = []
    for src in sorted(src_dir.glob("*.md")):
        body = src.read_text()
        # Slug is filename without extension; date is first 10 chars of slug (YYYY-MM-DD)
        slug = src.stem
        date = slug[:10] if len(slug) >= 10 and slug[4] == "-" and slug[7] == "-" else "(unknown)"
        word_count = len(body.split())
        wrapped = f"""# {slug}

**Date:** {date}
**Source:** `{conf['data_dir']}/transcripts/sessions/{src.name}`
**Word count:** ~{word_count:,}

!!! note "Auto-generated captions"
    This transcript is from auto-generated English captions on the live event stream. Expect misheard names and technical terms (e.g., "Vicksville" for "Nextflow"). Use search for exact quotes.

{body}
"""
        (out_dir / src.name).write_text(wrapped)
        entries.append((slug, word_count))
        written += 1

    idx_lines = [
        f"# {conf['label']} — Session Transcripts",
        "",
        f"All {written} session transcripts from {conf['label']}.",
        "",
        "| Session | Date | Words |",
        "|---|---|---|",
    ]
    for slug, wc in sorted(entries):
        date = slug[:10]
        idx_lines.append(f"| [{slug}]({slug}.md) | {date} | ~{wc:,} |")
    idx_lines.append("")
    (out_dir / "index.md").write_text("\n".join(idx_lines))
    print(f"→ {written} session pages + sessions/index.md for {conf['slug']}")
    return written
```

- [ ] **Step 2: Wire `build_md_session_pages` into `main()`**

In the same file, in `main()`, replace:

```python
        if conf.get("session_source") == "txt-transcripts":
            total_sessions += build_session_pages(conf)
```

with:

```python
        if conf.get("session_source") == "txt-transcripts":
            total_sessions += build_session_pages(conf)
        if conf.get("session_source") == "md-transcripts":
            total_sessions += build_md_session_pages(conf)
```

- [ ] **Step 3: Create `docs/conferences/nextflow-2026/index.md`**

Write to `/Users/lzhang34/Desktop/AACR/docs/conferences/nextflow-2026/index.md`:

```markdown
# Nextflow Summit 2026

Transcripts from the Nextflow Summit (April 30 – May 1, 2026), held in person and live-streamed via Goldcast. Three sessions captured: an opening day on AI in scientific workflows + protein-design competitions, an afternoon on workflow evolution and pipelines, and a second day on the Nextflow community training and ambassador program.

**Caveat:** Transcripts are from auto-generated English captions on the live stream. Misheard names and technical terms are common — for example, "Vicksville" appears throughout in place of "Nextflow." Use search for exact quotes; treat names as approximations until confirmed.

## Sessions

See [All sessions](sessions/) for the full list.

| Session | Date |
|---|---|
| [Day 1 (AM)](sessions/2026-04-30-nextflow-summit-day-1-am/) | 2026-04-30 |
| [Day 1 (PM)](sessions/2026-04-30-nextflow-summit-day-1-pm/) | 2026-04-30 |
| [Day 2](sessions/2026-05-01-nextflow-summit-day-2/) | 2026-05-01 |

## Source

Live stream: [Goldcast event ff174b87](https://events.goldcast.io/e/ff174b87-316f-47c7-8c7b-a51028b670b7).
Raw transcripts: `nextflow-2026/transcripts/sessions/` in this repo.
```

- [ ] **Step 4: Build and verify**

```bash
cd /Users/lzhang34/Desktop/AACR
python scripts/build_site.py > /tmp/build7.log 2>&1
ls docs/conferences/nextflow-2026/sessions/
wc -w docs/conferences/nextflow-2026/sessions/2026-04-30-nextflow-summit-day-1-am.md
```

Expected: 4 files (3 session pages + `index.md`), word counts non-trivial (~17K-22K each).

- [ ] **Step 5: Add Nextflow tab to `mkdocs.yml` nav**

In `/Users/lzhang34/Desktop/AACR/mkdocs.yml`, after the `- All AACR sessions: ...` line and before the `- Notes:` section, insert:

```yaml
  - Nextflow Summit 2026:
    - Overview: conferences/nextflow-2026/index.md
    - All sessions: conferences/nextflow-2026/sessions/index.md
    - Day 1 (AM): conferences/nextflow-2026/sessions/2026-04-30-nextflow-summit-day-1-am.md
    - Day 1 (PM): conferences/nextflow-2026/sessions/2026-04-30-nextflow-summit-day-1-pm.md
    - Day 2: conferences/nextflow-2026/sessions/2026-05-01-nextflow-summit-day-2.md
```

- [ ] **Step 6: Build mkdocs and smoke-test**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdocs build --strict 2>&1 | tee /tmp/mkdocs7.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs7.log
mkdocs serve -a 127.0.0.1:8765 &
SERVE_PID=$!
sleep 3
curl -s http://127.0.0.1:8765/conferences/nextflow-2026/ | grep -c "Nextflow Summit"
curl -s http://127.0.0.1:8765/conferences/nextflow-2026/sessions/2026-04-30-nextflow-summit-day-1-am/ | head -c 200
kill $SERVE_PID
```

Expected: warning count near baseline, Nextflow overview page renders, day-1 AM session non-empty.

- [ ] **Step 7: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add -A
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "build: render Nextflow Summit session pages + add Nextflow tab

build_md_session_pages() copies each .md transcript with an admonition
header. Adds nav tab and conference overview page.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 8: Add JPM 2026 placeholder

**Why:** Spec says JPM gets an empty stub conference — no expected-content roadmap, just title + "no content yet." Three artifacts: a `jpm-2026/README.md`, a `docs/conferences/jpm-2026/index.md`, and a JPM nav tab.

**Files:**
- Create: `jpm-2026/README.md`
- Create: `docs/conferences/jpm-2026/index.md`
- Modify: `mkdocs.yml` (add JPM tab)

- [ ] **Step 1: Create `jpm-2026/README.md`**

Write to `/Users/lzhang34/Desktop/AACR/jpm-2026/README.md`:

```markdown
# JPM 2026

Placeholder for J.P. Morgan Healthcare Conference 2026 corpus. No content yet.
```

- [ ] **Step 2: Create `docs/conferences/jpm-2026/index.md`**

Write to `/Users/lzhang34/Desktop/AACR/docs/conferences/jpm-2026/index.md`:

```markdown
# JPM 2026

J.P. Morgan Healthcare Conference 2026.

No content yet.
```

- [ ] **Step 3: Add JPM tab to `mkdocs.yml` nav**

In `/Users/lzhang34/Desktop/AACR/mkdocs.yml`, after the Nextflow tab block (added in Task 7) and before `- Notes:`, insert:

```yaml
  - JPM 2026:
    - Overview: conferences/jpm-2026/index.md
```

- [ ] **Step 4: Build and verify**

```bash
cd /Users/lzhang34/Desktop/AACR
python scripts/build_site.py > /tmp/build8.log 2>&1
mkdocs build --strict 2>&1 | tee /tmp/mkdocs8.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs8.log
mkdocs serve -a 127.0.0.1:8765 &
SERVE_PID=$!
sleep 3
curl -s http://127.0.0.1:8765/conferences/jpm-2026/ | grep -c "No content yet"
kill $SERVE_PID
```

Expected: build succeeds, JPM page renders with "No content yet."

- [ ] **Step 5: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add -A
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "scaffold: add JPM 2026 placeholder conference

Stub README and index page. Empty until JPM content arrives.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 9: Rewrite the home page as a 3-conference card grid

**Why:** Replaces the temporary stub `docs/index.md` from Task 5 with the real multi-conference home, per the spec. Uses `attr_list` + `md_in_html` (both already enabled in `mkdocs.yml`).

**Files:**
- Modify: `docs/index.md` (replace stub with full 3-card home)

- [ ] **Step 1: Replace `docs/index.md`**

Overwrite `/Users/lzhang34/Desktop/AACR/docs/index.md` with:

```markdown
# Conference Corpus

Curated transcripts and abstracts from biomedical and computational biology meetings, organized into a single searchable site.

## Conferences

[**AACR 2026**](conferences/aacr-2026/){ .md-button }
American Association for Cancer Research Annual Meeting. ~26 sessions, ~2,300 posters across 5 topics: agentic AI, single-cell & spatial omics, virtual cells, bioinfo / comp bio / AI methods, and clinical trials.

[**Nextflow Summit 2026**](conferences/nextflow-2026/){ .md-button }
Nextflow Summit (April 30 – May 1, 2026). 3 session transcripts (~370 KB total) on AI in scientific workflows, protein-design competition pipelines, and Nextflow community training.

[**JPM 2026**](conferences/jpm-2026/){ .md-button }
J.P. Morgan Healthcare Conference 2026. Placeholder — no content yet.

## How to use this site

1. **Pick a conference tab** — top nav has one tab per conference plus a global Notes section.
2. **Within a conference** — each conference has its own structure. AACR is split by topic with filterable poster tables; Nextflow is a flat session list; JPM is a stub.
3. **Search** — the top-right search indexes session transcripts and page content site-wide.

See [extraction notes](notes/extraction.md) and [caveats](notes/caveats.md) for details on how transcripts and abstracts were sourced.
```

- [ ] **Step 2: Build and smoke-test**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdocs build --strict 2>&1 | tee /tmp/mkdocs9.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs9.log
mkdocs serve -a 127.0.0.1:8765 &
SERVE_PID=$!
sleep 3
curl -s http://127.0.0.1:8765/ | grep -cE "AACR 2026|Nextflow Summit 2026|JPM 2026"
kill $SERVE_PID
```

Expected: 3 (one match per conference card).

- [ ] **Step 3: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add docs/index.md
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "ui: rewrite home page as 3-conference card grid

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 10: Rewrite repo-level `README.md` as conference-corpus overview

**Why:** Current README is AACR-specific (talks only about AACR layout, topics, poster overlaps). Replace with a multi-conference README; keep the AACR-specific tables but reframed as one conference among three.

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace `README.md`**

Overwrite `/Users/lzhang34/Desktop/AACR/README.md` with:

```markdown
# Conference Corpus — Multi-Conference Transcripts & Abstracts

Curated content from biomedical and computational biology meetings, served as one searchable MkDocs Material site (private, Cloudflare Pages + Basic Auth) with one nav tab per conference.

## Conferences

| Conference | Status | Sessions | Posters |
|---|---|---|---|
| **AACR 2026** | Live | ~26 unique transcripts | 2,298 (1,953 unique by Id) |
| **Nextflow Summit 2026** | Live | 3 transcripts (~370 KB) | — |
| **JPM 2026** | Placeholder | — | — |

## Layout

```
conference-corpus/
├── aacr-2026/                    # AACR 2026 raw data (transcripts/, raw/)
│   ├── transcripts/{agentic-ai,single-cell-spatial-omics,virtual-cells,bioinfo-tools,clinical-trials}/
│   └── raw/{...}/
├── nextflow-2026/                # Nextflow Summit raw data
│   └── transcripts/sessions/     # 3 .md files
├── jpm-2026/                     # JPM 2026 placeholder
├── docs/                         # MkDocs source
│   ├── index.md                  # 3-conference home
│   ├── conferences/{aacr-2026,nextflow-2026,jpm-2026}/
│   ├── notes/                    # extraction & caveats (shared)
│   ├── assets/{aacr-2026}/posters/{topic}.json   # generated
│   ├── javascripts/, stylesheets/                # shared
│   └── superpowers/specs, superpowers/plans      # design docs
├── scripts/
│   ├── build_site.py             # Preprocessor: poster JSON, session pages, dossier matrix
│   └── conferences.py            # Conference registry (single source of truth)
├── functions/_middleware.js      # Cloudflare Pages Basic Auth
├── mkdocs.yml                    # navigation.tabs — one tab per conference
└── requirements.txt
```

## Build

```bash
pip install -r requirements.txt
python scripts/build_site.py        # generate poster JSON, session pages, tool dossiers
mkdocs build                        # render the static site
```

`python scripts/build_site.py --survey` prints the bioinfo-tools mention table without writing files.

## AACR 2026 — topic breakdown

| Topic | Sessions | Words | Posters | Poster words |
|---|---|---|---|---|
| Agentic AI | 5 full + 3 AT02 slices | ~67,000 | 57 | ~19,000 |
| Single-cell & spatial omics | 20 full (1 shared) | ~273,000 | 1,015 | ~328,000 |
| Virtual cells | 1 native + 5 symlinks | ~80,500 | 48 | ~16,000 |
| Bioinfo / comp bio / AI methods | 12 symlinks (all borrowed) | ~162,000 | 536 | ~170,000 |
| Clinical trials | Deferred | — | 642 | ~230,000 |
| **Totals** | ~26 unique sessions | ~464,000 | 2,298 (1,953 unique by Id) | ~763,000 |

The bioinfo-tools sub-section includes a [tools matrix](https://github.com/LiudengZhang/conference-corpus/tree/main/docs/conferences/aacr-2026/topics/bioinfo-tools/tools) of foundation models and methods that cleared a 3-mention inclusion gate against the corpus (CHIEF, UNI/UNI2, Prov-GigaPath, Geneformer, scGPT, Cell2Location).

## Nextflow Summit 2026

Three sessions (Day 1 AM/PM, Day 2) captured from Goldcast event `ff174b87-316f-47c7-8c7b-a51028b670b7`. Captions are auto-generated; "Vicksville" recurs as a captioner mishearing of "Nextflow."

## JPM 2026

Placeholder folder; content to be added.

## Caveats

- All session captions are auto-generated English from the live stream. Expect misheard names and acronyms ("Foersch" → "Firsch", "Bunne" → "Bonner", "scGPT" → "SC-GPT", "Nextflow" → "Vicksville").
- Sub-talks inside a parent AACR session share the parent's video. Time-slice the parent VTT to extract one sub-talk (see the AT02 per-speaker slices as a worked example).
- VTT signatures in raw Vimeo configs expire after ~6 hours; re-extracting a session means re-navigating the live page.
- Clinical-trials session transcripts are deferred — the AACR poster corpus (~294K words) is the primary artifact for that topic.

See `docs/conferences/aacr-2026/topics/<topic>/README.md` for per-topic extraction methods, keyword unions, and overlap stats.
```

- [ ] **Step 2: Build (no behavior change in mkdocs; this only changes the GitHub README)**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdocs build --strict 2>&1 | tee /tmp/mkdocs10.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs10.log
```

Expected: warning count unchanged from Task 9.

- [ ] **Step 3: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add README.md
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "docs: rewrite repo README as conference-corpus overview

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 11: Update `mkdocs.yml` site_name + push branch + Cloudflare preview verification

**Why:** Branding + push a preview deploy to validate Cloudflare Pages still resolves under the new layout. `site_name` flips from "AACR Annual Meeting 2026" to "Conference Corpus" so the browser tab and header reflect the multi-conference scope. `repo_url` and `repo_name` stay on `aacr-2026` until Task 12 (after merge).

**Files:**
- Modify: `mkdocs.yml:1-2` (site_name + site_description)

- [ ] **Step 1: Update `site_name` and `site_description` in `mkdocs.yml`**

Replace lines 1-2 of `/Users/lzhang34/Desktop/AACR/mkdocs.yml`:

```yaml
site_name: Conference Corpus
site_description: Session transcripts and poster abstracts from AACR 2026, Nextflow Summit 2026, and JPM 2026 (placeholder), unified into one searchable site.
```

- [ ] **Step 2: Local build sanity check**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdocs build --strict 2>&1 | tee /tmp/mkdocs11.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs11.log
grep -c "Conference Corpus" site/index.html
```

Expected: warning count unchanged, "Conference Corpus" appears in rendered HTML.

- [ ] **Step 3: Commit**

```bash
cd /Users/lzhang34/Desktop/AACR
git add mkdocs.yml
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "ui: rebrand site as Conference Corpus

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 4: Push branch and let Cloudflare Pages produce a preview**

```bash
cd /Users/lzhang34/Desktop/AACR
git push -u origin refactor/conference-corpus
```

Expected: branch pushed; Cloudflare Pages picks it up and produces a preview URL of the form `https://refactor-conference-corpus.<project-name>.pages.dev`.

- [ ] **Step 5: Manual verification of preview deploy**

Visit the Cloudflare Pages preview URL in a browser. Verify:

1. Basic Auth still gates the site (you get the auth prompt).
2. Home page shows 3 conference cards.
3. Click each tab: AACR opens to the multi-topic view, Nextflow shows the 3 sessions, JPM shows "No content yet."
4. Click into one AACR topic (e.g., Agentic AI) — poster table loads, sortable, abstract expansion still works.
5. Click into one AACR session transcript page — body renders.
6. Click into one tool dossier (e.g., scGPT) — mention block at the bottom is intact, links to session pages work.
7. Hypothesis sidebar appears on the right edge.

If any of these fail, fix locally and force-push the branch (`git push --force-with-lease`).

- [ ] **Step 6: Open PR**

```bash
cd /Users/lzhang34/Desktop/AACR
gh pr create --title "Conference Corpus refactor: aacr-2026 → multi-conference monorepo" --body "$(cat <<'EOF'
## Summary
- Converts the single-conference \`aacr-2026\` repo into a multi-conference monorepo hosting AACR 2026, Nextflow Summit 2026, and a JPM 2026 placeholder, served as one MkDocs Material site with one tab per conference.
- Introduces \`scripts/conferences.py\` as the single source of truth; generalizes \`scripts/build_site.py\` to dispatch per-conference work.
- Moves AACR data under \`aacr-2026/\` and AACR docs under \`docs/conferences/aacr-2026/\`. Adds \`nextflow-2026/\` (3 transcripts) and \`jpm-2026/\` (placeholder).
- Switches poster JSON output from \`docs/assets/<topic>-posters.json\` to \`docs/assets/aacr-2026/posters/<topic>.json\`.
- Rewrites home page as a 3-conference card grid. Re-brands site as "Conference Corpus."
- Cloudflare Pages, Basic Auth, Hypothesis annotation, and Tabulator wiring all unchanged.

Spec: \`docs/superpowers/specs/2026-05-06-conference-corpus-design.md\`
Plan: \`docs/superpowers/plans/2026-05-06-conference-corpus.md\`

## Test plan
- [x] \`python scripts/build_site.py && mkdocs build --strict\` succeeds on every commit (modulo pre-existing baseline warnings).
- [x] Generated AACR poster JSONs are byte-identical to pre-refactor output (after path-flip in Task 5).
- [x] Local \`mkdocs serve\` smoke-checked: 3 cards on home, AACR topic page renders with poster table, Nextflow session page non-empty, JPM placeholder visible.
- [ ] Cloudflare Pages preview deploy: Basic Auth gates, all 3 tabs render, tool-dossier mention blocks intact (verify in PR review).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

Expected: PR URL printed.

---

## Task 12: After merge — repo rename + repo_url update

**Why:** Renaming on GitHub is safer after the refactor PR merges (the PR doesn't span a rename, and the new structure is already on `main`). GitHub serves redirects from the old URL indefinitely. Update `mkdocs.yml`'s `repo_url` and `repo_name` in a follow-up commit on `main`.

**Note:** This task only runs after the PR from Task 11 is merged.

**Files:**
- Modify: `mkdocs.yml:3-4` (repo_url, repo_name)

- [ ] **Step 1: Wait for PR merge**

Confirm the PR opened in Task 11 has been merged to `main` before proceeding.

- [ ] **Step 2: Rename the repo on GitHub**

Via GitHub web UI: `Settings → Rename` from `aacr-2026` to `conference-corpus`. (Cannot be automated via CLI by Claude — this is a user action.)

- [ ] **Step 3: Update local remote URL**

```bash
cd /Users/lzhang34/Desktop/AACR
git remote set-url origin https://github.com/LiudengZhang/conference-corpus.git
git remote -v
git fetch origin
```

Expected: `origin` now points to `conference-corpus.git`.

- [ ] **Step 4: Branch off main for the repo_url update**

```bash
cd /Users/lzhang34/Desktop/AACR
git checkout main
git pull
git checkout -b chore/repo-url-update
```

- [ ] **Step 5: Update `mkdocs.yml`**

Replace lines 3-4 of `/Users/lzhang34/Desktop/AACR/mkdocs.yml`:

```yaml
repo_url: https://github.com/LiudengZhang/conference-corpus
repo_name: LiudengZhang/conference-corpus
```

- [ ] **Step 6: Build and verify**

```bash
cd /Users/lzhang34/Desktop/AACR
mkdocs build --strict 2>&1 | tee /tmp/mkdocs12.log; true
grep -cE "WARNING|ERROR" /tmp/mkdocs12.log
grep -c "conference-corpus" site/index.html
```

Expected: warning count unchanged, "conference-corpus" appears in the rendered HTML (footer link).

- [ ] **Step 7: Commit and push**

```bash
cd /Users/lzhang34/Desktop/AACR
git add mkdocs.yml
git -c user.name="Liudeng Zhang" -c user.email="zhangliudeng@gmail.com" commit -m "chore: update mkdocs repo_url to conference-corpus

GitHub repo was renamed from aacr-2026 to conference-corpus; mkdocs
footer link follows.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
git push -u origin chore/repo-url-update
gh pr create --title "chore: update mkdocs repo_url to conference-corpus" --body "Follow-up to the conference-corpus refactor: GitHub repo was renamed, mkdocs footer link follows."
```

---

## Done

After Task 12 lands, the refactor is complete:

- Three conferences live under `conference-corpus.pages.dev` with Basic Auth.
- AACR 2026 retains every existing feature (poster tables, session pages, tool-dossier matrix, mention blocks, Hypothesis annotation).
- Nextflow Summit 2026 has 3 session transcripts under its own tab.
- JPM 2026 placeholder is visible and one nav-update away from real content.
- The build pipeline is conference-driven via `scripts/conferences.py`; adding a fourth conference is a config edit + data drop, not a code rewrite.
