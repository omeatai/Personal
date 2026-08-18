"""Shared sandbox + accordion helpers for JS tutorial sections."""
from __future__ import annotations

import html
import json
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAPS = ROOT / "snaps"
TUTORIAL = ROOT.parent / "tutorial.md"

RESULT_TMPL = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{title}</title>
    <link rel="stylesheet" href="../sandbox.css" />
    <style>
      pre {{
        white-space: pre-wrap;
        font-size: 15px;
        line-height: 1.35;
      }}
    </style>
  </head>
  <body>
    <h2>{heading}</h2>
    {body}
    <pre id="demo"></pre>
    {buttons}
    <script>
{script}
    </script>
  </body>
</html>
"""

SOURCE_TMPL = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{title} source</title>
    <link rel="stylesheet" href="../sandbox.css" />
    <style>
      body {{ background: #f1f1f1; }}
      pre {{
        margin: 0;
        padding: 12px 16px;
        background: #fff;
        border: 1px solid #ccc;
        border-left: 4px solid #04aa6d;
        font-family: Consolas, "Courier New", monospace;
        font-size: 16px;
        line-height: 1.4;
        white-space: pre-wrap;
      }}
    </style>
  </head>
  <body>
    <h3>Example</h3>
    <pre>{code}</pre>
  </body>
</html>
"""

INDEX_TMPL = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{title}</title>
    <link rel="stylesheet" href="../sandbox.css" />
  </head>
  <body>
    <h2>{title}</h2>
    <p>Open each example:</p>
    <ul>
{links}
    </ul>
  </body>
</html>
"""


def indent_js(code: str, spaces: int = 6) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line else "" for line in code.split("\n"))


def display_script(code: str, displays: list[tuple[str, str]]) -> str:
    parts = []
    for lab, expr in displays:
        parts.append(f"{json.dumps(lab + ' -> ')} + String({expr})")
    joined = ' + "\\n" + '.join(parts) if parts else '""'
    return f"""{indent_js(code)}
      document.getElementById("demo").innerText = {joined};"""


def S(
    stem: str,
    title: str,
    bullets: list[str],
    code: str,
    displays: list[tuple[str, str]] | None = None,
    outcome: str = "",
    *,
    script: str | None = None,
    body: str = "",
    buttons: str = "",
    wait_ms: int = 0,
) -> dict:
    if script is None:
        script = display_script(code, displays or [])
    return dict(
        stem=stem,
        title=title,
        bullets=bullets,
        code=code,
        script=script,
        outcome=outcome,
        body=body,
        buttons=buttons,
        wait_ms=wait_ms,
    )


def write_example(folder: Path, rec: dict) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{rec['stem']}.html").write_text(
        RESULT_TMPL.format(
            title=html.escape(rec["title"]),
            heading=html.escape(rec["title"]),
            body=rec.get("body") or "",
            buttons=rec.get("buttons") or "",
            script=rec["script"],
        ),
        encoding="utf-8",
    )
    (folder / f"{rec['stem']}-source.html").write_text(
        SOURCE_TMPL.format(title=html.escape(rec["title"]), code=html.escape(rec["code"])),
        encoding="utf-8",
    )


def write_index(folder: Path, title: str, items: list[tuple[str, str]]) -> None:
    links = "\n".join(
        f'      <li><a href="{stem}.html">{html.escape(label)}</a></li>'
        for stem, label in items
    )
    (folder / "index.html").write_text(
        INDEX_TMPL.format(title=html.escape(title), links=links),
        encoding="utf-8",
    )


def emit_section(slug: str, title: str, records: list[dict]) -> None:
    folder = ROOT / slug
    items = []
    for i, rec in enumerate(records, 1):
        write_example(folder, rec)
        items.append((rec["stem"], f"{i:02d} — {rec['title']}"))
    write_index(folder, title, items)


def md_example(slug: str, n: int, rec: dict) -> str:
    nn = f"{n:02d}"
    b = "\n".join(f"- [x] {x}" for x in rec["bullets"])
    return f"""<a id="{slug}-example-{nn}"></a>

