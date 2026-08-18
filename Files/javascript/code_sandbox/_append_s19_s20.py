"""Append S19–S20 generated accordions to tutorial2.md; one git commit per page."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

PERSONAL = Path(__file__).resolve().parents[3]
JS = PERSONAL / "Files" / "javascript"
TUTORIAL = JS / "tutorial2.md"
PLAN = JS / "tutorial_plan.md"
SANDBOX = JS / "code_sandbox"

PAGES = [
    ("19.1", "Debug Intro", "js-debugging", ["_build_s19.py"]),
    ("19.2", "Debug Console", "js-debugging-console", []),
    ("19.3", "Debug Breakpoints", "js-debugging-breakpoints", []),
    ("19.4", "Debug Errors", "js-debugging-errors", []),
    ("19.5", "Debug Async", "js-debugging-async", []),
    ("19.6", "Debug Reference", "js-debugging-reference", []),
    ("20.1", "JS Style Guide", "js-style-guide", ["_build_s20.py"]),
    ("20.2", "JS Best Practices", "js-best-practices", []),
    ("20.3", "JS Mistakes", "js-mistakes", []),
    ("20.4", "JS Performance", "js-performance", []),
]

SECTION_DONE = {
    "19.6": ("- [ ] **S19** Debugging (6)", "- [x] **S19** Debugging (6)"),
    "20.4": (
        "- [ ] **S20** Style Guide & Best Practices (4)",
        "- [x] **S20** Style Guide & Best Practices (4)",
    ),
}

NEXT_AFTER_LAST = ("21.1", "JS Alphabetic")


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
    if idx + 1 < len(PAGES):
        nxt = PAGES[idx + 1]
        next_line = f"- **Next task:** `{nxt[0]}` {nxt[1]} (new)."
        last_line = f"- **Last completed:** `{num}` {title}."
    else:
        next_line = f"- **Next task:** `{NEXT_AFTER_LAST[0]}` {NEXT_AFTER_LAST[1]} (new)."
        last_line = f"- **Last completed:** `{num}` {title}."
    text = re.sub(r"^- \*\*Next task:\*\*.*$", next_line, text, count=1, flags=re.M)
    text = re.sub(r"^- \*\*Last completed:\*\*.*$", last_line, text, count=1, flags=re.M)
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
    git("add", "Files/javascript/tutorial2.md", "Files/javascript/tutorial_plan.md")
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
    if idx == 0:
        git("add", "Files/javascript/code_sandbox/_gen_lib.py")
        git("add", "Files/javascript/code_sandbox/_append_s19_s20.py")
    msg = f"{num}: {title} — document JS tutorial section"
    git("commit", "-m", msg)
    print("committed", msg)


def main() -> None:
    import sys

    start = 0
    stop_at: str | None = None
    if len(sys.argv) > 1:
        want = sys.argv[1]
        start = next(i for i, p in enumerate(PAGES) if p[0] == want or p[2] == want)
    if len(sys.argv) > 2:
        stop_at = sys.argv[2]
    for i in range(start, len(PAGES)):
        if not ready(i):
            print("waiting for", PAGES[i][0], PAGES[i][2])
            break
        commit_one(i)
        if stop_at and (PAGES[i][0] == stop_at or PAGES[i][2] == stop_at):
            print("stopped after", PAGES[i][0], PAGES[i][2])
            break


if __name__ == "__main__":
    main()
