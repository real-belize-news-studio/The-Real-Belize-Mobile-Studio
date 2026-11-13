#!/usr/bin/env python3
"""Safely unpack the owner-supplied Mobile Studio review archive."""
from __future__ import annotations
import argparse, shutil, stat, zipfile
from pathlib import Path, PurePosixPath

EXPECTED_ROOT = "real-belize-smart-news-studio"
MAX_COMPRESSED = 25 * 1024 * 1024
MAX_UNCOMPRESSED = 60 * 1024 * 1024
MAX_FILES = 250
BLOCKED_NAMES = {".env", ".env.local", ".env.production", "id_rsa", "id_ed25519"}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True)
    ap.add_argument("--destination", required=True)
    args = ap.parse_args()
    archive = Path(args.archive)
    destination = Path(args.destination)
    if not archive.is_file() or archive.stat().st_size > MAX_COMPRESSED:
        raise SystemExit("Archive missing or larger than the 25 MB import limit.")
    with zipfile.ZipFile(archive) as zf:
        bad = zf.testzip()
        if bad:
            raise SystemExit(f"ZIP integrity failure: {bad}")
        infos = [i for i in zf.infolist() if not i.is_dir()]
        if not infos or len(infos) > MAX_FILES:
            raise SystemExit("Unexpected archive file count.")
        total = sum(i.file_size for i in infos)
        if total > MAX_UNCOMPRESSED:
            raise SystemExit("Archive expands beyond the 60 MB safety limit.")
        checked = []
        for info in infos:
            raw = info.filename.replace("\\", "/")
            path = PurePosixPath(raw)
            if path.is_absolute() or ".." in path.parts or not path.parts:
                raise SystemExit(f"Unsafe archive path: {raw}")
            if path.parts[0] != EXPECTED_ROOT:
                raise SystemExit(f"Unexpected top-level folder: {raw}")
            if any(part in BLOCKED_NAMES or part.startswith(".env.") for part in path.parts):
                raise SystemExit(f"Credential-like file rejected: {raw}")
            mode = (info.external_attr >> 16) & 0xFFFF
            if stat.S_ISLNK(mode):
                raise SystemExit(f"Symbolic link rejected: {raw}")
            relative = Path(*path.parts[1:])
            if not relative.parts:
                continue
            checked.append((info, relative))
        target_root = destination / EXPECTED_ROOT
        if target_root.exists():
            raise SystemExit(f"Destination already exists: {target_root}")
        target_root.mkdir(parents=True, exist_ok=False)
        try:
            for info, relative in checked:
                target = target_root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(info) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
            if not (target_root / "package.json").is_file() or not (target_root / "mobile-newsroom.html").is_file():
                raise SystemExit("Archive did not contain the expected application entry files.")
        except Exception:
            shutil.rmtree(target_root, ignore_errors=True)
            raise
    print(f"Imported {len(checked)} files ({total} uncompressed bytes) to {target_root}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
