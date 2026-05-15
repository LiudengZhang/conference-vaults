#!/usr/bin/env python3
"""Site-build preprocessor for the conference corpus.

Runs before `mkdocs build` on Cloudflare Pages. Iterates the CONFERENCES
registry from scripts/conferences.py and dispatches per-conference work:

  - Poster JSON for Tabulator tables (where conf.has_posters)
  - One MD page per unique session transcript (where conf.session_source set)
  - Tool-dossier mention blocks + matrix JSON (where conf.has_tools_index)
  - Tabulator JS/CSS vendored from CDN once at the top of the build

Path resolution flows through data_path(conf, ...), docs_path(conf, ...),
and conf_assets_path(conf, ...) so per-conference layout migrations are a
config edit, not a code change.

Idempotent: overwrites generated files on each run.
"""

import json
import re
import sys
import urllib.request
from pathlib import Path
from collections import defaultdict

from conferences import CONFERENCES

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


TABULATOR_JS_URL = "https://cdn.jsdelivr.net/npm/tabulator-tables@6.2.5/dist/js/tabulator.min.js"
TABULATOR_CSS_URL = "https://cdn.jsdelivr.net/npm/tabulator-tables@6.2.5/dist/css/tabulator.min.css"

INCLUSION_GATE = 3  # min unique mentions (posters + sessions, deduped) to ship a dossier

# (display_name, slug, family, [aliases])
# aliases are matched case-insensitive with word boundaries on both sides
TOOLS = [
    ("CHIEF",                 "chief",          "path-fm",     ["CHIEF"]),
    ("UNI / UNI2",            "uni",            "path-fm",     ["UNI", "UNI2", "UNI-2"]),
    ("CONCH",                 "conch",          "path-fm",     ["CONCH"]),
    ("PathChat",              "pathchat",       "path-fm",     ["PathChat", "Path-Chat"]),
    ("Virchow / Virchow2",    "virchow",        "path-fm",     ["Virchow", "Virchow2", "Virchow-2"]),
    ("Prov-GigaPath",         "prov-gigapath",  "path-fm",     ["Prov-GigaPath", "GigaPath"]),
    ("TITAN",                 "titan",          "path-fm",     ["TITAN"]),
    ("PLIP",                  "plip",           "path-fm",     ["PLIP"]),
    ("scGPT",                 "scgpt",          "sc-fm",       ["scGPT", "SC-GPT"]),
    ("Geneformer",            "geneformer",     "sc-fm",       ["Geneformer"]),
    ("UCE",                   "uce",            "sc-fm",       ["UCE", "Universal Cell Embeddings"]),
    ("scFoundation",          "scfoundation",   "sc-fm",       ["scFoundation"]),
    ("scBERT",                "scbert",         "sc-fm",       ["scBERT"]),
    ("Nicheformer",           "nicheformer",    "sc-fm",       ["Nicheformer"]),
    ("Cell2Sentence",         "cell2sentence",  "sc-fm",       ["Cell2Sentence", "C2S"]),
    ("Tangram",               "tangram",        "spatial",     ["Tangram"]),
    ("Cell2Location",         "cell2location",  "spatial",     ["Cell2Location", "cell2location"]),
    ("GEARS",                 "gears",          "perturbation",["GEARS"]),
    ("AlphaFold-Multimer",    "alphafold-multimer", "protein", ["AlphaFold-Multimer", "AlphaFold Multimer"]),
    ("ESM",                   "esm",            "protein",     ["ESM-2", "ESM2", "ESMFold"]),
]


def _alias_pattern(alias: str) -> re.Pattern:
    """Word-boundary, case-insensitive match for one alias.

    Standard \\b doesn't handle aliases that begin or end with non-word
    characters (like 'SC-GPT'). Custom lookbehind/lookahead checks for
    [A-Za-z0-9_] on either side instead.
    """
    return re.compile(rf"(?<![A-Za-z0-9_]){re.escape(alias)}(?![A-Za-z0-9_])", re.IGNORECASE)


