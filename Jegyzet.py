from pathlib import Path
from unittest import TestCase

x = "hello"

# if condition returns True, then nothing happens:
assert x == "hello"

# if condition returns False, AssertionError is raised:
assert x == "hello"

# .stem
# with_suffix


class TestCase1(TestCase):
    def test_against_ref_files(self):
        testroot = Path("c:\\Zsuzsi\\Python_programozas\\Pelda")
        self.check_file_content_equality(testroot / "Text1.txt", testroot / "Text2.txt")

    def check_file_content_equality(self, reference_file: Path, actual_file: Path):
        self. assertEqual(reference_file.read_bytes(), actual_file.read_bytes())
