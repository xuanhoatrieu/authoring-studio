#!/usr/bin/env python3
"""Build a reproducible plugin-root ZIP and SHA256 file; never publish."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

from validate_repo import ROOT, PLUGIN, validate


def archive_entries(archive, entries):
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, content in sorted(entries.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, content)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".sha256").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return {"archive": str(archive), "sha256": digest, "files": len(entries)}


def build(output):
    report = validate()
    if report["errors"]:
        raise ValueError("Repository validation failed: " + "; ".join(report["errors"]))
    output = Path(output).resolve()
    if output.is_relative_to(PLUGIN):
        raise ValueError("Release output must be outside the packaged plugin.")
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"authoring-studio-{report['version']}.zip"
    entries = {}
    for path in PLUGIN.rglob("*"):
        if path.is_symlink():
            raise ValueError("Symlinks cannot be packaged")
        if path.is_file() and not any(p in {"__pycache__", ".DS_Store", ".venv"} for p in path.parts) and path.suffix != ".pyc":
            entries[path.relative_to(PLUGIN).as_posix()] = path.read_bytes()
    for filename in ["LICENSE", "THIRD_PARTY_NOTICES.md"]:
        entries[filename] = (ROOT / filename).read_bytes()
    entries["PACKAGE.md"] = (ROOT / "docs/package.md").read_bytes()
    result = archive_entries(archive, entries)
    from build_standalone import entries as standalone_entries
    standalone = {"write-book/" + name: content for name, content in standalone_entries().items()}
    result["standalone"] = archive_entries(
        output / f"write-book-standalone-{report['version']}.zip", standalone)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=str(ROOT / "dist"))
    args = parser.parse_args()
    print(json.dumps(build(args.output), ensure_ascii=False, indent=2))