def match_aliases(text: str, aliases: list[str]) -> bool:
    """Return True if any alias matches `text` with word boundaries."""
    return any(_alias_pattern(a).search(text) for a in aliases)


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


def _context_window(text: str, alias: str, chars: int = 220) -> str:
    """Return ~`chars` chars of `text` centered on the first alias hit, single line."""
    pat = _alias_pattern(alias)
    m = pat.search(text)
    if not m:
        return ""
    start = max(0, m.start() - chars // 2)
    end = min(len(text), m.end() + chars // 2)
    snippet = text[start:end].strip()
    snippet = re.sub(r"\s+", " ", snippet)
    if start > 0:
        snippet = "…" + snippet
    if end < len(text):
        snippet = snippet + "…"
    return snippet


def scan_mentions(corpus: dict, aliases: list[str]) -> dict:
    """Find unique poster + session hits for any alias in `aliases`.

    Returns {"posters": [...], "sessions": [...]}, each item a dict
    augmented with `context` (~220-char snippet around first match).
    """
    poster_hits = []
    for p in corpus["posters"]:
        haystack = (p.get("Title", "") or "") + "\n" + (p.get("Abstract", "") or "")
        if not match_aliases(haystack, aliases):
            continue
        ctx = ""
        for a in aliases:
            ctx = _context_window(haystack, a)
            if ctx:
                break
        poster_hits.append({
            "Id": p["Id"],
            "Title": p.get("Title", ""),
            "PresentationNumber": p.get("PresentationNumber", "") or p.get("Id", ""),
            "context": ctx,
            "_topics": p.get("_topics", [p.get("_topic", "")]),
        })

    session_hits = []
    for s in corpus["sessions"]:
        if not match_aliases(s["text"], aliases):
            continue
        ctx = ""
        for a in aliases:
            ctx = _context_window(s["text"], a)
            if ctx:
                break
        session_hits.append({
            "stem": s["stem"],
            "context": ctx,
            "_topics": s["_topics"],
        })

    return {"posters": poster_hits, "sessions": session_hits}


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


MENTIONS_START = "<!-- mentions:start -->"
MENTIONS_END = "<!-- mentions:end -->"


def render_mentions_block(tool_name: str, hits: dict) -> str:
    """Build the markdown block (markers included) for a tool's corpus mentions."""
    lines = [MENTIONS_START, ""]
    posters = hits["posters"]
    sessions = hits["sessions"]

    lines.append(f"**Posters mentioning {tool_name} (n={len(posters)}):**")
    lines.append("")
    if not posters:
        lines.append("_No posters in the AACR 2026 corpus mention this tool._")
    else:
        for p in sorted(posters, key=lambda x: x.get("PresentationNumber", "")):
            num = p.get("PresentationNumber") or p.get("Id", "")
            title = p.get("Title", "").strip()
            ctx = p.get("context", "")
            lines.append(f"- **{num}** — *{title}*")
            if ctx:
                lines.append(f"  {ctx}")
    lines.append("")

    lines.append(f"**Sessions mentioning {tool_name} (n={len(sessions)}):**")
    lines.append("")
    if not sessions:
        lines.append("_No session transcripts in the AACR 2026 corpus mention this tool._")
    else:
        for s in sorted(sessions, key=lambda x: x["stem"]):
            stem = s["stem"]
            ctx = s.get("context", "")
            lines.append(f"- [{stem}](../../../sessions/{stem}.md)")
            if ctx:
                lines.append(f"  {ctx}")
    lines.append("")
    lines.append(MENTIONS_END)
    return "\n".join(lines)


def inject_mentions_block(md_text: str, new_block: str) -> str:
    """Replace the existing mentions block (between markers) with `new_block`.

    If markers are missing, append `new_block` to the end. `new_block` must
    contain its own start/end markers.
    """
    if MENTIONS_START in md_text and MENTIONS_END in md_text:
        pattern = re.compile(
            re.escape(MENTIONS_START) + r".*?" + re.escape(MENTIONS_END),
            re.DOTALL,
        )
        return pattern.sub(new_block, md_text)
    sep = "" if md_text.endswith("\n") else "\n"
    return md_text + sep + "\n" + new_block + "\n"


def stub_dossier(name: str, slug: str, family: str, also_in: list[str]) -> str:
    """Author-fillable scaffold for a new tool dossier."""
    also = ", ".join(sorted(set(also_in))) if also_in else "(none)"
    return f"""# {name}

**Family:** {family}
**Modality:** TODO
**Released:** TODO
**License:** TODO
**Code/checkpoint:** TODO
**Also surfaced in:** {also}

> TODO — one-paragraph plain-language description (~3 sentences). What
> the tool does, what it trains on, what its standout claim is.

## Architecture & training

TODO — backbone, pretraining corpus, objective, parameter count.

## Use in the AACR 2026 corpus

{MENTIONS_START}
_Auto-generated on next build._
{MENTIONS_END}

## What's missing / where evidence is weak

- TODO

## Takeaway

TODO — one paragraph on what the AACR 2026 corpus uniquely teaches us
about {name}.
"""


def build_tool_pages(conf: dict):
    """Survey the corpus, gate, then write/refresh dossier mention blocks
    and emit the matrix + mentions JSON for the index page."""
    if not conf.get("has_tools_index"):
        return
    tools_dir = docs_path(conf, "topics", "bioinfo-tools", "tools")
    tools_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = conf_assets_path(conf, "bioinfo-tools")
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


def ensure_dirs():
    """Create global directories that exist regardless of conference.
    Per-conference directories are created lazily by their respective
    build_* functions when needed."""
    JS_DIR.mkdir(parents=True, exist_ok=True)


def vendor_tabulator():
    css_dir = DOCS / "stylesheets"
    css_dir.mkdir(parents=True, exist_ok=True)
    targets = [
        (TABULATOR_JS_URL, JS_DIR / "tabulator.min.js", 50_000),
        (TABULATOR_CSS_URL, css_dir / "tabulator.min.css", 10_000),
    ]
    for url, out, min_size in targets:
        if out.exists() and out.stat().st_size > min_size:
            continue
        print(f"→ fetching {out.name} from {url}")
        req = urllib.request.Request(url, headers={"User-Agent": "aacr-build"})
        with urllib.request.urlopen(req, timeout=30) as r:
            out.write_bytes(r.read())


def build_poster_json(conf: dict, topic_slug: str) -> int:
    src = data_path(conf, "transcripts", topic_slug, "posters", "abstracts.jsonl")
    if not src.exists():
        return 0
    out = conf_assets_path(conf, "posters", f"{topic_slug}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
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


def slugify_transcript_filename(path: Path) -> str:
    """transcript .txt file basenames are already slugged; keep as-is (without extension)."""
    return path.stem


def resolve_symlink(p: Path) -> Path:
    return p.resolve() if p.is_symlink() else p


def read_transcript_text(txt_path: Path) -> str:
    """Read transcript, wrap long prose into paragraphs at sentence boundaries."""
    raw = resolve_symlink(txt_path).read_text()
    # Transcripts are single-paragraph blobs. Re-wrap by inserting \n\n at sentence ends
    # for readability (not strictly needed but improves render).
    wrapped = re.sub(r"(?<=[.!?])\s+(?=[A-Z])", "\n\n", raw.strip())
    return wrapped


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


def main():
    if "--survey" in sys.argv:
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
        ensure_dirs()
        if conf.get("has_posters"):
            for topic_slug, _ in conf["topics"]:
                total_posters += build_poster_json(conf, topic_slug)
        total_sessions += build_session_pages(conf)
        total_sessions += build_md_session_pages(conf)
        build_tool_pages(conf)
    print(f"\nBuild preprocessing complete.")
    print(f"  Posters  : {total_posters:>5} total")
    print(f"  Sessions : {total_sessions:>5} unique transcript pages")


if __name__ == "__main__":
    main()