### **Example {n}: {rec["title"]}**

{b}

Sandbox: `code_sandbox/{slug}/{rec["stem"]}.html`

```javascript
{rec["code"]}
```

<img alt="{slug} example {n} source" src="./code_sandbox/snaps/{slug}-{nn}-code.png" />

<img alt="{slug} example {n} result" src="./code_sandbox/snaps/{slug}-{nn}-result.png" />

- [x] **Outcome:** {rec["outcome"]}
"""


def md_qa(items: list[tuple[str, list[str]]]) -> str:
    blocks = []
    for i, (q, answers) in enumerate(items, 1):
        ans = "\n".join(f"- [x] {a}" for a in answers)
        blocks.append(
            f"""### Question {i}: {q}

<details>
<summary>Answer</summary>

{ans}

</details>
"""
        )
    return "\n".join(blocks)


def intro_toc(slug: str, records: list[dict]) -> str:
    lines = [f"This section has **{len(records)}** examples:", ""]
    for i, rec in enumerate(records, 1):
        lines.append(
            f"- [x] **Example {i}:** {rec['title']} [View](#{slug}-example-{i:02d})"
        )
    return "\n".join(lines)


def accordion(
    summary: str,
    intro: str,
    concepts: list[str],
    records: list[dict],
    slug: str,
    qa: list[tuple[str, list[str]]],
    summary_para: str,
    refs: list[tuple[str, str]],
) -> str:
    concept = "\n".join(f"- [x] {c}" for c in concepts)
    examples = "\n".join(md_example(slug, i, rec) for i, rec in enumerate(records, 1))
    ref_lines = "\n".join(f"- [{n}]({u})" for n, u in refs)
    return f"""<details>
  <summary>{summary}</summary>

## Introduction

{intro}

{intro_toc(slug, records)}

## Detailed Explanation

{concept}

{examples}
<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

```bash
# from Personal/Files/javascript/code_sandbox
py -3 -m http.server 8770 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8770/{slug}/`.

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

{md_qa(qa)}

</details>

## Summary

{summary_para}

## References

{ref_lines}

</details>
"""


def find_browser() -> str | None:
    candidates = [
        os.environ.get("CHROME_PATH"),
        shutil.which("msedge"),
        shutil.which("chrome"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for c in candidates:
        if c and Path(c).is_file():
            return c
    return None


def screenshot_section(slug: str, records: list[dict], browser: str, default_wait: int = 4000) -> None:
    SNAPS.mkdir(parents=True, exist_ok=True)
    folder = ROOT / slug
    for i, rec in enumerate(records, 1):
        nn = f"{i:02d}"
        result_html = (folder / f"{rec['stem']}.html").resolve().as_uri()
        source_html = (folder / f"{rec['stem']}-source.html").resolve().as_uri()
        result_png = str((SNAPS / f"{slug}-{nn}-result.png").resolve())
        code_png = str((SNAPS / f"{slug}-{nn}-code.png").resolve())
        wait = rec.get("wait_ms") or default_wait
        for url, out in ((source_html, code_png), (result_html, result_png)):
            cmd = [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                "--window-size=900,640",
                f"--screenshot={out}",
                f"--virtual-time-budget={wait}",
                url,
            ]
            subprocess.run(cmd, check=True, cwd=str(SNAPS), capture_output=True)


def build_and_snap(
    slug: str,
    title: str,
    records: list[dict],
    intro: str,
    concepts: list[str],
    qa: list[tuple[str, list[str]]],
    summary_para: str,
    refs: list[tuple[str, str]],
    *,
    wait: int = 4000,
) -> str:
    emit_section(slug, title, records)
    md = accordion(title, intro, concepts, records, slug, qa, summary_para, refs)
    out = ROOT / f"_generated_{slug}.md"
    out.write_text(md, encoding="utf-8")
    browser = find_browser()
    if not browser:
        raise RuntimeError("No Chrome/Edge found for screenshots")
    screenshot_section(slug, records, browser, default_wait=wait)
    return md
