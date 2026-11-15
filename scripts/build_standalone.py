#!/usr/bin/env python3
"""Derive a self-contained skill from the unchanged Codex package layout."""
import argparse
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/authoring-studio"
TARGET = ROOT / "skills/write-book"


def entries():
    result = {}
    for folder, prefix in [(PLUGIN / "skills/write-book", ""),
                           *[(PLUGIN / name, "resources/" + name + "/")
                             for name in ("templates", "profiles", "schemas", "scripts")]]:
        for path in folder.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Cannot bundle symlink: {path}")
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
                continue
            if folder.name == "write-book" and "agents" in path.relative_to(folder).parts:
                continue  # Codex UI metadata stays in the Codex package.
            result[prefix + path.relative_to(folder).as_posix()] = path.read_bytes()
    text = result["SKILL.md"].decode("utf-8")
    text = text.replace("Plugin root is two directories above this skill.",
                        "Resource root is `resources/` inside this skill. In supporting guidance,\n"
                        "paths such as `scripts/` and `templates/` are relative to that resource root.")
    text = text.replace("../../", "resources/")
    result["SKILL.md"] = text.encode("utf-8")
    result["resources/plugin.json"] = (PLUGIN / "plugin.json").read_bytes()
    result["resources/requirements.txt"] = (PLUGIN / "requirements.txt").read_bytes()
    for name in ("LICENSE", "THIRD_PARTY_NOTICES.md"):
        result[name] = (ROOT / name).read_bytes()
    result["bundle.json"] = (json.dumps({
        "name": "write-book", "version": json.loads(result["resources/plugin.json"])["version"],
        "source": "plugins/authoring-studio", "generated": True,
        "resource_root": "resources", "schema_version": 1,
    }, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return result


def sync(check=False):
    expected = entries()
    actual = {p.relative_to(TARGET).as_posix(): p.read_bytes()
              for p in TARGET.rglob("*") if p.is_file()
              and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name != ".DS_Store"}
    if check:
        changed = sorted(k for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k))
        if changed:
            raise ValueError("Stale standalone bundle; run build_standalone.py: " + ", ".join(changed))
    else:
        if TARGET.exists():
            shutil.rmtree(TARGET)  # Only the fixed, generated tree, never a user-supplied path.
        for name, data in expected.items():
            path = TARGET / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    return {"files": len(expected), "checked": check}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    print(json.dumps(sync(parser.parse_args().check)))
