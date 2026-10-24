"""
Automated Unit Tests for pypulse package.
"""

from pathlib import Path
import sys
import unittest

# Ensure src is on sys.path
pkg_src = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(pkg_src))

import pypulse
from pypulse.transformers import camel_to_snake, slugify, snake_to_camel, truncate_words
from pypulse.validators import is_valid_email, is_valid_slug, is_valid_url


class TestPyPulse(unittest.TestCase):
    def test_package_metadata(self):
        self.assertEqual(pypulse.__version__, "1.0.0")
        self.assertIn("is_valid_email", pypulse.__all__)
        self.assertIn("slugify", pypulse.__all__)

    def test_email_validation(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("first.last+tag@sub.domain.org"))
        self.assertFalse(is_valid_email("missing-at.com"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("@domain.com"))
        self.assertFalse(is_valid_email(123))  # type: ignore

    def test_url_validation(self):
        self.assertTrue(is_valid_url("https://python.org"))
        self.assertTrue(is_valid_url("http://localhost:8000/api"))
        self.assertFalse(is_valid_url("ftp://server.com"))
        self.assertFalse(is_valid_url("just a string"))

    def test_slug_validation(self):
        self.assertTrue(is_valid_slug("python-mastery-lab"))
        self.assertTrue(is_valid_slug("version-2"))
        self.assertFalse(is_valid_slug("Invalid Slug!"))
        self.assertFalse(is_valid_slug("-leading-hyphen"))

    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("UserAccountProfile"), "user_account_profile")
        self.assertEqual(camel_to_snake("httpRequest"), "http_request")
        self.assertEqual(camel_to_snake("simple"), "simple")

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("user_profile"), "userProfile")
        self.assertEqual(snake_to_camel("user_profile", pascal=True), "UserProfile")

    def test_slugify(self):
        self.assertEqual(slugify("Hello, World! 2026"), "hello-world-2026")
        self.assertEqual(slugify("Crème Brûlée Delicious"), "creme-brulee-delicious")

    def test_truncate_words(self):
        text = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(truncate_words(text, 4), "The quick brown fox...")
        self.assertEqual(truncate_words(text, 20), text)


if __name__ == "__main__":
    unittest.main()
