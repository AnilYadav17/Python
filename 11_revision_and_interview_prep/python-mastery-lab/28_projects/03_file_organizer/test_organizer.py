"""
Automated Unit & Integration Tests for Safe File Organizer (Project 03)
"""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from organizer import FileOrganizer, EXTENSION_CATEGORIES


class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        # Create an isolated temporary test directory
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        # Clean up temporary test files
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_category_resolution(self):
        organizer = FileOrganizer(self.test_dir)
        self.assertEqual(organizer.get_category_for_file(Path("notes.md")), "Documents")
        self.assertEqual(organizer.get_category_for_file(Path("photo.jpg")), "Images")
        self.assertEqual(organizer.get_category_for_file(Path("script.py")), "Code")
        self.assertEqual(organizer.get_category_for_file(Path("unknown.xyz")), "Miscellaneous")

    def test_collision_resolution(self):
        organizer = FileOrganizer(self.test_dir)
        target_folder = self.test_dir / "Documents"
        target_folder.mkdir(parents=True)

        # Create existing file: report.txt
        existing = target_folder / "report.txt"
        existing.write_text("first", encoding="utf-8")

        # First collision should resolve to report_1.txt
        resolved_1 = organizer.resolve_destination(target_folder, "report.txt")
        self.assertEqual(resolved_1.name, "report_1.txt")

        # Simulate report_1.txt existing
        resolved_1.write_text("second", encoding="utf-8")
        resolved_2 = organizer.resolve_destination(target_folder, "report.txt")
        self.assertEqual(resolved_2.name, "report_2.txt")

    def test_dry_run_mode_does_not_modify_files(self):
        # Create dummy file
        doc_file = self.test_dir / "thesis.pdf"
        doc_file.write_text("content", encoding="utf-8")

        organizer = FileOrganizer(self.test_dir, dry_run=True)
        actions = organizer.organize()

        self.assertEqual(len(actions), 1)
        self.assertFalse(actions[0].executed)
        # Original file MUST still exist at root
        self.assertTrue(doc_file.exists())
        # Target folder must NOT be created
        self.assertFalse((self.test_dir / "Documents").exists())

    def test_full_organization_and_audit_log(self):
        # Create sample files
        (self.test_dir / "report.txt").write_text("hello doc", encoding="utf-8")
        (self.test_dir / "picture.png").write_text("img data", encoding="utf-8")
        (self.test_dir / "app.py").write_text("print('hi')", encoding="utf-8")

        organizer = FileOrganizer(self.test_dir, dry_run=False)
        actions = organizer.organize()

        self.assertEqual(len(actions), 3)
        # Verify files were moved to corresponding category folders
        self.assertTrue((self.test_dir / "Documents" / "report.txt").exists())
        self.assertTrue((self.test_dir / "Images" / "picture.png").exists())
        self.assertTrue((self.test_dir / "Code" / "app.py").exists())

        # Verify audit log JSON exists and is valid
        audit_file = self.test_dir / "organize_audit.json"
        self.assertTrue(audit_file.exists())
        with open(audit_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 3)


if __name__ == "__main__":
    unittest.main()
