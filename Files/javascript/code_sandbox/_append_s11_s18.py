"""Append S11–S18 generated accordions and make one git commit per page."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

PERSONAL = Path(__file__).resolve().parents[3]
JS = PERSONAL / "Files" / "javascript"
TUTORIAL = JS / "tutorial.md"
PLAN = JS / "tutorial_plan.md"
SANDBOX = JS / "code_sandbox"

# (commit_num, plan_title as in tutorial_plan.md, slug, extra files)
PAGES = [
    ("11.1", "JS Arrays", "js-arrays", ["_build_s11.py"]),
    ("11.2", "JS Array Constructor", "js-array-constructor", []),
    ("11.3", "JS Array Methods", "js-array-methods", []),
    ("11.4", "JS Array Search", "js-array-search", []),
    ("11.5", "JS Array Sort", "js-array-sort", []),
    ("11.6", "JS Array Iterations", "js-array-iterations", []),
    ("11.7", "JS Array Reference", "js-array-reference", []),
    ("11.8", "JS Array const", "js-array-const", []),
    ("12.1", "JS Sets", "js-sets", ["_build_s12.py"]),
    ("12.2", "JS Set Methods", "js-set-methods", []),
    ("12.3", "JS Set Logic", "js-set-logic", []),
    ("12.4", "JS Set WeakSet", "js-set-weakset", []),
    ("12.5", "JS Set Reference", "js-set-reference", []),
    ("13.1", "JS Maps", "js-maps", []),
    ("13.2", "JS Map Methods", "js-map-methods", []),
    ("13.3", "JS Map WeakMap", "js-map-weakmap", []),
    ("13.4", "JS Map Reference", "js-map-reference", []),
    ("14.1", "JS Iterations", "js-iterations", ["_build_s14.py"]),
    ("14.2", "JS Iterables", "js-iterables", []),
    ("14.3", "JS Iterators", "js-iterators", []),
    ("14.4", "JS Generators", "js-generators", []),
    ("15.1", "JS Math", "js-math", []),
    ("15.2", "JS Math Reference", "js-math-reference", []),
    ("15.3", "JS Math Random", "js-math-random", []),
    ("16.1", "JS RegExp", "js-regexp", ["_build_s16.py"]),
    ("16.2", "JS RegExp Flags", "js-regexp-flags", []),
    ("16.3", "JS RegExp Classes", "js-regexp-classes", []),
    ("16.4", "JS RegExp Metachars", "js-regexp-metachars", []),
    ("16.5", "JS RegExp Assertions", "js-regexp-assertions", []),
    ("16.6", "JS RegExp Groups", "js-regexp-groups", []),
    ("16.7", "JS RegExp Quantifiers", "js-regexp-quantifiers", []),
    ("16.8", "JS RegExp Patterns", "js-regexp-patterns", []),
    ("16.9", "JS RegExp Objects", "js-regexp-objects", []),
    ("16.10", "JS RegExp Methods", "js-regexp-methods", []),
    ("17.1", "JS Data Types", "js-data-types", ["_build_s17.py"]),
    ("17.2", "JS Primitive Data", "js-primitive-data", []),
    ("17.3", "JS Object Types", "js-object-types", []),
    ("17.4", "JS Symbols", "js-symbols", []),
    ("17.5", "JS typeof", "js-typeof", []),
    ("17.6", "JS undefined", "js-undefined", []),
    ("17.7", "JS NaN", "js-nan", []),
    ("17.8", "JS toString()", "js-tostring", []),
    ("17.9", "JS toLocaleString()", "js-tolocalestring", []),
    ("17.10", "JS Type Coercion", "js-type-coercion", []),
    ("17.11", "JS Type Conversion", "js-type-conversion", []),
    ("17.12", "JS Destructuring", "js-destructuring", []),
    ("18.1", "JS Errors Intro", "js-errors-intro", ["_build_s18.py"]),
    ("18.2", "JS Errors Silent", "js-errors-silent", []),
    ("18.3", "JS Error Statements", "js-error-statements", []),
    ("18.4", "JS Error Object", "js-error-object", []),
]

SECTION_DONE = {
    "11.8": ("- [ ] **S11** Arrays (8)", "- [x] **S11** Arrays (8)"),
    "12.5": ("- [ ] **S12** Sets (5)", "- [x] **S12** Sets (5)"),
    "13.4": ("- [ ] **S13** Maps (4)", "- [x] **S13** Maps (4)"),
    "14.4": ("- [ ] **S14** Iterations (4)", "- [x] **S14** Iterations (4)"),
    "15.3": ("- [ ] **S15** Math (3)", "- [x] **S15** Math (3)"),
    "16.10": ("- [ ] **S16** RegExp (10)", "- [x] **S16** RegExp (10)"),
    "17.12": ("- [ ] **S17** Data Types (12)", "- [x] **S17** Data Types (12)"),
    "18.4": ("- [ ] **S18** Errors (4)", "- [x] **S18** Errors (4)"),
}

NEXT_AFTER_LAST = ("19.1", "Debug Intro")


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
    if f"<summary>{title}</summary>" not in body and f"<summary>JS {title}</summary>" not in body:
        # Accordion title should match; warn but continue if slug is in the file.
        if f'id="{slug}-example-01"' not in body:
            raise SystemExit(f"{slug}: generated markdown missing example anchors")
    cur = TUTORIAL.read_text(encoding="utf-8").rstrip() + "\n\n"
    if f"<summary>{title}</summary>" in cur:
        raise SystemExit(f"accordion already exists for {title}")
    TUTORIAL.write_text(cur + body, encoding="utf-8")
    update_plan(idx)
    git("add", "Files/javascript/tutorial.md", "Files/javascript/tutorial_plan.md")
    git("add", f"Files/javascript/code_sandbox/{slug}")
    # ?? so js-math does not also pick up js-math-reference / js-math-random
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
    extra_build = SANDBOX / f"_append_s11_s18.py"
    if idx == 0 and extra_build.is_file():
        git("add", "Files/javascript/code_sandbox/_append_s11_s18.py")
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
