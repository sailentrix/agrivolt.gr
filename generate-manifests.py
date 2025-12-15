#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FOLDERS = [
  ROOT / "assets" / "isologismoi",
  ROOT / "assets" / "dimosieuseis",
]

ALLOWED_EXT = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".doc", ".docx", ".xlsx"}

def make_manifest(folder: Path):
    folder.mkdir(parents=True, exist_ok=True)
    items = []
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.name != "manifest.json" and p.suffix.lower() in ALLOWED_EXT:
            items.append({"file": p.name})
    (folder / "manifest.json").write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {folder/'manifest.json'} ({len(items)} items)")

def main():
    for f in FOLDERS:
        make_manifest(f)

if __name__ == "__main__":
    main()
