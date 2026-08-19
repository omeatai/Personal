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


CONSOLE_BOOT = r"""
      const __out = [];
      let __indent = "";
      const __times = Object.create(null);
      const __counts = Object.create(null);
      function __fmt(args) {
        return Array.from(args).map(function (a) {
          if (typeof a === "string") return a;
          if (typeof a === "undefined") return "undefined";
          if (typeof a === "symbol") return String(a);
          if (a instanceof Error) return a.name + ": " + a.message;
          try { return JSON.stringify(a); } catch (e) { return String(a); }
        }).join(" ");
      }
      function __push(kind, args) {
        const rest = __fmt(args);
        __out.push(__indent + kind + (rest ? " " + rest : ""));
      }
      const __o = {
        log: console.log.bind(console),
        warn: console.warn.bind(console),
        error: console.error.bind(console),
        info: console.info.bind(console),
        dir: console.dir.bind(console),
        table: console.table.bind(console),
        assert: console.assert.bind(console),
        count: console.count.bind(console),
        clear: console.clear.bind(console),
        group: console.group.bind(console),
        groupCollapsed: console.groupCollapsed.bind(console),
        groupEnd: console.groupEnd.bind(console),
        time: console.time.bind(console),
        timeEnd: console.timeEnd.bind(console),
        trace: console.trace.bind(console)
      };
      console.log = function () { __o.log.apply(console, arguments); __push("log:", arguments); };
      console.warn = function () { __o.warn.apply(console, arguments); __push("warn:", arguments); };
      console.error = function () { __o.error.apply(console, arguments); __push("error:", arguments); };
      console.info = function () { __o.info.apply(console, arguments); __push("info:", arguments); };
      console.dir = function (obj) {
        __o.dir.apply(console, arguments);
        try { __out.push(__indent + "dir: " + JSON.stringify(obj)); }
        catch (e) { __out.push(__indent + "dir: " + String(obj)); }
      };
      console.table = function (data) {
        __o.table.apply(console, arguments);
        __out.push(__indent + "table: " + JSON.stringify(data));
      };
      console.assert = function (cond) {
        __o.assert.apply(console, arguments);
        if (!cond) {
          const rest = Array.prototype.slice.call(arguments, 1);
          __out.push(__indent + "assert: Assertion failed: " + __fmt(rest));
        }
      };
      console.count = function (label) {
        __o.count.apply(console, arguments);
        label = label === undefined ? "default" : String(label);
        __counts[label] = (__counts[label] || 0) + 1;
        __out.push(__indent + "count: " + label + ": " + __counts[label]);
      };
      console.clear = function () {
        __o.clear();
        __out.length = 0;
        __out.push("(console cleared)");
      };
      console.group = function () {
        __o.group.apply(console, arguments);
        __push("group:", arguments);
        __indent += "  ";
      };
      console.groupCollapsed = function () {
        __o.groupCollapsed.apply(console, arguments);
        __push("groupCollapsed:", arguments);
        __indent += "  ";
      };
      console.groupEnd = function () {
        __o.groupEnd();
        if (__indent.length >= 2) __indent = __indent.slice(0, -2);
        __out.push(__indent + "groupEnd");
      };
      console.time = function (label) {
        __o.time.apply(console, arguments);
        label = label === undefined ? "default" : String(label);
        __times[label] = performance.now();
        __out.push(__indent + "time: started " + JSON.stringify(label));
      };
      console.timeEnd = function (label) {
        __o.timeEnd.apply(console, arguments);
        label = label === undefined ? "default" : String(label);
        const started = __times[label];
        const ms = started !== undefined ? (performance.now() - started) : NaN;
        __out.push(__indent + "timeEnd: " + JSON.stringify(label) + ": " + (Number.isFinite(ms) ? ms.toFixed(1) + " ms" : "NaN"));
      };
      console.trace = function () {
        __o.trace.apply(console, arguments);
        const err = new Error(__fmt(arguments) || "trace");
        __out.push(__indent + "trace:\\n" + String(err.stack || "stack"));
      };
      function __flush() {
        document.getElementById("demo").innerText = __out.join("\n");
      }
"""


