#!/usr/bin/env python3
"""Transcribe local videos to a sibling .txt file.

Implements Personal/.cursor/rules/get_transcripts_from_video.mdc.
Does not download video. Does not commit.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
VIDEO_EXT = {".mp4", ".mkv", ".mov", ".webm", ".m4v", ".avi"}
TEXT_SUBS = {"subrip", "ass", "ssa", "mov_text", "webvtt", "text", "srt", "subviewer"}
WINDOW = 600.0
SAMPLE_RATE = 16000
TS_RE = re.compile(r"\[(\d{1,2}):(\d{2})(?::(\d{2}))?\]")


def find_ffmpeg() -> tuple[str, str]:
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if ffmpeg and ffprobe:
        return ffmpeg, ffprobe
    common = [Path(r"C:\ffmpeg\bin"), Path(r"C:\Program Files\ffmpeg\bin")]
    winget = Path.home() / "AppData/Local/Microsoft/WinGet/Packages"
    if winget.is_dir():
        for entry in winget.iterdir():
            if "FFmpeg" in entry.name or "ffmpeg" in entry.name.lower():
                for exe in entry.rglob("ffmpeg.exe"):
                    common.insert(0, exe.parent)
                    break
    for folder in common:
        ff = folder / "ffmpeg.exe"
        fp = folder / "ffprobe.exe"
        if ff.is_file() and fp.is_file():
            return str(ff), str(fp)
    sys.exit("[error] ffmpeg/ffprobe not found. Install FFmpeg and re-run.")


def enable_cuda_dlls() -> None:
    folders: list[Path] = []
    try:
        import nvidia.cublas as cublas
        import nvidia.cudnn as cudnn

        for mod in (cublas, cudnn):
            bin_dir = Path(mod.__file__).resolve().parent / "bin"
            if bin_dir.is_dir():
                folders.append(bin_dir)
    except Exception:
        pass
    if not folders:
        local = Path.home() / "AppData/Local/Packages"
        if local.is_dir():
            for dll in local.rglob("cublas64_12.dll"):
                folders.append(dll.parent)
                cudnn = dll.parent.parent.parent / "cudnn" / "bin"
                if cudnn.is_dir():
                    folders.append(cudnn)
                break
    for folder in folders:
        if hasattr(os, "add_dll_directory"):
            os.add_dll_directory(str(folder))
        os.environ["PATH"] = str(folder) + os.pathsep + os.environ.get("PATH", "")


def rel_source(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def fmt_ts(seconds: float) -> str:
    total = max(0, int(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"[{hours:02d}:{minutes:02d}:{secs:02d}]"
    return f"[{minutes:02d}:{secs:02d}]"


def parse_ts(line: str) -> float | None:
    match = TS_RE.search(line)
    if not match:
        return None
    hours_or_min, minutes_or_sec, seconds = match.group(1), match.group(2), match.group(3)
    if seconds is None:
        return int(hours_or_min) * 60 + int(minutes_or_sec)
    return int(hours_or_min) * 3600 + int(minutes_or_sec) * 60 + int(seconds)


def last_timestamp(text: str) -> float | None:
    last = None
    for line in text.splitlines():
        stamp = parse_ts(line)
        if stamp is not None:
            last = stamp
    return last


def duration_seconds(ffprobe: str, path: Path) -> float:
    try:
        out = subprocess.check_output(
            [
                ffprobe, "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", str(path),
            ],
            text=True, stderr=subprocess.DEVNULL, timeout=120,
        )
        return float(out.strip() or 0)
    except Exception:
        return 0.0


def subtitle_codecs(ffprobe: str, path: Path) -> list[str]:
    try:
        out = subprocess.check_output(
            [
                ffprobe, "-v", "error", "-select_streams", "s",
                "-show_entries", "stream=codec_name",
                "-of", "csv=p=0", str(path),
            ],
            text=True, stderr=subprocess.DEVNULL, timeout=120,
        )
    except Exception:
        return []
    return [line.strip() for line in out.splitlines() if line.strip()]


def parse_srt(text: str) -> list[tuple[float, str]]:
    cues: list[tuple[float, str]] = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for block in blocks:
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        if len(lines) < 2:
            continue
        time_line = next((ln for ln in lines if "-->" in ln), None)
        if not time_line:
            continue
        start = time_line.split("-->")[0].strip().split()[0]
        parts = start.replace(",", ".").split(":")
        try:
            if len(parts) != 3:
                continue
            seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
        except ValueError:
            continue
        body_lines = [ln for ln in lines if ln != time_line and not ln.isdigit()]
        body = re.sub(r"<[^>]+>", "", " ".join(body_lines))
        body = re.sub(r"\s+", " ", body).strip()
        if body:
            cues.append((seconds, body))
    return cues


def extract_subtitle(ffmpeg: str, path: Path) -> list[tuple[float, str]] | None:
    tmp = path.with_suffix(".extract.srt")
    try:
        proc = subprocess.run(
            [ffmpeg, "-y", "-i", str(path), "-map", "0:s:0", str(tmp)],
            capture_output=True, text=True, timeout=300,
        )
        if proc.returncode != 0 or not tmp.is_file() or tmp.stat().st_size == 0:
            return None
        return parse_srt(tmp.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None
    finally:
        if tmp.is_file():
            tmp.unlink()


def header(title: str, source: str, kind: str) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"# {title}\n\n"
        f"Source: {source}\n"
        f"Fetched On: {now}\n"
        f"Language: English\n"
        f"Transcript Type: {kind}\n\n"
        f"---\n\n"
    )


def is_complete(text: str, duration: float) -> bool:
    if not text.strip() or "Transcript not available" in text:
        return False
    last = last_timestamp(text)
    if last is None:
        return False
    if duration <= 0:
        return False
    return last >= max(0.0, duration - 45.0)


def is_compilation(path: Path) -> bool:
    return path.name.upper().startswith("MERGED")


def source_clips(folder: Path) -> list[Path]:
    clips = []
    if not folder.is_dir():
        return clips
    for path in folder.iterdir():
        if path.is_file() and path.suffix.lower() in VIDEO_EXT and not is_compilation(path):
            clips.append(path)
    return clips


def collect(dirs: list[Path], files: list[Path]) -> list[Path]:
    found: list[Path] = []
    for file_path in files:
        path = file_path if file_path.is_absolute() else (ROOT / file_path)
        if path.is_dir():
            dirs.append(path)
            continue
        if path.is_file() and path.suffix.lower() in VIDEO_EXT:
            found.append(path)
    for directory in dirs:
        folder = directory if directory.is_absolute() else (ROOT / directory)
        if not folder.is_dir():
            print(f"[error] folder not found: {folder}", flush=True)
            continue
        for path in folder.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in VIDEO_EXT:
                continue
            if "OLD_FILES" in path.parts:
                continue
            found.append(path)
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in found:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(resolved)
    return unique


def pcm_cache_path(video: Path, duration: float) -> Path:
    key = f"{video.resolve()}|{video.stat().st_size}|{duration:.3f}"
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:20]
    folder = Path(tempfile.gettempdir()) / "personal-video-transcripts"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{digest}.s16le"


def extract_pcm(ffmpeg: str, video: Path, dest: Path, duration: float) -> None:
    expected = int(duration * SAMPLE_RATE) * 2
    if dest.is_file() and expected > 0 and abs(dest.stat().st_size - expected) < SAMPLE_RATE * 4:
        print(f"    reuse audio cache {dest.name}", flush=True)
        return
    print("    extracting mono 16 kHz audio", flush=True)
    proc = subprocess.run(
        [
            ffmpeg, "-nostdin", "-y", "-v", "error",
            "-i", str(video),
            "-f", "s16le", "-acodec", "pcm_s16le",
            "-ac", "1", "-ar", str(SAMPLE_RATE),
            str(dest),
        ],
        capture_output=True, timeout=max(600, int(duration) + 600),
    )
    if proc.returncode != 0 or not dest.is_file():
        err = proc.stderr.decode("utf-8", errors="replace")[-800:]
        raise RuntimeError(f"ffmpeg audio extract failed: {err}")


def read_window(pcm: Path, start: float, seconds: float) -> np.ndarray:
    start_sample = max(0, int(start * SAMPLE_RATE))
    n_samples = max(0, int(seconds * SAMPLE_RATE))
    with pcm.open("rb") as handle:
        handle.seek(start_sample * 2)
        raw = handle.read(n_samples * 2)
    if len(raw) < 2:
        return np.zeros(0, dtype=np.float32)
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0
    return np.ascontiguousarray(audio)


class Transcriber:
    def __init__(self) -> None:
        self.model = None
        self.batched = None
        self.model_name = ""
        self.device = ""
        self.batch_size = 4
        self.use_batch = True

    def load(self) -> None:
        enable_cuda_dlls()
        try:
            from faster_whisper import BatchedInferencePipeline, WhisperModel
        except ImportError:
            print("[setup] installing faster-whisper ...", flush=True)
            subprocess.check_call([sys.executable, "-m", "pip", "install", "faster-whisper"])
            from faster_whisper import BatchedInferencePipeline, WhisperModel

        errors = []
        for name, device, compute in (
            ("distil-large-v3", "cuda", "float16"),
            ("small.en", "cuda", "float16"),
            ("small.en", "cpu", "int8"),
        ):
            try:
                print(f"[setup] loading {name} on {device} ({compute})", flush=True)
                model = WhisperModel(name, device=device, compute_type=compute)
                silence = np.zeros(SAMPLE_RATE, dtype=np.float32)
                list(model.transcribe(silence, language="en", beam_size=1, vad_filter=False)[0])
                self.model = model
                self.batched = BatchedInferencePipeline(model=model)
                self.model_name = name
                self.device = device
                print(f"[setup] ready {name} on {device}", flush=True)
                return
            except Exception as exc:
                errors.append(f"{name}/{device}: {exc}")
                print(f"[setup] {name} on {device} failed: {exc}", flush=True)
                self.model = None
                self.batched = None
        raise RuntimeError("faster-whisper could not load a model. " + " | ".join(errors))

    def transcribe_window(self, audio: np.ndarray) -> list[tuple[float, str]]:
        assert self.model is not None
        kwargs = dict(
            language="en",
            vad_filter=True,
            beam_size=1,
            condition_on_previous_text=False,
            temperature=0.0,
            without_timestamps=False,
        )
        if self.use_batch and self.batched is not None:
            try:
                segments, _info = self.batched.transcribe(audio, batch_size=self.batch_size, **kwargs)
                return self._cues(segments)
            except RuntimeError as exc:
                message = str(exc).lower()
                if "memory" in message and self.batch_size > 1:
                    self.batch_size = max(1, self.batch_size // 2)
                    print(f"    [setup] lowering batch size to {self.batch_size}", flush=True)
                    segments, _info = self.batched.transcribe(audio, batch_size=self.batch_size, **kwargs)
                    return self._cues(segments)
                print(f"    [setup] batched inference failed, using segment API: {exc}", flush=True)
                self.use_batch = False
        segments, _info = self.model.transcribe(audio, **kwargs)
        return self._cues(segments)

    @staticmethod
    def _cues(segments) -> list[tuple[float, str]]:
        cues = []
        for seg in segments:
            text = re.sub(r"\s+", " ", (seg.text or "")).strip()
            if text:
                cues.append((float(seg.start), text))
        return cues


def write_summary(folder: Path, rows: list[dict]) -> None:
    ok = [row for row in rows if row["status"] == "transcribed"]
    skipped = [row for row in rows if row["status"] == "skipped"]
    failed = [row for row in rows if row["status"] == "failed"]
    lines = [
        "# Transcript summary",
        "",
        f"- Considered: {len(rows)}",
        f"- Transcribed: {len(ok)}",
        f"- Skipped: {len(skipped)}",
        f"- Failed: {len(failed)}",
        "",
        "## Files",
        "",
    ]
    for row in rows:
        lines.append(f"- {row['status']}: `{row['out']}` — {row['source']} — {row['note']}")
    (folder / "transcript_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_cues(out: Path, cues: list[tuple[float, str]], previous: str) -> str:
    fresh = []
    last_text = ""
    for line in reversed(previous.splitlines()):
        if parse_ts(line) is not None:
            last_text = line.split("]", 1)[-1].strip()
            break
    last_stamp = last_timestamp(previous) or -1.0
    for start, text in cues:
        if start <= last_stamp + 0.4:
            continue
        if text == last_text:
            continue
        fresh.append(f"{fmt_ts(start)} {text}")
        last_text = text
        last_stamp = start
    if not fresh:
        return previous
    addition = "\n".join(fresh) + "\n"
    with out.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(addition)
    return previous + addition


def transcribe_file(
    engine: Transcriber,
    ffmpeg: str,
    ffprobe: str,
    video: Path,
    until: float | None,
) -> tuple[str, str]:
    out = video.with_suffix(".txt")
    source = rel_source(video)
    duration = duration_seconds(ffprobe, video)
    limit = duration if until is None else min(duration or until, until)
    existing = out.read_text(encoding="utf-8", errors="replace") if out.is_file() else ""
    if existing and is_complete(existing, duration if until is None else limit):
        return "skipped", "transcript already complete"
    if existing and "Transcript not available" in existing:
        existing = ""
    if existing and last_timestamp(existing) is None:
        existing = ""

    codecs = [codec for codec in subtitle_codecs(ffprobe, video) if codec in TEXT_SUBS]
    if codecs and not existing:
        cues = extract_subtitle(ffmpeg, video)
        if cues:
            body = "\n".join(f"{fmt_ts(start)} {text}" for start, text in cues)
            kind = f"Embedded subtitles ({', '.join(codecs)})"
            out.write_text(header(video.stem, source, kind) + body + "\n", encoding="utf-8", newline="\n")
            return "transcribed", kind

    kind = f"Local whisper ({engine.model_name}, {engine.device})"
    if not existing:
        out.write_text(header(video.stem, source, kind), encoding="utf-8", newline="\n")
        existing = out.read_text(encoding="utf-8")
    elif f"Transcript Type: {kind}" not in existing and "Transcript Type:" in existing:
        existing = re.sub(r"Transcript Type:.*", f"Transcript Type: {kind}", existing, count=1)
        out.write_text(existing, encoding="utf-8", newline="\n")

    pcm = pcm_cache_path(video, duration)
    extract_pcm(ffmpeg, video, pcm, duration)
    start = last_timestamp(existing)
    start = 0.0 if start is None else max(0.0, start - 1.0)
    target = limit if limit > 0 else WINDOW
    previous_text = ""
    while start < target - 0.25:
        audio = read_window(pcm, start, WINDOW)
        if audio.size < SAMPLE_RATE:
            break
        began = dt.datetime.now()
        cues = [(start + stamp, text) for stamp, text in engine.transcribe_window(audio)]
        existing = append_cues(out, cues, existing)
        elapsed = (dt.datetime.now() - began).total_seconds()
        done = min(target, start + WINDOW)
        rate = (min(WINDOW, target - start) / elapsed) if elapsed else 0
        print(f"    chunk through {fmt_ts(done)}  ({elapsed:.1f}s, {rate:.1f}x)", flush=True)
        if cues:
            tail = cues[-1][1]
            if tail == previous_text and len(cues) > 3:
                print("    [warn] repeated window text", flush=True)
            previous_text = tail
        start += WINDOW
    final = out.read_text(encoding="utf-8", errors="replace")
    if last_timestamp(final) is None:
        raise RuntimeError("no speech cues returned")
    return "transcribed", kind


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe local videos to sibling .txt files")
    parser.add_argument("--file", action="append", default=[], type=Path, help="One video file")
    parser.add_argument("--dir", action="append", default=[], type=Path, help="Folder of videos")
    parser.add_argument("--until-seconds", type=float, default=None, help="Stop early (debug)")
    args = parser.parse_args()
    if not args.file and not args.dir:
        parser.error("pass --file and/or --dir")

    ffmpeg, ffprobe = find_ffmpeg()
    print(f"[setup] ffmpeg {ffmpeg}", flush=True)
    videos = collect(list(args.dir), list(args.file))
    jobs = []
    rows: dict[Path, list[dict]] = {}

    for video in videos:
        folder = video.parent
        if is_compilation(video) and source_clips(folder):
            rows.setdefault(folder, []).append({
                "status": "skipped",
                "out": video.with_suffix(".txt").name,
                "source": rel_source(video),
                "note": "compilation and source clips are both in this folder",
            })
            continue
        duration = duration_seconds(ffprobe, video)
        out = video.with_suffix(".txt")
        existing = out.read_text(encoding="utf-8", errors="replace") if out.is_file() else ""
        if is_complete(existing, duration):
            rows.setdefault(folder, []).append({
                "status": "skipped",
                "out": out.name,
                "source": rel_source(video),
                "note": "transcript already complete",
            })
            continue
        jobs.append((video, duration))

    jobs.sort(key=lambda item: (item[1], str(item[0]).lower()))
    print(
        f"[queue] {len(jobs)} videos to transcribe, "
        f"{sum(len(v) for v in rows.values())} skipped",
        flush=True,
    )
    hours = sum(item[1] for item in jobs) / 3600
    print(f"[queue] about {hours:.1f} hours of audio", flush=True)
    if not jobs:
        for folder, folder_rows in rows.items():
            write_summary(folder, folder_rows)
        print("[done] nothing to transcribe", flush=True)
        return 0

    try:
        engine = Transcriber()
        engine.load()
    except Exception as exc:
        summary = ROOT / "course_videos" / "local_transcript_summary.md"
        summary.parent.mkdir(parents=True, exist_ok=True)
        summary.write_text(
            "# Local transcript summary\n\n"
            "Transcription did not start.\n\n"
            f"Reason: {exc}\n",
            encoding="utf-8",
        )
        print(f"[error] {exc}", flush=True)
        return 1

    for index, (video, duration) in enumerate(jobs, start=1):
        print(f"[{index}/{len(jobs)}] {duration / 60:.1f} min  {rel_source(video)}", flush=True)
        status = "transcribed"
        note = ""
        try:
            status, note = transcribe_file(engine, ffmpeg, ffprobe, video, args.until_seconds)
        except Exception as exc:
            status = "failed"
            note = str(exc)
            out = video.with_suffix(".txt")
            existing = out.read_text(encoding="utf-8", errors="replace") if out.is_file() else ""
            if last_timestamp(existing) is None:
                out.write_text(
                    header(video.stem, rel_source(video), "Unavailable")
                    + f"Transcript not available for: {video.stem}\nReason: {exc}\n",
                    encoding="utf-8",
                    newline="\n",
                )
            print(f"    FAILED {exc}", flush=True)
        rows.setdefault(video.parent, []).append({
            "status": status,
            "out": video.with_suffix(".txt").name,
            "source": rel_source(video),
            "note": note,
        })
        write_summary(video.parent, rows[video.parent])

    for folder, folder_rows in rows.items():
        write_summary(folder, folder_rows)
    print("[done] batch finished", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
