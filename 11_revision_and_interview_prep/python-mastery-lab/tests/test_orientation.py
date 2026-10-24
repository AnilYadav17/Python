"""
Automated Tests for Module 00: Orientation & Execution Pipeline
===============================================================
Validates that our environment, parser, compiler, and code objects behave
in accordance with CPython specifications.
"""

import ast
import dis
import io
import sys
import tokenize
import types
import unittest


class TestOrientationPipeline(unittest.TestCase):
    def test_python_version_baseline(self) -> None:
        """Verify the Python interpreter meets the minimum version requirement (>= 3.12)."""
        self.assertGreaterEqual(
            sys.version_info[:2],
            (3, 12),
            f"Python version must be >= 3.12, found {sys.version}",
        )
        self.assertEqual(sys.implementation.name, "cpython")

    def test_tokenization(self) -> None:
        """Verify the tokenizer breaks source text into expected token types."""
        source = "x = 42"
        tokens = list(tokenize.tokenize(io.BytesIO(source.encode("utf-8")).readline))
        # Filter out ENCODING and ENDMARKER
        filtered = [t for t in tokens if t.type not in (tokenize.ENCODING, tokenize.ENDMARKER)]

        token_names = [tokenize.tok_name[t.type] for t in filtered]
        token_strings = [t.string for t in filtered]

        self.assertIn("NAME", token_names)
        self.assertIn("OP", token_names)
        self.assertIn("NUMBER", token_names)
        self.assertEqual(token_strings[:3], ["x", "=", "42"])

    def test_ast_generation(self) -> None:
        """Verify that ast.parse generates the expected AST node hierarchy."""
        source = "area = width * height"
        tree = ast.parse(source)

        self.assertIsInstance(tree, ast.Module)
        self.assertEqual(len(tree.body), 1)

        assign_node = tree.body[0]
        self.assertIsInstance(assign_node, ast.Assign)
        self.assertEqual(len(assign_node.targets), 1)
        self.assertIsInstance(assign_node.targets[0], ast.Name)
        self.assertEqual(assign_node.targets[0].id, "area")

        binop_node = assign_node.value
        self.assertIsInstance(binop_node, ast.BinOp)
        self.assertIsInstance(binop_node.op, ast.Mult)

    def test_compilation_to_code_object(self) -> None:
        """Verify compile() transforms source code into a CodeType object and populates constants."""
        source = "x = 100000\ny = 'mastery_lab'\nz = x"
        code_obj = compile(source, filename="<test>", mode="exec")

        self.assertIsInstance(code_obj, types.CodeType)
        # Check names stored in the code object
        self.assertIn("x", code_obj.co_names)
        self.assertIn("y", code_obj.co_names)
        self.assertIn("z", code_obj.co_names)
        # Check constants table
        self.assertIn(100000, code_obj.co_consts)
        self.assertIn("mastery_lab", code_obj.co_consts)

    def test_bytecode_disassembly_instructions(self) -> None:
        """Verify bytecode instructions emitted by dis.get_instructions."""
        def dummy_add(a: int, b: int) -> int:
            return a + b

        instructions = list(dis.get_instructions(dummy_add))
        opnames = [instr.opname for instr in instructions]

        # Verify entry point and binary operation
        self.assertIn("RESUME", opnames)
        self.assertIn("BINARY_OP", opnames)
        self.assertIn("RETURN_VALUE", opnames)

        # In Python 3.11-3.13, local parameter loading emits LOAD_FAST.
        # In Python 3.14+, consecutive fast loads are specialized into superinstructions like
        # LOAD_FAST_BORROW_LOAD_FAST_BORROW. We verify either pattern:
        has_fast_load = any("LOAD_FAST" in name for name in opnames)
        self.assertTrue(
            has_fast_load,
            f"Expected a LOAD_FAST variant in opcodes, but found: {opnames}",
        )


if __name__ == "__main__":
    unittest.main()
