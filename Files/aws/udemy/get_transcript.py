#!/usr/bin/env python3
"""
Udemy Transcript Extractor

Usage:
    python get_transcript.py <udemy_lecture_url>

Extracts the transcript from a Udemy video lecture and saves it
as a .txt file in the ./notes/ directory.

Requirements:
    pip install selenium webdriver-manager

You must be logged into Udemy in Chrome for this to work
(uses your existing Chrome profile cookies).
"""

import sys
import os
import re
import time
import json
import argparse
from pathlib import Path

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install selenium webdriver-manager")
    sys.exit(1)

NOTES_DIR = Path(__file__).parent / "notes"


def parse_url(url: str) -> dict:
    """Extract course slug and lecture ID from a Udemy URL."""
    pattern = r"udemy\.com/course/([^/]+)/learn/lecture/(\d+)"
    match = re.search(pattern, url)
    if not match:
        print(f"Error: Could not parse Udemy lecture URL:\n  {url}")
        print("Expected format: https://www.udemy.com/course/<slug>/learn/lecture/<id>")
        sys.exit(1)
    return {"course_slug": match.group(1), "lecture_id": match.group(2)}


def get_chrome_profile_dir() -> str:
    """Return the default Chrome user-data directory for the current OS."""
    home = Path.home()
    if sys.platform == "darwin":
        return str(home / "Library/Application Support/Google/Chrome")
    elif sys.platform.startswith("linux"):
        return str(home / ".config/google-chrome")
    elif sys.platform == "win32":
        return str(home / "AppData/Local/Google/Chrome/User Data")
    return ""


def extract_transcript(url: str, headless: bool = True) -> tuple[str, str]:
    """
    Open the Udemy lecture in Chrome (reusing login session),
    click the transcript button, and scrape the transcript text.

    Returns (lecture_title, transcript_text).
    """
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,900")

    # Reuse Chrome profile so Udemy session cookies are available
    profile_dir = get_chrome_profile_dir()
    if profile_dir and Path(profile_dir).exists():
        opts.add_argument(f"--user-data-dir={profile_dir}")
        opts.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts,
    )

    try:
        print(f"Loading lecture page...")
        driver.get(url)

        # Wait for the video player area to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-purpose='curriculum-item-viewer-content']"))
        )
        time.sleep(3)

        # Get lecture title from the page
        title = "untitled"
        try:
            title_el = driver.find_element(
                By.CSS_SELECTOR,
                "[data-purpose='lecture-title'], .ud-heading-xl, h1"
            )
            title = title_el.text.strip()
        except Exception:
            try:
                title = driver.title.split("|")[0].strip()
            except Exception:
                pass

        # Try to open the transcript panel
        # Udemy has a transcript toggle button in the video controls
        transcript_opened = False
        try:
            # Look for transcript/CC button
            transcript_btn = driver.find_element(
                By.CSS_SELECTOR,
                "[data-purpose='transcript-toggle'], button[aria-label*='transcript' i], button[aria-label*='Transcript' i]"
            )
            transcript_btn.click()
            time.sleep(2)
            transcript_opened = True
        except Exception:
            pass

        if not transcript_opened:
            # Try clicking the "Transcript" text if it appears as a panel header or tab
            try:
                elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Transcript')]")
                for el in elements:
                    if el.is_displayed() and el.tag_name in ("button", "span", "div", "a"):
                        el.click()
                        time.sleep(2)
                        transcript_opened = True
                        break
            except Exception:
                pass

        # Now extract transcript text
        transcript_text = ""

        # Method 1: Look for transcript container with cue elements
        try:
            cues = driver.find_elements(
                By.CSS_SELECTOR,
                "[data-purpose='transcript-cue-container'] button span, "
                "[class*='transcript'] button span, "
                "[class*='transcript--cue-text']"
            )
            if cues:
                transcript_text = "\n".join(c.text.strip() for c in cues if c.text.strip())
        except Exception:
            pass

        # Method 2: Broader search for transcript region
        if not transcript_text:
            try:
                region = driver.find_element(
                    By.CSS_SELECTOR,
                    "[role='region'][aria-label*='transcript' i], "
                    "[data-purpose='transcript-panel'], "
                    "[class*='transcript--panel']"
                )
                transcript_text = region.text.strip()
            except Exception:
                pass

        # Method 3: Use Udemy's internal API
        if not transcript_text:
            try:
                info = parse_url(url)
                # Try fetching captions via Udemy's asset API
                script = """
                return fetch('/api-2.0/lectures/{lid}/captions/?format=json', {{
                    credentials: 'include'
                }}).then(r => r.json());
                """.replace("{lid}", info["lecture_id"])
                captions_data = driver.execute_script(script)
                if isinstance(captions_data, dict) and "results" in captions_data:
                    for cap in captions_data["results"]:
                        if cap.get("locale_id", "").startswith("en"):
                            cap_url = cap.get("url", "")
                            if cap_url:
                                vtt = driver.execute_script(
                                    f"return fetch('{cap_url}').then(r => r.text());"
                                )
                                # Parse VTT to plain text
                                lines = []
                                for line in vtt.split("\n"):
                                    line = line.strip()
                                    if (
                                        line
                                        and not line.startswith("WEBVTT")
                                        and not line.startswith("NOTE")
                                        and "-->" not in line
                                        and not line.isdigit()
                                    ):
                                        lines.append(line)
                                transcript_text = "\n".join(lines)
                                break
            except Exception:
                pass

        if not transcript_text:
            print("Warning: Could not extract transcript. The lecture may not have captions.")
            print("Make sure you are logged into Udemy in Chrome.")
            return title, ""

        return title, transcript_text

    finally:
        driver.quit()


def sanitize_filename(name: str) -> str:
    """Convert a title into a safe filename."""
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "_", name.strip())
    name = name[:100]  # limit length
    return name


def main():
    parser = argparse.ArgumentParser(description="Extract Udemy lecture transcript")
    parser.add_argument("url", help="Full Udemy lecture URL")
    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Show the browser window (useful for debugging)",
    )
    args = parser.parse_args()

    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    title, transcript = extract_transcript(args.url, headless=not args.no_headless)

    if not transcript:
        print("No transcript found. Exiting.")
        sys.exit(1)

    filename = sanitize_filename(title) + ".txt"
    filepath = NOTES_DIR / filename

    # Write transcript
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Lecture: {title}\n")
        f.write(f"URL: {args.url}\n")
        f.write("=" * 60 + "\n\n")
        f.write(transcript)

    print(f"\nTranscript saved to: {filepath}")
    print(f"  Title: {title}")
    print(f"  Lines: {len(transcript.splitlines())}")


if __name__ == "__main__":
    main()
