"""Append S24–S26 accordions to tutorial2.md; one git commit per page."""
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
    ("24.1", "HTML DOM", "html-dom", ["_dom_ui.py", "_build_s24.py", "_append_s24_s26.py", "_gen_lib.py"]),
    ("24.2", "HTML DOM API", "html-dom-api", []),
    ("24.3", "Selecting Elements", "selecting-elements", []),
    ("24.4", "Changing HTML", "changing-html", []),
    ("24.5", "Changing CSS", "changing-css", []),
    ("24.6", "Form Validation", "form-validation", []),
    ("24.7", "DOM Animations", "dom-animations", []),
    ("24.8", "Document Reference", "document-reference", ["_build_s24_ref.py"]),
    ("24.9", "Element Reference", "element-reference", []),
    ("25.1", "Intro to Events", "intro-to-events", ["_build_s25.py"]),
    ("25.2", "Mouse Events", "mouse-events", []),
    ("25.3", "Keyboard Events", "keyboard-events", []),
    ("25.4", "Load Events", "load-events", []),
    ("25.5", "Manage Events", "manage-events", []),
    ("25.6", "Event Examples", "event-examples", []),
    ("25.7", "Event Listener", "event-listener", []),
    ("26.1", "HTML First", "html-first", ["_build_s26.py"]),
    ("26.2", "HTML Progressive", "html-progressive", []),
    ("26.3", "HTML First Features", "html-first-features", []),
    ("26.4", "HTML First CSS", "html-first-css", []),
]

SECTION_DONE = {
    "24.9": ("- [ ] **S24** JS HTML DOM (9)", "- [x] **S24** JS HTML DOM (9)"),
    "25.7": ("- [ ] **S25** JS HTML Events (7)", "- [x] **S25** JS HTML Events (7)"),
    "26.4": ("- [ ] **S26** JS HTML First (4)", "- [x] **S26** JS HTML First (4)"),
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
    text = re.sub(
        r"^- \*\*Next task:\*\*.*$",
        "- **Next task:** `21.1` JS Alphabetic (new).",
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
    msg = f"{num}: {title} — document JS tutorial section"
    git("commit", "-m", msg)
    print("committed", msg)


def main() -> None:
    for i, page in enumerate(PAGES):
        if not ready(i):
            print("waiting for", page[0], page[2])
            break
        # Skip if already committed (accordion exists)
        title = page[1]
        if f"<summary>{title}</summary>" in TUTORIAL.read_text(encoding="utf-8"):
            print("already present", page[0], title)
            continue
        commit_one(i)


if __name__ == "__main__":
    main()
