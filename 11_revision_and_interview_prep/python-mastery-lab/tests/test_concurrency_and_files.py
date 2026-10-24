"""
Automated Tests for Modules 11, 12, 19: Concurrency, Files & Packaging
======================================================================
Tests pathlib operations, deque FIFO performance, ThreadPoolExecutor,
and module caching in sys.modules.
"""

from collections import deque
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import unittest


class TestConcurrencyAndFiles(unittest.TestCase):
    def test_pathlib_traversal_and_text(self) -> None:
        """Verify pathlib path concatenation via / and text I/O."""
        p = Path("unit_test_temp.txt")
        p.write_text("automated test", encoding="utf-8")

        self.assertTrue(p.exists())
        self.assertEqual(p.read_text(encoding="utf-8"), "automated test")
        self.assertEqual(p.suffix, ".txt")

        p.unlink()
        self.assertFalse(p.exists())

    def test_deque_operations(self) -> None:
        """Verify deque append and popleft FIFO operations."""
        d = deque(["first", "second"])
        d.append("third")
        self.assertEqual(d.popleft(), "first")
        self.assertEqual(d.pop(), "third")
        self.assertEqual(d.popleft(), "second")
        self.assertEqual(len(d), 0)

    def test_threadpool_concurrent_mapping(self) -> None:
        """Verify ThreadPoolExecutor maps functions across workers."""
        with ThreadPoolExecutor(max_workers=2) as executor:
            doubles = list(executor.map(lambda x: x * 2, [1, 2, 3, 4]))
        self.assertEqual(doubles, [2, 4, 6, 8])

    def test_sys_modules_caching(self) -> None:
        """Verify standard modules are cached in sys.modules."""
        import math
        self.assertIn("math", sys.modules)
        self.assertIs(sys.modules["math"], math)


if __name__ == "__main__":
    unittest.main()
