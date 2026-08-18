"""Append S22 JS Projects accordions to tutorial2.md; one git commit per page."""
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
    ("22.1", "JS Counter", "js-counter", ["_build_s22.py"]),
    ("22.2", "JS Event Listener (Project)", "js-event-listener", []),
    ("22.3", "JS To-Do List", "js-todo-list", []),
    ("22.4", "JS Modal Popup", "js-modal-popup", []),
    ("22.5", "JS Form Validation (Project)", "js-form-validation", []),
]

ACCORDION_TITLE = {
    "js-event-listener": "JS Event Listener",
    "js-form-validation": "JS Form Validation",
}

SECTION_DONE = {
    "22.5": ("- [ ] **S22** Projects (5)", "- [x] **S22** Projects (5)"),
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
    # S21 is still open — keep the course pointer there.
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
    summary = ACCORDION_TITLE.get(slug, title)
    cur = TUTORIAL.read_text(encoding="utf-8").rstrip() + "\n\n"
    if f"<summary>{summary}</summary>" in cur:
        raise SystemExit(f"accordion already exists for {summary}")
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
        git("add", "Files/javascript/code_sandbox/_append_s22.py")
    msg = f"{num}: {title} — document JS tutorial section"
    git("commit", "-m", msg)
    print("committed", msg)


def main() -> None:
    for i, page in enumerate(PAGES):
        if not ready(i):
            print("waiting for", page[0], page[2])
            break
        commit_one(i)


if __name__ == "__main__":
    main()
