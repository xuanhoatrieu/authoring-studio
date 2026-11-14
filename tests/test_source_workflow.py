"""Synthetic temporary fixtures only. No book manuscript is created in the repo."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/authoring-studio"
sys.path.insert(0, str(PLUGIN / "scripts"))
sys.path.insert(0, str(ROOT / "scripts"))
from init_book import initialize
from validate_book import validate
from build_release import build
from validate_repo import validate as validate_repo


class SourceWorkflow(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "book"
        initialize(self.root, "Sách kiểm thử", "rural-tourism-vi")

    def load(self, name):
        return yaml.safe_load((self.root / name).read_text(encoding="utf-8"))

    def save(self, name, data):
        (self.root / name).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def sample(self):
        (self.root / "image/example.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>')
        (self.root / "chapters/sample.md").write_text(
            '# Kiểm thử {#sec-example}\n\nThông tin kiểm thử [@source-example].\n\n'
            '![Sơ đồ kiểm thử](../image/example.svg){#fig-example}\n'
            '<!-- caption: fig-example -->\nSơ đồ kiểm thử.\n\n'
            '<!-- table: tbl-example -->\n<!-- caption: tbl-example -->\nBảng kiểm thử.\n\n'
            '| Nội dung | Số lượng |\n|---|---|\n| Mẫu | 1 |\n', encoding="utf-8")
        self.save("references.yaml", {"references": [{"id": "source-example", "type": "report", "title": "Nguồn kiểm thử"}]})
        self.save("image-index.yaml", {"schema_version": 1, "images": [{
            "id": "fig-example", "section": "sec-example", "chapter_file": "chapters/sample.md",
            "file": "image/example.svg", "caption_id": "fig-example", "layout": "full-width-below",
            "status": "reviewed", "origin": "diagram", "alt": "Sơ đồ kiểm thử", "rights": "Test fixture, authored locally"}]})
        self.save("table-index.yaml", {"schema_version": 1, "tables": [{
            "id": "tbl-example", "section": "sec-example", "chapter_file": "chapters/sample.md",
            "caption_id": "tbl-example", "header_rows": 1, "columns": ["text", "number"]}]})

    def test_initialization_has_no_prose_and_validates(self):
        self.assertEqual([], list((self.root / "chapters").iterdir()))
        self.assertEqual([], list((self.root / "image").iterdir()))
        self.assertEqual([], validate(self.root)["errors"])

    def test_existing_book_is_not_overwritten(self):
        original = (self.root / "book.yaml").read_bytes()
        with self.assertRaises(ValueError):
            initialize(self.root, "Replacement")
        self.assertEqual(original, (self.root / "book.yaml").read_bytes())

    def test_dry_run_does_not_create_parent(self):
        target = Path(self.temp.name) / "new-parent/new-book"
        initialize(target, "Draft", dry_run=True)
        self.assertFalse(target.parent.exists())

    def test_plugin_and_repository_cannot_hold_books(self):
        for path in [PLUGIN / "new-book", ROOT / "new-book"]:
            with self.assertRaises(ValueError):
                initialize(path, "Forbidden")

    def test_valid_source_and_validation_is_read_only(self):
        self.sample()
        def snapshot():
            return {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in self.root.rglob("*") if p.is_file()}
        before = snapshot()
        result = validate(self.root)
        self.assertEqual([], result["errors"])
        self.assertEqual([], result["warnings"])
        self.assertEqual(before, snapshot())

    def test_missing_asset_is_detected(self):
        self.sample()
        (self.root / "image/example.svg").unlink()
        self.assertTrue(any("Missing" in e for e in validate(self.root)["errors"]))

    def test_unknown_citation_and_duplicate_anchor(self):
        self.sample()
        with (self.root / "chapters/sample.md").open("a", encoding="utf-8") as f:
            f.write('\n[@absent]\n## Duplicate {#sec-example}\n')
        errors = validate(self.root)["errors"]
        self.assertTrue(any("Unknown citation" in e for e in errors))
        self.assertTrue(any("Duplicate anchor" in e for e in errors))

    def test_missing_caption_detected(self):
        self.sample()
        path = self.root / "chapters/sample.md"
        path.write_text(path.read_text(encoding="utf-8").replace('<!-- caption: fig-example -->', ''), encoding="utf-8")
        self.assertTrue(any("Missing anchor/caption" in e for e in validate(self.root)["errors"]))

    def test_path_escape_rejected(self):
        self.sample()
        data = self.load("image-index.yaml")
        data["images"][0]["file"] = "../outside.svg"
        self.save("image-index.yaml", data)
        self.assertTrue(any("escapes" in e for e in validate(self.root)["errors"]))

    def test_absolute_path_rejected(self):
        self.sample()
        data = self.load("image-index.yaml")
        data["images"][0]["file"] = str(self.root / "image/example.svg")
        self.save("image-index.yaml", data)
        self.assertTrue(any("Absolute path" in e for e in validate(self.root)["errors"]))

    def test_planned_asset_remains_unresolved(self):
        self.sample()
        data = self.load("image-index.yaml")
        data["images"][0].update(status="planned", file=None, origin="pending")
        self.save("image-index.yaml", data)
        self.assertTrue(any("Planned" in w for w in validate(self.root)["warnings"]))

    def test_unverified_evidence_and_false_verified_metadata(self):
        self.sample()
        record = {"id": "claim-example", "statement": "Test", "sections": ["sec-example"],
                  "source_ids": ["source-example"], "locator": None, "checked_on": None, "status": "unverified"}
        self.save("evidence.yaml", {"schema_version": 1, "claims": [record]})
        self.assertTrue(validate(self.root)["warnings"])
        record["status"] = "verified"
        self.save("evidence.yaml", {"schema_version": 1, "claims": [record]})
        self.assertTrue(any("Verified evidence lacks" in e for e in validate(self.root)["errors"]))

    def test_schema_upgrade_is_reported_without_mutation(self):
        data = self.load("book.yaml")
        data["schema_version"] = 2
        self.save("book.yaml", data)
        before = (self.root / "book.yaml").read_bytes()
        self.assertTrue(validate(self.root)["errors"])
        self.assertEqual(before, (self.root / "book.yaml").read_bytes())

    def test_duplicate_yaml_key_rejected(self):
        with (self.root / "book.yaml").open("a") as f:
            f.write('\ntitle: duplicate\n')
        self.assertTrue(any("Duplicate YAML key" in e for e in validate(self.root)["errors"]))

    def test_move_chapter_preserves_semantic_links(self):
        self.sample()
        (self.root / "chapters/sample.md").rename(self.root / "chapters/reordered.md")
        for name, key in [("image-index.yaml", "images"), ("table-index.yaml", "tables")]:
            data = self.load(name)
            data[key][0]["chapter_file"] = "chapters/reordered.md"
            self.save(name, data)
        self.assertEqual([], validate(self.root)["errors"])

    def test_reproducible_archive_and_package_contents(self):
        one = build(Path(self.temp.name) / "one")
        two = build(Path(self.temp.name) / "two")
        self.assertEqual(one["sha256"], two["sha256"])
        with zipfile.ZipFile(one["archive"]) as z:
            self.assertIn("plugin.json", z.namelist())
            self.assertIn("skills/write-book/SKILL.md", z.namelist())
            self.assertFalse(any(".venv" in n or "__pycache__" in n for n in z.namelist()))

    def test_release_version_mismatch_is_rejected(self):
        self.assertTrue(validate_repo("v9.9.9")["errors"])
        self.assertEqual([], validate_repo("v0.1.0")["errors"])


if __name__ == "__main__":
    unittest.main()
