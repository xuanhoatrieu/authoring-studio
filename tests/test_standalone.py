"""Exercise the distributed skill outside the repository, without a live AI host."""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_standalone
from build_release import build


class StandaloneBundle(unittest.TestCase):
    def test_stale_or_missing_resources_are_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "write-book"
            with patch.object(build_standalone, "TARGET", target):
                build_standalone.sync()
                build_standalone.sync(check=True)
                (target / "resources/templates/book.yaml").unlink()
                with self.assertRaises(ValueError):
                    build_standalone.sync(check=True)

    def test_extracted_bundle_is_self_contained_and_helpers_work(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            result = build(root / "dist")["standalone"]
            with zipfile.ZipFile(result["archive"]) as archive:
                archive.extractall(root / "unpacked")
            skill = root / "unpacked/write-book"
            self.assertEqual("0.2.0", json.loads((skill / "bundle.json").read_text())["version"])
            for path in skill.rglob("*.md"):
                if path.name in {"LICENSE", "THIRD_PARTY_NOTICES.md"} or "templates" in path.parts:
                    continue
                text = re.sub(r"(?ms)^```.*?^```\s*$", "", path.read_text(encoding="utf-8"))
                text = re.sub(r"`[^`\n]+`", "", text)
                for dest in re.findall(r"\]\(([^)]+)\)", text):
                    if "://" in dest or dest.startswith("#"):
                        continue
                    target = (path.parent / dest.split("#")[0]).resolve()
                    self.assertTrue(target.is_relative_to(skill.resolve()), (path, dest))
                    self.assertTrue(target.exists(), (path, dest))
            for profile in ("generic", "rural-tourism-vi"):
                book = root / profile
                command = [sys.executable, str(skill / "resources/scripts/init_book.py"),
                           str(book), "--title", "Portable fixture"]
                if profile != "generic":
                    command += ["--profile", profile]
                subprocess.run(command, cwd=root, check=True, capture_output=True)
                report = subprocess.run([sys.executable, str(skill / "resources/scripts/validate_book.py"),
                                         str(book)], cwd=root, check=True, capture_output=True, text=True)
                self.assertEqual([], json.loads(report.stdout)["errors"])
            refused = subprocess.run([sys.executable, str(skill / "resources/scripts/init_book.py"),
                                      str(skill / "wrong-book"), "--title", "Forbidden"],
                                     cwd=root, capture_output=True)
            self.assertNotEqual(0, refused.returncode)
            self.assertFalse((skill / "wrong-book").exists())

    def test_both_archives_are_reproducible_and_codex_layout_is_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            first = build(Path(folder) / "one")
            second = build(Path(folder) / "two")
            self.assertEqual(first["sha256"], second["sha256"])
            self.assertEqual(first["standalone"]["sha256"], second["standalone"]["sha256"])
            with zipfile.ZipFile(first["archive"]) as archive:
                for path in (ROOT / "plugins/authoring-studio").rglob("*"):
                    if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
                        continue
                    name = path.relative_to(ROOT / "plugins/authoring-studio").as_posix()
                    self.assertEqual(path.read_bytes(), archive.read(name), name)