def console_script(code: str, *, catch: bool = False, after: str = "") -> str:
    inner = indent_js(code, 8 if catch else 6)
    if catch:
        body = f"""      try {{
{inner}
      }} catch (e) {{
        __out.push(e.name + ": " + e.message);
      }}"""
    else:
        body = indent_js(code, 6)
    extra = ("\n" + indent_js(after, 6)) if after else ""
    return f"""{CONSOLE_BOOT}
{body}{extra}
      __flush();"""


def nf_script(snippet: str) -> str:
    return f"""      let msg;
      try {{
        new Function({json.dumps(snippet)})();
        msg = "ran without error";
      }} catch (e) {{
        msg = e.name + ": " + e.message;
      }}
      document.getElementById("demo").innerText =
        msg + "\\n" + "(caught via new Function; a raw <script> would fail to parse)";"""


def out_script(js: str, lines: list[tuple[str, str]]) -> str:
    parts = [f'{json.dumps(lab + " -> ")} + String({expr})' for lab, expr in lines]
    joined = ' + "\\n" + '.join(parts)
    return f"""{indent_js(js)}
      document.getElementById("demo").innerText = {joined};"""


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
        full_html: str | None = None,
        extra_files: dict[str, str] | None = None,
        fence: str = "javascript",
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
        full_html=full_html,
        extra_files=extra_files or {},
        fence=fence,
    )


def write_example(folder: Path, rec: dict) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    if rec.get("full_html"):
        (folder / f"{rec['stem']}.html").write_text(rec["full_html"], encoding="utf-8")
    else:
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
    for name, content in (rec.get("extra_files") or {}).items():
        (folder / name).write_text(content, encoding="utf-8")


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

```{rec.get("fence") or "javascript"}
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


def screenshot_section(
    slug: str,
    records: list[dict],
    browser: str,
    default_wait: int = 4000,
    *,
    use_http: bool = False,
    port: int = 8771,
) -> None:
    import sys
    import time

    SNAPS.mkdir(parents=True, exist_ok=True)
    folder = ROOT / slug
    proc = None
    if use_http:
        proc = subprocess.Popen(
            [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
            cwd=str(ROOT),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(0.7)
    try:
        for i, rec in enumerate(records, 1):
            nn = f"{i:02d}"
            if use_http:
                result_html = f"http://127.0.0.1:{port}/{slug}/{rec['stem']}.html"
                source_html = f"http://127.0.0.1:{port}/{slug}/{rec['stem']}-source.html"
            else:
                result_html = (folder / f"{rec['stem']}.html").resolve().as_uri()
                source_html = (folder / f"{rec['stem']}-source.html").resolve().as_uri()
            result_png = str((SNAPS / f"{slug}-{nn}-result.png").resolve())
            code_png = str((SNAPS / f"{slug}-{nn}-code.png").resolve())
            wait = rec.get("wait_ms") or default_wait
            print(f"snap {slug}-{nn} {rec['stem']}", flush=True)
            if Path(result_png).is_file() and Path(code_png).is_file():
                print(f"skip existing {slug}-{nn}", flush=True)
                continue
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
                subprocess.run(cmd, check=True, cwd=str(SNAPS), capture_output=True, timeout=90)
    finally:
        if proc is not None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()


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
    use_http: bool = False,
    port: int = 8771,
) -> str:
    emit_section(slug, title, records)
    md = accordion(title, intro, concepts, records, slug, qa, summary_para, refs)
    out = ROOT / f"_generated_{slug}.md"
    out.write_text(md, encoding="utf-8")
    browser = find_browser()
    if not browser:
        raise RuntimeError("No Chrome/Edge found for screenshots")
    screenshot_section(
        slug, records, browser, default_wait=wait, use_http=use_http, port=port
    )
    return md
