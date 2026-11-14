#!/usr/bin/env python3
"""Read-only integrity checks for source-format v1; not a factual/layout review."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    raise SystemExit("Missing dependencies. Install the plugin requirements in a virtual environment.")

PLUGIN = Path(__file__).resolve().parents[1]
FILES = {"book.yaml": "book", "state.yaml": "state", "image-index.yaml": "images",
         "table-index.yaml": "tables", "references.yaml": "references",
         "evidence.yaml": "evidence", "terms.yaml": "terms"}
ANCHOR = re.compile(r"\{#((?:sec|fig|tbl)-[a-z0-9-]+)\}")
TABLE = re.compile(r"<!--\s*table:\s*(tbl-[a-z0-9-]+)\s*-->")
CAPTION = re.compile(r"<!--\s*caption:\s*((?:fig|tbl)-[a-z0-9-]+)\s*-->")
MENTION = re.compile(r"(?<![\w@])@([a-z][a-z0-9-]*)")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)\s*\{#(fig-[a-z0-9-]+)\}")


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def safe_path(root, value):
    candidate = Path(value)
    if candidate.is_absolute():
        raise ValueError(f"Absolute path is not portable: {value}")
    resolved = (root / candidate).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes book root: {value}")
    return resolved


def without_code(text):
    return re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1\s*$", "", text)


def validate(root):
    root = Path(root).expanduser().resolve()
    errors, warnings, data = [], [], {}
    if not root.is_dir():
        return {"errors": ["Book directory does not exist."], "warnings": [], "files_checked": 0}
    schema = json.loads((PLUGIN / "schemas/project.schema.json").read_text(encoding="utf-8"))
    for filename, kind in FILES.items():
        try:
            raw = safe_path(root, filename).read_text(encoding="utf-8")
            value = yaml.load(raw, Loader=UniqueLoader)
            validator = Draft202012Validator({**schema, "$ref": f"#/$defs/{kind}"})
            issues = list(validator.iter_errors(value))
            errors.extend(f"{filename}: {'/'.join(map(str, e.path))}: {e.message}" for e in issues)
            if not issues:
                data[kind] = value
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{filename}: {exc}")
    for filename in ["decisions.md", "outline.md"]:
        if not (root / filename).is_file():
            errors.append(f"Missing project record: {filename}")
    for directory in ["chapters", "image"]:
        try:
            if not safe_path(root, directory).is_dir():
                errors.append(f"Missing project directory: {directory}")
        except ValueError as exc:
            errors.append(str(exc))
    if len(data) != len(FILES):
        return {"errors": errors, "warnings": warnings, "files_checked": len(data)}

    docs, anchors, figures, captions = {}, {}, {}, {}
    for file in sorted((root / "chapters").rglob("*.md")):
        rel = file.relative_to(root).as_posix()
        try:
            safe_path(root, rel)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        text = without_code(file.read_text(encoding="utf-8"))
        docs[rel] = text
        for key in ANCHOR.findall(text) + TABLE.findall(text):
            if key in anchors:
                errors.append(f"Duplicate anchor: {key}")
            anchors[key] = rel
        for match in CAPTION.finditer(text):
            key = match.group(1)
            if key in captions:
                errors.append(f"Duplicate caption: {key}")
            captions[key] = rel
            tail = text[match.end():].lstrip()
            if not tail or tail.startswith(("<!--", "#", "![", "|")):
                errors.append(f"Empty caption: {key}")
        for alt, path, key in IMAGE.findall(text):
            try:
                resolved = safe_path(root, (Path(rel).parent / path).as_posix())
                if not resolved.is_file():
                    errors.append(f"Missing image file: {path} in {rel}")
                figures[key] = resolved
            except ValueError as exc:
                errors.append(str(exc))
            if not alt.strip():
                errors.append(f"Missing alt text: {key}")
        for label in data["book"]["authoring"].get("forbidden_labels", []):
            visible = re.sub(r"<!--.*?-->", "", text, flags=re.S)
            if label.casefold() in visible.casefold():
                warnings.append(f"Review unwanted wording in {rel}: {label}")

    def records(kind, field):
        values = data[kind][field]
        counts = Counter(item["id"] for item in values)
        errors.extend(f"Duplicate {field} ID: {k}" for k, n in counts.items() if n > 1)
        return values

    sources = {item["id"] for item in records("references", "references")}
    for rel, text in docs.items():
        clean = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        for key in MENTION.findall(clean):
            if key.startswith(("fig-", "tbl-", "sec-")):
                if key not in anchors:
                    errors.append(f"Unresolved cross-reference: {key} in {rel}")
            elif key not in sources:
                errors.append(f"Unknown citation: {key} in {rel}")

    indexed = set()
    for kind, field in [("images", "images"), ("tables", "tables")]:
        for item in records(kind, field):
            key, chapter = item["id"], item["chapter_file"]
            indexed.add(key)
            try:
                safe_path(root, chapter)
            except ValueError as exc:
                errors.append(str(exc))
            planned = item.get("status") == "planned"
            if planned:
                warnings.append(f"Planned illustration not complete: {key}")
            if chapter not in docs:
                (warnings if planned else errors).append(f"Missing chapter for {key}: {chapter}")
            if anchors.get(item["section"]) != chapter:
                (warnings if planned else errors).append(f"Section mismatch for {key}: {item['section']}")
            if item["caption_id"] != key:
                errors.append(f"Caption ID must equal item ID: {key}")
            if not planned and (anchors.get(key) != chapter or captions.get(key) != chapter):
                errors.append(f"Missing anchor/caption for {key} in {chapter}")
            if kind == "images":
                if item["file"]:
                    try:
                        asset = safe_path(root, item["file"])
                        if not asset.is_relative_to((root / "image").resolve()):
                            errors.append(f"Asset must be under image/: {key}")
                        if not asset.is_file():
                            errors.append(f"Missing indexed image: {item['file']}")
                        if not planned and figures.get(key) != asset:
                            errors.append(f"Image mapping mismatch: {key}")
                    except ValueError as exc:
                        errors.append(str(exc))
                elif not planned:
                    errors.append(f"Image file not assigned: {key}")
                if not planned and not item.get("rights"):
                    warnings.append(f"Image rights unresolved: {key}")
                if not planned and item["origin"] in {"existing", "screenshot"} and not item.get("source_url"):
                    warnings.append(f"Image source unresolved: {key}")
                if item.get("source_id") and item["source_id"] not in sources:
                    errors.append(f"Unknown image source ID: {key}")
                if item["status"] in {"acquired", "needs-replacement"}:
                    warnings.append(f"Image needs review: {key}")
    for key in anchors:
        if key.startswith(("fig-", "tbl-")) and key not in indexed:
            errors.append(f"Unindexed illustration: {key}")

    for item in records("evidence", "claims"):
        for key in item["source_ids"]:
            if key not in sources:
                errors.append(f"Unknown evidence source: {key}")
        for section in item["sections"]:
            if section not in anchors:
                errors.append(f"Unknown evidence section: {section}")
        if item["status"] == "verified":
            if not item["source_ids"] or not item["locator"] or not item["checked_on"]:
                errors.append(f"Verified evidence lacks source, locator or date: {item['id']}")
        else:
            warnings.append(f"Evidence unresolved: {item['id']}")
    for term in records("terms", "terms"):
        if term["first_section"] and term["first_section"] not in anchors:
            errors.append(f"Unknown first-use section for term: {term['id']}")
    for chapter in data["state"]["chapters"]:
        try:
            path = safe_path(root, chapter["file"])
            if chapter["status"] != "planned" and not path.is_file():
                errors.append(f"State references missing chapter: {chapter['file']}")
        except ValueError as exc:
            errors.append(str(exc))
    return {"errors": sorted(set(errors)), "warnings": sorted(set(warnings)),
            "files_checked": len(data) + len(docs)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = validate(args.book)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if result["errors"] or (args.strict and result["warnings"]) else 0)


if __name__ == "__main__":
    main()
