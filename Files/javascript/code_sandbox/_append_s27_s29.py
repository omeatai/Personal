"""Append S27–S29 accordions to tutorial3.md; one git commit per page."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

PERSONAL = Path(__file__).resolve().parents[3]
JS = PERSONAL / "Files" / "javascript"
TUTORIAL = JS / "tutorial3.md"
PLAN = JS / "tutorial_plan.md"
SANDBOX = JS / "code_sandbox"

PAGES = [
    ("27.1", "JS Window", "js-window", ["_build_s27.py", "_gen_lib.py", "_append_s27_s29.py"]),
    ("27.2", "JS Screen", "js-screen", []),
    ("27.3", "JS Location", "js-location", []),
    ("27.4", "JS History", "js-history", []),
    ("27.5", "JS Navigator", "js-navigator", []),
    ("27.6", "JS Popup Alert", "js-popup-alert", []),
    ("27.7", "JS Cookies", "js-cookies", []),
    ("27.8", "JS Fetch API", "js-fetch-api", ["_build_s27.py"]),
    ("28.1", "JSON Intro", "json-intro", ["_build_s28.py"]),
    ("28.2", "JSON Syntax", "json-syntax", []),
    ("28.3", "JSON Values", "json-values", []),
    ("28.4", "JSON Parse", "json-parse", []),
    ("28.5", "JSON Stringify", "json-stringify", []),
    ("28.6", "JSON Fetch", "json-fetch", []),
    ("28.7", "JSON HTML", "json-html", []),
    ("28.8", "JSON vs XML", "json-vs-xml", ["_build_s28.py"]),
    ("29.1", "APIs Intro", "apis-intro", ["_build_s29.py"]),
    ("29.2", "API Geolocation", "api-geolocation", []),
    ("29.3", "API Web Pointer", "api-web-pointer", []),
    ("29.4", "API Web Storage", "api-web-storage", []),
    ("29.5", "API Validation", "api-validation", []),
    ("29.6", "API Web Worker", "api-web-worker", ["_build_s29.py"]),
]

SECTION_DONE = {
    "27.8": ("- [ ] **S27** JS Window API / BOM (8)", "- [x] **S27** JS Window API / BOM (8)"),
    "28.8": ("- [ ] **S28** JS JSON (8)", "- [x] **S28** JS JSON (8)"),
    "29.6": ("- [ ] **S29** JS Web API (6)", "- [x] **S29** JS Web API (6)"),
}

NEXT_AFTER = {
    "27.8": "`28.1` JSON Intro (new).",
    "28.8": "`29.1` APIs Intro (new).",
    "29.6": "`21.1` JS Alphabetic (new).",
}


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=PERSONAL, check=True)


def update_plan(idx: int) -> None:
    text = PLAN.read_text(encoding="utf-8")
    num, title, slug, _ = PAGES[idx]
    old = f"- [ ] `{num}` {title}"
    new = f"- [x] `{num}` {title}"
    if old not in text:
        raise SystemExit(f"plan line not found: {old}")
    text = text.replace(old, new, 1)
    if num in SECTION_DONE:
        a, b = SECTION_DONE[num]
        text = text.replace(a, b, 1)
    nxt = NEXT_AFTER.get(num)
    if nxt:
        text = re.sub(
            r"^- \*\*Next task:\*\*.*$",
            f"- **Next task:** {nxt}",
            text,
            count=1,
            flags=re.M,
        )
    else:
        following = PAGES[idx + 1]
        text = re.sub(
            r"^- \*\*Next task:\*\*.*$",
            f"- **Next task:** `{following[0]}` {following[1]} (new).",
            text,
            count=1,
            flags=re.M,
        )
    text = re.sub(
        r"^- \*\*Last completed:\*\*.*$",
        f"- **Last completed:** `{num}` {title}.",
        text,
        count=1,
        flags=re.M,
    )
    PLAN.write_text(text, encoding="utf-8")


def ready(idx: int) -> bool:
    _, _, slug, _ = PAGES[idx]
    gen = SANDBOX / f"_generated_{slug}.md"
    if not gen.is_file():
        return False
    snaps = list((SANDBOX / "snaps").glob(f"{slug}-??-code.png"))
    return bool(snaps)


def commit_one(idx: int) -> None:
    num, title, slug, extras = PAGES[idx]
    gen = SANDBOX / f"_generated_{slug}.md"
    body = gen.read_text(encoding="utf-8").rstrip() + "\n"
    if f'id="{slug}-example-01"' not in body:
        raise SystemExit(f"{slug}: generated markdown missing example anchors")
    cur = TUTORIAL.read_text(encoding="utf-8").rstrip() + "\n\n"
    if f"<summary>{title}</summary>" in cur:
        raise SystemExit(f"accordion already exists for {title}")
    TUTORIAL.write_text(cur + body, encoding="utf-8")
    update_plan(idx)
    git("add", "Files/javascript/tutorial3.md", "Files/javascript/tutorial_plan.md")
    git("add", f"Files/javascript/code_sandbox/{slug}")
    snaps = sorted((SANDBOX / "snaps").glob(f"{slug}-??-code.png")) + sorted(
        (SANDBOX / "snaps").glob(f"{slug}-??-result.png")
    )
    if not snaps:
        raise SystemExit(f"no snaps for {slug}")
    git("add", *[str(p.relative_to(PERSONAL)).replace("\\", "/") for p in snaps])
    for extra in extras:
        p = SANDBOX / extra
        if p.is_file():
            git("add", f"Files/javascript/code_sandbox/{extra}")
    msg = f"{num}: {title} — document JS tutorial section"
    git("commit", "-m", msg)
    print("committed", msg)


def main() -> None:
    for i, page in enumerate(PAGES):
        if not ready(i):
            print("waiting for", page[0], page[2])
            break
        title = page[1]
        if f"<summary>{title}</summary>" in TUTORIAL.read_text(encoding="utf-8"):
            print("already present", page[0], title)
            continue
        commit_one(i)


if __name__ == "__main__":
    main()
