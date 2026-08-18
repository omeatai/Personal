"""Shared HTML/DOM sandbox helpers for S24–S26."""
from __future__ import annotations

import html as html_lib

from _gen_lib import S


def ui_page(title: str, body: str, script: str, css: str = "") -> str:
    return f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="color-scheme" content="light" />
    <title>{html_lib.escape(title)}</title>
    <link rel="stylesheet" href="../sandbox.css" />
    <style>
      button {{ margin-right: 4px; }}
      {css}
    </style>
  </head>
  <body>
    {body}
    <pre id="demo"></pre>
    <script>
{script}
    </script>
  </body>
</html>
"""


def P(
    stem: str,
    title: str,
    bullets: list[str],
    code: str,
    outcome: str,
    *,
    body: str = "",
    js: str = "",
    css: str = "",
    wait_ms: int = 0,
    extra_files: dict[str, str] | None = None,
    fence: str = "html",
) -> dict:
    return S(
        stem,
        title,
        bullets,
        code,
        outcome=outcome,
        script="",
        full_html=ui_page(title, body, js, css),
        wait_ms=wait_ms,
        extra_files=extra_files or {},
        fence=fence,
    )


def show_js(expr: str) -> str:
    return f"""      try {{
        document.getElementById("demo").innerText = String({expr});
      }} catch (e) {{
        document.getElementById("demo").innerText = e.name + ": " + e.message;
      }}"""


def lines_js(stmts: str) -> str:
    return f"""      const __out = [];
      function show(v) {{ __out.push(String(v)); }}
      try {{
{stmts}
      }} catch (e) {{
        __out.push(e.name + ": " + e.message);
      }}
      document.getElementById("demo").innerText = __out.join("\\n");"""
