#!/usr/bin/env python3
"""
Cursor-based Udemy Transcript Saver

This is a helper script called by the Cursor agent after extracting
the transcript via the browser MCP. It saves raw transcript text to
the notes/ directory.

Usage (called programmatically):
    python cursor_transcript.py --title "Lecture Title" --url "<url>" --output notes/filename.txt

    Then pipe transcript text via stdin.
"""

import sys
import re
import argparse
from pathlib import Path

NOTES_DIR = Path(__file__).parent / "notes"


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "_", name.strip())
    return name[:100]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", help="Override output filename")
    args = parser.parse_args()

    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    transcript = sys.stdin.read().strip()
    if not transcript:
        print("No transcript provided on stdin.", file=sys.stderr)
        sys.exit(1)

    filename = args.output or (sanitize_filename(args.title) + ".txt")
    filepath = NOTES_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Lecture: {args.title}\n")
        f.write(f"URL: {args.url}\n")
        f.write("=" * 60 + "\n\n")
        f.write(transcript)

    print(f"Saved: {filepath}")


if __name__ == "__main__":
    main()
