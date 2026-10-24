"""
Project 1: Secure CLI Calculator Engine
======================================
Implements a safe arithmetic expression evaluator using Python's AST module,
avoiding the catastrophic security risks of eval().
"""

import ast
import operator
import sys
from typing import Any, Union

# Supported binary operators mapped to standard operator functions
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

# Supported unary operators
UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class InvalidExpressionError(CalculatorError):
    """Raised when an expression contains unsupported syntax or malicious constructs."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass


class SafeEvaluator(ast.NodeVisitor):
    """Walks the Abstract Syntax Tree (AST) to evaluate only safe arithmetic nodes."""

    def visit(self, node: ast.AST) -> float | int:
        method = f"visit_{type(node).__name__}"
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: ast.AST) -> Any:
        raise InvalidExpressionError(
            f"Unsupported operation or security violation: {type(node).__name__}"
        )

    def visit_Expression(self, node: ast.Expression) -> float | int:
        return self.visit(node.body)

    def visit_Constant(self, node: ast.Constant) -> float | int:
        if isinstance(node.value, (int, float)):
            return node.value
        raise InvalidExpressionError(f"Unsupported constant type: {type(node.value).__name__}")

    def visit_UnaryOp(self, node: ast.UnaryOp) -> float | int:
        op_type = type(node.op)
        if op_type not in UNARY_OPERATORS:
            raise InvalidExpressionError(f"Unsupported unary operator: {op_type.__name__}")
        operand = self.visit(node.operand)
        return UNARY_OPERATORS[op_type](operand)

    def visit_BinOp(self, node: ast.BinOp) -> float | int:
        op_type = type(node.op)
        if op_type not in OPERATORS:
            raise InvalidExpressionError(f"Unsupported binary operator: {op_type.__name__}")

        left = self.visit(node.left)
        right = self.visit(node.right)

        if op_type in (ast.Div, ast.FloorDiv, ast.Mod) and right == 0:
            raise DivisionByZeroError("Cannot divide or modulo by zero!")

        try:
            return OPERATORS[op_type](left, right)
        except Exception as err:
            raise CalculatorError(f"Calculation error: {err}") from err


def evaluate(expression: str) -> float | int:
    """Safely evaluates a mathematical expression string.

    Args:
        expression: String like "10 + 5 * (2 ** 3)"

    Returns:
        The calculated numerical result.
    """
    clean_expr = expression.strip()
    if not clean_expr:
        raise InvalidExpressionError("Empty expression provided.")

    try:
        # Parse expression in 'eval' mode (expects an expression, not statements)
        parsed_ast = ast.parse(clean_expr, mode="eval")
    except SyntaxError as err:
        raise InvalidExpressionError(f"Syntax error in expression: {err}") from err

    evaluator = SafeEvaluator()
    return evaluator.visit(parsed_ast)


def run_repl() -> None:
    """Runs an interactive REPL loop in the terminal."""
    print("=" * 60)
    print("Python Mastery Lab: Safe CLI Calculator")
    print("Type any arithmetic expression (e.g., '10 + 5 * 2') or 'quit' to exit.")
    print("=" * 60)

    while True:
        try:
            line = input("calc> ").strip()
            if not line:
                continue
            if line.lower() in ("quit", "exit", "q"):
                print("Goodbye!")
                break

            result = evaluate(line)
            print(f"= {result}")

        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except CalculatorError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Unexpected error: {err}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Single expression passed via CLI argument
        expr = " ".join(sys.argv[1:])
        try:
            print(evaluate(expr))
        except CalculatorError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        run_repl()
