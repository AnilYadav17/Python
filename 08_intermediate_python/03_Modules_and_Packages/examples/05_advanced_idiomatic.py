"""
05_advanced_idiomatic.py
Demonstrates advanced modular design patterns:
- Dynamic module loading using importlib
- Building a lightweight plugin registry
- Combinatoric constraint solving with itertools.product and permutations
"""

import importlib
import itertools

# 1. Dynamic Module / Plugin Loader
class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, handler_callable):
        self.plugins[name] = handler_callable

    def execute(self, name, *args, **kwargs):
        if name not in self.plugins:
            raise KeyError(f"Plugin '{name}' is not registered.")
        return self.plugins[name](*args, **kwargs)

    def load_built_in_math_plugin(self):
        # Dynamically imports 'math' module at runtime via importlib
        math_mod = importlib.import_module("math")
        self.register_plugin("sqrt", math_mod.sqrt)
        self.register_plugin("factorial", math_mod.factorial)


# 2. Combinatoric Problem Solver with itertools
def solve_cryptarithm_sample():
    """
    Finds unique digits (0-9) for letters A, B, C such that:
    AB + BC == 100 (where A, B, C are distinct non-zero digits)
    """
    digits = range(1, 10)
    solutions = []

    # itertools.permutations generates all non-repeating digit arrangements
    for a, b, c in itertools.permutations(digits, 3):
        ab = a * 10 + b
        bc = b * 10 + c
        if ab + bc == 100:
            solutions.append((a, b, c))

    return solutions


def main():
    print("--- 1. Dynamic Plugin Management via importlib ---")
    mgr = PluginManager()
    mgr.load_built_in_math_plugin()
    print(f"Registered plugins: {list(mgr.plugins.keys())}")
    print(f"Execute sqrt(144): {mgr.execute('sqrt', 144)}")
    print(f"Execute factorial(6): {mgr.execute('factorial', 6)}")

    print("\n--- 2. Combinatorics with itertools.permutations ---")
    solutions = solve_cryptarithm_sample()
    print(f"Solutions for AB + BC == 100 with distinct digits:")
    for a, b, c in solutions:
        print(f"  A={a}, B={b}, C={c} -> {a}{b} + {b}{c} == 100")

if __name__ == "__main__":
    main()
