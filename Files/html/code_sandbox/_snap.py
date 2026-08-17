"""Screenshot sandbox pages and W3Schools-style example boxes via Chrome headless."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAPS = ROOT / "snaps"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
CODEVIEW = ROOT / "_codeview_static.html"

TAG_RE = re.compile(r"(&lt;\/?[a-zA-Z0-9]+(?:\s[^&]*?)?&gt;)")


def highlight(src: str) -> str:
    esc = html.escape(src)
    return TAG_RE.sub(r'<span class="t">\1</span>', esc)


def write_codeview(snippet: str) -> None:
    inner = highlight(snippet.rstrip() + "\n")
    CODEVIEW.write_text(
        f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Example</title>
<style>
html, body {{ background:#fff; margin:0; }}
#snap-target {{
  display:inline-block;
  background:#E7E9EB;
  padding:16px 16px 20px;
  font-family:Verdana,Geneva,sans-serif;
  min-width:420px;
}}
h3 {{ margin:0 0 12px; font-size:20px; font-weight:bold; }}
.box {{
  background:#fff;
  border-left:4px solid #04AA6D;
  padding:8px 16px;
  font-family:Consolas,"Courier New",monospace;
  font-size:15px;
  line-height:1.45;
  color:#000;
  white-space:pre-wrap;
  overflow-wrap:anywhere;
}}
.t {{ color:#880055; }}
.btn {{
  display:inline-block;
  margin-top:12px;
  background:#04AA6D;
  color:#fff;
  padding:8px 16px;
  border-radius:5px;
  font-size:15px;
}}
</style>
</head>
<body>
<div id="snap-target">
  <h3>Example</h3>
  <div class="box">{inner}</div>
  <div class="btn">Try it Yourself »</div>
</div>
</body>
</html>
""",
        encoding="utf-8",
    )


def chrome_shot(url: str, out: Path, size: str = "800,500") -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--virtual-time-budget=3000",
        f"--window-size={size}",
        f"--screenshot={out}",
        url,
    ]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


def snap_result(path: str, name: str, size: str = "800,500") -> None:
    chrome_shot(f"http://127.0.0.1:8766/{path}", SNAPS / name, size)


def snap_code(snippet: str, name: str, size: str = "700,420") -> None:
    write_codeview(snippet)
    chrome_shot("http://127.0.0.1:8766/_codeview_static.html", SNAPS / name, size)


if __name__ == "__main__":
    # usage:
    #   python _snap.py result html-block-inline/ index.html-block-inline-result.png
    #   python _snap.py code html-block-inline-code.png <<'EOF' ... EOF
    mode = sys.argv[1]
    if mode == "result":
        snap_result(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "800,500")
    elif mode == "code":
        snippet = sys.stdin.read()
        snap_code(snippet, sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "700,420")
    else:
        raise SystemExit("mode must be result or code")
