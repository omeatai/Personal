"""Append each generated accordion and make one git commit per page."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

PERSONAL = Path(__file__).resolve().parents[3]
JS = PERSONAL / "Files" / "javascript"
TUTORIAL = JS / "tutorial.md"
PLAN = JS / "tutorial_plan.md"
SANDBOX = JS / "code_sandbox"

# (commit_num, plan_title, slug, extra files, accordion already uses JS-prefixed title)
PAGES = [
    ("8.1", "JS Objects", "js-objects", ["_build_s8.py"]),
    ("8.2", "Object Intro", "js-object-intro", []),
    ("8.3", "Object Properties", "js-object-properties", []),
    ("8.4", "Object Methods", "js-object-methods", []),
    ("8.5", "Object this", "js-object-this", []),
    ("8.6", "Object Display", "js-object-display", []),
    ("8.7", "Object Constructors", "js-object-constructors", []),
    ("9.1", "JS Scope", "js-scope", ["_build_s9.py"]),
    ("9.2", "JS Code Blocks", "js-code-blocks", []),
    ("9.3", "JS Hoisting", "js-hoisting", []),
    ("9.4", "JS var/let/const", "js-varletconst", []),
    ("9.5", "JS Strict Mode", "js-strict-mode", []),
    ("10.1", "JS Dates", "js-dates", []),
]


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
    if num == "8.7":
        text = text.replace("- [ ] **S8** Objects (7)", "- [x] **S8** Objects (7)", 1)
    if num == "9.5":
        text = text.replace("- [ ] **S9** Scope (5)", "- [x] **S9** Scope (5)", 1)
    if idx + 1 < len(PAGES):
        nxt = PAGES[idx + 1]
        next_line = f"- **Next task:** `{nxt[0]}` {nxt[1]} (new)."
        last_line = f"- **Last completed:** `{num}` {title}."
    else:
        next_line = "- **Next task:** `10.2` JS Date Formats (new)."
        last_line = "- **Last completed:** `10.1` JS Dates."
    text = re.sub(r"^- \*\*Next task:\*\*.*$", next_line, text, count=1, flags=re.M)
    text = re.sub(r"^- \*\*Last completed:\*\*.*$", last_line, text, count=1, flags=re.M)
    PLAN.write_text(text, encoding="utf-8")


def main() -> None:
    for i, (num, title, slug, extras) in enumerate(PAGES):
        gen = SANDBOX / f"_generated_{slug}.md"
        body = gen.read_text(encoding="utf-8").rstrip() + "\n"
        cur = TUTORIAL.read_text(encoding="utf-8").rstrip() + "\n\n"
        TUTORIAL.write_text(cur + body, encoding="utf-8")
        update_plan(i)
        git("add", "Files/javascript/tutorial.md", "Files/javascript/tutorial_plan.md")
        git("add", f"Files/javascript/code_sandbox/{slug}")
        snaps = sorted((SANDBOX / "snaps").glob(f"{slug}-*-code.png")) + sorted(
            (SANDBOX / "snaps").glob(f"{slug}-*-result.png")
        )
        if not snaps:
            raise SystemExit(f"no snaps for {slug}")
        git("add", *[str(p.relative_to(PERSONAL)).replace("\\", "/") for p in snaps])
        for extra in extras:
            git("add", f"Files/javascript/code_sandbox/{extra}")
        msg = f"{num}: {title} — document JS tutorial section"
        git("commit", "-m", msg)
        print("committed", msg)


if __name__ == "__main__":
    main()
