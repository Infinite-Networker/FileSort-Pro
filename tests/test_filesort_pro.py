#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║             FileSort Pro — Test Suite                        ║
║             Cherry Computer Ltd.                             ║
╚══════════════════════════════════════════════════════════════╝

Unit tests for filesort_pro.py covering:
  - Path validation
  - Directory scanning & sorting
  - Hidden-file filtering
  - Human-readable size formatting
  - File-icon mapping
  - Export functionality
"""

import os
import sys
import tempfile
import unittest

# Allow importing from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from filesort_pro import FileSortPro, _human_size, _file_icon


class TestPathValidation(unittest.TestCase):
    """Tests for FileSortPro.validate_path()"""

    def test_valid_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sorter = FileSortPro(tmpdir)
            valid, reason = sorter.validate_path()
            self.assertTrue(valid)
            self.assertEqual(reason, "")

    def test_nonexistent_path(self):
        sorter = FileSortPro("/this/path/does/not/exist")
        valid, reason = sorter.validate_path()
        self.assertFalse(valid)
        self.assertIn("does not exist", reason)

    def test_file_instead_of_directory(self):
        with tempfile.NamedTemporaryFile() as tmp:
            sorter = FileSortPro(tmp.name)
            valid, reason = sorter.validate_path()
            self.assertFalse(valid)
            self.assertIn("not a directory", reason)


class TestScanning(unittest.TestCase):
    """Tests for FileSortPro.scan()"""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        # Create test files (intentionally unsorted)
        self.visible_names = ["zebra.txt", "apple.py", "Mango.json", "banana.md"]
        self.hidden_names  = [".secret", ".config"]
        for name in self.visible_names + self.hidden_names:
            open(os.path.join(self.tmpdir, name), "w").close()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_sorted_order(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        names = sorter.files
        self.assertEqual(names, sorted(names, key=str.lower))

    def test_visible_files_only(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        for f in sorter.files:
            self.assertFalse(f.startswith("."), f"{f} is hidden but appeared in visible list")

    def test_hidden_files_separated(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        self.assertEqual(len(sorter.hidden_files), len(self.hidden_names))
        for f in sorter.hidden_files:
            self.assertTrue(f.startswith("."))

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sorter = FileSortPro(tmpdir)
            sorter.scan()
            self.assertEqual(sorter.files, [])
            self.assertEqual(sorter.hidden_files, [])

    def test_scan_time_recorded(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        self.assertIsNotNone(sorter.scan_time)
        self.assertGreaterEqual(sorter.scan_time, 0)

    def test_case_insensitive_sort(self):
        """Files starting with uppercase should sort alongside lowercase."""
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        lower_names = [f.lower() for f in sorter.files]
        self.assertEqual(lower_names, sorted(lower_names))


class TestExport(unittest.TestCase):
    """Tests for FileSortPro.export_results()"""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        for name in ["delta.py", "alpha.txt", "gamma.md"]:
            open(os.path.join(self.tmpdir, name), "w").close()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_export_creates_file(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        output_path = os.path.join(self.tmpdir, "test_output.txt")
        sorter.export_results(output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_export_contains_filenames(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        output_path = os.path.join(self.tmpdir, "test_output.txt")
        sorter.export_results(output_path)
        with open(output_path, "r") as f:
            content = f.read()
        for name in ["alpha.txt", "delta.py", "gamma.md"]:
            self.assertIn(name, content)

    def test_export_contains_header(self):
        sorter = FileSortPro(self.tmpdir)
        sorter.scan()
        output_path = os.path.join(self.tmpdir, "test_output.txt")
        sorter.export_results(output_path)
        with open(output_path, "r") as f:
            content = f.read()
        self.assertIn("Cherry Computer Ltd.", content)
        self.assertIn("Dr. Ahmad M. Ishanzai", content)


class TestHumanSize(unittest.TestCase):
    """Tests for _human_size() utility function."""

    def test_bytes(self):
        self.assertIn("B", _human_size(512))

    def test_kilobytes(self):
        result = _human_size(2048)
        self.assertIn("KB", result)

    def test_megabytes(self):
        result = _human_size(1024 * 1024 * 5)
        self.assertIn("MB", result)

    def test_gigabytes(self):
        result = _human_size(1024 ** 3 * 2)
        self.assertIn("GB", result)

    def test_zero_bytes(self):
        result = _human_size(0)
        self.assertIn("B", result)


class TestFileIcon(unittest.TestCase):
    """Tests for _file_icon() utility function."""

    def test_python_icon(self):
        self.assertEqual(_file_icon(".py"), "🐍")

    def test_pdf_icon(self):
        self.assertEqual(_file_icon(".pdf"), "📄")

    def test_image_icon(self):
        self.assertEqual(_file_icon(".png"), "🖼 ")

    def test_archive_icon(self):
        self.assertEqual(_file_icon(".zip"), "📦")

    def test_unknown_extension(self):
        self.assertEqual(_file_icon(".xyz"), "📁")

    def test_empty_extension(self):
        self.assertEqual(_file_icon(""), "📁")


if __name__ == "__main__":
    print("\n  FileSort Pro — Running Test Suite\n  Cherry Computer Ltd.\n")
    unittest.main(verbosity=2)
