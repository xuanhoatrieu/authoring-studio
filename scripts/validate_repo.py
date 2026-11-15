#!/usr/bin/env python3
"""Validate the repository's release contract without changing files."""
import argparse
import json
from pathlib import Path
import re
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/authoring-studio"


def validate(tag=None):
    errors = []
    manifest = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    legacy = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?", version):
        errors.append("Invalid release version")
    if (legacy["name"], legacy["version"]) != (manifest["name"], version):
        errors.append("Portable and compatibility manifest identities differ")
    if legacy.get("skills") != "./skills/":
        errors.append("Compatibility skill path is invalid")
    if tag and tag != "v" + version:
        errors.append("Release tag and manifest version differ")
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    for entry in marketplace["plugins"]:
        target = (ROOT / entry["source"]["path"]).resolve()
        if not target.is_relative_to(ROOT) or not (target / "plugin.json").is_file():
            errors.append("Marketplace points outside repo or to a missing plugin")
        elif entry["name"] != json.loads((target / "plugin.json").read_text(encoding="utf-8"))["name"]:
            errors.append("Marketplace/plugin names differ")
    skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
    if len(skills) != 1 or skills[0].parent.name != "write-book":
        errors.append("Package must contain only the implemented write-book skill")
    for skill in skills:
        text = skill.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3:
            errors.append("Missing skill frontmatter")
            continue
        meta = yaml.safe_load(parts[1])
        if meta.get("name") != skill.parent.name or not meta.get("description"):
            errors.append("Invalid skill metadata")
    for path in PLUGIN.rglob("*.md"):
        if "templates" in path.parts:
            continue
        prose = path.read_text(encoding="utf-8")
        prose = re.sub(r"(?ms)^```.*?^```\s*$", "", prose)
        prose = re.sub(r"`[^`\n]+`", "", prose)
        for dest in re.findall(r"\]\(([^)]+)\)", prose):
            if "://" in dest or dest.startswith("#"):
                continue
            target = (path.parent / dest.split("#")[0]).resolve()
            if not target.is_relative_to(PLUGIN) or not target.exists():
                errors.append(f"Broken packaged reference: {path.name}: {dest}")
    schema = json.loads((PLUGIN / "schemas/project.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    for path in (PLUGIN / "profiles").glob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        v = Draft202012Validator({**schema, "$ref": "#/$defs/book"})
        errors.extend(f"{path.name}: {e.message}" for e in v.iter_errors(data))
    ui = yaml.safe_load((skills[0].parent / "agents/openai.yaml").read_text(encoding="utf-8"))
    if "$write-book" not in ui["interface"]["default_prompt"]:
        errors.append("Default prompt does not invoke the skill")
    if not 25 <= len(ui["interface"]["short_description"]) <= 64:
        errors.append("Skill short description must be 25–64 characters")
    if version not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
        errors.append("Missing changelog entry")
    if not (ROOT / f"docs/releases/{version}.md").is_file():
        errors.append("Missing version-specific release note")
    for path in PLUGIN.rglob("*"):
        if path.is_symlink():
            errors.append(f"Do not package symlinks: {path.relative_to(PLUGIN)}")
        if path.is_file() and path.suffix in {".md", ".yaml", ".json", ".py", ".txt"}:
            if "/Users/macos/" in path.read_text(encoding="utf-8"):
                errors.append(f"Machine-specific path: {path.relative_to(PLUGIN)}")
    from build_standalone import sync
    try:
        sync(check=True)
    except ValueError as exc:
        errors.append(str(exc))
    return {"version": version, "errors": errors, "skills": len(skills)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag")
    args = parser.parse_args()
    result = validate(args.tag)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result["errors"]))
