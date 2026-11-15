#!/usr/bin/env python3
"""Initialize records outside the plugin; never draft or overwrite a book."""
import argparse
import json
from pathlib import Path
import shutil
import tempfile

try:
    import yaml
except ImportError:
    raise SystemExit("Missing PyYAML. Install the plugin requirements in a virtual environment.")

PLUGIN = Path(__file__).resolve().parents[1]


def initialize(target, title, profile="generic", dry_run=False):
    target = Path(target).expanduser().resolve()
    if not title.strip():
        raise ValueError("A non-empty book title is required.")
    if profile not in {"generic", "rural-tourism-vi"}:
        raise ValueError("Unsupported profile.")
    if target.exists():
        raise ValueError("Destination already exists; existing work will not be overwritten.")
    boundaries = [PLUGIN]
    # In a standalone skill, resources/ is nested inside the installed skill.
    # Keep manuscripts outside that whole bundle, just as for a Codex plugin.
    if (PLUGIN.parent / "bundle.json").is_file():
        boundaries.append(PLUGIN.parent)
    for ancestor in PLUGIN.parents:
        if (ancestor / ".agents/plugins/marketplace.json").is_file():
            boundaries.append(ancestor)
            break
    if any(target.is_relative_to(base) for base in boundaries):
        raise ValueError("Choose a book directory outside the plugin and its source repository.")
    files = [p.name for p in (PLUGIN / "templates").iterdir()
             if p.is_file() and p.name != "chapter-template.md"]
    if dry_run:
        return {"target": str(target), "profile": profile, "files": sorted(files),
                "directories": ["chapters", "image"], "dry_run": True}
    config_path = PLUGIN / ("templates/book.yaml" if profile == "generic"
                           else "profiles/rural-tourism-vi.yaml")
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    config["title"] = title.strip()
    state = yaml.safe_load((PLUGIN / "templates/state.yaml").read_text(encoding="utf-8"))
    state["plugin_version"] = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))["version"]
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".authoring-init-", dir=target.parent))
    try:
        for name in files:
            shutil.copyfile(PLUGIN / "templates" / name, temporary / name)
        if profile == "rural-tourism-vi":
            shutil.copyfile(PLUGIN / "profiles/rural-tourism-decisions.md", temporary / "decisions.md")
        for name, data in [("book.yaml", config), ("state.yaml", state)]:
            (temporary / name).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        (temporary / "chapters").mkdir()
        (temporary / "image").mkdir()
        # mkdir reserves the destination; copy into our newly-created directory only.
        target.mkdir()
        for child in temporary.iterdir():
            shutil.move(str(child), target / child.name)
    finally:
        shutil.rmtree(temporary, ignore_errors=True)
    return {"target": str(target), "profile": profile, "drafted_chapters": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target")
    parser.add_argument("--title", required=True)
    parser.add_argument("--profile", choices=["generic", "rural-tourism-vi"], default="generic")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        result = initialize(args.target, args.title, args.profile, args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
