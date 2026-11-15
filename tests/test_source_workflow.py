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

    def test_confirmed_tourism_layout_is_initialized_without_changing_generic(self):
        layout = self.load("book.yaml")["layout"]
        expected = {
            "paper": "A4", "orientation": "portrait",
            "margins_cm": {"left": 3, "right": 2, "top": 2, "bottom": 2},
            "body_font": "Times New Roman", "body_font_pt": 13,
            "body_alignment": "justify", "line_spacing_multiple": 1.3,
            "paragraph_spacing_pt": 4, "paragraph_spacing_position": "after",
            "paragraph_before_pt": 0, "paragraph_after_pt": 4,
            "chapter_heading_align": "left", "section_heading_align": "left",
            "caption_font_pt": 12, "caption_align": "center", "text_width_cm": 16,
            "book_cover": {
                "separate_page": True, "prominent_title": True,
                "representative_image": True, "caption": False, "numbered": False,
                "title_rendering": "typeset",
            },
            "footer": {
                "left_text": "@ TS.Triệu Xuân Hoà", "page_number_align": "right",
                "page_number_format": "arabic", "page_number_start": 1, "scope": "all-pages",
            },
            "table": {
                "title_align": "center", "header_horizontal_align": "center",
                "header_vertical_align": "center", "number_horizontal_align": "center",
                "text_horizontal_align": "left", "body_vertical_align": "center",
                "line_spacing_multiple": 1, "paragraph_before_pt": 0, "paragraph_after_pt": 0,
            },
        }
        self.assertEqual(expected, layout)
        authoring = self.load("book.yaml")["authoring"]
        self.assertEqual(["book-cover", "preface", "table-of-contents", "general-introduction"],
                         authoring["front_matter_order"])
        self.assertTrue(authoring["chapter_covers"]["content_starts_next_page"])
        self.assertFalse(authoring["chapter_covers"]["caption"])
        self.assertFalse(authoring["existing_images_first"])
        self.assertEqual("photorealistic", authoring["generated_scene_style"])
        generic = Path(self.temp.name) / "generic-book"
        initialize(generic, "Generic test")
        generic_layout = yaml.safe_load((generic / "book.yaml").read_text(encoding="utf-8"))["layout"]
        self.assertEqual("pending", generic_layout["chapter_heading_align"])
        self.assertEqual("pending", generic_layout["section_heading_align"])
        self.assertEqual("pending", generic_layout["paragraph_spacing_position"])
        self.assertIsNone(generic_layout["caption_font_pt"])
        self.assertNotIn("footer", generic_layout)
        self.assertNotIn("book_cover", generic_layout)

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

    def cover_sample(self, role="book-cover"):
        self.sample()
        path = self.root / "chapters/sample.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            '<!-- caption: fig-example -->\nSơ đồ kiểm thử.\n', ''), encoding="utf-8")
        data = self.load("image-index.yaml")
        data["images"][0].update(role=role, caption_id=None, numbered=False)
        self.save("image-index.yaml", data)

    def test_cover_roles_allow_no_caption_but_preserve_asset_checks(self):
        for role in ["book-cover", "chapter-cover"]:
            with self.subTest(role=role):
                self.cover_sample(role)
                self.assertEqual([], validate(self.root)["errors"])
                (self.root / "image/example.svg").unlink()
                self.assertTrue(any("Missing" in e for e in validate(self.root)["errors"]))

    def test_cover_rejects_caption_and_numbered_reference(self):
        self.cover_sample()
        path = self.root / "chapters/sample.md"
        with path.open("a", encoding="utf-8") as f:
            f.write('\n<!-- caption: fig-example -->\nForbidden caption.\n\nSee @fig-example.\n')
        errors = validate(self.root)["errors"]
        self.assertTrue(any("Cover must not have a caption" in e for e in errors))
        self.assertTrue(any("reference its section instead" in e for e in errors))

    def test_cover_rejects_figure_number_and_content_cannot_skip_caption(self):
        self.cover_sample()
        data = self.load("image-index.yaml")
        data["images"][0]["numbered"] = True
        self.save("image-index.yaml", data)
        self.assertTrue(validate(self.root)["errors"])
        for role in [None, "content"]:
            with self.subTest(role=role):
                item = data["images"][0]
                item.pop("role", None)
                if role:
                    item["role"] = role
                item["numbered"] = False
                self.save("image-index.yaml", data)
                self.assertTrue(validate(self.root)["errors"])

    def test_prompt_file_mapping_and_portability(self):
        self.sample()
        prompt = self.root / "image/prompts/fig-example.md"
        prompt.parent.mkdir()
        prompt.write_text('Draw the fixture as specified.\n', encoding="utf-8")
        data = self.load("image-index.yaml")
        data["images"][0]["prompt_file"] = "image/prompts/fig-example.md"
        self.save("image-index.yaml", data)
        self.assertEqual([], validate(self.root)["errors"])
        prompt.unlink()
        self.assertTrue(any("Missing image prompt" in e for e in validate(self.root)["errors"]))
        for value in ["../outside.md", str(prompt), "chapters/sample.md"]:
            with self.subTest(path=value):
                data["images"][0]["prompt_file"] = value
                self.save("image-index.yaml", data)
                self.assertTrue(validate(self.root)["errors"])

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
        self.assertEqual([], validate_repo("v0.2.1")["errors"])


if __name__ == "__main__":
    unittest.main()
