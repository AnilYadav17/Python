"""
02_edge_cases.py
Demonstrates type hinting edge cases:
- Forward reference problem and 'from __future__ import annotations'
- Heterogeneous vs homogeneous tuple annotations
- Proof of runtime non-enforcement (Python does not type-check at runtime)
"""

from __future__ import annotations  # Defers evaluation of annotations as strings

# 1. Forward Reference Resolution
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        # Without 'from __future__ import annotations', referencing TreeNode
        # inside its own class body raises NameError: name 'TreeNode' is not defined!
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


# 2. Tuple Type Annotation Edge Cases
# A tuple of EXACTLY two integers
pair: tuple[int, int] = (10, 20)

# A tuple of ONE integer (requires trailing comma in annotation)
single: tuple[int] = (42,)

# A tuple of ANY number of integers (uses ellipsis ...)
arbitrary_ints: tuple[int, ...] = (1, 2, 3, 4, 5)


def demonstrate_runtime_non_enforcement():
    print("--- Runtime Non-Enforcement Proof ---")

    def add_numbers(a: int, b: int) -> int:
        return a + b  # type: ignore

    # Python's runtime interpreter COMPLETELY ignores type hints!
    # Passing strings does NOT raise a TypeError at execution time:
    bad_result = add_numbers("Hello ", "World")
    print(f"Result with strings passed to int-annotated function: '{bad_result}'")
    print("Conclusion: Type hints are static contracts for linters and IDEs, not runtime barriers.")


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    print(f"TreeNode constructed: root={root.value}, left={root.left.value}, right={root.right.value}")
    demonstrate_runtime_non_enforcement()

if __name__ == "__main__":
    main()
